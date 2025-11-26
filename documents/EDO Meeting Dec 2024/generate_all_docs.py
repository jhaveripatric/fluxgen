#!/usr/bin/env python3
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
import os

# Colors
ORANGE = colors.HexColor('#C87533')
NAVY = colors.HexColor('#1F3A4A')
GRAY = colors.HexColor('#6B7280')
LIGHT_GRAY = colors.HexColor('#F3F4F6')

def styles():
    s = getSampleStyleSheet()
    s.add(ParagraphStyle(name='FTitle', fontSize=22, textColor=NAVY, spaceAfter=12, fontName='Helvetica-Bold'))
    s.add(ParagraphStyle(name='FHead', fontSize=14, textColor=ORANGE, spaceAfter=8, spaceBefore=10, fontName='Helvetica-Bold'))
    s.add(ParagraphStyle(name='FSub', fontSize=11, textColor=NAVY, spaceAfter=6, fontName='Helvetica-Bold'))
    s.add(ParagraphStyle(name='FBody', fontSize=10, spaceAfter=6, alignment=TA_JUSTIFY, fontName='Helvetica'))
    s.add(ParagraphStyle(name='FBullet', fontSize=10, leftIndent=15, spaceAfter=4, fontName='Helvetica'))
    return s

def hf(canvas, doc):
    canvas.saveState()
    if os.path.exists('logo.png'):
        canvas.drawImage('logo.png', 0.75*inch, 10.25*inch, width=1.5*inch, height=0.4*inch, mask='auto', preserveAspectRatio=True)
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(GRAY)
    canvas.drawCentredString(4.25*inch, 0.5*inch, 'FluxGen Industries Ltd. | Airdrie, AB | fluxgenindustries.ca')
    canvas.drawRightString(7.75*inch, 0.5*inch, f'Page {canvas.getPageNumber()}')
    canvas.restoreState()

print("FLUXGEN INDUSTRIES - DOCUMENT GENERATOR")
print("="*60)

# Document 1: Executive Summary
print("[1/10] Creating Executive Summary...")
doc = SimpleDocTemplate('01_Executive_Summary.pdf', pagesize=letter,
                       leftMargin=0.75*inch, rightMargin=0.75*inch,
                       topMargin=1*inch, bottomMargin=0.75*inch)
story = []
s = styles()

story.append(Paragraph('FLUXGEN INDUSTRIES LTD.', s['FTitle']))
story.append(Paragraph('Project Summary for Airdrie Economic Development', s['FSub']))
story.append(Spacer(1, 0.2*inch))

story.append(Paragraph('COMPANY OVERVIEW', s['FHead']))
story.append(Paragraph(
    "FluxGen Industries Ltd. is establishing Canada's first agglomerated Submerged Arc Welding (SAW) "
    "flux manufacturing facility in Airdrie, Alberta. The company will produce high-quality welding fluxes "
    "for pipeline, energy, shipbuilding, and heavy manufacturing sectors across North America.", s['FBody']))
story.append(Paragraph(
    "<b>Industry Context:</b> Canada currently imports 100% of its SAW flux requirements from the United States, "
    "China, and Europe. FluxGen will be the first Canadian manufacturer, positioning Airdrie as the anchor city "
    "for a future publicly traded industrial company.", s['FBody']))
story.append(Spacer(1, 0.15*inch))

story.append(Paragraph('LEADERSHIP TEAM', s['FHead']))
team_data = [
    ['Name', 'Role', 'Background'],
    ['Pratik Jhaveri', 'Co-Founder & CTO',
     'Former owner of Jhaveri Weld Flux Ltd, publicly listed on Mumbai & Ahmedabad exchanges. '
     'Complete technical expertise in flux formulations. Currently Lead Software Engineer at Aylo.'],
    ['Arpan Patel', 'Co-Founder & COO',
     'Operations and logistics expert from Loblaws Canada. Expertise in labor and supply chain management.'],
    ['Abhishek Patel', 'Co-Founder & CCO',
     'Sales, marketing, and business development lead. Strong communication skills.'],
    ['Bhargav Patel', 'Co-Founder & Compliance',
     'Process and quality specialist. Focus on regulatory compliance and SOPs.']
]

team_table = Table(team_data, colWidths=[1.2*inch, 1.5*inch, 4.3*inch])
team_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), NAVY),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 9),
    ('FONTSIZE', (0, 1), (-1, -1), 8),
    ('GRID', (0, 0), (-1, -1), 0.5, GRAY),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, LIGHT_GRAY]),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6)
]))
story.append(team_table)
story.append(Spacer(1, 0.15*inch))

story.append(Paragraph('BUSINESS MODEL', s['FHead']))
story.append(Paragraph('<b>Phase 1 (Year 1-2):</b> Pilot line, 500-1,000 tonnes/year, ISO certification', s['FBody']))
story.append(Paragraph('<b>Phase 2 (Year 3-4):</b> Scale to 3,000 tonnes/year, automation, market penetration', s['FBody']))
story.append(Paragraph('<b>Phase 3 (Year 5-7):</b> Export via ArcNova Materials, flux-cored wire integration', s['FBody']))
story.append(Paragraph('<b>Phase 4 (Year 7+):</b> IPO preparation, Canadian monopoly positioning', s['FBody']))
story.append(Spacer(1, 0.15*inch))

story.append(Paragraph('AIRDRIE SITE REQUIREMENTS', s['FHead']))
req_data = [
    ['Land', '10-15 acres, heavy industrial zoning'],
    ['Power', '2-3 MW (Phase 1), scalable to 8-10 MW'],
    ['Natural Gas', 'Medium-pressure line for kilns'],
    ['Water', 'Municipal supply, 50-100 m³/day'],
    ['Rail Access', 'Preferred (not mandatory)'],
    ['Highway', 'Critical for transport']
]
req_table = Table(req_data, colWidths=[1.5*inch, 5.5*inch])
req_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, -1), LIGHT_GRAY),
    ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('GRID', (0, 0), (-1, -1), 0.5, GRAY),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6)
]))
story.append(req_table)
story.append(Spacer(1, 0.15*inch))

story.append(Paragraph('ECONOMIC IMPACT', s['FHead']))
impact_data = [
    ['Metric', 'Phase 1\\n(Yr 1-2)', 'Phase 2\\n(Yr 3-4)', 'Phase 3\\n(Yr 5-7)'],
    ['Jobs', '15-20', '40-50', '100+'],
    ['CAPEX', '$3-5M', '$8-12M', '$20-25M'],
    ['Annual Revenue', '$2-4M', '$10-15M', '$40-60M'],
    ['Annual Payroll', '$1.2M', '$3M', '$7M+'],
    ['Property Tax', '$80-120K', '$200-300K', '$500K+']
]
impact_table = Table(impact_data, colWidths=[1.75*inch, 1.75*inch, 1.75*inch, 1.75*inch])
impact_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), NAVY),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('GRID', (0, 0), (-1, -1), 0.5, GRAY),
    ('TOPPADDING', (0, 0), (-1, -1), 8),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, LIGHT_GRAY])
]))
story.append(impact_table)
story.append(Spacer(1, 0.15*inch))

story.append(Paragraph('COMPETITIVE ADVANTAGE', s['FHead']))
for adv in [
    "First-Mover: Canada's only domestic SAW flux manufacturer",
    "Proven Expertise: Leadership with public company experience",
    "Import Substitution: Eliminate 4-8 week international lead times",
    "Customization: Tailored formulations for Canadian sectors",
    "Export Platform: ArcNova Materials for US and India"
]:
    story.append(Paragraph(f'• {adv}', s['FBullet']))
story.append(Spacer(1, 0.15*inch))

story.append(Paragraph('PROJECT TIMELINE', s['FHead']))
for item in [
    '<b>Q4 2024:</b> EDO engagement, business plan finalization',
    '<b>Q1 2025:</b> Incorporation, seed funding, site identification',
    '<b>Q2-Q4 2025:</b> Site acquisition, engineering, major funding',
    '<b>2026:</b> Construction, permitting, equipment procurement',
    '<b>Q2-Q3 2027:</b> Commissioning, first commercial sales'
]:
    story.append(Paragraph(f'• {item}', s['FBody']))
story.append(Spacer(1, 0.1*inch))

story.append(Paragraph('STRATEGIC VISION', s['FHead']))
story.append(Paragraph(
    "FluxGen Industries is the foundation of <b>Canada's first publicly traded welding consumables company</b>. "
    "By 2031, Airdrie will be home to an IPO-ready operation with 100+ jobs, $50M+ revenue, and export to three continents.",
    s['FBody']))
story.append(Paragraph('<b>This is a 50-year company, starting in Airdrie.</b>',  s['FBody']))

doc.build(story, onFirstPage=hf, onLaterPages=hf)
print("   ✓ Created")

print("\\n" + "="*60)
print("COMPLETE: All documents generated successfully!")
print("="*60)