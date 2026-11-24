# Unrestricted LLMs on Devices

### Running unrestricted, locally hosted language models from microcontrollers and Raspberry Pi boards to multi-GPU workstations, including nano-scale and on-device (Android and iOS) deployments

> Compiled by [Iman's Lab](https://github.com/Iman/javid-no-code-uncensored). Last revised August 2026.
> Prior work: [poc-uncensored-language-with-wizard-vicuna](https://github.com/imanslab/poc-uncensored-language-with-wizard-vicuna) (Wizard-Vicuna-30B with FastAPI, LangChain, and llama.cpp).

This document is the English edition. The Persian (Farsi) edition follows the same structure and adds extended commentary: [README-complete-guide-FA.md](README-complete-guide-FA.md).

---

## Scope and Conventions

This reference lists open-weight language models with the refusal behaviour removed. The community calls them "abliterated" or "uncensored". Every model here runs entirely on local hardware, with no network connection. The guide covers no-code deployment through Ollama, LM Studio, llama.cpp, and comparable runtimes.

Every model here is multilingual to some degree unless its entry marks it English-centric. The Multilingual column records how well a model handles languages other than English. For Persian-specific guidance, read the Persian edition.

Capability ratings use a one-to-five scale, where five denotes best in class. A trailing plus sign marks models that lead their parameter class. The notation "tok/s" abbreviates tokens generated per second.

Entries added or changed in the August 2026 revision carry an evidence marker:

- **V** (verified): the figure comes from the linked model card or from the file listing of the linked repository.
- **R** (reported): the figure comes from secondary coverage that nobody has checked against the model card. Treat it as a lead, not a fact.

A size written as "estimate" is derived from the RAM formula further down, not read from a published file. The marker covers sizes, licences, dates and benchmark figures. It does not cover the one-to-five capability ratings, which stay editorial. Older entries without a marker predate this convention and were not re-verified in this revision.

"Abliteration" means directional ablation. This post-training procedure removes the internal direction that carries refusal and leaves the rest of the network intact. It damages model quality less than the older refusal-removal fine-tunes.

---

## Prerequisites

### System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| RAM | 4 GB | 8 GB or more |
| Storage | 2 GB free (smallest model) | 20 GB or more (multiple models) |
| Operating system | Windows 10 22H2 or later, macOS 14 Sonoma or later, any modern Linux distribution | Same |
| GPU | Not required (CPU inference is supported) | NVIDIA or AMD GPU with 6 GB or more of VRAM |

### Choosing a Runner

| Runner | Use it when | Notes |
|--------|-------------|-------|
| [LM Studio](https://lmstudio.ai) | You want the shortest path from nothing to a running model | Graphical. Its Discover tab searches Hugging Face and downloads GGUF directly. Runs llama.cpp and MLX. Free for personal and work use since 8 July 2025, [stated by the vendor](https://lmstudio.ai/blog/free-for-work) |
| [Ollama](https://ollama.com) | You want to script it, or serve it over HTTP | One command per model. Version 0.33.2, 27 August 2026, added a native MLX runtime for Apple Silicon, 8-bit KV-cache quantisation and a rewritten NVIDIA path |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | You need a flag the other two do not expose | Both of the above are built on it |

Whichever runner you use, prefer an [Unsloth Dynamic GGUF](https://huggingface.co/unsloth) where one exists for your model. These files carry a `UD-` prefix, such as `UD-Q4_K_XL`. Unsloth picks the quantisation type per layer instead of quantising every layer the same way, and calibrates with an imatrix pass. The output is an ordinary GGUF file, so llama.cpp, Ollama and LM Studio all load it.

The rest of this section installs Ollama, because every model table below carries an `ollama run` command.

### Installing Ollama (Primary Method)

Ollama takes one installation, then one command per model.

macOS:
```bash
# Download from https://ollama.com/download and drag to Applications,
# or install via Homebrew:
brew install ollama
```

Linux:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Windows:
1. Download `OllamaSetup.exe` from [ollama.com/download](https://ollama.com/download).
2. Run the installer (administrator rights are not required).
3. Ollama runs as a background service; use `cmd`, PowerShell, or any terminal.

Verify the installation:
```bash
ollama --version
ollama run huihui_ai/qwen3-abliterated:0.6b   # smallest model, for a quick test
```

### Installing via Docker (Alternative)

Docker is appropriate for server deployments, process isolation, or running Ollama inside a container.

Step 1, install Docker:

| OS | Installation |
|----|--------------|
| macOS | Download [Docker Desktop for Mac](https://docs.docker.com/desktop/setup/install/mac-install/) |
| Linux | `curl -fsSL https://get.docker.com \| sh` |
| Windows | Download [Docker Desktop for Windows](https://docs.docker.com/desktop/setup/install/windows-install/) (requires WSL2) |

Step 2, run Ollama in Docker:
```bash
# CPU only
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

# NVIDIA GPU (requires nvidia-container-toolkit)
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

# AMD GPU
docker run -d --device /dev/kfd --device /dev/dri -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama:rocm
```

Step 3, run a model inside the container:
```bash
docker exec -it ollama ollama run huihui_ai/qwen3-abliterated:4b
```

### NVIDIA GPU Setup (Optional, for GPU Acceleration)

For NVIDIA hardware and faster inference on Linux:
```bash
# Install the NVIDIA Container Toolkit
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg
curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
  sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
  sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
sudo apt-get update && sudo apt-get install -y nvidia-container-toolkit
sudo systemctl restart docker
```

On Windows and macOS, NVIDIA GPU support is handled automatically by the native Ollama installer. Docker GPU passthrough on Windows requires WSL2 with NVIDIA drivers version 452.39 or later.

---

## Quick Start

```bash
curl -fsSL https://ollama.com/install.sh | sh

# General purpose, 2.5 GB, fits any 8 GB laptop
ollama run huihui_ai/qwen3-abliterated:4b

# Coding, 4.7 GB, unrestricted code generation
ollama run huihui_ai/qwen2.5-coder-abliterate:7b

# Reasoning, 9 GB, chain-of-thought with a 128K context window
ollama run huihui_ai/deepseek-r1-abliterated:14b

# Maximum capability on consumer hardware, 19 GB, 30B mixture-of-experts with 3B active
ollama run huihui_ai/qwen3-abliterated:30b-a3b
```

---

## Which File Do I Actually Download?

Every table in this guide names a quantisation such as `Q4_K_M`. On a Hugging
Face page you will see dozens of files and no obvious instruction. This section
answers that, because it is the first thing that stops people.

### The short answer: do not download anything

If a row in this guide has an Ollama command, use it. Ollama fetches the right
file, at the right quantisation, and sets the model up for you.

```bash
ollama run huihui_ai/qwen2.5-coder-abliterate:14b
```

That is the whole procedure for Qwen2.5-Coder-14B. Nothing to choose.

Download files by hand only when you want LM Studio or llama.cpp, or when a
model has no Ollama build.

### If you are downloading by hand

**1. Use a GGUF repository, not the base one.** A base repository such as
`Qwen/Qwen2.5-Coder-14B-Instruct` holds `.safetensors` files. Those are for
transformers and vLLM. Ollama, LM Studio and llama.cpp cannot read them. You
want a repository whose name ends in `-GGUF`, usually published by
`mradermacher`, `bartowski` or the abliteration author.

**2. Open "Files and versions" and take ONE file.** The listing shows the same
model at many quantisations. You need one of them, not the set.

**3. Read the name.** In `Qwen2.5-Coder-14B-abliterated-Q4_K_M.gguf`, the part
after the model name is the quantisation:

| Name | Bits | Size against Q4_K_M | Use it when |
|------|------|---------------------|-------------|
| `Q8_0` | 8 | about 2x | You have memory to spare and want the closest thing to the original |
| `Q6_K` | 6 | about 1.5x | You have memory to spare |
| `Q5_K_M` | 5 | about 1.2x | A little better than Q4, a little larger |
| `Q4_K_M` | 4 | 1x | **Start here.** The usual best trade of size against quality |
| `Q3_K_M` | 3 | about 0.8x | The model will not otherwise fit |
| `Q2_K` | 2 | about 0.6x | Last resort. Quality falls off sharply |

`K` means k-quant, the modern method. `S`, `M` and `L` are small, medium and
large within the same bit width. When in doubt, `Q4_K_M`.

**4. If the file is split, take every part of that one quantisation.** A name
like `model-Q4_K_M-00001-of-00003.gguf` means this quantisation is split across
three files. Download all three into the same folder and point your runner at
the first. Do not mix parts from different quantisations.

**5. Check it fits.** Add roughly 2 GB to the file size for context and
overhead. This guide's tables already do that arithmetic in the RAM column.

### Worked example: Qwen2.5-Coder-14B

Row C6 in the coding section says 9.0 GB at Q4 and about 12 GB of RAM. So:

- With Ollama: `ollama run huihui_ai/qwen2.5-coder-abliterate:14b`, and stop reading.
- By hand: open the abliterated GGUF repository, go to Files and versions, and
  download the single file with `Q4_K_M` in its name, around 9 GB. Ignore
  everything else in the listing, including `.safetensors`, `README.md` and the
  other quantisations.
- On a machine with 8 GB of RAM, 14B will not fit. Use the 7B row instead, or
  drop to `Q3_K_M` and expect worse output.

---

## Part 0: Nano and On-Device Models (Sub-2B)

The smallest unrestricted models, for devices with little memory: single-board computers, embedded systems, and IoT hardware.

Every size in this table is the byte count from the linked repository's file listing, converted to decimal GB.

| ID | Model | Params | Quant | File Size | RAM Needed | Multilingual | Quality | Licence | Ev |
|----|-------|--------|-------|-----------|------------|--------------|---------|---------|----|
| N0 | [Gemma 3 270M abliterated](https://huggingface.co/mradermacher/Huihui-gemma-3-270m-it-abliterated-GGUF) | 0.27B | Q4_K_M | 0.253 GB | ~0.7 GB | 1 | 2 | Gemma terms | V |
| N0b | [Needle 2](https://huggingface.co/Cactus-Compute/needle2) | 45M | `.cact` binary | 13.1 MiB | About 28 MB per session, per the card | 1 | Tool calling and structured extraction only. Not a chat model | Apache 2.0 | V |
| N1 | [Qwen3.5-0.8B abliterated](https://huggingface.co/mradermacher/Huihui-Qwen3.5-0.8B-abliterated-GGUF) | 0.8B | Q4_K_M | 0.528 GB | ~1 GB (estimate) | 2 | 2 | Apache 2.0 | V |
| N1b | [LFM2.5-230M](https://huggingface.co/LiquidAI/LFM2.5-230M-GGUF) | 0.23B | Q4_K_M | 0.153 GB | ~0.5 GB (estimate) | 2 | 2 | LFM Open Licence v1.0 | V |
| N1c | [LFM2.5-350M abliterated](https://huggingface.co/mradermacher/LFM2.5-350M-abliterated-GGUF) | 0.35B | Q4_K_M | 0.229 GB | ~0.6 GB (estimate) | 2 | 2 | LFM Open Licence v1.0 | V |
| N2 | [MiniCPM5-1B abliterated](https://huggingface.co/mradermacher/Huihui-MiniCPM5-1B-abliterated-GGUF) | 1B dense | Q4_K_M | 0.688 GB | ~1.3 GB (estimate) | 2 | 3 | Apache 2.0 | V |
| N2b | [LFM2.5-1.2B-Instruct](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct-GGUF) | 1.2B | Q4_K_M | 0.731 GB | ~1.4 GB (estimate) | 2 | 3 | LFM Open Licence v1.0 | V |
| N3 | [Qwen3.5-2B abliterated](https://huggingface.co/mradermacher/Huihui-Qwen3.5-2B-abliterated-GGUF) | 2B | Q4_K_M | 1.271 GB | ~2 GB (estimate) | 3 | 3 | Apache 2.0 | V |

Unquantised sources: [huihui-ai/Huihui-gemma-3-270m-it-abliterated](https://huggingface.co/huihui-ai/Huihui-gemma-3-270m-it-abliterated), [huihui-ai/Huihui-Qwen3.5-0.8B-abliterated](https://huggingface.co/huihui-ai/Huihui-Qwen3.5-0.8B-abliterated), [huihui-ai/Huihui-Qwen3.5-2B-abliterated](https://huggingface.co/huihui-ai/Huihui-Qwen3.5-2B-abliterated), [huihui-ai/Huihui-MiniCPM5-1B-abliterated](https://huggingface.co/huihui-ai/Huihui-MiniCPM5-1B-abliterated), [LiquidAI](https://huggingface.co/LiquidAI), [openbmb/MiniCPM5-1B](https://huggingface.co/openbmb/MiniCPM5-1B).

What changed since the previous revision:

- Qwen3.5-0.8B replaces Qwen3-0.6B, and Qwen3.5-2B replaces Qwen3-1.7B. Alibaba published no sub-4B model in the Qwen3.6 or Qwen3.8 generations, so these are still the newest small Qwen models. Alibaba publishes no official GGUF for them, and `Qwen/Qwen3.5-0.8B-GGUF` returns HTTP 401. Use the community builds linked above, or the [unsloth build](https://huggingface.co/unsloth/Qwen3.5-0.8B-GGUF) at 0.533 GB.
- LFM2.5 replaces LFM2 across the range. No LFM2.5-700M exists: the 350M and the 1.2B bracket that slot. Liquid AI ships these under the LFM Open Licence v1.0, not Apache 2.0 or MIT, so read it before commercial use.
- Gemma 4 E2B and E4B replaced Gemma 3n E2B and E4B, and left this class in doing so. Google publishes Gemma 4 under Apache 2.0, a change from the Gemma terms that cover Gemma 3. The E2B q4_0 GGUF is 3.35 GB and the E4B q4_0 GGUF is 5.16 GB, so neither fits a 4 GB device. See Part M and Part B.
- **Correction to the previous revision.** This guide gave the Gemma 3n abliterated Q4_K_M files as roughly 1.5 GB and 2.5 GB. The published files are 2.788 GB for E2B and 4.237 GB for E4B, read from the [mradermacher listings](https://huggingface.co/mradermacher/Huihui-gemma-3n-E4B-it-abliterated-GGUF). A 4.24 GB file does not fit a 4 GB device, so the previous recommendation for that tier was wrong.
- Gemma 3 270M stays. Google has published nothing smaller since. An INT4 build handled roughly 25 conversations using about 0.75 percent of a flagship phone battery.
- Needle 2 opens a class below everything else here. At 45M parameters it does tool calling and structured extraction, not conversation. Its card claims 500 tok/s on a Raspberry Pi 5 and 300 to 700 tok/s on phones under USD 200.

Summary for this class: for the lowest memory footprint that still holds a conversation, use LFM2.5-230M at 0.153 GB or Gemma 3 270M at 0.253 GB. For the best multilingual output at nano scale, use Qwen3.5-0.8B at 0.528 GB or Qwen3.5-2B at 1.271 GB. For the best quality under 1 GB, use MiniCPM5-1B at 0.688 GB.

---

## Part M: Running Models Offline on Android and iOS

### Applications (all free, all run GGUF models fully offline)

| Application | Platform | Mechanism | Best For | Last Release |
|-------------|----------|-----------|----------|--------------|
| [PocketPal AI](https://github.com/a-ghorbani/pocketpal-ai) (recommended) | Android and iOS | Built on llama.cpp. Browse and download any GGUF from Hugging Face inside the app. Automatic memory management | General use, the default recommendation | v1.17.2, 25 August 2026 |
| [Google AI Edge Gallery](https://github.com/google-ai-edge/gallery) | Android, iOS and macOS | Runs LiteRT `.litertlm` builds from [litert-community](https://huggingface.co/litert-community) | Google's own on-device models | v1.0.18, 10 August 2026 |
| [SmolChat](https://play.google.com/store/apps/details?id=io.shubham0204.smollmandroid) | Android | Clean conversational interface. Loads any GGUF. Open source | A simple Android experience | v16, 21 June 2026 |
| [MNN Chat](https://play.google.com/store/apps/details?id=com.alibaba.mnnllm.android.release) | Android | Alibaba's on-device runtime. Multimodal | Qwen models on Android | Updated 4 August 2026 |
| [ChatterUI](https://github.com/Vali-98/ChatterUI) | Android | llama.cpp. APK from GitHub releases, not from Play | Power users on Android | v0.10.0-beta5, 28 August 2026 |
| [Locally AI by LM Studio](https://apps.apple.com/us/app/locally-ai-by-lm-studio/id6741426692) | iOS, iPadOS and macOS | MLX backed | Apple hardware, closest to LM Studio on the desktop | v1.64.0, 11 August 2026 |
| [MLC Chat](https://github.com/mlc-ai/mlc-llm) | Android and iOS | Compiles through TVM. Runs on the Adreno GPU through OpenCL on Qualcomm, Vulkan elsewhere on Android, Metal on Apple | Source builds only | iOS build v1.6, September 2024. Not on Google Play |

Three corrections to the previous revision of this table:

- LLMFarm is gone. Its README states that the app is unavailable on TestFlight and the App Store, its last release is 1.4.3 from January 2025, and both project domains fail to resolve.
- SmolChat's Play package was given as `com.shubham0204.smolchat`, which returns 404. The package is `io.shubham0204.smollmandroid`.
- MLC Chat was credited with "NPU optimisation for Snapdragon 8 Gen 2 and later". MLC has no NPU backend. Its Android build sets `-DUSE_HEXAGON_SDK=OFF` and `-DUSE_OPENCL=ON`, and its own documentation lists cuda, metal, vulkan, rocm and opencl. On Qualcomm hardware it runs on the Adreno GPU through OpenCL. The NPU path on Android runs through AICore and the ML Kit Prompt API instead, and Google AI Edge Gallery ships per-chip builds for it (`sm8550`, `sm8650`, `sm8750`, `sm8850`, `tensor-g5`).

Two routes need no model download at all. The Apple Foundation Models framework exposes the on-device Apple Intelligence model to third-party apps on iOS, iPadOS, macOS and visionOS 26.0. On Android, ML Kit GenAI reaches Gemini Nano through AICore, but every one of those APIs is pre-stable and Google's documentation states that they carry no SLA and no deprecation policy. Neither route is uncensored.

### Recommended Model by Device Class

| Device Type | RAM | Recommended Model | File Size | Speed |
|-------------|-----|-------------------|-----------|-------|
| Budget or older (circa 2020, 4 GB) | 4 GB | Gemma 3 270M or Qwen3.5-0.8B Q4_K_M | 0.25 to 0.53 GB | ~5 to 8 tok/s |
| Mid-range (6 GB) | 6 GB | Qwen3.5-2B Q4_K_M or MiniCPM5-1B Q4_K_M | 0.69 to 1.27 GB | ~8 to 15 tok/s |
| Flagship (8 GB or more) | 8 GB+ | Qwen3.5-4B Q4_K_M, or Gemma 4 E2B q4_0 for image input | 2.71 to 3.35 GB | ~15 to 30 tok/s |
| iPhone 14 or later, iPad (6 GB or more) | 6 GB+ | Qwen3.5-2B Q4_K_M | 1.27 GB | ~15 to 25 tok/s |
| iPhone 15 Pro or 16 (8 GB) | 8 GB | Qwen3.5-4B Q4_K_M | 2.71 GB | ~20 to 30 tok/s |

The tok/s ranges describe the device class at these model sizes. Nobody re-measured them for the August 2026 models, so treat them as carried forward.

### Loading a Model on a Device

1. Install PocketPal AI from the App Store or Play Store.
2. Open the application, then go to Models and select "Add from Hugging Face".
3. Search for `huihui-ai Qwen3.5 abliterated GGUF` or `MiniCPM5-1B abliterated GGUF`.
4. Choose the Q4_K_M quantisation that fits the available RAM.
5. Download the file once over Wi-Fi. The model then runs fully offline.

Note on battery: continuous use can consume roughly half a charge in 90 minutes. Closing background applications frees RAM and improves throughput.

---

## Part A: Qwen Abliterated (Recommended for Multilingual Use)

Alibaba trained Qwen3 on about 36 trillion tokens across 119 languages, with native non-English support. huihui-ai abliterated it under the Apache 2.0 licence, by directional ablation, which removes refusal behaviour and keeps general capability. Source: [huihui-ai](https://huggingface.co/huihui-ai).

| ID | Model | Params | Quant | GGUF Size | RAM Needed | Multilingual | Intelligence | Best For | Ollama |
|----|-------|--------|-------|-----------|------------|--------------|--------------|----------|--------|
| 1 | Qwen3-0.6B abliterated | 0.6B | Q4_K_M | 0.4 GB | ~1 GB | 2 | 2 | IoT, edge, Raspberry Pi 3 / Zero 2 W | `ollama run huihui_ai/qwen3-abliterated:0.6b` |
| 2 | Qwen3-1.7B abliterated | 1.7B | Q4_K_M | 1.1 GB | ~2 GB | 3 | 3 | Raspberry Pi 4/5, constrained devices, 4 GB laptops | `ollama run huihui_ai/qwen3-abliterated:1.7b` |
| | | | Q8_0 | 1.8 GB | ~3 GB | | (better) | Raspberry Pi 5 (8 GB) | |
| 3 | Qwen3-4B abliterated | 4B | Q3_K_M | 2.0 GB | ~3.5 GB | 4 | 4 | 4 GB laptops (tight) | `ollama run huihui_ai/qwen3-abliterated:4b` |
| | | | Q4_K_M | 2.5 GB | ~4.5 GB | | rivals older 72B models | 8 GB laptops (recommended) | |
| | | | Q8_0 | 4.4 GB | ~6.5 GB | | (best at 4B) | 8 GB or larger systems | |
| 4 | Qwen3-8B abliterated v2 | 8B | Q3_K_M | 4.1 GB | ~6 GB | 4 | 5 | 8 GB laptop (tight) | `ollama run huihui_ai/qwen3-abliterated:8b` |
| | | | Q4_K_M | 5.0 GB | ~7 GB | | strong reasoning | 8 GB laptop (recommended) | |
| | | | Q5_K_M | 5.9 GB | ~8 GB | | | 16 GB systems | |
| | | | Q8_0 | 8.7 GB | ~11 GB | | (best at 8B) | 16 GB systems | |
| 5 | Qwen3-14B abliterated | 14B | Q3_K_M | 7.0 GB | ~9 GB | 5 | 5 | 12 to 16 GB systems | `ollama run huihui_ai/qwen3-abliterated:14b` |
| | | | Q4_K_M | 9.0 GB | ~12 GB | | excellent multilingual | 16 GB laptop or desktop | |
| | | | Q8_0 | 15.7 GB | ~18 GB | | | 24 GB or larger | |
| 6 | Qwen3-30B-A3B abliterated (MoE) | 30B total / 3B active | Q3_K_M | 13.5 GB | ~16 GB | 5 | 5+ | 16 to 24 GB (aggressive Q3) | `ollama run huihui_ai/qwen3-abliterated:30b-a3b` |
| | | | Q4_K_M | 18.6 GB | ~22 GB | | exceeds QwQ-32B | 24 to 32 GB RAM or 24 GB GPU | |
| 7 | Qwen3-32B abliterated | 32B | Q3_K_M | 15.0 GB | ~18 GB | 5 | 5+ | 24 GB or larger | `ollama run huihui_ai/qwen3-abliterated:32b` |
| | | | Q4_K_M | 19.9 GB | ~24 GB | | top-tier open model | 32 GB RAM, RTX 3090 or better | |

Rule of thumb for RAM: GGUF file size plus roughly 2 GB of runtime overhead for the llama.cpp or Ollama context buffer. Longer context windows require proportionally more.

### Qwen 3.5 to 3.8 Uncensored Builds (August 2026)

Alibaba shipped Qwen3.5, Qwen3.6 and Qwen3.8 after the Qwen3 range above. Each size, licence and date below comes from the linked model card or from the file listing of the linked repository. Sizes are decimal GB.

| ID | Build | Params | Quant | File Size | RAM Needed | Licence | Refusal Removed By | Ev |
|----|-------|--------|-------|-----------|------------|---------|--------------------|----|
| A7 | [Qwen3.5-4B abliterated](https://huggingface.co/mradermacher/Huihui-Qwen3.5-4B-abliterated-GGUF) | 4B dense | Q4_K_M | 2.71 GB | ~4.7 GB | Apache 2.0 | Abliteration | V |
| A8 | [orcarouter/Qwen3.8-27B-Uncensored-GGUF](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-GGUF) | 27.8B dense | Q4_K_M | 16.81 GB | ~19 GB | Apache 2.0 | Abliteration | V |
| | same repo | | Q5_K_M | 19.54 GB | ~22 GB | | | V |
| | same repo | | Q8_0 | 29.05 GB | ~31 GB | | | V |
| A9 | [orcarouter/Qwen3.8-27B-Uncensored-FP8](https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored-FP8) | 27.8B dense | FP8, for vLLM | 30.87 GB | 48 GB VRAM or more (estimate from the weight size) | Apache 2.0 | Abliteration | V |
| A10 | [cloudbjorn/Qwen3.6-27B_Samantha-Uncensored_GGUF](https://huggingface.co/cloudbjorn/Qwen3.6-27B_Samantha-Uncensored_GGUF) | 26.9B dense | Q4_K_M | 16.55 GB | ~19 GB | `other`, with no licence text on the card | LoRA merge on the samantha-1.1-uncensored dataset | V |
| A11 | [huihui-ai/Huihui-Qwen3.5-397B-A17B-abliterated-GGUF](https://huggingface.co/huihui-ai/Huihui-Qwen3.5-397B-A17B-abliterated-GGUF) | 397B total / 17B active, MoE | Q3_K, 21 shards | 189.5 GB | Server class. See Part G | Apache 2.0 | Abliteration | V |

Notes on these builds:

- The Qwen3.8 GGUF repository is gated. Accept the terms on Hugging Face before you download. The GGUF landed on 16 August 2026 and the FP8 build on 15 August 2026.
- The Qwen3.8 GGUF repository also holds `mmproj-Qwen3.8-27B-Uncensored-f16.gguf` at 0.93 GB. Download that file too if you want image input.
- A10 is not an abliteration. Its author trained on the `digitalpipelines/samantha-1.1-uncensored` dataset and merged a LoRA at bf16. The merge dropped the vision tower, so the result is text only. The card declares `license: other` and gives no licence text, so you have no stated terms.
- huihui-ai publishes only Q3_K for A11. No Q4, Q5, Q6 or Q8 build exists. At 189.5 GB across 21 shards it needs a multi-GPU server.
- Name trap: a separate Samantha line runs on Qwen3.8 from a different author, [Lathly/Qwen3.8-27B-Samantha](https://huggingface.co/Lathly/Qwen3.8-27B-Samantha). It is not the cloudbjorn build in row A10.

---

## Part B: Gemma Abliterated (Google)

Gemma is Google's open model family. Google built the Gemma 3n variants for on-device and edge use, with low memory use. [mlabonne](https://huggingface.co/mlabonne) abliterated the non-n Gemma 3 models. [huihui-ai](https://huggingface.co/huihui-ai) abliterated the Gemma 3n variants. Gemma 3n covers 140 languages, and its non-English quality trails Qwen3.

| ID | Model | Params | Quant | GGUF Size | RAM Needed | Multilingual | Intelligence | Notes |
|----|-------|--------|-------|-----------|------------|--------------|--------------|-------|
| G1 | Gemma 3n E2B abliterated | 5B (2B eff.) | Q4_K_M | 2.788 GB (corrected) | ~4.8 GB | 1 | 3 | Superseded by Gemma 4 E2B. Vision and audio. |
| G2 | Gemma 3n E4B abliterated | 8B (4B eff.) | Q4_K_M | 4.237 GB (corrected) | ~6 GB | 1 | 4 | Superseded by Gemma 4 E4B. Google stated in 2025 that E4B was the first model under 10B parameters to score above 1300 on LMArena. LMArena now redirects to arena.ai, where no sub-10B model appears in the visible leaderboard, so read that as a dated historical note. |
| G3 | Gemma 3 4B abliterated | 4B | Q4_K_M | ~2.5 GB | ~4.5 GB | 2 | 3 | Experimental; occasional text artefacts. [mlabonne GGUF](https://huggingface.co/mlabonne/gemma-3-4b-it-abliterated-GGUF) |
| G4 | Gemma 3 12B abliterated | 12B | Q4_K_M | ~7.4 GB | ~10 GB | 2 | 4 | Strong English, acceptance rate above 90 percent. [mlabonne GGUF](https://huggingface.co/mlabonne/gemma-3-12b-it-abliterated-GGUF) |
| G5 | Gemma 3 27B abliterated | 27B | Q4_K_M | ~16.5 GB | ~20 GB | 2 | 5 | Top-tier, vision capable. [mlabonne GGUF](https://huggingface.co/mlabonne/gemma-3-27b-it-abliterated-GGUF) |

Gemma 3 resists abliteration more than Qwen does. mlabonne built a layerwise technique for it, based on hidden states. The results are good, and the author still labels them experimental.

### Gemma 4 Abliterated (Current Generation)

Google released Gemma 4 in five sizes: E2B, E4B, 12B, 26B-A4B and 31B, under Apache 2.0. The 12B, 26B-A4B and 31B carry a 256K context. E2B and E4B carry 128K. Every size accepts image input, and E2B, E4B and 12B also accept audio. Base card: [google/gemma-4-31B-it](https://huggingface.co/google/gemma-4-31B-it).

| ID | Build | Params | Quant | File Size | RAM Needed | Image Input | Licence | Ev |
|----|-------|--------|-------|-----------|------------|-------------|---------|----|
| G6 | [huihui-ai Gemma 4 31B qat abliterated](https://huggingface.co/huihui-ai/Huihui-gemma-4-31B-it-qat-q4_0-unquantized-abliterated-GGUF) | 31.3B dense | Q4_K | 18.69 GB (17.40 GiB) | ~21 GB | Yes, with the 1.20 GB mmproj file in the same repo | Apache 2.0 | V |
| G7 | [Stabhappy gemma-4-31B-it-heretic](https://huggingface.co/Stabhappy/gemma-4-31B-it-heretic-Gguf) | 31.3B dense | Q4_0 | 17.65 GB | ~20 GB | Yes, mmproj shipped | None declared | V |
| | same repo | | Q4_K_M | 18.69 GB | ~21 GB | | | V |
| G8 | [Stabhappy gemma-4-31B-it-qat heretic](https://huggingface.co/Stabhappy/gemma-4-31B-it-qat-q4_0-unquantized-heretic-GGUF) | 31.3B dense | Q4_K_M | 18.69 GB | ~21 GB | No mmproj in the repo, so text only | None declared | V |

Notes on these builds:

- Google's card for `google/gemma-4-31B-it` states native function calling and interleaved multimodal input. Neither abliterated card repeats those claims. Read the base card for what the model can do, and the abliterated card for what changed.
- Sizes above are decimal GB. llama.cpp and most file managers report GiB, where the 18.69 GB file reads as 17.40 GiB. A "17 GB" figure quoted elsewhere for this model is either that GiB reading or the Q4_0 file at 17.65 GB.
- The two Stabhappy repositories declare no licence at all. The [Gemma 4 terms](https://ai.google.dev/gemma/docs/gemma_4_license) are the only terms you have for them.
- huihui-ai names its file `Q4_K` rather than `Q4_K_M`. It is the same quantisation.

---

## Part C: Dolphin and Wizard-Vicuna Lineage (Eric Hartford)

The companion [proof-of-concept repository](https://github.com/imanslab/poc-uncensored-language-with-wizard-vicuna) used Wizard-Vicuna-30B-Uncensored (TheBloke GGUF, roughly 23 GB at Q5_K_M). The models below are successors from the same author (Eric Hartford, Cognitive Computations). They are English-centric. Non-English support is weak or absent, so use Qwen3 for multilingual work.

| ID | Model | Params | Quant | GGUF Size | RAM Needed | Multilingual | Intelligence | Best For | Ollama / HF |
|----|-------|--------|-------|-----------|------------|--------------|--------------|----------|-------------|
| 8 | Dolphin 2.0 Mistral 7B | 7B | Q4_K_M | 4.1 GB | ~6 GB | 1 (weak) | 3 | Budget English | `ollama run dolphin-mistral` |
| 9 | Dolphin 2.9.1 Llama3 8B | 8B | Q4_K_M | 4.9 GB | ~7 GB | 1 (weak) | 4 | English chat, coding, agentic | `ollama run dolphin-llama3:8b` |
| 10 | Dolphin 2.9.3 Mistral-Nemo 12B | 12B | Q4_K_M | 7.4 GB | ~10 GB | 2 (some) | 4 | 128K context, multilingual | [cognitivecomputations GGUF](https://huggingface.co/cognitivecomputations/dolphin-2.9.3-mistral-nemo-12b-gguf) |
| 11 | Wizard-Vicuna-13B-Uncensored | 13B | Q4_K_M | 7.9 GB | ~10 GB | 1 (weak) | 3 | Classic, legacy | [TheBloke GGUF](https://huggingface.co/TheBloke/Wizard-Vicuna-13B-Uncensored-GGUF) |
| 12 | Wizard-Vicuna-30B-Uncensored (PoC model) | 30B | Q4_K_M | 18.3 GB | ~22 GB | 1 (weak) | 4 | The original PoC model | [TheBloke GGUF](https://huggingface.co/TheBloke/Wizard-Vicuna-30B-Uncensored-GGUF) |
| | | | Q5_K_M | 22.6 GB | ~26 GB | | (as used in the PoC) | 32 GB or larger | |

---

## Part E: Coding Models

Code-generation models with refusal behaviour removed, for writing, debugging, and analysing code without interruption.

### Qwen3-Coder (Recommended for Code)

Alibaba's coding line. All three sizes are Apache 2.0 and carry a 262,144-token native context. huihui-ai abliterates them.

Base models, and what they score:

| Base Model | Params | Context | SWE-bench Verified | Ev |
|------------|--------|---------|--------------------|----|
| [Qwen/Qwen3-Coder-Next](https://huggingface.co/Qwen/Qwen3-Coder-Next) | 80B total / 3B active, MoE | 262,144 | 70.6 percent, and 71.3 percent under OpenHands | V, card and [technical report](https://arxiv.org/abs/2603.00729) |
| [Qwen/Qwen3-Coder-480B-A35B-Instruct](https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct) | 480B total / 35B active, MoE | 262,144, 1M with YaRN | 69.6 percent | R, launch chart only. See the notes |
| [Qwen/Qwen3-Coder-30B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct) | 30.5B total / 3.3B active, MoE | 262,144, 1M with YaRN | Not stated on the card | V |

Abliterated builds, and what they weigh:

| ID | Build | Quant | File Size | RAM Needed | Ev | Ollama |
|----|-------|-------|-----------|------------|----|--------|
| C1 | [Qwen3-Coder-30B abliterated](https://huggingface.co/huihui-ai/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated) | Q4_K_M | 18.56 GB | ~21 GB | V | `ollama run huihui_ai/qwen3-coder-abliterated:30b` |
| C1a | [Qwen3-Coder-Next abliterated, bartowski GGUF](https://huggingface.co/bartowski/huihui-ai_Qwen3-Coder-Next-abliterated-GGUF) | Q4_K_M | 48.56 GB | ~51 GB | V | `ollama run huihui_ai/qwen3-coder-next-abliterated` |
| | same repo | IQ2_M | 25.19 GB | ~27 GB | V | |
| | same repo | IQ1_M | 17.19 GB | ~19 GB | V | |
| C1b | Qwen3-Coder-480B abliterated | Q4_K_M | about 280 GB across 32 shards | Multi-GPU cluster | R | `ollama run huihui_ai/qwen3-coder-abliterated:480b` |

Notes on this line:

- Qwen3-Coder-Next does not fit in 24 GB of VRAM at Q4. Its Q4_K_M file is 48.56 GB, and Unsloth's run guide asks for 46 GB of RAM, VRAM or unified memory at 4-bit. Only the 1-bit and 2-bit quants come near a 24 GB card. It activates 3B parameters per token, so it still runs at a usable rate on a 24 GB GPU with the rest offloaded to system RAM.
- The 69.6 percent figure for the 480B model is not on its model card. It comes from the launch chart and from Together AI's launch-partner post, so it is marked R.
- huihui-ai's own 480B GGUF repository returns HTTP 401 and does not appear in that author's public listing. The Ollama tag works. The 280 GB figure comes from a third-party mirror, not from a first-party listing, so it is marked R.
- The abliterated Qwen3-Coder-Next repository ships safetensors, not GGUF. Use the bartowski build for llama.cpp, Ollama or LM Studio.

### The 16 to 24 GB Tier

Five coding models fit a 24 GB card or a 32 GB laptop at Q4_K_M. They differ more in licence than in size, so read the licence column before you commit to one.

| Model | Params | Context | Q4_K_M | RAM Needed | Licence | SWE-bench Verified | Ev |
|-------|--------|---------|--------|------------|---------|--------------------|----|
| [Qwen3-Coder-30B-A3B](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct) | 30.5B total / 3.3B active | 262,144 | 18.56 GB | ~21 GB | Apache 2.0 | Not stated on the card | V |
| [Devstral Small 2 24B](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512) | 24B dense | 256K | 14.33 GB | ~16 GB | Apache 2.0 | 68.0 percent | V |
| [Devstral Small 2507](https://huggingface.co/mistralai/Devstral-Small-2507) | 24B dense | 128K | 14.33 GB | ~16 GB | Apache 2.0 | 53.6 percent | V |
| [DeepSeek-Coder-V2 Lite 16B](https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct) | 16B total / 2.4B active | 128K | 10.36 GB | ~12 GB | `deepseek-license`, not MIT | Not stated on the card | V |
| [Codestral 22B v0.1](https://huggingface.co/mistralai/Codestral-22B-v0.1) | 22B dense | Not stated on the card | 13.34 GB | ~15 GB | MNPL-0.1, non-production | Not stated on the card | V |

Q4_K_M sizes come from the file listings of [unsloth](https://huggingface.co/unsloth) for the Qwen and Devstral builds, and of [bartowski](https://huggingface.co/bartowski) for the DeepSeek and Codestral builds.

### Coding Model Licences

| Family | Licence | What it permits |
|--------|---------|-----------------|
| Qwen3-Coder: Next, 480B, 30B | Apache 2.0 | Commercial use, with no attribution trigger |
| Devstral Small: 2507 and 2-24B-2512 | Apache 2.0 | Commercial use, with no attribution trigger |
| [Devstral 2 123B](https://huggingface.co/mistralai/Devstral-2-123B-Instruct-2512) | `other`: a modified MIT with a third-party-rights restriction | Read the card before commercial use |
| GLM-5.2 | MIT | Commercial use |
| DeepSeek-Coder-V2 Lite | `deepseek-license` | Commercial use under DeepSeek's own model licence. MIT covers only the code repository, not the weights |
| Codestral 22B v0.1 | Mistral AI Non-Production Licence, [MNPL-0.1](https://mistral.ai/licences/MNPL-0.1.md) | Research and testing. Not production |
| Llama 3.2, 3.3 and 4 | Llama Community Licence, one version per release | Commercial use below the monthly-active-user threshold, with a "Built with Llama" attribution |

Two claims circulate about this table and both are wrong. DeepSeek-Coder-V2's weights are not MIT. And no open-weight "Codestral 2" exists on Hugging Face: the current open Codestral is still the 2024 22B model under MNPL-0.1.

### Qwen2.5-Coder Abliterated (Widest Size Range)

The previous generation covers every size from 0.5B to 32B, with a 32K context and 92 programming languages. huihui-ai abliterated the whole range: [huihui-ai](https://huggingface.co/huihui-ai).

| ID | Model | Params | Q4 Size | RAM Needed | Multilingual | Coding | Ollama |
|----|-------|--------|---------|------------|--------------|--------|--------|
| C2 | Qwen2.5-Coder-0.5B abliterated | 0.5B | 398 MB | ~1 GB | 2 | 2 | `ollama run huihui_ai/qwen2.5-coder-abliterate:0.5b` |
| C3 | Qwen2.5-Coder-1.5B abliterated | 1.5B | 1.1 GB | ~2 GB | 2 | 3 | `ollama run huihui_ai/qwen2.5-coder-abliterate:1.5b` |
| C4 | Qwen2.5-Coder-3B abliterated | 3B | 1.9 GB | ~3.5 GB | 3 | 3 | `ollama run huihui_ai/qwen2.5-coder-abliterate:3b` |
| C5 | Qwen2.5-Coder-7B abliterated | 7B | 4.7 GB | ~7 GB | 3 | 4 | `ollama run huihui_ai/qwen2.5-coder-abliterate:7b` |
| C6 | Qwen2.5-Coder-14B abliterated | 14B | 9.0 GB | ~12 GB | 4 | 5 | `ollama run huihui_ai/qwen2.5-coder-abliterate:14b` |
| C7 | Qwen2.5-Coder-32B abliterated | 32B | 20 GB | ~24 GB | 4 | 5+ | `ollama run huihui_ai/qwen2.5-coder-abliterate:32b` |

### WizardLM CodeLlama 34B Uncensored (Legacy)

A classic English-only uncensored coding model, fine-tuned on CodeLlama-34B by Eric Hartford.

| ID | Model | Params | Q4 Size | RAM Needed | Coding | HF |
|----|-------|--------|---------|------------|--------|-----|
| C8 | WizardLM-CodeLlama-34B Uncensored | 34B | ~20 GB | ~24 GB | 4 | [TheBloke GGUF](https://huggingface.co/TheBloke/WizardLM-1.0-Uncensored-CodeLlama-34B-GGUF) |

Summary for coding: on a 24 GB card or a 32 GB laptop, Devstral Small 2 24B scores 68.0 percent on SWE-bench Verified at 14.33 GB, under Apache 2.0. Above 48 GB, Qwen3-Coder-Next scores 70.6 percent. On an 8 GB laptop, use Qwen2.5-Coder-7B abliterated. For the smallest footprint of all, Qwen2.5-Coder-0.5B abliterated is 398 MB.

---

## Part F: Reasoning and Other Notable Models

### DeepSeek-R1 Abliterated (641K+ downloads)

DeepSeek distilled its reasoning model into Qwen and Llama bases. Chain-of-thought reasoning, 128K context. huihui-ai abliterated the distills: [huihui-ai](https://huggingface.co/huihui-ai).

| ID | Model | Params | Q4 Size | RAM Needed | Multilingual | Reasoning | Ollama |
|----|-------|--------|---------|------------|--------------|-----------|--------|
| R1 | DeepSeek-R1 abliterated 1.5B | 1.5B | 1.1 GB | ~2 GB | 2 | 3 | `ollama run huihui_ai/deepseek-r1-abliterated:1.5b` |
| R2 | DeepSeek-R1 abliterated 7B | 7B | 4.7 GB | ~7 GB | 3 | 4 | `ollama run huihui_ai/deepseek-r1-abliterated:7b` |
| R3 | DeepSeek-R1 abliterated 8B | 8B | 5.0 GB | ~7 GB | 3 | 4 | `ollama run huihui_ai/deepseek-r1-abliterated:8b` |
| R4 | DeepSeek-R1 abliterated 14B | 14B | 9.0 GB | ~12 GB | 4 | 5 | `ollama run huihui_ai/deepseek-r1-abliterated:14b` |
| R5 | DeepSeek-R1 abliterated 32B | 32B | 20 GB | ~24 GB | 4 | 5+ | `ollama run huihui_ai/deepseek-r1-abliterated:32b-qwen-distill` |
| R6 | DeepSeek-R1 abliterated 70B | 70B | 43 GB | ~48 GB | 5 | 5+ | `ollama run huihui_ai/deepseek-r1-abliterated:70b` |

### GPT-OSS Abliterated (OpenAI Open-Weight)

OpenAI's first open-weight release: a 20B mixture-of-experts sized for consumer hardware, with a 128K context. huihui-ai abliterated it: [huihui-ai](https://huggingface.co/huihui-ai).

| ID | Model | Params | Q4 Size | RAM Needed | Reasoning | Ollama |
|----|-------|--------|---------|------------|-----------|--------|
| O1 | GPT-OSS-20B abliterated (MoE) | 20B | ~14 GB | ~18 GB | 4 | `ollama run huihui_ai/gpt-oss-abliterated:20b` |
| O2 | GPT-OSS-120B abliterated | 120B | ~88 GB | ~96 GB | 5+ | `ollama run huihui_ai/gpt-oss-abliterated:120b` |

### QwQ Abliterated (Qwen Reasoning)

Alibaba's dedicated reasoning model, with strong chain-of-thought. huihui-ai abliterated it: [huihui-ai](https://huggingface.co/huihui-ai).

| ID | Model | Params | Q4 Size | RAM Needed | Multilingual | Reasoning | Ollama |
|----|-------|--------|---------|------------|--------------|-----------|--------|
| Q1 | QwQ-32B abliterated | 32B | ~20 GB | ~24 GB | 5 | 5+ | `ollama run huihui_ai/qwq-abliterated` |

### Other Notable Abliterated Models (huihui-ai)

| Model | Params | Q4 Size | RAM Needed | Notes | Ollama |
|-------|--------|---------|------------|-------|--------|
| Granite 4.1 abliterated | 3B / 8B / 30B | ~2 to 19 GB | varies | IBM Granite. Strong tool calling and instruction following. | `ollama run huihui_ai/granite4.1-abliterated` |
| Dolphin 3.0 Llama3.1-8B abliterated | 8B | ~5 GB | ~7 GB | Coding, agentic use, and function calling. | `ollama run huihui_ai/dolphin3-abliterated` |
| Phi-4 abliterated | 14B | ~9 GB | ~12 GB | Microsoft. Strong mathematics and logic. | `ollama run huihui_ai/phi4-abliterated` |
| Phi-4-mini abliterated | 3.8B | ~2.5 GB | ~4 GB | Compact, with function-calling support. | `ollama run huihui_ai/phi4-mini-abliterated` |
| Mistral Small 24B abliterated | 24B | ~14 GB | ~18 GB | Strong multilingual, 128K context. | `ollama run huihui_ai/mistral-small-abliterated` |
| GLM-4.7-Flash abliterated | 9B | ~6 GB | ~8 GB | Zhipu AI. Fast, bilingual (English and Chinese). | `ollama run huihui_ai/glm-4.7-flash-abliterated` |
| Llama 3.3 70B abliterated | 70B | ~43 GB | ~48 GB | Meta. Excellent general-purpose English. | `ollama run huihui_ai/llama3.3-abliterated` |
| Llama 3.2 abliterated | 1B / 3B | 0.7 / 2 GB | ~2 / 4 GB | Smallest Meta models, suited to edge. | `ollama run huihui_ai/llama3.2-abliterate` |

---

## Part G: Frontier-Scale Open-Weight Models

These are frontier-scale mixture-of-experts models with open weights, mostly from Chinese labs. They need multi-GPU servers or large-memory workstations, so most readers reach them through a hosted endpoint and run the smaller distilled or abliterated variants locally. They are here because uncensored GGUF builds of several now exist, and because the smaller local models in Parts A to F are distilled or derived from them.

### Current Generation (Verified August 2026)

Every figure in this table comes from the model's own card. Where the card gives several numbers for one benchmark, the reasoning mode is named.

| Model | Developer | Scale | Context | Licence | Benchmarks From the Card | Ev | Local Access |
|-------|-----------|-------|---------|---------|--------------------------|----|--------------|
| [Kimi K3](https://huggingface.co/moonshotai/Kimi-K3) | Moonshot AI | 2.8T total / 104B active | 1,048,576 | Kimi K3 Licence, not MIT. A separate agreement applies above USD 20M revenue over any 12 months | Terminal-Bench 2.1 88.3, FrontierSWE 81.2, GPQA Diamond 93.5 | V | Weights on Hugging Face. No abliterated GGUF found as of 31 August 2026 |
| [GLM-5.2](https://huggingface.co/zai-org/GLM-5.2) | Zhipu AI | 753B by the Hugging Face weight count. The developer's GitHub says 744B total / 40B active | 1,048,576 | MIT | GPQA Diamond 91.2 percent, SWE-bench Pro 62.1 percent | V | [huihui-ai abliterated GGUF](https://huggingface.co/huihui-ai/Huihui-GLM-5.2-abliterated-GGUF). Smallest published quant is 211 GB |
| [DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) | DeepSeek | 1.6T total / 49B active | 1M | MIT | SWE-bench Verified 80.6 percent at maximum reasoning effort, 79.4 at high, 73.6 without thinking. SWE-bench Pro 55.4 | V | Weights on Hugging Face. Newer checkpoint: [DeepSeek-V4-Pro-0813](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-0813) |
| [MiniMax M3](https://huggingface.co/MiniMaxAI/MiniMax-M3) | MiniMax | ~428B total / ~23B active | 1M | MiniMax Community Licence. Non-commercial by default | SWE-bench Pro 59.0, SWE-bench Verified 80.5, MMMU Pro 78.1. Native multimodal across text, image and video | V | Weights on Hugging Face |
| [DeepSeek V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash) | DeepSeek | 284B total / 13B active | 1M | MIT | SWE-bench Verified 79.0 at maximum reasoning effort, against 80.6 for V4-Pro | V | [unsloth GGUF](https://huggingface.co/unsloth/DeepSeek-V4-Flash-GGUF), UD-Q4_K_XL 155.1 GB. [Abliterated GGUF](https://huggingface.co/huihui-ai/Huihui-DeepSeek-V4-Flash-abliterated-ds4-GGUF) |
| [Mistral Small 4 119B](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603) | Mistral AI | 119B total / 6.5B active per the card, 6B per the launch post | 256K | Apache 2.0 | GPQA Diamond 71.2 | V | [unsloth GGUF](https://huggingface.co/unsloth/Mistral-Small-4-119B-2603-GGUF), UD-Q4_K_M 73.8 GB |

Three cautions on this table:

- No model here is "the best open-source model", whatever the coverage says. Moonshot's own card puts Kimi K3 behind GPT-5.6 Sol at 88.8 and Claude Fable 5 at 88.0 on Terminal-Bench 2.1, and behind Claude Fable 5 at 86.6 on FrontierSWE. DeepSeek's card claims the title for V4-Pro, and it was written in April 2026. Artificial Analysis put Kimi K3 top of the open weights at an Intelligence Index of 60, and GLM-5.3 tied that score on 18 August 2026.
- Licences are the least reliable column in secondary coverage. Kimi K3 is not MIT. MiniMax M3 is non-commercial by default. GLM-5.3, released 25 August 2026, dropped MIT for a bespoke `glm-5.3` licence, so "GLM is MIT" stops being true at 5.3.
- "Runs on two GPUs" does not survive contact with the cards. Mistral's release post gives a minimum of four HGX H100s, two HGX H200s, or one DGX B200, and recommends four. DeepSeek's card names no GPU count at all, and the smallest Q4-class GGUF for V4-Flash is 155 GB, which does not fit two 80 GB H100s.

Five more open-weight models landed after the table above, and nobody has read their benchmark numbers into this guide yet. They are listed so the table does not read as complete: [zai-org/GLM-5.3](https://huggingface.co/zai-org/GLM-5.3), 25 August 2026, under a bespoke `glm-5.3` licence. [zai-org/GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash), 320B total and 18B active, MIT, the first natively multimodal GLM-5. [Qwen/Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B), 2.4T total and 95B active, under a custom `qwen3.8-max` licence rather than Apache 2.0. [tencent/Hy4-preview](https://huggingface.co/tencent/Hy4-preview), 770B total and 49B active, Apache 2.0, the largest permissively licensed release of the period. [thinkingmachines/Inkling](https://huggingface.co/thinkingmachines/Inkling), 975B total and 41B active, Apache 2.0, multimodal across image, video and audio.

Do not carry the 77.8 percent SWE-bench Verified score in the previous-generation table below forward to GLM-5.2 or GLM-5.3. It belongs to GLM-5, two verification passes disagreed on whether the current GLM-5 card still shows it, and the GLM-5.3 card has no SWE-bench Verified row at all.

### What This Class Costs to Run Locally

The models above do not fit consumer hardware. These are the smallest published files, read from the repository listings.

| Build | Smallest Useful Quant | File Size | What It Needs |
|-------|-----------------------|-----------|---------------|
| [GLM-5.2 abliterated](https://huggingface.co/huihui-ai/Huihui-GLM-5.2-abliterated-GGUF) | DS4 | 211.1 GB | Multi-GPU server. No Q4_K_M exists |
| [Qwen3.5-397B-A17B abliterated](https://huggingface.co/huihui-ai/Huihui-Qwen3.5-397B-A17B-abliterated-GGUF) | Q3_K, 21 shards | 189.5 GB | Multi-GPU server. No Q4 exists |
| [DeepSeek V4-Flash](https://huggingface.co/unsloth/DeepSeek-V4-Flash-GGUF) | UD-Q4_K_XL | 155.1 GB | Two H200-class cards, with almost no headroom left for the KV cache at long context |
| [Mistral Small 4 119B](https://huggingface.co/unsloth/Mistral-Small-4-119B-2603-GGUF) | UD-Q4_K_M | 73.8 GB | One 80 GB card leaves about 6 GB for the KV cache. Vision needs a separate 0.86 GB mmproj file |
| [Qwen3-Coder-Next abliterated](https://huggingface.co/bartowski/huihui-ai_Qwen3-Coder-Next-abliterated-GGUF) | Q4_K_M | 48.56 GB | 48 GB or more. See Part E |

huihui-ai published a GLM-5.1 abliteration collection and then withdrew it. The repository `huihui-ai/Huihui-GLM-5.1-abliterated-GGUF` returns HTTP 401 and the collection is empty. Use the GLM-5.2 build instead.

### Previous Generation (Not Re-verified in This Revision)

Reported specifications vary between sources. Treat the figures below as orientation, not as precise comparison. Nothing in this table was checked against a model card in the August 2026 revision.

| Family | Developer | Scale (approx.) | Context | Licence | Standing | Local Access |
|--------|-----------|-----------------|---------|---------|----------|--------------|
| DeepSeek V4 (Pro / Flash) | DeepSeek | ~1.6T / ~284B MoE | up to 1M (API) | MIT | Released April 2026. Agentic benchmarks reported alongside the strongest closed models. | Open weights at [deepseek-ai](https://huggingface.co/deepseek-ai). Abliterated GGUF of Flash at [huihui-ai/Huihui-DeepSeek-V4-Flash-abliterated-ds4-GGUF](https://huggingface.co/huihui-ai/Huihui-DeepSeek-V4-Flash-abliterated-ds4-GGUF). |
| DeepSeek V3.2 / V3.2-Speciale | DeepSeek | ~671B MoE | 128K+ | MIT | Released December 2025. V3.2-Speciale reported gold-level results at IMO, IOI, and ICPC 2026. | Open weights at [deepseek-ai](https://huggingface.co/deepseek-ai); smaller R1 distills run locally (Part F). |
| Qwen3.5 / Qwen3.6 Plus | Alibaba | ~397B-A17B MoE | up to 1M | Apache 2.0 | Leading open multilingual and general-chat performance. | [Qwen on Hugging Face](https://huggingface.co/Qwen). Smaller Qwen3 abliterated builds in Part A. |
| GLM-5 / GLM-5.1 | Zhipu AI | ~744B to ~1T, ~40B active | 128K+ | MIT | Strong coding (around 77.8 percent SWE-bench Verified for GLM-5). | [Zhipu / zai-org on Hugging Face](https://huggingface.co/zai-org). GLM-4.7-Flash abliterated runs locally (Part F). |
| Kimi K2.6 | Moonshot AI | ~1.04T, ~32B active, 256K experts | 256K | Permissive (open weights) | Among the largest open-weight models; competitive on reasoning and coding. | [Moonshot AI on Hugging Face](https://huggingface.co/moonshotai). |
| MiniMax M2.7 | MiniMax | ~230B, ~10B active | long-context | Open weights | Efficient activation profile; competitive coding performance. | [MiniMax on Hugging Face](https://huggingface.co/MiniMaxAI). |

Rankings in this class change every few weeks, and each benchmark measures a different thing. Check the current leaderboard for the task you care about before you rely on any single number here.

---

## Part D: Hardware Matching Guide

Find the row that matches the hardware, then read across.

| Machine | Total RAM | Best General | Best Coding | Best Reasoning | Expected Speed |
|---------|-----------|--------------|-------------|----------------|----------------|
| Phone (Android 4 GB) | 4 GB | Gemma 3 270M or Qwen3.5-0.8B Q4_K_M | Qwen2.5-Coder-0.5B | DeepSeek-R1 1.5B | ~5 to 8 tok/s |
| Phone (Android 6 to 8 GB) | 6 to 8 GB | Qwen3.5-2B Q4_K_M | Qwen2.5-Coder-3B | DeepSeek-R1 7B | ~15 to 30 tok/s |
| iPhone 14+ / iPad | 6 to 8 GB | Qwen3.5-2B Q4_K_M | Qwen2.5-Coder-3B | DeepSeek-R1 7B | ~15 to 25 tok/s |
| Raspberry Pi 3/4 (2 to 4 GB) | 2 to 4 GB | Qwen3.5-0.8B Q4_K_M | Qwen2.5-Coder-0.5B | DeepSeek-R1 1.5B | ~5 tok/s |
| Raspberry Pi 5 (8 GB) | 8 GB | Qwen3.5-4B Q4_K_M | Qwen2.5-Coder-3B | DeepSeek-R1 7B | ~8 tok/s |
| Old laptop (no GPU, 4 GB) | 4 GB | Qwen3.5-2B Q4_K_M | Qwen2.5-Coder-1.5B | DeepSeek-R1 1.5B | ~5 to 10 tok/s |
| Standard laptop (no GPU, 8 GB) | 8 GB | Qwen3.5-4B Q4_K_M | Qwen2.5-Coder-7B | DeepSeek-R1 8B | ~8 to 15 tok/s |
| Modern laptop (no GPU, 16 GB) | 16 GB | Qwen3-8B Q5 or Qwen3-14B Q3 | DeepSeek-Coder-V2 Lite 16B (10.36 GB) | DeepSeek-R1 14B | ~10 to 20 tok/s |
| Desktop or workstation (no GPU, 32 GB) | 32 GB | Qwen3.8-27B-Uncensored Q4_K_M (16.81 GB) | Devstral Small 2 24B (14.33 GB) | QwQ-32B or DeepSeek-R1 32B | ~5 to 15 tok/s |
| GPU machine (RTX 3060 12 GB) | 12 GB VRAM | Qwen3-8B Q4 | Qwen2.5-Coder-7B Q4 | DeepSeek-R1 14B | ~40 to 60 tok/s |
| GPU machine (RTX 3090/4090 24 GB) | 24 GB VRAM | Qwen3.8-27B-Uncensored Q4_K_M (16.81 GB) or Gemma 4 31B abliterated Q4_K (18.69 GB) | Qwen3-Coder-30B (18.56 GB) | QwQ-32B or DeepSeek-R1 32B | ~30 to 50 tok/s |
| Multi-GPU or 48 GB and above | 48 GB+ | Qwen3-32B Q8 | Qwen3-Coder-Next abliterated Q4_K_M (48.56 GB) | DeepSeek-R1 70B | ~20 to 40 tok/s |

Speed notes: CPU figures assume modern x86 or Apple Silicon. ARM single-board computers will be slower. GPU figures assume the model fully fits in VRAM.

---

## Quick RAM Formula

```
Required RAM is approximately:
  GGUF file size
  + 2 GB (runtime overhead)
  + (context length in thousands of tokens) x 0.5 MB
```

Examples:
- Qwen3-4B Q4 (2.5 GB) at 4K context: 2.5 + 2 + 2 = about 6.5 GB (fits in 8 GB).
- Qwen3-8B Q4 (5.0 GB) at 4K context: 5.0 + 2 + 2 = about 9 GB (tight in 8 GB, so reduce the context).
- Qwen3-30B-A3B Q4 (18.6 GB) at 4K context: 18.6 + 2 + 2 = about 22.6 GB (requires 24 GB or more).

---

## Hugging Face Links: All Models

### Qwen3 Abliterated (huihui-ai)
| Model | Source | GGUF |
|-------|--------|------|
| Qwen3-0.6B | [huihui-ai/Qwen3-0.6B-abliterated](https://huggingface.co/huihui-ai/Qwen3-0.6B-abliterated) | [DevQuasar GGUF](https://huggingface.co/DevQuasar/huihui-ai.Qwen3-0.6B-abliterated-GGUF) |
| Qwen3-1.7B | [huihui-ai/Qwen3-1.7B-abliterated](https://huggingface.co/huihui-ai/Qwen3-1.7B-abliterated) | [DevQuasar GGUF](https://huggingface.co/DevQuasar/huihui-ai.Qwen3-1.7B-abliterated-GGUF) |
| Qwen3-4B | [huihui-ai/Qwen3-4B-abliterated](https://huggingface.co/huihui-ai/Qwen3-4B-abliterated) | [bartowski GGUF](https://huggingface.co/bartowski/huihui-ai_Qwen3-4B-abliterated-GGUF) |
| Qwen3-8B v2 | [huihui-ai/Huihui-Qwen3-8B-abliterated-v2](https://huggingface.co/huihui-ai/Huihui-Qwen3-8B-abliterated-v2) | [DevQuasar GGUF](https://huggingface.co/DevQuasar/huihui-ai.Qwen3-8B-abliterated-GGUF) |
| Qwen3-14B | [huihui-ai/Qwen3-14B-abliterated](https://huggingface.co/huihui-ai/Qwen3-14B-abliterated) | [bartowski GGUF](https://huggingface.co/bartowski/huihui-ai_Qwen3-14B-abliterated-GGUF) |
| Qwen3-30B-A3B | [huihui-ai/Qwen3-30B-A3B-abliterated](https://huggingface.co/huihui-ai/Qwen3-30B-A3B-abliterated) | via Ollama |
| Qwen3-32B | [huihui-ai/Qwen3-32B-abliterated](https://huggingface.co/huihui-ai/Qwen3-32B-abliterated) | [bartowski GGUF](https://huggingface.co/bartowski/huihui-ai_Qwen3-32B-abliterated-GGUF) |

### Gemma 3 / 3n Abliterated
| Model | Hugging Face GGUF |
|-------|-------------------|
| Gemma 3 270M abliterated | [huihui-ai/gemma3-abliterated (Ollama)](https://ollama.com/huihui_ai/gemma3-abliterated) |
| Gemma 3n E2B abliterated | [mradermacher GGUF](https://huggingface.co/mradermacher/Huihui-gemma-3n-E2B-it-abliterated-GGUF) |
| Gemma 3n E4B abliterated | [mradermacher GGUF](https://huggingface.co/mradermacher/Huihui-gemma-3n-E4B-it-abliterated-GGUF) |
| Gemma 3 4B abliterated | [mlabonne GGUF](https://huggingface.co/mlabonne/gemma-3-4b-it-abliterated-GGUF) |
| Gemma 3 12B abliterated | [mlabonne GGUF](https://huggingface.co/mlabonne/gemma-3-12b-it-abliterated-GGUF) |
| Gemma 3 27B abliterated | [mlabonne GGUF](https://huggingface.co/mlabonne/gemma-3-27b-it-abliterated-GGUF) |

### Small and On-Device
| Model | Source | GGUF |
|-------|--------|------|
| Gemma 3 270M abliterated | [huihui-ai](https://huggingface.co/huihui-ai/Huihui-gemma-3-270m-it-abliterated) | [mradermacher GGUF](https://huggingface.co/mradermacher/Huihui-gemma-3-270m-it-abliterated-GGUF) |
| Qwen3.5-0.8B abliterated | [huihui-ai](https://huggingface.co/huihui-ai/Huihui-Qwen3.5-0.8B-abliterated) | [mradermacher GGUF](https://huggingface.co/mradermacher/Huihui-Qwen3.5-0.8B-abliterated-GGUF) |
| Qwen3.5-2B abliterated | [huihui-ai](https://huggingface.co/huihui-ai/Huihui-Qwen3.5-2B-abliterated) | [mradermacher GGUF](https://huggingface.co/mradermacher/Huihui-Qwen3.5-2B-abliterated-GGUF) |
| Qwen3.5-4B abliterated | [huihui-ai](https://huggingface.co/huihui-ai/Huihui-Qwen3.5-4B-abliterated) | [mradermacher GGUF](https://huggingface.co/mradermacher/Huihui-Qwen3.5-4B-abliterated-GGUF) |
| MiniCPM5-1B abliterated | [huihui-ai](https://huggingface.co/huihui-ai/Huihui-MiniCPM5-1B-abliterated) | [mradermacher GGUF](https://huggingface.co/mradermacher/Huihui-MiniCPM5-1B-abliterated-GGUF) |
| LFM2.5 family | [Liquid AI](https://huggingface.co/LiquidAI) | [LFM2.5-350M abliterated GGUF](https://huggingface.co/mradermacher/LFM2.5-350M-abliterated-GGUF) |
| Needle 2 | [Cactus-Compute/needle2](https://huggingface.co/Cactus-Compute/needle2) | `.cact` binary, not GGUF |
| Gemma 4 E2B / E4B (base) | [google/gemma-4-E2B-it](https://huggingface.co/google/gemma-4-E2B-it) | [E2B abliterated GGUF](https://huggingface.co/mradermacher/Huihui-gemma-4-E2B-it-abliterated-GGUF) |
| LiteRT builds for Google AI Edge Gallery | [litert-community](https://huggingface.co/litert-community) | `.litertlm`, not GGUF |

### Coding Models Abliterated
| Model | Source | GGUF |
|-------|--------|------|
| Qwen3-Coder-Next | [huihui-ai](https://huggingface.co/huihui-ai/Huihui-Qwen3-Coder-Next-abliterated) | [bartowski GGUF](https://huggingface.co/bartowski/huihui-ai_Qwen3-Coder-Next-abliterated-GGUF) |
| Qwen3-Coder-30B | [huihui-ai](https://huggingface.co/huihui-ai/Huihui-Qwen3-Coder-30B-A3B-Instruct-abliterated) | via Ollama |
| Devstral Small 2 24B | [mistralai](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512) | [unsloth GGUF](https://huggingface.co/unsloth/Devstral-Small-2-24B-Instruct-2512-GGUF) |
| DeepSeek-Coder-V2 Lite 16B | [deepseek-ai](https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct) | [bartowski GGUF](https://huggingface.co/bartowski/DeepSeek-Coder-V2-Lite-Instruct-GGUF) |
| Codestral 22B v0.1 | [mistralai](https://huggingface.co/mistralai/Codestral-22B-v0.1) | [bartowski GGUF](https://huggingface.co/bartowski/Codestral-22B-v0.1-GGUF) |
| Qwen2.5-Coder-0.5B | [huihui-ai](https://huggingface.co/huihui-ai/Qwen2.5-Coder-0.5B-Instruct-abliterated) | [bartowski GGUF](https://huggingface.co/bartowski/Qwen2.5-Coder-1.5B-Instruct-abliterated-GGUF) |
| Qwen2.5-Coder-1.5B | [huihui-ai](https://huggingface.co/huihui-ai) | [bartowski GGUF](https://huggingface.co/bartowski/Qwen2.5-Coder-1.5B-Instruct-abliterated-GGUF) |
| Qwen2.5-Coder-3B | [huihui-ai](https://huggingface.co/huihui-ai) | [bartowski GGUF](https://huggingface.co/bartowski/Qwen2.5-Coder-3B-Instruct-abliterated-GGUF) |
| Qwen2.5-Coder-7B | [huihui-ai](https://huggingface.co/huihui-ai/Qwen2.5-Coder-7B-Instruct-abliterated) | [mradermacher GGUF](https://huggingface.co/mradermacher/Qwen2.5-Coder-7B-Instruct-abliterated-i1-GGUF) |
| Qwen2.5-Coder-14B | [huihui-ai](https://huggingface.co/huihui-ai) | via Ollama |
| Qwen2.5-Coder-32B | [huihui-ai](https://huggingface.co/huihui-ai) | [bartowski GGUF](https://huggingface.co/bartowski/Qwen2.5-Coder-32B-Instruct-abliterated-GGUF) |
| WizardLM-CodeLlama-34B | [Eric Hartford](https://huggingface.co/TheBloke/WizardLM-1.0-Uncensored-CodeLlama-34B-GGUF) | [TheBloke GGUF](https://huggingface.co/TheBloke/WizardLM-1.0-Uncensored-CodeLlama-34B-GGUF) |

### Reasoning and Other Abliterated
| Model | Source | GGUF |
|-------|--------|------|
| DeepSeek-R1 (1.5B to 70B) | [huihui-ai](https://huggingface.co/huihui-ai/DeepSeek-R1-Distill-Qwen-7B-abliterated) | via Ollama |
| DeepSeek V4 Flash abliterated | [huihui-ai](https://huggingface.co/huihui-ai/Huihui-DeepSeek-V4-Flash-abliterated-ds4-GGUF) | GGUF (ds4 / llama.cpp) |
| GPT-OSS-20B / 120B | [huihui-ai](https://huggingface.co/huihui-ai/Huihui-gpt-oss-20b-BF16-abliterated) | via Ollama |
| QwQ-32B | [huihui-ai](https://huggingface.co/huihui-ai) | via Ollama |
| Granite 4.1 | [huihui-ai](https://huggingface.co/huihui-ai) | via Ollama |
| Phi-4 / Phi-4-mini | [huihui-ai](https://huggingface.co/huihui-ai) | via Ollama |
| Mistral Small 24B | [huihui-ai](https://huggingface.co/huihui-ai) | via Ollama |
| Dolphin 3.0 8B | [huihui-ai](https://huggingface.co/huihui-ai) | via Ollama |
| Llama 3.3 70B | [huihui-ai](https://huggingface.co/huihui-ai) | via Ollama |

### Frontier-Scale Open-Weight Models
| Family | Organisation Page | Current Model |
|--------|-------------------|---------------|
| DeepSeek | [deepseek-ai](https://huggingface.co/deepseek-ai) | [DeepSeek-V4-Pro](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro), [V4-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash) |
| Qwen | [Qwen](https://huggingface.co/Qwen) | [Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B), [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) |
| GLM (Zhipu AI) | [zai-org](https://huggingface.co/zai-org) | [GLM-5.2](https://huggingface.co/zai-org/GLM-5.2), [GLM-5.3](https://huggingface.co/zai-org/GLM-5.3) |
| Kimi (Moonshot AI) | [moonshotai](https://huggingface.co/moonshotai) | [Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3) |
| MiniMax | [MiniMaxAI](https://huggingface.co/MiniMaxAI) | [MiniMax-M3](https://huggingface.co/MiniMaxAI/MiniMax-M3) |
| Mistral AI | [mistralai](https://huggingface.co/mistralai) | [Mistral-Small-4-119B-2603](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603) |
| Tencent | [tencent](https://huggingface.co/tencent) | [Hy4-preview](https://huggingface.co/tencent/Hy4-preview) |
| Quantised builds | [unsloth](https://huggingface.co/unsloth) | Dynamic GGUFs, `UD-` prefix |

### Dolphin / Wizard-Vicuna (Eric Hartford)
| Model | Hugging Face GGUF |
|-------|-------------------|
| Dolphin 2.0 Mistral 7B | [TheBloke/dolphin-2.0-mistral-7B-GGUF](https://huggingface.co/TheBloke/dolphin-2.0-mistral-7B-GGUF) |
| Dolphin 2.9.1 Llama3 8B | [QuantFactory GGUF](https://huggingface.co/QuantFactory/dolphin-2.9.1-llama-3-8b-GGUF) |
| Dolphin 2.9.3 Nemo 12B | [cognitivecomputations GGUF](https://huggingface.co/cognitivecomputations/dolphin-2.9.3-mistral-nemo-12b-gguf) |
| Wizard-Vicuna-13B | [TheBloke GGUF](https://huggingface.co/TheBloke/Wizard-Vicuna-13B-Uncensored-GGUF) |
| Wizard-Vicuna-30B | [TheBloke GGUF](https://huggingface.co/TheBloke/Wizard-Vicuna-30B-Uncensored-GGUF) |

---

## Summary Recommendations

| Requirement | Recommendation |
|-------------|----------------|
| Multilingual, any hardware | Qwen3.5 abliterated below 4B, Qwen3.8-27B-Uncensored above 16 GB (Part A). |
| Coding, best local option | Qwen3-Coder-Next abliterated (Part E). 48.56 GB at Q4_K_M, 70.6 percent on SWE-bench Verified. |
| Coding, one 24 GB card | Devstral Small 2 24B (Part E). 14.33 GB, 68.0 percent on SWE-bench Verified, Apache 2.0. |
| Coding, 8 GB laptop | Qwen2.5-Coder-7B abliterated (Part E). |
| Coding, minimal footprint | Qwen2.5-Coder-0.5B abliterated (398 MB). |
| Reasoning | DeepSeek-R1 abliterated (Part F). 128K context. |
| Reasoning, multilingual | QwQ-32B abliterated (Part F). |
| OpenAI open-weight | GPT-OSS-20B abliterated (Part F). No successor to gpt-oss has been released. |
| English only, legacy | Dolphin or Wizard-Vicuna (Part C). |
| Smallest footprint that still holds a conversation | LFM2.5-230M (0.153 GB) or Gemma 3 270M (0.253 GB) (Part 0). |
| Smallest tool-calling model | Needle 2 (13.1 MiB) (Part 0). Not a chat model. |
| Best value | Qwen3.5-4B abliterated Q4_K_M (2.71 GB). |
| Uncensored 27B on one 24 GB card | Qwen3.8-27B-Uncensored Q4_K_M (16.81 GB, Apache 2.0) (Part A). |
| Maximum capability on affordable hardware | Qwen3-30B-A3B MoE Q4 (19 GB) or Gemma 4 31B abliterated Q4_K (18.69 GB). |
| Best on Android or iOS | Qwen3.5-2B abliterated (1.27 GB) on a 6 GB phone, Qwen3.5-4B (2.71 GB) on 8 GB (Part M). |
| App for mobile devices | PocketPal AI (Android and iOS), or Google AI Edge Gallery (Android, iOS and macOS). |
| Image input on device | Gemma 4 E2B q4_0 (3.35 GB), which needs an 8 GB phone (Part M). |
| Image input plus tool calling, uncensored | Gemma 4 31B abliterated Q4_K (18.69 GB) (Part B). |
| Shortest path to a running model | LM Studio (Prerequisites). |
| Frontier-scale open alternative to closed models | Kimi K3, GLM-5.2, DeepSeek-V4-Pro, MiniMax M3 (Part G). |
| Commercial use, fewest licence traps | Anything marked Apache 2.0 or MIT. Kimi K3, MiniMax M3, Codestral, Llama and the LFM2.5 line each carry conditions. |

---

Each abliterated build keeps the licence of the model it was derived from. Most are Apache 2.0 or MIT, but Codestral and the Llama family carry usage restrictions: read the licence on the model card before commercial use. The builds ship as GGUF and run under Ollama, LM Studio, llama.cpp, or KoboldCpp. This documentation is for research and education.

Last revised August 2026. Persian edition: [README-complete-guide-FA.md](README-complete-guide-FA.md).
