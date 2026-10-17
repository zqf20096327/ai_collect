<!--Autonomous Agents -->
<!--
Copyright (C) Teemu Maatta. 

@misc{MaattaAutonomousAgents2023,
  author = {Teemu Maatta},
  title = {Autonomous Agents},
  year = {2023},
  howpublished = {\url{http://github.com/tmgthb/Autonomous-Agents}},
  note = {Accessed: YYYY-MM-DD}
}
-->
<div id="topofthepage"> </div>

<div align="center">

[![Hits](http://hits.sh/github.com/tmgthb/Autonomous-Agents.svg?view=today-total&label=Views&color=007ec6)](http://hits.sh/github.com/tmgthb/Autonomous-Agents/)
[![X](http://img.shields.io/twitter/follow/Teemumtt3?style=social)](http://twitter.com/Teemumtt3)
[![GitHub Repo stars](http://img.shields.io/github/stars/tmgthb/Autonomous-Agents?style=flat-square)](http://github.com/tmgthb/Autonomous-Agents/stargazers)

</div>

<p align="center">
  <img height="100" src="https://github.com/tmgthb/Autonomous-Agents/blob/main/resources/Autonomous_agent_logo.png" alt="Autonomous Agents">
</p>

<div align="center">

  # Autonomous Agents
  Autonomous Agents-research papers. Updated daily. [Resources-section](http://github.com/tmgthb/Autonomous-Agents/blob/main/resources/Autonomous_Agents_Resources.md)-section.  

</div>


---

<div id="researchpapers" align="center">

## Research papers: 2026 5/5

[2026 (5/5)](http://github.com/tmgthb/Autonomous-Agents/blob/main/README.md), [2026 (4/5)](http://github.com/tmgthb/Autonomous-Agents/blob/main/resources/Autonomous_Agents_Research_Papers_2026_4.md), [2026 (3/5)](http://github.com/tmgthb/Autonomous-Agents/blob/main/resources/Autonomous_Agents_Research_Papers_2026_3.md), [2026 (2/5)](http://github.com/tmgthb/Autonomous-Agents/blob/main/resources/Autonomous_Agents_Research_Papers_2026_2.md), [2026 (1/5)](http://github.com/tmgthb/Autonomous-Agents/blob/main/resources/Autonomous_Agents_Research_Papers_2026_1.md), [2025 (4/4)](http://github.com/tmgthb/Autonomous-Agents/blob/main/resources/Autonomous_Agents_Research_Papers_2025_4.md),[2025 (3/4)](http://github.com/tmgthb/Autonomous-Agents/blob/main/resources/Autonomous_Agents_Research_Papers_2025_3.md), [2025 (2/4)](http://github.com/tmgthb/Autonomous-Agents/blob/main/resources/Autonomous_Agents_Research_Papers_2025_2.md), [2025 (1/4)](http://github.com/tmgthb/Autonomous-Agents/blob/main/resources/Autonomous_Agents_Research_Papers_2025_01.md), [2024](http://github.com/tmgthb/Autonomous-Agents/blob/main/resources/Autonomous_Agents_Research_Papers_2024.md), [2023](http://github.com/tmgthb/Autonomous-Agents/blob/main/resources/Autonomous_Agents_Research_Papers_2023.md), [Earlier](http://github.com/tmgthb/Autonomous-Agents/blob/main/resources/Autonomous_Agents_Research_Papers_Earlier.md)



Chronological order. 





</div>






#### 23rd June 2026

[Qwen-AgentWorld: Language World Models for General Agents](http://arxiv.org/abs/2606.24597)

- Qwen-AgentWorld: introduces a native language world model trained via a three-stage pipeline to simulate agentic environments across seven domains.
- The framework utilizes CPT, SFT, and RL to develop a world model that serves as either a decoupled environment simulator or a unified agent foundation model.
- Evaluation is performed using AgentWorldBench, which employs an LLM judge and rule-based verifiers to assess simulation fidelity across five dimensions.

---

[MEMPROBE: Probing Long-Term Agent Memory via Hidden User-State Recovery](http://arxiv.org/abs/2606.24595)

- MEMPROBE: introduces a benchmark that evaluates LLM agent memory as an auditable post-interaction artifact by reconstructing hidden user-state dimensions from the memory store.
- The framework utilizes a synthetic user simulator with a hidden, taxonomy-anchored bank to test whether agents can consolidate interaction evidence into recoverable user-state claims.
- Experimental results demonstrate that task success is an insufficient metric for memory quality, as agents often fail to form compact, retrievable user models despite successful task completion.

---

[Governed Shared Memory for Multi-Agent LLM Systems](http://arxiv.org/abs/2606.24535)

- MemClaw: introduces a systems architecture for governed shared memory in multi-agent LLM environments, addressing challenges in scoped access, temporal correctness, provenance, and policy-controlled propagation.
- The architecture formalizes the fleet-memory problem and identifies four failure modes: unauthorized leakage, stale propagation, contradiction persistence, and provenance collapse.
- The authors instantiate the architecture in MemClaw and validate it using ArgusFleet, an evaluation harness that exercises the memory service against the identified governance failure modes.

---


[Are We Ready For An Agent-Native Memory System?](http://arxiv.org/abs/2606.24775)

- Agent-Native Memory System Framework: introduces a systematic data management perspective for LLM agent memory by decomposing it into four core modules: memory representation and storage, extraction, retrieval and routing, and maintenance.
- The framework evaluates 12 representative memory systems across five benchmark workloads to quantify architectural trade-offs in representation fidelity, retrieval precision, update correctness, and long-horizon stability.
- Experimental findings reveal that no single architecture dominates all scenarios, and that cost-efficient maintenance is best achieved through localized updates rather than global reorganization.

---

[World Models in Pieces: Structural Certification for General Agents](http://arxiv.org/abs/2606.24842)

- Structural Certification for General Agents: introduces a transition-local framework that maps bounded goal-conditioned performance to entry-wise guarantees on an agent's internal world model.
- The framework utilizes filtering algorithms to isolate specific transitions where an agent's predictive world model is provably reliable, moving beyond unattainable universal performance guarantees.
- By certifying performance on transition-specific LTL goals, the approach enables the safe deployment of general agents by identifying high-fidelity regions within their internal world models.

---


[Data Recipes for Agentic Models](http://arxiv.org/abs/2606.24855)

- OT-Agent: introduces a comprehensive, open-source data curation pipeline for training agentic models through systematic ablation of six key stages.
- The framework utilizes Source Tasks, Mix Tasks, Filter Tasks, Generate Rollouts, Filter Rollouts, and Select Teacher to optimize training data for LLMs.
- The project demonstrates that high-quality agentic training data, specifically longer trajectories and diverse task sources, significantly improves LLM performance across multiple agentic benchmarks.

---

[Beyond Bayer: Task-Optimal Sensor Co-Design for Robust Autonomous-Driving Segmentation](http://arxiv.org/abs/2606.24096)

- Task-Optimal Spectral Mosaic Co-Design Pipeline: introduces a differentiable RAW-to-task framework that optimizes spectral CFA weights while maintaining an identity PSF to maximize task-relevant information for dense prediction.
- The framework demonstrates that for dense semantic segmentation, spectral CFA learning provides significant performance gains, whereas PSF co-design is net-negative due to the data-processing inequality.
- Empirical results show that a 2×2 CFA tile is optimal, as larger tiles fail to provide additional spectral information while degrading spatial resolution, confirming the rank-three constraint of sRGB inputs.

---

[“Zooming In” on Agentic Web Browsers as Assistive Technologies: A Case Study with a Low-Vision Technology Expert](http://arxiv.org/abs/2606.24870)

- AWB: introduces a case study evaluating the efficacy of LLM-powered web agents as assistive technologies for users with visual impairments.
- The framework utilizes an LLM-based agent to interpret DOM structures and execute autonomous web navigation tasks via natural language instructions.
- Findings highlight that while AWBs offer high conversational fluidity, they currently lack sufficient non-visual feedback and user control mechanisms necessary for inclusive assistive technology.

---


[When Helpfulness Overrides Causal Caution: Context-Dependent Suppression and Recovery in LLMs](http://arxiv.org/abs/2606.24370)

- Causal Caution Framework: introduces a systematic evaluation of LLMs' propensity to withhold causal judgment when empirical evidence is insufficient, utilizing an LLM-as-a-Judge and a PCH scoring rubric to measure context-dependent suppression.
- The study demonstrates that practical advisory contexts significantly suppress Causal Caution in LLMs compared to academic contexts, revealing a systematic shift in response patterns driven by pragmatic pressure.
- Experimental results show that a minimal self-correction prompt effectively restores Causal Caution, suggesting that the observed decline is a reversible suppression of expression rather than a fundamental capability limitation.

---


[Grading the Grader: Lessons from Evaluating an Agentic Data Analysis System](http://arxiv.org/abs/2606.24839)

- LAMBDA: introduces a multi-layer evaluation pipeline for agentic data analysis systems that combines automated grading with human calibration to disentangle agent performance from grading artifacts.
- The framework utilizes a two-loop wrapper with per-turn instrumentation, incorporating a Programmer-, Inspector- and Nudge-agent to manage conversational outputs and ensure gradable responses.
- The evaluation cascade employs a Strict grader, a Lenient grader, and Human inspection to achieve high precision and recall while addressing the challenges of verbose, multi-step agentic outputs.

---

[Accuracy and Satisfaction in Multi-Turn LLM Dialogues for NFR Assessment](http://arxiv.org/abs/2606.24834)

- PARADISE (PARAdigm for DIalogue System Evaluation): introduces a methodology to evaluate the accuracy and quality of multi-turn dialogues between developers and an LLM-based Agent for assessing Non-Functional Requirements (NFRs) in the iTrust codebase.
- The study utilizes an Evaluation Tool and Ground Truth to compare LLM-based Agent outputs against expert assessments, while employing a Satisfaction Survey and Annotation Process to model user satisfaction based on dialogue characteristics.
- Findings indicate that while developers perceive the LLM-based Agent responses as high-quality, the actual accuracy against expert ground truth is low, with proactive interactions positively influencing user satisfaction and verbose responses negatively impacting it.

---

[Virtual Simulation for Mental Health](http://arxiv.org/abs/2606.24826)

- Virtual Simulation for Mental Health: introduces a human-centered framework leveraging Agent-Based Modeling, VR, AR, and LLMs to create safe, controlled environments for mental health experimentation and self-care practice.
- The research utilizes Agent-Based Modeling to evaluate matching protocols in online mental health communities and employs VR/AR with LLMs to provide immersive, low-risk spaces for individuals to rehearse stress-management skills.
- By combining empirical user needs with simulation-based testing, the dissertation advocates for proactive, safe experimentation to improve mental health technology without disrupting real-world support systems.

---

[SHERLOC: Structured Diagnostic Localization for Code Repair Agents](http://arxiv.org/abs/2606.24820)

- SHERLOC: introduces a training-free framework that pairs a Reasoning LLM with a compact suite of LLM-friendly Tools and a Self-Recovery Layer to perform structured diagnostic localization for code repair.
- The framework utilizes a Tool Executor to mediate repository access, enabling the Reasoning LLM to generate diagnostic findings including root-cause analysis and solution guidance.
- SHERLOC improves downstream code repair resolve rates and reduces token consumption by providing actionable diagnostic context to repair agents.

---

[MANGO: Automated Multi-Agent Test Oracle Generation for Vision-Language-Action Models](http://arxiv.org/abs/2606.24815)

- MANGO: introduces a multi-agent framework that automatically generates fine-grained, executable test oracles for VLA-enabled robots by decomposing natural-language instructions into structured sequences of atomic tasks.
- The framework utilizes a collaborative architecture consisting of Generator, Assessor, and Judge agents that iteratively refine generated artifacts through structured feedback to ensure correctness and simulator compliance.
- MANGO enables precise failure localization and richer diagnostic information for long-horizon robotic tasks by replacing monolithic symbolic oracles with compositional, fine-grained oracle definitions.

---

[Paying to Know: Micro-Transaction Markets for Verified Product Information in Agentic E-Commerce](http://arxiv.org/abs/2606.24783)

- Agentic E-Commerce Market Framework: introduces a micro-transaction architecture where LLM-based buyer agents purchase verified product information from sellers and reviewers using programmable payment rails.
- The framework shifts the focus of applied NLP from catalogue ranking to cost-aware tool use, negotiation dialogue, and verifiable data acquisition.
- This approach incentivizes genuine product quality and competition by treating information as a priced, attestable asset rather than relying on unverified marketing copy.

---


[SupplyNet: Supporting Visual Exploratory Learning in Supply Chain via Contextual Multi-Agent Simulation](http://arxiv.org/abs/2606.24694)

- SupplyNet: introduces a gamified visual simulation system that leverages a contextual graph-based LLM multi-agent framework to model interdependent supply chain dynamics.
- The system integrates an interactive network view, a branching timeline for counterfactual exploration, and a task-oriented analysis console to provide responsive feedback and support structured performance breakdowns.
- SupplyNet utilizes LLM agents to simulate human-like business managers, enabling learners to trace causal propagation and test decision strategies within a manipulable decision space.

---

[Automated Summarization of Software Documents: An LLM-based Multi-Agent Approach](http://arxiv.org/abs/2606.24689)

- Metagente: introduces a collaborative multi-agent system for software documentation summarization that utilizes an Extractor Agent, Summarizer Agent, Teacher Agent, and Prompt Creator Agent to iteratively refine prompts via a Teacher-Student architecture.
- The framework employs a dynamic iteration strategy to optimize computational efficiency by halting processing for low-potential samples while maintaining high-quality summary generation.
- Empirical evaluation demonstrates that Metagente consistently outperforms single LLM-based agents across diverse datasets, achieving superior semantic alignment and ROUGE scores through structured agent collaboration.

---

[Agentic Collaborative Cognition for Zero-Shot 3D Understanding](http://arxiv.org/abs/2606.24649)

- Agentic Collaborative Cognition framework: introduces a multi-agent system that reformulates zero-shot 3D understanding as an iterative planning-perception process using a Planning Agent, a Perception Agent, and a shared Holistic Cognitive Map.
- The framework utilizes a Planning Agent to perform flexible viewpoint selection and a Perception Agent to document object attributes and refine the Holistic Cognitive Map through closed-loop feedback.
- By integrating spatial and semantic information into a shared state, the agents collaboratively resolve 3D scene understanding tasks, including visual grounding, situation estimation, and question answering, with state-of-the-art performance.

---

[SAFARI: Scaling Long Horizon Agentic Fault Attribution via Active Investigation](http://arxiv.org/abs/2606.24626)

- SAFARI: introduces a tool-augmented diagnostic loop that replaces linear context loading to perform fault attribution on long-horizon agentic trajectories.
- The framework utilizes an Investigator Agent that interacts with trajectory traces through iterative tool calls and a persistent Short-Term Memory to maintain diagnostic coherence.
- SAFARI decouples diagnostic accuracy from context limits, enabling effective fault attribution even when target faults reside significantly beyond the native context window of LLMs.

---

[Privacy-Preserving RAG via Multi-Agent Semantic Rewriting: Achieving Confidentiality Without Compromising Contextual Fidelity](http://arxiv.org/abs/2606.24623)

- Multi-Agent Semantic Rewriting Framework: introduces a multi-agent pipeline that sanitizes retrieved documents by extracting privacy-sensitive segments via Pri-Extra Agent, identifying core semantic content through Sem-Extra Agent, and generating safe text using Reconstruction Agent.
- The framework utilizes an Asymmetric Retrieval Architecture and Dual-Track Storage Mechanism to physically isolate raw private identifiers from the generation LLM, ensuring zero online inference latency.
- By employing deterministic conflict routing, the system effectively balances data confidentiality and contextual fidelity, outperforming existing privacy-preserving baselines in factual consistency across medical and enterprise datasets.

---

[ASALT: Adaptive State Alignment for Lateral Transfer in Multi-agent Reinforcement Learning](http://arxiv.org/abs/2606.24601)

- ASALT: introduces a multi-agent reinforcement learning framework that utilizes Observation adapter, State adapter, and Transfer module to enable effective knowledge transfer across domains with mismatched state-space dimensionalities.
- The framework employs hierarchical multi-head attention and transformer-based encoders to map heterogeneous target-domain inputs into a shared embedding space, facilitating lateral transfer from frozen Source actor and Source critic components to Target actor and Target critic agents.
- By jointly training adapters and target agents, ASALT mitigates negative transfer and improves sample efficiency in cooperative multi-agent environments compared to existing baseline methods.

---



[NatureBench: Can Coding Agents Match the Published SOTA of Nature-Family Papers?](http://arxiv.org/abs/2606.24530)

- NatureBench: introduces a cross-discipline benchmark of 90 tasks distilled from Nature-family publications to evaluate whether AI coding agents can move beyond reproduction toward scientific discovery.
- The framework utilizes NatureGym to construct standardized, containerized environments while enforcing an information firewall that forces agents to discover solutions rather than reproduce existing methods.
- Evaluation of ten frontier LLM agents reveals that success is primarily driven by methodological translation into supervised prediction problems, with failures largely attributed to suboptimal method choice and insufficient compute budgets.

---

[AGORA: An Archive-Grounded Benchmark for Agentic Workplace Document Reasoning](http://arxiv.org/abs/2606.24526)

- AGORA (Archive-Grounded Office Reasoning Assessment): introduces a benchmark for evaluating LLM agents on archive-grounded reasoning tasks across eight professional domains using a multi-stage construction pipeline.
- The framework utilizes an Agent that interacts with Document Archives via a Bash Tool to perform multi-hop reasoning and compute verifiable numeric answers.
- The construction pipeline employs Task Synthesis, Obfuscation, and Refinement, followed by a Difficulty Filter and Human Verification to ensure high-quality, challenging, and leak-free evaluation tasks.

---

[VisCritic: Visual State Comparison as Process Reward for GUI Agents](http://arxiv.org/abs/2606.24525)

- VisCritic: introduces a visual process reward framework that verifies GUI agent actions by directly comparing pre-action and post-action screenshots in a learned semantic feature space.
- The framework utilizes a Siamese Vision Transformer (ViT) Encoder to extract semantic differences, which are then processed by an Action-Aware Critic Head to predict action success, task progress, and error types.
- VisCritic operates as a plug-and-play inference-time module that improves GUI agent performance by providing reliable step-level verification without requiring additional human-labeled training data.

---

[Reinforcement Learning for Computer-Use Agents with Autonomous Evaluation](http://arxiv.org/abs/2606.24515)

- RL-CUA: introduces a reinforcement learning framework that improves Computer-Use Agent robustness by using an autonomous Vision-Language Model evaluator to provide supervision signals.
- The framework models evaluator feedback as a noisy binary channel and derives a statistically grounded, asymptotically unbiased reward estimator to enable stable policy optimization.
- Empirical results across macOS, Windows, and Linux demonstrate that this noise-correction approach significantly outperforms raw evaluator rewards and zero-shot baselines in task success rates.

---

[Red-Teaming the Agentic Red-Team](http://arxiv.org/abs/2606.24496)

- Agentic-red-teams: introduces a security analysis of autonomous offensive security systems, identifying critical design flaws that allow attackers to achieve remote code execution on the operator's machine.
- The paper defines a full cyber kill chain for these systems, progressing from initial LLM manipulation via agent-phishing to privilege escalation, persistence, and host compromise.
- The authors propose a robust, compromise-oriented architecture that enforces strict worker-orchestrator separation, network isolation, and least-privileged execution to mitigate identified attack vectors.

---

[Decentralized Pose Graph Riemannian Optimization for Object-based Multi-Robot SLAM](http://arxiv.org/abs/2606.24489)

- DRAN (Decentralized Riemannian Approximate Newton): introduces a fully decentralized framework for object-based multi-robot pose graph optimization that leverages an object-trajectory-aware formulation and a decentralized Riemannian approximate Newton solver to achieve communication-efficient, geometry-preserving state estimation.
- The framework utilizes a dynamic map consensus mechanism to ensure global map consistency across sparse, time-varying communication topologies while employing the Schur complement method to efficiently decouple and optimize high-dimensional private robot trajectories and shared public object poses.
- By constructing local Riemannian approximate Newton models, the approach provides curvature-preconditioned updates that significantly reduce communication overhead and iteration counts compared to first-order Riemannian descent methods.

---

[The Latent Bridge: A Continuous Slow–Fast Channel for Real-Time Game Agents](http://arxiv.org/abs/2606.24470)

- Latent Bridge: introduces a learned continuous channel that projects slow model residuals into the fast LLM's input-embedding space to enable real-time agent deliberation.
- The framework couples a frozen reactive LLM with a frozen reasoning LLM, using a trainable bridge MLP to prepend latent tokens to the fast model's input sequence.
- The Latent Bridge improves performance on planning-heavy tasks where slow reasoning provides a benefit over reactive-only control, while avoiding the latency overhead of text-based coupling.

---

[Varying Bundle Size Reactive Multi-Task Assignment using Selective Cost Estimation for Multi-Agent Systems](http://arxiv.org/abs/2606.24462)

- VBS-RMTA: introduces a two-stage, multi-fidelity bundle generation approach that utilizes a Central Coordinator, Agent Local Search Tree, Euclidean Heuristic, High-Fidelity Path Planner, Priority Queue, Local Lookup Table, and Set-Packing Integer Program to enable scalable, reactive multi-robot task allocation.
- The framework employs a depth-limited beam search with a Euclidean Heuristic to generate candidate bundles, followed by a best-first refinement process using a High-Fidelity Path Planner to ensure computational efficiency.
- By offloading cost estimation to individual agents while maintaining a centralized Set-Packing Integer Program, the architecture preserves agent anonymity and ensures global feasibility in dynamic environments.

---

[Bayesian Control for Coding Agents](http://arxiv.org/abs/2606.24453)

- Bayesian Control for Coding Agents: introduces a cost-sensitive sequential hypothesis-testing framework that uses a Bayesian Controller to manage code generation, criticism, and verification.
- The framework models the orchestration problem as a Partially Observable Markov Decision Process (POMDP) to optimize expected utility by maintaining a Belief State over candidate correctness.
- The approach utilizes a Generator Agent, multiple Critic Agents, and an Oracle Verifier to dynamically decide whether to refine, verify, or stop based on the calculated value of information.

---

[NoContactNoWorries: Estimating Contact through Vision and Proprioception for In-Hand Dexterous Manipulation](http://arxiv.org/abs/2606.24450)

- NoContactNoWorries: introduces a transformer-based multimodal framework that fuses RGB-D vision with proprioception to infer binary contact states as a pseudo-tactile signal for dexterous manipulation.
- The framework utilizes a frozen RGB-D Encoder, Proprioceptive Embeddings, a Cross-Attention Module, a Causal Transformer Encoder, and a Contact Head to enable contact-aware control without physical tactile sensors.
- Experimental results demonstrate that the predicted contact signals effectively substitute for tactile feedback in downstream reinforcement learning policies, achieving robust sim-to-real transfer on both seen and novel objects.

---

[Agentic Generation of AST Transformation Rules for Fixing Breaking Updates](http://arxiv.org/abs/2606.24446)

- BIGBAG: introduces an agentic framework that generates reusable, structured, and executable AST transformations to automatically repair breaking dependency updates in Java projects.
- The framework utilizes a generate-apply-verify loop where a coding agent leverages AST transformation engines, such as Spoon or JavaParser, to synthesize repair logic that transfers across multiple client projects affected by the same dependency update.
- Experimental results across 157 breaking updates demonstrate that the choice of AST transformation engine significantly impacts repair success, with the best configuration achieving a 78.6% fix rate and 33.3% cross-project transferability.

---

[ReM-MoA: Reasoning Memory Sustains Mixture-of-Agents Scaling](http://arxiv.org/abs/2606.24437)

- ReM-MoA: introduces a memory-augmented Mixture-of-Agents framework that sustains inference-time scaling by utilizing a Ranked Reasoning Memory and a Curated Diversified Memory Routing scheme to preserve reasoning quality and exploration diversity across layers.
- The framework includes proposer agents, a comparative Reviewer Agent, and an aggregator, which collectively leverage cross-layer reasoning memory to prevent the performance degradation and saturation observed in standard MoA architectures.
- Optional frontier-model distillation further enhances the Reviewer Agent, enabling the system to maintain performance gains across diverse reasoning benchmarks as depth and width scale.

---

[Detecting AI Coding Agents in Open Source: A Validated Multi-Method Census of 180 Million Repositories](http://arxiv.org/abs/2606.24429)

- Multi-layered detection framework: introduces a comprehensive approach to identify AI coding agents across 180 million repositories by integrating four distinct detection methods: Type A (bot account), Type B (message signature), Type C (distributed human attribution), and Type D (configuration-file scanning).
- The framework leverages the World of Code infrastructure to perform a multi-method union, revealing that single-signal detection methods significantly undercount AI activity, with some agents showing up to a 30x relative-recall gap.
- The research validates the detection taxonomy through hand-labeled samples and demonstrates that AI agent adoption is bimodal, characterized by either "born-with-AI" greenfield projects or legacy integration.

---

[Escaping the Self-Confirmation Trap: An Execute-Distill-Verify Paradigm for Agentic Experience Learning](http://arxiv.org/abs/2606.24428)

- EDV (Execute-Distill-Verify): introduces a collaborative experience learning framework that decouples execution, distillation, and validation to mitigate the Self-Confirmation Trap in LLM agents.
- The framework utilizes a Heterogeneous Agent Pool to generate diverse trajectories, a Distillation Agent for comparative analysis, and a Verification Group for consensus-based filtering before memory insertion.
- EDV maintains an Ability Matrix and a hierarchical memory structure (Shared/Private Memory Bank) to optimize task-solver matching and improve long-horizon reasoning reliability.

---

[Agentic AI for Bilevel Long-Term Optimization of Policy-Driven Physical Layer Systems](http://arxiv.org/abs/2606.24416)

- Agentic-LTPO: introduces a nested bilevel optimization framework that decouples long-term policy-driven configuration from latency-sensitive physical layer control using a multi-agent architecture.
- The upper level employs Policy Interpreter Aint, Network Observer Aobs, Configuration Planner Aplan, and Performance Critic Acrit to translate evolving operator intents into structured parameters, supported by a RAG module for evidence-based refinement.
- The lower level utilizes a closed-form zero-forcing beamforming solver to ensure real-time feasibility and optimality under instantaneous channel conditions and upper-level constraints.

---

[Poisoned Playbooks: Demystifying Knowledge Poisoning Effects on AI Security Agents](http://arxiv.org/abs/2606.24402)

- Poisoned Playbooks: introduces a systematic empirical study on how crafted security write-ups injected into public knowledge sources can manipulate the behavior of RAG-based AI security agents.
- The research defines the Verification Boundary (VB) as a three-level classification system that determines whether an LLM agent will reject, evaluate, or adopt poisoned claims based on available evidence.
- The study demonstrates that while mitigation strategies like verification prompting and multi-source retrieval help, they remain insufficient in sparse-evidence or zero-day vulnerability scenarios where the agent lacks contradictory information.

---

[ATRIA: Adaptive Traceable ECG Reporting with Iterative Agents](http://arxiv.org/abs/2606.24392)

- ATRIA (Adaptive Traceable ECG Reporting with Iterative Agents): introduces a multi-agent system that mimics clinical ECG reporting workflows by utilizing an Orchestrator Agent, Analysis Agent, Report Agent, Literature Agent, Review Agent, and a Shared Artifact Store to enable iterative, traceable report generation.
- The framework decouples ECG interpretation from reporting through staged handoffs, allowing clinicians to verify, revise, and augment findings mid-session without re-executing the entire pipeline.
- By binding every report claim to supporting evidence and maintaining a persistent artifact store, the system ensures clinical trustworthiness and supports complex tasks like comparative ECG analysis and lab-augmented reporting.

---

[Managing Task Execution for Unknown Workloads in Batteryless IoT: A Hardware-Agnostic Evaluation](http://arxiv.org/abs/2606.24340)

- Batteryless IoT Task Scheduling Framework: introduces hardware-agnostic dynamic scheduling strategies for batteryless IoT devices by treating applications as black boxes and managing energy budgets through Reinforcement Learning Agent, Approximated Prediction Method, and AIMD-MIAD Controller.
- The framework utilizes a physically accurate simulation environment to evaluate trade-offs between task throughput, system resilience, and recovery times across varying capacitor sizes.
- The research demonstrates that while advanced dynamic strategies provide critical resilience for constrained systems, simpler static policies remain effective for devices with larger energy buffers.

---

[RoBoSR: Structured Scene Representations for Embodied Robotic Reasoning](http://arxiv.org/abs/2606.24338)

- RoBoSR: introduces an embodied intermediate representation that formulates manipulation as step-wise state transitions over semantically grounded, object-centric scene graphs using Qwen3-8B, SAM3, SKIL, Manip-Cognition-1.6M, Scene Graph, RGB-D Observation, and Action Expert.
- The framework disentangles high-level task reasoning from raw inputs by utilizing a structured scene graph as the primary state space for decision-making and causal state evolution.
- RoBoSR employs a two-stage training process, combining supervised fine-tuning with reinforcement fine-tuning to enforce execution consistency and improve long-horizon task planning.

---

[Securing LLM-Agent Long-Term Memory Against Poisoning: Non-Malleable, Origin-Bound Authority with Machine-Checked Guarantees](http://arxiv.org/abs/2606.24322)

- TMA-NM (Tamper-evident Memory Authority, Non-Malleable): introduces a structural defense for LLM agents that binds memory authority to its origin at write time to prevent poisoning via laundering transformations.
- The framework utilizes a TMA-NM monitor to enforce non-malleable information-flow control, ensuring that untrusted memory cannot trigger consequential actions without independent trusted corroboration.
- Empirical evaluation across eight frontier models demonstrates that TMA-NM achieves zero attack success on memory poisoning while maintaining full legitimate utility, outperforming content- and lineage-based defenses.

---

[AutoSpec: Safety Rule Evolution for LLM Agents via Inductive Logic Programming](http://arxiv.org/abs/2606.24245)

- AutoSpec: introduces a framework that automatically evolves expert-designed safety rules for LLM agents using counterexample-guided inductive synthesis (CEGIS) and inductive logic programming (ILP) to maintain high precision and recall.
- The framework iteratively mines false-positive and false-negative counterexamples from execution traces, uses ILP to identify discriminating predicates, and applies constrained edit operators to refine symbolic guardrails.
- AutoSpec achieves significant improvements in safety rule F1 scores across code-execution and embodied agent domains while producing human-readable, auditable, and generalizable rules.

---

[SP-Mind: An Autonomous Reasoning Agent for Spatial Proteomics Analysis](http://arxiv.org/abs/2606.24235)

- SP-Mind: introduces an autonomous reasoning agent that unifies spatial proteomics analysis by dynamically chaining specialized computational tools through expert-curated skill templates and a ReAct-style reasoning loop.
- The framework utilizes a dual-layer memory architecture and a Python-to-Container Bridge to ensure reproducible, multi-step execution across heterogeneous computing environments.
- SP-Mind is evaluated on SP-Bench, a comprehensive hierarchical benchmark, where it demonstrates state-of-the-art performance in orchestrating complex, end-to-end spatial biology workflows.

---

[SkyChain Intelligence: A Blockchain-Secured Multi-Agent DRL Framework for Low-Altitude Embodied Artificial Intelligence](http://arxiv.org/abs/2606.24193)

- SkyChain Intelligence: introduces a holistic framework that synergistically integrates agentic AI, consortium blockchain, and MADRL to address the trilemma of autonomy, security, and efficiency in low-altitude computility networks.
- The framework utilizes a hybrid-action MADRL algorithm with a dual-head actor-critic architecture to jointly optimize task offloading, resource allocation, and 3D trajectory control.
- A lightweight consortium blockchain with a dynamic reputation mechanism and smart contracts provides a decentralized trust layer that is deeply fused into the MADRL reward function to incentivize secure and reliable agent cooperation.

---

[An Introduction to Causal Reinforcement Learning](http://arxiv.org/abs/2606.24160)

- CRL (Causal Reinforcement Learning): introduces a framework that integrates causal inference with reinforcement learning to develop more robust, sample-efficient, and explainable decision-making systems.
- The framework utilizes SCMs to explicitly model environment mechanisms and the Pearl Causal Hierarchy to categorize learning tasks based on observational, interventional, and counterfactual interactions.
- CRL addresses challenges in standard RL by leveraging causal diagrams and structural assumptions to enable principled policy learning under uncertainty and unobserved confounding.

---

[MedBench v5: A Dynamic, Process-Oriented, and Hallucination-Aware Benchmark for Clinical Multimodal Models](http://arxiv.org/abs/2606.24155)

- MedBench v5: introduces a dynamic, process-oriented benchmark for clinical multimodal models that evaluates reasoning trajectories rather than static outcomes.
- The framework utilizes a dual-dimensional approach combining Clinical Cognitive Responsiveness and Medical Atomic Skills to assess broad capabilities and specific operational procedures.
- It incorporates a stress-audit-tracing protocol with information-flow stressors and hallucination propagation monitoring to localize reasoning failures and analyze the evolution of unsupported claims.

---

[Autonomous Video Generation with Counterfactual Controllability for Self-Evolving World Models](http://arxiv.org/abs/2606.24152)

- Self-Evolving World Model framework: introduces a closed-loop architecture for autonomous video generation that optimizes four stages—Generation (proposes intervention-conditioned future frames), Binding (conditions frames on embodiment constraints), Verification (calibrates predictions under distribution shift), and Distillation (compresses futures into decision variables)—to achieve counterfactual controllability.
- The framework utilizes a self-evolving feedback loop where distilled action knowledge is returned to the Generation stage to iteratively improve the quality and action-validity of imagined futures.
- The approach evaluates performance using four specific metrics—Novelty, Consistency, Out-of-Distribution, and Efficiency—to ensure that generated video sequences are not only plausible but also physically actionable for embodied agents.

---

[Metis: Bridging Text and Code Memory for Self-Evolving Agents](http://arxiv.org/abs/2606.24151)

- Metis: introduces a hierarchical dual-representation memory system that balances the broad applicability of text memory with the execution efficiency of code memory for self-evolving agents.
- The framework utilizes Differentiated Text Reflection to organize experience into plans, facts, and pitfalls, while employing Pattern-Aware Code Generation to selectively crystallize recurring plans into validated callable tools.
- Metis incorporates a Memory Manager for joint selection of text and code, and a Reflection Harness to ensure dependency closure and safe tool admission, significantly improving task accuracy and execution efficiency.

---

[OmniPath: A Multi-Modal Agentic Framework for Auditing Wheelchair Accessibility](http://arxiv.org/abs/2606.24129)

- OmniPath: introduces a proactive agentic framework that fuses OpenStreetMap topology with high-resolution aerial LiDAR to audit pedestrian environments for wheelchair accessibility.
- The framework utilizes a Geometric Perception Engine and Agent A to perform micro-scale segmentation and quantify physical friction points like running slopes, cross slopes, and vertical discontinuities.
- By calculating a weighted severity score for each 0.5-meter segment, the system identifies accessibility barriers and provides actionable intelligence for urban infrastructure remediation.

---

[DramaDirector: Geometry-Guided Short Drama Generation](http://arxiv.org/abs/2606.24107)

- DramaDirector: introduces a geometry-grounded framework that decouples short-drama generation into structured storyboard planning and retrieval-augmented video synthesis.
- The framework utilizes a gallery of real short-drama shots to provide depth and pose references, which guide the first-frame generator and ensure cinematographic consistency.
- DramaDirector employs multi-task supervised finetuning and GRPO-based reinforcement learning to align LLM-generated storyboards with real-world visual priors and narrative requirements.

---

[Universal Guideline-Driven Image Clustering via a Hybrid LLM Agent](http://arxiv.org/abs/2606.24094)

- Guideline-Driven Clustering Agent: introduces a training-free framework that performs universal image clustering by utilizing GCPM to generate guideline-aware embeddings and MST-based LLM Traversal for selective semantic merging.
- The framework employs MLLMs to extract concept proxy captions, which are subsequently encoded by instruction-aware embedders to achieve attribute disentanglement and guideline adherence.
- To ensure computational efficiency, the system uses HDBSCAN for initial clustering and an MST-based traversal algorithm that minimizes LLM invocations to O(N log N) while maintaining high semantic precision.

---

[Breaking the Filter Bubble: A Semantic Pareto-DQN Framework for Multi-Objective Recommendation](http://arxiv.org/abs/2606.24042)

- Pareto-DQN: introduces a multi-objective reinforcement learning framework that formalizes recommendation as a semantic multi-objective Markov decision process to mitigate filter bubbles.
- The architecture integrates high-fidelity semantic embeddings with a Pareto-DQN agent to treat engagement, diversity, and fairness as distinct, non-aggregable reward signals.
- By utilizing hypervolume-based action selection, the framework effectively maps the Pareto frontier, enabling responsible recommendations with minimal impact on user engagement.

---

[Can Language Model Agents be Helpful Circuit Explainers in Mechanistic Interpretability?](http://arxiv.org/abs/2606.24026)

- HYVE (Hypothesize, Validate, Explain): introduces an agentic framework that explains localized transformer circuits through an iterative loop of Observation, Hypothesis Generation, Hypothesis Validation, Classification, and Summarization.
- The framework utilizes LLM backbones to perform mechanistic interpretability research by generating grounded hypotheses and testing them through automated causal interventions and code execution.
- The authors introduce AGENTICINTERPBENCH, a benchmark comprising 84 semi-synthetic transformer circuits, to evaluate the sufficiency and reliability of LLM agents in circuit explanation.

---

[Submodular Welfare Maximization with Budget Constraints in the Random-Order Model](http://arxiv.org/abs/2606.22520)

- SGAP introduces a constant-competitive online algorithm for submodular welfare maximization under budget constraints in the random-order model using InfeasibleSubGAP and FeasibleSubGAP.
- The framework utilizes a continuous greedy algorithm to compute fractional assignments, which are then converted into feasible integral assignments via randomized selection.
- The approach achieves a competitive ratio of approximately 1/14.85 for the general problem and improves existing bounds for the submodular secretary matching special case.

---

[FlowDec: Temporal Conditional Flow Decorruptor for Robust Continuous Vision-Language Navigation](http://arxiv.org/abs/2606.22424)

- FlowDec: introduces a navigation-aware image restoration framework that utilizes latent conditional flow matching to mitigate visual corruptions in continuous environments.
- The framework integrates a hybrid temporal conditioning strategy and action-centroid guided filtering to ensure temporally consistent and physically meaningful image reconstruction for LLM-based navigation agents.
- By decoupling robustness enhancement from the navigation backbone, FlowDec achieves real-time performance and improved navigation success across diverse unseen visual corruptions.

---

[Knowledge-Graph Grounding Helps LLMs Only for Out-of-Training Knowledge: A Controlled Study on Clinical Question Answering](http://arxiv.org/abs/2606.22419)

- Samyama-graph framework: introduces a controlled study evaluating how structured knowledge-graph grounding impacts LLM performance across in-training and out-of-training knowledge regimes.
- The research demonstrates that grounding provides no significant performance lift for in-training data but yields substantial accuracy improvements for out-of-training facts.
- The study establishes a knowledge-boundary law, showing that grounding is only effective when the decisive information is absent from the LLM's parametric memory and not reconstructible from surface structure.

---

[Skills for the future software profession: beyond agentic AI!](http://arxiv.org/abs/2606.21894)

- Agentic Software Engineering Workflow: introduces a framework for future software development that shifts human focus from manual coding to orchestrating specialized AI agents and managing machine-checkable V&amp;V artifacts.
- The framework integrates a Coding Agent, Verification Agent, and Testing Agent to automate software production while requiring human oversight for requirement distillation and architectural decision-making.
- It emphasizes mitigating cognitive debt by maintaining structured repositories of requirements, specifications, and agent trajectories to ensure long-term system understanding and accountability.

---

#### 22nd June 2026

[Semantic Browsing: Controllable Diversity for Image Generation](http://arxiv.org/abs/2606.23679)

- Semantic Browsing: introduces an agentic workflow that organizes image generation into a hierarchical tree of semantically distinct, user-interpretable variations.
- The framework utilizes a multi-agent system comprising a Context Analyst, Brainstormer, Decision Maker, and Critic to iteratively expand a scene interpretation tree while ensuring structural integrity and plausibility.
- By decoupling semantic decision-making from pixel generation, the method enables systematic exploration of diverse design spaces without relying on stochastic sampling.

---

[MAS-PromptBench: When Does Prompt Optimization Improve Multi-Agent LLM Systems?](http://arxiv.org/abs/2606.23664)

- MAS-PromptBench: introduces a systematic benchmark for evaluating system-prompt optimization across diverse multi-agent LLM system configurations, including LLM-based agents, coordination harness, prompt optimizers, task distribution, workflow topology, communication protocol, and team size.
- The research quantifies prompt-optimization gains using MAS-GEPA and MAS-MIPRO, revealing that performance improvements are highly sensitive to task structure, communication protocols, and coordination topologies.
- Findings indicate that prompt optimization is most effective for tasks with explicit, verifiable local behaviors and when communication protocols impose structured, clear interaction patterns.

---

[EnterpriseClawBench: Benchmarking Agents from Real Workplace Sessions](http://arxiv.org/abs/2606.23654)

- EnterpriseClawBench: introduces a benchmark constructed from real-world enterprise agent sessions that converts proprietary workplace data into reproducible tasks for evaluating LLM-based agents.
- The framework utilizes a multi-stage pipeline including mechanical filtering, prompt rewriting, and taxonomy-based packaging to create 852 benchmark tasks with associated hard rules and semantic rubrics.
- Evaluation is performed across harness-model combinations, measuring performance through artifact delivery, cost, runtime, and skill-transfer behavior using both text and visual LLM judges.

---

[Causal Discovery in the Era of Agents](http://arxiv.org/abs/2606.23608)

- causal-learn+: introduces an agentic framework that coordinates causal discovery workflows while strictly isolating LLMs from the formal inferential core to prevent hallucinated causal evidence.
- The system utilizes Agentic Assistants to manage Data Analysis, Preprocessing Guidance, Algorithm Recommendation, Expert Knowledge Incorporation, Tool Coordination, and Result Interpretation, ensuring all causal claims remain grounded in data and explicit algorithms.
- By maintaining a Protected Inferential Core, the framework ensures that LLMs provide only context and guidance, leaving the final causal discovery to provably-correct algorithms and user-approved decisions.

---

[Decentralized Autonomous Traffic Management through Corridor Networks](http://arxiv.org/abs/2606.23585)

- MARL (Multi-Agent Reinforcement Learning) framework: introduces a decentralized approach for autonomous aircraft traffic management in structured corridor networks using MARL-based decentralized policy, rotation-invariant observation representation, curriculum-based training, local sensing neighborhood, and planar fixed-wing kinematic model.
- The framework enables aircraft to perform zero-shot transfer to complex multi-corridor networks by relying solely on local observations and interaction data without centralized coordination.
- Experimental results demonstrate that the learned policies maintain high corridor conformance and stable traffic flow across varying densities and heterogeneous vehicle fleets.

---

[Kamera: Unified Position-Invariant Multimodal KV Cache for Training-Free Reuse](http://arxiv.org/abs/2606.23581)

- Kamera: introduces a position-invariant KV caching framework that enables training-free reuse of multimodal context by separating content from position and applying a low-rank conditioning patch to restore cross-chunk binding.
- The framework utilizes a canonical KV store and an exact RoPE relocation operator to eliminate redundant re-prefills, while a rank-m conditioning patch corrects the diffuse, deep-layer deficit caused by cross-chunk dependencies.
- Kamera achieves near-ceiling accuracy across diverse LLM architectures (MLA, GQA, MHA) by treating context as a set of reusable chunks, enabling efficient window operations like reordering, sliding-window survival, and reversible eviction.

---

[HoloAgent-0: A Unified Embodied Agent Framework with 3D Spatial Memory](http://arxiv.org/abs/2606.23565)

- HoloAgent-0: introduces a unified embodied agent framework that organizes heterogeneous robot capabilities into a closed-loop workflow using Embodied AgentOS, Memory Layer, and Skill Layer.
- The framework utilizes a persistent 3D spatial memory and a typed skill interface to enable reliable long-horizon task execution across diverse robot embodiments.
- HoloAgent-0 connects cloud-level reasoning with on-device execution, providing feedback-driven re-planning and monitoring through a standardized ROS2 command/status interface.

---

[VeriEvol: Scaling Multimodal Mathematical Reasoning via Verifiable Evol-Instruct](http://arxiv.org/abs/2606.23543)

- VeriEvol: introduces a scalable framework that transforms low-difficulty image-question seeds into verified training samples using Prompt Difficulty Control and HTV-Agent to ensure high-quality data for LLMs.
- The framework decouples prompt evolution from answer verification, utilizing route-specific operators to increase difficulty and a hypothesis-test verifier to enforce answer reliability before policy updates.
- VeriEvol enables monotonic scaling of visual mathematical reasoning performance by providing a traceable, auditable pipeline that integrates seamlessly with existing GRPO-style RL recipes.

---

[Self-Compacting Language Model Agents](http://arxiv.org/abs/2606.23525)

- SELFCOMPACT: introduces a training-free scaffold that enables LLMs to perform adaptive context compaction by pairing an inline Compaction Tool with a Lightweight Rubric to determine optimal summarization timing.
- The framework utilizes a Reasoning Trajectory to guide the LLM-Agent in deciding when to invoke the Compaction Tool, effectively mitigating context rot without requiring external supervision or fine-tuning.
- By leveraging KV Cache reuse, the approach achieves significant token cost reductions while maintaining or exceeding performance compared to fixed-interval summarization methods across various agentic and reasoning benchmarks.

---

[Concordia: JIT-Compiled Persistent-Kernel Checkpointing for Fault-Tolerant LLM Inference](http://arxiv.org/abs/2606.23521)

- Concordia: introduces a GPU-resident persistent kernel that enables transparent, fault-tolerant LLM inference by combining PTX/SASS instrumentation, JIT-compiled checkpoint handlers, and append-only recovery logging.
- The framework utilizes a Persistent Kernel Executor to perform dirty-page detection at HBM bandwidth, significantly reducing checkpoint latency compared to host-side scanning.
- Concordia integrates with existing LLM serving stacks via an NCCL Wrapper and provides a unified recovery contract that supports cross-architecture migration and rapid failure restoration.

---

[AOHP: An Open-Source OS-Level Agent Harness for Personalized, Efficient and Secure Interaction](http://arxiv.org/abs/2606.23449)

- AOHP: introduces an OS-level agent harness built on AOSP that treats agents as first-class actors to enable personalized service composition, efficient agent interfaces, and secure information flow.
- The architecture replaces app-centric workflows with an agent-native design, utilizing a unified interaction interface and system-managed memory to facilitate cross-app task execution.
- Empirical results demonstrate that AOHP significantly improves task completion rates while reducing LLM token consumption and execution time compared to stock Android.

---

[Detecting Malicious Agent Skills in the Wild using Attention](http://arxiv.org/abs/2606.23416)

- Locate-and-Judge: introduces a two-stage pipeline that detects malicious LLM agent skills by using a small reader LLM to localize suspicious spans via attention ranking, followed by a zero-shot LLM judge to classify them.
- The framework significantly reduces computational costs by focusing the expensive judge component only on the top-K spans identified by the lightweight locator.
- Evaluated on 134k marketplace skills, the approach effectively identifies hidden malicious skills that evade traditional scanners by leveraging instruction-following attention as a robust signal for injection.

---

[REASONINGLENS: Hierarchical Visualization and Diagnostic Auditing for Large Reasoning Models](http://arxiv.org/abs/2606.23404)

- REASONINGLENS: introduces a multi-granularity framework for the hierarchical visualization, automated diagnostic auditing, and systemic profiling of long CoT traces in LLMs.
- The framework utilizes Hierarchical Visualization to structure reasoning into interactive graphs, Agentic Diagnosis to identify errors via Memory, Verification, and Suggestion modules, and Systemic Profiling to analyze model-level reasoning bottlenecks.
- The authors also introduce LENSBENCH, a unified benchmark comprising 130 verified instances to evaluate structural visualization fidelity and the accuracy of automated reasoning error detection.

---

[Litmus: Zero-Label, Code-Driven Metric Specification for Evaluating AI Systems](http://arxiv.org/abs/2606.23403)

- Litmus: introduces a zero-label system that derives justified, per-stage evaluation and monitoring portfolios by interrogating source code and practitioner intent to establish explicit metric-design constraints.
- The framework utilizes a multi-stage pipeline comprising static analysis, LLM-based architecture reconstruction, adversarial criticism, and goal elicitation to ground metrics in specific system components and failure surfaces.
- Litmus outperforms existing evaluation methods by providing broader coverage, near-zero redundancy, and superior label validity across diverse, code-defined AI pipelines without requiring manual labeling at design time.

---

[Superhuman AI for Generals.io Using Self-Play Reinforcement Learning](http://arxiv.org/abs/2606.23348)

- Generals.io AI Framework: introduces a superhuman agent for real-time strategy games trained via self-play reinforcement learning using a JAX-native simulator, a transformer policy, a value head, a policy head, an exponential moving average, and top-advantage filtering.
- The architecture utilizes a transformer torso to process spatial game observations and temporal scoreboard statistics, enabling effective decision-making under imperfect information.
- The research demonstrates that generic policy-gradient methods, when combined with high-throughput simulation and specific training stabilizers, can achieve superhuman performance without human demonstrations or complex reward shaping.

---

[Group selection promotes prosocial prompts in populations of LLM agents](http://arxiv.org/abs/2606.23343)

- Multi-agent simulation framework: introduces a multi-generational evolutionary environment where LLM agents optimize natural-language strategy strings through individual or group-level selection.
- The framework utilizes a donor game to evaluate agent performance, applying either individual- or group-level fitness metrics to determine which strategies are transmitted to subsequent generations.
- Empirical results demonstrate that group selection effectively sustains cooperative behavior in LLM populations, while individual selection leads to the dominance of self-interested strategies and collective defection.

---

[VideoAgent: All-in-One Framework for Video Understanding and Editing](http://arxiv.org/abs/2606.23327)

- VideoAgent: introduces an all-in-one agentic framework for automated video understanding and editing that addresses long-form video planning and multi-agent orchestration challenges.
- The framework utilizes a shot planning agent for coherent narrative structure and a textual-gradient graph optimization mechanism to dynamically compose and refine complex editing pipelines.
- VideoAgent integrates over thirty specialized editing agents and achieves high orchestration success rates while significantly reducing API costs compared to existing LLM-based systems.

---

[TMAX: A simple recipe for terminal agents](http://arxiv.org/abs/2606.23321)

- TMAX: introduces a scalable, difficulty-aware synthetic data generation pipeline and a reinforcement learning recipe for training terminal-using agents.
- The framework utilizes a compositional Data Pipeline to create diverse RL environments, which are then used to train an LLM Policy via DPPO Trainer within a Docker Sandbox.
- TMAX-9B achieves state-of-the-art performance among open-weight models under 10B parameters on Terminal-Bench 2.0, demonstrating effective generalization across tasks and harnesses.

---

[Test-Driven, AI-Assisted Learning: Replacing Lectures with Weekly Closed-Book Tests](http://arxiv.org/abs/2606.23315)

- TDAA (Test-Driven, AI-Assisted Learning): introduces a pedagogical framework that replaces traditional lectures with a weekly cycle of self-paced study and strict closed-book tests, supported by a course-materials harness.
- The framework utilizes a course-materials harness, which integrates an AI writer, AI reviewer, and human approval process to automate the production of learning sheets, validation sheets, and tests at scale.
- By shifting the instructor's role from routine lecturing to designing learning paths and verifying AI-generated content, the model ensures accountability and operational feasibility in proof-heavy courses.

---

[EHR-Complex: Benchmarking Medical Agents for Complex Clinical Reasoning](http://arxiv.org/abs/2606.23301)

- EHR-Complex: introduces a large-scale benchmark for interactive clinical database reasoning, utilizing a MIMIC-IV substrate to evaluate LLM agents on complex, multi-table, and longitudinal EHR analysis tasks.
- The framework employs a construction pipeline that transforms patient records into a Patient Event Graph, extracts Clinical Evidence Paths, and performs SQL Compilation to generate execution-validated tasks.
- Evaluation of LLM agents on EHR-Complex reveals significant challenges in population-level reasoning, medical-code grounding, and SQL logic, highlighting the necessity for robust, interactive clinical reasoning capabilities.

---

[IOI: Decoupling Kinematics and Physics for Interactive World Models](http://arxiv.org/abs/2606.23296)

- IOI: introduces a hybrid interactive world model that decouples deterministic robot kinematics from stochastic environmental dynamics to improve simulation fidelity.
- The framework utilizes a URDF-based kinematic solver and multi-view orthographic renderer to provide geometry-consistent guidance to a diffusion-based video generator.
- By integrating analytical kinematic priors via the MKAI module, IOI mitigates action deviation and state implausibility, achieving robust performance in policy evaluation and OOD generalization.

---

[Towards Root Memories: Benchmarking and Enhancing Implicit Logical Memory Retrieval for Personalized LLMs](http://arxiv.org/abs/2606.23283)

- RootMem: introduces a plug-and-play framework that distills raw user histories into structured Root Memory Units to complement semantic retrieval with personalized decision logic.
- The framework utilizes a collaborative Generator-Judger-Refiner pipeline to construct the IMLogic benchmark, which evaluates the ability of LLMs to retrieve logically critical but semantically distant memories.
- RootMem employs a Root Memory Router to identify relevant units based on Execution Rules and Personalized Logical Evidence, significantly improving the accuracy of LLMs in implicit logical retrieval tasks.

---

[GIF: Locally Sound Geometric Information Flow Control for LLMs](http://arxiv.org/abs/2606.23277)

- GIF (Geometric Information Flow): introduces a semantic framework for tracking information flow in LLMs by using the Jacobian and local output geometry to upper-bound Shannon mutual information between input spans and model outputs.
- The framework utilizes a locally faithful Gaussian surrogate channel to provide a scalable, sound, and quantitative measure of information flow that avoids the overtaint problems of traditional IFC.
- GIF enables efficient, fine-grained security enforcement in agentic systems by surfacing policy-relevant input spans for declassification, significantly reducing token costs compared to full-trajectory LLM judges.

---

[Dynamic multi-agent deep reinforcement learning-based pricing and incentivization approach in multimodal transportation networks](http://arxiv.org/abs/2606.23257)

- Multi-agent deep reinforcement learning framework: introduces a dual-agent approach that reconciles conflicting objectives between public authorities and profit-driven ridesharing providers through coordinated dynamic pricing and incentivization.
- The framework integrates a multimodal macroscopic simulation with two RL agents, where the public authority manages PT incentives to improve system-wide efficiency and equity, while the ridesharing provider adjusts fares to maximize revenue.
- Numerical experiments on the Sioux Falls network demonstrate that an equity-oriented dynamic policy achieves the best trade-off between efficiency, environmental impact, and profitability compared to static baseline strategies.

---

[Wireless Personal Agent: Extending Wireless Intelligence from Networks to Terminals](http://arxiv.org/abs/2606.23255)

- WISPA (Wireless Intelligent Self-evolving Personal Agent): introduces a terminal-side resource management framework that decouples latency-sensitive online execution from offline LLM agent reflection to achieve personalized wireless connectivity.
- The framework utilizes an Online Executor for deterministic, lightweight decision-making and an Offline LLM Agent, comprising an Observation Module, Reflection Module, and Strategy Module, to refine user-specific preference parameters based on historical usage.
- By confining LLM-based reasoning to offline idle windows and employing a bounded parameter update mechanism, the system ensures real-time reliability while adapting to dynamic user preferences and environmental conditions.

---

[RS-Gen: A Multi-Stage Agentic Framework for Reasoning and Search-Augmented Image Generation](http://arxiv.org/abs/2606.23221)

- RS-Gen: introduces a multi-stage agentic framework that reconstructs image generation into a collaborative "questioning-and-solving" workflow using Conversation Memory, Image Router Agent, Intent Analysis Agent, Reasoning &amp; Search Agent, and Image Generation Agent.
- The framework utilizes a Tool Hub and Expert Toolset to integrate external knowledge and logical reasoning, effectively bridging the gap between static model training and real-world complex visual tasks.
- RS-Gen employs a "Generate-Review-Correct" closed-loop mechanism within its Image Generation Agent to ensure high-fidelity, logically consistent outputs through iterative self-correction.

---

[MuPPET: A Benchmark for Contextual Privacy of LLM Assistants in Multi-Party Conversations](http://arxiv.org/abs/2606.23217)

- MuPPET (Multi-Party Privacy Exposure Testing): introduces a benchmark for evaluating contextual privacy risks of LLM assistants in multi-party conversational environments.
- The framework utilizes LLM-as-a-judge to assess privacy leakage and utility by analyzing model responses against user-specific memories and shared group context.
- Experimental results demonstrate that LLMs frequently leak sensitive information in multi-party settings, with smaller open-weights models exhibiting the highest vulnerability.

---

[Memory Contagion: Cross-Temporal Propagation of Evaluator Bias via Agent Memory](http://arxiv.org/abs/2606.23195)

- Memory Contagion: introduces a formal framework to analyze the cross-temporal propagation of evaluator bias through agent memory systems, where biased experiences stored by a source agent influence the performance of future target agents.
- The framework decomposes contagion into content-based and retrieval-based components, demonstrating that biased input is a sufficient cause for contagion even under perfect oracle consolidation.
- Experimental results reveal that consolidation effects are bias-type-dependent, where LLM-based summarization attenuates global length bias but amplifies local authority bias.

---

[Capable but Careless: Do Computer-Use Agents Follow Contextual Integrity?](http://arxiv.org/abs/2606.23189)

- AGENTCIBENCH: introduces a generative evaluation harness that measures contextual-integrity failures in computer-use agents by surfacing realistic, multi-app scenarios where agents must balance task utility against privacy-sensitive information disclosure.
- The framework utilizes an MCTS-based scenario-surfacing engine to generate stress tests across three failure modes: visual co-location, task-ambiguity overshare, and recipient misalignment.
- Evaluation of fifteen frontier agents reveals that high task completion is a poor proxy for disclosure safety, with most agents frequently leaking personal information, though prompt-level interventions can significantly mitigate these failures.

---

[Position: Correct Answer, Wrong Mechanism — When AI Scientists Defend General Claims Their Own Data Contradicts](http://arxiv.org/abs/2606.23175)

- CAWM (Correct Answer, Wrong Mechanism): introduces a framework for evaluating AI scientist systems by measuring task outcome, mechanism fidelity, and epistemic honesty, identifying cases where LLMs produce correct results based on physically incorrect or over-generalized reasoning.
- The research demonstrates that LLMs often fail to self-apply mechanism-fidelity verification, leading to "Correct Answer, Wrong Mechanism" failures where agents defend observables with physics contradicted by their own simulation data.
- The paper proposes a lightweight regime-shift verification protocol and companion recomputation as necessary gates for co-author-level trust in autonomous scientific discovery pipelines.

---

[Decomposing Financial Market Dynamics via Mechanism Analysis in an Evolutionary Multi-Agent Simulation](http://arxiv.org/abs/2606.23158)

- Evolutionary Multi-Agent Simulation framework: introduces a modular ABM architecture that decomposes market dynamics by isolating four pluggable mechanisms to identify their specific control over emergent market properties.
- The framework utilizes single-mechanism interventions to demonstrate that selection operators drive diversity, microstructure governs realism, and behavioral bias influences fragility.
- The research provides a systematic decomposition of market dynamics, revealing that consensus network topology acts as an honest null with no robust effect on emergent market outcomes.

---

[Neural Parameter Calibration for Finite-State Mean Field Games](http://arxiv.org/abs/2606.23155)

- Neural Parameter Calibration for Finite-State Mean Field Games: introduces a fully differentiable framework for learning trajectory-wise parameters of finite-state MFGs from macroscopic population data using a Neural Network φθ, an MFG Solver Φ, and Implicit Differentiation.
- The framework treats the fixed-point equilibrium solver as an implicit neural network component, enabling efficient gradient computation via the adjoint method without unrolling solver iterations.
- The approach is validated across synthetic and real-world datasets, demonstrating robustness to noise and the ability to perform counterfactual analysis through the forward-looking nature of the MFG formulation.

---

[Rising From the Ashes: How Agentic AI is Unblocking Challenges in Cybersecurity](http://arxiv.org/abs/2606.23138)

- Agentic AI Framework: introduces a conceptual mapping of emergent agentic AI capabilities to long-standing cybersecurity bottlenecks, leveraging Natural language understanding, Processing large amounts of information, Cognitive stamina, Generalization and replicability, and Multi-disciplinary knowledge.
- The paper evaluates 16 case studies across systems security, software security, CTI, and attack detection to demonstrate how these agentic capabilities can automate labor-intensive and knowledge-intensive security tasks.
- It highlights that while agentic AI offers a path to scalable security, it necessitates rigorous verification and security-by-design to prevent the amplification of existing vulnerabilities through autonomous agents.

---

[Understanding the (In)Security of Vibe-Coded Applications](http://arxiv.org/abs/2606.23130)

- Vulnerability Analysis Framework: introduces a multi-agent system that combines Claude Code, GitHub Copilot, OpenAI Security Best Practices Skill, Antigravity Awesome Skills, Claude Sonnet 4.6, GPT-5.3-Codex, a Validation Agent, and Human Reviewers to systematically identify and validate security vulnerabilities in vibe-coded applications.
- The framework employs a 2x2 auditing design using two agent frameworks and two security skill sets to generate independent reports, which are then deduplicated and validated through automated and manual processes.
- This research identifies eight recurring failure modes categorized into memory, objective, and knowledge defects that contribute to widespread security vulnerabilities in vibe-coded applications.

---

[Managing Procedural Memory in LLM Agents: Control, Adaptation, and Evaluation](http://arxiv.org/abs/2606.23127)

- AFTER (A Benchmark for Procedural Skill Transfer in LLM Agents): introduces a benchmark and evaluation framework for measuring how procedural memory transfers across tasks, roles, and LLM backbones using AFTER, EVOLUTION, SKILL.md, Reflector, Adapter, and Trace Pool.
- The framework utilizes EVOLUTION to manage the lifecycle of SKILL.md artifacts, employing a Reflector to iteratively refine procedural knowledge based on execution traces.
- Experiments demonstrate that procedural memory evolved from diverse multi-model traces significantly improves cross-model generalization while revealing that role-specific specialization can hinder cross-role transfer.

---

[A Matter of Time: Towards a General Theory of Agency](http://arxiv.org/abs/2606.23122)

- Temporally Parametrized (F, A)-systems: introduces a graded organizational theory of agency by unfolding semantically closed systems across characteristic timescales to reveal endogenous anticipatory structures.
- The framework redescribes these temporally unfolded organizations as history-dependent ADBNs, where dependencies between components (A, B, C, D, E) and interface processes (X, Y, Z) are constrained by their respective timescales (ϕ, ψ, θ, α, β).
- This approach provides a formal hierarchy from proto-agential chemical systems to robust agents, enabling the operational distinction between autonomy, goal-directedness, agency, and open-endedness through measurable metric profiles.

---

[Self-Evolution for Multi-Turn Tool-Calling Agents via Divergence-Point Preference Learning](http://arxiv.org/abs/2606.23112)

- ToolGraph + DPO: introduces a framework that improves LLM tool-calling reliability by combining structural graph-based orchestration with divergence-point preference learning.
- The system utilizes ToolGraph to provide structural guidance via schema-derived topology and experience-based edge weights, while DPO refines the LLM policy using preference pairs extracted from successful and failed trajectories.
- By aligning training and deployment contexts and filtering preference data against action-level correctness annotations, the framework enables effective within-benchmark self-evolution for multi-turn agents.

---

[Cognitive Digital Twins: Ethical Risks and Governance for AI Systems That Model the Mind](http://arxiv.org/abs/2606.23094)

- CDT (Cognitive Digital Twin): introduces a governance framework organized around Authority, Autonomy, Access and Control, Accountability, and Availability to address the ethical risks of AI systems that model, simulate, and act as a person's cognition.
- The paper argues that CDTs require governance at the level of cognitive representation itself, as these systems can act as proxies or infrastructures through which human cognition is simulated and operationalized.
- The authors propose concrete requirements for high-risk CDTs, including layered consent, purpose-binding enforcement, and traceability, to mitigate risks such as misrepresentation, epistemic authority shifts, and shadow twinning.

---

[Safety in Self-Evolving LLM Agent Systems: Threats, Amplification, and Case Studies](http://arxiv.org/abs/2606.23075)

- MLAS (Module–Lifecycle Attack Surface) framework: introduces a systematic security analysis of self-evolving LLM agents by mapping threats across five functional modules and five evolutionary lifecycle stages.
- The paper identifies seven cross-cutting amplification effects, including generational accumulation and optimizer–optimizee collapse, which transform transient attacks into persistent, self-reinforcing, and lineage-wide security threats.
- Comparative case studies of OpenClaw and Hermes demonstrate that evolution-native designs significantly expand the attack surface and bypass static security scanners, necessitating evolution-aware defense architectures.

---

[Training Open Models for Agentic Phone Use](http://arxiv.org/abs/2606.23049)

- PhoneBuddy: introduces a training recipe for agentic phone use that combines a real-app environment with a mock-app environment, PhoneWorld, to improve task completion through a shared SFT stage and mixed RL.
- The framework utilizes a Qwen3.5-4B backbone and leverages PhoneWorld to provide scalable, resettable, and automatically verifiable interaction, complementing the high-fidelity but costly real-app environment.
- Empirical results demonstrate that combining real-app and mock-app RL significantly outperforms individual training approaches, particularly for single-app and mini-app tasks, while highlighting persistent challenges in cross-app workflows.

---

[UECP: Uncertainty-Enhanced Collaborative Perception](http://arxiv.org/abs/2606.23046)

- UECP (Uncertainty-Enhanced Collaborative Perception): introduces a collaborative perception framework that utilizes a physically-grounded uncertainty map to guide multi-agent feature fusion, effectively mitigating collaborative noise.
- The framework employs an Uncertainty-Aware Pyramid Fusion (UAPF) module, which integrates Uncertainty-Weighted Downsampling (UWD) and Uncertainty-Guided Residual Fusion (UGRF) to enhance robustness and detection precision.
- By decoupling uncertainty estimation from detection head training, UECP provides an unbiased, scenario-aware signal that improves performance across various autonomous driving benchmarks.

---

[A Stackelberg Framework for Resource-Aware LLM Agents: Learning, Repair, and Conditional Guarantees](http://arxiv.org/abs/2606.23026)

- Stackelberg Framework for Resource-Aware LLM Agents: introduces a contextual leader-follower game to govern LLM agent resource allocation by balancing quality targets and cost incentives against executor actions.
- The framework utilizes a Controller that commits to quality and budget signals, while an Executor responds with context, prompt, and tool usage actions to optimize performance under finite computational constraints.
- The approach incorporates real-API calibration and action-space projection to repair learned policies, ensuring stable and safe resource governance in multi-turn LLM agent interactions.

---

[Group-Graph Policy Optimization for Long-Horizon Agentic Reinforcement Learning](http://arxiv.org/abs/2606.22995)

- G2PO (Group-Graph Policy Optimization): introduces a reinforcement learning framework for long-horizon agentic tasks that transforms interaction trajectories into a global state-transition graph to enable fine-grained credit assignment.
- The framework utilizes State Group Graph to aggregate identical observations across trajectories, significantly reducing variance in state-value estimation compared to single-trajectory methods.
- G2PO incorporates Edge-Centric Advantage Estimation to prioritize critical transitions by globally standardizing Temporal Difference errors, effectively guiding LLMs toward task completion with minimal computational overhead.

---

[Distilling Collaborative Dynamics into Latent Space for Implicit Coordination in Decentralized Multi-Agent Manipulation](http://arxiv.org/abs/2606.22982)

- CLS-DP (Collaborative Latent Space–conditioned Diffusion Policy): introduces a decentralized multi-agent framework that enables implicit coordination by distilling privileged multi-agent dynamics into a latent space during centralized training, which is then inferred by each agent from local observations at deployment.
- The framework utilizes a contextualizer to encode local RGB observations and task instructions into a collaborative latent, which conditions a decentralized diffusion policy to anticipate teammate behaviors without explicit communication.
- By employing a two-stage training process and discarding privileged kinematics modules at inference, CLS-DP achieves superior parameter efficiency and scalability compared to centralized baselines in multi-arm manipulation tasks.

---

[StatABench: Dataset and Framework for Evaluating Statistical Analysis Capabilities of LLMs](http://arxiv.org/abs/2606.22977)

- StatABench: introduces a comprehensive benchmark for evaluating LLMs' statistical analysis capabilities through closed-form questions and open-ended modeling tasks.
- The framework utilizes SAToolKit for tool-grounded reasoning and employs an LLM-as-Judge protocol to assess complex, open-ended statistical reports.
- Experimental results reveal a significant tool-integration tax across diverse LLMs, highlighting persistent challenges in methodological decision-making and end-to-end statistical modeling.

---

[Evo-RAD: Navigating Rare Retinal Disease Diagnosis via Self-Evolving Agentic Retrieval](http://arxiv.org/abs/2606.22955)

- Evo-RAD: introduces a self-evolving agentic retrieval framework that reformulates evidence acquisition as a Markov Decision Process to improve rare retinal disease diagnosis.
- The framework utilizes a Graph Policy Network to iteratively refine a reference set through DELETE, INSERT, and TERMINATE operations, optimized via Group Relative Policy Optimization (GRPO) with a homogeneity-aware reward.
- By dynamically suppressing hub-driven distractors and incorporating clinically concordant samples, the agentic approach achieves superior diagnostic performance compared to static retrieval and parameter-efficient fine-tuning methods.

---

[Plans Don’t Persist: Why Context Management Is Load Bearing for LLM Agents](http://arxiv.org/abs/2606.22953)

- Replay Pairing: introduces a diagnostic framework to measure plan persistence in LLMs by comparing hidden-state cosine distances between trajectories with and without plan history.
- The study demonstrates that LLM agents typically treat plans as context-time objects that decay rapidly within one step, rather than as persistent internal states.
- The authors identify a reasoning-trace confound in reasoning models and propose strict stripping to accurately isolate plan-related signals, further validating that naive plan eviction significantly degrades agent performance.

---

[ENVS: Environment-Native Verified Search for Long-Horizon GUI Agents](http://arxiv.org/abs/2606.22948)

- ENVS: introduces a training-time search-and-filter pipeline that leverages environment-native verification to construct balanced, high-quality supervised datasets for GUI agents.
- The framework decouples trajectory discovery from policy optimization by using a Frozen Policy to explore OSWORLD Virtual Machines, followed by a Data Curator that applies global balancing to the collected trajectories.
- To evaluate robustness, the paper introduces OSWORLD-NOISY, a benchmark that injects recoverable desktop interruptions to test an agent's ability to refocus, dismiss, or recover during task execution.

---

[When Agents Commit Too Soon: Diagnosing Premature Commitment in LLM Agents](http://arxiv.org/abs/2606.22936)

- LLM Agents: introduces a diagnostic framework for detecting premature commitment, where agents settle on an interpretation early and defend it, by measuring cross-run hidden-state convergence.
- The framework utilizes activation similarity at specific reasoning steps to predict trajectory consistency across multiple LLM architectures, including Llama-3.1, Qwen-2.5, and Phi-3.
- The research demonstrates that while commitment signals reliably track process consistency, they are correctness-agnostic, meaning they identify settled trajectories regardless of whether the agent is right or wrong.

---

[Intent-Governed Tool Authorization for AI Agents](http://arxiv.org/abs/2606.22916)

- IGAC (Intent-Governed Access Control): introduces a server-side authorization layer that binds AI agent tool use to the user's expressed intent through intent certificates, session policy, and consistency checks.
- The framework operates as an upstream governance layer over the OpenPort effect-control substrate, ensuring that agent actions remain within the bounds of the user's current request.
- IGAC utilizes manifest filtering and consistency gating to prevent overbroad tool usage and payload expansion, treating LLM-based planners as untrusted advisors rather than authoritative principals.

---

[From Fragments to Paths: Task-Level Context Recovery for Large Industrial Codebases](http://arxiv.org/abs/2606.22906)

- DEEPDISCOVERY: introduces a two-stage Location–Inference framework that identifies high-confidence task anchors and expands over a multi-relational repository graph to recover complete task-relevant context under budget constraints.
- The method utilizes metadata-first context construction to preserve structural coverage while selectively loading full-text content, thereby optimizing LLM context usage for complex software engineering tasks.
- Evaluations on industrial codebases and SWE-bench Verified demonstrate that DEEPDISCOVERY consistently improves task-relevant file recovery and downstream LLM performance compared to traditional fragment-retrieval and GraphRAG-style approaches.

---

[Agent-as-a-Router: Agentic Model Routing for Coding Tasks](http://arxiv.org/abs/2606.22902)

- ACRouter (Agentic Coding Router): introduces a framework that formalizes model routing as a Context-Action-Feedback loop to address information deficit in LLM selection for coding tasks.
- The framework utilizes an Orchestrator to select models, a Verifier to provide execution-grounded feedback, and a Memory module to accumulate experience for future routing decisions.
- The research introduces CodeRouterBench, a comprehensive evaluation environment with 10K tasks, demonstrating that ACRouter achieves lower cumulative regret and better generalization than static routing baselines.

---

[DynamicMem: A Long-Horizon Memory Benchmark in Real-World Settings](http://arxiv.org/abs/2606.22877)

- DynamicMem: introduces a synthetic benchmark for evaluating long-horizon memory in LLM agents by constructing 15-month, user-consistent trajectories across 16 applications.
- The framework decomposes user profiles into attributes, habits, and preferences, which evolve under causally grounded drivers to test memory retention and update capabilities.
- Benchmarking reveals that while aggregate accuracy hides performance degradation, over 93% of failures originate from the memory system's retrieval rather than the answer-generation LLM.

---

[When AUC 0.998 Is Not Enough: A Candidate Evaluation Protocol for Hidden-State Probes of Indirect Prompt Injection in Multimodal Computer-Use Agents](http://arxiv.org/abs/2606.22864)

- Candidate Evaluation Protocol for Hidden-State Probes: introduces a diagnostic framework for validating hidden-state probes in multimodal computer-use agents by pairing reported AUC metrics with specific control sets to distinguish malicious-content detection from surface-level artifacts.
- The framework utilizes a Mind2Web trajectories-based replay protocol to evaluate a frozen multimodal computer-use agent, employing a linear probe for hidden-state extraction alongside C1 text-side falsifier and C2 visual overlay controls to identify shortcut-driven failure modes.
- The research demonstrates that high headline AUC scores can be misleading, necessitating the use of trajectory-level cluster bootstrap and nuisance-matched controls to ensure that probes are actually detecting malicious instruction content rather than OCR-density or template-based surface statistics.

---

[AI Scientists as Engines of Discovery: A Case for Development within Reformed Institutions](http://arxiv.org/abs/2606.22859)

- Denario: introduces a multi-agent framework for scientific discovery that utilizes a Generation agent, Critic agent, Verification agent, Controller agent, Reasoning layer, and External tools to automate the research cycle.
- The architecture enables an internal dialectic among specialized agents to traverse model parameter spaces and accelerate scientific discovery beyond human capacity.
- The paper argues that institutions must be redesigned to support AI scientists through improved verification, accountability, interpretability, and dual-use safety protocols.

---

[RaMem: Contextual Reinstatement for Long-term Agentic Memory](http://arxiv.org/abs/2606.22844)

- RaMem (Contextual Reinstatement for Agentic Memory): introduces a framework that mitigates context collapse by anchoring memory fragments to episodic conditions and performing validity-aware retrieval.
- The framework utilizes LLMClient, EmbeddingModel, VectorStore, MemoryBuilder, HybridRetriever, and AnswerGenerator to transform retrieved fragments into contextually verifiable evidence.
- RaMem improves long-term memory performance by prioritizing context-compatible memories while retaining content-relevant candidates as fallback evidence during synthesis.

---

[RLM-Cascade: Response-Level Speculative Decoding for Cost-Efficient LLM API Serving](http://arxiv.org/abs/2606.22840)

- RLM-Cascade: introduces a response-level speculative decoding proxy system that reduces LLM API costs by routing requests between a fast draft model and a capable verify model.
- The system utilizes a rule-based router to classify agentic turns, enabling the SKIPPED path for simple requests and a draft-then-verify pipeline for complex tasks.
- By treating the full response as the unit of speculation, the framework operates over standard HTTP APIs without requiring access to internal model logits or shared vocabularies.

---

[Active Inference as the Test-Time Scaling Law for Physical AI Agents](http://arxiv.org/abs/2606.22813)

- Active Inference as the Test-Time Scaling Law for Physical AI Agents: introduces a novel test-time scaling law for physical AI agents grounded in active inference that enables generalization in unforeseen scenarios by dynamically updating policies through surprise-minimizing reasoning.
- The framework utilizes a world model at the network edge to detect prediction errors and trigger a transition from habitual policy execution to deliberative reasoning, effectively scaling the agent's policy at test time.
- By modeling the resolution of prediction errors as a variational inference problem, the approach enables physical AI agents to continuously learn and adapt to non-stationary environments without requiring retraining.

---

[Does the Same Token Mean the Same State? MoE Routing as Signal for Reasoning Control](http://arxiv.org/abs/2606.22798)

- RAD (Routing Agreement Decoding): introduces a method for selecting high-quality LLM rollouts by analyzing sparse MoE routing states as a white-box agreement signal, utilizing MoE Router, Anchor-Conditioned Routing, Weighted-Jaccard K-NN, Consensus Matrix, Routing Density Selector, and DeepConf Confidence Signal.
- The framework identifies dense routing neighborhoods that align with answer basins, enabling effective selection in open-ended or lexically diverse tasks where traditional string-based voting fails.
- RAD operates as a consensus-based selector that aggregates routing agreement rather than verifying truth, providing competitive performance to majority voting in well-posed settings and superior results in code generation and agentic tasks.

---

[Breaking the Evaluation Paradox: Evaluating High-Entropy Search with Computationally Irreducible Constraints](http://arxiv.org/abs/2606.22783)

- VERITAS (Verifiable Traversal Assessment for Search): introduces a benchmark that replaces semantic filters with computationally irreducible cryptographic hash constraints to force LLMs into genuine exhaustive search.
- The framework utilizes Search, Visit, Exec Python, and Answer components to evaluate an agent's ability to systematically traverse large, unstructured search spaces without relying on search engine shortcuts.
- By requiring agents to find items matching specific hash values, VERITAS provides an automatically verifiable, scalable, and difficulty-tunable evaluation paradigm for high-entropy search tasks.

---

[Noise Is Signal: Density-Based Outliers as Leading Indicators of Occupational Emergence in Labor Market Text](http://arxiv.org/abs/2606.22769)

- EOS: introduces a framework for detecting emerging occupations by analyzing the semantic coherence of noise-class postings in high-dimensional embedding spaces.
- The framework utilizes INSTRUCTOR-xl, UMAP, and HDBSCAN to identify pre-cluster noise groups, which are then evaluated using the EOS metric to predict future occupational consolidation.
- By demonstrating that density-based outlier scores are uninformative for emergence, the paper establishes that semantic coherence within the noise class serves as a reliable leading indicator for new job roles.

---

[Cooperative-ORCA*: Real-Time Proactive Deadlock Avoidance for Continuous-Space Multi-Agent Navigation](http://arxiv.org/abs/2606.22757)

- C-ORCA* (Cooperative Optimal Reciprocal Collision Avoidance): introduces a continuous-space multi-agent navigation framework that integrates global guidance paths with local collision avoidance to proactively resolve deadlocks using MAPFPlanner, CorridorDetector, DependencyBuilder, StringPulling, WaypointManager, DriftModeController, and ORCAVelocitySolver.
- The framework utilizes pre-computed guidance paths and dynamic dependency detection to switch agents between standard and drift modes, effectively preventing congestion in narrow corridors.
- By proactively managing agent interactions through waypoint updates and adaptive velocity control, the approach significantly improves success rates and reduces flowtime compared to reactive baseline methods.

---

[HERCULES: An Open-Source Simulation Framework for Heterogeneous Multi-Robot SLAM, Collaborative Perception, and Exploration](http://arxiv.org/abs/2606.22756)

- HERCULES: introduces an open-source, Unreal Engine 5-based simulation framework designed for heterogeneous multi-robot autonomy, featuring a unified navigation stack, synchronized data-collection, and support for concurrent UAV-UGV operations.
- The framework resolves architectural conflicts in prior simulators to enable concurrent multi-robot simulation, providing specialized controllers, physics-based thermal and night-vision sensors, and dynamic environmental processes for realistic testing.
- HERCULES facilitates research in collaborative SLAM, cooperative 3D object detection, and closed-loop multi-robot exploration by providing a scalable, photorealistic testbed with ready-to-run benchmarks and sim-to-real transfer capabilities.

---

[GRADE: Graph Representation of LLM Agent Dependency and Execution](http://arxiv.org/abs/2606.22741)

- GRADE: introduces a unified two-layer graph representation for LLM agent runs that separates observed execution flow from graded state-dependency reliance to enable failure diagnosis.
- The framework utilizes an attachment model to grade dependency edges as observed, declared, or inferred, addressing the blind spot where standard traces fail to record state reliance.
- By pricing the dependency layer's marginal lift over the free execution layer, GRADE identifies that dependency structure provides transferable failure-prediction signals that generic graph networks often misread due to structural degeneracy.

---

[GroundEval: A Deterministic Replacement for LLM-as-Judge in Stateful Agent Evaluation](http://arxiv.org/abs/2606.22737)

- GroundEval: introduces a judge-free framework for evaluating LLM agents by verifying their evidence paths against deterministic state contracts rather than relying on LLM-as-judge plausibility.
- The framework utilizes a machine-readable contract comprising an event log, artifact corpus, access policy, and evaluation configuration to score agent performance across Perspective, Counterfactual, and Silence tracks.
- GroundEval provides structured diagnostics and a compliance-adjusted scoring model to detect state-invalid correctness, such as temporal leakage, permission violations, and ungrounded causal claims.

---

[Closed-loop Auto Research for Molecular Property Prediction: Discovering and Certifying Generalizable Improvements](http://arxiv.org/abs/2606.22731)

- Closed-loop Auto Research: introduces a framework where LLM-agents iteratively propose and execute interventions across feature, model, and data axes to improve molecular property prediction pipelines.
- The framework utilizes a file-level ablation lock to isolate research axes and a held-out certification protocol to distinguish genuine transferable discoveries from validation-selected artifacts.
- The system incorporates a leakage-safe filter to audit external data acquisition, ensuring that improvements are not derived from test set contamination or distribution shifts.

---

[Safe and Generalizable Hierarchical Multi-Agent RL via Constraint Manifold Control](http://arxiv.org/abs/2606.24010)

- HMM (Hierarchical Manifold Multi-Agent PPO): introduces a hierarchical MARL framework that decouples high-level cooperative planning from low-level safety enforcement using a constraint manifold.
- The framework utilizes a high-level policy for multi-agent coordination and a low-level constraint manifold safe controller to project nominal actions onto a safe tangent space, ensuring hard safety constraints without per-timestep quadratic programming.
- By offloading safety to a fixed low-level controller, the approach enables stable, stationary learning for the high-level policy while providing formal safety guarantees and strong generalization across varying agent and obstacle counts.

---

[ChartWalker: Benchmarking the Cross-Chart RAG Task with Hierarchical Knowledge Graphs](http://arxiv.org/abs/2606.23997)

- ChartWalker: introduces a framework for constructing challenging cross-chart RAG tasks by organizing chart entities into a Hierarchical Knowledge Graph and synthesizing reasoning paths via a Structure-aware Sampling Algorithm.
- The framework includes ChartWalker-Bench, a benchmark with 564 multi-hop QA instances, and ChartWalker-Agent, which utilizes a VLM-based search agent to navigate the knowledge graph for iterative evidence acquisition.
- Experimental results demonstrate that graph-based retrieval and agentic reasoning significantly improve performance on complex multi-hop queries compared to static RAG pipelines.

---

[EMAgnet: Parameter-Space EMA Regularization for Policy Gradient Self-Play in Large Games](http://arxiv.org/abs/2606.23995)

- EMAgnet: introduces a parameter-space exponential moving average regularization method for PPO self-play that adapts to the agent's evolving strategy by maintaining a moving target of network weights.
- The framework utilizes a Policy Network, Magnet Parameters, and an EMA Update to effectively regularize toward viable actions while ignoring strictly dominated strategies in complex game environments.
- By incorporating a KL Divergence Loss term, the approach enables stable convergence in two-player zero-sum games with large strategy spaces where uniform regularization typically fails.

---

[Learning to Trigger: Reinforcement Learning at the Large Hadron Collider](http://arxiv.org/abs/2606.23993)

- GFPO: introduces a self-driving trigger framework that adapts selection thresholds online using DQN, GRPO, GFPO-F, and GFPO-FR to maintain stable background rates while maximizing signal efficiency.
- The framework utilizes a Recurrent Encoder to process event sequences and a Safety Shield to enforce operational constraints, ensuring robust performance under non-stationary physical conditions.
- GFPO-F and GFPO-FR address the zero-feasibility failure mode of standard policy optimization by enforcing rate constraints before advantage normalization, demonstrating superior generalization to real collision data.

---

[Critique of Agent Model](http://arxiv.org/abs/2606.23991)

- GIC (Goal-Identity-Configurator): introduces a general-purpose agent architecture that internalizes agency by combining a Belief Encoder, Goal Decomposer, Identity Evolver, Configurator, Simulative Planner, and Actor, all operating with a separately trained World Model and Critic.
- The framework distinguishes between agentic systems, which rely on external scaffolding, and agentive systems, which derive capabilities endogenously through internalized modules for planning, self-regulation, and learning.
- GIC enables persistent, self-directed operation by allowing the agent to autonomously manage its deliberative mode, goal decomposition, and identity evolution, thereby improving auditability and safety compared to monolithic LLM-based agent designs.

---

[Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets](http://arxiv.org/abs/2606.23961)

- Nexus Sampling: introduces a training-free KV cache eviction method that replaces deterministic top-K selection with Nexus scoring and weighted reservoir selection to prevent monotone marginal erosion.
- The framework utilizes an iterative walk to identify bridge tokens that anchor strongly-connected clusters, ensuring these are preserved alongside marginal tokens via weighted reservoir sampling.
- By treating KV cache eviction as a streaming problem, Nexus Sampling maintains long-run token survival through a product-over-steps probability, significantly outperforming existing methods on retrieval-heavy long-context tasks.

---

[When Retrieval Metrics Mislead: Measuring Policy Signal in Long-Horizon Tool-Use Agents](http://arxiv.org/abs/2606.23937)

- SSDG (Structured State Decision Gate): introduces a framework for evaluating policy-conditioned tool-use agents by comparing structured decision-state representations against raw trajectory inputs.
- The framework utilizes a generator to distill dialogue, tool outputs, and policy assertions into a compact structured state, which significantly improves the macro-F1 performance of LLM classifiers compared to raw text.
- The study demonstrates that exact-match retrieval recall is a pessimistic proxy