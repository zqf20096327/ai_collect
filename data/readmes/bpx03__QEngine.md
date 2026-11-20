# QEngine

![QEngine: fast local AI on RTX 3000, 4000 and 5000 series cards](docs/img/qengine.jpg)

<p align="center">
  <a href="https://buymeacoffee.com/bpx03"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy me a coffee" height="60"></a>
  <br>
  <sub>Built and tested on one home machine. If QEngine helps you, a coffee keeps it going.</sub>
</p>

QEngine is an open-source (MIT) inference engine for five models on NVIDIA RTX 3000, 4000 and 5000 series cards, with
nothing extra to install or set for any of them (tuned on the RTX 3090):

- **Qwen3.8-Flash-Next**, run from my checkpoint [bpx03/Qwen3.8-Flash-Next-QEngine](https://huggingface.co/bpx03/Qwen3.8-Flash-Next-QEngine)
  (routed experts INT4 from Intel's AutoRound quantization, repacked bit-exact; the parts every token passes through in
  INT8 or calibrated INT4): a sparse mixture-of-experts model with 512 routed experts, 262K
  context (up to 1M opt-in) and image input. Runs on 2 or more cards (tuned for 3 and 2).
- **Qwen3.8-27B** (INT4, the RedHatAI W4A16 checkpoint [RedHatAI/Qwen3.8-27B-INT4](https://huggingface.co/RedHatAI/Qwen3.8-27B-INT4)
  plus its MTP head; INT8 opt-in: [bpx03/Qwen3.8-27B-INT8-QEngine](https://huggingface.co/bpx03/Qwen3.8-27B-INT8-QEngine)): a dense model with 262K context (up to 1M
  opt-in, with optional sparse attention for long prompts) and image input. Tuned for 3 cards, also runs on 2, and on 1 as an experiment.
- **DeepSeek-V4.1-Flash** (preview), run from the third-party Maya-S GGUF files as they are
  ([peasantsmith/DeepSeek-V4.1-Flash-1017-Maya-GGUF](https://huggingface.co/peasantsmith/DeepSeek-V4.1-Flash-1017-Maya-GGUF)): a large sparse
  mixture-of-experts model (384 routed experts per layer, Engram n-gram memory, compressed sparse attention) on three
  24 GB cards plus about 170 GB of host RAM, with a DSpark draft model, 262K context. RTX 3000 / 4000 series only.
- **GLM-5.3-Flash** (preview), run from my INT4 quant [bpx03/GLM-5.3-Flash-INT4-QEngine](https://huggingface.co/bpx03/GLM-5.3-Flash-INT4-QEngine)
  (routed experts and KDA layers): a sparse mixture-of-experts
  model (288 routed experts per layer, 8 active) on three 24 GB cards plus about 192 GB of host RAM, with the experts in
  host RAM and a CPU expert lane next to the cards, MTP drafts, 262K context.
- **gpt-oss-120B** (preview), run from OpenAI's official checkpoint as it is,
  [openai/gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b) (MXFP4 experts): a sparse
  mixture-of-experts model (128 experts per layer, 4 active) on three 24 GB cards, all in VRAM, 128K context, up to 8
  conversations decoded together. RTX 3090-class cards (compute capability 8.6) only.

One server serves any of them through an **OpenAI-compatible** and an **Anthropic-compatible** API (it works with
agent clients such as Claude Code). The C++/CUDA engines are built as shared libraries; the Python server loads them
and handles the API, tool calls, structured output, scheduling and caching.

**Measured on my machine** (3× RTX 3090, 24 GB, PCIe 4.0 x16, GPU P2P on), QEngine 1.5.0 with its default settings
and the club-3090 benchmark tools (November 19, 2026):

| output tok/s unless noted | Qwen3.8-27B | Qwen3.8-Flash-Next | DeepSeek-V4.1-Flash | GLM-5.3-Flash | gpt-oss-120B |
|---|---:|---:|---:|---:|---:|
| single-stream decode, narrative / code | 275 / 524 | 310 / 452 | 88 / 120 | 110 / 92 | 301 / 301 |
| prefill, 10K-token prompt: tok/s, time to first token | 6,188, 1.60 s | 8,254, 1.23 s | 4,217, 2.35 s | 2,920, 3.42 s | 13,280, 0.74 s |
| prefill, 90K-token prompt: tok/s, time to first token | 4,994, 18.0 s | 8,390, 10.5 s | 4,895, 17.8 s | 3,572, 25.4 s | 5,055, 17.6 s |
| total output, 1 / 4 / 8 / 16 streams at once | 312 / 575 / 848 / 999 | 300 / 642 / 880 / 1,061 | 70 / 73 / 78 / 78 | 72 / 55 / 50 / 44 | 306 / 594 / 731 / 835 |

| model | weights | quality against a reference |
|---|---|---|
| Qwen3.8-27B | INT4 W4A16, group 128 (RedHatAI) plus its MTP head | next-token KL 0.0154 against BF16, top-1 agreement 95.3 % |
| Qwen3.8-Flash-Next | routed experts INT4 (Intel's AutoRound, repacked bit-exact); shared expert and dense parts INT8 or calibrated INT4; DeltaNet projections INT8 | next-token KL 0.114 against BF16, top-1 agreement 89.6 % |
| DeepSeek-V4.1-Flash | the Maya-S GGUF files as they are: experts IQ2_XXS / IQ2_S / IQ3_XXS / IQ3_S, dense Q8_0, Engram Q6_K | negative log-likelihood 1.635 on my test texts (no full-precision reference fits on this machine) |
| GLM-5.3-Flash | my INT4 quant: routed experts and KDA layers INT4 ([details](#glm-53-flash-preview)) | next-token KL 0.59 against the official FP8 model (three prompts: 0.45-0.77) |
| gpt-oss-120B | OpenAI's checkpoint as it is: MXFP4 experts, bf16 dense weights | next-token KL 0.118 against an fp32 reference of the model, top-1 agreement 86.9 % |

(Single-stream decode: club-3090 `bench.sh` with each model's own sampling; streams: its `concurrency-probe.sh`,
greedy, 256-token prompts and replies, total output of all streams; each number is the mean of 2 to 6 runs. The two
Qwen servers ran with thinking on at effort low and vision on. For 16 streams the servers that hold 8 conversations
by default were started with 16: `GLM_CONVS=16`, DeepSeek-V4.1-Flash `--max-active 16`, `GPTOSS_SLOTS=16`.
DeepSeek-V4.1-Flash and GLM-5.3-Flash decode one conversation at a time and give the streams turns, so their total
output stays at about one stream's. gpt-oss-120B at 90K: prompts of 86,786 and 89,998 tokens. Quality: the same
builds; the [8-pack](#quality) results are below.)

**Flash-Next quality**, in more detail: next-token KL divergence against the official BF16 model on the public set
[jyohukuchan/qwen38-flash-next-bf16-logits](https://huggingface.co/datasets/jyohukuchan/qwen38-flash-next-bf16-logits),
scored with its own `compare.py`: mean KL **0.114**, top-1 agreement **89.6 %**, WikiText-2 KL **0.125** (0.126 when
the context went through batched prefill). 1.5.0 build, November 19, 2026, the same as 1.3.6 to every digit; details
and the command under [Quality](#quality).

**What is new in 1.5.0**:

- **Three new models, as previews**, in the same server, API and Docker image as the two Qwen models (what each one
  supports: [Feature matrix](#feature-matrix)):
  - [DeepSeek-V4.1-Flash](#deepseek-v41-flash-preview), run from the Maya-S GGUF files as they are, on three 24 GB
    cards plus about 170 GB of host RAM: 262K context, DSpark drafts, thinking, tool calls and structured output, a
    host-RAM archive and shared system prompts for agent teams. 88 / 120 tok/s single-stream (narrative / code), a
    90K-token prompt in 17.8 s, 8-pack 122 / 133 of 150 (thinking off / on).
  - [GLM-5.3-Flash](#glm-53-flash-preview), run from my INT4 quant, on three 24 GB cards plus about 192 GB of host
    RAM, with the experts in host RAM and a CPU expert lane next to the cards: 262K context, MTP drafts, logprobs, up
    to 8 conversations at once by exact time slicing. 110 / 92 tok/s single-stream, a 90K-token prompt in 25.4 s,
    8-pack 121 / 133 of 150.
  - [gpt-oss-120B](#gpt-oss-120b-preview), run from OpenAI's checkpoint as it is, all in VRAM on three 24 GB cards,
    with or without GPU P2P: 128K context, up to 8 conversations decoded together, lookup drafts, presence /
    frequency penalties. 301 tok/s single-stream, 835 tok/s total with 16 streams, a 10K-token prompt in 0.74 s and a
    90K-token prompt in 17.6 s, 8-pack 110 / 116 of 150 (reasoning effort low / medium).

- **27B: the first token comes much sooner with many agents at once.** The 27B used to keep half of the GPU time for
  running replies however many requests waited for their prompt. Now the time split follows the queue: short prompts
  are prefilled back to back with one decode step between passes, long ones share the time by head count, and running
  replies keep at least 10 % of it (`--prefill-share-min`, `--prefill-short`; `--prefill-share-min 0.5` gives the old
  split). It counts a running reply at admission by its `max_tokens`, and no longer copies a whole conversation to the
  host archive when the next turn only replaces the last reply. On my 2 cards, in an agent replay with short tool
  results, the median time to the first token at 16 agents in flight went from 4.5 s to 0.86 s, with 7 % more total
  output; single-stream speed is unchanged ([numbers](#qwen38-27b-2)). Beyond its 16 decode seats a request is
  prefilled on one of two seats kept for prompts, gets its first token, and its reply waits parked in host memory (KV
  and state, resumed exactly where it stopped) until a decode seat frees (`--park`, `--park-reserve`; `--park 0`
  waits for a seat first, as before). Archived conversations keep two recurrent-state checkpoints instead of four
  (`QE_ARCH_SUBS`), so the host archive holds about 1.5 times as many agents. At 32 and 64 agents in flight with the
  defaults on 2 cards (release build): median first token 1.0 / 0.48 / 1.0 s at 16 / 32 / 64 agents in flight, with
  243 / 359 / 285 tok/s total output and no agent's prompt computed again. `QE_MAX_SEQS=32` (opt-in) seats 32 conversations on 2 and 3 cards: at 32 agents in flight
  on 2 cards the median first token went from 25 s to 0.48 s with 106 % more total output, at the cost of a smaller
  KV pool (2 cards: 417,792 tokens instead of 623,616, so two very long conversations no longer fit at once).

- **Flash-Next: the first token comes much sooner with several agents at once.** Every prompt now keeps the state at
  its own end, so an agent's next turn resumes there even when the client sends back another text for the reply or
  drops its reasoning; before, a turn shorter than 4,096 tokens was recomputed on the next turn (about a third of
  all prefill work in an agent replay). A conversation keeps three recurrent states instead of six (its system end,
  its latest prompt end and the newest other one; `FLASH_CKPT_KEEP=6` as before), so the host archive holds 64
  agents. On 3 cards the time split follows the queue as on the 27B: while short prompts are next, running replies
  get 10 % of the time after every prefill pass instead of half (`--prefill-share-min`; 2 cards and mode B keep the
  fixed split). In an agent replay with short tool results the median time to the first token went from 0.16 / 0.44
  / 1.91 / 3.93 s to 0.13 / 0.25 / 0.37 / 2.83 s at 1 / 4 / 16 / 32 agents in flight, with 15 / 14 / 16 / 10 % more
  total output ([numbers](#qwen38-flash-next-2)). Beyond the 16 decode seats Flash-Next now parks as the 27B does
  (`--park`, on 3 cards in `tp` mode): a reply gets its first token from one of 4 seats kept for prompts, waits in
  host memory and resumes exactly where it stopped when a seat frees. At 32 / 64 agents the median time to the
  first token went from 2.83 / 8.0 s to 0.26 / 0.75 s, with 5 / 9 % more total output.

- **Flash-Next: no more stops at a slot hand-off when the host is short of memory**
  ([#32](https://github.com/bpx03/QEngine/issues/32), [#25](https://github.com/bpx03/QEngine/issues/25)). The
  engine's log lines go through a writer thread, so a slow log reader can no longer hold up a GPU step
  (`QE_LOG_ASYNC`); the archive's memory is pinned in the background only while the engine is idle, 1 GB at a time,
  and pinning pauses (and backs off) when a registration is slow, which is a sign of host memory pressure. Thanks to
  cristianflorett, dgaglioni and gbinka for the reports and measurements behind the Flash-Next hand-off fix (#32, #25).

- **Both Qwen models give memory back when other programs squeeze the host while they serve.** A background thread
  watches the kernel's memory-pressure and swap-in counters next to `MemAvailable`; under pressure the engine stops
  growing, frees archive memory, shrinks the archive, drops pinned prompts and, last (Flash-Next), moves the n-gram
  table to the page cache, one logged stage at a time, and it returns slowly once the host stays calm (`QE_MEMP=0`
  turns it off; [details](docs/advanced.md#host-ram-safety)). With 179 GB taken by another program on my machine,
  Flash-Next went down to the last stage and served every request, with the same greedy text.

- **For every model:** streamed replies send a keep-alive after 10 s without an event (an OpenAI `: keep-alive`
  comment, an Anthropic `ping` event; `QE_SSE_KEEPALIVE`), so proxies and clients with a read timeout keep a stream
  whose request waits for its turn. At start the server logs one `[settings]` line for every flag or environment
  variable that is set but does nothing for the loaded model. A top-level `enable_thinking` in a request is read too
  ([#31](https://github.com/bpx03/QEngine/issues/31)).

- 27B and Flash-Next single-stream decode and prefill speed and their quality are the same as in 1.3.6 within the
  run-to-run spread (same benchmark, 1.3.6: 27B 281 / 507 tok/s, prefill 6,133 / 4,997 tok/s; Flash-Next 306 / 449
  tok/s, prefill 8,207 / 8,394 tok/s).

1.5.0 went through the release checks on my machine and passed all of them (the 262K-token stress runs with images
on 3 and on 2 cards, VRAM and host-RAM hogs taken mid-run, soaks, Docker smoke, per model). The 8-pack quality suite ran once per
model ([Quality](#quality)), next to the KL / NLL measurement and the speed runs of all five models.

Older releases and what changed in each: [releases page](https://github.com/bpx03/QEngine/releases).

## Contents

- [Quick start](#quick-start)
- [Hardware and interconnect](#hardware-and-interconnect)
- [Models](#models)
- [Feature matrix](#feature-matrix)
- [API](#api)
- [Serving behaviour](#serving-behaviour)
- [Settings](#settings)
- [Benchmarks](#benchmarks)
- [Troubleshooting and FAQ](#troubleshooting-and-faq)
- [Repository layout and tests](#repository-layout-and-tests)
- [Changelog](#changelog)
- [Support](#support)
- [License](#license), [Disclaimer](#disclaimer)

More settings, measurements and the troubleshooting table: [docs/advanced.md](docs/advanced.md).

## Quick start

You need Linux, two or three RTX 3000, 4000 or 5000 series cards (see [Hardware](#hardware-and-interconnect)), an
NVIDIA driver with CUDA 13.1
support, and enough host RAM (Flash-Next: about 140 GB for the full defaults; with less, the start-up sizes its host
memory to the machine, from 64 GB up; see [Host memory](#host-memory-flash-next)).

### 1. Get a model

The `hf` command comes with the Hugging Face hub client: `pip install -U "huggingface_hub[cli]"`.

```bash
# Qwen3.8-Flash-Next: my checkpoint is the supported way to run it (~129 GB, ready to run: converted weights,
# INT8 n-gram table and three small files)
hf download bpx03/Qwen3.8-Flash-Next-QEngine --local-dir models/Qwen3.8-Flash-Next-QE-INT4
# (the previous, 1.3.4 weights: add --revision v1.3.4; see "Model files" under Models)

# Qwen3.8-27B (incl. its MTP head); two small tuned files are fetched automatically at the first start
hf download RedHatAI/Qwen3.8-27B-INT4 --local-dir models/Qwen3.8-27B-INT4
```

### 2a. Run with Docker

Requirements on the host: the NVIDIA driver and the
[NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/). One image serves all
models; it picks the engine from the model's `config.json` (DeepSeek-V4.1-Flash: from the GGUF files).

```bash
docker run -d --name qengine --restart unless-stopped --gpus all --ipc=host --ulimit memlock=-1 \
  -p 127.0.0.1:8080:8080 -p 127.0.0.1:9393:9393 \
  -v /path/to/models:/app/models:ro -v qengine-cache:/root/.cache/qengine \
  -e QE_MODEL=/app/models/Qwen3.8-Flash-Next-QE-INT4 \
  ghcr.io/bpx03/qengine:latest
```

- Without `QE_MODEL` the container serves `/app/models/Qwen3.8-27B-INT4`.
- The API listens on 127.0.0.1 only, as the source start does. To reach it from other machines, publish it as
  `-p 8080:8080` (all interfaces) and put a firewall or an authenticating proxy in front: the server has no API keys.
- `--restart unless-stopped` matters: after a stalled GPU the server exits with code 75 and relies on a restart (see
  [Failure handling](#serving-behaviour)).
- Images: `latest` / `1.5.0` (text only) and `vision` / `1.5.0-vision` (with the image encoder). Earlier: `1.3.6`, `1.3.6-vision`, `1.3.5.9`, `1.3.5.9-vision`, `1.3.5.8`, `1.3.5.8-vision`, `1.3.5.7`, `1.3.5.7-vision`, `1.3.5.6`, `1.3.5.6-vision`, `1.3.5` and `1.3.5-vision`; experimental `1.3.5.5`, `1.3.5.5-vision`, `1.3.5.4`, `1.3.5.4-vision`, `1.3.5.3`, `1.3.5.3-vision`, `1.3.5.2`, `1.3.5.2-vision`, `1.3.5.1`, `1.3.5.1-vision`.
  Earlier releases stay available under their version tags.
- `QE_GPUS=0,2` picks the GPUs (host ids with `--gpus all`; default `0,1,2`; `QE_DEVICES`, if set, wins over `QE_GPUS`). Settings are environment variables
  (`-e FLASH_PAR=pp`); anything after the image name, or `QE_EXTRA_ARGS`, goes to the server (`--think 0`,
  `--vision 1`).
- Keep the `qengine-cache` volume: it holds the GEMM tuning table, the downloaded 27B files and the stats.
- `--ipc=host` and `--ulimit memlock=-1` are needed for the pinned host memory. On SELinux hosts (Fedora, RHEL) add
  `--security-opt label=disable`.
- Port 8080: the API. Port 9393: monitoring dashboard, `/api/stats`, Prometheus `/metrics`.
- Compose: `QE_MODELS_DIR=/path/to/models docker compose up -d` (see `docker-compose.yml`). It builds the image
  from this checkout (it does not pull `ghcr.io/bpx03/qengine`) and serves the 27B; for Flash-Next add
  `QE_MODEL: /app/models/Qwen3.8-Flash-Next-QE-INT4` under `environment:`. Unlike the `docker run` line above, it
  publishes the API on **all interfaces** (`QE_HOST_PORT`, default 8080) and the monitoring on 127.0.0.1
  (`QE_METRICS_HOST_PORT`, 9393). The server has no API keys, so anyone who can reach that port can use it: set
  `QE_HOST_PORT=127.0.0.1:8080` to keep it on this machine, or put it behind a firewall or an authenticating proxy.
  `QE_VISION_BUILD=0` builds the text-only image, `QE_REVISION` sets the build hash.
- DeepSeek-V4.1-Flash (preview): mount the folder that holds both `Maya-S/` and `dspark/` and point `QE_MODEL` at
  `Maya-S`, e.g. `-v /path/to/DeepSeek-V4.1-Flash-1017-GGUF:/app/models/dsv4:ro -e QE_MODEL=/app/models/dsv4/Maya-S`.
  Symbolic links inside the mount must resolve inside the container (mount their targets at the same paths). The
  image carries the DSV4 engine for sm_86 / sm_89 only. Engine settings go in with `-e`
  (`-e DSV4_EGMIRROR=...`), server flags in `QE_EXTRA_ARGS` (`--route-margin 0.05`).
  One image serves all models; the DSV4, GLM and gpt-oss engines add cuBLAS to it.
- GLM-5.3-Flash (preview): mount the `bpx03/GLM-5.3-Flash-INT4-QEngine` directory, e.g.
  `-v /path/to/GLM-5.3-Flash-INT4-QEngine:/app/models/glm:ro -e QE_MODEL=/app/models/glm`. The experts are pinned in
  host RAM (about 157 GB), so `--ipc=host --ulimit memlock=-1` matter here. Engine settings go in with `-e`
  (`-e GLM_CPU_ISA=avx2`), server flags in `QE_EXTRA_ARGS` (`--split 704,704,640`).
- gpt-oss-120B (preview): mount the `openai/gpt-oss-120b` directory, e.g.
  `-v /path/to/gpt-oss-120b:/app/models/gpt-oss-120b:ro -e QE_MODEL=/app/models/gpt-oss-120b`. Engine settings go in
  with `-e` (`-e GPTOSS_SLOTS=4`). The image carries the gpt-oss engine for sm_86 only.
- Build it yourself: `docker build -t qengine .` (with vision), `--build-arg VISION=0` (text only),
  `--build-arg CUDA_ARCHS=86` (RTX 3090 code only, faster build), `--build-arg REVISION=$(git rev-parse HEAD)` (the
  build hash the monitoring headers show; without it they say `build unknown`).

### 2b. Or build from source

Requirements: CUDA Toolkit **13.1**, CMake ≥ 3.24 and Ninja (or Make), a host compiler nvcc 13.1 accepts (it
rejects GCC 16; `CMakeLists.txt` uses `/usr/bin/g++-15` when present, otherwise pass e.g.
`-DCMAKE_CXX_COMPILER=g++-14 -DCMAKE_CUDA_HOST_COMPILER=g++-14`), Python 3.12.

```bash
cmake -B build -G Ninja
cmake --build build                          # -> build/libqengine.so (27B), build/libqflash.so + build/flash_run (Flash-Next)
python3 -m pip install -r requirements.txt   # torch: install the CUDA build matching your driver (see the file)
```

A source build contains code for the GPUs of the machine it is configured on (their compute capabilities from
`nvidia-smi`; the cmake output names them), always plus RTX 3090 code (sm_86). To build for other cards, name
them: `cmake -B build -G Ninja -DCMAKE_CUDA_ARCHITECTURES="86;120"` (or `"86;89;120"`, or just `120`).

```bash
server/run.sh 8080 --model models/Qwen3.8-Flash-Next-QE-INT4   # Flash-Next on GPUs 0,1,2, API on 127.0.0.1:8080
server/run.sh 8080                                             # Qwen3.8-27B (the default model directory)
python3 server/app.py --help                                   # all command-line options
```

### 3. Recipes by card count

| setup | command (source; Docker: the same variables with `-e`, GPUs with `QE_GPUS`) | notes |
|---|---|---|
| 3 cards (tuned) | `server/run.sh 8080 --model <dir>` | the default: GPUs 0,1,2 |
| 2 cards | `QE_DEVICES=0,2 server/run.sh 8080 --model <dir>` | Flash-Next keeps about half of its experts in host RAM; the 27B serves 16 slots, as on 3 cards (`QE_MAX_SEQS=32` for 32) |
| 1 card (27B only, experimental) | `QE_DEVICES=0 QE_MAX_SEQS=1 server/run.sh 8080` | one conversation, 206,848 tokens of context; `QE_MAX_SEQS` up to 4; MTP drafts unless you lower `--max-ctx` to what the start-up line says (`--max-ctx 165K` on my 24 GB card) or set `QE_DRAFTER=dflash2` ([DFlash2](#dflash2-block-drafter-27b-on-when-it-fits)) |
| a card also drives a desktop | Flash-Next `FLASH_EC_MARGIN_MB=256,2048,256`; 27B `QE_RESERVE_GB=1.5,3,1.5` | more free VRAM on that card (values in GPU order) |
| 4 or more cards (Flash-Next) | `QE_DEVICES=0,1,2,3 server/run.sh 8080 --model <dir>` | exactly 4 equal cards with verified P2P: `tp`, otherwise a pipeline (`pp`); see [4 or more cards](#4-or-more-cards) |
| long documents, short answers (Flash-Next) | `FLASH_PAR=pp` | pipeline mode: faster long prompts, slower single-stream decode |
| many long conversations (Flash-Next) | `FLASH_KV=ram FLASH_KV_RAM_TOKENS=4M` | KV cache in host RAM, ~74K tokens per GB |
| more KV per GB (Flash-Next) | `FLASH_KV_BITS=4` | 4-bit KV cache: 7,488 instead of 13,520 bytes per token (~134K tokens per GB with `FLASH_KV=ram`); see [Host memory](#host-memory-flash-next) |
| small cards, more context (27B) | `QE_KV_BITS=4` | 4-bit KV cache: about 1.5x the context on 8-12 GB cards; see [Smaller cards](#gpus) |

The first start on a new card count tunes the GEMMs and caches the table in `~/.cache/qengine`.

### 4. First request

```bash
curl -s http://127.0.0.1:8080/v1/chat/completions -H 'Content-Type: application/json' -d '{
  "model": "qwen3.8-flash-next-qengine",
  "messages": [{"role": "user", "content": "Write a haiku about PCIe."}],
  "max_tokens": 1024
}'
```

The served names are `qwen3.8-flash-next-qengine` and `qwen3.8-27b-qengine` (`--served-name` changes it).
For **Claude Code**, set `ANTHROPIC_BASE_URL=http://127.0.0.1:8080` and `CLAUDE_CODE_ATTRIBUTION_HEADER=0`.

### 5. Behind llama-swap (or another model switcher)

I run QEngine behind [llama-swap](https://github.com/mostlygeek/llama-swap) myself. A source build:

```yaml
healthCheckTimeout: 900          # the first start of a model takes longer (see below)
models:
  qwen3.8-flash-next-qengine:
    cmd: bash -c 'cd /path/to/QEngine && exec server/run.sh ${PORT} --model /path/to/models/Qwen3.8-Flash-Next-QE-INT4'
    checkEndpoint: /health
  qwen3.8-27b-qengine:
    cmd: bash -c 'cd /path/to/QEngine && exec server/run.sh ${PORT} --model /path/to/models/Qwen3.8-27B-INT4'
    checkEndpoint: /health
```

The Docker form (the switcher stops the container by name):

```yaml
  qwen3.8-flash-next-qengine:
    cmd: >
      docker run --rm --name qengine-fn --gpus all --ipc=host --ulimit memlock=-1
      -p 127.0.0.1:${PORT}:8080 -v /path/to/models:/app/models:ro -v qengine-cache:/root/.cache/qengine
      -e QE_MODEL=/app/models/Qwen3.8-Flash-Next-QE-INT4 ghcr.io/bpx03/qengine:latest
    cmdStop: docker stop -t 60 qengine-fn
    checkEndpoint: /health
```

- `exec` matters: it makes the server the process the switcher stops, so a stop ends the engine and frees the cards.
- `GET /health` answers only once the model is loaded and the API is up, so it is the readiness check.
- A start takes longer the first time on a machine: the GEMMs are tuned for the card count, the 27B downloads its
  tuned MTP head and draft ranking and the DFlash2 drafter (about 1.28 GB), and with `--lsa` the index map. All of it
  is cached in `~/.cache/qengine` (Docker: keep the `qengine-cache` volume), so later starts skip it.
- Only one engine can hold a card. A second one that starts while the first is still exiting waits up to
  `QE_GPU_LOCK_WAIT_S` (60 s) and then stops with the first one's pid and command line. So the switcher must stop one
  QEngine model before it starts another on the same GPUs (llama-swap does that by default: one model at a time).
  Two models side by side need separate cards (`QE_DEVICES`, Docker `QE_GPUS`).

## Hardware and interconnect

QEngine is tuned on 3× RTX 3090 with GPU P2P and plenty of host RAM, but it adapts by itself to machines that differ
from that:

- **no P2P** (stock driver, x4 / x8 slots, dual-socket or NUMA): both engines exchange through pinned host memory by
  DMA, close to the P2P speed ([details](#with-and-without-gpu-p2p));
- **long prompts on slow links**: `FLASH_PAR=pp`, a layer pipeline, picked automatically where it wins
  ([Parallel mode](#parallel-mode-flash-next-flash_par));
- **small host RAM** (e.g. 64-96 GB): the host-memory plan adapts, with no swapping at the defaults
  ([Host memory](#host-memory-flash-next));
- **mixed or uneven cards**: a per-card calibration and a layer split by speed;
- **4 or more cards**: see [4 or more cards](#4-or-more-cards); `FLASH_PAR=pptp` is experimental;
- **small cards** (8-16 GB): see [Smaller cards](#gpus);
- **RTX 3000, 4000 and 5000 series**: built in, nothing to set ([what has run where](#gpus)).

If a setup like this is still slow or misbehaves, please open an issue with the start-up log, started with
`FLASH_BOX_REPORT=1` (it adds `[box]` lines on each card and link; on 4 or more cards they are on by default): those,
the `[qflash] parallel mode` line and the `host RAM plan` line are what I need to look into it.

### GPUs

QEngine runs on the RTX 3000, 4000 and 5000 series with no extra steps. The Docker images carry the code for all three,
and a source build targets the GPUs it finds (`-DCMAKE_CUDA_ARCHITECTURES` sets others).

| series | code | what has run on it |
|---|---|---|
| RTX 3000 | sm_86 | 3090: all tuning (82 SMs, tile shapes, split counts, memory budgets) targets it, and everything published here was measured on it. Community: 4× modded 3080 20 GB ([#9](https://github.com/bpx03/QEngine/issues/9)) |
| RTX 4000 | sm_89 | built, but no run on record yet; reports are welcome |
| RTX 5000 | sm_120 | community: 2× 5090 ([club-3090 #1826](https://github.com/noonghunna/club-3090/issues/1826)), 4× 5080 16 GB ([#13](https://github.com/bpx03/QEngine/issues/13)) |

The 4000 and 5000 series use the settings tuned for the 3090, so they may have speed left unused. What limits a card
is its memory; see below.

How many cards each model runs on:

| model | cards | how |
|---|---|---|
| Qwen3.8-Flash-Next | 3 (tuned), 2 | tensor parallel or pipeline, picked at start (`FLASH_PAR=auto`) |
| Qwen3.8-Flash-Next | 4 | tensor parallel when peer access between all 4 equal cards passes the start-up check, else pipeline (`FLASH_PAR=auto`); community runs only, see [4 or more cards](#4-or-more-cards) |
| Qwen3.8-Flash-Next | 5 or more | pipeline (`FLASH_PAR=pp`); tested only as 4 pipeline stages on my 3 cards |
| Qwen3.8-Flash-Next | 1 | not supported |
| Qwen3.8-27B | 3 (tuned), 2 | tensor parallel |
| Qwen3.8-27B | 1 | experimental, `QE_MAX_SEQS` 1 to 4 |

**Smaller cards** (Flash-Next; measured on my 3090s with all but 12 GB or 8 GB of each card taken by another process
before the start, November 3, 2026; defaults otherwise, 16 conversation slots; c=1 / c=4: greedy decode of 400-token
replies, thinking off; prefill of an 11.5K-token prompt; a 53K-token needle; the 27B follows below):

| model | cards x free VRAM | context | c=1 / c=4 tok/s | prefill tok/s | needle |
|---|---|---:|---:|---:|---|
| Flash-Next | 3 x 12 GB | 262,144 | 66.5 / 145.1 | 4,612 | pass |
| Flash-Next | 3 x 8 GB | 262,144 | 47.2 / 91.1 | 3,819 | pass |
| Flash-Next | 2 x 12 GB | 262,144 | 40.7 / 78.7 | 3,546 | pass |
| Flash-Next | 2 x 8 GB | 65,536 (fitted at start) | 34.7 / 55.1 | 2,263 | pass |

- Flash-Next keeps its dense weights, slot state and KV cache on the cards and puts the experts that do not fit in
  host RAM (on 8 GB cards nearly all of them, so decode is host-link bound). The minimum per card is about 7.5 GB on
  3 cards and about 8 GB on 2 cards at a 65K context (about 10 GB at 262K); when the requested context does not fit,
  it starts with the largest that does and says so (`--max-ctx` sets it, `FLASH_MAX_SEQS` fewer slots leave room for
  more). Below the minimum it stops with a message naming what to change.
- 27B needs its weights on the cards: about 5 GB per card on 3 cards and 7.2 GB on 2, plus buffers, the conversation
  slots' state (110 MB per slot and card on 3 cards, about 200 MB on 2) and the KV cache. On a small card it starts
  with fewer slots and a smaller VRAM reserve (logged; `QE_MAX_SEQS`, `QE_RESERVE_GB` set them) so the KV cache holds
  at least a 32K context: 8 GB cards work on 3 cards, 12 GB cards on 2. Below that it stops with a message (exit
  code 3).
- 27B on one card needs about 15.8 GB for the weights alone, so a single 16 GB card does not start; 2 x 16 GB does.

**27B on smaller cards, and with a 4-bit KV cache (opt-in, `QE_KV_BITS=4`)** for more context. Each key and value
row is rotated (a fixed random Hadamard transform, which spreads the outlier channels) and stored in 4 bits with one
fp16 scale per 32 values: 144 bytes per row instead of 256 with FP8, so the pool holds 1.6-1.7x the tokens (the MTP
layer stays FP8). Measured like the table above (November 14, 2026, same day for both caches, before the INT4
verify head of 1.3.6, which leaves each card more room for the KV pool; the 3 x 8 GB FP8 row is from November 3;
needle at about 60 % of the served context; slots as fitted for FP8):

| cards x free VRAM | KV cache | context | c=1 / c=4 tok/s | prefill tok/s | needle |
|---|---|---:|---:|---:|---|
| 3 x 12 GB | FP8 | 255,649 | 220.2 / 630.1 | 6,372 | pass |
| 3 x 12 GB | 4-bit | 262,144 | 189.8 / 653.4: the context now fits DFlash2, which is slower than MTP on this story prompt (`QE_DRAFTER=mtp`: 212.9 / 664.6) | 6,231 | pass |
| 3 x 8 GB | FP8 | 44,675 (9 slots) | 220.6 / 619.3 | 6,288 | pass |
| 3 x 8 GB | 4-bit | 67,584 (9 slots) | 215.2 / 630.2 | 6,364 | pass |
| 2 x 12 GB | FP8 | 30,720 (14 slots) | 171.5 / 338.5 | 4,568 | pass |
| 2 x 12 GB | 4-bit | 46,080 (14 slots) | 190.7 / 513.3 | 4,537 | pass |
| 1 x 24 GB, `QE_MAX_SEQS=1` | 4-bit | 240,640 with DFlash2 (262,144 with `QE_DRAFTER=mtp`; FP8 on 1.3.5.8: about 191K) | 102.9 / - | 2,550 | pass |
| 2 x 8 GB | either | does not start (the weights do not fit) | - | - | - |

- Quality: next-token KL against a bf16 KV cache over 100K / 32K / 64K-token documents is 4.4e-3 with 4 bits and
  1.5e-3 with FP8 (for scale: the INT4 weights against BF16 are 1.45e-2); top-1 agreement stays at FP8's level, a
  passphrase needle at 130K (3 depths) and 239K passes, MTP / DFlash2 acceptance within 2 %. It is opt-in because it
  is not lossless against FP8; on cards with room the FP8 default is the better choice.
- Speed: decode within 2 % of FP8 at 32K and faster at long context (128K: -9 % time per step); prefill 0.4 % slower
  at 128K and 3 % at 256K (the prompt's keys are converted for the prefill kernels, about 0.5 KB per key and KV head
  of the served context). On 3 x 12 GB the context now fits the DFlash2 drafter, which `QE_DRAFTER=auto` then loads,
  as on 24 GB cards: warm c=1, it is 10 % faster than MTP alone on code and 7 % slower on prose, the same on both
  memory sizes (the c=1 numbers in the table are a first, cold request).
- Also checked with 4 bits: conversations restored from the RAM archive continue bit-identically, the disk cache
  resumes after a restart, the KV pool shrinks and grows back when another process takes and frees 16 GB of a card,
  and `--max-ctx 512K` (YaRN) serves 524,288 tokens on 3 cards with a 331K-token needle found.
- Not with `QE_LSA` (sparse attention reads FP8 keys; it is turned off with a start-up line) and not with
  `QE_KV_FP8=0`. Conversations archived or saved to disk with one cache format are not reused by the other.

GPU selection: `QE_DEVICES=0,2` (physical ids; Docker `QE_GPUS`), or `--devices` (indices within
`CUDA_VISIBLE_DEVICES`). By default every visible GPU is used. Each engine locks the GPUs it uses: a second engine on
a card in use stops at start with the first one's pid and command line (`QE_ALLOW_SHARED_GPU=1` skips the check).

### With and without GPU P2P

GeForce cards have no GPU-to-GPU P2P with the stock NVIDIA driver. A community patch of the open kernel modules
([aikitoria/open-gpu-kernel-modules](https://github.com/aikitoria/open-gpu-kernel-modules), a fork of tinygrad's patch
that tracks current driver versions, with Resizable BAR on)
enables it. QEngine detects which one you have and needs no setting.

Since 1.3.4 both engines are fast without P2P: their tensor-parallel exchanges copy through pinned host memory by
DMA (the copy engines), and the GPU cores only wait on flags in their own memory. Measured on 3× RTX 3090 (PCIe 4.0
x16), with P2P forced off (`QE_P2P=0`) against P2P on (November 1, 2026):

| measured (s, lower is better) | without P2P | with P2P | 1.3.3 without P2P |
|---|---:|---:|---:|
| Flash-Next prefill, 10K / 32K / 90K-token prompt (`flash_run`) | 1.83 / 6.06 / 17.03 | 1.35 / 4.54 / 13.06 | 3.75 / 12.55 / 34.95 |
| Flash-Next decode step, one conversation | 9.9 ms | 9.5 ms | 12.7 ms |
| 27B prefill, 16K-token prompt | 2.68 | 2.59 | 3.94 |

The 27B's decode speed does not depend on P2P. Without P2P the 27B uses a smaller KV pool (its position-split KV
layout needs P2P). Inside Docker, P2P works exactly when it works on the host (check the `P2P:` / `[comm]` lines of the
start-up log).

### Parallel mode (Flash-Next, `FLASH_PAR`)

Flash-Next can share the cards in several ways; the 27B always runs tensor parallel. `FLASH_PAR` selects the mode
(source: `FLASH_PAR=pp server/run.sh ...`; Docker: `-e FLASH_PAR=pp`).

| mode | `FLASH_PAR` | what it does | recommended for | picked by `auto`? | how to force / options |
|---|---|---|---|---|---|
| automatic (default) | `auto` | picks `tp` or `pp` at start from a link probe, a short per-card speed calibration and a model of a typical agent request | almost every machine | - | `FLASH_PAR_AUTO_P=32768` weighs 32K-token prompts instead of 8K (favours `pp`) |
| tensor parallel | `tp` | every layer split over the cards; all cards work on every token, exchanges in every layer (P2P, or host-staged without it) | 2-3 equal cards: fastest decode and short prompts, with or without P2P | yes: 2-3 equal cards; exactly 4 equal cards with verified peer access between all of them, if it fits | `FLASH_PAR=tp`; `FLASH_COMM` sets the exchange path |
| pipeline | `pp` | each stage holds a contiguous range of whole layers; prompts flow through in micro-batches, several conversations decode as groups moving stage to stage; only a 40 KB row per token crosses between stages, so it needs no P2P | long uncached prompts with short replies (RAG, long documents); uneven cards; 4 or more cards | yes: 5+ cards; 4 cards when peer access is missing or unverified, the cards are uneven, or tp does not fit; and uneven cards (or 2-3 cards without P2P) when it wins the mix | `FLASH_PAR=pp`; `FLASH_PP_LAYERS=17,17,14` sets layers per stage; a card may hold several stages (`--devices 0,1,2,0`; a test layout, it adds no compute) |
| pipeline over TP groups (experimental, untested on 4 cards) | `pptp` | a pipeline whose stages are tensor-parallel groups of 2-3 cards; per-layer exchanges stay inside a group | 4+ cards where P2P exists only inside card pairs (two PCIe switches, two CPU sockets) | no, opt-in only | `FLASH_PAR=pptp FLASH_PP_MAP=0,1\|2,3` (`,` inside a stage, `\|` between stages); without a map `FLASH_PP_TP=2` pairs consecutive cards |

`auto` models an 8K-token uncached prompt and a 512-token reply, averaged over 1, 4 and 8 conversations at once
(capped at `FLASH_MAX_SEQS`); `pp` must beat `tp` by 10 % over that mix to be picked. With P2P on equal cards it is
always `tp`. Settings of the pick and the pipeline: [docs/advanced.md](docs/advanced.md#parallel-modes-flash_par).

**Recipes**

| your machine and workload | setting |
|---|---|
| 2-3 equal cards, with or without P2P, agents / chat | leave `auto` (= `tp`) |
| mostly long uncached prompts (RAG, long documents, short answers) | `FLASH_PAR=pp`, or `FLASH_PAR_AUTO_P=32768` to let `auto` decide on that basis |
| uneven or mixed cards | leave `auto`: it calibrates each card and picks `pp` with a split by speed when that wins |
| exactly 4 cards | leave `auto`: `tp` with verified peer access between all of them, otherwise `pp`; mostly long uncached prompts: `FLASH_PAR=pp` ([why](#4-or-more-cards)) |
| 5 or more cards | leave `auto` (= `pp`); if your cards pair up on P2P, try `FLASH_PAR=pptp FLASH_PP_MAP=0,1\|2,3` |
| steering vectors or `FLASH_KV=ram` needed | `FLASH_PAR=tp` (2-4 cards) |

```bash
FLASH_PAR=pp server/run.sh 8080 --model models/Qwen3.8-Flash-Next-QE-INT4
docker run ... -e FLASH_PAR=pp -e QE_MODEL=/app/models/Qwen3.8-Flash-Next-QE-INT4 ghcr.io/bpx03/qengine:latest
docker run ... -e FLASH_PAR=pptp -e FLASH_PP_MAP='0,1|2,3' -e QE_GPUS=0,1,2,3 ... ghcr.io/bpx03/qengine:latest
```

**What was picked.** The start-up log has one line with the mode and the reason, e.g.
`[qflash] parallel mode: tp (auto: no peer access, but TP not beaten by the margin over the mix); probe: ...`, and a
`[qflash] cards:` line with each card's measured speed and free memory (cards of the same model count as uneven only
when a longer re-calibration confirms the gap). `/api/stats` on the monitoring port shows the same under `parallel`.

**The trade-off.** `pp` prefills 32K-90K-token prompts up to 1.8× faster than `tp` (3 cards with P2P: a 90K prompt
in 9.9 s against 13.6 s; on 2 cards with P2P the two are about even), decodes 4-8 conversations at 0.83-1.03× of
`tp`, but one conversation at only 0.54-0.65×; 10K prompts with P2P are faster in `tp`. Measured on the server, same build, cold prompts end to end and decode of 1 / 4 / 8
conversations (November 1, 2026):

| cards, link | mode | 10K prompt | 32K prompt | 90K prompt | decode tok/s, 1 / 4 / 8 at once |
|---|---|---:|---:|---:|---:|
| 3, P2P | `tp` | 1.52 s | 5.20 s | 13.55 s | 244 / 541 / 773 |
| 3, P2P | `pp` | 1.72 s | 3.89 s | 9.88 s | 132 / 447 / 696 |
| 3, no P2P | `tp` | 2.05 s | 7.09 s | 18.03 s | 232 / 487 / 708 |
| 3, no P2P | `pp` | 1.77 s | 3.95 s | 10.21 s | 136 / 438 / 703 |
| 2, P2P | `tp` | 2.54 s | 5.67 s | 15.96 s | 91 / 200 / 246 |
| 2, P2P | `pp` | 3.08 s | 5.59 s | 14.75 s | 56 / 203 / 245 |
| 2, no P2P | `tp` | 3.78 s | 8.31 s | 23.45 s | 88 / 195 / 236 |
| 2, no P2P | `pp` | 2.97 s | 5.63 s | 14.85 s | 57 / 201 / 241 |

Each row is one fresh server; the decode runs come first with a cold expert cache, which costs 2-card single-stream
decode most. The prompts and method differ from the headline table, so compare rows within this table only.

**Uneven cards.** `pp` splits the layers by each card's measured speed and free memory. With one 3090 slowed to a
third of its compute (a test setting), the split moved 4 layers off it: prefill about 30 % and decode 13 % faster than
an equal split.

**What `pp` and `pptp` do not serve**: image input in `pptp` (refused with a clear message; `pp` serves images since 1.3.5.1, experimental), steering vectors (not loaded),
`FLASH_KV=ram` (on 2 or 3 cards the server runs `tp` instead and logs it; on 4 or more cards the start is refused with
a message), activation capture; lookup drafts are off. Structured output and the thinking budget work as in `tp`
(a constrained step runs through the stages as a batch of one).

#### 4 or more cards

I have no 4-card machine: the 4-way split was
tested as 4 pipeline stages on my 3 cards (two stages on one card), where it gave the same output bit for bit as 3
stages. `pptp` was tested only in a 3-card layout (`0,1|2`), where its next-token probabilities match `tp` within the
run-to-run noise. A community run on four RTX 5080 cards (`tp`, 1.3.5.7 and 1.3.5.9, [#24](https://github.com/bpx03/QEngine/issues/24))
confirmed Flash-Next's long-context recall there: needles found up to 240,664 tokens at 262K, and at 1M up to 843,147
on 1.3.5.7 and 813,180 on 1.3.5.9 (one ladder rung lower), the same level as on 3 cards. More reports from 4-card machines are welcome.

**Since 1.3.5.4 (experimental):** on exactly 4 equal cards, `auto` picks `tp` when peer access between all of them passes the data check
at start and `tp` fits the free VRAM; otherwise it picks `pp`. With 5 or more cards it is always `pp`. If `tp` can't start
(out of device or host memory during the load, or a CUDA error or a stall in the check), the server restarts itself in
`pp` and says so in the log, at the cost of the partial load. On a card whose free VRAM is badly fragmented, a `tp` that did
load can still stop later on a request: use `FLASH_PAR=pp` there. This rule rests on one user's measurements on one rig
(4× RTX 5080 16 GB behind one PCIe switch, 1.3.5): one 1,000-token stream at 310.3 tok/s in `tp` against 145.4 in `pp`. On
1.3.4.3, prefill at 32K was higher in `pp` (7,367 against 5,466 tok/s), so for mostly long uncached prompts set
`FLASH_PAR=pp`. The rest was tested on 3 cards only. On 1.3.5 to 1.3.5.3, `auto` always picks `pp` on 4 cards and
prints `peer access no` even if your cards have P2P, so set `FLASH_PAR=tp` yourself.

### Link probe and `FLASH_COMM` / `QE_COMM`

At start both engines measure every GPU pair for a few milliseconds (P2P loads and stores, copy-engine copies, copies
staged through host memory), how much each transfer slows a kernel running next to it (the co-run tax), and whether
data sent over P2P really arrives intact:

```
[comm] topology: numa -1,-1,-1 (1 node), PCIe x16,x16,x16, P2P rank 0-1:0 0-2:0 1-2:0
[comm] P2P data check: SM loads, SM stores and copy engine ok on every pair (...)
[comm] prefill transfers: P2P SM loads / stores, ... (FLASH_COMM=auto, auto: ...: P2P kept: tax over the cap, under the 1 NUMA node cap)
[comm] decode collectives (QE_DECODE_COMM=auto, real decode steps, median of 4 interleaved rounds of 12): single sequence: P2P SM stores (P2P ..., host memory ... ms/step, host faster in 0/4); batched (4 sequences): ...; calibration ... ms
```

With `auto` (the default) Flash-Next keeps P2P on fast links, moves the prefill transfers to the copy engine on slow,
narrow (e.g. an x4 slot) or cross-socket links, and never uses a transport that failed the data check. The line ends
with the reason. `FLASH_COMM` (Flash-Next) and `QE_COMM` (27B) force a path: `p2p`, `ce` (copy engine), `host`.
The rule and its thresholds: [docs/advanced.md](docs/advanced.md#how-flash_commauto--qe_commauto-choose-a-path).

Decode sends only small messages, but several per layer and step (all-reduces, the attention exchanges): either as
SM stores into the other cards' memory (P2P) or through the host path, with the same results. The host path is the
one the engines use without peer access (`QE_P2P=0`): each card writes its words once into pinned host memory and the
others read them; peer access stays on for prefill. Which one is faster depends on the board: peer stores can stall the
other kernels running on a card, and only the real model shows by how much. With `auto` both engines time a few real
decode steps on each path at the end of the start-up (one sequence, and four batched sequences), keep P2P or the host
path for each, and print both timings on the `[comm] decode collectives` line. `QE_DECODE_COMM=p2p` or `host` forces
the decode path (both engines; prefill keeps its own path). Before 1.3.5.6 the host candidate was a slower path
(about 45 % more time per step on 3 cards), so boards where P2P stores are expensive decoded slower than on 1.3.4.3. The measurements are cached in `~/.cache/qengine` (the Docker volume) and reused while the cards, links, driver and
build stay the same; `QE_COMM_CACHE=refresh` measures again. A cached decode line says `from the start-up cache, not
measured this boot` and carries the date of the measurement, so compare its ms/step across boots with care; a round
that was not measured (with fewer than 4 slots there is no batched round) prints `n/a`.

Set `FLASH_COMM=ce` (27B: `QE_COMM=ce`) yourself when the `[comm]` line says P2P but:

- long prompts fail with `non-finite values` (HTTP 500) or the log shows `GUARD` lines;
- a card sits behind something the link width does not show (a PCIe switch, a riser or extension cable, a chipset
  slot, a bifurcated slot);
- the cards differ (e.g. a 3090 next to a 3090 Ti) or sit in slots of different PCIe generations, and the line shows a
  P2P co-run tax of about 1.9 or more;
- prefill is clearly slower than the numbers here.

The copy engine gives the same output; on fast x16 links P2P is a few percent faster in prefill.

**NUMA.** On a machine with several NUMA nodes, Flash-Next places pinned host memory by GPU (each card's host-backed
experts and staging buffers on its node, the n-gram table interleaved over the GPUs' nodes). When the system does not
report a card's node (`GPU NUMA ID: N/A`), those buffers are interleaved over all nodes; `QE_NUMA` sets the nodes by hand.

### Host memory (Flash-Next)

Both engines plan their host-RAM parts from the machine's size, not from what happens to be free at start. If other
programs hold RAM at start, the plan warns and stays: the archive keeps below `MemAvailable` minus the margin while
memory is short and grows when it comes back. Only the Flash-Next n-gram table is decided at start: when it does not fit
next to the experts as it is read, it comes from the page cache until the next restart (decode about 30 % slower at
c=1). If the free RAM is short at start, the server first waits up to 20 s for it (a previous server still exiting;
`QE_RAM_WAIT_S`). If the model can load it runs, with warnings; the load stops with a clear message only when the
experts really do not fit. The start-up line `host RAM plan: ...` says what was reduced. While serving, when another
program takes RAM, the archive gives memory back (log lines `archive: host memory below the margin ...`) and the server
keeps running.

Measured minimum free host RAM at start (3 cards, November 3, 2026): Flash-Next about 28 GB (the host-backed experts
must be pinned: about 14 GB on 3 cards, about 31 GB on 2, plus a margin), full speed (the n-gram table pinned) from
about 85 GB; 27B started with 24 GB free (the lowest I tried). Below its minimum Flash-Next stops at start with a
message naming the shortfall, before it pins anything.

| part | host RAM |
|---|---|
| host-resident experts (what VRAM cannot hold) | about 12 GB (3 cards), about 31 GB (2 cards) |
| n-gram embedding table (INT8, pinned) | 51.8 GB |
| conversation archive (`FLASH_KV_ARCHIVE_GB`) | 48 GB, filled as conversations leave VRAM |
| pinned system prompts (`FLASH_PREFIX_GB`) | 8 GB, as agent kinds appear |
| server process (Python, vision encoder, CUDA) | about 5 GB |
| `FLASH_KV=ram` (opt-in) | 13.5 GB per 1M tokens of KV, pinned at start; smaller when the host is short (see below) |

**The defaults fit the machine (since 1.3.4).** At start-up the engine plans its host memory from `MemTotal` and
`MemAvailable` (and a cgroup / `docker --memory` limit, if one is set). It first sets aside a reserve for the system
and the desktop: max(8 GB, 8 % of RAM). The rest goes, in this order, to:

1. the host-resident experts, which are not optional;
2. the n-gram table. It is pinned when it fits next to an 8 GB minimum archive. Otherwise it is read through the page
   cache (as with `FLASH_NGRAM_PIN=0`, below), and part of the remaining RAM stays free for the page cache to hold
   its rows;
3. the archive and the pinned system prompts, which get what is left, up to 48 + 8 GB.

With `FLASH_KV=ram` the KV pool in host RAM (`FLASH_KV_RAM_TOKENS`, 13,520 bytes per token, 13.5 GB at the default 1M;
7,488 bytes and 7.5 GB with `FLASH_KV_BITS=4`) is in the plan as well. It is pinned at start, like the experts and the n-gram table, so these three together must fit
both the RAM the machine has and what is free at start (`MemAvailable` minus the margin). When they do not, the plan
gives way in this order: the archive and the pinned prompts first; then the KV pool, down to the seats times the
context (`FLASH_MAX_SEQS` x `--max-ctx`, so every seat still holds a full window); then down to one window; then the
n-gram table moves to the page cache (it costs decode speed for every request, so it goes last). The experts are never
reduced; if even the smallest plan does not fit, the log warns and the server starts anyway. The start-up line shows
the pool and what is pinned at start next to what was free.

**Flash-Next with a 4-bit KV cache (opt-in, `FLASH_KV_BITS=4`).** Each key and value row of the attention layers (the
MTP layer too) is rotated (a fixed random Hadamard transform, which spreads the outlier channels) and stored in 4 bits
with one fp16 scale per 32 values: 576 bytes per layer and token instead of 1,040 with FP8, 7,488 instead of 13,520
bytes per token in all. The VRAM pool keeps its 262,144 tokens and gives the freed memory to the expert cache; with
`FLASH_KV=ram` the same host RAM holds 1.8x the tokens (1.05M tokens: 7.9 GB pinned instead of 14.2). Measured on 3 cards
(November 14, 2026, same day for both caches): KL against the FP8 cache 4.95e-2 on 32K-100K documents (two FP8 runs
that differ only in summation order: 2.52e-2), top-1 agreement 92.2 %; needle at 130K and at 1M (`FLASH_KV=ram`,
YaRN) pass; prefill of a 90K prompt 1-2 % faster, decode steps unchanged, MTP drafts accepted 3 % less (3.00 vs 3.10
tokens per step at 90K). Other values of `FLASH_KV_BITS` and settings that select an attention kernel without a
4-bit reader (`FLASH_ATTN_TC`, `FLASH_ATTN_DEC=0`) keep the FP8 cache and log it. On 2 cards, prompts of about
115K-188K prefill in 4096-row batches with the 4-bit cache (the smaller K/V arrays have less room for the big
batches). Known limit, from one community report on 4 cards
([#25](https://github.com/bpx03/QEngine/issues/25)): on a 1M-token recall ladder the 4-bit cache filled 83 % of the
window (every miss a refusal) against 91 % with FP8, so keep FP8 when maximum reach matters.

Nothing is planned beyond the RAM the machine has, so the defaults do not push it into swap. With about 140 GB or
more (3 cards) or about 160 GB or more (2 cards), the plan is exactly the defaults above. The log has one line with
the plan, and `/api/stats` reports it as `host_memory`:

```
[qflash] host RAM plan: MemTotal 98.8 GB, MemAvailable 92.8 GB, reserve 8.0 GB (OS + desktop), server base 6.0 GB,
engine buffers 1.3 GB; experts in host memory 31.2 GB (estimate 31.3 GB), n-gram table 51.8 GB from the page cache
(12.0 GB kept for it); KV archive 34.5 GB + pinned prefixes 5.7 GB; reduced: n-gram table not pinned: ...
```

Planned sizes by machine (start-up plan, desktop using about 6 GB):

| RAM | cards | n-gram table | archive + pinned prompts |
|---|---|---|---|
| 64 GB | 2 / 3 | page cache | 9.6 + 1.5 / 25.2 + 4.1 GB |
| 92 GB | 2 | page cache | 34.5 + 5.7 GB |
| 92 GB | 3 | pinned | 16.8 + 2.8 GB |
| 128 GB | 2 / 3 | pinned | 30.9 + 5.1 / 47.4 + 7.9 GB |
| 160 GB and more | 2 / 3 | pinned | 48 + 8 GB (the defaults) |

**Overrides.** A value you set wins: `FLASH_NGRAM_PIN=1` pins the table, `=0` keeps it in the page cache;
`FLASH_KV_ARCHIVE_GB` and `FLASH_PREFIX_GB` set the archive and the pinned prompts (`0` turns them off). If a value you
set does not fit, the log says so and the value is kept. On Flash-Next `FLASH_KV_ARCHIVE_GB=0` also turns off the pinned
prompts and every reuse that goes through the archive: no checkpoints, no copy of a cached prefix from another slot, and
a conversation that leaves its slot is prefilled again on its next turn. This holds with `FLASH_KV=ram` too: the KV pool
in host RAM holds only the conversations in the slots, it does not replace the archive. `QE_HOST_BASE_GB` (6) changes the share counted for the
server process.

**Keeping RAM free for other programs: two settings, used at different times.**

| setting | when it acts | what it does | raise it when |
|---|---|---|---|
| `QE_HOST_RESERVE_GB` | once, at start | RAM the start-up plan leaves out when it sizes the n-gram table, the archive and the pinned prompts | other programs will need more RAM later, or the plan comes out too large |
| `QE_MEM_MARGIN_GB` | all the time, while serving | free RAM (`MemAvailable`) the archive keeps: below it, the archive stops growing and gives memory back | programs that start later get squeezed, or swap appears |

On a small machine, lower them to leave more for the archive: with both at their 8 GB default, a 16 GB machine has
almost no archive, so a conversation that leaves VRAM is recomputed when it returns (a planned archive under 2 GB gets a
warning line at start; the start goes on). The lower you go, the closer the
kernel's OOM killer gets, and it would end the server.

- On **2 cards** about half of the expert groups stay in pinned host memory (about 15 GB per card) and are read over
  PCIe or copied into the expert cache when hot.
- While it fills, the archive keeps at least max(8 GB, 5 % of RAM) free (`QE_MEM_MARGIN_GB`), and gives memory back
  when other programs need it. The engine also watches the kernel's memory-pressure and swap-in counters while it runs:
  when other programs squeeze the host, it stops growing, shrinks the archive, drops pinned prompts and, last, moves the
  n-gram table to the page cache, one logged stage at a time, and keeps serving (`QE_MEMP=0` turns this off;
  [details](docs/advanced.md#host-ram-safety)).
- **n-gram table in the page cache** (`FLASH_NGRAM_PIN=0`, or chosen at start-up): the table stays in the file mapping
  and a host thread copies the rows each step needs. With the table fully in the page cache, agent throughput at 8
  conversations was 793 tok/s (pinned: 805); with the whole server limited to 12 GB of RAM, 493 tok/s (3 cards,
  October 25, 2026). After the load the engine drops the page cache of the weight files (it never reads them again),
  so they don't push the table out of the page cache (`FLASH_WEIGHTS_COLD=0` keeps it). Details:
  [docs/advanced.md](docs/advanced.md#disk-mode-for-the-n-gram-table).
- The 27B needs much less: its archive defaults to 32 GB (`QE_KV_ARCHIVE_GB`) plus 8 GB of pinned prompts
  (`QE_PREFIX_GB`), sized the same way. Its defaults fit from 64 GB of RAM.

### Operating system

Linux only (developed on Fedora 44). **Windows, including Docker Desktop / WSL2, is untested**: WSL2 has no GPU P2P
and limits pinned host memory, which the archive and Flash-Next's host-resident parts rely on.

## Models

### Qwen3.8-Flash-Next

48 layers (36 Gated DeltaNet + 12 sparse-attention layers), 512 routed experts (top-10) plus a shared expert,
4-stream hyper-connections and a per-layer n-gram embedding table. What the engine does:

- experts split over the cards in 128-wide groups (3 cards: 176/160/176, so the middle card can drive a desktop;
  `--split` sets one weight per card); INT4 expert GEMV / GEMM, dense parts INT4 or INT8 (stored that way in the
  checkpoint, or converted to INT8 at load where the file carries BF16; see the precision table below);
- an expert cache: the least-used expert groups live in pinned host memory and are copied into free VRAM while hot;
- attention KV in FP8, split by position over the cards, with the indexer's top-512 block selection beyond 2K
  tokens; 262,144 tokens of context per conversation;
- MTP drafts plus lookup drafts (one conversation decoding alone: 3 to 5 drafts per step, picked from the draft head's
  confidence; batched steps: up to 3), steps launched ahead, CUDA graphs;
- up to 16 conversations at once with batched decoding; prompts that arrive together share prefill batches (the
  expert weights are read once for all of them);
- prefix reuse, checkpoints and a host-RAM archive of conversations; image input (`--vision 1`); structured output.

**Model files.** The [Hugging Face download](https://huggingface.co/bpx03/Qwen3.8-Flash-Next-QEngine) is ready to
run. Since 1.3.4.1 its default revision stores the DeltaNet projections (in_proj_qkv / z / out_proj) as INT8 (group
128) and has the shared expert and the n-gram key/value projections calibrated with GPTQ (INT4); the routed experts
are unchanged. That brings the model about twice as close to BF16 (see
[Quality](#quality)) and costs decode speed: about 5 % with 8 conversations, about 4 % single-stream on the club-3090 bench and up to
9 % at one request in the concurrency test (the DeltaNet projections are read on every step, 0.35 GB more per card);
prefill speed is unchanged. The download is about 1 GB larger. The engine reads the format from the files, so the previous weights
still work as they are (QEngine 1.3.4 and older stop at load on the new files with `tensor not found:
...linear_attn.in_proj_qkv.weight_packed`: update QEngine, or download `--revision v1.3.4`):

```bash
hf download bpx03/Qwen3.8-Flash-Next-QEngine --revision v1.3.4 --local-dir models/Qwen3.8-Flash-Next-QE-INT4-v1.3.4
server/run.sh 8080 --model models/Qwen3.8-Flash-Next-QE-INT4-v1.3.4       # Docker: -e QE_MODEL=/app/models/...-v1.3.4
```

**What runs in which precision** (1.3.4.1 default weights; the files store exactly these formats except where noted):

| part | precision | note |
|---|---|---|
| routed experts (512 per layer) | INT4, group 128 | Intel's AutoRound quantization, repacked bit-exact |
| DeltaNet projections (in_proj_qkv / z / out_proj) | INT8, group 128 | 1.3.4 weights: INT4 |
| shared expert, n-gram key / value projections | INT4, group 128 | calibrated with GPTQ (1.3.4 weights: round-to-nearest) |
| attention q / k / v / o, lm_head, router, hyper-connection mix matrices | INT8, group 128 | BF16 in the files, converted at load |
| embeddings, n-gram table | BF16 / INT8 | the n-gram table ships as INT8 |
| norms, gates, DeltaNet a / b and conv, indexer | BF16 | |
| activations, accumulation | BF16 / FP16, FP32 accumulation | prefill GEMMs use INT8 activations |
| attention KV cache | FP8 (E4M3) | 4-bit opt-in: `FLASH_KV_BITS=4` |
| MTP draft head | INT8, group 128 (experts and shared expert INT4) | attention and fc BF16 in the files, converted at load |

**Context up to 1M tokens (opt-in)**: `FLASH_KV=ram server/run.sh 8080 --model <dir> --max-ctx 1M` turns on the
model card's YaRN RoPE scaling (Qwen3.8-27B: `--max-ctx 1M` on 3 cards, `--max-ctx 512K` on 2, no `FLASH_KV`). It applies to every request of that server, so use it only on a server meant for long
documents; see [docs/advanced.md](docs/advanced.md#context-up-to-1m-tokens-yarn-opt-in).

**KV cache in host RAM (opt-in)**: by default the attention KV of all conversations shares one VRAM pool of 262,144
tokens. With `FLASH_KV=ram` it lives in pinned host RAM (`FLASH_KV_RAM_TOKENS`, default `1M`, 13,520 bytes per token
for the whole machine) and VRAM keeps the indexer keys and a cache of recent blocks; output is bit-identical. Many
long conversations then stay resident: with 4 conversations of ~64K tokens sending follow-ups at once, output went
from 455 to 580 tok/s on 3 cards and from 233 to 332 tok/s on 2 cards (October 30, 2026). It is not the default
because short-request throughput is about 12 % lower (the indexer keys and block cache take VRAM from the experts).
Details: [docs/advanced.md](docs/advanced.md#kv-cache-in-host-ram-flash-next).

### Qwen3.8-27B

- INT4 weights repacked at load (a few seconds, no conversion) into tensor-core layouts.
- Verify head: an INT4 copy of `lm_head` screens the vocabulary, and each row's top 16 candidates (top 64 for sampled
  rows and logprobs) are rescored exactly from the BF16 rows in pinned host RAM, so greedy output takes the BF16
  argmax. It needs 2.5 GB of pinned host RAM on one card (0.85 GB per card on 3) and 0.64 GB less VRAM per card than
  an INT8 head. Without that host RAM, or with `QE_HEAD4R=0`, every card uses the INT8 head.
- Tensor parallel over PCIe; the four full-attention KV heads are split by position (3 cards with P2P), so no KV head
  is duplicated. All-reduces run inside the kernels and inside CUDA graphs.
- Speculative decoding, verified over the full vocabulary, so outputs are unchanged: the [DFlash2 block
  drafter](#dflash2-block-drafter-27b-on-when-it-fits) (7 drafts per step) for a conversation that decodes alone,
  when its memory fits; MTP with 1 to 7 drafts per step, chosen from the measured acceptance, for everything else.
  Lookup drafts on the GPU.
- Up to 32 conversations (`QE_MAX_SEQS`, default 16; more open requests are parked, see
  [Serving behaviour](#serving-behaviour)); KV cache in FP8 in one pool per card (1,232,896 tokens on 3 cards with P2P
  and 16 slots, 1,075,200 with 32; `QE_KV_BITS=4` stores it in 4 bits for small cards, see [GPUs](#gpus)); 262,144
  tokens per conversation.
- Prompt-cache states (snapshots of the recurrent state, about 150 MB of pinned host RAM each, split over the cards):
  up to 8 per sequence slot while they take at most 8 % of the host's RAM (or of a container's memory limit), at least
  4 per slot and at least 32 (`QE_SNAPSHOTS`); with 16 slots on a 256 GB host that is 128 states, about 19 GB. The
  states within the 8 % are pinned at start while the host has room, before the first request (`QE_ARCHIVE_WAIT_S`);
  the rest only as the store fills. With 32 for every slot count, 8 agent
  conversations on 32 slots dropped each other's states and re-prefilled from the system prompt; with 4 per slot, 16
  conversations on 16 slots still did. The state at the end of each
  prompt is copied to the host beside the first decode step instead of before it (about 6 ms less to the first token
  and per reply on one card, 2 ms on three; 16 MB of VRAM per card for the staged convolution rings;
  `QE_SNAP_ASYNC=0` copies it before the first step, as before).

**Release files.** Two files are attached to every [release](https://github.com/bpx03/QEngine/releases/latest):
`model_mtp_ft.safetensors` (849 MB, an MTP head fine-tuned on the engine's own answers) and `token_rank.bin` (the
draft-vocabulary ranking). The server downloads them on the first start into `~/.cache/qengine/assets`, checks them
against the release's `SHA256SUMS` and reuses them offline (the model directory is never written). Without them the
engine runs, just slower. Offline machines: put them into the model directory by hand:

```bash
cd models/Qwen3.8-27B-INT4
for f in model_mtp_ft.safetensors token_rank.bin SHA256SUMS; do
  curl -LO https://github.com/bpx03/QEngine/releases/latest/download/$f
done
sha256sum -c SHA256SUMS
```

`QE_FETCH_ASSETS=0` turns the download off; the start waits for it at most `QE_FETCH_WAIT_S` (120) seconds.

#### DFlash2 block drafter (27B, on when it fits)

Since 1.3.5.8 the 27B can draft with **DFlash2**, a small block drafter (the W4A16 build
[syvai/Qwen3.8-27B-DFlash2-W4A16](https://huggingface.co/syvai/Qwen3.8-27B-DFlash2-W4A16), Apache-2.0). It reads the
hidden states of five layers of the model and proposes 7 tokens per step; the model verifies them like MTP drafts, so
greedy output is identical to MTP, and sampled output follows the same distribution (only the random draws differ).

**Where it helps.** It is used for a conversation that decodes alone: one chat, one agent, one long answer. Measured
on this hardware (1.3.5.8; server, one conversation, against the MTP default of the same build):

| setup | short code | short prose | short math | 131K context |
|---|---:|---:|---:|---:|
| 1 card (`QE_DRAFTER=dflash2`) | +38 % | +17 % | +22 % | +10.5 % |
| 3 cards, P2P | +34 % (321 → 432 tok/s) | +6 % (230 → 244) | +15 % (297 → 341) | – |

The gain depends on the text: code and other predictable output gain most; long reasoning that MTP and lookup
drafts already predict well gains little (a 32K prompt with a long thinking part: +2 %).

Second choices on one card: when the drafter is unsure about its first three drafts (greedy replies), the step
verifies four drafts plus the drafter's second choice for each of the first three positions in the same 8 rows; a
right second choice keeps one more token. Output is identical. Measured on one card (engine, same build on / off):
+3.5 % on a 30-prompt mix, +4.6..4.9 % on the three short benchmark prompts, +2.7 % / +1.6 % at 32K / 96K, about level
on file edits. `QE_DF_SIB=0` turns it off.

Two conversations at once on one card: when exactly two conversations decode in the same step, each drafts with its
own DFlash2 context (8 rows each); output stays identical to each conversation decoding alone. Measured on one card
(server, two 512-token replies at once): +2.8 % for the pair as a whole; +8 % per step while both run (engine benchmark). With three or more
conversations in a step, and on 2 or 3 cards, batched steps draft with MTP as before (three at once on one card was
level to slightly slower, four 5 % slower). `QE_DF_BATCH=0` turns it off; `QE_DF_BATCH=n` allows it up to n
conversations per step. Grammar-constrained replies (`response_format`, a forced tool call until its header, `logprobs`) always keep MTP; a `tool_choice: none` reply drafts as usual. Agent turns that edit a file already in the context come out about 3 % slower,
because the model copies text the drafter no longer sees (it keeps the last ~2K positions); turns that write new text
are faster.

**What it costs.** VRAM on every card, plus 0.25 GB of pinned host RAM:

| cards | VRAM per card | KV pool (all conversations together) | context per conversation |
|---|---:|---|---|
| 1 | 1.20 GB (three context rings for the two-conversation steps; `QE_DF_BATCH=0`: 1.16 GB) | about −38K tokens | `QE_MAX_SEQS=1`: **206,848 → about 165,000** (default `QE_RESERVE_GB=1.5`) |
| 2 | 0.82 GB | 675,840 → 623,616 tokens | 262,144, unchanged |
| 3 | 0.70 GB | 1,298,432 → 1,232,896 tokens | 262,144, unchanged |

On 2 and 3 cards the default context still fits. **On one card it does not**, which is why a single card stays on MTP
by default.

**When it is on (`QE_DRAFTER`):**

- `auto` (default): at start the server loads DFlash2 only when the requested context (`--max-ctx`) and slots still
  fit with it, and prints one line saying which drafter it loaded and why (memory needed against memory free). The
  context is never lowered to make room for it. On 2 and 3 cards it is on with the defaults. **On one card the
  default `--max-ctx 262144` does not fit, so a single card stays on MTP**, and the start-up line tells you what this
  machine needs, e.g. `For DFlash2: --max-ctx <= 165K or QE_DRAFTER=dflash2` (the number is computed from your free
  VRAM). Either ask for that context or force it:
  ```bash
  # one card: room for DFlash2 by asking for less context (use the number from your start-up line)
  QE_DEVICES=0 QE_MAX_SEQS=1 server/run.sh 8080 --model <dir> --max-ctx 150K
  # or force it: the context becomes whatever still fits (logged)
  QE_DEVICES=0 QE_MAX_SEQS=1 QE_DRAFTER=dflash2 server/run.sh 8080 --model <dir>
  ```
  With the default 16 slots one card has about 43K tokens per conversation and stays on MTP; DFlash2 on one card is
  meant for `QE_MAX_SEQS` 1 to 4.
- `dflash2`: always load it; the served context shrinks to what fits, with a start-up line.
- `mtp`: never load it (and nothing is downloaded); the previous behaviour, full context.

**Files.** On the first start the server downloads the drafter (1.28 GB, a pinned revision checked against its
sha256) into `~/.cache/qengine/dflash2` (Docker: the `qengine-cache` volume) and reuses it offline. Without network
access and without the file the server starts on MTP and says so in one line; it never stops for it.
`QE_FETCH_ASSETS=0` turns the download off; `QE_DFLASH_URL` points it at a mirror. A local copy: `QE_DFLASH=<dir or
file>`, or a `dflash2/` directory inside the model directory.

#### INT8 weights (27B, opt-in, experimental)

INT4 stays the default. Pointing the server at an 8-bit checkpoint runs the INT8 layer weights: closer to the BF16 model
and slower, because a decode step reads twice the weight bytes. Three cards are recommended; one card can't hold them.
The weights are at [bpx03/Qwen3.8-27B-INT8-QEngine](https://huggingface.co/bpx03/Qwen3.8-27B-INT8-QEngine).

```bash
hf download bpx03/Qwen3.8-27B-INT8-QEngine --local-dir models/Qwen3.8-27B-INT8
server/run.sh 8080 --model models/Qwen3.8-27B-INT8     # Docker: -e QE_MODEL=/app/models/Qwen3.8-27B-INT8
```

To build one from the official BF16 weights (no GPU, no calibration data; Python packages in `requirements-ref.txt`):

```bash
hf download Qwen/Qwen3.8-27B --local-dir models/Qwen3.8-27B-BF16
python3 tools/quant_int8.py --src models/Qwen3.8-27B-BF16 --out models/Qwen3.8-27B-INT8 \
    --kv-from models/Qwen3.8-27B-INT4     # copies the FP8 KV scales, which keep the full KV pool
```

INT8 KL and top-1 are from 1.3.5.2. Everything else, the INT4 KL and top-1 included, is from November 1, on older code, and not
rerun since; 3 cards:

| metric | INT8 | INT4 | INT8 / INT4 |
|---|---:|---:|---:|
| KL vs BF16, mean (320 positions) | 6.66e-4 | 1.47e-2 | 22× closer |
| top-1 match with BF16 | 99.7 % | 95.3 % | |
| decode narrative / code, tok/s | 184.6 / 276.7 | 266.6 / 387.7 | 0.69 / 0.71 |
| prefill 10K / 90K, tok/s | 4,816 / 4,098 | 6,077 / 4,866 | 0.79 / 0.84 |
| agent c=8, output tok/s | 810 | 1,215 | 0.67 |
| KV pool, 32 slots, 262K context, tokens | 566,272 | 932,864 | 0.61 |

The 8-pack has not run on INT8, so whether the lower KL gives better answers in real tasks is not known yet.

**Your own checkpoint** goes in through `--model`. The engine reads one `model.safetensors` (not shards),
compressed-tensors pack-quantized, symmetric, group 128: `weight_packed` int32 `[N][K/4]` with bytes LSB-first and the
stored value `w + 128`, `weight_scale` bf16 `[N][K/128]`, tensor names as in the 27B INT4 checkpoint. A format it would
misread stops the start with the reason. Without FP8 KV scales it runs a bf16 KV cache with half the pool and no position
split (`QE_KV_SCALES=<a 27B INT4 model.safetensors>` borrows the scales; this fallback has not run on cards). INT8
checkpoints use their own `model_mtp.safetensors`, not the fine-tuned head (`QE_INT8_MTP_FT=1` uses it). Not tried:
`lued/Qwen3.8-27B-INT8-W8A16-MTP`; it is sharded, so the start refuses it as it is.

#### Long documents (27B, opt-in)

Above 262K tokens the 27B needs YaRN (`--max-ctx 512K` or `1M`), and for prompts that long most of the time goes to
attention; `--lsa` makes that attention sparse (the index map is downloaded once and cached, see the docs). Both are off by default. YaRN is static: it applies to every
request of that server, short ones too, so run a separate server for long documents. What `--lsa` changes
(3× RTX 3090, measured November 3, 2026; details in [docs/advanced.md](docs/advanced.md#sparse-attention-for-long-prompts-opt-in)):

| you gain | you give up |
|---|---|
| 512K prompt about 2× faster (225 → 103–114 s), 1M about 3× (736 → 239 s) | exactness: each token reads 2,048–4,096 of its keys, which carry about 60–80 % of the full attention weight in my measurement |
| decode at 1M about 2× (106 → 227 tok/s), at 512K 1.5× | tested only on 2 retrieval tasks at 128K and 512K plus one 1M needle (same answers as full attention): not RULER, not reasoning quality over long documents |
| nothing changes below a prompt position of ~64K or a context of ~192K (full attention runs there) | only one conversation at a time benefits (the last long prompt's); others, and requests on a pinned shared system prompt, use full attention |
| | about 0.5 GB per card less KV pool; needs P2P and the FP8 KV cache; at most 1.87M tokens |

### Both models: context and the KV archive

- `--max-ctx` (default 262,144) is the context of one conversation; the KV pool of all conversations together is
  sized from free VRAM. The served context is never larger than the pool: when the pool is smaller than `--max-ctx`,
  the server still starts, serves at most the pool's length (`max_model_len` in `/v1/models`, the length check) and
  says so in one start-up line (27B on 2 cards with `--max-ctx 1M`): `context: requested 1048576 tokens, KV pool 659456 tokens, served 659456 tokens per conversation`.
- Conversations that leave VRAM go to a **host-RAM archive** (`FLASH_KV_ARCHIVE_GB` 48, `QE_KV_ARCHIVE_GB` 32; smaller
  on machines with less RAM, see [Host memory](#host-memory-flash-next)): returning to a 50K-token conversation is a
  copy, not a recompute.
- **Pinned system prompts**: the KV and state at the end of each agent kind's system prompt and tools are kept apart
  from the archive (`FLASH_PREFIX_GB` / `QE_PREFIX_GB`, 8 GB), so a new agent of that kind starts after its system
  prompt even when the archive is full.
- There is no disk cache by default. With `--disk-cache DIR` (both models, 200 GB at most, `--disk-cache-gb`) conversations
  are also written to files and survive a restart: a conversation that returns is read back instead of recomputed. Flash-Next
  has it since 1.3.5.3, experimental; details in
  [docs/advanced.md](docs/advanced.md#disk-cache). A failing disk costs only the cache; the server keeps serving.

### DeepSeek-V4.1-Flash (preview)

DeepSeek-V4.1-Flash-1017: 40 layers, 384 routed experts per layer plus a shared expert, Engram n-gram memory tables and
compressed sparse attention. QEngine runs it on three 24 GB cards plus host RAM, with the DSpark draft model for
speculative decoding. It is a preview in 1.5: it runs in the same server and API as the other models, with the
limits listed below.

**Model files.** I do not ship weights for this model. QEngine runs from the **Maya-S GGUF files** on Hugging Face
([peasantsmith/DeepSeek-V4.1-Flash-1017-Maya-GGUF](https://huggingface.co/peasantsmith/DeepSeek-V4.1-Flash-1017-Maya-GGUF),
revision `c33d87b8`), read as they are: the routed experts (IQ2_XXS / IQ2_S / IQ3_XXS / IQ3_S), the dense weights
(Q8_0), the Engram tables (Q6_K), the tokenizer and the chat format from the GGUF metadata, and the DSpark drafter from
the `dspark/` folder next to `Maya-S/`. Nothing is converted on disk and the model directory is never written. About
348 GB with the drafter:

    hf download peasantsmith/DeepSeek-V4.1-Flash-1017-Maya-GGUF --revision c33d87b8 \
      --include "Maya-S/*" "dspark/*" --local-dir models/DeepSeek-V4.1-Flash-1017-GGUF
    server/run.sh 8080 --model models/DeepSeek-V4.1-Flash-1017-GGUF/Maya-S

The server recognises the model from the GGUF metadata (architecture `deepseek41`) and loads the DSV4 engine
(`build_dsv4/libqdsv4.so`, built by `src/dsv4/build.sh`; the Docker image has it). Other revisions are not tested: the
start checks the model's dimensions and stops with the reason if they differ. The first start writes a few derived
files (tokenizer, the drafter's experts re-packed for the GPU, Engram hash constants) into
`~/.cache/qengine/dsv4/<model id>` (`--cache-dir` moves it; Docker: the `qengine-cache` volume), so the first start takes longer. After that the server
is ready about 41 s after start with the files in the page cache.

**What it needs**

- **Exactly three NVIDIA cards with 24 GB each**, compute capability 8.6 or 8.9 (RTX 3090 / 3090 Ti, RTX 4090; tuned
  on the 3090). The DSV4 engine is built for sm_86 only, which runs on RTX 4000 (sm_89) cards as is; RTX 5000 cards
  (sm_120) are not supported in 1.5. The engine uses the first three visible cards (`QE_DEVICES`); a fourth is
  ignored, two are not enough. The expert pool on each card is sized from its free VRAM, so a card that drives a
  desktop works, with fewer experts in VRAM.
- **GPU P2P between every pair of cards is recommended, not required.** With it, the context reservation is lazy:
  `--max-ctx` defaults to 262,144 and short chats run as fast as at 32K, because the long-context memory is taken from
  the expert pool only while a long prompt needs it and given back after. Without it (a stock driver, or
  `DSV4_NOCTXLAZY=1`) the reservation is static: `--max-ctx` still defaults to 262,144, but its memory is held for the
  whole run, so fewer experts fit in VRAM (on my cards without P2P, decode 2-3 % slower at short context than with
  `--max-ctx 32768`). When that context does not
  leave 8 GiB free on the fullest card, the start halves it (down to 32,768) with a WARNING line. Without P2P the cards
  also exchange through pinned host memory. A start-up line says which reservation runs. An explicit `--max-ctx`
  always wins.
- **Host RAM: about 170 GB free** for the full setup (on my machine `MemAvailable` drops by about 165 GB while it
  serves a 233K-token conversation). With less, the engine keeps fewer host copies of the experts and reads the rarest
  ones from the GGUF files; I tested that under a RAM hog taken while it serves, not on a machine with less RAM. It never allocates past `MemAvailable` minus
  a safety margin: it serves slower instead of running into the out-of-memory killer, and gives memory back while
  serving when the host runs short.
- **An NVMe drive for the model files.** The two Engram shards (5 and 6, about 161 GB) stay on disk and are read row by
  row while a prompt is processed. A hard disk or a network share is far too slow for this.
- **A CPU with AVX-512 is recommended; AVX2 is the minimum** (x86-64-v3: AVX2, FMA, F16C, BMI2). The experts that are
  not in VRAM run on the CPU. The engine picks its CPU kernels at start: the AVX-512 kernels need the Zen 4 set
  (AVX-512 with VNNI, VBMI, BITALG, BF16: AMD Zen 4 / Zen 5, Intel Sapphire Rapids and later); other CPUs get the AVX2
  kernels, with the same output but slower decode. The start-up line
  `CPU lane: N threads, AVX-512 kernels` shows which. The CPU part uses 24 threads by default
  (`--engine-args "--cpu-threads N"`).
- Linux and an NVIDIA driver with CUDA 13.1 support, as for the other models.

**What works**

- The same server and API as the other models: OpenAI `POST /v1/chat/completions` (streaming or not), Anthropic
  `POST /v1/messages` and `count_tokens`, `GET /v1/models`, `GET /health`. Responses carry `timings` (prompt and
  decode tokens and seconds).
- **Thinking** on by default (`--think`, a request's `enable_thinking`). `reasoning_effort`: `low`, `medium` / `high`,
  `max` / `xhigh`, or a number 1-100 (default 75); `none` turns thinking off. The reasoning comes back in
  `reasoning_content` (OpenAI) or thinking blocks (Anthropic). The thinking budget (`--thinking-budget`, a request's
  `thinking.budget_tokens` / `thinking_budget`) closes the reasoning at its count.
- **Tool calls** in the OpenAI and Anthropic formats (the model's own DSML call blocks are parsed into tool calls),
  `tool_choice` (`auto`, `none`, `required`, a named tool) and **structured output** (`response_format` `json_object`
  / `json_schema`).
- **Several requests at once** (agents): up to `--max-active 8` are in service, more wait in the queue. They take turns
  on the GPU: a long prompt in chunks of 10,240 tokens, an answer in slices of 16 decode passes, so a short request does
  not wait behind a long prompt or a long answer. The engine decodes one conversation at a time, so the total speed
  stays that of one request; a switch between conversations is exact (each one's text is the same as served alone with
  the same expert state).
- **Shared system prompts** (agent teams): when a second conversation starts with the same system message (tools
  included, at least 1,024 tokens) as an earlier one, that part is kept once, and every later conversation with it
  starts from the kept copy and computes only its own part. `--no-prefix-share` turns it off.
- **Multi-turn reuse and a host-RAM archive**: a follow-up turn reuses the cached prompt, also with thinking on;
  regenerating a reply reuses it too. Idle conversations move to host RAM (`--archive-gib`, default 32 GiB, least
  recently used out first) and come back with a copy instead of a recompute. `cache_prompt: false` in a request forces
  a full prefill. `usage.prompt_tokens_details.cached_tokens` shows what was reused.
- **Stop strings** (`stop`), matched in the answer only, never inside the reasoning.
- **Sampling**: `temperature`, `top_p`, `top_k`, `min_p`, `seed`; defaults from the GGUF metadata (temperature 1.0,
  top_p 1.0) unless set with `--temperature` / `--top-p`. Speculative decoding with DSpark keeps the sampled
  distribution exact.
- **Monitoring**: `qetop` and the dashboard on the metrics port (`/api/stats` has a DSV4 panel: held conversation,
  archive, K/V pool, prefix entries, passes). A conversation that has to be computed again because it left the archive
  shows up as a refill, counted with the prefill.

**Known limits (preview)**

- Text only: no images. No logprobs, no presence / frequency penalty (the DSV4 sampler has none), no activation
  steering (a request that asks for it gets "not supported").
- **Constrained replies**: structured output and `tool_choice` `required` / a named tool decode greedy replies
  (temperature 0) on DSpark passes, each pass checked against the grammar (the same text as one masked step per
  token, about 1.6x faster); sampled constrained replies decode one token per step without drafts, so they are slower.
  `QE_DSV4_GRAM_PASS=0` turns the passes off.
- **One conversation decodes at a time.** Several requests share the GPU in turns, so the total output speed with 8
  agents is about that of one (on my cards 66 tok/s for 4 agents with unrelated prompts, 98 tok/s for 8 agents that
  share a system prompt), and each agent gets its share.
- **Greedy text depends on more than the prompt.** Which experts sit in VRAM changes as the model runs, and the GPU and
  CPU paths round differently, so the same greedy request can give a different text after unrelated requests, with
  another amount of free VRAM (a desktop on a card), with another `--cpu-threads`, with another `--max-ctx` and when a
  prompt is fed in chunks (beside other requests, or after a shared system prompt). The last three come from the
  prefill's CPU expert split: `DSV4_NOCPUPF=1` removes them at a prefill cost. `--tier-reset` makes repeats of
  a request give the same text (see Settings).
- Editing an earlier message re-processes the prompt from that point (reuse works when the new prompt extends an old
  one or a kept system prompt).
- Quality is that of the Maya-S quantization (2- to 3-bit experts, Q8_0 dense weights, Q6_K Engram), not of the
  original checkpoint.
- Decode speed at long context (256-token replies, greedy, on my cards): 103 tok/s with 117K tokens of context and 91
  tok/s with 233K, against 76-106 tok/s for three prompts at short context.

### GLM-5.3-Flash (preview)

Z.ai's GLM-5.3-Flash: 45 layers, 288 routed experts per layer (8 active per token) plus a shared expert, attention
layers with a sparse indexer for long prompts next to KDA linear-attention layers, and one MTP layer. QEngine runs it
on three 24 GB cards plus host RAM, with its own engine (`src/glm`): the experts used most often sit in VRAM, the full
set in pinned host RAM, and the rest of a step's experts run on the CPU next to the cards. It is a preview in 1.5: it
runs in the same server and API as the other models, with the limits listed below.

**Model files.** My INT4 quant of GLM-5.3-Flash,
[bpx03/GLM-5.3-Flash-INT4-QEngine](https://huggingface.co/bpx03/GLM-5.3-Flash-INT4-QEngine)
(routed experts and KDA layers in INT4; lossy, see the limits). **The GLM engine runs only from this checkpoint**: it
holds my GPTQ INT4 experts and KDA layers in QEngine's own layout, so other GLM-5.3-Flash quants, GGUF files and the
original weights do not load. About 186 GB:

    hf download bpx03/GLM-5.3-Flash-INT4-QEngine --local-dir models/GLM-5.3-Flash-INT4-QEngine
    server/run.sh 8080 --model models/GLM-5.3-Flash-INT4-QEngine

The server recognises the model from `config.json` (`model_type` `glm5_next`) and loads the GLM engine
(`build/libqglm.so`, built by the normal CMake build when `src/glm` is in the tree; the Docker image has it). The MTP
draft vocabulary and the expert prior (`tools/glm/draft_vocab_49k.i32`, `tools/glm/expert_prior_gen.f32`) are read
from next to the library (`<root>/build/libqglm.so` -> `<root>/tools/glm/`); without them the engine still runs, with
the full drafter head and an empty expert cache at start (a start-up line says so). The chat template is the model's
own `chat_template.jinja`. Loading takes about 60 s with the files in the page cache.

**What it needs**

- **Three NVIDIA cards with 24 GB each** (tuned and tested on RTX 3090s). Two cards also work, with fewer expert slots
  per card (slower decode). With four or more cards the engine uses the first three.
- **GPU P2P is optional.** Without it (the stock GeForce driver) the all-reduces go through host memory. A start-up
  line says which path runs; `GLM_P2P=0` forces the host path.
- **About 192 GB of host RAM**: the experts (about 157 GB) stay pinned in host RAM, plus the conversation archive
  (below, up to 32 GB by default). Less RAM means a smaller archive; the experts themselves have to fit.
- **An x86-64 CPU with AVX2.** The CPU expert lane is built twice and picks its kernels at start: AVX-512 when the
  CPU has the full Zen 4 set (with VNNI and BF16: Zen 4, Sapphire Rapids and later), else AVX2 (`GLM_CPU_ISA`
  forces one). The lane's thread placement is derived from the CPU topology at start (one log line).
- Linux and an NVIDIA driver with CUDA 13.1 support, as for the other models.

**What works**

- The same server and API as the other models: OpenAI `POST /v1/chat/completions` (streaming or not), Anthropic
  `POST /v1/messages` and `count_tokens`, `GET /v1/models`, `GET /health`.
- **Tool calls** in the GLM format (`<tool_call>` with `<arg_key>` / `<arg_value>`), returned in the OpenAI and
  Anthropic formats; `tool_choice` `auto`, `none`, `required` and a named tool; **structured output**
  (`response_format` `json_schema` / `json_object`).
- **Reasoning** on or off (`enable_thinking`, Anthropic thinking), `reasoning_effort` as the model's template takes it
  (`low`, `high`, `max`); the thinking budget (`--thinking-budget`, a request's budget) closes the reasoning at its
  count.
- **logprobs** / `top_logprobs`, **stop strings** (`stop`) with an exact rollback of the tokens past the match.
- **Prompt cache**: a follow-up turn reuses the prefix it shares with earlier turns; idle conversations go to a
  conversation archive in pinned host RAM and come back with a copy instead of a new prefill.
- **MTP speculative decoding** with the model's own MTP layer.
- **Several conversations at once** (8 by default, `GLM_CONVS`): replies take turns on the GPUs. A switch parks the
  running reply between two decode steps (its state, and its expert cache contents, saved to host RAM) and resumes the
  other one exactly where it stopped, so each reply is bit-identical to the same reply served alone. A new prompt starts
  once the running reply has had its turn (`GLM_PREEMPT_MS`, by default the slice length), so short replies end
  without a switch; long replies are sliced (`GLM_SLICE_MS` 2000, at least 8x the measured cost of a switch: a park,
  ~0.06 s, plus the later resume, ~0.3-0.6 s, so about 4-5 s per turn). With 8 agents (agent replay: 2-16K-token
  prompts, 64-token replies) the first token comes in 13.2 s p50 instead of 28.3 s one at a time, and the total output
  is 22.4 instead of 12.6 tok/s; 4 clients with 256-token replies get the same total output as one at a time (70.5 vs
  70.7 tok/s); one conversation alone runs as before.
- **Long prompts return between layers**: the prefill runs in host slices of about one second, so the server keeps
  reporting progress; a cancel (or a client that disconnects) stops the prompt at the next layer, within about half a
  second, and the cache goes back exactly to the start of the interrupted prefill window.

**Known limits (preview)**

- **One reply decodes at a time**: several conversations share the GPUs in turns (see above), not in one batch, so the
  total output speed does not grow with the number of conversations; a switch between two long replies costs ~0.3 s
  (the expert cache contents of the reply that resumes are copied back).
- Parked replies and the snapshots of up to 3 x `GLM_CONVS` conversations use pinned host RAM (about 150 MB each, plus
  the archived attention rows); under host-RAM pressure a parked reply whose rows were given back is prefilled again
  (logged; that reply is then no longer bit-identical to a run alone).
- Greedy output is deterministic for the same request on the same machine and settings, but it depends on the number
  of expert slots (free VRAM, the context setting, the number of cards) and on how the prompt was split across
  prefill windows: a prompt resumed from the cache can differ in the last bits from one prefilled at once.
- Constrained replies (structured output, forced tool calls) and logprobs are slower: each step reads the full logits
  on the host.
- The default checkpoint is a lossy INT4 quant (routed experts and KDA layers).
- Text only (no image input), no presence / frequency penalties (accepted and ignored), no activation steering, no disk
  cache, no smaller K/V formats.

### gpt-oss-120B (preview)

OpenAI's gpt-oss-120B: 36 layers, 128 experts per layer (4 active per token), MXFP4 expert weights, grouped attention
with every second layer on a 128-token window, and the harmony chat format. QEngine runs it on three 24 GB cards, all of
it in VRAM, with its own engine (`src/gptoss`). It is a preview in 1.5: it runs in the same server and API as the other
models, with the limits listed below.

**Model files.** The official checkpoint as OpenAI publishes it, read as it is: the MXFP4 experts and the bf16 dense
weights, nothing converted, nothing of mine to download. I tested revision `b5c939de`; about 65 GB without the
`original/` and `metal/` folders:

    hf download openai/gpt-oss-120b --revision b5c939de --exclude "original/*" "metal/*" \
      --local-dir models/gpt-oss-120b
    server/run.sh 8080 --model models/gpt-oss-120b

The server recognises the model from `config.json` (`model_type` `gpt_oss`) and loads the gpt-oss engine
(`build_gptoss/libqgptoss.so`, built by `src/gptoss/build.sh`; the Docker image has it). Without that library the
start stops and says how to build it. The chat template is the model's own `chat_template.jinja`. The server is ready
about 11 s after start with the files in the page cache.

**What it needs**

- **Three NVIDIA cards with 24 GB each, compute capability 8.6** (RTX 3090 / 3090 Ti). The engine is built for sm_86
  only. RTX 4000 cards (8.9) run the same code untested, with the output head computed in full: its fast two-stage form
  has a rounding margin I measured on 3090s only, so a start-up line says the full head is used (slower decode: about 6 % for one conversation on my 3090s).
  Other cards (A100 8.0, RTX 5000 12.0, ...) are refused at start in 1.5. Two or four cards are accepted but not tested (two
  24 GB cards cannot hold the 65 GB of weights: the start stops with what each card would need); one card is refused.
- **GPU P2P between the cards is not needed.** With it the cards write into each other's memory. Without it (the
  stock GeForce driver) they exchange through pinned host memory, with the same output bit for bit: on my cards the
  host path reaches about 94 % of the P2P speed (2026-11-19, engine tool: decode 314 against 332 tok/s for one
  conversation, 951 against 1,009 tok/s for eight, a 10K-token prompt at 13.1K against 13.8K tok/s). A start-up line
  says which path runs; `GPTOSS_COMM=host` forces the host path. The host path takes the same VRAM as the P2P path and
  about 0.5 GB of pinned host RAM; `GPTOSS_PF_HOSTLANES=0` with `GPTOSS_LM=full` is the older, slower host path with
  about 0.5 GB more K/V room per card. When the host cannot pin that memory at start, the engine falls back by
  itself (the one-lane host form, a smaller prefill chunk, pageable row copies; one WARNING line each, slower prefill)
  and keeps serving.
- **Host RAM** only for the conversation archive (below); the model itself stays in VRAM.
- Linux and an NVIDIA driver with CUDA 13.1 support, as for the other models.

**What works**

- The same server and API as the other models: OpenAI `POST /v1/chat/completions` (streaming or not), Anthropic
  `POST /v1/messages` and `count_tokens`, `GET /v1/models`, `GET /health`.
- **Reasoning** always runs (the model has no off switch). `reasoning_effort` `low` / `medium` (default) / `high`;
  other APIs' names are mapped: `max` and `xhigh` to `high`, `minimal` and `none` to `low`, thinking off
  (`enable_thinking: false`) to `low`. The reasoning comes back in `reasoning_content` (OpenAI) or thinking blocks
  (Anthropic); the thinking budget (`--thinking-budget`, a request's budget) closes it at its count.
- **Tool calls** (the harmony `functions` namespace) in the OpenAI and Anthropic formats, `tool_choice` (`auto`,
  `none`, `required`, a named tool) and **structured output** (`response_format` `json_object` / `json_schema`). A
  history with several tool calls in one assistant turn (from another model) is rendered as one call and its result
  after the other, as harmony expects; several system / developer messages at the start are joined into one.
- **Several conversations at once**: 8 slots when the context per conversation is at least 32,768 tokens (the default
  131,072), else 4 (`GPTOSS_SLOTS`); they share one K/V pool (3x24 GB: 144,611 rows in bf16). Greedy and plain-temperature replies decode together in one step, and a reply's tokens are
  the same as when it runs alone. A reply that cannot grow because the pool is full ends with `finish_reason`
  `length`; a new prompt waits until the running replies have room to grow.
- **Prompt cache**: a follow-up turn reuses its conversation's K/V; a shared system prompt (tools included) is kept
  once for all conversations that start with it; idle conversations move to host RAM (`QE_KV_ARCHIVE_GB`, default
  128 GiB, never closer than `QE_KV_ARCHIVE_MARGIN_GB` = 8 GiB to `MemAvailable`; least recently used out first) and
  come back with a copy. `cache_prompt: false` forces a full prefill.
- **Lookup drafts** for greedy replies (`GPTOSS_LOOKUP`): tokens that repeat earlier text (edits, code) are checked
  in one multi-row step; the text is exactly the plain greedy text.
- **Sampling**: `temperature` (default 1.0, OpenAI's recommendation), `top_p` (default 1.0), `top_k`, `min_p`, `seed`.
  Plain temperature sampling decodes at greedy speed; requests with `top_p` < 1, `top_k` or `min_p` run the full
  output head one row per step (slower: about 6 % for one conversation on my cards, more with several at once).
- **Presence / frequency penalties** (`presence_penalty`, `frequency_penalty`, OpenAI's definition: a token's logit
  drops by `frequency_penalty` times its count in the reply so far, plus `presence_penalty` once it has appeared;
  before the temperature), per conversation, on the GPU and at the plain decode speed, also for several conversations
  at once. A greedy request with a penalty takes the highest penalised logit. A reply with a penalty runs without
  lookup drafts.
- **Stop strings** (`stop`), matched in the final answer only, never in the reasoning.
- **A device fault ends the process** (exit code 75) after the open requests get an error, so llama-swap or Docker
  restarts it instead of a server that answers `/health` and fails every request.

**Known limits (preview)**

- Text only: an image part is answered with `[image omitted: this server runs without vision]` in its place. No
  logprobs (HTTP 400). No activation
  steering, no disk cache (`--disk-cache` is ignored with a start-up line).
- One tool call per reply (the model's format); the built-in `browser` and `python` tools are not run by the server.
- Constrained replies (structured output, `tool_choice` `required` / named / `none`) decode one row per step.
- The DFlash drafter is not used by the server in 1.5 (`GPTOSS_DFLASH` is ignored with a start-up line).
- A greedy or seeded reply in a reused conversation can differ from the same prompt sent fresh where two tokens are
  nearly tied: rows computed by decode and by prefill differ in rounding. The same holds for a conversation that
  shares its beginning with another one the server still holds (the same system prompt, or just the harmony header):
  the shared rows are reused, so the rest of the prompt is computed in a call of another size, which rounds
  differently. The text is equally valid either way; requests that start from the same server state give the same
  reply.
- Context per conversation: 131,072 tokens (the model's own limit, `--max-ctx`); the pool is shared by all slots.

## Feature matrix

The five engines don't all do the same things. This table is what each one supports today (✅ yes, 🟡 partly, ❌ no).

| feature | Qwen3.8-27B | Qwen3.8-Flash-Next | DeepSeek-V4.1-Flash | GLM-5.3-Flash | gpt-oss-120B |
|---|---|---|---|---|---|
| Tool calls, streaming, OpenAI + Anthropic APIs | ✅ | ✅ | ✅ | ✅ | ✅ |
| Structured output (`response_format`) | ✅ | ✅ | ✅ | ✅ | ✅ |
| `tool_choice` required / named / none | ✅ | ✅ | ✅ | ✅ | ✅ |
| `logprobs` | ✅ | ✅ | ❌ HTTP 400 | ✅ | ❌ HTTP 400 |
| Presence / frequency penalty | ✅ | ✅ | ❌ ignored | ❌ ignored | ✅ |
| Thinking budget | ✅ | ✅ | ✅ | ✅ | ✅ |
| Thinking off | ✅ | ✅ | ✅ | ✅ | 🟡 always reasons (effort low) |
| Images (`--vision 1`) | ✅ | ✅ | ❌ | ❌ | ❌ |
| Activation steering | ✅ | ✅ | ❌ | ❌ | ❌ |
| Prefix cache, shared system prompt | ✅ | ✅ | ✅ | ✅ | ✅ |
| Idle conversations in host RAM | ✅ | ✅ | ✅ | ✅ (8 at once, one decodes at a time) | ✅ |
| Disk cache (`--disk-cache`) | ✅ | ✅ | ❌ | ❌ | ❌ |
| KV cache in host RAM (`FLASH_KV=ram`) | ❌ | ✅ | ❌ | ❌ | ❌ |
| Smaller K/V formats (opt-in) | ✅ 4-bit | ✅ 4-bit | ❌ | ❌ | ✅ FP8, 12-bit K |
| Max context (default) | 256K, 1M with YaRN | 256K, 1M with YaRN + KV in RAM | 256K | 256K | 128K |
| Parked replies beyond the seats (`--park`) | ✅ | ✅ (3+ cards) | ❌ | ❌ | ❌ |
| Drafts | MTP, DFlash2, lookup | MTP, n-gram, lookup | DSpark | MTP | prompt lookup |
| Sparse attention for long prompts | ✅ LSA (opt-in) | built in | built in | built in | ❌ |
| Cards | 1-4 | 2-4 TP, more in PP | 3 | 3 (2 with fewer expert slots) | 3 (2-4 accepted, untested) |
| Without GPU P2P | ✅ | ✅ | ✅ | ✅ | ✅ |
| Docker image | ✅ | ✅ | ✅ | ✅ | ✅ |

`n > 1`, `logit_bias` and `parallel_tool_calls: false` are ignored on every model.

At start the server logs one `[settings]` line for every flag or environment variable that is set but does nothing for
the loaded model, e.g. `FLASH_KV=ram is set but has no effect for gpt-oss-120B (KV stays in VRAM ...)`. A request
parameter the model doesn't support gets one `[api]` line the first time it shows up; the request is then served as
the table says (ignored, or HTTP 400).

## API

- **OpenAI**: `POST /v1/chat/completions` (streaming or not), `GET /v1/models`.
- **Anthropic**: `POST /v1/messages`, `POST /v1/messages/count_tokens`.
- `GET /health`, `GET /props` (llama.cpp style), `GET /v1/steering`.

`/v1/models` and `/props` report what a client needs to size its requests: `max_model_len` (prompt + reply tokens of
one conversation), `max_num_seqs` (conversations served at once), `max_prompt_tokens`, `max_output_tokens` (`null`:
no cap beyond the context), `kv_pool_tokens`, `kv_cache` (`vram` / `ram`) and `input_modalities`; `/props` adds
`total_slots` and `default_generation_settings.n_ctx`.

**Too-long prompts** get HTTP 400 before any streaming starts. The Anthropic path says
`prompt is too long: N tokens > M maximum` (Claude Code compacts the conversation on it). The OpenAI path uses
OpenAI's wording, `This model's maximum context length is M tokens. However, your messages resulted in N tokens ...`
with code `context_length_exceeded`, which harnesses such as verifiers / AutomationBench and LiteLLM recognise as a
context overflow.

**Tool calls**: OpenAI `tools` and Anthropic `tool_use` / `tool_result`. Tools are rendered sorted by name with
sorted JSON keys, so a client that reorders the same tools keeps the prompt cache (`--sort-tools 0`: the client's
order). The chat template is `server/templates/qwen38_syssafe.jinja` (the model's template, accepting several leading
system messages). `--template` replaces it. A reply starts as reasoning only if the template's generation prompt opens
`<think>`: with a custom template that does not, a model reasoning without writing the tag shows that text in `content`,
followed by a literal `</think>`. Since 1.3.6 a `<tool_call>` that does not parse as a call (prose inside the tag,
broken markup), or a call that `tool_choice` filters out, reaches the client as plain text in `content`, streamed or
not, on both APIs, instead of an empty reply.

**`tool_choice`** on both APIs: `auto` (default), `none` (Anthropic `{"type": "none"}`: the tools stay in the prompt, the
tool-call token is masked, so the model answers in text), `required` (Anthropic `any`) and a named function (OpenAI
`{"type": "function", "function": {"name": ...}}`, Anthropic `{"type": "tool", "name": ...}`): the answer starts with
that call after any thinking. Enforced in the engine: `none` bans the tool-call token in the 