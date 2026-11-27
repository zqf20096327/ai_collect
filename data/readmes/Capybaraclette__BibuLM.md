<p align="center">
  <img src="assets/readme/logo.png" alt="BibuLM" width="128">
</p>

<h1 align="center">BibuLM</h1>

<h3 align="center">Full llama.cpp control. Native, fast, and open source.</h3>

<p align="center">
  A lightweight, native <b>Rust + WebView</b> (Tauri v2) desktop workbench and headless server for running, benchmarking, and serving local LLMs directly on upstream <code>llama.cpp</code>.
  <br><b>No black-box wrappers, no telemetry, no lock-in.</b>
</p>

<p align="center">
  <a href="https://github.com/Capybaraclette/Bibulm/releases"><img alt="Latest release" src="https://img.shields.io/github/v/release/Capybaraclette/Bibulm?color=2563EB&label=release"></a>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/github/license/Capybaraclette/Bibulm?color=2563EB"></a>
</p>

<p align="center">
  <a href="#quick-start"><b>Quick start</b></a> ·
  <a href="#a-closer-look">Screenshots</a> ·
  <a href="#features">Features</a> ·
  <a href="#bibulm-link-and-headless-cli">Link &amp; CLI</a> ·
  <a href="https://github.com/Capybaraclette/Bibulm/releases">Releases</a> ·
  <a href="#contributing">Contributing</a>
</p>

## Why BibuLM

Today, running local LLMs with a desktop interface forces an awkward trade-off: existing open-source tools are often incomplete — hiding or lagging behind real `llama.cpp` capabilities — while the more complete desktop options are closed source. BibuLM is built to give you both: complete, first-class control over `llama.cpp`, entirely in the open.

<table>
<tr>
<td width="50%" valign="top">

### Complete control, fully open source

No dumbed-down presets and no closed-source binary walls. BibuLM is MIT-licensed and exposes real `llama.cpp` parameters directly — from KV cache quantization and Flash Attention to custom tensor overrides and raw CLI flags.

### Direct upstream `llama.cpp`

Pull official `ggml-org/llama.cpp` releases directly inside the app — CUDA (with auto-matched CUDART DLLs), Vulkan, ROCm/HIP, SYCL, OpenVINO, or CPU — keep multiple versions side-by-side, or register your own compiled binary.

### Built for modern models

A pure-Rust GGUF v2/v3 inspector reads model metadata in milliseconds, estimates exact VRAM vs. RAM placement before loading, lets you disable vision (`mmproj`) whenever you don't need it to save VRAM, and exposes full thinking/reasoning controls.

</td>
<td width="50%" valign="top">

### Drop-in OpenAI &amp; Anthropic gateway

Serve your local and linked models on `http://127.0.0.1:1234` with OpenAI-compatible endpoints and Anthropic `/v1/messages` support for tools like Claude Code — complete with model alias routing, JIT loading, and idle auto-unload.

### Your devices, your own mesh

Use **BibuLM Link** to connect your laptop, desktop, and headless GPU servers over your personal Tailscale or Headscale network — zero third-party relays and no system VPN installation required.

### Native &amp; lightweight

Built with Rust and Tauri v2 instead of Electron, so your memory stays free for models and KV cache, with live VRAM/RAM spillover verification and built-in `llama-bench` matrices.

</td>
</tr>
</table>

## Quick start

1. **Install BibuLM** — Download the latest installer for your platform from [GitHub Releases](https://github.com/Capybaraclette/Bibulm/releases) (`.exe` / `.msi` on Windows, `.dmg` on macOS Apple Silicon, `.deb` / `.rpm` / `.AppImage` on Linux) and launch the app.

2. **Download a runtime** — Open **Runtime** (`Ctrl + Shift + R`) in the sidebar. BibuLM detects your hardware and highlights the recommended official `ggml-org/llama.cpp` build (CUDA + CUDART, Vulkan, ROCm/HIP, OpenVINO, or CPU). Click **Install** — it is automatically set as your active default runtime.

3. **Download a model** — Open **Model Search** in the sidebar to search HuggingFace GGUF repositories. Check the live VRAM fit verdict on each quantization, optionally attach a vision `mmproj`, and click **Download**. *(Already have local `.gguf` files? Add your folder in **Library**.)*

4. **Load your model** — Press `Ctrl + L` (or click **+ Load Model** in **Model Server**), review your context size, GPU offloading, vision toggle, or KV cache settings, and press `Ctrl + Enter` to load. Your model is immediately ready in **Benchmark / API Playground** and served at **`http://127.0.0.1:1234/v1`**.

<details>
<summary><b>Keyboard shortcuts</b></summary>
<br>

| Shortcut | Action |
| --- | --- |
| `Ctrl + L` | Quick Load / Switch active model |
| `Ctrl + R` | Reload last used model |
| `Ctrl + Shift + R` | Open Runtime Manager |
| `Ctrl + Shift + H` | Open Hardware &amp; Live Telemetry |
| `Ctrl + Enter` | Confirm load inside Load Config Modal |

</details>

## A closer look

<p align="center">
  <img src="assets/readme/model-server.png" alt="BibuLM Model Server: loaded model memory breakdown, model alias routing, OpenAI and Anthropic endpoints, and live server logs." width="100%">
  <br>
  <sub><b>Model Server.</b> Live VRAM/RAM placement bar, model alias routing, OpenAI &amp; Anthropic endpoints, and streaming server logs.</sub>
</p>

<p align="center">
  <img src="assets/readme/model-search.png" alt="BibuLM Model Search: HuggingFace GGUF browser with live VRAM fit verdicts and resumable downloads." width="49%">
  <img src="assets/readme/runtime.png" alt="BibuLM Runtime Manager: official ggml-org/llama.cpp builds for CUDA, Vulkan, ROCm, OpenVINO, and CPU." width="49%">
  <br>
  <sub><b>Model Search</b> checks VRAM fit before you download. <b>Runtime Manager</b> pulls official <code>llama.cpp</code> builds matched to your hardware.</sub>
</p>

<p align="center">
  <img src="assets/readme/benchmark.png" alt="BibuLM Benchmark and Placement: verified VRAM vs RAM breakdown, Quick Speed Test, API Playground, llama-bench Matrix, and history." width="49%">
  <img src="assets/readme/link.png" alt="BibuLM Link: BYO Tailscale userspace mesh to connect devices and headless GPU servers with zero manual keys." width="49%">
  <br>
  <sub><b>Benchmark &amp; Placement</b> inspects exact memory placement and runs <code>llama-bench</code> sweeps. <b>BibuLM Link</b> connects your devices over Tailscale.</sub>
</p>

<p align="center">
  <img src="assets/readme/loading.png" alt="BibuLM Load Configuration modal: live VRAM and RAM breakdown, context length, KV cache quantization, Flash Attention, vision projector toggle, and speculative decoding." width="58%">
  <br>
  <sub><b>Load Config.</b> Preview exact VRAM/RAM headroom, tune KV cache and Flash Attention, toggle vision (<code>mmproj</code>) off to save memory, or expose every <code>llama.cpp</code> flag.</sub>
</p>

## Features

| | |
| --- | --- |
| **Runtime Manager** | Fetch official `ggml-org/llama.cpp` GitHub releases (`bXXXX`) across Windows (`x64`/`arm64`), Linux (`x64`/`arm64`), and macOS (`arm64`) · automatic Windows CUDA + `cudart` DLL pairing via NVML · Vulkan, ROCm/HIP, SYCL, OpenVINO, and CPU builds · multiple versions side-by-side (`llama-server` + `llama-bench`) · register custom compiled binaries |
| **GGUF &amp; Memory Engine** | Pure-Rust GGUF v2/v3 header inspector for single and split `.gguf` files (architecture, layers, heads, chat template, reasoning support, tokenizer compatibility for Speculative Decoding) · live VRAM vs. RAM placement estimates before loading · GPU/CPU layer offloading (`-ngl`) and Custom Tensor Overrides (`-ot <regex>=<buffer>`) · toggle vision (`mmproj`) on or off per load to save VRAM · load-time VRAM guardrails |
| **Reasoning &amp; Controls** | Effort levels (`off`, `minimal`, `low`, `medium`, `high`, `xhigh`, `max`), `enable_thinking` toggle, token budgets (`--reasoning-budget`), cutoff messages, and `--reasoning-format` · KV cache quantization (`-ctk`/`-ctv`), Flash Attention (`-fa`), RoPE/YaRN scaling, speculative decoding (`-md`), multimodal `mmproj` toggle, live CLI preview, discovered `llama-server --help` flag catalog, and raw CLI escape hatch |
| **Models &amp; Library** | Search HuggingFace GGUF repos with capability badges (Vision, Reasoning) and sanitized READMEs · grouped split-GGUF quantizations with live VRAM fit verdicts · persistent pause/resume HTTP Range downloads with SHA-256 verification · recursive local library scanning |
| **API Gateway** | Local `axum` reverse-proxy gateway on `http://127.0.0.1:1234` · OpenAI endpoints (`/v1/models`, `/v1/chat/completions`, `/v1/completions`, `/v1/embeddings`, `/v1/responses`) · **Anthropic `/v1/messages` &amp; `/v1/messages/count_tokens`** with `x-api-key` auth for Claude Code · exact &amp; glob Model Alias Routing + fallback · SSE streaming, CORS, LAN toggle, JIT model loading, idle TTL auto-unload, SHA-256 API keys, and rotating logs |
| **Benchmark &amp; Telemetry** | Interactive multi-turn API Playground (Vision upload, Tools JSON + `tool_calls`, Structured JSON Schema, KV prefix cache telemetry) · multi-config `llama-bench` sweep matrix · SQLite benchmark history with CSV/JSON export · live `/metrics` &amp; `/slots` telemetry and GPU VRAM vs. RAM / WDDM spillover verification |
| **Desktop App** | Native Rust + Tauri v2 app · automatic Windows updates with `SHA256SUMS.txt` verification · OS process cleanup (`Job Objects` / `PR_SET_PDEATHSIG`) · OS-encrypted tokens (Windows DPAPI) · system tray and keyboard shortcuts |
| **BibuLM Link** | BYO Tailscale / Headscale mesh via an embedded `tsnet` userspace sidecar — discover your own remote GPUs, stream remote models through your local API gateway, and trigger remote loads, unloads, runtime installs, and model downloads with zero third-party relays |
| **Headless Server CLI** | Standalone `bibulm` CLI binary and Docker image for headless GPU servers — manage runtimes and models from the terminal, serve the gateway, generate `systemd` units, and join your BibuLM Link tailnet automatically |

## BibuLM Link and Headless CLI

### BibuLM Link (BYO Tailscale Mesh)

Sign in with your own Tailscale (or self-hosted Headscale) account inside **Link**. BibuLM runs completely in userspace (`tsnet`) — no admin rights, no system VPN install, and no third-party relay servers. Peers authenticate cryptographically via Tailscale WhoIs (`self_only` by default), so your laptop can route `http://127.0.0.1:1234/v1` requests straight to your home GPU rig over encrypted WireGuard tunnels.

### Headless Server CLI (`bibulm`)

Run BibuLM on a headless Linux box or home GPU server and manage it locally via the CLI or remotely from BibuLM Desktop:

```bash
# 1. Authenticate this server on your Tailscale tailnet (or pass --authkey / TS_AUTHKEY)
bibulm login --name gpu-box

# 2. Install a llama.cpp runtime and pull a GGUF model
bibulm runtime install
bibulm models pull unsloth/Qwen3-8B-GGUF --quant Q4_K_M

# 3. Start the OpenAI/Anthropic gateway + BibuLM Link mesh
bibulm serve --lan --port 1234

# Optional: inspect hardware/status or install a systemd service
bibulm hardware
bibulm status
bibulm service systemd --name gpu-box --lan --install
```

<details>
<summary><b>Docker Compose (headless server)</b></summary>
<br>

```yaml
services:
  bibulm-server:
    build: .
    image: bibulm-server:latest
    container_name: bibulm-server
    restart: unless-stopped
    ports:
      - "1234:1234"
    volumes:
      - bibulm_data:/data
    environment:
      BIBULM_DEVICE_NAME: ${BIBULM_DEVICE_NAME:-bibulm-docker}
      BIBULM_ACCESS_POLICY: ${BIBULM_ACCESS_POLICY:-self_only}
      TS_AUTHKEY: ${TS_AUTHKEY:-}
      HF_TOKEN: ${HF_TOKEN:-}
      GITHUB_TOKEN: ${GITHUB_TOKEN:-}
    # Uncomment for NVIDIA GPU (requires nvidia-container-toolkit):
    # deploy:
    #   resources:
    #     reservations:
    #       devices:
    #         - driver: nvidia
    #           count: all
    #           capabilities: [gpu]
    # Or uncomment for AMD / Intel GPU via Vulkan:
    # devices:
    #   - /dev/dri:/dev/dri

volumes:
  bibulm_data:
```

Run `TS_AUTHKEY=tskey-auth-... docker compose up -d --build` (or omit `TS_AUTHKEY` and open the Tailscale login URL printed in `docker compose logs -f`). Your server then appears as a peer in **BibuLM Desktop → Link**.

</details>

## Contributing

Contributions, bug reports, and ideas are welcome:

- **Found a bug or have an idea?** [Open an issue](https://github.com/Capybaraclette/Bibulm/issues).
- **Want to write code?** Read [CONTRIBUTING.md](CONTRIBUTING.md) for local setup, running the app, tests, and pull request guidelines.

## Support BibuLM

BibuLM is free and open source, with no ads and no paid tier, maintained by [Capybaraclette](https://github.com/Capybaraclette). If it has earned a place in your local LLM setup, here are a couple of ways to help:

- **Star the repository.** It helps other people discover BibuLM.
- **Tell someone about it**: a friend running local models, your homelab community, or a forum post.

## License

BibuLM is licensed under the [MIT License](LICENSE).

---

<p align="center">
  <b>Meet Abribus (Bibu)</b>
  <br>
  <em>Bibu is my cat's surname, and the logo is her face.</em>
  <br><br>
  <img src="assets/readme/bibu.jpg" alt="Abribus (Bibu)" width="340">
</p>
