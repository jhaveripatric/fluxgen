"""
Test script to debug PDF generation issues
Run this from PyCharm debugger to isolate problems
"""
import sys
from pathlib import Path

# Add repo/app to path
sys.path.insert(0, str(Path(__file__).parent / 'repo' / 'app'))

from generators.executive_summary import ExecutiveSummaryGenerator
from generators.team_bios import TeamBiosGenerator
from generators.market_analysis import MarketAnalysisGenerator
from generators.technical_specs import TechnicalSpecsGenerator

# Import database manager
import sqlite3
import os

class SimpleDatabaseManager:
    """Simplified database manager for testing"""
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row

    def get_company_info(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM company_info LIMIT 1")
        row = cursor.fetchone()
        return dict(row) if row else {}

    def get_team_members(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM team_members")
        return [dict(row) for row in cursor.fetchall()]

    def get_production_targets(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM production_targets")
        return [dict(row) for row in cursor.fetchall()]

    def get_investment_capex(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM investment_capex")
        return [dict(row) for row in cursor.fetchall()]

    def get_financial_summary(self):
        """Calculate financial summary from investment_capex table"""
        cursor = self.conn.cursor()

        # Check if financial_summary table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='financial_summary'")
        if cursor.fetchone():
            cursor.execute("SELECT * FROM financial_summary LIMIT 1")
            row = cursor.fetchone()
            if row:
                return dict(row)

        # Calculate from investment_capex if financial_summary doesn't exist
        cursor.execute("SELECT SUM(estimated_cost_cad) as total_capex FROM investment_capex")
        row = cursor.fetchone()
        total_capex = row[0] if row and row[0] else 0

        return {
            'total_capex': total_capex,
            'pilot_capex': total_capex,  # Simplified for now
            'total_revenue_projection': 0,
            'total_operating_expenses': 0
        }

    def get_funding_programs(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM funding_programs")
        return [dict(row) for row in cursor.fetchall()]

    def get_alloys_catalog(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM alloys_catalog")
        return [dict(row) for row in cursor.fetchall()]

    def get_certifications_roadmap(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM certifications_roadmap")
        return [dict(row) for row in cursor.fetchall()]


def test_executive_summary():
    """Test Executive Summary generation"""
    print("\n" + "="*60)
    print("Testing Executive Summary Generation")
    print("="*60)

    db_path = Path(__file__).parent / 'data' / 'fluxgen.db'
    output_dir = Path(__file__).parent / 'output'
    output_dir.mkdir(exist_ok=True)

    db = SimpleDatabaseManager(str(db_path))

    try:
        generator = ExecutiveSummaryGenerator(db, output_dir)
        pdf_path = generator.generate()
        print(f"✓ SUCCESS: Executive Summary generated at: {pdf_path}")
        return True
    except Exception as e:
        print(f"✗ FAILED: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_team_bios():
    """Test Team Bios generation"""
    print("\n" + "="*60)
    print("Testing Team Bios Generation")
    print("="*60)

    db_path = Path(__file__).parent / 'data' / 'fluxgen.db'
    output_dir = Path(__file__).parent / 'output'
    output_dir.mkdir(exist_ok=True)

    db = SimpleDatabaseManager(str(db_path))

    try:
        generator = TeamBiosGenerator(db, output_dir)
        pdf_path = generator.generate()
        print(f"✓ SUCCESS: Team Bios generated at: {pdf_path}")
        return True
    except Exception as e:
        print(f"✗ FAILED: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_market_analysis():
    """Test Market Analysis generation"""
    print("\n" + "="*60)
    print("Testing Market Analysis Generation")
    print("="*60)

    db_path = Path(__file__).parent / 'data' / 'fluxgen.db'
    output_dir = Path(__file__).parent / 'output'
    output_dir.mkdir(exist_ok=True)

    db = SimpleDatabaseManager(str(db_path))

    try:
        generator = MarketAnalysisGenerator(db, output_dir)
        pdf_path = generator.generate()
        print(f"✓ SUCCESS: Market Analysis generated at: {pdf_path}")
        return True
    except Exception as e:
        print(f"✗ FAILED: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_technical_specs():
    """Test Technical Specs generation"""
    print("\n" + "="*60)
    print("Testing Technical Specs Generation")
    print("="*60)

    db_path = Path(__file__).parent / 'data' / 'fluxgen.db'
    output_dir = Path(__file__).parent / 'output'
    output_dir.mkdir(exist_ok=True)

    db = SimpleDatabaseManager(str(db_path))

    try:
        generator = TechnicalSpecsGenerator(db, output_dir)
        pdf_path = generator.generate()
        print(f"✓ SUCCESS: Technical Specs generated at: {pdf_path}")
        return True
    except Exception as e:
        print(f"✗ FAILED: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("FluxGen PDF Generation Debug Test Suite")
    print("="*60)

    results = {
        'Executive Summary': test_executive_summary(),
        'Team Bios': test_team_bios(),
        'Market Analysis': test_market_analysis(),
        'Technical Specs': test_technical_specs()
    }

    print("\n" + "="*60)
    print("Test Results Summary")
    print("="*60)
    for test_name, passed in results.items():
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"{test_name:.<50} {status}")

    total = len(results)
    passed = sum(results.values())
    print(f"\nTotal: {passed}/{total} tests passed")

    return all(results.values())


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
