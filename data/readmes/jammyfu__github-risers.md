**English** | [简体中文](README.zh-Hans.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

# GitHub Risers: Ranked by Stars Gained per Day

<img src=".github/social-preview.png" alt="GitHub Risers: Ranked by Stars Gained per Day" width="640">

[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![CI](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml/badge.svg)](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml) [![updated](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjammyfu%2Fgithub-risers%2Fmain%2Fdata%2Fstats.json&query=%24.today_utc&label=updated&color=brightgreen)](latest/rankings.md)

Trending GitHub repos ranked by star growth (stars gained per day), not total stars: AI first, then developer tools, security, web, infrastructure, design and data.

Data from 2026-11-20 15:48 UTC. Updated daily.

**Live boards:** [Website](https://jammyfu.github.io/github-risers/) · [Latest snapshot](latest/rankings.md)

## Use it now

1. Open the [live boards](https://jammyfu.github.io/github-risers/) — no install.
2. Or read this round's category leaders below, then the boards.
3. Each board here shows the top 10; the full top 20 is in [latest/rankings.md](latest/rankings.md).

[Website](https://jammyfu.github.io/github-risers/) · [How it works](docs/HOW_IT_WORKS.md) · [Facts](docs/FACTS.md) · [History](rankings/README.md) · [Latest](latest/rankings.md)

## Category leaders this round

| Category | #1 new (7 days) | #1 this week | #1 this month | #1 this year | #1 total stars |
|---|---|---|---|---|---|
| **[AI](#ai)** ★ primary | [erkamyaman/rust-anything](https://github.com/erkamyaman/rust-anything)<br>1,502/day | [morluto/rea](https://github.com/morluto/rea)<br>2,145/day | [morluto/rea](https://github.com/morluto/rea)<br>4,068/day | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>2,873/day | [morluto/rea](https://github.com/morluto/rea)<br>471,071 ★ |
| **[Developer Tools](#developer-tools)** | [Orderchodrag/smelt-minecraft-mods-to-rust-converter](https://github.com/Orderchodrag/smelt-minecraft-mods-to-rust-converter)<br>35.5/day | [astral-sh/uv](https://github.com/astral-sh/uv)<br>84.9/day | [zed-industries/zed](https://github.com/zed-industries/zed)<br>122/day | [zed-industries/zed](https://github.com/zed-industries/zed)<br>75.1/day | [oven-sh/bun](https://github.com/oven-sh/bun)<br>96,799 ★ |
| **[Security](#security)** | n/a | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>43.1/day | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>35.2/day | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>28.8/day | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>39,572 ★ |
| **[Web / Frontend](#web--frontend)** | [rohit3a/t3-clawd](https://github.com/rohit3a/t3-clawd)<br>24.0/day | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>170/day | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>93.1/day | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>82.9/day | [facebook/react](https://github.com/facebook/react)<br>252,838 ★ |
| **[Infrastructure](#infrastructure)** | [replit/datacat](https://github.com/replit/datacat)<br>126/day | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>52.3/day | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>41.5/day | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>33.5/day | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>129,302 ★ |
| **[Design / Creative](#design--creative)** | n/a | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>62.7/day | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>64.4/day | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>73.5/day | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>136,019 ★ |
| **[Data](#data)** | n/a | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>26.0/day | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>31.9/day | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>25.8/day | [apache/superset](https://github.com/apache/superset)<br>75,588 ★ |

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
| 1 | [erkamyaman/rust-anything](https://github.com/erkamyaman/rust-anything)<br>Afraid to rewrite in Rust? Migrate piece by piece safely | 2026-11-16<br><sub>4.2 d</sub> | 6,233 | 1,501.5 |
| 2 | [sybil-solutions/inference-optimisation-skill](https://github.com/sybil-solutions/inference-optimisation-skill)<br>Local LLM too slow? Let an agent boost serving speed | 2026-11-16<br><sub>3.9 d</sub> | 1,304 | 336.0 |
| 3 | [boringmarketer/boring-marketing-skills](https://github.com/boringmarketer/boring-marketing-skills)<br>Give your AI agent 32 free marketing skills | 2026-11-16<br><sub>4.0 d</sub> | 734 | 182.3 |
| 4 | [INK-Q/agy-fast](https://github.com/INK-Q/agy-fast)<br>Tokens running out? Cut LLM turns and token quota | 2026-11-19<br><sub>1.4 d</sub> | 119 | 82.0 |
| 5 | [staryone/motlab](https://github.com/staryone/motlab)<br>Want to make videos with code? Let agents build from refs | 2026-11-16<br><sub>4.1 d</sub> | 256 | 62.7 |
| 6 | [diego3g/craft](https://github.com/diego3g/craft)<br>UI design takes too long? Let AI agents craft every screen | 2026-11-15<br><sub>4.8 d</sub> | 284 | 58.9 |
| 7 | [vaibhav-space/my-ai-coding-workflow](https://github.com/vaibhav-space/my-ai-coding-workflow)<br>Review and audit AI code with a 3-stage pipeline | 2026-11-14<br><sub>6.1 d</sub> | 309 | 50.7 |
| 8 | [JuneYaooo/rea-toon](https://github.com/JuneYaooo/rea-toon)<br>Let AI break down hit short dramas from script to shot | 2026-11-14<br><sub>6.1 d</sub> | 284 | 46.2 |
| 9 | [jackson-cmd/claude-multi-desktop](https://github.com/jackson-cmd/claude-multi-desktop)<br>Run multiple Claude Desktop accounts at once on Mac | 2026-11-16<br><sub>4.5 d</sub> | 203 | 45.4 |
| 10 | [google-deepmind/robotics-antigravity-plugin](https://github.com/google-deepmind/robotics-antigravity-plugin)<br>Sim to real robots? Power agentic robotics workflows | 2026-11-16<br><sub>3.9 d</sub> | 164 | 42.3 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#erkamyaman/rust-anything&Date"><img src="https://api.star-history.com/svg?repos=erkamyaman/rust-anything&type=Date" width="260" alt="star history erkamyaman/rust-anything"></a>

<a href="https://www.star-history.com/#sybil-solutions/inference-optimisation-skill&Date"><img src="https://api.star-history.com/svg?repos=sybil-solutions/inference-optimisation-skill&type=Date" width="260" alt="star history sybil-solutions/inference-optimisation-skill"></a>

<a href="https://www.star-history.com/#boringmarketer/boring-marketing-skills&Date"><img src="https://api.star-history.com/svg?repos=boringmarketer/boring-marketing-skills&type=Date" width="260" alt="star history boringmarketer/boring-marketing-skills"></a>

<a href="https://www.star-history.com/#INK-Q/agy-fast&Date"><img src="https://api.star-history.com/svg?repos=INK-Q/agy-fast&type=Date" width="260" alt="star history INK-Q/agy-fast"></a>

<a href="https://www.star-history.com/#staryone/motlab&Date"><img src="https://api.star-history.com/svg?repos=staryone/motlab&type=Date" width="260" alt="star history staryone/motlab"></a>

<a href="https://www.star-history.com/#diego3g/craft&Date"><img src="https://api.star-history.com/svg?repos=diego3g/craft&type=Date" width="260" alt="star history diego3g/craft"></a>

<a href="https://www.star-history.com/#vaibhav-space/my-ai-coding-workflow&Date"><img src="https://api.star-history.com/svg?repos=vaibhav-space/my-ai-coding-workflow&type=Date" width="260" alt="star history vaibhav-space/my-ai-coding-workflow"></a>

<a href="https://www.star-history.com/#JuneYaooo/rea-toon&Date"><img src="https://api.star-history.com/svg?repos=JuneYaooo/rea-toon&type=Date" width="260" alt="star history JuneYaooo/rea-toon"></a>

<a href="https://www.star-history.com/#jackson-cmd/claude-multi-desktop&Date"><img src="https://api.star-history.com/svg?repos=jackson-cmd/claude-multi-desktop&type=Date" width="260" alt="star history jackson-cmd/claude-multi-desktop"></a>

<a href="https://www.star-history.com/#google-deepmind/robotics-antigravity-plugin&Date"><img src="https://api.star-history.com/svg?repos=google-deepmind/robotics-antigravity-plugin&type=Date" width="260" alt="star history google-deepmind/robotics-antigravity-plugin"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>Let AI clone any software for you<br>`AI` | +15,015 | 2,145.0 | 471,071 |
| 2 | [stablyai/orca](https://github.com/stablyai/orca)<br>Several AIs write at once, see which one works best<br>`AI` | +6,644 | 949.1 | 130,693 |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>Give your coding AI memory, skills and safety checks<br>`AI` | +5,618 | 802.6 | 307,639 |
| 4 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>Less filler code from AI, the needed code done right<br>`AI` | +5,352 | 764.6 | 195,368 |
| 5 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>One AI hunts security holes, a fresh AI verifies each<br>`AI` | +4,674 | 667.7 | 76,141 |
| 6 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>Pick plugins and build the agent you want<br>`AI` | +4,634 | 662.0 | 284,610 |
| 7 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)<br>Stop AI from making every page look the same<br>`AI` | +4,606 | 658.0 | 119,205 |
| 8 | [anthropics/skills](https://github.com/anthropics/skills)<br>Learn to write Claude skills from the official examples<br>`AI` | +4,149 | 592.7 | 197,943 |
| 9 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>Too big to read? Start with this map of the code<br>`AI` | +4,041 | 577.3 | 150,996 |
| 10 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)<br>Can't edit video? Write it like a web page<br>`AI` | +3,664 | 523.4 | 87,325 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="star history morluto/rea"></a>

<a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="star history stablyai/orca"></a>

<a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="star history affaan-m/ECC"></a>

<a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="star history DietrichGebert/ponytail"></a>

<a href="https://www.star-history.com/#cloudflare/security-audit-skill&Date"><img src="https://api.star-history.com/svg?repos=cloudflare/security-audit-skill&type=Date" width="260" alt="star history cloudflare/security-audit-skill"></a>

<a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="star history deepseek-ai/deepseek-harness"></a>

<a href="https://www.star-history.com/#Leonxlnx/taste-skill&Date"><img src="https://api.star-history.com/svg?repos=Leonxlnx/taste-skill&type=Date" width="260" alt="star history Leonxlnx/taste-skill"></a>

<a href="https://www.star-history.com/#anthropics/skills&Date"><img src="https://api.star-history.com/svg?repos=anthropics/skills&type=Date" width="260" alt="star history anthropics/skills"></a>

<a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="star history Graphify-Labs/graphify"></a>

<a href="https://www.star-history.com/#heygen-com/hyperframes&Date"><img src="https://api.star-history.com/svg?repos=heygen-com/hyperframes&type=Date" width="260" alt="star history heygen-com/hyperframes"></a>

</details>

### Fastest rising this month (last 30 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>Let AI clone any software for you<br>`AI` | +122,040 | 4,068.0 | 471,071 |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>One AI hunts security holes, a fresh AI verifies each<br>`AI` | +41,540 | 1,384.7 | 76,141 |
| 3 | [stablyai/orca](https://github.com/stablyai/orca)<br>Several AIs write at once, see which one works best<br>`AI` | +30,821 | 1,027.4 | 130,693 |
| 4 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>Pick plugins and build the agent you want<br>`AI` | +29,539 | 984.6 | 284,610 |
| 5 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>Less filler code from AI, the needed code done right<br>`AI` | +25,673 | 855.8 | 195,368 |
| 6 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>Give your coding AI memory, skills and safety checks<br>`AI` | +23,625 | 787.5 | 307,639 |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>Swap models in your coding AI; quota runs out, it carries on<br>`AI` | +21,291 | 709.7 | 39,474 |
| 8 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>Too big to read? Start with this map of the code<br>`AI` | +20,752 | 691.7 | 150,996 |
| 9 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)<br>Stop AI from making every page look the same<br>`AI` | +19,469 | 649.0 | 119,205 |
| 10 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)<br>Can't edit video? Write it like a web page<br>`AI` | +18,839 | 628.0 | 87,325 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="star history morluto/rea"></a>

<a href="https://www.star-history.com/#cloudflare/security-audit-skill&Date"><img src="https://api.star-history.com/svg?repos=cloudflare/security-audit-skill&type=Date" width="260" alt="star history cloudflare/security-audit-skill"></a>

<a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="star history stablyai/orca"></a>

<a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="star history deepseek-ai/deepseek-harness"></a>

<a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="star history DietrichGebert/ponytail"></a>

<a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="star history affaan-m/ECC"></a>

<a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="star history yetone/magpie"></a>

<a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="star history Graphify-Labs/graphify"></a>

<a href="https://www.star-history.com/#Leonxlnx/taste-skill&Date"><img src="https://api.star-history.com/svg?repos=Leonxlnx/taste-skill&type=Date" width="260" alt="star history Leonxlnx/taste-skill"></a>

<a href="https://www.star-history.com/#heygen-com/hyperframes&Date"><img src="https://api.star-history.com/svg?repos=heygen-com/hyperframes&type=Date" width="260" alt="star history heygen-com/hyperframes"></a>

</details>

### Fastest rising this year (last 365 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>Pick plugins and build the agent you want<br>`AI` | +284,397 | 2,872.7 †<br><sub>÷99d</sub> | 284,610 |
| 2 | [morluto/rea](https://github.com/morluto/rea)<br>Let AI clone any software for you<br>`AI` | +470,466 | 2,138.5 †<br><sub>÷220d</sub> | 471,071 |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>Less filler code from AI, the needed code done right<br>`AI` | +195,082 | 1,211.7 †<br><sub>÷161d</sub> | 195,368 |
| 4 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>An AI assistant that gets things done, on your own devices<br>`AI` | +394,853 | 1,093.8 †<br><sub>÷361d</sub> | 394,901 |
| 5 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>Give your coding AI memory, skills and safety checks<br>`AI` | +307,411 | 1,004.6 †<br><sub>÷306d</sub> | 307,639 |
| 6 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>An AI helper that gets better the more you use it<br>`AI` | +264,811 | 725.5 | 264,916 |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>Swap models in your coding AI; quota runs out, it carries on<br>`AI` | +39,267 | 677.0 †<br><sub>÷58d</sub> | 39,474 |
| 8 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>Too big to read? Start with this map of the code<br>`AI` | +150,778 | 652.7 †<br><sub>÷231d</sub> | 150,996 |
| 9 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>An open-source AI that writes code in your terminal<br>`AI` | +196,164 | 537.4 | 228,179 |
| 10 | [stablyai/orca](https://github.com/stablyai/orca)<br>Several AIs write at once, see which one works best<br>`AI` | +130,234 | 525.1 †<br><sub>÷248d</sub> | 130,693 |

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
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>Let AI clone any software for you<br>`AI` | 471,071 |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>An AI assistant that gets things done, on your own devices<br>`AI` | 394,901 |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>Give your coding AI memory, skills and safety checks<br>`AI` | 307,639 |
| 4 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>Pick plugins and build the agent you want<br>`AI` | 284,610 |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>An AI helper that gets better the more you use it<br>`AI` | 264,916 |
| 6 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>An open-source AI that writes code in your terminal<br>`AI` | 228,179 |
| 7 | [anthropics/skills](https://github.com/anthropics/skills)<br>Learn to write Claude skills from the official examples<br>`AI` | 197,943 |
| 8 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>Less filler code from AI, the needed code done right<br>`AI` | 195,368 |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch)<br>Switch providers in one click, no config editing<br>`AI` | 156,012 |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)<br>UIs built by AI that look professionally designed<br>`AI` | 152,062 |

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
| 1 | [Orderchodrag/smelt-minecraft-mods-to-rust-converter](https://github.com/Orderchodrag/smelt-minecraft-mods-to-rust-converter)<br>Porting Java mods to Rust? Turn jar files into runnable code | 2026-11-16<br><sub>4.0 d</sub> | 142 | 35.5 |
| 2 | [govijr/fix-storage](https://github.com/govijr/fix-storage)<br>Fix storage problems on Mac and Linux with one CLI | 2026-11-14<br><sub>6.0 d</sub> | 160 | 26.8 |
| 3 | [ineedfoundmyway/planrelay](https://github.com/ineedfoundmyway/planrelay)<br>Annotate and resolve blockers across plan and code reviews | 2026-11-15<br><sub>5.3 d</sub> | 119 | 22.4 |
| 4 | [RescuerDevelop/CapCut-AI-PC-Latest](https://github.com/RescuerDevelop/CapCut-AI-PC-Latest)<br>Guide on how to get CapCut 2026 | 2026-11-19<br><sub>1.0 d</sub> | 101 | 101.0 |
| 5 | [zaxd122/cmp30hx-mod](https://github.com/zaxd122/cmp30hx-mod)<br>Shape the world, share your craft, and build together | 2026-11-16<br><sub>4.2 d</sub> | 153 | 36.8 |
| 6 | [parth888/runtime-forge](https://github.com/parth888/runtime-forge)<br>Inspect, install, and update your runtimes in CLI | 2026-11-15<br><sub>4.8 d</sub> | 153 | 31.9 |
| 7 | [Dude-web/easywinget-gui](https://github.com/Dude-web/easywinget-gui)<br>Manage Windows packages easily in a web interface | 2026-11-15<br><sub>4.8 d</sub> | 153 | 31.7 |
| 8 | [oriliz/agent-crop](https://github.com/oriliz/agent-crop)<br>Local timing and self-improvement tool for coding agents | 2026-11-14<br><sub>6.3 d</sub> | 167 | 26.3 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#Orderchodrag/smelt-minecraft-mods-to-rust-converter&Date"><img src="https://api.star-history.com/svg?repos=Orderchodrag/smelt-minecraft-mods-to-rust-converter&type=Date" width="260" alt="star history Orderchodrag/smelt-minecraft-mods-to-rust-converter"></a>

<a href="https://www.star-history.com/#govijr/fix-storage&Date"><img src="https://api.star-history.com/svg?repos=govijr/fix-storage&type=Date" width="260" alt="star history govijr/fix-storage"></a>

<a href="https://www.star-history.com/#ineedfoundmyway/planrelay&Date"><img src="https://api.star-history.com/svg?repos=ineedfoundmyway/planrelay&type=Date" width="260" alt="star history ineedfoundmyway/planrelay"></a>

<a href="https://www.star-history.com/#RescuerDevelop/CapCut-AI-PC-Latest&Date"><img src="https://api.star-history.com/svg?repos=RescuerDevelop/CapCut-AI-PC-Latest&type=Date" width="260" alt="star history RescuerDevelop/CapCut-AI-PC-Latest"></a>

<a href="https://www.star-history.com/#zaxd122/cmp30hx-mod&Date"><img src="https://api.star-history.com/svg?repos=zaxd122/cmp30hx-mod&type=Date" width="260" alt="star history zaxd122/cmp30hx-mod"></a>

<a href="https://www.star-history.com/#parth888/runtime-forge&Date"><img src="https://api.star-history.com/svg?repos=parth888/runtime-forge&type=Date" width="260" alt="star history parth888/runtime-forge"></a>

<a href="https://www.star-history.com/#Dude-web/easywinget-gui&Date"><img src="https://api.star-history.com/svg?repos=Dude-web/easywinget-gui&type=Date" width="260" alt="star history Dude-web/easywinget-gui"></a>

<a href="https://www.star-history.com/#oriliz/agent-crop&Date"><img src="https://api.star-history.com/svg?repos=oriliz/agent-crop&type=Date" width="260" alt="star history oriliz/agent-crop"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Install Python packages without the wait<br>`Developer Tools` | +594 | 84.9 | 92,456 |
| 2 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>Opens fast, and you can code together with others<br>`Developer Tools` | +547 | 78.1 | 95,410 |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>Dev tools, env variables and tasks, in one tool<br>`Developer Tools` | +261 | 37.3 | 36,346 |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>Search a whole folder for text, faster than grep<br>`Developer Tools` | +199 | 28.4 | 70,095 |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>Run, bundle, test, install: one tool does it all<br>`Developer Tools` | +156 | 22.3 | 96,799 |
| 6 | [cli/cli](https://github.com/cli/cli)<br>Handle GitHub from the command line, no browser<br>`Developer Tools` | +128 | 18.3 | 47,100 |
| 7 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>A text editor with language server and highlighting built in<br>`Developer Tools` | +91 | 13.0 | 46,945 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Format and check web code with one tool<br>`Developer Tools` | +70 | 10.0 | 26,161 |

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
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>Opens fast, and you can code together with others<br>`Developer Tools` | +3,672 | 122.4 | 95,410 |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Install Python packages without the wait<br>`Developer Tools` | +1,666 | 55.5 | 92,456 |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>Dev tools, env variables and tasks, in one tool<br>`Developer Tools` | +1,197 | 39.9 | 36,346 |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>Search a whole folder for text, faster than grep<br>`Developer Tools` | +943 | 31.4 | 70,095 |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>Run, bundle, test, install: one tool does it all<br>`Developer Tools` | +675 | 22.5 | 96,799 |
| 6 | [cli/cli](https://github.com/cli/cli)<br>Handle GitHub from the command line, no browser<br>`Developer Tools` | +467 | 15.6 | 47,100 |
| 7 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>A text editor with language server and highlighting built in<br>`Developer Tools` | +404 | 13.5 | 46,945 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Format and check web code with one tool<br>`Developer Tools` | +238 | 7.9 | 26,161 |

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
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>Opens fast, and you can code together with others<br>`Developer Tools` | +27,403 | 75.1 | 95,410 |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Install Python packages without the wait<br>`Developer Tools` | +20,771 | 56.9 | 92,456 |
| 3 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>Run, bundle, test, install: one tool does it all<br>`Developer Tools` | +16,520 | 45.3 | 96,799 |
| 4 | [jdx/mise](https://github.com/jdx/mise)<br>Dev tools, env variables and tasks, in one tool<br>`Developer Tools` | +15,313 | 42.0 | 36,346 |
| 5 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>Search a whole folder for text, faster than grep<br>`Developer Tools` | +13,347 | 36.6 | 70,095 |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>A text editor with language server and highlighting built in<br>`Developer Tools` | +6,454 | 17.7 | 46,945 |
| 7 | [cli/cli](https://github.com/cli/cli)<br>Handle GitHub from the command line, no browser<br>`Developer Tools` | +6,334 | 17.4 | 47,100 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Format and check web code with one tool<br>`Developer Tools` | +4,406 | 12.1 | 26,161 |

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
| 1 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>Run, bundle, test, install: one tool does it all<br>`Developer Tools` | 96,799 |
| 2 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>Opens fast, and you can code together with others<br>`Developer Tools` | 95,410 |
| 3 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Install Python packages without the wait<br>`Developer Tools` | 92,456 |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>Search a whole folder for text, faster than grep<br>`Developer Tools` | 70,095 |
| 5 | [cli/cli](https://github.com/cli/cli)<br>Handle GitHub from the command line, no browser<br>`Developer Tools` | 47,100 |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>A text editor with language server and highlighting built in<br>`Developer Tools` | 46,945 |
| 7 | [jdx/mise](https://github.com/jdx/mise)<br>Dev tools, env variables and tasks, in one tool<br>`Developer Tools` | 36,346 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Format and check web code with one tool<br>`Developer Tools` | 26,161 |

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
| 1 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>Write one template, scan for vulnerabilities in bulk<br>`Security` | +302 | 43.1 | 33,148 |
| 2 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>Scan containers and code repos for security issues at once<br>`Security` | +291 | 41.6 | 39,572 |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>Catch the problems in your code before you commit<br>`Security` | +215 | 30.7 | 17,852 |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>Concise cheat sheets on application security<br>`Security` | +111 | 15.9 | 34,145 |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>Are your dependencies safe? One scan tells you<br>`Security` | +67 | 9.6 | 11,572 |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>Does your container image have vulnerabilities? Scan it<br>`Security` | +53 | 7.6 | 13,308 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>Know the moment something odd happens in the cloud<br>`Security` | +17 | 2.4 | 9,593 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Scan your Go code for security problems<br>`Security` | +10 | 1.4 | 9,012 |

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
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>Scan containers and code repos for security issues at once<br>`Security` | +1,056 | 35.2 | 39,572 |
| 2 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>Write one template, scan for vulnerabilities in bulk<br>`Security` | +1,029 | 34.3 | 33,148 |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>Catch the problems in your code before you commit<br>`Security` | +709 | 23.6 | 17,852 |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>Concise cheat sheets on application security<br>`Security` | +487 | 16.2 | 34,145 |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>Are your dependencies safe? One scan tells you<br>`Security` | +371 | 12.4 | 11,572 |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>Does your container image have vulnerabilities? Scan it<br>`Security` | +257 | 8.6 | 13,308 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>Know the moment something odd happens in the cloud<br>`Security` | +109 | 3.6 | 9,593 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Scan your Go code for security problems<br>`Security` | +42 | 1.4 | 9,012 |

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
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>Scan containers and code repos for security issues at once<br>`Security` | +10,527 | 28.8 | 39,572 |
| 2 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>Write one template, scan for vulnerabilities in bulk<br>`Security` | +7,927 | 21.7 | 33,148 |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>Catch the problems in your code before you commit<br>`Security` | +4,645 | 12.7 | 17,852 |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>Concise cheat sheets on application security<br>`Security` | +3,684 | 10.1 | 34,145 |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>Are your dependencies safe? One scan tells you<br>`Security` | +3,613 | 9.9 | 11,572 |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>Does your container image have vulnerabilities? Scan it<br>`Security` | +2,407 | 6.6 | 13,308 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>Know the moment something odd happens in the cloud<br>`Security` | +1,269 | 3.5 | 9,593 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Scan your Go code for security problems<br>`Security` | +557 | 1.5 | 9,012 |

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
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>Scan containers and code repos for security issues at once<br>`Security` | 39,572 |
| 2 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>Concise cheat sheets on application security<br>`Security` | 34,145 |
| 3 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>Write one template, scan for vulnerabilities in bulk<br>`Security` | 33,148 |
| 4 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>Catch the problems in your code before you commit<br>`Security` | 17,852 |
| 5 | [anchore/grype](https://github.com/anchore/grype)<br>Does your container image have vulnerabilities? Scan it<br>`Security` | 13,308 |
| 6 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>Are your dependencies safe? One scan tells you<br>`Security` | 11,572 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>Know the moment something odd happens in the cloud<br>`Security` | 9,593 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Scan your Go code for security problems<br>`Security` | 9,012 |

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
| 1 | [rohit3a/t3-clawd](https://github.com/rohit3a/t3-clawd)<br>Get a Claude-inspired theme for T3 Code in one file | 2026-11-14<br><sub>5.8 d</sub> | 138 | 24.0 |
| 2 | [nforst/fagus](https://github.com/nforst/fagus)<br>Turn HTML into print-ready PDFs without running a browser | 2026-11-13<br><sub>6.9 d</sub> | 138 | 20.0 |
| 3 | [homielab/noteflare](https://github.com/homielab/noteflare)<br>Keep your notes to yourself with end-to-end encryption | 2026-11-14<br><sub>6.3 d</sub> | 104 | 16.5 |
| 4 | [johnnablea29-art/stratgies-indicator](https://github.com/johnnablea29-art/stratgies-indicator)<br>Automation script for repeatable bot task runs | 2026-11-15<br><sub>4.8 d</sub> | 153 | 31.9 |
| 5 | [ELEL182/bunny-hopping-mod](https://github.com/ELEL182/bunny-hopping-mod)<br>Master momentum and movement with Fabric bunny hopping | 2026-11-15<br><sub>4.8 d</sub> | 153 | 31.6 |
| 6 | [manuelgscom/inside-llm](https://github.com/manuelgscom/inside-llm)<br>Browser tool for inspecting GGUF tokens and samplers | 2026-11-15<br><sub>4.9 d</sub> | 109 | 22.4 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#rohit3a/t3-clawd&Date"><img src="https://api.star-history.com/svg?repos=rohit3a/t3-clawd&type=Date" width="260" alt="star history rohit3a/t3-clawd"></a>

<a href="https://www.star-history.com/#nforst/fagus&Date"><img src="https://api.star-history.com/svg?repos=nforst/fagus&type=Date" width="260" alt="star history nforst/fagus"></a>

<a href="https://www.star-history.com/#homielab/noteflare&Date"><img src="https://api.star-history.com/svg?repos=homielab/noteflare&type=Date" width="260" alt="star history homielab/noteflare"></a>

<a href="https://www.star-history.com/#johnnablea29-art/stratgies-indicator&Date"><img src="https://api.star-history.com/svg?repos=johnnablea29-art/stratgies-indicator&type=Date" width="260" alt="star history johnnablea29-art/stratgies-indicator"></a>

<a href="https://www.star-history.com/#ELEL182/bunny-hopping-mod&Date"><img src="https://api.star-history.com/svg?repos=ELEL182/bunny-hopping-mod&type=Date" width="260" alt="star history ELEL182/bunny-hopping-mod"></a>

<a href="https://www.star-history.com/#manuelgscom/inside-llm&Date"><img src="https://api.star-history.com/svg?repos=manuelgscom/inside-llm&type=Date" width="260" alt="star history manuelgscom/inside-llm"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>A compiler turns your components into efficient web code<br>`Web / Frontend` | +1,190 | 170.0 | 89,831 |
| 2 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>Good-looking components, and the code is yours to change<br>`Web / Frontend` | +594 | 84.9 | 128,632 |
| 3 | [facebook/react](https://github.com/facebook/react)<br>Build web and native app interfaces with one library<br>`Web / Frontend` | +400 | 57.1 | 252,838 |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>Build a whole site with React, front to back<br>`Web / Frontend` | +194 | 27.7 | 143,627 |
| 5 | [withastro/astro](https://github.com/withastro/astro)<br>For content-driven websites, with lightweight output<br>`Web / Frontend` | +182 | 26.0 | 64,091 |
| 6 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>Custom designs without writing a pile of CSS<br>`Web / Frontend` | +160 | 22.9 | 98,711 |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>Start with one small page, learn only what you use<br>`Web / Frontend` | +124 | 17.7 | 55,057 |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>Fetching data and caching it? Leave it to this<br>`Web / Frontend` | +47 | 6.7 | 50,596 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="star history sveltejs/svelte"></a>

<a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="star history shadcn-ui/ui"></a>

<a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="star history facebook/react"></a>

<a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="star history vercel/next.js"></a>

<a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="star history withastro/astro"></a>

<a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="star history tailwindlabs/tailwindcss"></a>

<a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="star history vuejs/core"></a>

<a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="star history tanstack/query"></a>

</details>

### Fastest rising this month (last 30 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>Good-looking components, and the code is yours to change<br>`Web / Frontend` | +2,794 | 93.1 | 128,632 |
| 2 | [facebook/react](https://github.com/facebook/react)<br>Build web and native app interfaces with one library<br>`Web / Frontend` | +1,767 | 58.9 | 252,838 |
| 3 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>A compiler turns your components into efficient web code<br>`Web / Frontend` | +1,577 | 52.6 | 89,831 |
| 4 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>Custom designs without writing a pile of CSS<br>`Web / Frontend` | +972 | 32.4 | 98,711 |
| 5 | [withastro/astro](https://github.com/withastro/astro)<br>For content-driven websites, with lightweight output<br>`Web / Frontend` | +829 | 27.6 | 64,091 |
| 6 | [vercel/next.js](https://github.com/vercel/next.js)<br>Build a whole site with React, front to back<br>`Web / Frontend` | +811 | 27.0 | 143,627 |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>Start with one small page, learn only what you use<br>`Web / Frontend` | +456 | 15.2 | 55,057 |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>Fetching data and caching it? Leave it to this<br>`Web / Frontend` | +198 | 6.6 | 50,596 |

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
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>Good-looking components, and the code is yours to change<br>`Web / Frontend` | +30,265 | 82.9 | 128,632 |
| 2 | [facebook/react](https://github.com/facebook/react)<br>Build web and native app interfaces with one library<br>`Web / Frontend` | +15,765 | 43.2 | 252,838 |
| 3 | [withastro/astro](https://github.com/withastro/astro)<br>For content-driven websites, with lightweight output<br>`Web / Frontend` | +10,604 | 29.1 | 64,091 |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>Build a whole site with React, front to back<br>`Web / Frontend` | +10,401 | 28.5 | 143,627 |
| 5 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>Custom designs without writing a pile of CSS<br>`Web / Frontend` | +8,924 | 24.4 | 98,711 |
| 6 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>A compiler turns your components into efficient web code<br>`Web / Frontend` | +6,219 | 17.0 | 89,831 |
| 7 | [tanstack/query](https://github.com/tanstack/query)<br>Fetching data and caching it? Leave it to this<br>`Web / Frontend` | +3,716 | 10.2 | 50,596 |
| 8 | [vuejs/core](https://github.com/vuejs/core)<br>Start with one small page, learn only what you use<br>`Web / Frontend` | +3,704 | 10.1 | 55,057 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="star history shadcn-ui/ui"></a>

<a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="star history facebook/react"></a>

<a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="star history withastro/astro"></a>

<a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="star history vercel/next.js"></a>

<a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="star history tailwindlabs/tailwindcss"></a>

<a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="star history sveltejs/svelte"></a>

<a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="star history tanstack/query"></a>

<a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="star history vuejs/core"></a>

</details>

### Total stars (all time)

| # | Project | Total stars |
|---|---|---:|
| 1 | [facebook/react](https://github.com/facebook/react)<br>Build web and native app interfaces with one library<br>`Web / Frontend` | 252,838 |
| 2 | [vercel/next.js](https://github.com/vercel/next.js)<br>Build a whole site with React, front to back<br>`Web / Frontend` | 143,627 |
| 3 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>Good-looking components, and the code is yours to change<br>`Web / Frontend` | 128,632 |
| 4 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>Custom designs without writing a pile of CSS<br>`Web / Frontend` | 98,711 |
| 5 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>A compiler turns your components into efficient web code<br>`Web / Frontend` | 89,831 |
| 6 | [withastro/astro](https://github.com/withastro/astro)<br>For content-driven websites, with lightweight output<br>`Web / Frontend` | 64,091 |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>Start with one small page, learn only what you use<br>`Web / Frontend` | 55,057 |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>Fetching data and caching it? Leave it to this<br>`Web / Frontend` | 50,596 |

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
| 1 | [replit/datacat](https://github.com/replit/datacat)<br>Track metrics and logs with self-hosted dashboards | 2026-11-17<br><sub>3.5 d</sub> | 445 | 125.7 |
| 2 | [Realmeshowroom/jet-reports-skill](https://github.com/Realmeshowroom/jet-reports-skill)<br>Visualize and organize complex workbook workflows | 2026-11-15<br><sub>4.8 d</sub> | 153 | 31.8 |
| 3 | [mmclucknorrismm/cmangos-helm](https://github.com/mmclucknorrismm/cmangos-helm)<br>Command and manage your CMaNGOS realm with Helm | 2026-11-15<br><sub>4.8 d</sub> | 153 | 31.6 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#replit/datacat&Date"><img src="https://api.star-history.com/svg?repos=replit/datacat&type=Date" width="260" alt="star history replit/datacat"></a>

<a href="https://www.star-history.com/#Realmeshowroom/jet-reports-skill&Date"><img src="https://api.star-history.com/svg?repos=Realmeshowroom/jet-reports-skill&type=Date" width="260" alt="star history Realmeshowroom/jet-reports-skill"></a>

<a href="https://www.star-history.com/#mmclucknorrismm/cmangos-helm&Date"><img src="https://api.star-history.com/svg?repos=mmclucknorrismm/cmangos-helm&type=Date" width="260" alt="star history mmclucknorrismm/cmangos-helm"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>Lots of containers? Leave deploying and scaling to it<br>`Infrastructure` | +366 | 52.3 | 129,302 |
| 2 | [docker/compose](https://github.com/docker/compose)<br>Put many containers in one file and run them together<br>`Infrastructure` | +321 | 45.9 | 39,067 |
| 3 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Set up a web server with HTTPS configured for you<br>`Infrastructure` | +315 | 45.0 | 79,323 |
| 4 | [grafana/grafana](https://github.com/grafana/grafana)<br>Metrics, logs and traces on one dashboard<br>`Infrastructure` | +170 | 24.3 | 78,012 |
| 5 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>When the system breaks, the alert finds you first<br>`Infrastructure` | +170 | 24.3 | 67,736 |
| 6 | [traefik/traefik](https://github.com/traefik/traefik)<br>With many services, traffic gets sorted automatically<br>`Infrastructure` | +103 | 14.7 | 65,629 |
| 7 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>Write cloud resources as code you can review and version<br>`Infrastructure` | +86 | 12.3 | 50,298 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>Manage cloud resources in a language you already know<br>`Infrastructure` | +32 | 4.6 | 25,926 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="star history kubernetes/kubernetes"></a>

<a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="star history docker/compose"></a>

<a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="star history caddyserver/caddy"></a>

<a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="star history grafana/grafana"></a>

<a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="star history prometheus/prometheus"></a>

<a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="star history traefik/traefik"></a>

<a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="star history hashicorp/terraform"></a>

<a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="star history pulumi/pulumi"></a>

</details>

### Fastest rising this month (last 30 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Set up a web server with HTTPS configured for you<br>`Infrastructure` | +1,245 | 41.5 | 79,323 |
| 2 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>When the system breaks, the alert finds you first<br>`Infrastructure` | +1,181 | 39.4 | 67,736 |
| 3 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>Lots of containers? Leave deploying and scaling to it<br>`Infrastructure` | +1,174 | 39.1 | 129,302 |
| 4 | [grafana/grafana](https://github.com/grafana/grafana)<br>Metrics, logs and traces on one dashboard<br>`Infrastructure` | +768 | 25.6 | 78,012 |
| 5 | [docker/compose](https://github.com/docker/compose)<br>Put many containers in one file and run them together<br>`Infrastructure` | +727 | 24.2 | 39,067 |
| 6 | [traefik/traefik](https://github.com/traefik/traefik)<br>With many services, traffic gets sorted automatically<br>`Infrastructure` | +422 | 14.1 | 65,629 |
| 7 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>Write cloud resources as code you can review and version<br>`Infrastructure` | +402 | 13.4 | 50,298 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>Manage cloud resources in a language you already know<br>`Infrastructure` | +168 | 5.6 | 25,926 |

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
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Set up a web server with HTTPS configured for you<br>`Infrastructure` | +12,237 | 33.5 | 79,323 |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>Lots of containers? Leave deploying and scaling to it<br>`Infrastructure` | +11,930 | 32.7 | 129,302 |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>Metrics, logs and traces on one dashboard<br>`Infrastructure` | +7,983 | 21.9 | 78,012 |
| 4 | [traefik/traefik](https://github.com/traefik/traefik)<br>With many services, traffic gets sorted automatically<br>`Infrastructure` | +7,639 | 20.9 | 65,629 |
| 5 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>When the system breaks, the alert finds you first<br>`Infrastructure` | +7,067 | 19.4 | 67,736 |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>Write cloud resources as code you can review and version<br>`Infrastructure` | +3,842 | 10.5 | 50,298 |
| 7 | [docker/compose](https://github.com/docker/compose)<br>Put many containers in one file and run them together<br>`Infrastructure` | +3,028 | 8.3 | 39,067 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>Manage cloud resources in a language you already know<br>`Infrastructure` | +2,107 | 5.8 | 25,926 |

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
| 1 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>Lots of containers? Leave deploying and scaling to it<br>`Infrastructure` | 129,302 |
| 2 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Set up a web server with HTTPS configured for you<br>`Infrastructure` | 79,323 |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>Metrics, logs and traces on one dashboard<br>`Infrastructure` | 78,012 |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>When the system breaks, the alert finds you first<br>`Infrastructure` | 67,736 |
| 5 | [traefik/traefik](https://github.com/traefik/traefik)<br>With many services, traffic gets sorted automatically<br>`Infrastructure` | 65,629 |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>Write cloud resources as code you can review and version<br>`Infrastructure` | 50,298 |
| 7 | [docker/compose](https://github.com/docker/compose)<br>Put many containers in one file and run them together<br>`Infrastructure` | 39,067 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>Manage cloud resources in a language you already know<br>`Infrastructure` | 25,926 |

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

No new repo met the criteria in this run.

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>Open it and draw, like sketching on paper<br>`Design / Creative` | +439 | 62.7 | 136,019 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>Design together as a team, on an open-source platform<br>`Design / Creative` | +283 | 40.4 | 62,576 |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>One icon set in one style, ready to use<br>`Design / Creative` | +157 | 22.4 | 25,883 |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>Diagrams and a whiteboard in one editor<br>`Design / Creative` | +153 | 21.9 | 9,491 |
| 5 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>Drop After Effects animations straight into web pages<br>`Design / Creative` | +137 | 19.6 | 32,532 |
| 6 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Pick ready-made components for Tailwind CSS<br>`Design / Creative` | +110 | 15.7 | 42,912 |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>A flexible icon family for everyone<br>`Design / Creative` | +34 | 4.9 | 7,833 |
| 8 | [lottiefiles/lottie-ios](https://github.com/lottiefiles/lottie-ios)<br>Drop After Effects animations straight into iOS<br>`Design / Creative` | +0 | 0.0 | 43 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#excalidraw/excalidraw&Date"><img src="https://api.star-history.com/svg?repos=excalidraw/excalidraw&type=Date" width="260" alt="star history excalidraw/excalidraw"></a>

<a href="https://www.star-history.com/#penpot/penpot&Date"><img src="https://api.star-history.com/svg?repos=penpot/penpot&type=Date" width="260" alt="star history penpot/penpot"></a>

<a href="https://www.star-history.com/#lucide-icons/lucide&Date"><img src="https://api.star-history.com/svg?repos=lucide-icons/lucide&type=Date" width="260" alt="star history lucide-icons/lucide"></a>

<a href="https://www.star-history.com/#jgraph/drawio&Date"><img src="https://api.star-history.com/svg?repos=jgraph/drawio&type=Date" width="260" alt="star history jgraph/drawio"></a>

<a href="https://www.star-history.com/#airbnb/lottie-web&Date"><img src="https://api.star-history.com/svg?repos=airbnb/lottie-web&type=Date" width="260" alt="star history airbnb/lottie-web"></a>

<a href="https://www.star-history.com/#saadeghi/daisyui&Date"><img src="https://api.star-history.com/svg?repos=saadeghi/daisyui&type=Date" width="260" alt="star history saadeghi/daisyui"></a>

<a href="https://www.star-history.com/#phosphor-icons/homepage&Date"><img src="https://api.star-history.com/svg?repos=phosphor-icons/homepage&type=Date" width="260" alt="star history phosphor-icons/homepage"></a>

<a href="https://www.star-history.com/#lottiefiles/lottie-ios&Date"><img src="https://api.star-history.com/svg?repos=lottiefiles/lottie-ios&type=Date" width="260" alt="star history lottiefiles/lottie-ios"></a>

</details>

### Fastest rising this month (last 30 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>Open it and draw, like sketching on paper<br>`Design / Creative` | +1,933 | 64.4 | 136,019 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>Design together as a team, on an open-source platform<br>`Design / Creative` | +1,274 | 42.5 | 62,576 |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>One icon set in one style, ready to use<br>`Design / Creative` | +751 | 25.0 | 25,883 |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>Diagrams and a whiteboard in one editor<br>`Design / Creative` | +606 | 20.2 | 9,491 |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Pick ready-made components for Tailwind CSS<br>`Design / Creative` | +361 | 12.0 | 42,912 |
| 6 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>Drop After Effects animations straight into web pages<br>`Design / Creative` | +311 | 10.4 | 32,532 |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>A flexible icon family for everyone<br>`Design / Creative` | +163 | 5.4 | 7,833 |
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
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>Open it and draw, like sketching on paper<br>`Design / Creative` | +26,826 | 73.5 | 136,019 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>Design together as a team, on an open-source platform<br>`Design / Creative` | +21,757 | 59.6 | 62,576 |
| 3 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>Diagrams and a whiteboard in one editor<br>`Design / Creative` | +6,701 | 18.4 | 9,491 |
| 4 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>One icon set in one style, ready to use<br>`Design / Creative` | +6,441 | 17.6 | 25,883 |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Pick ready-made components for Tailwind CSS<br>`Design / Creative` | +4,258 | 11.7 | 42,912 |
| 6 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>A flexible icon family for everyone<br>`Design / Creative` | +2,210 | 6.1 | 7,833 |
| 7 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>Drop After Effects animations straight into web pages<br>`Design / Creative` | +1,268 | 3.5 | 32,532 |
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
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>Open it and draw, like sketching on paper<br>`Design / Creative` | 136,019 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>Design together as a team, on an open-source platform<br>`Design / Creative` | 62,576 |
| 3 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Pick ready-made components for Tailwind CSS<br>`Design / Creative` | 42,912 |
| 4 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>Drop After Effects animations straight into web pages<br>`Design / Creative` | 32,532 |
| 5 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>One icon set in one style, ready to use<br>`Design / Creative` | 25,883 |
| 6 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>Diagrams and a whiteboard in one editor<br>`Design / Creative` | 9,491 |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>A flexible icon family for everyone<br>`Design / Creative` | 7,833 |
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
| 1 | [alibasimm1993/whalefeed](https://github.com/alibasimm1993/whalefeed)<br>Follow all your feeds in real-time right on your desktop | 2026-11-15<br><sub>4.8 d</sub> | 153 | 32.0 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#alibasimm1993/whalefeed&Date"><img src="https://api.star-history.com/svg?repos=alibasimm1993/whalefeed&type=Date" width="260" alt="star history alibasimm1993/whalefeed"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>Run SQL analysis without setting up a database server<br>`Data` | +182 | 26.0 | 43,206 |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>Real-time analysis of huge data, with open source<br>`Data` | +147 | 21.0 | 51,040 |
| 3 | [apache/superset](https://github.com/apache/superset)<br>Can't make sense of the data? Turn it into charts<br>`Data` | +104 | 14.9 | 75,588 |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>Table data handled fast, no more waiting<br>`Data` | +70 | 10.0 | 40,396 |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>Stream events between systems on one distributed platform<br>`Data` | +48 | 6.9 | 34,243 |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>Transform data the way software engineers build apps<br>`Data` | +33 | 4.7 | 14,193 |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>Across languages, the data works as it is<br>`Data` | +30 | 4.3 | 17,320 |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>Write code in the browser and see results as you go<br>`Data` | +11 | 1.6 | 13,475 |

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

### Fastest rising this month (last 30 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>Run SQL analysis without setting up a database server<br>`Data` | +956 | 31.9 | 43,206 |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>Real-time analysis of huge data, with open source<br>`Data` | +594 | 19.8 | 51,040 |
| 3 | [apache/superset](https://github.com/apache/superset)<br>Can't make sense of the data? Turn it into charts<br>`Data` | +455 | 15.2 | 75,588 |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>Table data handled fast, no more waiting<br>`Data` | +300 | 10.0 | 40,396 |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>Stream events between systems on one distributed platform<br>`Data` | +270 | 9.0 | 34,243 |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>Transform data the way software engineers build apps<br>`Data` | +158 | 5.3 | 14,193 |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>Across languages, the data works as it is<br>`Data` | +117 | 3.9 | 17,320 |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>Write code in the browser and see results as you go<br>`Data` | +34 | 1.1 | 13,475 |

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
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>Run SQL analysis without setting up a database server<br>`Data` | +9,413 | 25.8 | 43,206 |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>Real-time analysis of huge data, with open source<br>`Data` | +7,552 | 20.7 | 51,040 |
| 3 | [apache/superset](https://github.com/apache/superset)<br>Can't make sense of the data? Turn it into charts<br>`Data` | +7,367 | 20.2 | 75,588 |
| 4 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>Table data handled fast, no more waiting<br>`Data` | +4,760 | 13.0 | 40,396 |
| 5 | [apache/kafka](https://github.com/apache/kafka)<br>Stream events between systems on one distributed platform<br>`Data` | +3,307 | 9.1 | 34,243 |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>Transform data the way software engineers build apps<br>`Data` | +2,467 | 6.8 | 14,193 |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>Across languages, the data works as it is<br>`Data` | +1,302 | 3.6 | 17,320 |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>Write code in the browser and see results as you go<br>`Data` | +862 | 2.4 | 13,475 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="star history duckdb/duckdb"></a>

<a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="star history ClickHouse/ClickHouse"></a>

<a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="star history apache/superset"></a>

<a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="star history pola-rs/polars"></a>

<a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="star history apache/kafka"></a>

<a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="star history dbt-labs/dbt-core"></a>

<a href="https://www.star-history.com/#apache/arrow&Date"><img src="http