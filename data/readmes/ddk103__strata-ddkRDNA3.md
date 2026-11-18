# strata-ddkRDNA3

[English](README.md) · [简体中文](README.zh-CN.md)

**An RDNA3 (gfx1100) focused fork of Strata — built for the AMD RX 7900 XTX on Windows HIP.**

Based on [Niko1221/Strata](https://github.com/Niko1221/Strata) **v0.1.49.1**, with ported
modifications across 14 files (+663 / −29 lines) and a complete record of the tuning
work behind them.

---

## Why this fork exists

gfx1100 is in an awkward spot inside Strata. The 21-entry default switch table in
`src/core/arch_defaults.cpp` only applies when the GPU is a **gfx1151 (Strix Halo)**:

```cpp
if (!strata::kernels::gfx_arch_is_gfx1151(gcn_arch)) return t;
```

So on a 7900 XTX every one of those switches ships **off** by default, and each user ends
up back-porting them by hand. That is why the RDNA3 fork scene exists at all.

This branch ports several published techniques onto 0.1.49.1:

| Switch / change | What it does | Origin |
|---|---|---|
| `STRATA_STACK_ISOLATE` | Reserves the free address space below 1 TiB and gives the first thread its own stack (Windows HIP) | upstream issue **#3431** |
| `STRATA_VERIFY_DEFER_CPU` | Defers a decode window's CPU expert rows into the next layer's residual (**changes output**, opt-in) | pancake-strata |
| `STRATA_POOL_FUSE_PHASES` | Mode 7: gate/up and down run in one phase | pancake-strata item 29 |
| `STRATA_POOL_TAIL4` | Splits a phase's tail tasks to 1/4 size | basalt `553e9290d` |
| `resample_row` / `logit_bias` | Redraws a single row under grammar constraints | basalt `d64768699` / `02e1006fe` |
| `STRATA_PREFILL_COPY_EVENT_EVERY`, `_WAIT_DEDUPE` | Deduplicates prefill copy events | pancake-strata |
| `serve/grammar.py` wiring | `--grammar on` constrains tool calls and JSON output | see [NOTICE.md](NOTICE.md) |

Change list (`gfx1100/patches/strata-0.1.49.1-gfx1100.patch` has the full diff):

```
src/program/generate.cpp          +169      src/kernels/cuda/gr.cu            +45
src/core/pinned.cu                +119      src/kernels/cuda/elementwise.cu   +35
src/prefill/prefill.cpp            +99      CMakeLists.txt                    +17
src/kernels/cpu/pool.cpp           +86      serve/server.py                   +17
src/core/verify.cpp                +66      + 5 headers
```

**None of these techniques are mine.** The algorithms and kernels belong to their
respective authors; the porting to 0.1.49.1 is what this branch adds. Full attribution
chain in [NOTICE.md](NOTICE.md).

---

## `gfx1100/` — the tuning record

```
gfx1100/
├── docs/
│   ├── gfx1100-findings.md      which switches actually help on gfx1100, which don't
│   ├── TUNING-LOG.md            every change with its old value, new value and rollback
│   ├── quantization-plan.md     domain-specific quantization via imatrix + per-tensor types
│   ├── comparison-protocol.md   how to A/B two configs or models
│   ├── tuning-verdicts.md       which switches are real, no-ops, or machine-bound
│   └── corpus-notes.txt         how the calibration corpus was assembled
├── configs/
│   ├── fork-8090.example.json   engine config sample (44 env vars, queue and cache settings)
│   ├── glm-3.0bit.example.json  GLM-5.3-Flash launch config on PolyStrata
│   └── game-types.txt           llama-quantize per-tensor precision table
├── bench/
│   ├── bench.py                 decode-speed A/B benchmark
│   └── bench-*.json             raw measurements
└── patches/
    └── strata-0.1.49.1-gfx1100.patch    14 files, +663/−29
```

---

## Tested configuration

**Every number below was measured on this exact setup.** Change the model, the quant,
the engine flags or the driver and the figures no longer compare. The full list — all 44
environment variables, every launch flag — is in
[gfx1100/docs/test-environment.md](gfx1100/docs/test-environment.md).

| | |
|---|---|
| GPU | AMD Radeon RX 7900 XTX 24 GB (gfx1100), driver `32.0.21030.2001` |
| CPU | AMD Ryzen 7 9700X, 8C / 16T |
| RAM | 125.5 GiB |
| OS | **Windows 11 Pro `10.0.26200`**, HIP (`amdhip64_7.dll`) |
| Engine | Strata **0.1.49.1**, built from this tree |
| Model | **Qwen3.8-Flash-Next**, Unsloth Dynamic **`UD-IQ4_XS`**, **4.23 BPW**, **87.24 GB** / 4 shards |
| Quant layout | mixed per-tensor: routed experts IQ2_S/IQ3_XXS/IQ4_XS/IQ4_NL/Q5_0, attention Q6_K/Q8_0, router **F32**, n-gram table IQ4_NL |
| Prompt / output | fixed ~**1.5K token** prompt, **256 token** cap, `temperature 0` |
| Sampling | 2 warm-ups discarded; 16 baseline / 32 treatment runs; `decode_tok_s` from `/metrics` matched by request timestamp |

> ⚠️ **The 44 environment variables are not compiled into any default.** `arch_defaults.cpp`
> ships branches for gfx12, gfx1151 and iGPU parts — **not for gfx1100**. Building this tree
> and starting it with upstream defaults gives you the *untuned* engine, and none of these
> numbers reproduce. Use `gfx1100/configs/fork-8090.example.json`.

---

## Measured results

### 1. Conversation cache — the single biggest win

The default `--conversation-cache-mib auto` caps at 8 GiB, which holds only ~3 sessions
of ~96K tokens each. With several agent sessions alternating, they evict each other and
every turn re-reads the whole prompt.

| Setting | Before | After |
|---|---|---|
| `--conversation-cache-mib` | auto (8192) | **16384** |
| `--conversation-cache-slots` | 4 | **8** |

```
before: 142 evictions, last request reused 21,357 / 96,075 tokens → 25–40 s cold prefill
after :   0 evictions, 5–6 sessions parked, 97–100% reuse      →  1–3 s prefill
```

The conversation cache lives in **host RAM**, not VRAM — that is why the trade is so good.

### 2. Two decode switches

`bench/bench.py`: fixed ~1.5K prompt, fixed 256-token output, `temperature 0`, two warm-up
runs, then sampling `decode_tok_s` from `/metrics` matched by request timestamp.

| | Baseline | `STRATA_TSUM=1` + `STRATA_RDNA_Q6K=1` |
|---|---|---|
| Samples | 16 | 32 |
| Mean | 88.23 tok/s | 89.60 tok/s (**+1.5%**) |
| Median | 88.15 tok/s | 90.10 tok/s (**+2.2%**) |
| Welch t | — | 1.43 (**not significant**) |
| 95% CI | — | −0.50 … +3.23 tok/s |

Directionally positive, but not statistically provable. Neither switch changes model size
or VRAM, so the worst case is zero gain — which is why they are kept.

### 3. Queue model

| Setting | Value | What it does |
|---|---|---|
| `max_queue` | 5 | Admission cap = `max(1, batch) + max_queue` = 6 |
| `queue_timeout` | 270 | Requests waiting longer than 270 s get `429 queue_wait_timeout`, inside the client's 300 s idle timeout |

Lesson learned: `max_queue: 0` (cap of 1) makes a client exhaust its 5 retries on 429s;
no cap at all lets the queue grow without bound until the client aborts at 300 s and the
GPU work is wasted.

---

## ⚠️ Read this before using

### Compatibility

1. **Baseline is v0.1.49.1.** Upstream never published a git tag for that version, so this
   tree should not be merged with `main`.
2. **Verified on exactly one configuration**: RX 7900 XTX 24 GB + Windows 11 26200 + HIP
   (`amdhip64_7`). Linux, the official ROCm stack and other RDNA3 cards (7800 XT / 7700 XT /
   7600) are **untested**.
3. The changes touch CUDA/HIP kernels and CMake, so **a different compiler version may fail
   to build**.

### Not included

4. **No AMD proprietary binaries**: the ROCm runtime (`amdhip64_7.dll`, `amd_comgr.dll`),
   hipBLASLt tuning tables and rocBLAS libraries must be installed separately.
5. **No model weights**, no GGUF files.
6. No prebuilt `strata.exe`.

### About the numbers

7. Every figure is a **single-machine, single-session measurement with 3–5% noise**. It is
   not an authoritative benchmark; repeating it on the same machine can swing more than the
   difference being measured.
8. **Short and long contexts differ a lot**: ~88 tok/s at 1.5K context, ~68 tok/s at 100K
   (long contexts do KV streaming). Comparing figures across context lengths is meaningless.

### Output quality

9. **Some changes alter the output**, notably `STRATA_VERIFY_DEFER_CPU` (the code comment
   literally says "changes the output"). Turn those off before a bit-identical A/B.
10. `STRATA_RDNA_Q6K` and `STRATA_TSUM` are summation-order optimisations. They are
    mathematically equivalent but **not guaranteed bit-identical**.

### Security

11. The example configs have a placeholder `api_key`. Replace it with your own strong random
    value before deploying, and never commit a real key.
12. The sample config listens on `0.0.0.0`. Switch it back to `127.0.0.1` if you do not need
    LAN access.

---

## Building

Same procedure as upstream — see [README.upstream.md](README.upstream.md) and the upstream
`docs/INSTALL.md` / `docs/AMD_HIP.md`.

Key points for Windows + HIP:

- ROCm or the AMD HIP SDK must be installed (it provides `amdhip64_7.dll`)
- CMake ≥ 3.24 plus a HIP-capable MSVC or clang
- `-DCMAKE_HIP_ARCHITECTURES=gfx1100`
- The first build takes 10–20 minutes

---

## License

**MIT**. See [LICENSE](LICENSE) — the upstream copyright notice is retained verbatim.

Upstream copyright: Copyright (c) 2026 **Niko1221 and the Strata contributors**.
Ported techniques remain copyright of their respective authors (pancake-strata, basalt,
llama.cpp). This branch covers only the porting to 0.1.49.1 and the tuning record.

Full attribution chain: [NOTICE.md](NOTICE.md)
