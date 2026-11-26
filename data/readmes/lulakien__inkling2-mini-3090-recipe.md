# Inkling 2 Mini on RTX 3090s: a vLLM recipe for 1 or 2 consumer Ampere GPUs

Serve [`thinkingmachines/Inkling-2-Mini`](https://huggingface.co/thinkingmachines/Inkling-2-Mini) on **one RTX 3090
(128K context, or 262K with an FP8 KV cache)** or **two RTX 3090s (262K context, 512K in bf16 or 1M with FP8 KV as opt-in profiles)**, PCIe only, no NVLink, no P2P,
power-capped at 280 W, with the shipped checkpoint unchanged (NVFP4 experts, bf16 rest; see
[what precision you are running](#what-precision-you-are-running)).

The official `vllm/vllm-openai:inkling-2-mini` image only supports Hopper/Blackwell. This repo has small file
overlays (mounted read-only over that image, nothing rebuilt) that make it run on sm_86. A second set of overlays
makes it fast there. It also has the launchers, the tests behind every number below, and the raw results.
**No model weights are included.**

## What precision you are running

The official checkpoint, not a community quant. Nothing is requantized on disk; the table is what the GPU computes with.

| part | in the checkpoint | how this recipe serves it |
|---|---|---|
| MoE experts | NVFP4 (4-bit, as Thinking Machines ships it) | the same NVFP4 bytes, read directly by the kernel; math in bf16 with fp32 accumulation (W4A16) |
| attention qkv projections, LM head, Markov head, DSpark drafter layers | bf16 | **int8 per-channel weights by default** (converted at load, to save VRAM and bandwidth). `W8=` keeps them bf16 |
| everything else (attention output `wo_ud`, short convs, loop mixing, norms, embedding) | bf16 | bf16 |
| activations | | bf16, fp32 accumulation |
| KV cache | | bf16 by default; FP8 E4M3 only on the 1-GPU `262k` and 2-GPU `1m` profiles |

Quality checks, same harness for every row (1,140 MMLU questions, 57 subjects x 20, letter logits, sequential):
**911/1140 (79.9%) as served** vs **908 with the int8 layers kept in bf16 (`W8=`)**; the model card reports 79.47% on MMLU.
Multi-fact retrieval passes at 500K (bf16 KV, 8/8) and a single needle at 1.04M (FP8 KV). That is a sanity check, not a full
eval: coding and long-reasoning quality have not been compared against the official H100 deployment. Opt-in switches
that change numerics are marked where they appear (`KV_DTYPE=fp8`, `FAR_ATTN=1`). The speed comes mostly from the
speculative drafter that ships in the checkpoint (DSpark, ~2-3x on code) and PCIe all-reduce work, not from lower
precision.

## Results

<p>
<img src="docs/img/localmaxxing-2gpu.png" width="49%" alt="LocalMaxxing: 2x RTX 3090, 313 tok/s">
<img src="docs/img/localmaxxing-1gpu.png" width="49%" alt="LocalMaxxing: 1x RTX 3090, 242 tok/s">
</p>

Submitted to [LocalMaxxing](https://www.localmaxxing.com/en/models/thinkingmachines/Inkling-2-Mini). Its VRAM field
is the sum across GPUs (the 2-GPU card's 41.8 GB should read 40.8 GiB).

Same machine and checkpoint for every column. Batch 1 unless noted. Temp 0, reasoning effort "low" for decode.

| | 2 GPUs (`launch/2gpu.sh`) | 1 GPU, 128K (`launch/1gpu.sh`) | 1 GPU, 262K (`PROFILE=262k`, FP8 KV) |
|---|---|---|---|
| max context / KV pool | 262,144 / 302,534 tok | 131,072 / 135,401 tok | 262,144 / 262,755 tok |
| decode tok/s: code / explanation / story | **313 / 166 / 126** | **242 / 130 / 97** | **254 / 126 / 101** |
| decode step (DSpark k=7) | 13.7-14.2 ms | 17.8-18.6 ms | 18.4-19.0 ms |
| prefill tok/s at 2K / 16K / 64K | 7,480 / 7,140 / 6,280 | 5,800 / 5,280 / 4,360 | 5,420 / 4,640 / 3,370 |
| prefill, near max context | 4,270 tok/s (254K in 59 s) | 3,580 tok/s (127K in 35 s) | 1,650 tok/s (254K in 154 s) |
| agent turn: 13K prompt sharing a prefix with the previous one | 0.12 s (cold 1.9 s) | 0.19 s (cold 2.5 s) | 0.23 s (cold 2.8 s) |
| 2 / 4 / 8 concurrent streams, total tok/s | 250 / 426 / **580** | 211 / 317 / - | 190 / 248 / 251 (4 at a time, k=7) |
| needle in haystack (5% and 90% depth) | 255K: both found | 128K: both found | 255K and 262K: both found |
| MMLU, 57 subjects x 20, letter logits | 911 / 1140 (79.9%) | 912 / 1140 (80.0%) | 911 / 1140 (79.9%) |
| OpenAI API checks (`tests/api_smoke.py`) | 9/9 (+ image 10/10 with `MM=1`) | 9/9 | 9/9 |
| temp-0 run-to-run determinism | 8/8 identical | 8/8 | 8/8 |
| power while busy / max temp / peak VRAM | 277 W / 72 C / 21.0 GB per card | 278 W / 67 C / 23.4 GB | 276 W / 68 C / 23.7 GB |
| boot (compile cache warm / first ever) | 40 s / 125 s, + 6-14 s warm-up | 40 s, + 12 s warm-up | 35 s, + 10 s warm-up |

The 262K single-GPU profile stores the KV cache as FP8 E4M3, converted in software on Ampere. Quality gates match
bf16, but temp-0 outputs differ from the 128K profile within the first few hundred characters, and long prompts are slower
(see Limitations). Its higher code and story decode numbers come from different draft acceptance on that different
text (4.8 vs 4.5 tokens per step on code), not from a faster step.

**Longer context on 2 GPUs** (opt-in, `experiments/long-context-2gpu/RESULTS.md`):

| | `PROFILE=262k` (default) | `PROFILE=512k` | `PROFILE=1m` |
|---|---|---|---|
| max context / KV pool | 262,144 / 302,534 | **524,288 / 535,422** (bf16 KV) | 1,048,576 / 1,325,310 (FP8 KV) |
| what changes | | `SCONV_TAIL=1`, async scheduling off, 4 sequences | + FP8 KV, single-GPU memory knobs, 2 sequences |
| decode tok/s, code / explanation / story | 315 / 166 / 126 | 333 / 171 / 127 | 286 / 159 / 118 |
| cold agent prompt | 250K: 59 s | 250K: 59 s, 500K: 167 s | 250K: 102 s, 1.04M: 19.5 min |
| warm agent turn (cached prefix) | 250K: 1.1 s | 500K: 2.0 s | 250K: 2.0 s |
| retrieval, MMLU | 8/8 facts at 250K, 911 | 8/8 facts at 500K, 911 | needle at 1.04M found, 912 |

**Faster cold long prompts (opt-in, new):** `FAR_ATTN=1` lets the prefill attention kernel skip the relative-bias
work on keys more than 1,024 tokens back (x1.25 on that kernel with bf16 KV, x1.15 with FP8): **500K cold 167 s -> ~145 s** (4 runs: 144-146 s)
on `512k`. On `1m`, `MNBT=2048` also lets the copy-engine prefill pipeline run (its 1024-token chunks were below the
pipeline's minimum); the two together take **1.04M cold from 19.5 min to 14.9 min** (250K: 102 s -> 79 s; pool 1.29M).
Not bit-identical: fp32-rounding-level differences (in prefill and, at long context, decode), retrieval unchanged (`experiments/prefill/RESULTS.md`).

A second agent joining a long-running one stalls the first to ~11 tok/s while its own prompt prefills (11-18 s for
64K), then both decode at about three quarters of the single-stream speed.

**Other hardware (community reports, not re-run here):**

| setup | context / KV pool | decode, code / prose | prefill | long-context check | reported by |
|---|---|---|---|---|---|
| 2x A40 48 GB (sm_86), TP2, vLLM built from source + these overlays, `HOSTAR=0 CEAR=0` (P2P) | 262,144 / **1,042,673** (bf16 KV) | ~250-290 / ~96-100 tok/s | ~8.8K tok/s peak | 512K with FP8 KV: 524K-token needle found in 281 s | [buzz](https://github.com/buzz), [#3](https://github.com/lulakien/inkling2-mini-3090-recipe/issues/3#issuecomment-7109679182) ([details](results/community/2xA40_buzz.md)) |

More cards are welcome: see [#5](https://github.com/lulakien/inkling2-mini-3090-recipe/issues/5).

Decode speed depends on the text because speculative decoding (DSpark, the model's own drafter) accepts more
tokens on predictable text: about 4.5 tokens per step on code, 2.4 on technical prose, 1.75 on stories.

What the speed overlays add, measured on 2 GPUs (`results/2gpu_port_only`, which has only the overlays needed to
run, with every speed switch off):

| | port only | this recipe |
|---|---|---|
| decode, single stream | 109 tok/s (no speculation) | 313 / 166 / 126 tok/s (2.9x / 1.5x / 1.15x) |
| prefill 16K / 254K | 6,290 tok/s / 69.5 s | 7,140 tok/s / 59.4 s (+13.5% / -15%) |
| MMLU | 908 | 911 |

**350 W instead of 280 W** (2 GPUs, `results/2gpu_350w`; short run, decode and prefill only): decode
323 / 170 / 129 tok/s (+3%), prefill 2K / 16K / 64K 7,840 / 7,480 / 6,620 tok/s (+5%), cards at ~339 W,
peak 75 C. Not worth the extra heat for daily use here, so the published numbers stay at 280 W.

Serving several users at once: the draft length now shrinks with the batch (k=7 for one stream, 4 / 2 / 1 for
2 / 3-4 / 5+), so speculation keeps the single-stream speed and no longer costs throughput when many streams share a
step. 2 GPUs, total tok/s at 1 / 2 / 3 / 4 / 6 / 8 streams: 196 / 250 / 359 / 426 / 493 / **580**, against
167 / 227 / - / 296 / - / 429 with a fixed k=7 and 127 / 205 / - / 349 / - / 545 with no speculation (same session).
One GPU: 211 / 317 tok/s at 2 / 4 streams (fixed k=7: 191 / 265). The post-boot warm-up now also covers batched
shapes, so the first burst of users no longer waits on kernel compiles. Details and the TTFT trade-off of a second
agent (`LPT`): [`experiments/concurrency/RESULTS.md`](experiments/concurrency/RESULTS.md).

## Quick start

Requirements: Linux, Docker with the NVIDIA Container Toolkit, an NVIDIA driver that supports CUDA 13
(tested on 620.73), RTX 3090(s) **with no display attached** (the single-GPU profiles use the whole 24 GB),
about 20 GB of disk for the model and 36 GB for the image.

```bash
git clone https://github.com/lulakien/inkling2-mini-3090-recipe && cd inkling2-mini-3090-recipe
hf download thinkingmachines/Inkling-2-Mini --revision ed40e7da625f594fc9c4990f5f66be24873c22d7 \
  --local-dir ~/models/Inkling-2-Mini
. launch/image.env && docker pull "$IMAGE"

bash launch/2gpu.sh                    # two GPUs, 262K context
PROFILE=512k bash launch/2gpu.sh       # two GPUs, 512K context, bf16 KV (same speed)
PROFILE=1m bash launch/2gpu.sh         # two GPUs, 1M context, FP8 KV (cold 1M prompt ~20 min)
FAR_ATTN=1 MNBT=2048 PROFILE=1m bash launch/2gpu.sh   # opt-in faster long prefill (cold 1M ~15 min)
bash launch/1gpu.sh                    # one GPU (GPU=0|1), 128K context
PROFILE=262k bash launch/1gpu.sh       # one GPU, 262K context, FP8 KV (slower long prompts)
```

The server listens on `http://127.0.0.1:8000/v1` and the model name is `inkling-2-mini`. Stop it with
`docker stop inkling2` (2 GPUs) or `docker stop inkling2-1gpu`.
`MODEL_DIR`, `PORT`, `NAME`, `MAXLEN`, `MAXSEQS` and every switch in the `launch/serve.sh` header can be overridden
from the environment. To run two single-GPU servers at once, give each its own card, port and name:
`GPU=1 PORT=8001 NAME=inkling2-gpu1 bash launch/1gpu.sh`.

Reasoning: pass `"reasoning_effort": "none" | "low" | "medium" | "high"` (top level or in
`chat_template_kwargs`). Reasoning comes back in `message.reasoning`, the answer in `message.content`. Tool calling
(`--tool-call-parser inkling`) and JSON-schema `response_format` work (see `results/*/api_smoke.json`).

## Reproduce the numbers

```bash
bash tools/fetch_haystack.sh                         # needle-test text, copied out of the pinned image
LABEL=2gpu MAXCTX=262144 bash tests/run_suite.sh     # against a running 2gpu.sh server (~15 min)
NAME=inkling2-1gpu LABEL=1gpu_128k MAXCTX=131072 bash tests/run_suite.sh   # ~10 min; 262k: ~30 min
bash tests/kernels/run.sh                            # bit-exactness of the new kernels (stop the server first)
```

| test | what it checks |
|---|---|
| `tests/api_smoke.py` | chat, streaming with usage, reasoning split, tool call + tool-result turn, JSON-schema output, `/v1/completions` logprobs, prefix-cache hit, temp-0 determinism, stop sequences, image input (`--image`, needs `MM=1`) |
| `tests/spec_bench.py` | single-stream decode speed and DSpark acceptance on code / explanation / story, temp 0 and 0.6 |
| `tests/prefill_ttft.py` | cold prefill throughput, 2K to near max context (random token ids, so no cache hits) |
| `tests/prefix_midprobe.py` | agent-style turns: same 13K prefix, different user message |
| `tests/concurrency.py` | total and per-stream throughput with 1-8 concurrent streams |
| `tests/needle.py` | find a planted line in a long code haystack at 5% and 90% depth, near max context |
| `tests/agent_turns.py` | agent-style transcript (system prompt, tool calls, file reads) at a given length with planted facts: cold turn, warm turn, all facts at once, first turn after compaction; TTFT, cached tokens, decode, peak VRAM |
| `tests/second_stream.py` | a second agent joins while the first streams: the first agent's speed before / during / after, the newcomer's TTFT |
| `tests/greedy_check.py` | temp-0 outputs identical across runs (8 prompts) |
| `tests/mmlu_letters.py` | MMLU 57 subjects x 20 questions, letter logits, sequential (`tests/data`, MIT-licensed MMLU) |
| `tests/kernels/` | parallel MoE align (35 cases) and 2-pass attn_res (72 cases) vs the stock kernels, `torch.equal`; software FP8 E4M3 encode/decode vs `torch.float8_e4m3fn`, bit-exact |
| `tools/gpu_summary.py`, `tools/gemm_tflops.py` | power/temp/VRAM from the suite's 1 Hz log; sustained BF16 GEMM rate (unlock check) |

Raw JSON for every run is in `results/`. Run-to-run variation is about 1-2% for prefill and decode step time.
Decode tok/s also moves with draft acceptance at temp 0.6.

## What is in the recipe

Details, profiles and rejected ideas: [`docs/NOTES.md`](docs/NOTES.md). Each overlay has a diff against the stock
file in `patches/diffs/`.

| piece | effect |
|---|---|
| **sm_86 port**: minimum capability, FA2 vision attention, Triton fallbacks for `conv_mix` / `short_conv`, no TMA, Triton MoE align, unfused embedding, portable drafter KV writes, griddepcontrol/PDL off | runs at all. Three of the stock kernels exist only for sm_100 and **fail silently** on Ampere (garbage MoE routing) |
| DSpark speculative decoding, k=7 (the drafter ships in the checkpoint) | decode 2-3x on code |
| host-memory TP2 all-reduce / all-gather for small tensors (no P2P on GeForce; ~12 us vs 31 us NCCL, bit-identical) | decode step -1.5 ms |
| split-K skinny GEMM for the loop controllers and dynamic conv taps (cuBLAS picks 6-CTA kernels at 2-16 rows) | decode |
| int8 per-channel weights (own Triton kernel) for attention qkvr, LM head, Markov head, drafter layers; experts and `wo_ud` untouched | decode ~8%, frees VRAM; MMLU 911 vs 908 in bf16 |
| row-piece layer tail on the copy engines (prefill all-reduce overlapped with expert GEMMs) | prefill +6%, 254K -9% |
| split-KV full attention for long prompts | 254K -9% |
| parallel MoE align, 2-pass attn_res (bit-identical) | prefill +3.4% (1 GPU), +7.5% (2 GPUs) |
| prefix-cache retention every 64 tokens | prefix hits when a new prompt diverges mid-message |
| single GPU: W8 quantized at load, GMU 1.0 + 512 MiB KV margin, chunked prompt-logprob warm-up, input embedding in pinned host memory, `--no-async-scheduling` | context on one card: 3.7K -> 114K tokens |
| short-conv cache backs only each step's tail (`SCONV_TAIL=1`, single-GPU profiles) | 1 GPU: 131K with 1024-token prefill chunks (+18% prefill vs the old 512-token 128K profile) |
| FP8 E4M3 KV cache with software conversion on sm_86 (`KV_DTYPE=fp8`, bit-exact vs torch's E4M3) | half the KV bytes: 262K on one GPU |
| persistent Triton/inductor cache + post-boot warm-up | boot 90 -> 40 s, no compile stall on the first request |

### Why one GPU can hold 128K, and 262K with FP8

vLLM's KV planner reserves room in every sliding-window and short-conv cache for the tokens in flight. With async
scheduling that is two prefill chunks per cache. The model has 12 such caches, so this reserve took 2.36 GiB per
request at 64K, more than 64K tokens of full attention take (2.25 GiB). `--no-async-scheduling` halves it, with
no measurable speed cost (A/B: decode 243 vs 242 tok/s, prefill 5.28K vs 5.29K tok/s). `SCONV_TAIL=1` then shrinks
the six short-conv reserves to each step's tail (window + drafts + one prefix-hit block), so 131K fits with full
1024-token prefill chunks.

262K needs the FP8 KV cache plus about 0.25 GiB that came from the memory vLLM keeps back after warm-up: smaller
prompt-logprob warm-up chunks (less allocator fragmentation to reserve for), CUDA graphs only up to 16 tokens, and a
smaller non-torch reserve so long prompts keep their split-KV attention buffers. The full budget and every A/B are in
[`docs/NOTES.md`](docs/NOTES.md#the-262k-memory-budget). The KV pool is 262,755 tokens and shared, so while one
request holds close to 262K tokens, other requests wait for room.

## Roadmap / help wanted

Ideas collected from this repo's notes and the other Ampere ports
([peaster](https://github.com/peaster/inkling-2-mini-vllm-2x3090), [HyperInkling](https://github.com/Pento95/HyperInkling),
the [single-3090 vLLM fork](https://github.com/Hiutaky/vllm/tree/ampere-port), quidow's flags,
[vllm#69165](https://github.com/vllm-project/vllm/pull/69165)). See [CONTRIBUTING.md](CONTRIBUTING.md) to help.

| # | item | expected effect | status |
|---|---|---|---|
| [#1](https://github.com/lulakien/inkling2-mini-3090-recipe/issues/1) | short-conv cache holds only each step's tail (window + drafts + one 64-token block), not the whole prefill chunk | ~1.7 GiB more KV per request on 1 GPU, bigger prefill chunks | **done** (`SCONV_TAIL=1`, 1-GPU profiles) |
| [#2](https://github.com/lulakien/inkling2-mini-3090-recipe/issues/2) | FP8 E4M3 KV cache, emulated on sm_86 (the model is built for a unit-scale FP8 cache) | ~2x context on both profiles | **done** (`KV_DTYPE=fp8`; 1 GPU: 262K; 2 GPUs: the `1m` profile) |
| [#3](https://github.com/lulakien/inkling2-mini-3090-recipe/issues/3) | more 2-GPU context: async off + larger `MAXLEN` (~3 GiB per card is unused at 262K) | 262K -> ~400K+ | **done** (`PROFILE=512k` bf16, `PROFILE=1m` FP8; see the long-context table) |
| [#4](https://github.com/lulakien/inkling2-mini-3090-recipe/issues/4) | multi-request throughput: decode attention split count, adaptive draft length, sm_86 expert-GEMM configs, more `MAXSEQS` | 445 -> 580 tok/s at 8 streams (others report 690-750) | **in progress**: draft length by batch size done (`SPEC_SCHED`); attention splits, GEMM configs, `MAXSEQS` open |
| [#5](https://github.com/lulakien/inkling2-mini-3090-recipe/issues/5) | numbers on other cards (3090 Ti, A5000, A6000, 4090), NVLink pairs, stock cards without gpu-unlock | coverage | **help wanted**: open a benchmark report (2x A40 reported, thanks buzz) |
| [#6](https://github.com/lulakien/inkling2-mini-3090-recipe/issues/6) | P2P via a patched open driver vs this repo's host-memory all-reduce, measured per all-reduce | 2-GPU decode | help wanted |
| 7 | rebase onto upstream Ampere support once vllm#69165 ships | less patching | waiting |

## Test machine

| | |
|---|---|
| GPUs | 2x NVIDIA GeForce RTX 3090 24 GB (GA102, VBIOS 94.02.42.00.B4), power limit 280 W each (stock 350 W) |
| GPU links | PCIe 4.0 x8 / x8, no NVLink, no P2P (`nvidia-smi topo`: PHB) |
| GPU firmware mod | [gpu-unlock](https://github.com/Zagitta/gpu-unlock) active on both cards (see below) |
| display | on the CPU's integrated Radeon graphics; both 3090s headless |
| CPU | AMD Ryzen 7 9700X (8 cores / 16 threads, Zen 5) |
| board | ASUS ProArt B850-CREATOR WIFI NEO (BIOS 1103) |
| RAM | 64 GB DDR5 |
| storage | Samsung 990 PRO 1 TB (models), WD Blue SN5000 1 TB |
| OS | CachyOS, Linux 7.3.5-2-cachyos, NVIDIA driver 620.73.04 (open kernel module) |
| container | Docker 29.10.0, NVIDIA Container Toolkit 1.20.1 |
| image | `vllm/vllm-openai:inkling-2-mini` @ `sha256:c2dc759f...` (vLLM 0.1.dev25855+g7cb5dae22, PyTorch 2.14.0+cu130, Triton 3.8.0, Python 3.14) |
| model | `thinkingmachines/Inkling-2-Mini` @ `ed40e7da625f594fc9c4990f5f66be24873c22d7` (Apache-2.0) |

### gpu-unlock

GeForce Ampere cards run BF16/FP16 tensor-core math with FP32 accumulation at half rate. Zagitta's
[gpu-unlock](https://github.com/Zagitta/gpu-unlock) kernel module lifts that limit at boot. Prefill uses exactly that
math (Humming W4A16 expert GEMMs, bf16 attention and dense GEMMs), so **the prefill numbers above depend on it**.
On the same machine with the earlier Qwen3.8-27B recipe, the unlock gave +37% prefill. Decode is memory-bandwidth
bound and does not change. With the unlock, these cards sustain 91.5 TFLOPS dense BF16 at 280 W
(`results/kernels/gemm_tflops.txt`); a stock 3090 is rated for 71 at boost clocks. Install notes for this machine
are in [`gpu-unlock/`](gpu-unlock/README.md). It is third-party software that reprograms the GPU: read its README
first. Check the GEMM rate before benchmarking (`tools/gemm_tflops.py`): a GPU reset after boot silently drops the
unlock while the module stays loaded (seen here once: 64 instead of 91 TFLOPS, prefill ~22% lower until a reboot).

## Limitations and known issues

- **Tied to one image build.** Every overlay replaces a whole file of that exact build (vLLM `g7cb5dae22`).
  Pull by digest (`launch/image.env`). A newer `:inkling-2-mini` tag will probably need the patches rebased.
  `patches/diffs/` shows every change.
- **Tested here only on RTX 3090 (sm_86).** A community report shows the 2-GPU profile on 2x A40 (vLLM built from
  source with these overlays, see above). Other 24 GB+ Ampere cards (3090 Ti, A5000, A6000) should behave the same
  but are untested. Ada (sm_89) is untested. One GPU needs 24 GB: the weights alone take 16.5 GiB.
- **The GPUs must be headless for the single-GPU profiles.** They allocate the whole card (GMU 1.0, 512 MiB margin).
  A desktop or a game on the same card makes boot fail or the server run out of memory under load. Shared cards are
  untested (try a smaller `MAXLEN` and `GMU` below 1.0). Another process using the GPU (even one that doesn't show in `nvidia-smi`, such as a
  game) also slows every number here.
- **The 2-GPU `1m` profile is for one long session that stays warm.** Its FP8 KV is converted in software, so a cold
  1.04M-token prompt takes 19.5 min (250K: 102 s vs 59 s on the default; 14.9 min with the opt-in
  `FAR_ATTN=1 MNBT=2048`). `512k` keeps bf16 and full prefill speed.
  Retrieval was checked with planted facts up to 1.04M, which is easier than multi-needle benchmarks like MRCR.
- **Not shipped:** the varloop research checkpoint (`LOOP_SHARE=1` works and halves its attention KV, but it scores
  19-20 MMLU questions below Inkling 2 Mini here) and 2DSD (its Inkling runner does not fit one 24 GB card yet).
  Both are written up in `experiments/long-context-2gpu/RESULTS.md`.
- **Tuned for one or a few users.** Up to 8 concurrent streams on 2 GPUs (`MAXSEQS`), 4 on one GPU. The KV pool is shared: on one GPU, two requests
  can't both use 128K (or, with the 262K profile, more than ~131K each).
- **The 262K single-GPU profile changes precision and is slower on long prompts.** Its FP8 E4M3 KV cache is
  converted in software (sm_86 has no FP8 instructions): decode steps are 3-5% slower, prefill 7% slower at 2K, 12% at
  16K and 30% at 127K than the 128K profile (254K takes 154 s). Temp-0 output diverges from bf16 within the first
  18-584 characters (8 greedy prompts, median ~330); the quality gates (MMLU, needles at 255K/262K, determinism) are unchanged. It leaves
  ~600 tokens of KV beyond 262,144 and no room for more: do not raise `CG_MAX` or `PLP_CHUNK` there.
- Lowering `KV_MARGIN_MB` below 512 boots but runs out of memory on the first long prefill. Do not.
- **Reasoning cannot be fully turned off** (model behaviour, see the model card): even `reasoning_effort: "none"`
  writes a short reasoning block. Leave room for it in `max_tokens`. Structured output applies after it.
- **Vision** (`MM=1`) is smoke-tested on 2 GPUs only (one image, correct answer; KV pool 284K tokens). It is
  untested on one GPU and with video. The default is text-only (`--language-model-only`).
- **The KV cache is bf16 by default.** `KV_DTYPE=fp8` (used by the 262K single-GPU profile) is a precision change,
  see above.
- **int8 weights** (attention qkvr, LM head, Markov head, drafter) are a deliberate weight change. MMLU and the
  needle tests show no loss (911 vs 908 bf16), but outputs differ slightly from bf16. `W8=` restores bf16
  (measured on 2 GPUs; on one GPU it leaves less room for context, untested).
- **Speculative decoding at temp 0 is not token-identical to plain greedy decoding** (bf16 batch-shape numerics). It is
  deterministic run to run (8/8). Quality is judged by task metrics, not token identity.
- **Prefix cache:** hits need 64-token-aligned shared prefixes (128 with FP8 KV). With `SCONV_TAIL=1` (both
  single-GPU profiles) a prompt that diverges mid-message from a cached one hits only up to the last 1024-token
  prefill chunk boundary (13K agent probe: 12,288 of 12,608 shared tokens). The retention interval stores extra blocks
  per cached prefix. With many distinct long prefixes, use `EXTRA="--prefix-cache-retention-interval 2048"`.
- **MMLU here is a 1,140-question subset** scored by letter logits. It is a regression gate, not a reproduction of the
  model card.
- Numbers are at a 280 W cap with gpu-unlock. 350 W measured: +5% prefill, +3% decode (see Results).
  2-GPU prefill is also limited by PCIe x8/x8 all-reduces.
- **The first boot compiles kernels (~2 min).** They are cached in `~/.cache/inkling2-vllm` (`CACHE_DIR`). Delete it
  after changing patches.

## Layout

```
launch/     serve.sh (all switches), 2gpu.sh (PROFILE=262k|512k|1m), 1gpu.sh (PROFILE=128k|262k), image.env (pinned image digest)
patches/    files mounted over the image (+ hostar/ host-memory collectives, diffs/ vs the stock files)
tests/      run_suite.sh and the tests above, data/ (MMLU subset), kernels/ (bit-exactness harnesses)
tools/      fetch_haystack.sh, gpu_summary.py, gemm_tflops.py, make_diffs.sh, env_report.sh (for issues)
results/    raw JSON per profile: 2gpu, 1gpu_128k, 1gpu_262k, 2gpu_port_only, 2gpu_nospec, 2gpu_vision, kernels;
            old/ has superseded single-GPU runs (64K, 512-token 128K, development runs);
            community/ has reports from other hardware (2x A40)
experiments/ long-context-2gpu: FP8 / SCONV_TAIL / varloop shared-KV matrix, second-agent test, 2DSD attempt;
            concurrency: draft length by batch size, warm-up coverage, long-prefill cap, bigger chunks
docs/       NOTES.md: engineering notes, where the time goes, what was tried and rejected
gpu-unlock/ how this machine keeps the unlock boot entry current (CachyOS + Limine specific)
```

## Contributing

Benchmark reports from other cards, bug reports, ideas and patches are welcome: see [CONTRIBUTING.md](CONTRIBUTING.md)
and the issue templates.

## License

Apache-2.0. Most patched files are derived from vLLM (Apache-2.0) and two from Triton (MIT); their original
license headers are kept.
The MMLU subset in `tests/data` comes from [cais/mmlu](https://huggingface.co/datasets/cais/mmlu) (MIT).
