**English** | [简体中文](README.zh-Hans.md) | [繁體中文](README.zh-Hant.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

# GitHub Risers: Ranked by Stars Gained per Day

<img src=".github/social-preview.png" alt="GitHub Risers: Ranked by Stars Gained per Day" width="640">

[![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![CI](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml/badge.svg)](https://github.com/jammyfu/github-risers/actions/workflows/ci.yml) [![updated](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fjammyfu%2Fgithub-risers%2Fmain%2Fdata%2Fstats.json&query=%24.today_utc&label=updated&color=brightgreen)](latest/rankings.md)

Trending GitHub repos ranked by star growth (stars gained per day), not total stars: AI first, then developer tools, security, web, infrastructure, design and data.

Data from 2026-11-08 13:56 UTC. Updated daily.

**Live boards:** [Website](https://jammyfu.github.io/github-risers/) · [Latest snapshot](latest/rankings.md)

## Use it now

1. Open the [live boards](https://jammyfu.github.io/github-risers/) — no install.
2. Or read this round's category leaders below, then the boards.
3. Each board here shows the top 10; the full top 20 is in [latest/rankings.md](latest/rankings.md).

[Website](https://jammyfu.github.io/github-risers/) · [How it works](docs/HOW_IT_WORKS.md) · [Facts](docs/FACTS.md) · [History](rankings/README.md) · [Latest](latest/rankings.md)

## Category leaders this round

| Category | #1 new (7 days) | #1 this week | #1 this month | #1 this year | #1 total stars |
|---|---|---|---|---|---|
| **[AI](#ai)** ★ primary | [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)<br>773/day | [morluto/rea](https://github.com/morluto/rea)<br>3,756/day | [morluto/rea](https://github.com/morluto/rea)<br>13,710/day | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>3,172/day | [morluto/rea](https://github.com/morluto/rea)<br>442,531 ★ |
| **[Developer Tools](#developer-tools)** | [govijr/terminal-mac](https://github.com/govijr/terminal-mac)<br>431/day | [zed-industries/zed](https://github.com/zed-industries/zed)<br>283/day | [zed-industries/zed](https://github.com/zed-industries/zed)<br>107/day | [zed-industries/zed](https://github.com/zed-industries/zed)<br>74.3/day | [oven-sh/bun](https://github.com/oven-sh/bun)<br>96,703 ★ |
| **[Security](#security)** | [yorkeccak/globalhackmap](https://github.com/yorkeccak/globalhackmap)<br>22.0/day | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>34.0/day | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>30.2/day | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>28.0/day | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>39,116 ★ |
| **[Web / Frontend](#web--frontend)** | [AtomIllusionistDwell/watson-username-footprint-finder](https://github.com/AtomIllusionistDwell/watson-username-footprint-finder)<br>123/day | [facebook/react](https://github.com/facebook/react)<br>96.9/day | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>90.8/day | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>83.3/day | [facebook/react](https://github.com/facebook/react)<br>252,408 ★ |
| **[Infrastructure](#infrastructure)** | [MuseumCassowaryCarve/twitch-drops-miner](https://github.com/MuseumCassowaryCarve/twitch-drops-miner)<br>417/day | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>93.9/day | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>48.4/day | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>32.9/day | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>128,919 ★ |
| **[Design / Creative](#design--creative)** | [kubai087/kubai-icons](https://github.com/kubai087/kubai-icons)<br>52.8/day | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>64.9/day | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>67.1/day | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>74.0/day | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>135,323 ★ |
| **[Data](#data)** | n/a | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>31.4/day | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>32.9/day | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>25.8/day | [apache/superset](https://github.com/apache/superset)<br>75,450 ★ |

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
| 1 | [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)<br>Tired of babysitting agents? Approve only when needed | 2026-11-03<br><sub>5.2 d</sub> | 4,057 | 773.4 |
| 2 | [voyager-so/vork](https://github.com/voyager-so/vork)<br>Let agents work with 3D and visual effects | 2026-11-05<br><sub>2.6 d</sub> | 1,034 | 391.9 |
| 3 | [Sandflow-ai/sand3d](https://github.com/Sandflow-ai/sand3d)<br>Let language models build 3D models in Python | 2026-11-03<br><sub>5.2 d</sub> | 1,254 | 239.7 |
| 4 | [JosssphZhou/poki](https://github.com/JosssphZhou/poki)<br>Let AI operate your real iPhone | 2026-11-05<br><sub>3.0 d</sub> | 566 | 191.7 |
| 5 | [HerdBuilderEstimate/roblox-studio-mcp](https://github.com/HerdBuilderEstimate/roblox-studio-mcp)<br>Let AI edit your Roblox Studio scripts | 2026-11-06<br><sub>2.3 d</sub> | 420 | 181.1 |
| 6 | [shanselman/sandbox-mcp](https://github.com/shanselman/sandbox-mcp)<br>Test apps on disposable Windows machines | 2026-11-06<br><sub>1.8 d</sub> | 305 | 170.6 |
| 7 | [dhruvthakur11/youtube-ai-video-editing-system](https://github.com/dhruvthakur11/youtube-ai-video-editing-system)<br>Struggling with video edits? Let agents handle animations | 2026-11-06<br><sub>1.7 d</sub> | 244 | 145.0 |
| 8 | [AbhiKamane/ai-app-builder-open](https://github.com/AbhiKamane/ai-app-builder-open)<br>Need a full-stack Next.js app? Let AI build and host it | 2026-11-06<br><sub>1.7 d</sub> | 244 | 141.5 |
| 9 | [dabingfy-dot/solo-to-team-skills](https://github.com/dabingfy-dot/solo-to-team-skills)<br>Delegate work across your AI team | 2026-11-07<br><sub>1.5 d</sub> | 206 | 136.1 |
| 10 | [yucezerey/turkish-anti-ai-skill](https://github.com/yucezerey/turkish-anti-ai-skill)<br>Remove AI traces from Turkish writing | 2026-11-05<br><sub>2.7 d</sub> | 265 | 96.7 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#KKKKhazix/agent-autoloop&Date"><img src="https://api.star-history.com/svg?repos=KKKKhazix/agent-autoloop&type=Date" width="260" alt="star history KKKKhazix/agent-autoloop"></a>

<a href="https://www.star-history.com/#voyager-so/vork&Date"><img src="https://api.star-history.com/svg?repos=voyager-so/vork&type=Date" width="260" alt="star history voyager-so/vork"></a>

<a href="https://www.star-history.com/#Sandflow-ai/sand3d&Date"><img src="https://api.star-history.com/svg?repos=Sandflow-ai/sand3d&type=Date" width="260" alt="star history Sandflow-ai/sand3d"></a>

<a href="https://www.star-history.com/#JosssphZhou/poki&Date"><img src="https://api.star-history.com/svg?repos=JosssphZhou/poki&type=Date" width="260" alt="star history JosssphZhou/poki"></a>

<a href="https://www.star-history.com/#HerdBuilderEstimate/roblox-studio-mcp&Date"><img src="https://api.star-history.com/svg?repos=HerdBuilderEstimate/roblox-studio-mcp&type=Date" width="260" alt="star history HerdBuilderEstimate/roblox-studio-mcp"></a>

<a href="https://www.star-history.com/#shanselman/sandbox-mcp&Date"><img src="https://api.star-history.com/svg?repos=shanselman/sandbox-mcp&type=Date" width="260" alt="star history shanselman/sandbox-mcp"></a>

<a href="https://www.star-history.com/#dhruvthakur11/youtube-ai-video-editing-system&Date"><img src="https://api.star-history.com/svg?repos=dhruvthakur11/youtube-ai-video-editing-system&type=Date" width="260" alt="star history dhruvthakur11/youtube-ai-video-editing-system"></a>

<a href="https://www.star-history.com/#AbhiKamane/ai-app-builder-open&Date"><img src="https://api.star-history.com/svg?repos=AbhiKamane/ai-app-builder-open&type=Date" width="260" alt="star history AbhiKamane/ai-app-builder-open"></a>

<a href="https://www.star-history.com/#dabingfy-dot/solo-to-team-skills&Date"><img src="https://api.star-history.com/svg?repos=dabingfy-dot/solo-to-team-skills&type=Date" width="260" alt="star history dabingfy-dot/solo-to-team-skills"></a>

<a href="https://www.star-history.com/#yucezerey/turkish-anti-ai-skill&Date"><img src="https://api.star-history.com/svg?repos=yucezerey/turkish-anti-ai-skill&type=Date" width="260" alt="star history yucezerey/turkish-anti-ai-skill"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>Let AI clone any software for you<br>`AI` | +26,291 | 3,755.9 | 442,531 |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>One AI hunts security holes, a fresh AI verifies each<br>`AI` | +10,640 | 1,520.0 | 66,383 |
| 3 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>Pick plugins and build the agent you want<br>`AI` | +8,652 | 1,236.0 | 276,208 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca)<br>Several AIs write at once, see which one works best<br>`AI` | +7,111 | 1,015.9 | 118,981 |
| 5 | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)<br>AI no longer forgets where it left off<br>`AI` | +6,613 | 944.7 | 114,702 |
| 6 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>Give your coding AI memory, skills and safety checks<br>`AI` | +5,409 | 772.7 | 299,453 |
| 7 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>Less filler code from AI, the needed code done right<br>`AI` | +5,080 | 725.7 | 186,685 |
| 8 | [yetone/magpie](https://github.com/yetone/magpie)<br>Swap models in your coding AI; quota runs out, it carries on<br>`AI` | +4,955 | 707.9 | 32,109 |
| 9 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)<br>Stop AI from making every page look the same<br>`AI` | +4,664 | 666.3 | 111,881 |
| 10 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>Too big to read? Start with this map of the code<br>`AI` | +4,125 | 589.3 | 144,252 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="star history morluto/rea"></a>

<a href="https://www.star-history.com/#cloudflare/security-audit-skill&Date"><img src="https://api.star-history.com/svg?repos=cloudflare/security-audit-skill&type=Date" width="260" alt="star history cloudflare/security-audit-skill"></a>

<a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="star history deepseek-ai/deepseek-harness"></a>

<a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="star history stablyai/orca"></a>

<a href="https://www.star-history.com/#thedotmack/claude-mem&Date"><img src="https://api.star-history.com/svg?repos=thedotmack/claude-mem&type=Date" width="260" alt="star history thedotmack/claude-mem"></a>

<a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="star history affaan-m/ECC"></a>

<a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="star history DietrichGebert/ponytail"></a>

<a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="star history yetone/magpie"></a>

<a href="https://www.star-history.com/#Leonxlnx/taste-skill&Date"><img src="https://api.star-history.com/svg?repos=Leonxlnx/taste-skill&type=Date" width="260" alt="star history Leonxlnx/taste-skill"></a>

<a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="star history Graphify-Labs/graphify"></a>

</details>

### Fastest rising this month (last 30 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>Let AI clone any software for you<br>`AI` | +411,287 | 13,709.6 | 442,531 |
| 2 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)<br>One AI hunts security holes, a fresh AI verifies each<br>`AI` | +39,659 | 1,322.0 | 66,383 |
| 3 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>Pick plugins and build the agent you want<br>`AI` | +31,355 | 1,045.2 | 276,208 |
| 4 | [stablyai/orca](https://github.com/stablyai/orca)<br>Several AIs write at once, see which one works best<br>`AI` | +31,330 | 1,044.3 | 118,981 |
| 5 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>Less filler code from AI, the needed code done right<br>`AI` | +28,606 | 953.5 | 186,685 |
| 6 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>Give your coding AI memory, skills and safety checks<br>`AI` | +25,141 | 838.0 | 299,453 |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>Swap models in your coding AI; quota runs out, it carries on<br>`AI` | +25,117 | 837.2 | 32,109 |
| 8 | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)<br>Can't edit video? Write it like a web page<br>`AI` | +21,696 | 723.2 | 80,844 |
| 9 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>Too big to read? Start with this map of the code<br>`AI` | +19,881 | 662.7 | 144,252 |
| 10 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)<br>Stop AI from making every page look the same<br>`AI` | +18,378 | 612.6 | 111,881 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#morluto/rea&Date"><img src="https://api.star-history.com/svg?repos=morluto/rea&type=Date" width="260" alt="star history morluto/rea"></a>

<a href="https://www.star-history.com/#cloudflare/security-audit-skill&Date"><img src="https://api.star-history.com/svg?repos=cloudflare/security-audit-skill&type=Date" width="260" alt="star history cloudflare/security-audit-skill"></a>

<a href="https://www.star-history.com/#deepseek-ai/deepseek-harness&Date"><img src="https://api.star-history.com/svg?repos=deepseek-ai/deepseek-harness&type=Date" width="260" alt="star history deepseek-ai/deepseek-harness"></a>

<a href="https://www.star-history.com/#stablyai/orca&Date"><img src="https://api.star-history.com/svg?repos=stablyai/orca&type=Date" width="260" alt="star history stablyai/orca"></a>

<a href="https://www.star-history.com/#DietrichGebert/ponytail&Date"><img src="https://api.star-history.com/svg?repos=DietrichGebert/ponytail&type=Date" width="260" alt="star history DietrichGebert/ponytail"></a>

<a href="https://www.star-history.com/#affaan-m/ECC&Date"><img src="https://api.star-history.com/svg?repos=affaan-m/ECC&type=Date" width="260" alt="star history affaan-m/ECC"></a>

<a href="https://www.star-history.com/#yetone/magpie&Date"><img src="https://api.star-history.com/svg?repos=yetone/magpie&type=Date" width="260" alt="star history yetone/magpie"></a>

<a href="https://www.star-history.com/#heygen-com/hyperframes&Date"><img src="https://api.star-history.com/svg?repos=heygen-com/hyperframes&type=Date" width="260" alt="star history heygen-com/hyperframes"></a>

<a href="https://www.star-history.com/#Graphify-Labs/graphify&Date"><img src="https://api.star-history.com/svg?repos=Graphify-Labs/graphify&type=Date" width="260" alt="star history Graphify-Labs/graphify"></a>

<a href="https://www.star-history.com/#Leonxlnx/taste-skill&Date"><img src="https://api.star-history.com/svg?repos=Leonxlnx/taste-skill&type=Date" width="260" alt="star history Leonxlnx/taste-skill"></a>

</details>

### Fastest rising this year (last 365 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>Pick plugins and build the agent you want<br>`AI` | +275,971 | 3,172.1 †<br><sub>÷87d</sub> | 276,208 |
| 2 | [morluto/rea](https://github.com/morluto/rea)<br>Let AI clone any software for you<br>`AI` | +441,766 | 2,123.9 †<br><sub>÷208d</sub> | 442,531 |
| 3 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>Less filler code from AI, the needed code done right<br>`AI` | +186,518 | 1,251.8 †<br><sub>÷149d</sub> | 186,685 |
| 4 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>An AI assistant that gets things done, on your own devices<br>`AI` | +394,146 | 1,129.4 †<br><sub>÷349d</sub> | 394,178 |
| 5 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>Give your coding AI memory, skills and safety checks<br>`AI` | +299,307 | 1,018.1 †<br><sub>÷294d</sub> | 299,453 |
| 6 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>An AI helper that gets better the more you use it<br>`AI` | +261,559 | 716.6 | 261,632 |
| 7 | [yetone/magpie](https://github.com/yetone/magpie)<br>Swap models in your coding AI; quota runs out, it carries on<br>`AI` | +31,972 | 695.0 †<br><sub>÷46d</sub> | 32,109 |
| 8 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)<br>Too big to read? Start with this map of the code<br>`AI` | +144,110 | 658.0 †<br><sub>÷219d</sub> | 144,252 |
| 9 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>An open-source AI that writes code in your terminal<br>`AI` | +194,675 | 533.4 | 225,417 |
| 10 | [stablyai/orca](https://github.com/stablyai/orca)<br>Several AIs write at once, see which one works best<br>`AI` | +118,790 | 503.3 †<br><sub>÷236d</sub> | 118,981 |

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
| 1 | [morluto/rea](https://github.com/morluto/rea)<br>Let AI clone any software for you<br>`AI` | 442,531 |
| 2 | [openclaw/openclaw](https://github.com/openclaw/openclaw)<br>An AI assistant that gets things done, on your own devices<br>`AI` | 394,178 |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC)<br>Give your coding AI memory, skills and safety checks<br>`AI` | 299,453 |
| 4 | [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)<br>Pick plugins and build the agent you want<br>`AI` | 276,208 |
| 5 | [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)<br>An AI helper that gets better the more you use it<br>`AI` | 261,632 |
| 6 | [anomalyco/opencode](https://github.com/anomalyco/opencode)<br>An open-source AI that writes code in your terminal<br>`AI` | 225,417 |
| 7 | [anthropics/skills](https://github.com/anthropics/skills)<br>Learn to write Claude skills from the official examples<br>`AI` | 189,197 |
| 8 | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)<br>Less filler code from AI, the needed code done right<br>`AI` | 186,685 |
| 9 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch)<br>Switch providers in one click, no config editing<br>`AI` | 152,703 |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)<br>UIs built by AI that look professionally designed<br>`AI` | 146,760 |

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
| 1 | [govijr/terminal-mac](https://github.com/govijr/terminal-mac)<br>Don't leave the terminal; run full MacOS right inside it | 2026-11-03<br><sub>5.4 d</sub> | 2,343 | 430.7 |
| 2 | [PaladinSmash84/aida-64-extreme](https://github.com/PaladinSmash84/aida-64-extreme)<br>Aida 64 Extreme local deployment environment | 2026-11-08<br><sub>1.0 d</sub> | 302 | 302.0 |
| 3 | [OhmUrchinSee/abbyy-finereader-pdf](https://github.com/OhmUrchinSee/abbyy-finereader-pdf)<br>Abbyy Finereader Pdf 18.5 desktop deployment pipeline | 2026-11-08<br><sub>1.0 d</sub> | 300 | 300.0 |
| 4 | [Outsideclofilter/aion-2-trainer-tool](https://github.com/Outsideclofilter/aion-2-trainer-tool)<br>Aion 2 prompt engineering environment for local deployment | 2026-11-08<br><sub>1.0 d</sub> | 300 | 300.0 |
| 5 | [Perceptionzyavalue/ashampoo-uninstaller](https://github.com/Perceptionzyavalue/ashampoo-uninstaller)<br>Ashampoo Uninstaller 1.3.5 desktop deployment pipeline | 2026-11-08<br><sub>1.0 d</sub> | 300 | 300.0 |
| 6 | [PerfumerExcite/ashampoo-winoptimizer](https://github.com/PerfumerExcite/ashampoo-winoptimizer)<br>Ashampoo Winoptimizer 17.0 desktop setup environment | 2026-11-08<br><sub>1.0 d</sub> | 300 | 300.0 |
| 7 | [PoltergeistDisplay/borisfx](https://github.com/PoltergeistDisplay/borisfx)<br>BorisFX 2024 pre-configured environment for professional video editing, screen recording, and visual effects workflows. | 2026-11-08<br><sub>1.0 d</sub> | 300 | 300.0 |
| 8 | [PsycheGradeSpeak/chief-architect-premier](https://github.com/PsycheGradeSpeak/chief-architect-premier)<br>Chief Architect Premier 2026 pre-configured environment for seamless automated deployment pipeline in professional desktop software utility. | 2026-11-08<br><sub>1.0 d</sub> | 300 | 300.0 |
| 9 | [PurpleChordEvaluate/claude-jailbreak-prompt](https://github.com/PurpleChordEvaluate/claude-jailbreak-prompt)<br>Optimized local environment suite for Claude AI pipeline management and custom automation workflows. | 2026-11-08<br><sub>1.0 d</sub> | 300 | 300.0 |
| 10 | [Quantumoarefresh/daemon-pro](https://github.com/Quantumoarefresh/daemon-pro)<br>Daemon Pro 2024, pre-configured environment for seamless automated deployment pipeline on professional desktop software utility. | 2026-11-08<br><sub>1.0 d</sub> | 300 | 300.0 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#govijr/terminal-mac&Date"><img src="https://api.star-history.com/svg?repos=govijr/terminal-mac&type=Date" width="260" alt="star history govijr/terminal-mac"></a>

<a href="https://www.star-history.com/#PaladinSmash84/aida-64-extreme&Date"><img src="https://api.star-history.com/svg?repos=PaladinSmash84/aida-64-extreme&type=Date" width="260" alt="star history PaladinSmash84/aida-64-extreme"></a>

<a href="https://www.star-history.com/#OhmUrchinSee/abbyy-finereader-pdf&Date"><img src="https://api.star-history.com/svg?repos=OhmUrchinSee/abbyy-finereader-pdf&type=Date" width="260" alt="star history OhmUrchinSee/abbyy-finereader-pdf"></a>

<a href="https://www.star-history.com/#Outsideclofilter/aion-2-trainer-tool&Date"><img src="https://api.star-history.com/svg?repos=Outsideclofilter/aion-2-trainer-tool&type=Date" width="260" alt="star history Outsideclofilter/aion-2-trainer-tool"></a>

<a href="https://www.star-history.com/#Perceptionzyavalue/ashampoo-uninstaller&Date"><img src="https://api.star-history.com/svg?repos=Perceptionzyavalue/ashampoo-uninstaller&type=Date" width="260" alt="star history Perceptionzyavalue/ashampoo-uninstaller"></a>

<a href="https://www.star-history.com/#PerfumerExcite/ashampoo-winoptimizer&Date"><img src="https://api.star-history.com/svg?repos=PerfumerExcite/ashampoo-winoptimizer&type=Date" width="260" alt="star history PerfumerExcite/ashampoo-winoptimizer"></a>

<a href="https://www.star-history.com/#PoltergeistDisplay/borisfx&Date"><img src="https://api.star-history.com/svg?repos=PoltergeistDisplay/borisfx&type=Date" width="260" alt="star history PoltergeistDisplay/borisfx"></a>

<a href="https://www.star-history.com/#PsycheGradeSpeak/chief-architect-premier&Date"><img src="https://api.star-history.com/svg?repos=PsycheGradeSpeak/chief-architect-premier&type=Date" width="260" alt="star history PsycheGradeSpeak/chief-architect-premier"></a>

<a href="https://www.star-history.com/#PurpleChordEvaluate/claude-jailbreak-prompt&Date"><img src="https://api.star-history.com/svg?repos=PurpleChordEvaluate/claude-jailbreak-prompt&type=Date" width="260" alt="star history PurpleChordEvaluate/claude-jailbreak-prompt"></a>

<a href="https://www.star-history.com/#Quantumoarefresh/daemon-pro&Date"><img src="https://api.star-history.com/svg?repos=Quantumoarefresh/daemon-pro&type=Date" width="260" alt="star history Quantumoarefresh/daemon-pro"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>Opens fast, and you can code together with others<br>`Developer Tools` | +1,982 | 283.1 | 94,434 |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Install Python packages without the wait<br>`Developer Tools` | +403 | 57.6 | 91,765 |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>Dev tools, env variables and tasks, in one tool<br>`Developer Tools` | +342 | 48.9 | 35,929 |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>Search a whole folder for text, faster than grep<br>`Developer Tools` | +330 | 47.1 | 69,893 |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>Run, bundle, test, install: one tool does it all<br>`Developer Tools` | +257 | 36.7 | 96,703 |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>A text editor with language server and highlighting built in<br>`Developer Tools` | +183 | 26.1 | 46,917 |
| 7 | [cli/cli](https://github.com/cli/cli)<br>Handle GitHub from the command line, no browser<br>`Developer Tools` | +106 | 15.1 | 46,916 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Format and check web code with one tool<br>`Developer Tools` | +43 | 6.1 | 26,058 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="star history zed-industries/zed"></a>

<a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="star history astral-sh/uv"></a>

<a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="star history jdx/mise"></a>

<a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="star history BurntSushi/ripgrep"></a>

<a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="star history oven-sh/bun"></a>

<a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="star history helix-editor/helix"></a>

<a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="star history cli/cli"></a>

<a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="star history biomejs/biome"></a>

</details>

### Fastest rising this month (last 30 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>Opens fast, and you can code together with others<br>`Developer Tools` | +3,197 | 106.6 | 94,434 |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Install Python packages without the wait<br>`Developer Tools` | +1,420 | 47.3 | 91,765 |
| 3 | [jdx/mise](https://github.com/jdx/mise)<br>Dev tools, env variables and tasks, in one tool<br>`Developer Tools` | +1,207 | 40.2 | 35,929 |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>Search a whole folder for text, faster than grep<br>`Developer Tools` | +1,096 | 36.5 | 69,893 |
| 5 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>Run, bundle, test, install: one tool does it all<br>`Developer Tools` | +824 | 27.5 | 96,703 |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>A text editor with language server and highlighting built in<br>`Developer Tools` | +518 | 17.3 | 46,917 |
| 7 | [cli/cli](https://github.com/cli/cli)<br>Handle GitHub from the command line, no browser<br>`Developer Tools` | +439 | 14.6 | 46,916 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Format and check web code with one tool<br>`Developer Tools` | +218 | 7.3 | 26,058 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="star history zed-industries/zed"></a>

<a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="star history astral-sh/uv"></a>

<a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="star history jdx/mise"></a>

<a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="star history BurntSushi/ripgrep"></a>

<a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="star history oven-sh/bun"></a>

<a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="star history helix-editor/helix"></a>

<a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="star history cli/cli"></a>

<a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="star history biomejs/biome"></a>

</details>

### Fastest rising this year (last 365 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>Opens fast, and you can code together with others<br>`Developer Tools` | +27,134 | 74.3 | 94,434 |
| 2 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Install Python packages without the wait<br>`Developer Tools` | +21,053 | 57.7 | 91,765 |
| 3 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>Run, bundle, test, install: one tool does it all<br>`Developer Tools` | +16,645 | 45.6 | 96,703 |
| 4 | [jdx/mise](https://github.com/jdx/mise)<br>Dev tools, env variables and tasks, in one tool<br>`Developer Tools` | +15,159 | 41.5 | 35,929 |
| 5 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>Search a whole folder for text, faster than grep<br>`Developer Tools` | +13,467 | 36.9 | 69,893 |
| 6 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>A text editor with language server and highlighting built in<br>`Developer Tools` | +6,670 | 18.3 | 46,917 |
| 7 | [cli/cli](https://github.com/cli/cli)<br>Handle GitHub from the command line, no browser<br>`Developer Tools` | +6,272 | 17.2 | 46,916 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Format and check web code with one tool<br>`Developer Tools` | +4,485 | 12.3 | 26,058 |

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
| 1 | [oven-sh/bun](https://github.com/oven-sh/bun)<br>Run, bundle, test, install: one tool does it all<br>`Developer Tools` | 96,703 |
| 2 | [zed-industries/zed](https://github.com/zed-industries/zed)<br>Opens fast, and you can code together with others<br>`Developer Tools` | 94,434 |
| 3 | [astral-sh/uv](https://github.com/astral-sh/uv)<br>Install Python packages without the wait<br>`Developer Tools` | 91,765 |
| 4 | [BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)<br>Search a whole folder for text, faster than grep<br>`Developer Tools` | 69,893 |
| 5 | [helix-editor/helix](https://github.com/helix-editor/helix)<br>A text editor with language server and highlighting built in<br>`Developer Tools` | 46,917 |
| 6 | [cli/cli](https://github.com/cli/cli)<br>Handle GitHub from the command line, no browser<br>`Developer Tools` | 46,916 |
| 7 | [jdx/mise](https://github.com/jdx/mise)<br>Dev tools, env variables and tasks, in one tool<br>`Developer Tools` | 35,929 |
| 8 | [biomejs/biome](https://github.com/biomejs/biome)<br>Format and check web code with one tool<br>`Developer Tools` | 26,058 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#oven-sh/bun&Date"><img src="https://api.star-history.com/svg?repos=oven-sh/bun&type=Date" width="260" alt="star history oven-sh/bun"></a>

<a href="https://www.star-history.com/#zed-industries/zed&Date"><img src="https://api.star-history.com/svg?repos=zed-industries/zed&type=Date" width="260" alt="star history zed-industries/zed"></a>

<a href="https://www.star-history.com/#astral-sh/uv&Date"><img src="https://api.star-history.com/svg?repos=astral-sh/uv&type=Date" width="260" alt="star history astral-sh/uv"></a>

<a href="https://www.star-history.com/#BurntSushi/ripgrep&Date"><img src="https://api.star-history.com/svg?repos=BurntSushi/ripgrep&type=Date" width="260" alt="star history BurntSushi/ripgrep"></a>

<a href="https://www.star-history.com/#helix-editor/helix&Date"><img src="https://api.star-history.com/svg?repos=helix-editor/helix&type=Date" width="260" alt="star history helix-editor/helix"></a>

<a href="https://www.star-history.com/#cli/cli&Date"><img src="https://api.star-history.com/svg?repos=cli/cli&type=Date" width="260" alt="star history cli/cli"></a>

<a href="https://www.star-history.com/#jdx/mise&Date"><img src="https://api.star-history.com/svg?repos=jdx/mise&type=Date" width="260" alt="star history jdx/mise"></a>

<a href="https://www.star-history.com/#biomejs/biome&Date"><img src="https://api.star-history.com/svg?repos=biomejs/biome&type=Date" width="260" alt="star history biomejs/biome"></a>

</details>

## Security

> Vulnerability scanners, SAST, supply-chain and runtime security

### Hottest new repos (created in the last 7 days)

| # | Project | Created (UTC) | Total stars | Stars/day |
|---|---|---|---:|---:|
| 1 | [yorkeccak/globalhackmap](https://github.com/yorkeccak/globalhackmap)<br>See live security incidents on one globe | 2026-11-02<br><sub>5.9 d</sub> | 129 | 22.0 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#yorkeccak/globalhackmap&Date"><img src="https://api.star-history.com/svg?repos=yorkeccak/globalhackmap&type=Date" width="260" alt="star history yorkeccak/globalhackmap"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>Scan containers and code repos for security issues at once<br>`Security` | +238 | 34.0 | 39,116 |
| 2 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>Write one template, scan for vulnerabilities in bulk<br>`Security` | +176 | 25.1 | 32,676 |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>Catch the problems in your code before you commit<br>`Security` | +170 | 24.3 | 17,551 |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>Concise cheat sheets on application security<br>`Security` | +122 | 17.4 | 33,943 |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>Are your dependencies safe? One scan tells you<br>`Security` | +115 | 16.4 | 11,453 |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>Does your container image have vulnerabilities? Scan it<br>`Security` | +60 | 8.6 | 13,211 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>Know the moment something odd happens in the cloud<br>`Security` | +21 | 3.0 | 9,561 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Scan your Go code for security problems<br>`Security` | +7 | 1.0 | 9,001 |

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
| 1 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>Write one template, scan for vulnerabilities in bulk<br>`Security` | +907 | 30.2 | 32,676 |
| 2 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>Scan containers and code repos for security issues at once<br>`Security` | +861 | 28.7 | 39,116 |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>Catch the problems in your code before you commit<br>`Security` | +639 | 21.3 | 17,551 |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>Concise cheat sheets on application security<br>`Security` | +419 | 14.0 | 33,943 |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>Are your dependencies safe? One scan tells you<br>`Security` | +321 | 10.7 | 11,453 |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>Does your container image have vulnerabilities? Scan it<br>`Security` | +228 | 7.6 | 13,211 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>Know the moment something odd happens in the cloud<br>`Security` | +113 | 3.8 | 9,561 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Scan your Go code for security problems<br>`Security` | +44 | 1.5 | 9,001 |

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

### Fastest rising this year (last 365 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>Scan containers and code repos for security issues at once<br>`Security` | +10,229 | 28.0 | 39,116 |
| 2 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>Write one template, scan for vulnerabilities in bulk<br>`Security` | +7,679 | 21.0 | 32,676 |
| 3 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>Catch the problems in your code before you commit<br>`Security` | +4,465 | 12.2 | 17,551 |
| 4 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>Concise cheat sheets on application security<br>`Security` | +3,581 | 9.8 | 33,943 |
| 5 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>Are your dependencies safe? One scan tells you<br>`Security` | +3,556 | 9.7 | 11,453 |
| 6 | [anchore/grype](https://github.com/anchore/grype)<br>Does your container image have vulnerabilities? Scan it<br>`Security` | +2,365 | 6.5 | 13,211 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>Know the moment something odd happens in the cloud<br>`Security` | +1,270 | 3.5 | 9,561 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Scan your Go code for security problems<br>`Security` | +561 | 1.5 | 9,001 |

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
| 1 | [aquasecurity/trivy](https://github.com/aquasecurity/trivy)<br>Scan containers and code repos for security issues at once<br>`Security` | 39,116 |
| 2 | [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries)<br>Concise cheat sheets on application security<br>`Security` | 33,943 |
| 3 | [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)<br>Write one template, scan for vulnerabilities in bulk<br>`Security` | 32,676 |
| 4 | [semgrep/semgrep](https://github.com/semgrep/semgrep)<br>Catch the problems in your code before you commit<br>`Security` | 17,551 |
| 5 | [anchore/grype](https://github.com/anchore/grype)<br>Does your container image have vulnerabilities? Scan it<br>`Security` | 13,211 |
| 6 | [google/osv-scanner](https://github.com/google/osv-scanner)<br>Are your dependencies safe? One scan tells you<br>`Security` | 11,453 |
| 7 | [falcosecurity/falco](https://github.com/falcosecurity/falco)<br>Know the moment something odd happens in the cloud<br>`Security` | 9,561 |
| 8 | [securego/gosec](https://github.com/securego/gosec)<br>Scan your Go code for security problems<br>`Security` | 9,001 |

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
| 1 | [AtomIllusionistDwell/watson-username-footprint-finder](https://github.com/AtomIllusionistDwell/watson-username-footprint-finder)<br>Turn public-page people searches into one readable report | 2026-11-05<br><sub>3.4 d</sub> | 414 | 123.3 |
| 2 | [zeemscript/block-roll](https://github.com/zeemscript/block-roll)<br>Store and share encrypted files | 2026-11-05<br><sub>3.6 d</sub> | 164 | 45.9 |
| 3 | [YusufCeng1z/ding](https://github.com/YusufCeng1z/ding)<br>Toasts with real spring physics. One toast that morphs in place. No dependencies. React, Svelte and plain DOM. | 2026-11-05<br><sub>3.3 d</sub> | 145 | 44.1 |
| 4 | [lijiaqi-AI-Product-Manager/dsh-agent-compare](https://github.com/lijiaqi-AI-Product-Manager/dsh-agent-compare)<br>Try two working versions before choosing one | 2026-11-02<br><sub>6.6 d</sub> | 236 | 35.9 |
| 5 | [smokeeaasd/flawless-ui-ux](https://github.com/smokeeaasd/flawless-ui-ux)<br>A UI/UX skill for coding agents to build distinctive, usable interfaces. | 2026-11-03<br><sub>5.0 d</sub> | 101 | 20.3 |
| 6 | [spiderveer1-byte/play-reactive-slick](https://github.com/spiderveer1-byte/play-reactive-slick)<br>Play + Postgres starter template with a clean UI | 2026-11-06<br><sub>2.0 d</sub> | 149 | 75.4 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#AtomIllusionistDwell/watson-username-footprint-finder&Date"><img src="https://api.star-history.com/svg?repos=AtomIllusionistDwell/watson-username-footprint-finder&type=Date" width="260" alt="star history AtomIllusionistDwell/watson-username-footprint-finder"></a>

<a href="https://www.star-history.com/#zeemscript/block-roll&Date"><img src="https://api.star-history.com/svg?repos=zeemscript/block-roll&type=Date" width="260" alt="star history zeemscript/block-roll"></a>

<a href="https://www.star-history.com/#YusufCeng1z/ding&Date"><img src="https://api.star-history.com/svg?repos=YusufCeng1z/ding&type=Date" width="260" alt="star history YusufCeng1z/ding"></a>

<a href="https://www.star-history.com/#lijiaqi-AI-Product-Manager/dsh-agent-compare&Date"><img src="https://api.star-history.com/svg?repos=lijiaqi-AI-Product-Manager/dsh-agent-compare&type=Date" width="260" alt="star history lijiaqi-AI-Product-Manager/dsh-agent-compare"></a>

<a href="https://www.star-history.com/#smokeeaasd/flawless-ui-ux&Date"><img src="https://api.star-history.com/svg?repos=smokeeaasd/flawless-ui-ux&type=Date" width="260" alt="star history smokeeaasd/flawless-ui-ux"></a>

<a href="https://www.star-history.com/#spiderveer1-byte/play-reactive-slick&Date"><img src="https://api.star-history.com/svg?repos=spiderveer1-byte/play-reactive-slick&type=Date" width="260" alt="star history spiderveer1-byte/play-reactive-slick"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [facebook/react](https://github.com/facebook/react)<br>Build web and native app interfaces with one library<br>`Web / Frontend` | +678 | 96.9 | 252,408 |
| 2 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>Custom designs without writing a pile of CSS<br>`Web / Frontend` | +616 | 88.0 | 98,646 |
| 3 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>Good-looking components, and the code is yours to change<br>`Web / Frontend` | +591 | 84.4 | 127,619 |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>Build a whole site with React, front to back<br>`Web / Frontend` | +247 | 35.3 | 143,419 |
| 5 | [withastro/astro](https://github.com/withastro/astro)<br>For content-driven websites, with lightweight output<br>`Web / Frontend` | +205 | 29.3 | 63,814 |
| 6 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>A compiler turns your components into efficient web code<br>`Web / Frontend` | +192 | 27.4 | 88,668 |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>Start with one small page, learn only what you use<br>`Web / Frontend` | +80 | 11.4 | 54,856 |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>Fetching data and caching it? Leave it to this<br>`Web / Frontend` | +48 | 6.9 | 50,538 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="star history facebook/react"></a>

<a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="star history tailwindlabs/tailwindcss"></a>

<a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="star history shadcn-ui/ui"></a>

<a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="star history vercel/next.js"></a>

<a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="star history withastro/astro"></a>

<a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="star history sveltejs/svelte"></a>

<a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="star history vuejs/core"></a>

<a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="star history tanstack/query"></a>

</details>

### Fastest rising this month (last 30 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>Good-looking components, and the code is yours to change<br>`Web / Frontend` | +2,723 | 90.8 | 127,619 |
| 2 | [facebook/react](https://github.com/facebook/react)<br>Build web and native app interfaces with one library<br>`Web / Frontend` | +2,089 | 69.6 | 252,408 |
| 3 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>Custom designs without writing a pile of CSS<br>`Web / Frontend` | +989 | 33.0 | 98,646 |
| 4 | [withastro/astro](https://github.com/withastro/astro)<br>For content-driven websites, with lightweight output<br>`Web / Frontend` | +796 | 26.5 | 63,814 |
| 5 | [vercel/next.js](https://github.com/vercel/next.js)<br>Build a whole site with React, front to back<br>`Web / Frontend` | +788 | 26.3 | 143,419 |
| 6 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>A compiler turns your components into efficient web code<br>`Web / Frontend` | +584 | 19.5 | 88,668 |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>Start with one small page, learn only what you use<br>`Web / Frontend` | +423 | 14.1 | 54,856 |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>Fetching data and caching it? Leave it to this<br>`Web / Frontend` | +206 | 6.9 | 50,538 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#shadcn-ui/ui&Date"><img src="https://api.star-history.com/svg?repos=shadcn-ui/ui&type=Date" width="260" alt="star history shadcn-ui/ui"></a>

<a href="https://www.star-history.com/#facebook/react&Date"><img src="https://api.star-history.com/svg?repos=facebook/react&type=Date" width="260" alt="star history facebook/react"></a>

<a href="https://www.star-history.com/#tailwindlabs/tailwindcss&Date"><img src="https://api.star-history.com/svg?repos=tailwindlabs/tailwindcss&type=Date" width="260" alt="star history tailwindlabs/tailwindcss"></a>

<a href="https://www.star-history.com/#withastro/astro&Date"><img src="https://api.star-history.com/svg?repos=withastro/astro&type=Date" width="260" alt="star history withastro/astro"></a>

<a href="https://www.star-history.com/#vercel/next.js&Date"><img src="https://api.star-history.com/svg?repos=vercel/next.js&type=Date" width="260" alt="star history vercel/next.js"></a>

<a href="https://www.star-history.com/#sveltejs/svelte&Date"><img src="https://api.star-history.com/svg?repos=sveltejs/svelte&type=Date" width="260" alt="star history sveltejs/svelte"></a>

<a href="https://www.star-history.com/#vuejs/core&Date"><img src="https://api.star-history.com/svg?repos=vuejs/core&type=Date" width="260" alt="star history vuejs/core"></a>

<a href="https://www.star-history.com/#tanstack/query&Date"><img src="https://api.star-history.com/svg?repos=tanstack/query&type=Date" width="260" alt="star history tanstack/query"></a>

</details>

### Fastest rising this year (last 365 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>Good-looking components, and the code is yours to change<br>`Web / Frontend` | +30,397 | 83.3 | 127,619 |
| 2 | [facebook/react](https://github.com/facebook/react)<br>Build web and native app interfaces with one library<br>`Web / Frontend` | +15,616 | 42.8 | 252,408 |
| 3 | [withastro/astro](https://github.com/withastro/astro)<br>For content-driven websites, with lightweight output<br>`Web / Frontend` | +10,539 | 28.9 | 63,814 |
| 4 | [vercel/next.js](https://github.com/vercel/next.js)<br>Build a whole site with React, front to back<br>`Web / Frontend` | +10,412 | 28.5 | 143,419 |
| 5 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>Custom designs without writing a pile of CSS<br>`Web / Frontend` | +9,009 | 24.7 | 98,646 |
| 6 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>A compiler turns your components into efficient web code<br>`Web / Frontend` | +5,243 | 14.4 | 88,668 |
| 7 | [tanstack/query](https://github.com/tanstack/query)<br>Fetching data and caching it? Leave it to this<br>`Web / Frontend` | +3,790 | 10.4 | 50,538 |
| 8 | [vuejs/core](https://github.com/vuejs/core)<br>Start with one small page, learn only what you use<br>`Web / Frontend` | +3,607 | 9.9 | 54,856 |

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
| 1 | [facebook/react](https://github.com/facebook/react)<br>Build web and native app interfaces with one library<br>`Web / Frontend` | 252,408 |
| 2 | [vercel/next.js](https://github.com/vercel/next.js)<br>Build a whole site with React, front to back<br>`Web / Frontend` | 143,419 |
| 3 | [shadcn-ui/ui](https://github.com/shadcn-ui/ui)<br>Good-looking components, and the code is yours to change<br>`Web / Frontend` | 127,619 |
| 4 | [tailwindlabs/tailwindcss](https://github.com/tailwindlabs/tailwindcss)<br>Custom designs without writing a pile of CSS<br>`Web / Frontend` | 98,646 |
| 5 | [sveltejs/svelte](https://github.com/sveltejs/svelte)<br>A compiler turns your components into efficient web code<br>`Web / Frontend` | 88,668 |
| 6 | [withastro/astro](https://github.com/withastro/astro)<br>For content-driven websites, with lightweight output<br>`Web / Frontend` | 63,814 |
| 7 | [vuejs/core](https://github.com/vuejs/core)<br>Start with one small page, learn only what you use<br>`Web / Frontend` | 54,856 |
| 8 | [tanstack/query](https://github.com/tanstack/query)<br>Fetching data and caching it? Leave it to this<br>`Web / Frontend` | 50,538 |

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
| 1 | [MuseumCassowaryCarve/twitch-drops-miner](https://github.com/MuseumCassowaryCarve/twitch-drops-miner)<br>Claim Twitch drops in the background with no video download | 2026-11-08<br><sub>1.0 d</sub> | 417 | 417.0 |
| 2 | [Fragokemymy/penr-oz-play](https://github.com/Fragokemymy/penr-oz-play)<br>Play Framework REST API with Docker deployment | 2026-11-06<br><sub>2.0 d</sub> | 149 | 75.3 |
| 3 | [balkewkidane/grizl-fabric-observability](https://github.com/balkewkidane/grizl-fabric-observability)<br>Fabric Eventhouse and KQL observability library | 2026-11-06<br><sub>2.0 d</sub> | 149 | 75.0 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#MuseumCassowaryCarve/twitch-drops-miner&Date"><img src="https://api.star-history.com/svg?repos=MuseumCassowaryCarve/twitch-drops-miner&type=Date" width="260" alt="star history MuseumCassowaryCarve/twitch-drops-miner"></a>

<a href="https://www.star-history.com/#Fragokemymy/penr-oz-play&Date"><img src="https://api.star-history.com/svg?repos=Fragokemymy/penr-oz-play&type=Date" width="260" alt="star history Fragokemymy/penr-oz-play"></a>

<a href="https://www.star-history.com/#balkewkidane/grizl-fabric-observability&Date"><img src="https://api.star-history.com/svg?repos=balkewkidane/grizl-fabric-observability&type=Date" width="260" alt="star history balkewkidane/grizl-fabric-observability"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>When the system breaks, the alert finds you first<br>`Infrastructure` | +657 | 93.9 | 67,546 |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>Lots of containers? Leave deploying and scaling to it<br>`Infrastructure` | +402 | 57.4 | 128,919 |
| 3 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Set up a web server with HTTPS configured for you<br>`Infrastructure` | +314 | 44.9 | 78,889 |
| 4 | [grafana/grafana](https://github.com/grafana/grafana)<br>Metrics, logs and traces on one dashboard<br>`Infrastructure` | +194 | 27.7 | 77,758 |
| 5 | [docker/compose](https://github.com/docker/compose)<br>Put many containers in one file and run them together<br>`Infrastructure` | +118 | 16.9 | 38,644 |
| 6 | [traefik/traefik](https://github.com/traefik/traefik)<br>With many services, traffic gets sorted automatically<br>`Infrastructure` | +92 | 13.1 | 65,492 |
| 7 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>Write cloud resources as code you can review and version<br>`Infrastructure` | +89 | 12.7 | 50,165 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>Manage cloud resources in a language you already know<br>`Infrastructure` | +25 | 3.6 | 25,851 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="star history prometheus/prometheus"></a>

<a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="star history kubernetes/kubernetes"></a>

<a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="star history caddyserver/caddy"></a>

<a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="star history grafana/grafana"></a>

<a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="star history docker/compose"></a>

<a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="star history traefik/traefik"></a>

<a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="star history hashicorp/terraform"></a>

<a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="star history pulumi/pulumi"></a>

</details>

### Fastest rising this month (last 30 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Set up a web server with HTTPS configured for you<br>`Infrastructure` | +1,451 | 48.4 | 78,889 |
| 2 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>When the system breaks, the alert finds you first<br>`Infrastructure` | +1,216 | 40.5 | 67,546 |
| 3 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>Lots of containers? Leave deploying and scaling to it<br>`Infrastructure` | +1,114 | 37.1 | 128,919 |
| 4 | [grafana/grafana](https://github.com/grafana/grafana)<br>Metrics, logs and traces on one dashboard<br>`Infrastructure` | +784 | 26.1 | 77,758 |
| 5 | [traefik/traefik](https://github.com/traefik/traefik)<br>With many services, traffic gets sorted automatically<br>`Infrastructure` | +483 | 16.1 | 65,492 |
| 6 | [docker/compose](https://github.com/docker/compose)<br>Put many containers in one file and run them together<br>`Infrastructure` | +433 | 14.4 | 38,644 |
| 7 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>Write cloud resources as code you can review and version<br>`Infrastructure` | +417 | 13.9 | 50,165 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>Manage cloud resources in a language you already know<br>`Infrastructure` | +125 | 4.2 | 25,851 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="star history caddyserver/caddy"></a>

<a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="star history prometheus/prometheus"></a>

<a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="star history kubernetes/kubernetes"></a>

<a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="star history grafana/grafana"></a>

<a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="star history traefik/traefik"></a>

<a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="star history docker/compose"></a>

<a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="star history hashicorp/terraform"></a>

<a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="star history pulumi/pulumi"></a>

</details>

### Fastest rising this year (last 365 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Set up a web server with HTTPS configured for you<br>`Infrastructure` | +12,022 | 32.9 | 78,889 |
| 2 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>Lots of containers? Leave deploying and scaling to it<br>`Infrastructure` | +11,784 | 32.3 | 128,919 |
| 3 | [traefik/traefik](https://github.com/traefik/traefik)<br>With many services, traffic gets sorted automatically<br>`Infrastructure` | +8,666 | 23.7 | 65,492 |
| 4 | [grafana/grafana](https://github.com/grafana/grafana)<br>Metrics, logs and traces on one dashboard<br>`Infrastructure` | +7,908 | 21.7 | 77,758 |
| 5 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>When the system breaks, the alert finds you first<br>`Infrastructure` | +7,039 | 19.3 | 67,546 |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>Write cloud resources as code you can review and version<br>`Infrastructure` | +3,789 | 10.4 | 50,165 |
| 7 | [docker/compose](https://github.com/docker/compose)<br>Put many containers in one file and run them together<br>`Infrastructure` | +2,664 | 7.3 | 38,644 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>Manage cloud resources in a language you already know<br>`Infrastructure` | +2,075 | 5.7 | 25,851 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#caddyserver/caddy&Date"><img src="https://api.star-history.com/svg?repos=caddyserver/caddy&type=Date" width="260" alt="star history caddyserver/caddy"></a>

<a href="https://www.star-history.com/#kubernetes/kubernetes&Date"><img src="https://api.star-history.com/svg?repos=kubernetes/kubernetes&type=Date" width="260" alt="star history kubernetes/kubernetes"></a>

<a href="https://www.star-history.com/#traefik/traefik&Date"><img src="https://api.star-history.com/svg?repos=traefik/traefik&type=Date" width="260" alt="star history traefik/traefik"></a>

<a href="https://www.star-history.com/#grafana/grafana&Date"><img src="https://api.star-history.com/svg?repos=grafana/grafana&type=Date" width="260" alt="star history grafana/grafana"></a>

<a href="https://www.star-history.com/#prometheus/prometheus&Date"><img src="https://api.star-history.com/svg?repos=prometheus/prometheus&type=Date" width="260" alt="star history prometheus/prometheus"></a>

<a href="https://www.star-history.com/#hashicorp/terraform&Date"><img src="https://api.star-history.com/svg?repos=hashicorp/terraform&type=Date" width="260" alt="star history hashicorp/terraform"></a>

<a href="https://www.star-history.com/#docker/compose&Date"><img src="https://api.star-history.com/svg?repos=docker/compose&type=Date" width="260" alt="star history docker/compose"></a>

<a href="https://www.star-history.com/#pulumi/pulumi&Date"><img src="https://api.star-history.com/svg?repos=pulumi/pulumi&type=Date" width="260" alt="star history pulumi/pulumi"></a>

</details>

### Total stars (all time)

| # | Project | Total stars |
|---|---|---:|
| 1 | [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes)<br>Lots of containers? Leave deploying and scaling to it<br>`Infrastructure` | 128,919 |
| 2 | [caddyserver/caddy](https://github.com/caddyserver/caddy)<br>Set up a web server with HTTPS configured for you<br>`Infrastructure` | 78,889 |
| 3 | [grafana/grafana](https://github.com/grafana/grafana)<br>Metrics, logs and traces on one dashboard<br>`Infrastructure` | 77,758 |
| 4 | [prometheus/prometheus](https://github.com/prometheus/prometheus)<br>When the system breaks, the alert finds you first<br>`Infrastructure` | 67,546 |
| 5 | [traefik/traefik](https://github.com/traefik/traefik)<br>With many services, traffic gets sorted automatically<br>`Infrastructure` | 65,492 |
| 6 | [hashicorp/terraform](https://github.com/hashicorp/terraform)<br>Write cloud resources as code you can review and version<br>`Infrastructure` | 50,165 |
| 7 | [docker/compose](https://github.com/docker/compose)<br>Put many containers in one file and run them together<br>`Infrastructure` | 38,644 |
| 8 | [pulumi/pulumi](https://github.com/pulumi/pulumi)<br>Manage cloud resources in a language you already know<br>`Infrastructure` | 25,851 |

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
| 1 | [kubai087/kubai-icons](https://github.com/kubai087/kubai-icons)<br>Icons look mismatched, let a Claude skill draw one style | 2026-11-03<br><sub>5.2 d</sub> | 273 | 52.8 |
| 2 | [DominikScholz/open-bot-avatar](https://github.com/DominikScholz/open-bot-avatar)<br>Render interactive avatars for your agents | 2026-11-02<br><sub>5.9 d</sub> | 301 | 51.3 |
| 3 | [leodavincs/kalem](https://github.com/leodavincs/kalem)<br>Choose a fitting engine for each video scene | 2026-11-01<br><sub>7.0 d</sub> | 108 | 15.5 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#kubai087/kubai-icons&Date"><img src="https://api.star-history.com/svg?repos=kubai087/kubai-icons&type=Date" width="260" alt="star history kubai087/kubai-icons"></a>

<a href="https://www.star-history.com/#DominikScholz/open-bot-avatar&Date"><img src="https://api.star-history.com/svg?repos=DominikScholz/open-bot-avatar&type=Date" width="260" alt="star history DominikScholz/open-bot-avatar"></a>

<a href="https://www.star-history.com/#leodavincs/kalem&Date"><img src="https://api.star-history.com/svg?repos=leodavincs/kalem&type=Date" width="260" alt="star history leodavincs/kalem"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>Open it and draw, like sketching on paper<br>`Design / Creative` | +454 | 64.9 | 135,323 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>Design together as a team, on an open-source platform<br>`Design / Creative` | +275 | 39.3 | 62,180 |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>One icon set in one style, ready to use<br>`Design / Creative` | +213 | 30.4 | 25,635 |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>Diagrams and a whiteboard in one editor<br>`Design / Creative` | +144 | 20.6 | 9,248 |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Pick ready-made components for Tailwind CSS<br>`Design / Creative` | +73 | 10.4 | 42,764 |
| 6 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>Drop After Effects animations straight into web pages<br>`Design / Creative` | +68 | 9.7 | 32,377 |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>A flexible icon family for everyone<br>`Design / Creative` | +36 | 5.1 | 7,778 |
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
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>Open it and draw, like sketching on paper<br>`Design / Creative` | +2,014 | 67.1 | 135,323 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>Design together as a team, on an open-source platform<br>`Design / Creative` | +1,501 | 50.0 | 62,180 |
| 3 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>One icon set in one style, ready to use<br>`Design / Creative` | +778 | 25.9 | 25,635 |
| 4 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>Diagrams and a whiteboard in one editor<br>`Design / Creative` | +634 | 21.1 | 9,248 |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Pick ready-made components for Tailwind CSS<br>`Design / Creative` | +292 | 9.7 | 42,764 |
| 6 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>Drop After Effects animations straight into web pages<br>`Design / Creative` | +257 | 8.6 | 32,377 |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>A flexible icon family for everyone<br>`Design / Creative` | +167 | 5.6 | 7,778 |
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
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>Open it and draw, like sketching on paper<br>`Design / Creative` | +27,025 | 74.0 | 135,323 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>Design together as a team, on an open-source platform<br>`Design / Creative` | +21,830 | 59.8 | 62,180 |
| 3 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>Diagrams and a whiteboard in one editor<br>`Design / Creative` | +6,563 | 18.0 | 9,248 |
| 4 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>One icon set in one style, ready to use<br>`Design / Creative` | +6,337 | 17.4 | 25,635 |
| 5 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Pick ready-made components for Tailwind CSS<br>`Design / Creative` | +4,225 | 11.6 | 42,764 |
| 6 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>A flexible icon family for everyone<br>`Design / Creative` | +2,200 | 6.0 | 7,778 |
| 7 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>Drop After Effects animations straight into web pages<br>`Design / Creative` | +1,126 | 3.1 | 32,377 |
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
| 1 | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)<br>Open it and draw, like sketching on paper<br>`Design / Creative` | 135,323 |
| 2 | [penpot/penpot](https://github.com/penpot/penpot)<br>Design together as a team, on an open-source platform<br>`Design / Creative` | 62,180 |
| 3 | [saadeghi/daisyui](https://github.com/saadeghi/daisyui)<br>Pick ready-made components for Tailwind CSS<br>`Design / Creative` | 42,764 |
| 4 | [airbnb/lottie-web](https://github.com/airbnb/lottie-web)<br>Drop After Effects animations straight into web pages<br>`Design / Creative` | 32,377 |
| 5 | [lucide-icons/lucide](https://github.com/lucide-icons/lucide)<br>One icon set in one style, ready to use<br>`Design / Creative` | 25,635 |
| 6 | [jgraph/drawio](https://github.com/jgraph/drawio)<br>Diagrams and a whiteboard in one editor<br>`Design / Creative` | 9,248 |
| 7 | [phosphor-icons/homepage](https://github.com/phosphor-icons/homepage)<br>A flexible icon family for everyone<br>`Design / Creative` | 7,778 |
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
| 1 | [ArteVisualenVivo/fabric-pipeline-express-7](https://github.com/ArteVisualenVivo/fabric-pipeline-express-7)<br>OneLake pipeline with automated Upsert merge and Python | 2026-11-06<br><sub>2.0 d</sub> | 149 | 75.0 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#ArteVisualenVivo/fabric-pipeline-express-7&Date"><img src="https://api.star-history.com/svg?repos=ArteVisualenVivo/fabric-pipeline-express-7&type=Date" width="260" alt="star history ArteVisualenVivo/fabric-pipeline-express-7"></a>

</details>

### Fastest rising this week (last 7 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>Run SQL analysis without setting up a database server<br>`Data` | +220 | 31.4 | 42,914 |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>Real-time analysis of huge data, with open source<br>`Data` | +132 | 18.9 | 50,819 |
| 3 | [apache/kafka](https://github.com/apache/kafka)<br>Stream events between systems on one distributed platform<br>`Data` | +99 | 14.1 | 34,194 |
| 4 | [apache/superset](https://github.com/apache/superset)<br>Can't make sense of the data? Turn it into charts<br>`Data` | +97 | 13.9 | 75,450 |
| 5 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>Table data handled fast, no more waiting<br>`Data` | +58 | 8.3 | 40,285 |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>Transform data the way software engineers build apps<br>`Data` | +34 | 4.9 | 14,133 |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>Across languages, the data works as it is<br>`Data` | +19 | 2.7 | 17,278 |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>Write code in the browser and see results as you go<br>`Data` | +6 | 0.9 | 13,461 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="star history duckdb/duckdb"></a>

<a href="https://www.star-history.com/#ClickHouse/ClickHouse&Date"><img src="https://api.star-history.com/svg?repos=ClickHouse/ClickHouse&type=Date" width="260" alt="star history ClickHouse/ClickHouse"></a>

<a href="https://www.star-history.com/#apache/kafka&Date"><img src="https://api.star-history.com/svg?repos=apache/kafka&type=Date" width="260" alt="star history apache/kafka"></a>

<a href="https://www.star-history.com/#apache/superset&Date"><img src="https://api.star-history.com/svg?repos=apache/superset&type=Date" width="260" alt="star history apache/superset"></a>

<a href="https://www.star-history.com/#pola-rs/polars&Date"><img src="https://api.star-history.com/svg?repos=pola-rs/polars&type=Date" width="260" alt="star history pola-rs/polars"></a>

<a href="https://www.star-history.com/#dbt-labs/dbt-core&Date"><img src="https://api.star-history.com/svg?repos=dbt-labs/dbt-core&type=Date" width="260" alt="star history dbt-labs/dbt-core"></a>

<a href="https://www.star-history.com/#apache/arrow&Date"><img src="https://api.star-history.com/svg?repos=apache/arrow&type=Date" width="260" alt="star history apache/arrow"></a>

<a href="https://www.star-history.com/#jupyter/notebook&Date"><img src="https://api.star-history.com/svg?repos=jupyter/notebook&type=Date" width="260" alt="star history jupyter/notebook"></a>

</details>

### Fastest rising this month (last 30 days)

| # | Project | Stars gained | Stars/day | Total stars |
|---|---|---:|---:|---:|
| 1 | [duckdb/duckdb](https://github.com/duckdb/duckdb)<br>Run SQL analysis without setting up a database server<br>`Data` | +987 | 32.9 | 42,914 |
| 2 | [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)<br>Real-time analysis of huge data, with open source<br>`Data` | +594 | 19.8 | 50,819 |
| 3 | [apache/superset](https://github.com/apache/superset)<br>Can't make sense of the data? Turn it into charts<br>`Data` | +467 | 15.6 | 75,450 |
| 4 | [apache/kafka](https://github.com/apache/kafka)<br>Stream events between systems on one distributed platform<br>`Data` | +343 | 11.4 | 34,194 |
| 5 | [pola-rs/polars](https://github.com/pola-rs/polars)<br>Table data handled fast, no more waiting<br>`Data` | +311 | 10.4 | 40,285 |
| 6 | [dbt-labs/dbt-core](https://github.com/dbt-labs/dbt-core)<br>Transform data the way software engineers build apps<br>`Data` | +172 | 5.7 | 14,133 |
| 7 | [apache/arrow](https://github.com/apache/arrow)<br>Across languages, the data works as it is<br>`Data` | +113 | 3.8 | 17,278 |
| 8 | [jupyter/notebook](https://github.com/jupyter/notebook)<br>Write code in the browser and see results as you go<br>`Data` | +61 | 2.0 | 13,461 |

<details>
<summary>Star history charts for this board</summary>

<a href="https://www.star-history.com/#duckdb/duckdb&Date"><img src="https://api.star-history.com/svg?repos=duckdb/duckdb&type=Date" width="260" alt="star history duckdb/duckdb"></a>

<a href="https://www.star-hist