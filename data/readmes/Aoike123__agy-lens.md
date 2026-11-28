<div align="center">

<img src="assets/logo.svg" width="72" alt="Agy Lens logo">

# Agy Lens

**The all-in-one local cockpit & CLI for Antigravity 2.0.**<br>
Exact context window, live tok/s, 5-hour & weekly quotas, multi-cycle utilization & implied `$` value tracking, subagent tree spend, and 6-style WebGL/Pixel share cards — in one zero-dependency side panel.

[![CI](https://github.com/Aoike123/agy-lens/actions/workflows/ci.yml/badge.svg)](https://github.com/Aoike123/agy-lens/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/Aoike123/agy-lens?label=release)](https://github.com/Aoike123/agy-lens/releases/latest)
[![GitHub Stars](https://img.shields.io/github/stars/Aoike123/agy-lens?style=social)](https://github.com/Aoike123/agy-lens/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Zero dependencies](https://img.shields.io/badge/dependencies-0-brightgreen)

**English** · [简体中文](README.zh-CN.md) · [Install](#install-30-seconds) · [What you get](#what-you-get) · [Share Cards](#share-cards-6-styles--motion-export) · [Terminal CLI](#terminal-cli) · [Architecture](docs/architecture.md)

<img src="docs/img/hero-en.png" alt="Agy Lens: Overview, Quota and History tabs" width="100%">

</div>

Never get blindsided by a 5-hour wall, silent context trimming, quiet weekly quota shrinkage, or unstarted lazy weekly timers again. Agy Lens reads the databases Antigravity already stores on your machine and pairs them with your local language server — zero tokens per refresh, read-only by default, nothing leaves your computer.

## Why Agy Lens?

| | Agy Lens | [desktop-context](https://github.com/dimitr-io/antigravity-desktop-context) | [agy-context](https://github.com/ahmetdotsh/agy-context) + [agy-usage](https://github.com/ahmetdotsh/agy-usage) | Quota-only extensions |
| --- | :---: | :---: | :---: | :---: |
| Context window by category (exact `/context` parity) | ✅ | ✅ | ✅ | — |
| Streaming tok/s, TTFT, cache hit per model | ✅ | — | partial | — |
| Official 5-hour **and** weekly quotas with countdowns & opt-in auto-wake | ✅ | — | — | partial |
| Weekly implied `$` value, shrinkage tracker, in-cycle drill-down & multi-cycle waste (`Used / Total`) | ✅ | — | — | — |
| Project grouping, subagent tree rollups, pruned history archive & time-locked `% weekly` | ✅ | — | partial | — |
| 6-style WebGL & Pixel Hero share cards (Live Photo / MP4 / GIF / PNG / SVG) & CLI | ✅ | — | — | — |
| One-click SHA-256-verified in-panel updates | ✅ | — | — | — |
| Plugins to install | **1** | 1 | 2 | 1 |
| Runtime dependencies | **0** (built-in Node 24) | Python | 0 | IDE extension host |

## Install (30 seconds)

You only need the **Antigravity 2.0 desktop app**. It ships Node.js 24 with built-in `node:sqlite`, so there is nothing else to install.

**Windows (PowerShell)**

```powershell
irm https://raw.githubusercontent.com/Aoike123/agy-lens/main/scripts/install.ps1 | iex
```

**macOS / Linux**

```bash
curl -fsSL https://raw.githubusercontent.com/Aoike123/agy-lens/main/scripts/install.sh | bash
```

Then restart Antigravity, turn on **Agy Lens** under **Customizations → Installed**, and open it from the right-side pane of any conversation. Future releases show an in-panel **Update now** banner with automatic SHA-256 verification and atomic rollback.

<details>
<summary>Other ways to install</summary>

**Antigravity CLI**

```bash
agy plugin install https://github.com/Aoike123/agy-lens
```

**Release ZIP (no terminal):** download `agy-lens.zip` from the [latest release](https://github.com/Aoike123/agy-lens/releases/latest) and extract it so that `plugin.json` sits at:

- Windows: `%USERPROFILE%\.gemini\config\plugins\agy-lens\plugin.json`
- macOS / Linux: `~/.gemini/config/plugins/agy-lens/plugin.json`

**From source**

```bash
git clone https://github.com/Aoike123/agy-lens.git ~/.gemini/config/plugins/agy-lens
```

The installers replace the files atomically and clean up folders left by older versions, so you don't get duplicate panels.

</details>

## What you get

Each tab owns a distinct view without duplicating controls across pages:

| Overview | Quota | History |
| --- | --- | --- |
| ![Overview](docs/img/en/overview.png) | ![Quota](docs/img/en/quota.png) | ![History](docs/img/en/history.png) |

### Overview: the open conversation

- **Context window**, counted the same way as the agy CLI's `/context` from the token data Antigravity records for each model call, not estimated from characters. A 100-dot grid shows the breakdown: user messages, agent replies, tool calls, system prompt, rules, skills, MCP tools and more.
- **Request budget** warning before Antigravity starts trimming older history.
- **Output speed**: streaming tok/s (short/buffered outliers filtered), end-to-end speed, time to first token, cache hit rate, recent-call trend, split by model.
- **This conversation**: input, output, cache-read and thinking tokens (including live & archived subagents), estimated public-price cost, and its time-locked share of your weekly quota (`≈ X% weekly`).

### Quota: before you hit the wall (and see what you paid for)

- **Summary-first official limits**: reads official **weekly** and **5-hour** buckets for every pool reported by your plan (such as Gemini, Claude / GPT-OSS, or server-split Claude Opus / Sonnet buckets, plus Tab completion at the bottom) with 20-dot meters, live countdowns, and a clear **`Starts on first use`** hint when a freshly reset pool hasn't begun ticking yet.
- **Opt-in per-pool Auto-wake** *(strictly OFF by default)*: because Antigravity's weekly and 5h timers don't start counting down until the first message in a pool, you can optionally flip **Auto-wake** on per pool. When that pool resets to 100% with no countdown, Agy Lens sends **strictly 1** short tool-disabled message via the pool's cheapest model and deletes the temporary chat — protected by a persistent per-cycle circuit breaker (`pending_latched`), a 12-hour hard cooldown, and strict lock-before-send checks so it can never loop.
- **Implied 100% cycle dollar value & shrinkage tracker**: derives true cycle intervals from consecutive resets (`last reset − previous reset`, closing early resets immediately), applies LOOCV-gated empirical calibration when helpful, and renders an always-open `1:1` square-grid bar chart (`This month / 3 months / All`) with coral-red shrinkage caps and soft green growth fills against the current cycle.
- **Multi-cycle quota utilization (`Used / Total` · `Cycle left` · `Past unused`)**: beneath each pool's cycle chart, a closed-loop strip adds up total available quota across cycles (e.g. 4 cycles = `400%`), cumulative used `%`, live remaining `%`, and expired unused past quota so you can immediately tell whether you're under-using or outgrowing your plan.
- **Responsive in-cycle burn-rate drill-down**: click any cycle bar to expand in-place into variable-width burn-rate phases against a weighted baseline, highlighting `≥ 1.4×` surges, peak concurrent chats (`Up to N chats at once`), idle gaps, and off-device usage.

### History: where your tokens went

- **Segmented time-locked weekly accounting**: covers desktop **and** CLI conversations across `Today / 7d / 30d / All`, summing official per-cycle consumption on each cycle's own price scale alongside unpolled tails and earlier unrecorded calls (`exact` when 100% official, `≈` with breakdown when estimated), paired with an adaptive activity heatmap and period-scoped model leaderboard.
- **Pruned conversation recovery & compaction accounting**: preserves usage even after Antigravity deletes old conversation databases, resolves checkpoint/compaction model enums across DBs, and matches timestamps by response ID.
- **Project grouping & subagent trees**: toggle **By project / Flat** in **By session** and filter by project across **By session** and **Session list**, rolling up multi-level subagent trees (`self` vs `subagents`), per-pool USD spend, and segment-locked `≈ X% weekly` attribution.

### Share Cards: 6 styles & motion export

Open the **full-bleed Share Modal** from History to turn your `Today / 7d / 30d / All` aggregate metrics into a sanitized visual card — conversation titles and local file paths are never read or included:

- **6 curated styles with Night & Day themes**: **Mountain · Almanac**, **Abyssal · Trench**, **Eclipse · Astrolabe**, **Bauhaus · Overprint**, **Phosphor · Ribbon**, and **Pixel · Hero** (an RPG character card with 13 classes, 6 usage-derived stats, 12 unlockable achievements, and animated pixel sprites & arenas).
- **60fps WebGL1 live preview & zero-dependency motion export**: render live animated previews and export directly as **Live Photo (`.jpg`)**, **MP4**, **WebM**, **Floyd-Steinberg GIF**, **2× PNG**, or **SVG**, with one-click native OS clipboard copy.

<img src="docs/img/en/share-card.png" alt="Agy Lens 6 Share Card Styles: Mountain, Abyssal, Eclipse, Bauhaus, Phosphor, and Pixel Hero in Night and Day themes" width="100%">

### Terminal CLI

Get the same numbers in your terminal (requires Node.js 24+):

```bash
npx github:Aoike123/agy-lens          # summary of the latest conversation + history + quota
npx github:Aoike123/agy-lens --json   # machine-readable output
```

## Privacy

- **Local & read-only by default.** All usage and quota numbers come from files and the local language server on your machine. Conversation databases are opened read-only, the app is never patched, and zero telemetry or user data is ever uploaded.
- **Opt-in Auto-wake is OFF by default.** Zero model calls are made unless you explicitly turn **Auto-wake** on for a specific weekly pool, in which case it sends at most one minimal tool-disabled prompt via that pool's cheapest model on reset and cleans up the temporary conversation.
- **Anonymous public checks.** **Sync prices** downloads the public LiteLLM / OpenRouter price list on request, the cached release check queries GitHub Releases every 6 hours for the in-panel update banner (`AGY_LENS_NO_UPDATE_CHECK=1` to disable), and clicking **Update now** downloads and SHA-256-verifies the official release ZIP from GitHub (`AGY_LENS_NO_SELF_UPDATE=1` to disable). No credentials or local data are sent.

## FAQ

<details>
<summary>The panel doesn't show up under Customizations → Installed</summary>

Make sure `plugin.json` is directly inside the plugin folder (`~/.gemini/config/plugins/agy-lens/plugin.json`, not nested one level deeper), then fully restart Antigravity.

</details>

<details>
<summary>Quota says "unavailable"</summary>

Sign in to Antigravity, then turn Agy Lens off and on again so the sidecar receives the language server address and token.

</details>

<details>
<summary>Does it cost tokens or slow the agent down?</summary>

By default, **no** — it never calls a model and only reads local databases plus your local language server's quota status. Only if you explicitly enable the per-pool **Auto-wake** switch does it send one minimal prompt on the pool's cheapest model when a refreshed weekly pool has not started its countdown yet, with a per-cycle circuit breaker and 12-hour cooldown so it cannot repeat.

</details>

<details>
<summary>Are the dollar amounts or weekly % estimates my exact bill?</summary>

No. Dollar figures use public API list prices (`≈` marks same-family preview estimates), and implied weekly quota values assume official quota burn scales roughly with local public-price spend — shifts in model mix or usage on other devices can affect the weekly dollar benchmark.

</details>

## Contributing

Issues and pull requests are welcome, in English or Chinese. The architecture, data sources and protocol notes are in [docs/architecture.md](docs/architecture.md); the dev setup is in [CONTRIBUTING.md](CONTRIBUTING.md).

```bash
node --test tests/*.mjs          # unit tests
node tests/e2e/run.mjs           # end-to-end suite
node scripts/build-release.mjs   # build dist/agy-lens.zip
```

If Agy Lens saves you from a rate-limit surprise, helps you right-size your plan, or makes your usage card worth sharing, **give it a ⭐ on GitHub** — it helps other Antigravity users discover it!

## License

[MIT](LICENSE). Originally derived from [dimitr-io/antigravity-desktop-context](https://github.com/dimitr-io/antigravity-desktop-context) (MIT).
