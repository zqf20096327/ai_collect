# Awesome-LLM-Research-Collections

> Language: English | [中文](README.zh-CN.md)

> A Tool Recommend for read paper faster: [幻觉翻译](https://hjfy.top/)

# Contents

- [Attention](#attention)
  - [Attention Architecture](#attention-architecture)
- [LLMs](#llms)
  - [Foundation Models](#foundation-models)
  - [Inference](#inference)
  - [Interpretability](#interpretability)
  - [Detection](#detection)
- [Multimodal LLMs](#multimodal-llms)
  - [Video Generation](#video-generation)
  - [Vision-Language](#vision-language)
  - [Multimodal Reasoning](#multimodal-reasoning)
  - [VLA](#vla)
- [Embeddings](#embeddings)
- [Structured Data](#structured-data)
- [SFT](#sft)
  - [SFT Methods](#sft-methods)
- [Training](#training)
  - [Data Preparation](#data-preparation)
  - [Optimization](#optimization)
  - [Distillation](#distillation)
- [Reinforcement Learning](#reinforcement-learning)
  - [Policy Optimization](#policy-optimization)
  - [OPD](#opd)
  - [Reward Modeling](#reward-modeling)
  - [Video Generation RL](#video-generation-rl)
  - [Multimodal RL](#multimodal-rl)
  - [Reasoning RL](#reasoning-rl)
  - [Agentic RL](#agentic-rl)
  - [VLA RL](#vla-rl)
- [Agents Application](#agents-application)
  - [Computer Use](#computer-use)
  - [Tool Use](#tool-use)
  - [Web Agents](#web-agents)
  - [Data Agents](#data-agents)
  - [AI Research](#ai-research)
  - [Agent Skills](#agent-skills)
  - [Agent Development](#agent-development)
  - [Agent Evaluation](#agent-evaluation)
  - [Memory](#memory)
- [Vision](#vision)
  - [Object Detection](#object-detection)
  - [OCR](#ocr)
  - [Semantic Correspondence](#semantic-correspondence)
- [Auto-Prompt](#auto-prompt)
  - [Prompt Optimization](#prompt-optimization)
  - [Judge Prompting](#judge-prompting)
- [Notes](#notes)
  - [Paper Readings](#paper-readings)
  - [Technical Reflections](#technical-reflections)
- [Blogs](#blogs)

# Attention

## Attention Architecture

- **FlashMemory-DeepSeek-V4: Lightning Index Ultra-Long Context via Lookahead Sparse Attention** (2026.06) \
  **Description**: This paper proposes Lookahead Sparse Attention, which uses a separately trained neural memory indexer to predict future context needs and retain only query-critical KV chunks on GPU. FlashMemory reduces the physical KV cache footprint to 13.5% of full-context attention on average while preserving or slightly improving long-context accuracy. \
  <a href="https://arxiv.org/abs/2606.09079"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/libertywing/FlashMemory-Deepseek-V4"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/libertywing/FlashMemory-Deepseek-V4"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **MiniMax Sparse Attention** (2026.06) \
  **Description**: This paper introduces MiniMax Sparse Attention, a blockwise sparse attention mechanism built on GQA that uses a lightweight Index Branch to select group-specific Top-k KV blocks before exact sparse attention. Co-designed GPU kernels turn the sparsity into large practical speedups at million-token context while maintaining performance close to dense GQA. \
  <a href="https://arxiv.org/abs/2606.13392"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/MiniMax-AI/MSA"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/MiniMaxAI/MiniMax-M3"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **GQLA: Group-Query Latent Attention for Hardware-Adaptive Large Language Model Decoding** (2026.05) \
  **Description**: This paper proposes Group-Query Latent Attention, a minimal MLA modification that exposes both MQA-absorb and GQA decoding paths from the same trained weights. The runtime can select the path that matches target hardware without retraining or custom kernels, enabling H100-style compressed decoding, H20-oriented GQA plus MTP, and up to 8-way zero-redundancy tensor parallelism. \
  <a href="https://arxiv.org/abs/2605.15250"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/MuLabPKU/TransArch/tree/main/GQLA_preprint"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

- **Attention Residuals** (2026.03) \
  **Description**: This work replaces fixed residual accumulation with attention over previous layer outputs, enabling input-dependent depth-wise aggregation and reducing PreNorm-induced representation dilution. It also introduces Block AttnRes for scalable training with lower memory and communication overhead. \
  <a href="https://arxiv.org/abs/2603.15031"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/MoonshotAI/Attention-Residuals"><img src="assets/icons/project.svg" alt="Project" width="20"></a>

- **Kimi Linear: An Expressive, Efficient Attention Architecture** (2025.10) \
  **Description**: This paper introduces Kimi Linear, a hybrid architecture whose Kimi Delta Attention module combines fine-grained gating with an efficient chunkwise algorithm based on specialized diagonal-plus-low-rank transitions. A 48B-parameter model with 3B activated parameters outperforms full MLA under the same training recipe while reducing KV cache usage by up to 75% and delivering up to 6× decoding throughput at a 1M-token context. \
  <a href="https://arxiv.org/abs/2510.26692"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/MoonshotAI/Kimi-Linear"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/collections/moonshotai/kimi-linear-a3b"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **RoFormer: Enhanced Transformer with Rotary Position Embedding** (2021.04) \
  **Description**: This paper introduces Rotary Position Embedding (RoPE), which encodes absolute positions through rotations while making self-attention explicitly depend on relative positions. RoPE supports flexible sequence lengths, distance-aware dependency decay, and relative position encoding for linear self-attention. \
  <a href="https://arxiv.org/abs/2104.09864"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/ZhuiyiTechnology/roformer"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/junnyu/roformer_chinese_base"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **Fast Transformer Decoding: One Write-Head is All You Need** (2019.11) \
  **Description**: This paper introduces multi-query attention, sharing keys and values across attention heads to reduce the memory-bandwidth cost of incremental Transformer decoding. The variant speeds up decoding substantially while incurring only minor quality degradation relative to multi-head attention baselines. \
  <a href="https://arxiv.org/abs/1911.02150"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

# LLMs

## Foundation Models

- **BDH-CQ: In-Context Learning with Recurrent Latent Reasoning** (2026.08) \
  **Description**: BDH-CQ combines in-context learning through continuously updated recurrent memory with iterative reasoning in a high-dimensional latent space, without verbalizing intermediate reasoning. On ARC-AGI-1, its 150M-parameter configuration attains 29.5% pass@2 at a computed cost of $0.0007 per task, improving the reported cost-accuracy frontier. \
  <a href="https://arxiv.org/abs/2608.09888"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/pathwaycom/arc-task-gen"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

- **On the Design of Qwen3.8-Next Architecture: Evaluation, Efficiency, and Training Stability** (2026.08) \
  **Description**: Qwen3.8-Flash-Next combines hybrid Gated DeltaNet and sparse attention, gated residual branches, and host-memory n-gram embeddings in a 125B-parameter MoE backbone with 6B parameters activated per token. Joint architecture and Muon optimizer ablations examine downstream quality, training and inference costs, and stability, yielding competitive pretraining performance at roughly one-ninth the predecessor's training FLOPs. \
  <a href="https://arxiv.org/abs/2608.30320"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://qwen.ai/blog?id=qwen3.8-flash-next"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/QwenLM/Qwen3.8-Flash-Next"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/Qwen/Qwen3.8-Flash-Next"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **Kimi K3: Open Frontier Intelligence** (2026.07) \
  **Description**: Kimi K3 is a 2.8T-parameter MoE foundation model with 104B activated parameters, native vision, and a 1-million-token context window, built on Kimi Delta Attention, Attention Residuals, and Stable LatentMoE. These architectural and training advances improve overall scaling efficiency by about 2.5× over Kimi K2 and support frontier-level long-horizon coding, agentic, reasoning, and vision performance. \
  <a href="https://arxiv.org/abs/2607.24653"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://www.kimi.com/blog/kimi-k3"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/MoonshotAI/Kimi-K3"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/moonshotai/Kimi-K3"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **The MiniMax-M2 Series: Mini Activations Unleashing Max Real-World Intelligence** (2026.05) \
  **Description**: This technical report presents the MiniMax-M2 series, MoE language models with a small active-parameter footprint designed for real-world agentic deployment. It combines agent-driven verifiable data pipelines, the Forge agent-native RL system, and early self-evolution in M2.7 to improve coding, deep-search, office-task, and reasoning performance. \
  <a href="https://arxiv.org/abs/2605.26494"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://www.minimax.io/blog/minimax-m27"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/MiniMax-AI/MiniMax-M2.7"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/MiniMaxAI/MiniMax-M2.7"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **The Latent Space: Foundation, Evolution, Mechanism, Ability, and Outlook** (2026.04) \
  **Description**: This survey argues that continuous latent space is becoming a native computational substrate for language-based models, addressing the inefficiencies of explicit token-level generation such as redundancy, discretization bottlenecks, and semantic loss. It further organizes the field through mechanism and ability perspectives, and outlines key open challenges for future research. \
  <a href="https://arxiv.org/abs/2604.02029"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/YU-deep/Awesome-Latent-Space"><img src="assets/icons/project.svg" alt="Project" width="20"></a>

- **DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence** (2026.04) \
  **Description**: DeepSeek-V4 introduces 1.6T-parameter Pro and 284B-parameter Flash MoE language models, both supporting one-million-token contexts. Its hybrid Compressed Sparse Attention and Heavily Compressed Attention, Manifold-Constrained Hyper-Connections, and Muon optimizer improve long-context efficiency, with Pro using 27% of DeepSeek-V3.2's single-token inference FLOPs and 10% of its KV cache in the one-million-token setting. \
  <a href="https://arxiv.org/abs/2606.19348"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://deepseek.com/en/news/v4-preview/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://huggingface.co/collections/deepseek-ai/deepseek-v4"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **GLM-5: from Vibe Coding to Agentic Engineering** (2026.02) \
  **Description**: GLM-5 is a next-generation foundation model targeting long-horizon agentic engineering, with reduced training and inference cost and preserved long-context capability. It introduces asynchronous RL infrastructure and agent RL algorithms to improve post-training efficiency and real-world coding performance. \
  <a href="https://arxiv.org/abs/2602.15763"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://z.ai/blog/glm-5"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/zai-org/GLM-5"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/zai-org/GLM-5"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **Kimi K2.5: Visual Agentic Intelligence** (2026.02) \
  **Description**: This paper introduces an open-source multimodal agentic model that jointly optimizes text and vision through unified pretraining, SFT, and reinforcement learning. It also proposes Agent Swarm, a parallel orchestration framework for decomposing and executing complex tasks with coordinated agents. \
  <a href="https://arxiv.org/abs/2602.02276"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://www.kimi.com/ai-models/kimi-k2-5"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/MoonshotAI/Kimi-K2.5"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/moonshotai/Kimi-K2.5"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **MiMo-V2-Flash Technical Report** (2026.01) \
  **Description**: MiMo-V2-Flash is a 309B-parameter MoE foundation model with 15B active parameters, built for fast reasoning, coding, and agentic workloads through hybrid sliding-window/global attention, 27T-token pretraining, and long-context extension to 256k. It introduces Multi-Teacher On-Policy Distillation for scalable post-training and repurposes multi-token prediction as a draft model for speculative decoding speedups. \
  <a href="https://arxiv.org/abs/2601.02780"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/xiaomimimo/MiMo-V2-Flash"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/XiaomiMiMo/MiMo-V2-Flash"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models** (2026.01) \
  **Description**: This paper introduces conditional memory as a sparsity axis complementary to MoE, instantiated by Engram for constant-time lookup of static knowledge. A scaling law guides the allocation between neural computation and memory, enabling Engram models to improve knowledge, reasoning, code, math, and long-context retrieval at matched parameters and FLOPs. \
  <a href="https://arxiv.org/abs/2601.07372"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/deepseek-ai/Engram"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

- **DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models** (2025.12) \
  **Description**: DeepSeek-V3.2 is an open large language model that combines efficient long-context computation with strong reasoning and agent performance. Its key ingredients include DeepSeek Sparse Attention, scalable RL post-training, and a large-scale agentic task synthesis pipeline for improving tool-use generalization and instruction-following robustness. \
  <a href="https://arxiv.org/abs/2512.02556"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://api-docs.deepseek.com/news/news251201"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://huggingface.co/deepseek-ai/DeepSeek-V3.2"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **GLM-4.5: Agentic, Reasoning, and Coding (ARC) Foundation Models** (2025.08) \
  **Description**: GLM-4.5 introduces an open-source MoE foundation model with hybrid reasoning modes (thinking/direct response) to better support agentic, reasoning, and coding tasks. It combines large-scale pretraining and RL-based post-training, and releases both full and compact variants with strong benchmark performance. \
  <a href="https://arxiv.org/abs/2508.06471"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/zai-org/GLM-4.5"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/zai-org/GLM-4.5"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **Kimi K2: Open Agentic Intelligence** (2025.07) \
  **Description**: Kimi K2 presents a trillion-parameter MoE language model focused on strong agentic, reasoning, and coding capabilities with stable large-scale training. The work introduces MuonClip with QK-clip to improve optimization stability and token efficiency during pretraining. \
  <a href="https://arxiv.org/abs/2507.20534"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://moonshotai.github.io/Kimi-K2/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/MoonshotAI/Kimi-K2"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/moonshotai/Kimi-K2-Base"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **Qwen3 Technical Report** (2025.05) \
  **Description**: This report presents the Qwen3 family spanning dense and MoE models across a wide parameter range, emphasizing stronger multilingual performance and efficiency. It unifies deliberative thinking and fast response modes in one framework and scales post-training to improve reasoning, coding, and agentic behavior. \
  <a href="https://arxiv.org/abs/2505.09388"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://qwen.ai/blog?id=qwen3"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/QwenLM/Qwen3"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/collections/Qwen/qwen3"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **MiniMax-01: Scaling Foundation Models with Lightning Attention** (2025.01) \
  **Description**: MiniMax-01 introduces a long-context model family built around Lightning Attention and MoE to improve scaling efficiency and practical throughput. It combines optimized parallelization and communication-computation overlap to train large models with stronger long-context performance. \
  <a href="https://arxiv.org/abs/2501.08313"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://www.minimax.io/news/minimax-01-series-2"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/MiniMax-AI/MiniMax-01"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/MiniMaxAI/MiniMax-Text-01"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **DeepSeek-V3 Technical Report** (2024.12) \
  **Description**: DeepSeek-V3 is a 671B-parameter MoE language model with 37B activated parameters per token, built for efficient inference and cost-effective large-scale training. It extends MLA and DeepSeekMoE with auxiliary-loss-free load balancing and a multi-token prediction objective, achieving strong open-model performance with stable 14.8T-token pretraining and SFT/RL post-training. \
  <a href="https://arxiv.org/abs/2412.19437"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/deepseek-ai/DeepSeek-V3"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/deepseek-ai/DeepSeek-V3"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **Qwen2.5-Math Technical Report: Toward Mathematical Expert Model via Self-Improvement** (2024.09) \
  **Description**: This paper presents Qwen2.5-Math, a family of math-specialized language models that applies self-improvement throughout pre-training, post-training, and inference. The approach strengthens mathematical reasoning and tool-augmented problem solving across multiple model sizes. \
  <a href="https://arxiv.org/abs/2409.12122"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/QwenLM/Qwen2.5-Math"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/collections/Qwen/qwen25-math-66f7162f2be749b8a8e63c8a"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **Qwen2 Technical Report** (2024.07) \
  **Description**: This report introduces the Qwen2 series of dense and mixture-of-experts language models, covering base and instruction-tuned variants across a broad parameter range. It emphasizes stronger multilingual, coding, math, and reasoning performance while remaining competitive with proprietary systems. \
  <a href="https://arxiv.org/abs/2407.10671"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/QwenLM/Qwen2"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/collections/Qwen/qwen2-6641dc1d5fbb1a48c8708a52"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model** (2024.05) \
  **Description**: DeepSeek-V2 is a 236B-parameter MoE language model with 21B activated parameters per token and 128K context length, designed for economical training and efficient inference. It combines Multi-head Latent Attention for KV-cache compression with DeepSeekMoE sparse computation, reducing training cost and KV cache while improving throughput and open-model performance. \
  <a href="https://arxiv.org/abs/2405.04434"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/deepseek-ai/DeepSeek-V2"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/deepseek-ai/DeepSeek-V2"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

## Inference

- **Thinking Inertia: LLMs Keep Thinking When Told Not To** (2026.10) \
  **Description**: This paper evaluates no-thinking behavior by separating visible pre-answer text from final answers and measuring answer-only compliance, question relevance, and explicit inference. Across six LLMs and six prompting interventions, explicit inference persists under no-thinking controls, becoming more prevalent as answer spaces open and exposing a compliance–accuracy trade-off on open-ended tasks. \
  <a href="https://arxiv.org/abs/2610.11765"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://thinking-inertia.github.io/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/thinking-inertia/code"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/datasets/thinking-inertia/llm-nothinking-trajectories"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **LLMRouter: Unified Infrastructure for Developing, Evaluating, and Deploying LLM Routers** (2026.08) \
  **Description**: LLMRouter formulates LLM routing as a sequential decision process spanning single-turn, multi-turn, and personalized settings, and provides modular infrastructure with an automated pipeline for joint quality-cost evaluation. Its xRouteBench benchmark covers five routing scenarios, while experiments across more than 16 representative routers show that learned routers achieve a 14.6% relative improvement over the strongest fixed-model baseline. \
  <a href="https://arxiv.org/abs/2608.06867"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://ulab-uiuc.github.io/LLMRouter/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/ulab-uiuc/LLMRouter"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/datasets/ulab-ai/xRouteBench"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses** (2026.08) \
  **Description**: This paper introduces strong-to-weak scaffolding, in which a stronger builder model constructs an inference-time harness that improves a weaker target model without updating its parameters. Across four Theory-of-Mind benchmarks, the harness nearly doubles average performance by offloading unstable reasoning to deterministic code, task-specific routing, and strict answer-format enforcement. \
  <a href="https://arxiv.org/abs/2608.12307"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **Large Language Models Explore by Latent Distilling** (2026.04) \
  **Description**: This paper proposes Exploratory Sampling (ESamp), a decoding method that addresses the shallow lexical variation of standard stochastic sampling by encouraging semantic exploration. It trains a lightweight Distiller at test time to predict deep-layer representations from shallow ones, then uses prediction error as a novelty signal to reweight candidate tokens and improve Pass@k efficiency. \
  <a href="https://arxiv.org/abs/2604.24927"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/LinesHogan/tLLM"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

- **Procedural Knowledge at Scale Improves Reasoning** (2026.04) \
  **Description**: Reasoning Memory decomposes existing reasoning trajectories into 32 million self-contained subquestion–subroutine pairs, then retrieves relevant subroutines within the model's reasoning trace as procedural priors. Across six math, science, and coding benchmarks, it outperforms document-, trajectory-, and template-based RAG as well as a compute-matched test-time scaling baseline. \
  <a href="https://arxiv.org/abs/2604.01348"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/facebookresearch/reasoning-memory"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

- **Caterpillar of Thoughts: The Optimal Test-Time Algorithm for Large Language Models** (2026.03) \
  **Description**: This paper presents a theoretical framework for optimal test-time computation in LLMs, proving that the optimal algorithm always generates a caterpillar tree structure, and introduces CaT which achieves better success rate than Tree-of-Thoughts with fewer token generations. \
  <a href="https://arxiv.org/abs/2603.22784"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **FinChain: A Symbolic Benchmark for Verifiable Chain-of-Thought Financial Reasoning** (2025.06) \
  **Description**: FinChain introduces a contamination-free benchmark for machine-verifiable multi-step financial reasoning, covering 58 topics across 12 domains through parameterized templates with executable Python traces. Its ChainEval metric jointly evaluates final-answer correctness and step-level reasoning consistency, revealing persistent weaknesses across 26 leading LLMs. \
  <a href="https://arxiv.org/abs/2506.02515"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://mbzuai-nlp.github.io/finchain/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/mbzuai-nlp/finchain"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/spaces/Usmansafder/finchain-space"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

## Interpretability

- **Your Transformer Can Hold Two Thoughts at Once: Evidence of Linear Superposition in LLMs** (2026.09) \
  **Description**: This paper presents evidence that mixing embeddings from distinct text streams preserves a superposition of their next-token distributions, a property that weakens during pretraining and can be restored through lightweight fine-tuning. It also introduces guided decoding to recover two coherent continuations from a single mixed forward pass. \
  <a href="https://arxiv.org/abs/2609.29845"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

## Detection

- **Base Models Look Human To AI Detectors** (2026.05) \
  **Description**: This paper finds that commercial AI-text detectors often label base-model outputs as more human than outputs from instruction-tuned counterparts, suggesting they track tuning artifacts and local context rather than invariant machine-text signals. It proposes Humanization by Iterative Paraphrasing (HIP), a detector-agnostic fine-tuning and iterative paraphrasing pipeline that improves semantic preservation while evading detectors. \
  <a href="https://arxiv.org/abs/2605.19516"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/YixuanEvenXu/humanization-by-iterative-paraphrasing"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

# Multimodal LLMs

## Video Generation

- **StreamEval: Evaluating Interactive Streaming Video Generation Models** (2026.10) \
  **Description**: StreamEval is a benchmark for interactive streaming video generation across avatar dialogue and performance, world generation, and video editing. Its 300 scripted cases span 15–300-second sessions and use ten metrics to assess task execution, state consistency, visual fidelity, and audio-visual coordination. \
  <a href="https://arxiv.org/abs/2610.28402"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://streameval.ai/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/StreamEval/StreamEval"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/datasets/StreamEval/StreamEval"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

## Vision-Language

- **WeVisOne-VL: Unified Visual Perception from Objects to Pixels** (2026.10) \
  **Description**: WeVisOne-VL unifies object-level and pixel-level visual perception in a vision-language model, supporting detection, localization, counting, pointing, OCR, segmentation, and matting through structured token prediction and a lightweight pixel decoder. Trained with staged supervised fine-tuning followed by mixed-task reinforcement learning, it reports leading results across more than 30 benchmarks. \
  <a href="https://arxiv.org/abs/2610.31329"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://tencent.github.io/WeVisOne-VL/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/Tencent/WeVisOne-VL"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/tencent/WeVisOne-VL-4B"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **OmniCompass: A Holistic Benchmark for Omni-Modal Video Grounding and Understanding** (2026.10) \
  **Description**: OmniCompass evaluates video understanding through visual and joint audio-visual tracks, combining temporal grounding, spatial grounding, and question answering under paired text-only and text+image target specifications. Evaluation of 50 MLLMs reveals persistent difficulties in precise grounding, audio-visual understanding, and consistency across target specifications. \
  <a href="https://arxiv.org/abs/2610.18829"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://omnicompass.netlify.app/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/PolyU-VCLab/OmniCompass"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/datasets/VCLab-PolyU/OmniCompass"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **MJev-Spatial: System One Spatial Intelligence via Native Attention Matching** (2026.10) \
  **Description**: MJev-Spatial unifies spatial choice, numerical prediction, and pointing as candidate classification, reusing pretrained query and key projections without adding parameters or generating answer tokens. Coarse-to-fine classification handles scalar and point outputs, while joint teacher-forced supervision and balanced batching improve training efficiency; the Qwen3.5-4B-based model outperforms its autoregressive base on all twelve evaluated benchmarks. \
  <a href="https://arxiv.org/abs/2610.22276"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/Fr0zenCrane/MJev-Spatial"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/mindlab-research/MJev-Spatial-4B"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **Intern-S2-Preview: Scientific Agentic Foundation Model** (2026.08) \
  **Description**: Intern-S2-Preview is a series of scientific agentic foundation models that combines multimodal scientific pre-training with unified supervised fine-tuning, multi-task and agentic reinforcement learning, and on-policy distillation for scientific understanding, reasoning, generation, and long-horizon tasks. Its 397B model adds time-series forecasting and a separate Memory Decoder path for rapid scientific specialization, achieving competitive or leading results across scientific, multimodal, agentic, and general-purpose benchmarks. \
  <a href="https://arxiv.org/abs/2608.13505"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/InternLM/Intern-S1"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/internlm/Intern-S2-Preview-397B"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **VideoChat3: Fully Open Video MLLM for Efficient and Generalist Video Understanding** (2026.07) \
  **Description**: VideoChat3 is a fully open 4B video-centric MLLM that combines I3D-ViT with adaptive frame resolution for efficient spatiotemporal and streaming perception. Its scalable data synthesis pipeline curates datasets for general, long-form, and streaming video, improving cross-domain generalization while reducing computation. \
  <a href="https://arxiv.org/abs/2607.14935"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://mcg-nju.github.io/VideoChat3/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/MCG-NJU/VideoChat3"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/collections/MCG-NJU/videochat3"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **Lance: Unified Multimodal Modeling by Multi-Task Synergy** (2026.05) \
  **Description**: Lance introduces a lightweight native unified multimodal model for image and video understanding, generation, and editing without relying mainly on capacity scaling. It combines shared interleaved context modeling, decoupled capability pathways, dual-stream MoE, modality-aware rotary positional encoding, and staged multi-task training to improve both generation and understanding. \
  <a href="https://arxiv.org/abs/2605.18678"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://lance-project.github.io/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/bytedance/Lance"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/bytedance-research/Lance"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **Video-MME-v2: Towards the Next Stage in Benchmarks for Comprehensive Video Understanding** (2026.04) \
  **Description**: This paper introduces Video-MME-v2, an improved video understanding benchmark addressing the saturation issue in existing benchmarks where inflated leaderboard scores fail to reflect real-world model capabilities. \
  <a href="https://arxiv.org/abs/2604.05015"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://video-mme-v2.netlify.app/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/MME-Benchmarks/Video-MME-v2"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/datasets/MME-Benchmarks/Video-MME-v2"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **V-Reflection: Transforming MLLMs from Passive Observers to Active Interrogators** (2026.04) \
  **Description**: V-Reflection converts MLLMs from passive visual consumers to active interrogators through a think-then-look reflection mechanism that grounds each reasoning step in visual evidence. A two-stage distillation design improves fine-grained perception while keeping inference fully autoregressive and efficient. \
  <a href="https://arxiv.org/abs/2604.03307"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://idea-research.github.io/V-Reflection/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/IDEA-Research/V-Reflection"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/garlandchou/V-Reflection"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **ThinkJEPA: Empowering Latent World Models with Large Vision-Language Reasoning Model** (2026.03) \
  **Description**: This paper proposes a VLM-guided JEPA-style latent world modeling framework that combines dense-frame dynamics prediction with long-horizon semantic guidance through a dual-temporal design. It further introduces a hierarchical pyramid representation extraction module to transfer multi-layer VLM reasoning features into latent forecasting for more robust hand-manipulation trajectory prediction. \
  <a href="https://arxiv.org/abs/2603.22281"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **Qwen3-VL Technical Report** (2025.11) \
  **Description**: We introduce Qwen3-VL, the most capable vision-language model in the Qwen series to date, achieving superior performance across a broad range of multimodal benchmarks. It natively supports interleaved contexts of up to 256K tokens, seamlessly integrating text, images, and video. \
  <a href="https://arxiv.org/abs/2511.21631"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://qwen.ai/blog?id=99f0335c4ad9ff6153e517418d48535ab6d8afef&from=research.latest-advancements-list"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/QwenLM/Qwen3-VL"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/collections/Qwen/qwen3-vl"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **InternVL3.5: Advancing Open-Source Multimodal Models in Versatility, Reasoning, and Efficiency** (2025.08) \
  **Description**: This paper introduces InternVL 3.5, a new family of open-source multimodal models that significantly advances versatility, reasoning capability, and inference efficiency, featuring the Cascade Reinforcement Learning framework. \
  <a href="https://arxiv.org/abs/2508.18265"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **Qwen2.5-VL Technical Report** (2025.02) \
  **Description**: This technical report introduces Qwen2.5-VL, a flagship vision-language model with stronger visual recognition, precise localization, robust document parsing, and long-video understanding. It also improves agentic interaction with visual environments through better grounding and structured perception capabilities. \
  <a href="https://arxiv.org/abs/2502.13923"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/QwenLM/Qwen2.5-VL"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/collections/Qwen/qwen25-vl-67ad1d2357b3028d1e9c4d56"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **InternVL 2.5: Expanding Performance Boundaries of Open-Source Multimodal Models with Model, Data, and Test-Time Scaling** (2024.12) \
  **Description**: This paper introduces InternVL 2.5, an advanced multimodal LLM series that was the first open-source MLLMs to surpass 70% on the MMMU benchmark, achieving a 3.7-point improvement through Chain-of-Thought reasoning. \
  <a href="https://arxiv.org/abs/2412.05271"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://huggingface.co/spaces/OpenGVLab/InternVL"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution** (2024.09) \
  **Description**: This paper introduces Qwen2-VL, a vision-language model series that uses Naive Dynamic Resolution to process images at arbitrary resolutions and M-RoPE to fuse text, image, and video positional information. Scaling the model to 2B, 8B, and 72B parameters with larger multimodal data yields competitive image, video, multilingual OCR, document understanding, and agentic visual interaction performance. \
  <a href="https://arxiv.org/abs/2409.12191"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://qwenlm.github.io/blog/qwen2-vl/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/QwenLM/Qwen2-VL"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/collections/Qwen/qwen2-vl"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **LLaVA-NeXT-Interleave: Tackling Multi-image, Video, and 3D in Large Multimodal Models** (2024.07) \
  **Description**: This paper introduces LLaVA-NeXT-Interleave, which simultaneously tackles Multi-image, Multi-frame (video), Multi-view (3D), and Multi-patch scenarios in large multimodal models, extending visual instruction tuning to multi-modal scenarios. \
  <a href="https://arxiv.org/abs/2407.07895"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://llava-vl.github.io/blog/2024-06-16-llava-next-interleave/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/LLaVA-VL/LLaVA-NeXT"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

- **How Good is my Video LMM? Complex Video Reasoning and Robustness Evaluation Suite for Video-LMMs** (2024.05) \
  **Description**: This paper introduces CVRR-ES, a benchmark that comprehensively assesses Video-LMMs across 11 diverse real-world video dimensions, evaluating 9 recent models and finding that most open-source Video-LMMs struggle with robustness and reasoning on complex videos. \
  <a href="https://arxiv.org/abs/2405.03690"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://mbzuai-oryx.github.io/CVRR-Evaluation-Suite/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>

- **Qwen-VL: A Versatile Vision-Language Model for Understanding, Localization, Text Reading, and Beyond** (2023.08) \
  **Description**: This paper introduces Qwen-VL, a vision-language model series built on Qwen-LM with a visual receptor, multimodal interface, three-stage training pipeline, and multilingual multimodal corpus. By aligning image-caption-box tuples, Qwen-VL supports visual understanding, grounding, and text reading while achieving strong results across visual-centric benchmarks. \
  <a href="https://arxiv.org/abs/2308.12966"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/QwenLM/Qwen-VL"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/Qwen/Qwen-VL"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **LLaVA: Visual Instruction Tuning** (2023.04) \
  **Description**: This paper presents LLaVA, a large multimodal model trained end-to-end on machine-generated instruction tuning data, showing impressive multimodal chat abilities and achieving state-of-the-art results on Science QA. \
  <a href="https://arxiv.org/abs/2304.08485"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://llava-vl.github.io/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>

## Multimodal Reasoning

- **Think Before You Link: Rarity, Reasoning, and Retrieval in Multilingual Entity Linking** (2026.09) \
  **Description**: This paper characterizes rare-entity failures in multilingual multimodal entity linking using 15 metrics spanning popularity, documentation, knowledge-graph structure, and cross-lingual coverage. It introduces a training-free vision-language framework that iteratively retrieves and reasons over Wikipedia evidence, improving accuracy overall and especially on rare-entity slices, and releases the MERLIN-Rare benchmark. \
  <a href="https://arxiv.org/abs/2609.10745"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://neulab.github.io/think-before-you-link/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/neulab/think-before-you-link"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/datasets/neulab/merlin-rare"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **Multimodal Chain-of-Thought Reasoning: A Comprehensive Survey** (2025.03) \
  **Description**: This survey addresses the lack of an up-to-date review of multimodal Chain-of-Thought reasoning in MLLMs across image, video, speech, audio, 3D, and structured data. It introduces foundational definitions, a comprehensive taxonomy, methodological analysis across applications, and open challenges for future multimodal reasoning research. \
  <a href="https://arxiv.org/abs/2503.12605"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/yaotingwangofficial/Awesome-MCoT"><img src="assets/icons/project.svg" alt="Project" width="20"></a>

## VLA

- **Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving** (2026.08) \
  **Description**: Qwen-Drive-1.0 integrates 3D perception, visual question answering, and motion planning around an unchanged pretrained vision-language model, using an external BEV perception head and a Planning Expert for future ego trajectories. A staged recipe combines driving supervision with general vision-language data, preserving broad visual understanding while achieving strong 3D scene and closed-loop planning performance. \
  <a href="https://arxiv.org/abs/2609.00111"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://qwen.ai/blog?id=qwen-drive-1.0"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/QwenLM/Qwen-Drive-1.0"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/Qwen/Qwen-Drive-1.0-4B"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **LA4VLA: Learning to Act without Seeing via Language-Action Pretraining** (2026.06) \
  **Description**: This paper proposes LA4VLA, a language-action pretraining framework that teaches VLA policies language-conditioned action priors without visual observations by decomposing demonstrations into atomic action segments with low-level descriptions. It builds the LA-33K dataset and shows that combining language-action and VLA supervision improves manipulation success in both simulation and real-world tasks. \
  <a href="https://arxiv.org/abs/2606.27295"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/MINT-SJTU/LA4VLA"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/datasets/MINT-SJTU/LA-33K"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **Xiaomi OneVL: One-Step Latent Reasoning and Planning with Vision-Language Explanation** (2026.04) \
  **Description**: OneVL addresses real-time trajectory planning in VLA-based autonomous driving by compressing Chain-of-Thought reasoning into compact latent tokens supervised by both language reconstruction and future-frame prediction. Its three-stage training pipeline yields latent reasoning that surpasses explicit CoT while keeping answer-only inference latency. \
  <a href="https://arxiv.org/abs/2604.18486"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://xiaomi-embodied-intelligence.github.io/OneVL/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/xiaomi-research/onevl"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/collections/xiaomi-research/onevl-models"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **CLAP: Contrastive Latent Action Pretraining for Learning Vision-Language-Action Models from Human Videos** (2026.01) \
  **Description**: CLAP learns an executable latent action vocabulary from robot trajectories and contrastively aligns human video transitions with it, enabling VLA pretraining on abundant unlabeled human videos. It combines an autoregressive VLA with a rectified-flow action head and knowledge-matching regularization for efficient control and target-domain adaptation. \
  <a href="https://arxiv.org/abs/2601.04061"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://lin-shan.com/CLAP/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/LinShan-Bin/OpenCLAP"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/collections/LinShan/clap"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

# Embeddings

- **Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models** (2025.06) \
  **Description**: This paper introduces Qwen3 Embedding, a family of text embedding and reranking models built on Qwen3 foundation models with a multi-stage training pipeline, model merging, and LLM-synthesized multilingual data. The series covers 0.6B, 4B, and 8B sizes and achieves state-of-the-art results across multilingual embedding, retrieval, reranking, code retrieval, and cross-lingual benchmarks. \
  <a href="https://arxiv.org/abs/2506.05176"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://qwenlm.github.io/blog/qwen3-embedding/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/QwenLM/Qwen3-Embedding"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/collections/Qwen/qwen3-embedding"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **CoQuIR: A Comprehensive Benchmark for Code Quality-Aware Information Retrieval** (2025.05) \
  **Description**: This paper introduces CoQuIR, the first large-scale multilingual benchmark for quality-aware code retrieval, with 42,725 queries and 134,907 snippets annotated for correctness, efficiency, security, and maintainability. Its two quality-centric metrics and evaluation of 23 retrievers expose major quality-awareness gaps, while contrastive training improves quality-aware retrieval without sacrificing semantic relevance. \
  <a href="https://arxiv.org/abs/2506.11066"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/TRUMANCFY/CoQuIR"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/CoQuIR"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

# Structured Data

- **LimiX-2: A Contextual Mechanism Network Towards General Structured-Data Intelligence** (2026.09) \
  **Description**: LimiX-2 uses Contextual Mechanism Networks and context-conditional masked modeling to learn the joint structure of tabular data from synthetic causal datasets. It improves prediction across three tabular benchmarks and its feature attention supports causal skeleton recovery. \
  <a href="https://arxiv.org/abs/2609.17488"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://www.limix.ai/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/limix-ldm-ai/LimiX"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/stable-ai/LimiX-2"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

# SFT

## SFT Methods

- **StudentSim: Training LLM-based Student Simulators** (2026.09) \
  **Description**: StudentSim turns sparse records for individual learners into personalized LLM simulators through pooled training followed by per-student specialization. StudentSimEval measures whether they match each learner's responses and react to tutor guidance across chess, English writing, and mathematics. \
  <a href="https://arxiv.org/abs/2609.01591"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://microsoft.github.io/StudentSim/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/microsoft/StudentSim"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

- **Data Difficulty and the Generalization--Extrapolation Tradeoff in LLM Fine-Tuning** (2026.05) \
  **Description**: This paper systematically studies difficulty-based data selection for supervised fine-tuning and shows that no single difficulty level is universally optimal. It explains the data-size-dependent optimum through a tradeoff between in-distribution generalization and extrapolation, with the best difficulty shifting toward harder examples as the data budget grows. \
  <a href="https://arxiv.org/abs/2605.12906"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **Rethinking Generalization in Reasoning SFT: A Conditional Analysis on Optimization, Data, and Model Capability** (2026.04) \
  **Description**: This paper challenges the common claim that supervised fine-tuning (SFT) only memorizes while RL generalizes, finding cross-domain generalization from reasoning SFT with long chain-of-thought supervision depends jointly on optimization dynamics, training data, and base model capability. \
  <a href="https://arxiv.org/abs/2604.06628"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/Nebularaid2000/rethink_sft_generalization"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/collections/jasonrqh/rethink-sft-generalization"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **ProFit: Leveraging High-Value Signals in SFT via Probability-Guided Token Selection** (2026.01) \
  **Description**: This paper presents ProFit, a supervised fine-tuning method that mitigates single-reference overfitting by using token probability as a proxy for semantic importance and masking low-probability tokens. The approach focuses learning on core logical content and improves reasoning and math performance over standard SFT baselines. \
  <a href="https://arxiv.org/abs/2601.09195"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **BEFT: Bias-Efficient Fine-Tuning of Language Models in Low-Data Regimes** (2025.09) \
  **Description**: This paper studies which attention-projection bias terms to fine-tune in low-data settings and finds that directly tuning the value bias generally outperforms tuning query or key biases. The result holds across encoder-only and decoder-only language models up to 6.7B parameters, including bias-free models augmented with a value bias. \
  <a href="https://arxiv.org/abs/2509.15974"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/whubaichuan/BEFT"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

# Training

## Data Preparation

- **GraphForge: Training Working Agents with Graph-Anchored Workspace Synthesis** (2026.09) \
  **Description**: GraphForge synthesizes training tasks for working agents from real-file workspaces, using an evidence graph to ground both task requirements and verification rubrics. It checks executability and revises tasks before collecting trajectories, improving downstream agent performance through fine-tuning. \
  <a href="https://arxiv.org/abs/2609.38923"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://huggingface.co/collections/groundhogLLM/graphforge"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **BigBang: Pursuing Open-Ended Intelligence through Self-Evolving Synthesis of Verifiable Frontier Tasks** (2026.08) \
  **Description**: BigBang is a general-purpose 35B-A3B model post-trained on verifiable frontier tasks generated by an adversarial, self-evolving generator-critic framework. Calibrated with held-out research tasks, the pipeline iteratively improves task difficulty and evaluation quality, yielding broad gains in scientific research, reasoning, coding, and tool use. \
  <a href="https://endlessfrontier.tech/assets/paper.pdf"><img src="assets/icons/paper.svg" alt="Paper" width="20"></a>
  <a href="https://endlessfrontier.tech/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/endless-frontier/BigBang-v1"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/endless-frontier/BigBang-v1"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **DataPrep-Bench: Benchmarking LLMs as Training Data Preparators** (2026.05) \
  **Description**: DataPrep-Bench is the first unified, downstream-grounded benchmark for evaluating how LLMs, agents, and data-centric workflows construct supervised training data and predict candidate datasets' downstream utility. It also introduces a skill-guided construction agent and the Distributional Alignment Score, which outperforms existing quality, diversity, and heuristic evaluators across most tested domains. \
  <a href="https://arxiv.org/abs/2607.20465"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://datapreparationbench.github.io/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/OpenDCAI/Data-Preparation-Bench"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/datasets/lhpku20010120/Data-Prep-Bench"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

## Optimization

- **PowLU: An Activation Function for Stable Pre-Training of LLMs** (2026.05) \
  **Description**: This paper identifies SwiGLU's near-quadratic amplification on large positive inputs as a source of outliers and numerical instability in low-precision large-scale LLM pre-training. It proposes Power Linear Unit (PowLU), a rational-power activation that preserves adaptive nonlinearity while stabilizing spike regions, with scaling-law and Ling-model experiments showing competitive performance and improved training scalability. \
  <a href="https://arxiv.org/abs/2605.25704"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **Pre-training LLM without Learning Rate Decay Enhances Supervised Fine-Tuning** (2026.03) \
  **Description**: This paper shows that Warmup-Stable-Only pre-training, which keeps the learning rate constant after warmup, consistently improves downstream SFT performance over decay-based schedules across 1B and 8B models. Its loss-landscape analysis attributes the gain to flatter minima that preserve model adaptability. \
  <a href="https://arxiv.org/abs/2603.16127"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

## Distillation

- **Rethinking On-Policy Distillation of Large Language Models II: One Training Example** (2026.09) \
  **Description**: This paper studies on-policy distillation at the data-minimal limit and finds that training on a single query recovers most of the gain from full-data OPD across domains and model families. It explains this through state coverage and student-teacher alignment, showing that 16 semantically distinct queries can match full-data training while OPD is data-overfed but algorithm-starved. \
  <a href="https://arxiv.org/abs/2609.04172"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/Thinking-Space/One-Shot-OPD"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

- **On-Policy or Off-Policy Learning? A Systematic Study of Distillation Dynamics** (2026.09) \
  **Description**: This controlled study separates rollout policy, token-level KL direction, and learning rate in strong-to-weak distillation. Forward KL is robust to rollout source, reverse KL favors student-generated rollouts, and learning rate has a stronger effect on forgetting and update sparsity than rollout policy. \
  <a href="https://arxiv.org/abs/2609.35259"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **Simple-OPD: Demystifying Warm-up for On-policy Distillation** (2026.08) \
  **Description**: This paper shows that effective warm-up for on-policy distillation depends on teacher-compatible chain-of-thought supervision rather than answer correctness alone. It proposes Simple-OPD, a plug-and-play initialization recipe that uses near-saturation LoRA warm-up on teacher-generated reasoning traces to balance in-domain adaptation and out-of-distribution generalization. \
  <a href="https://arxiv.org/abs/2608.06802"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://wangjunjie-ai.github.io/publication/2026-08-07-simple-opd"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/Utaotao/Simple-OPD"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

- **Escaping the KL Agreement Trap in On-Policy Distillation** (2026.06) \
  **Description**: This paper identifies a low-KL agreement trap in on-policy distillation, where a teacher locally agrees with a student's corrupted rollout and provides little corrective supervision. It proposes KAT, an adaptive online termination rule that filters these uninformative suffixes, improving mathematical reasoning accuracy while reducing average rollout length by 59.73%. \
  <a href="https://arxiv.org/abs/2606.09471"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **On-Policy Distillation with Best-of-N Teacher Rollout Selection** (2026.05) \
  **Description**: This paper proposes BRTS, which samples multiple teacher trajectories and selects supervision by prioritizing correctness and then alignment with the student's current behavior. An auxiliary teacher-context branch and ground-truth-conditioned recovery improve OPD on challenging mathematical reasoning benchmarks. \
  <a href="https://arxiv.org/abs/2605.09725"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/BWGZK-keke/BRTS"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

- **Trust Region On-Policy Distillation** (2026.05) \
  **Description**: This paper proposes TrOPD to stabilize on-policy distillation under large teacher-student distribution mismatch by restricting reverse-KL supervision to reliable regions. It handles outliers through clipping, masking, or forward-KL estimation and uses teacher-prefix off-policy guidance to steer exploration back toward trustworthy regions. \
  <a href="https://arxiv.org/abs/2606.01249"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **Revisiting On-Policy Distillation: Empirical Failure Modes and Simple Fixes** (2026.03) \
  **Description**: This paper identifies three failure modes in sampled-token OPD: imbalanced token supervision, unreliable teacher guidance on student-generated prefixes, and tokenizer or special-token mismatch. It combines teacher top-K local support matching with top-p rollout sampling and special-token masking, improving stability and outperforming standard OPD by 19.8%. \
  <a href="https://arxiv.org/abs/2603.25562"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/hhh675597/revisiting_opd"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

- **Knowledge Distillation of Large Language Models** (2023.06) \
  **Description**: This paper studies white-box knowledge distillation for generative LLMs and proposes MiniLLM, replacing the standard forward KLD objective with reverse KLD to avoid overestimating low-probability teacher regions. The method derives an effective optimization procedure and improves instruction-following quality, calibration, exposure bias, and long-text generation across model families from 120M to 13B parameters. \
  <a href="https://arxiv.org/abs/2306.08543"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/microsoft/LMOps/tree/main/minillm"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/MiniLLM"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

# Reinforcement Learning

## Policy Optimization

- **Bellman Policy Optimization** (2026.09) \
  **Description**: This paper introduces Bellman Policy Optimization (BPO), a critic-free RLVR method that uses the Bellman equations to reformulate Policy Mirror Descent as a trajectory-level objective with the same unique optimum, avoiding intermediate state-value estimation. Its practical loss replaces GRPO's importance-sampling ratio with a mismatch-correction weight based on smoothed complementary token probabilities. \
  <a href="https://arxiv.org/abs/2609.15987"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **Score Centering Stabilizes Off-policy Reinforcement Learning** (2026.09) \
  **Description**: This paper identifies accumulating gradient drift as a primary cause of LLM reinforcement learning instability under training-inference mismatch and introduces an additive score-centering correction to cancel it. Across 0.6B–30B models, score centering matches or outperforms importance-sampling methods under quantization and combines with them to improve robustness to stale rollouts. \
  <a href="https://arxiv.org/abs/2609.20807"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/martin-marek/score-centering"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

- **Is One Layer Enough? Training A Single Transformer Layer Can Match Full-Parameter RL Training** (2026.07) \
  **Description**: This paper introduces layer contribution to measure how much of full-parameter RL improvement can be recovered by training each transformer layer independently. Across multiple models, RL algorithms, and tasks, it finds that gains consistently concentrate in a few middle layers and that single-layer training can match or surpass full-parameter training. \
  <a href="https://arxiv.org/abs/2607.01232"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **Turning Off-Policy Tokens On-Policy: A Plug-in Approach for Improving LLM Alignment** (2026.07) \
  **Description**: This paper introduces Selective Importance Sampling (SIS), a plug-in correction for off-policy LLM reinforcement learning that uses token-level rejection tests to treat accepted tokens as on-policy while retaining standard importance sampling for rejected tokens. SIS reduces the gap between token- and sequence-level gradient estimators with negligible overhead, improving performance and robustness across dense and MoE models. \
  <a href="https://arxiv.org/abs/2607.04728"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **SERPO: Self-Evolving Rubric Policy Optimization for Open-Ended Test-Time Reinforcement Learning** (2026.07) \
  **Description**: This paper introduces SERPO, a test-time reinforcement learning framework for open-ended generation that co-evolves response evidence, query-specific rubrics, and policy parameters without labeled feedback, external reward models, or stronger judges. Probabilistic criterion scoring turns verdict-token likelihoods into rewards, enabling the actor and its self-generated evaluation criteria to improve in a closed loop. \
  <a href="https://arxiv.org/abs/2607.26873"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/chiefovoavicii/SERPO"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

- **Rethinking the Divergence Regularization in LLM RL** (2026.06) \
  **Description**: This paper proposes Divergence Regularized Policy Optimization (DRPO), replacing DPPO's hard divergence mask with a smooth advantage-weighted quadratic regularizer that preserves its trust-region geometry. DRPO provides bounded continuous gradient weights and corrective signals beyond the trust-region boundary, improving LLM RL training stability and efficiency. \
  <a href="https://arxiv.org/abs/2606.09821"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/Tencent-Hunyuan/UniRL"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

- **Constraint-Infused Policy Optimization: Principles and Practices for Harnessing Advanced LLM Reasoning** (2026.05) \
  **Description**: This paper formulates LLM reinforcement learning as constrained policy optimization, unifying existing algorithms through different constraint choices and exposing the roles of clipping, KL regularization, and trust regions. It derives Constraint-Infused Policy Optimization (CIPO), which improves reasoning performance and training stability across diverse tasks and model families. \
  <a href="https://arxiv.org/abs/2605.16826"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/trestad/CIPO"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

- **BandPO: Bridging Trust Regions and Ratio Clipping via Probability-Aware Bounds for LLM Reinforcement Learning** (2026.03) \
  **Description**: BandPO projects trust regions defined by general divergence measures into dynamic, probability-aware clipping intervals, expanding the update margin for low-probability high-advantage actions. This principled replacement for fixed PPO-style clipping improves exploration and robustly mitigates entropy collapse across LLM reinforcement learning settings. \
  <a href="https://arxiv.org/abs/2603.04918"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/OpenMOSS/BandPO"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

- **Soft Adaptive Policy Optimization** (2025.11) \
  **Description**: This paper introduces Soft Adaptive Policy Optimization (SAPO), replacing hard clipping in group-based LLM reinforcement learning with a temperature-controlled soft gate that continuously attenuates off-policy token updates. Its sequence-coherent, token-adaptive objective improves training stability, sample efficiency, and reasoning performance across text and Qwen3-VL models. \
  <a href="https://arxiv.org/abs/2511.20347"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **Group Sequence Policy Optimization** (2025.07) \
  **Description**: This paper introduces GSPO, a reinforcement learning algorithm for LLMs that replaces token-level importance ratios with sequence-level likelihood ratios and performs sequence-level clipping, rewarding, and optimization. GSPO improves training efficiency and performance over GRPO, stabilizes MoE RL training, and helps simplify large-scale RL infrastructure for Qwen3 models. \
  <a href="https://arxiv.org/abs/2507.18071"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://qwen.ai/blog?id=gspo"><img src="assets/icons/project.svg" alt="Project" width="20"></a>

- **DAPO: An Open-Source LLM Reinforcement Learning System at Scale** (2025.03) \
  **Description**: This paper introduces Decoupled Clip and Dynamic Sampling Policy Optimization (DAPO), an open large-scale reinforcement learning system for eliciting LLM reasoning. It releases the training recipe, code, dataset, and model weights, reaching 50 points on AIME 2024 with Qwen2.5-32B and improving reproducibility for large-scale LLM RL. \
  <a href="https://arxiv.org/abs/2503.14476"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://dapo-sia.github.io/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/BytedTsinghua-SIA/DAPO"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/BytedTsinghua-SIA/DAPO-Qwen-32B"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **Provably Mitigating Overoptimization in RLHF: Your SFT Loss is Implicitly an Adversarial Regularizer** (2024.05) \
  **Description**: This paper identifies RLHF overoptimization as a consequence of distribution shift and uncertainty in learned preferences, then introduces Regularized Preference Optimization (RPO), which combines a preference optimization objective with an SFT loss that acts as an adversarial regularizer. RPO provides finite-sample guarantees and empirically improves alignment over DPO while reducing drift toward undesired responses. \
  <a href="https://arxiv.org/abs/2405.16436"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/YSLIU627/Regularized-Preference-Optimization"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

- **KTO: Model Alignment as Prospect Theoretic Optimization** (2024.02) \
  **Description**: This paper frames successful LLM alignment losses as human-aware losses that encode biases from prospect theory, then introduces KTO to optimize generation utility directly from binary desirable/undesirable feedback. KTO matches or exceeds preference-pair methods from 1B to 30B scales, highlighting how the best alignment loss depends on the setting's inductive biases. \
  <a href="https://arxiv.org/abs/2402.01306"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **Direct Preference Optimization: Your Language Model is Secretly a Reward Model** (2023.05) \
  **Description**: This paper introduces Direct Preference Optimization (DPO), which reparameterizes the RLHF reward model so the optimal policy can be learned directly from preference data with a simple classification loss. DPO removes separate reward-model fitting and online reinforcement learning while matching or improving PPO-based RLHF with simpler, more stable training. \
  <a href="https://arxiv.org/abs/2305.18290"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/eric-mitchell/direct-preference-optimization"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

- **Proximal Policy Optimization Algorithms** (2017.07) \
  **Description**: This paper introduces Proximal Policy Optimization (PPO), a family of policy-gradient methods that alternates environment sampling with multiple minibatch epochs on a surrogate objective. PPO retains key trust-region benefits while being simpler to implement and empirically balancing sample efficiency, performance, and wall-clock time. \
  <a href="https://arxiv.org/abs/1707.06347"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://openai.com/index/openai-baselines-ppo/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/openai/baselines"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

## OPD

- **The Teacher Is a Direction, Not a Destination: Extrapolating RL-Induced Representation Residuals in On-Policy Distillation** (2026.09) \
  **Description**: RIDE performs on-policy distillation by extrapolating the layerwise representation shift from a base model to its RL-trained teacher and regressing the student's hidden states toward those targets on student-generated trajectories. Across four model pairs, it approaches or exceeds the teachers and outperforms output-space reward extrapolation. \
  <a href="https://arxiv.org/abs/2609.36484"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/xixixixixxxx/RIDE"><img src="assets/icons/project.svg" alt="Project" width="20"></a>

- **Does On-Policy Distillation Really Distill? From Noisy Teacher to Self-Improvement** (2026.08) \
  **Description**: This paper finds that noisy teacher supervision is not the main source of on-policy distillation gains: suppressing student-sampled low-probability tokens with a fixed negative advantage achieves comparable performance. It introduces On-Policy Self-Adaptation (OPSA), a teacher- and reward-free method that scales negative advantages by token entropy to improve reasoning and generalization. \
  <a href="https://arxiv.org/abs/2608.31046"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://dripnowhy.github.io/On-Policy-Self-Adaptation/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/DripNowhy/On-Policy-Self-Adaptation"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/collections/Tuwhy/on-policy-self-adaptation"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **PowerOPD: Stabilizing On-Policy Distillation with Bounded Power Transformation** (2026.06) \
  **Description**: This paper identifies the unbounded log-ratio reward as the source of high-variance gradients and unstable training in sampled-token on-policy distillation. PowerOPD replaces it with a bounded, sign-consistent reward family derived from the Box-Cox power transformation, improving mathematical reasoning accuracy while reducing time and memory relative to full-vocabulary OPD. \
  <a href="https://arxiv.org/abs/2606.17199"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **Anti-Self-Distillation for Reasoning RL via Pointwise Mutual Information** (2026.05) \
  **Description**: This paper analyzes why on-policy self-distillation can hurt math reasoning, showing through pointwise mutual information that privileged context overemphasizes solution-implied tokens while suppressing deliberation tokens needed for search. It proposes AntiSD, which ascends rather than descends the self-distillation divergence with an entropy gate, reaching GRPO-level accuracy in 2 to 10x fewer steps and improving final accuracy by up to 11.5 points. \
  <a href="https://arxiv.org/abs/2605.11609"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/FloyedShen/AntiSD"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

- **Draft-OPD: Adapting Speculative Draft Models from LLMs via On-Policy Distillation** (2026.05) \
  **Description**: This paper proposes Draft-OPD, which adapts speculative draft models from RL-trained LLM traces through on-policy distillation without requiring expensive online generation for the draft model. It proves an equivalence between RL training and OPD-style distillation, reuses collected RL experience, and improves speculative decoding speed by up to 2.14x while preserving task performance. \
  <a href="https://arxiv.org/abs/2605.29343"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://www.haodilei.top/draft-opd/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/bingyang-lei/Draft-OPD"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/collections/bingyang-lei/draft-opd"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **OmniOPD: Logit-Free On-Policy Distillation via Speculative Verification** (2026.05) \
  **Description**: This paper introduces OmniOPD, a logit-free on-policy distillation framework that replaces brittle token-level logit matching with Monte Carlo chunk rollouts scored by semantic similarity, enabling black-box teachers. A peak-entropy scheduler focuses verification on uncertain reasoning forks, while Bayesian smoothing and a base-model KL anchor stabilize training; it outperforms standard OPD by up to 28.64% on math. \
  <a href="https://arxiv.org/abs/2606.01476"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **Self-Distilled RLVR** (2026.04) \
  **Description**: This paper studies on-policy self-distillation for RLVR and shows that relying only on a privileged self-teacher can cause information leakage and unstable long-term training. It proposes RLSD, which uses self-distillation to estimate token-level update magnitudes while keeping RLVR's environment feedback as the reliable update direction. \
  <a href="https://arxiv.org/abs/2604.03128"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://huggingface.co/datasets/iieycx/rlsd-train-MMFineReason-123K"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **Learning beyond Teacher: Generalized On-Policy Distillation with Reward Extrapolation** (2026.02) \
  **Description**: This paper shows that on-policy distillation is a special case of dense KL-constrained RL, then proposes G-OPD with a flexible reference model and reward scaling factor. Its reward extrapolation variant, ExOPD, improves over standard OPD and can let students surpass domain teachers when merging RL-trained experts. \
  <a href="https://arxiv.org/abs/2602.12125"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/RUCBM/G-OPD"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/datasets/Keven16/G-OPD-Training-Data"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models** (2026.01) \
  **Description**: This paper introduces On-Policy Self-Distillation (OPSD), where a single LLM acts as teacher and student under different contexts: the teacher sees privileged verified reasoning traces while the student samples from the question-only policy. By matching per-token distributions over the student's on-policy rollouts, OPSD provides dense supervision without an external teacher and achieves stronger token efficiency than GRPO and off-policy distillation on math reasoning. \
  <a href="https://arxiv.org/abs/2601.18734"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://siyan-zhao.github.io/blog/2026/opsd/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/siyan-zhao/OPSD"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

- **Self-Distillation Enables Continual Learning** (2026.01) \
  **Description**: This paper introduces Self-Distillation Fine-Tuning (SDFT), an on-policy self-distillation method that learns from expert demonstrations by using a demonstration-conditioned model as its own teacher. It improves new-task acquisition while reducing catastrophic forgetting, enabling sequential accumulation of skills and knowledge without explicit reward functions. \
  <a href="https://arxiv.org/abs/2601.19897"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://self-distillation.github.io/SDFT"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/idanshen/Self-Distillation"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

## Reward Modeling

- **RULER: Instance-aware Rubric Rewards for SVG Generation** (2026.09) \
  **Description**: RULER addresses unreliable evaluation and reward hacking in text-to-SVG generation by deriving six instruction-specific rubric items across semantic, visual, and stylistic dimensions. A vision-language judge scores rendered outputs item by item, and their weighted scores provide GRPO rewards without paired SVG ground truth or human preference labels. \
  <a href="https://arxiv.org/abs/2609.25270"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://hangyuran.github.io/RULER/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>

- **The Verification Horizon: No Silver Bullet for Coding Agent Rewards** (2026.06) \
  **Description**: This paper frames reliable verification as the emerging bottleneck for coding agents and evaluates reward signals by scalability, faithfulness, and robustness. Through test, rubric, user-feedback, and automated-agent verifiers, it shows that targeted designs can curb reward hacking and argues that verification must co-evolve with increasingly capable generators. \
  <a href="https://arxiv.org/abs/2606.26300"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **Bringing Value Models Back: Generative Critics for Value Modeling in LLM Reinforcement Learning** (2026.04) \
  **Description**: This paper revisits value modeling for LLM reinforcement learning and argues that one-shot discriminative critics are limited by their expressiveness. It introduces Generative Actor-Critic (GenAC), whose critic reasons before estimating value and uses in-context conditioning to track the current actor, improving value approximation, ranking reliability, out-of-distribution generalization, and downstream RL performance. \
  <a href="https://arxiv.org/abs/2604.10701"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **Reason Only When Needed: Efficient Generative Reward Modeling via Model-Internal Uncertainty** (2026.04) \
  **Description**: This paper introduces E-GRM, which estimates uncertainty from the convergence of parallel model generations and triggers chain-of-thought reasoning only when needed. A lightweight discriminative scorer trained with a hybrid regression-ranking objective provides fine-grained reasoning-path rewards, reducing inference cost while improving accuracy. \
  <a href="https://arxiv.org/abs/2604.10072"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **MemReward: Graph-Based Experience Memory for LLM Reward Prediction with Limited Labels** (2026.03) \
  **Description**: This paper introduces MemReward, a graph-based experience memory framework that achieves 97.3% of Oracle performance on 3B and 96.6% on 1.5B models for reward prediction with limited labels, surpassing Oracle in out-of-domain tasks. \
  <a href="https://arxiv.org/abs/2603.19310"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/ulab-uiuc/MemReward"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/datasets/ulab-ai/MemReward"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **Scaling Reward Modeling without Human Supervision** (2026.03) \
  **Description**: This paper studies unsupervised reward model scaling by learning preferences over web-corpus document prefixes and suffixes without human annotations. It reports consistent RewardBench gains across model backbones and shows downstream improvements in best-of-N selection and policy optimization. \
  <a href="https://arxiv.org/abs/2603.02225"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **Reward Modeling from Natural Language Human Feedback** (2026.01) \
  **Description**: This paper introduces RLVR on preference data for training Generative Reward Models, demonstrating that binary classification tasks make GRMs susceptible to guessing correct outcomes without sound critiques, and proposes a method to address this limitation. \
  <a href="https://arxiv.org/abs/2601.07349"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models** (2025.10) \
  **Description**: This survey reviews Process Reward Models for evaluating and guiding LLM reasoning at the step or trajectory level rather than only judging final answers. It organizes the full loop of process data generation, PRM construction, and PRM use in test-time scaling and reinforcement learning across math, code, multimodal reasoning, robotics, and agents. \
  <a href="https://arxiv.org/abs/2510.08049"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

## Video Generation RL

- **KVPO: ODE-Native GRPO for Autoregressive Video Alignment via KV Semantic Exploration** (2026.05) \
  **Description**: KVPO aligns streaming autoregressive video generators with human preferences using an ODE-native online GRPO framework. It replaces noise-based exploration with causal-semantic routing of historical KV cache entries and optimizes a velocity-field surrogate policy based on Trajectory Velocity Energy. \
  <a href="https://arxiv.org/abs/2605.14278"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://richard-zhang-ai.github.io/KVPO-Project/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/Richard-Zhang-AI/KVPO"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/Richard-ZZZZZ/KVPO"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

## Multimodal RL

- **Adaptive Reward Routing: Dynamic Multi-Reward Optimization for Joint Audio-Video Diffusion via Forward-Process RL** (2026.09) \
  **Description**: Adaptive Reward Routing improves reinforcement learning for joint audio-video diffusion by using cross-attention responses to direct reward-driven updates and reward-gradient interactions to adjust competing objectives. It improves modality quality, semantic alignment, and audio-video synchronization over RL baselines. \
  <a href="https://arxiv.org/abs/2609.37200"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **CapRL: Stimulating Dense Image Caption Capabilities via Reinforcement Learning** (2025.09) \
  **Description**: This paper introduces CapRL, the first RLVR framework for open-ended image captioning, which rewards captions by whether a vision-free language model can answer image questions using only the generated description. The resulting CapRL-3B model produces more informative and diverse captions, while its generated caption data improves large vision-language model pretraining across 12 benchmarks. \
  <a href="https://arxiv.org/abs/2509.22647"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/InternLM/CapRL"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/internlm/CapRL-3B"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **Visual Planning: Let's Think Only with Images** (2025.05) \
  **Description**: This paper introduces Visual Planning, a paradigm that performs step-by-step planning through sequences of images rather than text for vision-first spatial tasks. Its Visual Planning via Reinforcement Learning (VPRL) framework uses GRPO to post-train large vision models and improves planning on FrozenLake, Maze, and MiniBehavior. \
  <a href="https://arxiv.org/abs/2505.11409"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/yix8/VisualPlanning"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

## Reasoning RL

- **Ring-Zero: Scaling Zero RL to a Trillion Parameters for Emergent Reasoning** (2026.07) \
  **Description**: This paper scales reinforcement learning with verifiable rewards from a base model to one trillion parameters through a stable pipeline combining clipped importance sampling, training-inference ratio correction, and mixed-precision control. The resulting model improves sample efficiency and reasoning quality while spontaneously developing structured, self-verifying, and adaptive reasoning behaviors. \
  <a href="https://arxiv.org/abs/2607.12395"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **All Roads Lead to Rome: Incentivizing Divergent Thinking in Vision-Language Models** (2026.04) \
  **Description**: This paper presents MUPO, a reinforcement learning approach that addresses diversity collapse in GRPO-trained VLMs by incentivizing divergent thinking across multiple solutions, enabling deeper yet broader reasoning patterns. \
  <a href="https://arxiv.org/abs/2604.00479"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://xytian1008.github.io/MUPO/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/xytian1008/MUPO"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/xytian1008/MUPO-Thinker-7B"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **VL-Calibration: Decoupled Confidence Calibration for Large Vision-Language Models Reasoning** (2026.04) \
  **Description**: This paper introduces VL-Calibration, a reinforcement learning framework that separates visual and reasoning confidence in large vision-language models to address confidently incorrect predictions. It estimates visual certainty from image-perturbation grounding and token entropy, then applies token-level advantage reweighting to improve calibration and visual reasoning accuracy. \
  <a href="https://arxiv.org/abs/2604.09529"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/Mr-Loevan/VL-Calibration"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

- **The Art of Efficient Reasoning: Data, Reward, and Optimization** (2026.03) \
  **Description**: This paper studies efficient reasoning in LLMs, using RL to incentivize short accurate trajectories, with findings on training stages, rewards, and generalization across models from 0.6B to 30B parameters. \
  <a href="https://arxiv.org/abs/2602.20945"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://wutaiqiang.github.io/project/Art"><img src="assets/icons/project.svg" alt="Project" width="20"></a>

- **FIPO: Eliciting Deep Reasoning with Future-KL Influenced Policy Optimization** (2026.03) \
  **Description**: This paper presents FIPO, a reinforcement learning algorithm that overcomes reasoning bottlenecks in LLMs by addressing coarse-grained credit assignment in GRPO-style training, where outcome-based rewards fail to distinguish critical logical pivots from trivial tokens. \
  <a href="https://arxiv.org/abs/2603.19835"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **Agentic Proposing: Enhancing Large Language Model Reasoning via Compositional Skill Synthesis** (2026.02) \
  **Description**: This paper introduces Agentic Proposing, a framework that uses a specialized agent with Multi-Granularity Policy Optimization (MGPO) to dynamically select and compose modular reasoning skills for synthesizing high-precision training trajectories. \
  <a href="https://arxiv.org/abs/2602.03279"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **The Entropy Mechanism of Reinforcement Learning for Reasoning Language Models** (2025.05) \
  **Description**: This paper studies policy entropy collapse as a bottleneck in RL for reasoning language models, showing an empirical relationship between entropy and downstream performance that makes the performance ceiling predictable. It derives entropy dynamics from the covariance between action probability and logit updates, then proposes Clip-Cov and KL-Cov to preserve exploration and improve downstream performance. \
  <a href="https://arxiv.org/abs/2505.22617"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>

- **Seek in the Dark: Reasoning via Test-Time Instance-Level Policy Gradient in Latent Space** (2025.05) \
  **Description**: This paper introduces LatentSeek, a test-time instance-level adaptation framework that uses policy gradients and self-generated rewards to iteratively optimize an LLM's latent representations without updating model parameters. It improves reasoning across GSM8K, MATH-500, and AIME2024 while typically converging within only a few iterations. \
  <a href="https://arxiv.org/abs/2505.13308"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://bigai-nlco.github.io/LatentSeek/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/bigai-nlco/LatentSeek"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

- **DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning** (2025.01) \
  **Description**: This paper shows that pure reinforcement learning can directly elicit advanced reasoning behaviors in LLMs without human-labeled reasoning traces. The proposed framework induces self-reflection, verification, and adaptive strategy use, leading to strong gains on math, coding, and STEM reasoning tasks. \
  <a href="https://arxiv.org/abs/2501.12948"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://huggingface.co/deepseek-ai/DeepSeek-R1"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models** (2024.02) \
  **Description**: This paper introduces DeepSeekMath 7B, combining a carefully engineered web-scale math data selection pipeline with Group Relative Policy Optimization (GRPO), a PPO variant. The approach improves mathematical reasoning while reducing PPO's memory usage, reaching strong competition-level MATH performance without external tools or voting. \
  <a href="https://arxiv.org/abs/2402.03300"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/deepseek-ai/deepseek-math"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/deepseek-ai/deepseek-math-7b-rl"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

## Agentic RL

- **Sharpening Tax in Post-Training** (2026.10) \
  **Description**: This paper finds that RL post-training often raises agents' single-shot accuracy while reducing the range of tasks they can solve with repeated attempts, and introduces Sharpening Tax to measure the lost test-time scalability. Posterior-tempered group sampling adapts rollout temperature to task difficulty during RL training, improving both accuracy and solution coverage. \
  <a href="https://arxiv.org/abs/2610.01509"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://changdaeoh.github.io/sharpening-tax/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://github.com/changdaeoh/sharpening-tax"><img src="assets/icons/github.svg" alt="Code" width="20"></a>

- **MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement** (2026.10) \
  **Description**: MiMo-V2.6 scales agentic reinforcement learning through asynchronous large-batch training, diverse environments and harnesses, and groupwise agentic grading for more informative rewards on long-horizon tasks. Router freezing, layered defenses against reward hacking, and unified mixed-task rollout infrastructure support stable scaling across coding, general, visual, and cybersecurity tasks. \
  <a href="https://arxiv.org/abs/2610.11959"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://mimo.xiaomi.com/rl/mimo-v26/"><img src="assets/icons/project.svg" alt="Project" width="20"></a>
  <a href="https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **Agent-Reflex: Teaching Language Agents to Act Reflectively** (2026.10) \
  **Description**: Agent-Reflex trains tool-using agents to reflect proactively and recover from noisy tool feedback and user corrections by mining reusable reflection skills and converting them into reflective supervised fine-tuning data. Its On-Policy Reflective Policy Optimization combines agentic RL under noisy interactions with reflection-guided on-policy distillation, improving long-horizon tool use and robustness to noise. \
  <a href="https://arxiv.org/abs/2610.17953"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a href="https://github.com/RUC-NLPIR/Agent-Reflex"><img src="assets/icons/github.svg" alt="Code" width="20"></a>
  <a href="https://huggingface.co/collections/dongguanting/agent-reflex"><img src="assets/icons/huggingface.svg" alt="Hugging Face" width="20"></a>

- **SafeEvolve: Harness-Policy Co-Evolution from Agent Experience for Safety Alignment** (2026.09) \
  **Description**: SafeEvolve uses safety evidence from on-policy agent trajectories to co-evolve runtime safety prompts, hierarchical skills, and the policy. It combines bounded, auditable harness updates with harness-use SFT and harness-augmented RL using verifier-decomposed rewards, improving the balance between safety and task utility during multi-step interactions. \
  <a href="https://arxiv.org/abs/2609.02786"><img src="assets/icons/arxiv.svg" alt="Paper" width="20"></a>
  <a h