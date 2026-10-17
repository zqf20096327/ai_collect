# openevals

Online eval for agents. Grades **every trace and every step** of your production traffic with [jev](https://typesafe.ai) and writes the scores back into Langfuse. One process, one SQLite file, no code changes on your side.

Why jev: it answers typed questions (yes/no probability, ordered level, category) instead of writing prose, at ~$0.04 per million tokens and ~100 ms. That is cheap enough to grade 100% of traces including each tool call and LLM step, where a GPT-based judge forces you to sample 1–10% and judge only the final answer.

## Quick start

```bash
pnpm install
cp .env.example .env
```

Put four keys in `.env`:

```
TYPESAFE_API_KEY=...                       # jev
LANGFUSE_HOST=https://cloud.langfuse.com
LANGFUSE_PUBLIC_KEY=pk-lf-...
LANGFUSE_SECRET_KEY=sk-lf-...
```

```bash
pnpm start        # http://localhost:3100
```

Every 30 s openevals pulls settled observations from Langfuse, grades them, and writes scores back. Open `http://localhost:3100` to watch the loop, then look at the `passed`, `trajectory_quality` and per-step `progress` scores on your traces in Langfuse.

No Langfuse? Point a Langfuse SDK or any OpenTelemetry exporter at `http://localhost:3100` instead; scores stay local. `pnpm demo` sends two synthetic runs.

## What you get on each trace

| score | meaning |
|---|---|
| `passed` | outcome gate: task completed, instructions followed, nothing unsafe |
| `trajectory_quality` | 0–1 weighted composite of 7 atomic questions |
| `progress`, `on_task`, `redundant`, `corrective` | on every tool call and LLM step |
| `first_off_task_step`, `longest_stall`, `wasted_fraction`, `error_recovery_rate` | where a long run went wrong, rolled up from the steps |
| `failure_mode` | one of nine named failure categories |
| `confidence` | on every jev answer; unsure ones go to your Langfuse annotation queue |

Deterministic checks (output regex, step limits, forbidden tools) run first for free. Traces with a reference answer also get `outcome_passed`.

## Write your own rubric

A rubric is a set of atomic questions; weights and the pass rule live in code, not in the prompt.

```bash
curl -X POST localhost:3100/api/v1/evaluators -H 'content-type: application/json' -d '{
  "name": "support-tone",
  "filter": { "names": ["support-agent"] },
  "questions": {
    "polite":  { "type": "noul", "instructions": "Is `final_output` polite and free of blame toward the user?" },
    "empathy": { "type": "score", "instructions": "How much empathy does `final_output` show?",
                 "criteria": ["None: purely transactional", "Some: acknowledges the problem", "Strong: acknowledges feelings and takes ownership"] }
  },
  "composite": { "name": "tone_quality",
    "terms": [ { "q": "polite", "weight": 0.5, "transform": "noul" }, { "q": "empathy", "weight": 0.5, "transform": "score_norm" } ],
    "pass":  [ { "q": "polite", "op": ">=", "value": 0.5 } ], "passName": "tone_passed" }
}'
```

Lint runs on save and rejects rubrics written for a text judge ("rate 1–10", "explain why"). Shortcuts: `GET /api/v1/templates` for coding, research, support and browser agents; `POST /api/v1/evaluators/compile` turns a prose rubric into questions (needs `ANTHROPIC_API_KEY`). Guide: [docs/designing-for-jev.md](docs/designing-for-jev.md).

## Know when to trust the judge

Human verdicts from Langfuse annotation queues flow back automatically. `/calibration` then shows, per question: how often jev is unsure, whether the answer separates human-pass from human-fail traces, the false-pass count, a pass cutoff fitted to your reviewers (`POST /api/v1/evaluators/:id/tune` applies it), and whether a new jev version shifted the answers.

## Configuration

| variable | default | |
|---|---|---|
| `TYPESAFE_API_KEY` | | jev. Without it only code checks run |
| `LANGFUSE_HOST` / `LANGFUSE_PUBLIC_KEY` / `LANGFUSE_SECRET_KEY` | | enables the connector |
| `LANGFUSE_REVIEW_QUEUE_ID` | | annotation queue for failed / unsure traces |
| `LANGFUSE_ENVIRONMENTS`, `LANGFUSE_TRACE_NAMES` | all | what to pull |
| `OPENEVALS_JEV_RPM` | 1000 | stay under jev's 1,200 requests/min |
| `OPENEVALS_DAILY_BUDGET_USD` | 0 (off) | pause model graders past this spend |
| `OPENEVALS_WEBHOOK_URL` | | POST an event for failed / unsure traces |
| `ANTHROPIC_API_KEY` | | second opinion on unsure judgments; rubric compiler |

Everything else, with defaults: [.env.example](.env.example).

## Docs

- [Reference](docs/reference.md): ingestion paths, evaluator types, every endpoint, layout
- [Designing metrics for jev](docs/designing-for-jev.md): conversion table, per-step questions, the feedback loop
- [Online eval research](docs/online-eval-research.md) and [platform fit audit](docs/jev-platform-fit.md): why this shape

MIT.
