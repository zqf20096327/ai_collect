<p align="center">
  <img src="docs/assets/logo.svg" width="180" alt="RunSpiral logo" />
</p>

<h1 align="center">RunSpiral</h1>

<p align="center"><strong>AI run variance and reproducibility analyzer.</strong></p>

RunSpiral turns a pile of repeated run records into a clear verdict: how
reproducible is your model, agent, or pipeline when you run the same task again
and again? It scores three independent axes — answer stability, route
consistency, and timing variance — folds them into a single reproducibility
grade, and prints a deterministic report you can commit, diff, and gate CI on.

<p align="center">
  <img src="docs/assets/gauge.svg" width="420" alt="Animated reproducibility gauge" />
</p>

---

## Why RunSpiral

Modern AI systems are stochastic. The same prompt can produce different answers,
take different tool paths, and finish in wildly different times from one run to
the next. That variance is invisible until it bites: a flaky eval, a demo that
works once, a customer report you cannot reproduce.

RunSpiral makes variance a first-class, measurable quantity. You capture the
same task N times, hand the records to RunSpiral, and get back a number between
0 and 1 for each task — plus an aggregate grade for the whole suite. Because the
analyzer is fully deterministic, the report is stable input to stable input: the
tool is never the source of the variance it measures.

### What it measures

| Axis | Question it answers | Signal |
| --- | --- | --- |
| **Stability** | Do repeated runs produce the same answer? | modal-answer share + mean pairwise similarity |
| **Route** | Do repeated runs take the same tool path? | share of runs on the most common route |
| **Timing** | Is latency predictable? | coefficient of variation of run latency |

Each axis is a score on `[0, 1]` where `1.0` is perfect. The three are blended
by configurable weights into an overall **reproducibility** score, which is
bucketed into a letter grade (`A`–`F`).

---

## Quick start

```bash
# Analyze a JSONL log of repeated runs (human-readable report)
python -m runspiral analyze examples/repeated_runs.jsonl

# Emit canonical JSON for tooling
python -m runspiral analyze examples/repeated_runs.jsonl --format json

# Gate CI: exit non-zero if overall reproducibility drops below 0.85
python -m runspiral gate examples/repeated_runs.jsonl --threshold 0.85
```

The companion Go component, `spiral`, is a fast fold pre-aggregator that shares
the same record schema:

```bash
cd spiral
go build -o spiral .
./spiral fold -i ../examples/repeated_runs.jsonl
./spiral fingerprint -i ../examples/repeated_runs.jsonl
```

---


## Product workflow

RunSpiral fits into the tail end of any evaluation or benchmarking loop. The
harness you already use to exercise a model is responsible for producing run
records; RunSpiral does the rest.

```
   ┌─────────────┐   repeat N times    ┌──────────────────┐
   │  your task  │ ──────────────────▶ │  run records      │
   │  harness    │                     │  (.jsonl / .json) │
   └─────────────┘                     └────────┬─────────┘
                                                 │
                        ┌────────────────────────┼────────────────────────┐
                        │                         │                        │
                        ▼                         ▼                        ▼
                 ┌────────────┐            ┌────────────┐          ┌──────────────┐
                 │  spiral    │  optional  │  runspiral │          │  runspiral   │
                 │  fold      │  pre-fold  │  analyze   │          │  gate        │
                 │  (Go)      │──────────▶ │  (Python)  │───────▶  │  (CI verdict)│
                 └────────────┘            └─────┬──────┘          └──────────────┘
                                                 │
                                    ┌────────────┴────────────┐
                                    ▼                         ▼
                             ┌────────────┐            ┌────────────┐
                             │ text report│            │ JSON report│
                             │ (humans)   │            │ (tooling)  │
                             └────────────┘            └────────────┘
```

1. **Capture.** Run the same task multiple times, recording each execution as a
   run record (see the schema below). Group runs by `task_id`.
2. **Pre-fold (optional).** For very large logs, `spiral fold` collapses each
   task into a compact summary — distinct-answer and distinct-route counts, a
   stable route fingerprint, and latency extremes — so you can shard or triage
   before full scoring.
3. **Analyze.** `runspiral analyze` scores every group and prints a report.
4. **Gate.** `runspiral gate` turns the overall score into a CI pass/fail.

---

## Architecture

RunSpiral is two cooperating components that share one record schema.

### Python package `runspiral`

| Module | Responsibility |
| --- | --- |
| `model.py` | Immutable dataclasses: `Run`, `RunGroup`, the three score types, `GroupReport`, `Report`. Deterministic `to_dict` on every type. |
| `metrics.py` | Dependency-free similarity and statistics: token Jaccard, character-bigram Dice, combined similarity, mean pairwise similarity, modal, mean, population stdev, coefficient of variation. |
| `analyzer.py` | The scoring model: per-axis scorers, weight validation, grouping, grading, and the top-level `analyze`. |
| `io.py` | Input parsing for JSON and JSONL, plus JSON / text / summary rendering. |
| `cli.py` | The `argparse` command surface: `analyze`, `inspect`, `gate`, `version`. |

### Go module `spiral`

| Path | Responsibility |
| --- | --- |
| `fingerprint/fingerprint.go` | Route-key joining, an explicit FNV-1a 64-bit hash, order-independent route fingerprints, and per-task folding. |
| `main.go` | The `fold`, `fingerprint`, and `version` commands reading JSONL from stdin or `-i`. |

The two components are intentionally decoupled: the Go tool never calls Python
and vice versa. They communicate only through files that follow the shared run
record schema, which keeps each independently useful and independently testable.

---

---

## Milestones

- [x] **v0.1** - answer stability axis, JSON/JSONL loading (2019)
- [x] **v0.2** - route consistency axis, text report (2021)
- [x] **v0.3** - letter grading, frozen JSON schema (2022)
- [x] **v0.4** - timing variance axis, configurable weights (2024)
- [x] **v0.5** - combined similarity, Go fold pre-aggregator (2025)
- [x] **v1.0** - stable report schema, CI gate (2025)
- [ ] **v1.1** - multi-model comparison mode (in progress)

---

## License

MIT - see [LICENSE](LICENSE).
