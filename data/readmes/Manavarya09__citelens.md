<div align="center">

# Citelens

**The open-source SEO + GEO suite. See how Google and AI both talk about you — and what to do about it.**

Self-hosted. Two pillars under one dashboard: classic SEO (site audit, keywords,
rank tracking) and GEO (how ChatGPT, Claude, Perplexity, Gemini and Google AI
Overviews cite your brand vs. competitors) — then the exact fix to improve both.

</div>

---

## See it

Real data: how AI engines talk about your brand — visibility, share of voice vs.
competitors, and per-engine breakdown.

![Citelens dashboard](docs/screenshots/dashboard.png)

## Why

Search is splitting in two. Half your visibility is still classic Google
rankings; the other half is now whether AI answers even mention you. The tools
that cover the AI half (Profound, Otterly, Peec) cost $70-$500/mo, are closed,
and stop at a dashboard. The tools that cover the classic half (Ahrefs, Semrush)
cost the same and don't touch AI at all. Nobody does both, open, in one place.

The open-source options are CLI/JSON dumps with no UI.

Citelens is the one that's open, beautiful, and covers both halves - and it
closes the loop: it doesn't just say "you're invisible for this query," it tells
you why (who ranked or got cited instead, from what source) and drafts the fix.

## What it does

**GEO pillar** (ships first)
- Track real AI answers across ChatGPT, Claude, Perplexity, Gemini, and Google AI Overviews
- Share of voice - how often you're cited vs. named competitors
- Sentiment - is the AI recommending you, or warning people off?
- Action loop - for every query where you're invisible, diagnose the gap and draft the fix

**SEO pillar** (crawler + audit shipping now)
- Site crawler and technical/on-page audit - broken pages, titles, meta
  descriptions, H1s, thin content, canonicals, alt text → a 0-100 health score
- Keyword research and rank tracking (layer on via external data API)
- Backlinks via your choice of external data API (no native link index - see the plan for why)

**Both**
- Two answer mechanisms: provider APIs by default, optional scraping adapter for real-UI fidelity
- Self-hosted, your API keys, your data - no subscription, no sales call

## Status

Early development - `v0.0.1` (GEO core) is working: create a project, auto-generate
buyer-intent prompts, run them against Gemini, and see your visibility, share of
voice vs. competitors, and the sources the AI cited. The **SEO pillar's crawler +
on-page/technical audit** also works now (the "SEO audit" tab, or
`/citelens:seo` from the plugin); keyword/rank/backlink modules need external
data APIs and layer on next. Star to follow along.

See [`docs/IMPLEMENTATION_PLAN.md`](docs/IMPLEMENTATION_PLAN.md) for the full roadmap.

## Quick start

```bash
git clone https://github.com/Manavarya09/citelens.git
cd citelens
npm install
npm run db:migrate        # create the local SQLite database
npm run dev               # http://localhost:3000
```

Or launch it in one command (build + migrate + start):

```bash
node bin/citelens.mjs     # → http://localhost:3000   (published as `npx citelens`)
```

That's it - no API key required to try it. With no key, Citelens uses a
deterministic mock engine so the whole loop works offline.

For **live** answers with real citations, add a free Gemini key:

```bash
cp .env.example .env
# then set GEMINI_API_KEY (free from https://aistudio.google.com/apikey)
```

### No API keys? Use free browser mode

Don't want to deal with API keys or spend money? Set `CITELENS_BROWSER=1` and
Citelens drives the **real web UIs** in a browser on your machine instead:

- **Perplexity** and **Google AI Overview** work with no login.
- **ChatGPT** and **Gemini** need a one-time login — open **Browser mode** in the
  app, click *Open & log in*, sign in once (the session is saved on disk), then
  run your project.

Browser mode is experimental and opt-in: it automates your own browser, so it's
slower and more fragile than the API path (sites change their markup and may
challenge automated access), and it's subject to each site's terms of use. The
API path always works without it.

A single run hits **all four engines** — Gemini, Claude, ChatGPT, and
Perplexity — and each one runs live if its key is set (see `.env.example`),
otherwise it falls back to the mock. Gemini is the recommended starting point
because it's free and its Google Search grounding returns real cited sources.
The dashboard breaks down visibility per engine, share of voice vs. competitors,
sentiment toward your brand, where citations come from, and the run's cost.

## Use it inside Claude Code (plugin)

Citelens ships as a [Claude Code](https://claude.com/claude-code) plugin, so you
can run a GEO check without leaving your terminal:

```
/plugin marketplace add Manavarya09/citelens
/plugin install citelens
```

Then:

- `/citelens:check <brand>` - run the live GEO pipeline (prompt-gen → engines →
  parse → metrics) and print a visibility + share-of-voice report. Works offline
  on the mock; set `GEMINI_API_KEY` for real data.
- `/citelens:seo <url>` - crawl a site and run the technical/on-page SEO audit
  (the same crawler → audit → score pipeline as the dashboard's SEO tab).
- `/citelens:setup` - scaffold `.env`, migrate, and launch the dashboard.
- Ask anything about GEO and the `citelens-geo` knowledge skill explains the
  methodology.

The check and audit commands run `scripts/geo-check.ts` and `scripts/seo-audit.ts`
- the same pipelines as the web app, standalone with no database.

## Docker

```bash
docker build -t citelens .
docker run -p 3000:3000 -v citelens-data:/data -e GEMINI_API_KEY=your-key citelens
```

## Tests

```bash
npm test   # vitest — core GEO logic (answer parser, metrics, gap detection, mock)
```

## License

MIT
