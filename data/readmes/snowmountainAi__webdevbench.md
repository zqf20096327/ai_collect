# SWE-WebDev-Bench

## From Vibe Coding to Production: Evaluating AI App-Building Platforms as Virtual Software Agencies

- [Arxiv](https://arxiv.org/abs/2605.04637)
- [Website](https://webdevbench.com)
- [Github](https://github.com/snowmountainAi/webdevbench)

SWE-WebDev-Bench is a benchmark designed to evaluate vibe coding platforms - systems that generate full-stack applications from natural language - not just as code generators, but as end-to-end software agencies.

Unlike traditional benchmarks that focus on code correctness, SWE-WebDev-Bench evaluates whether platforms can:

- understand ambiguous business requirements,
- make sound product and architectural decisions,
- generate production-ready systems,
- handle iterative modifications,
- and meet real-world standards for security, scalability, and reliability.

## 🚀 Why This Benchmark Exists

Current evaluation frameworks (e.g., SWE-bench, HumanEval) focus on:

- function-level code generation
- patching existing repositories
- developer-centric workflows

But vibe coding platforms claim something fundamentally different:

> "Describe your idea -> get a working product."

This benchmark evaluates whether that promise holds.

## 🧠 What Makes SWE-WebDev-Bench Different

### 1. Full Software Agency Evaluation

We evaluate across three roles:

- PM (Product Manager) -> requirement understanding, ambiguity handling
- Engineering -> code quality, architecture, integrations
- Ops -> deployment, performance, reliability

### 2. Evaluation Across 3 Dimensions

| Dimension | Description |
| --- | --- |
| Interaction Mode | App Creation (ACR) vs App Modification (AMR) |
| Agency Angle | PM x Engineering x Ops |
| Complexity Tier | T4 (SaaS) vs T5 (AI-native apps) |

### 3. 68-Metric Evaluation Framework

- 25 Primary Metrics (what was built)
- 43 Diagnostic Metrics (why it worked or failed)

Grouped into:

| Group | Focus |
| --- | --- |
| G1 | Specification Fidelity |
| G2 | Code Quality |
| G3 | Integrations |
| G4 | Security & Scale |
| G5 | Changeability |
| G6 | Business Readiness |
| G7 | Production Readiness |

### 4. Canary Requirement Methodology 🐤

We introduce 80 embedded "canary requirements" to test real understanding.

These are:

- culturally specific (e.g., INR, DD/MM/YYYY),
- domain-embedded,
- easy to verify manually,
- hard to pass via template generation.

They help distinguish:

- real reasoning vs pattern-matching.

### 5. ACR vs AMR (First of Its Kind)

We separately evaluate:

- ACR (App Creation Requests) -> build from scratch
- AMR (App Modification Requests) -> modify existing apps

Why it matters:

Most real-world usage is iterative - and modification is significantly harder.

## 📊 Key Findings (Initial Study)

Across 6 platforms and 3 domains:

- ❌ No platform exceeds 60% engineering score
- ⚠️ Massive variance in requirement understanding (5.5x spread)
- 🎨 Frontend is mostly solved - backend is not
- 🔐 Security is consistently weak across all platforms
- 🧩 Iterative modification introduces regressions and context loss
