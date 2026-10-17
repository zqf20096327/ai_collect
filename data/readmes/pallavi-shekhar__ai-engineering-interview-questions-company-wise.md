<p align="center">
    <img alt="AI Engineering Interview Questions Company Wise" src="https://github.com/pallavi-shekhar/ai-engineering-interview-questions-company-wise/blob/main/assets/banner.png">
</p>

# AI Engineering Interview Questions Company Wise

> AI Engineering Interview Questions Company Wise - Your Cheat Sheet For AI Engineering Interviews at Top AI Companies
>
> Real interview questions asked in AI Engineering interviews at 35 companies, organized company by company, with answers linked wherever we have them.
>
> These interview questions and answers are helpful for roles such as:
>
> - AI Engineer
> - Gen AI Engineer
> - LLM Engineer
> - Agentic AI Engineer
> - AI Agent Engineer
> - Machine Learning Engineer
> - Research Engineer
> - Applied Scientist
> - Forward Deployed Engineer
> - AI Solutions Architect
> - AI Platform Engineer
> - Applied AI Engineer
> - LLM Inference and Performance Engineer
> - MLOps Engineer
> - LLMOps Engineer

## Table of Contents

- [How to use this](#how-to-use-this)
- [Common Questions Asked Across Companies](#common-questions-asked-across-companies)
  - [LLM Internals and Architecture](#llm-internals-and-architecture)
  - [Inference, Serving and GPU Performance](#inference-serving-and-gpu-performance)
  - [RAG and Retrieval](#rag-and-retrieval)
  - [Agents and Tool Use](#agents-and-tool-use)
  - [Fine-Tuning, Post-Training and Alignment](#fine-tuning-post-training-and-alignment)
  - [Evaluation and Observability](#evaluation-and-observability)
  - [Safety, Security and Responsible AI](#safety-security-and-responsible-ai)
  - [Multimodal, Speech and Voice AI](#multimodal-speech-and-voice-ai)
  - [AI System Design](#ai-system-design)
  - [Coding and Data Structures](#coding-and-data-structures)
- [Frontier AI Labs](#frontier-ai-labs)
  - [Anthropic](#anthropic)
  - [OpenAI](#openai)
  - [Google DeepMind and Google AI](#google-deepmind-and-google-ai)
  - [Meta (Superintelligence Labs, FAIR, Llama)](#meta-superintelligence-labs-fair-llama)
  - [xAI](#xai)
  - [Mistral AI](#mistral-ai)
  - [Cohere](#cohere)
  - [DeepSeek](#deepseek)
  - [Moonshot AI (Kimi)](#moonshot-ai-kimi)
  - [Zhipu AI (GLM)](#zhipu-ai-glm)
  - [Alibaba (Qwen)](#alibaba-qwen)
  - [Sarvam AI](#sarvam-ai)
- [Big Tech AI Organizations](#big-tech-ai-organizations)
  - [Microsoft](#microsoft)
  - [Amazon (AWS)](#amazon-aws)
  - [Apple](#apple)
  - [NVIDIA](#nvidia)
  - [Tesla](#tesla)
  - [Consumer-Scale ML Companies (Uber, Netflix, LinkedIn, Airbnb, Pinterest, Spotify)](#consumer-scale-ml-companies-uber-netflix-linkedin-airbnb-pinterest-spotify)
- [AI Infrastructure and Platform Companies](#ai-infrastructure-and-platform-companies)
  - [Databricks](#databricks)
  - [Groq](#groq)
  - [Together AI](#together-ai)
  - [Hugging Face](#hugging-face)
  - [Scale AI](#scale-ai)
  - [Perplexity](#perplexity)
- [AI-Native Product Companies](#ai-native-product-companies)
  - [Cursor (Anysphere)](#cursor-anysphere)
  - [Cognition (Devin, Windsurf)](#cognition-devin-windsurf)
  - [Sierra](#sierra)
  - [Harvey](#harvey)
  - [Glean](#glean)
  - [Character.AI](#characterai)
  - [ElevenLabs](#elevenlabs)
  - [Abridge](#abridge)
  - [Figure AI](#figure-ai)
  - [Waymo](#waymo)
- [Forward-Deployed and Enterprise AI](#forward-deployed-and-enterprise-ai)
  - [Palantir](#palantir)

### Prepared and maintained by [Outcome School](https://outcomeschool.com)

> AI and Machine Learning Program by Outcome School: [AI and Machine Learning Program](https://outcomeschool.com/program/ai-and-machine-learning)

### Follow Outcome School

- [YouTube](https://youtube.com/@OutcomeSchool)
- [X/Twitter](https://x.com/outcome_school)
- [LinkedIn](https://www.linkedin.com/company/outcomeschool)
- [GitHub](https://github.com/OutcomeSchool)

---

> **Note: We will keep updating this with new questions and answers.**
>
> For topic-wise questions and answers, see [AI Engineering Interview Questions and Answers](https://github.com/amitshekhariitbhu/ai-engineering-interview-questions).

---

## How to use this

- Questions are compiled from publicly reported interview experiences. Nothing here is confidential. Interview loops change constantly and vary by team, level, and region, so treat each company section as a map of what that company cares about, not a script of what you will be asked.
- Start with [Common Questions Asked Across Companies](#common-questions-asked-across-companies). These are the questions that recur across many companies. Each one is listed once, with the companies that ask it, so nothing is repeated in the company sections.
- Then go to your target companies. Each company section has the roles it covers, the interview loop as publicly reported, and the company-specific questions grouped by topic.
- Wherever we have an answer, it is linked right below the question. We will keep adding answers.

---

## Common Questions Asked Across Companies

> These questions come up in AI Engineering interviews at many companies. Each question is listed once here, with the companies where it (or a company-specific version of it) is asked. Work through these first.

### LLM Internals and Architecture

- Explain scaled dot-product attention and why the 1/sqrt(d_k) scaling factor matters.
  - Answer: [Math behind √dₖ Scaling Factor in Attention](https://outcomeschool.com/blog/scaling-dot-product-attention) and [Math behind Attention - Q, K, and V](https://outcomeschool.com/blog/math-behind-attention-qkv)
- What is the KV cache, and what are its memory implications at scale? Derive the formula.
  - Asked at: [OpenAI](#openai), [xAI](#xai), [Mistral AI](#mistral-ai), [Amazon](#amazon-aws), [Apple](#apple), [NVIDIA](#nvidia), [Together AI](#together-ai), [Character.AI](#characterai)
  - Answer: [What is KV Cache in LLMs?](https://outcomeschool.com/blog/kv-cache-in-llms) and [KV Cache Compression](https://outcomeschool.com/blog/kv-cache-compression)
- What are Multi-Query Attention (MQA) and Grouped-Query Attention (GQA), and what do they trade away?
  - Asked at: [Meta](#meta-superintelligence-labs-fair-llama), [Mistral AI](#mistral-ai)
  - Answer: [Grouped Query Attention](https://outcomeschool.com/blog/grouped-query-attention)
- What is Multi-head Latent Attention (MLA) and why did DeepSeek introduce it?
  - Asked at: [DeepSeek](#deepseek), [Moonshot AI](#moonshot-ai-kimi)
  - Answer: [KV Cache Compression](https://outcomeschool.com/blog/kv-cache-compression)
- Explain FlashAttention. It does not reduce FLOPs, so why is it faster?
  - Asked at: [Together AI](#together-ai)
  - Answer: [Decoding Flash Attention in LLMs](https://outcomeschool.com/blog/decoding-flash-attention)
- How does Byte Pair Encoding work, and what are its failure modes (numbers, code, non-Latin scripts)?
  - Asked at: [Alibaba](#alibaba-qwen), [Sarvam AI](#sarvam-ai), [Hugging Face](#hugging-face)
  - Answer: [Byte Pair Encoding](https://outcomeschool.com/blog/bpe-in-llms) and [Tokenization in Large Language Models (LLMs)](https://www.youtube.com/watch?v=sK2s9I84EVI) and [Tokenization in LLMs](https://outcomeschool.com/blog/tokenization-in-llms)
- What is positional encoding in transformers, and how has it evolved (sinusoidal → learned → RoPE → ALiBi)?
  - Answer: [Positional Embeddings in LLMs](https://outcomeschool.substack.com/p/positional-embeddings-in-llms) and [Math Behind RoPE (Rotary Position Embedding)](https://outcomeschool.com/blog/math-behind-rope-rotary-position-embedding)
- Explain RoPE and how position interpolation / YaRN extend context beyond the trained length.
  - Asked at: [Meta](#meta-superintelligence-labs-fair-llama), [Moonshot AI](#moonshot-ai-kimi), [Alibaba](#alibaba-qwen)
  - Answer: [Math Behind RoPE (Rotary Position Embedding)](https://outcomeschool.com/blog/math-behind-rope-rotary-position-embedding)
- What do the Chinchilla scaling laws say, and how do they differ from earlier scaling intuitions?
  - Asked at: [Anthropic](#anthropic)
- What is a mixture-of-experts architecture and how does it scale capacity without scaling FLOPs?
  - Asked at: [Mistral AI](#mistral-ai), [Cohere](#cohere), [DeepSeek](#deepseek), [Moonshot AI](#moonshot-ai-kimi), [Zhipu AI](#zhipu-ai-glm), [Alibaba](#alibaba-qwen)
  - Answer: [Mixture of Experts Explained](https://outcomeschool.com/blog/mixture-of-experts)
- Explain the difference between pre-training, supervised fine-tuning and preference optimisation.
  - Asked at: [Meta](#meta-superintelligence-labs-fair-llama), [Scale AI](#scale-ai)
  - Answer: [Decoding InstructGPT](https://outcomeschool.com/blog/decoding-instructgpt) and [Reinforcement Learning from Human Feedback (RLHF)](https://outcomeschool.com/blog/reinforcement-learning-from-human-feedback-rlhf)
- Compare greedy, beam search, top-k, top-p and temperature sampling. When does each fail?
  - Asked at: [Google DeepMind](#google-deepmind-and-google-ai), [Apple](#apple), [Perplexity](#perplexity)
  - Answer: [How does Temperature control LLM output?](https://outcomeschool.com/blog/how-does-temperature-control-llm-output) and [How do Top-k and Top-p Sampling work?](https://outcomeschool.com/blog/how-do-top-k-and-top-p-sampling-work)
- What is the lost-in-the-middle problem in long contexts and how do you address it?
  - Asked at: [Moonshot AI](#moonshot-ai-kimi)
  - Answer: [The Lost in the Middle Problem in LLMs](https://outcomeschool.com/blog/lost-in-the-middle-problem-in-llms)
- Why is LayerNorm placed pre-block in modern transformers, and what is RMSNorm?
  - Answer: [RMSNorm (Root Mean Square Layer Normalization)](https://outcomeschool.com/blog/rmsnorm-root-mean-square-layer-normalization)
- Explain SwiGLU and why gated activations replaced ReLU/GELU in modern LLM MLP blocks.
  - Asked at: [Meta](#meta-superintelligence-labs-fair-llama)
  - Answer: [Feed-Forward Networks in LLMs](https://outcomeschool.com/blog/feed-forward-networks-in-llms)
- Walk me through what happens, tensor by tensor, in one forward pass of a decoder-only transformer.
  - Asked at: [Anthropic](#anthropic)
  - Answer: [Decoding Transformer Architecture](https://outcomeschool.com/blog/decoding-transformer-architecture)

### Inference, Serving and GPU Performance

- Explain the prefill and decode phases. Why is prefill compute-bound and decode memory-bandwidth-bound?
  - Asked at: [Moonshot AI](#moonshot-ai-kimi), [NVIDIA](#nvidia), [Together AI](#together-ai)
  - Answer: [Prefill vs Decode: LLM Inference Optimization](https://outcomeschool.com/blog/prefill-vs-decode-llm-inference-optimization)
- What is continuous (in-flight) batching and why did it replace static batching?
  - Asked at: [Anthropic](#anthropic), [xAI](#xai), [Mistral AI](#mistral-ai), [NVIDIA](#nvidia), [Together AI](#together-ai)
  - Answer: [Continuous Batching in LLMs](https://outcomeschool.com/blog/continuous-batching-in-llms)
- How does PagedAttention work, and what problem of KV-cache fragmentation does it solve?
  - Asked at: [NVIDIA](#nvidia), [Together AI](#together-ai)
  - Answer: [Paged Attention in LLMs](https://outcomeschool.com/blog/paged-attention-in-llms) and [How does vLLM work?](https://outcomeschool.com/blog/how-does-vllm-work)
- What is speculative decoding? Why is output quality preserved, and when does it not help?
  - Asked at: [NVIDIA](#nvidia), [Together AI](#together-ai)
  - Answer: [Speculative Decoding](https://outcomeschool.com/blog/speculative-decoding)
- Explain prefix caching / prompt caching. When should you use it, and what invalidates a cached prefix?
  - Asked at: [Moonshot AI](#moonshot-ai-kimi), [Character.AI](#characterai)
  - Answer: [How does Prompt Caching work?](https://outcomeschool.com/blog/how-does-prompt-caching-work)
- Compare FP16, BF16, FP8, INT8, INT4 and FP4 for serving. What breaks at each step down?
  - Asked at: [Mistral AI](#mistral-ai), [Apple](#apple), [NVIDIA](#nvidia), [Together AI](#together-ai), [Character.AI](#characterai)
  - Answer: [How does Model Quantization work?](https://outcomeschool.com/blog/how-does-model-quantization-work)
- Compare tensor, pipeline, data, sequence and expert parallelism. When do you combine them?
  - Asked at: [Google DeepMind](#google-deepmind-and-google-ai), [Meta](#meta-superintelligence-labs-fair-llama), [Amazon](#amazon-aws), [NVIDIA](#nvidia)
- Estimate the GPU memory needed to serve a 70B model: weights, KV cache, activations, fragmentation.
  - Asked at: [NVIDIA](#nvidia)
  - Answer: [What is KV Cache in LLMs?](https://outcomeschool.com/blog/kv-cache-in-llms) and [Paged Attention in LLMs](https://outcomeschool.com/blog/paged-attention-in-llms)
- What are TTFT, TPOT, ITL and throughput, and how do they trade against each other?
  - Asked at: [Microsoft](#microsoft), [Apple](#apple), [Perplexity](#perplexity)
  - Answer: [Prefill vs Decode: LLM Inference Optimization](https://outcomeschool.com/blog/prefill-vs-decode-llm-inference-optimization) and [The First-Token Latency Problem in LLMs](https://www.youtube.com/watch?v=XD8DD4cEHu0)
- Do the roofline maths: how many tokens/sec can one H100 produce for a 70B model at batch size 1?
  - Asked at: [NVIDIA](#nvidia), [Together AI](#together-ai)
  - Answer: [Prefill vs Decode: LLM Inference Optimization](https://outcomeschool.com/blog/prefill-vs-decode-llm-inference-optimization)
- When would you choose vLLM vs SGLang vs TensorRT-LLM vs a custom stack?
  - Asked at: [NVIDIA](#nvidia), [Together AI](#together-ai)
  - Answer: [How does vLLM work?](https://outcomeschool.com/blog/how-does-vllm-work), [How does SGLang work?](https://outcomeschool.com/blog/how-does-sglang-work) and [How does TensorRT-LLM work?](https://outcomeschool.com/blog/how-does-tensorrt-llm-work)
- How would you cut LLM serving cost by 10x? Enumerate every lever and rank them.
  - Asked at: [Microsoft](#microsoft), [Amazon](#amazon-aws), [NVIDIA](#nvidia), [Cursor](#cursor-anysphere)
  - Answer: Explained in this video: [LLM Inference Optimization](https://www.youtube.com/watch?v=jV2sCj4lHYk) and [LLM Inference Optimization](https://outcomeschool.com/blog/llm-inference-optimization)
- Your p99 latency doubled after a deploy with no model change. Walk through the diagnosis.
  - Asked at: [OpenAI](#openai), [Amazon](#amazon-aws), [Databricks](#databricks), [Perplexity](#perplexity)
- What is chunked prefill, and why does it improve tail latency under mixed traffic?
- Explain disaggregated prefill/decode serving and when it pays for itself.
  - Asked at: [Moonshot AI](#moonshot-ai-kimi), [Groq](#groq)
  - Answer: [Prefill-Decode Disaggregation in LLM Inference](https://outcomeschool.com/blog/prefill-decode-disaggregation)

### RAG and Retrieval

- What chunking strategy would you use for a large technical documentation corpus, and why?
  - Asked at: [Glean](#glean)
  - Answer: [Chunking Strategies for RAG](https://outcomeschool.com/blog/chunking-strategies-for-rag)
- How do you choose between a sparse retriever (BM25) and a dense retriever? When do you need both?
  - Asked at: [Microsoft](#microsoft), [Perplexity](#perplexity), [Glean](#glean)
  - Answer: [How does Hybrid Search work?](https://outcomeschool.com/blog/how-does-hybrid-search-work)
- What is a reranker, when should you use one, and what does a cross-encoder cost you?
  - Asked at: [Cohere](#cohere), [Microsoft](#microsoft), [Perplexity](#perplexity)
  - Answer: [How does a Reranker work?](https://outcomeschool.com/blog/how-does-a-reranker-work)
- How would you evaluate the quality of a RAG pipeline: retrieval and generation separately?
  - Asked at: [Cohere](#cohere)
  - Answer: [LLM Evaluation](https://outcomeschool.com/blog/llm-evaluation)
- What is HyDE (hypothetical document embeddings) and when does it outperform standard dense retrieval?
  - Answer: [How does HyDE work in RAG?](https://outcomeschool.com/blog/how-does-hyde-work)
- How does agentic RAG differ from standard RAG, and when is the extra complexity justified?
  - Answer: [Agentic RAG](https://outcomeschool.com/blog/agentic-rag)
- What causes semantic drift in embedding search and how do you detect it?
  - Asked at: [Cohere](#cohere)
- Design permission-aware retrieval: users must never see content they can't access in the source system.
  - Asked at: [Microsoft](#microsoft), [Databricks](#databricks), [Glean](#glean), [Palantir](#palantir)
- Compare HNSW, IVF-PQ and flat indexes. How do you pick, and what does recall@k cost in latency?
  - Answer: [How does Approximate Nearest Neighbor (ANN) search work?](https://outcomeschool.com/blog/how-does-approximate-nearest-neighbor-ann-search-work) and [How does a Vector Database work?](https://outcomeschool.com/blog/how-does-a-vector-database-work)
- How do you handle tables, figures and multi-column PDFs in a retrieval pipeline?
- How do you keep an index fresh when the underlying corpus changes continuously?
  - Asked at: [Perplexity](#perplexity), [Cursor](#cursor-anysphere)
- How do you attribute every claim in a generated answer to a specific retrieved span?
  - Asked at: [Perplexity](#perplexity), [Harvey](#harvey), [Abridge](#abridge)

### Agents and Tool Use

- Explain the ReAct pattern and what it solves over chain-of-thought alone.
  - Answer: [ReAct Agent](https://outcomeschool.com/blog/react-agent) and [How does Chain-of-Thought (CoT) Prompting work?](https://outcomeschool.com/blog/how-does-chain-of-thought-prompting-work)
- How do you handle tool-call errors, timeouts and retries in an agentic loop?
  - Asked at: [OpenAI](#openai), [Cognition](#cognition-devin-windsurf)
  - Answer: [AI Agent Loop](https://outcomeschool.com/blog/ai-agent-loop)
- What is the difference between structured output and function calling?
  - Asked at: [Mistral AI](#mistral-ai), [Apple](#apple)
  - Answer: [How does Function Calling work in LLMs?](https://outcomeschool.com/blog/how-does-function-calling-work-in-llms)
- What is MCP (Model Context Protocol) and how does it differ from traditional function calling?
  - Asked at: [Microsoft](#microsoft)
  - Answer: Explained in this video: [AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization](https://www.youtube.com/watch?v=lnfWvX66FUk) and [What is MCP (Model Context Protocol)?](https://outcomeschool.com/blog/what-is-mcp-model-context-protocol)
- How many tools is too many? How do you design tool schemas an LLM can actually use correctly?
  - Asked at: [Anthropic](#anthropic), [Cognition](#cognition-devin-windsurf)
  - Answer: Explained in this video: [AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization](https://www.youtube.com/watch?v=lnfWvX66FUk)
- How does multi-agent orchestration work, and when does it break down?
  - Asked at: [Cognition](#cognition-devin-windsurf)
  - Answer: [Multi-Agent Systems](https://outcomeschool.com/blog/multi-agent-systems) and [AI Orchestration](https://outcomeschool.com/blog/ai-orchestration)
- Design memory for a long-running agent: what do you store, where, and how do you retrieve it?
  - Asked at: [Anthropic](#anthropic)
  - Answer: [AI Agent Memory](https://outcomeschool.com/blog/ai-agent-memory) and [How does ChatGPT remember you?](https://outcomeschool.com/blog/how-does-chatgpt-remember-you)
- How does an agent decide when to call a tool versus answer from its own knowledge?
  - Answer: [How does Function Calling work in LLMs?](https://outcomeschool.com/blog/how-does-function-calling-work-in-llms)
- What makes an agent loop terminate correctly? How do you bound cost and steps?
  - Answer: [AI Agent Loop](https://outcomeschool.com/blog/ai-agent-loop) and [Fix an infinite loop in an AI agent](https://www.linkedin.com/posts/pallavi-shekhar_ai-aiagents-machinelearning-share-7440257380707364864-5Ycc)
- How do you make an agent's actions reversible, or at least auditable, in a production system?
  - Asked at: [Palantir](#palantir)
- Design human-in-the-loop approval for an agent that takes consequential actions.
  - Asked at: [OpenAI](#openai), [Palantir](#palantir)
- Your agent drifts after a long run and confidently works on the wrong thing. Diagnose it.
  - Asked at: [Cognition](#cognition-devin-windsurf)

### Fine-Tuning, Post-Training and Alignment

- Walk me through RLHF end to end: reward model, policy optimisation, KL penalty.
  - Answer: [Reinforcement Learning from Human Feedback (RLHF)](https://outcomeschool.com/blog/reinforcement-learning-from-human-feedback-rlhf) and [Proximal Policy Optimization (PPO)](https://outcomeschool.com/blog/proximal-policy-optimization-ppo)
- What is DPO and why did it displace PPO-based RLHF at many labs? When is online RL still better?
  - Asked at: [Hugging Face](#hugging-face), [Scale AI](#scale-ai)
  - Answer: [Direct Preference Optimization (DPO)](https://outcomeschool.com/blog/direct-preference-optimization-dpo)
- Explain GRPO and why dropping the value network matters at scale.
  - Asked at: [DeepSeek](#deepseek)
  - Answer: [Group Relative Policy Optimization (GRPO)](https://outcomeschool.com/blog/group-relative-policy-optimization-grpo)
- Explain the LoRA decomposition mathematically. Why does it work, and how do you choose the rank r?
  - Answer: [LoRA - Low-Rank Adaptation of LLMs](https://outcomeschool.com/blog/lora-low-rank-adaptation-of-llms)
- How does QLoRA achieve its memory reduction, and what are the quantization trade-offs?
  - Asked at: [Hugging Face](#hugging-face)
  - Answer: Explained in this video: [AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization](https://www.youtube.com/watch?v=lnfWvX66FUk) and [How does Model Quantization work?](https://outcomeschool.com/blog/how-does-model-quantization-work)
- Compare LoRA, prefix tuning, prompt tuning and full fine-tuning. When would you choose each?
  - Asked at: [Sarvam AI](#sarvam-ai), [Apple](#apple)
  - Answer: [How does fine-tuning work?](https://outcomeschool.com/blog/how-does-fine-tuning-work) and [How does Prefix Tuning work?](https://outcomeschool.com/blog/how-does-prefix-tuning-work)
- What is catastrophic forgetting and how do you mitigate it during fine-tuning?
  - Asked at: [Mistral AI](#mistral-ai)
  - Answer: [Continual Learning in LLMs](https://outcomeschool.com/blog/continual-learning-in-llms)
- Prompting, RAG or fine-tuning: give me your decision framework with cost and latency attached.
  - Asked at: [OpenAI](#openai), [Mistral AI](#mistral-ai), [Cohere](#cohere), [Microsoft](#microsoft), [Databricks](#databricks), [Glean](#glean)
  - Answer: Explained in this video: [AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization](https://www.youtube.com/watch?v=lnfWvX66FUk)
- Do the GPU memory maths for full fine-tuning a 7B model in bf16 with Adam. Now with LoRA.
  - Asked at: [Mistral AI](#mistral-ai), [Hugging Face](#hugging-face)
- What is RLVR (RL with verifiable rewards) and where does it beat a learned reward model?
  - Asked at: [Zhipu AI](#zhipu-ai-glm), [Alibaba](#alibaba-qwen), [Sarvam AI](#sarvam-ai), [Scale AI](#scale-ai)
  - Answer: [Group Relative Policy Optimization (GRPO)](https://outcomeschool.com/blog/group-relative-policy-optimization-grpo)
- Explain reward hacking in RLHF and how labs address it.
  - Asked at: [Scale AI](#scale-ai)
  - Answer: [Reinforcement Learning from Human Feedback (RLHF)](https://outcomeschool.com/blog/reinforcement-learning-from-human-feedback-rlhf)
- What is distillation, and how do you build a strong small model from a large one?
  - Asked at: [Alibaba](#alibaba-qwen)
  - Answer: [How does Knowledge Distillation work?](https://outcomeschool.com/blog/how-does-knowledge-distillation-work)

### Evaluation and Observability

- Design an LLM-as-judge evaluation. What are its known biases and how do you correct for them?
  - Asked at: [Perplexity](#perplexity)
  - Answer: [LLM as a Judge](https://outcomeschool.com/blog/llm-as-a-judge)
- How do you build an eval set when there is no labelled ground truth and experts are expensive?
  - Asked at: [Cohere](#cohere), [Harvey](#harvey)
- How do you detect and measure hallucinations in a production RAG system?
  - Asked at: [Anthropic](#anthropic), [OpenAI](#openai), [Cursor](#cursor-anysphere)
- Design the regression gate that decides whether a prompt or model change ships.
  - Asked at: [Anthropic](#anthropic)
- Why do benchmark scores improve while users say the system got worse? Enumerate the reasons.
  - Asked at: [Cognition](#cognition-devin-windsurf)
- What is benchmark contamination and how do you guard against it?
  - Asked at: [Zhipu AI](#zhipu-ai-glm), [Alibaba](#alibaba-qwen), [Scale AI](#scale-ai)
  - Answer: [LLM Evaluation](https://outcomeschool.com/blog/llm-evaluation)
- What observability does a production LLM system need: traces, spans, costs, feedback?
  - Answer: [AI Agent Observability](https://outcomeschool.com/blog/ai-agent-observability)
- How do you manage prompt versioning and rollbacks in production?
- Design online evaluation: what do you log, what do you sample, and what do you A/B?
  - Asked at: [Perplexity](#perplexity)
- How would you evaluate an agent, as opposed to a single model response?
  - Asked at: [Moonshot AI](#moonshot-ai-kimi), [Zhipu AI](#zhipu-ai-glm), [Scale AI](#scale-ai), [Cognition](#cognition-devin-windsurf)
  - Answer: [AI Agent Evaluation](https://outcomeschool.com/blog/ai-agent-evaluation)

### Safety, Security and Responsible AI

- What is prompt injection (direct and indirect), and what is your layered defence?
  - Asked at: [Anthropic](#anthropic), [OpenAI](#openai), [Microsoft](#microsoft), [Sierra](#sierra)
  - Answer: [Prompt Injection in LLMs](https://outcomeschool.com/blog/prompt-injection-in-llms)
- Walk me through the OWASP Top 10 for LLM applications and which ones actually bite in practice.
- What is the difference between jailbreaking and adversarial prompting?
  - Answer: [Prompt Injection in LLMs](https://outcomeschool.com/blog/prompt-injection-in-llms)
- Design guardrails for a consumer-facing assistant. Input filters, output filters, or both?
  - Asked at: [Sierra](#sierra), [Character.AI](#characterai)
  - Answer: [How do LLM guardrails work?](https://outcomeschool.com/blog/how-do-llm-guardrails-work)
- What is Constitutional AI and how does it differ from RLHF? What is RLAIF?
  - Asked at: [Anthropic](#anthropic)
- How do you prevent an agent with tool access from exfiltrating data via a malicious web page?
  - Asked at: [OpenAI](#openai)
  - Answer: [Prompt Injection in LLMs](https://outcomeschool.com/blog/prompt-injection-in-llms)
- How do you handle PII in prompts, logs and training data?
  - Asked at: [Abridge](#abridge)
- What is mechanistic interpretability and why do labs invest in it?
- How would you audit a deployed model for differential performance across user groups?
  - Asked at: [Microsoft](#microsoft)
- Design a red-teaming programme for a model you are about to release.
  - Answer: [LLM Evaluation](https://outcomeschool.com/blog/llm-evaluation)

### Multimodal, Speech and Voice AI

- How do vision-language models get images into an LLM: projector, cross-attention, or native tokens?
  - Asked at: [Meta](#meta-superintelligence-labs-fair-llama), [Alibaba](#alibaba-qwen)
  - Answer: [Multimodal AI](https://outcomeschool.com/blog/multimodal-ai) and [Decoding Vision Transformer (ViT)](https://outcomeschool.com/blog/decoding-vision-transformer-vit)
- What changes when you move from images to video?
  - Asked at: [Meta](#meta-superintelligence-labs-fair-llama)
- Budget the latency for a real-time voice agent: VAD, ASR, LLM, TTS, network. Where does the time go?
  - Asked at: [Sarvam AI](#sarvam-ai), [ElevenLabs](#elevenlabs)
  - Answer: [Design a Real-Time Voice AI Agent](https://outcomeschool.com/blog/design-a-real-time-voice-ai-agent)
- Design barge-in / interruption handling for a voice agent.
  - Asked at: [ElevenLabs](#elevenlabs)
  - Answer: [Design a Real-Time Voice AI Agent](https://outcomeschool.com/blog/design-a-real-time-voice-ai-agent)
- Cascaded ASR+LLM+TTS versus native speech-to-speech: argue both sides.
  - Asked at: [ElevenLabs](#elevenlabs)
  - Answer: [Design a Real-Time Voice AI Agent](https://outcomeschool.com/blog/design-a-real-time-voice-ai-agent)
- How do you evaluate ASR quality beyond WER, and TTS quality when there is no single correct output?
  - Asked at: [ElevenLabs](#elevenlabs)
- How do you handle code-switching and accents in a production ASR system?
  - Asked at: [Sarvam AI](#sarvam-ai), [Abridge](#abridge)
- Explain streaming TTS chunking and jitter-buffer sizing.
  - Asked at: [ElevenLabs](#elevenlabs)
- Design a diarisation system and explain how you attribute roles, not just clusters.
  - Asked at: [Abridge](#abridge)
- How would you build multimodal retrieval over images, video and text in one index?
  - Answer: [How do Image Embeddings work?](https://outcomeschool.com/blog/how-do-image-embeddings-work)

### AI System Design

- Design an enterprise RAG assistant over 10M documents with per-user permissions.
  - Asked at: [OpenAI](#openai), [Microsoft](#microsoft), [Amazon](#amazon-aws), [Databricks](#databricks), [Scale AI](#scale-ai)
- Design a code assistant: repo indexing, context assembly, edit application, evaluation.
  - Asked at: [Cursor](#cursor-anysphere)
  - Answer: [How does Cursor work?](https://outcomeschool.com/blog/how-does-cursor-work) and [How does Claude Code work?](https://outcomeschool.com/blog/how-does-claude-code-work)
- Design a customer-support agent that can take real actions, with escalation to humans.
  - Asked at: [Consumer-Scale ML Companies](#consumer-scale-ml-companies-uber-netflix-linkedin-airbnb-pinterest-spotify), [Sierra](#sierra)
- Design semantic search over a large product catalogue.
  - Asked at: [Character.AI](#characterai)
  - Answer: [How does Semantic Search work?](https://outcomeschool.com/blog/how-does-semantic-search-work)
- Design a content-moderation system combining classifiers and LLMs.
  - Asked at: [Meta](#meta-superintelligence-labs-fair-llama)
- Design a document-intelligence pipeline: scanned PDFs in, structured fields out, at 10M documents.
  - Asked at: [Palantir](#palantir)
- Design a Text-to-SQL system over a warehouse with thousands of tables.
  - Asked at: [Databricks](#databricks), [Palantir](#palantir)
- Design a meeting assistant: recording, diarisation, summary, action items, integrations.
  - Asked at: [Microsoft](#microsoft)
- Design an LLM gateway: routing across providers, failover, caching, budgets and rate limits.
  - Asked at: [Perplexity](#perplexity), [Palantir](#palantir)
  - Answer: [LLM Routing](https://outcomeschool.com/blog/llm-routing) and [How does Semantic Caching work?](https://outcomeschool.com/blog/how-does-semantic-caching-work)
- Design the serving stack for a consumer chat assistant at hundreds of millions of users.
  - Asked at: [Anthropic](#anthropic), [OpenAI](#openai), [Google DeepMind](#google-deepmind-and-google-ai), [Meta](#meta-superintelligence-labs-fair-llama), [xAI](#xai)
  - Answer: [Inside ChatGPT: What Happens After You Hit Enter](https://outcomeschool.substack.com/p/inside-chatgpt-what-happens-after) and [LLM Inference Optimization](https://outcomeschool.com/blog/llm-inference-optimization)

### Coding and Data Structures

- Implement scaled dot-product attention with a causal mask, from scratch, in NumPy or PyTorch.
  - Asked at: [Anthropic](#anthropic), [Google DeepMind](#google-deepmind-and-google-ai), [Amazon](#amazon-aws)
  - Answer: [Math behind Attention - Q, K, and V](https://outcomeschool.com/blog/math-behind-attention-qkv) and [Causal Masking in Attention](https://outcomeschool.com/blog/causal-masking-in-attention)
- Implement multi-head attention, then convert it to grouped-query attention.
  - Asked at: [Google DeepMind](#google-deepmind-and-google-ai), [Mistral AI](#mistral-ai), [Alibaba](#alibaba-qwen)
  - Answer: [Multi-Head Attention in Transformers](https://outcomeschool.com/blog/multi-head-attention-in-transformers) and [Grouped Query Attention](https://outcomeschool.com/blog/grouped-query-attention)
- Implement a KV cache and single-step decode.
  - Asked at: [Moonshot AI](#moonshot-ai-kimi)
  - Answer: [What is KV Cache in LLMs?](https://outcomeschool.com/blog/kv-cache-in-llms)
- Implement BPE training and encoding from scratch.
  - Answer: [Byte Pair Encoding](https://outcomeschool.com/blog/bpe-in-llms)
- Implement top-k, top-p and temperature sampling over a logits vector.
  - Asked at: [Google DeepMind](#google-deepmind-and-google-ai), [Apple](#apple)
  - Answer: [How does Temperature control LLM output?](https://outcomeschool.com/blog/how-does-temperature-control-llm-output) and [How do Top-k and Top-p Sampling work?](https://outcomeschool.com/blog/how-do-top-k-and-top-p-sampling-work)
- Implement an LRU cache with O(1) get/put, then add TTL.
  - Asked at: [OpenAI](#openai), [xAI](#xai), [Alibaba](#alibaba-qwen)
- Implement a token-bucket rate limiter, then make it distributed.
  - Asked at: [Anthropic](#anthropic), [OpenAI](#openai), [xAI](#xai), [Cohere](#cohere)
- Write an async batch processor over an API with concurrency limits, retries with jitter and error isolation.
  - Asked at: [Anthropic](#anthropic), [Perplexity](#perplexity)
- Write a streaming SSE/JSON parser that handles arbitrary chunk boundaries.
  - Asked at: [Cohere](#cohere)
  - Answer: [How does Token Streaming work?](https://outcomeschool.com/blog/how-does-token-streaming-work)
- Implement a text chunker with overlap that never splits a semantic unit.
  - Asked at: [Harvey](#harvey)
  - Answer: [Chunking Strategies for RAG](https://outcomeschool.com/blog/chunking-strategies-for-rag)
- Implement cosine similarity search over embeddings, then explain why you would not ship it.
  - Answer: [How does a Vector Database work?](https://outcomeschool.com/blog/how-does-a-vector-database-work)
- Implement a minimal agent loop with tool dispatch, error handling and a step budget.
  - Asked at: [Cognition](#cognition-devin-windsurf)
  - Answer: [AI Agent Loop](https://outcomeschool.com/blog/ai-agent-loop)

## Frontier AI Labs

### Anthropic

> **Roles this covers:** Member of Technical Staff (MTS), Software Engineer (product / infra / API-serving), Research Engineer, Research Scientist, Applied AI Engineer, Forward Deployed Engineer (Applied AI), Performance Engineer (inference & kernels), Product Engineer (Claude Code / Claude.ai).
>
> **Interview loop, as publicly reported:** Recruiter screen (~30 min, substantive and failable) → CodeSignal-style or live coding assessment (~70–90 min, one practical problem in ~4 progressive levels) → virtual onsite of roughly five rounds: project deep-dive, one or two coding rounds, system design, and a dedicated values/culture round. Reported end-to-end: 3 weeks to ~2 months. Some MLE loops now include an AI-collaboration round where Claude is provided and you are graded on how you direct and verify it.
>
> **Also prepare:** the [common questions](#common-questions-asked-across-companies) tagged Anthropic under [LLM Internals and Architecture](#llm-internals-and-architecture), [Inference, Serving and GPU Performance](#inference-serving-and-gpu-performance), [Agents and Tool Use](#agents-and-tool-use), [Evaluation and Observability](#evaluation-and-observability), [Safety, Security and Responsible AI](#safety-security-and-responsible-ai), [AI System Design](#ai-system-design), [Coding and Data Structures](#coding-and-data-structures).

#### Coding and Data Structures

- Build core business logic for a toy banking application: a spec that grows in four progressive levels against a black-box evaluator.
- Build an in-memory database: SET/GET/DELETE first, then filtered scans, then TTL with timestamps, then file compaction.
- Create a task scheduler.
- Build an OOP system for managing courses, grades and students.
- Given a helper method that crawls a URL, write a crawler over a domain: first synchronous, then make it async.
- Convert nested stack traces into discrete start and end events.
- Build a rate limiter. Every ten minutes I add a requirement: per-tenant limits, burst allowances, then a sliding window. How do you keep the code from collapsing?
- You need to run an LLM call over 50,000 documents. The API allows ~100 concurrent requests and occasionally returns 429s and timeouts. Write the Python.
- How would you parallelise this task? (Concurrency and data mutation come up repeatedly across rounds.)
- SQL: write a query to find the top five pairs of products most frequently purchased together.
- SQL: determine whether any user has overlapping subscription date ranges.
- SQL: return each employee's current salary after an ETL error inserted a new salary row every year.

#### LLM Internals and Architecture

- What are the key components of a Transformer model and why does each matter?
  - Answer: [Decoding Transformer Architecture](https://outcomeschool.com/blog/decoding-transformer-architecture)
- Explain attention-free transformer architectures and their trade-offs.
- Walk me through matrix manipulations relevant to LLM architectures.
  - Answer: [Math behind Attention - Q, K, and V](https://outcomeschool.com/blog/math-behind-attention-qkv)

#### Inference, Serving and GPU Performance

- Design a batched inference system where 100 requests take the same time as 1.
  - Answer: [Continuous Batching in LLMs](https://outcomeschool.com/blog/continuous-batching-in-llms)
- Design the serving stack for a Claude-scale LLM API. Maximise GPU utilisation without wrecking p99 latency.
  - Answer: [LLM Inference Optimization](https://outcomeschool.com/blog/llm-inference-optimization)

#### Agents and Tool Use

- What matters more for an agentic coding tool like Claude Code: the model or the harness? Design the loop.
  - Answer: [How does Claude Code work?](https://outcomeschool.com/blog/how-does-claude-code-work) and [Harness Engineering in AI](https://outcomeschool.com/blog/harness-engineering-in-ai)
- Design the tool surface for a coding agent: which tools exist, what their schemas look like, and how results come back.
  - Answer: [How does Claude Code work?](https://outcomeschool.com/blog/how-does-claude-code-work)

#### Fine-Tuning, Post-Training and Alignment

- Explain Constitutional AI. What does it buy you over vanilla RLHF, and what doesn't it solve?
- How do scaling laws influence the safety evaluation of large models?

#### AI System Design

- Design the Claude chat service.
- Design a system that enables a large language model to handle multiple questions in a single thread.
- Design a distributed search system for 1 billion documents at 1 million QPS.
- Design APIs for developers to access Anthropic's models securely and efficiently.
- Design a file-sharing / distribution system.

#### Evaluation and Observability

- How would you design an experiment to test for a specific emergent capability or bias in a large language model?

#### Safety, Security and Responsible AI

- Your agent reads inbound email and can send replies and search internal docs. Walk me through the prompt-injection attack surface and your defences.
  - Answer: [Prompt Injection in LLMs](https://outcomeschool.com/blog/prompt-injection-in-llms)
- What do you see as the most pressing unsolved problem in AI alignment?
- How would you balance performance optimisation with model interpretability?
- How would you approach designing a system to ensure the safe deployment of AI models in production?

#### Applied and Forward-Deployed Scenarios

- An enterprise customer says “Claude hallucinates too much” in their RAG-based knowledge assistant. You're the applied engineer on the account. What happens in the first 48 hours?
- How would you make complex AI research findings accessible to a non-technical audience?

#### Behavioral and Culture

- Walk me through a project you owned end to end. What were the key technical decisions?
- Why Anthropic specifically, and where do you disagree with Anthropic?
- Tell me about a technical misjudgement that delayed a project.
- What are your thoughts on AI safety and the risks of advanced AI systems?

### OpenAI

> **Roles this covers:** Member of Technical Staff, Software Engineer, Machine Learning Engineer, Research Engineer, Research Scientist, Applied AI Engineer, Forward Deployed Engineer, Solutions Architect, Data Scientist.
>
> **Interview loop, as publicly reported:** Recruiter screen → technical screen (practical coding, often a build-something-real task rather than LeetCode) → onsite: two or three coding/practical rounds, a domain-depth or ML round, a system design round, and behavioural/mission-fit. Applied AI and FDE loops add a customer-scenario and solution-design round.
>
> **Also prepare:** the [common questions](#common-questions-asked-across-companies) tagged OpenAI under [LLM Internals and Architecture](#llm-internals-and-architecture), [Inference, Serving and GPU Performance](#inference-serving-and-gpu-performance), [Agents and Tool Use](#agents-and-tool-use), [Fine-Tuning, Post-Training and Alignment](#fine-tuning-post-training-and-alignment), [Evaluation and Observability](#evaluation-and-observability), [Safety, Security and Responsible AI](#safety-security-and-responsible-ai), [AI System Design](#ai-system-design), [Coding and Data Structures](#coding-and-data-structures).

#### Coding and Data Structures

- Design and implement an in-memory key-value store supporting set, transactional begin, commit and abort.
- Create a database ORM, step by step.
- Code a trivial web crawler using Go.
- Implement a UI from a mockup with provided CSS and API.
- Refactor bad code: here are ~120 lines of working but messy code with passing tests. Improve the architecture without breaking them. What do you change first?
- Write a Python function that displays the first n Fibonacci numbers.
- Infection-spread simulation.

#### ML and DL Fundamentals

- Compute the KL divergence given different random variables.
- If the accuracy of a classifier is 1, what is the lower/upper bound on the loss function for a single training example?
  - Answer: [Math Behind Cross-Entropy Loss](https://outcomeschool.com/blog/math-behind-cross-entropy-loss)
- We have two models, 85% and 82% accuracy. Which do you pick?
- How do you handle missing data in Pandas?

#### LLM Internals and Architecture

- Explain self-attention. What is its computational complexity, and what are your options when contexts get long?
  - Answer: [Self Attention in Transformers](https://outcomeschool.com/blog/self-attention-in-transformers) and [How does Sliding Window Attention work?](https://outcomeschool.com/blog/how-does-sliding-window-attention-work)
- What is the relationship between cross-entropy, KL divergence and perplexity, and why is cross-entropy the training loss for language models?
  - Answer: [Math Behind Cross-Entropy Loss](https://outcomeschool.com/blog/math-behind-cross-entropy-loss)
- What is the effect of adjusting an LLM's context window size?
  - Answer: [Context Window in LLMs](https://www.linkedin.com/posts/amit-shekhar-iitbhu_the-context-window-is-the-llms-working-memory-activity-7437754426175672320-MH9c) and [Why is the context window limited in LLMs?](https://www.youtube.com/watch?v=CGIhxIaOg3M&lc)

#### Agents and Tool Use

- You are building a production agent that calls tools (function calling). What makes the loop reliable enough to ship?
  - Answer: [How does Function Calling work in LLMs?](https://outcomeschool.com/blog/how-does-function-calling-work-in-llms) and [AI Agent Loop](https://outcomeschool.com/blog/ai-agent-loop)

#### AI System Design

- How would you build an LLM-powered enterprise search system?
- Design the serving stack for a ChatGPT-scale consumer assistant: hundreds of millions of weekly users, streaming chat, multiple model tiers.
  - Answer: [Inside ChatGPT: What Happens After You Hit Enter](https://outcomeschool.substack.com/p/inside-chatgpt-what-happens-after)
- Design and build a webhook delivery system that reliably delivers events to customer-registered URLs.
- Design a system to schedule jobs in a distributed environment.
- Design an in-memory database. / Design Slack.

#### Evaluation and Observability

- A customer says “the model got worse” after you upgraded model versions in their deployment. How do you verify and respond?
- An enterprise customer reports that responses from your deployed system have gotten slow. Walk me through the diagnosis.

#### Safety, Security and Responsible AI

- How do you approach GenAI safety in consumer products?
- How would you design safeguards for an AI system that can take actions on behalf of a user?

#### Applied and Forward-Deployed Scenarios

- An enterprise customer says: “We want AI to automate our claims processing.” You're the engineer in the room. What do the first two weeks look like?
- Do you have experience working with APIs? Are you used to working with C-suite executives?

#### Behavioral and Culture

- What is your favourite product and why?
- Tell me about a time you made a mistake.
- Tell me about a time you had a conflict with someone. How did you resolve it and what did you learn?
- Tell me about a time you had conflicting priorities with stakeholders and how you secured alignment.
- What is the project you are most proud of?

### Google DeepMind and Google AI

> **Roles this covers:** Research Engineer, Research Scientist, Machine Learning Engineer, Software Engineer (ML), Forward Deployed Engineer, Applied AI Engineer (Google Cloud / Vertex AI), Data Scientist.
>
> **Interview loop, as publicly reported:** Recruiter screen → technical phone screen (coding, sometimes ML fundamentals) → onsite: two coding rounds, an ML domain/breadth round, an ML system design round, and Googleyness/leadership. DeepMind Research Engineer loops add a research deep-dive plus maths/probability and a from-scratch implementation round; hiring committee and team matching follow.
>
> **Also prepare:** the [common questions](#common-questions-asked-across-companies) tagged Google DeepMind under [LLM Internals and Architecture](#llm-internals-and-architecture), [Inference, Serving and GPU Performance](#inference-serving-and-gpu-performance), [AI System Design](#ai-system-design), [Coding and Data Structures](#coding-and-data-structures).

#### Coding and Data Structures

- You are receiving an unbounded stream of event IDs. Return the k most frequent IDs seen so far, at any point, with bounded memory.
- Closest key: given a dictionary with letter keys and lists of letters as values, find the closest key.
- Write a function to compute root-mean-square error given y_pred and y_true lists.
- Parse bigrams: extract two-word phrases from strings for NLP feature engineering.

#### ML and DL Fundamentals

- Define the bias-variance trade-off and discuss the relationship between the two.
- What are the assumptions of linear regression?
- Distinguish regularization from validation: when is each the right tool?
  - Answer: [Regularization in Machine Learning: L1 vs L2](https://outcomeschool.com/blog/regularization-in-machine-learning)
- Derive the gradient of cross-entropy loss with softmax inputs, and explain why we fuse them numerically.
  - Answer: [Math Behind Cross-Entropy Loss](https://outcomeschool.com/blog/math-behind-cross-entropy-loss) and [Math Behind Backpropagation](https://outcomeschool.com/blog/math-behind-backpropagation)
- Explain the SVD and give two places it shows up in modern deep learning.
- On average, how many fair coin flips until you see two heads in a row? Walk me through it.
- When would you choose Q-learning over policy gradients, and vice versa?
- You have a binary loan-approval classifier and limited access to feature weights. How do you explain a rejection?

#### Fine-Tuning, Post-Training and Alignment

- Your pretraining loss suddenly diverges at step 300k of a long run. Diagnose and fix it.
- Design the training setup for a model that doesn't fit on one accelerator, say 70B parameters on a pod.

#### AI System Design

- Design the serving system for a multimodal assistant (text + image in, streaming text out) at hundreds of millions of users.
- Design a personalised recommendation system for rental listings using demographics, property metadata, amenities, price, reviews and location.
- Design a classifier that predicts the optimal moment to insert a commercial break in a video.
- How would you improve product search results, focusing on the fraction of relevant documents retrieved (recall)?
  - Answer: [Precision vs Recall](https://outcomeschool.com/blog/precision-vs-recall)
- Justify using a neural network for a given problem: what do you need to know about the network, dataset, timeline and business context?

#### Evaluation and Observability

- Build the evaluation harness for a new frontier model release. What does it need to do?
  - Answer: [LLM Evaluation](https://outcomeschool.com/blog/llm-evaluation)
- Do 1 million Seattle ride trips suffice to build an accurate ETA prediction model? How would you decide?

#### Behavioral and Culture

- Tell me about a time you disagreed with a researcher or tech lead about priorities, and what happened.

### Meta (Superintelligence Labs, FAIR, Llama)

> **Roles this covers:** Machine Learning Engineer (E4–E7), Research Engineer, Research Scientist, AI Infrastructure Engineer, Software Engineer (ML), Applied Research Scientist.
>
> **Interview loop, as publicly reported:** Recruiter screen → technical screen (2 coding problems in 45 min) → onsite: two coding rounds, one ML system design round, one ML domain/breadth round, and a behavioural (“Jedi”) round. Some 2026 loops now include an AI-assisted coding round in three stages: explore and fix issues, implement new functionality, extend and improve the system.
>
> **Also prepare:** the [common questions](#common-questions-asked-across-companies) tagged Meta under [LLM Internals and Architecture](#llm-internals-and-architecture), [Inference, Serving and GPU Performance](#inference-serving-and-gpu-performance), [Multimodal, Speech and Voice AI](#multimodal-speech-and-voice-ai), [AI System Design](#ai-system-design).

#### Coding and Data Structures

- Given an array nums of n integers where n > 1, return an output array (product of array except self).
- Find the minimum window in S which will contain all the characters in T.
- Serialize and deserialize a binary tree.
- Convert a binary tree to a circular doubly linked list.
- Alien dictionary: determine character ordering from a sorted word list.
- K closest points to origin; top-k frequent elements; minimum number of conference rooms.
- Regular expression matching with '.' and '\*'.
- Two-part warm-up: given a stream of user actions, return the k most engaged-with items. Then: why might your heap solution be the wrong choice in production?

#### ML and DL Fundamentals

- Your ads CTR model shows a 2% offline AUC gain, but the online A/B is revenue-neutral with worse calibration. What is going on, and what do you do?

#### LLM Internals and Architecture

- Explain the architectural choices in a Llama-class model: why grouped-query attention, RoPE and SwiGLU instead of the vanilla 2017 Transformer?
  - Answer: [Grouped Query Attention](https://outcomeschool.com/blog/grouped-query-attention), [Math Behind RoPE (Rotary Position Embedding)](https://outcomeschool.com/blog/math-behind-rope-rotary-position-embedding) and [Feed-Forward Networks in LLMs](https://outcomeschool.com/blog/feed-forward-networks-in-llms)
- What breaks when you scale LLM training from 8 GPUs to thousands, and how do modern stacks deal with it?

#### Inference, Serving and GPU Performance

- You need to serve a Llama-class 70B+ model to hundreds of millions of assistant users. What does the serving stack look like and where does the money go?
  - Answer: [LLM Inference Optimization](https://outcomeschool.com/blog/llm-inference-optimization)

#### Agents and Tool Use

- You're dropped into an unfamiliar multi-file codebase with a failing behaviour and an LLM assistant available. Walk me through how you'd fix it.

#### Fine-Tuning, Post-Training and Alignment

- Walk me through a post-training recipe to turn a pretrained base model into a personalised assistant.
  - Answer: [Decoding InstructGPT](https://outcomeschool.com/blog/decoding-instructgpt) and [Reinforcement Learning from Human Feedback (RLHF)](https://outcomeschool.com/blog/reinforcement-learning-from-human-feedback-rlhf)

#### AI System Design

- Design the recommendation system for Instagram Reels.
- Design a personalised news-feed ranking system / the “next post” logic for Facebook's feed.
- Design a recommendation system for Facebook Ads, and an evaluation framework for ads ranking.
- Design the ML components behind an Instagram Story feature.
- Design an end-to-end classification pipeline for Marketplace listings.
- Design a language translation model / service.

#### Evaluation and Observability

- How would you build the evaluation system for a Meta AI assistant before and after each model release?
  - Answer: [LLM Evaluation](https://outcomeschool.com/blog/llm-evaluation)

#### Safety, Security and Responsible AI

- Design the harmful-content detection system for Facebook and Instagram uploads.

#### Multimodal, Speech and Voice AI

- How do modern multimodal models get image and video understanding into an LLM, and what changes for video specifically?
  - Answer: [Multimodal AI](https://outcomeschool.com/blog/multimodal-ai)

#### Behavioral and Culture

- Give me an example of a project where you used data and machine learning. What obstacles did you hit?
- Tell me about a time you drove a significant result through ambiguity, and a time you were wrong.
- Tell me about maintaining a production ML pipeline. Why Meta?

### xAI

> **Roles this covers:** Member of Technical Staff, AI Engineer, Infrastructure Engineer, Research Engineer, Product Engineer (Grok), Data / RL environments engineer.
>
> **Interview loop, as publicly reported:** Fast, low-process loops. Typically a recruiter or hiring-manager screen → one or two live coding rounds heavy on data structures and systems → a practical build-something round (often a timed four-hour product build or a stubbed-out module in a real codebase) → founder/leadership conversation. Speed and raw shipping ability are weighted heavily.
>
> **Also prepare:** the [common questions](#common-questions-asked-across-companies) tagged xAI under [LLM Internals and Architecture](#llm-internals-and-architecture), [Inference, Serving and GPU Performance](#inference-serving-and-gpu-performance), [AI System Design](#ai-system-design), [Coding and Data Structures](#coding-and-data-structures).

#### Coding and Data Structures

- Build an in-memory key-value store with SET/GET/DELETE, then add transactions with BEGIN/COMMIT/ROLLBACK, including nested transactions.
- Write an iterator class that lazily flattens an arbitrarily nested list of lists/integers: no generators, explicit state.
- Here is a scheduler class from a small LLM inference engine. One method, \_admit_requests, is a stub: no spec, no docstring, no tests. Walk me through your first thirty minutes.

#### Inference, Serving and GPU Performance

- Estimate the KV-cache memory to serve a 70B-class model at 128k context. What do you do when it doesn't fit?
  - Answer: [What is KV Cache in LLMs?](https://outcomeschool.com/blog/kv-cache-in-llms) and [KV Cache Compression](https://outcomeschool.com/blog/kv-cache-compression)
- Design a rate limiter for an LLM API where cost scales with tokens, not requests.

#### Fine-Tuning, Post-Training and Alignment

- You're training on tens of thousands of GPUs and hardware fails constantly. How do you keep goodput high?
- Loss spikes mid-run on a large pretraining job. Walk me through your debugging process.
- Design a deduplication pipeline for a web-scale pretraining corpus. It has to run as a streaming process.

#### AI System Design

- Design the serving stack for a consumer chatbot with real-time search over a social-media firehose.

#### Behavioral and Culture

- You have four hours to build and demo a working AI-powered product. How do you spend them?

### Mistral AI

> **Roles this covers:** Research Engineer, ML Engineer, Applied AI Engineer, Solutions Architect / Forward Deployed Engineer, Inference Engineer, Platform Engineer.
>
> **Interview loop, as publicly reported:** Recruiter screen → technical screen (Python + ML fundamentals) → pair-programming round building a small LLM-backed service → deep-dive on transformer/serving internals → customer-scenario round for applied roles → culture/founders round. European enterprise and on-prem deployment context shows up throughout.
>
> **Also prepare:** the [common questions](#common-questions-asked-across-companies) tagged Mistral AI under [LLM Internals and Architecture](#llm-internals-and-architecture), [Inference, Serving and GPU Performance](#inference-serving-and-gpu-performance), [Agents and Tool Use](#agents-and-tool-use), [Fine-Tuning, Post-Training and Alignment](#fine-tuning-post-training-and-alignment), [Coding and Data Structures](#coding-and-data-structures).

#### Coding and Data Structures

- Pair-programming: build a service that takes a user question, enriches it with data from a third-party API, and answers via a chat-model API. How do you structure it?

#### LLM Internals and Architecture

- Mistral 7B shipped with grouped-query attention and sliding-window attention. What does each buy you, and what does each cost?
  - Answer: [Grouped Query Attention](https://outcomeschool.com/blog/grouped-query-attention) and [How does Sliding Window Attention work?](https://outcomeschool.com/blog/how-does-sliding-window-attention-work)
- Explain how a Mixtral-style sparse mixture-of-experts model works. Why does a ~47B-parameter model run at roughly the cost of a ~13B one?
  - Answer: [Mixture of Experts Explained](https://outcomeschool.com/blog/mixture-of-experts)

#### Inference, Serving and GPU Performance

- Estimate the KV-cache memory for serving Mistral 7B, and design the rolling-buffer cache that sliding-window attention enables.
  - Answer: [What is KV Cache in LLMs?](https://outcomeschool.com/blog/kv-cache-in-llms) and [How does Sliding Window Attention work?](https://outcomeschool.com/blog/how-does-sliding-window-attention-work)
- You need to quantize a model for a customer's hardware. How do you choose a scheme, and how do you prove quality hasn't regressed?
  - Answer: [How does Model Quantization work?](https://outcomeschool.com/blog/how-does-model-quantization-work)

#### Agents and Tool Use

- How does function calling actually work with an LLM, and how do you make it reliable enough for production agents?
  - Answer: [How does Function Calling work in LLMs?](https://outcomeschool.com/blog/how-does-function-calling-work-in-llms)

#### Fine-Tuning, Post-Training and Alignment

- After fine-tuning on a customer's task, target accuracy is up but the model got worse at everything else. What happened and what do you do?
  - Answer: [Continual Learning in LLMs](https://outcomeschool.com/blog/continual-learning-in-llms)

#### AI System Design

- Design an on-prem deployment of an open-weight model for a European bank that cannot send data to any external API.

### Cohere

> **Roles this covers:** Member of Technical Staff, ML Engineer, Applied AI Engineer, Solutions Architect / Forward Deployed Engineer, Platform & Inference Engineer.
>
> **Interview loop, as publicly reported:** Recruiter screen → technical screen (practical Python, streaming/API-shaped problems) → onsite: coding, retrieval/RAG depth, enterprise deployment design, customer-scenario round, and a values round. Remote-first; autonomy and ownership are explicitly tested.
>
> **Also prepare:** the [common questions](#common-questions-asked-across-companies) tagged Cohere under [LLM Internals and Architecture](#llm-internals-and-architecture), [RAG and Retrieval](#rag-and-retrieval), [Fine-Tuning, Post-Training and Alignment](#fine-tuning-post-training-and-alignment), [Evaluation and Observability](#evaluation-and-observability), [Coding and Data Structures](#coding-and-data-structures).

#### Coding and Data Structures

- Design a token-based rate limiter for a multi-tenant LLM API. Implement the core, then tell me what changes when it's distributed.

#### LLM Internals and Architecture

- Our flagship is a sparse MoE with ~10x more total than active parameters. Why is that architecture a good fit for private enterprise deployment, and where does it hurt?
  - Answer: [Mixture of Experts Explained](https://outcomeschool.com/blog/mixture-of-experts)

#### RAG and Retrieval

- You have an embedding model and a reranker. Why sell both? Design the two-stage retrieval pipeline and tell me when the reranker earns its latency.
  - Answer: [How does a Reranker work?](https://outcomeschool.com/blog/how-does-a-reranker-work)
- An enterprise wants semantic search over ~100M documents but is balking at vector-index cost. Walk me through embedding compression options and the maths.
  - Answer: [How does a Vector Database work?](https://outcomeschool.com/blog/how-does-a-vector-database-work)
- How would you evaluate multilingual retrieval quality when employees query in French and Korean over mostly-English documents?
- A customer 10x'd their indexed documents and reports answer quality “got noticeably worse.” Drive the investigation.

#### Agents and Tool Use

- Design an agent that automates an enterprise workflow, say, drafting RFP responses from internal documents and a CRM. What does “enter-prise-grade” add?

#### AI System Design

- A bank wants the whole stack (model, RAG, agents) deployed air-gapped on their own GPUs. What actually changes versus your SaaS?

#### Evaluation and Observability

- An enterprise customer wants to deploy your RAG system but has no labelled data. How do you evaluate it before and after launch?

#### Behavioral and Culture

- Tell me about a time you owned an ambiguous problem end-to-end without much direction.

### DeepSeek

> **Roles this covers:** Research Engineer, Infrastructure / Systems Engineer, Inference Engineer, Data Engineer, Algorithm Engineer.
>
> **Interview loop, as publicly reported:** Heavily research- and systems-weighted: paper deep-dive, from-scratch implementation rounds in PyTorch, distributed-training and low-precision depth, plus an algorithmic coding round. Expect direct questions about their published architecture and training papers.
>
> **Also prepare:** the [common questions](#common-questions-asked-across-companies) tagged DeepSeek under [LLM Internals and Architecture](#llm-internals-and-architecture), [Fine-Tuning, Post-Training and Alignment](#fine-tuning-post-training-and-alignment).

#### LLM Internals and Architecture

- Walk me through DeepSeekMoE. How is it different from a standard top-2 MoE like Mixtral?
  - Answer: [Mixture of Experts Explained](https://outcomeschool.com/blog/mixture-of-experts) and [DeepSeek-V4 Architecture Explained](https://outcomeschool.com/blog/decoding-deepseek-v4)
- DeepSeek-V3 uses auxiliary-loss-free load balancing. What was wrong with the auxiliary loss, and how does the bias trick work?
- What is multi-token prediction (MTP) and why train with it?
  - Answer: [DeepSeek-V4 Architecture Explained](https://outcomeschool.com/blog/decoding-deepseek-v4)
- Implement top-k MoE routing with a shared expert in PyTorch, and point out the efficiency and correctness traps.
  - Answer: [Mixture of Experts Explained](https://outcomeschool.com/blog/mixture-of-experts)

#### Inference, Serving and GPU Performance

- Sketch how you would serve a 671B-parameter MoE model with low latency under GPU-memory constraints.
  - Answer: [LLM Inference Optimization](https://outcomeschool.com/blog/llm-inference-optimization) 

#### Fine-Tuning, Post-Training and Alignment

- R1-Zero was trained with RL and essentially no SFT first. What did that show, and why did full R1 add SFT back?
  - Answer: [Large Reasoning Models (LRMs)](https://outcomeschool.com/blog/large-reasoning-models)
- FP8 training at 671B scale is hard. What actually breaks in low precision, and how do you make it stable?
- How do you build a training dataset without triggering model collapse when much of your data is synthetic?
- DualPipe overlaps computation and communication in training. Why is that overlap the whole game at this scale, and what is the trade-off?

#### Behavioral and Culture

- DeepSeek claims frontier-class results at a fraction of the usual training cost. If an interviewer asks “how is that even possible,” what is your structured answer?

### Moonshot AI (Kimi)

> **Roles this covers:** Research Engineer, Infrastructure Engineer, Inference / Serving Engineer, Agent Engineer.
>
> **Interview loop, as publicly reported:** Research and long-context systems focused: architecture deep-dive, distributed serving design, a PyTorch implementation round, and an agentic-evaluation discussion.
>
> **Also prepare:** the [common questions](#common-questions-asked-across-companies) tagged Moonshot AI under [LLM Internals and Architecture](#llm-internals-and-architecture), [Inference, Serving and GPU Performance](#inference-serving-and-gpu-performance), [Evaluation and Observability](#evaluation-and-observability), [Coding and Data Structures](#coding-and-data-structures).

#### LLM Internals and Architecture

- Kimi's headline feature is very long context. When you push from 8K to hundreds of thousands of tokens, what actually breaks first, and why?
  - Answer: [The Lost in the Middle Problem in LLMs](https://outcomeschool.com/blog/lost-in-the-middle-problem-in-llms) and [Why is the context window limited in LLMs?](https://www.youtube.com/watch?v=CGIhxIaOg3M&lc)
- Kimi K2 uses Multi-head Latent Attention (MLA). Explain what it does and how it compares to GQA for KV-cache reduction.
  - Answer: [KV Cache Compression](https://outcomeschool.com/blog/kv-cache-compression) and [Grouped Query Attention](https://outcomeschool.com/blog/grouped-query-attention)
- Kimi K2 is a 1T-parameter MoE with ~32B active per token and hundreds of experts. Explain the routing and the systems cost of training it.
  - Answer: [Mixture of Experts Explained](https://outcomeschool.com/blog/mixture-of-experts)
- How do you take a model trained at 8K–32K and make it work at 128K or more?
  - Answer: [Math Behind RoPE (Rotary Position Embedding)](https://outcomeschool.com/blog/math-behind-rope-rotary-position-embedding)

#### Inference, Serving and GPU Performance

- Walk me through why you would disaggregate prefill and decode onto separate machines, as Mooncake does. What does that buy you and what does it cost?
  - Answer: [Prefill-Decode Disaggregation in LLM Inference](https://outcomeschool.com/blog/prefill-decode-disaggregation)
- A chat assistant re-sends a long conversation history on every turn. How do you avoid recomputing all of it, and what are the pitfalls?
  - Answer: [How does Prompt Caching work?](https://outcomeschool.com/blog/how-does-prompt-caching-work)

#### RAG and Retrieval

- For a long-context assistant, when is a 1M-token context window the right tool, and when should you use retrieval instead?
  - Answer: [The Lost in the Middle Problem in LLMs](https://outcomeschool.com/blog/lost-in-the-middle-problem-in-llms)

#### Fine-Tuning, Post-Training and Alignment

- Training a trillion-parameter model, attention logits can blow up and destabilise the run. What is going on, and how does something like MuonClip address it?
- Kimi K1.5 scaled RL for reasoning without a process reward model or tree search. Why deliberately keep the RL recipe that simple?

#### Evaluation and Observability

- Kimi K2 targets agentic and coding tasks. How would you evaluate whether an agentic model is actually good, beyond a single benchmark number?
  - Answer: [AI Agent Evaluation](https://outcomeschool.com/blog/ai-agent-evaluation)

### Zhipu AI (GLM)

> **Roles this covers:** Research Engineer, Agent Engineer, RL Infrastructure Engineer, Applied AI Engineer.
>
> **Interview loop, as publicly reported:** Architecture and post-training depth, an RL-infrastructure design round, a GUI-agent design round, and an implementation round in PyTorch.
>
> **Also prepare:** the [common questions](#common-questions-asked-across-companies) tagged Zhipu AI under [LLM Internals and Architecture](#llm-internals-and-architecture), [Fine-Tuning, Post-Training and Alignment](#fine-tuning-post-training-and-alignment), [Evaluation and Observability](#evaluation-and-observability).

#### LLM Internals and Architecture

- GLM's original pre-training objective is autoregressive blank infilling. How does it differ from BERT and GPT, and why did the team argue it unifies understanding and generation?
  - Answer: [Encoder vs Decoder in Transformers](https://outcomeschool.com/blog/encoder-vs-decoder-in-transformers)
- GLM-4.5 is an MoE with 355B total but 32B active parameters. Explain the economics: what does that split buy you and what does it cost?
  - Answer: [Mixture of Experts Explained](https://outcomeschool.com/blog/mixture-of-experts)
- Implement a top-k MoE router in PyTorch. Then contrast auxiliary-loss load balancing with a loss-free approach.
  - Answer: [Mixture of Experts Explained](https://outcomeschool.com/blog/mixture-of-experts)
- What is Multi-Token Prediction (MTP), why add an MTP layer, and how does it help at inference time?
- GLM has been bilingual Chinese/English since GLM-130B. What changes in tokenization, data and evaluation when a model must serve both languages well?

#### Agents and Tool Use

- AutoGLM and CogAgent operate real GUIs from screenshots over tens of steps. Design the agent: perception, action space, and error recovery for a 50-step task.
  - Answer: [How do Computer-Use Agents work?](https://outcomeschool.com/blog/how-do-computer-use-agents-work)

#### Fine-Tuning, Post-Training and Alignment

- GLM-4.5 is a hybrid reasoning model with a thinking mode and a direct-response mode. How do you build one model that does both, and what are the training and serving implications?
  - Answer: [Large Reasoning Models (LRMs)](https://outcomeschool.com/blog/large-reasoning-models) and [DeepSeek-V4 Architecture Explained](https://outcomeschool.com/blog/decoding-deepseek-v4)
- Why does long-horizon agentic RL need a disaggregated, asynchronous design (as in the slime framework) rather than colocated-synchronous?
- GLM-4.5's post-training trains expert models per domain then unifies with self-distillation. Walk through why you would train specialists and then merge them.
  - Answer: [DeepSeek-V4 Architecture Explained](https://outcomeschool.com/blog/decoding-deepseek-v4) and [How does Knowledge Distillation work?](https://outcomeschool.com/blog/how-does-knowledge-distillation-work)

#### AI System Design

- Design AutoGLM end to end: a cloud service letting users delegate multi-step phone tasks (“order my usual coffee”) to an autonomous agent. Architecture and failure modes.
  - Answer: [How do Computer-Use Agents work?](https://outcomeschool.com/blog/how-do-computer-use-agents-work)

#### Evaluation and Observability

- How would you evaluate an agentic coding model on SWE-bench and τ-bench style benchmarks without fooling yourself?
  - Answer: [AI Agent Evaluation](https://outcomeschool.com/blog/ai-agent-evaluation)

### Alibaba (Qwen)

> **Roles this covers:** Algorithm Engineer (LLM), Research Engineer, Inference Engineer, Multimodal Engineer, Applied AI Engineer (Alibaba Cloud / Model Studio).
>
> **Interview loop, as publicly reported:** Classic Alibaba structure: two or three technical rounds (algorithms + ML depth), a cross-examination round with a senior manager, and an HR round, with Qwen-specific architecture and multilingual questions layered on top.
>
> **Also prepare:** the [common questions](#common-questions-asked-across-companies) tagged Alibaba under [LLM Internals and Architecture](#llm-internals-and-architecture), [Fine-Tuning, Post-Training and Alignment](#fine-tuning-post-training-and-alignment), [Evaluation and Observability](#evaluation-and-observability), [Multimodal, Speech and Voice AI](#multimodal-speech-and-voice-ai), [Coding and Data Structures](#coding-and-data-structures).

#### Coding and Data Structures

- Qwen2.5-Coder trains with repository-level fill-in-the-middle using tokens like <|fim_prefix|>, <|fim_suffix|>, <|repo_name|>. Write the function that formats a repo-level FIM example, and explain why repo-level beats file-level.

#### LLM Internals and Architecture

- Qwen uses byte-level BPE with a ~151K vocabulary, augmented for multilingual coverage and with digits split into single characters. Why those choices, and what are the trade-offs?
  - Answer: [Byte Pair Encoding](https://outcomeschool.com/blog/bpe-in-llms)
- Qwen3 unifies a thinking mode and a non-thinking mode in one model with a caller-settable thinking budget. How would you train that, and how would you serve it?
  - Answer: [Large Reasoning Models (LRMs)](https://outcomeschool.com/blog/large-reasoning-models)
- Qwen ships both dense and MoE models (30B with ~3B active; 235B with ~22B active). When would you pick the 30B-A3B MoE over a 32B dense?
  - Answer: [Mixture of Experts Explained](https://outcomeschool.com/blog/mixture-of-experts)
- Qwen2.5 extends context to 128K (and ~1M for Turbo) using YaRN plus Dual Chunk Attention, mostly training-free. Explain how, and why post-hoc extension is attractive.
  - Answer: [Math Behind RoPE (Rotary Position Embedding)](https://outcomeschool.com/blog/math-behind-rope-rotary-position-embedding)

#### Fine-Tuning, Post-Training and Alignment

- Qwen3 uses strong-to-weak distillation, bootstrapping smaller models from flagship ones. How does that work and why is it cheaper?
  - Answer: [How does Knowledge Distillation work?](https://outcomeschool.com/blog/how-does-knowledge-distillation-work)
- Qwen's reasoning models train with RL using verifiable rewards on maths and code. Why is that preferred over PPO with a learned reward model for these domains?
  - Answer: [Group Relative Policy Optimization (GRPO)](https://outcomeschool.com/blog/group-relative-policy-optimization-grpo)

#### Evaluation and Observability

- Qwen ships open weights that top public leaderboards. As the release engineer, how do you make sure the benchmark numbers are trustworthy and not contaminated?
  - Answer: [LLM Evaluation](https://outcomeschool.com/blog/llm-evaluation)

#### Multimodal, Speech and Voice AI

- Qwen2.5-VL uses a native dynamic-resolution ViT with window attention and multimodal RoPE. Why native resolution instead of fixed tiling, and what does MRoPE encode?
  - Answer: [Decoding Vision Transformer (ViT)](https://outcomeschool.com/blog/decoding-vision-transformer-vit)

#### Behavioral and Culture

- Alibaba open-sources Qwen under Apache 2.0 while running a commercial cloud business. Walk me through the strategy, and tell me about an ambiguous technical decision you owned end to end.

### Sarvam AI

> **Roles this covers:** Research Engineer (LLM / speech), ML Engineer, Applied AI / Forward Deployed Engineer, Speech Engineer, Edge / Inference Engineer.
>
> **Interview loop, as publicly reported:** Research and applied rounds side by side: Indic NLP and tokenizer depth, a speech/ASR round, an implementation round, a deployment-on-constrained-hardware round, and a government/enterprise deployment scenario.
>
> **Also prepare:** the [common questions](#common-questions-asked-across-companies) tagged Sarvam AI under [LLM Internals and Architecture](#llm-internals-and-architecture), [Fine-Tuning, Post-Training and Alignment](#fine-tuning-post-training-and-alignment), [Multimodal, Speech and Voice AI](#multimodal-speech-and-voice-ai).

#### Coding and Data Structures

- Write code to measure a tokenizer's fertility across languages, and explain what you would do with the result.
  - Answer: [Byte Pair Encoding](https://outcomeschool.com/blog/bpe-in-llms)

#### LLM Internals and Architecture

- Why is tokenization the first bottleneck for Indian-language LLMs, and how does a low-fertility tokenizer change the economics?
  - Answer: [Byte Pair Encoding](https://outcomeschool.com/blog/bpe-in-llms) and [Tokenization in Large Language Models (LLMs)](https://www.youtube.com/watch?v=sK2s9I84EVI) and [Tokenization in LLMs](https://outcomeschool.com/blog/tokenization-in-llms)

#### Inference, Serving and GPU Performance

- How do you deploy a capable assistant on cost-sensitive or on-device hardware without a datacentre GPU? Walk through the efficiency toolkit.
  - Answer: [How does Model Quantization work?](https://outcomeschool.com/blog/how-does-model-quantization-work) and [Small Language Models (SLMs)](https://outcomeschool.com/blog/small-language-models-slms)

#### RAG and Retrieval

- Design cross-lingual RAG: the knowledge base is in English and Hindi, but users ask in Tamil, Telugu or transliterated Hinglish.

#### Fine-Tuning, Post-Training and Alignment

- Sarvam-M ships hybrid think/non-think modes and was post-trained with SFT then RLVR. How would you build that, and why RLVR over vanilla RLHF?
  - Answer: [Large Reasoning Models (LRMs)](https://outcomeschool.com/blog/large-reasoning-models) and [Group Relative Policy Optimization (GRPO)](https://outcomeschool.com/blog/group-relative-policy-optimization-grpo)
- A regional government wants an assistant in a low-resource language with only a few thousand sentences of clean text. How do you adapt a model to it?
  - Answer: [How does fine-tuning work?](https://outcomeschool.com/blog/how-does-fine-tuning-work) and [LoRA - Low-Rank Adaptation of LLMs](https://outcomeschool.com/blog/lora-low-rank-adaptation-of-llms)

#### AI System Design

- Design a real-time voice agent for a citizen helpline in Hindi and three regional languages, targeting sub-250 ms perceived latency over a phone line.
  - Answer: [Design a Real-Time Voice AI Agent](https://outcomeschool.com/blog/design-a-real-time-voice-ai-agent)

#### Evaluation and Observability

- How would you evaluate an Indic LLM properly? Why is running translated English benchmarks not enough?
  - Answer: [LLM Evaluation](https://outcomeschool.com/blog/llm-evaluation)

#### Multimodal, Speech and Voice AI

- Build a Voice Activity Detector from scratch. How do you make it robust for phone-quality Indian-language audio?
  - Answer: [Design a Real-Time Voice AI Agent](https://outcomeschool.com/blog/design-a-real-time-voice-ai-agent)
- Whisper transcribes Hinglish poorly, often forcing output into one language or hallucinating. Why, and how would you build an ASR that handles code-mixed speech?
- Bulbul-style TTS has to speak code-mixed, mixed-script text naturally. What are the hard parts of text normalization and prosody for Indian-language TTS?

#### Applied and Forward-Deployed Scenarios

- A state agency wants to move a paper-and-call-centre welfare-scheme service onto a multilingual assistant, on-prem for data residency. How do you scope and ship it?

## Big Tech AI Organizations

### Microsoft

> **Roles this covers:** AI Engineer, Applied Scientist, Machine Learning Engineer, Software Engineer (AI Platform / Copilot), Azure AI Solutions Architect, Principal Applied AI Engineer.
>
> **Interview loop, as publicly reported:** Recruiter screen → technical phone screen (coding + a little ML) → onsite loop of 4–5 rounds: two coding, one ML/AI depth, one AI system design or low-level design, and an as-appropriate-hire round with a senior leader. Azure AI and Copilot roles add a customer-architecture round.
>
> **Also prepare:** the [common questions](#common-questions-asked-across-companies) tagged Microsoft under [Inference, Serving and GPU Performance](#inference-serving-and-gpu-performance), [RAG and Retrieval](#rag-and-retrieval), [Agents and Tool Use](#agents-and-tool-use), [Fine-Tuning, Post-Training and Alignment](#fine-tuning-post-training-and-alignment), [Safety, Security and Responsible AI](#safety-security-and-responsible-ai), [AI System Design](#ai-system-design).

#### Coding and Data Structures

- Implement “top-k most frequent search queries” over a large query log, then tell me what breaks when the log becomes an unbounded stream across many machines.
- Low-level design: sketch the classes and interfaces for the tool-calling layer of an agent host, where tools can come from native code, an OpenAPI spec, or an MCP server.
  - Answer: [What is MCP (Model Context Protocol)?](https://outcomeschool.com/blog/what-is-mcp-model-context-protocol) and [How does Function Calling work in LLMs?](https://outcomeschool.com/blog/how-does-function-calling-work-in-llms)

#### Inference, Serving and GPU Performance

- A Copilot chat feature has a p95 budget of 3 seconds to first useful content. Where does the time go, and how do you cut it?
  - Answer: Explained in this video: [The First-Token Latency Problem in LLMs](https://www.youtube.com/watch?v=XD8DD4cEHu0) and [Prefill vs Decode: LLM Inference Optimization](https://outcomeschool.com/blog/prefill-vs-decode-llm-inference-optimization)
- Estimate the annual serving cost of adding an LLM summary feature for 100 million weekly active users, and how you'd cut it by 10x.
  - Answer: Explained in this video: [LLM Inference Optimization](https://www.youtube.com/watch?v=jV2sCj4lHYk) and [LLM Inference Optimization](https://outcomeschool.com/blog/llm-inference-optimization)

#### AI System Design

- Design a Copilot feature that answers questions over a user's work email, documents and meetings, without ever leaking content the user can't access.
- Design an agent that can take actions in a spreadsheet (“insert a pivot table of Q3 sales by region”): orchestration, tools and failure handling.

#### Evaluation and Observability

- How would you evaluate a meeting-summarisation feature before shipping it to a hundred million users?
  - Answer: [LLM Evaluation](https://outcomeschool.com/blog/llm-evaluation)

#### Safety, Security and Responsible AI

- Your Copilot summarises incoming email. An attacker emails a target user with hidden instructions addressed to the model. Walk me through the attack and your defence.
  - Answer: [Prompt Injection in LLMs](https://outcomeschool.com/blog/prompt-injection-in-llms)
- A shipped Copilot feature that summarises job applicants for recruiters is accused of working worse for some groups. How do you establish whether that's true, and what do you do about it?

#### Behavioral and Culture

- Tell me about a time a technical decision you championed turned out to be wrong. What happened, and what did you change afterward?

### Amazon (AWS)

> **Roles this covers:** Applied Scientist (I/II/III), Machine Learning Engineer, Data Scientist, Software Development Engineer (AI/ML), GenAI Specialist Solutions Architect, Applied AI Engineer (Bedrock, Q, SageMaker).
>
> **Interview loop, as publicly reported:** Online assessment or phone screen → onsite “loop” of 4–6 rounds, each anchored on Leadership Principles: two coding, one ML breadth, one ML depth / research deep-dive or ML system design, one bar-raiser. Applied Scientist loops add a research presentation.
>
> **Also prepare:** the [common questions](#common-questions-asked-across-companies) tagged Amazon under [LLM Internals and Architecture](#llm-internals-and-architecture), [Inference, Serving and GPU Performance](#inference-serving-and-gpu-performance), [AI System Design](#ai-system-design), [Coding and Data Structures](#coding-and-data-structures).

#### Coding and Data Structures

- Find the top-K most frequent items in a high-volume event stream with bounded memory.
- Divide two integers without using multiplication, division or modulo. Find the number of connected components in a graph. Check balanced parentheses.

#### ML and DL Fundamentals

- What is the closed-form solution of linear regression, and when do you use gradient descent instead?
  - Answer: [Math Behind Gradient Descent](https://outcomeschool.com/blog/math-behind-gradient-descent)
- What are the differences between L1 and L2 regularization in logistic regression?
  - Answer: [Regularization in Machine Learning: L1 vs L2](https://outcomeschool.com/blog/regularization-in-machine-learning)
- Write the loss function for logistic regression and prove it has a global minimum.
  - Answer: [Math Behind Cross-Entropy Loss](https://outcomeschool.com/blog/math-behind-cross-entropy-loss) and [Linear Regression vs Logistic Regression](https://outcomeschool.com/blog/linear-regression-vs-logistic-regression)
- How is KL divergence loss different from cross-entropy loss? And from contrastive loss?
  - Answer: [Math Behind Cross-Entropy Loss](https://outcomeschool.com/blog/math-behind-cross-entropy-loss) and [What is Contrastive Learning?](https://outcomeschool.com/blog/contrastive-learning)
- How do bagging and boosting differ? What is the computational difference between XGBoost and Random Forest?
- Explain the bias-variance trade-off, cross-validation, and the curse of dimensionality.
- How do GRU cells work, and how do they address the vanishing gradient problem? How does a BiLSTM work?
  - Answer: [Recurrent Neural Network (RNN)](https://outcomeschool.com/blog/recurrent-neural-network)
- What is Attention in machine learning models? What happens in a neural network if you remove all the hidden layers?
  - Answer: [Math behind Attention - Q, K, and V](https://outcomeschool.com/blog/math-behind-attention-qkv)
- Discuss precision, recall and F1: when would you prioritise one over the others?
  - Answer: [Precision vs Recall](https://outcomeschool.com/blog/precision-vs-recall)
- How do you handle data imbalance, collinearity, feature selection and regularization?
  - Answer: [Feature Engineering in Machine Learning](https://outcomeschool.com/blog/feature-engineering) and [Regularization in Machine Learning: L1 vs L2](https://outcomeschool.com/blog/regularization-in-machine-learning)
- Explain how you would design and evaluate an A/B test. What is a p-value and how do you interpret it here?
- What is Maximum Likelihood Estimation and how does it differ from Bayesian inference?

#### LLM Internals and Architecture

- Why did transformers displace RNNs for language modelling, and what exactly does the KV cache buy you at inference time?
  - Answer: [How do RNNs and Transformers differ?](https://outcomeschool.com/blog/how-do-rnns-and-transformers-differ) and [What is KV Cache in LLMs?](https://outcomeschool.com/blog/kv-cache-in-llms)

#### Inference, Serving and GPU Performance

- A customer's Bedrock-hosted workload costs too much. Cut inference cost dramatically without unacceptable quality loss.
  - Answer: Explained in this video: [LLM Inference Optimization](https://www.youtube.com/watch?v=jV2sCj4lHYk) and [LLM Inference Optimization](https://outcomeschool.com/blog/llm-inference-optimization)

#### Agents and Tool Use

- Design an agent that operates a web browser to complete multi-step tasks. How do you make it reliable enough to ship?
  - Answer: [How do Computer-Use Agents work?](https://outcomeschool.com/blog/how-do-computer-use-agents-work) and [How do Browser Agents work?](https://outcomeschool.com/blog/how-do-browser-agents-work)

#### AI System Design

- Design a multi-tenant inference platform that serves many foundation models to thousands of customers (Bedrock-shaped).
- How would you design a recommendation system to suggest books to users? How would you model a warehouse inventory problem?

#### Evaluation and Observability

- How would you decide an LLM-powered assistant is ready to launch to millions of customers?

#### Behavioral and Culture

- Tell me about a time you disagreed with your team's technical direction. What did you do? (Have Backbone; Disagree and Commit)
- Tell me about your most significant failure. What happened, and what did you change afterward?
- Tell me about a time you saw an opportunity to do something bigger than the initial scope. (Think Big)

### Apple

> **Roles this covers:** Machine Learning Engineer, AI/ML Research Engineer, On-device ML Engineer, Software Engineer (Apple Intelligence / Siri), Applied Scientist.
>
> **Interview loop, as publicly reported:** Recruiter screen → hiring-manager technical call → onsite of 4–6 rounds with the specific team: coding, ML depth, on-device/efficiency depth, system design, and behavioural. Secrecy means you may be interviewed for work you cannot be told about.
>
> **Also prepare:** the [common questions](#common-questions-asked-across-companies) tagged Apple under [LLM Internals and Architecture](#llm-internals-and-architecture), [Inference, Serving and GPU Performance](#inference-serving-and-gpu-performance), [Agents and Tool Use](#agents-and-tool-use), [Fine-Tuning, Post-Training and Alignment](#fine-tuning-post-training-and-alignment), [Coding and Data Structures](#coding-and-data-structures).

#### Inference, Serving and GPU Performance

- You need to run a ~3B-parameter language model on a phone with tight memory and power budgets. What changes versus serving the same model in a datacenter?
  - Answer: [Cloud vs On-Device Model Deployment](https://outcomeschool.com/blog/cloud-vs-on-device-model-deployment) and [How does Model Quantization work?](https://outcomeschool.com/blog/how-does-model-quantization-work)
- Explain post-training quantization versus quantization-aware training. What breaks when you push weights to 2–4 bits, and how do you recover quality?
  - Answer: [How does Model Quantization work?](https://outcomeschool.com/blog/how-does-model-quantization-work)
- Estimate the KV-cache memory for a 3B on-device model at 4k context, and name the levers that shrink it.
  - Answer: [What is KV Cache in LLMs?](https://outcomeschool.com/blog/kv-cache-in-llms) and [KV Cache Compression](https://outcomeschool.com/blog/kv-cache-compression)
- Time-to-first-token for your on-device feature is 1.8 s. Walk me through diagnosing and fixing it.
  - Answer: Explained in this video: [The First-Token Latency Problem in LLMs](https://www.youtube.com/watch?v=XD8DD4cEHu0)

#### Agents and Tool Use

- Your on-device model must emit valid, schema-conforming tool calls. How do you guarantee validity rather than hope for it?
  - Answer: [How does Function Calling work in LLMs?](https://outcomeschool.com/blog/how-does-function-calling-work-in-llms)

#### Fine-Tuning, Post-Training and Alignment

- You have one on-device base model but a dozen features: summarization, rewriting, reply suggestions, tone adjustment. How do you specialise without shipping a dozen models?
  - Answer: [LoRA - Low-Rank Adaptation of LLMs](https://outcomeschool.com/blog/lora-low-rank-adaptation-of-llms)
- How would you improve an on-device model using signals from user devices without collecting user content?

#### AI System Design

- Design the routing layer that decides whether a user request is handled on-device, by a first-party server model, or by a third-party model.
  - Answer: [LLM Routing](https://outcomeschool.com/blog/llm-routing) and [Cloud vs On-Device Model Deployment](https://outcomeschool.com/blog/cloud-vs-on-device-model-deployment)
- A user says “send Maya the photos from Saturday's hike.” Design the on-device path from that utterance to a structured app action with resolved parameters.
  - Answer: [How does Function Calling work in LLMs?](https://outcomeschool.com/blog/how-does-function-calling-work-in-llms)

#### Evaluation and Observability

- You're shipping notification summarization to hundreds of millions of users in 30+ locales, and you cannot log user content. Design the evaluation and regression-detection story.

#### Behavioral and Culture

- Tell me about a time you had to make progress with incomplete information: you couldn't be told the full context of what you were building.

### NVIDIA

> **Roles this covers:** Deep Learning Software Engineer (Inference / LLM Performance), CUDA Kernel Engineer, Machine Learning Engineer, Solutions Architect, Applied Scientist, TensorRT-LLM / Dynamo engineer.
>
> **Interview loop, as publicly reported:** Recruiter screen → hiring-manager technical call → onsite of 4–6 rounds: CUDA/C++ or Python coding, GPU performance and roofline reasoning, LLM inference depth, ML fundamentals, and system/solution design. Solutions Architect loops replace kernel depth with customer-scenario rounds.
>
> **Also prepare:** the [common questions](#common-questions-asked-across-companies) tagged NVIDIA under [LLM Internals and Architecture](#llm-internals-and-architecture), [Inference, Serving and GPU Performance](#inference-serving-and-gpu-performance).

#### Coding and Data Structures

- Here's a CUDA kernel that's 10x slower than expected. Without running it, what are the usual suspects, and how do you confirm each?
  - Answer: [How does a GPU work for Deep Learning?](https://outcomeschool.com/blog/how-does-a-gpu-work-for-deep-learning) and [How do CUDA Kernels work?](https://outcomeschool.com/blog/how-do-cuda-kernels-work)
- Implement the block manager for a paged KV cache: allocate, append, free, and copy-on-write prefix sharing.
  - Answer: [Paged Attention in LLMs](https://outcomeschool.com/blog/paged-attention-in-llms)
- A model runs fine in FP32 but produces garbage after conversion to FP16. Debug it.

#### ML and DL Fundamentals

- Explain strategies to combat overfitting in tree-based classification models.
- Summarize the differences and benefits of the Adam optimizer compared with other methods for neural-network image classification.
- A network confuses pugs and pit bulls and some training labels are wrong. How do you modify the model and the data?
- How do you evaluate a clustering model's effectiveness without pre-labelled groups?

#### Inference, Serving and GPU Performance

- You want to serve a 70B-parameter model on a single 80 GB GPU. Walk me through whether it fits and what single-stream tokens/sec you'd expect.
  - Answer: [How does Model Quantization work?](https://outcomeschool.com/blog/how-does-model-quantization-work) and [What is KV Cache in LLMs?](https://outcomeschool.com/blog/kv-cache-in-llms)
- What does TensorRT / TensorRT-LLM actually do to a model to make it faster, and when will it not help?
  - Answer: [How does TensorRT-LLM work?](https://outcomeschool.com/blog/how-does-tensorrt-llm-work)
- Design the parallelism strategy for serving a 405B-parameter dense model. TP, PP, EP: what goes where and why?

#### AI System Design

- Design a podcast search engine with transcript indexing. / Design a recommendation algorithm for type-ahead search.

#### Applied and Forward-Deployed Scenarios

- A customer's LLM chatbot on 8 GPUs is “too slow and too expensive.” You have one week with them. What do you do?
  - Answer: Explained in this video: [LLM Inference Optimization](https://www.youtube.com/watch?v=jV2sCj4lHYk) and [LLM Inference Optimization](https://outcomeschool.com/blog/llm-inference-optimization)

#### Behavioral and Culture

- Describe a time you dealt with conflicting priorities or stakeholder feedback. What would your current manager say about you?

### Tesla

> **Roles this covers:** AI / ML Engineer (Autopilot, Optimus), Deep Learning Engineer, Computer Vision Engineer, Data Engineer (Autopilot), Inference / Silicon software engineer.
>
> **Interview loop, as publicly reported:** Recruiter screen → hiring-manager technical call → onsite: coding (often C++/Python), deep-learning depth focused on vision and training pipelines, a data/infra round, and a hands-on debugging round. Loops are fast and heavy on practical engineering.

#### Coding and Data Structures

- Implement non-maximum suppression. Then vectorise it.
- Write an efficient ring buffer for high-rate sensor data with a fixed memory budget.

#### ML and DL Fundamentals

- How would you design the neural network architecture for multi-camera 3D object detection without lidar?
- How do you handle extreme class imbalance in rare-event detection (e.g. a child running into the road)?
- Explain how you would auto-label a fleet dataset and what quality controls you would put on it.
- How would you detect and handle distribution shift between fleet data and your training set?

#### Inference, Serving and GPU Performance

- The onboard compute budget is fixed. Walk me through quantizing and pruning a vision model without losing recall on small objects.
  - Answer: [How does Model Quantization work?](https://outcomeschool.com/blog/how-does-model-quantization-work)

#### AI System Design

- Design the data engine: fleet triggers → upload → labelling → retraining → shadow-mode validation → release.

#### Evaluation and Observability

- Disengagement rate is a weak proxy. How would you actually measure whether an autonomy release is safer than the last one?

#### Multimodal, Speech and Voice AI

- How would you fuse camera, radar and IMU inputs into a single perception stack, and where would you fuse them?

#### Behavioral and Culture

- Tell me about the most technically demanding thing you have shipped, and what you would do differently.

### Consumer-Scale ML Companies (Uber, Netflix, LinkedIn, Airbnb, Pinterest, Spotify)

> **Roles this covers:** Machine Learning Engineer, Senior/Staff MLE, Applied Scientist, ML Platform Engineer, GenAI Engineer.
>
> **Interview loop, as publicly reported:** A consistent shape across all of them: coding screen → onsite with two coding rounds, one ML system design round (the differentiator), one ML breadth/depth round, and behavioural. GenAI rounds have been added to most of these loops since 2024.
>
> **Also prepare:** the [common questions](#common-questions-asked-across-companies) tagged Consumer-Scale ML Companies under [AI System Design](#ai-system-design).

#### Coding and Data Structures

- Implement a streaming top-k with a bounded-memory sketch; implement a sliding-window rate counter.

#### ML and DL Fundamentals

- Your offline metric improved but the online A/B did not. Enumerate the reasons this happens and how you would tell them apart.
- Explain position bias in ranking data and how you would debias training.
- How do you design a feature store, and what causes training/serving skew?

#### AI System Design

- Design the ETA prediction system for a ride-hailing marketplace. What features, what model, how do you serve it in <100 ms?
- Design a personalised feed ranking system with a two-stage candidate generation and ranking architecture.
- Design a content recommendation system for a streaming catalogue, including cold-start for new titles and new users.
- Design “people you may know” / job-recommendation ranking at a professional network's scale.
- Design dynamic pricing / surge for a two-sided marketplace and describe the feedback loops that can go wrong.
- Design a visual search system: user uploads an image, you return visually similar in-catalogue items.
  - Answer: [How do Image Embeddings work?](https://outcomeschool.com/blog/how-do-image-embeddings-work)
- Design a fraud-detection system with heavy class imbalance and an adversarial opponent.
- Design an LLM-powered customer-support assistant on top of an existing help centre, with escalation to humans.

#### Evaluation and Observability

- How do you monitor a deployed ranking model for drift, and what triggers a retrain?

#### Behavioral and Culture

- Tell me about a model you shipped that made a measurable business difference, and one that did not.

## AI Infrastructure and Platform Companies

### Databricks

> **Roles this covers:** Software Engineer (ML Platform / Mosaic AI), Machine Learning Engineer, GenAI Solutions Architect, Forward Deployed / Delivery Solutions Architect, Applied AI Engineer.
>
> **Interview loop, as publicly reported:** Recruiter screen → technical screen (practical coding, often concurrency or data-heavy) → onsite: two coding rounds, a distributed-systems or Spark-internals round, a GenAI/ML design round, and a customer-scenario round for field roles.
>
> **Also prepare:** the [common questions](#common-questions-asked-across-companies) tagged Databricks under [Inference, Serving and GPU Performance](#inference-serving-and-gpu-performance), [RAG and Retrieval](#rag-and-retrieval), [Fine-Tuning, Post-Training and Alignment](#fine-tuning-post-training-and-alignment), [AI System Design](#ai-system-design).

#### Coding and Data Structures

- Implement a thread-safe batching logger: many producer threads call log(msg); a background thread flushes batches of up to 100 messages every second or when full.
- You have a stream of billions of events and need the top-K most frequent keys with bounded memory. Exact is impossible: what do you do?
- Given allowed IP ranges as CIDR blocks plus explicit deny ranges, implement is_allowed(ip) efficiently for millions of checks per second.
- A Spark job joining a 2 TB fact table to a 50 GB dimension table has one straggler task running 100x longer than the rest. Diagnose and fix it.
- A Structured Streaming job reads Kafka and writes to a Delta table. The cluster is killed mid-batch and restarts. Does the customer get duplicate rows? Explain at the level of the checkpoint and the transaction log.

#### Fine-Tuning, Post-Training and Alignment

- When would you fine-tune instead of using RAG or prompt engineering, and if you do, LoRA or full fine-tuning?
  - Answer: Explained in this video: [AI Engineering Explained: LLM, RAG, MCP, Agent, Fine-Tuning, Quantization](https://www.youtube.com/watch?v=lnfWvX66FUk) and [How does fine-tuning work?](https://outcomeschool.com/blog/how-does-fine-tuning-work)

#### Evaluation and Observability

- Take a working GenAI agent prototype to production for an enterprise. What's your checklist between demo and launch?

#### Applied and Forward-Deployed Scenarios

- A customer insists on fine-tuning an open model on their support tickets because “we want our own model.” You think RAG solves it. What do you do?
- An agent you shipped four months ago runs on a base model being deprecated in 60 days. How d