"""
Site Requirements document generator for FluxGen
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from generators.base import BaseDocumentGenerator
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class SiteRequirementsGenerator(BaseDocumentGenerator):
    """Generates Site Requirements document (3-4 pages)"""
    
    def __init__(self, database_manager, output_dir: Path):
        super().__init__(database_manager, output_dir)
    
    def build_content(self):
        """Build site requirements content"""
        # Document title and company header
        self.add_company_header()
        self.add_title("Facility Site Requirements & Specifications")
        
        # Executive Summary
        self._add_site_executive_summary()
        
        # Land Requirements
        self._add_land_requirements()
        
        # Utilities Requirements
        self._add_utilities_requirements()
        self.add_page_break()
        
        # Infrastructure Needs
        self._add_infrastructure_needs()
        
        # Zoning & Regulatory
        self._add_zoning_regulatory()
        
        # Facility Layout
        self._add_facility_layout()
        self.add_page_break()
        
        # Environmental Considerations
        self._add_environmental_considerations()
        
        # Site Selection Criteria
        self._add_site_selection_criteria()
        
        # Footer
        self.add_footer_info()
    
    def _add_site_executive_summary(self):
        """Add site requirements executive summary"""
        self.add_heading1("Site Requirements Executive Summary")
        
        summary_text = """
        FluxGen Industries requires a strategic industrial location in the Airdrie region to establish 
        its SAW flux manufacturing facility. The site must accommodate current production requirements 
        while providing expansion capability for future growth.
        
        <br/>
        <b>Key Site Requirements:</b>
        <br/>
        • Land Area: 10-15 acres with expansion potential
        <br/>
        • Zoning: Heavy industrial with chemical processing permits
        <br/>
        • Utilities: High-capacity electrical, natural gas, water, and wastewater
        <br/>
        • Transportation: Highway access with rail connectivity preferred
        <br/>
        • Environmental: Compliance with air quality and waste management regulations
        <br/>
        
        <b>Strategic Location Factors:</b>
        <br/>
        • Proximity to major transportation corridors (Highway 2, Calgary ring road)
        <br/>
        • Access to skilled workforce in Calgary-Airdrie industrial corridor
        <br/>
        • Reasonable distance from suppliers and customers
        <br/>
        • Municipal support for industrial development and job creation
        <br/>
        • Competitive land and utility costs
        <br/>
        
        <b>Investment Considerations:</b>
        The facility site selection will significantly impact FluxGen's operational efficiency, 
        transportation costs, and expansion flexibility. The chosen location must support both 
        immediate production needs and long-term strategic growth objectives.
        """
        
        self.add_body_text(summary_text)
        self.add_spacer()
    
    def _add_land_requirements(self):
        """Add land requirements section"""
        self.add_heading1("Land Area & Physical Requirements")
        
        # Land use breakdown table
        land_use_data = [
            ['Facility Area', 'Initial Size', 'Expansion Size', 'Total Requirement', 'Key Features'],
            ['Manufacturing Building', '10,000 sq ft', '15,000 sq ft', '25,000 sq ft', 'High bay, crane service, utilities'],
            ['Raw Material Storage', '3,000 sq ft', '5,000 sq ft', '8,000 sq ft', 'Covered silos, segregated bays'],
            ['Finished Goods Warehouse', '4,000 sq ft', '6,000 sq ft', '10,000 sq ft', 'Climate controlled, loading docks'],
            ['Office & Laboratory', '2,000 sq ft', '1,000 sq ft', '3,000 sq ft', 'HVAC, fume hoods, meeting rooms'],
            ['Maintenance Shop', '1,000 sq ft', '500 sq ft', '1,500 sq ft', 'Equipment access, parts storage'],
            ['Parking & Landscaping', '5,000 sq ft', '2,000 sq ft', '7,000 sq ft', 'Employee & visitor parking'],
            ['Outdoor Storage/Expansion', '10,000 sq ft', '20,000 sq ft', '30,000 sq ft', 'Future expansion, equipment storage'],
            ['Total Building Area', '25,000 sq ft', '29,500 sq ft', '54,500 sq ft', ''],
            ['Total Land Requirement', '10 acres', '5 acres', '15 acres', 'Including setbacks & reserves']
        ]
        
        self.add_table(land_use_data, [1.5, 1.0, 1.0, 1.2, 1.3], title="Facility Land Use Planning")
        
        self.add_heading2("Site Characteristics & Requirements")
        
        characteristics_text = """
        <b>Topography & Soil Conditions:</b>
        <br/>
        • Relatively level terrain to minimize grading and foundation costs
        <br/>
        • Well-draining soils suitable for heavy industrial construction
        <br/>
        • Stable soil conditions for equipment foundations and building loads
        <br/>
        • Minimal environmental contamination or geotechnical challenges
        <br/>
        • Flood zone considerations and drainage planning
        <br/>
        
        <b>Site Configuration:</b>
        <br/>
        • Rectangular or square configuration for efficient layout
        <br/>
        • Multiple access points for truck and employee traffic
        <br/>
        • Adequate setbacks from property lines and neighboring uses
        <br/>
        • Orientation allowing for future expansion without disruption
        <br/>
        • Buffer areas for environmental compliance and aesthetics
        <br/>
        
        <b>Accessibility Requirements:</b>
        <br/>
        • Direct access to major arterial roads (Highway 2 corridor preferred)
        <br/>
        • Truck access routes avoiding residential areas
        <br/>
        • Employee access with public transit connectivity
        <br/>
        • Emergency vehicle access for fire and ambulance services
        <br/>
        • Clear sight lines and safe ingress/egress for all vehicle types
        <br/>
        
        <b>Future Expansion Considerations:</b>
        <br/>
        • Additional 5-10 acres available for purchase or lease
        <br/>
        • Expansion areas not constrained by utilities or environmental issues
        <br/>
        • Ability to add production capacity without disrupting existing operations
        <br/>
        • Flexibility for different product lines or manufacturing processes
        <br/>
        • Option for additional buildings or outdoor storage areas
        """
        
        self.add_body_text(characteristics_text)
        self.add_spacer()
    
    def _add_utilities_requirements(self):
        """Add utilities requirements section"""
        self.add_heading1("Utilities & Infrastructure Requirements")
        
        # Utilities requirements table
        utilities_data = [
            ['Utility', 'Initial Requirement', 'Future Requirement', 'Specifications', 'Backup/Redundancy'],
            ['Electrical Power', '300 kW demand', '500 kW demand', '480V, 3-phase service', 'Emergency generator 150 kW'],
            ['Natural Gas', '1.5 MMBtu/hr', '3.0 MMBtu/hr', 'Medium pressure service', 'Propane backup for critical equipment'],
            ['Water Supply', '200 gal/day', '500 gal/day', 'Potable water, 60+ PSI', 'Storage tank for process water'],
            ['Wastewater', '150 gal/day', '400 gal/day', 'Industrial discharge permit', 'On-site treatment if required'],
            ['Compressed Air', '50 SCFM', '100 SCFM', '100 PSI, clean & dry', 'Dual compressors for reliability'],
            ['Communications', 'High-speed internet', 'Fiber connectivity', '100+ Mbps bandwidth', 'Redundant providers'],
            ['Waste Management', '2 dumpsters/week', '4 dumpsters/week', 'Industrial waste collection', 'Recycling programs']
        ]
        
        self.add_table(utilities_data, [1.2, 1.2, 1.2, 1.4, 1.0], title="Utility Requirements & Specifications")
        
        self.add_heading2("Electrical Infrastructure")
        
        electrical_text = """
        <b>Primary Electrical Service:</b>
        <br/>
        • 480V, 3-phase service with 300 kW initial capacity
        <br/>
        • Expansion capability to 500+ kW for future growth
        <br/>
        • High-voltage switch gear and distribution panels
        <br/>
        • Power factor correction to maintain efficiency
        <br/>
        • Lightning protection system for equipment safety
        <br/>
        
        <b>Equipment Power Requirements:</b>
        <br/>
        • Batch Mixer: 75 kW variable frequency drive
        <br/>
        • Pelletizing Equipment: 15 kW with speed control
        <br/>
        • Rotary Dryer: 120 kW including fans and heating
        <br/>
        • Material Handling: 30 kW for conveyors and elevators
        <br/>
        • Dust Collection: 25 kW for baghouse and fans
        <br/>
        • Building Systems: 35 kW for lighting, HVAC, compressed air
        <br/>
        
        <b>Emergency Power:</b>
        <br/>
        • 150 kW diesel generator for critical systems
        <br/>
        • Automatic transfer switch with 10-second response
        <br/>
        • Fuel tank capacity for 48-hour operation
        <br/>
        • Emergency lighting and life safety systems
        <br/>
        • UPS systems for process control and communications
        <br/>
        
        <b>Energy Efficiency Measures:</b>
        <br/>
        • LED lighting throughout facility with occupancy sensors
        <br/>
        • High-efficiency motors with variable frequency drives
        <br/>
        • Power monitoring and energy management systems
        <br/>
        • Heat recovery from dryer exhaust for building heating
        <br/>
        • Solar panel installation consideration for future sustainability
        """
        
        self.add_body_text(electrical_text)
        
        self.add_heading2("Gas & Water Systems")
        
        gas_water_text = """
        <b>Natural Gas Requirements:</b>
        <br/>
        • Medium pressure service (2+ PSI) for dryer operations
        <br/>
        • 1.5 MMBtu/hr initial capacity, expandable to 3.0 MMBtu/hr
        <br/>
        • Pressure regulation and safety shut-off systems
        <br/>
        • Gas detection and alarm systems for safety
        <br/>
        • Backup propane system for critical equipment
        <br/>
        
        <b>Water Systems:</b>
        <br/>
        • Potable water for employee facilities and emergency systems
        <br/>
        • Process water for equipment cooling and cleaning
        <br/>
        • Fire protection water with adequate pressure and flow
        <br/>
        • Wastewater collection and treatment as required
        <br/>
        • Stormwater management and runoff control
        <br/>
        
        <b>Compressed Air System:</b>
        <br/>
        • 50 SCFM initial capacity, 100+ PSI delivery pressure
        <br/>
        • Dual compressors for redundancy and maintenance
        <br/>
        • Air dryer and filtration for clean, dry air
        <br/>
        • Distribution piping to all equipment locations
        <br/>
        • Monitoring and leak detection systems
        """
        
        self.add_body_text(gas_water_text)
        self.add_spacer()
    
    def _add_infrastructure_needs(self):
        """Add infrastructure needs section"""
        self.add_heading1("Transportation & Logistics Infrastructure")
        
        # Transportation requirements
        transport_data = [
            ['Transportation Mode', 'Requirement', 'Specifications', 'Usage Pattern', 'Infrastructure Needs'],
            ['Truck Access', 'Primary shipping mode', '53-foot trailers, 80,000 lb GVW', 'Daily inbound/outbound', 'Wide turning radii, loading docks'],
            ['Rail Access', 'Bulk materials (preferred)', 'Rail spur, covered hoppers', 'Weekly/bi-weekly', 'Rail siding, unloading equipment'],
            ['Employee Vehicles', 'Daily workforce', '25-30 parking spaces', 'Shift changes', 'Paved parking, lighting, security'],
            ['Emergency Vehicles', 'Safety compliance', 'Fire trucks, ambulances', 'As needed', 'Clear access routes, hydrants'],
            ['Maintenance Vehicles', 'Equipment service', 'Service trucks, cranes', 'Weekly service calls', 'Equipment access doors'],
            ['Visitor Parking', 'Customers, vendors', '10-15 spaces', 'Business hours', 'Separate from employee parking']
        ]
        
        self.add_table(transport_data, [1.2, 1.2, 1.4, 1.0, 1.2], title="Transportation Infrastructure Requirements")
        
        self.add_heading2("Road Access & Traffic Considerations")
        
        traffic_text = """
        <b>Primary Access Requirements:</b>
        <br/>
        • Direct connection to Highway 2 corridor or major arterial road
        <br/>
        • Minimum 24-foot wide access road with concrete or heavy-duty asphalt
        <br/>
        • Traffic signal or controlled intersection for safe truck access
        <br/>
        • Adequate sight distances for safe vehicle movement
        <br/>
        • Separation of truck and employee traffic where possible
        <br/>
        
        <b>Traffic Generation:</b>
        <br/>
        • Truck Traffic: 8-12 trucks per day (inbound materials, outbound products)
        <br/>
        • Employee Traffic: 25-30 vehicles per day during shift changes
        <br/>
        • Visitor Traffic: 5-10 vehicles per day (customers, vendors, services)
        <br/>
        • Peak Traffic: Morning and evening shift changes, delivery periods
        <br/>
        
        <b>Internal Circulation:</b>
        <br/>
        • One-way circulation pattern to minimize conflicts
        <br/>
        • Loading dock areas separated from parking
        <br/>
        • Fire lane access maintained around all buildings
        <br/>
        • Pedestrian walkways separated from vehicle areas
        <br/>
        • Clear signage and traffic control devices
        <br/>
        
        <b>Rail Infrastructure (Preferred):</b>
        <br/>
        • Direct rail spur connection to CN or CP main lines
        <br/>
        • Covered unloading facility for bulk materials
        <br/>
        • Rail car storage capacity for 2-3 cars
        <br/>
        • Material handling equipment for efficient unloading
        <br/>
        • Switch equipment and signaling as required by railway
        """
        
        self.add_body_text(traffic_text)
        self.add_spacer()
    
    def _add_zoning_regulatory(self):
        """Add zoning and regulatory requirements"""
        self.add_heading1("Zoning & Regulatory Requirements")
        
        # Regulatory requirements table
        regulatory_data = [
            ['Regulatory Category', 'Requirement', 'Jurisdiction', 'Timeline', 'Key Considerations'],
            ['Zoning Designation', 'Heavy Industrial (M-2 or equiv)', 'Municipal', '2-4 months', 'Chemical processing permitted'],
            ['Development Permit', 'Site plan approval', 'Municipal', '3-6 months', 'Building placement, landscaping'],
            ['Building Permit', 'Construction authorization', 'Municipal', '2-3 months', 'Code compliance, inspections'],
            ['Environmental Permit', 'Air emissions, waste discharge', 'Provincial', '6-12 months', 'Environmental impact assessment'],
            ['Fire Safety Approval', 'Fire prevention/suppression', 'Municipal/Provincial', '1-2 months', 'Access, water supply, systems'],
            ['Occupancy Permit', 'Final approval to operate', 'Municipal', '1 month', 'All systems operational, inspected']
        ]
        
        self.add_table(regulatory_data, [1.3, 1.4, 1.0, 1.0, 1.3], title="Regulatory Approval Requirements")
        
        self.add_heading2("Municipal Requirements")
        
        municipal_text = """
        <b>City of Airdrie Requirements:</b>
        <br/>
        • Land Use Bylaw compliance for industrial development
        <br/>
        • Development permit application with detailed site plans
        <br/>
        • Building permit applications for all structures
        <br/>
        • Municipal utility connections and capacity allocations
        <br/>
        • Business license and operational permits
        <br/>
        
        <b>Setback & Buffer Requirements:</b>
        <br/>
        • Minimum 30-foot setbacks from all property lines
        <br/>
        • 50-foot buffer from residential or commercial zones
        <br/>
        • Landscape screening along public road frontages
        <br/>
        • Fence and gate requirements for security and safety
        <br/>
        • Signage regulations and architectural standards
        <br/>
        
        <b>Municipal Services:</b>
        <br/>
        • Fire protection services and emergency response
        <br/>
        • Municipal water and wastewater connections
        <br/>
        • Storm drainage and stormwater management
        <br/>
        • Solid waste collection and recycling services
        <br/>
        • Snow removal and road maintenance for access roads
        """
        
        self.add_body_text(municipal_text)
        
        self.add_heading2("Environmental Compliance")
        
        environmental_text = """
        <b>Alberta Environment Requirements:</b>
        <br/>
        • Environmental Protection and Enhancement Act compliance
        <br/>
        • Air emissions permit for dust and combustion sources
        <br/>
        • Waste management permit for industrial waste streams
        <br/>
        • Groundwater protection and monitoring requirements
        <br/>
        • Spill prevention and emergency response planning
        <br/>
        
        <b>Air Quality Management:</b>
        <br/>
        • Dust collection system with 99.5%+ efficiency
        <br/>
        • Stack height calculations and dispersion modeling
        <br/>
        • Ambient air quality monitoring if required
        <br/>
        • Fugitive emissions control measures
        <br/>
        • Regular emissions testing and reporting
        <br/>
        
        <b>Waste & Water Management:</b>
        <br/>
        • Industrial waste characterization and disposal
        <br/>
        • Wastewater discharge permit if connecting to municipal system
        <br/>
        • Stormwater management plan with retention/detention
        <br/>
        • Spill containment and cleanup procedures
        <br/>
        • Recycling programs for packaging and materials
        <br/>
        
        <b>Noise & Vibration Control:</b>
        <br/>
        • Noise impact assessment and mitigation measures
        <br/>
        • Equipment enclosures and sound barriers
        <br/>
        • Operating hour restrictions if required
        <br/>
        • Vibration control for sensitive equipment
        <br/>
        • Community relations and complaint resolution procedures
        """
        
        self.add_body_text(environmental_text)
        self.add_spacer()
    
    def _add_facility_layout(self):
        """Add facility layout section"""
        self.add_heading1("Facility Layout & Design Considerations")
        
        # Layout zones table
        layout_data = [
            ['Facility Zone', 'Size (sq ft)', 'Key Features', 'Adjacent Zones', 'Special Requirements'],
            ['Raw Material Receiving', '1,500', 'Truck dock, scales, silos', 'Storage, Production', 'Dust control, material flow'],
            ['Raw Material Storage', '3,000', 'Segregated bays, silos', 'Receiving, Production', 'Climate control, inventory mgmt'],
            ['Production Area', '6,000', 'Processing equipment', 'Storage, QC Lab', 'Overhead crane, utilities'],
            ['Quality Control Lab', '400', 'Testing equipment, fume hoods', 'Production, Offices', 'Vibration isolation, HVAC'],
            ['Finished Goods Warehouse', '4,000', 'Racking, shipping dock', 'Production, Shipping', 'Climate control, security'],
            ['Maintenance Shop', '600', 'Equipment repair, parts', 'Production Area', 'Tool storage, welding area'],
            ['Office & Admin', '800', 'Offices, conference, reception', 'Main entrance', 'HVAC, IT infrastructure'],
            ['Employee Facilities', '300', 'Locker rooms, break room', 'Office Area', 'Ventilation, plumbing'],
            ['Utility Room', '400', 'Electrical, compressed air', 'Production Area', 'Ventilation, equipment access']
        ]
        
        self.add_table(layout_data, [1.4, 1.0, 1.4, 1.2, 1.0], title="Facility Zone Layout & Requirements")
        
        self.add_heading2("Material Flow & Process Layout")
        
        layout_text = """
        <b>Material Flow Design Principles:</b>
        <br/>
        • Linear flow from raw material receiving to finished goods shipping
        <br/>
        • Minimal material handling and transportation distances
        <br/>
        • Segregation of raw materials to prevent cross-contamination
        <br/>
        • Efficient workflow with minimal operator travel
        <br/>
        • Clear pathways for maintenance and emergency access
        <br/>
        
        <b>Production Area Layout:</b>
        <br/>
        • Sequential arrangement of process equipment
        <br/>
        • Overhead crane coverage for equipment maintenance
        <br/>
        • Adequate space for equipment access and maintenance
        <br/>
        • Dust collection ductwork and utility distribution
        <br/>
        • Emergency exits and safety shower/eyewash stations
        <br/>
        
        <b>Storage Area Design:</b>
        <br/>
        • Raw material silos with individual discharge gates
        <br/>
        • Segregated storage bays for different materials
        <br/>
        • FIFO (first-in, first-out) inventory rotation
        <br/>
        • Climate-controlled finished goods storage
        <br/>
        • Secure storage for valuable alloy materials
        <br/>
        
        <b>Traffic Flow & Circulation:</b>
        <br/>
        • Separate truck and employee entrances
        <br/>
        • One-way circulation to minimize vehicle conflicts
        <br/>
        • Loading docks positioned for efficient material flow
        <br/>
        • Emergency vehicle access to all areas
        <br/>
        • Visitor parking separated from operational areas
        """
        
        self.add_body_text(layout_text)
        
        # Building specifications table
        building_specs_data = [
            ['Building Component', 'Specification', 'Requirement', 'Design Standard'],
            ['Foundation', 'Reinforced concrete slab', '6-inch thickness, vapor barrier', 'Heavy equipment loads'],
            ['Structure', 'Pre-engineered steel building', '26-foot clear height', 'Crane loads, wind/snow'],
            ['Roof', 'Standing seam metal', 'Insulated, R-30 minimum', 'Weather-tight, low maintenance'],
            ['Walls', 'Insulated metal panels', 'R-19 insulation, vapor barrier', 'Energy efficient, durable'],
            ['Doors', 'Overhead doors (truck height)', '12x14 foot truck doors', 'Insulated, high-cycle'],
            ['Windows', 'Insulated glazing', 'Office areas, natural light', 'Energy efficient, security'],
            ['HVAC', 'Gas-fired unit heaters', 'Production area heating', 'Zoned control, energy efficient'],
            ['Lighting', 'LED high bay fixtures', '50+ foot-candle levels', 'Energy efficient, long life']
        ]
        
        self.add_table(building_specs_data, [1.3, 1.3, 1.6, 1.8], title="Building Design Specifications")
        
        self.add_spacer()
    
    def _add_environmental_considerations(self):
        """Add environmental considerations section"""
        self.add_heading1("Environmental Impact & Mitigation")
        
        # Environmental impact table
        environmental_data = [
            ['Environmental Aspect', 'Potential Impact', 'Mitigation Measures', 'Monitoring Requirements'],
            ['Air Emissions', 'Dust from material handling', 'Baghouse filtration, enclosures', 'Stack testing, opacity monitoring'],
            ['Noise', 'Equipment operation', 'Sound barriers, enclosures', 'Periodic noise measurements'],
            ['Water Usage', 'Process and cooling water', 'Recycling, efficient usage', 'Flow monitoring, usage tracking'],
            ['Wastewater', 'Process water discharge', 'Treatment, municipal connection', 'Discharge monitoring, pH control'],
            ['Stormwater', 'Site runoff', 'Retention pond, oil separation', 'Water quality monitoring'],
            ['Waste Generation', 'Packaging, maintenance waste', 'Recycling, proper disposal', 'Waste tracking, manifests'],
            ['Soil Protection', 'Spill prevention', 'Containment, cleanup procedures', 'Spill reporting, soil testing'],
            ['Visual Impact', 'Industrial appearance', 'Landscaping, screening', 'Maintenance of landscaping']
        ]
        
        self.add_table(environmental_data, [1.2, 1.4, 1.6, 1.8], title="Environmental Impact Assessment")
        
        self.add_heading2("Sustainability Measures")
        
        sustainability_text = """
        <b>Energy Efficiency:</b>
        <br/>
        • High-efficiency equipment and motors with variable frequency drives
        <br/>
        • LED lighting throughout facility with occupancy and daylight sensors
        <br/>
        • Building insulation exceeding minimum code requirements
        <br/>
        • Heat recovery from dryer exhaust for space heating
        <br/>
        • Energy monitoring and management systems
        <br/>
        
        <b>Water Conservation:</b>
        <br/>
        • Closed-loop cooling water systems with minimal makeup
        <br/>
        • Rainwater collection for non-potable uses
        <br/>
        • Low-flow fixtures and water-efficient equipment
        <br/>
        • Process water recycling and reuse
        <br/>
        • Native landscaping requiring minimal irrigation
        <br/>
        
        <b>Waste Minimization:</b>
        <br/>
        • Material recycling programs for packaging and scrap
        <br/>
        • Bulk material handling to reduce packaging waste
        <br/>
        • Reusable packaging systems with customers
        <br/>
        • Equipment maintenance to maximize useful life
        <br/>
        • Employee training on waste reduction practices
        <br/>
        
        <b>Environmental Management:</b>
        <br/>
        • Environmental management system implementation
        <br/>
        • Regular environmental audits and performance monitoring
        <br/>
        • Continuous improvement in environmental performance
        <br/>
        • Community engagement and transparency
        <br/>
        • Compliance with or exceeding regulatory requirements
        <br/>
        
        <b>Future Sustainability Initiatives:</b>
        <br/>
        • Solar panel installation for renewable energy
        <br/>
        • Electric vehicle charging stations for employees
        <br/>
        • Carbon footprint assessment and reduction programs
        <br/>
        • Green building certification consideration (LEED)
        <br/>
        • Partnership with local environmental organizations
        """
        
        self.add_body_text(sustainability_text)
        self.add_spacer()
    
    def _add_site_selection_criteria(self):
        """Add site selection criteria section"""
        self.add_heading1("Site Selection Criteria & Evaluation")
        
        # Site evaluation criteria
        criteria_data = [
            ['Evaluation Criteria', 'Weight (%)', 'Scoring Method', 'Key Factors', 'Decision Impact'],
            ['Location & Access', '25%', '1-10 scale', 'Highway access, customer proximity', 'Transportation costs, delivery times'],
            ['Land Cost & Availability', '20%', 'Cost per acre', 'Purchase/lease cost, expansion land', 'Capital investment, future flexibility'],
            ['Utilities Availability', '20%', 'Capacity vs. need', 'Electrical, gas, water capacity', 'Infrastructure investment, reliability'],
            ['Regulatory Environment', '15%', 'Permit complexity', 'Zoning approval, permit timeline', 'Project schedule, compliance cost'],
            ['Workforce Access', '10%', 'Labor availability', 'Skilled workforce, unemployment rate', 'Recruitment cost, training needs'],
            ['Community Support', '5%', 'Municipal cooperation', 'Economic development support', 'Permit efficiency, tax incentives'],
            ['Environmental Factors', '5%', 'Impact complexity', 'Environmental constraints', 'Permit cost, mitigation requirements']
        ]
        
        self.add_table(criteria_data, [1.4, 0.8, 1.2, 1.4, 1.2], title="Site Selection Evaluation Criteria")
        
        self.add_heading2("Preferred Site Characteristics")
        
        preferred_text = """
        <b>Ideal Site Profile:</b>
        <br/>
        
        <b>Location:</b>
        <br/>
        • Within 15 minutes of Highway 2 corridor
        <br/>
        • Airdrie or Calgary industrial area
        <br/>
        • Proximity to skilled workforce and suppliers
        <br/>
        • Access to CN or CP rail lines (preferred)
        <br/>
        • Municipal support for industrial development
        <br/>
        
        <b>Physical Characteristics:</b>
        <br/>
        • 10-15 acres with expansion potential
        <br/>
        • Level terrain requiring minimal site preparation
        <br/>
        • Good soil conditions for heavy construction
        <br/>
        • No environmental contamination or restrictions
        <br/>
        • Attractive industrial setting with landscaping potential
        <br/>
        
        <b>Infrastructure Readiness:</b>
        <br/>
        • Utilities available at property boundary
        <br/>
        • Road access adequate for truck traffic
        <br/>
        • Municipal services (fire, police, utilities) available
        <br/>
        • Telecommunications infrastructure in place
        <br/>
        • Waste management and recycling services
        <br/>
        
        <b>Economic Factors:</b>
        <br/>
        • Competitive land cost (purchase or lease)
        <br/>
        • Municipal tax rates and incentive programs
        <br/>
        • Utility rates competitive with regional standards
        <br/>
        • Minimal infrastructure investment required
        <br/>
        • Property appreciation potential
        <br/>
        
        <b>Regulatory Advantages:</b>
        <br/>
        • Appropriate industrial zoning in place
        <br/>
        • Streamlined permit processes
        <br/>
        • Municipal support for job creation
        <br/>
        • No significant environmental constraints
        <br/>
        • Established industrial area with precedent uses
        <br/>
        
        <b>Strategic Considerations:</b>
        FluxGen's site selection will balance immediate operational needs with long-term strategic objectives. 
        The chosen location must support efficient operations, provide growth flexibility, and position 
        the company competitively in the Western Canadian market.
        <br/>
        Key success factors include minimizing transportation costs, ensuring reliable utility supply, 
        maintaining regulatory compliance, and building strong community relationships.
        """
        
        self.add_body_text(preferred_text)
        self.add_spacer()
    
    def generate(self) -> Path:
        """Generate the Site Requirements PDF"""
        self.story = []  # Reset story
        self.build_content()
        
        filename = f"fluxgen_site_requirements_{self._get_timestamp()}"
        return self.generate_document(filename, "FluxGen Industries - Site Requirements")
    
    def _get_timestamp(self) -> str:
        """Get timestamp for filename"""
        from datetime import datetime
        return datetime.now().strftime('%Y%m%d_%H%M%S')