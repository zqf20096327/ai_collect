<div align="center">

<a href="https://github.com/haoran-zha/Awesome-Spiking-Neural-Networks-Hub"><img src="assets/banner.webp" alt="Awesome Spiking Neural Networks Hub" width="100%"></a>

<h1>Awesome Spiking Neural Networks Hub</h1>

<p><em>A comprehensive, deeply-annotated guide to the world of Spiking Neural Networks (SNNs)</em><br>
<sub>papers · models · neuromorphic hardware · datasets · tools · research groups</sub></p>

<p>
<a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a>
<a href="https://github.com/haoran-zha/Awesome-Spiking-Neural-Networks-Hub/stargazers"><img src="https://img.shields.io/github/stars/haoran-zha/Awesome-Spiking-Neural-Networks-Hub?style=flat-square&logo=github&color=e3b341" alt="Stars"></a>
<a href="https://github.com/haoran-zha/Awesome-Spiking-Neural-Networks-Hub/network/members"><img src="https://img.shields.io/github/forks/haoran-zha/Awesome-Spiking-Neural-Networks-Hub?style=flat-square&logo=github&color=8b949e" alt="Forks"></a>
<img src="https://img.shields.io/github/last-commit/haoran-zha/Awesome-Spiking-Neural-Networks-Hub?style=flat-square&color=blue" alt="Last commit">
<a href="#contributing"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square" alt="PRs Welcome"></a>
<a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="MIT"></a>
</p>

<p><b>English</b> &nbsp;·&nbsp; <a href="README.zh-CN.md">中文</a> &nbsp;|&nbsp; <a href="TIMELINE.md">Timeline edition</a></p>

<p><b>420+</b> papers &amp; resources &nbsp;·&nbsp; <b>50+</b> seminal works &nbsp;·&nbsp; <b>42</b> research groups &nbsp;·&nbsp; <b>45+</b> open-source projects</p>

<p><b>Jump to</b> &nbsp;
<a href="#start-here">Start Here</a> ·
<a href="#1--foundations--neural-coding">Fundamentals</a> ·
<a href="#3--training-methods">Learning &amp; Models</a> ·
<a href="#6--neuromorphic-hardware">Hardware</a> ·
<a href="#7--applications">Applications</a> ·
<a href="#8--energy-robustness--security">Topics</a> ·
<a href="#10--datasets--benchmarks">Resources</a> ·
<a href="#13--research-groups--labs">Groups</a></p>

<sub>If this guide helps your work, please star the repo and <a href="#citation">cite it</a> — contributions are very welcome.</sub>

</div>

---

## What Is a Spiking Neural Network? (Read Me First)

Conventional deep networks (ANNs) pass **continuous numbers** between neurons at every layer, synchronously, every forward pass. A **Spiking Neural Network** instead communicates with **discrete, binary events — "spikes" — in time**, exactly like biological neurons. A spiking neuron integrates incoming current onto a *membrane potential*; when that potential crosses a threshold, it emits a single spike and resets. Nothing happens when there is no spike.

Three consequences make SNNs compelling:

- **Event-driven & sparse** → computation (and energy) is spent only when a spike occurs. On neuromorphic hardware this can mean *orders-of-magnitude* lower power than a GPU.
- **Temporal by construction** → information lives not just in *how many* spikes fire but in *when* they fire, giving a natural substrate for time-series, audio, and event-camera data.
- **Brain-inspired** → SNNs are often called the **"third generation"** of neural networks (after perceptrons and rate-based deep nets), bridging neuroscience and machine learning.

The central difficulty is that a spike is a **step function — non-differentiable** — so ordinary backpropagation does not directly apply. The whole field, in a sense, is a set of answers to *"how do we train these things?"* — which is why the [Training Methods](#3--training-methods) section is the heart of this list.

> This is an **awesome-style hub for the whole SNN field** — papers, models, hardware, datasets, tools, and research groups. Each entry carries a one-line "why it matters" note (English here; 中文 in the [Chinese edition](README.zh-CN.md)) so you can navigate without drowning.

---

## Start Here

**13 must-read landmarks that trace the field's arc** — from the "third generation" idea to today's spiking Transformers and large models. *(The ★ markers throughout the guide flag many more.)*

| Year | Landmark | Venue | Link |
|:---:|---|:---:|:---:|
| 1997 | **Networks of Spiking Neurons: The Third Generation** — *the founding idea* | Neural Networks | [paper](https://doi.org/10.1016/S0893-6080(97)00011-7) |
| 2014 | **TrueNorth** — *a million-neuron neuromorphic chip* | Science | [paper](https://www.science.org/doi/10.1126/science.1254642) |
| 2015 | **Unsupervised Learning with STDP** — *bio-plausible learning* | Front. Comput. Neurosci. | [paper](https://doi.org/10.3389/fncom.2015.00099) |
| 2018 | **Loihi** — *on-chip-learning neuromorphic processor* | IEEE Micro | [paper](https://ieeexplore.ieee.org/document/8259423) |
| 2018 | **STBP** — *spatio-temporal backprop, the training workhorse* | Front. Neurosci. | [paper](https://doi.org/10.3389/fnins.2018.00331) |
| 2020 | **e-prop** — *biologically plausible online learning* | Nature Comm. | [paper](https://doi.org/10.1038/s41467-020-17236-y) |
| 2021 | **SEW-ResNet** — *directly training 100+ layer SNNs* | NeurIPS | [paper](https://arxiv.org/abs/2102.04159) |
| 2022 | **QCFS** — *near-lossless ANN→SNN conversion* | ICLR | [paper](https://arxiv.org/abs/2303.04347) |
| 2023 | **Spikformer** — *the first spiking Transformer* | ICLR | [paper](https://arxiv.org/abs/2209.15425) |
| 2023 | **Spike-driven Transformer** — *pure spike-driven attention* | NeurIPS | [paper](https://arxiv.org/abs/2307.01694) |
| 2024 | **SpikeGPT** — *the first generative spiking LLM* | TMLR | [paper](https://arxiv.org/abs/2302.13939) |
| 2025 | **Darwin Monkey** — *first 2-billion-neuron neuromorphic computer* | ZJU | [link](https://www.zju.edu.cn/english/2025/0910/c19573a3079424/page.htm) |
| 2026 | **SpikingBrain** — *7B/76B spiking brain-inspired LLM* | TMLR | [paper](https://arxiv.org/abs/2509.05276) |

---

## Recent Updates

<details open>
<summary><b>Changelog</b> — newest first (click to collapse)</summary>

- **2026-10** — **Top-journal & conference catch-up.** Added 87 papers, led by the Nature / Science family (Nature Communications 21, Nature Electronics 11, Nature Machine Intelligence 8, Nature 7, Nature Computational Science 5, Nature Neuroscience 5, Science 4, Science Advances 2, plus Nature Materials / Nanotechnology / Photonics / Reviews) and NeurIPS 2025 · ICLR 2026 · ICML 2026 orals & spotlights; seven classics added with ★ (Neftci–Mostafa–Zenke surrogate gradients, Roy et al. Nature 2019, all-optical spiking networks, Markram 1997 and Song–Miller–Abbott 2000 STDP, Spaun, Brunel 2000); NIR added to §11; fixed two dead lab links (UESTC, Western Sydney).
- **2026-08** — **Darwin Monkey & summer sweep.** Added ZJU's **Darwin Monkey** (first 2B-neuron neuromorphic computer) ★ and DarwinWafer; a new **Photonic Spiking Hardware** subsection; NSLLM (NSR 2026) ★ plus six more spiking-LLM works; SpiNNaker2 chip paper (OJCAS 2026), SpikeRAM (ISSCC 2026), UniSpike (DAC 2026) and four Nature-family hardware works; CVPR / ACM MM / TNNLS / Nat. Comm. paper catch-ups; industry updates (SpiNNcloud, BrainChip AKD1500/AKD2500, Innatera, POLYN).
- **2026-07** — **2026 conference sweep.** Added the first CVPR 2026 (13) and ICML 2026 (11) entries, plus ECCV / IJCAI 2026, two TPAMI 2026 works and a Nature Communications 2026 neuromorphic training chip — each with its own one-line summary. SpikingBrain re-tagged **arXiv 2025 → TMLR 2026**.
- **2026-07** — **Audit & ecosystem update.** Fixed dead/outdated links and a moved lab affiliation; added six 2026 works, four major labs, and per-lab **latest-work (2024–2026)** tags across §13.
- **2026-07** — **Launched the Hub.** 340+ entries across **6 Parts**; new **Research Groups & Labs** (§13), **Model Zoo & Community** (§12), and a dedicated **Spiking Large Models & LLMs** section (§5).
- **2026-07** — **Visual overhaul.** New banner, "Start Here" table, and datasets/frameworks/model-zoo turned into tables.
- **2026-07** — **Coverage push.** Added SpikingBrain, Sorbet, SpikeCLIP, Spike2Former, SDiT; Darwin3, Intel Hala Point, IBM NorthPole, Lynxi / BrainChip / Innatera / Xylo / GrAI; plus foundational works (Mead 1990, Missing Memristor 2008, Tempotron 2006) and frameworks (SPAIC, SNNAX, BrainPy, CARLsim…).

> New paper / model / chip / dataset / tool? [Open a PR](#contributing) and add a line here.

</details>

---

## Table of Contents

**Part I · Fundamentals**
- [1 · Foundations & Neural Coding](#1--foundations--neural-coding)
- [2 · Neuron Models](#2--neuron-models)

**Part II · Learning & Models**
- [3 · Training Methods](#3--training-methods)
- [4 · Architectures](#4--architectures)
- [5 · Spiking Large Models & LLMs](#5--spiking-large-models--llms)

**Part III · Hardware & Systems**
- [6 · Neuromorphic Hardware](#6--neuromorphic-hardware)

**Part IV · Applications**
- [7 · Applications](#7--applications)

**Part V · Cross-Cutting Topics**
- [8 · Energy, Robustness & Security](#8--energy-robustness--security)
- [9 · Theory & Neuroscience](#9--theory--neuroscience)

**Part VI · Resources & Ecosystem**
- [10 · Datasets & Benchmarks](#10--datasets--benchmarks)
- [11 · Software & Frameworks](#11--software--frameworks)
- [12 · Model Zoo & Community](#12--model-zoo--community)
- [13 · Research Groups & Labs](#13--research-groups--labs)

**Meta:** [Contributing](#contributing) · [Citation](#citation) · [Star History](#star-history) · [License](#license--acknowledgements)

**Legend:** ★ = seminal / must-read · [paper] = paper · [code] = official code

---

## Part I · Fundamentals

### 1 · Foundations & Neural Coding

> **In one breath:** the roots of the field — from the first threshold neuron and the Nobel-winning Hodgkin–Huxley model to Maass's "third generation" framing — plus *neural coding*: **how a real-valued signal becomes spikes** (and back). Rate coding counts spikes over a window (simple, robust, slow); temporal/latency coding puts information in spike *timing* (fast, efficient, harder to train); rank-order and population codes sit in between. Your choice of code sets the ceiling on both accuracy and latency.

#### Historical Foundations

- A Logical Calculus of the Ideas Immanent in Nervous Activity (**Bull. Math. Biophysics 1943**) ★. \[[paper](https://doi.org/10.1007/BF02478259)\]
  > The McCulloch–Pitts threshold neuron — the conceptual seed of all artificial and spiking neurons.
- A Quantitative Description of Membrane Current and Its Application to Conduction and Excitation in Nerve (**J. Physiology 1952**) ★. \[[paper](https://doi.org/10.1113/jphysiol.1952.sp004764)\]
  > The Hodgkin–Huxley model — the Nobel-winning biophysical basis for all spiking-neuron dynamics.
- Networks of Spiking Neurons: The Third Generation of Neural Network Models (**Neural Networks 1997**) ★. \[[paper](https://doi.org/10.1016/S0893-6080(97)00011-7)\]
  > Maass's landmark defining SNNs as the computationally more powerful "third generation."
- Spiking Neuron Models: Single Neurons, Populations, Plasticity (**Cambridge Univ. Press 2002**) ★. \[[paper](https://doi.org/10.1017/CBO9780511815706)\]
  > Gerstner & Kistler's foundational textbook unifying IF, SRM, population, and plasticity theory.

#### Neural Coding & Encoding Schemes

- Spike-Based Strategies for Rapid Processing (**Neural Networks 2001**). \[[paper](https://doi.org/10.1016/S0893-6080(01)00083-1)\]
  > Thorpe et al.'s rank-order coding — firing *order* alone enables ultra-fast recognition.
- Rapid Neural Coding in the Retina with Relative Spike Latencies (**Science 2008**). \[[paper](https://www.science.org/doi/10.1126/science.1149639)\]
  > Biological evidence that relative first-spike latency carries robust, contrast-invariant information.
- Neural Coding in Spiking Neural Networks: A Comparative Study for Robust Neuromorphic Systems (**Front. Neurosci. 2021**). \[[paper](https://www.frontiersin.org/articles/10.3389/fnins.2021.638474/full)\]
  > Systematically benchmarks rate / temporal / phase / burst codes for accuracy and robustness.
- Deep Neural Networks with Weighted Spikes (**Neurocomputing 2018**). \[[paper](https://doi.org/10.1016/j.neucom.2018.05.087)\]
  > Phase/weighted-spike coding assigns time-dependent weights to spikes, cutting latency and spike count.
- Conversion of Analog to Spiking Neural Networks Using Sparse Temporal Coding (**IEEE ISCAS 2018**). \[[paper](https://doi.org/10.1109/ISCAS.2018.8351295)\]
  > Time-to-first-spike conversion that slashes operations versus rate coding at near-zero accuracy loss.
- T2FSNN: Deep Spiking Neural Networks with Time-to-First-Spike Coding (**DAC 2020**). \[[paper](https://arxiv.org/abs/2003.11741)\]
  > Brings TTFS coding to deep SNNs with kernel thresholds and early-firing for low latency/energy.
- Temporal Coding in Spiking Neural Networks with Alpha Synaptic Function (**ICASSP 2020**). \[[paper](https://arxiv.org/abs/1907.13223)\]
  > Enables exact backprop through precise spike times using an alpha-shaped synaptic response.
- Temporal-Coded Deep Spiking Neural Network with Easy Training and Robust Performance (**AAAI 2021**). \[[paper](https://ojs.aaai.org/index.php/AAAI/article/view/17329)\]
  > Argues non-leaky single-spike temporal coding is best for directly-trainable, robust deep SNNs.
- DIET-SNN: Direct Input Encoding with Leakage and Threshold Optimization (**IEEE TNNLS 2023**). \[[paper](https://arxiv.org/abs/2008.03658)\]
  > Feeds analog pixels directly and learns leak/threshold end-to-end, popularizing direct input encoding.
- Supervised Learning Based on Temporal Coding in Spiking Neural Networks (**IEEE TNNLS 2018**). \[[paper](https://doi.org/10.1109/TNNLS.2017.2726060)\]
  > Mostafa's exact gradient descent on the *time* of the first spike — a foundational temporal-coding training method.
- Optimized Spiking Neurons Can Classify Images with High Accuracy through Temporal Coding with Two Spikes (FS neurons) (**Nature Machine Intelligence 2021**). \[[paper](https://www.nature.com/articles/s42256-021-00311-4)\]
  > Few-spike (FS) neurons emulate ANN activations with ~2 spikes, giving high-accuracy, ultra-sparse temporal coding.
- Fast and Energy-Efficient Neuromorphic Deep Learning with First-Spike Times (**Nature Machine Intelligence 2021**). \[[paper](https://www.nature.com/articles/s42256-021-00388-x)\]\[[code](https://github.com/JulianGoeltz/fastAndDeep)\]
  > Rigorously derives a first-spike-time learning rule for LIF networks that needs only input and output spike times, enabling error backprop in hierarchical SNNs, emulated on BrainScaleS-2 to harness its speed and energy efficiency.
- Efficiently Training Time-to-First-Spike Spiking Neural Networks from Scratch (**ICML 2026**). \[[paper](https://arxiv.org/abs/2410.23619)\]\[[code](https://github.com/CheKaiWei/ETTFS)\]
  > Counters signal diminishing and vanishing gradients in from-scratch TTFS training via parameter initialization and training normalization, plus a temporal output decoder rewarding earlier firing and average pooling that preserves single-spike constraints.
- I2E: Real-Time Image-to-Event Conversion for High-Performance Spiking Neural Networks (**AAAI 2026**). \[[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37179)\]\[[code](https://github.com/Ruichen0424/I2E)\]
  > Simulates microsaccadic eye movements with a highly parallelized convolution to turn static images into event streams over 300x faster than prior methods, enabling on-the-fly augmentation and synthetic-to-real SNN pre-training.

---

### 2 · Neuron Models

> **In one breath:** the neuron is the SNN's transistor. **LIF** (leaky integrate-and-fire) is the workhorse — cheap and good enough for deep learning. **Izhikevich** and **AdEx** buy richer spiking dynamics for little cost; **Hodgkin–Huxley** is biophysically exact but expensive. A modern trend is making neuron parameters (e.g., the membrane time constant) **learnable**, letting each neuron tune its own timescale.

- Lapicque's Introduction of the Integrate-and-Fire Model Neuron (1907) (**Brain Res. Bull. 1999**) ★. \[[paper](https://doi.org/10.1016/S0361-9230(99)00161-6)\]
  > Historical account crediting Lapicque (1907) with the original integrate-and-fire neuron.
- Simple Model of Spiking Neurons (**IEEE TNN 2003**) ★. \[[paper](https://doi.org/10.1109/TNN.2003.820440)\]
  > Izhikevich's two-variable model reproducing rich cortical firing patterns at integrate-and-fire cost.
- Which Model to Use for Cortical Spiking Neurons? (**IEEE TNN 2004**). \[[paper](https://doi.org/10.1109/TNN.2004.832719)\]
  > The famous chart trading biological fidelity against compute cost across neuron models — a selection guide.
- A Framework for Spiking Neuron Models: The Spike Response Model (**Handbook of Biol. Physics 2001**). \[[paper](https://www.sciencedirect.com/science/article/pii/S1383812101800154)\]
  > Formalizes the SRM, a kernel-based generalization of integrate-and-fire.
- Adaptive Exponential Integrate-and-Fire Model as an Effective Description of Neuronal Activity (**J. Neurophysiology 2005**). \[[paper](https://doi.org/10.1152/jn.00686.2005)\]
  > The AdEx model — an exponential spike term plus adaptation that accurately fits real neurons.
- Generalized Leaky Integrate-and-Fire Models Classify Multiple Neuron Types (**Nature Communications 2018**). \[[paper](https://www.nature.com/articles/s41467-017-02717-4)\]\[[code](https://github.com/AllenInstitute/GLIF_Teeter_et_al_2018)\]
  > Allen Institute's data-driven GLIF hierarchy fit to 645 real neurons across cell types.
- Incorporating Learnable Membrane Time Constant to Enhance Learning of SNNs (PLIF) (**ICCV 2021**) ★. \[[paper](https://openaccess.thecvf.com/content/ICCV2021/html/Fang_Incorporating_Learnable_Membrane_Time_Constant_To_Enhance_Learning_of_Spiking_ICCV_2021_paper.html)\]\[[code](https://github.com/fangwei123456/Parametric-Leaky-Integrate-and-Fire-Spiking-Neuron)\]
  > PLIF makes the membrane time constant learnable, boosting accuracy and easing initialization.
- GLIF: A Unified Gated Leaky Integrate-and-Fire Neuron for Spiking Neural Networks (**NeurIPS 2022**). \[[paper](https://openreview.net/forum?id=UmFSx2c4ubT)\]\[[code](https://github.com/Ikarosy/Gated-LIF)\]
  > Learnable gates fuse multiple bio-features per neuron, enlarging representational capacity.
- KLIF: An Optimized Spiking Neuron Unit for Tuning Surrogate Gradient Slope and Membrane Potential (**arXiv 2023**). \[[paper](https://arxiv.org/abs/2302.09238)\]
  > Adds a learnable scaling factor that dynamically shapes the surrogate-gradient curve during training.
- Parallel Spiking Neurons with High Efficiency and Ability to Learn Long-Term Dependencies (PSN) (**NeurIPS 2023**). \[[paper](https://arxiv.org/abs/2304.12760)\]\[[code](https://github.com/fangwei123456/Parallel-Spiking-Neuron)\]
  > Removes reset to reformulate neuronal dynamics for parallel (non-serial) simulation and long memory.
- TC-LIF: A Two-Compartment Spiking Neuron Model for Long-Term Sequential Modelling (**AAAI 2024**). \[[paper](https://ojs.aaai.org/index.php/AAAI/article/view/29625)\]\[[code](https://github.com/ZhangShimin1/TC-LIF)\]
  > Soma–dendrite two-compartment neuron designed to propagate gradients over long temporal gaps.
- CLIF: Complementary Leaky Integrate-and-Fire Neuron for Spiking Neural Networks (**ICML 2024**). \[[paper](https://proceedings.mlr.press/v235/huang24n.html)\]\[[code](https://github.com/HuuYuLong/Complementary-LIF)\]
  > A hyperparameter-free neuron that opens extra backprop paths to fight temporal vanishing gradients.
- Temporal Dendritic Heterogeneity Incorporated with SNNs for Learning Multi-Timescale Dynamics (DH-LIF) (**Nature Communications 2024**). \[[paper](https://www.nature.com/articles/s41467-023-44614-z)\]
  > Multi-branch dendritic neuron with learnable per-branch time constants for multi-timescale learning.
- PMSN: A Parallel Multi-compartment Spiking Neuron for Multi-scale Temporal Processing (**IEEE TNNLS 2026**). \[[paper](https://arxiv.org/abs/2408.14917)\]
  > PolyU's multi-compartment neuron with parallelizable multi-timescale dynamics — >10× training acceleration and +30% accuracy on Sequential CIFAR-10 vs LIF.
- Burst Spiking Neural Networks (BuSNN) (**arXiv 2026**). \[[paper](https://arxiv.org/abs/2607.11914)\]
  > BICLab argues SNN progress needs robustness, not just accuracy — burst-firing neurons with graded spikes plus a dynamic weight constraint.
- Neural Heterogeneity Promotes Robust Learning (**Nature Communications 2021**). \[[paper](https://www.nature.com/articles/s41467-021-26022-3)\]
  > Making neuronal time-constants diverse and *learnable* improves accuracy and robustness — a principled case for heterogeneity.
- Network Model with Internal Complexity Bridges Artificial Intelligence and Neuroscience (**Nature Computational Science 2024**). \[[paper](https://doi.org/10.1038/s43588-024-00674-9)\]\[[code](https://github.com/helx-20/complexity)\]
  > Proposes 'small models with internal complexity': the authors prove a network of Hodgkin–Huxley neurons can match the dynamics and performance of a larger LIF network, making richer neurons an alternative to scaling up.

---

<p align="right"><a href="#table-of-contents">↑ Back to top</a></p>

## Part II · Learning & Models

### 3 · Training Methods

> **In one breath — the field's central problem.** A spike is a non-differentiable step, so plain backprop fails. Three families answer this: **(1) Conversion** trains a normal ANN then maps it to an SNN (high accuracy, high latency); **(2) Surrogate-gradient direct training** pretends the spike has a smooth derivative and runs backprop-through-time (best accuracy-latency trade-off today); **(3) Bio-plausible local rules** like STDP learn from spike timing without global gradients (most brain-like, hardest to scale).

#### 3.1 ANN-to-SNN Conversion

> Train in the easy (ANN) world, deploy in the efficient (SNN) world. The art is matching an SNN's *firing rate* to an ANN's *activation* — via weight/threshold normalization — so almost no accuracy is lost, ideally at low latency.

- Spiking Deep Convolutional Neural Networks for Energy-Efficient Object Recognition (**IJCV 2015**) ★. \[[paper](https://doi.org/10.1007/s11263-014-0788-3)\]
  > The seminal work mapping a trained CNN to a spiking IF network via ReLU↔firing-rate correspondence — it launched the conversion paradigm.
- Fast-Classifying, High-Accuracy Spiking Deep Networks Through Weight and Threshold Balancing (**IJCNN 2015**) ★. \[[paper](https://doi.org/10.1109/IJCNN.2015.7280696)\]
  > Introduced weight normalization / threshold balancing that keeps firing rates in range, making conversion near-lossless.
- Conversion of Continuous-Valued Deep Networks to Efficient Event-Driven Networks (**Front. Neurosci. 2017**). \[[paper](https://doi.org/10.3389/fnins.2017.00682)\]\[[code](https://github.com/NeuromorphicProcessorProject/snn_toolbox)\]
  > Spiking equivalents of BatchNorm/max-pool/softmax/bias enabling accurate VGG/Inception conversion — ships the widely used SNN-Toolbox.
- Going Deeper in Spiking Neural Networks: VGG and Residual Architectures (**Front. Neurosci. 2019**) ★. \[[paper](https://doi.org/10.3389/fnins.2019.00095)\]
  > Scaled conversion to deep VGG-16 / ResNet on ImageNet with a Spike-Norm scheme, proving SNNs can go deep.
- Enabling Deep SNNs with Hybrid Conversion and Spike-Timing-Dependent Backpropagation (**ICLR 2020**). \[[paper](https://openreview.net/forum?id=B1xSperKvH)\]\[[code](https://github.com/nitin-rathi/hybrid-snn-conversion)\]
  > Initialize from a converted SNN, then fine-tune with spike-based backprop — cutting inference timesteps by an order of magnitude.
- RMP-SNN: Residual Membrane Potential Neuron for Deeper, High-Accuracy, Low-Latency SNNs (**CVPR 2020**). \[[paper](https://arxiv.org/abs/2003.01811)\]
  > "Soft reset" (residual membrane potential) removes a key source of conversion error for near-lossless deep SNNs.
- Optimal Conversion of Conventional ANNs to SNNs (**ICLR 2021**). \[[paper](https://openreview.net/forum?id=FZ1oTwcXchK)\]\[[code](https://github.com/Jackn0/snn_optimal_conversion_pipeline)\]
  > Decomposes conversion loss layer-wise and uses a rate-norm activation with optimal threshold/shift to shorten simulation length.
- A Free Lunch From ANN: Towards Efficient, Accurate SNN Calibration (**ICML 2021**). \[[paper](https://proceedings.mlr.press/v139/li21d.html)\]\[[code](https://github.com/yhhhli/SNN_Calibration)\]
  > Light-weight layer-by-layer calibration on a handful of samples, scaling to MobileNet/RegNet on ImageNet.
- Optimal ANN-SNN Conversion for High-Accuracy and Ultra-Low-Latency SNNs (QCFS) (**ICLR 2022**) ★. \[[paper](https://arxiv.org/abs/2303.04347)\]\[[code](https://github.com/putshua/ANN_SNN_QCFS)\]
  > Trains the ANN with a quantization-clip-floor-shift activation matching SNN dynamics — high accuracy in as few as 4 timesteps.
- Optimized Potential Initialization for Low-Latency Spiking Neural Networks (**AAAI 2022**). \[[paper](https://arxiv.org/abs/2202.01440)\]
  > Setting the initial membrane potential to half-threshold minimizes conversion error, enabling accuracy under 32 timesteps.
- Bridging the Gap Between ANNs and SNNs by Calibrating Offset Spikes (**ICLR 2023**). \[[paper](https://arxiv.org/abs/2302.10685)\]
  > Identifies "offset spikes" as the dominant residual error and fixes it by shifting the initial membrane potential.
- A Unified Optimization Framework of ANN-SNN Conversion (**ICML 2023**). \[[paper](https://proceedings.mlr.press/v202/jiang23a.html)\]\[[code](https://github.com/HaiyanJiang/SNN_Conversion_unified)\]
  > A SlipReLU unifies performance-loss and conversion-error views — first to reach usable accuracy at a *single* timestep.
- Reducing ANN-SNN Conversion Error via Residual Membrane Potential Alignment (**arXiv 2026**). \[[paper](https://arxiv.org/abs/2608.13952)\]
  > The PKU conversion lineage (QCFS authors) attacks low-timestep error with dynamic initial-potential tuning and residual-alignment regularization.

#### 3.2 Surrogate Gradient & Direct Training

> Replace the spike's undefined derivative with a smooth "surrogate" and backpropagate through time. This is where most SOTA accuracy on hard datasets now comes from.

- Error-Backpropagation in Temporally Encoded Networks of Spiking Neurons (SpikeProp) (**Neurocomputing 2002**) ★. \[[paper](https://doi.org/10.1016/S0925-2312(01)00658-0)\]
  > The first backprop rule for temporally-coded spiking neurons — ancestor of all gradient-based SNN training.
- Training Deep Spiking Neural Networks Using Backpropagation (**Front. Neurosci. 2016**). \[[paper](https://doi.org/10.3389/fnins.2016.00508)\]
  > Treats the membrane potential as a differentiable signal and spikes as noise, letting standard backprop train deep SNNs.
- Spatio-Temporal Backpropagation for Training High-Performance SNNs (STBP) (**Front. Neurosci. 2018**) ★. \[[paper](https://doi.org/10.3389/fnins.2018.00331)\]\[[code](https://github.com/yjwu17/STBP-for-training-SpikingNN)\]
  > Unrolls the SNN in space *and* time (BPTT) with a surrogate derivative — the workhorse recipe for modern direct training.
- Direct Training for Spiking Neural Networks: Faster, Larger, Better (NeuNorm) (**AAAI 2019**). \[[paper](https://arxiv.org/abs/1809.05793)\]
  > Adds neuron normalization (NeuNorm) and improved coding to scale STBP to larger nets and neuromorphic datasets.
- SLAYER: Spike Layer Error Reassignment in Time (**NeurIPS 2018**) ★. \[[paper](https://papers.nips.cc/paper/7415-slayer-spike-layer-error-reassignment-in-time)\]\[[code](https://github.com/bamsumit/slayerPytorch)\]
  > Back-propagates error through time with a temporal credit-assignment kernel, jointly learning weights and axonal delays.
- SuperSpike: Supervised Learning in Multilayer Spiking Neural Networks (**Neural Computation 2018**). \[[paper](https://doi.org/10.1162/neco_a_01086)\]\[[code](https://github.com/fzenke/pub2018superspike)\]
  > An online three-factor surrogate-gradient rule linking deep learning to biological plasticity.
- The Remarkable Robustness of Surrogate Gradient Learning for Instilling Complex Function in SNNs (**Neural Computation 2021**). \[[paper](https://doi.org/10.1162/neco_a_01367)\]\[[code](https://github.com/fzenke/randman)\]
  > Learning is robust to surrogate *shape* but sensitive to its *scale* — practical design guidance.
- Temporal Spike Sequence Learning via Backpropagation for Deep SNNs (TSSL-BP) (**NeurIPS 2020**). \[[paper](https://arxiv.org/abs/2002.10085)\]\[[code](https://github.com/stonezwr/TSSL-BP)\]
  > Splits credit assignment into inter- and intra-neuron dependencies for precise temporal learning in very few steps.
- Differentiable Spike: Rethinking Gradient-Descent for Training SNNs (Dspike) (**NeurIPS 2021**). \[[paper](https://proceedings.neurips.cc/paper/2021/hash/c4ca4238a0b923820dcc509a6f75849b-Abstract.html)\]
  > An adaptively-tunable family of differentiable surrogates that minimizes gradient mismatch.
- Training Feedback SNNs by Implicit Differentiation on the Equilibrium State (IDE) (**NeurIPS 2021**). \[[paper](https://arxiv.org/abs/2109.14247)\]\[[code](https://github.com/pkuxmq/IDE-FSNN)\]
  > Trains feedback SNNs via implicit differentiation of their equilibrium state — memory cost independent of timesteps.
- Sparse Spiking Gradient Descent (**NeurIPS 2021**). \[[paper](https://arxiv.org/abs/2105.08810)\]\[[code](https://github.com/npvoid/SparseSpikingBackprop)\]
  > Exploits spatiotemporal sparsity in the backward pass for up to 150× faster, 85% lower-memory training.
- Temporal Efficient Training of SNNs via Gradient Re-weighting (TET) (**ICLR 2022**) ★. \[[paper](https://arxiv.org/abs/2202.11946)\]\[[code](https://github.com/Gus-Lab/temporal_efficient_training)\]
  > A per-timestep loss compensating surrogate-gradient momentum loss — flatter minima, better generalization; now a default trick.
- Training High-Performance Low-Latency SNNs by Differentiation on Spike Representation (DSR) (**CVPR 2022**). \[[paper](https://arxiv.org/abs/2205.00459)\]\[[code](https://github.com/qymeng94/DSR)\]
  > Treats the firing-rate representation as a sub-differentiable map and trains through it, sidestepping non-differentiability.
- Online Training Through Time for Spiking Neural Networks (OTTT) (**NeurIPS 2022**). \[[paper](https://arxiv.org/abs/2210.04195)\]\[[code](https://github.com/pkuxmq/OTTT-SNN)\]
  > A constant-memory online alternative to BPTT with a three-factor Hebbian form suited to on-chip learning.
- RecDis-SNN: Rectifying Membrane Potential Distribution for Directly Training SNNs (**CVPR 2022**). \[[paper](https://openaccess.thecvf.com/content/CVPR2022/html/Guo_RecDis-SNN_Rectifying_Membrane_Potential_Distribution_for_Directly_Training_Spiking_Neural_CVPR_2022_paper.html)\]
  > A membrane-potential distribution loss that mitigates degeneration, saturation, and gradient mismatch.
- IM-Loss: Information Maximization Loss for Spiking Neural Networks (**NeurIPS 2022**). \[[paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/010c5ba0cafc743fece8be02e7adb8dd-Abstract-Conference.html)\]\[[code](https://github.com/yfguo91/IM-Loss-Information-Maximization-Loss-for-Spiking-Neural-Networks)\]
  > Maximizes activation information entropy to counter the loss caused by 0/1 spike quantization.
- RMP-Loss: Regularizing Membrane Potential Distribution for Spiking Neural Networks (**ICCV 2023**). \[[paper](https://arxiv.org/abs/2308.06787)\]
  > A loss pulling membrane potentials toward spike values, directly shrinking quantization error.
- Real Spike: Learning Real-valued Spikes for Spiking Neural Networks (**ECCV 2022**). \[[paper](https://arxiv.org/abs/2210.06686)\]\[[code](https://github.com/yfguo91/Real-Spike)\]
  > Learns real-valued spikes during training, re-parameterized back to binary at inference — capacity for free.
- Surrogate Module Learning: Reduce Gradient Error Accumulation in Training SNNs (**ICML 2023**). \[[paper](https://proceedings.mlr.press/v202/deng23d.html)\]
  > Surrogate modules create a shortcut path for more accurate gradients, curbing layer-wise gradient-error buildup.
- Towards Memory- and Time-Efficient Backpropagation for Training SNNs (SLTT) (**ICCV 2023**). \[[paper](https://arxiv.org/abs/2302.14311)\]\[[code](https://github.com/qymeng94/SLTT)\]
  > Shows temporal backprop contributes little; dropping those routes cuts memory >70% and training time >50%.
- A Tandem Learning Rule for Effective Training and Rapid Inference of Deep SNNs (**IEEE TNNLS 2023**). \[[paper](https://arxiv.org/abs/1907.01167)\]\[[code](https://github.com/deepspike/tandem_learning)\]
  > Couples an ANN and SNN via weight sharing — the ANN carries gradients while the SNN counts spikes.
- Advancing Spatiotemporal Representations in SNNs via Parametric Invertible Transformation (PIT) (**ICLR 2026**). \[[paper](https://openreview.net/forum?id=3JwNXQzxll)\]\[[code](https://github.com/YinsongYan/ICLR26)\]
  > Conjugates an invertible transform with neuron dynamics and corrects surrogate-gradient mismatch, expanding the usable binary-spike representation space.
- Scalable Training of Continuous-Time SNNs with Differentiable Spike-Time Discretization (DSTD) (**arXiv 2026**). \[[paper](https://arxiv.org/abs/2607.14672)\]
  > Makes exact spike-time (continuous-time, event-driven) training memory-tractable by mapping irregular spikes onto differentiable fixed time points.
- Accurate and Efficient Time-Domain Classification with Adaptive Spiking Recurrent Neural Networks (**Nature Machine Intelligence 2021**). \[[paper](https://doi.org/10.1038/s42256-021-00397-w)\]
  > Adaptive spiking neurons + surrogate-gradient RSNNs reach RNN-level accuracy on speech/gesture at far less compute.
- Surrogate Gradient Learning in Spiking Neural Networks: Bringing the Power of Gradient-Based Optimization to Spiking Neural Networks (**IEEE Signal Processing Magazine 2019**) ★. \[[paper](https://doi.org/10.1109/MSP.2019.2931595)\]
  > Neftci, Mostafa & Zenke's tutorial review that frames surrogate gradients — smooth stand-ins for the spike's derivative — as the flexible, efficient way to train SNNs with gradient descent.
- Accurate Online Training of Dynamical Spiking Neural Networks Through Forward Propagation Through Time (FPTT) (**Nature Machine Intelligence 2023**). \[[paper](https://www.nature.com/articles/s42256-023-00650-4)\]\[[code](https://github.com/byin-cwi/sFPTT)\]
  > Pairs Forward-Propagation Through Time with liquid time-constant spiking neurons to train recurrent SNNs online with low memory, learning exceedingly long sequences and directly training a deep SNN for joint object localization and recognition.
- High-Performance Deep Spiking Neural Networks with 0.3 Spikes per Neuron (**Nature Communications 2024**). \[[paper](https://www.nature.com/articles/s41467-024-51110-5)\]
  > Traces vanishing/exploding gradients in time-to-first-spike SNNs to ANN-style initialization; a constant membrane-potential slope at threshold makes training mirror a ReLU network, matching ANN accuracy with under 0.3 spikes per neuron.
- Efficient Event-Based Delay Learning in Spiking Neural Networks (**Nature Communications 2025**). \[[paper](https://www.nature.com/articles/s41467-025-65394-8)\]
  > Extends EventProp to exact gradients for weights and delays, supporting multiple spikes per neuron and recurrent SNNs. It uses less than half the memory of the state-of-the-art delay-learning method and runs up to 26× faster.
- DelGrad: Exact Event-Based Gradients for Training Delays and Weights on Spiking Neuromorphic Hardware (**Nature Communications 2025**). \[[paper](https://www.nature.com/articles/s41467-025-63120-y)\]\[[code](https://github.com/JulianGoeltz/fastAndDeep)\]
  > Computes exact event-based gradients for both synaptic weights and delays from spike times alone, and shows on the BrainScaleS-2 chip that learned delays improve accuracy, parameter efficiency and robustness to hardware noise.
- Training Deep Normalization-Free Spiking Neural Networks with Lateral Inhibition (**ICLR 2026**). \[[paper](https://arxiv.org/abs/2509.23253)\]\[[code](https://github.com/vwOvOwv/DeepEISNN)\]
  > Replaces standard SNN layers with cortical excitatory–inhibitory populations whose subtractive and divisive inhibition regulate activity, with E-I Init and E-I Prop stabilizing deep SNN training without normalization.
- Temporal Representation Enhancement (TRE): Learning to Forget Dominant Patterns for Enhanced Temporal Spiking Features (**CVPR 2026**). \[[paper](https://cvpr.thecvf.com/virtual/2026/poster/37392)\]
  > Counters redundancy from timestep-invariant supervision with a learning-to-forget scheme that accumulates class-specific contributions and dynamically suppresses dominant patterns, steering SNNs toward complementary temporal features.

#### 3.3 Biologically-Plausible / Local Learning

> **STDP** and friends: synapses strengthen or weaken based purely on the *relative timing* of pre- and post-synaptic spikes — local, unsupervised, and hardware-friendly, but historically hard to push to ImageNet scale.

- Synaptic Modifications in Cultured Hippocampal Neurons: Dependence on Spike Timing... (**J. Neuroscience 1998**) ★. \[[paper](https://doi.org/10.1523/JNEUROSCI.18-24-10464.1998)\]
  > Bi & Poo's landmark experiment quantifying STDP — the biological basis of local SNN learning rules.
- Regulation of Synaptic Efficacy by Coincidence of Postsynaptic APs and EPSPs (**Science 1997**) ★. \[[paper](https://doi.org/10.1126/science.275.5297.213)\]
  > Dual whole-cell recordings between neocortical pyramidal neurons show unitary EPSPs grow or shrink with the precise timing of postsynaptic APs. A founding STDP experiment alongside Bi & Poo.
- Competitive Hebbian Learning Through Spike-Timing-Dependent Synaptic Plasticity (**Nature Neuroscience 2000**) ★. \[[paper](https://www.nature.com/articles/nn0900_919)\]
  > Models show STDP itself produces Hebbian synaptic competition. Weights balance automatically, and inputs that fire the neuron with short latency or in correlated groups win while longer-latency inputs weaken.
- Unsupervised Learning of Digit Recognition Using STDP (**Front. Comput. Neurosci. 2015**) ★. \[[paper](https://doi.org/10.3389/fncom.2015.00099)\]\[[code](https://github.com/peter-u-diehl/stdp-mnist)\]
  > Diehl & Cook's STDP + lateral-inhibition network learns MNIST unsupervised (~95%) — the canonical bio-plausible baseline.
- STDP-Based Spiking Deep Convolutional Neural Networks for Object Recognition (**Neural Networks 2018**). \[[paper](https://doi.org/10.1016/j.neunet.2017.12.005)\]
  > Stacks STDP-trained conv layers with latency coding, showing local plasticity can learn deep hierarchical features.
- Bio-Inspired Digit Recognition Using Reward-Modulated STDP in Deep Conv Networks (**Pattern Recognition 2019**). \[[paper](https://arxiv.org/abs/1804.00227)\]\[[code](https://github.com/miladmozafari/SpykeTorch)\]
  > Combines unsupervised STDP with reward-modulated STDP (a three-factor rule) for reinforcement-driven feature learning.
- A Solution to the Learning Dilemma for Recurrent Networks of Spiking Neurons (e-prop) (**Nature Communications 2020**) ★. \[[paper](https://doi.org/10.1038/s41467-020-17236-y)\]\[[code](https://github.com/IGITUGraz/eligibility_propagation)\]
  > Local eligibility traces + top-down learning signals approximate BPTT without backward-in-time — enabling on-chip learning.
- Equilibrium Propagation: Bridging Energy-Based Models and Backpropagation (**Front. Comput. Neurosci. 2017**). \[[paper](https://doi.org/10.3389/fncom.2017.00024)\]
  > Computes exact gradients using only local, same-type computation across two phases — a biologically plausible backprop alternative.
- Training Spiking Neural Networks via Augmented Direct Feedback Alignment (**NeurIPS 2024**). \[[paper](https://arxiv.org/abs/2409.07776)\]
  > A gradient-free random-projection feedback-alignment rule avoiding weight transport, improving biological/hardware fit.
- Backpropagation-Free Spiking Neural Networks with the Forward-Forward Algorithm (**arXiv 2025**). \[[paper](https://arxiv.org/abs/2502.20411)\]
  > Adapts Hinton's Forward-Forward (two contrastive forward passes, layer-local goodness) to spiking neurons.
- Spike-Based Alignment Learning Solves the Weight Transport Problem (**Nature Communications 2026**). \[[paper](https://www.nature.com/articles/s41467-026-74460-8)\]
  > Bern/Heidelberg derive a spike-timing rule that aligns feedback weights locally — resolving weight transport for bio-plausible and on-chip credit assignment.
- The Tempotron: A Neuron That Learns Spike Timing-Based Decisions (**Nature Neuroscience 2006**) ★. \[[paper](https://doi.org/10.1038/nn1643)\]
  > Gütig & Sompolinsky's tempotron — a single neuron that learns to classify by the *timing* of its input spikes.
- Unsupervised Learning of Visual Features through Spike-Timing-Dependent Plasticity (**PLoS Comput. Biol. 2007**) ★. \[[paper](https://doi.org/10.1371/journal.pcbi.0030031)\]
  > Masquelier & Thorpe show STDP + latency coding self-organizes selective visual features — a landmark unsupervised result.
- Burst-Dependent Synaptic Plasticity Can Coordinate Learning in Hierarchical Circuits (Burstprop) (**Nature Neuroscience 2021**). \[[paper](https://doi.org/10.1038/s41593-021-00857-x)\]\[[code](https://github.com/apayeur/spikingburstprop)\]
  > When plasticity is gated by high-frequency spike bursts, higher-level pyramidal neurons can coordinate lower-level synapses; with short-term dynamics, apical dendritic activity and feedback plasticity, the rule solves deep-architecture tasks.
- Brain-Inspired Global-Local Learning Incorporated with Neuromorphic Computing (**Nature Communications 2022**). \[[paper](https://doi.org/10.1038/s41467-021-27653-2)\]
  > Meta-learns local synaptic plasticity together with top-down, error-driven supervision in a differentiable spiking model, outperforming single-rule learning on few-shot, continual and fault-tolerant tasks; co-designed for and run on Tianjic.
- The Combination of Hebbian and Predictive Plasticity Learns Invariant Object Representations in Deep Sensory Networks (**Nature Neuroscience 2023**). \[[paper](https://doi.org/10.1038/s41593-023-01460-y)\]\[[code](https://github.com/fmi-basel/latent-predictive-learning)\]
  > Latent predictive learning (LPL) adds predictive plasticity to Hebbian plasticity, giving a local rule that learns invariant object representations in deep networks, extends to spiking networks and reproduces STDP and metaplasticity.
- The Backpropagation Algorithm Implemented on Spiking Neuromorphic Hardware (**Nature Communications 2024**). \[[paper](https://www.nature.com/articles/s41467-024-53827-9)\]
  > Implements exact backpropagation entirely on Intel Loihi via synfire-gated dynamical information coordination; a three-layer spiking circuit learns MNIST and Fashion-MNIST with no computer in the loop.
- Co-Dependent Excitatory and Inhibitory Plasticity Accounts for Quick, Stable and Long-Lasting Memories in Biological Networks (**Nature Neuroscience 2024**). \[[paper](https://doi.org/10.1038/s41593-024-01597-4)\]\[[code](https://github.com/ejagnes/codependent_plasticity)\]
  > Co-dependent plasticity in spiking LIF neurons: inhibition gates excitatory plasticity and neighbouring excitatory activity sets LTP strength, so synaptic memories form quickly yet stay stable.
- Online Pseudo-Zeroth-Order Training of Neuromorphic Spiking Neural Networks (**ICLR 2026**). \[[paper](https://arxiv.org/abs/2407.12516)\]
  > Trains SNNs with a single noise-injected forward pass and direct top-down feedback, using a pseudo-zeroth-order formulation and momentum feedback to tame variance and avoid backprop's symmetric weights for on-chip learning.
- Model-Agnostic Linear-Memory Online Learning in Spiking Neural Networks (BrainTrace) (**Nature Communications 2026**). \[[paper](https://www.nature.com/articles/s41467-026-68453-w)\]\[[code](https://github.com/chaobrain/braintrace)\]
  > Compiles user-defined neuron and synapse dynamics into eligibility-trace online learning whose memory grows linearly with neuron count, and fits a connectome-constrained whole-brain Drosophila SNN to region-level activity.

#### 3.4 Efficiency: Pruning, Quantization, Distillation

> Making an already-efficient model *more* efficient: fewer timesteps, fewer weights, lower precision, and distilling knowledge from ANN teachers.

- Towards Ultra-Low-Latency SNNs for Vision and Sequential Tasks Using Temporal Pruning (**ECCV 2022**). \[[paper](https://doi.org/10.1007/978-3-031-20083-0_42)\]
  > Iteratively prunes timesteps during training, driving SNNs toward single-timestep inference.
- Constructing Deep SNNs from ANNs with Knowledge Distillation (**CVPR 2023**). \[[paper](https://arxiv.org/abs/2304.05627)\]
  > Uses an ANN teacher to distill feature/response knowledge into an SNN student, avoiding costly from-scratch training.
- TP-Spikformer: Token Pruned Spiking Transformer (**ICLR 2026**). \[[paper](https://openreview.net/forum?id=L5llQD0nMf)\]
  > Prunes low-information tokens without retraining across several spiking-Transformer families, reducing storage and compute while retaining competitive accuracy.
- Towards Lossless Memory-efficient Training of SNNs via Gradient Checkpointing and Spike Compression (**ICLR 2026**). \[[paper](https://openreview.net/forum?id=nrBJ0Uvj7c)\]\[[code](https://github.com/AllenYolk/snn-gradient-checkpointing)\]
  > Combines adaptive spatiotemporal checkpointing with lossless binary-spike compression for up to 8× lower training memory without accuracy loss.

> Also relevant: several low-timestep / low-memory training methods double as efficiency techniques — see **TET**, **SLTT**, **DSR** in [3.2](#32-surrogate-gradient--direct-training) and **DIET-SNN** in [Neural Coding](#1--foundations--neural-coding).

---

### 4 · Architectures

> **In one breath:** the network *shape*. The 2019–2021 breakthrough was getting **residual/BN tricks** to work in the spiking domain so SNNs could go deep; the 2023+ wave brought **spiking Transformers**, redesigning self-attention to run on spikes.

#### 4.1 Deep Spiking CNNs & ResNets

> Residual connections and spike-aware normalization (tdBN, BNTT, TEBN) are what let SNNs scale past a few layers without spikes vanishing or exploding.

- Spiking Deep Residual Networks (**IEEE TNNLS 2021**). \[[paper](https://arxiv.org/abs/1805.01352)\]
  > The original "Spiking ResNet" — scaled shortcuts + error compensation build the first >40-layer SNN matching ANN accuracy.
- Deep Residual Learning in Spiking Neural Networks (SEW-ResNet) (**NeurIPS 2021**) ★. \[[paper](https://arxiv.org/abs/2102.04159)\]\[[code](https://github.com/fangwei123456/Spike-Element-Wise-ResNet)\]
  > The spike-element-wise (SEW) block enables identity mapping and solves vanishing/exploding gradients — first directly-trained 100+ layer SNNs.
- Advancing Spiking Neural Networks Toward Deep Residual Learning (MS-ResNet) (**IEEE TNNLS 2024**). \[[paper](https://arxiv.org/abs/2112.08954)\]\[[code](https://github.com/Ariande1/MS-ResNet)\]
  > Membrane-potential (pre-activation) shortcuts preserve spike-driven computation and gradient-norm equality, scaling to 482 layers.
- Going Deeper with Directly-Trained Larger SNNs (STBP-tdBN) (**AAAI 2021**) ★. \[[paper](https://arxiv.org/abs/2011.05280)\]
  > Threshold-dependent BatchNorm (tdBN) balances firing rates across time, extending directly-trained SNNs from <10 to 50 layers.
- Revisiting Batch Normalization for Training Low-Latency Deep SNNs from Scratch (BNTT) (**Front. Neurosci. 2021**). \[[paper](https://arxiv.org/abs/2010.01729)\]\[[code](https://github.com/Intelligent-Computing-Lab-Panda/BNTT-Batch-Normalization-Through-Time)\]
  > Decouples BN parameters along the time axis to capture spike temporal dynamics and enable low-latency training from scratch.
- Temporal Effective Batch Normalization in Spiking Neural Networks (TEBN) (**NeurIPS 2022**). \[[paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/de2ad3ed44ee4e675b3be42aa0b615d0-Abstract-Conference.html)\]\[[code](https://github.com/ChaotengDuan/TEBN)\]
  > Rescales inputs with distinct learnable weights per time-step, smoothing temporal distributions and the optimization landscape.
- Membrane Potential Batch Normalization for Spiking Neural Networks (MPBN) (**ICCV 2023**). \[[paper](https://arxiv.org/abs/2308.08359)\]\[[code](https://github.com/yfguo91/MPBN)\]
  > A second BN on the membrane potential before firing, folded into the threshold by re-parameterization — zero inference cost.

#### 4.2 Spiking Transformers & Attention

> Self-attention, re-derived so that queries/keys/values are spikes and the expensive softmax is replaced by spike-friendly operations — bringing Transformer-level accuracy to the spiking world.

- Spikformer: When Spiking Neural Network Meets Transformer (**ICLR 2023**) ★. \[[paper](https://arxiv.org/abs/2209.15425)\]\[[code](https://github.com/ZK-Zhou/spikformer)\]
  > Introduces softmax-free Spiking Self-Attention (SSA) with spike-form Q/K/V — the first vision Transformer built directly in the spiking domain.
- Spike-driven Transformer (**NeurIPS 2023**) ★. \[[paper](https://arxiv.org/abs/2307.01694)\]\[[code](https://github.com/BICLab/Spike-Driven-Transformer)\]
  > A purely spike-driven Transformer whose attention uses only mask + sparse addition (linear complexity), cutting attention energy up to 87×.
- Spike-driven Transformer V2 (Meta-SpikeFormer) (**ICLR 2024**). \[[paper](https://arxiv.org/abs/2404.03663)\]\[[code](https://github.com/BICLab/Spike-Driven-Transformer-V2)\]
  > A meta spiking backbone unifying classification, detection, and segmentation, guiding next-gen neuromorphic chip design (80% ImageNet).
- Scaling Spike-driven Transformer with Efficient Spike Firing Approximation (V3) (**IEEE TPAMI 2025**). \[[paper](https://arxiv.org/abs/2411.16061)\]\[[code](https://github.com/BICLab/Spike-Driven-Transformer-V3)\]
  > Integer training + spike-driven inference plus a spike masked autoencoder scale SNNs to 86.2% on ImageNet.
- Spikformer V2: Join the High-Accuracy Club on ImageNet with an SNN Ticket (**arXiv 2024**). \[[paper](https://arxiv.org/abs/2401.02020)\]
  > A Spiking Convolutional Stem + self-supervised pretraining — among the first SNNs past 80% top-1 on ImageNet.
- QKFormer: Hierarchical Spiking Transformer using Q-K Attention (**NeurIPS 2024**). \[[paper](https://arxiv.org/abs/2403.16552)\]\[[code](https://github.com/zhouchenlin2096/QKFormer)\]
  > Linear-complexity binary Q-K attention + hierarchical pyramid — first directly-trained SNN past 85% top-1 on ImageNet.
- Spikingformer: A Key Foundation Model for Spiking Neural Networks (**AAAI 2026**). \[[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37207)\]\[[code](https://github.com/TheBrainLab/Spikingformer)\]
  > Replaces Spikformer's non-spike residuals with a fully spike-driven design, removing integer-float multiplications for hardware friendliness.
- SpikingResformer: Bridging ResNet and Vision Transformer in SNNs (**CVPR 2024**). \[[paper](https://arxiv.org/abs/2403.14302)\]\[[code](https://github.com/xyshi2000/SpikingResformer)\]
  > Combines a ResNet-style multi-stage backbone with Dual Spike Self-Attention (DSSA) for high accuracy at fewer params/energy.
- Masked Spiking Transformer (**ICCV 2023**). \[[paper](https://openaccess.thecvf.com/content/ICCV2023/html/Wang_Masked_Spiking_Transformer_ICCV_2023_paper.html)\]\[[code](https://github.com/bic-L/Masked-Spiking-Transformer)\]
  > An ANN-to-SNN converted Transformer with Random Spike Masking that prunes redundant spikes to cut energy without accuracy loss.
- Spiking Transformer with Spatial-Temporal Attention (STAtten) (**CVPR 2025**). \[[paper](https://arxiv.org/abs/2409.19764)\]\[[code](https://github.com/Intelligent-Computing-Lab-Panda/STAtten)\]
  > Block-wise attention jointly integrating spatial and temporal information at the cost of spatial-only spiking attention.
- Neural Dynamics Self-Attention for Spiking Transformers (**ICLR 2026**). \[[paper](https://openreview.net/forum?id=jJedqisfOt)\]
  > Adds a local receptive-field bias and realizes attention through charge–fire–reset dynamics, avoiding explicit attention-matrix storage at inference.
- Ge²mS-T: Multi-Dimensional Grouping for Ultra-High Energy Efficiency in Spiking Transformer (**ACM MM 2026**). \[[paper](https://arxiv.org/abs/2604.08894)\]
  > PKU's multi-dimensional grouped computation plus an exponential-coding ExpG-IF neuron jointly balances memory, learning and energy (Oral).
- Rethinking Attention Locality in Spiking Transformers (**arXiv 2026**). \[[paper](https://arxiv.org/abs/2608.08541)\]
  > Mean-attention-distance analysis shows "local" spiking attention needn't be spatially local, and proposes region-contiguous attention as the fix.
- TIM: An Efficient Temporal Interaction Module for Spiking Transformer (**IJCAI 2024**). \[[paper](https://arxiv.org/abs/2401.11687)\]
  > A lightweight convolutional module injecting previous-timestep information into the attention matrix, strengthening temporal modeling.
- Temporal-wise Attention Spiking Neural Networks for Event Streams Classification (TA-SNN) (**ICCV 2021**). \[[paper](https://openaccess.thecvf.com/content/ICCV2021/html/Yao_Temporal-Wise_Attention_Spiking_Neural_Networks_for_Event_Streams_Classification_ICCV_2021_paper.html)\]\[[code](https://github.com/BICLab/TA-SNN)\]
  > Temporal-wise attention weights event frames and discards noisy ones — a landmark attention-SNN for event data.
- Attention Spiking Neural Networks (MA-SNN) (**IEEE TPAMI 2023**). \[[paper](https://arxiv.org/abs/2209.13929)\]\[[code](https://github.com/BICLab/Attention-SNN)\]
  > Multi-dimensional (temporal/channel/spatial) attention modulates membrane potentials, yielding sparser firing and higher accuracy.
- Bipolar Self-Attention for Spiking Transformers (**NeurIPS 2025**). \[[paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/9316cfcb0a81e53a1f35b4353f115571-Abstract-Conference.html)\]
  > Models homopolar and heteropolar Query-Key membrane-potential interactions via ternary matrix multiplication, and adds Shiftmax, a shift-based Softmax approximation that partly restores row-stochastic attention while staying fully spike-driven (Spotlight).
- Toward Relative Positional Encoding in Spiking Transformers (**NeurIPS 2025**). \[[paper](https://arxiv.org/abs/2501.16745)\]\[[code](https://github.com/microsoft/SeqSNN)\]
  > Approximates relative positional encoding with strictly binary spikes: Gray-PE encodes distances in Gray code (constant Hamming distance at power-of-two offsets), and Log-PE folds log-distance into the spiking attention map (Spotlight).
- SmoothSpike: Spiking Transformer with Learnable Hadamard Transformation (**ICML 2026**). \[[paper](https://proceedings.mlr.press/v306/zhou26ax.html)\]\[[code](https://github.com/CayleyZ/SmoothSpike)\]
  > Traces spiking Transformers' language-modeling gap to spike-saturation homogenization, smoothing pre-activations with a randomized Hadamard rotation made learnable via Newton–Schulz orthogonal updates and fused into weights at inference.

#### 4.3 Recurrent, Reservoir & Other

> Recurrent SNNs (LSNN), liquid state machines, spiking GNNs/autoencoders/GANs, and neural-architecture-searched SNNs.

**Recurrent & Reservoir**
- Long Short-Term Memory and Learning-to-Learn in Networks of Spiking Neurons (LSNN) (**NeurIPS 2018**) ★. \[[paper](https://arxiv.org/abs/1803.09574)\]\[[code](https://github.com/IGITUGraz/LSNN-official)\]
  > Adaptive-threshold (ALIF) neurons + BPTT learning-to-learn first matched LSTM-level temporal computing power.
- Real-Time Computing Without Stable States (Liquid State Machine) (**Neural Computation 2002**) ★. \[[paper](https://direct.mit.edu/neco/article/14/11/2531/6650)\]
  > The foundational Liquid State Machine / reservoir-computing model — a recurrent spiking circuit projects inputs into a high-dimensional readable state.

**Spiking Graph Neural Networks**
- Spiking Graph Convolutional Networks (SpikingGCN) (**IJCAI 2022**). \[[paper](https://arxiv.org/abs/2205.02767)\]\[[code](https://github.com/ZulunZhu/SpikingGCN)\]
  > Encodes graph convolution into spike trains end-to-end, bringing energy-efficient SNN inference to node/graph tasks.
- Scaling Up Dynamic Graph Representation Learning via Spiking Neural Networks (SpikeNet) (**AAAI 2023**). \[[paper](https://ojs.aaai.org/index.php/AAAI/article/view/26034)\]\[[code](https://github.com/EdisonLeeeee/SpikeNet)\]
  > Replaces RNNs with spiking neurons to scale temporal graph learning to millions of nodes at low compute.
- A Graph is Worth 1-bit Spikes: Graph Contrastive Learning Meets SNNs (SpikeGCL) (**ICLR 2024**). \[[paper](https://arxiv.org/abs/2305.19306)\]\[[code](https://github.com/EdisonLeeeee/SpikeGCL)\]
  > Learns binarized 1-bit graph representations via spiking contrastive learning — ~32× storage compression at comparable accuracy.
- Dynamic Spiking Graph Neural Networks (Dy-SIGN) (**AAAI 2024**). \[[paper](https://arxiv.org/abs/2401.05373)\]
  > Tackles information loss in dynamic spiking GNNs with implicit differentiation and information compensation.

**Spiking Generative Models**
- Spiking-GAN: A Spiking Generative Adversarial Network Using Time-to-First-Spike Coding (**IJCNN 2022**). \[[paper](https://arxiv.org/abs/2106.15420)\]
  > The first spike-based GAN, trained with temporal coding and BPTT for ultra-low-energy generation.
- Spiking Denoising Diffusion Probabilistic Models (SDDPM) (**WACV 2024**). \[[paper](https://arxiv.org/abs/2306.17046)\]\[[code](https://github.com/SageCao1125/SDDPM)\]
  > Brings diffusion models into SNNs with a Spiking U-Net backbone, matching/beating ANN DDPM on FID.
- SDiT: Spiking Diffusion Model with Transformer (**arXiv 2024**). \[[paper](https://arxiv.org/abs/2402.11588)\]
  > Replaces the diffusion U-Net with a spiking Transformer backbone for higher-quality, lower-cost SNN image generation.
- Spiking Generative Adversarial Network with Attention Scoring Decoding (**Neural Networks 2024**). \[[paper](https://arxiv.org/abs/2305.10246)\]
  > An attention-scoring decoder generates higher-fidelity images from spike features.
- Fully Spiking Variational Autoencoder (FSVAE) (**AAAI 2022**). \[[paper](https://arxiv.org/abs/2110.00375)\]
  > The first fully-spiking VAE — samples latent variables as autoregressive Bernoulli spike trains, generating images end-to-end in spikes.

**Neural Architecture Search for SNNs**
- Neural Architecture Search for Spiking Neural Networks (SNASNet) (**ECCV 2022**). \[[paper](https://arxiv.org/abs/2201.10355)\]\[[code](https://github.com/Intelligent-Computing-Lab-Panda/Neural-Architecture-Search-for-Spiking-Neural-Networks)\]
  > Training-free NAS selecting architectures by spike-activation diversity at initialization, plus temporal backward connections.
- AutoSNN: Towards Energy-Efficient Spiking Neural Networks (**ICML 2022**). \[[paper](https://arxiv.org/abs/2201.12738)\]\[[code](https://github.com/nabk89/AutoSNN)\]
  > Spike-aware architecture search whose fitness jointly optimizes accuracy and spike count.
- Differentiable Hierarchical and Surrogate Gradient Search for SNNs (SpikeDHS) (**NeurIPS 2022**). \[[paper](https://openreview.net/forum?id=Lr2Z85cdvB)\]\[[code](https://github.com/Huawei-BIC/SpikeDHS)\]
  > Jointly and differentiably searches cell/layer architecture and the surrogate-gradient function.
- Supervised Learning in Spiking Neural Networks with FORCE Training (**Nature Communications 2017**). \[[paper](https://doi.org/10.1038/s41467-017-01827-3)\]\[[code](https://modeldb.science/190565)\]
  > Applies FORCE training (recursive least-squares weight learning) directly to recurrent spiking networks, which learn to mimic dynamical systems, classify inputs, reproduce zebra-finch song, and store and replay a movie scene.
- A Long Short-Term Memory for AI Applications in Spike-Based Neuromorphic Hardware (**Nature Machine Intelligence 2022**). \[[paper](https://www.nature.com/articles/s42256-022-00480-w)\]\[[code](https://github.com/intel-nrc-ecosystem/models/tree/master/nxsdk_modules_ncl/lsnn)\]
  > Uses slow after-hyperpolarizing currents in spiking neurons to emulate LSTM units on Loihi, explained by filter-approximation theory, enabling sparse, energy-efficient time-series classification and question answering about text.
- A Framework for the General Design and Computation of Hybrid Neural Networks (**Nature Communications 2022**). \[[paper](https://doi.org/10.1038/s41467-022-30964-7)\]\[[code](https://github.com/IbrahimYang/Hybrid-neural-networks)\]
  > Proposes hybrid units, hand-designed or learned, as a general interface between SNN and ANN modules, demonstrated by hybrid sensing, modulation and reasoning networks for tracking, meta-continual learning and multimodal reasoning.
- Neuromorphic Visual Scene Understanding with Resonator Networks (**Nature Machine Intelligence 2024**). \[[paper](https://www.nature.com/articles/s42256-024-00848-0)\]\[[code](https://doi.org/10.5281/zenodo.10810900)\]
  > Factorizes visual scenes into object identity and pose with hierarchical resonator networks over complex-valued vector-symbolic codes, run on Loihi via multi-compartment spiking phasor neurons encoding phase in spike timing.
- Adaptive Spatiotemporal Neural Networks Through Complementary Hybridization (**Nature Communications 2024**). \[[paper](https://www.nature.com/articles/s41467-024-51641-x)\]
  > Hybridizes recurrent ANN and spiking neurons in one network trained by unified surrogate-gradient BPTT. Hessian-aware neuron selection tunes their ratio to trade accuracy, robustness and efficiency; the network is deployed on the TianjicX chip.
- Hybrid Neural Networks for Continual Learning Inspired by Corticohippocampal Circuits (CH-HNN) (**Nature Communications 2025**). \[[paper](https://www.nature.com/articles/s41467-025-56405-9)\]\[[code](https://github.com/qqish/CH-HNN)\]
  > An ANN infers similarities across episodes and emits modulation masks for an SNN that learns episode-specific memories, with metaplasticity curbing catastrophic forgetting without task IDs; deployed on quadruped and robotic-arm platforms.

---

### 5 · Spiking Large Models & LLMs

> **In one breath:** the fastest-moving frontier — spiking **language models** and **multimodal** models that bring Transformer/LLM-scale capability into the event-driven, energy-efficient spiking world. (Vision spiking Transformers live in [§4.2](#42-spiking-transformers--attention).)

- SpikeGPT: Generative Pre-trained Language Model with Spiking Neural Networks (**TMLR 2024**) ★. \[[paper](https://arxiv.org/abs/2302.13939)\]\[[code](https://github.com/ridgerchu/SpikeGPT)\]
  > The first large generative spiking language model (up to 260M params), linearizing attention for ~20× fewer operations.
- Spiking Convolutional Neural Networks for Text Classification (**ICLR 2023**). \[[paper](https://openreview.net/forum?id=pgU3k7QXuz0)\]\[[code](https://github.com/Lvchangze/snn)\]
  > A conversion-plus-fine-tuning recipe encoding word embeddings as spikes, matching ANN text classifiers with more robustness.
- SpikingBERT: Distilling BERT to Train Spiking Language Models Using Implicit Differentiation (**AAAI 2024**). \[[paper](https://ojs.aaai.org/index.php/AAAI/article/view/28975)\]
  > A spiking BERT trained via implicit-differentiation equilibrium + ANN-to-SNN distillation, bringing SNNs to NLU tasks.
- SpikeBERT: A Language Spikformer Learned from BERT with Knowledge Distillation (**arXiv 2023**). \[[paper](https://arxiv.org/abs/2308.15122)\]\[[code](https://github.com/Lvchangze/SpikeBERT)\]
  > Two-stage distillation from BERT into a Spikformer, matching BERT on English/Chinese text classification at far lower energy.
- SpikeLM: Towards General Spike-Driven Language Modeling via Elastic Bi-Spiking Mechanisms (**ICML 2024**). \[[paper](https://arxiv.org/abs/2406.03287)\]\[[code](https://github.com/Xingrun-Xing/SpikeLM)\]
  > A fully spike-driven mechanism handling both discriminative and generative language tasks with elastic bidirectional spikes.
- SpikeLLM: Scaling up Spiking Neural Networks to Large Language Models via Saliency-Based Spiking (**arXiv 2024**). \[[paper](https://arxiv.org/abs/2407.04752)\]
  > The first spiking LLM scaled to 7–70B params, using generalized IF neurons and saliency-based spiking to beat quantization baselines.
- SpikeZIP-TF: Conversion is All You Need for Transformer-based SNN (**ICML 2024**). \[[paper](https://arxiv.org/abs/2406.03470)\]\[[code](https://github.com/Intelligent-Computing-Research-Group/SpikeZIP-TF)\]
  > Losslessly converts quantized Transformers into SNNs, closing the accuracy gap with ANN Transformers on vision and language.
- SpikingBrain: Spiking Brain-inspired Large Models (**TMLR 2026**) ★. \[[paper](https://arxiv.org/abs/2509.05276)\]\[[code](https://github.com/BICLab/SpikingBrain-7B)\]
  > CAS (Li Guoqi & Bo Xu) 7B-linear / 76B-MoE spiking LLMs with adaptive spike coding — >100× TTFT speedup on 4M-token contexts, trained on domestic (MetaX) GPUs.
- SpikingBrain2.0: Brain-Inspired Foundation Models for Efficient Long-Context and Cross-Platform Inference (**arXiv 2026**). \[[paper](https://arxiv.org/abs/2604.22575)\]\[[code](https://github.com/BICLab/SpikingBrain2.0)\]
  > Extends the family to 5B language and vision-language models with dual sparse attention and INT8-spiking / FP8 paths, supporting 10M+ tokens and GPU or neuromorphic inference — 5B base/instruct/think and VL-5B weights open-sourced May 2026.
- Neuromorphic Spike-based Large Language Model (NSLLM) (**National Science Review 2026**) ★. \[[paper](https://academic.oup.com/nsr/article/13/4/nwaf551/8365570)\]
  > CAS-IA/BAAI/UCSC convert LLMs into MatMul-free spike-based models — a 1.5B NSLLM on an AMD VCK190 FPGA runs at ~13.8 W with 19.8× energy efficiency and 21.3× memory reduction vs an A800.
- Spike-driven Large Language Model (**arXiv 2026**). \[[paper](https://arxiv.org/abs/2604.16475)\]
  > Replaces dense MatMuls with sparse additions via a two-step γ-SQP spike encoding — ~7× lower energy and +4.2% accuracy over prior spike-based LLMs.
- SpikeMLLM: Spike-based Multimodal Large Language Models (**arXiv 2026**). \[[paper](https://arxiv.org/abs/2604.18610)\]
  > First spike-based multimodal-LLM framework — modality-specific temporal scales and temporally-compressed LIF cut timesteps to log₂(L)−1 at near-lossless accuracy.
- LAS: Loss-less ANN-SNN Conversion for Fully Spike-Driven Large Language Models (**AAAI 2026**). \[[paper](https://ojs.aaai.org/index.php/AAAI/article/view/37151)\]
  > Sichuan Univ. neurons handling activation outliers and nonlinear ops make LLM/VLM conversion loss-less across six language and two vision-language models.
- SpikeVLA: Vision-Language-Action Models with Spiking Neural Networks (**ICML 2026**). \[[paper](https://arxiv.org/abs/2606.27807)\]
  > First spiking vision-language-action framework — spiking vision encoder, multimodal spiking LM and population-coded action policy for embodied control.
- Neuromorphic Principles for Efficient Large Language Models on Intel Loihi 2 (**arXiv 2025**). \[[paper](https://arxiv.org/abs/2503.18002)\]
  > Intel Labs + UCSC run a 370M MatMul-free LLM on Loihi 2 — up to 3× throughput at 2× less energy than an edge GPU.
- Neuromorphic Diffusion Language Models (N-MDLM) (**IEEE SiPS 2026**). \[[paper](https://arxiv.org/abs/2607.24841)\]
  > KCL fuses block-diffusion LLMs with spike-based computation — multiple tokens per parameter access plus spike-induced channel sparsity.
- Sorbet: A Neuromorphic Hardware-Compatible Transformer-Based Spiking Language Model (**ICML 2025**). \[[paper](https://arxiv.org/abs/2409.15298)\]
  > Replaces softmax and LayerNorm with shift-based PTsoftmax/BSPN for a hardware-friendly spiking LM — ~27× energy savings vs BERT on GLUE.
- SpikeCLIP: A Contrastive Language-Image Pretrained Spiking Neural Network (**Neural Networks 2025**). \[[paper](https://arxiv.org/abs/2310.06488)\]\[[code](https://github.com/Lvchangze/SpikeCLIP)\]
  > A CLIP-style *multimodal* spiking model aligning image and text in spike space — extends SNNs to vision-language.

---

<p align="right"><a href="#table-of-contents">↑ Back to top</a></p>

## Part III · Hardware & Systems

### 6 · Neuromorphic Hardware

> **In one breath:** SNNs only pay off when the *chip* is event-driven too. **Digital** platforms (TrueNorth, Loihi, SpiNNaker, Tianjic) route spikes as packets and idle between them; **analog/in-memory** designs (BrainScaleS, memristor/RRAM crossbars) compute inside the memory to kill the von-Neumann data-movement cost. **Event cameras** (DVS) are the matching sensor.

#### Foundations of Neuromorphic Engineering

- Neuromorphic Electronic Systems (**Proceedings of the IEEE 1990**) ★. \[[paper](https://doi.org/10.1109/5.58356)\]
  > Carver Mead's founding manifesto — analog VLSI that mimics neural computation. The paper that named the field.
- A Silicon Neuron (**Nature 1991**) ★. \[[paper](https://www.nature.com/articles/354515a0)\]
  > Mahowald & Douglas's analog VLSI neuron reproducing real spiking dynamics — the first silicon neuron.
- Point-to-Point Connectivity Between Neuromorphic Chips Using Address Events (**IEEE TCAS-II 2000**). \[[paper](https://doi.org/10.1109/82.842110)\]
  > Boahen formalizes Address-Event Representation (AER) — the spike-as-packet protocol every neuromorphic chip now uses.
- Efficient Training of Neuromorphic Electronics (**Nature Electronics 2026**). \[[paper](https://www.nature.com/articles/s41928-026-01631-2)\]
  > A heavyweight review (Tang, Linares-Barranco, Indiveri et al.) of off-chip, on-chip and hybrid training strategies across digital, mixed-signal and emerging neuromorphic hardware.
- Towards Spike-Based Machine Intelligence with Neuromorphic Computing (**Nature 2019**) ★. \[[paper](https://www.nature.com/articles/s41586-019-1677-2)\]
  > Roy, Jaiswal & Panda's Nature Perspective surveys spike-based learning algorithms and event-driven neuromorphic hardware together, with particular emphasis on algorithm–hardware co-design for energy-efficient machine intelligence.
- Neuro-Inspired Computing Chips (**Nature Electronics 2020**). \[[paper](https://www.nature.com/articles/s41928-020-0435-7)\]
  > Tsinghua-led review of ANN and SNN chips. It proposes four benchmarks (computing density, energy efficiency, accuracy, on-chip learning), device-to-algorithm co-design for NVM-based chips, an EDA toolchain and a roadmap toward large-scale chips.
- Physics for Neuromorphic Computing (**Nature Reviews Physics 2020**). \[[paper](https://doi.org/10.1038/s42254-020-0208-2)\]
  > Perspective arguing that orders-of-magnitude efficiency gains need a revolution in hardware that harnesses physics, reviewing resistive-switching, photonic and spintronic routes toward low-power chips that learn and infer in real time.
- Opportunities for Neuromorphic Computing Algorithms and Applications (**Nature Computational Science 2022**). \[[paper](https://www.nature.com/articles/s43588-021-00184-y)\]
  > Argues neuromorphic research has focused mostly on hardware; reviews recent algorithms and applications, explains what makes neuromorphic computing attractive, and maps opportunities and challenges slowing progress.
- Neuromorphic Computing at Scale (**Nature 2025**). \[[paper](https://www.nature.com/articles/s41586-024-08253-8)\]
  > Kudithipudi, Schuman, Furber et al. map the road to large-scale neuromorphic systems: key features of scalable architectures, applications that gain from scale, open challenges, and the tooling and community ecosystem required.

#### Digital Neuromorphic Chips

- A Million Spiking-Neuron Integrated Circuit with a Scalable Communication Network (TrueNorth) (**Science 2014**) ★. \[[paper](https://www.science.org/doi/10.1126/science.1254642)\]
  > IBM's TrueNorth packs 1M neurons + 256M synapses into a 65 mW event-driven non-von-Neumann chip — the landmark large-scale digital neuromorphic silicon.
- Convolutional Networks for Fast, Energy-Efficient Neuromorphic Computing (TrueNorth) (**PNAS 2016**). \[[paper](https://www.pnas.org/doi/10.1073/pnas.1604850113)\]
  > Maps deep convnets onto TrueNorth at near-SOTA accuracy, 1,200–2,600 fps and tens of mW.
- Loihi: A Neuromorphic Manycore Processor with On-Chip Learning (**IEEE Micro 2018**) ★. \[[paper](https://ieeexplore.ieee.org/document/8259423)\]\[[code](https://github.com/lava-nc/lava)\]
  > Intel's 14 nm 128-core chip with programmable synaptic learning, dendritic compartments and delays — the leading on-chip-learning research platform.
- Taking Neuromorphic Computing to the Next Level with Loihi 2 (**Intel Tech Brief 2021**). \[[paper](https://www.intel.com/content/www/us/en/research/neuromorphic-computing-loihi-2-technology-brief.html)\]\[[code](https://github.com/lava-nc/lava)\]
  > Loihi 2 adds graded spikes, programmable neuron microcode and up to 1M neurons in 7 nm, paired with the open-source Lava framework.
- The SpiNNaker Project (**Proc. IEEE 2014**). \[[paper](https://doi.org/10.1109/JPROC.2014.2304638)\]\[[code](https://github.com/SpiNNakerManchester)\]
  > Manchester's massively-parallel ARM machine models spiking networks in biological real time via brain-inspired packet routing.
- SpiNNaker: A 1-W 18-Core System-on-Chip for Massively-Parallel Neural Simulation (**IEEE JSSC 2013**). \[[paper](https://doi.org/10.1109/JSSC.2013.2259038)\]
  > The 18-ARM-core GALS chip (100M transistors, 1 W) — physical building block of the million-core SpiNNaker machine.
- SpiNNaker 2: A 10-Million-Core Processor System for Brain Simulation and Machine Learning (**arXiv 2019**). \[[paper](https://arxiv.org/abs/1911.02385)\]
  > 22 nm FDSOI successor adding numerical accelerators and adaptive power management for both brain simulation and ML.
- The SpiNNaker2 Chip: A Many-Core Platform for Flexible and Scalable Brain-Inspired Computing (**IEEE OJCAS 2026**). \[[paper](https://arxiv.org/abs/2607.24396)\]
  > The definitive SpiNNaker2 chip paper — 152 ARM M4F processing elements with MAC/exp/log accelerators, up to 4.5 TOPS (2.7 TOPS/W) and >150k neurons per chip.
- Towards Artificial General Intelligence with Hybrid Tianjic Chip Architecture (**Nature 2019**) ★. \[[paper](https://www.nature.com/articles/s41586-019-1424-8)\]
  > Tsinghua's Tianjic unifies ANN and SNN paradigms on one reconfigurable many-core chip — famously demoed driving an autonomous bicycle.
- Darwin: A Neuromorphic Hardware Co-Processor Based on Spiking Neural Networks (**J. Systems Architecture 2017**). \[[paper](https://www.sciencedirect.com/science/article/abs/pii/S1383762117300231)\]
  > China's Darwin NPU (180 nm, 2,048 neurons, configurable delays) — an early low-power embedded SNN co-processor.
- Darwin3: A Large-Scale Neuromorphic Chip with a Novel ISA and On-Chip Learning (**National Science Review 2024**). \[[paper](https://arxiv.org/abs/2312.17582)\]
  > Zhejiang Univ. (Gang Pan) digital chip with a dedicated 10-instruction ISA and on-chip learning — up to ~2.35M neurons per chip.
- UniSpike: Accelerating SNNs on Neuromorphic Systems via Eliminating Address Redundancy (**DAC 2026**). \[[paper](https://arxiv.org/abs/2605.23796)\]
  > ZJU hardware–software co-design packing same-destination spikes into compact packets — 1.93× less NoC traffic and 1.77× speedup on many-core neuromorphic systems.
- ODIN: A 0.086 mm² 12.7 pJ/SOP 64k-Synapse 256-Neuron Online-Learning Digital SNN Processor (**IEEE TBCAS 2019**). \[[paper](https://arxiv.org/abs/1804.07858)\]\[[code](https://github.com/ChFrenkel/ODIN)\]
  > A tiny open-source 28 nm chip with SDSP on-chip learning and Izhikevich-capable neurons, setting synaptic-density/energy records.
- MorphIC: A 65-nm Quad-Core Binary-Weight Digital Neuromorphic Processor with Stochastic Online Learning (**IEEE TBCAS 2019**). \[[paper](https://arxiv.org/abs/1904.08513)\]
  > Frenkel's four-core follow-up to ODIN, maximizing synaptic density with binary weights and stochastic plasticity for edge learning.
- μBrain: An Event-Driven and Fully Synthesizable Architecture for Spiking Neural Networks (**Front. Neurosci. 2021**). \[[paper](https://www.frontiersin.org/articles/10.3389/fnins.2021.664208/full)\]
  > The first clockless, fully-synthesizable digital SNN chip (40 nm, sub-100 μW) for always-on near-sensor edge AI.
- SENeCA: Building a Fully Digital Neuromorphic Processor (**Front. Neurosci. 2023**). \[[paper](https://www.frontiersin.org/articles/10.3389/fnins.2023.1187252/full)\]
  > imec's flexible RISC-V + loop-buffer architecture balancing programmability and efficiency for diverse SNN + on-device learning.
- A Digital Neurosynaptic Core Using Embedded Crossbar Memory with 45 pJ per Spike in 45 nm (**IEEE CICC 2011**). \[[paper](https://doi.org/10.1109/CICC.2011.6055294)\]
  > Merolla et al.'s neurosynaptic core — the direct architectural precursor to IBM TrueNorth.
- ReckOn: A 28 nm Sub-mm² Task-Agnostic Spiking Recurrent Neural Network Processor Enabling On-Chip Learning over Second-Long Timescales (**IEEE ISSCC 2022**). \[[paper](https://arxiv.org/abs/2208.09759)\]
  > Frenkel & Indiveri's chip does e-prop-style on-chip learning of temporal tasks over second-long horizons at sub-mW power.
- SpikeRAM: An Event-Driven Spiking Compute-Near/In-Memory Processor Enabling Life-Long On-Chip Learning (**IEEE ISSCC 2026**). \[[paper](https://submissions.mirasmart.com/ISSCC2026/PDF/ISSCC2026AdvanceProgram.pdf)\]
  > HKUST (Guangzhou) + SynSense silicon pairing a neuromorphic sensor with 48.1 pW/synapse/bit compute-near-memory for lifelong on-chip learning.
- Algorithm–Hardware Co-Design of Neuromorphic Networks with Dual Memory Pathways (**Nature Machine Intelligence 2026**). \[[paper](https://www.nature.com/articles/s42256-026-01255-3)\]
  > Fast/slow dual-memory spiking networks co-designed with a custom chip — >4× throughput and ~5× energy efficiency with 40–60% fewer parameters.
- A System Hierarchy for Brain-Inspired Computing (**Nature 2020**). \[[paper](https://www.nature.com/articles/s41586-020-2782-y)\]
  > Tsinghua defines 'neuromorphic completeness' and pairs a Turing-complete software model with an abstract neuromorphic architecture. One toolchain then targets GPU, FPSA and Tianjic, demonstrated on bicycle driving, Boid flocking and QR decomposition.
- Advancing Neuromorphic Computing With Loihi: A Survey of Results and Outlook (**Proceedings of the IEEE 2021**). \[[paper](https://ieeexplore.ieee.org/document/9395703)\]
  > Surveys Loihi results. Conventional feedforward DNNs gain little, while networks exploiting recurrence, spike timing, plasticity and sparsity cut latency and energy by orders of magnitude on event processing, control, optimization and search.
- Spike-Based Dynamic Computing with Asynchronous Sensing-Computing Neuromorphic Chip (**Nature Communications 2024**). \[[paper](https://www.nature.com/articles/s41467-024-47811-6)\]
  > Diagnoses 'dynamic imbalance' in SNNs and adds attention-based dynamic computing so energy varies with input; on Speck, an asynchronous sensor-plus-processor chip (0.42 mW resting), real-time power reaches 0.70 mW.
- A Deterministic Neuromorphic Architecture with Scalable Time Synchronization (NeuroScale) (**Nature Communications 2025**). \[[paper](https://www.nature.com/articles/s41467-025-65268-z)\]
  > Replaces the global barrier synchronization of TrueNorth/Loihi-style chips with local, event-driven aperiodic synchronization between cores, keeping spiking execution deterministic while scaling better at large system sizes; prototyped on FPGA.

#### Analog & Mixed-Signal / Sub-threshold

- Neurogrid: A Mixed-Analog-Digital Multichip System for Large-Scale Neural Simulations (**Proc. IEEE 2014**) ★. \[[paper](https://doi.org/10.1109/JPROC.2014.2313565)\]
  > Boahen's 16-Neurocore board simulates a million subthreshold-analog neurons with billions of synapses in real time at just 3 W.
- A Wafer-Scale Neuromorphic Hardware System for Large-Scale Neural Modeling (BrainScaleS-1) (**IEEE ISCAS 2010**). \[[paper](https://doi.org/10.1109/ISCAS.2010.5536970)\]
  > Heidelberg's HICANN wafer-scale system emulates ~200k neurons per wafer at 10,000× biological speed via accelerated analog dynamics.
- The BrainScaleS-2 Accelerated Neuromorphic System with Hybrid Plasticity (**Front. Neurosci. 2022**). \[[paper](https://www.frontiersin.org/articles/10.3389/fnins.2022.795876/full)\]
  > Couples continuous-time analog neuron/synapse circuits with embedded SIMD processors for flexible on-chip hybrid plasticity.
- DYNAP-SE: A Scalable Multicore Architecture with Heterogeneous Memory for Dynamic Neuromorphic Async Processors (**IEEE TBCAS 2018**). \[[paper](https://doi.org/10.1109/TBCAS.2017.2759700)\]
  > Indiveri's subthreshold-analog chip introduces heterogeneous routing that solves the connectivity-scaling problem.
- ROLLS: A Reconfigurable On-Line Learning Spiking Neuromorphic Processor (256 Neurons, 128k Synapses) (**Front. Neurosci. 2015**). \[[paper](https://doi.org/10.3389/fnins.2015.00141)\]
  > A mixed-signal chip emulating real neuron/synapse physics with spike-based plasticity for fully on-chip online learning.
- DYNAP-CNN & Speck: Event-Driven Convolutional Neuromorphic Vision Processors (SynSense) (**2020**). \[[paper](https://www.synsense.ai/products/speck-2/)\]\[[code](https://github.com/synsense/sinabs)\]
  > Commercial sub-mW spiking-CNN processors (Speck integrates a DVS + DynapCNN on one SoC) for always-on event vision at μs latency.
- Synaptic and Neural Behaviours in a Standard Silicon Transistor (NS-RAM) (**Nature 2025**). \[[paper](https://www.nature.com/articles/s41586-025-08742-4)\]
  > Biases one unmodified commercial bulk-silicon transistor near punch-through so impact ionization makes it spike like a neuron or act as a synapse; a two-transistor NS-RAM cell tunes the response with 100% yield.
- A Neuromorphic Processor with On-Chip Learning for Beyond-CMOS Device Integration (**Nature Communications 2025**). \[[paper](https://www.nature.com/articles/s41467-025-61576-6)\]
  > TEXEL, a 180 nm mixed-signal chip pairing AdExLIF neurons with a bistable calcium-based local learning rule (STDP at low activity, Hebbian at high). It is built to integrate two- and three-terminal beyond-CMOS memory devices.

#### In-Memory / Memristive / RRAM & PCM Computing

- Nanoscale Memristor Device as Synapse in Neuromorphic Systems (**Nano Letters 2010**) ★. \[[paper](https://pubs.acs.org/doi/10.1021/nl904092h)\]
  > Jo & Lu experimentally demonstrated STDP in a single nanoscale memristor — launching memristive-synapse computing.
- Nanoelectronic Programmable Synapses Based on Phase-Change Materials (**Nano Letters 2011**). \[[paper](https://pubs.acs.org/doi/10.1021/nl201040y)\]
  > Continuous PCM resistance transitions emulate analog synaptic plasticity (STDP) at picojoule energy.
- Training and Operation of an Integrated Neuromorphic Network Based on Metal-Oxide Memristors (**Nature 2015**) ★. \[[paper](https://www.nature.com/articles/nature14441)\]
  > The first transistor-free memristor crossbar perceptron trained in situ — proof of integrated memristive neural networks.
- Stochastic Phase-Change Neurons (**Nature Nanotechnology 2016**). \[[paper](https://www.nature.com/articles/nnano.2016.70)\]
  > IBM realizes integrate-and-fire neurons in PCM devices whose intrinsic stochasticity enables population coding.
- Memristors with Diffusive Dynamics as Synaptic Emulators (**Nature Materials 2017**). \[[paper](https://www.nature.com/articles/nmat4756)\]
  > Ag-nanoparticle diffusive memristors reproduce Ca²⁺-like short-term synaptic dynamics — a biologically faithful analog synapse.
- Fully Memristive Neural Networks for Pattern Classification with Unsupervised Learning (**Nature Electronics 2018**). \[[paper](https://www.nature.com/articles/s41928-018-0023-2)\]
  > Integrates diffusive-memristor LIF neurons with nonvolatile memristor synapses into an all-memristive unsupervised network.
- Equivalent-Accuracy Accelerated Neural-Network Training Using Analogue Memory (**Nature 2018**). \[[paper](https://www.nature.com/articles/s41586-018-0180-5)\]
  > IBM's PCM+capacitor analog synapse hits software-equivalent training accuracy at ~100× better energy efficiency than GPUs.
- Fully Hardware-Implemented Memristor Convolutional Neural Network (**Nature 2020**). \[[paper](https://www.nature.com/articles/s41586-020-1942-4)\]
  > Tsinghua integrates eight memristor crossbars into a complete CNN with hybrid training — >100× more energy-efficient than GPUs.
- The Missing Memristor Found (**Nature 2008**) ★. \[[paper](https://www.nature.com/articles/nature06932)\]
  > HP Labs' physical realization of Chua's memristor — the device that launched the entire memristive-synapse field.
- Experimental Demonstration and Tolerancing of a Large-Scale Neural Network (165,000 Synapses) Using Phase-Change Memory (**IEEE TED 2015**). \[[paper](https://doi.org/10.1109/TED.2015.2439635)\]
  > IBM's Burr et al. train a 165k-synapse network on real PCM hardware — a landmark large-scale in-memory demonstration.
- Neuromorphic Computing with Nanoscale Spintronic Oscillators (**Nature 2017**). \[[paper](https://www.nature.com/articles/nature23011)\]
  > Uses a single spin-torque nano-oscillator to classify spoken digits — opening spintronics as a neuromorphic substrate.
- Deep Learning Incorporating Biologically Inspired Neural Dynamics and In-Memory Computing (**Nature Machine Intelligence 2020**). \[[paper](https://www.nature.com/articles/s42256-020-0187-0)\]
  > Woźniak et al.'s spiking neural units (SNUs) bring LIF dynamics into deep-learning layers deployable on in-memory hardware.
- Spiking Neural Networks with Fatigue Spike-Timing-Dependent Plasticity Learning Using Hybrid Memristor Arrays (**Nature Electronics 2026**). \[[paper](https://www.nature.com/articles/s41928-025-01554-4)\]
  > PKU (Yuchao Yang) pairs fatigue-prone dynamic memristors with hafnia 1T1R devices to realize fatigue-STDP in hardware for noise-resilient unsupervised learning.
- Bio-Plausible Reconfigurable Spiking Neuron for Neuromorphic Computing (**Science Advances 2025**). \[[paper](https://www.science.org/doi/10.1126/sciadv.adr6733)\]
  > ZJU + Westlake's Mott-memristor + ECRAM artificial neuron switches among diverse biological firing patterns purely by programming device states.
- Printed MoS₂ Memristive Nanosheet Networks for Spiking Neurons with Multi-Order Complexity (**Nature Nanotechnology 2026**). \[[paper](https://www.nature.com/articles/s41565-026-02149-6)\]
  > Northwestern's printed nanosheet spiking neurons (tunable to 20 kHz, >10⁶ cycles) even stimulate living mouse Purkinje cells — printed neurons talking to real ones.
- Learning Through Ferroelectric Domain Dynamics in Solid-State Synapses (**Nature Communications 2017**). \[[paper](https://doi.org/10.1038/ncomms14736)\]
  > Shows STDP in ferroelectric tunnel-junction synapses stems from inhomogeneous polarization switching, modelled as nucleation-dominated domain reversal; simulated arrays of these nanosynapses learn to recognize patterns autonomously, toward unsupervised SNN learning.
- Neuromorphic Computing with Multi-Memristive Synapses (**Nature Communications 2018**). \[[paper](https://doi.org/10.1038/s41467-018-04933-y)\]
  > Builds each synapse from several phase-change memory devices, with a global counter-based arbitration choosing which device to program; an experiment on over a million PCM devices learns temporal correlations with a spiking network.
- Biological Plausibility and Stochasticity in Scalable VO2 Active Memristor Neurons (**Nature Communications 2018**). \[[paper](https://doi.org/10.1038/s41467-018-07052-w)\]
  > Neurons built from nanoscale VO2 active memristors show all three classes of excitability and 23 types of biological spiking behaviour, are intrinsically stochastic, and chart a path toward all-memristor neuromorphic computers.
- Spike-Timing-Dependent Plasticity Learning of Coincidence Detection with Passively Integrated Memristive Circuits (**Nature Communications 2018**). \[[paper](https://doi.org/10.1038/s41467-018-07757-y)\]
  > Passively integrated (0T1R) metal-oxide memristors in a 20×20 crossbar act as synapses that learn by STDP to detect coincident input spikes, driving an analog leaky-integrate-and-fire silicon neuron.
- Third-Order Nanocircuit Elements for Neuromorphic Engineering (**Nature 2020**). \[[paper](https://www.nature.com/articles/s41586-020-2735-5)\]
  > Mott-transition and other electrophysical dynamics combine into one nanoscale third-order circuit element, the theoretical minimum for action potentials; transistorless networks of them compute spiking Boolean logic and analogue graph partitioning.
- Spiking Neurons with Spatiotemporal Dynamics and Gain Modulation for Monolithically Integrated Memristive Neural Networks (**Nature Communications 2020**). \[[paper](https://doi.org/10.1038/s41467-020-17215-3)\]\[[code](https://github.com/duanqingxi/NCOMMS-20-02976)\]
  > Volatile NbOx memristor neurons integrate inputs over space and time, solve XOR and perform multiplicative gain modulation; integrated with TaOx memristor synapses in one crossbar, they learn patterns online.
- Ion-Tunable Antiambipolarity in Mixed Ion–Electron Conducting Polymers Enables Biorealistic Organic Electrochemical Neurons (**Nature Materials 2023**). \[[paper](https://www.nature.com/articles/s41563-022-01450-8)\]
  > A ladder polymer's ion-tunable antiambipolarity emulates Na⁺/K⁺ channel dynamics in a conductance-based organic electrochemical neuron that spikes near 100 Hz, is chemically modulated, and stimulates a mouse vagus nerve in vivo.
- Firing Feature-Driven Neural Circuits with Scalable Memristive Neurons for Robotic Obstacle Avoidance (**Nature Communications 2024**). \[[paper](https://www.nature.com/articles/s41467-024-48399-7)\]
  > Builds Hodgkin–Huxley neurons from NbO2 threshold-switching memristors: one encodes input as mixed tonic spikes and bursts, two others decode bursts and spikes to steer a LiDAR robot around obstacles.
- Spintronic Neural Systems (**Nature Reviews Electrical Engineering 2024**). \[[paper](https://www.nature.com/articles/s44287-024-00107-9)\]
  > Reviews how magnetic-tunnel-junction device dynamics implement neuronal and synaptic functions — MTJ spiking neurons, MTJ-crossbar SNNs and stochastic-MTJ computing — through cross-layer device–circuit–system co-design.
- A Spiking Artificial Neuron Based on One Diffusive Memristor, One Transistor and One Resistor (**Nature Electronics 2025**). \[[paper](https://www.nature.com/articles/s41928-025-01488-x)\]
  > J. Joshua Yang's group vertically integrates a diffusive memristor, transistor and resistor into roughly one transistor's footprint, reproducing leaky integration, threshold firing, refractoriness, intrinsic plasticity and stochasticity at picojoule-per-spike energy.
- Resistive Memory-Based Zero-Shot Liquid State Machine for Multimodal Event Data Learning (**Nature Computational Science 2025**). \[[paper](https://doi.org/10.1038/s43588-024-00751-z)\]\[[code](https://github.com/MrLinNing/MemristorLSM)\]
  > Hardware-software co-design on a 40 nm resistive-memory in-memory computing macro: a fixed random liquid state machine serves as the spiking encoder beneath trainable ANN projections, enabling low-training-cost zero-shot multimodal event-data learning.
- Fully Memristive Spiking Neural Network for Energy-Efficient Graph Learning (**Science Advances 2025**). \[[paper](https://www.science.org/doi/10.1126/sciadv.adv2312)\]
  > Finds shortest paths in graphs by letting spikes travel simultaneously through a fully memristive SNN instead of arithmetic search, with estimated energy efficiency three to four orders of magnitude above FPGAs.
- A Biologically Inspired Artificial Neuron with Intrinsic Plasticity Based on Monolayer Molybdenum Disulfide (**Nature Electronics 2025**). \[[paper](https://www.nature.com/articles/s41928-025-01433-y)\]
  > Builds an integrate-and-fire neuron from a wafer-scale monolayer-MoS₂ DRAM cell and inverter whose membrane potential self-adjusts to mimic intrinsic plasticity, with light-adaptive sensing and temporal coding in a 3×3 photoreceptor array.
- Topology Optimization of Random Memristors for Input-Aware Dynamic SNN (PRIME) (**Science Advances 2025**). \[[paper](https://www.science.org/doi/10.1126/sciadv.ads5340)\]
  > Prunes and optimizes random memristive SNNs, inspired by structural plasticity, to absorb device programming variability, plus an input-aware early-stop policy; a 40 nm 256K-memristor chip matches software baselines at far higher energy efficiency.
- A Spiking Neural Network-in-Logic Architecture Based on Reconfigurable Molybdenum Disulfide Dual-Gate Transistors with Ferroelectric Gating (**Nature Electronics 2026**). \[[paper](https://www.nature.com/articles/s41928-026-01706-0)\]
  > Filters task-irrelevant inputs with in-device logic before SNN processing, using reconfigurable HZO-ferroelectric-gated MoS₂ dual-gate transistors that serve as logic, synapse or neuron elements to cut needless neuron activation.
- An End-to-End Memristive Hardware System Based on Single-Spike Coding for Human–Machine Interfaces (**Nature Electronics 2026**). \[[paper](https://www.nature.com/articles/s41928-025-01544-6)\]\[[code](https://github.com/pekjuntiw/single-spiking-hmi)\]
  > PKU replaces rate coding with single-spike timing: VO₂ memristor spiking circuits feed an HfO₂/TaOₓ memristor chip, enabling real-time sEMG vehicle control with under 1.5% accuracy degradation versus software.

#### Photonic Spiking Hardware

- Nonlinear Photonic Neuromorphic Chips for Spiking Reinforcement Learning (**Optica 2026**). \[[paper](https://doi.org/10.1364/OPTICA.578687)\]
  > Xidian's two-chip system (16×16 MZI mesh + DFB laser array) computes linear *and* nonlinear spiking operations fully optically — real-time RL at 320 ps latency.
- Accelerating Spiking Neural Networks with Photonic Reconfigurable Devices (**Nature Communications 2026**). \[[paper](https://www.nature.com/articles/s41467-026-72119-y)\]
  > Fudan's programmable photonic devices unify synapse and neuron functions — 1176× latency reduction and 239× energy savings at equal accuracy.
- Compact Photonic Spiking Neuron with Inherent Stochasticity for Probabilistic Computing (**Nature Communications 2026**). \[[paper](https://www.nature.com/articles/s41467-026-73070-8)\]
  > HUST's 1.5 μm² phase-change photonic neuron turns intrinsic switching stochasticity into Bayesian spiking computation with uncertainty estimates.
- All-Optical Spiking Neurosynaptic Networks with Self-Learning Capabilities (**Nature 2019**) ★. \[[paper](https://www.nature.com/articles/s41586-019-1157-8)\]
  > Phase-change (GST) photonic neurons and synapses form an all-optical spiking network that learns supervised or unsupervised; wavelength-division multiplexing makes it scalable, recognizing patterns directly in the optical domain.
- Photonics for Artificial Intelligence and Neuromorphic Computing (**Nature Photonics 2021**). \[[paper](https://www.nature.com/articles/s41566-020-00754-y)\]
  > Shastri, Prucnal et al. survey integrated photonic neuromorphic systems, including excitable lasers and resonators for spiking, and argue that their sub-nanosecond latency complements latency-limited neuromorphic electronics.
- Superconducting Optoelectronic Single-Photon Synapses (**Nature Electronics 2022**). \[[paper](https://www.nature.com/articles/s41928-022-00840-9)\]
  > NIST monolithically integrates superconducting nanowire single-photon detectors with Josephson junctions: synapses leakily integrate single-photon spikes with electronic weighting, time constants from hundreds of ns to ms, and >10 MHz input rates.
- Photonically Linked Three-Dimensional Neural Networks Based on Memristive Blinking Neurons (**Nature Electronics 2026**). \[[paper](https://www.nature.com/articles/s41928-025-01529-5)\]
  > Ag/PMMA/Ag memristive neurons emit a light pulse after integrating enough electrical spikes, linking stacked layers optically into a three-dimensional spiking network evaluated on speech and MNIST classification.

#### Event Cameras & Neuromorphic Sensors

- A 128×128 120 dB 15 μs Latency Asynchronous Temporal Contrast Vision Sensor (DVS) (**IEEE JSSC 2008**) ★. \[[paper](https://doi.org/10.1109/JSSC.2007.914337)\]
  > Lichtsteiner, Posch & Delbruck's Dynamic Vision Sensor — pixels asynchronously emit spikes on brightness change, founding event-based vision.
- A QVGA 143 dB Dynamic Range Frame-Free PWM Image Sensor (ATIS) (**IEEE JSSC 2011**). \[[paper](https://doi.org/10.1109/JSSC.2010.2085952)\]
  > Combines event-based change detection with per-pixel PWM absolute-intensity encoding, adding grayscale to event vision.
- A 240×180 130 dB 3 μs Latency Global-Shutter Spatiotemporal Vision Sensor (DAVIS) (**IEEE JSSC 2014**). \[[paper](https://doi.org/10.1109/JSSC.2014.2342715)\]
  > Outputs asynchronous DVS events + synchronous APS frames from a shared photodiode — the most widely used event-camera format.
- A 1280×720 Back-Illuminated Stacked Temporal-Contrast Event-Based Vision Sensor (**IEEE ISSCC 2020**). \[[paper](https://ieeexplore.ieee.org/document/9063149)\]
  > Sony/Prophesee scale event cameras to HD with the industry's smallest pixels and >124 dB HDR, enabling commercial deployment.
- AER EAR: A Matched Silicon Cochlea Pair with Address-Event Representation Interface (**IEEE TCAS-I 2007**). \[[paper](https://doi.org/10.1109/TCSI.2006.887979)\]
  > A binaural silicon cochlea modeling basilar-membrane filtering and emitting AER spikes — the auditory counterpart to the DVS.
- A Bioinspired Flexible Organic Artificial Afferent Nerve (**Science 2018**). \[[paper](https://www.science.org/doi/10.1126/science.aao0098)\]
  > Pressure sensors drive organic ring oscillators that encode touch as 0–100 Hz action potentials, and a synaptic transistor integrates them. The nerve distinguishes braille characters and forms a hybrid bioelectronic reflex arc that actuates muscles.
- An Artificial Spiking Afferent Nerve Based on Mott Memristors for Neurorobotics (**Nature Communications 2020**). \[[paper](https://doi.org/10.1038/s41467-019-13827-6)\]
  > An NbOx Mott-memristor spiking afferent nerve fires in proportion to stimulus intensity, then slows past an inflection point at noxious levels; paired with a passive piezoelectric sensor, it forms a power-free spiking mechanoreceptor.
- An Organic Artificial Spiking Neuron for In Situ Neuromorphic Sensing and Biointerfacing (**Nature Electronics 2022**). \[[paper](https://www.nature.com/articles/s41928-022-00859-y)\]
  > A compact neuron built from organic electrochemical transistors spikes in aqueous electrolytes. Ion and dopamine concentrations across physiological and pathological ranges modulate its firing, and an epithelial-cell biohybrid version reports barrier disruption in real time.
- Event-Based Vision: A Survey (**IEEE TPAMI 2022**). \[[paper](https://arxiv.org/abs/1904.08405)\]
  > The reference survey of event cameras: sensor principles and available devices, event-processing methods including spiking networks, low- to high-level vision tasks, and open challenges.
- Neuromorphic Sensorimotor Loop Embodied by Monolithically Integrated, Low-Voltage, Soft E-Skin (**Science 2023**). \[[paper](https://www.science.org/doi/10.1126/science.ade0086)\]
  > Bao's group monolithically integrates a low-voltage soft e-skin that combines multimodal sensing, neuromorphic pulse-train generation and closed-loop actuation. A solid-state synaptic transistor drives stronger actuation as pressure rises, mimicking the biological sensorimotor loop.
- Computational Event-Driven Vision Sensors for In-Sensor Spiking Neural Networks (**Nature Electronics 2023**). \[[paper](https://www.nature.com/articles/s41928-023-01055-2)\]
  > Each sensor pairs two opposite-polarity photodiodes (5 μs resolution) whose programmable photoresponsivity sets spike amplitude and polarity. The non-volatile multilevel responsivity serves as synaptic weights, forming an in-sensor SNN for motion recognition.
- Reconfigurable In-Sensor Processing Based on a Multi-Phototransistor–One-Memristor Array (**Nature Electronics 2024**). \[[paper](https://www.nature.com/articles/s41928-024-01280-3)\]\[[code](https://doi.org/10.5281/zenodo.13747890)\]
  > PKU pairs multiple phototransistors with one niobium-oxide memristor of reconfigurable dynamics, so a single in-sensor array feeds optical CNNs, RNNs or spiking networks for static, motion and colour image recognition.
- High-Order Dynamics in an Ultra-Adaptive Neuromorphic Vision Device (**Nature Nanotechnology 2025**). \[[paper](https://www.nature.com/articles/s41565-025-01984-3)\]
  > SUSTech's single two-terminal IxTyO/CuOx/Pd device, under light or electrical input, acts as retina-like spiking/graded neurons and cortex-like synapses and LIF neurons; its arrays run event- and frame-driven vision on traffic scenes.
- Amplitude-Controllable Event-Driven Organic Photosensors Based on Ionic-Mediated Inhibition (**Nature Materials 2026**). \[[paper](https://www.nature.com/articles/s41563-026-02747-8)\]\[[code](https://github.com/Daniel-chen-hku/event_driven_oect)\]
  > Blends an organic mixed ionic–electronic donor (PgBDT-T) with the Y6 acceptor: fast electron extraction gives excitatory pho