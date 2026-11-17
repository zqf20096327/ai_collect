# inside-llm

[![Release](https://img.shields.io/github/v/release/manuelgscom/inside-llm?logo=github&color=blue)](https://github.com/manuelgscom/inside-llm/releases) [![License: MIT](https://img.shields.io/badge/license-MIT-blue)](https://github.com/manuelgscom/inside-llm/blob/main/LICENSE) [![llama.cpp](https://img.shields.io/badge/built%20with-llama.cpp-informational)](https://github.com/ggml-org/llama.cpp) [![Runs on: CUDA · Vulkan](https://img.shields.io/badge/runs%20on-CUDA%20%C2%B7%20Vulkan-informational)](#install) [![Platforms: Linux · Windows](https://img.shields.io/badge/platforms-Linux%20%C2%B7%20Windows-informational)](#install) [![Live demo](https://img.shields.io/badge/live%20demo-try%20it%20in%20your%20browser-brightgreen)](https://manuelgs.com/en/inside-llm/demo/)

**See inside any GGUF: where two quantizations part ways, token by token, and what each sampler cuts. Live, in your browser.**

https://github.com/user-attachments/assets/5f9492ba-0ba4-4f40-94b3-93503a099475

*`inside-llm` with Qwen3.5-4B at two quantizations, Q2_K and Q8_0: the token where their texts split, the candidates behind each pick, the sampler chain, branches and the relief of probabilities. Every number comes from the real engine running the two models.*

`inside-llm` loads one or two GGUF models with [llama.cpp](https://github.com/ggml-org/llama.cpp) and shows in the browser what the model does while it generates: the probability of each token, the alternatives it discarded, what each sampler removes and, with two models (two quantizations, or a base model and its fine-tune), the divergence at every position and the exact token where their texts split. It is a single native binary that serves its own web page. Everything runs on your machine: no accounts, no API keys, no telemetry. A session can be recorded and replayed later in a static page, with no engine and no GPU.

**[Try the live demo](https://manuelgs.com/en/inside-llm/demo/)**: recorded sessions replayed in your browser, nothing to install.

## What you see

![inside-llm comparing Qwen3.5-4B Q2_K (A) and Q8_0 (B): at position 31 A picks "six" and B "eight", and their texts split there](assets/inside-llm.png)

- **Stream:** the generated text, one column per model (A | B). Brightness is the probability the model gave to each token; a magenta mark shows where A and B would pick differently. Two modes: *Same text* (lockstep: both models read the text written by the driver) and *Each its own* (free: each model follows its own picks until the texts split).
- **Candidates:** the decision behind the selected token. Mirrored bars for A and B on each candidate, entropy, effective number of options, Jensen-Shannon divergence and KL in both directions. **Compare** puts the two distributions side by side.
- **Gates:** the sampler chain of that decision (penalties, top-k, top-p, min-p, temperature and a GBNF grammar), with how many candidates survive each stage. Click a stage to see the distribution after it. The chain, its order and the seed are set in the **Samplers** panel.
- **Metrics:** confidence, surprise, perplexity, margin, speed and latency of A and B, as sparklines along the text.
- **Timeline:** entropy of A and B and their divergence along the text, with the tree of branches. Sweep it with the mouse and every panel follows.
- **Relief 3D and Layers:** a surface whose height is a probability: the candidates at each position or, with `--lens`, what each layer would predict (logit lens), also as a 2D map.
- **Branching:** click a candidate and generation continues from there. Nothing is lost: every branch stays in the tree and can be viewed or resumed, and the engine returns to any node exactly.
- **Models:** pick model A and model B from the models folder, or search Hugging Face and download GGUF files, without restarting. The picker only offers B models that share A's tokenizer and warns when the pair will not fit in GPU memory.

![Relief 3D: the candidates of every position as a surface; cyan is model A, amber model B, magenta where their picks differ](assets/relief.png)

Both models must share the same tokenizer: two quantizations of a model, a base model and its fine-tune, or two sizes of one family that keep the tokenizer (every Qwen3.5 size, for instance). Without model B, everything except the comparison works.

## Install

Download the package for your system from the [latest release](https://github.com/manuelgscom/inside-llm/releases/latest). Each one is self-contained: nothing else to install besides the GPU driver.

| Package | For | Needs on the machine |
|---|---|---|
| `inside-llm-v1.0.0-linux-cuda.tar.gz` | Linux + NVIDIA | glibc 2.35 or newer, NVIDIA driver |
| `inside-llm-v1.0.0-linux-vulkan.tar.gz` | Linux + any dedicated GPU (AMD, Intel Arc, NVIDIA) | glibc 2.35 or newer, the GPU's Vulkan driver and `libvulkan1` (present on any desktop) |
| `inside-llm-v1.0.0-windows-cuda.zip` | Windows + NVIDIA | a recent NVIDIA driver |
| `inside-llm-v1.0.0-windows-vulkan.zip` | Windows + any dedicated GPU | the GPU driver |

glibc 2.35 or newer means Ubuntu 22.04, Debian 12, Fedora 36, Linux Mint 21 or later. The CUDA packages carry the CUDA runtime and cuBLAS, so no CUDA toolkit is needed.

**Linux** (here with Vulkan; the CUDA package works the same way):

```sh
curl -LO https://github.com/manuelgscom/inside-llm/releases/latest/download/inside-llm-v1.0.0-linux-vulkan.tar.gz
tar -xzf inside-llm-v1.0.0-linux-vulkan.tar.gz
./inside-llm-v1.0.0-linux-vulkan/inside-llm
```

The browser opens by itself (if not, go to http://localhost:8642) with the model picker. To load two models straight away: `inside-llm -a A.gguf -b B.gguf`.

**Windows:** unzip `inside-llm-v1.0.0-windows-cuda.zip` (or `-vulkan`) and double-click `inside-llm.exe`. The browser opens by itself with the model picker. From a terminal, `inside-llm.exe -a A.gguf -b B.gguf` loads two models straight away.

Models live in the `models` folder of the directory you start the engine from (created if missing; `--models-dir` picks another). Files downloaded from Hugging Face land there too.

At startup the engine prints the GPU it uses, or a warning if it found none. Integrated GPUs are never used: without a dedicated GPU the models run on the CPU, much slower.

**Checking a download:** each release has a `SHA256SUMS` file. In the folder with the downloads:

```sh
curl -LO https://github.com/manuelgscom/inside-llm/releases/latest/download/SHA256SUMS
sha256sum -c --ignore-missing SHA256SUMS
```

## Try it without installing

**Live demo: [manuelgs.com/inside-llm/demo/](https://manuelgs.com/en/inside-llm/demo/)**. Recorded sessions play back in a static build of the same web page: no engine, no models, no GPU. Pick a session in the gallery and press **Replay**: selection, sweeping, the recorded branches, gates and the relief all work; anything that would send a command to the engine is disabled.

To serve the same page yourself, from a clone of this repository (see [Build from source](#build-from-source)), with Docker:

```sh
make image               # toolchain images (once)
make web-static          # builds the static web with the recorded sessions
make web-static-serve    # serves it on http://localhost:4173 (STATIC_PORT=… to change)
```

Without parameters the page shows a gallery of the recorded sessions in `sessions/samples/` (listed in `sessions/index.json`). `?session=<url of an .ils file>` opens one directly. A live session can be downloaded from the bar (**Session**) and replayed the same way.

## Command-line options

```
inside-llm [-a <a.gguf> [-b <b.gguf>]] [options]
```

Without `-a` the engine starts with no model and the browser opens the model picker.

| Option | Meaning |
|---|---|
| `-a FILE` | Model A (GGUF), loaded at startup; any path |
| `-b FILE` | Model B (GGUF), to compare with A; same tokenizer |
| `--models-dir DIR` | Folder the browser picks models from and downloads into (default `models`) |
| `--ctx N` | Context size of each model (default 4096) |
| `--gpu-layers-a N`, `--gpu-layers-b N` | Layers of A / B on the GPU (default: all) |
| `--snapshot-mem MIB` | MiB of state snapshots each model may keep in RAM, used to jump back to a node exactly (default 3072) |
| `--lens` | Logit lens: what each layer would predict, projected on the CPU (about 2 GB of RAM per model and some 30 ms per step) |
| `--lens-layers LIST` | Layers of the lens, from 0, like `0,6,12,23` (at most 16; implies `--lens`; default: 8 spread evenly, the last one included) |
| `--host ADDR` | Listen address (default 127.0.0.1) |
| `--port N` | Port (default 8642; 0 picks a free one) |
| `--no-browser` | Do not open the browser at startup |
| `--allow-origin URL` | Extra origin accepted on the WebSocket (repeatable) |
| `--help` | Show the help |

The engine listens on `127.0.0.1` only unless you pass `--host`.

## Models

Any GGUF of a text-generating model that llama.cpp loads (Llama, Qwen, Gemma, Mistral, Phi, DeepSeek, MoE models…), at any quantization, as long as it fits in GPU memory. Multimodal models work on text only. Not supported: embedding-only models and GGUF files split in several parts. Some pairs to start with (also offered as suggestions in the picker):

| Use | Model A | Model B |
|---|---|---|
| Demo | `Qwen_Qwen3.5-4B-Q2_K.gguf` (bartowski, 2.2 GB) | `Qwen_Qwen3.5-4B-Q8_0.gguf` (bartowski, 4.6 GB) |
| Smaller | `Qwen3.5-2B-UD-Q2_K_XL.gguf` (unsloth, 1.0 GB) | `Qwen3.5-2B-Q8_0.gguf` (unsloth, 2.0 GB) |
| Smallest | `Qwen3.5-0.8B-Q4_K_M.gguf` (unsloth) | `Qwen3.5-0.8B-Q8_0.gguf` (unsloth) |

**From Hugging Face:** the **Hugging Face** tab of the model picker searches public GGUF repositories; tick two quantizations of one repository and **Download & compare** downloads both into the models folder and loads them as A and B. Downloads resume after a cancel. For gated repositories set `HF_TOKEN` in the engine's environment; `HF_ENDPOINT` points at a mirror.

## How it works

```
 ┌──────────────────────── inside-llm (one process) ─────────────────────────┐
 │                                                                           │
 │  model A ──┐                                                              │
 │ (llama.cpp)│   logits ─► sampler chain ─► pick ─► tree of tokens          │
 │  model B ──┘   (per step,  (penalties, top-k,        (branches, cursors, │
 │ (llama.cpp)     A and B)    top-p, min-p, temp,       state snapshots)    │
 │                             grammar), traced                              │
 │                                   │                                       │
 │                       binary frames over a WebSocket                      │
 └───────────────────────────────────┼───────────────────────────────────────┘
                                     ▼
              browser: Svelte 5 + Canvas 2D (+ three.js for the relief)
              ──► the same frames, saved to disk, are a recorded session
```

- **Engine (C++17):** links llama.cpp directly. For every step it reads the full distribution of A (and of B on the same context), computes entropy, divergence and the sampler chain stage by stage, and draws the token with its own seeded sampler. Each model keeps snapshots of its state so that jumping to another node of the tree is exact, not re-generated.
- **Protocol:** compact binary frames for each step plus JSON commands from the browser. A recorded session (`.ils`) is the same stream of frames, compressed.
- **Web:** Svelte 5 for the panels; the per-step data skips reactivity and is painted on canvases by one `requestAnimationFrame` loop. The relief is three.js, loaded only when opened. The page is embedded in the binary.

## Build from source

Everything builds and runs in Docker; nothing is installed on the host. Running on the GPU needs an NVIDIA GPU and the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) (`BACKEND=vulkan` builds and runs with Vulkan instead).

```sh
git clone --recursive https://github.com/manuelgscom/inside-llm.git
cd inside-llm
make image          # toolchain images (once)
make build          # the web and the binary
make test-unit      # engine and web tests: no GPU, no model
make models         # download the GGUF pairs above into models/ (optional)
make run            # then open http://localhost:8642 and pick the models
make run A=Qwen_Qwen3.5-4B-Q2_K.gguf B=Qwen_Qwen3.5-4B-Q8_0.gguf   # or load two of models/ at startup
```

`--recursive` also fetches llama.cpp, which is a git submodule. `make run` takes extra options with `ARGS="--lens --ctx 8192"`. `make test-gpu` runs the integration tests on the GPU with a real model, and `make run-fake` starts the engine with a scripted fake model (no GGUF, no GPU) for working on the web. The CUDA kernels are built for one architecture (`CUDA_ARCH`, default `120-real`; e.g. `make build CUDA_ARCH=89-real` for an RTX 40).

**Packages:** `make dist-linux-cuda` and `make dist-linux-vulkan` build the portable Linux binaries on Ubuntu 22.04 (in Docker) and pack them with the libraries they need in `dist/`. The Windows zips are built natively with MSVC: `packaging/windows/setup-tools.ps1` installs the toolchain once and `packaging/windows/build.ps1` builds both variants. `make dist-sums` writes `dist/SHA256SUMS`.

### Repository layout

```
CMakeLists.txt, Makefile   build (everything through Docker)
engine/
  src/        the engine: llama.cpp models, sampler chain, metrics, logit lens, tree and
              snapshots, session coordinator, binary frames, HTTP/WebSocket server,
              model catalog and Hugging Face downloads
  tests/      unit tests, golden sessions, a fake engine, GPU integration tests
web/
  src/        Svelte 5 app: panels, canvas renderers, store, frame decoder, e2e tests
  scripts/    static build of the recorded sessions, screenshots
sessions/     golden/ (the protocol contract, synthetic) and samples/ (recorded sessions)
docker/       toolchain images
packaging/    Linux (Ubuntu 22.04) and Windows (MSVC) packages
third_party/  llama.cpp (submodule)
```

## Limitations

- Model A and model B must share the tokenizer.
- Both models must fit in GPU memory at once; the picker estimates it before loading.
- One GPU at a time. Integrated GPUs are never used; without a dedicated GPU it runs on the CPU, much slower.
- Text only: multimodal models load, but only their text side is shown.
- The engine is meant for your own machine: it listens on localhost and has no authentication.

## License

The code is under the [MIT](LICENSE) license. The packages also contain llama.cpp/ggml, cpp-httplib, nlohmann/json, zlib, LibreSSL, Svelte, three.js, the Inter and JetBrains Mono fonts and, depending on the package, the NVIDIA CUDA runtime and cuBLAS, the Microsoft Visual C++ runtime or the GCC OpenMP runtime; their licenses and notices are in [THIRD_PARTY_NOTICES](THIRD_PARTY_NOTICES).

inside-llm is an independent project, not affiliated with or endorsed by the authors of llama.cpp, Qwen or any model it loads.

---

Author: [Manuel García](https://manuelgs.com)
