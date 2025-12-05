# Operations Toolkit

PDF document generation system for FluxGen Industries.

## Stack
Python 3.10+, Flask, SQLite, ReportLab

## Setup
```bash
source venv/bin/activate
pip install -r requirements.txt
python app/app.py  # :5000
```

## Database
SQLite: `data/fluxgen.db`

Key tables: company_info, team_members, investment_capex, production_targets, alloys_catalog

## Document Types
Executive Summary, Business Plan, Financial Projections, Market Analysis, Technical Specs, Team Bios, Site Requirements, Pitch Deck

## Rules
- Always use venv
- ReportLab Paragraph for text wrapping in tables
- Brand colors in config.py
- Test with `python test_pdf_generation.py`
