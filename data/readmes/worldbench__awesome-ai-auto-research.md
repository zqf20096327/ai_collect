[![Awesome Logo](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![arXiv](https://img.shields.io/badge/arXiv-2605.18661-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2605.18661)
[![Project Page](https://img.shields.io/badge/Project-Page-orange?style=flat-square&logo=gitbook)](https://worldbench.github.io/awesome-ai-auto-research)
![Visitors](https://komarev.com/ghpvc/?username=worldbench&repo=awesome-ai-auto-research&label=Hello,%20Visitor%20&color=yellow&style=social)
[![PR's Welcome](https://img.shields.io/badge/PRs-welcome-red.svg?style=flat)](https://github.com/worldbench/awesome-ai-auto-research/pulls)

# :sunglasses: Awesome AI Auto-Research

| <img width="100%" src="docs/assets/teaser_paper.png"> |
|:-:|

This repository accompanies the survey paper **"[AI for Auto-Research: Roadmap & User Guide](https://worldbench.github.io/awesome-ai-auto-research)"** and tracks papers on AI-assisted and automated scientific research, covering the **full research lifecycle**.

### :robot: AI Auto-Research

We organize the academic research lifecycle as eight interconnected stages grouped into four epistemological phases. Each phase serves a distinct function in producing, scrutinizing, and communicating scientific knowledge.

| | |
|:-:|:-|
| <img width="360px" src="docs/assets/s1.png"> | **Phase 1: Creation**<br>Generating novel research ideas, searching and synthesizing literature, running coding experiments, and creating publication-quality tables and figures. This phase spans **Idea Generation**, **Literature Review**, **Coding & Experiments**, and **Tables & Figures**. |
| <img width="360px" src="docs/assets/s5.png"> | **Phase 2: Writing**<br>Drafting, editing, and polishing academic manuscripts. AI assistance ranges from semi-automated grammar and citation tools to fully automated paper generation — the most commercially mature yet ethically contested stage. |
| <img width="360px" src="docs/assets/s6.png"> | **Phase 3: Validation**<br>Automated peer review generation, reviewer-paper matching, review quality assessment, and AI-assisted author rebuttals. This phase covers **Peer Review** and **Rebuttal & Revision**. |
| <img width="360px" src="docs/assets/s8.png"> | **Phase 4: Dissemination**<br>Converting papers into slides, posters, videos, websites, and social media content. Each output format targets a different audience and demands its own design logic and AI tool chain. |
| | |

For additional details, kindly refer to our :books: [**Paper**](https://worldbench.github.io/assets_common/papers/survey-ai-auto-research.pdf) and :earth_asia: [**Project Page**](https://worldbench.github.io/awesome-ai-auto-research).

### :books: Citation
If you find this work helpful for your research, please kindly consider citing our paper:
```bibtex
@article{survey-ai-auto-research,
  title   = {{AI} for {Auto-Research}: Roadmap \& User Guide},
  author  = {Kong, Lingdong and Sun, Xian and Chow, Wei and Li, Linfeng and Lin, Kevin Qinghong and Zhang, Xuan Billy
             and Wang, Song and Li, Rong and Wu, Qing and Gao, Wei and Wang, Yingshuo and Xie, Shaoyuan
             and Liu, Jiachen and Qu, Leigang and Li, Shijie and Ng, Lai Xing and Cottereau, Benoit R.
             and Liu, Ziwei and Chua, Tat-Seng and Ooi, Wei Tsang},
  journal = {arXiv preprint arXiv:2605.18661},
  year    = {2026}
}
```



## Table of Contents
- [**0. Background**](#background)
<!--
    - [What Is AI Auto-Research?](#what-is-ai-auto-research)
    - [Five Central Findings](#five-central-findings)
- [**Exhibition: AI-Generated Artifacts**](#exhibition-ai-generated-research-artifacts)
    - [Slide Decks](#ai-generated-slide-decks)
    - [Research Posters](#ai-generated-research-posters)
-->
- [**1. Idea Generation**](#1-idea-generation)
    - [LLM Internal Knowledge-Based Generation](#llm-internal-knowledge-based-generation)
    - [External Signal-Driven Generation](#external-signal-driven-generation)
    - [Multi-Agent Collaborative Generation](#multi-agent-collaborative-generation)
    - [Novelty and Feasibility Assessment](#novelty-and-feasibility-assessment)
- [**2. Literature Review & Paper Search**](#2-literature-review-paper-search)
    - [Literature Retrieval](#literature-retrieval)
    - [Survey & Related Work Generation](#survey-related-work-generation)
    - [Deep Research Agents](#deep-research-agents)
    - [Retrieval and Synthesis Quality Assessment](#retrieval-and-synthesis-quality-assessment)
- [**3. Coding & Experimentation**](#3-coding-experimentation)
    - [Code Generation](#code-generation)
    - [Paper-to-Code](#paper-to-code)
    - [Experiment Execution & Orchestration](#experiment-execution-orchestration)
    - [Code Correctness and Reproducibility Assessment](#code-correctness-and-reproducibility-assessment)
- [**4. Tables & Figures**](#4-tables-figures)
    - [Scientific Figure Generation](#scientific-figure-generation)
    - [Table Understanding & Generation](#table-understanding-generation)
    - [Mathematical Formulas & TikZ](#mathematical-formulas-tikz)
    - [Visual Fidelity and Scientific Accuracy Assessment](#visual-fidelity-and-scientific-accuracy-assessment)
- [**5. Paper Writing**](#5-paper-writing)
    - [Semi-Automated Writing Assistance](#semi-automated-writing-assistance)
    - [Fully Automated Paper Generation](#fully-automated-paper-generation)
    - [Societal Analysis](#societal-analysis)
    - [Writing Quality and AI Detection Assessment](#writing-quality-and-ai-detection-assessment)
- [**6. Peer Review**](#6-peer-review)
    - [Automated Review Generation](#automated-review-generation)
    - [Meta-Review & Reviewer Matching](#meta-review-reviewer-matching)
    - [Review Quality Assessment](#review-quality-assessment)
    - [Adversarial Attacks & Bias Analysis](#adversarial-attacks-bias-analysis)
    - [Detection & Policy](#detection-policy)
    - [Review Consistency and Bias Assessment](#review-consistency-and-bias-assessment)
- [**7. Rebuttal**](#7-rebuttal)
    - [Reviewer Comment Analysis](#reviewer-comment-analysis)
    - [Automated Rebuttal Generation](#automated-rebuttal-generation)
    - [Rebuttal Effectiveness Assessment](#rebuttal-effectiveness-assessment)
- [**8. Dissemination (Paper2X)**](#8-dissemination-paper2x)
    - [Slides & Presentations](#slides--presentations)
    - [Posters](#posters)
    - [Video & Web](#video--web)
    - [Fidelity and Adoption Assessment](#fidelity-and-adoption-assessment)
- [**9. End-to-End Systems**](#9-end-to-end-systems)
    - [Fully Automated Research Systems](#fully-automated-research-systems)
    - [Domain-Specific Systems](#domain-specific-systems)
    - [Evolutionary & Self-Improving Systems](#evolutionary-self-improving-systems)
    - [Research Platforms & Infrastructure](#research-platforms-infrastructure)
- [**10. Societal & Critical Perspectives**](#10-societal-critical-perspectives)
- [**11. Surveys & Curated Lists**](#11-surveys-curated-lists)
- [**12. Tools & GitHub Repos**](#12-tools-github-repos)




| <img width="100%" src="docs/assets/phase1.png"> |
|:-:|


<!--
# Background

| | |
|:-:|:-|
| <img width="260px" src="docs/assets/teaser.png"> | AI-assisted research is crossing a threshold. Fully automated systems can now generate research papers for as little as **$15**, while long-horizon agents execute experiments, draft manuscripts, and simulate critique with minimal human input. Yet this productivity frontier exposes a deeper integrity problem: under scientific pressure, even frontier LLMs still **fabricate results**, miss hidden errors, and fail to judge novelty reliably. |
| | |


## What Is AI Auto-Research?

"AI auto-research" refers to the use of AI systems to automate, assist, or accelerate stages of the **complete academic research lifecycle** -- from hypothesis formation to public dissemination. We organize the lifecycle into **eight interconnected stages** across **four phases**:

| Phase | Stages | Function |
|:-|:-|:-|
| **Phase 1: Creation** | Idea Generation · Literature Review · Coding & Experiments · Tables & Figures | Materially producing a research contribution |
| **Phase 2: Writing** | Paper Writing | Organizing outputs into a formal manuscript |
| **Phase 3: Validation** | Peer Review · Rebuttal & Revision | External scrutiny and iterative refinement |
| **Phase 4: Dissemination** | Paper2X (posters, slides, videos, agents) | Communicating findings to broader audiences |


## What Is the Capability-Integrity Challenge?

The central challenge is not whether AI can produce the *forms* of research, but whether it can preserve the *substance* -- evidence, judgment, provenance, and accountability:

- **Artifact generation outpaces verification.** Generated ideas can appear novel yet weaken after implementation; generated code may run but implement the wrong algorithm; fluent prose can conceal unsupported claims.
- **Capability boundaries emerge on open-ended tasks.** Performance drops sharply for genuinely novel ideas, long-horizon experiments, and scientific judgment.
- **Human-governed collaboration is most credible.** AI should reduce mechanical friction while researchers retain responsibility for interpretation, experimental design, and accountability.


## Five Central Findings

| # | Finding |
|:-:|:-|
| 1 | **Structured tasks benefit most.** AI excels at grounded, externally checkable tasks; capability drops for novel, underspecified, or long-horizon work. |
| 2 | **Artifact generation outpaces verification.** AI can produce plausible outputs faster than it can prove those outputs are correct, faithful, or meaningful. |
| 3 | **Human-governed collaboration is most reliable.** The strongest deployment pattern across all stages is not full autonomy but human-AI collaboration. |
| 4 | **Effective systems converge on layered architectures.** Exploration + execution + verification; orchestration and feedback design matter as much as model scale. |
| 5 | **AI use is a governance problem, not a detection problem.** The key questions are disclosure, attribution, and whether scientific integrity is preserved. |

| <img width="100%" src="docs/assets/teaser_paper.png"> |
|:-:|
| **AI auto-research across the complete lifecycle.** Four phases, eight stages. |



# Exhibition: AI-Generated Research Artifacts

> AI-generated outputs produced from this survey paper using state-of-the-art Paper2X tools. Click any thumbnail to visit the project page gallery.


## AI-Generated Slide Decks

Four automatically-generated presentation decks, each using a different AI tool.

| | |
|:-:|:-:|
| [![GPT-5.5 Slides](https://worldbench.github.io/assets/auto-research/slides/slides-teaser-GPT5.5.png)](https://worldbench.github.io/awesome-ai-auto-research#exhibition) | [![NotebookLM Slides](https://worldbench.github.io/assets/auto-research/slides/slides-teaser-NotebookLM.png)](https://worldbench.github.io/awesome-ai-auto-research#exhibition) |
| **GPT-5.5** (28 slides) &nbsp; [Download](https://worldbench.github.io/assets/auto-research/slides/slides-GPT5.5.pptx) | **NotebookLM** (11 slides) &nbsp; [Download](https://worldbench.github.io/assets/auto-research/slides/slides-NotebookLM.pptx) |
| [![Claude Opus 4.7 Slides](https://worldbench.github.io/assets/auto-research/slides/slides-teaser-Opus4.7.png)](https://worldbench.github.io/awesome-ai-auto-research#exhibition) | [![Manus 1.6 Slides](https://worldbench.github.io/assets/auto-research/slides/slides-teaser-Manus-1.6.png)](https://worldbench.github.io/awesome-ai-auto-research#exhibition) |
| **Claude Opus 4.7** (27 slides) &nbsp; [Download](https://worldbench.github.io/assets/auto-research/slides/slides-Opus4.7.pptx) | **Manus 1.6** (12 slides) &nbsp; [Download](https://worldbench.github.io/assets/auto-research/slides/slides-Manus-1.6.pptx) |


## AI-Generated Research Posters

Nine AI-generated posters -- six portrait and three landscape -- produced from the survey paper.

**Portrait Format**

| | | |
|:-:|:-:|:-:|
| [![01](https://worldbench.github.io/assets/auto-research/posters/Gemini-Pro.png)](https://worldbench.github.io/awesome-ai-auto-research#exhibition) | [![02](https://worldbench.github.io/assets/auto-research/posters/Qwen-Image-2.0.png)](https://worldbench.github.io/awesome-ai-auto-research#exhibition) | [![03](https://worldbench.github.io/assets/auto-research/posters/Claude-Opus4.7.jpg)](https://worldbench.github.io/awesome-ai-auto-research#exhibition) |
| **01 Gemini Pro** | **02 Qwen-Image-2.0** | **03 Claude Opus 4.7** |
| [![04](https://worldbench.github.io/assets/auto-research/posters/SenseNova-U1-8B-MoT.png)](https://worldbench.github.io/awesome-ai-auto-research#exhibition) | [![05](https://worldbench.github.io/assets/auto-research/posters/GPT-5.5.png)](https://worldbench.github.io/awesome-ai-auto-research#exhibition) | [![06](https://worldbench.github.io/assets/auto-research/posters/Seedream-4.0.png)](https://worldbench.github.io/awesome-ai-auto-research#exhibition) |
| **04 SenseNova-U1** | **05 GPT-5.5** | **06 Seedream 4.0** |

**Landscape Format**

| | |
|:-:|:-:|
| [![07](https://worldbench.github.io/assets/auto-research/posters/Gemini-Pro-Landscape.png)](https://worldbench.github.io/awesome-ai-auto-research#exhibition) | [![08](https://worldbench.github.io/assets/auto-research/posters/Qwen-Image-2.0-Landscape.png)](https://worldbench.github.io/awesome-ai-auto-research#exhibition) |
| **07 Gemini Pro** | **08 Qwen-Image-2.0** |

| [![09]( https://worldbench.github.io/assets/auto-research/posters/Claude-Opus4.7-Landscape.jpg)]( https://worldbench.github.io/awesome-ai-auto-research#exhibition) |
|:-:|
| **09 Claude Opus 4.7** |
-->
# 1. Idea Generation

### LLM Internal Knowledge-Based Generation

> In chronological order, from the earliest to the latest.

| Model | Paper | Venue | Website | GitHub |
|:-:|:-|:-:|:-:|:-:|
||
| `Chain of Ideas` | [![arXiv](https://img.shields.io/badge/arXiv-2410.13185-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2410.13185)<br>Chain of Ideas: Revolutionizing Research Via Novel Idea Development with LLM Agents | arXiv '24 | - | [![GitHub](https://img.shields.io/github/stars/DAMO-NLP-SG/CoI-Agent)](https://github.com/DAMO-NLP-SG/CoI-Agent) |
| `ResearchAgent` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://aclanthology.org/2025.naacl-long.342/)<br>ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models | NAACL '25 | - | [![GitHub](https://img.shields.io/github/stars/JinheonBaek/ResearchAgent)](https://github.com/JinheonBaek/ResearchAgent) |
| `SciMON` | [![arXiv](https://img.shields.io/badge/arXiv-2305.14259-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2305.14259)<br>SciMON: Scientific Inspiration Machines Optimized for Novelty | ACL '24 | - | [![GitHub](https://img.shields.io/github/stars/EagleW/CLBD)](https://github.com/EagleW/CLBD) |
| `Idea Gen Agent` | [![arXiv](https://img.shields.io/badge/arXiv-2409.04109-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2409.04109)<br>Can LLMs Generate Novel Research Ideas? A Large Scale Human Study with 100+ NLP Researchers | arXiv '24 | - | - |
| `IRIS` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://aclanthology.org/2025.acl-demo.57/)<br>IRIS: Interactive Research Ideation System for Accelerating Scientific Discovery | ACL '25 | - | [![GitHub](https://img.shields.io/github/stars/Anikethh/IRIS-Interactive-Research-Ideation-System)](https://github.com/Anikethh/IRIS-Interactive-Research-Ideation-System) |
| `Spark` | [![arXiv](https://img.shields.io/badge/arXiv-2504.20090-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2504.20090)<br>Spark: A System for Scientifically Creative Idea Generation | ICCC '25 | - | - |
| `Diverse Hypo. Search` | [![arXiv](https://img.shields.io/badge/arXiv-2606.10587-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2606.10587)<br>Towards Diverse Scientific Hypothesis Search with Large Language Models | arXiv '26 | - | - |
| `Tree-of-Ideas` | [![arXiv](https://img.shields.io/badge/arXiv-2608.10740-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.10740)<br>Tree-of-Ideas: Automated Research Ideation via Cross-Trajectory Reasoning over Scholarly Evolution | arXiv '26 | - | - |
| `IDEAgent` | [![arXiv](https://img.shields.io/badge/arXiv-2607.22375-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2607.22375)<br>IDEAgent: Agentic Quality-Diversity Search for Research Idea Generation | arXiv '26 | - | - |
||

### External Signal-Driven Generation

> In chronological order, from the earliest to the latest.

| Model | Paper | Venue | Website | GitHub |
|:-:|:-|:-:|:-:|:-:|
| `ActLim-Bench` | [![arXiv](https://img.shields.io/badge/arXiv-2610.23038-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2610.23038)<br>Where Research Ideation Begins: Forward-Citation Supervision for Actionable Limitation Generation | arXiv '26 | - | - |
| `IdeaAnchor` | [![arXiv](https://img.shields.io/badge/arXiv-2610.08781-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2610.08781)<br>IdeaAnchor: Teaching LLMs to Turn Literature into Research Ideas | arXiv '26 | [Project](https://ziyu.ch/research/ideaanchor) | - |
| `SGHA` | [![arXiv](https://img.shields.io/badge/arXiv-2608.17501-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.17501)<br>SGHA: Evidence-Grounded Research Problem Discovery with Local Language Models | arXiv '26 | - | - |
| `MAIL` | [![arXiv](https://img.shields.io/badge/arXiv-2608.28315-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.28315)<br>MAIL: Memory-driven, Adaptive, Incremental, and Literature-grounded Framework for Hypothesis Generation in Chemistry | arXiv '26 | - | - |
||
| `MOOSE-Chem` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://openreview.net/forum?id=X9OfMNNepI)<br>MOOSE-Chem: Large Language Models for Rediscovering Unseen Chemistry Scientific Hypotheses | ICLR '25 | - | - |
| `Nova` | [![arXiv](https://img.shields.io/badge/arXiv-2410.14255-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2410.14255)<br>Nova: An Iterative Planning and Search Approach to Enhance Novelty and Diversity of LLM Generated Ideas | arXiv '24 | - | - |
| `SciAgents` | [![arXiv](https://img.shields.io/badge/arXiv-2409.05556-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2409.05556)<br>SciAgents: Automating Scientific Discovery through Multi-Agent Intelligent Graph Reasoning | arXiv '24 | - | [![GitHub](https://img.shields.io/github/stars/lamm-mit/SciAgentsDiscovery)](https://github.com/lamm-mit/SciAgentsDiscovery) |
| `SciPIP` | [![arXiv](https://img.shields.io/badge/arXiv-2410.23166-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2410.23166)<br>SciPIP: An LLM-based Scientific Paper Idea Proposer | arXiv '24 | - | [![GitHub](https://img.shields.io/github/stars/cheerss/SciPIP)](https://github.com/cheerss/SciPIP) |
| `IdeaSynth` | [![arXiv](https://img.shields.io/badge/arXiv-2410.04025-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2410.04025)<br>IdeaSynth: Iterative Research Idea Development Through Evolving and Composing Idea Facets with Literature-Grounded Feedback | CHI '25 | - | - |
| `MOOSE-Chem2` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://nips.cc/virtual/2025/poster/118171)<br>MOOSE-Chem2: Exploring LLM Limits in Fine-Grained Scientific Hypothesis Discovery via Hierarchical Search | NeurIPS '25 | - | - |
| `HALO` | [![arXiv](https://img.shields.io/badge/arXiv-2607.18564-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2607.18564)<br>HALO: Interactive Co-abductive Reasoning in Scientific Hypothesis Generation | arXiv '26 | - | - |
| `TCA-SIR` | [![arXiv](https://img.shields.io/badge/arXiv-2607.28498-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2607.28498)<br>TCA-SIR: Learning Target-Conditioned Abstractions for Scientific Inspiration Retrieval | arXiv '26 | - | - |
| `ECLAIR` | [![arXiv](https://img.shields.io/badge/arXiv-2608.02323-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.02323)<br>ECLAIR: A Causally-Grounded AI Framework for Scientific Discovery in Empirical Software Engineering | arXiv '26 | - | - |
||

### Multi-Agent Collaborative Generation

> In chronological order, from the earliest to the latest.

| Model | Paper | Venue | Website | GitHub |
|:-:|:-|:-:|:-:|:-:|
| `HypoForge` | [![arXiv](https://img.shields.io/badge/arXiv-2608.25770-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.25770)<br>HypoForge: A Self-Improving Multi-Agent Framework for Automated Hypothesis Generation and Testing via Scientific Skill Learning | arXiv '26 | - | - |
||
| `Combi. Creativity` | [![arXiv](https://img.shields.io/badge/arXiv-2412.14141-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2412.14141)<br>Combi. Creativity | arXiv '24 | - | - |
| `Deep Ideation` | [![arXiv](https://img.shields.io/badge/arXiv-2511.02238-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2511.02238)<br>Deep Ideation: Designing LLM Agents to Generate Novel Research Ideas on Scientific Concept Network | arXiv '25 | - | [![GitHub](https://img.shields.io/github/stars/kyZhao-1/Deep-Ideation)](https://github.com/kyZhao-1/Deep-Ideation) |
| `VirSci` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://aclanthology.org/2025.acl-long.1368/)<br>Many Heads Are Better Than One: Improved Scientific Idea Generation by A LLM-Based Multi-Agent System | ACL '25 | - | [![GitHub](https://img.shields.io/github/stars/open-sciencelab/Virtual-Scientists)](https://github.com/open-sciencelab/Virtual-Scientists) |
| `Multi-Agent Dial.` | [![arXiv](https://img.shields.io/badge/arXiv-2507.08350-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2507.08350)<br>Multi-Agent Dial. | SIGDIAL '25 | - | - |
| `Artificial Hivemind` | [![arXiv](https://img.shields.io/badge/arXiv-2510.22954-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2510.22954)<br>Artificial Hivemind: The Open-Ended Homogeneity of Language Models (and Beyond) | NeurIPS '25 | - | - |
| `Auditable AI Sci.` | [![arXiv](https://img.shields.io/badge/arXiv-2607.09195-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2607.09195)<br>Toward Auditable AI Scientists: A Hypothesis Evolution Protocol for LLM Agents | arXiv '26 | - | - |
| `Diverse Personalized Ideation` | [![arXiv](https://img.shields.io/badge/arXiv-2607.28087-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2607.28087)<br>Diversifying Personalized Research Ideation against AI-Induced Homogenization | arXiv '26 | - | - |
||

### Novelty and Feasibility Assessment

> In chronological order, from the earliest to the latest.

| Model | Paper | Venue | Website | GitHub |
|:-:|:-|:-:|:-:|:-:|
| `MechHypoBench` | [![arXiv](https://img.shields.io/badge/arXiv-2610.05197-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2610.05197)<br>From Scientific Observations to Mechanisms: Benchmarking Hypothesis Generation by AI Scientists | arXiv '26 | - | - |
| `RATIO` | [![arXiv](https://img.shields.io/badge/arXiv-2608.27394-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.27394)<br>RATIO: A Benchmark for Retrieval Across Typed Ideation Operations in Scientific Literature | arXiv '26 | - | - |
| `Lit2Test` | [![arXiv](https://img.shields.io/badge/arXiv-2608.22948-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.22948)<br>What Proves You Wrong: Benchmarking Language Models on Falsifiable Research Ideation | arXiv '26 | - | - |
| `Energy Scoring` | [![arXiv](https://img.shields.io/badge/arXiv-2608.17270-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.17270)<br>Do LLMs Know a Good Hypothesis When They See One? Logit-Based Energy Scoring Outperforms Prompted LLM-as-Judge for Scientific Hypothesis Ranking | arXiv '26 | - | - |
| `Think-Probe-Respond` | [![arXiv](https://img.shields.io/badge/arXiv-2608.25660-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.25660)<br>Think-Probe-Respond: Improving Large Language Models as Judges of Research Idea Novelty | EMNLP '26 | - | - |
||
| `IdeaBench` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://doi.org/10.1145/3711896.3737419)<br>IdeaBench: Benchmarking Large Language Models for Research Idea Generation | KDD '25 | - | - |
| `LiveIdeaBench` | [![Article](https://img.shields.io/badge/Article-Nature_Communications-E30613?style=flat-square)](https://www.nature.com/articles/s41467-026-70245-1)<br>Evaluating LLMs' divergent thinking capabilities for scientific idea generation with minimal context | Nature Communications '26 | [Website & Leaderboard](https://liveideabench.com)<br>Data: [v1](https://huggingface.co/datasets/6cf/liveideabench) · [DLC-250127](https://huggingface.co/datasets/6cf/liveideabench-DLC-250127) · [v2](https://huggingface.co/datasets/6cf/liveideabench-v2)<br>Models: [IdeaWhiz](https://huggingface.co/6cf/QwQ-32B-Preview-IdeaWhiz-v1) · [GGUF](https://huggingface.co/6cf/QwQ-32B-Preview-IdeaWhiz-v1-GGUF) | [![GitHub](https://img.shields.io/github/stars/x66ccff/liveideabench)](https://github.com/x66ccff/liveideabench) |
| `AI Idea Bench 2025` | [![arXiv](https://img.shields.io/badge/arXiv-2504.14191-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2504.14191)<br>AI Idea Bench 2025: AI Research Idea Generation Benchmark | arXiv '25 | - | [![GitHub](https://img.shields.io/github/stars/yansheng-qiu/AI_Idea_Bench_2025)](https://github.com/yansheng-qiu/AI_Idea_Bench_2025) |
| `HeurekaBench` | [![arXiv](https://img.shields.io/badge/arXiv-2601.01678-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2601.01678)<br>HeurekaBench: A Benchmarking Framework for AI Co-scientist | ICLR '26 | - | [![GitHub](https://img.shields.io/github/stars/mlbio-epfl/HeurekaBench)](https://github.com/mlbio-epfl/HeurekaBench) |
| `ResearchBench` | [![arXiv](https://img.shields.io/badge/arXiv-2503.21248-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2503.21248)<br>ResearchBench: Benchmarking LLMs in Scientific Discovery via Inspiration-Based Task Decomposition | ACL '26 | - | - |
| `HindSight` | [![arXiv](https://img.shields.io/badge/arXiv-2603.15164-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2603.15164)<br>HindSight: Evaluating LLM-Generated Research Ideas via Future Impact | arXiv '26 | - | - |
| `Rubric Rewards` | [![arXiv](https://img.shields.io/badge/arXiv-2512.23707-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2512.23707)<br>Training AI Co-Scientists Using Rubric Rewards | arXiv '25 | - | - |
| `DeepInnovator` | [![arXiv](https://img.shields.io/badge/arXiv-2602.18920-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2602.18920)<br>DeepInnovator: Triggering the Innovative Capabilities of LLMs | arXiv '26 | - | [![GitHub](https://img.shields.io/github/stars/HKUDS/DeepInnovator)](https://github.com/HKUDS/DeepInnovator) |
| `FlowPIE` | [![arXiv](https://img.shields.io/badge/arXiv-2603.29557-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2603.29557)<br>FlowPIE: Test-Time Scientific Idea Evolution with Flow-Guided Literature Exploration | arXiv '26 | - | - |
| `SoundnessBench` | [![arXiv](https://img.shields.io/badge/arXiv-2605.30329-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2605.30329)<br>SoundnessBench: Can Your AI Scientist Really Tell Good Research Ideas from Bad Ones? | arXiv '26 | [Project](https://hosytuyen.github.io/projects/SoundnessBench/) | [![GitHub](https://img.shields.io/github/stars/hosytuyen/SoundnessBench)](https://github.com/hosytuyen/SoundnessBench) |
| `LLM-Judge Novelty` | [![arXiv](https://img.shields.io/badge/arXiv-2606.12071-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2606.12071)<br>On the Limits of LLM-as-Judge for Scientific Novelty Assessment | arXiv '26 | - | - |
| `LigBench` | [![arXiv](https://img.shields.io/badge/arXiv-2608.13136-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.13136)<br>LigBench: A Unified and Human-Aligned Benchmark for LLM-based Research Idea Generation | arXiv '26 | - | - |
| `Reconstruction` | [![arXiv](https://img.shields.io/badge/arXiv-2608.16645-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.16645)<br>Reconstruction: A Blind Benchmark for Recovering Research Ideas from Pre-Publication Bibliographies | arXiv '26 | - | - |
| `AgentIdeaBench` | [![arXiv](https://img.shields.io/badge/arXiv-2609.07611-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2609.07611)<br>AgentIdeaBench: Benchmarking Scientific Ideation in the Agent Era | arXiv '26 | - | [![GitHub](https://img.shields.io/github/stars/HKUST-KnowComp/AgentIdeaBench)](https://github.com/HKUST-KnowComp/AgentIdeaBench) |
| `IdeaAMBIG` | [![arXiv](https://img.shields.io/badge/arXiv-2609.10539-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2609.10539)<br>IdeaAMBIG: Benchmarking Implementation-Critical Gaps in Research-Idea Specifications | arXiv '26 | - | - |
| `NovGauge` | [![arXiv](https://img.shields.io/badge/arXiv-2609.11234-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2609.11234)<br>NovGauge: A Fine-Grained Benchmark for Diagnosing LLMs' Capability in Paper Novelty Assessment | arXiv '26 | - | - |
||



# 2. Literature Review & Paper Search

### Literature Retrieval

> In chronological order, from the earliest to the latest.

| Model | Paper | Venue | Website | GitHub |
|:-:|:-|:-:|:-:|:-:|
| `ITER` | [![arXiv](https://img.shields.io/badge/arXiv-2608.27912-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.27912)<br>ITER: Interaction-Aware Retrieval for Agentic Search | arXiv '26 | - | - |
| `Multi-Aspect Retrieval` | [![arXiv](https://img.shields.io/badge/arXiv-2608.15624-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.15624)<br>Can Retrievers Find the Same Paper from Different Aspects? A Multi-Aspect Full-Paper Scientific Retrieval Benchmark | arXiv '26 | - | - |
||
| `CiteME` | [![arXiv](https://img.shields.io/badge/arXiv-2407.12861-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2407.12861)<br>CiteME: Can Language Models Accurately Cite Scientific Claims? | arXiv '24 | - | - |
| `LitLLM` | [![arXiv](https://img.shields.io/badge/arXiv-2402.01788-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2402.01788)<br>LitLLM: A Toolkit for Literature Review with Large Language Models | arXiv '24 | - | - |
| `LitSearch` | [![arXiv](https://img.shields.io/badge/arXiv-2407.18940-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2407.18940)<br>LitSearch: A Retrieval Benchmark for Scientific Literature Search | arXiv '24 | - | [![GitHub](https://img.shields.io/github/stars/princeton-nlp/LitSearch)](https://github.com/princeton-nlp/LitSearch) |
| `PaperQA2` | [![arXiv](https://img.shields.io/badge/arXiv-2409.13740-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2409.13740)<br>Language Agents Achieve Superhuman Synthesis of Scientific Knowledge | arXiv '24 | - | [![GitHub](https://img.shields.io/github/stars/Future-House/paper-qa)](https://github.com/Future-House/paper-qa) |
| `OpenResearcher` | [![arXiv](https://img.shields.io/badge/arXiv-2408.06941-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2408.06941)<br>OpenResearcher: Unleashing AI for Accelerated Scientific Research | EMNLP '24 | - | - |
| `PaSa` | [![arXiv](https://img.shields.io/badge/arXiv-2501.10120-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2501.10120)<br>PaSa: An LLM Agent for Comprehensive Academic Paper Search | arXiv '25 | - | [![GitHub](https://img.shields.io/github/stars/bytedance/pasa)](https://github.com/bytedance/pasa) |
| `Self-Evolving Retrieval` | [![arXiv](https://img.shields.io/badge/arXiv-2605.14306-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2605.14306)<br>Towards Self-Evolving Agentic Literature Retrieval | arXiv '26 | - | - |
| `MasterSet` | [![arXiv](https://img.shields.io/badge/arXiv-2604.17680-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2604.17680)<br>MasterSet: A Large-Scale Benchmark for Must-Cite Citation Recommendation in the AI/ML Literature | arXiv '26 | - | - |
| `Search, Inspect, Fetch` | [![arXiv](https://img.shields.io/badge/arXiv-2608.02751-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.02751)<br>Search, Inspect, Fetch: Exploiting Structure-Aware Boolean Retrieval for Deep-Research Agents | arXiv '26 | - | - |
| `Rubric Reranker` | [![arXiv](https://img.shields.io/badge/arXiv-2608.03527-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.03527)<br>Training Documents Reranker with Search Rubrics for Deep Research Agent | arXiv '26 | - | - |
| `Personalized DR Refinement` | [![arXiv](https://img.shields.io/badge/arXiv-2608.05876-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.05876)<br>Personalized Deep Research Query Refinement with Graph-Scaffolded Evidence Grounding | arXiv '26 | - | - |
||

### Survey & Related Work Generation

> In chronological order, from the earliest to the latest.

| Model | Paper | Venue | Website | GitHub |
|:-:|:-|:-:|:-:|:-:|
| `ReviewPilot` | [![arXiv](https://img.shields.io/badge/arXiv-2610.21042-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2610.21042)<br>ReviewPilot: A Multi-Agent System for Screening and Data Extraction in Systematic Reviews | arXiv '26 | - | [![GitHub](https://img.shields.io/github/stars/ZhaoqianXue/ReviewPilot)](https://github.com/ZhaoqianXue/ReviewPilot) |
| `DAS` | [![arXiv](https://img.shields.io/badge/arXiv-2608.18034-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.18034)<br>Deep Academic Survey: Stateful Agentic Closed-Loop Paradigm for Academic Survey Automation | arXiv '26 | [Project](https://zhikaixu24.github.io/projects/DAS/) | [![GitHub](https://img.shields.io/github/stars/ZhikaiXu24/DAS)](https://github.com/ZhikaiXu24/DAS) |
| `Tree-of-Concerns` | [![arXiv](https://img.shields.io/badge/arXiv-2608.20777-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.20777)<br>Tree-of-Concerns: Hierarchical Multi-Agent Debate for Unstated-Limitation Extraction in Scientific Critique | EMNLP '26 | - | - |
||
| `ChatPaper` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://github.com/kaixindelele/ChatPaper)<br>ChatPaper: Use LLM to summarize papers | GitHub '23 | - | [![GitHub](https://img.shields.io/github/stars/kaixindelele/ChatPaper)](https://github.com/kaixindelele/ChatPaper) |
| `PaperQA` | [![arXiv](https://img.shields.io/badge/arXiv-2312.07559-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2312.07559)<br>PaperQA: Retrieval-Augmented Generative Agent for Scientific Research | arXiv '23 | - | [![GitHub](https://img.shields.io/github/stars/Future-House/paper-qa)](https://github.com/Future-House/paper-qa) |
| `AutoSurvey` | [![arXiv](https://img.shields.io/badge/arXiv-2406.10252-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2406.10252)<br>AutoSurvey: Large Language Models Can Automatically Write Surveys | arXiv '24 | - | [![GitHub](https://img.shields.io/github/stars/AutoSurveys/AutoSurvey)](https://github.com/AutoSurveys/AutoSurvey) |
| `GPT Researcher` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://github.com/assafelovic/gpt-researcher)<br>GPT Researcher: Autonomous Agent for Comprehensive Online Research | GitHub '24 | - | [![GitHub](https://img.shields.io/github/stars/assafelovic/gpt-researcher)](https://github.com/assafelovic/gpt-researcher) |
| `LLMs for Lit. Review` | [![arXiv](https://img.shields.io/badge/arXiv-2412.13612-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2412.13612)<br>LLMs for Lit. Review | arXiv '24 | - | - |
| `STORM` | [![arXiv](https://img.shields.io/badge/arXiv-2402.14207-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2402.14207)<br>Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models | arXiv '24 | - | [![GitHub](https://img.shields.io/github/stars/stanford-oval/storm)](https://github.com/stanford-oval/storm) |
| `Agentic AutoSurvey` | [![arXiv](https://img.shields.io/badge/arXiv-2509.18661-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2509.18661)<br>Agentic AutoSurvey: Let LLMs Survey LLMs | arXiv '25 | - | - |
| `Citegeist` | [![arXiv](https://img.shields.io/badge/arXiv-2503.23229-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2503.23229)<br>Citegeist: Automated Generation of Related Work Analysis on the arXiv Corpus | arXiv '25 | - | - |
| `IterSurvey` | [![arXiv](https://img.shields.io/badge/arXiv-2510.21900-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2510.21900)<br>IterSurvey: Deep Literature Survey Automation with an Iterative Workflow | arXiv '25 | - | [![GitHub](https://img.shields.io/github/stars/HancCui/IterSurvey_Autosurveyv2)](https://github.com/HancCui/IterSurvey_Autosurveyv2) |
| `LiRA` | [![arXiv](https://img.shields.io/badge/arXiv-2510.05138-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2510.05138)<br>LiRA: A Multi-Agent Framework for Reliable and Readable Literature Review Generation | arXiv '25 | - | - |
| `SurveyForge` | [![arXiv](https://img.shields.io/badge/arXiv-2503.04629-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2503.04629)<br>SurveyForge: On the Outline Heuristics, Memory-Driven Generation, and Multi-dimensional Evaluation for Automated Survey Writing | arXiv '25 | - | [![GitHub](https://img.shields.io/github/stars/Alpha-Innovator/SurveyForge)](https://github.com/Alpha-Innovator/SurveyForge) |
| `SurveyG` | [![arXiv](https://img.shields.io/badge/arXiv-2510.07733-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2510.07733)<br>SurveyG: A Multi-Agent LLM Framework with Hierarchical Citation Graph for Automated Survey Generation | arXiv '25 | - | - |
| `SurveyX` | [![arXiv](https://img.shields.io/badge/arXiv-2502.14776-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2502.14776)<br>SurveyX: Academic Survey Automation via Large Language Models | arXiv '25 | - | - |
| `InteractiveSurvey` | [![arXiv](https://img.shields.io/badge/arXiv-2504.08762-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2504.08762)<br>InteractiveSurvey: An LLM-based Personalized and Interactive Survey Paper Generation System | arXiv '25 | - | [![GitHub](https://img.shields.io/github/stars/TechnicolorGUO/InteractiveSurvey)](https://github.com/TechnicolorGUO/InteractiveSurvey) |
| `CiteLLM` | [![arXiv](https://img.shields.io/badge/arXiv-2602.23075-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2602.23075)<br>CiteLLM: An Agentic Platform for Trustworthy Scientific Reference Discovery | arXiv '26 | - | - |
| `DeepSurvey` | [![arXiv](https://img.shields.io/badge/arXiv-2605.29522-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2605.29522)<br>DeepSurvey: Enhancing Analytical Depth and Citation Reliability in Automated Survey Generation | arXiv '26 | - | - |
| `STRUCTSURVEY` | [![arXiv](https://img.shields.io/badge/arXiv-2607.01243-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2607.01243)<br>STRUCTSURVEY: Structured Agentic Retrieval for Automated Survey Paper Generation | arXiv '26 | - | - |
||

### Deep Research Agents

> In chronological order, from the earliest to the latest.

| Model | Paper | Venue | Website | GitHub |
|:-:|:-|:-:|:-:|:-:|
| `MIRA` | [![arXiv](https://img.shields.io/badge/arXiv-2610.25926-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2610.25926)<br>MIRA: A Multimodal Illustrated Deep Research Agent for Controllable Reports | arXiv '26 | [Project](https://mira-mmdeepresearch.github.io/) | - |
| `OpenSaC` | [![arXiv](https://img.shields.io/badge/arXiv-2610.25779-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2610.25779)<br>OpenSaC: A Python Library for Search as Code in Deep Research Agents | arXiv '26 | - | [![GitHub](https://img.shields.io/github/stars/liuqi6777/OpenSaC)](https://github.com/liuqi6777/OpenSaC) |
| `HybridResearcher` | [![arXiv](https://img.shields.io/badge/arXiv-2610.24899-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2610.24899)<br>HybridResearcher: Bridging the Structured-Unstructured Boundary for Deep Research Agents | arXiv '26 | - | - |
| `JevGPT` | [![arXiv](https://img.shields.io/badge/arXiv-2610.18272-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2610.18272)<br>JevGPT: Thinking Fast and Slow in Autonomous Research | arXiv '26 | [Project](https://sunyasheng.github.io/projects/JevGPT.html) | [![GitHub](https://img.shields.io/github/stars/sunyasheng/JevGPT)](https://github.com/sunyasheng/JevGPT) |
| `Crase` | [![arXiv](https://img.shields.io/badge/arXiv-2608.24809-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.24809)<br>Structurally-bounded Agentic Graph Exploration for Evidence-Grounded Scholarly DeepSearch | arXiv '26 | - | - |
| `DeepWeaver` | [![arXiv](https://img.shields.io/badge/arXiv-2608.18988-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.18988)<br>DeepWeaver: Bridging the Evidence Synthesis Gap in Open-Ended Question Answering | arXiv '26 | - | - |
| `AgentR` | [![arXiv](https://img.shields.io/badge/arXiv-2608.15264-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.15264)<br>AgentR A Stateful and Recovery-Aware Software Architecture for LLM-based Auditable Workflows | arXiv '26 | - | - |
||
| `ASReview` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://www.nature.com/articles/s42256-020-00287-7)<br>An Open Source Machine Learning Framework for Efficient and Transparent Systematic Reviews | Nature MI '21 | - | [![GitHub](https://img.shields.io/github/stars/asreview/asreview)](https://github.com/asreview/asreview) |
| `CHIME` | [![arXiv](https://img.shields.io/badge/arXiv-2407.16148-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2407.16148)<br>CHIME: LLM-Assisted Hierarchical Organization of Scientific Studies for Literature Review Support | arXiv '24 | - | - |
| `DeepResearch-Agent` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://github.com/SkyworkAI/DeepResearchAgent)<br>DeepResearchAgent: A Hierarchical Multi-Agent System for Deep Research | GitHub '25 | - | [![GitHub](https://img.shields.io/github/stars/SkyworkAI/DeepResearchAgent)](https://github.com/SkyworkAI/DeepResearchAgent) |
| `DeerFlow` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://github.com/bytedance/deer-flow)<br>DeerFlow: A Deep Research Framework Orchestrating Sub-Agents, Memory, and Sandboxes | GitHub '25 | - | [![GitHub](https://img.shields.io/github/stars/bytedance/deer-flow)](https://github.com/bytedance/deer-flow) |
| `OpenScholar` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://doi.org/10.1038/s41586-025-10072-4)<br>OpenScholar: Synthesizing Scientific Literature with Retrieval-Augmented LMs | Nature '26 | - | - |
| `AutoAgent` | [![arXiv](https://img.shields.io/badge/arXiv-2502.05957-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2502.05957)<br>AutoAgent | arXiv '25 | - | - |
| `Tongyi DeepResearch` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://github.com/Alibaba-NLP/DeepResearch)<br>Tongyi DeepResearch | GitHub '25 | - | [![GitHub](https://img.shields.io/github/stars/Alibaba-NLP/DeepResearch)](https://github.com/Alibaba-NLP/DeepResearch) |
| `O-Researcher` | [![arXiv](https://img.shields.io/badge/arXiv-2601.03743-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2601.03743)<br>O-Researcher: An Open Ended Deep Research Model via Multi-Agent Distillation and Agentic RL | arXiv '26 | - | - |
| `OpenResearcher` | [![arXiv](https://img.shields.io/badge/arXiv-2603.20278-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2603.20278)<br>OpenResearcher: Unleashing AI for Accelerated Scientific Research | arXiv '26 | - | [![GitHub](https://img.shields.io/github/stars/TIGER-AI-Lab/OpenResearcher)](https://github.com/TIGER-AI-Lab/OpenResearcher) |
| `AREX` | [![arXiv](https://img.shields.io/badge/arXiv-2607.21461-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2607.21461)<br>AREX: Towards a Recursively Self-Improving Agent for Deep Research | arXiv '26 | - | - |
| `Predictive Navigation` | [![arXiv](https://img.shields.io/badge/arXiv-2608.00432-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.00432)<br>Deep Research Pretraining via Predictive Navigation | arXiv '26 | - | - |
| `On-Device DR (4B)` | [![arXiv](https://img.shields.io/badge/arXiv-2607.12257-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2607.12257)<br>On-Device Deep Research at 4B: Exposure Bounds Faithfulness, Retrieval Bounds Coverage | arXiv '26 | - | - |
| `Carnot` | [![arXiv](https://img.shields.io/badge/arXiv-2608.09532-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.09532)<br>Carnot: Interpretable, Interactive, and Optimized Execution of Deep Research Queries | VLDB '26 | - | - |
| `Marginal Value Est.` | [![arXiv](https://img.shields.io/badge/arXiv-2608.08389-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.08389)<br>Not Worth Another Token: Marginal Value Estimation for Efficient Deep Research Agents | arXiv '26 | - | - |
| `Retrieval-Aware Control` | [![arXiv](https://img.shields.io/badge/arXiv-2608.15191-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.15191)<br>When Deep Research Agents Stagnate: Enhancing Reasoning with Retrieval-Aware Agent Control | arXiv '26 | - | - |
| `Analogical Deep Research` | [![arXiv](https://img.shields.io/badge/arXiv-2607.13602-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2607.13602)<br>Analogical Deep Research: Retrieving and Integrating Historical Analogies for Foresight Analysis | arXiv '26 | - | - |
| `Plato-Bio` | [![arXiv](https://img.shields.io/badge/arXiv-2607.23975-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2607.23975)<br>Plato-Bio: verification-first biological novelty screening with temporal rediscovery and structural benchmarks | arXiv '26 | - | - |
| `Albilich` | [![arXiv](https://img.shields.io/badge/arXiv-2607.27705-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2607.27705)<br>Albilich: Steerable Proof-State Orchestration for LLM-Based Mathematical Research with CAS Integration | arXiv '26 | - | - |
||

### Retrieval and Synthesis Quality Assessment

> In chronological order, from the earliest to the latest.

| Model | Paper | Venue | Website | GitHub |
|:-:|:-|:-:|:-:|:-:|
| `IBIS` | [![arXiv](https://img.shields.io/badge/arXiv-2608.23045-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.23045)<br>From Inertia to Objectivity: Improving Deep Research Agents with Noise Isolation | EMNLP '26 | - | - |
| `Agent to Blame` | [![arXiv](https://img.shields.io/badge/arXiv-2608.24306-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.24306)<br>Who is the Agent to Blame? Localizing Faithfulness and Citation Mistakes in Agentic Deep Research | EMNLP '26 | - | - |
||
| `DeepScholar-Bench` | [![arXiv](https://img.shields.io/badge/arXiv-2508.20033-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2508.20033)<br>DeepScholar-Bench: A Live Benchmark and Automated Evaluation for Generative Research Synthesis | arXiv '25 | - | [![GitHub](https://img.shields.io/github/stars/guestrin-lab/deepscholar-bench)](https://github.com/guestrin-lab/deepscholar-bench) |
| `ReportBench` | [![arXiv](https://img.shields.io/badge/arXiv-2508.15804-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2508.15804)<br>ReportBench: Evaluating Deep Research Agents via Academic Survey Tasks | arXiv '25 | - | [![GitHub](https://img.shields.io/github/stars/ByteDance-BandAI/ReportBench)](https://github.com/ByteDance-BandAI/ReportBench) |
| `IDRBench` | [![arXiv](https://img.shields.io/badge/arXiv-2601.06676-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2601.06676)<br>IDRBench: Interactive Deep Research Benchmark | arXiv '26 | - | - |
| `ScholarGym` | [![arXiv](https://img.shields.io/badge/arXiv-2601.21654-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2601.21654)<br>ScholarGym: Benchmarking Large Language Model Capabilities in the Information-Gathering Stage of Deep Research | arXiv '26 | - | - |
| `SciNetBench` | [![arXiv](https://img.shields.io/badge/arXiv-2601.03260-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2601.03260)<br>SciNetBench: A Relation-Aware Benchmark for Scientific Literature Retrieval Agents | arXiv '26 | - | - |
| `Super Research` | [![arXiv](https://img.shields.io/badge/arXiv-2603.00582-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2603.00582)<br>Super Research: Answering Highly Complex Questions with Large Language Models through Super Deep and Super Wide Research | arXiv '26 | [Website](https://cnsdqd-dyb.github.io/Super-Research-Benchmark/)<br>Data: [Hugging Face](https://huggingface.co/datasets/FreeFrank/Super-Research-Benchmark) | [![GitHub](https://img.shields.io/github/stars/cnsdqd-dyb/Super-Research-Benchmark)](https://github.com/cnsdqd-dyb/Super-Research-Benchmark) |
| `AutoResearchBench` | [![arXiv](https://img.shields.io/badge/arXiv-2604.25256-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2604.25256)<br>AutoResearchBench: Benchmarking AI Agents on Complex Scientific Literature Discovery | arXiv '26 | [Website](https://cheryou.github.io/autoresearchbench.github.io/)<br>Data: [Hugging Face](https://huggingface.co/datasets/Lk123/AutoResearchBench) | [![GitHub](https://img.shields.io/github/stars/CherYou/AutoResearchBench)](https://github.com/CherYou/AutoResearchBench) |
| `PaperMind` | [![arXiv](https://img.shields.io/badge/arXiv-2604.21304-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2604.21304)<br>PaperMind: Benchmarking Agentic Reasoning and Critique over Scientific Papers in Multimodal LLMs | arXiv '26 | - | - |
| `DRNOISE` | [![arXiv](https://img.shields.io/badge/arXiv-2607.17291-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2607.17291)<br>DRNOISE: Benchmarking Deep Research Agents in Misleading Evidence Environments | arXiv '26 | - | - |
| `HiEviDR-Bench` | [![arXiv](https://img.shields.io/badge/arXiv-2607.25151-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2607.25151)<br>HiEviDR-Bench: A Benchmark for Hierarchical Evidence Aggregation in Deep Research | arXiv '26 | - | - |
| `SciExplore` | [![arXiv](https://img.shields.io/badge/arXiv-2607.20926-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2607.20926)<br>SciExplore: Evaluating Autonomous Agents from Scientific Navigation to Information Integration | arXiv '26 | - | - |
| `WANDR` | [![arXiv](https://img.shields.io/badge/arXiv-2608.14747-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.14747)<br>WANDR: A Benchmark for Wide and Deep Research | arXiv '26 | - | - |
| `QA-to-DR Bench` | [![arXiv](https://img.shields.io/badge/arXiv-2608.02163-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.02163)<br>From Simple QA to Deep Research: A Verifiable Benchmark Constructed through Iterative Task Evolution | arXiv '26 | - | - |
| `PRISMA-LLM` | [![arXiv](https://img.shields.io/badge/arXiv-2609.11559-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2609.11559)<br>PRISMA-LLM: An Empirical Reporting Framework for AI-Assisted Systematic Reviews | arXiv '26 | - | - |
| `INSPIRE` | [![arXiv](https://img.shields.io/badge/arXiv-2609.33233-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2609.33233)<br>Inspire: Benchmarking Scientific Literature Search for Open Research Problems | arXiv '26 | - | - |
| `CESS` | [![arXiv](https://img.shields.io/badge/arXiv-2609.39026-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2609.39026)<br>Search Shapes Conclusions: Auditing Evidence Selection Bias in Deep Research Agents | arXiv '26 | - | - |
| `ScholarCatalyst` | [![arXiv](https://img.shields.io/badge/arXiv-2610.02202-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2610.02202)<br>ScholarCatalyst: A Benchmark for Retrieving Papers That Inspire New Research | arXiv '26 | - | [![GitHub](https://img.shields.io/github/stars/stanford-iris-lab/ScholarCatalyst)](https://github.com/stanford-iris-lab/ScholarCatalyst) |
||



# 3. Coding & Experimentation

### Code Generation

> In chronological order, from the earliest to the latest.

| Model | Paper | Venue | Website | GitHub |
|:-:|:-|:-:|:-:|:-:|
||
| `SWE-bench` | [![arXiv](https://img.shields.io/badge/arXiv-2310.06770-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2310.06770)<br>SWE-bench: Can Language Models Resolve Real-World GitHub Issues? | ICLR '24 | - | [![GitHub](https://img.shields.io/github/stars/princeton-nlp/SWE-bench)](https://github.com/princeton-nlp/SWE-bench) |
| `SWE-agent` | [![arXiv](https://img.shields.io/badge/arXiv-2405.15793-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2405.15793)<br>SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering | arXiv '24 | - | [![GitHub](https://img.shields.io/github/stars/princeton-nlp/SWE-agent)](https://github.com/princeton-nlp/SWE-agent) |
| `OpenHands` | [![arXiv](https://img.shields.io/badge/arXiv-2407.16741-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2407.16741)<br>OpenHands: An Open Platform for AI Software Developers as Generalist Agents | ICLR '25 | - | [![GitHub](https://img.shields.io/github/stars/All-Hands-AI/OpenHands)](https://github.com/All-Hands-AI/OpenHands) |
| `SWE-bench Pro` | [![arXiv](https://img.shields.io/badge/arXiv-2509.16941-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2509.16941)<br>SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? | arXiv '25 | - | - |
| `SWE-EVO` | [![arXiv](https://img.shields.io/badge/arXiv-2512.18470-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2512.18470)<br>SWE-EVO: Benchmarking Coding Agents in Long-Horizon Software Evolution Scenarios | arXiv '25 | - | - |
||

### Paper-to-Code

> In chronological order, from the earliest to the latest.

| Model | Paper | Venue | Website | GitHub |
|:-:|:-|:-:|:-:|:-:|
| `ReproAgent` | [![arXiv](https://img.shields.io/badge/arXiv-2608.24291-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.24291)<br>ReproAgent: Contract-Guided Paper-to-Code Reproduction | EMNLP '26 | - | - |
| `DeepRepro` | [![arXiv](https://img.shields.io/badge/arXiv-2608.26557-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.26557)<br>DeepRepro: State-Aware Subplanning for Paper-to-Code Reproduction in Evolving Repositories | CIKM '26 | - | - |
||
| `FunSearch` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://www.nature.com/articles/s41586-023-06924-6)<br>Mathematical Discoveries from Program Search with Large Language Models | Nature '24 | - | [![GitHub](https://img.shields.io/github/stars/google-deepmind/funsearch)](https://github.com/google-deepmind/funsearch) |
| `SciCode` | [![arXiv](https://img.shields.io/badge/arXiv-2407.13168-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2407.13168)<br>SciCode: A Research Coding Benchmark Curated by Scientists | arXiv '24 | - | [![GitHub](https://img.shields.io/github/stars/scicode-bench/SciCode)](https://github.com/scicode-bench/SciCode) |
| `PaperBench` | [![arXiv](https://img.shields.io/badge/arXiv-2504.01848-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2504.01848)<br>PaperBench: Evaluating AI's Ability to Replicate AI Research | arXiv '25 | - | [![GitHub](https://img.shields.io/github/stars/openai/preparedness)](https://github.com/openai/preparedness) |
| `PaperCoder` | [![arXiv](https://img.shields.io/badge/arXiv-2504.17192-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2504.17192)<br>Paper2Code: Automating Code Generation from Scientific Papers in Machine Learning | arXiv '25 | - | [![GitHub](https://img.shields.io/github/stars/going-doer/Paper2Code)](https://github.com/going-doer/Paper2Code) |
| `ResearchCodeBench` | [![arXiv](https://img.shields.io/badge/arXiv-2506.02314-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2506.02314)<br>ResearchCodeBench: Benchmarking LLMs on Implementing Novel ML Research Code | arXiv '25 | - | - |
| `SciReplicate-Bench` | [![arXiv](https://img.shields.io/badge/arXiv-2504.00255-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2504.00255)<br>SciReplicate-Bench: Benchmarking LLMs in Agent-driven Algorithmic Reproduction from Research Papers | arXiv '25 | - | [![GitHub](https://img.shields.io/github/stars/xyzCS/SciReplicate-Bench)](https://github.com/xyzCS/SciReplicate-Bench) |
| `PaperCompiler` | [![arXiv](https://img.shields.io/badge/arXiv-2609.02272-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2609.02272)<br>PaperCompiler: Faithful Paper-to-Code Generation via Repository-Level Specification Compilation | arXiv '26 | - | - |
||

### Experiment Execution & Orchestration

> In chronological order, from the earliest to the latest.

| Model | Paper | Venue | Website | GitHub |
|:-:|:-|:-:|:-:|:-:|
| `BMD` | [![arXiv](https://img.shields.io/badge/arXiv-2610.25747-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2610.25747)<br>Bayesian Model Discovery with Language Models: Closing the Loop between Hypotheses and Experiments | arXiv '26 | - | - |
| `DAGLoop` | [![arXiv](https://img.shields.io/badge/arXiv-2610.25089-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2610.25089)<br>DAGLoop: Aligning Method Design with Experimental Feedback in Automated AI Research | arXiv '26 | [Project](https://github.com/deng34567/DAGLoop) | - |
| `ResearchTrails` | [![arXiv](https://img.shields.io/badge/arXiv-2610.07184-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2610.07184)<br>Learning Scientific Exploration from Human Research Decision Trajectories | arXiv '26 | [Project](https://researchtrails.org) | [Code](https://github.com/xuchengong/ResearchTrails) |
| `Praxist` | [![arXiv](https://img.shields.io/badge/arXiv-2608.25955-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.25955)<br>Praxist: From Experimental Artifacts to Solution Lineages | arXiv '26 | - | - |
| `Skill-Based Baselines` | [![arXiv](https://img.shields.io/badge/arXiv-2608.23336-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.23336)<br>Can Coding Agents Build Robust Baselines? A Skill-Based Approach for Automating the Medical Imaging Model-Development Pipeline | MICCAI '26 | - | - |
||
| `BioPlanner` | [![arXiv](https://img.shields.io/badge/arXiv-2310.10632-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2310.10632)<br>BioPlanner: Automatic Evaluation of LLMs on Protocol Planning | arXiv '23 | - | [![GitHub](https://img.shields.io/github/stars/bioplanner/bioplanner)](https://github.com/bioplanner/bioplanner) |
| `CRISPR-GPT` | [![arXiv](https://img.shields.io/badge/arXiv-2404.18021-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2404.18021)<br>CRISPR-GPT for Agentic Automation of Gene-Editing Experiments | arXiv '24 | - | - |
| `DS-Agent` | [![arXiv](https://img.shields.io/badge/arXiv-2402.17453-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2402.17453)<br>DS-Agent: Automated Data Science by Empowering Large Language Models with Case-Based Reasoning | arXiv '24 | - | [![GitHub](https://img.shields.io/github/stars/guosyjlu/DS-Agent)](https://github.com/guosyjlu/DS-Agent) |
| `MLE-Bench` | [![arXiv](https://img.shields.io/badge/arXiv-2410.07095-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2410.07095)<br>MLE-Bench: Evaluating Machine Learning Agents on Machine Learning Engineering | arXiv '24 | - | - |
| `MLAgentBench` | [![arXiv](https://img.shields.io/badge/arXiv-2310.03302-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2310.03302)<br>MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation | arXiv '24 | - | [![GitHub](https://img.shields.io/github/stars/snap-stanford/MLAgentBench)](https://github.com/snap-stanford/MLAgentBench) |
| `MLR-Copilot` | [![arXiv](https://img.shields.io/badge/arXiv-2408.14033-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2408.14033)<br>MLR-Copilot: Autonomous Machine Learning Research based on Large Language Models Agents | arXiv '24 | - | - |
| `AIDE` | [![arXiv](https://img.shields.io/badge/arXiv-2502.13138-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2502.13138)<br>AIDE: AI-Driven Exploration in the Space of Code | arXiv '25 | - | [![GitHub](https://img.shields.io/github/stars/WecoAI/aideml)](https://github.com/WecoAI/aideml) |
| `AlphaEvolve` | [![arXiv](https://img.shields.io/badge/arXiv-2506.13131-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2506.13131)<br>AlphaEvolve: A Coding Agent for Scientific and Algorithmic Discovery | arXiv '25 | - | - |
| `AutoReproduce` | [![arXiv](https://img.shields.io/badge/arXiv-2505.20662-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2505.20662)<br>AutoReproduce: Automatic AI Experiment Reproduction with Paper Lineage | arXiv '25 | - | [![GitHub](https://img.shields.io/github/stars/AI9Stars/AutoReproduce)](https://github.com/AI9Stars/AutoReproduce) |
| `CURIE` | [![arXiv](https://img.shields.io/badge/arXiv-2502.16069-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2502.16069)<br>Curie: Toward Rigorous and Automated Scientific Experimentation with AI Agents | arXiv '25 | - | [![GitHub](https://img.shields.io/github/stars/Just-Curieous/Curie)](https://github.com/Just-Curieous/Curie) |
| `MLGym` | [![arXiv](https://img.shields.io/badge/arXiv-2502.14499-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2502.14499)<br>MLGym: A New Framework and Benchmark for Advancing AI Research Agents | arXiv '25 | - | - |
| `MLR-Bench` | [![arXiv](https://img.shields.io/badge/arXiv-2505.19955-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2505.19955)<br>MLR-Bench: Evaluating AI Agents on Open-Ended Machine Learning Research | arXiv '25 | - | - |
| `Execution-Grounded` | [![arXiv](https://img.shields.io/badge/arXiv-2601.14525-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2601.14525)<br>Towards Execution-Grounded Automated AI Research | arXiv '26 | - | - |
| `Learn to Discover` | [![arXiv](https://img.shields.io/badge/arXiv-2601.16175-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2601.16175)<br>Learning to Discover at Test Time | arXiv '26 | - | - |
| `AutoNumerics` | [![arXiv](https://img.shields.io/badge/arXiv-2602.17607-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2602.17607)<br>AutoNumerics: An Autonomous, PDE-Agnostic Multi-Agent Pipeline for Scientific Computing | arXiv '26 | - | [![GitHub](https://img.shields.io/github/stars/Daviddjddu/Autonumerics)](https://github.com/Daviddjddu/Autonumerics) |
| `SciNav` | [![arXiv](https://img.shields.io/badge/arXiv-2603.20256-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2603.20256)<br>SciNav: A General Agent Framework for Scientific Coding Tasks | arXiv '26 | - | - |
| `FrontierScience` | [![arXiv](https://img.shields.io/badge/arXiv-2601.21165-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2601.21165)<br>FrontierScience: Evaluating AI's Ability to Perform Expert-Level Scientific Tasks | arXiv '26 | - | - |
| `EvoDS` | [![arXiv](https://img.shields.io/badge/arXiv-2606.03841-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2606.03841)<br>EvoDS: Self-Evolving Autonomous Data Science Agent with Skill Learning and Context Management | arXiv '26 | - | - |
| `AutoTTS` | [![arXiv](https://img.shields.io/badge/arXiv-2605.08083-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2605.08083)<br>LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling | arXiv '26 | - | [![GitHub](https://img.shields.io/github/stars/zhengkid/AutoTTS)](https://github.com/zhengkid/AutoTTS) |
| `AutoScientists` | [![arXiv](https://img.shields.io/badge/arXiv-2605.28655-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2605.28655)<br>AutoScientists: Self-Organizing Agent Teams for Long-Running Scientific Experimentation | arXiv '26 | - | - |
| `EurekAgent` | [![arXiv](https://img.shields.io/badge/arXiv-2606.13662-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2606.13662)<br>EurekAgent: Agent Environment Engineering is All You Need For Autonomous Scientific Discovery | arXiv '26 | - | [![GitHub](https://img.shields.io/github/stars/THU-Team-Eureka/EurekAgent)](https://github.com/THU-Team-Eureka/EurekAgent) |
| `Experimental Experience Modeling` | [![arXiv](https://img.shields.io/badge/arXiv-2609.39392-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2609.39392)<br>Experimental Experience Modeling for Autonomous Research | arXiv '26 | - | - |
||

### Code Correctness and Reproducibility Assessment

> In chronological order, from the earliest to the latest.

| Model | Paper | Venue | Website | GitHub |
|:-:|:-|:-:|:-:|:-:|
| `VibeTraining-Bench` | [![arXiv](https://img.shields.io/badge/arXiv-2610.26342-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2610.26342)<br>VibeTraining-Bench: Data-Trainer-Harness Co-Design for Iterative System Improvement | arXiv '26 | - | - |
| `Auto-MD-bench` | [![arXiv](https://img.shields.io/badge/arXiv-2610.25069-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2610.25069)<br>Auto-MD-bench: Evaluating Autoresearch Agents for Real-World Medical Tasks | arXiv '26 | - | [![GitHub](https://img.shields.io/github/stars/Edwin0080/Auto-MD-bench)](https://github.com/Edwin0080/Auto-MD-bench) |
| `Author-in-loop Audit` | [![arXiv](https://img.shields.io/badge/arXiv-2610.22465-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2610.22465)<br>Author-in-the-loop Agentic Reproducibility Auditing for a Machine Learning Conference | arXiv '26 | - | - |
| `Autonomous Science Bench` | [![arXiv](https://img.shields.io/badge/arXiv-2610.18449-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2610.18449)<br>Autonomous Science Bench: Evaluating AI Agents for Autonomous Scientific Discovery | arXiv '26 | [Project](https://yibow.me/autonomous-science-bench) | [![GitHub](https://img.shields.io/github/stars/Yibo-Wen/as-bench)](https://github.com/Yibo-Wen/as-bench) |
| `ST-Bench` | [![arXiv](https://img.shields.io/badge/arXiv-2610.07763-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2610.07763)<br>ST-Bench: A Spatial-Temporal Benchmark for Multi-Agent System Generation on Scientific Research Tasks | arXiv '26 | - | - |
| `MMPostTrainBench` | [![arXiv](https://img.shields.io/badge/arXiv-2610.05398-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2610.05398)<br>MMPostTrainBench: Benchmarking Autonomous Research for Multimodal Post-Training | arXiv '26 | - | [Code](https://github.com/sod1010/MMPostTrainBench) |
| `Experimental Fidelity` | [![arXiv](https://img.shields.io/badge/arXiv-2608.26753-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.26753)<br>Beyond Execution: Auditing Experimental Fidelity in LLM-Driven Scientific Research | arXiv '26 | - | - |
||
| `DiscoveryBench` | [![arXiv](https://img.shields.io/badge/arXiv-2407.01725-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2407.01725)<br>DiscoveryBench: Towards Data-Driven Discovery with Large Language Models | arXiv '24 | - | [![GitHub](https://img.shields.io/github/stars/allenai/discoverybench)](https://github.com/allenai/discoverybench) |
| `DiscoveryWorld` | [![arXiv](https://img.shields.io/badge/arXiv-2406.06769-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2406.06769)<br>DiscoveryWorld: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents | arXiv '24 | - | [![GitHub](https://img.shields.io/github/stars/allenai/discoveryworld)](https://github.com/allenai/discoveryworld) |
| `InfiAgent-DABench` | [![arXiv](https://img.shields.io/badge/arXiv-2401.05507-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2401.05507)<br>InfiAgent-DABench: Evaluating Agents on Data Analysis Tasks | arXiv '24 | - | - |
| `ScienceAgentBench` | [![arXiv](https://img.shields.io/badge/arXiv-2410.05080-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2410.05080)<br>ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery | arXiv '24 | - | - |
| `LAB-Bench` | [![arXiv](https://img.shields.io/badge/arXiv-2407.10362-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2407.10362)<br>Lab-Bench: Measuring Capabilities of Language Models for Biology Research | arXiv '24 | - | [![GitHub](https://img.shields.io/github/stars/Future-House/LAB-Bench)](https://github.com/Future-House/LAB-Bench) |
| `KernelBench` | [![arXiv](https://img.shields.io/badge/arXiv-2502.10517-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2502.10517)<br>KernelBench: Can LLMs Write Efficient GPU Kernels? | arXiv '25 | - | [![GitHub](https://img.shields.io/github/stars/ScalingIntelligence/KernelBench)](https://github.com/ScalingIntelligence/KernelBench) |
| `TritonBench` | [![arXiv](https://img.shields.io/badge/arXiv-2502.14752-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2502.14752)<br>TritonBench: Benchmarking Large Language Model Capabilities for Generating Triton Operators | arXiv '25 | - | [![GitHub](https://img.shields.io/github/stars/thunlp/TritonBench)](https://github.com/thunlp/TritonBench) |
| `AstaBench` | [![arXiv](https://img.shields.io/badge/arXiv-2510.21652-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2510.21652)<br>AstaBench: Rigorous Benchmarking of AI Agents with a Scientific Research Suite | arXiv '25 | - | [![GitHub](https://img.shields.io/github/stars/allenai/asta-bench)](https://github.com/allenai/asta-bench) |
| `ResearchClawBench` | [![arXiv](https://img.shields.io/badge/arXiv-2512.16969-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2512.16969)<br>Probing Scientific General Intelligence of LLMs with Scientist-Aligned Workflows | arXiv '25 | - | [![GitHub](https://img.shields.io/github/stars/InternScience/ResearchClawBench)](https://github.com/InternScience/ResearchClawBench) |
| `EXP-Bench` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://openreview.net/forum?id=KjgyAm383Z)<br>EXP-Bench: Can AI Conduct AI Research Experiments? | ICLR '26 | - | [![GitHub](https://img.shields.io/github/stars/Just-Curieous/Curie)](https://github.com/Just-Curieous/Curie/tree/main/benchmark/exp_bench) |
| `PostTrainBench` | [![arXiv](https://img.shields.io/badge/arXiv-2603.08640-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2603.08640)<br>PostTrainBench: Can LLM Agents Automate LLM Post-Training? | arXiv '26 | - | [![GitHub](https://img.shields.io/github/stars/aisa-group/PostTrainBench)](https://github.com/aisa-group/PostTrainBench) |
| `MLReplicate` | [![arXiv](https://img.shields.io/badge/arXiv-2605.16616-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2605.16616)<br>MLReplicate: Benchmarking Autonomous Research Systems for Machine Learning Reproducibility | arXiv '26 | - | - |
| `BeyondSWE` | [![arXiv](https://img.shields.io/badge/arXiv-2603.03194-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2603.03194)<br>BeyondSWE: Can Current Code Agent Survive Beyond Single-Repo Bug Fixing? | arXiv '26 | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://aweai-team.github.io/BeyondSWE/) | [![GitHub](https://img.shields.io/github/stars/AweAI-Team/BeyondSWE)](https://github.com/AweAI-Team/BeyondSWE) |
| `NatureBench` | [![arXiv](https://img.shields.io/badge/arXiv-2606.24530-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2606.24530)<br>NatureBench: Can Coding Agents Match the Published SOTA of Nature-Family Papers? | arXiv '26 | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://frontisai.github.io/NatureBench/) | [![GitHub](https://img.shields.io/github/stars/FrontisAI/NatureBench)](https://github.com/FrontisAI/NatureBench) |
| `SciCoQA` | [![arXiv](https://img.shields.io/badge/arXiv-2601.12910-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2601.12910)<br>SciCoQA: Quality Assurance for Scientific Paper--Code Alignment | ACL '26 | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://ukplab.github.io/scicoqa/) | [![GitHub](https://img.shields.io/github/stars/UKPLab/scicoqa)](https://github.com/UKPLab/scicoqa) |
| `Dude` | [![arXiv](https://img.shields.io/badge/arXiv-2609.03416-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2609.03416)<br>Dude: A Dual-Detection Multi-Agent System for Paper-Code Discrepancy Detection | arXiv '26 | - | [![GitHub](https://img.shields.io/github/stars/VinnyLiu0817/Dude)](https://github.com/VinnyLiu0817/Dude) |
| `AgentActionBench` | [![arXiv](https://img.shields.io/badge/arXiv-2609.11117-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2609.11117)<br>Overview of the NLPCC 2026 Shared Task 11: Agent-Based Experiment Reproduction from Scientific Papers | arXiv '26 | - | - |
| `AutoDataBench` | [![arXiv](https://img.shields.io/badge/arXiv-2609.40097-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2609.40097)<br>AutoDataBench: A Data-centric Testbed for Accelerating Auto Research | arXiv '26 | - | [![GitHub](https://img.shields.io/github/stars/AutoDataBench/AutoDataBench)](https://github.com/AutoDataBench/AutoDataBench) |
| `EurekaBench` | [![arXiv](https://img.shields.io/badge/arXiv-2610.00492-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2610.00492)<br>EurekaBench: Measuring Agentic Ability to Discover New Scientific Insights | arXiv '26 | - | - |
||



# 4. Tables & Figures

### Scientific Figure Generation

> In chronological order, from the earliest to the latest.

| Model | Paper | Venue | Website | GitHub |
|:-:|:-|:-:|:-:|:-:|
||
| `ChartGPT` | [![arXiv](https://img.shields.io/badge/arXiv-2311.01920-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2311.01920)<br>ChartGPT: Leveraging LLMs to Generate Charts from Abstract Natural Language | arXiv '23 | - | - |
| `MatPlotAgent` | [![arXiv](https://img.shields.io/badge/arXiv-2402.11453-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2402.11453)<br>MatPlotAgent: Method and Evaluation for LLM-Based Agentic Scientific Data Visualization | arXiv '24 | - | - |
| `CoDA` | [![arXiv](https://img.shields.io/badge/arXiv-2510.03194-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2510.03194)<br>CoDA: Agentic Systems for Collaborative Data Visualization | arXiv '25 | - | - |
| `PlotGen` | [![arXiv](https://img.shields.io/badge/arXiv-2502.00988-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2502.00988)<br>PlotGen: Multi-Agent LLM-based Scientific Data Visualization via Multimodal Feedback | arXiv '25 | - | - |
| `VIS-Shepherd` | [![arXiv](https://img.shields.io/badge/arXiv-2506.13326-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2506.13326)<br>VIS-Shepherd: Constructing Critic for LLM-based Data Visualization Generation | arXiv '25 | - | - |
| `DiagramAgent` | [![arXiv](https://img.shields.io/badge/arXiv-2411.11916-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2411.11916)<br>From Words to Structured Visuals: A Benchmark and Framework for Text-to-Diagram Generation and Editing | CVPR '25 | - | - |
| `StarVector` | [![arXiv](https://img.shields.io/badge/arXiv-2312.11556-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2312.11556)<br>StarVector: Generating Scalable Vector Graphics Code from Images and Text | CVPR '25 | - | - |
| `VisCoder` | [![arXiv](https://img.shields.io/badge/arXiv-2506.03930-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2506.03930)<br>VisCoder: Fine-Tuning LLMs for Executable Python Visualization Code Generation | EMNLP '25 | - | - |
| `AI-Generated Figures` | [![arXiv](https://img.shields.io/badge/arXiv-2603.16159-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2603.16159)<br>AI-Generated Figures | arXiv '26 | - | - |
| `AutoFigure-Edit` | [![arXiv](https://img.shields.io/badge/arXiv-2603.06674-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2603.06674)<br>AutoFigure-Edit: Generating Editable Scientific Illustration | arXiv '26 | - | [![GitHub](https://img.shields.io/github/stars/ResearAI/AutoFigure-Edit)](https://github.com/ResearAI/AutoFigure-Edit) |
| `AutoFigure` | [![arXiv](https://img.shields.io/badge/arXiv-2602.03828-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2602.03828)<br>AutoFigure-Edit: Generating Editable Scientific Illustration | ICLR '26 | - | [![GitHub](https://img.shields.io/github/stars/ResearAI/AutoFigure)](https://github.com/ResearAI/AutoFigure) |
| `PaperBanana` | [![arXiv](https://img.shields.io/badge/arXiv-2601.23265-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2601.23265)<br>PaperBanana: Automating Academic Illustration for AI Scientists | ICML '26 (Spotlight) | [Website](https://dwzhu-pku.github.io/PaperBanana/) | [PaperBanana](https://github.com/dwzhu-pku/PaperBanana) / [PaperVizAgent](https://github.com/google-research/papervizagent) |
| `SAIL` | [![arXiv](https://img.shields.io/badge/arXiv-2603.18145-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2603.18145)<br>Setting SAIL: Leveraging Scientist-AI-Loops for Rigorous Visualization Tools | arXiv '26 | - | - |
| `Crafter` | [![arXiv](https://img.shields.io/badge/arXiv-2605.30611-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2605.30611)<br>Crafter: A Multi-Agent Harness for Editable Scientific Figure Generation from Diverse Inputs | arXiv '26 | - | - |
| `DiagramRAG` | [![arXiv](https://img.shields.io/badge/arXiv-2605.27931-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2605.27931)<br>DiagramRAG: A Lightweight Framework to Retrieve Scientific Diagram for Figure Generation | arXiv '26 | - | - |
| `GeoSVG-RL` | [![arXiv](https://img.shields.io/badge/arXiv-2605.25447-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2605.25447)<br>GeoSVG-RL: Geometry-Aware Reinforcement Learning for Layout-Constrained Text-to-SVG Diagram Generation | arXiv '26 | - | - |
| `Can AI Draw Sci.` | [![arXiv](https://img.shields.io/badge/arXiv-2606.28406-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2606.28406)<br>Can AI Draw Science? A Benchmark for Evaluating Scientific Figure Generation by Text-to-Image and Multimodal Models | arXiv '26 | - | - |
| `SciDiagramEdit` | [![arXiv](https://img.shields.io/badge/arXiv-2607.15272-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2607.15272)<br>SciDiagramEdit: Learning to Edit Scientific Diagrams from Paper Revisions | arXiv '26 | - | - |
| `GenGA` | [![arXiv](https://img.shields.io/badge/arXiv-2608.05478-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.05478)<br>GenGA: Editable and Data-Grounded Graphical Abstract Generation for Academic Papers | arXiv '26 | - | - |
| `FigTree` | [![arXiv](https://img.shields.io/badge/arXiv-2609.01006-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2609.01006)<br>Figures as Programs: Recursive Generation of Editable Scientific Figures | arXiv '26 | - | - |
| `EdiTikZ` | [![arXiv](https://img.shields.io/badge/arXiv-2609.01409-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2609.01409)<br>EdiTikZ: Scientific Figure Editing from Revision Trajectories | arXiv '26 | - | [![GitHub](https://img.shields.io/github/stars/NL2G/EdiTikZ)](https://github.com/NL2G/EdiTikZ) |
||

### Table Understanding & Generation

> In chronological order, from the earliest to the latest.

| Model | Paper | Venue | Website | GitHub |
|:-:|:-|:-:|:-:|:-:|
||
| `ArxivDIGESTables` | [![arXiv](https://img.shields.io/badge/arXiv-2410.22360-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2410.22360)<br>ArxivDIGESTables: Synthesizing Scientific Literature into Tables using Language Models | EMNLP '24 | - | - |
| `Chain-of-Table` | [![arXiv](https://img.shields.io/badge/arXiv-2401.04398-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2401.04398)<br>Chain-of-Table: Evolving Tables in Reasoning Chain for Table Understanding | ICLR '24 | - | - |
| `ShowTable` | [![arXiv](https://img.shields.io/badge/arXiv-2512.13303-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2512.13303)<br>ShowTable: Unlocking Creative Table Visualization with Collaborative Reflection and Refinement | CVPR '26 | - | - |
| `Table2LaTeX-RL` | [![arXiv](https://img.shields.io/badge/arXiv-2509.17589-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2509.17589)<br>Table2LaTeX-RL: Converting Table Images to High-Fidelity LaTeX Code Using Reinforced Multimodal Language Models | arXiv '25 | - | - |
| `CSPO` | [![arXiv](https://img.shields.io/badge/arXiv-2604.10918-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2604.10918)<br>CSPO: Alleviating Reward Ambiguity for Structured Table-to-LaTeX Generation | arXiv '26 | - | - |
||

### Mathematical Formulas & TikZ

> In chronological order, from the earliest to the latest.

| Model | Paper | Venue | Website | GitHub |
|:-:|:-|:-:|:-:|:-:|
||
| `AutomaTikZ` | [![arXiv](https://img.shields.io/badge/arXiv-2310.00367-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2310.00367)<br>AutomaTikZ: Text-Guided Synthesis of Scientific Vector Graphics with TikZ | ICLR '24 | - | - |
| `DeTikZify` | [![arXiv](https://img.shields.io/badge/arXiv-2405.15306-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2405.15306)<br>DeTikZify: Synthesizing Graphics Programs for Scientific Figures and Sketches with TikZ | NeurIPS '24 | - | - |
| `TikZilla` | [![arXiv](https://img.shields.io/badge/arXiv-2603.03072-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2603.03072)<br>TikZilla: Scaling Text-to-TikZ with High-Quality Data and Reinforcement Learning | arXiv '26 | - | - |
| `Edit2TikZ` | [![arXiv](https://img.shields.io/badge/arXiv-2608.13441-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.13441)<br>Edit2TikZ: A Comprehensive and Challenging Benchmark for Scientific Figure Editing with TikZ | arXiv '26 | - | - |
||

### Visual Fidelity and Scientific Accuracy Assessment

> In chronological order, from the earliest to the latest.

| Model | Paper | Venue | Website | GitHub |
|:-:|:-|:-:|:-:|:-:|
||
| `StructEval` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://openreview.net/forum?id=buDwV7LUA7)<br>StructEval: Benchmarking LLMs' Capabilities to Generate Structural Outputs | TMLR '25 | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://tiger-ai-lab.github.io/StructEval/) | [![GitHub](https://img.shields.io/github/stars/TIGER-AI-Lab/StructEval)](https://github.com/TIGER-AI-Lab/StructEval) |
| `PlotCraft` | [![arXiv](https://img.shields.io/badge/arXiv-2511.00010-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2511.00010)<br>PlotCraft: Pushing the Limits of LLMs for Complex and Interactive Data Visualization | arXiv '25 | - | - |
| `TeXpert` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://aclanthology.org/2025.sdp-1.2/)<br>TeXpert: Multi-Level Benchmark for LaTeX Code Generation | SDP '25 | - | - |
| `AbGen` | [![arXiv](https://img.shields.io/badge/arXiv-2507.13300-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2507.13300)<br>AbGen: Evaluating Large Language Models in Ablation Study Design and Evaluation for Scientific Research | ACL '25 | - | - |
| `SciFig` | [![arXiv](https://img.shields.io/badge/arXiv-2601.04390-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2601.04390)<br>SciFig: Towards Automating Scientific Figure Generation | arXiv '26 | - | - |
| `SciFlow-Bench` | [![arXiv](https://img.shields.io/badge/arXiv-2602.09809-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2602.09809)<br>SciFlow-Bench: Evaluating Structure-Aware Scientific Diagram Generation via Inverse Parsing | arXiv '26 | - | - |
| `FigureBench` | [![arXiv](https://img.shields.io/badge/arXiv-2602.03828-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2602.03828)<br>AutoFigure: Generating and Refining Publication-Ready Scientific Illustrations | ICLR '26 | - | [![GitHub](https://img.shields.io/github/stars/ResearAI/AutoFigure)](https://github.com/ResearAI/AutoFigure) |
| `SciFigQual-Bench` | [![arXiv](https://img.shields.io/badge/arXiv-2607.27084-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2607.27084)<br>SciFigQual-Bench: A Benchmark for Scientific Figure Quality Assessment with Full-Manuscript Context | arXiv '26 | - | - |
| `SciFigAlign` | [![arXiv](https://img.shields.io/badge/arXiv-2607.27066-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2607.27066)<br>SciFigAlign: Scoring Scientific Figures by Fine-tuned Alignment of Visuals with Manuscript Evidence | arXiv '26 | - | - |
| `SciFigPlag-Bench` | [![arXiv](https://img.shields.io/badge/arXiv-2607.29124-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2607.29124)<br>SciFigPlag-Bench: A Benchmark for Provenance-Aware Scientific Figure Plagiarism Detection | arXiv '26 | - | - |
| `VLM Blind/Misled` | [![arXiv](https://img.shields.io/badge/arXiv-2608.13267-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.13267)<br>How Do VLMs Behave When Blind or Misled? Behavioral Evaluation of VLMs on Scientific Figures | arXiv '26 | - | - |
| `SciFigure2Code` | [![arXiv](https://img.shields.io/badge/arXiv-2609.08155-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2609.08155)<br>SciFigure2Code: An AI-Reconstructed Benchmark for Scientific Figure-to-Code | arXiv '26 | - | - |
| `ReFigBench` | [![arXiv](https://img.shields.io/badge/arXiv-2609.18844-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2609.18844)<br>ReFigBench: Benchmarking Scientific Figure Reconstruction as Editable PowerPoint Artifacts | arXiv '26 | - | - |
||



# 5. Paper Writing

### Semi-Automated Writing Assistance

> In chronological order, from the earliest to the latest.

| Model | Paper | Venue | Website | GitHub |
|:-:|:-|:-:|:-:|:-:|
||
| `CoAuthor` | [![arXiv](https://img.shields.io/badge/arXiv-2201.06796-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2201.06796)<br>CoAuthor: Human-AI Collaborative Writing with Language Models | arXiv '22 | - | - |
| `AI Writing Study` | [![arXiv](https://img.shields.io/badge/arXiv-2506.20595-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2506.20595)<br>AI Writing Study | AIED '25 | - | - |
| `DraftMarks` | [![arXiv](https://img.shields.io/badge/arXiv-2509.23505-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2509.23505)<br>DraftMarks: Enhancing Transparency in Human-AI Co-Writing Through Interactive Skeuomorphic Process Traces | arXiv '25 | - | - |
| `PaperDebugger` | [![arXiv](https://img.shields.io/badge/arXiv-2512.02589-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2512.02589)<br>PaperDebugger: A Plugin-Based Multi-Agent System for In-Editor Academic Writing, Review, and Editing | arXiv '25 | - | [![GitHub](https://img.shields.io/github/stars/PaperDebugger/PaperDebugger)](https://github.com/PaperDebugger/PaperDebugger) |
| `ScholarCopilot` | [![arXiv](https://img.shields.io/badge/arXiv-2504.00824-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2504.00824)<br>ScholarCopilot: Training LLMs for Academic Writing with Integrated Citation | arXiv '25 | - | - |
| `XtraGPT` | [![arXiv](https://img.shields.io/badge/arXiv-2505.11336-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2505.11336)<br>XtraGPT: Context-Aware and Controllable Academic Paper Revision | arXiv '25 | - | - |
| `LimAgents` | [![arXiv](https://img.shields.io/badge/arXiv-2601.11578-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2601.11578)<br>Multi-Agent LLMs for Generating Research Limitations | arXiv '26 | - | - |
| `PaperMentor` | [![arXiv](https://img.shields.io/badge/arXiv-2606.08857-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2606.08857)<br>PaperMentor: A Human-Centered Multi-Agent Writing Tutor for AI Research Papers on Overleaf | arXiv '26 | - | - |
| `AutoSupervision` | [![arXiv](https://img.shields.io/badge/arXiv-2607.27845-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2607.27845)<br>AutoSupervision: Closing the Feedback Loop in Scientific Workflows with Grounded Revision Verification | arXiv '26 | - | - |
| `ReasFlow` | [![arXiv](https://img.shields.io/badge/arXiv-2607.14178-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2607.14178)<br>ReasFlow: Assisting Reasoning-Centric Scientific Discovery in Applied Mathematics via a Knowledge-Based Multi-Agent System | arXiv '26 | - | - |
||

### Fully Automated Paper Generation

> In chronological order, from the earliest to the latest.

| Model | Paper | Venue | Website | GitHub |
|:-:|:-|:-:|:-:|:-:|
||
| `CycleResearcher` | [![arXiv](https://img.shields.io/badge/arXiv-2411.00816-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2411.00816)<br>CycleResearcher: Improving Automated Research via Automated Review | ICLR '25 | - | - |
| `Agent Laboratory` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://aclanthology.org/2025.findings-emnlp.320/)<br>Agent Laboratory: Using LLM Agents as Research Assistants | EMNLP '25 | - | - |
| `FutureGen` | [![arXiv](https://img.shields.io/badge/arXiv-2503.16561-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2503.16561)<br>FutureGen: A RAG-based Approach to Generate the Future Work of Scientific Article | arXiv '25 | - | - |
| `AI Scientist` | [![arXiv](https://img.shields.io/badge/arXiv-2408.06292-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2408.06292)<br>The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery | Nature '26 | - | [![GitHub](https://img.shields.io/github/stars/SakanaAI/AI-Scientist)](https://github.com/SakanaAI/AI-Scientist) |
| `APRES` | [![arXiv](https://img.shields.io/badge/arXiv-2603.03142-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2603.03142)<br>APRES: An Agentic Paper Revision and Evaluation System | arXiv '26 | - | - |
| `LECTOR` | [![arXiv](https://img.shields.io/badge/arXiv-2605.25964-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2605.25964)<br>LECTOR: Joint Optimization of Scientific Reasoning Graphs and Introduction Generation | arXiv '26 | - | - |
| `RWGBench` | [![arXiv](https://img.shields.io/badge/arXiv-2606.24894-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2606.24894)<br>RWGBench: Evaluating Scholarly Positioning in Related Work Generation | arXiv '26 | - | - |
||

### Societal Analysis

> In chronological order, from the earliest to the latest.

| Model | Paper | Venue | Website | GitHub |
|:-:|:-|:-:|:-:|:-:|
||
| `AI Writing Adoption` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://www.nature.com/articles/s41586-025-08681-8)<br>AI Writing Adoption | Nature '26 | - | - |
| `Nature AI Survey` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://www.nature.com/articles/d41586-025-04066-5)<br>More than Half of Researchers Now Use AI for Peer Review | Nature '26 | - | - |
| `Denial of Science` | [![arXiv](https://img.shields.io/badge/arXiv-2607.10712-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2607.10712)<br>Distributed Denial of Science: How Indirect Data Poisoning of AI Systems Can Industrialize Scientific Fraud | arXiv '26 | - | - |
| `AI Slop OSS` | [![arXiv](https://img.shields.io/badge/arXiv-2607.04003-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2607.04003)<br>"AI Slop is DDoSing Open Source": Understanding the Impact of AI-Generated Contributions on Open Source Sustainability | arXiv '26 | - | - |
||

### Writing Quality and AI Detection Assessment

> In chronological order, from the earliest to the latest.

| Model | Paper | Venue | Website | GitHub |
|:-:|:-|:-:|:-:|:-:|
||
| `Mapping LLM Use` | [![arXiv](https://img.shields.io/badge/arXiv-2404.01268-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2404.01268)<br>Mapping the Increasing Use of LLMs in Scientific Papers | arXiv '24 | - | - |
| `CycleReviewer` | [![arXiv](https://img.shields.io/badge/arXiv-2411.00816-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2411.00816)<br>CycleResearcher: Improving Automated Research via Automated Review | ICLR '25 | - | - |
| `Stanford Agentic` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://paperreview.ai/tech-overview)<br>Stanford Agentic | Web '25 | - | - |
| `SciIG` | [![arXiv](https://img.shields.io/badge/arXiv-2508.14273-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2508.14273)<br>Let's Use ChatGPT To Write Our Paper! Benchmarking LLMs To Write the Introduction of a Research Paper | arXiv '25 | - | - |
| `Watermarking` | [![arXiv](https://img.shields.io/badge/arXiv-2503.15772-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2503.15772)<br>Detecting LLM-Generated Peer Reviews | arXiv '25 | - | - |
| `PaperWritingBench` | [![arXiv](https://img.shields.io/badge/arXiv-2604.05018-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2604.05018)<br>PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing | arXiv '26 | - | - |
| `CiteTracer` | [![arXiv](https://img.shields.io/badge/arXiv-2605.08583-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2605.08583)<br>Source or It Didn't Happen: A Multi-Agent Framework for Citation Hallucination Detection | arXiv '26 | - | - |
| `Process Eval` | [![arXiv](https://img.shields.io/badge/arXiv-2606.15583-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2606.15583)<br>Process-Oriented Evaluation of AI-Assisted Scientific Writing | arXiv '26 | - | - |
| `SciSlopBench / SciSlopHarness` | [![arXiv](https://img.shields.io/badge/arXiv-2610.00531-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2610.00531)<br>Science or Slop?: Benchmarking and Mitigating Scientific Slop in AI-Generated Papers | arXiv '26 | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://yerimoh.github.io/scientific-slop-demo/) | - |
||



# 6. Peer Review

### Automated Review Generation

> In chronological order, from the earliest to the latest.

| Model | Paper | Venue | Website | GitHub |
|:-:|:-|:-:|:-:|:-:|
| `RoundtableReview` | [![arXiv](https://img.shields.io/badge/arXiv-2610.24050-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2610.24050)<br>Discuss More, Comment Less: Boosting Automated Research via Multi-Perspective Collaborative Review | arXiv '26 | - | - |
||
| `ChatReviewer` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://github.com/nishiwen1214/ChatReviewer)<br>ChatReviewer: ChatGPT-based Paper Reviewing and Response Generation | GitHub '23 | - | [![GitHub](https://img.shields.io/github/stars/nishiwen1214/ChatReviewer)](https://github.com/nishiwen1214/ChatReviewer) |
| `AI-Peer-Review` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://github.com/poldrack/ai-peer-review)<br>AI-Peer-Review | GitHub '24 | - | [![GitHub](https://img.shields.io/github/stars/poldrack/ai-peer-review)](https://github.com/poldrack/ai-peer-review) |
| `MARG` | [![arXiv](https://img.shields.io/badge/arXiv-2401.04259-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2401.04259)<br>MARG: Multi-Agent Review Generation for Scientific Papers | arXiv '24 | - | - |
| `Reviewer2` | [![arXiv](https://img.shields.io/badge/arXiv-2402.10886-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2402.10886)<br>Reviewer2: Optimizing Review Generation Through Prompt Generation | arXiv '24 | - | - |
| `ReviewRL` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://aclanthology.org/2025.emnlp-main.857/)<br>ReviewRL: Towards Automated Scientific Review with RL | EMNLP '25 | - | - |
| `DeepReviewer` | [![arXiv](https://img.shields.io/badge/arXiv-2503.08569-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2503.08569)<br>DeepReview: Improving LLM-based Paper Review with Human-like Deep Thinking Process | arXiv '25 | - | - |
| `OpenReviewer` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://aclanthology.org/2025.naacl-demo.44/)<br>OpenReviewer: A Specialized Large Language Model for Generating Critical Scientific Paper Reviews | NAACL '25 | - | - |
| `REMOR` | [![arXiv](https://img.shields.io/badge/arXiv-2505.11718-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2505.11718)<br>REMOR: Automated Peer Review Generation with LLM Reasoning and Multi-Objective Reinforcement Learning | arXiv '25 | - | - |
| `ScholarPeer` | [![arXiv](https://img.shields.io/badge/arXiv-2601.22638-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2601.22638)<br>ScholarPeer: A Context-Aware Multi-Agent Framework for Automated Peer Review | arXiv '26 | - | - |
| `ProReviewer` | [![arXiv](https://img.shields.io/badge/arXiv-2606.13349-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2606.13349)<br>From Passive Generation to Investigation: A Proactive Scientific Peer Review Agent | arXiv '26 | - | - |
| `PeerCheck` | [![arXiv](https://img.shields.io/badge/arXiv-2606.20897-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2606.20897)<br>PeerCheck: Enhancing LLM-Generated Academic Reviews Towards Human-Level Quality | arXiv '26 | - | - |
| `Local Pre-Screening` | [![arXiv](https://img.shields.io/badge/arXiv-2608.14625-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.14625)<br>Local AI pre-screening for human triple-blind peer review in health sciences | arXiv '26 | - | - |
| `ReVoicer` | [![arXiv](https://img.shields.io/badge/arXiv-2608.00299-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.00299)<br>ReVoicer: Conversational Voice Annotation for Human-Centered, LLM-Assisted Peer Review | arXiv '26 | - | - |
| `ActReview` | [![arXiv](https://img.shields.io/badge/arXiv-2609.09076-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2609.09076)<br>ActReview: Rebuttal-Guided Training Data and Rubric Rewards for Actionable Peer Review Generation | arXiv '26 | - | - |
| `PaperDoctor` | [![arXiv](https://img.shields.io/badge/arXiv-2609.16995-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2609.16995)<br>PaperDoctor: Evidence-Grounded and Actionable Feedback for Scientific Papers in Progress | arXiv '26 | - | [![GitHub](https://img.shields.io/github/stars/QinghongLin/paperdoctor)](https://github.com/QinghongLin/paperdoctor) |
||

### Meta-Review & Reviewer Matching

> In chronological order, from the earliest to the latest.

| Model | Paper | Venue | Website | GitHub |
|:-:|:-|:-:|:-:|:-:|
| `Metag` | [![arXiv](https://img.shields.io/badge/arXiv-2608.20488-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2608.20488)<br>Metag: A dataset to build agentic meta-reviewing capabilities | arXiv '26 | - | - |
||
| `AgentReview` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://aclanthology.org/2024.emnlp-main.70/)<br>AgentReview: Exploring Peer Review Dynamics with LLM Agents | EMNLP '24 | - | - |
| `Meta-Review LLMs` | [![Website](https://img.shields.io/badge/Link-yellow?style=flat-square&logo=gitbook)](https://aclanthology.org/2025.naacl-long.395/)<br>Meta-Review LLMs | NAACL '25 | - | - |
| `RATE` | [![arXiv](https://img.shields.io/badge/arXiv-2601.19637-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2601.19637)<br>RATE: Reviewer Profiling and Annotation-free Training for Expertise Ranking in Peer Review Systems | arXiv '26 | - | - |
| `MERIT` | [![arXiv](https://img.shields.io/badge/arXiv-2605.27865-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2605.27865)<br>MERIT: Matching Expertise via Rubric-Informed Training for Reviewer Assignment | arXiv '26 | - | - |
||

### Adversarial Attacks & Bias Analysis

> In chronological order, from the earliest to the latest.

| Model | Paper | Venue | Website | GitHub |
|:-:|:-|:-:|:-:|:-:|
||
| `Raina etal` | [![arXiv](https://img.shields.io/badge/arXiv-2402.14016-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2402.14016)<br>Raina etal | EMNLP '24 | - | - |
| `AI Review Lottery` | [![arXiv](https://img.shields.io/badge/arXiv-2405.02150-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2405.02150)<br>The AI Review Lottery: Widespread AI-Assisted Peer Reviews Boost Paper Scores and Acceptance Rates | arXiv '24 | - | - |
| `Ye etal` | [![arXiv](https://img.shields.io/badge/arXiv-2412.01708-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2412.01708)<br>Ye etal | arXiv '24 | - | - |
| `Breaking the Reviewer` | [![arXiv](https://img.shields.io/badge/arXiv-2506.11113-b31b1b?style=flat-square&logo=arxiv)](https://arxiv.org/abs/2506.11113)<br>Breaking the Reviewer: Assessing the Vulner