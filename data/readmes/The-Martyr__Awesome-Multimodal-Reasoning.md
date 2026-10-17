# Awesome-Multimodal-Reasoning [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)



This is a repository for organizing papers related to Multimodal Reasoning in Multimodal Large Language Models (Image, Video).



With the development of the visual (audio) capabilities and reasoning capabilities (RL powered) of multimodal large language models(MLLMs/LVLMs/LSLMs), researchers have high hopes for the multimodal reasoning capabilities of MLLM/LVLM/LSLM.



This repo also select paper about visual generation (image generation/video generation) with RL/CoT.



**This repository aims to cover ALL possibly relevant papers to support research surveys, not just selected best papers.** We believe comprehensive coverage is more valuable for researchers than a curated list.



#### :star: If you find this list useful, welcome to star it!



## Table of Contents

- [Survey](#survey)

- [Image Reasoning](#image-reasoning)

- [Agent](#agent)

- [Embodied / Robotics](#embodied--robotics)

- [Video](#video)

- [DLLM](#dllm)

- [Audio](#audio)

- [Image/Video Generation](#imagevideo-generation)

- [Bench/Dataset](#benchdataset)

- [Latent](#latent)

- [Open Source Project](#open-source-project)



## Paper List (Updating...)



### Survey



(06 Jun 2026) Test-Time Scaling in Multimodal Foundation Models: A Comprehensive Survey of Generation and Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.08231)



(01 Jun 2026) TechRAG: Evidence-Gated Multimodal Agentic RAG for Technical Literature Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.01613)



(20 May 2026) A Survey of Audio Reasoning in Multimodal Foundation Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.21008)



(05 May 2026) Material Database Agent: A Multimodal Agentic Framework for Scientific Literature Mining [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.04278)



(25 Apr 2026) GAZE: Grounded Agentic Zero-shot Evaluation with Viewer-Level Tools and Literature Retrieval on Rare Brain MRI [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.00876)



(8 May 2025) Perception, Reason, Think, and Plan: A Survey on Large Multimodal Reasoning Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2505.04921v1)



(30 Apr 2025) Reinforced MLLM: A Survey on RL-Based Reasoning in Multimodal Large Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2504.21277v1)



(4 Apr 2025) Why Reasoning Matters? A Survey of Advancements in Multimodal Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2504.03151v1)



(18 Mar 2025) Aligning Multimodal LLM with Human Preference: A Survey [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2503.14504)



(16 Mar 2025) Multimodal Chain-of-Thought Reasoning: A Comprehensive Survey [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2503.12605)


### Image Reasoning

(09 Sep 2026) On-Policy Distillation for Vision-Language Model Adaptation, an Effective Paradigm on Low-Quality Multimodal Data [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.10321)

(09 Sep 2026) Beyond Surface Imitation: Contrastive Modeling for Reasoning Path Alignment in Multimodal In-Context Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.10177)

(09 Sep 2026) From Pixels to Hierarchical Sequences: Quadtree Mask Encoding for Vision-Language Binary Change Detection [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.09876)

(08 Sep 2026) Drive by Hindsight and Foresight: Tool-Grounded Synergistic Reasoning over Hierarchical Memory for Autonomous Driving [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.08217)

(08 Sep 2026) From Glance to Scrutiny: Progressive Distortion Reasoning for Fine-Grained Image Quality Assessment [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.08316)

(08 Sep 2026) SeGDeP: Semantic- and Geometric-Aware Decoupled Prompts for Reasoning Segmentation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.08867)

(08 Sep 2026) CoVeR: Coverage-Based Token Pruning for Multi-View 3D Reasoning in VLMs [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.08345)

(07 Sep 2026) Stable-MM-R1: Anchoring Multimodal Reasoning Dynamics via Entropy-Guided Stratification [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.07148)

(07 Sep 2026) SupGRPO: Enhancing GRPO with Matching-based Online SFT for Text Spotting [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.07081)

(07 Sep 2026) MV-STRIDE: Enabling MLLMs to Master Multi-View Spatial Reasoning via Hierarchical Capability Modeling [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.07258)

(06 Sep 2026) Counterfactual Tests for Measuring Chain-of-Thought Faithfulness in Visual Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.06704)

(06 Sep 2026) Separating Capability from Confidence: Grounded Dual-State Calibration for GRPO-Trained Medical Vision-Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.06419)

(05 Sep 2026) Distilling Vision-Language Models for On-Device Fire Understanding [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.05782)

(05 Sep 2026) Geometry-Aware Test-Time Learning for Quantitative Spatial Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.06004)

(04 Sep 2026) MCPO: Modality-Contrastive Preference Optimization for Multimodal Chain-of-Thought Compression [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.04947)

(04 Sep 2026) Think-Verify-Revise: Neuro-Symbolic Visual Reasoning with Vision-Language Models and Dynamic Logic Tensor Networks [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.05388)

(03 Sep 2026) Revisiting Topological Graphs for Macro Action based Closed-loop Reinforcement Learning of Vision Language Navigation in Continuous Environment [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.03906)

(03 Sep 2026) CORE: Improving Compositional Reasoning in MLLM Embedding via Reranker Distillation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.04083)

(03 Sep 2026) When Depth Hurts: Reliability-Aware Geometry Distillation for Depth-Free RGB-D Salient Object Detection [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.03378)

(03 Sep 2026) MedQA-MM: Shortcuts Behind Medical Visual Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.03261)

(03 Sep 2026) GraFT: A Training-Free Framework for Spatial Reasoning in Multimodal Large Language Models via 3D Scene Graphs [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.03892)

(02 Sep 2026) CA-OPD: Confidence-Aware On-Policy Distillation for Structured Visual Prediction [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.02401)

(02 Sep 2026) Test-Time Logit Prompting for Source-Free Missing Modality Adaptation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.02039)

(01 Sep 2026) Controllable Image Captioning with Prompt-Conditioned Scene Rewards [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.00709)

(01 Sep 2026) MERGED: Multimodal Entity Resolution via Generated Expert Reasoning Distillation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.01913)

(01 Sep 2026) GazeRefine: Expert Gaze as a Test-Time Prompt for Training-Free Medical Image Segmentation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.01310)

(01 Sep 2026) Towards reliable multimodal disaster severity assessment through preference optimization and explainable vision-language reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.00879)

(01 Sep 2026) A Glance Is All You Need: Single-Pass Fine-Grained Image Captioning with SimLoss [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.00591)

(01 Sep 2026) Separating perception from reasoning in vision-language models: a model-free render ceiling for crystal structures [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.00663)

(01 Sep 2026) Text Capability Loss in Vision-Language Adaptation: An Attention-Sink Diagnosis [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.00746)

(01 Sep 2026) Does Playing it Safe Count as Faithfulness? Reassessing LVLM Hallucination Mitigation Methods [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.01888)

(31 Aug 2026) Aligning Multi-Trajectory Supervision with Policy Optimization for VLA Driving [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.30122)

(31 Aug 2026) Learning Where Outcomes Change:Credit-Addressable Reasoning for Multimodal Geometry [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.30457)

(31 Aug 2026) Reactivating Test-Time Scaling for Plane Geometry Problem Solving [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.30156)

(31 Aug 2026) SlideBank: A Persistent Hierarchical Evidence Bank for Consistent Whole-Slide Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2609.00342)

(30 Aug 2026) InspectorGPT: A Comparative Reasoning Enhanced VLM for Comprehensive Industrial Anomaly Detection [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.29783)

(30 Aug 2026) Drive the Thoughts: Runtime Monitoring of VLA Reasoning-Trajectory Consistency [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.29583)

(29 Aug 2026) Think, Look, and Revise: Inconsistency-Aware Visual Self-Correction in MLLMs [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.29374)

(29 Aug 2026) GATE: Reliability-Gated Gaussian Evidence Fusion for Training-Free Test-Time Adaptation of Vision-Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.29395)

(27 Aug 2026) Instruction Distillation: Text Instructions as Visual Examples [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.28696)

(27 Aug 2026) From Reasoning to Pixels: Grounded Medical Multimodal LLMs for VQA and Segmentation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.26856)

(27 Aug 2026) Not Just Reason, Not Just Scan: Reinforcement Learning for Proactive Scientific Error Verification over Academic Paper [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.26596)

(26 Aug 2026) V-Rubrics: Visual Faithfulness via Rubric-Based Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.25580)

(26 Aug 2026) GGSS: Geodesic-Gated Spherical Steering for Inference-Time Debiasing of Generative Vision-Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.25375)

(25 Aug 2026) EVEREST:Endogenous Vision-Language Reinforcement Reasoning Exploration for Urban Socio-Semantic Segmentation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.24640)

(24 Aug 2026) AffectOmni: RL-Verifiable People-Centric Grounded Affective Reasoning for Social and Art-Related Scenes [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.26193)

(24 Aug 2026) CaRGo-T: Causal Reasoning Graph-of-Thought improves Multimodal Humor Comprehension [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.23172)

(24 Aug 2026) LG-GER: Language-Guided Group Emotion Recognition via Multimodal Evidence Distillation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.23880)

(23 Aug 2026) Think with Structured Grounding: Perceptual Reinforcement Learning for Chart and Visual-Tabular Understanding [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.22429)

(23 Aug 2026) UR$^{2}$-MLLM: Uncertainty-aware Revisit Reasoning in Multimodal Large Language Models for Radiology Report Generation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.22217)

(23 Aug 2026) LiST: Local-Simplex Test-Time LoRA Fusion [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.22370)

(22 Aug 2026) Hints, Critics, and Teachers: Prior Injection for Sparse-Reward RL in Vision-Language Math Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.21811)

(22 Aug 2026) VIG: Visual Information Gain as a Reward Signal for Multimodal Chain-of-Thought Compression [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.21883)

(21 Aug 2026) Re$^3$Cap: Retrieval-Guided Refinement for Image Captioning Enhancement via Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.21305)

(21 Aug 2026) ReFrame: Evidence-Guided Test-Time Safety Alignment in Multimodal Large Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.21100)

(21 Aug 2026) Is Visual Prompting All You Need? Studying VLM Spatial Reasoning under Progressive Visual Scaffolds [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.21170)

(21 Aug 2026) Latent Ordinal Evidence, Misaligned Outputs: Inference-Time Ordinal Lens Alignment for Multimodal LLMs [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.20999)

(20 Aug 2026) ArmorOCR: Grounded Adversarial Visual Perception via Observation-Transferred Self-Distillation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.20122)

(20 Aug 2026) Evidence-Gated Task and Motion Planning with Vision-Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.20084)

(20 Aug 2026) Rule-Compliant Visual Spatial Planning for Multimodal Large Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.20237)

(20 Aug 2026) G-CARL: Grounded Checklist-Aligned Reward Learning for Patient-Oriented Medical Report Interpretation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.20331)

(20 Aug 2026) PEA-DPO: Perception-Enhanced Alignment Direct Preference Optimization for MLLMs Alignment [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.19598)

(20 Aug 2026) Question-Guided Evidence Acquisition for Multimodal Visual Question Answering [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.19739)

(20 Aug 2026) Answer-Level Trust Selection for Physical Vision-Language Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.19807)

(20 Aug 2026) Towards Clinically Faithful Medical Image Captioning via Enhanced Vision-Language Alignment [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.19825)

(19 Aug 2026) UMER: Unifying Embedding and Ranking via Pair-Aware Discriminative Reasoning for Universal Multimodal Retrieval [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.18504)

(19 Aug 2026) PCQA-R1: Advancing Generalized 3D Point Cloud Quality Assessment with Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.18627)

(19 Aug 2026) Can a Lightweight Multimodal Model Estimate LLM Reasoning Performance? A Study for Compute-Optimal Document Inference [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.18591)

(19 Aug 2026) Clinically Structured Surrogate Rewards for Post-SFT Medical Image Captioning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.18654)

(19 Aug 2026) COSTA: A Cluster-Centric Paradigm for Annotation-Free Open-Set Semantic Segmentation of Aerial Point Clouds with Domain Shifts [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.18479)

(19 Aug 2026) DynCur-Geo: Dynamic Curiosity Reward Shaping for Multimodal Active Geo-Localization [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.18673)

(19 Aug 2026) GRACE: Grounded Reasoning via Adapter Composition and Evidence-Aware Calibration for Educational Visual Question Answering [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.19355)

(18 Aug 2026) Integrating Novelty and Surprise for Experience Prioritization and Exploration in Image-Based Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.17373)

(18 Aug 2026) PathoArgus: Advancing Evidence-Grounded Long-Context Visual Reasoning across Gigapixel Whole-Slide and Multi-Slide Case Contexts [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.17607)

(17 Aug 2026) Interactive Whole Slide Images for RL-based Tumour Segmentation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.16607)

(17 Aug 2026) Q-Learning With World Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.17163)

(17 Aug 2026) Lymphocyte Mimicry Correction via Region-Level Tissue Reasoning and Unbalanced Optimal Transport [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.17151)

(17 Aug 2026) Boosting Knowledge-based Visual Question Answering with Structured Context Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.21431)

(16 Aug 2026) SEER: Long-Context Reasoning via Selective Visual-Text Compression [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.15962)

(15 Aug 2026) MetaReason: Precise Interleaved Multimodal Reasoning via Editing Meta Information for Solving Geometry Problems [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.15006)

(15 Aug 2026) Risk-Adaptive Edge--Cloud Visual Reasoning for Communication-Efficient Autonomous Driving [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.14991)

(15 Aug 2026) Physiological World Models for Human State Transitions [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.15309)

(14 Aug 2026) Self-Supervised Visual On-Policy Distillation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.14144)

(14 Aug 2026) Test-Time Instance Selection for Improved Whole Slide Image Analysis [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.14759)

(14 Aug 2026) SPARGen: Unifying Spatial Perception and Reasoning through Native Multimodal Generation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.14138)

(13 Aug 2026) Beyond Correctness: Benchmarking and Aligning Response Behaviors in Hybrid-Thinking MLLMs [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.12781)

(13 Aug 2026) LongEarth-R1: Benchmarking and Aligning Vision-Language Models for Long-Horizon Earth Observation Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.13344)

(11 Aug 2026) ThinkAfford: Affordance-Centric Reasoning for Fine-Grained 3D Grounding in Cluttered Scenes [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.10981)

(11 Aug 2026) CARE: Confidence-Aware Reasoning for Reliable Medical VQA [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.10964)

(10 Aug 2026) ADOPD: Reference-Privileged On-Policy Distillation for MLLM-Based Industrial Anomaly Detection [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.09789)

(10 Aug 2026) Chain of Spatial Thoughts: Modality-Agnostic Spatial Grounding for Vision Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.10278)

(10 Aug 2026) FactorDrive: Adaptive Multi-Step Reasoning Driven by Planning-Critical Factors for End-to-End Autonomous Driving [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.09591)

(09 Aug 2026) Improving Generalization Robustness of Multimodal RLVR [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.08802)

(08 Aug 2026) Evidence-RL: Towards Evidence-intensive Visual Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.08021)

(08 Aug 2026) PhysX-CoT: Structured Physical Reasoning from a Single Image to Simulation-Ready 3D Assets [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.08053)

(08 Aug 2026) StructReward: Efficient Structured Process Rewards for Self-Correcting Multimodal Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.08326)

(06 Aug 2026) Learning from Failures: Retrieval-Centric CoT via Hard Negatives for Unified Multimodal Retrieval [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.06060)

(06 Aug 2026) WebGrader: Training LLMs for Web Development with Self-Evolving Programmatic Grader [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.06474)

(05 Aug 2026) Teaching MLLMs to Say No: Generalized Referring Expression Comprehension via Refusal Calibrated GRPO [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.04698)

(05 Aug 2026) Multi-Branch Policy Optimization for Multimodal Large Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.07581)

(05 Aug 2026) ReGround: Restoring Visual Grounding in Multi-Step Reasoning through Self-Diagnosis and Visual Re-Examination [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.04385)

(05 Aug 2026) Trace, Verify, and Correct: A Training-Free Framework for Spatial Reasoning in Multimodal LLMs [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.04759)

(05 Aug 2026) OPD-V: Visual On-Policy Self-Distillation with Modality Balance [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.05131)

(04 Aug 2026) Aligning Large Vision-Language Models at Test Time: A Trajectory-Guided Structured Sampling Approach [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.03204)

(04 Aug 2026) Taming the Implicit: Dual-Channel Risk-Aware Reinforcement Fine-Tuning for Continual Multimodal Post-Training [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.03660)

(04 Aug 2026) Enhancing VLM Reward Models Through Structure-Aware Fine-Tuning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.03875)

(04 Aug 2026) CARE-X: Towards Clinically Useful Radiology VLMs with Auxiliary Supervision, Reward-Aligned Learning, and Tool-Augmented Measurement [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.03890)

(04 Aug 2026) DocTrace: Towards Traceable Long Document VQA via Hierarchical Evidence Graph Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.03292)

(04 Aug 2026) Monte Carlo Tree Search for Table-to-Multimodal Report Generation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.04071)

(04 Aug 2026) TriCLE: Tri-Modal Vision-Language Reasoning for Edge-Deployed Fine-Grained Clustering [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.04175)

(03 Aug 2026) Deferred Exposure of Future Trajectories for Verifiable Reasoning in Autonomous Driving VLMs [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.01755)

(03 Aug 2026) VC-Tooler: Learning Compositional and Adaptive Visual Tool Use [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.02217)

(03 Aug 2026) SpatialQuery: Benchmarking Geometry-Grounded Multi-Instance Spatial Reasoning in Vision-Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.01709)

(03 Aug 2026) Local Margin Restoration for Test-Time Adaptation of Vision-Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.02216)

(03 Aug 2026) MoRAL: Sensor-Grounded BEV Reasoning for Compact VLMs toward Edge-Oriented Autonomous Driving [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.02449)

(03 Aug 2026) CURV: Enhancing Chart Understanding Through Curriculum Visual Grounded Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.02833)

(02 Aug 2026) It's the Decoding Format, Not the Perturbation: Auditing Consistency-Based Selection for Vision-Language Test-Time Scaling [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.01207)

(02 Aug 2026) Remember-R1: Mitigating Long-Context Visual Forgetting through Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.01314)

(02 Aug 2026) Distill What the Student Can See: Fisher-Projected On-Policy Distillation for Vision-Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.01263)

(31 Jul 2026) Distill What RGB Can Recover: Privileged 3D Evidence for RGB-Only Vision-Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2608.00110)

(30 Jul 2026) Can Vision-Language Models Reason about AI Edits in Images? [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.28464)

(29 Jul 2026) FAS-R1: A Unified Multi-Task MLLM for Reasoning Face Anti-Spoofing [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.26432)

(27 Jul 2026) Reasoning to Regulate: Chain-of-Thought for Traffic Rule Understanding [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.24199)

(26 Jul 2026) Offline-Online Curriculum RL for Multimodal Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.23700)

(26 Jul 2026) PathScale-R1: Cross-scale Reasoning for Pathological Image Analysis [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.23794)

(25 Jul 2026) Self-Boosting Vision-Language Models with Noisy Student On-Policy Self-Distillation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.23125)

(24 Jul 2026) Visual Saliency Steering Distillation for Multimodal Chain-of-Thought Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.22013)

(23 Jul 2026) Visual Contrastive Self-Distillation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.21556)

(23 Jul 2026) Be Consistent! Enhancing Robust Visual Reasoning in LVLMs with Consistency Constraints [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.21722)

(22 Jul 2026) Trace: A Taxonomy-Guided Environment for Multidomain Visual Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.19790)

(21 Jul 2026) DobicVLM: Aligning Chest X-Ray Report Generation with Clinically-Grounded Programmatic Rewards via Group Relative Policy Optimization [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.18988)

(21 Jul 2026) Cognitive Dual-Process Planning for Autonomous Driving with Structured Scene Knowledge and Verifiable Reasoning-Action Consistency [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.19194)

(19 Jul 2026) LenGuard-GPC: Length Guarding with Guided-Prompt Consistency for Spatial Reasoning Reinforce Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.17243)

(18 Jul 2026) FUSAR-R1: A Large-Scale Reasoning Model for Intelligent Interpretation of SAR Images [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.16819)

(17 Jul 2026) IoU-PD: IoU-Aware Privileged Distillation for Visual Grounding with Multimodal Large Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.15732)

(17 Jul 2026) ToolSciVer: Multimodal Scientific Claim Verification with Visual Tool Augmented Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.16131)

(17 Jul 2026) WeedExpert-R1: Incentivizing Botanical Reasoning in MLLMs with Reinforcement Learning for Precision Weed Grounding [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.16492)

(16 Jul 2026) Stop Thinking, Start Looking: Efficient Post-Training for Multimodal Document Question Answering via Reasoning-Free Alignment [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.14682)

(15 Jul 2026) SIVA-RL: Sensitivity-Invariance Visual Alignment for Multimodal Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.13931)

(15 Jul 2026) SD-MAR: Multi-image Analytical Reasoning via Synthetic Data and Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.14333)

(14 Jul 2026) UniVR: Thinking in Visual Space for Unified Visual Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.12800)

(14 Jul 2026) Visual Access Boundaries in Vision-Language Model Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.12815)

(13 Jul 2026) SVR-R1: Bootstrapping Multi-modal Reasoning with Self-verification in Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.10966)

(12 Jul 2026) Answer-Conditioned Chain-of-Thought Distillation for Few-Shot Industrial Vision with Small VLMs [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.10666)

(12 Jul 2026) When RLVR Shrinks the Reasoning Boundary: Diagnosing Pass@k Inversion [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.20543)

(10 Jul 2026) Multimodal Reward Hacking in Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.09492)

(08 Jul 2026) BUS: Brain-Inspired Unsupervised Self-Reflection via Backward Prediction for Multimodal Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.07361)

(07 Jul 2026) Progressive Reasoning with Primitive Correction for Compositional Zero-Shot Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.05911)

(05 Jul 2026) RL Forgets! Towards Continual Policy Optimization [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.04364)

(02 Jul 2026) Visually Grounded Self-Reflection for Vision-Language Models via Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.02490)

(02 Jul 2026) DetailAnywhere: Fashion Detail Generation via Cross-Modal Feature Alignment Distillation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.02220)

(01 Jul 2026) VLM-AR3L: Vision-Language Models for Absolute and Relative Rewards in Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.00483)

(01 Jul 2026) GeoSearcher: Anchor-Guided Progressive Reasoning for Remote Sensing Visual Grounding with Process Supervision [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.01050)

(01 Jul 2026) Perceive-to-Reason: Decoupling Perception and Reasoning for Fine-Grained Visual Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.01191)

(01 Jul 2026) Selective Test-Time Debiasing for CLIP via Reward Gating [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.00423)

(01 Jul 2026) ReShift: Aha-Moment-Driven Reasoning-Level Backdoor Attacks on Vision-Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.00361)

(01 Jul 2026) DART-VLN: Test-Time Memory Decay and Anti-Loop Regularization for Discrete Vision-Language Navigation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.01043)

(01 Jul 2026) ESC: Emotional Self-Correction for Reliable Vision-Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.02089)

(01 Jul 2026) H-OPD: Confidence Aware Heterogeneous Multi-Teacher Multimodal On-policy Distillation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2607.02592)

(24 Jun 2026) V-Zero: Answer-Label-Free On-Policy Distillation with Contrastive Evidence Gating for Fine-Grained Visual Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.25319)

(23 Jun 2026) PointVG-R: Internalizing Geometric Reasoning in MLLMs for Precise Pointing Localization via Visual Chain of Thought [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.24539)

(22 Jun 2026) CFPO: Counterfactual Policy Optimization for Multimodal Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.23206)

(22 Jun 2026) VeriEvol: Scaling Multimodal Mathematical Reasoning via Verifiable Evol-Instruct [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.23543)

(22 Jun 2026) Dense Reward for Multi-View 3D Reasoning with Global Maps and Local Views [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.23557)

(22 Jun 2026) AIR: Adaptive Interleaved Reasoning with Code in MLLMs [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.23678)

(18 Jun 2026) SPOT-E: Test-Time Entropy Shaping with Visual Spotlights for Frozen VLMs [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.20244)

(16 Jun 2026) Enhancing Pathological VLMs with Cross-scale Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.17412)

(16 Jun 2026) Reinforcing Dual-Path Reasoning in Spatial Vision Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.17539)

(16 Jun 2026) See First, Answer Later: Visual Evidence Pre-Alignment via Sufficiency-Driven RL [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.17678)

(15 Jun 2026) Thinking with Visual Grounding [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.16122)

(15 Jun 2026) DifferAD-R1: A Difference-Guided IndustrialAnomaly Localization with Multimodal LargeLanguage Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.16601)

(14 Jun 2026) NeRD: Neuro-Symbolic Rule Distillation for Efficient Ontology-Grounded Chain-of-Thought in Medical Image Diagnosis [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.15617)

(14 Jun 2026) Self-Questioning Vision-Language Models: Reinforcement Learning for Compositional Visual Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.15651)

(14 Jun 2026) SciOrch: Learning to Orchestrate Expert LLMs for Solving Frontier Multimodal Scientific Reasoning Tasks [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.15872)

(13 Jun 2026) Reinforcement Learning-Guided Retrieval with Soft Fusion for Robust Multimodal Imitation Learning under Missing Modalities [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.15514)

(12 Jun 2026) CORA: Analyzing and bridging thinking-answer gap in Multimodal RLVR via Consistency-Oriented Reasoning Alignment [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.14691)

(11 Jun 2026) Iterative Visual Thinking and the Self-Correction Mirage in VLM Grounding [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.13156)

(09 Jun 2026) Self-Distillation Policy Optimization via Visual Feedback: Bridging Code and Visual Artifacts [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.10334)

(08 Jun 2026) CRANE: Knowledge Editing for Reasoning MLLMs [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.09033)

(08 Jun 2026) Stabilizing On-Policy Distillation for MLLM Reasoning with Global Normalization [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.09091)

(06 Jun 2026) DyCo-RL: Dynamic Cross-Modal Coordination for Visual Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.08035)

(05 Jun 2026) Teaching the Way, Not the Answer: Privileged Tutoring Distillation for Multimodal Policy Optimization [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.07000)

(03 Jun 2026) Hyper-ICL: Attention Calibration with Hyperbolic Anchor Distillation for Multimodal In-Context Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.04434)

(03 Jun 2026) Food-R1: A Unified Multi-Task Food Vision-Language Model with Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.04986)

(02 Jun 2026) Entropy Is Not Enough: Unlocking Effective Reinforcement Learning for Visual Reasoning via Vision-Anchored Token Selection [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.03937)

(02 Jun 2026) Imaginative Perception Tokens Enhance Spatial Reasoning in Multimodal Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.03988)

(02 Jun 2026) SD-GRPO: Verifiable Segment Decomposition for Long-Form Vision-Language Generation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2606.09871)

(19 May 2026) From Seeing to Thinking: Decoupling Perception and Reasoning Improves Post-Training of Vision-Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.20177)

(19 May 2026) JUDO: A Juxtaposed Domain-Oriented Multimodal Reasoner for Industrial Anomaly QA [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.20284)

(18 May 2026) Vision-OPD: Learning to See Fine Details for Multimodal LLMs via On-Policy Self-Distillation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.18740)

(18 May 2026) IVR-R1: Refining Trajectories through Iterative Visual-Grounded Reasoning in Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.23997)

(17 May 2026) Reasoning Portability: Guiding Continual Learning for MLLMs in the RLVR Era [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.18903)

(16 May 2026) HEED: Density-Weighted Residual Alignment for Hybrid Vision-Language Model Distillation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.17093)

(14 May 2026) Think When Needed: Adaptive Reasoning-Driven Multimodal Embeddings with a Dual-LoRA Architecture [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.14448)

(13 May 2026) PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.13467)

(13 May 2026) Physics-R1: An Audited Olympiad Corpus and Recipe for Visual Physics Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.14040)

(13 May 2026) Multilingual OCR-Aware Fine-Tuning and Prompt-Guided Chain-of-Thought Reasoning for Multimodal Large Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.16409)

(12 May 2026) OmniThoughtVis: A Scalable Distillation Pipeline for Deployable Multimodal Reasoning Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.11629)

(12 May 2026) Composition of Memory Experts for Diffusion World Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.18813)

(10 May 2026) Reinforcing Multimodal Reasoning Against Visual Degradation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.09262)

(10 May 2026) DeltaRubric: Generative Multimodal Reward Modeling via Joint Planning and Verification [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.09269)

(10 May 2026) Reflection Anchors for Propagation-Aware Visual Retention in Long-Chain Multimodal Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.09614)

(10 May 2026) Overcoming Catastrophic Forgetting in Visual Continual Learning with Reinforcement Fine-Tuning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.09640)

(10 May 2026) Distilling 3D Spatial Reasoning into a Lightweight Vision-Language Model with CoT [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.09719)

(08 May 2026) BalCapRL: A Balanced Framework for RL-Based MLLM Image Captioning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.07394)

(08 May 2026) GazeVLM: Active Vision via Internal Attention Control for Multimodal Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.07817)

(04 May 2026) Enhancing Multimodal In-Context Learning via Inductive-Deductive Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.02378)

(03 May 2026) Chart-FR1: Visual Focus-Driven Fine-Grained Reasoning on Dense Charts [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.01882)

(02 May 2026) Injecting Distributional Awareness into MLLMs via Reinforcement Learning for Deep Imbalanced Regression [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.01402)

(01 May 2026) Structured Role-Aware Policy Optimization for Multimodal Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.07274)

(01 May 2026) MIRL: Mutual Information-Guided Reinforcement Learning for Vision-Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2605.01520)

(30 Apr 2026) VeraRetouch: A Lightweight Fully Differentiable Framework for Multi-Task Reasoning Photo Retouching [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.27375)

(30 Apr 2026) Beyond SFT-to-RL: Pre-alignment via Black-Box On-Policy Distillation for Multimodal RL [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.28123)

(30 Apr 2026) WaferSAGE: Large Language Model-Powered Wafer Defect Analysis via Synthetic Data Generation and Rubric-Guided Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.27629)

(30 Apr 2026) Detecting is Easy, Adapting is Hard: Local Expert Growth for Visual Model-Based Reinforcement Learning under Distribution Shift [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.27411)

(30 Apr 2026) PRTS: A Primitive Reasoning and Tasking System via Contrastive Representations [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.27472)

(30 Apr 2026) The Effects of Visual Priming on Cooperative Behavior in Vision-Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.27953)

(29 Apr 2026) World2VLM: Distilling World Model Imagination into VLMs for Dynamic Spatial Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.26934)

(29 Apr 2026) Beyond Shortcuts: Mitigating Visual Illusions in Frozen VLMs via Qualitative Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.26250)

(29 Apr 2026) Multiple Consistent 2D-3D Mappings for Robust Zero-Shot 3D Visual Grounding [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.26261)

(28 Apr 2026) Instruction-Evidence Contrastive Dual-Stream Decoding for Grounded Vision-Language Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.25809)

(28 Apr 2026) SIEVES: Selective Prediction Generalizes through Visual Evidence Scoring [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.25855)

(27 Apr 2026) Improving Vision-language Models with Perception-centric Process Reward Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.24583)

(27 Apr 2026) See Further, Think Deeper: Advancing VLM's Reasoning Ability with Low-level Visual Cues and Reflection [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.24339)

(27 Apr 2026) PhysNote: Self-Knowledge Notes for Evolvable Physical Reasoning in Vision-Language Model [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.24443)

(27 Apr 2026) VLM-VPI: A Vision-Language Reasoning Framework for Improving Automated Vehicle-Pedestrian Interactions [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.23934)

(13 Apr 2026) POINTS-Long: Adaptive Dual-Mode Visual Reasoning in MLLMs [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.11627v1)

(13 Apr 2026) CFMS: A Coarse-to-Fine Multimodal Synthesis Framework for Enhanced Tabular Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.10973v1)

(13 Apr 2026) Test-time Scaling over Perception: Resolving the Grounding Paradox in Thinking with Images [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.11025v1)

(10 Apr 2026) VL-Calibration: Decoupled Confidence Calibration for Large Vision-Language Models Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.09529v1)

(10 Apr 2026) Visually-Guided Policy Optimization for Multimodal Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.09349v1)

(09 Apr 2026) Towards Responsible Multimodal Medical Reasoning via Context-Aligned Vision-Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.08815v1)

(09 Apr 2026) TeamLLM: Exploring the Capabilities of LLMs for Multimodal Group Interaction Prediction [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.08771v1)

(09 Apr 2026) OpenVLThinkerV2: A Generalist Multimodal Reasoning Model for Multi-domain Visual Tasks [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.08539v1)

(09 Apr 2026) Fundus-R1: Training a Fundus-Reading MLLM with Knowledge-Aware Reasoning on Public Data [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.08322v1)

(09 Apr 2026) WorldMAP: Bootstrapping Vision-Language Navigation Trajectory Prediction with Generative World Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.07957v1)

(09 Apr 2026) AgriChain Visually Grounded Expert Verified Reasoning for Interpretable Agricultural Vision Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.07814v1)

(08 Apr 2026) Enhancing MLLM Spatial Understanding via Active 3D Scene Exploration for Multi-Perspective Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.06725v1)

(07 Apr 2026) MMEmb-R1: Reasoning-Enhanced Multimodal Embedding with Pair-Aware Selection and Adaptive Control [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.06156v1)

(07 Apr 2026) WikiSeeker: Rethinking the Role of Vision-Language Models in Knowledge-Based Visual Question Answering [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.05818v2)

(07 Apr 2026) Multi-Granularity Reasoning for Image Quality Assessment via Attribute-Aware Reinforcement Learning to Rank [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.09704v1)

(06 Apr 2026) Saliency-R1: Enforcing Interpretable and Faithful Vision-language Reasoning via Saliency-map Alignment Reward [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.04500v1)

(05 Apr 2026) Belief-Aware VLM Model for Human-like Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.09686v1)

(03 Apr 2026) Understanding the Role of Hallucination in Reinforcement Post-Training of Multimodal Reasoning Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.03179v1)

(03 Apr 2026) Chart-RL: Policy Optimization Reinforcement Learning for Enhanced Visual Reasoning in Chart Question Answering with Vision Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.03157v1)

(03 Apr 2026) CharTool: Tool-Integrated Visual Reasoning for Chart Understanding [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.02794v1)

(03 Apr 2026) FSUNav: A Cerebrum-Cerebellum Architecture for Fast, Safe, and Universal Zero-Shot Goal-Oriented Navigation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.03139v1)

(02 Apr 2026) Guideline2Graph: Profile-Aware Multimodal Parsing for Executable Clinical Decision Graphs [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.02477v1)

(02 Apr 2026) Impact of Multimodal and Conversational AI on Learning Outcomes and Experience [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.02221v1)

(02 Apr 2026) Not All Tokens See Equally: Perception-Grounded Policy Optimization for Large Vision-Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.01840v2)

(02 Apr 2026) MM-ReCoder: Advancing Chart-to-Code Generation with Reinforcement Learning and Self-Correction [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.01600v1)

(01 Apr 2026) Vero: An Open RL Recipe for General Visual Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.04917)

(01 Apr 2026) Rethinking Reinforcement Fine-Tuning in LVLM: Convergence, Reward Decomposition, and Generalization [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.19857)

(01 Apr 2026) EgoMind: Activating Spatial Cognition through Linguistic Reasoning in MLLMs [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.03318v1)

(01 Apr 2026) All Roads Lead to Rome: Incentivizing Divergent Thinking in Vision-Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.00479v1)

(30 Mar 2026) Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.28618v2)

(30 Mar 2026) MedLoc-R1: Performance-Aware Curriculum Reward Scheduling for GRPO-Based Medical Visual Grounding [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.28120v1)

(30 Mar 2026) $AutoDrive\text{-}P^3$: Unified Chain of Perception-Prediction-Planning Thought via Reinforcement Fine-Tuning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.28116v1)

(29 Mar 2026) LVRPO: Language-Visual Alignment with GRPO for Multimodal Understanding and Generation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.27693v1)

(29 Mar 2026) Learning to Focus and Precise Cropping: A Reinforcement Learning Framework with Information Gaps and Grounding Loss for MLLMs [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.27494v2)

(28 Mar 2026) Bridging Visual Representation and Reinforcement Learning from Verifiable Rewards in Large Vision-Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.27375v1)

(28 Mar 2026) Understanding and Mitigating Hallucinations in Multimodal Chain-of-Thought Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.27201v1)

(27 Mar 2026) Beyond Where to Look: Trajectory-Guided Reinforcement Learning for Multimodal RLVR [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.26126v1)

(26 Mar 2026) R-C2: Cycle-Consistent Reinforcement Learning Improves Multimodal Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.25720v1)

(26 Mar 2026) Bridging Perception and Reasoning: Token Reweighting for RLVR in Multimodal LLMs [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.25077v1)

(24 Mar 2026) MedCausalX: Adaptive Causal Reasoning with Self-Reflection for Trustworthy Medical Vision-Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.23085v1)

(24 Mar 2026) Rethinking Token-Level Policy Optimization for Multimodal Chain-of-Thought [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.22847v1)

(24 Mar 2026) GeoTikzBridge: Advancing Multimodal Code Generation for Geometric Perception and Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.22687v2)

(23 Mar 2026) Getting to the Point: Why Pointing Improves LVLMs [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.21746v1)

(23 Mar 2026) Rethinking Token Reduction for Large Vision-Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.21701v1)

(21 Mar 2026) Attention in Space: Functional Roles of VLM Heads for Spatial Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.20662v1)

(20 Mar 2026) One Model, Two Minds: Task-Conditioned Reasoning for Unified Image Quality and Aesthetic Assessment [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.19779v1)

(19 Mar 2026) Balanced Thinking: Improving Chain of Thought Training in Vision Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.18656v1)

(19 Mar 2026) TerraScope: Pixel-Grounded Visual Reasoning for Earth Observation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.19039v1)

(17 Mar 2026) HopChain: Multi-Hop Data Synthesis for Generalizable Vision-Language Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.17024v2)

(17 Mar 2026) DreamPlan: Efficient Reinforcement Fine-Tuning of Vision-Language Planners via Video World Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.16860v1)

(17 Mar 2026) The Cost of Reasoning: Chain-of-Thought Induces Overconfidence in Vision-Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.16728v1)

(17 Mar 2026) Reliable Reasoning in SVG-LLMs via Multi-Task Multi-Reward Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.16189v1)

(16 Mar 2026) Molecular Identifier Visual Prompt and Verifiable Reinforcement Learning for Chemical Reaction Diagram Parsing [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.15011v2)

(15 Mar 2026) On the Nature of Attention Sink that Shapes Decoding Strategy in MLLMs [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.14337v1)

(14 Mar 2026) Improving Visual Reasoning with Iterative Evidence Refinement [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.14117v1)

(12 Mar 2026) Surg-R1: A Hierarchical Reasoning Foundation Model for Scalable and Interpretable Surgical Decision Support with Multi-Center Clinical Validation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.12430v1)

(10 Mar 2026) C2F-Thinker: Coarse-to-Fine Reasoning with Hint-Guided Reinforcement Learning for Multimodal Sentiment Analysis [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2604.00013v2)

(10 Mar 2026) MORE-R1: Guiding LVLM for Multimodal Object-Entity Relation Extraction via Stepwise Reasoning with Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.09478v1)

(10 Mar 2026) GeoSolver: Scaling Test-Time Reasoning in Remote Sensing with Fine-Grained Process Supervision [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.09551v1)

(09 Mar 2026) MJ1: Multimodal Judgment via Grounded Verification [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.07990v2)

(08 Mar 2026) Med-Evo: Test-time Self-evolution for Medical Multimodal Large Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.07443v1)

(08 Mar 2026) Overthinking Causes Hallucination: Tracing Confounder Propagation in Vision Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.07619v2)

(07 Mar 2026) Perception-Aware Multimodal Spatial Reasoning from Monocular Images [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.06985v1)

(06 Mar 2026) MLLMRec-R1: Incentivizing Reasoning Capability in Large Language Models for Multimodal Sequential Recommendation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.06243v1)

(06 Mar 2026) PatchCue: Enhancing Vision-Language Model Reasoning with Patch-Based Visual Cues [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.05869v2)

(06 Mar 2026) ViewFusion: Structured Spatial Thinking Chains for Multi-View Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.06024v1)

(05 Mar 2026) Wiki-R1: Incentivizing Multimodal Reasoning for Knowledge-based VQA via Data and Sampling Curriculum [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.05256v1)

(04 Mar 2026) Phi-4-reasoning-vision-15B Technical Report [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.03975v1)

(04 Mar 2026) Discriminative Perception via Anchored Description for Reasoning Segmentation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.04002v1)

(03 Mar 2026) TRACE: Task-Adaptive Reasoning and Representation Learning for Universal Multimodal Retrieval [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.02929v2)

(03 Mar 2026) SaFeR-ToolKit: Structured Reasoning via Virtual Tool Calling for Multimodal Safety [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.02635v1)

(02 Mar 2026) Better Eyes, Better Thoughts: Why Vision Chain-of-Thought Fails in Medicine [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.06665v2)

(01 Mar 2026) Can Thinking Models Think to Detect Hateful Memes? [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.01225v1)

(01 Mar 2026) ClinCoT: Clinical-Aware Visual Chain-of-Thought for Medical Vision Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.01124v1)

(01 Mar 2026) DIVA-GRPO: Enhancing Multimodal Reasoning through Difficulty-Adaptive Variant Advantage [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.01106v1)

(01 Mar 2026) ICPRL: Acquiring Physical Intuition from Interactive Control [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.13295v1)

(28 Feb 2026) PaLMR: Towards Faithful Visual Reasoning via Multimodal Process Alignment [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2603.06652v1)

(27 Feb 2026) Thinking with Images as Continuous Actions: Numerical Visual Chain-of-Thought [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.23959v1)

(27 Feb 2026) EMO-R3: Reflective Reinforcement Learning for Emotional Reasoning in Multimodal Large Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.23802v1)

(27 Feb 2026) Annotation-Free Visual Reasoning for High-Resolution Large Multimodal Models via Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.23615v2)

(27 Feb 2026) Toward Guarantees for Clinical Reasoning in Vision Language Models via Formal Verification [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.24111v1)

(27 Feb 2026) Reasoning-Driven Multimodal LLM for Domain Generalization [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.23777v1)

(26 Feb 2026) MediX-R1: Open Ended Medical Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.23363v1)

(25 Feb 2026) MindDriver: Introducing Progressive Multimodal Reasoning for Autonomous Driving [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.21952v1)

(25 Feb 2026) See It, Say It, Sorted: An Iterative Training-Free Framework for Visually-Grounded Multimodal Reasoning in LVLMs [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.21497v2)

(25 Feb 2026) RuCL: Stratified Rubric-Based Curriculum Learning for Multimodal Large Language Model Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.21628v2)

(24 Feb 2026) Synergizing Understanding and Generation with Interleaved Analyzing-Drafting Thinking [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.21435v2)

(23 Feb 2026) TextShield-R1: Reinforced Reasoning for Tampered Text Detection [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.19828v1)

(23 Feb 2026) Circuit Tracing in Vision-Language Models: Understanding the Internal Mechanisms of Multimodal Thinking [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.20330v1)

(19 Feb 2026) Enabling Training-Free Text-Based Remote Sensing Segmentation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.17799v1)

(18 Feb 2026) Saliency-Aware Multi-Route Thinking: Revisiting Vision-Language Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.16702v1)

(17 Feb 2026) Can Vision-Language Models See Squares? Text-Recognition Mediates Spatial Reasoning Across Three Model Families [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.15950v2)

(17 Feb 2026) On the Out-of-Distribution Generalization of Reasoning in Multimodal LLMs for Simple Visual Planning Tasks [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.15460v1)

(16 Feb 2026) Diagnosing Knowledge Conflict in Multimodal Long-Chain Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.14518v1)

(16 Feb 2026) TikArt: Stabilizing Aperture-Guided Fine-Grained Visual Reasoning with Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.14482v2)

(15 Feb 2026) ForgeryVCR: Visual-Centric Reasoning via Efficient Forensic Tools in MLLMs for Image Forgery Detection and Localization [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.14098v1)

(15 Feb 2026) GeoEyes: On-Demand Visual Focusing for Evidence-Grounded Understanding of Ultra-High-Resolution Remote Sensing Imagery [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.14201v2)

(14 Feb 2026) Embed-RL: Reinforcement Learning for Reasoning-Driven Multimodal Embeddings [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.13823v3)

(13 Feb 2026) Reliable Thinking with Images [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.12916v2)

(13 Feb 2026) Thinking Like a Radiologist: A Dataset for Anatomy-Guided Interleaved Vision Language Reasoning in Chest X-ray Interpretation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.12843v1)

(12 Feb 2026) Credit Where It is Due: Cross-Modality Connectivity Drives Precise Reinforcement Learning for MLLM Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.11455v1)

(11 Feb 2026) Canvas-of-Thought: Grounding Reasoning via Mutable Structured States [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.10494v1)

(10 Feb 2026) Bridging Efficiency and Transparency: Explainable CoT Compression in Multimodal Large Reasoning Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.09485v1)

(10 Feb 2026) Visual Para-Thinker: Divide-and-Conquer Reasoning for Visual Comprehension [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.13310v1)

(10 Feb 2026) GenSeg-R1: RL-Driven Vision-Language Grounding for Fine-Grained Referring Segmentation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.09701v1)

(09 Feb 2026) AnomSeer: Reinforcing Multimodal LLMs to Reason for Time-Series Anomaly Detection [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.08868v1)

(09 Feb 2026) Do MLLMs Really See It: Reinforcing Visual Attention in Multimodal LLMs [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.08241v1)

(09 Feb 2026) When and How Much to Imagine: Adaptive Test-Time Scaling with World Models for Visual Spatial Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.08236v1)

(07 Feb 2026) Fine-R1: Make Multi-modal LLMs Excel in Fine-Grained Visual Recognition by Chain-of-Thought Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.07605v2)

(06 Feb 2026) MedMO: Grounding and Understanding Multimodal Large Language Model for Medical Images [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.06965v2)

(06 Feb 2026) SPARC: Separating Perception And Reasoning Circuits for Test-time Scaling of VLMs [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.06566v2)

(05 Feb 2026) Length-Unbiased Sequence Policy Optimization: Revealing and Controlling Response Length Variation in RLVR [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.05261v1)

(05 Feb 2026) Predicting Camera Pose from Perspective Descriptions for Spatial Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.06041v2)

(04 Feb 2026) Guided Verifier: Collaborative Multimodal Reasoning via Dynamic Process Supervision [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.04290v1)

(04 Feb 2026) Training Data Efficiency in Multimodal Process Reward Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.04145v2)

(03 Feb 2026) Decoupling Skeleton and Flesh: Efficient Multimodal Table Reasoning with Disentangled Alignment and Structure-aware Guidance [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.03491v1)

(02 Feb 2026) Thinking with Comics: Enhancing Multimodal Reasoning through Structured Visual Storytelling [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.02453v2)

(02 Feb 2026) VLM-Guided Experience Replay [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.01915v1)

(02 Feb 2026) ClueTracer: Question-to-Vision Clue Tracing for Training-Free Hallucination Suppression in Multimodal Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.02004v1)

(02 Feb 2026) Multimodal Large Language Models for Real-Time Situated Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.01880v1)

(01 Feb 2026) StreamVLA: Breaking the Reason-Act Cycle via Completion-State Gating [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.01100v2)

(01 Feb 2026) Med3D-R1: Incentivizing Clinical Reasoning in 3D Medical Vision-Language Models for Abnormality Diagnosis [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.01200v1)

(01 Feb 2026) SRVAU-R1: Enhancing Video Anomaly Understanding via Reflection-Aware Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.01004v1)

(31 Jan 2026) RGBX-R1: Visual Modality Chain-of-Thought Guided Reinforcement Learning for Multimodal Grounding [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2602.00504v1)

(29 Jan 2026) MMFineReason: Closing the Multimodal Reasoning Gap via Open Data-Centric Methods [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2601.21821v1)

(28 Jan 2026) MARE: Multimodal Alignment and Reinforcement for Explainable Deepfake Detection via Vision-Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2601.20433v3)

(27 Jan 2026) Innovator-VL: A Multimodal Large Language Model for Scientific Discovery [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2601.19325v1)

(26 Jan 2026) AdaReasoner: Dynamic Tool Orchestration for Iterative Visual Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2601.18631v2)

(22 Jan 2026) Explainable Deepfake Detection with RL Enhanced Self-Blended Images [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2601.15624v1)

(20 Jan 2026) Chain-of-Thought Compression Should Not Be Blind: V-Skip for Efficient Multimodal Reasoning via Dual-Path Anchoring [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2601.13879v4)

(19 Jan 2026) Think3D: Thinking with Space for Spatial Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2601.13029v3)

(16 Jan 2026) MMedExpert-R1: Strengthening Multimodal Medical Reasoning via Domain-Specific Adaptation and Clinical Guideline Reinforcement [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2601.10949v2)

(12 Jan 2026) CASHEW: Stabilizing Multimodal Reasoning via Iterative Trajectory Aggregation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2601.08010v1)

(12 Jan 2026) MEDVISTAGYM: A Scalable Training Environment for Thinking with Medical Images via Tool-Integrated Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2601.07107v1)

(11 Jan 2026) E^2-LLM: Bridging Neural Signals and Interpretable Affective Analysis [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2601.07877v1)

(11 Jan 2026) Thinking with Deltas: Incentivizing Reinforcement Learning via Differential Visual Reasoning Policy [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2601.06801v1)

(09 Jan 2026) SketchVL: Policy Optimization via Fine-Grained Credit Assignment for Chart Understanding and More [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2601.05688v1)

(08 Jan 2026) Agri-R1: Agricultural Reasoning for Disease Diagnosis via Automated-Synthesis and Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2601.04672v2)

(06 Jan 2026) ThinkRL-Edit: Thinking in Reinforcement Learning for Reasoning-Centric Image Editing [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2601.03467v3)

(06 Jan 2026) Towards Faithful Reasoning in Comics for Small MLLMs [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2601.02991v2)

(06 Jan 2026) Aligning Findings with Diagnosis: A Self-Consistent Reinforcement Learning Framework for Trustworthy Radiology Reporting [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2601.03321v2)

(01 Jan 2026) CPPO: Contrastive Perception for Vision Language Policy Optimization [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2601.00501v1)

(01 Jan 2026) From Sight to Insight: Improving Visual Reasoning Capabilities of Multimodal Models via Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2601.00215v1)

(31 Dec 2025) From Perception to Punchline: Empowering VLM with the Art of In-the-wild Meme [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.24555v2)

(22 Dec 2025) Training Multimodal Large Reasoning Models Needs Better Thoughts: A Three-Stage Framework for Long Chain-of-Thought Synthesis and Selection [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.18956v2)

(22 Dec 2025) CARE What Fails: Contrastive Anchored-REflection for Verifiable Multimodal Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.19554v4)

(22 Dec 2025) Anatomy-R1: Enhancing Anatomy Reasoning in Multimodal Large Language Models via Anatomical Similarity Curriculum and Group Diversity Augmentation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.19512v2)

(22 Dec 2025) SafeMed-R1: Adversarial Reinforcement Learning for Generalizable and Robust Medical Reasoning in Vision-Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.19317v1)

(20 Dec 2025) Stable and Efficient Single-Rollout RL for Multimodal Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.18215v1)

(19 Dec 2025) Deep But Reliable: Advancing Multi-turn Reasoning for Thinking with Images [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.17306v2)

(19 Dec 2025) Robust-R1: Degradation-Aware Reasoning for Robust Visual Understanding [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.17532v1)

(18 Dec 2025) AdaTooler-V: Adaptive Tool-Use for Images and Videos [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.16918v2)

(16 Dec 2025) Incentivizing Tool-augmented Thinking with Images for Medical Image Analysis [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.14157v1)

(16 Dec 2025) ViRC: Enhancing Visual Interleaved Mathematical CoT with Reason Chunking [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.14654v3)

(16 Dec 2025) OmniDrive-R1: Reinforcement-driven Interleaved Multi-modal Chain-of-Thought for Trustworthy Vision-Language Autonomous Driving [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.14044v2)

(13 Dec 2025) More Than the Final Answer: Improving Visual Extraction and Logical Consistency in Vision-Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.12487v1)

(13 Dec 2025) Journey Before Destination: On the importance of Visual Faithfulness in Slow Thinking [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.12218v2)

(12 Dec 2025) DentalGPT: Incentivizing Multimodal Complex Reasoning in Dentistry [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.11558v1)

(08 Dec 2025) MMRPT: MultiModal Reinforcement Pre-Training via Masked Vision-Dependent Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.07203v1)

(07 Dec 2025) Decouple to Generalize: Context-First Self-Evolving Learning for Data-Scarce Vision-Language Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.06835v1)

(07 Dec 2025) The Role of Entropy in Visual Grounding: Analysis and Optimization [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.06726v1)

(06 Dec 2025) ReCAD: Reinforcement Learning Enhanced Parametric CAD Model Generation with Vision-Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.06328v1)

(03 Dec 2025) TempR1: Improving Temporal Understanding of MLLMs via Temporal-Aware Multi-Task Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.03963v3)

(03 Dec 2025) Thinking with Programming Vision: Towards a Unified View for Thinking with Images [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.03746v1)

(03 Dec 2025) Omni-AutoThink: Adaptive Multimodal Reasoning via Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.03783v2)

(02 Dec 2025) See, Think, Learn: A Self-Taught Multimodal Reasoner [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.02456v1)

(29 Nov 2025) ChartPoint: Guiding MLLMs with Grounding Reflection for Chart Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.00305v1)

(28 Nov 2025) TIM-PRM: Verifying multimodal reasoning with Tool-Integrated PRM [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2511.22998v2)

(27 Nov 2025) GeoZero: Incentivizing Reasoning from Scratch on Geospatial Scenes [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2511.22645v3)

(24 Nov 2025) Syn-GRPO: Self-Evolving Data Synthesis for MLLM Perception Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2511.19343v1)

(23 Nov 2025) Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2511.18437v1)

(22 Nov 2025) PA-FAS: Towards Interpretable and Generalizable Multimodal Face Anti-Spoofing via Path-Augmented Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2511.17927v1)

(21 Nov 2025) VisReason: A Large-Scale Dataset for Visual Chain-of-Thought Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2511.17731v1)

(21 Nov 2025) ChainV: Atomic Visual Hints Make Multimodal Reasoning Shorter and Better [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2511.17106v1)

(20 Nov 2025) OpenMMReasoner: Pushing the Frontiers for Multimodal Reasoning with an Open and General Recipe [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2511.16334v4)

(19 Nov 2025) VisPlay: Self-Evolving Vision-Language Models from Images [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2511.15661v2)

(17 Nov 2025) Video Finetuning Improves Reasoning Between Frames [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2511.12868v1)

(17 Nov 2025) From Perception to Reasoning: Deep Thinking Empowers Multimodal Large Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2511.12861v4)

(17 Nov 2025) SafeGRPO: Self-Rewarded Multimodal Safety Alignment via Rule-Governed Policy Optimization [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2511.12982v1)

(14 Nov 2025) Closing the Gap: Data-Centric Fine-Tuning of Vision Language Models for the Standardized Exam Questions [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2512.00042v1)

(11 Nov 2025) From Exploration to Exploitation: A Two-Stage Entropy RLVR Approach for Noise-Tolerant MLLM Training [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2511.07738v2)

(10 Nov 2025) Revisiting the Data Sampling in Multimodal Post-training from a Difficulty-Distinguish View [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2511.06722v1)

(07 Nov 2025) PreResQ-R1: Towards Fine-Grained Rank-and-Score Reinforcement Learning for Visual Quality Assessment via Preference-Response Disentangled Policy Optimization [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2511.05393v1)

(04 Nov 2025) ChartM$^3$: A Multi-Stage Code-Driven Pipeline for Constructing Multi-Dimensional and Multi-Step Visual Reasoning Data in Chart Comprehension [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2511.02415v1)

(04 Nov 2025) SAIL-RL: Guiding MLLMs in When and How to Think via Dual-Reward RL Tuning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2511.02280v2)

(01 Nov 2025) UME-R1: Exploring Reasoning-Driven Generative Multimodal Embeddings [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2511.00405v2)

(01 Nov 2025) Saliency-R1: Incentivizing Unified Saliency Reasoning Capability in MLLM with Confidence-Guided Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2511.00396v3)

(31 Oct 2025) Spatial-SSRL: Enhancing Spatial Understanding via Self-Supervised Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2510.27606v2)

(23 Oct 2025) Metis-HOME: Hybrid Optimized Mixture-of-Experts for Multimodal Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2510.20519v1)

(23 Oct 2025) Small Drafts, Big Verdict: Information-Intensive Visual Reasoning via Speculation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2510.20812v1)

(18 Oct 2025) RL makes MLLMs see better than SFT [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2510.16333)

(16 Oct 2025) MathCanvas: Intrinsic Visual Chain-of-Thought for Multimodal Mathematical Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2510.14958v1)

(15 Oct 2025) Generative Universal Verifier as Multimodal Meta-Reasoner [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2510.13804v1)

(14 Oct 2025) HoneyBee: Data Recipes for Vision-Language Reasoners [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2510.12225)

(14 Oct 2025) DeepMMSearch-R1: Empowering Multimodal LLMs in Multimodal Web Search [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2510.12801)

(13 Oct 2025) CodePlot-CoT: Mathematical Visual Reasoning by Thinking with Code-Driven Images [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2510.11718)

(10 Oct 2025) Unleashing Perception-Time Scaling to Multimodal Reasoning Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2510.08964)

(10 Oct 2025) Spotlight on Token Perception for Multimodal Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2510.09285)

(10 Oct 2025) Tiny-R1V: Lightweight Multimodal Unified Reasoning Model via Model Merging [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2510.08987)

(9 Oct 2025) ARES: Multimodal Adaptive Reasoning via Difficulty-Aware Token-Level Entropy Shaping [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2510.08457v1)

(9 Oct 2025) SpatialLadder: Progressive Training for Spatial Reasoning in Vision-Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2510.08531v1)

(6 Oct 2025) Beyond Monolithic Rewards: A Hybrid and Multi-Aspect Reward Optimization for MLLM Alignment [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2510.05283)

(3 Oct 2025) Efficient Test-Time Scaling for Small Vision-Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2510.03574)

(29 Sep 2025) Latent Visual Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2509.24251v1)

(29 Sep 2025) GeoVLM-R1: Reinforcement Fine-Tuning for Improved Remote Sensing Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2509.25026v1)

(29 Sep 2025) VTPerception-R1: Enhancing Multimodal Reasoning via Explicit Visual and Textual Perceptual Grounding [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2509.24776v1)

(29 Sep 2025) Euclid's Gift: Enhancing Spatial Perception and Reasoning in Vision-Language Models via Geometric Surrogate Tasks [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2509.24473v1)

(28 Sep 2025) Poivre: Self-Refining Visual Pointing with Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2509.23746v1)

(27 Sep 2025) Decoupling Reasoning and Perception: An LLM-LMM Framework for Faithful Visual Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2509.23322v1)

(25 Sep 2025) MMR1: Enhancing Multimodal Reasoning with Variance-Aware Sampling and Open Resources [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2509.21268)

(12 Sep 2025) LaV-CoT: Language-Aware Visual CoT with Multi-Aspect Reward Optimization for Real-World Multilingual VQA [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2509.10026v1)

(9 Sep 2025) Mini-o3: Scaling Up Reasoning Patterns and Interaction Turns for Visual Search [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2509.07969v1)

(28 Aug 2025) R-4B: Incentivizing General-Purpose Auto-Thinking Capability in MLLMs via Bi-Mode Annealing and Reinforce Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2508.21113v1)

(27 Aug 2025) Self-Rewarding Vision-Language Model via Reasoning Decomposition [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2508.19652v1)

(18 Aug 2025) M3PO: Multimodal-Model-Guided Preference Optimization for Visual Instruction Following [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2508.12458v1)

(18 Aug 2025) Vision-G1: Towards General Vision Language Reasoning with Multi-Domain Data Curation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2508.12680v1)

(18 Aug 2025) Ovis2.5 Technical Report [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2508.11737v1)

(18 Aug 2025) MDPO: Overcoming the Training-Inference Divide of Masked Diffusion Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2508.13148v1)

(8 Aug 2025) SIFThinker: Spatially-Aware Image Focus for Visual Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2508.06259v1)

(7 Aug 2025) Uni-cot: Towards Unified Chain-of-Thought Reasoning Across Text and Vision [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2508.05606)

(7 Aug 2025) StructVRM: Aligning Multimodal Reasoning with Structured and Verifiable Reward Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2508.05383)

(5 Aug 2025) Geoint-R1: Formalizing Multimodal Geometric Reasoning with Dynamic Auxiliary Constructions [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2508.03173)

(30 Jul 2025) MoCHA: Advanced Vision-Language Reasoning with MoE Connector and Hierarchical Group Attention [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2507.22805)

(28 Jul 2025) Learning Only with Images: Visual Reinforcement Learning with Reasoning, Rendering, and Visual Feedback [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2507.20766v1)

(24 Jul 2025) MathOPEval: A Fine-grained Evaluation Benchmark for Visual Operations of MLLMs in Mathematical Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2507.18140v1)

(24 Jul 2025) SafeWork-R1: Coevolving Safety and Intelligence under the AI-45 Law [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2507.18576v1)

(22 Jul 2025) C2-Evo: Co-Evolving Multimodal Data and Model for Self-Improving Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://www.arxiv.org/abs/2507.16518)

(22 Jul 2025) Semi-off-Policy Reinforcement Learning for Vision-Language Slow-thinking Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2507.16814)

(11 Jul 2025) M2-Reasoning: Empowering MLLMs with Unified General and Spatial Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2507.08306v1)

(3 Jul 2025) Bootstrapping Grounded Chain-of-Thought in Multimodal LLMs for Data-Efficient Model Adaptation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2507.02859v1)

(1 Jul 2025) GLM-4.1V-Thinking: Towards Versatile Multimodal Reasoning with Scalable Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2507.01006)

(20 Jun 2025) GRPO-CARE: Consistency-Aware Reinforcement Learning for Multimodal Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2506.16141)

(16 Jun 2025) Metis-RISE: RL Incentivizes and SFT Enhances Multimodal Reasoning Model Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2506.13056v1)

(11 Jun 2025) ViCrit: A Verifiable Reinforcement Learning Proxy Task for Visual Perception in VLMs [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2506.10128v1)

(5 Jun 2025) Perceptual Decoupling for Scalable Multi-modal Reasoning via Reward-Optimized Captioning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2506.04559)

(5 Jun 2025) MINT-CoT: Enabling Interleaved Visual Tokens in Mathematical Chain-of-Thought Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2506.05331)

(16 May 2025) Visual Planning: Let's Think Only with Images [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2505.11409v1)

(15 May 2025) MathCoder-VL: Bridging Vision and Code for Enhanced Multimodal Mathematical Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2505.10557v1)

(13 May 2025) OpenThinkIMG: Learning to Think with Images via Visual Tool Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2505.08617v1)

(12 May 2025) Skywork-VL Reward: An Effective Reward Model for Multimodal Understanding and Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2505.07263v1)

(8 May 2025) Bring Reason to Vision: Understanding Perception and Reasoning through Model Merging [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2505.05464v1)

(08 May 2025) SpatialPrompting: Keyframe-driven Zero-Shot Spatial Reasoning with Off-the-Shelf Multimodal Large Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2505.04911v1)

(6 May 2025) X-Reasoner: Towards Generalizable Reasoning Across Modalities and Domains [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2505.03981v1)

(6 May 2025) Unified Multimodal Chain-of-Thought Reward Model through Reinforcement Fine-Tuning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2505.03318v1)

(6 May 2025) ReGraP-LLaVA: Reasoning enabled Graph-based Personalized Large Language and Vision Assistant [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2505.03654v1)

(5 May 2025) R1-Reward: Training Multimodal Reward Model Through Stable Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2505.02835v1)

(28 Apr 2025) SpatialReasoner: Towards Explicit and Generalizable 3D Spatial Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2504.20024v1)

(25 Apr 2025) Fast-Slow Thinking for Large Vision-Language Model Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2504.18458v1)

(25 Apr 2025) Unsupervised Visual Chain-of-Thought Reasoning via Preference Optimization [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2504.18397v1)

(25 Apr 2025) Skywork R1V2: Multimodal Hybrid Reinforcement Learning for Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2504.16656v1)

(21 Apr 2025) A Call for New Recipes to Enhance Spatial Reasoning in MLLMs [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2504.15037v1)

(20 Apr 2025) Relation-R1: Cognitive Chain-of-Thought Guided Reinforcement Learning for Unified Relational Comprehension [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2504.14642v1)

(12 Apr 2025) VisuoThink: Empowering LVLM Reasoning with Multimodal Tree Search [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2504.09130v1)

(10 Apr 2025) VLM-R1: A Stable and Generalizable R1-style Large Vision-Language Model [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2504.07615v1)

(10 Apr 2025) SoTA with Less: MCTS-Guided Sample Selection for Data-Efficient Visual Reasoning Self-Improvement [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2504.07934v1)

(10 Apr 2025) Perception-R1: Pioneering Perception Policy with Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2504.07954v1)

(10 Apr 2025) Kimi-VL Technical Report [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2504.07491)

(8 Apr 2025) On the Suitability of Reinforcement Fine-Tuning to Visual Tasks [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2504.05682v1)

(8 Apr 2025) Skywork R1V: Pioneering Multimodal Reasoning with Chain-of-Thought [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2504.05599v1)

(1 Apr 2025) Improved Visual-Spatial Reasoning via R1-Zero-Like Training [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2504.00883)

(17 Mar 2025) R1-VL: Learning to Reason with Multimodal Large Language Models via Step-wise Group Relative Policy Optimization [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2503.12937)

(13 Mar 2025) VisualPRM: An Effective Process Reward Model for Multimodal Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2503.10291)

(9 Mar 2025) Vision-R1: Incentivizing Reasoning Capability in Multimodal Large Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2503.06749)

(7 Mar 2025) R1-Omni: Explainable Omni-Multimodal Emotion Recognition with Reinforcement Learning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2503.05379)

(7 Mar 2025) Unified Reward Model for Multimodal Understanding and Generation [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2503.05236)

(7 Mar 2025) R1-Zero's "Aha Moment" in Visual Reasoning on a 2B Non-SFT Model [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2503.05132)

(3 Mar 2025) Visual-RFT: Visual Reinforcement Fine-Tuning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2503.01785)

(4 Feb 2025) Boosting Multimodal Reasoning with MCTS-Automated Structured Thinking [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2502.02339)

(13 Jan 2025) Imagine while Reasoning in Space: Multimodal Visualization-of-Thought [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2501.07542)

(10 Jan 2025) LlamaV-o1: Rethinking Step-by-step Visual Reasoning in LLMs [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2501.06186)

(9 Jan 2025) Can MLLMs Reason in Multimodality? EMMA: An Enhanced MultiModal ReAsoning Benchmark [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://www.arxiv.org/abs/2501.05444)

(3 Jan 2025) Virgo: A Preliminary Exploration on Reproducing o1-like MLLM [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2501.01904)

(30 Dec 2024) Slow Perception: Let's Perceive Geometric Figures Step-by-step [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2412.20631)

(19 Dec 2024) Progressive Multimodal Reasoning via Active Retrieval [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2412.14835)

(29 Nov 2024) Interleaved-Modal Chain-of-Thought [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2411.19488)

(15 Nov 2024) Thinking Before Looking: Improving Multimodal LLM Reasoning via Mitigating Visual Hallucination [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2411.12591)

(15 Nov 2024) LLaVA-CoT: Let Vision Language Models Reason Step-by-Step [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2411.10440)

(30 Oct 2024) Vision-Language Models Can Self-Improve Reasoning via Reflection [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2411.00855)

(23 Oct 2024) R-CoT: Reverse Chain-of-Thought Problem Generation for Geometric Reasoning in Large Multimodal Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2410.17885)

(21 Oct 2024) Improve Vision Language Model Chain-of-thought Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2410.16198)

(11 Oct 2024) M3Hop-CoT: Misogynous Meme Identification with Multimodal Multi-hop Chain-of-Thought [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2410.09220)

(6 Oct 2024) MC-CoT: A Modular Collaborative CoT Framework for Zero-shot Medical-VQA with LLM and MLLM Integration [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2410.04521)

(4 Oct 2024) Visual-O1: Understanding Ambiguous Instructions via Multi-modal Multi-turn Chain-of-thoughts Reasoning [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2410.03321)

(13 Jun 2024) Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2406.09403)

(28 Dec 2023) Grounding-Prompter: Prompting LLM with Multimodal Information for Temporal Sentence Grounding in Long Videos [![arXiv](https://img.shields.io/badge/arXiv-b31b1b.svg)](https://arxiv.org/abs/2312.17117v1)

(14 Dec 2023) Multi-modal Latent Space Learning for Chain-of-Thought Reasoning in Language Models [![arXiv](htt