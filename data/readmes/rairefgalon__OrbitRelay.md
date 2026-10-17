<!-- OrbitRelay README -->
<p align="center">
  <img src="docs/assets/orbit-banner.svg" alt="OrbitRelay banner" width="720"/>
</p>

<h1 align="center">OrbitRelay</h1>
<p align="center"><em>The Multi-Agent Handoff Inspector.</em></p>
<p align="center">
  <code>Python 3.11</code> &nbsp;•&nbsp; <code>.NET 9.0</code> &nbsp;•&nbsp; <code>zero dependencies</code> &nbsp;•&nbsp; <code>Apache-2.0</code>
</p>

---

## Why OrbitRelay exists

Multi-agent systems fail in the seams. A planner decomposes a task and hands it to a
researcher; the researcher gathers findings and hands them to an engineer; the engineer
proposes a fix and hands it to a reviewer. Each of those arrows — each **handoff** — is a
place where context can be dropped, mangled, or silently omitted. When a successor agent
never receives the *goal* it was supposed to pursue, or receives a *constraint* field that
was acknowledged but left empty, the whole session drifts. The failure is rarely in any
single agent; it is in the **relay**.

OrbitRelay treats the relay boundary as a first-class object. It ingests a recorded
multi-agent session, walks every handoff, classifies every transferred context field
against a declared contract, scores how *complete* each handoff was, surfaces where
coordination cost concentrates, and renders a **conversation-flow review dossier** you can
attach to an incident write-up or a regression review.

It is fully offline and dependency-free. The Python package renders the operator-facing
dossier; a companion **.NET 9 analyzer** recomputes completeness independently so you get a
cross-implementation sanity check on every trace.

<p align="center">
  <img src="docs/assets/orbit-pipeline.svg" alt="OrbitRelay pipeline stages" width="720"/>
</p>

---

## Table of contents

1. [Concepts and vocabulary](#concepts-and-vocabulary)
2. [The trace schema](#the-trace-schema)
3. [Architecture](#architecture)
4. [The five-stage pipeline](#the-five-stage-pipeline)
5. [Completeness scoring algorithm](#completeness-scoring-algorithm)
6. [Bottleneck detection](#bottleneck-detection)
7. [The dossier](#the-dossier)
8. [CLI reference and recipes](#cli-reference-and-recipes)
9. [The .NET companion analyzer](#the-net-companion-analyzer)
10. [Operations](#operations)
11. [Extension seams](#extension-seams)
12. [Glossary](#glossary)

---

## Concepts and vocabulary

OrbitRelay's model is deliberately small so a trace round-trips through JSON without custom
encoders. Five nouns carry the whole design:

- **Agent** — a named participant with a `role` and a set of `capabilities`. Roles matter
  because contracts are keyed by role, not by agent identity: any agent acting as a
  `reviewer` is held to the reviewer contract.
- **Turn** — a single utterance produced by one agent at a monotonic `tick`. Turns give the
  dossier a timeline and a token budget; they are not scored directly.
- **ContextField** — a named slice of state the source intends to transfer: `goal`,
  `constraints`, `root_cause_hypothesis`, `test_evidence`, and so on. Each field has a
  `kind` (goal / constraint / artifact / state / note) and a `value`.
- **Handoff** — the relay boundary itself. It records `source_agent`, `target_agent`, the
  `tick` at which control passed, a human `reason`, a `latency_ms`, and the bag of context
  fields carried across.
- **HandoffTrace** — the complete record: agents, turns, handoffs, a `contract`, and
  free-form `metadata`.

The **contract** is the heart of the analysis. It maps a target *role* to the list of
context field names that any handoff into that role must carry. If the `engineer` contract
requires `["goal", "root_cause_hypothesis", "affected_service", "constraints"]`, then a
handoff into an engineer that omits `constraints` is scored as incomplete — even if the
agents "felt" done.

---

## The trace schema

A trace is a single JSON object. Here is the shape, annotated:

```jsonc
{
  "trace_id": "orbit-2026-0417-incident-triage",   // stable identifier
  "metadata": { "title": "…", "session": "…" },     // free-form, shown in the dossier header
  "contract": {                                      // role -> required field names
    "engineer": ["goal", "root_cause_hypothesis", "affected_service", "constraints"]
  },
  "agents": [
    { "agent_id": "eng-1", "role": "engineer", "capabilities": ["code"], "model": "coder-pro" }
  ],
  "turns": [
    { "turn_id": "t4", "agent_id": "eng-1", "tick": 3, "text": "…", "tokens": 44 }
  ],
  "handoffs": [
    {
      "handoff_id": "h3",
      "source_agent": "rsr-1",
      "target_agent": "eng-1",
      "tick": 3,
      "reason": "implement fix",
      "latency_ms": 950,
      "fields": [
        { "name": "goal", "kind": "goal", "value": "Restore pool sizing", "required": true },
        { "name": "affected_service", "kind": "state", "value": "payments-api" }
      ]
    }
  ]
}
```

The loader validates structure and **referential integrity**: every `source_agent`,
`target_agent`, and turn `agent_id` must resolve to a declared agent, or loading fails with
a precise `TraceError` naming the offending record. This catches the most common corruption
mode — a renamed agent leaving dangling relay references — before scoring ever runs.

A field's **emptiness** is intrinsic, not declared: `null`, `""`, `[]`, and `{}` are all
empty regardless of the `required` flag. This is what lets the scorer distinguish a field
that was *forgotten* (missing) from one that was *acknowledged but never populated* (empty)
— two very different coordination failures.

---

## Architecture

OrbitRelay is a straight, stateless pipeline. Each stage consumes the previous stage's
output and adds no hidden state, so the same trace always yields the same dossier.

```
                         ┌────────────────────────────────────────────────┐
   trace.json  ─────────▶│  loader.load_trace                              │
                         │    · JSON parse                                 │
                         │    · structural validation                      │
                         │    · referential integrity check                │
                         └───────────────────────┬────────────────────────┘
                                                 │  HandoffTrace
                                                 ▼
                         ┌────────────────────────────────────────────────┐
                         │  inspector.inspect_handoffs                     │
                         │    · resolve target role                        │
                         │    · look up contract-required fields           │
                         │    · classify each field:                       │
                         │        PRESENT / EMPTY / MISSING / EXTRA         │
                         └───────────────────────┬────────────────────────┘
                                                 │  List[HandoffInspection]
                          ┌──────────────────────┼───────────────────────┐
                          ▼                       ▼                       ▼
              ┌────────────────────┐  ┌────────────────────┐  ┌────────────────────┐
              │ scoring            │  │ bottleneck         │  │ dossier            │
              │ ·weighted penalty  │  │ ·latency           │  │ ·flow map          │
              │ ·per-handoff grade │  │ ·fan-in / fan-out  │  │ ·relay ledger      │
              │ ·mean + weakest    │  │ ·rework            │  │ ·score + gaps      │
              └─────────┬──────────┘  └─────────┬──────────┘  └─────────┬──────────┘
                        │                       │                       │
                        └───────────────────────┴───────────────────────┘
                                                 ▼
                                        Markdown dossier
```

Module map:

| Module | Responsibility |
|--------|----------------|
| `orbitrelay/model.py` | Frozen dataclasses for the trace model. |
| `orbitrelay/loader.py` | JSON parsing, validation, referential integrity, `TraceError`. |
| `orbitrelay/inspector.py` | Per-field classification against the contract. |
| `orbitrelay/scoring.py` | Weighted-penalty completeness score and grade. |
| `orbitrelay/bottleneck.py` | Latency / fan / rework detection. |
| `orbitrelay/dossier.py` | Markdown composition of all stages. |
| `orbitrelay/cli.py` | Argparse pipeline: `inspect`, `score`, `bottlenecks`, `dossier`, `pipeline`. |
| `runtime/` | .NET 9 companion analyzer (independent recompute). |

---

## The five-stage pipeline

The pipeline is `load → inspect → score → bottlenecks → dossier`. Every stage is a pure
function of its input:

1. **load** parses and validates the trace document.
2. **inspect** classifies each transferred field. This is the only stage that touches the
   contract; downstream stages consume the classification.
3. **score** converts classifications into a numeric completeness score per handoff and an
   aggregate mean.
4. **bottlenecks** scans the relay graph for coordination hotspots.
5. **dossier** composes a Markdown review document from all of the above.

Run the whole thing with `python -m orbitrelay pipeline --trace examples/incident_triage.json`.

---

## Completeness scoring algorithm

Each handoff earns a score in `[0.0, 1.0]` from a **weighted penalty aggregate**. Start at a
perfect `1.0` and subtract penalties proportional to how the required fields fared:

```
base   = 1.0
base  -= 0.60 * (missing_required / max(required, 1))   # MISSING_WEIGHT
base  -= 0.30 * (empty_required   / max(required, 1))   # EMPTY_WEIGHT
base  -= 0.10 * (min(extra, 5) / 5)                      # EXTRA_WEIGHT, capped
score  = clamp(base, 0.0, 1.0)
```

The weights encode a coordination philosophy:

- **Missing required fields (0.60)** are the most damaging. A successor that never receives
  its goal cannot recover it from thin air; the relay has structurally failed.
- **Empty required fields (0.30)** are penalised half as hard. The source *knew* the field
  belonged in the bag — it just failed to populate it. That is a recoverable slip: the
  successor at least knows what is expected.
- **Extra fields (0.10, capped at 5)** incur a small penalty because they inflate the
  transferred context and can distract the successor. The cap ensures a genuinely verbose
  but complete relay never scores as a failure.

Scores map to letter grades for quick scanning:

| Score range | Grade | Reading |
|-------------|:-----:|---------|
| ≥ 0.90 | **A** | complete or near-complete relay |
| ≥ 0.75 | **B** | one recoverable gap |
| ≥ 0.55 | **C** | multiple gaps, review needed |
| ≥ 0.35 | **D** | significant context loss |
| < 0.35 | **F** | relay effectively failed |

The aggregate report also names the **weakest handoff** so a reviewer can jump straight to
the worst relay in a long session.

---

## Bottleneck detection

Scoring tells you *whether* context arrived. Bottleneck detection tells you *where
coordination cost concentrates*. Four deterministic signatures are recognised:

- **latency** — a relay whose `latency_ms` exceeds a rolling threshold of
  `mean + population-stddev` across the trace. Slow relays serialise the whole session.
  Severity scales with the relay's share of the peak latency.
- **fan_in** — an agent that receives handoffs from three or more distinct sources. High
  fan-in agents are integration chokepoints where many threads must be reconciled.
- **fan_out** — an agent that dispatches to three or more distinct targets. High fan-out is
  a dispatch chokepoint that may be over-delegating.
- **rework** — a relay pair `(source → target)` that repeats two or more times, signalling a
  relay that had to be retried because context was lost the first time.

Detection is threshold-based and fully deterministic. On the bundled incident-triage
fixture it flags the `rsr-1 → eng-1` relay (950 ms, above the 547 ms threshold) as the top
latency bottleneck and the `eng-1 → rev-1` pair as rework (the reviewer bounced the fix back
for load evidence, then re-approved).

---

## The dossier

The dossier is the human-facing artifact. It is pure string composition — no templating
engine — so it is reproducible and diff-friendly. Sections:

- **Header** — trace identity, agent/handoff/turn counts, token total, mean completeness,
  and the weakest relay.
- **Conversation flow map** — an ASCII rendering where each relay's arrow width grows with
  the number of fields carried, annotated with latency.
- **Relay ledger** — one row per handoff with present / empty / missing / extra counts.
- **Completeness scores** — per-handoff score, grade, and gap counts.
- **Coordination bottlenecks** — the detected hotspots, sorted by severity.
- **Notes** — a plain-language list of exactly which fields each incomplete relay dropped.

See [`docs/dossier-format.md`](docs/dossier-format.md) for a section-by-section spec.

---

## CLI reference and recipes

All commands read a trace with `--trace` and emit stable, sort-keyed output.

```bash
# Classify every field at every relay (JSON)
python -m orbitrelay inspect --trace examples/incident_triage.json

# Score handoff completeness with grades and the weakest relay
python -m orbitrelay score --trace examples/incident_triage.json

# Surface coordination bottlenecks
python -m orbitrelay bottlenecks --trace examples/incident_triage.json

# Render the dossier to stdout …
python -m orbitrelay dossier --trace examples/incident_triage.json

# … or to a file
python -m orbitrelay dossier --trace examples/incident_triage.json --out dossier.md

# Run the full pipeline and write dossier.md, printing a JSON summary
python -m orbitrelay pipeline --trace examples/incident_triage.json --out review.md
```

**Recipe — gate a session on completeness.** Pipe `score` through a JSON reader and fail CI
when the mean drops below your bar:

```bash
python -m orbitrelay score --trace trace.json \
  | python -c "import sys,json; d=json.load(sys.stdin); sys.exit(0 if d['mean_score']>=0.85 else 1)"
```

**Recipe — diff two runs.** Because JSON output is sort-keyed, you can capture two runs and
`diff` them to see exactly which relays regressed between versions of your agent stack.

**Recipe — triage the worst relay first.** `score` reports `weakest_handoff`; feed it back
to `inspect` and grep the outcomes to read the precise gap.

---

## The .NET companion analyzer

The `runtime/` project is an independent second opinion. It parses the same trace with
`System.Text.Json` (part of the .NET base class library — no NuGet packages) and recomputes
completeness with the **exact same weights and grade thresholds** as the Python scorer. If
the two implementations ever disagree on a trace, the scoring contract has drifted — which
is itself a useful signal.

```bash
# Independent completeness recompute
dotnet run --project runtime -c Release -- analyze examples/incident_triage.json

# Compact flow rendering
dotnet run --project runtime -c Release -- flow examples/incident_triage.json
```

On the bundled fixture both implementations report a mean completeness of **0.911** over 7
relays — byte-for-byte agreement on every per-handoff score.

---

## Operations

- **Determinism.** Every stage is a pure function; there is no wall-clock, randomness, or
  network access anywhere in the pipeline. Re-running a trace always yields the same dossier.
- **Failure modes.** Malformed JSON, missing required keys, and dangling agent references
  all raise `TraceError` with a message that names the exact record. The CLI maps these to
  exit code `2`.
- **Performance.** The pipeline is linear in the number of fields across all handoffs. A
  trace with thousands of relays scores in well under a second; there is no quadratic step.
- **Portability.** Python 3.11 standard library only; .NET 9 base class library only. No
  build step downloads anything.

---

## Extension seams

- **New field kinds.** `kind` is a free string; add `decision`, `risk`, or `budget` and the
  inspector will carry them through untouched. Only the contract decides what is *required*.
- **New bottleneck signatures.** Add a detector function in `bottleneck.py` that returns
  `Bottleneck` records; the dossier renders any kind you emit without changes.
- **Alternate scoring.** The weights (`MISSING_WEIGHT`, `EMPTY_WEIGHT`, `EXTRA_WEIGHT`,
  `EXTRA_CAP`) are module constants. Fork the scorer to weight your own risk model, and keep
  the C# constants in lockstep to preserve the cross-check.
- **Custom dossier sections.** `dossier.py` composes a list of string blocks; append your
  own block builder to inject an org-specific section.

---

## Glossary

| Term | Meaning |
|------|---------|
| **Agent** | A named participant with a role and capabilities. |
| **Bottleneck** | A place where coordination cost concentrates (latency / fan / rework). |
| **Completeness** | How fully a handoff satisfied its target contract, scored `[0,1]`. |
| **ContextField** | A named unit of state transferred at a handoff. |
| **Contract** | A role → required-field-names mapping the scorer enforces. |
| **Dossier** | The rendered Markdown conversation-flow review document. |
| **Empty field** | A field present in the bag but carrying a null/empty value. |
| **Extra field** | A supplied field not named in the target contract. |
| **Fan-in / fan-out** | Count of distinct source / target agents at a node. |
| **Handoff** | The relay boundary where control passes between agents. |
| **Missing field** | A contract-required field absent from the handoff bag. |
| **Relay** | A synonym for a handoff, emphasising the pass-the-baton framing. |
| **Rework** | A repeated relay pair, signalling a retried handoff. |
| **Tick** | A monotonic clock index ordering turns and handoffs. |
| **Trace** | The complete recorded multi-agent session. |
| **Weakest handoff** | The relay with the lowest completeness score in a trace. |

---

## Reporting issues

Bugs and surprising inspection results are both welcome as issues. Please
include the trace (or a minimised version of it) that produced the wrong
output, the command line used, and the expected versus actual result. Because
OrbitRelay is deterministic, a wrong score should reproduce exactly on the
same input, which makes trace plus command a complete bug report. Security
concerns should be reported privately rather than in a public issue; the
repository security policy lists the contact channel.

## License

Licensed under the Apache License, Version 2.0. See [`LICENSE`](LICENSE).
