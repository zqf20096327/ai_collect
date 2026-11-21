# AUREUS AI — Elite Trading Command Center

> A multi-agent AI system that analyses Forex, Crypto, Commodities, and Indices using Smart Money Concepts and Wyckoff methodology. Runs a full pipeline of specialist AI agents in parallel, then synthesizes everything into a single institutional-grade market outlook — all inside a sleek cyberpunk web UI.

---

## Table of Contents

1. [What It Does](#what-it-does)
2. [How It Works](#how-it-works)
3. [Project Structure](#project-structure)
4. [Requirements](#requirements)
5. [Installation](#installation)
6. [Configuration](#configuration)
7. [Running the App](#running-the-app)
8. [Using the Dashboard](#using-the-dashboard)
9. [Job Queue System](#job-queue-system)
10. [Technical Methodologies](#technical-methodologies)
11. [Disclaimer](#disclaimer)

---

## What It Does

You pick an asset (e.g. **GOLD**, **EUR/USD**, **BTC/USD**), click **Run Multi-Agent Analysis**, and the system:

1. **Downloads live market data** — OHLC candlestick data for the last 90 days on both 1-hour and 5-minute timeframes
2. **Runs two specialist AI analysts in parallel:**
   - An **SMC analyst** (Smart Money Concepts — tracks institutional order flow)
   - A **Wyckoff analyst** (identifies accumulation/distribution phases and trend stages)
3. **Runs two critic agents** that cross-check each analyst's report against the raw data and flag any errors
4. **Sends the critiques back** to the analysts to fix and produce final, corrected reports
5. **Runs a Metareasoning Consolidator** that reads both final reports, resolves any disagreements, and outputs a single trading signal with entry, stop-loss, and take-profit levels
6. **Streams all of this live** to the dashboard as it happens

The whole pipeline takes a few minutes. You can watch it run in real time in the console drawer.

---

## How It Works

```
                        ┌─────────────────────────────────┐
                        │         AUREUS AI Pipeline       │
                        └─────────────────────────────────┘

  [You click Analyse]
          │
          ▼
  ┌───────────────┐       ┌───────────────────────────────────────┐
  │ RealMarketAPI │──────▶│  1-hour chart + 5-min chart generated │
  │ Data Fetch    │       └───────────────────────────────────────┘
  └───────────────┘
          │
          ▼
  ┌──────────────────────────────────────┐
  │  Parallel Initial Analysis           │
  │                                      │
  │  ┌─────────────┐  ┌───────────────┐ │
  │  │ SMC Analyst │  │Wyckoff Analyst│ │
  │  └─────────────┘  └───────────────┘ │
  └──────────────────────────────────────┘
          │
          ▼
  ┌──────────────────────────────────────┐
  │  Grounding Critics (parallel)        │
  │  Check reports against raw data      │
  └──────────────────────────────────────┘
          │
          ▼
  ┌──────────────────────────────────────┐
  │  Reanalysis (parallel)               │
  │  Analysts correct their reports      │
  └──────────────────────────────────────┘
          │
          ▼
  ┌──────────────────────────────────────┐
  │  Metareasoning Consolidator          │
  │  Synthesises everything → Signal     │
  └──────────────────────────────────────┘
          │
          ▼
  [Dashboard shows charts + reports + signal]
```

**All AI calls are model-agnostic and use standard OpenAI-compatible completions.** Prompts are ordered such that system instructions and tool schemas are placed first, allowing providers that support prompt caching (like DeepSeek or Gemini) to cache context and save up to 90% in token costs.

---

## Project Structure

```
TradingBot/
│
├── server.py               # Flask web server — handles all API endpoints and SSE streaming
├── celery_app.py           # Celery + Redis configuration for the job queue
├── tasks.py                # The full analysis pipeline as a Celery background task
│
├── agent_orchestrator.py   # Coordinates parallel agent calls (initial → critique → reanalysis → consolidate)
├── tradebot.py             # SMC analysis agent (order blocks, FVGs, liquidity sweeps)
├── price_channels.py       # Wyckoff analysis agent (phases, springs, signs of strength)
├── trade.py                # Market data fetcher using RealMarketAPI
├── tradde.py               # Candlestick chart generator (produces base64 PNG images)
│
├── dashboard.html          # Main cyberpunk UI (open this in a browser via the server)
├── terminal.html           # Standalone console-only view
│
├── fx.py                   # Legacy CLI entrypoint (email dispatch, no UI)
├── requirements.txt        # Python package dependencies
└── .env                    # Your API key goes here (you create this)
```

---

## Requirements

### System Requirements

| Requirement | Minimum |
|-------------|---------|
| **Python** | 3.10+ |
| **Redis** | Any recent version (6+) |
| **OS** | Linux / macOS / WSL on Windows |
| **RAM** | ~512MB free |
| **Internet** | Required (for market data + AI API calls) |

### Why Redis?

Redis is used as a **message broker** and **state store** for the job queue. When you submit an analysis job, it gets written to Redis and picked up by a background Celery worker. This is what allows multiple jobs to run in parallel without hanging or blocking each other.

---

## Installation

### Step 1 — Install Redis

**Ubuntu / WSL:**
```bash
sudo apt update && sudo apt install redis-server -y
sudo service redis-server start
```

**macOS (Homebrew):**
```bash
brew install redis
brew services start redis
```

**Verify Redis is running:**
```bash
redis-cli ping
# Should print: PONG
```

---

### Step 2 — Clone the repo (if you haven't already)

```bash
git clone <your-repo-url>
cd TradingBot
```

---

### Step 3 — Install Python dependencies

```bash
pip install -r requirements.txt
```

This installs:

| Package | Purpose |
|---------|---------|
| `flask` + `flask-cors` | Web server |
| `celery` | Background job queue |
| `redis` | Python Redis client |
| `openai` | OpenAI client library (communicates with any OpenAI-compatible API) |
| `requests` | HTTP client for RealMarketAPI market data |
| `pandas` | Data manipulation |
| `mplfinance` + `scipy` | Chart generation |
| `mistune` | Markdown rendering |
| `python-dotenv` | Loading `.env` files |

---

### Step 4 — Create your `.env` file

```bash
# In the TradingBot/ directory:
echo 'LLM_API_KEY=your_api_key_here' > .env
echo 'LLM_BASE_URL=https://api.deepseek.com' >> .env
echo 'LLM_MODEL=deepseek-chat' >> .env
```

> Configure the credentials for your selected LLM provider and `REALMARKET_API_KEY` in `.env`. Keep this file local and never commit real credentials. If Redis uses a non-default address, set `REDIS_URL` as well:
> ```dotenv
> REDIS_URL=redis://localhost:6379/0
> ```

---

## Configuration

You can fully customize which LLM provider and model AUREUS AI uses. Configure the following variables in your `.env` file:

| Variable | Default | Description |
|----------|---------|-------------|
| `LLM_PROVIDER` | `selfhosted` | Provider mode. Use `deepseek` to select the DeepSeek defaults; other compatible OpenAI API endpoints can be configured with the URL and model variables. |
| `LLM_API_KEY` | Provider-specific fallback in current source | API credential for the selected LLM provider. Set your own key locally and do not commit it. |
| `LLM_BASE_URL` | Provider-specific | Base URL for the OpenAI-compatible LLM endpoint. |
| `LLM_MODEL` | Provider-specific | Model name sent to the LLM endpoint. |
| `REALMARKET_API_KEY` | *(required for live market data)* | Credential for RealMarketAPI candle and price data. |
| `REDIS_URL` | `redis://localhost:6379/0` | Redis broker and backend connection string. |

---

## Running the App

### The simple way (everything in one command)

```bash
python server.py
```

This does two things automatically:
1. **Starts the Flask web server** on `http://localhost:5050`
2. **Starts a Celery worker** in the background (handles the analysis queue with up to 3 parallel jobs)

Then open your browser: **[http://localhost:5050](http://localhost:5050)**

---

### The manual way (if you want separate terminals)

**Terminal 1 — Start the web server:**
```bash
python server.py
```

**Terminal 2 — Start the Celery worker manually:**
```bash
python -m celery -A tasks worker --loglevel=info --pool=threads --concurrency=3
```

> The `--concurrency=3` flag means up to **3 analyses can run at the same time**. If you submit a 4th, it waits in the queue.

---

### Checking that everything is running

After `python server.py`, you should see:
```
🚀 AUREUS AI on http://0.0.0.0:5050
👷 Starting background Celery worker process...
 * Running on http://127.0.0.1:5050
```

And `redis-cli ping` should still return `PONG`.

---

## Using the Dashboard

Once the server is running, open **http://localhost:5050** in your browser.

### Interface Overview

```
┌─────────────────────────────────────────────────────────────────┐
│  TOPBAR: Asset selector | Backtest toggle | [Run Analysis] btn  │
├───────────────────────┬────────────────────┬────────────────────┤
│  CHART PANEL          │  REPORT PANEL      │  SIDEBAR           │
│                       │                    │                    │
│  1-Hour chart         │  • Consolidated    │  Live Queue        │
│  (scroll to zoom,     │    Outlook tab     │  ─────────         │
│   drag to pan)        │  • SMC Analysis    │  ■ ■ □  slots      │
│                       │    tab             │  [GOLD running]    │
│  5-Min chart          │  • Wyckoff         │  [EURUSD queued]   │
│                       │    Analysis tab    │                    │
│                       │                    │  Completed         │
│                       │  [Console drawer   │  Sessions          │
│                       │   ▲ slides up]     │  ─────────         │
│                       │                    │  [BTC/USD done]    │
└───────────────────────┴────────────────────┴────────────────────┘
```

### How to run an analysis

1. **Click the asset selector** (top bar) and type or pick an asset — e.g. `GOLD`, `EUR/USD`, `BTC/USD`
2. **(Optional)** Enable **Backtest Mode** and pick a past date to analyse historical data
3. Click **Run Multi-Agent Analysis** ⚡
4. The console drawer slides up and streams live progress logs
5. Charts and reports appear as the pipeline completes

### Viewing a past analysis

Click any card in the **Completed Sessions** panel (right sidebar) to reload that job's charts and reports.

### Position Size Calculator

The right sidebar has a built-in calculator. Enter your:
- Account balance
- Leverage
- Entry price
- Stop-loss price
- Lot size

It will calculate your required margin, pip distance, dollar risk, and account risk percentage.

---

## Job Queue System

AUREUS AI uses **Celery + Redis** to manage analysis jobs as a proper background queue. This means:

### Key behaviours

- **Submit freely** — You can click "Run Analysis" multiple times without waiting. Each submission is queued as a separate job.
- **3 jobs run in parallel** — The Celery worker runs up to 3 analyses simultaneously. A 4th waits until a slot opens.
- **Jobs survive UI refreshes** — Because state is stored in Redis, you can reload the page and your jobs are still there.
- **Monitor live** — The **Live Analysis Queue** panel (top of right sidebar) shows running and queued jobs in real time, updating every 2 seconds.

### Understanding the queue panel

```
Live Analysis Queue
■ ■ □   0 running · 1 queued
```

| Colour | Meaning |
|--------|---------|
| 🔵 Cyan slot | A running analysis (occupying a worker thread) |
| 🟡 Amber slot | A queued analysis (waiting for a free slot) |
| ⬜ Empty slot | Available capacity |

Click any job card in the queue to switch the console stream to that specific job.

### Queue API

| Endpoint | Method | Description |
|----------|--------|-------------|
| `GET /api/queue` | GET | Live queue status: running, queued, capacity |
| `GET /api/jobs` | GET | All jobs (all statuses) |
| `GET /api/job/<id>` | GET | Full details + results for a specific job |
| `POST /api/analyse` | POST | Submit a new analysis job |
| `GET /api/stream/<id>` | GET | SSE stream for real-time job events |

---

## Technical Methodologies

### The Core Wisdom: Synergy of Wyckoff & SMC

The underlying logic of the AUREUS AI analysis pipeline relies on combining two institutional methodologies to form a complete trading plan:
> 💡 **The Wisdom**: **Wyckoff** tells us the **long-term direction** (the macro market cycle phase), and **SMC** tells us the **exact entry** (the micro order block/liquidity sweep levels).

By running both systems, the Metareasoning Consolidator ensures we are trading *with* the structural macro cycle (Wyckoff) while executing at high-probability institutional mitigation zones (SMC).

- **Direction Alignment**: If Wyckoff indicates a macro markup (bullish trend) but SMC finds no institutional buy block or shows a bearish structural break, the consolidator flags the contradiction and takes **no trade**.
- **Execution Precision**: When both agree (e.g. Wyckoff marks a markup structure and SMC spots a fresh bullish order block), we execute a trade using the SMC zone to minimize drawdowns.

---

### Smart Money Concepts (SMC)

Tracks **what institutions are doing** rather than retail indicator signals.

| Concept | What it means |
|---------|---------------|
| **Order Blocks** | Zones where big banks placed large orders — price tends to react there again |
| **Fair Value Gaps (FVG)** | Price imbalances created by rapid moves — often filled before continuation |
| **Liquidity Sweeps** | Price spikes that grab retail stop-losses before reversing — the "trap" |
| **Supply & Demand Zones** | Areas of strong institutional interest where price reversed sharply |

### Wyckoff Method

Identifies **where in the market cycle** we are.

| Phase | What it means |
|-------|---------------|
| **Accumulation** | Big players quietly buying — price looks choppy/flat |
| **Markup** | Price starts rising as institutions have filled their positions |
| **Distribution** | Big players quietly selling into retail buying |
| **Markdown** | Price falls as institutions have exited |

Key events like **Springs** (fake breakdowns), **Secondary Tests**, and **Signs of Strength** help pinpoint the exact sub-phase.

---

## Common Issues

**Redis connection refused**
```
Make sure Redis is running: sudo service redis-server start
```

**LLM API error (401)**
```
Check your .env file has LLM_API_KEY set correctly, with no quotes or spaces, and verify that LLM_BASE_URL aligns with your provider.
```

**Analysis hangs at "fetching data"**
```
Check your internet connection and verify REALMARKET_API_KEY is set in your .env file.
```

**Port 5050 already in use**
```bash
# Kill whatever is using it:
sudo lsof -i :5050
kill -9 <PID>
```

---

## Disclaimer

This project is provided for **research and educational use**. It does not provide financial advice or guarantee accurate market analysis. Trading can result in substantial losses. Verify all data and outputs independently; do not use generated signals as the sole basis for a financial decision.
