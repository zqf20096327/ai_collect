# SEO Intelligence

**SEO + AEO + GEO intelligence for Claude Code.**

[![License: MIT](https://img.shields.io/github/license/Trementdv/seo-intelligence-skill)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/Trementdv/seo-intelligence-skill?style=social)](https://github.com/Trementdv/seo-intelligence-skill/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/Trementdv/seo-intelligence-skill)](https://github.com/Trementdv/seo-intelligence-skill/issues)
[![Validate skill structure](https://github.com/Trementdv/seo-intelligence-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/Trementdv/seo-intelligence-skill/actions/workflows/validate.yml)

A [Claude Code](https://claude.com/claude-code) skill that turns Claude into a disciplined SEO auditor — covering **technical SEO**, **on-page SEO**, **schema/structured data**, **AEO** (Answer Engine Optimization — being cited by ChatGPT, Claude, Gemini, Perplexity) and **GEO** (Generative Engine Optimization — being understood and mentioned as a coherent brand entity by generative AI systems).

## Table of contents
- [Why SEO Intelligence?](#why-seo-intelligence)
- [What it is (and isn't)](#what-it-is-and-isnt)
- [Install](#install)
- [Quick start](#quick-start)
- [Example](#example)
- [Architecture](#architecture)
- [Checks](#checks)
- [Roadmap](#roadmap)
- [FAQ](#faq)
- [Contributing](#contributing)
- [License](#license)

## Why SEO Intelligence?

Search visibility now has three layers, and most tooling still only covers the first one:

| | Traditional SEO | + AEO | + GEO |
|---|---|---|---|
| **Optimizes for** | Google's ranking algorithm | Being quoted verbatim in an AI answer | Being correctly identified as a real, trustworthy entity by generative models |
| **Unit of work** | Pages and keywords | Answerable questions and citable fragments | Brand consistency across the web (NAP, schema, external sources, entity graph) |
| **Fails when** | Technical issues, thin content, weak links | Content buries the answer instead of leading with it | The same brand looks like different entities across the site, Google Business Profile, LinkedIn, directories |

Most "AI SEO" prompts produce a list of generic advice with no evidence behind it. This skill is built around one non-negotiable rule instead: **never invent data.** No fabricated traffic numbers, reviews, clients, or certifications. Every finding is tagged as `OBSERVED`, `INFERRED`, `RECOMMENDED`, or `UNKNOWN — requires verification` — see [`rules/`](rules/).

## What it is (and isn't)

**It is**: a structured prompt-based skill — a `SKILL.md` playbook plus modular check lists, workflows, and safety rules that guide Claude through a real audit-and-fix loop, with a strict evidence discipline.

**It isn't**: a crawler, a SaaS dashboard, or a black-box scoring tool. It doesn't call any external API on its own — it works with whatever access Claude already has to your codebase, Search Console, GA4, or PageSpeed data in your session.

**Current state (v1.0.0)**: 95 documented checks across 11 modules, 4 agent roles, 4 workflows, and a set of non-negotiable safety/evidence rules. See [Checks](#checks) for the exact count per module — this number will grow; the architecture is designed so new checks slot into existing folders without breaking anything (see [Roadmap](#roadmap)).

## Install

**Claude Code (recommended):**
```bash
git clone https://github.com/Trementdv/seo-intelligence-skill.git .claude/skills/seo-intelligence
```
Claude Code auto-discovers skills under `.claude/skills/`. Restart your session and the skill becomes available.

**Manual / any Claude Agent SDK project:**
```bash
git clone https://github.com/Trementdv/seo-intelligence-skill.git
```
Then paste the contents of `SKILL.md` (plus the `checks/` modules you need) into your system prompt or agent instructions.

## Quick start

Once installed, from Claude Code:

```
/full-audit
```

runs the complete discovery → audit → prioritize loop against your current project (see [`workflows/full-audit.md`](workflows/full-audit.md)) and returns a prioritized report — read-only, nothing is modified.

Other entry points:
```
/seo-audit        technical + on-page + indexing + performance only
/schema-audit      structured data — existence AND consistency with visible content
/aeo-audit         citability for AI assistants
/geo-audit         brand-entity signals for generative engines
/eeat-audit        Experience/Expertise/Authoritativeness/Trust, with evidence per finding
/gsc-analysis      Search Console query/page opportunity analysis (needs real GSC access)
/seo-fix           implement previously approved findings, one at a time, with rollback data
/regression-test   re-run the same checks and diff against the last snapshot
```
Full command reference in [`SKILL.md`](SKILL.md#3-comandos--modos-de-uso).

## Example

```
User: Audit this project for SEO.

Claude:
╔══════════════════════════════╗
║       SEO INTELLIGENCE       ║
╠══════════════════════════════╣
║ Technical       82%          ║
║ On-Page         70%          ║
║ Schema          40%          ║
║ AEO             55%          ║
╚══════════════════════════════╝

HIGH — Missing canonical on /pricing
  Evidence:  no <link rel="canonical"> in page source
  Impact:    duplicate-content risk if reachable via multiple URLs
  Fix:       add self-referencing canonical
  File:      /pricing.html
  Validate:  re-fetch the page and confirm the tag is present

Priorities:
1. Fix missing canonicals (HIGH, low effort)
2. Add Organization + Service JSON-LD (HIGH, medium effort)
3. Rewrite title/description for /pricing — 4,200 impressions, 1.1% CTR (MEDIUM, GSC-backed)
```
*(Illustrative example — not output from a real site. Real runs report real numbers only, per [`rules/never-fake-data.md`](rules/never-fake-data.md).)*

## Architecture

Not "audit → PDF → done." The loop the skill follows:

```
DISCOVER → AUDIT → IDENTIFY → PRIORITIZE → PLAN → IMPLEMENT → TEST → RE-AUDIT → LEARN → REPEAT
```

Four separated roles keep responsibilities clear (see [`agents/`](agents/)):

| Role | File | Can modify files? |
|---|---|---|
| Auditor | [`agents/auditor.md`](agents/auditor.md) | No — read-only |
| Fixer | [`agents/fixer.md`](agents/fixer.md) | Yes — only approved findings, one at a time |
| Researcher | [`agents/researcher.md`](agents/researcher.md) | No — competitor/entity/source research |
| Verifier | [`agents/verifier.md`](agents/verifier.md) | No — re-runs checks, diffs, reports regressions |

```
seo-intelligence-skill/
├── SKILL.md              the full playbook: workflow, commands, rules, report format
├── agents/                Auditor · Fixer · Researcher · Verifier
├── checks/                11 modules (see below)
├── workflows/             full-audit · fix · regression · gsc
├── templates/             audit report, llms.txt, llms-full.txt
├── rules/                 never-fake-data · safe-changes · evidence · validation
├── tests/                 structure fixtures + regression snapshots
└── .github/workflows/     CI that validates the skill's own structure
```

## Checks

11 independent modules — each one can grow (adding more granular checks) without touching the others:

| Module | Focus | Checks today |
|---|---|---|
| [`technical`](checks/technical/) | Canonicals, hreflang, sitemap/robots, redirects, JS rendering, HTTPS, mobile | 11 |
| [`on-page`](checks/on-page/) | Title/description, headings, internal links, cannibalization signals | 8 |
| [`indexing`](checks/indexing/) | Coverage, accidental noindex, duplicates, cannibalization, quick-win positions | 7 |
| [`schema`](checks/schema/) | Right Schema.org type per business, and consistency with visible content | 7 |
| [`performance`](checks/performance/) | Core Web Vitals (LCP, INP, CLS) | 7 |
| [`accessibility`](checks/accessibility/) | Semantic HTML that also helps AI parsing | 6 |
| [`eeat`](checks/eeat/) | Experience/Expertise/Authoritativeness/Trust, evidence-based, plus anti-spam detection | 9 |
| [`aeo`](checks/aeo/) | FAQ quality, direct answers, citable fragments, entity naming | 9 |
| [`geo`](checks/geo/) | Entity graph, NAP consistency, external sources vs. self-reported claims | 15 |
| [`llm`](checks/llm/) | `llms.txt` / `llms-full.txt` presence and accuracy | 5 |
| [`local-seo`](checks/local-seo/) | Google Business Profile — physical vs. service-area businesses | 11 |

**95 checks total.** Every failed check becomes a finding formatted as *Problem → Evidence → Impact → Solution → File → Recommended change → Validation* — never a bare checkbox (see [`SKILL.md` §6](SKILL.md)).

## Roadmap

**Current (v1.0.0)**
- Full check framework across 11 modules, 4 agent roles, 4 workflows.
- Evidence discipline (`OBSERVED` / `INFERRED` / `RECOMMENDED` / `UNKNOWN`) and anti-fake-data rules.
- Structure-validation CI.

**Next**
- Expand check coverage per module toward more granular, automatable checks.
- `tests/fixtures` with paired good/bad examples per check for regression coverage.
- CONTRIBUTING guide for adding new checks with review criteria.

**Planned (exploratory, not implemented yet)**
- Deeper Search Console workflow automation (`/gsc-analysis` today is a documented workflow, not a live API integration bundled in the repo).
- Competitor/content-gap tooling beyond the current researcher-agent guidance.
- Continuous SEO monitoring pattern (scheduled re-audits + regression alerts).

Nothing above is claimed as already built if it isn't — see [`CHANGELOG.md`](CHANGELOG.md) for what shipped in each version.

## FAQ

**What is SEO Intelligence?**
A Claude Code skill (a structured prompt playbook, not a SaaS) that guides Claude through evidence-based SEO/AEO/GEO audits and fixes.

**Is it free?**
Yes — MIT licensed, use it, fork it, redistribute it.

**Does it work with Claude Code?**
Yes, that's its primary target. It also works with any Claude Agent SDK setup by pasting `SKILL.md` into your system instructions.

**Who is it for?**
Developers and agencies who want Claude to audit and improve a site's SEO/AEO/GEO with real evidence instead of generic advice.

**What does it audit?**
Technical SEO, on-page SEO, indexing, structured data, performance, accessibility, E-E-A-T, AEO, GEO, `llms.txt`, and local SEO. See [Checks](#checks).

**Does it modify my code?**
Only if you ask it to (`/seo-fix`), and only after you approve specific findings. `/full-audit` and the other `*-audit` commands are read-only. See [`rules/safe-changes.md`](rules/safe-changes.md).

**Can I use it on an existing project?**
Yes — that's the main use case. It reads what's already there before proposing anything.

**Can I contribute a check?**
Yes, see [Contributing](#contributing).

**How is this different from traditional SEO tools?**
Traditional tools score pages against ranking signals. This skill also evaluates whether a brand can be understood, cited, and correctly attributed by generative AI systems (GEO) — and it explicitly refuses to fabricate data to make a report look more complete.

**Does it guarantee rankings?**
No. Nothing does. It gives you evidence-based findings and lets you (or Claude, once approved) act on them.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Security

Found something that looks like a security issue in the skill's guidance itself (e.g., a rule that could lead to leaking credentials or unsafe writes)? Please open an issue.

## License

[MIT](LICENSE) — use it, adapt it, ship it in your own tools and agents.

---

Created and maintained by [Trement](https://trement.co) — a software development and AI automation company based in Medellín, Colombia, that built this discipline while running SEO/AEO/GEO for its own site.

**If this was useful, a ⭐ helps other developers find it.**
