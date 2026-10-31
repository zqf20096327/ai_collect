<p align="center">
    <img alt="Forward Deployed Engineer Roadmap" src="https://github.com/amitshekhariitbhu/forward-deployed-engineer-roadmap/blob/main/assets/banner.png">
</p>

# Forward Deployed Engineer Roadmap

> Forward Deployed Engineer Roadmap - A step-by-step roadmap to become a Forward Deployed Engineer (FDE) in AI, with a blog for every topic

## Table of Contents

- [Who is a Forward Deployed Engineer?](#who-is-a-forward-deployed-engineer)
- [The FDE Engagement Lifecycle](#the-fde-engagement-lifecycle)
- [How to Use This Roadmap](#how-to-use-this-roadmap)
- [Step 0: Must Know](#step-0-must-know)
- [Step 1: AI and Machine Learning Essentials](#step-1-ai-and-machine-learning-essentials)
- [Step 2: How LLMs Work](#step-2-how-llms-work)
- [Step 3: Choosing the Right Model for the Customer](#step-3-choosing-the-right-model-for-the-customer)
- [Step 4: Prompt Engineering and Context Engineering](#step-4-prompt-engineering-and-context-engineering)
- [Step 5: RAG on Customer Data](#step-5-rag-on-customer-data)
- [Step 6: AI Agents and Tool Integration](#step-6-ai-agents-and-tool-integration)
- [Step 7: Agentic Engineering and Building Fast with Coding Agents](#step-7-agentic-engineering-and-building-fast-with-coding-agents)
- [Step 8: Evaluation and Observability: Proving Value to the Customer](#step-8-evaluation-and-observability-proving-value-to-the-customer)
- [Step 9: AI Safety, Security, and Trust](#step-9-ai-safety-security-and-trust)
- [Step 10: Latency and Cost in Production](#step-10-latency-and-cost-in-production)
- [Step 11: Fine-Tuning and Customizing Models](#step-11-fine-tuning-and-customizing-models)
- [Step 12: AI System Design and Infrastructure](#step-12-ai-system-design-and-infrastructure)
- [Step 13: Customer Use Case: Real-Time Voice AI Agent](#step-13-customer-use-case-real-time-voice-ai-agent)
- [Step 14: Prepare for Forward Deployed Engineer Interviews](#step-14-prepare-for-forward-deployed-engineer-interviews)

### Prepared and maintained by the **Founder** of [Outcome School](https://outcomeschool.com): Amit Shekhar

### Follow Amit Shekhar

- [X/Twitter](https://twitter.com/amitiitbhu)
- [LinkedIn](https://www.linkedin.com/in/amit-shekhar-iitbhu)
- [GitHub](https://github.com/amitshekhariitbhu)

### Follow Outcome School

- [YouTube](https://youtube.com/@OutcomeSchool)
- [X/Twitter](https://x.com/outcome_school)
- [LinkedIn](https://www.linkedin.com/company/outcomeschool)
- [GitHub](https://github.com/OutcomeSchool)

## I teach at Outcome School

- [AI and Machine Learning](https://outcomeschool.com/program/ai-and-machine-learning)

---

> **Note: We will keep updating this roadmap with new topics and blogs.**

---

### Who is a Forward Deployed Engineer?

A Forward Deployed Engineer (FDE) is a software engineer who works directly with the customer to take an AI product from a demo to a working system in production, inside the customer's real systems, data, and workflows.

An AI Engineer mostly builds the product. An FDE makes the product work for one specific customer, and then brings what they learned back to the product team.

In simple words, an FDE is:

- **An engineer:** writes production code, builds RAG pipelines and agents, integrates APIs, and ships.
- **A problem finder:** sits with the customer, understands the actual business problem, and turns a vague ask into a clear definition of done.
- **A trust builder:** proves with evals and numbers that the system works, keeps it safe and secure, and explains trade-offs to both engineers and business leaders.

This is why an FDE needs breadth more than depth. We must know enough about LLMs, RAG, agents, evaluation, inference, security, and system design to make the right call quickly, in front of the customer.

### The FDE Engagement Lifecycle

Almost every FDE engagement follows the same path. This roadmap is ordered to match it.

| Phase | What the FDE does | Steps in this roadmap |
| --- | --- | --- |
| Discover | Understand the customer problem, define what success looks like | Step 0 |
| Learn the toolbox | Know what AI can and cannot do, and why | Step 1, Step 2, Step 3 |
| Prototype | Build a working demo on the customer's data in days, not months | Step 4, Step 5, Step 6, Step 7 |
| Prove value | Measure quality with evals, show the numbers | Step 8 |
| Harden | Make it safe, secure, fast, and affordable | Step 9, Step 10, Step 11 |
| Deploy | Design the full system and choose where it runs | Step 12 |
| Ship a real use case | See every idea come together in one production system | Step 13 |

### How to Use This Roadmap

This roadmap is designed so that anyone can follow it in the given order, even without any prior background in AI.

- Follow the steps in order. Each step builds on top of the previous one.
- Inside each step, read the blogs in the given order. Every blog explains one concept in simple words with examples.
- Wherever we have a video for the same topic, it is listed right below the blog. Read the blog, then watch the video, or the other way around.
- After every step, ask yourself: "If a customer asked me about this tomorrow, could I explain it and make a decision?" If yes, move on.
- Every blog is free to read and is written for beginners. No jargon. No assumptions.

Let's get started.

### Step 0: Must Know

Before jumping into the details, we must know the six words that come up in every AI Engineering conversation:

- LLM
- RAG
- MCP
- Agent
- Fine-tuning
- Quantization

Learn about all six in one video: [AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization](https://www.youtube.com/watch?v=lnfWvX66FUk)

As an FDE, these six words will come up in our very first customer meeting. Customers will ask: "Should we use RAG or fine-tuning?", "Can an agent do this for us?", "Can we run the model on our own servers?". Now, we know the big picture. In the next steps, we will learn each of these in depth, one concept at a time, so that we can answer these questions with confidence.

### Step 1: AI and Machine Learning Essentials

In this step, we will learn the Machine Learning basics that every FDE must know to talk to data teams, understand customer data, and measure whether a model is good or bad. We will keep it practical and focused.

- [What is Machine Learning?](https://outcomeschool.com/blog/machine-learning)
- [Supervised vs Unsupervised Learning](https://outcomeschool.com/blog/supervised-vs-unsupervised-learning)
- [What is Feature Engineering in Machine Learning?](https://outcomeschool.com/blog/feature-engineering)
- [Feature Engineering in Machine Learning](https://www.youtube.com/watch?v=QLlywrWuXag) (Video)
- [What is One-hot Encoding in Machine Learning?](https://outcomeschool.com/blog/one-hot-encoding)
- [One-hot Encoding in Machine Learning](https://www.youtube.com/watch?v=6AmedU5i9go) (Video)
- [Why do we split data into train, validation, and test sets?](https://outcomeschool.com/blog/train-validation-test-split)
- [Epoch, Batch, Batch Size, Iteration](https://www.youtube.com/watch?v=NFLlXE-6vno) (Video)
- [Precision vs Recall](https://outcomeschool.com/blog/precision-vs-recall)
- [What is a Neural Network and How Does It Work?](https://outcomeschool.com/blog/neural-network)
- [What are Activation Functions in Neural Networks? Sigmoid, Tanh, ReLU, and Softmax Explained](https://outcomeschool.com/blog/activation-functions)
- [What is the Softmax Function and How Does It Work?](https://outcomeschool.com/blog/softmax-function)
- [Softmax Activation Function in Machine Learning](https://www.youtube.com/watch?v=2Zx6x01WwWM) (Video)
- [What are Logits in Machine Learning?](https://outcomeschool.com/blog/logits-in-machine-learning)
- [How Does Gradient Descent Work?](https://outcomeschool.com/blog/math-behind-gradient-descent)
- [What is Reinforcement Learning?](https://outcomeschool.com/blog/reinforcement-learning)

### Step 2: How LLMs Work

In this step, we will learn how an LLM works from the inside, how it generates text, and where it fails. An FDE must be able to explain to a customer why the model hallucinated, why it forgot something in a long document, and why responses take time.

- [What is Generative AI?](https://outcomeschool.com/blog/what-is-generative-ai)
- [How does an LLM work?](https://outcomeschool.com/blog/large-language-model-llm)
- [What are Autoregressive Models?](https://outcomeschool.com/blog/autoregressive-models)
- [Tokenization in LLMs](https://outcomeschool.com/blog/tokenization-in-llms)
- [Tokenization in Large Language Models (LLMs)](https://www.youtube.com/watch?v=sK2s9I84EVI) (Video)
- [What is Byte Pair Encoding (BPE) in LLMs?](https://outcomeschool.com/blog/bpe-in-llms)
- [What are Embeddings?](https://outcomeschool.com/blog/what-are-embeddings)
- [Embeddings in Machine Learning](https://www.youtube.com/watch?v=LedXW6xl21s) (Video)
- [How does Cosine Similarity work?](https://outcomeschool.com/blog/cosine-similarity)
- [How Does the Transformer Architecture Work?](https://outcomeschool.com/blog/decoding-transformer-architecture)
- [What is Self Attention in Transformers?](https://outcomeschool.com/blog/self-attention-in-transformers)
- [Evolution of LLM Architecture](https://outcomeschool.com/blog/evolution-of-llm-architecture)
- [How does Temperature control LLM output?](https://outcomeschool.com/blog/how-does-temperature-control-llm-output)
- [How do Top-k and Top-p Sampling work?](https://outcomeschool.com/blog/how-do-top-k-and-top-p-sampling-work)
- [Stop Tokens in LLMs](https://outcomeschool.com/blog/stop-tokens-in-llms)
- [How does Token Streaming work?](https://outcomeschool.com/blog/how-does-token-streaming-work)
- [Why is the context window limited in LLMs?](https://www.youtube.com/watch?v=CGIhxIaOg3M) (Video)
- [What is the Lost in the Middle Problem in LLMs?](https://outcomeschool.com/blog/lost-in-the-middle-problem-in-llms)
- [Why Do LLMs Hallucinate? The Token-Level Explanation](https://outcomeschool.com/blog/why-do-llms-hallucinate-the-token-level-explanation)

### Step 3: Choosing the Right Model for the Customer

In this step, we will learn that there is no single best model. The right choice depends on the customer's task, budget, latency needs, and where their data is allowed to go. We will learn the types of models and how to pick between them.

- [What are Small Language Models (SLMs)?](https://outcomeschool.com/blog/small-language-models-slms)
- [What are Large Reasoning Models (LRMs)?](https://outcomeschool.com/blog/large-reasoning-models)
- [What is Mixture of Experts (MoE)?](https://outcomeschool.com/blog/mixture-of-experts)
- [What is Multimodal AI?](https://outcomeschool.com/blog/multimodal-ai)
- [How does a Vision-Language Model (VLM) work?](https://outcomeschool.com/blog/vision-language-model-vlm)
- [What is LLM Routing? How to Send Each Query to the Right LLM](https://outcomeschool.com/blog/llm-routing)

### Step 4: Prompt Engineering and Context Engineering

In this step, we will learn the fastest and cheapest way to improve results for a customer: giving the model better instructions and better context. In most FDE engagements, this is where the first big win comes from.

- [How does Chain-of-Thought (CoT) Prompting work?](https://outcomeschool.com/blog/how-does-chain-of-thought-prompting-work)
- [How does Prompt Chaining work?](https://outcomeschool.com/blog/how-does-prompt-chaining-work)
- [How does Tree of Thoughts work?](https://outcomeschool.com/blog/how-does-tree-of-thoughts-work)
- [What is Context Engineering?](https://outcomeschool.com/blog/context-engineering)
- [How does Context Compaction work?](https://outcomeschool.com/blog/how-does-context-compaction-work)
- [How does Prompt Caching work?](https://outcomeschool.com/blog/how-does-prompt-caching-work)

### Step 5: RAG on Customer Data

In this step, we will learn how to make an LLM answer questions from the customer's own documents, tickets, wikis, and databases. RAG is the most common thing an FDE builds, so we will go from the basics of vector search all the way to advanced retrieval.

If you want a quick introduction to RAG before starting, watch: [AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization](https://www.youtube.com/watch?v=lnfWvX66FUk)

- [How does a Vector Database work?](https://outcomeschool.com/blog/how-does-a-vector-database-work)
- [How does Approximate Nearest Neighbor (ANN) Search work?](https://outcomeschool.com/blog/how-does-approximate-nearest-neighbor-ann-search-work)
- [How does Semantic Search work?](https://outcomeschool.com/blog/how-does-semantic-search-work)
- [How does Hybrid Search work?](https://outcomeschool.com/blog/how-does-hybrid-search-work)
- [How does a Reranker work?](https://outcomeschool.com/blog/how-does-a-reranker-work)
- [How to Chunk Documents for RAG? Chunking Strategies Explained](https://outcomeschool.com/blog/chunking-strategies-for-rag)
- [How does Contextual Retrieval work?](https://outcomeschool.com/blog/how-does-contextual-retrieval-work)
- [How does HyDE work in RAG?](https://outcomeschool.com/blog/how-does-hyde-work)
- [How do Query Rewriting and Multi-Query Retrieval work?](https://outcomeschool.com/blog/how-do-query-rewriting-and-multi-query-retrieval-work)
- [What is ColBERT? Late Interaction Retrieval Explained](https://outcomeschool.com/blog/decoding-colbert)
- [How do Image Embeddings work?](https://outcomeschool.com/blog/how-do-image-embeddings-work)
- [How does an Embedding Cache work?](https://outcomeschool.com/blog/how-does-an-embedding-cache-work)
- [How does Semantic Caching work?](https://outcomeschool.com/blog/how-does-semantic-caching-work)
- [What is Agentic RAG?](https://outcomeschool.com/blog/agentic-rag)
- [Agentic RAG Explained](https://www.youtube.com/watch?v=6nSegpuWJVw) (Video)
- [What is GraphRAG? How Knowledge Graphs Improve RAG](https://outcomeschool.com/blog/graphrag)
- [What is Vectorless RAG? RAG Without Embeddings or a Vector Database](https://outcomeschool.com/blog/vectorless-rag)

### Step 6: AI Agents and Tool Integration

In this step, we will learn how an LLM goes from answering questions to actually doing work inside the customer's systems: calling their APIs, reading their tools, and completing multi-step tasks. We will start with a single agent and move to systems where many agents work together.

- [What is an AI Agent? How It Works](https://outcomeschool.com/blog/ai-agent)
- [How does Function Calling work in LLMs?](https://outcomeschool.com/blog/how-does-function-calling-work-in-llms)
- [What is an AI Agent Loop?](https://outcomeschool.com/blog/ai-agent-loop)
- [What is a ReAct Agent?](https://outcomeschool.com/blog/react-agent)
- [What is a Plan-and-Execute Agent?](https://outcomeschool.com/blog/plan-and-execute-agent)
- [What is a Reflection Agent?](https://outcomeschool.com/blog/reflection-agent)
- [How does AI Agent Memory work?](https://outcomeschool.com/blog/ai-agent-memory)
- [How does ChatGPT remember you?](https://outcomeschool.com/blog/how-does-chatgpt-remember-you)
- [What is MCP (Model Context Protocol)?](https://outcomeschool.com/blog/what-is-mcp-model-context-protocol)
- [What are Agent Skills?](https://outcomeschool.com/blog/what-are-agent-skills)
- [What is OKF (Open Knowledge Format)?](https://outcomeschool.com/blog/what-is-okf-open-knowledge-format)
- [What are Multi-Agent Systems?](https://outcomeschool.com/blog/multi-agent-systems)
- [What are AI SubAgents?](https://outcomeschool.com/blog/ai-subagents)
- [How AI Agents Communicate](https://outcomeschool.com/blog/how-ai-agents-communicate)
- [What is AI Orchestration?](https://outcomeschool.com/blog/ai-orchestration)
- [How do Computer-Use Agents work?](https://outcomeschool.com/blog/how-do-computer-use-agents-work)
- [How do Browser Agents work?](https://outcomeschool.com/blog/how-do-browser-agents-work)

### Step 7: Agentic Engineering and Building Fast with Coding Agents

In this step, we will learn the engineering practices for building reliable agents, the frameworks we will meet at customer sites, and how coding agents work. FDEs are expected to ship a working prototype in days, and coding agents are a big part of how that happens.

- [What is Harness Engineering?](https://outcomeschool.com/blog/harness-engineering-in-ai)
- [What is Loop Engineering?](https://outcomeschool.com/blog/what-is-loop-engineering)
- [What is Graph Engineering?](https://outcomeschool.com/blog/what-is-graph-engineering)
- [How does LangChain work?](https://outcomeschool.com/blog/how-does-langchain-work)
- [How does LangGraph work?](https://outcomeschool.com/blog/how-does-langgraph-work)
- [How does Claude Code work?](https://outcomeschool.com/blog/how-does-claude-code-work)
- [How does Cursor work?](https://outcomeschool.com/blog/how-does-cursor-work)

### Step 8: Evaluation and Observability: Proving Value to the Customer

In this step, we will learn how to measure whether our system is actually doing a good job, and how to see what it is doing in production. For an FDE, evals are not optional. They are how we prove value, catch regressions, and get the customer to sign off on going live.

- [What is LLM Evaluation? Metrics, Benchmarks, and Methods Explained](https://outcomeschool.com/blog/llm-evaluation)
- [What is LLM as a Judge?](https://outcomeschool.com/blog/llm-as-a-judge)
- [How to Evaluate AI Agents? Metrics, Methods, and Best Practices](https://outcomeschool.com/blog/ai-agent-evaluation)
- [What is AI Agent Observability? Traces, Spans, and Metrics Explained](https://outcomeschool.com/blog/ai-agent-observability)

### Step 9: AI Safety, Security, and Trust

In this step, we will learn how to keep an AI system safe inside a customer's environment. Enterprise customers care deeply about this: what the model is allowed to say, what it is allowed to do, and how attackers might try to break it.

- [How do LLM Guardrails work?](https://outcomeschool.com/blog/how-do-llm-guardrails-work)
- [What is Prompt Injection in LLMs and How Do We Defend Against It?](https://outcomeschool.com/blog/prompt-injection-in-llms)
- [How does LLM Watermarking work?](https://outcomeschool.com/blog/how-does-llm-watermarking-work)

### Step 10: Latency and Cost in Production

In this step, we will learn how to make LLMs faster and cheaper to run. A demo that takes 10 seconds per answer or costs too much per user will never reach production. We will learn what happens during inference, the techniques that speed it up, and the serving engines a customer may run on their own servers.

- [LLM Inference Optimization](https://outcomeschool.com/blog/llm-inference-optimization)
- [LLM Inference Optimization](https://www.youtube.com/watch?v=jV2sCj4lHYk) (Video)
- [Prefill vs Decode: LLM Inference Optimization](https://outcomeschool.com/blog/prefill-vs-decode-llm-inference-optimization)
- [The First-Token Latency Problem in LLMs](https://www.youtube.com/watch?v=XD8DD4cEHu0) (Video)
- [What is KV Cache in LLMs?](https://outcomeschool.com/blog/kv-cache-in-llms)
- [What is Paged Attention in LLMs?](https://outcomeschool.com/blog/paged-attention-in-llms)
- [What is Continuous Batching in LLMs?](https://outcomeschool.com/blog/continuous-batching-in-llms)
- [What is Speculative Decoding?](https://outcomeschool.com/blog/speculative-decoding)
- [What is Prefill-Decode Disaggregation in LLM Inference?](https://outcomeschool.com/blog/prefill-decode-disaggregation)
- [How does Model Quantization work?](https://outcomeschool.com/blog/how-does-model-quantization-work)
- [How does GGUF work?](https://outcomeschool.com/blog/how-does-gguf-work)
- [How does llama.cpp run LLMs on everyday hardware?](https://outcomeschool.com/blog/how-does-llama-cpp-run-llms-on-everyday-hardware)
- [How does Ollama work?](https://outcomeschool.com/blog/how-does-ollama-work)
- [How does vLLM work?](https://outcomeschool.com/blog/how-does-vllm-work)
- [How does SGLang work?](https://outcomeschool.com/blog/how-does-sglang-work)
- [How does TensorRT-LLM work?](https://outcomeschool.com/blog/how-does-tensorrt-llm-work)

### Step 11: Fine-Tuning and Customizing Models

In this step, we will learn what to do when prompting and RAG are not enough: when the customer needs a specific style, format, or domain behavior, or wants a smaller and cheaper model that matches a bigger one. An FDE must know when fine-tuning is the right call and when it is not.

- [How does Fine-Tuning work?](https://outcomeschool.com/blog/how-does-fine-tuning-work)
- [What is LoRA (Low-Rank Adaptation)?](https://outcomeschool.com/blog/lora-low-rank-adaptation-of-llms)
- [How does Prefix Tuning work?](https://outcomeschool.com/blog/how-does-prefix-tuning-work)
- [How does Knowledge Distillation work?](https://outcomeschool.com/blog/how-does-knowledge-distillation-work)
- [What is Continual Learning in LLMs? Solving Catastrophic Forgetting](https://outcomeschool.com/blog/continual-learning-in-llms)
- [What is RLHF? Reinforcement Learning from Human Feedback Explained](https://outcomeschool.com/blog/reinforcement-learning-from-human-feedback-rlhf)
- [What is Direct Preference Optimization (DPO)?](https://outcomeschool.com/blog/direct-preference-optimization-dpo)

### Step 12: AI System Design and Infrastructure

In this step, we will learn how to design a complete AI system end to end and where to run it. An FDE must be able to sit with the customer's architects, draw the full system on a whiteboard, and advise on where it should run: in the cloud, on their own GPUs, or on the device.

Learn AI System Design step by step: [AI System Design](https://github.com/amitshekhariitbhu/ai-system-design)

- [How does a GPU work for Deep Learning?](https://outcomeschool.com/blog/how-does-a-gpu-work-for-deep-learning)
- [How do CUDA Kernels work?](https://outcomeschool.com/blog/how-do-cuda-kernels-work)
- [How does a Google TPU work?](https://outcomeschool.com/blog/how-does-a-google-tpu-work)
- [How does an LPU work?](https://outcomeschool.com/blog/how-does-an-lpu-work)
- [Cloud vs On-device Model Deployment](https://outcomeschool.com/blog/cloud-vs-on-device-model-deployment)

### Step 13: Customer Use Case: Real-Time Voice AI Agent

In this step, we will see everything come together in one of the most requested customer deployments: a real-time voice AI agent for customer support, sales, or scheduling. It touches models, agents, tools, latency, streaming, and system design all at once, which makes it the perfect end-to-end FDE project.

- [Design a Real-Time Voice AI Agent](https://outcomeschool.com/blog/design-a-real-time-voice-ai-agent)
- [Cascaded vs Speech-to-Speech: How to choose the right voice agent architecture?](https://outcomeschool.com/blog/cascaded-vs-speech-to-speech)
- [What is turn-taking in a voice AI agent?](https://outcomeschool.com/blog/what-is-turn-taking-in-a-voice-ai-agent)
- [How does endpointing decide when the user has finished speaking?](https://outcomeschool.com/blog/endpointing-in-voice-agents)
- [How do silence-based and model-based turn detection differ?](https://outcomeschool.com/blog/silence-vs-model-based-turn-detection)
- [How does dynamic endpointing adapt to how fast a user talks?](https://outcomeschool.com/blog/dynamic-endpointing)
- [How does a voice agent handle long pauses when the user is thinking?](https://outcomeschool.com/blog/long-pauses-in-voice-agents)
- [How does a voice agent know a phone number or email is not finished yet?](https://outcomeschool.com/blog/unfinished-input-in-voice-agents)
- [What is barge-in in a voice AI agent?](https://outcomeschool.com/blog/what-is-barge-in-in-a-voice-ai-agent)
- [How do you build a latency budget for a voice AI agent?](https://outcomeschool.com/blog/voice-agent-latency-budget)
- [How does the voice-to-voice latency of a voice agent get measured?](https://outcomeschool.com/blog/voice-to-voice-latency)
- [Why does the time-to-first-audio matter more than total response time?](https://outcomeschool.com/blog/time-to-first-audio)
- [How does sentence chunking feed LLM output into TTS faster?](https://outcomeschool.com/blog/sentence-chunking-for-tts)
- [How does a TTS model start speaking before the full sentence arrives?](https://outcomeschool.com/blog/streaming-tts)
- [How does speculative LLM generation start replying before the user finishes?](https://outcomeschool.com/blog/speculative-generation-in-voice-agents)
- [How do filler phrases hide latency in a voice agent?](https://outcomeschool.com/blog/filler-phrases-in-voice-agents)
- [How does a voice agent hide the delay of a slow tool call?](https://outcomeschool.com/blog/slow-tool-calls-in-voice-agents)

### Step 14: Prepare for Forward Deployed Engineer Interviews

Now that we have learned everything from AI foundations to shipping a production system at a customer site, it's time to prepare for the interviews.

FDE interviews usually test three things:

- **Coding with AI Agents:** practical, real-world development using AI coding agents to build, debug, and ship a feature end to end.
- **AI system design:** designing a RAG system, an agent, or a voice agent for a given customer problem, with trade-offs on quality, latency, cost, and security. Steps 5 to 13 and the [AI System Design](https://github.com/amitshekhariitbhu/ai-system-design) guide prepare us for this.
- **Customer scenarios:** a vague business problem is given, and we must ask the right questions, define success, pick an approach, and explain it simply. Step 0 and Step 8 prepare us for this.

Join the [AI and Machine Learning](https://outcomeschool.com/program/ai-and-machine-learning) program at Outcome School to learn all of these.

### License

```
   Copyright (C) 2026 Outcome School

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```
