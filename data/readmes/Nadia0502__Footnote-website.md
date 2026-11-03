<div align="center">

# Footnote

**From reported earnings to economic earnings, with every number traced to its source.**

An AI-assisted analyst desk that reads a company's 10-K, finds the unusual items hidden in the MD&A, the cash flow statement and the notes, and turns reported profit into NOPAT, invested capital, ROIC against the cost of capital, economic earnings and a rule-based rating.

[Live demo](https://footnote-ecru.vercel.app/) · [Methodology](docs/decisions.md) · [Prompt log](docs/prompt-log.md)

</div>

---

## Why Footnote

Reported earnings mix the recurring business with one-off gains, restructuring charges, impairments, litigation and lease costs, and many of these items are disclosed only in the notes. Adjusting for them by hand is slow; letting a language model do it alone is fast but unreliable on ambiguous items.

Footnote combines the two. **The AI reads and proposes, deterministic code calculates, and the analyst validates.** The language model never produces a final number, and every decision is recorded.

## How it works

Footnote runs one guided workflow per company and fiscal year. Each step has a validation point where the analyst accepts, modifies or rejects what was proposed.

| # | Step | AI | Code | Analyst |
|---|------|----|------|---------|
| 1 | **Read** | — | Finds the company and its 10-K filings on SEC EDGAR, downloads the filing and its XBRL data, splits it into sections with page numbers, screens the company type | Confirms the filing and fiscal year |
| 2 | **Extract** | Proposes unusual items with amount, unit, section, page and the exact quote | Converts units and verifies every quote against the filing | Accepts, edits, rejects or adds items |
| 3 | **Classify** | Proposes operating / non-operating and recurring / non-recurring, with a confidence score and rationale | Sends uncertain items to a *To decide* queue | Resolves the queue |
| 4 | **Calculate** | Proposes a side for balance-sheet lines no rule can read | Reformulates the statements; computes NOPAT, net operating assets, ROIC, WACC and economic earnings | Checks adjustments and cost-of-capital assumptions |
| 5 | **Compare** | — | Applies the same calculations to industry peers | Picks or excludes peers |
| 6 | **Check** | — | Runs consistency checks: tie-outs, signs, units, sources, taxes, year-on-year moves | Confirms or corrects each warning |
| 7 | **Report** | — | Computes the rating and builds a report where every figure links to its source | Signs off before export |

## Key features

- **Source for every number.** Each item carries its filing, section, page and verbatim quote; a quote that cannot be found in the filing is flagged *unverified*.
- **Append-only validation journal.** Every proposal and decision is logged with its reason. Undo, revert and reset create new entries; nothing is overwritten.
- **Transparent methodology.** Tax-shield NOPAT (top-down equals bottom-up), lease treatment by accounting regime (capitalised before ASC 842, already on the balance sheet after it), operating/financing reformulation with a tie-out check.
- **Rule-based business-strength rating.** Two criteria graded 1 to 5: *quality of earnings* (level and trend of economic earnings against reported EPS) and *ROIC by quintile* among US companies. No AI in the rating; every rule, threshold and figure is shown.
- **Analysis confidence.** A separate indicator of how much of the result rests on the analyst's own decisions. It never changes the rating.
- **Built-in evaluation.** AI proposals are compared with hand-checked reference sets, and each prompt version is logged with its results.

## Tech stack

| Area | Choice |
|------|--------|
| Framework | Next.js (App Router), React, TypeScript, Tailwind CSS |
| Language models | Qwen through Scaleway Generative APIs (primary), Google Gemini Flash (fallback); structured JSON output validated with zod |
| Data | SEC EDGAR (filings, XBRL company facts and frames), FRED (10-year Treasury), Damodaran datasets (equity risk premium, industry betas) |
| Tests | Vitest — every financial formula is unit-tested against reference figures computed by hand from the 10-K |
| Hosting | Vercel |

All API calls run server-side; no key ever reaches the browser. Only public filing text is sent to a language model.

## Getting started

Requires **Node.js 22+**.

```bash
npm install
cp .env.local.example .env.local   # then fill in the variables below
npm run dev                        # http://localhost:3000
```

| Variable | Purpose | Required |
|----------|---------|----------|
| `SEC_USER_AGENT` | Identifies the app to SEC EDGAR, e.g. `Footnote research (you@example.com)` | Yes |
| `SCALEWAY_API_KEY`, `SCALEWAY_BASE_URL`, `SCALEWAY_MODEL` | Primary language model (extraction, classification, explanations) | For AI steps |
| `GEMINI_API_KEY`, `GEMINI_MODEL` | Fallback language model | Optional |
| `FRED_API_KEY` | 10-year Treasury rate (series `DGS10`) | Recommended |

Without model keys the desk still runs and shows *provider not configured*; the demo runs on the Evaluate page work without any model call.

### Useful scripts

```bash
npm test                   # unit tests
npm run build              # production build
npm run lint               # lint
npm run benchmark:mapping  # statement-mapping benchmark (docs/mapping-benchmark.md)
npm run data:quintiles     # rebuild the ROIC quintile snapshots (local, SEC rate-limited)
```

## Project structure

```
app/            pages (landing, desk, evaluate, methodology, report) and server API routes
components/     desk steps, report, landing
lib/            pure, tested logic: SEC client, filing parser, AI layer, finance, checks, rating
data/           market snapshots (FRED, Damodaran, ROIC quintiles), demo runs, test-set template
docs/           accounting decisions, prompt log, mapping benchmark
scripts/        local data and benchmark scripts
test/           fixtures built from public SEC filings
```

## Limitations

Footnote is a prototype. It reads US 10-K filings of operating companies; banks, insurers and REITs are flagged. Model answers can vary between runs, so every AI proposal stays a proposal until the analyst confirms it. The rating covers business strength only: there is no market data and no valuation. See [docs/decisions.md](docs/decisions.md) for the documented choices and their limits.

## Disclaimer

For educational purposes only. Not investment advice.

---

© 2026 the Footnote authors. All rights reserved. Shared for viewing only.
