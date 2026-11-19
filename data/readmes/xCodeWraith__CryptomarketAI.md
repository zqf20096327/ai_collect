# 📊 CryptomarketAI: Autonomous Market Technical Analysis Agent

[![n8n](https://img.shields.io/badge/Workflow-n8n-FF6D5A?style=for-the-badge&logo=n8n)](https://n8n.io)
[![OpenAI](https://img.shields.io/badge/Model-GPT--4o%20Vision-412991?style=for-the-badge&logo=openai)](https://openai.com/)
[![TradingView](https://img.shields.io/badge/Data-Chart--img%20API-131722?style=for-the-badge&logo=tradingview)](https://chart-img.com)
[![Telegram](https://img.shields.io/badge/Interface-Telegram%20Bot-2CA5E0?style=for-the-badge&logo=telegram)](https://telegram.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

> **Conversational AI trading agent delivering Wall Street-grade technical analysis directly on Telegram.**  
> Powered by GPT-4o Vision, LangChain memory, Chart-img API, and n8n autonomous orchestration.

---

## 🎯 Overview

Stop spending hours buried beneath multi-monitor chart setups. **CryptomarketAI** transforms a conversational Telegram bot into a 24/7 personal market analyst. Simply message `"Analyze BTCUSD"`, and the agent automatically executes an institutional-grade technical analysis pipeline:

*   **Chart-img API Integration:** Fetches high-resolution candlestick charts directly from TradingView, complete with 14-period RSI and MACD indicators.
*   **GPT-4o Vision Parsing:** Examines candlesticks, trend patterns, and momentum oscillators like an experienced human charter.
*   **Conversational Memory:** Retains chat context (last 10 interactions) using LangChain memory for contextual follow-up inquiries.
*   **Autonomous Decision-Making:** Orchestrated via a dynamic LangChain Tool-Calling Agent inside n8n.

---

## 🏗️ Architecture & Execution Flow

```
┌─────────────────────────────────────────────────────────────┐
│                      MAIN WORKFLOW                          │
│  Telegram → AI Agent (LangChain) → [fetch_chart tool] → Out │
│                     ↑                                       │
│          GPT-4o + Context Memory                            │
└─────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                   TOOL SUB-WORKFLOW                         │
│  Symbol Parser → Chart-img API → GPT-4o Vision →            │
│  → Deliver Candlestick Chart + Structured Report on Telegram│
└─────────────────────────────────────────────────────────────┘
```

| Analysis Dimension | Details |
|--------------------|---------|
| 📈 **Trend Detection** | Directional bias (Bullish / Bearish / Accumulation / Distribution) |
| 🎯 **Key Price Levels** | Immediate support and resistance barriers with high liquidity confluence |
| 📊 **Momentum Oscillators** | RSI overbought/oversold states, MACD crossovers & divergence detection |
| ⏰ **Tactical Outlook** | High-probability short-term trade scenario planning |
| 💬 **Conversational Context** | 10-message conversational buffer for persistent session dialogue |

---

## 💬 Interactive Example

```
User:
Analyze BTCUSD on 1h

Agent:
📊 BTC/USD (1H) Technical Analysis Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📍 Current Price: $96,420
📈 Directional Bias: Bullish Momentum (Ascending Channel)

🎯 Key Levels:
  • Resistance 1: $97,800 (Local high liquidity wick)
  • Resistance 2: $99,200 (Psychological breakout target)
  • Support 1:    $95,300 (20 EMA & Value Area High)
  • Support 2:    $93,800 (Ascending Trendline Confluence)

📊 Momentum Oscillators:
  • RSI (14): 62.4 — Bullish expansion with healthy room before overbought (>70)
  • MACD: Bullish crossover confirmed with expanding positive histogram

💡 Tactical Outlook:
Price consolidating above the $96,000 baseline. High probability of testing
$97,800 liquidity if hourly candles close above $96,500.

[Sent with full dark-mode TradingView 1H Candlestick Chart with RSI + MACD]
```

---

## 🚀 Quickstart & Deployment

### Step 1: Prerequisites
- **Docker Engine** (or active n8n instance)
- **Telegram Bot Token** (obtainable via [@BotFather](https://t.me/BotFather))
- **OpenAI API Key** with GPT-4o access ([OpenAI Platform](https://platform.openai.com))
- **Chart-img API Key** ([chart-img.com](https://chart-img.com))

### Step 2: Spin Up n8n
```bash
docker run -d \
  --name n8n \
  -p 5678:5678 \
  -v n8n_data:/home/node/.n8n \
  n8nio/n8n
```
Access the n8n console at `http://localhost:5678`.

### Step 3: Import Workflow
1. Navigate to **Workflows** → **Import from File**.
2. Select `xCodeWraith Market Teknik Analiz Agent AI.json`.
3. Click **Import**.

### Step 4: Configure Credentials
In **Settings → Credentials**, set up:
1. **Telegram API:** Paste your BotFather token.
2. **OpenAI API:** Paste your OpenAI secret key (`sk-...`).
3. **Chart-img API (Header Auth):**
   - Header Name: `Authorization`
   - Header Value: `Bearer YOUR_CHARTIMG_API_KEY`

### Step 5: Self-Referencing Tool Setup
This workflow utilizes a modular self-referencing sub-workflow structure:
1. Note the workflow ID in the browser URL (`http://localhost:5678/workflow/<WORKFLOW_ID>`).
2. Open the **Grafik Çek / Fetch Chart** node.
3. Select this workflow under **Workflow to Call** (either by selection or ID).
4. Save and activate the workflow toggle.

---

## 🔧 Technical Details & Chart Configuration

### Chart-img Payload Specification
```json
{
  "symbol": "BINANCE:BTCUSD",
  "interval": "1h",
  "width": 800,
  "height": 600,
  "style": "candle",
  "theme": "dark",
  "timezone": "UTC",
  "studies": [
    { "name": "RSI", "inputs": { "length": 14 } },
    { "name": "MACD" }
  ]
}
```

---

## 👨‍💻 Author

**xCodeWraith**  
GitHub: [@xCodeWraith](https://github.com/xCodeWraith)  
X (Twitter): [@DEV](https://x.com/xCodeWraith)

---

## 📜 License & Disclaimer

This project is licensed under the MIT License.

> **Disclaimer:** This software is strictly for informational, educational, and research purposes. It does not constitute financial, investment, or trading advice. Cryptocurrency trading involves substantial financial risk. The author accepts no liability for any trading losses incurred through the use of this software.
