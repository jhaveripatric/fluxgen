"""
Business Plan document generator for FluxGen
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.base import BaseDocumentGenerator
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class BusinessPlanGenerator(BaseDocumentGenerator):
    """Generates comprehensive Business Plan document (8-12 pages)"""
    
    def __init__(self, database_manager, output_dir: Path):
        super().__init__(database_manager, output_dir)
    
    def build_content(self):
        """Build business plan content"""
        # Document title and company header
        self.add_company_header()
        self.add_title("Business Plan")
        
        # Table of Contents would go here in a real implementation
        
        # 1. Executive Summary
        self._add_executive_summary()
        self.add_page_break()
        
        # 2. Company Description
        self._add_company_description()
        
        # 3. Market Analysis
        self._add_market_analysis()
        self.add_page_break()
        
        # 4. Products & Services
        self._add_products_services()
        self.add_page_break()
        
        # 5. Operations Plan
        self._add_operations_plan()
        
        # 6. Management Team
        self._add_management_team()
        self.add_page_break()
        
        # 7. Financial Projections
        self._add_financial_overview()
        
        # 8. Risk Analysis
        self._add_risk_analysis()
        self.add_page_break()
        
        # 9. Implementation Timeline
        self._add_implementation_timeline()
        
        # Footer
        self.add_footer_info()
    
    def _add_executive_summary(self):
        """Add executive summary section"""
        self.add_heading1("Executive Summary")
        
        summary_text = """
        FluxGen Industries Ltd. is establishing a state-of-the-art manufacturing facility in Airdrie, Alberta, 
        to produce submerged arc welding (SAW) flux and specialty alloys for the North American market. 
        <br/>
        <b>Business Opportunity:</b> The Canadian welding materials market relies heavily on imports, creating 
        opportunities for local manufacturers to provide superior products, reduced lead times, and enhanced 
        supply chain reliability.
        <br/>
        <b>Competitive Advantage:</b> Strategic location, experienced management team, focus on quality and 
        customer service, and strong relationships with local raw material suppliers.
        <br/>
        <b>Financial Projections:</b> The business plan outlines a phased approach with initial pilot production 
        of 500 kg/month scaling to 5,000+ kg/month at full capacity.
        <br/>
        <b>Investment Required:</b> Total capital investment estimated at CAD $150,000-$200,000 for pilot phase, 
        with additional funding for scale-up operations.
        <br/>
        <b>Market Opportunity:</b> Targeting oil & gas, infrastructure, shipbuilding, and general manufacturing 
        sectors across Western Canada with expansion potential to broader North American markets.
        """
        
        self.add_body_text(summary_text)
        self.add_spacer()
    
    def _add_company_description(self):
        """Add company description section"""
        self.add_heading1("Company Description")
        
        self.add_heading2("Company Overview")
        if self.company_info:
            company_text = f"""
            <b>Legal Name:</b> {self.company_info.get('legal_name', 'FluxGen Industries Ltd.')}
            <br/>
            <b>Operating Name:</b> {self.company_info.get('operating_name', 'FluxGen Industries')}
            <br/>
            <b>Location:</b> {self.company_info.get('location', 'Airdrie')}, {self.company_info.get('province', 'Alberta')}, {self.company_info.get('country', 'Canada')}
            <br/>
            <b>Incorporation Status:</b> {self.company_info.get('incorporation_status', 'Under Formation')}
            <br/>
            <b>Website:</b> {self.company_info.get('website', 'www.fluxgen.ca')}
            <br/>
            <b>Vision Statement:</b>
            {self.company_info.get('vision', 'From molten core to global connection — FluxGen powers the world\'s welds')}
            <br/>
            <b>Mission Statement:</b>
            {self.company_info.get('mission', 'Localize production, reduce import dependency, and promote innovation in welding materials')}
            """
            self.add_body_text(company_text)
        
        self.add_heading2("Industry & Business Model")
        industry_text = """
        FluxGen operates in the welding consumables industry, specifically focusing on submerged arc welding (SAW) 
        flux and specialty alloy manufacturing. The business model emphasizes:
        <br/>
        • <b>Local Manufacturing:</b> Reducing dependency on imported materials
        <br/>
        • <b>Quality Focus:</b> Meeting and exceeding industry standards for welding performance
        <br/>
        • <b>Customer Partnership:</b> Working closely with customers to develop customized solutions
        <br/>
        • <b>Continuous Innovation:</b> Investing in R&D for product improvement and new applications
        <br/>
        • <b>Sustainable Operations:</b> Minimizing environmental impact through efficient processes
        <br/>
        
        The company targets B2B customers in heavy industry, infrastructure, and manufacturing sectors.
        """
        self.add_body_text(industry_text)
        self.add_spacer()
    
    def _add_market_analysis(self):
        """Add market analysis section"""
        self.add_heading1("Market Analysis")
        
        self.add_heading2("Industry Overview")
        market_text = """
        The global welding consumables market is valued at over $7 billion annually, with steady growth driven by 
        infrastructure development, energy projects, and manufacturing expansion.
        <br/>
        <b>Market Drivers:</b>
        <br/>
        • Infrastructure spending and maintenance in North America
        <br/>
        • Oil & gas pipeline construction and maintenance
        <br/>
        • Shipbuilding and marine applications
        <br/>
        • Heavy manufacturing and equipment production
        <br/>
        • Renewable energy infrastructure development
        <br/>
        <b>Market Trends:</b>
        <br/>
        • Increasing focus on supply chain localization
        <br/>
        • Demand for higher quality welding materials
        <br/>
        • Customization and technical support services
        <br/>
        • Environmental compliance and sustainable practices
        """
        self.add_body_text(market_text)
        
        self.add_heading2("Target Markets")
        target_text = """
        <b>Primary Markets:</b>
        <br/>
        • Oil & Gas: Pipeline construction, refineries, petrochemical facilities
        <br/>
        • Infrastructure: Bridges, buildings, municipal projects
        <br/>
        • Manufacturing: Heavy equipment, pressure vessels, structural fabrication
        <br/>
        • Marine: Shipbuilding, offshore platforms, vessel maintenance
        <br/>
        <b>Geographic Focus:</b>
        <br/>
        • Phase 1: Alberta and Saskatchewan
        <br/>
        • Phase 2: Western Canada (BC, Manitoba)
        <br/>
        • Phase 3: Central Canada and Northern US states
        <br/>
        <b>Customer Segments:</b>
        <br/>
        • Large fabrication shops (primary target)
        <br/>
        • Engineering and construction companies
        <br/>
        • Maintenance and repair operations
        <br/>
        • Government and municipal contractors
        """
        self.add_body_text(target_text)
        self.add_spacer()
    
    def _add_products_services(self):
        """Add products and services section"""
        self.add_heading1("Products & Services")
        
        self.add_heading2("Product Portfolio")
        
        # Get alloys catalog data
        alloys = self.db.get_alloys_catalog()
        
        if alloys:
            products_data = [['Alloy Symbol', 'Application', 'Grade Type', 'Key Features']]
            
            for alloy in alloys[:10]:  # Limit to first 10 for space
                products_data.append([
                    alloy.get('alloy_symbol', 'N/A'),
                    alloy.get('application', 'N/A')[:50] + '...' if alloy.get('application') and len(alloy.get('application', '')) > 50 else alloy.get('application', 'N/A'),
                    alloy.get('grade_type', 'N/A'),
                    alloy.get('typical_composition', 'N/A')[:40] + '...' if alloy.get('typical_composition') and len(alloy.get('typical_composition', '')) > 40 else alloy.get('typical_composition', 'N/A')
                ])
            
            self.add_table(products_data, [1.2, 2.2, 1.2, 2.4], title="Core Product Lines")
        
        products_text = """
        FluxGen's product portfolio focuses on high-quality SAW flux and specialty alloys designed for demanding 
        industrial applications. Our products are formulated to meet specific customer requirements and industry standards.
        <br/>
        <b>Product Categories:</b>
        <br/>
        • Submerged Arc Welding (SAW) Flux - Various compositions for different applications
        <br/>
        • Specialty Alloys - Custom formulations for specific welding requirements
        <br/>
        • Technical Support - Application engineering and process optimization
        <br/>
        • Custom Blending - Tailored products for unique customer specifications
        <br/>
        <b>Quality Standards:</b>
        <br/>
        • AWS (American Welding Society) specifications
        <br/>
        • CWB (Canadian Welding Bureau) requirements 
        <br/> 
        • DIN (German national standard body) requirements 
        <br/> 
        • ISO 9001 quality management system
        <br/>
        • Customer-specific quality requirements
        """
        self.add_body_text(products_text)
        
        self.add_heading2("Value Proposition")
        value_text = """
        <b>Superior Quality:</b> Consistent, high-performance products that meet or exceed industry standards
        <br/>
        <b>Local Supply:</b> Reduced lead times and transportation costs compared to imported alternatives
        <br/>
        <b>Technical Expertise:</b> Application support and custom formulation capabilities
        <br/>
        <b>Reliable Delivery:</b> Consistent supply with emergency response capabilities
        <br/>
        <b>Competitive Pricing:</b> Cost-effective solutions with transparent pricing
        <br/>
        <b>Customer Partnership:</b> Collaborative approach to solving welding challenges
        """
        self.add_body_text(value_text)
        self.add_spacer()
    
    def _add_operations_plan(self):
        """Add operations plan section"""
        self.add_heading1("Operations Plan")
        
        self.add_heading2("Manufacturing Process")
        
        # Get production targets
        production_targets = self.db.get_production_targets()
        
        if production_targets:
            process_data = [['Phase', 'Capacity (kg/month)', 'Process Flow', 'Sourcing Strategy']]
            
            for target in production_targets:
                process_data.append([
                    target.get('phase', 'N/A'),
                    f"{target.get('output_kg_month', 0):,}" if target.get('output_kg_month') else 'N/A',
                    target.get('process_flow', 'N/A'),
                    target.get('sourcing_strategy', 'N/A')
                ])
            
            self.add_table(process_data, [1.2, 1.5, 2.8, 1.5], title="Production Capabilities by Phase")
        
        operations_text = """
        <b>Manufacturing Process:</b>
        <br/>
        1. Raw Material Receiving and Quality Control
        <br/>
        2. Precision Blending according to specifications
        <br/>
        3. Agglomeration and pelletization
        <br/>
        4. Drying and heat treatment
        <br/>
        5. Screening and size classification
        <br/>
        6. Quality testing and certification
        <br/>
        7. Packaging and labeling
        <br/>
        8. Shipping and logistics
        <br/>
        <b>Quality Control:</b>
        <br/>
        • Incoming raw material inspection and testing
        <br/>
        • In-process monitoring and control systems
        <br/>
        • Final product testing and certification
        <br/>
        • Statistical process control and continuous improvement
        <br/>
        • Traceability and documentation systems
        <br/>
        <b>Facility Requirements:</b>
        <br/>
        • 10,000-15,000 sq ft manufacturing space
        <br/>
        • Raw material storage areas (climate controlled)
        <br/>
        • Finished goods warehouse
        <br/>
        • Quality control laboratory
        <br/>
        • Administrative offices
        """
        self.add_body_text(operations_text)
        
        self.add_heading2("Supply Chain Management")
        supply_text = """
        <b>Raw Material Sourcing:</b>
        <br/>
        • Primary suppliers located in Canada (80-90% of materials)
        <br/>
        • Secondary suppliers for specialty components
        <br/>
        • Strategic inventory management (30-60 day supply)
        <br/>
        • Supplier qualification and performance monitoring
        <br/>
        <b>Logistics and Distribution:</b>
        <br/>
        • Just-in-time delivery for large customers
        <br/>
        • Regional warehouse partnerships for smaller orders
        <br/>
        • Fleet management for critical deliveries
        <br/>
        • Third-party logistics for long-distance shipping
        <br/>
        <b>Inventory Management:</b>
        <br/>
        • ERP system for real-time inventory tracking
        <br/>
        • Automated reorder points and safety stock levels
        <br/>
        • Vendor-managed inventory for key customers
        <br/>
        • Regular cycle counting and inventory optimization
        """
        self.add_body_text(supply_text)
        self.add_spacer()
    
    def _add_management_team(self):
        """Add management team section"""
        self.add_heading1("Management Team")
        
        # Get team member data
        team_members = self.db.get_team_members()
        
        if team_members:
            team_data = [['Name', 'Position', 'Key Responsibilities', 'Contact']]
            
            for member in team_members:
                responsibilities = {
                    'Managing Director': 'Strategic planning, stakeholder relations, business development',
                    'Operations Director': 'Manufacturing operations, quality control, process optimization',
                    'Supply Chain Director': 'Procurement, logistics, vendor management',
                    'CFO': 'Financial management, accounting, investor relations',
                    'Sales Director': 'Customer relations, market development, sales strategy'
                }.get(member.get('role', ''), 'Various operational responsibilities')
                
                contact = []
                if member.get('email'):
                    contact.append(member['email'])
                if member.get('phone'):
                    contact.append(member['phone'])
                
                team_data.append([
                    member.get('name', 'N/A'),
                    member.get('role', 'N/A'),
                    responsibilities,
                    ' | '.join(contact) if contact else 'N/A'
                ])
            
            self.add_table(team_data, [1.5, 1.5, 2.5, 1.5], title="Key Management Personnel")
        
        team_text = """
        The FluxGen management team combines extensive experience in manufacturing, operations, finance, and 
        business development. The team has successfully launched and scaled industrial operations in competitive markets.
        <br/>
        <b>Organizational Structure:</b>
        <br/>
        • Executive leadership responsible for strategic direction
        <br/>
        • Operations team managing day-to-day manufacturing
        <br/>
        • Sales and customer service for market development
        <br/>
        • Finance and administration for business support
        <br/>
        • Technical team for quality control and R&D
        <br/>
        <b>Advisory Board:</b>
        The company will establish an advisory board comprising industry experts, successful entrepreneurs, 
        and technical specialists to provide guidance on strategic decisions and market opportunities.
        <br/>
        <b>Staffing Plan:</b>
        <br/>
        • Phase 1: 8-12 employees (core team)
        <br/>
        • Phase 2: 15-20 employees (full production)
        <br/>
        • Phase 3: 25+ employees (expansion)
        """
        self.add_body_text(team_text)
        self.add_spacer()
    
    def _add_financial_overview(self):
        """Add financial overview section"""
        self.add_heading1("Financial Overview")
        
        # Get financial data
        capex_items = self.db.get_investment_capex()
        financial_summary = self.db.get_financial_summary()
        
        self.add_heading2("Capital Investment Requirements")
        
        if capex_items:
            capex_data = [['Category', 'Description', 'Estimated Cost (CAD)', 'Phase']]
            
            for item in capex_items:
                capex_data.append([
                    item.get('category', 'N/A'),
                    (item.get('description', 'N/A')[:60] + '...') if item.get('description') and len(item.get('description', '')) > 60 else item.get('description', 'N/A'),
                    self.format_currency(item.get('estimated_cost_cad')),
                    item.get('phase', 'N/A')
                ])
            
            self.add_table(capex_data, [1.8, 2.5, 1.5, 1.2], title="Capital Expenditure Breakdown")
        
        financial_text = f"""
        <b>Investment Summary:</b>
        <br/>
        • Total Estimated CAPEX: {self.format_currency(financial_summary.get('total_capex', 0))}
        <br/>
        • Pilot Phase Investment: Focused on essential equipment and facility setup
        <br/>
        • Scale-up Investment: Additional capacity and automation
        <br/>
        • Working Capital: Inventory, accounts receivable, operating expenses
        <br/>
        <b>Revenue Projections:</b>
        <br/>
        • Year 1: CAD $200,000 - $300,000 (pilot production)
        <br/>
        • Year 2: CAD $800,000 - $1,200,000 (scale-up phase)
        <br/>
        • Year 3+: CAD $2,000,000+ (full production capacity)
        <br/>
        <b>Key Financial Assumptions:</b>
        <br/>
        • Average selling price: CAD $4-6 per kg
        <br/>
        • Gross margin target: 35-45%
        <br/>
        • Operating expense ratio: 25-30% of revenue
        <br/>
        • Working capital: 15-20% of annual revenue
        """
        self.add_body_text(financial_text)
        self.add_spacer()
    
    def _add_risk_analysis(self):
        """Add risk analysis section"""
        self.add_heading1("Risk Analysis & Mitigation")
        
        risk_data = [
            ['Risk Category', 'Description', 'Impact', 'Mitigation Strategy'],
            ['Market Risk', 'Economic downturn affecting demand', 'High', 'Diversified customer base, flexible cost structure'],
            ['Competition Risk', 'New entrants or aggressive pricing', 'Medium', 'Quality differentiation, customer relationships'],
            ['Supply Chain Risk', 'Raw material price volatility', 'Medium', 'Long-term supplier agreements, inventory management'],
            ['Operational Risk', 'Equipment failure or quality issues', 'Medium', 'Preventive maintenance, quality systems, insurance'],
            ['Regulatory Risk', 'Changes in environmental or safety regulations', 'Low', 'Proactive compliance, industry monitoring'],
            ['Financial Risk', 'Cash flow or funding challenges', 'Medium', 'Conservative financial management, banking relationships']
        ]
        
        self.add_table(risk_data, [1.5, 2.0, 1.0, 2.5], title="Risk Assessment Matrix")
        
        risk_text = """
        <b>Risk Management Approach:</b>
        FluxGen employs a comprehensive risk management strategy that includes regular risk assessment, 
        mitigation planning, and contingency preparation.
        <br/>
        <b>Insurance Coverage:</b>
        <br/>
        • General liability and product liability insurance
        <br/>
        • Property and equipment coverage
        <br/>
        • Business interruption insurance
        <br/>
        • Workers' compensation and employment practices liability
        <br/>
        <b>Financial Controls:</b>
        <br/>
        • Regular financial reporting and variance analysis
        <br/>
        • Cash flow forecasting and management
        <br/>
        • Credit management and collection procedures
        <br/>
        • Banking relationships and credit facilities
        <br/>
        <b>Operational Controls:</b>
        <br/>
        • Quality management systems and certifications
        <br/>
        • Safety programs and training
        <br/>
        • Preventive maintenance schedules
        <br/>
        • Business continuity planning
        """
        self.add_body_text(risk_text)
        self.add_spacer()
    
    def _add_implementation_timeline(self):
        """Add implementation timeline section"""
        self.add_heading1("Implementation Timeline")
        
        timeline_data = [
            ['Phase', 'Timeline', 'Key Milestones', 'Success Metrics'],
            ['Pre-Launch', 'Months 1-6', 'Site selection, permits, equipment procurement', 'All permits obtained, facility ready'],
            ['Pilot Launch', 'Months 7-12', 'Initial production, customer trials', '500 kg/month capacity achieved'],
            ['Scale-Up', 'Months 13-24', 'Capacity expansion, market development', '2,000+ kg/month, 10+ customers'],
            ['Full Operations', 'Months 25+', 'Optimization, expansion planning', '5,000+ kg/month, profitability']
        ]
        
        self.add_table(timeline_data, [1.3, 1.3, 2.7, 1.7], title="Implementation Milestones")
        
        implementation_text = """
        <b>Critical Success Factors:</b>
        <br/>
        • Securing appropriate facility and permits on schedule
        <br/>
        • Successful equipment installation and commissioning
        <br/>
        • Hiring and training qualified production staff
        <br/>
        • Establishing reliable supply chain relationships
        <br/>
        • Achieving consistent product quality standards
        <br/>
        • Building strong customer relationships and repeat business
        <br/>
        <b>Key Performance Indicators:</b>
        <br/>
        • Monthly production volume and capacity utilization
        <br/>
        • Product quality metrics and customer satisfaction
        <br/>
        • Financial performance vs. budget and projections
        <br/>
        • Safety incidents and environmental compliance
        <br/>
        • Customer acquisition and retention rates
        <br/>
        • Market share and competitive position
        <br/>
        The implementation plan is designed to be flexible and responsive to market conditions while 
        maintaining focus on quality, safety, and customer satisfaction.
        """
        self.add_body_text(implementation_text)
        self.add_spacer()
    
    def generate(self) -> Path:
        """Generate the Business Plan PDF"""
        self.story = []  # Reset story
        self.build_content()
        
        filename = f"fluxgen_business_plan_{self._get_timestamp()}"
        return self.generate_document(filename, "FluxGen Industries - Business Plan")
    
    def _get_timestamp(self) -> str:
        """Get timestamp for filename"""
        from datetime import datetime
        return datetime.now().strftime('%Y%m%d_%H%M%S')