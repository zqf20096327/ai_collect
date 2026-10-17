# gxtop

**A digital-rain style `htop`/`nvtop` for NVIDIA GB10 machines** – ASUS Ascent GX10, NVIDIA DGX Spark and
other Grace Blackwell desktops. It shows the system at a glance and answers the question
nvtop can't: *which AI models are loaded right now, and which tool loaded them?*

![gxtop running on an ASUS Ascent GX10 with vLLM, ComfyUI and Ollama](docs/screenshot.png)

<sub>Real capture from a GX10 (200×56 terminal). The hostname, IP address, user name and one container name were replaced with placeholders.</sub>

- **Single Python file, zero dependencies.** It only uses the standard library and `curses`.
- **Unified-memory aware.** On GB10, `nvidia-smi` reports *"Not Supported"* for GPU memory. gxtop adds up the per-process GPU allocations and splits the shared CPU+GPU memory by engine.
- **Model & engine detection** for vLLM, Ollama, ComfyUI, llama.cpp, SGLang, TGI and TensorRT-LLM. Each engine is mapped to its Docker container or systemd service.
- **Live digital rain.** Density and speed follow GPU load and vLLM token throughput.

Example: the *Loaded models* panel.

```
╭─┤ LOADED MODELS · ENGINES ├──────────────────────────────────────────────────────────────────────┤ 3 active ├╮
│  ● vLLM      qwen3.6-35b                          GPU   47.7G  idle     docker vllm-main :8000 pid 151891    │
│    └ nvidia/Qwen3.6-35B-A3B-NVFP4 · ctx 131072 · kv fp8 · mem 0.4 · tp 1                                     │
│      ⚡  42.3 tok/s  ▁▂▅▇█▇▅▃  prefill 812 t/s  ▶ 2  ◌ 0  KV  3.1%  prefix-hit 77%  Σ 166.7k tok            │
│  ◉ ComfyUI   queue ▶ 1  ◌ 0                       GPU   36.8G  BUSY     systemd comfyui :8188 pid 1106632    │
│    ├ diffusion qwen_image_2.1_int8_convrot  6.8G                                                             │
│    ├ text-enc  qwen3vl_8b_int8_convrot  8.7G                                                                 │
│    └ vae       qwen_image_2.1_vae_bf16  644.2M                                                               │
│  ● Ollama    1 loaded · 2 installed               GPU  881.0M  idle     docker ollama :11434 pid 163390      │
│    └ embeddinggemma:latest  307.58M BF16  649.8M (100% GPU)  ctx 2048  unloads in 4m12s                      │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Panels

| Panel | Shows |
|---|---|
| **GPU** | utilization with history graph, allocated GPU memory, temperature, power (incl. max seen), clocks, P-state, throttle reasons |
| **Unified memory** | one bar split by engine (vLLM / ComfyUI / Ollama / …), system, cache and free memory, plus swap and memory pressure (PSI) |
| **CPU** | per-core load and frequency, with performance (P) and efficiency (E) cores marked |
| **System** | SoC / GPU / NVMe temperatures, network and disk throughput, root filesystem usage |
| **Loaded models** | each engine with its models, origin (Docker container, systemd service or process owner), port, PID and live metrics |
| **GPU processes** | an nvtop-style process list with GPU memory, CPU %, RSS, engine and container/service |
| **Events** | live log of loaded/unloaded models, finished generations (tokens, tok/s), finished ComfyUI workflows, downloads, throttling and **OOM-killer events** |

### What gets detected

| Engine | Detected via | Details shown |
|---|---|---|
| vLLM | `vllm serve` process + `/metrics` (no API key needed) | served name, model, context, KV dtype, tok/s, prefill t/s, running/waiting requests, KV-cache usage, prefix-cache hit rate |
| Ollama | `ollama serve` process + `/api/ps`, `/api/tags` | loaded models, size, quantization, GPU share, context, time until unload |
| ComfyUI | `main.py` process + `/queue` + model files the process has open | checkpoints by category (diffusion, text encoder, VAE, LoRA, …), queue, in-progress downloads (`.part` files) |
| llama.cpp | `llama-server` process + `/health`, `/slots` | model file, context, busy slots |
| SGLang, TGI, TensorRT-LLM | launcher process + health endpoint | model |
| anything else on the GPU | `nvidia-smi` compute apps | command line, open model files (if readable) |

Ollama's internal `llama-server` runners are counted towards Ollama, not shown as separate engines.

## Install

```bash
mkdir -p ~/.local/bin
curl -fsSL https://raw.githubusercontent.com/medpex/gxtop/main/gxtop.py -o ~/.local/bin/gxtop
chmod +x ~/.local/bin/gxtop
gxtop
```

Or clone it:

```bash
git clone https://github.com/medpex/gxtop.git
ln -s "$PWD/gxtop/gxtop.py" ~/.local/bin/gxtop
```

Make sure `~/.local/bin` is in your `PATH`.

### Requirements

- Linux with an NVIDIA GPU and `nvidia-smi`. gxtop is built for GB10, but the generic parts also run on other NVIDIA systems.
- Python 3 with `curses`. It is tested with Python 3.12 on Ubuntu (aarch64).
- A terminal with UTF-8 and 256 colors. The minimum size is 80×24, and the logo header appears from 46 rows.
- Optional: access to the `docker` CLI so container names can be shown. Without it, gxtop shows container IDs.

## Usage

```
gxtop [-i INTERVAL] [--fps FPS] [--no-rain] [--no-intro] [--json]
```

| Key | Action |
|---|---|
| `q` / `Esc` | quit |
| `m` | toggle digital rain |
| `+` / `-` | change sample interval (0.5–10 s) |
| `f` | freeze values |
| `?` | help |

`gxtop --json` takes one sample and prints everything as JSON. This is handy for scripting or for debugging the detection.

### Permissions

gxtop runs fine as a normal user. Some details are only visible for your own processes, such as the model files a process has open. To list ComfyUI checkpoints, run gxtop as the same user as ComfyUI, or as root.

## Privacy

gxtop only reads local data: `/proc`, `/sys`, `nvidia-smi`, `docker ps` and the HTTP endpoints of model servers running **on the same machine**. It sends nothing anywhere, collects no telemetry and writes no files.

## License

[MIT](LICENSE)

## Disclaimer

gxtop is an independent hobby project. It is not affiliated with, endorsed by or sponsored by NVIDIA, ASUS or any of the projects it monitors. NVIDIA, DGX, Grace Blackwell, ASUS, Ascent, vLLM, Ollama, ComfyUI, llama.cpp, SGLang, TGI and TensorRT-LLM are trademarks or names of their respective owners and are used here only to describe compatibility.
