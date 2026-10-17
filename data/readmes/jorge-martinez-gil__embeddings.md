# EmbedCatalog

**A reproducible catalog for choosing embedding layouts under quality, memory,
and latency constraints.**

EmbedCatalog treats post-hoc embedding compression as a physical-design problem
for vector retrieval systems. Given a frozen text embedder, a workload, and
relevance judgments, it evaluates candidate vector layouts, measures retrieval
quality, storage, and latency, and returns a statistically annotated Pareto
catalog that operators can scan against their deployment budget. A small
advisor then answers the deployment question directly: given a RAM budget, a
latency budget, and a quality SLO, which layout is the smallest one that fits,
or which budget is the binding one when nothing fits.

Implementation note: the public method and paper contribution are called
**EmbedCatalog**. The Python package and CLI are exposed as `embedopt` for
backward compatibility with existing scripts, manifests, and experiment logs.

## Why This Matters

Modern retrieval systems often store one dense vector per object. At production
scale, the embedding column can become one of the largest materialized
structures in the system. Choosing between float32, float16, scalar int8 or
int4, binary codes, PQ, OPQ, truncation, or composed layouts is therefore not
just a modeling decision; it is a physical layout decision.

EmbedCatalog answers that decision empirically:

1. Freeze the embedding backbone.
2. Sweep a unified space of post-hoc vector layouts.
3. Measure quality, bytes per vector, and query latency under one protocol.
4. Attach uncertainty with paired bootstrap confidence intervals, paired
   randomization p-values, TOST equivalence verdicts, and codebook seed
   variance.
5. Emit a Pareto-filtered catalog plus reproducible manifests.
6. Query the catalog with a constraint vector to obtain a layout or an
   infeasibility certificate.

## Results At A Glance

The released artifact covers 23 backbone-dataset pairs on BEIR:

| Group | Backbones | Datasets | Pairs |
| --- | --- | --- | --- |
| Main matrix | E5-base, BGE-base, MXBAI-large, GTE-base | SciFact, NFCorpus, ArguAna, FiQA | 16 |
| Larger corpus | E5-base, BGE-base, MXBAI-large, GTE-base | TREC-COVID (171k documents) | 4 |
| High-dimensional backbone | GTE-Qwen2-1.5B (d = 1536) | SciFact, NFCorpus, ArguAna | 3 |

| Finding | Practical reading | Evidence |
| --- | --- | --- |
| Float16 halves storage with absolute nDCG@10 deltas below 1e-3 and passes TOST equivalence on every pair. | A conservative first storage reduction for any vector collection. | `results/tost_float16.csv`, `figures/fig_storage_modes_bar.png` |
| Scalar int8 saves 4x storage and is the smallest layout within 1% of identity nDCG@10 on all 16 main-matrix pairs. | A strong default when memory dominates and exact float scoring is not required. | `tables/main-pareto.tex`, `results/tost_scalar_int8.csv`, candidate CSVs with `ci95_diff_lower`, `ci95_diff_upper`, `p_value`, `significant_05` |
| Scalar int4 saves 8x storage but fails the 1% TOST equivalence test on 8 of 23 pairs, and its per-query dispersion is wider than int8. | Worth testing per collection rather than adopting blindly. | `results/tost_scalar_int4.csv`, `figures/fig_int4_dispersion.png` |
| PQ, OPQ, binary, binary-with-rescore, and truncate-then-PQ reach 48x to 128x reductions at looser quality budgets. | The best aggressive layout depends on backbone, dataset, and budget. | `figures/fig_pareto_quality_storage.png`, `figures/fig_pq_ablation_heatmap.png`, `tables/thresholds.tex` |
| Codebook seed variance for PQ and OPQ is small relative to the layout-to-layout gaps. | Single-seed catalog rankings are stable. | `results/*__seed_variance_summary.csv`, `tables/seed-variance.tex` |
| The float16, int8, and int4 verdicts are stable across corpus sizes from 10k to 171k documents on TREC-COVID. | The scalar results transfer as the collection grows. | `results/corpus_size_ablation.csv`, `tables/robustness.tex` |
| Every reported number is tied to a manifest. | Results are replayable from config, seed, package version, and platform metadata. | `results/*__manifest.json` |

## Claim-To-Artifact Map

| Paper claim | Where to inspect it | How to regenerate |
| --- | --- | --- |
| Unified post-hoc layout search over float32, float16, truncation, int8, int4, binary, binary-with-rescore, PQ, OPQ, and compositions. | `src/embedopt/compression/`, `results/*__candidates.csv` | `python scripts/embed_once.py ...` then `python scripts/run_catalog.py ...` |
| Pareto catalogs over quality and storage, with latency as a diagnostic. | `src/embedopt/moo/`, `results/*__manifest.json`, `figures/fig_pair_pareto_frontiers.png` | `python scripts/refilter_pareto_2d.py --results results` and `python scripts/plot_paper_figures.py` |
| Statistical testing against the uncompressed baseline. | candidate CSV columns `delta_vs_identity`, `ci95_diff_lower`, `ci95_diff_upper`, `p_value`, `significant_05`, plus the `r100_*` columns for Recall@100 | `scripts/run_catalog.py` writes them (`--bootstrap-resamples 5000`) |
| TOST equivalence of the near-lossless codecs. | `results/tost_*.csv`, `tables/tost.tex` | `python scripts/tost_equivalence.py --results results --spec scalar_int8 --metric ndcg` |
| Codebook seed variance for PQ and OPQ. | `results/*__seed_variance_summary.csv`, `tables/seed-variance.tex` | `python scripts/run_seed_variance_cheap.py` (CPU) or `scripts/run_seed_variance_gpu.py` |
| Corpus-size stability of the scalar verdicts. | `results/corpus_size_ablation.csv`, `tables/robustness.tex` | `python scripts/ablate_corpus_size.py --cache-dir cache --results results` |
| Storage-mode view of common vector engines. | `results/storage_modes_comparison.csv`, `tables/storage-modes.tex` | `python scripts/make_storage_modes.py --results results` |
| Constrained layout selection (advisor). | `src/embedopt/pipelines/advisor.py`, `tests/test_advisor.py` | `embedopt advise results/e5-base__scifact__candidates.csv --ram-gb 2 --n-vectors 1000000 --slo 0.99` |
| ANN backend sensitivity. | `results/*__index.csv`, `figures/fig_index_tradeoff.png`, `tables/ann-backends.tex` | `python scripts/run_ann_backends.py --backbones e5-base --datasets scifact` |
| All paper tables. | `tables/*.tex` | `python scripts/regen_tables.py --results results --emit-dir tables` |
| Reproducibility and provenance. | `results/*__manifest.json` | the catalog runner writes manifests automatically |

## Repository Layout

```text
src/embedopt/
  compression/     Vector layout operators: identity, float16, truncation,
                   scalar int8 and int4, binary, binary with rescoring,
                   PQ, OPQ, and composed pipelines
  evaluation/      Retrieval metrics (nDCG@10, Recall@20/100, MRR@10), BEIR
                   loaders, per-query statistics, bootstrap confidence
                   intervals, randomization tests, TOST
  indexing/        Exact NumPy and optional FAISS-family ANN backends
  models/          Hashing, random projection, and sentence-transformer
                   backbones with query/passage prefix handling
  moo/             Pareto filtering, NSGA-II, scalarizers, hypervolume
  pipelines/       Smoke runs, Pareto sweeps, storage-mode comparisons,
                   and the constraint advisor
  profiling/       Bytes per vector, fit/encode time, median and p95 latency
  utils/           Seeding, run manifests, shared types

scripts/
  embed_once.py                 Embed each (backbone, dataset) pair once and cache it
  run_catalog.py                CPU catalog runner over cached embeddings
  run_catalog_gpu.py            PyTorch variant of the catalog runner for CUDA
  run_seed_variance_cheap.py    PQ/OPQ codebook seed variance (CPU)
  run_seed_variance_gpu.py      PQ/OPQ codebook seed variance (CUDA)
  tost_equivalence.py           TOST verdicts for float16, int8, and int4
  ablate_corpus_size.py         Corpus-size ablation of the scalar verdicts
  make_storage_modes.py         Storage-mode table from an existing catalog
  refilter_pareto_2d.py         Re-project catalogs onto the (quality, bytes) frontier
  run_ann_backends.py           FAISS backend comparison on cached vectors
  regen_tables.py               Regenerate every LaTeX table from results/
  plot_paper_figures.py         Publication figure generator
  run_paper_experiments.py      Original end-to-end runner (embeds and evaluates)
  run_all.sh / run_all.bat      One-command wrappers around run_paper_experiments.py
  compare_storage_modes.py      Synthetic float32/float16/int8/binary/PQ comparison
  run_seed_variance.py          Seed-variance ablation for the original runner

results/                        Candidate CSVs, manifests, TOST verdicts, ablations
figures/                        PDF and PNG paper figures
tables/                         LaTeX table bodies ready to \input
tests/                          Offline unit and smoke tests
```

## Quickstart

The offline smoke path needs no GPU and no external benchmark download.

```bash
python -m pip install -e ".[dev]"
pytest
embedopt version
embedopt pareto --dim 128 --seed 0
embedopt storage-modes --dim 128 --seed 0
python scripts/run_catalog.py --selftest
```

Ask the advisor a deployment question over a released catalog:

```bash
embedopt advise results/e5-base__scifact__candidates.csv \
  --ram-gb 2 --n-vectors 1000000 --latency-max-ms 5 --slo 0.99
```

The command prints the smallest-storage layout that satisfies all three
budgets. When none does, it exits with code 2 and reports the minimal
relaxation on each axis that restores feasibility.

## Reproducing The Paper Matrix

The revision workflow separates the single GPU step (embedding) from the
CPU-only analysis so that everything after the embeddings is cheap to rerun.

1. Download the BEIR datasets into `data/` (the `run_all.sh` driver does this
   automatically, or use any BEIR download helper).

2. Embed each pair once and cache the vectors:

   ```bash
   python -m pip install -e ".[paper,index]"
   python scripts/embed_once.py \
     --backbones e5-base bge-base mxbai-large gte-base \
     --datasets scifact nfcorpus arguana fiqa trec-covid \
     --data-dir data --cache-dir cache
   python scripts/embed_once.py \
     --backbones gte-qwen2-1.5b \
     --datasets scifact nfcorpus arguana \
     --data-dir data --cache-dir cache
   ```

3. Build the catalogs, seed-variance runs, TOST verdicts, tables, and figures:

   ```bash
   python scripts/run_catalog.py \
     --backbones e5-base bge-base mxbai-large gte-base \
     --datasets scifact nfcorpus arguana fiqa trec-covid \
     --cache-dir cache --output-dir results
   python scripts/run_catalog.py \
     --backbones gte-qwen2-1.5b --datasets scifact nfcorpus arguana \
     --cache-dir cache --output-dir results
   python scripts/run_seed_variance_cheap.py \
     --backbones e5-base bge-base mxbai-large gte-base \
     --datasets scifact nfcorpus arguana fiqa trec-covid \
     --seeds 0 1 2 3 4 --cache-dir cache --output-dir results
   python scripts/tost_equivalence.py --results results --spec scalar_int8 --metric ndcg
   python scripts/tost_equivalence.py --results results --spec float16 --metric ndcg
   python scripts/tost_equivalence.py --results results --spec scalar_int4 --metric ndcg
   python scripts/ablate_corpus_size.py --cache-dir cache --results results
   python scripts/make_storage_modes.py --results results
   python scripts/regen_tables.py --results results --emit-dir tables
   python scripts/plot_paper_figures.py --results-dir results --output-dir figures
   ```

Every step is resumable: embeddings are cached per pair and completed pairs
are skipped, so an interrupted run can simply be restarted. On a CUDA machine,
`run_catalog_gpu.py` and `run_seed_variance_gpu.py` are drop-in replacements
for their CPU counterparts.

The original end-to-end driver is still available and runs embedding and
evaluation in one process:

```bash
bash scripts/run_all.sh            # Linux, macOS, Colab
bash scripts/run_all.sh --smoke    # tiny offline smoke test
scripts\run_all.bat                # Windows
```

Useful overrides for the driver:

```bash
BENCHMARK_PRESET=beir-small     bash scripts/run_all.sh
BACKBONES="e5-base"             bash scripts/run_all.sh
DATASETS="scifact nfcorpus"     bash scripts/run_all.sh
OUTPUT_DIR=results-2026-05      bash scripts/run_all.sh
SCORE_DEVICE=cuda               bash scripts/run_all.sh
SKIP_INSTALL=1 SKIP_DOWNLOAD=1  bash scripts/run_all.sh
```

## Output Artifacts

For each `(backbone, dataset)` pair, EmbedCatalog writes:

| Artifact | Contents |
| --- | --- |
| `results/<backbone>__<dataset>__candidates.csv` | One row per layout spec with nDCG@10, Recall@20, Recall@100, MRR@10, delta versus identity, 95% bootstrap CI, p-value, bytes per vector, corpus bytes, fit/encode time, and median/p95 query latency. |
| `results/<backbone>__<dataset>__index.csv` | One row per `(layout, backend)` pair with index build time, index size, recall/nDCG, exact-recall, and median/p95 search latency (main matrix). |
| `results/<backbone>__<dataset>__manifest.json` | Config hash, seed, package version, platform info, Pareto labels, hypervolume, and output paths. |
| `results/<backbone>__<dataset>__seed_variance.csv` and `..._summary.csv` | Per-seed and aggregated PQ/OPQ results across codebook seeds. |
| `results/tost_<spec>.csv` and `results/tost_<spec>_r100.csv` | TOST equivalence verdicts per pair on nDCG@10 and Recall@100. |
| `results/corpus_size_ablation.csv` | Scalar int8/int4 verdicts at several corpus sizes. |
| `results/storage_modes_comparison.csv` | The canonical vector-engine storage modes projected from the catalog. |

Generate publication figures from any result directory:

```bash
python scripts/plot_paper_figures.py --results-dir results --output-dir figures
```

Available figure families:

| Figure | Purpose |
| --- | --- |
| `fig_pareto_quality_storage` | Quality versus bytes with Pareto points marked. |
| `fig_pair_pareto_frontiers` | Per-backbone and per-dataset frontier panels. |
| `fig_latency_storage_quality` | Three-objective latency/storage/quality view. |
| `fig_pq_ablation_heatmap` | PQ subspace count versus bit-width ablation. |
| `fig_significance_ci_forest` | Paired-bootstrap confidence intervals. |
| `fig_int4_dispersion` | 90% TOST intervals of per-query delta nDCG@10 for int8 versus int4, per pair. |
| `fig_training_cost` | Compressor fit and encoding cost. |
| `fig_index_tradeoff` | Index bytes versus index nDCG, colored by latency. |
| `fig_storage_modes_bar` | Float32, float16, int8, int4, binary, and PQ comparison. |
| `fig_hypervolume` | Frontier hypervolume per backbone and dataset. |

## Search Space

EmbedCatalog evaluates conservative, aggressive, and composed layouts under the
same interface:

| Family | Examples | Why it is included |
| --- | --- | --- |
| Raw precision | float32, float16 | Baselines and low-risk storage reductions. |
| Dimensional truncation | keep 32, 64, 128, 256, 512 dimensions | Tests whether leading dimensions preserve retrieval structure. |
| Scalar quantization | int8 and int4 affine quantization | Common vector-database storage modes with 4x and 8x footprint reduction. |
| Binary quantization | one bit per dimension, optionally rescored with float16 or int8 | Extreme compression point for loose quality budgets, plus the two-stage variant vector engines ship. |
| Product quantization | PQ with multiple subspace and bit-width settings | Standard codebook-based vector compression. |
| Optimized PQ | OPQ rotation plus PQ | Tests whether learned rotations recover PQ quality at the same byte budget. |
| Compositions | truncate-then-PQ, truncate-then-binary | Explores layout pipelines beyond single operators. |

Each candidate implements `fit`, `transform`, `score`, and
`bytes_per_vector`, so it can be registered, evaluated, stored, and replayed as
a single specification string.

## Storage-Mode Comparison

For practitioners, the repository includes a direct comparison of the storage
layouts that common vector engines expose:

| Mode | EmbedCatalog compressor | Typical production analogue |
| --- | --- | --- |
| float32 | `IdentityCompressor` | pgvector `vector`, Milvus `FLOAT`, FAISS `IndexFlat` |
| float16 | `Float16Compressor` | pgvector `halfvec`, Milvus `FLOAT16`, Qdrant `Float16` |
| int8 | `ScalarQuantizeCompressor` | FAISS `IndexScalarQuantizer`, Milvus `SQ8`, Qdrant `Int8` |
| int4 | `Int4ScalarQuantizeCompressor` | FAISS `QT_4bit` scalar quantizer, Elasticsearch `int4_hnsw` |
| binary | `BinaryQuantizeCompressor` | FAISS binary indexes, Milvus `BIN_*`, Qdrant `Binary` |
| binary + rescore | `BinaryRescoreCompressor` | Qdrant and Weaviate binary quantization with rescoring |
| PQ | `ProductQuantizeCompressor` | FAISS `IndexPQ`, Milvus `IVF_PQ`, OpenSearch FAISS PQ |

Derive the table from an existing catalog, or run the synthetic version
locally:

```bash
python scripts/make_storage_modes.py --results results
python scripts/compare_storage_modes.py --dim 128 --seed 0 \
  --output results/storage_modes_comparison.csv
```

## ANN Backends

The `--index-backends` flag of `run_paper_experiments.py` and the standalone
`scripts/run_ann_backends.py` compare representation choices against several
FAISS-family execution paths:

| Backend | FAISS analogue | Role |
| --- | --- | --- |
| `exact-numpy` | NumPy brute force | Dependency-free reference. |
| `faiss-flat` | `IndexFlatIP` | Exact dense inner product. |
| `faiss-ivf` | `IndexIVFFlat` | Inverted-file approximate search. |
| `faiss-ivfpq` | `IndexIVFPQ` | Inverted-file search with PQ codes. |
| `faiss-hnsw` | `IndexHNSWFlat` | Graph-based approximate search. |
| `faiss-opq` | `IndexPreTransform(OPQMatrix, IndexPQ)` | OPQ rotation plus PQ index. |

This is intentionally a codec-layer and FAISS-layer benchmark. It maps results
to documented production analogues in vector systems, but it does not claim to
benchmark full DBMS products end to end.

## Reproducibility Checklist

| Requirement | Status |
| --- | --- |
| Offline test suite | `pytest` runs deterministic unit and smoke tests. |
| Deterministic seeds | Synthetic data, NSGA-II, random projection, PQ/OPQ fitting, bootstrap, and randomization tests use explicit seeds. |
| Result provenance | Every experiment writes a `RunManifest` with config hash, package version, platform info, and repo state. |
| Resume support | Cached embeddings and completed pairs are skipped on restart. |
| Statistical uncertainty | Candidate CSVs include paired bootstrap CIs and paired randomization p-values; TOST files include equivalence verdicts at two tolerances. |
| Seed variance | PQ and OPQ layouts are re-evaluated across five codebook seeds on every pair. |
| Table and figure regeneration | All LaTeX tables and paper figures are produced directly from result CSVs. |
| CPU fallback | Everything after embedding runs on CPU; `embed_once.py` falls back to CPU when CUDA is absent. |

## CI

GitHub Actions runs:

```bash
ruff check .
black --check .
isort --check-only .
mypy --strict src
pytest
```

## License

This repository is released under the MIT License. See `LICENSE`.
