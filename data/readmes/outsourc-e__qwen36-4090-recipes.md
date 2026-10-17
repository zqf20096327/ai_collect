# Qwen3.6-27B on RTX 4090 — Recipes & Receipts

Reproducible llama.cpp configs for **Qwen3.6-27B-Q4_K_M** on a single **RTX 4090 (24 GB)**, with **per-category quality verification** — not just raw tok/s.

> **TL;DR:** Same-vocab speculative decoding via **mainline llama.cpp** (not ik_llama.cpp) + **Qwen3.5-4B draft** = **43 tok/s mean / 67 peak with 6/6 quality pass** on Q4_K_M. Cross-vocab spec-dec setups hit higher peak numbers but silently corrupt JSON and structured output.

This repo logs every config we tested on April 25, 2026 — winners, dead ends, and the silent-corruption bug nobody mentions.

---

## Results matrix

All numbers are RTX 4090, Qwen3.6-27B-Q4_K_M, benched with [`bench/bench-split.py`](bench/bench-split.py) — 6 task categories with automated quality checks (lists, code, JSON, reasoning, tool-calls, essay).

| Tag | Engine | Draft | Ctx | KV | Mean tps | Max tps | Pass | VRAM | Use case |
|---|---|---|---:|---|---:|---:|:---:|---:|---|
| **C1-agg** ([config](configs/start-mainline-c1-agg.sh) · [run](results/run-c1-agg.txt)) | mainline llama.cpp | Qwen3.5-4B same-vocab | 8K | q8 | **43.2** | **67.1** | ✅ 6/6 | 22 GB | **Production default** |
| **C1-32K-dkv** ([config](configs/start-mainline-c1-32k-dkv.sh) · [run](results/run-c1-32k-dkv.txt)) | mainline llama.cpp | Qwen3.5-4B same-vocab | 32K | q4 | **41.6** | **61.9** | ✅ 6/6 | 23 GB | **Long context + spec-dec** |
| **C2-64K** ([config](configs/start-mainline-c2-64k.sh) · [run](results/run-c2-64k.txt)) | mainline llama.cpp | none | 64K | q4 | 38.6 | 41.3 | ✅ 6/6 | ~21 GB | Mid context, no spec-dec |
| **C3-256K** ([config](configs/start-mainline-c3-256k.sh) · [run](results/run-c3-256k.txt)) | mainline llama.cpp | none | 256K | q4 | 38.2 | 42.1 | ✅ 6/6 | 22 GB | **Massive context (RAG/agent)** |
| **A2 (caveat)** ([config](reference/start-8k.sh)) | ik_llama.cpp | Qwen3-1.7B cross-vocab | 8K | q8 | 61.2 | 102.1 | ⚠️ 4/6 | 18 GB | Speed-only; **corrupts JSON & lists** |
| A1 ([config](reference/start-32k-nodraft.sh)) | ik_llama.cpp | none | 32K | q8 | 36.8 | 41.5 | ✅ 6/6 | 16 GB | Pre-mainline production |

The **bold rows are the recommended stack.**

---

## The silent-corruption bug

Most "150 tok/s on Qwen3.6-27B" recipes use `ik_llama.cpp` with a Qwen3-1.7B draft. ik_llama logs:

```
the target and draft vocabs are not compatible - tokens will be translated between the two
```

…and runs anyway. The translation works **statistically** — high acceptance rate, big tps gains — but it **silently breaks** edge tokens: JSON braces, list separators, quote escapes, tool-call boundaries.

Per-category quality split for the cross-vocab "speed king" config (A2):

```
code   ✅ 63 tps    reason ✅ 61 tps    essay  ✅ 90 tps
tool   ✅ 31 tps    json   ❌ 102 tps   list   ❌ 20 tps
```

Aggregate looks great. Output is unusable for anything structured.

We tested **four different drafts** including same-`n_vocab` Qwen3.5-0.8B (config in [`reference/start-32k-samevocab.sh`](reference/start-32k-samevocab.sh)) — ik_llama still triggers the translation path because the BPE merges/special-token tables don't match exactly. Build 4274 cannot do clean same-vocab spec-dec.

---

## The fix: mainline llama.cpp + same-vocab draft

`Qwen3.5-4B` shares Qwen3.6-27B's tokenizer (vocab 248,320, identical BPE, identical specials). On **mainline llama.cpp** — which implements `SSM_CONV_TREE` (ik_llama 4274 doesn't) — the draft loads cleanly and there is **no translation layer**. Output is identical to no-spec.

Build mainline on Linux/WSL with CUDA:

```bash
git clone --depth 1 https://github.com/ggerganov/llama.cpp ~/llama-mainline/llama.cpp
cd ~/llama-mainline/llama.cpp
export PATH=/usr/local/cuda-12.8/bin:$PATH
export CUDACXX=/usr/local/cuda-12.8/bin/nvcc
cmake -B build -DGGML_CUDA=ON -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_CUDA_COMPILER=$CUDACXX -DCUDAToolkit_ROOT=/usr/local/cuda-12.8
cmake --build build --config Release -j 16 --target llama-server
```

Then point the configs at it:

```bash
export LLAMA_MAINLINE=$HOME/llama-mainline
export MODELS_DIR=/path/to/your/gguf/folder
./configs/start-mainline-c1-agg.sh
```

Models you need:
- `Qwen3.6-27B-Q4_K_M.gguf` ([lmstudio-community](https://huggingface.co/lmstudio-community/Qwen3.6-27B-GGUF))
- `Qwen3.5-4B-Q4_K_M.gguf` (any standard GGUF release)

---

## Benchmarking your own setup

```bash
pip install --user requests   # bench-split.py uses urllib stdlib actually
# Start a config in another terminal, then:
python3 bench/bench-split.py http://127.0.0.1:8081/v1 my-config-label
```

Every run prints a `# JSON_RESULT={...}` line at the bottom — `results/run-*.txt` contains ours.

The bench covers 6 categories with automated checks:
- **list** — Top 10 programming languages, must include ≥5 known names
- **code** — Python FizzBuzz, must define a function with the right modulo logic
- **json** — Structured language list, must parse + match schema
- **reason** — Train word-problem, must produce coherent step-by-step
- **tool** — Tool-call decision, must emit valid JSON tool invocation
- **essay** — Long-gen prose, must hit a word-count floor

Per-category tps and pass/fail prevent the "good aggregate, broken structured output" trap.

---

## Dead ends (so you don't repeat them)

Things that look promising but do NOT work on a single 4090 today:

- **z-lab/Qwen3.6-27B-DFlash** (vLLM nightly) — auxiliary BF16 hidden-state cache OOMs at 24 GB even with `max_model_len=1024, max_num_seqs=1, num_speculative_tokens=4`. Memory ceiling ~24-26 GB. Needs ≥32 GB VRAM (5090 / A6000 / H100).
- **spiritbuun/Qwen3.6-27B-DFlash-GGUF** — llama.cpp doesn't recognize the `dflash-draft` arch (`error loading model architecture: unknown model architecture: 'dflash-draft'`). Requires custom kernel work for SSM/non-causal attention.
- **TurboQuant TQ3_4S** — neither runtime supports the format yet.
- **vLLM + AutoRound INT4 + cudagraph** — hangs / deadlocks on Qwen3.5/3.6 hybrid attention.
- **MTP via vLLM (`--speculative-algo NEXTN`)** — INT4 quantization wrecks acceptance, and BF16 target won't fit on 24 GB.

The DFlash failure mode is documented in the [`reference/start-dflash-gguf.sh`](reference/start-dflash-gguf.sh) script (ik_llama segfault on the GGUF arch).

---

## Open issues / upstream

1. **Mainline llama.cpp** — same-vocab spec-dec hangs at >32K with q8 KV (Qwen3.5-4B draft × Qwen3.6-27B target). Workaround: q4 KV for both target+draft (see `c1-32k-dkv` config).
2. **ik_llama.cpp 4274** — missing `SSM_CONV_TREE` op; cannot load Qwen3.5-4B as draft.
3. **ik_llama.cpp 4274** — silent vocab translation on cross-vocab spec-dec corrupts structured output. Should warn louder or refuse.

---

## Repo layout

```
configs/    -- mainline llama.cpp launch scripts (the recommended stack)
reference/  -- ik_llama.cpp configs (broken / cross-vocab references)
bench/      -- bench-split.py (per-category tps + quality)
results/    -- raw run-*.txt logs with JSON_RESULT lines
```

Set `MODELS_DIR`, `LLAMA_MAINLINE`, and `IK_LLAMA` environment variables before running any script.

---

## Following work

- **Custom-trained Qwen3.6-Drafter-0.6B** — distill on Qwen3.6-27B outputs, exact same tokenizer config. Goal: 100+ tps with full 6/6 quality pass.
- **Same recipes on RTX 5090 / A6000** — DFlash should fit; would close the loop on the 4090 ceiling.

---

Built and benched by [@outsourc-e](https://github.com/outsourc-e). PRs and replication welcome.
