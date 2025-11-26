"""
Database connection and utilities for FluxGen application
"""
import sqlite3
import json
from pathlib import Path
from contextlib import contextmanager
from typing import Dict, List, Any, Optional


class DatabaseManager:
    """SQLite database manager for FluxGen data"""
    
    def __init__(self, db_path: Path):
        self.db_path = db_path
        
    @contextmanager
    def get_connection(self):
        """Get database connection with automatic cleanup"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Enable dict-like access
        try:
            yield conn
        finally:
            conn.close()
    
    def execute_query(self, query: str, params: tuple = ()) -> List[Dict[str, Any]]:
        """Execute SELECT query and return results as list of dicts"""
        with self.get_connection() as conn:
            cursor = conn.execute(query, params)
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
    
    def execute_update(self, query: str, params: tuple = ()) -> int:
        """Execute INSERT/UPDATE/DELETE query and return affected rows"""
        with self.get_connection() as conn:
            cursor = conn.execute(query, params)
            conn.commit()
            return cursor.rowcount
    
    def get_company_info(self) -> Optional[Dict[str, Any]]:
        """Get company information"""
        result = self.execute_query("SELECT * FROM company_info LIMIT 1")
        return result[0] if result else None
    
    def update_company_info(self, data: Dict[str, Any]) -> bool:
        """Update company information"""
        query = """
        UPDATE company_info SET 
            legal_name = ?, operating_name = ?, location = ?, province = ?, 
            country = ?, incorporation_status = ?, tagline = ?, vision = ?, 
            mission = ?, website = ?, primary_email = ?, primary_phone = ?
        WHERE id = 1
        """
        params = (
            data.get('legal_name'), data.get('operating_name'), data.get('location'),
            data.get('province'), data.get('country'), data.get('incorporation_status'),
            data.get('tagline'), data.get('vision'), data.get('mission'),
            data.get('website'), data.get('primary_email'), data.get('primary_phone')
        )
        return self.execute_update(query, params) > 0
    
    def get_team_members(self) -> List[Dict[str, Any]]:
        """Get all team members"""
        return self.execute_query("SELECT * FROM team_members ORDER BY id")
    
    def get_team_member(self, member_id: int) -> Optional[Dict[str, Any]]:
        """Get specific team member"""
        result = self.execute_query("SELECT * FROM team_members WHERE id = ?", (member_id,))
        return result[0] if result else None
    
    def add_team_member(self, data: Dict[str, Any]) -> int:
        """Add new team member"""
        query = """
        INSERT INTO team_members (name, role, email, phone, address, status, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        params = (
            data.get('name'), data.get('role'), data.get('email'),
            data.get('phone'), data.get('address'), data.get('status', 'active'),
            data.get('notes')
        )
        with self.get_connection() as conn:
            cursor = conn.execute(query, params)
            conn.commit()
            return cursor.lastrowid
    
    def update_team_member(self, member_id: int, data: Dict[str, Any]) -> bool:
        """Update team member"""
        query = """
        UPDATE team_members SET 
            name = ?, role = ?, email = ?, phone = ?, address = ?, status = ?, notes = ?
        WHERE id = ?
        """
        params = (
            data.get('name'), data.get('role'), data.get('email'),
            data.get('phone'), data.get('address'), data.get('status'),
            data.get('notes'), member_id
        )
        return self.execute_update(query, params) > 0
    
    def delete_team_member(self, member_id: int) -> bool:
        """Delete team member"""
        return self.execute_update("DELETE FROM team_members WHERE id = ?", (member_id,)) > 0
    
    def get_investment_capex(self) -> List[Dict[str, Any]]:
        """Get all CAPEX items"""
        return self.execute_query("SELECT * FROM investment_capex ORDER BY phase, category")
    
    def update_capex_item(self, item_id: int, data: Dict[str, Any]) -> bool:
        """Update CAPEX item"""
        query = """
        UPDATE investment_capex SET 
            category = ?, description = ?, estimated_cost_cad = ?, 
            actual_cost_cad = ?, phase = ?, status = ?, notes = ?
        WHERE id = ?
        """
        params = (
            data.get('category'), data.get('description'), data.get('estimated_cost_cad'),
            data.get('actual_cost_cad'), data.get('phase'), data.get('status'),
            data.get('notes'), item_id
        )
        return self.execute_update(query, params) > 0
    
    def get_production_targets(self) -> List[Dict[str, Any]]:
        """Get all production targets"""
        return self.execute_query("SELECT * FROM production_targets ORDER BY phase")
    
    def update_production_target(self, target_id: int, data: Dict[str, Any]) -> bool:
        """Update production target"""
        query = """
        UPDATE production_targets SET 
            phase = ?, output_kg_month = ?, facility_type = ?, 
            process_flow = ?, sourcing_strategy = ?, target_date = ?, status = ?
        WHERE id = ?
        """
        params = (
            data.get('phase'), data.get('output_kg_month'), data.get('facility_type'),
            data.get('process_flow'), data.get('sourcing_strategy'), 
            data.get('target_date'), data.get('status'), target_id
        )
        return self.execute_update(query, params) > 0
    
    def get_alloys_catalog(self) -> List[Dict[str, Any]]:
        """Get alloys catalog"""
        return self.execute_query("SELECT * FROM alloys_catalog ORDER BY alloy_symbol")
    
    def get_funding_programs(self) -> List[Dict[str, Any]]:
        """Get funding programs"""
        return self.execute_query("SELECT * FROM funding_programs ORDER BY program_name")
    
    def get_certifications_roadmap(self) -> List[Dict[str, Any]]:
        """Get certifications roadmap"""
        return self.execute_query("SELECT * FROM certifications_roadmap ORDER BY phase, target_date")

    def get_business_assumptions(self) -> List[Dict[str, Any]]:
        """Get key business assumptions by phase/category"""
        return self.execute_query(
            "SELECT * FROM business_assumptions ORDER BY phase, category, assumption_name"
        )

    def get_competitors(self) -> List[Dict[str, Any]]:
        """Get competitor list"""
        return self.execute_query("SELECT * FROM competitors ORDER BY company_name")

    def get_competitor_pricing(self) -> List[Dict[str, Any]]:
        """Get competitor pricing benchmarks"""
        return self.execute_query(
            "SELECT * FROM competitor_pricing ORDER BY supplier, flux_name"
        )

    def get_market_analysis(self) -> List[Dict[str, Any]]:
        """Get market analysis metrics"""
        return self.execute_query(
            "SELECT * FROM market_analysis ORDER BY category, metric, year DESC"
        )

    def get_raw_materials(self) -> List[Dict[str, Any]]:
        """Get raw material specifications"""
        return self.execute_query(
            "SELECT * FROM raw_materials ORDER BY material_name, batch_mark"
        )
    
    def get_brand_assets(self) -> List[Dict[str, Any]]:
        """Get brand assets"""
        return self.execute_query("SELECT * FROM brand_assets ORDER BY brand_type")
    
    def get_financial_summary(self) -> Dict[str, Any]:
        """Get financial summary data"""
        # Total estimated CAPEX
        capex_result = self.execute_query(
            "SELECT SUM(estimated_cost_cad) as total_estimated_capex FROM investment_capex"
        )
        total_capex = capex_result[0]['total_estimated_capex'] or 0
        
        # Production capacity
        production_result = self.execute_query(
            "SELECT SUM(output_kg_month) as total_capacity FROM production_targets"
        )
        total_capacity = production_result[0]['total_capacity'] or 0
        
        # Team size
        team_result = self.execute_query(
            "SELECT COUNT(*) as team_size FROM team_members WHERE status = 'active'"
        )
        team_size = team_result[0]['team_size'] or 0
        
        return {
            'total_capex': total_capex,
            'total_capacity': total_capacity,
            'team_size': team_size
        }
