# DGX Spark Unsloth Lossless Speedup

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Hardware: DGX Spark](https://img.shields.io/badge/hardware-NVIDIA_DGX_Spark_(GB10)-76b900)]()
[![Compute: sm_121a](https://img.shields.io/badge/compute-sm__121a-76b900)]()
[![LoRA: 7.67×](https://img.shields.io/badge/LoRA-7.67×_faster-brightgreen)]()
[![Full FT: 8.35×](https://img.shields.io/badge/Full_FT-8.35×_faster-brightgreen)]()
[![Quality: lossless](https://img.shields.io/badge/quality-bit--identical_loss_curve-success)]()
[![Models: Qwen3.5 0.8B → 27B](https://img.shields.io/badge/models-Qwen3.5_0.8B_→_27B-blue)]()

**Train Qwen3.5 fine-tunes on NVIDIA DGX Spark at wall-clock parity with a rented H100 — on hardware you already own.**

This project takes stock Unsloth on DGX Spark from "barely runs" to **7.67× faster LoRA** and **8.35× faster Full Fine-Tuning** on real multimodal Qwen3.5-2B, with the loss curve verified bit-identical to the unoptimized reference within BF16 precision. Measured numbers, not synthetic: 3461 tok/s LoRA and 3173 tok/s Full FT on 24,315 real chat examples (pack 5376, batch 1, gradient accumulation 16).

## How it compares

> _Same training job — 25k × 3 epochs of real multimodal Qwen3.5-2B (~73M tokens). Four setups._

|     | Setup | Hardware | LoRA tok/s | Wall-clock | Cost per retrain |
|:---:|---|---|---:|---:|:---:|
| 🐢 | Stock Unsloth | DGX Spark (GB10) | 451 | ~5 days | 🟢 **$0** |
| 🚀 | **This project** | **DGX Spark (GB10)** | **3,461** | **~20 h** | 🟢 **$0** |
| ☁️ | Unsloth | H100 80GB *(rented)* | ~1.5–2× ours¹ | ~15–20 h | 🔴 **~$50**² |
| ☁️ | Unsloth | A100 40GB *(rented)* | ~0.5× ours¹ | ~1.5–2 days | 🔴 **~$45**² |

<div align="center">

### Same ~20 hours of training. **$50 on a rented H100. $0 on your DGX Spark.**

> ### 💰 Run your DGX Spark 24/7 — it pays for itself in **just ~79 days.**
> $4,699 hardware ÷ $2.49/h H100 rental = **1,887 H100-hours ≈ 11 weeks of nonstop training**.  
> Every day after that is pure savings — and your training data **never leaves the box.**

</div>

<sup>¹ Throughput on rented H100/A100 estimated from public transformer-training benchmarks (Unsloth blog, Modal docs); no canonical single-number Qwen3.5-2B LoRA H100 benchmark exists. Wall-clock estimate scales H100 ≈ 1.5–2× DGX Spark BF16 throughput, A100 ≈ 0.5×.  
² Cost math: 20-hour wall-clock × $2.49/h (Lambda H100 80GB on-demand, May 2026). Other providers: RunPod $2.39–$2.69/h, Spheron $2.01/h SXM. A100 40GB at $1.10–$1.29/h × ~36 h. Break-even = $4,699 MSRP ÷ $2.49/h ÷ 24h/day ≈ 79 days continuous training.</sup>

---

## Quick Start — three commands, zero config

```bash
git clone https://github.com/albond/DGX_Spark_Unsloth_Lossless_Speedup.git
cd DGX_Spark_Unsloth_Lossless_Speedup
./run.sh
```

<div align="center">

**📦 Docker build** ─→ **🤖 Pick model** ─→ **📊 Validate data** ─→ **⏱ Time estimate** ─→ **🔥 Train** ─→ **⚡ MTP head** ─→ **✅ `vllm serve`-ready**

</div>

The wizard runs the whole pipeline. First run builds the optimized image (~30 min); every run after reuses it (~10 s). All knobs — `pack_length`, `epochs`, LoRA vs Full FT — auto-recommended from your data and overridable before launch.

For Qwen3.5 bases the wizard also offers Step 6 — attach an MTP speculative head for **lossless** inference speedup (bit-exact at temperature=0 via vLLM's rejection sampling). Pick **trained** (warm-start on your data, time scales with dataset — minutes on a few hundred examples, several hours on 20k+; typically 2–3× serving throughput) or **upstream-only** (inject Qwen3.5's stock MTP head as-is, ~1 min, modest free speedup). See [Lossless inference speedup — MTP speculative head](#lossless-inference-speedup--mtp-speculative-head). Non-interactive flags in [Detailed setup](#detailed-setup).

<sub>[Hardware requirements](#prerequisites) · [Supported models](#supported-models) · [Detailed speedup numbers](#speedup-details) · [MTP speculative head](#lossless-inference-speedup--mtp-speculative-head) · [What changed and why](#what-changed-and-why)</sub>

---

## Why this matters: the small-model workflow

Pay-per-token frontier models and 100B+ open-weight generalists are expensive and slow at scale. The honest alternative — distilling a small specialist from your own collected interactions — is gated by two things:

- **Data volume.** A usable LoRA on a 2B-class model wants tens of thousands of training examples; a usable full fine-tune wants hundreds of thousands.
- **Training time.** At stock Unsloth throughput on DGX Spark, that's *weeks to months* per training round, with no guarantee the result is good enough.

The cost arithmetic that actually matters (real multimodal Qwen3.5-2B, mean ~3000 tokens/example):

| Dataset × epochs | Mode | Stock Unsloth on DGX Spark | This project on DGX Spark | H100 rental for the same job |
|---|---|---:|---:|---:|
| 25k × 3 | LoRA r=128 | **~5 days** | **~20 hours** | $50–60 |
| 100k × 3 | LoRA r=128 | **~20 days** | **~3 days** | $200–250 |
| 100k × 3 | Full Fine-Tuning | **~25 days** | **~3 days** | $200–300 |

A 25k-example specialist trained in under a day is the threshold where this becomes a real workflow:

1. **Train a specialist** on whatever data you have today. Expect roughly 60% production-acceptable on the first pass — quality grows sublinearly with data, so going from 60% to 80% takes much more than 2× the data.
2. **Serve it as the primary** in production with a validator (cheap classifier or rules) on the output.
3. **Route the 30–40% that the validator rejects** through the slow/expensive path (paid LLM, larger model) and **harvest those interactions** as the next round of training data.
4. **Retrain when you've collected another batch.** With this project's throughput, that loop runs in days, not months.

The bottleneck after that point is data collection and model-architecture design — both out of scope here.

---

## What this project does and doesn't

**Does:**
- Replace the unoptimized Unsloth training path with a vanilla-PyTorch loop and sm_121a-aware Triton kernels.
- Preserve the loss curve bit-identical to the unoptimized reference (verified by per-step A/B comparison on real fine-tuning data).
- Document every optimization that worked and every one that didn't, so you can audit and customize.

**Doesn't:**
- Change the model. No vocabulary trimming, no pruning, no distillation, no experimental optimizers, no RLHF. The math is exactly the math the unoptimized stack would have done.
- Help with inference / serving optimization (vLLM, INT4, deployment). That's a separate concern.
- Promise the speedup ports to non-Qwen models without measurement. Numbers here are measured on a Qwen3.5-2B-shape model; the *techniques* generalize, but please verify on your actual model.

---

## Supported models

The wizard's model picker (Step 1) offers five **measured-and-validated** Qwen3.5 sizes plus an "Other" option for any Qwen-compatible model you bring yourself. All numbers below come from real end-to-end smoke tests on DGX Spark (GB10, 128 GB unified, `test_30.jsonl`, pack_length=2048, gradient_accumulation=2):

| Picker | Model | BF16 weights | Measured tok/s (LoRA) | LoRA fits | Full FT fits |
|---:|---|---:|---:|---|---|
| `1` | Qwen3.5-0.8B | 1.8 GB | **5,650** | ✓ | ✓ |
| `2` | Qwen3.5-2B *(measured anchor)* | 4.4 GB | **3,568** | ✓ | ✓ |
| `3` | Qwen3.5-4B | 9.0 GB | **1,712** | ✓ | ✓ |
| `4` | Qwen3.5-9B | 18.0 GB | **1,095** | ✓ | ✗ |
| `5` | Qwen3.5-27B | 54.0 GB | **370** | ✓ *(pack ≤ 1024 only)* | ✗ |
| `0` | Custom HF id or local path | — | scaled from 2B by parameter count | depends on size | depends on size |

The wizard validates anything you pass under `0`: it reads the model's HF config without downloading the weights, checks that `model_type` (or `text_config.model_type` for multimodal) is one of `qwen2`, `qwen3`, `qwen3_5`, `llama`, `mistral` (or any architecture with Qwen-style `q_proj`/`k_proj`/`v_proj`/`o_proj`/`gate_proj`/`up_proj`/`down_proj` linear naming), and estimates a parameter count for the ETA. Models the wizard doesn't recognise are confirmed with you before training starts.

**Speedup numbers in this README are anchored on Qwen3.5-2B** — that's the only model where the full Path-A-vs-Path-B comparison was run end-to-end. The four other catalog sizes are calibrated relative to that anchor; the calibration error is within ±25% (always in the safe-overestimate direction).

---

## Speedup details

Measured on a real NVIDIA DGX Spark (GB10, sm_121a). All numbers eager-mode, batch size 1, single GPU. Anchor row is **stock Unsloth out of the box** — what you get when you `pip install unsloth` and follow the official getting-started.

### Real multimodal Qwen3.5-2B (production target — chat fine-tuning)

The full multimodal `Qwen/Qwen3.5-2B` checkpoint (6 Attention + 18 GatedDeltaNet/SSM layers + vision encoder) trained on real chat JSONL. Sequence length 5376 packed, gradient accumulation 16. Measured on `valid_full.jsonl` (24,315 examples).

#### LoRA r=128 (default mode for ≤ 50k examples)

| Stack | Step time | tok/s | Speedup vs stock |
|---|---:|---:|---:|
| Stock Unsloth + gc=True (Baseline v0) | ~191 s | 451 | 1.00× *(anchor)* |
| Path B (StaticLoRA + silu_mul) without SSM fast path | ~170 s | 505 | 1.12× |
| Path B + SSM fast path — opt-in via `--static-lora` | 28.0 s | 3076 | 6.82× |
| **Unsloth PEFT + SSM fast path (production default)** | **24.85 s** | **3461** | **7.67×** |

#### Full Fine-Tuning (≥ 100k examples with ≥ 200M tokens)

| Stack | Step time | tok/s | Speedup vs stock |
|---|---:|---:|---:|
| Stock Unsloth + gc=True (Baseline v0, estimated) | ~240 s | ~380 | 1.00× *(anchor)* |
| `wrap_full_ft` + SSM fast path — opt-in via `--wrap-full-ft` | 27.0 s | 3186 | 8.38× |
| **Native Unsloth + SSM fast path (production default)** | **27.1 s** | **3173** | **8.35×** |

The decisive change: Qwen3.5 is a hybrid (75% of its decoder layers are GatedDeltaNet/SSM, not Attention). Without `flash-linear-attention` + `causal-conv1d`, those 18 layers fall back to a pure-PyTorch implementation that dominates the step time. Once they're installed (the wizard's Dockerfile now bakes them in), the SSM math runs on optimized kernels and stops being the bottleneck.

A second finding from this phase: on top of the SSM fast path, Unsloth's own `torch.compile`-friendly forward beats the hand-written StaticLoRA + silu_mul kernels by +12% (3461 vs 3076 tok/s). The custom kernels are still shipped — they remain the best path for users on vendored stacks where compile can't run — but the production default now uses Unsloth's PEFT injection, gated by `--static-lora` for users who prefer the custom Path B.

For other Qwen3.5 sizes the speedup ratio over their stock-Unsloth baseline should be similar (same kernel path applies), but the full stock-vs-fast comparison was only run on the 2B model.

### Synthetic upper bound (no SSM, text-only Qwen-shape)

Reference numbers on the stripped-down `qwen_minimal_bench` — 28 dense attention layers with no SSM, no vision encoder, no chat-template tokenization. This isolates the kernel-level speedup ceiling:

| Stack | Step time | tok/s | Speedup vs stock |
|---|---:|---:|---:|
| Stock Unsloth (Baseline v0, synthetic) | ~7300 ms | 701 | 1.00× |
| Drop-in tuning (Path A) | ~5980 ms | 856 | 1.22× |
| Vanilla-PyTorch loop + fused kernels (Path B) | **1524 ms** | **3361** | **4.80×** |

Real multimodal (3076 tok/s) is now within 10% of the synthetic ceiling — meaning the production code path is essentially as fast as the kernels physically allow on this hardware.

### Full Fine-Tuning (synthetic, real-multimodal bench pending)

| Stack | Step time | tok/s | Speedup vs stock |
|---|---:|---:|---:|
| Stock Unsloth (Baseline v0, synthetic) | ~9050 ms | 565 | 1.00× *(anchor)* |
| Drop-in tuning | ~7180 ms | 713 | 1.26× |
| Vanilla-PyTorch loop + fused kernels | **1480 ms** | **3459** | **6.12×** |

Full FT uses the same model-loading path as LoRA, so the SSM fast-path lift applies symmetrically.

### Time savings on a real training run

Real multimodal Qwen3.5-2B, mean example length ~3000 tokens (the dataset that motivated this project — 24k examples, ~73M tokens total).

| Run size | Mode | Stock Unsloth | This project | Saved |
|---|---|---:|---:|---:|
| 25,000 examples × 3 epochs | LoRA | ~5 days | **~20 hours** | **~4 days** |
| 25,000 examples × 3 epochs | Full FT | ~6 days | **~20 hours** | **~5 days** |
| 100,000 examples × 3 epochs | LoRA | ~20 days | **~3 days** | **~17 days** |
| 100,000 examples × 3 epochs | Full FT | ~25 days | **~3 days** | **~22 days** |

Numbers include real-world overhead (data loading, JIT warmup, checkpoint save). Pure step-time speedup is the table above.

---

## Loss is preserved

Every optimization that lands here passes a per-step A/B test against the unoptimized reference on real fine-tuning data:

- Training loss curve over a 30-step reference run stays bit-identical (rel difference 0.000% at every step within BF16 precision).
- Same initialization, same data, same optimizer, same seed.
- No NaN, no instability, no silent dtype drift.

The bench's loss curve in synthetic mode is bit-identical to the unoptimized reference; a per-step A/B comparison on real-data fine-tuning (separate evaluation rig) confirms the same for production data.

Optimizations that fail this gate are documented as "evaluated, rejected" so you can skip them — see [What didn't ship](#what-didnt-ship).

---

## Lossless inference speedup — MTP speculative head

Training speed is one half; serving speed is the other. As a final Step 6, the
wizard attaches a Multi-Token Prediction (MTP) head to the merged base so vLLM
can use it for **speculative decoding** — **bit-exact by construction** at
temperature=0 because rejection sampling discards every mismatched draft, and
accepted tokens equal what the plain base would have produced.

Qwen3.5 ships an MTP head on HuggingFace, which makes two flavours practical:

| Mode | What happens | Added wall-clock | Speedup at inference |
|---|---|---|---|
| **Trained MTP** (`y`) | Warm-start the upstream MTP head on the fine-tuned base for one epoch, then inject. | scales linearly with tokens × epochs — see table below | typically 2-3× tokens/s |
| **Default MTP** (`d`) | Extract the upstream MTP head and inject it as-is, no training. | ~1 min | modest, but free |
| **Skip** (`n`) | No MTP step at all — plain BF16 serving. | 0 | 1× |

The wizard asks on Step 4 (Recommended configuration), so the ETA you see
before training already includes the MTP cost (computed for one warm-start
epoch on the actual token count of your dataset). The merged BF16 base is
produced regardless of MTP outcome; if the MTP step fails, the base is still
usable for plain `vllm serve`.

#### Trained-MTP wall-clock — measured examples on DGX Spark

MTP training runs at pack_length=8192 over the assistant tokens in your
dataset; throughput on Qwen3.5-2B is steady-state ~8 000 tok/s with the
default `lm_head_opt` ON (see `mtp/RESULTS_SM121.md`). Real-world numbers:

| Dataset | Mean tokens/example | Epochs | Wall-clock |
|---|---:|---:|---:|
| 30 examples (`test_30.jsonl`, smoke) | ~5 400 | 1 | ~3 min |
| 24k long chat examples | ~3 500 | 1 | ~3 h |
| 22k long chat examples (measured, May 2026) | ~3 500 | **2** | **~5 h** |

For each extra epoch the time roughly doubles, so the warm-start default of
`num_epochs=1` is what the wizard's ETA shows. If you change it in
`mtp/train_mtp.sh` or pass a different value, scale the estimate accordingly.

The output directory layout depends on the mode:

```
output/{run}/              # merged BF16 base (always produced)
output/{run}-mtp/          # trained-MTP injection target (mode = trained)
output/{run}-mtp-default/  # upstream-MTP injection target (mode = default)
```

Serve with:

```bash
vllm serve output/{run}-mtp/ \
    --speculative-config '{"method":"mtp","num_speculative_tokens":2,"model":"output/{run}-mtp/"}'
```

The MTP step auto-skips for non-Qwen3.5 bases (vLLM's MTP path is Qwen3.5-only
today). See `mtp/` for the trainer (`train_mtp.py`, `losses.py`, `mtp_head.py`),
`mtp/extract_upstream_mtp.py` for the partial-download utility (only the
safetensors shards containing `mtp.*` keys are fetched), `mtp/inject_mtp.py`
for the merge-into-base step, and `setup/train_mtp_step.py` for the wizard
orchestration glue.

---

## Detailed setup

### Prerequisites

- NVIDIA DGX Spark (or any GB10 / sm_121a board) with CUDA 13.0+ driver
- Docker with NVIDIA Container Toolkit
- ~60 GB free disk for the Docker image
- Your fine-tuning dataset as JSONL with `{"messages": [{role, content}, ...]}` per line

### Pinned versions

`docker/Dockerfile.opt` pins the exact stack the speedup is verified against. Versions matter — Unsloth requires `transformers<=5.5.0`, and Triton 3.6 needs PyTorch 2.11 (the NGC 25.10 inductor is incompatible with Triton 3.6's `cluster_dims`).

| Component | Pin in Dockerfile | Verified at runtime |
|---|---|---|
| Base image | `nvcr.io/nvidia/pytorch:26.03-py3` | NGC 26.03 |
| PyTorch | (from base) | `2.11.0a0+a6c236b` |
| Triton | `v3.6.0` (from source, `TORCH_CUDA_ARCH_LIST=12.1`) | `3.6.0` |
| xformers | `v0.0.33` (from source) | `0.0.33` |
| transformers | `==5.5.0` (exact — Unsloth requires this) | `5.5.0` |
| trl | `==0.24.0` | `0.24.0` |
| peft | `>=0.18.0` | `0.19.1` |
| unsloth | (latest) | `2026.5.2` |
| unsloth_zoo | (latest) | `2026.5.1` |
| bitsandbytes | `>=0.49.0,<0.50.0` (aarch64 wheel) | `0.49.2` |
| datasets | `>=3.4.1,<4.4.0` | `4.3.0` |
| `flash-linear-attention` | `>=0.5.0` (mandatory for SSM fast path) | `0.5.0` |
| `causal-conv1d` | `>=1.4.0` (mandatory for SSM fast path) | `1.4.0` |
| CUDA driver | `13.0+` | 13.2 (forward-compat) |

The same stack is also available as a plain `docker/Dockerfile` (Baseline v0) with `torch.compile` disabled — that's what the "stock Unsloth" row of the speedup table is measured against, so the comparison is apples-to-apples on identical pinned versions.

### Non-interactive flags

The wizard accepts a few flags for scripted use:

```bash
./run.sh --data /path/to/train.jsonl --model Qwen/Qwen3.5-2B   # bypass pickers
./run.sh --rebuild                                              # force docker rebuild
./run.sh --rebuild=clean                                        # delete old image, then rebuild
./run.sh --non-interactive                                      # accept all defaults (CI)
```

### Bypassing the wizard

If you don't want the wizard — e.g. CI, scripted retraining loops — invoke `train.py` directly:

```bash
./install.sh             # only docker build + smoke test, no wizard
./scripts/run.sh python train.py \
    --mode lora --train-data /data/train.jsonl \
    --num-epochs 3 --per-device-batch-size 1 --gradient-accumulation 16 \
    --max-seq-length 16384 --pack --pack-length 5120 \
    --save-steps 200
```

To resume from a crash:

```bash
./scripts/run.sh python train.py --mode lora --train-data /data/train.jsonl \
    --num-epochs 3 --pack --pack-length 5120 \
    --resume-from-checkpoint results/lora-2026-01-15-120000/checkpoint-1200
```

### Verification bench

After the install, the verification bench confirms the kernel-level speedup on your machine:

```bash
docker run --rm --gpus=all --ipc=host \
    --ulimit memlock=-1 --ulimit stack=67108864 \
    -v $(pwd):/workspace -w /workspace \
    dgx-spark-unsloth-opt:latest \
    python -m lab.training_loop.qwen_minimal_bench --mode lora

docker run --rm --gpus=all --ipc=host \
    --ulimit memlock=-1 --ulimit stack=67108864 \
    -v $(pwd):/workspace -w /workspace \
    dgx-spark-unsloth-opt:latest \
    python -m lab.training_loop.qwen_minimal_bench --mode full-bf16
```

---

## What changed and why

The 7.67× LoRA / 8.35× Full FT win comes from four layers of optimization stacked on top of each other.

**1. Use the right Docker base.** NGC PyTorch 26.03 (not 25.10 — its bundled inductor is incompatible with Triton 3.6's `cluster_dims`) and Triton 3.6.0 built from source for sm_121a. `transformers==5.5.0` pinned exactly (Unsloth refuses anything else for Qwen3.5).

**2. Install the SSM fast path.** 75% of Qwen3.5's decoder layers are GatedDeltaNet/SSM (not Attention). Without `flash-linear-attention` + `causal-conv1d`, those layers fall back to a pure-PyTorch loop that dominates step time. Adding both packages to the image is the single biggest win in this project — a ~6× lift on real multimodal data, taking Qwen3.5-2B LoRA from 505 tok/s to 3076 tok/s before any custom kernel work is even active.

**3. Pack sequences at the dataset mean, not the maximum.** Setting `pack_length` equal to the mean token count per example (5120 for the reference dataset, mean was 5354) eliminates padding waste, stabilizes step-time variance from ~8× to ~1×, and lets JIT autotune caches actually hit. Packing at the *maximum* sequence length is a regression because attention is O(seq²).

**4. Replace the wrapper stack (optional fallback path).** For users whose stack can't run `torch.compile`, the project ships a vanilla-PyTorch training loop with a graph-safe `StaticLoRA` nn.Module replacing `peft.LoraLinear`, plus a fused Triton `silu_mul` kernel. Profiling shows `transformers.Trainer` + `peft.LoraLinear` + Unsloth's wrapper layer issue ~2 million `cudaLaunchKernel` calls per step on the slow ARM Grace CPU — ~56 seconds of pure host-side overhead. Removing them via this path was the original Path B design. The current production default uses Unsloth's compile-friendly forward directly (it beats the hand-written path by 12% with the SSM fast path active), but Path B remains available via `--static-lora` / `--wrap-full-ft`.

All four layers are lossless (loss curve preserved bit-identical to the unoptimized reference).

---

## What didn't ship

A speedup that breaks training quality is worse than no speedup. Everything below was tried, measured, and either failed the lossless gate or regressed end-to-end despite winning in isolation. Saved here so the next person can skip them.

### Configuration knobs that look promising but don't help

- **`max_autotune` + `cudagraphs` + `combo_kernels=True` in `torch.compile`** — Unsloth's Triton kernels live outside inductor's autotune scope. No-op.
- **`flash-attn 2.8.x` explicit install** — PyTorch 2.11 SDPA in NGC 26.03 already routes BF16 to a flash backend. The standalone wheel calls the same kernel.
- **Liger Kernel `qwen3_5` patches** — fail at install (`liger_rotary_pos_emb not available`; Qwen3.5 uses hybrid Gated DeltaNet, not standard rotary). The `qwen3_vl` fallback applies bit-identically to Unsloth's already-fused kernels → no-op.
- **`bs=2 × accum=8`** — pre-tokenized pipeline lacks a padding collator; a custom one would waste ~30% padding at this length distribution.
- **Packing above the dataset mean (e.g., `pack_length=8192`)** — regress. Attention is O(seq²); doubling pack-length more than doubles attention compute.
- **`group_by_length=True`** — only useful when `per_device_batch_size > 1`.
- **`num_warps` sweep on Unsloth's Triton kernels** — bit-identical; those kernels are not the bottleneck.

### Hardware features absent on sm_121a (no software fix possible)

NVIDIA staff confirmed on the developer forum (May 2026):

- **Tensor Memory (`tcgen05.*`)** — physically not on the sm_121a die.
- **`wgmma.mma_async`** — Hopper-only feature, never implemented in consumer Blackwell.
- **TMA `.multicast`** — absent on sm_121a. Single-CTA `cp.async.bulk{,.tensor}` *is* available.
- **Distributed shared memory** (`ld.shared::cluster`) — absent.
- **Cluster shape > 1×1×1** — locked at 1×1×1.

### Hardware features that ARE present but don't help this workload

- **Single-CTA TMA via `tl.make_tensor_descriptor`** — Triton 3.6 *does* emit `cp.async.bulk.tensor + mbarrier` on sm_121a (verified at PTX level). Bit-exact, but −2.2% end-to-end vs the `cp.async + ldmatrix + mma.sync` baseline. TMA's main wins (multicast, DSMEM, wgmma producer-consumer overlap) need HW absent here.
- **Hardware FP8 e4m3 MMA** — `mma.sync.aligned.kind::f8f6f4.m16n8k32` is HW-supported on sm_121a (validated bit-exact). Per-kernel microbench gives +16–41% over BF16 cuBLAS. **But end-to-end at batch=1, seq=5120, the Python-side quantize/dequantize launch overhead cancels the gain.** Net win is only 1–6%, not enough to justify the architectural complexity (loss scaling, requantize-on-step, per-channel scale tracking).
- **CUDA Graph capture** — works once the wrapper layer is gone, but adds only ~14 ms saving on top of the vanilla-PyTorch loop. At this config the workload is GPU-compute-bound, not Python-launch-bound after the major fixes.

### Software ecosystem not yet on sm_121

- **TransformerEngine FP8 / NVFP4** — TE has no sm_121 backend (NVIDIA confirmed, no roadmap). MXFP8/MXFP4 throw runtime assertions.
- **Triton 3.6 `tl.dot` on FP8 operands** — falls back to software emulation, 2–22× slower than BF16. The HW path exists; you need CUDA C++ + inline PTX to reach it.

### Kernel-integration anti-patterns

- **`F.linear` monkey-patch dispatching to a custom Triton matmul** — 21× slowdown in real training despite microbench wins. `weight.t().contiguous()` per-call dominates (3.8 GB of memcpy per step). Anti-pattern: use a proper `nn.Module` swap (the `StaticLoRA` pattern), not a monkey-patch.
- **Fused SwiGLU kernel that includes the matmul** — forward microbench +22%, end-to-end −3.3% because the autograd backward chain runs 4 elementwise PyTorch ops anyway. A smaller, single-launch elementwise `silu_mul` (operating on pre-computed `gate` and `up` tensors) replaces it — and that one IS net positive. The smaller fusion ships; the bigger one is preserved as a negative result in `lab/kernels/fused_swiglu_mm/`.
- **CUDA Graph capture of HF `Trainer` + Unsloth-wrapped step** — fails with `cudaErrorStreamCaptureUnsupported`. PEFT's dict iteration, Unsloth's lazy patches, and bitsandbytes' stateful 4-bit ops all break capture. Solution: replace the wrappers (see Path B), then capture works.

### Going further still

After all the above, further wins on this exact workload (batch=1, sequence 5120, Qwen3.5-2B shape) are diminishing-returns territory — typically 1–3% per attempt, with quality risk. The next meaningful step would be algorithm-level: a different optimizer, curriculum learning, distillation, etc. Those change the model and are out of scope for this project.

---

## File map — where to look for what

| Topic | File / Directory |
|-------|------------------|
| Interactive wizard (recommended entry point) | [`run.sh`](run.sh) + [`setup/wizard.py`](setup/wizard.py) |
| Data analyzer (JSONL → length distribution) | [`setup/analyze.py`](setup/analyze.py) |
| LoRA-vs-Full-FT recommendation + time estimate | [`setup/recommend.py`](setup/recommend.py) |
| Post-training merge → deployable model | [`setup/merge.py`](setup/merge.py) |
| Baseline v0 Docker image (stock pinned versions) | [`docker/Dockerfile`](docker/Dockerfile) |
| Optimized Docker image (compile ON + SSM fast path) | [`docker/Dockerfile.opt`](docker/Dockerfile.opt) |
| Docker-only install script (no wizard, for CI) | [`install.sh`](install.sh) |
| Training script — Unsloth PEFT default + Path B fallback | [`train.py`](train.py) |
| sm_121a-tuned BF16 matmul kernel | [`kernels/sm121a_matmul.py`](kernels/sm121a_matmul.py) |
| `StaticLoRA` (drop-in replacement for `peft.LoraLinear`) | [`lab/training_loop/static_lora.py`](lab/training_loop/static_lora.py) |
| `FullFT_BF16_Linear` (drop-in for `nn.Linear` in Full FT) | [`lab/training_loop/full_ft_bf16.py`](lab/training_loop/full_ft_bf16.py) |
| Verification bench (run after install to confirm speedup) | [`lab/training_loop/qwen_minimal_bench.py`](lab/training_loop/qwen_minimal_bench.py) |
| Single-launch LoRA matmul + per-shape dispatcher | [`lab/kernels/fused_lora/v3_hybrid.py`](lab/kernels/fused_lora/v3_hybrid.py) |
| Fused `silu_mul` Triton kernel + custom backward | [`lab/kernels/fused_silu_mul/kernel.py`](lab/kernels/fused_silu_mul/kernel.py) |

---

## Preparing your dataset and model

### Downloading the base model

This project is tuned against the Qwen3.5-2B family (multimodal `Qwen/Qwen3.5-2B`). Inside the Docker container, Unsloth's `FastModel.from_pretrained` downloads on first use:

```python
from unsloth import FastModel
model, tokenizer = FastModel.from_pretrained(
    "Qwen/Qwen3.5-2B",
    max_seq_length=16384,
    dtype=None,         # auto-pick BF16 on DGX Spark
    load_in_4bit=False, # 4.4 GB BF16 fits in 128 GB unified memory; 4-bit is unnecessary
)
```

To pre-download to a cache that survives container restarts, mount `~/.cache/huggingface` into the container (the `scripts/run.sh` helper does this). For headless boxes set `HF_TOKEN` if the model is gated.

### JSONL format

`train.py` expects one JSON record per line with a chat-template `messages` array:

```jsonl
{"messages": [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}
{"messages": [{"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}
```

Each line is one independent training example. The `system` role is optional. Multi-turn conversations work the same way — just append more `user` / `assistant` pairs to the same `messages` array.

### Data preparation tips

Things that matter for training speed and quality on this stack:

- **Length distribution.** Measure the mean and p99 of token counts per example with the model's tokenizer. The `--pack-length` flag in `train.py` should be set close to your **mean** length (rounded to the nearest multiple of 128 for kernel alignment). Setting it to the maximum length is a regression because attention is O(seq²).
- **Quality of assistant turns is what's being learned.** Loss is masked over everything up to the assistant response (user turns, system prompt, chat-template scaffolding are zero-weighted). System+user content matters for the conditioning, but you're only training the model to predict assistant tokens.
- **Drop pathological examples.** Examples whose token count exceeds `max_seq_length` get truncated (label values become wrong); whose assistant response is empty produce zero gradient. A 30-second filter pass over the JSONL pays for itself.
- **Hold a small fraction back for eval.** A 1–5% held-out split is enough to detect overfitting and quality regressions per training run. The eval set should be drawn from the same distribution as training; the production validator (which decides what goes to a larger model) is separate.
- **Validation loss is not quality.** Two checkpoints with the same eval loss can produce very different downstream behavior. Always score a small set of real prompts with your task's actual quality metric (BLEU/chrF/exact match/human grading/your validator), not just compare loss numbers.
- **Tokenize once.** Re-tokenizing per epoch wastes time. Pre-tokenize the dataset with the model's tokenizer once and persist; iterate over token IDs not text strings.

### Iteration loop

For specialist distillation work on a dataset that's still growing:

1. Train a checkpoint on whatever you have today. Hold 1–5% back for eval.
2. Run that checkpoint as your primary in production with a validator on the output.
3. Route validator-rejected cases to the slow/expensive path (paid LLM, larger model) and **save those exchanges** as next-round training data.
4. When you've collected enough additional examples (a few thousand minimum), retrain. With this project's throughput, that retrain takes days, not months.

The bottleneck shifts from compute time to data collection and validation-rule quality.

---

## Related work and credits

This project builds on prior community efforts to get sm_121a working at all — extending them rather than reinventing.

- [NVIDIA DGX Spark Unsloth Playbook](https://github.com/NVIDIA/dgx-spark-playbooks/tree/main/nvidia/unsloth) — official getting-started.
- [`raphaelamorim/spark-playbooks`](https://github.com/raphaelamorim/spark-playbooks) — community QLoRA recipe.
- [`haven-jeon/unsloth-vllm-gb10`](https://github.com/haven-jeon/unsloth-vllm-gb10) — Docker image with sm_121a patches.
- [Unsloth on DGX Spark](https://unsloth.ai/docs/blog/fine-tuning-llms-with-nvidia-dgx-spark-and-unsloth) — vendor blog.
- [karpathy/nanochat discussion #28](https://github.com/karpathy/nanochat/discussions/28) — community evidence of an 8× gap between default and optimized stacks on this hardware.

Forum threads that motivated parts of this design:

- [DGX Spark GB10 fine-tune slow time problem (361703)](https://forums.developer.nvidia.com/t/nvidia-spark-dgx-gb10-fine-tune-slow-time-problem-urgent-help/361703)
- [Unsloth 2048 RL training - very slow (356948)](https://forums.developer.nvidia.com/t/unsloth-2048-rl-training-very-slow/356948)
- [Working Docker Image for Unsloth (350673)](https://forums.developer.nvidia.com/t/working-docker-image-for-unsloth/350673)

Cloud GPU references used in the headline comparison:

- [QeRL: Beyond Efficiency — Quantization-enhanced Reinforcement Learning for LLMs](https://arxiv.org/abs/2510.11696) — Qwen2.5 series LoRA throughput study on H100 (RL rollouts, not direct LoRA training, but a useful data point for H100 scaling).
- [Unsloth Qwen3.5 fine-tune docs](https://unsloth.ai/docs/models/qwen3.5/fine-tune) — Unsloth's own 1.5× speedup claim vs FA2 baseline.

H100 / A100 on-demand pricing (May 2026 snapshot):

- [RunPod GPU pricing](https://www.runpod.io/pricing) · [Lambda Labs](https://lambda.ai/service/gpu-cloud) · [Spheron blog: GPU cloud pricing 2026](https://www.spheron.network/blog/gpu-cloud-pricing-comparison-2026/) · [Tom's Hardware: DGX Spark price hike](https://www.tomshardware.com/desktops/mini-pcs/nvidia-dgx-spark-gets-18-percent-price-increase-as-memory-shortages-bite-founders-edition-now-usd4-699-up-from-usd3-999) (MSRP source).

---

## License

[MIT License](LICENSE).

This recipe is meant to be reused, modified, and incorporated into commercial work without restriction. Citation back to this repository is appreciated but not required.
