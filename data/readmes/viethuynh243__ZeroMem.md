# ZeroMem

[![inspired by](https://img.shields.io/badge/inspired_by-arXiv%3A2607.29377v1-b31b1b)](https://arxiv.org/abs/2607.29377)
[![LLM calls in pipeline](https://img.shields.io/badge/LLM_calls_in_pipeline-0-2ea44f)](tests/test_no_llm_calls.py)
[![new dependencies](https://img.shields.io/badge/new_dependencies-0-2ea44f)](requirements.txt)
[![python](https://img.shields.io/badge/python-3.12%2B-3776ab)](pyproject.toml)
[![install](https://img.shields.io/badge/install-numpy%20%7C%20scipy%20%7C%20regex-2ea44f)](#install)
[![Claude Code skill](https://img.shields.io/badge/Claude_Code-skill-d97757)](SKILL.md)

Long-term memory for Claude Code, over your own session history.

> The two green badges are load-bearing claims, not decoration.
> `tests/test_no_llm_calls.py` fails the build if any module under `zeromem/`
> imports an HTTP client or names an LLM API, and every dependency in
> `requirements.txt` was already present — BM25 is vendored on `scipy.sparse`,
> nearest-neighbour search is a numpy matmul, entity extraction is regex.

ZeroMem is an independent, from-scratch Claude Code skill: it indexes your own
Claude Code transcripts (`~/.claude/projects/**/*.jsonl`) and returns evidence
for recall using deterministic, token-free memory operations — **no LLM call
anywhere in the memory pipeline itself**.

The architecture takes its starting point from the Zero-Mem paper
(arXiv:2607.29377v1) and builds on its four components — a
provenance-preserving token-free memory substrate, query-conditioned evidence
routing, dual-view retrieval with closure, and deterministic calibration. Every
line of code here is written from scratch against Claude Code transcripts; no
code, data, or result is taken from the paper.

Several things this project adds are **not** in the paper and were designed and
measured here:

- **Abstention** — a support gate that reports when the corpus does not hold
  the answer, with the missing terms named (`references/abstention.md`)
- **A targeted probe** on weak results that says where each missing term
  actually occurs, if anywhere (`zeromem/retrieve/escalate.py`)
- **A local recall daemon** that loads the index once, ~18× faster warm recall
  (`references/latency.md`)
- **A measurement suite** — throughput, extractor precision, router accuracy,
  recall ablations, abstention — all run on a real corpus, all reported with
  what the sample cannot see

The only model in the loop is Claude, reading what the pipeline returns.

## Install

Works the same on Windows, macOS, and Linux. Python 3.12+ is the only
prerequisite.

```
git clone https://github.com/viethuynh243/ZeroMem
cd ZeroMem
python install.py
```

That installs the engine (putting `zeromem` on your PATH) and links the skill
into `~/.claude/skills/zeromem`. `--no-skill` installs the engine only,
`--uninstall` removes the link and never the repo.

**Total download: numpy, scipy, regex.** Nothing else is required, no model is
fetched, and the pipeline makes no network call at any point. The dense encoder
tiers (~2 GB of torch wheels) are strictly opt-in:

```
python install.py --dense      # only if you want the balanced/full tiers
```

Without them the tier auto-routes to `lite`, which is BM25-only and fully
functional — abstention, the entity graph, closure, and calibration all work
unchanged.

### As a Claude Code plugin

If you would rather install through Claude Code's plugin system:

```
/plugin marketplace add viethuynh243/ZeroMem
/plugin install zeromem@zeromem
```

That delivers the skill; run `pip install zeromem` (or `pip install -e .` in a
clone) once for the engine itself.

### Already have it another way?

`pip install git+https://github.com/viethuynh243/ZeroMem` gives you the engine
alone. Verify any install with:

```
zeromem doctor          # or: python -m zeromem doctor
```

## First build

Start with one project rather than the whole corpus:

```
zeromem status                            # what is available
zeromem build --scope <SLUG> --with-graph
```

A full-corpus build here took ~45 minutes for 135,369 units. `build` refuses a
projected encode over 10 minutes unless you pass `--yes-long-build`.

## First recall

```
zeromem recall "what did I do about the ENOENT bug" --top-k 5
```

Optionally start the daemon first — it makes recall ~18× faster by loading the
index once instead of per call:

```
zeromem serve
```

## Keeping it current

```
zeromem update          # incremental refresh + graph rebuild
zeromem update --quiet  # silent when nothing changed
```

Scheduling is documented in `references/usage.md` and deliberately **not**
enabled — a multi-minute background encode is your decision.

## Documentation

- `SKILL.md` — what Claude loads when the skill triggers
- `references/usage.md` — full CLI reference, troubleshooting, scheduling
- `references/architecture.md` — the pipeline stage by stage, mapped to the
  paper's equations, with every deviation stated, plus the alternatives that
  were considered and rejected
- `references/method-notes.md` — what transferred from an earlier project, and
  the two ideas that were measured and rejected anyway

## Measured, not claimed

Every quantitative claim in this project has a report behind it naming its
sample and stating what that sample cannot see. All numbers are my own, taken
on my own machine and my own transcript corpus — they are not the paper's
numbers and are not comparable to them (different corpus, different task,
different metric).

> Project, scope, file and path names appearing in these reports (`TaskBot`,
> `DataHub`, `CalcEngine`, `D--Projects-…`, …) are anonymised placeholders for a
> private corpus. Only the names were substituted; every measured value,
> distribution and verdict is unmodified.

| Report | Measures | Headline |
|---|---|---|
| [`references/tiers.md`](references/tiers.md) | encoder throughput, build wall-clock | 47.3 units/s (balanced, full build) |
| [`references/corpus.md`](references/corpus.md) | ingest profile of the real corpus | 690 files, 1.33 GB, 134,216 units |
| [`references/entities.md`](references/entities.md) | extractor precision, 400-unit sample | 0.884 |
| [`references/routing.md`](references/routing.md) | router accuracy, 40 hand-authored queries | 0.900 |
| [`references/recall-quality.md`](references/recall-quality.md) | recall@k, full vs 3 ablations, 25 queries | see report |
| [`references/latency.md`](references/latency.md) | cold start, daemon, memory | 1.7 s warm vs 34 s cold, 18× |
| [`references/abstention.md`](references/abstention.md) | does it know when it does *not* know | 20/20 unanswerable questions hedged, 0 false answers |
| [`references/method-notes.md`](references/method-notes.md) | outside methods measured against this system | 2 plausible ideas rejected on the numbers |

**It tells you when it does not know.** Ask about something absent from your
history and recall says so, names the terms it could not find, and reports
which of them occur nowhere in your indexed sessions at all — rather than
returning five confident-looking blocks about something else. Measured on 20
answerable + 20 unanswerable questions: every unanswerable one drew a hedge,
none was presented as an answer.

Two retrieval findings are recorded and **not** acted on, because tuning
against a small self-authored set would be overfitting: `graph-only` outscores
`full` on recall@3/5/10, and `no-closure` is numerically identical to `full`.

## Design constraints

- **No new pip installs.** BM25 vendored on `scipy.sparse`, nearest-neighbour by
  chunked numpy matmul, entity extraction by deterministic regex families.
- **`~/.claude/projects` is read-only.** Never written, moved, or deleted.
- **Redaction at ingest is mandatory** and has no off switch — transcripts
  contain real tool output.
- **Deterministic.** Same index + same query + same `--now` ⇒ same evidence, in
  the same order, with the same scores.
- **The ledger writes only under `~/.zeromem/ledger/`.** The coordination
  ledger (`ledger` subcommand, `references/ledger.md`) is the one write path
  besides the index; it reads transcripts and never writes near them.

## License

MIT — see [`LICENSE`](LICENSE).

The Zero-Mem paper (arXiv:2607.29377v1) is the starting point for the
architecture and is credited throughout; it is linked, not redistributed, and
none of its code, data, or results appear here. This repository is my own
independent work.
