# Awesome Qwen-Image 2.1

A curated list of checkpoints, quants, prompt engines, LoRAs, and tooling for **Qwen-Image 2.1** — Alibaba's 7B unified text-to-image and image-editing model.

<div align="center">

<img alt="awesome-qwen-image" src="https://github.com/user-attachments/assets/ea5c1e84-e58b-498f-9627-15e63154059d" />

[![Hugging Face][hf-shield]][hf-url]
[![License][lic-shield]][lic-url]
[![Last Commit][commit-shield]][commit-url]
[![PRs Welcome][prs-shield]][prs-url]

</div>

> [!NOTE]
> **Qwen-Image 2.1** was released **2026-09-20** with day-0 support in Diffusers, ComfyUI, vLLM-Omni, SGLang, and LightX2V. It unifies generation and editing in one 7B DiT, adds native RGBA output, and accepts up to 10 reference images. Licensed under the **Qwen Research License**.

<details>
<summary><b>Table of Contents</b></summary>

* [Quick start](#quick-start)
* [Official checkpoints](#official)
  * [Base model](#official-base)
  * [Official Turbo](#official-turbo)
  * [ComfyUI official](#official-comfy)
* [Text encoders &amp; prompt engines](#encoders)
  * [Prompt rewriters](#pe)
  * [Heretic &amp; abliterated](#heretic)
  * [Quantized &amp; ported](#pe-quant)
* [Quantizations](#quant)
  * [GGUF](#quant-gguf)
  * [4-bit &amp; 8-bit](#quant-lowbit)
  * [FP8 &amp; bf16](#quant-fp8)
  * [Nunchaku (SVDQ)](#quant-nunchaku)
* [Turbo &amp; step distillation](#turbo)
  * [Turbo GGUF](#turbo-gguf)
  * [Official &amp; converted](#turbo-models)
* [LoRA &amp; adapters](#lora)
* [Platform ports](#port)
  * [Apple Silicon](#port-apple)
  * [Mobile &amp; edge (MNN)](#port-mnn)
  * [AMD &amp; domestic accelerators](#port-alt)
  * [ComfyUI package formats](#port-pkg)
  * [Experimental VAE](#port-vae)
* [Tools &amp; notebooks](#tools)
* [Contributing](#contributing)

</details>

---

<a id="quick-start"></a>

## ⌬ Quick start

Pick your entry point based on the runtime you already have.

| I want to… | Use | Why |
| :--- | :--- | :--- |
| Run the reference model in Diffusers | **[Qwen](https://huggingface.co/Qwen/Qwen-Image-2.1)** | Official BF16 diffusers repo, `QwenImage21Pipeline` |
| Use it in ComfyUI | **[Comfy-Org](https://huggingface.co/Comfy-Org/Qwen-Image-2.1)** | Pre-split folder layout, Day-0 native nodes |
| Fit it in 8–12 GB VRAM | **[INT4ConvRot-ComfyUI](https://huggingface.co/chfm/Qwen-Image-2.1-INT4ConvRot-ComfyUI)** | Complete ComfyUI pack incl. int4 ConvRot DiT + TE |
| Run locally with llama.cpp / GGUF | **[Unsloth GGUF](https://huggingface.co/unsloth/Qwen-Image-2.1-GGUF)** | Widest quant spread, Q2_K → Q8_0 |
| Generate in 8 steps (official) | **[Qwen-Image-2.1-Turbo](https://huggingface.co/Qwen/Qwen-Image-2.1-Turbo)** | Qwen's own 8-step checkpoint; CFG 1, schedule carried in the weights |
| Generate in 4 steps | **[Viggle Turbo](https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo)** | Community DMD distill + LoRA variants |
| On a Mac (Apple Silicon) | **[MLX-4bit](https://huggingface.co/themindstudio/Qwen-Image-2.1-MLX-4bit)** | MLX 4-bit, native unified memory |
| Improve prompt quality | **[PE-T2I](https://huggingface.co/Qwen/Qwen-Image-2.1-PE-T2I)** | Official prompt rewriter + aspect-ratio picker |

**Official resources**

* [Qwen-Image-2.1 model card](https://huggingface.co/Qwen/Qwen-Image-2.1) — official weights, license, aspect-ratio table
* [Qwen-Image-2.1 GitHub repo](https://github.com/QwenLM/Qwen-Image-2.1) — inference code, news, supported frameworks
* [Qwen blog: Qwen-Image-2.1](https://qwen.ai/blog?id=qwen-image-2.1) — release notes with architecture and benchmark figures
* [ComfyUI native workflow example](https://docs.comfy.org/tutorials/image/qwen/qwen-image-2-1) — official ComfyUI tutorial
* [ModelScope mirror](https://modelscope.cn/models/Qwen/Qwen-Image-2.1) — official CN mirror

**Model facts worth knowing**

* **7B parameters** in the visual generation component, **32 single-stream DiT layers**.
* Mixed-granularity attention (token-level causal for text, chunk-level for image) with **prefix KV cache reuse** for multi-reference editing.
* Native **RGBA** output — the prompt decides whether the result has an alpha channel.
* Editing accepts **up to 10 reference images**, plus circles, painted annotations, or separate masks for local edits.
* **Qwen3-VL-8B** is the text encoder, so the text encoder is the largest single download at ~17.5 GB BF16.
* Default sample setting is **40 steps without classifier-free guidance**; CFG is available for prompt adherence.

<p id="official" align="center">◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆</p>

## ▓ Official checkpoints

The reference weights. Start here before touching any community conversion.

<p id="official-base" align="center">· · · · · · · · · · · · · ·</p>

### ▣ Base model

| Name | Precision | Layout | DiT | Text encoder | VAE | Links |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Qwen-Image-2.1** | ![bf16][badge-bf16] | diffusers | 14.23 GB | 17.53 GB (Qwen3-VL-8B) | 1.35 GB | [![][gh-Qwen]](https://huggingface.co/Qwen/Qwen-Image-2.1) |

The reference release, and the only repo you need for a standard Diffusers setup. The DiT and text encoder ship as numbered safetensors shards with an index, so pull the repo rather than a single file.

<p id="official-turbo" align="center">· · · · · · · · · · · · · ·</p>

### ▣ Official Turbo

| Name | Precision | Layout | DiT | Text encoder | VAE | Links |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Qwen-Image-2.1-Turbo** | ![bf16][badge-bf16] | diffusers | 14.23 GB | 17.53 GB (Qwen3-VL-8B) | 0.68 GB | [![][gh-Qwen]](https://huggingface.co/Qwen/Qwen-Image-2.1-Turbo) |

Qwen's own accelerated checkpoint, released **2026-10-09**: the same 7B architecture at **8 denoising steps**, **CFG 1.0** by default, and the recommended sampling schedule is carried *inside the checkpoint*, so `QwenImage21Pipeline` configures the sampler itself — no manual sigma grid. Prefix KV caching reuses the text and reference-image context across steps, which is where the speed comes from on editing. Needs a diffusers build with pipeline-configured sampling sigmas (`transformers>=5.17.0`; support landed in diffusers PR #14950). Card examples run text-to-image at 1696×2528 and editing at 2048×2048. The ComfyUI pre-split build of these weights is the **Turbo** rows in the Comfy-Org table below; the community few-step lines live under [Turbo](#turbo).

<p id="official-comfy" align="center">· · · · · · · · · · · · · ·</p>

### ▣ ComfyUI official

**[Comfy-Org](https://huggingface.co/Comfy-Org/Qwen-Image-2.1)** — the Day-0 ComfyUI repackage, now covering the base model and the official Turbo side by side. Files land directly in `models/` with no renaming.

| Name | Precision | Size | Links |
| :--- | :---: | :---: | :---: |
| **Image Model** | ![bf16][badge-bf16] | 14.23 GB | [![][gh-Comfy--Org]](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/diffusion_models/qwen_image_2.1_bf16.safetensors) |
| **Image Model** | ![int8][badge-int8] | 7.26 GB | [![][gh-Comfy--Org]](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/diffusion_models/qwen_image_2.1_int8_convrot.safetensors) |
| **Image Model (Turbo)** | ![bf16][badge-bf16] | 14.23 GB | [![][gh-Comfy--Org]](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/diffusion_models/qwen_image_2.1_turbo_bf16.safetensors) |
| **Image Model (Turbo)** | ![int8][badge-int8] | 7.26 GB | [![][gh-Comfy--Org]](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/diffusion_models/qwen_image_2.1_turbo_int8_convrot.safetensors) |
| **Text Encoder** | ![bf16][badge-bf16] | 17.53 GB | [![][gh-Comfy--Org]](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3vl_8b_bf16.safetensors) |
| **Text Encoder** | ![int8][badge-int8] | 9.35 GB | [![][gh-Comfy--Org]](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3vl_8b_int8_convrot.safetensors) |
| **Text Encoder** | ![w4a8][badge-w4a8] | 6.31 GB | [![][gh-Comfy--Org]](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3vl_8b_w4a8.safetensors) |
| **Prompt Engine T2I** | ![int8][badge-int8] | 9.47 GB | [![][gh-Comfy--Org]](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3.5_9b_qwen_image_2.1_pe_t2i.int8_convrot.safetensors) |
| **Prompt Engine I2I** | ![int8][badge-int8] | 9.47 GB | [![][gh-Comfy--Org]](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3.5_9b_qwen_image_2.1_pe_i2i.int8_convrot.safetensors) |
| **VAE** | ![bf16][badge-bf16] | 0.68 GB | [![][gh-Comfy--Org]](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/vae/qwen_image_2.1_vae_bf16.safetensors) |
| **ControlNet Union** | ![bf16][badge-bf16] | 7.55 GB | [![][gh-Comfy--Org]](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/model_patches/qwen_image_2.1_fun_controlnet_union_bf16.safetensors) |
| **ControlNet Union** | ![int8][badge-int8] | 3.78 GB | [![][gh-Comfy--Org]](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/model_patches/qwen_image_2.1_fun_controlnet_union_int8_convrot.safetensors) |
| **Turbo LoRA** | ![bf16][badge-bf16] | 0.91 GB | [![][gh-Comfy--Org]](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/loras/qwen_image_2.1_turbo_lora_avg_rank_178_bf16.safetensors) |

> [!TIP]
> `ConvRot` files are ComfyUI's native rotated-channel integer format. Use a recent ComfyUI build and load them with the standard diffusion-model and text-encoder loaders — no custom nodes required.
>
> Destination folders: **Image Model** → `models/diffusion_models/`, **Text Encoder** and both **Prompt Engine** rows → `models/text_encoders/`, **VAE** → `models/vae/`, both **ControlNet Union** rows → `models/model_patches/`, **Turbo LoRA** → `models/loras/`.
>
> The two **Image Model (Turbo)** rows are the official 8-step checkpoint pre-split for ComfyUI — same weights as the Qwen repo above, 8 steps and CFG 1. If you would rather keep the base DiT and switch speed at runtime, the **Turbo LoRA** row is the adapter extracted from those weights (average rank 178, by Kijai): load it on the BF16 base with `LoraLoaderModelOnly` at strength 1.0, and do not stack it on a Turbo model.
>
> The two ControlNet rows are the Alibaba PAI Union checkpoint repacked, not an official Qwen release — the int8 build is the cheapest ControlNet here by half. The first **Image Model** row also ships as `model_patches/`, so a ComfyUI ControlNet workflow wants a matching-precision base.

<p id="encoders" align="center">◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆</p>

## ⚲ Text encoders &amp; prompt engines

Qwen-Image 2.1 conditions on **Qwen3-VL-8B**, which at BF16 is the largest file in the stack. It also ships dedicated **prompt-rewriting** models — separate text models that take a short request in any language and return a detailed English prompt plus a recommended aspect ratio. Neither is part of the diffusion path; both are optional, and you can run the base model without either.

<p id="pe" align="center">· · · · · · · · · · · · · ·</p>

### ▣ Prompt rewriters

The official pair is fine-tuned Qwen3.5-VL 9B. The **Pocket** builds are fine-tuned from Qwen3.5 base models instead — roughly 5× smaller, text-to-image only.

| Name | Task | Params | Precision | Size | Links |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **PE-T2I** | ![text → image][task-t2i] | 9B | ![bf16][badge-bf16] | 18.82 GB | [![][gh-Qwen]](https://huggingface.co/Qwen/Qwen-Image-2.1-PE-T2I) |
| **PE-I2I** | ![image → image][task-i2i] | 9B | ![bf16][badge-bf16] | 18.82 GB | [![][gh-Qwen]](https://huggingface.co/Qwen/Qwen-Image-2.1-PE-I2I) |
| **PE-T2I Pocket 2B** | ![text → image][task-t2i] | 2B | ![bf16][badge-bf16] | 3.76 GB | [![][gh-ML--Intern--lab]](https://huggingface.co/ML-Intern-lab/Qwen-Image-2.1-PE-T2I-Pocket-2B) |
| **PE-T2I Pocket 0.8B** | ![text → image][task-t2i] | 0.8B | ![Q8_0][badge-Q8_0] | 1.50 GB | [![][gh-ML--Intern--lab]](https://huggingface.co/ML-Intern-lab/Qwen-Image-2.1-PE-T2I-Pocket-0.8B) |

The official rewriters ship a `system_prompt.txt` and work with `AutoModelForCausalLM` + `AutoTokenizer`. Output is JSON after a reasoning block, so split on the think-tag before parsing. The T2I rewriter also returns a recommended `wh_ratio` you can map straight to a size.

Each official repo splits into four `model-0000N.safetensors` shards plus a `model.safetensors.index.json`, so download the repo — there is no single-file build to link to. The 0.8B Pocket build also ships a `Q8_0` GGUF (0.81 GB) for llama.cpp.

<p id="heretic" align="center">· · · · · · · · · · · · · ·</p>

### ▣ Heretic &amp; abliterated

> [!WARNING]
> These repos have the safety refusal direction **abliterated**. The model no longer refuses prompt content, which means it will happily rewrite anything you ask. Same Qwen Research License as the base weights — the license does not grant you additional rights.
>
> Applied to both halves of the text stack: the **text encoder** (the conditioning signal itself no longer refuses) and the **prompt rewriter**.

| Type | Name | Task | Precision | Size | Links |
| :---: | :--- | :---: | :---: | :---: | :---: |
| ![TE][ltype-te] | **Heretic TE GGUF** | | ![Q4_K_M][badge-Q4_K_M] ![fp8][badge-fp8] ![bf16][badge-bf16] | 33.07 GB | [![][gh-pottokao]](https://huggingface.co/pottokao/Qwen-Image-2.1-Text-Encoder-Heretic-GGUF/resolve/main/qwen3vl_8b_heretic-Q4_K_M.gguf) |
| ![TE][ltype-te] | **Heretic TE DHQ GGUF** | | ![IQ4_XS][badge-IQ4_XS] ![Q4_K_M][badge-Q4_K_M] ![Q3_K_M][badge-Q3_K_M] | 4.56 GB | [![][gh-pottokao]](https://huggingface.co/pottokao/Qwen-Image-2.1-Text-Encoder-Heretic-DHQ-GGUF) |
| ![TE][ltype-te] | **Heretic TE NVFP4** | | ![nvfp4][badge-nvfp4] | 6.31 GB | [![][gh-pottokao]](https://huggingface.co/pottokao/Qwen-Image-2.1-Text-Encoder-Heretic-NVFP4/resolve/main/qwen3vl_8b_nvfp4_heretic.safetensors) |
| ![TE][ltype-te] | **Heretic TE int8 ConvRot** | | ![int8][badge-int8] | 9.35 GB | [![][gh-pottokao]](https://huggingface.co/pottokao/Qwen-Image-2.1-Text-Encoder-Heretic-int8-convrot/resolve/main/qwen3vl_8b_int8_convrot_heretic.safetensors) |
| ![TE][ltype-te] | **Heretic TE W4A8** | | ![w4a8][badge-w4a8] | 6.31 GB | [![][gh-Karsus1997]](https://huggingface.co/Karsus1997/Qwen-Image-2.1-Text-Encoder-Heretic-W4A8) |
| ![TE][ltype-te] | **Heretic TE BF16** | | ![bf16][badge-bf16] | 17.53 GB | [![][gh-kkxao]](https://huggingface.co/kkxao/Qwen-Image-2.1-Text-Encoder-Heretic) |
|  |  |  |  |  |  |
| ![PE][ltype-pe] | **PE-T2I Heretic GGUF** | ![text → image][task-t2i] | ![Q4_K_M][badge-Q4_K_M] | 5.89 GB | [![][gh-pottokao]](https://huggingface.co/pottokao/Qwen-Image-2.1-PE-T2I-Heretic-GGUF/resolve/main/pe_t2i_heretic-Q4_K_M.gguf) |
| ![PE][ltype-pe] | **PE-I2I Heretic GGUF** | ![image → image][task-i2i] | ![Q4_K_M][badge-Q4_K_M] | 6.81 GB | [![][gh-pottokao]](https://huggingface.co/pottokao/Qwen-Image-2.1-PE-I2I-Heretic-GGUF/resolve/main/pe_i2i_heretic-Q4_K_M.gguf) |
| ![PE][ltype-pe] | **ComfyUI PE bundle** | ![both][task-both] | ![Q4_K_M][badge-Q4_K_M] | 18.07 GB | [![][gh-t8star]](https://huggingface.co/t8star/qwen-image-2.1-comfy) |
| ![PE][ltype-pe] | **PE-I2I Abliterated** | ![image → image][task-i2i] | ![bf16][badge-bf16] | 18.82 GB | [![][gh-base11231]](https://huggingface.co/base11231/Qwen-Image-2.1-PE-I2I-Abliterated) |
| ![PE][ltype-pe] | **PE-T2I Heretic** | ![text → image][task-t2i] | ![bf16][badge-bf16] | 18.82 GB | [![][gh-darrellbest]](https://huggingface.co/darrellbest/Qwen-Image-2.1-PE-T2I-Heretic) |
| ![PE][ltype-pe] | **PE-I2I Heretic** | ![image → image][task-i2i] | ![bf16][badge-bf16] | 18.82 GB | [![][gh-darrellbest]](https://huggingface.co/darrellbest/Qwen-Image-2.1-PE-I2I-Heretic) |
| ![PE][ltype-pe] | **PE-T2I Heretic NVFP4** | ![text → image][task-t2i] | ![nvfp4][badge-nvfp4] | 11.20 GB | [![][gh-darrellbest]](https://huggingface.co/darrellbest/Qwen-Image-2.1-PE-T2I-Heretic-NVFP4) |
| ![PE][ltype-pe] | **PE-I2I Heretic NVFP4** | ![image → image][task-i2i] | ![nvfp4][badge-nvfp4] | 11.20 GB | [![][gh-darrellbest]](https://huggingface.co/darrellbest/Qwen-Image-2.1-PE-I2I-Heretic-NVFP4) |

Start with the **TE GGUF** build if you want one download: Q4_K_M (5.03 GB), fp8 (9.34 GB), bf16 (17.53 GB), plus a 1.16 GB `mmproj` projector, all in one repo.

**DHQ** (Dual-Head Quant) is a sibling of that build, not a different model: the same heretic weights re-quantized so each tensor gets the precision that matters to what the **Qwen 2.1 DiT actually reads** — measured through the DiT's own text-input stage rather than by next-token loss. Every file is byte-for-byte the same *size* as llama.cpp's build of that name and better at it. The ladder runs IQ2_S → IQ4_XS plus Q2_K / Q3_K_M / Q4_K_M, and each one ships its imatrix recipe. Take DHQ below Q5; at Q5 and above the standard recipe already matches it, so there is no reason to. It is tuned for this DiT specifically — Ideogram 4 and the other Qwen3-VL-8B consumers can load the files but were not tuned for.

<p id="pe-quant" align="center">· · · · · · · · · · · · · ·</p>

### ▣ Quantized &amp; ported

| Name | Format | Precision | Size | Links |
| :--- | :---: | :---: | :---: | :---: |
| **PE ComfyUI pack** | BF16 + int8 ConvRot | ![bf16][badge-bf16] ![int8][badge-int8] | 64.68 GB | [![][gh-HarleyWang]](https://huggingface.co/HarleyWang/Qwen-Image-2.1-PE-ComfyUI) |
| **PE-T2I MLX** | MLX (4/8/16-bit) | ![int4][badge-int4] ![int8][badge-int8] ![bf16][badge-bf16] | 35.20 GB | [![][gh-prithivMLmods]](https://huggingface.co/prithivMLmods/Qwen-Image-2.1-PE-T2I-MLX) |
| **PE-I2I MLX** | MLX (4/8/16-bit) | ![int4][badge-int4] ![int8][badge-int8] ![bf16][badge-bf16] | 35.20 GB | [![][gh-prithivMLmods]](https://huggingface.co/prithivMLmods/Qwen-Image-2.1-PE-I2I-MLX) |
| **Prompt Enhancement INT8** | int8 ConvRot | ![int8][badge-int8] | 24.69 GB | [![][gh-foofifoo]](https://huggingface.co/foofifoo/Qwen-Image-2.1-Prompt-Enhancement-INT8-Convrot) |
| **Heretic T2I int8 tensorwise** | int8 tensorwise ConvRot | ![int8][badge-int8] | 9.99 GB | [![][gh-diffnamehard]](https://huggingface.co/diffnamehard/Qwen-Image-2.1-PE-T2I-Heretic-int8-tensorwise-convrot) |
| **Heretic PE int8 ConvRot** | int8 ConvRot (T2I + I2I) | ![int8][badge-int8] | 19.91 GB | [![][gh-netrunner--exe]](https://huggingface.co/netrunner-exe/Qwen-Image-2.1-PE-Heretic) |

The INT8 ConvRot pack covers both PE-T2I and PE-I2I in one download. The heretic int8 ConvRot pair does too, and unlike the tensorwise build it keeps the MTP head — 1,395 tensors against 829, one file per task at 9.96 GB.

<p id="quant" align="center">◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆</p>

## ◈ Quantizations

Community conversions of the base DiT. Sizes are total weight bytes per repo. Distilled turbo GGUFs live under [Turbo](#turbo) instead.

<p id="quant-gguf" align="center">· · · · · · · · · · · · · ·</p>

### ▣ GGUF

Transformer-only weights for llama.cpp, sorted from the highest quant down. **Q4_K_M** is the usual quality/size balance point. **[Unsloth](https://huggingface.co/unsloth/Qwen-Image-2.1-GGUF)** is the primary source — it carries the widest ladder, so it wins every quant it ships. Where two repos offer a quant Unsloth does not, both are linked in the same cell.

| Quant | Size | Download |
| :---: | :---: | :---: |
| ![F16][badge-bf16] | 14.23 GB | [![][gh-unsloth]](https://huggingface.co/unsloth/Qwen-Image-2.1-GGUF/resolve/main/qwen-image-2.1-F16.gguf) |
| ![BF16][badge-bf16] | 14.23 GB | [![][gh-abenzerps]](https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-Quantized/resolve/main/qwen-image-2.1-UC-BF16.gguf) |
| ![Q8_0][badge-q8] | 7.64 GB | [![][gh-unsloth]](https://huggingface.co/unsloth/Qwen-Image-2.1-GGUF/resolve/main/qwen-image-2.1-Q8_0.gguf) |
| ![Q6_K_XL][badge-q6k] | 6.72 GB | [![][gh-unsloth]](https://huggingface.co/unsloth/Qwen-Image-2.1-GGUF/resolve/main/qwen-image-2.1-Q6_K_XL.gguf) |
| ![Q6_K][badge-q6k] | 6.27 GB | [![][gh-unsloth]](https://huggingface.co/unsloth/Qwen-Image-2.1-GGUF/resolve/main/qwen-image-2.1-Q6_K.gguf) |
| ![Q5_K_M][badge-q5km] | 5.39 GB | [![][gh-unsloth]](https://huggingface.co/unsloth/Qwen-Image-2.1-GGUF/resolve/main/qwen-image-2.1-Q5_K_M.gguf) |
| ![Q5_K_S][badge-q5km] | 4.50 GB | [![][gh-unsloth]](https://huggingface.co/unsloth/Qwen-Image-2.1-GGUF/resolve/main/qwen-image-2.1-Q5_K_S.gguf) |
| ![Q4 · HVQ3 (sd.cpp)][badge-q4km] | 5.96 GB | [![][gh-zcf0508]](https://huggingface.co/zcf0508/qwen-image-2.1-hqv3-sdcpp-fixed/resolve/main/Qwen-Image-2.1-Q4-sd.cpp.gguf) |
| ![NVFP4][badge-nvfp4] | 4.05 GB | [![][gh-gguf-org]](https://huggingface.co/gguf-org/qwen-image-2.1-gguf/resolve/main/qwen-image-2.1-nvfp4.gguf) |
| ![Q4_K_M][badge-q4km] | 4.20 GB | [![][gh-unsloth]](https://huggingface.co/unsloth/Qwen-Image-2.1-GGUF/resolve/main/qwen-image-2.1-Q4_K_M.gguf) |
| ![Q4_0][badge-q4km] | 4.15 GB | [![][gh-abenzerps]](https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-Quantized/resolve/main/qwen-image-2.1-UC-Q4_0.gguf) ┊ [![][gh-ped4enko]](https://huggingface.co/ped4enko/Qwen-Image-2.1-Dessi/resolve/main/qwen-image-2.1-Q4_0.gguf) |
| ![Q4_K_S][badge-q4km] | 3.91 GB | [![][gh-unsloth]](https://huggingface.co/unsloth/Qwen-Image-2.1-GGUF/resolve/main/qwen-image-2.1-Q4_K_S.gguf) |
| ![Q3_K_XL][badge-q3km] | 3.61 GB | [![][gh-unsloth]](https://huggingface.co/unsloth/Qwen-Image-2.1-GGUF/resolve/main/qwen-image-2.1-Q3_K_XL.gguf) |
| ![Q3_K_M][badge-q3km] | 3.17 GB | [![][gh-unsloth]](https://huggingface.co/unsloth/Qwen-Image-2.1-GGUF/resolve/main/qwen-image-2.1-Q3_K_M.gguf) |
| ![Q3_K_S][badge-q3km] | 2.72 GB | [![][gh-unsloth]](https://huggingface.co/unsloth/Qwen-Image-2.1-GGUF/resolve/main/qwen-image-2.1-Q3_K_S.gguf) |
| ![Q2_K][badge-q2k] | 2.47 GB | [![][gh-unsloth]](https://huggingface.co/unsloth/Qwen-Image-2.1-GGUF/resolve/main/qwen-image-2.1-Q2_K.gguf) |
| Text encoder ![NVFP4][badge-nvfp4] | 6.30 GB | [![][gh-gguf-org]](https://huggingface.co/gguf-org/qwen-image-2.1-gguf/resolve/main/qwen3vl-8b-nvfp4.gguf) |
| Text encoder ![Q4_K_M][badge-q4km] | 5.03 GB | [![][gh-gguf-org]](https://huggingface.co/gguf-org/qwen-image-2.1-gguf/resolve/main/qwen3vl-8b-it-q4_k_m.gguf) |
| mmproj projector ![Q8_0][badge-q8] | 0.75 GB | [![][gh-gguf-org]](https://huggingface.co/gguf-org/qwen-image-2.1-gguf/resolve/main/mmproj-qwen3vl-8b-it-q8_0.gguf) |
| VAE ![BF16][badge-bf16] | 0.68 GB | [![][gh-gguf-org]](https://huggingface.co/gguf-org/qwen-image-2.1-gguf/resolve/main/pig_qwen_image_2.1_vae_bf16.gguf) |
| VAE ![F16][badge-f16] | 0.68 GB | [![][gh-gguf-org]](https://huggingface.co/gguf-org/qwen-image-2.1-gguf/resolve/main/pig_qwen_image_2.1_vae_fp32-f16.gguf) |

<p id="quant-lowbit" align="center">· · · · · · · · · · · · · ·</p>

### ▣ 4-bit &amp; 8-bit

Every FP4 / NVFP4 / MXFP4 / INT8 / INT4 / W4A4 conversion in one place.

| Name | Precision | Size | Links | Notes |
| :--- | :---: | :---: | :---: | :--- |
| **INT4ConvRot-ComfyUI** | ![bf16][badge-bf16] ![int8][badge-int8] ![int4][badge-int4] ![w4a8][badge-w4a8] | 65.91 GB | [![][gh-chfm]](https://huggingface.co/chfm/Qwen-Image-2.1-INT4ConvRot-ComfyUI) | **Best all-in-one ComfyUI pack.** DiT and TE at three precisions plus VAE, in correct folder layout. |
| **Darkstar ModelOpt W4A4 NVFP4** | ![nvfp4][badge-nvfp4] | 23.66 GB | [![][gh-HangGlidersRule]](https://huggingface.co/HangGlidersRule/Darkstar-Qwen-Image-2.1-Base-ModelOpt-W4A4-NVFP4) | NVIDIA ModelOpt-derived, full repo. |
| **INT8** | ![int8][badge-int8] | 17.96 GB | [![][gh-Rin247]](https://huggingface.co/Rin247/Qwen-Image-2.1-INT8) | Full diffusers repo. |
| **DiT NVFP4 ComfyUI** | ![nvfp4][badge-nvfp4] | 13.82 GB | [![][gh-pottokao]](https://huggingface.co/pottokao/Qwen-Image-2.1-DiT-NVFP4-ComfyUI/resolve/main/qwen_image_2.1_nvfp4.safetensors) | Three ComfyUI cuts: `nvfp4`, `nvfp4_T2`, `nvfp4_T3`. |
| **FP4** | ![fp4][badge-fp4] | 11.74 GB | [![][gh-Rin247]](https://huggingface.co/Rin247/Qwen-Image-2.1-FP4/resolve/main/transformer/diffusion_pytorch_model.safetensors) | DiT 6.46 + TE 4.94 + VAE 0.34. |
| **INT4** | ![int4][badge-int4] | 11.08 GB | [![][gh-Rin247]](https://huggingface.co/Rin247/Qwen-Image-2.1-INT4) | Full diffusers repo. |
| **bnb 4bit** | ![int4][badge-int4] | 11.41 GB | [![][gh-circulus]](https://huggingface.co/circulus/Qwen-Image-2.1-bnb-4bit) | Standard bitsandbytes NF4. |
| **MXFP4 (Paiton)** | ![mxfp4][badge-mxfp4] | 9.31 GB | [![][gh-EliovpAI]](https://huggingface.co/EliovpAI/Qwen_Image-2.1-MXFP4) | Paiton backend, 57 shards. |
| **MXFP4 Paiton RDNA4** | ![mxfp4][badge-mxfp4] | 9.31 GB | [![][gh-EliovpAI]](https://huggingface.co/EliovpAI/Qwen_Image-2.1-MXFP4-Paiton-RDNA4) | RDNA4-specific kernel variant, identical layout. |
| **Uncensored MXFP4 Paiton** | ![mxfp4][badge-mxfp4] | 9.31 GB | ⚠️ [![][gh-EliovpAI]](https://huggingface.co/EliovpAI/Qwen_Image-2.1-Uncensored-MXFP4-Paiton) | Uncensored, derived from the abenzerps GGUF. |
| **Pipi** | ![int8][badge-int8] | 7.26 GB | ⚠️ [![][gh-RunningHubAI]](https://huggingface.co/RunningHubAI/rh-pipi-qwen-image-2.1-int8-01-unet) | A photorealistic merged DiT in a genuinely mixed format: **649 tensors**, of which 192 are `I8` and 192 `U8` — a quantized ConvRot-style pair — plus 192 F32 scales and 73 BF16 tensors left in full precision. Single file for `models/diffusion_models/`, **no LoRA needed**. The card asks for trigger `photorealistic`, Euler, 40 steps, CFG 1.0, and states outright that no LoRA should be stacked on it. Uncensored in practice — the repo title marks it 无审查 ("unreviewed"). |
| **Noct Q** | ![int8][badge-int8] | 7.26 GB | ⚠️ [![][gh-Noctaluna]](https://huggingface.co/Noctaluna/Noct-Q-Uncensored-Qwen-Image-2.1) | The photorealistic line, and the parent of the Anime row below. Merged DiT, int8 ConvRot, single file for `models/diffusion_models/`. **Take V4** — the card measures it rendering explicit scenes as asked three times as often as V3, which is kept alongside for comparison. 25 steps, `euler`/`simple`, CFG 3 with a negative prompt; CFG 1 is twice as fast but then ignores the negative. The wider int4/fp8/bf16/fp16 ladder and the prompt gallery live on Civitai. |
| **Noct Q Anime** | ![int8][badge-int8] | 7.26 GB | ⚠️ [![][gh-Noctaluna]](https://huggingface.co/Noctaluna/Noct-Q-Anime-Uncensored-Qwen-Image-2.1) | Merged anime fine-tune of the DiT, single file, int8 ConvRot. Fits 8–12 GB cards. **Without the word "anime" in the prompt you get a photo** — the card is blunt that there is no trigger word. 25 steps, `euler`/`simple`, CFG 3. Uncensored: it will render explicit content. The card names no second parent model or merge recipe, so the lineage is Qwen 2.1 plus undisclosed transformer edits. |
| **Ray Qwen2.1 edit-enhanced** | ![int8][badge-int8] | 6.76 GB | ⚠️ [![][cv-Ray3780]](https://civitai.com/models/2972899/ray-qwen21?modelVersionId=3369126) | A merged DiT, not a distillation: a custom editing LoKR plus realtime fine-tuning folded into the base, so it keeps base step counts — **25–40 steps, CFG 1–4**, Euler_A + simple for T2I and `beta57` for edits, 832×1216 for a 1024×1536 target. The card is explicit that this is not a turbo cut and that existing turbo LoRAs cost quality; female anatomy is corrected, male anatomy is not yet. The version bundles the madebyollin texture-fix VAE. **Download requires a Civitai login.** Adults only. |
| **Ray Qwen2.1 turbo v1.3** | ![int8][badge-int8] | 6.70 GB | ⚠️ [![][cv-Ray3780]](https://civitai.com/models/2972899/ray-qwen21?modelVersionId=3395380) | Remaster of the official 09/10 Turbo checkpoint with the same editing work folded in: **8–16 steps at CFG 1** — the card's sweet spot is Euler_A + linear_quadratic at 12 steps for T2I, seeds_2/heunpp2 + linear_quadratic at 12 for edits. Unlocked, but complex two-person T2I poses still break limbs. Same texture-fix VAE bundle. **Download requires a Civitai login.** Adults only. |
| **W4A4 NVFP4** | ![nvfp4][badge-nvfp4] | 4.88 GB | [![][gh-ModelsLab]](https://huggingface.co/ModelsLab/Qwen-Image-2.1-W4A4-nvfp4) | DiT only; near-identical to the INT4 build. |
| **W4A4 INT4** | ![int4][badge-int4] | 4.66 GB | [![][gh-ModelsLab]](https://huggingface.co/ModelsLab/Qwen-Image-2.1-W4A4-int4) | DiT only. |
| **Uncensored NVFP4** | ![nvfp4][badge-nvfp4] | 4.20 GB | ⚠️ [![][gh-abenzerps]](https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-Quantized/resolve/main/qwen-image-2.1-UC-NVFP4.safetensors) | DiT only, native NVFP4 rather than a GGUF conversion. Repo's own 192 F8_E4M3 scales against 192 FP32 originals. |

<p id="quant-fp8" align="center">· · · · · · · · · · · · · ·</p>

### ▣ FP8 &amp; bf16

| Name | Precision | Size | Links | Notes |
| :--- | :---: | :---: | :---: | :--- |
| **Darkstar ModelOpt FP8** | ![fp8][badge-fp8] | 26.33 GB | [![][gh-HangGlidersRule]](https://huggingface.co/HangGlidersRule/Darkstar-Qwen-Image-2.1-Base-ModelOpt-FP8) | NVIDIA ModelOpt-derived, full repo. |
| **FP8** | ![fp8][badge-fp8] | 17.96 GB | [![][gh-Rin247]](https://huggingface.co/Rin247/Qwen-Image-2.1-FP8) | Closest thing to a drop-in smaller BF16. |
| **Uncensored BF16 SafeTensor** | ![bf16][badge-bf16] | 14.23 GB | ⚠️ [![][gh-dh123456789123]](https://huggingface.co/dh123456789123/Qwen-Image-2.1-Uncensored-BF16-SafeTensor/resolve/main/qwen-image-2.1-UC-BF16_bf16.safetensors) ┊ [![][gh-RunningHubAI]](https://huggingface.co/RunningHubAI/rh-qwen-image-2.1-bf16-unet/resolve/main/Qwen-Image-2.1-_bf16%E6%97%A0%E5%AE%A1%E6%9F%A5.safetensors) | Single 14.23 GB file — the full DiT in one piece, mirrored by both repos. |
| **Uncensored Genesis BF16** | ![bf16][badge-bf16] | 32.46 GB | ⚠️ [![][gh-LuffyTheFox]](https://huggingface.co/LuffyTheFox/Qwen-Image-2.1-Uncensored-Genesis-BF16-GGUF) | The abenzerps uncensored DiT with the author's "Genesis" denoising pass applied — a post-training SVD repair, not a fine-tune, so it is a distinct weight set rather than a re-upload. Self-contained: DiT 14.23 + a Genesis Qwen3-VL-8B text encoder (16.39) + `mmproj` (1.16) + VAE 0.68. |
| **DF11 ComfyUI** | ![bf16][badge-bf16] | 9.72 GB | [![][gh-mingyi456]](https://huggingface.co/mingyi456/Qwen-Image-2.1-DF11-ComfyUI/resolve/main/qwen_image_2.1_bf16-DF11.safetensors) | `qwen_image_2.1_bf16-DF11.safetensors`. |

<p id="quant-nunchaku" align="center">· · · · · · · · · · · · · ·</p>

### ▣ Nunchaku (SVDQ)

SVDQ-based 4-bit for Nunchaku, which targets low-VRAM systems and 4090-class cards.

| Name | Precision | Size | Links | Notes |
| :--- | :---: | :---: | :---: | :--- |
| **nunchaku** | ![fp4][badge-fp4] | 8.75 GB | [![][gh-catplusplus]](https://huggingface.co/catplusplus/nunchaku-qwen-image-2.1/resolve/main/best_quality_fp4.safetensors) | Two builds: `best_quality_fp4` and `svdq-fp4_r32`. |
| **nunchaku lite int4** | ![int4][badge-int4] | 4.15 GB | [![][gh-BlazeMCworld]](https://huggingface.co/BlazeMCworld/Qwen-Image-2.1-nunchaku-lite-int4) | Half the size of the FP4 build. |

<p id="turbo" align="center">◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆</p>

## ▸ Turbo &amp; step distillation

Few-step students of the base model, plus plain adapters that only change the schedule. Qwen's own 8-step checkpoint is the official reference and sits in the [official table](#official-turbo) above, so this page is the community response. Everything here trades fidelity for speed: useful for iteration and batch work, weaker than 40 steps on multi-reference composition and identity-preserving edits.

**Current Viggle release: `v0.3` (2026-09-29), 6 steps.** It supersedes `v0.2.1` (2026-09-24), `v0.2` (5-step name, sampled at 6) and `v0.1` (4 steps). Sample with `sigmas=[1.0, 0.9375, 0.875, 0.75, 0.5, 0.25]`, CFG 1.0, empty negative prompt. v0.3 is **not a strict upgrade** over v0.2.1 — less grain and cleaner surfaces, fine texture a little softer — so if you prefer the crisper look, v0.2.1 is still in the repository. A new **9-step mode** (7 turbo steps, then the LoRA off and the base model finishes the last two) buys small-text accuracy at about 1.4–1.5× the 6-step cost; it is diffusers- and Space-only. Official source: **[Viggle/Qwen-Image-2.1-viggle-turbo](https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo)**.

Three independent distillation lines are listed below, and their checkpoints are **not interchangeable** — pick one family. **Viggle** is the reference DMD line above. **Alibaba PAI** ships an official 4-step line via Parallel Decoding Distillation (PDD) in VideoX-Fun. **[Pruna](https://huggingface.co/Pruna-Qwen-Image-2.1)** is a third-party DMD line with 8-step and 5-step adapters. Beyond the three, **[congruency](https://huggingface.co/congruency/Qwen-Image-2.1-turbo-mfd)** trains against Mean Flow Distillation and **[lightx2v](https://huggingface.co/lightx2v/Qwen-Image-2.1-Lightning)** ships a 4-step Lightning adapter — both are ordinary LoRAs on the base model, so they compose with whatever else you run.

The Pruna adapters are strict about sampling. Each has its own sigma schedule and they are **not** interchangeable, so load exactly one: 8-step wants `sigmas=[1.0, 14/15, 6/7, 10/13, 2/3, 6/11, 0.4, 2/9]`, 5-step wants `sigmas=[1.0, 0.94, 6/7, 2/3, 0.4]`. Both need `shift=1.0` with dynamic shifting **off** (otherwise the sigmas get shifted twice), no CFG, no negative prompt, and LoRA strength 1.0. Trained at 1K with up to 3 reference images; 2K runs but sits outside training coverage. Requires a pinned diffusers commit.

<p id="turbo-gguf" align="center">· · · · · · · · · · · · · ·</p>

### ▣ Turbo GGUF

DiT-only quants for ComfyUI-GGUF, from the **v0.1 full fine-tune** (4-step). Both repos keep FP32 attention norms and BF16 patch embeddings, so do **not** stack a Viggle LoRA on top. Repos: **[realrebelai](https://huggingface.co/realrebelai/Viggle_Qwen-Image-2.1-Turbo_GGUFs)** (wider ladder) and **[Abiray](https://huggingface.co/Abiray/Qwen-Image-2.1-viggle-4-steps-turbo-GGUF)** (adds `Q4_K_S`). Where both ship a quant, both are linked; sizes differ because the builds differ.

| Quant | Size | Download |
| :---: | :---: | :---: |
| ![Q8_0][badge-Q8_0] | 7.69 / 7.59 GB | [![][gh-realrebelai]](https://huggingface.co/realrebelai/Viggle_Qwen-Image-2.1-Turbo_GGUFs/resolve/main/Qwen-Image-2.1-viggle-turbo-Q8_0.gguf) ┊ [![][gh-Abiray]](https://huggingface.co/Abiray/Qwen-Image-2.1-viggle-4-steps-turbo-GGUF/resolve/main/qwen_image_2.1_turbo_Q8_0.gguf) |
| ![Q6_K][badge-Q6_K] | 6.91 / 5.88 GB | [![][gh-realrebelai]](https://huggingface.co/realrebelai/Viggle_Qwen-Image-2.1-Turbo_GGUFs/resolve/main/Qwen-Image-2.1-viggle-turbo-Q6_K.gguf) ┊ [![][gh-Abiray]](https://huggingface.co/Abiray/Qwen-Image-2.1-viggle-4-steps-turbo-GGUF/resolve/main/qwen_image_2.1_turbo_Q6_K.gguf) |
| ![Q5_K_M][badge-Q5_K_M] | 5.96 / 5.01 GB | [![][gh-realrebelai]](https://huggingface.co/realrebelai/Viggle_Qwen-Image-2.1-Turbo_GGUFs/resolve/main/Qwen-Image-2.1-viggle-turbo-Q5_K_M.gguf) ┊ [![][gh-Abiray]](https://huggingface.co/Abiray/Qwen-Image-2.1-viggle-4-steps-turbo-GGUF/resolve/main/qwen_image_2.1_turbo_Q5_K_M.gguf) |
| ![Q4_K_M][badge-Q4_K_M] | 5.56 / 4.19 GB | [![][gh-realrebelai]](https://huggingface.co/realrebelai/Viggle_Qwen-Image-2.1-Turbo_GGUFs/resolve/main/Qwen-Image-2.1-viggle-turbo-Q4_K_M.gguf) ┊ [![][gh-Abiray]](https://huggingface.co/Abiray/Qwen-Image-2.1-viggle-4-steps-turbo-GGUF/resolve/main/qwen_image_2.1_turbo_Q4_K_M.gguf) |
| ![Q4_K_S][badge-Q4_K_S] | 4.06 GB | [![][gh-Abiray]](https://huggingface.co/Abiray/Qwen-Image-2.1-viggle-4-steps-turbo-GGUF/resolve/main/qwen_image_2.1_turbo_Q4_K_S.gguf) |
| ![Q3_K_M][badge-Q3_K_M] | 4.19 / 3.19 GB | [![][gh-realrebelai]](https://huggingface.co/realrebelai/Viggle_Qwen-Image-2.1-Turbo_GGUFs/resolve/main/Qwen-Image-2.1-viggle-turbo-Q3_K_M.gguf) ┊ [![][gh-Abiray]](https://huggingface.co/Abiray/Qwen-Image-2.1-viggle-4-steps-turbo-GGUF/resolve/main/qwen_image_2.1_turbo_Q3_K_M.gguf) |
| ![Q2_K][badge-Q2_K] | 3.77 GB | [![][gh-realrebelai]](https://huggingface.co/realrebelai/Viggle_Qwen-Image-2.1-Turbo_GGUFs/resolve/main/Qwen-Image-2.1-viggle-turbo-Q2_K.gguf) |

With the official Turbo out, **[Abiray](https://huggingface.co/Abiray/Qwen-Image-2.1-Turbo-GGUF)** runs the full ladder off *it* instead — `Q2_K` through `Q8_0`, converted with ComfyUI-GGUF and a patched llama-quantize build that natively handles the 297-tensor `qwen_image` architecture. Sampling matches the official checkpoint: `euler` with `simple` or `normal`, 4–8 steps (6 is the card's pick), CFG 1.0 — the card is explicit that raising CFG on a distilled model clips contrast and adds artifacts. Text encoder and VAE come from the Comfy-Org pack; this repo is DiT only.

| Quant | Size | Download |
| :---: | :---: | :---: |
| ![Q8_0][badge-Q8_0] | 7.59 GB | [![][gh-Abiray]](https://huggingface.co/Abiray/Qwen-Image-2.1-Turbo-GGUF/resolve/main/qwen_image_2.1_turbo_Q8_0.gguf) |
| ![Q6_K][badge-Q6_K] | 5.88 GB | [![][gh-Abiray]](https://huggingface.co/Abiray/Qwen-Image-2.1-Turbo-GGUF/resolve/main/qwen_image_2.1_turbo_Q6_K.gguf) |
| ![Q5_K_M][badge-Q5_K_M] | 5.01 GB | [![][gh-Abiray]](https://huggingface.co/Abiray/Qwen-Image-2.1-Turbo-GGUF/resolve/main/qwen_image_2.1_turbo_Q5_K_M.gguf) |
| ![Q5_K_S][badge-q5km] | 4.94 GB | [![][gh-Abiray]](https://huggingface.co/Abiray/Qwen-Image-2.1-Turbo-GGUF/resolve/main/qwen_image_2.1_turbo_Q5_K_S.gguf) |
| ![Q5_0][badge-q5km] | 4.94 GB | [![][gh-Abiray]](https://huggingface.co/Abiray/Qwen-Image-2.1-Turbo-GGUF/resolve/main/qwen_image_2.1_turbo_Q5_0.gguf) |
| ![Q4_K_M][badge-Q4_K_M] | 4.19 GB | [![][gh-Abiray]](https://huggingface.co/Abiray/Qwen-Image-2.1-Turbo-GGUF/resolve/main/qwen_image_2.1_turbo_Q4_K_M.gguf) |
| ![Q4_K_S][badge-Q4_K_S] | 4.06 GB | [![][gh-Abiray]](https://huggingface.co/Abiray/Qwen-Image-2.1-Turbo-GGUF/resolve/main/qwen_image_2.1_turbo_Q4_K_S.gguf) |
| ![Q4_0][badge-q4km] | 4.05 GB | [![][gh-Abiray]](https://huggingface.co/Abiray/Qwen-Image-2.1-Turbo-GGUF/resolve/main/qwen_image_2.1_turbo_Q4_0.gguf) |
| ![Q3_K_M][badge-Q3_K_M] | 3.19 GB | [![][gh-Abiray]](https://huggingface.co/Abiray/Qwen-Image-2.1-Turbo-GGUF/resolve/main/qwen_image_2.1_turbo_Q3_K_M.gguf) |
| ![Q3_K_S][badge-q3km] | 3.11 GB | [![][gh-Abiray]](https://huggingface.co/Abiray/Qwen-Image-2.1-Turbo-GGUF/resolve/main/qwen_image_2.1_turbo_Q3_K_S.gguf) |
| ![Q2_K][badge-Q2_K] | 2.45 GB | [![][gh-Abiray]](https://huggingface.co/Abiray/Qwen-Image-2.1-Turbo-GGUF/resolve/main/qwen_image_2.1_turbo_Q2_K.gguf) |

<p id="turbo-models" align="center">· · · · · · · · · · · · · ·</p>

### ▣ Official &amp; converted

Repo links: **[Viggle](https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo)** · **[alibaba-pai](https://huggingface.co/alibaba-pai/Qwen-Image-2.1-Fun-Acc-LoRAs)** · **[Pruna](https://huggingface.co/PrunaAI/Pruna-Qwen-Image-2.1)** · **[chfm](https://huggingface.co/chfm/Qwen-Image-2.1-viggle-turbo)** (v0.2 snapshot) · **[t8star](https://huggingface.co/t8star/Qwen-Image-2.1-viggle-turbo-4step-r64-comfy)** · **[xingewh](https://huggingface.co/xingewh/Qwen-Image-2.1-viggle-turbo-v0.2-5step-lora-r256_comfy)** · **[RunningHubAI](https://huggingface.co/RunningHubAI/rh-qwen-image-2.1-viggle-turbo-4step-r64-comfyui-t8-lora)** · **[addlabsviral](https://huggingface.co/addlabsviral/Qwen-Image-2.1-Turbo-4bit)** · **[cgb](https://huggingface.co/cgb/Qwen-Image-2.1-Turbo-ONNX)** · **[Zabin](https://huggingface.co/Zabin/Qwen_Image_2.1_Turbo_8Steps)** · **[t8star HiFi](https://huggingface.co/t8star/Qwen-Image-2.1-Turbo-Hifi-Comfy)** · **[congruency](https://huggingface.co/congruency/Qwen-Image-2.1-turbo-mfd)** · **[lightx2v](https://huggingface.co/lightx2v/Qwen-Image-2.1-Lightning)** · **[Abiray official-turbo GGUF](https://huggingface.co/Abiray/Qwen-Image-2.1-Turbo-GGUF)**

Two ComfyUI conversions of the v0.2.1 adapters exist and are not interchangeable. **[xingewh](https://huggingface.co/xingewh/Qwen-Image-2.1-viggle-turbo-v0.2-5step-lora-r256_comfy)** re-keys the weights for ComfyUI and loads with the stock `Load LoRA` node. **[t8star](https://huggingface.co/t8star/Qwen-Image-2.1-viggle-turbo-4step-r64-comfy)** fuses gate/up for ComfyUI's merged MLP, which is why its files are larger; load those with the built-in `LoraLoaderBypassModelOnly` at strength 1.0 on a **BF16** base, because ordinary merging loaders lose adapter updates to rounding.

Only **v0.2.1** has those third-party conversions — for v0.3, ComfyUI support means copying `viggle_turbo.py` from the repo into `custom_nodes/`. It ships two nodes: an **unmerged** LoRA node and a **Viggle Turbo Sigmas** node. Use the unmerged node; the stock LoRA loaders merge the adapter into the weights and drop about 30% of its update on bf16, adding noise on int8. The merged single-file transformers below skip the LoRA entirely and need only the sigmas node — but they are *close to, not the same as*, the LoRA path: on roughly 8 of 96 held-out requests the merged model settles on a different composition or outfit. If outputs must match diffusers, use the LoRA. Of the merged quants, **Q4_K_M drifts visibly more** (23–29 of 96 requests change noticeably) — use it only when nothing larger fits.

| Name | Steps | Precision | Size | Links | Notes |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Sarvam Tez** | 2 | ![bf16][badge-bf16] | 1.34 GB | [![][gh-sarvamaigc]](https://huggingface.co/sarvamaigc/Qwen-Image-2.1-Sarvam-Tez/resolve/main/Qwen-Image-2.1-sarvam-tez-2step-lora-r256.safetensors) | **The shortest schedule on this page**, from Sarvam AI: 2 steps, no CFG, and it is a plain LoRA on the stock pipeline, so the text encoder and VAE you already use are unchanged. The card claims it *beats* the 40-step base on DPG-Bench (86.44 vs 84.30, both without CFG) and puts 1024×1024 at 0.37 s on a B200. Rank 256, the widest adapter here. Needs the repo's `sarvam_tez.py` helper (`enable_sarvam_tez`) — there is no ComfyUI path, and no sigmas schedule to copy. Research licence, non-commercial. |
| **v0.3 LoRA r256** | 6 | ![bf16][badge-bf16] | 1.36 GB | [![][gh-Viggle]](https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo/resolve/main/Qwen-Image-2.1-viggle-turbo-v0.3-6step-lora-r256.safetensors) | **Start here.** The current official release. Load on the base transformer at runtime — do not merge, and keep strength 1.0. The r128 cut is an exact per-layer SVD of this update. |
| **v0.3 LoRA r128** | 6 | ![bf16][badge-bf16] | 0.68 GB | [![][gh-Viggle]](https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo/resolve/main/Qwen-Image-2.1-viggle-turbo-v0.3-6step-lora-r128.safetensors) | What the shipped ComfyUI workflows use. |
| **v0.3 adapter (peft)** | 6 | ![fp32][badge-fp32] | 2.72 GB | [![][gh-Viggle]](https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo/tree/main/peft_v0.3) | The v0.3 LoRA in PEFT key format, F32 as trained. Same weights as the r256 file under different key names — load one or the other, never both. |
| **v0.2.1 LoRA r256** | 6 | ![bf16][badge-bf16] | 1.36 / 1.36 / 1.76 GB | [![][gh-Viggle]](https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo/resolve/main/Qwen-Image-2.1-viggle-turbo-v0.2.1-6step-lora-r256.safetensors) ┊ [![][gh-xingewh]](https://huggingface.co/xingewh/Qwen-Image-2.1-viggle-turbo-v0.2-5step-lora-r256_comfy/resolve/main/Qwen-Image-2.1-viggle-turbo-v0.2.1-6step-lora-r256_comfy.safetensors) ┊ [![][gh-t8star]](https://huggingface.co/t8star/Qwen-Image-2.1-viggle-turbo-4step-r64-comfy/resolve/main/qwen_image_2.1_viggle_turbo_v0.2.1_r256_comfy.safetensors) | The crisper of the two 6-step releases, and the last one with third-party ComfyUI conversions. Runs the demo Space. |
| **v0.2.1 LoRA r128** | 6 | ![bf16][badge-bf16] | 0.68 / 0.68 / 0.88 GB | [![][gh-Viggle]](https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo/resolve/main/Qwen-Image-2.1-viggle-turbo-v0.2.1-6step-lora-r128.safetensors) ┊ [![][gh-xingewh]](https://huggingface.co/xingewh/Qwen-Image-2.1-viggle-turbo-v0.2-5step-lora-r256_comfy/resolve/main/Qwen-Image-2.1-viggle-turbo-v0.2.1-6step-lora-r128_comfy.safetensors) ┊ [![][gh-t8star]](https://huggingface.co/t8star/Qwen-Image-2.1-viggle-turbo-4step-r64-comfy/resolve/main/qwen_image_2.1_viggle_turbo_v0.2.1_r128_comfy.safetensors) | Same adapter cut to rank 128; what the shipped ComfyUI workflows use. |
| **v0.2.1 adapter (peft)** | 6 | ![fp32][badge-fp32] | 2.72 GB | [![][gh-Viggle]](https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo/tree/main/peft_v0.2.1) | The v0.2.1 LoRA in PEFT key format, F32 as trained. |
| **v0.2 LoRA r256** | 5 / 6 | ![bf16][badge-bf16] | 1.36 GB | [![][gh-Viggle]](https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo/resolve/main/Qwen-Image-2.1-viggle-turbo-v0.2-5step-lora-r256.safetensors) ┊ [![][gh-chfm]](https://huggingface.co/chfm/Qwen-Image-2.1-viggle-turbo/resolve/main/Qwen-Image-2.1-viggle-turbo-v0.2-5step-lora-r256.safetensors) ┊ [![][gh-xingewh]](https://huggingface.co/xingewh/Qwen-Image-2.1-viggle-turbo-v0.2-5step-lora-r256_comfy/resolve/main/Qwen-Image-2.1-viggle-turbo-v0.2-5step-lora-r256_comfy.safetensors) | Step 600 of the same run. The `5step` in the name is the launch schedule; sample at 6 like v0.2.1. |
| **v0.2 LoRA r128** | 5 / 6 | ![bf16][badge-bf16] | 0.68 GB | [![][gh-Viggle]](https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo/resolve/main/Qwen-Image-2.1-viggle-turbo-v0.2-5step-lora-r128.safetensors) | Rank-128 cut of v0.2. |
| **v0.1 full fine-tune** | 4 | ![bf16][badge-bf16] | 14.23 GB | [![][gh-Viggle]](https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo/tree/main/transformer) | Merged transformer, no LoRA needed. This is what the GGUF quants above were built from. |
| **v0.1 LoRA r64** | 4 | ![bf16][badge-bf16] | 0.34 GB | [![][gh-Viggle]](https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo/resolve/main/Qwen-Image-2.1-viggle-turbo-4step-lora-r64.safetensors) ┊ [![][gh-t8star]](https://huggingface.co/t8star/Qwen-Image-2.1-viggle-turbo-4step-r64-comfy/resolve/main/Qwen-Image-2.1-viggle-turbo-4step-r64-comfyui-T8.safetensors) ┊ [![][gh-RunningHubAI]](https://huggingface.co/RunningHubAI/rh-qwen-image-2.1-viggle-turbo-4step-r64-comfyui-t8-lora/resolve/main/Qwen-Image-2.1-viggle-turbo-4step-r64-comfyui-T8.safetensors) | Superseded — diversity collapsed to 0.75× base and the output was visibly softer. Kept for reproducibility. |
| **Fun-Acc 4Step (PDD)** | 4 | ![bf16][badge-bf16] | 0.35 GB | [![][gh-alibaba--pai]](https://huggingface.co/alibaba-pai/Qwen-Image-2.1-Fun-Acc-LoRAs/resolve/main/models/Qwen-Image-2.1-Fun-Acc-4Step.safetensors) | **Official Alibaba PAI line**, rank 64, via Parallel Decoding Distillation. Independent of Viggle — 4 NFE for both T2I and instruction editing. | 
| **Pruna 8Step** | 8 | ![bf16][badge-bf16] | 0.34 GB | [![][gh-PrunaAI]](https://huggingface.co/PrunaAI/Pruna-Qwen-Image-2.1/resolve/main/p_qwen_image_2.1_8step_v0.1.safetensors) ┊ [![][gh-t8star]](https://huggingface.co/t8star/Pruna-Qwen-Image-2.1-Comfy/resolve/main/p_qwen_image_2.1_8step_v0.1-comfyui-T8.safetensors) | Third-party DMD line, rank 64 / alpha 128. Better of the two and the card's default, but v0.1 is marked work in progress. |
| **Pruna 5Step** | 5 | ![bf16][badge-bf16] | 0.34 GB | [![][gh-PrunaAI]](https://huggingface.co/PrunaAI/Pruna-Qwen-Image-2.1/resolve/main/p_qwen_image_2.1_5step_v0.1.safetensors) ┊ [![][gh-t8star]](https://huggingface.co/t8star/Pruna-Qwen-Image-2.1-Comfy/resolve/main/p_qwen_image_2.1_5step_v0.1-comfyui-T8.safetensors) | Same line, faster and visibly weaker. One adapter at a time — see the schedule note above. |
| **UltraFast 8Step** | 8 | ![bf16][badge-bf16] | 0.17 GB | [![][gh-Haverbex]](https://huggingface.co/Haverbex/Qwen-Image-2.1-UltraFast/tree/main/adapter) | Editing-focused rather than T2I, trained on MagicBrush. Rank 32, but loaded by the repo's own `inject_dit_lora` script, **not** a stock PEFT or ComfyUI loader. |
| **Turbo 4bit diffusers** | 8 | ![int4][badge-int4] | 11.41 GB | [![][gh-addlabsviral]](https://huggingface.co/addlabsviral/Qwen-Image-2.1-Turbo-4bit) | The official Turbo pipeline at bnb **NF4**: DiT 4.00 + TE 6.73 + VAE 0.68, same `QwenImage21Pipeline`, same saved 8-step sigmas and CFG 1 — the card bills it as the consumer-GPU build with base-model quality. Needs `accelerate` + `bitsandbytes` and diffusers from git. Replaces the author's earlier BF16/FP4 repos, which are no longer public. |
| **Turbo 8bit diffusers** | 8 | ![int8][badge-int8] | 17.82 GB | [![][gh-addlabsviral]](https://huggingface.co/addlabsviral/Qwen-Image-2.1-Turbo-diffuser-8bit) | torchao int8 weight-only over the same official Turbo: DiT 7.12 + TE 10.03 + VAE 0.68. Same 8 steps and CFG 1; needs `torchao` and the same pipeline-sigmas diffusers build. |
| **Turbo ONNX (browser)** | 4 | ![int4][badge-int4] | ~17.2 GB | [![][gh-cgb]](https://huggingface.co/cgb/Qwen-Image-2.1-Turbo-ONNX) | r64 LoRA merged into the denoiser, then Q4 MatMulNBits. WebGPU in-browser; needs the FreeGen pipeline and a desktop adapter. Experimental. |
| **v0.3 merged int8** | 6 | ![int8][badge-int8] | 7.26 GB | [![][gh-Viggle]](https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo/resolve/main/Qwen-Image-2.1-viggle-turbo-v0.3-6step-int8_convrot.safetensors) | Base transformer with the r256 LoRA merged in FP32, then quantized once. Goes in `models/diffusion_models/` with the stock loader. You still need the **Viggle Turbo Sigmas** node and the Comfy-Org text encoder and VAE. |
| **v0.3 merged fp8** | 6 | ![fp8][badge-fp8] | 7.25 GB | [![][gh-Viggle]](https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo/resolve/main/Qwen-Image-2.1-viggle-turbo-v0.3-6step-fp8_e4m3fn.safetensors) | Same, weight-only fp8 e4m3fn. Picks up the workflow's fp8 branch; the int8 file is the default. |
| **v0.3 merged Q8_0** | 6 | ![Q8_0][badge-Q8_0] | 7.69 GB | [![][gh-Viggle]](https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo/resolve/main/Qwen-Image-2.1-viggle-turbo-v0.3-6step-Q8_0.gguf) | Closest of the merged files to the LoRA path — needs ComfyUI-GGUF. Q6_K 6.00 GB, Q5_K_M 5.14 GB and Q4_K_M 4.34 GB sit in the same directory under the same naming. |
| **6NFE Distill** | 6 | ![fp32][badge-fp32] | 28.46 GB | [![][gh-Sutoonq]](https://huggingface.co/Sutoonq/Qwen-Image-2.1-6NFE-Distill/tree/main/transformer) | Full transformer distill in 8 shards, **297 tensors FP32** — no LoRA to load. Handles T2I and editing. **Needs `shift_terminal=0.4`** and conditional-only sampling (`true_cfg_scale=1.0`, no negative prompt) while keeping the base's dynamic shift, because the sixth evaluated sigma is 0.4. Ships its own `inference.py`; `--cpu-offload` trades speed for VRAM. Third-party, same research license. |
| **HDR full fine-tune** | 4 | ![bf16][badge-bf16] | 14.23 GB | [![][gh-yhzr2222]](https://huggingface.co/yhzr2222/qwen_image_2.1_bf16_hdr_ViggleHDR_noised) | Full-parameter fine-tune (**265 tensors, BF16**, single file) through a 3-stage curriculum: artistic style, then Chinese mythology/guofeng, then 4-step distillation. **The one row here that wants CFG above 1** — the card tests 2.5 as the sweet spot for contrast and saturation, where 1.0 is already sharp. 4 steps, or 20–30 if you want the extra detail; `euler`/`simple`. Goes in `models/unet/`. Marked experimental, and unlike everything else on this page the card carries a "generated by AI, for reference" note. |
| **UltraFast Q4_K** | 8 | ![Q4_K][badge-Q4_K] | 4.05 GB | [![][gh-Haverbex]](https://huggingface.co/Haverbex/Qwen-Image-2.1-UltraFast-GGUF/resolve/main/Qwen-Image-2.1-UltraFast-Q4_K.gguf) | DiT-only Q4_K with the UltraFast adapter **already merged** — do not stack the adapter on top. Still needs the text/vision encoders and the matching VAE. Quality and speed unbenchmarked. |
| **Pruna 8Step SDNQ** | 8 | ![int4][badge-int4] | 11.51 GB | [![][gh-SamuelTallet]](https://huggingface.co/SamuelTallet/Pruna-Qwen-Image-2.1-8steps-SDNQ-4bit-dynamic-hadamard256) | The Pruna 8-step adapter **merged** into the base and re-quantized with [SDNQ](https://github.com/Disty0/sdnq) — UINT4 dynamic, Hadamard rotation at group size 256. Full diffusers pipeline (DiT 4.10 + TE 6.74 + VAE 0.68), so the text encoder is quantized too. Needs SDNQ 0.2.0+, Triton and diffusers from git. Follows the Pruna sigma schedule above. |
| **Official Turbo diffusers** | 8 | ![bf16][badge-bf16] | 32.44 GB | [![][gh-Qwen]](https://huggingface.co/Qwen/Qwen-Image-2.1-Turbo) | The reference 8-step checkpoint itself (listed in full under [official checkpoints](#official-turbo)): CFG 1.0, schedule carried in the weights, prefix KV cache on. Point of comparison for every row below — the community lines above trade its fidelity for size, speed or a different look. |
| **Merged 8Step (BF16)** | 8 | ![bf16][badge-bf16] | 14.23 GB | [![][gh-Zabin]](https://huggingface.co/Zabin/Qwen_Image_2.1_Turbo_8Steps/resolve/main/QwenImage_2.1_bf16_turbo_8Steps_v1.safetensors) | A home-made merge, not a distillation: base BF16 with three adapters baked in — Viggle v0.2.1 r128 at 0.75, Viggle v0.1 r64 at 0.15, and the community Turbo8 LoRA at 0.2. Single 265-tensor file for `models/diffusion_models/`, so no LoRA to load. The card warns of anatomical errors and grid noise, and the recipe inherits the Viggle v0.1 branch's softer look. The repo also keeps the rank-128 adapter SVD-extracted back out of this merge (0.64 GB) if you would rather run it on the stock base. |
| **Merged 8Step (int8)** | 8 | ![int8][badge-int8] | 7.16 GB | [![][gh-Zabin]](https://huggingface.co/Zabin/Qwen_Image_2.1_Turbo_8Steps/resolve/main/QwenImage_2.1_turbo_8Step_Int8_Convrot_v1.safetensors) | The same merge in int8 ConvRot — 196 `I8`/`U8` tensor pairs with F32 scales, 69 tensors left BF16. Half the VRAM of the BF16 file above; the merge recipe is identical, so expect the same caveats. |
| **Merged 5Step (int8)** | 5 | ![int8][badge-int8] | 7.16 GB | [![][gh-Zabin]](https://huggingface.co/Zabin/Qwen_Image_2.1_Turbo_8Steps/resolve/main/qwen_image2.1_turbo_5Steps_int8_convrot_v3.safetensors) | The author's 5-step take, v3 of the same repo. Generation and editing from one file; nothing in the card separates its quality from the 8-step builds, so treat the step count as unvalidated. |
| **MFD research LoRA** | 2–12 | ![bf16][badge-bf16] | 0.07 GB | [![][gh-congruency]](https://huggingface.co/congruency/Qwen-Image-2.1-turbo-mfd) | Mean Flow Distillation (the paper the card cites is arXiv 2606.11155) instead of DMD — six snapshots of one run, `v0.1`–`v0.6`, all 0.07 GB, spanning 2–12 steps; **v0.5 is the card's general-use pick** (4–6 steps) and v0.6 is the 2-step experiment. Trained on a single 4090. ComfyUI wants plain `euler` / `sgm_uniform` with no shift, no manual sigmas and no custom node; diffusers loads it with the standard LoRA API. |
| **T8 HiFi v001** | 8 | ![f16][badge-f16] | 19.56 GB | [![][gh-t8star]](https://huggingface.co/t8star/Qwen-Image-2.1-Turbo-Hifi-Comfy/resolve/main/qwen_image_2.1_turbo_lora_hifi_T8_v001.safetensors) | The Turbo delta itself, saved as an adapter: the official Turbo-minus-base weight difference, lifted out by adaptive-rank SVD (665 tensors — F16 LoRA factors plus F32 vector diffs) instead of being trained. Preserves ~99.9% of the update energy, which is why it costs 19.56 GB — bigger than the DiT it patches. Load on the **base** BF16 model with `LoraLoaderModelOnly` at strength 1.0; never on a full Turbo model and never beside another Turbo LoRA. The sigma schedule is mandatory: `1.0, 0.978453, 0.95418, 0.926626, 0.89508, 0.845148, 0.704534, 0.414568, 0` through `ManualSigmas`, Euler, CFG 1. |
| **T8 HiFi compact (r512 / r768 / r896)** | 8 | ![f16][badge-f16] | 2.61 / 3.91 / 4.56 GB | [![][gh-t8star]](https://huggingface.co/t8star/Qwen-Image-2.1-Turbo-Hifi-Comfy) | The same extraction with the rank capped at 512 / 768 / 896, cutting the file to a quarter of v001. The card is blunt that this is **lossy**: 53–64% of the delta energy survives, against v001's 99.9%, and the v001 guarantee does not carry over. Same loader, same mandatory sigma grid. Pick by budget; the card's own PSNR ladder shows the bigger caps closer to the full Turbo output, not across the board. |
| **LightX2V Lightning** | 4 | ![fp32][badge-fp32] | 0.07 GB | [![][gh-lightx2v]](https://huggingface.co/lightx2v/Qwen-Image-2.1-Lightning/resolve/main/pytorch_lora_weights.safetensors) | A 4-step DMD adapter from the LightX2V project, trained on 16 Ascend 910B NPUs, covering both generation and editing. Wants `FlowMatchEulerDiscreteScheduler` with `shift_terminal=None` and the fixed grid `sigmas=[1.0, 0.75, 0.5, 0.25]`, CFG 1.0, prefix KV cache off. diffusers-only — the card shows `load_lora_weights` and no ComfyUI path. F32-stored factors, and the repo declares no license. |

<p id="lora" align="center">◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆</p>

## ◉ LoRA &amp; adapters

Style, control, and fix adapters. All target the base DiT unless noted. Grouped by type, then by size.

| Name | Type | Precision | Size | Links | Notes |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **ControlNet-Union** | ![Control][ltype-control] | ![bf16][badge-bf16] | 7.55 GB | [![][gh-alibaba--pai]](https://huggingface.co/alibaba-pai/Qwen-Image-2.1-Fun-Controlnet-Union/resolve/main/Qwen-Image-2.1-Fun-Controlnet-Union.safetensors) ┊ [![][gh-t8star]](https://huggingface.co/t8star/Qwen-Image-2.1-Fun-Controlnet-Union-Comfy/resolve/main/Qwen-Image-2.1-Fun-Controlnet-Union-ComfyUI.safetensors) | **Official Alibaba PAI / VideoX-Fun.** One checkpoint for 8 conditions (Canny, Depth, Grayscale, HED, Lineart, MLSD, Pose, Scribble) plus inpainting. Control branch only, 16 injection points, loaded `strict=False`. The t8star link is the same weights re-saved under ComfyUI naming, for 368 bytes more. ComfyUI users can skip both and take the `model_patches/` cut from Comfy-Org above, which also has an int8 build at 3.78 GB. |
| **Object Mover Bbox Preview** | ![Control][ltype-control] | ![bf16][badge-bf16] | 0.50 GB | [![][gh-prithivMLmods]](https://huggingface.co/prithivMLmods/Qwen-Image-2.1-Object-Mover-Bbox-Preview) | Bbox object *moving*, 6 checkpoints. |
| **Object Remover Bbox Preview** | ![Control][ltype-control] | ![bf16][badge-bf16] | 0.50 GB | [![][gh-prithivMLmods]](https://huggingface.co/prithivMLmods/Qwen-Image-2.1-Object-Remover-Bbox-Preview) | Bbox object removal, full-quality variant. |
| **Object Remover Bbox turbo** | ![Control][ltype-control] | ![bf16][badge-bf16] | 0.42 GB | [![][gh-prithivMLmods]](https://huggingface.co/prithivMLmods/Qwen-Image-2.1-Object-Remover-Bbox-turbo) | 4-step-compatible variant. |
| **BFS Head Swap v1** | ![Control][ltype-control] | ![bf16][badge-bf16] | 0.32 GB | [![][gh-Alissonerdx]](https://huggingface.co/Alissonerdx/BFS-Best-Face-Swap/resolve/main/bfs_head_v1_qwen_2.1.safetensors) | Head replacement, **not** a whole-face blend: identity, hair, eye colour and nose come from image 2 while gaze direction, head rotation and expression stay with image 1. Rank 64, 5,000 steps, MIT. **Image order is load-bearing** — swapping the two inputs swaps who is retargeted. Trigger with the `head_swap:` prefix. The repo's other 17 adapters target Qwen Image Edit 2509/2511, Flux 2 Klein, Krea 2 and LTX-2, not this base. |
| **Multiple Angles** | ![Control][ltype-control] | ![f16][badge-f16] | 0.32 GB | [![][gh-akhaliq]](https://huggingface.co/akhaliq/Qwen-Image-2.1-Multiple-Angles-LoRA/resolve/main/checkpoints_v2%2Fangles_v2_full_qwen21_multiple_angles_v2_qwen21_multiple_angles_v2_000001500.safetensors) ┊ [![][gh-akhaliq]](https://huggingface.co/akhaliq/Qwen-Image-2.1-Multiple-Angles-LoRA/resolve/main/multiple_angles_step1000.safetensors) | Reshoot a subject from a named camera position: trigger `<mva>` followed by an angle and height — `front-right quarter view, eye-level shot`, `back view`, `high-angle`, `top-down`, each with a `close-up` variant. Start at strength **1.0** and drop to 0.8 if the output drifts into copying the reference. **v2 (rank 64, step 1500, linked first) is the one to take** — trained on 13,328 pairs with rigged characters, so it holds identity on people where v1 softens. The second link is v1 step 1000 (rank 32), still the better choice if v2 over-bakes the angle. Not interchangeable with the fixed-prompt `Orbit Alpha` above, which needs a 3D render as its second input. |
| **Next Scene** | ![Control][ltype-control] | ![f16][badge-f16] | 0.32 GB | [![][gh-akhaliq]](https://huggingface.co/akhaliq/Qwen-Image-2.1-Next-Scene-LoRA/resolve/main/next_scene_step2500.safetensors) | Directs the *next shot* rather than a new angle: start the prompt with `Next Scene:` and lead with the camera move — `Next Scene: The camera tracks forward and tilts down as rain begins to streak the lens.` Keep the world, characters and palette while the camera moves, reveals or relights. Strength **0.7–0.9**, 28–40 steps, CFG 1. Chain each output back in as the next input to build a storyboard; if a hop copies its input too closely, drop toward 0.7. The Qwen-Image-2.1 port of a format that only existed on the 2509 edit model. Pairs with Multiple Angles above: where the camera is, and where the story goes. |
| **QMA camera angles** | ![Control][ltype-control] | ![bf16][badge-bf16] | 0.32 GB | [![][gh-gribbliest]](https://huggingface.co/gribbliest/qwen-image-2.1-qma-camera-angles/resolve/main/qwen-image-2.1-qma-camera-angles.safetensors) | Orbits the camera around the subject you keep: trigger `<qma>` then one pick each from azimuth / elevation / distance — `right side view eye-level shot medium shot` — with directions taken from the **original camera**, not the subject. Rank 64, 3,000 steps at 512/1024 on photo + Blender pairs, ai-toolkit. Strength 1.0, 30 steps, CFG 3, `euler`/`simple`, source image as the reference, ~1 MP out. **Apache-2.0.** A [drag-the-camera node](https://github.com/CoreyCorza/QMA-Multi-Angle-Lora-Node) can write the prompt for you. Quarter views, elevated shots and distance changes are the most reliable; wide orbits on landscape scenes can stop short of 90°, and anything the source does not show has to be invented. |
| **Orbit Alpha** | ![Control][ltype-control] | ![bf16][badge-bf16] | 0.17 GB | [![][gh-ML--Intern--lab]](https://huggingface.co/ML-Intern-lab/Qwen-Image-2.1-viewpoint-orbit-LoRA/resolve/main/checkpoints/steps2000res768/orbit_alpha_lora_gate_up_split.safetensors) | **Official ML-Intern-lab.** One RGBA image in, the same object from a new viewpoint out. Rank 32, 2,000 steps at 768 px. Use the `_gate_up_split` file — the other checkpoint in the repo does not load correctly. `<orbit>` grammar, 40 steps, no CFG. |
| **FG extract v4** | ![Control][ltype-control] | ![bf16][badge-bf16] | 0.17 GB | [![][gh-trmz]](https://huggingface.co/trmz/qwen-image-2.1-fg-extract-lora/resolve/main/qwen-image-2.1-fg-extract-v4.safetensors) | Cuts a masked element out as an **RGBA cutout** at the input's exact size and position — it extracts rather than redraws. Built on the **Viggle turbo** base, so **4 steps, no CFG**; ~2 s at 512², ~9 s at 1024² with cleaner edges. You supply the mask (SAM, box, or a detector): image 1 is the original dimmed to 20% outside the mask, image 2 is the plain RGB original. Do **not** pass the mask itself as an input image or it gets copied into the result. Needs an alpha-capable VAE for transparency. v3 is the fixed-prompt fallback. |
| **Doodle-in** | ![Control][ltype-control] | ![f16][badge-f16] | 0.17 GB | [![][gh-ML--Intern--lab]](https://huggingface.co/ML-Intern-lab/Qwen-Image-2.1-doodle-in-LoRA/resolve/main/doodle_in_lora_qwen21_gate_up_split.safetensors) | Turns a magenta scribble into the object you name, keeping its shape and pose. **Diffusers users want the linked `_gate_up_split` file** — ai-toolkit's fused `img_mlp.gate_up` is silently dropped otherwise, loading 384 of 448 modules. In ComfyUI use `doodle_in_lora_qwen21.safetensors` instead. Marker is pure magenta RGB (255, 0, 255) at 3–7 px. Now published by ML-Intern-lab, the same lab as the Orbit row above. |
| **Outpaint v2** | ![Control][ltype-control] | ![bf16][badge-bf16] | 0.16 GB | [![][gh-ausboss]](https://huggingface.co/ausboss/Qwen-Image-2.1-Outpaint-LoRA/resolve/main/qwen-image-2.1-outpaint-v2.safetensors) | Pad the picture with flat `#808080`, hand the padded canvas to the model as the reference; the adapter fills the gray and keeps the original pixel-registered. One side, a corner, or all four. Rank 32, ComfyUI keys, 2,000 steps. 25 steps, CFG 1, `resolution` 0, target 1–2 MP. Do **not** pin the known area with a latent noise mask — on this model it draws a visible rectangle at the seam. |
| **Outpaint v1** | ![Control][ltype-control] | ![bf16][badge-bf16] | 0.16 GB | [![][gh-ausboss]](https://huggingface.co/ausboss/Qwen-Image-2.1-Outpaint-LoRA/resolve/main/qwen-image-2.1-outpaint.safetensors) | Same adapter one step earlier, trained at ≤1 MP over more extreme zoom-outs. The better of the two on very large extensions; the two are within noise on ordinary crops. The repo also keeps the step-500 and step-1250 intermediates. |
| **Pano 360** | ![Control][ltype-control] | ![bf16][badge-bf16] | 0.16 GB | [![][gh-Gogodr]](https://huggingface.co/Gogodr/qwen-image-2.1-edit-pano360-lora/resolve/main/pano360_qwen21_edit_v1.safetensors) | Turns 1–3 ordinary photos taken from one spot into a **2:1 equirectangular 360 panorama** for a viewer, VR photo or skybox, inventing what was behind the camera. Trained on CC0 Poly Haven HDRIs; prompt is "Transform this set of images into an equirectangular 360 panorama. Scene: …". **Image order decides placement** — the first view is always the centre of the sphere. Output 1536×768 loses fine detail relative to the input views. |
| **AnyAngle** | ![Control][ltype-control] | ![bf16][badge-bf16] | 0.12 GB | [![][gh-lilylilith]](https://huggingface.co/lilylilith/QI_2.1_AnyAngle/resolve/main/QI2.1_AnyAngle.safetensors) | Arbitrary camera-angle change, not the fixed azimuth/elevation of Orbit Alpha. Image 1 is the photo whose content and style you keep; image 2 is a **coarse render from the angle you want**, typically shot from a Gaussian splat or 3D model in Blender. Prompt is literally "Change the camera angle from `<image2>` to `<image1>`". **Strength 1, CFG 3.0, 20+ steps** — the only adapter here that wants CFG above 1. Quality is bounded by the splat: a bad reconstruction puts objects in the wrong place. |
| **Realism edit** | ![Control][ltype-control] | ![bf16][badge-bf16] | 0.04 GB | [![][gh-houseofboern]](https://huggingface.co/houseofboern/realism-qwen-image-2.1-edit-lora/resolve/main/realism-qwen-image-2.1-edit-lora-e8.safetensors) | Nudges an AI-looking photo toward a real phone shot — but only in **tone and colour**, not detail. From the same author as the LoKR row below, and a **different repo**: that one is generation-time, this one is an edit adapter. Rank 8, `LoraLoaderModelOnly` at 1.0. **Use the exact prompt `convert this into a real phone photo`** — it is the only caption it saw, so extra style words dilute it and an empty negative prompt is required. Trained at 0.5 MP, so set the encoder resolution near **768**, and sample **25 steps, CFG 1**. A separate entry from the `Fix` pair despite the similar name. |
|  |  |  |  |  |  |
| **Fix Opinionated** | ![Fix][ltype-fix] | ![fp32][badge-fp32] | 0.50 GB | [![][gh-e--n--v--y]](https://huggingface.co/e-n-v-y/Qwen-Image-2.1-Fix-Opinionated-v1.0/resolve/main/qwen2.1-detail-fix-opinionated-v1.0.safetensors) | The same fix, dialled up: cleans the noise **and shifts composition**, which the card states plainly. Rank 16 adapters stored in **F32**, which is why it is roughly 10× the size of Fix v2.0 for the same idea — halve it with any quantizer if the size matters more. Take this one when v2.0 leaves grain behind; take v2.0 when you want the frame left alone. |
| **Anime consistency** | ![Fix][ltype-fix] | ![bf16][badge-bf16] | 0.17 GB | [![][gh-RunningHubAI]](https://huggingface.co/RunningHubAI/rh-qwen-image-2.1-loras-lora/resolve/main/Qwen2.1_Anime_consistency.safetensors) | Character consistency while restyling anime images, trained from 4-view reference sheets. **The author marks it experimental** — start LoRA weight at 0.6–0.8. Diffusers keys with a `transformer_blocks.` prefix, no `diffusion_model.`. |
| **Background perspective** | ![Fix][ltype-fix] | ![bf16][badge-bf16] | 0.16 GB | [![][gh-RunningHubAI]](https://huggingface.co/RunningHubAI/rh-qwen-image-2.1v2.0-lora/resolve/main/qwen-image-2.1%E7%BA%A0%E6%AD%A3%E8%83%8C%E6%99%AF%E9%80%8F%E8%A7%86%E6%BA%B6%E5%9B%BEv2.0.safetensors) | Fixes the one thing compositing usually breaks: a cut-out subject sitting in a background whose perspective disagrees with theirs. Trigger `pysj666`, then `keep the subject position and size unchanged, adjust the background perspective angle to align with the subject's vanishing point`. Trained from ModelScope's X MuseAI set. Rank 16. |
| **Outfit Swap Consistency** | ![Fix][ltype-fix] | ![bf16][badge-bf16] | 0.16 GB | [![][gh-ausboss]](https://huggingface.co/ausboss/Qwen-Image-2.1-Outfit-Swap-Consistency-LoRA/resolve/main/qwen-image-2.1-outfit-swap.safetensors) | Virtual try-on that keeps the picture pinned: on 16 unseen swaps the result sat **0.1 px** from the original instead of 3.6 px, face pixels changing 1.7% instead of 14.1%, background 0.9% instead of 10.8%. Same author's drift-fix family as Edit consistency below, aimed at a different edit. **Strength 1.0** — at 0.5 half the drift returns. Person as image 1, outfit as image 2; the card's prompt keeps face, hair, hands, pose and background explicit. Ships a ComfyUI workflow; also on Civitai. |
| **Edit consistency** | ![Fix][ltype-fix] | ![bf16][badge-bf16] | 0.16 GB | [![][gh-ausboss]](https://huggingface.co/ausboss/Qwen-Image-2.1-Consistency-LoRA/resolve/main/qwen-image-2.1-consistency.safetensors) | Stops edits from resizing or nudging the picture — the same drift Outpaint fixes, from the opposite side. No trigger word, so it composes with any edit prompt. The card measures worst-corner drift falling from 24.3 px to 1.6 px on restyles. Rank 32. The linked step-1500 file keeps Qwen's own look; a step-2000 file in the repo aligns tighter but washes colour out. |
| **COS auto-retouching v2** | ![Fix][ltype-fix] | ![bf16][badge-bf16] | 0.16 GB | [![][cv-l15625089091628]](https://civitai.com/models/2975411/cosv2cos-auto-retouching-v2?modelVersionId=3372259) | One-step automatic retouching for real-life cosplay photographs — skin and colour cleanup without manual masking. The card is Chinese-only, with a Bilibili demo. **Download requires a Civitai login.** |
| **Fix** | ![Fix][ltype-fix] | ![bf16][badge-bf16] | 0.11 GB | [![][gh-e--n--v--y]](https://huggingface.co/e-n-v-y/Qwen-Image-2.1-Fix/resolve/main/qwen-image-2.1-fix-1.0-comfy.safetensors) | The most-liked community LoRA. |
| **Deblur anything** | ![Fix][ltype-fix] | ![bf16][badge-bf16] | 0.08 GB | [![][cv-Luntrix]](https://civitai.com/models/2975487/deblur-anything?modelVersionId=3372351) | Removes defocus blur — even heavy blur — and reconstructs what was behind it, which is a trained guess rather than a recovery. Trigger `Wibble snargle floof` (deliberately nonsense). Trained on Gaussian blur only, so it does **not** fix a lanczos-resized image or a bokeh background — that is the row below. The samples run Viggle Turbo at 8 steps; for quality use 20 steps without turbo at CFG 2–4. |
| **Remove bokeh** | ![Fix][ltype-fix] | ![bf16][badge-bf16] | 0.08 GB | [![][cv-Luntrix]](https://civitai.com/models/2976381/edit-remove-bokeh-remove-blur-sharp-background?modelVersionId=3373431) | Puts a background the camera threw out of focus back into sharpness. Trigger `remove blur, sharp background`. The page ships two files: **lite** is more natural and can fail to remove the blur, **strong** sharpens harder with less detail. **Download requires a Civitai login.** |
| **Watermark removal** | ![Fix][ltype-fix] | ![bf16][badge-bf16] | 0.07 GB | [![][cv-saladin]](https://civitai.com/models/2969142/watermark-removal-lora?modelVersionId=3364468) | Removes watermarks where plain Qwen 2.1 repaints the whole image around them. Prompt `Remove the watermarks`, no trigger word; the card asks for responsible use. |
| **Fix v2.0** | ![Fix][ltype-fix] | ![bf16][badge-bf16] | 0.05 GB | [![][gh-e--n--v--y]](https://huggingface.co/e-n-v-y/Qwen-Image-2.1-Fix-v2.0/resolve/main/qwen2.1-detail-fix-2.0.safetensors) | The author's own rerun, at rank 8 — a quarter of the size of v1.0 and the smallest Fix here. The card is bare, so treat strength and sampler as untested. |
| **Unblur background** | ![Fix][ltype-fix] | ![bf16][badge-bf16] | 0.04 GB | [![][gh-houseofboern]](https://huggingface.co/houseofboern/unblur-background-qwen-image-2.1-edit-lora/resolve/main/unblur-background-qwen-image-2.1-edit-lora.safetensors) | Puts a shallow-depth-of-field background back into focus while the subject, pose, clothes and framing stay put — it does not repair motion blur on the subject, add grain or relight. Rank 8 on 17 paired shots, epoch 2 (step 34), trained on square 1024×1024 crops. One fixed caption — `bring the background into sharp focus and full detail` — at strength 1.0, 25 steps, CFG 1, `euler`/`simple`, on the **BF16 base, not Turbo**; the shipped workflow needs ComfyUI-KJNodes for the crop. Early days: the author has run it on three unseen previews and no example images are published. |
|  |  |  |  |  |  |
| **De-AI LoRA pack** | ![Style][ltype-style] | ![bf16][badge-bf16] | 2.45 GB | [![][gh-RunningHubAI]](https://huggingface.co/RunningHubAI/rh-qwen-image-2.1ai-lora) | 8-file "remove the AI look" pack (CN filenames). |
| **Natural Exposure LoRA** | ![Style][ltype-style] | ![bf16][badge-bf16] | 0.42 GB | [![][gh-prithivMLmods]](https://huggingface.co/prithivMLmods/Qwen-Image-2.1-Natural-Exposure-LoRA) | Exposure correction, 5 checkpoints. |
| **Anything2RealCharacters** | ![Style][ltype-style] | ![bf16][badge-bf16] | 0.30 GB | [![][cv-AIGC--Singularity]](https://civitai.com/models/2808492/anything2realcharacters?modelVersionId=3363600) | V3 of the Krea2 Anything2Real series, now published as a LoRA rather than merged weights: turns 2D, anime or painted input into a photorealistic character with skin micro-texture and facial detail, and is built to stack with external Krea2 style or character LoRAs. Trigger `photorealistic,transform the image to realistic photograph`. **Download requires a Civitai login.** |
| **Clay Sculpture** | ![Style][ltype-style] | ![bf16][badge-bf16] | 0.25 GB | [![][gh-prithivMLmods]](https://huggingface.co/prithivMLmods/Qwen-Image-2.1-Clay-Sculpture-Style/resolve/main/Qwen-Image-2.1-Clay-Sculpture-Style-2000.safetensors) | Rank 16, 3 checkpoints, trained at 1 MP from ModelScope's X MuseAI set. Trigger `Transform the image into a clay sculpture style`. Diffusers-style keys (`pipe.dit.` prefix stripped), so ComfyUI needs no rename. |
| **Voxel** | ![Style][ltype-style] | ![bf16][badge-bf16] | 0.25 GB | [![][gh-prithivMLmods]](https://huggingface.co/prithivMLmods/Qwen-Image-2.1-Voxel-Style/resolve/main/Qwen-Image-2.1-Voxel-Style-2000.safetensors) | Same author's voxel-cube treatment, same rank and 3-checkpoint layout. |
| **Amethyst Theme** | ![Style][ltype-style] | ![bf16][badge-bf16] | 0.25 GB | [![][gh-prithivMLmods]](https://huggingface.co/prithivMLmods/Qwen-Image-2.1-Amethyst-Theme/resolve/main/Qwen-Image-2.1-Amethyst-Theme-2000.safetensors) | Same series again, this one amethyst/mystical. All three repos are independently trained, not stacked — pick one per pass. |
| **Outrun** | ![Style][ltype-style] | ![bf16][badge-bf16] | 0.25 GB | [![][gh-prithivMLmods]](https://huggingface.co/prithivMLmods/Qwen-Image-2.1-Outrun/resolve/main/Qwen-Image-2.1-Outrun-2000.safetensors) | Neon-noir synthwave: magenta/cyan rim light, heavy contrast, 1980s film look. Rank 16, 3 checkpoints, **image-to-image** — trigger `Transform the image into an outrun theme`. The card marks it an experimental preview and says results vary with the input's lighting and silhouettes, so it wants a well-lit source. |
| **Heatwave** | ![Style][ltype-style] | ![bf16][badge-bf16] | 0.25 GB | [![][gh-prithivMLmods]](https://huggingface.co/prithivMLmods/Qwen-Image-2.1-Heatwave/resolve/main/Qwen-Image-2.1-Heatwave-2000.safetensors) | The same author's thermal-shimmer look, same rank 16 and 3-checkpoint layout. Trigger `Apply a heatwave theme to the image`. |
| **Casual phone photo** | ![Style][ltype-style] | ![bf16][badge-bf16] | 0.17 GB | [![][gh-19nbrown]](https://huggingface.co/19nbrown/qwen-image-2.1-casual-phone-photo-style-lora/resolve/main/lbxstyle-qwen-image-2.1-step-1890.safetensors) | Rank 32 on a small 126-pair set — the card calls it a single-run fine-tune and suggests comparing a few LoRA scales before committing to a batch. Trigger `lbxstyle`, start at **scale 0.8**. Text-to-image, so it adds the aesthetic rather than restyling a reference. |
| **Product relight** | ![Style][ltype-style] | ![bf16][badge-bf16] | 0.17 GB | [![][gh-RunningHubAI]](https://huggingface.co/RunningHubAI/rh-qwen-image-2.1-lora-2104918997757157378/resolve/main/Qwenimag21_c2-st2000.safetensors) | Lights a product or object so it sits in its background: matching speculars, front-to-back falloff, a real contact shadow. **Trigger `pengyu` at the very start of the prompt** or it does nothing. The card documents no sampler or strength range, so treat the defaults as untested. |
| **De-AI + lighting v5** | ![Style][ltype-style] | ![bf16][badge-bf16] | 0.17 GB | [![][gh-RunningHubAI]](https://huggingface.co/RunningHubAI/rh-qwen-image-2.1-lora-2071763057486946305/resolve/main/Qwen%20Image%202.1%E5%8E%BB%E9%99%A4ai%2B%E5%85%89%E5%BD%B1%E4%BC%98%E5%8C%96v5.safetensors) | Two revisions of the same de-AI + lighting adapter; v5 is the newer. The repo also has two lighting-only adapters, 0.24 and 0.09 GB. CN filenames. |
| **Dot Film** | ![Style][ltype-style] | ![fp32][badge-fp32] | 0.17 GB | [![][gh-foprc]](https://huggingface.co/foprc/Dot-Film-Qwen-Image-2.1/resolve/main/dot-film-v0.1-qwen-image-2.1-step1000.safetensors) | Direct-flash 35 mm point-and-shoot look — hard frontal flash, bright skin, a sharp shadow behind the subject, coarse grain, uneven exposure; night trains and late-night street portraits are its home ground. One training run cut at 500 / 750 / 1000 updates, **all three in the repo** (the step-1000 file is linked); the card compares them on the same seven prompts and says plainly that more steps is *not* proven better — switching checkpoint can change face, clothes and pose. Rank 16 on 64 online photographs whose licences the author did not verify, DiffSynth-Studio, F32-stored hence the size. Strength 1.0, CFG 1 on the flash scenes and 2–3 on the rest. |
| **ZZZ style** | ![Style][ltype-style] | ![bf16][badge-bf16] | 0.16 GB | [![][gh-wesjos]](https://huggingface.co/wesjos/Qwen-Image2.1-ZenlessZoneZero-Lora/resolve/main/zzz_style_v1.7_4500.safetensors) | Zenless Zone Zero-inspired look, rank 32 / alpha 64, **Apache-2.0**. **Strength 0.8 is the card's sweet spot**; 0.6–0.8 for lighter influence, above 1.0 it starts overriding your composition. 25 steps, CFG 4.3, `euler`/`simple`, shift 3.1, empty negative. The repo now carries three families: **v1.7** (rank 16, 0.08 GB, 2 checkpoints — the card's pick for editing), **v1.6** (5 checkpoints) and **v1.4** (the older 4). Card guidance is v1.6/v1.7/v1.4 for text-to-image and **v1.7 over v1.6 for edits**. Triggers `zenlesszonezero` (1.6) / `zzz_style` (1.4) are optional. For edits, denoise 0.5–0.7 restyles hard, 0.3–0.5 keeps more linework, and inputs under ~512 px smear — upscale first. Trained on the Comfy-Org int8 base and mostly single-girl portraits, so multi-character and male subjects generalize poorly. |
| **Genshin TCG 2D** | ![Style][ltype-style] | ![f16][badge-f16] | 0.16 GB | [![][gh-wesjos]](https://huggingface.co/wesjos/Qwen-Image2.1-Genshin-2D-Lora/resolve/main/genshintcg_style_st3500.safetensors) | Trading-card anime rendering rather than illustration: flat cel shading, hard outlines, the card-frame proportions of Genshin Impact's TCG. Trigger `genshintcg_style`. Works in **both** text-to-image and image editing, so it restyles a photo or generates from scratch. Rank 16, 3 checkpoints. **Trained on `qwen_image_2.1_int8_convrot`** — the author asks that you use it as the base model. Apache-2.0. |
| **Qingqing** | ![Style][ltype-style] | ![bf16][badge-bf16] | 0.16 GB | [![][gh-RunningHubAI]](https://huggingface.co/RunningHubAI/rh-qwen-image-2.1-2500-lora/resolve/main/Qingqing_000002500.safetensors) ┊ [![][gh-RunningHubAI]](https://huggingface.co/RunningHubAI/rh-qwen-image-2.1-qingqing-2750-lora/resolve/main/Qingqing_000002750.safetensors) | A named character LoRA, trigger `Qingqing`. Two checkpoints of the same training run are published as separate repos: step 2500 (linked first) and step 2750, the run's final step. They are distinct files, so pick by budget rather than by capability — there is no card guidance separating them. Rank 16. |
| **Ricklistic Anime to real** | ![Style][ltype-style] | ![bf16][badge-bf16] | 0.15 GB | [![][cv-RICK666]](https://civitai.com/models/2964789/ricklistic-anime-to-real?modelVersionId=3359189) | Converts anime and manga art into a realistic rendering while keeping the composition. Trigger `Realistic`, and keep the prompt simple — the card only asks that the image be turned into a realistic style. Full-body shots drift toward a 3D look, so start from a good base image. Card is Chinese and English. **Download requires a Civitai login.** |
| **MoreReal** | ![Style][ltype-style] | ![bf16][badge-bf16] | 0.15 GB | [![][cv-NO8D]](https://civitai.com/models/2904424/morereal?modelVersionId=3374264) | Any-image-to-photograph adapter trained across many painting styles. Trigger `photorealistic`, weight **0.6–0.9**, 30–40 steps. The public file is the beta build trained at 768 px; a 1536 px build sits on the author's Patreon. **Download requires a Civitai login.** |
| **Manga to Real People V1** | ![Style][ltype-style] | ![bf16][badge-bf16] | 0.15 GB | [![][cv-qingfengy36939]](https://civitai.com/models/2984825/qwen-image-21-manga-to-real-people-v1?modelVersionId=3383994) | Paired manga-to-photo training that keeps composition, pose, clothing and scene while replacing the rendering. The card's tested settings: strength **1.0**, 25 steps, CFG **1.0**, `euler`/`simple`, encoder resolution **1536** — an area budget rather than an edge cap. Beta: expressions, eye state, mouth shape, iris colour and small accessories can shift, and skin often comes back smoother. |
| **Sts2 Cards Drawer** | ![Style][ltype-style] | ![fp16][badge-f16] | 0.10 GB | [![][gh-Airmongsity]](https://huggingface.co/Airmongsity/Qwen-Image-2.1-Sts2-Cards-Drawer) | `deckbuilder_cardart_style_lora_v1_fp16`. |
| **ZZZ chibi** | ![Style][ltype-style] | ![f16][badge-f16] | 0.08 GB | [![][gh-wesjos]](https://huggingface.co/wesjos/Qwen-Image2.1-ZenlessZoneZeroChibi-Lora/resolve/main/zzz_chibi_v2_st2500.safetensors) | Compresses proportions to chibi rather than just restyling. Rank 16, F16, all 32 layers. **Take `st2500` at strength 0.70**; st2000 is gentler, st3000 flattens clothing detail. Trained on the **Comfy-Org int8 ConvRot** base, so expect slightly less fine detail than an FP16-trained LoRA. Separate from the ZZZ style row — not a stacked pair. |
| **2anime** | ![Style][ltype-style] | ![bf16][badge-bf16] | 0.08 GB | [![][gh-NicknickAI]](https://huggingface.co/NicknickAI/QwenImage2.1-2anime/resolve/main/2anime-QwenImage2.1.safetensors) | Photo to anime, **image-to-image**, at 4,000 steps — the most heavily trained adapter in this group. Trigger `2anime`, LoRA weight 1, and only **8 steps at CFG 1**. The card is otherwise bare, so treat the sampler as untested. |
| **Canon UltraReal** | ![Style][ltype-style] | ![f16][badge-f16] | 0.07 GB | [![][cv-Danrisi]](https://civitai.com/models/2783143/canon-ultrareal?modelVersionId=3352035) | Reproduces the look of the author's own Canon 1Ds full-frame photographs: rich colour, distinctive rendering, deep bokeh. Trained on 28, 50, 100 and 500 mm lenses, so the character of the look follows the focal length you describe. Trigger `c2n0n` at strength **0.7**, with a detailed prompt — the trigger alone does little, and the card asks you to describe the out-of-focus foreground and background. |
| **GrainScape UltraReal** | ![Style][ltype-style] | ![f16][badge-f16] | 0.07 GB | [![][cv-Danrisi]](https://civitai.com/models/1332651/grainscape-ultrareal?modelVersionId=3352222) | Coarse film grain with deeper colour. The card notes the newer builds cut the vertical banding on flat textures, keep the black-and-white moody look, and fix a repeated-face problem. Strength **0.7**. |
| **NiceGirls UltraReal** | ![Style][ltype-style] | ![f16][badge-f16] | 0.07 GB | [![][cv-Danrisi]](https://civitai.com/models/1862761/nicegirls-ultrareal?modelVersionId=3352079) | Portrait realism on a girls dataset: v2 is a 10,000-step retrain of the slavic set the author prefers, and the page also carries an asian-girls v1 and the older slavic v1. No trigger word; strength **0.6–0.8**. The card says it stacks freely with other adapters. |
| **RAW style photo** | ![Style][ltype-style] | ![bf16][badge-bf16] | 0.07 GB | [![][cv-latent--space--dreams]](https://civitai.com/models/1751076/raw-style-photo?modelVersionId=3391625) | Neutral-colour, neutral-light conversion toward a RAW-photograph look. Trigger `Change to RAW photo`; if the output goes noisy, switch to `euler_a`. Also usable for text-to-image at **0.3**. v3 was trained on an expanded dataset; the page carries Flux builds of the same idea for other bases. |
| **Y2K digicam** | ![Style][ltype-style] | ![fp32][badge-fp32] | 0.07 GB | [![][gh-empero--ai]](https://huggingface.co/empero-ai/Homebrew-Qwen-Image-2.1-Y2K/resolve/main/pytorch_lora_weights.safetensors) | Early-2000s digicam look: direct-flash highlights, muted sensor cast, soft detail. Trigger `y2kphoto`. Trained on only **160 Wikimedia digicam photographs** (CC BY-SA 3.0 / public domain, credited in the card), and this is the **step 500 of 1000** snapshot, so it is deliberately under-trained. F32-stored, hence the size. Non-commercial only. |
| **Realism (Nano Banana)** | ![Style][ltype-style] | ![bf16][badge-bf16] | 0.004 GB | [![][gh-houseofboern]](https://huggingface.co/houseofboern/realism-nano-banana-qwen-image-2.1-lokr/resolve/main/realism-nb-qwen-image-2.1-lokr-step1000.safetensors) | Makes a generated image read as a real phone photo — skin texture, single-source lighting, sensor noise. **LoKR, not LoRA**: needs a LyCORIS loader, and it is the only entry in this table that does. Checkpoints at 500 / 750 / 1000. **Use strength 0.5–0.7, not 1.0** — the card is explicit that 1.0 is heavy. |
|  |  |  |  |  |  |
| **Normal2RGB** | ![Utility][ltype-utility] | ![bf16][badge-bf16] | 0.25 GB | [![][gh-Aero--Ex]](https://huggingface.co/Aero-Ex/Qwen-Image2.1_Normal2RGB/resolve/main/Normal2RGB_4000.safetensors) | Normal map → RGB render, 3 checkpoints. |
| **White model** | ![Utility][ltype-utility] | ![bf16][badge-bf16] | 0.16 GB | [![][gh-RunningHubAI]](https://huggingface.co/RunningHubAI/rh-qwen-image-2.1-lora-2103639501527670786/resolve/main/QI2.1Convert-to-white-model.safetensors) | Strips people down to grey CG mannequins while preserving posture, gesture and camera angle — useful as a clean reference for sculpting or rigging. Handles two people at once. **The trigger is a fixed 60-word prompt**, not a keyword; the metadata records it verbatim as the only caption seen in training, so paraphrasing it will weaken the effect. Rank 16, 2,000 steps. |
| **Image Translator** | ![Utility][ltype-utility] | ![f16][badge-f16] | 0.16 GB | [![][gh-ysharma]](https://huggingface.co/ysharma/Qwen-Image-2.1-image-translator-LoRA/resolve/main/imtrans_full_2000_gate_up_split.safetensors) ┊ [![][gh-ysharma]](https://huggingface.co/ysharma/Qwen-Image-2.1-image-translator-LoRA/resolve/main/imtrans_full_000001500_gate_up_split.safetensors) | Rewrites text inside an image in the target language, matching font, colour, size and position, and leaves every non-text pixel alone. Seven languages: English, Chinese, Japanese, Korean, Spanish, French, German. **No right-to-left scripts** (Arabic, Hebrew) — the card cites the literature on why. **Take the `_gate_up_split` file for diffusers** (linked first): the ComfyUI-keyed checkpoint loads but silently drops all 64 fused `img_mlp.gate_up` keys, so the adapter half-loads without warning. Two modes — let the model translate, or supply exact source→target strings to typeset. Rank 32, 2,000 steps, 6,000 training pairs. Numbers, prices, URLs and brand names are never translated. |
| **Restore** | ![Utility][ltype-utility] | ![bf16][badge-bf16] | 0.16 GB | [![][gh-ausboss]](https://huggingface.co/ausboss/Qwen-Image-2.1-Restore-LoRA/resolve/main/qwen-image-2.1-restore.safetensors) ┊ [![][gh-ausboss]](https://huggingface.co/ausboss/Qwen-Image-2.1-Restore-LoRA/resolve/main/qwen-image-2.1-restore-1250.safetensors) | Softens the base model's own over-eager upscaling, which invents pores, freckles and wrinkles that were never in the picture. Measured on 37 self-shrunk images: about **0.3 px off** the original with it, over 2 px without. Start at strength 1.0, but **drop to 0.5 for out-of-focus or video-frame inputs** — at 1.0 it faithfully reproduces the blur. Enlarge to roughly 2 MP first, sides divisible by 32. It is a redraw, not a recovery: fine detail is invented to fit, and plain Qwen draws more texture. The author runs it on Viggle Turbo at 8 steps; 25 steps works too and lands closer. Rank 16. The repo keeps two steps of one run — **step 1500** (linked first) and **step 1250**, which carries a little more skin texture. |
| **High resolution** | ![Utility][ltype-utility] | ![bf16][badge-bf16] | 0.07 GB | [![][cv-NO8D]](https://civitai.com/models/2436859/high-resolution?modelVersionId=3396843) | High-definition restoration from the MoreReal author, recommended alongside Qwen-Image-2.1-Turbo. The card calls this the hardest of the HighQuality series to train — ten-plus dataset and parameter iterations — and marks it experimental. **Download requires a Civitai login.** |
| **Realism edit v2** | ![Utility][ltype-utility] | ![bf16][badge-bf16] | 0.04 GB | [![][gh-houseofboern]](https://huggingface.co/houseofboern/realism-qwen-image-2.1-edit-v2/resolve/main/realism-qwen-image-2.1-edit-v2.safetensors) | The `Realism edit` row in the Control group above, retrained: same idea and same exact caption `convert this into a real phone photo`, but v2 asks for **0.5–0.75** where v1 wanted 1.0, because v1 at full strength gave prickly skin and shifted windows. 25 steps, CFG 1, about 1 MP. Rank 8 from 30 pairs. A distinct file from v1 — take v2 first. |
|  |  |  |  |  |  |
| **Hips / buttocks** | ![NSFW][ltype-nsfw] | ![bf16][badge-bf16] | 0.47 GB | ⚠️ [![][gh-RunningHubAI]](https://huggingface.co/RunningHubAI/rh-qwen-image-2.1-lora/resolve/main/qwen2509%E8%87%80%E9%83%A8%E6%94%BE%E5%A4%A7.safetensors) | Body-shape slider, ported from a Qwen-2.5-09 derivative. CN filename. |
| **Asian mix** | ![NSFW][ltype-nsfw] | ![bf16][badge-bf16] | 0.32 GB | ⚠️ [![][gh-RunningHubAI]](https://huggingface.co/RunningHubAI/rh-qwen21-hina-qwenimage2.1-asianmix-lora-v3.0-rank64-lora/resolve/main/Qwen21-%E4%BA%9A%E6%B4%B2hina_QwenImage2.1_asianMix_Lora_v3.0-rank64.safetensors) | v3.0 of a portrait LoRA on the `hina` character, at **rank 64** — unusually wide for a character adapter, and the metadata records a delta-space reduced-QR merge with a full core SVD, so it is not a plain rank-64 crop. Trigger `women` / `asian women`, which makes it easy to fire by accident on unrelated prompts. Partly F32-stored, hence the size at rank 64. |
| **FUSAL Anime** | ![NSFW][ltype-nsfw] | ![bf16][badge-bf16] | 0.29 GB | ⚠️ [![][gh-MicksHF]](https://huggingface.co/MicksHF/Qwen-Image-2.1-Anime-Fusal/resolve/main/loras/fusal-qwen-image-2.1-style-hires-exact-r56.safetensors) | Wide-domain anime style plus character interaction from ~50k hand-picked records, with dedicated NSFW training — **adults and research use only**, and the repo is flagged `not-for-all-audiences`. Trigger `fusal style.` at strength 1.0, 30–40 steps, CFG 1, on the official **Base** model (the card reports Turbo loses the effect). Rank 56 = the style epoch and hi-res epoch concatenated, BF16, alpha-less (the loader derives alpha = rank). The bundled Qwen3-VL-8B **Heretic** BF16 encoder (17.53 GB) is the one the training embeddings were cached with — keep the official processor, tokenizer and VAE beside it. The repo also keeps an r80 stack of all four adapters (0.42 GB) and its rank-48 SVD cut (0.25 GB); ComfyUI wants Load LoRA (Model Only) and `CLIPLoader` type `qwen_image`. |
| **Futanari anatomy** | ![NSFW][ltype-nsfw] | ![bf16][badge-bf16] | 0.24 GB | ⚠️ [![][gh-glowleaf]](https://huggingface.co/glowleaf/qwen-image-2.1-futanari-lora/resolve/main/futa_qwen21_v1_000001000.safetensors) | Teaches one specific anatomy, **without testicles**, solo or as a two-woman scene. **Strength 0.5–0.65** — 1.0 flattens skin. Take `ckpt1250` for close-ups, `ckpt1000` (the default in most of the samples) elsewhere, `ckpt750` only if the render still shows testicles. Rank 16, 3 checkpoints. Examples use the Q8 GGUF. |
| **Breasts and hips** | ![NSFW][ltype-nsfw] | ![bf16][badge-bf16] | 0.17 GB | ⚠️ [![][gh-RunningHubAI]](https://huggingface.co/RunningHubAI/rh-qwen-image-2.1-lora/resolve/main/Qwen%20Image%202.1%E5%A4%A7%E8%83%B8%E5%A4%A7%E8%87%80.safetensors) | Combined body-shape adapter from the same pack. CN filename. |
| **RadianceChrome Voluptuous** | ![NSFW][ltype-nsfw] | ![bf16][badge-bf16] | 0.17 GB | ⚠️ [![][gh-AIImageStudio]](https://huggingface.co/AIImageStudio/RadianceChromeVoluptuous_QwenImage2.1_v1.0) | Character-style LoRA. |
| **NSFW LoRA** | ![NSFW][ltype-nsfw] | ![bf16][badge-bf16] | 0.16 GB | ⚠️ [![][gh-Wickedlizerd]](https://huggingface.co/Wickedlizerd/NSFW-Qwen-Image-2.1-LoRA/resolve/main/nsfw_qwen_21.safetensors) | Civitai original by TheseAlpacas, mirrored unmodified. Rank 32, 192 targets. The author asks for **25+ steps**, `er_sde` and the `beta` scheduler on an INT8 ConvRot base — it is not a few-step adapter. |
| **NSFW Image Edit** | ![NSFW][ltype-nsfw] | ![bf16][badge-bf16] | 0.08 GB | ⚠️ [![][gh-RunningHubAI]](https://huggingface.co/RunningHubAI/rh-qwen-image-2.1-aio-nsfw-lora/resolve/main/Qwen-Image-2.1%20NSFW%20Image%20Edit.safetensors) | Editing LoRA, uploaded 2026-09-24. |
| **Glamour Realism** | ![NSFW][ltype-nsfw] | ![f16][badge-f16] | 0.07 GB | ⚠️ [![][cv-TP--AI--63]](https://civitai.com/models/2986100/qwen-image-21-glamour-realism-lora-16-gb-tested?modelVersionId=3385496) | Gentle polish for glamour portraits of adult subjects: natural-looking skin and photographic colour instead of plastic, and at 0.5–0.7 it keeps the outfit, pose and framing you prompt. Rank 16, no trigger word, recommended strength **0.6**; the author tested to fit a 16 GB GPU. **Download requires a Civitai login.** |
| **Uncensored LoRA** | ![NSFW][ltype-nsfw] | ![bf16][badge-bf16] | 0.03 GB | ⚠️ [![][gh-abenzerps]](https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-Quantized/resolve/main/qwen-image-2.1-uncensored-lora.safetensors) | The adapter form of the uncensored weights, from the most-downloaded repo here. Undocumented on the card — the full weights are already in that repo's GGUF ladder, so reach for this only if you want the uncensored behaviour *without* replacing the DiT. |
| **Breasts Slider V1** | ![NSFW][ltype-nsfw] | ![bf16][badge-bf16] | 0.003 GB | ⚠️ [![][gh-RunningHubAI]](https://huggingface.co/RunningHubAI/rh-qwen-image-2.1-breasts-slider-lora/resolve/main/Pornmaster_QI2.1_Breasts_Slider_V1.safetensors) | Slider control, 3 MB. |

> [!CAUTION]
> Repos marked ⚠️ are uncensored, abliterated, or NSFW. They are listed for completeness because they are widely used — the uncensored GGUF in particular is the most-downloaded repo in this ecosystem. They carry the same **Qwen Research License** as the base model; a research license is not a license to do whatever you want, and you remain responsible for how you use them. Sizes are the LoRA file only; none of these merge a base model.

<p id="port" align="center">◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆◇◆</p>

## ⬡ Platform ports

Non-CUDA runtimes and specialized accelerator backends.

<p id="port-apple" align="center">· · · · · · · · · · · · · ·</p>

### ▣ Apple Silicon

| Name | Format | Precision | Size | Links | Notes |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **MLX 8bit** | MLX (mflux) | ![int8][badge-int8] | 24.04 GB | [![][gh-JoyFusionAI]](https://huggingface.co/JoyFusionAI/Qwen-Image-2.1-MLX-8bit) | For [mflux](https://github.com/filipstrand/mflux). 13 TE shards. |
| **Coreml** | CoreML `.mlpackage` | ![bf16][badge-bf16] | 14.74 GB | [![][gh-devin--lai]](https://huggingface.co/devin-lai/Qwen-Image-2.1-Coreml) | 4 transformer blocks (~3.5 GB each) + embed + VAE decoder. |
| **QIPACK base** | QIPACK1 `.qipack` | ![fp16][badge-fp16] | 14.23 GB | [![][gh-netdur]](https://huggingface.co/netdur/Qwen-Image-2.1-QIPACK) | For the native C++/Metal [qwen-image-cplus](https://github.com/netdur/qwen-image-cplus) runtime. 40-step base, defaults to TaylorSeer caching. |
| **QIPACK distilled** | QIPACK1 `.qipack` | ![fp16][badge-fp16] | 14.23 GB | [![][gh-netdur]](https://huggingface.co/netdur/Qwen-Image-2.1-QIPACK) | Same runtime, 4-step. The Viggle v0.1 **full fine-tune**, not its LoRA and not v0.2.1. |
| **MLX 4bit** | MLX | ![int4][badge-int4] | 11.59 GB | [![][gh-themindstudio]](https://huggingface.co/themindstudio/Qwen-Image-2.1-MLX-4bit) | Smallest viable Apple build. |
| **Uncensored MLX** | MLX (4/6/8-bit) | ![int4][badge-int4] ![int8][badge-int8] | 7.56 GB | ⚠️ [![][gh-abenzerps]](https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-Quantized) | The uncensored line's Apple build, from the GGUF repo — 7.56 GB at 8-bit, 5.78 at 6-bit, 4.00 at 4-bit. The repo also carries a BF16 text encoder (17.53 GB), an int8 ConvRot one (9.35 GB) and the VAE (0.68 GB), but those are plain diffusers-layout safetensors rather than MLX builds, so an MLX pipeline still pairs with one of the two repos above. |

The repo is self-contained: alongside the two packs it now ships the Qwen3-VL-8B text encoder (4 shards, 17.53 GB), the VAE (1.35 GB) and the processor files, so the support download is no longer needed. Needs macOS 14+. 1024×1024 works; 2048×2048 does not yet.

<p id="port-mnn" align="center">· · · · · · · · · · · · · ·</p>

### ▣ Mobile &amp; edge (MNN)

Alibaba MNN runtime for on-device inference. The full repos are large — the MNN build bundles the text encoder, DiT, and VAE together.

| Name | Precision | Size | Links | Notes |
| :--- | :---: | :---: | :---: | :--- |
| **MNN fp16** | ![fp16][badge-fp16] | 30.72 GB | [![][gh-yunfengwang]](https://huggingface.co/yunfengwang/Qwen-Image-2.1-MNN-fp16) | Highest fidelity, and by far the largest. |
| **MNN int8** | ![int8][badge-int8] | 21.42 GB | [![][gh-yunfengwang]](https://huggingface.co/yunfengwang/Qwen-Image-2.1-MNN-int8) | |
| **MNN int4** | ![int4][badge-int4] | 14.39 GB | [![][gh-yunfengwang]](https://huggingface.co/yunfengwang/Qwen-Image-2.1-MNN-int4) | |
| **MNN** | ![int4][badge-int4] | 10.62 GB | [![][gh-evankuo]](https://huggingface.co/evankuo/Qwen-Image-2.1-MNN) | `llm.mnn.weight` 4.73 + `dit.mnn.weight` 4.47 + VAE 0.51 GB. |

<p id="port-alt" align="center">· · · · · · · · · · · · · ·</p>

### ▣ AMD &amp; domestic accelerators

**p150** is the standout entry here. A full port to a **single Tenstorrent Blackhole p150a** via `tt-nn`, with all three sub-models resident on-chip. ~20.5 s for a 40-step 1024² generation (513 ms/step sustained), and it beats an RTX 5090 with CPU offload by 1.4–1.6× end to end. Includes editing support for 1–4 condition images. No weights are redistributed — it pulls the official ones.

**[ROCm gfx1151](https://huggingface.co/kingjones777/Qwen-Image-2.1-ROCm-gfx1151)** targets AMD Strix Halo / RX 9070-class iGPUs. Code only; no weights in the repo.

**Intel Arc (SYCL).** **[Frosty40](https://huggingface.co/Frosty40/Qwen-Image-2.1-SYCL-Turbo-GGUF)** is a serving package for the `sd.cpp` SYCL backend, not a fine-tune — "turbo" refers to the recipe, not to step distillation. Despite the name the weights are Qwen's own, quantized from a BF16 master.

| Name | Precision | Size | Links | Notes |
| :--- | :---: | :---: | :---: | :--- |
| **SYCL quality** | ![q5_0][badge-Q5_0] | 7.89 GB | [![][gh-Frosty40]](https://huggingface.co/Frosty40/Qwen-Image-2.1-SYCL-Turbo-GGUF) | Attention qkv/o kept at F16; 73 BF16 + 128 F16 + 96 Q5_0. |
| **SYCL lean** | ![q5_0][badge-Q5_0] | 5.07 GB | [![][gh-Frosty40]](https://huggingface.co/Frosty40/Qwen-Image-2.1-SYCL-Turbo-GGUF) | All-exception Q5_0, 73 BF16 + 224 Q5_0. |

Both ship with a pinned Qwen3-VL-8B-Instruct Q8_0 text encoder (8.71 GB) and the BF16 VAE (0.68 GB). Two non-obvious requirements: `--vae-tiling` is mandatory at 1024² or the SYCL VAE overflows int32, and **one `sd-cli` per GPU** — a second concurrent run wedges the xe driver and needs a root-only reset. The 3.84× speedup comes from `--eager-load --cache-mode easycache`, not from fewer steps.

**FlagOS** ships eight builds for Chinese NPUs, same 28-file layout in each:

| Name | Target | Precision | Size | Links |
| :--- | :---: | :---: | :---: | :---: |
| **BF16 nvidia** | NV