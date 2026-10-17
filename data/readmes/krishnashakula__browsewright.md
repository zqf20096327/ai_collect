<div align="center">

# 🦾 Browsewright

### The browser that scripts itself.

**Give an LLM a URL and a goal. It drives a real Chrome, fills out forms, gets past
bot walls, and hands you structured data not raw HTML.**

[![CI](https://github.com/krishnashakula/browsewright/actions/workflows/ci.yml/badge.svg)](https://github.com/krishnashakula/browsewright/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/browsewright?color=2563eb&cacheSeconds=3600)](https://pypi.org/project/browsewright/)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-orange)](https://github.com/krishnashakula/browsewright/pulls)

</div>

---

**Browsewright is an open-source, MIT-licensed Python library for intent-driven browser automation and AI web scraping.** You give it a URL and a goal in plain English, and a large language model drives a real Chrome browser to navigate, fill out forms, get past bot protection, and return structured JSON instead of raw HTML — no selectors, no XPath, and no scrapers to maintain when a site ships a redesign.

> **Playwright automates a browser _you_ script.**
> **Browsewright is the browser that scripts _itself_.**

You don't write selectors. You don't maintain scrapers that break every time a
site ships a redesign. You give it intent — *"find the pricing"*, *"enrich this
lead"*, *"fill out this form"* — and an LLM drives a real browser to get it done.

```bash
pip install browsewright
bw "https://stripe.com" "what does this company do and who is it for"
```

```
============================================================
RESULT  [api]  412 tokens  3.1s
------------------------------------------------------------
Stripe is financial infrastructure for the internet. It provides
payment processing, billing, and treasury APIs for businesses from
startups to enterprises like Amazon and Shopify...
============================================================
```

<!-- TODO: Record the Maryland form-fill (your best hero clip) and drop it at docs/demo.gif.
     A 30–60s GIF showing the form filling itself and returning JSON is the single
     highest-converting thing you can add above the fold. Until then this image is a placeholder. -->
<p align="center">
  <img src="docs/demo.gif" alt="Browsewright filling a real government form that has no API and returning structured JSON" width="820">
  <br>
  <em>Browsewright reading a form's labels, filling it with an LLM, and returning results as JSON — no selectors written.</em>
</p>

---

## 🤯 It doesn't just read the web. It *does things* on the web.

Most "AI scrapers" hand you text. Browsewright **acts**. Point it at a real
government records form with no API, give it a profile, and walk away:

```bash
bw-tasks form \
  "https://registers.maryland.gov/RowNetWeb/Estates/frmEstateSearch2.aspx" \
  --profile examples/sample_profile.json
```

It read the field labels, mapped your profile onto the form with an LLM, picked
valid dropdown options, submitted it, and came back with:

> **Page 1 of 815** results — real names and dates, extracted as JSON.

No selectors. No XPath. No API. The form has none — it's a 20-year-old ASP.NET
page that's invisible to every HTTP scraper. Browsewright drives it like a human.

---

## 💸 And it's almost free

> **Benchmark — 50 real, diverse websites in one run:**
> **50 / 50 extracted successfully · `$0.047` total · ~1,200 tokens & ~20s median per site.**
> 28% were answered by the free API/archive shortcut with **no browser at all.**
> _(Reproduce it: `python examples/batch_test.py`.)_

It tries the **cheapest path first** — open APIs, RSS, public archives — and only
spins up Chrome when a page actually needs it. You pay pennies for the easy 80%
and a real browser for the hard 20%.

---

## How it stacks up

| | **Browsewright** | Firecrawl | Browser-Use | Tavily |
|---|:---:|:---:|:---:|:---:|
| Returns structured JSON from intent | ✅ | ✅ | ⚠️ scripted | ✅ |
| **Fills & submits real forms** | ✅ | ❌ | ✅ | ❌ |
| Drives a **real** Chrome (human motor layer) | ✅ | ❌ | ✅ | ❌ |
| Gets past Cloudflare/DataDome bot walls | ✅ | ⚠️ | ⚠️ | ❌ |
| Free API/archive shortcut before any browser | ✅ | ❌ | ❌ | ❌ |
| Runs **fully local**, your own API key | ✅ | ❌ SaaS | ✅ | ❌ SaaS |
| 5 ready-made business tasks built in | ✅ | ❌ | ❌ | ❌ |
| MIT, self-hostable | ✅ | partial | ✅ | ❌ |

*Comparisons reflect typical default usage; all four are good tools. Browsewright's
bet is **intent in → action + structured data out**, run locally for pennies.*

---

## Install

```bash
pip install browsewright          # core
pip install "browsewright[mcp]"   # + MCP server (Claude Desktop / Code / any client)
```

Or from source:

```bash
git clone https://github.com/krishnashakula/browsewright && cd browsewright
python -m venv .venv && . .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -e .
```

Add your Anthropic API key:

```bash
cp .env.example .env
# edit .env and paste your key from https://console.anthropic.com/settings/keys
```

The first browser run launches Chrome via `nodriver` (Chrome must be installed).

> **`bw` "not recognized" after install?** pip put the scripts in a folder that
> isn't on your PATH (common on Windows). Use the module form, which always works:
> `python -m browsewright "<url>" "<goal>"` · `python -m browsewright.tasks_cli enrich "<url>"`

---

## Use it

### CLI

```bash
bw "https://news.ycombinator.com" "the top story right now"
bw "https://example.com" "find the pricing" --json
bw "https://example.com" "debug this" --no-headless --verbose
```

### Python

```python
import asyncio
from browsewright import search

res = asyncio.run(search("https://stripe.com", "what does this company do"))
print(res.answer)         # synthesized answer
print(res.stage)          # "api" | "browser" | "common_crawl" | "blocked" | "error"
print(res.tokens_total, res.elapsed_s)
```

### As an MCP tool (Claude Desktop / Claude Code / any MCP client)

```jsonc
{ "mcpServers": { "browsewright": { "command": "bw-mcp" } } }
```

Your LLM now has a `read_page(url, goal)` tool.

---

## The 5 built-in tasks — `bw-tasks`

One pipeline — **fetch → structured extract (JSON) → diff/aggregate → action** —
exposed as five business workflows. Each is a CLI subcommand and a library function.

| Task | Command | Output |
|---|---|---|
| 🕵️ Competitor watch | `bw-tasks watch <url>` | Baseline now, change alerts later |
| 🎯 Lead enrichment | `bw-tasks enrich <url>` | CRM fields + a personalized cold-email line |
| 📝 Agentic form fill | `bw-tasks form <url> --profile p.json` | Understands fields, fills, submits, reads results |
| 💰 Price/stock tracking | `bw-tasks track <url>` | Price & availability change alerts |
| 📣 Brand monitoring | `bw-tasks brand <name> <urls…>` | Mentions + sentiment digest |

Common flags: `--json`, `--out FILE`, `--slack <webhook>`, `--no-headless`, `--aggressive`.

**Real `enrich` output (trimmed):**

```json
{
  "company_name": "Tavily",
  "industry": "AI/SaaS - Developer Tools",
  "tech_stack_or_integrations": ["OpenAI", "Anthropic", "Groq", "Databricks"],
  "recent_news_or_signals": ["Raised $25M Series A", "Databricks MCP partnership"],
  "icp_fit_score_1_to_10": 7,
  "personalized_cold_email_first_line": "I noticed Tavily just partnered with Databricks on the MCP Marketplace—looks like you're doubling down on enterprise adoption after your $25M Series A."
}
```

### Build your own task with the core primitive

Every task is a thin wrapper over `extract_structured(url, schema)`. Define any
schema, get JSON back:

```python
import asyncio
from browsewright import extract_structured

schema = {"headline": "string",
          "open_roles": [{"title": "string", "team": "string", "location": "string"}]}
data = asyncio.run(extract_structured(
    "https://example.com/careers", schema,
    instruction="Extract the page headline and every open job posting."))
print(data["open_roles"])
```

### Scheduling

Tasks are single-shot; snapshot/diff state persists between runs, so change
detection works across invocations. Run on cron, n8n/Make/Zapier, or `/loop`:

```bash
# every 6h, alert on competitor pricing changes
0 */6 * * * bw-tasks watch "https://competitor.com/pricing" --slack https://hooks.slack.com/services/XXX
```

---

## How it works

```
search(url, goal)
   │
   ├─ Polite gate ........ robots.txt check + per-host rate limit
   │
   ├─ Pre-flight pipeline (cheapest path first)
   │     1. Common Crawl ... public archive            (opt-in)
   │     2. Open API ....... RSS / wp-json / *.json     (no browser, ~1.5k tokens)
   │     3. Origin IP ...... CDN bypass                 (skipped in polite mode)
   │     4. Classifier ..... detect Cloudflare/Akamai/DataDome/…
   │
   └─ Browser session (only if no shortcut hit)
         • real headless Chrome via nodriver (native TLS fingerprint)
         • human motor layer — Bézier mouse, typing cadence, scroll pacing
         • LLM decides actions only at junctions (~1 call/page)
         • blind-scene shortcut: extract directly when the DOM scan is blocked
         • visual recovery: a vision call clears interstitials/challenges
```

---

## Polite by default

**Polite mode is the default and what you should ship.** It checks `robots.txt`,
rate-limits per host, and does **not** bypass CDN bot protection. `--aggressive`
(`polite=False`) enables origin-IP discovery and ignores robots — use it **only**
on targets you own or are authorized to test.

> ⚠️ **You are responsible** for complying with each site's Terms of Service,
> applicable law (CFAA and equivalents), and data-protection rules (GDPR/CCPA).
> Browsewright is for authorized research, your own properties, and sites whose
> terms permit automated access. The authors accept no liability for misuse.

---

## FAQ

**What is Browsewright?**
Browsewright is an open-source, MIT-licensed Python library for intent-driven browser automation and AI web scraping. You give it a URL and a goal in plain language, and a large language model drives a real Chrome browser to navigate, fill out forms, bypass bot protection, and return structured JSON instead of raw HTML. Install it with `pip install browsewright`.

**How is Browsewright different from Playwright or Selenium?**
Playwright and Selenium automate a browser that you script with explicit selectors and XPath. Browsewright is the opposite: you describe intent ("find the pricing", "fill this form") and an LLM decides the actions, so there are no selectors to write and no scrapers to maintain when a site changes its layout.

**How is Browsewright different from Firecrawl, Browser-Use, and Tavily?**
Browsewright fills and submits real forms, drives a real Chrome browser, tries free API and archive shortcuts before launching a browser, and runs fully locally on your own API key. Firecrawl and Tavily return text but do not fill forms or drive a real browser, and Browser-Use drives a browser but is scripted rather than intent-first and has no free pre-flight shortcut.

**Can Browsewright fill out and submit web forms?**
Yes. Browsewright reads a form's field labels, maps a user profile onto the fields with an LLM, selects valid dropdown options, submits the form, and parses the results into JSON. It has filled real government records forms that expose no API.

**Does Browsewright work on websites with no API?**
Yes. Browsewright drives a real browser the way a human would, so it works on sites that have no API at all, including 20-year-old ASP.NET pages that are invisible to HTTP-only scrapers.

**Can Browsewright get past Cloudflare or DataDome bot protection?**
Browsewright runs a real Chrome browser via nodriver with a native TLS fingerprint and a human motor layer (Bézier-curve mouse movement, typing cadence, and scroll pacing), which lets it pass many Cloudflare, Akamai, and DataDome bot checks. Bypassing CDN bot protection is disabled in the default polite mode and is only enabled with the `--aggressive` flag on sites you own or are authorized to test.

**How much does it cost to run?**
In a benchmark across 50 diverse websites, Browsewright extracted all 50 for $0.047 total, with about 28% answered by a free API or archive shortcut and no browser at all. It tries the cheapest path first and only launches Chrome when a page requires it.

**Is Browsewright free and open source?**
Yes. Browsewright is free and MIT-licensed, runs locally, and uses your own Anthropic API key, so you pay only for the LLM tokens you use — typically a fraction of a cent per page.

**Can I use Browsewright with Claude or as an MCP tool?**
Yes. Browsewright ships an MCP server (`bw-mcp`) that exposes a `read_page(url, goal)` tool to any MCP client, including Claude Desktop and Claude Code. Install it with `pip install "browsewright[mcp]"`.

**Does Browsewright run locally?**
Yes. Browsewright runs entirely on your own machine with your own API key. There is no SaaS backend, and no data is sent anywhere except the LLM provider you configure.

**What do I need to run Browsewright?**
Browsewright requires Python 3.10 or newer and a local installation of Chrome, which it launches via nodriver on the first browser run. Add an Anthropic API key to a `.env` file to get started.

---

## ⭐ Star history

[![Star History Chart](https://api.star-history.com/svg?repos=krishnashakula/browsewright&type=Date)](https://star-history.com/#krishnashakula/browsewright&Date)

---

## ⭐ Star it / contribute

If Browsewright saved you a scraper, **drop a star** — it's the whole reason this
is open source. Issues and PRs welcome: pre-flight vendors, new tasks, more sites
in the benchmark.

**MIT licensed.** Built on [`nodriver`](https://github.com/ultrafunkamsterdam/nodriver)
+ [Anthropic Claude](https://www.anthropic.com/).
