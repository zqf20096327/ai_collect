## 📢 News

- **[2026-09]** ➕ Added 104 new papers: new base models (DiffusionGemma, LLaDA2.1, LLaDA MoE v2, Seed Diffusion, Mercury, Nemotron-Labs-Diffusion), a major Safety & Alignment expansion (jailbreaks, backdoors, privacy attacks & defenses), the diffusion speculative-decoding family (DFlash, DSpark, AdaFlash, …), and new work across RL, distillation, foundations, adaptation, multimodal, and code dLLMs.
- **[2026-07]** 🎉 Repository restructured around a method-centric post-training taxonomy. All entries now use arXiv + AlphaXiv badges and collapsible details. Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

## 📖 What Counts as dLLM Post-Training?

This list focuses on the **post-training** stage of Diffusion Language Models, i.e. everything that happens after (or adapts) the base diffusion pre-training:

- **Base models** — influential dLLMs whose training pipeline includes a post-training (SFT / alignment) stage and that subsequent post-training work builds upon
- **SFT & instruction tuning** — supervised fine-tuning for instruction following, chat, long-CoT, and task adaptation
- **Preference optimization** — DPO/KTO/IPO-style alignment from paired or unpaired preference data
- **RL & reasoning** — GRPO/PPO/RLVR policy optimization, reward modeling, and trajectory-level RL for reasoning
- **Safety & alignment** — safety training, jailbreak robustness, and alignment analysis specific to dLLMs
- **Distillation** — knowledge/self/consistency/few-step distillation for faster or smaller dLLMs
- **Inference acceleration** — learned parallel decoding, speculative decoding, KV-cache training, and guidable decoding
- **Training objectives & foundations** — core discrete-diffusion objectives and training-inference analyses that post-training builds upon
- **Adaptation techniques** — AR→DLM conversion, long-context post-training, and representation alignment
- **Multimodal & code dLLMs** — domain-specific post-training for vision-language and code diffusion LMs

We cover **masked/absorbing, block, and continuous diffusion LMs**, including **multimodal** and **code** dLLMs. Pure pre-training architecture papers are included only when they establish training objectives or pipelines that post-training builds upon.

## 📑 Table of Contents

- [Surveys](#surveys) (7)
- [Base Models](#base-models) (12)
- [SFT & Instruction Tuning](#sft--instruction-tuning) (9)
- [Preference Optimization](#preference-optimization) (5)
- [RL & Reasoning](#rl--reasoning) (43)
- [Safety & Alignment](#safety--alignment) (14)
- [Distillation](#distillation) (23)
- [Inference Acceleration](#inference-acceleration) (41)
- [Training Objectives & Foundations](#training-objectives--foundations) (21)
- [Adaptation Techniques](#adaptation-techniques) (13)
- [Multimodal dLLMs](#multimodal-dllms) (28)
- [Code dLLMs](#code-dllms) (17)
- [Frameworks & Benchmarks](#frameworks--benchmarks)
- [Star History](#star-history)
- [Contributing](#contributing)
- [License](#license)

---

## Surveys

- <details>
  <summary>
    <b>[09/2026] Diffusion Language Models for Mobile Edge Agentic AI: Foundations, Applications, and Challenges</b>
    <a href="https://arxiv.org/abs/2609.04778"><img src="https://img.shields.io/badge/arXiv-2609.04778-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2609.04778"><img src="https://img.shields.io/badge/AlphaXiv-2609.04778-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Chenqi Li, Minghui Min, Dusit Niyato, Wei Ni

  **TL;DR:** A survey on diffusion language models for mobile edge agentic AI, covering foundations, applications, and challenges including multimodal dLLMs. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[07/2026] Accelerating Masked Diffusion Large Language Models: A Survey of Efficient Inference Techniques</b>
    <a href="https://arxiv.org/abs/2607.12829"><img src="https://img.shields.io/badge/arXiv-2607.12829-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2607.12829"><img src="https://img.shields.io/badge/AlphaXiv-2607.12829-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Daehoon Gwak, Minhyung Lee, Junwoo Park, Jaegul Choo

  **TL;DR:** Introduces a unified latency decomposition framework for dLLMs and surveys efficient inference techniques across algorithms, architectures, and systems, with reproducible benchmarking guidelines. IJCAI-ECAI 2026 Survey Track.
  </details>

- <details>
  <summary>
    <b>[04/2026] Beyond the Autoregressive Horizon: A Comprehensive Survey of Diffusion Models, World Modelling, and State Space Models for Code</b>
    <a href="https://arxiv.org/abs/2606.23690"><img src="https://img.shields.io/badge/arXiv-2606.23690-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2606.23690"><img src="https://img.shields.io/badge/AlphaXiv-2606.23690-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Kishan Maharaj, Ashita Saxena, Srikanth Tamilselvam

  **TL;DR:** A comprehensive survey of diffusion models, world models, and state-space models for code generation beyond the autoregressive paradigm. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[01/2026] Top 10 Open Challenges Steering the Future of Diffusion Language Model and Its Variants</b>
    <a href="https://arxiv.org/abs/2601.14041"><img src="https://img.shields.io/badge/arXiv-2601.14041-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2601.14041"><img src="https://img.shields.io/badge/AlphaXiv-2601.14041-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Yunhe Wang, Kai Han, Huiling Zhen, Yuchuan Tian, Hanting Chen, Yongbing Huang, Yufei Cui, Yingte Shu, et al.

  **TL;DR:** A position paper outlining ten open challenges for diffusion language models, spanning training, post-training, inference, and applications. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[08/14/2025] A Survey on Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2508.10875"><img src="https://img.shields.io/badge/arXiv-2508.10875-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2508.10875"><img src="https://img.shields.io/badge/AlphaXiv-2508.10875-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/VILA-Lab/Awesome-DLMs"><img src="https://img.shields.io/github/stars/VILA-Lab/Awesome-DLMs?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Tianyi Li, Mingda Chen, Bowei Guo, Zhiqiang Shen

  **TL;DR:** The most comprehensive DLM survey to date, systematically covering pre-training, SFT, RL alignment, inference acceleration, and applications, with a dedicated post-training chapter. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[06/2025] Discrete Diffusion in Large Language and Multimodal Models: A Survey</b>
    <a href="https://arxiv.org/abs/2506.13759"><img src="https://img.shields.io/badge/arXiv-2506.13759-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2506.13759"><img src="https://img.shields.io/badge/AlphaXiv-2506.13759-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/LiQiiiii/DLLM-Survey"><img src="https://img.shields.io/github/stars/LiQiiiii/DLLM-Survey?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Runpeng Yu, Qi Li, Xinchao Wang

  **TL;DR:** Focuses on discrete diffusion formulations, training, and inference in large language and multimodal models, covering LLaDA, Dream, Dimple, and more. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[05/2023] A Survey of Diffusion Models in Natural Language Processing</b>
    <a href="https://arxiv.org/abs/2305.14671"><img src="https://img.shields.io/badge/arXiv-2305.14671-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2305.14671"><img src="https://img.shields.io/badge/AlphaXiv-2305.14671-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Hao Zou, Zae Myung Kim, Dongyeop Kang

  **TL;DR:** An earlier survey reviewing diffusion models for NLP tasks including generation, sentiment analysis, topic modeling, and machine translation, with comparisons to autoregressive models. arXiv 2023.
  </details>

## Base Models

- <details>
  <summary>
    <b>[08/2026] LLaDA MoE v2: Scaling Mixture-of-Experts Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2608.03457"><img src="https://img.shields.io/badge/arXiv-2608.03457-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2608.03457"><img src="https://img.shields.io/badge/AlphaXiv-2608.03457-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Fengqi Zhu, Shaoxuan Xu, Jingyang Ou, Zebin You, Yipeng Xing, Huabin Liu, Xiaolu Zhang, Jun Zhou, Zhenzhong Lan, Yankai Lin, Wayne Xin Zhao, Jianguo Li, Chongxuan Li, Ji-Rong Wen

  **TL;DR:** Derives scaling principles for mixture-of-experts diffusion language models and validates them by training a 30B-A3B model that matches dense-model quality at a fraction of the compute. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[07/2026] DiffusionGemma Technical Report</b>
    <a href="https://arxiv.org/abs/2608.00146"><img src="https://img.shields.io/badge/arXiv-2608.00146-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2608.00146"><img src="https://img.shields.io/badge/AlphaXiv-2608.00146-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** DiffusionGemma Team, Adrien Ali Taïga, James Assiene, Daniele Calandriello, Rahma Chaabouni, João Gante, Tamara von Glehn, Nate Keating, et al.

  **TL;DR:** An open-weight experimental diffusion text model from Google, fine-tuned from Gemma 4 MoE (25.2B total / 3.8B active parameters) into a block-parallel diffusion LM with 256-token blocks. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[07/2026] Nemotron-Labs-Diffusion: A Tri-Mode Language Model Unifying AR, Diffusion, and Self-Speculation Decoding</b>
    <a href="https://arxiv.org/abs/2607.05722"><img src="https://img.shields.io/badge/arXiv-2607.05722-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2607.05722"><img src="https://img.shields.io/badge/AlphaXiv-2607.05722-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/NVlabs/Nemotron-Labs-Diffusion"><img src="https://img.shields.io/github/stars/NVlabs/Nemotron-Labs-Diffusion?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Yonggan Fu, Lexington Whalen, Abhinav Garg, Chengyue Wu, Maksim Khadkevich, Nicolai Oswald, Enze Xie, Daniel Egert, et al.

  **TL;DR:** A single set of weights supporting autoregressive, diffusion, and self-speculative decoding modes with an instruct-version training recipe, achieving ~6× throughput over Qwen3-8B. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[06/2026] Improved Large Language Diffusion Models (iLLaDA)</b>
    <a href="https://arxiv.org/abs/2606.25331"><img src="https://img.shields.io/badge/arXiv-2606.25331-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2606.25331"><img src="https://img.shields.io/badge/AlphaXiv-2606.25331-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/ML-GSAI/LLaDA"><img src="https://img.shields.io/github/stars/ML-GSAI/LLaDA?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Shen Nie, Qiyang Min, Shaoxuan Xu, Zihao Huang, Yuxuan Song, Yong Shan, Yankai Lin, Wayne Xin Zhao, Chongxuan Li, Ji-Rong Wen

  **TL;DR:** An 8B masked diffusion language model trained from scratch with fully bidirectional attention, scaling pre-training to 12T tokens and SFT on a 25B-token instruction corpus; strong improvements over LLaDA on general, math, and code benchmarks. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[02/2026] LLaDA2.1: Speeding Up Text Diffusion via Token Editing</b>
    <a href="https://arxiv.org/abs/2602.08676"><img src="https://img.shields.io/badge/arXiv-2602.08676-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2602.08676"><img src="https://img.shields.io/badge/AlphaXiv-2602.08676-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/inclusionAI/LLaDA2.X"><img src="https://img.shields.io/github/stars/inclusionAI/LLaDA2.X?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Tiwei Bie, Maosong Cao, Xiang Cao, Bingsen Chen, Fuyuan Chen, Kun Chen, Lun Du, Daozhuo Feng, et al.

  **TL;DR:** Introduces token-to-token (T2T) editing that revises only changed positions instead of regenerating the whole sequence, breaking the speed–quality trade-off; releases LLaDA2.1-mini and LLaDA2.1-flash. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[12/2025] LLaDA2.0: Scaling Up Diffusion Language Models to 100B</b>
    <a href="https://arxiv.org/abs/2512.15745"><img src="https://img.shields.io/badge/arXiv-2512.15745-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2512.15745"><img src="https://img.shields.io/badge/AlphaXiv-2512.15745-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/inclusionAI/LLaDA2.X"><img src="https://img.shields.io/github/stars/inclusionAI/LLaDA2.X?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Tiwei Bie, Maosong Cao, Kun Chen, Lun Du, Mingliang Gong, Zhuochen Gong, Yanmei Gu, Jiaqi Hu, Zenan Huang, Zhenzhong Lan, Chengxi Li, Chongxuan Li, Jianguo Li, Zehuan Li, Huabin Liu, Lin Liu, Guoshan Lu, Xiaocheng Lu, Yuxin Ma, Jianfeng Tan, Lanning Wei, Ji-Rong Wen, Yipeng Xing, Xiaolu Zhang, Junbo Zhao, Da Zheng, Jun Zhou, Junlin Zhou, Zhanchao Zhou, Liwang Zhu, Yihong Zhuang

  **TL;DR:** Scales diffusion language models to 100B via AR→dLLM conversion with a 3-phase block-level WSD training scheme, releasing instruction-tuned MoE variants LLaDA2.0-mini (16B) and LLaDA2.0-flash (100B). arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[09/2025] LLaDA-MoE: A Sparse MoE Diffusion Language Model</b>
    <a href="https://arxiv.org/abs/2509.24389"><img src="https://img.shields.io/badge/arXiv-2509.24389-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2509.24389"><img src="https://img.shields.io/badge/AlphaXiv-2509.24389-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/ML-GSAI/LLaDA"><img src="https://img.shields.io/github/stars/ML-GSAI/LLaDA?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Fengqi Zhu, Zebin You, Yipeng Xing, Zenan Huang, Lin Liu, Yihong Zhuang, Guoshan Lu, Kangyu Wang, Xudong Wang, Lanning Wei, Hongrui Guo, Jiaqi Hu, Wentao Ye, Tieyuan Chen, Chenchen Li, Chengfu Tang, Haibo Feng, Jun Hu, Jun Zhou, Xiaolu Zhang, Zhenzhong Lan, Junbo Zhao, Da Zheng, Chongxuan Li, Jianguo Li, Ji-Rong Wen

  **TL;DR:** A 7B-A1B MoE diffusion model trained from scratch on ~20T tokens; the Instruct version is obtained via SFT, with strong performance despite fewer active parameters. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[08/2025] Dream 7B: Diffusion Large Language Models</b>
    <a href="https://arxiv.org/abs/2508.15487"><img src="https://img.shields.io/badge/arXiv-2508.15487-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2508.15487"><img src="https://img.shields.io/badge/AlphaXiv-2508.15487-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/DreamLM/Dream"><img src="https://img.shields.io/github/stars/DreamLM/Dream?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Jiacheng Ye, Zhihui Xie, Lin Zheng, Jiahui Gao, Zirui Wu, Xin Jiang, Zhenguo Li, Lingpeng Kong

  **TL;DR:** AR initialization plus context-adaptive token-level noise rescaling; releases Dream-Base and Dream-Instruct (SFT), one of the strongest open instruction-tuned diffusion model baselines. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[08/2025] Seed Diffusion: A Large-Scale Diffusion Language Model with High-Speed Inference</b>
    <a href="https://arxiv.org/abs/2508.02193"><img src="https://img.shields.io/badge/arXiv-2508.02193-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2508.02193"><img src="https://img.shields.io/badge/AlphaXiv-2508.02193-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Yuxuan Song, Zheng Zhang, Cheng Luo, Pengyang Gao, Fan Xia, Hao Luo, Zheng Li, Yuehang Yang, et al.

  **TL;DR:** A large-scale discrete diffusion language model from ByteDance Seed reaching 2146 tokens/s on code tasks via constrained-order parallel decoding and block-wise inference. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[06/2025] Mercury: Ultra-Fast Language Models Based on Diffusion</b>
    <a href="https://arxiv.org/abs/2506.17298"><img src="https://img.shields.io/badge/arXiv-2506.17298-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2506.17298"><img src="https://img.shields.io/badge/AlphaXiv-2506.17298-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Inception Labs, Samar Khanna, Siddhant Kharbanda, Shufan Li, Harshit Varma, Eric Wang, Sawyer Birnbaum, Ziyang Luo, Yanis Miraoui, Akash Palrecha, Stefano Ermon, Aditya Grover, Volodymyr Kuleshov

  **TL;DR:** Technical report of Mercury Coder, a commercial-scale diffusion language model from Inception Labs delivering ultra-fast code generation. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[02/2025] TESS 2: A Large-Scale Generalist Diffusion Language Model</b>
    <a href="https://arxiv.org/abs/2502.13917"><img src="https://img.shields.io/badge/arXiv-2502.13917-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2502.13917"><img src="https://img.shields.io/badge/AlphaXiv-2502.13917-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/hamishivi/tess-2"><img src="https://img.shields.io/github/stars/hamishivi/tess-2?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Jaesung Tae, Hamish Ivison, Sachin Kumar, Arman Cohan

  **TL;DR:** A general instruction-following diffusion language model adapted from a strong AR model via continued pretraining and instruction tuning, introducing modular reward guidance for inference-time alignment. ACL 2025.
  </details>

- <details>
  <summary>
    <b>[02/2025] Large Language Diffusion Models (LLaDA)</b>
    <a href="https://arxiv.org/abs/2502.09992"><img src="https://img.shields.io/badge/arXiv-2502.09992-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2502.09992"><img src="https://img.shields.io/badge/AlphaXiv-2502.09992-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/ML-GSAI/LLaDA"><img src="https://img.shields.io/github/stars/ML-GSAI/LLaDA?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Shen Nie, Fengqi Zhu, Zebin You, Xiaolu Zhang, Jingyang Ou, Jun Hu, Jun Zhou, Yankai Lin, Ji-Rong Wen, Chongxuan Li

  **TL;DR:** An 8B masked diffusion LM trained from scratch plus SFT (noise applied to responses only), demonstrating for the first time that SFT in the diffusion paradigm can match LLaMA3-8B-level instruction following. NeurIPS 2025.
  </details>

## SFT & Instruction Tuning

- <details>
  <summary>
    <b>[09/2026] In-Place Instruction Following in Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2609.07160"><img src="https://img.shields.io/badge/arXiv-2609.07160-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2609.07160"><img src="https://img.shields.io/badge/AlphaXiv-2609.07160-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Zheng Nie, Zherui Li, Jiaming Zhang, Kun Wang, Zhenhong Zhou, Yufei Guo

  **TL;DR:** Formalizes in-place instruction following (IIF) — arbitrary-position anchored constraints unique to dLLMs — builds the hierarchical IIF-Bench, and proposes GRAFT (constraint-aware SFT plus preference optimization) with a +15.35 average improvement. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[06/2026] DreamReasoner-8B: Block-Size Curriculum Learning for Diffusion Reasoning Models</b>
    <a href="https://arxiv.org/abs/2606.19257"><img src="https://img.shields.io/badge/arXiv-2606.19257-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2606.19257"><img src="https://img.shields.io/badge/AlphaXiv-2606.19257-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Zirui Wu, Lin Zheng, Jiacheng Ye, Shansan Gong, Xueliang Zhao, Yansong Feng, Wei Bi, Lingpeng Kong

  **TL;DR:** Systematically studies how block size in training and inference affects long-CoT reasoning of block diffusion models, and proposes block-size curriculum learning. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[06/2026] VoidPadding: Let [VOID] Handle Padding in MDLMs so that [EOS] Can Focus on Semantic Termination</b>
    <a href="https://arxiv.org/abs/2606.17999"><img src="https://img.shields.io/badge/arXiv-2606.17999-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2606.17999"><img src="https://img.shields.io/badge/AlphaXiv-2606.17999-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Chunyu Liu, Zhengyang Fan, Kaisen Yang, Alex Lamb

  **TL;DR:** Decouples padding from semantic termination by introducing a [VOID] token, fixing EOS overflow in large-block decoding of instruction-tuned MDLMs. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[05/2026] Learnability-Informed Fine-Tuning of Diffusion Language Models (LIFT)</b>
    <a href="https://arxiv.org/abs/2605.22939"><img src="https://img.shields.io/badge/arXiv-2605.22939-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2605.22939"><img src="https://img.shields.io/badge/AlphaXiv-2605.22939-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/divelab/LIFT"><img src="https://img.shields.io/github/stars/divelab/LIFT?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Shubham Parashar, Atharv Chagi, Jacob Helwig, Lakshmi Jotsna, Sushil Vemuri, James Caverlee, Dileep Kalathil, Shuiwang Ji

  **TL;DR:** An SFT-based post-training algorithm that aligns learning difficulty with diffusion time steps, improving reasoning in dLLMs without relying on RL. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[04/2026] TRIMS: Trajectory-Ranked Instruction Masked Supervision for Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2604.00666"><img src="https://img.shields.io/badge/arXiv-2604.00666-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2604.00666"><img src="https://img.shields.io/badge/AlphaXiv-2604.00666-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Lingjie Chen, Ruizhong Qiu, Yuyu Fan, Yanjun Zhao, Hanghang Tong

  **TL;DR:** Replaces random masking in SFT with token-difficulty signals and trajectory-aware masking, approaching distillation quality at lower cost. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[10/2025] Rainbow Padding: Mitigating Early Termination in Instruction-Tuned Diffusion LLMs</b>
    <a href="https://arxiv.org/abs/2510.03680"><img src="https://img.shields.io/badge/arXiv-2510.03680-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2510.03680"><img src="https://img.shields.io/badge/AlphaXiv-2510.03680-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/quasar529/rainbow-padding"><img src="https://img.shields.io/github/stars/quasar529/rainbow-padding?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Bumjun Kim, Dongjae Jeon, Dueun Kim, Wonje Jeung, Albert No

  **TL;DR:** A simple remedy for `<eos>` overflow in instruction-tuned dLLMs that uses cyclic distinct padding tokens to prevent early termination and improve length robustness. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[09/2025] GIFT: Guided Importance-Aware Fine-Tuning for Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2509.20863"><img src="https://img.shields.io/badge/arXiv-2509.20863-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2509.20863"><img src="https://img.shields.io/badge/AlphaXiv-2509.20863-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Guowei Xu, Wenxin Xu, Jiawang Zhao, Kaisheng Ma

  **TL;DR:** An importance-aware SFT method that identifies and up-weights the key tokens guiding the generation direction, improving fine-tuning consistency of dLLMs that lack precise per-step probability estimates. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[08/2023] Diffusion Language Models Can Perform Many Tasks with Scaling and Instruction-Finetuning</b>
    <a href="https://arxiv.org/abs/2308.12219"><img src="https://img.shields.io/badge/arXiv-2308.12219-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2308.12219"><img src="https://img.shields.io/badge/AlphaXiv-2308.12219-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/yegcjs/DiffusionLLM"><img src="https://img.shields.io/github/stars/yegcjs/DiffusionLLM?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Jiasheng Ye, Zaixiang Zheng, Yu Bao, Lihua Qian, Quanquan Gu

  **TL;DR:** Scales diffusion language models via masked-language-model pretraining and diffusive adaptation, then unlocks general task solving through task-specific and instruction finetuning, eliciting zero/few-shot in-context learning. arXiv 2023.
  </details>

- <details>
  <summary>
    <b>[10/2022] DiffuSeq: Sequence to Sequence Text Generation with Diffusion Models</b>
    <a href="https://arxiv.org/abs/2210.08933"><img src="https://img.shields.io/badge/arXiv-2210.08933-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2210.08933"><img src="https://img.shields.io/badge/AlphaXiv-2210.08933-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/Shark-NLP/DiffuSeq"><img src="https://img.shields.io/github/stars/Shark-NLP/DiffuSeq?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Shansan Gong, Mukai Li, Jiangtao Feng, Zhiyong Wu, Lingpeng Kong

  **TL;DR:** Casts conditional seq2seq tasks as conditional fine-tuning of a diffusion model; an early representative of task fine-tuning for text diffusion (pre-LLM scale). ICLR 2023.
  </details>

## Preference Optimization

- <details>
  <summary>
    <b>[03/2026] dTRPO: Trajectory Reduction in Policy Optimization of Diffusion Large Language Models</b>
    <a href="https://arxiv.org/abs/2603.18806"><img src="https://img.shields.io/badge/arXiv-2603.18806-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2603.18806"><img src="https://img.shields.io/badge/AlphaXiv-2603.18806-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/facebookresearch/dllm_post_training"><img src="https://img.shields.io/github/stars/facebookresearch/dllm_post_training?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Wenxuan Zhang, Lemeng Wu, Changsheng Zhao, Ernie Chang, Mingchen Zhuge, Zechun Liu, Andy Su, Hanxian Huang, Jun Chen, Chong Zhou, Raghuraman Krishnamoorthi, Vikas Chandra, Mohamed Elhoseiny, Wei Wen

  **TL;DR:** Shows the probability ratio of newly unmasked tokens is an unbiased estimator of interval ratios under reference-policy regularization, drastically cutting trajectory-probability cost for scalable offline preference and policy training. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[02/2026] Entropy Aware Reward Guidance for Diffusion Language Model Alignment (EntRGi)</b>
    <a href="https://arxiv.org/abs/2602.05000"><img src="https://img.shields.io/badge/arXiv-2602.05000-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2602.05000"><img src="https://img.shields.io/badge/AlphaXiv-2602.05000-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Atula Tejaswi, Litu Rout, Constantine Caramanis, Sanjay Shakkottai, Sujay Sanghavi

  **TL;DR:** Ports reward guidance / posterior sampling from continuous diffusion to discrete tokens via an entropy-aware mechanism for dLLM alignment. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[10/2025] Aligning Diffusion Language Models via Unpaired Preference Optimization (ELBO-KTO)</b>
    <a href="https://arxiv.org/abs/2510.23658"><img src="https://img.shields.io/badge/arXiv-2510.23658-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2510.23658"><img src="https://img.shields.io/badge/AlphaXiv-2510.23658-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/vaibhavjindal/elbo-kto"><img src="https://img.shields.io/github/stars/vaibhavjindal/elbo-kto?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Vaibhav Jindal, Hejian Sang, Chun-Mao Lai, Yanning Chen, Zhipeng Wang

  **TL;DR:** Combines an ELBO surrogate for intractable diffusion log-likelihoods with the unpaired, prospect-theoretic KTO objective plus variance-reduction practices, establishing unpaired preference optimization as a viable alternative to pairwise alignment on LLaDA-8B-Instruct. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[05/2025] LLaDA 1.5: Variance-Reduced Preference Optimization for Large Language Diffusion Models (VRPO)</b>
    <a href="https://arxiv.org/abs/2505.19223"><img src="https://img.shields.io/badge/arXiv-2505.19223-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2505.19223"><img src="https://img.shields.io/badge/AlphaXiv-2505.19223-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/ML-GSAI/LLaDA-1.5"><img src="https://img.shields.io/github/stars/ML-GSAI/LLaDA-1.5?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Fengqi Zhu, Rongzhen Wang, Shen Nie, Xiaolu Zhang, Chunwei Wu, Jun Hu, Jun Zhou, Jianfei Chen, Yankai Lin, Ji-Rong Wen, Chongxuan Li

  **TL;DR:** Formally analyzes the variance of ELBO-based likelihood estimates for MDM preference optimization and introduces unbiased variance reduction (optimal Monte Carlo budget allocation, antithetic sampling); the resulting LLaDA 1.5 significantly improves over its SFT-only predecessor on math, code, and alignment benchmarks. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[03/2025] Preference-Based Alignment of Discrete Diffusion Models (D2-DPO)</b>
    <a href="https://arxiv.org/abs/2503.08295"><img src="https://img.shields.io/badge/arXiv-2503.08295-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2503.08295"><img src="https://img.shields.io/badge/AlphaXiv-2503.08295-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Umberto Borso, Davide Paglieri, Jude Wells, Tim Rocktäschel

  **TL;DR:** The first adaptation of DPO to discrete diffusion models formulated as continuous-time Markov chains, deriving a loss that aligns the generative process with preference data while preserving fidelity to a reference distribution, without explicit reward models. arXiv 2025.
  </details>

## RL & Reasoning

- <details>
  <summary>
    <b>[08/2026] Beyond On-Policy Exploration: Integrating External Policy Rollouts for Reinforcement Learning in Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2608.01717"><img src="https://img.shields.io/badge/arXiv-2608.01717-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2608.01717"><img src="https://img.shields.io/badge/AlphaXiv-2608.01717-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Wonseok Lee, Jimyeong Kim, Jungmin Ko, Wonjong Rhee

  **TL;DR:** Mixes high-reward rollouts from a stronger external policy when on-policy successes are scarce, addressing length mismatch and training instability. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[07/2026] Mask-Aware Policy Gradients for Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2607.15200"><img src="https://img.shields.io/badge/arXiv-2607.15200-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2607.15200"><img src="https://img.shields.io/badge/AlphaXiv-2607.15200-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/Haran71/mask-aware-policy-gradients"><img src="https://img.shields.io/github/stars/Haran71/mask-aware-policy-gradients?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Haran Raajesh, Kulin Shah, Adam Klivans, Philipp Krähenbühl

  **TL;DR:** Formalizes MDLM generation as a two-stage action MDP over what tokens to place and which positions to remask, decomposing the policy gradient into token and masking terms; optimizing both yields state-of-the-art results on math reasoning and coding (87.1% GSM8K, 53.4% MBPP). COLM 2026.
  </details>

- <details>
  <summary>
    <b>[07/2026] A Continuous-Time Reinforcement Learning Framework for Fine-Tuning Discrete Diffusion Models</b>
    <a href="https://arxiv.org/abs/2607.14522"><img src="https://img.shields.io/badge/arXiv-2607.14522-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2607.14522"><img src="https://img.shields.io/badge/AlphaXiv-2607.14522-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Zikun Zhang, Jiayuan Sheng, David D. Yao, Wenpin Tang

  **TL;DR:** Formulates RL for discrete diffusion in continuous time via controlled CTMCs, deriving continuous-time PPO/GRPO variants that incorporate intermediate rewards along the denoising trajectory, with tractable policy parameterizations and trajectory subsampling for efficient dLLM post-training on math and code. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[07/2026] SLIM-RL: Risk-Budgeted Random-Masking RL for Diffusion LLMs Without Trajectory Slicing</b>
    <a href="https://arxiv.org/abs/2607.00208"><img src="https://img.shields.io/badge/arXiv-2607.00208-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2607.00208"><img src="https://img.shields.io/badge/AlphaXiv-2607.00208-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Ruikang Zhao, Zhenting Wang, Han Gao, Ligong Han

  **TL;DR:** Addresses TraceRL's trajectory-slicing cost scaling with block size via a τ-budget decoder that bounds commit risk plus a trajectory-free random-masking objective. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[06/2026] DiPOD: Diffusion Policy Optimization without Drifting Apart</b>
    <a href="https://arxiv.org/abs/2606.13795"><img src="https://img.shields.io/badge/arXiv-2606.13795-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2606.13795"><img src="https://img.shields.io/badge/AlphaXiv-2606.13795-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/Astro-Eric/DiPOD-release"><img src="https://img.shields.io/github/stars/Astro-Eric/DiPOD-release?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Haozhe Jiang, Haiwen Feng, Pieter Abbeel, Jiantao Jiao, Angjoo Kanazawa, Nika Haghtalab

  **TL;DR:** Identifies a "double drift" between ELBO surrogates and true log-likelihoods that derails policy gradients, and proposes a stable and reliable diffusion policy optimization method. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[06/2026] Back on Track: Aligning Rewards and States for Reasoning in Diffusion LLMs (PAPO)</b>
    <a href="https://arxiv.org/abs/2606.08501"><img src="https://img.shields.io/badge/arXiv-2606.08501-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2606.08501"><img src="https://img.shields.io/badge/AlphaXiv-2606.08501-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Yawen Shao, Jie Xiao, Kai Zhu, Yu Liu, Hongchen Luo, Xueyang Fu, Yang Cao, Wei Zhai, Zheng-Jun Zha

  **TL;DR:** Targets the dual mismatch of indiscriminate terminal-reward assignment and off-track state updates via step-aware process rewards for trajectory-aligned RL. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[06/2026] Read the Trace, Steer the Path: Trajectory-Aware Reinforcement Learning for Diffusion Language Models (CAPR)</b>
    <a href="https://arxiv.org/abs/2606.04396"><img src="https://img.shields.io/badge/arXiv-2606.04396-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2606.04396"><img src="https://img.shields.io/badge/AlphaXiv-2606.04396-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Anant Khandelwal, Manish Gupta

  **TL;DR:** Compresses denoising traces into path states and generates cheap sibling continuations from cached trajectories, obtaining tree-like fine-grained supervision at non-tree cost. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[05/2026] Masked Diffusion Language Models are Strong and Steerable Text-Based World Models for Agentic RL</b>
    <a href="https://arxiv.org/abs/2607.16204"><img src="https://img.shields.io/badge/arXiv-2607.16204-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2607.16204"><img src="https://img.shields.io/badge/AlphaXiv-2607.16204-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Darshan Deshpande

  **TL;DR:** Fine-tunes MDLMs as steerable text-based world models that serve as training environments for agentic RL. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[05/2026] GDSD: Reinforcement Learning as Guided Denoiser Self-Distillation for Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2605.29398"><img src="https://img.shields.io/badge/arXiv-2605.29398-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2605.29398"><img src="https://img.shields.io/badge/AlphaXiv-2605.29398-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/GaryBall/GDSD"><img src="https://img.shields.io/github/stars/GaryBall/GDSD?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Xiaohang Tang, Keyue Jiang, Che Liu, Qifang Zhao, Xiaoxiao Xu, Sangwoong Yoon, Ilija Bogunovic

  **TL;DR:** Reframes dLLM RL as guided denoiser self-distillation, sidestepping the train-inference mismatch bias of ELBO likelihood surrogates. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[05/2026] DACA-GRPO: Denoising-Aware Credit Assignment for Reinforcement Learning in Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2605.16342"><img src="https://img.shields.io/badge/arXiv-2605.16342-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2605.16342"><img src="https://img.shields.io/badge/AlphaXiv-2605.16342-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Amin Karimi Monsefi, Dominic Culver, Nikhil Bhendawade, Lokesh Boominathan, Manuel R. Ciosici, Yizhe Zhang, Irina Belousova

  **TL;DR:** A plug-and-play GRPO enhancement tackling missing temporal credit assignment and mean-field likelihood bias via Denoising Progress Scores and Stratified Masking Likelihood, consistently improving three GRPO base methods across seven math, code, and constraint-satisfaction benchmarks. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[05/2026] Relative Score Policy Optimization for Diffusion Language Models (RSPO)</b>
    <a href="https://arxiv.org/abs/2605.10218"><img src="https://img.shields.io/badge/arXiv-2605.10218-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2605.10218"><img src="https://img.shields.io/badge/AlphaXiv-2605.10218-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Zichao Yu, Shengze Xu, Bingqing Jiang, Wenyi Zhang, Difan Zou

  **TL;DR:** Replaces intractable likelihoods with relative scores for group-based policy optimization of diffusion language models. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[03/2026] Training Diffusion Language Models for Black-Box Optimization (DiBO)</b>
    <a href="https://arxiv.org/abs/2603.17919"><img src="https://img.shields.io/badge/arXiv-2603.17919-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2603.17919"><img src="https://img.shields.io/badge/AlphaXiv-2603.17919-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/zpointS/DiBO"><img src="https://img.shields.io/github/stars/zpointS/DiBO?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Zipeng Sun, Can Chen, Ye Yuan, Haolun Wu, Jiayao Gu, Christopher Pal, Xue Liu

  **TL;DR:** A two-stage post-training pipeline (SFT + alignment) enabling diffusion LLMs to generate high-scoring designs for black-box optimization in robotics and DNA design. ICML 2026 Spotlight.
  </details>

- <details>
  <summary>
    <b>[03/2026] LightningRL: Breaking the Accuracy-Parallelism Trade-off of Block-wise dLLMs via Reinforcement Learning</b>
    <a href="https://arxiv.org/abs/2603.13319"><img src="https://img.shields.io/badge/arXiv-2603.13319-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2603.13319"><img src="https://img.shields.io/badge/AlphaXiv-2603.13319-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Yanzhe Hu, Yijie Jin, Pengfei Liu, Kai Yu, Zhijie Deng

  **TL;DR:** Uses RL to break the accuracy-parallelism trade-off of block-wise dLLMs, complementary to dUltra. ICML 2026.
  </details>

- <details>
  <summary>
    <b>[03/2026] Reinforcement Learning for Diffusion LLMs with Entropy-Guided Step Selection and Stepwise Advantages (EGSPO)</b>
    <a href="https://arxiv.org/abs/2603.12554"><img src="https://img.shields.io/badge/arXiv-2603.12554-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2603.12554"><img src="https://img.shields.io/badge/AlphaXiv-2603.12554-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/vishnutez/egspo-dllm-rl"><img src="https://img.shields.io/github/stars/vishnutez/egspo-dllm-rl?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Vishnu Teja Kunde, Fatemeh Doudi, Mahdi Farahbakhsh, Dileep Kalathil, Krishna Narayanan, Jean-Francois Chamberland

  **TL;DR:** Entropy-guided selection of critical denoising steps combined with stepwise advantages, reducing the variance and cost of dLLM RL. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[03/2026] Stabilizing Reinforcement Learning for Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2603.06743"><img src="https://img.shields.io/badge/arXiv-2603.06743-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2603.06743"><img src="https://img.shields.io/badge/AlphaXiv-2603.06743-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Jianyuan Zhong, Kaibo Wang, Ding Ding, Zijin Feng, Haoli Bai, Yang Xiang, Jiacheng Sun, Qiang Xu

  **TL;DR:** Diagnoses reward collapse when GRPO is directly applied to dLLMs (noisy importance ratios and group advantage defects) and provides stabilization fixes. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[03/2026] LFPO: Likelihood-Free Policy Optimization for Masked Diffusion Models</b>
    <a href="https://arxiv.org/abs/2603.01563"><img src="https://img.shields.io/badge/arXiv-2603.01563-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2603.01563"><img src="https://img.shields.io/badge/AlphaXiv-2603.01563-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Chenxing Wei, Jiazhen Kang, Hong Wang, Jianqing Zhang, Hao Jiang, Xiaolong Xu, Ningyuan Sun, Ying He, F. Richard Yu, Yao Shu, Bo Jiang

  **TL;DR:** A fully likelihood-free RLVR policy optimization method that sidesteps the high-variance likelihood approximations of prior dLLM RL approaches. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[02/2026] Efficient and Stable Reinforcement Learning for Diffusion Language Models (STP)</b>
    <a href="https://arxiv.org/abs/2602.08905"><img src="https://img.shields.io/badge/arXiv-2602.08905-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2602.08905"><img src="https://img.shields.io/badge/AlphaXiv-2602.08905-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Jiawei Liu, Xiting Wang, Yuanyuan Zhong, Defu Lian, Yu Yang

  **TL;DR:** A spatiotemporal pruning framework that compresses generation redundancy in dLLMs, improving both RL efficiency and stability. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[02/2026] Diffusion-State Policy Optimization for Masked Diffusion Language Models (DiSPO)</b>
    <a href="https://arxiv.org/abs/2602.06462"><img src="https://img.shields.io/badge/arXiv-2602.06462-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2602.06462"><img src="https://img.shields.io/badge/AlphaXiv-2602.06462-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Daisuke Oba, Hiroki Furuta, Naoaki Okazaki

  **TL;DR:** A plug-in credit-assignment layer that branches at intermediate masked states from rollout-cached logits and updates only newly filled tokens, consistently improving terminal-feedback baselines such as diffu-GRPO and SPG on math and planning under matched rollout compute. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[01/2026] The Flexibility Trap: Rethinking the Value of Arbitrary Order in Diffusion Language Models (JustGRPO)</b>
    <a href="https://arxiv.org/abs/2601.15165"><img src="https://img.shields.io/badge/arXiv-2601.15165-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2601.15165"><img src="https://img.shields.io/badge/AlphaXiv-2601.15165-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/LeapLabTHU/JustGRPO"><img src="https://img.shields.io/github/stars/LeapLabTHU/JustGRPO?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Zanlin Ni, Shenzhi Wang, Yang Yue, Tianyu Yu, Weilin Zhao, Yeguo Hua, Tianyi Chen, Jun Song, Cheng Yu, Bo Zheng, Gao Huang

  **TL;DR:** Argues that arbitrary-order flexibility is not necessary: a straightforward GRPO transplant matches complex diffusion-specific RL modifications (using ESPO as the comparison baseline). arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[01/2026] T\*: Progressive Block Scaling for Masked Diffusion Language Models Through Trajectory Aware Reinforcement Learning</b>
    <a href="https://arxiv.org/abs/2601.11214"><img src="https://img.shields.io/badge/arXiv-2601.11214-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2601.11214"><img src="https://img.shields.io/badge/AlphaXiv-2601.11214-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Hanchen Xia, Baoyou Chen, Yutang Ge, Guojiang Zhao, Siyu Zhu

  **TL;DR:** A curriculum-style progressive block-size scaling training scheme built on TraceRL for masked diffusion language models. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[12/2025] Co-GRPO: Co-Optimized Group Relative Policy Optimization for Masked Diffusion Model</b>
    <a href="https://arxiv.org/abs/2512.22288"><img src="https://img.shields.io/badge/arXiv-2512.22288-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2512.22288"><img src="https://img.shields.io/badge/AlphaXiv-2512.22288-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Renping Zhou, Zanlin Ni, Tianyi Chen, Zeyu Liu, Yang Yue, Yulin Wang, Yuxuan Wang, Jingshu Liu, Gao Huang

  **TL;DR:** Jointly optimizes the model and the decoding schedule (how many tokens to decode per step), bridging MDM training-inference discrepancies. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[12/2025] dUltra: Ultra-Fast Diffusion Large Language Models via Reinforcement Learning</b>
    <a href="https://arxiv.org/abs/2512.21446"><img src="https://img.shields.io/badge/arXiv-2512.21446-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2512.21446"><img src="https://img.shields.io/badge/AlphaXiv-2512.21446-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/chinsengi/dUltra-os"><img src="https://img.shields.io/github/stars/chinsengi/dUltra-os?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Shirui Chen, Jiantao Jiao, Lillian J. Ratliff, Banghua Zhu

  **TL;DR:** Uses GRPO to learn a "path planner" over unmasking order and parallelism, greatly accelerating diffusion LLM decoding while preserving quality. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[12/2025] d-TreeRPO: Towards More Reliable Policy Optimization for Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2512.09675"><img src="https://img.shields.io/badge/arXiv-2512.09675-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2512.09675"><img src="https://img.shields.io/badge/AlphaXiv-2512.09675-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/THU-BPM/d-TreeRPO"><img src="https://img.shields.io/github/stars/THU-BPM/d-TreeRPO?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Leyi Pan, Shuchang Tao, Yunpeng Zhai, Zheyu Fu, Liancheng Fang, Minghua He, Lingzhe Zhang, Zhaoyang Liu, Bolin Ding, Aiwei Liu, Lijie Wen

  **TL;DR:** Tree-structured grouping and rollout organization improves the reliability of dLLM policy optimization. ACL 2026 Main.
  </details>

- <details>
  <summary>
    <b>[12/2025] Learning Unmasking Policies for Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2512.09106"><img src="https://img.shields.io/badge/arXiv-2512.09106-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2512.09106"><img src="https://img.shields.io/badge/AlphaXiv-2512.09106-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/apple/ml-rl-dllm"><img src="https://img.shields.io/github/stars/apple/ml-rl-dllm?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Metod Jazbec, Theo X. Olausson, Louis Béthune, Pierre Ablin, Michael Kirchhof, João Monteiro, Victor Turrisi, Jason Ramapuram, Marco Cuturi

  **TL;DR:** Uses RL to learn a standalone unmasking-order policy module instead of fixed confidence-based sampling, in the lineage of DCoLT/UPM. ICML 2026 (oral spotlight).
  </details>

- <details>
  <summary>
    <b>[12/2025] Principled RL for Diffusion LLMs Emerges from a Sequence-Level Perspective (ESPO)</b>
    <a href="https://arxiv.org/abs/2512.03759"><img src="https://img.shields.io/badge/arXiv-2512.03759-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2512.03759"><img src="https://img.shields.io/badge/AlphaXiv-2512.03759-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/ML-GSAI/ESPO"><img src="https://img.shields.io/github/stars/ML-GSAI/ESPO?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Jingyang Ou, Jiaqi Han, Minkai Xu, Shaoxuan Xu, Jianwen Xie, Stefano Ermon, Yi Wu, Chongxuan Li

  **TL;DR:** Treats the entire sequence generation as a single action, using the ELBO as a sequence-level likelihood surrogate with per-token normalized importance ratios; +20–40 points over token-level baselines on Countdown. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[10/2025] MRO: Enhancing Reasoning in Diffusion Language Models via Multi-Reward Optimization</b>
    <a href="https://arxiv.org/abs/2510.21473"><img src="https://img.shields.io/badge/arXiv-2510.21473-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2510.21473"><img src="https://img.shields.io/badge/AlphaXiv-2510.21473-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Chenglong Wang, Yang Gan, Hang Zhou, Chi Hu, Yongyu Mu, Kai Song, Murun Yang, Bei Li, Chunliang Zhang, Tongran Liu, Jingbo Zhu, Zhengtao Yu, Tong Xiao

  **TL;DR:** Joint multi-reward optimization to improve dLLM reasoning. NeurIPS 2025.
  </details>

- <details>
  <summary>
    <b>[10/2025] Boundary-Guided Policy Optimization for Memory-Efficient RL of Diffusion Large Language Models (BGPO)</b>
    <a href="https://arxiv.org/abs/2510.11683"><img src="https://img.shields.io/badge/arXiv-2510.11683-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2510.11683"><img src="https://img.shields.io/badge/AlphaXiv-2510.11683-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/THU-KEG/BGPO"><img src="https://img.shields.io/github/stars/THU-KEG/BGPO?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Nianyi Lin, Jiajie Zhang, Lei Hou, Juanzi Li

  **TL;DR:** Exploits the boundary structure of block diffusion to maximize a linear lower bound of the ELBO, significantly reducing RL training memory. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[10/2025] SPG: Sandwiched Policy Gradient for Masked Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2510.09541"><img src="https://img.shields.io/badge/arXiv-2510.09541-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2510.09541"><img src="https://img.shields.io/badge/AlphaXiv-2510.09541-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/facebookresearch/SPG"><img src="https://img.shields.io/github/stars/facebookresearch/SPG?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Chenyu Wang, Paria Rashidinejad, DiJia Su, Song Jiang, Sid Wang, Siyan Zhao, Cai Zhou, Shannon Zejiang Shen, Feiyu Chen, Tommi Jaakkola, Yuandong Tian, Bo Liu

  **TL;DR:** Constructs a "sandwich" objective from log-likelihood upper and lower bounds for policy gradients, significantly outperforming ELBO-based methods (d1/wd1). ICLR 2026.
  </details>

- <details>
  <summary>
    <b>[10/2025] Improving Reasoning for Diffusion Language Models via Group Diffusion Policy Optimization (GDPO)</b>
    <a href="https://arxiv.org/abs/2510.08554"><img src="https://img.shields.io/badge/arXiv-2510.08554-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2510.08554"><img src="https://img.shields.io/badge/AlphaXiv-2510.08554-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Kevin Rojas, Jiahe Lin, Kashif Rasul, Anderson Schneider, Yuriy Nevmyvaka, Molei Tao, Wei Deng

  **TL;DR:** A diffusion adaptation of GRPO that improves how group-relative advantages are assigned across denoising steps, surpassing diffu-GRPO. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[10/2025] Enhancing Reasoning for Diffusion LLMs via Distribution Matching Policy Optimization (DMPO)</b>
    <a href="https://arxiv.org/abs/2510.08233"><img src="https://img.shields.io/badge/arXiv-2510.08233-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2510.08233"><img src="https://img.shields.io/badge/AlphaXiv-2510.08233-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/yuchen-zhu-zyc/DMPO"><img src="https://img.shields.io/github/stars/yuchen-zhu-zyc/DMPO?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Yuchen Zhu, Wei Guo, Jaemoo Choi, Petr Molodyk, Bo Yuan, Molei Tao, Yongxin Chen

  **TL;DR:** Formulates RL as a distribution matching problem, avoiding direct estimation of intractable likelihoods. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[10/2025] Simple Policy Gradients for Reasoning with Diffusion Language Models (AGRPO)</b>
    <a href="https://arxiv.org/abs/2510.04019"><img src="https://img.shields.io/badge/arXiv-2510.04019-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2510.04019"><img src="https://img.shields.io/badge/AlphaXiv-2510.04019-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/probablyabot/agrpo"><img src="https://img.shields.io/github/stars/probablyabot/agrpo?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Anthony Zhan

  **TL;DR:** Amortized Group Relative Policy Optimization leverages the Markovian nature of dLLMs, optimizing individual denoising steps rather than full sequences and avoiding biased sequence-level likelihood approximations. ICML 2026.
  </details>

- <details>
  <summary>
    <b>[10/2025] Consolidating Reinforcement Learning for Multimodal Discrete Diffusion Models (MaskGRPO)</b>
    <a href="https://arxiv.org/abs/2510.02880"><img src="https://img.shields.io/badge/arXiv-2510.02880-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2510.02880"><img src="https://img.shields.io/badge/AlphaXiv-2510.02880-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/martian422/MaskGRPO"><img src="https://img.shields.io/github/stars/martian422/MaskGRPO?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Tianren Ma, Mu Zhang, Yibing Wang, Qixiang Ye

  **TL;DR:** A unified GRPO training framework consolidating RL for LLaDA/MMaDA-style multimodal discrete diffusion models. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[10/2025] DiFFPO: Training Diffusion LLMs to Reason Fast and Furious via Reinforcement Learning</b>
    <a href="https://arxiv.org/abs/2510.02212"><img src="https://img.shields.io/badge/arXiv-2510.02212-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2510.02212"><img src="https://img.shields.io/badge/AlphaXiv-2510.02212-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Hanyang Zhao, Dawen Liang, Wenpin Tang, David Yao, Nathan Kallus

  **TL;DR:** A unified RL framework that jointly trains the model and the sampler policy, improving both reasoning accuracy and latency and pushing the accuracy/compute Pareto frontier. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[10/2025] Advancing Reasoning in Diffusion Language Models with Denoising Process Rewards</b>
    <a href="https://arxiv.org/abs/2510.01544"><img src="https://img.shields.io/badge/arXiv-2510.01544-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2510.01544"><img src="https://img.shields.io/badge/AlphaXiv-2510.01544-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Shaoan Xie, Lingjing Kong, Xiangchen Song, Xinshuai Dong, Guangyi Chen, Eric P. Xing, Kun Zhang

  **TL;DR:** Introduces denoising-process rewards that directly supervise intermediate denoising steps, guiding dLLMs toward progressively better-structured reasoning instead of outcome-only rewards. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[09/2025] Taming Masked Diffusion Language Models via Consistency Trajectory Reinforcement Learning with Fewer Decoding Steps (CJ-GRPO)</b>
    <a href="https://arxiv.org/abs/2509.23924"><img src="https://img.shields.io/badge/arXiv-2509.23924-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2509.23924"><img src="https://img.shields.io/badge/AlphaXiv-2509.23924-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/yjyddq/EOSER-ASS-RL"><img src="https://img.shields.io/github/stars/yjyddq/EOSER-ASS-RL?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Jingyi Yang, Guanxu Chen, Xuhao Hu, Jing Shao

  **TL;DR:** Enforces consistency between rollout and optimization trajectories, resolving the train-inference mismatch between MDLM non-causal decoding and AR-style RL. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[09/2025] Inpainting-Guided Policy Optimization for Diffusion Large Language Models (IGPO)</b>
    <a href="https://arxiv.org/abs/2509.10396"><img src="https://img.shields.io/badge/arXiv-2509.10396-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2509.10396"><img src="https://img.shields.io/badge/AlphaXiv-2509.10396-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/facebookresearch/igpo"><img src="https://img.shields.io/github/stars/facebookresearch/igpo?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Siyan Zhao, Mengchen Liu, Jing Huang, Miao Liu, Chenyu Wang, Bo Liu, Yuandong Tian, Guan Pang, Sean Bell, Aditya Grover, Feiyu Chen

  **TL;DR:** Leverages the partial inpainting ability of diffusion models to inject partial ground-truth answer fragments into rollouts, easing exploration under sparse rewards. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[09/2025] Revolutionizing Reinforcement Learning Framework for Diffusion Large Language Models (TraceRL / TraDo)</b>
    <a href="https://arxiv.org/abs/2509.06949"><img src="https://img.shields.io/badge/arXiv-2509.06949-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2509.06949"><img src="https://img.shields.io/badge/AlphaXiv-2509.06949-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/Gen-Verse/dLLM-RL"><img src="https://img.shields.io/github/stars/Gen-Verse/dLLM-RL?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Yinjie Wang, Ling Yang, Bowen Li, Ye Tian, Ke Shen, Mengdi Wang

  **TL;DR:** Trajectory-aware RL aligning the training objective with the model's actual inference trajectory, with a diffusion value model for variance reduction; yields TraDo-4B/8B and the first long-CoT diffusion model TraDo-8B-Thinking. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[08/2025] MDPO: Overcoming the Training-Inference Divide of Masked Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2508.13148"><img src="https://img.shields.io/badge/arXiv-2508.13148-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2508.13148"><img src="https://img.shields.io/badge/AlphaXiv-2508.13148-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/autonomousvision/mdpo"><img src="https://img.shields.io/github/stars/autonomousvision/mdpo?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Haoyu He, Katrin Renz, Yong Cao, Andreas Geiger

  **TL;DR:** Optimizes the policy following the progressive refinement schedule used at inference, bridging the MDLM training-inference gap. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[07/2025] wd1: Weighted Policy Optimization for Reasoning in Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2507.08838"><img src="https://img.shields.io/badge/arXiv-2507.08838-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2507.08838"><img src="https://img.shields.io/badge/AlphaXiv-2507.08838-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/xiaohangt/wd1"><img src="https://img.shields.io/github/stars/xiaohangt/wd1?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Xiaohang Tang, Rares Dolga, Sangwoong Yoon, Ilija Bogunovic

  **TL;DR:** Reweights low-advantage samples instead of discarding them, improving diffu-GRPO's sample efficiency and compute cost; surpasses d1 on GSM8K/MATH/Sudoku/Countdown. ICLR 2026.
  </details>

- <details>
  <summary>
    <b>[05/2025] Reinforcing the Diffusion Chain of Lateral Thought with Diffusion Language Models (DCoLT)</b>
    <a href="https://arxiv.org/abs/2505.10446"><img src="https://img.shields.io/badge/arXiv-2505.10446-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2505.10446"><img src="https://img.shields.io/badge/AlphaXiv-2505.10446-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/maple-research-lab/LLaDOU"><img src="https://img.shields.io/github/stars/maple-research-lab/LLaDOU?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Zemin Huang, Zhiyang Chen, Zijun Wang, Tiancheng Li, Guo-Jun Qi

  **TL;DR:** Treats intermediate reverse-sampling steps as "thinking actions" and optimizes the entire denoising trajectory with outcome-reward RL; proposes the Unmask Policy Module on LLaDA with Plackett-Luce modeling of unmasking order. NeurIPS 2025.
  </details>

- <details>
  <summary>
    <b>[04/2025] d1: Scaling Reasoning in Diffusion Large Language Models via Reinforcement Learning</b>
    <a href="https://arxiv.org/abs/2504.12216"><img src="https://img.shields.io/badge/arXiv-2504.12216-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2504.12216"><img src="https://img.shields.io/badge/AlphaXiv-2504.12216-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/dllm-reasoning/d1"><img src="https://img.shields.io/github/stars/dllm-reasoning/d1?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Siyan Zhao, Devaansh Gupta, Qinqing Zheng, Aditya Grover

  **TL;DR:** Proposes diffu-GRPO, using mean-field approximation and random prompt masking to estimate sequence/token log-probabilities in a single forward pass; a two-stage SFT+RL recipe greatly improves LLaDA's math/planning reasoning — a foundational work of dLLM RL. NeurIPS 2025.
  </details>

- <details>
  <summary>
    <b>[02/2025] Fine-Tuning Discrete Diffusion Models with Policy Gradient Methods (SEPO)</b>
    <a href="https://arxiv.org/abs/2502.01384"><img src="https://img.shields.io/badge/arXiv-2502.01384-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2502.01384"><img src="https://img.shields.io/badge/AlphaXiv-2502.01384-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/ozekri/SEPO"><img src="https://img.shields.io/github/stars/ozekri/SEPO?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Oussama Zekri, Nicolas Boullé

  **TL;DR:** An early systematic application of policy gradient methods to fine-tune discrete diffusion models. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[10/2024] DRAKES: Fine-Tuning Discrete Diffusion Models via Reward Optimization with Applications to DNA and Protein Design</b>
    <a href="https://arxiv.org/abs/2410.13643"><img src="https://img.shields.io/badge/arXiv-2410.13643-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2410.13643"><img src="https://img.shields.io/badge/AlphaXiv-2410.13643-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/ChenyuWang-Monica/DRAKES"><img src="https://img.shields.io/github/stars/ChenyuWang-Monica/DRAKES?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Chenyu Wang, Masatoshi Uehara, Yichun He, Amy Wang, Tommaso Biancalani, Avantika Lal, Tommi Jaakkola, Sergey Levine, Hanchen Wang, Aviv Regev

  **TL;DR:** A reward fine-tuning framework that backpropagates rewards through the entire reverse chain of discrete diffusion, demonstrated on DNA/protein design and directly applicable to text MDMs. ICLR 2025.
  </details>

## Safety & Alignment

- <details>
  <summary>
    <b>[09/2026] Membership Inference in Fine-tuned Diffusion Language Models via Token-level Memorization Asymmetry (Q-Skew)</b>
    <a href="https://arxiv.org/abs/2609.00873"><img src="https://img.shields.io/badge/arXiv-2609.00873-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2609.00873"><img src="https://img.shields.io/badge/AlphaXiv-2609.00873-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Shengfang Zhai, Leo Marchyok, Yuling Shi, Huanran Chen, Yinpeng Dong, Jiaheng Zhang, Sanghyun Hong

  **TL;DR:** Derives a token-level memorization asymmetry phenomenon from diffusion training dynamics and proposes the Q-Skew metric for membership inference and PII extraction attacks on fine-tuned DLMs. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[08/2026] Beyond Token Positions: Safety Alignment Across Denoising Steps in Diffusion Language Models (RAEC)</b>
    <a href="https://arxiv.org/abs/2609.00495"><img src="https://img.shields.io/badge/arXiv-2609.00495-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2609.00495"><img src="https://img.shields.io/badge/AlphaXiv-2609.00495-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Guoli Wang, Haonan Shi, Tu Ouyang, An Wang

  **TL;DR:** Traces refusal signals along denoising steps, finding they concentrate in early steps and front positions, and proposes training-free Refusal-Aware Early Commitment decoding to lower attack success rates. EMNLP 2026.
  </details>

- <details>
  <summary>
    <b>[08/2026] Diffusion LLMs as Targets and Adversaries: Mechanistic Safety Exploits</b>
    <a href="https://arxiv.org/abs/2608.07430"><img src="https://img.shields.io/badge/arXiv-2608.07430-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2608.07430"><img src="https://img.shields.io/badge/AlphaXiv-2608.07430-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Elena Dumitrescu, Gert Lek, Lydia Y. Chen, Jérémie Decouchant

  **TL;DR:** Mechanistically shows that AR-to-dLLM converted models inherit "safety neuron footprints" from their source models, which can be exploited by transfer attacks. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[05/2026] D²-Monitor: Dynamic Safety Monitoring for Diffusion LLMs via Hesitation-Aware Routing</b>
    <a href="https://arxiv.org/abs/2605.25893"><img src="https://img.shields.io/badge/arXiv-2605.25893-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2605.25893"><img src="https://img.shields.io/badge/AlphaXiv-2605.25893-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Aoxi Liu, Yupeng Chen, James Oldfield, Guanzhe Hong, Junchi Yu, Baoyuan Wu, Philip Torr, Adel Bibi

  **TL;DR:** Predicts probe failures from "safety hesitation" steps in intermediate denoising hidden states via a two-layer dynamic-routing safety monitor (≤0.85M parameters). arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[05/2026] Backdooring Masked Diffusion Language Models (ShadowMask)</b>
    <a href="https://arxiv.org/abs/2605.19262"><img src="https://img.shields.io/badge/arXiv-2605.19262-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2605.19262"><img src="https://img.shields.io/badge/AlphaXiv-2605.19262-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Daniel Yiming Cao, Chengzhong Wang, Sheng-Yen Chou, Chengyu Huang, Pin-Yu Chen, Shengwei An

  **TL;DR:** The first training-time backdoor attack on MDLMs, corrupting the terminal prior of the forward process; achieves near-100% ASR on LLaDA-8B and survives PEFT fine-tuning. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[05/2026] Adaptive Steering and Remasking for Safe Generation in Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2605.13043"><img src="https://img.shields.io/badge/arXiv-2605.13043-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2605.13043"><img src="https://img.shields.io/badge/AlphaXiv-2605.13043-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Yejin Lee, Yo-Sub Han

  **TL;DR:** Defends against harmful-token propagation at intermediate denoising steps via adaptive steering combined with remasking. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[05/2026] GPO-V: Jailbreak Diffusion Vision Language Model by Global Probability Optimization</b>
    <a href="https://arxiv.org/abs/2605.07399"><img src="https://img.shields.io/badge/arXiv-2605.07399-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2605.07399"><img src="https://img.shields.io/badge/AlphaXiv-2605.07399-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Yu Pan, Andi Zhang, Yi Wang, Sibei Yang, Wenjie Wang

  **TL;DR:** The first visual-modality jailbreak framework against diffusion VLMs, optimizing over denoising trajectories and exposing a "progressive refusal" failure mode with strong cross-model transferability. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[02/2026] Self-Purification Mitigates Backdoors in Multimodal Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2602.22246"><img src="https://img.shields.io/badge/arXiv-2602.22246-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2602.22246"><img src="https://img.shields.io/badge/AlphaXiv-2602.22246-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Guangnian Wan, Qi Li, Gongfan Fang, Xinyin Ma, Xinchao Wang

  **TL;DR:** Shows that data poisoning can implant backdoors into multimodal DLMs and defends against them via the model's own self-purification mechanism. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[01/2026] Safer by Diffusion, Broken by Context: Diffusion LLM's Safety Blessing and Its Failure Mode</b>
    <a href="https://arxiv.org/abs/2602.00388"><img src="https://img.shields.io/badge/arXiv-2602.00388-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2602.00388"><img src="https://img.shields.io/badge/AlphaXiv-2602.00388-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Zeyuan He, Yupeng Chen, Lang Lin, Yihan Wang, Shenxu Chang, Eric Sommerlade, Philip Torr, Junchi Yu, Adel Bibi, Jialin Yu

  **TL;DR:** Analyzes dLLMs' inherent robustness to autoregressive jailbreaks (denoising gradually suppresses attacks) and introduces context-nesting attacks that jailbreak Gemini Diffusion for the first time. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[10/2025] Toward Safer Diffusion Language Models: Discovery and Mitigation of Priming Vulnerability</b>
    <a href="https://arxiv.org/abs/2510.00565"><img src="https://img.shields.io/badge/arXiv-2510.00565-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2510.00565"><img src="https://img.shields.io/badge/AlphaXiv-2510.00565-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Shojiro Yamabe, Jun Sakuma

  **TL;DR:** Reveals a jailbreak "priming" vulnerability introduced by iterative denoising and proposes mitigations. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[09/2025] A2D: Any-Order, Any-Step Safety Alignment for Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2509.23286"><img src="https://img.shields.io/badge/arXiv-2509.23286-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2509.23286"><img src="https://img.shields.io/badge/AlphaXiv-2509.23286-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Wonje Jeung, Sangyeon Yoon, Yoonjun Cho, Dongjae Jeon, Sangwoo Shin, Hyesoo Hong, Albert No

  **TL;DR:** A safety alignment method tailored to dLLMs' any-order, any-step decoding, mitigating their unique jailbreak vulnerabilities. ICLR 2026.
  </details>

- <details>
  <summary>
    <b>[08/2025] Where to Start Alignment? Diffusion Large Language Model May Demand a Distinct Position</b>
    <a href="https://arxiv.org/abs/2508.12398"><img src="https://img.shields.io/badge/arXiv-2508.12398-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2508.12398"><img src="https://img.shields.io/badge/AlphaXiv-2508.12398-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Zhixin Xie, Xurui Song, Jun Luo

  **TL;DR:** An analytical work showing that the alignment starting point and data position for dLLMs is fundamentally different from AR models, providing design guidance for dLLM alignment. AAAI 2026 (oral).
  </details>

- <details>
  <summary>
    <b>[07/2025] Jailbreaking Large Language Diffusion Models (PAD)</b>
    <a href="https://arxiv.org/abs/2507.19227"><img src="https://img.shields.io/badge/arXiv-2507.19227-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2507.19227"><img src="https://img.shields.io/badge/AlphaXiv-2507.19227-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Yuanhe Zhang, Fangzhou Xie, Zhenhong Zhou, Zherui Li, Hao Chen, Kun Wang, Yufei Guo

  **TL;DR:** A parallel-decoding jailbreak attack (Multi-Point Attention Attack) reaching 97% ASR across four dLLMs while generating harmful content 2× faster. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[07/2025] The Devil Behind the Mask: An Emergent Safety Vulnerability of Diffusion LLMs (DIJA)</b>
    <a href="https://arxiv.org/abs/2507.11097"><img src="https://img.shields.io/badge/arXiv-2507.11097-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2507.11097"><img src="https://img.shields.io/badge/AlphaXiv-2507.11097-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/ZichenWen1/DIJA"><img src="https://img.shields.io/github/stars/ZichenWen1/DIJA?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Zichen Wen, Jiashu Qu, Zhaorun Chen, Xiaoya Lu, Dongrui Liu, Zhiyuan Liu, Ruixi Wu, Yicun Yang, et al.

  **TL;DR:** The first systematic jailbreak framework for dLLMs, exploiting bidirectional modeling and parallel decoding with mask-text interleaved prompts; reaches 100% ASR on Dream-Instruct. arXiv 2025.
  </details>

## Distillation

- <details>
  <summary>
    <b>[09/2026] A Ticket from Marginals to Joints: Coupled-Noise Distillation for One-Step Block Generation (CONDOR)</b>
    <a href="https://arxiv.org/abs/2609.06324"><img src="https://img.shields.io/badge/arXiv-2609.06324-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2609.06324"><img src="https://img.shields.io/badge/AlphaXiv-2609.06324-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Lin Yao

  **TL;DR:** A noise-conditioned masked denoiser plus coupled-noise distillation that commits an entire block of tokens in a single forward pass. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[08/2026] SelFusion: Self-distillation for Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2608.22898"><img src="https://img.shields.io/badge/arXiv-2608.22898-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2608.22898"><img src="https://img.shields.io/badge/AlphaXiv-2608.22898-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Hyeongsoo Lim, Jinyoung Kim, Eunseo Seo, Minho Jang, Jiwon Yoon

  **TL;DR:** Shows that naive knowledge distillation is ineffective or even harmful for DLMs, and proposes a two-stage self-distillation framework using two mask ratios (hard/easy) of the same model without an external teacher. ACL 2026.
  </details>

- <details>
  <summary>
    <b>[08/2026] OPTD: On-Policy Transition Distillation with Consistency-Guided Adaptive Compression for Few-Step Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2608.02942"><img src="https://img.shields.io/badge/arXiv-2608.02942-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2608.02942"><img src="https://img.shields.io/badge/AlphaXiv-2608.02942-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Xiaocheng Lu, Hualei Zhang, Shuhan Guo, Jie Zhang, Xiaoyi Pang, Jian Liu, Haoxi Li, Bohai Gu, Haoxuan Che, Jingcai Guo, Song Guo

  **TL;DR:** Builds few-step distillation supervision on the student's own on-policy trajectories, using a frozen teacher to verify the longest compressible prefix and fix off-distribution drift under aggressive step compression. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[07/2026] Latent-Kernel Discrete Flow Maps for Few-Step Generation</b>
    <a href="https://arxiv.org/abs/2607.27529"><img src="https://img.shields.io/badge/arXiv-2607.27529-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2607.27529"><img src="https://img.shields.io/badge/AlphaXiv-2607.27529-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Mansoor Ahmed, Yue-Tsz Fan, Hemanth Venkateswara, Murray Patterson

  **TL;DR:** Learns discrete flow maps for few-step text generation. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[07/2026] Multi-Mask Diffusion Language Models for Few-Step Generation</b>
    <a href="https://arxiv.org/abs/2607.19686"><img src="https://img.shields.io/badge/arXiv-2607.19686-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2607.19686"><img src="https://img.shields.io/badge/AlphaXiv-2607.19686-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Sijin Chen, Yinuo Ren, Heyang Zhao, Ziheng Cheng, Quanquan Gu, Lexing Ying

  **TL;DR:** A multi-mask training objective enabling few-step generation. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[07/2026] TOPD: Trace-Based On-Policy Distillation for Masked Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2607.16872"><img src="https://img.shields.io/badge/arXiv-2607.16872-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2607.16872"><img src="https://img.shields.io/badge/AlphaXiv-2607.16872-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Haolin Ren, Ziyang Huang, Chenhao Yuan, Jun Zhao, Kang Liu

  **TL;DR:** Applies teacher supervision on the student's own denoising trajectories, transferring reasoning ability without reward estimation — between SFT's exposure bias and RL's sparse rewards. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[07/2026] dOPSD: On-Policy Self-Distillation for Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2607.04428"><img src="https://img.shields.io/badge/arXiv-2607.04428-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2607.04428"><img src="https://img.shields.io/badge/AlphaXiv-2607.04428-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Phuong Tuan Dat, Qi Li, Xinchao Wang

  **TL;DR:** Derives the teacher's privilege signal directly from the student's own denoising trajectory for on-policy self-distillation of dLLMs, addressing SFT's exposure bias and RL's sparse sequence-level rewards. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[06/2026] Learning from the Self-future: On-policy Self-distillation for dLLMs (d-OPSD)</b>
    <a href="https://arxiv.org/abs/2606.18195"><img src="https://img.shields.io/badge/arXiv-2606.18195-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2606.18195"><img src="https://img.shields.io/badge/AlphaXiv-2606.18195-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/xingzhejun/d-opsd-code"><img src="https://img.shields.io/github/stars/xingzhejun/d-opsd-code?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Yifu Luo, Zeyu Chen, Haoyu Wang, Xinhao Hu, Yuxuan Zhang, Zhizhou Sha, Shiwei Liu

  **TL;DR:** The first on-policy self-distillation framework tailored for dLLMs, reframing self-teacher construction via self-generated answers as suffix conditioning so the student learns from its "self future-experience". arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[05/2026] DiLaDiff: Distilled Latent-Augmented Diffusion for Language Modeling</b>
    <a href="https://arxiv.org/abs/2605.23605"><img src="https://img.shields.io/badge/arXiv-2605.23605-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2605.23605"><img src="https://img.shields.io/badge/AlphaXiv-2605.23605-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Jean-Marie Lemercier, Tomas Geffner, Karsten Kreis, Morteza Mardani, Arash Vahdat, Ante Jukić

  **TL;DR:** A distilled latent-augmented diffusion language model for accelerated generation. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[05/2026] Self-Distilled Trajectory-Aware Boltzmann Modeling: Bridging the Training-Inference Discrepancy in Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2605.11854"><img src="https://img.shields.io/badge/arXiv-2605.11854-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2605.11854"><img src="https://img.shields.io/badge/AlphaXiv-2605.11854-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Kecheng Chen, Ziru Liu, Xijia Tao, Hui Liu, Yibing Liu, Xinyu Fu, Shi Wu, Suiyun Zhang, Dandan Tu, Lingpeng Kong, Rui Liu, Haoliang Li

  **TL;DR:** Self-distillation plus trajectory-aware Boltzmann modeling to bridge the DLM training-inference discrepancy. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[05/2026] Infinite Mask Diffusion for Few-Step Distillation (IMDM)</b>
    <a href="https://arxiv.org/abs/2605.10518"><img src="https://img.shields.io/badge/arXiv-2605.10518-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2605.10518"><img src="https://img.shields.io/badge/AlphaXiv-2605.10518-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Jaehoon Yoo, Wonjung Kim, Chanhyuk Lee, Seunghoon Hong

  **TL;DR:** An infinite-mask diffusion distillation framework enabling few-step sampling. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[05/2026] TAD: Temporal-Aware Trajectory Self-Distillation for Fast and Accurate Diffusion LLM</b>
    <a href="https://arxiv.org/abs/2605.09536"><img src="https://img.shields.io/badge/arXiv-2605.09536-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2605.09536"><img src="https://img.shields.io/badge/AlphaXiv-2605.09536-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/BHmingyang/TAD"><img src="https://img.shields.io/github/stars/BHmingyang/TAD?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Haoyang Zhou, Li Kong, Shijie Ren, Xiting Wang, Shuang Liang, Guowei Wang, Zhenxuan Pan

  **TL;DR:** Temporal-aware trajectory self-distillation that accelerates dLLM sampling while preserving accuracy. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[05/2026] Trajectory as the Teacher: Few-Step Discrete Flow Matching via Energy-Navigated Distillation (TS-DFM)</b>
    <a href="https://arxiv.org/abs/2605.07924"><img src="https://img.shields.io/badge/arXiv-2605.07924-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2605.07924"><img src="https://img.shields.io/badge/AlphaXiv-2605.07924-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Amin Karimi Monsefi, Dominic Culver, Nikhil Bhendawade, Manuel R. Ciosici, Yizhe Zhang, Irina Belousova

  **TL;DR:** Reshapes teacher trajectories with energy guidance during training; an 8-step student achieves 32% lower perplexity than its 1024-step teacher. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[04/2026] FlowLM: Few-Step Language Modeling via Diffusion-to-Flow Adaptation</b>
    <a href="https://arxiv.org/abs/2605.20199"><img src="https://img.shields.io/badge/arXiv-2605.20199-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2605.20199"><img src="https://img.shields.io/badge/AlphaXiv-2605.20199-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Runzhe Zhang, Letian Chen, Wenpeng Zhang, Zhouhan Lin, Peilin Zhao

  **TL;DR:** Transforms pretrained diffusion LMs into flow-matching models via efficient fine-tuning, re-aligning curved sampling trajectories into straight-line flows for high-quality few-step generation. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[04/2026] Consistent Diffusion Language Models (Multi-Path Consistency)</b>
    <a href="https://arxiv.org/abs/2605.00161"><img src="https://img.shields.io/badge/arXiv-2605.00161-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2605.00161"><img src="https://img.shields.io/badge/AlphaXiv-2605.00161-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Hasan Amin, Yuan Gao, Yaser Souri, Subhojit Som, Ming Yin, Rajiv Khanna, Xia Song

  **TL;DR:** Proposes a multi-path consistency principle for training discrete diffusion language models toward consistent few-step generation. ICML 2026.
  </details>

- <details>
  <summary>
    <b>[04/2026] Turning the TIDE: Cross-Architecture Distillation for Diffusion Large Language Models</b>
    <a href="https://arxiv.org/abs/2604.26951"><img src="https://img.shields.io/badge/arXiv-2604.26951-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2604.26951"><img src="https://img.shields.io/badge/AlphaXiv-2604.26951-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/PKU-YuanGroup/TIDE"><img src="https://img.shields.io/github/stars/PKU-YuanGroup/TIDE?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Gongbo Zhang, Wen Wang, Ye Tian, Li Yuan

  **TL;DR:** Cross-architecture distillation framework compressing 8B dense / 16B MoE dLLM teachers into a 0.6B student via TIDAL, CompDemo, and Reverse CALM. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[02/2026] Flow Map Language Models: One-step Language Modeling via Continuous Denoising</b>
    <a href="https://arxiv.org/abs/2602.16813"><img src="https://img.shields.io/badge/arXiv-2602.16813-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2602.16813"><img src="https://img.shields.io/badge/AlphaXiv-2602.16813-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Chanhyuk Lee, Jaehoon Yoo, Manan Agarwal, Sheel Shah, Jerry Huang, Aditi Raghunathan, Seunghoon Hong, Nicholas M. Boffi, Jinwoo Kim

  **TL;DR:** One-step language modeling by learning flow maps through continuous denoising. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[02/2026] T3D: Few-Step Diffusion Language Models via Trajectory Self-Distillation</b>
    <a href="https://arxiv.org/abs/2602.12262"><img src="https://img.shields.io/badge/arXiv-2602.12262-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2602.12262"><img src="https://img.shields.io/badge/AlphaXiv-2602.12262-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Tunyu Zhang, Xinxi Zhang, Ligong Han, Haizhou Shi, Xiaoxiao He, Zhuowei Li, Hao Wang, Kai Xu, Akash Srivastava, Chengzhi Mao, Hao Wang, Vladimir Pavlovic, Dimitris N. Metaxas

  **TL;DR:** Trajectory self-distillation for few-step dLLM sampling. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[01/2026] d3LLM: Ultra-Fast Diffusion LLM using Pseudo-Trajectory Distillation</b>
    <a href="https://arxiv.org/abs/2601.07568"><img src="https://img.shields.io/badge/arXiv-2601.07568-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2601.07568"><img src="https://img.shields.io/badge/AlphaXiv-2601.07568-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/hao-ai-lab/d3LLM"><img src="https://img.shields.io/github/stars/hao-ai-lab/d3LLM?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Yu-Yang Qian, Junda Su, Lanxiang Hu, Peiyuan Zhang, Zhijie Deng, Peng Zhao, Hao Zhang

  **TL;DR:** Pseudo-trajectory distillation teaches the model which tokens can be confidently decoded at early steps; combined with entropy-based multi-block decoding and KV-cache refresh, up to 10× speedup on LLaDA/Dream. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[01/2026] CD4LM: Consistency Distillation and aDaptive Decoding for Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2601.02236"><img src="https://img.shields.io/badge/arXiv-2601.02236-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2601.02236"><img src="https://img.shields.io/badge/AlphaXiv-2601.02236-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/yihao-liang/CDLM"><img src="https://img.shields.io/github/stars/yihao-liang/CDLM?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Yihao Liang, Ze Wang, Hao Chen, Ximeng Sun, Jialian Wu, Xiaodong Yu, Jiang Liu, Emad Barsoum, Zicheng Liu, Niraj K. Jha

  **TL;DR:** Discrete-space consistency distillation trains a trajectory-invariant student; with confidence-adaptive decoding skips, 5.18× speedup on GSM8K while strictly dominating the accuracy-efficiency Pareto frontier. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[11/2025] CDLM: Consistency Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2511.19269"><img src="https://img.shields.io/badge/arXiv-2511.19269-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2511.19269"><img src="https://img.shields.io/badge/AlphaXiv-2511.19269-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/SqueezeAILab/CDLM"><img src="https://img.shields.io/github/stars/SqueezeAILab/CDLM?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Minseo Kim, Chenfeng Xu, Coleman Hooper, Harman Singh, Ben Athiwaratkun, Ce Zhang, Kurt Keutzer, Amir Gholami

  **TL;DR:** Brings consistency modeling into DLM training, distilling a full bidirectional teacher and aligning predictions along the decoding trajectory; block-wise causal attention enables KV cache, reducing latency 3.6–14.5×. MLSys 2026.
  </details>

- <details>
  <summary>
    <b>[09/2025] dParallel: Learnable Parallel Decoding for dLLMs</b>
    <a href="https://arxiv.org/abs/2509.26488"><img src="https://img.shields.io/badge/arXiv-2509.26488-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2509.26488"><img src="https://img.shields.io/badge/AlphaXiv-2509.26488-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/czg1225/dParallel"><img src="https://img.shields.io/github/stars/czg1225/dParallel?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Zigeng Chen, Gongfan Fang, Xinyin Ma, Ruonan Yu, Xinchao Wang

  **TL;DR:** Certainty-forcing distillation fine-tunes on self-generated trajectories so masked tokens reach high confidence in parallel faster; 256→30 steps on GSM8K, 8.5× speedup. arXiv 2025.
  </details>

- <details>
  <summary>
    <b>[09/2025] Ultra-Fast Language Generation via Discrete Diffusion Divergence Instruct (DiDi-Instruct)</b>
    <a href="https://arxiv.org/abs/2509.25035"><img src="https://img.shields.io/badge/arXiv-2509.25035-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2509.25035"><img src="https://img.shields.io/badge/AlphaXiv-2509.25035-7c3aed.svg" alt="AlphaXiv"></a>
    <a href="https://github.com/haoyangzheng-ai/didi-instruct"><img src="https://img.shields.io/github/stars/haoyangzheng-ai/didi-instruct?style=social&label=Stars" alt="GitHub Stars"></a>
  </summary>

  **Authors:** Haoyang Zheng, Xinyang Liu, Cindy Xiangrui Kong, Nan Jiang, Zheyuan Hu, Weijian Luo, Wei Deng, Guang Lin

  **TL;DR:** Distribution-matching distillation based on integral KL divergence minimization, distilling a dLLM teacher into an 8–16-step few-step student; 64× speedup while surpassing the teacher. ICLR 2026.
  </details>

## Inference Acceleration

- <details>
  <summary>
    <b>[09/2026] DFlow: Enabling Verifier Information Flow in Block Diffusion Speculative Decoding</b>
    <a href="https://arxiv.org/abs/2609.06498"><img src="https://img.shields.io/badge/arXiv-2609.06498-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2609.06498"><img src="https://img.shields.io/badge/AlphaXiv-2609.06498-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Yaojie Zhang, Linfeng Zhang, Bin Cui, Xupeng Miao

  **TL;DR:** Feeds verifier information back into the block-diffusion drafter to improve speculation quality. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[09/2026] Unlocking Lossless Speedups in LLMs via Discrete Diffusion</b>
    <a href="https://arxiv.org/abs/2609.04010"><img src="https://img.shields.io/badge/arXiv-2609.04010-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2609.04010"><img src="https://img.shields.io/badge/AlphaXiv-2609.04010-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Subham Sekhar Sahoo, Lingjie Chen, Khiem Pham, Jonathan Geuter, Chaitanya Dwivedi, Varad Pimpalkhute, Yash Akhauri, Alexander Moreno, et al.

  **TL;DR:** Diffusion-augmented LLMs: keeps the AR model's distribution intact while sampling from it in parallel with diffusion, achieving lossless speedups. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[09/2026] Predict, Don't Iterate: Efficient Adaptive-Length Infilling for Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2609.02108"><img src="https://img.shields.io/badge/arXiv-2609.02108-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2609.02108"><img src="https://img.shields.io/badge/AlphaXiv-2609.02108-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Haobo Xu, Sirui Chen, Yuanchen Bei, Lingjie Chen, Yuchen Yan, Dongqi Fu, Jingrui He, Hanghang Tong

  **TL;DR:** Predicts the span length of infill regions instead of iterative trial-and-error, enabling adaptive-length infilling. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[08/2026] CARVE: Verified Expansion for Variable-Length Generation in Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2608.30922"><img src="https://img.shields.io/badge/arXiv-2608.30922-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2608.30922"><img src="https://img.shields.io/badge/AlphaXiv-2608.30922-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Wail Bouhedja, Amr Mohamed, Guokan Shang

  **TL;DR:** A verified canvas-expansion mechanism that removes the rigid requirement of pre-setting response length in masked diffusion. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[08/2026] Trajectory-Level Speculative Decoding for Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2608.27514"><img src="https://img.shields.io/badge/arXiv-2608.27514-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2608.27514"><img src="https://img.shields.io/badge/AlphaXiv-2608.27514-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Tianxiang Pan, Baitao Gong, Mo Guang, Hongwei Yong, Tianpeng Jiang, Yaqian Li, Zheng Cao, Kaiwen Long

  **TL;DR:** Generalizes speculative decoding from fixed left-to-right token sequences to the denoising-trajectory level (sequences of multi-token updates). ICML 2026.
  </details>

- <details>
  <summary>
    <b>[08/2026] Prefix-Denoising Consistency: Test-Time Verification for Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2608.25311"><img src="https://img.shields.io/badge/arXiv-2608.25311-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2608.25311"><img src="https://img.shields.io/badge/AlphaXiv-2608.25311-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Yuki Ichihara, Naoto Iwase, Mohammad Atif Quamar, Junpei Komiyama

  **TL;DR:** Uses prefix-denoising consistency as a test-time verification and correction signal for dLLMs. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[08/2026] DARTree: Speculative Diffusion Decoding with Autoregressive Draft Trees</b>
    <a href="https://arxiv.org/abs/2608.13524"><img src="https://img.shields.io/badge/arXiv-2608.13524-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2608.13524"><img src="https://img.shields.io/badge/AlphaXiv-2608.13524-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Tianyi Li, Yaxin Luo, Xinyi Shang, Zhiqiang Shen

  **TL;DR:** Combines diffusion decoding with autoregressive draft trees. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[08/2026] Commitment Before Realization: When Classifier-Free Guidance Becomes Unnecessary in Masked Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2608.08082"><img src="https://img.shields.io/badge/arXiv-2608.08082-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2608.08082"><img src="https://img.shields.io/badge/AlphaXiv-2608.08082-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Fan Zhou, Weitian Wang, Tim Van de Cruys

  **TL;DR:** Defines a "remaining guidance value" to determine when classifier-free guidance is actually needed, enabling adaptive shutoff to save compute. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[08/2026] xPress: Parallel Refinement for Diffusion Drafters in Speculative Decoding</b>
    <a href="https://arxiv.org/abs/2608.02438"><img src="https://img.shields.io/badge/arXiv-2608.02438-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2608.02438"><img src="https://img.shields.io/badge/AlphaXiv-2608.02438-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Zheng Wang, Davis Wertheimer, Yu Chin Fabian Lim, Mudhakar Srivatsa, Raghu K. Ganti, Minjia Zhang, Naigang Wang

  **TL;DR:** Parallel refinement for diffusion drafters in speculative decoding pipelines. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[07/2026] Speculative Correction: Draft-then-Refine Decoding for Diffusion Language Models</b>
    <a href="https://arxiv.org/abs/2608.02625"><img src="https://img.shields.io/badge/arXiv-2608.02625-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2608.02625"><img src="https://img.shields.io/badge/AlphaXiv-2608.02625-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Brian K Chen, Chong Wu, Kenji Kawaguchi

  **TL;DR:** Drafts a complete sequence first, then refines it globally with bidirectional diffusion — a training-free speedup that also improves GSM8K/MBPP accuracy. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[07/2026] DC-Leap: Training-Free Acceleration of dLLMs via Draft-Guided Contiguous Leaping Decoding</b>
    <a href="https://arxiv.org/abs/2607.20467"><img src="https://img.shields.io/badge/arXiv-2607.20467-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2607.20467"><img src="https://img.shields.io/badge/AlphaXiv-2607.20467-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Yanhua Jiao, Tianyi Wu, Xiaoxi Sun, Yulin Li, HuiLing Zhen, Libo Qin, Baotian Hu, Zhuotao Tian, Min Zhang

  **TL;DR:** Dynamic contiguous verification cancels joint-probability dependency errors; up to 53× speedup on long MBPP sequences. ICML 2026.
  </details>

- <details>
  <summary>
    <b>[07/2026] AdaFlash: Adaptive Speculative Decoding via On-Policy Distilled Diffusion Drafters</b>
    <a href="https://arxiv.org/abs/2607.19223"><img src="https://img.shields.io/badge/arXiv-2607.19223-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2607.19223"><img src="https://img.shields.io/badge/AlphaXiv-2607.19223-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Yu-Yang Qian, Hao-Cong Wu, Chen Chen, Jiacheng Sun, Zhenhua Dong, Peng Zhao, Zhi-Hua Zhou

  **TL;DR:** On-policy distilled diffusion drafters with adaptive verification length, fixing acceptance-rate degradation under OOD inputs. arXiv 2026.
  </details>

- <details>
  <summary>
    <b>[07/2026] DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation</b>
    <a href="https://arxiv.org/abs/2607.05147"><img src="https://img.shields.io/badge/arXiv-2607.05147-b31b1b.svg" alt="arXiv"></a>
    <a href="https://www.alphaxiv.org/abs/2607.05147"><img src="https://img.shields.io/badge/AlphaXiv-2607.05147-7c3aed.svg" alt="AlphaXiv"></a>
  </summary>

  **Authors:** Xin Cheng, Xingkai Yu, Chenze Shao, Jiashi Li, Yunfan Xiong, Yi Qian, Jiaqi Zhu, Shirong Ma, et al.

  **TL;DR:** Confidence-scheduled semi-autoregressive generati