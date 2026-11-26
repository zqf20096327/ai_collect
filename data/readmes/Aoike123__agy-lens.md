<div align="center">

<img src="assets/logo.svg" width="72" alt="Agy Lens logo">

# Agy Lens

**The all-in-one local cockpit & CLI for Antigravity 2.0.**<br>
Exact context window, live tok/s, 5-hour & weekly quotas, implied weekly quota value tracking, and subagent token spend — in one zero-dependency side panel.

[![CI](https://github.com/Aoike123/agy-lens/actions/workflows/ci.yml/badge.svg)](https://github.com/Aoike123/agy-lens/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/Aoike123/agy-lens?label=release)](https://github.com/Aoike123/agy-lens/releases/latest)
[![GitHub Stars](https://img.shields.io/github/stars/Aoike123/agy-lens?style=social)](https://github.com/Aoike123/agy-lens/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Zero dependencies](https://img.shields.io/badge/dependencies-0-brightgreen)

**English** · [简体中文](README.zh-CN.md) · [Install](#install-30-seconds) · [What you get](#what-you-get) · [Terminal CLI](#terminal-cli) · [Architecture](docs/architecture.md)

<img src="docs/img/hero-en.png" alt="Agy Lens: Overview, Quota and History tabs" width="100%">

</div>

Never get blindsided by a 5-hour wall, silent context trimming, or quiet weekly quota shrinkage again. Agy Lens reads the databases Antigravity already stores on your machine and pairs them with your local language server — zero tokens per refresh, read-only, nothing leaves your computer.

## Why Agy Lens?

| | Agy Lens | [desktop-context](https://github.com/dimitr-io/antigravity-desktop-context) | [agy-context](https://github.com/ahmetdotsh/agy-context) + [agy-usage](https://github.com/ahmetdotsh/agy-usage) | Quota-only extensions |
| --- | :---: | :---: | :---: | :---: |
| Context window by category (exact `/context` parity) | ✅ | ✅ | ✅ | — |
| Streaming tok/s, TTFT, cache hit per model | ✅ | — | partial | — |
| Official 5-hour **and** weekly quotas with countdowns | ✅ | — | — | ✅ |
| Weekly quota implied `$` value & week-over-week shrinkage tracker | ✅ | — | — | — |
| Subagent tree rollups, pruned history archive & per-project `% weekly` | ✅ | — | partial | — |
| Sanitized share card (SVG / PNG) & terminal CLI | ✅ | — | — | — |
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

Then restart Antigravity, turn on **Agy Lens** under **Customizations → Installed**, and open it from the right-side pane of any conversation.

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
- **Output speed**: streaming tok/s (outliers filtered), end-to-end speed, time to first token, cache hit rate, recent-call trend, split by model.
- **This conversation**: input, output, cache-read and thinking tokens (including live & archived subagents), estimated public-price cost, and its share of your weekly quota (`≈ X% weekly`).

### Quota: before you hit the wall (and track shrinkage)

- Official **weekly** and **5-hour** limits for each model pool reported by your plan (such as Gemini, Claude / GPT-OSS, or separate Claude Opus / Sonnet buckets, plus Tab completion), read from the app's local language server, with 20-dot meters and live reset countdowns.
- **Implied 100% quota cycle dollar value**: measures true cycle length from consecutive reset timestamps (`last reset − previous reset`, never hardcoding 7 days) and uses in-cycle sample deltas before two resets are observed — scaling partial-usage cycles by actual `%` consumed (with a 5% sample floor and pre-saturation lock so post-limit AI credits don't skew the baseline).
- **Cycle valuations & baseline diff chart**: renders an always-open per-pool adaptive `1:1` square-grid bar chart (`This month / 3 months / All`, steady height across densities) with top refresh dates, Peak + Current pool headers, reset & early-reset counts, and current-cycle baseline diff shading (coral-red caps preserving intensity depth above current for shrinkage; borderless soft green fill below current for growth), while keeping unlimited pools (such as Tab completion) cleanly below.
- **In-cycle burn-rate drill-down**: click any cycle bar to animate in-place into per-segment burn-rate phases against a weighted baseline, highlighting accelerated `≥ 1.4×` surges alongside peak concurrent conversation counts (`Up to N chats at once`), idle gaps, and off-device usage.

### History: where your tokens went

- Desktop **and** CLI conversations across `Today / 7d / 30d / All`, with **segmented time-locked weekly quota totals** that sum official per-cycle usage on each period's own scale alongside unpolled tails and earlier unrecorded calls (`exact` when 100% official, `≈` with breakdown when estimated, plus multi-pool breakdown when active), an adaptive activity heatmap, and **period-scoped model leaderboard** (`By model` updates tokens, cost, and time-locked `X% weekly` to match the selected window).
- **Pruned conversation recovery & compaction accounting**: keeps usage after Antigravity deletes old conversation databases (importing older local caches once), resolves checkpoint/compaction model enums across databases, and matches generation timestamps by response ID.
- **By session & project grouping**: top-level conversations grouped by Antigravity project (or switched to **Flat** view, with project filter pills in both **By session** and **Session list**), rolling up multi-level subagents, usage-by-level split (`self` vs `subagents`), per-pool dollar breakdown, and **time-locked per-period `≈ X% weekly` sizing** (locked to the cycle/segment prices when each project's calls ran, summing across multi-cycle projects cleanly).
- **Share card**: copy a sanitized aggregate usage card (PNG image or SVG) straight to your clipboard with **period-adaptive activity charts** (`Today` 24-hour clock chart, `7d` labeled columns, `30d` bar timeline, `All` calendar heatmap). Conversation titles and file paths are never included.

<img src="docs/img/en/share-card.png" alt="Agy Lens share card: 30-day tokens, cost, model mix as a 100-dot grid, daily activity" width="100%">

### Terminal CLI

Get the same numbers in your terminal (requires Node.js 24+):

```bash
npx github:Aoike123/agy-lens          # summary of the latest conversation + history + quota
npx github:Aoike123/agy-lens --json   # machine-readable output
```

## Privacy

- **Local by default.** All usage and quota numbers come from files and the local language server on your machine. No telemetry, no uploads.
- **Read-only.** Conversation databases are opened read-only. The app is never patched; Agy Lens only uses the official plugin/sidecar mechanism.
- **Anonymous public checks.** **Sync prices** downloads the public LiteLLM / OpenRouter price list on request, the cached release check queries GitHub Releases every 6 hours for an in-panel update banner (set `AGY_LENS_NO_UPDATE_CHECK=1` to disable), and clicking **Update now** downloads and SHA-256-verifies the official release ZIP from GitHub (set `AGY_LENS_NO_SELF_UPDATE=1` to disable in-panel updates). No credentials or local data are sent.

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

No. It never calls a model. It only reads local databases and asks the local language server for quota.

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

If Agy Lens saves you from a rate-limit surprise or helps you size your projects, **give it a ⭐ on GitHub** — it helps other Antigravity users discover it!

## License

[MIT](LICENSE). Originally derived from [dimitr-io/antigravity-desktop-context](https://github.com/dimitr-io/antigravity-desktop-context) (MIT).
