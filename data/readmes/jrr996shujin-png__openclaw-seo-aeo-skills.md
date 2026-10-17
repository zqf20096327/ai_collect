# 🦞 openclaw-seo-aeo-skills

**SEO & AEO skill pack for [OpenClaw](https://openclaw.ai) — turn your personal AI assistant into an SEO/AEO analyst.**

Search is shifting from blue links to AI-generated answers. Google AI Overviews, ChatGPT Search, Perplexity, and Claude are now the front door for millions of queries. Traditional SEO still matters, but it's no longer enough. You also need **Answer Engine Optimization (AEO)** — making your content the source that AI engines cite.

This skill pack gives your OpenClaw agent the ability to:

- 🔍 **Diagnose** your website's technical health and AI-readiness
- 📡 **Discover** what real users are asking on Reddit/Quora and mine long-tail questions for AEO
- 📊 **Monitor** your keyword rankings, content performance, and competitor activity
- 📋 **Report** monthly with interactive dashboards and prioritized action plans

## Skills Overview

| Skill | What It Does | Trigger Examples |
|-------|-------------|-----------------|
| [`aeo-content-strategy`](#aeo-content-strategy) | Reddit/Quora monitoring → long-tail question mining → content topic recommendations | *"What should I write about?"* *"What are people asking on Reddit?"* |
| [`seo-aeo-diagnostics`](#seo-aeo-diagnostics) | 7-module website health check covering technical SEO, AI crawler accessibility, structured data, content structure, and more | *"Check my website"* *"Diagnose example.com"* |
| [`seo-competitive-intel`](#seo-competitive-intel) | Keyword ranking + content performance tracking + competitor content monitoring + monthly reports | *"How are our rankings?"* *"What did competitors publish?"* *"Generate monthly report"* |

### How They Work Together

```
┌─────────────────────────────────┐
│   seo-competitive-intel         │
│   (monthly report finds gaps)   │
└──────────┬──────────┬───────────┘
           │          │
     content gap    page decay
     detected       detected
           │          │
           ▼          ▼
┌──────────────┐ ┌──────────────────┐
│ aeo-content  │ │ seo-aeo          │
│ -strategy    │ │ -diagnostics     │
│ (mine long-  │ │ (run technical   │
│  tail topics)│ │  audit on page)  │
└──────────────┘ └──────────────────┘
```

---

## Quick Start

### Installation

```bash
# Clone the repo
git clone https://github.com/jrr996shujin-png/openclaw-seo-aeo-skills.git

# Run the installer
cd openclaw-seo-aeo-skills
bash install.sh
```

This copies all three skills into `~/.openclaw/skills/`. Restart OpenClaw or start a new session to pick them up.

### Configuration

`seo-competitive-intel` requires API keys. Add them to `~/.openclaw/openclaw.json`:

```json
{
  "skills": {
    "entries": {
      "seo-competitive-intel": {
        "enabled": true,
        "apiKey": "YOUR_SEMRUSH_API_KEY",
        "env": {
          "SEMRUSH_API_KEY": "YOUR_SEMRUSH_API_KEY"
        }
      }
    }
  }
}
```

Google Search Console and Google Analytics authenticate via OAuth on first run — OpenClaw's browser tool handles the flow automatically.

The other two skills (`aeo-content-strategy` and `seo-aeo-diagnostics`) require no API keys and work out of the box using OpenClaw's built-in web browsing capabilities.

### Try It

Message your OpenClaw on WhatsApp, Telegram, Discord, or any connected channel:

```
"Diagnose example.com for SEO and AEO readiness"
"What are people asking about AI writing tools on Reddit?"
"How are our keyword rankings this week?"
"Generate this month's SEO report"
```

---

## Skills in Detail

### `aeo-content-strategy`

**What it does:** Generates a complete AEO content strategy by combining community monitoring, long-tail question mining, and prioritized content recommendations.

**Why it matters:** AI search engines cite content that directly answers specific questions. This skill finds those questions before your competitors do — by listening to what real users are asking on Reddit and Quora, then transforming those signals into content your team can execute immediately.

**How it works:**

| Phase | Action | Output |
|-------|--------|--------|
| 1. Community Scan | Searches Reddit & Quora for discussions about your product category, brand, and competitors | 30-50 relevant threads with engagement data |
| 2. Signal Analysis | Categorizes threads: unanswered questions, competitor mentions, brand sentiment, general discussions | Prioritized opportunity map |
| 3. Long-Tail Mining | Transforms community signals into 25+ word conversational questions (how real users ask AI) | 40-50 long-tail questions |
| 4. Prioritization | Scores each topic on competition level, purchase intent, and AI citation potential | Ranked topic list |
| 5. Report | Assembles everything into an actionable report with content calendar | Ready-to-execute content plan |

**Required inputs:** Brand name, product category, target audience, 2-3 competitor names, key use cases, target market.

**Output:** A structured report including executive summary, community landscape, question bank, top 15 content recommendations with outlines, and a weekly content calendar.

📄 [Full documentation →](docs/aeo-content-strategy.md)

---

### `seo-aeo-diagnostics`

**What it does:** Runs a comprehensive health check on any website, scoring it across 7 modules on a 100-point scale. Goes beyond traditional SEO to evaluate AI-readiness — can AI crawlers access your content? Can AI engines understand your page structure? Will AI platforms choose to cite you?

**Modules:**

| Module | Checks | Points | Why It Matters for AEO |
|--------|--------|--------|----------------------|
| Technical Foundation | Dead links, page speed, mobile-friendliness, HTTPS | /20 | Broken pages can't be crawled by anyone |
| Search Accessibility | Robots.txt (incl. GPTBot, ClaudeBot, PerplexityBot), Sitemap, HTML vs JS rendering, Canonical tags | /20 | Most AI crawlers don't execute JavaScript — if your content depends on JS, AI can't see it |
| Structured Data | Schema Markup, Open Graph, Twitter Cards, hreflang | /15 | Schema helps AI engines understand what your content IS, not just what it says |
| Content Structure | Meta tags, H1-H4 hierarchy, list independence, tables, FAQ format | /15 | AI engines extract structured content 37% more often than unstructured text |
| Multimedia Accessibility | Image alt text, video transcripts | /10 | AI can't see images or hear video — alt text and transcripts are all they have |
| Content Quality Signals | Author info (E-E-A-T), publish/update dates, word count, readability | /10 | AI engines increasingly favor content from identifiable, credible authors |
| Site Architecture | Internal link health, click depth to key pages | /10 | Deep-buried pages are hard for any crawler to discover |

**Usage:** Provide a URL and the skill runs all 7 modules (or specific ones if you prefer), then generates a prioritized fix list.

Each sub-module can also be triggered independently — ask "check my robots.txt" and only the Search Accessibility module runs.

📄 [Full documentation →](docs/seo-aeo-diagnostics.md)

---

### `seo-competitive-intel`

**What it does:** Dual-perspective (brand vs competitor) monitoring system that tracks keyword rankings, content performance, and competitor publishing activity — then generates monthly reports with actionable recommendations.

**Sub-modules:**

#### Keyword & Ranking Tracker

Manages keywords in 4 categories with different alert thresholds:

| Category | Examples | Alert Threshold |
|----------|---------|----------------|
| A: Brand terms | Your company name, product names | Drop out of top 3 |
| B: Core business | "best AI agent", "AI productivity tool" | Drop ≥ 5 positions |
| C: Long-tail questions | "what AI tool can automate customer emails" | Drop out of page 1 |
| D: Competitor comparisons | "Genspark vs Manus", "Manus alternative" | Drop ≥ 5 positions |

Tracks both **Google and Bing** rankings — Bing matters because ChatGPT Search uses the Bing index. Your Bing ranking directly affects whether ChatGPT cites you.

#### Content Performance Tracker

Monitors every page on your site weekly:
- Identifies **rising content** (click growth > 20%)
- Flags **decaying content** (traffic down ≥ 10% over 30 consecutive days)
- Tracks **new articles** through a 7/14/30/60/90 day observation period
- Sends **update reminders** for stale content (titles containing old years, articles untouched for 6+ months)

#### Competitor Content Monitor

Scans competitor websites weekly for:
- **New blog posts** — immediate notification when a competitor publishes
- **New docs, learning resources, changelogs, help center articles** (if they exist)
- **Rising articles** — when a competitor's article climbs in rankings, runs a 6-dimension deep analysis:
  1. Title strategy (length, keywords, emotional hooks)
  2. Content structure (headings, word count, FAQ sections, tables)
  3. Content depth (sub-topics covered vs your coverage = content gaps)
  4. Schema Markup (what structured data they use vs you)
  5. Backlink analysis (new links driving the rise)
  6. Estimated traffic trend

#### Monthly Report

Generates a **React interactive dashboard** with 5 tabs:

1. **Overview** — KPI cards with month-over-month comparison, alert timeline
2. **Keywords** — Sortable ranking table, trend charts, new keyword opportunities
3. **Content** — Performance heatmap, decay list, new article tracking, update queue
4. **Competitors** — New content timeline, rising article analyses, keyword battle map
5. **Action Plan** — Auto-generated prioritized recommendations with linked skill triggers

**Data sources:** SEMrush API, Google Search Console API, Google Analytics API (GA4).

📄 [Full documentation →](docs/seo-competitive-intel.md)

---

## Directory Structure

```
~/.openclaw/skills/                          (after installation)
├── aeo-content-strategy/
│   └── SKILL.md
├── seo-aeo-diagnostics/
│   ├── SKILL.md                             ← orchestrator
│   ├── technical-foundation/SKILL.md
│   ├── search-accessibility/SKILL.md
│   ├── structured-data/SKILL.md
│   ├── content-structure/SKILL.md
│   ├── multimedia-accessibility/SKILL.md
│   ├── content-quality-signals/SKILL.md
│   └── site-architecture/SKILL.md
└── seo-competitive-intel/
    ├── SKILL.md                             ← orchestrator
    ├── keyword-ranking/SKILL.md
    ├── content-performance/SKILL.md
    ├── competitor-content/SKILL.md
    └── monthly-report/SKILL.md
```

## Requirements

| Requirement | Required For | Notes |
|-------------|-------------|-------|
| [OpenClaw](https://openclaw.ai) | Everything | v0.1+ |
| SEMrush API key | `seo-competitive-intel` | [Get one here](https://www.semrush.com/api/) |
| Google Search Console access | `seo-competitive-intel` | OAuth via browser on first run |
| Google Analytics (GA4) access | `seo-competitive-intel` | OAuth via browser on first run |

`aeo-content-strategy` and `seo-aeo-diagnostics` work with no API keys — they use OpenClaw's built-in web browsing and fetching tools.

## Background: What is AEO?

**Answer Engine Optimization (AEO)** is the practice of optimizing content to be cited by AI-powered search platforms like ChatGPT, Perplexity, Google AI Overviews, and Claude.

Traditional SEO optimizes for ranking in a list of blue links. AEO optimizes for being the source an AI quotes in its answer. The key differences:

| | Traditional SEO | AEO |
|---|---|---|
| **Goal** | Rank #1 in search results | Be the source AI cites |
| **Keywords** | 2-3 word phrases | 25+ word conversational questions |
| **Measurement** | Position #1-10 | Share of voice across AI platforms |
| **Content format** | Keyword-optimized pages | Structured, quotable, fact-rich content |
| **Off-site signals** | Backlinks | Reddit presence, third-party reviews, knowledge graph consistency |

These skills were designed based on analysis of four leading SEO/AEO publications and encode their combined best practices into executable workflows.

## Contributing

Contributions welcome! Some areas that could use help:

- Additional diagnostic checks for the `seo-aeo-diagnostics` modules
- Support for more data sources beyond SEMrush (Ahrefs, Moz)
- Localization of skill descriptions for non-English markets
- Templates for specific verticals (e-commerce, SaaS, local business)

Please open an issue first to discuss what you'd like to change.

## License

[MIT](LICENSE)
