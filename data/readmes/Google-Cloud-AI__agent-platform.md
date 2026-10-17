# Agent Platform Samples

A curated list of code samples and tutorials for building agents on **Gemini Enterprise Agent Platform** (previously Vertex AI).

![AgentPlatform](AgentPlatform.png)

## 🚀 Getting Started

*   **[Onboarding Guide](https://goo.gle/agent-platform-onboard)** - A quick-start guide to accelerate your onboarding to the platform.

### [Watch the Intro Video](https://goo.gle/agent-platform-video)

[![What is Gemini Enterprise Agent Platform?](https://img.youtube.com/vi/j8qW5poBkEU/maxresdefault.jpg)](https://goo.gle/agent-platform-video)

---

## 🧠 Foundation Models
The state-of-the-art intelligence powering the entire platform.

*   **[Gemini API](https://deepmind.google/models/gemini/)** - Access Google's most capable generative ai models.
*   **[Veo (Video)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate)** - High-definition video generation and editing.
*   **[Lyria (Music)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-3)** - World-class music and audio generation.
*   **[Nano Banana (Image)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-1-flash-image)** - Fast, high-quality image generation.
*   **[Model Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/explore-models)** - Discover and deploy 150+ partner and open-weight models (including Claude).

---

## 🛠️ [Build](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build) - Turning code into agents

*   **Development Framework**
    *   **[Agent Development Kit (ADK)](https://adk.dev)** - Open-source, model-agnostic framework for building production agents.
    *   **[Agents CLI](https://goo.gle/agents-cli)** - Command-line tool for scaffolding, testing, and deploying agents.
*   **Builders & Discovery**
    *   **[Agent Studio](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/agent-studio)** - Low-code visual interface for rapid agent prototyping and deployment.
    *   **[Agent Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/agent-garden)** - Discover, customize, and deploy pre-built agent templates.
*   **Tools & Data Integration**
    *   **[Grounding](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/grounding/intro-grounding-gemini.ipynb)** - Connect models to real-world data and Google Search for factual accuracy.
    *   **[RAG Engine](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/rag-engine/intro_rag_engine.ipynb)** - Managed Retrieval-Augmented Generation for enterprise datasets.
    *   **[Agent Search (previously Vertex AI Search, Generative AI App Builder)](https://docs.cloud.google.com/generative-ai-app-builder/docs/try-enterprise-search)** - Semantic search engines tailored for your data.
    *   **[Vector Search 2.0](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/embeddings/vector-search-2-intro.ipynb)** - High-scale, low-latency managed vector database.

### 🌐 Protocols & Interoperability

Open standards to help agents communicate, perform actions, and generate interfaces.

*   **[Agent2Agent (A2A)](https://a2a-protocol.org)** - Secure protocol for multi-agent coordination and handoffs.
*   **[Model Context Protocol (MCP)](https://modelcontextprotocol.io/)** - Universal standard for connecting models to external tools.
*   **[Agent-to-UI (A2UI)](https://a2ui.org)** - Protocol for dynamic, agent-driven user interface generation.
*   **[Agent Payments Protocol (AP2)](https://ap2-protocol.org)** - Secure standard for automated financial transactions by agents.
*   **[Universal Commerce Protocol (UCP)](https://ucp.dev/)** - Unified standard for managing e-commerce and retail operations.

---

## 📈 [Scale](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale) - Reliability over time

*   **[Agent Runtime (previously Agent Engine, Reasoning Engine)](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/agent-engine/intro_agent_engine.ipynb)** - Managed platform for hosting and serving agentic code.
*   **[Agent Sessions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/sessions)** - Built-in state management for multi-turn, long-running interactions.
*   **[Agent Memory Bank](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/agent_engine/memory_bank/get_started_with_memory_bank.ipynb)** - Persistent, long-term semantic memory for personalized agent experiences.
*   **[Agent Sandbox (Code Execution)](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/agent_engine/tutorial_get_started_with_code_execution.ipynb)** - Secure, isolated environment for code execution and computer use.

---

## 🔐 [Govern](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern) - Trust as a feature

*   **[Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview)** - Central control point for authentication, authorization, and rate-limiting. (Private Preview)
*   **[Agent Identity](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/agent-identity-overview)** - Unique credentials for agentic identities.
*   **[Agent Policies](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/policies/overview)** - IAM Policies specifically for agents. (Private Preview)
*   **[Agent Registry](https://docs.cloud.google.com/agent-registry/overview)** - Enterprise catalog for managing and auditing approved tools and agents.
*   **[Model Armor](https://docs.cloud.google.com/model-armor/overview)** - Real-time protection against prompt injections, PII leaks, and toxic content.

---

## ⚙️ [Optimize](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize) - Evaluation and enhancement

*   **[Agent Evaluation](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/evaluation/create_agent_and_run_evaluation.ipynb)** - Framework for testing complex reasoning and tool-use accuracy.
*   **[Agent Simulation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/evaluate-simulated)** - Generate synthetic user interactions to stress-test agent behavior.
*   **[Agent Observability](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/observability/overview)** - Forensic visibility into agent thought processes and tool calls.
*   **[Agent Optimizer](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/optimize-agent)** - Automate the improvement of agent prompts based on failure analysis.

---

## 🪜 Tutorials & Notebooks
Deep dives into specific platform capabilities and use cases.

### Core Capabilities

*   [Intro to Gemini 3.5 Flash](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_3_5_flash.ipynb)
*   [Intro to Gemini 3.1 Flash-Lite](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_3_1_flash_lite.ipynb)
*   [Intro to Gemini 3.1 Pro](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_3_1_pro.ipynb)
*   [Intro to Batch Prediction](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/batch-prediction/intro_batch_prediction.ipynb)
*   [Intro to Code Execution](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/code-execution/intro_code_execution.ipynb)
*   [Intro to Computer Use](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/computer-use/intro_computer_use.ipynb)
*  [Intro to Agentic Vision](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/code-execution/intro_agentic_vision.ipynb)
*   [Intro to Context Caching](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/context-caching/intro_context_caching.ipynb)
*   [Intro to Live API](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/multimodal-live-api/live_api_quickstart.ipynb)

### Specialized Use Cases

*   [Intro to Supervised Fine Tuning](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/tuning/sft_gemini_summarization.ipynb)
*   [Intro to Evaluation](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/evaluation/quick_start_gen_ai_eval.ipynb)
*   [Document Processing](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/document-processing/document_processing.ipynb)
*   [Spatial Understanding](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/spatial-understanding/spatial_understanding.ipynb)
*   [YouTube Video Analysis](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/use-cases/video-analysis/youtube_video_analysis.ipynb)
*   [Intro to Prompt Attacks and Mitigation](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/responsible-ai/gemini_prompt_attacks_mitigation_examples.ipynb)
*   [Intro to LangGraph](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/orchestration/intro_langgraph_gemini.ipynb)
  
### Specialized Models

*   [Image Generation (Nano Banana)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/3-1-flash-image)
    *   [Gemini 3.1 Flash Image (Nano Banana 2 🍌)](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_3_1_flash_image_gen.ipynb)
    *   [Gemini 3 Pro Image (Nano Banana Pro 🍌)](http://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_3_image_gen.ipynb)
*   [Video Generation (Veo)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate)
    *   [Veo 3.1 Video Generation](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/vision/getting-started/veo3_video_generation.ipynb)
    *   [Veo 3.1 Advanced Controls](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/vision/getting-started/veo3_advanced_controls.ipynb)
*   [Music Generation (Lyria)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/lyria/lyria-3)
    *   [Lyria 3 Music Generation](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/audio/music/getting-started/lyria3_music_generation.ipynb)

### [Embeddings](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/embeddings) & Vector Search

*   [Getting Started with Text Embeddings + Vector Search](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/embeddings/intro-textemb-vectorsearch.ipynb)
*   [Introduction to Multimodal Embeddings](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/embeddings/intro_multimodal_embeddings.ipynb)
*   [Introduction to Vector Search 2.0](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/embeddings/vector-search-2-intro.ipynb)
*   [Hybrid Search Tutorial](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/embeddings/hybrid-search.ipynb)


---

This is not an officially supported Google product. This project is not
eligible for the [Google Open Source Software Vulnerability Rewards Program](https://bughunters.google.com/open-source-security).
