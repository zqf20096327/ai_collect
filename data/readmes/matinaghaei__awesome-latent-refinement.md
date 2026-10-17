<h1 align="center">🧬 Awesome Latent Refinement</h1>
<h3 align="center"><em>Iterative Reasoning & Planning in Latent Space</em></h3>

<p align="center">
  <a href="https://awesome.re">
    <img src="https://awesome.re/badge.svg"/>
  </a>
  <a href="https://github.com/matinaghaei/awesome-latent-refinement/stargazers">
    <img src="https://img.shields.io/github/stars/matinaghaei/awesome-latent-refinement.svg"/>
  </a>
  <a href="https://github.com/matinaghaei/awesome-latent-refinement/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg"/>
  </a>
  <a href="https://github.com/matinaghaei/awesome-latent-refinement/blob/main/CONTRIBUTING.md">
    <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen.svg"/>
  </a>
</p>

<p align="center">
  <img src="cover.jpg" width="650"/>
</p>

<br/>

<p align="center">
  ⭐ If you find this useful, please consider giving the repo a star!
</p>

---

## 🧠 Overview

- [🎯 Aim of the Project](#-aim-of-the-project)
- [🧬 Supervised Latent Refinement](#-supervised-latent-refinement)
  - [🧠 Dedicated Reasoners](#-dedicated-reasoners)
  - [🔁 Looped Language Models](#-looped-language-models)
  - [🦾 Vision-Language-Action Models](#-vision-language-action-models)
- [🎮 Reinforcement-Learned Latent Refinement](#-reinforcement-learned-latent-refinement)
  - [🗺️ Model-Free Planning](#️-model-free-planning)
  - [♻️ Recurrent Reasoning Agents](#-recurrent-reasoning-agents)
  - [⏱️ Compute in RL](#-compute-in-rl)
- [🔒 Inclusion Criteria](#-inclusion-criteria)
- [🔗 Related Awesome Lists](#-related-awesome-lists)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

---

## 🎯 Aim of the Project

Latent refinement has recently emerged across both supervised reasoning and reinforcement learning. In these systems, performance improves not by producing explicit intermediate outputs, but by repeatedly updating internal representations using shared or recurrent computation.

This repository aims to:

- organize research on **iterative refinement of latent state**
- highlight the connection between **supervised reasoning** and **reinforcement-learned planning**
- track systems where **additional inference-time compute improves performance**
- provide a focused, high-signal resource for researchers interested in latent iterative computation

---

## 🧬 Supervised Latent Refinement

Models that learn to perform **iterative updates over latent state** for reasoning tasks.

### 🧠 Dedicated Reasoners

Architectures explicitly designed to perform reasoning through iterative latent-state updates.

- **Can You Learn an Algorithm? Generalizing from Easy to Hard Problems with Recurrent Networks**. [![arXiv](https://img.shields.io/badge/arXiv-2106.04537-b31b1b.svg)](https://arxiv.org/abs/2106.04537) [![OpenReview](https://img.shields.io/badge/OpenReview-Paper-8E44AD.svg)](https://openreview.net/forum?id=Tsp2PL7-GQ) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/aks2203/deep-thinking)

- **End-to-end Algorithm Synthesis with Recurrent Networks: Logical Extrapolation Without Overthinking**. [![arXiv](https://img.shields.io/badge/arXiv-2202.05826-b31b1b.svg)](https://arxiv.org/abs/2202.05826) [![OpenReview](https://img.shields.io/badge/OpenReview-Paper-8E44AD.svg)](https://openreview.net/forum?id=PPjSKy40XUB) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/aks2203/deep-thinking)

- **HRM**: "Hierarchical Reasoning Model". [![arXiv](https://img.shields.io/badge/arXiv-2506.21734-b31b1b.svg)](https://arxiv.org/abs/2506.21734) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/sapientinc/HRM)

- **TRM**: "Less is More: Recursive Reasoning with Tiny Networks". [![arXiv](https://img.shields.io/badge/arXiv-2510.04871-b31b1b.svg)](https://arxiv.org/abs/2510.04871) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/SamsungSAILMontreal/TinyRecursiveModels)

- **Your Latent Reasoning is Secretly Policy Improvement Operator**. [![arXiv](https://img.shields.io/badge/arXiv-2511.16886-b31b1b.svg)](https://arxiv.org/abs/2511.16886) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/machinestein/Deep-Improvement-Supervision)

- **Are Your Reasoning Models Reasoning or Guessing? A Mechanistic Analysis of Hierarchical Reasoning Models**. [![arXiv](https://img.shields.io/badge/arXiv-2601.10679-b31b1b.svg)](https://arxiv.org/abs/2601.10679) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/arcprize/hierarchical-reasoning-model-analysis)

- **Tiny Recursive Reasoning with Mamba-2 Attention Hybrid**. [![arXiv](https://img.shields.io/badge/arXiv-2602.12078-b31b1b.svg)](https://arxiv.org/abs/2602.12078)

- **SE-RRM**: "Symbol-Equivariant Recurrent Reasoning Models". [![arXiv](https://img.shields.io/badge/arXiv-2603.02193-b31b1b.svg)](https://arxiv.org/abs/2603.02193) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ml-jku/SE-RRM)

- **Recursive Inference Machines for Neural Reasoning**. [![arXiv](https://img.shields.io/badge/arXiv-2603.05234-b31b1b.svg)](https://arxiv.org/abs/2603.05234)

- **One Step Forward and K Steps Back: Better Reasoning with Denoising Recursion Models**. [![arXiv](https://img.shields.io/badge/arXiv-2604.18839-b31b1b.svg)](https://arxiv.org/abs/2604.18839) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/wwwwwwwwz/DenoisingRecursionModels)

### 🔁 Looped Language Models

Language models that reuse internal computation (e.g., via loops or recurrent depth) to iteratively refine latent representations.

- **Coconut**: "Training Large Language Models to Reason in a Continuous Latent Space". [![arXiv](https://img.shields.io/badge/arXiv-2412.06769-b31b1b.svg)](https://arxiv.org/abs/2412.06769) [![OpenReview](https://img.shields.io/badge/OpenReview-Paper-8E44AD.svg)](https://openreview.net/forum?id=Itxz7S4Ip3) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/facebookresearch/coconut)

- **Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach**. [![arXiv](https://img.shields.io/badge/arXiv-2502.05171-b31b1b.svg)](https://arxiv.org/abs/2502.05171) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/seal-rg/recurrent-pretraining)

- **Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking**. [![arXiv](https://img.shields.io/badge/arXiv-2502.13842-b31b1b.svg)](https://arxiv.org/abs/2502.13842)

- **Reasoning with Latent Thoughts: On the Power of Looped Transformers**. [![arXiv](https://img.shields.io/badge/arXiv-2502.17416-b31b1b.svg)](https://arxiv.org/abs/2502.17416) [![OpenReview](https://img.shields.io/badge/OpenReview-Paper-8E44AD.svg)](https://openreview.net/forum?id=din0lGfZFd)

- **Encode, Think, Decode: Scaling test-time reasoning with recursive latent thoughts**. [![arXiv](https://img.shields.io/badge/arXiv-2510.07358-b31b1b.svg)](https://arxiv.org/abs/2510.07358) [![OpenReview](https://img.shields.io/badge/OpenReview-Paper-8E44AD.svg)](https://openreview.net/forum?id=jBSye8M3FQ)

- **Efficient Parallel Samplers for Recurrent-Depth Models and Their Connection to Diffusion Language Models**. [![arXiv](https://img.shields.io/badge/arXiv-2510.14961-b31b1b.svg)](https://arxiv.org/abs/2510.14961) [![OpenReview](https://img.shields.io/badge/OpenReview-Paper-8E44AD.svg)](https://openreview.net/forum?id=z62rRFnNaX) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/seal-rg/recurrent-pretraining)

- **PLT**: "Parallel Loop Transformer (PLT) for Efficient Test-Time Computation Scaling". [![arXiv](https://img.shields.io/badge/arXiv-2510.24824-b31b1b.svg)](https://arxiv.org/abs/2510.24824)

- **Ouro**: "Scaling Latent Reasoning via Looped Language Models". [![arXiv](https://img.shields.io/badge/arXiv-2510.25741-b31b1b.svg)](https://arxiv.org/abs/2510.25741) [![Website](https://img.shields.io/badge/Website-Link-blue.svg)](https://ouro-llm.github.io/) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Models-yellow.svg)](https://huggingface.co/collections/ByteDance/ouro)

- **Teaching Pretrained Language Models to Think Deeper with Retrofitted Recurrence**. [![arXiv](https://img.shields.io/badge/arXiv-2511.07384-b31b1b.svg)](https://arxiv.org/abs/2511.07384) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/mcleish7/retrofitting-recurrence) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Models-yellow.svg)](https://huggingface.co/collections/tomg-group-umd/retrofitting-recurrence)

- **Think-at-Hard**: "Selective Latent Iterations to Improve Reasoning Language Models". [![arXiv](https://img.shields.io/badge/arXiv-2511.08577-b31b1b.svg)](https://arxiv.org/abs/2511.08577) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/thu-nics/TaH)

- **Depth-Recurrent Attention Mixtures: Giving Latent Reasoning the Attention it Deserves**. [![arXiv](https://img.shields.io/badge/arXiv-2601.21582-b31b1b.svg)](https://arxiv.org/abs/2601.21582)

- **LoopFormer**: "Elastic-Depth Looped Transformers for Latent Reasoning via Shortcut Modulation". [![arXiv](https://img.shields.io/badge/arXiv-2602.11451-b31b1b.svg)](https://arxiv.org/abs/2602.11451) [![OpenReview](https://img.shields.io/badge/OpenReview-Paper-8E44AD.svg)](https://openreview.net/forum?id=RzYXb5YWBs) [![Website](https://img.shields.io/badge/Website-Link-blue.svg)](https://loopformer.github.io/) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/ArmenAgha/loopformer) [![HuggingFace](https://img.shields.io/badge/HuggingFace-Models-yellow.svg)](https://huggingface.co/collections/ArmenAgha/loopformer)

- **GTS**: "Inference-Time Scaling of Latent Reasoning with a Learnable Gaussian Thought Sampler". [![arXiv](https://img.shields.io/badge/arXiv-2602.14077-b31b1b.svg)](https://arxiv.org/abs/2602.14077)

- **Inner Loop Inference for Pretrained Transformers: Unlocking Latent Capabilities Without Training**. [![arXiv](https://img.shields.io/badge/arXiv-2602.14759-b31b1b.svg)](https://arxiv.org/abs/2602.14759)

- **From Growing to Looping: A Unified View of Iterative Computation in LLMs**. [![arXiv](https://img.shields.io/badge/arXiv-2602.16490-b31b1b.svg)](https://arxiv.org/abs/2602.16490)

- **Thinking in Latents: Adaptive Anchor Refinement for Implicit Reasoning in LLMs**. [![arXiv](https://img.shields.io/badge/arXiv-2603.15051-b31b1b.svg)](https://arxiv.org/abs/2603.15051) [![OpenReview](https://img.shields.io/badge/OpenReview-Paper-8E44AD.svg)](https://openreview.net/forum?id=fyWD8DDPKE)

- **Thinking Deeper, Not Longer: Depth-Recurrent Transformers for Compositional Generalization**. [![arXiv](https://img.shields.io/badge/arXiv-2603.21676-b31b1b.svg)](https://arxiv.org/abs/2603.21676)

- **Loop, Think, & Generalize: Implicit Reasoning in Recurrent-Depth Transformers**. [![arXiv](https://img.shields.io/badge/arXiv-2604.07822-b31b1b.svg)](https://arxiv.org/abs/2604.07822) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/OSU-NLP-Group/Loop-Think-Generalize)

- **A Mechanistic Analysis of Looped Reasoning Language Models**. [![arXiv](https://img.shields.io/badge/arXiv-2604.11791-b31b1b.svg)](https://arxiv.org/abs/2604.11791)

### 🦾 Vision-Language-Action Models

Vision-language-action systems that use latent iterative refinement instead of explicit tokenized reasoning.

- **RD-VLA**: "Recurrent-Depth VLA: Implicit Test-Time Compute Scaling of Vision-Language-Action Models via Latent Iterative Reasoning". [![arXiv](https://img.shields.io/badge/arXiv-2602.07845-b31b1b.svg)](https://arxiv.org/abs/2602.07845) [![OpenReview](https://img.shields.io/badge/OpenReview-Paper-8E44AD.svg)](https://openreview.net/forum?id=hsIm52gD9p) [![Website](https://img.shields.io/badge/Website-Link-blue.svg)](https://rd-vla.github.io/) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/rd-vla/rd-vla)

### 🚫 Excluded (Supervised)

- text-based self-refinement methods
- branching or search-based reasoning
- diffusion or generative latent refinement not used for reasoning
- standard feedforward transformers without iterative computation

---

## 🎮 Reinforcement-Learned Latent Refinement

Agents that develop **iterative latent computation** through interaction and reward.

### 🗺️ Model-Free Planning

Recurrent agents that exhibit planning-like behavior through internal latent computation without explicit world models.

- **An Investigation of Model-Free Planning**. [![arXiv](https://img.shields.io/badge/arXiv-1901.03559-b31b1b.svg)](https://arxiv.org/abs/1901.03559) [![Code](https://img.shields.io/badge/Code-Boxoban-green.svg)](https://github.com/google-deepmind/boxoban-levels)

- **Planning in a recurrent neural network that plays Sokoban**. [![arXiv](https://img.shields.io/badge/arXiv-2407.15421-b31b1b.svg)](https://arxiv.org/abs/2407.15421) [![OpenReview](https://img.shields.io/badge/OpenReview-Paper-8E44AD.svg)](https://openreview.net/forum?id=ORxjH9kTp8) [![Code](https://img.shields.io/badge/Code-Analysis-green.svg)](https://github.com/AlignmentResearch/learned-planner) [![Code](https://img.shields.io/badge/Code-Training-green.svg)](https://github.com/AlignmentResearch/train-learned-planner)

- **Interpreting Emergent Planning in Model-Free Reinforcement Learning**. [![arXiv](https://img.shields.io/badge/arXiv-2504.01871-b31b1b.svg)](https://arxiv.org/abs/2504.01871) [![OpenReview](https://img.shields.io/badge/OpenReview-Paper-8E44AD.svg)](https://openreview.net/forum?id=DzGe40glxs) [![Website](https://img.shields.io/badge/Website-Link-blue.svg)](https://tuphs28.github.io/projects/interpplanning/) [![Code](https://img.shields.io/badge/Code-GitHub-green.svg)](https://github.com/tuphs28/emergent-planning/tree/main)

- **Path Channels and Plan Extension Kernels: a Mechanistic Description of Planning in a Sokoban RNN**. [![arXiv](https://img.shields.io/badge/arXiv-2506.10138-b31b1b.svg)](https://arxiv.org/abs/2506.10138) [![OpenReview](https://img.shields.io/badge/OpenReview-Paper-8E44AD.svg)](https://openreview.net/forum?id=aAshH4kQ1v)

### ♻️ Recurrent Reasoning Agents

Agents trained with reinforcement learning that develop reusable latent reasoning dynamics across environment interactions.

- **HRM-Agent**: "HRM-Agent: Training a recurrent reasoning model in dynamic environments using reinforcement learning". [![arXiv](https://img.shields.io/badge/arXiv-2510.22832-b31b1b.svg)](https://arxiv.org/abs/2510.22832)

### ⏱️ Compute in RL

Work studying how increased internal computation improves reinforcement learning performance and generalization.

- **On the Role of Iterative Computation in Reinforcement Learning**. [![arXiv](https://img.shields.io/badge/arXiv-2602.05999-b31b1b.svg)](https://arxiv.org/abs/2602.05999) [![Website](https://img.shields.io/badge/Website-Link-blue.svg)](https://rajghugare19.github.io/computation-rl/index.html)

### 🚫 Excluded (RL)

- model-based RL relying on explicit planning over learned world models
- tree search methods such as MCTS
- policies without iterative internal computation
- latent world models used purely for simulation

---

## 🔒 Inclusion Criteria

A paper is included only if it satisfies all of the following:

1. **Iterative refinement of latent state** at inference time
2. **Shared or recurrent computation** across refinement steps
3. **Performance improves with additional internal compute**

---

## 🔗 Related Awesome Lists

Neighboring curated lists and resources on latent reasoning, implicit reasoning, efficient reasoning, and inference-time computation:

- **[Awesome Latent CoT](https://github.com/EIT-NLP/Awesome-Latent-CoT)**  
  Curated resources on latent chain-of-thought reasoning.

- **[Awesome LLM Implicit Reasoning](https://github.com/digailab/awesome-llm-implicit-reasoning)**  
  Papers and resources on implicit reasoning in language models.

- **[Awesome Efficient Reasoning](https://github.com/hemingkx/Awesome-Efficient-Reasoning)**  
  Efficient reasoning methods and inference-time scaling techniques.

- **[Awesome Inference-Time Scaling](https://github.com/ThreeSR/Awesome-Inference-Time-Scaling)**  
  Research on inference-time and test-time scaling.

- **[Awesome Latent Space](https://github.com/YU-deep/Awesome-Latent-Space)**  
  Broad collection of work on latent-space methods across modalities.

- **[Awesome World Models](https://github.com/knightnemo/Awesome-World-Models)**  
  Curated research on world models and latent dynamics.


---

## 🤝 Contributing

Contributions are very welcome!

If you know of a paper, project, implementation, or related resource that fits the scope of this repository, feel free to open a pull request or issue.

This list is intended to stay focused, so suggested additions should match the core idea:

1. **Iterative refinement of latent state** at inference time
2. **Shared or recurrent computation** across refinement steps
3. **Performance improves with additional inference-time compute**

If you are unsure whether something belongs, opening an issue for discussion is completely fine.

Please see [CONTRIBUTING.md](./CONTRIBUTING.md) for formatting guidelines.

---

## 📜 License

This work is licensed under the [Creative Commons Zero v1.0 Universal (CC0 1.0)](https://github.com/matinaghaei/awesome-latent-refinement/blob/main/LICENSE).
