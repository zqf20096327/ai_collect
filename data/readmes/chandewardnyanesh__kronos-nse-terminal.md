# Kronos NSE Trading Terminal

> **First open-source application of Kronos (AAAI 2026) to Indian markets** — a real-time trading terminal with AI-powered candlestick forecasting, walk-forward backtesting, technical indicators, and dual data sources.

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://python.org)
[![Kronos](https://img.shields.io/badge/Model-Kronos--base%20102M-yellow)](https://github.com/shiyu-coder/Kronos)
[![Flask](https://img.shields.io/badge/Backend-Flask-green)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

![Dashboard Preview](docs/dashboard_preview.png)

## What this is

A production-quality trading terminal that runs the [Kronos foundation model](https://github.com/shiyu-coder/Kronos) (accepted AAAI 2026, trained on 45+ global exchanges) on live NSE/BSE data. Built as an end-to-end ML system from data ingestion to model inference to quantitative evaluation.

**Key contributions:**
- First public application of Kronos to Indian markets (NSE/BSE)
- Walk-forward backtesting framework with Sharpe ratio, max drawdown, P&L simulation
- Dual data source architecture: yfinance primary + Zerodha Kite live backup
- Confidence band visualisation from multi-sample Kronos inference
- Structured trading signal engine combining Kronos output with 5 technical indicators
- Async inference pipeline (job polling) — handles 1–5 min CPU inference without UI blocking
- MCP server integration — forecasts callable as Claude AI tool

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     NSE Trading Terminal                     │
├──────────────┬──────────────────────┬───────────────────────┤
│  Data Layer  │   Inference Layer    │    Analytics Layer    │
│              │                      │                       │
│  yfinance    │  KronosTokenizer     │  Technical Indicators │
│  (primary)   │  → discrete tokens   │  RSI, MACD, BB, VWAP  │
│              │                      │  EMA9/21, SuperTrend  │
│  Kite API    │  Kronos Transformer  │                       │
│  (live/bkp)  │  102M params (base)  │  Walk-Forward Backtest│
│              │  autoregressive      │  Hit rate, Sharpe,    │
│  ORB calc    │  OHLCV generation    │  MAE, P&L simulation  │
│              │                      │                       │
│              │  Multi-sample paths  │  Signal Generation    │
│              │  → confidence bands  │  Entry / SL / Target  │
└──────────────┴──────────────────────┴───────────────────────┘
         ↓                   ↓                    ↓
┌─────────────────────────────────────────────────────────────┐
│              Flask REST API  (port 7073)                    │
│  /api/fetch-data  /api/predict  /api/backtest               │
│  /api/indicators  /api/signal   /api/kite-connect           │
└─────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────┐
│         Dark Terminal UI  (Plotly.js + vanilla JS)          │
│  Live candlestick chart · ORB overlay · Prediction bands   │
│  Indicator panel · Signal card · Backtest equity curve     │
└─────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────┐
│              Kronos MCP Server  (stdio)                     │
│  Claude AI tools: kronos_forecast, kronos_batch_forecast    │
│  Shared model cache via ~/kronos_mcp_venv                   │
└─────────────────────────────────────────────────────────────┘
```

---

## Features

### Live Market Data
- **yfinance** for all intervals (1m → 1d) — no API key required
- **Zerodha Kite** live feed — real-time candle top-up during market hours (09:15–15:30 IST)
- Auto-fallback: if yfinance fails → Kite; if market live → Kite top-up applied
- 12 NSE instruments pre-configured: NIFTY 50, BANK NIFTY, RELIANCE, TCS, HDFC, INFY, ICICI...

### Kronos AI Forecasting
- **Kronos-mini** (4.1M, 2048 ctx) · **Kronos-small** (24.7M, 512 ctx) · **Kronos-base** (102.3M, 512 ctx)
- Full-day forecast (75 × 5-min candles = 09:15–15:30)
- **Multi-sample confidence bands** — run N paths, visualise 5th/95th percentile
- Async prediction: POST returns `job_id` → poll `/api/predict-status/{id}` every 2s

### Technical Indicators
| Indicator | Parameters | Use |
|-----------|-----------|-----|
| EMA 9/21/50 | — | Trend direction |
| VWAP | Intraday reset | Fair value |
| RSI | 14-period | Momentum |
| MACD | 12/26/9 | Trend + momentum |
| Bollinger Bands | 20-period, 2σ | Volatility |
| ATR | 14-period | Position sizing |
| SuperTrend | 10-period, 3× ATR | Trend filter |

### Walk-Forward Backtesting
```
Hit Rate:      63.4%    (% correct directional calls)
MAE:           ₹18.2    (mean absolute error)
Sharpe Ratio:  1.47     (annualised)
Max Drawdown:  -4.2%
Total P&L:     ₹12,840  (on ₹1L position, 60 trades)
```
*(Sample results — actual results vary by instrument and market conditions)*

### Trading Signal Engine
Combines Kronos forecast with all indicators to generate structured signals:
```json
{
  "direction":   "BUY",
  "confidence":  71.4,
  "entry":       23609.30,
  "stop_loss":   23521.45,
  "target_1":    23668.12,
  "target_2":    23777.90,
  "risk_reward": 1.92,
  "reasoning":   ["Kronos: +0.82% predicted", "RSI 38 — neutral", "EMA9 > EMA21 — bullish"]
}
```

---

## Quick Start

### Option 1: Python (recommended)

```bash
# Clone
git clone https://github.com/chandewardnyanesh/Kronos.git
cd Kronos

# Install
pip install -r webui/requirements_nse_enhanced.txt

# Pre-download model (first time only, ~400MB)
python -c "
from model import Kronos, KronosTokenizer
KronosTokenizer.from_pretrained('NeoQuasar/Kronos-Tokenizer-base')
Kronos.from_pretrained('NeoQuasar/Kronos-base')
print('Ready.')
"

# Run
KRONOS_REPO_PATH=. python webui/nse_dashboard_enhanced.py
# open http://localhost:7073
```

### Option 2: Docker

```bash
docker build -t kronos-nse .
docker run -p 7073:7073 kronos-nse
# open http://localhost:7073
```

### Kite Live Data (optional)

1. Create a Kite Connect app at [developers.zerodha.com](https://developers.zerodha.com)
2. In the dashboard sidebar → Kite Connect → enter API key
3. Click "Open Login URL" → authorise → paste the `request_token` back
4. Toggle data source to "Kite Live"

---

## API Reference

All endpoints accept/return JSON. No authentication required (localhost only).

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/symbols` | GET | Available instruments and intervals |
| `/api/fetch-data` | POST | Fetch OHLCV + ORB levels |
| `/api/indicators` | POST | Compute all technical indicators |
| `/api/predict` | POST | Start async Kronos forecast → returns `job_id` |
| `/api/predict-status/{id}` | GET | Poll forecast job status |
| `/api/signal` | POST | Get structured trading signal |
| `/api/backtest` | POST | Run walk-forward backtest |
| `/api/load-model` | POST | Load Kronos model into memory |
| `/api/model-status` | GET | Check loaded model |
| `/api/kite-connect` | POST | Authenticate with Kite |

---

## Project Structure

```
webui/
├── nse_dashboard_enhanced.py   # Flask app, all routes
├── data_fetcher_enhanced.py    # yfinance + Kite dual source
├── indicators.py               # Technical indicators (7 indicators)
├── signals.py                  # Trading signal generator
├── backtester.py               # Walk-forward backtesting engine
├── templates/
│   └── nse_dashboard_enhanced.html   # Dark terminal UI
├── requirements_nse_enhanced.txt
└── Dockerfile

kronos_mcp/
├── server.py                   # Kronos MCP server (Claude tool integration)
└── setup.sh

india_finetune/
├── fetch_india_data.py         # NSE data fetcher for fine-tuning
└── run_india_finetune.py       # End-to-end fine-tuning pipeline
```

---

## Technical Highlights (for interviews)

**Why this project stands out:**

1. **Novel application of SOTA research** — Kronos (AAAI 2026, 27k GitHub stars) had no Indian market tooling. This fills that gap.

2. **End-to-end ML system** — raw market data → tokenization → transformer inference → structured signal → backtested P&L. Not a demo script.

3. **Quantitative rigour** — walk-forward testing (not in-sample), realistic transaction costs, proper Sharpe computation, max drawdown.

4. **Production patterns** — async job queue (no blocking on 1-5min CPU inference), dual data source with failover, NaN-safe JSON serialisation, IST-aware market hour filtering.

5. **MCP integration** — Kronos forecast callable as a Claude AI tool, enabling conversational trading analysis.

---

## Disclaimer

This project is for educational and research purposes only. It is not financial advice. Past backtested performance does not guarantee future results. Always consult a qualified financial advisor before trading.

---

## Citation

If you use Kronos in your research:
```bibtex
@misc{shi2025kronos,
  title={Kronos: A Foundation Model for the Language of Financial Markets},
  author={Yu Shi et al.}, year={2025},
  eprint={2508.02739}, archivePrefix={arXiv}
}
```
