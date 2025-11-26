"""
Executive Summary document generator for FluxGen
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.base import BaseDocumentGenerator
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class ExecutiveSummaryGenerator(BaseDocumentGenerator):
    """Generates Executive Summary document (1-2 pages)"""
    
    def __init__(self, database_manager, output_dir: Path):
        super().__init__(database_manager, output_dir)
    
    def build_content(self):
        """Build executive summary content"""
        # Document title and company header
        self.add_company_header()
        self.add_title("Executive Summary")
        
        # Company Overview
        self._add_company_overview()
        
        # Business Model and Phases
        self._add_business_model()
        
        # Team Overview
        self._add_team_overview()
        
        # Financial Highlights
        self._add_financial_highlights()
        
        # Economic Impact
        self._add_economic_impact()
        
        # Site Requirements Summary
        self._add_site_requirements()
        
        # Next Steps
        self._add_next_steps()
        
        # Footer
        self.add_footer_info()
    
    def _add_company_overview(self):
        """Add company overview section"""
        self.add_heading1("Company Overview")
        
        if self.company_info:
            overview_text = f"""
            {self.company_info.get('legal_name', 'FluxGen Industries Ltd.')} is {self.company_info.get('incorporation_status', 'under formation')} 
            and positioned to become a leading manufacturer of submerged arc welding (SAW) flux and specialty alloys in Western Canada.
            <br/>
            <b>Vision:</b>
{self.company_info.get('vision', 'From molten core to global connection — FluxGen powers the world\'s welds')}
            <br/>
            <b>Mission:</b> {self.company_info.get('mission', 'Localize production, reduce import dependency, and promote innovation in welding materials')}
            <br/>
            Located in {self.company_info.get('location', 'Airdrie')}, {self.company_info.get('province', 'Alberta')}, 
            FluxGen will address the critical supply chain gaps in the North American welding materials market while supporting 
            local economic development and job creation.
            """
        else:
            overview_text = """
            FluxGen Industries Ltd. is under formation and positioned to become a leading manufacturer of submerged arc welding (SAW) 
            flux and specialty alloys in Western Canada. The company addresses critical supply chain gaps in the North American 
            welding materials market while supporting local economic development and job creation.
            """
        
        self.add_body_text(overview_text)
        self.add_spacer()
    
    def _add_business_model(self):
        """Add business model and phases"""
        self.add_heading1("Business Model & Development Phases")
        
        # Get production targets for phases
        production_targets = self.db.get_production_targets()
        
        if production_targets:
            phases_data = [['Phase', 'Output (kg/month)', 'Facility Type', 'Key Focus']]
            
            for target in production_targets:
                phases_data.append([
                    target.get('phase', 'N/A'),
                    f"{target.get('output_kg_month', 0):,}" if target.get('output_kg_month') else 'N/A',
                    target.get('facility_type', 'N/A'),
                    target.get('sourcing_strategy', 'N/A')
                ])
            
            self.add_table(phases_data, [1.5, 1.5, 2.0, 2.5], title="Development Phases")
        
        business_model_text = """
        FluxGen operates on a phased approach to market entry and scaling:
        <br/>
        • <b>Pilot Phase:</b> Establish manufacturing capabilities, validate product quality, and build initial customer base
        <br/>
        • <b>Scale-Up Phase:</b> Expand production capacity, automate processes, and capture larger market share
        <br/>
        • <b>Full Production:</b> Achieve optimal production efficiency and market leadership in Western Canada
        <br/>
        The business model emphasizes local sourcing (80-90% Canada-based raw materials), quality manufacturing, 
        and strong customer relationships in the oil & gas, infrastructure, and manufacturing sectors.
        """
        
        self.add_body_text(business_model_text)
        self.add_spacer()
    
    def _add_team_overview(self):
        """Add team overview section"""
        self.add_heading1("Management Team")
        
        team_members = self.db.get_team_members()
        
        if team_members:
            team_data = [['Name', 'Role', 'Contact']]
            
            for member in team_members:
                contact_info = []
                if member.get('email'):
                    contact_info.append(member['email'])
                if member.get('phone'):
                    contact_info.append(member['phone'])
                
                team_data.append([
                    member.get('name', 'N/A'),
                    member.get('role', 'N/A'),
                    ' | '.join(contact_info) if contact_info else 'N/A'
                ])
            
            self.add_table(team_data, [2.0, 2.5, 2.5], title="Key Personnel")
        
        team_text = """
        The FluxGen management team brings together extensive experience in manufacturing, operations, and supply chain management. 
        The leadership team has a proven track record in scaling industrial operations and building successful businesses in 
        competitive markets.
        
        The team's combined expertise in metallurgy, manufacturing processes, business development, and financial management 
        positions FluxGen for successful execution of its business plan and achievement of operational milestones.
        """
        
        self.add_body_text(team_text)
        self.add_spacer()
    
    def _add_financial_highlights(self):
        """Add financial highlights section"""
        self.add_heading1("Financial Highlights")
        
        # Get CAPEX data
        capex_items = self.db.get_investment_capex()
        financial_summary = self.db.get_financial_summary()
        
        # Calculate phase totals
        pilot_capex = sum(item.get('estimated_cost_cad', 0) for item in capex_items 
                         if item.get('phase') == 'pilot')
        total_capex = financial_summary.get('total_capex', 0)
        
        financial_data = [
            ['Investment Category', 'Pilot Phase', 'Total Estimated'],
            ['Total CAPEX Investment', self.format_currency(pilot_capex), self.format_currency(total_capex)],
            ['Production Capacity', '500 kg/month', '5,000+ kg/month'],
            ['Target Markets', 'Alberta', 'Western Canada'],
            ['Raw Material Sourcing', '80% Canadian', '90% Canadian']
        ]
        
        self.add_table(financial_data, [2.0, 1.8, 1.8], title="Investment Overview")
        
        funding_programs = self.db.get_funding_programs()
        if funding_programs:
            funding_text = f"""
            <b>Funding Strategy:</b> FluxGen has identified {len(funding_programs)} government funding programs 
            that align with our manufacturing and innovation objectives. These programs support local manufacturing, 
            job creation, and supply chain resilience initiatives.
            
            The company's location in Alberta provides access to significant government support for manufacturing 
            and economic development, potentially reducing the effective investment required from private sources.
            """
            
            self.add_body_text(funding_text)
        
        self.add_spacer()
    
    def _add_economic_impact(self):
        """Add economic impact section"""
        self.add_heading1("Economic Impact")
        
        production_targets = self.db.get_production_targets()
        total_capacity = sum(target.get('output_kg_month', 0) for target in production_targets)
        
        economic_text = f"""
        FluxGen's operations will deliver significant economic benefits to the Airdrie region and Alberta:
        <br/>
        • <b>Job Creation:</b> Direct employment of 15-25 full-time positions across manufacturing, quality control, 
          logistics, and administration
          <br/>
        • <b>Local Sourcing:</b> Prioritizing Canadian suppliers for 80-90% of raw materials, supporting domestic supply chains
        <br/>
        • <b>Manufacturing Capacity:</b> Up to {total_capacity:,} kg/month production capacity at full scale
        <br/>
        • <b>Import Substitution:</b> Reducing dependency on imported welding materials from offshore suppliers
        <br/>
        • <b>Skills Development:</b> Training programs and partnerships with local technical institutions
        <br/>
        • <b>Tax Revenue:</b> Contributing to municipal and provincial tax base through property, corporate, and employment taxes
        <br/>
        The facility will serve as a hub for welding materials innovation and manufacturing excellence in Western Canada.
        """
        
        self.add_body_text(economic_text)
        self.add_spacer()
    
    def _add_site_requirements(self):
        """Add site requirements summary"""
        self.add_heading1("Facility Requirements")
        
        site_text = """
        FluxGen requires a strategic industrial location with the following specifications:
        <br/>
        • <b>Land Area:</b> 10-15 acres for manufacturing facility, raw material storage, and future expansion
        <br/>
        • <b>Utilities:</b> High-capacity electrical service (1-2 MW), natural gas access, reliable water supply
        <br/>
        • <b>Transportation:</b> Highway access for truck transportation, proximity to rail transportation preferred
        <br/>
        • <b>Zoning:</b> Heavy industrial zoning with permits for chemical processing and manufacturing operations
        <br/>
        • <b>Environmental:</b> Compliance with environmental regulations, dust control, and waste management systems
        <br/>
        The Airdrie location provides excellent access to regional markets, transportation infrastructure, 
        and skilled workforce while maintaining competitive operating costs.
        """
        
        self.add_body_text(site_text)
        self.add_spacer()
    
    def _add_next_steps(self):
        """Add next steps section"""
        self.add_heading1("Next Steps & Milestones")
        
        next_steps_text = """
        <b>Immediate Priorities (Next 90 Days):</b>
        <br/>
        • Complete market validation and customer engagement
        <br/>
        • Finalize site selection and facility planning
        <br/>
        • Submit applications for identified government funding programs
        <br/>
        • Complete detailed equipment specifications and vendor selection
        <br/>
        • Advance corporate structure and regulatory compliance
        <br/>
        <b>Phase 1 Implementation (6-12 Months):</b>
        <br/>
        • Secure facility lease/purchase and begin build-out
        <br/>
        • Complete equipment procurement and installation
        <br/>
        • Hire core production and quality control team
        <br/>
        • Obtain necessary permits and certifications
        <br/>
        • Begin pilot production and customer trials
        <br/>
        <b>Long-term Objectives (12-24 Months):</b>
        <br/>
        • Achieve consistent production quality and customer satisfaction
        <br/>
        • Scale operations to meet growing market demand
        <br/>
        • Expand product portfolio and customer base
        <br/>
        • Evaluate opportunities for additional facilities or capabilities
        """
        
        self.add_body_text(next_steps_text)
        self.add_spacer()
    
    def generate(self) -> Path:
        """Generate the Executive Summary PDF"""
        self.story = []  # Reset story
        self.build_content()
        
        filename = f"fluxgen_executive_summary_{self._get_timestamp()}"
        return self.generate_document(filename, "FluxGen Industries - Executive Summary")
    
    def _get_timestamp(self) -> str:
        """Get timestamp for filename"""
        from datetime import datetime
        return datetime.now().strftime('%Y%m%d_%H%M%S')