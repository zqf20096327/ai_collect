# Awesome Frontier Models (LLMs / VLMs) as Robot Policies [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![entries](https://img.shields.io/badge/entries-152-blue?style=flat-square) ![newest](https://img.shields.io/badge/newest%20entry-2026--11--26-green?style=flat-square) ![license](https://img.shields.io/badge/license-CC0--1.0-lightgrey?style=flat-square)

> **Can a general-purpose frontier model (GPT, Claude, Gemini, Qwen…) *be* the robot policy, and if so, what is left for the learned System 1?**
>
> A curated, data-driven list of papers, reports, benchmarks and critiques on frontier LLMs/VLMs controlling robots directly, through code, or on top of learned low-level controllers. Every entry records **what sits below the frontier model**, **how success was judged**, and **how fast and expensive it is**.

<p align="center"><img src="assets/question-in-one-picture.jpg" width="100%" alt="The question in one picture. Left, classic dual-system VLA: System 2, an onboard VLM at about 1 to 10 Hz, passes a latent or subtask to System 1, a learned policy at 50 to 200 Hz, which drives System 0, joint and torque control. Right, frontier model as policy (2026): a cloud frontier model at about 0.05 to 0.5 Hz emits code, end-effector waypoints or skill calls to System 1, which is either a learned VLA or WAM, or nothing, above System 0: IK, tracker and reflexes."></p>

<details><summary>Text version of the figure</summary>

```text
         classic dual-system VLA                      frontier model as policy (2026)       
 +--------------------------------------+      +-------------------------------------------+
 | System 2   VLM, ~1-10 Hz, onboard    |      | Frontier model (cloud), ~0.05-0.5 Hz      |
 |    | latent / subtask                |      |    | code / EEF waypoints / skill calls   |
 | System 1   learned policy, 50-200 Hz | ---> | System 1?  learned VLA/WAM  -or-  nothing |
 |    |                                 |      |    |                                      |
 | System 0   joint / torque control    |      | System 0   IK / tracker / reflexes        |
 +--------------------------------------+      +-------------------------------------------+
```

</details>

**Scope.** In: a general-purpose model that was *not* trained for robotics acts as, or directly steers, the policy. Also in, as context: the dual-system VLAs being challenged, the benchmarks both sides are scored on, and critiques. Out: robot-specific VLAs with no frontier-model angle, and pure task planners with no closed-loop control.

<a id="latest-updates"></a>
## 📰 Latest updates

- **2026-11-27** · ➕ [SOLVE](#solve), [SEEK](#seek), [Skeptic](#skeptic), [AWAIT](#await-bench), [RoboInF](#roboinf), [DeCoNav-Act](#deconav-act), [RESET](#reset-one-demo), [Paper context for LLM quadruped navigation](#paper-context-quadruped), [RoboDojo-Mirror](#robodojo-mirror), [RoboARC](#roboarc), [MFM-VLA](#mfm-vla), [ROAM-Bench](#roam-bench) · SOLVE has GPT-6 Astra write sparse end-effector keyposes instead of dense steps, reaching 74.5% on RoboDojo and 84.5% on RoboLab at $1.7 per episode, and 75 of 85 real UR12e episodes; RoboARC finds frontier coding agents solve 86% of physical puzzles with privileged state but 43% from their own sensors, while zero-shot VLAs solve none. · <sub>28 candidates screened</sub>
- **2026-11-26** · ➕ [RoboLiveMem](#robolivemem), [ICLWorld](#iclworld), [WorldLeague](#worldleague), [RUIBench](#ruibench), [RoboUniverse-10K](#robouniverse-10k), [X-Harness](#x-harness), [RoboHarness-Zero](#roboharness-zero), [RegHarness](#regharness), [RoboEvo²](#roboevo2), [Agent on Guard (AoG)](#agent-on-guard), [EvoMisty](#evomisty), [AA-Robotics-Sim](#aa-robotics-sim), [MARGIN](#margin), [RoboClock](#roboclock), [ReWeave](#reweave), [Next-Manip](#next-manip), [Atomic Policy](#atomic-policy), [Boundary-Aware Policy Learning](#boundary-aware-policy), [SkillHarness](#skillharness), [JiL (Judgment-in-the-Loop)](#jil-wam-calibration), [Weight-Space Programming for RFMs](#wsp-robot-repair), [Mibot-RUA](#mibot-rua), [RoboSpoof](#robospoof) · ✏️ [AA-Robotics](#aa-robotics), [RoboDojo](#robodojo) · 🏁 [RoboLiveMem](#robolivemem) (added) · RoboLiveMem runs the same robot-memory tasks with the world paused and running: 8 Claude and GPT models drop from 97% to 50% success. Artificial Analysis launched AA-Robotics-Sim (simulated Unitree G1; GPT-6.2 Astra 71.0) and reported GPT-6.2 Astra at 79 on AA-Robotics. Later run: Roboclock charges model thinking time to the task clock, and GPT-6 Astra falls from 19.0% to 3.0% while the fine-tuned π0.5 keeps 8.3%; Xiaomi Robotics' Mibot-RUA (GPT-6 Astra) now tops the RoboDojo agent track at 79.33% SR, starred for task-specific priors. · <sub>88 candidates screened</sub>
- **2026-11-24** · ➕ [Astra on Codex (Robocurve)](#codex-vs-inspect-robots), [Embo-Harness](#embo-harness), [Contact Harness](#contact-harness), [TRIP (Tripwire)](#trip-tripwire), [ACAP](#acap), [NavRSI](#navrsi), [Embodied-Harness](#embodied-harness), [EvoTER](#evoter), [Real2Worlds2Real](#real2worlds2real), [RoboColiseum](#robocoliseum), [ROSWorld](#rosworld), [γ-Scape](#gamma-scape), [DualManip](#dualmanip) · ✏️ [RoboDojo-RC Tier 1](#robodojo-rc-tier1) · 🏁 [Astra on Codex (Robocurve)](#codex-vs-inspect-robots) (added) · Same model, new harness: GPT-6.2 Astra scores 97% on RoboDojo-RC Tier 1 through Codex vs 65.7% through Inspect Robots; Robocurve is retiring RoboDojo. From the arXiv scan: Embo-Harness, a controlled harness study, puts a directly-acting GPT-6-Astra at 83.3% on RoboLab-120 (second to AMP1's 86.0%). · <sub>61 candidates screened</sub>
- **2026-11-23** · ➕ [Waddle-1](#waddle-1), [RoboDojo-RC Tier 1](#robodojo-rc-tier1), [HuGo](#hugo), [DiMuRe](#dimure), [SPARK](#spark-bt), [Recursia](#recursia), [SCOPE](#scope-program-edits), [UniManip](#unimanip) · Waddle-1, a robot-use agent directing local lower-level policies, tops Robocurve's RoboDojo-RC Tier 1 at 81.4% vs 65.7% for GPT-6.2 Astra (not like-for-like: no call cap). From the arXiv scan: HuGo has gpt-5.4 write closed-loop policy code over a frozen whole-body controller on a Unitree G1 (93.3% zero-shot on hardware for its best push-button policy). · <sub>62 candidates screened</sub>
- **2026-11-22** · ➕ [Claude Fable 5.2 (RoboDojo Sim)](#claude-fable-5-2), [Mind2Act World](#mind2act-world), [UniCraft](#unicraft), [SO-101 Bench](#so101-bench), [Real2Gym](#real2gym), [BiCICLe](#bicicle), [InSight](#insight-steerable-vla), [NovaPlan](#novaplan), [STeP](#step-stl), [AquaCap](#aquacap), [ScaleVLA](#scalevla), [CoEnv / CoEx](#coenv-coex) · Anthropic reports Claude Fable 5.2 at 64.9% on RoboDojo Sim in its own runs, more than double GPT-6 Astra (29.8%). · <sub>75 candidates screened</sub>
- **2026-11-21** · ➕ [AgentRoboCritic](#agentrobocritic), [ForceHarness](#forceharness), [RoboTeam](#roboteam), [PhysEvo](#physevo), [Push-T, revisited](#push-t-agentic), [EmbodyAgent](#embodyagent), [Astra as visuo-tactile policy](#astra-visuotactile), [RoC](#reasoning-on-call), [LEXP](#lexp), [ReTrace](#retrace), [LADDER](#ladder), [Gemini 4 Hydrogen](#gemini-4-hydrogen) · ✏️ [Hi Robot](#hi-robot), [Efficient VLA survey](#efficient-vla-survey), [FAEA](#faea) · ForceHarness lets frozen frontier models use force without a wrist sensor, lifting GPT-6 Astra from 2/60 to 54/60 on six real contact tasks. · <sub>43 candidates screened</sub>
- **2026-11-21** · List published with 72 entries; daily automated maintenance switched on.

## Contents

- [📰 Latest updates](#latest-updates)
- [🏁 Milestones](#milestones)
- [📊 Leaderboards: who measured what](#leaderboards)
- [🗂️ At a glance: what sits below the frontier model?](#at-a-glance)
- [🎯 Frontier Model as Direct Policy](#direct) (11)
- [🧑‍💻 Agentic & Code-Writing Policies](#agentic) (21)
- [🎛️ Frontier Model over a Learned System 1 / System 0](#orchestrated) (21)
- [📈 Getting Better Without Weight Updates](#self-improving) (24)
- [⚡ Making It Fast & Cheap](#fast) (8)
- [🧠 The Incumbent: Dual-System VLAs](#dual-system) (17)
- [📊 Benchmarks & Evaluation Reports](#benchmarks) (29)
- [🔍 Analyses, Critiques & Reproducibility](#critiques) (7)
- [🗺️ Surveys, Essays & Perspectives](#perspectives) (9)
- [🏛️ Foundations (pre-2025)](#foundations) (5)
- [Legend](#legend) · [Maintenance](#how-this-list-is-maintained) · [Related lists](#related-lists) · [Contributing](#contributing) · [Citation](#citation)

<a id="milestones"></a>
## 🏁 Milestones

| Date | Work | Why it matters |
|---|---|---|
| 2022-09-16 | [Code as Policies](#code-as-policies) | Introduced code as the interface between an LLM and a robot. |
| 2025-02-20 | [Helix](#helix) | Popularized the 'System 1 / System 2' framing for robot foundation models. |
| 2026-01-28 | [FAEA](#faea) | Early evidence that unmodified coding-agent infrastructure transfers to manipulation. |
| 2026-03-23 | [CaP-X](#cap-x) | The shared benchmark that made agent-vs-VLA comparisons routine. |
| 2026-06-18 | [ENPIRE](#enpire) | An alternative answer: the frontier model builds System 1 instead of replacing it. |
| 2026-07-09 | [Harness VLA](#harness-vla) | The canonical 'keep System 1 for contact' design. |
| 2026-07-09 | [Claude on robotics](#anthropic-robotics) | Direct evidence that a frontier model on top of System 1 can hurt in-distribution and help out-of-distribution. |
| 2026-09-07 | [Robot-Use Agents](#isola-rua) | Named and framed the 'robot-use agent' paradigm. |
| 2026-09-21 | [LLM as Policy on RoboDojo](#robodojo-astra) | First time an LLM topped a public robot-policy leaderboard. |
| 2026-09-24 | [RACaP](#racap) | One of the first concrete distillations of a frontier-agent policy into a small on-robot model. |
| 2026-10-01 | [OpenRUA](#openrua) | Showed that bespoke harness engineering may be unnecessary: native ROS 2 is enough. |
| 2026-10-14 | [Astranomy](#astranomy) | First controlled study comparing the three roles a frontier model can take: direct, agentic, and orchestrator. |
| 2026-10-18 | [Bitter Lesson → Robotics](#bitter-lesson-robotics) | First 'scaling-trend' measurement for frontier models as robot policies. |
| 2026-11-06 | [AMP1](#amp1) | A generalist model beats specialist VLAs and WAMs by a wide margin in the real world as well as in sim. |
| 2026-11-11 | [JustRUA](#justrua) | First controlled ablation showing which harness choices actually produce robot-use-agent gains. |
| 2026-11-13 | [ATLAS](#atlas) | Clearest example of a frontier agent steering a frozen System 0 rather than replacing it. |
| 2026-11-13 | [PEAR / RURL](#pear-rurl) | Robot use as an ordinary foundation-model post-training skill, with no general-capability regression. |
| 2026-11-14 | [RoboDojo leaderboard retest](#openrua-retest) | Benchmark-integrity wake-up call for LLM-as-policy leaderboards. |
| 2026-11-17 | [InteractVLA](#interactvla) | A richer System 2 → System 1 contract: geometric steering instead of language commands. |
| 2026-11-22 | [Astra on Codex (Robocurve)](#codex-vs-inspect-robots) | The top real-world RoboDojo-RC score (97%) came from swapping the harness, not the model: the same GPT-6.2 Astra had scored 65.7% under the benchmark's own harness. |
| 2026-11-23 | [RoboLiveMem](#robolivemem) | Paused-simulator results overstated frontier robot memory: with the world running instead of paused, the same 8 Claude and GPT models fell from 97% to 50% success (Claude Opus 5.5: 100% to 44%). |

<a id="leaderboards"></a>
## 📊 Leaderboards: who measured what

> Numbers are quoted from the cited source. 'measured_by' = whose run produced the number; 'source' = entry id where it is reported. Rows with different settings are NOT directly comparable; read the 'setting' column.

### RoboLab-120 (simulation, zero-shot, DROID-style arm)

| System | Model | Type | Success rate | Setting | Measured by | Source |
|---|---|---|---|---|---|---|
| AMP1 | frontier agent | frontier: agentic | **86.0%** | 2579 / 3000, 25 eps/task; leaderboard Score 93.5 | RoboLab leaderboard | [AMP1](#amp1) |
| AMP1 | frontier agent (best config) | frontier: agentic | **85.6%** | zero-shot | Apple (AMP1) | [AMP1](#amp1) |
| SOLVE + experience | GPT-6 Astra | frontier: direct | **84.5%** | 120 tasks × 5 episodes (600), no guides; first rollout without notes 79.8% | Li et al. (SOLVE) | [SOLVE](#solve) |
| Embo-Harness | GPT-6-Astra (xhigh) + VLA refinement | frontier: direct | **83.3%** | full RoboLab-120, zero-shot; Score 89.2; episodes per task not stated | Wu et al. (Embo-Harness) | [Embo-Harness](#embo-harness) |
| Astra — Agentic | GPT-6 Astra (Codex) | frontier: agentic | **74.8%** | 5 seeds/task | NVIDIA (Astranomy) | [Astranomy](#astranomy) |
| Astra — Orchestrated | GPT-6 Astra + Cosmos3-Nano-Policy | frontier over System 1 | **66.5%** | 5 seeds/task | NVIDIA (Astranomy) | [Astranomy](#astranomy) |
| Astra — Direct (EEF) | GPT-6 Astra | frontier: direct | **66.3%** | 5 seeds/task | NVIDIA (Astranomy) | [Astranomy](#astranomy) |
| SenseNova-RoboRSI | GPT-6-Astra (per Embo-Harness) | frontier: self-improving | **57.1%** | 685 / 1200, 10 eps/task; leaderboard Score 69.9 | RoboLab leaderboard | [Embo-Harness](#embo-harness) |
| Lakeside | LWM | learned System 1 | **51.0%** | 1531 / 3000, 25 eps/task; leaderboard Score 65.3; best learned policy on the board | RoboLab leaderboard | [RoboLab](#robolab) |
| π0.5 | VLA | learned System 1 | **49.2%** | leaderboard number cited by AMP1 | RoboLab leaderboard (via AMP1) | [AMP1](#amp1) |
| FLUX 3 Action | WAM | learned System 1 | **42.9%** | leaderboard number cited by AMP1 | RoboLab leaderboard (via AMP1) | [AMP1](#amp1) |
| Cosmos3-Nano-Policy | WAM (DROID-finetuned) | learned System 1 | **36.8%** | 5 seeds/task | NVIDIA (Astranomy) | [Astranomy](#astranomy) |
| π0.5 | VLA | learned System 1 | **28.0%** | 5 seeds/task | NVIDIA (Astranomy) | [Astranomy](#astranomy) |
| π0.5 | VLA | learned System 1 | **28.0%** | 336 / 1200, 10 eps/task; leaderboard Score 43.4 | RoboLab leaderboard | [RoboLab](#robolab) |

> π0.5 appears twice: 49.2% (leaderboard, cited by AMP1) vs 28.0% (Astranomy's own run). That 21-point gap on one benchmark is why every row says who measured it.

### RoboDojo (simulation, 42 tasks)

| System | Model | Type | Success rate / robodojo score | Setting | Measured by | Source |
|---|---|---|---|---|---|---|
| AMP1+ (after practice) | frontier agent + memory | frontier: agentic + memory | **84.1% SR** | few-shot practice, no weight updates | Apple (AMP1) | [AMP1](#amp1) |
| Mibot-RUA* | GPT-6 Astra (per adapter PR) | frontier: self-improving | **79.33% SR · Score 83.94** | official leaderboard agent track, Avg. (w/o Open); starred: task-specific briefs, skills, experience and scene priors beyond the official Detail Description | RoboDojo leaderboard (contributed by Xiaomi Robotics) | [Mibot-RUA](#mibot-rua) |
| SOLVE + experience | GPT-6 Astra (xhigh) | frontier: direct | **74.5% SR · Score 78.9** | official evaluation, seed 3, 2,100 episodes (50 per task); per-task rules distilled from rollouts; GPT-6.1 Sol 68.0% (2 seeds × 5 eps/task) | Li et al. (SOLVE) | [SOLVE](#solve) |
| Boundary-Aware Policy Learning | Claude Opus 5.5 (high) + boundary-trained π0.5 | frontier over System 1 | **69.2%** | 26 Generalization/Memory/Open-vocabulary tasks only, 10 episodes per task; Harness VLA (VPP2) 40.8% under the same subset | Fang et al. (Boundary-Aware) | [Boundary-Aware Policy Learning](#boundary-aware-policy) |
| Claude Fable 5.2 | Claude Fable 5.2 (Max effort) | frontier: model launch | **64.9% avg SR** | Anthropic's internal run, same harness for all models (undisclosed); highest available effort | Anthropic | [Claude Fable 5.2 (RoboDojo Sim)](#claude-fable-5-2) |
| X-Harness (model pool, Semi-online rescue) | Claude Opus 5.5 + GPT-6 Astra + Gemini 4 Argon over WALL-OSS-1.0-lite | frontier over System 1 | **62.2%** | Pure-RGB RoboDojo, 42 tasks × 20 layouts (seed 0), five-axis macro mean; code evolved on training layouts; WALL-OSS-1.0-lite official 35.0 | Lai et al. (X-Harness) | [X-Harness](#x-harness) |
| PhysEvo | Astra (frozen) | frontier: self-improving | **62.00% SR · Score 68.14** | held-out layouts; retained task-specific deployment versions; five-dimension weighting | Tian et al. | [PhysEvo](#physevo) |
| Next-Manip | GPT-6 Astra (medium) + Simate VLA, GPT-6 Luna allocator | frontier over System 1 | **59.58% SR · Score 67.88** | 12 representative tasks only (3 per Generalization/Precision/Long-Horizon/Memory), 20 trials per task; published standalone Astra 14.83% and Simate 38.56% on the same 12 tasks | Liu et al. (Next-Manip) | [Next-Manip](#next-manip) |
| ReWeave | GPT-6.1 Sol (xhigh) controller + frozen π0.5 | frontier: self-improving | **58.25% SR · Score 63.43** | 42 tasks, held-out seeds 1–10, native step limits; harness optimized on seed 0 (≤10 rounds per task); seed harness H0 25.50% | Xu et al. (ReWeave) | [ReWeave](#reweave) |
| UniCraft (frozen skills) | GPT-6 Astra (high effort, Codex harness) | frontier: self-improving code | **54.8% SR (115/210)** | zero-shot transfer of skills learned on other benchmarks; seed and layout 0, 42 tasks × 5 rollouts | Wang et al. (UniCraft) | [UniCraft](#unicraft) |
| AoG | GPT-6 Astra (xhigh) + frozen VPP2 WAM | frontier over System 1 | **50.57% SR · Score 57.26** | 42 tasks × 50 eps; harness frozen after 5 self-improvement rounds; world keeps running while the agent reasons | Cui et al. (AoG) | [Agent on Guard (AoG)](#agent-on-guard) |
| InteractVLA | VL agent + steerable VLA | frontier over System 1 | **48.62%** | with recursive self-improvement | Zhao et al. | [InteractVLA](#interactvla) |
| SEEK (10 attempts) | GPT-6 Astra (xhigh) | frontier: self-improving | **48.0% SR · Score 54.4** | 42 tasks, 50 evaluation episodes per task after 10 evolution attempts; no carryover 19.7% SR · 27.0 | Guan et al. (SEEK) | [SEEK](#seek) |
| Claude Opus 5.5 | Claude Opus 5.5 (Max effort) | frontier: model launch | **39.4% avg SR** | Anthropic's internal run, same harness for all models (undisclosed); highest available effort | Anthropic | [Claude Fable 5.2 (RoboDojo Sim)](#claude-fable-5-2) |
| Gemini 4 Argon | Gemini 4 Argon (High effort) | frontier: model launch | **34.2% avg SR** | Anthropic's internal run, same harness for all models (undisclosed); highest available effort | Anthropic | [Claude Fable 5.2 (RoboDojo Sim)](#claude-fable-5-2) |
| VPP2 (standalone) | world action model | learned System 1 | **32.26% SR · Score 39.26** | same protocol, AoG's baseline table | Cui et al. (AoG) | [Agent on Guard (AoG)](#agent-on-guard) |
| GPT-6 Astra | GPT-6 Astra (Max effort) | frontier: model launch | **29.8% avg SR** | Anthropic's internal run, same harness for all models (undisclosed); highest available effort | Anthropic | [Claude Fable 5.2 (RoboDojo Sim)](#claude-fable-5-2) |
| X-Harness (Offline) | Claude Opus 5.5 over π0.5 | frontier over System 1 | **28.1%** | 42 tasks, 2D detections only, 8 evolution rounds, 0 test-time VLM calls; π0.5 official 6.9 / rerun 9.6 | Lai et al. (X-Harness) | [X-Harness](#x-harness) |
| AMP1 (zero-shot) | frontier agent | frontier: agentic | **26.4% SR** | zero-shot | Apple (AMP1) | [AMP1](#amp1) |
| LLM as policy | GPT-6 Astra | frontier: direct | **22.48% SR · Score 28.97** | official 50 eps/task | Zhang et al. | [LLM as Policy on RoboDojo](#robodojo-astra) |
| LLM as policy | DeepSeek-Flash | frontier: direct | **1.92% SR** | 10 eps/task | Zhang et al. | [LLM as Policy on RoboDojo](#robodojo-astra) |
| LLM as policy | GPT-5.5 | frontier: direct | **0.88% SR** | official 50 eps/task | Zhang et al. | [LLM as Policy on RoboDojo](#robodojo-astra) |
| JustRUA | GPT-6 Astra | frontier: agentic (lean harness) | **Score 50.3** | no learned policy / self-improvement / task tuning; official L3 harness = 29.7 | Wang et al. | [JustRUA](#justrua) |
| uni-robot-agent | Qwen3.8-Flash-Next (open) | open model: agentic | **Score 31.39** | no privileged inputs | Yuan et al. | [uni-robot-agent](#democratizing-rua) |

> On the official leaderboard's agent track, Xiaomi Robotics' Mibot-RUA (GPT-6 Astra) leads at Avg. (w/o Open) 83.94 / 79.33% (added 2026-11-26), but RoboDojo stars it, like every other agent entry tested before its 2026-11-14 rules, for injecting task-specific information beyond the official Detail Description. The Astra direct-policy entry ranked above all 40 public policies at the time. See Critiques for leaderboard entries that did not survive retesting.

### LIBERO-PRO (perturbed LIBERO)

| System | Model | Type | Success rate | Setting | Measured by | Source |
|---|---|---|---|---|---|---|
| ASPIRE | Claude Opus 5.5 | frontier: self-improving code | **99%** | all 80 tasks; with skill learning | NVIDIA GEAR | [ASPIRE](#aspire) |
| AMP1 | frontier agent | frontier: agentic | **95.2%** | zero-shot via CaP-Gym (project page) | Apple (AMP1) | [AMP1](#amp1) |
| OpenRUA | Claude Code + Opus 5 | frontier: agentic | **87.0%** | zero-shot | Chu et al. | [OpenRUA](#openrua) |
| RACaP | GPT-5.6 ReAct | frontier: agentic | **45.0%** | zero-shot | Li et al. | [RACaP](#racap) |
| PEAR / RURL | open 27B, RL in sim | open model: direct | **57.4%** | new task in familiar scene (π0.5: 0.75%) | Tang et al. | [PEAR / RURL](#pear-rurl) |
| UniCraft | GPT-6 Astra (high effort, Codex harness) | frontier: self-improving code | **86.00%** | pooled unseen scenarios and tasks after 3 learning epochs (X-VLA 96.00 in the same table) | Wang et al. (UniCraft) | [UniCraft](#unicraft) |
| ScaleVLA | DeepSeek-V4.1-Flash 552B (frozen) + action DiT | VLA with frontier backbone | **45.1%** | mean of three perturbation settings, 500 episodes per setting; smaller backbones at most 31.3% | Yu et al. (ScaleVLA) | [ScaleVLA](#scalevla) |
| SCOPE | GLM-5.3-Flash | frontier: self-improving code | **80.66%** | 6 Object/Goal/Spatial Pos & Task settings, mean of 3 runs | Shu et al. (SCOPE) | [SCOPE](#scope-program-edits) |
| SPARK | Qwen3.8-27B (4-bit, open) | open model: agentic | **75.1%** | 6 Object/Goal/Spatial Pos & Task settings, 50 eps/task, no practice; benchmark success check read to trigger retries (67.5% without) | Grant et al. (SPARK) | [SPARK](#spark-bt) |
| Recursia (frozen stack) | coding agent (not specified for sim) | frontier: self-improving code | **28.4% Pos · 53.4% Task** | LIBERO-Pro Long only, 10 tasks × 50 seeds per axis, zero-shot transfer | Chen et al. (Recursia) | [Recursia](#recursia) |
| Real2Worlds2Real (136-skill library) | GPT-6 Astra | frontier: self-improving code | **82.2%** | LIBERO-Pro Long only, 20 tasks (10 position, 10 task perturbation) × 50 held-out initial states; 52.9% with no skills; mean over all candidate programs 69.1% | Gu et al. (Real2Worlds2Real) | [Real2Worlds2Real](#real2worlds2real) |
| X-Harness (Offline) | Claude Opus 5.5 over π0.5 | frontier over System 1 | **95.4%** | 40 tasks × 4 shifts pooled; code evolved on training initial states; π0.5 rerun 58.6 | Lai et al. (X-Harness) | [X-Harness](#x-harness) |
| RegHarness | DeepSeek-Flash (run time); skills refined by Claude Opus 5.5 | frontier: self-improving code | **87.8% (158/180)** | 60 Object/Goal/Spatial tasks × initial states 0–2; state 0 used for development; task check read during execution | Liu et al. (RegHarness) | [RegHarness](#regharness) |
| RATs (rerun) | DeepSeek-Flash | frontier: agentic | **39.4% (71/180)** | same 180 paired trials as RegHarness | Liu et al. (RegHarness) | [RegHarness](#regharness) |
| RoboEvo² (hybrid) | GPT-6 Astra coding agent + agent-trained π0.5 | frontier: self-improving | **90.5%** | all 8 settings, 100 eps each on unseen initial states, after co-evolution; standalone policy 84.1% | Liu et al. (RoboEvo²) | [RoboEvo²](#roboevo2) |
| MARGIN | Claude Opus 5.5 | frontier: self-improving code | **98.2%** | all 80 tasks, eight-category mean (six-category 99.1%); ASPIRE incumbents plus margin-refined programs; authors' ASPIRE reproduction 98.175% on 4,000 held-out episodes | Duan et al. (MARGIN) | [MARGIN](#margin) |
| ReWeave | GPT-6 Astra (low) controller + frozen π0.5; harness optimized by GPT-6.1 Sol | frontier: self-improving | **98.75%** | 80 tasks, held-out seeds 1–10; harness optimized on seed 0 (≤10 rounds per task); seed harness H0 89.00% | Xu et al. (ReWeave) | [ReWeave](#reweave) |
| Skeptic | Qwen3.8-27B (open, FP8) | frontier: self-improving | **78.3%** | all 80 tasks, held-out seeds (50 per task), mean of 2 campaigns; ASPIRE with the same model 63.4% | Sun et al. (Skeptic) | [Skeptic](#skeptic) |
| MFM-VLA | GPT-6 Astra + fine-tuned π0.5 | frontier over System 1 | **69.8%** | full LIBERO-PRO, 8,000 episodes (50 inits per task); base π0.5 54.9%; with Code Policy extension 84.4%; zero-shot GPT-6 Astra 3.5% | Zheng et al. (MFM-VLA) | [MFM-VLA](#mfm-vla) |

> Papers use different LIBERO-PRO conditions and subsets. Treat as indicative, not a single leaderboard.

### AA-Robotics (real 6-axis arm, 8 tasks, human-graded)

| System | Model | Type | Score / 100 | Setting | Measured by | Source |
|---|---|---|---|---|---|---|
| Codex | GPT-6 Astra | frontier: agentic | **69.4** | high effort | Artificial Analysis | [AA-Robotics](#aa-robotics) |
| Codex | GPT-6.1 Sol | frontier: agentic | **64.6** | high effort | Artificial Analysis | [AA-Robotics](#aa-robotics) |
| Antigravity + Robotics plugin | Gemini 4 Hydrogen | frontier: agentic | **58** | not stated | Google (launch post; not yet on AA's own page) | [Gemini 4 Hydrogen](#gemini-4-hydrogen) |
| Antigravity | Gemini 4 Argon | frontier: agentic | **55.3** | high effort | Artificial Analysis | [AA-Robotics](#aa-robotics) |
| Claude Code | Claude Opus 5.5 | frontier: agentic | **48.8** | high effort | Artificial Analysis | [AA-Robotics](#aa-robotics) |
| Claude Code | Claude Fable 5.1 | frontier: agentic | **46.3** | high effort | Artificial Analysis | [AA-Robotics](#aa-robotics) |
| not stated | GPT-6.2 Astra | frontier: agentic | **79** | not stated (AA's 2026-11-17 article; not yet on the AA-Robotics page) | Artificial Analysis | [AA-Robotics](#aa-robotics) |
| not stated | GPT-6.2 Sol | frontier: agentic | **78** | not stated (AA's 2026-11-17 article; not yet on the AA-Robotics page) | Artificial Analysis | [AA-Robotics](#aa-robotics) |
| not stated | Claude Fable 5.2 | frontier: agentic | **75** | not stated (AA's 2026-11-17 article; not yet on the AA-Robotics page) | Artificial Analysis | [AA-Robotics](#aa-robotics) |

> Independent third party, but no VLA baseline. AA's 2026-11-17 article puts GPT-6.2 Astra (79) on top, ahead of GPT-6.2 Sol (78) and Claude Fable 5.2 (75); those three scores give no harness or effort and are not yet on the AA-Robotics page.

### RoboDojo-RC Tier 1 (real bimanual YAM, 6 tasks × 20 trials, human-graded)

| System | Model | Type | Mean progress score | Setting | Measured by | Source |
|---|---|---|---|---|---|---|
| Codex | GPT-6.2 Astra (ultrafast) | frontier: agentic | **97.3%** | Codex harness (self-written tools, several moves per turn), no call cap, 20-min limit · $9.46 (estimate) · 5.6 min | Robocurve | [Astra on Codex (Robocurve)](#codex-vs-inspect-robots) |
| Antigravity | Gemini 4 Neon (high) | frontier: agentic | **89.7%** | coding agent, no call cap, 60-min limit · $5.46 (estimate) · 37.5 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Claude Code | Claude Fable 5.2 (high, fast) | frontier: agentic | **89.0%** | coding agent, no call cap, 20-min limit · $12.08 (recorded) · 9.7 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Waddle-1 | undisclosed cloud LLMs + local policies | frontier over System 1 | **81.4%** | full system, no call cap, 10-min limit · $2.46 · 7.4 min | Robocurve | [Waddle-1](#waddle-1) |
| Inspect Robots agent | GPT-6.2 Astra (high, ultrafast) | frontier: direct | **65.7%** | 40 calls · $10.51 · 2.7 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Dream-1 (Dream Labs) | world action model (hosted API) | learned System 1 | **59.5%** | 3,600 steps · $0.15 · 1.5 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Inspect Robots agent | Claude Fable 5.2 (high, fast) | frontier: direct | **57.5%** | 40 calls · $5.93 · 4.5 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Inspect Robots agent | Gemini 4 Carbon (high) | frontier: direct | **54.5%** | 40 calls · $2.16 · 32.1 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Inspect Robots agent | Gemini 4 Argon (high, priority) | frontier: direct | **48.2%** | 40 calls · $2.34 · 20.5 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Inspect Robots agent | GPT-6 Astra (high, fast) | frontier: direct | **42.5%** | 40 calls · $3.48 · 4.0 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Inspect Robots agent | GPT-6.1 Sol (high, fast) | frontier: direct | **41.7%** | 40 calls · $2.15 · 4.0 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Inspect Robots agent | Claude Opus 5.5 (high, fast) | frontier: direct | **38.2%** | 40 calls · $2.23 · 3.1 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Inspect Robots agent | GPT-6 Astra (medium) | frontier: direct | **36.7%** | 40 calls · $1.14 · 4.2 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Inspect Robots agent | Gemini 3.8 Flash (high) | frontier: direct | **36.2%** | 40 calls · $0.66 · 7.2 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Inspect Robots agent | Claude Opus 5.5 (medium) | frontier: direct | **36.0%** | 40 calls · $0.90 · 4.5 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Inspect Robots agent | GPT-6 Sol (high, fast) | frontier: direct | **22.0%** | 40 calls · $0.95 · 3.7 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| MolmoAct2 | open VLA | learned System 1 | **19.5%** | 3,600 steps · $0.07 (GPU rental) · 0.8 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| Inspect Robots agent | GPT-5.6 Sol (high, fast) | frontier: direct | **14.9%** | 40 calls · $1.77 · 3.6 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |
| GR00T N1.7 | open VLA | learned System 1 | **9.5%** | 3,600 steps · $0.05 (GPU rental) · 0.9 min | Robocurve | [RoboDojo-RC Tier 1](#robodojo-rc-tier1) |

> Frontier LLMs, coding agents, a full agent system and learned VLAs/WAMs on one rig, all measured by Robocurve. Setting = call or step cap · cost per attempt · wall-clock per attempt. Graders were not blinded. Caps are not like-for-like: plain LLMs get 40 calls, while coding agents (Codex, Claude Code, Antigravity) and Waddle-1 run with no call cap under 20-, 60- and 10-minute limits. Harness matters: the same GPT-6.2 Astra scores 97.3% through Codex vs 65.7% through Robocurve's 40-call Inspect Robots harness; all three coding agents (89.0–97.3%) top Waddle-1 (81.4%). Robocurve is retiring RoboDojo from future evaluations.

### LIBERO-10 (direct EEF control via tool calls)

| System | Model | Type | Success rate | Setting | Measured by | Source |
|---|---|---|---|---|---|---|
| direct EEF | GPT-6 Astra | frontier: direct | **44%** | best effort level | Espinola et al. | [Frontier models on LIBERO-10](#libero10-frontier) |
| direct EEF | Gemini-4 Argon | frontier: direct | **43%** | best effort level | Espinola et al. | [Frontier models on LIBERO-10](#libero10-frontier) |

> 6 models × 3 effort levels, 1,800 episodes total; only the top two are quoted in the abstract.

### Real-world head-to-heads

| System | Model | Type | Successes / trials | Setting | Measured by | Source |
|---|---|---|---|---|---|---|
| AMP1 | Claude Opus 5.5 (main) | frontier: agentic | **104 / 108** | 12 tasks × 3 robots | Apple (AMP1) | [AMP1](#amp1) |
| FLUX 3 Action | WAM | learned System 1 | **49 / 108** | same tasks | Apple (AMP1) | [AMP1](#amp1) |
| π0.5 | VLA | learned System 1 | **30 / 108** | same tasks | Apple (AMP1) | [AMP1](#amp1) |
| ACE-CaP-0 (frozen programs) | coding agent at dev time only | frontier-developed code | **221 / 240** | 8 tasks; no model in loop at runtime | ACE-CaP Team | [ACE-CaP-0](#ace-cap-0) |
| Reins | GPT-6.1 Sol | frontier: agentic | **88% of episodes** | 5 long-horizon dual-arm tasks | Ye et al. | [Reins](#reins) |
| PEAR / RURL | open 27B, RL in sim | open model: direct | **60% of trials** | real dual-arm; base model 0% | Tang et al. | [PEAR / RURL](#pear-rurl) |
| Inspect Robots agent | GPT-6 Astra | frontier: agentic | **19 / 20 bowl · 2 / 20 puzzle** | bimanual YAM; unblinded graders | Robocurve | [Robocurve Astra eval](#robocurve-astra) |
| GTA-2 | Gemini 3.1 Pro | frontier: agentic | **73.9% avg** | 14 tasks, zero-shot; vs π0.5 + CaP baselines (best baseline 31.4 pp lower) | Seker et al. | [GTA-2](#gta-2) |
| ForceHarness | GPT-6 Astra | frontier: agentic | **54 / 60** | Franka FR3, 6 contact tasks × 10; operator-judged | Sun et al. | [ForceHarness](#forceharness) |
| ForceHarness | GPT-6.1 Sol | frontier: agentic | **47 / 60** | same tasks | Sun et al. | [ForceHarness](#forceharness) |
| Same harness, no force | GPT-6 Astra | frontier: agentic | **2 / 60** | same tasks | Sun et al. | [ForceHarness](#forceharness) |
| LEXP | GPT-6 Astra | frontier: direct + experience | **23 / 36** | bimanual YAM, 12 tasks × 3; human-annotated; vanilla Astra 2 / 36 | Zeng et al. | [LEXP](#lexp) |
| RoC | frontier agent over FastWAM | frontier over System 1 | **73.3% avg** | SO-ARM101, 3 tasks × 10; FastWAM alone 30.0% | Cen et al. | [RoC](#reasoning-on-call) |
| SCOPE (frozen programs) | GLM-5.3-Flash | frontier: self-improving code | **40 / 60** | Quanta X2, 3 tasks × 20 held-out placements; ASPIRE 24 / 60 | Shu et al. (SCOPE) | [SCOPE](#scope-program-edits) |
| HuGo | gpt-5.4 over frozen whole-body policy | frontier over System 1 | **93.3% PBT · 66.7% LBX** | Unitree G1, best policy per task, zero-shot sim-to-real, 15 trials each | Choi et al. (HuGo) | [HuGo](#hugo) |
| Embo-Harness | GPT-6-Astra | frontier: direct | **15/20** | Franka FR3, 4 tasks x 5 zero-shot trials (block stacking 5/5, fruit packing 5/5, dish washing 2/5, flower arranging 3/5); paper's baseline harness 7/20 | Wu et al. (Embo-Harness) | [Embo-Harness](#embo-harness) |
| Contact Harness | GPT-6 Astra (high) | frontier: direct | **136/150 (90.7%)** | Rokae arm, connector insertion, 15 connector types x 10 trials, full insertion to mechanical limit, zero-shot | Shan et al. (Contact Harness) | [Contact Harness](#contact-harness) |
| TRIP + π0.5 | GPT-6.1-sol (medium) + Qwen3.5-9B tripwire VLM | frontier over System 1 | **25/40** | xArm 7, mug + towel hanging, 10 setups each, 'block' and 'move target' human disturbances; turn-based agentic harness 5/40, π0.5 alone 1/40; contact = failure | Chen et al. (TRIP) | [TRIP (Tripwire)](#trip-tripwire) |
| Embodied-Harness | GPT-6 Astra | frontier: direct + self-improving harness | **96.7% avg** | Piper arm, 3 tasks × 10 episodes; π0.5 40.0% on same tasks | Fan et al. (Embodied-Harness) | [Embodied-Harness](#embodied-harness) |
| EvoTER (real-world evolved) | gpt-6.1-sol over frozen π0.5-based policy + Tether | frontier over System 1 | **4/5 · 5/5 · 5/5** | Franka, table setting · drawer storage · two-cup hanging, 5 trials each; direct transfer of sim library 1/5 each | Zhou et al. (EvoTER) | [EvoTER](#evoter) |
| DualManip | GPT-5.6 Terra + shape-adaptive correspondence net | frontier over System 1 | **53.3%** | KUKA iiwa, 3 general tasks under continuous scene change, 15 trials each (CLEA agentic VLM replanning 0.0%, ReKep 28.9%) | Li et al. | [DualManip](#dualmanip) |
| RegHarness | DeepSeek-Flash | frontier: self-improving code | **28 / 45** | Kinova Gen3, 3 tasks × 15; RATs 21 / 45; difference not significant | Liu et al. (RegHarness) | [RegHarness](#regharness) |
| RoboEvo² (hybrid) | GPT-6 Astra harness + agent-trained π0.5 | frontier: self-improving | **95.0%** | Unitree G1-D, 4 tasks × 10; standalone policy (120 auto-collected demos) 85.0% vs π0.5 on 200 teleop demos 80.0% | Liu et al. (RoboEvo²) | [RoboEvo²](#roboevo2) |
| Next-Manip | GPT-6 Astra (medium) + fine-tuned π0.5 | frontier over System 1 | **77.50%** | xArm7, 4 tasks × 20 trials, operator labels; average success rate | Liu et al. (Next-Manip) | [Next-Manip](#next-manip) |
| π0.5 (policy only) | VLA | learned System 1 | **28.75%** | same tasks and layouts as Next-Manip | Liu et al. (Next-Manip) | [Next-Manip](#next-manip) |
| GPT-6-Astra agent (100% control) | GPT-6 Astra | frontier: direct | **89.3%** | AgileX Piper, 3 tasks × 50 trials (average success) | Li et al. (JiL) | [JiL (Judgment-in-the-Loop)](#jil-wam-calibration) |
| JiL System 1 & 2 | GPT-6 Astra over Fast-WAM (30% agent calls) | frontier over System 1 | **82.0%** | same tasks; 86.0% over LingBot-VA | Li et al. (JiL) | [JiL (Judgment-in-the-Loop)](#jil-wam-calibration) |
| Fast-WAM (base) | WAM | learned System 1 | **44.0%** | same tasks; LingBot-VA base 50.7% | Li et al. (JiL) | [JiL (Judgment-in-the-Loop)](#jil-wam-calibration) |
| SOLVE | GPT-6 Astra | frontier: direct | **75 / 85** | UR12e, 16 zero-shot tasks, 5 episodes per task (10 for shirt folding) | Li et al. (SOLVE) | [SOLVE](#solve) |
| SEEK (5 attempts) | GPT-6 Astra (xhigh) | frontier: self-improving | **83.3 avg score** | Franka Panda, 4 tasks × 10 unseen episodes, operator-scored 0–100; GPT-6 Astra acting directly 66.9 | Guan et al. (SEEK) | [SEEK](#seek) |
| RESET (frozen code) | Claude Opus 5.5 (Claude Code) at practice time only | frontier: self-improving | **223 / 280** | 4 robots, 10 trials per task; fixed-base 210 / 240; Unitree G1 13 / 40; no runtime LLM calls | Sun et al. (RESET) | [RESET](#reset-one-demo) |
| MFM-VLA | GPT-6 Astra + fine-tuned π0.5 | frontier over System 1 | **31.7% multi-stage · 54.4% atomic** | 11 glassware tasks, 20 trials per setting; base π0.5 0.8% / 15.3% | Zheng et al. (MFM-VLA) | [MFM-VLA](#mfm-vla) |

### ⏱️ The speed gap (the open problem)

| System | Rate / latency | Cost | Source |
|---|---|---|---|
| Helix System 1 | 200 Hz | onboard | [Helix](#helix) |
| GR00T N1 action module | ≈120 Hz | onboard | [GR00T N1](#gr00t-n1) |
| Fast-in-Slow | 117.7 Hz | onboard | [Fast-in-Slow](#fast-in-slow) |
| DASH System 1 | 20 Hz, independent of 0.8B–8B backbone | onboard | [DASH](#dash) |
| π0.5 | 46.96 ms / call | — | [Astranomy](#astranomy) |
| Cosmos3-Nano-Policy | 713.76 ms / call | — | [Astranomy](#astranomy) |
| Claude models (non-reasoning) | ≈0.2–0.4 Hz | — | [Claude on robotics](#anthropic-robotics) |
| GPT-6 Astra — Direct | 18.56 s / call | $1.96 / episode | [Astranomy](#astranomy) |
| GPT-6 Astra — Orchestrated | 11.50 s / 2.74 s (as listed) | $17.72 / episode | [Astranomy](#astranomy) |
| GPT-6 Astra — Agentic | 13.37 s | $36.40 / episode | [Astranomy](#astranomy) |
| GPT-6 Astra (Robocurve bowl) | ≈2.5 min / run | $0.94 / run | [Robocurve Astra eval](#robocurve-astra) |
| AA-Robotics agents | ≈30 min / task (human ≈20 s) | ≈10× human hourly wage | [AA-Robotics](#aa-robotics) |
| RACaP distilled (Qwen3-VL-8B) | 13.2× faster per decision than GPT-5.6 teacher | — | [RACaP](#racap) |
| ACE-CaP-0 frozen programs | 0.97–2.27 min / task, zero model calls | dev-time only | [ACE-CaP-0](#ace-cap-0) |
| H2E distilled VLA | 3.7× faster than agent + VLA | zero LLM tokens | [H2E](#h2e) |
| GPT-6 Astra direct control | median 31.9 s per decision (π0.5: 0.11 s) | API | [AgentRoboCritic](#agentrobocritic) |

<a id="at-a-glance"></a>
## 🗂️ At a glance: what sits below the frontier model?

| Work | Date | Frontier model | Role | Below it | Eval | Judged by |
|---|---|---|---|---|---|---|
| [Mibot-RUA](#mibot-rua) | 2026-11-26 | GPT-6 Astra | self-improving | none | sim | RoboDojo simulator checker (official leaderboard) |
| [X-Harness](#x-harness) | 2026-11-25 | Claude Opus 5.5, Claude Sonnet 5.5, GPT-6 Astra, Gemini 4 Argon, Gemini 3.8 Flash, Gemini 3.5 Flash-Lite | orchestrator | frozen learned policy | sim+real | each benchmark's own success check (sim); real: replay on held-out recordings plus live chunk checks |
| [RegHarness](#regharness) | 2026-11-25 | DeepSeek-Flash (provider alias deepseek-flash), Claude Opus 5.5 | agentic / code | analytic (IK / waypoints / scripted) | sim+real | benchmark task check (LIBERO-PRO / MolmoSpaces), also read by the controller during execution; real: operator on site |
| [RoboEvo²](#roboevo2) | 2026-11-25 | GPT-6 Astra, Qwen3.8-27B | self-improving | trained by the agent | sim+real | task-level success check (simulator) for selecting training data and for evaluation; real-world judge not stated |
| [SOLVE](#solve) | 2026-11-25 | GPT-6 Astra, GPT-6.1 Sol, Gemini 4 Argon | direct | analytic (IK / waypoints / scripted) | sim+real | RoboDojo / RoboLab simulator checkers; real-robot judge not stated |
| [SEEK](#seek) | 2026-11-25 | GPT-6 Astra, GPT-6.2 Astra, Claude Opus 5.5 | self-improving | analytic (IK / waypoints / scripted) | sim+real | RoboDojo task score and strict SR; real robot: operator scores each episode with predefined rules |
| [Skeptic](#skeptic) | 2026-11-25 | Qwen3.8-27B | self-improving | analytic (IK / waypoints / scripted) | sim | simulator task-completion predicate; skill admission also checks an independent verifier agent |
| [MARGIN](#margin) | 2026-11-24 | Claude Opus 5.5 | self-improving | analytic (IK / waypoints / scripted) | sim | benchmark success check (LIBERO-Pro / LIBERO-90 / Robosuite) on held-out and fresh seeds; acceptance uses development seeds only |
| [Next-Manip](#next-manip) | 2026-11-24 | GPT-6 Astra (medium), GPT-6 Luna (Decisions API, classifier) | orchestrator | frozen learned policy | sim+real | benchmark native success criteria (sim); real: recorded operator labels |
| [Atomic Policy](#atomic-policy) | 2026-11-24 | gpt-6-astra, gemini-3.8-flash, claude-opus-5.5, gemini-2.5-flash, Qwen3-VL-235B | orchestrator | frozen learned policy | sim+real | benchmark success checks (sim); real: task score from completed grasp/place steps (scorer not stated) |
| [Boundary-Aware Policy Learning](#boundary-aware-policy) | 2026-11-24 | Claude Opus 5.5, GPT-6.1 Sol, GPT-6 Astra, Kimi K3.1 Pro, DeepSeek-V4.1-Flash, GPT-6.1 Terra (data collection) | orchestrator | frozen learned policy | sim+real | benchmark success checks (RoboTwin 2.0, RoboDojo official implementation); real: single qualitative episode |
| [SkillHarness](#skillharness) | 2026-11-24 | DeepSeek V4.1 Flash (non-thinking), Gemma 4 E2B (local monitor) | orchestrator | frozen learned policy | sim+real | route success criteria (clear all obstacles in order, permitted contacts only, stop within tolerance before deadline); scorer not stated |
| [Weight-Space Programming for RFMs](#wsp-robot-repair) | 2026-11-24 | Claude Opus 5.5 | self-improving | trained by the agent | sim | simulator success on new seeded scenes against a pass mark set in advance; failures identified from the simulator's exact measurements |
| [RESET](#reset-one-demo) | 2026-11-24 | Claude Opus 5.5 (Claude Code), GPT-6 Astra (asset rebuild) | self-improving | analytic (IK / waypoints / scripted) | sim+real | read-only scorer derived from the demonstrated final state (criterion confirmed once per task by a person); real-robot judge not stated |
| [Embo-Harness](#embo-harness) | 2026-11-23 | GPT-6-Astra, GPT-6.1-Sol, GPT-6.1-Terra | direct | analytic (IK / waypoints / scripted) | sim+real | RoboLab-120 SR/Score metrics (sim); real-world judge not stated |
| [ACAP](#acap) | 2026-11-23 | Astra (lead xhigh, members medium; paper does not give the full model name) | agentic / code | analytic (IK / waypoints / scripted) | real | human annotators with task-specific rubrics (physical progress, completion); operators monitor safety |
| [Real2Worlds2Real](#real2worlds2real) | 2026-11-23 | GPT-6 Astra | self-improving | trained by the agent | sim+real | real: not stated; LIBERO-Pro: benchmark checker on 50 held-out initial states |
| [RoboHarness-Zero](#roboharness-zero) | 2026-11-23 | GPT-6 Astra, GPT-6.1 Sol | orchestrator | frozen learned policy | sim | RoboCasa365 environment success predicate |
| [Agent on Guard (AoG)](#agent-on-guard) | 2026-11-23 | GPT-6 Astra, GPT-6.1 Sol | orchestrator | frozen learned policy | sim+real | benchmark success criteria and Score (RoboDojo-Sim, RoboCasa365); real: full task completion without human intervention (judge not named) |
| [EvoMisty](#evomisty) | 2026-11-23 | Claude Opus 5.5, GPT-6 Astra | agentic / code | analytic (IK / waypoints / scripted) | real | agent-written automatic checks plus human checks for anything seen or heard; optimisation metrics measured by the authors on held-out data |
| [ReWeave](#reweave) | 2026-11-23 | GPT-6 Astra (low), GPT-6.1 Sol (xhigh), GPT-6.1 Terra (high), Claude Sonnet 5.5, DeepSeek V4.1 Flash | self-improving | frozen learned policy | sim+real | official benchmark success labels (sim); real: on-site operator using physical endpoint criteria |
| [JiL (Judgment-in-the-Loop)](#jil-wam-calibration) | 2026-11-23 | GPT-6 Astra | orchestrator | frozen learned policy | sim+real | benchmark success checks (RoboTwin 2.0, LIBERO-Plus); real-world scorer not stated |
| [MFM-VLA](#mfm-vla) | 2026-11-23 | GPT-6 Astra | orchestrator | jointly trained | sim+real | benchmark environments in sim; real-world judge not stated |
| [Contact Harness](#contact-harness) | 2026-11-22 | GPT-6 Astra, Claude Fable 5.1, Claude Fable 5.2 | direct | analytic (IK / waypoints / scripted) | sim+real | task-specific success criteria (real: insertion counts only at the mechanical limit; judge not named); sim: task checks, Write judged by a person (VLA Write runs judged by GPT-6 Astra) |
| [Waddle-1](#waddle-1) | 2026-11-20 | a set of cloud LLMs (not named) | orchestrator | frozen learned policy | real | Robocurve human grader (not blinded) |
| [TRIP (Tripwire)](#trip-tripwire) | 2026-11-20 | GPT-6.1-sol, GPT-6 Astra, Claude Opus 5.5, Qwen3.5-9B (tripwire VLM) | orchestrator | frozen learned policy | sim+real | RoboCasa365 task check + geometric capsule-box human-contact check (sim); task outcome with no contact with the person (real) |
| [NavRSI](#navrsi) | 2026-11-20 | GPT-6-Astra, GPT-6-Luna, GPT-5.6-Sol, GPT-6.1-Terra, GPT-6.1-Sol, GPT-6.2-Sol, GPT-6.2-Astra, Claude Sonnet-5, Claude Opus-5, Claude Opus-5.5, Claude Fable-5, Claude Fable-5.2, Gemini-3.8-Flash, Gemini-4-Hydrogen, Qwen3.7-Flash, Qwen3.8-Flash, Qwen3.8-27B | self-improving | none | sim+real | VLN-CE standard metrics in simulator (NE/OSR/SR/SPL); real-world judging not stated |
| [Embodied-Harness](#embodied-harness) | 2026-11-20 | GPT-6 Astra | self-improving | analytic (IK / waypoints / scripted) | sim+real | benchmark success checks (RoboTwin 2.0, RoboSPA, RMBench); real-world judging not stated |
| [EvoTER](#evoter) | 2026-11-20 | gpt-6.1-sol | self-improving | frozen learned policy | sim+real | 'externally evaluated task outcome' (RoboCasa365 checker in sim); real-world judge not stated |
| [EmbodyAgent](#embodyagent) | 2026-11-19 | Astra Medium (black-box teacher), Qwen3.5-9B (student) | agentic / code | none | sim | LIBERO BDDL success predicate |
| [RoC](#reasoning-on-call) | 2026-11-19 | GPT-6.1 Sol (xhigh), FastWAM (low-level) | orchestrator | frozen learned policy | sim+real | — |
| [UniCraft](#unicraft) | 2026-11-19 | GPT-6 Astra, Gemini 3.8 Flash, DeepSeek-V4.1-Flash, transfer: GPT-6.1 Sol, GPT-6.1 Terra, MiniMax M3.1 Flash | self-improving | analytic (IK / waypoints / scripted) | sim | native benchmark success checks |
| [InteractVLA](#interactvla) | 2026-11-17 | vision-language agent | orchestrator | frozen learned policy | sim | benchmark checkers |
| [Gemini 4 Hydrogen](#gemini-4-hydrogen) | 2026-11-17 | Gemini 4 Hydrogen (gemini-4-hydrogen) | agentic / code | — | real | — |
| [ForceHarness](#forceharness) | 2026-11-16 | GPT-6 Astra, GPT-6.1 Sol, Claude Fable 5.2 | agentic / code | analytic (IK / waypoints / scripted) | sim+real | human operator (real); ForceBench public evaluator; HiddenPhys code check on final state |
| [ATLAS](#atlas) | 2026-11-13 | VLM agent (unnamed on page) | orchestrator | frozen learned policy | sim+real | authors |
| [PEAR / RURL](#pear-rurl) | 2026-11-13 | open-weight 27B reasoning model (RL-trained) | direct | analytic (IK / waypoints / scripted) | sim+real | — |
| [Reins](#reins) | 2026-11-12 | GPT-6.1 Sol, GPT-6 Astra, Claude Opus 5.5 | agentic / code | analytic (IK / waypoints / scripted) | real | — |
| [ACE-CaP-0](#ace-cap-0) | 2026-11-12 | coding agent (development time only) | self-improving | analytic (IK / waypoints / scripted) | real | — |
| [H2E](#h2e) | 2026-11-12 | LLM planner (teacher) + 8B VLA (student) | self-improving | trained by the agent | sim | benchmark |
| [AMP1](#amp1) | 2026-11-06 | Claude Opus 5.5 (main real-world), Gemini 4 Argon, 13 models incl. 6 open-weight | agentic / code | analytic (IK / waypoints / scripted) | sim+real | benchmark checkers (sim); experimenters (real) |
| [DiMuRe](#dimure) | 2026-11-03 | DeepSeek V4.1 Flash (terminal replanning) | agentic / code | analytic (IK / waypoints / scripted) | sim | LIBERO-Disturb task checks |
| [uni-robot-agent](#democratizing-rua) | 2026-11-01 | Qwen3.8-Flash-Next (open-weight) | agentic / code | analytic (IK / waypoints / scripted) | sim+real | — |
| [LEXP](#lexp) | 2026-10-30 | GPT-6 Astra, Opus 5.5, Sol 5.6 | self-improving | none | real | human annotation against predefined completion criteria, independent of the actor's own declaration |
| [Frontier models on LIBERO-10](#libero10-frontier) | 2026-10-21 | GPT-6 Astra, GPT-6.1 Sol, GPT-6 Luna, Claude Opus 5, Claude Opus 5.5, Gemini-4 Argon | direct | analytic (IK / waypoints / scripted) | sim | LIBERO checker |
| [Astra as visuo-tactile policy](#astra-visuotactile) | 2026-10-19 | GPT-6 Astra (xhigh) | direct | none | sim | simulator checker (official success criteria; one task's criterion relaxed) |
| [Bitter Lesson → Robotics](#bitter-lesson-robotics) | 2026-10-18 | 9 frontier multimodal LMs at multiple effort / service tiers | direct | analytic (IK / waypoints / scripted) | real | — |
| [Recursia](#recursia) | 2026-10-17 | GPT-6 Astra (physical runs), Claude Opus 5.5 (low effort, verifier calls) | self-improving | analytic (IK / waypoints / scripted) | sim+real | official LIBERO-Pro evaluator (sim); manual assessment (real) |
| [SCOPE](#scope-program-edits) | 2026-10-16 | GLM-5.3-Flash (local) | self-improving | analytic (IK / waypoints / scripted) | sim+real | benchmark checkers (sim); held-out physical placements (real) |
| [Astranomy](#astranomy) | 2026-10-14 | GPT-6 Astra | direct | analytic (IK / waypoints / scripted) | sim | RoboLab task checkers |
| [SEAR](#sear) | 2026-10-13 | 7 frontier LMs | self-improving | trained by the agent | sim+real | benchmark with controls |
| [ReTrace](#retrace) | 2026-10-11 | GPT-6 Astra (high, learner), GPT-6 Astra-low, GPT-6 Sol-xhigh | self-improving | none | real | — |
| [PhysEvo](#physevo) | 2026-10-06 | Astra (frozen; task agent and meta-agent) | self-improving | none | sim+real | RoboDojo native evaluator (sim); authors' rubric (real) |
| [OpenRUA](#openrua) | 2026-10-01 | Claude Code + Claude Opus 5 | agentic / code | analytic (IK / waypoints / scripted) | sim | benchmark checkers |
| [Real2Gym](#real2gym) | 2026-09-29 | GPT-6 Astra (medium reasoning), baselines: GPT-6 Astra Direct Mode, GPT-5.6 Sol xhigh | self-improving | analytic (IK / waypoints / scripted) | sim+real | predefined completion criteria and human inspection |
| [DualManip](#dualmanip) | 2026-09-25 | GPT-5.6 Terra, Qwen3.5-2B | orchestrator | frozen learned policy | real | not stated (success counts per task) |
| [RAPID](#rapid) | 2026-09-24 | coding agent | agentic / code | analytic (IK / waypoints / scripted) | sim+real | — |
| [HarnessPAI](#harnesspai) | 2026-09-24 | — | orchestrator | frozen learned policy | sim+real | — |
| [RACaP](#racap) | 2026-09-24 | GPT-5.6 (teacher), Qwen3-VL-8B-Instruct (distilled) | self-improving | analytic (IK / waypoints / scripted) | sim | benchmark checkers |
| [HuGo](#hugo) | 2026-09-24 | gpt-5.4 | orchestrator | frozen learned policy | sim+real | simulator task checks; hardware trials on a Unitree G1 |
| [LLM as Policy on RoboDojo](#robodojo-astra) | 2026-09-21 | GPT-6 Astra, GPT-5.5, DeepSeek-Flash | direct | analytic (IK / waypoints / scripted) | sim | RoboDojo checker |
| [AquaCap](#aquacap) | 2026-09-19 | DeepSeek-V4-Pro (policy), DeepSeek-V4-Flash (coding), Qwen3.7-Flash (VLM) | agentic / code | analytic (IK / waypoints / scripted) | sim+real | task-specific success criterion (lift held, transport within distance) |
| [GPT-Policy](#gpt-policy) | 2026-09-16 | GPT-6 Astra and others | self-improving | analytic (IK / waypoints / scripted) | real | — |
| [AGP](#agent-as-policy) | 2026-09-11 | general-purpose agent | agentic / code | analytic (IK / waypoints / scripted) | real | authors |
| [Show-Harness](#show-harness) | 2026-09-09 | closed frontier VLMs, small open VLMs (fine-tuned) | direct | analytic (IK / waypoints / scripted) | sim+real | — |
| [GTA-2](#gta-2) | 2026-09-09 | Gemini 3.1 Pro (all agents) | agentic / code | analytic (IK / waypoints / scripted) | real | authors |
| [EMERGE-Policy](#emerge-policy) | 2026-08-30 | — | orchestrator | frozen learned policy | sim+real | — |
| [Push-T, revisited](#push-t-agentic) | 2026-08-18 | Claude Code with Fable 5 | agentic / code | analytic (IK / waypoints / scripted) | sim | gym_pusht coverage threshold (simulator checker) |
| [Gemini Robotics 2](#gemini-robotics-2) | 2026-07-30 | Gemini Robotics ER 2, Gemini Robotics 2 (VLA), Gemini Robotics On-Device 2 | orchestrator | jointly trained | real | — |
| [STeP](#step-stl) | 2026-07-20 | GPT-5.4 | agentic / code | analytic (IK / waypoints / scripted) | sim+real | simulator checker (LIBERO / LIBERO-PRO); not stated (real) |
| [Harness VLA](#harness-vla) | 2026-07-09 | LLM coding agent | orchestrator | frozen learned policy | sim+real | benchmark checkers |
| [Claude on robotics](#anthropic-robotics) | 2026-07-09 | Claude Mythos Preview, Opus 4.5–4.7, GPT-5.4, Gemini 3.1 Pro, Kimi K2.6, Qwen 3.6+ | direct | frozen learned policy | sim+real | simulator; informal real Go2 runs |
| [ASPIRE](#aspire) | 2026-06-30 | Claude Opus 5.5 (best), other frontier models | self-improving | analytic (IK / waypoints / scripted) | sim+real | benchmark checkers |
| [SPARK](#spark-bt) | 2026-06-29 | Qwen3.8-27B (4-bit, local; sim main table), Gemini 3.5 Flash (hardware), gemini-3.1-pro-preview (ablation) | agentic / code | analytic (IK / waypoints / scripted) | sim+real | benchmark checkers (sim); hardware trials |
| [InSight](#insight-steerable-vla) | 2026-06-23 | Gemini 3 Flash | self-improving | trained by the agent | sim+real | ground-truth state (sim); human against binary criteria (real); VLM filters acquisition rollouts |
| [ENPIRE](#enpire) | 2026-06-18 | frontier coding agents | self-improving | trained by the agent | real | automatic verifier |
| [BiCICLe](#bicicle) | 2026-04-22 | GPT-5-mini (gpt-5-mini-2025-08-07), Qwen 2.5 7B (replication) | direct | analytic (IK / waypoints / scripted) | sim+real | TWIN simulator checker (sim); not stated (real) |
| [CoEnv / CoEx](#coenv-coex) | 2026-04-07 | Claude Code (code agent), GPT-5.6 Sol (planner) | agentic / code | analytic (IK / waypoints / scripted) | sim+real | twin verifier (privileged state) during exploration; task milestones on the real robots |
| [CaP-X](#cap-x) | 2026-03-23 | 12 models incl. Gemini 3 Pro, GPT-5.2, Claude Opus 4.5 | agentic / code | analytic (IK / waypoints / scripted) | sim+real | benchmark checkers |
| [NovaPlan](#novaplan) | 2026-02-23 | GPT-5.2 | orchestrator | analytic (IK / waypoints / scripted) | real | human |
| [UniManip](#unimanip) | 2026-02-13 | Qwen3-VL-4B | agentic / code | analytic (IK / waypoints / scripted) | sim+real | benchmark checkers (sim); trial success criterion on hardware (object in receptacle, no e-stop or intervention) |
| [FAEA](#faea) | 2026-01-28 | Claude Agent SDK (unmodified) | agentic / code | analytic (IK / waypoints / scripted) | sim | benchmark checkers |
| [ALRM](#alrm) | 2026-01-27 | 10 LLMs; best closed: Claude-4.1-Opus; best open: Falcon-H1-7B | agentic / code | analytic (IK / waypoints / scripted) | sim | benchmark checkers |
| [Gemini Robotics 1.5](#gemini-robotics-1-5) | 2025-10-02 | Gemini Robotics-ER 1.5 (orchestrator), Gemini Robotics 1.5 (VLA) | orchestrator | jointly trained | real | — |

<a id="direct"></a>
## 🎯 Frontier Model as Direct Policy

*The general-purpose model itself emits the next action (end-effector pose, joint target, trajectory) at every step. No learned System 1 underneath; the only thing below it is IK / a position controller.*

<details open><summary><b>11 entries</b> + 18 cross-listed</summary>

<a id="solve"></a>
- **[SOLVE: Sparse, Ordered Keyposes Make LLM Agents Versatile and Efficient Robot Manipulator](https://arxiv.org/abs/2611.34750)**
  NVIDIA (per RoboDojo leaderboard) · *Paper* · 2026-11-25 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.34750)] [[Project](https://serenos.github.io/solve-website)]  
  'SOLVE reaches state-of-the-art performance of 74.5% on RoboDojo and 84.5% on RoboLab, with only $1.7 per episode on average, 12x less than previous dense-control agent policies.' On a real UR12e 'the same agent achieves an 88% success rate (75 of 85 episodes) over 16 challenging zero-shot tasks.' Ablation on RoboDojo: the RoboProbe GPT-6 Astra baseline at 22.9% (154.6 calls) rises to 49.5% with sparse keyposes alone and 68.3% with query points and notes.  
  <sub>**Model:** GPT-6 Astra, GPT-6.1 Sol, Gemini 4 Argon · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Training-free multimodal LLM agent writes a sparse, ordered sequence of 6-DoF end-effector keyposes per call, observes the result and writes the next; a motion planner interpolates; keyposes grounded by sparse depth queries (triangulation, stereo or monocular depth); reflects on rollouts and distils a few rules per task · **Eval:** sim+real · **Judged by:** RoboDojo / RoboLab simulator checkers; real-robot judge not stated · **Trials:** RoboDojo official run: seed 3, 2,100 episodes (50 per task); RoboLab: 120 tasks × 5 episodes; real UR12e: 16 tasks, 85 episodes · **Speed/cost:** 'each model call takes seconds'; real robot averages 21.9 calls and 6.6 minutes per episode; $1.7 per episode with GPT-6 Astra, $0.5 with GPT-6.1 Sol (list prices), vs $21.1 cited for GPT-6 Astra Direct</sub>  
  ⚠️ <sub>Authors: 'Some real tasks require force or continuous feedback that keyposes cannot provide, and each model call takes seconds.' GPT-6.1 Sol RoboDojo rows are two runs at 5 episodes per task. RoboDojo stars the SOLVE leaderboard entry for injecting task-specific information beyond the official Detail Description (see the robodojo entry). Shirt folding was the weakest real task (6 of 10).</sub>  
  <sub>↪ also in: [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="embo-harness"></a>
- **[Embo-Harness: Towards Understanding Frontier-Model-as-Policy Harness](https://arxiv.org/abs/2611.31201)**
  S-Lab, Nanyang Technological University; ACE Robotics; SenseTime Research · *Paper* · 2026-11-23 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.31201)] [[Project](https://dravenalg.github.io/projects/Embo-Harness/)]  
  Controlled study of frontier-model-as-policy harnesses, varying prompting, planning, action execution and tool use one factor at a time on GPT-6-Astra. 'On RoboLab-120, Embo-Harness achieves an 83.3% success rate' (Score 89.2) 'compared with 57.1% for SenseNova-RoboRSI, the strongest existing baseline'; real robot (Franka FR3): 'succeeds in 15 of 20 zero-shot trials across four real-world manipulation tasks'. Probes suggest the model relies on spatial target estimation more than low-level joint/trajectory generation.  
  <sub>**Model:** GPT-6-Astra, GPT-6.1-Sol, GPT-6.1-Terra · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** GPT-6-Astra (xhigh) emits short fixed-length chunks (8) of absolute end-effector targets executed via IK, plus a short multi-action-sequence tool and a VLA-refinement tool (a VLA proposes an action each step, the model refines and executes it); 640x360 two-view images · **Eval:** sim+real · **Judged by:** RoboLab-120 SR/Score metrics (sim); real-world judge not stated · **Trials:** ablations: 20 RoboLab tasks x 3 runs; full RoboLab-120: per-task episode count not stated; real: 4 tasks x 5 zero-shot trials · **Speed/cost:** harness time 10.5-14.8 min per (ablation) configuration on 20 tasks x 3 runs (Table 1); not reported for full RoboLab-120; dropping visual history cuts KV-cache hit rate from over 95% to ~25%, a '7–8× increase in uncached token consumption'</sub>  
  ⚠️ <sub>Authors: 'Our findings depend on the capabilities of current frontier models and may evolve with future advances.' and 'dexterous manipulation, locomotion, and tactile perception require additional low-level and dynamic capabilities'. Real-world failures 'primarily stem from limitations in fine-grained spatial perception'. AMP1 is excluded from the comparison because of its 'external high-accuracy depth estimator'; NVIDIA's Astranomy (74.8% on RoboLab-120) is cited only as a concurrent blog, not compared. The final recipe includes VLA refinement but the paper does not name which VLA. Recipe chosen on a 20-task RoboLab subset that is part of RoboLab-120. SenseNova-RoboRSI (the 'strongest baseline') is by the SenseNova joint team, which shares several authors with this paper.</sub>  
  <sub>↪ also in: [Analyses, Critiques & Reproducibility](#critiques)</sub>

<a id="contact-harness"></a>
- **[Contact Harness: Enabling VLM Agents to Perform Contact-Rich Manipulation](https://arxiv.org/abs/2611.29377)**
  MARS Lab, Nanyang Technological University · *Paper* · 2026-11-22 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.29377)] [[Project](https://ntumars.github.io/ContactHarness/)]  
  Textual skills plus compliant force-limited execution let a frozen GPT-6 Astra do contact-rich manipulation zero-shot on Rokae and Franka arms. 'With a single prompt skill, Contact Harness achieves a full-insertion rate of 90.7% across 15 connector types' (136/150), and wiping, writing, peeling and pivoting succeed in all 40 trials. In simulation it 'reaches 96.7% success, compared with at most 68.3% for pretrained VLA baselines fine-tuned on task demonstrations' (Fable 5.1/5.2: 98.3%).  
  <sub>**Model:** GPT-6 Astra, Claude Fable 5.1, Claude Fable 5.2 · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Guided by textual skills, the VLM requests vision/force/tactile/proprioception observations and issues a single command or short batch (target displacement + duration); an impedance controller with soft/hard contact-force limits executes it, regulating motion between agent decisions · **Eval:** sim+real · **Judged by:** task-specific success criteria (real: insertion counts only at the mechanical limit; judge not named); sim: task checks, Write judged by a person (VLA Write runs judged by GPT-6 Astra) · **Trials:** real: 15 connectors x 10 (150) + 4 other contact tasks x 10 + real-PC 3 x 10 + speed tests 3 x 10; sim: 6 tasks x 10 per method · **Speed/cost:** connector insertion 378 s on average, ~90% spent on model inference and observation; 96 s with fast mode + memory (IEC); 'a real-robot USB-A insertion using about 1.6 million tokens on average'</sub>  
  ⚠️ <sub>Authors: 'The main limitation is long execution time, primarily due to the agent’s reasoning latency.' Supplement: depends on a remote model service whose 'interruptions or stalls put the execution on hold and sometimes cause a failure directly'; small/occluded plugs are hard to see; 'token usage is high' (~1.6M tokens per USB-A insertion); some sockets (e.g. HDMI hidden ring) remain unsolved; uneven connector surfaces need connector-specific prompting; requires wrist force or joint-torque sensing with compliant control. Task prompts are per-task and hand-written; sim benchmark is the authors' own six tasks.</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic)</sub>

<a id="libero10-frontier"></a>
- **[From Reasoning to Action: Benchmarking Frontier AI Models on LIBERO-10 Robot Manipulation Tasks](https://arxiv.org/abs/2610.30051)**
  — · *Paper* · 2026-10-21 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2610.30051)]  
  Best is Astra at 44%, then Gemini-4 Argon at 43%. More reasoning effort generally helps, at extra cost. Models do well on placement and struggle with precise spatial arrangement and multi-step interaction.  
  <sub>**Model:** GPT-6 Astra, GPT-6.1 Sol, GPT-6 Luna, Claude Opus 5, Claude Opus 5.5, Gemini-4 Argon · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Structured tool calls specifying target EEF poses and gripper commands · **Eval:** sim · **Judged by:** LIBERO checker · **Trials:** 18 configurations, 1,800 episodes</sub>  
  <sub>↪ also in: [Benchmarks & Evaluation Reports](#benchmarks)</sub>

<a id="astra-visuotactile"></a>
- **[GPT-6 Astra Is a Native Visuo-Tactile Policy for Contact-Rich Manipulation](https://arxiv.org/abs/2610.26846)**
  Tsinghua University / Alibaba (Amap) · *Paper* · 2026-10-19 · `💻 code / results`  
  [[Paper](https://arxiv.org/abs/2610.26846)] [[Project](https://tactalent.github.io/)] [[Code](https://github.com/ccyydd/TacTalent)] ![stars](https://img.shields.io/github/stars/ccyydd/TacTalent?style=flat-square&label=%E2%98%85)  
  First demonstration that a frontier model reads vision-based tactile images and uses contact cues, few-shot and closed loop. With visuo-tactile input Astra reaches 93.8% (UniVTAC) and 81.8% (OpenViTac), 22.9 and 13.1 points above the strongest reported specialist baselines; vision-only reaches 76.3% and 80.6%.  
  <sub>**Model:** GPT-6 Astra (xhigh) · **Below it:** none · **Interface:** Scene + tactile RGB images and in-context demos in; ordered 7-D EEF-delta + gripper commands out, converted by a benchmark adapter · **Eval:** sim · **Judged by:** simulator checker (official success criteria; one task's criterion relaxed) · **Trials:** 19 tasks (UniVTAC + OpenViTac), 210 sampled scene seeds per setting · **Speed/cost:** median response 15.4 s (vision) / 14.0 s (visuo-tactile); 335.97 million tokens, CNY 7,505.05 for both phases</sub>  
  ⚠️ <sub>Authors: simulation only; cost limits most tasks to ten episodes instead of the full 100-episode evaluation, while baselines are published full-benchmark numbers. Uses task-specific successful demonstrations in context. Tactile input hurts on some tasks.</sub>  

<a id="bitter-lesson-robotics"></a>
- **[The Bitter Lesson Comes to Robotics](https://arxiv.org/abs/2610.25287)**
  — · *Paper* · 2026-10-18 · `📝 preprint` · 🏷️ CoRL 2026 Action Gap workshop  
  [[Paper](https://arxiv.org/abs/2610.25287)] [[Post](https://lesswrong.com/posts/ndS9Xn8Qx5PppHJ3Q/the-ability-of-frontier-models-to-control-robots-is-rapidly)]  
  First broad comparison of frontier LMs on a common real-hardware manipulation suite. Models can directly control real arms but are not yet precise or efficient enough to finish within a practical action budget. Performance doubling time of 53.9 days over July–October 2026.  
  <sub>**Model:** 9 frontier multimodal LMs at multiple effort / service tiers · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Direct end-effector pose commands · **Eval:** real · **Trials:** 6 RoboDojo tasks on physical hardware · **Speed/cost:** best execution rate improved 4.4× (Jul–Oct 2026); lowest execution cost fell 6.2× (Jul–Oct 2026)</sub>  
  ⚠️ <sub>Short window (4 months) and 6 tasks: a weak basis for extrapolation. The LessWrong companion post says each trial is graded by GPT-6 Astra (H) from the three camera feeds, i.e. an LLM judge that is also one of the evaluated models; trials have a 40-action budget, and the authors call the doubling-time CI (36.1–59.5 days) 'relatively wide'.</sub>  
  <sub>↪ also in: [Benchmarks & Evaluation Reports](#benchmarks)</sub>

<a id="astranomy"></a>
- **[Astranomy: An Empirical Study of GPT-6 Astra as a Native Robot Policy](https://research.nvidia.com/labs/srl/projects/astranomy/)**
  NVIDIA Seattle Robotics Lab · *Report* · 2026-10-14 · `💬 post only` · 🏷️ CoRL 2026 LBR  
  [[Project](https://research.nvidia.com/labs/srl/projects/astranomy/)]  
  Zero-shot on RoboLab-120: Agentic 74.8%, Orchestrated 66.5%, Direct (EEF) 66.3%, against Cosmos3-Nano-Policy 36.8% and π0.5 28.0%. Ablations: the action space and the geometry in the prompt matter hugely for Direct (19.3% → 72.7% with gripper/camera geometry) but barely for Agentic.  
  <sub>**Model:** GPT-6 Astra · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Three roles: Direct (EEF / joint / B-spline chunks per API call), Agentic (persistent Codex session with tools), Orchestrated (reviews or overrides Cosmos3-Nano-Policy proposals) · **Eval:** sim · **Judged by:** RoboLab task checkers · **Trials:** 120 tasks × 5 seeds · **Speed/cost:** Direct 18.56 s/call; Agentic 13.37 s; π0.5 46.96 ms; Direct $1.96, Orchestrated $17.72, Agentic $36.40 per episode</sub>  
  ⚠️ <sub>Sim only; 5 episodes per task (authors flag this); no arXiv yet. Putting Astra on top of a weak System 1 (Orchestrated) did not beat Astra alone.</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic), [Frontier Model over a Learned System 1 / System 0](#orchestrated)</sub>

<a id="robodojo-astra"></a>
- **[An Unexpected Robot Policy: Early Evaluations of GPT-6 Astra on RoboDojo and Beyond](https://arxiv.org/abs/2609.24170)**
  — · *Paper* · 2026-09-21 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2609.24170)] [[Post](https://robodojo-benchmark.com/report/gpt-6-astra-eval)]  
  Frames the question in System 1 / System 2 terms. Astra: 22.48% success, Score 28.97, ranking above all 40 public policies; GPT-5.5 0.88% and DeepSeek-Flash 1.92%. Capability is sharply polarized: good at semantic generalization, poor at precision, dynamic control, and bimanual coordination. One-shot demos give no aggregate gain.  
  <sub>**Model:** GPT-6 Astra, GPT-5.5, DeepSeek-Flash · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** LLM as policy with shared post-processing · **Eval:** sim · **Judged by:** RoboDojo checker · **Trials:** 42 tasks × 50 episodes (Astra, GPT-5.5); 10 (DeepSeek)</sub>  
  <sub>↪ also in: [Benchmarks & Evaluation Reports](#benchmarks)</sub>

<a id="show-harness"></a>
- **[Show-Harness: Just a VLM Agent Can Play Robots](https://arxiv.org/abs/2609.10522)**
  Show Lab, NUS · *Paper* · 2026-09-09 · `💻 code / results`  
  [[Paper](https://arxiv.org/abs/2609.10522)] [[Project](https://showlab.github.io/Show-Harness/)] [[Code](https://github.com/showlab/Show-Harness)] ![stars](https://img.shields.io/github/stars/showlab/Show-Harness?style=flat-square&label=%E2%98%85)  
  Argues the right interface unlocks VLM capability without extra capacity: zero-shot control with closed frontier VLMs, and small open VLMs adapted with a few GPU-hours. GUMI extends the same action space to GUI-based demonstration collection.  
  <sub>**Model:** closed frontier VLMs, small open VLMs (fine-tuned) · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Discrete semantic action units that embodiment-specific interpreters ground deterministically; the VLM stays responsible for fine-grained physical decisions · **Eval:** sim+real</sub>  
  <sub>↪ also in: [Making It Fast & Cheap](#fast)</sub>

<a id="anthropic-robotics"></a>
- **[How Claude performs on robotics tasks](https://www.anthropic.com/research/claude-plays-robotics)**
  Anthropic (Frontier Red Team) · *Report* · 2026-07-09 · `💬 post only`  
  [[Post](https://www.anthropic.com/research/claude-plays-robotics)]  
  'Interface matters as much as the model.' Direct joint control mostly fails: best LIBERO full-task success is 5.5%, and no model stands a collapsed G1 up. Supervising pretrained controllers works far better. However, every model did worse supervising MolmoAct than MolmoAct alone on its own tasks, while beating it on novel tasks.  
  <sub>**Model:** Claude Mythos Preview, Opus 4.5–4.7, GPT-5.4, Gemini 3.1 Pro, Kimi K2.6, Qwen 3.6+ · **Below it:** frozen learned policy · **Interface:** Four interfaces compared: direct torques/commands, programmatic controller, model-designed RL, high-level steering of a gait or VLA (MolmoAct) · **Eval:** sim+real · **Judged by:** simulator; informal real Go2 runs · **Trials:** 35 per cell (200 for LIBERO-40) · **Speed/cost:** ≈0.2–0.4 Hz non-reasoning calls vs ≈83 Hz needed for quadruped control</sub>  
  ⚠️ <sub>Simulator paused between calls (best-case capability); prompts not tuned per model.</sub>  
  <sub>↪ also in: [Frontier Model over a Learned System 1 / System 0](#orchestrated), [Analyses, Critiques & Reproducibility](#critiques)</sub>

<a id="bicicle"></a>
- **[Bimanual Robot Manipulation via Multi-Agent In-Context Learning](https://arxiv.org/abs/2604.20348)**
  Sapienza University of Rome · TU Darmstadt · *Paper* · 2026-04-22 · `📄 peer-reviewed` · 🏷️ CoRL 2026  
  [[Paper](https://arxiv.org/abs/2604.20348)] [[Project](https://alesspalma.github.io/bicicle)]  
  Off-the-shelf text LLMs control two arms through in-context learning with no fine-tuning. 'Evaluated on 13 tasks from the TWIN benchmark, BiCICLe achieves 70.5% average success rate, outperforming the best training-free baseline by 6.1 percentage points'; real bimanual Franka: 60.0% Lift Box, 40.0% Open Pot, 60.0% Cleanup.  
  <sub>**Model:** GPT-5-mini (gpt-5-mini-2025-08-07), Qwen 2.5 7B (replication) · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Text-serialized object poses and few-shot demos in the prompt; a leader LLM agent predicts one arm's discretized end-effector keyframes, a follower agent predicts the other arm conditioned on the leader; executed keyframe by keyframe with re-observation · **Eval:** sim+real · **Judged by:** TWIN simulator checker (sim); not stated (real) · **Trials:** 13 TWIN tasks × 3 seeds × 100 episodes; 3 real tasks × 10 trials · **Speed/cost:** median 125.3s LLM wall time per episode (Lift Ball, GPT-5-mini)</sub>  
  ⚠️ <sub>Simulation uses ground-truth segmentation masks; the discrete keypose interface caps precision; bounded by context window and API latency.</sub>  

**Cross-listed here:**

- ↪ **[ICLWorld](#iclworld)**: ICLWorld: Benchmarking In-Context Learning of Agents from Digital to Physical Worlds <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[Atomic Policy](#atomic-policy)**: Atomic Policy: Composing Atomic Manipulation Skills with Agentic Reasoning <sub>(listed under [Frontier Model over a Learned System 1 / System 0](#orchestrated))</sub>
- ↪ **[WorldLeague](#worldleague)**: WorldLeague: Benchmarking Physical Agency <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[NavRSI](#navrsi)**: NavRSI: Recursive Harness Self-Improvement for Vision-and-Language Navigation <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[Embodied-Harness](#embodied-harness)**: Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[RoboColiseum](#robocoliseum)**: RoboColiseum: Co-evolution of Simulation, Evaluation, and Models <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[ROSWorld](#rosworld)**: ROSWORLD: When Digital Task Competence Meets Physical Execution <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[AgentRoboCritic](#agentrobocritic)**: AgentRoboCritic: Understanding the Capability of Frontier Agents on Direct Robot Control <sub>(listed under [Analyses, Critiques & Reproducibility](#critiques))</sub>
- ↪ **[Gemini 4 Hydrogen](#gemini-4-hydrogen)**: Gemini 4 Hydrogen: a faster model for general purpose robotics <sub>(listed under [Agentic & Code-Writing Policies](#agentic))</sub>
- ↪ **[ForceHarness](#forceharness)**: ForceHarness: Turning Force into Action and Physics for Frozen Frontier Models <sub>(listed under [Agentic & Code-Writing Policies](#agentic))</sub>
- ↪ **[PEAR / RURL](#pear-rurl)**: Training Reasoning Models in Simulation to Natively Use Real Robots <sub>(listed under [Making It Fast & Cheap](#fast))</sub>
- ↪ **[Claude Fable 5.2 (RoboDojo Sim)](#claude-fable-5-2)**: Introducing Claude Fable 5.2 and Claude Mythos 5.2 <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[LEXP](#lexp)**: Learning from Physical Experience:Context-Space Adaptation for Robotic Manipulation <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[ReTrace](#retrace)**: ReTrace: Cross-Stage Failure Attribution for Self-Improving Robotic Manipulation <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[PhysEvo](#physevo)**: PhysEvo: Astra Can Act, Let It <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[RoboDojo-RC Tier 1](#robodojo-rc-tier1)**: RoboDojo-RC Tier 1: real-world leaderboard of frontier models, agents and VLAs (Robocurve) <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[Robocurve Astra eval](#robocurve-astra)**: GPT-6 Astra vs Claude Fable 5 / 5.1 on bimanual YAM arms <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[RoboSpoof](#robospoof)**: You Can't See Everything: Perceptual Attacks on Embodied AI <sub>(listed under [Analyses, Critiques & Reproducibility](#critiques))</sub>

</details>

<a id="agentic"></a>
## 🧑‍💻 Agentic & Code-Writing Policies

*The model acts through a harness: it writes and runs code against sensing/perception/motion APIs, observes the outcome, and repairs. Learned System 1 is absent; motion is analytic (IK, waypoints, ROS).*

<details open><summary><b>21 entries</b> + 31 cross-listed</summary>

<a id="regharness"></a>
- **[RegHarness: Regulating What Code-as-Policy Agents Keep from Steps to Skills](https://arxiv.org/abs/2611.33739)**
  Xiamen University Malaysia; Beijing Zhongke Huiling Robot Technology; Institute of Automation, CAS · *Paper* · 2026-11-25 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.33739)]  
  With 'a single low-cost model across all run-time roles, RegHarness achieves an 87.8% success rate (158/180) on paired LIBERO-PRO trials, compared with 39.4% for RATs, and a 72.0% success rate on MolmoSpaces trials'. A 2×2 ablation 'shows that its skill refinement alone increases RATs' successful trials from 71 to 135, whereas run-time governance alone achieves 105 and RATs' native stepwise reset-and-replay mode achieves only 46'. Real Kinova Gen3: 28 of 45 vs 21 for RATs, 'a difference not significant at this sample size'.  
  <sub>**Model:** DeepSeek-Flash (provider alias deepseek-flash), Claude Opus 5.5 · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Two-level harness around the RATs Code-as-Policy agent team: within a trial, each proposed step is tested from a reset scene with committed steps replayed, and a fixed-rule controller commits it only if the verifier and a task-long LLM auditor approve (all run-time roles on deepseek-flash); between runs, Claude Opus 5.5 in Claude Code turns logged failures into default-off revisions of skills, primitives and rules that the authors choose to enable · **Eval:** sim+real · **Judged by:** benchmark task check (LIBERO-PRO / MolmoSpaces), also read by the controller during execution; real: operator on site · **Trials:** LIBERO-PRO: 180 paired trials (60 tasks × 3 initial states), 300 over 5 states; MolmoSpaces: 200; real Kinova Gen3: 3 tasks × 15 trials · **Speed/cost:** 'takes 66 minutes on average against 50' per LIBERO-PRO trial (vs RATs); 'an estimated CNY 2.16 (US$0.32)' per trial in run-time model calls</sub>  
  ⚠️ <sub>Authors: 'Reset-and-replay is currently limited to simulation'; both levels were debugged on initial state 0, so 'the observed gain from skill refinement may be an upper estimate'; refinement 'is gated by the authors and lacks the automatic acceptance test'; the coding agent 'reads success checks, full logs and, on MolmoSpaces during design, the benchmark's ground truth'; all systems read the task check during execution. Perception uses simulator camera extrinsics and noise-free depth. All MolmoSpaces trials are in-sample. LIBERO-PRO here is the 60 Object/Goal/Spatial tasks only.</sub>  
  <sub>↪ also in: [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="acap"></a>
- **[ACAP: Asynchronous Coding Agents for Efficient Robot Control](https://arxiv.org/abs/2611.31205)**
  S-Lab, Nanyang Technological University; University of Oxford; ACE Robotics · *Paper* · 2026-11-23 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.31205)] [[Project](https://projects.zxhezexin.com/acap)]  
  Splits a robot across asynchronous coding agents per control group, coordinated by a lead hyper-agent, on Galaxea R1 Pro and AgileX PiPER robots. 'Across 72 real-world rollouts covering 25 task/platform settings, ACAP reduces task-balanced time cost by 28.2% compared with a single-agent Direct Policy'; on repeated trials it lowers mean 30-min-capped cost on all six tasks (−29.4%), and on Collaborative tasks 'ACAP completes ten of ten runs, compared with eight for Direct and three for Fixed.'  
  <sub>**Model:** Astra (lead xhigh, members medium; paper does not give the full model name) · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** One robot run as a team of persistent coding agents: each member owns a control group (arm+gripper, torso+chassis) and runs its own observe–reason–code–execute loop issuing end-effector/joint targets; a lead 'hyper-agent' assigns work, sets event-based waits, and can take over groups for coupled actions under exclusive control ownership · **Eval:** real · **Judged by:** human annotators with task-specific rubrics (physical progress, completion); operators monitor safety · **Trials:** task-coverage: 72 rollouts over 25 task/platform settings; repeated-trial: 90 rollouts (6 tasks x 5 trials x 3 policies) · **Speed/cost:** task-balanced mean 13.67 min (ACAP) vs 19.04 min (Direct) per task over 25 settings</sub>  
  ⚠️ <sub>Authors: 'The current framework does not include a dedicated motion-level collision-checking layer.' Evaluation is about time cost vs. the authors' own single-agent and fixed-delegation baselines; no learned-policy (VLA) comparison. Progress is human-annotated; operators monitor safety. The model is named only as 'Astra'. Releases a real-world rollout dataset.</sub>  
  <sub>↪ also in: [Making It Fast & Cheap](#fast)</sub>

<a id="evomisty"></a>
- **[EvoMisty: Building, Optimizing, and Evolving Capabilities on a Social Robot](https://arxiv.org/abs/2611.31341)**
  University at Buffalo · *Paper* · 2026-11-23 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.31341)] [[Project](https://wangxiaoshawn.github.io/projects/evomisty/index.html)]  
  Coding agents build a social robot's capabilities from its documentation and verify them on hardware. 'The two agents construct 109 and 107 verified atomic capabilities, respectively. Both complete all 28 AutoMisty benchmark tasks and seven additional tasks beyond AutoMisty's capabilities.' 'Optimization improves all seven evaluated metrics across five tasks', e.g. 'dialogue response latency decreases by 52% and 71%'.  
  <sub>**Model:** Claude Opus 5.5, GPT-6 Astra · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Plugin for Claude Code (Opus 5.5) and Codex (GPT-6 Astra): the agent reads Misty II documentation, writes a control program, verifies each capability on the physical robot, writes task programs from the capability and skill libraries, and optimizes them on user-specified metrics · **Eval:** real · **Judged by:** agent-written automatic checks plus human checks for anything seen or heard; optimisation metrics measured by the authors on held-out data · **Trials:** 28 AutoMisty tasks + 7 new tasks on one physical Misty II; attempts per task not stated</sub>  
  ⚠️ <sub>Authors: 'the applicability of EvoMisty to other robot platforms remains to be validated'; 'Capability verification and task completion checks still rely on human observation and feedback'. Tasks are mostly speech, display and base motion, with no manipulation. The AutoMisty baseline was rerun by the authors. Code 'coming soon'.</sub>  
  <sub>↪ also in: [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="gemini-4-hydrogen"></a>
- **[Gemini 4 Hydrogen: a faster model for general purpose robotics](https://developers.googleblog.com/gemini-hydrogen-for-robotics/)**
  Google DeepMind · *Blog* · 2026-11-17 · `💬 post only`  
  [[Code](https://github.com/google-deepmind/robotics-antigravity-plugin)] [[Post](https://developers.googleblog.com/gemini-hydrogen-for-robotics/)] ![stars](https://img.shields.io/github/stars/google-deepmind/robotics-antigravity-plugin?style=flat-square&label=%E2%98%85)  
  A general-purpose fast Gemini 4 model that replaces Gemini Robotics ER 2 for embodied reasoning and ships a Robotics plugin for Google Antigravity (I2RT YAM, SO-ARM101, FR3 Duo, YAM Pro). On Artificial Analysis Robotics 0.1, 'Hydrogen scores 58', similar to Argon at a lower cost per token; a new arm is 'calibrated and ready for tasks in about 10 minutes'.  
  <sub>**Model:** Gemini 4 Hydrogen (gemini-4-hydrogen) · **Interface:** Plain-language goal + camera view; the model plans, writes and runs control code (Google Antigravity Robotics plugin, MuJoCo, Gemini API); can also drive arms directly from images. Low-level controller not described. · **Eval:** real · **Speed/cost:** 'faster' (qualitative only); 'lower cost per token' than Argon (no figure)</sub>  
  ⚠️ <sub>Vendor blog; no success rates, trial counts or latency figures. The AA score is Google-reported. Antigravity requires a paid Google AI Pro or Ultra subscription.</sub>  
  <sub>↪ also in: [Frontier Model as Direct Policy](#direct)</sub>

<a id="forceharness"></a>
- **[ForceHarness: Turning Force into Action and Physics for Frozen Frontier Models](https://arxiv.org/abs/2611.21099)**
  Show Lab, NUS · *Paper* · 2026-11-16 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.21099)] [[Project](https://showlab.github.io/ForceHarness)]  
  Gives API-only frozen models force sensing without demos or finetuning, on a Franka FR3 with no wrist F/T sensor. Real robot: GPT-6 Astra goes from 2/60 without force to 54/60, GPT-6.1 Sol reaches 47/60. ForceBench: Astra and Sol 87.5% (Fable 75.0%) vs 35.31% for the best trained policy; HiddenPhys: Astra 87/140 → 135/140, matching the hand-written expert at 136/140.  
  <sub>**Model:** GPT-6 Astra, GPT-6.1 Sol, Claude Fable 5.2 · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** One tool call per turn picking a self-terminating force primitive (move_until_contact, push, insert, screw, …) run by admittance control on the stock impedance controller; a physics translation layer returns mass, friction, contact height with uncertainty · **Eval:** sim+real · **Judged by:** human operator (real); ForceBench public evaluator; HiddenPhys code check on final state · **Trials:** real: 6 tasks × 10 episodes per condition; ForceBench 8 tasks × 10; HiddenPhys 7 tasks × 20 seeds · **Speed/cost:** 'Model queries add seconds between primitives'; cuts Astra's cost per episode by 45% (HiddenPhys)</sub>  
  ⚠️ <sub>Authors: 'Model queries add seconds between primitives and preclude reactive coordination, a fixed menu limits new motion laws, and our ablations run only in simulation.' Primitive menu, physics estimators and per-task instructions are hand-written; ForceBench tools were tuned on 8 of 10 seeds; HiddenPhys gives object poses as noisy text (privileged state). Code to be released on publication.</sub>  
  <sub>↪ also in: [Frontier Model as Direct Policy](#direct)</sub>

<a id="reins"></a>
- **[Reins: Frontier Multimodal Models Driving Real Robot Arms on Long-Horizon Tasks, Zero-Shot](https://arxiv.org/abs/2611.16632)**
  — · *Paper* · 2026-11-12 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.16632)]  
  Targets the 'blind while the arm moves and while it thinks' problem. GPT-6.1 Sol succeeds in 88% of real episodes with no task-specific code; without the harness it fails every shell game and takes 8× as long. Three frontier models perform alike but differ in tracking a scene that changes while the actor thinks. Also builds a sim-ready twin of the scene for continual learning.  
  <sub>**Model:** GPT-6.1 Sol, GPT-6 Astra, Claude Opus 5.5 · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** 3D perception tools plus atomic actions that report contact and grip; actions chained in one call with per-step conditions; a second 'narrator' instance watches the cameras continuously · **Eval:** real · **Trials:** 5 real long-horizon tasks (dual-arm)</sub>  
  ⚠️ <sub>Code to be released on publication.</sub>  

<a id="amp1"></a>
- **[On Agentic Manipulation Policies](https://arxiv.org/abs/2611.09892)**
  Apple · *Paper* · 2026-11-06 · `💻 code / results`  
  [[Paper](https://arxiv.org/abs/2611.09892)] [[Project](https://apple-aiml-research.github.io/ml-amp/)] [[Code](https://github.com/apple-aiml-research/ml-amp)] ![stars](https://img.shields.io/github/stars/apple-aiml-research/ml-amp?style=flat-square&label=%E2%98%85)  
  Reference harness that runs unchanged on single-arm, bimanual, and mobile manipulation with no grasp/push/place skills. Zero-shot 85.6% on RoboLab-120 (vs 49.2% leading VLA, 42.9% leading WAM); 104/108 real-world successes. AMP1+ adds a persistent notes/code memory that lifts RoboDojo from 26.4% to 84.1% after practice.  
  <sub>**Model:** Claude Opus 5.5 (main real-world), Gemini 4 Argon, 13 models incl. 6 open-weight · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Python in a persistent interpreter; SDK for sensing, a segmented scene model, and timed TCP waypoints (harness does IK + limit checks) · **Eval:** sim+real · **Judged by:** benchmark checkers (sim); experimenters (real) · **Trials:** 108 real trials over 12 tasks × 3 robots · **Speed/cost:** avg 34.8 model calls per RoboLab episode</sub>  
  ⚠️ <sub>Authors: 'AMPs are not yet practical, as the robot spends much of each episode waiting for the model.' Quasi-static scenes only; no mid-trajectory revision. Proposed fix is to distill AMP experience into fast local controllers.</sub>  
  <sub>↪ also in: [Getting Better Without Weight Updates](#self-improving), [Analyses, Critiques & Reproducibility](#critiques)</sub>

<a id="dimure"></a>
- **[DiMuRe: Diagnosis-Guided Multilevel Recovery for Robotic Task Execution](https://arxiv.org/abs/2611.04226)**
  Beijing Institute of Technology · *Paper* · 2026-11-03 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.04226)]  
  A recovery layer for program-based robot-use agents, plus LIBERO-Disturb, a benchmark of mid-execution disturbances for both program agents and VLAs. On 801 disturbed Encore cases, Local DiMuRe reaches 77.65% complete-task success vs 58.68% for the original program under the same physical-step allowance; Full DiMuRe reaches 81.90% with terminal MLLM replanning, an additional step allowance and early handoff.  
  <sub>**Model:** DeepSeek V4.1 Flash (terminal replanning) · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Diagnosis selects reuse of the robot-use agent's task program, predefined recovery skills (including bounded GraspVLA grasping), or, after the program exits, MLLM-generated corrective code from images and execution feedback; each recovery is locally verified · **Eval:** sim · **Judged by:** LIBERO-Disturb task checks · **Trials:** 801 scheduled disturbed Encore cases (30 fixed Encore programs × 3 reset seeds)</sub>  
  ⚠️ <sub>Authors: current evidence is limited to simulation; Full's extra allowance and early handoff mean its gain over Local cannot be attributed to MLLM replanning alone; Encore and VLA evaluations use different disturbance versions and protocols, so they are not directly comparable.</sub>  
  <sub>↪ also in: [Benchmarks & Evaluation Reports](#benchmarks)</sub>

<a id="openrua"></a>
- **[OpenRUA: Robot-Use Agents Are Zero-Shot Visuomotor Policies](https://arxiv.org/abs/2610.02459)**
  — · *Paper* · 2026-10-01 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2610.02459)]  
  An off-the-shelf coding agent, with no bespoke primitives, reaches 99.0% on CaP-Bench and 87.0% on LIBERO-PRO. Emergent behaviour: the agent writes its own metric-perception code in 96.8% of episodes and its own motion-control clients in 95.9%.  
  <sub>**Model:** Claude Code + Claude Opus 5 · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Zero-abstraction: terminal access to native ROS 2 plus its docs only; perception becomes file I/O, manipulation becomes coding · **Eval:** sim · **Judged by:** benchmark checkers</sub>  
  ⚠️ <sub>Secondary critiques note the simulator is paused while the agent thinks, episodes take ~100 turns, and baselines are copied from original papers. The OpenRUA team also published retests of RoboDojo leaderboard entries (see Critiques).</sub>  
  <sub>↪ also in: [Analyses, Critiques & Reproducibility](#critiques)</sub>

<a id="rapid"></a>
- **[RAPID: Robot Agentic Programming from Demonstrations](https://arxiv.org/abs/2609.30249)**
  — · *Paper* · 2026-09-24 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2609.30249)] [[Project](https://yuyaoliu.me/projects/rapid)]  
  From one visual human demonstration, infers a testable spec, primitives, and an environment, then generates, verifies, and refines robot programs. Covers 8 contact-rich nonprehensile tasks (sim and a real Franka) plus LIBERO-Pro.  
  <sub>**Model:** coding agent · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Object-centric relational programs whose primitives are trajectory-optimization programs · **Eval:** sim+real</sub>  

<a id="aquacap"></a>
- **[AquaCap: A Training-Free Underwater Embodied Agent with Code-as-Policy](https://arxiv.org/abs/2609.23133)**
  Sun Yat-sen University · Dalian University of Technology · *Paper* · 2026-09-19 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2609.23133)]  
  Closed-loop code-as-policy for an underwater ROV with no training, using only onboard camera images and robot state. 'AquaCap achieves an overall SR of 66.43%, outperforming U0 by 19.29 percentage points' in simulation; real ROV grasping and transport are demonstrated.  
  <sub>**Model:** DeepSeek-V4-Pro (policy), DeepSeek-V4-Flash (coding), Qwen3.7-Flash (VLM) · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Policy agent plans condition-aware stages; coding agent writes control programs over high-level ROV / arm APIs; failure-aware memory drives replanning and code revision · **Eval:** sim+real · **Judged by:** task-specific success criterion (lift held, transport within distance) · **Trials:** Sim: 20 Stonefish tasks; real: 10 grasping + 10 transport trials</sub>  
  ⚠️ <sub>Authors: 'Execution efficiency, however, remains a key bottleneck'; controls the ROV only through high-level APIs, not thruster dynamics; real-world success is much lower than in sim.</sub>  
  <sub>↪ also in: [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="agent-as-policy"></a>
- **[Agent as Policy for Robotic Manipulation](https://arxiv.org/abs/2609.12541)**
  — · *Paper* · 2026-09-11 · `💻 code / results`  
  [[Paper](https://arxiv.org/abs/2609.12541)] [[Project](https://agent-as-policy-2026.github.io/)] [[Code](https://github.com/agent-as-policy-2026/agent-as-policy)] [[Data](https://huggingface.co/datasets/Agent-as-Policy/agent-as-policy)] ![stars](https://img.shields.io/github/stars/agent-as-policy-2026/agent-as-policy?style=flat-square&label=%E2%98%85)  
  A general agent drives a physical robot through the whole task, including dynamic and deformable ones (dice flipping, targeted throwing, bimanual towel folding, assembly from human video). At least 80% success on 7 of 8 task configurations. Reusing saved procedures shortens execution over repeated trials.  
  <sub>**Model:** general-purpose agent · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Agent reads visual evidence, writes programs, issues motion commands, revises on physical outcomes · **Eval:** real · **Judged by:** authors</sub>  
  <sub>↪ also in: [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="gta-2"></a>
- **[GTA-2: A Multi-VLM Framework for Synthesizing Robot Manipulation Skills via Grounded Task Axes](https://arxiv.org/abs/2609.09808)**
  — · *Paper* · 2026-09-09 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2609.09808)] [[Project](https://gta2-project.github.io/)]  
  Zero-shot 73.9% average on 14 real-robot tasks, 31.4 pp above the strongest baseline (π0.5 and two Code-as-Policies variants); targeted human feedback raises it to 90.7%.  
  <sub>**Model:** Gemini 3.1 Pro (all agents) · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Four VLM agents build task-axis skills: keypoints/axes, controller compositions, scene parameters · **Eval:** real · **Judged by:** authors · **Trials:** 14 real tasks</sub>  

<a id="push-t-agentic"></a>
- **[Revisiting the "Push-T" Robot Manipulation Task with Agentic Robotics](https://arxiv.org/abs/2608.18227)**
  UC Berkeley · *Paper* · 2026-08-18 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2608.18227)]  
  A demonstration-free code-as-policy for Push-T, built by Claude Code with Fable 5. The state controller reaches 100.0% success (vision controller 97.2%) vs 62.5% for the LeRobot Diffusion Policy checkpoint over 200 seeds, at 120.1 vs 223.7 mean steps. A self-generated curriculum extends it to Push-A–Z (99.4% overall) and to simulated Franka (vision 89.8%) and UR5e (vision 98.5%).  
  <sub>**Model:** Claude Code with Fable 5 · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Coding agent writes, runs and revises a state-machine / MPC controller and vision pipeline offline in simulation; the generated code is the runtime policy (no LLM in the 10 Hz loop) · **Eval:** sim · **Judged by:** gym_pusht coverage threshold (simulator checker) · **Trials:** Push-T: 200 seeds; Push-A–Z: 25 episodes per letter (650) · **Speed/cost:** about 9.5 million output tokens, approximately $1,500–$2,000 API cost, approximately 221 hours in auto mode</sub>  
  ⚠️ <sub>Authors: the agent may exploit simulator-specific state or contact behaviour unavailable on real robots; 'Claude is computationally expensive and sensitive to the prompt.' State controllers use privileged ground-truth state. Simulation only; development took ~221 h under human interaction.</sub>  
  <sub>↪ also in: [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="step-stl"></a>
- **[STeP: Signal Temporal Logic for Precise Specifications for Action Generation with Vision Language Models](https://arxiv.org/abs/2607.18580)**
  University of Maryland, College Park · *Paper* · 2026-07-20 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2607.18580)]  
  'On LIBERO-PRO, STeP retains 54%-89% success across five of six evaluated perturbation settings', against 12%–26% for CaP-Agent0 (copied from CaP-X); on LIBERO-Constrained it reaches 80% safe success vs 14% for SmolVLA.  
  <sub>**Model:** GPT-5.4 · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** GPT-5.4 (System 2) formalizes the instruction as a Signal Temporal Logic spec over a fixed predicate / skill library; RRT + MPC (System 1) enforces it; an online STL monitor recalls System 2 with a history log to replan · **Eval:** sim+real · **Judged by:** simulator checker (LIBERO / LIBERO-PRO); not stated (real) · **Trials:** LIBERO-Constrained: 49 task–constraint instances; replanning: 20 trials</sub>  
  ⚠️ <sub>Authors: 'To resolve objects and their locations in LIBERO we read privileged simulator state'; a fixed predicate library limits generalization; LIBERO-PRO baselines are not re-run.</sub>  

<a id="spark-bt"></a>
- **[Sequential Planning via Anchored Robotic Keypoints](https://arxiv.org/abs/2606.30613)**
  Case Western Reserve University · *Paper* · 2026-06-29 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2606.30613)] [[Project](https://cwru-aism.github.io/spark-page/)]  
  With one open-weight 27B planner at 4-bit, no practice on the evaluated tasks and no ground-truth poses, SPARK reaches 75.1% mean success on six LIBERO-PRO position and task settings and 69.7% on the held-out language and object settings. On hardware it completes 150 of 220 trials (68.2%) across 11 task-platform settings on three robots; on CaP-Bench it scores 65.1% vs 68.3% for CaP-Agent0's three-model ensemble.  
  <sub>**Model:** Qwen3.8-27B (4-bit, local; sim main table), Gemini 3.5 Flash (hardware), gemini-3.1-pro-preview (ablation) · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** The LM writes a YAML behavior tree over a fixed skill library from SAM3 masks, 3D keypoints and the instruction; each step is re-anchored to the current scene and verified, with local recovery before asking for a new plan · **Eval:** sim+real · **Judged by:** benchmark checkers (sim); hardware trials · **Trials:** 50 episodes per task on LIBERO-PRO; 20 trials per task-platform on hardware (220 total)</sub>  
  ⚠️ <sub>In the headline run the benchmark's success check is read after each attempt to decide retries; with the robot's own checks only, it scores 67.5%. LIBERO tasks were used to develop the controllers and skills. Lowest on the goal suite (66.7%). Hardware cells with 20 trials vary by about ±20 points.</sub>  
  <sub>↪ also in: [Making It Fast & Cheap](#fast)</sub>

<a id="coenv-coex"></a>
- **[CoEnv: Code-Driven Exploration in Real-to-Sim Digital Twins for Multi-Arm Manipulation](https://arxiv.org/abs/2604.05484)**
  USTC · CUHK-Shenzhen · Fudan · SJTU · Shanghai AI Lab et al. · *Paper* · 2026-04-07 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2604.05484)] [[Project](https://faceong.github.io/CoEnv/)]  
  On five real multi-arm tasks with up to t