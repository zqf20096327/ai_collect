# ComfyUI LongCat Avatar

This repository adapts the official Avatar 1.5 and Avatar 1.6 pipelines to ComfyUI. It focuses on CUDA inference, Whisper-large-v3 audio conditioning, distill LoRA inference (the selected distill LoRA for Avatar 1.5, the official DMD and OPSD LoRA pair inside the checkpoint for Avatar 1.6), single-audio avatar generation for both versions, multi-audio generation for Avatar 1.5, single-file `.safetensors` DiT loading for Avatar 1.5, official sharded and official sharded INT8 DiT loading for both versions, and bounded automatic download of known official checkpoint assets.

<p align="center">
  <a href="https://github.com/meituan-longcat/LongCat-Video">Official LongCat-Video Repo</a> |
  <a href="https://meigen-ai.github.io/LongCat-Video-Avatar-1.5-Page/">Official Avatar 1.5 Project Page</a>
</p>

<div align="center">
  <video src="https://github.com/user-attachments/assets/dbad0a81-c961-4cef-9a18-09377de2397a" width="900"></video>
</div>

## Last Update

<details>

<summary><strong>Avatar 1.6 support and prebuilt INT8 attention in 0.5.0</strong></summary>

- Added Avatar 1.6 as a second supported model version. The model node has two new weight modes, `official_v16_sharded` and `official_v16_int8_sharded`, with selector cards, a pinned and bounded automatic download of the official Avatar 1.6 checkpoint, and the official DMD and OPSD LoRA pair loaded automatically from the checkpoint, so no separate LoRA file is needed. Existing Avatar 1.5 workflows and their saved values keep working unchanged.
- Added the per-step LoRA mix of Avatar 1.6 to the Sampler: `lora_mix_steps` (default 4) and `lora_mix_alpha` (default 1.0). Both are ignored for Avatar 1.5. While a mix is active, a continuation does not use the KV cache, so videos with several segments take longer.
- `LongCat Avatar Audio Encode` has a new `model_version` input (default `avatar-v1.5`), because Avatar 1.6 prepares its audio differently. The Sampler stops with a message that names the fix when the audio was encoded for the other version.
- Resident ComfyUI models are now unloaded when LongCat needs the memory, and reload when they are used again. Before, the memory request never matched a resident model.
- Added the Avatar 1.6 example workflow (`example_workflows/longcat-avatar1.6.json`, INT8, with `mask_frame_range` 0). The release-archive audit, the Registry metadata validation, and the browser tests now cover it and the new controls.
- Added the opt-in `comfy_kitchen_int8` attention mode. It runs Avatar self and audio attention on the prebuilt INT8 kernel of comfy-kitchen on supported NVIDIA CUDA hardware; on the tested Windows host it built no Triton code at run time. Text attention stays on PyTorch SDPA, and the mode falls back to SDPA with one warning per reason when the kernel is unavailable. `auto` and the other modes behave as before.
- Observed generation on a CUDA host (2026-11-26, Windows, ComfyUI Core 0.46.0, one NVIDIA RTX PRO 6000 Blackwell GPU): Avatar 1.6 INT8 and Avatar 1.5 INT8 single audio completed with one and with two segments using `attention_mode=sdpa`. With `comfy_kitchen_int8`, Avatar 1.6 INT8 completed one segment and Avatar 1.5 INT8 two segments, and the denoising loop of a segment took about 63 to 69 s instead of about 100 to 111 s with `sdpa`, at the same peak GPU memory. These are completion checks and timings on that one host, not a lip-sync, identity, or image-quality claim.
- Not verified on that host: generation with `sageattn` (the value saved in both example workflows), Avatar 1.6 BF16 generation, two-speaker and 720p generation with Avatar 1.6, and macOS or MLX with Avatar 1.6.

</details>

<details>

<summary><strong>Current ComfyUI compatibility and runtime reliability update in 0.3.0</strong></summary>

- Validated all nine nodes and the example workflow against current ComfyUI Core and both bundled and tracked frontend versions.
- Hardened official sharded checkpoint loading with immutable source revisions plus index, shard, tensor-key, dtype, shape, and byte-total checks.
- Refreshed the model source selector and Audio Crop preview for current frontend widgets, panels, subgraphs, and Vue Nodes.
- Made Avatar 1.5 sampler controls reflect the effective distill values, kept image-free `at2v`, and added preferred native ComfyUI `AUDIO` muxing with a bounded legacy-path fallback.
- Coordinated the self-managed LongCat model lifecycle with ComfyUI memory pressure handling and consolidated shared single/multi-avatar runtime behavior.
- Added deterministic release-archive checks and clarified that Registry or Git custom-node directories—not standalone wheels—are the supported distribution format.

</details>

<details>

<summary><strong>Desktop installation and workflow reliability refreshed in 0.2.5</strong></summary>

- Fixed fresh-install startup failures by removing the undeclared Loguru dependency and loading optional Triton-backed block-sparse attention only when selected.
- Aligned Python, dependency, and ComfyUI compatibility metadata while preserving the host-managed PyTorch and CUDA stack.
- Added a complete nine-node Registry inventory and versioned workflow attribution so missing workflows identify `comfyui-longcat-avatar` instead of an unknown pack.
- Verified all nine nodes and the example workflow on ComfyUI Core 0.22.3 / Frontend 1.43.18 and Core 0.27.1 / Frontend 1.45.20.

</details>

<details>

<summary><strong>Apple Silicon MLX testing branch</strong></summary>

A macOS inference branch, `macOS-MLX`, is available for Apple Silicon MLX testing. If you have a suitable Mac, please try it and share feedback through GitHub issues or pull requests.

</details>

## Validated Compatibility

Historical install/workflow checks remain verified on ComfyUI Core 0.22.3 / Frontend 1.43.18 and Core 0.27.1 / Frontend 1.45.20. On 2026-08-09, the current contract was also validated on Core 0.31.0 with its bundled Frontend 1.48.7 and the tracked Frontend 1.50.3. That current-host scope covers startup, node-schema, workflow, and browser behavior; it is not a model-generation or performance claim.

Windows dependency/startup cells passed on Python 3.12.13 and Python 3.13.9. CUDA validation was limited to startup, node registration, and a tiny allocation on the tested host; it did not load a LongCat checkpoint or measure generation. Optional FlashAttention, xFormers, and SageAttention installations remain host-specific and were not added to the default dependency set.

The Avatar 1.6 example workflow and the new controls were also checked in that same browser harness (Core 0.31.0, with Frontend 1.48.7 and 1.50.3). The workflow loads with all its LongCat nodes, its saved widget values and the new inputs reach the queued prompt, both Avatar 1.6 selector cards can be selected, and the Avatar 1.5 workflow still loads with its saved values. This is a browser and schema check, not a generation claim.

Generation was observed separately, on a different host, on 2026-11-26: Windows, ComfyUI Core 0.46.0 (frontend package 1.59.11, as the server reported it), Python 3.12.12, PyTorch 2.9.1+cu130, and one NVIDIA RTX PRO 6000 Blackwell Workstation Edition GPU. The checkpoint files were present on the host beforehand, so these runs do not cover the node's automatic download. The bundled example workflows were run with only these changes: the input image and audio, the audio crop length, the debug-mode switch, `attention_mode=sdpa`, and, for Avatar 1.5, the INT8 weight mode:

| Run | Weight mode | Segments | Result |
| --- | --- | --- | --- |
| Avatar 1.5 INT8, single audio | `official_int8_sharded` | 1 | Completed: 75 frames at 25 fps (3.0 s) |
| Avatar 1.6 INT8, single audio | `official_v16_int8_sharded` | 1 | Completed: 75 frames at 25 fps (3.0 s) |
| Avatar 1.6 INT8, single audio | `official_v16_int8_sharded` | 2 | Completed: 150 frames at 25 fps (6.0 s) |
| Avatar 1.5 INT8, single audio | `official_int8_sharded` | 2 | Completed: 150 frames at 25 fps (6.0 s) |

Each output had the frame count that the segment arithmetic expects, a non-constant and moving picture, and an audio track of the video's length. Those are completion and sanity checks; they are not a lip-sync, identity, or image-quality claim.

Every run in this table used `attention_mode=sdpa`. Both bundled example workflows save `sageattn`, and generation with `sageattn` was not verified on that host (SageAttention's Triton kernels build a small helper library the first time they run on Windows). Avatar 1.6 BF16 generation, two-speaker generation, 720p generation with Avatar 1.6, and macOS or MLX with Avatar 1.6 were not run.

With comfy-kitchen 0.2.42 on the same Windows CUDA host, `comfy_kitchen_int8` completed Avatar 1.6 INT8 single-audio generation in one segment (75 frames at 25 fps) and Avatar 1.5 INT8 single-audio generation in two segments (150 frames at 25 fps). The Avatar 1.5 run used the continuation KV cache for the second segment. Both runs exercised the prebuilt kernel for self and audio attention and used SDPA for text attention. With the same settings on that host, the denoising loop took 68.6 s for the Avatar 1.6 segment and 68.7 s and 62.9 s for the two Avatar 1.5 segments, against 111.1 s, 111.0 s, and 99.9 s with `sdpa`, and peak allocated GPU memory was unchanged. These completion and sanity checks leave lip-sync, identity, and image-quality stability unmeasured.

## Table of Contents

- [Last Update](#last-update)
- [Validated Compatibility](#validated-compatibility)
- [Feature Status](#feature-status)
- [Installation](#installation)
- [Model Files](#model-files)
- [Inference Weight Modes](#inference-weight-modes)
- [Model Source Boundaries](#model-source-boundaries)
- [Automatic Official Weight Download](#automatic-official-weight-download)
- [Nodes](#nodes)
- [Attention Backends](#attention-backends)
- [Audio Conditioning And Dual-Person Mode](#audio-conditioning-and-dual-person-mode)
- [Generation Controls](#generation-controls)
- [Avatar 1.5 Usage Tips](#avatar-15-usage-tips)
- [Avatar 1.6 Usage Tips](#avatar-16-usage-tips)
- [Troubleshooting Desktop Installation](#troubleshooting-desktop-installation)
- [License](#license)

## Feature Status

| Capability | Status |
| --- | --- |
| Avatar 1.5 single audio `ai2v` | Supported |
| Avatar 1.5 single audio `at2v` | Supported without an image connection; `ai2v` still requires an image |
| Avatar 1.5 multi audio | Supported with `ai2v` only |
| Avatar 1.6 single audio `ai2v` with INT8 weights (`official_v16_int8_sharded`) | Supported; completed with one and with two segments on a CUDA host (Windows, ComfyUI Core 0.46.0, `attention_mode=sdpa`), and with one segment using `comfy_kitchen_int8`, see [Validated Compatibility](#validated-compatibility) |
| Avatar 1.6 single audio `ai2v` with BF16 weights (`official_v16_sharded`) | Implemented; generation was not run here |
| Avatar 1.6 `at2v`, two-speaker, 720p, and macOS or MLX | Not claimed; not run |
| 480p and 720p generation | Supported for Avatar 1.5; Avatar 1.6 was run at the example workflow's `480p` setting only |
| Distill inference | Required for both versions: Avatar 1.5 uses the selected distill LoRA, Avatar 1.6 uses the DMD and OPSD LoRA pair inside its checkpoint; sampler defaults are 8 steps, text CFG 1.0, audio CFG 1.0 |
| Single-file DiT `.safetensors` | Supported for Avatar 1.5 from `ComfyUI/models/diffusion_models/` |
| Official sharded DiT | Supported for Avatar 1.5 and Avatar 1.6 `base_model/` checkpoints |
| Official sharded INT8 DiT | Supported for Avatar 1.5 and Avatar 1.6 `base_model_int8/` checkpoints |
| Manifest-backed official weight download | Supported for known official Avatar 1.5 and Avatar 1.6 sharded DiT assets (Avatar 1.6 also includes `scheduler/` and the LoRA pair) and shared LongCat text encoder assets |
| Selectable attention backends | Supported for `auto`, `sdpa`, `flash_attn_2`, `flash_attn_3`, `xformers`, `sageattn`, and `comfy_kitchen_int8` (NVIDIA CUDA only; it falls back to SDPA elsewhere). The reserved `sageattn_3` option fails fast because LongCat varlen cross-attention wiring is incomplete. |
| GGUF DiT | Not supported yet |
| Avatar 1.0 | Not supported by this ComfyUI contract |
| CPU or MPS inference | Not supported for the CUDA-only model path |

## Installation

Install the custom node inside ComfyUI:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/rookiestar28/ComfyUI-LongCat-Avatar
cd ComfyUI-LongCat-Avatar
pip install -r requirements.txt
```

The supported distribution is a Registry or Git custom-node directory under ComfyUI. Direct `pip install .` or standalone wheel installation is not supported by this repository layout; `pip install -r requirements.txt` installs dependencies into the Python environment that already launches ComfyUI, not the node itself as a wheel.

Use the Python environment that launches ComfyUI. The runtime path is CUDA-oriented and expects a compatible NVIDIA GPU plus a working CUDA PyTorch build already installed for ComfyUI. The default `requirements.txt` installs dependencies for the exposed LongCat Avatar nodes, including vocal extraction support, but intentionally does not install `torch`, `torchvision`, `torchaudio`, FlashAttention, xFormers, SageAttention, Streamlit, OpenAI SDK, or upstream demo/server-only packages, because replacing those packages can break an existing ComfyUI setup.

System prerequisites:

- Python >=3.10,<3.14. Windows dependency/startup validation passed on Python 3.12.13 and Python 3.13.9. Python 3.14 is currently excluded because the default vocal-separation dependency chain does not provide the required compatible Windows binary dependency.
- FFmpeg executable: required by `LongCat Avatar Vocal Extract` through `audio-separator`, and by video/audio mux helpers. This must be an `ffmpeg` command visible on the PATH used to launch ComfyUI; Python packages such as `imageio-ffmpeg` do not satisfy every subprocess lookup.

Install examples:

```bash
# Conda/Miniforge environment used to launch ComfyUI
conda install -c conda-forge ffmpeg

# macOS Homebrew
brew install ffmpeg

# Debian/Ubuntu
sudo apt-get install ffmpeg
```

Verify from the same terminal or service environment that starts ComfyUI:

```bash
ffmpeg -version
```

macOS/MPS inference is not supported in this release. Any MPS work must happen on a dedicated experimental branch and must not be merged into the public CUDA path until Apple Silicon smoke inference proves model loading, attention fallback, audio encoding, VAE encode/decode, and end-to-end timing.

Dependency groups:

| File | Use When | Notes |
| --- | --- | --- |
| `requirements.txt` | Default node install | Required Python packages for model loading, audio encoding, vocal extraction, and sampling. |
| `requirements-acceleration.txt` | You want optional attention acceleration | Documentation-only examples for FlashAttention, xFormers, SageAttention, and comfy-kitchen. Do not install blindly; choose versions manually that match your ComfyUI PyTorch/CUDA stack. |

## Model Files

Use the normal ComfyUI model folders so the node dropdowns can find manually placed files.

Some official assets can be downloaded automatically from inside the nodes. Enable `auto_download_missing_weights` on `(auto)Load LongCat Avatar Model` for official sharded Avatar 1.5 and Avatar 1.6 DiT checkpoints, and enable `auto_download_missing_text_encoder` on `LongCat Avatar Text Encode` for the official shared LongCat-Video tokenizer/text encoder. VAE, Whisper, and, for Avatar 1.5, the selectable distill LoRA still need to be placed in the normal ComfyUI model folders.

Required for normal Avatar 1.5 generation:

- ComfyUI/models/loras/
  longcat-avatar-dmd_lora.safetensors

- ComfyUI/models/vae/
  LongCat-Video-Avatar-vae.safetensors

- ComfyUI/models/audio_encoders/
  whisper-large-v3.safetensors

Required for Avatar 1.6 generation:

- ComfyUI/models/vae/
  LongCat-Video-Avatar-vae.safetensors

- ComfyUI/models/audio_encoders/
  whisper-large-v3.safetensors

Avatar 1.6 needs no file in `ComfyUI/models/loras/`. Its DMD LoRA (`loraA/lora.safetensors`) and OPSD LoRA (`loraB/lora.safetensors`) are part of the official checkpoint and are loaded from the checkpoint folder. Leave the node's `lora` selector at `none`; a LoRA selected there is ignored, and the console says so. The observed Avatar 1.6 runs used the same VAE and Whisper file names as Avatar 1.5.

Choose one DiT source:

- `official_sharded`: use `auto_download_missing_weights` or place the official sharded files under `ComfyUI/models/longcat/LongCat-Video-Avatar-1.5/base_model/`.
- `official_int8_sharded`: use `auto_download_missing_weights` or place the official INT8 sharded files under `ComfyUI/models/longcat/LongCat-Video-Avatar-1.5/base_model_int8/`.
- `official_v16_sharded`: use `auto_download_missing_weights` or place the official Avatar 1.6 sharded files under `ComfyUI/models/longcat/LongCat-Video-Avatar-1.6/base_model/`, together with `loraA/lora.safetensors` and `loraB/lora.safetensors` from the same checkpoint.
- `official_v16_int8_sharded`: use `auto_download_missing_weights` or place the official Avatar 1.6 INT8 sharded files under `ComfyUI/models/longcat/LongCat-Video-Avatar-1.6/base_model_int8/`, together with `loraA/lora.safetensors` and `loraB/lora.safetensors` from the same checkpoint.
- `single_file_safetensors`: place `LongCat-Video-Avatar-1.5-int8.safetensors` under `ComfyUI/models/diffusion_models/`.

Choose one text encoder source:

- Recommended native path: use `auto_download_missing_text_encoder` or place the shared official assets under `ComfyUI/models/longcat/LongCat-Video/tokenizer/` and `ComfyUI/models/longcat/LongCat-Video/text_encoder/`.
- Existing fallback path: connect ComfyUI `Load CLIP` to `LongCat Avatar Text Encode` and place `umt5_xxl_fp8_e4m3fn_scaled.safetensors` under `ComfyUI/models/clip/`.

Optional vocal separation:

- ComfyUI/models/longcat/
  Kim_Vocal_2.onnx

Official sharded checkpoint layouts:

- ComfyUI/models/longcat/LongCat-Video-Avatar-1.5/base_model/
  config.json
  diffusion_pytorch_model.safetensors.index.json
  diffusion_pytorch_model-00001-of-00006.safetensors
  ...


- ComfyUI/models/longcat/LongCat-Video-Avatar-1.5/base_model_int8/
  config.json
  quantization_config.json
  quantized_model.safetensors.index.json
  quantized_model-00001-of-00004.safetensors
  ...

- ComfyUI/models/longcat/LongCat-Video-Avatar-1.6/base_model/ or base_model_int8/
  the same file layout as the Avatar 1.5 folder of that name (the BF16 `base_model/` has 6 shards, the INT8 `base_model_int8/` has 4)

- ComfyUI/models/longcat/LongCat-Video-Avatar-1.6/loraA/
  lora.safetensors

- ComfyUI/models/longcat/LongCat-Video-Avatar-1.6/loraB/
  lora.safetensors

The automatic download of an Avatar 1.6 checkpoint also fetches `scheduler/scheduler_config.json`; the node's loader does not require that file.

Download sources:

- Avatar 1.5 official weights: <https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5>
- Avatar 1.6 official weights: <https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.6>
- Shared LongCat-Video tokenizer/text encoder: <https://huggingface.co/meituan-longcat/LongCat-Video>
- Community INT8 merged DiT: <https://huggingface.co/smthem/LongCat-Video-Avatar-1.5-merge>
- UMT5 text encoder: <https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files/text_encoders>
- Optional vocal separator: <https://huggingface.co/seanghay/uvr_models/blob/main/Kim_Vocal_2.onnx>

| Model file | Description | Download link | ComfyUI filename |
| --- | --- | --- | --- |
| Whisper-large-v3 | Audio encoder used by `LongCat Avatar Whisper` (the same file name is used with Avatar 1.5 and with the observed Avatar 1.6 runs) | [Hugging Face](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5/blob/main/whisper-large-v3/model.safetensors) | Download as `model.safetensors`, then rename to `whisper-large-v3.safetensors` under `ComfyUI/models/audio_encoders/`. |
| Distill LoRA | Required Avatar 1.5 distillation LoRA for 8-step inference (not used by Avatar 1.6, which loads its LoRA pair from the checkpoint) | [Hugging Face](https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5/blob/main/lora/dmd_lora.safetensors) | Keep as `dmd_lora.safetensors` or rename to `longcat-avatar-dmd_lora.safetensors` under `ComfyUI/models/loras/`. |
| Kim_Vocal_2.onnx | Optional vocal separation model used by `LongCat Avatar Vocal Model` | [Hugging Face](https://huggingface.co/seanghay/uvr_models/blob/main/Kim_Vocal_2.onnx) | Keep as `Kim_Vocal_2.onnx` under `ComfyUI/models/longcat/`. |

The VAE filename is selectable from the ComfyUI VAE dropdown; `LongCat-Video-Avatar-vae.safetensors` and `LongCat_Avatar_1.5_vae.safetensors` are both acceptable local filenames as long as the selected file is the Avatar 1.5 VAE. The Avatar 1.6 example workflow selects `LongCat-Video-Avatar-vae.safetensors`.

`Kim_Vocal_2.onnx` is only needed when using the vocal separation nodes. The Python dependencies for those nodes are included in the default `requirements.txt` install.

Automatic download coverage:

- `auto_download_missing_weights` only applies to the official Avatar 1.5 and Avatar 1.6 sharded DiT checkpoint modes, described below.
- VAE is not included in the automatic download manifest. Keep `LongCat-Video-Avatar-vae.safetensors` in `ComfyUI/models/vae/`.
- The official manifest includes the upstream `lora/dmd_lora.safetensors` asset for checkpoint completeness, but the ComfyUI node still loads the selected distill LoRA from `ComfyUI/models/loras/`. Keep `longcat-avatar-dmd_lora.safetensors` in `ComfyUI/models/loras/` so the LoRA dropdown can find it.
- The Avatar 1.6 manifest includes `loraA/lora.safetensors`, `loraB/lora.safetensors`, and `scheduler/`. The node loads the two LoRAs from the checkpoint folder, so nothing is copied into `ComfyUI/models/loras/` for Avatar 1.6.
- The official UMT5 text encoder is shared with the base `LongCat-Video` model. `LongCat Avatar Text Encode` can auto-download the bounded `tokenizer/*` and `text_encoder/*` assets from `meituan-longcat/LongCat-Video` into `ComfyUI/models/longcat/LongCat-Video/`. Existing workflows with `Load CLIP` connected to `LongCat Avatar Text Encode` use the single-file UMT5 fallback path.

## Inference Weight Modes

`(auto)Load LongCat Avatar Model` exposes five supported inference weight modes. The selected mode determines the DiT source automatically; there is no separate `diffusion_models` or `official_checkpoint` selector on the node.

| Mode | Auto-selected source | Expected files |
| --- | --- | --- |
| `single_file_safetensors` | `LongCat-Video-Avatar-1.5-int8.safetensors` | One `.safetensors` DiT file in `ComfyUI/models/diffusion_models/` |
| `official_sharded` | `LongCat-Video-Avatar-1.5/base_model/diffusion_pytorch_model.safetensors.index.json` | Official `base_model/` index and all referenced shards |
| `official_int8_sharded` | `LongCat-Video-Avatar-1.5/base_model_int8/quantized_model.safetensors.index.json` | Official `base_model_int8/` index, `quantization_config.json`, and all referenced shards |
| `official_v16_sharded` | `LongCat-Video-Avatar-1.6/base_model/diffusion_pytorch_model.safetensors.index.json` | Official Avatar 1.6 `base_model/` `config.json`, index, and all referenced shards, plus `loraA/lora.safetensors` and `loraB/lora.safetensors` |
| `official_v16_int8_sharded` | `LongCat-Video-Avatar-1.6/base_model_int8/quantized_model.safetensors.index.json` | Official Avatar 1.6 `base_model_int8/` `config.json`, `quantization_config.json`, index, and all referenced shards, plus `loraA/lora.safetensors` and `loraB/lora.safetensors` |

The mode also selects the Avatar version. The three Avatar 1.5 modes build an Avatar 1.5 model, and the two `official_v16_*` modes build an Avatar 1.6 model, which needs `model_version` set to `avatar-v1.6` on `LongCat Avatar Audio Encode`.

Single-file mode loads the default merged/community DiT filename from `ComfyUI/models/diffusion_models/`. Official sharded modes pin automatic downloads to immutable source revisions and validate the checkpoint index JSON, required config files, every referenced shard, tensor-key coverage, allowed dtype, model shape compatibility, and declared tensor byte total before applying the state dictionary.

GGUF remains unsupported and is not exposed as a model-node selector.

## Model Source Boundaries

The official sharded modes are the official checkpoint contract for this repository. They load the official Avatar 1.5 or Avatar 1.6 `base_model/` or `base_model_int8/` layouts from `ComfyUI/models/longcat/` (`LongCat-Video-Avatar-1.5/` or `LongCat-Video-Avatar-1.6/`) and validate the official index files before tensor loading. For Avatar 1.6, the loader also requires both LoRA files of the checkpoint and checks that they form a matching pair.

Single-file `.safetensors` mode is for local or community-converted DiT files in `ComfyUI/models/diffusion_models/`. A converted single-file checkpoint can originate from official weights, but it is not the official sharded layout and is not treated as an `official_sharded` or `official_int8_sharded` source.

Third-party wrapper-specific conversions and scheduler names are engineering references only. They do not redefine this repository's tensor schema, checkpoint layout, scheduler semantics, or supported runtime modes. This repository does not require third-party wrapper conversion before use.

FP16, FP8, GGUF, and alternate scheduler controls are not accepted official runtime modes in this release. They remain unsupported or experimental until implemented with explicit compatibility checks, tests, and documentation.

Official runtime precision remains bf16 by default. Official INT8 support is selected through `official_int8_sharded` or `official_v16_int8_sharded` as a checkpoint/weight mode, not through a generic FP8 runtime switch. FP16, FP8, and GGUF are not runtime precision modes in this release.

## Automatic Official Weight Download

`auto_download_missing_weights` is available as an on/off toggle on `(auto)Load LongCat Avatar Model`. When enabled with `official_sharded`, `official_int8_sharded`, `official_v16_sharded`, or `official_v16_int8_sharded`, the node builds a fixed manifest for the matching official repository (`meituan-longcat/LongCat-Video-Avatar-1.5` or `meituan-longcat/LongCat-Video-Avatar-1.6`) and downloads missing official checkpoint assets under the folder of the selected version:

```text
ComfyUI/models/longcat/LongCat-Video-Avatar-1.5/
ComfyUI/models/longcat/LongCat-Video-Avatar-1.6/
```

The downloader is intentionally bounded:

- It is manifest-backed and limited to known official assets.
- It does not accept arbitrary URLs.
- It does not accept arbitrary repo IDs.
- It does not add a token text box; use normal Hugging Face local authentication when your environment requires gated access.
- It does not replace every ComfyUI model dropdown. VAE, Whisper, and, for Avatar 1.5, the distill LoRA still need to be present in their normal ComfyUI model folders.
- It does not download the VAE into `ComfyUI/models/vae/`.
- For Avatar 1.5, it does not register the official repo's `lora/dmd_lora.safetensors` as a selectable LoRA in `ComfyUI/models/loras/`; place or copy the required distill LoRA there before loading the model node. Avatar 1.6 needs no such copy.

`auto_download_missing_text_encoder` is available on `LongCat Avatar Text Encode`. When enabled, it downloads only the shared base `meituan-longcat/LongCat-Video` `tokenizer/*` and `text_encoder/*` assets into:

```text
ComfyUI/models/longcat/LongCat-Video/
```

`LongCat Avatar Text Encode` also exposes its own `offload_device` control for the native official path. The default is `cpu` so the native UMT5 text encoder weights do not consume VRAM; choose `cuda` only when you have enough headroom and want faster text encoding. If the `clip` input is connected, the node uses the existing ComfyUI `Load CLIP` single-file UMT5 fallback and does not load the native text encoder.

Broad manual checkpoint download:

```bash
hf download meituan-longcat/LongCat-Video-Avatar-1.5 --local-dir ComfyUI/models/longcat/LongCat-Video-Avatar-1.5
hf download meituan-longcat/LongCat-Video-Avatar-1.6 --local-dir ComfyUI/models/longcat/LongCat-Video-Avatar-1.6
```

Those commands download the upstream repository layout more broadly than the node's bounded manifest. The node still requires VAE, Whisper, and, for Avatar 1.5, selectable distill LoRA files to be placed in the normal ComfyUI model folders described above.

## Nodes

| Node | Purpose |
| --- | --- |
| `(auto)Load LongCat Avatar Model` | Loads the DiT source selected by `inference_weight_mode`, the VAE, and the required Avatar 1.5 distill LoRA (Avatar 1.6 loads its DMD and OPSD LoRA pair from the checkpoint) |
| `LongCat Avatar Whisper` | Loads `whisper-large-v3.safetensors` from `ComfyUI/models/audio_encoders/` |
| `LongCat Avatar Text Encode` | Preferred official-first text node. Without `clip`, it uses the shared official `LongCat-Video` tokenizer and UMT5 text encoder; with `clip`, it uses the ComfyUI `Load CLIP` single-file fallback |
| `LongCat Avatar Audio Crop` | Trims a ComfyUI audio input by start/end time, returns AUDIO, and provides an inline cropped-audio preview |
| `LongCat Avatar Audio Encode` | Builds reusable full-clip single-audio or optional dual-audio conditioning; `model_version` selects the Avatar 1.5 or Avatar 1.6 audio preparation |
| `LongCat Avatar Audio Window` | Optionally slices reusable full-clip audio conditioning for explicit continuation windows |
| `LongCat Avatar Sampler` | Generates frames in `ai2v` or `at2v` mode and can optionally mux audio into a saved video; `lora_mix_steps` and `lora_mix_alpha` control the Avatar 1.6 LoRA mix |
| `LongCat Avatar Vocal Model` | Loads an optional ONNX vocal separation model from `ComfyUI/models/longcat/` |
| `LongCat Avatar Vocal Extract` | Extracts vocals from an input audio clip before audio conditioning |

Typical graph order:

1. Load the model with `(auto)Load LongCat Avatar Model`.
2. Prefer `LongCat Avatar Text Encode` without connecting `clip` for official prompt-conditioning parity. It can auto-download the shared base `LongCat-Video` tokenizer/text encoder assets when `auto_download_missing_text_encoder` is enabled.
3. Load Whisper with `LongCat Avatar Whisper`.
4. Existing `Load CLIP` + `LongCat Avatar Text Encode` graphs remain supported as the UMT5 single-file fallback path.
5. Optionally trim source audio with `LongCat Avatar Audio Crop`. Its `Crop Preview` button queues only this output node so you can crop and preview audio without running the downstream sampler/video nodes.
6. Encode audio with `LongCat Avatar Audio Encode`, and set its `model_version` to the Avatar version of the model loaded in step 1.
7. Generate with `LongCat Avatar Sampler`.

## Attention Backends

`(auto)Load LongCat Avatar Model` includes an `attention_mode` selector:

| Mode | Behavior |
| --- | --- |
| `auto` | Preserves the attention flags from the selected LongCat checkpoint config. Official configs currently default to FlashAttention 2. If an optional backend from the config is unavailable, the runtime prints a warning and falls back to SDPA where supported. |
| `sdpa` | Forces PyTorch `scaled_dot_product_attention`. This is the most portable fallback. |
| `flash_attn_2` | Forces FlashAttention 2. The loader raises a clear error if the optional package is unavailable in the ComfyUI Python environment. |
| `flash_attn_3` | Forces FlashAttention 3. The loader raises a clear error if the optional package is unavailable in the ComfyUI Python environment. |
| `xformers` | Forces xFormers memory-efficient attention. The loader raises a clear error if xFormers is unavailable. |
| `sageattn` | Forces SageAttention for DiT attention. The loader raises a clear error if SageAttention is unavailable. |
| `sageattn_3` | Reserved for SageAttention3 Blackwell kernels. It currently raises a clear error even when a candidate backend is present because LongCat text varlen cross-attention support is not fully wired; use `sageattn` instead. |
| `comfy_kitchen_int8` | Opt-in prebuilt INT8 self-attention and audio cross-attention on supported NVIDIA CUDA hardware. Text cross-attention uses SDPA. The node falls back to SDPA with a warning when the optional backend is unavailable. |

For `comfy_kitchen_int8`, use a comfy-kitchen wheel with prebuilt INT8 attention in the Python environment that launches ComfyUI. The mode uses SDPA on other devices and when the installed wheel lacks the required kernel. It emits one warning per fallback reason per process. Select the model's checkpoint independently with `inference_weight_mode`.

SageAttention support is optional. Install and validate the package in the same Python environment that launches ComfyUI. The node uses lazy imports and does not require SageAttention for startup or CPU-only tests. At model load, the console prints the requested `attention_mode`, effective backend flags, and backend availability so slow SDPA fallback is visible.

## Audio Conditioning And Dual-Person Mode

`LongCat Avatar Audio Encode` supports a single-person path and an optional two-person dialogue path.

For single-person generation, connect only `audio`. Leave `left_audio` disconnected.

`model_version` selects the Avatar version the audio is prepared for: `avatar-v1.5` (the default, so existing workflows keep their behavior) or `avatar-v1.6`. Avatar 1.6 prepares one more second of audio than the generated duration and skips the loudness normalization that Avatar 1.5 applies before Whisper. The value must match the connected model. If it does not, the Sampler stops before any generation work with a message of this form: `Audio conditioning was encoded for 'avatar-v1.5', but the connected model is 'avatar-v1.6'. Set the Audio Encode node's model_version to 'avatar-v1.6' and encode the audio again.` Audio conditioning that carries no version reads as Avatar 1.5.

For two-person dialogue generation, the audio inputs are assigned by the characters' visual positions in the input image or video frame. Two-person generation was not run with Avatar 1.6 and is not claimed for it.

| Input | Meaning |
| --- | --- |
| `left_audio` | Speech for the person on the left side of the image or video frame |
| `audio` | Speech for the person on the right side of the image or video frame |

The left/right naming does not refer to stereo audio channels. It refers to where the people appear in the visual frame. In a two-person image, connect the left person's speech to `left_audio` and the right person's speech to `audio`.

`audio_type` controls how the two clips are combined:

| `audio_type` | Meaning |
| --- | --- |
| `para` | Parallel dialogue. The left and right clips are treated as simultaneous tracks and should have matching duration. |
| `add` | Sequential dialogue. The left clip is placed before the right clip with silence-padding semantics. |

`p_box` optionally tells the node where the people are in the image. Use comma-separated bounding boxes in this order:

```text
[left_y_min, left_x_min, left_y_max, left_x_max], [right_y_min, right_x_min, right_y_max, right_x_max]
```

Measure these coordinates on the original image connected to `Load Image`, not on the generated 480p/720p output. The pipeline builds masks from the original-image coordinates first, then resizes and center-crops the masks together with the image for inference.

To get the values, open the source image in an image editor or viewer that shows cursor coordinates, then record each person's bounding rectangle:

1. Read the top-left point as `x_min`, `y_min`.
2. Read the bottom-right point as `x_max`, `y_max`.
3. Enter the box in LongCat order: `[y_min, x_min, y_max, x_max]`.

Example: if the left person covers `x=120..430`, `y=80..760`, and the right person covers `x=520..820`, `y=90..770`, enter:

```text
[80, 120, 760, 430], [90, 520, 770, 820]
```

The first box maps to `left_audio`; the second box maps to `audio`. A third box may be provided for other/background people that should receive silent background conditioning:

```text
[left_y_min, left_x_min, left_y_max, left_x_max], [right_y_min, right_x_min, right_y_max, right_x_max], [other_y_min, other_x_min, other_y_max, other_x_max]
```

If `p_box` is empty, the node still builds audio conditioning, but it does not provide explicit person-location boxes to the multi-person path.

## Generation Controls

- `resolution`: `480p` maps to 480x832 and `720p` maps to 768x1280.
- `steps`: defaults to 8 for Avatar 1.5 DMD/distill inference; accepted range is 1 to 50. When the DMD/distill LoRA is active, the effective value is fixed to the official 8-step contract.
- `text_guidance_scale`: defaults to 1.0; accepted range is 1.0 to 10.0. It only affects non-DMD normal inference; Avatar 1.5 DMD/distill inference forces the effective text CFG to 1.0.
- `audio_guidance_scale`: defaults to 1.0; accepted range is 1.0 to 10.0. It only affects non-DMD normal inference; Avatar 1.5 DMD/distill inference forces the effective audio CFG to 1.0.
- `LongCat Avatar Audio Encode` computes `num_segments` automatically from the prepared input audio length and current `save_fps`. The first generated window is 93 frames; each continuation adds 80 new frames because the official window keeps 13 overlap frames. At 25 fps, an 18 second clip computes to 6 segments so generation covers the full audio. The sampler trims the generated segment envelope back to the source-audio frame count before returning image frames or muxing video.
- `save_fps`: defaults to 25. Treat 25 fps as the reliable Avatar 1.5 setting. Changing this value also changes audio-window segmentation and target output frame counts, but local validation showed non-25 fps values can make lip sync and motion timing unstable.
- `ref_img_index`: integer frame index for the reference image insertion/attention anchor used during continuation. It defaults to 10; official guidance commonly uses values in the 0 to 24 range for consistency.
- `mask_frame_range`: integer radius around `ref_img_index` where reference-frame attention is masked to reduce repeated motion. It defaults to 3; larger values may reduce repeated actions but can introduce artifacts. For Avatar 1.6, upstream changed its own default from 3 to 0 and its continuation examples use 0, so use 0 with Avatar 1.6; the Avatar 1.6 example workflow sets 0. This node's default stays 3 so that saved Avatar 1.5 workflows keep their values. `LongCat Avatar Audio Window` has the same control with the same default.
- `p_box`: optional person boxes for `LongCat Avatar Audio Encode`; see [Audio Conditioning And Dual-Person Mode](#audio-conditioning-and-dual-person-mode) for left/right audio mapping and coordinate order.
- `block_num`: integer memory-streaming control. `0` uses eager full DiT loading on CUDA and offloads the DiT back to CPU after generation. Values from `1` to `64` enable streaming prefetch mode with that block count.
- `offload_device`: VAE offload target used during denoising. `cpu` is the default and preserves the lower-VRAM behavior. `cuda` keeps the VAE resident on the active CUDA device to avoid VAE CPU/GPU transfers, but requires more VRAM.
- `inference_weight_mode`: choose `single_file_safetensors`, `official_sharded`, `official_int8_sharded`, `official_v16_sharded`, or `official_v16_int8_sharded`; the node auto-selects the corresponding default DiT source and the Avatar version.
- `auto_download_missing_weights`: on/off toggle for bounded official sharded checkpoint download (Avatar 1.5 and Avatar 1.6) when required files are missing.
- `lora_mix_steps` (Avatar 1.6 only): whole number from 1 to 8, default 4. The first N denoising steps mix the DMD and OPSD LoRAs; the remaining steps use OPSD only. Ignored for Avatar 1.5.
- `lora_mix_alpha` (Avatar 1.6 only): number from 0.0 to 1.0, default 1.0. The DMD weight in the mixed steps, as `alpha * DMD + (1 - alpha) * OPSD`: 1.0 uses DMD only in those steps and 0.0 uses OPSD only. Ignored for Avatar 1.5.
- With the defaults, an Avatar 1.6 run uses DMD for steps 1 to 4 and OPSD for steps 5 to 8. These are the values the official Avatar 1.6 model card documents as the defaults; the upstream demo script's command-line parser, as read for this release, defaults to 3 and 0.5 instead, and this node follows the documented values. A mixed run does not use the continuation KV cache, because a cache built under one LoRA state would be stale after the switch, so videos with several segments take longer. The console prints the decision at the start of each run, for example `LongCat LoRA mix: model_type=avatar-v1.6, steps=4, alpha=1.0, continuation KV cache off.`
- `auto_download_missing_text_encoder`: on/off toggle on text encode nodes for bounded shared base `LongCat-Video` tokenizer/text encoder download.
- `LongCat Avatar Text Encode` `offload_device`: chooses where the native official UMT5 text encoder is loaded for prompt encoding. `cpu` is the default to avoid loading the large text encoder into VRAM; `cuda` can be faster but needs substantially more VRAM. This is ignored when `clip` is connected for fallback.
- `mux_audio`: preferred optional native ComfyUI `AUDIO` connection for muxing. The sampler validates it before generation, writes a scoped temporary WAV only after frames are ready, removes that file after mux success or failure, and saves the final `.mp4` only under the ComfyUI output directory.
- `mux_audio_path`: deprecated compatibility input for existing workflows. During the migration window it accepts only readable supported media inside the current ComfyUI input, output, or temp directory. Leave both mux inputs empty to return image frames with an empty `video_path`; connecting native audio and setting the legacy path at the same time is an error.
- The example workflow connects cropped native audio to both the sampler mux input and the Core CreateVideo path so each route is visible. Disconnect one route before queueing if you want only one saved video.
- `debug_mode`: when enabled on `LongCat Avatar Sampler`, prints detailed phase timing, CUDA synchronization, and memory counters around cache cleanup, runtime-plan setup, generation, cleanup, and video muxing.

The aggregate LongCat pipeline is self-managed rather than registered as a ComfyUI-managed model patcher. Before LongCat placement begins, it estimates the DiT, LoRA, and VAE allocation and asks ComfyUI's public memory-management boundary to free host-owned model memory. Resident ComfyUI models are unloaded as needed to make room, and they reload when they are used again. LongCat generation is serialized so overlapping runs cannot corrupt placement or cleanup state. These safeguards improve host coexistence; they are not a claim that peak generation memory or generation time was reduced.

Alternate scheduler controls are not exposed. Reference-wrapper scheduler names such as `longcat_distill_euler` are not adopted unless official Avatar 1.5 parity is proven with source comparison and tests.

## Avatar 1.5 Usage Tips

| Tip | Repo-aligned guidance |
| --- | --- |
| Prompt detail | Use longer, descriptive prompts for better consistency. Include character appearance, speaking action, clothing, and scene context, for example: `A young woman with long black hair is speaking and smiling, wearing a white blouse, sitting in a bright cafe.` |
| Reference frame controls | `ref_img_index` defaults to 10. Values in the 0 to 24 range are commonly used for consistency; 30 can be tried when repeated motion is visible. `mask_frame_range` defaults to 3; larger values may reduce repeated actions but can introduce artifacts. |
| Resolution | The sampler supports `480p` and `720p` through the `resolution` control. In this ComfyUI node, `480p` maps to 480x832 and `720p` maps to 768x1280. |
| Dual-audio mode | `audio_type=para` is for simultaneous two-person dialogue and requires equal prepared clip lengths. `audio_type=add` makes a sequential turn-taking track: `left_audio` first, then `audio`, with silence padding semantics. |
| Avatar version | This ComfyUI package supports Avatar 1.5 and Avatar 1.6, chosen through `inference_weight_mode`; see [Avatar 1.6 Usage Tips](#avatar-16-usage-tips) for Avatar 1.6. Both use Whisper-large-v3 audio conditioning here; Avatar 1.0/Wav2Vec2 is not a supported runtime path in this repo. |
| Distill inference | Avatar 1.5 requires the DMD/distill LoRA. When the DMD LoRA is active, the effective sampler values are fixed to 8 steps, text CFG 1.0, and audio CFG 1.0; UI CFG inputs are accepted but do not affect inference. CFG tuning only applies to non-DMD normal inference. |
| INT8 mode | INT8 is supported for Avatar 1.5 through `official_int8_sharded` or a compatible INT8 single-file DiT source. Use it when you want lower VRAM usage and have the required INT8 files available. |

## Avatar 1.6 Usage Tips

| Tip | Repo-aligned guidance |
| --- | --- |
| Choosing Avatar 1.6 | Select `official_v16_int8_sharded` (INT8) or `official_v16_sharded` (BF16) on `(auto)Load LongCat Avatar Model`, and set `model_version` to `avatar-v1.6` on `LongCat Avatar Audio Encode`. The bundled `example_workflows/longcat-avatar1.6.json` sets both and uses the INT8 mode. INT8 is the mode that was run on the observed host; BF16 loading is implemented and was not run there. |
| LoRA | Leave `lora` at `none`. Avatar 1.6 loads its DMD and OPSD LoRAs from the checkpoint (`loraA`, `loraB`); a LoRA selected in the node is ignored, and the console says so. |
| LoRA mix | The defaults `lora_mix_steps` 4 and `lora_mix_alpha` 1.0 use DMD for the first four steps and OPSD for the rest. See [Generation Controls](#generation-controls). |
| Several segments | A mixed run does not use the continuation KV cache, so a continuation recomputes the condition frames at every denoising step instead of reusing a cached copy. Measured with `attention_mode=sdpa`, INT8 weights, and the example workflow's `480p` setting on one NVIDIA RTX PRO 6000 Blackwell GPU, the denoising loop took about 110.8 s for segment 1 and 109.7 s for segment 2 in the two-segment Avatar 1.6 run (cache off), and about 111.0 s and 99.9 s in the two-segment Avatar 1.5 run (cache on). These are two different models, so read them as a note about the cache, not as a speed comparison between versions. |
| `mask_frame_range` | Use 0 with Avatar 1.6, as the example workflow does. |
| Audio | Set `model_version` to `avatar-v1.6` on the Audio Encode node and encode the audio again after switching models; a mismatch stops the Sampler with an error that names the fix. |
| Memory | A LongCat run may unload resident ComfyUI models to make room for itself; they reload when they are used again. |
| Attention backend | The example workflows save `sageattn`. The observed runs used `sdpa` and `comfy_kitchen_int8`. See [Validated Compatibility](#validated-compatibility) for the tested scope. |

## Troubleshooting Desktop Installation

If ComfyUI Desktop reports the LongCat nodes as missing after installing Registry version 0.2.0, update the node pack to version 0.2.1 or later and fully restart ComfyUI. Version 0.2.0 omitted required fresh-install metadata and could fail before node registration; reinstalling current dependencies in the Python environment managed by ComfyUI Desktop and restarting clears that stale installation state.

The example workflow identifies this package as `comfyui-longcat-avatar`. When the package is absent, current ComfyUI frontends should group its missing nodes under that package name instead of an unknown pack. Model-file warnings are separate: follow [Model Files](#model-files) after all LongCat node types are available.

## License

This project is licensed under the [MIT License](LICENSE).
