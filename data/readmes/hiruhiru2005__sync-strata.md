# Sync-Strata

English | [日本語](README.ja.md)

Sync-Strata runs Qwen3.8-Flash-Next (a 125B MoE model) on a single home PC.
The engine is a fork of [Strata](https://github.com/Niko1221/Strata), and the models, **Sync-XS, Sync-S and Sync-M**, are re-quantized to run faster than upstream's Gyro.
A chat app ([dsh](https://www.npmjs.com/package/@deepseek-ai/dsh)) comes with the engine, and you can use it from the desktop app, your phone, the command line or an OpenAI-compatible API.

> **Experimental.** Windows and Linux, with NVIDIA RTX 30/40 series supported (other GPUs: see the table below). The model and engine formats are not compatible with upstream Strata or llama.cpp.

## Requirements

| | |
|---|---|
| OS | Windows 11, Windows 10 (1803 or later), or 64-bit Linux (glibc 2.28 or later: Ubuntu 20.04, Debian 10, RHEL 8 or later, and so on. The author's machine runs Ubuntu 24.04; other distributions are not checked) |
| GPU | See "Supported GPUs" below |
| NVIDIA driver | R580 or newer (CUDA 13; on Linux 580.95.05 or newer). The GTX 10 series, V100 and Titan V (CUDA 12 engine) need 576.57 or newer on Windows and 575.57.08 or newer on Linux |
| CPU | AVX2 is required. CPUs without AVX-512 work, but chat speed drops by about 10% (measured on the author's PC with AVX-512 not used) |
| RAM, VRAM | See the table under "Choosing a model" for the model that fits the RAM in your PC (the minimum amounts are to be measured) |
| Disk | About 2 GB for the app, plus about 35 GB of shared parts that every model needs, plus the model (Sync-XS about 24 GB, Sync-S about 28 GB, Sync-M about 35 GB). An NVMe SSD is recommended for the model |
| Admin rights, Python, Node | Not needed (they are included) |

### Supported GPUs

Setup checks your GPU and downloads only the matching engine (Windows and Linux).

| GPU | Status |
|---|---|
| NVIDIA RTX 30 and 40 series | Supported |
| NVIDIA RTX 20, GTX 16 and RTX 50 series | Expected to work (not checked on real hardware) |
| NVIDIA GTX 10 series, Tesla P100, Tesla V100 and Titan V (CUDA 12 engine) | Experimental (not checked on real hardware) |
| AMD Radeon RX 6000, 7000 and 9000 series, discrete cards including laptop ones such as the RX 7600M and RX 6700S (HIP engine), on Windows and Linux | Experimental (not checked on real hardware) |
| The integrated Radeon of AMD Ryzen AI Max (Strix Halo: 8060S, 8050S, 8040S), on Windows and Linux | Experimental (not checked on real hardware) |
| NVIDIA data-center Ampere cards such as the A100 | Not checked (the engine may not start) |
| Other integrated GPUs and Intel GPUs (Intel Arc and integrated) | Not supported (an integrated Radeon on Windows stops the GPU at the start of text generation; on Linux, integrated Radeons other than Strix Halo are not supported either) |
| NVIDIA Maxwell or older (GTX 900 series and earlier) | Not supported |
| A GPU with less than 8 GB of memory | Not supported (the engine cannot start, so the app stops with a message) |
| No GPU, or a CPU without AVX2 | Not supported |

- Only one GPU is used, even if the PC has several. Of the supported ones, the one with the most memory is chosen (the newer generation if the memory is the same), because more GPU memory is faster. A supported NVIDIA GPU comes first; if no NVIDIA GPU is supported, a supported Radeon is used.
- Macs are not supported.
- WSL2 (Linux on Windows): the author used it with an NVIDIA GPU to build and check the Linux engine. Running the app there is not checked.
- On a PC with no screen (a server over SSH), start with `sync up --no-gui` (`./sync.sh up --no-gui` on Linux). It starts the engine and dsh without opening a window.

## Install

### Windows

1. Download `SyncStrata-<version>.zip` from [Releases](https://github.com/hiruhiru2005/sync-strata/releases) and unzip it (a path without non-ASCII characters is recommended).
2. Double-click `setup.cmd` inside. It installs only what is missing, so running it again is safe.
3. Open **Sync-Strata** on the desktop. The first screen helps you install a model; pick the recommended one (it downloads from Hugging Face).

### Linux

1. Download `SyncStrata-<version>-linux.zip` from [Releases](https://github.com/hiruhiru2005/sync-strata/releases) and extract it.
2. Run `./setup.sh` in a terminal. Like on Windows, it installs only what is missing.
3. Open **Sync-Strata** from the application menu (an icon is also placed on the desktop). The app goes into `~/.local/share/SyncStrata`, and settings and chats into `~/.config/SyncStrata`.

Options (install location, model folder, repair): [docs/INSTALL.md](docs/INSTALL.md). Moving the app or the models after installing: [docs/STORAGE.md](docs/STORAGE.md).

## Use

- **Desktop app**: from the desktop icon. When you close the window you can choose "close the app only", "close the app and dsh" or "close everything". Closing only the app keeps the engine and dsh running.
- **Phone**: on the PC's screen, set "Phone connection" to "Same Wi-Fi" and scan the QR code that appears with a phone on the same Wi-Fi. From outside your home, use [Tailscale](https://tailscale.com/). The QR code is a one-time pass that expires in 3 minutes; the long-lived key never leaves the PC. A phone's login ends 30 days after the day it scanned the QR code; when 7 days or fewer are left, a warning appears on the phone's screen and in "Connected devices" on the PC, and you can take a device's login back there. On the same Wi-Fi the connection is not encrypted ([docs/REMOTE.md](docs/REMOTE.md)).
- **Command line**: `sync` in the install folder (`./sync.sh` on Linux). All commands and options are in [docs/CLI.md](docs/CLI.md).
  ```
  sync up              # start the engine and dsh (no window)
  sync up --api-only   # the API only
  sync status          # running? model, speed
  sync chat            # chat in the terminal
  sync down            # stop everything
  ```
- **API**: `http://127.0.0.1:8080/v1` (8080 is the default port; if another program is using it, the app moves to a free port, so `sync api` shows the actual one. OpenAI-compatible `/v1/chat/completions`, `/v1/responses`, `/v1/models`; Anthropic-compatible `/v1/messages`). `sync api` prints the model name and examples. Connecting from another PC needs a key ([docs/API.md](docs/API.md)).

## Choosing a model

| RAM installed in the PC | Recommended |
|---|---|
| 24 GB or less | **Sync-XS** |
| 32 GB | **Sync-S** |
| 48 GB or more | **Sync-M** |

With the default setting ("auto"), the app checks how much RAM is installed and picks the model for that row. If the free RAM at that moment is not enough, it does not switch to a smaller model. Instead it warns you that part of the model stays on the SSD and runs slower, and that closing some apps would give RAM back. Contents and sizes are on each model page: [Sync-XS](https://huggingface.co/hiru2005/Sync-XS), [Sync-S](https://huggingface.co/hiru2005/Sync-S), [Sync-M](https://huggingface.co/sync-strata/Sync-M).

## Settings

Every setting defaults to "auto". Change them under "Start settings" in the app (PC or phone) or with `sync settings set <name> <value|auto>`. They apply from the next start.

| Setting | Values | What it does |
|---|---|---|
| tail skip (`tail_skip`) | auto, R4, R7, R10 | Uses fewer experts per token to run faster. R4 is the fastest; R10 skips none (highest quality). Auto picks R4 or R7 for your PC |
| Max context length (`context`) | auto, 32K, 64K, 128K, 256K | How much text the model can handle at once. Longer uses more VRAM. Auto: see the table below |
| Quantization (`kv_format`) | auto, k8v4, k8, k4 | Compression of the conversation memory (K/V). k8v4 is the usual; k4 uses the least VRAM |
| RAM limit (`ram_max_gib`) | auto, a number (GiB) | The most RAM used to hold the model. Lower it to run other apps alongside |
| VRAM to leave free (`vram_reserve_mib`) | auto, a number (MiB) | VRAM kept free for other apps |

With "auto", the context and quantization follow your VRAM:

| VRAM | Max context length | Quantization |
|---|---|---|
| 12 GB or more | 256K | k8v4 |
| 10-11 GB | 128K | k8v4 |
| 8-9 GB | 64K | k4 |

dsh summarizes a chat starting at 188,416 tokens when the context is 262,144 (the smaller of 90% of the context and "context - 65,536 for one reply - 8,192 of margin"). This value is set at every start from your settings, and the same value is shown as "where summarizing starts" in the chat screen.

In the app: "Start settings", then "Context settings"; it shows "up to about N tokens" for the setting (`sync ctx` too). Combinations that do not fit in VRAM cannot be chosen. If a chat grows past the limit and VRAM runs out, it slows down, then stops, and the engine is restarted. Other settings, and OS settings that help speed: [docs/SETTINGS.md](docs/SETTINGS.md).

## What happens at start and during chats

- **Memory squeeze**: at start, and once each time you switch models, the app pushes the RAM used by other apps out of memory (to disk) and gives it to the model (on by default). It does not close any app. The amount is shown in the start reason. Turn it off with the `ram_squeeze` setting.
- **Chat saves**: the saved state (K/V) that lets a chat resume quickly is kept on the same drive as the models. The total is capped at the smaller of 20 GiB and 10% of the free space on that drive by default; beyond that, the oldest are deleted. Change the folder and the cap with the `sessions_dir` and `sessions_max_gib` settings.
- **Web search**: the chat screen can search the web. The search engine, [RustXNG](https://github.com/sahenjp/RustXNG) (AGPL-3.0), is not in the release: it is downloaded from upstream the first time you search. The dsh plug-in that connects it, [dsh-rustxng](https://github.com/kgmkm/dsh-rustxng), is MIT.
- **Fewer refusals (uncensored, experimental)**: turned on in Strata settings, the same control vector as upstream Strata makes the model decline less often (off by default). The model weights are not changed. Its safety behavior is weakened too, so you are responsible for what you have it write. From the command line: `sync.cmd settings set refusal_reduction on`.

## Update and uninstall

- **Update**: "Sync-Strata update" in the Start menu on Windows, "Sync-Strata update" in the application menu on Linux (`~/.local/share/SyncStrata/update.sh` does the same). It replaces only the parts that changed and keeps the previous version ("Roll back Sync-Strata" returns to it). Close the app with "close everything" first.
- **Uninstall**: "Uninstall Sync-Strata" in the Start menu on Windows, or in the application menu on Linux (`~/.local/share/SyncStrata/uninstall.sh`). It asks whether to delete the models and your settings and chats (the default keeps them).

Updates and uninstalls never delete models, settings or chats unless you say so.

## Benchmarks

The table below is measured on the author's PC. The values below were measured with version 0.1.0.

- PC: Ryzen 7 7800X3D, 32 GB RAM (DDR5), RTX 3080 12 GB (also drives the display), NVMe SSD. OS: both Windows 11 and Linux (Ubuntu 24.04) (the Linux values are to be measured)
- Engine: Sync-Strata 0.1.0 (Gyro-S and Gyro-M on upstream Strata 0.2.13.1)
- **jbench**: upstream Strata's speed benchmark (tokens/s). Decode is the geometric mean of 10 fixed requests (English and Japanese text, code, JSON, copying, each at temperature 0 and 0.7); prefill is the speed of reading a request of about 1,000 tokens. Thinking is off; the value is the median of 3 runs with different seeds.
- **dsh chat**: average tokens/s of Japanese chats through dsh (thinking "low", default temperature), total tokens divided by total time. 6 casual chats (3-4 turns each, about 18 replies), run 2-3 times with different seeds. dsh's instructions and tool descriptions (about 5,600 tokens) are placed in front every time.

| OS | Model | tail skip | jbench decode | jbench prefill | dsh chat |
|---|---|---|---:|---:|---:|
| Windows | Sync-XS | R4, R7, R10 | To be measured | To be measured | To be measured |
| Windows | Sync-S | R4 | 144.0 | 597 | 104.1 |
| Windows | Sync-S | R7 | 127.5 | 648 | 90.7 |
| Windows | Sync-S | R10 | 104.6 | 593 | 80.1 |
| Windows | Sync-M | R4 | 124.6 | 316 | 92.2 |
| Windows | Sync-M | R7 | 93.6 | 322 | 75.7 |
| Windows | Sync-M | R10 | 69.1 | 322 | 59.1 |
| Windows | Gyro-S (upstream, default) | 7 | 72.6 | 241 | To be measured |
| Windows | Gyro-S (upstream, fastest settings) | | To be measured | To be measured | To be measured |
| Windows | Gyro-M (upstream, default) | 7 | 43.2 | 93 | To be measured |
| Windows | Gyro-M (upstream, fastest settings) | 4 | 67.8 | 102 | To be measured |
| - | GTX 10 series, V100, Titan V (CUDA 12 engine) | - | No hardware; not measured | | |
| - | Radeon RX 6000/7000/9000 (HIP engine) | - | No hardware; not measured | | |

The Linux values (Sync-S, Sync-M and upstream Gyro) are to be measured.

Quality (distance from the original model) is on each model page. Sync-XS quality was measured with the production eval_v4 on Colab. It is on par with the original Sync-XS (the table-lookup form): +0.60% on "scale B", with a 95% range of -0.23 to +1.34%. It is 16.1% better than Gyro-S and 34.8% worse than Sync-S (ratios of KL on scale B; the table is on the [Sync-XS page](https://huggingface.co/hiru2005/Sync-XS)). Speed depends a lot on the PC, especially the amount of RAM, the SSD and what else is running.

## Limitations and known issues

- Only NVIDIA RTX 30/40 series are checked. RTX 20, GTX 16, RTX 50, GTX 10, V100, Titan V and Radeon are not checked on real hardware (table above). Mac, Intel GPUs and integrated GPUs are not supported (only the integrated Radeon of Ryzen AI Max, i.e. Strix Halo such as the 8060S, is supported experimentally on both Windows and Linux). An integrated Radeon on Windows stops the GPU at the start of text generation. On a PC with both a discrete Radeon and an integrated Radeon, the discrete one is used.
- Images are read on the CPU and take a dozen seconds or so each (every release includes image reading).
- Apps that use a lot of GPU or memory bandwidth slow it down a lot (CPU contention is handled automatically). `sync doctor` shows which apps are using them.
- Running on the GPU that also drives your display leaves less VRAM.
- On Radeon (the HIP engine), a test on an unsupported integrated Radeon (Ryzen 7000 series) on Linux showed that GPU work can run out of order and corrupt replies (for example, all zeros). Until this is fixed, Sync-Strata turns on a setting that waits for each GPU step to finish (`AMD_SERIALIZE_KERNEL=2`) on Radeon on Linux by default; reading prompts can be a little slower. Whether this happens on discrete Radeon cards and Strix Halo is not checked.
- On Radeon on Windows, users' RX 9070 XT and RX 9060 XT showed that the setting above stops at the first message, and that the RX 9000 series cannot start because GPU virtual memory (VMM) fails. From 0.1.2, Radeon on Windows uses `AMD_SERIALIZE_KERNEL=0`, `STRATA_HIP_VMM=0` and `STRATA_QL_DMA_GPUFLAG=0` by default (the author has no Radeon running Windows and has not tested this).
- Do not use `STRATA_HIP_PROMPT_F16=1`, which the engine suggests on Radeon: with the Sync models it corrupts replies.
- Part of the calibration text was made from the author's own chat logs (see below).

## About calibration

The models were calibrated on public text (code, documentation, encyclopedia articles, several languages, agent traces) and on some text made from the author's own chat logs. The calibration text is not distributed.

## Support (optional)

Sync-Strata is free and will stay free. If you would like to support it, there is a donation page ([Ko-fi](https://ko-fi.com/hiruhiru2005)).

- A donation is a thank-you only. You get nothing in return: no perks, no priority support, no feature promises.
- Development and support are the same whether or not you donate.
- Donations are meant for development and learning costs, but there is no promise on how they are used.
- Donations are generally non-refundable.
- Donating does not change the license terms of the app, the models or any component (including the Qwen Community License 1.0).

## Credits

- [Strata](https://github.com/Niko1221/Strata) by Niko1221 and the Strata contributors (MIT): the engine and the app are a fork of it.
- Web search uses [RustXNG](https://github.com/sahenjp/RustXNG) (AGPL-3.0). It is not in the release: it is downloaded from upstream at a pinned version (v0.27.0) the first time you search, and checked. The dsh plug-in that connects it, [dsh-rustxng](https://github.com/kgmkm/dsh-rustxng), is MIT.
- [agentionai](https://huggingface.co/agentionai): the Gyro format and kernels, and the Gyro-S weights (the shared parts are cut from them).
- [Qwen](https://huggingface.co/Qwen/Qwen3.8-Flash-Next): the original model, Qwen3.8-Flash-Next.
- [dsh](https://www.npmjs.com/package/@deepseek-ai/dsh) by DeepSeek (MIT): the chat app.
- [llama.cpp / ggml](https://github.com/ggml-org/llama.cpp) (MIT), [Project Maya](https://github.com/mw00/project-maya) (MIT), [Tauri](https://tauri.app/) (MIT / Apache-2.0), [Zen Kaku Gothic New](https://github.com/googlefonts/zen-kakugothic) (SIL OFL 1.1).
- Every bundled part and its license: [LICENSES.md](LICENSES.md).

## License

- Sync-Strata's code: [MIT](LICENSE), the same as upstream Strata.
- The models (Sync-XS, Sync-S, Sync-M and the shared parts): the [Qwen Community License 1.0](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) of the original model. It requires the model name to be shown in commercial products with more than 100 million monthly active users or US$20 million monthly revenue, and a separate license from Qwen for commercial use in a Model-as-a-Service or AI work assistant (coding or office) business. Read the full text in `LICENSE` on each model page.
- Bundled parts: their own licenses ([LICENSES.md](LICENSES.md)).
