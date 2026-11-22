<div align="center">

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo-dark.png">
    <img src="assets/logo.png" width="420" alt="megakernel zoo">
  </picture>
</p>

**Model-specific megakernel inference engines for LLM decoding, written by coding agents**

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB.svg?logo=python&logoColor=white)](pyproject.toml)
[![CUDA](https://img.shields.io/badge/CUDA-13.x-76B900.svg?logo=nvidia&logoColor=white)](#installation)
[![GPUs](https://img.shields.io/badge/GPU-H100_%7C_B200-76B900.svg)](#supported-models)
[![Blog](https://img.shields.io/badge/Blog-A_Megakernel_per_Model-1f5db8.svg)](https://dangxingyu.github.io/megakernel/)

[Blog post](https://dangxingyu.github.io/megakernel/) | [Benchmark data](https://dangxingyu.github.io/megakernel/full.html) | [Quick start](#quick-start) | [Benchmarks](#benchmarks) | [Build your own engine](#build-your-own-engine) | [Contributing](CONTRIBUTING.md)

</div>

<p align="center"><img src="assets/demo.gif" width="860" alt="The same question answered by a megakernel engine and by the fastest general engine on the same GPU, replayed at the recorded speed"></p>

**megakernel-zoo** is a collection of LLM inference engines, each built for exactly one checkpoint on one GPU
architecture. A megakernel runs the whole decode step (every transformer layer, choosing the next token and feeding it back)
as one GPU program: one persistent CUDA kernel for the steady-decode engines, a
device-scheduled kernel loop for the serving engines. Between tokens there is no kernel launch per operator and no
synchronization with the host, and the work split, weight layout and memory traffic are fixed at compile time for the
checkpoint's shapes.

Every engine in this repository was written by a coding agent (Claude) in an autonomous optimization run against a fixed
evaluator, and audited afterwards. The repository contains the engines, an OpenAI-compatible server for them, the
evaluator and benchmark suite, and the tooling to run the same kind of optimization on another model or GPU.

- With the checkpoint's own number formats (track A), steady decoding is 1.13–1.77× as fast as the fastest general
  engine on the same GPU (vLLM, SGLang, or Cohere's megakernel for North Mini Code) with one sequence, on nine models
  from 8 B to 594 B parameters. With lossless model-specific weight storage (track B) it reaches 2.05×.
- With exact speculative decoding on Inkling-2-Mini's own draft head (track C), one sequence decodes at 1.26 ms per
  token on one B200 (0.80 ms on natural text), 1.24× as fast as vLLM's speculative decoding (1.09× on natural text),
  whose output is not lossless.
- On a production request trace at 8 requests per second, the Inkling-2-Small serving engine keeps 99.2% of requests
  within the service levels (SGLang 81.7%). Its longest stall is 0.15 s (SGLang 4.4 s).
- `mkserve` serves any engine through the OpenAI completions and chat-completions API, with streaming and sampling.
- An engine is timed only after its logits match an FP64 reference of the model at every position. The evaluator
  and the reference builder are in the repository.
- [`runs/`](runs) has the source, the hypothesis and the score of every submission of the agent runs.

## News

- **2026-11-22** A faster track-C engine for Inkling-2-Mini: its draft head now runs inside the track-A megakernel,
  1.26 ms per token with one sequence (was 1.53) and 0.80 ms on natural text (was 1.02), 1.24× and 1.09× vLLM with
  DSpark; at 8 sequences it decodes like track A (5.08 ms, was 6.30). Records of three more runs in `runs/`.
- **2026-11-21** Inkling-2-Mini (26 B, MoE; 12 of its 24 layers run three times per token) on one B200: track-A and
  track-B engines, 1.36× and 1.38× as fast as vLLM with one sequence and even with it at eight, and the first track-C
  engine: exact speculative decoding with the checkpoint's MTP draft head, whose greedy tokens are exactly its own
  one-token-per-step tokens. `mkserve serve thinkingmachines/Inkling-2-Mini --track C`; 22 engines for 9 models; the
  records of the seven Inkling-2-Mini runs are in `runs/`.
- **2026-11-18** Engines for three more models: gpt-oss-20b (H100), Qwen3-32B and gpt-oss-120b (B200), and newer
  steady-decode engines for Qwen3-8B; 19 engines for 8 models in all. `scripts/check_engine.py` checks an engine before a
  pull request, and [CONTRIBUTING.md](CONTRIBUTING.md#your-own-hidden-set) shows how to build your own hidden test set.
- **2026-11-17** New `mkserve` commands `doctor`, `pull`, `chat` and `bench`; options `--api-key` and `--served-model-name`; a
  `/metrics` endpoint. The autoresearch kit adds a phase profiler for persistent kernels, a bit-identity check between two
  builds, and a playbook of what the earlier runs measured.
- **2026-11-16** Initial release: 13 engines for 5 models on H100 and B200, `mkserve`, the evaluation suite and the
  autoresearch kit. Write-up: [A Megakernel per Model](https://dangxingyu.github.io/megakernel/).

## Contents

- [Supported models](#supported-models)
- [Installation](#installation)
- [Quick start](#quick-start)
- [Benchmarks](#benchmarks)
- [Evaluation suite](#evaluation-suite)
- [Build your own engine](#build-your-own-engine)
- [Repository layout](#repository-layout)
- [Limitations](#limitations)
- [Citation](#citation)

## Supported models

| Model | Parameters | GPU | Steady-decode engines | Serving engines |
|---|---|---|---|---|
| [Qwen/Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B) | 8.2 B, dense | 1 × H100 | track A, track B | track A, track B |
| [CohereLabs/North-Mini-Code-1.0](https://huggingface.co/CohereLabs/North-Mini-Code-1.0) | 30.5 B, MoE (128 experts per layer) | 1 × H100 | track A, track B | – |
| [openai/gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b) | 20.9 B, MoE (32 experts per layer, MXFP4 experts) | 1 × H100 | track A, track B | – |
| [RecursiveSI/flint](https://huggingface.co/RecursiveSI/flint) | 39.8 B, MoE (256 experts per layer) | 1 × B200 | track A, track B | – |
| [Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) | 27.8 B, dense | 1 × B200 | track A, track B | – |
| [Qwen/Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) | 32.8 B, dense | 1 × B200 | track A, track B | – |
| [openai/gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b) | 116.8 B, MoE (128 experts per layer, MXFP4 experts) | 1 × B200 | track A, track B | – |
| [thinkingmachines/Inkling-2-Small](https://huggingface.co/thinkingmachines/Inkling-2-Small) | 594 B, MoE (384 experts per layer, 4-bit experts) | 4 × B200 | track A, track B | track A |
| [thinkingmachines/Inkling-2-Mini](https://huggingface.co/thinkingmachines/Inkling-2-Mini) | 26.2 B, MoE (128 experts per layer, 4-bit experts; 12 of its 24 layers run three times per token) | 1 × B200 | track A, track B, track C | – |

**Track A** keeps the checkpoint's weights, number formats and data flow, and changes only how the computation is
organized on the GPU. **Track B** may additionally change how the model is stored and what is precomputed at load time,
as long as the function is unchanged in exact arithmetic (no quantization, pruning or approximation). The track-B engines
of flint, Qwen3.8-27B, Qwen3-32B, gpt-oss-120b, Inkling-2-Small and Inkling-2-Mini are bit-identical to track A. The
other three are not: Qwen3-8B keeps the residual stream in FP32, gpt-oss-20b pre-multiplies the router weights by the
norm weights in FP32, and North Mini Code adds its rare out-of-range weights in a separate pass, so the sums are rounded
in another order.

**Track C** is exact speculative decoding: the engine drafts several tokens with the checkpoint's own draft head (the
MTP head of Inkling-2-Mini) and checks them with its track-A decode step in one pass. With greedy decoding its tokens are
exactly the ones its own one-token-per-step path produces, for every sequence; the evaluator checks that instead of
allowing for ties, and counts time per token by the tokens received, since a speculative server sends several tokens
at once. Track C is compared only with the general engines' own speculative decoding, whose output is not lossless.

A **steady-decode** engine holds up to 8 sequences and a 2,048-token context and is the fastest at decoding. A **serving**
engine admits requests while others decode, processes prompts in chunks inside the kernel, pages K/V memory and reuses
shared prompt prefixes (64 sequences, 34,816-token context).
Serving engines exist so far for two models at the two ends of the range, Qwen3-8B on one H100 and Inkling-2-Small on
four B200: each takes an agent run of its own against the request-trace evaluator. For the other models, a serving engine
can start from `engines/qwen3-8b_h100/online-a` with the [autoresearch kit](#build-your-own-engine); contributions are
welcome ([CONTRIBUTING.md](CONTRIBUTING.md)).

## Installation

**Prerequisites**

- The GPU an engine was built for: NVIDIA H100 (sm_90a) or B200 (sm_100a); Inkling-2-Small needs a node with four B200.
- CUDA toolkit 13.x with `nvcc` on `PATH` (engines are compiled from source on first use). Tested with CUDA 13.2.
- Python 3.10 or newer and PyTorch with CUDA support. Tested with Python 3.12 and PyTorch 2.15.

**Install from source**

```bash
git clone https://github.com/dangxingyu/megakernel-zoo.git
cd megakernel-zoo
pip install -e .            # installs the `mkserve` command
```

The evaluation scripts create their own environments with [`uv`](https://docs.astral.sh/uv/).

## Quick start

Check the machine, list the engines and serve one (the weights are downloaded from Hugging Face; `--model-dir` uses a
local snapshot):

```bash
mkserve doctor Qwen/Qwen3-8B                         # GPU, CUDA toolkit, Python packages, engines for this GPU
mkserve list
mkserve serve Qwen/Qwen3-8B --port 8000              # the default engine of this model on this GPU
mkserve serve Qwen/Qwen3-8B --engine offline-b       # a specific engine
```

Then talk to it, or time it on the benchmark workload (the same command times vLLM or SGLang with `--url`):

```bash
mkserve chat
mkserve bench --batch 1 8
```

Query it with any OpenAI-compatible client:

```python
from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:8000/v1", api_key="none")
stream = client.chat.completions.create(
    model="Qwen/Qwen3-8B",
    messages=[{"role": "user", "content": "Explain how a hash table works."}],
    max_tokens=512,
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="", flush=True)
```

`mkserve` validates every request before the engine sees it (context length, token ids, `max_tokens`) and implements
sampling (`temperature`, `top_p`, `top_k`, `seed`) on the engine's logits. An engine is tied to one model and one GPU
type; any other pair is refused. See [`mkserve/README.md`](mkserve/README.md) for endpoints and options.

<details>
<summary><b>All registered engines</b></summary>

| Model | GPU | Engine | Track | Kind | Sequences | Context | From |
|---|---|---|---|---|---|---|---|
| Qwen/Qwen3-8B | h100 | `online-b` (default) | B | online | 64 | 34,816 | run s3-q8b-online-a1, submission s0039 |
| Qwen/Qwen3-8B | h100 | `online-a` | A | online | 64 | 34,816 | run s3-q8b-online-a1, submission s0038 |
| Qwen/Qwen3-8B | h100 | `offline-b` | B | offline | 8 | 2,048 | run s11-q8b-h100-b1, submission s0020 |
| Qwen/Qwen3-8B | h100 | `offline-a` | A | offline | 8 | 2,048 | run s11-q8b-h100-b1, submission s0016 |
| RecursiveSI/flint | b200 | `offline-a` (default) | A | offline | 8 | 2,048 | run s11-flint-b200-b1, submission s0026 |
| RecursiveSI/flint | b200 | `offline-b` | B | offline | 8 | 2,048 | run s11-flint-b200-b1, submission s0027 |
| Qwen/Qwen3.8-27B | b200 | `offline-a` (default) | A | offline | 8 | 2,048 | run s9-qwen38-27b-b200-f1, submission s0022 |
| Qwen/Qwen3.8-27B | b200 | `offline-b` | B | offline | 8 | 2,048 | run s11-q27-b200-b1, submission s0020 |
| CohereLabs/North-Mini-Code-1.0 | h100 | `offline-a` (default) | A | offline | 8 | 2,048 | run s4-north-h100-a1, submission s0022 |
| CohereLabs/North-Mini-Code-1.0 | h100 | `offline-b` | B | offline | 8 | 2,048 | run s4-north-h100-a1, submission s0021 |
| thinkingmachines/Inkling-2-Small | b200x4 | `offline-a` (default) | A | offline | 8 | 2,048 | run s7-inkling2s-b200x4-fb1, submission s0034 |
| thinkingmachines/Inkling-2-Small | b200x4 | `offline-b` | B | offline | 8 | 2,048 | run s7-inkling2s-b200x4-fb1, submission s0036 |
| thinkingmachines/Inkling-2-Small | b200x4 | `online-a` | A | online | 64 | 34,816 | run s8-inkling2s-b200x4-on1, submission s0043 |
| openai/gpt-oss-20b | h100 | `offline-a` (default) | A | offline | 8 | 2,048 | run s12-oss20-h100-a1, submission s0047 |
| openai/gpt-oss-20b | h100 | `offline-b` | B | offline | 8 | 2,048 | run s12-oss20-h100-a1, submission s0050 |
| Qwen/Qwen3-32B | b200 | `offline-a` (default) | A | offline | 8 | 2,048 | run s12-q32-b200-a1, submission s0033 |
| Qwen/Qwen3-32B | b200 | `offline-b` | B | offline | 8 | 2,048 | run s12-q32-b200-a1, submission s0036 |
| openai/gpt-oss-120b | b200 | `offline-a` (default) | A | offline | 8 | 2,048 | run s12-oss120-b200-a1, submission s0049 |
| openai/gpt-oss-120b | b200 | `offline-b` | B | offline | 8 | 2,048 | run s12-oss120-b200-a1, submission s0051 |
| thinkingmachines/Inkling-2-Mini | b200 | `offline-a` (default) | A | offline | 8 | 2,048 | run s17-mini-b200-ma, submission s0014 |
| thinkingmachines/Inkling-2-Mini | b200 | `offline-b` | B | offline | 8 | 2,048 | run s17-mini-b200-mb, submission s0020 |
| thinkingmachines/Inkling-2-Mini | b200 | `offline-c` | C | offline | 8 | 2,048 | run s18-mini-b200-c4, submission s0013 |

</details>

## Benchmarks

<p align="center"><img src="assets/speedup.png" width="820" alt="Speed of every system relative to SGLang on the same GPU, by model and batch size"></p>

Time per token over HTTP with a 64-token prompt and 1,024 greedy tokens, with one sequence and with eight. The figure
is relative to SGLang (vLLM for flint, which SGLang cannot load, and for North Mini Code); the table gives each model's
fastest general engine, and the factor is its time divided by ours.

| Model | GPU | Fastest general engine, ms | Track A, ms | Track A | Track B, ms | Track B |
|---|---|---|---|---|---|---|
| Qwen3-8B | H100 | SGLang 6.09 / 6.85 | 5.13 / 5.48 | **1.19×** / **1.25×** | 3.83 / 4.25 | **1.59×** / **1.61×** |
| North Mini Code | H100 | Cohere's own megakernel 3.62 / 7.07 | 2.54 / 6.90 | **1.43×** / 1.02× | 2.15 / 6.05 | **1.68×** / **1.17×** |
| gpt-oss-20b | H100 | vLLM 3.31 / 4.93 | 1.87 / 3.39 | **1.77×** / **1.45×** | 1.62 / 3.39 | **2.05×** / **1.46×** |
| flint | B200 | vLLM 1.99 / 3.79 | 1.39 / 3.35 | **1.43×** / **1.13×** | 1.36 / 3.35 | **1.47×** / **1.13×** |
| Qwen3.8-27B | B200 | SGLang 9.53 / 10.30 | 8.45 / 8.89 | **1.13×** / **1.16×** | 7.26 / 7.72 | **1.31×** / **1.33×** |
| Qwen3-32B | B200 | SGLang 11.43 / 11.68 | 10.11 / 10.43 | **1.13×** / **1.12×** | 8.99 / 9.44 | **1.27×** / **1.24×** |
| gpt-oss-120b | B200 | SGLang 2.22 / 3.33 | 1.78 / 3.07 | **1.25×** / 1.08× | 1.69 / 3.03 | **1.31×** / **1.10×** |
| Inkling-2-Small | 4 × B200 | SGLang 4.74 / 6.55 | 3.30 / 5.39 | **1.43×** / **1.22×** | 3.29 / 5.38 | **1.44×** / **1.22×** |
| Inkling-2-Mini | B200 | vLLM 3.71 / 5.09 | 2.74 / 5.08 | **1.36×** / 1.00× | 2.68 / 5.11 | **1.38×** / 1.00× |

How the comparison is made:

- **Same GPU, same job.** All systems of a row run on the same GPU in the same job, one after another, for three
  rounds; each round restarts every server.
- **Same interface and client.** Every system is behind an OpenAI-compatible streaming endpoint and timed by one client
  ([`eval/client.py`](eval/client.py)) that records the arrival of each token.
- **Same work.** Prompts are sent as token ids, every request generates exactly 1,024 tokens, and time per token is taken
  over the window in which all sequences decode.
- **Released baselines.** vLLM and SGLang are installed from their releases and run with their recommended flags, or a
  faster setting where we found one. For North Mini Code the reference is the vendor's own hand-written megakernel.
  Inkling-2-Mini is not in a release of either yet: vLLM is its model pull request (vllm-project/vllm#69028) built
  from source, SGLang the image of its pull request (sgl-project/sglang#51926), both with the model's recipe flags.
  Both quantize the expert inputs to 4 or 8 bits, as the checkpoint's quantization config asks; our engines and the
  reference do not, so the general engines compute a slightly different function.

**Track C, exact speculative decoding** (Inkling-2-Mini on one B200, in the same job as its row above). Time per token
is counted in tokens received, since a speculative server sends several tokens per chunk. The comparison is with the
general engines' own speculative decoding on the checkpoint's draft head: vLLM with DSpark and 7 draft tokens (the
model's recipe) and SGLang with DSPARK.

| Model | GPU | Fastest general engine with speculative decoding, ms | Track C, ms | Track C |
|---|---|---|---|---|
| Inkling-2-Mini | B200 | vLLM + DSpark 1.55 / 2.71 | 1.25 / 5.08 | **1.24×** / 0.53× |

The track-C engine drafts inside the track-A megakernel and only for a single sequence; with 2 to 8 it decodes one
token per pass, as fast as track A and slower than the general engines' speculative decoding (2.19-2.71 ms for vLLM
with DSpark at 2 to 8 sequences). On natural text (prose, code and word problems) with one sequence it takes 0.80 ms
per token, and vLLM with DSpark 0.87 ms. The general engines' speculative output is not lossless: with greedy
decoding, vLLM's text with speculation equals its own text without it in 12 of 243 streams, SGLang's in 6 of 243. The
track-C engine's tokens equal its own one-token-per-step tokens in every test (the evaluator's sequences and natural
text, 1 and 8 sequences, staggered requests).

**Serving a production request trace** (300-second replay of the
[Mooncake tool-and-agent trace](https://github.com/kvcache-ai/Mooncake/tree/main/FAST25-release/traces), all systems over HTTP on
the same hardware; a request is within the service levels when its first token arrives within 5 s and its tokens are on
average at most 0.1 s apart):

| Model, GPU | Rate | Within service levels | Longest stall |
|---|---|---|---|
| Inkling-2-Small, 4 × B200 | 1–4 req/s | **100%** vs 83–85% (SGLang) | 0.08–0.09 s vs 2.4–2.6 s |
| Inkling-2-Small, 4 × B200 | 8 req/s | **99.2%** vs 81.7% (SGLang) | 0.15 s vs 4.4 s |
| Qwen3-8B, 1 × H100 | 1–2 req/s | **95–97%** vs 68–75% (SGLang, vLLM) | 0.09–0.11 s vs 0.5–6.9 s |
| Qwen3-8B, 1 × H100 | 3 req/s | **90–93%** vs 59–68% (SGLang, vLLM) | 0.09 s vs 0.6–7.3 s |

<p align="center"><img src="assets/serving-inkling.png" width="820" alt="Inkling-2-Small on four B200 under a production request trace"></p>

The serving engines have a slower 99th-percentile first token and, on Inkling-2-Small, a slower median time
between tokens. Every measurement, including batch sizes from 1 to 64, long generations, long prompts, natural-text
prompts and sampling, is in the [benchmark data tables](https://dangxingyu.github.io/megakernel/full.html); the write-up discusses the limits.

To reproduce a comparison on your own GPU:

```bash
# serves each system in turn on this GPU and times it with one client
MK_MODEL=Qwen/Qwen3-8B COMPARE_SYSTEMS="mkserve:offline-a mkserve:offline-b sglang vllm" bash scripts/compare.sh
```

## Evaluation suite

```bash
bash scripts/eval_selftest.sh Qwen/Qwen3-8B      # once per model: weights, an FP64 reference on this GPU, the evaluator on the starter
MK_MODEL=Qwen/Qwen3-8B bash scripts/eval_setup.sh
python eval/kernel_eval.py --workspace engines/qwen3-8b_h100/offline-a --out result.json
```

[`eval/kernel_eval.py`](eval/kernel_eval.py) builds an engine and reports a time only if it is correct:

| Gate | What is checked |
|---|---|
| `numeric`, `numeric_long` | logits against an FP64 run of the reference model at every position to 128 and at every 8th position to 1,152, alone and in a batch of 8; relative error within 2× that of the Hugging Face BF16 implementation |
| `tokens` | top-1 agreement with FP64 within one point of the BF16 implementation's |
| `batch` | a sequence alone and inside a batch give the same logits |
| `generate`, `http_tokens` | the engine's own decode loop and its HTTP path reproduce its step-by-step greedy tokens (track C: every sequence exactly) |
| `timed_steps` | the steps that were timed are checked against the reference afterwards |

The reference is computed on your GPU for the token sequences in [`eval/refs/`](eval/refs) (the ones our runs were
scored on), so results are comparable with ours. [`eval/release_check.py`](eval/release_check.py) adds every batch size
from 1 to 8, slot permutation, neighbor independence, repetition, state after a full context, and a process restart;
[`eval/spec_check.py`](eval/spec_check.py) checks a track-C engine's tokens on natural text, at batch 1 and 8 and
with staggered requests;
[`scripts/mkserve_check.py`](scripts/mkserve_check.py) tests a served engine through the API.

## Build your own engine

The engines were produced by an agent that edits one engine directory, measures on the GPU, and submits to the evaluator
above. The same loop runs on a single machine:

```bash
bash scripts/eval_selftest.sh Qwen/Qwen3-8B
python autoresearch/start.py my-run --model Qwen/Qwen3-8B --card h100 --hours 12
cd my-run/workspace && claude -p "$(cat ../PROMPT.md)" --dangerously-skip-permissions
```

`start.py` creates a workspace with a starting engine (the Hugging Face model behind the engine contract, or any engine
of this repository with `--engine`), installs the skill, writes the prompt, and gives the agent one tool: `mk submit`
evaluates the engine and records the result, `mk board` shows every submission and the time left. Any coding agent with
a shell can drive it. The prompts state the goal, the rules and the two tracks; they name no optimization technique.

- [`autoresearch/skills/megakernel`](autoresearch/skills/megakernel): the skill every run starts from (the engine
  contract, how the evaluator scores, how to log).
- [`autoresearch/skills_by_model`](autoresearch/skills_by_model): the skills of our runs, with the facts of each model
  and GPU.
- [`autoresearch/skills/megakernel/playbook.md`](autoresearch/skills/megakernel/playbook.md): what the earlier runs measured:
  where each engine's time went, which changes paid and by how much, track-B formats, dead ends, correctness traps.
- [`autoresearch/tools`](autoresearch/tools): `mkprof` (phase timings inside a persistent kernel, which a profiler sees
  as one kernel), `bitcheck.py` (are two builds the same function, bit for bit?) and `weights_census.py` (exact
  statistics of a checkpoint's weights).
- [`runs/`](runs): every submission of our 29 runs (source, hypothesis, score) and the agents' notes, as worked examples.

For a model that is not in Hugging Face `transformers`, a reference implementation has to be written first;
[`eval/inkling2_ref.py`](eval/inkling2_ref.py) is the one for Inkling-2-Small and Inkling-2-Mini. To add an engine to
this repository, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Repository layout

```
engines/        one directory per engine: CUDA source, build script, Python binding (engine/api.py)   engines/README.md
mkserve/        OpenAI-compatible server and the engine registry (registry.json)
eval/           evaluator, reference builder, benchmark client, extended checks                     eval/README.md
scripts/        environment setup, same-GPU comparison, server tests, check_engine.py
baselines/      how the general engines were installed and launched
autoresearch/   the local optimization loop: tools, skills, prompts
starter/        the reference model behind the engine contract (where a run starts)
runs/           the record of every agent run                                                       runs/README.md
```

To contribute an engine, a model or a fix, see [CONTRIBUTING.md](CONTRIBUTING.md); `python scripts/check_engine.py --all`
runs the static checks every engine in `engines/` passes.

## Limitations

- An engine is specific to one checkpoint and one GPU type, and is compiled on the machine that serves it.
- Steady-decode engines hold 8 sequences and a 2,048-token context and read the prompt one token per pass.
- Decoding inside the kernel is greedy; sampling runs in `mkserve` and costs 1 to 11%.
- The track-C engine (Inkling-2-Mini) speculates only with one sequence; with 2 to 8 it decodes one token per pass,
  like its track-A engine, and is slower than the general engines' speculative decoding there. A request that arrives
  while others decode waits for them.
- Use the engines through `mkserve`: called directly, most of them do not validate requests. The serving engines for
  Qwen3-8B match shared prompt prefixes by a 64-bit hash without comparing tokens.
- Benchmark numbers are from single nodes and two to three rounds.

The findings of the independent audit of every engine are summarized in the [write-up](https://dangxingyu.github.io/megakernel/#limits).

## Citation

```bibtex
@misc{dang2026megakernel,
  title        = {A Megakernel per Model},
  author       = {Dang, Xingyu},
  year         = {2026},
  howpublished = {\url{https://dangxingyu.github.io/megakernel/}},
  note         = {Code: \url{https://github.com/dangxingyu/megakernel-zoo}}
}
```

## License and acknowledgements

Apache-2.0. `eval/inkling2_ref.py` began as a transcription of model code from NovaSky-AI/SkyRL (Apache-2.0), as noted in
the file. The baselines are [vLLM](https://github.com/vllm-project/vllm), [SGLang](https://github.com/sgl-project/sglang)
and Cohere's megakernel for North Mini Code; the request trace is the tool-and-agent trace released with
[Mooncake](https://github.com/kvcache-ai/Mooncake) ([FAST '25](https://www.usenix.org/conference/fast25/presentation/qin)).
