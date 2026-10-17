<div align="center">

# Liquidation Cluster Signal Scraper

### Automated crypto liquidation heatmap signal detector for Binance, Bybit, and OKX futures markets.

![Liquidation Cluster Signal Scraper — workflow demo](media.gif)

</div>

**Liquidation Cluster Signal Scraper** is an open-source **crypto trading signal tool** that detects potential **short squeeze and long squeeze events** by monitoring liquidation heatmaps and open interest (OI) data across major derivatives exchanges.

The system continuously analyzes **liquidation clusters, price proximity, and open interest acceleration** to identify areas where leveraged traders are likely to be liquidated. These zones often act as liquidity magnets and can trigger rapid price moves in futures markets.

The scraper collects data from:

- **Binance Futures**
- **Bybit Perpetuals**
- **OKX derivatives markets**
- liquidation heatmap sources such as **Coinglass**

Signals are generated when:

- price approaches a high-density liquidation cluster
- open interest increases rapidly near that level
- cluster density exceeds a configurable threshold

The project runs **locally in Python using WebSockets, Selenium scraping, and exchange APIs**, and outputs structured signals that can be used for **manual trading, research, or integration with algorithmic trading systems**.


## 🧠 How the Squeeze Detector Works

Most traders watch liquidation heatmaps manually. They see a bright cluster on Coinglass, think "that looks like a magnet," and either act on instinct or hesitate too long.

This bot removes the human latency from that loop.

```
╔══════════════════════════════════════════════════════════════════════════╗
║              LIQUIDATION CLUSTER SIGNAL PIPELINE                         ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║   Exchange APIs / Heatmap Scrapers                                       ║
║   ┌─────────────────────────────┐                                        ║
║   │  Binance Futures OI Feed    │──────┐                                 ║
║   │  Bybit Liquidation WS       │      │                                 ║
║   │  OKX Open Interest REST     │      ▼                                 ║
║   └─────────────────────────────┘   ╔══════════════════╗                 ║
║                                     ║  Cluster Parser  ║                 ║
║   Heatmap Visual Scraper            ║  + OI Delta      ║                 ║
║   ┌─────────────────────────────┐   ║  Correlator      ║                 ║
║   │  Coinglass DOM Scraper      │──▶║                  ║                 ║
║   │  Hyblock Heatmap Parser     │   ╚════════╦═════════╝                 ║
║   └─────────────────────────────┘            │                           ║
║                                              ▼                           ║
║                                    ╔══════════════════╗                  ║
║                                    ║  Squeeze Signal  ║                  ║
║                                    ║  Engine          ║                  ║
║                                    ║  SHORT / LONG    ║                  ║
║                                    ╚════════╦═════════╝                  ║
║                                             │                            ║
║                          ┌──────────────────┼──────────────────┐         ║
║                          ▼                  ▼                  ▼         ║
║                    Console Alert      Log File           [Private]        ║
║                    + Threshold        + History          Telegram Push    ║
║                    Trigger            Replay             + Discord        ║
╚══════════════════════════════════════════════════════════════════════════╝
```

**The core insight:** Liquidation clusters are not random. They form where leveraged traders placed stops — and where price is statistically attracted once momentum builds toward them. By tracking both the *heatmap density* (where clusters sit) and *OI delta* (whether new positions are being added into resistance), the bot distinguishes between clusters that will be swept and clusters that will hold.

---

## 📡 Live Signal Output Samples

What the bot actually prints when it fires. These are representative outputs from paper-mode runs.

```
═══════════════════════════════════════════════════════════
  LIQUIDATION CLUSTER SIGNAL SCRAPER  |  v0.3.1
  Asset: BTCUSDT  |  Exchange: Binance Futures
  Scan Interval: 30s  |  Mode: PAPER
  UTC: 2026-03-11 14:22:07
═══════════════════════════════════════════════════════════

[14:22:07] OI SNAPSHOT       BTC/USDT  — OI: $14.82B  Δ+1h: +$312M (+2.15%)
[14:22:07] HEATMAP PARSE     Cluster detected @ $84,200 — Density: ████████░░ HIGH
[14:22:07] HEATMAP PARSE     Cluster detected @ $81,500 — Density: █████░░░░░ MED
[14:22:07] PRICE              Current: $83,440  |  Dist to upper cluster: 0.90%

[14:22:37] OI DELTA          +$48M in 30s  ← ACCELERATION DETECTED
[14:22:37] SIGNAL ENGINE     ⚡ SHORT SQUEEZE SETUP FORMING
           ├─ Cluster proximity: 0.90% above current price
           ├─ OI acceleration: +$48M / 30s (threshold: $30M)
           ├─ Cluster density score: 8.2 / 10
           └─ Confidence: HIGH

═══════════════════════════════════════════════════════════
  🔴 ALERT: SHORT SQUEEZE IMMINENT — BTCUSDT @ $83,440
  Target cluster: $84,200 (+0.90%)
  Recommendation: Monitor for long entry on confirmation candle
  Paper mode — no order placed
═══════════════════════════════════════════════════════════

[14:24:11] PRICE              $84,190  ← Cluster approached
[14:24:11] OI DELTA          -$187M in 90s  ← SHORT LIQUIDATIONS FIRING
[14:24:11] SIGNAL ENGINE     ✅ SQUEEZE CONFIRMED — cluster swept
           └─ Move: +$750 (+0.90%) in 94 seconds
```

```
═══════════════════════════════════════════════════════════
  Asset: ETHUSDT  |  Exchange: Bybit Perpetuals
  UTC: 2026-03-11 09:47:33
═══════════════════════════════════════════════════════════

[09:47:33] HEATMAP PARSE     Cluster @ $3,105 — Density: ██████████ EXTREME
[09:47:33] OI SNAPSHOT       ETH/USDT  — OI: $8.1B  Δ+1h: -$220M (-2.64%)
[09:47:33] SIGNAL ENGINE     ⚡ LONG SQUEEZE SETUP FORMING
           ├─ Cluster proximity: 1.2% below current price ($3,143)
           ├─ OI declining into support → longs adding at resistance
           ├─ Cluster density score: 9.7 / 10
           └─ Confidence: HIGH

[09:48:44] ALERT: LONG SQUEEZE IMMINENT — ETHUSDT @ $3,143
  Target cluster: $3,105 (-1.2%)
  Paper mode — no order placed

[09:51:02] SQUEEZE CONFIRMED — ETH swept to $3,098 in 138 seconds
```

---

## 🔬 Key Features of the Liquidation Cluster Signal Scraper

| Feature | What It Does |
|---|---|
| **Heatmap DOM Parser** | Scrapes live liquidation heatmap data from major sources — no paid API required |
| **OI Delta Engine** | Tracks open-interest change rate per configurable interval (15s / 30s / 60s) |
| **Cluster Proximity Trigger** | Fires alert when price enters configurable % range of a high-density cluster |
| **Squeeze Classifier** | Distinguishes SHORT squeeze setups from LONG squeeze setups based on OI direction |
| **Confidence Scoring** | Combines cluster density + OI acceleration + price distance into a single score |
| **Paper Mode** | Full signal pipeline runs without any trade execution — validate before you deploy |
| **History Logger** | Every signal written to JSON log with outcome tracking for backreview |
| **Configurable Thresholds** | All sensitivity values tunable per asset in `config.yaml` |

---

## ⚡ Why Not Just Use Coinglass?

This is the honest answer to the most common question.

Coinglass is excellent at *showing* you the heatmap. It does not *alert* you when a cluster is about to be hit, correlate it with OI acceleration, or make any programmatic decision. You are still the bottleneck — watching a browser tab.

| Capability | Coinglass | Hyblock | TradingView Script | **This Bot** |
|---|:---:|:---:|:---:|:---:|
| Live liquidation heatmap | ✅ | ✅ | ❌ | ✅ |
| Automated proximity alert | ❌ | ❌ | Partial | ✅ |
| OI delta correlation | Manual | Manual | ❌ | ✅ |
| Short vs Long squeeze classification | ❌ | ❌ | ❌ | ✅ |
| Confidence scoring per cluster | ❌ | ❌ | ❌ | ✅ |
| Runs locally (your machine) | ❌ | ❌ | ❌ | ✅ |
| Open source & auditable | ❌ | ❌ | Partial | ✅ |
| No monthly subscription | ❌ ($30-50/mo) | ❌ ($200+/mo) | Partial | ✅ |
| Push alerts (Telegram/Discord) | ❌ | ❌ | ❌ | 🔒 Private build |
| Multi-asset parallel scan | ❌ Manual | ❌ Manual | ❌ | 🔒 Private build |
| ML cluster scoring | ❌ | ❌ | ❌ | 🔒 Private build |

---

## 🏗️ Architecture Deep-Dive

The signal pipeline has four distinct layers. Understanding each one helps you tune it intelligently.

**Layer 1 — Data Ingestion**
Two parallel streams feed the parser: exchange WebSocket/REST feeds for live OI snapshots, and a Selenium-based DOM scraper for heatmap density values. Both streams are normalized into a common internal format before the cluster engine sees them.

**Layer 2 — Cluster Parser**
The parser identifies price levels where liquidation density exceeds a configurable threshold. It scores each cluster on a 1–10 scale using density magnitude, cluster width, and recency of formation. Only clusters above the score floor are passed to the signal engine.

**Layer 3 — Signal Engine**
The engine evaluates proximity (current price vs. nearest high-score cluster), OI delta direction and acceleration, and whether OI is net increasing or decreasing into the cluster. This combination separates a genuine squeeze setup from a cluster that price has already neutralized.

**Layer 4 — Alert Dispatch**
Console output with structured formatting in the public build. The private build adds Telegram bot integration, Discord webhook, and a local SQLite log with win-rate tracking per signal type.

---

## 🛠️ Installation

**Requirements:** Python 3.11+, Chrome/Chromium (for Selenium scraper), a terminal.

**Step 1 — Clone the repository**
```bash
git clone https://github.com/Leionion/liquidation-cluster-signal-scraper.git
cd liquidation-cluster-signal-scraper
```

**Step 2 — Create a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
```

**Step 3 — Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 4 — Configure your targets**
```bash
cp config.example.yaml config.yaml
nano config.yaml   # or open in any editor
```

**Step 5 — Run in paper mode first (strongly recommended)**
```bash
python3 main.py --mode paper
```

Paper mode runs the full signal pipeline with live data — alerts fire to console and log, but no orders are sent and no exchange credentials are required.

---

## ⚙️ Configuration

```yaml
# config.yaml — Liquidation Cluster Signal Scraper

# ── Assets to monitor ──────────────────────────────────────────────────
assets:
  - symbol: BTCUSDT
    exchange: binance       # binance | bybit | okx
    interval: 30            # OI snapshot interval in seconds
  - symbol: ETHUSDT
    exchange: bybit
    interval: 30

# ── Cluster Detection Thresholds ───────────────────────────────────────
cluster:
  min_density_score: 6.0    # 1–10 — clusters below this score are ignored
  proximity_pct: 1.5        # Alert when price is within 1.5% of cluster
  lookback_candles: 24      # How many periods of OI history to load on start

# ── OI Acceleration Trigger ─────────────────────────────────────────────
oi_delta:
  acceleration_usd: 30000000   # $30M OI change per interval triggers flag
  direction_confirm: true       # Require OI direction to match squeeze type

# ── Signal Engine ────────────────────────────────────────────────────────
signal:
  min_confidence: 7.0          # Minimum composite score to fire an alert
  cooldown_seconds: 120        # Min time between alerts for same asset

# ── Output ───────────────────────────────────────────────────────────────
output:
  log_file: logs/signals.json  # Signal history log path
  console: true                # Print alerts to terminal
  # telegram: false            # Available in private build
  # discord: false             # Available in private build

# ── Runtime ──────────────────────────────────────────────────────────────
mode: paper                    # paper | live (live requires exchange API keys)
log_level: INFO                # DEBUG | INFO | WARNING
```

---

## 📊 Supported Exchanges & Data Sources

| Source | Type | OI Data | Heatmap Data | Status |
|---|---|:---:|:---:|:---:|
| Binance Futures | WebSocket + REST | ✅ | ✅ (scraper) | Stable |
| Bybit Perpetuals | WebSocket + REST | ✅ | ✅ (scraper) | Stable |
| OKX Futures | REST | ✅ | 🔜 v0.5 | In Progress |
| Coinglass | DOM Scraper | — | ✅ | Stable |
| Hyblock | DOM Scraper | — | 🔜 v0.5 | Planned |
| dYdX | REST | 🔜 v0.6 | ❌ | Planned |

---

## 🗺️ Roadmap

```
✅  SHIPPED
    v0.1.0  — Binance OI delta engine + console alerts
    v0.2.0  — Selenium heatmap scraper (Coinglass)
    v0.3.0  — Cluster density scoring (1–10 composite)
    v0.3.1  — Short vs Long squeeze classifier
    v0.3.2  — Paper mode + JSON signal logger

🔨  ACTIVE DEVELOPMENT
    v0.4.0  — Bybit heatmap scraper integration
    v0.4.1  — OI acceleration threshold tuning UI
    v0.4.2  — Signal confidence backreview report generator

🔜  PLANNED (public build)
    v0.5.0  — OKX support + multi-source cluster consensus
    v0.5.1  — Hyblock DOM parser
    v0.6.0  — CLI dashboard with real-time cluster map

🔒  PRIVATE BUILD (in active development — contact for access)
    —  Telegram + Discord push alert integration
    —  Parallel multi-asset scanner (unlimited symbols)
    —  ML cluster scoring model (trained on 18 months of sweep data)
    —  Win-rate tracker with per-signal-type breakdown
    —  Webhook output for integration with any trading system
    —  Exchange order execution module (paper-validated before live)
```

---

## 🔐 Security & Privacy Architecture

This bot runs entirely on your machine. Understanding exactly what touches the network:

- **Exchange WebSocket / REST calls** — read-only public endpoints. No API key required in paper mode. In live mode, keys stay in your local `config.yaml` and are never transmitted anywhere except to the exchange.
- **Heatmap scraper (Selenium)** — opens a local Chrome instance and reads DOM data from the heatmap site. No credentials stored or sent.
- **Log files** — written to your local filesystem. Never uploaded.
- **No telemetry, no phone-home, no analytics.** The codebase is fully auditable.

---

## 💼 Want the Full Version?

The public repo gives you the complete signal detection pipeline — data ingestion, cluster parsing, OI correlation, and paper-mode alerting.

The private build adds the layer that turns signals into workflow: push alerts the moment a squeeze sets up, parallel scanning across every asset you care about simultaneously, and an ML scoring layer that has been trained on 18 months of confirmed sweep events to reduce noise.

**This is built for:**

| Profile | Why They Use the Full Build |
|---|---|
| **Crypto futures traders** running intraday plays on BTC, ETH, and alts — who are tired of missing squeezes because they weren't watching the right chart at the right second | Real-time Telegram alerts mean the setup finds you, not the other way around |
| **Algorithmic traders** who already have execution infrastructure and need a reliable, auditable signal feed they can pipe into their own system | Webhook output + JSON signal format integrates with any stack in under an hour |
| **Multi-asset traders** scanning 10+ perpetuals simultaneously | Parallel scanner handles N assets with no degradation in signal latency |
| **Systematic traders** who want to know whether a signal type actually has edge before sizing into it | Win-rate breakdown per signal type, per asset, per session — in a local dashboard |

**How to reach me:**

→ GitHub: **[@Leionion](https://github.com/Leionion)**

When you message, mention three things:
1. Which assets or exchanges you're primarily trading
2. Whether you need the alerts only, or alerts + execution
3. Whether you've run the public build already (not required — just helps me calibrate)

The full build is not a SaaS subscription. It's a direct handoff to serious traders who have a real use case. If that's you, the conversation is worth 10 minutes.

---

<div align="center">

**Built with:** Python 3.11 · Selenium · WebSockets · CCXT · asyncio · pandas

*The setup finds you. You make the call.*

[![GitHub](https://img.shields.io/badge/GitHub-Leionion-181717?style=for-the-badge&logo=github)](https://github.com/Leionion)

</div>
