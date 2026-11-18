<!--
DataForSEO Agent is a free, open source terminal app for the DataForSEO API. Ask SEO questions in plain words:
it picks the cheapest correct DataForSEO v3 endpoint, shows the price before it spends anything, and draws the
results as charts, tables and maps in your terminal. SERP API, keyword research, Google rankings, local SEO
geogrid, backlinks, on-page audits, AI visibility (AI Optimization API), app data and merchant data. Works with
Claude, ChatGPT, Gemini and 75+ AI model providers.
-->

<p align="center">
  <img src="docs/screenshots/home.png" width="1100" alt="DataForSEO Agent home screen in the terminal: chat sidebar on the left, the prompt with four starter questions, and the three Homies walking past a keyword ideas station" />
</p>

<h1 align="center">DataForSEO Agent</h1>

<p align="center">
  <b>Ask SEO questions in plain words. Get DataForSEO data as charts, tables and maps in your terminal.</b><br />
  It picks the cheapest correct API call and shows you the price before it spends a cent.
</p>

<p align="center">
  <a href="#see-it-running">Screenshots</a> · <a href="#install">Install</a> · <a href="#how-it-keeps-your-money-safe">Cost guard</a> · <a href="#charts-and-maps">Charts</a> · <a href="#the-12-apis-and-the-team">APIs and team</a> · <a href="#commands">Commands</a> · <a href="#faq">FAQ</a> · <a href="#privacy-and-network">Privacy</a>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT" /></a>
  <img src="https://img.shields.io/badge/DataForSEO%20API-v3-2862A8" alt="DataForSEO API v3" />
  <img src="https://img.shields.io/badge/endpoints-576%20live--tested-137A74" alt="576 endpoints, live-tested" />
  <img src="https://img.shields.io/badge/models-Claude%20%C2%B7%20ChatGPT%20%C2%B7%20Gemini%20%C2%B7%2075%2B-EABD59" alt="Claude, ChatGPT, Gemini and 75+ providers" />
</p>

**DataForSEO Agent turns an SEO question into the right DataForSEO API calls, asks before it spends, and shows the answer as a chart you can sort, hover and save.**

- **Plain-language SEO research:** "Who ranks for best crm in the US?", "Backlink gap between my site and a competitor", "Where does my plumbing business rank across the city?"
- **Price first, every time:** the agent estimates the cost from the catalog and ends with "Run it for $X?". Then the app itself asks again, showing the list price, before any paid request.
- **A hard session budget:** $1 by default. Once a session has spent it, no more DataForSEO requests go out.
- **Charts, not raw JSON:** 16 chart types in the terminal, including a local SEO geogrid on map tiles and a US state map, plus a one-file HTML report.
- **All of DataForSEO:** 576 active v3 endpoints across 12 APIs, every one live-tested, with a specialist agent per API.
- **Any AI model:** Claude, ChatGPT, Gemini, OpenRouter and 75+ other providers.

## See it running

<p align="center">
  <a href="https://www.youtube.com/watch?v=FtuQkcnrw2w"><img src="docs/screenshots/video.jpg" width="720" alt="Watch the DataForSEO Agent demo on YouTube: keyword research, Google Maps and a geogrid, an AI Overview check and competitor research, with the price of each run" /></a><br />
  <b><a href="https://www.youtube.com/watch?v=FtuQkcnrw2w">Watch the full demo on YouTube</a></b> (28 min): keyword research, Google Maps with a geogrid, an AI Overview check and competitor research.
</p>

Real screenshots from one sitting, about 10 cents of DataForSEO credit in total.

**It asks before it spends.** The plan, the estimate, then a prompt with the list price and the exact endpoint. Nothing is sent until you accept.

<p align="center">
  <img src="docs/screenshots/approval.png" width="1100" alt="Approval prompt for a paid DataForSEO call: from $0.012, POST dataforseo_labs google keyword_ideas live, with Accept, Allow all in chat, Always this endpoint and Deny" />
</p>

**Keyword ideas** (Labs API, $0.024). "Find keyword ideas for crm software in the United States with search volume and difficulty." The answer stays in the chat and the table stays in the results pane on the right.

<p align="center">
  <img src="docs/screenshots/keywords.png" width="1100" alt="Keyword ideas for crm software in the US: the agent's notes in the chat and a sortable table of keywords with search volume, difficulty and CPC in the results pane" />
</p>

<table>
  <tr>
    <td width="50%"><img src="docs/screenshots/serp.png" alt="Top 10 Google results for best crm software in the US, as a table of rank, domain, type and title, with the agent's findings" /></td>
    <td width="50%"><img src="docs/screenshots/trend.png" alt="Line chart of monthly US search volume for crm software, project management software and email marketing software over 12 months" /></td>
  </tr>
  <tr>
    <td><b>Google rankings</b> (SERP API, $0.002). "Top 10 Google results for best crm software in the US."</td>
    <td><b>Search volume over time</b> (Keywords Data API, $0.06). Three keywords compared across 12 months.</td>
  </tr>
  <tr>
    <td><img src="docs/screenshots/maps.png" alt="Google Maps results for coffee shop in Austin, Texas: a scatter chart of rating against review count for 20 places, with the agent's notes" /></td>
    <td><img src="docs/screenshots/intent.png" alt="Search intent mix of 100 keyword ideas as a share bar: 44 percent commercial, 40 informational, 12 navigational, 4 transactional" /></td>
  </tr>
  <tr>
    <td><b>Local results</b> (Google Maps, $0.002). "Who shows up on Google Maps for coffee shop in Austin, Texas?"</td>
    <td><b>Search intent mix</b>, drawn from the same keyword ideas call at no extra cost.</td>
  </tr>
</table>

## Install

<p align="center">
  <img src="docs/readme/install.svg" width="1200" height="420" alt="Install DataForSEO Agent in three commands: tools/install.sh, dataforseo-agent-setup to connect your DataForSEO API account, set a session budget and market and pick any AI model, then dataforseo to start. Press start: the three bots boot up while the counters fill to 14 SEO agents and 33 SEO workflow skills." />
</p>

You need [Bun](https://bun.sh), Python 3, Node 22 or newer (for the DataForSEO MCP server) and a [DataForSEO](https://dataforseo.com) account.

```bash
git clone https://github.com/AgriciDaniel/dataforseo-agent.git
cd dataforseo-agent
tools/install.sh          # builds the app and installs dataforseo-agent and dataforseo to ~/.local/bin
dataforseo-agent-setup    # account, budget and market, AI model
dataforseo                # start
```

Your first run:

```text
> What's my DataForSEO balance?                 (free, no prompt)
> Top 10 Google results for "best crm" in the US
  ...route, plan and cost...
  Run it for $0.002?                            (say yes, then approve the request)
```

<details>
<summary><b>What setup asks</b></summary>

1. **Account.** Type your API login and password (the password is hidden), or point to an env file you already keep. Typed credentials go only into `~/.config/dataforseo-agent/credentials.env`, readable only by you. From an env file, only the `DATAFORSEO_*` lines are read. Your password never goes through a model.
2. **Budget and market.** The session budget, and your default location, language and mode.
3. **Model.** Sign in to Claude or ChatGPT, or add an API key later with `/connect`.

Credentials already in your environment (`DATAFORSEO_LOGIN` or `DATAFORSEO_USERNAME`, and `DATAFORSEO_PASSWORD`) always win over the saved file.

Choosing a model:

- Claude, through your Claude Code login: `dataforseo-agent auth login claude-agent`
- ChatGPT, through your ChatGPT account: `dataforseo-agent auth login openai` (add `--method chatgpt-token-sharing` when the terminal is not interactive)
- Gemini, OpenRouter and the rest: an API key, with `/connect` in the app. Then pick a model with `/models`, or start with `dataforseo -m provider/model`.

</details>

## How it keeps your money safe

<p align="center">
  <img src="docs/readme/cost.svg" width="1200" height="420" alt="DataForSEO Agent cost guard: each DataForSEO API call stops at a gate with its price. The free /dfs-balance call passes with no prompt, paid SEO calls for rank checks and keyword research wait for YES and fill a $1.00 session budget meter, and the call that would cross the budget is blocked with Session budget reached." />
</p>

Every paid DataForSEO call stops at a prompt that shows the method, path, body, number of tasks and the catalog list price, and waits for your yes. "Always allow" covers that one endpoint only. Free calls run without asking: the sandbox, your balance, task results, location and language lists, and docs lookups. Raw calls to `api.dataforseo.com` from the shell or a web fetch ask too.

Session spend is written to disk, so restarting the app does not refill the budget. Each paid call reserves its estimated cost before it is sent, so chats and child agents running at the same time cannot overshoot together. A call that was sent but whose result was lost in a crash is never sent again on its own: the agent is told it may already have been billed.

The session budget is enforced by the app itself, not just by the agent's instructions. It adds up the billed cost of each call in the session and its sub-agents (or the catalog price when a response leaves the cost out). As a backstop it also watches your account balance, so anything else billed while the session is open counts too. Free calls, such as fetching a result you already paid for, are never blocked. The sidebar shows your balance, today's spend against the daily limit, and this session's spend against the budget.

**Known limit:** the agent also has a shell tool. It refuses any command that names `api.dataforseo.com`, so a paid call cannot skip the price prompt that way, but the check reads the command text. A script that builds the address in pieces would get past it. The balance backstop still counts that spend against the session budget.

<details>
<summary><b>Settings</b></summary>

`~/.config/dataforseo-agent/settings.json`, changed with `/dfs-settings` or `dataforseo-agent-setup`:

| Setting | Default | What it does |
|---|---|---|
| `budget_per_session_usd` | `1` | Hard stop. Once a session (with its sub-agents) has spent this much, the app sends no more DataForSEO requests. |
| `ask_above_usd` | `0` | The agent skips its "Run it for $X?" question for estimates at or below this. `0` means it always asks. The app's own request prompt still appears. |
| `default_location_code` | `2840` (United States) | Used when you don't name a market. |
| `default_language_code` | `en` | Same, for language. |
| `prefer_mode` | `cheapest` | `cheapest`, `standard` or `live`. |

</details>

## Charts and maps

<p align="center">
  <img src="docs/readme/maps.svg" width="1200" height="420" alt="DataForSEO Agent charts in the terminal: a local SEO geogrid of 25 rank tiles lights up on map tiles around a pinned business, green for ranks 1 to 3, teal for 4 to 10, gold for 11 to 20, with Top 3: 9 of 25. The view flips to a US tile map of keyword search volume by state and a 12 month trend sparkline. 16 chart types in total." />
</p>

Numeric results come back as one of 16 chart types: table, kpi, hbar, grouped-bar, share-bar, diverging-bar, line, sparkline, scatter, heatmap, distribution (rank buckets per domain), overlap (shared keywords), gauge, donut, geogrid (a local rank grid drawn on map tiles, with your business pinned) and tilemap (a map of US states). Each chart names the endpoint and the billed cost under it, and each workflow draws the same default charts every time.

- Click a column header to sort. Point at a bar, marker or tile to see its exact value.
- Under each chart: `table` switches between chart and table, `copy` and `save` export the data as CSV, `report` writes one HTML file with every chart in the session (light and dark mode), and `expand` opens the chart full screen.
- On a wide terminal (about 150 columns), charts stay in a results pane on the right while the chat scrolls, with previous and next. `/results` shows or hides it.

## Several chats at once

Each chat in the sidebar carries a marker for its state: waiting for your approval, asked you a question, failed, working, or finished since you last looked. A line above the list says how many need you and jumps to the first one. `/activity` lists every chat and child agent by state, with search.

You can close the terminal while work is running. With the background service, chats keep going and a pending approval stays pending; starting `dataforseo` again reopens the last chat, shows the approval or question again and reconnects open terminals. `/detach` does the same on purpose and tells you how many chats are still running. Started with `--standalone`, the app stops its work when it closes, and says so.

Notifications and sounds for approvals, questions and finished chats are off by default; turn them on under Notifications in the command palette.

The chat sidebar on the left lists your chats and shows the account: balance, today's spend, and this session's spend against its budget. The balance and session spend also sit in the prompt footer, so they stay in view with the sidebar folded. The home screen has starter prompts for common jobs; clicking one fills the prompt and waits for you to send it.

## The 12 APIs and the team

<p align="center">
  <img src="docs/readme/apis.svg" width="1200" height="420" alt="The 12 DataForSEO APIs as a pixel city: the three bots visit SERP, Keywords Data, Labs, Backlinks, OnPage, Domain Analytics, Content Analysis, Business Data, Merchant, App Data, AI Optimization for AI visibility, and Databases, while the counter reaches 576 DataForSEO API endpoints, every one live-tested, with one specialist agent per API." />
</p>

The main agent, `dataforseo`, routes every job. `@cost-guard` estimates cost, checks your balance and budget, and blocks unapproved spend. Twelve specialists, one per API, know their endpoints, parameters, limits and prices.

<details>
<summary><b>The specialists</b></summary>

| Agent | DataForSEO API | Good for |
|---|---|---|
| `@serp` | SERP API | Google, Bing and other search results, rank checks, SERP features |
| `@keywords-data` | Keywords Data API | Search volume, CPC, Google Trends |
| `@labs` | DataForSEO Labs | Keyword research, competitors, ranked keywords, traffic estimates |
| `@backlinks` | Backlinks API | Backlink profiles, referring domains, link gaps |
| `@onpage` | OnPage API | Site crawls, technical SEO checks, page audits |
| `@domain-analytics` | Domain Analytics API | Technologies, Whois |
| `@content-analysis` | Content Analysis API | Brand mentions, sentiment |
| `@business-data` | Business Data API | Google Business profiles, reviews, local SEO |
| `@merchant` | Merchant API | Google Shopping and Amazon products and sellers |
| `@app-data` | App Data API | Google Play and App Store apps and reviews |
| `@ai-optimization` | AI Optimization API | AI visibility: what ChatGPT, Gemini, Perplexity and AI Overviews say about a brand |
| `@databases` | Databases | Advice on bulk datasets (no API calls) |

Behind them sits the DataForSEO Brain: source-cited notes and 33 workflow skills, from a backlink gap check to a local rank geogrid. Who it's for: SEO consultants who want answers without writing API code, agencies watching API spend across clients, and developers learning which endpoint fits a job.

</details>

## Commands

| Command | What it does |
|---|---|
| `dataforseo` or `dataforseo-agent` | Start the app. `dataforseo -m provider/model` starts with a given model. |
| `dataforseo-agent-setup` | Connect the account, set budget and market, sign in to a model. |
| `dataforseo-agent --check-account` | Check the login, balance and today's spend (free). |
| `dataforseo-agent-update` | Pull the latest version, rebuild and reinstall. |
| `dataforseo-agent service status` | What is alive in the background: running turns, pending approvals and questions, open terminals, uptime. |

Inside the app:

| Command | What it does |
|---|---|
| `/dfs-route` | Which endpoint fits this job, and what it will cost. |
| `/dfs-cost` | Estimate the cost of a plan before running it. |
| `/dfs-balance` | Account balance and limits (free). |
| `/dfs-endpoint` | One endpoint explained: parameters, modes, limits, price, an example request. |
| `/dfs-news` | What changed at DataForSEO lately (free). |
| `/dfs-settings` | Show or change the budget, default market and mode. |
| `/results` | Show or hide the results pane with the session's charts. |
| `/activity` | Every chat and child agent by state: waiting for approval, asked a question, failed, working, finished. Enter jumps to it. |
| `/detach` | Leave the app while chats keep running. Start `dataforseo` again to come back. |

## FAQ

<details>
<summary><b>Is DataForSEO Agent free?</b></summary>

The app is free and open source (MIT). DataForSEO itself is pay as you go: you pay DataForSEO for the API calls you approve, and the app shows each price before you approve it. Your AI model works through your own Claude or ChatGPT login, or your own API key.

</details>

<details>
<summary><b>How much does a typical question cost?</b></summary>

Most single lookups cost a fraction of a cent to a few cents: a top 10 Google check is about $0.002, a backlink summary about $0.02. Bigger jobs, such as a site crawl or a city-wide geogrid, cost more, and the agent shows the arithmetic before it asks. The session budget caps any one session ($1 by default).

</details>

<details>
<summary><b>Can it spend money without asking me?</b></summary>

No. Every paid request stops at a permission prompt with its price, and the session budget is a hard stop in the app itself. Only calls the catalog marks free, such as your balance or a task result you already paid for, run without asking.

</details>

<details>
<summary><b>Which AI models does it work with?</b></summary>

Any of them: Claude through your Claude Code login, ChatGPT through your ChatGPT account, and Gemini, OpenRouter and 75+ other providers with an API key. Your DataForSEO password never goes through the model.

</details>

<details>
<summary><b>Does it do local SEO?</b></summary>

Yes. The geogrid chart shows where a business ranks across a grid of points around its location, drawn on map tiles with the business pinned. It uses the DataForSEO SERP and Business Data APIs.

</details>

<details>
<summary><b>How do I know the endpoint and price data are current?</b></summary>

The catalog is built from DataForSEO's official OpenAPI spec and pricing pages, and every one of the 576 active endpoints was called live to confirm it works. `/dfs-news` shows recent DataForSEO changes. If a Brain note and the catalog disagree, the catalog wins.

</details>

<details>
<summary><b>Good to know</b></summary>

- **Platforms:** Linux and macOS (built with Bun). Windows is untested.
- **Where things live:** the app and its generated agents, skills and MCP config live in `~/.config/dataforseo-agent/` (rewritten on every install). Your own config is `~/.config/dataforseo-agent/dataforseo-agent.jsonc`, created once and never touched again. Sessions and logs are in `~/.local/share/dataforseo-agent/`.
- **Refreshing the Brain and catalog:** rebuild the catalog with `research/scripts/README.md`, update the Brain following `Brain/docs/OPERATOR_KIT.md`, check it with `Brain/tools/check.sh`, then run `tools/install.sh` again.
- **Uninstall:** delete `~/.local/bin/dataforseo-agent`, `~/.local/bin/dataforseo`, `~/.local/bin/dataforseo-agent-setup`, `~/.local/bin/dataforseo-agent-update`, `~/.local/lib/dataforseo-agent` and `~/.config/dataforseo-agent`.

</details>

## Privacy and network

In normal use the app talks to these servers:

- **DataForSEO**, with your API login, for the calls you approve and for the free account and catalog checks.
- **Your AI model provider**, with your chat, as with any AI tool. Which one is your choice at setup.
- **models.dev**, to refresh the public list of models and prices. Nothing about you or your chats is sent.
- **The npm registry**, to download the official DataForSEO MCP server (`dataforseo-mcp-server`) that makes the API calls.
- **GitHub**, to download syntax highlighting files the first time a code block in a given language is shown.

It reaches other servers only when the work calls for it: a web page the agent fetches, a web search provider if the agent searches the web, and any plugin or extra MCP server you add yourself.

There is no telemetry and no automatic update. Usage data is exported only if you set the standard `OTEL_EXPORTER_OTLP_ENDPOINT` variable yourself. Your DataForSEO password is stored in `~/.config/dataforseo-agent/credentials.env`, readable only by you, and never goes through a model.

## License

MIT, see [LICENSE](LICENSE).

The engine is a fork of [opencode](https://github.com/sst/opencode), an open source terminal agent, also MIT licensed. Thank you to its authors.

DataForSEO is a trademark of its owner. This is an independent project that uses the public DataForSEO API.

Built by **[Agrici Daniel](https://agricidaniel.com/about)**, AI Workflow Architect, with help from the [AI Marketing Hub Pro](https://www.skool.com/ai-marketing-hub-pro) community. The three bots are from my GitHub profile.

<p align="center">
  <img src="docs/readme/footer.svg" width="1200" height="420" alt="Thanks for playing: a CONTINUE? countdown runs, a price tag says starring the DataForSEO Agent repo is free with no prompt, the three bots hop and a pixel star fills gold. Recap: 576 DataForSEO API endpoints, 12 APIs, 14 agents, 33 SEO skills, 16 chart types, 75+ AI model providers. Continue? Star the repo." />
</p>

<p align="center">
  <a href="https://www.youtube.com/@AgriciDaniel"><img src="docs/readme/btn-youtube.svg" width="137" height="44" alt="Tutorials and demos on YouTube" /></a>
  <a href="https://www.skool.com/ai-marketing-hub"><img src="docs/readme/btn-hub.svg" width="210" height="44" alt="AI Marketing Hub, the free community on Skool" /></a>
  <a href="https://www.skool.com/ai-marketing-hub-pro"><img src="docs/readme/btn-pro.svg" width="155" height="44" alt="AI Marketing Hub Pro" /></a>
</p>
