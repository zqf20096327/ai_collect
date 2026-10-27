# 👁️‍🗨️ Awesome VLM Architectures [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
<!--lint disable double-link-->
![VLM](https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/5c9ee091-1f37-4d92-8398-a7d4e006c014)

**Awesome VLM Architectures** is a citation-first visual catalog of **200 Vision-Language Model (VLM/MLLM) architectures**, spanning contrastive encoders, multimodal LLMs, native multimodal models, unified understanding and generation, video, OCR, GUI agents, and embodied AI. Each entry links to primary sources and summarizes the model architecture, modality alignment or fusion, training stages, datasets, and distinctive design choices, with an architectural figure when available.

Use this repository to compare multimodal model families, trace architectural ideas over time, or retrieve grounded references for research and AI-agent workflows. The catalog includes a source-linked release timeline reviewed through October 27, 2026 and covers foundational systems such as CLIP and Flamingo alongside current multimodal reasoning and agentic models. **Expand any model panel for its detailed architecture summary.**

- 📙 <a href="https://github.com/gokayfem/ComfyUI_VLM_nodes">Visit my other repo to try Vision Language Models on ComfyUI</a>

Last reviewed: October 27, 2026 (Europe/Istanbul).

[October 2026 review](UPDATES-2026-10-27.md): additions since the August 1 review, earlier omissions, family updates, date evidence, and availability caveats. This is a curated architecture catalog, not an exhaustive index of every fine-tune or API version.

## Contents

- [Citation](#citation)
- [Models](#models)
- [Release Timeline](#release-timeline)
- [Architectures](#architectures)
- [Important References](#important-references)

## Citation

If this repository is useful in your work, you may cite it below. Please also cite the original paper for claims about any individual model; this catalog is a guide to the literature, not a substitute for it.

Created and maintained by [Gökay Aydoğan](https://www.researchgate.net/profile/Goekay-Aydogan-2) at [fal.ai](https://fal.ai) ([ORCID](https://orcid.org/0000-0002-2343-9433); [gokay@fal.ai](mailto:gokay@fal.ai)).

Architecture images are credited individually in the [figure credits](assets/architectures/CREDITS.md) and remain subject to the rights described in the [figure notice](assets/architectures/FIGURE_NOTICE.md).

<details>
<summary>📚 <i>BibTeX</i></summary>

```bibtex
@misc{aydogan2024awesomevlmarchitectures,
  author       = {Gökay Aydoğan},
  title        = {Awesome VLM Architectures},
  year         = {2024},
  howpublished = {\url{https://github.com/gokayfem/awesome-vlm-architectures}},
  note         = {GitHub repository, fal.ai},
  url          = {https://github.com/gokayfem/awesome-vlm-architectures}
}
```

</details>

## Models

All architecture panels are ordered by release date, newest first. Models released on the same day retain editorial catalog order.

<details>
<summary>🧭 <i>Chronological Model Index (200 architectures, newest first)</i></summary>

**2026:** [Nemotron 3.5 Parse](#nemotron-35-parse-compact-visual-prefix-decoding-for-structured-documents) | [Nemotron 3.5 Super VL](#nemotron-35-super-vl-hybrid-state-space-moe-for-long-context-visual-agents) | [Muse Spark Open](#muse-spark-open-sparse-multimodal-experts-with-a-shared-perception-encoder) | [Step 5 Preview](#step-5-preview-deep-sparse-experts-with-gated-sliding-window-and-sparse-gqa) | [Liquid d1](#liquid-d1-single-pass-multimodal-decisions-without-text-decoding) | [GroundAnything](#groundanything-autoregressive-and-block-diffusion-spatial-grounding) | [Holo4](#holo4-visual-computer-use-agents-trained-across-gui-and-tool-environments) | [MiMo-V2.6](#mimo-v26-hybrid-sliding-window-omni-encoders-and-multi-teacher-distillation) | [Qwen3.8-Omni-Flash](#qwen38-omni-flash-native-omni-agents-with-spatial-audio-and-sparse-long-context-reasoning) | [Taichu 5.0](#taichu-50-entropy-gated-recurrent-latent-visual-reasoning) | [DeepSeek-V4.1-Flash](#deepseek-v41-flash-causal-encoder-decoder-multimodality-with-shared-sparse-kv-memory) | [LLaDA-UI](#llada-ui-block-diffusion-reasoning-and-actions-for-gui-agents) | [Ling-3.0-flash-VL](#ling-30-flash-vl-kimi-delta-attention-and-gated-latent-attention-for-vision) | [Jina-OCR-v1](#jina-ocr-v1-compressed-visual-parsing-with-recursive-multi-token-drafting) | [NeoMME](#neomme-single-tower-bidirectional-multimodal-embeddings-from-masked-diffusion) | [Qwen-Drive-1.0](#qwen-drive-10-shared-visual-reasoning-with-external-3d-perception-and-planning) | [GLM-5.3-Flash](#glm-53-flash-native-multimodal-sparse-and-linear-attention-with-mhc) | [Qwen3.8-Flash-Next](#qwen38-flash-next-sparse-hybrid-attention-and-off-accelerator-n-gram-memory) | [dots3-note-preview](#dots3-note-preview-omnimodal-moe-with-a-sparse-vision-expert-encoder) | [North Micro Vision](#north-micro-vision-compact-native-resolution-vision-with-multilayer-feature-injection) | [Muse Glimmer](#muse-glimmer-dense-visual-agents-with-local-global-attention-and-diffusion-drafting) | [Shieldstral](#shieldstral-policy-conditioned-visual-moderation-in-one-forward-pass) | [MODUS](#modus-decoder-only-any-to-any-multimodal-modeling) | [Argus-Unified](#argus-unified-economical-understanding-and-generation) | [Kimi K3](#kimi-k3-kimi-delta-attention-at-trillion-parameter-scale) | [Mage-VL](#mage-vl-codec-native-streaming-multimodality) | [Apertus 1.5](#apertus-15-early-fusion-of-discrete-visual-and-audio-tokens) | [Audio-Visual Flamingo](#audio-visual-flamingo-temporally-aligned-audio-video-reasoning-over-long-clips) | [Inkling](#inkling-relative-position-multimodal-mixture-of-experts) | [Hy-Embodied-VLM](#hy-embodied-vlm-sparse-moe-reasoning-for-physical-agents) | [MonkeyOCRv2](#monkeyocrv2-document-native-visual-text-pretraining) | [DiffusionGemma](#diffusiongemma-cached-causal-context-with-a-block-diffusion-text-decoder) | [InternVideo3](#internvideo3-multimodal-contextual-reasoning-for-video-agents) | [Keye-VL 2.0](#keye-vl-20-sparse-attention-for-long-video-agents) | [Zamba2-VL](#zamba2-vl-hybrid-state-space-vision-language-modeling) | [MiniMax M3](#minimax-m3-native-multimodality-with-sparse-long-context-attention) | [Cosmos 3](#cosmos-3-omnimodal-world-modeling-with-mixture-of-transformers) | [Fara1.5](#fara15-verified-synthetic-environments-for-screenshot-based-computer-use) | [Lance](#lance-unified-image-and-video-understanding-generation-and-editing) | [ZAYA1-VL](#zaya1-vl-vision-specialized-compressed-convolutional-attention) | [LensVLM](#lensvlm-selective-expansion-of-visually-compressed-text-context) | [Falcon Perception](#falcon-perception-early-fusion-grounding-segmentation-and-ocr) | [Granite Vision 4.1](#granite-vision-41-window-q-formers-and-dual-deepstack-feature-injection) | [GLM-5V-Turbo](#glm-5v-turbo-native-multimodal-agency) | [Nemotron 3 Nano Omni](#nemotron-3-nano-omni-hybrid-moe-with-dynamic-visual-resolution-and-native-audio) | [SenseNova-U1 and U1.5](#sensenova-u1-and-u15-native-pixel-space-unified-understanding-and-generation) | [PLaMo 2.1-VL](#plamo-21-vl-lightweight-japanese-vision-language-modeling) | [Qwen3.5-Omni](#qwen35-omni-hybrid-attention-thinker-talker-and-adaptive-speech-alignment) | [EXAONE 4.5](#exaone-45-native-multimodal-pretraining-for-documents) | [BidirLM and BidirLM-Omni](#bidirlm-and-bidirlm-omni-causal-decoders-as-multimodal-encoders) | [Gemma 4](#gemma-4-open-weight-native-multimodal-models) | [Penguin-VL](#penguin-vl-efficient-vlms-with-llm-based-vision-encoders) | [Phi-4-Reasoning-Vision](#phi-4-reasoning-vision-compact-multimodal-reasoning) | [V-SONAR and V-LCM](#v-sonar-and-v-lcm-vision-language-modeling-in-concept-space) | [Qwen3.5](#qwen35-native-multimodal-hybrid-attention-models) | [Youtu-VL](#youtu-vl-unified-autoregressive-supervision-for-dense-vision) | [Kimi K2.5 and K2.6](#kimi-k25-and-k26-native-multimodal-agentic-moe) | [LightOnOCR-2 and LightOnOCR-3](#lightonocr-2-and-lightonocr-3-compact-end-to-end-ocr-with-document-grounding) | [Step3-VL-10B](#step3-vl-10b-language-aligned-perception-with-16-token-compression)

**2025:** [Molmo2](#molmo2-open-video-understanding-with-pointing-and-object-tracking) | [Mistral Large 3](#mistral-large-3-large-sparse-multimodal-experts-with-an-integrated-visual-encoder) | [Ministral 3](#ministral-3-dense-multimodal-backbones-with-compute-efficient-training) | [ERNIE 5.0](#ernie-50-unified-autoregressive-omnimodal-mixture-of-experts) | [Emu3.5](#emu35-native-multimodal-next-token-learning-with-diffusion-adaptation) | [Nemotron Nano V2 VL](#nemotron-nano-v2-vl-hybrid-state-space-visual-reasoning-with-efficient-video-sampling) | [DeepSeek-OCR](#deepseek-ocr-visual-context-compression-through-deepencoder) | [OmniVinci](#omnivinci-joint-audio-visual-alignment-with-grouped-temporal-embeddings) | [PaddleOCR-VL](#paddleocr-vl-ultra-compact-multilingual-document-parsing) | [Qwen3-Omni](#qwen3-omni-thinker-talker-moe-with-streaming-multicodebook-speech) | [Qwen3-VL](#qwen3-vl-deepstack-vision-language-models) | [Moondream 3](#moondream-3-compact-sparse-visual-experts-with-learned-attention-temperature) | [Intern-S1](#intern-s1-scientific-multimodality-with-dynamic-tokenization-and-expert-reasoning) | [LFM2-VL and LFM2.5-VL](#lfm2-vl-and-lfm25-vl-short-convolution-language-backbones-with-native-resolution-vision) | [Step3](#step3-model-system-co-design-for-cost-effective-multimodal-intelligence) | [GLM-4.1V-Thinking](#glm-41v-thinking-general-purpose-multimodal-reasoning-through-curriculum-sampled-rl) | [ERNIE 4.5-VL](#ernie-45-vl-heterogeneous-modality-mixture-of-experts) | [Show-o2](#show-o2-unified-text-prediction-and-continuous-visual-flow-matching) | [MiMo-VL](#mimo-vl-multimodal-pretraining-with-mixed-on-policy-reinforcement-learning) | [BAGEL](#bagel-a-mixture-of-transformer-experts-for-unified-understanding-and-generation) | [Seed1.5-VL](#seed15-vl-sparse-moe-multimodal-understanding-and-agentic-reasoning) | [PerceptionLM](#perceptionlm-open-data-and-training-for-detailed-image-video-understanding) | [Perception Encoder](#perception-encoder-contrastive-visual-pretraining-with-aligned-language-and-spatial-features) | [InternVL3 and InternVL3.5](#internvl3-and-internvl35-native-multimodal-pretraining-and-adaptive-resolution) | [Kimi-VL](#kimi-vl-native-resolution-vision-with-a-sparse-moe-decoder) | [Llama 4 Scout and Maverick](#llama-4-scout-and-maverick-native-multimodal-mixture-of-experts-models) | [Qwen2.5-Omni](#qwen25-omni-streaming-multimodal-perception-and-speech-generation) | [Gemma 3](#gemma-3-long-context-multimodality-with-efficient-interleaved-attention) | [Aya Vision](#aya-vision-multilingual-multimodality-through-cross-modal-model-merging) | [Phi-4-multimodal](#phi-4-multimodal-text-vision-and-speech-through-mixture-of-loras) | [SigLIP 2](#siglip-2-multilingual-vision-language-encoders-with-native-aspect-ratio-support) | [EVEv2](#evev2-improved-baselines-for-encoder-free-vision-language-models) | [Qwen2.5-VL](#qwen25-vl-enhanced-vision-language-capabilities-in-the-qwen-series) | [VideoLLaMA 3](#videollama-3-frontier-multimodal-foundation-models-for-image-and-video-understanding) | [UI-TARS](#ui-tars-pioneering-automated-gui-interaction-with-native-agents) | [MiniMax-01](#minimax-01-scaling-foundation-models-with-lightning-attention) | [MiniCPM-o-2.6](#minicpm-o-26-a-gpt-4o-level-mllm-for-vision-speech-and-multimodal-live-streaming) | [Eagle 2](#eagle-2-building-post-training-data-strategies-from-scratch-for-frontier-vision-language-models) | [Sa2VA](#sa2va-marrying-sam2-with-llava-for-dense-grounded-understanding-of-images-and-videos)

**2024:** [VideoChat-Flash](#videochat-flash-hierarchical-compression-for-long-context-video-modeling) | [OmniVLM](#omnivlm-a-token-compressed-sub-billion-parameter-vision-language-model-for-efficient-on-device-inference) | [Apollo](#apollo-an-exploration-of-video-understanding-in-large-multimodal-models) | [DeepSeek-VL2](#deepseek-vl2-mixture-of-experts-vision-language-models-for-advanced-multimodal-understanding) | [Maya](#maya-an-instruction-finetuned-multilingual-multimodal-model) | [InternVL 2.5](#internvl-25-expanding-performance-boundaries-of-open-source-multimodal-models-with-model-data-and-test-time-scaling) | [PaliGemma 2](#paligemma-2-a-family-of-versatile-vlms-for-transfer) | [ShowUI](#showui-vision-language-action-modeling-for-gui-agents) | [SmolVLM](#smolvlm-a-small-efficient-and-open-source-vision-language-model) | [AIMv2](#aimv2-multimodal-autoregressive-pre-training-of-large-vision-encoders) | [LLaVA-CoT](#llava-cot-let-vision-language-models-reason-step-by-step) | [LLM2CLIP](#llm2clip-powerful-language-model-unlocks-richer-visual-representation) | [Tarsier2](#tarsier2-advancing-large-vision-language-models-from-detailed-video-description-to-comprehensive-video-understanding) | [Janus and Janus-Pro](#janus-and-janus-pro-decoupled-visual-understanding-and-generation) | [ARIA](#aria-an-open-multimodal-native-mixture-of-experts-model) | [Emu3](#emu3-next-token-prediction-across-text-image-and-video) | [Molmo and PixMo](#molmo-and-pixmo-open-weights-open-data-and-grounded-pointing) | [Llama 3.2-Vision](#llama-32-vision-enhanced-multimodal-capabilities-built-on-llama-3) | [NVLM](#nvlm-open-frontier-class-multimodal-llms) | [Pixtral 12B](#pixtral-12b-a-cutting-edge-open-multimodal-language-model) | [VILA-U](#vila-u-fully-autoregressive-visual-understanding-and-generation) | [Qwen2-VL](#qwen2-vl-a-powerful-open-source-vision-language-model-for-image-and-video-understanding) | [EAGLE](#eagle-exploring-the-design-space-for-multimodal-llms-with-mixture-of-encoders) | [Show-o](#show-o-autoregressive-language-and-discrete-diffusion-vision-in-one-transformer) | [Idefics3-8B](#idefics3-8b-building-and-better-understanding-vision-language-models) | [Transfusion](#transfusion-next-token-text-prediction-and-continuous-image-diffusion) | [mPLUG-Owl3](#mplug-owl3-hyper-attention-for-long-image-sequences) | [VITA](#vita-towards-open-source-interactive-omni-multimodal-llm) | [LLaVA-OneVision](#llava-onevision-easy-visual-task-transfer) | [VILA²](#vila²-vila-augmented-vila) | [INF-LLaVA](#inf-llava-high-resolution-image-perception-for-multimodal-large-language-models) | [SlowFast-LLaVA](#slowfast-llava-a-strong-training-free-baseline-for-video-large-language-models) | [EVLM](#evlm-an-efficient-vision-language-model-for-visual-understanding) | [InternLM-XComposer-2.5](#internlm-xcomposer-25-a-versatile-large-vision-language-model-supporting-long-contextual-input-and-output) | [OMG-LLaVA](#omg-llava-bridging-image-level-object-level-pixel-level-reasoning-and-understanding) | [Cambrian-1](#cambrian-1-vision-centric-multimodal-llms) | [EVE](#eve-unveiling-encoder-free-vision-language-models) | [Ovis](#ovis-structural-visual-text-embedding-alignment) | [Parrot](#parrot-multilingual-visual-instruction-tuning) | [ConvLLaVA](#convllava-hierarchical-backbones-as-visual-encoder-for-large-multimodal-models) | [Phi-3-Vision and Phi-3.5-Vision](#phi-3-vision-and-phi-35-vision-compact-long-context-multimodal-reasoning) | [CogVLM2](#cogvlm2-enhanced-vision-language-models-for-image-and-video-understanding) | [Chameleon](#chameleon-mixed-modal-early-fusion-foundation-models) | [PaliGemma](#paligemma-a-versatile-and-transferable-3b-vision-language-model) | [xGen-MM (BLIP-3)](#xgen-mm-blip-3-an-open-source-framework-for-building-powerful-and-responsible-large-multimodal-models) | [MANTIS](#mantis-mastering-multi-image-understanding-through-interleaved-instruction-tuning) | [Moondream-next](#moondream-next-compact-vision-language-model-with-enhanced-capabilities) | [Idefics2](#idefics2) | [InternLM-XComposer2-4KHD](#internlm-xcomposer2-4khd-a-pioneering-large-vision-language-model-handling-resolutions-from-336-pixels-to-4k-hd) | [MM1](#mm1-methods-analysis-and-insights-from-multimodal-pre-training) | [DeepSeek-VL](#deepseek-vl-towards-real-world-vision-language-understanding) | [AnyGPT](#anygpt-unified-any-to-any-multimodal-modeling-with-discrete-tokens) | [SPHINX-X](#sphinx-x-scaling-data-and-parameters-for-a-family-of-multi-modal-large-language-models) | [LLaVA 1.6](#llava-16-llava-next-improved-reasoning-ocr-and-world-knowledge) | [MiniCPM-V](#minicpm-v-a-gpt-4v-level-mllm-on-your-phone) | [MouSi](#mousi-poly-visual-expert-vision-language-models) | [InternLM-XComposer2](#internlm-xcomposer2-mastering-free-form-text-image-composition-and-comprehension-in-vision-language-large-model) | [MoE-LLaVA](#moe-llava-mixture-of-experts-for-large-vision-language-models) | [moondream1 and moondream2](#moondream1-and-moondream2) | [FireLLaVA](#firellava) | [COSMO](#cosmo-contrastive-streamlined-multimodal-model-with-interleaved-pre-training)

**2023:** [TinyGPT-V](#tinygpt-v-efficient-multimodal-large-language-model-via-small-backbones) | [MobileVLM](#mobilevlm-a-fast-strong-and-open-vision-language-assistant-for-mobile-devices) | [Alpha-CLIP](#alpha-clip-a-clip-model-focusing-on-wherever-you-want) | [Nous-Hermes-2-Vision - Mistral 7B](#nous-hermes-2-vision---mistral-7b) | [SPHINX](#sphinx-the-joint-mixing-of-weights-tasks-and-visual-embeddings-for-multi-modal-large-language-models) | [Florence-2](#florence-2-a-deep-dive-into-its-unified-architecture-and-multi-task-capabilities) | [u-LLaVA](#u-llava-unifying-multi-modal-tasks-via-large-language-model) | [LLaVA-Plus](#llava-plus-learning-to-use-tools-for-creating-multimodal-agents) | [OtterHD](#otterhd-a-high-resolution-multi-modality-model) | [CoVLM](#covlm-composing-visual-entities-and-relationships-in-large-language-models-via-communicative-decoding) | [GLaMM](#glamm-pixel-grounding-large-multimodal-model) | [Fuyu-8B](#fuyu-8b-a-multimodal-architecture-for-ai-agents) | [PaLI-3 Vision Language Models](#pali-3-vision-language-models-smaller-faster-stronger) | [MiniGPT-v2](#minigpt-v2-large-language-model-as-a-unified-interface-for-vision-language-multi-task-learning) | [BakLLaVA](#bakllava) | [Ferret](#ferret-refer-and-ground-anything-anywhere-at-any-granularity) | [LLaVA 1.5](#llava-15-improved-baselines-with-visual-instruction-tuning) | [CogVLM](#cogvlm-visual-expert-for-pretrained-language-models) | [MetaCLIP](#metaclip-demystifying-clip-data) | [Qwen-VL](#qwen-vl-a-versatile-vision-language-model-for-understanding-localization-text-reading-and-beyond) | [IDEFICS](#idefics) | [BLIVA](#bliva-a-simple-multimodal-llm-for-better-handling-of-text-rich-visual-questions) | [KOSMOS-2](#kosmos-2-grounding-multimodal-large-language-models-to-the-world) | [LaVIN](#lavin-cheap-and-quick-efficient-vision-language-instruction-tuning-for-large-language-models) | [InstructBLIP](#instructblip-towards-general-purpose-vision-language-models-with-instruction-tuning) | [ImageBind](#imagebind-one-embedding-space-to-bind-them-all) | [LLaVA](#llava-large-language-and-vision-assistant---visual-instruction-tuning) | [MiniGPT-4](#minigpt-4-enhancing-vision-language-understanding-with-advanced-large-language-models) | [SigLIP](#siglip-sigmoid-loss-for-language-image-pre-training) | [OpenFlamingo](#openflamingo-an-open-source-framework-for-training-large-autoregressive-vision-language-models) | [PaLM-E](#palm-e-an-embodied-multimodal-language-model) | [KOSMOS-1](#kosmos-1-language-is-not-all-you-need-aligning-perception-with-language-models) | [BLIP-2](#blip-2-bootstrapping-language-image-pre-training-with-frozen-image-encoders-and-large-language-models)

**2022:** [MULTIINSTRUCT](#multiinstruct-improving-multi-modal-zero-shot-learning-via-instruction-tuning) | [PaLI](#pali-a-jointly-scaled-multilingual-language-image-model) | [Flamingo](#flamingo-a-visual-language-model-for-few-shot-learning) | [BLIP](#blip-bootstrapping-language-image-pre-training)

**2021:** [GLIP](#glip-grounded-language-image-pre-training) | [FROZEN](#frozen-multimodal-few-shot-learning-with-frozen-language-models) | [CLIP](#clip-contrastive-language-image-pre-training)

**2020:** [ViT](#vit-an-image-is-worth-16x16-words-transformers-for-image-recognition-at-scale)

</details>

## Release Timeline

Dates use the first documented official model release; when none is available, they use the paper's arXiv v1 submission or first technical report. Family point releases are folded into their first architecture release, and same-day entries retain catalog order.

<!--lint disable table-pipe-alignment table-cell-padding-->

<details>
<summary>🗓️ <i>Release Timeline (200 architectures, newest first)</i></summary>

| Date | Architecture | Distinctive contribution |
| --- | --- | --- |
| 2026-10-17 | Nemotron 3.5 Parse | Compact visual-prefix decoding for structured documents |
| 2026-10-15 | Nemotron 3.5 Super VL | Hybrid state-space MoE for long-context visual agents |
| 2026-10-15 | Muse Spark Open | Sparse multimodal experts with a shared perception encoder |
| 2026-10-15 | Step 5 Preview | Deep sparse experts with gated sliding-window and sparse GQA |
| 2026-10-07 | Liquid d1 | Single-pass multimodal decisions without text decoding |
| 2026-09-30 | GroundAnything | Autoregressive and block-diffusion spatial grounding |
| 2026-09-28 | Holo4 | Visual computer-use agents trained across GUI and tool environments |
| 2026-09-22 | MiMo-V2.6 | Hybrid sliding-window omni encoders and multi-teacher distillation |
| 2026-09-18 | Qwen3.8-Omni-Flash | Native omni agents with spatial audio and sparse long-context reasoning |
| 2026-09-15 | Taichu 5.0 | Entropy-gated recurrent latent visual reasoning |
| 2026-09-10 | DeepSeek-V4.1-Flash | Causal encoder-decoder multimodality with shared sparse KV memory |
| 2026-09-09 | LLaDA-UI | Block-diffusion reasoning and actions for GUI agents |
| 2026-09-04 | Ling-3.0-flash-VL | Kimi Delta Attention and gated latent attention for vision |
| 2026-09-02 | Jina-OCR-v1 | Compressed visual parsing with recursive multi-token drafting |
| 2026-08-31 | NeoMME | Single-tower bidirectional multimodal embeddings from masked diffusion |
| 2026-08-31 | Qwen-Drive-1.0 | Shared visual reasoning with external 3D perception and planning |
| 2026-08-26 | GLM-5.3-Flash | Native multimodal sparse and linear attention with mHC |
| 2026-08-26 | Qwen3.8-Flash-Next | Sparse hybrid attention and off-accelerator n-gram memory |
| 2026-08-14 | dots3-note-preview | Omnimodal MoE with a sparse vision expert encoder |
| 2026-08-12 | North Micro Vision | Compact native-resolution vision with multilayer feature injection |
| 2026-08-10 | Muse Glimmer | Dense visual agents with local-global attention and diffusion drafting |
| 2026-08-04 | Shieldstral | Policy-conditioned visual moderation in one forward pass |
| 2026-07-28 | MODUS | Shared decoder context with autoregressive and flow-matching modality experts |
| 2026-07-28 | Argus-Unified | Hybrid continuous and discrete visual tokens for economical understanding and generation |
| 2026-07-27 | Kimi K3 | Kimi Delta Attention, Attention Residuals, and extremely sparse LatentMoE routing |
| 2026-07-27 | Mage-VL | Codec-native selective video tokenization with a proactive event gate |
| 2026-07-24 | Apertus 1.5 | Early fusion of discrete visual and audio tokens |
| 2026-07-17 | Audio-Visual Flamingo | Temporally aligned audio-video reasoning over long clips |
| 2026-07-15 | Inkling | Relative-position million-context multimodal MoE trained from scratch |
| 2026-07-15 | Hy-Embodied-VLM | Action-centric sparse-MoE reasoning for physical-world agents |
| 2026-07-11 | MonkeyOCRv2 | Joint image-to-text and pixel-reconstruction pretraining for document vision |
| 2026-06-10 | DiffusionGemma | Cached causal context with a block-diffusion text decoder |
| 2026-06-10 | InternVideo3 | Token-preserving latent KV compression and closed-loop video reasoning |
| 2026-06-09 | Keye-VL 2.0 | DeepSeek Sparse Attention adapted to GQA-based long-video multimodality |
| 2026-06-02 | Zamba2-VL | Hybrid Mamba-2 and shared-attention blocks for efficient VLM inference |
| 2026-06-01 | MiniMax M3 | Native multimodality with block-sparse grouped-query attention at million-token context |
| 2026-05-31 | Cosmos 3 | Coupled autoregressive reasoner and diffusion generator for physical AI |
| 2026-05-21 | Fara1.5 | Verified synthetic environments for screenshot-based computer use |
| 2026-05-18 | Lance | Shared-sequence understanding, generation, and editing with modality experts |
| 2026-05-08 | ZAYA1-VL | Vision-conditional LoRA and compressed convolutional attention in an open-data MoE |
| 2026-05-07 | LensVLM | Selective expansion of visually compressed text context |
| 2026-05-03 | Falcon Perception | Early fusion with hybrid attention and continuous mask heads |
| 2026-04-29 | Granite Vision 4.1 | Window Q-Formers and dual DeepStack feature injection |
| 2026-04-29 | GLM-5V-Turbo | Perception integrated into reasoning, planning, tools, and execution |
| 2026-04-28 | Nemotron 3 Nano Omni | Hybrid MoE with dynamic visual resolution and native audio |
| 2026-04-27 | SenseNova-U1 and U1.5 | Native pixel-space unified understanding and generation |
| 2026-04-21 | PLaMo 2.1-VL | Compact Japanese VQA and grounding for edge deployment |
| 2026-04-17 | Qwen3.5-Omni | Hybrid-attention Thinker-Talker and adaptive speech alignment |
| 2026-04-09 | EXAONE 4.5 | Native multimodal pretraining with document-focused data and 256K context |
| 2026-04-02 | BidirLM and BidirLM-Omni | Converting causal decoders into bidirectional multimodal encoders |
| 2026-03-31 | Gemma 4 | Dense and MoE native multimodality, including an encoder-free 12B design |
| 2026-03-06 | Penguin-VL | Text-LLM-initialized vision encoder and priority-aware token compression |
| 2026-03-04 | Phi-4-Reasoning-Vision | Mid-fusion compact VLM with explicit reasoning and direct-answer modes |
| 2026-03-01 | V-SONAR and V-LCM | Vision-language alignment and prediction in multilingual concept space |
| 2026-02-16 | Qwen3.5 | Native early fusion with hybrid linear/full attention and sparse MoE variants |
| 2026-01-27 | Youtu-VL | Unified autoregressive visual tokens that emit dense vision outputs without task heads |
| 2026-01-27 | Kimi K2.5 and K2.6 | Trillion-parameter native multimodal MoE for agents and computer use |
| 2026-01-20 | LightOnOCR-2 and LightOnOCR-3 | Compact end-to-end OCR with document grounding |
| 2026-01-14 | Step3-VL-10B | Language-aligned perception encoder with 16-fold visual-token compression |
| 2025-12-11 | Molmo2 | Open video understanding with pointing and object tracking |
| 2025-12-02 | Mistral Large 3 | Large sparse multimodal experts with an integrated visual encoder |
| 2025-12-02 | Ministral 3 | Dense multimodal backbones with compute-efficient training |
| 2025-11-13 | ERNIE 5.0 | One autoregressive sparse MoE for text, images, video, audio, and generation |
| 2025-10-30 | Emu3.5 | Native multimodal next-token learning with diffusion adaptation |
| 2025-10-28 | Nemotron Nano V2 VL | Hybrid state-space visual reasoning with efficient video sampling |
| 2025-10-20 | DeepSeek-OCR | DeepEncoder compresses high-resolution documents into very short visual contexts |
| 2025-10-17 | OmniVinci | Joint audio-visual alignment with grouped temporal embeddings |
| 2025-10-16 | PaddleOCR-VL | NaViT-style dynamic resolution with a compact ERNIE decoder for document parsing |
| 2025-09-22 | Qwen3-Omni | Thinker-Talker MoE with streaming multicodebook speech |
| 2025-09-22 | Qwen3-VL | DeepStack multi-level ViT fusion and explicit video timestamp alignment |
| 2025-09-18 | Moondream 3 | Compact sparse visual experts with learned attention temperature |
| 2025-08-21 | Intern-S1 | Scientific multimodality with dynamic tokenization and expert reasoning |
| 2025-08-12 | LFM2-VL and LFM2.5-VL | Short-convolution language backbones with native-resolution vision |
| 2025-07-25 | Step3 | Model-system co-design for communication-efficient sparse-MoE multimodality |
| 2025-07-01 | GLM-4.1V-Thinking | Curriculum-sampled reinforcement learning for multimodal reasoning |
| 2025-06-30 | ERNIE 4.5-VL | Heterogeneous shared and modality-specific experts with isolated routing |
| 2025-06-19 | Show-o2 | Unified text prediction and continuous visual flow matching |
| 2025-06-04 | MiMo-VL | Four-stage multimodal pretraining followed by mixed on-policy RL |
| 2025-05-20 | BAGEL | Mixture-of-Transformer-Experts for understanding and generation |
| 2025-05-11 | Seed1.5-VL | Compact vision encoder with a 20B-active MoE for reasoning and agents |
| 2025-04-17 | PerceptionLM | Open data and training for detailed image-video understanding |
| 2025-04-17 | Perception Encoder | Contrastive visual pretraining with aligned language and spatial features |
| 2025-04-11 | InternVL3 and InternVL3.5 | Native multimodal pretraining, later extended with adaptive resolution and cascade RL |
| 2025-04-10 | Kimi-VL | MoonViT native-resolution packing with a sparse MoE decoder |
| 2025-04-05 | Llama 4 Scout and Maverick | Early-fusion native multimodality in sparse-MoE Scout and Maverick models |
| 2025-03-26 | Qwen2.5-Omni | Streaming Thinker-Talker architecture for multimodal input and speech output |
| 2025-03-12 | Gemma 3 | Efficient local/global attention with long-context image understanding |
| 2025-03-04 | Aya Vision | Cross-modal model merging for multilingual multimodality without language forgetting |
| 2025-03-03 | Phi-4-multimodal | Mixture-of-LoRAs for text, vision, and speech |
| 2025-02-20 | SigLIP 2 | Multilingual, localization-aware, native-aspect-ratio vision-language encoding |
| 2025-02-08 | EVEv2 | Improved Baselines for Encoder-Free Vision-Language Models |
| 2025-01-26 | Qwen2.5-VL | Enhanced Vision-Language Capabilities in the Qwen Series |
| 2025-01-21 | VideoLLaMA 3 | Frontier Multimodal Foundation Models for Image and Video Understanding |
| 2025-01-20 | UI-TARS | Pioneering Automated GUI Interaction with Native Agents |
| 2025-01-14 | MiniMax-01 | Scaling Foundation Models with Lightning Attention |
| 2025-01-12 | MiniCPM-o-2.6 | A GPT-4o Level MLLM for Vision, Speech and Multimodal Live Streaming |
| 2025-01-10 | Eagle 2 | Building Post-Training Data Strategies from Scratch for Frontier Vision-Language Models |
| 2025-01-07 | Sa2VA | Marrying SAM2 with LLaVA for Dense Grounded Understanding of Images and Videos |
| 2024-12-31 | VideoChat-Flash | Hierarchical Compression for Long-Context Video Modeling |
| 2024-12-16 | OmniVLM | A Token-Compressed, Sub-Billion-Parameter Vision-Language Model for Efficient On-Device Inference |
| 2024-12-13 | Apollo | An Exploration of Video Understanding in Large Multimodal Models |
| 2024-12-13 | DeepSeek-VL2 | Mixture-of-Experts Vision-Language Models for Advanced Multimodal Understanding |
| 2024-12-10 | Maya | An Instruction Finetuned Multilingual Multimodal Model |
| 2024-12-05 | InternVL 2.5 | Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling |
| 2024-12-04 | PaliGemma 2 | A Family of Versatile VLMs for Transfer |
| 2024-11-26 | ShowUI | UI-guided visual-token selection and interleaved action histories |
| 2024-11-26 | SmolVLM | A Small, Efficient, and Open-Source Vision-Language Model |
| 2024-11-21 | AIMv2 | Multimodal Autoregressive Pre-training of Large Vision Encoders |
| 2024-11-15 | LLaVA-CoT | Let Vision Language Models Reason Step-by-Step |
| 2024-11-06 | LLM2CLIP | Powerful Language Model Unlocks Richer Visual Representation |
| 2024-11-05 | Tarsier2 | Advancing Large Vision-Language Models from Detailed Video Description to Comprehensive Video Understanding |
| 2024-10-17 | Janus and Janus-Pro | Decoupled visual encoders for understanding and generation with one transformer |
| 2024-10-08 | ARIA | An Open Multimodal Native Mixture-of-Experts Model |
| 2024-09-27 | Emu3 | One next-token objective over discrete text, image, and video tokens |
| 2024-09-25 | Molmo and PixMo | Open data pipeline with human captions and grounded pointing supervision |
| 2024-09-25 | Llama 3.2-Vision | Enhanced Multimodal Capabilities Built on Llama 3 |
| 2024-09-17 | NVLM | Open Frontier-Class Multimodal LLMs |
| 2024-09-11 | Pixtral 12B | A Cutting-Edge Open Multimodal Language Model |
| 2024-09-06 | VILA-U | Shared discrete visual tokens for autoregressive understanding and generation |
| 2024-08-29 | Qwen2-VL | A Powerful Open-Source Vision-Language Model for Image and Video Understanding |
| 2024-08-28 | EAGLE | Exploring The Design Space for Multimodal LLMs with Mixture of Encoders |
| 2024-08-22 | Show-o | Autoregressive language and discrete-diffusion image generation in one transformer |
| 2024-08-22 | Idefics3-8B | Building and Better Understanding Vision-Language Models |
| 2024-08-20 | Transfusion | Autoregressive text and continuous image diffusion in one transformer |
| 2024-08-09 | mPLUG-Owl3 | Hyper-attention for long image sequences and video |
| 2024-08-09 | VITA | Towards Open-Source Interactive Omni Multimodal LLM |
| 2024-08-05 | LLaVA-OneVision | Easy Visual Task Transfer |
| 2024-07-24 | VILA² | VILA Augmented VILA |
| 2024-07-23 | INF-LLaVA | High-Resolution Image Perception for Multimodal Large Language Models |
| 2024-07-22 | SlowFast-LLaVA | A Strong Training-Free Baseline for Video Large Language Models |
| 2024-07-19 | EVLM | An Efficient Vision-Language Model for Visual Understanding |
| 2024-07-03 | InternLM-XComposer-2.5 | A Versatile Large Vision Language Model Supporting Long-Contextual Input and Output |
| 2024-06-27 | OMG-LLaVA | Bridging Image-level, Object-level, Pixel-level Reasoning and Understanding |
| 2024-06-24 | Cambrian-1 | Spatial Vision Aggregator and systematic multi-encoder study |
| 2024-06-17 | EVE | Unveiling Encoder-Free Vision-Language Models |
| 2024-06-14 | Ovis | Learnable visual vocabulary for structural visual-text embedding alignment |
| 2024-06-04 | Parrot | Multilingual Visual Instruction Tuning |
| 2024-05-24 | ConvLLaVA | Hierarchical Backbones as Visual Encoder for Large Multimodal Models |
| 2024-05-21 | Phi-3-Vision and Phi-3.5-Vision | Compact dynamic-resolution VLM with 128K context |
| 2024-05-20 | CogVLM2 | Enhanced Vision-Language Models for Image and Video Understanding |
| 2024-05-16 | Chameleon | Mixed-modal early fusion over a shared token sequence |
| 2024-05-14 | PaliGemma | A Versatile and Transferable 3B Vision-Language Model |
| 2024-05-06 | xGen-MM (BLIP-3) | An Open-Source Framework for Building Powerful and Responsible Large Multimodal Models |
| 2024-05-02 | MANTIS | Mastering Multi-Image Understanding Through Interleaved Instruction Tuning |
| 2024-04-19 | Moondream-next | Compact Vision-Language Model with Enhanced Capabilities |
| 2024-04-15 | Idefics2 | Open 8B VLM with native-resolution inputs and strong OCR and document understanding |
| 2024-04-09 | InternLM-XComposer2-4KHD | A Pioneering Large Vision-Language Model Handling Resolutions from 336 Pixels to 4K HD |
| 2024-03-14 | MM1 | Controlled study of encoders, connectors, token counts, and data mixtures |
| 2024-03-08 | DeepSeek-VL | Towards Real-World Vision-Language Understanding |
| 2024-02-19 | AnyGPT | Any-to-any autoregression over discrete text, image, speech, and music tokens |
| 2024-02-08 | SPHINX-X | Scaling Data and Parameters for a Family of Multi-modal Large Language Models |
| 2024-01-30 | LLaVA 1.6 | LLaVA-NeXT Improved reasoning, OCR, and world knowledge |
| 2024-01-30 | MiniCPM-V | A GPT-4V Level MLLM on Your Phone |
| 2024-01-30 | MouSi | Poly-Visual-Expert Vision-Language Models |
| 2024-01-29 | InternLM-XComposer2 | Mastering Free-form Text-Image Composition and Comprehension in Vision-Language Large Model |
| 2024-01-29 | MoE-LLaVA | Mixture of Experts for Large Vision-Language Models |
| 2024-01-20 | moondream1 and moondream2 | Compact SigLIP–Phi VLMs optimized for efficient edge inference |
| 2024-01-05 | FireLLaVA | LLaVA derivative trained rapidly on a curated multimodal instruction mixture |
| 2024-01-01 | COSMO | COntrastive Streamlined MultimOdal Model with Interleaved Pre-Training |
| 2023-12-28 | TinyGPT-V | Efficient Multimodal Large Language Model via Small Backbones |
| 2023-12-28 | MobileVLM | A Fast, Strong and Open Vision Language Assistant for Mobile Devices |
| 2023-12-06 | Alpha-CLIP | A CLIP Model Focusing on Wherever You Want |
| 2023-11-28 | Nous-Hermes-2-Vision - Mistral 7B | SigLIP-equipped Mistral VLM with OCR and function-calling data |
| 2023-11-13 | SPHINX | The Joint Mixing of Weights, Tasks, and Visual Embeddings for Multi-modal Large Language Models |
| 2023-11-10 | Florence-2 | A Deep Dive into its Unified Architecture and Multi-Task Capabilities |
| 2023-11-09 | u-LLaVA | Unifying Multi-Modal Tasks via Large Language Model |
| 2023-11-09 | LLaVA-Plus | Learning to Use Tools for Creating Multimodal Agents |
| 2023-11-07 | OtterHD | A High-Resolution Multi-modality Model |
| 2023-11-06 | CoVLM | Composing Visual Entities and Relationships in Large Language Models Via Communicative Decoding |
| 2023-11-06 | GLaMM | Pixel Grounding Large Multimodal Model |
| 2023-10-17 | Fuyu-8B | A Multimodal Architecture for AI Agents |
| 2023-10-13 | PaLI-3 Vision Language Models | Smaller, Faster, Stronger |
| 2023-10-13 | MiniGPT-v2 | large language model as a unified interface for vision-language multi-task learning |
| 2023-10-12 | BakLLaVA | Mistral-based LLaVA variant with a CLIP vision encoder and projection adapter |
| 2023-10-11 | Ferret | Refer and Ground Anything Anywhere at Any Granularity |
| 2023-10-05 | LLaVA 1.5 | Improved Baselines with Visual Instruction Tuning |
| 2023-10-05 | CogVLM | Visual Expert for Pretrained Language Models |
| 2023-09-28 | MetaCLIP | Demystifying CLIP Data |
| 2023-08-24 | Qwen-VL | A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond |
| 2023-08-22 | IDEFICS | Open Flamingo-style model for interleaved image-text generation |
| 2023-08-19 | BLIVA | A Simple Multimodal LLM for Better Handling of Text-rich Visual Questions |
| 2023-06-26 | KOSMOS-2 | Grounding Multimodal Large Language Models to the World |
| 2023-05-24 | LaVIN | Cheap and Quick: Efficient Vision-Language Instruction Tuning for Large Language Models |
| 2023-05-11 | InstructBLIP | Towards General-purpose Vision-Language Models with Instruction Tuning |
| 2023-05-09 | ImageBind | One Embedding Space To Bind Them All |
| 2023-04-17 | LLaVA | Large Language and Vision Assistant - Visual Instruction Tuning |
| 2023-04-16 | MiniGPT-4 | Enhancing Vision-Language Understanding with Advanced Large Language Models |
| 2023-03-27 | SigLIP | Sigmoid Loss for Language Image Pre-Training |
| 2023-03-14 | OpenFlamingo | An Open-Source Framework for Training Large Autoregressive Vision-Language Models |
| 2023-03-06 | PaLM-E | An Embodied Multimodal Language Model |
| 2023-02-27 | KOSMOS-1 | Language Is Not All You Need: Aligning Perception with Language Models |
| 2023-01-30 | BLIP-2 | Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models |
| 2022-12-21 | MULTIINSTRUCT | Improving Multi-Modal Zero-Shot Learning via Instruction Tuning |
| 2022-09-14 | PaLI | A Jointly-Scaled Multilingual Language-Image Model |
| 2022-04-28 | Flamingo | a Visual Language Model for Few-Shot Learning |
| 2022-01-28 | BLIP | Bootstrapping Language-Image Pre-training |
| 2021-12-07 | GLIP | Grounded Language-Image Pre-training |
| 2021-06-25 | FROZEN | Multimodal Few-Shot Learning with Frozen Language Models |
| 2021-01-05 | CLIP | Contrastive Language-Image Pre-training |
| 2020-10-22 | ViT | An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale |

</details>

<!--lint enable table-pipe-alignment table-cell-padding-->

## Architectures

### **Nemotron 3.5 Parse: Compact visual-prefix decoding for structured documents**

A compact C-RADIO and mBART system generates document text, element classes, and bounding boxes with a causal visual prefix.

[![Model](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/nvidia/Nemotron-3.5-Parse)

NVIDIA<br>
**Released:** 2026-10-17

<!-- architecture-figure:158 -->
> **Architecture figure:** The October 17 model card describes C-RADIO, convolutional compression, and mBART in text; no model-specific architecture diagram or paper was found in the cited release.
<!-- /architecture-figure:158 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

C-RADIOv4-SO400M processes rectangular NaViT inputs. Convolutional adapters compress its features before a ten-layer mBART causal decoder with grouped-query attention. The approximately 0.631B parameters include a one-step prediction head. Task tokens select text, layout classes, and box extraction.

Supervision pairs document images with OCR text and layout annotations. The released decoder supports ordinary generation; the accompanying serving plugin can use the bundled prediction head for speculative decoding. The card does not disclose a complete stage-by-stage training recipe.

Training combines rendered documents, scientific PDFs, tables, and synthetic word/character pages with automated and human labels. Outputs can be converted into Markdown, HTML, or structured records. Weights use OpenMDW 1.1; tokenizer and benchmark components have separately documented terms.

</details>

### **Nemotron 3.5 Super VL: Hybrid state-space MoE for long-context visual agents**

A Mamba-Transformer mixture-of-experts backbone combines a C-RADIO visual encoder with long-context image and video reasoning.

[![Paper](https://img.shields.io/badge/Report-Primary_source-b31b1b.svg?style=flat-square)](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Super-and-Lightning-Technical-Report.pdf) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/NVIDIA-NeMo/Nemotron) [![Model](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-BF16) [![Source](https://img.shields.io/badge/Official-Source-blue?style=flat-square)](https://research.nvidia.com/labs/nemotron/Nemotron-3.5-Super-and-Lightning/)

NVIDIA<br>
**Released:** 2026-10-15

<!-- architecture-figure:157 -->
<p align="center">
  <img src="assets/architectures/157-nemotron-3-5-super-vl.png" alt="Nemotron 3.5 Super VL architecture or training overview from its primary paper" width="820">
</p>
<p align="center"><sub><b>Figure 4.</b> Visual-language post-training pipeline: teachers, text-trunk reinforcement learning, and multi-teacher on-policy distillation. <a href="https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Super-and-Lightning-Technical-Report.pdf">Source paper</a>, PDF p. 13. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:157 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

The 120B/A12B model combines Mamba-2, attention, and LatentMoE blocks. A C-RADIO encoder, projection layers, and temporal video embedding connect visual inputs to the language backbone. Multi-token prediction supports speculative decoding; the advertised context is 1M tokens.

Training starts from Nemotron 3 Super, proceeds through continued pretraining and multimodal supervised tuning, then combines verifiable-reward and preference optimization with multi-teacher on-policy distillation. A final stage improves the prediction head.

Inputs are text, images, and video; output is text. The recipe discloses data mixtures and stages, but some supervised/RL datasets remain pending release. Weights use OpenMDW 1.1. Encoder-version labels differ across official artifacts, so the family name C-RADIO is used here.

</details>

### **Muse Spark Open: Sparse multimodal experts with a shared perception encoder**

A large sparse multimodal transformer integrates perceptual inputs with agentic language reasoning over a million-token context.

[![Model](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B) [![Source](https://img.shields.io/badge/Official-Source-blue?style=flat-square)](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B/blob/main/README.md)

Meta Superintelligence Labs<br>
**Released:** 2026-10-15

<!-- architecture-figure:188 -->
> **Architecture figure:** The Muse Spark Open model card provides architecture specifications but no model-specific diagram. The cited evaluation report is not an architecture paper.
<!-- /architecture-figure:188 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

The 816B/42B-active model has 62 decoder layers, gated grouped-query attention, and 256 experts with eight selected per token. A 1.8B perception encoder combines learned absolute and 2D rotary positions with sparse/full attention. Supported inputs are text, images, video, and audio; output is text.

The downloadable version includes additional safety post-training relative to the hosted system. The card details the architecture and evaluations but does not publish a complete reproducible pretraining or alignment recipe.

Data sources include public web material, third-party collections, Meta services, and synthetic multimodal examples, with filtering and deduplication. BF16 and NVFP4 checkpoints are offered through gated access under the Muse Model License. October 15 is explicitly recorded as the release date.

</details>

### **Step 5 Preview: Deep sparse experts with gated sliding-window and sparse GQA**

A narrow, deep multimodal MoE interleaves gated local attention with sparse grouped-query attention for long agent trajectories.

[![Model](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/stepfun-ai/Step-5-Preview) [![Source](https://img.shields.io/badge/Official-Source-blue?style=flat-square)](https://platform.stepfun.com/blog/inside-step-5-preview)

StepFun<br>
**Released:** 2026-10-15

*Timeline basis: Dated primary architecture/training article; earlier API release day remains unresolved.*

<!-- architecture-figure:189 -->
<p align="center">
  <img src="assets/architectures/189-step-5-preview.png" alt="Sparse GQA indexing and selected-token attention in Step 5 Preview." width="820">
</p>
<p align="center"><sub><b>Official architecture diagram.</b> Sparse GQA indexing and selected-token attention in Step 5 Preview. <a href="https://platform.stepfun.com/blog/inside-step-5-preview">Primary source</a>. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:189 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

The 600B/27B-active model uses 92 transformer blocks and a 3:1 ratio of gated sliding-window to sparse full-attention layers. Sparse GQA adds blockwise token merging to reduce indexer cost. The public checkpoint supports text and image input with text output and up to 1M context.

The technical article describes precision and gradient-handling changes for deep-model stability. An agent-native synthesis system constructs tasks under expert-defined controls, followed by agentic reinforcement learning.

The release targets coding and knowledge-work trajectories. Full training data are not published. The card’s introduction also advertises video, while its input table lists text/image; this discrepancy is left explicit. October 15 is the dated architecture disclosure used here, not a claim about the earliest hosted API availability.

</details>

### **Liquid d1: Single-pass multimodal decisions without text decoding**

A decision head returns typed, calibrated answers in one forward pass instead of generating an autoregressive response.

[![Model](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/LiquidAI/d1-3B) [![Source](https://img.shields.io/badge/Official-Source-blue?style=flat-square)](https://huggingface.co/blog/LiquidAI/open-d1)

Liquid AI<br>
**Released:** 2026-10-07

<!-- architecture-figure:175 -->
<p align="center">
  <img src="assets/architectures/175-liquid-d1.png" alt="Liquid d1-3B decision model architecture" width="820">
</p>
<p align="center"><sub><b>Official architecture diagram.</b> d1-3B visual decision model: a generative backbone adapted to single-pass decisions. <a href="https://www.liquid.ai/blog/d1-open">Primary source</a>. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<p align="center">
  <img src="assets/architectures/liquid-d1-omni-supplement.png" alt="Liquid d1-omni-600M encoder and decision heads" width="820">
</p>
<p align="center"><sub><b>Official architecture diagram.</b> d1-omni-600M decision model with visual and audio encoders; accepts text with either image or audio input. <a href="https://www.liquid.ai/blog/d1-open">Primary source</a>. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>

<!-- /architecture-figure:175 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

d1-3B adapts LFM2.5-VL-3B to score yes/no questions, named options, and ratings. The experimental d1-omni-600M instead combines a bidirectional LFM encoder with SigLIP2 vision and FastConformer audio pathways. Its supported combinations are text-plus-image or text-plus-audio, not simultaneous image-plus-audio.

Decision-focused post-training teaches calibrated typed outputs from a shared state and multiple questions. The interface reads scores directly from decision positions, eliminating output-token decoding.

The release provides inference examples and evaluations across text, visual, and audio decisions. A complete training-data inventory is not published in the cards. Both checkpoints use the custom LFM license. These are discriminative decision models, distinct from the chat-generating LFM2.5-VL base.

</details>

### **GroundAnything: Autoregressive and block-diffusion spatial grounding**

A shared visual-language backbone supports separate autoregressive and parallel diffusion checkpoints for spatial predictions.

[![Paper](https://img.shields.io/badge/arXiv-2609.39600-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2609.39600) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/groundingpi/GroundAnything) [![Model](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/GroundingPI/GroundAnything-VLM)

Qize Yu et al., GroundingPI and collaborators<br>
**Released:** 2026-09-30

*Timeline basis: First paper publication; code and weights followed in October.*

<!-- architecture-figure:185 -->
<p align="center">
  <img src="assets/architectures/185-groundanything.png" alt="GroundAnything architecture or training overview from its primary paper" width="820">
</p>
<p align="center"><sub><b>Figure 2.</b> A shared visual-language backbone supports separate autoregressive and parallel diffusion checkpoints for spatial predictions. <a href="https://arxiv.org/abs/2609.39600">Source paper</a>, PDF p. 6. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:185 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

MoonViT-V2/Kimi-K3 perception feeds Qwen3-4B through 2×2 spatial aggregation and a two-layer MLP. A vocabulary of 1,000 coordinate tokens represents spatial outputs. The diffusion variant adds a mask token and bidirectional response-block denoising; GroundAnything-VLM is the autoregressive checkpoint.

The training recipe develops grounded perception before converting the decoder to diffusion. Entropy-guided decoding refines spatial hypotheses in parallel. An optional self-speculative mode offers a separate speed/accuracy operating point.

Tasks span object localization, referring expressions, pointing, OCR, document layout, and GUI grounding. The paper appeared September 30, code October 3, and ModelScope weights October 14. Original contributions use Apache 2.0, while upstream Kimi-derived material retains its license conditions.

</details>

### **Holo4: Visual computer-use agents trained across GUI and tool environments**

A family of visual agents combines screenshot-based interaction with code, API, and MCP tools through task-factory training.

[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/hcompai/hai-agents-python) [![Model](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/Hcompany/Holo4-35B-A3B) [![Source](https://img.shields.io/badge/Official-Source-blue?style=flat-square)](https://hcompany.ai/newsroom/holo4)

H Company<br>
**Released:** 2026-09-28

<!-- architecture-figure:164 -->
<p align="center">
  <img src="assets/architectures/164-holo4.png" alt="Holo4 task-factory training pipeline." width="820">
</p>
<p align="center"><sub><b>Official architecture diagram.</b> Holo4 task-factory training pipeline. <a href="https://hcompany.ai/newsroom/holo4">Primary source</a>. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:164 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

Holo4-27B builds on dense Qwen3.8, while Holo4-35B-A3B uses Qwen3.6 MoE. Both retain their base visual-language pathways and learn action policies spanning browser, desktop, and mobile environments. The contribution is the agent training system rather than a new shared vision tower.

A task factory creates environments and trajectories for supervised learning. Separate LoRA reinforcement-learning experts train on desktop/web tasks and terminal/MCP/API tasks, then merge with equal weighting. This connects GUI actions with structured tools within one agent.

The release documents task construction and provides evaluation trajectories; those traces are not the complete training corpus. Availability differs by checkpoint: 35B-A3B uses Apache 2.0, whereas 27B carries research/noncommercial terms. The family release date does not imply identical licenses.

</details>

### **MiMo-V2.6: Hybrid sliding-window omni encoders and multi-teacher distillation**

Visual and audio encoders feed a hybrid sliding-window MoE, with specialist reinforcement learning consolidated through multi-teacher on-policy distillation.

[![Paper](https://img.shields.io/badge/Report-Primary_source-b31b1b.svg?style=flat-square)](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL/blob/main/MiMo_V2_6_technical_report.pdf) [![Model](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-MOPD) [![Source](https://img.shields.io/badge/Official-Source-blue?style=flat-square)](https://mimo.xiaomi.com/mimo-v2-6)

Xiaomi MiMo<br>
**Released:** 2026-09-22

<!-- architecture-figure:163 -->
<p align="center">
  <img src="assets/architectures/163-mimo-v2-6.png" alt="MiMo-V2.6 architecture or training overview from its primary paper" width="820">
</p>
<p align="center"><sub><b>Figure 2.</b> Visual and audio encoders feed a hybrid sliding-window MoE, with specialist reinforcement learning consolidated through multi-teacher on-policy distillation. <a href="https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL/blob/main/MiMo_V2_6_technical_report.pdf">Source paper</a>, PDF p. 5. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:163 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

Flash has 309B total/15B active parameters and Pro 1.02T/42B. A 681M vision transformer uses local/global attention and spatial patch merging; audio tokenization and a patch encoder provide another input path. The language backbone alternates sliding-window and global attention and includes multi-token prediction.

Multimodal midtraining precedes large-scale agentic reinforcement learning. MOPD2 combines specialist teachers with rollout, teacher-prefix, and supervised-prefix training to consolidate capabilities and reduce failures such as repeated tool calls.

The report details coding and general-agent task construction, verifiers, and multimodal mixtures. Text, image, audio, and video inputs produce text with up to 1M context. RL and distilled checkpoints are separate releases under MIT; they should not be conflated in comparisons.

</details>

### **Qwen3.8-Omni-Flash: Native omni agents with spatial audio and sparse long-context reasoning**

A sparse hybrid Thinker combines vision, general audio, and spatial audio encoders for long-context multimodal agent work.

[![Paper](https://img.shields.io/badge/arXiv-2609.25611-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2609.25611) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/QwenLM/Qwen-MM-Plugins) [![Source](https://img.shields.io/badge/Official-Source-blue?style=flat-square)](https://qwen.ai/blog?id=qwen3.8-omni-flash)

Qwen Team<br>
**Released:** 2026-09-18

<!-- architecture-figure:187 -->
<p align="center">
  <img src="assets/architectures/187-qwen3-8-omni-flash.png" alt="Qwen3.8-Omni-Flash architecture or training overview from its primary paper" width="820">
</p>
<p align="center"><sub><b>Figure 2.</b> AuT audio encoder and its local attention layout; this is a component diagram, not the full multimodal system. <a href="https://arxiv.org/abs/2609.25611">Source paper</a>, PDF p. 4. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:187 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

The backbone inherits Qwen3.8-Next’s Gated DeltaNet and Qwen Sparse Attention. Alongside the vision encoder, AuT encodes general audio while Spatial AuT processes multichannel spatial cues. Explicit timestamps preserve cross-modal correspondence; post-training extends native 256K context to 1M.

Early mixed-modality co-training is followed by long-context reasoning and interactive agent training, then multi-teacher distillation. The report includes realtime text/speech interaction and selective retrieval of audio-video segments.

Training spans pure text and paired/interleaved audio, image, and video data. Qwen-MM-Plugins and Qwen-Live-Harness are released tooling; they are not downloadable model weights. The report documents hosted-model architecture and agent integration.

</details>

### **Taichu 5.0: Entropy-gated recurrent latent visual reasoning**

A compact visual reasoner adds adaptive recurrent latent computation to a Qwen-based model with C-RADIO perception.

[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/Taichu-AI/ZDTaichu5.0-9B) [![Model](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/TaichuAI/ZDTaichu5.0-9B) [![Source](https://img.shields.io/badge/Official-Source-blue?style=flat-square)](https://taichu-ai.github.io/ZDTaichu5.0-9B/)

Taichu AI<br>
**Released:** 2026-09-15

*Timeline basis: Explicit Initial release commit.*

<!-- architecture-figure:172 -->
> **Architecture figure:** The Taichu 5.0 project page and model card describe adaptive latent recurrence but provide examples and benchmarks rather than a published architecture diagram.
<!-- /architecture-figure:172 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

ZDTaichu5.0-9B combines Qwen3.5-9B with C-RADIOv4-H and adaptive image resolution. Entropy-gated adaptive recurrence allocates additional latent reasoning computation when needed. The supported context is 128K.

The release targets general visual understanding alongside spatial, multi-view, and embodied reasoning. Public architecture descriptions explain adaptive recurrence, but do not disclose a complete training corpus or sufficiently detailed stage schedule for independent reproduction.

Inputs include text and visual observations; outputs are textual answers and reasoning. Official code and a model checkpoint are linked. The timeline follows the explicitly titled Initial release commit on September 15, not the earlier model-repository creation timestamp.

</details>

### **DeepSeek-V4.1-Flash: Causal encoder-decoder multimodality with shared sparse KV memory**

A causal encoder-decoder MoE shares global KV memory across decoder layers, combining native vision with compressed sparse attention.

[![Paper](https://img.shields.io/badge/Report-Primary_source-b31b1b.svg?style=flat-square)](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/DeepSeek_V41_Tech_Report.pdf) [![Model](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) [![Source](https://img.shields.io/badge/Official-Source-blue?style=flat-square)](https://deepseek.com/en/news/deepseek-v4-1-flash/)

DeepSeek-AI<br>
**Released:** 2026-09-10

<!-- architecture-figure:156 -->
<p align="center">
  <img src="assets/architectures/156-deepseek-v4-1-flash.png" alt="DeepSeek-V4.1-Flash architecture or training overview from its primary paper" width="820">
</p>
<p align="center"><sub><b>Figure 3.</b> A causal encoder-decoder MoE shares global KV memory across decoder layers, combining native vision with compressed sparse attention. <a href="https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/blob/main/DeepSeek_V41_Tech_Report.pdf">Source paper</a>, PDF p. 7. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:156 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

The 40-layer backbone splits into 20 causal encoder and 20 decoder layers. Decoder layers reuse memory derived from the final encoder states. CSA2 combines full, reindex, and reuse modes with hierarchical sparse selection. DeepSeekViT uses 2D rotary positions, 3×3 patch unshuffle, and an MLP connector. The 552B backbone has a separate 196B Engram store; active computation differs between prefill and decoding.

Early multimodal pretraining spans 45T tokens, followed by instruction tuning, reinforcement learning, and on-policy distillation. Context training extends to 1M tokens; sparse attention and low-precision caching control memory costs.

Text and image inputs produce text. The report describes corpus categories and training stages rather than releasing the complete training corpus. Weights use the MIT license.

**Flash-1017** is a subsequent checkpoint update in the same architecture. Its official card describes reasoning, visual, and agentic improvements and links the same technical report; it is not counted as another architecture. [Updated checkpoint](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017)

</details>

### **LLaDA-UI: Block-diffusion reasoning and actions for GUI agents**

A native-resolution visual encoder feeds a block-diffusion MoE that jointly predicts GUI reasoning and action tokens.

[![Paper](https://img.shields.io/badge/arXiv-2609.13287-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2609.13287) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/inclusionAI/LLaDA-UI) [![Model](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/inclusionAI/LLaDA-UI)

inclusionAI<br>
**Released:** 2026-09-09

*Timeline basis: First arXiv submission.*

<!-- architecture-figure:162 -->
<p align="center">
  <img src="assets/architectures/162-llada-ui.png" alt="LLaDA-UI architecture or training overview from its primary paper" width="820">
</p>
<p align="center"><sub><b>Figure 2.</b> A native-resolution visual encoder feeds a block-diffusion MoE that jointly predicts GUI reasoning and action tokens. <a href="https://arxiv.org/abs/2609.13287">Source paper</a>, PDF p. 3. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:162 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

The approximately 16.7B system adapts LLaDA2.0-mini to screenshots with a vision encoder and multimodal connector. Bidirectional denoising operates within response blocks while earlier context remains available. Outputs combine reasoning with executable actions and normalized coordinates.

Training first aligns vision and language, then applies GUI instruction tuning across web, desktop, and mobile environments. The task-generation pipeline decomposes and composes capabilities, executes candidate trajectories, and verifies outcomes.

The report describes multimodal alignment data and synthesized GUI trajectories. Public model and inference code are available. Reported parallel-decoding gains depend on block size and decoding settings; this is a diffusion agent, not an autoregressive model with only a speculative head.

</details>

### **Ling-3.0-flash-VL: Kimi Delta Attention and gated latent attention for vision**

A visual MoE alternates Kimi Delta Attention with gated multi-head latent attention for efficient image and video reasoning.

[![Model](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/inclusionAI/Ling-3.0-flash-VL)

inclusionAI<br>
**Released:** 2026-09-04

*Timeline basis: First model/configuration upload.*

<!-- architecture-figure:171 -->
> **Architecture figure:** The official Ling-3.0-flash-VL card provides architecture specifications but no architecture diagram. Its training-content disclosure is not an architecture paper.
<!-- /architecture-figure:171 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

The card specifies 124B total and 5.5B active parameters across 42 layers, using a 5:1 KDA-to-gated-MLA ratio. A vision transformer and two-layer MLP connect visual tokens to the decoder; VideoRoPE carries spatial-temporal position information.

The released instruction model supports reasoning and tool workflows with up to 256K context. The model card supplies architecture and serving details, while a separate training-content disclosure summarizes data provenance. It does not provide a complete stage-by-stage reproducible recipe.

Text, images, and video produce text. Weights use MIT. The timeline records the first model/configuration upload on September 4, rather than interpreting a later README edit as a new architecture release.

</details>

### **Jina-OCR-v1: Compressed visual parsing with recursive multi-token drafting**

A DeepSeek-OCR-derived parser adds shared recursive speculative decoding and dense verifiable rewards for document structure.

[![Paper](https://img.shields.io/badge/arXiv-2609.03181-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2609.03181) [![Model](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/jinaai/jina-ocr-v1)

Alejandro Barón García et al., Jina AI<br>
**Released:** 2026-09-02

*Timeline basis: First arXiv submission.*

<!-- architecture-figure:173 -->
<p align="center">
  <img src="assets/architectures/173-jina-ocr-v1.png" alt="Jina-OCR-v1 architecture or training overview from its primary paper" width="820">
</p>
<p align="center"><sub><b>Figure 2.</b> A DeepSeek-OCR-derived parser adds shared recursive speculative decoding and dense verifiable rewards for document structure. <a href="https://arxiv.org/abs/2609.03181">Source paper</a>, PDF p. 4. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:173 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

DeepEncoder provides a global compressed view and local tiles to a 3B MoE decoder with roughly 570M active parameters. FastMTP reuses one draft block over three prediction steps. Greedy verification preserves the verifier’s greedy output rather than accepting approximate drafts.

Post-training combines instruction alignment, difficult-document fine-tuning, and GRPO. Formula, table, and structure checks award partial credit through dense deterministic rewards. Iterative error analysis guides subsequent data and checkpoint refinement.

Training mixes cleaned public document corpora with targeted synthetic pages. The model outputs structured document text and is distributed under CC BY-NC 4.0. Performance and speed depend on resolution and decoding settings; the paper reports the corresponding operating points.

</details>

### **NeoMME: Single-tower bidirectional multimodal embeddings from masked diffusion**

A single bidirectional transformer learns joint text-patch embeddings without a separate vision tower or causal language decoder.

[![Paper](https://img.shields.io/badge/arXiv-2609.01657-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2609.01657) [![Model](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/Hcompany/NeoMME-260M)

Aurélien Lac and Tony Wu, H Company<br>
**Released:** 2026-08-31

*Timeline basis: First arXiv submission, despite the September identifier.*

<!-- architecture-figure:166 -->
<p align="center">
  <img src="assets/architectures/166-neomme.png" alt="NeoMME architecture or training overview from its primary paper" width="820">
</p>
<p align="center"><sub><b>Figure 1.</b> A single bidirectional transformer learns joint text-patch embeddings without a separate vision tower or causal language decoder. <a href="https://arxiv.org/abs/2609.01657">Source paper</a>, PDF p. 1. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:166 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

NeoMME-260M and 800M ingest raw image patches and text tokens in one encoder. Dynamic-resolution processing and alternating local/global attention support long multimodal sequences. Retrieval can use either pooled dense vectors or token-level late interaction.

Pretraining reconstructs masked discrete text while conditioning on visible image patches; it does not add a pixel-reconstruction loss. Subsequent contrastive retrieval training supports both dense and late-interaction representations.

The report covers web, code, mathematics, documents, image captions, and synthetic OCR data. Compression experiments combine pooling and quantization; their ratios are configuration-specific. Apache-licensed weights target retrieval and representation learning rather than autoregressive chat.

</details>

### **Qwen-Drive-1.0: Shared visual reasoning with external 3D perception and planning**

A shared VLM supports visual questions, explicit 3D perception, and flow-matching trajectory planning through external heads.

[![Paper](https://img.shields.io/badge/arXiv-2609.00111-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2609.00111) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/QwenLM/Qwen-Drive-1.0) [![Model](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/Qwen/Qwen-Drive-1.0-4B)

Xin Zhou et al., Qwen Team<br>
**Released:** 2026-08-31

*Timeline basis: First arXiv submission.*

<!-- architecture-figure:191 -->
<p align="center">
  <img src="assets/architectures/191-qwen-drive-1-0.png" alt="Qwen-Drive-1.0 architecture or training overview from its primary paper" width="820">
</p>
<p align="center"><sub><b>Figure 2.</b> A shared VLM supports visual questions, explicit 3D perception, and flow-matching trajectory planning through external heads. <a href="https://arxiv.org/abs/2609.00111">Source paper</a>, PDF p. 3. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:191 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

The Qwen3.5-4B vision-language architecture remains unchanged. An external bird’s-eye-view head predicts objects, occupancy, and maps from shared representations. A separate Planning Expert uses flow matching to generate future ego trajectories; the VLM continues answering free-form visual questions.

A staged recipe initializes and trains perception, adapts the multimodal pathway, and develops planning. Joint driving/general-vision supervision reduces forgetting. Separate supervised and reward-optimized planners are released.

Training unifies labels and trajectories across driving datasets, with consistency filtering and general vision-language data. The RL planner uses NAVSIM PDMS, WOD-E2E RFS, and displacement rewards. Public code and Apache-licensed weights accompany the first paper dated August 31.

</details>

### **GLM-5.3-Flash: Native multimodal sparse and linear attention with mHC**

A newly pretrained multimodal MoE combines sparse and linear attention with manifold-constrained residual connections.

[![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/zai-org/GLM-5) [![Model](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/zai-org/GLM-5.3-Flash)

Z.ai<br>
**Released:** 2026-08-26

*Timeline basis: First substantive model-card and weight commits on August 26; repository initialized August 25.*

<!-- architecture-figure:159 -->
> **Architecture figure:** The cited GLM-5.3-Flash card publishes architecture text and benchmark plots, but no model-specific architecture figure. Its linked GLM-5 paper predates this architecture.
<!-- /architecture-figure:159 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

The official card specifies 320B total and 18B active parameters, hybrid sparse/linear attention, and manifold-constrained hyper-connections (mHC). This is a new multimodal base, rather than simply a post-training update of GLM-5.2.

The model uses a 30T-token multimodal pretraining corpus and targets coding, visual reasoning, and long-running tool workflows. The card does not disclose a complete visual-encoder specification or a reproducible post-training mixture.

The public checkpoint accepts visual and textual inputs and generates text under the MIT license. The linked February GLM-5 paper describes an earlier model: its architecture and figure should not be presented as a GLM-5.3-Flash-specific report.

</details>

### **Qwen3.8-Flash-Next: Sparse hybrid attention and off-accelerator n-gram memory**

Gated DeltaNet and micro-block sparse attention combine with n-gram memory and widened residual streams for efficient multimodal inference.

[![Paper](https://img.shields.io/badge/arXiv-2608.30320-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2608.30320) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/QwenLM/Qwen3.8-Flash-Next) [![Model](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) [![Source](https://img.shields.io/badge/Official-Source-blue?style=flat-square)](https://github.com/QwenLM/Qwen3.8-Flash-Next)

Qwen Team<br>
**Released:** 2026-08-26

<!-- architecture-figure:160 -->
<p align="center">
  <img src="assets/architectures/160-qwen3-8-flash-next.png" alt="Qwen3.8-Flash-Next architecture or training overview from its primary paper" width="820">
</p>
<p align="center"><sub><b>Figure 1.</b> Gated DeltaNet and micro-block sparse attention combine with n-gram memory and widened residual streams for efficient multimodal inference. <a href="https://arxiv.org/abs/2608.30320">Source paper</a>, PDF p. 2. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:160 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

The model has 125B backbone parameters with 6B active, plus separate 51B n-gram embedding tables and a prediction module. Three Gated DeltaNet layers alternate with one Qwen Sparse Attention layer. Gated residual read/write operations and a causal vision encoder complement sparse MoE routing.

The technical report studies attention, residual, and optimization choices, including Muon/AdamW training. Native context is 262,144 tokens, with extension to roughly 1M; these are distinct operating settings.

Text, image, and video inputs produce text. Public weights and inference integrations are available under Qwen Community License 1.0. The paper provides architectural ablations, not a release of the entire pretraining dataset.

</details>

### **dots3-note-preview: Omnimodal MoE with a sparse vision expert encoder**

A sparse vision encoder and audio pathway feed a hybrid sparse-attention and sliding-window MoE language model.

[![Model](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/dots-studio/dots3-note-prev) [![Source](https://img.shields.io/badge/Official-Source-blue?style=flat-square)](https://studio.dots.ai/dots/dots3-en.html)

dots.studio<br>
**Released:** 2026-08-14

*Timeline basis: Explicit preview-release commit dated August 14.*

<!-- architecture-figure:170 -->
> **Architecture figure:** The official dots3 preview card and technical blog provide configuration details but no architecture diagram; the full technical report is still pending.
<!-- /architecture-figure:170 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

The preview specifies a 280B/16B-active language backbone with 46 layers, combining 13 sparse-attention and 33 sliding-window layers. Its vision MoE contains about 7B parameters with 1.2B active, alongside an 800M audio encoder. A multi-token prediction module supports efficient decoding.

The official technical blog and card describe architectural configuration and deployment. A complete training report is still pending, so precise stage sizes, alignment objectives, and post-training datasets are not inferred from other models.

Text, images, video, and audio are accepted within a 512K context; output is text. Apache 2.0 weights are available as a preview. The August 14 release commit, rather than the earlier repository creation timestamp, anchors the timeline.

</details>

### **North Micro Vision: Compact native-resolution vision with multilayer feature injection**

A compact vision-language model injects multiple visual feature levels into a hybrid local/global language decoder.

[![Model](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct) [![Source](https://img.shields.io/badge/Official-Source-blue?style=flat-square)](https://huggingface.co/blog/CohereLabs/meet-north-micro-vision-instruct)

Cohere Labs<br>
**Released:** 2026-08-12

<!-- architecture-figure:165 -->
<p align="center">
  <img src="assets/architectures/165-north-micro-vision.png" alt="Native-resolution vision encoder, multilayer projection, and local/global language decoder." width="820">
</p>
<p align="center"><sub><b>Official architecture diagram.</b> Native-resolution vision encoder, multilayer projection, and local/global language decoder. <a href="https://huggingface.co/blog/CohereLabs/meet-north-micro-vision-instruct">Primary source</a>. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:165 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

A custom 400M vision encoder and in-house 2B language model form the approximately 2.4B system. Vision uses native resolution, 2D rotary positions, and learned 1D embeddings. DeepStack-style projectors inject intermediate visual features into early decoder layers. The decoder repeats three sliding-window layers with rotary positions and one global layer without positional embeddings.

The instruction checkpoint targets OCR, documents, charts, visual reasoning, and grounding. The public card explains the architecture and usage but does not provide a complete reproducible training recipe or corpus inventory.

Text and image inputs produce text or normalized grounding coordinates. Although the underlying language model supports 128K context, the released multimodal model is validated at 8K. Weights are Apache 2.0.

</details>

### **Muse Glimmer: Dense visual agents with local-global attention and diffusion drafting**

A compact dense agent combines a Perception Encoder with local-global attention and a separate block-diffusion speculative drafter.

[![Paper](https://img.shields.io/badge/Report-Primary_source-b31b1b.svg?style=flat-square)](https://ai.meta.com/research/publications/muse-glimmer-30b-an-on-device-agentic-model/) [![Model](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/meta-models/Muse-Glimmer-30B)

Meta Superintelligence Lab<br>
**Released:** 2026-08-10

*Timeline basis: Model publication commit; card specifies August 2026 only.*

<!-- architecture-figure:169 -->
<p align="center">
  <img src="assets/architectures/169-muse-glimmer.png" alt="Muse Glimmer architecture specification table captured from PDF page 2" width="820">
</p>
<p align="center"><sub><b>Table 1.</b> Architecture specifications from the paper; no system schematic is published. <a href="https://ai.meta.com/research/publications/muse-glimmer-30b-an-on-device-agentic-model/">Source paper</a>, PDF p. 2. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:169 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

The roughly 29.6B model includes a 1.8B ViT-G/14 perception encoder. Its 52-layer language stack repeats three local layers and one global layer, with gated grouped-query attention and rotary positions confined to local layers. An optional five-layer DFlash drafter proposes sixteen-token blocks for verification.

Distillation from Muse Spark and agent-focused post-training target tool use, multi-step tasks, and recovery from failed actions. Quantized checkpoints and drafter variants support local inference.

The card lists public, third-party, and Meta-service multimodal data across more than 100 languages, without releasing the full mixture. Inputs are text and images; outputs are text. Weights use Apache 2.0. The card dates the release only to August; August 10 is the model publication commit used here.

</details>

### **Shieldstral: Policy-conditioned visual moderation in one forward pass**

A small visual-language model scores compliance with a supplied natural-language policy without lengthy response generation.

[![Paper](https://img.shields.io/badge/arXiv-2607.25857-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2607.25857) [![Model](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/mistralai/Shieldstral-1.0-3B) [![Source](https://img.shields.io/badge/Official-Source-blue?style=flat-square)](https://mistral.ai/news/shieldstral/)

Mistral AI<br>
**Released:** 2026-08-04

<!-- architecture-figure:183 -->
<p align="center">
  <img src="assets/architectures/183-shieldstral.png" alt="Shieldstral architecture or training overview from its primary paper" width="820">
</p>
<p align="center"><sub><b>Figure 1.</b> A small visual-language model scores compliance with a supplied natural-language policy without lengthy response generation. <a href="https://arxiv.org/abs/2607.25857">Source paper</a>, PDF p. 2. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:183 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

Shieldstral-1.0-3B adapts Ministral 3 with Pixtral visual perception. A policy and text/image content condition a binary decision and confidence score. Classification uses one forward pass, separating moderation decisions from general assistant generation.

The report studies policy-conditioned training and evaluation across varied moderation policies. The released model was trained at 32K context; the larger architectural context limit is not equivalent to validated training coverage.

The public checkpoint supports twelve languages and both textual and visual inputs under Apache 2.0. The August 4 announcement is the release date; the preceding technical report documents the method. Dataset composition and evaluation protocols are described in the report rather than inferred from the base model.

</details>

### **MODUS: Decoder-Only Any-to-Any Multimodal Modeling**

MODUS shares a decoder context across modalities, with discrete autoregressive and continuous flow-matching experts enabling chained generation and cross-modal self-verification.

[![arXiv](https://img.shields.io/badge/arXiv-2607.25948-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2607.25948) [![Project](https://img.shields.io/badge/Project-MODUS-blue?style=flat-square)](https://modus-multimodal.epfl.ch/)

Mingqiao Ye et al., EPFL<br>
**Released:** 2026-07-28

<!-- architecture-figure:1 -->
<p align="center">
  <img src="assets/architectures/modus-2026-arch.png" alt="MODUS: Decoder-Only Any-to-Any Multimodal Modeling architecture: Decoder-only any-to-any modeling across tokenized 1D and 2D modalities" width="820">
</p>
<p align="center"><sub><b>Figure 2.</b> Decoder-only any-to-any modeling across tokenized 1D and 2D modalities. <a href="https://arxiv.org/abs/2607.25948">Source paper</a>, PDF p. 4. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:1 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**MODUS** builds on BAGEL's mixture-of-transformer design, sharing a causal context across modalities while retaining two experts. Discrete 1D representations use autoregressive next-token prediction; continuous 2D representations use latent flow matching. Attention is causal within 1D sequences, bidirectional within 2D modalities, and causal between modalities. Vision uses both semantic ViT features and VAE latents.

The experts are trained with different objectives: cross-entropy for discrete tokens and mean-squared error for the continuous velocity field. Thus, the paper's symmetric modality formulation should not be read as eliminating separate experts or loss functions. The training mixture connects text, RGB, geometry, segmentation, edges, and visual feature representations, allowing intermediate-modality chains and self-verification within one checkpoint.

</details>

### **Argus-Unified: Economical Understanding and Generation**

Argus-Unified combines continuous tokens for understanding with learned discrete tokens for generation, reusing a frozen unified visual encoder and pretrained VLM to lower the cost of unified modeling.

[![arXiv](https://img.shields.io/badge/arXiv-2607.25527-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2607.25527)

Weiming Zhuang et al.<br>
**Released:** 2026-07-28

<!-- architecture-figure:2 -->
<p align="center">
  <img src="assets/architectures/argus-unified-2026-arch.png" alt="Argus-Unified: Economical Understanding and Generation architecture: Two-stage hybrid-token training for unified image understanding and generation" width="820">
</p>
<p align="center"><sub><b>Figure 3.</b> Two-stage hybrid-token training for unified image understanding and generation. <a href="https://arxiv.org/abs/2607.25527">Source paper</a>, PDF p. 4. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:2 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**Argus-Unified** resolves the conflicting visual representations required by comprehension and synthesis through hybrid visual tokens. Continuous encoder features preserve semantic information for understanding, while a learned quantizer produces discrete tokens for image generation from the same frozen visual encoder.

Training first learns the quantizer and image decoder, then initializes the language component from a pretrained VLM and trains unified multimodal prediction. The reported recipe uses 15.6 million examples and roughly $2,000 of compute, positioning the model as a reproducible baseline for understanding-and-generation research rather than a scale demonstration.

</details>

### **Kimi K3: Kimi Delta Attention at Trillion-Parameter Scale**

Kimi K3 is a native multimodal sparse MoE that combines Kimi Delta Attention, gated latent attention, Attention Residuals, and 896 routed experts for million-token reasoning and agency.

[![arXiv](https://img.shields.io/badge/arXiv-2607.24653-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2607.24653) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/MoonshotAI/Kimi-K3) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/moonshotai/Kimi-K3)

Kimi Team, Moonshot AI<br>
**Released:** 2026-07-27

<!-- architecture-figure:3 -->
<p align="center">
  <img src="assets/architectures/kimi-k3-2026-arch.png" alt="Kimi K3: Kimi Delta Attention at Trillion-Parameter Scale architecture: Kimi Delta Attention, Stable LatentMoE, Attention Residuals, and MoonViT-V2" width="820">
</p>
<p align="center"><sub><b>Figure 2.</b> Kimi Delta Attention, Stable LatentMoE, Attention Residuals, and MoonViT-V2. <a href="https://arxiv.org/abs/2607.24653">Source paper</a>, PDF p. 3. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:3 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**Kimi K3** has 2.8T total and 104B active parameters across 93 layers. Sixty-nine layers use gated delta-rule linear attention and 24 use gated Multi-head Latent Attention; learned Attention Residuals create structured information paths across depth. Stable LatentMoE activates 16 of 896 routed experts plus two shared experts, making the model unusually sparse for its scale.

A 401M-parameter MoonViT-V2 encoder supplies native image and video input. The model supports a 1,048,576-token context and receives multimodal, long-context, agentic, reasoning, and tool-use training. Quantization-aware pretraining targets MXFP4 weights and MXFP8 activations rather than treating low-precision deployment as an afterthought.

</details>

### **Mage-VL: Codec-Native Streaming Multimodality**

Mage-VL uses video-codec signals to encode only dynamic, information-rich regions and pairs a lightweight event gate with a causal decoder for proactive streaming perception.

[![arXiv](https://img.shields.io/badge/arXiv-2607.24904-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2607.24904) [![Project](https://img.shields.io/badge/Project-Mage--VL-blue?style=flat-square)](https://microsoft.github.io/Mage/)

Senqiao Yang et al., Microsoft Research<br>
**Released:** 2026-07-27

<!-- architecture-figure:4 -->
<p align="center">
  <img src="assets/architectures/mage-vl-2026-arch.png" alt="Mage-VL: Codec-Native Streaming Multimodality architecture: Codec-native streaming perception with an event gate and causal language decoder" width="820">
</p>
<p align="center"><sub><b>Figure 3.</b> Codec-native streaming perception with an event gate and causal language decoder. <a href="https://arxiv.org/abs/2607.24904">Source paper</a>, PDF p. 8. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:4 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**Mage-ViT** replaces uniform frame sampling with selective 16×16-patch encoding guided by motion vectors and residual energy across anchor and predicted frames. This codec-native tokenization reduces visual-token use by more than 75% while retaining spatiotemporal context. The encoder is trained from scratch on roughly 560M unlabeled images and 100M unlabeled video frames.

The complete VLM uses a dual-system design: a small event gate decides when a stream warrants deeper processing, and a causal decoder performs contextual reasoning. This turns streaming perception into an event-driven process and yields up to a reported 3.5× wall-clock speedup while retaining static-image and spatial reasoning ability.

</details>

### **Apertus 1.5: Early fusion of discrete visual and audio tokens**

An unchanged language decoder learns image and audio understanding through early fusion of discrete modality tokens.

[![Model](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/swiss-ai/Apertus-v1.5-70B) [![Source](https://img.shields.io/badge/Official-Source-blue?style=flat-square)](https://huggingface.co/blog/swiss-ai/apertus-v15-release-notes)

Swiss AI Initiative<br>
**Released:** 2026-07-24

*Timeline basis: July 24 weight release explicitly recorded in October 15 release notes.*

<!-- architecture-figure:184 -->
<p align="center">
  <img src="assets/architectures/184-apertus-1-5.png" alt="Apertus 1.5 continued-pretraining and post-training stages." width="820">
</p>
<p align="center"><sub><b>Official architecture diagram.</b> Apertus 1.5 continued-pretraining and post-training stages. <a href="https://huggingface.co/blog/swiss-ai/apertus-v15-release-notes">Primary source</a>. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:184 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

Apertus 1.5 extends 8B and 70B decoders by expanding their vocabulary with Emu3.5 visual tokens and WavTokenizer audio tokens. A 512-pixel image maps to 1,024 discrete tokens; audio uses a 40Hz token stream. No separate continuous vision tower is attached to the decoder.

Continued pretraining mixes text with unpaired and paired multimodal data, followed by cooldown and long-context stages. Supervised tuning and preference/reward-based alignment develop instruction following and tool behavior.

The release notes document 4T/2T continued-pretraining budgets for the respective scales and link data-transparency records. Context extends to 256K. Inputs are text, images, and audio; output is text. Apache-licensed weights were released July 24; October 15 is the release-notes publication date.

</details>

### **Audio-Visual Flamingo: Temporally aligned audio-video reasoning over long clips**

Interleaved audio and visual features with constrained rotary time embeddings support grounded reasoning over long videos.

[![Paper](https://img.shields.io/badge/arXiv-2607.16107-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2607.16107) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/NVIDIA/audio-flamingo) [![Model](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/nvidia/nemotron-labs-audio-visual-flamingo-hf)

Sreyan Ghosh et al., NVIDIA and collaborators<br>
**Released:** 2026-07-17

*Timeline basis: First arXiv submission; June 29 card label is a checkpoint date.*

<!-- architecture-figure:178 -->
<p align="center">
  <img src="assets/architectures/178-audio-visual-flamingo.png" alt="Audio-Visual Flamingo architecture or training overview from its primary paper" width="820">
</p>
<p align="center"><sub><b>Figure 2.</b> Paper architecture, including an optional speech-generation path; the released checkpoint produces text only. <a href="https://arxiv.org/abs/2607.16107">Source paper</a>, PDF p. 4. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:178 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

SigLIP with Dynamic-S2 processing and an AF-Whisper audio encoder connect through separate MLP projectors to Qwen2.5-7B. Time-aligned chunks are interleaved, and Constrained Rotary Time Embeddings encode their correspondence. The released checkpoint generates text, not speech.

A three-stage curriculum progresses from short clips to long-video supervised training and then chain-of-thought tuning with GRPO. Temporal interleaved reasoning explicitly references evidence timestamps.

Audio-Visual-Skills contains about 7M caption/QA instances; AVF-Instruct and AVF-Think support instruction and reasoning stages. The final stage supports roughly fifteen-minute clips at 32K tokens. Weights use NVIDIA’s noncommercial research terms. The timeline uses the paper date, not the June 29 internal checkpoint label.

</details>

### **Inkling: Relative-Position Multimodal Mixture of Experts**

Inkling is an open-weight multimodal MoE trained from scratch on text, images, audio, and video, using relative positions and alternating local/global attention for million-token contexts.

[![Website](https://img.shields.io/badge/Official-Inkling-blue?style=flat-square)](https://thinkingmachines.ai/news/introducing-inkling/) [![Model Card](https://img.shields.io/badge/Model_Card-Inkling-blue?style=flat-square)](https://thinkingmachines.ai/model-card/inkling/) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/thinkingmachines/Inkling)

Thinking Machines Lab<br>
**Released:** 2026-07-15

<!-- architecture-figure:5 -->
> **Architecture figure:** The official Inkling model card contains no architecture figure.
<!-- /architecture-figure:5 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**Inkling** contains 975B total and 41B active parameters. Its MoE layers activate six of 256 routed experts plus two shared experts using sigmoid routing and auxiliary-loss-free balancing. Attention alternates five local sliding-window layers with one global layer and uses learned relative-position representations rather than RoPE; short convolutions further refine key, value, attention, and MLP pathways.

Pretraining spans 45T text, image, audio, and video tokens. Post-training begins with a small synthetic supervised bootstrap and scales asynchronous reinforcement learning across multimodal understanding, tools, coding, mathematics, conversation, and safety. The released weights support controllable reasoning effort and contexts up to one million tokens.

</details>

### **Hy-Embodied-VLM: Sparse-MoE Reasoning for Physical Agents**

Hy-Embodied-VLM-1.0 joins a native-aspect-ratio vision encoder to a compact sparse MoE and trains an action-centric reasoning hierarchy for perception, planning, reflection, and recovery.

[![arXiv](https://img.shields.io/badge/arXiv-2607.12894-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2607.12894) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/Tencent-Hunyuan/HY-Embodied) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/tencent/Hy-Embodied-VLM-1.0)

Tencent Robotics X, Hy Vision Team and Futian Laboratory<br>
**Released:** 2026-07-15

<!-- architecture-figure:6 -->
<p align="center">
  <img src="assets/architectures/hy-embodied-vlm-2026-arch.png" alt="Hy-Embodied-VLM: Sparse-MoE Reasoning for Physical Agents architecture: Self-evolving supervised fine-tuning, rejection sampling, and specialized reinforcement learning" width="820">
</p>
<p align="center"><sub><b>Figure 4.</b> Self-evolving supervised fine-tuning, rejection sampling, and specialized reinforcement learning. <a href="https://arxiv.org/abs/2607.12894">Source paper</a>, PDF p. 11. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:6 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**Hy-Embodied-VLM-1.0** connects Hy-ViT2 to a roughly 30B-total, 3B-active language model. Each sparse-MoE layer selects eight of 128 routed experts plus one shared expert. It accepts as many as 128 images in a 32K context and exposes direct-response and explicit-thinking modes through the same checkpoint.

Its curriculum moves from action-relevant state understanding to transition reasoning and then sequential, adaptive reasoning. A self-evolving post-training loop alternates reinforcement learning with rejection-sampling fine-tuning, separately optimizing geometric precision and higher-level planning before policy fusion.

</details>

### **MonkeyOCRv2: Document-Native Visual-Text Pretraining**

MonkeyOCRv2 learns document vision jointly through image-to-text generation and pixel reconstruction, preserving both semantic content and character-level strokes across 17 languages.

[![arXiv](https://img.shields.io/badge/arXiv-2607.11562-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2607.11562) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/Yuliang-Liu/MonkeyOCRv2)

Yuliang Liu et al.<br>
**Released:** 2026-07-11

<!-- architecture-figure:7 -->
<p align="center">
  <img src="assets/architectures/monkeyocrv2-2026-arch.png" alt="MonkeyOCRv2: Document-Native Visual-Text Pretraining architecture: Document-native pretraining through text generation and pixel reconstruction" width="820">
</p>
<p align="center"><sub><b>Figure 1.</b> Document-native pretraining through text generation and pixel reconstruction. <a href="https://arxiv.org/abs/2607.11562">Source paper</a>, PDF p. 2. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:7 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**MonkeyOCRv2** is a visual-text foundation encoder specialized for the properties that natural-image pretraining often misses: dense text, small glyphs, fine strokes, and layout. Its two complementary objectives align images with their transcribed content while forcing the encoder to retain pixel-level document structure.

The MonkeyDoc v2 corpus contains 113M document images in 17 languages. The frozen encoder improves recognition, detection, tamper analysis, segmentation, parsing, and understanding; paired with a lightweight language model, it forms a 0.7B document parser. Public weights were announced July 11, two days before the arXiv report, so the timeline follows the model release rather than the paper date.

</details>

### **DiffusionGemma: Cached causal context with a block-diffusion text decoder**

A causal context encoder supplies cached memory to a bidirectional diffusion decoder that generates text in blocks.

[![Paper](https://img.shields.io/badge/arXiv-2608.00146-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2608.00146) [![Model](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/google/diffusiongemma-26B-A4B-it) [![Source](https://img.shields.io/badge/Official-Source-blue?style=flat-square)](https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/)

Google DeepMind<br>
**Released:** 2026-06-10

<!-- architecture-figure:168 -->
<p align="center">
  <img src="assets/architectures/168-diffusiongemma.png" alt="DiffusionGemma context encoder and diffusion decoder generation pipeline" width="820">
</p>
<p align="center"><sub>