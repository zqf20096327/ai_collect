# 👽 Marffet Investment System

🌐 [繁體中文](./README-zh-TW.md) | [简体中文](./README-zh-CN.md)

**Your AI-powered investment companion.** Backtest strategies, track your portfolio, and compete on the leaderboard — all in a sleek, cyberpunk interface.

**Built for Taiwan's ETF era.** Every listed active ETF, with its NAV and its market price always read from the *same* source on the *same* date — so the discount/premium (折溢價) in front of you is one you could actually trade on, not an artefact of two feeds drifting apart.

## 🖼️ App Preview

| Home | Mars Strategy | Compound Chart | Portfolio Insights | ETF Hub |
|:---:|:---:|:---:|:---:|:---:|
| ![Home](screenshots/en/landing.png) | ![Mars Strategy](screenshots/en/mars_strategy.png) | ![Compound](screenshots/en/compound_chart.png) | ![Portfolio](screenshots/en/portfolio_radar.png) | ![ETF Hub](screenshots/en/etf_hub.png) |

---

Marffet is a web-based investment simulation and portfolio management tool that **proves "time in the market beats timing the market."** Watch 20+ years of Taiwan stock history unfold in dynamic visualizations, compare your performance against proven strategies, and get AI-powered insights.

---

## 🚀 Getting Started

### Access the App
- **URL**: [https://marffet.zeabur.app](https://marffet.zeabur.app)
- **New address (September 2026)**: Marffet used to live at `marffet-app.zeabur.app`.
  The old address still works for now and will point you here, but please update your
  bookmarks. If you were signed in before the change, just sign in once more — your
  portfolio, holdings and history are all untouched.
- **PWA Installation Note**: When adding Marffet to your Home Screen (PWA), please ensure you do so from the Home Grid (`/`) or your desired starting page. The PWA shortcut will persistently capture and launch the specific URL you were on during installation.
- **Login Required**: To ensure peak performance and prevent heavy background loading, all features require you to **Sign in with your Google Account**.
- **Guest Mode**: Explore the simulator and visualizations without creating an account by clicking "Explore as Guest".

### First Steps
1. **Sign In** with Google
2. **Explore "Mars Strategy"** — see the top 100 stock survivors from 2006 to today
3. **Add Your Holdings** in the Portfolio tab
4. **Watch Your Race** — see your investments compete over time
5. **Customize** your profile, nickname, and settings via the ⚙️ icon

---

## 📊 Features

### 1. Mars Strategy Simulator 🪐
The core of Marffet. Simulates 20+ years of investment history to find the **Top 100 Survivors**.

- **Customizable**: Set your Start Year, Initial Capital, and Annual Contribution
- **Three Strategies**: Compare Buy-At-Opening (BAO), Buy-At-Highest (BAH), and Buy-At-Lowest (BAL)
- **Full Coverage**: TWSE stocks, TPEx/OTC, Bond ETFs (e.g., 00679B), and Convertible Bonds
- **Blazing Fast**: Results in under 200ms thanks to DuckDB + vectorized computation
- **Export**: Download Top 100 data as Excel spreadsheets

### 2. Bar Chart Race 🏎️
A dynamic animated visualization of stock performance racing over time.

- **Watch History Unfold**: See which stocks rise and fall year by year
- **Premium Feature**: CAGR metric toggle for advanced analysis

### 3. Compound Interest Calculator 💰
Simulate long-term compounding with single stocks or compare multiple assets side by side.

- **Single Mode**: Calculate compound growth for one stock with dividends reinvested
- **Comparison Mode**: Put up to 3 stocks head-to-head
- **Up-to-date dividends**: Reinvested returns and yields always reflect the latest ex-dividend events

### 4. Portfolio Tracker 📋
Manage your real investment portfolio with a sleek, "Webull-style" interface featuring full transaction history.

- **Visual Allocation**: ECharts donut charts and premium stats cards for quick insights
- **Groups**: Organize holdings into Dividend, Growth, Speculative, or custom categories
- **Transactions**: Log buys and sells with dates, shares, and prices
- **Real-Time Sync**: Pull current market data to calculate live P/L
- **Responsive UX**: 7-column stacked desktop view and cyberpunk framed mobile cards with smooth stagger animations

### 5. Portfolio Trend 📈
Your personal investment curve aligned with your transaction history.

- **Net Worth Over Time**: Visualize your portfolio growth month by month
- **Dividend Tracking**: Toggle dividend income as a separate chart layer
- **Realized & Unrealized P/L**: See both gains broken down

### 6. My Race 🏁
Your personal bar chart race — watch your own holdings compete against each other.

- **Animated Playback**: Play, pause, and scrub through time
- **Quarterly Resolution**: See shifts in your top performers each quarter

### 7. Cash Ladder (Leaderboard) 🏆
See how your ROI compares against other Marffet users.

- **Global Rankings**: Sorted by ROI percentage
- **Public Profiles**: View others' top holdings and allocation (without dollar amounts)
- **Sync Stats**: Update your ranking with one click

### 8. CB Strategy 🔧
Specialized tools for Convertible Bond investors.

- **Premium Monitoring**: Track CB premiums and identify arbitrage opportunities
- **Yield Hunter**: Alerts when premium falls below -1% (buy) or rises above 30% (sell)

### 9. ETF Hub — Active Discount/Premium Board 🪐
**The board we built because the number is so easy to get wrong.** A discount/premium (折溢價) figure only means something if the NAV and the market price come from the same source on the same date — and that is exactly what most tables quietly fail to guarantee. Ours is a focused board for Taiwan-listed **active ETFs**, built around that one rule.

- **One honest reading, or none at all**: NAV, market price and 折溢價 always arrive together, out of a single scrape. If a fund cannot form an honest pair that day, the cell shows `—`. We would rather show you nothing than a premium that isn't real.
- **Ex-rights aware, same day**: the official TWSE ex-dividend / ex-rights tables are re-crawled daily and merged upward-only, so a fund that has just gone ex-dividend is repriced in the same session instead of carrying a stale figure until the next refresh.
- **Auto-curated**: The universe is sourced from the official **TWSE/TPEx ISIN registry** (refreshed daily). When a new active ETF is listed, it shows up automatically.
- **One-glance health**: A green bar inside ±1% means the ETF is trading close to NAV. Amber means widening discount/premium worth attention.
- **Switch the lens**: Quickly flip between Active, Passive, Leveraged, and Inverse universes.
- **Free tier**: the live (frozen-close) NAV/price tuple whenever the market is closed — evenings, nights, weekends. Only *during* the 09:00–13:30 session does it fall back to yesterday's close NAV vs the same-day market close. **Premium/VIP**: live intraday tracking during the session too.

**ETF Screener** — under ETF → 洞察 (Insights), the first sub-tab. Open to everyone, no sign-in needed.

- **Filter by payout frequency**: monthly, quarterly, semiannual, annual, or no payout
- **Filter by fund type**: active, passive, market-cap, high-dividend, bond
- **Drag two sliders**: a minimum 1-year return and a minimum fund size — leave a slider at its far left for "no limit"
- **Live count**: the number of matching funds updates as you adjust; tap any result card to open that fund
- **Bookmark or share**: your filters are kept in the page address, so a filtered view can be saved or sent to a friend. **Reset** clears everything at once

**All-ETF List** — under ETF → 總覽 (Overview), also open to everyone. Every Taiwan ETF we track, organised into groups (active, bond, leveraged/inverse, futures/ETN, market-cap, high-dividend, other passive) with a count beside each group. Tap a code to open that fund.

**Every code is a link** — ETF codes shown in 每日焦點 (Daily Focus — swap radar, AUM flow, buy/sell radars, ETF concentration) and in 個股追蹤 (Stock Tracker) all open that fund's detail page. ⌘ / Ctrl / middle-click still opens a new tab as usual.

**Fund Detail Page** — needs a free account. Visitors see the fund name and code, then a prompt to register for free (Google sign-in); no payment is involved.

- **Summary strip on top**: closing price and daily change, discount/premium, dividend yield, fund size, payout frequency, and the date the numbers are from
- **Tabs below**: holdings, sector breakdown, holdings changes, and fund size
- **New shortcut**: tap any row in the 現股價格·淨值·折溢價 table to jump straight to that fund

**Holdings Buy/Sell Analysis** — on the fund detail page's 異動 (Changes) tab, for Premium members and above.

- Choose a period: today, or the last 5 / 10 / 20 / 60 trading days
- See the fund's net buying, total bought, and total sold over that period
- See the top 10 stocks it bought into and the top 10 it sold out of
- Amounts are estimated from each day's official closing price

**ETF Calculators** — the 定期定額 (regular investment) and 配息試算 (dividend estimate) tabs.

- **Type-ahead fund search**: start typing a code or a name and pick from the suggestions, instead of hunting through a long dropdown
- **Newly listed funds included**: when a fund does not yet have a full year of payout history, we show an estimate based on its current yield, clearly marked 預估 in amber

**ETF Dividend Landing Analysis (配息落點分析)** — see in which months of the year your dividends actually land.

- **Starts from what you hold**: your currently-held ETFs are pre-selected, each with a month-by-month payout row and a yearly total
- **Compare any fund**: add any ETF with a number of lots (張數) to see how it would change your monthly income mix
- **Check what you want summed**: tick or untick any row and the 已勾選加總 (selected total) row updates instantly
- **Estimates fill the gaps**: months without a realized payout are filled with estimates based on the fund's current yield (schedule-aware for quarterly and semiannual funds), clearly marked 預估 in amber — and the yearly total turns amber whenever it includes estimates
- **A confirmed ex-date never blanks out your year**: when an issuer has announced the ex-dividend date but not yet the amount (待公告), that month still shows its projected figure in amber instead of falling out of your yearly view. The realized total stays fact-only; the amber projected total carries the estimate, and it settles onto the real number the moment the issuer publishes.

### 10. Mars AI Copilot 🤖
An intelligent investment assistant powered by Google Gemini.

| | Free Tier | Premium Tier |
|:--|:--|:--|
| **Personality** | Encouraging Educator | Ruthless Wealth Manager |
| **Focus** | Explains why buy-and-hold works | Active rebalancing advice |
| **Advice** | General education | Sell overheated stocks, buy oversold ones |

---

## 💎 Membership Tiers

| Feature | Guest | FREE | PREMIUM | VIP |
|:--------|:------|:-----|:--------|:----|
| **ETF NAV / Price** | ❌ | ✅ Live after close / T-1 in session `*` | ✅ Live | ✅ Live |
| **ETF Discount/Premium (折溢價)** | ❌ | ✅ Live after close / T-1 in session `*` | ✅ Live | ✅ Live |
| **ETF Yield (殖利率)** | ❌ | ✅ | ✅ | ✅ |
| **ETF Ranking / News** | ✅ | ✅ | ✅ | ✅ |
| **ETF Screener / All-ETF List** | ✅ | ✅ | ✅ | ✅ |
| **ETF Fund Detail Page** | ❌ | ✅ | ✅ | ✅ |
| **ETF Snapshot / Delta / Overlap** | ❌ | ❌ | ✅ | ✅ |
| **ETF Holdings Buy/Sell (持股買賣超)** | ❌ | ❌ | ✅ | ✅ |
| **ETF Technicals / Compare** | ❌ | ❌ | ✅ | ✅ |
| **ETF Dividend Calendar** | ❌ | ✅ | ✅ | ✅ |
| **ETF Dividend Landing Analysis (配息落點分析)** | ❌ | ✅ | ✅ | ✅ |
| **ETF Sync-add / Add Radar / Sell Radar** | ❌ | ❌ | ❌ | ✅ |
| **Active-ETF Trust / Foreign Joint Net Buy-Sell Board** | ❌ | ❌ | ❌ | ✅ |
| Mars Strategy | ✅ | ✅ | ✅ | ✅ |
| Bar Chart Race | Basic | Basic | Advanced (CAGR) | Advanced (CAGR) |
| Compound Interest (Single) | ✅ | ✅ | ✅ | ✅ |
| Compound Interest (Comparison) | 🔒 | 🔒 | ✅ | ✅ |
| Portfolio Tracker | ✅ (Local) | ✅ | ✅ | ✅ |
| Trend Dashboard | ❌ | ✅ | ✅ | ✅ |
| Return Calendar | ❌ | ✅ | ✅ | ✅ |
| My Portfolio Race | ❌ | ✅ | ✅ | ✅ |
| Cash Ladder | ❌ | ✅ | ✅ | ✅ |
| Portfolio Groups | 3 max | 11 max | 20 max | 30 max |
| Targets per Group | 10 max | 50 max | 100 max | 200 max |
| Transactions per Target | 10 max | 100 max | 500 max | 1,000 max |
| AI Copilot | ❌ | 🎓 Educator | 🎓 Educator | 💼 Wealth Manager |
| CB Notifications | ❌ | ❌ | ✅ In-App | ✅ In-App + Email |
| Rebalancing Alerts | ❌ | ❌ | ✅ In-App | ✅ In-App + Email |
| Data Export | ❌ | 📦 Unfiltered | 📥 Filtered + 📦 Unfiltered | 📥 Filtered + 📦 Unfiltered |
| Server-Side Data | ❌ | ✅ | ✅ | ✅ |
| Priority Support | ❌ | ❌ | ❌ | ✅ |
| Early Access | ❌ | ❌ | ❌ | ✅ |

`*` **FREE's ETF freshness depends on whether the market is open, not on the tier
alone.** During the Taipei session (09:00–13:30 Mon–Fri) FREE sees T-1 and the
intraday tick is Premium/VIP-only. Every other hour — evenings, nights, weekends,
holidays — **FREE sees the same live tuple the paid tiers do**, frozen on that day's
close. Once the session ends the issuer estimate stops moving, so there is no
real-time edge left to gate. Guests see nothing at either time.

> **How to upgrade?** Go to ⚙️ Settings → Sponsor Us → choose Ko-fi or Buy Me a Coffee. Your membership will be activated!

---

## ☕ Sponsorship & Memberships

Love the Marffet Investment System? You can sponsor our development and unlock **Premium** or **VIP** features!

<a href="https://www.buymeacoffee.com/terranandes" target="_blank"><img src="frontend/public/images/bmc-yellow-button.png" alt="Buy Me A Coffee" height="50"></a>
<a href="https://ko-fi.com/terranandes" target="_blank"><img src="frontend/public/images/kofi-blue-button.png" alt="Ko-fi" height="50"></a>

1. Go to **Settings** ⚙️ and click the **Sponsor Us** tab.
2. Choose your preferred platform to sponsor.
3. Once sponsored, we will manually activate your Premium or VIP membership on your account.

---

## 🛠 Need Help?

- **Found a Bug?** Use the ⚙️ Settings panel in the app to report it
- **Feature Request?** Send your ideas through the same Settings panel
- **Questions?** Check the in-app documentation page (/doc) for a quick overview of all features

---

*Built with ❤️ by the Marffet AI Team • v5.1*
