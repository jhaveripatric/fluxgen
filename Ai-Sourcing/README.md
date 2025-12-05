# FluxGen AI Supplier Sourcing System

Automated supplier discovery, contact management, pricing tracking, and outreach system powered by Claude AI.

## Quick Start

```bash
cd /path/to/Ai-Sourcing

# Install dependencies
pip install -r requirements.txt

# Initialize database schema
python cli.py init

# Check system status
python cli.py status

# Run first search (dry-run)
python cli.py search --dry-run
```

## Configuration

Copy `.env.template` to `.env` and add your API key:

```bash
ANTHROPIC_API_KEY=sk-ant-api03-your-key-here
```

## Unified CLI

All operations through single entry point:

```bash
# Search for suppliers
python cli.py search --batch-size 5
python cli.py search --dry-run

# Score suppliers
python cli.py score --summary
python cli.py score --supplier-id 1

# Manage contacts
python cli.py contacts --stats
python cli.py contacts --status Prospect --dry-run

# Track pricing
python cli.py pricing market
python cli.py pricing --compare --product "Silica Sand"
python cli.py pricing --alerts

# Manage outreach
python cli.py outreach --templates
python cli.py outreach --preview --template direct_fluxgen
python cli.py outreach --stats

# Dashboard
python cli.py dashboard
python cli.py dashboard --full
python cli.py dashboard --export report.json

# Reports
python cli.py report --csv
python cli.py report --summary
```

## Modules

### 1. Supplier Search (`daily_supplier_search.py`)
- Automated supplier discovery using Claude AI with web search
- Processes items from research queue
- Extracts company info (name, website, location, contacts)
- Saves to SQLite database

```bash
python daily_supplier_search.py --batch-size 5
python daily_supplier_search.py --dry-run
```

### 2. Supplier Scoring (`supplier_scorer.py`)
- Multi-factor scoring (0-100 scale)
- Weights: location, website quality, certifications, contact info
- Grade assignment (A+ to F)

```bash
python supplier_scorer.py --supplier-id 1
python supplier_scorer.py --summary
```

### 3. Contact Manager (`contact_manager.py`)
- Extract contacts from supplier websites
- AI-powered contact extraction
- Store emails, phones, LinkedIn URLs
- Track verification status

```bash
python contact_manager.py --stats
python contact_manager.py --supplier-id 1
python contact_manager.py --status Prospect --batch-size 10
```

### 4. Pricing Tracker (`pricing_tracker.py`)
- Log quotes from suppliers
- Calculate market price ranges (min/avg/max)
- Price change alerts
- Supplier comparison

```bash
python pricing_tracker.py market
python pricing_tracker.py compare "Silica Sand"
python pricing_tracker.py alerts --threshold 10
python pricing_tracker.py add --supplier-id 1 --product "Silica" --price 150
```

### 5. Outreach Engine (`outreach_engine.py`)
- Email templates for different personas
- AI-generated custom emails
- Track outreach status
- Follow-up management

```bash
python outreach_engine.py templates
python outreach_engine.py preview direct_fluxgen --supplier-id 1
python outreach_engine.py stats
python outreach_engine.py followups
```

### 6. Dashboard (`dashboard.py`)
- Supplier database overview
- Pricing analytics
- Outreach statistics
- Geographic distribution

```bash
python dashboard.py --summary
python dashboard.py --full
python dashboard.py --export data.json
```

## Database Schema

Main tables:
- `suppliers` - Supplier companies
- `supplier_contacts` - Contact persons
- `price_quotes` - Pricing quotes
- `outreach_log` - Outreach history
- `trade_shows` - Industry events
- `research_queue` - Items to research
- `supplier_search_history` - Search logs

Initialize/update schema:
```bash
python db_utils.py
# or
python cli.py init
```

## Personas

Different identities for market research:

| Persona | Use Case |
|---------|----------|
| `fluxgen` | Direct supplier inquiry |
| `fab_shop` | Fabrication shop perspective |
| `distributor` | Distribution partnership |
| `researcher` | Market research |

## Templates

Built-in email templates:
- `fab_shop_inquiry` - Fab shop product inquiry
- `distributor_inquiry` - Distribution partnership
- `direct_fluxgen` - Direct FluxGen inquiry
- `follow_up` - Follow-up email
- `quote_request` - Formal RFQ

## Testing

```bash
cd tests
python test_modules.py
```

## File Structure

```
Ai-Sourcing/
├── cli.py                 # Unified CLI entry point
├── config.py              # Configuration and constants
├── db_utils.py            # Database utilities
├── schema_update.sql      # Schema definitions
├── daily_supplier_search.py
├── supplier_scorer.py
├── contact_manager.py
├── pricing_tracker.py
├── outreach_engine.py
├── dashboard.py
├── generate_reports.py
├── test_setup.py
├── requirements.txt
├── .env                   # API keys (not in git)
├── .env.template
├── tests/
│   └── test_modules.py
└── README.md
```

## Dry Run Mode

All modules support `--dry-run` flag to preview actions without database changes:

```bash
python cli.py search --dry-run
python cli.py contacts --dry-run
python pricing_tracker.py add --supplier-id 1 --product X --price 100 --dry-run
```
