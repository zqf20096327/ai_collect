# API Scraper

A desktop GUI application that automates the discovery and validation of API keys for AI/LLM services and cloud platforms by searching GitHub commits for accidentally leaked credentials.

## Screenshots

![Main window with results](1.PNG)

![Keys table and detailed view](2.PNG)

## Supported Services

**LLM Providers:**
OpenAI, Anthropic, Cohere, Google Gemini, Mistral, DeepSeek, Groq, Together AI, HuggingFace

**Cloud Platforms:**
AWS, Azure, GCP

Custom regex patterns are also supported for services not in the predefined list.

## Features

- Multi-service GitHub commit search with rate-limit handling
- Concurrent diff download and key extraction (configurable thread counts)
- Validation of discovered keys against each service's API endpoints
- Balance checking for supported services (DeepSeek)
- Deduplication across commits with source metadata tracking
- Detailed results table with filtering, searching, and color-coded status
- Export to TXT, CSV, and JSON formats
- Auto-export on completion
- Import previously exported results for browsing
- Persistent configuration (token, services, thread counts, etc.)
- File and console logging for debugging

## Requirements

- Python 3.9+
- PyQt5 >= 5.15
- requests >= 2.28

## Installation

```bash
git clone https://github.com/Sewer2K/apiscraper.git
cd apiscraper
pip install -r requirements.txt
```

## Usage

### GUI Mode

```bash
python -m apiscraper.main
```

1. Enter a GitHub personal access token (optional but recommended for higher rate limits)
2. Select the services you want to scan for
3. Configure search settings (pages, thread counts, query template)
4. Click "Start Scraping" to begin
5. Browse results in the Summary, Keys, and Detailed View tabs
6. Export results via File > Export or the Export toolbar button

### Console Test Mode

```bash
python run_console_test.py
```

This runs the full pipeline with console output and saves a detailed log to `~/.apiscraper/logs/`.

### Backend Test Suite

```bash
python run_test.py
```

## Configuration

Settings are persisted to `~/.apiscraper/apiscraper_config.json` and include:

| Setting | Default | Description |
|---------|---------|-------------|
| `github_token` | (empty) | GitHub personal access token |
| `selected_services` | OpenAI, DeepSeek, Anthropic | Active services |
| `max_pages` | 20 | Pages of search results |
| `download_threads` | 10 | Concurrent diff downloads |
| `validation_threads` | 5 | Concurrent key validations |
| `max_keys_per_diff` | 200 | Key extraction limit per diff |
| `search_query_template` | `remove {service}_api_key` | GitHub search query |
| `auto_export` | false | Auto-export on completion |
| `auto_export_format` | json | Auto-export format |
| `auto_export_dir` | (empty) | Auto-export directory |

## Project Structure

```
apiscraper/
├── __init__.py
├── main.py                  # Entry point
├── backend/
│   ├── __init__.py
│   ├── services.py          # Service definitions (patterns, endpoints)
│   ├── github_searcher.py   # GitHub commit search
│   ├── diff_downloader.py   # Concurrent diff download
│   ├── key_extractor.py     # Regex-based key extraction
│   ├── key_validator.py     # Key validation and balance checking
│   ├── result_manager.py    # Thread-safe results storage
│   ├── exporter.py          # TXT/CSV/JSON export and import
│   └── config_manager.py    # Settings persistence
├── gui/
│   ├── __init__.py
│   └── main_window.py       # PyQt5 GUI
└── resources/
```

## Logs

All logs are saved to `~/.apiscraper/logs/` with timestamps in the filename. Both detailed (DEBUG level) and console (INFO level) output are captured.

## Security

- API keys are masked in the UI (first 6 + last 4 characters shown)
- The GitHub token is stored in the config file as plaintext -- restrict access to `~/.apiscraper/` if needed
- Exported files contain unmasked keys -- handle with care

## License

This project is provided for educational and security research purposes only. Use responsibly and only on repositories you own or have permission to test.
