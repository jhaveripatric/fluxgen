from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY


def create_executive_summary():
    filename = "./FluxGen_Executive_Summary_EDO.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter,
                            topMargin=0.4 * inch, bottomMargin=0.4 * inch,
                            leftMargin=0.65 * inch, rightMargin=0.65 * inch)

    story = []
    styles = getSampleStyleSheet()

    # Custom styles - more compact
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=14,
        textColor=colors.HexColor('#2C3E50'),
        spaceAfter=4,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#B87333'),
        spaceAfter=8,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=10,
        textColor=colors.HexColor('#2C3E50'),
        spaceAfter=4,
        spaceBefore=6,
        fontName='Helvetica-Bold'
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=8.5,
        textColor=colors.HexColor('#333333'),
        spaceAfter=3,
        alignment=TA_JUSTIFY,
        leading=10
    )

    # Header
    story.append(Paragraph("FLUXGEN INDUSTRIES LTD.", title_style))
    story.append(Paragraph("Partnership Proposal to City of Airdrie Economic Development", subtitle_style))
    story.append(Paragraph("<i>Canada's First SAW Flux & Alloy Manufacturer | Airdrie, Alberta</i>",
                           ParagraphStyle('Tagline', parent=body_style, fontSize=8.5, alignment=TA_CENTER,
                                          textColor=colors.HexColor('#666666'))))
    story.append(Spacer(1, 0.08 * inch))

    # Market Opportunity
    story.append(Paragraph("THE MARKET OPPORTUNITY", heading_style))
    story.append(Paragraph(
        "Canada imports 100% of its Submerged Arc Welding (SAW) flux—a critical consumable for pipeline welding, "
        "shipbuilding, and heavy equipment manufacturing. With <b>$33 million in annual imports (11,000+ tonnes)</b>, "
        "Canada has zero domestic manufacturers, creating supply chain vulnerability and currency risk. "
        "FluxGen will be <b>Canada's first SAW flux manufacturer</b>, capturing domestic demand while positioning for "
        "U.S. and international exports through our subsidiary, <b>ArcNova Materials</b>.",
        body_style
    ))
    story.append(Spacer(1, 0.06 * inch))

    # Partnership Request - Compact Table
    story.append(Paragraph("PARTNERSHIP REQUEST FROM CITY OF AIRDRIE", heading_style))
    partnership_data = [
        ['WHAT WE REQUEST', 'WHAT AIRDRIE RECEIVES'],
        ['• 10-15 acres industrial land', '• $312M economic impact (7 years)'],
        ['• Municipal support letter', '• 40+ jobs ($55K-$75K wages)'],
        ['• Utility connection guidance', '• $300K-$400K property tax revenue'],
        ['• Collaborative permitting', '• National prestige (Canada\'s first)']
    ]

    partnership_table = Table(partnership_data, colWidths=[3.4 * inch, 3.4 * inch])
    partnership_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2C3E50')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8.5),
        ('FONTSIZE', (0, 1), (-1, -1), 7.5),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 5),
        ('TOPPADDING', (0, 1), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 4),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CCCCCC')),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F8F9FA')),
    ]))
    story.append(partnership_table)
    story.append(Spacer(1, 0.06 * inch))

    # Why FluxGen Will Succeed - More Compact
    story.append(Paragraph("WHY FLUXGEN WILL SUCCEED", heading_style))
    story.append(Paragraph(
        "<b>1. Proven Technology:</b> 40+ years commercial expertise (Jhaveri Weldflux Ltd., publicly traded BSE/ASE). "
        "Production-ready formulations—NOT R&D. "
        "<b>2. Guaranteed Demand:</b> 100% import dependency = 11,000 tonnes/year existing customer base. "
        "<b>3. Experienced Team:</b> Four equal partners with complementary skills—technical, operations, sales, compliance. "
        "<b>4. Phased Growth:</b> 800 tonnes (Y1-2) → 3,000 tonnes (Y3-4) → 6,000 tonnes + exports (Y5-7).",
        body_style
    ))
    story.append(Spacer(1, 0.06 * inch))

    # Alignment - Condensed
    story.append(Paragraph("ALIGNMENT WITH AIRDRIE'S ECONOMIC STRATEGY 2018-2028", heading_style))
    story.append(Paragraph(
        "FluxGen accelerates Airdrie's priorities: <b>The Place to Be</b> (skilled professionals, above-average wages), "
        "<b>Right for Business</b> (shifting tax base to industrial with $9.17M Phase 1 investment), "
        "<b>A Connected Community</b> (Calgary Airport proximity for export logistics). We deliver what your strategy already targets.",
        body_style
    ))
    story.append(Spacer(1, 0.06 * inch))

    # Timeline - Compact
    story.append(Paragraph("PROJECT TIMELINE", heading_style))
    timeline_data = [
        ['Dec 2025 - Jan 2026', 'MOU, land commitment, federal grant apps'],
        ['Q2-Q4 2026', 'Site prep, design, permits'],
        ['2027', 'Construction, equipment, AWS certification'],
        ['Q2 2028', 'PRODUCTION START (800 t/yr, 10 jobs, $2.5M revenue)'],
    ]

    timeline_table = Table(timeline_data, colWidths=[1.3 * inch, 5.5 * inch])
    timeline_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('FONTSIZE', (0, 0), (-1, -1), 7.5),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LINEBELOW', (0, 0), (-1, -2), 0.5, colors.HexColor('#DDDDDD')),
    ]))
    story.append(timeline_table)
    story.append(Spacer(1, 0.06 * inch))

    # Key Note - Compact
    story.append(Paragraph(
        "<b>CRITICAL:</b> Land commitment by Jan 2026 enables Q2 2028 production. Delays push timeline back, delaying jobs and tax revenue.",
        ParagraphStyle('KeyNote', parent=body_style, fontSize=7.5, textColor=colors.HexColor('#B87333'),
                       backColor=colors.HexColor('#FFF8F0'), borderPadding=4, borderWidth=1,
                       borderColor=colors.HexColor('#B87333'))
    ))
    story.append(Spacer(1, 0.08 * inch))

    # Leadership Team - Very Compact
    story.append(Paragraph("LEADERSHIP: PROVEN OPERATORS", heading_style))
    story.append(Paragraph(
        "<b>Pratik Jhaveri, CTO:</b> 40+ yrs flux manufacturing (Jhaveri Weldflux, publicly traded). "
        "<b>Arpan Patel, COO:</b> Loblaws logistics. "
        "<b>Abhishek Patel, CCO:</b> B2B sales. "
        "<b>Bhargav Patel, Compliance:</b> Quality systems. Equal partnership (25% each).",
        body_style
    ))
    story.append(Spacer(1, 0.08 * inch))

    # Footer - Compact
    footer_style = ParagraphStyle(
        'Footer',
        parent=body_style,
        fontSize=8.5,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#2C3E50'),
        fontName='Helvetica-Bold'
    )

    story.append(Paragraph("_________________________________________________________________________________________",
                           ParagraphStyle('Line', parent=body_style, alignment=TA_CENTER,
                                          textColor=colors.HexColor('#CCCCCC'), fontSize=6)))
    story.append(Spacer(1, 0.05 * inch))
    story.append(Paragraph(
        "<b>VALUE EXCHANGE:</b> Airdrie invests 10-15 acres ($0 current revenue) → "
        "FluxGen delivers $312M impact + 40 jobs + $400K tax + national prestige",
        footer_style
    ))
    story.append(Spacer(1, 0.05 * inch))

    contact_style = ParagraphStyle(
        'Contact',
        parent=body_style,
        fontSize=8,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#666666')
    )

    story.append(Paragraph(
        "<b>Pratik Jhaveri</b>, Chief Technical Officer | FluxGen Industries Ltd.<br/>"
        "pratik.jhaveri@fluxgenindustries.ca | Airdrie, Alberta<br/>"
        "<i>December 1, 2025 | City of Airdrie Economic Development</i>",
        contact_style
    ))

    # Build PDF
    doc.build(story)
    print(f"✓ Executive summary created: {filename}")


if __name__ == "__main__":
    create_executive_summary()