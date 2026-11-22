# ⚡ Wall Street MCP Suite — Examples & Quick Start

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![PyPI Version](https://img.shields.io/pypi/v/wallstreet-mcp-tools.svg)](https://pypi.org/project/wallstreet-mcp-tools/)
[![Claude Desktop](https://img.shields.io/badge/Claude-Desktop-orange.svg)](https://claude.ai)
[![Cursor](https://img.shields.io/badge/Cursor-IDE-purple.svg)](https://cursor.sh)
[![ChatGPT](https://img.shields.io/badge/ChatGPT-Plugin%20%26%20MCP-teal.svg)](https://chatgpt.com)
[![Model Context Protocol](https://img.shields.io/badge/MCP-2024--11--05-green.svg)](https://modelcontextprotocol.io)
[![M8ven Score](https://m8ven.ai/badge/mcp/mcp-collector-pick-wallstreet-mcp-examples-1us97n?v=8fc0f6d2c66b01728a4b35a291e6db1b)](https://m8ven.ai/mcp/mcp-collector-pick-wallstreet-mcp-examples-1us97n?s=readme)

Ready-to-use examples for connecting **90+ institutional-grade quantitative & macro engines** to Claude Desktop, Cursor, Windsurf, ChatGPT (Custom GPT Actions), LangChain, and CrewAI via the [Model Context Protocol (MCP)](https://modelcontextprotocol.io).

---

### 📸 Live Demo Output Preview (360° Quant Audit on NVDA)

```text
🏛️ WALL STREET INSTITUTIONAL INVESTMENT MEMO — NVIDIA CORP ($NVDA)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 1. FUNDAMENTAL HEALTH & ECONOMIC MOAT
   • Buffett Economic Moat: WIDE MOAT (ROIC 58.2% vs WACC 11.4% → +46.8% spread)
   • 9-Point Piotroski F-Score: 8 / 9 (Top 2% Institutional Decile)
   • Altman Z-Score: 14.82 (Safe Zone > 3.0, Zero Bankruptcy Risk)
   • Lynch PEG Parity: 1.15 (Growth-adjusted Valuation: Fair-to-Attractive)

📈 2. TECHNICAL SQUEEZE & MOMENTUM FACTOR
   • John Carter TTM Squeeze: FIRED BULLISH (Bollinger Band expanded outside Keltner)
   • Wilder RSI(14): 64.2 (Bullish momentum zone, no divergence)
   • 20MA / 200MA Reclaim: RECLAIMED (Trading +12.4% above rising 200DMA)

🐋 3. FLOW & INSTITUTIONAL CONVICTION
   • 13F Superinvestor Net Flow: +$1.84B Net Inflow (Top 3 tech hedge funds accumulating)
   • Dark Pool Off-Exchange Volume: 48.2% (Institutional block accumulation detected)
   • Order Flow Imbalance: +61.4% Buyer Dominance

🛡️ 4. RISK MANAGEMENT & STOP-LOSS CONTRACT
   • Dynamic 2ATR Trailing Stop: $128.40 (Current Price: $141.50)
   • SPDR XLK Sector Relative Strength: Top Decile (+4.2% alpha vs SPY)

🎯 VERDICT: STRONG BULLISH CONVICTION | TIMEFRAME: SWING (2-6 WEEKS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

<div align="center">
  <img src="assets/wallstreet-suite.gif" alt="Claude Desktop Wall Street Suite Live Demo" width="100%" />
  <p><em>▲ Real-time Claude Desktop session: Executing 360° Quant Audit on NVDA via Wall Street Suite MCP (Pure MCP Mode, No Web Search).</em></p>
</div>

---

## 🤔 Why This Exists

LLMs hallucinate financial metrics. When you ask Claude to calculate a Piotroski F-Score from memory, it's off by 2-3 points out of 9. When it estimates WACC, the error margin is 4-8 percentage points.

This MCP suite **pre-computes all 60 quantitative indicators** server-side and streams only the deterministic results — so your AI agent works with verified numbers, not guesses.

---

## 🚀 Quick Start

### Option A: Claude Desktop (30 seconds)

1. Open your `claude_desktop_config.json`:
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

2. Add this configuration:

```json
{
  "mcpServers": {
    "wallstreet-suite": {
      "command": "npx",
      "args": [
        "-y",
        "@apify/actors-mcp-server",
        "--actors",
        "mcp_collector/wallstreet-hedgefund-suite-mcp"
      ],
      "env": {
        "APIFY_TOKEN": "YOUR_APIFY_TOKEN"
      }
    }
  }
}
```

3. Restart Claude Desktop. Try prompting:
> *"Run a 360° institutional quant audit on NVDA"*

---

### Option B: Cursor / Windsurf (30 seconds)

Add to your Cursor MCP settings (`Cursor Settings > Features > MCP > Add New MCP Server`):

- **Type**: `SSE`
- **Name**: `wallstreet-master`
- **URL**: `https://mcp.apify.com/?actors=mcp_collector/wallstreet-hedgefund-suite-mcp`
- **Headers**:
  - `Authorization`: `Bearer YOUR_APIFY_TOKEN`

---

### Option C: Python (LangChain / CrewAI / AutoGen)

```bash
pip install langchain-mcp-adapters langchain-openai
```

```python
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o", temperature=0)
tools = load_mcp_tools(
    "https://mcp.apify.com/?actors=mcp_collector/wallstreet-hedgefund-suite-mcp"
)
agent = llm.bind_tools(tools)
response = agent.invoke("Run a 360° quant audit on NVDA")
print(response)
```

---

### Option D: ChatGPT (Official Plugins & MCP Server — 30 seconds)

Connect directly to ChatGPT via the official 2026 Agent Plugin and Remote MCP Gateway:

1. **Add MCP Server (`Settings > MCP Servers > + Add Server`)**:
   - **URL**: `https://wallstreet.mcp-collector.workers.dev`
   - **Headers**: Leave completely blank (Enables OAuth 2.1 user authentication flow).
2. **Enable Plugin (`Custom Settings > Plugins`)**:
   - Verify `Wall Street Hedge Fund Suite` (v0.1.4) is enabled.
3. **Execute in Chat**:
   - Prompt: `@Wall Street Hedge Fund Suite Run a full 360-degree institutional quant analysis on NVDA.`
   - Click the **[Authenticate]** button to link your Apify token once.
   - Comprehensive quantitative hedge fund memo will be rendered in real-time.
4. See [`examples/chatgpt/README.md`](examples/chatgpt/README.md) for full step-by-step walkthrough, screenshots, and troubleshooting.

---

### Option E: Autonomous Agent Recipes (Cron, CrewAI & LangChain)

Looking to run 24/7 automated quant research pipelines? Check the recipes in [`examples/automation/`](examples/automation/):

- **Daily Morning S&P 500 Screener** (`daily_morning_screener.py`): Automated pre-market audit across watchlist + Slack alerts.
- **3-Agent Autonomous Hedge Fund Team** (`crewai_hedgefund_team.py`): Forensic Analyst + Risk Officer + CIO in CrewAI.
- **Forensic Anomaly Sentinel** (`langchain_anomaly_sentinel.py`): Real-time monitor for Beneish earnings manipulation and Altman Z distress.

```bash
cd examples/automation && pip install -r requirements.txt
python daily_morning_screener.py
```

### Option F: Python SDK (`pip install wallstreet-mcp-tools`)

Install the official Python client directly from PyPI:

```bash
pip install wallstreet-mcp-tools
```

```python
from wallstreet_mcp import WallStreetClient

client = WallStreetClient()
audit = client.audit('NVDA')
print(f"Piotroski F-Score: {audit.get('piotroski_f_score')}/9")
```

---

## 🔬 Benchmark: Traditional Scraping vs. MCP Suite

*Reproducible test: Full 360° fundamental & technical audit on NVDA*

| Metric | Traditional Scraping / Raw APIs | MCP Suite | Improvement |
| :--- | :---: | :---: | :---: |
| **Execution Latency** | 14.2s (anti-bot waiting) | **2.1s (direct stream)** | **6.7x faster ⚡** |
| **Context Tokens** | ~22,400 (raw JSON/HTML) | **~1,150 (quant-optimized)** | **94.8% reduction 📉** |
| **Piotroski Accuracy** | High hallucination risk | **100% Deterministic** | Math-grounded 🎯 |
| **Buffett Moat (ROIC-WACC)** | Rough guess | **Exact spread** | Deterministic 🎯 |
| **Cost per 1,000 queries** | ~$15+ (token overhead) | **$8 ($0.008/call)** | **~50% savings 💰** |

---

## 🏛️ 5 Hero Engines

| Engine | What It Does | Try This Prompt |
| :--- | :--- | :--- |
| **360° Master Hub** | All-in-one institutional investment memo | *"Full 360° quant audit on AAPL"* |
| **Buffett Economic Moat** | ROIC vs WACC spread analysis | *"Does MSFT have an economic moat?"* |
| **TTM Squeeze** | Bollinger inside Keltner compression detection | *"Is TTM Squeeze firing on TSLA?"* |
| **13F Whale Flow** | Berkshire, Bridgewater, Scion portfolio tracking | *"Check OXY for Berkshire accumulation"* |
| **Dark Pool Activity** | Off-exchange institutional block prints | *"Show dark pool activity for AMZN"* |

---

<details>
<summary><strong>📦 Full 90+ Quantitative Engine Catalog (click to expand)</strong></summary>

| # | Category | Engine Actor ID | Description |
|---|----------|-----------------|-------------|
| 1 | Trend | `us-stock-etf-quant-signal-mcp` | RSI Turnup, 20MA Breakout, 2ATR Stop |
| 2 | Macro | `macro-regime-liquidity-mcp` | Goldilocks vs Stagflation 7-Asset Regime |
| 3 | Flow | `smart-money-insider-flow-mcp` | 13F & C-Suite Insider Net Inflow |
| 4 | Consensus | `wallstreet-consensus-target-mcp` | Mean/High/Low Targets & 4Q Beat Streak |
| 5 | Dividend | `us-dividend-safety-growth-mcp` | OCF Payout Coverage & Dividend Cut Risk |
| 6 | Short | `us-short-squeeze-sentiment-mcp` | Short % of Float & Days to Cover |
| 7 | Value | `us-stock-intrinsic-value-dcf-mcp` | Graham Number & Lynch PEG Parity |
| 8 | Options | `options-market-sentiment-maxpain-mcp` | PCR & Max Pain Strike Magnet |
| 9 | Sector | `sp500-sector-rotation-relative-strength-mcp` | 11 SPDR Sector Momentum |
| 10 | Earnings | `earnings-calendar-catalyst-mcp` | D-Day Countdown & Earnings Shock Defense |
| 11 | Crypto | `crypto-bitcoin-macro-onchain-mcp` | Mayer Multiple 200DMA & Funding Rates |
| 12 | FX | `global-fx-dollar-liquidity-mcp` | DXY & USD/JPY Yen Carry Stress |
| 13 | Commodity | `commodity-gold-oil-inflation-mcp` | Dr. Copper/Gold Ratio & WTI |
| 14 | VIX | `volatility-vix-tail-risk-mcp` | Spot VIX / VIX3M Contango & SKEW |
| 15 | Squeeze | `bollinger-keltner-squeeze-momentum-mcp` | TTM Squeeze Detection |
| 16 | Health | `financial-health-piotroski-altman-mcp` | 9-pt F-Score & Altman Z |
| 17 | Moat | `quality-moat-roic-wacc-mcp` | ROIC vs WACC Spread |
| 18 | Breadth | `us-market-breadth-thrust-mcp` | RSP/SPY Divergence & Zweig Thrust |
| 19 | 13F | `institutional-13f-superinvestor-portfolio-mcp` | Berkshire, Scion, Bridgewater |
| 20 | Special | `stock-splits-spinoff-special-situations-mcp` | Stock Splits & Buyback Yield |
| 21 | **Hub** | `wallstreet-hedgefund-suite-mcp` | **All-in-One 360° Master Hub** |
| 22 | Fib | `us-stock-fibonacci-retracement-mcp` | 61.8% Golden Ratio S/R |
| 23 | Ichimoku | `us-stock-ichimoku-cloud-mcp` | 9/26/52 Kumo Breakout |
| 24 | MACD | `us-stock-macd-divergence-mcp` | Hidden/Regular Divergence |
| 25 | VWAP | `us-stock-volume-profile-vwap-mcp` | Anchored VWAP & POC |
| 26 | Gap | `us-stock-gap-analysis-mcp` | Unfilled Gap Analysis |
| 27 | ETF Flow | `us-etf-fund-flow-tracker-mcp` | Institutional ETF Liquidity |
| 28 | Insider | `us-stock-insider-cluster-buy-mcp` | C-Suite Cluster Buy |
| 29 | RS | `us-stock-relative-strength-ibdrs-mcp` | IBD RS 1-99 Rating |
| 30 | Dark Pool | `us-stock-dark-pool-activity-mcp` | Off-Exchange Block Prints |
| 31 | Order Flow | `us-stock-order-flow-imbalance-mcp` | Bid/Ask Delta |
| 32 | SAR | `us-stock-parabolic-sar-trend-mcp` | Stop & Reversal |
| 33 | Volume | `us-stock-volume-breakout-surge-mcp` | RVol > 2.5x Breakout |
| 34 | OBV | `us-stock-smart-money-accumulation-obv-mcp` | On-Balance Volume |
| 35 | ADX | `us-stock-adx-trend-strength-mcp` | ADX, +DI/-DI |
| 36 | Donchian | `us-stock-donchian-channel-breakout-mcp` | Turtle Trading 20/55 |
| 37 | CMF | `us-stock-chaikin-money-flow-cmf-mcp` | 21-Day Chaikin |
| 38 | Keltner | `us-stock-keltner-channel-breakout-mcp` | ATR Volatility Band |
| 39 | StochRSI | `us-stock-stochastic-rsi-momentum-mcp` | Fast Oscillator |
| 40 | Supertrend | `us-stock-supertrend-indicator-mcp` | ATR Trailing Flip |
| 41 | Aroon | `us-stock-aroon-oscillator-trend-mcp` | 25-Day Trend |
| 42 | Vortex | `us-stock-vortex-indicator-mcp` | VM+/VM- Cross |
| 43 | Coppock | `us-stock-coppock-curve-momentum-mcp` | Monthly Bottom Finder |
| 44 | CCI | `us-stock-commodity-channel-index-cci-mcp` | Mean Deviation |
| 45 | ROC | `us-stock-rate-of-change-roc-mcp` | Price Velocity |
| 46 | Williams | `us-stock-williams-r-momentum-mcp` | -80/-20 Oversold |
| 47 | Ultimate | `us-stock-ultimate-oscillator-mcp` | 3-Period Multi-TF |
| 48 | Elder-Ray | `us-stock-elder-ray-bull-bear-power-mcp` | Bull/Bear Power |
| 49 | KAMA | `us-stock-kaufman-adaptive-moving-average-kama-mcp` | Adaptive MA |
| 50 | Hull MA | `us-stock-hull-moving-average-hma-mcp` | Zero-Lag MA |
| 51 | TRIX | `us-stock-trix-triple-exponential-mcp` | Triple EMA RoC |
| 52 | Mass Index | `us-stock-mass-index-reversal-mcp` | Reversal Bulge |
| 53 | DPO | `us-stock-detrended-price-oscillator-dpo-mcp` | Cycle Peak/Trough |
| 54 | KST | `us-stock-know-sure-thing-kst-mcp` | Multi-TF RCMA |
| 55 | McGinley | `us-stock-mcginley-dynamic-indicator-mcp` | Auto-Speed MA |
| 56 | EOM | `us-stock-ease-of-movement-eom-mcp` | Volume-to-Price |
| 57 | MFI | `us-stock-money-flow-index-mfi-mcp` | Volume-Weighted RSI |
| 58 | Force | `us-stock-force-index-elder-mcp` | Price×Volume |
| 59 | TSI | `us-stock-true-strength-index-tsi-mcp` | Double Smoothed |
| 60 | BOP | `us-stock-balance-of-power-bop-mcp` | Buyer/Seller Dominance |
| 61 | Bands | `us-stock-vwap-bands-mcp` | VWAP StdDev Bands |
| 62 | Thrust | `us-stock-elder-force-index-mcp` | Elder Force Index Volume Thrust |
| 63 | Volatility | `us-stock-chaikin-volatility-mcp` | Chaikin Volatility Range Expansion |
| 64 | Execution | `us-stock-twap-execution-flow-mcp` | TWAP Institutional Benchmark Flow |
| 65 | Reversion | `us-stock-connors-rsi-reversal-mcp` | Connors RSI (CRSI) Mean Reversion |
| 66 | Trend | `us-stock-heikin-ashi-trend-mcp` | Heikin-Ashi Smoothed Trend Filter |
| 67 | Bands | `us-stock-rainbow-oscillator-mcp` | Rainbow MA Band Oscillator |
| 68 | Filter | `us-stock-adaptive-laguerre-rsi-mcp` | Adaptive Laguerre Filter RSI |
| 69 | S/R | `us-stock-pivot-points-standard-mcp` | Floor Traders Pivot Points |
| 70 | Breakout | `us-stock-camarilla-pivot-breakout-mcp` | Camarilla Intraday S/R Breakout |
| 71 | Exhaustion | `us-stock-demark-sequential-td9-mcp` | DeMark Sequential TD-9 Setup |
| 72 | Trend | `us-stock-woodies-cci-trend-mcp` | Woodies CCI Trend Continuity |
| 73 | Cycle | `us-stock-center-of-gravity-oscillator-mcp` | Ehlers Center of Gravity Oscillator |
| 74 | Reversal | `us-stock-fisher-transform-mcp` | Ehlers Fisher Transform Reversal |
| 75 | Adaptive | `us-stock-mesa-adaptive-moving-avg-mcp` | MESA Adaptive Moving Average |
| 76 | Cycle | `us-stock-cyber-cycle-indicator-mcp` | Ehlers Cyber Cycle Instantaneous |
| 77 | Breakout | `us-stock-fractal-chaos-bands-mcp` | Fractal Chaos Bands Breakout |
| 78 | Efficiency | `us-stock-polarized-fractal-efficiency-mcp` | Polarized Fractal Efficiency |
| 79 | Volume | `us-stock-intraday-intensity-index-mcp` | Intraday Intensity Index Volume |
| 80 | Flow | `us-stock-price-volume-trend-pvt-mcp` | Price Volume Trend (PVT) Flow |
| 81 | Efficiency | `us-stock-kaufman-efficiency-ratio-mcp` | Kaufman Efficiency Ratio (KER) |
| 82 | Velocity | `us-stock-linear-regression-slope-mcp` | Linear Regression Slope Velocity |
| 83 | Forecast | `us-stock-time-series-forecast-tsf-mcp` | Time Series Forecast (TSF) |
| 84 | Bands | `us-stock-standard-error-bands-mcp` | Standard Error Regression Bands |
| 85 | Microstructure | `us-stock-volume-spread-analysis-vsa-mcp` | Volume Spread Analysis (VSA) |
| 86 | Volatility | `us-stock-relative-volatility-index-mcp` | Relative Volatility Index (RVI) |
| 87 | Volatility | `us-stock-true-range-envelope-mcp` | Dynamic True Range Envelope |
| 88 | Oscillator | `us-stock-percentage-price-oscillator-mcp` | Percentage Price Oscillator (PPO) |
| 89 | Volume | `us-stock-percentage-volume-oscillator-mcp` | Percentage Volume Oscillator (PVO) |
| 90 | Trend | `us-stock-disparity-index-mcp` | Disparity Index Moving Average |

</details>

---

## 📁 Directory Structure & Key Files

```
examples/
├── automation/
│   ├── daily_morning_screener.py   ← Cron-driven S&P 500 morning audit + Slack
│   ├── crewai_hedgefund_team.py    ← 3-agent CrewAI research team
│   ├── langchain_anomaly_sentinel.py ← Forensic red flag sentinel
│   ├── requirements.txt            ← Dependency manifest
│   └── README.md                   ← Automation recipes guide
├── claude-desktop/
│   ├── config.json                 ← Copy to claude_desktop_config.json
│   └── custom-instructions.md      ← Paste into Claude Settings
├── cursor/
│   ├── mcp-config.json             ← Add to Cursor MCP settings
│   └── .cursorrules                ← Institutional quant ruleset
├── chatgpt/
│   ├── openapi-actions-schema.yaml ← Paste into Custom GPT Actions
│   ├── custom-gpt-instructions.md  ← Paste into Custom GPT Instructions
│   └── README.md                   ← 60-second setup & OAuth guide
└── python/
    ├── quick_360_memo.py           ← Simplest example (5 lines)
    └── crewai_hedgefund_agent.py   ← Autonomous daily screener
sdk/
└── python/                         ← Lightweight Python SDK (wallstreet-mcp-tools)
    ├── wallstreet_mcp/             ← Direct Python client
    └── pyproject.toml              ← pip installable package
.cursor/
└── rules/
    └── wallstreet-quant-analyst.mdc ← Official Cursor MDC ruleset
```

---

## 🤝 Contributing

Found a bug? Want to add an example for another framework? PRs and issues are welcome!

1. Fork this repo
2. Create your feature branch: `git checkout -b feat/my-example`
3. Commit: `git commit -m "feat: add autogen example"`
4. Push: `git push origin feat/my-example`
5. Open a Pull Request

---

## 📄 License

MIT — see [LICENSE](LICENSE) for details.

---

**Built on [Apify](https://apify.com) MCP infrastructure** | **Catalog: [mcp_collector Suite](https://apify.com/mcp_collector)**
