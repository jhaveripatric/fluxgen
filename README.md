# FluxGen Industries - Document Generation System

A comprehensive document generation system for FluxGen Industries Ltd., designed to create professional PDF documents for business development and investor relations.

## Overview

FluxGen Industries Ltd. is establishing a SAW flux manufacturing facility in Airdrie, Alberta. This system generates 8 professional documents using data from an existing SQLite database.

## Features

- **8 Professional Documents**: Executive Summary, Business Plan, Financial Projections, Market Analysis, Technical Specifications, Team Biographies, Site Requirements, and Pitch Deck
- **Web-Based Interface**: Clean, modern UI for data editing and document generation
- **Database Integration**: Connects to existing SQLite database with company data
- **PDF Generation**: High-quality PDF documents with proper text wrapping and formatting
- **Responsive Design**: Works on desktop and mobile devices

## Technology Stack

- **Backend**: Flask (Python 3.10+)
- **Database**: SQLite (existing database at `/data/fluxgen.db`)
- **PDF Generation**: ReportLab with custom FluxGen branding
- **Frontend**: HTML5, CSS3 (Tailwind CDN), Vanilla JavaScript
- **Styling**: Tailwind CSS with FluxGen brand colors

## Installation

1. **Clone or download the project**:
   ```bash
   cd /Users/pratikjhaveri/FluxGen
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify database exists**:
   ```bash
   ls -la data/fluxgen.db
   ```

## Usage

1. **Start the Flask application**:
   ```bash
   cd app
   python app.py
   ```

2. **Open your web browser**:
   ```
   http://localhost:5000
   ```

3. **Navigate the application**:
   - **Dashboard**: Overview of data and quick stats
   - **Data Editor**: Edit company information and operational data
   - **Documents**: Generate and download PDF documents

## Document Types

1. **Executive Summary** (1-2 pages)
   - Company overview and key highlights
   - Team summary and business model
   - Economic impact and next steps

2. **Business Plan** (8-12 pages)
   - Comprehensive business strategy
   - Market analysis and operations plan
   - Financial overview and risk analysis

3. **Financial Projections** (4-6 pages)
   - CAPEX and OPEX analysis
   - Revenue forecasts and cash flow
   - Break-even analysis and funding requirements

4. **Market Analysis** (5-7 pages)
   - Industry overview and target markets
   - Competitive landscape and positioning
   - Market size and growth projections

5. **Technical Specifications** (6-8 pages)
   - Manufacturing processes and equipment
   - Quality control procedures
   - Product catalog and certifications

6. **Team Biographies** (2-3 pages)
   - Management team profiles
   - Organizational structure
   - Hiring plans and advisory board

7. **Site Requirements** (3-4 pages)
   - Facility specifications
   - Utilities and infrastructure needs
   - Environmental considerations

8. **Pitch Deck** (12-15 slides)
   - Investor presentation format
   - Problem, solution, and market opportunity
   - Financial highlights and funding ask

## Database Schema

The system connects to an existing SQLite database with the following tables:

- `company_info`: Company details and contact information
- `team_members`: Management team and personnel
- `investment_capex`: Capital expenditure items
- `production_targets`: Production capacity by phase
- `alloys_catalog`: Product specifications
- `funding_programs`: Government funding opportunities
- `certifications_roadmap`: Regulatory compliance timeline
- `brand_assets`: Corporate branding information

## API Endpoints

### Data Management
- `GET /api/data/company` - Get company information
- `PUT /api/data/company` - Update company information
- `GET /api/data/team` - Get team members
- `POST /api/data/team` - Add team member
- `PUT /api/data/team/<id>` - Update team member
- `DELETE /api/data/team/<id>` - Delete team member

### Document Generation
- `POST /api/documents/generate/<doc_name>` - Generate single document
- `POST /api/documents/generate-all` - Generate all documents
- `GET /api/documents/download/<filename>` - Download PDF
- `GET /api/documents/list` - List generated files
- `DELETE /api/documents/<filename>` - Delete PDF

### System Health
- `GET /api/health` - System health check

## Configuration

Key configuration options in `app/config.py`:

- `DATABASE_PATH`: Path to SQLite database
- `OUTPUT_DIR`: Directory for generated PDFs
- `BRAND_COLORS`: FluxGen corporate colors
- `DOCUMENTS`: Document type definitions

## Text Wrapping

All PDF documents use proper text wrapping in tables through ReportLab's Paragraph objects. This ensures professional formatting without text overflow.

## Troubleshooting

### Common Issues

1. **Database Connection Error**:
   - Verify database file exists at `/data/fluxgen.db`
   - Check file permissions

2. **PDF Generation Error**:
   - Ensure ReportLab is installed correctly
   - Check output directory permissions
   - Verify database data completeness

3. **Port Already in Use**:
   - Change port in `app.py` or stop conflicting service
   - Use: `lsof -ti:5000 | xargs kill` to free port 5000

### Logs

Application logs are displayed in the console where Flask is running. Check for errors and warnings.

## Development

### Adding New Documents

1. Create new generator class in `app/generators/`
2. Inherit from `BaseDocumentGenerator`
3. Implement `build_content()` method
4. Add to `GENERATORS` mapping in `document_routes.py`
5. Update frontend documents list

### Customizing Styles

- Modify `BaseDocumentGenerator` for global changes
- Update brand colors in `config.py`
- Customize CSS in `app/static/css/style.css`

## Security Notes

- Database is read/write with input validation
- No authentication implemented (intended for internal use)
- File uploads not supported (security by design)
- Generated files stored locally only

## Performance

- Document generation typically takes 5-15 seconds per document
- Bulk generation processes all 8 documents sequentially
- Generated PDFs are cached until manually deleted

## Support

For technical issues or questions about the FluxGen Industries Document Generation System, please contact the development team.

## License

Proprietary software for FluxGen Industries Ltd. All rights reserved.

---

*Generated by Claude Code for FluxGen Industries Ltd.*