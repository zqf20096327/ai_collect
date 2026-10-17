# pseo-ai-kit

> Programmatic SEO starter for AI apps. Next.js 15 + Vercel + LLM content generator + sitemap / JSON-LD / internal-link graph — built by an operator of 43+ pSEO sites.

[![npm version](https://img.shields.io/npm/v/@swarmclawai/pseo-ai-kit.svg)](https://www.npmjs.com/package/@swarmclawai/pseo-ai-kit)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![CI](https://github.com/swarmclawai/pseo-ai-kit/actions/workflows/ci.yml/badge.svg)](https://github.com/swarmclawai/pseo-ai-kit/actions/workflows/ci.yml)

## Why this exists

Every indie operator doing pSEO + LLMs right now is rebuilding the same plumbing in private:

- Keyword list → LLM → typed content
- Canonical tags, sitemap, robots.txt, JSON-LD
- An internal-link graph that isn't just a hub-and-spoke disaster
- A validator that catches duplicate slugs and thin content *before* Google does
- A content-data layer that survives edits and redeploys

The space is dominated by closed-source courses and Twitter threads. `pseo-ai-kit` is a single open-source scaffold that gives you the whole stack — shipped by someone running 43+ pSEO sites on Vercel Pro.

## 30-second demo

```bash
# Scaffold a new pSEO site
npx -p @swarmclawai/pseo-ai-kit create-pseo-ai my-site --template directory
cd my-site
pnpm install

# Drop your keywords into keywords.txt (one per line)
echo "best project management software for remote teams" >> keywords.txt

# Plan, then LLM-generate pages
pnpm run keywords
export ANTHROPIC_API_KEY=sk-...
pnpm run generate:incremental

# Sanity-check the output (duplicate slugs, thin content, missing related keywords, etc.)
pnpm run validate
pnpm run graph:svg

# Ship
pnpm run dev            # → http://localhost:3000
pnpm run deploy:preflight
pseo-ai deploy --prod
```

> The package ships two bins (`pseo-ai` and `create-pseo-ai`), so `npx` needs `-p <pkg> <bin>` to disambiguate. Inside a scaffolded site the `pnpm run` scripts call `pseo-ai` directly — so you only use the long form once.

## What you get

A scaffolded Next.js 15 App Router site with:

- **Typed content data layer** — every generated page goes through a Zod schema; frontmatter + markdown body round-trip through `gray-matter`
- **LLM content generator** — `generate.ts` calls Claude Haiku by default, parses strict JSON, and writes one page per keyword with bounded concurrency
- **Keyword planning workflow** — txt/CSV import, dedupe, deterministic clusters, related-keyword mappings, and incremental generation cache
- **SEO essentials** — canonical tags, sitemap (`/sitemap.xml`), robots, OG + Twitter meta, `Article` + `FAQPage` JSON-LD
- **Internal link graph** — `buildLinkGraph` connects pages by keyword overlap, renders related pages, and can export `graph.svg`
- **Validator + doctor** — catches duplicate slugs/titles/descriptions, title/description drift, thin content, graph orphans, missing setup, and deploy blockers
- **Vercel preflight** — `pseo-ai deploy --preflight-only` runs setup checks, validation, and the site build before invoking Vercel

## Commands

| Command | Purpose |
|---|---|
| `pseo-ai init [dir] --template <directory\|blog\|comparison>` | Scaffold a Next.js pSEO site |
| `pseo-ai keywords <keywords.txt>` | Clean, dedupe, cluster, and write `keywords.plan.json` |
| `pseo-ai generate [keywords.txt] --plan keywords.plan.json --incremental` | LLM-generate pages from a keyword file or plan |
| `pseo-ai validate` | Static SEO checks across all pages |
| `pseo-ai graph --svg graph.svg` | Print/export the internal-link graph |
| `pseo-ai doctor` | Check local setup, package scripts, content dir, and env readiness |
| `pseo-ai deploy --provider vercel --preflight-only` | Run Vercel-oriented deploy preflight; omit `--preflight-only` to invoke `vercel deploy` |
| `pseo-ai help-agents` | Machine-readable CLI catalog |
| `create-pseo-ai <dir>` | Standalone scaffolder bin (same as `pseo-ai init`) |

Every command accepts `--json` and returns a one-line JSON envelope. Exit codes: `0` success, `1` user error, `2` internal error.

## Page schema

Every generated page matches this shape — Zod-validated at generation and on read:

```ts
{
  slug: string,            // kebab-case, URL-safe, unique
  title: string,           // 30-60 chars for SERP display
  metaDescription: string, // 120-155 chars
  h1: string,
  intro: string,           // 60-120 words
  sections: [{ heading: string, body: string }],  // 2-10
  keyword: string,
  topicCluster?: string,
  relatedKeywords: string[],
  faqs: [{ q: string, a: string }],
}
```

You can hand-edit the generated `*.md` files. The generator respects existing slugs (won't clobber them) and the Next.js app re-reads content on every build.

## Keyword plans

`pseo-ai keywords keywords.txt --out keywords.plan.json` creates a deterministic plan with cleaned keywords, topic clusters, related-keyword mappings, and a source hash. `pseo-ai generate --plan keywords.plan.json --incremental` uses that plan and skips pages whose generation inputs and existing markdown file have not changed.

CSV input is supported with `--format csv --keyword-column keyword`.

## Providers

The default generator uses Anthropic's Claude Haiku for cost. The `ContentClient` interface is one method (`generatePage`), so dropping in OpenAI, a local model via Ollama, or a custom pipeline is trivial:

```ts
import { generatePages } from "@swarmclawai/pseo-ai-kit";

await generatePages({
  site,
  keywords,
  client: {
    async generatePage({ site, keyword, relatedKeywords, existingSlugs }) {
      // ...call your own model...
      return pageSchema.parse(result);
    },
  },
});
```

The library also exports `createKeywordPlan`, `keywordPlanSchema`, `buildGraphSvg`, `generationCacheSchema`, and cache hashing helpers for custom pipelines.

Next.js templates import page-runtime helpers from `@swarmclawai/pseo-ai-kit/runtime` so generator-only dependencies stay out of the app build.

## How it compares

| | **pseo-ai-kit** | Astro starters | Contentlayer-based templates | Vercel templates |
|---|---|---|---|---|
| pSEO-focused content pipeline | ✅ | ❌ | ❌ | ❌ |
| LLM generator built-in | ✅ | ❌ | ❌ | partial |
| JSON-LD + FAQPage schema | ✅ | ❌ | ❌ | ❌ |
| Internal-link graph generator | ✅ | ❌ | ❌ | ❌ |
| Validator for SEO fundamentals | ✅ | ❌ | ❌ | ❌ |
| Agent-driven CLI | ✅ | — | — | — |

## Built for coding agents

Every swarmclawai CLI follows the same agent conventions so Claude Code, Cursor, Cline, Aider, Codex et al can drive them without guessing:

- `--json` everywhere, one-line envelope on stdout
- Stderr for logs, stdout for data
- Stable exit codes: `0` / `1` / `2`
- Non-interactive by default
- `pseo-ai help-agents` returns the entire command catalog as JSON

See [`AGENTS.md`](./AGENTS.md) for the full machine-readable reference.

## Roadmap

- Optional BYOK keyword-volume enrichment
- Built-in Lighthouse budget assertions
- More example campaigns and template overlays

## Contributing

See [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## License

[MIT](./LICENSE)
