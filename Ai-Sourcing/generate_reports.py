# !/usr/bin/env python3
"""
FluxGen Report Generation System
Export supplier data to CSV, JSON, and generate reports
"""

import sqlite3
import csv
import json
from datetime import datetime
from typing import Dict, List, Optional
import argparse
from pathlib import Path


class ReportGenerator:
    """Generate reports and export supplier data"""

    def __init__(self, db_path: str = "/Users/pratikjhaveri/FluxGen/data/fluxgen.db"):
        self.db_path = db_path
        self.conn = None
        self.cursor = None
        self.output_dir = Path("/Users/pratikjhaveri/FluxGen/reports")
        self.output_dir.mkdir(exist_ok=True)

    def connect(self):
        """Connect to database"""
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def export_suppliers_csv(self, output_file: str = None, material: str = None) -> str:
        """Export suppliers to CSV"""

        # Build query
        if material:
            query = "SELECT * FROM suppliers WHERE materials_supplied LIKE ? ORDER BY company_name"
            self.cursor.execute(query, (f'%{material}%',))
        else:
            query = "SELECT * FROM suppliers ORDER BY company_name"
            self.cursor.execute(query)

        suppliers = [dict(row) for row in self.cursor.fetchall()]

        if not suppliers:
            print("❌ No suppliers found")
            return None

        # Generate filename if not provided
        if not output_file:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            material_suffix = f"_{material.replace(' ', '_')}" if material else ""
            output_file = self.output_dir / f"suppliers{material_suffix}_{timestamp}.csv"
        else:
            output_file = Path(output_file)

        # Write CSV
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            if suppliers:
                writer = csv.DictWriter(f, fieldnames=suppliers[0].keys())
                writer.writeheader()
                writer.writerows(suppliers)

        print(f"✅ Exported {len(suppliers)} suppliers to: {output_file}")
        return str(output_file)

    def export_suppliers_json(self, output_file: str = None, material: str = None) -> str:
        """Export suppliers to JSON"""

        # Build query
        if material:
            query = "SELECT * FROM suppliers WHERE materials_supplied LIKE ? ORDER BY company_name"
            self.cursor.execute(query, (f'%{material}%',))
        else:
            query = "SELECT * FROM suppliers ORDER BY company_name"
            self.cursor.execute(query)

        suppliers = [dict(row) for row in self.cursor.fetchall()]

        if not suppliers:
            print("❌ No suppliers found")
            return None

        # Generate filename if not provided
        if not output_file:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            material_suffix = f"_{material.replace(' ', '_')}" if material else ""
            output_file = self.output_dir / f"suppliers{material_suffix}_{timestamp}.json"
        else:
            output_file = Path(output_file)

        # Write JSON
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(suppliers, f, indent=2, default=str)

        print(f"✅ Exported {len(suppliers)} suppliers to: {output_file}")
        return str(output_file)

    def generate_supplier_summary_report(self, output_file: str = None) -> str:
        """Generate comprehensive supplier summary report"""

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        if not output_file:
            output_file = self.output_dir / f"supplier_summary_{timestamp}.txt"
        else:
            output_file = Path(output_file)

        # Gather statistics
        stats = self._gather_statistics()

        # Generate report
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("FLUXGEN SUPPLIER DATABASE SUMMARY REPORT\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 80 + "\n\n")

            # Overall statistics
            f.write("OVERALL STATISTICS\n")
            f.write("-" * 80 + "\n")
            f.write(f"Total Suppliers: {stats['total_suppliers']}\n")
            f.write(f"Total Equipment Items: {stats['total_equipment']}\n")
            f.write(f"Total Raw Materials: {stats['total_materials']}\n")
            f.write(f"Suppliers with Contact Info: {stats['suppliers_with_email']}\n")
            f.write(f"Suppliers with Websites: {stats['suppliers_with_website']}\n")
            f.write("\n")

            # By country
            f.write("SUPPLIERS BY COUNTRY\n")
            f.write("-" * 80 + "\n")
            for country, count in stats['by_country']:
                f.write(f"  {country:.<40} {count:>5}\n")
            f.write("\n")

            # By type
            f.write("SUPPLIERS BY TYPE\n")
            f.write("-" * 80 + "\n")
            for stype, count in stats['by_type']:
                f.write(f"  {stype:.<40} {count:>5}\n")
            f.write("\n")

            # By status
            f.write("SUPPLIERS BY STATUS\n")
            f.write("-" * 80 + "\n")
            for status, count in stats['by_status']:
                f.write(f"  {status:.<40} {count:>5}\n")
            f.write("\n")

            # Top materials
            f.write("TOP 10 MATERIALS BY SUPPLIER COUNT\n")
            f.write("-" * 80 + "\n")
            for material, count in stats['top_materials'][:10]:
                f.write(f"  {material:.<40} {count:>5} suppliers\n")
            f.write("\n")

            # Search history summary
            f.write("SEARCH HISTORY SUMMARY\n")
            f.write("-" * 80 + "\n")
            f.write(f"Total Searches: {stats['total_searches']}\n")
            f.write(f"Average Results per Search: {stats['avg_results_per_search']:.1f}\n")
            if stats['recent_searches']:
                f.write(f"\nRecent Searches (Last 10):\n")
                for search in stats['recent_searches']:
                    f.write(f"  {search['search_date']}: {search['search_query']}")
                    f.write(f" ({search['num_results']} results)\n")
            f.write("\n")

            # Research queue status
            f.write("RESEARCH QUEUE STATUS\n")
            f.write("-" * 80 + "\n")
            f.write(f"Pending Items: {stats['queue_pending']}\n")
            f.write(f"Completed Items: {stats['queue_completed']}\n")
            f.write(f"Total Items: {stats['queue_total']}\n")

        print(f"✅ Generated summary report: {output_file}")
        return str(output_file)

    def _gather_statistics(self) -> Dict:
        """Gather statistics from database"""

        stats = {}

        # Total suppliers
        self.cursor.execute("SELECT COUNT(*) as count FROM suppliers")
        stats['total_suppliers'] = self.cursor.fetchone()['count']

        # Total equipment and materials
        self.cursor.execute("SELECT COUNT(*) as count FROM equipment")
        stats['total_equipment'] = self.cursor.fetchone()['count']

        self.cursor.execute("SELECT COUNT(DISTINCT material_name) as count FROM raw_materials_requirements")
        stats['total_materials'] = self.cursor.fetchone()['count']

        # Suppliers with contact info
        self.cursor.execute("SELECT COUNT(*) as count FROM suppliers WHERE email IS NOT NULL AND email != ''")
        stats['suppliers_with_email'] = self.cursor.fetchone()['count']

        self.cursor.execute("SELECT COUNT(*) as count FROM suppliers WHERE website IS NOT NULL AND website != ''")
        stats['suppliers_with_website'] = self.cursor.fetchone()['count']

        # By country
        self.cursor.execute("""
            SELECT country, COUNT(*) as count 
            FROM suppliers 
            WHERE country IS NOT NULL
            GROUP BY country 
            ORDER BY count DESC
        """)
        stats['by_country'] = [(row['country'], row['count']) for row in self.cursor.fetchall()]

        # By type
        self.cursor.execute("""
            SELECT supplier_type, COUNT(*) as count 
            FROM suppliers 
            GROUP BY supplier_type 
            ORDER BY count DESC
        """)
        stats['by_type'] = [(row['supplier_type'], row['count']) for row in self.cursor.fetchall()]

        # By status
        self.cursor.execute("""
            SELECT status, COUNT(*) as count 
            FROM suppliers 
            GROUP BY status 
            ORDER BY count DESC
        """)
        stats['by_status'] = [(row['status'], row['count']) for row in self.cursor.fetchall()]

        # Top materials
        self.cursor.execute("""
            SELECT materials_supplied, COUNT(*) as count 
            FROM suppliers 
            GROUP BY materials_supplied 
            ORDER BY count DESC
        """)
        stats['top_materials'] = [(row['materials_supplied'], row['count']) for row in self.cursor.fetchall()]

        # Search history
        self.cursor.execute("SELECT COUNT(*) as count FROM supplier_search_history")
        stats['total_searches'] = self.cursor.fetchone()['count']

        self.cursor.execute("SELECT AVG(num_results) as avg FROM supplier_search_history")
        result = self.cursor.fetchone()
        stats['avg_results_per_search'] = result['avg'] if result['avg'] else 0

        self.cursor.execute("""
            SELECT search_date, search_query, num_results 
            FROM supplier_search_history 
            ORDER BY search_date DESC 
            LIMIT 10
        """)
        stats['recent_searches'] = [dict(row) for row in self.cursor.fetchall()]

        # Research queue
        self.cursor.execute("SELECT COUNT(*) as count FROM research_queue WHERE status = 'pending'")
        stats['queue_pending'] = self.cursor.fetchone()['count']

        self.cursor.execute("SELECT COUNT(*) as count FROM research_queue WHERE status = 'completed'")
        stats['queue_completed'] = self.cursor.fetchone()['count']

        self.cursor.execute("SELECT COUNT(*) as count FROM research_queue")
        stats['queue_total'] = self.cursor.fetchone()['count']

        return stats

    def generate_material_report(self, material: str, output_file: str = None) -> str:
        """Generate detailed report for specific material"""

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        material_clean = material.replace(' ', '_')

        if not output_file:
            output_file = self.output_dir / f"material_report_{material_clean}_{timestamp}.txt"
        else:
            output_file = Path(output_file)

        # Get suppliers for this material
        self.cursor.execute("""
            SELECT * FROM suppliers 
            WHERE materials_supplied LIKE ?
            ORDER BY country, company_name
        """, (f'%{material}%',))

        suppliers = [dict(row) for row in self.cursor.fetchall()]

        if not suppliers:
            print(f"❌ No suppliers found for material: {material}")
            return None

        # Generate report
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write(f"SUPPLIER REPORT: {material.upper()}\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 80 + "\n\n")

            f.write(f"Total Suppliers Found: {len(suppliers)}\n\n")

            # Group by country
            by_country = {}
            for supplier in suppliers:
                country = supplier['country'] or 'Unknown'
                if country not in by_country:
                    by_country[country] = []
                by_country[country].append(supplier)

            # Write details
            for country, country_suppliers in sorted(by_country.items()):
                f.write(f"\n{country.upper()}\n")
                f.write("-" * 80 + "\n")

                for supplier in country_suppliers:
                    f.write(f"\n{supplier['company_name']}\n")
                    f.write(f"  Type: {supplier['supplier_type']}\n")
                    f.write(f"  Status: {supplier['status']}\n")

                    if supplier['website']:
                        f.write(f"  Website: {supplier['website']}\n")
                    if supplier['email']:
                        f.write(f"  Email: {supplier['email']}\n")
                    if supplier['phone']:
                        f.write(f"  Phone: {supplier['phone']}\n")

                    if supplier['city'] or supplier['province_state']:
                        location = ", ".join(filter(None, [supplier['city'], supplier['province_state']]))
                        f.write(f"  Location: {location}\n")

                    if supplier['notes']:
                        f.write(f"  Notes: {supplier['notes'][:100]}...\n")

        print(f"✅ Generated material report: {output_file}")
        return str(output_file)

    def export_research_queue_csv(self, output_file: str = None) -> str:
        """Export research queue to CSV"""

        self.cursor.execute("SELECT * FROM research_queue ORDER BY priority DESC, status")
        items = [dict(row) for row in self.cursor.fetchall()]

        if not items:
            print("❌ Research queue is empty")
            return None

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        if not output_file:
            output_file = self.output_dir / f"research_queue_{timestamp}.csv"
        else:
            output_file = Path(output_file)

        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=items[0].keys())
            writer.writeheader()
            writer.writerows(items)

        print(f"✅ Exported research queue ({len(items)} items) to: {output_file}")
        return str(output_file)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='FluxGen Report Generation System')

    parser.add_argument('--csv', action='store_true', help='Export suppliers to CSV')
    parser.add_argument('--json', action='store_true', help='Export suppliers to JSON')
    parser.add_argument('--summary', action='store_true', help='Generate summary report')
    parser.add_argument('--material', type=str, help='Filter by material (for CSV/JSON/detailed report)')
    parser.add_argument('--material-report', action='store_true', help='Generate detailed material report')
    parser.add_argument('--queue', action='store_true', help='Export research queue')
    parser.add_argument('--output', type=str, help='Output file path')
    parser.add_argument('--all', action='store_true', help='Generate all reports')

    args = parser.parse_args()

    with ReportGenerator() as generator:
        generated_files = []

        if args.all or args.csv:
            file_path = generator.export_suppliers_csv(
                output_file=args.output,
                material=args.material
            )
            if file_path:
                generated_files.append(file_path)

        if args.all or args.json:
            file_path = generator.export_suppliers_json(
                output_file=args.output if not args.csv else None,
                material=args.material
            )
            if file_path:
                generated_files.append(file_path)

        if args.all or args.summary:
            file_path = generator.generate_supplier_summary_report(
                output_file=args.output if not (args.csv or args.json) else None
            )
            if file_path:
                generated_files.append(file_path)

        if args.material_report and args.material:
            file_path = generator.generate_material_report(
                material=args.material,
                output_file=args.output
            )
            if file_path:
                generated_files.append(file_path)

        if args.all or args.queue:
            file_path = generator.export_research_queue_csv(
                output_file=args.output if len(generated_files) == 0 else None
            )
            if file_path:
                generated_files.append(file_path)

        if not any([args.csv, args.json, args.summary, args.material_report, args.queue, args.all]):
            print(
                "❌ Please specify at least one action (--csv, --json, --summary, --material-report, --queue, or --all)")
            parser.print_help()
        elif generated_files:
            print(f"\n{'=' * 80}")
            print(f"✅ REPORT GENERATION COMPLETE")
            print(f"{'=' * 80}")
            print(f"Generated {len(generated_files)} file(s):")
            for file_path in generated_files:
                print(f"  📄 {file_path}")
            print()


if __name__ == "__main__":
    main()