# !/usr/bin/env python3
"""
FluxGen Automated Supplier Search System
Main automation script for finding and ranking suppliers
"""

import sqlite3
import json
import re
import os
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Tuple
import argparse
from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class SupplierSearchAutomation:
    """Main automation engine for supplier research"""

    def __init__(self, db_path: str = "/Users/pratikjhaveri/FluxGen/data/fluxgen.db"):
        self.db_path = db_path
        self.conn = None
        self.cursor = None
        
        # Initialize Anthropic client
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment variables")
        self.client = Anthropic(api_key=api_key)

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

    def get_pending_items(self, limit: int = 5) -> List[Dict]:
        """Get items from research queue that need searching"""
        query = """
            SELECT *
            FROM research_queue
            WHERE status = 'pending'
              AND (next_research_date IS NULL OR next_research_date <= date('now'))
              AND num_suppliers_found < target_suppliers
            ORDER BY priority DESC, estimated_cost DESC
            LIMIT ?
        """
        self.cursor.execute(query, (limit,))
        return [dict(row) for row in self.cursor.fetchall()]

    def build_search_query(self, item: Dict) -> str:
        """Build optimized search query for supplier"""
        item_name = item['item_name']
        item_type = item['item_type']
        category = item.get('item_category', '')

        # Build query based on item type
        if item_type == 'equipment':
            # Equipment: Focus on manufacturers and industrial suppliers
            query = f"{item_name} suppliers manufacturers industrial"
        elif item_type == 'material':
            # Raw materials: Focus on bulk suppliers and distributors
            query = f"{item_name} bulk suppliers distributor industrial grade"
        else:
            query = f"{item_name} suppliers"

        return query

    def perform_web_search(self, query: str, max_results: int = 10) -> Tuple[List[Dict], str]:
        """
        Perform web search using Claude with web_search tool

        Returns:
            Tuple of (search_results, raw_response)
        """
        print(f"🔍 Searching: {query}")
        
        try:
            # Call Claude API with web_search tool
            response = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=4096,
                tools=[{"type": "web_search_tool_20241209"}],
                messages=[{
                    "role": "user",
                    "content": f"""Search the web for: {query}
                    
                    Return the results as a JSON array with objects containing:
                    - title: company/page title
                    - url: website URL
                    - snippet: description/snippet
                    - domain: domain name
                    
                    Focus on finding actual supplier companies, manufacturers, or distributors.
                    Skip general information pages, news articles, or non-supplier content.
                    
                    Return ONLY the JSON array, no other text."""
                }]
            )
            
            # Parse the response
            search_results = []
            raw_content = ""
            
            for block in response.content:
                if block.type == "text":
                    raw_content += block.text
                    # Try to parse JSON from text
                    try:
                        # Look for JSON array in the response
                        text = block.text.strip()
                        if text.startswith('['):
                            search_results = json.loads(text)
                        else:
                            # Try to find JSON within the text
                            import re
                            json_match = re.search(r'\[.*\]', text, re.DOTALL)
                            if json_match:
                                search_results = json.loads(json_match.group())
                    except json.JSONDecodeError:
                        print(f"   ⚠️  Could not parse JSON from response")
                        
            print(f"   ✅ Found {len(search_results)} results")
            return search_results[:max_results], raw_content
            
        except Exception as e:
            print(f"   ❌ Search error: {e}")
            return [], str(e)

    def extract_supplier_info(self, search_result: Dict) -> Optional[Dict]:
        """Extract supplier information from search result"""

        # Extract company name from title
        title = search_result.get('title', '')
        company_name = self._extract_company_name(title)

        if not company_name:
            return None

        # Extract website
        website = search_result.get('url', '')
        domain = search_result.get('domain', '')
        
        # If domain not provided, extract from URL
        if not domain and website:
            from urllib.parse import urlparse
            parsed = urlparse(website)
            domain = parsed.netloc

        # Extract snippet info
        snippet = search_result.get('snippet', '')

        # Try to extract location from snippet
        location_info = self._extract_location(snippet)

        # Determine supplier type based on location
        country = location_info.get('country', 'Unknown')
        if country in ['USA', 'Canada']:
            supplier_type = 'Local'
        elif country == 'Unknown':
            supplier_type = 'Distributor'  # Default for unknown locations
        else:
            supplier_type = 'Import'

        supplier_data = {
            'company_name': company_name,
            'website': website,
            'address_line1': None,
            'city': location_info.get('city'),
            'province_state': location_info.get('state'),
            'country': country,
            'postal_code': None,
            'contact_person': None,
            'phone': self._extract_phone(snippet),
            'email': self._extract_email(snippet),
            'materials_supplied': '',  # Will be set by caller
            'supplier_type': supplier_type,  # Must be: Local, Regional, Import, or Distributor
            'priority': 'Secondary',
            'status': 'Prospect',
            'notes': f"Found via web search: {snippet[:200]}",
            'source_url': website,
            'search_rank': None  # Will be set by caller
        }

        return supplier_data

    def _extract_company_name(self, title: str) -> Optional[str]:
        """Extract company name from title"""
        # Remove common suffixes
        title = re.sub(r'\s*[-–|]\s*.*$', '', title)

        # Clean up
        title = title.strip()

        # Skip if too short or looks like a generic title
        if len(title) < 3 or title.lower() in ['home', 'about', 'contact']:
            return None

        return title

    def _extract_location(self, text: str) -> Dict:
        """Extract location information from text"""
        location = {}

        # Common US states
        us_states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California',
                     'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia',
                     'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
                     'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
                     'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska',
                     'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
                     'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
                     'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
                     'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
                     'West Virginia', 'Wisconsin', 'Wyoming']

        # Canadian provinces
        ca_provinces = ['Alberta', 'British Columbia', 'Manitoba', 'New Brunswick',
                        'Newfoundland and Labrador', 'Northwest Territories', 'Nova Scotia',
                        'Nunavut', 'Ontario', 'Prince Edward Island', 'Quebec',
                        'Saskatchewan', 'Yukon']

        # Check for states/provinces
        for state in us_states:
            if state in text or state.upper() in text:
                location['state'] = state
                location['country'] = 'USA'
                break

        for province in ca_provinces:
            if province in text or province.upper() in text:
                location['state'] = province
                location['country'] = 'Canada'
                break

        # Check for country mentions
        if 'Canada' in text or 'Canadian' in text:
            location['country'] = 'Canada'
        elif 'USA' in text or 'United States' in text or 'American' in text:
            location['country'] = 'USA'
        elif 'China' in text or 'Chinese' in text:
            location['country'] = 'China'
        elif 'India' in text or 'Indian' in text:
            location['country'] = 'India'

        return location

    def _extract_phone(self, text: str) -> Optional[str]:
        """Extract phone number from text"""
        # Common phone patterns
        patterns = [
            r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',  # 123-456-7890
            r'\(\d{3}\)\s*\d{3}[-.]?\d{4}',  # (123) 456-7890
            r'\+\d{1,3}\s*\d{3}[-.]?\d{3}[-.]?\d{4}',  # +1 123-456-7890
        ]

        for pattern in patterns:
            match = re.search(pattern, text)
            if match:
                return match.group()

        return None

    def _extract_email(self, text: str) -> Optional[str]:
        """Extract email from text"""
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        match = re.search(pattern, text)
        if match:
            return match.group()
        return None

    def save_supplier(self, supplier_data: Dict) -> int:
        """Save supplier to database"""

        # Check if supplier already exists
        self.cursor.execute(
            "SELECT id FROM suppliers WHERE company_name = ? OR website = ?",
            (supplier_data['company_name'], supplier_data['website'])
        )
        existing = self.cursor.fetchone()

        if existing:
            print(f"   ⚠️  Supplier already exists: {supplier_data['company_name']}")
            return existing['id']

        # Insert new supplier
        fields = [
            'company_name', 'contact_person', 'phone', 'email', 'website',
            'address_line1', 'city', 'province_state', 'country', 'postal_code',
            'materials_supplied', 'supplier_type', 'priority', 'notes', 'status'
        ]

        values = [supplier_data.get(f) for f in fields]
        placeholders = ','.join(['?'] * len(fields))

        query = f"""
            INSERT INTO suppliers ({','.join(fields)})
            VALUES ({placeholders})
        """

        self.cursor.execute(query, values)
        supplier_id = self.cursor.lastrowid

        print(f"   ✅ Saved supplier: {supplier_data['company_name']} (ID: {supplier_id})")

        return supplier_id

    def log_search(self, item: Dict, query: str, num_results: int, notes: str = None):
        """Log search in supplier_search_history"""
        self.cursor.execute("""
            INSERT INTO supplier_search_history 
            (equipment_id, material_name, search_query, search_date, num_results, search_engine, notes)
            VALUES (?, ?, ?, date('now'), ?, 'brave', ?)
        """, (
            item.get('item_id') if item['item_type'] == 'equipment' else None,
            item['item_name'] if item['item_type'] == 'material' else None,
            query,
            num_results,
            notes
        ))

    def update_research_queue(self, item_id: int, num_suppliers_found: int):
        """Update research queue after search"""
        self.cursor.execute("""
            UPDATE research_queue
            SET 
                status = CASE 
                    WHEN num_suppliers_found + ? >= target_suppliers THEN 'completed'
                    ELSE 'pending'
                END,
                num_suppliers_found = num_suppliers_found + ?,
                last_researched = date('now'),
                next_research_date = date('now', '+' || research_frequency_days || ' days'),
                updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (num_suppliers_found, num_suppliers_found, item_id))

    def run_search_for_item(self, item: Dict, max_suppliers: int = 5) -> int:
        """Run complete search workflow for one item"""

        print(f"\n{'=' * 80}")
        print(f"🔎 SEARCHING: {item['item_name']} ({item['item_type']})")
        print(f"   Priority: {item['priority']} | Target: {item['target_suppliers']} suppliers")
        print(f"   Already found: {item['num_suppliers_found']} suppliers")
        print(f"{'=' * 80}")

        # Build search query
        search_query = self.build_search_query(item)
        print(f"\n📝 Query: {search_query}")

        # Perform web search
        search_results, raw_response = self.perform_web_search(search_query, max_results=max_suppliers)

        # Process results
        suppliers_saved = 0
        for rank, result in enumerate(search_results[:max_suppliers], 1):
            supplier_data = self.extract_supplier_info(result)

            if supplier_data:
                # Add item-specific data
                supplier_data['materials_supplied'] = item['item_name']
                supplier_data['search_rank'] = rank

                # Save to database
                try:
                    self.save_supplier(supplier_data)
                    suppliers_saved += 1
                except Exception as e:
                    print(f"   ❌ Error saving supplier: {e}")

        # Log search
        self.log_search(
            item,
            search_query,
            len(search_results),
            f"Saved {suppliers_saved} new suppliers"
        )

        # Update research queue
        self.update_research_queue(item['id'], suppliers_saved)

        print(f"\n✅ Completed: Found {len(search_results)} results, saved {suppliers_saved} new suppliers")

        return suppliers_saved

    def run_daily_batch(self, batch_size: int = 5):
        """Run daily batch of searches"""

        print(f"\n{'#' * 80}")
        print(f"# FluxGen Automated Supplier Search")
        print(f"# {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'#' * 80}\n")

        # Get pending items
        items = self.get_pending_items(limit=batch_size)

        if not items:
            print("✅ No pending items in research queue!")
            return

        print(f"📋 Found {len(items)} items to research\n")

        # Process each item
        total_suppliers = 0
        for i, item in enumerate(items, 1):
            try:
                suppliers_found = self.run_search_for_item(item)
                total_suppliers += suppliers_found
            except Exception as e:
                print(f"❌ ERROR processing {item['item_name']}: {e}")

        # Summary
        print(f"\n{'#' * 80}")
        print(f"# BATCH COMPLETE")
        print(f"# Processed: {len(items)} items")
        print(f"# Total new suppliers: {total_suppliers}")
        print(f"{'#' * 80}\n")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description='FluxGen Supplier Search Automation')
    parser.add_argument('--item', type=str, help='Search for specific item name')
    parser.add_argument('--batch-size', type=int, default=5, help='Number of items to process')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be searched without executing')

    args = parser.parse_args()

    with SupplierSearchAutomation() as automation:
        if args.dry_run:
            print("🔍 DRY RUN MODE - Showing pending items:\n")
            items = automation.get_pending_items(limit=args.batch_size)
            for i, item in enumerate(items, 1):
                query = automation.build_search_query(item)
                print(f"{i}. {item['item_name']} ({item['item_type']})")
                print(f"   Query: {query}")
                print(
                    f"   Priority: {item['priority']} | Found: {item['num_suppliers_found']}/{item['target_suppliers']}")
                print()
        else:
            automation.run_daily_batch(batch_size=args.batch_size)


if __name__ == "__main__":
    main()