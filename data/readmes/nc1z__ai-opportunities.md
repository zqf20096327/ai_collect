# The Opportunities in AI

An industry scan of the AI ecosystem — a structured overview of where the field stands, what's being built, and where the gaps are. Built to help builders orient themselves across five layers, from consumer-facing applications down to model consumption APIs.

**Live:** [nc1z.github.io/ai-opportunities](https://nc1z.github.io/ai-opportunities)

## What this is

The taxonomy covers five layers of the AI stack where most builders actually operate:

1. **Application Layer** — products and use cases shipped to end users
2. **Agent & Workflow Layer** — orchestration patterns, agent topologies, human oversight
3. **Harness & Runtime Layer** — context, memory, tool orchestration, safety, observability
4. **Developer Tooling Layer** — evals, prompt management, SDKs, CI/CD, guardrails
5. **Model Consumption Layer** — how applications access, route, and optimise model calls

Deep infrastructure — compute, semiconductors, and foundation model training — is intentionally excluded.

## Research methodology

The taxonomy was built through a structured multi-agent deep research process. Five AI research agents were independently tasked with analysing the AI landscape across each layer. Signals were cross-validated by source agreement count and merged into a unified taxonomy before any code was written.

Agents were selected with reference to the [DeepResearch-Bench leaderboard](https://deepresearch-bench.github.io) — an independent benchmark for deep, multi-step research tasks.

See the [About page](https://nc1z.github.io/ai-opportunities/#/about) for full methodology.

## Running locally

```bash
pnpm install
pnpm run dev
pnpm run build
```

## License

This project uses a dual license:

**Code** — [MIT License](./LICENSE)
The source code is MIT licensed. Use it, fork it, build on it freely.

**Content** — [CC BY 4.0](./LICENSE-CONTENT)
The taxonomy data, written copy, and research-derived content (including `src/data/`) are licensed under Creative Commons Attribution 4.0 International. You are free to share and adapt the content for any purpose, including commercially, as long as you give appropriate credit to the original author ([@nc1z](https://github.com/nc1z)) and link back to this repository.
