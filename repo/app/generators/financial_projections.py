"""
Financial Projections document generator for FluxGen
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.base import BaseDocumentGenerator
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class FinancialProjectionsGenerator(BaseDocumentGenerator):
    """Generates Financial Projections document (4-6 pages)"""
    
    def __init__(self, database_manager, output_dir: Path):
        super().__init__(database_manager, output_dir)
    
    def build_content(self):
        """Build financial projections content"""
        # Document title and company header
        self.add_company_header()
        self.add_title("Financial Projections & Analysis")
        
        # Executive Summary
        self._add_financial_executive_summary()
        
        # CAPEX Breakdown
        self._add_capex_breakdown()
        self.add_page_break()
        
        # OPEX Projections
        self._add_opex_projections()
        
        # Revenue Forecasts
        self._add_revenue_forecasts()
        self.add_page_break()
        
        # Break-even Analysis
        self._add_breakeven_analysis()
        
        # 5-Year P&L Projection
        self._add_profit_loss_projection()
        self.add_page_break()
        
        # Cash Flow Analysis
        self._add_cash_flow_analysis()
        
        # Funding Requirements
        self._add_funding_requirements()
        
        # Financial Assumptions
        self._add_financial_assumptions()
        
        # Footer
        self.add_footer_info()
    
    def _add_financial_executive_summary(self):
        """Add financial executive summary"""
        self.add_heading1("Financial Executive Summary")
        
        financial_summary = self.db.get_financial_summary()
        
        summary_text = f"""
        FluxGen Industries' financial projections demonstrate a viable path to profitability with strong return 
        on investment potential. The phased approach minimizes initial capital requirements while building toward 
        significant revenue generation.
        <br/>
        <b>Key Financial Highlights:</b>
        <br/>
        • Total CAPEX Investment: {self.format_currency(financial_summary.get('total_capex', 0))}
        <br/>
        • Projected Break-even: Month 18-24 of operations
        <br/>
        • 5-Year Revenue Target: CAD $3.5-5.0 million annually
        <br/>
        • Target Gross Margin: 35-45%
        <br/>
        • Projected ROI: 25-35% by Year 3
        <br/>
        
        <b>Investment Strategy:</b>
        The financial plan emphasizes conservative growth with strong cash flow management. Initial investment 
        focuses on essential equipment and working capital, with expansion funded through operational cash flow 
        and targeted growth financing.
        <br/>
        <b>Risk Management:</b>
        Financial projections include sensitivity analysis for key variables including raw material costs, 
        pricing pressures, and demand fluctuations. Multiple scenarios ensure robust planning for various 
        market conditions.
        """
        
        self.add_body_text(summary_text)
        self.add_spacer()
    
    def _add_capex_breakdown(self):
        """Add CAPEX breakdown section"""
        self.add_heading1("Capital Expenditure Analysis")
        
        # Get CAPEX data
        capex_items = self.db.get_investment_capex()
        
        if capex_items:
            # Group by phase
            pilot_items = [item for item in capex_items if item.get('phase') == 'pilot']
            scaleup_items = [item for item in capex_items if item.get('phase') == 'scale-up']
            
            # Pilot Phase CAPEX
            if pilot_items:
                pilot_data = [['Category', 'Description', 'Estimated Cost', 'Notes']]
                pilot_total = 0
                
                for item in pilot_items:
                    cost = item.get('estimated_cost_cad', 0)
                    pilot_total += cost
                    pilot_data.append([
                        item.get('category', 'N/A'),
                        (item.get('description', 'N/A')[:50] + '...') if len(item.get('description', '')) > 50 else item.get('description', 'N/A'),
                        self.format_currency(cost),
                        item.get('notes', 'N/A')[:30] if item.get('notes') else 'N/A'
                    ])
                
                pilot_data.append(['TOTAL PILOT PHASE', '', self.format_currency(pilot_total), ''])
                self.add_table(pilot_data, [1.5, 2.2, 1.3, 2.0], title="Pilot Phase Capital Investment")
            
            # Scale-up Phase CAPEX
            if scaleup_items:
                scaleup_data = [['Category', 'Description', 'Estimated Cost', 'Notes']]
                scaleup_total = 0
                
                for item in scaleup_items:
                    cost = item.get('estimated_cost_cad', 0)
                    scaleup_total += cost
                    scaleup_data.append([
                        item.get('category', 'N/A'),
                        (item.get('description', 'N/A')[:50] + '...') if len(item.get('description', '')) > 50 else item.get('description', 'N/A'),
                        self.format_currency(cost),
                        item.get('notes', 'N/A')[:30] if item.get('notes') else 'N/A'
                    ])
                
                scaleup_data.append(['TOTAL SCALE-UP', '', self.format_currency(scaleup_total), ''])
                self.add_table(scaleup_data, [1.5, 2.2, 1.3, 2.0], title="Scale-Up Phase Capital Investment")
        
        capex_text = """
        <b>Capital Investment Strategy:</b>
        The CAPEX plan is structured in phases to minimize initial investment while building scalable infrastructure. 
        Priority is given to essential production equipment with expansion capabilities built in.
        <br/>
        <b>Equipment Financing:</b>
        <br/>
        • 60-70% equipment purchases, 30-40% leasing for flexibility
        <br/>
        • Vendor financing available for major equipment packages
        <br/>
        • Government incentives and tax credits applied where applicable
        <br/>
        <b>Depreciation Schedule:</b>
        <br/>
        • Manufacturing equipment: 7-10 year straight line
        <br/>
        • Facility improvements: 15-20 year straight line
        <br/>
        • Vehicles and office equipment: 5 year straight line
        """
        
        self.add_body_text(capex_text)
        self.add_spacer()
    
    def _add_opex_projections(self):
        """Add OPEX projections section"""
        self.add_heading1("Operating Expense Projections")
        
        # Sample OPEX projections based on industry standards
        opex_data = [
            ['Expense Category', 'Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5'],
            ['Raw Materials (COGS)', '$120,000', '$480,000', '$1,000,000', '$1,400,000', '$1,750,000'],
            ['Labor & Benefits', '$180,000', '$240,000', '$320,000', '$400,000', '$480,000'],
            ['Utilities & Facility', '$36,000', '$48,000', '$60,000', '$72,000', '$84,000'],
            ['Transportation & Logistics', '$18,000', '$36,000', '$60,000', '$84,000', '$105,000'],
            ['Insurance & Legal', '$24,000', '$30,000', '$36,000', '$42,000', '$48,000'],
            ['Marketing & Sales', '$15,000', '$24,000', '$36,000', '$48,000', '$60,000'],
            ['Professional Services', '$18,000', '$24,000', '$30,000', '$36,000', '$42,000'],
            ['Other Operating Expenses', '$12,000', '$18,000', '$24,000', '$30,000', '$36,000'],
            ['TOTAL OPEX', '$423,000', '$900,000', '$1,566,000', '$2,112,000', '$2,605,000']
        ]
        
        self.add_table(opex_data, [1.8, 1.0, 1.0, 1.0, 1.0, 1.2], title="5-Year Operating Expense Forecast")
        
        opex_text = """
        <b>Operating Expense Assumptions:</b>
        <br/>
        <b>Raw Materials (COGS):</b> Variable costs estimated at 50-60% of revenue, improving with scale and 
        operational efficiency. Based on current supplier quotes and long-term supply agreements.
        <br/>
        <b>Labor & Benefits:</b> Includes production, quality control, administrative, and management personnel. 
        Assumes 3-5% annual wage increases and comprehensive benefits package.
        <br/>
        <b>Utilities & Facility:</b> Power consumption for production equipment, facility heating/cooling, 
        water usage, and facility lease/maintenance costs.
        <br/>
        <b>Transportation & Logistics:</b> Inbound raw materials, outbound finished goods, equipment maintenance, 
        and emergency deliveries. Scales with production volume.
        <br/>
        <b>Fixed vs. Variable Costs:</b>
        <br/>
        • Fixed Costs (60%): Labor, facility, insurance, professional services
        <br/>
        • Variable Costs (40%): Raw materials, transportation, utilities
        
        This structure provides operational leverage as production scales, improving margins at higher volumes.
        """
        
        self.add_body_text(opex_text)
        self.add_spacer()
    
    def _add_revenue_forecasts(self):
        """Add revenue forecasts section"""
        self.add_heading1("Revenue Forecasts & Market Projections")
        
        # Get production targets
        production_targets = self.db.get_production_targets()
        
        # Revenue projections table
        revenue_data = [
            ['Metric', 'Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5'],
            ['Production Volume (kg)', '6,000', '24,000', '48,000', '60,000', '72,000'],
            ['Average Selling Price ($/kg)', '$5.00', '$5.25', '$5.50', '$5.75', '$6.00'],
            ['Gross Revenue', '$30,000', '$126,000', '$264,000', '$345,000', '$432,000'],
            ['Volume Discounts & Returns', '$3,000', '$6,300', '$10,560', '$13,800', '$17,280'],
            ['Net Revenue', '$27,000', '$119,700', '$253,440', '$331,200', '$414,720'],
            ['Monthly Growth Rate', '5%', '8%', '12%', '8%', '6%'],
            ['Market Share (Western Canada)', '0.5%', '2.0%', '3.5%', '4.2%', '5.0%']
        ]
        
        self.add_table(revenue_data, [1.8, 1.0, 1.0, 1.0, 1.0, 1.2], title="5-Year Revenue Projections")
        
        # Market analysis by segment
        segment_data = [
            ['Market Segment', 'Year 3 Revenue', '% of Total', 'Growth Potential', 'Key Customers'],
            ['Oil & Gas', '$101,000', '40%', 'High', 'Pipeline contractors, refineries'],
            ['Infrastructure', '$76,000', '30%', 'Medium', 'Bridge builders, municipal projects'],
            ['Manufacturing', '$51,000', '20%', 'High', 'Equipment manufacturers, fabricators'],
            ['Marine & Offshore', '$25,000', '10%', 'Medium', 'Shipyards, offshore platforms']
        ]
        
        self.add_table(segment_data, [1.5, 1.2, 1.2, 1.5, 1.6], title="Revenue by Market Segment (Year 3)")
        
        revenue_text = """
        <b>Revenue Assumptions & Methodology:</b>
        <br/>
        <b>Pricing Strategy:</b>
        <br/>
        • Competitive pricing vs. imported alternatives
        <br/>
        • Premium for local supply and technical support (5-10%)
        <br/>
        • Annual price adjustments based on raw material costs and market conditions
        <br/>
        • Volume discounts for large customers (5-15%)
        <br/>
        <b>Sales Channels:</b>
        <br/>
        • Direct sales to large customers (70% of revenue)
        <br/>
        • Distributor partnerships for smaller customers (20% of revenue)
        <br/>
        • Online sales and emergency orders (10% of revenue)
        <br/>
        <b>Customer Acquisition:</b>
        <br/>
        • Year 1: 3-5 pilot customers
        <br/>
        • Year 2: 8-12 active customers  
        <br/>
        • Year 3+: 15-25 regular customers with recurring orders
        <br/>
        <b>Market Penetration:</b>
        Conservative estimates based on capturing 0.5-5% of addressable Western Canada market over 5 years.
        """
        
        self.add_body_text(revenue_text)
        self.add_spacer()
    
    def _add_breakeven_analysis(self):
        """Add break-even analysis section"""
        self.add_heading1("Break-Even Analysis")
        
        # Break-even calculations
        breakeven_data = [
            ['Analysis Component', 'Value', 'Calculation', 'Notes'],
            ['Fixed Costs (Monthly)', '$28,500', 'Avg monthly fixed expenses', 'Labor, facility, insurance, admin'],
            ['Variable Cost per Unit', '$3.50', 'Per kg produced', 'Raw materials, transportation, variable labor'],
            ['Average Selling Price', '$5.50', 'Per kg sold', 'Blended price across all products'],
            ['Contribution Margin', '$2.00', 'ASP minus variable cost', '36% contribution margin'],
            ['Break-even Volume', '14,250 kg', 'Fixed costs ÷ contribution margin', 'Monthly break-even point'],
            ['Break-even Revenue', '$78,375', 'Break-even volume × ASP', 'Monthly revenue needed'],
            ['Time to Break-even', '18-24 months', 'Based on production ramp', 'Includes learning curve effects']
        ]
        
        self.add_table(breakeven_data, [1.8, 1.2, 1.8, 2.2], title="Break-Even Analysis Summary")
        
        # Sensitivity analysis
        sensitivity_data = [
            ['Scenario', 'Price Change', 'Volume Change', 'Break-even (kg)', 'Time to Break-even'],
            ['Base Case', '$5.50', '100%', '14,250', '20 months'],
            ['Optimistic', '$6.00', '110%', '11,600', '16 months'],
            ['Conservative', '$5.00', '85%', '19,000', '28 months'],
            ['Stress Test', '$4.50', '75%', '28,500', '36+ months']
        ]
        
        self.add_table(sensitivity_data, [1.2, 1.2, 1.2, 1.4, 1.0], title="Break-Even Sensitivity Analysis")
        
        breakeven_text = """
        <b>Break-Even Insights:</b>
        <br/>
        The break-even analysis demonstrates that FluxGen can achieve profitability within 18-24 months of 
        operations, assuming steady production ramp and market acceptance.
        <br/>
        <b>Key Success Factors:</b>
        <br/>
        • Achieving 70%+ capacity utilization by month 18
        <br/>
        • Maintaining gross margins of 35%+ through efficient operations
        <br/>
        • Building recurring customer base with predictable order patterns
        <br/>
        • Managing working capital effectively during growth phase
        <br/>
        <b>Risk Mitigation:</b>
        <br/>
        • Conservative volume assumptions provide buffer for market challenges
        <br/>
        • Flexible cost structure allows rapid adjustment to demand changes
        <br/>
        • Multiple revenue streams reduce dependency on single customers
        <br/>
        • Strong supplier relationships ensure competitive raw material costs
        <br/>
        The sensitivity analysis shows resilience to price and volume fluctuations, with break-even achievable 
        even in conservative scenarios within reasonable timeframes.
        """
        
        self.add_body_text(breakeven_text)
        self.add_spacer()
    
    def _add_profit_loss_projection(self):
        """Add 5-year P&L projection"""
        self.add_heading1("5-Year Profit & Loss Projection")
        
        # P&L projection table
        pl_data = [
            ['', 'Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5'],
            ['REVENUE', '', '', '', '', ''],
            ['Gross Sales', '$200,000', '$800,000', '$1,750,000', '$2,400,000', '$3,200,000'],
            ['Returns & Allowances', '$10,000', '$24,000', '$52,500', '$72,000', '$96,000'],
            ['Net Revenue', '$190,000', '$776,000', '$1,697,500', '$2,328,000', '$3,104,000'],
            ['', '', '', '', '', ''],
            ['COST OF GOODS SOLD', '', '', '', '', ''],
            ['Raw Materials', '$95,000', '$388,000', '$849,000', '$1,164,000', '$1,552,000'],
            ['Direct Labor', '$38,000', '$93,000', '$170,000', '$210,000', '$248,000'],
            ['Manufacturing Overhead', '$19,000', '$46,000', '$85,000', '$117,000', '$155,000'],
            ['Total COGS', '$152,000', '$527,000', '$1,104,000', '$1,491,000', '$1,955,000'],
            ['', '', '', '', '', ''],
            ['GROSS PROFIT', '$38,000', '$249,000', '$593,500', '$837,000', '$1,149,000'],
            ['Gross Margin %', '20.0%', '32.1%', '35.0%', '36.0%', '37.0%'],
            ['', '', '', '', '', ''],
            ['OPERATING EXPENSES', '', '', '', '', ''],
            ['Sales & Marketing', '$15,000', '$31,000', '$68,000', '$93,000', '$124,000'],
            ['General & Administrative', '$57,000', '$78,000', '$102,000', '$128,000', '$155,000'],
            ['Total Operating Expenses', '$72,000', '$109,000', '$170,000', '$221,000', '$279,000'],
            ['', '', '', '', '', ''],
            ['EBITDA', '($34,000)', '$140,000', '$423,500', '$616,000', '$870,000'],
            ['EBITDA Margin %', '(17.9%)', '18.0%', '24.9%', '26.5%', '28.0%'],
            ['', '', '', '', '', ''],
            ['Depreciation', '$12,000', '$15,000', '$18,000', '$21,000', '$24,000'],
            ['Interest Expense', '$3,000', '$5,000', '$7,000', '$6,000', '$4,000'],
            ['', '', '', '', '', ''],
            ['NET INCOME', '($49,000)', '$120,000', '$398,500', '$589,000', '$842,000'],
            ['Net Margin %', '(25.8%)', '15.5%', '23.5%', '25.3%', '27.1%']
        ]
        
        self.add_table(pl_data, [1.8, 1.0, 1.0, 1.0, 1.0, 1.2], title="5-Year Income Statement Projection")
        
        pl_text = """
        <b>Financial Performance Highlights:</b>
        <br/>
        <b>Revenue Growth:</b> Strong revenue growth driven by production scaling, market penetration, and 
        price optimization. Compound annual growth rate (CAGR) of approximately 95% over 5 years.
        <br/>
        <b>Margin Improvement:</b> Gross margins improve from 20% in Year 1 to 37% in Year 5 due to:
        <br/>
        • Operational efficiency gains and learning curve effects
        <br/>
        • Better raw material procurement and inventory management
        <br/>
        • Product mix optimization toward higher-margin specialty products
        <br/>
        • Fixed cost leverage as production scales
        <br/>
        <b>Profitability Timeline:</b>
        <br/>
        • Year 1: Investment phase with expected losses due to startup costs
        <br/>
        • Year 2: Achievement of positive EBITDA and cash flow breakeven
        <br/>
        • Years 3-5: Strong profitability with margins approaching industry benchmarks
        <br/>
        <b>Return on Investment:</b>
        <br/>
        • 3-Year ROI: Approximately 280% cumulative return
        <br/>
        • 5-Year ROI: Over 500% cumulative return on initial investment
        """
        
        self.add_body_text(pl_text)
        self.add_spacer()
    
    def _add_cash_flow_analysis(self):
        """Add cash flow analysis section"""
        self.add_heading1("Cash Flow Analysis & Working Capital")
        
        # Cash flow projection
        cashflow_data = [
            ['Cash Flow Component', 'Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5'],
            ['NET INCOME', '($49,000)', '$120,000', '$398,500', '$589,000', '$842,000'],
            ['Add: Depreciation', '$12,000', '$15,000', '$18,000', '$21,000', '$24,000'],
            ['Operating Cash Flow', '($37,000)', '$135,000', '$416,500', '$610,000', '$866,000'],
            ['', '', '', '', '', ''],
            ['Working Capital Changes:', '', '', '', '', ''],
            ['Accounts Receivable', '($16,000)', '($47,000)', '($77,000)', '($48,000)', '($62,000)'],
            ['Inventory', '($19,000)', '($39,000)', '($64,000)', '($41,000)', '($52,000)'],
            ['Accounts Payable', '$13,000', '$26,000', '$43,000', '$28,000', '$35,000'],
            ['Net Working Capital Change', '($22,000)', '($60,000)', '($98,000)', '($61,000)', '($79,000)'],
            ['', '', '', '', '', ''],
            ['Free Cash Flow', '($59,000)', '$75,000', '$318,500', '$549,000', '$787,000'],
            ['', '', '', '', '', ''],
            ['Capital Expenditures', '($120,000)', '($45,000)', '($35,000)', '($25,000)', '($30,000)'],
            ['', '', '', '', '', ''],
            ['Net Cash Flow', '($179,000)', '$30,000', '$283,500', '$524,000', '$757,000'],
            ['Cumulative Cash Flow', '($179,000)', '($149,000)', '$134,500', '$658,500', '$1,415,500']
        ]
        
        self.add_table(cashflow_data, [1.8, 1.0, 1.0, 1.0, 1.0, 1.2], title="5-Year Cash Flow Projection")
        
        # Working capital analysis
        wc_data = [
            ['Working Capital Component', 'Days', 'Year 2', 'Year 3', 'Year 5', 'Industry Std'],
            ['Accounts Receivable', '30 days', '$65,000', '$142,000', '$259,000', '30-45 days'],
            ['Inventory (Raw Materials)', '45 days', '$48,000', '$101,000', '$179,000', '30-60 days'],
            ['Inventory (Finished Goods)', '15 days', '$22,000', '$46,000', '$82,000', '10-20 days'],
            ['Accounts Payable', '30 days', '$44,000', '$92,000', '$163,000', '30-45 days'],
            ['Net Working Capital', '', '$91,000', '$197,000', '$357,000', '15-25% of revenue'],
            ['As % of Revenue', '', '11.7%', '11.6%', '11.5%', 'Target: <15%']
        ]
        
        self.add_table(wc_data, [1.8, 1.0, 1.0, 1.0, 1.0, 1.2], title="Working Capital Management")
        
        cashflow_text = """
        <b>Cash Flow Management Strategy:</b>
        <br/>
        <b>Operating Cash Flow:</b> Strong operating cash flow generation begins in Year 2, providing 
        self-funding capability for growth and expansion investments.
        <br/>
        <b>Working Capital Optimization:</b>
        <br/>
        • Accounts Receivable: 30-day payment terms with early payment discounts
        <br/>
        • Inventory Management: Just-in-time delivery balanced with safety stock requirements
        <br/>
        • Supplier Relations: Negotiate favorable payment terms while maintaining good relationships
        <br/>
        <b>Capital Allocation:</b>
        <br/>
        • Reinvestment in capacity expansion and efficiency improvements
        <br/>
        • Debt service and interest payments
        <br/>
        • Dividend policy consideration beginning Year 3
        <br/>
        • Strategic reserves for market opportunities
        <br/>
        <b>Financing Requirements:</b>
        <br/>
        • Initial capital investment: $120,000 in Year 1
        <br/>
        • Working capital line of credit: $50,000-$100,000 facility
        <br/>
        • Equipment financing for major purchases
        <br/>
        • Potential equity raises for significant expansion opportunities
        """
        
        self.add_body_text(cashflow_text)
        self.add_spacer()
    
    def _add_funding_requirements(self):
        """Add funding requirements section"""
        self.add_heading1("Funding Requirements & Sources")
        
        # Get funding programs
        funding_programs = self.db.get_funding_programs()
        
        if funding_programs:
            funding_data = [['Program Name', 'Type', 'Max Coverage', 'Max Amount', 'Status']]
            
            for program in funding_programs:
                funding_data.append([
                    program.get('program_name', 'N/A'),
                    program.get('funding_type', 'N/A'),
                    f"{program.get('max_coverage_percent', 0)}%" if program.get('max_coverage_percent') else 'N/A',
                    self.format_currency(program.get('max_amount_cad')),
                    program.get('application_status', 'N/A')
                ])
            
            self.add_table(funding_data, [2.2, 1.2, 1.0, 1.3, 1.3], title="Government Funding Opportunities")
        
        # Funding sources breakdown
        sources_data = [
            ['Funding Source', 'Amount Range', 'Terms', 'Timeline', 'Probability'],
            ['Founder Investment', '$50,000-$75,000', 'Equity', 'Immediate', 'Confirmed'],
            ['Angel Investors', '$75,000-$125,000', 'Equity/Convertible', '3-6 months', 'High'],
            ['Government Grants', '$25,000-$100,000', 'Grant/Loan', '6-12 months', 'Medium'],
            ['Equipment Financing', '$40,000-$80,000', 'Secured loan', '1-3 months', 'High'],
            ['Working Capital LOC', '$50,000-$100,000', 'Revolving credit', '2-4 months', 'High'],
            ['Strategic Partners', '$100,000-$200,000', 'Equity/Revenue share', '6-18 months', 'Medium']
        ]
        
        self.add_table(sources_data, [1.5, 1.2, 1.2, 1.2, 1.1], title="Funding Sources Analysis")
        
        funding_text = """
        <b>Total Funding Requirement: CAD $200,000-$300,000</b>
        <br/>
        <b>Use of Funds:</b>
        <br/>
        • Equipment and Machinery: 60% ($120,000-$180,000)
        <br/>
        • Facility Setup and Infrastructure: 20% ($40,000-$60,000)
        <br/>
        • Working Capital and Inventory: 15% ($30,000-$45,000)
        <br/>
        • Marketing and Business Development: 5% ($10,000-$15,000)
        <br/>
        <b>Funding Strategy:</b>
        Phase 1 funding focuses on essential startup capital with a mix of founder investment, angel funding, 
        and equipment financing. Government grants provide valuable non-dilutive funding for specific initiatives.
        <br/>
        <b>Future Funding Needs:</b>
        <br/>
        • Year 2-3: $300,000-$500,000 for scale-up phase
        <br/>
        • Year 4-5: Potential debt financing for major expansion
        <br/>
        • Self-funding capability expected by Year 3
        <br/>
        <b>Investor Returns:</b>
        <br/>
        • Target IRR: 25-35% for equity investors
        <br/>
        • Exit opportunities: Strategic acquisition, management buyout, or dividend recapitalization
        <br/>
        • Strong cash flow provides flexibility for investor returns
        """
        
        self.add_body_text(funding_text)
        self.add_spacer()
    
    def _add_financial_assumptions(self):
        """Add financial assumptions section"""
        self.add_heading1("Key Financial Assumptions & Sensitivities")
        
        # Key assumptions table
        assumptions_data = [
            ['Assumption Category', 'Base Case', 'Conservative', 'Optimistic', 'Source/Rationale'],
            ['Annual Revenue Growth', '95% CAGR', '75% CAGR', '120% CAGR', 'Market research, customer feedback'],
            ['Gross Margin (Mature)', '35-37%', '30-32%', '40-42%', 'Industry benchmarks, cost analysis'],
            ['Working Capital % Revenue', '12-15%', '18-20%', '8-10%', 'Industry standards, payment terms'],
            ['EBITDA Margin (Year 5)', '28%', '22%', '33%', 'Operational efficiency targets'],
            ['Raw Material Inflation', '2-3% annually', '5% annually', '1% annually', 'Supplier forecasts, contracts'],
            ['Customer Payment Terms', '30 days', '45 days', '20 days', 'Industry practice, negotiation'],
            ['Capacity Utilization', '75% average', '65% average', '85% average', 'Production planning, demand'],
            ['Equipment Utilization', '16 hrs/day', '12 hrs/day', '20 hrs/day', 'Operational planning']
        ]
        
        self.add_table(assumptions_data, [1.5, 1.1, 1.1, 1.1, 2.2], title="Financial Modeling Assumptions")
        
        assumptions_text = """
        <b>Sensitivity Analysis Summary:</b>
        <br/>
        The financial model is most sensitive to:
        <br/>
        1. <b>Sales Volume:</b> 10% change in volume impacts EBITDA by approximately 15-20%
        <br/>
        2. <b>Average Selling Price:</b> 5% price change impacts margins by 8-12%
        <br/>
        3. <b>Raw Material Costs:</b> 10% cost increase reduces gross margin by 5-7%
        <br/>
        4. <b>Production Efficiency:</b> Capacity utilization directly impacts fixed cost absorption
        <br/>
        <b>Risk Mitigation Factors:</b>
        <br/>
        • Flexible cost structure allows rapid adjustment to market changes
        <br/>
        • Multiple revenue streams reduce customer concentration risk
        <br/>
        • Long-term supplier relationships provide cost stability
        <br/>
        • Conservative growth assumptions provide buffer for market challenges
        <br/>
        <b>Model Validation:</b>
        <br/>
        Financial projections validated through:
        <br/>
        • Industry benchmark analysis and peer comparison
        <br/>
        • Customer feedback and market research
        <br/>
        • Supplier quotes and cost verification
        <br/>
        • Operational pilot testing and efficiency studies
        <br/>
        <b>Monitoring & Updates:</b>
        Financial model will be updated quarterly with actual results and revised assumptions. 
        Key performance indicators will be tracked monthly to ensure performance vs. plan.
        """
        
        self.add_body_text(assumptions_text)
        self.add_spacer()
    
    def generate(self) -> Path:
        """Generate the Financial Projections PDF"""
        self.story = []  # Reset story
        self.build_content()
        
        filename = f"fluxgen_financial_projections_{self._get_timestamp()}"
        return self.generate_document(filename, "FluxGen Industries - Financial Projections")
    
    def _get_timestamp(self) -> str:
        """Get timestamp for filename"""
        from datetime import datetime
        return datetime.now().strftime('%Y%m%d_%H%M%S')