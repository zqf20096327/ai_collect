# SingleSpark — Qwen3.8-Flash-Next on one NVIDIA DGX Spark, at 44 tokens per second

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Hardware](https://img.shields.io/badge/NVIDIA-DGX_Spark_%28GB10%29-76B900?style=flat&logo=nvidia&logoColor=white)](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)
[![Model](https://img.shields.io/badge/%F0%9F%A4%97-Qwen3.8--Flash--Next-yellow)](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)
[![Quantization](https://img.shields.io/badge/quantization-NVFP4_%2B_FP8_hybrid-orange?style=flat)](#what-is-inside)
[![Single request](https://img.shields.io/badge/single_request-44_tok%2Fs-brightgreen?style=flat)](#what-you-get-measured)
[![Runtime](https://img.shields.io/badge/runtime-vLLM-red?style=flat)](https://docs.vllm.ai/)
[![Status](https://img.shields.io/badge/status-experimental-red?style=flat)](#what-you-get-measured)

**Experimental, and fast.** A 180-billion-parameter mixture-of-experts model,
running whole on a single desktop machine, answering at **44 tokens per second**
— with the quality cost of getting it there measured and published rather than
asserted.

One command installs it. It speaks the OpenAI API, so any chat client, agent
framework or IDE plugin that already talks to OpenAI talks to this.

```bash
git clone https://github.com/albond/SingleSpark-Qwen3.8-Flash-Next.git
cd SingleSpark-Qwen3.8-Flash-Next && ./install.sh
```

## Why this is hard

`Qwen/Qwen3.8-Flash-Next` is 125B total parameters with 6B activated, plus a
51B n-gram embedding table and a 4B multi-token-prediction layer — about 180B
resident. Qwen describes it as the lightweight architecture ahead of Qwen4, and
it is a strong model: on published evaluations it beats a dense 27B on
real-world work tasks and agentic terminal use.

The published FP8 checkpoint is **172.78 GiB**. An NVIDIA DGX Spark has **128 GB**
of unified memory. FP8 does not fit, and nothing upstream validates a
single-device configuration at all — vLLM's own recipe for this model starts at
four GB300s.

So this runs it from a four-bit NVFP4 checkpoint, converts the dense
projections to blockwise FP8, holds the output projection at eight bits, and
drafts with a product-quantized speculative head. Every one of those is a
quality risk, so every one of them is gated.

**If that trade is not the one you want**, the same author's
[DenseSpark-Qwen3.8-27B](https://github.com/albond/DenseSpark-Qwen3.8-27B)
serves a dense 27B on the same DGX Spark. It is a smaller model that fits with
room to spare, and it ships nothing that fails its quality gate. Two honest
options: a bigger model with the drift published, or a smaller one with none to
publish.

## What you get, measured

One NVIDIA DGX Spark (GB10), single stream, **65,536-token context**, eager
execution, speculative depth 3. Three prompt classes, one warm-up each, three
retained runs, one process start, prefill excluded by timing from the first
streamed token.

| prompt | tok/s | spread (tok/s) | tokens/step | target step |
|---|---:|---:|---:|---:|
| question | 45.64 | 0.97 | 2.543 | 55.72 ms |
| code | 43.34 | 0.08 | 2.395 | 55.27 ms |
| prose | 42.88 | 2.30 | 2.354 | 54.89 ms |
| **cross-prompt median** | **43.34** | — | — | **55.27 ms** |

The shipped window moved from 8,192 to 65,536 in 1.2. Both were measured, and
the smaller one is still one environment variable away:

| context | cross-prompt median | target step | engine's max concurrency |
|---:|---:|---:|---:|
| 8,192 | 43.81 tok/s | 54.32 ms | 10.69x |
| 32,768 | 43.51 tok/s | 55.75 ms | 3.04x |
| **65,536, shipped** | **43.34 tok/s** | **55.27 ms** | **1.70x** |

Eight times the window costs **1.7% of the step** and 1.1% of the rate. That is
the price of *declaring* a larger window — block-size and layout effects —
because all three of those rows decoded 300 tokens from a short prompt. **What
a genuinely long request costs is not measured here**; see Known limits.

The same image with the FP8 conversion switched off gives 34.36 tok/s and a
69.34 ms step. **The step is 22% shorter** — that pair was measured against
each other at 8,192, so it is 69.34 ms against the 54.32 ms row above, not
against the shipped 55.27.

The median is published rather than the mean, because the mean is pulled up by
the fastest shape: these three average 43.95 tok/s. **The spread column is the
range of three retained runs in tok/s, not a percentage** — 0.08 on the code
shape here against 2.30 on prose, where the 8,192 capture had 2.52 and 0.94. It
moves that much between captures because accepted tokens per step depends on
what the model actually generates, and at 300 tokens the three runs of a prompt
do not always generate the same thing. A single run is not representative;
three runs and a median absorb some of that, and not all of it.

Check it yourself against your own server:

```bash
./bench_singlespark.py --runs 3
```

### The same server on another project's benchmark

[GB10-3.8-Flash-Next](https://github.com/azampatti/GB10-3.8-Flash-Next) serves
this model on the same hardware under SGLang and publishes a table of its own,
measured with its own `sgbench.sh`. That script was run against this server,
unchanged apart from the port it dials:

| workload | its published figure | this build, its script |
|---|---:|---:|
| Q&A | 35.2 | 50.7 |
| Code | 38.4 | 55.3 |
| JSON | 43.9 | 63.2 |
| Math | 42.7 | 49.6 |
| LongCode | 43.6 | 53.6 |

The two tables measure different things and neither is wrong. Its panel includes
JSON and long code continuation, the most predictable output shapes there are
and so the ones where speculative decoding earns most; the panel above scores
higher than this project's three-shape panel on the same server in the same
hour. Its script also divides completion tokens by the whole request, so prefill
sits in its denominator where this project's decode figure excludes it — which
makes its own published numbers conservative, not generous. And its column was
measured on its own machine with its own checkpoint; nothing here has run its
runtime.

```bash
curl -fsSLO https://raw.githubusercontent.com/azampatti/GB10-3.8-Flash-Next/main/sgbench.sh
sed -i 's/localhost:30000/localhost:8000/' sgbench.sh && bash sgbench.sh
```

### Two things about that number

**The reasoning trace is counted.** This model thinks before it answers. Those
tokens cost exactly as much to generate as any other, so they are timed and
counted. A benchmark that recognises only the answer field measures a shorter
window against the same budget and reports about twice the truth — this
project's own instrument did that until it was caught. A figure measured with
reasoning disabled is a different quantity and is not comparable to the table.

**The target step is the honest half.** Output tokens per second is a step time
multiplied by a speculative acceptance rate, and acceptance moves whenever the
output moves. The step is what an optimisation has to move; the rate is what
you feel.

### Quality, and the limit of the claim

Paired teacher-forced mean negative log-likelihood against the BF16-dense
control, over 23,988 frozen positions: **+0.003277 nat/token**, standard error
0.003174, against a +0.005 threshold declared before the run. Greedy repeats
were identical 9 of 9 at eight lengths from 32 to 1,024 tokens.

That bounds movement in the model's own predictive distribution on one corpus,
and it cannot see a change to state carried between decode steps — it returns
exactly zero for one. Task accuracy is measured separately, on 210 questions
with computed answers and long reasoning chains, and is reported above for the
recurrent-state change.

**Neither is an agentic measurement.** Nothing here says what drift costs across
fifty tool-using steps, which is exactly where four-bit conversion is most
likely to hurt and exactly where this model's published advantage lives. The
claim is as narrow as it is written, and that is deliberate: the alternative is
a promise nobody checked.

## What you need, and what gets installed

`./install.sh` checks every prerequisite before it downloads anything, reports
all of the missing ones at once with the command that fixes each, and does not
stop at the first.

| prerequisite | tested with | if it is missing |
|---|---|---|
| NVIDIA driver | 580.173.02 (CUDA 13.0) | install your distribution's driver |
| Docker Engine, usable without `sudo` | 29.2.1 | [docs.docker.com](https://docs.docker.com/engine/install/ubuntu/), then `sudo usermod -aG docker $USER` |
| NVIDIA Container Toolkit | — | `sudo apt install -y nvidia-container-toolkit && sudo nvidia-ctk runtime configure --runtime=docker` |
| python3 | 3.12.3 | `sudo apt install -y python3` |
| python3 `torch` | 2.13.0+cu130 | needed on the host by the two artifact builders |
| python3 `safetensors` | 0.8.0 | `python3 -m pip install safetensors` |
| coreutils (`df`, `readlink`) | — | `sudo apt install -y coreutils` |
| free disk under `$HOME` | 210 GB | 101 GiB checkpoint, 2.7 GiB hybrid weights, the image |

Nothing else lands on the host. Everything the server runs lives in the
container image, pinned by digest:

| inside the image | version |
|---|---|
| base image | `vllm/vllm-openai@sha256:3b0e188f…54477e` (arm64) |
| vLLM | 0.1.dev20073+g8e685d198 |
| PyTorch | 2.13.0+cu130 |
| torchvision | 0.28.0+cu130 |
| Triton | 3.7.1 |
| transformers | 5.15.1 |
| FlashInfer | 0.6.17 |
| RunAI model streamer | 0.16.1 |
| NumPy | 2.2.6 |
| xgrammar | 0.2.3 |
| Starlette / FastAPI | 1.6.0 / 0.136.3 |
| CUDA (torch) | 13.0 |

The only things outside the image are the checkpoint and the hybrid built
beside it under `~/.cache/huggingface`, and the draft head's structure under
`~/.cache/singlespark`.

## Tested environment, and what is not claimed

| component | tested value |
|---|---|
| hardware | NVIDIA DGX Spark, GB10, compute capability 12.1, 128 GB unified memory |
| OS | Ubuntu 24.04.4 LTS, aarch64, kernel 6.17 |
| checkpoint | `starkweatherdigital/qwen3.8-flash-next-nvfp4`, revision `1b304e5f` |

Every number here was measured on one machine with the protocol beside it. What
is **not** measured, and therefore not claimed:

- **Concurrent serving.** Every number here is single stream. The concurrency
  figures quoted beside the context windows are the engine's own startup
  arithmetic for how many requests of that size its pool could hold; no
  concurrent load was ever run against this server.
- **A request that actually fills the window.** The shipped context is 65,536
  and all three measured windows decoded 300 tokens from a short prompt. Long
  prefill, decode against a filled cache, and retrieval across the window are
  unmeasured. Windows above 65,536 are unmeasured entirely.
- Multimodal requests. The checkpoint has a vision tower; it is not exercised.
- General task accuracy, and agentic accuracy in particular. A 210-question
  probe with computed answers is reported above for the recurrent-state change;
  it is not a benchmark score, and nothing here measures accuracy across a long
  tool-using chain.
- Any other machine, driver, or checkpoint revision.

Version drift is the likeliest way this stops working. The image is pinned by
digest and every transform aborts rather than editing when the installed source
does not match its anchor, so a changed dependency fails at build time with the
file it could not patch — not silently at inference.

## Install

```bash
./install.sh
```

It checks every prerequisite before downloading a hundred gigabytes, then
fetches the base checkpoint, builds the hybrid FP8 checkpoint beside it, trains
the draft-head artifact, builds the runtime image, and confirms that Docker can
actually reach the GPU. On failure it writes one diagnostics file and stops.
Nothing is installed outside Docker and your Hugging Face cache.

The base checkpoint is
[`starkweatherdigital/qwen3.8-flash-next-nvfp4`](https://huggingface.co/starkweatherdigital/qwen3.8-flash-next-nvfp4);
its licence is the upstream model's.

## Run

```bash
SNAPSHOT="$HYBRID" ./configs/launch-release.sh
```

`install.sh` prints the exact `HYBRID` path when it finishes. The server speaks
the OpenAI API on `127.0.0.1:8000`.

```bash
SNAPSHOT="$HYBRID" BIND=0.0.0.0 DETACH=1 ./configs/launch-release.sh
docker logs -f singlespark          # follow the load
./configs/smoke-test.sh             # health, model list, coherence, decode
./bench_singlespark.py              # reproduce the table above
docker rm -f singlespark            # stop
```

`BIND=0.0.0.0` reaches it from another machine — read [SECURITY.md](SECURITY.md)
first, this server has no authentication of its own. `DETACH=1` returns the
terminal. Plumbing knobs: `IMAGE`, `PORT`, `GPU_MEM`, `BIND`, `DETACH`. Two more
change what is being measured rather than how it is reached, and both say so
when you move them.

### The context window is CTX, and you may raise it at your own risk

`CTX` defaults to **65,536**, which is what the table above describes. Both
`install.sh` and the launcher accept it, and the installer prints the serve
command with whatever you chose:

```bash
CTX=131072 ./install.sh
CTX=131072 SNAPSHOT="$HYBRID" ./configs/launch-release.sh
```

Three windows have numbers — 8,192, 32,768 and 65,536 — and they sit within
1.7% of each other on the step. **Above 65,536 nothing here has been measured:
no rate, no step, no quality.** The model carries 262,144 positions natively, so
the limit is memory rather than the checkpoint, and only twelve of its
forty-eight layers keep a KV cache. Asked for the full 262,144 at this memory
envelope the engine refused and named its own ceiling:

> To serve at least one request with the model's max seq len (262144), 7.08 GiB
> KV cache is needed, which is larger than the available KV cache memory
> (4.41 GiB). Based on the available memory, the estimated maximum model length
> is 158080.

It prints `GPU KV cache size: N tokens, Maximum concurrency for CTX tokens per
request` at startup and refuses rather than failing later, so a window that is
too large fails immediately. Read that line: below 1.00x it will not start.

### The recurrent state is BF16, and that came from a neighbour

The idea is [GB10-3.8-Flash-Next](https://github.com/azampatti/GB10-3.8-Flash-Next)'s:
it moves the Gated DeltaNet recurrent state off the FP32 the checkpoint asks
for. Taken here, measured, and carried further.

BF16 halves the recurrent state a target step moves and takes **3.2% off the
step** against a matched same-day control at 8,192, 56.13 ms to 54.32. Measured
against the step this README published before the change, 55.41 ms, it is 2.0%;
the two controls are the same configuration measured hours apart, and that gap
is the honest size of this box's run-to-run drift. FP16 was tried as the obvious
improvement — same two bytes, eight times the mantissa — and is **slower than
FP32 itself** at 58.46 ms. Disassembling the shipped kernel says why: it is
templated on the state type and only `__nv_bfloat16` and `float` are compiled,
so FP16 cannot enter the fused CUDA path and falls back to Triton. That is a
different kernel, not a conversion cost.

Quality was measured rather than assumed, because the frozen-vector gate cannot
see a change to state carried between decode steps — it returns exactly zero
here with every logprob identical. Over 210 questions with computed answers and
long reasoning chains, paired: **-2.0 points, McNemar p = 0.45**, and greedy
repeats stay byte-identical.

**That is "not established", not "no difference", and this README said the
stronger thing first.** A third of the hardest task family never reached an
answer at all — it ran out of the token budget mid-reasoning — so the headline
partly measures whether the model can close a chain in the budget. Restricting
the comparison to items where both settings actually finished, BF16 loses three
of twenty-nine counting items and one of a hundred and thirty-eight mixed items,
and gains none. One-directional, far too small to call at these sample sizes,
and **not excluded**. The larger counting run that would settle it has not been
done.

`SSM_STATE=float32` restores the checkpoint's precision at the cost above.
Nothing falls back silently: the launcher always passes the flag explicitly and
`configs/smoke-test.sh` exits non-zero if the engine applied anything else.

## Using it from a chat client or an agent

Point any OpenAI-compatible client at `http://<host>:8000/v1` with model
`singlespark-qwen3.8-flash-next`. No API key is required or accepted.

**Reasoning.** The server runs a reasoning parser, so the trace arrives in a
`reasoning` field and the answer in `content`, clean and without a stray
`</think>` in the middle of it. Note the field name: `reasoning`, not
`reasoning_content`, which stays empty. A client that looks only for
`reasoning_content` simply shows the answer, which is usually what you want.

**Budget.** The trace is generated before the answer, so a small `max_tokens`
can be consumed entirely by it and the answer never arrives — a 16-token budget
here produced five reasoning chunks and no content at all. Give it room.

**Tool calling** works: send `tools` with `tool_choice: "auto"` and structured
`tool_calls` come back. A request without `tools` is unaffected.

## What is inside

| transform | what it does |
|---|---|
| `01-ple-nvfp4-loader` | loads the four-bit n-gram table, resident and packed |
| `03`, `04` | holds the 248,320-row output projection at eight bits, pinned Triton kernel |
| `05`, `06` | product-quantized draft head: 16.9 MiB of codebooks replacing a 606 MiB scan |
| `10-fp8-hybrid` | serializes 309 dense projections as blockwise FP8 beside the four-bit experts |
| `11-mtp-atomic` | extends that to the draft layer, reduction override scoped to one module |

Each is a text edit of the installed runtime, applied at image build time. Each
aborts without editing when its anchor does not match, is idempotent, and is
inert unless its own environment variable is set. Several transforms in the tree
are **default off because they were measured and lost** — the negative result is
the useful part, and it is cheaper to read than to rediscover.

### The kernels were read, not assumed

GB10 is compute capability 12.1. The kernels a profiled decode step actually
spends its time in were disassembled and matched against that instruction set,
and then — in this release — counted while they ran. **98.02% of GPU kernel time
is accounted for by name**, including the cuBLAS and cuBLASLt kernels that no
name-indexed disassembly can reach, because a profiler that reads hardware
counters does not need a symbol table. Three results are worth stating because
none of them is what a reader would guess.

The mixture-of-experts grouped GEMM — the single largest component of a decode
step, at 38.5% of GPU kernel time — issues
`OMMA.SF.16864.F32.E2M1.E2M1.UE4M3.4X`, the chip's native four-bit blockscaled
tensor instruction. Its module carries 2,972 kernels and only 64 of them reach
that instruction; the engine launches one of the 64. There is nothing faster to
move it to.

And the vendor libraries ship 8,513 embedded cubins between them, of which
**four are built for compute capability 12.1 — and all four hold nothing but a
hardware-detection stub.** That is a statement about cubins shipped ahead of
time, and it is not the whole picture: cuBLASLt links NVRTC and builds kernels
while the server runs, naming each one after the architecture it built it for.
Three kernels named `nvjet_sm121_*` appear in the profiled step — 198 launches,
6.0446 ms. They are in none of the 8,513 cubins because they did not exist until
the process compiled them.

Third, the whole instruction stream of one decode step was counted rather than
inferred: **1,634,850,612 warp instructions per target step, 650,298,573 per
accepted token, across 317 distinct opcode forms.** This chip issues at most
48 SMs × 4 schedulers × 2.418 GHz, so the 54.15 ms step this was captured at —
at the 8,192 window, before the default moved — has 25.1 billion issue slots and
uses **6.50%** of them. Priced into issue time the stream models out
at 8.816 ms against that step, and **46.3% of that is one instruction** — the
four-bit tensor op above, which has nothing narrower to move to. The largest
non-tensor opcode in the step, `LOP3.LUT`, is worth 0.59% of it.

That 8.816 ms is a modelled floor, not a measurement, and two things in it are
assumptions rather than counts. **82.1% of the instructions have no measured
rate on this box** and are costed at the scheduler ceiling, which is the most
favourable rate available, so every "available" figure derived from it
over-states what removing those instructions could buy. And **the rate for the
tensor op carrying 46.3% of the model is derived, not measured here** — it
comes from a sibling experiment whose witness issues the same instruction with
a different scale format. The count of instructions is a count; their price is
a model.

No speed change follows from any of this, and that is the finding: the step is
bound by memory bandwidth, not by instruction selection. What that used to be
was an inference from a byte model. It is now a count.

## Known limits

- **Greedy output is not reproducible across speculative depths.** The target
  reduces in a different geometry at verify width 1+K than at width 1, so two
  arms at different depths produce different, equally valid text.
- **Repeats are byte-identical at a fixed seed, and the seed matters.** With
  `seed` set, a 500-token greedy completion repeated inside one server lifetime
  and again after a cold restart produced the same SHA-256. Without one, the
  benchmark's own captures disagree between repeats of the same prompt at
  `temperature: 0` — the server-reported completion length differs, in every
  capture, on every prompt that finishes before its token cap. **Send a seed if
  you need reproducibility.** What has been shown reproducible without one is a
  fixed forward pass: scoring a frozen token sequence gives identical logprobs
  at every length tested.
- **Reproducibility of a fixed forward pass is lost past the first prefill chunk
  boundary**, at about position 2,051. Below it, repeated scoring is
  byte-identical. That measurement is about scoring, not about generation.
- Prefix caching is off: not safe on the pinned hybrid-cache path.
- **CUDA graphs are not enabled.** An early attempt at the wrong configuration —
  every capture size, both graph modes — exhausted unified memory and made the
  host unresponsive. A narrower configuration has since captured a 0.06 GiB
  graph pool in three seconds, and it is not promoted: the screen that measured
  it cannot separate the gain from what the three runs of a prompt generated.
- The shipped context is 65,536 tokens and the model's own limit is 262,144.
  Asked for the full 262,144 at this memory envelope the engine refused and
  estimated its own ceiling at 158,080. Windows above 65,536 are not measured
  here, and the launcher says so.
- **A genuinely long request is not measured.** Every published context number
  decoded 300 tokens from a short prompt, so what is priced is declaring the
  window, not filling it. A 60,000-token prompt pays a prefill nobody here has
  timed and a decode against a far larger KV cache.

## The pair

These two are published together because a reader arriving at either one is
choosing between them:

| | model | disposition |
|---|---|---|
| [DenseSpark-Qwen3.8-27B](https://github.com/albond/DenseSpark-Qwen3.8-27B) | dense 27B | measured and quality-gated; run it if you want a known answer |
| **SingleSpark** (this) | 180B mixture-of-experts at four bits | experimental; a bigger model, with the drift measured and published |

Same machine, same method, same discipline about numbers. Different bet.

## Repository layout

```text
.
├── install.sh                    one command: prerequisites, checkpoint,
│                                 hybrid weights, draft head, image
├── bench_singlespark.py          the decode measurement behind the table above
├── configs/
│   ├── launch-release.sh         the published profile — the one to use
│   └── smoke-test.sh             health, model list, coherence, one decode
├── docker/Dockerfile             the pinned image and every build step
└── patches/                      one directory per transform, each anchored,
                                  idempotent and self-verifying
```

## Attribution

The blockwise-FP8 conversion of the dense projections was reproduced here after
studying the Apache-2.0 implementation in
[blazux/qwen3.8-Flash-DGX](https://github.com/blazux/qwen3.8-Flash-DGX/tree/209646cd98290035ccbddef29b14c460460a8709),
which in turn credits Saren-Arterius's AutoRound implementation.
`patches/10-fp8-hybrid/singlespark_fp8_hybrid.py` records that lineage at the
top of the file. It is a reimplementation for this checkpoint's layout, not a
copy.

The BF16 recurrent state shipped here is
[azampatti/GB10-3.8-Flash-Next](https://github.com/azampatti/GB10-3.8-Flash-Next)'s
idea (Apache-2.0), taken from its SGLang configuration and carried further: FP16
tested and rejected against the disassembled kernel, and the quality cost
measured on task accuracy rather than assumed. Its FP8 KV cache setting does not
port — vLLM's sparse-attention layer refuses any non-BF16 KV cache at model
init. No code was copied; the flags were read from its installer and reproduced
against vLLM's own equivalents.

Every other transform here was written from the measurements in this
repository.

## Licence

MIT. See [LICENSE](LICENSE). The checkpoint and the runtime it patches carry
their own.

---

Keywords: run Qwen3.8-Flash-Next locally, NVIDIA DGX Spark, GB10, self-hosted
LLM, local inference, 180B mixture-of-experts on one GPU, NVFP4 four-bit
quantization, blockwise FP8, vLLM, OpenAI-compatible API, speculative decoding,
multi-token prediction, single-machine large language model serving.
