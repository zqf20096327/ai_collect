<p align="center">
  <img src="docs/assets/beacon.svg" alt="driftlantern beacon" width="640"/>
</p>

# driftlantern

**A vector snapshot observatory.** driftlantern takes two snapshots of an
embedding space — a *baseline* and a *candidate* — and tells you, in one
number and one word, how far the space has moved. It computes centroid shift,
neighbourhood stability, and per-dimension distribution changes, then blends
them into a single drift score that lands in one of four signal bands:
`stable`, `watch`, `drifting`, or `alarm`.

Embedding models are silent about their own drift. When you re-embed a corpus
with a new model revision, retrain a fine-tune, or rotate a vector store, the
geometry underneath your semantic search or clustering pipeline changes — and
nothing tells you until retrieval quality quietly degrades. driftlantern turns
that invisible change into a report you can read, diff, and gate a CI job on.

It ships as a **Python 3.11 package** with a command-line interface and a
matching **C# net9.0 console analyzer**. Both implementations compute the same
drift score from the same JSON snapshots, so you can embed the observatory in a
Python data pipeline or a .NET service and get identical numbers.

Everything here is standard library. No NumPy, no ML framework, no external
NuGet or PyPI packages. The math is written out explicitly so it can be
audited line by line.

---

## Why it exists

A drift check needs three properties that off-the-shelf "cosine of the mean"
one-liners do not give you:

1. **Scale awareness.** A raw centroid distance of `0.4` means nothing on its
   own — it depends on the magnitude of your vectors. driftlantern normalises
   shift against the baseline's mean magnitude so the signal is comparable
   across models.
2. **Structure awareness.** Two snapshots can share a centroid yet have
   completely reshuffled local neighbourhoods. driftlantern measures
   nearest-neighbour stability with a Jaccard overlap so a reshuffle is caught
   even when the bulk statistics look calm.
3. **Direction vs magnitude separation.** A cloud that grows uniformly is very
   different from a cloud that rotates. The centroid cosine term isolates
   directional change from magnitude change.

The result is a score that reacts to the kinds of drift that actually break
retrieval, not just the ones that are easy to compute.

---

## Architecture

driftlantern is organised as a thin CLI over a pure metric core, with a
parallel C# runtime that reuses the same snapshot contract.

```
                          ┌───────────────────────────────────────┐
                          │              snapshot JSON              │
                          │   { name, dim, vectors:[{id,values}] }  │
                          └───────────────────┬─────────────────────┘
                                              │
                 ┌────────────────────────────┼────────────────────────────┐
                 │                             │                            │
        ┌────────▼─────────┐         ┌─────────▼──────────┐        ┌────────▼─────────┐
        │  Python loader   │         │   metric core      │        │   C# loader      │
        │  model.Snapshot  │         │   metrics.py       │        │  Snapshot.cs     │
        │  strict validate │         │  centroid / cosine │        │  System.Text.Json│
        └────────┬─────────┘         │  knn stability     │        └────────┬─────────┘
                 │                   │  distribution      │                 │
                 │                   └─────────┬──────────┘                 │
                 │                             │                            │
        ┌────────▼─────────┐         ┌─────────▼──────────┐        ┌────────▼─────────┐
        │  Observatory     │         │   DriftReport      │        │  Observatory.cs  │
        │  observatory.py  │────────▶│  score + signal    │◀───────│  same weights    │
        └────────┬─────────┘         └─────────┬──────────┘        └────────┬─────────┘
                 │                             │                            │
        ┌────────▼─────────┐         ┌─────────▼──────────┐        ┌────────▼─────────┐
        │  render.py       │         │   JSON output      │        │  Program.cs      │
        │  box-table view  │         │   (CI ingestible)  │        │  console/json    │
        └──────────────────┘         └────────────────────┘        └──────────────────┘
```

The data flow is deliberately linear: **load → validate → measure → score →
render**. Each stage is a small module you can import on its own.

| Module | Responsibility |
|--------|----------------|
| `driftlantern/model.py` | `Snapshot`, `Vector`, `DriftReport` dataclasses; strict JSON loading and validation. |
| `driftlantern/metrics.py` | Centroid, Euclidean, cosine, magnitude, k-NN stability, distribution and dimension-drift functions. |
| `driftlantern/observatory.py` | Blends metrics into a bounded score and maps it to a signal band. |
| `driftlantern/render.py` | Renders a `DriftReport` as a box-drawn console table with ASCII meters. |
| `driftlantern/cli.py` | `compare`, `summarize`, `version` subcommands with JSON/table output and exit codes. |
| `runtime/Snapshot.cs` | C# snapshot model + `System.Text.Json` loader with identical validation. |
| `runtime/Metrics.cs` | C# port of the metric core. |
| `runtime/Observatory.cs` | C# scoring with the same weights and bands. |
| `runtime/Program.cs` | C# console entry point mirroring the Python CLI. |

---

## Install and build

No dependencies to download. You need Python 3.11+ and the .NET 9 SDK.

```bash
# byte-compile the Python package (compile-only, no tests)
python -m compileall -q driftlantern

# build the C# analyzer in Release
dotnet build runtime/DriftLantern.Runtime.csproj -c Release --nologo
```

Or use the Makefile:

```bash
make build      # compiles both stacks
make run        # runs the fixture example through the Python CLI
make compare    # compares baseline vs the drift candidate
make cs-run     # runs the C# analyzer against fixtures
```

---

## Usage

### Compare two snapshots (Python)

```bash
python -m driftlantern compare fixtures/baseline.json fixtures/candidate-drift.json
```

```
+----------------------------------------------------------+
| driftlantern report  baseline -> candidate-drift         |
+----------------------------------------------------------+
| signal        [>] DRIFTING                               |
| drift score   0.3963  ##########..............           |
|                                                          |
| dimension     4                                          |
| baseline size 8                                          |
| candidate size8                                          |
| shared ids    8                                          |
|                                                          |
| centroid shift    0.3916                                 |
| centroid cosine   0.9898                                 |
| neighbor stability0.3500                                 |
| magnitude delta   +0.0735                                |
+----------------------------------------------------------+
| per-dimension mean delta                                 |
|   dim 0   +0.2562  ######..................              |
|   dim 1   +0.2325  ######..................              |
|   dim 2   +0.1663  ####....................              |
|   dim 3   +0.0775  ##......................              |
+----------------------------------------------------------+
```

### JSON output for pipelines

```bash
python -m driftlantern compare fixtures/baseline.json fixtures/candidate-drift.json --json
```

```json
{
  "baseline": "baseline",
  "candidate": "candidate-drift",
  "dim": 4,
  "baseline_size": 8,
  "candidate_size": 8,
  "shared_ids": 8,
  "centroid_shift": 0.391619,
  "centroid_cosine": 0.989828,
  "neighbor_stability": 0.35,
  "magnitude_delta": 0.073463,
  "signal": "drifting",
  "score": 0.396272
}
```

### Summarise a single snapshot

```bash
python -m driftlantern summarize fixtures/baseline.json
```

```
snapshot: baseline  dim=4  size=8
magnitude mean=0.8949 std=0.0260 min=0.8535 max=0.9224
  dim 0   mean=+0.2763 std=0.3838 min=+0.0400 max=+0.9000
  dim 1   mean=+0.2713 std=0.3745 min=+0.0300 max=+0.8800
  dim 2   mean=+0.2850 std=0.3760 min=+0.0500 max=+0.9100
  dim 3   mean=+0.2588 std=0.3661 min=+0.0200 max=+0.8900
```

### The C# analyzer

```bash
dotnet run --project runtime/DriftLantern.Runtime.csproj -c Release -- \
  fixtures/baseline.json fixtures/candidate-drift.json --json
```

It prints the same score and signal. Use `--k N` to change the neighbourhood
size and `--json` for machine-readable output.

### Tune the neighbourhood size

```bash
python -m driftlantern compare fixtures/baseline.json fixtures/candidate-drift.json --k 5
```

A larger `k` makes the stability metric more forgiving of small local
reshuffles; a smaller `k` makes it more sensitive.

---

## The drift score

The observatory blends three normalised signals:

```
shift_norm        = min(centroid_shift / baseline_mean_magnitude, 1)
direction_penalty = (1 - centroid_cosine) / 2
instability       = 1 - neighbour_stability

score = 0.45 * shift_norm + 0.25 * direction_penalty + 0.30 * instability
```

The score is clamped to `[0, 1]` and mapped to a band:

| Score range | Signal   | Exit code | Meaning                                   |
|-------------|----------|-----------|-------------------------------------------|
| `< 0.10`    | stable   | 0         | Negligible movement; safe to ship.        |
| `< 0.25`    | watch    | 0         | Minor movement; keep an eye on it.        |
| `< 0.50`    | drifting | 3         | Meaningful drift; review before shipping. |
| `>= 0.50`   | alarm    | 4         | Large drift; likely a breaking change.    |

The non-zero exit codes let you gate a CI job directly:

```bash
python -m driftlantern compare baseline.json candidate.json || \
  echo "drift gate tripped with exit $?"
```

Full definitions live in [`docs/metrics.md`](docs/metrics.md).

---

## Signal gauge

<p align="center">
  <img src="docs/assets/gauge.svg" alt="driftlantern signal gauge" width="600"/>
</p>

The needle sweeps from the calm green edge through the amber watch and drift
bands into the red alarm zone — the same four bands the score maps to.

---

## Snapshot format

Snapshots are plain JSON: a name, a dimensionality, and a list of labelled
vectors.

```json
{
  "name": "baseline",
  "dim": 4,
  "vectors": [
    {"id": "doc-alpha", "values": [0.90, 0.10, 0.05, 0.02]},
    {"id": "doc-beta",  "values": [0.85, 0.15, 0.10, 0.05]}
  ]
}
```

Both loaders enforce the same contract: non-empty name, positive `dim`, no
duplicate ids, and every vector matching `dim`. Snapshots need not share ids —
when they differ, the report notes how many ids appeared or were removed and
computes neighbour stability over the shared subset. The full specification is
in [`docs/snapshot-format.md`](docs/snapshot-format.md).

---

## Bundled fixtures

| Fixture | Purpose |
|---------|---------|
| `fixtures/baseline.json` | Four tight clusters across four dimensions. |
| `fixtures/candidate-stable.json` | The baseline with tiny per-value jitter — scores `stable`. |
| `fixtures/candidate-drift.json` | The clusters pulled toward the centre and rotated — scores `drifting`. |

Run both comparisons end to end:

```bash
python examples/run_fixtures.py
```

---

## Design choices

**Standard library only.** The metric core is a few dozen lines of explicit
loops. That keeps the tool auditable and dependency-free, and it makes the
Python and C# ports line-for-line comparable.

**Two runtimes, one contract.** The Python package is the reference. The C#
analyzer exists so the same drift gate can live inside a .NET service without a
Python interpreter. Both read the identical JSON and produce the identical
score — verified on the fixtures (both report `0.3963` for baseline vs
candidate-drift).

**Scale-relative signals.** Every term feeding the score is normalised, so a
threshold you pick on one model transfers to another with different vector
magnitudes.

**Exit codes as a gate.** The CLI encodes the signal in its exit status so a
comparison can fail a pipeline without any extra scripting.

---

## Repository layout

```
driftlantern/
├── driftlantern/            Python package (model, metrics, observatory, cli, render)
├── runtime/                 C# net9.0 console analyzer
├── fixtures/                baseline + stable + drift snapshots
├── examples/                runnable fixture walkthrough
├── docs/                    metrics + snapshot format references, SVG assets
├── .github/workflows/       compile-only CI for both stacks
├── Makefile                 build / run / compare targets
├── CHANGELOG.md
├── ROADMAP.md
└── LICENSE                  Apache-2.0
```

---

## Reporting issues

Bugs and surprising drift readings are both welcome as issues. Please include
the two snapshots (or a minimised version of them) that produced the wrong
score, the command line used, and the expected versus actual signal. Because
DriftLantern is deterministic, a wrong score should reproduce exactly on the
same input, which makes the snapshots plus command a complete bug report.
Security concerns should be reported privately rather than in a public issue;
the repository security policy lists the contact channel.

## License

Apache-2.0. See [`LICENSE`](LICENSE).
