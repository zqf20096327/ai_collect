# Kimi K3 — a from-scratch implementation

An implementation of the architecture, pre-training protocol, systems co-designs,
and post-training framework described in *Kimi K3: Open Frontier Intelligence*
(arXiv:2607.24653v1).

Scale is configuration. Nothing in `kimi3/` branches on model size, so the same
code path runs a 20M-parameter model on a laptop CPU and describes the paper's
2.8T configuration. This repository executes the small end and the verification
suite. Training at cluster scale is out of scope, and `docs/PAPER_MAP.md` marks
which components are wired into a runnable path and which are libraries.

Parameter counts reproduce the paper's Table 1:

| | This implementation | Paper (Table 1) |
|---|---|---|
| Total parameters | 2.778 T | 2.78 T |
| Activated per token | 104.108 B | 104.2 B |
| Vision tower | 400.9 M | 401 M |

## Requirements

Python ≥ 3.10, PyTorch ≥ 2.4. **No GPU is required.** The test suite, the
parameter audit of the 2.8T config, the demos, and the nano training run all
complete on CPU.

A GPU is used when one is available: `resolve_device("auto")` selects CUDA if the
card has enough free memory, and falls back to CPU otherwise. Training is roughly
7× faster per step on a small GPU. Triton is optional; the fused KDA path falls
back to the reference implementation when it is absent, and never runs during
training because it has no fused backward pass.

```bash
pip install -e .          # runtime
pip install -e '.[dev]'   # adds pytest
```

Optional extras: `[hf]`, `[vision]`, `[triton]`.

## Quick start

```bash
# Inspect the 2.8T configuration without allocating anything
python3 scripts/count_params.py configs/k3_2p8t.yaml --check

# Train the nano model end to end (CPU is fine)
bash scripts/train_nano.sh

# Train on your own data: a text directory, a JSONL file, or packed shards
python3 -m kimi3.train.pretrain --config configs/k3_nano.yaml --jsonl corpus.jsonl

# Run the full gate suite
bash scripts/verify.sh
```

## Common scripts

These run against the published `checkpoints/nano-3000.pt`; swap in your own
`runs/<name>/<name>.pt` once you have trained one.

```bash
# Generate text from a checkpoint
python demos/1_complete.py --checkpoint 3000 --prompt "John looked at Sam and said " --temperature 0.25 --n 60 --seed 7

# Serve the model through an OpenAI-compatible API (defaults to the same checkpoint)
python scripts/serve_openai.py --config configs/k3_nano.yaml --checkpoint checkpoints/nano-3000.pt

# Continue training from a *training* checkpoint -- one saved by the trainer, with
# optimizer state and a step counter; the published weights-only files cannot resume
python scripts/continue_train.py --config configs/k3_nano.yaml --resume runs/nano/k3_nano.pt --text-dir training_data/text --steps 1000 --out runs/nano/k3_nano-2.pt
```

Five runnable demos are in `demos/`, including a trained 19.8M model generating
Python and a side-by-side comparison of models trained on real versus synthetic
data. See `demos/README.md`.

Raw-text preprocessing uses exact SHA-256 deduplication and an incremental
per-file cache by default. The cache lives under the configured `out_dir`; use
`--dedupe fuzzy` when near-duplicate filtering is needed, or `--no-cache` to
disable reuse.

## Results

The nano model trains from a loss of 8.13 to 0.32 in 400 steps on synthetic
data, starting at `ln(vocab)` as expected for correct initialisation.

On a real corpus -- 47,902 documents of system documentation and source code,
deduplicated and split so no held-out document shares a near-duplicate cluster
with training data -- 3,000 steps give:

| Metric | Start | End | Reference |
|---|---|---|---|
| Held-out loss | 6.2726 | 0.8434 | 6.238 = chance |
| Parser-valid generations | 0.1389 | 0.7021 | 0.8182 = training corpus |

The model reaches 86% of the parser-validity rate of its own training data, and
remains significantly below it (z = −2.23 over 480 generations). `docs/RESULTS.md`
Phase 9 documents the scorers, confidence intervals, and why a dictionary
word-rate metric is not a quality measure on its own.

## Architecture

Implemented from paper §2:

- **Kimi Delta Attention** with the lower-bounded decay of Eq. 5 and a full-rank
  output gate.
- **Gated MLA**, with NoPE (no positional encoding) throughout.
- **Block Attention Residuals**.
- **Stable LatentMoE** with SiTU-GLU and Quantile Balancing.
- **MoonViT-V2**, trained from scratch under next-token prediction.

At the 2.8T configuration:

**Hybrid attention schedule.** `hybrid_ratio: 3` with `trailing_global: true`
lays out 93 layers as 23 × [KDA, KDA, KDA, MLA] plus a trailing MLA: 69 KDA and
24 MLA layers, so the tail carries two consecutive MLA layers. Under NoPE,
position information enters the model only through KDA's recurrent decay.

**LatentMoE.** 896 routed experts at top-16 (sparsity 56), plus two always-on
shared experts and one leading dense FFN layer. Routing is dropless: there is no
capacity factor in the config, every token emits exactly top-k assignments, and
all of them are computed. Empty experts are skipped; tokens are not. The router
scores the full-width d = 7168 token. The 3584-wide latent reduces expert compute
and dispatch payload without shrinking the routing space. The Quantile-Balancing
bias is a buffer rather than a parameter: mean-centred, applied one optimizer
step late, and frozen at inference.

**Block Attention Residuals.** 8 blocks of 12 layers, so at most eight completed
block sources, one partial sum, and the embedding are resident simultaneously —
`O(N·d)` live memory instead of `O(L·d)`. Across pipeline stages, `AttnResCache`
transfers only the blocks the current stage created.

## Pre-training (§3)

Per-Head Muon, cosine schedule with 1% warmup, the four-stage 8K → 64K → 256K →
1M context curriculum, and document-isolated packing.

## Infrastructure (§5)

KDA Context Parallelism (Eq. 17), MoonEP with the appendix E bound on redundant
experts, Pipeline ZeRO-2 with CPU-resident gradient shards, P2P Muon
orthogonalisation, block-wise FP8 activations, a unified activation manager, and
cache-based AttnRes pipeline communication.

**These are verified components, not an assembled distributed trainer.** Each is
tested against a single-process reference, and KCP and P2P Muon run under real
`torchrun` processes. However, `kimi3/train/pretrain.py` still imports nothing
from `kimi3/parallel/`, and its optimizer step is single-process. The only
multi-process work it does is raw-text preprocessing — up to four worker
processes reading, filtering and tokenising files before training starts; pass
`--workers 1` to disable it or `--workers N` to tune it.

Two components are accounting rather than transport:

- MoonEP's dispatch and combine are a local permutation with no `all_to_all`.
- The pipeline schedule computes stage partitions and transfer byte counts
  without moving activations.

`docs/PAPER_MAP.md` records the status of each component, and
`tests/test_reachability.py` enforces it: a module that nothing calls fails the
suite unless it is listed with a reason.

## Post-training (§4)

The XTML chat template from appendix F, SFT with MXFP4/MXFP8 quantisation-aware
training, partial rollout, per-problem reasoning-effort budgets producing nine
domain × effort experts, an agentic generative reward model, Multi-Teacher
On-Policy Distillation, and resumable sandboxes.

## Serving (§5.4)

A unified paged cache for the hybrid KDA–MLA state, KDA-aware prefix caching with
decoupled hash and physical granularities, ReplaySSM speculative decoding, and an
EAGLE-3 draft model trained with the LK loss. A single `PagePool` serves both
MLA-KV and KDA-state pages. It is sized by constructor argument, has no YAML
binding and no eviction policy, and raises `MemoryError("page pool exhausted")`
at the limit.

## Verification

The reference implementations define the intended behaviour; the kernels are
optimisations of them. The main gates are therefore equivalence checks:

| Gate | Result |
|---|---|
| KDA chunkwise form vs Eq. 1 recurrence (fp64) | 6.7e-16, all chunk sizes, with and without document resets |
| KDA Context Parallelism vs single-device states | 4.86e-16 across four processes |
| MoonEP balance within the appendix E bound | 200/200 randomised skewed routings, including all-to-one |
| Block AttnRes at block size 1 vs unblocked Eq. 8–9 | exact |
| Triton kernel vs reference | 5e-4, cosine similarity 1.000000 |

For comparison, the naive additive scheme used for vanilla linear attention is
wrong by over 10% on the KCP test case. That error is the reason KCP exists.

Run everything with `bash scripts/verify.sh`. This includes 322 unit and
equivalence tests, three multi-process `torchrun` gates, and the Triton kernel
check.

## Scale ladder

| Config | Total | Activated | Purpose |
|---|---|---|---|
| `k3_nano` | 19.754 M | 8.744 M | correctness proof |
| `k3_micro` | 999.755 M | 273.092 M | multi-process parity, 64K context |
| `k3_small` | 14.452 B | 1.995 B | first multi-node run |
| `k3_2p8t` | 2.778 T | 104.108 B | the paper's configuration |

Every figure is `scripts/count_params.py` output rather than an estimate.

`docs/SCALING.md` covers choosing `PP × EP × CP × DP` degrees and the failure
modes to expect. `docs/HARDWARE.md` derives memory, cluster size, interconnect,
and cost for each rung.

## Not implemented

- **Training a 2.8T model, or reproducing any benchmark score.** The proprietary
  corpora and in-house evaluation suites are not available.
- **A multi-node launcher.** No Slurm, Ray, or `torchrun --nnodes` path exists.
  The only distributed entry points are the three single-node parity gates in
  `scripts/verify.sh`, which run on gloo.
- **An SFT or RL entry point.** `kimi3/posttrain/sft.py` and `kimi3/posttrain/rl/`
  export pure functions — losses, schedulers, reward models — with no `main`, no
  CLI, and no optimizer step. MXFP4/MXFP8 QAT is wired into the expert forward and
  tested by `tests/test_qat.py`, but nothing enables it automatically.
- **MoE all-to-all.** MoonEP plans and balances the expert assignment; the token
  exchange itself is a local permutation.
- **A fused backward pass for the Triton KDA kernel.** The kernel therefore never
  runs during training: the module upcasts to fp32 and the fused path declines any
  call requiring gradients.
- **The Firecracker backend for AgentENV.** What exists is an in-process lifecycle
  state machine (`start/pause/resume/fork/snapshot/destroy` over a dictionary)
  that executes no code. The repository contains no `subprocess`, `exec`, or
  `os.system` call, and the `Sandbox` protocol has no execute method. A real
  backend would need to define its isolation contract — process, filesystem,
  network, timeout, teardown — before running model-generated code.
- **A vision pathway in the trained model.** `kimi3/vision/` implements MoonViT-V2
  and is tested against the paper's parameter count, but `kimi3/model.py` does not
  import it. The backbone is text-only.

## Documentation

| File | Contents |
|---|---|
| `docs/PAPER_MAP.md` | every paper section mapped to its implementation and test |
| `docs/RESULTS.md` | measured results for every gate |
| `docs/AMBIGUITIES.md` | the nine fields Table 1 leaves unspecified, and the evidence for each default |
| `docs/SCALING.md` | parallelism degrees and failure modes |
| `docs/HARDWARE.md` | memory, cluster size, and cost per rung |
| `demos/README.md` | five runnable demonstrations |

## Licence

Copyright © 2026 Tim Rots.

Licensed under the **GNU Affero General Public License, version 3 or later**
([`LICENSE`](LICENSE)). You may use, study, modify and redistribute this code.
If you modify it and make it available to others — including over a network, as
a hosted service — you must release your complete source under the same licence.

That is deliberate. The AGPL does not forbid commercial use; it forbids building
a closed product on this work. Anyone is free to run it, learn from it, and
contribute back.

**Commercial licences are available.** If the AGPL's source-disclosure
requirement does not suit your organisation, contact the author to arrange
alternative terms.

### What the licence does not cover

- **The Kimi K3 architecture.** This is an independent implementation of a public
  paper (arXiv:2607.24653v1). The licence covers this source code, not the ideas
  or the paper, which belong to their authors.
- **Model weights.** Any checkpoint produced by training this code inherits
  obligations from the data it was trained on. The demo weights come from a
  corpus that is roughly 69 % copyleft-licensed by document count; the legal
  status of weights derived from such data is unsettled and is not resolved by
  this licence. No trained weights are distributed in this repository.
