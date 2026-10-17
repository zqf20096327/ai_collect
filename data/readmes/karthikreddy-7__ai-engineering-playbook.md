<div align="center">

# AI Engineering Playbook

**A zero-to-100 learning path for applied AI engineering.**

RAG · embeddings · vector search · agents · MCP · and the production engineering around them

<br>

[![Read the site](https://img.shields.io/badge/read_the_site-4C5BD4?style=for-the-badge&logoColor=white)](https://karthikreddy-7.github.io/ai-engineering-playbook/)
[![Contributing](https://img.shields.io/badge/contributing-22242E?style=for-the-badge)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-22242E?style=for-the-badge)](LICENSE)

<br>

![Sections](https://img.shields.io/badge/sections-11-4C5BD4)
![Pages](https://img.shields.io/badge/pages-56-4C5BD4)
![Diagrams](https://img.shields.io/badge/diagrams-49-4C5BD4)
![Worked designs](https://img.shields.io/badge/worked_designs-5-4C5BD4)
![Quiz questions](https://img.shields.io/badge/quiz_questions-230-1F9D63)
![Flashcards](https://img.shields.io/badge/flashcards-155-1F9D63)

### 📖 **[karthikreddy-7.github.io/ai-engineering-playbook](https://karthikreddy-7.github.io/ai-engineering-playbook/)**

*Search · dark mode · rendered diagrams · self-graded quizzes · flashcard drills · progress tracking*

</div>

---

## What this is

The **consumer side** of AI engineering: you take models you did not train and build systems that
are correct, fast, cheap, and safe enough to put in front of real users.

Most material on this subject is a pile of definitions. Definitions tell you what something is
called. They don't tell you what breaks without it, what it costs, or what you'd reach for instead
— and those are the things that matter when you're the one building it.

So every page answers three questions, in order:

<table>
<tr>
<td width="33%" valign="top">

**① Why does this exist?**

The specific pain that makes the concept necessary, and why the obvious alternatives lose.

</td>
<td width="33%" valign="top">

**② How does it actually work?**

One level down, with a diagram: the mechanism, the parameters, and the maths that matter.

</td>
<td width="33%" valign="top">

**③ What goes wrong in production?**

Scale, cost, latency, failure modes — the things that only show up under real traffic.

</td>
</tr>
</table>

> [!NOTE]
> **This is not a machine-learning course.** No PyTorch, no training loops, no backprop. Model
> internals appear only at *survival depth* — enough to reason about a boundary question without
> bluffing.

## Who it's for

Engineers building at the application layer who want to understand these systems properly rather
than assemble them from tutorials. It assumes you can code and have called an LLM API.

It's organized around the questions that decide whether a system works:

- How does RAG actually work — and what does productionizing it involve?
- How does HNSW work, and why cosine similarity?
- How do you evaluate retrieval quality when there's no single right answer?
- What does document Q&A over 10M documents for 50k users look like?
- When should you *not* build an agent?
- Where do latency, cost, and failures come from in an LLM pipeline?

## The path

Eleven sections in dependency order. Each assumes the ones above it.

| # | Section | What it covers |
|---|---|---|
| 01 | [LLM Fundamentals](docs/01-llm-fundamentals/) | How LLMs work, tokens & context, sampling, prompting, structured output, APIs, hallucination |
| 02 | [Embeddings & Search](docs/02-embeddings-and-search/) | Embeddings, similarity metrics, ANN indexes (HNSW/IVF), hybrid search, rerankers |
| 03 | [Vector Databases](docs/03-vector-databases/) | Choosing a store, metadata filtering, scaling & operations |
| 04 | [RAG](docs/04-rag/) | The pipeline, chunking, retrieval patterns, graph & agentic RAG, **evaluation**, **production** |
| 05 | [Agents](docs/05-agents/) | The agent loop, tool calling, orchestration & memory, multi-agent, reliability |
| 06 | [MCP](docs/06-mcp/) | The Model Context Protocol, and building MCP servers |
| 07 | [Production](docs/07-production/) | Latency, cost, reliability, observability, security, evals & testing |
| 08 | [Model Landscape](docs/08-model-landscape/) | Choosing models, open source & self-hosting, fine-tuning vs RAG |
| 09 | [Multimodal](docs/09-multimodal/) | Vision, audio, and multimodal ingestion at survival depth |
| 10 | [System Design](docs/10-system-design/) | A repeatable reasoning framework + five worked designs |
| 11 | [Rapid Fire](docs/11-rapid-fire/) | Flashcard-style Q→A per section, plus tradeoff one-liners |

## How every page is built

| Section | What it does |
|---|---|
| **Prerequisites** | What the page assumes, linked — so you can walk *up* when something is shaky |
| **The intuition** | The idea in plain language, with one load-bearing analogy, before any terminology |
| **Why it exists** | The specific pain that makes the concept necessary, and why the alternatives lose |
| **The core idea** | The concept stated properly and densely — the version you'd want to explain out loud |
| **How it actually works** | One level down, with a diagram: mechanism, parameters, and the maths that matter |
| **The flows** | The distinct end-to-end paths, each with what selects it and what breaks it |
| **A worked example** | One concrete input traced through with real numbers — then deliberately broken |
| **Production concerns** | Scale, cost, latency, failure modes, and what only shows up with real traffic |
| **Common drill-downs** | The questions a good engineer asks one level down, with answers |
| **Test yourself** | Scenario questions — reasoning, not recall |
| **Go deeper** | Curated, individually verified links: official docs, canonical blogs, papers, talks |
| **Where this connects** | The natural next topics, and why you'd go there |

Every page opens with its **prerequisites** and closes with **where this connects**, so the site is
a web you can walk rather than a list you read front to back.

## Built to be studied, not skimmed

Recognising an answer feels almost identical to being able to produce one — and the two come apart
the moment you have to explain something out loud. So the site makes you produce it.

| | |
|---|---|
| 🧠 **230 quiz questions** | Scenario questions at the end of every page. Answer out loud, reveal, then grade yourself. The grade is what counts, not the recognition. |
| 🔁 **155 flashcards** | The rapid-fire decks in drill mode — keyboard navigation, shuffle, and a *weak only* filter that comes straight back to what you flagged. |
| 📈 **Progress tracking** | Mark pages understood and watch the path fill in. Stored in your browser — no account, nothing sent anywhere. |

## How to use it

**Read the whole path** — sections in nav order. Each assumes the ones above it, and pages inside a
section are ordered so nothing is used before it's introduced. Follow the
[dependency map](https://karthikreddy-7.github.io/ai-engineering-playbook/docs/#the-dependency-map)
and you'll never hit an idea you haven't met.

**Repair one weak spot** — start at the page you're shaky on and walk its **Prerequisites** links
*upward* until you hit something solid, then come back down.

**Fast recall** — the [rapid-fire decks](docs/11-rapid-fire/) and
[tradeoff one-liners](docs/11-rapid-fire/tradeoff-one-liners.md). Drill them, say the answer out
loud, grade yourself honestly.

## The running example

One system recurs across the site so abstract ideas land on something concrete: a **governed
enterprise LLM platform** — a model gateway over a managed cloud model service, with
entitlement-filtered retrieval over internal documents, temporary document upload, grounded web
search, an agent mode calling internal tools over MCP, and a guardrails/observability layer around
all of it.

It's deliberately generic — an architecture pattern many organizations converge on, not any one
company's system. Numbers used with it are illustrative typical scale, not measured figures.

## Correctness policy

- **Every external link was fetched and verified** before being committed. No dead links, no
  hallucinated citations.
- **Broken internal links, missing anchors, and pages left out of the nav fail the build** — they
  can never reach the site.
- **Content is checked against its source on every build**, so nothing can be silently lost in
  publishing.
- **This field rots fast.** Model names, prices, context limits, and API specifics change monthly.
  Mechanisms and tradeoffs don't. Cross-check any specific figure against provider docs before
  relying on it.

## Running it locally

The site is [Next.js](https://nextjs.org) + [Fumadocs](https://fumadocs.dev), statically exported.
Prose lives in `docs/` as plain Markdown; the site content is generated from it.

```bash
cd web
pnpm install
pnpm run migrate   # docs/*.md -> web/content/docs/*.mdx
pnpm dev           # http://localhost:3000
pnpm run check     # everything CI enforces
```

```
docs/               plain Markdown — the source of truth, edit this
mkdocs.yml          the nav order (pedagogical, not alphabetical)
web/                the Next.js + Fumadocs site
  content/docs/     GENERATED from docs/ — never edit by hand
  components/       quizzes, flashcard decks, progress, diagrams
  scripts/          migration, nav generation, and the build checks
```

## Contributing

Spotted an error, a stale claim, or a better canonical resource? Issues and PRs welcome — this
field moves fast and correctness beats coverage.

**→ Read [CONTRIBUTING.md](CONTRIBUTING.md) first.** The one rule: write in `docs/`, never edit
`web/content/`.

## License

[MIT](LICENSE)
