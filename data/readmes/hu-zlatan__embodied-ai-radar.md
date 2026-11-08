# Embodied AI Radar · 具身智能雷达

**A bilingual (English / [中文](README.zh-CN.md)), always-fresh map of embodied AI and robot learning.**
Hand-verified papers, code, datasets, simulators and hardware with one-line takeaways — plus every new robotics paper on arXiv, fetched and tagged by topic every day.

### 🌐 [Open the website → hu-zlatan.github.io/embodied-ai-radar](https://hu-zlatan.github.io/embodied-ai-radar/)

[![Website](https://img.shields.io/badge/website-live-0f6fde)](https://hu-zlatan.github.io/embodied-ai-radar/)
[![Daily arXiv intake](https://github.com/hu-zlatan/embodied-ai-radar/actions/workflows/intake.yml/badge.svg)](https://github.com/hu-zlatan/embodied-ai-radar/actions/workflows/intake.yml)
[![Verified links](https://github.com/hu-zlatan/embodied-ai-radar/actions/workflows/verify.yml/badge.svg)](https://github.com/hu-zlatan/embodied-ai-radar/actions/workflows/verify.yml)
[![License: MIT + CC BY 4.0](https://img.shields.io/badge/license-MIT%20%2B%20CC%20BY%204.0-lightgrey)](LICENSE-DATA.md)

![Screenshot of the Embodied AI Radar website](docs/screenshot.png)

**CoRL 2026 (Nov 9–12, Austin):** the [program guide](https://hu-zlatan.github.io/embodied-ai-radar/venues/corl-2026-program.html) lists all 687 accepted papers by session and poster number, with filters and arXiv/code links, plus the 32 workshops.

**New to the field?** Follow the [reading path](https://hu-zlatan.github.io/embodied-ai-radar/start.html): 10 steps from RL and imitation basics through visuomotor policies, VLA models, simulation, locomotion and world models to hardware you can build — 41 hand-picked entries, each with a bilingual takeaway.

## Why this one

- **Verified.** Every curated arXiv ID is checked against arXiv and every link is checked by CI, weekly.
- **Fresh.** A GitHub Action pulls new cs.RO papers (plus robotics papers from cs.CV / cs.LG / cs.AI / cs.CL) every day and tags them by topic — they appear on the site without anyone touching the repo.
- **Searchable.** Instant search and filters (topic · robot type: arm, hand, humanoid, legged, drone… · accepted venue such as CoRL, NeurIPS, IROS · curated vs. daily · has code) on a fast static site that works on phones. Papers accepted at a venue also get a page per conference, e.g. [CoRL 2026](https://hu-zlatan.github.io/embodied-ai-radar/venues/corl-2026.html) ([all venues](https://hu-zlatan.github.io/embodied-ai-radar/venues/index.html)), and every robot type has its own page and Atom feed, e.g. [humanoid](https://hu-zlatan.github.io/embodied-ai-radar/robots/humanoid.html) · [dexterous hand](https://hu-zlatan.github.io/embodied-ai-radar/robots/hand.html) · [quadruped](https://hu-zlatan.github.io/embodied-ai-radar/robots/legged.html). You can also browse by lab or company, e.g. [NVIDIA](https://hu-zlatan.github.io/embodied-ai-radar/labs/nvidia.html) · [Stanford](https://hu-zlatan.github.io/embodied-ai-radar/labs/stanford.html) · [Shanghai AI Lab](https://hu-zlatan.github.io/embodied-ai-radar/labs/shanghai-ai-lab.html) ([all labs](https://hu-zlatan.github.io/embodied-ai-radar/labs/index.html)).
- **Signal, not just volume.** Each paper shows the GitHub stars of its code and, when it made [Hugging Face Daily Papers](https://huggingface.co/papers), its community upvotes (▲) — sort search by either, or see the most-upvoted robotics papers of the last two weeks on the home page.
- **Code tracker.** [Every curated repo](https://hu-zlatan.github.io/embodied-ai-radar/code.html) on one page: GitHub stars, stars gained this week, last update and detected license, with filters by topic and license.
- **Reusable.** The whole curated index is downloadable as [`curated.json`](https://hu-zlatan.github.io/embodied-ai-radar/curated.json) or [`curated.csv`](https://hu-zlatan.github.io/embodied-ai-radar/curated.csv) (opens in Excel; CC BY 4.0) with topics, robot types, links, takeaways and GitHub stars — build your own tools on it.
- **Bilingual.** Every curated entry has a one-line takeaway in English and Chinese; the site has an EN / 中文 toggle.
- **Citable.** Every arXiv paper on the site has a one-click BibTeX, and [`curated.bib`](https://hu-zlatan.github.io/embodied-ai-radar/curated.bib) bundles all curated papers (built from arXiv metadata). Every curated entry also has its own shareable page, e.g. [LEAP Hand](https://hu-zlatan.github.io/embodied-ai-radar/e/arxiv-2309.06440.html).

| What | How often |
|---|---|
| Daily arXiv feed ([site](https://hu-zlatan.github.io/embodied-ai-radar/feed.html) · [Atom](https://hu-zlatan.github.io/embodied-ai-radar/feed.xml); one Atom feed per topic, e.g. [VLA](https://hu-zlatan.github.io/embodied-ai-radar/topics/vla.xml)) | every day, automatically |
| Curated index (below and on the site) · agent picks from the daily feed ([Atom](https://hu-zlatan.github.io/embodied-ai-radar/picks.xml), a few a day, bilingual) | several times a week |
| [Weekly digest](digest/) | weekly |

## Topics

VLA & robot foundation models · manipulation & dexterous hands · tactile sensing · locomotion & humanoids · world models · navigation & embodied agents · perception, SLAM & 3D mapping · planning, control & safety · sim-to-real & simulators · datasets & benchmarks · hardware & open-source robots.

## Curated index

**Editor's rating:** ⭐⭐⭐ must-read (at most one per topic) · ⭐⭐ highly recommended · ⭐ recommended · no star = worth knowing. Each topic lists the rated entries first, then the newest picks; **All N entries** opens the complete list. Generated from [`data/curated/`](data/curated) — edit the YAML, not these lists.

<!-- radar:start -->

[VLA & Robot Foundation Models](#vla) · [Manipulation & Dexterous Hands](#manipulation) · [Tactile & Visuotactile Sensing](#tactile) · [Locomotion & Humanoids](#locomotion) · [World Models](#world-models) · [Navigation & Embodied Agents](#navigation) · [Perception, SLAM & 3D Mapping](#perception) · [Planning, Control & Safety](#control) · [Robot Learning: RL & Imitation](#learning) · [Sim-to-Real & Simulators](#sim) · [Datasets & Benchmarks](#datasets) · [Hardware & Open-Source Robots](#hardware)

<a id="vla"></a>
### VLA & Robot Foundation Models

_Vision-language-action models and generalist robot policies._ [Browse with the latest papers →](https://hu-zlatan.github.io/embodied-ai-radar/topics/vla.html)

- ⭐⭐⭐ **[π0: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164)** (2024) — A VLM backbone with a flow-matching action expert, trained across many robots, doing long dexterous tasks like laundry folding. · [code](https://github.com/Physical-Intelligence/openpi)
- ⭐⭐ **[A Pragmatic VLA Foundation Model](https://arxiv.org/abs/2601.18692)** (2026) — LingBot-VLA: an Apache-2.0 foundation model trained on about 20,000 hours of real data from nine dual-arm setups, tested on four platforms with 100 tasks each; code, base model and benchmark data are released. · [code](https://github.com/Robbyant/lingbot-vla) · [project](https://technology.robbyant.com/lingbot-vla)
- ⭐⭐ **[From Pixels to Actions - Towards Native Vision-Language-Action Policies](https://arxiv.org/abs/2611.06918)** (2026) — NEO-VLA drops the visual encoder: images and language evolve in one backbone and a flow-matching action expert reads several depths. Layer probing shows action signals often peak before the final visual layer. · [code](https://github.com/EvolvingLMMs-Lab/NEO) · [project](https://weichenfan.github.io/NEO-VLA-Page/)
- ⭐⭐ **[Open-HumanWAM: An Open Recipe for Scaling Human and Robot Experience for Embodied Foundation Models](https://arxiv.org/abs/2611.06817)** (2026) — Opens a 50,000-hour annotated egocentric video corpus with pipelines and checkpoints. Reports a log-linear law between pretraining hours and robot success, and 84.6% on RoboTwin 2.0 Clean2Random. · [code](https://github.com/DAGroup-PKU/HumanNet) · [project](https://dagroup-pku.github.io/open-humanscale/)
- ⭐⭐ **[RoboColosseum: Evaluating Physical Intelligence at Scale In-The-Wild](https://arxiv.org/abs/2611.02497)** (2026) — Blinded pairwise trials at 124 sites compare VLAs and frontier agents. Rankings barely agree across robots (W = 0.24), and open rankings poorly predict results after fine-tuning; no policy finishes a G1 task. · [code](https://github.com/RoboColosseum/robocolosseum-client)
- ⭐⭐ **[π\*0.6: a VLA That Learns From Experience](https://arxiv.org/abs/2511.14759)** (2025) — RECAP trains a VLA with RL via advantage conditioning on demos, on-robot rollouts and teleop corrections; reports it more than doubles throughput on hard tasks like laundry folding and espresso making. · [project](https://pi.website/blog/pistar06)
- ⭐⭐ **[OpenVLA: An Open-Source Vision-Language-Action Model](https://arxiv.org/abs/2406.09246)** (2024) — A 7B open VLA built on Llama 2 + DINOv2/SigLIP; the de-facto open baseline for VLA research and LoRA fine-tuning. · [code](https://github.com/openvla/openvla)
- ⭐⭐ **[RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818)** (2023) — Coined "VLA" — co-fine-tuning a web-scale VLM to output action tokens transfers semantic knowledge to robot control. · [project](https://robotics-transformer2.github.io/)
- ⭐ **[Being-H0.5: Scaling Human-Centric Robot Learning for Cross-Embodiment Generalization](https://arxiv.org/abs/2601.12993)** (2026) — CoRL 2026 Oral. Cross-embodiment VLA that treats human interaction traces as a shared language, pre-trained on UniHand-2.0: over 35,000 hours of multimodal data across 30 robot embodiments. · [code](https://github.com/BeingBeyond/Being-H) · [project](https://research.beingbeyond.com/being-h05)
- ⭐ **[Demystifying When and Why VLAs Fail in Contact-Rich Tasks and How to Fix Them](https://arxiv.org/abs/2608.01402)** (2026) — CoRL 2026 Spotlight. Studies why VLA models struggle in contact-rich manipulation and separates two failure modes: precision failures, where policies struggle to produce small corrective actions, and force failures.
- ⭐ **[EagleVLA: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference](https://arxiv.org/abs/2607.12659)** (2026) — EagleVLA: asynchronous VLA inference for low-power onboard chips such as Jetson Orin, tackling perception-execution misalignment and slow reaction; a CoRL 2026 Spotlight, formerly titled Jetson-PI. · [code](https://github.com/PKU-SEC-Lab/EagleVLA)
- ⭐ **[GigaBrain-0.5M\*: a VLA That Learns From World Model-Based Reinforcement Learning](https://arxiv.org/abs/2602.12099)** (2026) — Post-trains a VLA (GigaBrain-0.5, 10k+ h of robot data) with RL conditioned on a video world model's predictions (RAMP); reports ~30% over the RECAP baseline on laundry folding, box packing and espresso making. · [code](https://github.com/open-gigaai/giga-brain-0) · [project](https://gigabrain05m.github.io)

**[All 259 entries →](lists/vla.md)**

<a id="manipulation"></a>
### Manipulation & Dexterous Hands

_Imitation learning, diffusion policies, grasping, bimanual and dexterous manipulation._ [Browse with the latest papers →](https://hu-zlatan.github.io/embodied-ai-radar/topics/manipulation.html)

- ⭐⭐⭐ **[Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://arxiv.org/abs/2303.04137)** (2023) — Generating action sequences by denoising handles multimodal demos far better than regression; now a standard IL baseline. · [code](https://github.com/real-stanford/diffusion_policy)
- ⭐⭐ **[AIRoA-0: Long-Horizon, Precise, Cross-Embodiment Manipulation from Handheld Data](https://arxiv.org/abs/2611.03815)** (2026) — Learned from 16,151 hours of handheld gripper demos with no robot data; reports 78% average success over ten tasks versus 27% for the best other VLA, and releases the dataset, weights and post-training recipe. · [code](https://github.com/airoa-org/AIRoA-0) · [project](https://a-0.airoa.io)
- ⭐⭐ **[Generalizable Humanoid Manipulation with 3D Diffusion Policies](https://arxiv.org/abs/2410.10803)** (2024) — iDP3: whole-upper-body teleop, a 25-DoF humanoid with 3D LiDAR, and an improved 3D Diffusion Policy for noisy human data, aiming at skills beyond a single scene. · [code](https://github.com/YanjieZe/Improved-3D-Diffusion-Policy) · [project](https://humanoid-manipulation.github.io/)
- ⭐⭐ **[Universal Manipulation Interface: In-The-Wild Robot Teaching Without In-The-Wild Robots](https://arxiv.org/abs/2402.10329)** (2024) — A handheld gripper with a GoPro collects demos anywhere; policies transfer directly to robot arms. · [code](https://github.com/real-stanford/universal_manipulation_interface)
- ⭐⭐ **[Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://arxiv.org/abs/2304.13705)** (2023) — ALOHA + ACT — a ~$20k bimanual teleop rig and an action-chunking Transformer that learns precise tasks from ~50 demos. · [code](https://github.com/tonyzhaozh/act)
- ⭐ **[Constraint-Decomposed Impedance Control from Generative Policy for Articulated Object Manipulation](https://arxiv.org/abs/2610.16316)** (2026) — CoRL 2026 Spotlight. Addresses impedance gain selection for articulated tasks such as doors, bolts and drawers, where neural policies may violate kinematic constraints. · [code](https://github.com/erickun0125/constraint-decomposed-impedance-control) · [project](https://erickun0125.github.io/constraint-decomposed-impedance/)
- ⭐ **[HexaShell: A Universal Harness for Robot Coding Agents in Simulation and the Real World](https://arxiv.org/abs/2610.23479)** (2026) — A coding agent drives a bimanual robot through one command line; after each failure it reads the logs and writes or fixes small reusable tool programs. · [code](https://github.com/HexaFuture/HexaShell)
- ⭐ **[Learning Object-Centric Motion Priors from Human for Robotic Dexterous Manipulation](https://arxiv.org/abs/2611.05979)** (2026) — Learns to predict future hand-object states from human interaction datasets and uses the predicted object states as a general RL reward, reducing reward engineering; deployed on different hands (AAAI oral).
- ⭐ **[Long-Horizon Multi-Object Rearrangement via Distilled Tree Search over Continuous Actions](https://arxiv.org/abs/2610.25785)** (2026) — DISCO runs progressive-widening MCTS in GPU-parallel simulation, with a learned policy proposing continuous actions, then distills plans into a policy-value model used without search. Reports wins over BC, RL and search. · [code](https://github.com/kallol-saha/DISCO) · [project](https://distilled-search.github.io)
- ⭐ **[Noise-Invariant Spatial Encoding for 3D Manipulation Policies under Depth Corruption](https://arxiv.org/abs/2610.24674)** (2026) — NISE targets the sharp failure of 3D policies under realistic depth noise, carrying position uncertainty into attention; tested on transparent and reflective objects with commodity RGB-D.
- ⭐ **[3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations](https://arxiv.org/abs/2403.03954)** (2024) — Conditions a diffusion policy on a compact point-cloud encoding; more data-efficient and robust to viewpoint than images. · [code](https://github.com/YanjieZe/3D-Diffusion-Policy)
- ⭐ **[Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation](https://arxiv.org/abs/2401.02117)** (2024) — Puts ALOHA on a mobile base; co-training with static ALOHA data boosts mobile tasks like cooking and opening cabinets. · [code](https://github.com/MarkFzp/mobile-aloha)

**[All 170 entries →](lists/manipulation.md)**

<a id="tactile"></a>
### Tactile & Visuotactile Sensing

_Tactile sensors, touch representations and contact-rich control._ [Browse with the latest papers →](https://hu-zlatan.github.io/embodied-ai-radar/topics/tactile.html)

- ⭐⭐⭐ **[DIGIT: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation](https://arxiv.org/abs/2005.14679)** (2020) — An inexpensive, compact GelSight-style fingertip sensor that made vision-based touch widely accessible. · [code](https://github.com/facebookresearch/digit-interface)
- ⭐ **[Visible Touch: Rendering Contact for Visuomotor Policies](https://arxiv.org/abs/2609.14156)** (2026) — CoRL 2026 Spotlight. Brings contact into image-conditioned policies by rendering it, targeting the gap left by approaches that need tactile hardware, separate tactile encoders or non-image backbones. · [code](https://github.com/qaz1678249/visibletouch) · [project](https://visibletouch.github.io/)
- **[Blind Dexterous Grasping via Real2Sim2Real Tactile Policy Learning](https://arxiv.org/abs/2606.11767)** (2026) — Tactile-only blind grasping on a LEAP Hand: calibrate a digital twin to reproduce real touch signals, pretrain a layout-aware tactile encoder, and distill object-specific RL experts into a diffusion policy.
- **[Equivariant Visual-Tactile Diffusion Policy for Contact-Rich Manipulation](https://arxiv.org/abs/2610.03333)** (2026) — VISTA: equivariant visuotactile diffusion policy that fuses touch into spherical visual tokens and rotates them with the gripper pose, for more data-efficient contact-rich imitation. · [code](https://github.com/Kenn3o3/Vista) · [project](https://vista-paper.github.io/)
- **[FM-VLA: Force-based Memory for Vision-Language-Action Models in Contact-Rich Manipulation](https://arxiv.org/abs/2607.18231)** (2026) — Gives a VLA memory through compact force-history tokens from a pretrained VAE, for tasks like pressing a button a set number of times. Reports over 80% success on three memory-dependent tasks. · [project](https://qft-333.github.io/FM-VLA-Page/)
- **[FTP-1: A Generalist Foundation Tactile Policy Across Tactile Sensors for Contact-Rich Manipulation](https://arxiv.org/abs/2606.13102)** (2026) — Tactile policy pretrained on ~3,000 hours from 26 sources and 21 sensors, mapping image, array and state signals into shared tokens. Reports +17.2% on seen setups and +31% on two unseen sensor setups. · [code](https://github.com/michaelyuancb/ftp1-policy) · [project](https://ftp1-policy.github.io)
- **[ForceBand: Learning Forceful Manipulation with sEMG](https://arxiv.org/abs/2606.26093)** (2026) — Low-cost wrist sEMG band whose model predicts per-finger forces, turning video demos into force-labelled ones after a short calibration. Reports >50% lower force error than vision and 87% on force-sensitive tasks. · [code](https://github.com/Bottle101/ForceBand) · [project](https://forceband-emg.github.io)
- **[Heterogeneous Tactile Transformer](https://arxiv.org/abs/2606.29948)** (2026) — Shared tactile representation across sensors: sensor-specific encoders plus a common transformer, pretrained on a new 1.6M-frame paired dataset from four sensors; adapts to new tasks and unseen sensors. · [code](https://github.com/jxbi1010/HTT) · [project](https://jxbi1010.github.io/htt-gh-page/)
- **[How Firm Should a Grasp Be?](https://arxiv.org/abs/2610.11221)** (2026) — Estimates mass, elasticity and friction visuotactilely during the grasp and applies the minimum safe grip force; adds a dataset of fruits and vegetables with measured physical properties.
- **[Inference-time Policy Steering via Vision and Touch](https://arxiv.org/abs/2606.14981)** (2026) — Inference-time steering with vision and touch: visual sampling picks the behaviour, tactile-guided diffusion editing fixes local contact, scored by a visuo-tactile latent world model. Reports +51% over the base policy. · [code](https://github.com/yilin-wu98/vital) · [project](https://yilin-wu98.github.io/vital_website)
- **[Learning with Object-centric Representations of Tactile Interactive Perception for Robot Manipulation](https://arxiv.org/abs/2609.33235)** (2026) — Learns object representations from tactile exploration, aligned with text descriptions of properties, and uses them as context for manipulation. Reports task success from 41% to 92% (seen) and 19% to 67% (unseen). · [project](https://xinyiyxyx.github.io/tactile-object-centric/)
- **[Modular Sensory Stream for Integrating Physical Feedback in Vision-Language-Action Models](https://arxiv.org/abs/2604.23272)** (2026) — Adds separate tactile, force and torque streams to a pretrained VLA through joint cross-modal attention, with staged training and an auxiliary task that predicts future physical signals. Real-robot tests. · [project](https://jiminlx.github.io/MoSS)

**[All 76 entries →](lists/tactile.md)**

<a id="locomotion"></a>
### Locomotion & Humanoids

_Legged locomotion, humanoid whole-body control and parkour._ [Browse with the latest papers →](https://hu-zlatan.github.io/embodied-ai-radar/topics/locomotion.html)

- ⭐⭐⭐ **[Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning](https://arxiv.org/abs/2109.11978)** (2021) — Thousands of parallel GPU environments train a quadruped walking policy in minutes; legged_gym became a standard starter. · [code](https://github.com/leggedrobotics/legged_gym)
- ⭐⭐ **[Perceptive Humanoid Motion from Simulation](https://arxiv.org/abs/2611.06908)** (2026) — HALO trains humanoid skills on vision-language-motion data synthesised in a thousand procedural homes, so data scales with compute. Reports zero-shot transfer: 91% over 360 trials in six real environments. · [code](https://github.com/apple-aiml-research/ml-halo) · [project](https://apple-aiml-research.github.io/ml-halo/)
- ⭐⭐ **[BeyondMimic: From Motion Tracking to Versatile Humanoid Control via Guided Diffusion](https://arxiv.org/abs/2508.08241)** (2025) — One motion-tracking recipe with shared hyperparameters learns agile skills (cartwheels, flip-kicks); a guided latent diffusion model composes them for new goals like joystick control, zero-shot on hardware. · [code](https://github.com/HybridRobotics/whole_body_tracking)
- ⭐⭐ **[SONIC: Supersizing Motion Tracking for Natural Humanoid Whole-Body Control](https://arxiv.org/abs/2511.07820)** (2025) — Tests scaling on humanoid control: more network, data and compute yield a generalist motion-tracking foundation model, with no manual reward engineering.
- ⭐⭐ **[Real-World Humanoid Locomotion with Reinforcement Learning](https://arxiv.org/abs/2303.03381)** (2023) — A causal Transformer policy trained in simulation walks a full-size humanoid outdoors, zero-shot.
- ⭐⭐ **[DeepMimic: Example-Guided Deep Reinforcement Learning of Physics-Based Character Skills](https://arxiv.org/abs/1804.02717)** (2018) — Showed RL can imitate a wide range of motion clips, flips and spins included, while staying robust. The motion-imitation template much humanoid work builds on. · [code](https://github.com/xbpeng/DeepMimic)
- ⭐ **[CMP: Robust Whole-Body Tracking for Loco-Manipulation via Competence Manifold Projection](https://arxiv.org/abs/2604.07457)** (2026) — CoRL 2026 Spotlight. Hardens whole-body end-effector tracking for legged manipulators against out-of-distribution inputs such as sensor noise or infeasible commands, using a frame-wise single-step safety manifold. · [project](https://shepherd1226.github.io/CMP)
- ⭐ **[SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model](https://arxiv.org/abs/2610.28480)** (2026) — Rather than distilling per-motion experts or brute-forcing one RL policy, trains a humanoid tracking policy jointly with one differentiable world model of shared dynamics, fit from simulator logs (CoRL 2026 oral). · [project](https://supermimic.github.io)
- ⭐ **[ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills](https://arxiv.org/abs/2502.01143)** (2025) — Learns a residual "delta action" model from real rollouts to fix sim physics, enabling agile athletic humanoid motions. · [code](https://github.com/LeCAR-Lab/ASAP)
- ⭐ **[KungfuBot: Physics-Based Humanoid Whole-Body Control for Learning Highly-Dynamic Skills](https://arxiv.org/abs/2506.12851)** (2025) — Learns highly dynamic skills such as kung fu and dancing, through multi-step motion processing and adaptive motion tracking. · [code](https://github.com/TeleHuman/PBHC) · [project](https://kungfubot.github.io)
- ⭐ **[OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction](https://arxiv.org/abs/2509.26633)** (2025) — Retargeting that preserves human-object and human-scene interaction rather than only body pose, generating physically plausible data for humanoid loco-manipulation. · [code](https://github.com/amazon-far/holosoma) · [project](https://omniretarget.github.io)
- ⭐ **[Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking](https://arxiv.org/abs/2510.02252)** (2025) — Shows retargeting artifacts such as foot sliding hurt tracking policies, and offers GMR, a general retargeter. Its open-source repo is widely used for humanoid data. · [code](https://github.com/YanjieZe/GMR) · [project](https://jaraujo98.github.io/retargeting_matters)

**[All 170 entries →](lists/locomotion.md)**

<a id="world-models"></a>
### World Models

_Learned dynamics, video world models, world action models (WAM) and model-based RL for embodied agents._ [Browse with the latest papers →](https://hu-zlatan.github.io/embodied-ai-radar/topics/world-models.html)

- ⭐⭐⭐ **[Mastering Diverse Domains through World Models](https://arxiv.org/abs/2301.04104)** (2023) — DreamerV3 — one set of hyperparameters works across 150+ tasks, including collecting diamonds in Minecraft from scratch. · [code](https://github.com/danijar/dreamerv3)
- ⭐⭐ **[Cosmos 3: Omnimodal World Models for Physical AI](https://arxiv.org/abs/2606.02800)** (2026) — A family of omnimodal models that handles language, image, video, audio and action in one mixture-of-transformers, folding VLMs, video generators, world simulators and world-action models into a single framework. · [code](https://github.com/nvidia/cosmos) · [project](https://research.nvidia.com/labs/cosmos-lab/cosmos3/)
- ⭐⭐ **[DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos](https://arxiv.org/abs/2602.06949)** (2026) — A foundation world model pretrained on 44k hours of egocentric human video, using continuous latent actions as proxies for missing labels, then post-trained on small robot datasets. · [code](https://github.com/NVIDIA/DreamDojo) · [project](https://dreamdojo-world.github.io/)
- ⭐⭐ **[OpenWAM: An Open, Modular Exploration Towards Systematic World-Action Model Pretraining](https://arxiv.org/abs/2609.07398)** (2026) — An open research stack that splits world-action models into composable modules, then runs controlled studies on what to inherit from video priors and how world and action learning interact. · [code](https://github.com/OpenWAM-Official/OpenWAM) · [project](https://openwam-official.github.io/)
- ⭐⭐ **[RoboJEPA: Scaling Robotic Latent World Models](https://arxiv.org/abs/2610.10515)** (2026) — A JEPA world model trained across 12 robot embodiments; its imagination error follows a power law in compute, so model quality can be predicted beyond the fitted scale. · [code](https://github.com/facebookresearch/robo_jepa) · [project](https://robojepa.github.io/)
- ⭐⭐ **[World Action Models: A Survey](https://arxiv.org/abs/2606.20781)** (2026) — Separates WAMs from world models, video generators and VLAs, then sorts work by what is generated (rendered, latent or none) and how it is built; concludes the field is moving toward generating less of the future. · [project](https://world-action-models.github.io/)
- ⭐ **[Causal World Modeling for Robot Control](https://arxiv.org/abs/2601.21998)** (2026) — LingBot-VA: an autoregressive diffusion framework that learns frame prediction and policy together, with shared video-action latents, closed-loop rollout and asynchronous inference. · [code](https://github.com/Robbyant/lingbot-va) · [project](https://technology.robbyant.com/lingbot-va)
- ⭐ **[Chunk-wise Model-based Policy Optimization](https://arxiv.org/abs/2610.14564)** (2026) — CoRL 2026 Spotlight. Model-based RL that uses a chunk world model as a differentiable training-time evaluator, targeting compounding error, inference latency and BPTT instability. · [code](https://github.com/song-wx/CMPO) · [project](https://song-wx.github.io/cmpo.github.io/)
- ⭐ **[DreamX: Video Diffusion Model is a Universal Latent Action Learner](https://arxiv.org/abs/2611.05377)** (2026) — Reuses a pretrained video diffusion model to extract compact latent actions (1,200 to 4 tokens per frame) that act as a shared interface across humans, robots and environments, including zero-shot action transfer. · [code](https://github.com/cvlab-kaist/DreamX) · [project](https://cvlab-kaist.github.io/DreamX/)
- ⭐ **[Fast-WAM: Do World Action Models Need Test-time Future Imagination?](https://arxiv.org/abs/2603.16666)** (2026) — Asks whether WAMs need future imagination at test time: keeps video co-training during training but skips video generation at inference, separating the two effects in a controlled comparison. · [code](https://github.com/yuantianyuan01/FastWAM) · [project](https://yuantianyuan01.github.io/FastWAM/)
- ⭐ **[GigaWorld-Policy: An Efficient Action-Centered World--Action Model](https://arxiv.org/abs/2603.17240)** (2026) — An action-centered WAM that predicts actions from the observation and makes video generation optional, so motion accuracy depends less on forecast quality and inference is cheaper. · [code](https://github.com/open-gigaai/giga-world-policy) · [project](https://gigaai-research.github.io/GigaWorld-Policy/)
- ⭐ **[GreenWAM: A World Foundation Model for Robotics](https://arxiv.org/abs/2610.18774)** (2026) — One world model that is also the policy, across 20 robot families mapped to a shared joint-space action format; reports strong WorldArena, RoboTwin 2.0 and LIBERO-plus results and a one-step distilled humanoid policy. · [code](https://github.com/greenvla/GreenWAM) · [project](https://greenvla.github.io/GreenWAM)

**[All 129 entries →](lists/world-models.md)**

<a id="navigation"></a>
### Navigation & Embodied Agents

_Vision-language navigation, embodied question answering, mobile manipulation and LLM planners._ [Browse with the latest papers →](https://hu-zlatan.github.io/embodied-ai-radar/topics/navigation.html)

- ⭐⭐⭐ **[Do As I Can, Not As I Say: Grounding Language in Robotic Affordances](https://arxiv.org/abs/2204.01691)** (2022) — SayCan — an LLM proposes steps and learned value functions score what the robot can actually do right now.
- ⭐ **[Driving, Fast or Slow? Neuro-Symbolic Guidance for Motion Prediction in Multi-Modal Ground Mobility](https://arxiv.org/abs/2606.15251)** (2026) — TraCS adds interpretable, probabilistic traffic-rule logic to black-box motion predictors, generated from natural-language regulations; reports consistent gains on Argoverse 2. Oral.
- ⭐ **[ViNT: A Foundation Model for Visual Navigation](https://arxiv.org/abs/2306.14846)** (2023) — A Transformer navigation policy trained on many robots' driving data that adapts to new goal types and robots with light fine-tuning. · [code](https://github.com/robodhruv/visualnav-transformer)
- ⭐ **[GNM: A General Navigation Model to Drive Any Robot](https://arxiv.org/abs/2210.03370)** (2022) — The predecessor of ViNT — one goal-conditioned navigation policy trained on pooled data from several different robots, which transfers to new robots including ones not seen in training. · [code](https://github.com/robodhruv/visualnav-transformer)
- ⭐ **[The Marathon 2: A Navigation System](https://arxiv.org/abs/2003.00368)** (2020) — The paper behind Nav2, the standard ROS 2 navigation stack - behavior-tree orchestration of planners, controllers and recovery behaviors, validated by long marathon runs on real robots. · [code](https://github.com/ros-navigation/navigation2)
- **[AcroRL: Learning Aggressive Quadrotor Inversion using Bidirectional Thrust](https://arxiv.org/abs/2605.24301)** (2026) — RL policies modulate a reference trajectory for compact quadrotor flips with reversible thrust, one policy per direction. In JAX simulation: 32% lower position RMSE and 57% shorter settling than baselines.
- **[Adaptive Risk-Certified Event-Triggered Replanning for Dynamic Navigation](https://arxiv.org/abs/2610.09302)** (2026) — Uses calibrated barrier risk (CVaR along the MPC rollout) as an early warning to switch to a safer planning mode. Reports 83.3% fewer collisions than a safety-filter-only baseline. · [project](https://nail-uh.github.io/corl2026.github.io/)
- **[An Agentic Framework for Proactive Robots with Procedural Assistance Memory](https://arxiv.org/abs/2610.21211)** (2026) — Proactive assistant robot: a VLM reads a state-machine memory of the user's routine to decide when to help, and a VLA executes. The memory is revised daily by reflection, without retraining. · [code](https://github.com/DAVIAN-Robotics/PAM) · [project](https://davian-robotics.github.io/PAM/)
- **[Approximate Imitation Learning for Event-based Quadrotor Flight in Cluttered Environments](https://arxiv.org/abs/2603.07578)** (2026) — Event-camera drone flight: learn the representation offline from a large dataset, then fine-tune the policy online on cheap state only, with no event rendering. Training drops from 52.44 h to 1.86 h.
- **[AsyncVLA: An Asynchronous VLA for Fast and Robust Navigation on the Edge](https://arxiv.org/abs/2602.13476)** (2026) — A large foundation model on a remote workstation gives high-level guidance while a light onboard Edge Adapter refines actions at high rate. Reports 40% higher success than baselines with delays up to 6 s.
- **[COOL: Curiosity-Driven Object Ownership Learning for Personalized Robotic Assistance](https://arxiv.org/abs/2610.09358)** (2026) — Learns who owns which objects from everyday observation and keeps a long-term spatial memory refreshed by curiosity-driven exploration, so commands like 'find my bottle' work.
- **[CoFL-S: Spatially Queryable Sector Flow Fields for Local Language-Conditioned Navigation](https://arxiv.org/abs/2607.02222)** (2026) — Low-level VLN action head that predicts a language-conditioned flow field over the visible sector and rolls it out into trajectories. Adds a continuous-time Habitat benchmark. · [code](https://github.com/ut-dragon-lab/CoFL)

**[All 83 entries →](lists/navigation.md)**

<a id="perception"></a>
### Perception, SLAM & 3D Mapping

_Visual / LiDAR SLAM and odometry, 3D reconstruction, object pose, depth and open-vocabulary scene maps for robots._ [Browse with the latest papers →](https://hu-zlatan.github.io/embodied-ai-radar/topics/perception.html)

- ⭐⭐⭐ **[ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM](https://arxiv.org/abs/2007.11898)** (2020) — The go-to feature-based SLAM library — monocular, stereo and RGB-D, with IMU fusion and multi-map relocalization. · [code](https://github.com/UZ-SLAMLab/ORB_SLAM3)
- ⭐⭐ **[Segment Anything](https://arxiv.org/abs/2304.02643)** (2023) — SAM — a promptable segmentation model (points, boxes, masks) trained on 1B+ masks; a standard building block for object masks in robot perception pipelines. · [code](https://github.com/facebookresearch/segment-anything)
- ⭐ **[FoundationStereo: Zero-Shot Stereo Matching](https://arxiv.org/abs/2501.09898)** (2025) — Stereo depth model trained on large synthetic data that reports strong zero-shot accuracy on real scenes — a drop-in depth source for stereo-camera robots. · [code](https://github.com/NVlabs/FoundationStereo)
- ⭐ **[SAM 3: Segment Anything with Concepts](https://arxiv.org/abs/2511.16719)** (2025) — Segments and tracks every instance of a concept given a short noun phrase or image exemplar, in images and video; trained with a data engine covering 4M concept labels, with open weights and the SA-Co benchmark. · [code](https://github.com/facebookresearch/sam3)
- ⭐ **[VGGT: Visual Geometry Grounded Transformer](https://arxiv.org/abs/2503.11651)** (2025) — One feed-forward transformer predicts cameras, depth, point maps and tracks for many views at once, in about a second. · [code](https://github.com/facebookresearch/vggt)
- ⭐ **[Depth Anything V2](https://arxiv.org/abs/2406.09414)** (2024) — Trains a large teacher only on synthetic images with precise depth, then pseudo-labels many real images to train smaller students; gives sharper, more robust monocular depth than V1. · [code](https://github.com/DepthAnything/Depth-Anything-V2)
- ⭐ **[Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data](https://arxiv.org/abs/2401.10891)** (2024) — Monocular depth model trained on tens of millions of pseudo-labelled images; a common off-the-shelf depth prior for robots. · [code](https://github.com/LiheYoung/Depth-Anything)
- ⭐ **[FAST-LIVO2: Fast, Direct LiDAR-Inertial-Visual Odometry](https://arxiv.org/abs/2408.14035)** (2024) — FAST-LIVO2 — fuses LiDAR, camera and IMU in one filter with direct (feature-free) updates for both sensors, sharing a single voxel map where image patches are attached to LiDAR points. · [code](https://github.com/hku-mars/FAST-LIVO2)
- ⭐ **[Grounding Image Matching in 3D with MASt3R](https://arxiv.org/abs/2406.09756)** (2024) — Extends DUSt3R with a dense local-feature head, so one network gives both 3D pointmaps and accurate pixel matches between views — useful for calibration-free reconstruction and localization. · [code](https://github.com/naver/mast3r)
- ⭐ **[SAM 2: Segment Anything in Images and Videos](https://arxiv.org/abs/2408.00714)** (2024) — Extends SAM to video with a streaming memory, so a mask prompted once is tracked across frames — handy for following objects during manipulation. · [code](https://github.com/facebookresearch/sam2)
- ⭐ **[BundleSDF: Neural 6-DoF Tracking and 3D Reconstruction of Unknown Objects](https://arxiv.org/abs/2303.14158)** (2023) — Tracks the 6-DoF pose of a never-seen object in RGB-D video while building its neural 3D model online, with no CAD model needed; useful for manipulating novel objects. · [code](https://github.com/NVlabs/BundleSDF)
- ⭐ **[CoTracker: It is Better to Track Together](https://arxiv.org/abs/2307.07635)** (2023) — Transformer that tracks many video points jointly rather than one at a time, staying robust through occlusions; widely used to extract motion tracks from human or robot videos for policy learning. · [code](https://github.com/facebookresearch/co-tracker)

**[All 53 entries →](lists/perception.md)**

<a id="control"></a>
### Planning, Control & Safety

_Motion planning, trajectory optimization, MPC, safety filters and safe learning-based control._ [Browse with the latest papers →](https://hu-zlatan.github.io/embodied-ai-radar/topics/control.html)

- ⭐⭐⭐ **[cuRobo: Parallelized Collision-Free Minimum-Jerk Robot Motion Generation](https://arxiv.org/abs/2310.17274)** (2023) — GPU-parallel motion generation for arms — many trajectory optimizations run at once, giving collision-free, smooth plans in milliseconds. · [code](https://github.com/NVlabs/curobo)
- ⭐ **[cuRoboV2: Dynamics-Aware Motion Generation with Depth-Fused Distance Fields for High-DoF Robots](https://arxiv.org/abs/2603.05493)** (2026) — cuRoboV2 adds torque-aware B-spline trajectory optimization and GPU-native TSDF/ESDF perception for high-DoF robots. · [code](https://github.com/NVlabs/curobo)
- ⭐ **[PyRoki: A Modular Toolkit for Robot Kinematic Optimization](https://arxiv.org/abs/2505.03728)** (2025) — PyRoki: a modular, cross-platform kinematic optimization toolkit that runs natively on CPU, GPU and TPU. · [code](https://github.com/chungmin99/pyroki) · [project](https://pyroki-toolkit.github.io)
- ⭐ **[Planning with Diffusion for Flexible Behavior Synthesis](https://arxiv.org/abs/2205.09991)** (2022) — Diffuser — treats planning as denoising whole trajectories, so goals and rewards can steer sampling; an early link between diffusion and control. · [code](https://github.com/jannerm/diffuser)
- ⭐ **[Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo](https://arxiv.org/abs/2212.00541)** (2022) — Introduces MuJoCo MPC (MJPC), an interactive tool for real-time predictive control in MuJoCo, and shows that a simple sampling-based planner is a strong baseline for contact-rich behaviours. · [code](https://github.com/google-deepmind/mujoco_mpc)
- ⭐ **[legged_control](https://github.com/qiayuanl/legged_control)** (2022) — Open-source NMPC + whole-body control + state-estimation stack for quadrupeds built on OCS2 and ros-control, with a sim-to-real path; a popular starting point for model-based legged control.
- ⭐ **[Jerk-limited Real-time Trajectory Generation with Arbitrary Target States](https://arxiv.org/abs/2105.04830)** (2021) — Ruckig — open-source C++/Python library for time-optimal, jerk-limited online trajectories to any target position, velocity and acceleration; a common drop-in for smooth arm motion on real controllers. · [code](https://github.com/pantor/ruckig)
- ⭐ **[OCS2: Optimal Control for Switched Systems](https://github.com/leggedrobotics/ocs2)** (2021) — C++ toolbox for nonlinear MPC on switched systems (SLQ, DDP, SQP) with robot examples for legged robots and mobile manipulators; the base of many open-source legged MPC + whole-body control stacks.
- ⭐ **[OSQP: An Operator Splitting Solver for Quadratic Programs](https://arxiv.org/abs/1711.08013)** (2020) — A fast, robust ADMM-based QP solver with warm starting and embedded C code generation; widely used inside MPC and whole-body controllers. · [code](https://github.com/osqp/osqp)
- ⭐ **[Crocoddyl: An Efficient and Versatile Framework for Multi-Contact Optimal Control](https://arxiv.org/abs/1909.04947)** (2019) — An open-source DDP-based solver for contact-rich trajectory optimization, widely used for legged and humanoid motion generation and MPC. · [code](https://github.com/loco-3d/crocoddyl)
- ⭐ **[MoveIt 2](https://moveit.ai/)** (2019) — The ROS 2 manipulation framework - motion planning, inverse kinematics, collision checking and real-time servoing for robot arms. · [code](https://github.com/moveit/moveit2)
- ⭐ **[Pinocchio](https://github.com/stack-of-tasks/pinocchio)** (2019) — Fast C++/Python rigid-body dynamics library with analytical derivatives; a common backbone for kinematics, optimal control (e.g. Crocoddyl) and legged/humanoid control stacks.

**[All 50 entries →](lists/control.md)**

<a id="learning"></a>
### Robot Learning: RL & Imitation

_Reinforcement learning, imitation learning and policy post-training methods for robots, on any embodiment._ [Browse with the latest papers →](https://hu-zlatan.github.io/embodied-ai-radar/topics/learning.html)

- ⭐⭐⭐ **[Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)** (2017) — The clipped policy-gradient method behind most GPU-parallel sim-to-real locomotion and dexterity training.
- ⭐⭐ **[Precise and Dexterous Robotic Manipulation via Human-in-the-Loop Reinforcement Learning](https://arxiv.org/abs/2410.21845)** (2024) — HIL-SERL — real-world RL with human corrections, reported to reach near-perfect success on precise assembly and dynamic tasks after a few hours of training. · [code](https://github.com/rail-berkeley/hil-serl)
- ⭐ **[Control-Ready Uncertainty for Trajectory Diffusion](https://arxiv.org/abs/2610.12431)** (2026) — SCOPE gives diffusion trajectory models calibrated uncertainty tubes without Monte Carlo sampling, by distilling score curvature; tested in crowd navigation and Franka manipulation. · [project](https://zackaxue.github.io/SCOPE-project-page/)
- ⭐ **[Diffusion ReRoll: Revisable Denoising for Robotic Sequential Prediction](https://arxiv.org/abs/2607.19919)** (2026) — CoRL 2026 Spotlight. Diffusion sequence prediction with selective re-noising, so segments of the horizon can be refined again using context from the rest. · [project](https://seonsoo-p1.github.io/DiffusionReRoll/)
- ⭐ **[FedGuide: Diffusion Prior Alignment and Value Baseline Guidance for Heterogeneous Federated Reinforcement Learning](https://arxiv.org/abs/2609.18964)** (2026) — Federated RL for heterogeneous clients that aggregates diffusion behavior priors with optimal transport rather than averaging policies, plus a low-variance DICE value baseline.
- ⭐ **[Learning from Fleet Experience: Collective Experience Learning Across 96 Robots](https://arxiv.org/abs/2610.25736)** (2026) — Deployed robots pool their runs; failures retrieve matching successful segments from the fleet buffer to fine-tune on, with no new demos. Reports 93–99% on five real tasks; 96 robots lift phone packing 79% → 98%. · [code](https://github.com/RLinf/RLinf) · [project](https://cel-robot-learning.github.io)
- ⭐ **[Scaling in Games: Continued Pre-Training For Embodied Agents In Diverse Virtual Worlds](https://arxiv.org/abs/2610.28698)** (2026) — Continued pre-training study for game-playing agents: 120 runs over 0.8B–27B models, 50–1,600 h of data and multi-world mixes; reports diversity aids transfer to related worlds, little to distant ones. · [code](https://github.com/THUSI-Lab/GameScaling) · [project](https://gamescaling.github.io)
- ⭐ **[RLinf-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models](https://arxiv.org/abs/2510.06710)** (2025) — Open RL training framework for VLAs (PPO/GRPO across GPU-parallel simulators); reports 98.11% on 130 LIBERO tasks and 97.66% on 25 ManiSkill tasks after RL — a common base for VLA+RL work. · [code](https://github.com/RLinf/RLinf)
- ⭐ **[SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning](https://arxiv.org/abs/2509.09674)** (2025) — Online RL for VLAs with GRPO and only binary success rewards on OpenVLA-OFT, plus exploration tweaks; reports 99.1% on LIBERO and 70.4% on RoboTwin 1.0 (vs 39.8% for the SFT baseline). · [code](https://github.com/PRIME-RL/SimpleVLA-RL)
- ⭐ **[Decision Transformer: Reinforcement Learning via Sequence Modeling](https://arxiv.org/abs/2106.01345)** (2021) — Recasts RL as sequence modeling — a GPT-style model predicts actions conditioned on the desired return; an early bridge between transformers and control. · [code](https://github.com/kzl/decision-transformer)
- ⭐ **[What Matters in Learning from Offline Human Demonstrations for Robot Manipulation](https://arxiv.org/abs/2108.03298)** (2021) — robomimic — a controlled study of imitation and offline RL on human-collected manipulation demos (demo quality, observation choices, history-aware BC), released with the framework and datasets. · [code](https://github.com/ARISE-Initiative/robomimic)
- ⭐ **[Addressing Function Approximation Error in Actor-Critic Methods](https://arxiv.org/abs/1802.09477)** (2018) — TD3 — fixes DDPG's value overestimation with twin critics, delayed policy updates and target smoothing; still a standard continuous-control baseline. · [code](https://github.com/sfujim/TD3)

**[All 132 entries →](lists/learning.md)**

<a id="sim"></a>
### Sim-to-Real & Simulators

_Physics simulators, GPU-parallel training and transfer to real robots._ [Browse with the latest papers →](https://hu-zlatan.github.io/embodied-ai-radar/topics/sim.html)

- ⭐⭐⭐ **[MuJoCo](https://mujoco.org/)** (2012) — Fast, accurate contact physics; the default simulator for robot learning research, open-sourced by DeepMind. · [code](https://github.com/google-deepmind/mujoco)
- ⭐⭐ **[When the Simulator Fails, Not the Policy: Auditing Contact Artifacts in Simulated Robot Benchmarks](https://arxiv.org/abs/2610.41857)** (2026) — Many benchmark 'policy failures' are physics-engine ejections. SimuGuard traced RoboTwin artifacts to one collision constant; changing it cut artifact episodes from 12/100 to none and lifted five tasks 89% → 98%. · [code](https://github.com/ALEXander22568/simuguard)
- ⭐ **[Genie Sim 3.0 : A High-Fidelity Comprehensive Simulation Platform for Humanoid Robot](https://arxiv.org/abs/2601.02078)** (2026) — Genie Sim 3.0: a manipulation simulation platform whose LLM tool builds scenes from natural language, with an LLM- and VLM-based automated benchmark. · [code](https://github.com/AgibotTech/genie_sim)
- ⭐ **[Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning](https://arxiv.org/abs/2511.04831)** (2025) — The reference paper for Isaac Lab, Orbit's successor — GPU-parallel physics, rendering and sensor simulation with ready-made robots and tasks for RL and imitation. · [code](https://github.com/isaac-sim/IsaacLab)
- ⭐ **[MuJoCo Playground](https://arxiv.org/abs/2502.08844)** (2025) — GPU-accelerated MJX environments for locomotion and manipulation that train in minutes and transfer to real robots. · [code](https://github.com/google-deepmind/mujoco_playground)
- ⭐ **[Newton](https://github.com/newton-physics/newton)** (2025) — Open, GPU-accelerated physics engine built on NVIDIA Warp and OpenUSD with multiple solvers for contact-rich robot learning; co-developed by Disney Research, Google DeepMind and NVIDIA, hosted by the Linux Foundation.
- ⭐ **[RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization for Robust Bimanual Robotic Manipulation](https://arxiv.org/abs/2506.18088)** (2025) — Simulation pipeline that writes and checks task code with multimodal LLMs to mass-produce bimanual demos under heavy randomization (clutter, lighting, backgrounds, instructions); also a 50-task dual-arm benchmark. · [code](https://github.com/RoboTwin-Platform/RoboTwin)
- ⭐ **[GRUtopia: Dream General Robots in a City at Scale](https://arxiv.org/abs/2407.10943)** (2024) — Simulated interactive 3D society for many robot types; its GRScenes set has 100k annotated scenes across 89 categories that combine into city-scale worlds. · [code](https://github.com/OpenRobotLab/GRUtopia)
- ⭐ **[Genesis](https://github.com/Genesis-Embodied-AI/Genesis)** (2024) — An open-source, Python-native physics platform covering rigid bodies, soft bodies, fluids and fast GPU simulation.
- ⭐ **[Humanoid-Gym: Reinforcement Learning for Humanoid Robot with Zero-Shot Sim2Real Transfer](https://arxiv.org/abs/2404.05695)** (2024) — Isaac Gym–based RL framework for humanoid locomotion with a sim-to-sim check in MuJoCo before deploying zero-shot to real humanoids; a common starting point for humanoid RL. · [code](https://github.com/roboterax/humanoid-gym)
- ⭐ **[ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI](https://arxiv.org/abs/2410.00425)** (2024) — GPU-parallel simulation and rendering with many manipulation tasks; fast visual RL and data generation. · [code](https://github.com/haosulab/ManiSkill)
- ⭐ **[RoboCasa: Large-Scale Simulation of Everyday Tasks for Generalist Robots](https://arxiv.org/abs/2406.02523)** (2024) — 120 kitchen scenes, 2,500+ objects and 100 tasks with generated demonstrations for training generalist policies. · [code](https://github.com/robocasa/robocasa)

**[All 63 entries →](lists/sim.md)**

<a id="datasets"></a>
### Datasets & Benchmarks

_Large robot datasets, egocentric data and evaluation suites._ [Browse with the latest papers →](https://hu-zlatan.github.io/embodied-ai-radar/topics/datasets.html)

- ⭐⭐⭐ **[Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://arxiv.org/abs/2310.08864)** (2023) — 1M+ trajectories from 22 robot types pooled by 30+ labs; RT-X models trained on it beat single-robot baselines. · [code](https://github.com/google-deepmind/open_x_embodiment)
- ⭐⭐ **[LeRobot](https://github.com/huggingface/lerobot)** (2024) — PyTorch library with datasets, pretrained policies (ACT, Diffusion, SmolVLA) and drivers for low-cost arms.
- ⭐⭐ **[LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning](https://arxiv.org/abs/2306.03310)** (2023) — 130 language-conditioned tasks in four suites; now the most common simulation benchmark for VLA papers. · [code](https://github.com/Lifelong-Robot-Learning/LIBERO)
- ⭐ **[BEAKER: An Expert-Curated Benchmark for Embodied Brains in Self-Driving Chemical Laboratories](https://arxiv.org/abs/2611.06911)** (2026) — 1,000 expert-curated questions over 11 image and video task types test multimodal LLMs as the brain of a self-driving chemistry lab: affordances, trajectories, apparatus setup, safety and step reasoning.
- ⭐ **[WireCraft: A Simulation Benchmark for Industrial DLO Manipulation](https://arxiv.org/abs/2606.18097)** (2026) — CoRL 2026 Spotlight. Simulation benchmark for wires and cables in industrial assembly, aimed at the gap left by benchmarks tied to specific hardware or lacking modular, customizable task assets.
- ⭐ **[RoboVerse: Towards a Unified Platform, Dataset and Benchmark for Scalable and Generalizable Robot Learning](https://arxiv.org/abs/2504.18904)** (2025) — MetaSim puts many simulators (Isaac Sim/Gym, MuJoCo, Genesis, SAPIEN…) behind one interface; adds a large synthetic dataset migrated from public benchmarks and unified IL/RL benchmarks. · [code](https://github.com/RoboVerseOrg/RoboVerse) · [project](https://roboverseorg.github.io/)
- ⭐ **[Evaluating Real-World Robot Manipulation Policies in Simulation](https://arxiv.org/abs/2405.05941)** (2024) — SimplerEnv — real-to-sim environments whose scores correlate with real-robot results for RT-1/Octo-style policies. · [code](https://github.com/simpler-env/SimplerEnv)
- ⭐ **[CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks](https://arxiv.org/abs/2112.03227)** (2021) — Chains of five language instructions in a row test long-horizon, language-conditioned control. · [code](https://github.com/mees/calvin)
- ⭐ **[Habitat: A Platform for Embodied AI Research](https://arxiv.org/abs/1904.01201)** (2019) — A very fast photorealistic 3D simulator and task suite that standardized embodied navigation research. · [code](https://github.com/facebookresearch/habitat-sim)
- ⭐ **[Meta-World: A Benchmark and Evaluation for Multi-Task and Meta Reinforcement Learning](https://arxiv.org/abs/1910.10897)** (2019) — 50 Sawyer manipulation tasks for multi-task and meta-RL evaluation. · [code](https://github.com/Farama-Foundation/Metaworld)
- ⭐ **[RLBench: The Robot Learning Benchmark & Learning Environment](https://arxiv.org/abs/1909.12271)** (2019) — 100 hand-designed manipulation tasks with demos; a staple for 3D policy methods like PerAct. · [code](https://github.com/stepjam/RLBench)
- ⭐ **[ScanNet: Richly-annotated 3D Reconstructions of Indoor Scenes](https://arxiv.org/abs/1702.04405)** (2017) — RGB-D scans of 1,500+ indoor scenes with 3D reconstructions, camera poses and semantic labels; the standard benchmark for 3D scene understanding that embodied perception builds on. · [code](https://github.com/ScanNet/ScanNet)

**[All 97 entries →](lists/datasets.md)**

<a id="hardware"></a>
### Hardware & Open-Source Robots

_Low-cost arms, hands, grippers and data-collection rigs you can build._ [Browse with the latest papers →](https://hu-zlatan.github.io/embodied-ai-radar/topics/hardware.html)

- ⭐⭐⭐ **[LEAP Hand: Low-Cost, Efficient, and Anthropomorphic Hand for Robot Learning](https://arxiv.org/abs/2309.06440)** (2023) — A 16-DoF dexterous hand buildable for about $2,000 from off-the-shelf parts. · [code](https://github.com/leap-hand/LEAP_Hand_API) · [project](https://leaphand.com/)
- ⭐⭐ **[Pixel: A Co-Designed Full-Stack Robot System for Learning General-Purpose Mobile Manipulation](https://arxiv.org/abs/2611.03648)** (2026) — Hardware, data and learning designed together: a low-cost wheeled humanoid with compliant grippers, teleoperation and robot-free human data collection, one whole-body controller and a shared policy pipeline. · [project](https://pixel-robot.com/pixel)
- ⭐ **[Demonstrating Berkeley Humanoid Lite: An Open-source, Accessible, and Customizable 3D-printed Humanoid Robot](https://arxiv.org/abs/2504.17249)** (2025) — Open-source humanoid with 3D-printed modular gearboxes, buildable for under US$5,000; hardware designs, embedded code and training code are released. · [code](https://github.com/HybridRobotics/Berkeley-Humanoid-Lite) · [project](https://lite.berkeley-humanoid.org)
- ⭐ **[OpenArm](https://github.com/enactic/openarm)** (2025) — Fully open-source 7-DoF humanoid arm for contact-rich work — CAD, electronics, firmware, ROS 2 and MuJoCo/Genesis models, plus leader–follower force-feedback teleop and gravity compensation. · [project](https://openarm.dev)
- ⭐ **[ALOHA 2: An Enhanced Low-Cost Hardware for Bimanual Teleoperation](https://arxiv.org/abs/2405.02292)** (2024) — Upgraded ALOHA bimanual rig (stronger grippers, gravity compensation, sturdier frame) with open hardware designs and a MuJoCo model for simulation. · [code](https://github.com/tonyzhaozh/aloha) · [project](https://aloha-2.github.io/)
- ⭐ **[Open-TeleVision: Teleoperation with Immersive Active Visual Feedback](https://arxiv.org/abs/2407.01512)** (2024) — VR teleoperation with an actively steered stereo camera, used to collect humanoid manipulation data. · [code](https://github.com/OpenTeleVision/TeleVision)
- ⭐ **[SO-ARM100 / SO-101](https://github.com/TheRobotStudio/SO-ARM100)** (2024) — An open 3D-printed 6-DoF arm (leader + follower) costing roughly $100–200 per arm; the default LeRobot starter kit.
- ⭐ **[An Open Torque-Controlled Modular Robot Architecture for Legged Locomotion Research](https://arxiv.org/abs/1910.00093)** (2019) — The open-source Solo quadruped and its modular torque-controlled actuators, built from off-the-shelf and 3D-printed parts so labs can reproduce a dynamic legged robot. · [code](https://github.com/open-dynamic-robot-initiative/open_robot_actuator_hardware)
- **[Belt-Finger: An Affordable Soft Belt-Driven Gripper for Dexterous In-Hand Manipulation](https://arxiv.org/abs/2606.20193)** (2026) — A cheap drop-in finger module for parallel grippers: two soft belts keep normal open/close and add in-hand translation, pitch and roll; used with MPC, a light 10-DoF teleop interface and learned policies.
- **[Hardware-as-Regularization: Enhancing Data Consistency in Imitation Learning via an Adjustable Passive Compliant Leader Arm](https://arxiv.org/abs/2610.22977)** (2026) — Adds a cheap clutch and 3D-printed spring to each joint of a passive leader arm so redundant joints return to a neutral pose, making demos more consistent; block stacking success 73.3% vs 36.7%.
- **[PanoVine: Whole-Body Visuomotor Control for Soft Growing Vine Robot](https://arxiv.org/abs/2606.22923)** (2026) — First autonomous vine (soft growing) robot: 19 cameras along its body feed an end-to-end visuomotor policy learned from demos, which steers through branches, up slopes and into confined spaces. · [code](https://github.com/xxm19/panovine) · [project](https://panovine-bot.github.io)
- **[RealDexUMI: A Wearable Universal Manipulation Interface for Dexterous Robot Learning](https://arxiv.org/abs/2606.06033)** (2026) — Wearable dexterous UMI: a shared end-effector module (light hand, in-hand camera, fingertip touch) driven by an isomorphic glove, so collected and deployed observations and actions match. Eight real tasks.

**[All 51 entries →](lists/hardware.md)**

<!-- radar:end -->

## Related lists & learning resources

Other good maps of the field, plus courses and docs we point newcomers to. This radar complements them with search, a daily feed and bilingual takeaways.

<!-- resources:start -->

**Related lists**

- [Embodied-AI-Guide](https://github.com/TianxingChen/Embodied-AI-Guide) `中文` — A large Chinese-language beginner's guide to embodied AI, from fundamentals to research directions.
- [Embodied_AI_Paper_List (HCPLab-SYSU)](https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List) — Paper list accompanying a survey of embodied AI, organized by perception, interaction, agents and sim-to-real.
- [awesome-humanoid-robot-learning](https://github.com/YanjieZe/awesome-humanoid-robot-learning) — A focused list of humanoid robot learning papers.
- [Awesome-Robotics-Foundation-Models](https://github.com/robotics-survey/Awesome-Robotics-Foundation-Models) — Papers on foundation models in robotics, from the survey "Foundation Models in Robotics".
- [awesome-embodied-vla-va-vln](https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln) — A frequently updated list of vision-language-action (VLA) and vision-language navigation (VLN) papers.

**Courses & textbooks**

- [Robotic Manipulation (MIT 6.4210, Russ Tedrake)](https://manipulation.csail.mit.edu/) — Free online textbook and course on perception, planning and control for manipulation, with Drake notebooks.
- [Underactuated Robotics (MIT, Russ Tedrake)](https://underactuated.mit.edu/) — Free online textbook on nonlinear dynamics, optimal control and trajectory optimization for walking, flying and swimming robots.
- [CS 285 Deep Reinforcement Learning (UC Berkeley)](https://rail.eecs.berkeley.edu/deeprlcourse/) — Sergey Levine's deep RL course; lecture videos and slides are public.
- [蘑菇书 EasyRL (Datawhale)](https://github.com/datawhalechina/easy-rl) `中文` — A popular open Chinese reinforcement-learning tutorial (from Q-learning to PPO, DDPG and TD3) with code; readable online.
- [动手学强化学习 (Hands-on RL)](https://github.com/boyu-ai/Hands-on-RL) `中文` — Chinese RL textbook built from runnable Jupyter notebooks; the online version is at hrl.boyuai.com.

**Tool docs**

- [LeRobot documentation](https://huggingface.co/docs/lerobot) — Hands-on docs for Hugging Face LeRobot — record data, train ACT/diffusion/VLA policies and run them on low-cost arms.
- [Isaac Lab documentation](https://isaac-sim.github.io/IsaacLab/) — Docs and tutorials for NVIDIA's GPU-parallel robot learning framework.
- [MuJoCo documentation](https://mujoco.readthedocs.io/) — Reference and modeling guide for the MuJoCo physics engine (MJX, MJCF, Python bindings).

**Communities**

- [古月居 (GuYueHome)](https://www.guyuehome.com/) `中文` — A long-running Chinese ROS and robotics community with tutorials and forums.

<!-- resources:end -->

## Contribute

Found a great paper, repo, dataset or robot that's missing — or a mistake? [Open an issue](https://github.com/hu-zlatan/embodied-ai-radar/issues/new) or send a pull request that adds one entry to `data/curated/<topic>.yaml`. See [CONTRIBUTING.md](CONTRIBUTING.md).

## How this project is run

This repository is **built and maintained by an AI agent** (Claude, made by Anthropic) that works on a schedule, under the oversight of [@hu-zlatan](https://github.com/hu-zlatan). The agent's brief is [AUTOPILOT.md](AUTOPILOT.md); its notes, decisions and run log are in [`.autopilot/`](.autopilot). Data is never invented: entries that fail verification are fixed or removed.

## License

Code: [MIT](LICENSE). Curated text and data: [CC BY 4.0](LICENSE-DATA.md). arXiv metadata: CC0, from the [arXiv API](https://info.arxiv.org/help/api/index.html) — thank you to arXiv for use of its open access interoperability.
