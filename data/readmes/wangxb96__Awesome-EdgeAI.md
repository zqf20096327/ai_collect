# Awesome Edge AI

**From TinyML to Cognitive Edge Computing**  
*Curated resources on data, model, system optimization + Large Models (LLMs/VLMs), Agents & On-Device AI (2016–2026)*

**Last refresh: 11 November 2026** — 39 verified papers were added across the two 2026 refreshes (see [2026 Additions](#new-2026-additions-verified-nov-2026)), plus 30+ official repositories in the [On-Device Model Families & Tool Repository Index](#new-on-device-model-families--tool-repository-index). All 135 pre-existing arXiv identifiers were re-validated against the arXiv API; mismatched IDs, dead links and withdrawn preprints were corrected or flagged.

**Maintainers / Survey Authors**
- [Xubin Wang](https://github.com/wangxb96)<sup>1</sup>
- [Qing Li](https://scholar.google.com/citations?user=D1LEg-YAAAAJ&hl=zh-CN)<sup>2</sup>
- [Weijia Jia](https://scholar.google.com/citations?user=jtvFB20AAAAJ&hl=zh-CN&oi=ao)<sup>3,4</sup>

<sup>1</sup> East China University of Science and Technology
<sup>2</sup> The Hong Kong Polytechnic University
<sup>3</sup> Beijing Normal University  
<sup>4</sup> Beijing Normal-Hong Kong Baptist University  


![Awesome](https://awesome.re/badge.svg)
![Stars](https://img.shields.io/github/stars/wangxb96/Awesome-EdgeAI?style=social)
![Forks](https://img.shields.io/github/forks/wangxb96/Awesome-EdgeAI?style=social)
![License](https://img.shields.io/github/license/wangxb96/Awesome-EdgeAI?color=blue)

**Core Survey (2025, v2) + Official Repository**
- Paper: [Cognitive Edge Computing: A Comprehensive Survey on Optimizing Large Models and AI Agents for Pervasive Deployment](https://arxiv.org/abs/2501.03265) (arXiv:2501.03265, v2 Nov 2025)
- **This repository (`wangxb96/Awesome-EdgeAI`) is the official artifact repository** of the TMC manuscript *Cognitive Edge Computing: A Survey on Optimizing Large Language Models and Autonomous Agents for the Edge* (TMC-2026-05-1923, Major Revision). See [Official Repository for TMC-2026-05-1923](#official-repository-for-tmc-2026-05-1923) for the scoped survey protocol, frozen retained-link manifests, and revision crosswalk.
- Earlier focused companion repository (historical, superseded as the official artifact): [cognitive-edge-llm-agent-survey](https://github.com/wangxb96/cognitive-edge-llm-agent-survey).

**Legacy Survey (v1) — retained here for historical completeness**  
This repository continues to host and reference the original survey:  
- [Optimizing Edge AI: A Comprehensive Survey on Data, Model, and System Strategies](https://arxiv.org/abs/2501.03265v1)

**Legacy citation (for the data-model-system triad paper):**
```bibtex
@article{wang2025optimizing,
  title={Optimizing edge AI: A comprehensive survey on data, model, and system strategies},
  author={Wang, Xubin and Jia, Weijia},
  journal={arXiv e-prints},
  pages={arXiv--2501},
  year={2025}
}
```
---

## Abstract

This living repository curates the most important advances in **Edge AI**, spanning:

- Classic **data / model / system** optimization for tiny deep learning (CNNs, RNNs, efficient architectures).
- The new frontier: **on-device / edge Large Language Models (LLMs), Vision-Language Models (VLMs), Small Language Models (SLMs)**, efficient inference, quantization, speculative decoding, KV-cache optimization, on-device training, and **AI Agents** that run with tool use on phones, microcontrollers, and NPUs.

It serves researchers, engineers, and students who want to deploy real intelligence at the extreme edge (KB–few GB memory, mW–few W power). The list is actively maintained and regularly enriched with 2023–2026 literature, frameworks, benchmarks, and hardware. New entries are checked against their primary source (arXiv abstract page or publisher DOI) before being added, and withdrawn preprints are excluded.

**Cite the main survey (v2):**
```bibtex
@article{wang2025cognitive,
  title={Cognitive Edge Computing: A Comprehensive Survey on Optimizing Large Models and AI Agents for Pervasive Deployment},
  author={Wang, Xubin and Li, Qing and Jia, Weijia},
  journal={arXiv preprint arXiv:2501.03265},
  year={2025}
}
```

---

## New: Unified Architecture & Cognitive Edge (2023–2026)

**Master Overview Figure** — the Cognitive Edge Computing unified stack (Fig 1):

![Cognitive Edge AI Architecture](Figures/cognitive_edge_ai_architecture.png)

> **Five-layer architecture**: **Hardware (NPU/GPU/MCU)** → **Runtimes (llama.cpp, MLC-LLM, ExecuTorch)** → **Model Efficiency (Quantization, Pruning, KD)** → **Agentic/Cognitive (LLM Agents, RAG, Planning)** → **Applications (Healthcare, Smart Home, Autonomous)** — with cross-cutting concerns (security, energy, benchmarks, data pipeline, feedback loops, networking, standardization) on the left. See the full **Modern Era** section below for detailed 2023–2026 literature and supporting figures.

---

# Table of Contents
  - [Official Repository for TMC-2026-05-1923](#official-repository-for-tmc-2026-05-1923)
  - [New: 2026 Additions (verified Nov 2026)](#new-2026-additions-verified-nov-2026)
  - [New: On-Device Model Families & Tool Repository Index](#new-on-device-model-families--tool-repository-index)
  - [New: Unified Architecture & Cognitive Edge (2023–2026)](#new-unified-architecture--cognitive-edge-20232026)
    - [Modern Era: Large Models, Agents & Cognitive Systems](#modern-era-large-models-agents--cognitive-systems-on-edge-20232026)
    - [AI Agents on Edge](#5-ai-agents-on-edge--on-device-agents)
    - [Frameworks & Runtimes (2023–2026)](#6-frameworks--runtimes-for-edge--on-device-deployment-20232026)
    - [Hardware Acceleration](#7-hardware-acceleration-for-edge-ai--llms)
    - [Benchmarks & Tools (2023–2026)](#8-benchmarks-datasets--tools-20232026-focus)
    - [Recent Surveys & Highlights](#9-recent-surveys--overviews-20232026)
  - [New: Federated Learning on Edge](#new-federated-learning-on-edge)
  - [New: TinyML & Microcontroller AI](#new-tinyml--microcontroller-ai)
  - [New: Edge AI Security & Privacy](#new-edge-ai-security--privacy)
  - [New: On-Device Training & Personalization](#new-on-device-training--personalization)
  - [New: Multimodal & Embodied Edge AI](#new-multimodal--embodied-edge-ai)
  - [New: Real-World Applications & Case Studies](#new-real-world-applications--case-studies)
  - [Historical Foundations (Legacy v1 Content — fully retained)](#historical-foundations-legacy-v1-content--fully-retained)
    - [Background Knowledge](#1-background-knowledge)
    - [2. Our Survey (To be released)](#2-our-survey-to-be-released)
    - [The Data-Model-System Optimization Triad (full tables)](#3-the-data-model-system-optimization-triad)
  - [Contributing](#contributing)
    
---

## Official Repository for TMC-2026-05-1923

This repository is the **official artifact repository** for the IEEE TMC Major Revision of

> *Cognitive Edge Computing: A Survey on Optimizing Large Language Models and Autonomous Agents for the Edge* (Manuscript `TMC-2026-05-1923`, decision 28 Oct 2026, revision due 26 Jan 2027).

The manuscript and this repository are maintained together: the paper cites this repository as its public artifact, and the repository maintains the retained-link census, tool-repository index, and inspectable protocol behind the paper's methodology and evidence grading. Historical search/screening logs are incomplete; the census does not establish exhaustive literature coverage.

| Manuscript claim / section | Verifiable artifact here |
|---|---|
| Survey source classes, query-concept families, inclusion/exclusion and retained-corpus audit (with historical search-log limitations) | [`survey/protocol.md`](survey/protocol.md) |
| Result-level evidence definitions (publication status recorded separately) | [`survey/protocol.md`](survey/protocol.md), Section 3 |
| Frozen retained-link census, commit `82b6110` | [`survey/corpus_manifest.json`](/wangxb96/Awesome-EdgeAI/blob/82b6110/survey/corpus_manifest.json), [`survey/repos_manifest.json`](/wangxb96/Awesome-EdgeAI/blob/82b6110/survey/repos_manifest.json) |
| Literature-link audit (arXiv ID ↔ authoritative title, withdrawn check) | [`survey/verify_corpus.py`](survey/verify_corpus.py) |
| Linked tool/model repository reachability audit (live Git HEAD, not ownership verification) | [`survey/verify_repos.py`](survey/verify_repos.py), [`survey/repos_manifest.json`](survey/repos_manifest.json) |
| Future benchmark logging, energy/failure boundaries, and descriptive analysis helper | [`survey/benchmark_protocol.md`](survey/benchmark_protocol.md), [`survey/compute_ci.py`](survey/compute_ci.py) |
| Figure 1 schematic source and editable/vector/raster exports | [`survey/figures/cognitive_edge_overview.py`](survey/figures/cognitive_edge_overview.py), [`survey/figures/cognitive_edge_overview.pdf`](survey/figures/cognitive_edge_overview.pdf), [`survey/figures/cognitive_edge_overview.svg`](survey/figures/cognitive_edge_overview.svg) |
| Analytical weight/KV memory illustration and formula-generated values | [`survey/figures/memory_budget.py`](survey/figures/memory_budget.py), [`PDF`](survey/figures/memory_budget.pdf), [`CSV`](survey/figures/memory_budget_analytical.csv) |
| Deployment feasibility, resource coupling, and workflow evaluation diagrams | [`Python source`](survey/figures/deployment_reasoning.py), [`Placement`](survey/figures/placement_decision.pdf), [`Couplings`](survey/figures/cross_layer_couplings.pdf), [`Workflow`](survey/figures/workflow_evaluation.pdf), [`Communication patterns`](survey/figures/collaboration_patterns.pdf) |
| 2025–2026 literature refresh (39 verified papers) | [2026 Additions](#new-2026-additions-verified-nov-2026) |
| On-device model families and 30+ official tool repositories | [Model Families & Tool Repository Index](#new-on-device-model-families--tool-repository-index) |

**Frozen retained-link census (11 Nov 2026, commit `82b6110`; literature coverage through 10 Nov).** The archived manifests contain **145/145** resolved arXiv identifiers, **0 unresolved** and **0 withdrawal flags**; **137** selected Markdown labels were title-audited, with **9** low-similarity flags manually inspected. The 137 labels are one selected label per labelled arXiv ID, not all link occurrences. Records from 2023-2026 account for **123/145 (84.8%)**. The repository audit records **123/123** linked GitHub roots with a live HEAD at the audit date. These are different counting units, not a study-screening flow, and live HEAD does not establish official ownership or replication support. Recompute the dated counts in a disposable clone:

```bash
# In a disposable clone of this repository:
git checkout --detach 82b6110
python3 survey/verify_corpus.py --offline
python3 survey/verify_repos.py --offline
```

The archived commands reuse saved results and rewrite manifests in that checkout; they do not check current network state. Running without `--offline` performs a new live audit, whose date and commit must be reported separately. The updated protocol and helper on the current branch are separate from the frozen census snapshot; cite their own Git revision when using them.

**Historical benchmark boundary.** Supplement S1 retains incomplete summaries from a `4xRTX 4090 D` server (5 models, 4 nominal context budgets, 10 micro-tasks). These are **E3 exploratory records**, not reproducible validation or a validated within-stack ranking/Pareto frontier. Exact prompts, settings, raw outputs, repetitions, failure denominators, and power attribution were not retained and cannot be restored. Successful-complete-batch selection has unknown bias; averaged context-specific p95 values are not pooled request percentiles. Reported GPU-board J/token is an unverified power/throughput approximation, with unknown four-board attribution and sampling integration; it is not system or edge-device energy. These summaries do not derive the survey recommendations.

**Future-run reporting.** The linked protocol specifies new request-level observations, all failure outcomes, prompt/scorer/configuration provenance, and device/power timing boundaries. The helper reports logged task/batch denominators, unconditional task-attempt success, explicitly conditional status-ok numeric summaries, and empirical request p95. Bootstrap intervals are off by default and require an independently justified repetition grouping. It summarizes supplied energy fields rather than validating power integration, and refuses to synthesize missing inputs. Future logging cannot reconstruct historical measurements.

**Manuscript-side revision deliverables** are kept in a standalone revision package, `paper_10_Cognitive_EC/TMC_Revision_2026-11-10/`: `Summary of Changes.pdf` (the separate point-by-point response), black-text `TMC-2026-05-1923-main.tex/pdf` and `TMC-2026-05-1923-supp.tex/pdf`, plus separate color-coded review copies. Figure 1 is a compact closed-loop schematic with original vector pictograms for the model, runtime, agent, device/edge/cloud tiers, and evaluation metrics. The design takes a restrained hierarchical-flow approach; the marks are conceptual categories, not vendor or product logos. The original May 2026 submission package `TMC_Submission_2026/` is preserved byte-for-byte.

---

## New: 2026 Additions (verified Nov 2026)

> **Scope.** Entries below were added in the November 2026 refresh. Papers are checked against their primary source (arXiv abstract page or publisher DOI record) for title, authors, date, and venue; withdrawn preprints are excluded (e.g. *SplitLite*, arXiv:2608.23018, withdrawn Sep 2026). They complement — not replace — the topic sections below, which retain the full legacy and 2023–2026 collections.

**1) On-device LLM inference, compression & energy** — see [Modern Era](#modern-era-large-models-agents--cognitive-systems-on-edge-20232026) and [Hardware Acceleration](#7-hardware-acceleration-for-edge-ai--llms)

- [Large Models for Small Devices: Recent Advances and Empirical Analysis of Edge AI Deployment](https://arxiv.org/abs/2608.15693) (arXiv, Aug 2026; parts at IEEE CCNC 2026) — real-hardware study on GPU/CPU/Raspberry Pi showing that *what compresses well need not deploy well*: quantization wins for QA while pruning wins for segmentation, and pruning can inflate the deployed artifact by 21–49% by breaking k-quant super-block alignment.
- [EdgeXpert: An Edge Device for Memory-Efficient LLM Inference with Mixture-of-Experts and Speculative Decoding](https://arxiv.org/abs/2608.05303) (MICRO 2026) — 28nm SW/HW co-designed accelerator that reconciles MoE with speculative decoding via prompt-wise expert reuse and depth-aware expert coalescing; up to 56.3% latency and 44.1% energy reduction.
- [SpecQuant: Speculative Decoding with Multi-Parent Quantization for Adaptive LLM Inference](https://arxiv.org/abs/2609.21704) (ICPC2T 2026) — training-free INT4/FP8/FP16 variants derived from shared weights with query-complexity routing; 35–43% speedups within 2% accuracy.
- [EnerInfer: Energy-Aware On-Device LLM Inference](https://arxiv.org/abs/2606.23001) (arXiv, Jun 2026) — jointly manages NPU/DDR frequency for energy efficiency, throughput and thermal comfort; up to 65% better energy efficiency on phones without QoE violations.
- [Does Mixture-of-Experts Actually Help Inference on Consumer and Edge Hardware? An Empirical Study](https://arxiv.org/abs/2606.21428) (arXiv, Jun 2026) — on bandwidth-bound Jetson-class hardware, inference cost tracks *total* parameters rather than active ones: OLMoE trails dense baselines by ~31% at 2.1× energy per token.

**2) Edge agents & edge–cloud collaboration** — see [AI Agents on Edge](#5-ai-agents-on-edge--on-device-agents)

- [Nexus: An Execution Fabric for AI Agents Across Cloud, Edge, and Devices](https://arxiv.org/abs/2610.05709) (arXiv, Oct 2026) — OpenWrt-based persistent-task runtime with run-scoped delegation, journaling and permission revocation for cross-device agent services.
- [EdgeWise: Bringing Long-Horizon Agents to the Edge via Selective Cloud Delegation](https://arxiv.org/abs/2610.17560) (arXiv, Oct 2026, v2) — SLM on device as primary solver with step-level RL delegation; matches pure-LLM execution while cutting inference cost up to 62% (SWE-Rebench) and 34% (Terminal-Bench 2.1).
- [Diffusion Language Models for Mobile Edge Agentic AI: Foundations, Applications, and Challenges](https://arxiv.org/abs/2609.04778) (arXiv, Sep 2026) — survey of non-autoregressive DLMs for edge agents (parallel refinement, early exit, quality–latency elasticity).
- [Empowering Edge Agents: A Systematic Analysis of Edge-Cloud Collaboration in LLM Agent Execution](https://arxiv.org/abs/2610.17816) (arXiv, Oct 2026) — EC²-Bench: 128 executable long-horizon tasks jointly measuring performance, cloud cost and privacy exposure (see also [Section 5](#5-ai-agents-on-edge--on-device-agents)).

**3) Federated learning & on-device training** — see [Federated Learning](#new-federated-learning-on-edge) and [On-Device Training](#new-on-device-training--personalization)

- [Thermo-FL: Thermal-Aware Robust Federated Fine-Tuning of Large Language Models for Edge AI](https://arxiv.org/abs/2608.21172) (arXiv, Aug 2026) — device temperature as an active control signal for LoRA training plus Byzantine-robust aggregation (TERRA), validated on a Jetson testbed.
- [Just Talk Once: Communication-Efficient Split Federated LLM Fine-Tuning on Edge Devices](https://arxiv.org/abs/2609.01457) (MobiHoc 2026) — L-shaped SFT removes the bidirectional split-loop bottleneck; one-shot activation upload lets clients go offline while the server keeps optimizing.
- [Fed-FSTQ: Fisher-Guided Token Quantization for Communication-Efficient Federated Fine-Tuning of LLMs on Edge Devices](https://arxiv.org/abs/2604.25421) (arXiv, Apr 2026, v3) — token-level Fisher sensitivity for mixed-precision adapter updates; 46× less cumulative uplink traffic and 6.16× per-round speedup.
- [Training Specialist LLMs on Your Phone: Forward-Only Optimization via Block-Spectral Coordinates](https://arxiv.org/abs/2611.04797) (arXiv, 3 Nov 2026) — MobileSpec trains 1–5 MB forward-only specialists from verifiable rewards, adapts INT4 models without changing weights, and fine-tunes a personalized 8B model on an iPhone 16 Pro overnight.
- [Memory-Efficient Structured Backpropagation for On-Device LLM Fine-Tuning](https://arxiv.org/abs/2602.13069) (ACL 2026) — MeSP derives mathematically identical LoRA gradients with 49% less memory (361 MB → 136 MB on Qwen2.5-0.5B).
- [TrainDeeploy: Hardware-Accelerated Parameter-Efficient Fine-Tuning of Small Transformer Models at the Extreme Edge](https://arxiv.org/abs/2603.09511) (DATE 2026) — first complete CNN + Transformer on-device training pipeline on a RISC-V heterogeneous ultra-low-power SoC, with selective layer-wise tuning and LoRA.

**4) TinyML & microcontrollers** — see [TinyML](#new-tinyml--microcontroller-ai)

- [What changes after deployment? A survey on On-device Learning in TinyML](https://arxiv.org/abs/2605.31226) (arXiv, May 2026) — ~70 on-device-learning works organized by distribution-change regime; documents the gap between methodological benchmarks and real deployments.
- [AutoMCU: Feasibility-First MCU Neural Network Customization via LLM-based Multi-Agent Systems](https://arxiv.org/abs/2605.21560) (arXiv, May 2026) — hardware-in-the-loop LLM agents filter infeasible designs via vendor-toolchain feedback before training; 1–2 h customization validated on STM32 boards.
- [Ariel-ML: Computing Parallelization with Embedded Rust for Neural Networks on Heterogeneous Multi-core Microcontrollers](https://arxiv.org/abs/2512.09800) (ISIoT 2026; arXiv v2 May 2026) — open-source Rust toolkit for parallel TinyML inference across Arm Cortex-M, RISC-V and ESP32 multicore MCUs.

**5) Security & privacy** — see [Edge AI Security & Privacy](#new-edge-ai-security--privacy)

- [Understanding the Security Boundary of Obfuscation-based On-Device LLM Protection](https://arxiv.org/abs/2609.10117) (ACM CCS 2026) — formalizes obfuscation primitives, exposes a shared vulnerability in top-tier TEE-shielded LLM partition schemes, and extends the security boundary.
- [BiShield-TEE: On the (In-)Security of Unilateral Weight Obfuscation in On-Device TEE-Shielded LLM Partition](https://arxiv.org/abs/2610.21565) (NeurIPS 2026) — bilateral input/output obfuscation inducing ambiguous solutions, closing the "solution determinacy" vulnerability.
- [Protecting On-Device AI Inference: A Systematic Review of Attacks and Defence Mechanisms](https://arxiv.org/abs/2605.29450) (arXiv, May 2026) — first review dedicated to on-device *inference* threats; documents an attack/defence asymmetry (e.g. ~1/3 of attack literature has no corresponding defence).

**6) Multimodal VLMs, embodied AI & hardware measurements** — see [Multimodal & Embodied Edge AI](#new-multimodal--embodied-edge-ai) and [Benchmarks](#8-benchmarks-datasets--tools-20232026-focus)

- [How Far Are We From On-Device VLM Inference? A Measurement Study on Edge NPUs](https://arxiv.org/abs/2610.40039) (arXiv, Oct 2026) — 6 VLMs × 3 edge platforms × 10 multimodal benchmarks; challenges softmax/linear-attention assumptions and identifies task-specific "sweet resolutions".
- [Phase Matters: Characterizing Heterogeneous Vision-Language Inference on a Mobile SoC](https://arxiv.org/abs/2606.27906) (MobiSys Workshop 2026) — Snapdragon 8 Elite study: NPU gives 1.64× on prefill but only 1.18× on decode, with 2.52× lower energy and 10.47 °C lower steady-state temperature.
- [VLA-HWBench: Where the Time Goes When VLA Models Run on Edge Hardware](https://arxiv.org/abs/2610.34717) (arXiv, Oct 2026) — 18 open VLA models on Jetson AGX Thor / Ryzen AI Max+ with a seven-stage latency breakdown; action-generation strategy dominates model size.
- [Deltoris: Enabling Real-time VLA Inference in Embodied AI via Bit-level Sparsity and Speculative Inference](https://arxiv.org/abs/2608.04428) (arXiv, Aug 2026) — temporal bit-sparsity + speculative data loading + systolic bit-serial accelerator; up to 34.2× speedup over mobile GPUs.
- [LLM Inference at the Edge: Mobile, NPU, and GPU Performance Efficiency Trade-offs Under Sustained Load](https://arxiv.org/abs/2603.23640) (arXiv, Mar 2026, v2 Jun 2026) — Qwen2.5-1.5B INT4 across RPi 5 + Hailo-10H, Galaxy S24 Ultra, iPhone 16 Pro and RTX 4050; thermal throttling supersedes peak compute on phones.

**7) 6G, networks & surveys** — see [Edge AI in 6G Networks](#edge-ai-in-6g-networks) and [Recent Surveys](#9-recent-surveys--overviews-20232026)

- [From Semantic to Token Communication: The Next Paradigm for Large-Model-Driven 6G Intelligent Connectivity](https://arxiv.org/abs/2609.10714) (arXiv, Sep 2026) — proposes the LM *token* as a universal semantic unit above the bit level, enabling importance assignment and resource allocation at token granularity for AI-native 6G.
- [LLM-Powered Agentic AI for 5G/6G Networks: A Tutorial and Survey on Architectures, Protocols, and Standardization](https://arxiv.org/abs/2607.16066) (arXiv, Jul 2026) — tutorial/survey mapping agentic capabilities onto 5G/6G control planes, evaluation and standardization.

**8) Newly covered topics: on-device RAG & speech** — these directions were previously only a bullet in [Section 5](#5-ai-agents-on-edge--on-device-agents); they now have primary literature.

- [Energy-Efficient On-Device RAG on a Mobile NPU: System Design and Benchmark on Snapdragon X Elite](https://arxiv.org/abs/2606.11257) (arXiv, Jun 2026) — full embedding / retrieval / reranking / generation pipeline on the Hexagon NPU, benchmarked against CPU and GPU for energy and latency.
- [Lightweight Chunk Selection for Mobile Retrieval-Augmented Generation](https://arxiv.org/abs/2608.03148) (arXiv, Aug 2026) — retains only the most useful retrieved chunk to cut mobile prefill compute and memory.
- [MemLLM: End-to-end In-Storage Acceleration of On-device Retrieval-Augmented Generation using Precomputed KV Caches](https://arxiv.org/abs/2610.22579) (arXiv, Oct 2026) — moves precomputed RAG KV caches into storage to remove the edge prefill bottleneck over a narrow interconnect.
- [Depth through Recurrence: Towards Ultra-Efficient On-Device ASR](https://arxiv.org/abs/2610.37833) (arXiv, Oct 2026) — weight-sharing recurrent blocks retain ASR model depth at a fraction of the parameters for watches and glasses.
- [Offline AI Modules: Voice-First Offline Architecture, Hardware Reference Stack, Quantization and Benchmarking](https://arxiv.org/abs/2610.07026) (arXiv, Oct 2026) — fully offline, low-power voice-first stack with a hardware reference design and benchmarks.
- [SSEmb: Training a Generalizable Speech Retrieval Model Using Only Automatic Speech Recognition Data](https://arxiv.org/abs/2610.17813) (arXiv, Oct 2026) — speech-to-text retrieval without spoken query–document pairs, relevant to on-device voice agents.

**Framework / runtime progress (2026).** Two open-source runtimes complement [Section 6](#6-frameworks--runtimes-for-edge--on-device-deployment-20232026): Google's [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) (cross-platform orchestration for on-device LLM inference with GPU/NPU acceleration, already listed above) and Microsoft's [ONNX Runtime GenAI](https://github.com/microsoft/onnxruntime-genai) (generative-AI loop, logits processing, sampling and KV-cache management for ONNX models across CPU/GPU/NPU backends).

---

## New: On-Device Model Families & Tool Repository Index

> **Why this section.** The tables above catalogue *papers*; this section catalogues the *artifacts* needed to reproduce or deploy them. Every GitHub link below was verified to resolve (via `git ls-remote` against the repository HEAD) on 10 November 2026. Model reports were checked against their arXiv abstract pages; entries without an arXiv report link to official model cards / developer docs instead. Two stale paths (`OpenSparseLLM/OmniQuant`, `ARM-software/ethos-u-vela`) were excluded — OmniQuant is linked at its current home, `OpenGVLab/OmniQuant`.

### A. On-device / small model families (2024–2026)

| Family | Edge-relevant sizes | Report / official documentation | Code / weights |
| ---- | ---- | ---- | ---- |
| Qwen3 | 0.6B / 1.7B / 4B dense | [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388) (2025) — unified thinking / non-thinking modes with a thinking budget | [QwenLM/Qwen3](https://github.com/QwenLM/Qwen3) |
| Gemma 3 / Gemma 3n | 1B / 4B; 3n E2B / E4B | [Gemma 3 Technical Report](https://arxiv.org/abs/2503.19786) (2025); [Gemma 3n developer guide](https://ai.google.dev/gemma/docs/gemma-3n) — MatFormer nested submodels, PLE caching, audio + vision input | [google-deepmind/gemma](https://github.com/google-deepmind/gemma) |
| Phi-4-Mini | 3.8B | [Phi-4-Mini Technical Report](https://arxiv.org/abs/2503.01743) (2025) — compact multimodal model via mixture-of-LoRAs | [microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook) |
| MiniCPM4 | 0.5B / 8B | [MiniCPM4: Ultra-Efficient LLMs on End Devices](https://arxiv.org/abs/2506.07900) (2025) — native sparsity, QAT INT4, CPM.cu inference stack | [OpenBMB/MiniCPM](https://github.com/OpenBMB/MiniCPM) |
| BitNet | 2B, 1.58-bit | [The Era of 1-bit LLMs](https://arxiv.org/abs/2402.17764) (2024); [BitNet b1.58 2B4T Technical Report](https://arxiv.org/abs/2504.12285) (2025) | [microsoft/BitNet](https://github.com/microsoft/BitNet) |
| SmolLM3 / SmolVLM | 3B / 2B | [SmolLM3 release notes](https://huggingface.co/blog/smollm3) (2025) — fully open training recipe, on-device-oriented | [huggingface/smollm](https://github.com/huggingface/smollm) |
| Llama 3.2 | 1B / 3B | [official 1B model card](https://huggingface.co/meta-llama/Llama-3.2-1B) (2024) — pruned / distilled edge sizes | [meta-llama/llama-models](https://github.com/meta-llama/llama-models) |
| MobileLLM / MobileLLM-R1 | 0.1B–1B | [MobileLLM](https://arxiv.org/abs/2402.14905) (2024); [MobileLLM-R1](https://arxiv.org/abs/2509.24945) (2025, already in Section 4) | -- |

This extends the Section 4 roster (MobileLLM / Phi-3 / Qwen2 / MiniCPM-V, all 2024) to the 2025–2026 generation of device-sized models.

### B. Inference engines & runtimes (official repositories)

- [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) — GGUF quantized LLM/VLM inference in C/C++ across CPU, GPU and mobile backends; the de-facto edge baseline.
- [ggml-org/ggml](https://github.com/ggml-org/ggml) — tensor library underlying llama.cpp.
- [ml-explore/mlx-lm](https://github.com/ml-explore/mlx-lm) — Apple Silicon LLM generation / LoRA fine-tuning (companion to `ml-explore/mlx`).
- [microsoft/BitNet](https://github.com/microsoft/BitNet) — official 1-bit LLM inference framework, CPU-first.
- [SJTU-IPADS/PowerInfer](https://github.com/SJTU-IPADS/PowerInfer) — activation-sparsity CPU/GPU hybrid serving for local deployment (code for the PowerInfer papers in Section 4).
- [OAID/Tengine](https://github.com/OAID/Tengine) — lightweight embedded inference with INT8 / NPU support.
- [kvcache-ai/ktransformers](https://github.com/kvcache-ai/ktransformers) — heterogeneous CPU/GPU inference with offloaded experts.
- [InternLM/lmdeploy](https://github.com/InternLM/lmdeploy) — compression, deployment and serving with optimized KV-cache management.
- [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) — Jetson / edge-GPU kernels, paged KV cache, FP4/INT4 quantization and speculative decoding.
- [ollama/ollama](https://github.com/ollama/ollama) and [mudler/LocalAI](https://github.com/mudler/LocalAI) — local model servers commonly used as edge baselines.
- [exo-explore/exo](https://github.com/exo-explore/exo) — splits one model across a cluster of everyday devices.
- [google-ai-edge/mediapipe](https://github.com/google-ai-edge/mediapipe) and [google-ai-edge/ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch) — on-device perception and PyTorch → LiteRT / Qualcomm export.
- [google-ai-edge/model-explorer](https://github.com/google-ai-edge/model-explorer) — visual inspection of large on-device model graphs.

### C. Quantization, compression & PEFT tooling

- [mit-han-lab/llm-awq](https://github.com/mit-han-lab/llm-awq) (AWQ), [mit-han-lab/smoothquant](https://github.com/mit-han-lab/smoothquant) (SmoothQuant), [IST-DASLab/gptq](https://github.com/IST-DASLab/gptq) (GPTQ), [AutoGPTQ/AutoGPTQ](https://github.com/AutoGPTQ/AutoGPTQ), [OpenGVLab/OmniQuant](https://github.com/OpenGVLab/OmniQuant) — reference implementations for the quantization papers in Section 4.
- [intel/neural-compressor](https://github.com/intel/neural-compressor) and [huggingface/optimum](https://github.com/huggingface/optimum) — vendor-neutral / Hugging Face-native quantization pipelines.
- [unslothai/unsloth](https://github.com/unslothai/unsloth) and [bitsandbytes-foundation/bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes) — memory-efficient fine-tuning and low-bit kernels used with LoRA / QLoRA (Section 3).

### D. TinyML / MCU toolchain

- [mlcommons/tiny](https://github.com/mlcommons/tiny) — MLPerf Tiny benchmark suite for ultra-low-power MCUs.
- [mlcommons/inference](https://github.com/mlcommons/inference) — MLPerf Inference, including edge / mobile scenarios.
- [espressif/esp-tflite-micro](https://github.com/espressif/esp-tflite-micro) — TFLM port for ESP32-class boards.
- [emlearn/emlearn](https://github.com/emlearn/emlearn) — classical-ML / tiny-NN inference in C for microcontrollers.

Existing entries in [TinyML Frameworks & Tools](#new-tinyml--microcontroller-ai) (TFLM, CMSIS-NN, microTVM, TinyEngine, MCUNet, Edge Impulse) are retained there.

---

## New: Federated Learning on Edge

Federated Learning (FL) enables collaborative model training across distributed edge devices without centralizing raw data, crucial for privacy-preserving edge AI. Recent advances combine FL with LLMs, PEFT, and heterogeneous edge hardware.

![Federated Learning on Edge](Figures/federated_learning_edge.png)

### Federated Learning Foundations & Systems

| Title & Basic Information | Affiliation | Code |
| ---- | ---- | ---- | 
| [Communication-Efficient Learning of Deep Networks from Decentralized Data (FedAvg)](https://proceedings.mlr.press/v54/mcmahan17a.html) (AISTATS 2017) | Google | -- |
| [Federated Learning: Strategies for Improving Communication Efficiency](https://arxiv.org/abs/1610.05492) (arXiv 2016) | Google | -- |
| [Federated Optimization in Heterogeneous Networks (FedProx)](https://proceedings.mlsys.org/paper/2020/hash/38af86134b65d0f10fe33d30dd76442e-Abstract.html) (MLSys 2020) | University of Michigan | [Code](https://github.com/litian96/FedProx) |
| [SCAFFOLD: Stochastic Controlled Averaging for Federated Learning](https://proceedings.mlr.press/v119/karimireddy20a.html) (ICML 2020) | EPFL | -- |
| [Adaptive Federated Optimization](https://arxiv.org/abs/2003.00295) (ICLR 2021) | Google Research | -- |
| [Federated Learning with Matched Averaging (FedMA)](https://openreview.net/forum?id=BkluqlSFDS) (ICLR 2020) | IBM Research | -- |

### Federated Learning for LLMs & Edge Models

| Title & Basic Information | Affiliation | Code |
| ---- | ---- | ---- | 
| [Federated Learning of Large Language Models with Parameter-Efficient Prompt Tuning and Adaptive Optimization (FedPepTAO)](https://arxiv.org/abs/2310.15080) (EMNLP 2023) | -- | -- |
| [FedPETuning: When Federated Learning Meets the Parameter-Efficient Tuning Methods of Pre-trained Language Models](https://arxiv.org/abs/2212.10025) (arXiv 2022; v2 2023) | HIT Shenzhen / Peng Cheng Lab | -- |
| [Federated Full-Parameter Tuning of Billion-Sized Language Models with Communication Cost under 18 Kilobytes](https://arxiv.org/abs/2312.06353) (ICML 2024) | -- | -- |
| [DeepFusion: Accelerating MoE Training via Federated Knowledge Distillation from Heterogeneous Edge Devices](https://arxiv.org/abs/2602.14301) (arXiv 2026) | -- | -- |
| [FedGen-Edge: Parameter-Efficient and Personalized Federated Training of Generative Models at the Edge](https://arxiv.org/abs/2511.11585) (arXiv 2025) | -- | -- |
| [Federated Black-box Prompt Tuning System for Large Language Models on the Edge](https://doi.org/10.1145/3636534.3698856) (MobiCom 2024) | -- | -- |
| [Training Machine Learning Models at the Edge: A Survey](https://arxiv.org/abs/2403.02619) (arXiv 2024) | -- | -- |
| [Split Learning for Health: Distributed Deep Learning without Sharing Raw Patient Data](https://arxiv.org/abs/1812.00564) (arXiv 2018) | MIT | -- |
| [Efficient Split Learning for Collaborative Edge AI](https://scholar.google.com/scholar?q=%22Efficient+Split+Learning+for+Collaborative+Edge+AI%22) (IEEE IoTJ 2023; publisher link pending verification) | -- | -- |

---

## New: TinyML & Microcontroller AI

TinyML pushes AI inference to ultra-low-power microcontrollers (MCUs) with KB-level memory and mW-level power budgets. The field has rapidly evolved from basic CNNs to on-device Transformers and small language models.

![TinyML Ecosystem](Figures/tinyml_ecosystem_landscape.png)

### Foundational TinyML Papers

| Title & Basic Information | Affiliation | Code |
| ---- | ---- | ---- | 
| [MCUNet: Tiny Deep Learning on IoT Devices](https://proceedings.neurips.cc/paper/2020/hash/86c51678350f656dcc7f490a43946ee5-Abstract.html) (NeurIPS 2020) | MIT HAN Lab | [Code](https://github.com/mit-han-lab/mcunet) |
| [MCUNetV2: Memory-Efficient Patch-based Inference for Tiny Deep Learning](https://proceedings.neurips.cc/paper/2021/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html) (NeurIPS 2021) | MIT HAN Lab | [Code](https://github.com/mit-han-lab/mcunet) |
| [MCUNetV3: On-Device Training Under 256KB Memory](https://proceedings.neurips.cc/paper_files/paper/2022/hash/963ba4661bc7947d498241f7c46e48ba-Abstract.html) (NeurIPS 2022) | MIT HAN Lab | [Code](https://github.com/mit-han-lab/mcunet) |
| [TinyTL: Reduce Memory, Not Parameters for Efficient On-Device Learning](https://proceedings.neurips.cc/paper/2020/hash/81f7acabd411274fcf65ce2070ed568a-Abstract.html) (NeurIPS 2020) | MIT HAN Lab | [Code](https://github.com/mit-han-lab/tinyML) |
| [MicroNets: Neural Network Architectures for Deploying TinyML Applications on Commodity Microcontrollers](https://proceedings.mlsys.org/paper/2021/hash/d67d8ab4f4c10bf22aa353e27879133c-Abstract.html) (MLSys 2021) | Arm Research | -- |
| [Tiny Machine Learning: Progress and Futures](https://arxiv.org/abs/2403.19076) (IEEE CAS Magazine 2024) | MIT HAN Lab | -- |
| [On-Device Training Under 256KB Memory](https://arxiv.org/abs/2206.15472) (NeurIPS 2022) | MIT HAN Lab | [Code](https://github.com/mit-han-lab/tiny-training) |
| [TinyEngine: Efficient Training and Inference on Microcontrollers](https://github.com/mit-han-lab/tinyengine) (2023) | MIT HAN Lab | [Code](https://github.com/mit-han-lab/tinyengine) |

### TinyML Frameworks & Tools

- [TensorFlow Lite for Microcontrollers (TFLM)](https://github.com/tensorflow/tflite-micro) — Google's framework for MCU inference.
- [CMSIS-NN](https://github.com/ARM-software/CMSIS-NN) — ARM's optimized NN kernels for Cortex-M.
- [Edge Impulse](https://www.edgeimpulse.com/) — End-to-end TinyML development platform.
- [Arduino Edge / TinyML Kit](https://www.arduino.cc/) — Arduino's TinyML hardware + software.
- [microTVM](https://tvm.apache.org/docs/topic/microtvm/index.html) — Apache TVM for microcontrollers.
- [Neuton TinyML](https://neuton.ai/) — AutoML for ultra-tiny models.

---

## New: Edge AI Security & Privacy

As edge devices handle increasingly sensitive data with on-device LLMs, security and privacy have become paramount. Key topics include adversarial robustness, model extraction defense, differential privacy, and TEE-based secure inference.

### Security & Adversarial Robustness

| Title & Basic Information | Affiliation | Code |
| ---- | ---- | ---- | 
| [Towards Deep Learning Models Resistant to Adversarial Attacks](https://arxiv.org/abs/1706.06083) (ICLR 2018) | MIT / UC Berkeley | -- |
| [Adversarial Examples for Semantic Segmentation and Object Detection](https://openaccess.thecvf.com/content_ICCV_2017/html/Xie_Adversarial_Examples_for_ICCV_2017_paper.html) (ICCV 2017) | Johns Hopkins | -- |
| [Threat of Adversarial Attacks on Deep Learning in Computer Vision: A Survey](https://ieeexplore.ieee.org/abstract/document/8294186/) (IEEE Access 2018) | -- | -- |
| [Differential Privacy: A Survey of Results](https://link.springer.com/chapter/10.1007/978-3-540-79228-4_1) (TAMC 2008) | Microsoft Research | -- |
| [Speed Kills: Exploring Confused Deputy Attacks Through Edge AI Accelerators](https://arxiv.org/abs/2605.17707) (CVE-2025-66425, arXiv 2026) | -- | -- |
| [Competition for Attention Predicts Good-to-Bad Tipping in Edge AI](https://arxiv.org/abs/2602.14370) (arXiv 2026) | -- | -- |
| [Integer-Arithmetic-Only Certified Robustness for Quantized Neural Networks](https://openaccess.thecvf.com/content/ICCV2021/html/Lin_Integer-Arithmetic-Only_Certified_Robustness_for_Quantized_Neural_Networks_ICCV_2021_paper.html) (ICCV 2021) | USC | -- |

### Privacy-Preserving Edge AI

| Title & Basic Information | Affiliation | Code |
| ---- | ---- | ---- | 
| [Deep Learning with Differential Privacy](https://arxiv.org/abs/1607.00133) (CCS 2016) | Google | -- |
| [Federated Learning with Differential Privacy: Algorithms and Performance Analysis](https://scholar.google.com/scholar?q=%22Federated+Learning+with+Differential+Privacy%3A+Algorithms+and+Performance+Analysis%22) (IEEE TIFS 2020; publisher link pending verification) | -- | -- |
| [When FinTech Meets Privacy: Securing Financial LLMs with Differential Private Fine-Tuning](https://arxiv.org/abs/2509.08995) (arXiv 2025) | -- | -- |
| [SecureInfer: Heterogeneous TEE-GPU Architecture for Privacy-Critical LLM Deployment](https://arxiv.org/abs/2510.19979) (IEEE ICEdge 2025) | -- | -- |
| [On-Device Generative AI for GDPR-Compliant Visual Monitoring](https://arxiv.org/abs/2605.30544) (arXiv 2026) | -- | -- |
| [PolyLink: A Blockchain-Based Decentralized Edge AI Platform for LLM Inference](https://arxiv.org/abs/2510.02395) (arXiv 2025) | PolyU | [Code](https://github.com/IMCL-PolyLink/PolyLink) |
| [Privacy-Preserving Multimodal Wearable for Local Voice-and-Vision Inference](https://arxiv.org/abs/2511.11811) (arXiv 2025) | UMD | -- |
| [Secure Multi-LLM Agentic AI and Agentification for Edge General Intelligence by Zero-Trust](https://arxiv.org/abs/2508.19870) (arXiv 2025) | -- | -- |

---

## New: On-Device Training & Personalization

Beyond inference, enabling on-device training and fine-tuning allows models to adapt to user-specific data and changing environments without privacy leakage.

### On-Device Training & Fine-tuning

| Title & Basic Information | Affiliation | Code |
| ---- | ---- | ---- | 
| [On-Device Training Under 256KB Memory](https://arxiv.org/abs/2206.15472) (NeurIPS 2022) | MIT HAN Lab | [Code](https://github.com/mit-han-lab/tiny-training) |
| [TinyTL: Reduce Memory, Not Parameters for Efficient On-Device Learning](https://proceedings.neurips.cc/paper/2020/hash/81f7acabd411274fcf65ce2070ed568a-Abstract.html) (NeurIPS 2020) | MIT HAN Lab | [Code](https://github.com/mit-han-lab/tinyML) |
| [Enabling On-Device CNN Training by Self-Supervised Instance Filtering and Error Map Pruning](https://ieeexplore.ieee.org/abstract/document/9211513/) (IEEE TCAD 2020) | University of Pittsburgh | -- |
| [Octo: INT8 Training with Loss-aware Compensation and Backward Quantization for Tiny On-device Learning](https://www.usenix.org/system/files/atc21-zhou.pdf) (USENIX ATC 2021) | PolyU | [Code](https://github.com/kimihe/Octo) |
| [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) (ICLR 2022) | Microsoft | [Code](https://github.com/microsoft/LoRA) |
| [QLoRA: Efficient Finetuning of Quantized LLMs](https://proceedings.neurips.cc/paper_files/paper/2023/hash/1feb87871436031bdc0f2beaa62a049b-Abstract.html) (NeurIPS 2023) | University of Washington | [Code](https://github.com/artidoro/qlora) |
| [DoRA: Weight-Decomposed Low-Rank Adaptation](https://arxiv.org/abs/2402.09353) (ICML 2024) | -- | [Code](https://github.com/NVlabs/DoRA) |
| [VeRA: Vector-based Random Matrix Adaptation](https://arxiv.org/abs/2310.11454) (ICLR 2024) | -- | -- |
| [Unlocking the Edge Deployment and On-Device Acceleration of Multi-LoRA Enabled One-for-All Foundational LLM](https://arxiv.org/abs/2604.18655) (ACL 2026) | Samsung | -- |
| [Parameter-Efficient and Personalized Federated Training of Generative Models at the Edge (FedGen-Edge)](https://arxiv.org/abs/2511.11585) (arXiv 2025) | -- | -- |
| [PL-NPU: An Energy-Efficient Edge-Device DNN Training Processor With Posit-Based Logarithm-Domain Computing](https://ieeexplore.ieee.org/abstract/document/9803862/) (IEEE TCAS-I 2022) | Tsinghua | -- |

---

## New: Multimodal & Embodied Edge AI

Multimodal models (vision + language + audio) and embodied AI systems (robots, AR/VR, autonomous vehicles) running on edge devices represent the next frontier. Key challenges include fusing modalities under tight memory/power budgets.

![Edge AI Agent Architecture](Figures/edge_ai_agent_architecture.png)

### Multimodal Models on Edge

| Title & Basic Information | Affiliation | Code |
| ---- | ---- | ---- | 
| [MiniCPM-V: A GPT-4V Level MLLM on Your Phone](https://arxiv.org/abs/2408.01800) (arXiv 2024) | OpenBMB / THU | [Code](https://github.com/OpenBMB/MiniCPM-V) |
| [MiniCPM-o 4.5: Towards Real-Time Full-Duplex Omni-Modal Interaction](https://arxiv.org/abs/2604.27393) (arXiv 2026) | OpenBMB | -- |
| [MobileVLM: Vision-Language Model for Mobile Devices](https://arxiv.org/abs/2312.16886) (arXiv 2023) | Meituan | [Code](https://github.com/Meituan-AutoML/MobileVLM) |
| [LLaVA-1.5: Improved Baselines for Visual Instruction Tuning](https://arxiv.org/abs/2310.03744) (NeurIPS 2024) | UW-Madison / Microsoft | [Code](https://github.com/haotian-liu/LLaVA) |
| [Self-adapting Large Visual-Language Models to Edge Devices Across Visual Modalities](https://doi.org/10.1007/978-3-031-73390-1_18) (ECCV 2024) | -- | -- |
| [VaVLM: Toward Efficient Edge-Cloud Video Analytics With Vision-Language Models](https://doi.org/10.1109/tbc.2025.3549983) (IEEE TBC 2025) | -- | -- |
| [AdaVFM: Adaptive Vision Foundation Models for Edge Intelligence via LLM-Guided Execution](https://arxiv.org/abs/2604.15622) (arXiv 2026; v2 retitled *AdaDINO: Context-Adaptive DINO-Distilled Vision Foundation Models for Efficient Open-Vocabulary Edge Inference*) | Intel Labs / CMU | -- |
| [FastReasonSeg: Fast Reasoning Segmentation for Images and Videos on Edge](https://arxiv.org/abs/2511.12368) (arXiv 2025) | -- | -- |

### Embodied AI & Robotics on Edge

| Title & Basic Information | Affiliation | Code |
| ---- | ---- | ---- | 
| [VLA-Perf: How Fast Can I Run My VLA? Demystifying VLA Inference Performance](https://arxiv.org/abs/2602.18397) (arXiv 2026) | Stanford | -- |
| [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818) (arXiv 2023) | Google DeepMind | -- |
| [Octo: An Open-Source Generalist Robot Policy](https://arxiv.org/abs/2405.12213) (RSS 2024) | UC Berkeley | [Code](https://github.com/octo-models/octo) |
| [π0: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164) (arXiv 2024) | Physical Intelligence | -- |
| [An Agentic AI Framework with LLMs and CoT for UAV-Assisted Logistics Scheduling with MEC](https://arxiv.org/abs/2605.13221) (arXiv 2026) | NTU | -- |

---

## New: Real-World Applications & Case Studies

Edge AI is transforming diverse industries. This section highlights real-world deployments and application-focused research.

### Healthcare & Wellness

| Title & Basic Information | Affiliation | Code |
| ---- | ---- | ---- | 
| [ECG Foundation Models and Medical LLMs for Agentic Cardiovascular Intelligence at the Edge](https://arxiv.org/abs/2604.02501) (arXiv 2026) | KAUST | -- |
| [A Memory-Efficient Retrieval Architecture for RAG-Enabled Wearable Medical LLMs-Agents](https://arxiv.org/abs/2510.27107) (BioCAS 2025) | HKUST | -- |
| [Edge2Analysis: A Novel AIoT Platform for Atrial Fibrillation Recognition and Detection](https://ieeexplore.ieee.org/abstract/document/9769989/) (IEEE JBHI 2022) | Sun Yat-Sen | -- |
| [Accessible Melanoma Detection Using Smartphones and Mobile Image Analysis](https://ieeexplore.ieee.org/abstract/document/8316868/) (IEEE TMM 2018) | SUTD | -- |
| [Edge-Based Compression and Classification for Smart Healthcare Systems](https://www.sciencedirect.com/science/article/pii/S0957417418305967) (ESWA 2019) | Qatar University | -- |

### Smart Home & IoT

| Title & Basic Information | Affiliation | Code |
| ---- | ---- | ---- | 
| [AIoT Smart Home via Autonomous LLM Agents](https://doi.org/10.1109/jiot.2024.3471904) (IEEE IoTJ 2024) | -- | -- |
| [BitRL-Light: 1-bit LLM Agents with DRL for Energy-Efficient Smart Home Lighting](https://arxiv.org/abs/2512.20623) (IPCCC 2025) | -- | -- |
| [VoiceAlign: A Shimming Layer for Enhancing the Usability of Legacy VUI Systems](https://arxiv.org/abs/2602.22374) (IUI 2026) | -- | -- |
| [Privacy-Preserving Multimodal Wearable for Local Voice-and-Vision Inference](https://arxiv.org/abs/2511.11811) (arXiv 2025) | UMD | -- |

### Autonomous Driving & Transportation

| Title & Basic Information | Affiliation | Code |
| ---- | ---- | ---- | 
| [Edge Computing for Autonomous Driving: Opportunities and Challenges](https://ieeexplore.ieee.org/abstract/document/8744265/) (Proc. IEEE 2019) | Wayne State | -- |
| [Edge Intelligence for Autonomous Driving in 6G Wireless System](https://ieeexplore.ieee.org/abstract/document/9430907/) (IEEE Wireless Comm. 2021) | -- | -- |
| [LLM-Generated Fault Scenarios for Evaluating Perception-Driven Lane Following in Autonomous Edge Systems](https://arxiv.org/abs/2604.07362) (arXiv 2026) | -- | -- |
| [Efficient On-Device Training for Object Detection at the Edge](https://openaccess.thecvf.com/content_CVPRW_2020/papers/w28/Farhadi_Enabling_Incremental_Knowledge_Transfer_for_Object_Detection_at_the_Edge_CVPRW_2020_paper.pdf) (CVPRW 2020) | ASU | -- |

### Industrial IoT & Manufacturing

| Title & Basic Information | Affiliation | Code |
| ---- | ---- | ---- | 
| [Edge Computing in Industrial Internet of Things: Architecture, Advances and Challenges](https://ieeexplore.ieee.org/abstract/document/9139976/) (IEEE COMST 2020) | -- | -- |
| [Artificial Intelligence-Driven Mechanism for Edge Computing-Based Industrial Applications](https://ieeexplore.ieee.org/abstract/document/8658105/) (IEEE TII 2019) | -- | -- |
| [A Reconfigurable Method for Intelligent Manufacturing Based on Industrial Cloud and Edge Intelligence](https://ieeexplore.ieee.org/abstract/document/8887246/) (IEEE IoTJ 2019) | -- | -- |
| [Rethinking On-Device LLM Reasoning for IoT DDoS Detection](https://arxiv.org/abs/2601.14343) (arXiv 2026) | -- | -- |

### Edge AI in 6G Networks

| Title & Basic Information | Affiliation | Code |
| ---- | ---- | ---- | 
| [6G Needs Agents: Toward Agentic AI-Native Networks for Autonomous Intelligence](https://arxiv.org/abs/2605.01546) (arXiv 2026) | -- | -- |
| [CORE: Toward Ubiquitous 6G Intelligence Through Collaborative Orchestration of LLM Agents Over Hierarchical Edge](https://arxiv.org/abs/2601.21822) (IEEE Comm. Mag. 2026) | -- | -- |
| [GELATO: Generative Entropy- and Lyapunov-based Adaptive Token Offloading for Device-Edge Speculative LLM Inference](https://arxiv.org/abs/2605.10124) (arXiv 2026) | BJTU | -- |
| [Fast Collaborative Inference via Distributed Speculative Decoding (TSLT)](https://arxiv.org/abs/2512.16273) (arXiv 2025) | -- | -- |
| [Communication-Efficient Collaborative LLM Inference via Distributed Speculative Decoding (TK-SLT)](https://arxiv.org/abs/2509.04576) (WCSP 2025) | -- | -- |
| [A Survey on Cloud-Edge-Terminal Collaborative Intelligence in AIoT Networks](https://arxiv.org/abs/2508.18803) (arXiv 2025) | -- | -- |

---

## Historical Foundations (Legacy v1 Content — fully retained)

**All previous papers, tables, and classic Data-Model-System content from the original v1 survey are preserved below without any deletions.**

---

## 1. Background Knowledge
### 1.1. Edge Computing
Edge computing is a distributed computing paradigm that brings computation and data storage closer to the sources of data generation. This proximity is expected to improve response times, reduce bandwidth consumption, and enable real-time analytics.

![Edge Computing Infrastructure](Figures/Edge_computing_infrastructure.png)

- [What is edge computing? Everything you need to know](https://www.techtarget.com/searchdatacenter/definition/edge-computing)
- [Machine Learning at the Edge — μML](https://heartbeat.comet.ml/machine-learning-at-the-edge-%CE%BCml-2802f1af92de)

### 1.2. Edge AI
Edge AI refers to the deployment of artificial intelligence (AI) algorithms and models directly on edge devices, such as mobile phones, Internet of Things (IoT) devices, and smart sensors. By processing data locally, Edge AI enables real-time decision-making, reduces the need for data transmission to remote servers, and enhances data privacy and security. The proliferation of edge devices and the demand for intelligent, low-latency applications have made Edge AI a critical area of research and development.

#### 1.2.1. Blogs About Edge AI
- [Edge AI – What is it and how does it Work?](https://micro.ai/blog/edge-ai-what-is-it-and-how-does-it-work)
- [What is Edge AI?](https://www.advian.fi/en/what-is-edge-ai)
- [Edge AI – Driving Next-Gen AI Applications in 2022](https://viso.ai/edge-ai/edge-ai-applications-and-trends/)
- [Edge Intelligence: Edge Computing and Machine Learning (2023 Guide)](https://viso.ai/edge-ai/edge-intelligence-deep-learning-with-edge-computing/)
- [What is Edge AI, and how does it work?](https://xailient.com/blog/a-comprehensive-guide-to-edge-ai/)
- [Edge AI 101- What is it, Why is it important, and How to implement Edge AI?](https://www.seeedstudio.com/blog/2021/04/02/edge-ai-what-is-it-and-what-can-it-do-for-edge-iot/)
- [Edge AI: The Future of Artificial Intelligence](https://softtek.eu/en/tech-magazine-en/artificial-intelligence-en/edge-ai-el-futuro-de-la-inteligencia-artificial/)
- [What is Edge AI? Machine Learning + IoT](https://www.digikey.com/en/maker/projects/what-is-edge-ai-machine-learning-iot/4f655838138941138aaad62c170827af)
- [What is edge AI computing?](https://www.telusinternational.com/insights/ai-data/article/what-is-edge-ai-computing)
- [在边缘实现机器学习都需要什么？](https://www.infoq.cn/article/shdudgbwmho0ewwpmk5i)
- [边缘计算 | 在移动设备上部署深度学习模型的思路与注意点](https://www.cnblogs.com/showmeai/p/16627579.html)

## 2. Our Survey (To be released)
### 2.1 The Taxonomy of the Discussed Topics
![Framework](Figures/survey_structureV2.png)

**Edge AI — Unified Taxonomy (New)**:

![Edge AI Unified Taxonomy](Figures/Framework.png)

### 2.2 Edge AI Optimization Triad
We introduce a data-model-system optimization triad for edge deployment.
![Scope](Figures/edge_ai_frameworks.png)
### 2.3 The Edge AI Deployment Pipeline
An overview of edge deployment. The figure shows a general pipeline from the three aspects of data, model and system. Note that not all steps are necessary in real applications.
![Pipeline](Figures/edge_deployment_pipeline.png)

**Research Scope Overview — Edge AI**:

![Research Scope](Figures/research_scope.png)


##  3. The Data-Model-System Optimization Triad
### 3.1. Data Optimization
An overview of data optimization operations. Data cleaning improves data quality by removing errors and inconsistencies in the raw data. Feature compression is used to eliminate irrelevant and redundant features. For scarce data, data augmentation is employed to increase the data size.
![Data](Figures/data_optimization.png)

#### 3.1.1. Data Cleaning
| Title & Basic Information | Affiliation | Code |
| ---- | ---- | ---- | 
| [Active label cleaning for improved dataset quality under resource constraints[J]. Nature communications, 2022.](https://www.nature.com/articles/s41467-022-28818-3) | Microsoft Research Cambridge |  [Code](https://github.com/microsoft/InnerEye-DeepLearning/tree/1606729c7a16e1bfeb269694314212b6e2737939/InnerEye-DataQuality) |
| [Locomotion mode recognition using sensory data with noisy labels: A deep learning approach. IEEE Trans. on Mobile Computing.](https://ieeexplore.ieee.org/abstract/document/9653808/) | Indian Institute of Technology BHU Varanasi | [Code](https://github.com/errahulm/LRNL_approach) |
| [Big data cleaning based on mobile edge computing in industrial sensor-cloud[J]. IEEE Trans. on Industrial Informatics, 2019.](https://ieeexplore.ieee.org/abstract/document/8822503/) | Huaqiao University | -- |
| [Federated data cleaning: Collaborative and privacy-preserving data cleaning for edge intelligence[J]. IoTJ, 2020.](https://ieeexplore.ieee.org/abstract/document/9210000/) | Xidian University | -- |
| [A data stream cleaning system using edge intelligence for smart city industrial environments[J]. IEEE Trans. on Industrial Informatics, 2021.](https://ieeexplore.ieee.org/abstract/document/9424956/) | Hangzhou Dianzi University | -- |
| [Protonn: Compressed and accurate knn for resource-scarce devices[C] ICML, 2017.](https://proceedings.mlr.press/v70/gupta17a.html) | Microsoft Research, India | [Code](https://github.com/Microsoft/ELL) |
| [Intelligent data collaboration in heterogeneous-device iot platforms[J]. ACM Trans. on Sensor Networks (TOSN), 2021.](https://dl.acm.org/doi/abs/10.1145/3427912) | Hangzhou Dianzi University | -- |


#### 3.1.2. Feature Compression
##### 3.1.2.1. Feature Selection
| Title & Basic Information | Affiliation | Code |
| ---- | ---- | ---- | 
| [Accessible melanoma detection using smartphones and mobile image analysis[J]. IEEE Trans. on Multimedia, 2018.](https://ieeexplore.ieee.org/abstract/document/8316868/) | Singapore University of Technology and Design | -- |
| [ActID: An efficient framework for activity sensor based user identification[J]. Computers & Security, 2021.](https://sciencedirect.53yu.com/science/article/pii/S0167404821001437) | University of Houston-Clear Lake | -- |
| [Descriptor Scoring for Feature Selection in Real-Time Visual Slam[C] ICIP, 2020.](https://cz5waila03cyo0tux1owpyofgoryroob.oss-cn-beijing.aliyuncs.com/17/B9/05/17B90503C6B685151A7C1EC364D10815.pdf) | Processor Architecture Research Lab, Intel Labs | -- |
| [Edge2Analysis: a novel AIoT platform for atrial fibrillation recognition and detection[J]. IEEE Journal of Biomedical and Health Informatics, 2022.](https://ieeexplore.ieee.org/abstract/document/9769989/) | Sun Yat-Sen University | -- |
| [Feature selection with limited bit depth mutual information for portable embedded systems[J]. Knowledge-Based Systems, 2020.](https://sci-hub.et-fine.com/10.1016/j.knosys.2020.105885) | CITIC, Universidade da Coruña | -- |
| [Seremas: Self-resilient mobile autonomous systems through predictive edge computing[C] SECON, 2021.](https://ieeexplore.ieee.org/abstract/document/9491618/) | University of California, Irvine | -- |
| [A covid-19 detection algorithm using deep features and discrete social learning particle swarm optimization for edge computing devices[J]. ACM Trans. on Internet Technology (TOIT), 2021.](https://dl.acm.org/doi/abs/10.1145/3453170) | Hubei Province Key Laboratory of Intelligent Information Processing and Real-time Industrial System | -- |

##### 3.1.2.2. Feature Extraction
| Title & Basic Information | Affiliation | Code |
| ---- | ---- | ---- | 
| [Supervised compression for resource-constrained edge computing systems[C] WACV, 2022.](https://openaccess.thecvf.com/content/WACV2022/html/Matsubara_Supervised_Compression_for_Resource-Constrained_Edge_Computing_Systems_WACV_2022_paper.html) | University of California, Irvine | [Code](https://github.com/yoshitomo-matsubara/supervised-compression) |
| ["Blessing of dimensionality: High-dimensional feature and its efficient compression for face verification." CVPR, 2013.](https://www.cv-foundation.org/openaccess/content_cvpr_2013/html/Chen_Blessing_of_Dimensionality_2013_CVPR_paper.html) | University of Science and Technology of China | -- |
| [Toward intelligent sensing: Intermediate deep feature compression[J]. TIP, 2019.](https://ieeexplore.ieee.org/abstract/document/8848858/) | Nangyang Technological University | -- | 
| [Selective feature compression for efficient activity recognition inference[C] ICCV, 2021.](http://openaccess.thecvf.com/content/ICCV2021/html/Liu_Selective_Feature_Compression_for_Efficient_Activity_Recognition_Inference_ICCV_2021_paper.html) | Amazon Web Services | -- |
| [Video coding for machines: A paradigm of collaborative compression and intelligent analytics[J]. TIP, 2020.](https://ieeexplore.ieee.org/abstract/document/9180095/) | Peking University | -- |
| [Communication-computation trade-off in resource-constrained edge inference[J]. IEEE Communications Magazine, 2020.](https://ieeexplore.ieee.org/abstract/document/9311935/) | The Hong Kong Polytechnic University | [Code](https://github.com/shaojiawei07/Edge_Inference_three-step_framework) |
| [Edge-based compression and classification for smart healthcare systems: Concept, implementation and evaluation[J]. ESWA, 2019.](https://www.sciencedirect.com/science/article/pii/S0957417418305967) | Qatar University | -- |
| [EFCam: Configuration-adaptive fog-assisted wireless cameras with reinforcement learning[C] SECON, 2021.](https://ieeexplore.ieee.org/abstract/document/9491609/) | Nanyang Technological University | -- | 
| [Edge computing for smart health: Context-aware approaches, opportunities, and challenges[J]. IEEE Network, 2019.](https://ieeexplore.ieee.org/abstract/document/8674240/) | Qatar University | -- |
| [DEEPEYE: A deeply tensor-compressed neural network for video comprehension on terminal devices[J]. TECS, 2020.](https://dl.acm.org/doi/abs/10.1145/3381805) | Shanghai Jiao Tong University | -- |
| [CROWD: crow search and deep learning based feature extractor for classification of Parkinson’s disease[J]. TOIT, 2021.](https://dl.acm.org/doi/abs/10.1145/3418500) | Taif University | -- |
| ["Deep-Learning Based Monitoring Of Fog Layer Dynamics In Wastewater Pumping Stations", Water research 202 (2021): 117482.](https://cz5waila03cyo0tux1owpyofgoryroob.oss-cn-beijing.aliyuncs.com/50/65/C8/5065C803C133DF389836C73A6267F1E0.pdf) | Deltares | -- |
| [Distributed and efficient object detection via interactions among devices, edge, and cloud[J]. IEEE Trans. on Multimedia, 2019.](https://ieeexplore.ieee.org/abstract/document/8695132/) | Central South University | -- |

#### 3.1.3. Data Augmentation
| Title & Basic Information | Affiliation | Code |
| ---- | ---- | ---- | 
| [An effective litchi detection method based on edge devices in a complex scene[J]. Biosystems Engineering, 2022.](https://sciencedirect.53yu.com/science/article/pii/S1537511022001714) | Beihang University | -- |
| [Segmentation of drivable road using deep fully convolutional residual network with pyramid pooling[J]. Cognitive Computation, 2018.](https://linkspringer.53yu.com/article/10.1007/s12559-017-9524-y) | Tsinghua University | -- |
| [Multiuser physical layer authentication in internet of things with data augmentation[J]. IoTJ, 2019.](https://ieeexplore.ieee.org/abstract/document/8935162/) | University of Electronic Science and Technology of China | -- |
| [Data-augmentation-based cellular traffic prediction in edge-computing-enabled smart city[J]. TII, 2020.](https://ieeexplore.ieee.org/abstract/document/9140397/) | University of Electronic Science and Technology of China | -- |
| [Towards light-weight and real-time line segment detection[C] AAAI, 2022.](https://ojs.aaai.org/index.php/AAAI/article/view/19953) | NAVER/LINE Corp. | [Code](https://github.com/navervision/mlsd) |
| [Intrusion Detection System After Data Augmentation Schemes Based on the VAE and CVAE[J]. IEEE Trans. on Reliability, 2022.](https://ieeexplore.ieee.org/abstract/document/9761959/) | Guangdong Ocean University | -- |
| [Magicinput: Training-free multi-lingual finger input system using data augmentation based on mnists[C] ICIP, 2021.](https://dl.acm.org/doi/abs/10.1145/3412382.3458261) | Shanghai Jiao Tong University | -- |


### 3.2. Model Optimization
An overview of model optimization operations. Model design involves creating lightweight models through manual and automated techniques, including architecture selection, parameter tuning, and regularization. Model compression involves using various techniques, such as pruning, quantization, and knowledge distillation, to reduce the size of the model and obtain a compact model that requires fewer resources while maintaining high accuracy.
![Model](Figures/model_optimization.png)

#### 3.2.1. Model Design
##### 3.2.1.1. Compact Architecture Design
| Title & Basic Information | Affiliation | Code |
| ---- | ---- | ---- | 
| [Mobilenets: Efficient convolutional neural networks for mobile vision applications[J]. arXiv, 2017.](https://arxiv.53yu.com/abs/1704.04861) | Google Inc. | [Code](https://github.com/Zehaos/MobileNet) |
| [Mobilenetv2: Inverted residuals and linear bottlenecks[C] CVPR, 2018.](http://openaccess.thecvf.com/content_cvpr_2018/html/Sandler_MobileNetV2_Inverted_Residuals_CVPR_2018_paper.html) | Google Inc. | [Code](https://github.com/d-li14/mobilenetv2.pytorch) |  
| [Searching for mobilenetv3[C]// ICCV, 2019.](http://openaccess.thecvf.com/content_ICCV_2019/html/Howard_Searching_for_MobileNetV3_ICCV_2019_paper.html) | Google Inc. | [Code](https://github.com/xiaolai-sqlai/mobilenetv3) | 
| [Rethinking bottleneck structure for efficient mobile network design[C] ECCV, 2020.](https://arxiv.org/abs/2007.02269) | National University of Singapore | [Code](https://github.com/zhoudaquan/rethinking_bottleneck_design) |
| [Mnasnet: Platform-aware neural architecture search for mobile[C] CVPR, 2019.](http://openaccess.thecvf.com/content_CVPR_2019/html/Tan_MnasNet_Platform-Aware_Neural_Architecture_Search_for_Mobile_CVPR_2019_paper) | Google Brain | [Code](https://github.com/tensorflow/tpu/tree/master/models/official/mnasnet) |
| [Shufflenet: An extremely efficient convolutional neural network for mobile devices[C] CVPR, 2018.](http://openaccess.thecvf.com/content_cvpr_2018/html/Zhang_ShuffleNet_An_Extremely_CVPR_2018_paper.html) | Megvii Inc (Face++) | [Code](https://github.com/megvii-model/ShuffleNet-Series/tree/master/ShuffleNetV1) |
| [Shufflenet v2: Practical guidelines for efficient cnn architecture design[C] ECCV, 2018.](http://openaccess.thecvf.com/content_ECCV_2018/html/Ningning_Light-weight_CNN_Architecture_ECCV_2018_paper.html) | Megvii Inc (Face++) | [Code](https://github.com/megvii-model/ShuffleNet-Series/tree/master/ShuffleNetV2) |
| [Single path one-shot neural architecture search with uniform sampling[C] ECCV, 2020.](https://linkspringer.53yu.com/chapter/10.1007/978-3-030-58517-4_32) | Megvii Inc (Face++) | [Code](https://github.com/megvii-model/ShuffleNet-Series/tree/master/OneShot) |
| [SqueezeNet: AlexNet-level accuracy with 50x fewer parameters and< 0.5 MB model size[J]. arXiv, 2016.](https://arxiv.53yu.com/abs/1602.07360) | DeepScale∗ & UC Berkeley | [Code](https://github.com/forresti/SqueezeNet) |
| [Squeezenext: Hardware-aware neural network design[C] CVPR Workshops. 2018.](https://openaccess.thecvf.com/content_cvpr_2018_workshops/w33/html/Gholami_SqueezeNext_Hardware-Aware_Neural_CVPR_2018_paper.html) | UC Berkeley | [Code](https://github.com/Timen/squeezenext-tensorflow) |
| [Ghostnet: More features from cheap operations[C] CVPR, 2020.](http://openaccess.thecvf.com/content_CVPR_2020/html/Han_GhostNet_More_Features_From_Cheap_Operations_CVPR_2020_paper.html) | Noah’s Ark Lab, Huawei Technologies | [Code](https://github.com/huawei-noah/ghostnet) |
| [Efficientnet: Rethinking model scaling for convolutional neural networks[C] ICML, 2019.](http://proceedings.mlr.press/v97/tan19a.html) | Google Brain | [Code](https://github.com/lukemelas/EfficientNet-PyTorch) |
| [Efficientnetv2: Smaller models and faster training[C] ICML, 2021.](http://proceedings.mlr.press/v139/tan21a.html) | Google Brain | [Code](https://github.com/google/automl/tree/master/efficientnetv2) |
| [Efficientdet: Scalable and efficient object detection[C] CVPR, 2020.](http://openaccess.thecvf.com/content_CVPR_2020/html/Tan_EfficientDet_Scalable_and_Efficient_Object_Detection_CVPR_2020_paper.html) | Google Brain | [Code](https://github.com/google/automl/tree/master/efficientdet) |
| [Condensenet: An efficient densenet using learned group convolutions[C] CVPR, 2018.](http://openaccess.thecvf.com/content_cvpr_2018/html/Huang_CondenseNet_An_Efficient_CVPR_2018_paper.html) | Cornell University | [Code](https://github.com/ShichenLiu/CondenseNet) |
| [Condensenet v2: Sparse feature reactivation for deep networks[C] CVPR, 2021.](http://openaccess.thecvf.com/content/CVPR2021/html/Yang_CondenseNet_V2_Sparse_Feature_Reactivation_for_Deep_Networks_CVPR_2021_paper.html) | Tsinghua University |[Code](https://github.com/jianghaojun/CondenseNetV2) |
| [Espnet: Efficient spatial pyramid of dilated convolutions for semantic segmentation[C] ECCV, 2018.](http://openaccess.thecvf.com/content_ECCV_2018/html/Sachin_Mehta_ESPNet_Efficient_Spatial_ECCV_2018_paper.html) | University of Washington | [Code](https://github.com/sacmehta/ESPNet/) |
| [Espnetv2: A light-weight, power efficient, and general purpose convolutional neural network[C] CVPR, 2019.](http://openaccess.thecvf.com/content_CVPR_2019/html/Mehta_ESPNetv2_A_Light-Weight_Power_Efficient_and_General_Purpose_Convolutional_Neural_CVPR_2019_paper.html) | University of Washington | [Code](https://github.com/sacmehta/ESPNetv2) |
| [Fbnet: Hardware-aware efficient convnet design via differentiable neural architecture search[C] CVPR, 2019.](http://openaccess.thecvf.com/content_CVPR_2019/html/Wu_FBNet_Hardware-Aware_Efficient_ConvNet_Design_via_Differentiable_Neural_Architecture_Search_CVPR_2019_paper.html) | UC Berkeley | [Code](https://github.com/facebookresearch/mobile-vision) |
| [Fbnetv2: Differentiable neural architecture search for spatial and channel dimensions[C] CVPR, 2020.](https://openaccess.thecvf.com/content_CVPR_2020/papers/Wan_FBNetV2_Differentiable_Neural_Architecture_Search_for_Spatial_and_Channel_Dimensions_CVPR_2020_paper.pdf) | UC Berkeley | [Code](https://github.com/facebookresearch/mobile-vision) |
| [Fbnetv3: Joint architecture-recipe search using predictor pretraining[C] CVPR, 2021.](https://openaccess.thecvf.com/content/CVPR2021/papers/Dai_FBNetV3_Joint_Architecture-Recipe_Search_Using_Predictor_Pretraining_CVPR_2021_paper.pdf) | Facebook Inc. & UC Berkeley | -- |
| [Pelee: A real-time object detection system on mobile devices[J]. NeurIPS, 2021.](https://proceedings.neurips.cc/paper/2018/file/9908279ebbf1f9b250ba689db6a0222b-Paper.pdf) | University of Western Ontario | [Code](https://github.com/Robert-JunWang/Pelee) |
| [Going deeper with convolutions[C] CVPR, 2015.](https://www.cv-foundation.org/openaccess/content_cvpr_2015/papers/Szegedy_Going_Deeper_With_2015_CVPR_paper.pdf) | Google Inc. | [Code](https://github.com/conan7882/GoogLeNet-Inception) |
| [Batch normalization: Accelerating deep network training by reducing internal covariate shift[C] ICML, 2015.](https://arxiv.org/pdf/1502.03167.pdf) | Google Inc. | [Code](https://github.com/shanglianlm0525/PyTorch-Networks/blob/master/ClassicNetwork/InceptionV2.py) |
| [Rethinking the inception architecture for computer vision[C]// CVPR, 2016.](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Szegedy_Rethinking_the_Inception_CVPR_2016_paper.pdf) | Google Inc. | [Code](https://github.com/shanglianlm0525/PyTorch-Networks/blob/master/ClassicNetwork/InceptionV3.py) |
| [Inception-v4, inception-resnet and the impact of residual connections on learning[C] AAAI, 2017.](https://ojs.aaai.org/index.php/aaai/article/view/11231) | Google Inc. | [Code](https://github.com/shanglianlm0525/PyTorch-Networks/blob/master/ClassicNetwork/InceptionV4.py) |
| [Xception: Deep learning with depthwise separable convolutions[C] CVPR, 2017.](https://openaccess.thecvf.com/content_cvpr_2017/papers/Chollet_Xception_Deep_Learning_CVPR_2017_paper.pdf) | Google, Inc. | [Code](https://github.com/weiaicunzai/pytorch-cifar100/blob/master/models/xception.py) |
| [Mobilevit: light-weight, general-purpose, and mobile-friendly vision transformer[J]. arXiv, 2021.](https://arxiv.org/pdf/2110.02178.pdf) | Apple | [Code](https://github.com/apple/ml-cvnets) |
| [Lite transformer with long-short range attention[J]. arXiv, 2020.](https://arxiv.org/pdf/2004.11886.pdf) | Massachusetts Institute of Technology | [Code](https://github.com/mit-han-lab/lite-transformer) |
| [Coordinate attention for efficient mobile network design[C] CVPR, 2021.](https://openaccess.thecvf.com/content/CVPR2021/papers/Hou_Coordinate_Attention_for_Efficient_Mobile_Network_Design_CVPR_2021_paper.pdf) | National University of Singapore | [Code](https://github.com/houqb/CoordAttention) |
| [ECA-Net: Efficient channel attention for deep convolutional neural networks[C] CVPR, 2020.](https://openaccess.thecvf.com/content_CVPR_2020/papers/Wang_ECA-Net_Efficient_Channel_Attention_for_Deep_Convolutional_Neural_Networks_CVPR_2020_paper.pdf) | Tianjin University | [Code](https://github.com/BangguWu/ECANet) |
| [Sa-net: Shuffle attention for deep convolutional neural networks[C] ICASSP, 2021.](https://ieeexplore.ieee.org/abstract/document/9414568) | Nanjing University | [Code](https://github.com/wofmanaf/SA-Net) |
| [Triplet Attention: Rethinking the Similarity in Transformers[C] KDD, 2021.](https://dl.acm.org/doi/abs/10.1145/3447548.3467241) | Beihang University | [Code](https://github.com/zhouhaoyi/TripletAttention) |
| [Resnest: Split-attention networks[C] CVPR, 2020.](https://openaccess.thecvf.com/content/CVPR2022W/ECV/papers/Zhang_ResNeSt_Split-Attention_Networks_CVPRW_2022_paper.pdf) | Meta | [Code](https://github.com/zhanghang1989/ResNeSt) |    

#### 3.2.1.2. Neural Architecture Search (NAS)
| Title & Basic Information | Affiliation | Code |
| ---- | ---- | ---- | 
| [FTT-NAS: Discovering fault-tolerant convolutional neural architecture[J]. TODAES), 2021.](https://dl.acm.org/doi/abs/10.1145/3460288) | Tsinghua University | [Code](https://github.com/walkerning/aw_nas) |
| [An adaptive neural architecture search design for collaborative edge-cloud computing[J]. IEEE Network, 2021.](https://ieeexplore.ieee.org/abstract/document/9606812/) | Nanjing University of Posts and Telecommunications | -- |
| [Binarized neural architecture search for efficient object recognition[J]. IJCV, 2021.](https://linkspringer.53yu.com/article/10.1007/s11263-020-01379-y) | Beihang University | -- |
| [Multiobjective reinforcement learning-based neural architecture search for efficient portrait parsing[J]. IEEE Trans. on Cybernetics, 2021.](https://ieeexplore.ieee.org/abstract/document/9524839/) | University of Electronic Science and Technology of China | -- |
| [Intermittent-aware neural architecture search[J]. ACM Transactions on Embedded Computing Systems (TECS), 2021.](https://dl.acm.org/doi/abs/10.1145/3476995) | Academia Sinica and National Taiwan University | [Code](https://github.com/EMCLab-Sinica/Intermittent-aware-NAS) |
| [Hardcore-nas: Hard constrained differentiable neural architecture search[C] ICML, 2021.](http://proceedings.mlr.press/v139/nayman21a.html) | Alibaba Group, Tel Aviv, Israel | [Code](https://github.com/Alibaba-MIIL/HardCoReNAS) |
| [MemNAS: Memory-efficient neural architecture search with grow-trim learning[C] CVPR, 2020.](http://openaccess.thecvf.com/content_CVPR_2020/html/Liu_MemNAS_Memory-Efficient_Neural_Architecture_Search_With_Grow-Trim_Learning_CVPR_2020_paper.html) | Beijing University of Posts and Telecommunications | -- |
| [Pvnas: 3D neural architecture search with point-voxel convolution[J]. TPAMI, 2021.](https://ieeexplore.ieee.org/abstract/document/9527118/) | Massachusetts Institute of Technology | -- |
| [Toward tailored models on private aiot devices: Federated direct neural architecture search[J]. IoTJ, 2022.](https://ieeexplore.ieee.org/abstract/document/9721425/) | Northeastern University, Qinhuangdao | -- |
| [Automatic design of convolutional neural network architectures under resource constraints[J]. TNNLS, 2021.](https://ieeexplore.ieee.org/abstract/document/9609007/) | Sichuan University | -- |


### 3.2.2. Model Compression
#### 3.2.2.1. Model Pruning
| Title & Basic Information | Affiliation | Code |
| ---- | ---- | ---- | 
| [Supervised compression for resource-constrained edge computing systems[C] WACV, 2022.](https://openaccess.thecvf.com/content/WACV2022/html/Matsubara_Supervised_Compression_for_Resource-Constrained_Edge_Computing_Systems_WACV_2022_paper.html) | University of Pittsburgh | -- |
| [Train big, then compress: Rethinking model size for efficient training and inference of transformers[C] ICML, 2020.](http://proceedings.mlr.press/v119/li20m.html) | UC Berkeley | -- |
| [Hrank: Filter pruning using high-rank feature map[C]// CVPR, 2020.](http://openaccess.thecvf.com/content_CVPR_2020/html/Lin_HRank_Filter_Pruning_Using_High-Rank_Feature_Map_CVPR_2020_paper.html) |  Xiamen University | [Code](https://github.com/lmbxmu/HRank) | 
| [Clip-q: Deep network compression learning by in-parallel pruning-quantization[C] CVPR, 2018.](http://openaccess.thecvf.com/content_cvpr_2018/html/Tung_CLIP-Q_Deep_Network_CVPR_2018_paper.html) | Simon Fraser University | -- |
| [Sparse: Sparse architecture search for cnns on resource-constrained microcontrollers[J]. NeurIPS, 2019.](https://proceedings.neurips.cc/paper/2019/hash/044a23cadb567653eb51d4eb40acaa88-Abstract.html) | Arm ML Research | -- |
| [Deepadapter: A collaborative deep learning framework for the mobile web using context-aware network pruning[C] INFOCOM, 2020.](https://ieeexplore.ieee.org/abstract/document/9155379/) |  Beijing University of Posts and Telecommunications | -- |
| [SCANN: Synthesis of compact and accurate neural networks[J]. IEEE Trans. on Computer-Aided Design of Integrated Circuits and Systems, 2021.](https://ieeexplore.ieee.org/abstract/document/9552199/) | Princeton University | -- |
| [Directx: Dynamic resource-aware cnn reconfiguration framework for real-time mobile applications[J]. IEEE Trans. on Computer-Aided Design of Integrated Circuits and Systems, 2020.](https://ieeexplore.ieee.org/abstract/document/9097286/) | George Mason University | -- |
| [Pruning deep reinforcement learning for dual user experience and storage lifetime improvement on mobile devices[J]. IEEE Trans. on Computer-Aided Design of Integrated Circuits and Systems, 2020.](https://ieeexplore.ieee.org/abstract/document/9211447/) | City University of Hong Kong | -- |
| [SuperSlash: A unified design space exploration and model compression methodology for design of deep learning accelerators with reduced off-chip memory access volume[J]. IEEE Trans. on Computer-Aided Design of Integrated Circuits and Systems, 2020.](https://ieeexplore.ieee.org/abstract/document/9211496/) | Information Technology University | -- |
| [Penni: Pruned kernel sharing for efficient CNN inference[C] ICML, 2020.](http://proceedings.mlr.press/v119/li20d.html) | Duke University | [Code](https://github.com/timlee0212/PENNI) | 
| [Fast operation mode selection for highly efficient iot edge devices[J]. IEEE Trans. on Computer-Aided Design of Integrated Circuits and Systems, 2019.](https://ieeexplore.ieee.org/abstract/document/8634947) | Karlsruhe Institute of Technology | -- |
| [Efficient on-chip learning for optical neural networks through power-aware sparse zeroth-order optimization[C] AAAI, 2021.](https://ojs.aaai.org/index.php/AAAI/article/view/16928) | University of Texas at Austin | -- |
| [A Fast Post-Training Pruning Framework for Transformers[C]// NeurIPS](https://arxiv.org/pdf/2204.09656.pdf) | UC Berkeley |  [Code](https://github.com/WoosukKwon/retraining-free-pruning) |
| [Radio frequency fingerprinting on the edge[J]. TMC, 2021.](https://ieeexplore.ieee.org/abstract/document/9372779/) | Northeastern University, Boston | -- |
| [Exploring sparsity in image super-resolution for efficient inference[C] CVPR, 2021.](https://openaccess.thecvf.com/content/CVPR2021/html/Wang_Exploring_Sparsity_in_Image_Super-Resolution_for_Efficient_Inference_CVPR_2021_paper.html?ref=https://githubhelp.com) | National University of Defense Technology | [Code](https://github.com/LongguangWang/SMSR) |
| [O3BNN-R: An out-of-order architecture for high-performance and regularized BNN inference[J]. TPDS, 2020.](https://ieeexplore.ieee.org/abstract/document/9154597/) | Boston University | -- |
| [Enabling on-device cnn training by self-supervised instance filtering and error map pruning[J]. TCAD, 2020.](https://ieeexplore.ieee.org/abstract/document/9211513/) | University of Pittsburgh | -- |
| [Dropnet: Reducing neural network complexity via iterative pruning[C] ICML, 2020.](http://proceedings.mlr.press/v119/tan20a.html) | National University of Singapore | [Code](https://github.com/tanchongmin/DropNet) |
| [Edgebert: Sentence-level energy optimizations for latency-aware multi-task nlp inference[C] MICRO-54, 2021.](https://dl.acm.org/doi/abs/10.1145/3466752.3480095) | Harvard University | [Code](https://github.com/harvard-acc/EdgeBERT) |
| [Fusion-catalyzed pruning for optimizing deep learning on intelligent edge devices[J]. TCAD, 2020.](https://ieeexplore.ieee.org/abstract/document/9211462/) | Chinese Academy of Sciences | -- |
| [3D CNN acceleration on FPGA using hardware-aware pruning[C] DAC, 2020.](https://ieeexplore.ieee.org/abstract/document/9218571/) | Northeastern University, MA | -- |
| [Width & depth pruning for vision transformers[C] AAAI, 2020.](https://ojs.aaai.org/index.php/AAAI/article/view/20222) | Institute of Computing Technology, Chinese Academy of Sciences | -- |
| [Prive-hd: Privacy-preserved hyperdimensional computing[C] DAC, 2020.](https://ieeexplore.ieee.org/abstract/document/9218493/) | UC San Diego | -- |
| [NestFL: efficient federated learning through progressive model pruning in heterogeneous edge computing[C] MobiCom, 2022.](https://dl.acm.org/doi/abs/10.1145/3495243.3558248) | Purple Mountain Laboratories, Nanjing | -- |


### 3.2.2.2. Parameter Sharing 
| Title & Basic Information | Affiliation | Code |
| ---- | ---- | ---- | 
| [Deep k-means: Re-training and parameter sharing with harder cluster assignments for compressing deep convolutions[C] ICML, 2018.](http://proceedings.mlr.press/v80/wu18h.html) | Texas A&M University | [Code](https://github.com/Sandbox3aster/Deep-K-Means) |
| [T-basis: a compact representation for neural networks[C] ICML, 2020.](http://proceedings.mlr.press/v119/obukhov20a/obukhov20a.pdf) | ETH Zurich | [Code](http://obukhov.ai/tbasis) |
| [ "Soft Weight-Sharing for Neural Network Compression." International Conference on Learning Representations.](https://arxiv.org/pdf/1702.04008.pdf) | University of Amsterdam | [Code](https://github.com/KarenUllrich/Tutorial-SoftWeightSharingForNNCompression) |
| [ShiftAddNAS: Hardware-inspired search for more accurate and efficient neural networks[C] ICML, 2022.](https://proceedings.mlr.press/v162/you22a.html) | Rice University | [Code](https://github.com/RICE-EIC/ShiftAddNAS) |
| [EfficientTDNN: Efficient architecture search for speaker recognition[J]. IEEE/ACM Trans. on Audio, Speech, and Language Processing, 2022.](https://ieeexplore.ieee.org/abstract/document/9798861/) | Tongji University | [Code](https://github.com/mechanicalsea/sugar) |
| [A generic network compression framework for sequential recommender systems[C] SIGIR, 2020.](https://dl.acm.org/doi/abs/10.1145/3397271.3401125) | University of Science and Technology | [Code](https://github.com/siat-nlp/CpRec) |
| [Neural architecture search for LF-MMI trained time delay neural networks[J]. IEEE/ACM Trans. on Audio, Speech, and Language Processing, 2022.](https://ieeexplore.ieee.org/abstract/document/9721103/) | The Chinese University of Hong Kong | -- |
| [Structured transforms for small-footprint deep learning[J]. NeurIPS, 2015.](https://proceedings.neurips.cc/paper/2015/hash/851300ee84c2b80ed40f51ed26d866fc-Abstract.html) | Google, New York | -- | 


### 3.2.2.3. Model Quantization
| Title & Basic Information | Affiliation | Code |
| ---- | ---- | ---- | 
| [Fractrain: Fractionally squeezing bit savings both temporally and spatially for efficient dnn training[J]. NeurIPS, 2020.](https://proceedings.neurips.cc/paper_files/paper/2020/file/8dc5983b8c4ef1d8fcd5f325f9a65511-Paper.pdf) | Rice University | [Code](https://github.com/RICE-EIC/FracTrain) |
| [Edgebert: Sentence-level energy optimizations for latency-aware multi-task nlp inference[C] MICRO-54, 2021.](https://dl.acm.org/doi/abs/10.1145/3466752.3480095) | Harvard University | -- |
| [Stochastic precision ensemble: self-knowledge distillation for quantized deep neural networks[C] AAAI, 2021.](https://ojs.aaai.org/index.php/AAAI/article/view/16839) | Seoul National University | -- |
| [Q-capsnets: A specialized framework for quantizing capsule networks[C] DAC, 2020.](https://ieeexplore.ieee.org/abstract/document/9218746/) | Technische Universitat Wien (TU Wien) | [Code](https://git.io/JvDIF) |
| [Fspinn: An optimization framework for memory-efficient and energy-efficient spiking neural networks[J]. TCAD, 2020.](https://ieeexplore.ieee.org/abstract/document/9211568/) | Technische Universität Wien | -- |
| [Octo: INT8 Training with Loss-aware Compensation and Backward Quantization for Tiny On-device Learning[C] USENIX Annual Technical Conference. 2021.](https://www.usenix.org/system/files/atc21-zhou.pdf) | Hong Kong Polytechnic University | [Code](https://github.com/kimihe/Octo) |
| [Hardware-centric automl for mixed-precision quantization[J]. IJCV, 2020.](https://linkspringer.53yu.com/article/10.1007/s11263-020-01339-6) | Massachusetts Institute of Technology | -- |
| [An automated quantization framework for high-utilization rram-based pim[J]. TCAD, 2021.](https://ieeexplore.ieee.org/abstract/document/9360862/) | Capital Normal University | -- |
| [Exact neural networks from inexact multipliers via fibonacci weight encoding[C] DAC, 2021.](https://ieeexplore.ieee.org/abstract/document/9586245/) | Swiss Federal Institute of Technology Lausanne (EPFL) | -- |
| [Integer-arithmetic-only certified robustness for quantized neural networks[C] ICCV, 2021.](http://openaccess.thecvf.com/content/ICCV2021/html/Lin_Integer-Arithmetic-Only_Certified_Robustness_for_Quantized_Neural_Networks_ICCV_2021_paper.html) | University of Southern California | -- |
| [Bits-Ensemble: Toward Light-Weight Robust Deep Ensemble by Bits-Sharing[J]. TCAD, 2022.](https://ieeexplore.ieee.org/abstract/document/9854091/) | McGill University | -- |
| [Similarity-Aware CNN for Efficient Video Recognition at the Edge[J]. TCAD, 2021.](https://ieeexplore.ieee.org/abstract/document/9656540/) | University of Southampton | -- |
| [ Data-Free Network Compression via Parametric Non-uniform Mixed Precision Quantization[C] CVPR, 2022.](http://openaccess.thecvf.com/content/CVPR2022/html/Chikin_Data-Free_Network_Compression_via_Parametric_Non-Uniform_Mixed_Precision_Quantization_CVPR_2022_paper.html) | Huawei Noah's Ark Lab | -- |

### 3.2.2.4. Knowledge Distillation
| Title & Basic Information | Affiliation | Code |
| ---- | ---- | ---- | 
| [Be your own teacher: Improve the performance of convolutional neural networks via self distillation[C] ICCV, 2019.](https://openaccess.thecvf.com/content_ICCV_2019/papers/Zhang_Be_Your_Own_Teacher_Improve_the_Performance_of_Convolutional_Neural_ICCV_2019_paper.pdf) | Tsinghua University | [Code](https://github.com/ArchipLab-LinfengZhang/) |
| [Dynabert: Dynamic bert with adaptive width and depth[J]. NeurIPS, 2020.](https://proceedings.neurips.cc/paper/2020/hash/6f5216f8d89b086c18298e043bfe48ed-Abstract.html) | Huawei Noah’s Ark Lab | [Code](https://github.com/huawei-noah/Pretrained-Language-Model/tree/master/DynaBERT) |
| [Scan: A scalable neural networks framework towards compact and efficient models[J]. NeurIPS, 2019.](https://proceedings.neurips.cc/paper/2019/hash/934b535800b1cba8f96a5d72f72f1611-Abstract.html) | Tsinghua University | [Code](https://github.com/ArchipLab-LinfengZhang/pytorch-scalable-neural-networks) |
| [Content-aware gan compression[C] CVPR, 2021.](http://openaccess.thecvf.com/content/CVPR2021/html/Liu_Content-Aware_GAN_Compression_CVPR_2021_paper.html) | Princeton University | -- |
| [Stochastic precision ensemble: self-knowledge distillation for quantized deep neural networks[C] AAAI, 2021.](https://ojs.aaai.org/index.php/AAAI/article/view/16839) | Seoul National University | -- |
| [Cross-modal knowledge distillation for vision-to-sensor action recognition[C] ICASSP, 2022.](https://ieeexplore.ieee.org/abstract/document/9746752/) | Texas State University | -- |
| [Learning efficient and accurate detectors with dynamic knowledge distillation in remote sensing imagery[J]. IEEE Trans. on Geoscience and Remote Sensing, 2021.](https://ieeexplore.ieee.org/abstract/document/9625952/) | Chinese Academy of Sciences | -- |
| [On-Device Next-Item Recommendation with Self-Supervised Knowledge Distillation[C] SIGIR, 2022.](https://dl.acm.org/doi/abs/10.1145/3477495.3531775) | The University of Queensland | [Code](https://github.com/xiaxin1998/OD-Rec) |
| [Personalized edge intelligence via federated self-knowledge distillation[J]. TPDS, 2022.](https://ieeexplore.ieee.org/abstract/document/9964434/) | Huazhong University of Science and Technology | -- |
| [Mobilefaceswap: A lightweight framework for video face swapping[C] AAAI, 2022.](https://ojs.aaai.org/index.php/AAAI/article/view/20203) | Baidu Inc. | -- |
| [Dynamically pruning segformer for efficient semantic segmentation[C] ICASSP, 2022.](https://ieeexplore.ieee.org/abstract/document/9747634) | Amazon Halo Health & Wellness | -- |
| [CDFKD-MFS: Collaborative Data-Free Knowledge Distillation via Multi-Level Feature Sharing[J]. IEEE Trans. on Multimedia, 2022.](https://ieeexplore.ieee.org/abstract/document/9834142/) | Beijing Institute of Technology | [Code](https://github.com/Hao840/CDFKD-MFS) |
| [Learning Efficient Vision Transformers via Fine-Grained Manifold Distillation[J]. NeurIPS, 2022.](https://proceedings.neurips.cc/paper_files/paper/2022/hash/3bd2d73b4e96b0ac5a319be58a96016c-Abstract-Conference.html) | Beijing Institute of Technology | [Code](https://github.com/Hao840/manifold-distillation) |
| [Learning Accurate, Speedy, Lightweight CNNs via Instance-Specific Multi-Teacher Knowledge Distillation for Distracted Driver Posture Identification[J]. IEEE Trans. on Intelligent Transportation Systems, 2022.](https://ieeexplore.ieee.org/abstract/document/9750058/) | Hefei Institutes of Physical Science (HFIPS), Chinese Academy of Sciences | -- | 

### 3.2.2.5. Low-rank Factorization
| Title & Basic Information | Affiliation | Code |
| ---- | ---- | ---- | 
| [Learning low-rank deep neural networks via singular vector orthogonality regularization and singular value sparsification[C] CVPR workshops. 2020.](https://openaccess.thecvf.com/content_CVPRW_2020/papers/w40/Yang_Learning_Low-Rank_Deep_Neural_Networks_via_Singular_Vector_Orthogonality_Regularization_CVPRW_2020_paper.pdf) | Duke University | -- |
| [MicroNet: Towards image recognition with extremely low FLOPs[J]. arXiv, 2020.](https://arxiv.org/pdf/2011.12289.pdf) | UC San Diego | -- |
| [Locality Sensitive Hash Aggregated Nonlinear Neighborhood Matrix Factorization for Online Sparse Big Data Analysis[J]. ACM/IMS Transactions on Data Science (TDS), 2022.](https://dl.acm.org/doi/abs/10.1145/3497749) | Hunan University | -- |

### 3.3. System Optimization
An overview of system optimization operations. Software optimization involves developing frameworks for lightweight model training and inference, while hardware optimization focuses on accelerating models using hardware-based approaches to improve computational efficiency on edge devices.
![System](Figures/system_optimization.png)

#### 3.3.1. Software Optimization
| Title & Basic Information | Affiliation | Code |
| ---- | ---- | ---- | 
| [Hidet: Task-mapping programming paradigm for deep learning tensor programs[C] ASPLOS Conference, 2023.](https://dl.acm.org/doi/abs/10.1145/3575693.3575702) | University of Toronto | [Code](https://www.github.com/hidet-org/hidet) |
| [SparkNoC: An energy-efficiency FPGA-based accelerator using optimized lightweight CNN for edge computing[J]. Journal of Systems Architecture, 2021.](https://sciencedirect.53yu.com/science/article/pii/S1383762121000138) | Shanghai Advanced Research Institute, Chinese Academy of Sciences | -- |
| [Re-architecting the on-chip memory sub-system of machine-learning accelerator for embedded devices[C] ICCAD, 2016.](https://ieeexplore.ieee.org/abstract/document/7827590/) | Institute of Computing Technology, Chinese Academy of Sciences | -- |
| [A unified optimization approach for cnn model inference on integrated gpus[C] ICPP, 2019.](https://dl.acm.org/doi/pdf/10.1145/3337821.3337839) | Amazon Web Services | [Code](https://github.com/dmlc/tvm/) |
| [ACG-engine: An inference accelerator for content generative neural networks[C] ICCAD, 2019.](https://ieeexplore.ieee.org/abstract/document/8942169/) | University of Chinese Academy of Sciences | -- |
| [Edgeeye: An edge service framework for real-time intelligent video analytics[C] EDGESYS Conference, 2018.](https://dl.acm.org/doi/pdf/10.1145/3213344.3213345) | University of Wisconsin-Madison | -- |
| [Haq: Hardware-aware automated quantization with mixed precision[C] CVPR, 2019.](https://openaccess.thecvf.com/content_CVPR_2019/papers/Wang_HAQ_Hardware-Aware_Automated_Quantization_With_Mixed_Precision_CVPR_2019_paper.pdf) | Massachusetts Institute of Technology | -- |
| [Source compression with bounded dnn perception loss for iot edge computer vision[C] MobiCom, 2019.](https://dl.acm.org/doi/abs/10.1145/3300061.3345448) | Hewlett Packard Labs | -- |
| [A lightweight collaborative deep neural network for the mobile web in edge cloud[J]. TMC, 2020.](https://ieeexplore.ieee.org/abstract/document/9286558/) | Beijing University of Posts and Telecommunications | -- |
| [Enabling incremental knowledge transfer for object detection at the edge[C] CVPR Workshops, 2020.](https://openaccess.thecvf.com/content_CVPRW_2020/papers/w28/Farhadi_Enabling_Incremental_Knowledge_Transfer_for_Object_Detection_at_the_Edge_CVPRW_2020_paper.pdf) | Arizona State university | -- |
| [DA3: Dynamic Additive Attention Adaption for Memory-Efficient On-Device Multi-Domain Learning[C] CVPR, 2022.](https://openaccess.thecvf.com/content/CVPR2022W/ECV/papers/Yang_DA3_Dynamic_Additive_Attention_Adaption_for_Memory-Efficient_On-Device_Multi-Domain_Learning_CVPRW_2022_paper.pdf) | Arizona State University | -- |
| [An efficient GPU-accelerated inference engine for binary neural network on mobile phones[J]. Journal of Systems Architecture, 2021.](https://sciencedirect.53yu.com/science/article/pii/S1383762121001120) | Sun Yat-sen University | [Code](https://code.ihub.org.cn/projects/915/repository/PhoneBit) |
| [RAPID-RL: A Reconfigurable Architecture with Preemptive-Exits for Efficient Deep-Reinforcement Learning[C] ICRA, 2022.](https://ieeexplore.ieee.org/abstract/document/9812320) | Purdue University | -- |
| [A variational information bottleneck based method to compress sequential networks for human action recognition[C] WACV, 2021.](https://openaccess.thecvf.com/content/WACV2021/papers/Srivastava_A_Variational_Information_Bottleneck_Based_Method_to_Compress_Sequential_Networks_WACV_2021_paper.pdf) | Indian Institute of Technology Delhi | -- |
| [EdgeDRNN: Recurrent neural network accelerator for edge inference[J]. IEEE Journal on Emerging and Selected Topics in Circuits and Systems, 2020.](https://ieeexplore.ieee.org/abstract/document/9268992/) | University of Zürich and ETH Zürich | -- |
| [Structured pruning of recurrent neural networks through neuron selection[J]. Neural Networks, 2020.](https://www.sciencedirect.com/science/article/pii/S0893608019303776) | University of Electronic Science and Technology of China | -- |
| [Dynamically hierarchy revolution: dirnet for compressing recurrent neural network on mobile devices[J]. arXiv, 2018.](https://arxiv.org/pdf/1806.01248.pdf) | Arizona State University | -- | 
| [High-throughput cnn inference on embedded arm big. little multicore processors[J]. TCAD, 2019.](https://ieeexplore.ieee.org/abstract/document/8852739/) | National University of Singapore | -- |
| [SCA: a secure CNN accelerator for both training and inference[C] DAC, 2020.](https://ieeexplore.ieee.org/abstract/document/9218752/) | University of Pittsburgh | -- |
| [NeuLens: spatial-based dynamic acceleration of convolutional neural networks on edge[C] MobiCom, 2022.](https://dl.acm.org/doi/abs/10.1145/3495243.3560528?casa_token=ioLt8xczh7cAAAAA:EpjRGtBuz0Hy3sYw9H4v1TVXcX03I68KMtlLjk1Tt2FhheVS0MA97woEWGgg_pjfjXc_njTf2JV8sQ) | New Jersey Institute of Technology | -- |
| [Weightless neural networks for efficient edge inference[C] PACT, 2022.](https://dl.acm.org/doi/pdf/10.1145/3559009.3569680) | The University of Texas at Austin | [Code](https://github.com/ZSusskind/BTHOWeN) |
| [O3BNN-R: An out-of-order architecture for high-performance and regularized BNN inference[J]. TPDS, 2020.](https://ieeexplore.ieee.org/abstract/document/9154597/) | -- | -- |
| [Blockgnn: Towards efficient gnn acceleration using block-circulant weight matrices[C] DAC, 2021.](https://ieeexplore.ieee.org/abstract/document/9586181/) | Peking University | -- |
| [{Hardware/Software}{Co-Programmable} Framework for Computational {SSDs} to Accelerate Deep Learning Service on {Large-Scale} Graphs[C] FAST, 2022.](https://www.usenix.org/conference/fast22/presentation/kwon) | KAIST | -- |
| [Achieving full parallelism in LSTM via a unified accelerator design[C] ICCD, 2020.](https://ieeexplore.ieee.org/abstract/document/9283568/) | University of Pittsburgh | -- |
| [Pasgcn: An reram-based pim design for gcn with adaptively sparsified graphs[J]. TCAD, 2022.](https://ieeexplore.ieee.org/abstract/document/9774869/) | Shanghai Jiao Tong University | -- |


#### 3.3.2. Hardware Optimization
| Title & Basic Information | Affiliation | Code |
| ---- | ---- | ---- | 
| [Ncpu: An embedded neural cpu architecture on resource-constrained low power devices for real-time end-to-end performance[C] MICRO, 2020.](https://ieeexplore.ieee.org/abstract/document/9251958/) | Northwestern Univeristy, Evanston, IL | -- |
| [Reduct: Keep it close, keep it cool!: Efficient scaling of dnn inference on multi-core cpus with near-cache compute[C] ISCA, 2021.](https://ieeexplore.ieee.org/abstract/document/9499927/) | ETH Zurich  | -- |
| [FARNN: FPGA-GPU hybrid acceleration platform for recurrent neural networks[J]. TPDS, 2021.](https://ieeexplore.ieee.org/abstract/document/9600618/) | Sungkyunkwan University | -- |
| [Apgan: Approximate gan for robust low energy learning from imprecise components[J]. IEEE Trans. on Computers, 2019.](https://ieeexplore.ieee.org/abstract/document/8880521/) | University of Central Florida | -- |
| [An FPGA overlay for CNN inference with fine-grained flexible parallelism[J]. TACO, 2022.](https://dl.acm.org/doi/full/10.1145/3519598) | International Institute of Information Technology | -- |
| [Pipelined data-parallel CPU/GPU scheduling for multi-DNN real-time inference[C] RTSS, 2019.](https://ieeexplore.ieee.org/abstract/document/9052147/) | University of California, Riverside | -- |
| [Deadline-based scheduling for GPU with preemption support[C] RTSS, 2018.](https://ieeexplore.ieee.org/abstract/document/8603197) | University of Modena and Reggio Emilia Modena | -- |
| [Energon: Toward Efficient Acceleration of Transformers Using Dynamic Sparse Attention[J]. TCAD, 2022.](https://ieeexplore.ieee.org/abstract/document/9763839/) | Peking University | -- |
| [Light-OPU: An FPGA-based overlay processor for lightweight convolutional neural networks[C] FPGA, 2022.](https://dl.acm.org/doi/abs/10.1145/3373087.3375311) | University of california, Los Angeles | -- |
| [Fluid Batching: Exit-Aware Preemptive Serving of Early-Exit Neural Networks on Edge NPUs[J]. arXiv, 2022.](https://arxiv.org/pdf/2209.13443.pdf) | Samsung AI Center, Cambridge | -- |
| [BitSystolic: A 26.7 TOPS/W 2b~ 8b NPU with configurable data flows for edge devices[J]. IEEE Trans. on Circuits and Systems I: Regular Papers, 2020.](https://ieeexplore.ieee.org/abstract/document/9301197/) | Duke University | -- |
| [PL-NPU: An Energy-Efficient Edge-Device DNN Training Processor With Posit-Based Logarithm-Domain Computing[J]. IEEE Trans. on Circuits and Systems I: Regular Papers, 2022.](https://ieeexplore.ieee.org/abstract/document/9803862/) | Tsinghua University | -- |

<!-- 
## 4. Important Surveys on Edge AI (Related to edge inference and model deployment)
- [Convergence of edge computing and deep learning: A comprehensive survey. IEEE Communications Surveys & Tutorials, 22(2), 869-904.](https://ieeexplore.ieee.org/abstract/document/8976180/)
![](Figures/relation_ei_ie.png)
- [Deep learning with edge computing: A review. Proceedings of the IEEE, 107(8), 1655-1674.](https://ieeexplore.ieee.org/abstract/document/8763885/)
![](Figures/DNN_inference_speedup_methods.png)
- [Machine learning at the network edge: A survey. ACM Computing Surveys (CSUR), 54(8), 1-37.](https://dl.acm.org/doi/abs/10.1145/3469029)
![](Figures/ML_at_edge.png)
- [Edge intelligence: The confluence of edge computing and artificial intelligence. IEEE Internet of Things Journal, 7(8), 7457-7469.](https://ieeexplore.ieee.org/abstract/document/9052677/)
![](Figures/research_roadmap_edge_intelligence.png)
- [Edge intelligence: Paving the last mile of artificial intelligence with edge computing. Proceedings of the IEEE, 107(8), 1738-1762.](https://ieeexplore.ieee.org/abstract/document/8736011/)
![](Figures/six_level_EI.png)
- [Edge intelligence: Empowering intelligence to the edge of network. Proceedings of the IEEE, 109(11), 1778-1837.](https://ieeexplore.ieee.org/abstract/document/9596610/)
![](Figures/classification_of_edge_ai.png)


## 2. Papers 

### 2.1. Edge Computing
- [Shi, W., Cao, J., Zhang, Q., Li, Y., & Xu, L. (2016). Edge computing: Vision and challenges. IEEE internet of things journal, 3(5), 637-646.](https://ieeexplore.ieee.org/abstract/document/7488250)
- [Varghese, B., Wang, N., Barbhuiya, S., Kilpatrick, P., & Nikolopoulos, D. S. (2016, November). Challenges and opportunities in edge computing. In 2016 IEEE International Conference on Smart Cloud (SmartCloud) (pp. 20-26). IEEE.](https://ieeexplore.ieee.org/abstract/document/7796149)
- [Shi, W., & Dustdar, S. (2016). The promise of edge computing. Computer, 49(5), 78-81.](https://ieeexplore.ieee.org/abstract/document/7469991)
- [Satyanarayanan, M. (2017). The emergence of edge computing. Computer, 50(1), 30-39.](https://ieeexplore.ieee.org/abstract/document/7807196)
- [Khan, W. Z., Ahmed, E., Hakak, S., Yaqoob, I., & Ahmed, A. (2019). Edge computing: A survey. Future Generation Computer Systems, 97, 219-235.](https://www.sciencedirect.com/science/article/pii/S0167739X18319903)
- [Abbas, N., Zhang, Y., Taherkordi, A., & Skeie, T. (2017). Mobile edge computing: A survey. IEEE Internet of Things Journal, 5(1), 450-465.](https://ieeexplore.ieee.org/abstract/document/8030322)
- [Mao, Y., You, C., Zhang, J., Huang, K., & Letaief, K. B. (2017). A survey on mobile edge computing: The communication perspective. IEEE communications surveys & tutorials, 19(4), 2322-2358.](https://ieeexplore.ieee.org/abstract/document/8016573)
- [Liu, F., Tang, G., Li, Y., Cai, Z., Zhang, X., & Zhou, T. (2019). A survey on edge computing systems and tools. Proceedings of the IEEE, 107(8), 1537-1562.](https://ieeexplore.ieee.org/abstract/document/8746691/)
- [Premsankar, G., Di Francesco, M., & Taleb, T. (2018). Edge computing for the Internet of Things: A case study. IEEE Internet of Things Journal, 5(2), 1275-1284.](https://ieeexplore.ieee.org/abstract/document/8289317/)
- [Xiao, Y., Jia, Y., Liu, C., Cheng, X., Yu, J., & Lv, W. (2019). Edge computing security: State of the art and challenges. Procee