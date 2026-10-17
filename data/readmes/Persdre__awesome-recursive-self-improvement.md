<h1 align="center">Awesome Recursive Self-Improvement</h1>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-CC0--1.0-blue.svg" alt="License: CC0-1.0"></a>
  <a href="https://github.com/Persdre/awesome-recursive-self-improvement/commits/main"><img src="https://img.shields.io/github/last-commit/Persdre/awesome-recursive-self-improvement" alt="Last commit"></a>
</p>

<p align="center"><sub>A <b>definition-first</b> curated list of papers, systems, and resources on recursive self-improvement (RSI) in AI, organized by <i>what is modified</i> × <i>degree of loop closure</i>.</sub></p>

"RSI" gets used for everything from prompt tweaking to intelligence-explosion scenarios, and most collections mix them freely. This list starts from the definitions and tags every entry, so you always know *what kind* of self-improvement a work actually does.

<p align="center">
  <img src="assets/taxonomy.svg" alt="A taxonomy of recursive self-improvement: what is modified × degree of loop closure" width="90%">
</p>

> [!NOTE]
> **How entries are tagged.** Two axes resolve the definitional mess:
>
> - **What is modified**: 🧠 **weights** (the model itself) · 🔧 **code** (the agent's own scaffold/tools) · 📝 **memory** (prompts, experience, skills) · 🧬 **artifacts** (external programs, algorithms, rewards) · 🔬 **research** (the research process itself)
> - **Loop closure**: **L1** human-in-the-loop · **L2** self-improves, humans gate/evaluate rounds · **L3** fully closed loop / open-ended
>
> The frontier cell (🔬 research × L3: systems improving the very process that improves them) is RSI in the strong, intelligence-explosion sense. Everything else here is a step on the spectrum toward it.

## Contents

- [🔥 Start Here](#-start-here)
- [What Counts as RSI?](#what-counts-as-rsi)
- [Foundations & Theory](#foundations--theory)
- [Weight-Level Self-Improvement 🧠](#weight-level-self-improvement-)
- [Scaffold & Code-Level Self-Evolution 🔧](#scaffold--code-level-self-evolution-)
- [Prompt, Memory & Experience 📝](#prompt-memory--experience-)
- [Open-Ended & Evolutionary Methods 🧬](#open-ended--evolutionary-methods-)
- [Automated AI Research 🔬](#automated-ai-research-)
- [Safety, Alignment & Governance](#safety-alignment--governance)
- [Benchmarks & Evaluation](#benchmarks--evaluation)
- [Surveys & Position Papers](#surveys--position-papers)
- [Talks, Blogs & Communities](#talks-blogs--communities)
- [Contributing](#contributing)

## 🔥 Start Here

Eight works that span the whole spectrum; read these and you know the field:

- [1965] **Speculations Concerning the First Ultraintelligent Machine**: I. J. Good coins the intelligence explosion. [[paper](https://languagelog.ldc.upenn.edu/myl/Good1964.pdf)]
- [2003] **Gödel Machines**: Schmidhuber's provably-optimal self-rewriter, the theoretical north star. [[paper](https://arxiv.org/abs/cs/0309048)]
- [2022] **STaR**: the modern weight-level bootstrap (reason, filter, retrain, repeat). [[paper](https://arxiv.org/abs/2203.14465)] [[code](https://github.com/ezelikman/STaR)]
- [2023] **STOP**: code that improves code that improves code, with a frozen model. [[paper](https://arxiv.org/abs/2310.02304)] [[code](https://github.com/microsoft/stop)]
- [2024] **The AI Scientist**: the research process itself, automated end-to-end. [[paper](https://arxiv.org/abs/2408.06292)] [[code](https://github.com/SakanaAI/AI-Scientist)]
- [2025] **Darwin Gödel Machine**: agents rewriting their own code inside an open-ended evolutionary archive. [[paper](https://arxiv.org/abs/2505.22954)] [[code](https://github.com/jennyzzt/dgm)]
- [2025] **AlphaEvolve**: evolutionary search over programs producing new SOTA algorithms. [[paper](https://arxiv.org/abs/2506.13131)] [[blog](https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)]
- [2026] **Bounded Self-Refinement vs. Open-Ended RSI**: the survey that separates industrial self-refinement from RSI proper. [[paper](https://arxiv.org/abs/2607.07663)]

## What Counts as RSI?

Almost nobody means the same thing by "recursive self-improvement": of the eight key sources below, **only two use the word "recursive" at all**. Expand each to see how they disagree on what improves, who does the improving, and how closed the loop is.

<details>
<summary><b>Gödel Machine</b> (Schmidhuber, 2003): rewrites any part of its own code once it can <i>prove</i> the rewrite helps</summary>

- **What improves:** the solver's entire source code, including the proof searcher itself
- **Who improves it:** the machine itself, via self-referential proof search
- **Loop closure:** fully closed in theory; rewrites happen only after a proof of usefulness
- **Says "recursive"?** No; uses "self-referential" and "self-improvement"

> A universal problem solver that rewrites any part of its own code as soon as it finds a proof that the rewrite increases expected utility. [[paper](https://arxiv.org/abs/cs/0309048)]
</details>

<details>
<summary><b>I. J. Good</b> (1965): ultraintelligent machines designing still better machines, the intelligence explosion</summary>

- **What improves:** machine design / intelligence itself
- **Who improves it:** an ultraintelligent machine designing successor machines
- **Loop closure:** closed in principle (speculative); each generation designs the next
- **Says "recursive"?** No; coins "intelligence explosion"

> An ultraintelligent machine could design still better machines; machine design being an intellectual activity, this yields an intelligence explosion. [[paper](https://languagelog.ldc.upenn.edu/myl/Good1964.pdf)]
</details>

<details>
<summary><b>Yampolskiy</b> (2015): self-improving software where each improvement raises the capacity for further improvement</summary>

- **What improves:** the software's own code and capabilities
- **Who improves it:** the software autonomously (seed AI)
- **Loop closure:** analyzes fully closed loops; argues hard limits (RSI Convergence Theory)
- **Says "recursive"?** **Yes**: "Recursively Self-Improving software", with formal definitions

> Software that improves itself, where each improvement raises its capacity for further improvement, subject to computational and convergence limits. [[paper](https://arxiv.org/abs/1502.06512)]
</details>

<details>
<summary><b>Darwin Gödel Machine</b> (2025): agents empirically rewriting their own codebase inside an evolutionary archive</summary>

- **What improves:** the coding agent's own codebase (scaffold, tools, workflows)
- **Who improves it:** FM-powered agents modify their own code; archive + benchmarks select variants
- **Loop closure:** largely closed; empirical validation replaces proofs; safety sandboxing retained
- **Says "recursive"?** No; uses "self-improving" and "open-ended evolution"

> An agent that repeatedly modifies its own code (thereby also improving its ability to modify its own codebase), validated empirically within an evolutionary archive. [[paper](https://arxiv.org/abs/2505.22954)]
</details>

<details>
<summary><b>SEAL</b> (2025): an LLM generating its own finetuning data and update directives for persistent weight updates</summary>

- **What improves:** model weights, via persistent finetuning updates
- **Who improves it:** the model generates its own "self-edits"; an RL outer loop rewards them
- **Loop closure:** partially closed; self-generated updates inside a human-designed harness
- **Says "recursive"?** No; uses "self-adapting" and "self-edits"

> An LLM that self-adapts by generating its own finetuning data and update directives, yielding persistent weight updates rewarded by downstream performance. [[paper](https://arxiv.org/abs/2506.10943)]
</details>

<details>
<summary><b>Self-Evolving Agents Survey</b> (2025): agents continually adapting model, memory, tools, and architecture</summary>

- **What improves:** agent components: model, memory, tools, architecture
- **Who improves it:** the agent itself, via intra/inter-test-time adaptation
- **Loop closure:** varies by method; a spectrum of feedback from data, interactions, experience
- **Says "recursive"?** No; uses "self-evolving", framed as the path toward ASI

> Self-evolving agents continually adapt their models, memory, tools, and architecture from interaction and experience, moving beyond static LLMs. [[paper](https://arxiv.org/abs/2507.21046)]
</details>

<details>
<summary><b>Self-Improvements in Modern Agentic Systems</b> (2026): a "self-induced update operator" over parameters or scaffold</summary>

- **What improves:** model parameters or scaffold components (prompts, memory, tools, control logic)
- **Who improves it:** the agent, via a "self-induced update operator"
- **Loop closure:** explicit experience→update→capability loop with minimal human intervention
- **Says "recursive"?** No; uses "self-improvement"

> Self-improvement is a self-induced update operator committing updates to model parameters or scaffold components, converting experience into capability gains. [[paper](https://arxiv.org/abs/2607.13104)]
</details>

<details>
<summary><b>Bounded Self-Refinement vs. Open-Ended RSI</b> (2026): loop closure as the axis separating self-refinement from RSI proper</summary>

- **What improves:** four targets: deployment behavior, training policy, the evaluator, or the research process itself
- **Who improves it:** a spectrum from human-in-the-loop to fully autonomous systems
- **Loop closure:** treated as the defining axis; every loop claims some signal can substitute for human judgment
- **Says "recursive"?** **Yes**: "recursive self-improvement" is the framing term

> Distinguishes bounded self-refinement (convergent, evaluable, industrial practice) from open-ended RSI, which remains bounded by grounding, collapse dynamics, and compute. [[paper](https://arxiv.org/abs/2607.07663)]
</details>

---

## Foundations & Theory

The classical line: from Good's intelligence explosion through Schmidhuber's provably-optimal self-rewriters, to formal arguments about the limits of RSI.

| Year | Venue | Paper | Code | Tags |
|---|---|---|---|---|
| 2024 | ICLR 2025 | [Mind the Gap: Examining the Self-Improvement Capabilities of Large Language Models](https://arxiv.org/abs/2412.02674) | — | 🧠 weights |
| 2023 | ICLR 2024 | [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798) | — | 📝 memory |
| 2016 | AGI 2016 | [Self-Modification of Policy and Utility Function in Rational Agents](https://arxiv.org/abs/1605.03142) | — | 🔧 code |
| 2015 | AGI 2015 | [On the Limits of Recursively Self-Improving AGI](https://link.springer.com/chapter/10.1007/978-3-319-21365-1_40) | — | 🔬 research |
| 2015 | arXiv | [From Seed AI to Technological Singularity via Recursively Self-Improving Software](https://arxiv.org/abs/1502.06512) | — | 🔧 code |
| 2013 | MIRI | [Intelligence Explosion Microeconomics](https://intelligence.org/files/IEM.pdf) | — | 🔬 research |
| 2011 | arXiv | [POWERPLAY: Training an Increasingly General Problem Solver by Continually Searching for the Simplest Still Unsolvable Problem](https://arxiv.org/abs/1112.5309) | — | 🔧 code · L3 |
| 2010 | J. Consciousness Studies | [The Singularity: A Philosophical Analysis](https://consc.net/papers/singularity.pdf) | — | — |
| 2008 | AGI 2008 | [The Basic AI Drives](https://selfawaresystems.com/wp-content/uploads/2008/01/ai_drives_final.pdf) | — | — |
| 2003 | arXiv | [Gödel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements](https://arxiv.org/abs/cs/0309048) | — | 🔧 code · L3 |
| 1965 | Advances in Computers | [Speculations Concerning the First Ultraintelligent Machine](https://languagelog.ldc.upenn.edu/myl/Good1964.pdf) | — | — |

---

## Weight-Level Self-Improvement 🧠

The model's own parameters are updated using self-generated data, rewards, or curricula, from STaR-style bootstrapping to zero-data self-play.

| Year | Venue | Paper | Code | Tags |
|---|---|---|---|---|
| 2025 | arXiv | [Language Self-Play For Data-Free Training](https://arxiv.org/abs/2509.07414) | — | 🧠 weights · L3 |
| 2025 | ICLR 2026 | [R-Zero: Self-Evolving Reasoning LLM from Zero Data](https://arxiv.org/abs/2508.05004) | [code](https://github.com/Chengsong-Huang/R-Zero) | 🧠 weights · L3 |
| 2025 | ICLR 2026 | [SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning via Multi-Agent Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2506.24119) | [code](https://github.com/spiral-rl/spiral) | 🧠 weights · L3 |
| 2025 | NeurIPS 2025 | [Self-Adapting Language Models (SEAL)](https://arxiv.org/abs/2506.10943) | [code](https://github.com/Continual-Intelligence/SEAL) | 🧠 weights · L2 |
| 2025 | NeurIPS 2025 | [Absolute Zero: Reinforced Self-play Reasoning with Zero Data](https://arxiv.org/abs/2505.03335) | [code](https://github.com/LeapLabTHU/Absolute-Zero-Reasoner) | 🧠 weights · L3 |
| 2025 | NeurIPS 2025 | [TTRL: Test-Time Reinforcement Learning](https://arxiv.org/abs/2504.16084) | [code](https://github.com/PRIME-RL/TTRL) | 🧠 weights · L2 |
| 2025 | ICML 2025 | [rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking](https://arxiv.org/abs/2501.04519) | [code](https://github.com/microsoft/rStar) | 🧠 weights · L2 |
| 2024 | ICLR 2025 | [Self-Improvement in Language Models: The Sharpening Mechanism](https://arxiv.org/abs/2412.01951) | — | 🧠 weights · L2 |
| 2024 | EMNLP 2025 | [Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge](https://arxiv.org/abs/2407.19594) | — | 🧠 weights · L2 |
| 2024 | NeurIPS 2024 | [Self-playing Adversarial Language Game Enhances LLM Reasoning (SPAG)](https://arxiv.org/abs/2404.10642) | [code](https://github.com/Linear95/SPAG) | 🧠 weights · L2 |
| 2024 | COLM 2024 | [Quiet-STaR: Language Models Can Teach Themselves to Think Before Speaking](https://arxiv.org/abs/2403.09629) | [code](https://github.com/ezelikman/quiet-star) | 🧠 weights · L2 |
| 2024 | ACL 2024 | [Self-Distillation Bridges Distribution Gap in Language Model Fine-Tuning](https://arxiv.org/abs/2402.13669) | [code](https://github.com/sail-sg/sdft) | 🧠 weights · L2 |
| 2024 | COLM 2024 | [V-STaR: Training Verifiers for Self-Taught Reasoners](https://arxiv.org/abs/2402.06457) | — | 🧠 weights · L2 |
| 2024 | ICML 2024 | [Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020) | — | 🧠 weights · L2 |
| 2024 | ICML 2024 | [Self-Play Fine-Tuning Converts Weak Language Models to Strong Language Models (SPIN)](https://arxiv.org/abs/2401.01335) | [code](https://github.com/uclaml/SPIN) | 🧠 weights · L2 |
| 2023 | TMLR 2024 | [Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models (ReST-EM)](https://arxiv.org/abs/2312.06585) | — | 🧠 weights · L2 |
| 2023 | ICML 2024 | [RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Feedback with AI Feedback](https://arxiv.org/abs/2309.00267) | — | 🧠 weights · L2 |
| 2023 | arXiv | [Reinforced Self-Training (ReST) for Language Modeling](https://arxiv.org/abs/2308.08998) | — | 🧠 weights · L2 |
| 2022 | ACL 2023 | [Self-Instruct: Aligning Language Models with Self-Generated Instructions](https://arxiv.org/abs/2212.10560) | [code](https://github.com/yizhongw/self-instruct) | 🧠 weights · L2 |
| 2022 | arXiv | [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073) | — | 🧠 weights · L1 |
| 2022 | EMNLP 2023 | [Large Language Models Can Self-Improve (LMSI)](https://arxiv.org/abs/2210.11610) | — | 🧠 weights · L2 |
| 2022 | NeurIPS 2022 | [STaR: Bootstrapping Reasoning With Reasoning](https://arxiv.org/abs/2203.14465) | [code](https://github.com/ezelikman/STaR) | 🧠 weights · L2 |

---

## Scaffold & Code-Level Self-Evolution 🔧

Agents that rewrite their own code, tools, workflows, or harness: the lineage of the Gödel Machine made empirical.

| Year | Venue | Paper | Code | Tags |
|---|---|---|---|---|
| 2026 | arXiv | [MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems](https://arxiv.org/abs/2605.22794) | [code](https://github.com/hkgai-official/Moss) | 🔧 code · L3 |
| 2025 | arXiv | [Huxley-Gödel Machine: Human-Level Coding Agent Development by an Approximation of the Optimal Self-Improving Machine](https://arxiv.org/abs/2510.21614) | [code](https://github.com/metauto-ai/HGM) | 🔧 code · L3 |
| 2025 | arXiv | [EvoAgentX: An Automated Framework for Evolving Agentic Workflows](https://arxiv.org/abs/2507.03616) | [code](https://github.com/EvoAgentX/EvoAgentX) | 🔧 code · L2 |
| 2025 | arXiv | [Darwin Gödel Machine: Open-Ended Evolution of Self-Improving Agents](https://arxiv.org/abs/2505.22954) | [code](https://github.com/jennyzzt/dgm) | 🔧 code · L3 |
| 2025 | arXiv | [Alita: Generalist Agent Enabling Scalable Agentic Reasoning with Minimal Predefinition and Maximal Self-Evolution](https://arxiv.org/abs/2505.20286) | [code](https://github.com/CharlesQ9/Alita) | 🔧 code · L2 |
| 2025 | arXiv | [A Self-Improving Coding Agent (SICA)](https://arxiv.org/abs/2504.15228) | [code](https://github.com/MaximeRobeyns/self_improving_coding_agent) | 🔧 code · L3 |
| 2024 | ICLR 2025 | [AFlow: Automating Agentic Workflow Generation](https://arxiv.org/abs/2410.10762) | [code](https://github.com/FoundationAgents/AFlow) | 🔧 code · L2 |
| 2024 | ICLR 2025 | [AgentSquare: Automatic LLM Agent Search in Modular Design Space](https://arxiv.org/abs/2410.06153) | [code](https://github.com/tsinghua-fib-lab/AgentSquare) | 🔧 code · L2 |
| 2024 | ACL 2025 | [Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement](https://arxiv.org/abs/2410.04444) | [code](https://github.com/Arvid-pku/Godel_Agent) | 🔧 code · L3 |
| 2024 | ICLR 2025 | [Automated Design of Agentic Systems (ADAS)](https://arxiv.org/abs/2408.08435) | [code](https://github.com/ShengranHu/ADAS) | 🔧 code · L3 |
| 2024 | arXiv | [Symbolic Learning Enables Self-Evolving Agents](https://arxiv.org/abs/2406.18532) | [code](https://github.com/aiwaves-cn/agents) | 🔧 code · L2 |
| 2023 | COLM 2024 | [Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation](https://arxiv.org/abs/2310.02304) | [code](https://github.com/microsoft/stop) | 🔧 code · L3 |

---

## Prompt, Memory & Experience 📝

Improvement without touching weights or agent code: evolving prompts, accumulating skills, distilling experience into reusable memory.

| Year | Venue | Paper | Code | Tags |
|---|---|---|---|---|
| 2026 | arXiv | [Recursive Self-Evolving Agents via Held-Out Selection](https://arxiv.org/abs/2606.28374) | — | 📝 memory · L3 |
| 2025 | ICLR 2026 | [Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models](https://arxiv.org/abs/2510.04618) | [code](https://github.com/ace-agent/ace) | 📝 memory · L3 |
| 2025 | NeurIPS 2025 | [A-MEM: Agentic Memory for LLM Agents](https://arxiv.org/abs/2502.12110) | [code](https://github.com/agiresearch/A-mem) | 📝 memory · L3 |
| 2025 | arXiv | [Dynamic Cheatsheet: Test-Time Learning with Adaptive Memory](https://arxiv.org/abs/2504.07952) | [code](https://github.com/suzgunmirac/dynamic-cheatsheet) | 📝 memory · L3 |
| 2024 | arXiv | [Agent Workflow Memory](https://arxiv.org/abs/2409.07429) | [code](https://github.com/zorazrw/agent-workflow-memory) | 📝 memory · L3 |
| 2024 | ICLR 2024 | [Large Language Models as Optimizers (OPRO)](https://arxiv.org/abs/2309.03409) | [code](https://github.com/google-deepmind/opro) | 📝 memory · L2 |
| 2024 | ICLR 2024 | [Connecting Large Language Models with Evolutionary Algorithms Yields Powerful Prompt Optimizers (EvoPrompt)](https://arxiv.org/abs/2309.08532) | [code](https://github.com/beeevita/EvoPrompt) | 📝 memory · L2 |
| 2024 | AAAI 2024 | [ExpeL: LLM Agents Are Experiential Learners](https://arxiv.org/abs/2308.10144) | [code](https://github.com/LeapLabTHU/ExpeL) | 📝 memory · L3 |
| 2023 | arXiv | [Promptbreeder: Self-Referential Self-Improvement via Prompt Evolution](https://arxiv.org/abs/2309.16797) | — | 📝 memory · L3 |
| 2023 | arXiv | [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) | [code](https://github.com/MineDojo/Voyager) | 📝 memory · L3 |
| 2023 | NeurIPS 2023 | [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) | [code](https://github.com/madaan/self-refine) | 📝 memory · L2 |
| 2023 | NeurIPS 2023 | [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) | [code](https://github.com/noahshinn/reflexion) | 📝 memory · L3 |

---

## Open-Ended & Evolutionary Methods 🧬

Evolutionary and open-ended search that produces ever-better external artifacts: programs, algorithms, rewards, environments.

| Year | Venue | Paper | Code | Tags |
|---|---|---|---|---|
| 2025 | arXiv | [AlphaEvolve: A Coding Agent for Scientific and Algorithmic Discovery](https://arxiv.org/abs/2506.13131) | [code](https://github.com/google-deepmind/alphaevolve_results) | 🧬 artifacts · L3 |
| 2023 | Nature | [Mathematical Discoveries from Program Search with Large Language Models (FunSearch)](https://www.nature.com/articles/s41586-023-06924-6) | [code](https://github.com/google-deepmind/funsearch) | 🧬 artifacts · L3 |
| 2023 | ICLR 2024 | [Eureka: Human-Level Reward Design via Coding Large Language Models](https://arxiv.org/abs/2310.12931) | [code](https://github.com/eureka-research/Eureka) | 🧬 artifacts · L3 |
| 2023 | ICLR 2024 | [Quality-Diversity through AI Feedback (QDAIF)](https://arxiv.org/abs/2310.13032) | [code](https://github.com/CarperAI/OpenELM) | 🧬 artifacts · L3 |
| 2023 | ICLR 2024 | [OMNI: Open-endedness via Models of human Notions of Interestingness](https://arxiv.org/abs/2306.01711) | [code](https://github.com/jennyzzt/omni) | 🧬 artifacts · L3 |
| 2022 | arXiv | [Evolution through Large Models (ELM)](https://arxiv.org/abs/2206.08896) | [code](https://github.com/CarperAI/OpenELM) | 🧬 artifacts · L3 |
| 2020 | ICML 2020 | [Enhanced POET: Open-Ended Reinforcement Learning through Unbounded Invention of Learning Challenges and their Solutions](https://arxiv.org/abs/2003.08536) | [code](https://github.com/uber-research/poet) | 🧬 artifacts · L3 |
| 2020 | ICML 2020 | [AutoML-Zero: Evolving Machine Learning Algorithms From Scratch](https://arxiv.org/abs/2003.03384) | [code](https://github.com/google-research/google-research/tree/master/automl_zero) | 🧬 artifacts · L3 |
| 2019 | arXiv | [Paired Open-Ended Trailblazer (POET): Endlessly Generating Increasingly Complex and Diverse Learning Environments and Their Solutions](https://arxiv.org/abs/1901.01753) | [code](https://github.com/uber-research/poet/tree/original_poet) | 🧬 artifacts · L3 |

---

## Automated AI Research 🔬

Systems that automate the research process itself: idea generation, experimentation, paper writing, review. The closer these loops get to closing, the closer we are to RSI in the strong sense.

| Year | Venue | Paper | Code | Tags |
|---|---|---|---|---|
| 2026 | Nature | [Accelerating scientific discovery with Co-Scientist](https://arxiv.org/abs/2502.18864) | — | 🔬 research · L1 |
| 2025 | arXiv | [AI-Researcher: Autonomous Scientific Innovation](https://arxiv.org/abs/2505.18705) | [code](https://github.com/HKUDS/AI-Researcher) | 🔬 research · L3 |
| 2025 | arXiv | [The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search](https://arxiv.org/abs/2504.08066) | [code](https://github.com/SakanaAI/AI-Scientist-v2) | 🔬 research · L3 |
| 2025 | arXiv | [AgentRxiv: Towards Collaborative Autonomous Research](https://arxiv.org/abs/2503.18102) | [code](https://github.com/SamuelSchmidgall/AgentLaboratory) | 🔬 research · L3 |
| 2025 | arXiv | [AIDE: AI-Driven Exploration in the Space of Code](https://arxiv.org/abs/2502.13138) | [code](https://github.com/WecoAI/aideml) | 🔬 research · L3 |
| 2025 | arXiv | [Agent Laboratory: Using LLM Agents as Research Assistants](https://arxiv.org/abs/2501.04227) | [code](https://github.com/SamuelSchmidgall/AgentLaboratory) | 🔬 research · L2 |
| 2025 | NAACL 2025 | [ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models](https://arxiv.org/abs/2404.07738) | [code](https://github.com/JinheonBaek/ResearchAgent) | 🔬 research · L2 |
| 2025 | ICLR 2025 | [CycleResearcher: Improving Automated Research via Automated Review](https://arxiv.org/abs/2411.00816) | [code](https://github.com/zhu-minjun/Researcher) | 🔬 research · L3 |
| 2025 | ICLR 2025 | [Can LLMs Generate Novel Research Ideas? A Large-Scale Human Study with 100+ NLP Researchers](https://arxiv.org/abs/2409.04109) | [code](https://github.com/NoviScl/AI-Researcher) | 🔬 research · L2 |
| 2024 | arXiv | [The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery](https://arxiv.org/abs/2408.06292) | [code](https://github.com/SakanaAI/AI-Scientist) | 🔬 research · L3 |

---

## Safety, Alignment & Governance

What breaks when the loop closes: reward hacking, model collapse, deceptive alignment, and the governance of automated AI R&D.

| Year | Venue | Paper | Code | Tags |
|---|---|---|---|---|
| 2026 | METR | [Review of the "Risks from automated R&D" section in the Anthropic Risk Report](https://metr.org/blog/2026-05-08-rd-section-anthropic-risk-report-feb-2026-review/) | — | 🔬 research |
| 2025 | arXiv | [Bare Minimum Mitigations for Autonomous AI Development](https://arxiv.org/abs/2504.15416) | — | 🔬 research |
| 2025 | Forethought | [Will AI R&D Automation Cause a Software Intelligence Explosion?](https://www.forethought.org/research/will-ai-r-and-d-automation-cause-a-software-intelligence-explosion) | — | 🔬 research · L3 |
| 2025 | arXiv | [Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation](https://arxiv.org/abs/2503.11926) | — | 🧠 weights |
| 2024 | arXiv | [Alignment Faking in Large Language Models](https://arxiv.org/abs/2412.14093) | [code](https://github.com/redwoodresearch/alignment_faking_public) | 🧠 weights |
| 2024 | arXiv | [Frontier Models are Capable of In-context Scheming](https://arxiv.org/abs/2412.04984) | — | — |
| 2024 | arXiv | [Safety Cases for Frontier AI](https://arxiv.org/abs/2410.21572) | — | 🔬 research |
| 2024 | Nature | [AI models collapse when trained on recursively generated data](https://www.nature.com/articles/s41586-024-07566-y) | — | 🧠 weights · L3 |
| 2024 | arXiv | [Spontaneous Reward Hacking in Iterative Self-Refinement](https://arxiv.org/abs/2407.04549) | — | 📝 memory · L1 |
| 2024 | arXiv | [AI Sandbagging: Language Models can Strategically Underperform on Evaluations](https://arxiv.org/abs/2406.07358) | — | — |
| 2024 | arXiv | [Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data](https://arxiv.org/abs/2404.01413) | — | 🧠 weights · L3 |
| 2024 | ICML 2024 | [Feedback Loops With Language Models Drive In-Context Reward Hacking](https://arxiv.org/abs/2402.06627) | — | 📝 memory · L1 |

---

## Benchmarks & Evaluation

How do you measure a system's ability to improve systems, including itself?

| Year | Venue | Paper | Code | Tags |
|---|---|---|---|---|
| 2026 | arXiv | [AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement](https://arxiv.org/abs/2608.20318) | — | 🔬 research |
| 2026 | arXiv | [EvoAgentBench: Benchmarking Agent Self-Evolution via Ability Transfer](https://arxiv.org/abs/2607.05202) | [code](https://huggingface.co/datasets/EverMind-AI/EvoAgentBench) | 📝 memory |
| 2026 | arXiv | [PostTrainBench: Can LLM Agents Automate LLM Post-Training?](https://arxiv.org/abs/2603.08640) | [code](https://github.com/aisa-group/PostTrainBench) | 🧠 weights |
| 2025 | NeurIPS 2025 | [Measuring AI Ability to Complete Long Software Tasks](https://arxiv.org/abs/2503.14499) | [code](https://github.com/METR/eval-analysis-public) | 🔬 research |
| 2025 | NeurIPS 2025 | [MLR-Bench: Evaluating AI Agents on Open-Ended Machine Learning Research](https://arxiv.org/abs/2505.19955) | [code](https://github.com/chchenhui/mlrbench) | 🔬 research |
| 2025 | arXiv | [PaperBench: Evaluating AI's Ability to Replicate AI Research](https://arxiv.org/abs/2504.01848) | [code](https://github.com/openai/frontier-evals/tree/main/project/paperbench) | 🔬 research |
| 2025 | arXiv | [HCAST: Human-Calibrated Autonomy Software Tasks](https://arxiv.org/abs/2503.17354) | — | 🔬 research |
| 2025 | ICLR 2025 | [MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering](https://arxiv.org/abs/2410.07095) | [code](https://github.com/openai/mle-bench) | 🔬 research |
| 2024 | arXiv | [RE-Bench: Evaluating frontier AI R&D capabilities of language model agents against human experts](https://arxiv.org/abs/2411.15114) | [code](https://github.com/METR/ai-rd-tasks) | 🔬 research |
| 2024 | ICML 2024 | [MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation](https://arxiv.org/abs/2310.03302) | [code](https://github.com/snap-stanford/MLAgentBench) | 🔬 research |

---

## Surveys & Position Papers

| Year | Venue | Paper | Code | Tags |
|---|---|---|---|---|
| 2026 | arXiv | [Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops](https://arxiv.org/abs/2607.07663) | — | 🔬 research |
| 2026 | arXiv | [Self-Improvements in Modern Agentic Systems: A Survey](https://arxiv.org/abs/2607.13104) | — | 🧠 weights · 🔧 code |
| 2026 | arXiv | [Measuring AI R&D Automation](https://arxiv.org/abs/2603.03992) | — | 🔬 research |
| 2026 | TechRxiv | [A Systematic Survey of Self-Evolving Agents: From Model-Centric to Environment-Driven Co-Evolution](https://www.techrxiv.org/doi/10.36227/techrxiv.177203250.05832634) | [code](https://github.com/XMUDeepLIT/Awesome-Self-Evolving-Agents) | 🔧 code |
| 2025 | arXiv | [A Comprehensive Survey of Self-Evolving AI Agents: A New Paradigm Bridging Foundation Models and Lifelong Agentic Systems](https://arxiv.org/abs/2508.07407) | — | 🔧 code |
| 2025 | arXiv | [A Survey of Self-Evolving Agents: What, When, How, and Where to Evolve on the Path to Artificial Super Intelligence](https://arxiv.org/abs/2507.21046) | — | 🔧 code |
| 2025 | arXiv | [Preparing for the Intelligence Explosion](https://arxiv.org/abs/2506.14863) | — | 🔬 research |
| 2025 | arXiv | [AI Governance to Avoid Extinction: The Strategic Landscape and Actionable Research Questions](https://arxiv.org/abs/2505.04592) | — | 🔬 research |
| 2024 | arXiv | [A Survey on Self-Evolution of Large Language Models](https://arxiv.org/abs/2404.14387) | — | 🧠 weights |

---

## Talks, Blogs & Communities

| Year | Venue | Resource | Tags |
|---|---|---|---|
| 2026 | ICLR 2026 Workshop | [ICLR 2026 Workshop on AI with Recursive Self-Improvement (RSI 2026)](https://recursive-workshop.github.io/): 110 papers; spotlights include [Towards Execution-Grounded Automated AI Research](https://openreview.net/forum?id=gpLJamvbsK) and [Can Language Models Discover Scaling Laws?](https://openreview.net/forum?id=Nj6VGY4dej) | 🔬 research |
| 2025 | Sakana AI blog | [The Darwin Gödel Machine: AI that Improves Itself by Rewriting Its Own Code](https://sakana.ai/dgm/) | 🔧 code · L3 |
| 2025 | Google DeepMind blog | [AlphaEvolve: A Gemini-Powered Coding Agent for Designing Advanced Algorithms](https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) | 🧬 artifacts · L3 |
| 2025 | Essay / scenario | [AI 2027](https://ai-2027.com/): Kokotajlo, Alexander, Larsen, Lifland & Dean's scenario built around automated AI research | 🔬 research |
| 2024 | Essay | [Situational Awareness: The Decade Ahead](https://situational-awareness.ai/), Part II on the intelligence explosion via automated AI research | 🔬 research |

---

## Contributing

Contributions are welcome; see the [contribution guide](CONTRIBUTING.md). Every entry must declare its taxonomy cell (what is modified + loop closure), and if a work challenges the taxonomy itself, open an issue: that discussion is exactly what this list is for.

## License

[CC0 1.0](LICENSE), public domain.
