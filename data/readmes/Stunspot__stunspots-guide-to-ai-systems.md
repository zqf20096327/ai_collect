<p align="center">
  <img src="./docs/assets/brand/stunspots-guide-readme-hero.png" alt="">
</p>

# Stunspot’s Guide to AI Systems

**The AI Engineering Systems Canon**  
*A model-loadable operating canon for production AI systems.*

![Status: public canon](https://img.shields.io/badge/status-public_canon-darkgreen)
![Reports: 37](https://img.shields.io/badge/reports-37-blue)
![Volumes: 12](https://img.shields.io/badge/volumes-12-blueviolet)
![License: CC BY 4.0](https://img.shields.io/badge/license-CC_BY_4.0-darkgrey)

*Stunspot’s Guide to AI Systems* is a Markdown-native, model-loadable operating canon for production AI systems.

Its primary reader is the model. Its beneficiary is the human designing, building, evaluating, operating, or governing the system.

In an AI workspace, RAG pipeline, long-context session, agent memory layer, project knowledge base, or retrieval corpus, the Guide supplies structured doctrine, field vocabulary, decision frameworks, failure maps, design patterns, evaluation logic, and operational heuristics as a common frame for reasoning about the whole system.

This is not an agent tutorial or a framework cookbook. Agentic systems are one layer of a broader production discipline spanning model steering, context architecture, corpus engineering, retrieval, model lifecycle, runtime mechanics, agents, Skills, Augments, tools, multimodal interfaces, security, resilience, evals, telemetry, governance, product architecture, and system doctrine.

Human readers can use it as a field manual and architectural reference. Its deeper purpose is practical augmentation: supporting engineers, builders, prompt designers, product leads, and technical decision-makers as they turn vague AI ambition into precise, build-aware system decisions.

At its core is a simple engineering premise:

> AI systems are probabilistic cognitive engines operating inside deterministic operational environments. Good AI engineering means designing the interfaces, constraints, context, tools, feedback loops, and human controls that let that probabilistic core behave usefully, safely, and economically under real conditions.

Use it as reference material.  
Use it as RAG substrate.  
Use it as project knowledge.  
Use it as doctrine for AI agents tasked with designing, critiquing, or improving AI systems.

Part of the Stunspot’s Guide to… Advanced Knowledge Base Library
Browse the full library: 
[Gateway Repo](https://github.com/Stunspot/stunspots-guides) · [stunspot.com](https://stunspot.com/#guides)

---

## Start Here

- [Canon Map](./docs/canon-map.md)
- [Agents, Skills, Augments, Tools, and Capabilities](./docs/agents-skills-augments-tools-and-capabilities.md)
- [Worked Example — Same Task, Three Prompting Paradigms](./docs/worked-example-promptcraft.md)
- [Worked Example — A Refund Agent Without Giving the Model a Wallet](./docs/worked-example-refund-agent.md)
- [How to Use This Canon](./docs/how-to-use-this-canon.md)
- [Choose a Knowledge Pack](./docs/knowledge-packs.md)

### Core Volumes

- [Volume 1 — The Informational/Epistemic Layer](./docs/volume-01/)
- [Volume 2 — Knowledge, Data, and Corpus Engineering](./docs/volume-02/)
- [Volume 3 — Model Lifecycle and Adaptation](./docs/volume-03/)
- [Volume 4 — Runtime Architecture and Inference Mechanics](./docs/volume-04/)
- [Volume 5 — Agentic Systems and Tool-Using Architectures](./docs/volume-05/)
- [Volume 6 — Multimodal and Interface-Controlling Systems](./docs/volume-06/)
- [Volume 7 — Failure, Security, and Hostile Environments](./docs/volume-07/)
- [Volume 8 — Resilience, Degraded Modes, and Human Trust](./docs/volume-08/)
- [Volume 9 — Observability, Evaluation, and Verification](./docs/volume-09/)
- [Volume 10 — Operations, Governance, and Lifecycle Management](./docs/volume-10/)
- [Volume 11 — Product, Business, and Organizational Architecture](./docs/volume-11/)
- [Volume 12 — Engineering Method and System Doctrine](./docs/volume-12/)

## Knowledge Packs

The canonical source reports live in [`/docs/`](./docs/).

For AI Projects, RAG systems, NotebookLM-style tools, and long-context workspaces, the Guide also includes bundled knowledge packs:

| Pack | Location | Best Use |
|---|---|---|
| **By Volume** | [`/knowledge-packs/by-volume/`](./knowledge-packs/by-volume/) | Twelve files, one per canon volume. |
| **By Part** | [`/knowledge-packs/by-part/`](./knowledge-packs/by-part/) | Recommended default. Five larger files grouped by major canon part. Useful when file count is limited. |
| **Omnibus** | [`/knowledge-packs/omnibus/`](./knowledge-packs/omnibus/) | Full canon in one file. Best for archival, local search, or systems that handle large single-file knowledge sources well. |

Most users should start with the **By Part** pack. It preserves the canon’s structure while avoiding both extremes: one giant file or 37 separate reports.

---

## What This Canon Covers

The canon is organized across **12 volumes** and **37 reports**, from **AI-ENG-A** through **AI-ENG-AK**.

It covers:

- model steering, prompt semantics, harness engineering, and adaptation choice
- context architecture, memory, state management, and the Tenure Principle
- inference economics, cost attribution, latency, throughput, and system margins
- corpus engineering, source authority, data provenance, and knowledge hygiene
- RAG architecture, retrieval pipelines, hybrid search, semantic injection, and citation quality
- model selection, fine-tuning, LoRA, preference tuning, distillation, and regression control
- runtime architecture, KV cache mechanics, quantization, routing, serving, and deployment topology
- agent orchestration, tool contracts, action verification, and bounded autonomy
- multimodal document, image, table, chart, video, speech, browser, and interface-control systems
- hallucination, malformed output, prompt injection, data leakage, supply-chain risk, and resource abuse
- fallback chains, degraded modes, trust calibration, human review, and high-impact workflow governance
- telemetry, traces, evals, golden sets, verification artifacts, and reproducibility
- AI operations, incident response, rollback, governance, compliance, and sustainable infrastructure
- AI product architecture, adoption systems, build/buy/vendor strategy, and engineering doctrine

---

## Who This Is For

This canon is written for people building or directing real AI systems:

- **AI engineers** designing production LLM systems
- **software engineers** adapting to probabilistic model behavior
- **prompt engineers** moving beyond surface promptcraft into system design
- **RAG and knowledge-system builders** working with retrieval, corpora, context, memory, and citations
- **agent builders** designing tool-using systems with bounded autonomy
- **technical founders and product leads** deciding where AI belongs in workflows
- **AI governance, security, and operations teams** responsible for risk, auditability, and reliability
- **serious learners** who want a map of the field instead of scattered tutorials and benchmark gossip

---

## How To Read It

The canon can be read straight through, but most readers should enter through their problem.

### If you are building RAG or knowledge systems

Start with:

1. [AI-ENG-A — Model Steering](./docs/volume-01/ai-eng-a-model-steering.md)
2. [AI-ENG-B — Context Architecture](./docs/volume-01/ai-eng-b-context-architecture.md)
3. [AI-ENG-D — Corpus Engineering](./docs/volume-02/ai-eng-d-corpus-engineering.md)
4. [AI-ENG-E — The Retrieval Pipeline](./docs/volume-02/ai-eng-e-retrieval-pipeline.md)
5. [AI-ENG-F — Knowledge Freshness, Conflict Detection & Context Rot Prevention](./docs/volume-02/ai-eng-f-knowledge-freshness-conflict-detection-context-rot-prevention.md)

### If you are building agents

Start with:

1. [AI-ENG-A — Model Steering](./docs/volume-01/ai-eng-a-model-steering.md)
2. [AI-ENG-M — Agentic Orchestration](./docs/volume-05/ai-eng-m-agentic-orchestration.md)
3. [AI-ENG-N — Tool Contracts](./docs/volume-05/ai-eng-n-tool-contracts.md)
4. [AI-ENG-O — Action Verification](./docs/volume-05/ai-eng-o-action-verification.md)
5. [AI-ENG-S — Production Pathologies](./docs/volume-07/ai-eng-s-production-pathologies.md)

### If you are selecting or serving models

Start with:

1. [AI-ENG-C — The Economic Physics of Inference](./docs/volume-01/ai-eng-c-economic-physics-of-inference.md)
2. [AI-ENG-G — Model Selection](./docs/volume-03/ai-eng-g-model-selection.md)
3. [AI-ENG-J — Throughput Mechanics](./docs/volume-04/ai-eng-j-throughput-mechanics.md)
4. [AI-ENG-K — Weight Dynamics](./docs/volume-04/ai-eng-k-weight-dynamics.md)
5. [AI-ENG-L — Model Serving Architecture](./docs/volume-04/ai-eng-l-model-serving-architecture.md)

### If you are responsible for reliability, safety, or governance

Start with:

1. [AI-ENG-S — Production Pathologies](./docs/volume-07/ai-eng-s-production-pathologies.md)
2. [AI-ENG-T — Boundary Defense](./docs/volume-07/ai-eng-t-boundary-defense.md)
3. [AI-ENG-Z — Strategic Telemetry](./docs/volume-09/ai-eng-z-strategic-telemetry.md)
4. [AI-ENG-AA — Evals Architecture](./docs/volume-09/ai-eng-aa-evals-architecture.md)
5. [AI-ENG-AC — AI Operations](./docs/volume-10/ai-eng-ac-ai-operations.md)
6. [AI-ENG-AD — Governance Architecture](./docs/volume-10/ai-eng-ad-governance-architecture.md)

### If you want the philosophical spine

Read:

1. [AI-ENG-AI — Contract Thinking](./docs/volume-12/ai-eng-ai-contract-thinking.md)
2. [AI-ENG-AJ — AI System Design Patterns](./docs/volume-12/ai-eng-aj-ai-system-design-patterns.md)
3. [AI-ENG-AK — The AI Engineering Mindset](./docs/volume-12/ai-eng-ak-ai-engineering-mindset.md)

---

## Repository Structure

```text
.
├── README.md
├── LICENSE.md
├── NOTICE.md
├── CONTRIBUTING.md
├── SUPPORT.md
├── SECURITY.md
├── scripts/
│   └── check-docs.ps1
├── CITATION.cff
├── knowledge-packs/
│   ├── by-volume/
│   ├── by-part/
│   └── omnibus/
└── docs/
    ├── index.md
    ├── canon-map.md
    ├── worked-example-refund-agent.md
    ├── knowledge-packs.md
    ├── how-to-use-this-canon.md
    ├── _config.yml
    ├── _layouts/
    │   └── default.html
    ├── assets/
    │   ├── brand/
    │   └── css/
    │       └── style.css
    ├── volume-01/
    ├── volume-02/
    ├── volume-03/
    ├── volume-04/
    ├── volume-05/
    ├── volume-06/
    ├── volume-07/
    ├── volume-08/
    ├── volume-09/
    ├── volume-10/
    ├── volume-11/
    └── volume-12/
```

The `/docs/` directory contains the canonical source reports and GitHub Pages site.

The `/knowledge-packs/` directory contains bundled upload formats for AI Projects, RAG systems, NotebookLM-style tools, and long-context workspaces.

---

## Evidence and Limitations

This canon was constructed through AI-assisted research and synthesis using GPT and Gemini Deep Research. That method supports broad synthesis; it does not make every statement correct, current, complete, or universally applicable.

Use the Guide as a working engineering reference and decision support—not as proof that a particular architecture, implementation, security control, legal interpretation, or operational choice is correct in your environment. For consequential decisions, verify applicable claims against current primary sources, executable behavior, and qualified domain review. If current evidence or observed behavior contradicts the canon, reality wins and the canon should be corrected.

The `public_canon` status means that all 37 planned reports and the documented pack formats are present in this repository. It is not a claim of independently verified factual accuracy, benchmarked model improvement, comparative reliability, deployment safety, or suitability for a particular environment.

The dependency-free [`scripts/check-docs.ps1`](./scripts/check-docs.ps1) gate checks local Markdown targets, the canonical report count, fenced JSON syntax and completeness, exact canonical report bodies in each expected knowledge pack, the expected CC BY 4.0 license text, citation-mirror consistency, shared published-brand-image custody, and obvious packaging debris. Those checks establish structural and packaging integrity only; they do not establish factual correctness or measured model performance.

Please [open a correction or source-quality issue](https://github.com/Stunspot/stunspots-guide-to-ai-systems/issues/new/choose) with the affected report, passage, and supporting evidence.

--stunspot | ⟨🤩⨯📍⟩ and 💠‍🌐Nova

## Citation, License, and Support

- Cite the current repository state using [`CITATION.cff`](./CITATION.cff). For a reproducible citation, use a commit permalink, record the full commit SHA and access date, and use the `CITATION.cff` stored in that revision. Versioned archives may carry different metadata and license terms.
- Current-main original material is licensed under [CC BY 4.0](./LICENSE.md); read the [copyright, attribution, and version notice](./NOTICE.md).
- See [How to Use This Canon](./docs/how-to-use-this-canon.md), [Contributing](./CONTRIBUTING.md), [Support](./SUPPORT.md), and [Security](./SECURITY.md) for the relevant task path.
