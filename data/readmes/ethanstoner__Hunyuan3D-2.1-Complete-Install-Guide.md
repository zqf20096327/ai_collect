# Hunyuan3D-2.1 Complete Installation Guide

<div align="center">

**Install Hunyuan3D-2.1 on ComfyUI Portable (Windows, NVIDIA) with one script, or by hand.**

[![Windows](https://img.shields.io/badge/Platform-Windows-blue?style=flat-square)](https://www.microsoft.com/windows)
[![ComfyUI](https://img.shields.io/badge/ComfyUI-v0.3.45-green?style=flat-square)](https://github.com/comfyanonymous/ComfyUI)
[![Python](https://img.shields.io/badge/Python-3.12-yellow?style=flat-square)](https://www.python.org/)
[![PowerShell](https://img.shields.io/badge/PowerShell-5.1%2B-blue?style=flat-square)](https://learn.microsoft.com/powershell/)

</div>

---

## Table of Contents

- [Quick Start](#quick-start)
- [What the installer does](#what-the-installer-does)
- [Already installed? Run the doctor](#already-installed-run-the-doctor)
- [Installer options](#installer-options)
- [GPU requirements](#gpu-requirements)
- [Manual installation](#manual-installation)
- [Troubleshooting](#troubleshooting)
- [What has actually been tested](#what-has-actually-been-tested)
- [Additional resources](#additional-resources)

---

## Quick Start

You need [ComfyUI Portable (NVIDIA) v0.3.45](https://github.com/comfyanonymous/ComfyUI/releases/download/v0.3.45/ComfyUI_windows_portable_nvidia.7z) extracted somewhere, plus [Git for Windows](https://git-scm.com/downloads/win). That is it.

1. Download **`install.ps1`** and **`Install.bat`** from this repo into any folder.
2. Double-click **`Install.bat`**.
3. Wait. It finds ComfyUI, installs everything, downloads the models, and verifies the result.

If ComfyUI is not auto-detected, point at it:

```powershell
.\install.ps1 -ComfyUIPath "D:\ComfyUI_windows_portable"
```

Prefer to see what it would do first? Nothing is written in dry-run mode:

```powershell
.\install.ps1 -DryRun
```

> The script is plain text, around 960 lines, with no network calls beyond Git, pip and the two HuggingFace downloads. Read it before running it. `Install.bat` only sets `-ExecutionPolicy Bypass` for its own process, so your machine's PowerShell policy is left alone.

---

## What the installer does

Every phase is idempotent, so re-running it repairs what is missing and leaves the rest alone.

| Phase | Action | Why it matters |
|---|---|---|
| 0 | Preflight | Checks Git, and reads GPU name plus compute capability from `nvidia-smi` |
| 1 | Locate ComfyUI | Verifies `python_embeded\python.exe`, reads the real torch and ComfyUI versions |
| 2 | Custom nodes | Clones the 4 node packs and pins KJNodes to `37a0973` |
| 3 | Wheels | **Picks the wheel matching your actual torch build** instead of a hardcoded filename |
| 4 | Dependencies | `requirements.txt`, `pytorch_lightning`, `rembg[cpu]`, `timm>=0.9.12` |
| 5 | OpenCV | Installs `opencv-contrib-python` so `cv2.ximgproc` exists |
| 6 | Models | Downloads the dit and vae checkpoints, resumable, verified by exact byte size |
| 7 | Verification | Imports every module and reports a pass/fail table |

Three of these are fixes for things the old version of this guide got wrong or left out. They are explained in [Troubleshooting](#troubleshooting).

---

## Already installed? Run the doctor

If Hunyuan3D is already set up and something is broken, diagnose without changing anything:

```powershell
.\install.ps1 -Doctor
```

Real output from a working install that had one genuine problem:

```
==> Phase 1/7  Locate ComfyUI Portable
    [ OK ] Embedded Python 3.12.10 (cp312)
    [ OK ] torch 2.7.0+cu128 (CUDA 12.8)
    [ OK ] ComfyUI 0.3.45

==> Phase 3/7  Prebuilt wheels (matched to this Python and torch build)
    [ OK ] custom_rasterizer -> custom_rasterizer-0.1.0+torch270.cuda128-cp312-cp312-win_amd64.whl
    [ OK ] mesh_inpaint_processor -> mesh_inpaint_processor-0.0.0-cp312-cp312-win_amd64.whl

==> Phase 7/7  Verification
    [ OK ] ComfyUI-Hunyuan3d-2-1
    [ OK ] ComfyUI-Hunyuan3DWrapper
    [ OK ] ComfyUI-KJNodes pinned at 37a0973
    [WARN] ComfyUI-VideoHelperSuite is not installed (optional). Provides
           VHS_VideoCombine, used by community turntable workflows.
    [ OK ] torch  (2.7.0+cu128)
    [ OK ] custom_rasterizer
    [ OK ] mesh_inpaint_processor
    [ OK ] rembg
    [FAIL] cv2.ximgproc  opencv 4.12.0 lacks ximgproc
```

`-Doctor` never writes. It is safe to run on a setup you care about.

Verification checks the four custom node packs as well as the Python imports,
because a missing or drifted node pack breaks nothing at import time. It only
shows up as a missing node at the moment you load a workflow, which is what
most of the [Troubleshooting](#troubleshooting) entries below are about. A pack
that is required reports `[FAIL]` when it is absent; an optional one reports
`[WARN]`, since not having it just means the workflows that use it will not
run. KJNodes is additionally checked against its pin, because drifting off
`37a0973` is what produces `No module named 'comfy_api.latest'`.

---

## Installer options

| Flag | Effect |
|---|---|
| `-ComfyUIPath <path>` | Point at the ComfyUI Portable root. Accepts the parent folder too. |
| `-Doctor` | Read-only diagnosis. Changes nothing. |
| `-DryRun` | Print every action without executing it. |
| `-SkipModels` | Skip the 7.5 GB checkpoint downloads. |
| `-SkipNodes` | Skip cloning and pinning custom nodes. |
| `-SelfTest` | Run the built-in unit tests for the wheel-selection logic and exit. |

Exit code is `0` when everything passes and `1` when any check fails, so it can be used in a script.

---

## GPU requirements

**Required:** an NVIDIA GPU with **compute capability 8.0 or higher** (Ampere or newer) and **8 GB VRAM** minimum. 12 to 24 GB is much more comfortable.

| Supported | Not supported |
|---|---|
| RTX 30-series (3060 and up) | RTX 20-series (2060, 2070, 2080) |
| RTX 40-series / 50-series | GTX 16-series, GTX 10-series |
| RTX A-series (A2000, A4000, A5000) | Anything older than Ampere |

<details>
<summary><strong>Why older GPUs fail, and what it looks like</strong></summary>

Hunyuan3D-2.1 uses a precompiled CUDA rasterizer (`custom_rasterizer_kernel`). The Windows wheels are built for Ampere and newer only, with no SM 7.5 (Turing) code.

On an unsupported GPU:

- ComfyUI starts normally
- Models load normally
- Generation fails the moment the rasterizer runs, with:

```
CUDA error: no kernel image is available for execution on the device
```

The installer reads your compute capability from `nvidia-smi` in Phase 0 and warns before you spend time downloading 7.5 GB of models.

**Unofficial workaround:** rebuild the rasterizer from source with `TORCH_CUDA_ARCH_LIST=7.5`, or use a workflow that never invokes it. Neither is supported here.

</details>

---

## Manual installation

<details>
<summary><strong>Step-by-step, if you would rather not run a script</strong></summary>

All commands run from the **ComfyUI Portable root**, the folder containing `python_embeded\`, `ComfyUI\` and `run_nvidia_gpu.bat`.

> Always use `python_embeded\python.exe`. Running pip against system Python does nothing for ComfyUI Portable.

### 1. Clone the custom nodes

```bat
cd ComfyUI\custom_nodes

git clone https://github.com/visualbruno/ComfyUI-Hunyuan3d-2-1
git clone https://github.com/visualbruno/ComfyUI-Hunyuan3DWrapper
git clone https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git

git clone https://github.com/kijai/ComfyUI-KJNodes.git
cd ComfyUI-KJNodes
git checkout 37a0973
cd ..\..\..
```

KJNodes must stay pinned to `37a0973` (2025-07-21). Anything newer expects `comfy_api.latest`, which ComfyUI 0.3.45 does not have. **Do not use "Update All" in ComfyUI-Manager**, it will unpin this.

### 2. Install the wheels

The wrapper ships several rasterizer builds. Pick the one matching your torch build, do not assume:

```bat
python_embeded\python.exe -c "import torch; print(torch.__version__)"
```

ComfyUI Portable 0.3.45 reports `2.7.0+cu128`, so the matching wheel is the `torch270.cuda128` one:

```bat
python_embeded\python.exe -m pip install ComfyUI\custom_nodes\ComfyUI-Hunyuan3DWrapper\wheels\custom_rasterizer-0.1.0+torch270.cuda128-cp312-cp312-win_amd64.whl

python_embeded\python.exe -m pip install ComfyUI\custom_nodes\ComfyUI-Hunyuan3d-2-1\hy3dpaint\DifferentiableRenderer\dist\mesh_inpaint_processor-0.0.0-cp312-cp312-win_amd64.whl
```

### 3. Install Python dependencies

```bat
python_embeded\python.exe -m pip install -r ComfyUI\custom_nodes\ComfyUI-Hunyuan3d-2-1\requirements.txt
python_embeded\python.exe -m pip install pytorch_lightning "rembg[cpu]"
python_embeded\python.exe -m pip install --upgrade "timm>=0.9.12"
```

The `[cpu]` on rembg is not optional. See [No onnxruntime backend found](#error-no-onnxruntime-backend-found).

### 4. Install OpenCV contrib

`requirements.txt` installs plain `opencv-python`, which has no `ximgproc`. Do this step **after** step 3:

```bat
python_embeded\python.exe -m pip uninstall -y opencv-python opencv-python-headless
python_embeded\python.exe -m pip install --force-reinstall --no-cache-dir opencv-contrib-python
```

### 5. Download the models

| File | Save as | Folder | Size (bytes) |
|---|---|---|---|
| [dit model.fp16.ckpt](https://huggingface.co/tencent/Hunyuan3D-2.1/blob/main/hunyuan3d-dit-v2-1/model.fp16.ckpt) | `hunyuan3d-dit-v2-1.ckpt` | `ComfyUI\models\diffusion_models\` | 7,366,389,768 |
| [vae model.fp16.ckpt](https://huggingface.co/tencent/Hunyuan3D-2.1/blob/main/hunyuan3d-vae-v2-1/model.fp16.ckpt) | `hunyuan3d-vae-v2-1.ckpt` | `ComfyUI\models\vae\` | 655,648,152 |

Check the byte sizes after downloading. A truncated checkpoint fails later with confusing errors.

### 6. Launch

```bat
run_nvidia_gpu.bat
```

Open `http://127.0.0.1:8188` and load `ComfyUI\custom_nodes\ComfyUI-Hunyuan3d-2-1\workflow_examples\Full_Workflow.json`.

### Do I need the CUDA Toolkit and Visual C++ Build Tools?

Usually no. Every component above installs from a prebuilt wheel, and no compilation happens on a normal install. Install [CUDA 12.6](https://developer.nvidia.com/cuda-12-6-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=11&target_type=exe_local) and the [Visual C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) (MSVC v143, Windows SDK, CMake) only if pip tries to build something from source on your machine, or if you intend to rebuild the rasterizer yourself.

</details>

---

## Troubleshooting

Search this section for the exact error text you got.

### Error: `No onnxruntime backend found`

```
No onnxruntime backend found.
Please install rembg with CPU or GPU support:
    pip install "rembg[cpu]"  # for CPU
```

**Cause:** current `rembg` releases do not depend on onnxruntime themselves. `pip install rembg` therefore installs a package that raises this the moment anything imports it. Older guides (including earlier versions of this one) told you to run plain `pip install rembg`.

**Fix:**

```bat
python_embeded\python.exe -m pip install "rembg[cpu]"
```

Use `"rembg[gpu]"` instead if you want onnxruntime-gpu, but then its CUDA and cuDNN expectations have to match your machine. CPU is fine here, background removal is not the slow part.

---

### Error: `ModuleNotFoundError: No module named 'cv2.ximgproc'`

**Cause:** `ximgproc` only ships in `opencv-contrib-python`. The node pack's `requirements.txt` installs plain `opencv-python`, so a by-the-book install ends up without it.

**Fix**, from the ComfyUI Portable root:

```bat
python_embeded\python.exe -m pip uninstall -y opencv-python opencv-python-headless
python_embeded\python.exe -m pip install --force-reinstall --no-cache-dir opencv-contrib-python
```

Removing `opencv-python-headless` as well is deliberate. All three packages install into the same `cv2/` directory, so whichever is installed last owns it. Clearing them first makes the outcome independent of install order.

Then restart ComfyUI and confirm:

```bat
python_embeded\python.exe -c "import cv2; print(hasattr(cv2,'ximgproc'))"
```

> Note: `opencv-contrib-python` 4.12.0.88 requires `numpy<2.3.0`. If pip warns about a numpy conflict, pin numpy below 2.3.

---

### Error: `Prompt has failed validation: VHS_VideoCombine`

**Cause:** the workflow you loaded uses [VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite), which is not part of Hunyuan3D. None of the 9 bundled example workflows use this node, so this comes from a community or YouTube workflow, typically a turntable render.

**Fix:**

```bat
cd ComfyUI\custom_nodes
git clone https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite.git
```

Restart ComfyUI. The installer clones this by default.

---

### Error: `No module named 'comfy_api.latest'`

**Cause:** KJNodes is newer than ComfyUI 0.3.45.

**Fix:**

```bat
cd ComfyUI\custom_nodes\ComfyUI-KJNodes
git checkout 37a0973
```

Do not update KJNodes afterwards, and do not use "Update All" in ComfyUI-Manager.

---

### Missing nodes: `INTConstant`, `StringConstant`, `SetNode`, `GetNode`

**Cause:** these four come from KJNodes, and `Full_Workflow.json` needs all of them. Seeing them missing means KJNodes failed to import, usually the `comfy_api.latest` problem above.

**Fix:** check the ComfyUI console for `IMPORT FAILED: ComfyUI-KJNodes`, then re-clone and pin:

```bat
cd ComfyUI\custom_nodes
rmdir /s /q ComfyUI-KJNodes
git clone https://github.com/kijai/ComfyUI-KJNodes.git
cd ComfyUI-KJNodes
git checkout 37a0973
```

---

### Missing nodes: `AuraSR.AuraSRUpscaler`, `InvSRSampler`, `LoadInvSRModels`

**Cause:** two of the bundled example workflows use optional upscalers that are not part of this install.

| Workflow | Needs |
|---|---|
| `Mesh_Texturing_UpscaleWithAuraSR.json` | [ComfyUI-AuraSR](https://github.com/GreenLandisaLie/AuraSR-ComfyUI) |
| `Mesh_Texturing_UpscaleWithInvSR.json` | [ComfyUI-InvSR](https://github.com/yuvraj108c/ComfyUI-InvSR) |

**Fix:** install the matching node pack, or use `Full_Workflow.json` / `Mesh_Texturing.json`, which need neither.

---

### Error: `DLL load failed while importing custom_rasterizer_kernel`

```
ImportError: DLL load failed while importing custom_rasterizer_kernel:
The specified module could not be found.
```

**Cause, if you hit this while testing by hand:** `custom_rasterizer` links against torch's CUDA DLLs and cannot load unless torch is imported first. This is a healthy install:

```bat
python_embeded\python.exe -c "import torch, custom_rasterizer; print('ok')"
```

and this fails on the *same* install, misleadingly:

```bat
python_embeded\python.exe -c "import custom_rasterizer"
```

ComfyUI always imports torch first, so this particular failure does not affect normal use. Test with the first form before concluding the wheel is broken.

**Cause, if ComfyUI itself raises it:** the installed wheel does not match your torch build. Check what you have and reinstall the matching wheel:

```bat
python_embeded\python.exe -c "import torch; print(torch.__version__)"
dir ComfyUI\custom_nodes\ComfyUI-Hunyuan3DWrapper\wheels
```

`ComfyUI-Hunyuan3DWrapper` currently ships three builds:

| Wheel | For |
|---|---|
| `custom_rasterizer-0.1-cp312-cp312-win_amd64.whl` | untagged fallback |
| `custom_rasterizer-0.1.0+torch260.cuda126-...whl` | torch 2.6.0 + cu126 |
| `custom_rasterizer-0.1.0+torch270.cuda128-...whl` | torch 2.7.0 + cu128 |

`.\install.ps1` picks this automatically. `.\install.ps1 -SelfTest` runs the unit tests for that selection logic.

---

### Error: `CUDA error: no kernel image is available for execution on the device`

Your GPU is older than Ampere. See [GPU requirements](#gpu-requirements). ComfyUI starting successfully does not mean the GPU is supported.

---

### Generation is fine but the mesh has no texture

Texturing needs `cv2.ximgproc` and `mesh_inpaint_processor`. Run `.\install.ps1 -Doctor` and check both report `[ OK ]`.

---

## What has actually been tested

Being explicit about this, because "it should work" is not the same as "it was run".

**Verified on a real machine** (ComfyUI Portable 0.3.45, Python 3.12.10, torch 2.7.0+cu128, RTX 4090, Windows 11):

- `-Doctor` and `-DryRun` complete against a real install and modify nothing
- Wheel selection picks `torch270.cuda128` for torch 2.7.0+cu128, and `cp312` mesh_inpaint
- `import torch, custom_rasterizer` succeeds while `import custom_rasterizer` alone fails on that same install
- KJNodes pin detection reports `37a0973`
- Checkpoint byte sizes match the values in this README
- `-SelfTest` passes 17 of 17

**Verified in an isolated Python 3.12 venv:**

- `pip install rembg` produces a package where `import rembg` fails with "No onnxruntime backend found"
- `pip install "rembg[cpu]"` fixes it
- With `opencv-python` and `opencv-python-headless` 4.12.0.88 installed, `cv2.ximgproc` is absent
- After removing both and installing `opencv-contrib-python`, `cv2.ximgproc` imports

**Not tested, be aware:**

- A complete fresh install from an empty ComfyUI Portable, end to end
- The model download path executing against HuggingFace (URLs and sizes were confirmed by HTTP headers only)
- The pre-Ampere compute-capability warning firing on real pre-Ampere hardware
- Any GPU other than an RTX 4090, and any ComfyUI version other than 0.3.45

Reports from other setups are welcome, please open an issue with your `.\install.ps1 -Doctor` output.

---

## Additional resources

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- [Hunyuan3D-2.1 on Hugging Face](https://huggingface.co/tencent/Hunyuan3D-2.1)
- [ComfyUI-Hunyuan3d-2-1 node pack](https://github.com/visualbruno/ComfyUI-Hunyuan3d-2-1)
- [ComfyUI-Hunyuan3DWrapper](https://github.com/visualbruno/ComfyUI-Hunyuan3DWrapper)

---

<div align="center">

If this saved you an afternoon, a star helps other people find it.

</div>
