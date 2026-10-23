# Awesome Industrial Anomaly Detection [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

We discuss public datasets and related studies in detail. Welcome to read our paper and make comments.

[Deep Industrial Image Anomaly Detection: A Survey (Machine Intelligence Research)](https://link.springer.com/article/10.1007/s11633-023-1459-z)

[A Survey of Recent Advances in Industrial Anomaly Detection: From Normal-Only Training to Foundation-Model Priors [2026]](https://www.preprints.org/manuscript/202606.0719)

[IM-IAD: Industrial Image Anomaly Detection Benchmark in Manufacturing [TCYB 2024]](https://arxiv.org/abs/2301.13359)[[code]](https://github.com/M-3LAB/open-iad)[[中文]](https://blog.csdn.net/m0_63828250/article/details/136891730)

We will keep focusing on this field and updating relevant information.

Keywords: anomaly detection, anomaly segmentation, industrial image, defect detection

<!-- [[Main Page]](https://github.com/M-3LAB) [[]](https://github.com/M-3LAB/awesome-industrial-anomaly-detection) [[Benchmark]](https://github.com/M-3LAB/open-iad) [[Result]](https://github.com/M-3LAB/IM-IAD) -->

🔥🔥🔥 Contributions to our repository are welcome. Feel free to categorize the papers and [pull requests](https://github.com/M-3LAB/awesome-industrial-anomaly-detection/pulls).

---
🔥🔥🔥 We have released AD-Copilot, an end-to-end trained MLLM for industrial anomaly detection. Most impressively, AD-Copilot surpasses humans on real industrial inspection tasks! Try it at [[Code]](https://github.com/jam-cc/AD-Copilot)[[Demo]](https://huggingface.co/spaces/jiang-cc/AD-Copilot)

🔥🔥🔥 How well are current MLLMs performing as industrial quality inspectors? Which MLLM performs best in industrial anomaly detection? Please refer to our recent research. [[ICLR 2025]](https://arxiv.org/abs/2410.09453)[[Github]](https://github.com/jam-cc/MMAD)

🔥🔥🔥 We compare different types of anomaly synthesis methods in detail. Welcome to make comments. 

ASBench: Image Anomalies Synthesis Benchmark for Anomaly Detection [[paper]](https://arxiv.org/abs/2510.07927)

A Survey on Industrial Anomalies Synthesis [[paper]](https://arxiv.org/abs/2502.16412)[[github]](https://github.com/M-3LAB/awesome-anomaly-synthesis)

🔥🔥🔥 3D Anomaly Detection: Approaches, Benchmark, Challenges, and Prospects for Intelligent Manufacturing [[paper]](https://www.researchsquare.com/article/rs-11314110/v1) [[github]](https://github.com/M-3LAB/awesome-3d-anomaly-detection)

---
## Table of Contents
- [Awesome Industrial Anomaly Detection ](#awesome-industrial-anomaly-detection-)
  - [Table of Contents](#table-of-contents)
- [SOTA methods with code](#sota-methods-with-code)
- [Recommended Benchmarks](#recommended-benchmarks)
- [Recent research \[survey\]](#recent-research-survey)
  - [ECCV 2026](#eccv-2026)
  - [ICML 2026](#icml-2026)
  - [CVPR 2026](#cvpr-2026)
  - [ICLR 2026](#iclr-2026)
  - [AAAI 2026](#aaai-2026)
  - [NeurIPS 2025](#neurips-2025)
  - [KDD 2025](#kdd-2025)
  - [ICCV 2025](#iccv-2025)
  - [ICML 2025](#icml-2025)
  - [CVPR 2025](#cvpr-2025)
- [Paper Tree (Classification of representative methods)](#paper-tree-classification-of-representative-methods)
- [Timeline](#timeline)
- [Paper list for industrial image anomaly detection](#paper-list-for-industrial-image-anomaly-detection)
- [Related Survey, Benchmark, and Framework](#related-survey-benchmark-and-framework)
- [2 Unsupervised AD](#2-unsupervised-ad)
  - [2.1 Feature-Embedding-based Methods](#21-feature-embedding-based-methods)
    - [2.1.1 Teacher-Student](#211-teacher-student)
    - [2.1.2 One-Class Classification (OCC)](#212-one-class-classification-occ)
    - [2.1.3 Distribution-Map](#213-distribution-map)
    - [2.1.4 Memory Bank](#214-memory-bank)
    - [2.1.5 Vison Language AD](#215-vison-language-ad)
  - [2.2 Reconstruction-Based Methods](#22-reconstruction-based-methods)
    - [2.2.1 Autoencoder (AE)](#221-autoencoder-ae)
    - [2.2.2 Generative Adversarial Networks (GANs)](#222-generative-adversarial-networks-gans)
    - [2.2.3 Transformer](#223-transformer)
    - [2.2.4 Diffusion Model](#224-diffusion-model)
    - [2.2.5 Others](#225-others)
  - [2.3 Supervised AD](#23-supervised-ad)
    - [More Normal Samples With (Less Abnormal Samples or Weak Labels)](#more-normal-samples-with-less-abnormal-samples-or-weak-labels)
    - [More Abnormal Samples](#more-abnormal-samples)
- [3 Other Research Direction](#3-other-research-direction)
  - [3.1 Zero/Few-Shot AD](#31-zerofew-shot-ad)
    - [Zero-Shot AD](#zero-shot-ad)
    - [Few-Shot AD](#few-shot-ad)
  - [3.2 Noisy AD](#32-noisy-ad)
  - [3.3 Anomaly Synthesis \[awesome-anomaly-synthesis\]](#33-anomaly-synthesis-awesome-anomaly-synthesis)
  - [3.4 RGBD AD](#34-rgbd-ad)
  - [3.5 3D AD](#35-3d-ad)
  - [3.6 Continual AD](#36-continual-ad)
  - [3.7 Uniform/Multi-Class AD](#37-uniformmulti-class-ad)
  - [3.8 Logical AD](#38-logical-ad)
  - [3.9 MLLM-based AD](#39-mllm-based-ad)
  - [3.10 Video IAD](#310-video-iad)
  - [Other settings](#other-settings)
    - [TTT binary segmentation](#ttt-binary-segmentation)
    - [MoE with TTA](#moe-with-tta)
    - [Adversary Attack](#adversary-attack)
    - [Defect Classification](#defect-classification)
    - [Rubustness](#rubustness)
    - [Universal Task](#universal-task)
- [4 Dataset](#4-dataset)
  - [BibTex Citation](#bibtex-citation)
  - [Star History](#star-history)


# SOTA methods with code

|  Title  |   Venue  |   Date   |   Code   |   topic   |
|:--------|:--------:|:--------:|:--------:|:--------:|
| ![Star](https://img.shields.io/github/stars/hq-deng/RD4AD.svg?style=social&label=Star) <br> [**Anomaly Detection via Reverse Distillation from One-Class Embedding**](https://openaccess.thecvf.com/content/CVPR2022/html/Deng_Anomaly_Detection_via_Reverse_Distillation_From_One-Class_Embedding_CVPR_2022_paper.html) <br> | CVPR | 2022 | [Github](https://github.com/hq-deng/RD4AD) | Teacher-Student |
| ![Star](https://img.shields.io/github/stars/guojiajeremy/Dinomaly.svg?style=social&label=Star) <br> [**Dinomaly: The Less Is More Philosophy in Multi-Class Unsupervised Anomaly Detection**](https://openaccess.thecvf.com/content/CVPR2025/html/Guo_Dinomaly_The_Less_Is_More_Philosophy_in_Multi-Class_Unsupervised_Anomaly_CVPR_2025_paper.html) <br> | CVPR | 2025 | [Github](https://github.com/guojiajeremy/Dinomaly) | Multi-Class Unified |
| ![Star](https://img.shields.io/github/stars/guojiajeremy/Dinomaly2.svg?style=social&label=Star) <br> [**One Dinomaly2 Detect Them All: A Unified Framework for Full-Spectrum Unsupervised Anomaly Detection**](https://arxiv.org/abs/2510.17611) <br> | Arxiv | 2025 | [Github](https://github.com/guojiajeremy/Dinomaly2) | Multi-Class, Multi-View, Multi-Modal, Few-shot |
| ![Star](https://img.shields.io/github/stars/tientrandinh/Revisiting-Reverse-Distillation.svg?style=social&label=Star) <br> [**Revisiting Reverse Distillation for Anomaly Detection**](https://openaccess.thecvf.com/content/CVPR2023/html/Tien_Revisiting_Reverse_Distillation_for_Anomaly_Detection_CVPR_2023_paper.html) <br> | CVPR | 2023 | [Github](https://github.com/tientrandinh/Revisiting-Reverse-Distillation) | Teacher-Student |
| ![Star](https://img.shields.io/github/stars/DonaldRR/SimpleNet.svg?style=social&label=Star) <br> [**SimpleNet: A Simple Network for Image Anomaly Detection and Localization**](https://openaccess.thecvf.com/content/CVPR2023/html/Liu_SimpleNet_A_Simple_Network_for_Image_Anomaly_Detection_and_Localization_CVPR_2023_paper.html) <br> | CVPR | 2023 | [Github](https://github.com/DonaldRR/SimpleNet) | One-Class-Classification |
| ![Star](https://img.shields.io/github/stars/gudovskiy/cflow-ad.svg?style=social&label=Star) <br> [**Real-time unsupervised anomaly detection with localization via conditional normalizing flows**](https://openaccess.thecvf.com/content/WACV2022/html/Gudovskiy_CFLOW-AD_Real-Time_Unsupervised_Anomaly_Detection_With_Localization_via_Conditional_Normalizing_WACV_2022_paper.html) <br> | WACV | 2022 | [Github](https://github.com/gudovskiy/cflow-ad) | Distribution Map |
| ![Star](https://img.shields.io/github/stars/amazon-science/patchcore-inspection.svg?style=social&label=Star) <br> [**Towards total recall in industrial anomaly detection**](https://openaccess.thecvf.com/content/CVPR2022/html/Roth_Towards_Total_Recall_in_Industrial_Anomaly_Detection_CVPR_2022_paper.html) <br> | CVPR | 2022 | [Github](https://github.com/amazon-science/patchcore-inspection) | Memory-bank |
| ![Star](https://img.shields.io/github/stars/vitjanz/draem.svg?style=social&label=Star) <br> [**Draem-a discriminatively trained reconstruction embedding for surface anomaly detection**](https://openaccess.thecvf.com/content/ICCV2021/html/Zavrtanik_DRAEM_-_A_Discriminatively_Trained_Reconstruction_Embedding_for_Surface_Anomaly_ICCV_2021_paper.html) <br> | ICCV | 2021 | [Github](https://github.com/vitjanz/draem) | Reconstruction-based |
| ![Star](https://img.shields.io/github/stars/VitjanZ/DSR_anomaly_detection.svg?style=social&label=Star) <br> [**DSR: A dual subspace re-projection network for surface anomaly detection**](https://link.springer.com/chapter/10.1007/978-3-031-19821-2_31) <br> | ECCV | 2022 | [Github](https://github.com/VitjanZ/DSR_anomaly_detection) | Reconstruction-based |
| ![Star](https://img.shields.io/github/stars/zhangzjn/ocr-gan.svg?style=social&label=Star) <br> [**Omni-frequency Channel-selection Representations for Unsupervised Anomaly Detection**](https://ieeexplore.ieee.org/abstract/document/10192551/) <br> | TIP | 2023 | [Github](https://github.com/zhangzjn/ocr-gan) | Reconstruction-based |
| ![Star](https://img.shields.io/github/stars/cnulab/RealNet.svg?style=social&label=Star) <br> [**RealNet: A Feature Selection Network with Realistic Synthetic Anomaly for Anomaly Detection**](https://arxiv.org/abs/2403.05897) <br> | CVPR | 2024 | [Github](https://github.com/cnulab/RealNet) | Reconstruction-based |
| ![Star](https://img.shields.io/github/stars/MediaBrain-SJTU/RegAD.svg?style=social&label=Star) <br> [**Registration based few-shot anomaly detection**](https://link.springer.com/chapter/10.1007/978-3-031-20053-3_18) <br> | ECCV | 2022 | [Github](https://github.com/MediaBrain-SJTU/RegAD) | Few Shot |
| ![Star](https://img.shields.io/github/stars/CASIA-IVA-Lab/AnomalyGPT.svg?style=social&label=Star) <br> [**AnomalyGPT: Detecting Industrial Anomalies using Large Vision-Language Models**](https://arxiv.org/abs/2308.15366) <br> | AAAI | 2024 | [Github](https://github.com/CASIA-IVA-Lab/AnomalyGPT) | Few Shot |
| ![Star](https://img.shields.io/github/stars/jam-cc/AD-Copilot.svg?style=social&label=Star) <br> [**AD-Copilot: A Vision-Language Assistant for Industrial Anomaly Detection via Visual In-context Comparison**](https://arxiv.org/abs/2603.13779) <br> | arxiv | 2026 | [Github](https://github.com/jam-cc/AD-Copilot) | MLLM |
| ![Star](https://img.shields.io/github/stars/Choubo/DRA.svg?style=social&label=Star) <br> [**Catching Both Gray and Black Swans: Open-set Supervised Anomaly Detection**](https://openaccess.thecvf.com/content/CVPR2022/html/Ding_Catching_Both_Gray_and_Black_Swans_Open-Set_Supervised_Anomaly_Detection_CVPR_2022_paper.html) <br> | CVPR | 2022 | [Github](https://github.com/Choubo/DRA) | Few abnormal samples |
| ![Star](https://img.shields.io/github/stars/xcyao00/BGAD.svg?style=social&label=Star) <br> [**Explicit Boundary Guided Semi-Push-Pull Contrastive Learning for Supervised Anomaly Detection**](https://openaccess.thecvf.com/content/CVPR2023/html/Yao_Explicit_Boundary_Guided_Semi-Push-Pull_Contrastive_Learning_for_Supervised_Anomaly_Detection_CVPR_2023_paper.html) <br> | CVPR | 2023 | [Github](https://github.com/xcyao00/BGAD) | Few abnormal samples |
| ![Star](https://img.shields.io/github/stars/tianyu0207/IGD.svg?style=social&label=Star) <br> [**Deep one-class classification via interpolated gaussian descriptor**](https://ojs.aaai.org/index.php/AAAI/article/view/19915) <br> | AAAI | 2022 | [Github](https://github.com/tianyu0207/IGD) | Noisy AD |
| ![Star](https://img.shields.io/github/stars/TencentYoutuResearch/AnomalyDetection-SoftPatch.svg?style=social&label=Star) <br> [**SoftPatch: Unsupervised Anomaly Detection with Noisy Data**](https://proceedings.neurips.cc/paper_files/paper/2022/hash/637a456d89289769ac1ab29617ef7213-Abstract-Conference.html) <br> | NeurIPS | 2022 | [Github](https://github.com/TencentYoutuResearch/AnomalyDetection-SoftPatch) | Noisy AD |
| ![Star](https://img.shields.io/github/stars/DeclanMcIntosh/InReaCh.svg?style=social&label=Star) <br> [**Inter-Realization Channels: Unsupervised Anomaly Detection Beyond One-Class Classification**](https://openaccess.thecvf.com/content/ICCV2023/html/McIntosh_Inter-Realization_Channels_Unsupervised_Anomaly_Detection_Beyond_One-Class_Classification_ICCV_2023_paper.html) <br> | ICCV | 2023 | [Github](https://github.com/DeclanMcIntosh/InReaCh) | Noisy AD |
| ![Star](https://img.shields.io/github/stars/shirowalker/UCAD.svg?style=social&label=Star) <br> [**Unsupervised Continual Anomaly Detection with Contrastively-learned Prompt**](https://ojs.aaai.org/index.php/AAAI/article/view/28153) <br> | AAAI | 2024 | [Github](https://github.com/shirowalker/UCAD) | Continual AD |
| ![Star](https://img.shields.io/github/stars/zhiyuanyou/UniAD.svg?style=social&label=Star) <br> [**A Unified Model for Multi-class Anomaly Detection**](https://proceedings.neurips.cc/paper_files/paper/2022/hash/1d774c112926348c3e25ea47d87c835b-Abstract-Conference.html) <br> | NeurIPS | 2022 | [Github](https://github.com/zhiyuanyou/UniAD) | Multi-class unified |
| ![Star](https://img.shields.io/github/stars/RuiyingLu/HVQ-Trans.svg?style=social&label=Star) <br> [**Hierarchical Vector Quantized Transformer for Multi-class Unsupervised Anomaly Detection**](https://openreview.net/pdf?id=clJTNssgn6) <br> | NeurIPS | 2023 | [Github](https://github.com/RuiyingLu/HVQ-Trans) | Multi-class unified |
| ![Star](https://img.shields.io/github/stars/nomewang/M3DM.svg?style=social&label=Star) <br> [**Multimodal Industrial Anomaly Detection via Hybrid Fusion**](https://openaccess.thecvf.com/content/CVPR2023/html/Wang_Multimodal_Industrial_Anomaly_Detection_via_Hybrid_Fusion_CVPR_2023_paper.html) <br> | CVPR | 2023 | [Github](https://github.com/nomewang/M3DM) | RGBD |
| ![Star](https://img.shields.io/github/stars/M-3LAB/Real3D-AD.svg?style=social&label=Star) <br> [**Real3D-AD: A Dataset of Point Cloud Anomaly Detection**](https://openreview.net/pdf?id=zGthDp4yYe) <br> | NeurIPS | 2023 | [Github](https://github.com/M-3LAB/Real3D-AD) | Point Cloud |
| ![Star](https://img.shields.io/github/stars/hq-deng/AnoVL.svg?style=social&label=Star) <br> [**AnoVL: Adapting Vision-Language Models for Unified Zero-shot Anomaly Localization**](https://arxiv.org/abs/2308.15939) <br> | arxiv | 2023 | [Github](https://github.com/hq-deng/AnoVL) | Zero Shot |
| ![Star](https://img.shields.io/github/stars/caoyunkang/GroundedSAM-zero-shot-anomaly-detection.svg?style=social&label=Star) <br> [**Segment Any Anomaly without Training via Hybrid Prompt Regularization**](https://arxiv.org/abs/2305.10724) <br> | arxiv | 2023 | [Github](https://github.com/caoyunkang/GroundedSAM-zero-shot-anomaly-detection) | Zero Shot |
| ![Star](https://img.shields.io/github/stars/oopil/PSAD_logical_anomaly_detection.svg?style=social&label=Star) <br> [**PSAD: Few Shot Part Segmentation Reveals Compositional Logic for Industrial Anomaly Detection**](https://ojs.aaai.org/index.php/AAAI/article/view/28703) <br> | AAAI | 2024 | [Github](https://github.com/oopil/PSAD_logical_anomaly_detection) | Logical/Few Shot |
| ![Star](https://img.shields.io/github/stars/MaticFuc/SALAD.svg?style=social&label=Star) <br> [**SALAD -- Semantics-Aware Logical Anomaly Detection**](https://arxiv.org/abs/2509.02101) <br> | ICCV | 2025 | [Github](https://github.com/MaticFuc/SALAD) | Logical |
| ![Star](https://img.shields.io/github/stars/YoojLee/Uniformaly.svg?style=social&label=Star) <br> [**UniFormaly: Towards Task-Agnostic Unified Framework for Visual Anomaly Detection**](https://arxiv.org/abs/2307.12540) <br> | arxiv | 2023 | [Github](https://github.com/YoojLee/Uniformaly) | Multi-class unified |


# Recommended Benchmarks
|  Title  |   Venue  |   Date   |   Code   |   topic   |
|:--------|:--------:|:--------:|:--------:|:--------:|
| ![Star](https://img.shields.io/github/stars/open-edge-platform/anomalib.svg?style=social&label=Star) <br> [**Anomalib: A Deep Learning Library for Anomaly Detection**](https://ieeexplore.ieee.org/abstract/document/9897283/) <br> | ICIP | 2022 | [Github](https://github.com/open-edge-platform/anomalib) | Benchmark |
| ![Star](https://img.shields.io/github/stars/M-3LAB/open-iad.svg?style=social&label=Star) <br> [**IM-IAD: Industrial Image Anomaly Detection Benchmark in Manufacturing**](https://arxiv.org/abs/2301.13359) <br> | TCYB | 2024 | [Github](https://github.com/M-3LAB/open-iad) | Benchmark |
| ![Star](https://img.shields.io/github/stars/zhangzjn/ader.svg?style=social&label=Star) <br> [**ADer: A Comprehensive Benchmark for Multi-class Visual Anomaly Detection**](http://arxiv.org/pdf/2406.03262v1) <br> | arxiv | 2024 | [Github](https://github.com/zhangzjn/ader) | Benchmark |
| ![Star](https://img.shields.io/github/stars/jam-cc/MMAD.svg?style=social&label=Star) <br> [**MMAD: The First-Ever Comprehensive Benchmark for Multimodal Large Language Models in Industrial Anomaly Detection**](https://arxiv.org/abs/2410.09453) <br> | ICLR | 2025 | [Github](https://github.com/jam-cc/MMAD) | Benchmark |
| ![Star](https://img.shields.io/github/stars/en-research/RobustMAD.svg?style=social&label=Star) <br> [**RobustMAD: Evaluating Real-World Robustness of Multimodal Small Language Models for Deployable Anomaly Detection Assistants**](https://openreview.net/pdf?id=skrA9UYNIZ) <br> | TMLR | 2026 | [Github](https://github.com/en-research/RobustMAD) | Benchmark |


# Recent research [[survey]](https://www.preprints.org/manuscript/202606.0719)

<!-- Recent advances in industrial anomaly detection are organized below by five sources of generalization, highlighting emerging research trends and representative methods.  -->

[![Figure 2: Representative industrial anomaly detection methods organized by five sources of generalization and the evaluation frontier](assets/fig2_taxonomy.png)](assets/fig2_taxonomy.pdf)

## ECCV 2026
+ CMDS-AD: Cross-Modal Dual-Stream Decoupling for Few-Shot Anomaly Detection [[ECCV 2026]](https://arxiv.org/abs/2606.20300)[[code]](https://github.com/Junhaocai27/CMDS-AD)
+ Defect-aware Hybrid Prompt Optimization for Zero-Shot Multi-type Anomaly Detection and Segmentation [[ECCV 2026]](https://arxiv.org/abs/2512.09446)
+ DeCo: Zero-Shot Anomaly Generation through Decoupling and Recoupling [[ECCV 2026]](https://arxiv.org/abs/2608.07904)[[code]](https://github.com/HUST-SLOW/DeCo)
+ UniScale: Arbitrary-Scale Anomaly Generation [[ECCV 2026]](https://arxiv.org/abs/2608.07864)[[code]](https://github.com/HUST-SLOW/UniScale)
+ PADFormer: Pose-agnostic Anomaly Detection from Sparse View Images [[ECCV 2026 Oral]](https://arxiv.org/abs/2608.04210)
+ ReFP-AD: Rectified Flow Preconditioning for Energy-Based Anomaly Detection [[ECCV 2026]](https://arxiv.org/abs/2608.01793)[[code]](https://github.com/CLendering/ReFP-AD)
+ IMMoE: Incomplete Multi-View Anomaly Detection via Mixture of View Experts Fusion [[ECCV 2026]](https://arxiv.org/abs/2607.19032)[[code]](https://github.com/HULEI7/IMMoE)
+ O-VAD: Industrial Video Anomaly Detection through Object-Centric Tracking and Reasoning [[ECCV 2026]](https://arxiv.org/abs/2607.18142)[[code]](https://o-vad.github.io/)
+ Global Logic and Local Search: Dual-Stream Multimodal In-Context Learning for Verifiable Industrial Anomaly Detection [[ECCV 2026]](https://arxiv.org/abs/2607.03817)
+ ArcAD: Anomaly-Rectified Calibration for Cold-Start Supervised Anomaly Detection [[ECCV 2026]](https://arxiv.org/abs/2607.02252)[[code]](https://github.com/LGC-AD/ArcAD)
+ Robust Zero-shot Anomaly Detection under Limited Auxiliary Anomaly Priors [[ECCV 2026]](https://arxiv.org/abs/2606.29428)
+ LogiCo: A Unified Framework for Logical and Structural Anomaly Detection [[ECCV 2026]](https://arxiv.org/abs/2606.28688)[[code]](https://github.com/cnulab/LogiCo)
+ DeCoFlow: Structural Decomposition of Normalizing Flows for Continual Anomaly Detection [[ECCV 2026]](https://arxiv.org/abs/2606.26687)
+ MATCH: Flow Matching for Multi-View Anomaly Detection [[ECCV 2026]](https://arxiv.org/abs/2606.24375)
+ Rethinking Continual Anomaly Detection on the Edge: Benchmarking Under Realistic Industrial Conditions [[ECCV 2026]](https://arxiv.org/abs/2605.24251)[[code]](https://github.com/Continue-Edge-AI-Lab/Rethinking-Continual-AD)
+ FuDU: A Fuzzy Dual-dimension Uncertainty Framework for Streaming Active Learning in Industrial Defect Detection[[ECCV 2026]](https://arxiv.org/abs/2609.02212)[[code]](https://github.com/wangzhaoyang-508/FuDU)
+ Proximity-CLIP: Text-Guided Semantic Proximity Learning for Zero-Shot Anomaly Detection [[ECCV 2026]](https://arxiv.org/abs/2609.07229)[[paper]](https://media.eventhosts.cc/Conferences/ECCV2026/pdfs/8183.pdf)
+ CL-Anomaly: Layer-Adaptive Mixture-of-Experts with Multimodal Large Language Model for Continual Learning in Anomaly Detection [[ECCV 2026]](https://arxiv.org/abs/2607.02930)[[code]](https://github.com/WenDongyp/CL-Anomaly)
+ Anomaly Factory 3D: A Modular Framework for Diverse Pseudo-Anomaly Synthesis in Unsupervised 3D Anomaly Detection [[ECCV 2026]](https://arxiv.org/abs/2606.29181)[[code]](https://github.com/vpc-ccg/AF3AD)
+ GroundingAnomaly: Spatially-Grounded Diffusion for Few-Shot Anomaly Synthesis [[ECCV 2026]](https://arxiv.org/abs/2604.08301)
+ BAAF: Universal Transformation of One-Class Classifiers for Unsupervised Image Anomaly Detection [[ECCV 2026]](https://arxiv.org/abs/2602.13091)[[code]](https://github.com/DeclanMcIntosh/BAAF)
+ DeltaDeno: Zero-Shot Anomaly Generation via Delta-Denoising Attribution [[ECCV 2026]](https://arxiv.org/abs/2511.16920)[[code]](https://github.com/CROVO1026/DeltaDeno)
+ VarProtoAD: Variational Prototype-Conditioned Prompting for Zero-Shot Anomaly Detection [[ECCV 2026]](https://eccv.ecva.net/virtual/2026/poster/3553)
+ DeMuS: Learning Decoupled Matching and Scoring for Batch Zero-Shot Industrial Anomaly Detection [[ECCV 2026]](https://eccv.ecva.net/virtual/2026/poster/3717)[[code]](https://github.com/evoLonation/DeMuS)
+ Fast Dynamic Prototypes for Unsupervised Anomaly Detection and Localization [[ECCV 2026]](https://eccv.ecva.net/virtual/2026/poster/3350)[[code coming soon]](https://github.com/lmlpy/FDP)
+ HLRAD: High-dimensional Latent Representation for Unified Anomaly Detection [[ECCV 2026]](https://eccv.ecva.net/virtual/2026/poster/5190)
+ Beyond Common Sense: Grounding Logical Anomaly Detection in Inspection Criteria [[ECCV 2026]](https://eccv.ecva.net/virtual/2026/poster/4468)[[code]](https://github.com/tzjtatata/SCAN)
+ EGVLR: Evidence-Grounded Vision-Language Reinforcement for Anomaly Reasoning [[ECCV 2026]](https://eccv.ecva.net/virtual/2026/poster/4683)[[code]](https://github.com/leolin65/EGVLR-project)
+ A Comprehensive Analysis about Unsupervised Outlier Detection for Images [[ECCV 2026]](https://eccv.ecva.net/virtual/2026/poster/5320)[[code]](https://github.com/zhliu-uod/VUOD)

## ICML 2026
+ Memory-Distilled Selection for Noise-Robust Anomaly Detection [[ICML 2026]](https://arxiv.org/abs/2605.26676)[[code]](https://github.com/SirojbekSafarov/MeDS)
+ CoGeoAD: Hierarchical Color-Geometric Fusion with Multi-View Attention for Zero-Shot 3D Anomaly Detection [[ICML 2026]](https://icml.cc/virtual/2026/poster/62489)
+ Formally Exploring Visual Anomaly Detection Evaluation Metrics [[ICML 2026]](https://icml.cc/virtual/2026/poster/65518)
+ Is Training Necessary for Anomaly Detection? [[ICML 2026]](https://arxiv.org/abs/2601.22763)[[code]](https://github.com/longkukuhi/RAD)
+ Remove the Ambiguity: Few-shot Multimodal Anomaly Detection Using Crossmodal Feature Replacers [[ICML 2026]](https://icml.cc/virtual/2026/poster/62880)
+ Anomaly-Preference Image Generation [[ICML 2026]](https://arxiv.org/abs/2605.02439)
+ Mixture Prototype Flow Matching for Open-Set Supervised Anomaly Detection [[ICML 2026]](https://arxiv.org/abs/2605.02438)[[code]](https://github.com/fuyunwang/MPFM-OSAD)

## CVPR 2026
+ Towards an Incremental Unified Multimodal Anomaly Detection: Augmenting Multimodal [[CVPR 2026]](https://arxiv.org/abs/2603.02629)
+ InvAD: Inversion-based Reconstruction-Free Anomaly Detection with Diffusion Models [[CVPR 2026]](https://arxiv.org/abs/2504.05662)[[code]](https://github.com/SkyShunsuke/InversionAD)
+ SubspaceAD: Training-Free Few-Shot Anomaly Detection via Subspace Modeling [[CVPR 2026]](https://arxiv.org/abs/2602.23013)[[code]](https://github.com/CLendering/SubspaceAD)
+ VisualAD: Language-Free Zero-Shot Anomaly Detection via Vision Transformer [[CVPR 2026]](https://arxiv.org/abs/2603.07952)[[code]](https://github.com/7HHHHH/VisualAD)
+ Bidirectional Multimodal Prompt Learning with Scale-Aware Training for Few-Shot Multi-Class Anomaly Detection [[CVPR 2026]](https://arxiv.org/abs/2408.13516)[[code]](https://github.com/YoojLee/AnoPLe)
+ MAGIC: Few-Shot Mask-Guided Anomaly Inpainting with Prompt Perturbation, Spatially Adaptive Guidance, and Context Awareness [[CVPR 2026 Findings]](https://arxiv.org/abs/2507.02314)[[code]](https://github.com/SpatialAILab/MAGIC-Anomaly-generation)
+ DLVP-CLIP: Enhancing Fine-Grained Zero-Shot Anomaly Detection via Dynamic Local Visual Prompting [[CVPR 2026]](https://cvpr.thecvf.com/virtual/2026/poster/39303)
+ Back to Point: Exploring Point-Language Models for Zero-Shot 3D Anomaly Detection [[CVPR 2026]](https://arxiv.org/abs/2603.21511)[[code]](https://github.com/wistful-8029/BTP-3DAD)
+ AnomalyVFM -- Transforming Vision Foundation Models into Zero-Shot Anomaly Detectors [[CVPR 2026]](https://arxiv.org/abs/2601.20524)[[code]](https://github.com/MaticFuc/AnomalyVFM)
+ MoECLIP: Patch-Specialized Experts for Zero-shot Anomaly Detection [[CVPR 2026]](https://arxiv.org/abs/2603.03101)[[code]](https://github.com/CoCoRessa/MoECLIP)
+ AG-VAS: Anchor-Guided Zero-Shot Visual Anomaly Segmentation with Large Multimodal Models [[CVPR 2026]](https://arxiv.org/abs/2603.01305)[[code]](https://github.com/xiaozhen228/AG-VAS)
+ Wavelet-Driven 3D Anomaly Detection under Pose-Agnostic and Sparse-View [[CVPR 2026]](https://cvpr.thecvf.com/virtual/2026/poster/38024)
+ PDD: Manifold-Prior Diverse Distillation for Medical Anomaly Detection [[CVPR 2026]](https://arxiv.org/abs/2603.07142)[[code]](https://github.com/OxygenLu/PDD)
+ CoPS: Conditional Prompt Synthesis for Zero-Shot Anomaly Detection [[CVPR 2026 Findings]](https://arxiv.org/abs/2508.03447)[[code]](https://github.com/cqylunlun/CoPS)
+ One-to-More: High-Fidelity Training-Free Anomaly Generation with Attention Control [[CVPR 2026]](https://arxiv.org/abs/2603.18093)[[code]](https://github.com/echrao/O2MAG)
+ FB-CLIP: Fine-Grained Zero-Shot Anomaly Detection with Foreground-Background Disentanglement [[CVPR 2026]](https://arxiv.org/abs/2603.19608)[[code]](https://github.com/Xi-Mu-Yu/FB-CLIP)
+ FastRef:Fast Prototype Refinement for Few-Shot Industrial Anomaly Detection [[CVPR 2026]](https://arxiv.org/abs/2506.21398)
+ RAID: Retrieval-Augmented Anomaly Detection [[CVPR 2026]](https://arxiv.org/abs/2602.19611)[[code]](https://github.com/Mingxiu-Cai/RAID)
+ Complementary Prototype Mapping for Efficient Multimodal Anomaly Detection [[CVPR 2026]](https://cvpr.thecvf.com/virtual/2026/poster/37601)
+ GPFlow: Gaussian Prototype Probability Flow for Unsupervised Multi-Modal Anomaly Detection [[CVPR 2026]](https://cvpr.thecvf.com/virtual/2026/poster/37603)
+ Hierarchical Point-Patch Fusion with Adaptive Patch Codebook for 3D Shape Anomaly Detection [[CVPR 2026]](https://arxiv.org/abs/2604.03972)[[code]](https://github.com/alexandor91/Shape-Anomaly-Codebook)
+ GS-CLIP: Zero-shot 3D Anomaly Detection by Geometry-Aware Prompt and Synergistic View Representation Learning [[CVPR 2026]](https://arxiv.org/abs/2602.19206)[[code]](https://github.com/zhushengxinyue/GS-CLIP)
+ Geometry-Aligned and Anomaly-Aware Reconstruction for 3D Anomaly Detection [[CVPR 2026]](https://cvpr.thecvf.com/virtual/2026/poster/36699)
+ Reasoning-Driven Anomaly Detection and Localization with Image-Level Supervision [[CVPR 2026]](https://arxiv.org/abs/2603.27179)[[code]](https://github.com/YizhouJin313/ReADL)
+ MMR-AD: A Large-Scale Multimodal Dataset for Benchmarking General Anomaly Detection with Multimodal Large Language Models [[CVPR 2026]](https://arxiv.org/abs/2604.10971)[[code]](https://xcyao00.github.io/MMR-AD)
+ ADSeeker: A Knowledge-Grounded Reasoning Framework for Industry Anomaly Detection and Reasoning [[CVPR 2026]](https://arxiv.org/abs/2508.03088)
+ Multi-Prototype Compactness and Boundary-Aware Synthesis for Unsupervised Anomaly Detection [[CVPR 2026]](https://cvpr.thecvf.com/virtual/2026/poster/37868)
+ Dual-Prototype-Guided Multi-task Learning for Unsupervised Anomaly Detection and Classification [[CVPR 2026]](https://cvpr.thecvf.com/virtual/2026/poster/38573)
+ Defect Cue-Preserved Structural Feature Refinement for Few-Shot Anomaly Detection [[CVPR 2026]](https://cvpr.thecvf.com/virtual/2026/poster/39808)
+ UniMMAD: Unified Multi-Modal and Multi-Class Anomaly Detection via MoE-Driven Feature Decompression [[CVPR 2026]](https://arxiv.org/abs/2509.25934)[[code]](https://github.com/yuanzhao-CVLAB/UniMMAD)
+ Omni-AD: A Large-scale and Versatile Benchmark for Industrial Anomaly Detection [[CVPR 2026]](https://cvpr.thecvf.com/virtual/2026/poster/39148)
+ From Attraction to Equilibrium: Physics-Inspired Semantic Gravitons for Zero-Shot Anomaly Detection [[CVPR 2026]](https://cvpr.thecvf.com/virtual/2026/poster/39782)
+ Anomaly as Non-Conformity via Training-Free Graph Laplacian Energy Minimization [[CVPR 2026]](https://cvpr.thecvf.com/virtual/2026/poster/38295)
+ A Semantically Disentangled Unified Model for Multi-category 3D Anomaly Detection [[CVPR 2026]](https://arxiv.org/abs/2603.25159)[[code]](https://visualsciencelab-khu.github.io/SeDiR_project)
+ Hyperbolic Defect Feature Synthesis for Few-Shot Defect Classification [[CVPR 2026]](https://cvpr.thecvf.com/virtual/2026/poster/40073)
+ UniSpector: Towards Universal Open-set Defect Recognition via Spectral-Contrastive Visual Prompting [[CVPR 2026]](https://cvpr.thecvf.com/virtual/2026/poster/38081)
+ Towards Open-Vocabulary Industrial Defect Understanding with a Large-Scale Multimodal Dataset [[CVPR 2026]](https://arxiv.org/abs/2512.24160)[[data]](https://ninaneon.github.io/projectpage)
+ Real-IAD MVN: A Multi-View Normal Vector Dataset and Benchmark for High-Fidelity Industrial Anomaly Detection [[CVPR 2026]](https://arxiv.org/abs/2605.07149)

## ICLR 2026
+ Foundation Visual Encoders Are Secretly Few-Shot Anomaly Detectors [[ICLR 2026]](https://arxiv.org/abs/2510.01934)[[code]](https://github.com/ymxlzgy/FoundAD)
+ MRAD: Zero-Shot Anomaly Detection with Memory-Driven Retrieval [[ICLR 2026]](https://arxiv.org/abs/2602.00522)
+ PIRN: Prototypical-based Intra-modal Reconstruction with Normality Communication for Multi-modal Anomaly Detection [[ICLR 2026]](https://openreview.net/forum?id=7L7kmHHfgf)
+ Dual Distillation for Few-Shot Anomaly Detection [[ICLR 2026]](https://openreview.net/forum?id=tRO6G20Qba)
+ Judo: A Juxtaposed Domain-oriented Multimodal Reasoner for Industrial Anomaly QA [[ICLR 2026]](https://openreview.net/forum?id=XW4mROtaVb)
+ MRAD: Zero-Shot Anomaly Detection with Memory-Driven Retrieval [[ICLR 2026]](https://openreview.net/forum?id=TQkFiW3AEX)[[code]](https://github.com/CROVO1026/MRAD)

## AAAI 2026
+ Towards High-Resolution 3D Anomaly Detection: A Scalable Dataset and Real-Time Framework for Subtle Industrial Defects [[AAAI 2026 oral]](https://arxiv.org/abs/2507.07435)[[code]](https://hustcyq.github.io/MiniShift-Simple3D/)
+ AdaptCLIP: Adapting CLIP for Universal Visual Anomaly Detection [[AAAI 2026]](https://arxiv.org/abs/2505.09926)[[code]](https://github.com/gaobb/AdaptCLIP)
+ AnomalyMoE: Towards a Language-free Generalist Model for Unified Visual Anomaly Detection [[AAAI 2026]](https://arxiv.org/abs/2508.06203)[[code]](https://github.com/CASIA-LMC-Lab/AnomalyMoE)
+ AnoStyler: Text-Driven Localized Anomaly Generation via Lightweight Style Transfer [[AAAI 2026]](https://arxiv.org/abs/2511.06687)[[code]](https://github.com/yulimso/AnoStyler)
+ Anomagic: Crossmodal Prompt-driven Zero-shot Anomaly Generation [[AAAI 2026]](https://arxiv.org/abs/2511.10020)[[code]](https://github.com/yuxin-jiang/Anomagic)
+ Commonality in Few: Few-Shot Multimodal Anomaly Detection via Hypergraph-Enhanced Memory [[AAAI 2026]](https://arxiv.org/abs/2511.05966)[[code]](https://github.com/Sunny5250/CIF)
+ IAD-R1: Reinforcing Consistent Reasoning in Industrial Anomaly Detection [[AAAI 2026]](https://arxiv.org/abs/2508.09178)[[code]](https://github.com/Yanhui-Lee/IAD-R1)
+ CASL: Curvature-Augmented Self-supervised Learning for 3D Anomaly Detection [[AAAI 2026]](https://arxiv.org/abs/2511.12909)[[code]](https://github.com/zyh16143998882/CASL)
+ MaskAD: Parallel Masked Autoencoder for Multi-class Unsupervised Anomaly Detection [[AAAI 2026]](https://ojs.aaai.org/index.php/AAAI/article/download/38573/42535)[[code]](https://github.com/liugang-xd/MaskAD)
+ CHIMERA:Controllable High-quality Image-Mask Extraction for Reliable Diffusion-Based Anomaly Synthesis [[AAAI 2026]](https://ojs.aaai.org/index.php/AAAI/article/view/37511)[[code]](https://github.com/cvlab-kaist/CHIMERA)
+ PromptMoE: Generalizable Zero-Shot Anomaly Detection via Visually-Guided Prompt Mixtures [[AAAI 2026]](https://arxiv.org/abs/2511.18116)[[code]](https://github.com/yourusername/PromptMoE)
+ Unsupervised Multi-View Visual Anomaly Detection via Progressive Homography-Guided Alignment [[AAAI 2026]](https://arxiv.org/abs/2511.18766)
+ AnomalyPainter: Vision-Language-Diffusion Synergy for Zero-Shot Realistic and Diverse Industrial Anomaly Synthesis [[AAAI 2026]](https://arxiv.org/abs/2503.07253)
+ Exploring High-order-aware Prompt Learning for Zero-shot Anomaly Detection [[AAAI 2026]](https://ojs.aaai.org/index.php/AAAI/article/view/38029)
+ RcAE: Recursive Reconstruction Framework for Unsupervised Industrial Anomaly Detection [[AAAI 2026]](https://arxiv.org/abs/2512.11284)
+ CADiff: Context-Aware Diffusion for Controllable Anomaly Generation in Anomaly Detection [[AAAI 2026]](https://ojs.aaai.org/index.php/AAAI/article/view/37917)
+ Quality-Aware Language-Conditioned Local Auto-Regressive Anomaly Synthesis and Detection [[AAAI 2026]](https://arxiv.org/abs/2508.03539)[[code]](https://github.com/neymarql/QARAD)
+ MAU-GPT: Enhancing Multi-type Industrial Anomaly Understanding via Anomaly-aware and Generalist Experts Adaptation [[AAAI 2026]](https://arxiv.org/abs/2602.07011)
+ SCoNE: Spherical Consistent Neighborhoods Ensemble for Effective and Efficient Multi-View Anomaly Detection [[AAAI 2026]](https://arxiv.org/abs/2512.05540)
+ Commonality in Few: Few-Shot Multimodal Anomaly Detection via Hypergraph-Enhanced Memory [[AAAI 2026]](https://arxiv.org/abs/2511.05966)[[code]](https://github.com/Sunny5250/CIF)
+ RPE-PAD: Relative Pose Estimation for Pose-agnostic Anomaly Detection [[AAAI 2026]](https://ojs.aaai.org/index.php/AAAI/article/view/38304)
+ AD-FM: Multimodal LLMs for Anomaly Detection via Multi-Stage Reasoning and Fine-Grained Reward Optimization [[AAAI 2026]](https://arxiv.org/abs/2508.04175)
+ FDP: A Frequency-Decomposition Preprocessing Pipeline for Unsupervised Anomaly Detection in Brain MRI [[AAAI 2026]](https://arxiv.org/abs/2511.12899)[[code]](https://github.com/ls1rius/MRI_FDP)

## NeurIPS 2025
+ FAST: Foreground-aware Diffusion with Accelerated Sampling Trajectory for Segmentation-oriented Anomaly Synthesis [[NeurIPS 2025]](https://arxiv.org/abs/2509.20295)[[code]](https://anonymous.4open.science/r/NeurIPS-938/README1.md)
+ Normal-Abnormal Guided Generalist Anomaly Detection [[NeurIPS 2025]](https://arxiv.org/abs/2510.00495)[[code]](https://github.com/JasonKyng/NAGL)
+ Registration is a Powerful Rotation-Invariance Learner for 3D Anomaly Detection [[NeurIPS 2025]](https://arxiv.org/abs/2510.16865)
+ ADPretrain: Advancing Industrial Anomaly Detection via Anomaly Representation Pretraining [[NeurIPS 2025]](https://arxiv.org/abs/2511.05245)[[code]](https://github.com/xcyao00/ADPretrain)

## KDD 2025
+ Self-Tuning Self-Supervised Image Anomaly Detection [[KDD 2025]](https://arxiv.org/abs/2306.12033) [[code]](https://github.com/jaeminyoo/ST-SSAD)
 + Logical Anomaly Detection with Text-based Logic via Component-Aware Contrastive Language-Image Training [[KDD 25]](https://dl.acm.org/doi/abs/10.1145/3711896.3737032)


<!-- ## ACM MM 2025
+ AF-CLIP: Zero-Shot Anomaly Detection via Anomaly-Focused CLIP Adaptation [[ACM MM 2025]](https://arxiv.org/abs/2507.19949)[[code]](https://github.com/Faustinaqq/AF-CLIP)
+ AnomalyControl: Highly-Aligned Anomalous Image Generation with Controlled Diffusion Model [[ACM MM 2025]](https://dl.acm.org/doi/abs/10.1145/3746027.3755274)
+ Taming Anomalies with Down-Up Sampling Networks: Group Center Preserving Reconstruction for 3D Anomaly Detection [[ACM MM 2025]](https://arxiv.org/abs/2507.03903v1)
+ Robust Modality-Incomplete Anomaly Detection: A Modality-Instructive Framework with Benchmark [[ACM MM 2025]](https://dl.acm.org/doi/abs/10.1145/3746027.3754766)
+ Exploring Multimodal Prompts For Unsupervised Continuous Anomaly Detection [[ACM MM 2025]](https://dl.acm.org/doi/abs/10.1145/3746027.3755219)
+ Learning Invariant Discriminative Patterns for Unified Anomaly Detection [[ACM MM 2025]](https://dl.acm.org/doi/abs/10.1145/3746027.3755179)
+ Uniad: Integrating geometric and semantic cues for unified anomaly detection [[ACM MM 2025]](https://dl.acm.org/doi/abs/10.1145/3746027.3755422) -->

## ICCV 2025
+ SeaS: Few-shot Industrial Anomaly Image Generation with Separation and Sharing Fine-tuning [[ICCV 2025]](https://arxiv.org/pdf/2410.14987)[[code]](https://github.com/HUST-SLOW/SeaS)
+ MultiADS: Defect-aware Supervision for Multi-type Anomaly Detection and Segmentation in Zero-Shot Learning [[ICCV 2025]](https://arxiv.org/abs/2504.06740)[[code]](https://github.com/boschresearch/MultiADS)
+ Towards Real Unsupervised Anomaly Detection Via Confident Meta-Learning [[ICCV 2025]](https://arxiv.org/abs/2508.02293)
+ DictAS: A Framework for Class-Generalizable Few-Shot Anomaly Segmentation via Dictionary Lookup [[ICCV 2025]](https://www.arxiv.org/abs/2508.13560)[[code]](https://github.com/xiaozhen228/DictAS)
+ SALAD -- Semantics-Aware Logical Anomaly Detection [[ICCV 2025]](https://arxiv.org/abs/2509.02101)[[code]](https://github.com/MaticFuc/SALAD)
+ Kaputt: A Large-Scale Dataset for Visual Defect Detection [[ICCV 2025]](https://arxiv.org/abs/2510.05903)[[data]](https://www.kaputt-dataset.com/)
+ G2SF: Geometry-Guided Score Fusion for Multimodal Industrial Anomaly Detection[[ICCV 2025]](https://openaccess.thecvf.com/content/ICCV2025/papers/Tao_G2SF_Geometry-Guided_Score_Fusion_for_Multimodal_Industrial_Anomaly_Detection_ICCV_2025_paper.pdf)[[code]](https://github.com/ctaoaa/G2SF)
+ FE-CLIP: Frequency Enhanced CLIP Model for Zero-Shot Anomaly Detection and Segmentation [[ICCV 2025]](https://openaccess.thecvf.com/content/ICCV2025/papers/Gong_FE-CLIP_Frequency_Enhanced_CLIP_Model_for_Zero-Shot_Anomaly_Detection_and_ICCV_2025_paper.pdf)
+ DecAD: Decoupling Anomalies in Latent Space for Multi-Class Unsupervised Anomaly Detection [[ICCV 2025]](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_DecAD_Decoupling_Anomalies_in_Latent_Space_for_Multi-Class_Unsupervised_Anomaly_ICCV_2025_paper.html)
+ Triad: Empowering LMM-based Anomaly Detection with Vision Expert-guided Visual Tokenizer and Manufacturing Process [[ICCV 2025]](https://arxiv.org/abs/2503.13184)[[code]](https://github.com/tzjtatata/Triad)
+ Fine-grained Abnormality Prompt Learning for Zero-shot Anomaly Detection [[ICCV 2025]](https://arxiv.org/abs/2410.10289)[[code]](https://github.com/mala-lab/FAPrompt)
+ Anomaly Detection of Integrated Circuits Package Substrates Using the Large Vision Model SAIC: Dataset Construction, Methodology, and Application [[ICCV 2025]](https://openaccess.thecvf.com/content/ICCV2025/papers/Yu_Anomaly_Detection_of_Integrated_Circuits_Package_Substrates_Using_the_Large_ICCV_2025_paper.pdf)[[data]](https://github.com/Bingyang0410/CPS2D-AD)
+ Debiasing Trace Guidance: Top-down Trace Distillation and Bottom-up Velocity Alignment for Unsupervised Anomaly Detection [[ICCV 2025]](https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_Debiasing_Trace_Guidance_Top-down_Trace_Distillation_and_Bottom-up_Velocity_Alignment_ICCV_2025_paper.pdf)
+ FIND: Few-Shot Anomaly Inspection with Normal-Only Multi-Modal Data [[ICCV 2025]](https://openaccess.thecvf.com/content/ICCV2025/papers/Li_FIND_Few-Shot_Anomaly_Inspection_with_Normal-Only_Multi-Modal_Data_ICCV_2025_paper.pdf)
+ Bridging 3D Anomaly Localization and Repair via High-Quality Continuous Geometric Representation [[ICCV 2025]](https://arxiv.org/abs/2505.24431)[[code]](https://github.com/ZZZBBBZZZ/PASDF)
+ SiM3D: Single-instance Multiview Multimodal and Multisetup 3D Anomaly Detection Benchmark [[ICCV 2025]](https://arxiv.org/abs/2506.21549)[[data]](https://alex-costanzino.github.io/SiM3D/)
+ Toward Long-Tailed Online Anomaly Detection through Class-Agnostic Concepts [[ICCV 2025]](https://arxiv.org/abs/2507.16946)[[data]](https://zenodo.org/records/16283853)
+ ReMP-AD: Retrieval-enhanced Multi-modal Prompt Fusion for Few-Shot Industrial Visual Anomaly Detection [[ICCV 2025]](https://openaccess.thecvf.com/content/ICCV2025/papers/Ma_ReMP-AD_Retrieval-enhanced_Multi-modal_Prompt_Fusion_for_Few-Shot_Industrial_Visual_Anomaly_ICCV_2025_paper.pdf)[[code]](https://github.com/cshcma/ReMP-AD)
+ RareCLIP: Rarity-aware Online Zero-shot Industrial Anomaly Detection [[ICCV 2025]](https://openaccess.thecvf.com/content/ICCV2025/papers/He_RareCLIP_Rarity-aware_Online_Zero-shot_Industrial_Anomaly_Detection_ICCV_2025_paper.pdf)[[code]](https://github.com/hjf02/RareCLIP)
+ Wave-MambaAD: Wavelet-driven State Space Model for Multi-class Unsupervised Anomaly Detection [[ICCV 2025]](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_Wave-MambaAD_Wavelet-driven_State_Space_Model_for_Multi-class_Unsupervised_Anomaly_Detection_ICCV_2025_paper.pdf)
+ Salvaging the Overlooked: Leveraging Class-Aware Contrastive Learning for Multi-Class Anomaly Detection [[ICCV 2025]](https://openaccess.thecvf.com/content/ICCV2025/papers/Fan_Salvaging_the_Overlooked_Leveraging_Class-Aware_Contrastive_Learning_for_Multi-Class_Anomaly_ICCV_2025_paper.pdf)[[code]](https://github.com/LGC-AD/AD-LGC)
+ Training-Free Industrial Defect Generation with Diffusion Models [[ICCV 2025]](https://openaccess.thecvf.com/content/ICCV2025/papers/Xu_Training-Free_Industrial_Defect_Generation_with_Diffusion_Models_ICCV_2025_paper.pdf)[[code]](https://github.com/rubymiaomiao/TF-IDG)

## ICML 2025
+ CostFilter-AD: Enhancing Anomaly Detection through Matching Cost Filtering [[ICML2025]](https://openreview.net/pdf?id=6p2wsBeYSs)[[code]](https://github.com/ZHE-SAPI/CostFilter-AD)
+ OmiAD: One-Step Adaptive Masked Diffusion Model for Multi-class Anomaly Detection via Adversarial Distillation [[ICML2025]](https://icml.cc/virtual/2025/poster/46291)
+ Demeaned Sparse: Efficient Anomaly Detection by Residual Estimate [[ICML2025]](https://icml.cc/virtual/2025/poster/45914)

<!-- ## IJCAI 2025
+ MC3D-AD: A Unified Geometry-aware Reconstruction Model for Multi-category 3D Anomaly Detection [[IJCAI 2025]](https://arxiv.org/abs/2505.01969)
+ ReplayCAD: Generative Diffusion Replay for Continual Anomaly Detection [[IJCAI 2025]](https://arxiv.org/abs/2505.06603)[[code]](https://github.com/HULEI7/ReplayCAD) -->

## CVPR 2025
+ Anomaly Anything: Promptable Unseen Visual Anomaly Generation [[CVPR 2025]](https://arxiv.org/abs/2406.01078)[[code]](https://github.com/EPFL-IMOS/AnomalyAny)
+ Real-IAD D<sup>3</sup>: A Real-World 2D/Pseudo-3D/3D Dataset for Industrial Anomaly Detection [[CVPR 2025]](https://arxiv.org/abs/2504.14221)
+ Distribution Prototype Diffusion Learning for Open-set Supervised Anomaly Detection [[CVPR 2025]](https://arxiv.org/abs/2502.20981)[[code]](https://github.com/fuyunwang/DPDL)
+ One-for-More: Continual Diffusion Model for Anomaly Detection [[CVPR 2025]](https://arxiv.org/abs/2502.19848)[[code]](https://github.com/FuNz-0/One-for-More)
+ Exploring Intrinsic Normal Prototypes within a Single Image for Universal Anomaly Detection [[CVPR 2025]](https://arxiv.org/abs/2503.02424)[[code]](https://github.com/luow23/INP-Former)
+ UniVAD: A Training-free Unified Model for Few-shot Visual Anomaly Detection [[CVPR 2025]](https://arxiv.org/abs/2412.03342)[[code]](https://uni-vad.github.io/#)
+ Towards Visual Discrimination and Reasoning of Real-World Physical Dynamics: Physics-Grounded Anomaly Detection [[CVPR 2025]](https://arxiv.org/abs/2503.03562)[[code]](https://github.com/Chopper-233/Physics-AD)
+ Odd-One-Out: Anomaly Detection by Comparing with Neighbors [[CVPR 2025]](https://arxiv.org/abs/2406.20099)[[code]](https://github.com/VICO-UoE/OddOneOutAD)
+ UniNet: A Contrastive Learning-guided Unified Framework with Feature Selection for Anomaly Detection [[CVPR 2025]](https://pangdatangtt.github.io/)[[code]](https://github.com/pangdatangtt/UniNet)
+ Towards Zero-Shot Anomaly Detection and Reasoning with Multimodal Large Language Models [[CVPR 2025]](https://arxiv.org/abs/2502.07601)[[code]](https://xujiacong.github.io/Anomaly-OV/)
+ MANTA: A Large-Scale Multi-View and Visual-Text Anomaly Detection Dataset for Tiny Objects [[CVPR 2025]](https://arxiv.org/abs/2412.04867)[[data]](https://grainnet.github.io/MANTA)
+ AA-CLIP: Enhancing Zero-shot Anomaly Detection via Anomaly-Aware CLIP [[CVPR 2025]](https://arxiv.org/pdf/2503.06661)[[code]](https://github.com/Mwxinnn/AA-CLIP)
+ AnomalyNCD: Towards Novel Anomaly Class Discovery in Industrial Scenarios [[CVPR 2025]](https://arxiv.org/abs/2410.14379)[[code]](https://github.com/HUST-SLOW/AnomalyNCD)
+ Towards Training-free Anomaly Detection with Vision and Language Foundation Models [[CVPR 2025]](https://arxiv.org/abs/2503.18325)[[code]](https://github.com/zhang0jhon/LogSAD)
+ TailedCore: Few-Shot Sampling for Unsupervised Long-Tail Noisy Anomaly Detection [[CVPR 2025]](https://jungyg.github.io/TailedCore_site/)[[code]](https://github.com/jungyg/TailedCore)
+ DualAnoDiff: Dual-Interrelated Diffusion Model for Few-Shot Anomaly Image Generation [[CVPR 2025]](https://arxiv.org/abs/2408.13509)[[code]](https://github.com/yinyjin/DualAnoDiff)
+ PO3AD: Predicting Point Offsets toward Better 3D Point Cloud Anomaly Detection [[CVPR 2025]](https://arxiv.org/abs/2412.12617)
+ Multi-Sensor Object Anomaly Detection: Unifying Appearance, Geometry, and Internal Properties [[CVPR 2025]](https://zzzbbbzzz.github.io/MulSen_AD/index.html)[[code]](https://github.com/ZZZBBBZZZ/MulSen-AD)
+ Bayesian Prompt Flow Learning for Zero-Shot Anomaly Detection [[CVPR 2025]](https://arxiv.org/abs/2503.10080)[[code coming soon]](https://github.com/xiaozhen228/Bayes-PFL)
+ DefectFill: Realistic Defect Generation with Inpainting Diffusion Model for Visual Inspection [[CVPR 2025]](https://arxiv.org/abs/2503.13985)
+ Correcting Deviations from Normality: A Reformulated Diffusion Model for Multi-Class Unsupervised Anomaly Detection [[CVPR 2025]](https://arxiv.org/abs/2503.19357)[[code]](https://github.com/farzad-bz/DeCo-Diff)
+ Dinomaly: The Less is More Philosophy in Multi-Class Unsupervised Anomaly Detection [[CVPR 2025]](https://arxiv.org/abs/2405.14325)[[code]](https://github.com/guojiajeremy/Dinomaly)
+ A Unified Latent Schrödinger Bridge Diffusion Model for Unsupervised Anomaly Detection and Localization[[CVPR 2025]](https://openaccess.thecvf.com/content/CVPR2025/html/Akshay_A_Unified_Latent_Schrodinger_Bridge_Diffusion_Model_for_Unsupervised_Anomaly_CVPR_2025_paper.html)[[code]](https://github.com/ShilhoraAkshayPatel/LASB)
+ DFM: Differentiable Feature Matching for Anomaly Detection[[CVPR 2025]](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_DFM_Differentiable_Feature_Matching_for_Anomaly_Detection_CVPR_2025_paper.html)
+ Correcting Deviations from Normality: A Reformulated Diffusion Model for Multi-Class Unsupervised Anomaly Detection[[CVPR 2025]](https://openaccess.thecvf.com/content/CVPR2025/html/Beizaee_Correcting_Deviations_from_Normality_A_Reformulated_Diffusion_Model_for_Multi-Class_CVPR_2025_paper.html)[[code]](https://github.com/farzad-bz/DeCo-Diff)
+ Beyond Single-Modal Boundary: Cross-Modal Anomaly Detection through Visual Prototype and Harmonization[[CVPR 2025]](https://openaccess.thecvf.com/content/CVPR2025/html/Mao_Beyond_Single-Modal_Boundary_Cross-Modal_Anomaly_Detection_through_Visual_Prototype_and_CVPR_2025_paper.html)[[code]](https://github.com/Kerio99/CMAD)
+ PatchGuard: Adversarially Robust Anomaly Detection and Localization through Vision Transformers and Pseudo Anomalies[[CVPR 2025]](https://openaccess.thecvf.com/content/CVPR2025/html/Nafez_PatchGuard_Adversarially_Robust_Anomaly_Detection_and_Localization_through_Vision_Transformers_CVPR_2025_paper.html)[[code]](https://github.com/rohban-lab/PatchGuard)
+ Wavelet and Prototype Augmented Query-based Transformer for Pixel-level Surface Defect Detection[[CVPR 2025]](https://openaccess.thecvf.com/content/CVPR2025/html/Yan_Wavelet_and_Prototype_Augmented_Query-based_Transformer_for_Pixel-level_Surface_Defect_CVPR_2025_paper.html)[[code]](https://github.com/yfhdm/WPFormer)
+ VAND 3.0: Visual Anomaly and Novelty Detection - 3rd Edition [[CVPR 2025W]](https://sites.google.com/view/vand30cvpr2025)
+ Feature Attenuation of Defective Representation Can Resolve Incomplete Masking on Anomaly Detection [[CVPR 2025 VAND 3.0 Workshop]](https://arxiv.org/abs/2407.04597)  
+ RoBiS: Robust Binary Segmentation for High-Resolution Industrial Images [[CVPR 2025 VAND 3.0 Workshop]](https://arxiv.org/abs/2505.21152)[[code]](https://github.com/xrli-U/RoBiS)
+ When Textures Deceive: Weakly Supervised Industrial Anomaly Detection with Adapted-Loss (AL-CycleGAN) [[CVPR 2025 VAND Workshop]](https://openaccess.thecvf.com/content/CVPR2025W/VAND/papers/Nakkina_When_Textures_Deceive_Weakly_Supervised_Industrial_Anomaly_Detection_with_Adapted-Loss_CVPRW_2025_paper.pdf)[[code]](https://github.com/ganatma/AL-CycleGAN)[[data / MCBT]](https://github.com/ganatma/AL-CycleGAN)
+ AnomalyHybrid: A Domain-agnostic Generative Framework for General Anomaly Detection [[CVPR 2025 SyntaGen Workshop]](https://openaccess.thecvf.com/content/CVPR2025W/SyntaGen/papers/Zhao_AnomalyHybrid_A_Domain-agnostic_Generative_Framework_for_General_Anomaly_Detection_CVPRW_2025_paper.pdf)  

<!-- ## ICLR 2025
+ MMAD: The Comprehensive Benchmark for Multimodal Large Language Models in Industrial Anomaly Detection [[ICLR 2025]](https://openreview.net/forum?id=JDiER86r8v)[[Code]](https://github.com/jam-cc/MMAD)  [[Data]](https://huggingface.co/datasets/jiang-cc/MMAD)
+ One-for-All Few-Shot Anomaly Detection via Instance-Induced Prompt Learning [[ICLR 2025]](https://openreview.net/forum?id=Zzs3JwknAY) 
+ Language-Assisted Feature Transformation for Anomaly Detection [[ICLR 2025]](https://openreview.net/forum?id=2p03KljxE9)
+ Adversarially Robust Anomaly Detection through Spurious Negative Pair Mitigation [[ICLR 2025]](https://openreview.net/forum?id=t8fu5m8R5m)


## AAAI 2025
+ MVREC: A General Few-shot Defect Classification Model Using Multi-View Region-Context [[AAAI 2025]](https://arxiv.org/abs/2412.16897)
+ Revisiting Multimodal Fusion for 3D Anomaly Detection from an Architectural Perspective [[AAAI 2025]](https://arxiv.org/abs/2412.17297)
+ KAG-prompt: Kernel-Aware Graph Prompt Learning for Few-Shot Anomaly Detection [[AAAI 2025]](https://arxiv.org/abs/2412.17619)[[code]](https://github.com/CVL-hub/KAG-prompt)
+ FiCo: Filter or Compensate: Towards Invariant Representation from Distribution Shift for Anomaly Detection [[AAAI 2025]](https://arxiv.org/abs/2412.10115)[[code]](https://github.com/znchen666/FiCo)
+ CKAAD: Boosting Fine-Grained Visual Anomaly Detection with Coarse-Knowledge-Aware Adversarial Learning [[AAAI 2025]](https://arxiv.org/abs/2412.12850)[[code]](https://github.com/Faustinaqq/CKAAD)
+ CNC: Cross-modal Normality Constraint for Unsupervised Multi-class Anomaly Detection [[AAAI 2025]](https://arxiv.org/abs/2501.00346)[[code]](https://github.com/cvddl/CNC)
+ LogicAD: Explainable Anomaly Detection via VLM-based Text Feature Extraction [[AAAI 2025]](https://arxiv.org/abs/2501.01767)[[code]](https://github.com/jasonjin34/logicAD)
+ Look Inside for More: Internal Spatial Modality Perception for 3D Anomaly Detection [[AAAI 2025]](https://arxiv.org/abs/2412.13461)[[code]](https://github.com/M-3LAB/Look-Inside-for-More)
+ Unlocking the Potential of Reverse Distillation for Anomaly Detection [[AAAI 2025]](https://arxiv.org/abs/2412.07579)[[code]](https://github.com/hito2448/URD)
+ Promptable Anomaly Segmentation with SAM Through Self-Perception Tuning [[AAAI 2025]](https://arxiv.org/abs/2411.17217)[[code]](https://github.com/THU-MIG/SAM-SPT)
+ 3CAD: A Large-Scale Real-World 3C Product Dataset for Unsupervised Anomaly [[AAAI 2025]](https://arxiv.org/abs/2502.05761)[[code]](https://github.com/EnquanYang2022/3CAD) -->


<!--- 

## NeurIPS 2024
+ MambaAD: Exploring State Space Models for Multi-class Unsupervised Anomaly Detection [[NeurIPS 2024]](https://arxiv.org/abs/2404.06564)[[code]](https://lewandofskee.github.io/projects/MambaAD/)
+ PointAD: Comprehending 3D Anomalies from Points and Pixels for Zero-shot 3D Anomaly Detection [[NeurIPS 2024]](https://arxiv.org/abs/2410.00320)[[code]](https://github.com/zqhang/PointAD)
+ CableInspect-AD: An Expert-Annotated Anomaly Detection Dataset [[NeurIPS 2024]](https://arxiv.org/abs/2409.20353)[[data]](https://mila-iqia.github.io/cableinspect-ad/)
+ ResAD: A Simple Framework for Class Generalizable Anomaly Detection [[NeurIPS 2024]](https://arxiv.org/abs/2410.20047)[[code]](https://github.com/xcyao00/ResAD)
+ One-to-Normal: Anomaly Personalization for Few-shot Anomaly Detection [[NeurIPS 2024]](https://openreview.net/pdf?id=tIzW3l2uaN)
+ MetaUAS: Universal Anomaly Segmentation with One-Prompt Meta-Learning [[NeurIPS 2024]](https://arxiv.org/abs/2505.09265)[[code]](https://github.com/gaobb/MetaUAS)

## ECCV 2024
+ R3D-AD: Reconstruction via Diffusion for 3D Anomaly Detection [[ECCV 2024]](https://arxiv.org/abs/2407.10862)[[homepage]](https://zhouzheyuan.github.io/r3d-ad)
+ An Incremental Unified Framework for Small Defect Inspection [[ECCV 2024]](https://arxiv.org/abs/2312.08917v2)[[code]](https://github.com/jqtangust/IUF)
+ Learning Unified Reference Representation for Unsupervised Multi-class Anomaly Detection [[ECCV 2024]](https://arxiv.org/abs/2403.11561)[[code]](https://github.com/hlr7999/RLR)
+ Self-supervised Feature Adaptation for 3D Industrial Anomaly Detection [[ECCV 2024]](https://arxiv.org/abs/2401.03145)
+ Learning to Detect Multi-class Anomalies with Just One Normal Image Prompt [[ECCV 2024]](https://arxiv.org/abs/2505.09264)[[code]](https://github.com/gaobb/OneNIP)
+ Few-Shot Anomaly-Driven Generation for Anomaly Classification and Segmentation [[ECCV 2024]](https://csgaobb.github.io/Pub_files/ECCV2024_AnoGen_CR_0730_Mobile.pdf)[[code]](https://github.com/gaobb/AnoGen)
+ AdaCLIP: Adapting CLIP with Hybrid Learnable Prompts for Zero-Shot Anomaly Detection [[ECCV 2024]](https://arxiv.org/abs/2407.15795)[[code]](https://github.com/caoyunkang/AdaCLIP)
+ GLAD: Towards Better Reconstruction with Global and Local Adaptive Diffusion Models for Unsupervised Anomaly Detection [[ECCV 2024]](https://arxiv.org/abs/2406.07487)[[code]](https://github.com/hyao1/GLAD)
+ GeneralAD: Anomaly Detection Across Domains by Attending to Distorted Features [[ECCV 2024]](https://arxiv.org/abs/2407.12427)[[code]](https://github.com/LucStrater/GeneralAD)
+ VCP-CLIP: A visual context prompting model for zero-shot anomaly segmentation [[ECCV 2024]](https://arxiv.org/abs/2407.12276)[[code]](https://github.com/xiaozhen228/VCP-CLIP)
+ A Unified Anomaly Synthesis Strategy with Gradient Ascent for Industrial Anomaly Detection and Localization [[ECCV 2024]](https://arxiv.org/abs/2407.09359)[[code]](https://github.com/cqylunlun/GLASS)
+ Hierarchical Gaussian Mixture Normalizing Flow Modeling for Unified Anomaly Detection [[ECCV 2024]](https://arxiv.org/abs/2403.13349)[[code]](https://github.com/xcyao00/HGAD)
+ TransFusion -- A Transparency-Based Diffusion Model for Anomaly Detection [[ECCV 2024]](https://arxiv.org/abs/2311.09999)[[code]](https://github.com/MaticFuc/ECCV_TransFusion)
+ Continuous Memory Representation for Anomaly Detection [[ECCV 2024]](https://arxiv.org/abs/2402.18293)[[homepage]](https://tae-mo.github.io/crad/)[[code]](https://github.com/tae-mo/CRAD)
+ Defect Spectrum: A Granular Look of Large-Scale Defect Datasets with Rich Semantics [[ECCV 2024]](https://openreview.net/forum?id=RLhS1TrjK3)[[data]](https://github.com/EnVision-Research/Defect_Spectrum)
+ AD3: Introducing a score for Anomaly Detection Dataset Difficulty assessment using VIADUCT dataset [[ECCV 2024]](https://eccv.ecva.net/virtual/2024/poster/2287)[[data]](https://fordatis.fraunhofer.de/handle/fordatis/363.2)
+ Learning Diffusion Models for Multi-View Anomaly Detection [[ECCV 2024]](https://eccv2024.ecva.net/virtual/2024/poster/1911)
+ MoEAD: A Parameter-efficient Model for Multi-class Anomaly Detection [[ECCV 2024]](https://eccv2024.ecva.net/virtual/2024/poster/2653)[[code]](https://github.com/TheStarOfMSY/MoEAD)
+ Unsupervised, Online and On-The-Fly Anomaly Detection For Non-Stationary Image Distributions [[ECCV 2024]](https://eccv2024.ecva.net/virtual/2024/poster/2289)[[code]](https://github.com/DeclanMcIntosh/Online_InReaCh)
+ Tackling Structural Hallucination in Image Translation with Local Diffusion [[ECCV 2024 oral]](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/10498.pdf)[[code]](https://github.com/edshkim98/LocalDiffusion-Hallucination)


## ACM MM 2024
+ FiLo: Zero-Shot Anomaly Detection by Fine-Grained Description and High-Quality Localization [[ACM MM 2024]](https://arxiv.org/abs/2404.13671)[[code]](https://github.com/CASIA-IVA-Lab/FiLo)
+ Dual-Modeling Decouple Distillation for Unsupervised Anomaly Detection [[ACM MM 2024]](https://arxiv.org/abs/2408.03888)
+ FOCT: Few-shot Industrial Anomaly Detection with Foreground-aware Online Conditional Transport [[ACM MM 2024]](https://dl.acm.org/doi/10.1145/3664647.3680771)
+ Towards High-resolution 3D Anomaly Detection via Group-Level Feature Contrastive Learning [[ACM MM 2024]](https://arxiv.org/abs/2408.04604)[[code]](https://github.com/M-3LAB/Group3AD)

## CVPR 2024
+ Text-Guided Variational Image Generation for Industrial Anomaly Detection and Segmentation [[CVPR 2024]](https://arxiv.org/abs/2403.06247)[[code]](https://github.com/MingyuLee82/TGI_AD_v1)
+ RealNet: A Feature Selection Network with Realistic Synthetic Anomaly for Anomaly Detection [[CVPR 2024]](https://arxiv.org/abs/2403.05897)[[code]](https://github.com/cnulab/RealNet)
+ Toward Generalist Anomaly Detection via In-context Residual Learning with Few-shot Sample Prompts [[CVPR 2024]](https://arxiv.org/abs/2403.06495)[[code]](https://github.com/mala-lab/InCTRL)
+ Multimodal Industrial Anomaly Detection by Crossmodal Feature Mapping [[CVPR 2024]](https://arxiv.org/abs/2312.04521)
+ Towards Scalable 3D Anomaly Detection and Localization: A Benchmark via 3D Anomaly Synthesis and A Self-Supervised Learning Network [[CVPR 2024]](https://arxiv.org/abs/2311.14897)[[code]](https://github.com/Chopper-233/Anomaly-ShapeNet)
+ Real-IAD: A Real-World Multi-view Dataset for Benchmarking Versatile Industrial Anomaly Detection [[CVPR 2024]](https://arxiv.org/abs/2403.12580)[[code]](https://github.com/TencentYoutuResearch/AnomalyDetection_Real-IAD)[[data]](https://realiad4ad.github.io/Real-IAD/)
+ Long-Tailed Anomaly Detection with Learnable Class Names [[CVPR 2024]](https://arxiv.org/abs/2403.20236)[[data split]](https://zenodo.org/records/10854201)
+ PromptAD: Learning Prompts with only Normal Samples for Few-Shot Anomaly Detection [[CVPR 2024]](https://arxiv.org/abs/2404.05231)[[code]](https://github.com/FuNz-0/PromptAD)
+ Supervised Anomaly Detection for Complex Industrial Images [[CVPR 2024]](https://openaccess.thecvf.com/content/CVPR2024/html/Baitieva_Supervised_Anomaly_Detection_for_Complex_Industrial_Images_CVPR_2024_paper.html)[[code]](https://github.com/abc-125/segad)
+ Anomaly Heterogeneity Learning for Open-set Supervised Anomaly Detection [[CVPR 2024]](https://arxiv.org/abs/2310.12790)[[code]](https://github.com/mala-lab/AHL)
+ Prompt-enhanced Multiple Instance Learning for Weakly Supervised Anomaly Detection [[CVPR 2024]](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_Prompt-Enhanced_Multiple_Instance_Learning_for_Weakly_Supervised_Video_Anomaly_Detection_CVPR_2024_paper.html)[[code]](https://github.com/Junxi-Chen/PE-MIL)
+ Looking 3D: Anomaly Detection with 2D-3D Alignment [[CVPR 2024]](https://openaccess.thecvf.com/content/CVPR2024/html/Bhunia_Looking_3D_Anomaly_Detection_with_2D-3D_Alignment_CVPR_2024_paper.html)[[homepage]](https://groups.inf.ed.ac.uk/vico/research/Looking3D)[[code]](https://github.com/VICO-UoE/Looking3D)
+ CVPRW: VAND 2.0: Visual Anomaly and Novelty Detection - 2nd Edition [[Challenge and Call for Papers]](https://sites.google.com/view/vand-2-0-cvpr-2024/home)
+ Divide and Conquer: High-Resolution Industrial Anomaly Detection via Memory Efficient Tiled Ensemble [[CVPR 24 Visual Anomaly Detection Workshop]](https://arxiv.org/abs/2403.04932)[[homepage]](https://summerofcode.withgoogle.com/archive/2023/projects/WUSjdxGl)

## ICASSP 2024
+ Implicit Foreground-Guided Network for Anomaly Detection and Localization [[ICASSP 2024]](https://ieeexplore.ieee.org/abstract/document/10446952)
+ Neural Network Training Strategy To Enhance Anomaly Detection Performance: A Perspective On Reconstruction Loss Amplification [[ICASSP 2024]](https://ieeexplore.ieee.org/document/10446942)
+ Patch-Wise Augmentation for Anomaly Detection and Localization [[ICASSP 2024]](https://ieeexplore.ieee.org/document/10446994)
+ A Reconstruction-Based Feature Adaptation for Anomaly Detection with Self-Supervised Multi-Scale Aggregation [[ICASSP 2024]](https://ieeexplore.ieee.org/document/10446766)
+ Feature-Constrained and Attention-Conditioned Distillation Learning for Visual Anomaly Detection [[ICASSP 2024]](https://ieeexplore.ieee.org/document/10448432)
+ CAGEN: Controllable Anomaly Generator using Diffusion Model [[ICASSP 2024]](https://ieeexplore.ieee.org/document/10447663)
+ Mixed-Attention Auto Encoder for Multi-Class Industrial Anomaly Detection [[ICASSP 2024]](https://ieeexplore.ieee.org/document/10446794)

## ICLR 2024
+ AnomalyCLIP: Object-agnostic Prompt Learning for Zero-shot Anomaly Detection [[ICLR 2024]](https://openreview.net/forum?id=buC4E91xZE)[[code]](https://github.com/zqhang/AnomalyCLIP)
+ MuSc: Zero-Shot Industrial Anomaly Classification and Segmentation with Mutual Scoring of the Unlabeled Images[[ICLR 2024]](https://openreview.net/forum?id=AHgc5SMdtd)[[code]](https://github.com/xrli-U/MuSc)][[2025 v2]](https://arxiv.org/abs/2511.10047)

## AAAI 2024
+ Rethinking Reverse Distillation for Multi-Modal Anomaly Detection [[AAAI 2024]](https://ojs.aaai.org/index.php/AAAI/article/view/28687)
+ Unsupervised Continual Anomaly Detection with Contrastively-learned Prompt [[AAAI 2024]](https://ojs.aaai.org/index.php/AAAI/article/view/28153)[[code]](https://github.com/shirowalker/UCAD)
+ Few Shot Part Segmentation Reveals Compositional Logic for Industrial Anomaly Detection [[AAAI 2024]](https://ojs.aaai.org/index.php/AAAI/article/view/28703)[[code]](https://github.com/oopil/PSAD_logical_anomaly_detection)
+ DiAD: A Diffusion-based Framework for Multi-class Anomaly Detection [[AAAI 2024]](https://ojs.aaai.org/index.php/AAAI/article/view/28690)[[code]](https://lewandofskee.github.io/projects/diad)
+ Generating and Reweighting Dense Contrastive Patterns for Unsupervised Anomaly Detection [[AAAI 2024]](https://ojs.aaai.org/index.php/AAAI/article/view/27910)
+ AnomalyDiffusion: Few-Shot Anomaly Image Generation with Diffusion Model [[AAAI 2024]](https://ojs.aaai.org/index.php/AAAI/article/view/28696)[[code]](https://github.com/sjtuplayer/anomalydiffusion)
+ AnomalyGPT: Detecting Industrial Anomalies using Large Vision-Language Models [[AAAI 2024]](https://ojs.aaai.org/index.php/AAAI/article/view/27963)[[code]](https://github.com/CASIA-IVA-Lab/AnomalyGPT)[[project page]](https://anomalygpt.github.io/)
+ A Comprehensive Augmentation Framework for Anomaly Detection [[AAAI 2024]](https://ojs.aaai.org/index.php/AAAI/article/view/28720)


## WACV 2024
+ ReConPatch: Contrastive Patch Representation Learning for Industrial Anomaly Detection [[WACV 2024]](https://openaccess.thecvf.com/content/WACV2024/papers/Hyun_ReConPatch_Contrastive_Patch_Representation_Learning_for_Industrial_Anomaly_Detection_WACV_2024_paper.pdf)
+ Learning Transferable Representations for Image Anomaly Localization Using Dense Pretraining [[WACV 2024]](https://openaccess.thecvf.com/content/WACV2024/papers/He_Learning_Transferable_Representations_for_Image_Anomaly_Localization_Using_Dense_Pretraining_WACV_2024_paper.pdf)[[code]](https://github.com/terrlo/DS2)
+ EfficientAD: Accurate Visual Anomaly Detection at Millisecond-Level Latencies [[WACV 2024]](https://openaccess.thecvf.com/content/WACV2024/papers/Batzner_EfficientAD_Accurate_Visual_Anomaly_Detection_at_Millisecond-Level_Latencies_WACV_2024_paper.pdf)
+ Contextual Affinity Distillation for Image Anomaly Detection [[WACV 2024]](https://openaccess.thecvf.com/content/WACV2024/papers/Zhang_Contextual_Affinity_Distillation_for_Image_Anomaly_Detection_WACV_2024_paper.pdf)
+ Attention Modules Improve Image-Level Anomaly Detection for Industrial Inspection: A DifferNet Case Study [[WACV 2024]](https://openaccess.thecvf.com/content/WACV2024/papers/Vieira_e_Silva_Attention_Modules_Improve_Image-Level_Anomaly_Detection_for_Industrial_Inspection_A_WACV_2024_paper.pdf)
+ PromptAD: Zero-shot Anomaly Detection using Text Prompts [[WACV 2024]](https://openaccess.thecvf.com/content/WACV2024/papers/Li_PromptAD_Zero-Shot_Anomaly_Detection_Using_Text_Prompts_WACV_2024_paper.pdf)
+ High-Fidelity Zero-Shot Texture Anomaly Localization Using Feature Correspondence Analysis [[WACV 2024]](https://openaccess.thecvf.com/content/WACV2024/html/Ardelean_High-Fidelity_Zero-Shot_Texture_Anomaly_Localization_Using_Feature_Correspondence_Analysis_WACV_2024_paper.html)
+ Cheating Depth: Enhancing 3D Surface Anomaly Detection via Depth Simulation [[WACV 2024]](https://openaccess.thecvf.com/content/WACV2024/papers/Zavrtanik_Cheating_Depth_Enhancing_3D_Surface_Anomaly_Detection_via_Depth_Simulation_WACV_2024_paper.pdf)[[code]](https://github.com/VitjanZ/3DSR)

## NeurIPS 2023
+ Real3D-AD: A Dataset of Point Cloud Anomaly Detection [[NeurIPS 2023]](https://openreview.net/pdf?id=zGthDp4yYe)[[code]](https://github.com/M-3LAB/Real3D-AD)[[中文]](https://blog.csdn.net/m0_63828250/article/details/136667168)
+ PAD: A Dataset and Benchmark for Pose-agnostic Anomaly Detection [[NeurIPS 2023]](https://openreview.net/pdf?id=kxFKgqwFNk)[[code]](https://github.com/EricLee0224/PAD)
+ Zero-Shot Anomaly Detection via Batch Normalization [[NeurIPS 2023]](https://openreview.net/pdf?id=d1wjMBYbP1)[[code]](https://github.com/aodongli/zero-shot-ad-via-batch-norm)
+ SANFlow: Semantic-Aware Normalizing Flow for Anomaly Detection and Localization [[NeurIPS 2023]](https://openreview.net/pdf?id=BqZ70BEtuW)
+ Energy-Based Models for Anomaly Detection: A Manifold Diffusion Recovery Approach [[NeurIPS 2023]](https://openreview.net/pdf?id=4nSDDokpfK)
+ Hierarchical Vector Quantized Transformer for Multi-class Unsupervised Anomaly Detection [[NeurIPS 2023]](https://openreview.net/pdf?id=clJTNssgn6)[[code]](https://github.com/RuiyingLu/HVQ-Trans)
+ ReContrast: Domain-Specific Anomaly Detection via Contrastive Reconstruction [[NeurIPS 2023]](https://openreview.net/pdf?id=KYxD9YCQBH)[[code]](https://github.com/guojiajeremy/ReContrast)

## ICML 2023
+ Shape-Guided Dual-Memory Learning for 3D Anomaly Detection [[ICML 2023]](https://openreview.net/forum?id=IkSGn9fcPz)
+ Fascinating Supervisory Signals and Where to Find Them: Deep Anomaly Detection with Scale Learning [[ICML 2023]](https://openreview.net/forum?id=V6PNBRWRil)

## ACM MM 2023
+ EasyNet: An Easy Network for 3D Industrial Anomaly Detection [[ACM MM 2023]](https://arxiv.org/abs/2307.13925)

## ICCV 2023
+ Remembering Normality: Memory-guided Knowledge Distillation for Unsupervised Anomaly Detection [[ICCV 2023]](https://openaccess.thecvf.com/content/ICCV2023/papers/Gu_Remembering_Normality_Memory-guided_Knowledge_Distillation_for_Unsupervised_Anomaly_Detection_ICCV_2023_paper.pdf)
+ Unsupervised Surface Anomaly Detection with Diffusion Probabilistic Model [[ICCV 2023]](https://openaccess.thecvf.com/content/ICCV2023/papers/Zhang_Unsupervised_Surface_Anomaly_Detection_with_Diffusion_Probabilistic_Model_ICCV_2023_paper.pdf)
+ PNI: Industrial Anomaly Detection using Position and Neighborhood Information [[ICCV 2023]](https://openaccess.thecvf.com/content/ICCV2023/papers/Bae_PNI__Industrial_Anomaly_Detection_using_Position_and_Neighborhood_Information_ICCV_2023_paper.pdf)[[code]](https://github.com/wogur110/PNI_Anomaly_Detection)
+ Anomaly Detection using Score-based Perturbation Resilience [[ICCV 2023]](https://openaccess.thecvf.com/content/ICCV2023/papers/Shin_Anomaly_Detection_using_Score-based_Perturbation_Resilience_ICCV_2023_paper.pdf)
+ Template-guided Hierarchical Feature Restoration for Anomaly Detection [[ICCV 2023]](https://openaccess.thecvf.com/content/ICCV2023/papers/Guo_Template-guided_Hierarchical_Feature_Restoration_for_Anomaly_Detection_ICCV_2023_paper.pdf)
+ Focus the Discrepancy: Intra- and Inter-Correlation Learning for Image Anomaly Detection [[ICCV 2023]](https://openaccess.thecvf.com/content/ICCV2023/papers/Yao_Focus_the_Discrepancy_Intra-_and_Inter-Correlation_Learning_for_Image_Anomaly_ICCV_2023_paper.pdf)[[code]](https://github.com/xcyao00/FOD)
+ Anomaly Detection under Distribution Shift [[ICCV 2023]](https://openaccess.thecvf.com/content/ICCV2023/papers/Cao_Anomaly_Detection_Under_Distribution_Shift_ICCV_2023_paper.pdf)[[code]](https://github.com/mala-lab/ADShift)
+ FastRecon: Few-shot Industrial Anomaly Detection via Fast Feature Reconstruction [[ICCV 2023]](https://openaccess.thecvf.com/content/ICCV2023/papers/Fang_FastRecon_Few-shot_Industrial_Anomaly_Detection_via_Fast_Feature_Reconstruction_ICCV_2023_paper.pdf)[[code]](https://github.com/FzJun26th/FastRecon)
+ Inter-Realization Channels: Unsupervised Anomaly Detection Beyond One-Class Classification [[ICCV 2023]](https://openaccess.thecvf.com/content/ICCV2023/papers/McIntosh_Inter-Realization_Channels_Unsupervised_Anomaly_Detection_Beyond_One-Class_Classification_ICCV_2023_paper.pdf)[[code]](https://github.com/DeclanMcIntosh/InReaCh)
+ Removing Anomalies as Noises for Industrial Defect Localization [[ICCV 2023]](https://openaccess.thecvf.com/content/ICCV2023/papers/Lu_Removing_Anomalies_as_Noises_for_Industrial_Defect_Localization_ICCV_2023_paper.pdf)


## MLLM related
+ Myriad: Large Multimodal Model by Applying Vision Experts for Industrial Anomaly Detection [[2023]](https://arxiv.org/abs/2310.19070)[[code]](https://github.com/tzjtatata/Myriad)
+ AnomalyGPT: Detecting Industrial Anomalies using Large Vision-Language Models [[AAAI 2024]](https://arxiv.org/abs/2308.15366)[[code]](https://github.com/CASIA-IVA-Lab/AnomalyGPT)[[project page]](https://anomalygpt.github.io/)
+ The Dawn of LMMs: Preliminary Explorations with GPT-4V(ision) [[2023 Section 9.2]](https://arxiv.org/abs/2309.17421)
+ Towards Generic Anomaly Detection and Understanding: Large-scale Visual-linguistic Model (GPT-4V) Takes the Lead [[2023]](https://arxiv.org/abs/2311.02782)[[code]](https://github.com/caoyunkang/GPT4V-for-Generic-Anomaly-Detection)
+ Exploring Grounding Potential of VQA-oriented GPT-4V for Zero-shot Anomaly Detection [[2023]](https://arxiv.org/abs/2311.02612)[[code]](https://github.com/zhangzjn/GPT-4V-AD)
+ Customizing Visual-Language Foundation Models for Multi-modal Anomaly Detection and Reasoning [[2024]](https://arxiv.org/abs/2403.11083)
+ Do LLMs Understand Visual Anomalies? Uncovering LLM Capabilities in Zero-shot Anomaly Detection [[2024]](https://arxiv.org/abs/2404.09654)
+ LogiCode: an LLM-Driven Framework for Logical Anomaly Detection [[2024]](https://arxiv.org/pdf/2406.04687)
+ FabGPT: An Efficient Large Multimodal Model for Complex Wafer Defect Knowledge Queries [[ICCAD 2024]](https://arxiv.org/abs/2407.10810)
+ VMAD: Visual-enhanced Multimodal Large Language Model for Zero-Shot Anomaly Detection [[2024]](https://arxiv.org/abs/2409.20146)
+ Are Anomaly Scores Telling the Whole Story? A Benchmark for Multilevel Anomaly Detection [[2024]](https://arxiv.org/abs/2411.14515)
+ MMAD: The Comprehensive Benchmark for Multimodal Large Language Models in Industrial Anomaly Detection [[ICLR 2025]](https://openreview.net/forum?id=JDiER86r8v)[[Code]](https://github.com/jam-cc/MMAD)  [[Data]](https://huggingface.co/datasets/jiang-cc/MMAD)
+ Can Multimodal Large Language Models be Guided to Improve Industrial Anomaly Detection? [[2025]](https://arxiv.org/abs/2501.15795)
+ EIAD: Explainable Industrial Anomaly Detection Via Multi-Modal Large Language Models [[ICME 2025]](https://arxiv.org/abs/2503.14162v1)
+ Towards Zero-Shot Anomaly Detection and Reasoning with Multimodal Large Language Models [[CVPR 2025]](https://arxiv.org/abs/2502.07601)[[code]](https://xujiacong.github.io/Anomaly-OV/)
+ AnomalyR1: A GRPO-based End-to-end MLLM for Industrial Anomaly Detection [[2025]](https://arxiv.org/abs/2504.11914)
+ Detect, Classify, Act: Categorizing Industrial Anomalies with Multi-Modal Large Language Models [[2025]](https://arxiv.org/abs/2505.02626)
+ Triad: Empowering LMM-based Anomaly Detection with Vision Expert-guided Visual Tokenizer and Manufacturing Process [[ICCV 2025]](https://openaccess.thecvf.com/content/ICCV2025/html/Li_Triad_Empowering_LMM-based_Anomaly_Detection_with_Expert-guided_Region-of-Interest_Tokenizer_and_ICCV_2025_paper.html)
+ LR-IAD:Mask-Free Industrial Anomaly Detection with Logical Reasoning [[2025]](https://arxiv.org/abs/2504.19524)
+ OmniAD: Detect and Understand Industrial Anomaly via Multimodal Reasoning[[2025]](https://arxiv.org/abs/2505.22039)
+ EMIT: Enhancing MLLMs for Industrial Anomaly Detection via Difficulty-Aware [[2025]](https://arxiv.org/abs/2507.21619)[[code]](https://github.com/guanwei49/EMIT)
+ IAD-R1: Reinforcing Consistent Reasoning in Industrial Anomaly Detection [[ICCV 2025]](https://arxiv.org/abs/2508.09178)[[code]](https://github.com/Yanhui-Lee/IAD-R1)
+ AD-FM: Multimodal LLMs for Anomaly Detection via Multi-Stage Reasoning and Fine-Grained Reward Optimization [[AAAI 2026]](https://arxiv.org/abs/2508.04175)
+ AgentIAD: Tool-Augmented Single-Agent for Industrial Anomaly Detection [[2025]](https://arxiv.org/abs/2512.13671)

## CVPR 2023
+ CVPR 2023 Tutorial on "Recent Advances in Anomaly Detection" [[CVPR Workshop 2023(mainly on video anomaly detection)]](https://sites.google.com/view/cvpr2023-tutorial-on-ad/)[[video]](https://www.youtube.com/watch?v=dXxrzWeybBo&feature=youtu.be)
+ Workshop on Vision-Based Industrial Inspection [[CVPR Workshop paper list 2023]](https://openaccess.thecvf.com/CVPR2023_workshops/VISION)
+ Visual Anomaly and Novelty Detection [[CVPR Workshop paper list 2023]](https://openaccess.thecvf.com/CVPR2023_workshops/VAND)
+ Revisiting Reverse Distillation for Anomaly Detection [[CVPR 2023]](https://openaccess.thecvf.com/content/CVPR2023/papers/Tien_Revisiting_Reverse_Distillation_for_Anomaly_Detection_CVPR_2023_paper.pdf) [[code]](https://github.com/tientrandinh/Revisiting-Reverse-Distillation)
+ OmniAL A unifiled CNN framework for unsupervised anomaly localization [[CVPR 2023]](https://openaccess.thecvf.com/content/CVPR2023/papers/Zhao_OmniAL_A_Unified_CNN_Framework_for_Unsupervised_Anomaly_Localization_CVPR_2023_paper.pdf)
+ Explicit Boundary Guided Semi-Push-Pull Contrastive Learning for Supervised Anomaly Detection [[CVPR 2023]](https://arxiv.org/abs/2207.01463)[[code]](https://github.com/xcyao00/BGAD)
+ DeSTSeg: Segmentation Guided Denoising Student-Teacher for Anomaly Detection [[CVPR 2023]](https://arxiv.org/abs/2211.11317)[[code]](https://github.com/apple/ml-destseg)
+ Diversity-Measurable Anomaly Detection [[CVPR 2023]](https://arxiv.org/abs/2303.05047)
+ WinCLIP: Zero-/Few-Shot Anomaly Classification and Segmentation [[CVPR 2023]](https://arxiv.org/abs/2303.14814)
+ SimpleNet: A Simple Network for Image Anomaly Detection and Localization [[CVPR 2023]](https://arxiv.org/abs/2303.15140)[[code]](https://github.com/DonaldRR/SimpleNet)
+ PyramidFlow: High-Resolution Defect Contrastive Localization using Pyramid Normalizing Flow [[CVPR 2023]](https://arxiv.org/abs/2303.02595)[[code]](https://github.com/gasharper/PyramidFlow)
+ Multimodal Industrial Anomaly Detection via Hybrid Fusion [[CVPR 2023]](https://arxiv.org/abs/2303.00601)[[code]](https://github.com/nomewang/M3DM)
+ Prototypical Residual Networks for Anomaly Detection and Localization [[CVPR 2023]](https://arxiv.org/abs/2212.02031)[[code]](https://github.com/xcyao00/PRNet)
+ SQUID: Deep Feature In-Painting for Unsupervised Anomaly Detection [[CVPR 2023]](https://arxiv.org/abs/2111.13495)
+ APRIL-GAN: A Zero-/Few-Shot Anomaly Classification and Segmentation Method for CVPR 2023 VAND Workshop Challenge Tracks 1&2: 1st Place on Zero-shot AD and 4th Place on Few-shot AD [[CVPR 2023 VAND Workshop Challenge]](https://arxiv.org/abs/2305.17382)

## SAM segment anything
+ Segment Anything Is Not Always Perfect: An Investigation of SAM on Different Real-world Applications [[2023 SAM tech report]](https://arxiv.org/abs/2304.05750)
+ SAM Struggles in Concealed Scenes -- Empirical Study on "Segment Anything" [[2023 SAM tech report]](https://arxiv.org/abs/2304.06022)
+ Segment Any Anomaly without Training via Hybrid Prompt Regularization [[2023]](https://arxiv.org/abs/2305.10724) [[code]](https://github.com/caoyunkang/GroundedSAM-zero-shot-anomaly-detection)
+ Application of Segment Anything Model for Civil Infrastructure Defect Assessment [[2023 SAM tech report]](https://arxiv.org/abs/2304.12600)
+ Segment Anything in Defect Detection [[2023]](https://arxiv.org/abs/2311.10245)
+ Unsupervised Continual Anomaly Detection with Contrastively-learned Prompt [[AAAI 2024]](https://ojs.aaai.org/index.php/AAAI/article/view/28153)[[code]](https://github.com/shirowalker/UCAD)
+ ClipSAM: CLIP and SAM Collaboration for Zero-Shot Anomaly Segmentation [[2023]](https://arxiv.org/pdf/2401.12665)
+ A SAM-guided Two-stream Lightweight Model for Anomaly Detection [[2024]](https://arxiv.org/abs/2402.19145)[[code]](https://github.com/StitchKoala/STLM)
+ Inspiring the Next Generation of Segment Anything Models: Comprehensively Evaluate SAM and SAM 2 with Diverse Prompts Towards Context-Dependent Concepts under Different Scenes [[2024]](https://arxiv.org/abs/2412.01240)[[code]](https://github.com/lartpang/SAMs-CDConcepts-Eval)


## ICLR 2023
+ Pushing the Limits of Fewshot Anomaly Detection in Industry Vision: Graphcore [[ICLR 2023]](https://openreview.net/pdf?id=xzmqxHdZAwO)
+ RGI: robust GAN-inversion for mask-free image inpainting and unsupervised pixel-wise anomaly detection [[ICLR 2023]](https://openreview.net/pdf?id=1UbNwQC89a)

## Others
+ Self-Tuning Self-Supervised Anomaly Detection [[2023]](https://openreview.net/forum?id=saj54kqrBj)
+ Model Selection of Anomaly Detectors in the Absence of Labeled Validation Data [[2023]](https://arxiv.org/abs/2310.10461)
+ The Dawn of LMMs: Preliminary Explorations with GPT-4V(ision) [[2023 Section 9.2]](https://arxiv.org/abs/2309.17421)
+ End-to-End Augmentation Hyperparameter Tuning for Self-Supervised Anomaly Detection [[2023]](https://arxiv.org/abs/2306.12033)
+ CVPR 1st workshop on Vision-based InduStrial InspectiON [[CVPR 2023 Workshop]](https://vision-based-industrial-inspection.github.io/cvpr-2023/) [[data link]](https://drive.google.com/drive/folders/1TVp_UXJuXudqhC2L3ZKyIDcmQ_2O3JVi)
+ How Low Can You Go? Surfacing Prototypical In-Distribution Samples for Unsupervised Anomaly Detection [Dataset Distillation][[2023]](http://arxiv.org/pdf/2312.03804v1)
+ RAD: A Comprehensive Dataset for Benchmarking the Robustness of Image Anomaly Detection [[CASE 2024]](https://arxiv.org/abs/2406.07176)[[github page]](https://github.com/hustCYQ/RAD-dataset)

-->

<!-- ## Medical (related)
+ Towards Universal Unsupervised Anomaly Detection in Medical Imaging [[2024]](http://arxiv.org/pdf/2401.10637v1)
+ MAEDiff: Masked Autoencoder-enhanced Diffusion Models for Unsupervised Anomaly Detection in Brain Images [[2024]](http://arxiv.org/pdf/2401.10561v1)
+ BMAD: Benchmarks for Medical Anomaly Detection [[2023]](https://arxiv.org/abs/2306.11876)
+ Unsupervised Pathology Detection: A Deep Dive Into the State of the Art [[2023]](https://arxiv.org/abs/2303.00609)
+ Adapting Visual-Language Models for Generalizable Anomaly Detection in Medical Images [[CVPR 2024]](https://arxiv.org/abs/2403.12570)
+ Multi-Image Visual Question Answering for Unsupervised Anomaly Detection [[2024]](http://arxiv.org/abs/2404.07622v1)
+ Contrastive Language Prompting to Ease False Positives in Medical Anomaly Detection [[ISBI 2025]](https://arxiv.org/abs/2411.07546v2)   -->

# Paper Tree (Classification of representative methods)
![PaperTree](https://github.com/M-3LAB/awesome-industrial-anomaly-detection/blob/main/paper_tree.png)
# Timeline
![Timeline](https://github.com/M-3LAB/awesome-industrial-anomaly-detection/blob/main/timeline.png)

Recent developments in industrial anomaly detection have reshaped method categories and research paradigms, as illustrated in the timeline below. [[paper]](https://www.preprints.org/manuscript/202606.0719)

[![Figure 1: Timeline of industrial anomaly detection methods and the transition toward foundation-model priors](assets/fig1_timeline.png)](assets/fig1_timeline.pdf)

# Paper list for industrial image anomaly detection

# Related Survey, Benchmark, and Framework
+ A review on computer vision based defect detection and condition assessment of concrete and asphalt civil infrastructure [[2015]](https://www.sciencedirect.com/science/article/abs/pii/S1474034615000208)
+ Visual-based defect detection and classification approaches for industrial applications: a survey [[2020]](https://pdfs.semanticscholar.org/1dfc/080a5f26b5ce78f9ce3e9f106bf7e8124f74.pdf)
+ A Unified Survey on Anomaly, Novelty, Open-Set, and Out-of-Distribution Detection: Solutions and Future Challenges [[TMLR 2022]](https://arxiv.org/abs/2110.14051)
+ Deep Learning for Unsupervised Anomaly Localization in Industrial Images: A Survey [[TIM 2022]](http://arxiv.org/pdf/2207.10298)
+ A Survey on Unsupervised Industrial Anomaly Detection Algorithms [[2022]](https://arxiv.org/abs/2204.11161)
+ A Survey of Methods for Automated Quality Control Based on Images [[IJCV 2023]](https://link.springer.com/article/10.1007/s11263-023-01822-w)[[github page]](https://github.com/jandiers/mvtec-results)
+ Benchmarking Unsupervised Anomaly Detection and Localization [[2022]](https://arxiv.org/abs/2205.14852)
+ IM-IAD: Industrial Image Anomaly Detection Benchmark in Manufacturing [[TCYB 2024]](https://arxiv.org/abs/2301.13359)[[code]](https://github.com/M-3LAB/open-iad)[[中文]](https://blog.csdn.net/m0_63828250/article/details/136891730)
+ A Deep Learning-based Software for Manufacturing Defect Inspection [[TII 2017]](https://ieeexplore.ieee.org/document/9795891)[[code]](https://github.com/sundyCoder/DEye)
+ Anomalib: A Deep Learning Library for Anomaly Detection [[ICIP 2022]](https://ieeexplore.ieee.org/abstract/document/9897283/)[[code]](https://github.com/open-edge-platform/anomalib)
+ Ph.D. thesis of Paul Bergmann(The first author of MVTec AD series) [[2022]](https://mediatum.ub.tum.de/1662158)
+ CVPR 2023 Tutorial on "Recent Advances in Anomaly Detection" [[CVPR Workshop 2023]](https://sites.google.com/view/cvpr2023-tutorial-on-ad/)[[video]](https://www.youtube.com/watch?v=dXxrzWeybBo&feature=youtu.be)
+ A Survey on Visual Anomaly Detection: Challenge, Approach, and Prospect [[2024]](https://arxiv.org/pdf/2401.16402.pdf)
+ AUPIMO: Redefining Visual Anomaly Detection Benchmarks with High Speed and Low Tolerance [[2024]](https://arxiv.org/abs/2401.01984)
+ Explainable Anomaly Detection in Images and Videos: A Survey [[2024]](https://arxiv.org/pdf/2302.06670)[[repo]](https://github.com/wyzjack/Awesome-XAD)
+ RAD: A Comprehensive Dataset for Benchmarking the Robustness of Image Anomaly Detection [[CASE 2024]](https://arxiv.org/abs/2406.07176)[[github page]](https://github.com/hustCYQ/RAD-dataset)
+ Generalized Out-of-Distribution Detection and Beyond in Vision Language Model Era: A Survey [[2024]](https://arxiv.org/abs/2407.21794)[[github page]](https://github.com/AtsuMiyai/Awesome-OOD-VLM)
+ Large Language Models for Anomaly and Out-of-Distribution Detection: A Survey [[2024]](https://arxiv.org/abs/2409.01980)[[github page]](https://github.com/rux001/Awesome-LLM-Anomaly-OOD-Detection)
+ A Survey on RGB, 3D, and Multimodal Approaches for Unsupervised Industrial Anomaly Detection [[2024]](https://arxiv.org/abs/2410.21982)[[github page]](https://github.com/Sunny5250/Awesome-Multi-Setting-UIAD)
+ OpenOOD: Benchmarking Generalized Out-of-Distribution Detection [[NeurIPS2022v1]](https://openreview.net/pdf?id=gT6j4_tskUt)[[2024v1.5]](https://arxiv.org/abs/2306.09301)[[github page]](https://github.com/Jingkang50/OpenOOD)
+ Exploring Plain ViT Reconstruction for Multi-class Unsupervised Anomaly Detection [[CVIU 2025]](https://www.sciencedirect.com/science/article/abs/pii/S1077314225000311?via%3Dihub)[[code]](https://zhangzjn.github.io/projects/ViTAD/)
+ A Survey on Foundation-Model-Based Industrial Defect Detection [[2025]](https://arxiv.org/abs/2502.19106)
+ Foundation Models for Anomaly Detection: Vision and Challenges [[2025]](https://arxiv.org/abs/2502.06911)
+ Beyond Academic Benchmarks: Critical Analysis and Best Practices for Visual Industrial Anomaly Detection [[2025]](https://arxiv.org/abs/2503.23451)[[code]](https://github.com/abc-125/viad-benchmark)
+ A Comprehensive Survey for Real-World Industrial Defect Detection: Challenges, Approaches, and Prospects [[2025]](https://www.arxiv.org/abs/2507.13378)
+ Towards High-Resolution Industrial Image Anomaly Detection [[2025]](https://arxiv.org/abs/2508.12931)[[code]](https://github.com/cnulab/HiAD)
+ ASBench: Image Anomalies Synthesis Benchmark for Anomaly Detection [[TAI 2026]](https://arxiv.org/abs/2510.07927)[[code]](https://github.com/M-3LAB/ASBench)
+ A Survey of Recent Advances in Industrial Anomaly Detection: From Normal-Only Training to Foundation-Model Priors [[2026]](https://www.preprints.org/manuscript/202606.0719)
+ Anomaly Detection and Generation with Diffusion Models: A Survey [[TPAMI 2026]](https://ieeexplore.ieee.org/abstract/document/11718971)

# 2 Unsupervised AD

## 2.1 Feature-Embedding-based Methods

### 2.1.1 Teacher-Student
+ Contextual Affinity Distillation for Image Anomaly Detection [[WACV 2024]](https://openaccess.thecvf.com/content/WACV2024/papers/Zhang_Contextual_Affinity_Distillation_for_Image_Anomaly_Detection_WACV_2024_paper.pdf)
+ Revisiting Reverse Distillation for Anomaly Detection [[CVPR 2023]](https://openaccess.thecvf.com/content/CVPR2023/papers/Tien_Revisiting_Reverse_Distillation_for_Anomaly_Detection_CVPR_2023_paper.pdf) [[code]](https://github.com/tientrandinh/Revisiting-Reverse-Distillation)
+ Uninformed students: Student-teacher anomaly detection with discriminative latent embeddings [[CVPR 2020]](http://arxiv.org/pdf/1911.02357)
+ Multiresolution knowledge distillation for anomaly detection [[CVPR 2021]](https://arxiv.org/pdf/2011.11108)
+ Glancing at the Patch: Anomaly Localization With Global and Local Feature Comparison [[CVPR 2021]](https://openaccess.thecvf.com/content/CVPR2021/html/Wang_Glancing_at_the_Patch_Anomaly_Localization_With_Global_and_Local_CVPR_2021_paper.html)
+ Reconstruction Student with Attention for Student-Teacher Pyramid Matching [[2021]](https://arxiv.org/pdf/2111.15376.pdf)
+ Student-Teacher Feature Pyramid Matching for Anomaly Detection [[2021]](https://arxiv.org/pdf/2103.04257.pdf)[[code]](https://github.com/smiler96/PFM-and-PEFM-for-Image-Anomaly-Detection-and-Segmentation)
+ PFM and PEFM for Image Anomaly Detection and Segmentation [[CASE 2022]](https://ieeexplore.ieee.org/abstract/document/9926547/) [[TII 2022]](https://ieeexplore.ieee.org/document/9795121)[[code]](https://github.com/smiler96/PFM-and-PEFM-for-Image-Anomaly-Detection-and-Segmentation)
+ Reconstructed Student-Teacher and Discriminative Networks for Anomaly Detection [[2022]](https://arxiv.org/pdf/2210.07548.pdf)
+ Anomaly Detection via Reverse Distillation from One-Class Embedding [[CVPR 2022]](http://arxiv.org/pdf/2201.10703)[[code]](https://github.com/hq-deng/RD4AD)
+ Asymmetric Student-Teacher Networks for Industrial Anomaly Detection [[WACV 2022]](https://arxiv.org/pdf/2210.07829.pdf)[[code]](https://github.com/marco-rudolph/AST)
+ Informative knowledge distillation for image anomaly segmentation [[2022]](https://www.sciencedirect.com/science/article/pii/S0950705122004038/pdfft?md5=758c327dd4d1d052b61a19882f957123&pid=1-s2.0-S0950705122004038-main.pdf)[[code]](https://github.com/caoyunkang/IKD)
+ Learning deep feature correspondence for unsupervised anomaly detection and segmentation[[PR 2022]](https://www.sciencedirect.com/science/article/abs/pii/S0031320322003557)[[code]](https://github.com/YoungGod/DFC)
+ Remembering Normality: Memory-guided Knowledge Distillation for Unsupervised Anomaly Detection [[ICCV 2023]](https://openaccess.thecvf.com/content/ICCV2023/papers/Gu_Remembering_Normality_Memory-guided_Knowledge_Distillation_for_Unsupervised_Anomaly_Detection_ICCV_2023_paper.pdf)
+ A Discrepancy Aware Framework for Robust Anomaly Detection [[2023]](https://arxiv.org/abs/2310.07585)[[code]](https://github.com/caiyuxuan1120/DAF)
+ Enhanced multi-scale features mutual mapping fusion based on reverse knowledge distillation for industrial anomaly detection and localization [[TBD 2024]](https://ieeexplore.ieee.org/abstract/document/10382612)
+ AEKD: Unsupervised auto-encoder knowledge distillation for industrial anomaly detection [[JMS 2024]](https://www.sciencedirect.com/science/article/pii/S0278612524000244)
+ Masked feature regeneration based asymmetric student–teacher network for anomaly detection [[Multimedia Tools and Applications 2024]](https://link.springer.com/article/10.1007/s11042-024-18512-5)
+ Feature-Constrained and Attention-Conditioned Distillation Learning for Visual Anomaly Detection [[ICASSP 2024]](https://ieeexplore.ieee.org/document/10448432)
+ MiniMaxAD: A Lightweight Autoencoder for Feature-Rich Anomaly Detection [[2024]](https://arxiv.org/abs/2405.09933)
+ Enhanced Fabric Defect Detection with Feature Contrast Interference Suppression [[TIM 2025]](https://ieeexplore.ieee.org/abstract/document/10937904)
+ Anomaly Detection and Localization via Reverse Distillation with Latent Anomaly Suppression [[TCSVT 2025]](https://ieeexplore.ieee.org/abstract/document/10969994)
+ Memory-Distilled Selection for Noise-Robust Anomaly Detection [[ICML 2026]](https://arxiv.org/abs/2605.26676)[[code]](https://github.com/SirojbekSafarov/MeDS)

### 2.1.2 One-Class Classification (OCC)
+ Patch svdd: Patch-level svdd for anomaly detection and segmentation [[ACCV 2020]](https://arxiv.org/pdf/2006.16067.pdf)
+ Anomaly detection using improved deep SVDD model with data structure preservation [[2021]](https://www.sciencedirect.com/science/article/am/pii/S0167865521001598)
+ A Semantic-Enhanced Method Based On Deep SVDD for Pixel-Wise Anomaly Detection [[2021]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9428370)
+ MOCCA: Multilayer One-Class Classification for Anomaly Detection [[2021]](http://arxiv.org/pdf/2012.12111)
+ Defect Detection of Metal Nuts Applying Convolutional Neural Networks [[2021]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9529439)
+ Panda: Adapting pretrained features for anomaly detection and segmentation [[2021]](http://arxiv.org/pdf/2010.05903)
+ Mean-shifted contrastive loss for anomaly detection [[2021]](https://arxiv.org/pdf/2106.03844.pdf)
+ Learning and Evaluating Representations for Deep One-Class Classification [[2020]](https://arxiv.org/pdf/2011.02578.pdf)
+ Self-supervised learning for anomaly detection with dynamic local augmentation [[2021]](https://ieeexplore.ieee.org/ielx7/6287639/6514899/09597511.pdf)
+ Contrastive Predictive Coding for Anomaly Detection [[2021]](https://arxiv.org/pdf/2107.07820.pdf)
+ Cutpaste: Self-supervised learning for anomaly detection and localization [[ICCV 2021]](http://arxiv.org/pdf/2104.04015)[[unofficial code]](https://github.com/Runinho/pytorch-cutpaste)
+ Consistent estimation of the max-flow problem: Towards unsupervised image segmentation [[2020]](http://arxiv.org/pdf/1811.00220)
+ MemSeg: A semi-supervised method for image surface defect detection using differences and commonalities [[2022]](https://arxiv.org/pdf/2205.00908.pdf)[[unofficial code]](https://github.com/TooTouch/MemSeg)
+ SimpleNet: A Simple Network for Image Anomaly Detection and Localization [[CVPR 2023]](https://github.com/DonaldRR/SimpleNet)[[code]](https://github.com/DonaldRR/SimpleNet)
+ End-to-End Augmentation Hyperparameter Tuning for Self-Supervised Anomaly Detection [[2023]](https://arxiv.org/abs/2306.12033)
+ Anomaly Detection under Distribution Shift [[ICCV 2023]](https://openaccess.thecvf.com/content/ICCV2023/papers/Cao_Anomaly_Detection_Under_Distribution_Shift_ICCV_2023_paper.pdf)[[code]](https://github.com/mala-lab/ADShift)
+ Learning Transferable Representations for Image Anomaly Localization Using Dense Pretraining [[WACV 2024]](https://openaccess.thecvf.com/content/WACV2024/papers/He_Learning_Transferable_Representations_for_Image_Anomaly_Localization_Using_Dense_Pretraining_WACV_2024_paper.pdf)[[code]](https://github.com/terrlo/DS2)
+ GeneralAD: Anomaly Detection Across Domains by Attending to Distorted Features [[ECCV 2024]](https://arxiv.org/abs/2407.12427)[[code]](https://github.com/LucStrater/GeneralAD)
+ A Unified Anomaly Synthesis Strategy with Gradient Ascent for Industrial Anomaly Detection and Localization [[ECCV 2024]](https://arxiv.org/abs/2407.09359)[[code]](https://github.com/cqylunlun/GLASS)
+ Dual-Modeling Decouple Distillation for Unsupervised Anomaly Detection [[ACM MM 2024]](https://arxiv.org/abs/2408.03888)
+ SuperSimpleNet: Unifying Unsupervised and Supervised Learning for Fast and Reliable Surface Defect Detection [[ICPR 2024]](https://arxiv.org/abs/2408.03143)[[JIMS 2025]](https://link.springer.com/article/10.1007/s10845-025-02680-8)[[code]](https://github.com/blaz-r/SuperSimpleNet/tree/main)
+ Progressive Boundary Guided Anomaly Synthesis for Industrial Anomaly Detection [[TCSVT 2024]](https://ieeexplore.ieee.org/document/10716437)[[code]](https://github.com/cqylunlun/PBAS)
+ BAAF: Universal Transformation of One-Class Classifiers for Unsupervised Image Anomaly Detection [[ECCV 2026]](https://arxiv.org/abs/2602.13091)[[code]](https://github.com/DeclanMcIntosh/BAAF)

### 2.1.3 Distribution-Map
+ Anomaly Detection in Nanofibrous Materials by CNN-Based Self-Similarity [[Sensors 2018]](https://www.mdpi.com/1424-8220/18/1/209)
+ A Multi-Scale A Contrario method for Unsupervised Image Anomaly Detection [[2021]](http://arxiv.org/pdf/2110.02407)
+ Modeling the distribution of normal data in pre-trained deep features for anomaly detection [[2021]](http://arxiv.org/pdf/2005.14140)
+ Transfer Learning Gaussian Anomaly Detection by Fine-Tuning Representations [[2021]](https://arxiv.org/pdf/2108.04116.pdf)
+ PEDENet: Image anomaly localization via patch embedding and density estimation [[2022]](https://arxiv.org/pdf/2110.15525.pdf)
+ Unsupervised image anomaly detection and segmentation based on pre-trained feature mapping [[2022]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9795121)
+ Position Encoding Enhanced Feature Mapping for Image Anomaly Detection [[2022]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9926547)[[code]](https://github.com/smiler96/PFM-and-PEFM-for-Image-Anomaly-Detection-and-Segmentation)
+ Focus your distribution: Coarse-to-fine non-contrastive learning for anomaly detection and localization [[ICME 2022]](http://arxiv.org/pdf/2110.04538)
+ Anomaly Detection of Defect using Energy of Point Pattern Features within Random Finite Set Framework [[2021]](https://arxiv.org/abs/2108.12159)[[code]](https://github.com/AmmarKamoona/RFS-Energy-Anomaly-Detection-of-Defect)
+ Fastflow: Unsupervised anomaly detection and localization via 2d normalizing flows [[2021]](https://arxiv.org/pdf/2111.07677.pdf)[[unofficial code]](https://github.com/gathierry/FastFlow)
+ Same same but differnet: Semi-supervised defect detection with normalizing flows [[WACV 2021]](http://arxiv.org/pdf/2008.12577)[[code]](https://github.com/marco-rudolph/differnet)
+ Fully convolutional cross-scale-flows for image-based defect detection [[WACV 2022]](http://arxiv.org/pdf/2110.02855)[[code]](https://github.com/marco-rudolph/cs-flow)
+ Cflow-ad: Real-time unsupervised anomaly detection with localization via conditional normalizing flows [[WACV 2022]](http://arxiv.org/pdf/2107.12571)[[code]](https://github.com/gudovskiy/cflow-ad)
+ CAINNFlow: Convolutional block Attention modules and Invertible Neural Networks Flow for anomaly detection and localization tasks [[2022]](https://arxiv.org/pdf/2206.01992.pdf)
+ AltUB: Alternating Training Method to Update Base Distribution of Normalizing Flow for Anomaly Detection [[2022]](https://arxiv.org/pdf/2210.14913.pdf)
+ Collaborative Discrepancy Optimization for Reliable Image Anomaly Localization [[TII 2023]](https://ieeexplore.ieee.org/document/10034849)[[code]](https://github.com/caoyunkang/CDO)
+ PyramidFlow: High-Resolution Defect Contrastive Localization using Pyramid Normalizing Flow [[CVPR 2023]](https://arxiv.org/abs/2303.02595)[[code]](https://github.com/gasharper/PyramidFlow)
+ Attention Modules Improve Image-Level Anomaly Detection for Industrial Inspection: A DifferNet Case Study [[WACV 2024]](https://openaccess.thecvf.com/content/WACV2024/papers/Vieira_e_Silva_Attention_Modules_Improve_Image-Level_Anomaly_Detection_for_Industrial_Inspection_A_WACV_2024_paper.pdf)
+ Fascinating Supervisory Signals and Where to Find Them: Deep Anomaly Detection with Scale Learning [[ICML 2023]](https://openreview.net/forum?id=V6PNBRWRil)
+ FRAnomaly: flow-based rapid anomaly detection from images [[Applied Intelligence 2024]](https://link.springer.com/article/10.1007/s10489-024-05332-1)
+ Image alignment-based patch distribution framework for anomaly detection [[ICCVDM 2024]](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/13063/130630O/Image-alignment-based-patch-distribution-framework-for-anomaly-detection/10.1117/12.3021499.full)
+ MSFlow: Multi-Scale Flow-based Framework for Unsupervised Anomaly Detection [[2024]](https://arxiv.org/abs/2308.15300)[[code]](https://github.com/cool-xuan/msflow)
+ Distribution Prototype Diffusion Learning for Open-set Supervised Anomaly Detection [[CVPR 2025]](https://arxiv.org/abs/2502.20981)[[code]](https://github.com/fuyunwang/DPDL)
+ Multi-Prototype Compactness and Boundary-Aware Synthesis for Unsupervised Anomaly Detection [[CVPR 2026]](https://cvpr.thecvf.com/virtual/2026/poster/37868)

### 2.1.4 Memory Bank
 + ReConPatch: Contrastive Patch Representation Learning for Industrial Anomaly Detection [[WACV 2024]](https://openaccess.thecvf.com/content/WACV2024/papers/Hyun_ReConPatch_Contrastive_Patch_Representation_Learning_for_Industrial_Anomaly_Detection_WACV_2024_paper.pdf)
 + Sub-image anomaly detection with deep pyramid correspondences [[2020]](https://arxiv.org/pdf/2005.02357.pdf)
 + Semi-orthogonal embedding for efficient unsupervised anomaly segmentation [[2021]](https://arxiv.org/pdf/2105.14737.pdf)
 + Anomaly Detection Via Self-Organizing Map [[2021]](http://arxiv.org/pdf/2107.09903)
 + PaDiM: A Patch Distribution Modeling Framework for Anomaly Detection and Localization [[ICPR 2021]](https://link.springer.com/chapter/10.1007/978-3-030-68799-1_35)[[unofficial code]](https://github.com/xiahaifeng1995/PaDiM-Anomaly-Detection-Localization-master)
 + Industrial Image Anomaly Localization Based on Gaussian Clustering of Pretrained Feature [[2021]](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9479740)
 + Towards total recall in industrial anomaly detection[[CVPR 2022]](http://arxiv.org/pdf/2106.08265)[[code]](https://github.com/amazon-science/patchcore-inspection)
 + CFA: Coupled-Hypersphere-Based Feature Adaptation for Target-Oriented Anomaly Localization[[2022]](https://arxiv.org/pdf/2206.04325.pdf)[[code]](https://github.com/sungwool/CFA_for_anomaly_localization)
 + FAPM: Fast Adaptive Patch Memory for Real-time Industrial Anomaly Detection[[2022]](https://arxiv.org/pdf/2211.07381.pdf)
 + N-pad: Neighboring Pixel-based Industrial Anomaly Detection [[2022]](https://arxiv.org/pdf/2210.08768.pdf)
 + Multi-scale patch-based representation learning for image anomaly detection and segmentation [[2022]](https://openaccess.thecvf.com/content/WACV2022/papers/Tsai_Multi-Scale_Patch-Based_Representation_Learning_for_Image_Anomaly_Detection_and_Segmentation_WACV_2022_paper.pdf)
 + SPot-the-Difference Self-supervised Pre-training for Anomaly Detection and Segmentation [[ECCV 2022]](https://arxiv.org/pdf/2207.14315.pdf)
 + Diversity-Measurable Anomaly Detection [[CVPR 2023]](https://arxiv.org/abs/2303.05047)
 + Self-supervised Context Learning for Visual Inspection of Industrial Defects [[2023]](https://arxiv.org/abs/2311.06504)[[code]](https://github.com/wangpeng000/VisualInspection)
 + SelFormaly: Towards Task-Agnostic Unified Anomaly Dete