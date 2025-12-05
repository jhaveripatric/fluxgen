"""
Team Biographies document generator for FluxGen
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.base import BaseDocumentGenerator
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class TeamBiosGenerator(BaseDocumentGenerator):
    """Generates Team Biographies document (2-3 pages)"""
    
    def __init__(self, database_manager, output_dir: Path):
        super().__init__(database_manager, output_dir)
    
    def build_content(self):
        """Build team biographies content"""
        # Document title and company header
        self.add_company_header()
        self.add_title("Management Team & Key Personnel")
        
        # Team Overview
        self._add_team_overview()
        
        # Individual Biographies
        self._add_individual_bios()
        
        # Organizational Structure
        self._add_organizational_structure()
        self.add_page_break()
        
        # Advisory Board
        self._add_advisory_board()
        
        # Hiring Plan
        self._add_hiring_plan()
        
        # Footer
        self.add_footer_info()
    
    def _add_team_overview(self):
        """Add team overview section"""
        self.add_heading1("Executive Team Overview")
        
        # Get team member data
        team_members = self.db.get_team_members()
        
        # Break into smaller sections to prevent overflow
        intro_text = """
        FluxGen Industries is led by a highly experienced founding team with complementary expertise in 
        manufacturing operations, business development, supply chain management, and quality control. 
        The team combines decades of collective experience in welding consumables manufacturing and industrial operations.
        """
        
        philosophy_text = """
        <b>Leadership Philosophy:</b>
        <br/>
        • Customer-focused approach with emphasis on quality and service
        <br/>
        • Operational excellence and continuous improvement mindset
        <br/>
        • Collaborative leadership style promoting team development
        <br/>
        • Strategic thinking balanced with hands-on execution
        <br/>
        • Commitment to safety, environmental responsibility, and community engagement
        """
        
        strengths_text = """
        <b>Team Strengths:</b>
        <br/>
        • Proven track record in scaling manufacturing operations globally
        <br/>
        • Deep understanding of welding industry and customer needs
        <br/>
        • Strong relationships with suppliers, customers, and industry partners
        <br/>
        • Technical knowledge of SAW flux formulation and manufacturing processes
        <br/>
        • Operational excellence in logistics, quality control, and compliance
        """
        
        self.add_body_text(intro_text)
        self.add_body_text(philosophy_text)
        self.add_body_text(strengths_text)
        
        if team_members:
            # Team summary table
            team_summary_data = [['Name', 'Position', 'Background', 'Current Role']]
            
            for member in team_members:
                current_pos = member.get('current_position', 'N/A')
                background_short = member.get('background', 'N/A')
                
                team_summary_data.append([
                    member.get('name', 'N/A'),
                    member.get('role', 'N/A'),
                    background_short,
                    current_pos
                ])
            
            self.add_table(team_summary_data, [1.3, 1.8, 2.5, 1.4], title="Management Team Summary")
        
        self.add_spacer()
    
    def _add_individual_bios(self):
        """Add detailed individual biographies"""
        self.add_heading1("Individual Biographies")
        
        team_members = self.db.get_team_members()
        
        if team_members:
            for member in team_members:
                name = member.get('name', 'Unknown')
                role = member.get('role', 'Team Member')
                email = member.get('email', '')
                phone = member.get('phone', '')
                background = member.get('background', '')
                expertise_raw = member.get('expertise', '')
                current_position = member.get('current_position', '')
                value = member.get('value_to_fluxgen', '')
                
                self.add_heading2(f"{name} — {role}")
                
                # Contact information
                contact_info = []
                if email:
                    contact_info.append(f"Email: {email}")
                if phone:
                    contact_info.append(f"Phone: {phone}")
                
                if contact_info:
                    contact_text = " | ".join(contact_info)
                    self.add_body_text(f"<b>Contact:</b> {contact_text}")
                
                # Background section
                if background:
                    bio_text = f"""<b>Background:</b>
                    <br/>
                    {background}
                    <br/>"""
                    self.add_body_text(bio_text)
                
                # Expertise section (convert pipe-separated to bullet list)
                if expertise_raw:
                    expertise_list = expertise_raw.split('|')
                    expertise_text = "<b>Expertise:</b><br/>"
                    for exp in expertise_list:
                        expertise_text += f"• {exp.strip()}<br/>"
                    self.add_body_text(expertise_text)
                
                # Current Role section
                if current_position:
                    current_text = f"""<b>Current Role:</b>
                    <br/>
                    {current_position}
                    <br/>"""
                    self.add_body_text(current_text)
                
                # Value to FluxGen section
                if value:
                    value_text = f"""<b>Value to FluxGen:</b>
                    <br/>
                    {value}
                    <br/>"""
                    self.add_body_text(value_text)
                
                self.add_spacer(0.3)
        
        else:
            placeholder_text = """
            <b>Team biographies will be completed upon final team confirmation.</b>
            <br/>
            The FluxGen management team is being assembled with individuals who bring the necessary 
            expertise and experience to successfully launch and operate the manufacturing facility. 
            Detailed biographies will be provided as team members are confirmed and onboarded.
            """
            self.add_body_text(placeholder_text)
    
    def _add_organizational_structure(self):
        """Add organizational structure section"""
        self.add_heading1("Organizational Structure & Reporting")
        
        # Organizational chart data
        org_data = [
            ['Position', 'Reports To', 'Direct Reports', 'Key Responsibilities'],
            ['Founder & Technical Director', 'Board of Directors', 'All Managers', 'Technical strategy, formulations, R&D, quality standards'],
            ['Operations & Logistics Manager', 'Founder', 'Production, warehouse staff', 'Daily operations, supply chain, inventory, vendor management'],
            ['Sales & Marketing Lead', 'Founder', 'Sales team', 'Customer acquisition, account management, brand development'],
            ['Quality Assurance & Compliance Manager', 'Founder', 'QC technicians', 'Quality control, certifications, process documentation, compliance'],
            ['Production Manager', 'Operations Manager', 'Operators, maintenance', 'Daily production, scheduling, equipment maintenance'],
            ['Warehouse Supervisor', 'Operations Manager', 'Warehouse staff', 'Inventory, shipping, receiving, logistics coordination']
        ]
        
        self.add_table(org_data, [1.8, 1.2, 1.2, 2.8], title="Organizational Reporting Structure")
        
        governance_text = """
        <b>Corporate Governance:</b>
        FluxGen Industries will establish a Board of Directors with independent oversight and industry expertise.
        The board will provide strategic guidance, risk oversight, and performance monitoring.
        """

        management_philosophy_text = """
        <b>Management Philosophy:</b>
        <br/>
        • Flat organizational structure promoting communication and agility
        <br/>
        • Clear accountability and decision-making authority
        <br/>
        • Cross-functional collaboration and teamwork
        <br/>
        • Performance-based culture with measurable objectives
        <br/>
        • Open communication and continuous feedback
        """

        decision_making_text = """
        <b>Decision-Making Process:</b>
        <br/>
        • Daily operations managed by department managers
        <br/>
        • Weekly management team meetings for coordination
        <br/>
        • Monthly board meetings for strategic oversight
        <br/>
        • Quarterly business reviews with stakeholders
        <br/>
        • Annual strategic planning and budget cycles
        """

        performance_mgmt_text = """
        <b>Performance Management:</b>
        <br/>
        • Clear job descriptions and performance expectations
        <br/>
        • Regular performance reviews and development planning
        <br/>
        • Compensation aligned with company and individual performance
        <br/>
        • Professional development and training opportunities
        <br/>
        • Recognition and advancement programs
        """

        self.add_body_text(governance_text)
        self.add_body_text(management_philosophy_text)
        self.add_body_text(decision_making_text)
        self.add_body_text(performance_mgmt_text)
        self.add_spacer()
    
    def _add_advisory_board(self):
        """Add advisory board section"""
        self.add_heading1("Advisory Board & Industry Experts")
        
        advisory_intro_text = """
        FluxGen Industries is establishing an Advisory Board comprising industry experts, successful entrepreneurs,
        and technical specialists to provide strategic guidance and market insights.

        <b>Advisory Board Structure:</b>
        """

        industry_expert_text = """
        <b>Industry Expert - Welding Technology:</b>
        <br/>
        • Background: 25+ years in welding consumables industry
        <br/>
        • Expertise: Product development, technical standards, customer applications
        <br/>
        • Value: Market insights, product strategy, technical validation
        """

        business_advisor_text = """
        <b>Business Advisor - Manufacturing:</b>
        <br/>
        • Background: Former manufacturing executive with scaling experience
        <br/>
        • Expertise: Operations optimization, lean manufacturing, quality systems
        <br/>
        • Value: Operational strategy, process improvement, cost optimization
        """

        financial_advisor_text = """
        <b>Financial Advisor - Industrial Investments:</b>
        <br/>
        • Background: Investment banking and industrial finance experience
        <br/>
        • Expertise: Capital markets, mergers & acquisitions, financial strategy
        <br/>
        • Value: Financial planning, funding strategy, exit planning
        """

        govt_advisor_text = """
        <b>Government Relations Advisor:</b>
        <br/>
        • Background: Former government official with economic development experience
        <br/>
        • Expertise: Regulatory affairs, government programs, public-private partnerships
        <br/>
        • Value: Regulatory guidance, funding programs, government relations
        """

        customer_panel_text = """
        <b>Customer Advisory Panel:</b>
        <br/>
        FluxGen will also establish a Customer Advisory Panel with representatives from key customer segments:
        <br/>
        • Major fabrication companies
        <br/>
        • Pipeline construction contractors
        <br/>
        • Equipment manufacturers
        <br/>
        • Government and municipal users

        <br/>
        This panel will provide ongoing feedback on product development, market trends, and service requirements.
        """

        self.add_body_text(advisory_intro_text)
        self.add_body_text(industry_expert_text)
        self.add_body_text(business_advisor_text)
        self.add_body_text(financial_advisor_text)
        self.add_body_text(govt_advisor_text)
        self.add_body_text(customer_panel_text)
        
        # Advisory meeting schedule
        advisory_schedule_data = [
            ['Advisory Function', 'Meeting Frequency', 'Key Topics', 'Expected Outcomes'],
            ['Board of Directors', 'Monthly', 'Strategy, performance, major decisions', 'Governance oversight, strategic guidance'],
            ['Industry Advisory Board', 'Quarterly', 'Market trends, product development', 'Market insights, technical direction'],
            ['Customer Advisory Panel', 'Semi-annually', 'Product feedback, service needs', 'Product roadmap, service improvement'],
            ['Financial Advisors', 'As needed', 'Funding, financial strategy, exit planning', 'Financial optimization, growth strategy'],
            ['Technical Consultants', 'As needed', 'Process optimization, troubleshooting', 'Technical problem solving, innovation']
        ]
        
        self.add_table(advisory_schedule_data, [1.4, 1.1, 1.8, 1.7], title="Advisory Structure & Engagement")
        
        self.add_spacer()
    
    def _add_hiring_plan(self):
        """Add hiring plan section"""
        self.add_heading1("Staffing Plan & Human Resources Strategy")
        
        # Hiring timeline
        hiring_data = [
            ['Position', 'Phase 1 (Months 1-6)', 'Phase 2 (Months 7-18)', 'Phase 3 (Months 19+)', 'Key Qualifications'],
            ['Founding Team', '4 founders', 'Same', 'Same', 'Industry experience, leadership'],
            ['Production Staff', '3-4 operators', '6-8 operators', '10-12 operators', 'Manufacturing experience, safety'],
            ['Quality Control', '1 technician', '2 technicians', '3 technicians', 'Lab experience, certifications'],
            ['Maintenance', '1 mechanic', '2 mechanics', '3 mechanics', 'Equipment maintenance, troubleshooting'],
            ['Administration', '1-2 staff', '2-3 staff', '3-4 staff', 'Accounting, HR, customer service'],
            ['Sales Representatives', '1 rep', '2 reps', '3-4 reps', 'Industry relationships, technical sales'],
            ['Total FTE', '10-12', '15-18', '23-27', '']
        ]
        
        self.add_table(hiring_data, [1.2, 1.1, 1.3, 1.0, 1.4], title="Staffing Plan by Phase")
        
        recruitment_text = """
        <b>Recruitment Strategy:</b>
        <br/>
        • Target experienced professionals from oil & gas, manufacturing, and welding industries
        <br/>
        • Partner with local technical colleges and trade schools for skilled trades
        <br/>
        • Competitive compensation packages with performance incentives
        <br/>
        • Comprehensive benefits including health, dental, retirement, and professional development
        <br/>
        • Employee stock option plan for key contributors
        """

        training_text = """
        <b>Training & Development:</b>
        <br/>
        • Comprehensive orientation program for safety and quality procedures
        <br/>
        • Technical training on equipment operation and maintenance
        <br/>
        • Cross-training to develop versatile workforce
        <br/>
        • Professional development and certification support
        <br/>
        • Leadership development for high-potential employees
        """

        culture_text = """
        <b>Workplace Culture:</b>
        <br/>
        • Safety-first culture with zero-incident goal
        <br/>
        • Team-oriented environment promoting collaboration
        <br/>
        • Open communication and employee feedback
        <br/>
        • Recognition and reward programs
        <br/>
        • Work-life balance and flexible scheduling where possible
        """

        compensation_text = """
        <b>Compensation Philosophy:</b>
        <br/>
        • Market competitive base salaries
        <br/>
        • Performance-based bonuses and incentives
        <br/>
        • Comprehensive benefits package
        <br/>
        • Equity participation for key employees
        <br/>
        • Professional development investment
        """

        employee_relations_text = """
        <b>Employee Relations:</b>
        <br/>
        • Regular employee surveys and feedback sessions
        <br/>
        • Fair and consistent HR policies and procedures
        <br/>
        • Conflict resolution and grievance procedures
        <br/>
        • Wellness programs and employee assistance
        <br/>
        • Community involvement and volunteer opportunities
        """

        skills_dev_text = """
        <b>Skills Development:</b>
        <br/>
        FluxGen is committed to developing local talent through:
        <br/>
        • Apprenticeship programs with local trade schools
        <br/>
        • Technical certification support and reimbursement
        <br/>
        • Cross-functional training and career advancement
        <br/>
        • Industry conference and training attendance
        <br/>
        • Mentorship programs pairing senior and junior staff
        """

        self.add_body_text(recruitment_text)
        self.add_body_text(training_text)
        self.add_body_text(culture_text)
        self.add_body_text(compensation_text)
        self.add_body_text(employee_relations_text)
        self.add_body_text(skills_dev_text)
        self.add_spacer()
    
    def generate(self) -> Path:
        """Generate the Team Biographies PDF"""
        self.story = []  # Reset story
        self.build_content()
        
        filename = f"fluxgen_team_biographies_{self._get_timestamp()}"
        return self.generate_document(filename, "FluxGen Industries - Team Biographies")
    
    def _get_timestamp(self) -> str:
        """Get timestamp for filename"""
        from datetime import datetime
        return datetime.now().strftime('%Y%m%d_%H%M%S')
