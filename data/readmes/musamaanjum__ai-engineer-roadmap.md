<div align="center">

# AI & LLM Engineer Roadmap

### From Software Engineer to AI Engineer -- The Complete Path

![License](https://img.shields.io/badge/license-MIT-green)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)
![Last Updated](https://img.shields.io/badge/updated-March_2026-blue)
![Stars](https://img.shields.io/github/stars/musamaanjum/ai-engineer-roadmap?style=social)

**A structured, no-fluff roadmap for software engineers who want to break into AI, LLM, and Generative AI roles.**

*Free and paid courses. Hands-on projects. Interview prep. Everything you need.*

---

**If you already know how to code and have basic ML knowledge,<br>
getting an AI/LLM engineering job is a piece of cake -- if you follow the right path.**<br>
This roadmap is that path.

</div>

---

## Why This Roadmap?

The AI job market in 2025-2026 is **exploding**. Companies are hiring **AI Engineers**, **LLM Engineers**, **ML Engineers**, and **Generative AI Engineers** at unprecedented rates. But most candidates fail because they:

- Waste months on theory without building anything
- Don't know the difference between what interviewers *actually ask* vs. what tutorials teach
- Skip production/deployment skills that separate junior from senior candidates

**This roadmap fixes all of that.** It is designed specifically for **software engineers who already know Python and basic ML** and want the fastest path to an AI/LLM role.

> **After completing this roadmap, landing an AI engineering job will be a piece of cake.** You will have the exact skills, projects, and interview preparation that top companies -- FAANG, top startups, and AI labs -- are looking for.

---

## Contents

- [Prerequisites](#prerequisites)
- [Curriculum](#curriculum)
  - [Phase 1: Transformer & LLM Foundations](#phase-1-transformer--llm-foundations-weeks-1-2)
  - [Phase 2: Core LLM Engineering](#phase-2-core-llm-engineering-weeks-3-5)
  - [Phase 3: Advanced & Production Skills](#phase-3-advanced--production-skills-weeks-6-8)
  - [Phase 4: Specialization & Differentiation](#phase-4-specialization--differentiation-ongoing)
- [Portfolio Projects](#portfolio-projects)
- [Interview Preparation](#interview-preparation)
  - [Concepts & Question Banks](#concepts--question-banks)
  - [Coding & System Design](#coding--system-design)
  - [Mock Interviews](#mock-interviews)
- [Books & Reading](#books--reading)
- [Stay Current](#stay-current)
- [Suggested Timeline](#suggested-timeline)
- [Community](#community)
- [Contributing](#contributing)

---

## Prerequisites

This roadmap assumes you already have:

- **Programming**: Intermediate-to-advanced Python skills
- **Software Engineering**: Experience building and deploying software
- **Machine Learning**: Completed at least one ML course (Andrew Ng's ML Specialization, fast.ai, or equivalent)
- **Math**: Comfortable with linear algebra, calculus, and probability at a college level

If you are missing any of the above, complete them first. This roadmap will still be here.

---

## Curriculum

### Phase 1: Transformer & LLM Foundations (Weeks 1-2)

> **Goal**: Deeply understand how Transformers and LLMs work under the hood. Every single AI interview starts here.

Topics covered:
`transformers` `self-attention` `positional encoding` `tokenization` `embeddings` `encoder-decoder architecture` `GPT` `BERT` `pretraining` `transfer learning`

| # | Course | Platform | Duration | Cost | Difficulty |
|:-:|--------|----------|----------|------|:----------:|
| 1 | [**Attention Is All You Need** (original paper)](https://arxiv.org/abs/1706.03762) | arXiv | 2-3 hrs | Free | Hard |
| 2 | [**The Illustrated Transformer**](https://jalammar.github.io/illustrated-transformer/) | Jay Alammar's Blog | 1 hr | Free | Medium |
| 3 | [**3Blue1Brown: Deep Learning Series (Chapters 5-6 on Transformers)**](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) | YouTube | 1 hr | Free | Easy |
| 4 | [**Neural Networks: Zero to Hero**](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) | YouTube (Andrej Karpathy) | 13 hrs | Free | Medium |
| 5 | [**Let's build GPT: from scratch, in code**](https://www.youtube.com/watch?v=kCc8FmEb1nY) | YouTube (Andrej Karpathy) | 2 hrs | Free | Medium |
| 6 | [**Let's reproduce GPT-2 (124M)**](https://www.youtube.com/watch?v=l8pRSuU81PU) | YouTube (Andrej Karpathy) | 4 hrs | Free | Hard |
| 7 | [**How Transformer LLMs Work**](https://www.deeplearning.ai/short-courses/how-transformer-llms-work/) | DeepLearning.AI | 1.5 hrs | Free | Easy |

<details>
<summary><b>What you'll be able to do after Phase 1</b></summary>

- Explain self-attention, multi-head attention, and positional encoding from scratch
- Whiteboard the full Transformer architecture in an interview
- Code a small GPT from scratch in PyTorch
- Understand tokenization (BPE, WordPiece, SentencePiece) and why it matters

</details>

---

### Phase 2: Core LLM Engineering (Weeks 3-5)

> **Goal**: Learn to build real applications with LLMs -- prompt engineering, RAG, chains, agents, and fine-tuning. This is where you go from "I understand the theory" to "I can build things."

Topics covered:
`prompt engineering` `RAG` `retrieval augmented generation` `vector databases` `embeddings` `LangChain` `LlamaIndex` `fine-tuning` `LoRA` `QLoRA` `PEFT` `RLHF` `agents` `tool use` `chains`

| # | Course | Platform | Duration | Cost | Difficulty |
|:-:|--------|----------|----------|------|:----------:|
| 8 | [**ChatGPT Prompt Engineering for Developers**](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) | DeepLearning.AI | 1.5 hrs | Free | Easy |
| 9 | [**LangChain for LLM Application Development**](https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/) | DeepLearning.AI | 1.5 hrs | Free | Medium |
| 10 | [**LangChain: Chat with Your Data**](https://learn.deeplearning.ai/courses/langchain-chat-with-your-data/) | DeepLearning.AI | 1.5 hrs | Free | Medium |
| 11 | [**Building Agentic RAG with LlamaIndex**](https://www.deeplearning.ai/short-courses/building-agentic-rag-with-llamaindex/) | DeepLearning.AI | 1 hr | Free | Medium |
| 12 | [**Finetuning Large Language Models**](https://www.deeplearning.ai/short-courses/finetuning-large-language-models/) | DeepLearning.AI | 1.5 hrs | Free | Medium |
| 13 | [**Pretraining LLMs**](https://www.deeplearning.ai/short-courses/pretraining-llms/) | DeepLearning.AI | 1.5 hrs | Free | Medium |
| 14 | [**LLMOps: Building Real-World Applications With LLMs**](https://www.udacity.com/course/building-real-world-applications-with-large-language-models--cd13455) | Udacity | 11 hrs | Free | Medium |
| 15 | [**Hugging Face NLP Course**](https://huggingface.co/learn/nlp-course/) | Hugging Face | 15+ hrs | Free | Medium |

<details>
<summary><b>What you'll be able to do after Phase 2</b></summary>

- Build a full RAG pipeline with vector databases, document loaders, and retrieval optimization
- Fine-tune open-source models using LoRA/QLoRA/PEFT
- Create LLM-powered agents that use tools (search, code execution, APIs)
- Evaluate LLM outputs systematically (not just "vibes")
- Use LangChain, LlamaIndex, and Hugging Face Transformers fluently

</details>

---

### Phase 3: Advanced & Production Skills (Weeks 6-8)

> **Goal**: Go from prototype to production. This is what separates the candidates who get offers from the ones who don't.

Topics covered:
`LLMOps` `model serving` `inference optimization` `quantization` `guardrails` `evaluation` `monitoring` `cost optimization` `CI/CD for ML` `deployment` `Docker` `Kubernetes` `API design`

| # | Course | Platform | Duration | Cost | Difficulty |
|:-:|--------|----------|----------|------|:----------:|
| 16 | [**Master LLMs and RAG**](https://www.udacity.com/course/large-language-models-llms-and-retrieval-augmented-generation-rag--cd13318) | Udacity | 17 hrs | Paid (~$249/mo) | Advanced |
| 17 | [**Agentic AI** (Andrew Ng)](https://learn.deeplearning.ai/courses/agentic-ai/information) | DeepLearning.AI | 6 hrs | Free | Advanced |
| 18 | [**Generative AI for Software Development**](https://www.coursera.org/professional-certificates/generative-ai-for-software-development) | Coursera (DeepLearning.AI) | 20 hrs | Free to audit | Medium |
| 19 | [**Machine Learning Engineering for Production (MLOps)**](https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops) | Coursera (DeepLearning.AI) | 40+ hrs | Free to audit | Advanced |
| 20 | [**Full Stack LLM Bootcamp**](https://fullstackdeeplearning.com/llm-bootcamp/spring-2023/) | FSDL | 10+ hrs | Free (recordings) | Advanced |

<details>
<summary><b>What you'll be able to do after Phase 3</b></summary>

- Deploy LLM applications with proper monitoring, logging, and guardrails
- Design ML system architectures (this is THE interview question for senior roles)
- Optimize inference cost and latency (quantization, caching, batching)
- Build CI/CD pipelines for ML model training and deployment
- Articulate production trade-offs: cost vs. quality, latency vs. accuracy, sync vs. async

</details>

---

### Phase 4: Specialization & Differentiation (Ongoing)

> **Goal**: Go deep in an area that makes you stand out. Pick 1-2 based on the roles you are targeting.

Topics covered:
`multimodal AI` `vision-language models` `speech AI` `AI safety` `alignment` `RLHF` `DPO` `scaling laws` `distributed training` `model distillation`

| # | Course | Platform | Duration | Cost | Difficulty |
|:-:|--------|----------|----------|------|:----------:|
| 21 | [**Stanford CS324: Large Language Models**](https://stanford-cs324.github.io/winter2022/) | Stanford Online | Self-paced | Free | Expert |
| 22 | [**Introducing Multimodal Llama 3.2**](https://www.deeplearning.ai/short-courses/introducing-multimodal-llama-3-2/) | DeepLearning.AI | 1.5 hrs | Free | Medium |
| 23 | [**Building with Llama 4**](https://www.deeplearning.ai/short-courses/building-with-llama-4/) | DeepLearning.AI | 1 hr | Free | Medium |
| 24 | [**Prompt Engineering Bootcamp**](https://zerotomastery.io/courses/prompt-engineering-bootcamp/) | Zero to Mastery | 24 days | Paid (~$39/mo) | Medium |

---

## Portfolio Projects

> **Projects are the single most important thing on your resume.** Certificates alone mean nothing. Build these, put them on GitHub, deploy at least two with a live demo, and you will stand out from 90% of applicants.

### Project 1: RAG-Powered Document Q&A System

| | |
|---|---|
| **Difficulty** | Intermediate |
| **Time** | 1-2 weeks |
| **Stack** | LangChain or LlamaIndex, ChromaDB or Weaviate, OpenAI or open-source embeddings, FastAPI, Streamlit/Gradio |

**What to build**: An end-to-end system that lets users ask natural language questions over a custom document corpus (research papers, company docs, legal contracts).

**What to showcase**:
- Multiple chunking strategies and their impact on retrieval quality
- Hybrid search (BM25 + dense vector retrieval)
- Evaluation with [RAGAS](https://docs.ragas.io/) -- precision, recall, faithfulness scores
- Source citation in every answer
- Clean API with FastAPI + interactive UI

**Why it matters**: RAG is the #1 pattern companies are deploying in production right now. This project alone can carry an interview.

---

### Project 2: Fine-Tuned Domain-Specific Model

| | |
|---|---|
| **Difficulty** | Intermediate-Advanced |
| **Time** | 1-2 weeks |
| **Stack** | Hugging Face Transformers + PEFT + TRL, Weights & Biases, Llama 3 / Mistral / Phi |

**What to build**: Fine-tune an open-source LLM on a domain-specific dataset (medical, legal, financial, code) using QLoRA. Compare base model vs. fine-tuned model on domain benchmarks.

**What to showcase**:
- Data curation and preprocessing pipeline
- Training with LoRA/QLoRA, hyperparameter sweeps tracked in W&B
- Before/after evaluation with quantitative metrics
- Model quantization (GPTQ, AWQ) for efficient deployment
- Hosted on Hugging Face Hub with a model card

**Why it matters**: Demonstrates you can go beyond API calls and actually train models.

---

### Project 3: Multi-Agent AI System

| | |
|---|---|
| **Difficulty** | Advanced |
| **Time** | 2-3 weeks |
| **Stack** | LangGraph or CrewAI or AutoGen, tool integrations (web search, code execution, databases) |

**What to build**: A system where multiple LLM agents collaborate -- e.g., a research agent searches the web, a writer agent drafts content, a critic agent reviews and iterates.

**What to showcase**:
- Agent orchestration with state management and handoffs
- Tool use (web search, code interpreter, database queries, API calls)
- Error recovery and retry logic
- Observable traces (LangSmith / Langfuse)
- Real-world use case with measurable output quality

**Why it matters**: Agentic AI is the hottest area in 2026 hiring. Multi-agent systems are what companies are building *right now*.

---

### Project 4: LLM Evaluation & Benchmarking Framework

| | |
|---|---|
| **Difficulty** | Intermediate |
| **Time** | 1 week |
| **Stack** | Python, multiple model APIs, custom eval harness, visualization (Plotly/Streamlit) |

**What to build**: A systematic evaluation pipeline that benchmarks LLM outputs across accuracy, hallucination rate, toxicity, latency, and cost.

**What to showcase**:
- Automated test suites for LLM outputs
- Regression detection across model versions
- Cost/quality/latency tradeoff dashboards
- Support for multiple providers (OpenAI, Anthropic, open-source)

**Why it matters**: Companies desperately need people who can *measure* LLM quality, not just build demos. This is a rare and highly valued skill.

---

### Project 5: Production-Grade AI Application

| | |
|---|---|
| **Difficulty** | Advanced |
| **Time** | 2-3 weeks |
| **Stack** | FastAPI or Next.js, Redis, LangSmith/Langfuse, Docker, AWS/GCP/Vercel |

**What to build**: A fully deployed chatbot or AI copilot with authentication, rate limiting, streaming responses, response caching, guardrails, and observability.

**What to showcase**:
- Production concerns: auth, rate limiting, input validation, output guardrails
- Streaming SSE/WebSocket responses
- Caching layer (Redis) for cost reduction
- Full observability (traces, metrics, logs)
- CI/CD pipeline with automated tests
- Live deployed URL with uptime

**Why it matters**: This bridges the gap from "I completed a tutorial" to "I can ship production software." It is the most convincing project you can have.

---

### Project Tips

- **Every project** must have a polished README with architecture diagram, setup instructions, and results
- **Include quantitative metrics**: latency (p50/p95/p99), accuracy scores, cost per query, throughput
- **Deploy at least 2 projects** with a live URL or recorded demo video
- **Write a blog post** about at least one project -- this dramatically boosts your visibility

---

## Interview Preparation

### Concepts & Question Banks

> **These resources cover the exact questions you will be asked in AI/LLM engineering interviews.**

| Resource | Focus | Cost |
|----------|-------|------|
| [**Chip Huyen's ML Interviews Book**](https://huyenchip.com/ml-interviews-book/) | 200+ ML interview questions, difficulty-rated, with solutions. The gold standard. | Free |
| [**LLM Interview Questions -- Complete Guide (LockedIn AI)**](https://www.lockedinai.com/blog/llm-interview-questions-answers-complete-guide-engineers) | Transformers, RAG, fine-tuning, system design -- LLM-specific focus | Free |
| [**Top 20 LLM Interview Questions (Analytics Vidhya)**](https://www.analyticsvidhya.com/blog/2026/01/llm-interview-questions-and-answers/) | Practical answers with clear explanations, updated 2026 | Free |
| [**13 Common LLM Interview Questions (Coursera)**](https://www.coursera.org/articles/large-language-models-interview-questions) | Structured prep with "how to prepare" guidance | Free |

### Coding & System Design

| Resource | Focus | Cost |
|----------|-------|------|
| [**LeetCode**](https://leetcode.com/) | DSA fundamentals -- still required even at AI companies | Free / $35/mo |
| [**Neetcode.io**](https://neetcode.io/) | Curated DSA roadmap with video explanations, 150 essential problems | Free / $99/yr |
| [**Grokking the Machine Learning Interview (Educative)**](https://www.educative.io/courses/grokking-the-machine-learning-interview) | ML system design: ranking, recommendation, search, ads, LLM serving | ~$59/mo |
| [**ByteByteGo**](https://bytebytego.com/) | General system design (API design, distributed systems, databases) | $79/yr |

### Mock Interviews

| Resource | Focus | Cost |
|----------|-------|------|
| [**Interviewing.io**](https://interviewing.io/) | Anonymous mock interviews with FAANG engineers | Free practice |
| [**Pramp**](https://www.pramp.com/) | Free peer-to-peer mock interviews | Free |
| [**LockedIn AI**](https://www.lockedinai.com/) | AI-powered mock interviews with real-time coaching | Free tier |
| [**Exponent**](https://www.tryexponent.com/) | ML system design mocks, curated question bank | ~$99/3 months |

---

## Books & Reading

| Book | Author | Why |
|------|--------|-----|
| [**Designing Machine Learning Systems**](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/) | Chip Huyen | Amazon #1 bestseller in AI. Covers the full ML system lifecycle. Must-read for system design interviews. |
| [**Attention Is All You Need**](https://arxiv.org/abs/1706.03762) | Vaswani et al. | The paper that started it all. Read it, understand it, be able to explain it. |
| [**The Illustrated Transformer**](https://jalammar.github.io/illustrated-transformer/) | Jay Alammar | The single best visual explanation of how Transformers work. Referenced by Stanford, MIT, Harvard. |

---

## Stay Current

The AI field moves at breakneck speed. **You must stay updated** or your knowledge becomes stale in months.

| Resource | Format | Why |
|----------|--------|-----|
| [**The Batch**](https://www.deeplearning.ai/the-batch/) | Newsletter | Andrew Ng's weekly AI news digest. 5-minute read, high signal. |
| [**Latent Space Podcast**](https://www.latent.space/) | Podcast | Deep dives into AI engineering with top practitioners. The #1 AI engineering podcast. |
| [**Simon Willison's Blog**](https://simonwillison.net/) | Blog | Practical, hands-on LLM engineering insights from a veteran developer. |
| [**Hugging Face Blog**](https://huggingface.co/blog) | Blog | Latest models, benchmarks, releases, and research from the open-source AI hub. |
| [**Papers with Code**](https://paperswithcode.com/) | Website | Every ML paper with linked code and benchmarks. |
| [**r/LocalLLaMA**](https://www.reddit.com/r/LocalLLaMA/) | Reddit | Best community for open-source LLM news, quantization, and local deployment. |
| [**r/MachineLearning**](https://www.reddit.com/r/MachineLearning/) | Reddit | Academic ML discussion, paper reviews, industry trends. |

---

## Suggested Timeline

> **Estimated total: 8-10 weeks of focused work (20-30 hrs/week).** Adjust based on your pace.

| Week | Focus | Deliverables |
|------|-------|-------------|
| **1-2** | [Phase 1: Foundations](#phase-1-transformer--llm-foundations-weeks-1-2) | Can explain Transformers from scratch, coded a mini-GPT |
| **3-5** | [Phase 2: Core LLM Engineering](#phase-2-core-llm-engineering-weeks-3-5) | Completed all short courses, comfortable with LangChain + RAG + fine-tuning |
| **5-7** | [Projects 1 & 2](#project-1-rag-powered-document-qa-system) | RAG system deployed, fine-tuned model on HF Hub |
| **7-9** | [Project 3 or 5](#project-3-multi-agent-ai-system) + [Interview Prep](#interview-preparation) | Agents project or production app live, grinding interview questions |
| **9-10** | Polish & Apply | GitHub cleaned up, 2+ projects deployed, mock interviews done, **start applying** |
| **Ongoing** | [Phase 3-4](#phase-3-advanced--production-skills-weeks-6-8) + [Stay Current](#stay-current) | Depth building while interviewing, newsletter + podcast habit |

---

## The Bottom Line

> **The AI engineering job market in 2026 favors builders, not certificate collectors.**
>
> If you follow this roadmap -- complete the courses, build the projects, and prepare for interviews -- **you will have every skill that top companies are hiring for**. The demand for AI engineers far exceeds the supply of qualified candidates. The path is clear. The resources are (mostly) free. The only variable is your effort.
>
> **Getting an AI engineering job after completing this roadmap will be a piece of cake.**

---

## Community

- Found this useful? **Star this repo** -- it helps others find it.
- Have a suggestion? **Open an issue** or **submit a PR**.
- Want to discuss? Start a conversation in the **Discussions** tab.

---

## Contributing

Contributions are welcome! If you find a broken link, want to add a course, or have project ideas:

1. Fork this repository
2. Create your feature branch (`git checkout -b add-new-course`)
3. Commit your changes (`git commit -m 'Add amazing course'`)
4. Push to the branch (`git push origin add-new-course`)
5. Open a Pull Request

Please ensure all course links are verified and working before submitting.

---

## License

This project is licensed under the MIT License -- see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**If this roadmap helped you, give it a star and share it with someone who needs it.**

Made with determination by software engineers, for software engineers.

Keywords: `AI engineer roadmap` `LLM engineer` `how to become an AI engineer` `AI career path` `LLM courses` `generative AI courses` `machine learning engineer` `AI interview preparation` `RAG tutorial` `fine-tuning LLM` `LangChain course` `AI portfolio projects` `AI job 2026` `software engineer to AI engineer` `LLM interview questions` `AI engineer salary` `best AI courses` `free AI courses` `ChatGPT developer` `prompt engineering course` `transformer tutorial` `hugging face course` `MLOps` `AI agent` `agentic AI` `deeplearning.ai courses` `Andrej Karpathy` `Andrew Ng`

</div>
