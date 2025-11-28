# FluxGen AI Supplier Sourcing System

Automated supplier discovery and ranking system powered by Claude AI with real web search capabilities.

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd /Users/pratikjhaveri/FluxGen/Ai-Sourcing
pip3 install -r requirements.txt
```

### 2. Configure API Key

1. Get your Anthropic API key from: https://console.anthropic.com/
2. Edit the `.env` file:
   ```bash
   nano .env
   ```
3. Add your API key:
   ```
   ANTHROPIC_API_KEY=sk-ant-api03-your-key-here
   ```
4. Save and exit (Ctrl+X, then Y, then Enter)

### 3. Test Your Setup

```bash
python3 test_setup.py
```

This will verify:
- ✅ API key is configured
- ✅ Dependencies are installed
- ✅ Database is accessible
- ✅ API connection works

### 4. Run Your First Search

```bash
# Search for one item
python3 daily_supplier_search.py --batch-size 1

# Or test with dry-run mode first
python3 daily_supplier_search.py --batch-size 1 --dry-run
```

## 📋 Usage

### Search Commands

```bash
# Process 5 items from the research queue
python3 daily_supplier_search.py --batch-size 5

# Preview what will be searched (no API calls)
python3 daily_supplier_search.py --batch-size 5 --dry-run

# Search for specific item
python3 daily_supplier_search.py --item "Solar Panel"
```

### Score Suppliers

```bash
# Score a specific supplier
python3 supplier_scorer.py --supplier-id 1

# Score all unscored suppliers
python3 supplier_scorer.py --all
```

### Generate Reports

```bash
# Generate weekly supplier report
python3 generate_reports.py

# Generate custom date range report
python3 generate_reports.py --days 14
```

## 🤖 How It Works

1. **Daily Search (`daily_supplier_search.py`)**
   - Reads items from `research_queue` table
   - Uses Claude AI to search the web for suppliers
   - Extracts company information (name, website, location)
   - Saves suppliers to the `suppliers` table
   - Logs all searches in `supplier_search_history`

2. **Supplier Scoring (`supplier_scorer.py`)**
   - Uses AI to evaluate supplier quality
   - Scores based on: reliability, capabilities, pricing
   - Updates supplier records with scores and analysis

3. **Report Generation (`generate_reports.py`)**
   - Creates summaries of newly found suppliers
   - Groups by item type and priority
   - Exports to CSV/PDF for review

## 🔧 Configuration

### Environment Variables (.env)

```bash
# Required
ANTHROPIC_API_KEY=sk-ant-api03-...

# Optional
DATABASE_PATH=/Users/pratikjhaveri/FluxGen/data/fluxgen.db
```

### Search Parameters

Edit in `daily_supplier_search.py`:
- `max_results`: Maximum search results per query (default: 10)
- `batch_size`: Items to process per run (default: 5)
- `research_frequency_days`: Days between searches (default: 30)

## 📊 Database Tables

The system uses three main tables:

1. **research_queue**: Items that need supplier research
2. **suppliers**: All found suppliers
3. **supplier_search_history**: Log of all searches performed

## ⚙️ Automation (Optional)

To run automatically every day:

```bash
crontab -e
```

Add these lines:

```bash
# Run supplier search daily at 2 AM
0 2 * * * cd /Users/pratikjhaveri/FluxGen/Ai-Sourcing && /usr/bin/python3 daily_supplier_search.py

# Generate reports daily at 8 AM
0 8 * * * cd /Users/pratikjhaveri/FluxGen/Ai-Sourcing && /usr/bin/python3 generate_reports.py
```

## 🐛 Troubleshooting

### "ANTHROPIC_API_KEY not found"
- Make sure `.env` file exists in the Ai-Sourcing directory
- Check that the API key is set correctly in `.env`
- Key should start with `sk-ant-`

### "supplier_type CHECK constraint failed"
- This has been fixed in the latest version
- Valid values: 'Local', 'Regional', 'Import', 'Distributor'

### "Database not found"
- Verify database path in script
- Check that `/Users/pratikjhaveri/FluxGen/data/fluxgen.db` exists

### Search returns no results
- Check your API key is valid
- Verify internet connection
- Try with `--dry-run` to see what would be searched

## 📝 Example Output

```
################################################################################
# FluxGen Automated Supplier Search
# 2025-11-26 10:00:00
################################################################################

📋 Found 3 items to research

================================================================================
🔎 SEARCHING: Rotary Dryer/Calciner (Primary) (equipment)
   Priority: 10 | Target: 10 suppliers
   Already found: 0 suppliers
================================================================================

📝 Query: Rotary Dryer/Calciner (Primary) suppliers manufacturers industrial
🔍 Searching: Rotary Dryer/Calciner (Primary) suppliers manufacturers industrial
   ✅ Found 8 results
   ✅ Saved supplier: FEECO International (ID: 45)
   ✅ Saved supplier: Metso Outotec (ID: 46)
   ...

✅ Completed: Found 8 results, saved 7 new suppliers
```

## 📞 Support

For issues or questions, check the database logs:

```bash
sqlite3 /Users/pratikjhaveri/FluxGen/data/fluxgen.db
> SELECT * FROM supplier_search_history ORDER BY search_date DESC LIMIT 5;
```
