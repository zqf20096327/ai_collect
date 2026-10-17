# ComfyUI Installer for AMD Ryzen AI Max 395 (gfx1151)

This repository contains installation scripts and documentation for running **ComfyUI** with GPU acceleration on AMD Ryzen AI Max 395 APUs (Strix Halo architecture, gfx1151).

## Table of Contents

- [Overview](#overview)
- [The Problem](#the-problem)
- [The Solution](#the-solution)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Technical Details](#technical-details)
- [Download Links & Wheel Sources](#download-links--wheel-sources)
- [Sources & References](#sources--references)

---

## Overview

The AMD Ryzen AI Max 395 features an integrated Radeon GPU based on the **RDNA 3.5** architecture, identified as **gfx1151** (Strix Halo). This is a relatively new GPU architecture that requires specific PyTorch wheels compiled with gfx1151 support.

### Hardware Specifications

| Component | Details |
|-----------|---------|
| APU | AMD Ryzen AI Max 395 |
| GPU Architecture | RDNA 3.5 (gfx1151) |
| GPU Name | AMD Radeon Graphics (Strix Halo) |
| Device ID | 0x1586 |
| Shared Memory | Up to 96GB (system RAM) |

---

## The Problem

### Symptoms

When attempting to run ComfyUI with standard ROCm PyTorch wheels, users encounter several errors:

**Error 1: No GPU detected**
```
RuntimeError: No HIP GPUs are available
```

**Error 2: Architecture mismatch (after GPU is detected)**
```
HIP error: invalid device function
```

**Error 3: Missing library in nightly wheels**
```
ModuleNotFoundError: Unknown rocm library 'hipsparselt'
```

### Root Cause Analysis

The issue occurs at multiple levels of the ROCm stack:

```
Layer                          Status
─────────────────────────────────────────────────────
Kernel Driver (amdgpu)         ✅ Working
Display/OpenGL (Mesa)          ✅ Working
ROCm SMI (rocm-smi)            ✅ Working
HSA Runtime (rocminfo)         ⚠️  May show errors
HIP Compute                    ❌ "invalid device function"
PyTorch                        ❌ Kernels don't match gfx1151
```

**The core problem**: Official PyTorch ROCm wheels from `https://download.pytorch.org/whl/rocm6.x` are compiled for these GPU architectures:

- gfx900, gfx906, gfx908, gfx90a (Vega/MI series)
- gfx1030 (RDNA 2)
- gfx1100 (RDNA 3)

**gfx1151 (Strix Halo) is NOT included** in the official wheels.

When PyTorch attempts to run a CUDA/HIP kernel on gfx1151 using wheels compiled for other architectures, it fails with `invalid device function` because the GPU instruction set doesn't match.

### The hipsparselt Error

The CloudFront nightly wheels (`d2awnip2yjpvqn.cloudfront.net/v2/gfx1151/`) have a **bug** in the `rocm_sdk` package. It tries to preload `hipsparselt`, a library that doesn't exist for gfx1151:

```python
# This fails because hipsparselt isn't available for gfx1151
ModuleNotFoundError: Unknown rocm library 'hipsparselt'
```

This is why we use the **self-contained wheel** from scottt instead.

---

## The Solution

### Self-Contained PyTorch Wheel (Recommended)

The install script uses [@scottt's self-contained wheel](https://github.com/scottt/rocm-TheRock/releases/tag/v6.5.0rc-pytorch) which:

- Bundles all required ROCm libraries internally
- Doesn't rely on the broken `rocm_sdk` package
- Is compiled specifically for gfx1151
- **Requires Python 3.11** (not 3.12)

### Wheel Comparison

| Wheel Source | Status | Python | Issue |
|--------------|--------|--------|-------|
| `pytorch.org/whl/rocm6.x` | ❌ Broken | Any | No gfx1151 kernels |
| `d2awnip2yjpvqn.cloudfront.net` | ❌ Broken | 3.12 | hipsparselt missing |
| **scottt/rocm-TheRock** | ✅ Working | **3.11** | Self-contained |

### The Fix Applied

The install script:

1. **Requires Python 3.11** - The working wheel is only available for Python 3.11
2. **Uses scottt's self-contained wheel** - Avoids the broken rocm_sdk package
3. **Prevents torch overwrite** - ComfyUI's `requirements.txt` includes `torch` which would replace our working wheel
4. **Verifies torch version** - Checks and reinstalls if the wrong version was installed

### Why Dependencies Break Things

#### Problem 1: requirements.txt

ComfyUI's `requirements.txt` includes:
```
torch
torchvision
torchaudio
```

When pip installs these, it pulls from PyPI/the default index, which gives you `torch==2.6.0+rocm6.1` - the **broken** wheel without gfx1151 support.

#### Problem 2: Transitive Dependencies (kornia)

Even after filtering torch from requirements.txt, packages like **kornia** have `torch>=2.0.0` as a dependency. When pip resolves kornia's dependencies, it downloads the default CUDA torch from PyPI:

```
Collecting torch>=2.0.0 (from kornia>=0.7.1...)
  Downloading torch-2.6.0-cp311-cp311-manylinux1_x86_64.whl
```

This results in **torch-2.6.0+cu124** (CUDA version) being installed, which fails with:
```
RuntimeError: Found no NVIDIA driver on your system
```

#### The Solution

The script handles these issues by:
1. Installing scottt's wheel first
2. Using `--no-deps` when installing torchvision/torchaudio
3. Filtering torch packages from requirements.txt
4. **Installing kornia with `--no-deps`** to prevent torch dependency resolution
5. **Force reinstalling scottt's wheel as the FINAL step** - guarantees correct wheel
6. Verifying the correct version and failing if wrong

---

## Requirements

### System Requirements

- **OS**: Ubuntu 22.04 / 24.04 LTS (or compatible Linux distribution)
- **Kernel**: 6.x with amdgpu driver
- **Python**: **3.11** (required - see installation below)
- **RAM**: 32GB+ recommended (shared with GPU)
- **Storage**: 20GB+ free space

### Python 3.11 Installation (Ubuntu 24.04)

Ubuntu 24.04 ships with Python 3.12 by default. You need to install Python 3.11 from the deadsnakes PPA:

```bash
# Add the deadsnakes PPA
sudo add-apt-repository -y ppa:deadsnakes/ppa

# Update package lists
sudo apt update

# Install Python 3.11
sudo apt install -y python3.11 python3.11-venv python3.11-dev

# Verify installation
python3.11 --version
# Should output: Python 3.11.x
```

### ROCm Requirements

The following ROCm tools should be installed and functional:

```bash
# Check ROCm tools
rocm-smi -i          # Should show your GPU
rocminfo             # May show warnings on gfx1151 (non-fatal)
```

### Install ROCm (if not already installed)

```bash
# Add AMD ROCm repository (Ubuntu 24.04)
wget https://repo.radeon.com/amdgpu-install/latest/ubuntu/noble/amdgpu-install_6.3.60300-1_all.deb
sudo apt install ./amdgpu-install_6.3.60300-1_all.deb
sudo amdgpu-install --usecase=rocm

# Add user to required groups
sudo usermod -aG video,render $USER
# Log out and back in for group changes to take effect
```

---

## Installation

### Quick Start

```bash
# 1. Install Python 3.11 (if not already installed)
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.11 python3.11-venv python3.11-dev

# 2. Clone this repository
git clone <this-repo> ~/Projects/comfyui
cd ~/Projects/comfyui

# 3. Remove any existing broken venv
rm -rf ~/ComfyUI/venv

# 4. Run the installer
chmod +x install_comfyui_amd_ryzen.sh
./install_comfyui_amd_ryzen.sh
```

### What the Script Does

1. **Checks Python version** - Verifies Python 3.11 is available
2. **Validates ROCm installation** - Checks for rocminfo, rocm-smi
3. **Tests GPU visibility** - Ensures rocm-smi can see your GPU
4. **Installs system dependencies** - git, python3-venv, build-essential
5. **Clones/updates ComfyUI** - From official GitHub repository
6. **Creates Python 3.11 virtual environment** - Isolated from system Python
7. **Removes conflicting packages** - Old torch/CUDA/ROCm/NVIDIA wheels
8. **Installs scottt's self-contained gfx1151 wheel** - From GitHub releases
9. **Installs dependencies with `--no-deps`** - Prevents pip from pulling in CUDA torch
10. **Removes any NVIDIA packages** - Cleans up any accidentally installed CUDA dependencies
11. **Force reinstalls the gfx1151 torch wheel** - Ensures correct version after all deps installed
12. **Creates launcher script** - `run_comfy_amd_ryzen_ai.sh`
13. **Validates PyTorch HIP** - Tests GPU compute functionality

### Post-Installation Fixes

If you see import errors about missing modules after installation, install them manually:

```bash
source ~/ComfyUI/venv/bin/activate

# Common missing dependencies (due to --no-deps installation strategy)
pip install typing-inspection kornia_rs httpx

# If huggingface-hub version conflict:
pip install "huggingface-hub<1.0,>=0.34.0"
```

### Environment Variables

You can customize the installation:

```bash
# Use a different install directory
COMFY_DIR=~/my-comfyui ./install_comfyui_amd_ryzen.sh

# Use a specific Python binary (must be 3.11)
PYTHON_BIN=/usr/bin/python3.11 ./install_comfyui_amd_ryzen.sh
```

---

## Usage

### Starting ComfyUI

```bash
cd ~/ComfyUI
./run_comfy_amd_ryzen_ai.sh
```

Then open your browser to: **http://localhost:8188/**

### Launcher Script Environment

The launcher script (`run_comfy_amd_ryzen_ai.sh`) sets these environment variables:

```bash
unset CUDA_VISIBLE_DEVICES    # CRITICAL: Remove any empty CUDA_VISIBLE_DEVICES
HIP_VISIBLE_DEVICES=0         # Use first AMD GPU
AMD_LOG_LEVEL=0               # Reduce log noise
GPU_MAX_HEAP_SIZE=100         # Allow full VRAM usage
GPU_MAX_ALLOC_PERCENT=100     # Allow large allocations
```

> ⚠️ **Important**: The `unset CUDA_VISIBLE_DEVICES` is critical! PyTorch ROCm uses CUDA API names internally. If `CUDA_VISIBLE_DEVICES` is set to empty (even from your `.bashrc`), PyTorch won't see any GPUs. The run script now explicitly unsets this variable.

### Debugging

If you encounter issues, enable debug mode by editing the launcher:

```bash
# Uncomment these lines in run_comfy_amd_ryzen_ai.sh:
export AMD_SERIALIZE_KERNEL=3
export HIP_LAUNCH_BLOCKING=1
```

---

## Troubleshooting

### "No HIP GPUs are available"

**Cause**: PyTorch can't see the GPU via HIP.

**Solutions**:

1. **Check if `CUDA_VISIBLE_DEVICES` is set to empty** - This is the most common cause!
   ```bash
   # Check current value
   echo $CUDA_VISIBLE_DEVICES

   # If it shows empty (but the variable exists), that's the problem!
   # BAD - This hides the GPU from PyTorch ROCm:
   export CUDA_VISIBLE_DEVICES=""

   # GOOD - Unset it completely:
   unset CUDA_VISIBLE_DEVICES
   export HIP_VISIBLE_DEVICES=0
   ```

2. **Try a fresh terminal** - Your `.bashrc` or other startup scripts might set `CUDA_VISIBLE_DEVICES=""`. Open a completely new terminal and try again.

3. **Check for the variable in startup files**:
   ```bash
   grep -r "CUDA_VISIBLE_DEVICES" ~/.bashrc ~/.profile ~/.zshrc 2>/dev/null
   ```

4. Check user groups: `groups $USER` should include `video` and `render`

5. Check device permissions: `ls -la /dev/dri/`

6. Verify ROCm: `rocm-smi -i`

```bash
# Fix permissions
sudo usermod -aG video,render $USER
# Then log out and back in
```

### "invalid device function"

**Cause**: PyTorch wheels don't include gfx1151 kernels.

**Solution**: Ensure you're using scottt's self-contained wheel. Re-run the install script.

```bash
# Verify correct PyTorch version
source ~/ComfyUI/venv/bin/activate
python -c "import torch; print(torch.__version__)"
# Should show: 2.7.0a0+gitbfd8155 (self-contained wheel)
# NOT: 2.6.0+rocm6.1 or 2.7.1+rocm7.10.0a... (broken wheels)
```

### "Unknown rocm library 'hipsparselt'"

**Cause**: Using the CloudFront nightly wheels which have a broken rocm_sdk package.

**Solution**: The script now uses scottt's self-contained wheel which doesn't have this issue. If you see this error:

```bash
# Remove the broken venv and reinstall
rm -rf ~/ComfyUI/venv
cd ~/Projects/comfyui
./install_comfyui_amd_ryzen.sh
```

### "python3.11 not found"

**Cause**: Python 3.11 is not installed.

**Solution**: Install from deadsnakes PPA:

```bash
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.11 python3.11-venv python3.11-dev
```

### Wrong torch version installed

**Cause**: Dependencies (requirements.txt or packages like kornia) overwrote the gfx1151 wheel.

**Symptoms**:
```bash
python -c "import torch; print(torch.__version__)"
# Shows: 2.6.0+rocm6.1  (WRONG - standard ROCm, no gfx1151)
# Shows: 2.6.0+cu124    (WRONG - CUDA version, needs NVIDIA)
# Should show: 2.7.0a0+gitbfd8155  (CORRECT - scottt's gfx1151 wheel)
```

**Solution**: The updated script now force-reinstalls the correct wheel as the final step. If it still fails:

```bash
source ~/ComfyUI/venv/bin/activate

# Uninstall all torch packages
pip uninstall -y torch torchvision torchaudio

# Reinstall scottt's wheel
pip install --force-reinstall --no-deps \
  https://github.com/scottt/rocm-TheRock/releases/download/v6.5.0rc-pytorch/torch-2.7.0a0+gitbfd8155-cp311-cp311-linux_x86_64.whl

# Reinstall torchvision/torchaudio without dependencies
pip install --no-deps torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.1
```

### "Found no NVIDIA driver on your system"

**Cause**: CUDA version of torch was installed instead of ROCm/HIP version.

**Symptoms**:
```bash
python -c "import torch; print(torch.__version__)"
# Shows: 2.6.0+cu124 or similar with "cu" in version
```

**Solution**: Same as above - reinstall scottt's wheel. The "cu" in the version indicates CUDA.

### "rocminfo" shows errors

**Cause**: HSA runtime issues on gfx1151 (common, often non-fatal).

**Note**: This may not prevent PyTorch from working. The gfx1151 wheels handle HSA differently.

### torch.cuda.is_available() returns False (but worked before)

**Cause**: The virtual environment got corrupted by conflicting packages. This often happens when pip installs dependencies that pull in CUDA torch, overwriting the gfx1151 wheel.

**Symptoms**:
```bash
python -c "import torch; print(torch.cuda.is_available())"
# Returns: False (even though torch.__version__ looks correct)
```

**Solution**: Create a fresh virtual environment:

```bash
# Remove corrupted venv
rm -rf ~/ComfyUI/venv

# Create fresh venv with Python 3.11
cd ~/ComfyUI
python3.11 -m venv venv
source venv/bin/activate

# Install scottt's wheel first
pip install --upgrade pip wheel setuptools
pip install https://github.com/scottt/rocm-TheRock/releases/download/v6.5.0rc-pytorch/torch-2.7.0a0+gitbfd8155-cp311-cp311-linux_x86_64.whl

# Install other dependencies with --no-deps to prevent torch replacement
pip install --no-deps torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.1
pip install numpy pillow scipy aiohttp yarl pyyaml tqdm psutil requests
pip install --no-deps kornia spandrel einops transformers tokenizers sentencepiece safetensors torchsde
pip install typing-inspection kornia_rs httpx "huggingface-hub<1.0,>=0.34.0" packaging regex trampoline
pip install pydantic pydantic-settings annotated-types pydantic-core python-dotenv
pip install alembic SQLAlchemy greenlet Mako av opencv-python-headless
pip install comfyui-frontend-package comfyui-workflow-templates comfyui-embedded-docs

# Verify
python -c "import torch; print('CUDA:', torch.cuda.is_available())"
# Should return: CUDA: True
```

### torchaudio errors (libhipblas.so.2 not found)

**Cause**: The ROCm 6.1 torchaudio package requires `libhipblas.so.2`, but scottt's torch wheel uses ROCm 6.5 which has a different library version.

**Symptoms**:
```
OSError: libhipblas.so.2: cannot open shared object file: No such file or directory
Cannot import nodes_audio.py module for custom nodes
```

**Impact**: Audio-related features in ComfyUI won't work (ACE model, MMAudio VAE, Whisper). **All image/video generation features work normally.**

**Solution**: This is expected and can be safely ignored. To suppress the warnings:

```bash
source ~/ComfyUI/venv/bin/activate
pip uninstall -y torchaudio
```

### Out of Memory (OOM) errors

**Cause**: Strix Halo shares system RAM with the GPU.

**Solutions**:
1. Close other applications
2. Use smaller models
3. Reduce batch sizes in ComfyUI
4. Increase swap space

---

## Technical Details

### Architecture Comparison

| Architecture | Family | Examples | ROCm Support |
|-------------|--------|----------|--------------|
| gfx900 | Vega | Vega 56/64 | Official |
| gfx906 | Vega | MI50 | Official |
| gfx908 | CDNA | MI100 | Official |
| gfx90a | CDNA2 | MI210/250 | Official |
| gfx1030 | RDNA2 | RX 6800 | Official |
| gfx1100 | RDNA3 | RX 7900 | Official |
| **gfx1151** | **RDNA3.5** | **Strix Halo** | **Community** |

### Why Python 3.11?

The self-contained wheel from scottt is only built for Python 3.11:
- `torch-2.7.0a0+gitbfd8155-cp311-cp311-linux_x86_64.whl`

The Python 3.12 wheels from the CloudFront nightly index have the broken `rocm_sdk` package that tries to load `hipsparselt`. Until this is fixed upstream, Python 3.11 is required.

### Self-Contained vs SDK-Based Wheels

| Aspect | Self-Contained (scottt) | SDK-Based (CloudFront) |
|--------|------------------------|------------------------|
| ROCm Libraries | Bundled in wheel | External rocm_sdk package |
| hipsparselt | Not required | Required (but missing) |
| Size | Larger (~700MB) | Smaller wheel + SDK |
| Python | 3.11 only | 3.12 |
| Status | ✅ Working | ❌ Broken |

### AOTriton Support

The gfx1151 wheels include AOTriton with experimental gfx1151 support, enabling:
- `torch.nn.functional.scaled_dot_product_attention`
- Flash Attention (experimental)
- Optimized transformer operations

---

## Download Links & Wheel Sources

### Recommended: scottt's Self-Contained Wheels (Working)

These wheels bundle all ROCm libraries internally and don't require the broken `rocm_sdk` package.

| Platform | Python | Wheel | Download |
|----------|--------|-------|----------|
| **Linux** | **3.11** | torch-2.7.0a0+gitbfd8155 | [Download](https://github.com/scottt/rocm-TheRock/releases/download/v6.5.0rc-pytorch/torch-2.7.0a0+gitbfd8155-cp311-cp311-linux_x86_64.whl) |
| Windows | 3.12 | torch-2.7.0a0+git3f903c3 | [Download](https://github.com/scottt/rocm-TheRock/releases/download/v6.5.0rc-pytorch/torch-2.7.0a0+git3f903c3-cp312-cp312-win_amd64.whl) |
| Windows | 3.12 | torchvision-0.22.0+9eb57cd | [Download](https://github.com/scottt/rocm-TheRock/releases/download/v6.5.0rc-pytorch/torchvision-0.22.0+9eb57cd-cp312-cp312-win_amd64.whl) |
| Windows | 3.12 | torchaudio-2.6.0a0+1a8f621 | [Download](https://github.com/scottt/rocm-TheRock/releases/download/v6.5.0rc-pytorch/torchaudio-2.6.0a0+1a8f621-cp312-cp312-win_amd64.whl) |

**Release Page**: [github.com/scottt/rocm-TheRock/releases/tag/v6.5.0rc-pytorch](https://github.com/scottt/rocm-TheRock/releases/tag/v6.5.0rc-pytorch)

### CloudFront Nightly Wheels (Broken - hipsparselt issue)

> ⚠️ **WARNING**: These wheels have a bug in the `rocm_sdk` package that tries to load `hipsparselt` which doesn't exist for gfx1151. Use scottt's wheels instead.

**Index URL**: `https://d2awnip2yjpvqn.cloudfront.net/v2/gfx1151/`

Available packages (if the hipsparselt issue gets fixed):

| Package | Versions Available | Python |
|---------|-------------------|--------|
| torch | 2.7.0a0 - 2.10.0a0 | 3.11, 3.12, 3.13 |
| torchvision | 0.22.0 - 0.25.0a0 | 3.11, 3.12, 3.13 |
| torchaudio | 2.7.0 - 2.10.0a0 | 3.11, 3.12, 3.13 |
| pytorch-triton-rocm | Various | 3.11, 3.12, 3.13 |
| rocm-sdk | Various | 3.11, 3.12 |

Browse packages: [d2awnip2yjpvqn.cloudfront.net/v2/gfx1151/](https://d2awnip2yjpvqn.cloudfront.net/v2/gfx1151/)

### Official PyTorch ROCm Wheels (No gfx1151 support)

> ❌ **NOT WORKING FOR gfx1151**: These wheels don't include gfx1151 kernels.

**Index URL**: `https://download.pytorch.org/whl/rocm6.x`

Only useful for torchvision/torchaudio when installed with `--no-deps`.

### Direct Download Commands

```bash
# Linux (Python 3.11) - RECOMMENDED
pip install https://github.com/scottt/rocm-TheRock/releases/download/v6.5.0rc-pytorch/torch-2.7.0a0+gitbfd8155-cp311-cp311-linux_x86_64.whl

# Windows (Python 3.12)
pip install https://github.com/scottt/rocm-TheRock/releases/download/v6.5.0rc-pytorch/torch-2.7.0a0+git3f903c3-cp312-cp312-win_amd64.whl
pip install https://github.com/scottt/rocm-TheRock/releases/download/v6.5.0rc-pytorch/torchvision-0.22.0+9eb57cd-cp312-cp312-win_amd64.whl
pip install https://github.com/scottt/rocm-TheRock/releases/download/v6.5.0rc-pytorch/torchaudio-2.6.0a0+1a8f621-cp312-cp312-win_amd64.whl

# CloudFront nightly (if hipsparselt issue gets fixed)
pip install torch torchvision torchaudio --index-url https://d2awnip2yjpvqn.cloudfront.net/v2/gfx1151/
```

---

## Sources & References

### Official Documentation

- [ROCm Installation Guide](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/)
- [PyTorch ROCm Compatibility](https://rocm.docs.amd.com/en/latest/compatibility/ml-compatibility/pytorch-compatibility.html)
- [ComfyUI GitHub](https://github.com/comfyanonymous/ComfyUI)

### Community Resources (gfx1151 Support)

- [ROCm/TheRock Discussion #655](https://github.com/ROCm/TheRock/discussions/655) - Self-contained gfx1151 PyTorch wheels
- [ROCm/TheRock Discussion #244](https://github.com/ROCm/TheRock/discussions/244) - gfx1151 PyTorch working with hipBLASLt
- [scottt/rocm-TheRock Releases](https://github.com/scottt/rocm-TheRock/releases/tag/v6.5.0rc-pytorch) - **Working wheel download**
- [weiziqian/rocm_pytorch_docker_gfx1151](https://github.com/weiziqian/rocm_pytorch_docker_gfx1151) - Docker setup for gfx1151
- [CloudFront gfx1151 Index](https://d2awnip2yjpvqn.cloudfront.net/v2/gfx1151/) - Nightly wheels (currently broken)

### Issue Trackers

- [ROCm Issue #5643](https://github.com/ROCm/ROCm/issues/5643) - hipBLASLt on gfx1151
- [ROCm Issue #5404](https://github.com/ROCm/ROCm/issues/5404) - AOTriton for gfx1151
- [hipBLASLt Issue #1243](https://github.com/ROCm/hipBLASLt/issues/1243) - Architecture support

### Articles

- [PyTorch with ROCm 7 for Windows on Strix Halo](https://medium.com/@GenerationAI/pytorch-with-rocm-7-for-windows-on-amd-ryzen-ai-max-395-strix-halo-radeon-8060s-gfx1151-1ba069edc2c4) - Wei Lu on Medium
- [Strix Halo LLM Tracker](https://llm-tracker.info/_TOORG/Strix-Halo) - Comprehensive status tracking

---

## Files in This Repository

| File | Description |
|------|-------------|
| `install_comfyui_amd_ryzen.sh` | Main installation script |
| `run_comfy_amd_ryzen_ai.sh` | Generated launcher (after install) |
| `rocm_comfyui_diagnostics.sh` | ROCm diagnostic tool |
| `cleanup_rocm_pytorch_comfyui.sh` | Cleanup script |
| `README.md` | This documentation |

---

## Known Limitations

1. **Python 3.11 required** - The working wheel is only available for Python 3.11
2. **VRAM limitation** - Some users report PyTorch can only use ~32GB even with 64GB available
3. **hipBLASLt fallback** - Performance may be reduced as hipBLASLt falls back to hipBLAS
4. **Flash Attention** - Experimental support, may not work for all models
5. **torchaudio incompatibility** - The ROCm 6.1 torchaudio requires `libhipblas.so.2` which may not be available; audio features (ACE, MMAudio, Whisper) will be disabled but image/video generation works fine
6. **CUDA_VISIBLE_DEVICES interference** - If your shell has `CUDA_VISIBLE_DEVICES=""` set (common for NVIDIA setups), it will hide the GPU from PyTorch ROCm. The run script now uses `unset CUDA_VISIBLE_DEVICES` to handle this
7. **Venv corruption** - Installing packages can sometimes corrupt the venv by replacing the gfx1151 torch wheel with CUDA torch. Solution: delete venv and recreate from scratch

---

## Contributing

If you find issues or improvements for gfx1151 support:

1. Test changes on actual Ryzen AI Max hardware
2. Document any new findings
3. Submit issues to the appropriate upstream projects

## License

Scripts in this repository are provided as-is for educational and personal use. ComfyUI and PyTorch have their own respective licenses.

---

**Last Updated**: December 2025
**Tested On**: AMD Ryzen AI Max 395, Ubuntu 24.04, ROCm 6.5/7.1, Python 3.11
**Working Wheel**: `torch-2.7.0a0+gitbfd8155-cp311-cp311-linux_x86_64.whl` from scottt
**Status**: ✅ ComfyUI running with GPU acceleration on gfx1151
