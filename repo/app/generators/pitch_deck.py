"""
Pitch Deck document generator for FluxGen
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.base import BaseDocumentGenerator
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class PitchDeckGenerator(BaseDocumentGenerator):
    """Generates Pitch Deck presentation document (12-15 slides as PDF pages)"""
    
    def __init__(self, database_manager, output_dir: Path):
        super().__init__(database_manager, output_dir)
    
    def build_content(self):
        """Build pitch deck content as slides"""
        # Slide 1: Title Slide
        self._add_title_slide()
        self.add_page_break()
        
        # Slide 2: Problem Statement
        self._add_problem_slide()
        self.add_page_break()
        
        # Slide 3: Solution
        self._add_solution_slide()
        self.add_page_break()
        
        # Slide 4: Market Opportunity
        self._add_market_opportunity_slide()
        self.add_page_break()
        
        # Slide 5: Product Overview
        self._add_product_overview_slide()
        self.add_page_break()
        
        # Slide 6: Business Model
        self._add_business_model_slide()
        self.add_page_break()
        
        # Slide 7: Traction/Milestones
        self._add_traction_slide()
        self.add_page_break()
        
        # Slide 8: Management Team
        self._add_team_slide()
        self.add_page_break()
        
        # Slide 9: Financial Projections
        self._add_financials_slide()
        self.add_page_break()
        
        # Slide 10: Competition
        self._add_competition_slide()
        self.add_page_break()
        
        # Slide 11: Go-to-Market Strategy
        self._add_go_to_market_slide()
        self.add_page_break()
        
        # Slide 12: The Ask (Funding)
        self._add_funding_ask_slide()
        self.add_page_break()
        
        # Slide 13: Use of Funds
        self._add_use_of_funds_slide()
        self.add_page_break()
        
        # Slide 14: Contact & Next Steps
        self._add_contact_slide()
    
    def _add_slide_header(self, slide_number: int, title: str):
        """Add slide header with number and title"""
        header_text = f"Slide {slide_number}"
        self.add_body_text(f"<i>{header_text}</i>")
        self.add_title(title)
    
    def _add_title_slide(self):
        """Slide 1: Title slide"""
        self._add_slide_header(1, "FluxGen Industries Ltd.")
        
        if self.company_info:
            subtitle = self.company_info.get('tagline', 'Forging Tomorrow\'s Welds')
            tagline = self.company_info.get('vision', 'From molten core to global connection — FluxGen powers the world\'s welds')
        else:
            subtitle = 'Forging Tomorrow\'s Welds'
            tagline = 'From molten core to global connection — FluxGen powers the world\'s welds'
        
        self.add_heading1(subtitle)
        self.add_body_text(f"<i>{tagline}</i>")
        self.add_spacer(0.5)
        
        title_content = f"""
        <b>Localizing SAW Flux Manufacturing in Western Canada</b>
        <br/>
        Presentation for Economic Development Office
        {self.format_date('2025-11-25')}
        <br/>
        Confidential Business Plan Summary
        """
        
        self.add_body_text(title_content)
    
    def _add_problem_slide(self):
        """Slide 2: Problem Statement"""
        self._add_slide_header(2, "The Problem: Supply Chain Vulnerability")
        
        problem_text = """
        <b>Western Canada's Welding Materials Market is Import-Dependent</b>
        <br/>
        
        <b>Key Challenges:</b>
        <br/>
        • 80%+ of SAW flux imported from Asia and Eastern US
        <br/>
        • Long lead times (4-8 weeks) impacting project schedules
        <br/>
        • Supply chain disruptions during COVID-19 and geopolitical tensions
        <br/>
        • Limited local technical support and application expertise
        <br/>
        • High transportation costs adding 15-25% to product costs
        <br/>
        • Quality inconsistencies from overseas suppliers
        <br/>
        
        <b>Market Pain Points:</b>
        <br/>
        • Energy companies struggling with material availability for pipeline projects
        <br/>
        • Fabricators carrying excessive inventory due to supply uncertainty
        <br/>
        • Emergency situations requiring expensive air freight for critical materials
        <br/>
        • Limited customization options from offshore suppliers
        <br/>
        • Lack of responsive technical support for complex applications
        <br/>
        
        <b>The Opportunity:</b>
        <br/>
        Western Canada needs a reliable, local manufacturer of high-quality welding materials
        to support the region's energy, infrastructure, and manufacturing sectors.
        """
        
        self.add_body_text(problem_text)
        
        # Problem impact table
        impact_data = [
            ['Impact Area', 'Current State', 'Cost to Industry'],
            ['Lead Times', '6-8 weeks average', '$50M+ in carrying costs'],
            ['Supply Disruptions', '15+ incidents in 2023', '$25M+ in project delays'],
            ['Emergency Supply', '20% price premium', '$15M+ in emergency costs'],
            ['Quality Issues', '5-8% reject rates', '$10M+ in rework costs']
        ]
        
        self.add_table(impact_data, [1.5, 2.0, 2.5], title="Market Problem Quantification")
    
    def _add_solution_slide(self):
        """Slide 3: Solution"""
        self._add_slide_header(3, "The FluxGen Solution")
        
        solution_text = """
        <b>Local Manufacturing Excellence for Western Canada</b>
        <br/>
        
        <b>Our Solution:</b>
        <br/>
        FluxGen Industries establishes state-of-the-art SAW flux manufacturing in Airdrie, Alberta, 
        providing local supply, superior quality, and responsive service to Western Canadian markets.
        
        <br/>
        <b>Value Proposition:</b>
        <br/>
        • <b>Local Supply:</b> 1-2 week delivery vs. 6-8 weeks from imports
        <br/>
        • <b>Superior Quality:</b> Consistent, certified products meeting AWS standards
        <br/>
        • <b>Technical Support:</b> Local application engineering and customer support
        <br/>
        • <b>Competitive Pricing:</b> Eliminate import markups and transportation costs
        <br/>
        • <b>Custom Solutions:</b> Flexible manufacturing for specific customer requirements
        <br/>
        • <b>Supply Reliability:</b> Reduced risk of supply chain disruptions
        <br/>
        
        <b>Competitive Advantages:</b>
        <br/>
        • Strategic location in Calgary-Edmonton industrial corridor
        <br/>
        • Canadian content supporting government procurement preferences
        <br/>
        • Experienced management team with industry relationships
        <br/>
        • Scalable manufacturing platform for growth
        <br/>
        • 80-90% Canadian raw material sourcing
        """
        
        self.add_body_text(solution_text)
        
        # Solution benefits table
        benefits_data = [
            ['Benefit Category', 'Customer Value', 'Competitive Advantage'],
            ['Delivery Speed', '75% faster delivery', 'Local manufacturing & logistics'],
            ['Technical Support', '24-hour response time', 'Local application engineers'],
            ['Product Quality', '99.5%+ consistency', 'Advanced quality control systems'],
            ['Cost Savings', '10-15% total cost reduction', 'Eliminate import markups'],
            ['Supply Security', '99% availability target', 'Local inventory & production']
        ]
        
        self.add_table(benefits_data, [1.5, 2.0, 2.5], title="Customer Value Proposition")
    
    def _add_market_opportunity_slide(self):
        """Slide 4: Market Opportunity"""
        self._add_slide_header(4, "Massive Market Opportunity")
        
        market_text = """
        <b>$150M+ Addressable Market in Western Canada</b>
        <br/>
        
        <b>Market Size & Growth:</b>
        <br/>
        • Total Addressable Market: CAD $150-200 million annually
        <br/>
        • Annual Growth Rate: 4.1% driven by infrastructure and energy projects
        <br/>
        • Import Dependency: 80%+ creating local manufacturer opportunity
        <br/>
        • Market Expansion: Additional $200M+ in central Canada and northern US
        <br/>
        
        <b>Key Market Drivers:</b>
        <br/>
        • $180+ billion federal infrastructure investment program
        <br/>
        • Major pipeline projects (TMX, Coastal GasLink expansions)
        <br/>
        • Oil & gas facility maintenance and expansion
        <br/>
        • Manufacturing sector growth and reshoring trends
        <br/>
        • Government emphasis on supply chain localization
        """
        
        self.add_body_text(market_text)
        
        # Market segments
        market_segments_data = [
            ['Market Segment', 'Size (CAD)', 'Growth Rate', 'FluxGen Opportunity'],
            ['Oil & Gas', '$60 million', '5.2%', 'High - Local advantage'],
            ['Infrastructure', '$45 million', '4.8%', 'High - Government spending'],
            ['Manufacturing', '$30 million', '3.5%', 'Medium - Diverse needs'],
            ['Marine & Offshore', '$15 million', '2.8%', 'Medium - Specialized'],
            ['<b>Total Market</b>', '<b>$150 million</b>', '<b>4.1%</b>', '<b>Target 3-5% share</b>']
        ]
        
        self.add_table(market_segments_data, [1.5, 1.3, 1.0, 1.2], title="Market Segment Analysis")
        
        growth_text = """
        <b>Market Penetration Strategy:</b>
        <br/>
        • Year 1: Capture 0.5% market share ($0.75M revenue)
        <br/>
        • Year 3: Achieve 3.5% market share ($5.8M revenue)  
        <br/>
        • Year 5: Target 6.0% market share ($11.6M revenue)
        <br/>
        
        <b>Conservative Growth Assumptions:</b>
        Our projections assume capturing only 3-6% of the addressable market, 
        leaving significant room for growth and market expansion.
        """
        
        self.add_body_text(growth_text)
    
    def _add_product_overview_slide(self):
        """Slide 5: Product Overview"""
        self._add_slide_header(5, "Product Portfolio & Quality")
        
        product_text = """
        <b>Comprehensive SAW Flux Product Line</b>
        <br/>
        
        <b>Core Product Categories:</b>
        <br/>
        • <b>Basic Flux (F6XX Series):</b> General structural welding applications
        <br/>
        • <b>Low Hydrogen Flux (F7XX Series):</b> Pressure vessels and critical structures  
        <br/>
        • <b>Neutral Flux:</b> Multi-pass welding and build-up operations
        <br/>
        • <b>Specialty Alloys:</b> Custom formulations for specific applications
        <br/>
        
        <b>Quality Standards & Certifications:</b>
        <br/>
        • AWS A5.17 & A5.23 specifications compliance
        <br/>
        • CWB (Canadian Welding Bureau) approvals
        <br/>
        • ISO 9001:2015 quality management system
        <br/>
        • Full traceability and batch documentation
        <br/>
        • Rigorous testing: chemical, mechanical, and performance
        """
        
        self.add_body_text(product_text)
        
        # Get some alloy data if available
        alloys = self.db.get_alloys_catalog()
        if alloys and len(alloys) > 0:
            # Product examples table
            product_examples_data = [['Product', 'Application', 'Key Benefits']]
            
            for alloy in alloys[:4]:  # Show top 4 products
                product_examples_data.append([
                    alloy.get('alloy_symbol', 'F6XX'),
                    alloy.get('application', 'General welding')[:40] + '...' if len(alloy.get('application', '')) > 40 else alloy.get('application', 'General welding'),
                    'High quality, local supply, technical support'
                ])
            
            self.add_table(product_examples_data, [1.2, 2.3, 2.5], title="Product Examples")
        
        quality_text = """
        <b>Manufacturing Excellence:</b>
        <br/>
        • Advanced blending and agglomeration processes
        <br/>
        • Automated quality control and testing systems 
        <br/> 
        • Statistical process control for consistency
        <br/>
        • Continuous improvement and lean manufacturing
        <br/>
        • Environmental compliance and sustainability focus
        <br/>
        
        <b>Customer Support:</b>
        <br/>
        • Local application engineering support
        <br/>
        • Welding procedure development assistance
        <br/>
        • Technical training and education programs
        <br/>
        • 24/7 emergency supply capability
        <br/>
        • Custom formulation development services
        """
        
        self.add_body_text(quality_text)
    
    def _add_business_model_slide(self):
        """Slide 6: Business Model"""
        self._add_slide_header(6, "Scalable Business Model")
        
        business_model_text = """
        <b>Phased Growth Strategy with Strong Unit Economics</b>
        <br/>
        <b>Three-Phase Development Plan:</b>
        <br/>
        """
        
        self.add_body_text(business_model_text)
        
        # Get production targets
        production_targets = self.db.get_production_targets()
        
        if production_targets:
            phases_data = [['Phase', 'Capacity (kg/month)', 'Revenue Target', 'Key Focus']]
            
            revenue_targets = {
                'Pilot': '$0.75M annually',
                'Scale-Up': '$5.8M annually'
            }
            
            for target in production_targets:
                phase = target.get('phase', 'Unknown')
                phases_data.append([
                    phase,
                    f"{target.get('output_kg_month', 0):,}",
                    revenue_targets.get(phase, 'TBD'),
                    target.get('sourcing_strategy', 'Market development')
                ])
            
            self.add_table(phases_data, [1.2, 1.5, 1.5, 1.8], title="Phased Development Strategy")
        
        model_details = """
        <b>Revenue Model:</b>
        <br/>
        • Direct sales to large customers (70% of revenue)
        <br/>
        • Distributor partnerships for smaller customers (20% of revenue)
        <br/>
        • Online sales and emergency orders (10% of revenue)
        <br/>
        
        <b>Target Margins:</b>
        <br/>
        • Gross Margin: 35-45% (improving with scale)
        <br/>
        • EBITDA Margin: 25-30% at full scale
        <br/>
        • Strong cash flow generation for self-funded growth
        <br/>
        
        <b>Competitive Positioning:</b>
        <br/>
        • Premium quality with competitive pricing
        <br/>
        • Local supply advantage vs. imports
        <br/>
        • Superior service vs. large manufacturers
        <br/>
        • Technical expertise vs. distributors
        <br/>
        
        <b>Scalability Factors:</b>
        <br/>
        • Modular production system for capacity expansion
        <br/>
        • Proven processes and quality systems
        <br/>
        • Established customer relationships and market presence
        <br/>
        • Management team with scaling experience
        """
        
        self.add_body_text(model_details)
    
    def _add_traction_slide(self):
        """Slide 7: Traction/Milestones"""
        self._add_slide_header(7, "Progress & Milestones")
        
        traction_text = """
        <b>Strong Foundation & Execution Progress</b>
        <br/>
        
        <b>Completed Milestones:</b>
        <br/>
        • Market research and customer validation completed
        <br/>
        • Management team assembled with relevant experience
        <br/>
        • Technology and process design finalized
        <br/>
        • Supplier relationships established with Canadian sources
        <br/>
        • Site selection criteria developed for Airdrie location
        <br/>
        • Financial projections and business plan completed
        <br/>
        
        <b>Current Activities:</b>
        <br/>
        • Government funding program applications in progress
        <br/>
        • Equipment vendor selection and quote process
        <br/>
        • Site visits and lease/purchase negotiations  
        <br/>
        • Initial customer discussions and letters of intent
        <br/>
        • Regulatory compliance planning and permit preparation
        """
        
        self.add_body_text(traction_text)
        
        # Milestone timeline
        milestone_data = [
            ['Milestone', 'Target Date', 'Status', 'Success Criteria'],
            ['Team Assembly', 'Completed', 'Done ✓', 'Key roles filled'],
            ['Business Plan', 'Completed', 'Done ✓', 'Comprehensive plan ready'],
            ['Funding Secured', 'Month 3', 'In Progress', '$200K+ secured'],
            ['Site Selection', 'Month 4', 'In Progress', 'Lease signed'],
            ['Equipment Ordered', 'Month 5', 'Planned', 'Major equipment contracts'],
            ['Permits Obtained', 'Month 8', 'Planned', 'All permits approved'],
            ['Facility Buildout', 'Month 10', 'Planned', 'Construction complete'],
            ['Production Start', 'Month 12', 'Planned', 'First product shipped'],
            ['Customer Trials', 'Month 14', 'Planned', '3+ customers qualified'],
            ['Full Production', 'Month 18', 'Planned', '500+ kg/month capacity']
        ]
        
        self.add_table(milestone_data, [1.4, 1.0, 1.0, 1.6], title="Implementation Timeline")
        
        validation_text = """
        <b>Market Validation:</b>
        <br/>
        • Customer interviews confirming demand and pricing
        <br/>
        • Supplier meetings validating cost and availability
        <br/>
        • Industry expert validation of market opportunity
        <br/>
        • Government support for local manufacturing initiatives
        <br/>
        
        <b>Risk Mitigation:</b>
        <br/>
        • Conservative financial projections with multiple scenarios
        <br/>
        • Experienced team with relevant industry background
        <br/>
        • Phased approach minimizing initial investment
        <br/>
        • Multiple customer segments reducing concentration risk
        """
        
        self.add_body_text(validation_text)
    
    def _add_team_slide(self):
        """Slide 8: Management Team"""
        self._add_slide_header(8, "Experienced Management Team")
        
        team_intro = """
        <b>Industry Experience + Proven Track Record</b>
        <br/>
        The FluxGen management team combines deep industry knowledge with proven execution 
        capability in manufacturing and business development.
        """
        
        self.add_body_text(team_intro)
        
        # Get team data
        team_members = self.db.get_team_members()
        
        if team_members:
            team_data = [['Name', 'Role', 'Key Experience', 'Value to FluxGen']]
            
            experience_map = {
                'Managing Director': '15+ years executive leadership, manufacturing scale-up',
                'Operations Director': '12+ years manufacturing operations, quality systems',
                'Supply Chain Director': '10+ years procurement, logistics, vendor management'
            }
            
            value_map = {
                'Managing Director': 'Strategic leadership, stakeholder management, business development',
                'Operations Director': 'Manufacturing excellence, quality assurance, operational efficiency',
                'Supply Chain Director': 'Cost optimization, supplier relationships, inventory management'
            }
            
            for member in team_members:
                role = member.get('role', 'Team Member')
                team_data.append([
                    member.get('name', 'TBD'),
                    role,
                    experience_map.get(role, '8+ years relevant experience'),
                    value_map.get(role, 'Industry expertise and execution capability')
                ])
            
            self.add_table(team_data, [1.3, 1.3, 1.7, 1.7], title="Management Team")
        
        team_strength = """
        <b>Team Strengths:</b>
        <br/>
        • Collective 40+ years of manufacturing and business experience
        <br/>
        • Proven track record in scaling industrial operations
        <br/>
        • Deep relationships with suppliers, customers, and industry partners
        <br/>
        • Complementary skill sets covering all critical business functions
        <br/>
        • Commitment to operational excellence and customer satisfaction
        <br/>
        
        <b>Advisory Support:</b>
        <br/>
        • Industry advisory board with welding technology experts
        <br/>
        • Business advisors with manufacturing and financial expertise
        <br/>
        • Customer advisory panel providing market feedback
        <br/>
        • Government relations support for regulatory compliance
        <br/>
        
        <b>Future Hiring:</b>
        <br/>
        • Production team: experienced operators and technicians
        <br/>
        • Quality control: certified lab technicians and inspectors
        <br/>
        • Sales team: industry relationships and technical sales experience
        <br/>
        • Administration: accounting, HR, and customer service support
        """
        
        self.add_body_text(team_strength)
    
    def _add_financials_slide(self):
        """Slide 9: Financial Projections"""
        self._add_slide_header(9, "Strong Financial Projections")
        
        financial_summary = self.db.get_financial_summary()
        
        financials_intro = f"""
        <b>Path to Profitability with Strong Returns</b>
        
        <br/>
        <b>Investment Highlights:</b>
        <br/>
        • Total CAPEX Investment: {self.format_currency(financial_summary.get('total_capex', 150000))}
        <br/>
        • Break-even: Month 18-24 of operations
        <br/>
        • 5-Year Revenue Target: $3.5-5.0 million annually
        <br/>
        • Target EBITDA Margin: 25-30% at scale
        <br/>
        • Projected ROI: 25-35% by Year 3
        """
        
        self.add_body_text(financials_intro)
        
        # 5-year summary projections
        projections_data = [
            ['Metric', 'Year 1', 'Year 2', 'Year 3', 'Year 5'],
            ['Revenue', '$200K', '$800K', '$1.8M', '$3.2M'],
            ['Gross Margin', '20%', '32%', '35%', '37%'],
            ['EBITDA', '($34K)', '$140K', '$424K', '$870K'],
            ['EBITDA Margin', '(17%)', '18%', '25%', '27%'],
            ['Production (kg/month)', '500', '2,000', '4,000', '6,000'],
            ['Customers', '3-5', '8-12', '15-20', '25+'],
            ['Employees', '8-12', '15-18', '20-25', '25-30']
        ]
        
        self.add_table(projections_data, [1.3, 1.0, 1.0, 1.0, 1.0], title="5-Year Financial Projections")
        
        financial_highlights = """
        <b>Key Financial Assumptions:</b>
        <br/>
        • Conservative market penetration (3-6% of addressable market)
        <br/>
        • Competitive pricing with 5-15% local supply premium
        <br/>
        • Gross margins improving with scale and operational efficiency
        <br/>
        • Working capital maintained at 12-15% of revenue
        <br/>
        
        <b>Cash Flow & Returns:</b>
        <br/>
        • Positive cash flow by Year 2
        <br/>
        • Self-funding capability by Year 3
        <br/>
        • Strong ROI for investors with multiple exit options
        <br/>
        • Dividend potential beginning Year 4
        <br/>
        
        <b>Sensitivity Analysis:</b>
        <br/>
        • Break-even achievable even with 15% lower volumes
        <br/>
        • Price sensitivity of 10% impacts EBITDA by 15-20%
        <br/>
        • Multiple scenarios validate robust financial performance
        """
        
        self.add_body_text(financial_highlights)
    
    def _add_competition_slide(self):
        """Slide 10: Competition"""
        self._add_slide_header(10, "Competitive Landscape")
        
        competition_text = """
        <b>Favorable Competitive Position</b>
        <br/>
        
        <b>Current Market Structure:</b>
        <br/>
        • Global manufacturers (Lincoln Electric, ESAB): 45% market share
        <br/>
        • Regional distributors: 30% market share
        <br/>  
        • Asian imports: 20% market share
        <br/>
        • Local manufacturers: 5% market share ← FluxGen opportunity
        """
        
        self.add_body_text(competition_text)
        
        # Competitive comparison
        competition_data = [
            ['Competitor Type', 'Strengths', 'Weaknesses', 'FluxGen Advantage'],
            ['Global Manufacturers', 'Brand recognition, R&D', 'High prices, slow delivery', 'Local supply, competitive pricing'],
            ['Regional Distributors', 'Relationships, inventory', 'No manufacturing control', 'Quality control, direct sales'],
            ['Asian Imports', 'Low cost, high volume', 'Quality issues, long lead times', 'Superior quality, fast delivery'],
            ['Existing Local', 'Local presence', 'Limited capacity, old technology', 'Modern facility, scalable processes']
        ]
        
        self.add_table(competition_data, [1.2, 1.6, 1.6, 1.6], title="Competitive Analysis")
        
        competitive_strategy = """
        <b>Competitive Strategy:</b>
        <br/>
        • <b>vs. Global Manufacturers:</b> Compete on speed, service, and local presence
        <br/>
        • <b>vs. Distributors:</b> Direct relationships and superior technical support
        <br/>
        • <b>vs. Imports:</b> Quality, reliability, and responsive customer service
        <br/>
        • <b>vs. Local Competitors:</b> Modern technology and scalable operations
        <br/>
        
        <b>Sustainable Advantages:</b>
        <br/>
        • Local manufacturing reducing lead times by 75%
        <br/>
        • Technical support with 24-hour response capability
        <br/>
        • Custom formulation flexibility for specific applications
        <br/>
        • Canadian content supporting government procurement
        <br/>
        • Strong supplier relationships ensuring cost competitiveness
        <br/>
        
        <b>Barriers to Entry:</b>
        <br/>
        • Significant capital investment requirements ($200K+ initial investment)
        <br/>
        • Technical expertise and industry certifications
        <br/>
        • Customer relationships and trust building
        <br/>
        • Regulatory compliance and permit requirements
        """
        
        self.add_body_text(competitive_strategy)
    
    def _add_go_to_market_slide(self):
        """Slide 11: Go-to-Market Strategy"""
        self._add_slide_header(11, "Go-to-Market Strategy")
        
        gtm_strategy = """
        <b>Multi-Channel Approach with Direct Sales Focus</b>
        <br/>
        
        <b>Phase 1: Market Entry (Months 1-12)</b>
        <br/>
        • Target: 3-5 pilot customers in Alberta
        <br/>
        • Approach: Direct sales with intensive technical support
        <br/>
        • Focus: Product validation and quality demonstration
        <br/>
        • Goal: $0.75M revenue, proof of concept
        <br/>
        
        <b>Phase 2: Market Development (Months 13-24)</b>
        <br/>
        • Target: 10-15 active customers across Alberta/Saskatchewan
        <br/>
        • Approach: Direct sales + selective distributor partnerships
        <br/>
        • Focus: Market penetration and capacity scaling
        <br/>
        • Goal: $3.1M revenue, operational efficiency
        <br/>
        
        <b>Phase 3: Regional Expansion (Months 25+)</b>
        <br/>
        • Target: Western Canada market leadership
        <br/>
        • Approach: Multi-channel distribution strategy
        <br/>
        • Focus: Geographic expansion and full product portfolio
        <br/>
        • Goal: $5.8M+ revenue, sustainable profitability
        """
        
        self.add_body_text(gtm_strategy)
        
        # Sales channel strategy
        channel_data = [
            ['Sales Channel', 'Target Customers', 'Value Proposition', 'Revenue %'],
            ['Direct Sales', 'Large fabricators, contractors', 'Full service, technical support', '70%'],
            ['Distributor Partners', 'Small-medium manufacturers', 'Local inventory, relationships', '20%'],
            ['Online/Emergency', 'Maintenance, urgent needs', 'Fast delivery, availability', '10%']
        ]
        
        self.add_table(channel_data, [1.3, 1.8, 1.6, 1.3], title="Sales Channel Strategy")
        
        customer_acquisition = """
        <b>Customer Acquisition Strategy:</b>
        <br/>
        • <b>Direct Outreach:</b> Target top 50 potential customers with direct sales
        <br/>
        • <b>Industry Events:</b> Trade shows, technical conferences, and industry meetings
        <br/>
        • <b>Referral Program:</b> Incentives for customer referrals and testimonials
        <br/>
        • <b>Technical Leadership:</b> Thought leadership through technical publications
        <br/>
        • <b>Government Relations:</b> Leverage Canadian content preferences
        <br/>
        
        <b>Key Success Metrics:</b>
        <br/>
        • Customer acquisition: 5-10 new customers annually
        <br/>
        • Average deal size: $50K-$200K annually per customer
        <br/>
        • Customer retention: 90%+ annual retention rate
        <br/>
        • Sales cycle: 3-6 months average from lead to first order
        <br/>
        • Win rate: 60%+ for qualified opportunities
        """
        
        self.add_body_text(customer_acquisition)
    
    def _add_funding_ask_slide(self):
        """Slide 12: The Ask (Funding)"""
        self._add_slide_header(12, "Investment Opportunity")
        
        funding_ask = """
        <b>Seeking $200K-$300K Series A Investment</b>
        <br/>
        
        <b>The Ask:</b>
        <br/>
        • Total Funding Requirement: CAD $200,000-$300,000
        <br/>
        • Investment Type: Equity or convertible preferred shares
        <br/>
        • Use Period: 18-24 months to achieve cash flow positive
        <br/>
        • Investor Profile: Strategic investors or experienced angels
        """
        
        self.add_body_text(funding_ask)
        
        # Funding sources breakdown
        funding_sources_data = [
            ['Funding Source', 'Amount Range', 'Terms', 'Probability'],
            ['Founder Investment', '$50K-$75K', 'Equity', 'Committed'],
            ['Angel Investors', '$75K-$125K', 'Equity/Convertible', 'High'],
            ['Government Grants', '$25K-$100K', 'Grant/Loan', 'Medium'],
            ['Equipment Financing', '$40K-$80K', 'Secured Loan', 'High'],
            ['Strategic Partners', '$100K-$200K', 'Equity/Revenue Share', 'Medium']
        ]
        
        self.add_table(funding_sources_data, [1.4, 1.2, 1.2, 1.2], title="Funding Sources Strategy")
        
        investor_benefits = """
        <b>Investor Value Proposition:</b>
        <br/>
        • <b>Market Opportunity:</b> $150M+ addressable market with 4.1% annual growth
        <br/>
        • <b>Competitive Advantage:</b> First-mover advantage in local manufacturing
        <br/>
        • <b>Strong Returns:</b> Target IRR of 25-35% for equity investors
        <br/>
        • <b>Scalable Model:</b> Proven processes with expansion potential
        <br/>
        • <b>Experienced Team:</b> Management with track record of success
        <br/>
        
        <b>Exit Opportunities:</b>
        <br/>
        • Strategic acquisition by global welding materials company
        <br/>
        • Management buyout funded by strong cash flows
        <br/>
        • Private equity rollup of regional manufacturers
        <br/>
        • Dividend recapitalization after achieving scale
        <br/>
        
        <b>Risk Mitigation:</b>
        <br/>
        • Phased investment approach with performance milestones
        <br/>
        • Conservative financial projections with upside potential
        <br/>
        • Diversified customer base and market segments
        <br/>
        • Asset-backed investment with tangible equipment value
        """
        
        self.add_body_text(investor_benefits)
    
    def _add_use_of_funds_slide(self):
        """Slide 13: Use of Funds"""
        self._add_slide_header(13, "Use of Investment Funds")
        
        use_of_funds_intro = """
        <b>Strategic Allocation for Maximum Impact</b>
        <br/>
        Investment funds will be allocated to achieve operational milestones and 
        position FluxGen for sustainable growth and profitability.
        """
        
        self.add_body_text(use_of_funds_intro)
        
        # Use of funds breakdown
        use_data = [
            ['Category', 'Amount', 'Percentage', 'Purpose'],
            ['Equipment & Machinery', '$120K-$180K', '60%', 'Production equipment, installation, commissioning'],
            ['Facility & Infrastructure', '$40K-$60K', '20%', 'Building lease/purchase, utilities, site preparation'],
            ['Working Capital', '$30K-$45K', '15%', 'Initial inventory, operating expenses, cash flow'],
            ['Marketing & Business Dev', '$10K-$15K', '5%', 'Customer acquisition, trade shows, marketing materials']
        ]
        
        self.add_table(use_data, [1.8, 1.0, 1.0, 2.2], title="Investment Fund Allocation")
        
        funding_timeline = """
        <b>Fund Deployment Timeline:</b>
        <br/>
        • <b>Months 1-3:</b> Equipment deposits and facility preparation (40%)
        <br/>
        • <b>Months 4-8:</b> Equipment delivery and installation (35%)
        <br/>
        • <b>Months 9-12:</b> Working capital and operational ramp-up (20%)
        <br/>
        • <b>Months 13+:</b> Marketing and business development (5%)
        <br/>
        
        <b>Milestone-Based Investment:</b>
        <br/>
        • Tranche 1 ($100K): Site secured, equipment ordered
        <br/>
        • Tranche 2 ($100K): Equipment installed, permits obtained
        <br/>
        • Tranche 3 ($50K+): Production trials successful, first customer orders
        <br/>
        
        <b>ROI Acceleration:</b>
        <br/>
        • Faster time to market with adequate funding
        <br/>
        • Higher quality equipment improving efficiency and margins
        <br/>
        • Professional marketing accelerating customer acquisition
        <br/>
        • Working capital supporting larger customer orders
        <br/>
        
        <b>Alternative Scenario:</b>
        With minimum funding ($150K), FluxGen can achieve break-even but with 
        longer timeline and reduced market penetration speed.
        """
        
        self.add_body_text(funding_timeline)
    
    def _add_contact_slide(self):
        """Slide 14: Contact & Next Steps"""
        self._add_slide_header(14, "Next Steps & Contact Information")
        
        if self.company_info:
            contact_info = f"""
            <b>Ready to Move Forward</b>
            <br/>
            <b>Contact Information:</b><br/>
            {self.company_info.get('legal_name', 'FluxGen Industries Ltd.')}<br/>
            Location: {self.company_info.get('location', 'Airdrie')}, {self.company_info.get('province', 'Alberta')}<br/>
            Website: {self.company_info.get('website', 'www.fluxgen.ca')}<br/>
            Email: {self.company_info.get('primary_email', 'info@fluxgen.ca')}<br/>
            Phone: {self.company_info.get('primary_phone', '+1 (403) XXX-XXXX')}
            """
        else:
            contact_info = """
            <b>Ready to Move Forward</b>
            <br/>
            <b>Contact Information:</b>
            FluxGen Industries Ltd.
            Location: Airdrie, Alberta
            Website: www.fluxgen.ca
            Email: info@fluxgen.ca
            """
        
        self.add_body_text(contact_info)
        
        # Team contact info if available
        team_members = self.db.get_team_members()
        if team_members:
            team_contacts_data = [['Name', 'Role', 'Contact Information']]
            
            for member in team_members[:3]:  # Show top 3 team members
                contact_details = []
                if member.get('email'):
                    contact_details.append(member['email'])
                if member.get('phone'):
                    contact_details.append(member['phone'])
                
                team_contacts_data.append([
                    member.get('name', 'TBD'),
                    member.get('role', 'Team Member'),
                    ' | '.join(contact_details) if contact_details else 'Contact through main number'
                ])
            
            self.add_table(team_contacts_data, [1.5, 1.5, 3.0], title="Key Team Contacts")
        
        next_steps = """
        <b>Immediate Next Steps:</b>
        <br/>
        • Due diligence package available upon request
        <br/>
        • Facility site visits and equipment demonstrations
        <br/>
        • Customer reference calls and market validation
        <br/>
        • Financial model review and sensitivity analysis
        <br/>
        • Investment term sheet and legal documentation
        <br/>
        
        <b>Timeline for Investment Decision:</b>
        <br/>
        • Initial discussion and interest confirmation: 1-2 weeks
        <br/>
        • Due diligence and documentation review: 2-4 weeks  
        <br/>
        • Final investment decision and legal closure: 2-3 weeks
        <br/>
        • Target funding completion: 6-8 weeks from initial contact
        <br/>
        
        <b>Ready to Partner:</b>
        FluxGen Industries represents a compelling investment opportunity in Western Canada's 
        growing industrial manufacturing sector. We're seeking strategic partners who share 
        our vision of building a leading regional manufacturer.
        <br/>
        <b>Thank you for your consideration. We look forward to discussing this opportunity.</b>
        """
        
        self.add_body_text(next_steps)
    
    def generate(self) -> Path:
        """Generate the Pitch Deck PDF"""
        self.story = []  # Reset story
        self.build_content()
        
        filename = f"fluxgen_pitch_deck_{self._get_timestamp()}"
        return self.generate_document(filename, "FluxGen Industries - Investment Pitch Deck")
    
    def _get_timestamp(self) -> str:
        """Get timestamp for filename"""
        from datetime import datetime
        return datetime.now().strftime('%Y%m%d_%H%M%S')