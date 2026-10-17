<div align="center">

# PromptLedger

Version prompt templates, run deterministic comparison snapshots, score candidate responses, and ship diffable experiment reports.

<img src="docs/assets/pipeline.svg" alt="PromptLedger pipeline: template, ledger, snapshot, score, report" width="100%"/>

`Python 3.11+` · `Go 1.24+` · standard library only · deterministic by construction

</div>

## The problem it solves

A one-word edit to a prompt template can move output quality across an entire evaluation set, and without a durable record you cannot say which revision produced which result. promptledger treats prompts the way version control treats code: every template gets a content fingerprint, every comparison is a repeatable snapshot, and every snapshot renders to a canonical JSON report with a Markdown twin.

Scoring is a pure function of its inputs, so two runs over the same experiment produce byte-identical reports. A diff between yesterday's baseline and today's candidate becomes a mechanical regression signal instead of a judgement call.

## Two tools, one shared invariant

The toolkit is split across two binaries that agree on exactly one thing: the fingerprint algorithm.

- A Python core and CLI author templates, record revisions, run snapshots, and render reports.
- A Go companion, `ledgerctl`, independently verifies a persisted ledger against its sources and diffs two reports.

If the Go tool recomputes the exact digest the Python tool stored, the ledger has not drifted. That cross-language agreement is the whole point. Nothing is needed beyond the two language toolchains: no third-party packages, no network access.

## Vocabulary

| Term | Meaning |
| :--- | :------ |
| Template | Prompt text with `{{ placeholder }}` tokens, carrying a stable SHA-256 fingerprint over its name and normalized body. |
| Fingerprint | `sha256(name + NUL + normalized_body)`. Content derived, timestamp free, reproducible. |
| Ledger | Append-only, idempotent record of every fingerprint seen, with a monotonic revision number, persisted as one JSON document. |
| Case | One evaluation scenario: rendering variables, a reference answer, required keywords, a target length, and candidate responses. |
| Snapshot | A deterministic run of one or more template variants across all cases, with every candidate scored and ranked. |
| Score card | The four-signal breakdown for a candidate plus its clamped weighted total. |
| Report | The canonical `promptledger.report/1` JSON, plus a Markdown projection of the same data. |

## How the pieces connect

```
 templates.json ─▶ template.py ─▶ fingerprint (sha256)
                                       │
                                       ▼
                                   ledger.py ─▶ ledger.json (append-only)

 experiment.json ─▶ snapshot.py ─▶ scoring.py (4 pure signals)
                        │
                        ▼
                    report.py ─▶ *.report.json + *.report.md
                        │
                        │  shared fingerprint algorithm
                        ▼
      ledger/ (Go)  ledgerkit.Fingerprint  must match Python
                    ledgerkit.Verify  ─▶ ledger integrity
                    ledgerkit.Diff    ─▶ leaderboard deltas
                    cmd/ledgerctl: verify · diff · fingerprint
```

The Python side owns authoring and reporting. The Go side owns independent verification. They meet at one contract: the fingerprint function, re-implemented in `ledgerkit.NormalizeBody` and `ledgerkit.Fingerprint` to match `promptledger.template` byte for byte.

## Build

You need Python 3.11+ and Go 1.24+. There are no packages to download.

```bash
# byte-compile the Python package
python -m compileall -q promptledger

# build every Go package and the companion binary
cd ledger && go build ./... && go build -o ledgerctl ./cmd/ledgerctl && cd ..
```

Or use the Makefile:

```bash
make compile   # compile-py + compile-go
make build     # produce ledger/ledgerctl
make sample    # run the end-to-end example
```

## Quick start

```bash
# 1. record template revisions
python -m promptledger commit \
  --templates examples/templates.json \
  --ledger ledger.json

# 2. run a comparison snapshot and render both report formats
python -m promptledger snapshot \
  --experiment examples/experiment.json \
  --out reports --format both

# 3. verify the ledger with the Go tool
ledger/ledgerctl verify -ledger ledger.json -templates examples/templates.json
```

The one-shot equivalent is `python examples/end_to_end.py`.

## The Python CLI

```
python -m promptledger <command> [options]
```

`commit` records template revisions into a ledger, idempotent per fingerprint:

```bash
python -m promptledger commit --templates templates.json --ledger ledger.json
```

```
rev   1  ace9443f9e6d  summarize.v1
rev   2  0f413e564409  summarize.v2
ledger saved -> ledger.json
```

`snapshot` runs a comparison and writes reports. `--format` accepts `md`, `json`, or `both`, and the command prints a leaderboard plus the paths it wrote:

```bash
python -m promptledger snapshot --experiment experiment.json --out reports --format both
```

`score` scores a single candidate file against a reference and emits a JSON score card to stdout:

```bash
python -m promptledger score \
  --candidate answer.txt --reference gold.txt \
  --keyword Perseverance --keyword Jezero --target-words 18
```

`show` lists ledger entries with their variables:

```bash
python -m promptledger show --ledger ledger.json
```

## The Go companion (ledgerctl)

```
ledgerctl <verify|diff|fingerprint> [flags]
```

`verify` recomputes each ledger entry's fingerprint from the source templates and confirms nothing drifted:

```bash
ledgerctl verify -ledger ledger.json -templates templates.json
```

```
checked=2 ok=2 mismatch=0 unmatched=0
ledger integrity verified
```

A non-zero exit with a `MISMATCH` or `UNMATCHED` line signals drift.

`diff` compares two reports and surfaces leaderboard deltas plus changed case winners:

```bash
ledgerctl diff -baseline reports/prev.report.json -candidate reports/new.report.json
```

`fingerprint` computes the content fingerprint for a template body, useful for scripting and for confirming cross-language agreement:

```bash
ledgerctl fingerprint -name summarize.v1 -body-file body.txt
```

## Scoring model

Four deterministic signals, each in `[0, 1]`:

| Signal | Weight | What it measures |
| :----- | -----: | :--------------- |
| `lexical` | 0.45 | Token-set Jaccard similarity to the reference answer. |
| `coverage` | 0.35 | Fraction of required keywords present (case-insensitive substring). |
| `length` | 0.20 | Closeness of word count to a target band `target * (1 ± tolerance)`. |
| `penalty` | subtracted | Deductions for empty output, unbalanced delimiters, truncation markers, and runaway repetition. |

```
base  = lexical*0.45 + coverage*0.35 + length*0.20
total = clamp(base - penalty, 0.0, 1.0)
```

<div align="center">
<img src="docs/assets/score-signals.svg" alt="score composition: lexical, coverage, length stacked, penalty subtracted, clamped to zero and one" width="66%"/>
</div>

The full penalty table lives in [`docs/scoring-model.md`](docs/scoring-model.md). Weights are overridable per case via the experiment's `weights` object.

## Report schema

The canonical artifact is `promptledger.report/1` JSON:

```json
{
  "schema": "promptledger.report/1",
  "experiment": "summarize-v1-vs-v2",
  "leaderboard": [
    { "template": "summarize.v1", "mean_score": 0.9032 }
  ],
  "cases": [
    {
      "case_id": "mars-rover",
      "variants": [
        {
          "template": "summarize.v1",
          "fingerprint": "ace9443f9e6d...",
          "winner": "draft",
          "winning_score": 0.8984,
          "cards": [
            { "candidate_id": "draft", "lexical": 0.824, "coverage": 1.0,
              "length": 0.889, "penalty": 0.0, "total": 0.8984 }
          ]
        }
      ]
    }
  ]
}
```

Field-by-field documentation is in [`docs/report-schema.md`](docs/report-schema.md). The Markdown report is a projection of this structure. When they disagree, the JSON is authoritative.

## Experiment definition

An experiment binds templates to cases:

```json
{
  "name": "summarize-v1-vs-v2",
  "templates": {
    "summarize.v1": { "body": "Summarize in {{ target }} words.\n\n{{ text }}", "tags": ["summarize"] }
  },
  "cases": [
    {
      "id": "mars-rover",
      "variables": { "target": "20", "text": "..." },
      "reference": "expected answer text",
      "keywords": ["Perseverance", "Jezero", "2021"],
      "target_words": 18,
      "candidates": { "draft": "response text", "terse": "..." }
    }
  ]
}
```

Every template is rendered with each case's `variables`. Each case's `candidates` are scored against its `reference`, `keywords`, and `target_words`.

## Worked example

Running `python examples/end_to_end.py` over the bundled fixtures produces a Markdown leaderboard like:

```
| Rank | Template       | Mean Winning Score |
| ---: | :------------- | -----------------: |
|    1 | summarize.v1   |             0.9032 |
|    2 | summarize.v2   |             0.9032 |
```

and a per-case table that explains why each winner won. The `broken` and `repetitive` candidates in the `cache-policy` case intentionally trip the structure penalty (unbalanced parenthesis with truncation, and runaway repetition), so they never win. That is a concrete demonstration that the penalty term does real work.

## The determinism contract

PromptLedger makes one promise: identical inputs yield identical outputs.

- No wall-clock timestamps enter a fingerprint or a report body.
- No randomness is used in rendering or scoring.
- All floats are rounded to six decimals before serialization.
- Ranking uses a total order (`-total`, then `candidate_id`), so insertion order never affects results.
- Ledger revisions derive from insertion order, and fingerprints from content alone.

This is what makes `ledgerctl diff` trustworthy: any change it reports is caused by a real change in templates, candidates, or scoring, never by nondeterminism.

## Repository layout

```
promptledger/
├── promptledger/            Python package (stdlib only)
│   ├── __main__.py          CLI: commit / snapshot / score / show
│   ├── template.py          placeholder engine + fingerprints
│   ├── ledger.py            append-only revision store
│   ├── scoring.py           four deterministic signals + ScoreCard
│   ├── snapshot.py          deterministic comparison runs
│   └── report.py            Markdown + JSON renderers
├── ledger/                  Go module (own go.mod)
│   ├── ledgerkit/           fingerprint + verify + diff (library)
│   └── cmd/ledgerctl/       CLI: verify / diff / fingerprint
├── examples/                fixtures + end-to-end driver
├── docs/                    scoring model, report schema, workflow, assets
├── Makefile
└── LICENSE                  Apache-2.0
```

## Extending it

Add a scoring signal by writing a pure function in `promptledger/scoring.py` that returns a float in `[0, 1]`, adding it to `ScoreCard` with a weight, and updating `total`. Keep it deterministic, with no clocks and no randomness.

Add a report format by rendering from a `Snapshot`; a `render_html(snapshot)` can reuse `_leaderboard(...)` and the same case iteration.

Add a `ledgerctl` subcommand by registering it in `ledger/cmd/ledgerctl/main.go` and putting the logic in `ledger/ledgerkit` so it stays testable in isolation. Walking a template's revision chain as a `history` command is a natural next step.

If you must change the fingerprint, change it in both `promptledger/template.py` and `ledger/ledgerkit/verify.go` together, then run `ledgerctl verify` to confirm the two implementations still agree.

## Design notes

- Two languages, one invariant. Python is ergonomic for authoring and text rendering; Go produces a single static binary suited to a CI verification gate. The fingerprint is the seam that keeps them honest.
- JSON everywhere. Ledgers and reports are plain JSON so they diff cleanly in version control and need no bespoke parser.
- Strict rendering. A missing placeholder value or an unused variable is an error, not a warning, so experiments never drift silently.
- Penalties over hard rejects. Malformed output loses points rather than being dropped, so a report still shows how badly a candidate failed.

## License

Apache-2.0. See [LICENSE](LICENSE).
