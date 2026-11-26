# Zorlo

**Run large Mixture-of-Experts language models on an ordinary PC: CPU only, from 4-8 GB of RAM.**

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
![Platform: Windows x64](https://img.shields.io/badge/platform-Windows%20x64-lightgrey)
![Language: C++17](https://img.shields.io/badge/language-C%2B%2B17-informational)

[Website](https://zorlo.stream) · [Download](https://github.com/shahihussainofficial1/zorlo/releases/latest) ·
[Models](https://huggingface.co/Haidershahi1) · [Technical report](https://doi.org/10.5281/zenodo.24136832) ·
[Design and benchmarks](docs/design.md) · [Usage](docs/usage.md)

A 30B model doesn't fit in 8 GB of RAM, but a Mixture-of-Experts model only uses a small part of
its weights for each token. Zorlo keeps the always-needed part (attention, norms, routers, output head) in
RAM and leaves the experts on the SSD. It reads only the experts each token is routed to, into a cache
sized to the RAM the machine has free right now.

The output is **identical to llama.cpp**, token for token and logit for logit on greedy decoding. The
lossy speed-ups are opt-in, and their quality cost is measured.

![Zorlo Desktop in Agent mode with Qwen3-30B-A3B: it wrote a one-page website with the user's approval and shows it in the Preview panel](docs/images/zorlo-agent.webp)

## Results

Qwen3-30B-A3B (Q4_K_M, 18.6 GB on disk) on a 4-core laptop (Intel i5-1135G7, 8 GB RAM, NVMe SSD), decode
speed against llama.cpp at the same commit reading the model with mmap:

| Run | Expert cache | Decode | Output |
|---|---|---|---|
| llama.cpp (mmap) | - | 1.43 tok/s | reference |
| Zorlo, exact | 256 MB | 2.98 tok/s | identical to llama.cpp |
| Zorlo, exact | 1.2 GB | **3.47 tok/s** (2.4x) | identical to llama.cpp |
| Zorlo, `--mode fast` | 256 MB | **5.47 tok/s** | 94.7% of greedy tokens unchanged |

The full measurements, including the cache simulations, the quality tables for every lossy switch, and
what was tried and dropped, are in [docs/design.md](docs/design.md).

## Features

- **Expert streaming from SSD:** parallel unbuffered reads at the queue depth the SSD needs, plus a
  next-layer prefetch predicted by the router (88% recall).
- **A live RAM budget:** the expert cache grows and shrinks as other programs use memory, and always
  leaves 512 MB for the OS.
- **Exact by default:** bit-identical to llama.cpp, checked on every change with a golden test set. It
  gives the same output on every x86 CPU, from AVX2 to AVX-512.
- **Speed modes:** `exact`, `balanced` (+12%) and `fast` (2.4x). Fast mode uses an adaptive expert count
  and an importance-weighted 2-bit copy of cold experts.
- **Exact speculative decoding:** drafts come from the text already in the context, with no draft model,
  and the output is unchanged.
- **Prompt KV saved to disk:** a long agent system prompt is computed once and reloads in under a second,
  also after a restart.
- **An OpenAI- and Anthropic-compatible server:** `zorlo serve` supports streaming, tool calls, reasoning
  output and several requests at once (`-np N`).
- **Zorlo Desktop:** a Windows app with a model picker, downloads from Hugging Face, chat, and a coding
  agent with permissions, MCP connectors, file previews and undo.

## Quick start

### Windows app

1. Download `zorlo-v0.1-windows-x64.zip` from [Releases](https://github.com/shahihussainofficial1/zorlo/releases/latest) and unzip it.
2. Run **Zorlo Desktop.exe**, pick a model, and wait for the download.
3. Chat, or switch to Agent mode and give it a project folder.

Requirements: Windows 10/11 x64, a CPU with AVX2, 8 GB RAM (works from 4 GB, slower), and an NVMe SSD.

### Command line

```
zorlo pull Haidershahi1/qwen3-30b-a3b-zorlo models\qwen3-30b-a3b
zorlo run models\qwen3-30b-a3b -p "Explain mixture-of-experts in two sentences." -n 256
zorlo serve models\qwen3-30b-a3b --port 8080
```

Then point any OpenAI client at `http://127.0.0.1:8080/v1`, or open `http://127.0.0.1:8080/` for the chat
and agent app. To convert a GGUF file yourself:

```
zorlo pack Qwen3-30B-A3B-Q4_K_M.gguf models\qwen3-30b-a3b
```

The server API, speed modes, agent tools and the model catalog are described in [docs/usage.md](docs/usage.md).

## Supported models

| Architecture | Tested model | Status |
|---|---|---|
| `qwen3moe` | Qwen3-30B-A3B | exact vs llama.cpp |

More MoE architectures are on the roadmap. Each one is
added only after its output matches llama.cpp on a golden test set.

## How it works

```
             RAM                                     SSD
 ┌──────────────────────────────┐     ┌────────────────────────────────┐
 │ core.gguf: attention, norms, │     │ experts.bin: every expert,     │
 │ routers, output head         │     │ aligned for unbuffered reads   │
 │                              │ ◄── │                                │
 │ expert cache: hot set + LRU, │     │ experts.lo.bin (optional):     │
 │ sized from free RAM          │     │ 2-bit copy for fast mode       │
 └──────────────────────────────┘     └────────────────────────────────┘
```

Each layer, the router picks the token's experts. Experts already in the cache are used at once, and the
missing ones are read in parallel while the next layer's experts are prefetched. Decode speed is then
`SSD bandwidth / (active expert bytes × cache miss rate)`, so very sparse models with many total parameters
are the best fit. The design and its measurements are in [docs/design.md](docs/design.md).

## Build from source

You need Visual Studio 2022 (the "Desktop development with C++" workload), CMake 3.24+ and Git.

```
git clone --recursive https://github.com/shahihussainofficial1/zorlo
cd zorlo
.\tools\get-webview2.ps1
cmake -S . -B build -DBUILD_SHARED_LIBS=ON -DGGML_BACKEND_DL=ON -DGGML_CPU_ALL_VARIANTS=ON
cmake --build build --config Release --parallel
```

CMake applies the two small patches in `patches/` to the llama.cpp submodule. They make float math follow
one order on every CPU, which is what keeps the output identical everywhere. Tests:

```
python -m unittest discover -s tests
zorlo golden models\qwen3-30b-a3b golden\qwen3-30b-a3b.jsonl
```

## Repository layout

| Path | What it is |
|---|---|
| `src/engine/` | the streaming MoE engine: pack loader, expert cache, forward pass |
| `src/pack/` | GGUF → Zorlo pack converter (`zorlo pack`) |
| `src/cli/` | `zorlo` CLI: `run`, `serve`, `pull`, `start`, `golden`, the agent backend |
| `src/desktop/` | Zorlo Desktop (WebView2) |
| `ui/` | the chat and agent web app |
| `tools/` | disk benchmark, cache simulator, routing-trace collector, golden generator, release packaging |
| `golden/` | reference outputs from llama.cpp used for exactness tests |
| `patches/` | llama.cpp patches applied at configure time |

## Contributing

Bug reports, benchmarks from other hardware, and new architectures are welcome. See
[CONTRIBUTING.md](CONTRIBUTING.md).

## License

Zorlo is licensed under the [Apache License 2.0](LICENSE). See [NOTICE](NOTICE) for third-party code.
Models keep their own licenses (Qwen3 is Apache 2.0).

## Citation

If you use Zorlo in research, please cite the technical report
([doi:10.5281/zenodo.24136832](https://doi.org/10.5281/zenodo.24136832)):

```bibtex
@techreport{shahi_zorlo_2026,
  author      = {Shahi, Haider Md. Faiyaz Hussain},
  title       = {Zorlo: Running Large Mixture-of-Experts Models on Low-RAM PCs
                 by Streaming Experts from the SSD},
  institution = {Zenodo},
  year        = {2026},
  month       = nov,
  doi         = {10.5281/zenodo.24136832},
  url         = {https://doi.org/10.5281/zenodo.24136832}
}
```

Built on [llama.cpp / ggml](https://github.com/ggml-org/llama.cpp).
