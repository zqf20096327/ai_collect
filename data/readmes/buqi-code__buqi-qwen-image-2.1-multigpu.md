# Qwen-Image 2.1 Multi-GPU for ComfyUI

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

A ComfyUI custom node for Qwen-Image 2.1 multi-GPU inference, using mathematically equivalent Ulysses sequence parallelism to accelerate text-to-image and multi-reference image editing across 2, 4, or 8 NVIDIA GPUs. It supports native BF16, INT8 ConvRot, FP8 loading, and distributed prefix caching.

The node returns a standard ComfyUI `MODEL`. Existing Qwen Image 2.1 / QwenImage21 workflows keep their official text encoder, conditioning, sampler, cache, VAE, editing, and RGBA nodes; replace only `Load Diffusion Model` with `Qwen-Image 2.1 Multi-GPU Loader (Ulysses SP)`.

## Features

- Standard ComfyUI workflow and UI support; no external inference server.
- 1, 2, 4, and 8 GPU execution on Linux or WSL2 with NCCL.
- Qwen-Image 2.1 text-to-image and multi-reference editing.
- Block-causal attention equivalent to the native ComfyUI implementation.
- Per-rank lossless prefix KV cache for editing workflows, with `auto`, `gpu`, `cpu`, and `off` storage modes.
- Uneven token splits without padding.
- DynamicVRAM in the main ComfyUI process; worker GPUs keep one full DiT resident for predictable collectives.
- Bounded startup and collective timeouts with automatic group teardown after failure.

## Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/buqi-code/buqi-qwen-image-2.1-multigpu
```

Restart ComfyUI after installation. Multi-GPU mode requires ComfyUI commit `c194dd00` or newer because that commit introduced the Qwen-Image 2.1 attention hook used by sequence parallelism. No tagged ComfyUI release through `v0.37.4` contains that commit, so do not rely on a `>=0.37.0` version check. Native Windows is not supported because PyTorch NCCL is required; use Linux or WSL2.

## Models

ModelScope repository: `Comfy-Org/Qwen-Image-2.1`

ModelScope and Hugging Face both host the native ComfyUI files. Place one DiT, one text encoder, and the VAE in the matching folders:

| Component | File | Size | Status |
|---|---|---:|---|
| BF16 DiT | `diffusion_models/qwen_image_2.1_bf16.safetensors` | 13.25 GB | tested reference |
| INT8 ConvRot DiT | `diffusion_models/qwen_image_2.1_int8_convrot.safetensors` | 6.76 GB | tested, fastest on 2×L20 |
| BF16 text encoder | `text_encoders/qwen3vl_8b_bf16.safetensors` | 16.33 GB | tested |
| INT8 ConvRot text encoder | `text_encoders/qwen3vl_8b_int8_convrot.safetensors` | 8.71 GB | tested |
| W4A8 text encoder | `text_encoders/qwen3vl_8b_w4a8.safetensors` | 5.88 GB | tested, lowest VRAM |
| VAE | `vae/qwen_image_2.1_vae_bf16.safetensors` | 644 MB | tested |

Use `weight_dtype=default` for native INT8 ConvRot checkpoints. The loader can also cast the BF16 DiT with `fp8_e4m3fn_fast`, but it was slightly slower than native INT8 on L20. Diffusers-sharded FP8 repositories and GGUF files are not directly compatible with this loader. GGUF requires a separate GGUF loader and its distributed worker integration has not been implemented.

## Workflow use

Load one of the files under `examples/`, or edit an existing official Qwen-Image 2.1 workflow:

1. Replace `Load Diffusion Model` with `QwenImage21SPUNETLoader`.
2. Select the Qwen-Image 2.1 diffusion checkpoint. Use `weight_dtype=default` for native INT8.
3. Select `world_size` from the `1/2/4/8` dropdown.
4. Leave `devices=auto`, or enter physical CUDA IDs such as `0,1,2,3`.
5. Keep the official `TextEncodeQwenImage21`, `QwenImage21Cache`, sampler, and `VAEDecode` nodes.

The supplied UI workflows expose DiT, text encoder, VAE, DiT cast, seed, CFG, negative prompt, GPU count, and GPU IDs at the top level. Cache dtype remains visible but SP supports only `default`; INT8/INT4 cache storage is separate from model quantization and remains rejected.

The first selected device must be ComfyUI's primary visible GPU. For eight GPUs, launch ComfyUI with all eight devices visible and select `world_size=8`; each rank computes 4 of the model's 32 attention heads.

Ready-to-submit API examples include BF16 T2I, INT8 T2I, and image editing. Copy your edit source to `ComfyUI/input/reference.png` before submitting the image-edit example. Prompt refinement is disabled by default in the UI edit workflow so the optional 9B prompt-enhancer model is not required.

## Precision

The implementation does not quantize activations or change the denoising algorithm. NCCL all-to-all only redistributes sequence rows and attention heads. BF16 kernel tiling changes produce small floating-point differences, so outputs are not promised to be bit-identical.

Measured on 2× NVIDIA L20 46GB with ComfyUI `7fbcfa8b`:

| Workload | Single GPU | SP2 | Speedup |
|---|---:|---:|---:|
| 1024², 5 steps, warm | 3.222s | 2.344s | 1.37× |
| 2048², 3 steps, warm | 10.611s | 7.021s | 1.51× |
| 1024², 25 steps, decoded image | 17.231s | 12.000s | 1.44× |

For the 1024² 25-step comparison with identical prompt and seed, decoded RGBA output measured 43.04dB PSNR and 0.25/255 mean absolute pixel difference. A real 512px one-step DiT comparison measured relative L2 0.0239 and cosine 0.99975 for T2I, and relative L2 0.0144 and cosine 0.99990 for editing. These differences come from BF16 GEMM and attention tiling changes, not approximate attention or reduced-step methods.

Eight-rank CPU/Gloo parity covers T2I, single-reference editing, multi-reference editing, prefix-cache reuse, batch size 2, and uneven sequence splits. Physical 8-GPU performance is not claimed until tested on an eight-GPU host.

### Quantized benchmark

Measured end-to-end on 2× NVIDIA L20, including VAE decode and PNG save. Stable time is the mean of the last two warm runs unless noted.

| Configuration | Resolution / steps | GPUs | Stable time | Result |
|---|---:|---:|---:|---|
| BF16 DiT + INT8 text encoder | 1024² / 25 | 2 | 12.000s | reference |
| INT8 ConvRot DiT + INT8 text encoder | 1024² / 25 | 1 | 10.285s | tested |
| INT8 ConvRot DiT + INT8 text encoder | 1024² / 25 | 2 | **8.947s** | fastest tested production preset |
| BF16 DiT cast with `fp8_e4m3fn_fast` + INT8 text encoder | 1024² / 25 | 2 | 8.988s | tested |
| INT8 ConvRot DiT + W4A8 text encoder | 1024² / 25 | 2 | 8.940s | same steady DiT speed, lower encoder VRAM |
| INT8 ConvRot DiT + W4A8 text encoder | 512² / 5 | 2 | **0.562s** | fastest tested preview |
| INT8 ConvRot DiT + W4A8 text encoder | 2048² / 3 | 2 | 7.175s | tested |

The INT8 SP2 production preset is about 1.15× faster than INT8 single-GPU and 1.34× faster than the measured BF16 SP2 path. Text encoder quantization mainly changes prompt-encoding memory and cold-start time; repeated denoising speed is governed by the DiT. Chinese, English, and Japanese prompts were each decoded successfully. Quantized checkpoints are not numerically equivalent to BF16.

## GPU compatibility

| GPU | Compatibility | Recommended model | Notes |
|---|---|---|---|
| NVIDIA L20 48GB | physically validated, 2 GPUs | BF16 or INT8 | Test host has PCIe/PHB and no CUDA P2P; NCCL host transport still works. |
| GeForce RTX 4090 24GB | architecture-compatible, not physically tested | INT8 DiT + W4A8/INT8 encoder | Each worker keeps a full DiT resident. Prefer 1024px first; large 2K jobs depend on available VRAM. |
| GeForce RTX 5090 32GB | architecture-compatible, not physically tested | INT8 or BF16 | Requires a Blackwell-capable NVIDIA driver and PyTorch/CUDA build. |
| RTX PRO 5000 Blackwell 48/72GB | architecture-compatible, not physically tested | BF16 or INT8 | Use full physical GPUs; MIG is not validated for this NCCL path. |

Linux or WSL2 with CUDA and NCCL is required. NVLink is not required, but PCIe/P2P topology can materially change scaling. Mixed GPU models are allowed only when every rank can load the same checkpoint; execution is limited by the slowest GPU and the smallest VRAM capacity, so homogeneous cards are recommended.

## Cache behavior

`QwenImage21Cache` remains part of the standard workflow. The lossless `default` dtype is supported:

- `auto`: GPU when sufficient free VRAM exists, otherwise CPU.
- `gpu`: keep each rank's head-sharded prefix K/V on its GPU.
- `cpu`: keep the cache in host memory and transfer per block.
- `off`: recompute the prefix each step.

INT8 and INT4 prefix-cache storage are intentionally rejected in SP mode because they are lossy. A warm 512px single-reference edit measured 0.877s with the default cache versus 1.342s with cache disabled for five steps.

## Current limits

- Static and dynamic LoRA patches are rejected until worker patch synchronization is enabled.
- Qwen-Image 2.1 ControlNet is not supported by the current native ComfyUI model path.
- Do not combine this node with ComfyUI threaded MultiGPU clones.
- `torch.compile` wrappers and transformer block replacement patches are rejected when they cannot be synchronized safely.
- Only 2×L20 has received physical multi-GPU acceptance so far; 4/8 GPU support is covered by distributed parity tests.

## Environment variables

- `QWEN_IMAGE21_SP_DEVICES=0,1,2,3`
- `QWEN_IMAGE21_SP_STARTUP_TIMEOUT=300`
- `QWEN_IMAGE21_SP_COLLECTIVE_TIMEOUT=120`
- `QWEN_IMAGE21_SP_LOGDIR=/tmp`

## Validation

```bash
COMFYUI_ROOT=/path/to/ComfyUI python -m unittest discover -s tests -v
COMFYUI_ROOT=/path/to/ComfyUI torchrun --standalone --nproc-per-node=2 tests/test_current_api.py
COMFYUI_ROOT=/path/to/ComfyUI torchrun --standalone --nproc-per-node=8 tests/test_current_api.py
```

The model weights remain subject to the Qwen Research License. This repository's source code is MIT licensed.
