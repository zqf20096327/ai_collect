# 👁️‍🗨️ Awesome VLM Architectures [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
<!--lint disable double-link-->
![VLM](https://github.com/gokayfem/Awesome-VLM-Architectures/assets/88277926/5c9ee091-1f37-4d92-8398-a7d4e006c014)

**Awesome VLM Architectures** is a citation-first visual catalog of **155+ Vision-Language Model (VLM/MLLM) architectures**, spanning contrastive encoders, multimodal LLMs, native multimodal models, unified understanding and generation, video, OCR, GUI agents, and embodied AI. Each entry links to primary sources and summarizes the model architecture, modality alignment or fusion, training stages, datasets, and distinctive design choices, with an architectural figure when available.

Use this repository to compare multimodal model families, trace architectural ideas over time, or retrieve grounded references for research and AI-agent workflows. The catalog includes a verified release timeline through July 2026 and covers foundational systems such as CLIP and Flamingo alongside current multimodal reasoning and agentic models. **Expand any model panel for its detailed architecture summary.**

- 📙 <a href="https://github.com/gokayfem/ComfyUI_VLM_nodes">Visit my other repo to try Vision Language Models on ComfyUI</a>

*Last reviewed: August 1, 2026.*

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
<summary>🧭 <i>Chronological Model Index (155 architectures, newest first)</i></summary>

**2026:** [MODUS](#modus-decoder-only-any-to-any-multimodal-modeling) | [Argus-Unified](#argus-unified-economical-understanding-and-generation) | [Kimi K3](#kimi-k3-kimi-delta-attention-at-trillion-parameter-scale) | [Mage-VL](#mage-vl-codec-native-streaming-multimodality) | [Inkling](#inkling-relative-position-multimodal-mixture-of-experts) | [Hy-Embodied-VLM](#hy-embodied-vlm-sparse-moe-reasoning-for-physical-agents) | [MonkeyOCRv2](#monkeyocrv2-document-native-visual-text-pretraining) | [MiniMax M3](#minimax-m3-native-multimodality-with-sparse-long-context-attention) | [InternVideo3](#internvideo3-multimodal-contextual-reasoning-for-video-agents) | [Keye-VL 2.0](#keye-vl-20-sparse-attention-for-long-video-agents) | [Zamba2-VL](#zamba2-vl-hybrid-state-space-vision-language-modeling) | [Cosmos 3](#cosmos-3-omnimodal-world-modeling-with-mixture-of-transformers) | [Lance](#lance-unified-image-and-video-understanding-generation-and-editing) | [ZAYA1-VL](#zaya1-vl-vision-specialized-compressed-convolutional-attention) | [Falcon Perception](#falcon-perception-early-fusion-grounding-segmentation-and-ocr) | [GLM-5V-Turbo](#glm-5v-turbo-native-multimodal-agency) | [PLaMo 2.1-VL](#plamo-21-vl-lightweight-japanese-vision-language-modeling) | [EXAONE 4.5](#exaone-45-native-multimodal-pretraining-for-documents) | [BidirLM and BidirLM-Omni](#bidirlm-and-bidirlm-omni-causal-decoders-as-multimodal-encoders) | [Gemma 4](#gemma-4-open-weight-native-multimodal-models) | [Penguin-VL](#penguin-vl-efficient-vlms-with-llm-based-vision-encoders) | [Phi-4-Reasoning-Vision](#phi-4-reasoning-vision-compact-multimodal-reasoning) | [V-SONAR and V-LCM](#v-sonar-and-v-lcm-vision-language-modeling-in-concept-space) | [Qwen3.5](#qwen35-native-multimodal-hybrid-attention-models) | [Youtu-VL](#youtu-vl-unified-autoregressive-supervision-for-dense-vision) | [Kimi K2.5 and K2.6](#kimi-k25-and-k26-native-multimodal-agentic-moe) | [Step3-VL-10B](#step3-vl-10b-language-aligned-perception-with-16-token-compression)

**2025:** [ERNIE 5.0](#ernie-50-unified-autoregressive-omnimodal-mixture-of-experts) | [DeepSeek-OCR](#deepseek-ocr-visual-context-compression-through-deepencoder) | [PaddleOCR-VL](#paddleocr-vl-ultra-compact-multilingual-document-parsing) | [Qwen3-VL](#qwen3-vl-deepstack-vision-language-models) | [Step3](#step3-model-system-co-design-for-cost-effective-multimodal-intelligence) | [GLM-4.1V-Thinking](#glm-41v-thinking-general-purpose-multimodal-reasoning-through-curriculum-sampled-rl) | [ERNIE 4.5-VL](#ernie-45-vl-heterogeneous-modality-mixture-of-experts) | [MiMo-VL](#mimo-vl-multimodal-pretraining-with-mixed-on-policy-reinforcement-learning) | [BAGEL](#bagel-a-mixture-of-transformer-experts-for-unified-understanding-and-generation) | [Seed1.5-VL](#seed15-vl-sparse-moe-multimodal-understanding-and-agentic-reasoning) | [InternVL3 and InternVL3.5](#internvl3-and-internvl35-native-multimodal-pretraining-and-adaptive-resolution) | [Kimi-VL](#kimi-vl-native-resolution-vision-with-a-sparse-moe-decoder) | [Llama 4 Scout and Maverick](#llama-4-scout-and-maverick-native-multimodal-mixture-of-experts-models) | [Qwen2.5-Omni](#qwen25-omni-streaming-multimodal-perception-and-speech-generation) | [Gemma 3](#gemma-3-long-context-multimodality-with-efficient-interleaved-attention) | [Aya Vision](#aya-vision-multilingual-multimodality-through-cross-modal-model-merging) | [Phi-4-multimodal](#phi-4-multimodal-text-vision-and-speech-through-mixture-of-loras) | [SigLIP 2](#siglip-2-multilingual-vision-language-encoders-with-native-aspect-ratio-support) | [EVEv2](#evev2-improved-baselines-for-encoder-free-vision-language-models) | [Qwen2.5-VL](#qwen25-vl-enhanced-vision-language-capabilities-in-the-qwen-series) | [VideoLLaMA 3](#videollama-3-frontier-multimodal-foundation-models-for-image-and-video-understanding) | [UI-TARS](#ui-tars-pioneering-automated-gui-interaction-with-native-agents) | [MiniMax-01](#minimax-01-scaling-foundation-models-with-lightning-attention) | [MiniCPM-o-2.6](#minicpm-o-26-a-gpt-4o-level-mllm-for-vision-speech-and-multimodal-live-streaming) | [Eagle 2](#eagle-2-building-post-training-data-strategies-from-scratch-for-frontier-vision-language-models) | [Sa2VA](#sa2va-marrying-sam2-with-llava-for-dense-grounded-understanding-of-images-and-videos)

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
<summary>🗓️ <i>Release Timeline (155 architectures, newest first)</i></summary>

| Date | Architecture | Distinctive contribution |
| --- | --- | --- |
| 2026-07-28 | MODUS | Decoder-only any-to-any modeling without modality-specific heads or losses |
| 2026-07-28 | Argus-Unified | Hybrid continuous and discrete visual tokens for economical understanding and generation |
| 2026-07-27 | Kimi K3 | Kimi Delta Attention, Attention Residuals, and extremely sparse LatentMoE routing |
| 2026-07-27 | Mage-VL | Codec-native selective video tokenization with a proactive event gate |
| 2026-07-15 | Inkling | Relative-position million-context multimodal MoE trained from scratch |
| 2026-07-15 | Hy-Embodied-VLM | Action-centric sparse-MoE reasoning for physical-world agents |
| 2026-07-11 | MonkeyOCRv2 | Joint image-to-text and pixel-reconstruction pretraining for document vision |
| 2026-06-11 | MiniMax M3 | Native multimodality with block-sparse grouped-query attention at million-token context |
| 2026-06-10 | InternVideo3 | Token-preserving latent KV compression and closed-loop video reasoning |
| 2026-06-09 | Keye-VL 2.0 | DeepSeek Sparse Attention adapted to GQA-based long-video multimodality |
| 2026-06-02 | Zamba2-VL | Hybrid Mamba-2 and shared-attention blocks for efficient VLM inference |
| 2026-05-31 | Cosmos 3 | Coupled autoregressive reasoner and diffusion generator for physical AI |
| 2026-05-18 | Lance | Shared-sequence understanding, generation, and editing with modality experts |
| 2026-05-08 | ZAYA1-VL | Vision-conditional LoRA and compressed convolutional attention in an open-data MoE |
| 2026-05-03 | Falcon Perception | Early fusion with hybrid attention and continuous mask heads |
| 2026-04-29 | GLM-5V-Turbo | Perception integrated into reasoning, planning, tools, and execution |
| 2026-04-21 | PLaMo 2.1-VL | Compact Japanese VQA and grounding for edge deployment |
| 2026-04-09 | EXAONE 4.5 | Native multimodal pretraining with document-focused data and 256K context |
| 2026-04-02 | BidirLM and BidirLM-Omni | Converting causal decoders into bidirectional multimodal encoders |
| 2026-03-31 | Gemma 4 | Dense and MoE native multimodality, including an encoder-free 12B design |
| 2026-03-06 | Penguin-VL | Text-LLM-initialized vision encoder and priority-aware token compression |
| 2026-03-04 | Phi-4-Reasoning-Vision | Mid-fusion compact VLM with explicit reasoning and direct-answer modes |
| 2026-03-01 | V-SONAR and V-LCM | Vision-language alignment and prediction in multilingual concept space |
| 2026-02-16 | Qwen3.5 | Native early fusion with hybrid linear/full attention and sparse MoE variants |
| 2026-01-27 | Youtu-VL | Unified autoregressive visual tokens that emit dense vision outputs without task heads |
| 2026-01-27 | Kimi K2.5 and K2.6 | Trillion-parameter native multimodal MoE for agents and computer use |
| 2026-01-14 | Step3-VL-10B | Language-aligned perception encoder with 16-fold visual-token compression |
| 2025-11-13 | ERNIE 5.0 | One autoregressive sparse MoE for text, images, video, audio, and generation |
| 2025-10-20 | DeepSeek-OCR | DeepEncoder compresses high-resolution documents into very short visual contexts |
| 2025-10-16 | PaddleOCR-VL | NaViT-style dynamic resolution with a compact ERNIE decoder for document parsing |
| 2025-09-22 | Qwen3-VL | DeepStack multi-level ViT fusion and explicit video timestamp alignment |
| 2025-07-25 | Step3 | Model-system co-design for communication-efficient sparse-MoE multimodality |
| 2025-07-01 | GLM-4.1V-Thinking | Curriculum-sampled reinforcement learning for multimodal reasoning |
| 2025-06-30 | ERNIE 4.5-VL | Heterogeneous shared and modality-specific experts with isolated routing |
| 2025-06-04 | MiMo-VL | Four-stage multimodal pretraining followed by mixed on-policy RL |
| 2025-05-20 | BAGEL | Mixture-of-Transformer-Experts for understanding and generation |
| 2025-05-11 | Seed1.5-VL | Compact vision encoder with a 20B-active MoE for reasoning and agents |
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

### **MODUS: Decoder-Only Any-to-Any Multimodal Modeling**

MODUS treats every modality symmetrically as both input and output, enabling chained generation and cross-modal self-verification without modality-specific heads, losses, or task pipelines.

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

**MODUS** is a decoder-only any-to-any model that represents diverse modalities inside one autoregressive architecture. Unlike encoder-decoder or diffusion systems assembled around modality-specific output paths, the same model predicts any supported modality from any combination of the others. This makes intermediate-modality chains and self-scoring through a second generated modality native behaviors rather than external workflows.

The design deliberately reuses strong pretrained decoder-only priors instead of training a bespoke multimodal stack from scratch. A single checkpoint is evaluated across heterogeneous tasks and modalities, making MODUS most notable as a general architectural formulation rather than a narrowly optimized VLM endpoint.

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

### **MiniMax M3: Native Multimodality with Sparse Long-Context Attention**

MiniMax M3 combines native multimodal pretraining with learned block-sparse grouped-query attention, making million-token contexts practical in a 109B-parameter model.

[![arXiv](https://img.shields.io/badge/arXiv-2606.13392-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2606.13392) [![Website](https://img.shields.io/badge/Official-MiniMax_M3-blue?style=flat-square)](https://www.minimax.io/blog/minimax-m3) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/MiniMaxAI/MiniMax-M3)

MiniMax<br>
**Released:** 2026-06-11

<!-- architecture-figure:8 -->
<p align="center">
  <img src="assets/architectures/minimax-m3-2026-arch.png" alt="MiniMax M3: Native Multimodality with Sparse Long-Context Attention architecture: MiniMax Sparse Attention index and exact-attention branches" width="820">
</p>
<p align="center"><sub><b>Figure 1.</b> MiniMax Sparse Attention index and exact-attention branches. <a href="https://arxiv.org/abs/2606.13392">Source paper</a>, PDF p. 1. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:8 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**MiniMax Sparse Attention** adds a lightweight index branch that scores KV blocks independently for each grouped-query-attention group. The main branch performs exact attention only over selected blocks, while a KV-outer kernel groups queries retrieving the same block to improve memory locality and reuse.

The released 109B-parameter model is trained natively across modalities and evaluated at contexts up to one million tokens. The sparse-attention report focuses on architecture, kernel design, and scaling behavior; it does not publish a complete source-level training-data inventory.

</details>

### **InternVideo3: Multimodal Contextual Reasoning for Video Agents**

InternVideo3 reframes long-video understanding as an evolving loop of observation, reasoning, tools, and memory, while compressing KV state without dropping the underlying token stream.

[![arXiv](https://img.shields.io/badge/arXiv-2606.12195-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2606.12195)

Ziang Yan et al.<br>
**Released:** 2026-06-10

<!-- architecture-figure:9 -->
<p align="center">
  <img src="assets/architectures/internvideo3-2026-arch.png" alt="InternVideo3: Multimodal Contextual Reasoning for Video Agents architecture: InternVideo3 with multimodal multi-head latent attention across long contexts" width="820">
</p>
<p align="center"><sub><b>Figure 2.</b> InternVideo3 with multimodal multi-head latent attention across long contexts. <a href="https://arxiv.org/abs/2606.12195">Source paper</a>, PDF p. 7. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:9 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**Multimodal Contextual Reasoning** maintains one evolving context containing observations, instructions, intermediate reasoning, tool actions, and memory. This closed loop lets the model accumulate and verify evidence across long videos rather than treating video QA as a single static prompt.

**Multimodal Multi-head Latent Attention** reparameterizes and compresses KV-cache states while preserving the complete visual-token sequence. Training combines continued pretraining, short-to-long supervised tuning, rule-based reinforcement learning, and on-policy distillation; a retrieval-equipped video-agent implementation demonstrates the intended tool-using setting.

</details>

### **Keye-VL 2.0: Sparse Attention for Long-Video Agents**

Keye-VL 2.0 adapts DeepSeek Sparse Attention to a GQA-based multimodal MoE, targeting lossless 256K contexts, hour-scale video, and self-correcting tool-using agents.

[![arXiv](https://img.shields.io/badge/arXiv-2606.10651-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2606.10651)

Kwai Keye Team<br>
**Released:** 2026-06-09

<!-- architecture-figure:10 -->
<p align="center">
  <img src="assets/architectures/keye-vl-2-0-2026-arch.png" alt="Keye-VL 2.0: Sparse Attention for Long-Video Agents architecture: Four-stage curriculum extending Keye-VL from alignment to 256K context" width="820">
</p>
<p align="center"><sub><b>Figure 2.</b> Four-stage curriculum extending Keye-VL from alignment to 256K context. <a href="https://arxiv.org/abs/2606.10651">Source paper</a>, PDF p. 8. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:10 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**Keye-VL-2.0-30B-A3B** is the first reported adaptation of DeepSeek Sparse Attention to grouped-query multimodal attention. Only 3B of 30B parameters activate per token, while the sparse retrieval mechanism keeps critical frames and long-range dependencies accessible across a 256K context. Heterogeneous ViT-language-model parallelism and custom sparse-attention kernels address the systems cost of hour-long video.

Cross-Modal Multi-Teacher On-Policy Distillation feeds dense token-level guidance from specialist teachers back into on-policy trajectories. Context-RL and Video-RL then target long-context reasoning, temporal localization, code, search, tools, and multimodal self-correction without collapsing the multi-task mixture.

</details>

### **Zamba2-VL: Hybrid State-Space Vision-Language Modeling**

Zamba2-VL combines efficient Mamba-2 state-space layers with a small number of shared Transformer blocks, reducing long-context prefill and recurrent-state costs across compact VLM scales.

[![arXiv](https://img.shields.io/badge/arXiv-2606.00390-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2606.00390) [![Project](https://img.shields.io/badge/Official-Zamba2--VL-blue?style=flat-square)](https://www.zyphra.com/our-work/zamba2-vl)

Zyphra<br>
**Released:** 2026-06-02

<!-- architecture-figure:11 -->
<p align="center">
  <img src="assets/architectures/zamba2-vl-2026-arch.png" alt="Zamba2-VL: Hybrid State-Space Vision-Language Modeling architecture: Zamba2 hybrid state-space language backbone connected to a vision encoder" width="820">
</p>
<p align="center"><sub><b>Figure 1.</b> Zamba2 hybrid state-space language backbone connected to a vision encoder. <a href="https://arxiv.org/abs/2606.00390">Source paper</a>, PDF p. 3. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:11 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**Zamba2-VL** extends the Zamba hybrid backbone to vision-language inputs in 1.2B, 2.7B, and 7B variants. Most sequence processing occurs in Mamba-2 state-space layers, with a small set of shared attention blocks supplying global token interaction. This preserves transformer-like multimodal reasoning while moving more computation toward near-linear prefill and bounded recurrent state.

The architecture is particularly relevant for edge and long-context deployment: visual sequences can be large even when the language model is small, so reducing quadratic attention changes time-to-first-token and memory behavior more materially than ordinary parameter pruning.

</details>

### **Cosmos 3: Omnimodal World Modeling with Mixture of Transformers**

Cosmos 3 couples an autoregressive reasoner with a diffusion generator through a shared representation for language, vision, audio, actions, simulation, and robot control.

[![arXiv](https://img.shields.io/badge/arXiv-2606.02800-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2606.02800) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/NVIDIA/cosmos) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Models-blue?style=flat-square)](https://huggingface.co/collections/nvidia/cosmos3)

NVIDIA<br>
**Released:** 2026-05-31

<!-- architecture-figure:12 -->
<p align="center">
  <img src="assets/architectures/cosmos-3-2026-arch.png" alt="Cosmos 3: Omnimodal World Modeling with Mixture of Transformers architecture: Mixture-of-Transformers reasoner and generator with shared attention" width="820">
</p>
<p align="center"><sub><b>Figure 5.</b> Mixture-of-Transformers reasoner and generator with shared attention. <a href="https://arxiv.org/abs/2606.02800">Source paper</a>, PDF p. 11. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:12 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**Cosmos 3** uses a Mixture-of-Transformers with two communicating towers. An autoregressive transformer reasons over language, vision, and action sequences; a diffusion transformer generates continuous images, video, and world trajectories. Their shared representation lets the family serve as a VLM, forward or inverse dynamics model, simulator, generator, or policy without separate task pipelines.

Nano configurations combine 8B-class components and Super configurations combine 32B-class components. Training spans text, image, video, audio, simulated physical interaction, action trajectories, robot demonstrations, driving, and synthetic worlds. The July 20 Cosmos 3 Edge release preserves the same two-tower design in a smaller real-time deployment branch and is folded into this family.

</details>

### **Lance: Unified Image and Video Understanding, Generation, and Editing**

Lance is a compact model trained from scratch to understand, generate, and edit images and video inside one interleaved sequence while preserving specialized semantic and synthesis capacity.

[![arXiv](https://img.shields.io/badge/arXiv-2605.18678-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2605.18678) [![Project](https://img.shields.io/badge/Project-Lance-blue?style=flat-square)](https://lance-project.github.io/)

Lance Team<br>
**Released:** 2026-05-18

<!-- architecture-figure:13 -->
<p align="center">
  <img src="assets/architectures/lance-2026-arch.png" alt="Lance: Unified Image and Video Understanding, Generation, and Editing architecture: Dual-expert sequence modeling for understanding and visual generation" width="820">
</p>
<p align="center"><sub><b>Figure 6.</b> Dual-expert sequence modeling for understanding and visual generation. <a href="https://arxiv.org/abs/2605.18678">Source paper</a>, PDF p. 9. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:13 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**Lance** interleaves text, image, and video in a shared 3B-parameter sequence model while routing semantic understanding and visual synthesis through dedicated experts. Semantic ViT tokens coexist with clean or noised VAE latents, and generalized 3D causal attention plus modality-aware positional encoding preserve spatial and temporal relationships.

One checkpoint supports visual understanding, text-to-image and text-to-video generation, image-to-video generation, and editing. Its training-from-scratch recipe uses no more than 128 A100 GPUs, making the contribution as much about an attainable unified architecture as headline generation quality.

</details>

### **ZAYA1-VL: Vision-Specialized Compressed Convolutional Attention**

ZAYA1-VL adds visual capacity to a sparse MoE through vision-only LoRA and compressed-convolutional-attention parameters, trained on an entirely open multimodal data mixture.

[![arXiv](https://img.shields.io/badge/arXiv-2605.08560-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2605.08560) [![Project](https://img.shields.io/badge/Official-ZAYA1--VL-blue?style=flat-square)](https://www.zyphra.com/our-work/zaya1-vl-8b) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/Zyphra/ZAYA1-VL-8B)

Zyphra<br>
**Released:** 2026-05-08

<!-- architecture-figure:14 -->
<p align="center">
  <img src="assets/architectures/zaya1-vl-2026-arch.png" alt="ZAYA1-VL: Vision-Specialized Compressed Convolutional Attention architecture: Visual routing, compressed convolutional attention, and a hybrid language backbone" width="820">
</p>
<p align="center"><sub><b>Figure 2.</b> Visual routing, compressed convolutional attention, and a hybrid language backbone. <a href="https://arxiv.org/abs/2605.08560">Source paper</a>, PDF p. 5. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:14 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**ZAYA1-VL-8B** joins a Qwen2.5-VL visual encoder to ZAYA1's MoE decoder. Vision-only LoRA and Compressed Convolutional Attention parameters activate for visual tokens without duplicating the language backbone, while bidirectional attention within image-token spans improves spatial integration.

The model is trained on roughly 140B vision-language tokens assembled from open data and released under Apache 2.0. Its importance is the clean separation of visual specialization from shared language capacity in a compact sparse model.

</details>

### **Falcon Perception: Early-Fusion Grounding, Segmentation, and OCR**

Falcon Perception uses early image-text fusion, hybrid attention, instance tokens, and continuous mask heads to unify open-vocabulary grounding, segmentation, and OCR in compact models.

[![arXiv](https://img.shields.io/badge/arXiv-2603.27365-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2603.27365) [![Project](https://img.shields.io/badge/Project-Falcon_Perception-blue?style=flat-square)](https://vision.falcon.aidrc.tii.ae/) [![Release](https://img.shields.io/badge/Official-Release-blue?style=flat-square)](https://www.tii.ae/news/tii-launches-falcon-perception-new-multimodal-ai-model-helps-machines-see-and-understand-world)

Technology Innovation Institute<br>
**Released:** 2026-05-03

<!-- architecture-figure:15 -->
<p align="center">
  <img src="assets/architectures/falcon-perception-2026-arch.png" alt="Falcon Perception: Early-Fusion Grounding, Segmentation, and OCR architecture: Early-fusion perception Transformer with grounding, geometry, and segmentation pathways" width="820">
</p>
<p align="center"><sub><b>Figure 1.</b> Early-fusion perception Transformer with grounding, geometry, and segmentation pathways. <a href="https://arxiv.org/abs/2603.27365">Source paper</a>, PDF p. 3. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:15 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**Falcon Perception** is a dense early-fusion Transformer in which image patches and text interact from the first layer. Its attention mask is bidirectional over image tokens and causal over prediction tokens. Variable-length instance tokens identify multiple objects, while lightweight continuous heads produce masks without turning segmentation into an unwieldy text sequence.

The family includes a 600M perception model and a 300M OCR model. The paper was submitted March 28, but the timeline uses the documented May 3 public model launch, following this repository's release-date policy.

</details>

### **GLM-5V-Turbo: Native Multimodal Agency**

GLM-5V-Turbo integrates visual perception into reasoning, planning, tool use, execution, and verification instead of treating images and video as an auxiliary language-model interface.

[![arXiv](https://img.shields.io/badge/arXiv-2604.26752-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2604.26752)

GLM-V Team<br>
**Released:** 2026-04-29

<!-- architecture-figure:16 -->
<p align="center">
  <img src="assets/architectures/glm-5v-turbo-2026-arch.png" alt="GLM-5V-Turbo: Native Multimodal Agency architecture: Multimodal multi-token prediction with image placeholders and shared Transformer blocks" width="820">
</p>
<p align="center"><sub><b>Figure 2.</b> Multimodal multi-token prediction with image placeholders and shared Transformer blocks. <a href="https://arxiv.org/abs/2604.26752">Source paper</a>, PDF p. 3. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:16 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**GLM-5V-Turbo** is organized around end-to-end multimodal agency across images, video, webpages, documents, GUIs, code, and external tools. Its contribution is the integration of perception with the agent loop: observations remain available during planning and execution, and outcomes can be visually verified rather than handed off to a detached captioning stage.

The report describes coordinated changes to model design, multimodal training, hierarchical optimization, reinforcement learning, toolchains, and agent-framework integration. Because this is a new native agent foundation model rather than a latency-only checkpoint, it is kept separate from the GLM-4.1V family.

</details>

### **PLaMo 2.1-VL: Lightweight Japanese Vision-Language Modeling**

PLaMo 2.1-VL provides compact 2B and 8B Japanese-English VLMs that combine visual question answering and grounding for local, edge, and autonomous-device deployment.

[![arXiv](https://img.shields.io/badge/arXiv-2604.19324-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2604.19324)

Tommi Kerola et al., Preferred Networks<br>
**Released:** 2026-04-21

<!-- architecture-figure:17 -->
> **Architecture figure:** The PLaMo 2.1-VL paper contains application and data figures, but no model architecture diagram.
<!-- /architecture-figure:17 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**PLaMo 2.1-VL** is designed around a constrained deployment envelope rather than frontier scale. Both sizes support VQA and bounding-box grounding, with evaluations emphasizing Japanese language operation and applications such as factory tool recognition and infrastructure anomaly detection.

A large synthetic-data pipeline supplies Japanese multimodal instructions, grounding examples, and domain-oriented supervision. The entry broadens the catalog's language and edge coverage; its contribution is a deployable bilingual VQA-and-grounding family rather than a new attention primitive.

</details>

### **EXAONE 4.5: Native Multimodal Pretraining for Documents**

EXAONE 4.5 is LG AI Research's first open-weight VLM, integrating a dedicated visual encoder into EXAONE and emphasizing document-centric native multimodal pretraining and Korean context.

[![arXiv](https://img.shields.io/badge/arXiv-2604.08644-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2604.08644)

Eunbi Choi et al., LG AI Research<br>
**Released:** 2026-04-09

<!-- architecture-figure:18 -->
<p align="center">
  <img src="assets/architectures/exaone-4-5-2026-arch.png" alt="EXAONE 4.5: Native Multimodal Pretraining for Documents architecture: Native-resolution vision encoding, projection, language decoding, and multi-token prediction" width="820">
</p>
<p align="center"><sub><b>Figure 1.</b> Native-resolution vision encoding, projection, language decoding, and multi-token prediction. <a href="https://arxiv.org/abs/2604.08644">Source paper</a>, PDF p. 2. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:18 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**EXAONE 4.5** adds a dedicated vision encoder to the EXAONE 4.0 framework and trains the resulting stack natively over text and visual inputs. Its data mixture is deliberately document-heavy, targeting enterprise documents, OCR-rich layouts, and Korean contextual reasoning while retaining general language capability.

Context extends to 256K tokens for long documents and enterprise workflows. The combination of open weights, native multimodal training, long context, and focused document/Korean coverage makes it a distinct public VLM release rather than a post-training adapter.

</details>

### **BidirLM and BidirLM-Omni: Causal Decoders as Multimodal Encoders**

BidirLM converts pretrained causal language decoders into bidirectional representation encoders; BidirLM-Omni extends the method to one contrastively aligned text, image, and audio embedding model.

[![arXiv](https://img.shields.io/badge/arXiv-2604.02045-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2604.02045) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Models-blue?style=flat-square)](https://huggingface.co/BidirLM) [![Release](https://img.shields.io/badge/Official-Release-blue?style=flat-square)](https://huggingface.co/blog/Nicolas-BZRD/bidirlm-release)

BidirLM Team<br>
**Released:** 2026-04-02

<!-- architecture-figure:19 -->
<p align="center">
  <img src="assets/architectures/bidirlm-and-bidirlm-omni-2026-arch.png" alt="BidirLM and BidirLM-Omni: Causal Decoders as Multimodal Encoders architecture: Specialist-backbone merging with frozen modality projection heads" width="820">
</p>
<p align="center"><sub><b>Figure 10.</b> Specialist-backbone merging with frozen modality projection heads. <a href="https://arxiv.org/abs/2604.02045">Source paper</a>, PDF p. 25. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:19 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**BidirLM** removes the causal mask and adapts a decoder with masked next-token prediction and contrastive learning. Weight merging and mixed-domain training preserve generative knowledge while recovering the full-context interaction needed by retrieval and embedding tasks.

**BidirLM-Omni** combines Qwen3 text, Qwen3-VL, and Qwen3-ASR specialist backbones with frozen visual and audio projectors, aligning all three modalities in one contrastive space. The entry belongs beside CLIP, SigLIP, and ImageBind as an encoder architecture, despite originating from decoder checkpoints.

</details>

### **Gemma 4: Open-Weight Native Multimodal Models**

Gemma 4 is Google DeepMind's open-weight multimodal family spanning mobile-efficient, dense, sparse-MoE, and encoder-free designs, with configurable reasoning and deployment targets ranging from phones to servers.

[![arXiv](https://img.shields.io/badge/arXiv-2607.02770-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2607.02770) [![Releases](https://img.shields.io/badge/Official-Releases-blue?style=flat-square)](https://ai.google.dev/gemma/docs/releases) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Models-blue?style=flat-square)](https://huggingface.co/collections/google/gemma-4)

Gemma Team, Google DeepMind<br>
**Released:** 2026-03-31

<!-- architecture-figure:20 -->
<p align="center">
  <img src="assets/architectures/gemma-4-2026-arch.png" alt="Gemma 4: Open-Weight Native Multimodal Models architecture: Aspect-preserving image resizing, patch pooling, and soft-token production" width="820">
</p>
<p align="center"><sub><b>Figure 2.</b> Aspect-preserving image resizing, patch pooling, and soft-token production. <a href="https://arxiv.org/abs/2607.02770">Source paper</a>, PDF p. 16. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:20 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**Gemma 4** is a suite of related architectures rather than one uniform network. E2B and E4B target mobile and edge deployment; 31B is a dense server-class decoder; and 26B-A4B is a sparse Mixture-of-Experts model with roughly 4B active parameters. These branches accept images through improved visual processing, while the mobile models additionally support audio. The distinctive **Gemma 4 12B Unified** removes separate vision and audio encoders: raw image patches and audio features enter through direct linear projections, reducing duplicated encoder memory and latency. Context windows reach 128K or 256K depending on the variant.

Pretraining jointly develops language, code, reasoning, and multimodal understanding, followed by instruction tuning, safety alignment, and reasoning post-training. A configurable thinking mode lets the instruction-tuned models emit a reasoning trace before answering. The family also ships dedicated multi-token-prediction draft models for speculative decoding, while per-layer embeddings and shared key-value caching improve inference efficiency in applicable variants.

Google describes a large multilingual mixture containing web text, documents, code, mathematics, image-text pairs, OCR and document examples, audio, and video-derived supervision. The complete record-level training corpus is not released, so benchmark collections should not be mistaken for an exhaustive dataset list. Image support includes variable resolutions and aspect ratios; native audio and video coverage depends on the specific branch.

</details>

### **Penguin-VL: Efficient VLMs with LLM-Based Vision Encoders**

Penguin-VL challenges the assumption that compact VLMs require contrastively pretrained vision backbones, adapting a text-only language model into a fine-grained visual encoder for efficient image and video understanding.

[![arXiv](https://img.shields.io/badge/arXiv-2603.06569-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2603.06569) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/tencent-ailab/Penguin-VL) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Models-blue?style=flat-square)](https://huggingface.co/collections/tencent/penguin-vl)

Boqiang Zhang, Lei Ke, Ruihan Yang, Qi Gao, Tianyuan Qu, Rossell Chen, Dong Yu, Leoweiliang<br>
**Released:** 2026-03-06

<!-- architecture-figure:21 -->
<p align="center">
  <img src="assets/architectures/penguin-vl-2026-arch.png" alt="Penguin-VL: Efficient VLMs with LLM-Based Vision Encoders architecture: An LLM-initialized vision encoder with priority-aware video-token compression" width="820">
</p>
<p align="center"><sub><b>Figure 3.</b> An LLM-initialized vision encoder with priority-aware video-token compression. <a href="https://arxiv.org/abs/2603.06569">Source paper</a>, PDF p. 4. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:21 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**Penguin-VL** builds its Penguin-Encoder by initializing a vision backbone from a text-only Qwen3-0.6B model. Causal attention is converted to bidirectional attention, and 2D rotary position embeddings permit variable-resolution visual tokenization. The encoder is connected to compact language decoders to form 2B- and 8B-class VLMs. For video, **Temporal Redundancy-Aware compression** assigns larger token budgets to informative key frames and compresses redundant intermediate frames, allowing longer sequences within a fixed visual-token budget.

Training begins with mixed-supervision encoder adaptation. A teacher vision encoder supplies amplitude, direction, and relational distillation targets while image reconstruction-style supervision stabilizes the LLM-to-vision conversion. A low-to-high-resolution curriculum then aligns the encoder for fine-grained perception, followed by unified image and video multimodal pretraining and instruction tuning. This recipe is designed to preserve OCR, spatial, temporal, and dense-captioning signals that category-oriented contrastive objectives can suppress.

The project releases Penguin-Recap-I, a reconstructed high-quality image training set, and Penguin-Recap-V, video annotations at dense timestamp, paragraph, and whole-video granularities. These resources complement broader image-text, document, OCR, mathematical reasoning, and video instruction mixtures described in the report. The authors' comparisons attribute the compact models' gains primarily to visual representation quality and token allocation rather than parameter scaling alone.

</details>

### **Phi-4-Reasoning-Vision: Compact Multimodal Reasoning**

Phi-4-Reasoning-Vision-15B is a compact open-weight model that combines high-resolution perception with selectable direct and chain-of-thought modes, focusing on mathematical, scientific, document, and GUI reasoning.

[![arXiv](https://img.shields.io/badge/arXiv-2603.03975-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2603.03975) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/microsoft/Phi-4-reasoning-vision-15B) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/microsoft/Phi-4-reasoning-vision-15B)

Jyoti Aneja, Michael Harrison, Neel Joshi, Tyler LaBonte, John Langford, Eduardo Salinas<br>
**Released:** 2026-03-04

<!-- architecture-figure:22 -->
<p align="center">
  <img src="assets/architectures/phi-4-reasoning-vision-2026-arch.png" alt="Phi-4-Reasoning-Vision: Compact Multimodal Reasoning architecture: SigLIP2 vision encoding, cross-modal projection, mid-fusion, and language reasoning" width="820">
</p>
<p align="center"><sub><b>Figure 3.</b> SigLIP2 vision encoding, cross-modal projection, mid-fusion, and language reasoning. <a href="https://arxiv.org/abs/2603.03975">Source paper</a>, PDF p. 4. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:22 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**Phi-4-Reasoning-Vision-15B** uses a mid-fusion architecture built from the Phi-4-Reasoning language backbone and a SigLIP 2 vision encoder. Visual features are projected into the language embedding space and inserted into the decoder sequence. Dynamic-resolution processing produces up to 3,600 visual tokens, supporting fine-grained documents and interface screenshots. Bidirectional attention is restricted to tokens within each image, improving spatial interaction while avoiding the overfitting Microsoft observed with broader bidirectional attention.

The model is trained through supervised fine-tuning on a deliberately mixed curriculum of reasoning and non-reasoning examples. Explicit `<think>` and `<nothink>` modes allow one checkpoint to use extended reasoning for mathematics and science or answer directly for perception-heavy tasks such as captioning, OCR, detection, and grounding. Microsoft reports four days of training on 240 NVIDIA B200 GPUs, followed by safety SFT and automated red-team evaluation.

Training data primarily comprises heavily filtered and corrected open-source vision-language datasets, augmented with synthetic examples, internally produced domain data, and targeted acquisitions. Microsoft emphasizes filtering, error correction, and synthetic augmentation as larger contributors than raw scale, but does not publish a complete source-level dataset inventory. Public evaluations span scientific diagrams, charts, mathematical reasoning, OCR, and GUI grounding; those benchmarks are evaluation references, not a claimed exhaustive training list.

</details>

### **V-SONAR and V-LCM: Vision-Language Modeling in Concept Space**

V-SONAR aligns image and video representations with SONAR's multilingual concept space, enabling text-trained concept models to process vision. V-LCM then instruction-tunes a latent-diffusion Large Concept Model directly over unified visual and linguistic embeddings.

[![arXiv](https://img.shields.io/badge/arXiv-2603.01096-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2603.01096) [![OpenReview](https://img.shields.io/badge/ICLR-2026-8c1b13?style=flat-square)](https://openreview.net/forum?id=4LiX5ddGcU)

Yifu Qiu, Paul-Ambroise Duquenne, Holger Schwenk<br>
**Released:** 2026-03-01

<!-- architecture-figure:23 -->
<p align="center">
  <img src="assets/architectures/v-sonar-and-v-lcm-2026-arch.png" alt="V-SONAR and V-LCM: Vision-Language Modeling in Concept Space architecture: Visual-semantic alignment and concept-space prediction" width="820">
</p>
<p align="center"><sub><b>Figure 1.</b> Visual-semantic alignment and concept-space prediction. <a href="https://arxiv.org/abs/2603.01096">Source paper</a>, PDF p. 3. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:23 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**V-SONAR** starts with Meta's Perception Encoder for image and video features and learns a lightweight projector into the pre-existing SONAR embedding space. Positional embeddings and a temporal-attention layer preserve frame order, while attention pooling produces a modality-level representation compatible with SONAR text concepts. Because the target space is shared with OMNISONAR, the representation can be decoded into text across SONAR's multilingual coverage. A text-only Large Concept Model can also consume these aligned visual embeddings without vision-specific pretraining.

V-SONAR is trained with a coarse-to-fine post-hoc alignment curriculum rather than retraining the foundation encoders from scratch. The alignment uses paired visual-caption supervision and SONAR text embeddings, with staged optimization and asynchronous learning rates for the newly initialized projector and pretrained encoder. **V-LCM** then concatenates V-SONAR visual concepts with SONAR language concepts and retains LCM's two-tower contextualizer and denoiser architecture. It predicts the next continuous concept embedding with the same latent-diffusion objective used during text-only LCM pretraining.

Vision-language instruction tuning uses M3IT, which spans image and video inputs, eight task categories, and 80 languages. Retrieval and captioning experiments additionally use VATEX, DREAM-1K, PE-Video, and VideoXum. The resulting system separates perception, multilingual semantic alignment, and generative concept modeling instead of converting every modality into a single discrete token vocabulary.

</details>

### **Qwen3.5: Native Multimodal Hybrid-Attention Models**

Qwen3.5 unifies text, image, and video understanding in one model family while combining hybrid linear attention with sparse expert routing. Qwen3.6 continues the same native-multimodal direction with stronger agentic coding and updated dense and MoE checkpoints.

[![Blog](https://img.shields.io/badge/Official-Qwen3.5-b31b1b?style=flat-square)](https://qwen.ai/blog?id=qwen3.5) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/QwenLM/Qwen3.6) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/Qwen/Qwen3.5-397B-A17B)

Qwen Team<br>
**Released:** 2026-02-16

<!-- architecture-figure:24 -->
> **Architecture figure:** Qwen3.5 has no public technical paper containing an architecture figure.
<!-- /architecture-figure:24 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**Qwen3.5** is a natively multimodal decoder family rather than a separate text model with a later VL edition. Its flagship 397B-A17B checkpoint uses sparse Mixture-of-Experts routing, activating about 17B parameters per token, and combines **Gated DeltaNet** linear-attention layers with standard softmax-attention layers. Visual inputs are handled inside the same model interface as text, supporting image and video reasoning, tool use, coding, and long-context agent workflows. Smaller dense and MoE variants extend the design across deployment scales.

The training pipeline combines large-scale multimodal pretraining with supervised fine-tuning and reinforcement learning. Qwen describes a scalable asynchronous RL system spanning text, multimodal, and multi-turn interaction, enabling a single checkpoint to switch between thinking and non-thinking behavior. The data mixture covers natural language, code, mathematics, images, video, documents, GUI interactions, tool calls, and multi-turn agent trajectories; the full source-level corpus is not publicly enumerated.

**Qwen3.6** is best treated as a continuation of this architecture rather than a separate VLM family. Its open dense and sparse checkpoints retain native multimodality and unified thinking and non-thinking modes while prioritizing stability and agentic coding. Folding these releases into the Qwen3.5 entry keeps the catalog focused on architectural changes rather than model-version churn.

</details>

### **Youtu-VL: Unified Autoregressive Supervision for Dense Vision**

Youtu-VL extends the language vocabulary with learned visual codes, making visual tokens prediction targets so one autoregressive model can emit segmentation, depth, pose, and detection without task-specific heads.

[![arXiv](https://img.shields.io/badge/arXiv-2601.19798-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2601.19798) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/TencentCloudADP/youtu-vl) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/tencent/Youtu-VL-4B-Instruct)

Tencent Youtu Lab<br>
**Released:** 2026-01-27

<!-- architecture-figure:25 -->
<p align="center">
  <img src="assets/architectures/youtu-vl-2026-arch.png" alt="Youtu-VL: Unified Autoregressive Supervision for Dense Vision architecture: Unified visual-text autoregressive supervision and dense-output decoding" width="820">
</p>
<p align="center"><sub><b>Figure 3.</b> Unified visual-text autoregressive supervision and dense-output decoding. <a href="https://arxiv.org/abs/2601.19798">Source paper</a>, PDF p. 3. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:25 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**Vision-Language Unified Autoregressive Supervision** learns a visual codebook whose symbols expand the text vocabulary into one multimodal vocabulary. Visual tokens are not passive conditioning embeddings: the decoder predicts them alongside text through joint visual-token and text reconstruction.

Because dense outputs are serialized in the same vocabulary, a standard autoregressive VLM can produce segmentation, monocular depth, human pose, and object detections without separate heads. This turns dense perception into native generation while retaining ordinary visual question answering and instruction following.

</details>

### **Kimi K2.5 and K2.6: Native Multimodal Agentic MoE**

Kimi K2.5 is a trillion-parameter native multimodal MoE for reasoning, coding, and computer use; K2.6 keeps the topology while extending context and agentic post-training.

[![arXiv](https://img.shields.io/badge/arXiv-2602.02276-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2602.02276) [![HuggingFace](https://img.shields.io/badge/HuggingFace-K2.6-blue?style=flat-square)](https://huggingface.co/moonshotai/Kimi-K2.6) [![Release](https://img.shields.io/badge/Official-K2.6-blue?style=flat-square)](https://www.kimi.com/blog/kimi-k2-6)

Kimi Team, Moonshot AI<br>
**Released:** 2026-01-27

<!-- architecture-figure:26 -->
<p align="center">
  <img src="assets/architectures/kimi-k2-5-and-k2-6-2026-arch.png" alt="Kimi K2.5 and K2.6: Native Multimodal Agentic MoE architecture: Agentic reinforcement-learning environments, rollout management, and training services" width="820">
</p>
<p align="center"><sub><b>Figure 10.</b> Agentic reinforcement-learning environments, rollout management, and training services. <a href="https://arxiv.org/abs/2602.02276">Source paper</a>, PDF p. 23. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:26 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**Kimi K2.5** connects MoonViT to a 1T-total, 32B-active decoder with 61 layers, Multi-head Latent Attention, and 384 routed experts. Eight routed experts plus shared capacity activate per token. Native multimodal training supports images, video, reasoning, code, tools, and GUI interaction within the same model.

Released April 20, **Kimi K2.6** retains the K2.5 architecture while extending context to 256K and strengthening coding, research, and multimodal-agent post-training. It is folded here rather than receiving a duplicate timeline row; Kimi K3 is separate because its attention, residual, sparsity, scale, and vision stack change materially.

</details>

### **Step3-VL-10B: Language-Aligned Perception with 16× Token Compression**

Step3-VL-10B combines a 1.8B language-aligned perception encoder with a Qwen3-8B decoder and aggressively compresses high-resolution visual features before language reasoning.

[![arXiv](https://img.shields.io/badge/arXiv-2601.09668-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2601.09668) [![Project](https://img.shields.io/badge/Project-Step3--VL--10B-blue?style=flat-square)](https://stepfun-ai.github.io/Step3-VL-10B/)

StepFun<br>
**Released:** 2026-01-14

<!-- architecture-figure:27 -->
> **Architecture figure:** The Step3-VL-10B report contains performance and RL figures, but no architecture diagram.
<!-- /architecture-figure:27 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**Step3-VL-10B** is architecturally distinct from the much larger 2025 Step3 sparse-MoE system. Its 1.8B perception encoder is aligned to language during pretraining, then a projector with two stride-2 stages reduces the spatial sequence by 16× before feeding a Qwen3-8B decoder.

Images combine one 728×728 global view with 504×504 local crops, treated as independent batch items. Explicit newline tokens mark patch rows while standard one-dimensional RoPE is retained. The PaCoRe parallel proposer-and-synthesizer reasoning method is a post-training and inference addition rather than the defining visual architecture.

</details>

### **ERNIE 5.0: Unified Autoregressive Omnimodal Mixture of Experts**

ERNIE 5.0 unifies text, image, video, and audio understanding and generation in a 2.4T ultra-sparse MoE trained through modality-specific forms of grouped next-token prediction.

[![arXiv](https://img.shields.io/badge/arXiv-2602.04705-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2602.04705) [![Architecture](https://img.shields.io/badge/Official-Architecture-blue?style=flat-square)](https://ernie.baidu.com/blog/posts/ernie5.0/)

Baidu ERNIE Team<br>
**Released:** 2025-11-13

<!-- architecture-figure:28 -->
<p align="center">
  <img src="assets/architectures/ernie-5-0-2026-arch.png" alt="ERNIE 5.0: Unified Autoregressive Omnimodal Mixture of Experts architecture: Unified image understanding, image generation, and video generation objectives" width="820">
</p>
<p align="center"><sub><b>Figure 2.</b> Unified image understanding, image generation, and video generation objectives. <a href="https://arxiv.org/abs/2602.04705">Source paper</a>, PDF p. 6. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:28 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**ERNIE 5.0** maps language, images, video, and audio into one autoregressive framework using Next-Group-of-Tokens Prediction. Text uses next-token and multi-token prediction; visual generation predicts the next frame and scale; audio generation predicts codec tokens depth-wise. Modality-agnostic expert routing activates less than 3% of the 2.4T-parameter network.

Elastic depth, width, and top-k sparsity train a super-network from which smaller deployment configurations can be extracted. Baidu first unveiled ERNIE 5.0 at Baidu World on November 13, 2025, formally released it in January 2026, and published the technical report on February 4; the timeline therefore uses the earliest documented public disclosure.

</details>

### **DeepSeek-OCR: Visual Context Compression through DeepEncoder**

DeepSeek-OCR treats document vision as a context-compression mechanism, representing thousands of text tokens with a much smaller sequence of visual tokens before decoding them with a sparse language model.

[![arXiv](https://img.shields.io/badge/arXiv-2510.18234-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2510.18234) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/deepseek-ai/DeepSeek-OCR) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/deepseek-ai/DeepSeek-OCR)

DeepSeek-AI<br>
**Released:** 2025-10-20

<!-- architecture-figure:29 -->
<p align="center">
  <img src="assets/architectures/deepseek-ocr-2025-arch.png" alt="DeepSeek-OCR: Visual Context Compression through DeepEncoder architecture: A SAM-CLIP DeepEncoder connected to a sparse language decoder" width="820">
</p>
<p align="center"><sub><b>Figure 3.</b> A SAM-CLIP DeepEncoder connected to a sparse language decoder. <a href="https://arxiv.org/abs/2510.18234">Source paper</a>, PDF p. 5. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:29 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**DeepSeek-OCR** consists of **DeepEncoder** and a DeepSeek-3B-MoE decoder with roughly 570M active parameters. DeepEncoder combines a SAM-derived local-perception pathway, a CLIP-derived semantic pathway, convolutional compression, and windowed and global attention to turn high-resolution pages into as few as 64 to 800 visual tokens. Multiple resolution modes trade recognition fidelity for compression.

Training first develops the encoder's visual-text representation and then jointly optimizes document decoding with the MoE language model. Data covers multilingual text pages, natural images, formulas, tables, charts, diagrams, and structured document conversion, supplemented with synthetic renderings. The work frames OCR as an experiment in optical compression for future long-context memory, rather than only a document benchmark model.

**DeepSeek-OCR 2**, released January 27, 2026, replaces the fixed raster-scan assumption with **DeepEncoder V2** and Visual Causal Flow. The encoder dynamically reorders visual tokens according to document semantics before language decoding, exploring whether cascaded one-dimensional causal reasoning can better represent complex two-dimensional layouts. [Paper](https://arxiv.org/abs/2601.20552) · [Repository](https://github.com/deepseek-ai/DeepSeek-OCR-2)

</details>

### **PaddleOCR-VL: Ultra-Compact Multilingual Document Parsing**

PaddleOCR-VL combines a NaViT-style dynamic-resolution encoder with ERNIE-4.5-0.3B to parse multilingual documents using only 0.9B parameters.

[![arXiv](https://img.shields.io/badge/arXiv-2510.14528-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2510.14528) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/PaddlePaddle/PaddleOCR) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/PaddlePaddle/PaddleOCR-VL)

PaddleOCR Team, Baidu<br>
**Released:** 2025-10-16

<!-- architecture-figure:30 -->
<p align="center">
  <img src="assets/architectures/paddleocr-vl-2025-arch.png" alt="PaddleOCR-VL: Ultra-Compact Multilingual Document Parsing architecture: Document layout analysis, compact VLM inference, instructions, and structured output" width="820">
</p>
<p align="center"><sub><b>Figure 2.</b> Document layout analysis, compact VLM inference, instructions, and structured output. <a href="https://arxiv.org/abs/2510.14528">Source paper</a>, PDF p. 5. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:30 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**PaddleOCR-VL-0.9B** connects a NaViT-style dynamic-resolution visual encoder to the compact ERNIE-4.5-0.3B language model. Variable-resolution packing preserves page detail and aspect ratio without forcing every document through a fixed square canvas. The decoder emits text and structured representations for paragraphs, tables, formulas, charts, and other document elements across 109 languages.

Its curriculum combines element-level recognition with page-level document parsing, followed by instruction tuning on complex layouts and structured outputs. Training data includes multilingual OCR, synthetic and scanned documents, tables, mathematical expressions, charts, reading-order annotations, and layout-rich pages. **PaddleOCR-VL-1.5** (January 2026) adds robust physical-document distortions, seal recognition, and text spotting; **1.6** (June 2026) adds region-aware data optimization and progressive reinforcement-learning post-training without changing the core architecture.

</details>

### **Qwen3-VL: DeepStack Vision-Language Models**

Qwen3-VL expands the Qwen vision-language family with dense and sparse-MoE checkpoints, native long multimodal context, and stronger spatial, video, OCR, visual-agent, and visual-coding capabilities.

[![arXiv](https://img.shields.io/badge/arXiv-2511.21631-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2511.21631) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/QwenLM/Qwen3-VL) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Models-blue?style=flat-square)](https://huggingface.co/collections/Qwen/qwen3-vl)

Qwen Team<br>
**Released:** 2025-09-22

<!-- architecture-figure:31 -->
<p align="center">
  <img src="assets/architectures/qwen3-vl-2025-arch.png" alt="Qwen3-VL: DeepStack Vision-Language Models architecture: Vision encoding, DeepStack injection, and dense or mixture-of-experts decoding" width="820">
</p>
<p align="center"><sub><b>Figure 1.</b> Vision encoding, DeepStack injection, and dense or mixture-of-experts decoding. <a href="https://arxiv.org/abs/2511.21631">Source paper</a>, PDF p. 3. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:31 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**Qwen3-VL** combines a native-dynamic-resolution Vision Transformer with Qwen3 language backbones in dense 2B, 4B, 8B, and 32B configurations and sparse 30B-A3B and 235B-A22B Mixture-of-Experts configurations. Its **DeepStack** mechanism injects features from multiple ViT depths into corresponding language-model layers instead of relying only on the visual encoder's final layer. **Interleaved-MRoPE** distributes temporal, height, and width position information across rotary-embedding frequencies, while explicit text-timestamp alignment improves event localization in video. The family supports interleaved text, images, and video in a native 256K-token context, with documented extrapolation for longer contexts.

Training proceeds through large-scale multimodal pretraining followed by supervised instruction tuning and reasoning-oriented post-training. The released Instruct checkpoints target direct response and agent interaction, whereas Thinking checkpoints generate extended reasoning for visual mathematics, spatial analysis, and other difficult multimodal tasks. The curriculum emphasizes recognition, multilingual OCR, document structure, 2D and 3D grounding, long-video understanding, GUI operation, and code generation from visual inputs.

The technical report describes a broad mixture of text, image-text, document, OCR, grounding, chart, multi-image, video, and agent-interaction data. Qwen does not publish a reproducible itemized list of every pretraining source, so individual benchmark datasets should not be presented as the complete training corpus.

</details>

### **Step3: Model-System Co-Design for Cost-Effective Multimodal Intelligence**

Step3 is a 321B-total, 38B-active multimodal MoE whose architecture and serving system are co-designed to reduce the communication cost of sparse expert decoding.

[![arXiv](https://img.shields.io/badge/arXiv-2507.19427-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2507.19427) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/stepfun-ai/Step3) [![Website](https://img.shields.io/badge/Website-Step3-blue?style=flat-square)](https://chat.stepfun.com/research/en/step3)

StepFun<br>
**Released:** 2025-07-25

<!-- architecture-figure:32 -->
<p align="center">
  <img src="assets/architectures/step3-2025-arch.png" alt="Step3: Model-System Co-Design for Cost-Effective Multimodal Intelligence architecture: Attention-FFN disaggregation across attention and expert instances" width="820">
</p>
<p align="center"><sub><b>Figure 6.</b> Attention-FFN disaggregation across attention and expert instances. <a href="https://arxiv.org/abs/2507.19427">Source paper</a>, PDF p. 11. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:32 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**Step3** uses a 321B-parameter sparse-MoE decoder with approximately 38B parameters active per token. The language stack contains dense lower layers followed by routed expert layers, while its vision pathway supports images and video for multimodal reasoning. The model is designed together with an **Attention-FFN Disaggregation** serving architecture, separating attention and expert computation so hardware placement and communication topology match their different workloads.

Training combines large-scale text and multimodal pretraining with instruction tuning and reasoning-oriented reinforcement learning. The data mixture spans language, code, mathematics, image-text, OCR, documents, charts, multi-image, video, and multimodal reasoning. The system report discloses architecture and deployment mechanisms more clearly than the source-level training corpus, which remains categorically described.

</details>

### **GLM-4.1V-Thinking: General-Purpose Multimodal Reasoning through Curriculum-Sampled RL**

GLM-4.1V-9B-Thinking combines a native-resolution AIMv2-based vision stack with long-chain-of-thought post-training and Reinforcement Learning with Curriculum Sampling to strengthen reasoning across visual, document, video, grounding, and agent tasks.

[![arXiv](https://img.shields.io/badge/arXiv-2507.01006-b31b1b.svg?style=flat-square)](https://arxiv.org/abs/2507.01006) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/zai-org/GLM-V) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Model-blue?style=flat-square)](https://huggingface.co/zai-org/GLM-4.1V-9B-Thinking)

GLM-V Team, Zhipu AI and Tsinghua University<br>
**Released:** 2025-07-01

<!-- architecture-figure:33 -->
<p align="center">
  <img src="assets/architectures/glm-4-1v-thinking-2025-arch.png" alt="GLM-4.1V-Thinking: General-Purpose Multimodal Reasoning through Curriculum-Sampled RL architecture: Native-resolution vision encoding, projection, decoding, and timestamped video tokens" width="820">
</p>
<p align="center"><sub><b>Figure 2.</b> Native-resolution vision encoding, projection, decoding, and timestamped video tokens. <a href="https://arxiv.org/abs/2507.01006">Source paper</a>, PDF p. 4. <a href="assets/architectures/FIGURE_NOTICE.md">Figure notice</a>.</sub></p>
<!-- /architecture-figure:33 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**GLM-4.1V-9B-Thinking** joins an AIMv2-Huge-initialized vision encoder, an MLP projector, and the GLM-4-9B-0414 language decoder. The vision tower replaces two-dimensional patch convolutions with 3D convolutions, temporally downsampling video while duplicating single images for consistent processing. Interpolated absolute position embeddings and 2D RoPE support native resolutions and extreme aspect ratios; the language decoder applies 3D RoPE to multimodal tokens. Explicit timestamp tokens after video frames supply temporal position and distance cues.

Training begins with broad multimodal pretraining, followed by continual training on video, higher-resolution imagery, and sequences up to 32K tokens. Supervised fine-tuning then teaches a standardized long-reasoning format with separate `<think>` and `<answer>` spans. The final stage introduces **Reinforcement Learning with Curriculum Sampling (RLCS)**. Rather than sampling a fixed task mixture, RLCS estimates changing model competence and prioritizes informative problems of suitable difficulty. Domain-specific rule, model, and hybrid rewards cover both verifiable and open-ended tasks.

Pretraining draws on curated caption pairs, knowledge-rich web and academic-book interleaving, 220M OCR images, natural-image and GUI grounding, instructional video, and text replay. SFT and RL span STEM reasoning, charts, documents, video, grounding, coding, GUI agents, and general visual instruction following. The later GLM-4.5V and GLM-4.6V families scale and extend this framework; they are successors, not separate architectures in this catalog.

</details>

### **ERNIE 4.5-VL: Heterogeneous Modality Mixture-of-Experts**

ERNIE 4.5-VL combines shared and modality-specific experts with isolated routing and balancing losses so visual learning can reinforce rather than degrade language capability.

[![Website](https://img.shields.io/badge/Report-ERNIE_4.5-blue?style=flat-square)](https://ernie.baidu.com/blog/posts/ernie4.5/) [![GitHub](https://badges.aleen42.com/src/github.svg)](https://github.com/PaddlePaddle/ERNIE) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Models-blue?style=flat-square)](https://huggingface.co/collections/baidu/ernie-45)

Baidu ERNIE Team<br>
**Released:** 2025-06-30

<!-- architecture-figure:34 -->
> **Architecture figure:** ERNIE 4.5-VL has no public paper containing an extractable architecture figure.
<!-- /architecture-figure:34 -->

<details>
<summary>ℹ️ <i>More Information</i></summary>

**ERNIE 4.5-VL** includes 424B-total/47B-active and 28B-total/3B-active multimodal MoE models, plus dense members of the broader ERNIE 4.5 family. Its **heterogeneous modality MoE** shares some experts across text and visual tokens while reserving other experts for individual modalities. Modality-isolated routing, router orthogonality loss, and multimodal token-balancing loss reduce competition between modalities.

The models are jointly pretrained on text, images, and video, then post-trained in both direct-response and thinking modes. PaddlePaddle infrastructure uses heterogeneous hybrid parallelism, hierarchical load balancing, FP8 mixed precision, and fine-grained recomputation to train and serve the sparse models efficiently. Baidu describes broa