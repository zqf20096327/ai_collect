**English** | [简体中文](README.zh-Hans.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

# GitHub Risers: Ranked by Stars Gained per Day

<img src=".github/social-preview.png" alt="GitHub Risers: Ranked by Stars Gained per Day" width="640">

[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![CI](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml/badge.svg)](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml) [![updated](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjammyfu%2Fgithub-risers%2Fmain%2Fdata%2Fstats.json&query=%24.today_utc&label=updated&color=brightgreen)](latest/rankings.md)

Trending GitHub repos ranked by star growth (stars gained per day), not total stars: AI first, then developer tools, security, web, infrastructure, design and data.

Data from 2026-11-22 14:56 UTC. Updated daily.

**Live boards:** [Website](https://jammyfu.github.io/github-risers/) · [Latest snapshot](latest/rankings.md)

## Use it now

1. Open the [live boards](https://jammyfu.github.io/github-risers/) — no install.
2. Or read this round's category leaders below, then the boards.
3. Each board here shows the top 10; the full top 20 is in [latest/rankings.md](latest/rankings.md).

[Website](https://jammyfu.github.io/github-risers/) · [How it works](docs/HOW_IT_WORKS.md) · [Facts](docs/FACTS.md) · [History](rankings/README.md) · [Latest](latest/rankings.md)

## Category leaders this round

| Category | #1 new (7 days) | #1 this week | #1 this month | #1 this year | #1 total stars |
|---|---|---|---|---|---|
| **[AI](#ai)** ★ primary | [erkamyaman/rust-anything](https://github.com/erkamyaman/rust-anything)<br>1,275/day | [morluto/rea](https://github.com/morluto/rea)<br>1,884/day | [morluto/rea](https://github.com/morluto/rea)<br>3,575/day | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>2,824/day | [morluto/rea](https://github.com/morluto/rea)<br>473,633 ★ |
| **[Developer Tools](#developer-tools)** | n/a | [astral-sh/uv](https://github.com/astral-sh/uv)<br>90.1/day | [zed-industries/zed](https://github.com/zed-industries/zed)<br>123/day | [zed-industries/zed](https://github.com/zed-industries/zed)<br>75.1/day | [oven-sh/bun](https://github.com/oven-sh/bun)<br>96,825 ★ |
| **[Security](#security)** | n/a | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>39.4/day | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>34.3/day | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>28.9/day | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>39,613 ★ |
| **[Web / Frontend](#web--frontend)** | [manuelgscom/inside-llm](https://github.com/manuelgscom/inside-llm)<br>17.4/day | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>172/day | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>90.3/day | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>82.9/day | [facebook/react](https://github.com/facebook/react)<br>252,903 ★ |
| **[Infrastructure](#infrastructure)** | [replit/datacat](https://github.com/replit/datacat)<br>98.1/day | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>51.0/day | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>41.5/day | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>33.6/day | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>129,355 ★ |
| **[Design / Creative](#design--creative)** | n/a | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>63.0/day | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>63.3/day | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>73.3/day | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>136,117 ★ |
| **[Data](#data)** | n/a | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>23.3/day | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>29.4/day | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>25.7/day | [apache/superset](https://github.com/apache/superset)<br>75,619 ★ |

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
| 1 | [erkamyaman/rust-anything](https://github.com/erkamyaman/rust-anything)<br>Afraid to rewrite in Rust? Migrate piece by piece safely | 2026-11-16<br><sub>6.1 d</sub> | 7,795 | 1,274.7 |
| 2 | [EL4CTEO/fast-anything](https://github.com/EL4CTEO/fast-anything)<br>App running slow? Let an agent rewrite the slow 5% | 2026-11-21<br><sub>1.0 d</sub> | 1,095 | 1,083.0 |
| 3 | [sybil-solutions/inference-optimisation-skill](https://github.com/sybil-solutions/inference-optimisation-skill)<br>Local LLM too slow? Let an agent boost serving speed | 2026-11-16<br><sub>5.8 d</sub> | 1,874 | 320.6 |
| 4 | [w01fb0ss/PiBot](https://github.com/w01fb0ss/PiBot)<br>Run an open-source, local AI agent team on your desktop | 2026-11-21<br><sub>1.3 d</sub> | 314 | 235.3 |
| 5 | [danielwh2/sprite-stacking](https://github.com/danielwh2/sprite-stacking)<br>Turn four pixel views into 3D sprites you can spin | 2026-11-20<br><sub>2.0 d</sub> | 427 | 211.8 |
| 6 | [pritamux/gridlines](https://github.com/pritamux/gridlines)<br>UI misaligned? Draw guide lines and fix the padding | 2026-11-21<br><sub>1.1 d</sub> | 156 | 137.6 |
| 7 | [boringmarketer/boring-marketing-skills](https://github.com/boringmarketer/boring-marketing-skills)<br>Give your AI agent 32 free marketing skills | 2026-11-16<br><sub>6.0 d</sub> | 790 | 131.9 |
| 8 | [INK-Q/agy-fast](https://github.com/INK-Q/agy-fast)<br>Tokens running out? Cut LLM turns and token quota | 2026-11-19<br><sub>3.4 d</sub> | 399 | 116.8 |
| 9 | [sous-labs/songe](https://github.com/sous-labs/songe)<br>Wasting idle compute? Use it to train your local model | 2026-11-20<br><sub>2.2 d</sub> | 210 | 97.1 |
| 10 | [staryone/motlab](https://github.com/staryone/motlab)<br>Want to make videos with code? Let agents build from refs | 2026-11-16<br><sub>6.0 d</sub> | 375 | 62.0 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#erkamyaman/rust-anything&Date"><img src="https://api.star-history.com/svg?repos=erkamyaman/rust-anything&type=Date" width="260" alt="star history erkamyaman/rust-anything"></a>

<a href="https://www.star-history.com/#EL4CTEO/fast-anything&Date"><img src="https://api.star-history.com/svg?repos=EL4CTEO/fast-anything&type=Date" width="260" alt="star history EL4CTEO/fast-anything"></a>

<a href="https://www.star-history.com/#sybil-solutions/inference-optimisation-skill&Date"><img src="https://api.star-history.com/svg?repos=sybil-solutions/inference-optimisation-skill&type=Date" width="260" alt="star history sybil-solutions/inference-optimisation-skill"></a>

<a href="https://www.star-history.com/#w01fb0ss/PiBot&Date"><img src="https://api.star-history.com/svg?repos=w01fb0ss/PiBot&type=Date" width="260" alt="star history w01fb0ss/PiBot"></a>

<a href="https://www.star-history.com/#danielwh2/sprite-stacking&Date"><img src="https://api.star-history.com/svg?repos=danielwh2/sprite-stacking&type=Date" width="260" alt="star history danielwh2/sprite-stacking"></a>

<a href="https://www.star-history.com/#pritamux/gridlines&Date"><img src="https://api.star-history.com/svg?repos=pritamux/gridlines&type=Date" width="260" alt="star history pritamux/gridlines"></a>

<a href="https://www.star-history.com/#boringmarketer/boring-marketing-skills&Date"><img src="https://api.star-history.com/svg?repos=boringmarketer/boring-marketing-skills&type=Date" width="260" alt="star history boringmarketer/boring-marketing-skills"></a>

<a href="https://www.star-history.com/#INK-Q/agy-fast&Date"><img src="https://api.star-history.com/svg?repos=INK-Q/agy-fast&type=Date" width="260" alt="star history INK-Q/agy-fast"></a>

<a href="https://www.star-history.com/#sous-labs/songe&Date"><img src="https://api.star-history.com/svg?repos=sous-labs/songe&type=Date" width="260" alt="star history sous-labs/songe"></a>

<a href="https://www.star-history.com/#staryone/motlab&Date"><img src="https://api.star-history.com/svg?repos=staryone/motlab&type=Date" width="260" alt="star history staryone/motlab"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>Let AI clone any software for you<br>`AI` | +13,187 | 1,883.9 | 473,633 |
| 2 | [stablyai/orca](https://github.com/stablyai/orca)<br>Several AIs write at once, see which one works best<br>`AI` | +7,247 | 1,035.3 | 132,624 |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>Less filler code from AI, the needed code done right<br>`AI` | +5,675 | 810.7 | 196,696 |
| 4 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>Give your coding AI memory, skills and safety checks<br>`AI` | +5,467 | 781.0 | 308,707 |
| 5 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>Pick plugins and build the agent you want<br>`AI` | +4,262 | 608.9 | 285,407 |
| 6 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)<br>Stop AI from making every page look the same<br>`AI` | +4,182 | 597.4 | 119,951 |
| 7 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>One AI hunts security holes, a fresh AI verifies each<br>`AI` | +4,114 | 587.7 | 76,918 |
| 8 | [anthropics/skills](https://github.com/anthropics/skills)<br>Learn to write Claude skills from the official examples<br>`AI` | +4,020 | 574.3 | 198,820 |
| 9 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>Too big to read? Start with this map of the code<br>`AI` | +3,902 | 557.4 | 151,844 |
| 10 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)<br>Can't edit video? Write it like a web page<br>`AI` | +3,594 | 513.4 | 88,089 |

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
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>Let AI clone any software for you<br>`AI` | +107,239 | 3,574.6 | 473,633 |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>One AI hunts security holes, a fresh AI verifies each<br>`AI` | +36,947 | 1,231.6 | 76,918 |
| 3 | [stablyai/orca](https://github.com/stablyai/orca)<br>Several AIs write at once, see which one works best<br>`AI` | +29,883 | 996.1 | 132,624 |
| 4 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>Pick plugins and build the agent you want<br>`AI` | +27,971 | 932.4 | 285,407 |
| 5 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>Less filler code from AI, the needed code done right<br>`AI` | +23,377 | 779.2 | 196,696 |
| 6 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>Give your coding AI memory, skills and safety checks<br>`AI` | +23,046 | 768.2 | 308,707 |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>Swap models in your coding AI; quota runs out, it carries on<br>`AI` | +20,422 | 680.7 | 39,965 |
| 8 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)<br>Stop AI from making every page look the same<br>`AI` | +19,023 | 634.1 | 119,951 |
| 9 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>Too big to read? Start with this map of the code<br>`AI` | +18,977 | 632.6 | 151,844 |
| 10 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)<br>Can't edit video? Write it like a web page<br>`AI` | +18,102 | 603.4 | 88,089 |

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
| 1 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>Pick plugins and build the agent you want<br>`AI` | +285,224 | 2,824.0 †<br><sub>÷101d</sub> | 285,407 |
| 2 | [morluto/rea](https://github.com/morluto/rea)<br>Let AI clone any software for you<br>`AI` | +473,107 | 2,131.1 †<br><sub>÷222d</sub> | 473,633 |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>Less filler code from AI, the needed code done right<br>`AI` | +196,522 | 1,205.7 †<br><sub>÷163d</sub> | 196,696 |
| 4 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>An AI assistant that gets things done, on your own devices<br>`AI` | +394,993 | 1,088.1 †<br><sub>÷363d</sub> | 395,036 |
| 5 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>Give your coding AI memory, skills and safety checks<br>`AI` | +308,514 | 1,001.7 †<br><sub>÷308d</sub> | 308,707 |
| 6 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>An AI helper that gets better the more you use it<br>`AI` | +265,251 | 726.7 | 265,335 |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>Swap models in your coding AI; quota runs out, it carries on<br>`AI` | +39,865 | 664.4 †<br><sub>÷60d</sub> | 39,965 |
| 8 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>Too big to read? Start with this map of the code<br>`AI` | +151,697 | 651.1 †<br><sub>÷233d</sub> | 151,844 |
| 9 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>An open-source AI that writes code in your terminal<br>`AI` | +196,320 | 537.9 | 228,528 |
| 10 | [stablyai/orca](https://github.com/stablyai/orca)<br>Several AIs write at once, see which one works best<br>`AI` | +132,254 | 529.0 †<br><sub>÷250d</sub> | 132,624 |

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
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>Let AI clone any software for you<br>`AI` | 473,633 |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>An AI assistant that gets things done, on your own devices<br>`AI` | 395,036 |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>Give your coding AI memory, skills and safety checks<br>`AI` | 308,707 |
| 4 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>Pick plugins and build the agent you want<br>`AI` | 285,407 |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>An AI helper that gets better the more you use it<br>`AI` | 265,335 |
| 6 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>An open-source AI that writes code in your terminal<br>`AI` | 228,528 |
| 7 | [anthropics/skills](https://github.com/anthropics/skills)<br>Learn to write Claude skills from the official examples<br>`AI` | 198,820 |
| 8 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>Less filler code from AI, the needed code done right<br>`AI` | 196,696 |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch)<br>Switch providers in one click, no config editing<br>`AI` | 156,344 |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)<br>UIs built by AI that look professionally designed<br>`AI` | 152,725 |

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
| 1 | [Adabi0304/studioonepro7-release](https://github.com/Adabi0304/studioonepro7-release)<br>Studioonepro7 desktop suite release with all features | 2026-11-21<br><sub>1.0 d</sub> | 339 | 339.0 |
| 2 | [cr4zyp4ul/quicken-deluxe](https://github.com/cr4zyp4ul/quicken-deluxe)<br>Quicken Deluxe desktop financial management release | 2026-11-21<br><sub>1.0 d</sub> | 338 | 338.0 |
| 3 | [Daax116/startall-back-utility](https://github.com/Daax116/startall-back-utility)<br>Startall Back Utility desktop customization tool | 2026-11-21<br><sub>1.0 d</sub> | 338 | 338.0 |
| 4 | [dongarenikhilit047-star/portfolio-rebalancer](https://github.com/dongarenikhilit047-star/portfolio-rebalancer)<br>Portfolio Rebalancer desktop allocation tool | 2026-11-21<br><sub>1.0 d</sub> | 338 | 338.0 |
| 5 | [eastspaper6-cmyk/ninjatrader-bot](https://github.com/eastspaper6-cmyk/ninjatrader-bot)<br>NinjaTrader Bot for Discord and Telegram | 2026-11-21<br><sub>1.0 d</sub> | 338 | 338.0 |
| 6 | [hariachayan5-dotcom/sp-flash-tool](https://github.com/hariachayan5-dotcom/sp-flash-tool)<br>SP Flash Tool command-line utility for MediaTek | 2026-11-21<br><sub>1.0 d</sub> | 338 | 338.0 |
| 7 | [ayux777/metatrader-5-bot](https://github.com/ayux777/metatrader-5-bot)<br>MetaTrader 5 bot for Discord and Telegram | 2026-11-21<br><sub>1.0 d</sub> | 337 | 337.0 |
| 8 | [jshami391-bit/scrcpy-screen-mirroring](https://github.com/jshami391-bit/scrcpy-screen-mirroring)<br>Scrcpy Screen Mirroring display and input tool | 2026-11-21<br><sub>1.0 d</sub> | 337 | 337.0 |
| 9 | [njoniktu5/microstation-utility](https://github.com/njoniktu5/microstation-utility)<br>MicroStation Utility engineering toolset | 2026-11-21<br><sub>1.0 d</sub> | 337 | 337.0 |
| 10 | [official00shivansh-eng/ultra-iso](https://github.com/official00shivansh-eng/ultra-iso)<br>Ultra ISO desktop disc image toolkit | 2026-11-21<br><sub>1.0 d</sub> | 337 | 337.0 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#Adabi0304/studioonepro7-release&Date"><img src="https://api.star-history.com/svg?repos=Adabi0304/studioonepro7-release&type=Date" width="260" alt="star history Adabi0304/studioonepro7-release"></a>

<a href="https://www.star-history.com/#cr4zyp4ul/quicken-deluxe&Date"><img src="https://api.star-history.com/svg?repos=cr4zyp4ul/quicken-deluxe&type=Date" width="260" alt="star history cr4zyp4ul/quicken-deluxe"></a>

<a href="https://www.star-history.com/#Daax116/startall-back-utility&Date"><img src="https://api.star-history.com/svg?repos=Daax116/startall-back-utility&type=Date" width="260" alt="star history Daax116/startall-back-utility"></a>

<a href="https://www.star-history.com/#dongarenikhilit047-star/portfolio-rebalancer&Date"><img src="https://api.star-history.com/svg?repos=dongarenikhilit047-star/portfolio-rebalancer&type=Date" width="260" alt="star history dongarenikhilit047-star/portfolio-rebalancer"></a>

<a href="https://www.star-history.com/#eastspaper6-cmyk/ninjatrader-bot&Date"><img src="https://api.star-history.com/svg?repos=eastspaper6-cmyk/ninjatrader-bot&type=Date" width="260" alt="star history eastspaper6-cmyk/ninjatrader-bot"></a>

<a href="https://www.star-history.com/#hariachayan5-dotcom/sp-flash-tool&Date"><img src="https://api.star-history.com/svg?repos=hariachayan5-dotcom/sp-flash-tool&type=Date" width="260" alt="star history hariachayan5-dotcom/sp-flash-tool"></a>

<a href="https://www.star-history.com/#ayux777/metatrader-5-bot&Date"><img src="https://api.star-history.com/svg?repos=ayux777/metatrader-5-bot&type=Date" width="260" alt="star history ayux777/metatrader-5-bot"></a>

<a href="https://www.star-history.com/#jshami391-bit/scrcpy-screen-mirroring&Date"><img src="https://api.star-history.com/svg?repos=jshami391-bit/scrcpy-screen-mirroring&type=Date" width="260" alt="star history jshami391-bit/scrcpy-screen-mirroring"></a>

<a href="https://www.star-history.com/#njoniktu5/microstation-utility&Date"><img src="https://api.star-history.com/svg?repos=njoniktu5/microstation-utility&type=Date" width="260" alt="star history njoniktu5/microstation-utility"></a>

<a href="https://www.star-history.com/#official00shivansh-eng/ultra-iso&Date"><img src="https://api.star-history.com/svg?repos=official00shivansh-eng/ultra-iso&type=Date" width="260" alt="star history official00shivansh-eng/ultra-iso"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Install Python packages without the wait<br>`Developer Tools` | +631 | 90.1 | 92,602 |
| 2 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>Opens fast, and you can code together with others<br>`Developer Tools` | +501 | 71.6 | 95,510 |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>Dev tools, env variables and tasks, in one tool<br>`Developer Tools` | +233 | 33.3 | 36,392 |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>Search a whole folder for text, faster than grep<br>`Developer Tools` | +205 | 29.3 | 70,137 |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>Run, bundle, test, install: one tool does it all<br>`Developer Tools` | +164 | 23.4 | 96,825 |
| 6 | [cli/cli](https://github.com/cli/cli)<br>Handle GitHub from the command line, no browser<br>`Developer Tools` | +132 | 18.9 | 47,141 |
| 7 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>A text editor with language server and highlighting built in<br>`Developer Tools` | +95 | 13.6 | 46,967 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Format and check web code with one tool<br>`Developer Tools` | +74 | 10.6 | 26,176 |

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
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>Opens fast, and you can code together with others<br>`Developer Tools` | +3,702 | 123.4 | 95,510 |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Install Python packages without the wait<br>`Developer Tools` | +1,673 | 55.8 | 92,602 |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>Dev tools, env variables and tasks, in one tool<br>`Developer Tools` | +1,173 | 39.1 | 36,392 |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>Search a whole folder for text, faster than grep<br>`Developer Tools` | +918 | 30.6 | 70,137 |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>Run, bundle, test, install: one tool does it all<br>`Developer Tools` | +655 | 21.8 | 96,825 |
| 6 | [cli/cli](https://github.com/cli/cli)<br>Handle GitHub from the command line, no browser<br>`Developer Tools` | +486 | 16.2 | 47,141 |
| 7 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>A text editor with language server and highlighting built in<br>`Developer Tools` | +403 | 13.4 | 46,967 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Format and check web code with one tool<br>`Developer Tools` | +239 | 8.0 | 26,176 |

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
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>Opens fast, and you can code together with others<br>`Developer Tools` | +27,422 | 75.1 | 95,510 |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Install Python packages without the wait<br>`Developer Tools` | +20,741 | 56.8 | 92,602 |
| 3 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>Run, bundle, test, install: one tool does it all<br>`Developer Tools` | +16,518 | 45.3 | 96,825 |
| 4 | [jdx/mise](https://github.com/jdx/mise)<br>Dev tools, env variables and tasks, in one tool<br>`Developer Tools` | +15,307 | 41.9 | 36,392 |
| 5 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>Search a whole folder for text, faster than grep<br>`Developer Tools` | +13,341 | 36.6 | 70,137 |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>A text editor with language server and highlighting built in<br>`Developer Tools` | +6,441 | 17.6 | 46,967 |
| 7 | [cli/cli](https://github.com/cli/cli)<br>Handle GitHub from the command line, no browser<br>`Developer Tools` | +6,357 | 17.4 | 47,141 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Format and check web code with one tool<br>`Developer Tools` | +4,391 | 12.0 | 26,176 |

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
| 1 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>Run, bundle, test, install: one tool does it all<br>`Developer Tools` | 96,825 |
| 2 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>Opens fast, and you can code together with others<br>`Developer Tools` | 95,510 |
| 3 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Install Python packages without the wait<br>`Developer Tools` | 92,602 |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>Search a whole folder for text, faster than grep<br>`Developer Tools` | 70,137 |
| 5 | [cli/cli](https://github.com/cli/cli)<br>Handle GitHub from the command line, no browser<br>`Developer Tools` | 47,141 |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>A text editor with language server and highlighting built in<br>`Developer Tools` | 46,967 |
| 7 | [jdx/mise](https://github.com/jdx/mise)<br>Dev tools, env variables and tasks, in one tool<br>`Developer Tools` | 36,392 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Format and check web code with one tool<br>`Developer Tools` | 26,176 |

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
| 1 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>Write one template, scan for vulnerabilities in bulk<br>`Security` | +276 | 39.4 | 33,195 |
| 2 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>Scan containers and code repos for security issues at once<br>`Security` | +266 | 38.0 | 39,613 |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>Catch the problems in your code before you commit<br>`Security` | +199 | 28.4 | 17,885 |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>Concise cheat sheets on application security<br>`Security` | +105 | 15.0 | 34,157 |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>Are your dependencies safe? One scan tells you<br>`Security` | +75 | 10.7 | 11,593 |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>Does your container image have vulnerabilities? Scan it<br>`Security` | +57 | 8.1 | 13,322 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>Know the moment something odd happens in the cloud<br>`Security` | +18 | 2.6 | 9,599 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Scan your Go code for security problems<br>`Security` | +7 | 1.0 | 9,013 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#projectdiscovery/nuclei&Date"><img src="https://api.star-history.com/svg?repos=projectdiscovery/nuclei&type=Date" width="260" alt="star history projectdiscovery/nuclei"></a>

<a href="https://www.star-history.com/#aquasecurity/trivy&Date"><img src="https://api.star-history.com/svg?repos=aquasecurity/trivy&type=Date" width="260" alt="star history aquasecurity/trivy"></a>

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
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>Scan containers and code repos for security issues at once<br>`Security` | +1,030 | 34.3 | 39,613 |
| 2 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>Write one template, scan for vulnerabilities in bulk<br>`Security` | +1,016 | 33.9 | 33,195 |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>Catch the problems in your code before you commit<br>`Security` | +713 | 23.8 | 17,885 |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>Concise cheat sheets on application security<br>`Security` | +482 | 16.1 | 34,157 |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>Are your dependencies safe? One scan tells you<br>`Security` | +363 | 12.1 | 11,593 |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>Does your container image have vulnerabilities? Scan it<br>`Security` | +244 | 8.1 | 13,322 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>Know the moment something odd happens in the cloud<br>`Security` | +97 | 3.2 | 9,599 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Scan your Go code for security problems<br>`Security` | +39 | 1.3 | 9,013 |

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
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>Scan containers and code repos for security issues at once<br>`Security` | +10,559 | 28.9 | 39,613 |
| 2 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>Write one template, scan for vulnerabilities in bulk<br>`Security` | +7,954 | 21.8 | 33,195 |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>Catch the problems in your code before you commit<br>`Security` | +4,661 | 12.8 | 17,885 |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>Concise cheat sheets on application security<br>`Security` | +3,692 | 10.1 | 34,157 |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>Are your dependencies safe? One scan tells you<br>`Security` | +3,625 | 9.9 | 11,593 |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>Does your container image have vulnerabilities? Scan it<br>`Security` | +2,418 | 6.6 | 13,322 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>Know the moment something odd happens in the cloud<br>`Security` | +1,267 | 3.5 | 9,599 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Scan your Go code for security problems<br>`Security` | +555 | 1.5 | 9,013 |

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
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>Scan containers and code repos for security issues at once<br>`Security` | 39,613 |
| 2 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>Concise cheat sheets on application security<br>`Security` | 34,157 |
| 3 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>Write one template, scan for vulnerabilities in bulk<br>`Security` | 33,195 |
| 4 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>Catch the problems in your code before you commit<br>`Security` | 17,885 |
| 5 | [anchore/grype](https://github.com/anchore/grype)<br>Does your container image have vulnerabilities? Scan it<br>`Security` | 13,322 |
| 6 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>Are your dependencies safe? One scan tells you<br>`Security` | 11,593 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>Know the moment something odd happens in the cloud<br>`Security` | 9,599 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Scan your Go code for security problems<br>`Security` | 9,013 |

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
| 1 | [manuelgscom/inside-llm](https://github.com/manuelgscom/inside-llm)<br>Browser tool for inspecting GGUF tokens and samplers | 2026-11-15<br><sub>6.8 d</sub> | 119 | 17.4 |
| 2 | [MinosoaRafalimanana/adobe-dreamweaver-varvera](https://github.com/MinosoaRafalimanana/adobe-dreamweaver-varvera)<br>Adobe Dreamweaver web development build, Varvera edition | 2026-11-18<br><sub>3.8 d</sub> | 150 | 39.2 |
| 3 | [chuxuan861119/zhichan-xiaozhan-work](https://github.com/chuxuan861119/zhichan-xiaozhan-work)<br>Draft and review Chinese patent filings with built-in AI | 2026-11-17<br><sub>5.1 d</sub> | 155 | 30.4 |
| 4 | [johnnablea29-art/stratgies-indicator](https://github.com/johnnablea29-art/stratgies-indicator)<br>Automation script for repeatable bot task runs | 2026-11-15<br><sub>6.8 d</sub> | 153 | 22.6 |
| 5 | [ELEL182/bunny-hopping-mod](https://github.com/ELEL182/bunny-hopping-mod)<br>Master momentum and movement with Fabric bunny hopping | 2026-11-15<br><sub>6.8 d</sub> | 153 | 22.5 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#manuelgscom/inside-llm&Date"><img src="https://api.star-history.com/svg?repos=manuelgscom/inside-llm&type=Date" width="260" alt="star history manuelgscom/inside-llm"></a>

<a href="https://www.star-history.com/#MinosoaRafalimanana/adobe-dreamweaver-varvera&Date"><img src="https://api.star-history.com/svg?repos=MinosoaRafalimanana/adobe-dreamweaver-varvera&type=Date" width="260" alt="star history MinosoaRafalimanana/adobe-dreamweaver-varvera"></a>

<a href="https://www.star-history.com/#chuxuan861119/zhichan-xiaozhan-work&Date"><img src="https://api.star-history.com/svg?repos=chuxuan861119/zhichan-xiaozhan-work&type=Date" width="260" alt="star history chuxuan861119/zhichan-xiaozhan-work"></a>

<a href="https://www.star-history.com/#johnnablea29-art/stratgies-indicator&Date"><img src="https://api.star-history.com/svg?repos=johnnablea29-art/stratgies-indicator&type=Date" width="260" alt="star history johnnablea29-art/stratgies-indicator"></a>

<a href="https://www.star-history.com/#ELEL182/bunny-hopping-mod&Date"><img src="https://api.star-history.com/svg?repos=ELEL182/bunny-hopping-mod&type=Date" width="260" alt="star history ELEL182/bunny-hopping-mod"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>A compiler turns your components into efficient web code<br>`Web / Frontend` | +1,206 | 172.3 | 89,895 |
| 2 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>Good-looking components, and the code is yours to change<br>`Web / Frontend` | +562 | 80.3 | 128,740 |
| 3 | [facebook/react](https://github.com/facebook/react)<br>Build web and native app interfaces with one library<br>`Web / Frontend` | +380 | 54.3 | 252,903 |
| 4 | [withastro/astro](https://github.com/withastro/astro)<br>For content-driven websites, with lightweight output<br>`Web / Frontend` | +190 | 27.1 | 64,129 |
| 5 | [vercel/next.js](https://github.com/vercel/next.js)<br>Build a whole site with React, front to back<br>`Web / Frontend` | +153 | 21.9 | 143,607 |
| 6 | [vuejs/core](https://github.com/vuejs/core)<br>Start with one small page, learn only what you use<br>`Web / Frontend` | +147 | 21.0 | 55,124 |
| 7 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>Custom designs without writing a pile of CSS<br>`Web / Frontend` | +141 | 20.1 | 98,707 |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>Fetching data and caching it? Leave it to this<br>`Web / Frontend` | +60 | 8.6 | 50,614 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="star history sveltejs/svelte"></a>

<a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="star history shadcn-ui/ui"></a>

<a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="star history facebook/react"></a>

<a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="star history withastro/astro"></a>

<a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="star history vercel/next.js"></a>

<a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="star history vuejs/core"></a>

<a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="star history tailwindlabs/tailwindcss"></a>

<a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="star history tanstack/query"></a>

</details>

### Fastest rising this month (last 30 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>Good-looking components, and the code is yours to change<br>`Web / Frontend` | +2,710 | 90.3 | 128,740 |
| 2 | [facebook/react](https://github.com/facebook/react)<br>Build web and native app interfaces with one library<br>`Web / Frontend` | +1,731 | 57.7 | 252,903 |
| 3 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>A compiler turns your components into efficient web code<br>`Web / Frontend` | +1,592 | 53.1 | 89,895 |
| 4 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>Custom designs without writing a pile of CSS<br>`Web / Frontend` | +945 | 31.5 | 98,707 |
| 5 | [withastro/astro](https://github.com/withastro/astro)<br>For content-driven websites, with lightweight output<br>`Web / Frontend` | +810 | 27.0 | 64,129 |
| 6 | [vercel/next.js](https://github.com/vercel/next.js)<br>Build a whole site with React, front to back<br>`Web / Frontend` | +746 | 24.9 | 143,607 |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>Start with one small page, learn only what you use<br>`Web / Frontend` | +478 | 15.9 | 55,124 |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>Fetching data and caching it? Leave it to this<br>`Web / Frontend` | +205 | 6.8 | 50,614 |

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
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>Good-looking components, and the code is yours to change<br>`Web / Frontend` | +30,261 | 82.9 | 128,740 |
| 2 | [facebook/react](https://github.com/facebook/react)<br>Build web and native app interfaces with one library<br>`Web / Frontend` | +15,752 | 43.2 | 252,903 |
| 3 | [withastro/astro](https://github.com/withastro/astro)<br>For content-driven websites, with lightweight output<br>`Web / Frontend` | +10,613 | 29.1 | 64,129 |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>Build a whole site with React, front to back<br>`Web / Frontend` | +10,341 | 28.3 | 143,607 |
| 5 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>Custom designs without writing a pile of CSS<br>`Web / Frontend` | +8,892 | 24.4 | 98,707 |
| 6 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>A compiler turns your components into efficient web code<br>`Web / Frontend` | +6,221 | 17.0 | 89,895 |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>Start with one small page, learn only what you use<br>`Web / Frontend` | +3,731 | 10.2 | 55,124 |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>Fetching data and caching it? Leave it to this<br>`Web / Frontend` | +3,718 | 10.2 | 50,614 |

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
| 1 | [facebook/react](https://github.com/facebook/react)<br>Build web and native app interfaces with one library<br>`Web / Frontend` | 252,903 |
| 2 | [vercel/next.js](https://github.com/vercel/next.js)<br>Build a whole site with React, front to back<br>`Web / Frontend` | 143,607 |
| 3 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>Good-looking components, and the code is yours to change<br>`Web / Frontend` | 128,740 |
| 4 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>Custom designs without writing a pile of CSS<br>`Web / Frontend` | 98,707 |
| 5 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>A compiler turns your components into efficient web code<br>`Web / Frontend` | 89,895 |
| 6 | [withastro/astro](https://github.com/withastro/astro)<br>For content-driven websites, with lightweight output<br>`Web / Frontend` | 64,129 |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>Start with one small page, learn only what you use<br>`Web / Frontend` | 55,124 |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>Fetching data and caching it? Leave it to this<br>`Web / Frontend` | 50,614 |

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
| 1 | [replit/datacat](https://github.com/replit/datacat)<br>Track metrics and logs with self-hosted dashboards | 2026-11-17<br><sub>5.5 d</sub> | 540 | 98.1 |
| 2 | [piomin/ai-software-factory](https://github.com/piomin/ai-software-factory)<br>Need an AI software factory? Run it on Kubernetes | 2026-11-18<br><sub>3.7 d</sub> | 132 | 35.9 |
| 3 | [hackclub/orchard](https://github.com/hackclub/orchard)<br>Deploying to servers is hard? Ship from Git in one command | 2026-11-17<br><sub>5.5 d</sub> | 120 | 21.9 |
| 4 | [Realmeshowroom/jet-reports-skill](https://github.com/Realmeshowroom/jet-reports-skill)<br>Visualize and organize complex workbook workflows | 2026-11-15<br><sub>6.8 d</sub> | 153 | 22.6 |
| 5 | [mmclucknorrismm/cmangos-helm](https://github.com/mmclucknorrismm/cmangos-helm)<br>Command and manage your CMaNGOS realm with Helm | 2026-11-15<br><sub>6.8 d</sub> | 153 | 22.5 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#replit/datacat&Date"><img src="https://api.star-history.com/svg?repos=replit/datacat&type=Date" width="260" alt="star history replit/datacat"></a>

<a href="https://www.star-history.com/#piomin/ai-software-factory&Date"><img src="https://api.star-history.com/svg?repos=piomin/ai-software-factory&type=Date" width="260" alt="star history piomin/ai-software-factory"></a>

<a href="https://www.star-history.com/#hackclub/orchard&Date"><img src="https://api.star-history.com/svg?repos=hackclub/orchard&type=Date" width="260" alt="star history hackclub/orchard"></a>

<a href="https://www.star-history.com/#Realmeshowroom/jet-reports-skill&Date"><img src="https://api.star-history.com/svg?repos=Realmeshowroom/jet-reports-skill&type=Date" width="260" alt="star history Realmeshowroom/jet-reports-skill"></a>

<a href="https://www.star-history.com/#mmclucknorrismm/cmangos-helm&Date"><img src="https://api.star-history.com/svg?repos=mmclucknorrismm/cmangos-helm&type=Date" width="260" alt="star history mmclucknorrismm/cmangos-helm"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Set up a web server with HTTPS configured for you<br>`Infrastructure` | +357 | 51.0 | 79,398 |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>Lots of containers? Leave deploying and scaling to it<br>`Infrastructure` | +349 | 49.9 | 129,355 |
| 3 | [docker/compose](https://github.com/docker/compose)<br>Put many containers in one file and run them together<br>`Infrastructure` | +298 | 42.6 | 39,116 |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>When the system breaks, the alert finds you first<br>`Infrastructure` | +162 | 23.1 | 67,756 |
| 5 | [grafana/grafana](https://github.com/grafana/grafana)<br>Metrics, logs and traces on one dashboard<br>`Infrastructure` | +155 | 22.1 | 78,034 |
| 6 | [traefik/traefik](https://github.com/traefik/traefik)<br>With many services, traffic gets sorted automatically<br>`Infrastructure` | +111 | 15.9 | 65,658 |
| 7 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>Write cloud resources as code you can review and version<br>`Infrastructure` | +76 | 10.9 | 50,303 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>Manage cloud resources in a language you already know<br>`Infrastructure` | +34 | 4.9 | 25,932 |

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
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Set up a web server with HTTPS configured for you<br>`Infrastructure` | +1,244 | 41.5 | 79,398 |
| 2 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>When the system breaks, the alert finds you first<br>`Infrastructure` | +1,155 | 38.5 | 67,756 |
| 3 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>Lots of containers? Leave deploying and scaling to it<br>`Infrastructure` | +1,133 | 37.8 | 129,355 |
| 4 | [grafana/grafana](https://github.com/grafana/grafana)<br>Metrics, logs and traces on one dashboard<br>`Infrastructure` | +738 | 24.6 | 78,034 |
| 5 | [docker/compose](https://github.com/docker/compose)<br>Put many containers in one file and run them together<br>`Infrastructure` | +721 | 24.0 | 39,116 |
| 6 | [traefik/traefik](https://github.com/traefik/traefik)<br>With many services, traffic gets sorted automatically<br>`Infrastructure` | +414 | 13.8 | 65,658 |
| 7 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>Write cloud resources as code you can review and version<br>`Infrastructure` | +376 | 12.5 | 50,303 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>Manage cloud resources in a language you already know<br>`Infrastructure` | +163 | 5.4 | 25,932 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="star history caddyserver/caddy"></a>

<a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="star history prometheus/prometheus"></a>

<a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="star history kubernetes/kubernetes"></a>

<a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="star history grafana/grafana"></a>

<a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="star history docker/compose"></a>

<a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="star history traefik/traefik"></a>

<a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="star history hashicorp/terraform"></a>

<a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="star history pulumi/pulumi"></a>

</details>

### Fastest rising this year (last 365 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Set up a web server with HTTPS configured for you<br>`Infrastructure` | +12,265 | 33.6 | 79,398 |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>Lots of containers? Leave deploying and scaling to it<br>`Infrastructure` | +11,897 | 32.6 | 129,355 |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>Metrics, logs and traces on one dashboard<br>`Infrastructure` | +7,968 | 21.8 | 78,034 |
| 4 | [traefik/traefik](https://github.com/traefik/traefik)<br>With many services, traffic gets sorted automatically<br>`Infrastructure` | +7,460 | 20.4 | 65,658 |
| 5 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>When the system breaks, the alert finds you first<br>`Infrastructure` | +7,063 | 19.4 | 67,756 |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>Write cloud resources as code you can review and version<br>`Infrastructure` | +3,837 | 10.5 | 50,303 |
| 7 | [docker/compose](https://github.com/docker/compose)<br>Put many containers in one file and run them together<br>`Infrastructure` | +3,027 | 8.3 | 39,116 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>Manage cloud resources in a language you already know<br>`Infrastructure` | +2,097 | 5.7 | 25,932 |

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
| 1 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>Lots of containers? Leave deploying and scaling to it<br>`Infrastructure` | 129,355 |
| 2 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Set up a web server with HTTPS configured for you<br>`Infrastructure` | 79,398 |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>Metrics, logs and traces on one dashboard<br>`Infrastructure` | 78,034 |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>When the system breaks, the alert finds you first<br>`Infrastructure` | 67,756 |
| 5 | [traefik/traefik](https://github.com/traefik/traefik)<br>With many services, traffic gets sorted automatically<br>`Infrastructure` | 65,658 |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>Write cloud resources as code you can review and version<br>`Infrastructure` | 50,303 |
| 7 | [docker/compose](https://github.com/docker/compose)<br>Put many containers in one file and run them together<br>`Infrastructure` | 39,116 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>Manage cloud resources in a language you already know<br>`Infrastructure` | 25,932 |

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
| 1 | [himeshsuthar91-eng/after-effects-ceramar-motion-design](https://github.com/himeshsuthar91-eng/after-effects-ceramar-motion-design)<br>After Effects motion design project using Ceramar methods | 2026-11-21<br><sub>1.1 d</sub> | 194 | 184.3 |
| 2 | [randrianiaina1/illustrator-datalin-vector-design](https://github.com/randrianiaina1/illustrator-datalin-vector-design)<br>Illustrator vector design workflow for structured artwork | 2026-11-20<br><sub>1.6 d</sub> | 205 | 125.4 |
| 3 | [bgleeson180-afk/cinema-4d-sacerin-motion-studio](https://github.com/bgleeson180-afk/cinema-4d-sacerin-motion-studio)<br>Cinema 4D motion scene builder with a studio workflow | 2026-11-21<br><sub>1.6 d</sub> | 201 | 124.4 |
| 4 | [124113009-art/adobe-fresco-elrina](https://github.com/124113009-art/adobe-fresco-elrina)<br>Visual guides for Adobe Fresco Elrina brushes and tools | 2026-11-19<br><sub>2.6 d</sub> | 150 | 56.9 |
| 5 | [SPAPharma/adobe-animate-velvona](https://github.com/SPAPharma/adobe-animate-velvona)<br>Animation creation and refinement tools for Adobe Animate | 2026-11-19<br><sub>2.6 d</sub> | 148 | 56.0 |
| 6 | [Anais27-pharma/adobe-character-animator-calrara](https://github.com/Anais27-pharma/adobe-character-animator-calrara)<br>Real-time puppet animation with webcam and audio input | 2026-11-19<br><sub>2.6 d</sub> | 147 | 55.7 |
| 7 | [charaf24/substance-3d-designer-norlora](https://github.com/charaf24/substance-3d-designer-norlora)<br>Node-based texturing workflow for procedural 3D materials | 2026-11-18<br><sub>3.7 d</sub> | 150 | 40.3 |
| 8 | [tarouquelaprogramacao-max/krita-elvona-art-studio](https://github.com/tarouquelaprogramacao-max/krita-elvona-art-studio)<br>Krita plugin that builds art studio workspaces | 2026-11-18<br><sub>4.0 d</sub> | 151 | 37.5 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#himeshsuthar91-eng/after-effects-ceramar-motion-design&Date"><img src="https://api.star-history.com/svg?repos=himeshsuthar91-eng/after-effects-ceramar-motion-design&type=Date" width="260" alt="star history himeshsuthar91-eng/after-effects-ceramar-motion-design"></a>

<a href="https://www.star-history.com/#randrianiaina1/illustrator-datalin-vector-design&Date"><img src="https://api.star-history.com/svg?repos=randrianiaina1/illustrator-datalin-vector-design&type=Date" width="260" alt="star history randrianiaina1/illustrator-datalin-vector-design"></a>

<a href="https://www.star-history.com/#bgleeson180-afk/cinema-4d-sacerin-motion-studio&Date"><img src="https://api.star-history.com/svg?repos=bgleeson180-afk/cinema-4d-sacerin-motion-studio&type=Date" width="260" alt="star history bgleeson180-afk/cinema-4d-sacerin-motion-studio"></a>

<a href="https://www.star-history.com/#124113009-art/adobe-fresco-elrina&Date"><img src="https://api.star-history.com/svg?repos=124113009-art/adobe-fresco-elrina&type=Date" width="260" alt="star history 124113009-art/adobe-fresco-elrina"></a>

<a href="https://www.star-history.com/#SPAPharma/adobe-animate-velvona&Date"><img src="https://api.star-history.com/svg?repos=SPAPharma/adobe-animate-velvona&type=Date" width="260" alt="star history SPAPharma/adobe-animate-velvona"></a>

<a href="https://www.star-history.com/#Anais27-pharma/adobe-character-animator-calrara&Date"><img src="https://api.star-history.com/svg?repos=Anais27-pharma/adobe-character-animator-calrara&type=Date" width="260" alt="star history Anais27-pharma/adobe-character-animator-calrara"></a>

<a href="https://www.star-history.com/#charaf24/substance-3d-designer-norlora&Date"><img src="https://api.star-history.com/svg?repos=charaf24/substance-3d-designer-norlora&type=Date" width="260" alt="star history charaf24/substance-3d-designer-norlora"></a>

<a href="https://www.star-history.com/#tarouquelaprogramacao-max/krita-elvona-art-studio&Date"><img src="https://api.star-history.com/svg?repos=tarouquelaprogramacao-max/krita-elvona-art-studio&type=Date" width="260" alt="star history tarouquelaprogramacao-max/krita-elvona-art-studio"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>Open it and draw, like sketching on paper<br>`Design / Creative` | +441 | 63.0 | 136,117 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>Design together as a team, on an open-source platform<br>`Design / Creative` | +288 | 41.1 | 62,634 |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>One icon set in one style, ready to use<br>`Design / Creative` | +176 | 25.1 | 25,932 |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>Diagrams and a whiteboard in one editor<br>`Design / Creative` | +142 | 20.3 | 9,512 |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Pick ready-made components for Tailwind CSS<br>`Design / Creative` | +105 | 15.0 | 42,928 |
| 6 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>Drop After Effects animations straight into web pages<br>`Design / Creative` | +97 | 13.9 | 32,543 |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>A flexible icon family for everyone<br>`Design / Creative` | +33 | 4.7 | 7,838 |
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
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>Open it and draw, like sketching on paper<br>`Design / Creative` | +1,900 | 63.3 | 136,117 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>Design together as a team, on an open-source platform<br>`Design / Creative` | +1,247 | 41.6 | 62,634 |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>One icon set in one style, ready to use<br>`Design / Creative` | +755 | 25.2 | 25,932 |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>Diagrams and a whiteboard in one editor<br>`Design / Creative` | +593 | 19.8 | 9,512 |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Pick ready-made components for Tailwind CSS<br>`Design / Creative` | +359 | 12.0 | 42,928 |
| 6 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>Drop After Effects animations straight into web pages<br>`Design / Creative` | +311 | 10.4 | 32,543 |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>A flexible icon family for everyone<br>`Design / Creative` | +151 | 5.0 | 7,838 |
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
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>Open it and draw, like sketching on paper<br>`Design / Creative` | +26,758 | 73.3 | 136,117 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>Design together as a team, on an open-source platform<br>`Design / Creative` | +21,791 | 59.7 | 62,634 |
| 3 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>Diagrams and a whiteboard in one editor<br>`Design / Creative` | +6,710 | 18.4 | 9,512 |
| 4 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>One icon set in one style, ready to use<br>`Design / Creative` | +6,463 | 17.7 | 25,932 |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Pick ready-made components for Tailwind CSS<br>`Design / Creative` | +4,249 | 11.6 | 42,928 |
| 6 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>A flexible icon family for everyone<br>`Design / Creative` | +2,212 | 6.1 | 7,838 |
| 7 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>Drop After Effects animations straight into web pages<br>`Design / Creative` | +1,272 | 3.5 | 32,543 |
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
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>Open it and draw, like sketching on paper<br>`Design / Creative` | 136,117 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>Design together as a team, on an open-source platform<br>`Design / Creative` | 62,634 |
| 3 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Pick ready-made components for Tailwind CSS<br>`Design / Creative` | 42,928 |
| 4 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>Drop After Effects animations straight into web pages<br>`Design / Creative` | 32,543 |
| 5 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>One icon set in one style, ready to use<br>`Design / Creative` | 25,932 |
| 6 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>Diagrams and a whiteboard in one editor<br>`Design / Creative` | 9,512 |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>A flexible icon family for everyone<br>`Design / Creative` | 7,838 |
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

| # | Project | Created (UTC) | Total stars | Stars/day |
|---|---|---|---:|---:|
| 1 | [aurahamzzz-cyber/microsoft-excel-alvaora](https://github.com/aurahamzzz-cyber/microsoft-excel-alvaora)<br>Automates structured data workflows in Excel | 2026-11-18<br><sub>3.8 d</sub> | 150 | 39.7 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#aurahamzzz-cyber/microsoft-excel-alvaora&Date"><img src="https://api.star-history.com/svg?repos=aurahamzzz-cyber/microsoft-excel-alvaora&type=Date" width="260" alt="star history aurahamzzz-cyber/microsoft-excel-alvaora"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>Run SQL analysis without setting up a database server<br>`Data` | +163 | 23.3 | 43,234 |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>Real-time analysis of huge data, with open source<br>`Data` | +145 | 20.7 | 51,062 |
| 3 | [apache/superset](https://github.com/apache/superset)<br>Can't make sense of the data? Turn it into charts<br>`Data` | +116 | 16.6 | 75,619 |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>Table data handled fast, no more waiting<br>`Data` | +93 | 13.3 | 40,431 |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>Stream events between systems on one distributed platform<br>`Data` | +44 | 6.3 | 34,250 |
| 6 | [apache/arrow](https://github.com/apache/arrow)<br>Across languages, the data works as it is<br>`Data` | +36 | 5.1 | 17,336 |
| 7 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>Transform data the way software engineers build apps<br>`Data` | +32 | 4.6 | 14,202 |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>Write code in the browser and see results as you go<br>`Data` | +12 | 1.7 | 13,478 |

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

</det