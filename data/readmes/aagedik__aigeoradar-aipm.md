# AI Page Manifest (AIPM)

**Open specification for per-page `.ai.json` — machine-readable page metadata for AI crawlers, RAG systems, and GEO (Generative Engine Optimization).**

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Spec hub](https://img.shields.io/badge/spec-aigeoradar.com-indigo)](https://aigeoradar.com/specifications/aipm)
[![Schema 1.2](https://img.shields.io/badge/JSON%20Schema-1.2.0-blue)](https://aigeoradar.com/schemas/aipm/1.2/page-manifest.schema.json)
[![GitHub](https://img.shields.io/badge/github-aagedik%2Faigeoradar--aipm-black)](https://github.com/aagedik/aigeoradar-aipm)

**Search / discover this project as:** `AIPM` · `AI Page Manifest` · `.ai.json` · `GEO` · `llms.txt companion` · `AI discovery sidecar`

Maintained by [AigeoRadar](https://aigeoradar.com) as part of the **AI Discovery Framework (ADF)**.

---

## Why AIPM exists

HTML is for humans. Classic SEO (titles, sitemaps, JSON-LD) helps search engines. **AI answer engines** still often guess from messy page HTML — wrong price, wrong product, missing brand.

AIPM gives each page a small, trusted **sidecar JSON** next to the human URL:

```
https://example.com/blog/my-post          ← human HTML
https://example.com/blog/my-post.ai.json  ← AI Page Manifest (AIPM)
```

Crawlers and tools can fetch facts (`purpose`, `abstract`, `keyFacts`, topic, language) **without** parsing the full document.

| Approach | Role |
|----------|------|
| SEO / JSON-LD | Search engines & rich results |
| `llms.txt` / `entity.json` | Site-level AI guide & identity |
| **AIPM `.ai.json`** | **Per-page** facts for AI systems |

AIPM does **not** replace SEO or `llms.txt`. It completes the stack: site guide → entity → **page manifest**.

---

## How it fits AI Discovery (ADF)

Recommended read order for AI systems:

1. [`/llms.txt`](https://aigeoradar.com/llms.txt) — site guide  
2. [`/entity.json`](https://aigeoradar.com/entity.json) — who the brand is  
3. **`{page}.ai.json` (AIPM)** — what *this* page is about  
4. [`/ai-feed.xml`](https://aigeoradar.com/ai-feed.xml) — capabilities / updates  

Related open project: [AI Crawler Registry (ACR)](https://github.com/aagedik/aigeoradar-acr) — crawler identities for `robots.txt` policy.

---

## Mini example

```json
{
  "$schema": "https://aigeoradar.com/schemas/aipm/1.2/page-manifest.schema.json",
  "specification": {
    "name": "AI Page Manifest",
    "shortName": "AIPM",
    "version": "1.2.0",
    "rfc": "AIPM-002"
  },
  "manifestType": "page",
  "url": "https://example.com/pricing",
  "title": "Pricing",
  "purpose": "Explain plans and prices for buyers comparing GEO tools.",
  "abstract": "Transparent pricing for Starter, Pro, and Agency.",
  "primaryTopic": "pricing",
  "keyFacts": [
    "Starter includes WordPress Connector sync",
    "No credit card required for the free scan"
  ]
}
```

Full live examples: [`examples/`](./examples/) · production: [https://aigeoradar.com/pricing.ai.json](https://aigeoradar.com/pricing.ai.json)

---

## Adopt in 5 minutes

1. Copy [schema/1.2/page-manifest.schema.json](./schema/1.2/page-manifest.schema.json) (or validate against the live schema URL).  
2. Publish a sidecar: `/your-page.ai.json` next to `/your-page`.  
3. Add a discovery link in HTML `<head>`:

```html
<link rel="alternate"
      type="application/json"
      href="/your-page.ai.json"
      title="AI Page Manifest (AIPM) v1.2.0">
```

4. Optional: tell agents in `llms.txt` that per-page manifests use the `.ai.json` convention.  
5. Details: [docs/discovery-link.md](./docs/discovery-link.md) · [BEST_PRACTICES.md](./BEST_PRACTICES.md)

**WordPress:** one-click via [AigeoRadar Connector](https://aigeoradar.com/help/wordpress-plugin-setup) (virtual sidecars, no files on disk).  
**Custom PHP / other stacks:** generate JSON from your CMS/DB and serve at `{path}.ai.json` (Apache/Nginx rewrite or front controller). Spec stays the same.

---

## Current version

| Field | Value |
|-------|-------|
| **Version** | 1.2.0 |
| **RFC** | [AIPM-002](./rfcs/AIPM-002.md) |
| **Status** | Stable |
| **JSON Schema** | https://aigeoradar.com/schemas/aipm/1.2/page-manifest.schema.json |
| **Spec hub** | https://aigeoradar.com/specifications/aipm |
| **This repo** | https://github.com/aagedik/aigeoradar-aipm |

---

## Repository contents

```
README.md     You are here — overview & adoption
llms.txt      Production discovery URL seed (crawler beacon)
entity.json   Pointer to live entity graph
schema/1.1/   JSON Schema (legacy)
schema/1.2/   JSON Schema (current)
examples/     Live manifests from aigeoradar.com
rfcs/         RFC AIPM-001, AIPM-002
docs/         Discovery link & WordPress notes
```

---

## Production discovery (canonical)

Crawlers that seed from GitHub should prefer **live** URLs:

| File | Canonical URL |
|------|----------------|
| [llms.txt](./llms.txt) | https://aigeoradar.com/llms.txt |
| well-known | https://aigeoradar.com/.well-known/llms.txt |
| [entity.json](./entity.json) | https://aigeoradar.com/entity.json |
| AI feed | https://aigeoradar.com/ai-feed.xml |
| AI sitemap | https://aigeoradar.com/sitemap-ai.xml |
| AIPM schema | https://aigeoradar.com/schemas/aipm/1.2/page-manifest.schema.json |

---

## Quick start (spec readers)

1. [SPECIFICATION.md](./SPECIFICATION.md)  
2. Validate against [schema/1.2/page-manifest.schema.json](./schema/1.2/page-manifest.schema.json)  
3. Publish `{page-path}.ai.json`  
4. Add `<link rel="alternate" type="application/json" …>` — [docs/discovery-link.md](./docs/discovery-link.md)

---

## Reference implementations

| Platform | Implementation |
|----------|----------------|
| **AigeoRadar.com** | Laravel CMS — virtual serve, live `.ai.json` on marketing pages & blog |
| **WordPress** | [AigeoRadar Connector](https://aigeoradar.com/help/wordpress-plugin-setup) v0.2.2+ — meta storage, virtual `{slug}.ai.json` |

---

## Examples (live)

| File | Source URL |
|------|------------|
| [homepage.ai.json](./examples/homepage.ai.json) | https://aigeoradar.com/index.ai.json |
| [pricing.ai.json](./examples/pricing.ai.json) | https://aigeoradar.com/pricing.ai.json |
| [features.ai.json](./examples/features.ai.json) | https://aigeoradar.com/features.ai.json |
| [blog-aipm-launch.ai.json](./examples/blog-aipm-launch.ai.json) | Launch post sidecar |

---

## Documentation

- [SPECIFICATION.md](./SPECIFICATION.md) — overview  
- [rfcs/AIPM-001.md](./rfcs/AIPM-001.md) — core specification  
- [rfcs/AIPM-002.md](./rfcs/AIPM-002.md) — v1.2.0 changes  
- [BEST_PRACTICES.md](./BEST_PRACTICES.md)  
- [MIGRATION.md](./MIGRATION.md)  
- [CHANGELOG.md](./CHANGELOG.md)  
- Live hub: https://aigeoradar.com/specifications/aipm  

---

## Keywords (for humans & indexes)

`AI Page Manifest` · `AIPM` · `.ai.json` · `GEO` · `generative engine optimization` · `AI visibility` · `llms.txt` · `entity.json` · `AI crawler` · `RAG metadata` · `ChatGPT` · `Perplexity` · `WordPress GEO` · `open specification` · `AigeoRadar` · `ADF`

---

## License

This specification and documentation are licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](./LICENSE).

When implementing or extending AIPM, attribute:

> AI Page Manifest (AIPM) v1.2.0 — maintained by AigeoRadar — https://aigeoradar.com/specifications/aipm

## Author

**Ahmet Gedik** · [AigeoRadar](https://aigeoradar.com) · [GitHub @aagedik](https://github.com/aagedik)

## Contributing

We want people to **use and improve** AIPM — not only read it.

- Start here: **[CONTRIBUTING.md](./CONTRIBUTING.md)**  
- Easy tasks: **[.github/GOOD_FIRST_ISSUES.md](./.github/GOOD_FIRST_ISSUES.md)** (open as GitHub Issues)  
- Release notes: **[RELEASE_NOTES_v1.2.0.md](./RELEASE_NOTES_v1.2.0.md)**  

## Roadmap

- [ ] Validator CLI (`npx @aigeoradar/aipm-validate`)  
- [ ] PHP package / drop-in for custom sites  
- [ ] Optional GitHub **org mirror** later (`aigeoradar/*`) — personal repo stays canonical for now  
- [x] Production discovery seed files (`llms.txt`, `entity.json` pointer)  
- [x] Contributor docs + good-first-issue pack  
