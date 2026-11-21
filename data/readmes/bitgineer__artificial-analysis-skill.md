# Artificial Analysis Skill

An agent skill and small CLI that collect LLM model data from [ArtificialAnalysis.ai](https://artificialanalysis.ai), apply a fixed comparison scale, and emit JSON. The agent that runs the skill writes the report from that JSON.

No API keys. No accounts. No dependencies beyond Node.js.

## Why a fixed scale

Model comparisons drift: one report ranks by intelligence, the next by price, a third by whatever the model felt like. This project keeps one auditable definition of what matters:

- a **metric registry** where every metric declares its unit and which direction is better;
- **use-case profiles** that rank models by their average position across the metrics that matter for a job.

Adding a metric or a use case is a one-line data edit in `scripts/lib/scale.mjs`.

## Requirements

Node.js 18 or newer. The scripts use only built-in modules.

## Install

OpenCode: copy this folder into your skills directory.

```powershell
# Windows
Copy-Item -Recurse . "$env:USERPROFILE\.config\opencode\skills\artificial-analysis"
```

```bash
# macOS / Linux
cp -r . ~/.config/opencode/skills/artificial-analysis
```

Any other agent: point it at `SKILL.md` and let it run the scripts. The skill is Markdown plus Node scripts, nothing else.

## Works with

The skill is Markdown plus Node scripts, so it is not tied to one harness:

- **OpenCode**: native skill format. Copy the folder into `skills/`.
- **Claude Code, Codex, Cursor, Windsurf, Cline, Aider, Gemini CLI**: point the agent at `SKILL.md` and let it run the scripts.
- **DSH (DeepSeek Harness)** and other harnesses: same rule, `SKILL.md` plus Node 18 or newer.

Tested with OpenCode.

## Use

```bash
# 1. Discover model ids (optional)
node scripts/collect.mjs --list --query deepseek

# 2. Collect and rank. Two or more ids.
node scripts/collect.mjs --models claude-opus-5-5,gpt-6-astra --out aa-comparison.json

# 3. Or read an existing comparison page
node scripts/collect.mjs --url "https://artificialanalysis.ai/models/comparisons/a-vs-b" --out aa-comparison.json
```

The collector prints the metric leaders and the top of every use-case ranking, then writes the JSON. The write is atomic. Parallel runs should pass a distinct `--out` each, since the last run wins.

## Output

| Field | Meaning |
|---|---|
| `collectedAt`, `sourceUrl`, `extractionSource` | Provenance. Cite the first two. |
| `modelCount`, `modelsWithData` | Catalog size, and how many models carry any metric. |
| `models[]` | Normalized records: prices, speed, context, flags, benchmarks, cost per task. |
| `metrics[]` | Leaders per metric: `best.value`, `best.names`, `direction`, `unit`. |
| `useCases[]` | Ranking per use case: `averageRank`, `metricsWithData`, `metricsTotal`. |

See `references/scale.md` for every field, metric and use case.

## The scale

Metrics cover intelligence, benchmarks, price, performance and capabilities. Each declares a direction, so lower prices win and higher scores win. Missing values stay null and never count as zero.

Use cases: software development, agents and automation, scientific research, interactive and general use, and QA and test engineering.

## Limits

- The data comes from scraping a public page. The page can change without notice, and its catalog is far larger than the set that carries benchmark data.
- A few metrics are published for only part of the catalog. Rankings say how many metrics each row rests on.
- Cost per task is Artificial Analysis's weighted cost over its evaluation suite, not your workload.
- This project is not affiliated with Artificial Analysis.

## Privacy

No telemetry, no credentials, no local data. The scripts make HTTPS requests to `artificialanalysis.ai` only and reject every other host. Generated JSON stays wherever you write it.

## Tests

```bash
npm test
```

The tests run offline against fixtures.

## License

Not chosen yet.
