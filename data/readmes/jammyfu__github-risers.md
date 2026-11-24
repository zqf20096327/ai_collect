**English** | [简体中文](README.zh-Hans.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

# GitHub Risers: Ranked by Stars Gained per Day

<img src=".github/social-preview.png" alt="GitHub Risers: Ranked by Stars Gained per Day" width="640">

[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![CI](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml/badge.svg)](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml) [![updated](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjammyfu%2Fgithub-risers%2Fmain%2Fdata%2Fstats.json&query=%24.today_utc&label=updated&color=brightgreen)](latest/rankings.md)

Trending GitHub repos ranked by star growth (stars gained per day), not total stars: AI first, then developer tools, security, web, infrastructure, design and data.

Data from 2026-11-23 18:49 UTC. Updated daily.

**Live boards:** [Website](https://jammyfu.github.io/github-risers/) · [Latest snapshot](latest/rankings.md)

## Use it now

1. Open the [live boards](https://jammyfu.github.io/github-risers/) — no install.
2. Or read this round's category leaders below, then the boards.
3. Each board here shows the top 10; the full top 20 is in [latest/rankings.md](latest/rankings.md).

[Website](https://jammyfu.github.io/github-risers/) · [How it works](docs/HOW_IT_WORKS.md) · [Facts](docs/FACTS.md) · [History](rankings/README.md) · [Latest](latest/rankings.md)

## Category leaders this round

| Category | #1 new (7 days) | #1 this week | #1 this month | #1 this year | #1 total stars |
|---|---|---|---|---|---|
| **[AI](#ai)** ★ primary | [EL4CTEO/fast-anything](https://github.com/EL4CTEO/fast-anything)<br>1,388/day | [morluto/rea](https://github.com/morluto/rea)<br>1,782/day | [morluto/rea](https://github.com/morluto/rea)<br>3,417/day | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>2,801/day | [morluto/rea](https://github.com/morluto/rea)<br>475,351 ★ |
| **[Developer Tools](#developer-tools)** | n/a | [astral-sh/uv](https://github.com/astral-sh/uv)<br>99.9/day | [zed-industries/zed](https://github.com/zed-industries/zed)<br>124/day | [zed-industries/zed](https://github.com/zed-industries/zed)<br>75.2/day | [oven-sh/bun](https://github.com/oven-sh/bun)<br>96,843 ★ |
| **[Security](#security)** | n/a | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>37.4/day | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>33.8/day | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>29.0/day | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>39,655 ★ |
| **[Web / Frontend](#web--frontend)** | [Johnson-Durui/ApexCluster](https://github.com/Johnson-Durui/ApexCluster)<br>32.0/day | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>173/day | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>89.3/day | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>83.0/day | [facebook/react](https://github.com/facebook/react)<br>252,905 ★ |
| **[Infrastructure](#infrastructure)** | [replit/datacat](https://github.com/replit/datacat)<br>88.8/day | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>52.3/day | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>41.3/day | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>33.7/day | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>129,346 ★ |
| **[Design / Creative](#design--creative)** | n/a | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>62.1/day | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>63.8/day | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>73.3/day | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>136,186 ★ |
| **[Data](#data)** | n/a | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>24.9/day | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>28.9/day | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>25.8/day | [apache/superset](https://github.com/apache/superset)<br>75,631 ★ |

Each board shows the top 10 here. The full top-20 lists are in [latest/rankings.md](latest/rankings.md).

Each row is one line on purpose. The full description of every project, with tool names and technical details, is in [docs/DETAILS.md](docs/DETAILS.md).

## Quick answers

### What is GitHub Risers?

A leaderboard of GitHub repos ranked by stars gained per day, not total stars. AI is the main board; six more categories follow. Built by script from the GitHub API. [Read more](docs/FAQ.md#what-is-github-risers)

### How is it different from GitHub Trending?

GitHub Trending is GitHub's own page. GitHub Risers is an independent open-source project with published rules, five languages and a saved history of every update. It is not affiliated with GitHub. [Read more](docs/FAQ.md#is-it-the-same-as-github-trending)

### How often is it updated?

Updated daily. Every run is archived. [Read more](docs/FAQ.md#how-often-is-it-updated)

### How is the data computed?

Stars gained in the last 7, 30 or 365 complete UTC days, divided by those days. All numbers come from the GitHub API; nothing is typed or estimated. [Read more](docs/FAQ.md#how-is-the-growth-rate-computed)

### How do I use or contribute?

Read the boards below, or the full top 20 in latest/. To add a tracked project, edit data/projects.json (five languages) and open a pull request. [Read more](docs/FAQ.md#how-can-i-suggest-a-project-or-report-a-mistake)

## AI

> LLMs, agents, MCP, coding copilots and generative AI

### Hottest new repos (created in the last 7 days)

| # | Project | Created (UTC) | Total stars | Stars/day |
|---|---|---|---:|---:|
| 1 | [EL4CTEO/fast-anything](https://github.com/EL4CTEO/fast-anything)<br>App running slow? Let an agent rewrite the slow 5% | 2026-11-21<br><sub>2.2 d</sub> | 3,015 | 1,387.7 |
| 2 | [erkamyaman/safe-anything](https://github.com/erkamyaman/safe-anything)<br>Find vulnerabilities before anyone else does | 2026-11-22<br><sub>1.1 d</sub> | 421 | 387.4 |
| 3 | [w01fb0ss/PiBot](https://github.com/w01fb0ss/PiBot)<br>Run an open-source, local AI agent team on your desktop | 2026-11-21<br><sub>2.5 d</sub> | 494 | 197.9 |
| 4 | [danielwh2/sprite-stacking](https://github.com/danielwh2/sprite-stacking)<br>Turn four pixel views into 3D sprites you can spin | 2026-11-20<br><sub>3.2 d</sub> | 625 | 196.7 |
| 5 | [pierridotite/mobile-agent-testers](https://github.com/pierridotite/mobile-agent-testers)<br>Find broken app flows with 20 parallel AI testers | 2026-11-16<br><sub>7.0 d</sub> | 1,363 | 195.2 |
| 6 | [INK-Q/agy-fast](https://github.com/INK-Q/agy-fast)<br>Tokens running out? Cut LLM turns and token quota | 2026-11-19<br><sub>4.6 d</sub> | 769 | 168.0 |
| 7 | [pritamux/gridlines](https://github.com/pritamux/gridlines)<br>UI misaligned? Draw guide lines and fix the padding | 2026-11-21<br><sub>2.3 d</sub> | 213 | 92.8 |
| 8 | [sous-labs/songe](https://github.com/sous-labs/songe)<br>Wasting idle compute? Use it to train your local model | 2026-11-20<br><sub>3.3 d</sub> | 291 | 87.5 |
| 9 | [JimLiu/open-artifact](https://github.com/JimLiu/open-artifact)<br>Save slides and UI designs locally as plain files | 2026-11-17<br><sub>6.7 d</sub> | 431 | 64.5 |
| 10 | [lukendeasy/open-diagram](https://github.com/lukendeasy/open-diagram)<br>Draw dense architecture diagrams that check their layout | 2026-11-18<br><sub>5.0 d</sub> | 321 | 63.5 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#EL4CTEO/fast-anything&Date"><img src="https://api.star-history.com/svg?repos=EL4CTEO/fast-anything&type=Date" width="260" alt="star history EL4CTEO/fast-anything"></a>

<a href="https://www.star-history.com/#erkamyaman/safe-anything&Date"><img src="https://api.star-history.com/svg?repos=erkamyaman/safe-anything&type=Date" width="260" alt="star history erkamyaman/safe-anything"></a>

<a href="https://www.star-history.com/#w01fb0ss/PiBot&Date"><img src="https://api.star-history.com/svg?repos=w01fb0ss/PiBot&type=Date" width="260" alt="star history w01fb0ss/PiBot"></a>

<a href="https://www.star-history.com/#danielwh2/sprite-stacking&Date"><img src="https://api.star-history.com/svg?repos=danielwh2/sprite-stacking&type=Date" width="260" alt="star history danielwh2/sprite-stacking"></a>

<a href="https://www.star-history.com/#pierridotite/mobile-agent-testers&Date"><img src="https://api.star-history.com/svg?repos=pierridotite/mobile-agent-testers&type=Date" width="260" alt="star history pierridotite/mobile-agent-testers"></a>

<a href="https://www.star-history.com/#INK-Q/agy-fast&Date"><img src="https://api.star-history.com/svg?repos=INK-Q/agy-fast&type=Date" width="260" alt="star history INK-Q/agy-fast"></a>

<a href="https://www.star-history.com/#pritamux/gridlines&Date"><img src="https://api.star-history.com/svg?repos=pritamux/gridlines&type=Date" width="260" alt="star history pritamux/gridlines"></a>

<a href="https://www.star-history.com/#sous-labs/songe&Date"><img src="https://api.star-history.com/svg?repos=sous-labs/songe&type=Date" width="260" alt="star history sous-labs/songe"></a>

<a href="https://www.star-history.com/#JimLiu/open-artifact&Date"><img src="https://api.star-history.com/svg?repos=JimLiu/open-artifact&type=Date" width="260" alt="star history JimLiu/open-artifact"></a>

<a href="https://www.star-history.com/#lukendeasy/open-diagram&Date"><img src="https://api.star-history.com/svg?repos=lukendeasy/open-diagram&type=Date" width="260" alt="star history lukendeasy/open-diagram"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>Let AI clone any software for you<br>`AI` | +12,471 | 1,781.6 | 475,351 |
| 2 | [stablyai/orca](https://github.com/stablyai/orca)<br>Several AIs write at once, see which one works best<br>`AI` | +7,659 | 1,094.1 | 134,272 |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>Less filler code from AI, the needed code done right<br>`AI` | +5,608 | 801.1 | 197,419 |
| 4 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>Give your coding AI memory, skills and safety checks<br>`AI` | +5,477 | 782.4 | 309,450 |
| 5 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>Pick plugins and build the agent you want<br>`AI` | +4,094 | 584.9 | 286,012 |
| 6 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)<br>Stop AI from making every page look the same<br>`AI` | +4,015 | 573.6 | 120,582 |
| 7 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>One AI hunts security holes, a fresh AI verifies each<br>`AI` | +3,920 | 560.0 | 77,463 |
| 8 | [anthropics/skills](https://github.com/anthropics/skills)<br>Learn to write Claude skills from the official examples<br>`AI` | +3,768 | 538.3 | 199,382 |
| 9 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>Too big to read? Start with this map of the code<br>`AI` | +3,728 | 532.6 | 152,437 |
| 10 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)<br>Can't edit video? Write it like a web page<br>`AI` | +3,708 | 529.7 | 88,818 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="star history morluto/rea"></a>

<a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="star history stablyai/orca"></a>

<a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="star history DietrichGebert/ponytail"></a>

<a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="star history affaan-m/ECC"></a>

<a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="star history deepseek-ai/deepseek-harness"></a>

<a href="https://www.star-history.com/#Leonxlnx/taste-skill&Date"><img src="https://api.star-history.com/svg?repos=Leonxlnx/taste-skill&type=Date" width="260" alt="star history Leonxlnx/taste-skill"></a>

<a href="https://www.star-history.com/#cloudflare/security-audit-skill&Date"><img src="https://api.star-history.com/svg?repos=cloudflare/security-audit-skill&type=Date" width="260" alt="star history cloudflare/security-audit-skill"></a>

<a href="https://www.star-history.com/#anthropics/skills&Date"><img src="https://api.star-history.com/svg?repos=anthropics/skills&type=Date" width="260" alt="star history anthropics/skills"></a>

<a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="star history Graphify-Labs/graphify"></a>

<a href="https://www.star-history.com/#heygen-com/hyperframes&Date"><img src="https://api.star-history.com/svg?repos=heygen-com/hyperframes&type=Date" width="260" alt="star history heygen-com/hyperframes"></a>

</details>

### Fastest rising this month (last 30 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>Let AI clone any software for you<br>`AI` | +102,509 | 3,417.0 | 475,351 |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>One AI hunts security holes, a fresh AI verifies each<br>`AI` | +34,929 | 1,164.3 | 77,463 |
| 3 | [stablyai/orca](https://github.com/stablyai/orca)<br>Several AIs write at once, see which one works best<br>`AI` | +30,105 | 1,003.5 | 134,272 |
| 4 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>Pick plugins and build the agent you want<br>`AI` | +27,432 | 914.4 | 286,012 |
| 5 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>Less filler code from AI, the needed code done right<br>`AI` | +22,910 | 763.7 | 197,419 |
| 6 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>Give your coding AI memory, skills and safety checks<br>`AI` | +22,906 | 763.5 | 309,450 |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>Swap models in your coding AI; quota runs out, it carries on<br>`AI` | +20,206 | 673.5 | 40,431 |
| 8 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)<br>Stop AI from making every page look the same<br>`AI` | +19,057 | 635.2 | 120,582 |
| 9 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>Too big to read? Start with this map of the code<br>`AI` | +18,749 | 625.0 | 152,437 |
| 10 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)<br>Can't edit video? Write it like a web page<br>`AI` | +17,879 | 596.0 | 88,818 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="star history morluto/rea"></a>

<a href="https://www.star-history.com/#cloudflare/security-audit-skill&Date"><img src="https://api.star-history.com/svg?repos=cloudflare/security-audit-skill&type=Date" width="260" alt="star history cloudflare/security-audit-skill"></a>

<a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="star history stablyai/orca"></a>

<a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="star history deepseek-ai/deepseek-harness"></a>

<a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="star history DietrichGebert/ponytail"></a>

<a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="star history affaan-m/ECC"></a>

<a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="star history yetone/magpie"></a>

<a href="https://www.star-history.com/#Leonxlnx/taste-skill&Date"><img src="https://api.star-history.com/svg?repos=Leonxlnx/taste-skill&type=Date" width="260" alt="star history Leonxlnx/taste-skill"></a>

<a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="star history Graphify-Labs/graphify"></a>

<a href="https://www.star-history.com/#heygen-com/hyperframes&Date"><img src="https://api.star-history.com/svg?repos=heygen-com/hyperframes&type=Date" width="260" alt="star history heygen-com/hyperframes"></a>

</details>

### Fastest rising this year (last 365 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>Pick plugins and build the agent you want<br>`AI` | +285,746 | 2,801.4 †<br><sub>÷102d</sub> | 286,012 |
| 2 | [morluto/rea](https://github.com/morluto/rea)<br>Let AI clone any software for you<br>`AI` | +474,555 | 2,128.0 †<br><sub>÷223d</sub> | 475,351 |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>Less filler code from AI, the needed code done right<br>`AI` | +197,073 | 1,201.7 †<br><sub>÷164d</sub> | 197,419 |
| 4 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>An AI assistant that gets things done, on your own devices<br>`AI` | +395,043 | 1,085.3 †<br><sub>÷364d</sub> | 395,097 |
| 5 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>Give your coding AI memory, skills and safety checks<br>`AI` | +309,158 | 1,000.5 †<br><sub>÷309d</sub> | 309,450 |
| 6 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>An AI helper that gets better the more you use it<br>`AI` | +265,499 | 727.4 | 265,626 |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>Swap models in your coding AI; quota runs out, it carries on<br>`AI` | +40,225 | 659.4 †<br><sub>÷61d</sub> | 40,431 |
| 8 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>Too big to read? Start with this map of the code<br>`AI` | +152,168 | 650.3 †<br><sub>÷234d</sub> | 152,437 |
| 9 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>An open-source AI that writes code in your terminal<br>`AI` | +196,429 | 538.2 | 228,778 |
| 10 | [stablyai/orca](https://github.com/stablyai/orca)<br>Several AIs write at once, see which one works best<br>`AI` | +133,511 | 531.9 †<br><sub>÷251d</sub> | 134,272 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="star history deepseek-ai/deepseek-harness"></a>

<a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="star history morluto/rea"></a>

<a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="star history DietrichGebert/ponytail"></a>

<a href="https://www.star-history.com/#openclaw/openclaw&Date"><img src="https://api.star-history.com/svg?repos=openclaw/openclaw&type=Date" width="260" alt="star history openclaw/openclaw"></a>

<a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="star history affaan-m/ECC"></a>

<a href="https://www.star-history.com/#NousResearch/hermes-agent&Date"><img src="https://api.star-history.com/svg?repos=NousResearch/hermes-agent&type=Date" width="260" alt="star history NousResearch/hermes-agent"></a>

<a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="star history yetone/magpie"></a>

<a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="star history Graphify-Labs/graphify"></a>

<a href="https://www.star-history.com/#anomalyco/opencode&Date"><img src="https://api.star-history.com/svg?repos=anomalyco/opencode&type=Date" width="260" alt="star history anomalyco/opencode"></a>

<a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="star history stablyai/orca"></a>

</details>

† The repo is younger than the window, so stars/day is divided by the repo age in days (shown under the figure) instead of the full window.

### Total stars (all time)

| # | Project | Total stars |
|---|---|---:|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>Let AI clone any software for you<br>`AI` | 475,351 |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>An AI assistant that gets things done, on your own devices<br>`AI` | 395,097 |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>Give your coding AI memory, skills and safety checks<br>`AI` | 309,450 |
| 4 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>Pick plugins and build the agent you want<br>`AI` | 286,012 |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>An AI helper that gets better the more you use it<br>`AI` | 265,626 |
| 6 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>An open-source AI that writes code in your terminal<br>`AI` | 228,778 |
| 7 | [anthropics/skills](https://github.com/anthropics/skills)<br>Learn to write Claude skills from the official examples<br>`AI` | 199,382 |
| 8 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>Less filler code from AI, the needed code done right<br>`AI` | 197,419 |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch)<br>Switch providers in one click, no config editing<br>`AI` | 156,630 |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)<br>UIs built by AI that look professionally designed<br>`AI` | 153,209 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="star history morluto/rea"></a>

<a href="https://www.star-history.com/#openclaw/openclaw&Date"><img src="https://api.star-history.com/svg?repos=openclaw/openclaw&type=Date" width="260" alt="star history openclaw/openclaw"></a>

<a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="star history affaan-m/ECC"></a>

<a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="star history deepseek-ai/deepseek-harness"></a>

<a href="https://www.star-history.com/#NousResearch/hermes-agent&Date"><img src="https://api.star-history.com/svg?repos=NousResearch/hermes-agent&type=Date" width="260" alt="star history NousResearch/hermes-agent"></a>

<a href="https://www.star-history.com/#anomalyco/opencode&Date"><img src="https://api.star-history.com/svg?repos=anomalyco/opencode&type=Date" width="260" alt="star history anomalyco/opencode"></a>

<a href="https://www.star-history.com/#anthropics/skills&Date"><img src="https://api.star-history.com/svg?repos=anthropics/skills&type=Date" width="260" alt="star history anthropics/skills"></a>

<a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="star history DietrichGebert/ponytail"></a>

<a href="https://www.star-history.com/#farion1231/cc-switch&Date"><img src="https://api.star-history.com/svg?repos=farion1231/cc-switch&type=Date" width="260" alt="star history farion1231/cc-switch"></a>

<a href="https://www.star-history.com/#nextlevelbuilder/ui-ux-pro-max-skill&Date"><img src="https://api.star-history.com/svg?repos=nextlevelbuilder/ui-ux-pro-max-skill&type=Date" width="260" alt="star history nextlevelbuilder/ui-ux-pro-max-skill"></a>

</details>

## Developer Tools

> CLIs, editors, package managers, linters and build tooling

### Hottest new repos (created in the last 7 days)

| # | Project | Created (UTC) | Total stars | Stars/day |
|---|---|---|---:|---:|
| 1 | [Adabi0304/studioonepro7-release](https://github.com/Adabi0304/studioonepro7-release)<br>Studioonepro7 desktop suite release with all features | 2026-11-21<br><sub>2.1 d</sub> | 339 | 164.0 |
| 2 | [Daax116/startall-back-utility](https://github.com/Daax116/startall-back-utility)<br>Startall Back Utility desktop customization tool | 2026-11-21<br><sub>2.1 d</sub> | 338 | 163.6 |
| 3 | [hariachayan5-dotcom/sp-flash-tool](https://github.com/hariachayan5-dotcom/sp-flash-tool)<br>SP Flash Tool command-line utility for MediaTek | 2026-11-21<br><sub>2.1 d</sub> | 338 | 163.6 |
| 4 | [cr4zyp4ul/quicken-deluxe](https://github.com/cr4zyp4ul/quicken-deluxe)<br>Quicken Deluxe desktop financial management release | 2026-11-21<br><sub>2.1 d</sub> | 338 | 163.3 |
| 5 | [official00shivansh-eng/ultra-iso](https://github.com/official00shivansh-eng/ultra-iso)<br>Ultra ISO desktop disc image toolkit | 2026-11-21<br><sub>2.1 d</sub> | 337 | 163.3 |
| 6 | [jshami391-bit/scrcpy-screen-mirroring](https://github.com/jshami391-bit/scrcpy-screen-mirroring)<br>Scrcpy Screen Mirroring display and input tool | 2026-11-21<br><sub>2.1 d</sub> | 337 | 163.0 |
| 7 | [jomicat1989-dotcom/rust-external-trainer-tool](https://github.com/jomicat1989-dotcom/rust-external-trainer-tool)<br>Rust external trainer tool, listed for game enhancement | 2026-11-21<br><sub>2.1 d</sub> | 337 | 162.9 |
| 8 | [dongarenikhilit047-star/portfolio-rebalancer](https://github.com/dongarenikhilit047-star/portfolio-rebalancer)<br>Portfolio Rebalancer desktop allocation tool | 2026-11-21<br><sub>2.1 d</sub> | 338 | 159.6 |
| 9 | [eastspaper6-cmyk/ninjatrader-bot](https://github.com/eastspaper6-cmyk/ninjatrader-bot)<br>NinjaTrader Bot for Discord and Telegram | 2026-11-21<br><sub>2.1 d</sub> | 338 | 158.2 |
| 10 | [njoniktu5/microstation-utility](https://github.com/njoniktu5/microstation-utility)<br>MicroStation Utility engineering toolset | 2026-11-21<br><sub>2.1 d</sub> | 337 | 157.0 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#Adabi0304/studioonepro7-release&Date"><img src="https://api.star-history.com/svg?repos=Adabi0304/studioonepro7-release&type=Date" width="260" alt="star history Adabi0304/studioonepro7-release"></a>

<a href="https://www.star-history.com/#Daax116/startall-back-utility&Date"><img src="https://api.star-history.com/svg?repos=Daax116/startall-back-utility&type=Date" width="260" alt="star history Daax116/startall-back-utility"></a>

<a href="https://www.star-history.com/#hariachayan5-dotcom/sp-flash-tool&Date"><img src="https://api.star-history.com/svg?repos=hariachayan5-dotcom/sp-flash-tool&type=Date" width="260" alt="star history hariachayan5-dotcom/sp-flash-tool"></a>

<a href="https://www.star-history.com/#cr4zyp4ul/quicken-deluxe&Date"><img src="https://api.star-history.com/svg?repos=cr4zyp4ul/quicken-deluxe&type=Date" width="260" alt="star history cr4zyp4ul/quicken-deluxe"></a>

<a href="https://www.star-history.com/#official00shivansh-eng/ultra-iso&Date"><img src="https://api.star-history.com/svg?repos=official00shivansh-eng/ultra-iso&type=Date" width="260" alt="star history official00shivansh-eng/ultra-iso"></a>

<a href="https://www.star-history.com/#jshami391-bit/scrcpy-screen-mirroring&Date"><img src="https://api.star-history.com/svg?repos=jshami391-bit/scrcpy-screen-mirroring&type=Date" width="260" alt="star history jshami391-bit/scrcpy-screen-mirroring"></a>

<a href="https://www.star-history.com/#jomicat1989-dotcom/rust-external-trainer-tool&Date"><img src="https://api.star-history.com/svg?repos=jomicat1989-dotcom/rust-external-trainer-tool&type=Date" width="260" alt="star history jomicat1989-dotcom/rust-external-trainer-tool"></a>

<a href="https://www.star-history.com/#dongarenikhilit047-star/portfolio-rebalancer&Date"><img src="https://api.star-history.com/svg?repos=dongarenikhilit047-star/portfolio-rebalancer&type=Date" width="260" alt="star history dongarenikhilit047-star/portfolio-rebalancer"></a>

<a href="https://www.star-history.com/#eastspaper6-cmyk/ninjatrader-bot&Date"><img src="https://api.star-history.com/svg?repos=eastspaper6-cmyk/ninjatrader-bot&type=Date" width="260" alt="star history eastspaper6-cmyk/ninjatrader-bot"></a>

<a href="https://www.star-history.com/#njoniktu5/microstation-utility&Date"><img src="https://api.star-history.com/svg?repos=njoniktu5/microstation-utility&type=Date" width="260" alt="star history njoniktu5/microstation-utility"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Install Python packages without the wait<br>`Developer Tools` | +699 | 99.9 | 92,648 |
| 2 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>Opens fast, and you can code together with others<br>`Developer Tools` | +494 | 70.6 | 95,571 |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>Dev tools, env variables and tasks, in one tool<br>`Developer Tools` | +236 | 33.7 | 36,428 |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>Search a whole folder for text, faster than grep<br>`Developer Tools` | +233 | 33.3 | 70,190 |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>Run, bundle, test, install: one tool does it all<br>`Developer Tools` | +168 | 24.0 | 96,843 |
| 6 | [cli/cli](https://github.com/cli/cli)<br>Handle GitHub from the command line, no browser<br>`Developer Tools` | +143 | 20.4 | 47,166 |
| 7 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>A text editor with language server and highlighting built in<br>`Developer Tools` | +103 | 14.7 | 46,975 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Format and check web code with one tool<br>`Developer Tools` | +78 | 11.1 | 26,186 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="star history astral-sh/uv"></a>

<a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="star history zed-industries/zed"></a>

<a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="star history jdx/mise"></a>

<a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="star history BurntSushi/ripgrep"></a>

<a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="star history oven-sh/bun"></a>

<a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="star history cli/cli"></a>

<a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="star history helix-editor/helix"></a>

<a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="star history biomejs/biome"></a>

</details>

### Fastest rising this month (last 30 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>Opens fast, and you can code together with others<br>`Developer Tools` | +3,718 | 123.9 | 95,571 |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Install Python packages without the wait<br>`Developer Tools` | +1,736 | 57.9 | 92,648 |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>Dev tools, env variables and tasks, in one tool<br>`Developer Tools` | +1,176 | 39.2 | 36,428 |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>Search a whole folder for text, faster than grep<br>`Developer Tools` | +941 | 31.4 | 70,190 |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>Run, bundle, test, install: one tool does it all<br>`Developer Tools` | +659 | 22.0 | 96,843 |
| 6 | [cli/cli](https://github.com/cli/cli)<br>Handle GitHub from the command line, no browser<br>`Developer Tools` | +494 | 16.5 | 47,166 |
| 7 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>A text editor with language server and highlighting built in<br>`Developer Tools` | +417 | 13.9 | 46,975 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Format and check web code with one tool<br>`Developer Tools` | +243 | 8.1 | 26,186 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="star history zed-industries/zed"></a>

<a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="star history astral-sh/uv"></a>

<a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="star history jdx/mise"></a>

<a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="star history BurntSushi/ripgrep"></a>

<a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="star history oven-sh/bun"></a>

<a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="star history cli/cli"></a>

<a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="star history helix-editor/helix"></a>

<a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="star history biomejs/biome"></a>

</details>

### Fastest rising this year (last 365 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>Opens fast, and you can code together with others<br>`Developer Tools` | +27,433 | 75.2 | 95,571 |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Install Python packages without the wait<br>`Developer Tools` | +20,774 | 56.9 | 92,648 |
| 3 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>Run, bundle, test, install: one tool does it all<br>`Developer Tools` | +16,520 | 45.3 | 96,843 |
| 4 | [jdx/mise](https://github.com/jdx/mise)<br>Dev tools, env variables and tasks, in one tool<br>`Developer Tools` | +15,321 | 42.0 | 36,428 |
| 5 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>Search a whole folder for text, faster than grep<br>`Developer Tools` | +13,369 | 36.6 | 70,190 |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>A text editor with language server and highlighting built in<br>`Developer Tools` | +6,433 | 17.6 | 46,975 |
| 7 | [cli/cli](https://github.com/cli/cli)<br>Handle GitHub from the command line, no browser<br>`Developer Tools` | +6,371 | 17.5 | 47,166 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Format and check web code with one tool<br>`Developer Tools` | +4,386 | 12.0 | 26,186 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="star history zed-industries/zed"></a>

<a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="star history astral-sh/uv"></a>

<a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="star history oven-sh/bun"></a>

<a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="star history jdx/mise"></a>

<a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="star history BurntSushi/ripgrep"></a>

<a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="star history helix-editor/helix"></a>

<a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="star history cli/cli"></a>

<a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="star history biomejs/biome"></a>

</details>

### Total stars (all time)

| # | Project | Total stars |
|---|---|---:|
| 1 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>Run, bundle, test, install: one tool does it all<br>`Developer Tools` | 96,843 |
| 2 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>Opens fast, and you can code together with others<br>`Developer Tools` | 95,571 |
| 3 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Install Python packages without the wait<br>`Developer Tools` | 92,648 |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>Search a whole folder for text, faster than grep<br>`Developer Tools` | 70,190 |
| 5 | [cli/cli](https://github.com/cli/cli)<br>Handle GitHub from the command line, no browser<br>`Developer Tools` | 47,166 |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>A text editor with language server and highlighting built in<br>`Developer Tools` | 46,975 |
| 7 | [jdx/mise](https://github.com/jdx/mise)<br>Dev tools, env variables and tasks, in one tool<br>`Developer Tools` | 36,428 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Format and check web code with one tool<br>`Developer Tools` | 26,186 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="star history oven-sh/bun"></a>

<a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="star history zed-industries/zed"></a>

<a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="star history astral-sh/uv"></a>

<a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="star history BurntSushi/ripgrep"></a>

<a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="star history cli/cli"></a>

<a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="star history helix-editor/helix"></a>

<a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="star history jdx/mise"></a>

<a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="star history biomejs/biome"></a>

</details>

## Security

> Vulnerability scanners, SAST, supply-chain and runtime security

### Hottest new repos (created in the last 7 days)

No new repo met the criteria in this run.

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>Scan containers and code repos for security issues at once<br>`Security` | +262 | 37.4 | 39,655 |
| 2 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>Write one template, scan for vulnerabilities in bulk<br>`Security` | +261 | 37.3 | 33,226 |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>Catch the problems in your code before you commit<br>`Security` | +185 | 26.4 | 17,909 |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>Concise cheat sheets on application security<br>`Security` | +105 | 15.0 | 34,173 |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>Are your dependencies safe? One scan tells you<br>`Security` | +70 | 10.0 | 11,603 |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>Does your container image have vulnerabilities? Scan it<br>`Security` | +61 | 8.7 | 13,338 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>Know the moment something odd happens in the cloud<br>`Security` | +23 | 3.3 | 9,603 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Scan your Go code for security problems<br>`Security` | +9 | 1.3 | 9,016 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="star history aquasecurity/trivy"></a>

<a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="star history projectdiscovery/nuclei"></a>

<a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="star history semgrep/semgrep"></a>

<a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="star history OWASP/CheatSheetSeries"></a>

<a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="star history google/osv-scanner"></a>

<a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="star history anchore/grype"></a>

<a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="star history falcosecurity/falco"></a>

<a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="star history securego/gosec"></a>

</details>

### Fastest rising this month (last 30 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>Scan containers and code repos for security issues at once<br>`Security` | +1,014 | 33.8 | 39,655 |
| 2 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>Write one template, scan for vulnerabilities in bulk<br>`Security` | +1,006 | 33.5 | 33,226 |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>Catch the problems in your code before you commit<br>`Security` | +696 | 23.2 | 17,909 |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>Concise cheat sheets on application security<br>`Security` | +478 | 15.9 | 34,173 |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>Are your dependencies safe? One scan tells you<br>`Security` | +361 | 12.0 | 11,603 |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>Does your container image have vulnerabilities? Scan it<br>`Security` | +244 | 8.1 | 13,338 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>Know the moment something odd happens in the cloud<br>`Security` | +97 | 3.2 | 9,603 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Scan your Go code for security problems<br>`Security` | +39 | 1.3 | 9,016 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="star history aquasecurity/trivy"></a>

<a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="star history projectdiscovery/nuclei"></a>

<a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="star history semgrep/semgrep"></a>

<a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="star history OWASP/CheatSheetSeries"></a>

<a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="star history google/osv-scanner"></a>

<a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="star history anchore/grype"></a>

<a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="star history falcosecurity/falco"></a>

<a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="star history securego/gosec"></a>

</details>

### Fastest rising this year (last 365 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>Scan containers and code repos for security issues at once<br>`Security` | +10,578 | 29.0 | 39,655 |
| 2 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>Write one template, scan for vulnerabilities in bulk<br>`Security` | +7,969 | 21.8 | 33,226 |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>Catch the problems in your code before you commit<br>`Security` | +4,670 | 12.8 | 17,909 |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>Concise cheat sheets on application security<br>`Security` | +3,699 | 10.1 | 34,173 |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>Are your dependencies safe? One scan tells you<br>`Security` | +3,631 | 9.9 | 11,603 |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>Does your container image have vulnerabilities? Scan it<br>`Security` | +2,415 | 6.6 | 13,338 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>Know the moment something odd happens in the cloud<br>`Security` | +1,270 | 3.5 | 9,603 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Scan your Go code for security problems<br>`Security` | +557 | 1.5 | 9,016 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="star history aquasecurity/trivy"></a>

<a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="star history projectdiscovery/nuclei"></a>

<a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="star history semgrep/semgrep"></a>

<a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="star history OWASP/CheatSheetSeries"></a>

<a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="star history google/osv-scanner"></a>

<a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="star history anchore/grype"></a>

<a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="star history falcosecurity/falco"></a>

<a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="star history securego/gosec"></a>

</details>

### Total stars (all time)

| # | Project | Total stars |
|---|---|---:|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>Scan containers and code repos for security issues at once<br>`Security` | 39,655 |
| 2 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>Concise cheat sheets on application security<br>`Security` | 34,173 |
| 3 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>Write one template, scan for vulnerabilities in bulk<br>`Security` | 33,226 |
| 4 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>Catch the problems in your code before you commit<br>`Security` | 17,909 |
| 5 | [anchore/grype](https://github.com/anchore/grype)<br>Does your container image have vulnerabilities? Scan it<br>`Security` | 13,338 |
| 6 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>Are your dependencies safe? One scan tells you<br>`Security` | 11,603 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>Know the moment something odd happens in the cloud<br>`Security` | 9,603 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Scan your Go code for security problems<br>`Security` | 9,016 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="star history aquasecurity/trivy"></a>

<a href="https://www.star-history.com/#OWASP/CheatSheetSeries&Date"><img src="https://api.star-history.com/svg?repos=OWASP/CheatSheetSeries&type=Date" width="260" alt="star history OWASP/CheatSheetSeries"></a>

<a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="star history projectdiscovery/nuclei"></a>

<a href="https://www.star-history.com/#semgrep/semgrep&Date"><img src="https://api.star-history.com/svg?repos=semgrep/semgrep&type=Date" width="260" alt="star history semgrep/semgrep"></a>

<a href="https://www.star-history.com/#anchore/grype&Date"><img src="https://api.star-history.com/svg?repos=anchore/grype&type=Date" width="260" alt="star history anchore/grype"></a>

<a href="https://www.star-history.com/#google/osv-scanner&Date"><img src="https://api.star-history.com/svg?repos=google/osv-scanner&type=Date" width="260" alt="star history google/osv-scanner"></a>

<a href="https://www.star-history.com/#falcosecurity/falco&Date"><img src="https://api.star-history.com/svg?repos=falcosecurity/falco&type=Date" width="260" alt="star history falcosecurity/falco"></a>

<a href="https://www.star-history.com/#securego/gosec&Date"><img src="https://api.star-history.com/svg?repos=securego/gosec&type=Date" width="260" alt="star history securego/gosec"></a>

</details>

## Web / Frontend

> Frontend frameworks, UI kits, CSS and browser tooling

### Hottest new repos (created in the last 7 days)

| # | Project | Created (UTC) | Total stars | Stars/day |
|---|---|---|---:|---:|
| 1 | [Johnson-Durui/ApexCluster](https://github.com/Johnson-Durui/ApexCluster)<br>Tired of writing PRDs? Let AI agents draft prototypes | 2026-11-19<br><sub>4.7 d</sub> | 151 | 32.0 |
| 2 | [chuxuan861119/zhichan-xiaozhan-work](https://github.com/chuxuan861119/zhichan-xiaozhan-work)<br>Draft and review Chinese patent filings with built-in AI | 2026-11-17<br><sub>6.3 d</sub> | 203 | 32.4 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#Johnson-Durui/ApexCluster&Date"><img src="https://api.star-history.com/svg?repos=Johnson-Durui/ApexCluster&type=Date" width="260" alt="star history Johnson-Durui/ApexCluster"></a>

<a href="https://www.star-history.com/#chuxuan861119/zhichan-xiaozhan-work&Date"><img src="https://api.star-history.com/svg?repos=chuxuan861119/zhichan-xiaozhan-work&type=Date" width="260" alt="star history chuxuan861119/zhichan-xiaozhan-work"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>A compiler turns your components into efficient web code<br>`Web / Frontend` | +1,212 | 173.1 | 89,897 |
| 2 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>Good-looking components, and the code is yours to change<br>`Web / Frontend` | +576 | 82.3 | 128,855 |
| 3 | [facebook/react](https://github.com/facebook/react)<br>Build web and native app interfaces with one library<br>`Web / Frontend` | +389 | 55.6 | 252,905 |
| 4 | [withastro/astro](https://github.com/withastro/astro)<br>For content-driven websites, with lightweight output<br>`Web / Frontend` | +184 | 26.3 | 64,151 |
| 5 | [vuejs/core](https://github.com/vuejs/core)<br>Start with one small page, learn only what you use<br>`Web / Frontend` | +184 | 26.3 | 55,152 |
| 6 | [vercel/next.js](https://github.com/vercel/next.js)<br>Build a whole site with React, front to back<br>`Web / Frontend` | +140 | 20.0 | 143,600 |
| 7 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>Custom designs without writing a pile of CSS<br>`Web / Frontend` | +123 | 17.6 | 98,693 |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>Fetching data and caching it? Leave it to this<br>`Web / Frontend` | +65 | 9.3 | 50,620 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="star history sveltejs/svelte"></a>

<a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="star history shadcn-ui/ui"></a>

<a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="star history facebook/react"></a>

<a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="star history withastro/astro"></a>

<a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="star history vuejs/core"></a>

<a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="star history vercel/next.js"></a>

<a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="star history tailwindlabs/tailwindcss"></a>

<a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="star history tanstack/query"></a>

</details>

### Fastest rising this month (last 30 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>Good-looking components, and the code is yours to change<br>`Web / Frontend` | +2,678 | 89.3 | 128,855 |
| 2 | [facebook/react](https://github.com/facebook/react)<br>Build web and native app interfaces with one library<br>`Web / Frontend` | +1,732 | 57.7 | 252,905 |
| 3 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>A compiler turns your components into efficient web code<br>`Web / Frontend` | +1,621 | 54.0 | 89,897 |
| 4 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>Custom designs without writing a pile of CSS<br>`Web / Frontend` | +926 | 30.9 | 98,693 |
| 5 | [withastro/astro](https://github.com/withastro/astro)<br>For content-driven websites, with lightweight output<br>`Web / Frontend` | +810 | 27.0 | 64,151 |
| 6 | [vercel/next.js](https://github.com/vercel/next.js)<br>Build a whole site with React, front to back<br>`Web / Frontend` | +717 | 23.9 | 143,600 |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>Start with one small page, learn only what you use<br>`Web / Frontend` | +514 | 17.1 | 55,152 |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>Fetching data and caching it? Leave it to this<br>`Web / Frontend` | +203 | 6.8 | 50,620 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="star history shadcn-ui/ui"></a>

<a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="star history facebook/react"></a>

<a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="star history sveltejs/svelte"></a>

<a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="star history tailwindlabs/tailwindcss"></a>

<a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="star history withastro/astro"></a>

<a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="star history vercel/next.js"></a>

<a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="star history vuejs/core"></a>

<a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="star history tanstack/query"></a>

</details>

### Fastest rising this year (last 365 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>Good-looking components, and the code is yours to change<br>`Web / Frontend` | +30,309 | 83.0 | 128,855 |
| 2 | [facebook/react](https://github.com/facebook/react)<br>Build web and native app interfaces with one library<br>`Web / Frontend` | +15,771 | 43.2 | 252,905 |
| 3 | [withastro/astro](https://github.com/withastro/astro)<br>For content-driven websites, with lightweight output<br>`Web / Frontend` | +10,617 | 29.1 | 64,151 |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>Build a whole site with React, front to back<br>`Web / Frontend` | +10,325 | 28.3 | 143,600 |
| 5 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>Custom designs without writing a pile of CSS<br>`Web / Frontend` | +8,869 | 24.3 | 98,693 |
| 6 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>A compiler turns your components into efficient web code<br>`Web / Frontend` | +6,245 | 17.1 | 89,897 |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>Start with one small page, learn only what you use<br>`Web / Frontend` | +3,772 | 10.3 | 55,152 |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>Fetching data and caching it? Leave it to this<br>`Web / Frontend` | +3,717 | 10.2 | 50,620 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="star history shadcn-ui/ui"></a>

<a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="star history facebook/react"></a>

<a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="star history withastro/astro"></a>

<a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="star history vercel/next.js"></a>

<a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="star history tailwindlabs/tailwindcss"></a>

<a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="star history sveltejs/svelte"></a>

<a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="star history vuejs/core"></a>

<a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="star history tanstack/query"></a>

</details>

### Total stars (all time)

| # | Project | Total stars |
|---|---|---:|
| 1 | [facebook/react](https://github.com/facebook/react)<br>Build web and native app interfaces with one library<br>`Web / Frontend` | 252,905 |
| 2 | [vercel/next.js](https://github.com/vercel/next.js)<br>Build a whole site with React, front to back<br>`Web / Frontend` | 143,600 |
| 3 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>Good-looking components, and the code is yours to change<br>`Web / Frontend` | 128,855 |
| 4 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>Custom designs without writing a pile of CSS<br>`Web / Frontend` | 98,693 |
| 5 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>A compiler turns your components into efficient web code<br>`Web / Frontend` | 89,897 |
| 6 | [withastro/astro](https://github.com/withastro/astro)<br>For content-driven websites, with lightweight output<br>`Web / Frontend` | 64,151 |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>Start with one small page, learn only what you use<br>`Web / Frontend` | 55,152 |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>Fetching data and caching it? Leave it to this<br>`Web / Frontend` | 50,620 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="star history facebook/react"></a>

<a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="star history vercel/next.js"></a>

<a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="star history shadcn-ui/ui"></a>

<a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="star history tailwindlabs/tailwindcss"></a>

<a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="star history sveltejs/svelte"></a>

<a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="star history withastro/astro"></a>

<a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="star history vuejs/core"></a>

<a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="star history tanstack/query"></a>

</details>

## Infrastructure

> Containers, Kubernetes, cloud, networking and observability

### Hottest new repos (created in the last 7 days)

| # | Project | Created (UTC) | Total stars | Stars/day |
|---|---|---|---:|---:|
| 1 | [replit/datacat](https://github.com/replit/datacat)<br>Track metrics and logs with self-hosted dashboards | 2026-11-17<br><sub>6.7 d</sub> | 592 | 88.8 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#replit/datacat&Date"><img src="https://api.star-history.com/svg?repos=replit/datacat&type=Date" width="260" alt="star history replit/datacat"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Set up a web server with HTTPS configured for you<br>`Infrastructure` | +366 | 52.3 | 79,453 |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>Lots of containers? Leave deploying and scaling to it<br>`Infrastructure` | +336 | 48.0 | 129,346 |
| 3 | [docker/compose](https://github.com/docker/compose)<br>Put many containers in one file and run them together<br>`Infrastructure` | +286 | 40.9 | 39,104 |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>When the system breaks, the alert finds you first<br>`Infrastructure` | +145 | 20.7 | 67,770 |
| 5 | [grafana/grafana](https://github.com/grafana/grafana)<br>Metrics, logs and traces on one dashboard<br>`Infrastructure` | +142 | 20.3 | 78,051 |
| 6 | [traefik/traefik](https://github.com/traefik/traefik)<br>With many services, traffic gets sorted automatically<br>`Infrastructure` | +111 | 15.9 | 65,667 |
| 7 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>Write cloud resources as code you can review and version<br>`Infrastructure` | +69 | 9.9 | 50,313 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>Manage cloud resources in a language you already know<br>`Infrastructure` | +36 | 5.1 | 25,938 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="star history caddyserver/caddy"></a>

<a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="star history kubernetes/kubernetes"></a>

<a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="star history docker/compose"></a>

<a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="star history prometheus/prometheus"></a>

<a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="star history grafana/grafana"></a>

<a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="star history traefik/traefik"></a>

<a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="star history hashicorp/terraform"></a>

<a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="star history pulumi/pulumi"></a>

</details>

### Fastest rising this month (last 30 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Set up a web server with HTTPS configured for you<br>`Infrastructure` | +1,240 | 41.3 | 79,453 |
| 2 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>When the system breaks, the alert finds you first<br>`Infrastructure` | +1,142 | 38.1 | 67,770 |
| 3 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>Lots of containers? Leave deploying and scaling to it<br>`Infrastructure` | +1,138 | 37.9 | 129,346 |
| 4 | [docker/compose](https://github.com/docker/compose)<br>Put many containers in one file and run them together<br>`Infrastructure` | +731 | 24.4 | 39,104 |
| 5 | [grafana/grafana](https://github.com/grafana/grafana)<br>Metrics, logs and traces on one dashboard<br>`Infrastructure` | +730 | 24.3 | 78,051 |
| 6 | [traefik/traefik](https://github.com/traefik/traefik)<br>With many services, traffic gets sorted automatically<br>`Infrastructure` | +410 | 13.7 | 65,667 |
| 7 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>Write cloud resources as code you can review and version<br>`Infrastructure` | +368 | 12.3 | 50,313 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>Manage cloud resources in a language you already know<br>`Infrastructure` | +162 | 5.4 | 25,938 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="star history caddyserver/caddy"></a>

<a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="star history prometheus/prometheus"></a>

<a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="star history kubernetes/kubernetes"></a>

<a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="star history docker/compose"></a>

<a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="star history grafana/grafana"></a>

<a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="star history traefik/traefik"></a>

<a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="star history hashicorp/terraform"></a>

<a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="star history pulumi/pulumi"></a>

</details>

### Fastest rising this year (last 365 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Set up a web server with HTTPS configured for you<br>`Infrastructure` | +12,297 | 33.7 | 79,453 |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>Lots of containers? Leave deploying and scaling to it<br>`Infrastructure` | +11,913 | 32.6 | 129,346 |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>Metrics, logs and traces on one dashboard<br>`Infrastructure` | +7,970 | 21.8 | 78,051 |
| 4 | [traefik/traefik](https://github.com/traefik/traefik)<br>With many services, traffic gets sorted automatically<br>`Infrastructure` | +7,399 | 20.3 | 65,667 |
| 5 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>When the system breaks, the alert finds you first<br>`Infrastructure` | +7,055 | 19.3 | 67,770 |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>Write cloud resources as code you can review and version<br>`Infrastructure` | +3,832 | 10.5 | 50,313 |
| 7 | [docker/compose](https://github.com/docker/compose)<br>Put many containers in one file and run them together<br>`Infrastructure` | +3,042 | 8.3 | 39,104 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>Manage cloud resources in a language you already know<br>`Infrastructure` | +2,095 | 5.7 | 25,938 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="star history caddyserver/caddy"></a>

<a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="star history kubernetes/kubernetes"></a>

<a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="star history grafana/grafana"></a>

<a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="star history traefik/traefik"></a>

<a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="star history prometheus/prometheus"></a>

<a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="star history hashicorp/terraform"></a>

<a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="star history docker/compose"></a>

<a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="star history pulumi/pulumi"></a>

</details>

### Total stars (all time)

| # | Project | Total stars |
|---|---|---:|
| 1 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>Lots of containers? Leave deploying and scaling to it<br>`Infrastructure` | 129,346 |
| 2 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Set up a web server with HTTPS configured for you<br>`Infrastructure` | 79,453 |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>Metrics, logs and traces on one dashboard<br>`Infrastructure` | 78,051 |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>When the system breaks, the alert finds you first<br>`Infrastructure` | 67,770 |
| 5 | [traefik/traefik](https://github.com/traefik/traefik)<br>With many services, traffic gets sorted automatically<br>`Infrastructure` | 65,667 |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>Write cloud resources as code you can review and version<br>`Infrastructure` | 50,313 |
| 7 | [docker/compose](https://github.com/docker/compose)<br>Put many containers in one file and run them together<br>`Infrastructure` | 39,104 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>Manage cloud resources in a language you already know<br>`Infrastructure` | 25,938 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="star history kubernetes/kubernetes"></a>

<a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="star history caddyserver/caddy"></a>

<a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="star history grafana/grafana"></a>

<a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="star history prometheus/prometheus"></a>

<a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="star history traefik/traefik"></a>

<a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="star history hashicorp/terraform"></a>

<a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="star history docker/compose"></a>

<a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="star history pulumi/pulumi"></a>

</details>

## Design / Creative

> Design systems, drawing, animation and creative tooling

### Hottest new repos (created in the last 7 days)

| # | Project | Created (UTC) | Total stars | Stars/day |
|---|---|---|---:|---:|
| 1 | [praseesh369/youtube-ai-video-editing-system](https://github.com/praseesh369/youtube-ai-video-editing-system)<br>AI editing workflow for YouTube | 2026-11-21<br><sub>2.1 d</sub> | 337 | 163.5 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#praseesh369/youtube-ai-video-editing-system&Date"><img src="https://api.star-history.com/svg?repos=praseesh369/youtube-ai-video-editing-system&type=Date" width="260" alt="star history praseesh369/youtube-ai-video-editing-system"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>Open it and draw, like sketching on paper<br>`Design / Creative` | +435 | 62.1 | 136,186 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>Design together as a team, on an open-source platform<br>`Design / Creative` | +275 | 39.3 | 62,665 |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>One icon set in one style, ready to use<br>`Design / Creative` | +175 | 25.0 | 25,955 |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>Diagrams and a whiteboard in one editor<br>`Design / Creative` | +141 | 20.1 | 9,532 |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Pick ready-made components for Tailwind CSS<br>`Design / Creative` | +116 | 16.6 | 42,950 |
| 6 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>Drop After Effects animations straight into web pages<br>`Design / Creative` | +83 | 11.9 | 32,555 |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>A flexible icon family for everyone<br>`Design / Creative` | +34 | 4.9 | 7,844 |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>Drop After Effects animations straight into iOS<br>`Design / Creative` | +0 | 0.0 | 43 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="star history excalidraw/excalidraw"></a>

<a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="star history penpot/penpot"></a>

<a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="star history lucide-icons/lucide"></a>

<a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="star history jgraph/drawio"></a>

<a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="star history saadeghi/daisyui"></a>

<a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="star history airbnb/lottie-web"></a>

<a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="star history phosphor-icons/homepage"></a>

<a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="star history lottiefiles/lottie-ios"></a>

</details>

### Fastest rising this month (last 30 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>Open it and draw, like sketching on paper<br>`Design / Creative` | +1,913 | 63.8 | 136,186 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>Design together as a team, on an open-source platform<br>`Design / Creative` | +1,224 | 40.8 | 62,665 |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>One icon set in one style, ready to use<br>`Design / Creative` | +756 | 25.2 | 25,955 |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>Diagrams and a whiteboard in one editor<br>`Design / Creative` | +593 | 19.8 | 9,532 |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Pick ready-made components for Tailwind CSS<br>`Design / Creative` | +372 | 12.4 | 42,950 |
| 6 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>Drop After Effects animations straight into web pages<br>`Design / Creative` | +319 | 10.6 | 32,555 |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>A flexible icon family for everyone<br>`Design / Creative` | +147 | 4.9 | 7,844 |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>Drop After Effects animations straight into iOS<br>`Design / Creative` | +0 | 0.0 | 43 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="star history excalidraw/excalidraw"></a>

<a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="star history penpot/penpot"></a>

<a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="star history lucide-icons/lucide"></a>

<a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="star history jgraph/drawio"></a>

<a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="star history saadeghi/daisyui"></a>

<a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="star history airbnb/lottie-web"></a>

<a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="star history phosphor-icons/homepage"></a>

<a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="star history lottiefiles/lottie-ios"></a>

</details>

### Fastest rising this year (last 365 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>Open it and draw, like sketching on paper<br>`Design / Creative` | +26,755 | 73.3 | 136,186 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>Design together as a team, on an open-source platform<br>`Design / Creative` | +21,809 | 59.8 | 62,665 |
| 3 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>Diagrams and a whiteboard in one editor<br>`Design / Creative` | +6,722 | 18.4 | 9,532 |
| 4 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>One icon set in one style, ready to use<br>`Design / Creative` | +6,475 | 17.7 | 25,955 |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Pick ready-made components for Tailwind CSS<br>`Design / Creative` | +4,261 | 11.7 | 42,950 |
| 6 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>A flexible icon family for everyone<br>`Design / Creative` | +2,214 | 6.1 | 7,844 |
| 7 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>Drop After Effects animations straight into web pages<br>`Design / Creative` | +1,281 | 3.5 | 32,555 |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>Drop After Effects animations straight into iOS<br>`Design / Creative` | +1 | 0.0 | 43 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="star history excalidraw/excalidraw"></a>

<a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="star history penpot/penpot"></a>

<a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="star history jgraph/drawio"></a>

<a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="star history lucide-icons/lucide"></a>

<a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="star history saadeghi/daisyui"></a>

<a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="star history phosphor-icons/homepage"></a>

<a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="star history airbnb/lottie-web"></a>

<a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="star history lottiefiles/lottie-ios"></a>

</details>

### Total stars (all time)

| # | Project | Total stars |
|---|---|---:|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>Open it and draw, like sketching on paper<br>`Design / Creative` | 136,186 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>Design together as a team, on an open-source platform<br>`Design / Creative` | 62,665 |
| 3 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Pick ready-made components for Tailwind CSS<br>`Design / Creative` | 42,950 |
| 4 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>Drop After Effects animations straight into web pages<br>`Design / Creative` | 32,555 |
| 5 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>One icon set in one style, ready to use<br>`Design / Creative` | 25,955 |
| 6 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>Diagrams and a whiteboard in one editor<br>`Design / Creative` | 9,532 |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>A flexible icon family for everyone<br>`Design / Creative` | 7,844 |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>Drop After Effects animations straight into iOS<br>`Design / Creative` | 43 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="star history excalidraw/excalidraw"></a>

<a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="star history penpot/penpot"></a>

<a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="star history saadeghi/daisyui"></a>

<a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="star history airbnb/lottie-web"></a>

<a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="star history lucide-icons/lucide"></a>

<a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="star history jgraph/drawio"></a>

<a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="star history phosphor-icons/homepage"></a>

<a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="star history lottiefiles/lottie-ios"></a>

</details>

## Data

> Databases, analytics, ETL and data engineering

### Hottest new repos (created in the last 7 days)

No new repo met the criteria in this run.

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>Run SQL analysis without setting up a database server<br>`Data` | +174 | 24.9 | 43,273 |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>Real-time analysis of huge data, with open source<br>`Data` | +138 | 19.7 | 51,081 |
| 3 | [apache/superset](https://github.com/apache/superset)<br>Can't make sense of the data? Turn it into charts<br>`Data` | +123 | 17.6 | 75,631 |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>Table data handled fast, no more waiting<br>`Data` | +113 | 16.1 | 40,460 |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>Stream events between systems on one distributed platform<br>`Data` | +44 | 6.3 | 34,252 |
| 6 | [apache/arrow](https://github.com/apache/arrow)<br>Across languages, the data works as it is<br>`Data` | +38 | 5.4 | 17,337 |
| 7 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>Transform data the way software engineers build apps<br>`Data` | +33 | 4.7 | 14,203 |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>Write code in the browser and see results as you go<br>`Data` | +10 | 1.4 | 13,480 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="star history duckdb/duckdb"></a>

<a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="star history ClickHouse/ClickHouse"></a>

<a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="star history apache/superset"></a>

<a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="star history pola-rs/polars"></a>

<a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="star history apache/kafka"></a>

<a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="star history apache/arrow"></a>

<a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="star history dbt-labs/dbt-core"></a>

<a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="star history jupyter/notebook"></a>

</details>

### Fastest rising this month (last 30 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>Run SQL analysis without setting up a database server<br>`Data` | +866 | 28.9 | 43,273 |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>Real-time analysis of huge data, with open source<br>`Data` | +574 | 19.1 | 51,081 |
| 3 | [apache/superset](https://github.com/apache/superset)<br>Can't make sense of the data? Turn it into charts<br>`Data` | +445 | 14.8 | 75,631 |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>Table data handled fast, no more waiting<br>`Data` | +329 | 11.0 | 40,460 |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>Stream events between systems on one distributed platform<br>`Data` | +260 | 8.7 | 34,252 |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>Transform data the way software engineers build apps<br>`Data` | +152 | 5.1 | 14,203 |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>Across languages, the data works as it is<br>`Data` | +133 | 4.4 | 17,337 |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>Write code in the browser and see results as you go<br>`Data` | +32 | 1.1 | 13,480 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="star history duckdb/duckdb"></a>

<a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="star history ClickHouse/ClickHouse"></a>

<a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="star history apache/superset"></a>

<a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="star history pola-rs/polars"></a>

<a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="star history apache/kafka"></a>

<a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="star history dbt-labs/dbt-core"></a>

<a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="star history apache/arrow"></a>

<a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="star history jupyter/notebook"></a>

</details>

### Fastest rising this year (last 365 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>Run SQL analysis without setting up a database server<br>`Data` | +9,414 | 25.8 | 43,273 |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>Real-time analysis of huge data, with open source<br>`Data` | +7,520 | 20.6 | 51,081 |
| 3 | [apache/superset](https://github.com/apache/superset)<br>Can't make sense of the data? Turn it into charts<br>`Data` | +7,375 | 20.2 | 75,631 |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>Table data handled fast, no more waiting<br>`Data` | +4,769 | 13.1 | 40,460 |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>Stream events between systems on one distributed platform<br>`Data` | +3,285 | 9.0 | 34,252 |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>Transform data the way software engineers build apps<br>`Data` | +2,464 | 6.8 | 14,203 |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>Across languages, the data works as it is<br>`Data` | +1,315 | 3.6 | 17,337 |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>Write code in the browser and see results as you go<br>`Data` | +860 | 2.4 | 13,480 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="star history duckdb/duckdb"></a>

<a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="star history ClickHouse/ClickHouse"></a>

<a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="star history apache/superset"></a>

<a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="star history pola-rs/polars"></a>

<a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="star history apache/kafka"></a>

<a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="star history dbt-labs/dbt-core"></a>

<a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="star history apache/arrow"></a>

<a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="star history jupyter/notebook"></a>

</details>

### Total stars (all time)

| # | Project | Total stars |
|---|---|---:|
| 1 | [apache/superset](https://github.com/apache/superset)<br>Can't make sense of the data? Turn it into charts<br>`Data` | 75,631 |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>Real-time analysis of huge data, with open source<br>`Data` | 51,081 |
| 3 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>Run SQL analysis without setting up a database server<br>`Data` | 43,273 |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>Table data handled fast, no more waiting<br>`Data` | 40,460 |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>Stream events between systems on one distributed platform<br>`Data` | 34,252 |
| 6 | [apache/arrow](https://github.com/apache/arrow)<br>Across languages, the data works as it is<br>`Data` | 17,337 |
| 7 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>Transform data the way software engineers build apps<br>`Data` | 14,203 |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>Write code in the browser and see results as you go<br>`Data` | 13,480 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#apa