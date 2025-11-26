"""
Individual Prep Documents generator for FluxGen Team Members
Generates personalized prep documents for investor/partner meetings
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.base import BaseDocumentGenerator
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class IndividualPrepGenerator(BaseDocumentGenerator):
    """Generates Individual Prep Documents for team members (1-2 pages each)"""
    
    def __init__(self, database_manager, output_dir: Path):
        super().__init__(database_manager, output_dir)
        self.current_member = None
    
    def build_content_for_member(self, member):
        """Build prep content for a specific team member"""
        self.current_member = member
        
        # Document header
        self.add_company_header()
        
        name = member.get('name', 'Team Member')
        role = member.get('role', 'Role')
        
        self.add_title(f"Meeting Prep Document")
        self.add_body_text(f"<b>FOR: {name} — {role}</b><br/><b>CONFIDENTIAL - INTERNAL USE ONLY</b>")
        self.add_spacer(0.3)
        
        # Add all sections
        self._add_your_role_section()
        self._add_why_you_section()
        self._add_questions_section()
        self._add_talking_points_section()
        self._add_dos_and_donts_section()
        
        # Footer
        self.add_footer_info()
    
    def _add_your_role_section(self):
        """Add 'Your Role in FluxGen' section"""
        member = self.current_member
        role = member.get('role', 'Team Member')
        value = member.get('value_to_fluxgen', '')
        
        self.add_heading1("Your Role in FluxGen")
        
        role_text = f"""
        <b>Official Title:</b> {role}
        <br/>
        
        <b>Why This Role Matters:</b>
        <br/>
        {value if value else 'You are a critical member of the FluxGen founding team.'}
        <br/>
        
        <b>What Investors Need to See:</b>
        <br/>
        Investors want to see that each team member brings unique, essential skills. Your job in the meeting 
        is to demonstrate deep expertise in your domain and show that you're not just competent — you're the 
        right person for this specific role in this specific industry.
        <br/>
        
        <b>Your Positioning:</b>
        <br/>
        You are not "helping out" or "learning the business" — you are a co-founder with specialized expertise 
        that FluxGen cannot succeed without. Own your area of responsibility with confidence.
        """
        
        self.add_body_text(role_text)
        self.add_spacer()
    
    def _add_why_you_section(self):
        """Add 'Why You're on This Team' section"""
        member = self.current_member
        name = member.get('name', 'Team Member')
        background = member.get('background', '')
        expertise_raw = member.get('expertise', '')
        current_position = member.get('current_position', '')
        
        self.add_heading1("Why You're on This Team")
        
        # Parse expertise
        expertise_list = expertise_raw.split('|') if expertise_raw else []
        
        why_text = f"""
        <b>Your Background (What Investors Will Hear):</b>
        <br/>
        {background if background else 'Industry professional with relevant experience.'}
        <br/>
        
        <b>Your Core Competencies:</b>
        <br/>"""
        
        for exp in expertise_list:
            why_text += f"• {exp.strip()}<br/>"
        
        why_text += f"""
        <br/>
        <b>Current Professional Role:</b>
        <br/>
        {current_position if current_position else 'N/A'}
        <br/>
        
        <b>Key Message for Investors:</b>
        <br/>
        You bring proven, real-world experience that directly translates to FluxGen's success. You're not 
        learning on the job — you're applying mastery from previous successes to build something new.
        """
        
        self.add_body_text(why_text)
        self.add_spacer()
    
    def _add_questions_section(self):
        """Add anticipated questions section"""
        member = self.current_member
        role = member.get('role', 'Team Member')
        name = member.get('name', 'Team Member').split()[0]
        
        self.add_heading1("What Investors Will Ask You")
        
        # Role-specific questions
        questions_map = self._get_role_specific_questions(role, name)
        
        self.add_body_text(questions_map['intro'])
        
        for qa in questions_map['questions']:
            q_text = f"""<b>Q: {qa['question']}</b>
            <br/>
            <b>A:</b> {qa['answer']}
            <br/>"""
            self.add_body_text(q_text)
        
        self.add_spacer()
    
    def _add_talking_points_section(self):
        """Add key talking points section"""
        member = self.current_member
        role = member.get('role', 'Team Member')
        
        self.add_heading1("Your Key Talking Points")
        
        talking_points = self._get_role_talking_points(role)
        
        points_text = f"""
        <b>When discussing FluxGen, always emphasize:</b>
        <br/>
        
        <b>General (All Team Members):</b>
        <br/>
        • FluxGen is Canada's first SAW flux manufacturing company
        <br/>
        • We're not importing — we're localizing production to reduce supply chain risk
        <br/>
        • Our team has direct, hands-on experience running similar operations at scale
        <br/>
        • We're starting pilot, scaling smart, and targeting profitability early
        <br/>
        
        <b>Specific to Your Role:</b>
        <br/>"""
        
        for point in talking_points:
            points_text += f"• {point}<br/>"
        
        self.add_body_text(points_text)
        self.add_spacer()
    
    def _add_dos_and_donts_section(self):
        """Add do's and don'ts section"""
        member = self.current_member
        role = member.get('role', 'Team Member')
        
        self.add_heading1("Do's and Don'ts")
        
        dos_donts = self._get_role_dos_donts(role)
        
        dos_donts_text = f"""
        <b>✅ DO:</b>
        <br/>"""
        
        for do in dos_donts['dos']:
            dos_donts_text += f"• {do}<br/>"
        
        dos_donts_text += """
        <br/>
        <b>❌ DON'T:</b>
        <br/>"""
        
        for dont in dos_donts['donts']:
            dos_donts_text += f"• {dont}<br/>"
        
        dos_donts_text += """
        <br/>
        <b>General Meeting Etiquette:</b>
        <br/>
        • Dress professionally (business casual minimum, business formal for major investors)
        <br/>
        • Arrive 10-15 minutes early to review notes
        <br/>
        • Turn off phone notifications completely
        <br/>
        • Listen actively — don't interrupt other team members
        <br/>
        • If you don't know an answer, say "That's not my area, but [Team Member] can address that"
        <br/>
        • Never contradict another team member in front of investors — discuss internally later
        <br/>
        • Take notes if investors ask follow-up questions — shows you're listening
        <br/>
        
        <b>Remember:</b>
        <br/>
        Investors are looking for three things: <b>Competence</b>, <b>Cohesion</b>, and <b>Commitment</b>. 
        Show you know your stuff, that you work well together, and that you're all-in on FluxGen's success.
        """
        
        self.add_body_text(dos_donts_text)
        self.add_spacer()
    
    def _get_role_specific_questions(self, role, name):
        """Get role-specific Q&A based on team member role"""
        
        questions_db = {
            'Founder & Technical Director': {
                'intro': f"""
                As the <b>Technical Director</b>, investors will probe your formulation expertise, 
                manufacturing knowledge, and ability to ensure consistent product quality. They want to 
                know you've actually done this before — not just read about it.
                <br/>""",
                'questions': [
                    {
                        'question': 'Tell me about your experience with Jhaveri Weld Flux. What scale were you operating at?',
                        'answer': f'{name} should mention it was publicly listed on Mumbai and Ahmedabad exchanges, became one of India\'s largest SAW flux manufacturers, and produced both agglomerated flux and flux-cored wire at industrial scale. Emphasize this was a full-scale commercial operation, not a startup or pilot.'
                    },
                    {
                        'question': 'What makes you confident you can replicate that success in Canada?',
                        'answer': 'The fundamentals of flux formulation and agglomeration are the same. The difference is market positioning — Canada has strong demand but limited local supply. We\'re not inventing a new product; we\'re localizing proven manufacturing for an underserved market.'
                    },
                    {
                        'question': 'What are the biggest technical risks in SAW flux manufacturing?',
                        'answer': 'Consistency in particle size distribution, moisture control during storage, and maintaining precise chemical composition across batches. We mitigate this through rigorous QC protocols, climate-controlled storage, and batch tracking systems.'
                    },
                    {
                        'question': 'Why aren\'t you working in the welding industry full-time right now?',
                        'answer': 'After successfully building Jhaveri Weld Flux, I transitioned into software engineering at Aylo, which gave me exposure to modern operational systems and data-driven manufacturing approaches. Now I\'m bringing both skill sets together to build FluxGen with better technology and processes than traditional flux manufacturers.'
                    },
                    {
                        'question': 'How involved will you be day-to-day?',
                        'answer': 'Initially, very involved — overseeing formulation, QC setup, and production commissioning. As we scale and hire technical staff, I\'ll transition to strategic oversight, R&D, and customer technical support. The goal is to build systems that don\'t depend on me for daily operations.'
                    }
                ]
            },
            
            'Operations & Logistics Manager': {
                'intro': f"""
                As the <b>Operations & Logistics Manager</b>, investors will focus on your ability to run 
                the plant smoothly, manage supply chains, and handle labour effectively. They want to see 
                you're a hands-on operator, not just a manager.
                <br/>""",
                'questions': [
                    {
                        'question': 'What was your role at Loblaws, and how does it translate to FluxGen?',
                        'answer': 'I managed warehouse operations and inventory systems in a high-volume, fast-paced distribution environment. That experience taught me how to coordinate complex logistics, manage labour teams, and maintain inventory accuracy under pressure — all critical for manufacturing operations.'
                    },
                    {
                        'question': 'Have you ever worked in manufacturing before?',
                        'answer': 'While my background is in logistics and warehouse operations, the skills are highly transferable. Managing material flow, coordinating vendors, optimizing inventory, and leading teams are universal operational competencies. Plus, I have strong contacts in Alberta\'s industrial sector from my time at Loblaws.'
                    },
                    {
                        'question': 'How will you handle raw material sourcing?',
                        'answer': 'We\'re sourcing Canadian suppliers wherever possible — silica, dolomite, and calcite are all available domestically. I\'ve already begun vetting suppliers in Alberta and BC. Our strategy is to establish long-term relationships with 2-3 primary suppliers per material and maintain safety stock to avoid disruptions.'
                    },
                    {
                        'question': 'What if a key supplier has issues or raises prices unexpectedly?',
                        'answer': 'That\'s why we\'re building redundancy into the supply chain from day one — multiple qualified suppliers, safety stock buffers, and long-term contracts with price protection clauses. In a worst-case scenario, we can source materials from the US, though it increases costs slightly.'
                    },
                    {
                        'question': 'How will you manage labour in a small manufacturing facility?',
                        'answer': 'Small teams require strong interpersonal skills and proactive communication — which is my strength. I\'ll focus on hiring the right people, creating a positive work culture, and addressing issues before they escalate. My experience at Loblaws taught me how to keep teams motivated and productive.'
                    }
                ]
            },
            
            'Sales & Marketing Lead': {
                'intro': f"""
                As the <b>Sales & Marketing Lead</b>, investors will evaluate your ability to acquire 
                customers, build the brand, and communicate FluxGen's value. They want to see energy, 
                confidence, and a clear go-to-market plan.
                <br/>""",
                'questions': [
                    {
                        'question': 'Who are your target customers, and why will they buy from FluxGen?',
                        'answer': 'Our primary targets are fabrication shops, pipeline contractors, and heavy manufacturing companies in Alberta and Saskatchewan. They\'ll buy from us because we offer local supply, faster delivery, technical support, and competitive pricing compared to imported alternatives.'
                    },
                    {
                        'question': 'What\'s your sales strategy for the first year?',
                        'answer': 'Direct B2B outreach to 20-30 key accounts, attending industry trade shows like FABTECH and CWB events, and leveraging our team\'s existing industry contacts. We\'ll start with pilot orders and sample testing to build credibility, then scale to recurring orders once customers validate quality.'
                    },
                    {
                        'question': 'How do you compete with established suppliers?',
                        'answer': 'We don\'t compete on brand recognition — we compete on proximity, service, and flexibility. Established suppliers are overseas or Eastern Canada. We offer same-week delivery, custom formulations, and technical support. For price-sensitive customers, we match or beat import pricing because we eliminate long shipping costs.'
                    },
                    {
                        'question': 'What if customers are hesitant to switch suppliers?',
                        'answer': 'That\'s expected. We overcome it by offering free sample testing, trial orders at discounted rates, and technical consultations to demonstrate our product quality meets or exceeds their current supplier. Once they see the performance and service, switching becomes a no-brainer.'
                    },
                    {
                        'question': 'How will you build the FluxGen brand?',
                        'answer': 'Through a combination of digital presence (website, LinkedIn), trade show participation, and word-of-mouth referrals from satisfied customers. We\'re positioning FluxGen as "Canada\'s Local Flux Solution" — emphasizing quality, reliability, and local supply chain advantages.'
                    }
                ]
            },
            
            'Quality Assurance & Compliance Manager': {
                'intro': f"""
                As the <b>Quality Assurance & Compliance Manager</b>, investors will focus on your ability 
                to ensure product consistency, manage certifications, and maintain compliance. They want to 
                see meticulous attention to detail and process discipline.
                <br/>""",
                'questions': [
                    {
                        'question': 'What quality certifications will FluxGen pursue, and why?',
                        'answer': 'We\'ll prioritize AWS (American Welding Society) certifications for our flux products, CWB (Canadian Welding Bureau) compliance, and eventually ISO 9001 for our quality management system. These certifications are non-negotiable for selling to major industrial customers.'
                    },
                    {
                        'question': 'How will you ensure batch-to-batch consistency?',
                        'answer': 'Through rigorous incoming material inspection, in-process monitoring, and final product testing. Every batch will have documented test results for chemical composition, particle size distribution, and moisture content. We\'ll use statistical process control to identify deviations before they become issues.'
                    },
                    {
                        'question': 'What happens if a batch fails quality tests?',
                        'answer': 'Failed batches will be quarantined immediately, root cause analyzed, and either reworked or scrapped depending on the defect. We\'ll maintain a non-conformance log and implement corrective actions to prevent recurrence. Customer shipments will never include non-conforming material.'
                    },
                    {
                        'question': 'How do you handle customer complaints about product performance?',
                        'answer': 'We\'ll establish a formal complaint handling process: immediate acknowledgment, investigation with batch traceability, root cause analysis, and corrective action. If the issue is on our end, we replace the material at no cost and implement process improvements. Transparency and accountability are key.'
                    },
                    {
                        'question': 'What\'s your experience with manufacturing quality systems?',
                        'answer': 'While my background is in IT, my attention to detail, process discipline, and systematic approach make me well-suited for quality management. I thrive in structured environments where precision matters — and I\'ll be working closely with Pratik, who has deep QC experience from Jhaveri Weld Flux.'
                    }
                ]
            }
        }
        
        return questions_db.get(role, {
            'intro': 'Prepare to answer questions about your role and responsibilities at FluxGen.<br/>',
            'questions': [
                {
                    'question': 'Tell me about your background and how it applies to FluxGen.',
                    'answer': 'Provide specific examples of your relevant experience and skills.'
                },
                {
                    'question': 'What are your main responsibilities at FluxGen?',
                    'answer': 'Outline your core duties and how they contribute to company success.'
                },
                {
                    'question': 'How do you plan to execute on your role?',
                    'answer': 'Describe your strategy and approach with concrete examples.'
                }
            ]
        })
    
    def _get_role_talking_points(self, role):
        """Get role-specific talking points"""
        
        points_db = {
            'Founder & Technical Director': [
                'I ran a publicly listed flux manufacturing company in India — this isn\'t theoretical for me',
                'Our formulations are based on proven recipes from Jhaveri Weld Flux, adapted for the Canadian market',
                'Quality control is non-negotiable — every batch will be tested and certified before shipment',
                'We\'re not reinventing flux manufacturing — we\'re localizing proven processes for Canada',
                'My software engineering background brings modern data systems to traditional manufacturing'
            ],
            
            'Operations & Logistics Manager': [
                'I managed high-volume logistics at one of Canada\'s largest retailers — I know how to move materials efficiently',
                'Our supply chain strategy prioritizes Canadian suppliers to reduce lead times and costs',
                'I have strong contacts in Alberta\'s industrial and logistics networks from my time at Loblaws',
                'I\'m hands-on — I\'ll be on the floor daily ensuring smooth operations',
                'Our goal is 95%+ on-time delivery from day one — we\'re building reliability into the system'
            ],
            
            'Sales & Marketing Lead': [
                'I\'m the face of FluxGen — my job is to build relationships and win customers',
                'We\'re targeting 20-30 key accounts in Year 1 through direct outreach and trade shows',
                'Our value proposition is simple: local supply, fast delivery, and great service',
                'I speak the customer\'s language — I can communicate technical benefits clearly',
                'We\'re not selling commodity products — we\'re selling partnership and reliability'
            ],
            
            'Quality Assurance & Compliance Manager': [
                'Quality is my only job — if it doesn\'t meet spec, it doesn\'t ship',
                'We\'ll pursue AWS and CWB certifications from day one to meet customer requirements',
                'Every batch will have full traceability — we can trace any issue back to raw materials',
                'I\'m detail-oriented by nature — I thrive in environments where precision matters',
                'Our QC lab will be set up before production starts — quality comes first, always'
            ]
        }
        
        return points_db.get(role, [
            'I bring relevant experience and skills to my role at FluxGen',
            'I\'m committed to FluxGen\'s success and ready to execute',
            'I work collaboratively with the team to achieve our goals'
        ])
    
    def _get_role_dos_donts(self, role):
        """Get role-specific do's and don'ts"""
        
        general_dos = [
            'Be confident but not arrogant — you know your stuff, but stay humble',
            'Use specific examples from your experience when answering questions',
            'If you don\'t know something, defer to the team member who does',
            'Show enthusiasm for FluxGen — investors want to see you\'re all-in',
            'Listen carefully to questions before answering — don\'t rush'
        ]
        
        general_donts = [
            'Never say "I\'m still learning" or "I\'m figuring it out" — investors want experts, not learners',
            'Don\'t over-promise or exaggerate — be realistic about challenges',
            'Don\'t contradict other team members — maintain a united front',
            'Don\'t badmouth competitors — focus on FluxGen\'s strengths',
            'Don\'t use jargon without explanation — keep language clear'
        ]
        
        role_specific = {
            'Founder & Technical Director': {
                'dos': general_dos + [
                    'Emphasize your hands-on experience running Jhaveri Weld Flux at scale',
                    'Use technical terms confidently — but explain them if asked',
                    'Mention specific formulations or processes when relevant'
                ],
                'donts': general_donts + [
                    'Don\'t get too deep into chemistry unless asked — keep it accessible',
                    'Don\'t dismiss questions about your current software role — frame it as an asset'
                ]
            },
            'Operations & Logistics Manager': {
                'dos': general_dos + [
                    'Highlight your Loblaws experience managing complex logistics',
                    'Mention specific contacts or supplier relationships you\'re building',
                    'Talk about contingency plans — investors want to know you\'ve thought through risks'
                ],
                'donts': general_donts + [
                    'Don\'t say you\'ve "never worked in manufacturing" — focus on transferable skills',
                    'Don\'t make it sound like operations will be easy — acknowledge challenges'
                ]
            },
            'Sales & Marketing Lead': {
                'dos': general_dos + [
                    'Show energy and confidence — you\'re the public face of FluxGen',
                    'Name specific target customers or industries',
                    'Talk about your communication skills as a core strength'
                ],
                'donts': general_donts + [
                    'Don\'t promise unrealistic sales numbers — be conservative in estimates',
                    'Don\'t rely only on charisma — back up claims with strategy'
                ]
            },
            'Quality Assurance & Compliance Manager': {
                'dos': general_dos + [
                    'Emphasize your attention to detail and process discipline',
                    'Talk about specific certifications and testing procedures',
                    'Show you understand the critical importance of consistency'
                ],
                'donts': general_donts + [
                    'Don\'t minimize the importance of your non-manufacturing background — own your strengths',
                    'Don\'t suggest quality is "just following checklists" — it\'s strategic'
                ]
            }
        }
        
        return role_specific.get(role, {
            'dos': general_dos,
            'donts': general_donts
        })
    
    def generate_for_member(self, member_name: str) -> Path:
        """Generate prep document for a specific team member"""
        # Get team member data
        query = f"SELECT * FROM team_members WHERE name = '{member_name}'"
        result = self.db.execute_query(query)
        
        if not result:
            logger.error(f"Team member {member_name} not found")
            return None
        
        member = result[0]
        
        # Build content
        self.story = []
        self.build_content_for_member(member)
        
        # Generate filename
        filename = f"fluxgen_prep_{member_name.lower().replace(' ', '_')}_{self._get_timestamp()}"
        return self.generate_document(filename, f"Meeting Prep - {member_name}")
    
    def generate_all_members(self) -> list[Path]:
        """Generate prep documents for all team members"""
        team_members = self.db.get_team_members()
        generated_files = []
        
        for member in team_members:
            member_name = member.get('name')
            if member_name:
                file_path = self.generate_for_member(member_name)
                if file_path:
                    generated_files.append(file_path)
        
        return generated_files
    
    def _get_timestamp(self) -> str:
        """Get timestamp for filename"""
        from datetime import datetime
        return datetime.now().strftime('%Y%m%d_%H%M%S')
