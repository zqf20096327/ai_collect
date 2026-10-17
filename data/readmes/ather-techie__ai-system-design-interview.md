# 🧠 AI System Design Interview Prep

> Design **production LLM systems** under interview pressure — gateways, caching, streaming, cost, evals, and the trade-offs senior interviewers actually probe. Not flashcards: real decision matrices, architecture diagrams, and "what the interviewer asks next."

[![Stars](https://img.shields.io/github/stars/ather-techie/ai-system-design-interview?style=social)](https://github.com/ather-techie/ai-system-design-interview)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**⭐ If this helps your prep, star it — it’s the fastest way to help other engineers find it.**

---

If you're preparing for an **AI / ML system design interview** — LLM system design, GenAI infrastructure, or an AI platform / ML infra role — this repo gives you the senior-level answers: how to *choose models, design LLM gateways, cache and route requests, control cost, stream responses, and build evals* the way production teams actually do. Every answer leads with the decision, backs it with a trade-off table or diagram, and ends with the follow-up the interviewer asks next.

---

## 📚 AI Interview Prep series

This repo is the **system-design hub**. Topic depth lives in dedicated companion repos — each focused so you can go deep without wading through everything else:

| Repo | Focus | Go here for |
|------|-------|-------------|
| **AI System Design Interview** *(you are here)* | LLM fundamentals + end-to-end system design | Model selection, gateways, caching, streaming, cost, evals, full design walkthroughs |
| [🔎 rag-interview-system](https://github.com/ather-techie/rag-interview-system) | Retrieval-Augmented Generation, in depth | 200+ RAG Q&As: chunking, vector DBs, hybrid search, rerankers, RAG evaluation |
| [🤖 ai-agents-design-patterns](https://github.com/ather-techie/ai-agents-design-patterns) | Agentic systems & patterns | ReAct/Plan-Execute, tool use, multi-agent orchestration, memory, guardrails |

> Preparing for a full AI system design round? Work through this repo, then go deep on RAG and Agents in the companion repos. ⭐ all three.

---

## 👋 Who This Is For

- Software engineers preparing for **Senior / Staff / Principal** AI roles
- Backend engineers moving into **ML platform or AI infrastructure** positions
- Candidates interviewing at FAANG, AI startups, FinTech, InsurTech, and SaaS companies
- Engineers who want to understand **production AI systems**, not just theory

---

## 🗂️ What's Inside

| Module | Topics | Questions |
|--------|--------|-----------|
| [LLM Fundamentals](./1-llm-fundamentals/) | Model selection, fine-tuning, prompting, serving, evals, context, multimodal, alignment, embeddings | 24 |
| [System Design Patterns](./2-system-design/) | Gateways, routing, caching, streaming, cost, scale, observability, guardrails, vector search, ingestion, capacity math, multi-region | 40 |
| [Case Studies](./3-case-studies/) | Full worked design walkthroughs (LLM gateway, code assistant, content moderation, semantic search…) | 5 |
| [Resources](./4-resources/) | Study plan, cheat sheets, mock interview template | — |
| 🔎 RAG | → [rag-interview-system](https://github.com/ather-techie/rag-interview-system) | 200+ |
| 🤖 AI Agents | → [ai-agents-design-patterns](https://github.com/ather-techie/ai-agents-design-patterns) | — |

---

## 🚀 Quick Start

**If you have 1 week:** Focus on [LLM Fundamentals](./1-llm-fundamentals/) + [System Design Patterns](./2-system-design/)

**If you have 2 weeks:** Add the [Case Studies](./3-case-studies/) and go deep on RAG via [rag-interview-system](https://github.com/ather-techie/rag-interview-system)

**If you have 1 month:** All modules + Agents via [ai-agents-design-patterns](https://github.com/ather-techie/ai-agents-design-patterns) + practice with the [mock interview template](./4-resources/mock-interview-template.md)

---

## 🗂️ Module Overview

### 🟡 LLM Fundamentals
Core knowledge every AI engineer needs.
- Model selection criteria (cost, latency, capability)
- Fine-tuning vs prompting vs RAG decision framework
- Prompt engineering patterns for production
- Serving & inference optimization (vLLM, batching, KV cache, quantization)
- Evaluation frameworks and benchmarks
- Token budgeting and context window management
- Multimodal model selection and alignment methods (RLHF/DPO)
- Embedding model selection for semantic search

### 🟠 System Design Patterns
How to design end-to-end AI systems at scale.
- LLM gateway and routing patterns
- Streaming architectures for real-time inference
- Caching strategies (semantic cache, prompt cache)
- Cost optimization at scale
- Multi-tenancy, rate limiting, and quota design
- Observability, tracing, and monitoring
- Scaling, failover, and graceful degradation
- Safety guardrails and CI/CD for prompts & evals
- Vector search infrastructure (index types, hybrid search, re-embedding migrations)
- Data ingestion pipelines, backfills, and freshness SLAs
- Capacity estimation, GPU math, and multi-region / disaster recovery

### 🟢 Case Studies
End-to-end worked walkthroughs you can practice against — clarify, design, deep-dive, trade-offs.

---

## 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) before submitting a PR.

- 💡 Found a gap? Open an [issue](https://github.com/ather-techie/ai-system-design-interview/issues)
- ✏️ Want to add questions? See the [question template](.github/ISSUE_TEMPLATE/question.md)
- ⭐ Found this useful? Star the repo — it helps others discover it

---

## Support

For issues, questions, or general feedback:

- Open an issue on [GitHub](https://github.com/ather-techie/ai-system-design-interview/issues)
- Join the [Discord community](https://discord.gg/FqEFjRT3Y)
- Contact: [ather.techie@gmail.com](mailto:ather.techie@gmail.com)

---

## 📄 License

MIT — free to use, share, and build upon with attribution.

---
