# AEO Radar

[English](README.md) · [繁體中文](README.zh-TW.md)

[![CI](https://github.com/hellowalt/aeo-radar/actions/workflows/ci.yml/badge.svg)](https://github.com/hellowalt/aeo-radar/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE)
[![Node.js](https://img.shields.io/badge/node-%E2%89%A520-black.svg)](https://nodejs.org)
[![TypeScript](https://img.shields.io/badge/typescript-5-black.svg)](https://www.typescriptlang.org/)
[![Next.js](https://img.shields.io/badge/next.js-16-black.svg)](https://nextjs.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-black.svg)](CONTRIBUTING.md)

> Open-source **Answer Engine Optimization** monitor. Track how often your brand shows up in AI answers, where you rank, and which competitors are beating you.

**Why this exists**: search is moving from ten blue links to one AI-generated answer. If your brand isn't cited in that answer, you're invisible — no matter how good your SEO is. AEO Radar scrapes AI answer engines on your keywords every day and turns the raw responses into a dashboard you can actually act on.

Default target: **ChatGPT**. The architecture lets you plug in additional engines (Gemini, Perplexity, Claude) by subclassing a single base crawler — see [Adding a platform](#adding-a-platform).

![Dashboard](docs/screenshot.png)

<details>
<summary>More screenshots — Query Results · Keyword manager</summary>

### Query Results — every AI answer, with brand mention / rank / sentiment

![Query Results](docs/screenshot-query.png)

### Keyword & Prompt management

![Keywords and prompts](docs/screenshot-keywords.png)

</details>

---

## ⚠️ Disclaimer — read before using

AEO Radar automates interactions with third-party AI services (ChatGPT by default). Before you run it:

- **Third-party Terms of Service.** Automating ChatGPT, Gemini, Perplexity, or Claude web interfaces may violate the provider's ToS. You are responsible for reviewing and complying with the terms of any service you target.
- **Account risk.** Scraped accounts can be suspended or banned at the provider's discretion. **Use a dedicated account, never your primary one.**
- **Not affiliated.** This project is independent and not affiliated with, endorsed by, or sponsored by OpenAI, Google, Anthropic, Perplexity, or any AI service provider. Product names are trademarks of their respective owners.
- **Rate limits.** Run the default daily schedule or lower. Bursting more queries can trigger anti-abuse systems and impact other users.
- **Data you scrape.** AI responses may contain third-party content. You're responsible for how you store, redistribute, or publish any output.
- **No warranty.** Provided "as is" under the [MIT License](LICENSE). Use at your own risk.

If any of the above is a hard no for your context (enterprise, regulated industry, risk-averse legal review), **use an API-based AEO tool instead**.

---

## What you get

- **Daily headless crawl** — Playwright + stealth plugin, no API keys, no cost per query.
- **LLM-powered analysis** — each answer is parsed for brand mention, ranking position, sentiment, competitors, and cited domains/URLs.
- **Minimal dark dashboard** — Next.js + Ant Design + Recharts on a grayscale-only theme. KPI cards, trend lines, competitor tables, raw query results with screenshots.
- **Single config file** — point it at your brand, your keywords, your market, and the whole pipeline follows.
- **SQLite by default** — zero-setup storage. Swap to Postgres by editing one Prisma datasource.

---

## How it works

```
┌────────────────┐     ┌────────────────┐     ┌────────────────┐     ┌──────────────────┐
│ brand.ts       │ ──▶ │  Claude CLI    │ ──▶ │ Playwright     │ ──▶ │ Claude CLI       │
│ (your config)  │     │  generates     │     │ scrapes AI     │     │ analyzes the     │
│                │     │  4 prompts per │     │ answer engine  │     │ answer → JSON    │
│                │     │  keyword       │     │ (headless)     │     │                  │
└────────────────┘     └────────────────┘     └────────────────┘     └──────────────────┘
                                                                                │
                                                                                ▼
                                                                     ┌──────────────────┐
                                                                     │ SQLite           │
                                                                     │ (5 tables)       │
                                                                     └──────────────────┘
                                                                                │
                                                                                ▼
                                                                     ┌──────────────────┐
                                                                     │ Next.js          │
                                                                     │ Dashboard        │
                                                                     └──────────────────┘
```

**Four intent prompts per keyword**: each keyword ("project management software") expands into recommendation / comparison / tutorial / procurement variants — so you see visibility across the whole funnel, not just "top picks" queries.

**Analysis fields per answer**: `brand_mentioned`, `brand_rank`, `brand_description`, `sentiment`, `sentiment_score`, `competitors[]`, `referenced_domains[]`, `referenced_urls[]`, `total_recommendations`.

---

## Prerequisites

- **Node.js 20+** and **npm**
- **Playwright** will install its bundled Chromium on first run
- **Claude CLI** on `$PATH` — used for prompt generation and answer analysis. Install from [claude.com/claude-code](https://www.claude.com/claude-code).

---

## Quick start

```bash
# 1. Clone & install
git clone https://github.com/hellowalt/aeo-radar.git
cd aeo-radar
npm install
cd web && npm install && cd ..
npx playwright install chromium

# 2. Configure your brand
#    Edit src/config/brand.ts — set name, description, target market, keywords.
$EDITOR src/config/brand.ts

# 3. Create the SQLite database
npm run db:push

# 4. Generate prompts from your keywords (uses Claude CLI)
npm run seed

# 5. Run your first crawl (headless, ~60s per prompt on ChatGPT)
npm run crawl

# 6. Launch the dashboard
npm run dashboard
# open http://localhost:3003
```

### Want to see the dashboard with data before you commit to a crawl?

```bash
npm run db:push
npm run demo:reset     # wipes + seeds 14 days of synthetic demo data
npm run dashboard
```

The demo seeder (`scripts/seed-demo.ts`) fabricates a fictional "DinoEgg" dinosaur-egg toy brand with realistic trends — great for screenshots, videos, or showing the tool to a teammate. It doesn't touch `brand.ts` or call any AI service.

---

## Configuring your brand

Everything that is brand-specific lives in **one file**: `src/config/brand.ts`.

```ts
export const brand: BrandConfig = {
  name: 'Acme',
  description: 'a project management SaaS for small remote teams',
  targetMarket: 'English-speaking SMB owners in North America',
  keywords: [
    { keyword: 'project management software', category: 'Product' },
    { keyword: 'remote team collaboration tool', category: 'Product' },
    { keyword: 'task tracking for distributed teams', category: 'Service' },
    { keyword: 'agile planning tool for startups', category: 'Service' },
  ],
};
```

- `name` — the string the analyzer matches against in AI answers.
- `description` — injected into prompt-generation so the LLM understands your product.
- `targetMarket` — drives prompt language/style (the LLM follows your market hint).
- `keywords` — 4–10 seed keywords is a sweet spot. Too many = hours per crawl.

After editing, re-run `npm run seed` to regenerate prompts. Existing keywords are kept; only missing ones are added.

---

## CLI reference

```bash
npm run crawl                  # run ChatGPT crawl on all active prompts
npm run crawl -- --visible     # show the browser window (debugging)
npm run analyze <runId>        # re-analyze a past run (after editing analysis-template.md)
npm run seed                   # generate prompts for keywords in brand.ts
npm run db:push                # sync Prisma schema → SQLite
npm run dashboard              # start the Next.js dashboard on :3003
```

---

## Scheduling a daily crawl

**macOS (launchd)** — a ready-made example lives in `scripts/daily-crawl.sh`. Wire it up with a plist under `~/Library/LaunchAgents/`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>com.aeo-radar.daily</string>
  <key>ProgramArguments</key>
  <array>
    <string>/bin/bash</string>
    <string>/ABSOLUTE/PATH/TO/aeo-radar/scripts/daily-crawl.sh</string>
  </array>
  <key>StartCalendarInterval</key>
  <dict><key>Hour</key><integer>11</integer><key>Minute</key><integer>0</integer></dict>
  <key>StandardOutPath</key><string>/Users/YOURNAME/Library/Logs/aeo-radar/aeo-crawl.log</string>
  <key>StandardErrorPath</key><string>/Users/YOURNAME/Library/Logs/aeo-radar/aeo-crawl-error.log</string>
</dict></plist>
```

> ⚠️ macOS TCC blocks `launchd` from writing logs inside `~/Desktop/`. Keep the log directory outside `~/Desktop/` (e.g. `~/Library/Logs/aeo-radar/`).

**Linux (cron)**:

```
0 11 * * * /ABSOLUTE/PATH/TO/aeo-radar/scripts/daily-crawl.sh >> /var/log/aeo-radar.log 2>&1
```

---

## Adding a platform

ChatGPT is the default. Adding another AI answer engine is ~60 lines:

1. Create `src/crawlers/<name>.ts` that extends `BaseCrawler`.
2. Implement `async crawl(prompt, runId, resultId)`. See `chatgpt.ts` for the pattern.
3. Add the name to `LLM_PLATFORMS` in `src/types.ts`.
4. Register the class in the `createCrawler` switch in `src/pipeline/runner.ts`.

Tips from production:
- Some engines (e.g. Gemini) fingerprint Chrome-for-Testing as a bot and silently drop submissions. Override `launchChannel` to `'chrome'` in your subclass to route through the user's real Chrome install.
- Anti-bot challenges (Cloudflare, reCAPTCHA) are handled automatically for 120s of manual solve time in non-headless mode — see `BaseCrawler.waitForChallengeIfNeeded`.

---

## Project structure

```
aeo-radar/
├── src/
│   ├── cli.ts                 # Entry: run / analyze / seed
│   ├── types.ts               # Platform enum + shared types
│   ├── config/brand.ts        # ← your brand / keywords / market
│   ├── crawlers/
│   │   ├── base.ts            # Stealth, challenge detection, persistent profile
│   │   └── chatgpt.ts
│   ├── pipeline/
│   │   ├── runner.ts          # Orchestrates prompts × platforms
│   │   └── analyzer.ts        # Claude CLI → structured analysis
│   ├── prompts/generator.ts   # Seeds prompts from brand.ts
│   └── db/prisma.ts           # Prisma singleton
├── prompts/
│   ├── generator-template.md  # Prompt fed to Claude for prompt generation
│   └── analysis-template.md   # Prompt fed to Claude for answer analysis
├── prisma/schema.prisma       # 5 models — keywords, prompts, runs, results, analysis
├── scripts/
│   ├── daily-crawl.sh         # Network probe + crawl loop
│   └── backfill-urls.ts       # Re-extract URLs from past answers
├── web/                       # Next.js 16 dashboard (port 3003)
│   └── src/
│       ├── app/               # Pages + 13 API routes
│       ├── components/        # KPI, tables, charts, settings
│       └── lib/theme.ts       # Grayscale design tokens
└── data/
    └── aeo.db                 # SQLite (gitignored)
```

---

## Database schema (5 tables)

| Model | Purpose |
|---|---|
| `AeoKeyword` | Seed keywords from `brand.ts` |
| `AeoPrompt` | 4 intent-specific prompts per keyword |
| `AeoCrawlRun` | One row per `npm run crawl` invocation |
| `AeoResult` | Raw AI response + screenshot, per prompt × platform |
| `AeoAnalysis` | LLM-extracted brand rank, sentiment, competitors, cited URLs |

See `prisma/schema.prisma` for field-level detail.

---

## FAQ

**Does this cost API money?** No — the crawler drives the ChatGPT web UI (free tier is enough for a few dozen prompts/day). Analysis uses the Claude CLI, which is bundled with your Claude plan.

**Will my ChatGPT account get banned?** The crawler uses a persistent browser profile and stealth plugin, and only fires a few queries per day. We haven't seen a ban in production use, but there's no guarantee — use a dedicated account if you're nervous.

**How many keywords should I track?** 4–10 is ideal. Each keyword becomes 4 prompts, so 10 keywords = 40 prompts ≈ 40 minutes per daily run on ChatGPT.

**Can I monitor multiple brands?** Not out of the box — `brand.ts` is a single config. Fork the repo or swap it at runtime via env var if you need multi-tenant.

**Why only ChatGPT by default?** Keeping the OSS release focused. ChatGPT is the dominant AI answer engine; every other engine adds bot-detection headaches. The architecture makes adding Gemini / Perplexity / Claude straightforward — see [Adding a platform](#adding-a-platform).

---

## Alternatives

A few paid AEO / GEO tracking platforms in the same space, for context:

| Tool | Approach | Notable trade-off |
|---|---|---|
| **AEO Radar** (this project) | Self-hosted, web-UI scraping via Playwright | You run it; no SaaS fee; ToS gray zone |
| [Otterly AI](https://otterly.ai) | Paid SaaS, uses providers' APIs | API results diverge from real UI output ([their own blog](https://otterly.ai/blog/ui-api-chatgpt-perplexity/)) |
| [Peec AI](https://peec.ai) | Paid SaaS, "UI scraping as a service" | Doesn't disclose how it beats Cloudflare, so it's a black box |
| [Profound](https://www.tryprofound.com) | Paid SaaS, real-user panel data | Only works at scale; needs a panel partner |
| [ZipTie](https://ziptie.dev) | Paid SaaS, marketing-team focus | Closed source; no raw data export |

If you want a managed service and don't want to think about infra, pay them. If you want the raw data on your own machine and can stomach the [ToS caveats](#%EF%B8%8F-disclaimer--read-before-using), use this.

---

## Roadmap

What's on the table for future releases. Vote / suggest via [GitHub Discussions](https://github.com/hellowalt/aeo-radar/discussions).

- [ ] **Gemini crawler in `main`** — code path already exists in `BaseCrawler`; waiting for a stable selector set
- [ ] **GitHub Actions scheduled crawl** — run daily in CI without a local machine
- [ ] **Postgres adapter** — one-line Prisma swap, documented end-to-end
- [ ] **Multi-brand monitoring** — runtime brand config, one DB, N brands
- [ ] **Slack / Discord alerts** — notify when mention rate drops or a new competitor appears
- [ ] **Weekly markdown report export** — feed into your team's internal Wiki / Notion / LLM context

---

## Background reading

Three short write-ups in [`docs/decisions/`](docs/decisions/) record dead ends so you don't repeat them:

- [`0001-platform-scope.md`](docs/decisions/0001-platform-scope.md) — what breaks on Perplexity, Claude, Google AI Overview, and Gemini.
- [`0002-scheduling-on-macos.md`](docs/decisions/0002-scheduling-on-macos.md) — the macOS TCC trap that makes `launchd` silently fail.
- [`0003-citation-url-extraction.md`](docs/decisions/0003-citation-url-extraction.md) — why `referenced_urls` is usually empty for anonymous ChatGPT.

---

## Contributing

PRs welcome. A few guardrails:

- **No brand-specific content** in `main`. Your fork's `brand.ts` should stay in your fork.
- **Keep the grayscale theme**. If you need an accent color, propose it in an issue first.
- **Every new platform** ships with a selector-stability note in the PR description — AI engine DOMs shift constantly.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full contributor guide and [CLAUDE.md](CLAUDE.md) for the development playbook. Security issues: [SECURITY.md](SECURITY.md).

## Community

- **Questions / ideas** — [GitHub Discussions](../../discussions) (enable on your repo settings).
- **Bugs** — [open an issue](../../issues/new/choose).

---

## License

[MIT](LICENSE) — do what you want, credit appreciated.
