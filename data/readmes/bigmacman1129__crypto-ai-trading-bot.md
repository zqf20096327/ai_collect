# Crypto Liquidity Trading Bot

Self-hosted **market-making, liquidity-signal, and arbitrage** bot for crypto spot markets. It watches the order book, posts inventory-aware quotes, and scans for cross-exchange and triangular edges.

The runtime is **Node.js** (not Python). Control it with ADAMANT messenger commands, optional Telegram/CLI, and a local health API.

[![Node](https://img.shields.io/badge/node-%3E%3D18.18-blue.svg)](https://nodejs.org/) [![License](https://img.shields.io/badge/license-GPL--3.0-green.svg)](LICENSE)

![Crypto Liquidity Trading Bot](assets/image.png)

<details>
<summary><strong>📋 Table of contents</strong></summary>

- [Why liquidity matters](#why-liquidity-matters)
- [Who this is for](#who-this-is-for)
- [Commercial use](#commercial-use)
- [Strategy concept](#strategy-concept)
- [Architecture](#architecture)
- [New in 7.1](#new-in-71)
- [Quick start](#quick-start)
- [What you get](#what-you-get)
- [How liquidity hunting works](#how-liquidity-hunting-works)
- [Installation](#installation)
- [Supported exchanges](#supported-exchanges)
- [Project layout](#project-layout)
- [Use cases](#use-cases)
- [Related projects](#related-projects)
- [FAQ](#faq)
- [Contributing](#contributing)

</details>

---

## Why liquidity matters

Most crypto trading bots rely only on **price and technical indicators**. Professional traders, however, monitor **order book liquidity**, because price often moves toward zones where liquidity is concentrated—and away when that liquidity is swept.

This project focuses on **liquidity-aware trading signals** instead of lagging indicators: it detects gaps, walls, and sweeps so you can act on structure, not just price.

---

## Who this is for

This project may be useful for:

- **Crypto trading firms** building in-house liquidity and execution tools  
- **Quant researchers** studying order book and market microstructure  
- **Exchanges** building surveillance or liquidity analytics  
- **Developers** building AI trading agents or signal systems  

---

## Commercial use

If you are interested in **custom crypto trading bots** (liquidity, arbitrage, execution), **AI trading signal systems**, or **liquidity detection algorithms** and exchange API integrations:

**For collaboration or development work:**

- **Telegram** — [@k02_xx](https://t.me/k02_xx)

---

## New in 7.1

Classic wash-volume market-making is still here. On top of it:

| Engine | What it does | How to start |
|---|---|---|
| **Smart quoter** | Avellaneda–Stoikov style two-sided quotes: spread from realized vol, skew from inventory | `/start mm smart` or `/enable smart 0.2%` |
| **Arbitrage** | Cross-exchange bid/ask scanner + triangular cycles on the home venue | `/enable arb scan` (default), `paper`, or `live -y` |
| **Signals** | Order-book imbalance, walls, gaps, liquidity sweeps | On by default; `/signals` |
| **Risk** | Max order, inventory, open notional, daily loss halt | `config.jsonc` → `risk`; `/risk` |

Live arbitrage is **opt-in**. Scan mode only alerts. Cross-exchange live legs need API keys on **both** venues (`arbitrage.accounts` plus the home account). REST latency and fees often consume small edges — treat live mode as experimental.

---

## Backtest performance

This release does **not** ship a verified historical backtest. Paper-trade `/enable arb paper` and `/start mm smart` on your pair before any live size. Live results depend on fees, delay, inventory, and venue quality.

Example signal:

```json
{
  "symbol": "ADM/USDT",
  "direction": "LONG",
  "strength": 0.61,
  "reason": "liquidity_sweep_detected",
  "ts": "2026-08-25T01:00:00Z"
}
```

---
## Strategy concept

**Price indicators lag. Liquidity moves first.**

Large orders and stop-loss clusters sit in the order book before price reaches them. When price sweeps those levels, liquidity is consumed and moves tend to accelerate. This bot identifies those levels and signals sweep events so you can trade with the flow instead of chasing price.

---

## Architecture

```
Exchange public/private APIs
        ↓
Order-book analytics (microprice, imbalance, walls, gaps)
        ↓
   ┌────┴────┬────────────┬──────────────┐
   ↓         ↓            ↓              ↓
Smart     Volume MM    Arb scanner    Signal engine
quoter    (optional)   (cross + tri)  (alerts)
   ↓         ↓            ↓
Risk manager (inventory / daily loss / order caps)
        ↓
ADAMANT / Slack / Discord /health /status
```

Core paths:

- `app.js` — boot, MongoDB, engines
- `trade/engines/` — pure math (quotes, arb, risk, book analytics)
- `trade/mm_*.js` — live loops
- `modules/commandTxs.js` — chat commands
- `trade/trader_*.js` — exchange adapters

---

## Quick start

### Quick start (Node)

```bash
git clone https://github.com/asonglin/crypto-liquidity-ai-trading-bot.git && cd crypto-liquidity-ai-trading-bot
npm install
cp config.default.jsonc config.jsonc
# set exchange keys, pair, and (optionally) ADAMANT passPhrase
node app.js
```

Then in chat:

```
/start mm smart
/enable arb scan
/signals
/arb
/risk
```

---

## What you get

| Capability | Description |
|------------|-------------|
| **Liquidity detection** | Scans order books and pools for depth, gaps, and imbalance. |
| **Hidden walls** | Surfaces large buy/sell walls and their changes. |
| **Multi-exchange** | Built to plug into Binance, Bybit, Kraken, OKX, and others. |
| **Alerts** | Configurable notifications when liquidity events fire. |
| **Trading framework** | Modular so you can add execution, risk, or dashboards. |

Use it for **liquidity grabs**, **order book imbalance strategies**, **market microstructure research**, and **algorithmic trading**—whether you trade manually or automate.

---

## How liquidity hunting works

Liquidity hunting targets zones where lots of orders sit (e.g. stop-loss clusters). When price sweeps those levels, liquidity is “taken” and price can move fast. This bot helps you find and watch those zones.

1. **Find** where large stop-loss clusters or thin book zones sit.  
2. **Detect** liquidity sweeps and wall removals in real time.  
3. **Alert** so you can enter when liquidity is taken or book vacuum appears.  
4. **Extend** with your own execution (manual or automated).

Signals you can get: *stop-loss clusters*, *sudden order book vacuum*, *liquidity wall removal*, *aggressive market order flow*.

---

## Installation

```bash
git clone https://github.com/asonglin/crypto-liquidity-ai-trading-bot.git
cd crypto-liquidity-ai-trading-bot
```

**Quick start (Node)** — main engine:

```bash
npm install
cp config.default.jsonc config.jsonc
# Edit config.jsonc, then:
node app.js
```

Then: `/start mm smart`, `/enable arb scan`, `/signals`.

---
## Production hardening checklist

- Keep `api.host` set to `127.0.0.1` unless you explicitly front the API with a trusted reverse proxy.
- Keep `api.debug` disabled in production; if enabled, configure `api.debugToken` and `api.debugAllowlist`.
- Prefer env vars for secrets (`BOT_PASSPHRASE`, `EXCHANGE_API_KEY`, `EXCHANGE_API_SECRET`) over plain config values.
- Never commit `config.jsonc` or `.env` with real credentials.

---

## Container deployment

Build and run with Docker Compose:

```bash
cp .env.example .env
cp config.default.jsonc config.jsonc
docker compose up --build -d
```

The compose stack starts:
- `bot` (this project)
- `mongo` (MongoDB 7)

---

## Supported exchanges

Adapters in this repo (spot):

| Exchange | Module |
|----------|--------|
| Azbit | `trader_azbit.js` |
| P2PB2B | `trader_p2pb2b.js` |
| StakeCube | `trader_stakecube.js` |
| Coinstore | `trader_coinstore.js` |
| FameEX | `trader_fameex.js` |
| NonKYC | `trader_nonkyc.js` |
| XeggeX | `trader_xeggex.js` |

The arb scanner uses public tickers on every name listed in `config.exchanges`. Live execution uses the home `exchange` keys, plus optional `arbitrage.accounts` for a second venue.

---

## Project layout

```
crypto-liquidity-ai-trading-bot/
├── app.js                 # entry point
├── config.default.jsonc   # config template
├── package.json
├── helpers/               # shared utils
├── modules/               # api, DB, config, commands
├── routes/                # /ping, /status, debug
├── trade/
│   ├── engines/           # analytics, quotes, arb math, risk
│   ├── mm_smart_quoter.js
│   ├── mm_arbitrage.js
│   ├── mm_signal_engine.js
│   ├── mm_trader.js       # volume MM (optional)
│   └── trader_*.js        # exchange adapters
├── tests/unit/
└── assets/
```

---

## Use cases

- **Crypto algorithmic trading** — Feed signals into your execution engine.  
- **Quant research** — Order book and liquidity analysis.  
- **AI/ML strategy dev** — Use liquidity events as features or triggers.  
- **Market microstructure** — Study gaps, walls, and sweep behavior.

---


## FAQ

**What is liquidity hunting?**  
A strategy that focuses on levels where lots of stop-loss or passive orders sit; when those levels are hit, liquidity is consumed and price often moves sharply.

**Is the bot fully automated?**  
Volume MM, smart quoting, and live arb can place orders. Arb defaults to **scan** (alerts only). Smart quotes need `/enable smart` or `/start mm smart`.

**Who is it for?**  
Token issuers and traders who want self-hosted market-making, microstructure signals, and a conservative arb scanner on the supported CEX adapters.

---

## Contributing

We welcome pull requests and issues. Fork → branch → PR. See CONTRIBUTING.md if present.

**License:** MIT © 2026
