# Awesome Free AI

Free, open-source AI tools you can run yourself, with what most lists leave out: **how hard each one is to set up**, **whether you can sell what you build with it** (code *and* model license), and **what it runs on**.

Only projects that are still active make the list. Search all of them, with filters, at **[freeairepo.com](https://www.freeairepo.com)**.

_Last updated 2026-11-02._

## Contents

- [Rising this week](#rising-this-week)
- [Free alternatives to paid AI tools](#free-alternatives-to-paid-ai-tools)
- [LLMs & chat](#llms--chat)
- [Agents & automation](#agents--automation)
- [Coding assistants](#coding-assistants)
- [RAG & search](#rag--search)
- [Image generation & editing](#image-generation--editing)
- [Video](#video)
- [Voice & audio](#voice--audio)
- [Vision & OCR](#vision--ocr)
- [Training & fine-tuning](#training--fine-tuning)
- [Inference & serving](#inference--serving)
- [Dev tools & SDKs](#dev-tools--sdks)
- [Productivity apps](#productivity-apps)

## Rising this week

| Repo | What it does | Stars this week |
|---|---|---:|
| [rea](https://www.freeairepo.com/repo/morluto/rea) | Reverse engineer binaries, applications, and runtime behavior with AI agents. | +23,926 |
| [dsh-our-free-model](https://www.freeairepo.com/repo/Ebony-Vinyl/dsh-our-free-model) | Free AI model plugin for dsh, enabling access to advanced models without login or API key… | +9,839 |
| [DeepTutor](https://www.freeairepo.com/repo/HKUDS/DeepTutor) | AI tutor for personalized lifelong learning. | +8,387 |
| [VoiceStudio](https://www.freeairepo.com/repo/debpalash/VoiceStudio) | Create and use cloned voices for various tasks locally. | +7,341 |
| [elephant-goldfish-model](https://www.freeairepo.com/repo/google/elephant-goldfish-model) | AI agents for spec-driven development with deep-context and zero-context subagents. | +6,858 |
| [security-audit-skill](https://www.freeairepo.com/repo/cloudflare/security-audit-skill) | A coding-agent skill for multi-phase security audits with independently verified, machine… | +6,835 |
| [hallmark](https://www.freeairepo.com/repo/Nutlope/hallmark) | Anti-AI-slop design skill for Claude Code, Cursor, and Codex. | +6,664 |
| [claude-mem](https://www.freeairepo.com/repo/thedotmack/claude-mem) | Maintains context for AI agents across sessions. | +6,426 |
| [agent-desktop](https://www.freeairepo.com/repo/lahfir/agent-desktop) | Agent Desktop gives any agent reliable computer use on the desktop. Built with Rust, it s… | +5,816 |
| [Orkas](https://www.freeairepo.com/repo/Orkas-AI/Orkas) | Orkas manages AI agents to automate and coordinate tasks for productivity. | +5,515 |

## Free alternatives to paid AI tools

| Instead of | Try |
|---|---|
| [ChatGPT](https://www.freeairepo.com/alternatives/chatgpt) | [open-webui](https://www.freeairepo.com/repo/open-webui/open-webui), [lobehub](https://www.freeairepo.com/repo/lobehub/lobehub), [LibreChat](https://www.freeairepo.com/repo/LibreChat-AI/LibreChat) |
| [Claude](https://www.freeairepo.com/alternatives/claude) | [open-webui](https://www.freeairepo.com/repo/open-webui/open-webui), [lobehub](https://www.freeairepo.com/repo/lobehub/lobehub), [LibreChat](https://www.freeairepo.com/repo/LibreChat-AI/LibreChat) |
| [Perplexity](https://www.freeairepo.com/alternatives/perplexity) | [Vane](https://www.freeairepo.com/repo/ItzCrazyKns/Vane), [gpt-researcher](https://www.freeairepo.com/repo/assafelovic/gpt-researcher) |
| [Midjourney](https://www.freeairepo.com/alternatives/midjourney) | [ComfyUI](https://www.freeairepo.com/repo/Comfy-Org/ComfyUI), [InvokeAI](https://www.freeairepo.com/repo/invoke-ai/InvokeAI) |
| [DALL·E](https://www.freeairepo.com/alternatives/dall-e) | [ComfyUI](https://www.freeairepo.com/repo/Comfy-Org/ComfyUI), [InvokeAI](https://www.freeairepo.com/repo/invoke-ai/InvokeAI) |
| [remove.bg](https://www.freeairepo.com/alternatives/remove-bg) | [rembg](https://www.freeairepo.com/repo/danielgatis/rembg) |
| [Topaz Gigapixel](https://www.freeairepo.com/alternatives/topaz) | [upscayl](https://www.freeairepo.com/repo/upscayl/upscayl) |
| [Photoroom](https://www.freeairepo.com/alternatives/photoroom) | [rembg](https://www.freeairepo.com/repo/danielgatis/rembg), [ComfyUI](https://www.freeairepo.com/repo/Comfy-Org/ComfyUI) |
| [Runway](https://www.freeairepo.com/alternatives/runway) | [ComfyUI](https://www.freeairepo.com/repo/Comfy-Org/ComfyUI) |
| [ElevenLabs](https://www.freeairepo.com/alternatives/elevenlabs) | [GPT-SoVITS](https://www.freeairepo.com/repo/RVC-Boss/GPT-SoVITS), [fish-speech](https://www.freeairepo.com/repo/fishaudio/fish-speech) |
| [Otter.ai](https://www.freeairepo.com/alternatives/otter-ai) | [whisper](https://www.freeairepo.com/repo/openai/whisper), [whisper.cpp](https://www.freeairepo.com/repo/ggml-org/whisper.cpp), [faster-whisper](https://www.freeairepo.com/repo/SYSTRAN/faster-whisper) |
| [Wispr Flow](https://www.freeairepo.com/alternatives/wispr-flow) | [whisper.cpp](https://www.freeairepo.com/repo/ggml-org/whisper.cpp), [whisper](https://www.freeairepo.com/repo/openai/whisper) |
| [Cursor](https://www.freeairepo.com/alternatives/cursor) | [zed](https://www.freeairepo.com/repo/zed-industries/zed), [cline](https://www.freeairepo.com/repo/cline/cline), [continue](https://www.freeairepo.com/repo/continuedev/continue) |
| [GitHub Copilot](https://www.freeairepo.com/alternatives/github-copilot) | [continue](https://www.freeairepo.com/repo/continuedev/continue), [tabby](https://www.freeairepo.com/repo/TabbyML/tabby), [cline](https://www.freeairepo.com/repo/cline/cline) |
| [Devin](https://www.freeairepo.com/alternatives/devin) | [OpenHands](https://www.freeairepo.com/repo/OpenHands/OpenHands), [aider](https://www.freeairepo.com/repo/Aider-AI/aider) |
| [Lovable](https://www.freeairepo.com/alternatives/lovable) | [bolt.diy](https://www.freeairepo.com/repo/stackblitz-labs/bolt.diy) |
| [Zapier](https://www.freeairepo.com/alternatives/zapier) | [n8n](https://www.freeairepo.com/repo/n8n-io/n8n), [activepieces](https://www.freeairepo.com/repo/activepieces/activepieces), [windmill](https://www.freeairepo.com/repo/windmill-labs/windmill) |
| [ChatPDF](https://www.freeairepo.com/alternatives/chatpdf) | [anything-llm](https://www.freeairepo.com/repo/Mintplex-Labs/anything-llm) |
| [Notion AI](https://www.freeairepo.com/alternatives/notion-ai) | [AFFiNE](https://www.freeairepo.com/repo/toeverything/AFFiNE), [AppFlowy](https://www.freeairepo.com/repo/AppFlowy-IO/AppFlowy) |
| [Character.AI](https://www.freeairepo.com/alternatives/character-ai) | [SillyTavern](https://www.freeairepo.com/repo/SillyTavern/SillyTavern) |
| [Gamma](https://www.freeairepo.com/alternatives/gamma) | [presenton](https://www.freeairepo.com/repo/presenton/presenton) |
| [Manus](https://www.freeairepo.com/alternatives/manus) | [browser-use](https://www.freeairepo.com/repo/browser-use/browser-use), [OpenHands](https://www.freeairepo.com/repo/OpenHands/OpenHands) |
| [TinyFish](https://www.freeairepo.com/alternatives/tinyfish) | [browser-use](https://www.freeairepo.com/repo/browser-use/browser-use), [skyvern](https://www.freeairepo.com/repo/Skyvern-AI/skyvern), [stagehand](https://www.freeairepo.com/repo/browserbase/stagehand) |
| [Context.dev](https://www.freeairepo.com/alternatives/context-dev) | [crawl4ai](https://www.freeairepo.com/repo/unclecode/crawl4ai), [reader](https://www.freeairepo.com/repo/jina-ai/reader), [crawlee](https://www.freeairepo.com/repo/apify/crawlee) |
| [Firecrawl](https://www.freeairepo.com/alternatives/firecrawl) | [crawl4ai](https://www.freeairepo.com/repo/unclecode/crawl4ai), [reader](https://www.freeairepo.com/repo/jina-ai/reader), [Scrapegraph-ai](https://www.freeairepo.com/repo/ScrapeGraphAI/Scrapegraph-ai) |
| [Pinecone](https://www.freeairepo.com/alternatives/pinecone) | [qdrant](https://www.freeairepo.com/repo/qdrant/qdrant), [milvus](https://www.freeairepo.com/repo/milvus-io/milvus), [weaviate](https://www.freeairepo.com/repo/weaviate/weaviate) |
| [MrScraper](https://www.freeairepo.com/alternatives/mrscraper) | [Scrapegraph-ai](https://www.freeairepo.com/repo/ScrapeGraphAI/Scrapegraph-ai), [maxun](https://www.freeairepo.com/repo/getmaxun/maxun), [crawl4ai](https://www.freeairepo.com/repo/unclecode/crawl4ai) |
| [Exa](https://www.freeairepo.com/alternatives/exa) | [searxng](https://www.freeairepo.com/repo/searxng/searxng), [Vane](https://www.freeairepo.com/repo/ItzCrazyKns/Vane), [gpt-researcher](https://www.freeairepo.com/repo/assafelovic/gpt-researcher) |
| [cloro](https://www.freeairepo.com/alternatives/cloro) | [searxng](https://www.freeairepo.com/repo/searxng/searxng), [Vane](https://www.freeairepo.com/repo/ItzCrazyKns/Vane) |
| [AnyAPI](https://www.freeairepo.com/alternatives/anyapi) | [litellm](https://www.freeairepo.com/repo/BerriAI/litellm), [new-api](https://www.freeairepo.com/repo/QuantumNous/new-api), [gateway](https://www.freeairepo.com/repo/Portkey-AI/gateway) |

Pick the ones you pay for and see what you'd save: [Swap your AI bill](https://www.freeairepo.com/swap).

## LLMs & chat

| Repo | What it does | Stars | Setup | Sell what you build? | Runs on |
|---|---|---:|---|---|---|
| [openclaw](https://www.freeairepo.com/repo/openclaw/openclaw) | Runs AI assistants on your devices for personal or team use. | 394k | Easy | Yes | Mac, No GPU |
| [ollama](https://www.freeairepo.com/repo/ollama/ollama) | Get up and running with Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other mode… | 186k | Easy | Yes | Mac |
| [open-webui](https://www.freeairepo.com/repo/open-webui/open-webui) | Self-hosted AI platform for managing and integrating various language models. | 158k | Medium | Check first | No GPU |
| [OpenHands](https://www.freeairepo.com/repo/OpenHands/OpenHands) | 🙌 OpenHands: AI-Driven Development | 92k | Easy | Yes | – |
| [NextChat](https://www.freeairepo.com/repo/ChatGPTNextWeb/NextChat) | Instant AI chat assistant with GPT-5, Claude 4, Gemini 2.5, DeepSeek, and more. | 89k | Medium | Yes | Mac, No GPU |
| [unsloth](https://www.freeairepo.com/repo/unslothai/unsloth) | Run and train various AI models and agents locally. | 79k | Easy | Yes | Mac, No GPU |
| [daily_stock_analysis](https://www.freeairepo.com/repo/ZhuLinsen/daily_stock_analysis) | AI驱动的多市场股票智能分析系统，自动推送决策报告。 | 67k | Easy | Yes | – |
| [dsh-our-free-model](https://www.freeairepo.com/repo/Ebony-Vinyl/dsh-our-free-model) | Free AI model plugin for dsh, enabling access to advanced models without login or API key… | 57k | – | Yes | – |
| [textgen](https://www.freeairepo.com/repo/oobabooga/textgen) | Open-source desktop app for local LLMs. Text, vision, tool-calling, OpenAI/Anthropic-comp… | 48k | Medium | Yes, with conditions | Mac, No GPU |
| [AstrBot](https://www.freeairepo.com/repo/AstrBotDevs/AstrBot) | Build production-ready AI applications with integrated chatbots and agents. | 46k | Easy | Yes, with conditions | Mac, No GPU |
| [jan](https://www.freeairepo.com/repo/janhq/jan) | Runs local AI models for chat and task assistance. | 45k | Easy | Check first | Mac, No GPU |
| [GPT_API_free](https://www.freeairepo.com/repo/chatanywhere/GPT_API_free) | 提供免费和付费的GPT、DeepSeek等大模型API服务。 | 45k | – | Yes | – |
| [chatbox](https://www.freeairepo.com/repo/chatboxai/chatbox) | Desktop client for AI chat models like ChatGPT and Claude. | 42k | Hard | Yes, with conditions | Mac, No GPU |
| [Vane](https://www.freeairepo.com/repo/ItzCrazyKns/Vane) | Privacy-focused AI-powered answering engine with local and cloud LLM support. | 38k | Medium | Yes | No GPU |
| [khoj](https://www.freeairepo.com/repo/khoj-ai/khoj) | Self-hostable AI app for personal and enterprise use, integrating LLMs and automating res… | 38k | – | Yes, with conditions | No GPU |
| [heretic](https://www.freeairepo.com/repo/p-e-w/heretic) | Automatically removes censorship from language models. | 38k | Medium | Yes, with conditions (model) | No GPU |
| [QwenPaw](https://www.freeairepo.com/repo/agentscope-ai/QwenPaw) | AI assistant for automation, coding, and document processing. | 37k | Easy | Yes | No GPU |
| [langfuse](https://www.freeairepo.com/repo/langfuse/langfuse) | Monitor and evaluate LLM applications with Langfuse's open-source platform. | 37k | Medium | Check first | – |
| [SillyTavern](https://www.freeairepo.com/repo/SillyTavern/SillyTavern) | A powerful frontend for interacting with language models. | 35k | – | Yes, with conditions | – |
| [happy-llm](https://www.freeairepo.com/repo/datawhalechina/happy-llm) | 📚 从零开始构建大模型 | 35k | – | Check first | – |
| [mcp-for-blender](https://www.freeairepo.com/repo/ahujasid/mcp-for-blender) | Community plugin to control Blender 3D with any LLM of your choice. Not affiliated with t… | 33k | Easy | Yes | Mac |
| [self-llm](https://www.freeairepo.com/repo/datawhalechina/self-llm) | 《开源大模型食用指南》针对中国宝宝量身打造的基于Linux环境快速微调（全参数/Lora）、部署国内外开源大模型（LLM）/多模态大模型（MLLM）教程 | 33k | – | Yes | Mac |
| [xiaozhi-esp32](https://www.freeairepo.com/repo/78/xiaozhi-esp32) | Build and control AI chatbots on ESP32 devices. | 32k | – | Yes | – |
| [gitleaks](https://www.freeairepo.com/repo/gitleaks/gitleaks) | Find secrets with Gitleaks 🔑 | 31k | Easy | Yes | Mac |
| [semantic-kernel](https://www.freeairepo.com/repo/microsoft/semantic-kernel) | Build and orchestrate AI agents and multi-agent systems with a flexible SDK. | 29k | Medium | Yes | No GPU |

More in [LLMs & chat](https://www.freeairepo.com/category/llm-chat).

## Agents & automation

| Repo | What it does | Stars | Setup | Sell what you build? | Runs on |
|---|---|---:|---|---|---|
| [rea](https://www.freeairepo.com/repo/morluto/rea) | Reverse engineer binaries, applications, and runtime behavior with AI agents. | 421k | Easy | Yes | – |
| [ECC](https://www.freeairepo.com/repo/affaan-m/ECC) | Optimizes agent performance for AI development and coding. | 295k | Easy | Yes | – |
| [deepseek-harness](https://www.freeairepo.com/repo/deepseek-ai/deepseek-harness) | Build and manage AI agents with a plugin architecture. | 269k | Easy | Yes | – |
| [hermes-agent](https://www.freeairepo.com/repo/NousResearch/hermes-agent) | Self-improving AI agent that learns from experience and adapts to user needs. | 260k | Easy | Yes | Mac, No GPU |
| [n8n](https://www.freeairepo.com/repo/n8n-io/n8n) | Build and deploy AI agents and workflows with a visual canvas and custom code. | 209k | Easy | Check first | – |
| [firecrawl](https://www.freeairepo.com/repo/firecrawl/firecrawl) | Supercharge your AI agents with data from the web and beyond. Building the library for su… | 198k | Easy | Yes, with conditions | – |
| [AutoGPT](https://www.freeairepo.com/repo/Significant-Gravitas/AutoGPT) | AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission… | 188k | Medium | Check first | – |
| [ponytail](https://www.freeairepo.com/repo/DietrichGebert/ponytail) | Turns AI agents into lazy senior developers, writing minimal, test-covered code. | 182k | – | Yes | – |
| [dify](https://www.freeairepo.com/repo/langgenius/dify) | Build and deploy AI workflows and agents on a collaborative platform. | 160k | Medium | Check first | No GPU |
| [JavaGuide](https://www.freeairepo.com/repo/Snailclimb/JavaGuide) | Java 面试 & 后端通用面试指南，覆盖计算机基础、数据库、分布式、高并发、系统设计与 AI 应用开发 | 159k | – | Yes | – |
| [langflow](https://www.freeairepo.com/repo/langflow-ai/langflow) | Langflow is a powerful tool for building and deploying AI-powered agents and workflows. | 156k | Medium | Yes | Mac |
| [codex](https://www.freeairepo.com/repo/openai/codex) | Lightweight coding agent that runs in your terminal | 133k | Easy | Yes | Mac |
| [browser-use](https://www.freeairepo.com/repo/browser-use/browser-use) | Run AI browser agents locally or on Browser Use Cloud. | 120k | – | Yes | – |
| [TradingAgents](https://www.freeairepo.com/repo/TauricResearch/TradingAgents) | Build and manage multi-agent financial trading systems using LLMs. | 120k | Hard | Yes | – |
| [paperclip](https://www.freeairepo.com/repo/paperclipai/paperclip) | Orchestrates AI agents for business tasks and goals. | 110k | Easy | Yes | No GPU |
| [gemini-cli](https://www.freeairepo.com/repo/google-gemini/gemini-cli) | Brings Gemini AI directly into your terminal for coding and automation. | 109k | Easy | Yes | No GPU |
| [taste-skill](https://www.freeairepo.com/repo/Leonxlnx/taste-skill) | Designs websites and app screens for coding agents using art direction and real images. | 108k | Easy | Yes | No GPU |
| [Agent-Reach](https://www.freeairepo.com/repo/Panniantong/Agent-Reach) | 给AI代理互联网访问能力，无需付费API，支持多个平台。 | 108k | – | Yes | – |
| [worldmonitor](https://www.freeairepo.com/repo/koala73/worldmonitor) | AI-powered global intelligence dashboard for real-time news and geopolitical monitoring. | 90k | Easy | Yes, with conditions | Mac, No GPU |
| [deer-flow](https://www.freeairepo.com/repo/bytedance/deer-flow) | Runs and orchestrates multiple AI agents for complex tasks. | 85k | Easy | Yes | No GPU |
| [lobehub](https://www.freeairepo.com/repo/lobehub/lobehub) | Manage and schedule AI agents for 24/7 operations. | 84k | Easy | Check first | – |
| [ruflo](https://www.freeairepo.com/repo/ruvnet/ruflo) | Build and manage multi-agent systems for AI workflows. | 81k | Easy | Yes | – |
| [learn-claude-code](https://www.freeairepo.com/repo/shareAI-lab/learn-claude-code) | Teaches how to build an agent harness for AI models. | 80k | Hard | Yes | – |
| [headroom](https://www.freeairepo.com/repo/headroomlabs-ai/headroom) | Compresses inputs and outputs for AI agents to optimize token usage. | 79k | Easy | Yes | No GPU |
| [Front-End-Checklist](https://www.freeairepo.com/repo/thedaviddias/Front-End-Checklist) | 🗂 The essential checklist for modern web development, for humans and AI agents | 75k | Easy | Yes | – |

More in [Agents & automation](https://www.freeairepo.com/category/agents).

## Coding assistants

| Repo | What it does | Stars | Setup | Sell what you build? | Runs on |
|---|---|---:|---|---|---|
| [opencode](https://www.freeairepo.com/repo/anomalyco/opencode) | AI coding assistant for developers. | 224k | Easy | Yes | No GPU |
| [claude-code](https://www.freeairepo.com/repo/anthropics/claude-code) | Claude Code is an agentic coding tool that lives in your terminal, understands your codeb… | 154k | Easy | Check first | Mac |
| [cc-switch](https://www.freeairepo.com/repo/farion1231/cc-switch) | Manage multiple AI providers and agents in one desktop app. | 151k | Easy | Yes | – |
| [spec-kit](https://www.freeairepo.com/repo/github/spec-kit) | AI coding assistant with structured processes and templates. | 145k | – | Yes | – |
| [ui-ux-pro-max-skill](https://www.freeairepo.com/repo/nextlevelbuilder/ui-ux-pro-max-skill) | Generates professional UI/UX design systems using AI. | 144k | Hard | Yes | – |
| [graphify](https://www.freeairepo.com/repo/Graphify-Labs/graphify) | Turn codebases into queryable knowledge graphs for AI-assisted code analysis. | 141k | Easy | Yes | Mac, No GPU |
| [caveman](https://www.freeairepo.com/repo/JuliusBrussee/caveman) | Reduces token usage in AI agent responses without altering code. | 117k | Easy | Yes | No GPU |
| [orca](https://www.freeairepo.com/repo/stablyai/orca) | Orchestrate multiple AI agents in one interface. | 113k | Easy | Yes | – |
| [agent-skills](https://www.freeairepo.com/repo/addyosmani/agent-skills) | Production-grade engineering skills for AI coding agents. | 113k | Easy | Yes | – |
| [claude-mem](https://www.freeairepo.com/repo/thedotmack/claude-mem) | Maintains context for AI agents across sessions. | 110k | Easy | Yes | – |
| [open-design](https://www.freeairepo.com/repo/nexu-io/open-design) | The 1st Collaborative AI Design Agent Workspace. Local-first and open source. Create moti… | 105k | Easy | Yes | – |
| [archify](https://www.freeairepo.com/repo/tt-a1i/archify) | Turn ideas and plans into interactive diagrams with AI agents. | 93k | Easy | Yes | – |
| [zed](https://www.freeairepo.com/repo/zed-industries/zed) | Code at the speed of thought – Zed is a high-performance, multiplayer code editor from th… | 93k | Easy | Check first | Mac |
| [Scrapling](https://www.freeairepo.com/repo/D4Vinci/Scrapling) | A Python web scraping framework for efficient data extraction. | 92k | Medium | Yes | No GPU |
| [Understand-Anything](https://www.freeairepo.com/repo/Egonex-AI/Understand-Anything) | Graphs that teach > graphs that impress. Turn any code into an interactive knowledge grap… | 90k | Easy | Yes | – |
| [crawl4ai](https://www.freeairepo.com/repo/unclecode/crawl4ai) | Converts websites into LLM-ready Markdown for AI agents and data pipelines. | 87k | Medium | Yes | No GPU |
| [rtk](https://www.freeairepo.com/repo/rtk-ai/rtk) | CLI tool for optimizing LLM token usage in development commands. | 85k | Easy | Yes | Mac, No GPU |
| [OmniRoute](https://www.freeairepo.com/repo/diegosouzapw/OmniRoute) | Never stop coding. Free MIT AI gateway: one endpoint, 375 providers (150+ free), 1,400+ m… | 84k | Easy | Yes | – |
| [OmniRoute](https://www.freeairepo.com/repo/cheaper-inference/OmniRoute) | Free AI gateway with 375 providers and 1,400+ models for cost-effective AI inference. | 84k | Easy | Yes | – |
| [career-ops](https://www.freeairepo.com/repo/career-ops-hq/career-ops) | AI job search agent that scores jobs against your CV and tailors applications. | 79k | Easy | Yes | No GPU |
| [hyperframes](https://www.freeairepo.com/repo/heygen-com/hyperframes) | Create HTML-based videos for AI agents and standalone use. | 77k | Easy | Yes | No GPU |
| [cline](https://www.freeairepo.com/repo/cline/cline) | Autonomous coding agent as an SDK, IDE extension, or CLI assistant. | 71k | Easy | Yes | Mac |
| [gpt4free](https://www.freeairepo.com/repo/xtekky/gpt4free) | A community-driven project for accessing multiple language models via APIs and GUIs. | 67k | Easy | Yes, with conditions | Mac, No GPU |
| [last30days-skill](https://www.freeairepo.com/repo/mvanhorn/last30days-skill) | AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and t… | 66k | Easy | Yes | – |
| [diagram-design](https://www.freeairepo.com/repo/cathrynlavery/diagram-design) | Editorial diagram design for Claude Code, Codex, GitHub Copilot, Cursor, Factory Droid, Q… | 64k | Easy | Yes | – |

More in [Coding assistants](https://www.freeairepo.com/category/coding).

## RAG & search

| Repo | What it does | Stars | Setup | Sell what you build? | Runs on |
|---|---|---:|---|---|---|
| [ragflow](https://www.freeairepo.com/repo/infiniflow/ragflow) | Builds context layers for LLMs using RAG and agent capabilities. | 93k | Hard | Yes | No GPU |
| [serviette](https://www.freeairepo.com/repo/pathwaycom/serviette) | A no-code RAG server that keeps answers in sync with your documents. Works with 8 vector… | 59k | Medium | Yes | – |
| [private-gpt](https://www.freeairepo.com/repo/zylon-ai/private-gpt) | Complete API layer for private AI applications on local models: RAG, skills, tools, MCP,… | 58k | Easy | Yes | Mac |
| [OpenViking](https://www.freeairepo.com/repo/volcengine/OpenViking) | Organizes AI agent knowledge as a virtual filesystem for easy navigation and management. | 41k | Easy | Yes, with conditions | No GPU |
| [LightRAG](https://www.freeairepo.com/repo/HKUDS/LightRAG) | LightRAG is a fast retrieval-augmented generation tool for large language models. | 40k | Medium | Yes | No GPU |
| [PageIndex](https://www.freeairepo.com/repo/VectifyAI/PageIndex) | Indexes and retrieves information from documents using LLM reasoning without vector datab… | 40k | Medium | Yes | No GPU |
| [graphrag](https://www.freeairepo.com/repo/microsoft/graphrag) | Enhances LLMs with graph-based context for better reasoning. | 37k | – | Yes | No GPU |
| [WeKnora](https://www.freeairepo.com/repo/Tencent/WeKnora) | Builds a knowledge base and reasoning agent from documents. | 36k | Easy | Check first | No GPU |
| [qdrant](https://www.freeairepo.com/repo/qdrant/qdrant) | Qdrant - High-performance, massive-scale Vector Database and Vector Search Engine for the… | 35k | Easy | Yes | – |
| [onyx](https://www.freeairepo.com/repo/onyx-dot-app/onyx) | Self-hosted AI platform for integrating LLMs with enterprise apps and data. | 33k | Easy | Check first | – |
| [opendataloader-pdf](https://www.freeairepo.com/repo/opendataloader-project/opendataloader-pdf) | Extracts AI-ready data from PDFs for RAG and accessibility. | 30k | Medium | Yes | No GPU |
| [FastGPT](https://www.freeairepo.com/repo/labring/FastGPT) | 提供开箱即用的AI代理构建平台，简化复杂应用开发。 | 30k | Medium | Check first | – |
| [chroma](https://www.freeairepo.com/repo/chroma-core/chroma) | Build vector databases for AI search and retrieval. | 30k | Medium | Yes | – |
| [kotaemon](https://www.freeairepo.com/repo/Cinnamon/kotaemon) | Build and use RAG-based document QA systems with a customizable UI. | 26k | Medium | Yes | No GPU |
| [pgvector](https://www.freeairepo.com/repo/pgvector/pgvector) | Open-source vector similarity search for Postgres | 24k | Easy | Check first | – |
| [localGPT](https://www.freeairepo.com/repo/PromtEngineer/localGPT) | LocalGPT privately indexes and queries documents with AI. | 22k | Hard | Yes | Mac, No GPU |
| [memvid](https://www.freeairepo.com/repo/memvid/memvid) | Provides persistent, model-agnostic memory for AI agents. | 17k | Hard | Yes | No GPU |
| [weaviate](https://www.freeairepo.com/repo/weaviate/weaviate) | Weaviate is an open-source vector database that stores both objects and vectors, allowing… | 17k | Easy | Check first | – |
| [needle](https://www.freeairepo.com/repo/cactus-compute/needle) | AI agent for mobile devices and microcontrollers, handling tool calls and structured extr… | 14k | Medium | Yes | No GPU |
| [LEANN](https://www.freeairepo.com/repo/StarTrail-org/LEANN) | Transform laptop into a powerful RAG system with 97% storage savings. | 14k | Easy | Yes | No GPU |
| [txtai](https://www.freeairepo.com/repo/neuml/txtai) | txtai is an all-in-one AI framework for semantic search and LLM workflows. | 13k | Medium | Yes | No GPU |
| [all-in-rag](https://www.freeairepo.com/repo/datawhalechina/all-in-rag) | 🔍大模型应用开发实战一：RAG 技术全栈指南，在线阅读地址：https://datawhalechina.github.io/all-in-rag/ | 13k | – | Check first | – |
| [FlagEmbedding](https://www.freeairepo.com/repo/FlagOpen/FlagEmbedding) | Build and use retrieval-augmented LLMs for search and information retrieval. | 12k | Medium | Yes | – |
| [PixelRAG](https://www.freeairepo.com/repo/StarTrail-org/PixelRAG) | Search documents by visual content, not just text. | 11k | Easy | Yes | No GPU |
| [paper-qa](https://www.freeairepo.com/repo/Future-House/paper-qa) | Generate answers from scientific documents using RAG. | 9.5k | Medium | Yes | No GPU |

More in [RAG & search](https://www.freeairepo.com/category/rag-search).

## Image generation & editing

| Repo | What it does | Stars | Setup | Sell what you build? | Runs on |
|---|---|---:|---|---|---|
| [ComfyUI](https://www.freeairepo.com/repo/Comfy-Org/ComfyUI) | The most powerful and modular diffusion model GUI, api and backend with a graph/nodes int… | 145k | – | Yes, with conditions | Mac, GPU 4 GB |
| [photocraft](https://www.freeairepo.com/repo/storytold/photocraft) | PhotoCraft: An open-source, photo editor written by scratch in pure Rust | 76k | Easy | Yes | Mac |
| [upscayl](https://www.freeairepo.com/repo/upscayl/upscayl) | 🆙 Upscayl - #1 Free and Open Source AI Image Upscaler for Linux, MacOS and Windows. | 52k | Easy | Yes, with conditions | – |
| [diffusers](https://www.freeairepo.com/repo/huggingface/diffusers) | Generate images, audio, and 3D structures using diffusion models. | 35k | Medium | Yes | – |
| [Open-Generative-AI](https://www.freeairepo.com/repo/Anil-matcha/Open-Generative-AI) | Generate AI images and videos using 600+ models without content filters. | 32k | Easy | Yes | – |
| [InvokeAI](https://www.freeairepo.com/repo/invoke-ai/InvokeAI) | Generate and refine images using Stable Diffusion models. | 29k | – | Yes | Mac, GPU 8 GB |
| [rembg](https://www.freeairepo.com/repo/danielgatis/rembg) | Remove image backgrounds using machine learning models. | 25k | Easy | Yes | No GPU |
| [HivisionIDPhotos](https://www.freeairepo.com/repo/Zeyi-Lin/HivisionIDPhotos) | 生成高质量证件照，支持多种尺寸和美颜功能。 | 22k | Medium | Yes | No GPU |
| [Wan2.2](https://www.freeairepo.com/repo/Wan-Video/Wan2.2) | Generates high-definition videos with advanced MoE architecture and aesthetic control. | 18k | Hard | Yes | GPU 16 GB |
| [DiffSynth-Studio](https://www.freeairepo.com/repo/modelscope/DiffSynth-Studio) | Generates images, videos, and audio using Diffusion models. | 13k | Hard | Yes | GPU 4 GB |
| [ian-xiaohei-illustrations](https://www.freeairepo.com/repo/helloianneo/ian-xiaohei-illustrations) | 生成中文文章的16:9手绘怪诞配图。 | 13k | Hard | Yes | – |
| [krita-ai-diffusion](https://www.freeairepo.com/repo/Acly/krita-ai-diffusion) | AI image generation and inpainting for Krita. | 11k | – | Yes, with conditions | Mac, GPU 6 GB |
| [Sana](https://www.freeairepo.com/repo/NVlabs/Sana) | Generates high-resolution images and videos using linear diffusion transformers. | 9.8k | Hard | Yes | – |
| [StabilityMatrix](https://www.freeairepo.com/repo/LykosAI/StabilityMatrix) | Manage and run Stable Diffusion models with a multi-platform UI. | 9.0k | Easy | Yes, with conditions | – |
| [modly](https://www.freeairepo.com/repo/lightningpixel/modly) | Generate 3D models from images using local AI. | 8.5k | Easy | Check first | Mac, GPU 4 GB |
| [dream-textures](https://www.freeairepo.com/repo/carson-katri/dream-textures) | Generate textures and concept art using text prompts in Blender. | 8.2k | – | Yes, with conditions | Mac, GPU 4 GB |
| [MochiDiffusion](https://www.freeairepo.com/repo/MochiDiffusion/MochiDiffusion) | Generate images locally on Mac using Core ML Stable Diffusion and FLUX.2 Klein models. | 8.0k | Easy | Yes, with conditions | Mac, No GPU |
| [stable-diffusion.cpp](https://www.freeairepo.com/repo/leejet/stable-diffusion.cpp) | A C++ library for inference of diffusion models including image generation and editing. | 7.9k | – | Yes | No GPU |
| [sygil-webui](https://www.freeairepo.com/repo/Sygil-Dev/sygil-webui) | Stable Diffusion web UI | 7.9k | – | Yes, with conditions | – |
| [Final2x](https://www.freeairepo.com/repo/EutropicAI/Final2x) | Super-resolves images for Windows, macOS, and Linux. | 7.4k | Easy | Yes | Mac, No GPU |
| [eSearch](https://www.freeairepo.com/repo/xushengfeng/eSearch) | 截屏 离线OCR 搜索翻译 以图搜图 贴图 录屏 万向滚动截屏 屏幕翻译 Screenshot Offline OCR Search Translate Search for p… | 7.4k | Easy | Yes, with conditions | – |
| [sdnext](https://www.freeairepo.com/repo/vladmandic/sdnext) | Generate and edit images and videos using AI models. | 7.4k | Hard | Yes | Mac, GPU 4 GB |
| [civitai](https://www.freeairepo.com/repo/civitai/civitai) | A platform for sharing and customizing AI-generated images. | 7.3k | Hard | Yes | – |
| [ComfyUI-WanVideoWrapper](https://www.freeairepo.com/repo/kijai/ComfyUI-WanVideoWrapper) | Wraps WanVideo models for use in ComfyUI. | 6.8k | – | Yes | – |
| [ip-as-logo-skill](https://www.freeairepo.com/repo/s1dashu/ip-as-logo-skill) | Generate simple, cute IP mascots for logos using AI agents. | 6.3k | Easy | Yes | – |

More in [Image generation & editing](https://www.freeairepo.com/category/image).

## Video

| Repo | What it does | Stars | Setup | Sell what you build? | Runs on |
|---|---|---:|---|---|---|
| [MoneyPrinterTurbo](https://www.freeairepo.com/repo/harry0703/MoneyPrinterTurbo) | 一键生成高清短视频，自动化工作流。 | 137k | Hard | Yes | – |
| [OpenMontage](https://www.freeairepo.com/repo/calesthio/OpenMontage) | Turn AI coding assistants into full video production studios. | 75k | Hard | Yes, with conditions | No GPU |
| [Pixelle-Video](https://www.freeairepo.com/repo/ATH-MaaS/Pixelle-Video) | 自动完成短视频创作，从文案到视频合成。 | 30k | Hard | Yes | Mac, No GPU |
| [hypit](https://www.freeairepo.com/repo/hypit-ai/hypit) | Automate video cloning and generation with AI agents. | 27k | Easy | Check first | – |
| [Toonflow-app](https://www.freeairepo.com/repo/HBAI-Ltd/Toonflow-app) | 开源AI工具，用于短剧、漫剧和短视频创作。 | 20k | Easy | Yes | Mac, No GPU |
| [LivePortrait](https://www.freeairepo.com/repo/KlingAIResearch/LivePortrait) | Bring portraits to life! | 19k | Hard | Check first | – |
| [video-shotcraft](https://www.freeairepo.com/repo/Vincentwei1021/video-shotcraft) | Automate creation of cinematic product videos with AI and Remotion. | 16k | Easy | Yes | – |
| [waoowaoo](https://www.freeairepo.com/repo/waooAI/waoowaoo) | AI agent for controlled film and video production. | 15k | – | Check first | – |
| [palmier-pro](https://www.freeairepo.com/repo/palmier-io/palmier-pro) | AI-powered macOS video editor with built-in generation and MCP support. | 15k | Easy | Yes, with conditions | Mac |
| [OpenCreator](https://www.freeairepo.com/repo/krillinai/OpenCreator) | Unified AI workspace for video, image, and voice creation and editing. | 14k | Easy | Yes | No GPU |
| [Concat](https://www.freeairepo.com/repo/jub0t/Concat) | The truly free, open-source, local-first, cross-platform CapCut replacement. Scriptable t… | 14k | Easy | Yes, with conditions | Mac |
| [ViMax](https://www.freeairepo.com/repo/HKUDS/ViMax) | Automates video creation from concept to final assembly. | 13k | Hard | Yes | No GPU |
| [HunyuanVideo](https://www.freeairepo.com/repo/Tencent-Hunyuan/HunyuanVideo) | HunyuanVideo: A Systematic Framework For Large Video Generation Model | 13k | Medium | Check first | – |
| [NarratoAI](https://www.freeairepo.com/repo/linyqh/NarratoAI) | 自动化影视解说和视频剪辑工具，基于大语言模型。 | 12k | Medium | Yes | Mac, No GPU |
| [lemo-opuscar](https://www.freeairepo.com/repo/lemomo-ai/lemo-opuscar) | Create films using AI-generated code and styles. | 11k | Hard | Yes | No GPU |
| [LTX-2](https://www.freeairepo.com/repo/Lightricks/LTX-2) | Generate audio-video content using the LTX-2 model. | 10k | Hard | Check first | GPU 66 GB |
| [autoclip](https://www.freeairepo.com/repo/zhouxiaoka/autoclip) | 一键将长视频剪辑成短视频并生成字幕和发布文案。 | 9.9k | Easy | Yes | Mac, No GPU |
| [dramaclaw](https://www.freeairepo.com/repo/dramaclaw/dramaclaw) | Automate video production from script to finished film using AI. | 6.9k | Easy | Check first | No GPU |
| [ArcReel](https://www.freeairepo.com/repo/ArcReel/ArcReel) | 将文本转化为角色一致、可控的短视频。 | 6.1k | Medium | Yes, with conditions | No GPU |
| [AI-Youtube-Shorts-Generator](https://www.freeairepo.com/repo/Anil-matcha/AI-Youtube-Shorts-Generator) | Generate viral YouTube Shorts from long-form videos using AI. | 5.7k | Hard | Yes | No GPU |
| [html-video](https://www.freeairepo.com/repo/nexu-io/html-video) | Turn HTML, CSS & data into animated videos with coding agents. | 4.8k | – | Yes | – |
| [FastVideo](https://www.freeairepo.com/repo/hao-ai-lab/FastVideo) | Accelerated video generation framework for real-time inference. | 4.8k | – | Yes | Mac, GPU 8 GB |
| [lingbot-world](https://www.freeairepo.com/repo/Robbyant/lingbot-world) | Generates high-fidelity video from text prompts. | 4.6k | Hard | Yes | GPU 4 GB |
| [PersonaLive](https://www.freeairepo.com/repo/GVCLab/PersonaLive) | Generates expressive portrait animations for live streaming. | 4.1k | Hard | Yes | GPU 12 GB |
| [TurboDiffusion](https://www.freeairepo.com/repo/thu-ml/TurboDiffusion) | Accelerates video generation by 100-200x using SageAttention and SLA. | 3.9k | Medium | Yes | GPU 40 GB |

More in [Video](https://www.freeairepo.com/category/video).

## Voice & audio

| Repo | What it does | Stars | Setup | Sell what you build? | Runs on |
|---|---|---:|---|---|---|
| [whisper](https://www.freeairepo.com/repo/openai/whisper) | Speech recognition model for multilingual transcription and translation. | 112k | – | Yes | Mac, GPU 8 GB |
| [VoiceStudio](https://www.freeairepo.com/repo/debpalash/VoiceStudio) | Create and use cloned voices for various tasks locally. | 98k | Easy | Yes, with conditions | Mac, No GPU |
| [ppt-master](https://www.freeairepo.com/repo/hugohe3/ppt-master) | AI generates native PowerPoint presentations from documents. | 72k | Easy | Yes | – |
| [GPT-SoVITS](https://www.freeairepo.com/repo/RVC-Boss/GPT-SoVITS) | Converts voice samples to text-to-speech models for various languages. | 65k | Hard | Yes | Mac, No GPU |
| [voicebox](https://www.freeairepo.com/repo/jamiepine/voicebox) | Local AI voice studio for voice cloning and speech generation. | 59k | Easy | Yes | Mac, No GPU |
| [whisper.cpp](https://www.freeairepo.com/repo/ggml-org/whisper.cpp) | Port of OpenAI's Whisper model in C/C++ | 55k | Medium | Yes | Mac, No GPU |
| [VoxCPM](https://www.freeairepo.com/repo/OpenBMB/VoxCPM) | Generates high-quality multilingual speech from text. | 41k | Medium | Yes | GPU 2 GB |
| [Retrieval-based-Voice-Conversion-WebUI](https://www.freeairepo.com/repo/RVC-Project/Retrieval-based-Voice-Conversion-WebUI) | WebUI for training and using retrieval-based voice conversion models. | 39k | – | Yes | No GPU |
| [fish-speech](https://www.freeairepo.com/repo/fishaudio/fish-speech) | Generate high-quality speech from text using advanced AI models. | 34k | – | Check first (model) | No GPU |
| [meetily](https://www.freeairepo.com/repo/Zackriya-Solutions/meetily) | Privacy-first AI meeting assistant for real-time transcription and summaries. | 32k | Easy | Yes | Mac, No GPU |
| [ultimatevocalremovergui](https://www.freeairepo.com/repo/Anjok07/ultimatevocalremovergui) | Remove vocals from audio files using deep neural networks. | 27k | Easy | Yes | Mac, No GPU |
| [faster-whisper](https://www.freeairepo.com/repo/SYSTRAN/faster-whisper) | Transcribes audio faster than OpenAI Whisper with CTranslate2. | 26k | Medium | Yes | GPU 2 GB |
| [whisperX](https://www.freeairepo.com/repo/m-bain/whisperX) | Automatic speech recognition with word-level timestamps and speaker diarization. | 25k | Easy | Yes | No GPU |
| [index-tts](https://www.freeairepo.com/repo/index-tts/index-tts) | Clones voices from single audio clips for text-to-speech. | 25k | Hard | Check first | No GPU |
| [CosyVoice](https://www.freeairepo.com/repo/QwenAudio/CosyVoice) | Multi-lingual large voice generation model, providing inference, training and deployment… | 24k | Medium | Yes | – |
| [buzz](https://www.freeairepo.com/repo/chidiwilliams/buzz) | Transcribes and translates audio offline using Whisper. | 22k | Easy | Yes | Mac, No GPU |
| [FunASR](https://www.freeairepo.com/repo/modelscope/FunASR) | Open-source toolkit for speech recognition and ASR deployment. | 21k | Medium | Yes | No GPU |
| [ebook2audiobook](https://www.freeairepo.com/repo/DrewThomasson/ebook2audiobook) | Convert e-books to audiobooks with text-to-speech and voice cloning. | 20k | Medium | Yes | Mac, GPU 1 GB |
| [pyvideotrans](https://www.freeairepo.com/repo/jianchang512/pyvideotrans) | Translate videos and audio, add dubbing and subtitles. | 20k | Medium | Yes, with conditions | No GPU |
| [VideoLingo](https://www.freeairepo.com/repo/Huanshere/VideoLingo) | Automated video subtitle and dubbing tool with AI translation. | 19k | Medium | Yes | Mac, No GPU |
| [Speech](https://www.freeairepo.com/repo/NVIDIA-NeMo/Speech) | A scalable generative AI framework built for researchers and developers working on Large… | 19k | Medium | Yes | – |
| [pipecat](https://www.freeairepo.com/repo/pipecat-ai/pipecat) | Build real-time voice and multimodal conversational agents. | 17k | Hard | Yes | No GPU |
| [KittenTTS](https://www.freeairepo.com/repo/KittenML/KittenTTS) | Convert text to high-quality speech using CPU or GPU. | 17k | Medium | Yes | Mac, No GPU |
| [sherpa-onnx](https://www.freeairepo.com/repo/k2-fsa/sherpa-onnx) | Local speech recognition and synthesis for various platforms and programming languages. | 16k | Easy | Yes | Mac, No GPU |
| [F5-TTS](https://www.freeairepo.com/repo/SWivid/F5-TTS) | Generates realistic speech using diffusion transformers and flow matching. | 16k | Medium | No (model) | Mac, GPU 12 GB |

More in [Voice & audio](https://www.freeairepo.com/category/voice-audio).

## Vision & OCR

| Repo | What it does | Stars | Setup | Sell what you build? | Runs on |
|---|---|---:|---|---|---|
| [Stirling-PDF](https://www.freeairepo.com/repo/Stirling-Tools/Stirling-PDF) | #1 PDF Application on GitHub that lets you edit PDFs on any device anywhere | 96k | Easy | Check first | – |
| [PaddleOCR](https://www.freeairepo.com/repo/PaddlePaddle/PaddleOCR) | Converts images and PDFs into structured data for LLMs. | 92k | – | Yes | No GPU |
| [ultralytics](https://www.freeairepo.com/repo/ultralytics/ultralytics) | Perform object detection, instance segmentation, and image classification using YOLO mode… | 63k | Medium | Yes, with conditions | No GPU |
| [yolov5](https://www.freeairepo.com/repo/ultralytics/yolov5) | Object detection, image segmentation, and image classification using PyTorch. | 58k | Medium | Yes, with conditions | No GPU |
| [supervision](https://www.freeairepo.com/repo/roboflow/supervision) | Build computer vision tools with reusable components and models. | 51k | Medium | Yes | No GPU |
| [tesseract.js](https://www.freeairepo.com/repo/naptha/tesseract.js) | Extract text from images using JavaScript. | 39k | Medium | Yes | No GPU |
| [mediapipe](https://www.freeairepo.com/repo/google-ai-edge/mediapipe) | Cross-platform ML solutions for live and streaming media processing. | 38k | – | Yes | No GPU |
| [changedetection.io](https://www.freeairepo.com/repo/dgtlmoon/changedetection.io) | Best and simplest tool for website change detection, web page monitoring, and website cha… | 35k | Easy | Yes | – |
| [vit-pytorch](https://www.freeairepo.com/repo/lucidrains/vit-pytorch) | PyTorch implementation of Vision Transformer for image classification. | 26k | Medium | Yes | No GPU |
| [MaaAssistantArknights](https://www.freeairepo.com/repo/MaaAssistantArknights/MaaAssistantArknights) | 使用图像识别技术一键完成明日方舟游戏日常任务。 | 24k | Easy | Yes, with conditions | No GPU |
| [deepface](https://www.freeairepo.com/repo/serengil/deepface) | Facial recognition and attribute analysis library for Python. | 24k | Medium | Yes | No GPU |
| [AirSim](https://www.freeairepo.com/repo/microsoft/AirSim) | Simulate and control autonomous vehicles for AI research. | 19k | – | Check first | – |
| [vision](https://www.freeairepo.com/repo/pytorch/vision) | Provides datasets, models, and transforms for computer vision tasks. | 18k | – | Yes | – |
| [cvat](https://www.freeairepo.com/repo/cvat-ai/cvat) | Open-source data annotation platform for image, video, audio, and 3D datasets. | 17k | Medium | Yes | No GPU |
| [labelme](https://www.freeairepo.com/repo/wkentaro/labelme) | Annotate images with polygons, rectangles, and more for computer vision tasks. | 16k | Medium | Yes, with conditions | Mac, No GPU |
| [Easydict](https://www.freeairepo.com/repo/tisfeng/Easydict) | 一个简洁优雅的词典翻译 macOS App。开箱即用，支持离线 OCR 识别，支持有道词典，🍎 苹果系统词典，🍎 苹果系统翻译，OpenAI，Gemini，DeepL，Goo… | 15k | Easy | Yes, with conditions | Mac |
| [Meshroom](https://www.freeairepo.com/repo/alicevision/Meshroom) | Node-based visual programming for 3D reconstruction and image processing. | 13k | – | Check first | No GPU |
| [pytorch-grad-cam](https://www.freeairepo.com/repo/jacobgil/pytorch-grad-cam) | Provides advanced methods for explaining AI model predictions in computer vision. | 13k | – | Yes | No GPU |
| [chandra](https://www.freeairepo.com/repo/datalab-to/chandra) | OCR model for complex documents and forms with layout preservation. | 13k | Medium | Yes | No GPU |
| [chineseocr_lite](https://www.freeairepo.com/repo/DayBreak-u/chineseocr_lite) | 轻量级中文 OCR 项目，支持文本检测与识别。 | 12k | Hard | Yes, with conditions | Mac, No GPU |
| [segmentation_models.pytorch](https://www.freeairepo.com/repo/qubvel-org/segmentation_models.pytorch) | Provides PyTorch models for image semantic segmentation. | 12k | Medium | Yes | No GPU |
| [X-AnyLabeling](https://www.freeairepo.com/repo/CVHub520/X-AnyLabeling) | Unified cross-platform desktop app for annotating text, images, videos, and point clouds. | 11k | Easy | Yes, with conditions | Mac, No GPU |
| [caire](https://www.freeairepo.com/repo/esimov/caire) | Content aware image resize library | 11k | Easy | Yes | Mac |
| [yolov3](https://www.freeairepo.com/repo/ultralytics/yolov3) | Real-time object detection using YOLOv3 models. | 11k | Hard | Yes, with conditions | No GPU |
| [manga-image-translator](https://www.freeairepo.com/repo/zyddnys/manga-image-translator) | Translate text in manga and images. | 11k | Medium | Yes, with conditions | No GPU |

More in [Vision & OCR](https://www.freeairepo.com/category/vision).

## Training & fine-tuning

| Repo | What it does | Stars | Setup | Sell what you build? | Runs on |
|---|---|---:|---|---|---|
| [tensorflow](https://www.freeairepo.com/repo/tensorflow/tensorflow) | Build and deploy ML applications with a comprehensive Python framework. | 201k | Medium | Yes | No GPU |
| [transformers](https://www.freeairepo.com/repo/huggingface/transformers) | Provides state-of-the-art machine learning models for text, vision, audio, and multimodal… | 168k | Medium | Yes | – |
| [pytorch](https://www.freeairepo.com/repo/pytorch/pytorch) | Provides GPU-accelerated tensor computation and dynamic neural networks for deep learning. | 105k | Medium | Check first | – |
| [MinerU](https://www.freeairepo.com/repo/opendatalab/MinerU) | Converts complex documents into LLM-ready formats for AI workflows. | 83k | Easy | Check first | No GPU |
| [LlamaFactory](https://www.freeairepo.com/repo/hiyouga/LlamaFactory) | Unified platform for fine-tuning 100+ large language models with CLI and Web UI. | 76k | Medium | Yes | No GPU |
| [OpenBB](https://www.freeairepo.com/repo/openbq-org/OpenBB) | Integrates data sources for AI copilots and research dashboards. | 75k | Easy | Check first | – |
| [docling](https://www.freeairepo.com/repo/docling-project/docling) | Converts various document formats into structured data for AI processing. | 70k | Medium | Yes | Mac, No GPU |
| [scikit-learn](https://www.freeairepo.com/repo/scikit-learn/scikit-learn) | Machine learning library for Python. | 68k | – | Yes | No GPU |
| [keras](https://www.freeairepo.com/repo/keras-team/keras) | Build and train deep learning models easily with Keras 3. | 64k | Medium | Yes | – |
| [meilisearch](https://www.freeairepo.com/repo/meilisearch/meilisearch) | A fast, AI-powered search engine for full-text and semantic queries. | 60k | Easy | Check first | – |
| [paperless-ngx](https://www.freeairepo.com/repo/paperless-ngx/paperless-ngx) | Transform physical documents into searchable digital archives. | 48k | – | Yes, with conditions | No GPU |
| [milvus](https://www.freeairepo.com/repo/milvus-io/milvus) | Efficiently organizes and searches large-scale vector data for AI applications. | 47k | Medium | Yes | No GPU |
| [photoprism](https://www.freeairepo.com/repo/photoprism/photoprism) | AI-powered photo and video organization and search. | 40k | – | Check first | Mac, No GPU |
| [PDFMathTranslate](https://www.freeairepo.com/repo/PDFMathTranslate/PDFMathTranslate) | Translate scientific PDF documents while preserving layout and formulas. | 38k | Medium | Yes, with conditions | Mac, No GPU |
| [pytorch-image-models](https://www.freeairepo.com/repo/huggingface/pytorch-image-models) | A collection of PyTorch image models for training and inference. | 37k | – | Yes | – |
| [timesfm](https://www.freeairepo.com/repo/google-research/timesfm) | Time-series forecasting model for multivariate and univariate data. | 35k | Medium | No (model) | – |
| [spaCy](https://www.freeairepo.com/repo/explosion/spaCy) | Advanced NLP library for Python with neural network models and pipelines. | 34k | Medium | Yes | No GPU |
| [pytorch-lightning](https://www.freeairepo.com/repo/Lightning-AI/pytorch-lightning) | Scales AI model training across GPUs with minimal code changes. | 31k | Medium | Yes | – |
| [xgboost](https://www.freeairepo.com/repo/dmlc/xgboost) | A fast and flexible gradient boosting library for machine learning. | 29k | – | Yes | – |
| [label-studio](https://www.freeairepo.com/repo/HumanSignal/label-studio) | Label data for machine learning models with a user-friendly UI. | 29k | Medium | Yes | No GPU |
| [open-r1](https://www.freeairepo.com/repo/huggingface/open-r1) | Reproduce and extend the R1 pipeline for training and evaluating language models. | 26k | Hard | Yes | No GPU |
| [verl](https://www.freeairepo.com/repo/verl-project/verl) | verl/HybridFlow: A Flexible and Efficient RL Post-Training Framework | 24k | – | Yes | – |
| [unilm](https://www.freeairepo.com/repo/microsoft/unilm) | Research and development of large-scale pre-trained models for NLP, vision, speech, and m… | 22k | – | Yes | – |
| [datasets](https://www.freeairepo.com/repo/huggingface/datasets) | Download and preprocess datasets for AI models easily. | 22k | Medium | Yes | – |
| [peft](https://www.freeairepo.com/repo/huggingface/peft) | Efficiently fine-tune large language models with parameter-efficient methods. | 22k | Medium | Yes | No GPU |

More in [Training & fine-tuning](https://www.freeairepo.com/category/data-ml).

## Inference & serving

| Repo | What it does | Stars | Setup | Sell what you build? | Runs on |
|---|---|---:|---|---|---|
| [llama.cpp](https://www.freeairepo.com/repo/ggml-org/llama.cpp) | LLM inference in C/C++ | 133k | Easy | Yes | – |
| [vllm](https://www.freeairepo.com/repo/vllm-project/vllm) | High-throughput inference engine for LLMs. | 96k | Medium | Yes | No GPU |
| [netdata](https://www.freeairepo.com/repo/netdata/netdata) | The fastest path to AI-powered full stack observability, even for lean teams. | 81k | Easy | Yes, with conditions | – |
| [coolify](https://www.freeairepo.com/repo/coollabsio/coolify) | An open-source, self-hostable PaaS alternative to Vercel, Heroku & Netlify that lets you… | 66k | Easy | Yes | Mac |
| [kong](https://www.freeairepo.com/repo/Kong/kong) | 🦍 The API and AI Gateway | 44k | Hard | Yes | Mac |
| [ray](https://www.freeairepo.com/repo/ray-project/ray) | Distributed AI compute engine for ML and RL workloads. | 44k | – | Yes | No GPU |
| [DeepSpeed](https://www.freeairepo.com/repo/deepspeedai/DeepSpeed) | DeepSpeed is a deep learning optimization library that makes distributed training and inf… | 43k | Medium | Yes | – |
| [airllm](https://www.freeairepo.com/repo/lyogavin/airllm) | Runs large language models on low VRAM GPUs. | 42k | Medium | Yes | Mac, GPU 4 GB |
| [BitNet](https://www.freeairepo.com/repo/microsoft/BitNet) | Optimized inference framework for 1-bit LLMs on CPU and GPU. | 41k | Hard | Yes | No GPU |
| [llmfit](https://www.freeairepo.com/repo/AlexsJones/llmfit) | Automatically recommends LLM models based on hardware capabilities. | 39k | Easy | Yes | Mac, No GPU |
| [sglang](https://www.freeairepo.com/repo/sgl-project/sglang) | Serves large language and multimodal models for inference and RL. | 38k | Hard | Yes | No GPU |
| [frigate](https://www.freeairepo.com/repo/blakeblackshear/frigate) | Local NVR with AI object detection for IP cameras. | 37k | – | Yes | No GPU |
| [llamafile](https://www.freeairepo.com/repo/mozilla-ai/llamafile) | Run LLMs and speech-to-text models with a single-file executable. | 27k | – | Check first (model) | Mac, No GPU |
| [llm-action](https://www.freeairepo.com/repo/liguodongiot/llm-action) | 本项目旨在分享大模型相关技术原理以及实战经验（大模型工程化、大模型应用落地） | 25k | – | Yes | – |
| [DeepInfer](https://www.freeairepo.com/repo/deepseek-ai/DeepInfer) | High-performance inference framework for DeepSeek models. | 25k | – | Yes | – |
| [mlc-llm](https://www.freeairepo.com/repo/mlc-ai/mlc-llm) | Compile and deploy large language models on various platforms. | 23k | – | Yes | Mac, No GPU |
| [turbovec](https://www.freeairepo.com/repo/RyanCodrai/turbovec) | A fast, low-memory vector index for Python and Rust. | 17k | Medium | Yes | No GPU |
| [kubesphere](https://www.freeairepo.com/repo/kubesphere/kubesphere) | The container platform tailored for Kubernetes multi-cloud, datacenter, and edge manageme… | 17k | – | Check first | – |
| [MNN](https://www.freeairepo.com/repo/alibaba/MNN) | A high-performance inference engine for deploying LLMs and Edge AI models. | 16k | – | Yes | No GPU |
| [zvec](https://www.freeairepo.com/repo/alibaba/zvec) | A fast, in-process vector database for similarity search. | 16k | – | Yes | Mac, No GPU |
| [FreeToken](https://www.freeairepo.com/repo/FlashML-org/FreeToken) | FreeToken brings datacenter-scale model serving to your desktop. Run massive models local… | 16k | Medium | Yes | – |
| [TensorRT-LLM](https://www.freeairepo.com/repo/NVIDIA/TensorRT-LLM) | Optimizes inference for large language models on NVIDIA GPUs. | 15k | – | Check first | – |
| [llmware](https://www.freeairepo.com/repo/llmware-ai/llmware) | Builds knowledge-based local AI applications with small, specialized models. | 15k | Hard | Yes | Mac, No GPU |
| [semantica](https://www.freeairepo.com/repo/semantica-agi/semantica) | Builds context and knowledge graphs for AI systems with full decision provenance. | 14k | Medium | Yes | No GPU |
| [gpu-unlock](https://www.freeairepo.com/repo/Zagitta/gpu-unlock) | Your GeForce runs AI at half speed. This fixes it for 20/30/40 series cards. Up to 2× FP1… | 14k | Hard | Check first | – |

More in [Inference & serving](https://www.freeairepo.com/category/infra).

## Dev tools & SDKs

| Repo | What it does | Stars | Setup | Sell what you build? | Runs on |
|---|---|---:|---|---|---|
| [markitdown](https://www.freeairepo.com/repo/microsoft/markitdown) | Python tool for converting files and office documents to Markdown. | 193k | Medium | Yes | – |
| [langchain](https://www.freeairepo.com/repo/langchain-ai/langchain) | The agent engineering platform. | 149k | – | Yes | – |
| [ui](https://www.freeairepo.com/repo/shadcn-ui/ui) | Composable, accessible components with thoughtful defaults. Build your own component libr… | 127k | – | Yes | – |
| [servers](https://www.freeairepo.com/repo/modelcontextprotocol/servers) | Provides reference implementations for the Model Context Protocol (MCP) to secure LLM acc… | 92k | Easy | Check first | – |
| [litellm](https://www.freeairepo.com/repo/BerriAI/litellm) | Unified interface for calling multiple LLM providers with a single API. | 63k | Medium | Check first | No GPU |
| [new-api](https://www.freeairepo.com/repo/QuantumNous/new-api) | Centralized gateway for managing and routing AI models and services. | 51k | Medium | Yes, with conditions | – |
| [colibri](https://www.freeairepo.com/repo/JustVugg/colibri) | Runs large language models on local hardware using a tiny engine. | 46k | Hard | Yes | Mac, No GPU |
| [Fabric](https://www.freeairepo.com/repo/danielmiessler/Fabric) | Fabric is an open-source framework for augmenting humans using AI. It provides a modular… | 45k | Easy | Yes | Mac |
| [gradio](https://www.freeairepo.com/repo/gradio-app/gradio) | Build and share machine learning web apps in Python with Gradio. | 44k | Medium | Yes | No GPU |
| [curl](https://www.freeairepo.com/repo/curl/curl) | A command line tool and library for transferring data with URL syntax, supporting DICT, F… | 43k | – | Check first | – |
| [prompt-optimizer](https://www.freeairepo.com/repo/linshenkx/prompt-optimizer) | Optimizes AI prompts for better results and quality. | 40k | Easy | Check first | – |
| [quivr](https://www.freeairepo.com/repo/The-Vibe-Company/quivr) | An open-source engine that turns continuous content streams into search and monitoring. D… | 40k | Hard | Yes | Mac |
| [dspy](https://www.freeairepo.com/repo/stanfordnlp/dspy) | DSPy: The framework for programming—not prompting—language models | 39k | Medium | Yes | – |
| [dsh-desktop](https://www.freeairepo.com/repo/anywhere-labs/dsh-desktop) | 为 DeepSeek Harness (DSH) 插件生态打造的现代化桌面端解决方案。万物皆「插件」，桌面本身也是「插件」。 | 34k | Easy | Yes | Mac |
| [openai-python](https://www.freeairepo.com/repo/openai/openai-python) | The official Python library for the OpenAI API | 32k | Medium | Yes | – |
| [promptfoo](https://www.freeairepo.com/repo/promptfoo/promptfoo) | Test your prompts, agents, and RAGs. Red teaming/pentesting/vulnerability scanning for AI… | 27k | Easy | Yes | – |
| [crawlee](https://www.freeairepo.com/repo/apify/crawlee) | Crawlee—A web scraping and browser automation library for Node.js to build reliable crawl… | 26k | Easy | Yes | – |
| [kratos](https://www.freeairepo.com/repo/go-kratos/kratos) | Your ultimate Go microservices framework for the cloud-native era. | 26k | Easy | Yes | – |
| [python-sdk](https://www.freeairepo.com/repo/modelcontextprotocol/python-sdk) | Build and interact with MCP servers and clients for LLM applications. | 25k | – | Yes | – |
| [opik](https://www.freeairepo.com/repo/comet-ml/opik) | Monitor and evaluate LLM applications and AI agents with comprehensive tracing and dashbo… | 23k | Easy | Yes | – |
| [coze-studio](https://www.freeairepo.com/repo/coze-dev/coze-studio) | Develop AI agents with visual tools and low-code frameworks. | 22k | Hard | Yes | No GPU |
| [tiktoken](https://www.freeairepo.com/repo/openai/tiktoken) | tiktoken is a fast BPE tokeniser for use with OpenAI's models. | 20k | Medium | Yes | – |
| [langchainjs](https://www.freeairepo.com/repo/langchain-ai/langchainjs) | Build LLM-powered applications with a modular framework. | 18k | – | Yes | – |
| [math](https://www.freeairepo.com/repo/openai/math) | This repository contains mathematical manuscripts and supporting proof artifacts produced… | 17k | – | Yes | – |
| [dsh-desktop](https://www.freeairepo.com/repo/dataelement/dsh-desktop) | DSHDesktop：DeepSeek Harness Desktop / DeepSeek Harness 桌面版 | 17k | Easy | Yes | Mac |

More in [Dev tools & SDKs](https://www.freeairepo.com/category/dev-tools).

## Productivity apps

| Repo | What it does | Stars | Setup | Sell what you build? | Runs on |
|---|---|---:|---|---|---|
| [AppFlowy](https://www.freeairepo.com/repo/AppFlowy-IO/AppFlowy) | AI-powered collaborative workspace for project management and note-taking. | 78k | Easy | Yes, with conditions | Mac, No GPU |
| [AFFiNE](https://www.freeairepo.com/repo/toeverything/AFFiNE) | There can be more than Notion and Miro. AFFiNE(pronounced [ə‘fain]) is a next-gen knowled… | 74k | Easy | Check first | – |
| [siyuan](https://www.freeairepo.com/repo/siyuan-note/siyuan) | A privacy-first knowledge management system with AI writing and Q/A chat. | 47k | Easy | Yes, with conditions | – |
| [open-notebook](https://www.freeairepo.com/repo/lfnovo/open-notebook) | A privacy-focused, open-source alternative to Google's Notebook LM for AI-driven note-tak… | 41k | Medium | Yes | No GPU |
| [searxng](https://www.freeairepo.com/repo/searxng/searxng) | A privacy-focused metasearch engine that aggregates results from multiple sources. | 39k | – | Yes, with conditions | – |
| [nextai-translator](https://www.freeairepo.com/repo/nextai-translator/nextai-translator) | AI-powered translation and text polishing tool for multiple languages. | 25k | Easy | Yes, with conditions | Mac, No GPU |
| [nuclear](https://www.freeairepo.com/repo/nukeop/nuclear) | Streaming music player that finds free music for you | 19k | Easy | Yes, with conditions | Mac |
| [claude-obsidian](https://www.freeairepo.com/repo/AgriciDaniel/claude-obsidian) | Self-organizing AI second brain for Obsidian + Claude Code. Drop any source and Claude re… | 16k | Hard | Yes | – |
| [inbox-zero](https://www.freeairepo.com/repo/elie222/inbox-zero) | AI assistant for managing email inbox and calendar. | 13k | Easy | Check first | Mac, No GPU |
| [magic-resume](https://www.freeairepo.com/repo/JOYCEQL/magic-resume) | free online AI resume editor，the only official website is https://magicv.art | 11k | Medium | Check first | – |
| [blinko](https://www.freeairepo.com/repo/blinkospace/blinko) | AI-powered note-taking tool for capturing and organizing thoughts. | 11k | Easy | Yes, with conditions | Mac, No GPU |
| [tutanota](https://www.freeairepo.com/repo/tutao/tutanota) | Tuta is an email service with a strong focus on security and privacy that lets you encryp… | 8.1k | Easy | Yes, with conditions | – |
| [Dayflow](https://www.freeairepo.com/repo/JerryZLiu/Dayflow) | Automatically tracks work on Mac using AI for detailed time and activity journaling. | 7.4k | Easy | Yes | Mac |
| [PasteMD](https://www.freeairepo.com/repo/RICHQAQ/PasteMD) | 工具用于将Markdown和AI对话粘贴到Word、WPS和Excel中。 | 5.4k | Easy | Yes, with conditions | No GPU |
| [GEOFlow](https://www.freeairepo.com/repo/yaojingang/GEOFlow) | 开源智能运营系统，用于企业官网内容生产与多站点分发。 | 4.0k | Medium | Yes, with conditions | – |
| [surf](https://www.freeairepo.com/repo/deta/surf) | AI-powered note-taking and research tool for organizing files and webpages. | 3.6k | Easy | Yes | Mac, No GPU |
| [eidos](https://www.freeairepo.com/repo/mayneyao/eidos) | A single-file relational spreadsheet for you and your agent. | 3.2k | Easy | Yes, with conditions | Mac |
| [edgeever](https://www.freeairepo.com/repo/tianma-if/edgeever) | AI-native knowledge base and Evernote/Obsidian alternative with instant sync and native A… | 3.1k | Easy | Yes, with conditions | – |
| [dittofeed](https://www.freeairepo.com/repo/dittofeed/dittofeed) | Open-source customer engagement. Automate transactional and marketing messages across ema… | 3.0k | – | Yes | – |
| [BeeCount](https://www.freeairepo.com/repo/TNT-Likely/BeeCount) | AI驱动的开源个人财务管理应用，支持多平台同步和自建云端。 | 2.7k | – | Check first | – |
| [Ebook-Translator-Calibre-Plugin](https://www.freeairepo.com/repo/bookfere/Ebook-Translator-Calibre-Plugin) | Translate ebooks into specified languages using AI. | 2.7k | – | Yes, with conditions | – |
| [zennotes](https://www.freeairepo.com/repo/ZenNotes/zennotes) | Keyboard-first local Markdown notes with Vim motions, diagrams, and MCP integration. | 2.6k | Easy | Yes | Mac |
| [MarkFlowy](https://www.freeairepo.com/repo/drl990114/MarkFlowy) | A high-performance, cross-platform editor that supports WYSIWYG Markdown and general text… | 2.4k | Easy | Yes, with conditions | Mac |
| [obsidian-omnisearch](https://www.freeairepo.com/repo/scambier/obsidian-omnisearch) | A search engine that "just works" for Obsidian. | 2.2k | Easy | Yes, with conditions | – |
| [obsidian-textgenerator-plugin](https://www.freeairepo.com/repo/nhaouari/obsidian-textgenerator-plugin) | Text Generator is a versatile plugin for Obsidian that allows you to generate text conten… | 2.0k | Hard | Yes | – |

More in [Productivity apps](https://www.freeairepo.com/category/productivity).

## How to read the columns

- **Setup**: Easy (a desktop app or one command, about 5 minutes), Medium (Docker or a package, about 30 minutes), Hard (building from source, an hour or more).
- **Sell what you build?**: Yes, Yes with conditions, Check first or No, from the code license and the license of the model it uses. "(model)" means the model is what limits it. A guide, not legal advice.
- **Runs on**: what the project says it needs. "–" means it doesn't say.

## Missing something?

[Suggest a repo](https://www.freeairepo.com/submit) on FreeAIRepo. If it fits, it's added right away, with credit to you.

## License

This list is licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/): reuse it freely, with a link back to [FreeAIRepo](https://www.freeairepo.com).
