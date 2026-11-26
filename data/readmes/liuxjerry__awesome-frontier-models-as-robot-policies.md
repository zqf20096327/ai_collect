# Awesome Frontier Models (LLMs / VLMs) as Robot Policies [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![entries](https://img.shields.io/badge/entries-117-blue?style=flat-square) ![newest](https://img.shields.io/badge/newest%20entry-2026--11--23-green?style=flat-square) ![license](https://img.shields.io/badge/license-CC0--1.0-lightgrey?style=flat-square)

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
- [🎯 Frontier Model as Direct Policy](#direct) (10)
- [🧑‍💻 Agentic & Code-Writing Policies](#agentic) (19)
- [🎛️ Frontier Model over a Learned System 1 / System 0](#orchestrated) (12)
- [📈 Getting Better Without Weight Updates](#self-improving) (16)
- [⚡ Making It Fast & Cheap](#fast) (8)
- [🧠 The Incumbent: Dual-System VLAs](#dual-system) (17)
- [📊 Benchmarks & Evaluation Reports](#benchmarks) (17)
- [🔍 Analyses, Critiques & Reproducibility](#critiques) (4)
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

<a id="leaderboards"></a>
## 📊 Leaderboards: who measured what

> Numbers are quoted from the cited source. 'measured_by' = whose run produced the number; 'source' = entry id where it is reported. Rows with different settings are NOT directly comparable; read the 'setting' column.

### RoboLab-120 (simulation, zero-shot, DROID-style arm)

| System | Model | Type | Success rate | Setting | Measured by | Source |
|---|---|---|---|---|---|---|
| AMP1 | frontier agent | frontier: agentic | **86.0%** | 2579 / 3000, 25 eps/task; leaderboard Score 93.5 | RoboLab leaderboard | [AMP1](#amp1) |
| AMP1 | frontier agent (best config) | frontier: agentic | **85.6%** | zero-shot | Apple (AMP1) | [AMP1](#amp1) |
| Embo-Harness | GPT-6-Astra (xhigh) + VLA refinement | frontier: direct | **83.3%** | full RoboLab-120, zero-shot; Score 89.2; episodes per task not stated | Wu et al. (Embo-Harness) | [Embo-Harness](#embo-harness) |
| Astra — Agentic | GPT-6 Astra (Codex) | frontier: agentic | **74.8%** | 5 seeds/task | NVIDIA (Astranomy) | [Astranomy](#astranomy) |
| Astra — Orchestrated | GPT-6 Astra + Cosmos3-Nano-Policy | frontier over System 1 | **66.5%** | 5 seeds/task | NVIDIA (Astranomy) | [Astranomy](#astranomy) |
| Astra — Direct (EEF) | GPT-6 Astra | frontier: direct | **66.3%** | 5 seeds/task | NVIDIA (Astranomy) | [Astranomy](#astranomy) |
| SenseNova-RoboRSI | GPT-6-Astra (per Embo-Harness) | frontier: self-improving | **57.1%** | 685 / 1200, 10 eps/task; leaderboard Score 69.9 | RoboLab leaderboard | [Embo-Harness](#embo-harness) |
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
| Claude Fable 5.2 | Claude Fable 5.2 (Max effort) | frontier: model launch | **64.9% avg SR** | Anthropic's internal run, same harness for all models (undisclosed); highest available effort | Anthropic | [Claude Fable 5.2 (RoboDojo Sim)](#claude-fable-5-2) |
| PhysEvo | Astra (frozen) | frontier: self-improving | **62.00% SR · Score 68.14** | held-out layouts; retained task-specific deployment versions; five-dimension weighting | Tian et al. | [PhysEvo](#physevo) |
| UniCraft (frozen skills) | GPT-6 Astra (high effort, Codex harness) | frontier: self-improving code | **54.8% SR (115/210)** | zero-shot transfer of skills learned on other benchmarks; seed and layout 0, 42 tasks × 5 rollouts | Wang et al. (UniCraft) | [UniCraft](#unicraft) |
| InteractVLA | VL agent + steerable VLA | frontier over System 1 | **48.62%** | with recursive self-improvement | Zhao et al. | [InteractVLA](#interactvla) |
| Claude Opus 5.5 | Claude Opus 5.5 (Max effort) | frontier: model launch | **39.4% avg SR** | Anthropic's internal run, same harness for all models (undisclosed); highest available effort | Anthropic | [Claude Fable 5.2 (RoboDojo Sim)](#claude-fable-5-2) |
| Gemini 4 Argon | Gemini 4 Argon (High effort) | frontier: model launch | **34.2% avg SR** | Anthropic's internal run, same harness for all models (undisclosed); highest available effort | Anthropic | [Claude Fable 5.2 (RoboDojo Sim)](#claude-fable-5-2) |
| GPT-6 Astra | GPT-6 Astra (Max effort) | frontier: model launch | **29.8% avg SR** | Anthropic's internal run, same harness for all models (undisclosed); highest available effort | Anthropic | [Claude Fable 5.2 (RoboDojo Sim)](#claude-fable-5-2) |
| AMP1 (zero-shot) | frontier agent | frontier: agentic | **26.4% SR** | zero-shot | Apple (AMP1) | [AMP1](#amp1) |
| LLM as policy | GPT-6 Astra | frontier: direct | **22.48% SR · Score 28.97** | official 50 eps/task | Zhang et al. | [LLM as Policy on RoboDojo](#robodojo-astra) |
| LLM as policy | DeepSeek-Flash | frontier: direct | **1.92% SR** | 10 eps/task | Zhang et al. | [LLM as Policy on RoboDojo](#robodojo-astra) |
| LLM as policy | GPT-5.5 | frontier: direct | **0.88% SR** | official 50 eps/task | Zhang et al. | [LLM as Policy on RoboDojo](#robodojo-astra) |
| JustRUA | GPT-6 Astra | frontier: agentic (lean harness) | **Score 50.3** | no learned policy / self-improvement / task tuning; official L3 harness = 29.7 | Wang et al. | [JustRUA](#justrua) |
| uni-robot-agent | Qwen3.8-Flash-Next (open) | open model: agentic | **Score 31.39** | no privileged inputs | Yuan et al. | [uni-robot-agent](#democratizing-rua) |

> The Astra direct-policy entry ranked above all 40 public policies at the time. See Critiques for leaderboard entries that did not survive retesting.

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

> Independent third party, but no VLA baseline.

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
| [Embo-Harness](#embo-harness) | 2026-11-23 | GPT-6-Astra, GPT-6.1-Sol, GPT-6.1-Terra | direct | analytic (IK / waypoints / scripted) | sim+real | RoboLab-120 SR/Score metrics (sim); real-world judge not stated |
| [ACAP](#acap) | 2026-11-23 | Astra (lead xhigh, members medium; paper does not give the full model name) | agentic / code | analytic (IK / waypoints / scripted) | real | human annotators with task-specific rubrics (physical progress, completion); operators monitor safety |
| [Real2Worlds2Real](#real2worlds2real) | 2026-11-23 | GPT-6 Astra | self-improving | trained by the agent | sim+real | real: not stated; LIBERO-Pro: benchmark checker on 50 held-out initial states |
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

<details open><summary><b>10 entries</b> + 14 cross-listed</summary>

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

</details>

<a id="agentic"></a>
## 🧑‍💻 Agentic & Code-Writing Policies

*The model acts through a harness: it writes and runs code against sensing/perception/motion APIs, observes the outcome, and repairs. Learned System 1 is absent; motion is analytic (IK, waypoints, ROS).*

<details open><summary><b>19 entries</b> + 21 cross-listed</summary>

<a id="acap"></a>
- **[ACAP: Asynchronous Coding Agents for Efficient Robot Control](https://arxiv.org/abs/2611.31205)**
  S-Lab, Nanyang Technological University; University of Oxford; ACE Robotics · *Paper* · 2026-11-23 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.31205)] [[Project](https://projects.zxhezexin.com/acap)]  
  Splits a robot across asynchronous coding agents per control group, coordinated by a lead hyper-agent, on Galaxea R1 Pro and AgileX PiPER robots. 'Across 72 real-world rollouts covering 25 task/platform settings, ACAP reduces task-balanced time cost by 28.2% compared with a single-agent Direct Policy'; on repeated trials it lowers mean 30-min-capped cost on all six tasks (−29.4%), and on Collaborative tasks 'ACAP completes ten of ten runs, compared with eight for Direct and three for Fixed.'  
  <sub>**Model:** Astra (lead xhigh, members medium; paper does not give the full model name) · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** One robot run as a team of persistent coding agents: each member owns a control group (arm+gripper, torso+chassis) and runs its own observe–reason–code–execute loop issuing end-effector/joint targets; a lead 'hyper-agent' assigns work, sets event-based waits, and can take over groups for coupled actions under exclusive control ownership · **Eval:** real · **Judged by:** human annotators with task-specific rubrics (physical progress, completion); operators monitor safety · **Trials:** task-coverage: 72 rollouts over 25 task/platform settings; repeated-trial: 90 rollouts (6 tasks x 5 trials x 3 policies) · **Speed/cost:** task-balanced mean 13.67 min (ACAP) vs 19.04 min (Direct) per task over 25 settings</sub>  
  ⚠️ <sub>Authors: 'The current framework does not include a dedicated motion-level collision-checking layer.' Evaluation is about time cost vs. the authors' own single-agent and fixed-delegation baselines; no learned-policy (VLA) comparison. Progress is human-annotated; operators monitor safety. The model is named only as 'Astra'. Releases a real-world rollout dataset.</sub>  
  <sub>↪ also in: [Making It Fast & Cheap](#fast)</sub>

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
  On five real multi-arm tasks with up to three heterogeneous robots, 'CoEx reaches 70% average success, against 50% for the same system without the code agent'; a π0.5 policy fine-tuned on agent-generated rollouts is also reported.  
  <sub>**Model:** Claude Code (code agent), GPT-5.6 Sol (planner) · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Claude Code writes a complete multi-arm program, runs it in a real-to-sim digital twin and refines it against privileged-state checks, checkpoint predicates and rendered views; verified joint trajectories are replayed on hardware after collision checks · **Eval:** sim+real · **Judged by:** twin verifier (privileged state) during exploration; task milestones on the real robots · **Trials:** 10 per agent per task, 5 real tasks</sub>  
  ⚠️ <sub>Authors: 'Real-world execution is open-loop replay, so residual pose offsets remain a main source of failure'; programs query privileged simulator state; rigid objects, fixed bases, static scenes; evaluation is modest in scale.</sub>  
  <sub>↪ also in: [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="cap-x"></a>
- **[CaP-X: A Framework for Benchmarking and Improving Coding Agents for Robot Manipulation](https://arxiv.org/abs/2603.22435)**
  UC Berkeley · NVIDIA · Stanford · CMU · *Paper* · 2026-03-23 · `💻 code / results` · 🏷️ ICML 2026 (per catalogs)  
  [[Paper](https://arxiv.org/abs/2603.22435)] [[Project](https://capgym.github.io/)] [[Code](https://github.com/capgym/cap-x)] ![stars](https://img.shields.io/github/stars/capgym/cap-x?style=flat-square&label=%E2%98%85)  
  CaP-Gym environment + CaP-Bench. Finding: performance rises with human-crafted abstractions and falls as they are removed, but scaling agentic test-time compute (multi-turn, execution feedback, visual differencing, skill synthesis) closes much of the gap. Introduces training-free CaP-Agent0 and CaP-RL (RL with verifiable rewards, sim→real).  
  <sub>**Model:** 12 models incl. Gemini 3 Pro, GPT-5.2, Claude Opus 4.5 · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Programs that compose perception and control primitives at varying abstraction levels (CaP-Gym) · **Eval:** sim+real · **Judged by:** benchmark checkers</sub>  
  ⚠️ <sub>Authors propose a hybrid in which agents handle logic and recovery while VLAs handle fine motor control.</sub>  
  <sub>↪ also in: [Benchmarks & Evaluation Reports](#benchmarks), [Analyses, Critiques & Reproducibility](#critiques)</sub>

<a id="unimanip"></a>
- **[UniManip: Open-World Robotic Manipulation via Agentic Operational Graphs](https://arxiv.org/abs/2602.13086)**
  Nanyang Technological University · *Paper* · 2026-02-13 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2602.13086)] [[Project](https://henryhcliu.github.io/unimanip)]  
  A small general VLM orchestrates an explicit operational graph with closed-loop verification and recovery. It reaches 0.83 task success in cluttered scenes (RoboEXP 0.39, no-graph variant 0.40) and 0.94 on the VLA benchmark vs 0.71 for the strongest baseline. On LIBERO-Pro it scores 0.77/0.85 on Object Pos/Task, against π0.5's 0.17/0.01.  
  <sub>**Model:** Qwen3-VL-4B · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** A VLM builds and updates an Agentic Operational Graph over tool calls; a scene graph supplies affordances and a safety-aware planner synthesises collision-free trajectories; the VLM verifies outcomes and repairs locally or replans · **Eval:** sim+real · **Judged by:** benchmark checkers (sim); trial success criterion on hardware (object in receptacle, no e-stop or intervention) · **Trials:** 10 trials per task and method on the Galaxea A1 (80 in clutter); 15–20 per task in cross-embodiment tests</sub>  
  ⚠️ <sub>Authors: failures are dominated by grasping (0.16 of all trials, from single-view depth noise) and embodiment kinematics. π0.5 beats it on LIBERO-Pro Goal Pos (0.38 vs 0.33).</sub>  

<a id="faea"></a>
- **[Demonstration-Free Robotic Control via LLM Agents](https://arxiv.org/abs/2601.20334)**
  — · *Paper* · 2026-01-28 · `📄 peer-reviewed` · 🏷️ IROS 2026  
  [[Paper](https://arxiv.org/abs/2601.20334)]  
  Frontier Agent as Embodied Agent: 84.9% LIBERO, 85.7% ManiSkill3, 96% MetaWorld, approaching VLAs trained on fewer than 100 demos per task, with zero demonstrations. One round of human feedback raises LIBERO to 88.2%.  
  <sub>**Model:** Claude Agent SDK (unmodified) · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** Software-engineering agent loop applied unchanged to manipulation · **Eval:** sim · **Judged by:** benchmark checkers</sub>  
  ⚠️ <sub>Uses privileged environment state. Authors scope the claim to 'tasks dominated by deliberative, task-level planning'.</sub>  

<a id="alrm"></a>
- **[ALRM: Agentic LLM for Robotic Manipulation](https://arxiv.org/abs/2601.19510)**
  TII · *Paper* · 2026-01-27 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2601.19510)] [[Project](https://tiiuae.github.io/ALRM/)]  
  Agentic framework plus a 56-task simulation benchmark with linguistically varied instructions. Claude-4.1-Opus is the top closed model under both modes.  
  <sub>**Model:** 10 LLMs; best closed: Claude-4.1-Opus; best open: Falcon-H1-7B · **Below it:** analytic (IK / waypoints / scripted) · **Interface:** ReAct loop in two modes: Code-as-Policy (writes control code) and Tool-as-Policy (iterative tool calls) · **Eval:** sim · **Judged by:** benchmark checkers</sub>  
  <sub>↪ also in: [Benchmarks & Evaluation Reports](#benchmarks)</sub>

**Cross-listed here:**

- ↪ **[Real2Worlds2Real](#real2worlds2real)**: Real2Worlds2Real: Scaling Self-Improving Agentic Real2Sim2Real for Robot Manipulation <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[Astra on Codex (Robocurve)](#codex-vs-inspect-robots)**: Why is Astra better on Codex for robotics? <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[Contact Harness](#contact-harness)**: Contact Harness: Enabling VLM Agents to Perform Contact-Rich Manipulation <sub>(listed under [Frontier Model as Direct Policy](#direct))</sub>
- ↪ **[Waddle-1](#waddle-1)**: Waddle-1: a robot-use agent that directs local lower-level policies <sub>(listed under [Frontier Model over a Learned System 1 / System 0](#orchestrated))</sub>
- ↪ **[γ-Scape](#gamma-scape)**: $γ$-Scape: An Agent-Centric World for Mobile Embodied Intelligence <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[EmbodyAgent](#embodyagent)**: EmbodyAgent: Post-Training Embodied VLM Agents via Distillation, SFT, and RL <sub>(listed under [Making It Fast & Cheap](#fast))</sub>
- ↪ **[UniCraft](#unicraft)**: Alignment Drives Reuse: Learning Generalizable Robot-Use Agents from Heterogeneous Experience <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[RoboTeam](#roboteam)**: RoboTeam: Benchmarking Vision-Based Multi-Agent Control of Many Robot Arms in Real Time <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[JustRUA](#justrua)**: JustRUA: A Controlled Study of GPT-6 Robot-Use Agents <sub>(listed under [Analyses, Critiques & Reproducibility](#critiques))</sub>
- ↪ **[uni-robot-agent](#democratizing-rua)**: Democratizing Robot-Use Agents: A Unified Harness with Open Models <sub>(listed under [Making It Fast & Cheap](#fast))</sub>
- ↪ **[SO-101 Bench](#so101-bench)**: SO-101 Bench: Accessible Spatial Manipulation <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[Recursia](#recursia)**: Learning to Compose: Recursive Self-Improvement of Shared Executable Stacks for Zero-Shot Long-Horizon Robot Manipulation <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[SCOPE](#scope-program-edits)**: SCOPE: Selective Certification of Program Edits for Embodied Heuristic Learning <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[Astranomy](#astranomy)**: Astranomy: An Empirical Study of GPT-6 Astra as a Native Robot Policy <sub>(listed under [Frontier Model as Direct Policy](#direct))</sub>
- ↪ **[LADDER](#ladder)**: LADDER: A Long-Horizon Robot Manipulation Benchmark <sub>(listed under [Benchmarks & Evaluation Reports](#benchmarks))</sub>
- ↪ **[Real2Gym](#real2gym)**: Real2Gym: Building Gyms from Videos, Bringing Skills to Robots <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[HuGo](#hugo)**: HuGo: LLMs as Whole-Body Policy Code Designers for Humanoid Loco-Manipulation <sub>(listed under [Frontier Model over a Learned System 1 / System 0](#orchestrated))</sub>
- ↪ **[GPT-Policy](#gpt-policy)**: In-Context Robot Learning with VLM Agents <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[EMERGE-Policy](#emerge-policy)**: EMERGE-Policy: A Robot Mind Emerges Beyond a Single Policy <sub>(listed under [Frontier Model over a Learned System 1 / System 0](#orchestrated))</sub>
- ↪ **[ASPIRE](#aspire)**: ASPIRE: Agentic /Skills Discovery for Robotics <sub>(listed under [Getting Better Without Weight Updates](#self-improving))</sub>
- ↪ **[NovaPlan](#novaplan)**: NovaPlan: Zero-Shot Long-Horizon Manipulation via Closed-Loop Video Language Planning <sub>(listed under [Frontier Model over a Learned System 1 / System 0](#orchestrated))</sub>

</details>

<a id="orchestrated"></a>
## 🎛️ Frontier Model over a Learned System 1 / System 0

*The general model supervises, steers, or edits the output of a learned low-level controller (a VLA, a world-action model, or a whole-body tracker). This is where the 'is System 1 still needed?' question is decided.*

<details open><summary><b>12 entries</b> + 9 cross-listed</summary>

<a id="waddle-1"></a>
- **[Waddle-1: a robot-use agent that directs local lower-level policies](https://waddlelabs.ai/research/introducing-waddle)**
  Waddle Labs · *Project* · 2026-11-20 · `💬 post only`  
  [[Project](https://waddlelabs.ai/research/introducing-waddle)] [[Data](https://robocurve.org/)]  
  Announced on X as Waddle Labs' first robot-use agent, controlling bimanual robots zero-shot on unseen tasks. Robocurve measures it at 81.4% on RoboDojo-RC Tier 1, the top score, ahead of GPT-6.2 Astra (65.7%) and the Dream-1 world action model (59.5%). A System 2 over System 1 design: 'agents that combine the capability of reasoning models and the efficiency of reactive policies'.  
  <sub>**Model:** a set of cloud LLMs (not named) · **Below it:** frozen learned policy · **Interface:** Cloud LLMs decompose the goal, write control code and call lower-level policies that run locally on the robot; skills go into a shared library · **Eval:** real · **Judged by:** Robocurve human grader (not blinded) · **Trials:** 120 attempts (RoboDojo-RC Tier 1) · **Speed/cost:** 7.4 min per attempt (Robocurve); $2.46 per attempt at a planned $20/hr</sub>  
  ⚠️ <sub>Robocurve: a 'full system' with 'one chat per task, a 10-minute limit and no call cap', while single LLMs get 40 model calls, so not like-for-like. LLMs and the lower-level policy type are not disclosed; no paper. Preview API by request.</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic)</sub>

<a id="trip-tripwire"></a>
- **[Tripwire: Robot Agents that Program Their Own Interrupts under Human Disturbance](https://arxiv.org/abs/2611.27182)**
  University of Massachusetts Amherst · *Paper* · 2026-11-20 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.27182)]  
  Event-driven harness where the agent writes its own interrupt programs while a pretrained policy runs. On RoboHD (168 RoboCasa365 scenes with a reactive human avatar), with Xiaomi-Robotics-1 'TRIP halves the rate of human contact with the strongest policy, raising safety from 61.3% to 81.3%, without sacrificing task success (38.7% vs. 31.0%)' versus a turn-based harness with the same agent. Real robot (xArm 7, π0.5): 'TRIP succeeds in 25 of 40 trials across two disturbance conditions … compared with 5 of 40 for the turn-based harness and 1 of 40 for the policy alone.'  
  <sub>**Model:** GPT-6.1-sol, GPT-6 Astra, Claude Opus 5.5, Qwen3.5-9B (tripwire VLM) · **Below it:** frozen learned policy · **Interface:** The agent calls a frozen VLA/WAM (or direct base/arm/gripper commands) and attaches a 'tripwire': a sandboxed, stateful Python monitor run every control step that can query a compact VLM (Qwen3.5-9B) plus depth and timers, and halts the call and wakes the agent with a reason when it fires · **Eval:** sim+real · **Judged by:** RoboCasa365 task check + geometric capsule-box human-contact check (sim); task outcome with no contact with the person (real) · **Trials:** sim: 168 RoboHD scenes x 1 episode per method/policy (+ same scenes without person); real: 2 tasks x 10 setups x 3 conditions per method · **Speed/cost:** real robot: tripwire check 0.24 s avg vs agent turn 4.3 s avg; sim pauses physics, ~12 min wall-clock per 1.5 min robot time; '$0.2–0.3 in API calls' per TRIP episode with GPT-6.1-sol; spend cap $0.40/episode</sub>  
  ⚠️ <sub>Authors: 'The person is simulated: an avatar that plays motion-capture clips under a scripted controller, with no collision body.' 'The physics pauses while the agent and the tripwire’s VLM compute, so the robot’s time excludes their latency.' 'Due to high (10×) API costs, only Xiaomi-Robotics is tested with the current state-of-the-art agentic model, GPT-6 Astra.' Real-robot disturber is one of the authors; base policies are single-task π0.5 trained on 100 demos each. Claude Opus 5.5 (40-scene supplement) touched the person in 17/40 vs 9/40 for GPT-6.1-sol.</sub>  
  <sub>↪ also in: [Making It Fast & Cheap](#fast)</sub>

<a id="reasoning-on-call"></a>
- **[Reasoning on Call: Efficient Agentic Robot Control for Long-Horizon Robot Manipulation](https://arxiv.org/abs/2611.26341)**
  Wuhan University / Zhongguancun Academy / Samsung · *Paper* · 2026-11-19 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.26341)]  
  Event-triggered frontier-agent intervention over a world-action-model policy. On RMBench, 99.6% average success vs 75.6% for GPT-as-Policy and 71.9% for Direct Control, using 65.3% fewer tokens than GPT-as-Policy; 98.1% vs 83.0% for MemoryWAM, the strongest policy-only baseline. Real robot: 73.3% vs 30.0% for the policy alone.  
  <sub>**Model:** GPT-6.1 Sol (xhigh), FastWAM (low-level) · **Below it:** frozen learned policy · **Interface:** A trained task-state monitor triggers the agent only on events; the agent approves a prefix of the FastWAM action chunk, makes local EEF/gripper corrections, takes over directly, or revises the next subtask · **Eval:** sim+real · **Trials:** RMBench 9 tasks (30 trials/task vs agents, 100 vs policies); real SO-ARM101: 3 tasks × 10 trials · **Speed/cost:** monitor 2.77 Hz overall; 288.3 tokens/episode vs 830.3 (GPT-as-Policy) and 1845.1 (Direct Control) on RMBench</sub>  
  ⚠️ <sub>Authors: failures are mostly difficult grasps that agent intervention can't rescue, 'highlighting agent capability as a remaining bottleneck'. Agent baselines use GPT-6 Astra while RoC uses GPT-6.1 Sol. The agent model on the real robot is not stated.</sub>  
  <sub>↪ also in: [Making It Fast & Cheap](#fast)</sub>

<a id="interactvla"></a>
- **[InteractVLA: Turning VLAs into Interactive Tools for Agentic Robotic Manipulation](https://arxiv.org/abs/2611.22584)**
  — · *Paper* · 2026-11-17 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2611.22584)] [[Project](https://lingwupro.github.io/InteractVLA/)]  
  Instead of treating the VLA as an opaque language-only primitive, makes System 1 geometrically steerable and inspectable by the agent. Reports 99.4% LIBERO-Plus, 48.62% RoboDojo, and 89.4% RoboCasa365, with recursive self-improvement.  
  <sub>**Model:** vision-language agent · **Below it:** frozen learned policy · **Interface:** Two-way geometric interface: agent-specified EEF targets steer a flow-based VLA via test-time gradient guidance; generated action chunks and reprojections are shown back to the agent · **Eval:** sim · **Judged by:** benchmark checkers</sub>  
  <sub>↪ also in: [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="atlas"></a>
- **[ATLAS: Agentic Harness for Whole-Body Intelligence from Human Video](https://atlas-humanoid.github.io/)**
  UC Berkeley · NVIDIA · HKU · Stanford · *Project* · 2026-11-13 · `💬 post only` · 🏷️ Best Demo, CoRL 2026 Agentic Robotics Workshop  
  [[Project](https://atlas-humanoid.github.io/)]  
  Humanoid whole-body tasks from one human video, no robot demos or task-specific sim training. Real trash pickup goes from 0% to 88% (last 8 attempts) within 38 attempts. In Isaac Lab, online model-based RL reaches 83% apple lift vs 58% bias estimator / 13% model-free RL / 4% no learner.  
  <sub>**Model:** VLM agent (unnamed on page) · **Below it:** frozen learned policy · **Interface:** Agent writes a task spec once from 1 human video + 1 prompt; harness edits the end-effector reach; frozen ScaleBFM whole-body tracker (System 0) follows the edited motion; a fast learner adds a residual · **Eval:** sim+real · **Judged by:** authors · **Trials:** 38 real attempts (trash pickup)</sub>  
  ⚠️ <sub>Project page only (no paper link yet); the VLM is not named. Date is from the announcement post.</sub>  
  <sub>↪ also in: [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="harnesspai"></a>
- **[HarnessPAI: An Evolving Harness for Physical AI](https://arxiv.org/abs/2609.29166)**
  — · *Paper* · 2026-09-24 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2609.29166)] [[Project](https://darwin-agent.github.io/HarnessPAI/)]  
  Argues that the action-model training recipe erodes perception and reasoning. Works across arms, household robots, a robot vacuum, and a legged agent. The converged programs also become cheap expert data for fine-tuning VLAs and WAMs.  
  <sub>**Below it:** frozen learned policy · **Interface:** Code as the evolvable interface that organizes underlying action primitives: open-loop program within a rollout, closed-loop evolution across rollouts · **Eval:** sim+real</sub>  
  <sub>↪ also in: [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="hugo"></a>
- **[HuGo: LLMs as Whole-Body Policy Code Designers for Humanoid Loco-Manipulation](https://arxiv.org/abs/2609.30594)**
  UC Berkeley · *Paper* · 2026-09-24 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2609.30594)] [[Project](https://iconlab.negarmehr.com/HuGo/)]  
  An LLM writes the high-level policy as code on top of a frozen whole-body controller for a Unitree G1, with no rewards or demonstrations, and refines it from its own rollouts. Best-of-N selection lifts the mean success rate across five tasks and two low-level policies 'from 43.9% to 79.1% from N=1 to N=10'. The best policies transfer zero-shot to hardware at 93.3% (PBT) and 66.7% (LBX), and refinement on hardware raises the worst-transferring policy from 20% to 90%.  
  <sub>**Model:** gpt-5.4 · **Below it:** frozen learned policy · **Interface:** The LLM writes closed-loop high-level policy code that reads numeric observations every timestep and outputs commands to a frozen whole-body tracking policy (rl_isaac at 50 Hz, sonic at 10 Hz); it refines the code from rollout trajectories and video frames · **Eval:** sim+real · **Judged by:** simulator task checks; hardware trials on a Unitree G1 · **Trials:** 100 held-out initial states per task in sim; 15 hardware trials per policy; 10 trials per hardware refinement candidate · **Speed/cost:** code runs at the controller rate; obtaining a policy takes a few hours, mostly simulated rollouts; ≈$1.1 per generated and refined policy, ≈$11 for best-of-10</sub>  
  ⚠️ <sub>Single generated policies vary widely, so best-of-10 selection is needed. The LLM misdiagnoses contact failures on the box-lifting task without a geometry hint. Observations are numeric state (motion capture on hardware), not images. Neither low-level policy maintains grasp force.</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic), [Getting Better Without Weight Updates](#self-improving)</sub>

<a id="emerge-policy"></a>
- **[EMERGE-Policy: A Robot Mind Emerges Beyond a Single Policy](https://arxiv.org/abs/2608.29896)**
  — · *Paper* · 2026-08-30 · `💻 code / results`  
  [[Paper](https://arxiv.org/abs/2608.29896)] [[Project](https://emerge-policy.github.io/EMERGE-Policy/)] [[Code](https://github.com/EMERGE-Policy/EMERGE-Policy)] ![stars](https://img.shields.io/github/stars/EMERGE-Policy/EMERGE-Policy?style=flat-square&label=%E2%98%85)  
  Treats models, including action models, as skills called inside a multi-agent orchestration, with verification and branch-stack recovery. No additional fine-tuning.  
  <sub>**Below it:** frozen learned policy · **Interface:** Graph of a main agent plus sub-agents (perception, monitoring, verification, memory); heterogeneous model backends exposed as Operational / Imagination / Evaluation skills · **Eval:** sim+real</sub>  
  <sub>↪ also in: [Agentic & Code-Writing Policies](#agentic)</sub>

<a id="gemini-robotics-2"></a>
- **[Gemini Robotics 2 brings whole-body intelligence to robots](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/)**
  Google DeepMind · *Blog* · 2026-07-30 · `💬 post only`  
  [[Post](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/)]  
  Whole-body humanoid control. Reported success includes 74.2% general pick-and-place and 89.6% precise insertion on Franka Duo, and 36–92% on multi-finger tasks, which the page says 'remains challenging'. On-Device 2 adapts to new bi-arms with fewer than 200 examples.  
  <sub>**Model:** Gemini Robotics ER 2, Gemini Robotics 2 (VLA), Gemini Robotics On-Device 2 · **Below it:** jointly trained · **Interface:** ER 2 plans, monitors, and coordinates; the VLA emits motor commands; an on-device VLA runs locally · **Eval:** real</sub>  
  ⚠️ <sub>Vendor blog; numbers not independently reproduced.</sub>  
  <sub>↪ also in: [The Incumbent: Dual-System VLAs](#dual-system)</sub>

<a id="harness-vla"></a>
- **[Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents](https://arxiv.org/abs/2607.08448)**
  — · *Paper* · 2026-07-09 · `📝 preprint`  
  [[Paper](https://arxiv.org/abs/2607.08448)] [[Project](https://harnessvla.github.io/)]  
  Keeps a learned System 1 only for the local contact-rich phases and lifts everything else to the planner. +38.6 pp on LIBERO-Pro and +25.4 pp on RoboCasa365 over the strongest baselines; 58.4% on RoboTwin C2R; real dual-Franka demos.  
  <sub>**Model:** LLM coding agent · **Below it:** frozen learned policy · **Interface:** Frozen VLA exposed as a retryable contact-rich primitive, plus analytic primitives for grounding, staging, transport, and release · **Eval:** sim+real · **Judged by:** benchmark checkers</sub>  
  ⚠️ <sub>AMP1 notes that orchestration methods like this are capped by the reliability of the VLA they delegate to.</sub>  

<a id="novaplan"></a>
- **[NovaPlan: Zero-Shot Long-Horizon Manipulation via Closed-Loop Video Language Planning](https://arxiv.org/abs/2602.20119)**
  Robotics and AI Institute · CMU · Brown · UPenn · UIUC · Harvard · *Paper* · 2026-02-23 · `📄 peer-reviewed` · 🏷️ C