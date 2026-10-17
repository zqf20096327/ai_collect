<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/llmquant-x-hermes-dark.svg" />
  <img src="docs/images/llmquant-x-hermes.svg" alt="LLMQuant × Hermes Agent" width="280" />
</picture>

<h1>llmquant-hermes</h1>

<p><strong>English</strong> | <a href="README.zh-CN.md">简体中文</a></p>

<p><strong>Turn your Hermes agent into a financial analyst.</strong><br/>
Ask it anything from equities to prediction markets — and let it keep watch: morning briefs, earnings pings, 13F diffs, delivered while you sleep. Powered by LLMQuant Data.</p>

<p>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-lightgrey.svg" alt="License: MIT" /></a>
  <a href="https://github.com/LLMQuant/data-mcp"><img src="https://img.shields.io/badge/data-LLMQuant%20Data%20MCP-0B5FFF" alt="LLMQuant Data MCP" /></a>
  <a href="https://github.com/LLMQuant/skills"><img src="https://img.shields.io/badge/companion-LLMQuant%2Fskills-8A5A44" alt="Companion repo: LLMQuant/skills" /></a>
  <a href="https://github.com/NousResearch/hermes-agent"><img src="https://img.shields.io/badge/built%20for-Hermes%20Agent-6E56CF" alt="Built for Hermes Agent" /></a>
</p>

</div>

## What you get

One paste gives your Hermes agent an analyst's full stack — market data, analysis method, and five standing watchers it runs for you:

- **Morning brief** — a pre-open rundown of macro, your watchlist's overnight moves, fresh company news, earnings-adjacent filings — and overnight prediction-market odds moves, cross-checked against the news — waiting when you wake up.
- **Earnings watch** — a nudge when a name on your list reports or updates guidance, so you never miss a print.
- **13F diff** — what the big managers you track bought, sold, or trimmed in their latest 13F, with news context on the changed names.
- **Portfolio pulse** — a weekly check-up on your saved holdings: trend, macro, and news that touches what you own.
- **Polymarket watch** — a short morning list of prediction markets worth a look: the biggest overnight odds moves, fresh high-volume markets, and where the odds disagree with the news.

Alongside them come the 18 [`LLMQuant/skills`](https://github.com/LLMQuant/skills) analysis skills (`/llmquant-equities`, `/llmquant-macro`, …) for on-demand deep dives — five standing watchers plus a full analysis toolkit. Type `/llmquant` in Hermes and all of it shows up:

![The /llmquant slash-command picker listing the analysis skills](docs/images/slash-commands.png)

## Contents

- [What you get](#what-you-get)
- [Setup](#setup)
- [Use it](#use-it)
- [What it looks like](#what-it-looks-like)
- [FAQ](#faq)
- [Reference](#reference)
- [Contributing](#contributing)
- [License](#license)

## Setup

You need a running Hermes agent, a messaging channel (Telegram, Discord, Slack, …), and a model backend. These playbooks are tuned for a cost-conscious **DeepSeek** baseline.

### If you don't have Hermes yet

Hermes Agent is a separate project from Nous Research. Install it first:

- **Linux / macOS / WSL2:** `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`
- **Windows (PowerShell):** `iex (irm https://hermes-agent.nousresearch.com/install.ps1)`
- **Desktop GUI (Electron, macOS / Windows):** run `hermes desktop` after the CLI install, or grab the installer from the official site.

Then run `hermes model` to pick a provider and `hermes` to start the terminal TUI. Full docs: [getting started](https://hermes-agent.nousresearch.com/docs/getting-started/installation) · [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent). From here on this README assumes Hermes is running.

### If you already have Hermes

Paste this into your agent — it is the whole setup:

```text
Read https://raw.githubusercontent.com/LLMQuant/llmquant-hermes/master/SETUP.md and set up LLMQuant Data for me. Use DeepSeek as the baseline model. Only ask me for things you can't do yourself.
```

Your Hermes agent will:

- connect the hosted LLMQuant Data MCP URL first, with local stdio as the fallback;
- confirm your Hermes model, with DeepSeek as the recommended baseline;
- install the five market playbooks, the analyst persona, and the [`LLMQuant/skills`](https://github.com/LLMQuant/skills) analysis skills;
- smoke-test the connection with a 0-credit call;
- get you to a first answer right away — a question to try or a manual `morning-brief` run (scheduling is optional, later);
- ask before it edits config, writes cron jobs, or needs an API key.

If the raw URL is unreachable, point the agent at the local [`SETUP.md`](SETUP.md) — the same runbook.

<details>
<summary><strong>Prefer to wire it up by hand?</strong></summary>

1. Sign up at [llmquantdata.com](https://llmquantdata.com) (Free Beta is enough to start), then copy a hosted Remote MCP URL from **Dashboard -> Connect**.
2. Add one entry to `~/.hermes/config.yaml`, then reload MCP (or restart Hermes):

   ```yaml
   mcp_servers:
     llmquant-data:
       url: "https://mcp.llmquantdata.com/u/<token>/mcp"
   ```

3. Call `personal_profile` once — a 0-credit auth smoke test.
4. Install the skills:

   ```bash
   hermes skills tap add LLMQuant/llmquant-hermes
   hermes skills tap add LLMQuant/skills
   hermes skills list
   ```

   Tap may register a source without installing it (see the [FAQ](#faq)). If skills are missing from the list, install them with your Hermes version's skill flow, or clone each repo and copy its `skills/` into `~/.hermes/skills/`.
5. Copy [`templates/SOUL.md`](templates/SOUL.md) to `~/.hermes/SOUL.md`, and [`templates/AGENTS.md`](templates/AGENTS.md) into the workspace that will run the market jobs (edit the watchlist and delivery settings).
6. See it work now: ask Hermes a question or run one playbook manually. Scheduling is optional — see [Use it](#use-it).

Local stdio still works — use [`config/mcp-stdio.example.yaml`](config/mcp-stdio.example.yaml) and edit the YAML by hand (see the [FAQ](#faq) on the `hermes mcp add --env` bug).

</details>

## Use it

You don't need cron to get value. Once setup finishes, just talk to Hermes.

**Ask in plain language** — Hermes picks the right LLMQuant Data tools:

- How do you see NVIDIA's price action these past few days?
- What changed in Berkshire's latest 13F?
- Any notable news on my watchlist today?
- Which prediction markets moved overnight — and does the news back the move?

**Run a playbook with a slash command.** Every installed skill is a `/skill-name` you can follow with a task:

- [`/morning-brief`](skills/morning-brief/SKILL.md) — the full pre-open brief, on demand.
- [`/earnings-watch`](skills/earnings-watch/SKILL.md) — scan your watchlist for earnings and guidance.
- [`/13f-diff`](skills/13f-diff/SKILL.md) `compare my tracked managers to the last run` — pass an inline instruction.
- [`/portfolio-pulse`](skills/portfolio-pulse/SKILL.md) — a check-up on your saved holdings.
- [`/polymarket-watch`](skills/polymarket-watch/SKILL.md) — this morning's interesting prediction markets, on demand.

**Go deeper with the analysis skills.** The [`LLMQuant/skills`](https://github.com/LLMQuant/skills) toolkit triggers the same way — `/llmquant-equities`, `/llmquant-macro`, `/llmquant-prediction-markets`, 18 in all; run `hermes skills list` to see them. You can stack up to five skills in one message.

Want a playbook to run on its own? Each `SKILL.md` carries a cron command. `hermes cron trigger` fires the job immediately, so you can confirm it works without waiting for the next scheduled run.

## What it looks like

**One paste sets everything up.** The agent connects the MCP, installs the skills, and hands you first steps:

![Setup complete — the agent offers a first question, a manual morning-brief run, and the slash commands](docs/images/setup-complete.png)

**Ask in plain language.** NVDA's price action, answered from LLMQuant Data tools with the week's news behind it:

![NVDA price action over two weeks, answered in the Hermes terminal](docs/images/terminal-session.png)

**It knows your saved holdings.** `personal_holdings` turns your LLMQuant profile into a portfolio snapshot (demo profile shown — illustrative data):

![Holdings snapshot with P&L from a demo LLMQuant profile — illustrative data](docs/images/holdings-snapshot.png)

## FAQ

**Remote MCP URL or local stdio?**
Prefer the hosted Remote MCP URL — it needs no local Node.js and avoids a stdio bug where `hermes mcp add --env` wrote the key into `args` instead of `env` (seen on v0.18.0). If you do use stdio, put `LLMQUANT_API_KEY` under `env` and edit the YAML by hand.

**`hermes skills tap add` didn't install anything?**
Tap can register a source without installing it. Run `hermes skills list`; if a skill is missing, install it with your Hermes version's skill flow, or copy the repo's `skills/` into `~/.hermes/skills/` — Hermes only reads that global path.

**My cron fired at the wrong time?**
Cron runs in the host machine's local time on some Hermes versions. Confirm the next-run time with `hermes cron list` after scheduling; `every 3d` parses on v0.18.x and later.

**What does it cost?**
Two separate bills. **Hermes model inference** is paid to your model backend (Nous Portal, DeepSeek, OpenRouter, …); **LLMQuant credits** are spent only when a playbook calls LLMQuant Data tools. The Free Beta plan is enough to try things out — current plans are at [llmquantdata.com](https://llmquantdata.com).

## Reference

### How this fits together

Three layers, wired by one paste: **[LLMQuant Data](https://github.com/LLMQuant/data-mcp)** is the tools (prices, filings, 13F holdings, macro, and company news over MCP), **[`LLMQuant/skills`](https://github.com/LLMQuant/skills)** is the analysis method, and **[Hermes](https://github.com/NousResearch/hermes-agent)** is the runtime (cron, messaging, memory). This repo is the glue — it answers **how to watch, not how to analyze**: when a job runs, which tools it calls, where the output goes. Alongside the playbooks it ships the setup runbook ([`SETUP.md`](SETUP.md)), an analyst persona and workspace templates ([`templates/`](templates/)), and MCP config examples ([`config/`](config/)).

### Company news

The playbooks lean on `news_browse`, the LLMQuant Data tool for recent company news. It returns an AI-written title, abstract, summary, event/topic labels, tickers, publication date, and a source link. It is exact filtering, not semantic search — query by ticker, event, topic, date range, and limit. Coverage runs from April 11, 2026 onward.

### Repository layout

```text
llmquant-hermes/
├── README.md
├── README.zh-CN.md
├── SETUP.md
├── LICENSE
├── docs/
│   └── images/            # screenshots referenced by "What it looks like"
├── skills/
│   ├── llmquant-setup/SKILL.md
│   ├── morning-brief/SKILL.md
│   ├── earnings-watch/SKILL.md
│   ├── 13f-diff/SKILL.md
│   ├── portfolio-pulse/SKILL.md
│   └── polymarket-watch/SKILL.md
├── templates/
│   ├── SOUL.md
│   └── AGENTS.md
└── config/
    ├── mcp-remote.example.yaml
    └── mcp-stdio.example.yaml
```

## Contributing

Keep this repo small: add a playbook only if it needs Hermes-specific capabilities — cron, messaging, persistent memory, or standing agent context. Anything that works equally in Claude Code, Cursor, or Codex belongs in [`LLMQuant/skills`](https://github.com/LLMQuant/skills), not here.

## License

MIT. See [LICENSE](LICENSE).

<div align="center">
  <br/>
  <strong><a href="https://llmquant.com">LLMQuant</a></strong>
  <br/>
  <sub>Open-source community for AI, LLMs, and quantitative finance.</sub>
  <br/><br/>
  <a href="https://llmquantdata.com">LLMQuant Data</a> ·
  <a href="https://github.com/LLMQuant/data-mcp">Data MCP</a> ·
  <a href="https://github.com/LLMQuant/skills">Skills</a>
  <br/>
  <a href="https://llmquant.com">Website</a> ·
  <a href="https://github.com/LLMQuant">GitHub</a> ·
  <a href="https://linkedin.com/company/llmquant">LinkedIn</a>
</div>
