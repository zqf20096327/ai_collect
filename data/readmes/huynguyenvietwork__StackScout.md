<div align="center">

# StackScout

**New tech, matched to your stack.**

A weekly tech radar that reads the sources that matter, picks what is relevant to *the tools you actually use*, and compares each new thing with them, with a source link for every claim.

[**Live demo**](https://huynguyenvietwork.github.io/StackScout/) · [**Download**](https://github.com/huynguyenvietwork/StackScout/releases/latest) · [Quick start](#quick-start) · [Changelog](CHANGELOG.md) · [Tiếng Việt](README.vi.md) · [**Want it hosted? Join the waitlist**](../../issues/new?template=hosted_waitlist.yml)

[![Latest release](https://img.shields.io/github/v/release/huynguyenvietwork/StackScout)](https://github.com/huynguyenvietwork/StackScout/releases/latest) ![CI](../../actions/workflows/ci.yml/badge.svg) ![License: MIT](https://img.shields.io/badge/license-MIT-blue)

![StackScout demo](docs/assets/demo.gif)

</div>

## Quick start

> **Scope:** StackScout is currently designed for personal self-hosting. The web UI serves one local profile and has no login: it listens on 127.0.0.1 only, so don't expose it to a network without authentication in front of it. A managed hosted version may come later.

You need an AI backend: an **Anthropic API key**, or the [Claude Code](https://code.claude.com) CLI already logged in (any CLI that reads a prompt on stdin works through `STACKSCOUT_AI_CMD`). See [what it costs](#what-it-costs).

### 🤖 Install with your AI assistant

Using Claude Code, Cursor or Codex? Paste this:

```text
Install StackScout from https://github.com/huynguyenvietwork/StackScout: clone it, follow its AGENTS.md, run `main.py doctor` until there is no ❌, then open the web UI. When an API key or token is needed, ask me to enter it in my own terminal, never in this chat.
```

It checks your machine, installs what is missing and opens the web UI. [AGENTS.md](AGENTS.md) tells it what to do, and that secrets never go through the chat.

### Docker, prebuilt image (no clone)

```bash
read -rsp "Anthropic API key: " ANTHROPIC_API_KEY && export ANTHROPIC_API_KEY   # hidden, not in your shell history
docker run -d --name stackscout --restart unless-stopped -p 127.0.0.1:8000:8000 -e ANTHROPIC_API_KEY \
  -v stackscout_data:/app/data -v stackscout_reports:/app/reports ghcr.io/huynguyenvietwork/stackscout
```

Open http://127.0.0.1:8000. Check the setup with `docker exec stackscout uv run --no-sync main.py doctor --online`. Notification channels are set in the web UI.

### Docker Compose (from source)

```bash
git clone https://github.com/huynguyenvietwork/StackScout && cd StackScout   # or: unzip the release, cd into it
cp .env.example .env          # set ANTHROPIC_API_KEY, and a notification channel if you want one
docker compose up -d --build --wait   # web UI on http://127.0.0.1:8000; digests go out on the schedule set in the Notifications tab
docker compose exec web uv run --no-sync main.py doctor   # check the setup
docker compose --profile bot up -d   # optional: the Telegram bot too
```

### uv

```bash
git clone https://github.com/huynguyenvietwork/StackScout && cd StackScout   # or: unzip the release, cd into it
uv sync                       # Python 3.11+, https://docs.astral.sh/uv/
uv run main.py setup          # creates .env, asks for the API key (hidden) or uses the `claude` CLI, then checks everything
uv run main.py web            # http://127.0.0.1:8000
```

No git? [Download the latest release](https://github.com/huynguyenvietwork/StackScout/releases/latest) (**Source code (zip)** under *Assets*), unzip it and open a terminal in that folder. Something wrong? `uv run main.py doctor` lists what is missing and how to fix it.

Create your profile in the browser (about 2 minutes), press **Run this week's radar** (2–3 minutes), and comparisons fill in on their own over the next minutes.

### What it costs

StackScout itself is free. The AI calls are what cost something, once a week (or per day/month, as you schedule it):

- **Claude Code CLI**: runs on your Claude plan, no extra bill. Measured on a fresh install with a 9-technology profile: one weekly run made 16 comparisons (6 against the stack, 10 new models vs their rivals) in about 17 minutes.
- **Anthropic API key**: billed per token plus web searches. Not measured yet; the server log prints the tokens and searches of every call with running totals (`api usage: …`), so you can see your own cost. A smaller profile means fewer comparisons; `STACKSCOUT_MODEL` picks a cheaper model.

## Why

Keeping up is a part-time job: new models every week, new libraries, release notes, benchmarks that disagree. Most newsletters list *everything*. StackScout starts from **your stack** and answers one question per item: *should I care, and how does it compare with what I use today?*

## Features

<table>
<tr>
<td width="29%" valign="top">

### 📡 Your week at a glance

One page with the week's headlines, grouped by what they mean for you.

- New AI models & tools
- New tech of the same kind as your stack
- Updates to tools you already use
- Other ecosystems, new areas, weekly roundup

Click **Details** to read a group in full.

</td>
<td width="71%" valign="top"><a href="docs/assets/overview.png"><img src="docs/assets/overview.png" alt="Weekly overview: headlines grouped by type"></a></td>
</tr>
<tr>
<td width="29%" valign="top">

### 🤖 New AI models vs. their strongest rivals

Straight from first-party channels: Anthropic, OpenAI, Google DeepMind, Gemini, Hugging Face…

Click a model to open its own page with its **3–5 strongest competitors**, already researched:

- a table of the rivals at a glance, then one section per rival
- key numbers side by side (benchmarks, prices, context window…)
- what it does better and worse, and which one to pick, a link behind every line

</td>
<td width="71%" valign="top"><a href="docs/assets/rivals.png"><img src="docs/assets/rivals.png" alt="GPT-6.2 Astra compared with Claude Fable 5.2, Gemini 4 Carbon and others"></a></td>
</tr>
<tr>
<td width="29%" valign="top">

### 🧩 Compared with your stack, automatically

Right after the radar runs, every new technology of the same kind as one of your tools is compared with that tool, grouped by your skills.

- a verdict: **adopt, trial, watch or skip**
- **Details** opens a full page; Back returns to your place in the list
- **⋯** compares it with any other tool in your profile

</td>
<td width="71%" valign="top"><a href="docs/assets/vs-stack.png"><img src="docs/assets/vs-stack.png" alt="New tools grouped by the skill they compete with, each with a verdict"></a></td>
</tr>
<tr>
<td width="29%" valign="top">

### 🔗 Every claim has a source

Each comparison has its own page: the verdict and its confidence, a *for you* note, what is new, **key numbers side by side**, up to 5 pros and 5 cons, **how hard it is to switch**, and the numbered sources.

Enforced in code, not left to the AI:

- a claim without a valid link is dropped
- fewer than 2 sources → *"not enough data yet"*
- independent benchmarks preferred and labelled

</td>
<td width="71%" valign="top"><a href="docs/assets/claims.png"><img src="docs/assets/claims.png" alt="SQLite vs PostgreSQL: verdict, fit, pros, cons and numbered sources"></a></td>
</tr>
<tr>
<td width="29%" valign="top">

### 📬 The digest, where you read

Every week, in your language, on any of:

- **Telegram**
- **Email**
- **Slack** and **Discord**
- any **webhook** (n8n, Zapier, Make…)

Under each item: the verdict against your tool, or the rivals of a new model.

</td>
<td width="71%" valign="top"><a href="docs/assets/digests.png"><img src="docs/assets/digests.png" alt="The weekly digest by email and on Telegram"></a></td>
</tr>
<tr>
<td width="29%" valign="top">

### 🔔 Notifications, set up in minutes

A dedicated tab: **daily, weekly or monthly**, at the time you pick, then turn on any channel.

- step-by-step guide for each one (BotFather, Gmail app password, Slack and Discord webhooks…)
- presets for Gmail, Outlook and SendGrid; **Find chat ID** for Telegram
- **Save and send a test**, plus a delivery log
- secrets stay on your machine, never shown again

</td>
<td width="71%" valign="top"><a href="docs/assets/notifications.png"><img src="docs/assets/notifications.png" alt="Notifications tab: schedule and channel setup"></a></td>
</tr>
<tr>
<td width="29%" valign="top">

### 👤 Your profile, in your own words

Type what you use, typos and all (*"c#, entity framwork, postgres, k8s"*), or generate it from your code or CV with the included prompt.

- AI normalises names and levels; you confirm before saving
- **private by design**: only technology names and levels are stored, nothing about your projects or employer

</td>
<td width="71%" valign="top"><a href="docs/assets/profile.png"><img src="docs/assets/profile.png" alt="Skill profile grouped by category, with levels"></a></td>
</tr>
<tr>
<td width="29%" valign="top">

### 📰 Sources that matter, picked for your stack

About 60 curated, live feeds.

- first-party AI channels: always on
- official blogs and release feeds of *your* technologies: on automatically
- community sources (Hacker News, trending GitHub repos, Lobsters…): one click
- add any blog, RSS feed or GitHub repo

</td>
<td width="71%" valign="top"><a href="docs/assets/sources.png"><img src="docs/assets/sources.png" alt="Source list with first-party and official feeds"></a></td>
</tr>
<tr>
<td width="29%" valign="top">

### 🌏 5 languages, light and dark, on your phone

English, Tiếng Việt, 中文, 日本語, 한국어 for the interface, the AI-written summaries and comparisons, the digests and the Telegram bot.

Light and dark themes; comparisons open as a bottom sheet on phones.

</td>
<td width="71%" valign="top"><a href="docs/assets/looks.png"><img src="docs/assets/looks.png" alt="Dark theme in Japanese, light theme in Vietnamese, and a phone"></a></td>
</tr>
</table>

## How it works

1. **Profile**: your technologies and levels, normalised to a fixed taxonomy.
2. **Collect**: the week's items from your sources (RSS/Atom, release feeds, Hacker News, GitHub, sitemaps), deduplicated across weeks.
3. **Classify** with AI into the same taxonomy, then **match in plain Python**:

   | Match | What you get |
   |---|---|
   | New version of a tool you use | Short changelog line |
   | **Same category, same ecosystem** | **Automatic comparison with your tool** |
   | Same category, other ecosystem | Reference note |
   | New model or AI tool | **Comparison with its strongest competitors** |
   | Category you don't have yet | "Worth a look" |

4. **Compare** with web search, then enforce the source rules in code; **deliver** on your channels.

## Notifications

Open the **Notifications** tab, pick **daily, weekly or monthly** and the time, and set up any of **Telegram, email, Slack, Discord** or a **JSON webhook** (n8n, Zapier, Make, ntfy…). Each channel has a step-by-step guide, a test button and a delivery log. A daily digest only has what is new since the last one (no message on quiet days); a monthly one covers the last 31 days. The web server sends on schedule, so there is no cron to set up; if the machine was off at that time, the digest goes out as soon as it is back.

Secrets you enter there go only to your own StackScout server, are stored in `data/users/<id>/notify.yaml` (owner-only file) and are never returned to the browser after saving. For Docker or several users, the same settings can come from `.env` (`TELEGRAM_BOT_TOKEN`, `SMTP_HOST`…, see `.env.example`); they fill any field left empty in the tab.

Without the web UI: `uv run main.py schedule` sends on the same schedule, and `uv run main.py digest` sends right now (cron-friendly).

## Telegram bot

`uv run main.py bot` (set `TELEGRAM_BOT_TOKEN` and `STACKSCOUT_ALLOWED_USERS` first: every request costs an AI call on your account). The bot follows your Telegram language; change it with `/language`.

| Command | What it does |
|---|---|
| `/start` | Create your profile |
| `/profile`, `/add redis, kafka`, `/remove` | View and edit your skills |
| `/sources`, `/addsource <link>`, `/reset` | Manage sources |
| `/radar` | Build this week's radar now |
| send a `.yaml` file | Import a profile generated from your code or CV |
| `/language`, `/cancel` | Change language, abort the current step |

## Privacy

- Your profile stores **technology names and levels only**. Project names, repos, what they are for and anything about your employer are dropped on save and on import; URLs, emails, IPs, hostnames and secret-looking strings are scrubbed from free text.
- Secrets (API key, bot token, SMTP password, webhook URLs) are sent only to your self-hosted StackScout server, stored locally with owner-only permissions (`.env` or `data/users/<id>/notify.yaml`), and never returned to the browser after saving.
- Every AI step runs without tools, except comparisons, which get web search and fetch only. Your profile is never put in a search query.
- Data stays on your machine: `data/` (profiles, sources, comparisons) and `reports/` are plain files.

## Project layout

```
config/                  taxonomy and the curated source catalog
prompts/                 every prompt, kept out of code so they are easy to tune
stackscout/ai.py         AI backends: Anthropic API or a headless CLI
stackscout/profile.py    normalise, validate, merge, import profiles
stackscout/sources.py    per-user sources, feed discovery, SSRF guard
stackscout/collect.py    RSS / Hacker News / GitHub / sitemap fetchers, dedupe
stackscout/classify.py   AI classification + Python matching
stackscout/compare.py    sourced comparisons (your stack, market rivals), rule enforcement
stackscout/digest.py     the weekly pipeline, comparison caches, report files
stackscout/render.py     the digest for each channel, in each language
stackscout/notify.py     Telegram, email, Slack, Discord, webhook delivery
stackscout/i18n.py       server-side messages in 5 languages
stackscout/web.py        local web UI + API;  stackscout/static/index.html
stackscout/bot.py        Telegram bot (texts in bot_text.py)
main.py                  web | bot | digest | schedule
scripts/build_demo.py    builds the read-only demo in docs/
```

## Contributing

Ideas, sources, languages and channels are all welcome: see [CONTRIBUTING.md](CONTRIBUTING.md). Run the tests with `uv run pytest -q` (offline, no AI calls). Security issues: [SECURITY.md](SECURITY.md).

**Would you use a hosted version** (no install, no API key)? [Tell us here](../../issues/new?template=hosted_waitlist.yml): it decides whether we build it.

## License

[MIT](LICENSE)
