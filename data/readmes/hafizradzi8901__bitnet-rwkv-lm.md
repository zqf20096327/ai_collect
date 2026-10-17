# BitNet-RWKV-7 — a from-scratch 1.58-bit language model on an 8GB GPU

A **0.15B-parameter RWKV-7 language model with BitNet 1.58-bit (ternary) weights**, trained from
scratch on a single **8GB consumer GPU** (RTX 5060) over ~9.9B tokens of story/chat text. The goal
was to learn modern LLM training *end to end* — quantization-aware training, a custom data pipeline,
inference, and fine-tuning — under hard memory constraints, and to ship a working local chat app.

This repo is the **training, inference, and fine-tuning toolkit** I built around it, plus a detailed
engineering log. It builds on two reference implementations (RWKV-LM and Microsoft's BitNet — see
[Attribution](#attribution-and-integration)); the BitNet↔RWKV integration and all tooling here are my own.

---

## What's interesting here

- **BitNet b1.58 quantization-aware training** ([`model_bitnet/bit_linear.py`](model_bitnet/bit_linear.py))
  — a `BitLinear` layer whose weights are **ternary {−1, 0, +1}** with mean-absolute-value scaling,
  trained with a **straight-through estimator** so gradients flow through the non-differentiable
  rounding. Master weights stay fp32 for the optimizer; every forward fake-quantizes to ternary.
- **2-bit weight packing for real inference savings** ([`tools/phase5/pack_int2.py`](tools/phase5/pack_int2.py))
  — packs 4 ternary weights per byte and runs packed inference, targeting ~5× lower VRAM and far
  higher throughput than the bf16 fake-quant used in training.
- **A data pipeline that scales past 4B tokens** ([`tools/parquet_to_binidx.py`](tools/parquet_to_binidx.py))
  — multi-schema Parquet → `binidx` conversion (8 parallel workers), with the int64 indexing fix
  required once a corpus crosses the 4B-token boundary.
- **A rejection-sampling fine-tuning (RFT) pipeline** ([`tools/rft/`](tools/rft/))
  — sample N candidates per prompt → score (length, repetition, style similarity, self-perplexity)
  → keep the winners → retrain on them.
- **A local chat app** ([`tools/web_chat.py`](tools/web_chat.py)) — a Gradio UI with temperature,
  top-p, and repetition-penalty controls, plus a CLI inference path.
- **Hard-won numerical-stability lessons** — see [Engineering notes](ENGINEERING_NOTES.md). Three
  real failure modes that each cost hours: `torch.compile` silently breaking the STE (→ NaN),
  8-bit AdamW annihilating BitNet's tiny gradients (→ loss explodes to billions), and TorchScript
  scripting `BitLinear` into a no-op (→ weights never quantized).

## Model at a glance

| | |
|---|---|
| Architecture | RWKV-7 ("Goose" x070) — a linear-attention RNN/transformer hybrid |
| Size | 0.15B params · `n_embd=768` · `n_layer=12` · `head_size=64` |
| Weights | BitNet **1.58-bit ternary**, quantization-aware training |
| Tokenizer | RWKV World byte-level trie (no out-of-vocabulary by construction) |
| Corpus | ~9.9B tokens of mixed story / chat data |
| Hardware | single RTX 5060 8GB · `ctx_len=1024` · ~11.6K tokens/s training throughput |

## Repository map

| Path | What it is |
|---|---|
| `model_bitnet/bit_linear.py` | **The core:** `BitLinear` 1.58-bit QAT module (STE, ternary weights) |
| `model_bitnet/test_bit_linear.py` | Unit tests for the quantizer |
| `tools/parquet_to_binidx.py` | Parallel multi-schema Parquet → binidx tokenized corpus |
| `tools/phase5/pack_int2.py` · `rnn_inference.py` | 2-bit weight packing + packed/RNN-mode inference |
| `tools/rft/` | Rejection-sampling fine-tuning: extract → sample → score → build → launch |
| `tools/web_chat.py` · `tools/infer.py` | Gradio chat UI · CLI inference |
| `tools/sanity_check.py` · `cleanup_checkpoints.py` · `toolchain.py` | Model/kernel verification, checkpoint pruning, MSVC+CUDA env loader |
| `launch_train.py` · `train_bitnet.ps1` | Training entry point (auto-resume) + launcher |
| [`ENGINEERING_NOTES.md`](ENGINEERING_NOTES.md) | Full build log: architecture, the critical gotchas, phase roadmap |

## Run it

```bash
# 1. Tokenize a Parquet corpus into binidx (excludes a held-out test split)
python tools/parquet_to_binidx.py

# 2. Train (auto-resumes from the latest checkpoint)
python launch_train.py --no_compile --no_grad_cp

# 3. Chat with a checkpoint locally (Gradio UI on http://127.0.0.1:7860)
python tools/web_chat.py
```

> The training corpus (~20GB tokenized) and checkpoints are **not** committed — bring your own
> Parquet shards with a `text` / `conversations` / `story` column. `--no_compile` is mandatory; see
> the engineering notes for why.

## Attribution and integration

This project stands on two open-source reference implementations:

- **[RWKV-LM](https://github.com/BlinkDL/RWKV-LM)** by BlinkDL — Apache-2.0. Provides the RWKV-7
  architecture and trainer. I patched five files to add BitNet support and large-corpus handling:
  `src/model.py` (swap `nn.Linear` → `BitLinear` under a `--bitnet` flag), `src/trainer.py`
  (checkpoint auto-prune), `src/dataset.py` (int64 fix for >4B-token corpora), `src/binidx.py`
  (a `skip_warmup` deserialization fix), and `train.py` (the `--bitnet` flag).
- **[BitNet](https://github.com/microsoft/BitNet)** by Microsoft — MIT. Reference for the b1.58
  quantization formula and the packed-inference kernels that `tools/phase5/` mirrors.

The upstream repositories are not vendored here (clone them separately to reproduce end-to-end).
My original code in this repo is MIT-licensed — see [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md).
