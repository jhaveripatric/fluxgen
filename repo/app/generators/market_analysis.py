"""
Market Analysis document generator for FluxGen
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.base import BaseDocumentGenerator
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class MarketAnalysisGenerator(BaseDocumentGenerator):
    """Generates Market Analysis document (5-7 pages)"""
    
    def __init__(self, database_manager, output_dir: Path):
        super().__init__(database_manager, output_dir)
    
    def build_content(self):
        """Build market analysis content"""
        # Document title and company header
        self.add_company_header()
        self.add_title("Market Analysis & Competitive Assessment")
        
        # Executive Summary
        self._add_market_executive_summary()
        
        # Industry Overview
        self._add_industry_overview()
        self.add_page_break()
        
        # Target Markets
        self._add_target_markets()
        
        # Competitive Landscape
        self._add_competitive_landscape()
        self.add_page_break()
        
        # Market Size & Growth
        self._add_market_size_growth()
        
        # Customer Segments
        self._add_customer_segments()
        self.add_page_break()
        
        # Pricing Strategy
        self._add_pricing_strategy()
        
        # Market Entry Strategy
        self._add_market_entry_strategy()
        
        # Footer
        self.add_footer_info()
    
    def _add_market_executive_summary(self):
        """Add market executive summary"""
        self.add_heading1("Market Executive Summary")
        
        summary_text = """
        The Canadian welding consumables market presents a significant opportunity for FluxGen Industries, 
        with an addressable market size of CAD $150-200 million annually in Western Canada alone.
        <br/>
        <b>Key Market Drivers:</b>
        <br/>
        • Infrastructure renewal and expansion across Canada
        <br/>
        • Oil & gas pipeline construction and maintenance
        <br/>
        • Growing demand for locally-sourced industrial materials
        <br/>
        • Supply chain resilience requirements post-COVID-19
        <br/>
        • Government emphasis on domestic manufacturing capacity
        <br/>
        
        <b>Market Opportunity:</b>
        <br/>
        • 80%+ of welding flux currently imported from Asia and Eastern US
        <br/>
        • Limited local suppliers with inconsistent quality and delivery
        <br/>
        • Strong customer preference for technical support and rapid delivery
        <br/>
        • Premium pricing opportunity for superior quality and service
        <br/>
        
        <b>Competitive Advantage:</b>
        FluxGen is positioned to capture market share through local manufacturing, superior customer service, 
        technical expertise, and competitive pricing while maintaining higher margins than import-dependent competitors.
        """
        
        self.add_body_text(summary_text)
        self.add_spacer()
    
    def _add_industry_overview(self):
        """Add industry overview section"""
        self.add_heading1("SAW Flux Industry Overview")
        
        self.add_heading2("Industry Structure & Value Chain")
        
        industry_text = """
        The Submerged Arc Welding (SAW) flux industry is a specialized segment of the broader welding consumables market. 
        SAW flux is essential for high-volume, high-quality welding applications in heavy industry.
        
        <br/>
        <b>Value Chain Components:</b>
        <br/>
        • Raw Material Suppliers (silica, dolomite, calcite, alloys)
        <br/>
        • Flux Manufacturers (blending, agglomeration, quality control)
        <br/>
        • Distributors and Resellers
        <br/>
        • End-User Customers (fabricators, contractors, manufacturers)
        <br/>
        • Technical Support and Application Engineering
        <br/>
        
        <b>Industry Characteristics:</b>
        <br/>
        • Highly technical products requiring specialized knowledge
        <br/>
        • Quality and consistency critical for welding performance
        <br/>
        • Long customer relationships and high switching costs
        <br/>
        • Cyclical demand tied to construction and energy sectors
        <br/>
        • Regulatory compliance requirements (AWS, CWB standards)
        """
        
        self.add_body_text(industry_text)
        
        # Industry statistics table
        industry_data = [
            ['Market Metric', 'Global', 'North America', 'Canada', 'Western Canada'],
            ['Market Size (CAD)', '$8.5 billion', '$2.1 billion', '$350 million', '$150 million'],
            ['Annual Growth Rate', '3.2%', '2.8%', '3.5%', '4.1%'],
            ['Import Dependency', '25%', '35%', '65%', '80%'],
            ['Key Applications', 'Infrastructure', 'Energy, Infrastructure', 'Oil & Gas, Infrastructure', 'Oil & Gas'],
            ['Avg. Price ($/kg)', '$4.50-$8.00', '$5.00-$9.00', '$5.50-$10.00', '$6.00-$11.00']
        ]
        
        self.add_table(industry_data, [1.5, 1.3, 1.3, 1.3, 1.6], title="Industry Market Overview")
        
        self.add_heading2("Industry Trends & Drivers")
        
        trends_text = """
        <b>Growth Drivers:</b>
        <br/>
        • Infrastructure spending: $180+ billion committed by Canadian governments
        <br/>
        • Energy transition projects: Pipeline upgrades, renewable energy infrastructure
        <br/>
        • Manufacturing reshoring: Bringing production back to North America
        <br/>
        • Quality requirements: Increasing demands for certified, traceable materials
        <br/>
        • Supply chain localization: Reduced dependency on offshore suppliers
        <br/>
        
        <b>Technology Trends:</b>
        <br/>
        • Automated welding systems requiring consistent, high-quality flux
        <br/>
        • Environmental regulations driving cleaner, more efficient formulations
        <br/>
        • Digitalization enabling better inventory management and ordering
        <br/>
        • Custom formulations for specific applications and customer requirements
        <br/>
        
        <b>Market Challenges:</b>
        <br/>
        • Raw material price volatility
        <br/>
        • Skilled labor shortages in manufacturing and welding
        <br/>
        • Economic cyclicality affecting construction and energy sectors
        <br/>
        • Regulatory compliance and certification requirements
        """
        
        self.add_body_text(trends_text)
        self.add_spacer()
    
    def _add_target_markets(self):
        """Add target markets section"""
        self.add_heading1("Target Markets & Applications")
        
        # Market segments table
        segments_data = [
            ['Market Segment', 'Size (CAD)', 'Growth Rate', 'Key Applications', 'FluxGen Opportunity'],
            ['Oil & Gas', '$60 million', '5.2%', 'Pipelines, refineries, petrochemical', 'High - local advantage'],
            ['Infrastructure', '$45 million', '4.8%', 'Bridges, buildings, transit', 'High - government spending'],
            ['Manufacturing', '$30 million', '3.5%', 'Equipment, pressure vessels', 'Medium - diverse needs'],
            ['Marine & Offshore', '$15 million', '2.8%', 'Ships, platforms, ports', 'Medium - specialized needs'],
            ['Total Addressable Market', '$150 million', '4.1%', 'All segments', 'Target 3-5% share']
        ]
        
        self.add_table(segments_data, [1.5, 1.0, 1.0, 1.8, 1.7], title="Western Canada Market Segments")
        
        self.add_heading2("Geographic Markets")
        
        geographic_text = """
        <b>Phase 1 Markets (Years 1-2): Alberta & Saskatchewan</b>
        <br/>
        • Primary focus: Calgary, Edmonton, Saskatoon corridors
        <br/>
        • Target customers: Major fabricators, energy contractors
        <br/>
        • Market size: CAD $85-100 million annually
        <br/>
        • Competition: Limited local suppliers, mainly distributors
        <br/>
        • Advantages: Proximity, technical support, rapid delivery
        <br/>
        
        <b>Phase 2 Markets (Years 3-4): Western Canada Expansion</b>
        <br/>
        • British Columbia: Vancouver, Prince George industrial areas
        <br/>
        • Manitoba: Winnipeg manufacturing and agriculture sectors
        <br/>
        • Market size: Additional CAD $50-65 million annually
        <br/>
        • Strategy: Distributor partnerships and direct sales
        <br/>
        
        <b>Phase 3 Markets (Years 5+): Central Canada & Northern US</b>
        <br/>
        • Ontario: Toronto-Hamilton-Oshawa manufacturing belt
        <br/>
        • Northern US States: Montana, North Dakota energy sectors
        <br/>
        • Market size: CAD $200+ million additional opportunity
        <br/>
        • Approach: Strategic partnerships or satellite facilities
        """
        
        self.add_body_text(geographic_text)
        
        self.add_heading2("Customer Application Analysis")
        
        applications_text = """
        <b>Pipeline Construction & Maintenance:</b>
        <br/>
        • High-volume SAW applications for mainline pipe welding
        <br/>
        • Critical quality requirements for pressure vessel standards
        <br/>
        • Seasonal demand patterns with rush periods
        <br/>
        • Long-term contracts with established contractors
        <br/>
        
        <b>Structural Steel Fabrication:</b>
        <br/>
        • Building construction, bridge fabrication
        <br/>
        • Consistent quality requirements for certified welders
        <br/>
        • Local sourcing preferred for just-in-time delivery
        <br/>
        • Growing market with infrastructure investments
        <br/>
        
        <b>Heavy Equipment Manufacturing:</b>
        <br/>
        • Agriculture, mining, construction equipment
        <br/>
        • Custom flux formulations for specific applications
        <br/>
        • Technical support and application engineering valued
        <br/>
        • Established supplier relationships but open to local alternatives
        <br/>
        
        <b>Shipbuilding & Marine:</b>
        <br/>
        • Specialized flux requirements for marine environments
        <br/>
        • High-quality standards for safety-critical applications
        <br/>
        • Limited local suppliers creating opportunity
        <br/>
        • Government procurement preferences for Canadian suppliers
        """
        
        self.add_body_text(applications_text)
        self.add_spacer()
    
    def _add_competitive_landscape(self):
        """Add competitive landscape section"""
        self.add_heading1("Competitive Landscape Analysis")
        
        # Competitive analysis table
        competitors_data = [
            ['Competitor', 'Type', 'Strengths', 'Weaknesses', 'Market Share'],
            ['Lincoln Electric', 'Global Manufacturer', 'Brand, technology, distribution', 'Price, lead times', '25%'],
            ['ESAB', 'Global Manufacturer', 'Product range, quality', 'Limited local presence', '20%'],
            ['Regional Distributors', 'Distribution', 'Relationships, inventory', 'No manufacturing, margins', '30%'],
            ['Asian Imports', 'Import/Distribution', 'Low cost, volume', 'Quality, delivery, support', '20%'],
            ['FluxGen Opportunity', 'Local Manufacturer', 'Local, quality, service', 'Scale, brand recognition', '3-5% target']
        ]
        
        self.add_table(competitors_data, [1.3, 1.2, 1.6, 1.6, 1.3], title="Competitive Market Share Analysis")
        
        self.add_heading2("Competitive Positioning")
        
        positioning_text = """
        <b>Global Manufacturers (Lincoln Electric, ESAB, Miller):</b>
        <br/>
        • Strengths: Established brands, broad product lines, technical resources
        <br/>
        • Weaknesses: Higher prices, longer lead times, limited local support
        <br/>
        • Market Position: Premium segment, large customers
        <br/>
        • FluxGen Strategy: Compete on service, delivery, and local technical support
        <br/>
        
        <b>Regional Distributors:</b>
        <br/>
        • Strengths: Local relationships, inventory, established sales channels
        <br/>
        • Weaknesses: No manufacturing control, margin pressure, limited technical expertise
        <br/>
        • Market Position: Mid-market, relationship-based sales
        <br/>
        • FluxGen Strategy: Direct sales to large customers, partner with distributors for smaller accounts
        <br/>
        
        <b>Asian Import Suppliers:</b>
        <br/>
        • Strengths: Low manufacturing costs, high volume capacity
        <br/>
        • Weaknesses: Quality consistency, long lead times, limited technical support
        <br/>
        • Market Position: Price-sensitive segments
        <br/>
        • FluxGen Strategy: Compete on quality, reliability, and local presence
        """
        
        self.add_body_text(positioning_text)
        
        # Competitive advantages table
        advantages_data = [
            ['Competitive Factor', 'FluxGen Advantage', 'Competitor Challenge', 'Customer Benefit'],
            ['Lead Times', '1-2 week delivery', '4-8 week import times', 'Reduced inventory, faster projects'],
            ['Technical Support', 'Local application engineers', 'Remote or no support', 'Better welding performance'],
            ['Quality Control', 'Batch traceability', 'Limited visibility', 'Consistent weld quality'],
            ['Custom Formulations', 'Flexible production', 'Minimum order quantities', 'Optimized applications'],
            ['Emergency Supply', '24-48 hour response', 'Stock-out delays', 'Project continuity'],
            ['Pricing Transparency', 'Direct manufacturer pricing', 'Multiple markups', 'Lower total cost']
        ]
        
        self.add_table(advantages_data, [1.3, 1.3, 1.3, 1.1], title="FluxGen Competitive Advantages")
        
        self.add_spacer()
    
    def _add_market_size_growth(self):
        """Add market size and growth section"""
        self.add_heading1("Market Size & Growth Projections")
        
        # Market size projections
        market_size_data = [
            ['Market Segment', '2024', '2025', '2026', '2027', '2029', 'CAGR'],
            ['Oil & Gas SAW Flux', '$60M', '$63M', '$67M', '$71M', '$79M', '5.2%'],
            ['Infrastructure', '$45M', '$47M', '$50M', '$53M', '$59M', '4.8%'],
            ['Manufacturing', '$30M', '$31M', '$32M', '$34M', '$37M', '3.5%'],
            ['Marine & Offshore', '$15M', '$15M', '$16M', '$16M', '$18M', '2.8%'],
            ['Total Western Canada', '$150M', '$156M', '$165M', '$174M', '$193M', '4.1%'],
            ['FluxGen Target Share', '0.5%', '2.0%', '3.5%', '4.5%', '6.0%', ''],
            ['FluxGen Revenue Target', '$0.75M', '$3.1M', '$5.8M', '$7.8M', '$11.6M', '98% CAGR']
        ]
        
        self.add_table(market_size_data, [1.5, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5], title="5-Year Market Size & Growth Projections")
        
        self.add_heading2("Market Growth Drivers")
        
        growth_text = """
        <b>Infrastructure Investment Programs:</b>
        <br/>
        • Federal Infrastructure Plan: $180+ billion over 12 years
        <br/>
        • Provincial infrastructure spending: $25+ billion annually in Western Canada
        <br/>
        • Municipal infrastructure renewal: Aging bridges, water systems, transit
        <br/>
        • Green infrastructure: Clean energy, environmental projects
        <br/>
        
        <b>Energy Sector Developments:</b>
        <br/>
        • Pipeline expansion and replacement projects (TMX, Coastal GasLink)
        <br/>
        • Oil sands facility expansions and upgrades
        <br/>
        • Renewable energy infrastructure (wind, solar, hydrogen)
        <br/>
        • Carbon capture and storage facility construction
        <br/>
        
        <b>Manufacturing Sector Growth:</b>
        <br/>
        • Agricultural equipment manufacturing expansion
        <br/>
        • Mining equipment and services growth
        <br/>
        • Aerospace and defense manufacturing
        <br/>
        • Clean technology manufacturing incentives
        <br/>
        
        <b>Supply Chain Localization Trends:</b>
        <br/>
        • Government "Buy Canadian" policies
        <br/>
        • Corporate supply chain risk mitigation strategies 
        <br/> 
        • Reduced dependency on offshore suppliers
        <br/>
        • Shorter supply chains for better responsiveness
        """
        
        self.add_body_text(growth_text)
        
        # Market penetration strategy
        penetration_data = [
            ['Year', 'Target Customers', 'Market Share Goal', 'Revenue Target', 'Key Strategies'],
            ['Year 1', '3-5 pilot customers', '0.5%', '$0.75M', 'Product validation, quality demonstration'],
            ['Year 2', '8-12 active customers', '2.0%', '$3.1M', 'Capacity scaling, distributor partnerships'],
            ['Year 3', '15-20 customers', '3.5%', '$5.8M', 'Geographic expansion, product line extension'],
            ['Year 4', '25-30 customers', '4.5%', '$7.8M', 'Market leadership, customer retention'],
            ['Year 5', '35+ customers', '6.0%', '$11.6M', 'Regional dominance, new market entry']
        ]
        
        self.add_table(penetration_data, [0.8, 1.5, 1.2, 1.2, 2.3], title="Market Penetration Strategy")
        
        self.add_spacer()
    
    def _add_customer_segments(self):
        """Add customer segments section"""
        self.add_heading1("Customer Segment Analysis")
        
        self.add_heading2("Primary Customer Segments")
        
        # Customer segment profiles
        segments_profile_data = [
            ['Segment', 'Company Size', 'Annual SAW Usage', 'Decision Factors', 'Sales Approach'],
            ['Tier 1 Fabricators', '$50M+ revenue', '100+ tons/year', 'Quality, reliability, cost', 'Direct sales, technical support'],
            ['Regional Contractors', '$10-50M revenue', '20-100 tons/year', 'Delivery, service, relationship', 'Direct sales, local presence'],
            ['Specialty Manufacturers', '$5-25M revenue', '5-50 tons/year', 'Custom products, expertise', 'Technical partnership'],
            ['Maintenance Operations', 'Various sizes', '1-20 tons/year', 'Availability, fast delivery', 'Distributor channel'],
            ['Government/Municipal', 'Public sector', '10-100 tons/year', 'Canadian content, compliance', 'Direct tender response']
        ]
        
        self.add_table(segments_profile_data, [1.4, 1.2, 1.2, 1.4, 1.8], title="Customer Segment Profiles")
        
        self.add_heading2("Customer Needs Analysis")
        
        customer_needs_text = """
        <b>Large Fabricators & Contractors:</b>
        <br/>
        • Consistent quality and performance across large volumes
        <br/>
        • Reliable delivery schedules to support project timelines
        <br/>
        • Technical support for complex welding applications
        <br/>
        • Competitive pricing with volume discounts
        <br/>
        • Vendor certification and quality documentation
        <br/>
        • Emergency supply capability for critical projects
        <br/>
        
        <b>Mid-Size Manufacturing Companies:</b>
        <br/>
        • Flexible order quantities and packaging options
        <br/>
        • Local technical support and application assistance
        <br/>
        • Competitive pricing without volume commitments
        <br/>
        • Fast delivery for just-in-time manufacturing
        <br/>
        • Product customization for specific applications
        <br/>
        • Strong supplier relationships and account management
        <br/>
        
        <b>Maintenance & Repair Operations:</b>
        <br/>
        • Wide product range for diverse repair needs
        <br/>
        • Emergency availability for critical equipment repairs
        <br/>
        • Small packaging for occasional use
        <br/>
        • Technical guidance for proper product selection
        <br/>
        • Local inventory and rapid delivery
        <br/>
        • Flexible payment terms
        """
        
        self.add_body_text(customer_needs_text)
        
        # Customer acquisition strategy
        acquisition_data = [
            ['Customer Type', 'Acquisition Strategy', 'Value Proposition', 'Sales Cycle', 'Success Metrics'],
            ['Major Fabricators', 'Direct sales, technical demos', 'Quality, service, local supply', '6-12 months', 'Contract wins, volume growth'],
            ['Regional Contractors', 'Relationship building, referrals', 'Reliability, fast delivery', '3-6 months', 'Repeat orders, expansion'],
            ['Manufacturers', 'Technical partnership, trials', 'Custom solutions, expertise', '6-9 months', 'Long-term partnerships'],
            ['Distributors', 'Channel partnerships', 'Margins, support, training', '3-4 months', 'Sales growth, territory coverage'],
            ['Government', 'Tender responses, compliance', 'Canadian content, quality', '9-18 months', 'Contract awards, renewals']
        ]
        
        self.add_table(acquisition_data, [1.2, 1.5, 1.3, 1.0, 1.0], title="Customer Acquisition Strategies")
        
        self.add_spacer()
    
    def _add_pricing_strategy(self):
        """Add pricing strategy section"""
        self.add_heading1("Pricing Strategy & Market Positioning")
        
        # Pricing analysis table
        pricing_data = [
            ['Product Category', 'Import Price', 'Distributor Price', 'FluxGen Target', 'Value Justification'],
            ['Standard SAW Flux', '$4.50-5.50/kg', '$6.00-7.00/kg', '$5.75-6.50/kg', 'Local supply, quality, service'],
            ['Specialty Formulations', '$6.00-8.00/kg', '$8.00-10.00/kg', '$7.50-9.00/kg', 'Custom solutions, technical support'],
            ['Emergency/Rush Orders', '$7.00-9.00/kg', '$10.00-12.00/kg', '$9.00-11.00/kg', 'Rapid response, availability'],
            ['Volume Contracts', '$4.00-5.00/kg', '$5.50-6.50/kg', '$5.25-6.00/kg', 'Consistency, reliability, local'],
            ['Government Contracts', '$5.00-6.50/kg', '$6.50-8.00/kg', '$6.00-7.25/kg', 'Canadian content, compliance']
        ]
        
        self.add_table(pricing_data, [1.4, 1.2, 1.2, 1.2, 1.0], title="Competitive Pricing Analysis")
        
        self.add_heading2("Value-Based Pricing Strategy")
        
        pricing_text = """
        <b>Pricing Philosophy:</b>
        <br/>
        FluxGen employs value-based pricing that reflects the total cost of ownership benefits 
        <br/>
        provided to customers, including reduced inventory costs, faster delivery, and technical support.
        <br/>
        
        <b>Pricing Components:</b>
        <br/>
        • Base Product Cost: Competitive with imports + local value premium
        <br/>
        • Service Premium: 10-15% for technical support and rapid delivery
        <br/>
        • Customization Premium: 15-25% for custom formulations
        <br/>
        • Emergency Premium: 30-50% for rush orders and critical supply
        <br/>
        • Volume Discounts: 5-15% for large contracts and loyal customers
        <br/>
        
        <b>Competitive Positioning:</b>
        <br/>
        • Position between import prices and premium distributor markups
        <br/>
        • Justify premium through superior value proposition
        <br/>
        • Maintain pricing flexibility for market penetration
        <br/>
        • Focus on total cost of ownership, not just unit price
        <br/>
        
        <b>Dynamic Pricing Factors:</b>
        <br/>
        • Raw material cost fluctuations (quarterly adjustments)
        <br/>
        • Market demand and capacity utilization
        <br/>
        • Competitive responses and market conditions
        <br/>
        • Customer relationship and volume commitments
        <br/>
        • Geographic market differences and logistics costs
        """
        
        self.add_body_text(pricing_text)
        
        # Total cost of ownership comparison
        tco_data = [
            ['Cost Component', 'Import Supplier', 'Regional Distributor', 'FluxGen Advantage'],
            ['Product Price ($/kg)', '$5.00', '$6.50', '$6.00'],
            ['Shipping & Logistics', '$0.75', '$0.25', '$0.20'],
            ['Inventory Carrying Cost', '$0.60', '$0.30', '$0.15'],
            ['Quality Risk/Rework', '$0.40', '$0.20', '$0.05'],
            ['Emergency Premium', '$2.00', '$1.50', '$0.75'],
            ['Technical Support Cost', '$0.50', '$0.25', '$0.00'],
            ['Total Cost of Ownership', '$9.25', '$8.00', '$7.15'],
            ['FluxGen Advantage', '', '10.6% savings', '12.6% savings']
        ]
        
        self.add_table(tco_data, [1.6, 1.2, 1.4, 1.8], title="Total Cost of Ownership Analysis")
        
        self.add_spacer()
    
    def _add_market_entry_strategy(self):
        """Add market entry strategy section"""
        self.add_heading1("Market Entry & Growth Strategy")
        
        self.add_heading2("Go-to-Market Strategy")
        
        entry_strategy_text = """
        <b>Phase 1: Market Entry (Months 1-12)</b>
        <br/>
        • Focus: Proof of concept with 3-5 pilot customers
        <br/>
        • Approach: Direct sales with heavy technical support
        <br/>
        • Geography: Calgary-Edmonton corridor (Alberta core market)
        <br/>
        • Products: Standard SAW flux formulations
        <br/>
        • Goals: Product validation, quality demonstration, customer feedback
        <br/>
        
        <b>Phase 2: Market Development (Months 13-24)</b>
        <br/>
        • Focus: Scale customer base to 10-15 active customers
        <br/>
        • Approach: Direct sales plus selective distributor partnerships
        <br/>
        • Geography: Alberta and Saskatchewan expansion
        <br/>
        • Products: Expanded product line, custom formulations
        <br/>
        • Goals: Market penetration, revenue growth, operational efficiency
        <br/>
        
        <b>Phase 3: Regional Expansion (Months 25-36)</b>
        <br/>
        • Focus: Geographic expansion to Western Canada
        <br/>
        • Approach: Multi-channel distribution strategy
        <br/>
        • Geography: British Columbia and Manitoba markets
        <br/>
        • Products: Full product portfolio, specialized applications
        <br/>
        • Goals: Regional market leader, sustainable profitability
        """
        
        self.add_body_text(entry_strategy_text)
        
        # Channel strategy table
        channel_data = [
            ['Sales Channel', 'Target Segment', 'Products', 'Support Level', 'Margin Structure'],
            ['Direct Sales', 'Large fabricators, contractors', 'All products, custom', 'Full technical support', 'Standard margins'],
            ['Distributor Partners', 'Small-medium customers', 'Standard products', 'Training & marketing', 'Distributor margins'],
            ['Online Platform', 'Maintenance, small orders', 'Catalog products', 'Self-service + phone', 'Higher margins'],
            ['Government Tenders', 'Public sector projects', 'Standard & specialty', 'Compliance support', 'Competitive margins'],
            ['OEM Partnerships', 'Equipment manufacturers', 'Custom formulations', 'Application engineering', 'Partnership terms']
        ]
        
        self.add_table(channel_data, [1.2, 1.4, 1.2, 1.2, 1.0], title="Multi-Channel Distribution Strategy")
        
        self.add_heading2("Success Metrics & KPIs")
        
        metrics_text = """
        <b>Market Penetration Metrics:</b>
        <br/>
        • Market share growth: Target 1% annually
        <br/>
        • Customer acquisition: 5-10 new customers per year after Year 1
        <br/>
        • Revenue per customer: $50,000-$200,000 annually
        <br/>
        • Geographic expansion: New territory annually
        <br/>
        • Product penetration: Average 3+ products per customer
        <br/>
        
        <b>Competitive Position Metrics:</b>
        <br/>
        • Win rate vs. competitors: Target 60%+ for qualified opportunities
        <br/>
        • Price premium achievement: 5-15% vs. import alternatives
        <br/>
        • Customer retention rate: 90%+ annual retention
        <br/>
        • Brand recognition: Unaided awareness growth in target markets
        <br/>
        • Technical leadership: Innovation and product development metrics
        <br/>
        
        <b>Operational Excellence Metrics:</b>
        <br/>
        • Order fulfillment: 95%+ on-time delivery
        <br/>
        • Quality performance: <0.5% defect rate
        <br/>
        • Customer satisfaction: 8.5+ NPS score
        <br/>
        • Technical support response: <24 hour response time
        <br/>
        • Emergency supply capability: 48-hour critical delivery
        <br/>
        
        The market analysis demonstrates a clear opportunity for FluxGen to establish a strong position 
        in the Western Canada SAW flux market through superior local service, quality products, and 
        competitive pricing.
        """
        
        self.add_body_text(metrics_text)
        self.add_spacer()
    
    def generate(self) -> Path:
        """Generate the Market Analysis PDF"""
        self.story = []  # Reset story
        self.build_content()
        
        filename = f"fluxgen_market_analysis_{self._get_timestamp()}"
        return self.generate_document(filename, "FluxGen Industries - Market Analysis")
    
    def _get_timestamp(self) -> str:
        """Get timestamp for filename"""
        from datetime import datetime
        return datetime.now().strftime('%Y%m%d_%H%M%S')