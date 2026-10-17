<p align="center">
  <img src="./assets/readme/hero.svg" width="100%" alt="ComfyUI-PrunaVAED native LTX-2.3 video VAE loader and decode benchmark">
</p>

<p align="center">
  <a href="https://github.com/Comfy-Org/ComfyUI"><img alt="ComfyUI custom node" src="https://img.shields.io/badge/ComfyUI-custom_node-111318?style=flat-square"></a>
  <a href="https://huggingface.co/PrunaAI/PrunaVAED"><img alt="PrunaVAED for LTX 2.3" src="https://img.shields.io/badge/LTX--2.3-PrunaVAED-8B5CF6?style=flat-square"></a>
  <img alt="No extra Python dependencies" src="https://img.shields.io/badge/dependencies-none-35C99A?style=flat-square">
  <a href="./LICENSE"><img alt="GPL version 3 license" src="https://img.shields.io/badge/license-GPL--3.0-667085?style=flat-square"></a>
</p>

## What it does

**ComfyUI-PrunaVAED** loads [PrunaAI/PrunaVAED](https://huggingface.co/PrunaAI/PrunaVAED) from ComfyUI's standard `models/vae` directory and exposes it as a normal ComfyUI `VAE`.

It replaces the **LTX-2.3 video VAE** in a workflow. It does **not** replace the LTX audio VAE or the LTX transformer.

```text
LTX-2.3 latent ──> Load PrunaVAED ──> VAE Decode ──> video frames
                         │
                         └── standard ComfyUI VAE output
```

- Native ComfyUI model and VRAM offloading path
- Standard `VAE` output
- Compatible with regular `VAE Decode`
- Compatible with LTX tiled decode nodes that call the standard VAE interface
- Video encoding support for image-to-video workflows
- No Diffusers runtime dependency
- No automatic downloads, telemetry, or background network requests

> [!IMPORTANT]
> PrunaVAED is a **video VAE only**. Continue loading `LTX23_audio_vae_bf16.safetensors` with the regular LTX audio VAE loader.

## Nodes

### Load PrunaVAED

Loads and validates the PrunaVAED checkpoint.

| Port | Direction | Type | Description |
|---|---|---|---|
| `vae_name` | input | filename | Selects a checkpoint from `ComfyUI/models/vae` |
| `device` | input | choice | `main_device` runs on the active accelerator; `cpu` runs entirely on CPU |
| `weight_dtype` | input | choice | Selects `bf16`, `fp16`, or `fp32` for VAE weights and compute |
| `VAE` | output | `VAE` | Standard ComfyUI VAE object for video encode and decode |

Internally, the loader remaps the upstream Diffusers-style state dictionary to the native ComfyUI LTX VAE layout and instantiates the pruned decoder channel structure. Unsupported checkpoints fail with an explicit format error.

`main_device` with `bf16` is the recommended configuration and matches the upstream PrunaVAED usage. Choose `cpu` only when freeing accelerator VRAM is more important than decode speed. `fp32` offers the widest CPU compatibility but uses twice the model memory of `bf16`/`fp16`. `fp16` support and performance depend on the selected device and PyTorch build.

### Benchmark LTX VAE vs PrunaVAED

Measures both decoders against the **same latent tensor**.

| Port | Direction | Type | Description |
|---|---|---|---|
| `samples` | input | `LATENT` | One shared LTX-2.3 latent |
| `reference_vae` | input | `VAE` | Stock LTX-2.3 video VAE |
| `pruna_vae` | input | `VAE` | VAE returned by `Load PrunaVAED` |
| `warmup_runs` | input | integer | Untimed warm-up passes |
| `timed_runs` | input | integer | Passes used for the median |
| `report` | output | string | Per-run timings, medians, and decode speedup |

CUDA is synchronized around every timed pass. Model loading is excluded after warm-up, and the final report is also written to the ComfyUI console.

## Installation

### 1. Install the custom node

Clone or copy this repository into:

```text
ComfyUI/custom_nodes/ComfyUI-PrunaVAED
```

No additional Python packages are required.

### 2. Install the model

Download the official checkpoint from the [PrunaVAED model repository](https://huggingface.co/PrunaAI/PrunaVAED/tree/main/vae):

```text
vae/diffusion_pytorch_model.safetensors
```

Rename it and place it in the standard ComfyUI VAE directory:

```text
ComfyUI/models/vae/PrunaVAED.safetensors
```

### 3. Restart ComfyUI

Add **Load PrunaVAED**, select `PrunaVAED.safetensors`, and connect its output wherever the workflow expects the LTX-2.3 video VAE.

Leave `device` on `main_device` and `weight_dtype` on `bf16` for the recommended GPU or accelerator configuration. Select `cpu` to keep VAE execution off the accelerator; use `fp32` if the CPU or PyTorch build does not execute reduced-precision operators efficiently.

## Workflow wiring

### Text-to-video

```text
LTX sampler output ──> VAE Decode
                           ▲
Load PrunaVAED ────────────┘
```

### Image-to-video

Use the same `VAE` output for both source-image encoding and final video decoding.

### Audio

Keep the existing audio path unchanged:

```text
LTX23_audio_vae_bf16.safetensors ──> LTX Audio VAE Decode
```

## Reproducible decode benchmark

Drag [`examples/PrunaVAED_benchmark.json`](./examples/PrunaVAED_benchmark.json) into ComfyUI.

The workflow:

1. Creates one synthetic LTX-2.3 latent at `1280 × 768`, `121` frames.
2. Sends that exact latent to the stock and Pruna decoders.
3. Runs warm-up passes.
4. Measures synchronized decode passes.
5. Prints median latency and calculated speedup.

This isolates VAE decode performance. It does not benchmark sampling, text encoding, audio generation, file encoding, or total workflow time.

## Performance expectations

The [upstream PrunaVAED model card](https://huggingface.co/PrunaAI/PrunaVAED) reports approximately **1.7× faster video decoding** and **about 50% lower peak VRAM** in its tested configuration.

Those numbers were measured upstream on an NVIDIA H100 using BF16 and mostly full-frame decoding without tiling or rolling. Results can differ substantially with:

- GPU architecture
- resolution and frame count
- ComfyUI's internal chunking
- spatial or temporal tiling
- dtype and VRAM mode
- model offloading and concurrent models

Only the latent-to-video decode stage is accelerated. If sampling dominates the workflow, the total generation time may change only slightly.

### Local benchmark results

The benchmark node was also validated on an NVIDIA GeForce RTX 4090 using BF16, one warm-up pass, three synchronized timed passes, and median reporting.

| Latent | Decoded video | Stock LTX-2.3 VAE | PrunaVAED | Speedup |
|---|---|---:|---:|---:|
| `1 × 128 × 16 × 24 × 40` | `121 × 768 × 1280` | `3,373.9 ms` | `1,898.8 ms` | **1.78×** |
| `1 × 128 × 51 × 24 × 40` | `401 × 768 × 1280` | `12,149.0 ms` | `6,177.9 ms` | **1.97×** |

This reduced measured decode latency by approximately **43.7%** for 121 frames and **49.1%** for 401 frames.

<details>
<summary>Raw synchronized timings</summary>

```text
121 frames
Stock LTX-2.3 VAE: 3373.9, 3431.8, 3286.8 ms
PrunaVAED:          1843.4, 1899.6, 1898.8 ms

401 frames
Stock LTX-2.3 VAE: 12149.0, 12209.6, 12025.3 ms
PrunaVAED:          6132.3, 6177.9, 6267.5 ms
```

</details>

## Compatibility

| Component | Status |
|---|---|
| LTX-2.3 video latents | Supported |
| Standard ComfyUI `VAE Decode` | Supported |
| LTX tiled decode nodes | Supported through the standard VAE interface |
| Image-to-video VAE encode | Supported |
| LTX audio VAE | Separate; not replaced |
| Other video model latent formats | Not supported |
| Diffusers installation | Not required |

The loader is architecture-specific and intentionally rejects arbitrary VAE checkpoints.

### Windows and Linux

The node contains no hard-coded drive letters, path separators, shell commands, or Windows-only APIs. Model discovery is handled by ComfyUI's `folder_paths`, while device placement and offloading use ComfyUI's model-management layer.

- **Windows:** validated with ComfyUI Portable and CUDA
- **Linux:** supported by the same platform-neutral ComfyUI code path
- **NVIDIA / ROCm:** synchronization is used when PyTorch exposes the device as `cuda`
- **CPU / MPS:** the benchmark skips CUDA synchronization and uses the active ComfyUI device

A native Linux GPU benchmark has not yet been run in this development environment, but no OS-specific runtime path exists in the node.

## Sources and attribution

- [PrunaAI/PrunaVAED](https://huggingface.co/PrunaAI/PrunaVAED) — model weights, architecture description, upstream benchmark, and usage terms
- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) — host application, VAE interface, model management, and LTX VAE primitives
- [Lightricks/LTX-2](https://github.com/Lightricks/LTX-2) — LTX-2 model architecture and license
- [Lightricks/ComfyUI-LTXVideo](https://github.com/Lightricks/ComfyUI-LTXVideo) — LTX-specific ComfyUI workflows and tiled decode integrations

## License

The custom-node source code in this repository is distributed under the [GNU General Public License v3.0](./LICENSE).

The PrunaVAED model weights are **not included** and remain subject to the [LTX-2 Community License Agreement](https://github.com/Lightricks/LTX-2/blob/main/LICENSE). Review the upstream model and license terms before use or redistribution.
