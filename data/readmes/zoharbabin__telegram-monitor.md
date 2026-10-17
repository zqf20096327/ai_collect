# Telegram Monitor

[![CI](https://github.com/zoharbabin/telegram-monitor/actions/workflows/ci.yml/badge.svg)](https://github.com/zoharbabin/telegram-monitor/actions/workflows/ci.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Real-time Telegram channel monitoring with AI-powered intelligence briefings.

Streams messages from configured Telegram channels, translates non-English content, and produces structured intelligence briefings using Claude — all in a multi-pane terminal dashboard.

<img width="2384" height="1375" alt="image" src="https://github.com/user-attachments/assets/1e3d431e-f897-4644-b6dd-8e4625f06880" />


## Features

- **Real-time monitoring** — Live feed from 99+ Telegram channels via Telethon (MTProto user client)
- **AI-powered analysis** — Claude translates, categorizes, and summarizes messages into structured intelligence briefings with urgency assessment, key actors, timeline reconstruction, and source analysis
- **Multi-pane TUI** — Three-panel Textual dashboard: live feed, media wall, and intelligence briefing
- **Media downloads** — Automatic photo/video/GIF downloading with iTerm2 inline image support
- **Configurable profiles** — Six included config profiles (Iran, Israel, Ukraine, cybersecurity, crypto, Africa) — or generate your own
- **Caption translation** — Batch-translates media captions from non-English languages (Farsi, Arabic, Hebrew, Russian, French, etc.)
- **Headless mode** — `--log-only` for server deployments without a terminal UI

## Architecture

```
Telegram Channels
       │
       ▼
  Telethon (MTProto)
       │
       ▼
  asyncio message queue
       │
       ├──▶ TUI Live Feed Panel
       ├──▶ TUI Media Wall Panel (+ caption translation via Claude Haiku)
       └──▶ Message buffer
               │
               ▼
         Claude Sonnet analysis (batch)
               │
               ▼
         TUI Intelligence Briefing Panel
```

## Prerequisites

- **Python 3.10+**
- **Telegram API credentials** — obtain from [my.telegram.org](https://my.telegram.org) → API development tools
- **Claude API key** — obtain from [console.anthropic.com](https://console.anthropic.com) (used via `claude-agent-sdk`)
- **ffmpeg** (optional) — for video thumbnail extraction in iTerm2

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/zoharbabin/telegram-monitor.git
cd telegram-monitor

# 2. Install dependencies
pip install .

# 3. Configure credentials
cp .env.example .env
# Edit .env with your Telegram API ID, API hash, and Anthropic API key

# 4. Join channels (first time only)
python join_channels.py

# 5. Run the monitor
python monitor.py
```

On first run, Telethon will send a verification code to your Telegram app. Enter it at the prompt. Subsequent runs reconnect automatically.

## Usage

```bash
python monitor.py                                # TUI dashboard (default)
python monitor.py --log-only                     # Headless log mode
python monitor.py --debug                        # TUI with debug logging
python monitor.py --config configs/israel.json   # Use a different config profile
python monitor.py --setup                        # Print setup guide
python -m telegram_monitor                       # Run as a Python module
```

### Configuration Wizard

```bash
python configure.py                              # Interactive Claude-powered config generator
python configure.py --config new.json            # Generate a new config file
```

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `q` | Quit |
| `f` | Toggle live feed panel |
| `b` | Toggle intelligence briefing panel |
| `m` | Toggle media wall panel |
| `c` | Copy latest briefing to clipboard |
| `v` | View most recent media (iTerm2 inline or system viewer) |

## Project Structure

```
telegram-monitor/
├── monitor.py                  # Entry point wrapper → telegram_monitor.cli.main()
├── join_channels.py            # Entry point wrapper → telegram_monitor.join.main()
├── configure.py                # Entry point wrapper → telegram_monitor.wizard.main()
├── telegram_monitor/           # Python package (all library code)
│   ├── __init__.py
│   ├── __main__.py             # python -m telegram_monitor
│   ├── cli.py                  # CLI args, logging, orchestration
│   ├── client.py               # Telethon client — connects, streams, downloads media
│   ├── analyzer.py             # Claude-powered message analysis and translation
│   ├── tui.py                  # Multi-pane Textual terminal UI
│   ├── config.py               # Loads JSON config, exposes constants
│   ├── iterm_images.py         # iTerm2 inline image display (OSC 1337 protocol)
│   ├── utils.py                # Shared helpers (filename sanitization, arg parsing)
│   ├── join.py                 # Bulk-join Telegram channels from config
│   └── wizard.py               # Interactive configuration wizard (Claude-powered)
├── configs/
│   ├── iran.json               # Iran/Middle East focus (default)
│   ├── israel.json             # Israel/Palestine conflict
│   ├── ukraine.json            # Russia-Ukraine war
│   ├── cyber.json              # Cybersecurity threat intelligence
│   ├── crypto.json             # Crypto & DeFi markets
│   └── africa.json             # Africa security & stability
├── docs/
│   └── CONFIGURATION.md        # Full configuration reference
├── data/                       # Downloaded media files (auto-created, gitignored)
│   └── .gitkeep
├── tests/                      # pytest test suite
│   ├── fixtures/               # Test config fixtures
│   ├── test_analyzer.py
│   ├── test_client.py
│   ├── test_config.py
│   └── test_utils.py
├── .github/workflows/ci.yml   # GitHub Actions CI
├── .env.example                # Template for API credentials
├── .gitignore
├── pyproject.toml              # Python packaging metadata & entry points
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## Configuration

Configuration lives in JSON files under `configs/`. Each file is a complete region profile. Key sections:

- **channels** — Telegram channel usernames organized by category
- **topics** — Intelligence topics for focused analysis (each gets a deep-dive section)
- **summary_batch_size** / **summary_interval_seconds** — Analysis trigger thresholds
- **analysis_system_prompt** — Analyst persona and language capabilities
- **stances** / **tones** — Classification labels for source analysis

See [docs/CONFIGURATION.md](docs/CONFIGURATION.md) for the full reference.

### Config Profiles

Use `--config` to load different profiles:

```bash
python monitor.py --config configs/israel.json   # Israel/Palestine conflict
python monitor.py --config configs/ukraine.json  # Russia-Ukraine war
python monitor.py --config configs/cyber.json    # Cybersecurity threat intel
python monitor.py --config configs/crypto.json   # Crypto & DeFi markets
python monitor.py --config configs/africa.json   # Africa security & stability
```

Generate new profiles interactively with `python configure.py --config <name>.json`.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and guidelines. PRs for new config profiles are especially welcome.

## License

[MIT](LICENSE)
