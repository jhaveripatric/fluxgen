"""
Technical Specifications document generator for FluxGen
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.base import BaseDocumentGenerator
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class TechnicalSpecsGenerator(BaseDocumentGenerator):
    """Generates Technical Specifications document (6-8 pages)"""
    
    def __init__(self, database_manager, output_dir: Path):
        super().__init__(database_manager, output_dir)
    
    def build_content(self):
        """Build technical specifications content"""
        # Document title and company header
        self.add_company_header()
        self.add_title("Technical Specifications & Manufacturing Process")
        
        # Manufacturing Process Overview
        self._add_manufacturing_overview()
        
        # Process Flow Details
        self._add_process_flow()
        self.add_page_break()
        
        # Equipment Specifications
        self._add_equipment_specifications()
        
        # Quality Control Procedures
        self._add_quality_control()
        self.add_page_break()
        
        # Product Catalog
        self._add_product_catalog()
        
        # Certifications Roadmap
        self._add_certifications_roadmap()
        self.add_page_break()
        
        # Raw Material Requirements
        self._add_raw_materials()
        
        # Technical Standards & Compliance
        self._add_technical_standards()
        
        # Footer
        self.add_footer_info()
    
    def _add_manufacturing_overview(self):
        """Add manufacturing process overview"""
        self.add_heading1("Manufacturing Process Overview")
        
        # Get production target data
        production_targets = self.db.get_production_targets()
        
        overview_text = """
        FluxGen Industries employs advanced manufacturing processes to produce high-quality submerged arc welding (SAW) 
        flux and specialty alloys. The manufacturing system is designed for flexibility, quality, and scalability.
        <br/>
        <b>Core Manufacturing Philosophy:</b><br/>
        • Quality First: Every batch meets or exceeds industry standards<br/>
        • Consistency: Reproducible processes and standardized procedures<br/>
        • Flexibility: Ability to produce custom formulations<br/>
        • Efficiency: Optimized processes for competitive production costs<br/>
        • Sustainability: Environmentally responsible manufacturing practices
        <br/>
        <b>Production Capabilities:</b>
        FluxGen's phased production approach allows for controlled growth while maintaining quality standards.
        """
        
        self.add_body_text(overview_text)
        
        if production_targets:
            # Production capacity table
            capacity_data = [['Phase', 'Monthly Capacity (kg)', 'Facility Type', 'Automation Level', 'Staffing']]
            
            for target in production_targets:
                automation_level = {
                    'Manual-to-semi-automated': 'Manual + Basic Automation',
                    'Semi-automated to automated': 'Advanced Automation'
                }.get(target.get('facility_type', ''), 'TBD')
                
                staffing = {
                    'Pilot': '3-5 operators per shift',
                    'Scale-Up': '5-8 operators per shift'
                }.get(target.get('phase', ''), '2-3 operators per shift')
                
                capacity_data.append([
                    target.get('phase', 'N/A'),
                    f"{target.get('output_kg_month', 0):,}" if target.get('output_kg_month') else 'N/A',
                    target.get('facility_type', 'N/A'),
                    automation_level,
                    staffing
                ])
            
            self.add_table(capacity_data, [1.2, 1.4, 1.8, 1.6, 1.0], title="Production Capacity by Phase")
        
        process_overview_text = """
        <b>Manufacturing Principles:</b><br/>
        • Batch processing for quality control and traceability<br/>
        • Statistical process control for consistency<br/>
        • Preventive maintenance for equipment reliability<br/>
        • Continuous improvement and lean manufacturing practices<br/>
        • Environmental compliance and waste minimization<br/>
        
        <b>Technology Integration:</b><br/>
        • Process control systems for parameter monitoring<br/>
        • Quality management system with full traceability<br/>
        • Inventory management with real-time tracking<br/>
        • Automated testing and certification processes
        """
        
        self.add_body_text(process_overview_text)
        self.add_spacer()
    
    def _add_process_flow(self):
        """Add detailed process flow"""
        self.add_heading1("Detailed Manufacturing Process Flow")
        
        # Process steps table
        process_data = [
            ['Step', 'Process', 'Equipment', 'Key Parameters', 'Quality Controls'],
            ['1', 'Raw Material Receiving', 'Scales, testing equipment', 'Weight, moisture, composition', 'Incoming inspection, certificates'],
            ['2', 'Material Storage', 'Silos, climate control', 'Temperature, humidity', 'Inventory tracking, FIFO rotation'],
            ['3', 'Weighing & Batching', 'Automated batching system', 'Accuracy ±0.1%', 'Scale verification, batch records'],
            ['4', 'Blending', 'High-intensity mixers', 'Mix time, uniformity', 'Sample testing, homogeneity check'],
            ['5', 'Agglomeration', 'Pelletizing equipment', 'Binder ratio, pellet size', 'Size distribution, strength testing'],
            ['6', 'Drying', 'Rotary dryers', 'Temperature, residence time', 'Moisture content, temperature profile'],
            ['7', 'Screening', 'Vibrating screens', 'Particle size distribution', 'Size analysis, rejects handling'],
            ['8', 'Final Testing', 'Laboratory equipment', 'Chemistry, performance', 'Full analysis per AWS standards'],
            ['9', 'Packaging', 'Automated packaging', 'Weight, seal integrity', 'Package inspection, labeling'],
            ['10', 'Shipping', 'Warehouse systems', 'Inventory accuracy', 'Order verification, logistics tracking']
        ]
        
        self.add_table(process_data, [0.6, 1.4, 1.3, 1.4, 1.3], title="Manufacturing Process Steps")
        
        self.add_heading2("Critical Process Parameters")
        
        parameters_text = """
        <b>Raw Material Specifications:</b><br/>
        • Silica Sand: SiO₂ content 95%+, particle size 50-200 mesh<br/>
        • Dolomite: MgO content 20-22%, CaO content 30-35%<br/>
        • Calcite: CaCO₃ content 95%+, low sulfur content<br/>
        • Ferroalloys: Specific chemistry per application requirements<br/>
        • Moisture content: <0.5% for all raw materials<br/>
        
        <b>Blending Parameters:</b><br/>
        • Mix time: 15-30 minutes depending on batch size<br/>
        • Uniformity: Coefficient of variation <3%<br/>
        • Binder addition: 2-5% by weight (sodium silicate solution)<br/>
        • Temperature control: Ambient to 50°C maximum<br/>
        
        <b>Agglomeration Controls:</b><br/>
        • Pellet size: 0.7-4.0 mm (per AWS classification)<br/>
        • Green strength: >5 kg crush strength<br/>
        • Moisture: 8-12% after pelletizing<br/>
        • Sphericity: >80% for optimal flow characteristics<br/>
        
        <b>Drying Specifications:</b><br/>
        • Final moisture: <0.5%<br/>
        • Temperature: 300-600°C (product dependent)<br/>
        • Residence time: 45-90 minutes<br/>
        • Cooling rate: Controlled to prevent thermal shock
        """
        
        self.add_body_text(parameters_text)
        self.add_spacer()
    
    def _add_equipment_specifications(self):
        """Add equipment specifications section"""
        self.add_heading1("Equipment Specifications & Layout")
        
        # Equipment list table
        equipment_data = [
            ['Equipment', 'Specification', 'Capacity', 'Power Req.', 'Key Features'],
            ['Batch Mixer', 'High-intensity paddle mixer', '1,000 kg/batch', '75 kW', 'Variable speed, jacketed'],
            ['Pelletizing Disc', 'Inclined disc pelletizer', '500 kg/hr', '15 kW', 'Variable angle & speed'],
            ['Rotary Dryer', 'Co-current flow design', '800 kg/hr', '120 kW', 'Temperature control, dust collection'],
            ['Vibrating Screen', 'Multi-deck screening', '1,200 kg/hr', '5 kW', 'Multiple size fractions'],
            ['Packaging System', 'Automated bagging', '20 bags/min', '10 kW', 'Weight control, heat sealing'],
            ['Dust Collection', 'Baghouse filtration', '15,000 CFM', '25 kW', 'Pulse-jet cleaning'],
            ['Raw Material Silos', 'Steel construction', '50 ton capacity', 'N/A', 'Level monitoring, discharge gates'],
            ['Process Control', 'PLC-based system', 'Plant-wide', '5 kW', 'HMI interface, data logging'],
            ['Quality Lab', 'Testing equipment', 'Full analysis', '15 kW', 'Automated analyzers, calibration'],
            ['Material Handling', 'Conveyors, elevators', '2,000 kg/hr', '30 kW', 'Enclosed, dust-tight design']
        ]
        
        self.add_table(equipment_data, [1.3, 1.4, 1.0, 0.8, 1.5], title="Major Equipment Specifications")
        
        self.add_heading2("Facility Layout & Infrastructure")
        
        layout_text = """
        <b>Production Area Layout:</b><br/>
        • Raw Material Storage: 2,000 sq ft with segregated bays<br/>
        • Processing Area: 3,500 sq ft with overhead crane service<br/>
        • Packaging & Warehouse: 2,500 sq ft with shipping dock<br/>
        • Quality Laboratory: 400 sq ft with fume hoods and testing equipment<br/>
        • Maintenance Shop: 600 sq ft with spare parts storage<br/>
        • Office Space: 1,000 sq ft for administration and technical staff<br/>
        
        <b>Utility Requirements:</b><br/>
        • Electrical: 480V, 3-phase, 500 kW total demand<br/>
        • Natural Gas: 2 million BTU/hr for dryer operation<br/>
        • Compressed Air: 100 SCFM at 100 PSI for pneumatic systems<br/>
        • Water: 500 gal/day for process and cleaning<br/>
        • Wastewater: Treatment system for process water recycling<br/>
        
        <b>Environmental Systems:</b><br/>
        • Dust collection with 99.5% efficiency baghouse filters<br/>
        • Noise control with equipment enclosures and barriers<br/>
        • Spill containment and emergency response systems<br/>
        • Storm water management and runoff control<br/>
        
        <b>Safety & Security:</b><br/>
        • Fire suppression system with dry chemical and water spray<br/>
        • Emergency shower/eyewash stations throughout facility<br/>
        • Lockout/tagout procedures for equipment maintenance<br/>
        • Security system with access control and surveillance
        """
        
        self.add_body_text(layout_text)
        self.add_spacer()
    
    def _add_quality_control(self):
        """Add quality control procedures"""
        self.add_heading1("Quality Control & Testing Procedures")
        
        # Quality testing matrix
        testing_data = [
            ['Test Category', 'Parameter', 'Test Method', 'Frequency', 'Acceptance Criteria'],
            ['Chemical Analysis', 'SiO₂, Al₂O₃, CaO, MgO', 'XRF Spectroscopy', 'Every batch', 'AWS A5.17 limits'],
            ['Physical Properties', 'Particle size distribution', 'Sieve analysis', 'Every batch', '0.7-4.0 mm range'],
            ['Physical Properties', 'Moisture content', 'Loss on drying', 'Every batch', '<0.5%'],
            ['Physical Properties', 'Bulk density', 'Standard cup method', 'Every batch', '1.4-1.8 g/cm³'],
            ['Welding Performance', 'Tensile strength', 'AWS test procedure', 'Weekly', '>70 ksi minimum'],
            ['Welding Performance', 'Charpy impact', 'Impact testing', 'Weekly', '>27 J at -29°C'],
            ['Welding Performance', 'Chemical analysis of weld metal', 'Spectrographic', 'Weekly', 'Customer specification'],
            ['Quality Systems', 'Traceability records', 'Document review', 'Continuous', '100% traceability'],
            ['Quality Systems', 'Calibration status', 'Equipment check', 'Monthly', 'All equipment current'],
            ['Environmental', 'Dust emissions', 'Stack testing', 'Quarterly', '<20 mg/m³ outlet']
        ]
        
        self.add_table(testing_data, [1.2, 1.2, 1.2, 0.9, 1.5], title="Quality Control Testing Matrix")
        
        self.add_heading2("Quality Management System")
        
        qms_intro_text = """
        <b>ISO 9001:2015 Quality Management System:</b>
        FluxGen implements a comprehensive quality management system based on ISO 9001:2015 principles,
        ensuring consistent product quality and continuous improvement.
        """

        document_control_text = """
        <b>Document Control:</b><br/>
        • Standard Operating Procedures (SOPs) for all processes<br/>
        • Work instructions with revision control<br/>
        • Quality forms and checklists<br/>
        • Training records and competency assessments<br/>
        • Change control procedures for process modifications
        """

        spc_text = """
        <b>Statistical Process Control:</b><br/>
        • Control charts for key process parameters<br/>
        • Capability studies for critical characteristics<br/>
        • Trend analysis and corrective action procedures<br/>
        • Process improvement initiatives based on data analysis
        """

        supplier_quality_text = """
        <b>Supplier Quality:</b><br/>
        • Approved supplier list with qualification criteria<br/>
        • Incoming material inspection and testing<br/>
        • Supplier audits and performance monitoring<br/>
        • Certificate of analysis verification<br/>
        • Non-conforming material procedures
        """

        customer_quality_text = """
        <b>Customer Quality:</b><br/>
        • Customer specification review and approval<br/>
        • Custom product qualification procedures<br/>
        • Customer feedback and complaint handling<br/>
        • Performance monitoring and reporting<br/>
        • Continuous improvement based on customer input
        """

        self.add_body_text(qms_intro_text)
        self.add_body_text(document_control_text)
        self.add_body_text(spc_text)
        self.add_body_text(supplier_quality_text)
        self.add_body_text(customer_quality_text)
        
        # Traceability system
        traceability_data = [
            ['Traceability Element', 'Information Captured', 'System', 'Retention Period'],
            ['Raw Materials', 'Supplier, lot #, analysis, receipt date', 'ERP System', '7 years'],
            ['Production Batches', 'Recipe, parameters, operators, equipment', 'MES System', '7 years'],
            ['Quality Testing', 'Test results, analyst, equipment, dates', 'LIMS', '10 years'],
            ['Finished Product', 'Batch records, packaging, shipping', 'ERP System', '7 years'],
            ['Customer Complaints', 'Investigation, root cause, corrective action', 'Quality System', '10 years'],
            ['Calibration Records', 'Equipment, standards, frequency, results', 'Calibration System', 'Equipment life + 3 years']
        ]
        
        self.add_table(traceability_data, [1.5, 2.0, 1.2, 1.3], title="Traceability System Requirements")
        
        self.add_spacer()
    
    def _add_product_catalog(self):
        """Add product catalog section"""
        self.add_heading1("Product Catalog & Technical Specifications")
        
        # Get alloys catalog data
        alloys = self.db.get_alloys_catalog()
        
        if alloys:
            # Product specifications table
            product_data = [['Product Code', 'Description', 'Application', 'Key Specifications', 'AWS Classification']]
            
            for alloy in alloys:
                # Create AWS classification based on alloy symbol
                aws_class = f"F{alloy.get('alloy_symbol', '')[1:] if alloy.get('alloy_symbol', '').startswith('F') else alloy.get('alloy_symbol', '')}"
                
                product_data.append([
                    alloy.get('alloy_symbol', 'N/A'),
                    alloy.get('alloy_name', 'N/A')[:30] + '...' if alloy.get('alloy_name') and len(alloy.get('alloy_name', '')) > 30 else alloy.get('alloy_name', 'N/A'),
                    alloy.get('application', 'N/A')[:40] + '...' if alloy.get('application') and len(alloy.get('application', '')) > 40 else alloy.get('application', 'N/A'),
                    alloy.get('typical_composition', 'N/A')[:35] + '...' if alloy.get('typical_composition') and len(alloy.get('typical_composition', '')) > 35 else alloy.get('typical_composition', 'N/A'),
                    aws_class
                ])
            
            self.add_table(product_data, [1.0, 1.4, 1.8, 1.5, 1.3], title="Standard Product Portfolio")
        
        self.add_heading2("Product Categories & Applications")
        
        products_text = """
        <b>Standard SAW Flux Products:</b>
        FluxGen manufactures a comprehensive range of SAW flux products designed for various welding applications 
        and base metal combinations.
        <br/>
        <b>Basic Flux (F6XX Series):</b><br/>
        • Applications: General structural welding, ship building<br/>
        • Base metals: Carbon and low alloy steels<br/>
        • Characteristics: Good slag detachability, smooth bead profile<br/>
        • Typical chemistry: CaO-SiO₂ based system<br/>
        
        <b>Low Hydrogen Flux (F7XX Series):</b><br/>
        • Applications: Pressure vessels, critical structures<br/>
        • Base metals: Medium to high strength steels<br/>
        • Characteristics: Low diffusible hydrogen, excellent toughness<br/>
        • Typical chemistry: CaF₂-CaO-SiO₂ system<br/>
        
        <b>Neutral Flux (F6A2 and similar):</b><br/>
        • Applications: Multi-pass welding, build-up operations<br/>
        • Base metals: Various carbon and alloy steels<br/>
        • Characteristics: Minimal weld metal dilution<br/>
        • Typical chemistry: SiO₂-MnO based system<br/>
        
        <b>Specialty Alloy Products:</b><br/>
        • Weather-resistant steel flux for Corten applications<br/>
        • Stainless steel flux for corrosion-resistant applications<br/>
        • High-strength steel flux for offshore and arctic applications<br/>
        • Custom formulations for specific customer requirements
        """
        
        self.add_body_text(products_text)
        
        # Performance specifications table
        performance_data = [
            ['Property', 'F6A2-EM12K', 'F7A2-EM12K', 'F7A4-EM12K', 'Test Method'],
            ['Tensile Strength (min)', '70 ksi', '80 ksi', '90 ksi', 'AWS A4.2'],
            ['Yield Strength (min)', '58 ksi', '68 ksi', '78 ksi', 'AWS A4.2'],
            ['Elongation (min)', '22%', '20%', '18%', 'AWS A4.2'],
            ['CVN Impact @ -29°C', '27 J', '40 J', '35 J', 'AWS A4.2'],
            ['Diffusible Hydrogen', '<8 ml/100g', '<4 ml/100g', '<4 ml/100g', 'AWS A4.3'],
            ['Slag Removal', 'Excellent', 'Good', 'Good', 'Visual assessment'],
            ['Bead Appearance', 'Smooth', 'Smooth', 'Smooth', 'Visual assessment']
        ]
        
        self.add_table(performance_data, [1.3, 1.1, 1.1, 1.1, 1.4], title="Typical Mechanical Properties")
        
        self.add_spacer()
    
    def _add_certifications_roadmap(self):
        """Add certifications roadmap section"""
        self.add_heading1("Certifications & Compliance Roadmap")
        
        # Get certifications data
        certifications = self.db.get_certifications_roadmap()
        
        if certifications:
            # Certifications timeline table
            cert_data = [['Certification', 'Certifying Body', 'Phase', 'Target Date', 'Status', 'Cost Estimate']]
            
            for cert in certifications:
                cert_data.append([
                    cert.get('certification_name', 'N/A'),
                    cert.get('certification_body', 'N/A'),
                    f"Phase {cert.get('phase', 'N/A')}",
                    self.format_date(cert.get('target_date')),
                    cert.get('status', 'N/A'),
                    self.format_currency(cert.get('cost_estimate_cad'))
                ])
            
            self.add_table(cert_data, [1.8, 1.2, 0.8, 1.0, 0.8, 1.4], title="Certification Timeline & Requirements")
        
        self.add_heading2("Regulatory Compliance Framework")
        
        product_cert_intro_text = """
        <b>Product Certifications:</b>
        """

        aws_cert_text = """
        <b>AWS (American Welding Society) Certification:</b><br/>
        • A5.17 Specification for Carbon Steel Electrodes and Fluxes for SAW<br/>
        • A5.23 Specification for Low-Alloy Steel Electrodes and Fluxes for SAW<br/>
        • Product qualification testing and ongoing surveillance<br/>
        • Certificate of Conformance for each product shipment
        """

        cwb_cert_text = """
        <b>CWB (Canadian Welding Bureau) Approval:</b><br/>
        • CWB W47.1 Certification of Companies for Welding<br/>
        • Product approval for use in Canadian pressure vessel applications<br/>
        • Quality system certification and periodic audits<br/>
        • Canadian compliance for government and institutional projects
        """

        iso_cert_text = """
        <b>ISO 9001:2015 Quality Management:</b><br/>
        • Third-party certification of quality management system<br/>
        • Annual surveillance audits and continuous improvement<br/>
        • Customer confidence and international market access<br/>
        • Process standardization and documentation requirements
        """

        env_compliance_text = """
        <b>Environmental Compliance:</b><br/>
        • Provincial environmental permits for manufacturing operations<br/>
        • Air emissions compliance with Alberta Environment standards<br/>
        • Waste management and recycling program implementation<br/>
        • Environmental management system (ISO 14001 consideration)
        """

        safety_compliance_text = """
        <b>Workplace Safety:</b><br/>
        • Alberta OHS compliance and safety management system<br/>
        • WHMIS training and hazardous material management<br/>
        • Emergency response planning and equipment<br/>
        • Regular safety audits and incident reporting systems
        """

        self.add_body_text(product_cert_intro_text)
        self.add_body_text(aws_cert_text)
        self.add_body_text(cwb_cert_text)
        self.add_body_text(iso_cert_text)
        self.add_body_text(env_compliance_text)
        self.add_body_text(safety_compliance_text)
        
        # Compliance timeline
        timeline_data = [
            ['Milestone', 'Timeline', 'Activities', 'Dependencies'],
            ['Facility Permits', 'Months 1-3', 'Building permits, environmental approvals', 'Site selection, design completion'],
            ['Quality System', 'Months 4-6', 'ISO 9001 implementation, documentation', 'Staff hiring, training completion'],
            ['Product Testing', 'Months 7-9', 'AWS qualification testing, approvals', 'Equipment commissioning, pilot production'],
            ['Certifications', 'Months 10-12', 'Third-party audits, certificate issuance', 'Quality system maturity, test results'],
            ['Market Entry', 'Month 12+', 'Customer trials, commercial sales', 'All certifications complete']
        ]
        
        self.add_table(timeline_data, [1.2, 1.0, 2.2, 1.6], title="Certification Implementation Timeline")
        
        self.add_spacer()
    
    def _add_raw_materials(self):
        """Add raw material requirements section"""
        self.add_heading1("Raw Material Requirements & Sourcing")
        
        # Raw materials specifications
        materials_data = [
            ['Raw Material', 'Specification', 'Monthly Usage (tons)', 'Primary Supplier', 'Backup Source'],
            ['Silica Sand', 'SiO₂ >95%, 50-200 mesh', '15-20', 'Western Canada Sand', 'US Silica'],
            ['Dolomite', 'MgO 20-22%, CaO 30-35%', '8-12', 'Graymont Ltd (BC)', 'Carmeuse (US)'],
            ['Calcite', 'CaCO₃ >95%, low sulfur', '5-8', 'Omya Canada', 'Mississippi Lime'],
            ['Ferromanganese', 'Mn 75-80%, C <0.75%', '2-3', 'Ferroglobe Canada', 'Eramet Norway'],
            ['Ferrosilicon', 'Si 70-75%, low Al', '1-2', 'Elkem Canada', 'Ferroglobe'],
            ['Sodium Silicate', 'SiO₂/Na₂O ratio 3.2-3.4', '1-2', 'PQ Corporation', 'Kapp-Chemie'],
            ['Packaging Materials', 'Multi-wall kraft bags', '2,000 bags', 'Mondi Bags Canada', 'International Paper']
        ]
        
        self.add_table(materials_data, [1.2, 1.6, 1.2, 1.4, 1.6], title="Raw Material Specifications & Sources")
        
        self.add_heading2("Supply Chain Strategy")
        
        canadian_content_text = """
        <b>Canadian Content Maximization:</b>
        FluxGen prioritizes Canadian suppliers to achieve 80-90% domestic content, supporting local
        economy and reducing supply chain risk.
        """

        supplier_qual_text = """
        <b>Supplier Qualification:</b><br/>
        • Technical capability assessment and quality system audits<br/>
        • Financial stability evaluation and business continuity planning<br/>
        • Logistics capability and delivery performance tracking<br/>
        • Environmental and social responsibility compliance<br/>
        • Long-term partnership potential and strategic alignment
        """

        inventory_mgmt_text = """
        <b>Inventory Management:</b><br/>
        • 30-45 day safety stock for primary raw materials<br/>
        • 15-30 day inventory for secondary materials<br/>
        • Seasonal purchasing for cost optimization<br/>
        • Just-in-time delivery for packaging materials<br/>
        • Strategic stockpiling for supply disruption mitigation
        """

        quality_assurance_text = """
        <b>Quality Assurance:</b><br/>
        • Certificate of analysis for every shipment<br/>
        • Incoming inspection and testing procedures<br/>
        • Supplier corrective action processes<br/>
        • Alternative source qualification and approval<br/>
        • Continuous monitoring of supplier performance
        """

        cost_mgmt_text = """
        <b>Cost Management:</b><br/>
        • Annual supply agreements with price escalation clauses<br/>
        • Volume commitments for preferential pricing<br/>
        • Market intelligence and commodity price monitoring<br/>
        • Transportation optimization and freight consolidation<br/>
        • Waste reduction and material utilization improvement
        """

        self.add_body_text(canadian_content_text)
        self.add_body_text(supplier_qual_text)
        self.add_body_text(inventory_mgmt_text)
        self.add_body_text(quality_assurance_text)
        self.add_body_text(cost_mgmt_text)
        self.add_spacer()
    
    def _add_technical_standards(self):
        """Add technical standards and compliance section"""
        self.add_heading1("Technical Standards & Industry Compliance")
        
        # Standards compliance table
        standards_data = [
            ['Standard', 'Scope', 'Compliance Level', 'Testing Requirements', 'Certification Body'],
            ['AWS A5.17', 'Carbon Steel SAW Electrodes/Flux', 'Full Compliance', 'Chemical, mechanical, radiographic', 'AWS'],
            ['AWS A5.23', 'Low Alloy Steel SAW Materials', 'Full Compliance', 'Chemical, mechanical, impact', 'AWS'],
            ['CSA W48', 'Filler Metals for Welding', 'Full Compliance', 'Performance qualification', 'CSA Group'],
            ['ASME Sec II-C', 'Welding Rods/Electrodes/Filler', 'Full Compliance', 'Material properties', 'ASME'],
            ['API 5L-X', 'Line Pipe Welding Materials', 'Selective Compliance', 'Sour service testing', 'API'],
            ['ISO 14341', 'Wire Electrodes and Deposits', 'Reference Standard', 'Chemical analysis', 'ISO'],
            ['EN 760', 'SAW Consumables', 'Reference Standard', 'European test methods', 'EN']
        ]
        
        self.add_table(standards_data, [1.0, 1.6, 1.0, 1.4, 1.0], title="Applicable Technical Standards")
        
        self.add_heading2("Performance Testing Protocols")
        
        performance_testing_text = """
        <b>Welding Performance Testing:</b>
        All FluxGen products undergo comprehensive performance testing according to AWS A4.2 procedures:
        <br/>
        • <b>Tensile Testing:</b> Ultimate and yield strength determination per ASTM A370<br/>
        • <b>Bend Testing:</b> Root and face bend testing for ductility assessment<br/>
        • <b>Impact Testing:</b> Charpy V-notch testing at specified temperatures<br/>
        • <b>Hardness Testing:</b> Brinell hardness of weld metal and heat-affected zone<br/>
        • <b>Chemical Analysis:</b> Weld metal composition verification<br/>
        • <b>Radiographic Testing:</b> Weld quality and discontinuity assessment
        """

        special_testing_text = """
        <b>Special Testing Requirements:</b><br/>
        • <b>Hydrogen Testing:</b> Diffusible hydrogen measurement per AWS A4.3<br/>
        • <b>Sour Service Testing:</b> For oil & gas applications per NACE MR0175<br/>
        • <b>Low Temperature Testing:</b> Impact testing down to -46°C for arctic applications<br/>
        • <b>Fatigue Testing:</b> Cyclic loading performance for dynamic applications<br/>
        • <b>Corrosion Testing:</b> Salt spray and atmospheric exposure testing
        """

        process_qual_text = """
        <b>Process Qualification:</b><br/>
        • Welding Procedure Specification (WPS) development<br/>
        • Procedure Qualification Record (PQR) testing<br/>
        • Welder Performance Qualification support<br/>
        • Pre-qualified joint design assistance<br/>
        • Technical support for customer applications
        """

        documentation_cert_text = """
        <b>Documentation & Certification:</b><br/>
        • Material Test Reports (MTR) for each batch<br/>
        • Certificate of Compliance with applicable standards<br/>
        • Welding consumable data sheets with performance data<br/>
        • Application guides and technical bulletins<br/>
        • Welding procedure recommendations
        """

        self.add_body_text(performance_testing_text)
        self.add_body_text(special_testing_text)
        self.add_body_text(process_qual_text)
        self.add_body_text(documentation_cert_text)
        self.add_spacer()
    
    def generate(self) -> Path:
        """Generate the Technical Specifications PDF"""
        self.story = []  # Reset story
        self.build_content()
        
        filename = f"fluxgen_technical_specifications_{self._get_timestamp()}"
        return self.generate_document(filename, "FluxGen Industries - Technical Specifications")
    
    def _get_timestamp(self) -> str:
        """Get timestamp for filename"""
        from datetime import datetime
        return datetime.now().strftime('%Y%m%d_%H%M%S')