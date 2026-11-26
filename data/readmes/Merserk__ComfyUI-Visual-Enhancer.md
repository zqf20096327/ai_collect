<div align="center">

# ComfyUI-Visual-Enhancer

Official ComfyUI integration for **[Visual Enhancer](https://github.com/Merserk/dlss5-visual-enhancer)** (`VE_CLI.exe`).  
Bring hardware-accelerated image and video pipelines directly into ComfyUI — with **zero third-party node dependencies**.

[![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=flat-square&logo=windows&logoColor=white)](https://github.com/Merserk/dlss5-visual-enhancer)
[![ComfyUI](https://img.shields.io/badge/ComfyUI-Custom_Nodes-222222?style=flat-square)](#included-nodes)
[![Dependencies](https://img.shields.io/badge/Dependencies-None-2EA043?style=flat-square)](#installation)

<br />

<img width="1439" height="836" alt="Visual Enhancer preview (ComfyUI)" src="https://github.com/user-attachments/assets/2959ab73-ac76-4c92-aea5-44aea53568e2" />

</div>

---

## Quick Start

### Prerequisites
- **[Visual Enhancer](https://github.com/Merserk/dlss5-visual-enhancer)** installed on Windows (default path: `%LOCALAPPDATA%\Programs\Visual Enhancer\VE_CLI.exe`).
- **ComfyUI** (compatible with native `IMAGE` and `VIDEO` nodes).

### Installation
Clone the repository into your `ComfyUI/custom_nodes` directory and restart ComfyUI:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Merserk/ComfyUI-Visual-Enhancer.git
```

All nodes will appear under the **`Visual Enhancer`** category.

### How It Works
- **`Connection` Node**: Automatically detects `VE_CLI.exe` at its default location on open. For custom installs, enter the path in `ve_cli_path` or click **`Select VE_CLI.exe`** directly on the node to browse for it. Once verified, it selects the target GPU and activates all Visual Enhancer nodes.
- **Unified `Image` / `Video` Modes**: Dual-mode nodes let you toggle `mode` between **`Image`** and **`Video`**, while video-only nodes automatically lock `mode` to **`Video`**. Chain them freely with native ComfyUI nodes (`Load Image`, `Preview Image`, `Save Image`, `Load Video`, `Save Video`).

---

## Included Nodes

All nodes live under the **`Visual Enhancer`** menu category.

### Core
| Node | Mode | Description |
| :--- | :--- | :--- |
| **Connection** | `Setup` | Auto-detects `VE_CLI.exe` (`%LOCALAPPDATA%\Programs\Visual Enhancer\VE_CLI.exe`), includes a **`Select VE_CLI.exe`** picker for custom paths, and selects the target GPU. |

### Free Processing
| Node | Mode | Description |
| :--- | :--- | :--- |
| **DLSS Neural Rendering** | `Image` / `Video` | DLSS 5 Neural Rendering with Style (`0`/`1`/`2`), Preset (`A`/`B`), Intensity, Passes, Tone/Structure strength, Automatic Mask, and Optical Flow / External Motion Vectors. |
| **Scaling** | `Image` / `Video` | High-precision spatial scaling (`Lanczos4`, `Spline36`, `Lanczos`, `Area`, `Bicubic`, `Bilinear`, `Nearest`) from `25%` to `1600%`. |
| **DLSS Super Resolution** | `Image` / `Video` | NVIDIA DLSS Super Resolution & DLAA (`DLAA`, `Quality`, `Balanced`, `Performance`, `Ultra Performance`) with presets `Default`, `J`, `K`, `L`, and `M`. |
| **DLSS Ray Reconstruction** | `Image` / `Video` | Native-resolution (`1x`) NVIDIA DLSS Ray Reconstruction with configurable Video NVOFA Optical Flow Quality. |
| **RTX Video Super Resolution** | `Image` / `Video` | NVIDIA RTX Video Super Resolution (`1 - Low` to `4 - Ultra`) with `1x`–`4x` Scale Factor or Custom Dimensions. |
| **RTX Video HDR** | `Video` *(Locked)* | SDR to 10-bit HDR10 video conversion with Contrast, Saturation, Middle Gray, Peak Luminance (`400`–`2000` nits), and Precision controls. |
| **DLSS Frame Generation** | `Video` *(Locked)* | NVIDIA DLSS Frame Generation (`2x`–`8x` Multiplier or Target FPS up to `480` FPS). |
| **FSR Frame Generation** | `Video` *(Locked)* | AMD FidelityFX Super Resolution 3 (FSR 3) Frame Generation (`2x`–`8x` Multiplier or Target FPS). |
| **Video Super Resolution** | `Video` *(Locked)* | NVIDIA VFX Video Super Resolution supporting Standard Upscaling, Denoise, Deblur, and High-Bitrate mode families. |
| **Upscale (Lightweight)** | `Video` *(Locked)* | Fast spatial video upscaling (`4/3x`–`4x`) with adjustable sharpening strength. |
| **Video Frame Generation** | `Video` *(Locked)* | NVIDIA VFX Video Frame Generation (`Low`, `Medium`, `High`) with automatic scene-cut detection. |
| **Coloring** | `Image` / `Video` | 3D `.cube` LUT loader (`33`, `65`, `129` grid sizes) and parametric grading (Exposure, Contrast, Highlights, Shadows, Whites, Blacks, Midtones, Temperature, Tint, Hue Shift, Vibrance, Saturation). |
| **Sharpening** | `Image` / `Video` | **AMD CAS** (Contrast Adaptive Sharpening) and **NVIDIA NIS** (Image Sharpening). |
| **Grain** | `Image` / `Video` | Film grain synthesis with Amount, Size, Color Grain, Tonal Response, Seed, and temporal animation. |

### Subscription Processing (`(Paid)`)

> [!NOTE]
> Listed at the bottom of the node menu. Requires an active Visual Enhancer license signed in via the desktop app.

| Node | Mode | Description |
| :--- | :--- | :--- |
| **Denoising (Paid)** | `Image` / `Video` | **ClearMagnetar** AI Denoising with optional Noise Adaptation translator. |
| **Deblurring (Paid)** | `Image` / `Video` | **FocusPulsar** AI Deblurring for images and videos. |
| **Upscale (Paid)** | `Image` / `Video` | AI Upscaling with **VisionNext**, **RazorNext**, **PeakMagnetar**, **OptiPulsar**, **Lucid**, and **Lucid 2** (`1x`–`8x` for images; `2x`/`4x` or Target Resolution up to `8K` for video). |
| **Frame Interpolation (Paid)** | `Video` *(Locked)* | **Glide** AI Frame Interpolation (`2x`–`8x` Multiplier or Target FPS) with scene-cut detection. |

---

## Example Workflows

Ready-to-run workflows are included in [`example_workflows/`](example_workflows/) and automatically appear in ComfyUI's built-in **Workflow Templates** (Free workflows first, `(Paid)` workflows at the bottom).

<details>
<summary><strong>Single-Feature Showcases (14 Workflows)</strong> — <code>1 Feature = 1 Workflow</code></summary>

| # | Workflow File | Pipeline |
| :-: | :--- | :--- |
| 01 | `01_DLSS_Neural_Rendering.json` | `Load Image` → `DLSS Neural Rendering` → `Save Image` |
| 02 | `02_Scaling.json` | `Load Image` → `Scaling` → `Save Image` |
| 03 | `03_DLSS_Super_Resolution.json` | `Load Image` → `DLSS Super Resolution` → `Save Image` |
| 04 | `04_DLSS_Ray_Reconstruction.json` | `Load Image` → `DLSS Ray Reconstruction` → `Save Image` |
| 05 | `05_RTX_Video_Super_Resolution.json` | `Load Image` → `RTX Video Super Resolution` → `Save Image` |
| 06 | `06_RTX_Video_HDR.json` | `Load Video` → `RTX Video HDR` → `Save Video` |
| 07 | `07_DLSS_Frame_Generation.json` | `Load Video` → `DLSS Frame Generation` → `Save Video` |
| 08 | `08_FSR_Frame_Generation.json` | `Load Video` → `FSR Frame Generation` → `Save Video` |
| 09 | `09_Video_Super_Resolution.json` | `Load Video` → `Video Super Resolution` → `Save Video` |
| 10 | `10_Upscale_Lightweight.json` | `Load Video` → `Upscale (Lightweight)` → `Save Video` |
| 11 | `11_Video_Frame_Generation.json` | `Load Video` → `Video Frame Generation` → `Save Video` |
| 12 | `12_Coloring.json` | `Load Image` → `Coloring` → `Save Image` |
| 13 | `13_Sharpening.json` | `Load Image` → `Sharpening` → `Save Image` |
| 14 | `14_Grain.json` | `Load Image` → `Grain` → `Save Image` |

</details>

<details>
<summary><strong>Multi-Feature Combination Pipelines (3 Workflows)</strong></summary>

| # | Workflow File | Pipeline |
| :-: | :--- | :--- |
| 15 | `15_Combo_Image_Neural_Rendering_Coloring_Sharpening.json` | `Load Image` → `DLSS Neural Rendering` → `Coloring` → `Sharpening` → `Save Image` |
| 16 | `16_Combo_Image_Ray_Reconstruction_DLSS_SR_Grain.json` | `Load Image` → `DLSS Ray Reconstruction` → `DLSS Super Resolution` → `Grain` → `Save Image` |
| 17 | `17_Combo_Video_RTX_Upscale_DLSS_Frame_Gen_HDR.json` | `Load Video` → `RTX Video Super Resolution` → `DLSS Frame Generation` → `RTX Video HDR` → `Save Video` |

</details>

<details>
<summary><strong>Subscription Workflows (5 Workflows — <code>(Paid)</code>)</strong></summary>

| # | Workflow File | Pipeline |
| :-: | :--- | :--- |
| 18 | `18_Denoising (Paid).json` | `Load Image` → `Denoising (Paid)` → `Save Image` |
| 19 | `19_Deblurring (Paid).json` | `Load Image` → `Deblurring (Paid)` → `Save Image` |
| 20 | `20_Upscale (Paid).json` | `Load Image` → `Upscale (Paid)` → `Save Image` |
| 21 | `21_Frame_Interpolation (Paid).json` | `Load Video` → `Frame Interpolation (Paid)` → `Save Video` |
| 22 | `22_Combo_Full_AI_Restoration_and_Upscale (Paid).json` | `Load Image` → `Denoising (Paid)` → `Deblurring (Paid)` → `Upscale (Paid)` → `Coloring` → `Sharpening` → `Save Image` |

</details>

---

## Links & License

- **Visual Enhancer Repository**: [github.com/Merserk/dlss5-visual-enhancer](https://github.com/Merserk/dlss5-visual-enhancer)
- **License**: [Merserk ComfyUI Integration & Source License 1.0](LICENSE)