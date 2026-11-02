# Awesome Self-Hosted AI [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Open-source AI you can run on your own hardware or server.

308 projects across local LLMs, chat interfaces, agents, MCP servers, RAG, speech and image generation. A weekly job checks every project against the GitHub API, and anything archived, deleted or silent for over a year moves to [UNMAINTAINED.md](UNMAINTAINED.md).

**308** projects | **307** active in the last 90 days | **10.6M** combined stars | **0** unmaintained | refreshed 2026-10-31

See the [live health table](LIVE.md) for stars, last push and license per project.

## Contents

- [Agents and Automation](#agents-and-automation) (27)
- [Chat Interfaces](#chat-interfaces) (11)
- [Coding Assistants](#coding-assistants) (24)
- [Document AI and OCR](#document-ai-and-ocr) (10)
- [Fine-Tuning and Training](#finetuning-and-training) (10)
- [Home and Personal AI](#home-and-personal-ai) (13)
- [Image and Video Generation](#image-and-video-generation) (13)
- [LLM Runtimes and Inference](#llm-runtimes-and-inference) (38)
- [MCP Servers and Gateways](#mcp-servers-and-gateways) (19)
- [Model Gateways and Routers](#model-gateways-and-routers) (11)
- [Observability and Evals](#observability-and-evals) (20)
- [RAG and Vector Databases](#rag-and-vector-databases) (24)
- [Search and Knowledge](#search-and-knowledge) (13)
- [Speech and Audio](#speech-and-audio) (15)
- [Vision and Multimodal](#vision-and-multimodal) (5)
- [Voice Agents](#voice-agents) (5)
- [Rising](#rising) (25)
- [Source-Available](#source-available) (25)

## Agents and Automation

- [Agent Development Kit](https://github.com/google/adk-python) - Python toolkit for building and evaluating LLM agents, with multi-model support.
- [AgentScope](https://github.com/agentscope-ai/agentscope) - Multi-agent framework with tracing, memory and tool use for building and deploying agents.
- [Agno](https://github.com/agno-agi/agno) - Python framework for building multi-agent systems with memory, knowledge, and a runtime for agent apps.
- [Botpress](https://github.com/botpress/botpress) - Platform for building and self-hosting conversational AI chatbots and agents with a visual flow builder.
- [browser-use](https://github.com/browser-use/browser-use) - Library that lets LLM agents drive a real browser to complete web tasks.
- [CrewAI](https://github.com/crewAIInc/crewAI) - Framework for orchestrating role-based teams of AI agents inside your own Python environment.
- [Cua](https://github.com/trycua/cua) - Sandboxes, SDKs and benchmarks for running computer-use agents against desktop environments.
- [DeerFlow](https://github.com/bytedance/deer-flow) - Agent harness that coordinates subagents, sandboxed execution, and memory for long-running tasks.
- [Forge](https://github.com/antoinezambelli/forge) - Python framework for tool calling and multi-step workflows on self-hosted LLMs.
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) - Autonomous agent that runs server-side, keeps persistent memory and refines its behavior over time.
- [Julep](https://github.com/julep-ai/julep) - Server platform for stateful agent workflows with memory, tools, branching and long-running tasks.
- [Langflow](https://github.com/langflow-ai/langflow) - Visual builder for AI agents and RAG workflows in Python, with each flow exposed as an API.
- [LangGraph](https://github.com/langchain-ai/langgraph) - Library for building stateful, long-running agent workflows as graphs with checkpointing.
- [Letta](https://github.com/letta-ai/letta) - Server for stateful agents that keep long-term memory and run as persistent services.
- [mem0](https://github.com/mem0ai/mem0) - Memory layer for AI assistants that stores and retrieves user facts across sessions.
- [Microsandbox](https://github.com/superradcompany/microsandbox) - Local microVM runtime that isolates AI agent and untrusted workloads in sandboxed execution.
- [Open Interpreter](https://github.com/OpenInterpreter/open-interpreter) - Natural-language interface that lets an LLM run code and shell commands on your own computer.
- [open-multi-agent](https://github.com/open-multi-agent/open-multi-agent) - Self-hosted TypeScript agent runtime with durable approvals and verifiable run records.
- [OpenManus](https://github.com/FoundationAgents/OpenManus) - General-purpose agent framework that runs tools and a browser on your own machine.
- [OpenShell](https://github.com/NVIDIA/OpenShell) - Runtime for autonomous agents that enforces policy-driven execution boundaries, with a CLI.
- [Paperclip](https://github.com/paperclipai/paperclip) - Open-source MIT app for coordinating AI agents across projects, tasks and workflows.
- [Pydantic AI](https://github.com/pydantic/pydantic-ai) - Type-safe Python agent framework with model-agnostic tool calling and structured outputs.
- [Sim](https://github.com/simstudioai/sim) - Visual workflow builder for agents and LLM pipelines that can be self-hosted with Docker.
- [Steel Browser](https://github.com/steel-dev/steel-browser) - Open-source browser sandbox with an API that lets AI agents run web automation sessions.
- [Trigger.dev](https://github.com/triggerdotdev/trigger.dev) - TypeScript background job framework for long-running AI tasks with retries and run monitoring.
- [UI-TARS Desktop](https://github.com/bytedance/UI-TARS-desktop) - Desktop app that runs ByteDance's multimodal GUI agent to control a local computer.
- [Zep](https://github.com/getzep/zep) - Memory service that stores and retrieves facts and conversation history for AI agents over time.

## Chat Interfaces

- [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) - Self-hosted app for chatting with documents using local or cloud models and built-in RAG.
- [big-AGI](https://github.com/enricoros/big-AGI) - Multi-model chat app with personas and tools that can be self-hosted for power users.
- [Chatbox](https://github.com/chatboxai/chatbox) - Cross-platform desktop and web client for chatting with local and remote LLM APIs.
- [Cherry Studio](https://github.com/CherryHQ/cherry-studio) - Desktop client for chatting with many LLM providers, with knowledge bases and local document search.
- [HuggingChat (self-hosted)](https://github.com/huggingface/chat-ui) - Self-hostable chat web app that connects to OpenAI-compatible model endpoints.
- [Jan](https://github.com/janhq/jan) - Open-source desktop app for running local models and chatting with cloud providers.
- [LibreChat](https://github.com/danny-avila/LibreChat) - Multi-provider chat UI with plugins, file uploads, and agents that runs in Docker on your server.
- [NextChat](https://github.com/ChatGPTNextWeb/NextChat) - Lightweight web chat client for many LLM providers, deployable as a single container.
- [Perplexica](https://github.com/ItzCrazyKns/Perplexica) - AI answering search engine that cites web sources and runs with local or cloud models.
- [SillyTavern](https://github.com/SillyTavern/SillyTavern) - Customizable web frontend for chatting and roleplaying with locally hosted or remote LLMs.
- [text-generation-webui](https://github.com/oobabooga/text-generation-webui) - Gradio web UI for running local models through llama.cpp, Transformers, and ExLlama backends.

## Coding Assistants

- [AiderDesk](https://github.com/hotovo/aider-desk) - Desktop app that wraps the Aider coding assistant with a UI, agent mode and MCP support.
- [Archon](https://github.com/coleam00/Archon) - YAML-defined workflow engine that makes coding agent processes repeatable from planning to validation.
- [Claude Code Local](https://github.com/nicedreamzapp/claude-code-local) - MLX server exposing the Anthropic Messages API so the Claude Code CLI can run against local models on Apple Silicon.
- [Cline](https://github.com/cline/cline) - VS Code agent that plans and edits code using model API keys you supply.
- [Codex CLI](https://github.com/openai/codex) - Local terminal coding agent that reads, edits, and runs code inside your repository.
- [Continue](https://github.com/continuedev/continue) - IDE extension for autocomplete, chat, and agentic edits against local or hosted models.
- [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) - Plugin-based agent harness for DeepSeek models with a local Web UI.
- [DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) - Terminal coding agent built around DeepSeek models, tuned for prefix-cache stability.
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) - Open-source terminal agent for coding and shell tasks, built on Google Gemini models.
- [goose](https://github.com/block/goose) - On-machine coding agent that runs shell, file, and extension tools with any supported model.
- [Goose](https://github.com/aaif-goose/goose) - On-machine development agent that edits files and runs tasks, with extensible tool support.
- [gptme](https://github.com/gptme/gptme) - Terminal agent with local tools that writes code, runs shell commands and browses the web.
- [jcode](https://github.com/1jehuang/jcode) - Rust coding agent harness built for running many agent sessions at once.
- [Kilo Code](https://github.com/Kilo-Org/kilocode) - Open-source coding agent for VS Code and the terminal, with bring-your-own model keys.
- [Mistral Vibe](https://github.com/mistralai/mistral-vibe) - Lightweight command-line coding agent from Mistral for local development workflows.
- [Open Code Review](https://github.com/alibaba/open-code-review) - Code review CLI that combines deterministic analysis passes with LLM agents.
- [OpenCode](https://github.com/anomalyco/opencode) - Terminal-native autonomous coding agent for editing and running code from the command line.
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) - Platform for AI software agents that edit code, run commands, and browse inside a sandbox.
- [Pi](https://github.com/earendil-works/pi) - Modular terminal coding agent toolkit with a unified model layer and TUI and web front ends.
- [PR-Agent (Qodo)](https://github.com/qodo-ai/pr-agent) - AI pull request reviewer that runs on GitHub, GitLab, Bitbucket, and Azure DevOps.
- [Qwen Code](https://github.com/QwenLM/qwen-code) - Terminal coding agent tuned for Qwen models and compatible with other OpenAI-style APIs.
- [screenshot-to-code](https://github.com/abi/screenshot-to-code) - Turns screenshots, mockups, and Figma designs into frontend code using vision-language models.
- [SWE-agent](https://github.com/SWE-agent/SWE-agent) - Software engineering agent that resolves GitHub issues by editing code and running commands in a container.
- [T3 Code](https://github.com/pingdotgg/t3code) - Minimal web and desktop GUI for driving coding agents such as Codex and Claude Code.

## Document AI and OCR

- [Docling](https://github.com/docling-project/docling) - Parses PDF, DOCX, PPTX and HTML into structured Markdown or JSON, with OCR and table recovery.
- [GLM-OCR](https://github.com/zai-org/GLM-OCR) - Open OCR model and code from Z.ai for text, table and formula recognition in document images.
- [kordoc](https://github.com/chrisryugj/kordoc) - Converts HWP, HWPX, PDF and Office files to Markdown, with a CLI and an MCP server.
- [LiteParse](https://github.com/run-llama/liteparse) - Fast, local, model-free document parser for extracting text and layout from documents.
- [Marker](https://github.com/datalab-to/marker) - Converts PDFs and other documents to Markdown, with table extraction and optional LLM cleanup.
- [MarkItDown (Microsoft)](https://github.com/microsoft/markitdown) - Command-line and Python tool that converts Office files, PDFs, and images into Markdown.
- [OpenContracts](https://github.com/Open-Source-Legal/OpenContracts) - Self-hosted platform for annotating legal documents with semantic search and contract analysis.
- [OpenMed](https://github.com/maziyarpanahi/openmed) - Local-first healthcare app for de-identifying clinical text and extracting medical entities.
- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) - OCR toolkit with text detection, recognition, and layout analysis that can run as a local service.
- [Unstructured](https://github.com/Unstructured-IO/unstructured) - ETL toolkit and API that parses complex documents into structured elements for language model pipelines.

## Fine-Tuning and Training

- [Axolotl](https://github.com/axolotl-ai-cloud/axolotl) - Config-driven toolkit for full and LoRA fine-tuning and preference training on your own GPUs.
- [H2O LLM Studio](https://github.com/h2oai/h2o-llmstudio) - No-code GUI for fine-tuning LLMs with supervised training and reward modeling.
- [LLaMA-Factory](https://github.com/hiyouga/LlamaFactory) - Unified framework for fine-tuning 100+ LLMs and VLMs with LoRA, QLoRA and RLHF methods.
- [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) - Web UI and CLI for fine-tuning LLMs with SFT, DPO, ORPO and KTO.
- [MergeKit](https://github.com/arcee-ai/mergekit) - Command-line tools for merging pretrained language models using configurable merge recipes.
- [nnU-Net](https://github.com/MIC-DKFZ/nnUNet) - Command-line segmentation pipeline that configures and trains its own model for a medical imaging dataset.
- [OneTrainer](https://github.com/Nerogar/OneTrainer) - GUI application for training diffusion image models such as SD 1.5, SDXL and FLUX.
- [Oumi](https://github.com/oumi-ai/oumi) - Open platform with a CLI for fine-tuning, evaluating and deploying open LLMs and vision-language models.
- [Soup](https://github.com/MakazhanAlpamys/Soup) - Fine-tunes LLMs from one YAML file, with layer streaming for GPUs with limited memory.
- [TRL](https://github.com/huggingface/trl) - Library for post-training language models with SFT, DPO and GRPO on top of Transformers.

## Home and Personal AI

- [AI Novel Writer](https://github.com/EthanYoQ/AI-Novel-Writer) - Local-first desktop workbench for drafting long fiction with characters, worldbuilding and chapter plans.
- [AionsHome](https://github.com/death34018-hue/AionsHome) - Self-hosted AI companion with long-term memory, voice interaction and camera-based vision.
- [AIRI](https://github.com/moeru-ai/airi) - Self-hosted AI companion platform with Live2D characters and real-time voice conversation.
- [AstrBot](https://github.com/AstrBotDevs/AstrBot) - Agent framework and bot server that connects LLMs to many messaging platforms.
- [DeepTutor](https://github.com/HKUDS/DeepTutor) - Multi-agent tutoring system that adapts lessons to a learner through interactive workflows.
- [Home Assistant](https://github.com/home-assistant/core) - Home automation platform with local voice assistants and LLM conversation agents.
- [Khoj](https://github.com/khoj-ai/khoj) - Self-hostable personal assistant for chat, search, and automations over your notes and documents.
- [llmfit](https://github.com/AlexsJones/llmfit) - Terminal tool that scores which local models fit your CPU, GPU and RAM before you download them.
- [nanobot](https://github.com/HKUDS/nanobot) - Lightweight personal AI agent with a built-in web UI, model routing, MCP support, and chat channels.
- [Octop](https://github.com/TencentCloud/Octop) - Self-hosted AI assistant for several users, running multiple agents side by side.
- [OGAM](https://github.com/off-grid-ai/OGAM) - Offline AI app for phone and Mac that chats, sees, speaks and generates images with local models.
- [OpenClaw](https://github.com/openclaw/openclaw) - Local-first personal AI assistant that links chat channels to agents running on your own machine.
- [RuView](https://github.com/ruvnet/RuView) - Software and firmware that senses presence, pose and vitals from commodity WiFi signals without video.

## Image and Video Generation

- [AI Toolkit](https://github.com/ostris/ai-toolkit) - Scripts and UI for training LoRAs and fine-tunes on diffusion and video models.
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - Node-based interface and engine for running diffusion image and video pipelines locally.
- [ComfyUI](https://github.com/Comfy-Org/ComfyUI) - Node-based editor and server for building and running diffusion image and video workflows locally.
- [DiffSynth-Studio](https://github.com/modelscope/DiffSynth-Studio) - Diffusion engine for image and video generation with memory-optimized local inference.
- [Diffusers](https://github.com/huggingface/diffusers) - Library of diffusion pipelines and schedulers for image, video, and audio generation in PyTorch.
- [InvokeAI](https://github.com/invoke-ai/InvokeAI) - Creative image generation studio with a browser UI, canvas editing, and model management.
- [iris.c](https://github.com/antirez/iris.c) - Pure C inference engine for the FLUX.2 image generation model.
- [Mochi](https://github.com/genmoai/mochi) - Open text-to-video model released with inference code for running on local GPUs.
- [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) - Pipeline that produces short videos from a topic, covering script, footage, and voiceover.
- [MOSS-Image](https://github.com/OpenMOSS/MOSS-Image) - Official code for MOSS-Image, a 5B-parameter diffusion transformer for high-quality image generation.
- [sd-scripts](https://github.com/kohya-ss/sd-scripts) - Training and fine-tuning scripts for Stable Diffusion and related image models.
- [SD.Next](https://github.com/vladmandic/sdnext) - WebUI for image and video generation with many diffusion models and multiple hardware backends.
- [stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp) - C/C++ inference for Stable Diffusion, FLUX and other image models, with no Python stack required.

## LLM Runtimes and Inference

- [Aphrodite Engine](https://github.com/aphrodite-engine/aphrodite-engine) - Large-scale LLM inference engine with a REST API and LoRA support, forked from vLLM.
- [Colibri](https://github.com/JustVugg/colibri) - Zero-dependency C engine that runs large mixture-of-experts models locally by streaming experts from disk.
- [distributed-llama](https://github.com/b4rtaz/distributed-llama) - Runs one LLM across several home devices over the network, so adding machines speeds up inference.
- [ds4](https://github.com/antirez/ds4) - Native local inference engine for DeepSeek 4 Flash and Pro models on Metal, CUDA and ROCm GPUs.
- [ExecuTorch](https://github.com/pytorch/executorch) - PyTorch runtime and toolchain for deploying models to mobile, embedded and edge hardware.
- [ExLlamaV3](https://github.com/turboderp-org/exllamav3) - Inference library for running quantized LLMs efficiently on consumer NVIDIA GPUs.
- [exo](https://github.com/exo-explore/exo) - Peer-to-peer system that pools devices on a local network to run one larger model.
- [gemma.cpp](https://github.com/google/gemma.cpp) - Lightweight standalone C++ engine for running Google Gemma models locally.
- [GPUStack](https://github.com/gpustack/gpustack) - GPU cluster manager that places and runs model servers such as vLLM and SGLang across your machines.
- [ik_llama.cpp](https://github.com/ikawrakow/ik_llama.cpp) - Llama.cpp fork with extra state-of-the-art quantization types and faster hybrid GPU and CPU inference.
- [KTransformers](https://github.com/kvcache-ai/ktransformers) - Inference framework that offloads MoE experts to the CPU so large models fit on modest GPUs.
- [Lemonade](https://github.com/lemonade-sdk/lemonade) - Local LLM server with an OpenAI-compatible API that uses GPU and NPU acceleration.
- [Llama Stack](https://github.com/meta-llama/llama-stack) - Server with unified APIs for inference, RAG, agents, and safety that runs Llama and other models.
- [llama-swap](https://github.com/mostlygeek/llama-swap) - Lightweight proxy that swaps between llama.cpp, vLLM, and other model servers per request.
- [llama.cpp](https://github.com/ggml-org/llama.cpp) - C and C++ inference engine for running GGUF models on CPUs and GPUs across many backends.
- [llamafile](https://github.com/mozilla-ai/llamafile) - Single-file executables that bundle a model with llama.cpp so it runs locally on most computers.
- [llm-d](https://github.com/llm-d/llm-d) - Kubernetes-native framework for distributed LLM inference that spreads serving across cluster nodes.
- [LMDeploy](https://github.com/InternLM/lmdeploy) - Toolkit for quantizing, deploying and serving LLMs, with 4-bit inference and an API server.
- [LocalAI](https://github.com/mudler/LocalAI) - OpenAI-compatible server that runs text, image, and audio models on local hardware.
- [Magnitude](https://github.com/magnitudedev/magnitude) - Inference engine that tunes kernels on your own hardware to find the fastest way to run each model.
- [mistral.rs](https://github.com/EricLBuehler/mistral.rs) - Rust LLM inference engine with an OpenAI-compatible server and quantization support.
- [MLC LLM](https://github.com/mlc-ai/mlc-llm) - Compiler-based LLM deployment that runs models natively on phones, browsers, and desktop GPUs.
- [mlx-lm](https://github.com/ml-explore/mlx-lm) - Run and fine-tune language models on Apple silicon with the MLX framework.
- [MNN](https://github.com/alibaba/MNN) - Lightweight inference runtime from Alibaba for running and training neural networks on devices.
- [ninfer](https://github.com/Neroued/ninfer) - Single-GPU inference engine for selected model checkpoints and GPUs, with a CLI and server.
- [NVIDIA Dynamo](https://github.com/ai-dynamo/dynamo) - NVIDIA datacenter-scale distributed inference server that orchestrates engines such as vLLM and SGLang.
- [Ollama](https://github.com/ollama/ollama) - Local model runner with a CLI and HTTP API for pulling and serving open-weight LLMs.
- [omlx](https://github.com/jundot/omlx) - Local LLM server for Apple Silicon that batches requests, caches to SSD, and runs from the macOS menu bar.
- [RamaLama](https://github.com/containers/ramalama) - Developer CLI that serves local models inside containers, detecting the GPU and pulling a matching image.
- [SGLang](https://github.com/sgl-project/sglang) - Serving framework for LLMs and multimodal models with structured generation and prefix caching.
- [shimmy](https://github.com/Michael-A-Kuykendall/shimmy) - Single-binary Rust inference server with an OpenAI-compatible API for GGUF and SafeTensors models.
- [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) - An open inference backend and runtime for serving LLMs efficiently on NVIDIA GPUs.
- [Text Embeddings Inference (Hugging Face)](https://github.com/huggingface/text-embeddings-inference) - Inference server for embedding, reranking, and classification models with token-based batching.
- [Triton Inference Server](https://github.com/triton-inference-server/server) - Model server that runs models from many frameworks on GPUs and CPUs with dynamic batching.
- [Unsloth](https://github.com/unslothai/unsloth) - Training toolkit that speeds up LoRA and full fine-tuning of open LLMs on your own GPUs.
- [vLLM](https://github.com/vllm-project/vllm) - High-throughput LLM serving engine with paged attention and an OpenAI-compatible server.
- [vLLM Production Stack](https://github.com/vllm-project/production-stack) - Kubernetes deployment stack for vLLM that adds automated scaling and monitoring around the engine.
- [Xinference](https://github.com/xorbitsai/inference) - Model serving platform that exposes LLM, embedding, and speech models through one API.

## MCP Servers and Gateways

- [agentgateway](https://github.com/agentgateway/agentgateway) - Rust proxy for agent traffic that supports MCP and A2A protocols.
- [AI Memory](https://github.com/akitaonrails/ai-memory) - Rust memory server and MCP client that gives coding CLIs long-term recall with full-text search.
- [AnythingMCP](https://github.com/HelpCode-ai/anythingmcp) - Turns REST, GraphQL, SOAP and SQL APIs into MCP tools behind one gateway.
- [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) - MCP server that lets coding agents control and inspect a local Chrome instance via DevTools.
- [cocoindex-code](https://github.com/cocoindex-io/cocoindex-code) - Local AST-aware code search CLI and MCP server backed by an embedded SQLite index.
- [codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) - C-based MCP server that indexes repositories into local type-resolved knowledge graphs.
- [DesktopCommander MCP](https://github.com/wonderwhy-er/DesktopCommanderMCP) - MCP server that gives AI clients terminal control, file search, and diff-based file editing.
- [Docker MCP Gateway](https://github.com/docker/mcp-gateway) - Runs MCP servers in isolated containers and exposes them to clients through one gateway.
- [FastMCP](https://github.com/PrefectHQ/fastmcp) - Pythonic framework for building MCP servers and clients.
- [GitHub MCP Server](https://github.com/github/github-mcp-server) - Official MCP server exposing GitHub repositories, issues, and pull requests to AI clients.
- [Korean Law MCP](https://github.com/chrisryugj/korean-law-mcp) - MCP server and CLI for querying Korea's official statutes, precedents and administrative rules.
- [MCP for Blender](https://github.com/ahujasid/mcp-for-blender) - Blender add-on and MCP server that lets LLM agents create and modify 3D scenes.
- [mcp-context-forge](https://github.com/IBM/mcp-context-forge) - Gateway and registry that federates MCP and REST services with auth, rate limits, and an admin UI.
- [mcp-proxy (sparfenyuk)](https://github.com/sparfenyuk/mcp-proxy) - Bridges stdio MCP servers to SSE or streamable HTTP transports and back.
- [mcp-proxy (TBXark)](https://github.com/TBXark/mcp-proxy) - Aggregates several MCP servers behind one endpoint with config-driven routing.
- [mcp-use](https://github.com/mcp-use/mcp-use) - Framework for building MCP clients and agents, with Python and TypeScript SDKs.
- [Mobile MCP](https://github.com/mobile-next/mobile-mcp) - MCP server that automates and inspects iOS and Android simulators, emulators, and real devices.
- [Playwright MCP](https://github.com/microsoft/playwright-mcp) - MCP server giving LLM clients browser control through Playwright accessibility snapshots.
- [Unla](https://github.com/AmoyLab/Unla) - Gateway that turns existing HTTP APIs and MCP servers into MCP endpoints with a web console.

## Model Gateways and Routers

- [Arch Gateway](https://github.com/katanemo/archgw) - Edge proxy built on Envoy that routes and guards LLM traffic across model providers.
- [Bifrost](https://github.com/maximhq/bifrost) - Go-based LLM gateway with failover, load balancing and an OpenAI-compatible API you host yourself.
- [Claude Code Router](https://github.com/musistudio/claude-code-router) - Local router that sends coding-agent requests to different model providers based on rules.
- [CliRelay](https://github.com/kittors/CliRelay) - Self-hosted gateway that gives coding CLIs one API across several model providers.
- [Envoy AI Gateway](https://github.com/envoyproxy/ai-gateway) - Envoy-based gateway that routes and secures traffic to multiple LLM providers.
- [Headroom](https://github.com/chopratejas/headroom) - Proxy that compresses tool outputs, logs and retrieved chunks to cut token use for AI agents.
- [Higress (Alibaba)](https://github.com/alibaba/higress) - AI-native API gateway that adds model routing and AI plugins on top of Envoy.
- [LLM (Simon Willison)](https://github.com/simonw/llm) - Command-line tool for prompting many local and hosted models through one interface.
- [New API](https://github.com/QuantumNous/new-api) - AI model gateway that fronts many upstream providers behind one key with quotas and billing.
- [optillm](https://github.com/algorithmicsuperintelligence/optillm) - Optimizing inference proxy that adds routing, load balancing and failover across multiple LLM providers.
- [Switchyard](https://github.com/NVIDIA-NeMo/Switchyard) - Rust proxy that routes traffic across LLM providers while keeping OpenAI and Anthropic API compatibility.

## Observability and Evals

- [agentsview](https://github.com/kenn-io/agentsview) - Local-first search, analytics, and token and cost statistics for coding agent sessions.
- [Aim](https://github.com/aimhubio/aim) - Self-hosted experiment tracker with a web UI for comparing very large numbers of training runs.
- [Argilla](https://github.com/argilla-io/argilla) - Data annotation and feedback platform for curating datasets and reviewing LLM outputs by hand.
- [ChainForge](https://github.com/ianarawjo/ChainForge) - Visual node-based environment for comparing prompts and model outputs across many LLMs.
- [DeepEval](https://github.com/confident-ai/deepeval) - Pytest-style evaluation framework for LLM apps with metrics for RAG and agent outputs.
- [Future AGI](https://github.com/future-agi/future-agi) - Self-hostable platform for tracing, evals, simulations and guardrails across LLM and agent apps.
- [Garak (NVIDIA)](https://github.com/NVIDIA/garak) - Command-line LLM vulnerability scanner that probes models for prompt injection, leakage and hallucination.
- [Harbor](https://github.com/harbor-framework/harbor) - Framework for running agent evaluations and building reinforcement-learning environments from the CLI.
- [Helicone](https://github.com/helicone/helicone) - LLM observability gateway that logs requests, costs, and latency through a proxy you host.
- [iFixAi](https://github.com/ifixai-ai/iFixAi) - Command-line agent auditing framework that runs adversarial checks and produces scored reports.
- [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) - Framework for evaluating LLMs and agents with solvers, scorers, and sandboxed tool execution.
- [LangWatch](https://github.com/langwatch/langwatch) - LLM monitoring and evaluation platform with tracing, datasets, and prompt management for AI apps.
- [LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness) - Framework for running standard benchmark suites against language models locally.
- [MLflow](https://github.com/mlflow/mlflow) - ML lifecycle platform with tracing, prompt versioning, and evaluation for LLM applications.
- [OpenLIT](https://github.com/openlit/openlit) - OpenTelemetry-native observability for LLM apps, with tracing, cost tracking and GPU metrics.
- [OpenLLMetry](https://github.com/traceloop/openllmetry) - OpenTelemetry instrumentation for LLM and vector database calls, exporting to any backend.
- [Opik](https://github.com/comet-ml/opik) - Open-source LLM tracing and evaluation platform with a self-hostable Docker deployment.
- [Pezzo](https://github.com/pezzolabs/pezzo) - Open-source LLMOps platform for prompt versioning, delivery and observability.
- [Promptfoo](https://github.com/promptfoo/promptfoo) - CLI and library for evaluating prompts, models, and RAG outputs with test assertions.
- [SkillSpector (NVIDIA)](https://github.com/NVIDIA/SkillSpector) - Security scanner that checks agent skills and MCP tools for prompt injection and exfiltration risks.

## RAG and Vector Databases

- [Chroma](https://github.com/chroma-core/chroma) - Embedding database for LLM apps with a single-node server and Python and JS clients.
- [Cognee](https://github.com/topoteretes/cognee) - Knowledge engine that builds graph and vector memory from documents for agents.
- [Graphiti](https://github.com/getzep/graphiti) - Framework for building temporal knowledge graphs from agent and user data for retrieval.
- [Haystack](https://github.com/deepset-ai/haystack) - Python framework for building search and RAG pipelines from swappable components.
- [HelixDB](https://github.com/HelixDB/helix-db) - Graph database with built-in vector and full-text search, written in Rust on object storage.
- [Hindsight](https://github.com/vectorize-io/hindsight) - Self-hosted long-term memory service for AI agents with integrations for common agent frameworks.
- [Infinity (AI Database)](https://github.com/infiniflow/infinity) - AI-native database server offering hybrid dense, sparse, and full-text search for LLM applications.
- [LanceDB](https://github.com/lancedb/lancedb) - Embedded multimodal vector database that stores tables on local disk or object storage.
- [LightRAG](https://github.com/HKUDS/LightRAG) - Graph-based retrieval system that indexes entities and relations for faster RAG queries.
- [LlamaIndex](https://github.com/run-llama/llama_index) - Data framework that connects private documents to LLMs through indexes and retrievers.
- [MaxKB](https://github.com/1Panel-dev/MaxKB) - Knowledge base and agent platform for RAG chatbots and workflow automation over your own documents.
- [MemPalace](https://github.com/MemPalace/mempalace) - Local AI memory system that stores and retrieves context for long-running agent workflows over MCP.
- [Milvus](https://github.com/milvus-io/milvus) - Distributed vector database built for large-scale embedding search with hybrid filtering.
- [MindsDB](https://github.com/mindsdb/mindsdb) - Federated SQL layer that connects databases and apps to AI models for querying and in-database ML.
- [OpenViking](https://github.com/volcengine/OpenViking) - Context database that unifies agent memory, knowledge retrieval and skills as a virtual filesystem.
- [pgvector](https://github.com/pgvector/pgvector) - Vector similarity search extension for PostgreSQL with exact and approximate nearest-neighbor indexes.
- [pgvectorscale](https://github.com/timescale/pgvectorscale) - PostgreSQL extension adding DiskANN-based vector indexes for faster approximate nearest neighbor search.
- [PrivateGPT](https://github.com/zylon-ai/private-gpt) - Offline document chat API with ingestion, embeddings, and an OpenAI-style interface.
- [Qdrant](https://github.com/qdrant/qdrant) - Vector similarity search engine in Rust with payload filtering and REST and gRPC APIs.
- [Quivr](https://github.com/The-Vibe-Company/quivr) - Open-source RAG app for chatting with your documents, runnable on your own infrastructure.
- [RAGFlow](https://github.com/infiniflow/ragflow) - Document-understanding RAG engine with chunking templates, citations, and agent workflows.
- [Supermemory](https://github.com/supermemoryai/supermemory) - Memory engine and app for agents that can run fully locally, with context-aware storage and retrieval.
- [Vespa](https://github.com/vespa-engine/vespa) - Search and serving engine combining vector and keyword retrieval with real-time indexing.
- [zvec](https://github.com/alibaba/zvec) - In-process vector database library for fast similarity search without running a server.

## Search and Knowledge

- [Agent-Reach](https://github.com/Panniantong/Agent-Reach) - CLI and search layer that lets agents pull content from Reddit, X, YouTube, GitHub and more.
- [Codegraph](https://github.com/colbymchenry/codegraph) - Local pre-indexed code knowledge graph that cuts token use and tool calls for coding agents.
- [Crawl4AI](https://github.com/unclecode/crawl4ai) - Open-source web crawler that turns pages into clean Markdown for retrieval and agent pipelines.
- [DB-GPT](https://github.com/eosphoros-ai/DB-GPT) - Self-hosted assistant for private knowledge and databases, with data-aware chat and RAG workflows.
- [DocsGPT](https://github.com/arc53/DocsGPT) - Self-hosted platform for building document-grounded assistants and agents with enterprise search.
- [Firecrawl](https://github.com/firecrawl/firecrawl) - Self-hostable web data API that scrapes and crawls sites into clean markdown or JSON for LLMs.
- [gpt-researcher](https://github.com/assafelovic/gpt-researcher) - Autonomous research agent that searches the web and writes cited reports on any topic.
- [LLM Wiki](https://github.com/nashsu/llm_wiki) - Desktop app that turns your documents into a linked wiki maintained by an LLM.
- [Open Notebook](https://github.com/lfnovo/open-notebook) - Self-hosted alternative to NotebookLM for organizing sources, notes and chats over your documents.
- [OpenResearch](https://github.com/alphaXiv/OpenResearch) - Local-first workspace that turns coding agents into research agents for literature review.
- [SearXNG](https://github.com/searxng/searxng) - Privacy-respecting metasearch engine you run yourself, aggregating results from many search services.
- [SurfSense](https://github.com/MODSetter/SurfSense) - Self-hosted workspace for organizing and querying team knowledge, in the style of a notebook app.
- [WeKnora](https://github.com/Tencent/WeKnora) - Knowledge platform that turns documents into a RAG index, a reasoning agent, and a maintained wiki.

## Speech and Audio

- [faster-whisper](https://github.com/SYSTRAN/faster-whisper) - Whisper reimplementation on CTranslate2 that transcribes faster with lower memory use.
- [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) - Few-shot voice cloning and text-to-speech system with a web interface, trained on short samples.
- [Kokoro-FastAPI](https://github.com/remsky/Kokoro-FastAPI) - OpenAI-compatible FastAPI server wrapping the Kokoro text-to-speech model.
- [Meetily](https://github.com/Zackriya-Solutions/meetily) - Local meeting assistant that transcribes audio in real time and writes summaries on your machine.
- [Moshi](https://github.com/kyutai-labs/moshi) - Full-duplex speech-to-speech model and dialogue system for real-time spoken conversation.
- [Piper](https://github.com/OHF-Voice/piper1-gpl) - Fast local neural text-to-speech engine that runs well on small single-board computers.
- [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) - Speech toolkit on ONNX Runtime for offline ASR, TTS and speaker tasks across many platforms.
- [Silero VAD](https://github.com/snakers4/silero-vad) - Voice activity detector model that runs on CPU from a small ONNX file.
- [Speaches](https://github.com/speaches-ai/speaches) - OpenAI-compatible server for transcription and speech synthesis on your own hardware.
- [TypeWhisper](https://github.com/TypeWhisper/typewhisper-mac) - Local speech-to-text app for macOS that runs models on-device, with optional cloud.
- [Voicebox](https://github.com/jamiepine/voicebox) - Local voice studio for cloning voices, generating multilingual speech, and dictating text.
- [VoiceStudio](https://github.com/debpalash/VoiceStudio) - Local voice platform covering multi-engine text-to-speech, voice cloning, and video dubbing.
- [Whisper](https://github.com/openai/whisper) - Reference speech recognition model and inference code for multilingual transcription.
- [whisper.cpp](https://github.com/ggml-org/whisper.cpp) - C and C++ port of Whisper for fast transcription on CPUs, Apple Silicon, and GPUs.
- [WhisperX](https://github.com/m-bain/whisperX) - Whisper pipeline that adds word-level timestamps and speaker diarization.

## Vision and Multimodal

- [CVAT](https://github.com/cvat-ai/cvat) - Web-based annotation tool for labeling images and video used to train computer vision models.
- [JoyAI-Image](https://github.com/jd-opensource/JoyAI-Image) - Multimodal foundation model for image understanding and text-to-image generation.
- [MiniCPM-V](https://github.com/OpenBMB/MiniCPM-V) - Multimodal model family for image, video and document understanding, with small variants for local use.
- [modlens](https://github.com/liustack/modlens) - Vision bridge that gives text-only LLM tools image understanding through a plugin.
- [WeVisDoc](https://github.com/Tencent/WeVisDoc) - End-to-end document parser for page images, fine-tuned from Qwen3-VL-2B-Instruct.

## Voice Agents

- [LiveKit](https://github.com/livekit/livekit) - Open-source WebRTC media server that realtime voice and video agent apps connect through.
- [LiveKit Agents](https://github.com/livekit/agents) - Framework for realtime voice and video AI agents, with plugins for speech, LLM and TTS services.
- [Pipecat](https://github.com/pipecat-ai/pipecat) - Python framework for real-time voice and multimodal conversational agents with pluggable services.
- [Speech to Speech](https://github.com/huggingface/speech-to-speech) - Modular voice agent pipeline chaining voice activity detection, speech recognition, LLM, and synthesis.
- [VoiceMem](https://github.com/xzf-thu/VoiceMem) - Memory infrastructure for voice agents that keeps conversation context across sessions.

## Rising

New projects under 500 stars that are worth watching. They move to their category at 500 stars.

- [Agentrove](https://github.com/Mng-dev-ai/agentrove) - Self-hosted workspace to run and orchestrate several AI coding agent CLIs in one place. (Coding Assistants)
- [Basjoo](https://github.com/haoyiyin/basjoo) - Self-hosted AI customer support platform with per-knowledge-base RAG on Qdrant. (RAG and Vector Databases)
- [flowcat](https://github.com/AreevAI/flowcat) - Self-hosted Rust runtime for real-time voice agents, shipped as a single binary. (Voice Agents)
- [franken_ocr](https://github.com/Dicklesworthstone/franken_ocr) - CPU-only OCR engine written in Rust that runs the Unlimited-OCR vision-language model. (MIT with OpenAI and Anthropic rider) (Document AI and OCR)
- [fxhoudinimcp](https://github.com/healkeiser/fxhoudinimcp) - MCP server that exposes SideFX Houdini scene control to AI agents. (MCP Servers and Gateways)
- [Guaardvark](https://github.com/guaardvark/guaardvark) - Self-hosted AI studio on your own GPU for chatting with your files and running agents. (Agents and Automation)
- [gyotaku](https://github.com/xevrion/gyotaku) - Offline Linux app that searches your screenshots by the text inside them. (Search and Knowledge)
- [keirouter](https://github.com/mydisha/keirouter) - Self-hostable AI gateway that proxies requests to multiple model providers. (Model Gateways and Routers)
- [kensaku](https://github.com/yjid/kensaku) - Local search across documents, code and screenshots, indexed on your own machine. (Search and Knowledge)
- [Kindly Web Search MCP Server](https://github.com/Shelpuk-AI-Technology-Consulting/kindly-web-search-mcp-server) - MCP server for web search and robust page content retrieval in AI coding tools. (MCP Servers and Gateways)
- [llamastash](https://github.com/llamastash/llamastash) - Terminal-native orchestrator that launches and manages local LLM engines and models with low overhead. (LLM Runtimes and Inference)
- [llmserve](https://github.com/AlexsJones/llmserve) - Terminal UI that picks a local model and backend, then starts a server for it. (LLM Runtimes and Inference)
- [Lumiverse](https://github.com/prolix-oc/Lumiverse) - Self-hosted AI chat frontend with an extension ecosystem and a focus on performance. (Lumiverse Community License 2.2, not OSI) (Chat Interfaces)
- [Mira](https://github.com/miracodeai/mira) - Self-hosted AI code reviewer with indexed pull request reviews and walkthroughs. (Coding Assistants)
- [mlxtop](https://github.com/maximpri/mlxtop) - Terminal monitor for local LLMs showing memory, GPU use and tokens per second. (Observability and Evals)
- [Myna](https://github.com/canonical/myna) - Lightweight speech-to-text desktop application for Ubuntu. (Speech and Audio)
- [Nyro](https://github.com/nyroway/nyro) - Self-hosted AI gateway that lets coding CLIs and SDKs call any model provider. (Model Gateways and Routers)
- [openasr](https://github.com/QuintinShaw/openasr) - Local-first speech-to-text command line tool that runs without cloud services or telemetry. (Speech and Audio)
- [PMetal](https://github.com/Epistates/pmetal) - Apple Silicon framework for local LLM inference and LoRA or QLoRA fine-tuning. (Fine-Tuning and Training)
- [ScribeCrate](https://github.com/hwdsl2/scribecrate) - Self-hosted Whisper speech-to-text server powered by faster-whisper. (Speech and Audio)
- [shodh-memory](https://github.com/varun29ankuS/shodh-memory) - Local, LLM-free memory engine for AI agents, packaged as one offline Rust binary. (Agents and Automation)
- [thunderbird-mcp](https://github.com/TKasperczyk/thunderbird-mcp) - MCP server that gives AI assistants access to Thunderbird email, contacts and calendar. (MCP Servers and Gateways)
- [VoicEra](https://github.com/COSS-India/VoicEra) - Voice AI building block with telephony integration and real-time speech processing. (Voice Agents)
- [YoloRouter](https://github.com/yolorouter/yolorouter) - Self-hosted OpenAI-compatible LLM gateway with provider failover and key rotation. (Model Gateways and Routers)
- [zx-bench](https://github.com/suncityldp/zx-bench) - Local LLM benchmarking platform with versioned datasets and deterministic scoring. (Observability and Evals)

## Source-Available

Widely used and self-hostable, but the license adds terms beyond a standard open-source license. Check them before commercial use.

- [Activepieces](https://github.com/activepieces/activepieces) - Self-hostable automation platform that adds AI agents and MCP integrations to workflow building. (MIT core, ee directory under separate terms)
- [agent-qa](https://github.com/vostride/agent-qa) - Web and mobile QA agent with CLI/MCP, memidex memory, validated self-improvement and reviewable evidence. (FSL-1.1-ALv2; commercial use limited to the license's Permitted Purpose)
- [Agenta](https://github.com/Agenta-AI/agenta) - Open-source LLMOps platform for prompt management, evaluation and observability. (MIT core, ee/ directories under their own license)
- [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) - Platform for building, running and monitoring autonomous AI agents with a visual workflow builder. (Polyform Shield for platform, MIT elsewhere)
- [Browserless](https://github.com/browserless/browserless) - Headless Chrome service that agents and scripts drive over an API for browser automation at scale. (MongoDB SSPL or commercial license)
- [Crush](https://github.com/charmbracelet/crush) - Terminal-based AI coding agent that works with multiple LLM providers and project context. (FSL-1.1-MIT (converts to MIT after two years))
- [Dify](https://github.com/langgenius/dify) - Platform for building agentic workflows and LLM apps with a visual editor, RAG pipeline and model management. (Modified Apache-2.0 with extra terms)
- [FastGPT](https://github.com/labring/FastGPT) - Knowledge base and workflow platform for building RAG chatbots over your own documents. (Apache-2.0 with additional conditions)
- [Fish Speech](https://github.com/fishaudio/fish-speech) - Text-to-speech and voice cloning model and server for multilingual speech synthesis. (Fish Audio Community License 1.0)
- [Foundry Local](https://github.com/microsoft/Foundry-Local) - Microsoft on-device runtime with a CLI and local API for running open models on your own hardware. (SDK is MIT; CLI under Microsoft license terms)
- [HunyuanVideo](https://github.com/Tencent-Hunyuan/HunyuanVideo) - Large open video generation model from Tencent for text-to-video creation on your own GPUs. (Tencent Hunyuan Community License, excludes EU/UK/KR)
- [IndexTTS](https://github.com/index-tts/index-tts) - Zero-shot text-to-speech model that clones a voice from a short reference audio clip. (bilibili Model Use License Agreement)
- [Langfuse](https://github.com/langfuse/langfuse) - LLM engineering platform for tracing, prompt management and evals, self-hostable with Docker. (MIT core, ee/ directories under their own license)
- [LiteLLM](https://github.com/BerriAI/litellm) - Python SDK and proxy server that calls 100+ LLM APIs in the OpenAI format. (MIT core, enterprise/ directory under its own license)
- [LobeChat](https://github.com/lobehub/lobe-chat) - Modern chat UI for many LLM providers with plugins, knowledge bases and multimodal input. (LobeHub Community License)
- [LTX-2](https://github.com/Lightricks/LTX-2) - Open video generation model and pipeline for text-to-video and image-to-video on your own GPUs. (LTX Community License Agreement)
- [Meilisearch](https://github.com/meilisearch/meilisearch) - Search engine with typo tolerance and hybrid and vector search, run as a single self-hosted binary. (MIT core, EE parts under Business Source License 1.1)
- [MinerU](https://github.com/opendatalab/MinerU) - Converts PDFs into Markdown and JSON with layout, table and formula recognition, on local GPUs or CPUs. (Apache-2.0 plus commercial-use terms in LICENSE)
- [n8n](https://github.com/n8n-io/n8n) - Workflow automation platform with code and no-code nodes, including AI agent and LLM building blocks. (Sustainable Use License)
- [Open WebUI](https://github.com/open-webui/open-webui) - Self-hosted web interface for chatting with local and cloud LLMs, with RAG, tools and user management. (Open WebUI License)
- [Phoenix](https://github.com/Arize-ai/phoenix) - Tracing, evaluation and prompt experimentation tool for LLM apps, built on OpenTelemetry. (Elastic License 2.0 (ELv2))
- [Qwen-Image-2.1](https://github.com/QwenLM/Qwen-Image-2.1) - Open image generation model from the Qwen team, distributed under the Qwen research license. (Qwen Research License Agreement)
- [TEN Framework](https://github.com/TEN-framework/ten-framework) - Framework for real-time multimodal voice agents with modules for ASR, LLM, TTS and avatars. (Apache-2.0 with additional conditions)
- [Wan2GP](https://github.com/deepbeepmeep/Wan2GP) - Low-VRAM app for running Wan and other open video generation models on consumer GPUs. (WanGP Community License 2.0)
- [Weaviate](https://github.com/weaviate/weaviate) - Vector database with hybrid search and built-in embedding modules, runnable on your own servers. (BSD-3 core, wl/ directory under Weaviate License)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). New projects go in `data/projects.json`; this file is generated.
