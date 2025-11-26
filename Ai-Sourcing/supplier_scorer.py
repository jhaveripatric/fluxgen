# !/usr/bin/env python3
"""
FluxGen Supplier Scoring System
Ranks and scores suppliers based on multiple factors
"""

import sqlite3
import json
from typing import Dict, List, Optional
from datetime import datetime
import argparse


class SupplierScorer:
    """Intelligent supplier ranking and scoring system"""

    # Scoring weights (total = 100)
    WEIGHTS = {
        'website_quality': 15,  # Has professional website
        'location': 20,  # Proximity (Canada > USA > International)
        'certifications': 15,  # ISO, quality certs
        'search_rank': 10,  # Position in search results
        'contact_info': 15,  # Complete contact details
        'supplier_type': 10,  # Local > Online > Import
        'pricing_available': 10,  # Has pricing history
        'notes_quality': 5  # Detailed notes/info
    }

    def __init__(self, db_path: str = "/Users/pratikjhaveri/FluxGen/data/fluxgen.db"):
        self.db_path = db_path
        self.conn = None
        self.cursor = None

    def connect(self):
        """Connect to database"""
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.commit()
            self.conn.close()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def score_website_quality(self, supplier: Dict) -> float:
        """Score based on website quality (0-15 points)"""
        score = 0
        website = supplier.get('website', '')

        if not website:
            return 0

        # Has website
        score += 5

        # HTTPS (secure)
        if website.startswith('https://'):
            score += 3

        # Professional domain (not free hosting)
        free_domains = ['.blogspot.', '.wordpress.', '.wix.', '.weebly.']
        if not any(domain in website.lower() for domain in free_domains):
            score += 4

        # Has proper TLD
        good_tlds = ['.com', '.ca', '.net', '.org', '.co']
        if any(website.endswith(tld) for tld in good_tlds):
            score += 3

        return min(score, 15)

    def score_location(self, supplier: Dict) -> float:
        """Score based on location/proximity (0-20 points)"""
        country = supplier.get('country', '').upper()
        supplier_type = supplier.get('supplier_type', '').lower()

        # Canada (highest priority)
        if 'CANADA' in country or 'CA' == country:
            return 20

        # USA (second priority)
        if 'USA' in country or 'US' == country or 'UNITED STATES' in country:
            return 15

        # Local supplier (regardless of country)
        if supplier_type == 'local':
            return 18

        # Online/International
        return 8

    def score_certifications(self, supplier: Dict) -> float:
        """Score based on certifications (0-15 points)"""
        score = 0

        # Check supplier_certifications table
        supplier_id = supplier.get('id')
        if supplier_id:
            self.cursor.execute("""
                SELECT COUNT(*) as cert_count
                FROM supplier_certifications
                WHERE supplier_id = ?
            """, (supplier_id,))

            result = self.cursor.fetchone()
            cert_count = result['cert_count'] if result else 0

            # 5 points per certification, max 15
            score = min(cert_count * 5, 15)

        return score

    def score_search_rank(self, supplier: Dict) -> float:
        """Score based on search ranking (0-10 points)"""
        # Higher rank (lower number) = better score
        # Rank 1 = 10 points, Rank 10 = 1 point

        notes = supplier.get('notes', '')

        # Try to extract search rank from notes
        import re
        match = re.search(r'rank[:\s]+(\d+)', notes, re.IGNORECASE)

        if match:
            rank = int(match.group(1))
            score = max(10 - rank + 1, 0)
            return min(score, 10)

        return 5  # Default/unknown rank

    def score_contact_info(self, supplier: Dict) -> float:
        """Score based on completeness of contact info (0-15 points)"""
        score = 0

        # Email (5 points)
        if supplier.get('email'):
            score += 5

        # Phone (5 points)
        if supplier.get('phone'):
            score += 5

        # Contact person (2 points)
        if supplier.get('contact_person'):
            score += 2

        # Address (3 points)
        if supplier.get('address_line1') or supplier.get('city'):
            score += 3

        return min(score, 15)

    def score_supplier_type(self, supplier: Dict) -> float:
        """Score based on supplier type (0-10 points)"""
        supplier_type = supplier.get('supplier_type', '').lower()

        type_scores = {
            'local': 10,
            'online': 7,
            'import': 5,
            'unknown': 3
        }

        return type_scores.get(supplier_type, 5)

    def score_pricing_available(self, supplier: Dict) -> float:
        """Score based on pricing history (0-10 points)"""
        supplier_id = supplier.get('id')

        if not supplier_id:
            return 0

        # Check if we have pricing history
        self.cursor.execute("""
            SELECT COUNT(*) as price_count
            FROM supplier_pricing_history
            WHERE supplier_id = ?
        """, (supplier_id,))

        result = self.cursor.fetchone()
        price_count = result['price_count'] if result else 0

        if price_count >= 3:
            return 10
        elif price_count >= 1:
            return 7
        else:
            return 0

    def score_notes_quality(self, supplier: Dict) -> float:
        """Score based on quality of notes (0-5 points)"""
        notes = supplier.get('notes', '')

        if not notes:
            return 0

        # Length-based scoring
        if len(notes) > 200:
            return 5
        elif len(notes) > 100:
            return 3
        elif len(notes) > 20:
            return 2
        else:
            return 1

    def calculate_total_score(self, supplier: Dict) -> Dict:
        """Calculate total supplier score with breakdown"""

        scores = {
            'website_quality': self.score_website_quality(supplier),
            'location': self.score_location(supplier),
            'certifications': self.score_certifications(supplier),
            'search_rank': self.score_search_rank(supplier),
            'contact_info': self.score_contact_info(supplier),
            'supplier_type': self.score_supplier_type(supplier),
            'pricing_available': self.score_pricing_available(supplier),
            'notes_quality': self.score_notes_quality(supplier)
        }

        # Calculate total (max 100)
        total = sum(scores.values())

        # Calculate grade
        if total >= 90:
            grade = 'A+'
        elif total >= 80:
            grade = 'A'
        elif total >= 70:
            grade = 'B'
        elif total >= 60:
            grade = 'C'
        elif total >= 50:
            grade = 'D'
        else:
            grade = 'F'

        return {
            'total_score': round(total, 2),
            'grade': grade,
            'breakdown': scores
        }

    def get_all_suppliers(self, material: str = None) -> List[Dict]:
        """Get all suppliers, optionally filtered by material"""

        if material:
            query = "SELECT * FROM suppliers WHERE materials_supplied LIKE ?"
            self.cursor.execute(query, (f'%{material}%',))
        else:
            self.cursor.execute("SELECT * FROM suppliers")

        return [dict(row) for row in self.cursor.fetchall()]

    def score_supplier_by_id(self, supplier_id: int) -> Optional[Dict]:
        """Score a single supplier by ID"""

        self.cursor.execute("SELECT * FROM suppliers WHERE id = ?", (supplier_id,))
        supplier = self.cursor.fetchone()

        if not supplier:
            return None

        supplier_dict = dict(supplier)
        scoring = self.calculate_total_score(supplier_dict)

        return {
            'supplier': supplier_dict,
            'scoring': scoring
        }

    def score_all_suppliers(self, material: str = None, save_to_db: bool = False) -> List[Dict]:
        """Score all suppliers and return ranked list"""

        suppliers = self.get_all_suppliers(material)

        print(f"\n{'=' * 80}")
        print(f"📊 SUPPLIER SCORING REPORT")
        print(f"{'=' * 80}")
        print(f"Total suppliers: {len(suppliers)}")
        if material:
            print(f"Material filter: {material}")
        print(f"{'=' * 80}\n")

        scored_suppliers = []

        for supplier in suppliers:
            scoring = self.calculate_total_score(supplier)

            scored_suppliers.append({
                'id': supplier['id'],
                'company_name': supplier['company_name'],
                'materials_supplied': supplier['materials_supplied'],
                'country': supplier['country'],
                'total_score': scoring['total_score'],
                'grade': scoring['grade'],
                'breakdown': scoring['breakdown'],
                'website': supplier['website']
            })

        # Sort by score (highest first)
        scored_suppliers.sort(key=lambda x: x['total_score'], reverse=True)

        # Display results
        self._display_ranked_suppliers(scored_suppliers)

        # Optionally save scores to database (could add a scoring_history table)
        if save_to_db:
            self._save_scores_to_db(scored_suppliers)

        return scored_suppliers

    def _display_ranked_suppliers(self, scored_suppliers: List[Dict]):
        """Display ranked suppliers in a nice format"""

        print(f"\n{'=' * 80}")
        print(f"🏆 TOP RANKED SUPPLIERS")
        print(f"{'=' * 80}\n")

        for rank, supplier in enumerate(scored_suppliers[:20], 1):  # Top 20
            print(f"{rank:2d}. {supplier['company_name']}")
            print(f"    Score: {supplier['total_score']:.1f}/100 ({supplier['grade']})")
            print(f"    Material: {supplier['materials_supplied']}")
            print(f"    Location: {supplier['country']}")

            # Show top 3 scoring factors
            breakdown = supplier['breakdown']
            top_factors = sorted(breakdown.items(), key=lambda x: x[1], reverse=True)[:3]

            print(f"    Strengths:", end='')
            for factor, score in top_factors:
                if score > 0:
                    print(f" {factor.replace('_', ' ').title()}({score:.0f})", end='')
            print()

            if supplier['website']:
                print(f"    Website: {supplier['website']}")

            print()

    def _save_scores_to_db(self, scored_suppliers: List[Dict]):
        """Save scoring results to database"""
        # This would require a scoring_history table
        # For now, just print a message
        print("\n💾 Saving scores to database...")
        print("   (Scoring history table not yet implemented)")

    def generate_scoring_summary(self) -> Dict:
        """Generate summary statistics of all supplier scores"""

        suppliers = self.get_all_suppliers()

        if not suppliers:
            return {'error': 'No suppliers found'}

        scores = []
        grades = {'A+': 0, 'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}

        for supplier in suppliers:
            scoring = self.calculate_total_score(supplier)
            scores.append(scoring['total_score'])
            grades[scoring['grade']] += 1

        summary = {
            'total_suppliers': len(suppliers),
            'average_score': sum(scores) / len(scores),
            'min_score': min(scores),
            'max_score': max(scores),
            'grade_distribution': grades
        }

        return summary


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='FluxGen Supplier Scoring System')
    parser.add_argument('--material', type=str, help='Filter by material/equipment name')
    parser.add_argument('--supplier-id', type=int, help='Score specific supplier by ID')
    parser.add_argument('--summary', action='store_true', help='Show scoring summary only')
    parser.add_argument('--save', action='store_true', help='Save scores to database')

    args = parser.parse_args()

    with SupplierScorer() as scorer:
        if args.supplier_id:
            # Score single supplier
            result = scorer.score_supplier_by_id(args.supplier_id)
            if result:
                print(f"\n{'=' * 80}")
                print(f"📊 SUPPLIER SCORE CARD")
                print(f"{'=' * 80}")
                print(f"Company: {result['supplier']['company_name']}")
                print(f"Material: {result['supplier']['materials_supplied']}")
                print(f"\nTOTAL SCORE: {result['scoring']['total_score']}/100 ({result['scoring']['grade']})")
                print(f"\nBREAKDOWN:")
                for factor, score in result['scoring']['breakdown'].items():
                    print(f"  {factor.replace('_', ' ').title():.<30} {score:.1f}/{scorer.WEIGHTS[factor]}")
            else:
                print(f"❌ Supplier ID {args.supplier_id} not found")

        elif args.summary:
            # Show summary only
            summary = scorer.generate_scoring_summary()
            print(f"\n{'=' * 80}")
            print(f"📈 SCORING SUMMARY")
            print(f"{'=' * 80}")
            print(f"Total Suppliers: {summary['total_suppliers']}")
            print(f"Average Score: {summary['average_score']:.1f}/100")
            print(f"Score Range: {summary['min_score']:.1f} - {summary['max_score']:.1f}")
            print(f"\nGrade Distribution:")
            for grade, count in summary['grade_distribution'].items():
                pct = (count / summary['total_suppliers']) * 100
                bar = '█' * int(pct / 2)
                print(f"  {grade:3s} : {bar:<50} {count} ({pct:.1f}%)")

        else:
            # Score all suppliers
            scorer.score_all_suppliers(
                material=args.material,
                save_to_db=args.save
            )


if __name__ == "__main__":
    main()