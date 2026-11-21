# Awesome AI Tools [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

![GitHub stars](https://img.shields.io/github/stars/d123d/awesome-ai-tools?style=social) ![Last commit](https://img.shields.io/github/last-commit/d123d/awesome-ai-tools)

**By the numbers (Nov 20, 2026):** 420+ entries · 74 tools worth a look (new) · 297 starred repos in 9 sections · 34 custom skills · 58 system skills · 30+ connectors. Links are checked weekly by CI.

A curated handout of **the AI tools we actually use and star** — agent harnesses, coding agents, skills and MCP servers, local models and inference, ComfyUI video/image pipelines, 3D and world generation, voice, and the automation that ties them together.

Two lists in one:

1. **Our stack** — the tools in daily use here, grouped by job. The full inventory handout is [TOOLS.md](TOOLS.md).
2. **Starred by d123d** — every GitHub repo [d123d](https://github.com/d123d) has starred — **297 public repos** as of Nov 19, 2026 (1 private star omitted), pulled live from the GitHub API, no cherry-picking. Machine-readable copy: [data/starred.json](data/starred.json).

Sister list: [awesome-dnd](https://github.com/d123d/awesome-dnd)

Only open, free, or free-tier tools are listed as *tools* in Our Stack. Each entry keeps its own license — check it before reuse. The list itself is CC0.

## Contents

- [Recent Additions](#recent-additions)
- [Agent Harnesses & Coding Agents](#agent-harnesses--coding-agents)
- [Skills, MCP & Agent Infrastructure](#skills-mcp--agent-infrastructure)
- [Local Models & Inference](#local-models--inference)
- [Image, Video & ComfyUI](#image-video--comfyui)
- [3D, Animation & Worlds](#3d-animation--worlds)
- [Voice, Audio & Music](#voice-audio--music)
- [Writing, Worldbuilding & Games](#writing-worldbuilding--games)
- [Automation & Bridges](#automation--bridges)
- [More Tools Worth a Look](#more-tools-worth-a-look)
- [Starred by d123d — the complete list](#starred-by-d123d--the-complete-list)
- [License](#license)

## Recent Additions

### Nov 19, 2026 — D&D agent-stack tools (in [dnd-agent-stack](https://github.com/d123d/dnd-agent-stack))

- `tools/stage.py` — Event-to-stage translator: campaign events (NDJSON) → Blender staging script + shotlist; sets per location, named actors per NPC, keyframed moves/deaths/reveals, camera per beat. Nothing is staged before its reveal event.
- `tools/rigs.py` — Rig pass: species→height, name-hash palette, props, articulated proxy rigs (root + torso/head/arms/legs) built by stage.py.
- `tools/film.py` + `film_session.py` — Filming: previs camera paths by intent, Eevee previs / Cycles final, DM approval gate, then an mmx handoff file with per-shot frame, prompt, and exact MiniMax command.
- `tools/srd.py` — SRD 5.2.1 loader over the complete 5e database (341 monsters, 339 spells).
- `tools/dmctl.py` + `state_engine.py` — Campaign state engine: SQLite + append-only events, mutate → validate → commit.
- `tools/dm_mcp_server.py` — MCP server exposing the same validated state path to agents.
- `tools/lore.py` + `permissions.py` — Tiered lore (campaign > canon > reference) and server-side role permissions for DM / player / NPC agents.
- `build_lore_index.py` (dnd-library) — Lore index builder over the Forgotten Realms play files.

### Nov 14, 2026 — Skill batch (29 skills, read-first, from skills.sh)

World generation: procedural-gen, worldbuilding, threejs-world-generation, worldlabs, scenario-3d-worlds, systemic-worldbuilding, oblique-worldbuilding, maplibre-terrain-rendering, cesiumjs-terrain-environment. Blender & 3D: blender-modeling/materials/rendering/export/animation/cameras, blender-mcp, camera-cinematography, threejs-animation, meshy-3d-generation, layer-3d, game-3d-assets. MiniMax: mmx-cli, h3-prompt-writing. Writing & D&D: fantasy-fiction-writer, fantasy-writer, story-planning, dnd, dnd5e-srd. Plus openrouter-typescript-sdk, ponytail, and caveman.

### Most recently starred (Nov 2026, newest first)

- [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) — Long-video generation model.
- [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) — Editable AI video editor. *Open source.*
- [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) — Gives an agent eyes on the internet: Twitter, Reddit, YouTube and more.
- [EL4CTEO/blender-skills](https://github.com/EL4CTEO/blender-skills) — Blender 5.3 workflows as agent skills for Claude Code, Codex, Gemini CLI.
- [toyxyz/toyxyz_RGBMocap](https://github.com/toyxyz/toyxyz_RGBMocap) — Windows video motion capture (ExMR / FlowHMR / GVHMR).
- [MaxLiu22/Motion2MixamoRig](https://github.com/MaxLiu22/Motion2MixamoRig) — Retarget human motion from video to a Mixamo-rigged character.
- [Moh4696/cinematic-skill](https://github.com/Moh4696/cinematic-skill) — Agent skill for narrated cinematic films built from code.
- [codepawl/crucible](https://github.com/codepawl/crucible) — 3D engine that AI agents drive.
- [islandmed/SculptForge](https://github.com/islandmed/SculptForge) — Open-source 3D sculpting. 
- [JAMESYJL/ShapeLLM-Omni](https://github.com/JAMESYJL/ShapeLLM-Omni) — Multimodal LLM for 3D generation and understanding (NeurIPS 2025).
- [yyeboah/Awesome-Text-to-3D](https://github.com/yyeboah/Awesome-Text-to-3D) — Text-to-3D curation.
- [suvadityamuk/trellis2-cuda](https://github.com/suvadityamuk/trellis2-cuda) — TRELLIS.2 image-to-3D in pure CUDA, 5.3× faster.
- [Nebuluss/H3-AudioRetake-studio](https://github.com/Nebuluss/H3-AudioRetake-studio) — Audio and lip-sync retake studio for ComfyUI + MiniMax H3.
- [jutsuhq/open-source-higgsfield](https://github.com/jutsuhq/open-source-higgsfield) — Index of open-source Higgsfield alternatives (117 projects).
- [rediumvex/ai-video-generator-claude](https://github.com/rediumvex/ai-video-generator-claude) — Claude skills that write studio-quality AI video prompts.
- [alisson-anjos/Henge](https://github.com/alisson-anjos/Henge) — Motion transfer and video swaps with MiniMax H3.
- [itsmetamike/reshoot-4d](https://github.com/itsmetamike/reshoot-4d) — Reshoot any video in 4D; camera editor in ComfyUI.
- [PxTicks/h3-motion](https://github.com/PxTicks/h3-motion) — MiniMax H3 motion work.
- [nomadoor/ComfyUI-Panorama-Stickers](https://github.com/nomadoor/ComfyUI-Panorama-Stickers) — Panorama stickers node for ComfyUI.
- [xentome/EDITS-WITH-AI](https://github.com/xentome/EDITS-WITH-AI) — Local AI music edits: MiniMax H3 + local LLM in ComfyUI.

All 20 are also in the full starred list below.

## Agent Harnesses & Coding Agents

- [Muse](https://github.com/Musespark) — Meta's personal agent (Muse Spark): long-running memory, skills, connectors, scheduled work, and subagents. The agent writing this list.
- [Claude Code](https://claude.com/product/claude-code) — Anthropic's terminal coding agent; runs locally on the PC, directed remotely through our Telegram bridge.
- [OpenAI Codex](https://openai.com/codex/) — OpenAI's coding agent, used alongside Claude Code in the agent stack.
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) — Google's open-source terminal agent. *Apache-2.0.*
- [OpenCode](https://opencode.ai/) — Open-source, provider-agnostic coding agent with quota checks in our scripts.
- [Crush](https://github.com/charmbracelet/crush) — Charm's terminal coding agent; binaries and versions audited by our ai-scripts.
- [OpenClaw](https://github.com/openclaw/openclaw) — Self-hosted personal-agent gateway (Telegram channel, scheduled tasks, failover recovery).
- [Aider](https://github.com/Aider-AI/aider) — Pair-programming in the terminal over your own git repo. *Apache-2.0.*
- [Ollama](https://github.com/ollama/ollama) — Run LLMs locally; the default local-model entry point. *MIT.*

## Skills, MCP & Agent Infrastructure

- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) — The open standard every tool server here speaks: GitHub, Blender, SRD data, state engines.
- [skills.sh / Find Skills](https://skills.sh/) — Skill discovery and install (`npx skills add <owner/repo>`). Local rule: read the SKILL.md first, never run third-party install scripts uninspected.
- [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) — Curated agent skills collection (starred).
- [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) — Skills for OpenClaw (starred).
- [OpenRouter](https://openrouter.ai/) — One API for many models; we use its TypeScript SDK.
- [Temporal](https://temporal.io/) — Durable workflows; owns turns and dice rolls in the voice-agent D&D experiments we fork and star.
- Our own skill packs — 34 custom skills in daily use (Blender ×7, D&D, worldbuilding, 3D generation, cinematography, MiniMax H3 prompting, caveman/ponytail token discipline). Full list in [TOOLS.md](TOOLS.md).

## Local Models & Inference

- [llama.cpp](https://github.com/ggml-org/llama.cpp) — Local inference workhorse; our PC runs a llama router with Qwen and Granite models behind it. *MIT.*
- [Unsloth](https://github.com/unslothai/unsloth) — Fast local fine-tuning (starred).
- Qwen model family — local primary models on the PC (Qwen2.5 14B launcher, Qwen router configs in ai-scripts).
- IBM Granite 8B — tuned local model in the router mix.
- ComfyUI — the inference hub for most media work; listed once under [Image, Video & ComfyUI](#image-video--comfyui).

## Image, Video & ComfyUI

- [ComfyUI](https://github.com/Comfy-Org/ComfyUI) — The studio: custom nodes, idle releaser, watchdog and process guard in our ai-scripts keep it healthy on one GPU.
- [MiniMax H3 + mmx CLI](TOOLS.md) — Text/image-to-video finishing pass for our film pipeline: Blender previs → H3 repaint. Prompting rules live in our `h3-prompt-writing` skill.
- Higgsfield-style open studios — a whole starred family of open-source ComfyUI studios (image, video, VFX, lip-sync, music) cloned and compared; see the starred list, Video section.
- [Meshy](https://www.meshy.ai/) — Text/image-to-3D generation, used through our `meshy-3d-generation` skill.
- [World Labs](https://www.worldlabs.ai/) — 3D world/environment generation from images and prompts.
- [Scenario](https://www.scenario.com/) — Model-picking and consistent-character image/video/3D generation, plus its Blender plugin and skills (starred).

## 3D, Animation & Worlds

- [Blender](https://www.blender.org/) — Everything stages here first. Driven headless and over MCP (`blender-mcp` skill + 6 Blender sub-skills). *GPL.*
- [MPFB](https://github.com/makehumancommunity/mpfb2) — Rigged humans in Blender; our standard rig is Mixamo.
- Mesh2Motion — CC0 auto-rigging (humanoid, horse, dragon, bird, fox/wolf, snake, fish, spider, kaiju templates).
- [Kimodo (NVIDIA)](https://github.com/nv-tlabs/kimodo) — Text-to-motion clip generation when the motion library has no match.
- Motion library — 14,858 BVH clips on the PC (CMU, Mixamo, 100STYLE, Bandai, LAFAN1, ZEGGS and more), indexed and searchable.
- [TRELLIS / TRELLIS.2 (Microsoft)](https://github.com/microsoft/TRELLIS) — Image-to-3D (starred); part of the picture → mesh comparison route with Pixal3D and Hunyuan3D.
- [Hunyuan3D 2.1 (Tencent)](https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1) — Image-to-3D generation (starred), plus the HunyuanWorld family for world generation.
- [Three.js](https://github.com/mrdoob/three.js) — Browser 3D: world generation and animation skills, Gaussian splat viewers (starred). *MIT.*
- [CesiumJS](https://cesium.com/platform/cesiumjs/) and [MapLibre GL](https://maplibre.org/) — Terrain, globe and map rendering for world projects.

## Voice, Audio & Music

- Edge TTS — OpenAI-compatible local TTS API shim in ai-scripts; the default narration voice route.
- [Whisper](https://github.com/openai/whisper) — Transcription for recordings and voice notes. *MIT.*
- MiniMax H3 audio retake / lip-sync — ComfyUI studio for retakes that keep the picture (starred: Nebuluss/H3-AudioRetake-studio).

## Writing, Worldbuilding & Games

- Our D&D / Forgotten Realms agent stack — [dnd-agent-stack](https://github.com/d123d/dnd-agent-stack) (DM state engine, SRD loader, MCP server, Blender staging and filming tools) and [awesome-dnd](https://github.com/d123d/awesome-dnd).
- Worldbuilding skill suite — systemic worldbuilding, oblique/documentary worldbuilding, story planning, fantasy fiction writing (custom skills, see [TOOLS.md](TOOLS.md)).
- Reverse-engineered games — the awesome lists and engine reimplementations we starred in Oct 2026 (heaven-hm/awesome-reverse-engineered-games, morluto/awesome-reverse-engineering, SubmitGame/awesome-decomp-games); all in the starred list below.

## Automation & Bridges

- Telegram bridge — cloud Muse → Telegram bot → PC-side bridge (Telethon) → local Claude inbox/outbox. Design and scripts are ours.
- GitHub API helpers — `gh_api.py`, `gh_pr_push.py`, `gh_tarball.py`, `gh_download.py`: all GitHub writes from the cloud VM go through the API.
- Hourly GitHub rotation — one active repo improved per hour, hard limits: no deletes, no force-pushes, no visibility changes, copyrighted text never in public repos.
- Tool inventory maintenance — weekly job that refreshes the PC's tool registry, applies safe stable updates, smoke-tests, and reports by Telegram.

---
## More Tools Worth a Look

**Not in daily use (yet).** Verified live on GitHub on Nov 20, 2026 — repo, star count, and description pulled from the API — and grouped by the job they would do here. Candidates for the stack, not part of it. Two more verified tools are already in Our Stack above and are not repeated: [ComfyUI](#image-video--comfyui) and [Aider](#agent-harnesses--coding-agents).

### Platforms & Inference

- [huggingface/huggingface_hub](https://github.com/huggingface/huggingface_hub) — ★4,059 — The official CLI and Python client for the Hugging Face Hub. *Apache-2.0.*
- [huggingface/transformers](https://github.com/huggingface/transformers) — ★169,331 — 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and… *Apache-2.0.*
- [vllm-project/vllm](https://github.com/vllm-project/vllm) — ★97,284 — A high-throughput and memory-efficient inference and serving engine for LLMs. *Apache-2.0.*
- [sgl-project/sglang](https://github.com/sgl-project/sglang) — ★38,888 — SGLang is a high-performance serving framework for large language models and multimodal models. *Apache-2.0.*
- [open-webui/open-webui](https://github.com/open-webui/open-webui) — ★159,172 — User-friendly AI Interface (Supports Ollama, OpenAI API, ...). *NOASSERTION.*
- [LibreChat-AI/LibreChat](https://github.com/LibreChat-AI/LibreChat) — ★47,370 — Enhanced ChatGPT Clone: Features Agents, MCP, Skills, DeepSeek, Anthropic, AWS, OpenAI, Responses API, Azure, Groq, o1, GPT-5, Mistral, OpenRouter, Vertex AI, Gemini,… *MIT.*
- [langgenius/dify](https://github.com/langgenius/dify) — ★161,582 — Build Agentic workflows, RAG pipelines, with rich AI model and tool support on one collaborative workspace. Deploy on cloud, VPC, or self-hosted, so teams move from… *NOASSERTION.*
- [langflow-ai/langflow](https://github.com/langflow-ai/langflow) — ★156,812 — Langflow is a powerful tool for building and deploying AI-powered agents and workflows. *MIT.*
- [FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise) — ★55,584 — Build AI Agents, Visually. *NOASSERTION.* *(archived)*
- [n8n-io/n8n](https://github.com/n8n-io/n8n) — ★211,555 — Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations. *NOASSERTION.*
- [nomic-ai/gpt4all](https://github.com/nomic-ai/gpt4all) — ★77,332 — GPT4All: Run Local LLMs on Any Device. Open-source and available for commercial use. *MIT.*
- [janhq/jan](https://github.com/janhq/jan) — ★45,964 — Jan is an open source alternative to ChatGPT that runs 100% offline on your computer. *NOASSERTION.*
- [lmstudio-ai/lms](https://github.com/lmstudio-ai/lms) — ★5,444 — LM Studio CLI. *MIT.*
- [oobabooga/textgen](https://github.com/oobabooga/textgen) — ★47,734 — Open-source desktop app for local LLMs. Text, vision, tool-calling, OpenAI/Anthropic-compatible API. 100% private. *AGPL-3.0.*
- [pinokiocomputer/pinokio](https://github.com/pinokiocomputer/pinokio) — ★8,424 — AI Browser. *MIT.*

### Agents & MCP

- [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) — ★45,204 — Build resilient agents. *MIT.*
- [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) — ★61,130 — Framework for orchestrating role-playing, autonomous AI agents. By fostering collaborative intelligence, CrewAI empowers agents to work together seamlessly, tackling… *MIT.*
- [microsoft/autogen](https://github.com/microsoft/autogen) — ★61,954 — A programming framework for agentic AI. *CC-BY-4.0.* *(archived)*
- [huggingface/smolagents](https://github.com/huggingface/smolagents) — ★30,461 — 🤗 smolagents: a barebones library for agents that think in code. *Apache-2.0.*
- [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) — ★93,929 — 🙌 OpenHands: AI-Driven Development. *MIT.*
- [SWE-agent/SWE-agent](https://github.com/SWE-agent/SWE-agent) — ★20,840 — SWE-agent takes a GitHub issue and tries to automatically fix it, using your LM of choice. It can also be employed for offensive cybersecurity or competitive coding… *MIT.*
- [mem0ai/mem0](https://github.com/mem0ai/mem0) — ★69,286 — The Memory Layer for AI Agents - Drop-in memory infrastructure for AI agents and apps. Context that persists. Built for production. *Apache-2.0.*
- [letta-ai/letta](https://github.com/letta-ai/letta) — ★25,505 — Platform for stateful agents: AI with advanced memory that can learn and self-improve over time. *Apache-2.0.*
- [topoteretes/cognee](https://github.com/topoteretes/cognee) — ★33,437 — Cognee is the open-source AI memory platform for agents. Give your AI agents persistent long-term memory with small models for free. *Apache-2.0.*
- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) — ★92,135 — Model Context Protocol Reference Servers. *NOASSERTION.*
- [github/github-mcp-server](https://github.com/github/github-mcp-server) — ★34,625 — GitHub's official MCP Server. *MIT.*
- [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) — ★39,942 — Playwright MCP server. *Apache-2.0.*
- [upstash/context7](https://github.com/upstash/context7) — ★65,194 — Context7 Platform -- Up-to-date docs for AI agents. *MIT.*
- [oraios/serena](https://github.com/oraios/serena) — ★31,557 — A powerful MCP toolkit for coding, providing semantic retrieval and editing capabilities  - the IDE for your agent. *NOASSERTION.*

### Coding Agents

- [continuedev/continue](https://github.com/continuedev/continue) — ★36,532 — open-source coding agent. *Apache-2.0.*
- [RooCodeInc/Roo-Code](https://github.com/RooCodeInc/Roo-Code) — ★24,237 — Roo Code gives you a whole dev team of AI agents in your code editor. *Apache-2.0.* *(archived)*
- [TabbyML/tabby](https://github.com/TabbyML/tabby) — ★33,933 — Self-hosted AI coding assistant. *NOASSERTION.*

### Browser Agents

- [browser-use/browser-use](https://github.com/browser-use/browser-use) — ★121,623 — Open-source Python library for AI browser agents, plus Browser Use Cloud: stealth browsers and a hosted agent API. *MIT.*
- [browserbase/stagehand](https://github.com/browserbase/stagehand) — ★26,105 — The SDK to extract data and interact with any site on the web. Get started with Claude Code, Codex, Eve, Mastra, and more. *MIT.*
- [Skyvern-AI/skyvern](https://github.com/Skyvern-AI/skyvern) — ★23,481 — Automate browser based workflows with AI. *AGPL-3.0.*

### Data, RAG & Evals

- [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) — ★205,301 — Knowledge infrastructure to make your agents smarter. Search, scrape and access 550+ data providers through one API. *AGPL-3.0.*
- [docling-project/docling](https://github.com/docling-project/docling) — ★70,828 — Get your documents ready for gen AI. *MIT.*
- [opendatalab/MinerU](https://github.com/opendatalab/MinerU) — ★84,064 — Transforms complex documents like PDFs and Office docs into LLM-ready markdown/JSON for your Agentic workflows. *NOASSERTION.*
- [qdrant/qdrant](https://github.com/qdrant/qdrant) — ★35,650 — Qdrant - High-performance, massive-scale Vector Database and Vector Search Engine for the next generation of AI. Also available in the cloud https://cloud.qdrant.io/. *Apache-2.0.*
- [chroma-core/chroma](https://github.com/chroma-core/chroma) — ★29,718 — Search infrastructure for AI. *Apache-2.0.*
- [milvus-io/milvus](https://github.com/milvus-io/milvus) — ★46,708 — Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search. *Apache-2.0.*
- [langfuse/langfuse](https://github.com/langfuse/langfuse) — ★37,680 — 🪢 Open source AI engineering platform: AI Gateway, agent observability, evals, and prompt/skill management, built on OpenTelemetry. One open platform for every AI… *NOASSERTION.*
- [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) — ★12,366 — AI Observability & Evaluation. *NOASSERTION.*
- [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) — ★27,501 — Test your prompts, agents, and RAGs. Red teaming/pentesting/vulnerability scanning for AI. Compare performance of GPT, Claude, Gemini, DeepSeek, and more. Simple… *MIT.*

### Voice & Audio

- [livekit/livekit](https://github.com/livekit/livekit) — ★22,314 — End-to-end realtime stack for connecting humans and AI. *Apache-2.0.*
- [pipecat-ai/pipecat](https://github.com/pipecat-ai/pipecat) — ★17,364 — Open Source framework for voice agents, multimodal apps, and realtime AI. Maintained by Daily and the community. *BSD-2-Clause.*
- [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper) — ★26,911 — Faster Whisper transcription with CTranslate2. *MIT.*
- [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox) — ★28,007 — SoTA open-source TTS. *MIT.*
- [hexgrad/kokoro](https://github.com/hexgrad/kokoro) — ★10,269 — https://hf.co/hexgrad/Kokoro-82M. *Apache-2.0.*
- [QwenAudio/CosyVoice](https://github.com/QwenAudio/CosyVoice) — ★24,463 — Multi-lingual large voice generation model, providing inference, training and deployment full-stack ability. *Apache-2.0.*
- [SWivid/F5-TTS](https://github.com/SWivid/F5-TTS) — ★15,632 — Official code for "F5-TTS: A Fairytaler that Fakes Fluent and Faithful Speech with Flow Matching". *MIT.*
- [rany2/edge-tts](https://github.com/rany2/edge-tts) — ★12,599 — Use Microsoft Edge's online text-to-speech service from Python WITHOUT needing Microsoft Edge. *NOASSERTION.*

### Image & Video Models

- [lllyasviel/Fooocus](https://github.com/lllyasviel/Fooocus) — ★53,962 — Focus on prompting and generating. *GPL-3.0.*
- [invoke-ai/InvokeAI](https://github.com/invoke-ai/InvokeAI) — ★29,131 — Invoke is a leading creative engine that uses image and video generation models to empower professionals, artists, and enthusiasts to generate and create visual media… *Apache-2.0.*
- [AUTOMATIC1111/stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) — ★165,366 — Stable Diffusion web UI. *AGPL-3.0.*
- [black-forest-labs/flux](https://github.com/black-forest-labs/flux) — ★26,072 — Official inference repo for FLUX.1 models. *Apache-2.0.*
- [Lightricks/LTX-Video](https://github.com/Lightricks/LTX-Video) — ★11,445 — Official repository for LTX-Video. *Apache-2.0.*
- [Wan-Video/Wan2.1](https://github.com/Wan-Video/Wan2.1) — ★17,468 — Wan: Open and Advanced Large-Scale Video Generative Models. *Apache-2.0.*
- [zai-org/CogVideo](https://github.com/zai-org/CogVideo) — ★13,217 — text and image to video generation: CogVideoX (2024) and CogVideo (ICLR 2023). *Apache-2.0.*
- [Tencent-Hunyuan/HunyuanVideo](https://github.com/Tencent-Hunyuan/HunyuanVideo) — ★12,814 — HunyuanVideo: A Systematic Framework For Large Video Generation Model. *NOASSERTION.*
- [genmoai/mochi](https://github.com/genmoai/mochi) — ★3,766 — The best OSS video generation models, created by Genmo. *Apache-2.0.*
- [upscayl/upscayl](https://github.com/upscayl/upscayl) — ★52,989 — 🆙 Upscayl - #1 Free and Open Source AI Image Upscaler for Linux, MacOS and Windows. *AGPL-3.0.*
- [xinntao/Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) — ★37,588 — Real-ESRGAN aims at developing Practical Algorithms for General Image/Video Restoration. *BSD-3-Clause.*
- [OpenTalker/SadTalker](https://github.com/OpenTalker/SadTalker) — ★14,213 — [CVPR 2023] SadTalker：Learning Realistic 3D Motion Coefficients for Stylized Audio-Driven Single Image Talking Face Animation. *NOASSERTION.*
- [Rudrabha/Wav2Lip](https://github.com/Rudrabha/Wav2Lip) — ★13,282 — This repository contains the codes of "A Lip Sync Expert Is All You Need for Speech to Lip Generation In the Wild", published at ACM Multimedia 2020. For HD…
- [antgroup/echomimic_v2](https://github.com/antgroup/echomimic_v2) — ★4,678 — [CVPR 2025] EchoMimicV2: Towards Striking, Simplified, and Semi-Body Human Animation. *Apache-2.0.*
- [bytedance/LatentSync](https://github.com/bytedance/LatentSync) — ★6,306 — Taming Stable Diffusion for Lip Sync! *Apache-2.0.*

### Training

- [huggingface/peft](https://github.com/huggingface/peft) — ★21,908 — 🤗 PEFT: State-of-the-art Parameter-Efficient Fine-Tuning. *Apache-2.0.*
- [huggingface/trl](https://github.com/huggingface/trl) — ★19,781 — Train transformer language models with reinforcement learning. *Apache-2.0.*
- [axolotl-ai-cloud/axolotl](https://github.com/axolotl-ai-cloud/axolotl) — ★12,739 — Go ahead and axolotl questions. *Apache-2.0.*
- [hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory) — ★76,162 — Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024). *Apache-2.0.*

### Cloud GPU & APIs

- [modal-labs/modal-examples](https://github.com/modal-labs/modal-examples) — ★1,291 — Examples of programs built using Modal. *MIT.*
- [replicate/replicate-python](https://github.com/replicate/replicate-python) — ★919 — Python client for Replicate. *Apache-2.0.*
- [fal-ai/fal](https://github.com/fal-ai/fal) — ★983 — ⚡ Fastest way to serve open source ML models to millions. *Apache-2.0.*
## Starred by d123d — the complete list

All **297 GitHub repos starred by [d123d](https://github.com/d123d)**, pulled from the GitHub API and sorted into sections automatically by name, description, and topics (star counts as of the last refresh). Every public star, no cherry-picking (1 private star omitted). Machine-readable copy: [data/starred.json](data/starred.json). Regenerate with `python3 build_list.py`.

### Agents, Harnesses, Skills & MCP (42)

- [morluto/rea](https://github.com/morluto/rea) — ★470,064 — Reverse engineer anything with agents, from app behavior down to native binaries. *TypeScript.*
- [obra/superpowers](https://github.com/obra/superpowers) — ★322,112 — An agentic skills framework & software development methodology that works. *Shell.*
- [anthropics/skills](https://github.com/anthropics/skills) — ★197,724 — Public repository for Agent Skills. *Python.*
- [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) — ★194,869 — Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote. *JavaScript.*
- [f/prompts.chat](https://github.com/f/prompts.chat) — ★177,902 — f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open source — self-host for your organization with complete privacy. *MDX.*
- [farion1231/cc-switch](https://github.com/farion1231/cc-switch) — ★155,817 — A cross-platform desktop All-in-One assistant for Claude Code, Codex, OpenCode,DeepSeek Harness and more. Only official website: ccswitch.io. *Rust.*
- [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) — ★121,570 — why use many token when few token do trick. Skill + local proxy for coding agents: shorter answers, smaller tool output, every original recoverable. *Go.*
- [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) — ★119,190 — Production-grade engineering skills for AI coding agents. *JavaScript.*
- [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) — ★113,340 — Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees. *Python.*
- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) — ★98,263 — A collection of MCP servers.
- [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) — ★87,057 — AI video you can actually edit. HyperFrames is a free, open-source AI video editor. Describe any video and get a real project you can change down to the frame. *TypeScript.*
- [OpenMontageInc/OpenMontage](https://github.com/OpenMontageInc/OpenMontage) — ★81,769 — World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700+ agent skill and production-knowledge files. Turn your AI coding assistant into a full video production studio. *Python.*
- [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) — ★80,173 — Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens for coding agents, 60-95% fewer tokens for JSON, same answers. Library, proxy, MCP server. *Python.*
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) — ★79,900 — A curated list of awesome Claude Skills, resources, and tools for customizing Claude AI workflows. *Python.*
- [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) — ★79,611 — Learn AI Engineering! Learn it. Build it. Ship it for others. *Python.*
- [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) — ★71,975 — Leaked system prompts of ChatGPT, Claude, Gemini and more. The hidden system prompt of every popular chatbot, in full, every version since May 2025. Also Anthropic Claude Code, OpenAI Codex, Google Antigravity, xAI Grok, Meta Muse, Moonshot Kimi, Alibaba Qwen, Z.ai GLM ZCode, MiniMax, Cursor, Perplexity, DeepSeek and 30+ others. Updated daily. *Python.*
- [blader/humanizer](https://github.com/blader/humanizer) — ★71,281 — Agent skill that removes signs of AI-generated writing from text. *Python.*
- [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) — ★53,875 — The awesome collection of OpenClaw skills. 5,400+ skills filtered and categorized from the official OpenClaw Skills Registry.🦞.
- [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) — ★40,222 — Turn Claude Code into a full game dev studio — 49 AI agents, 75 workflow skills, and a complete coordination system mirroring real studio hierarchy. *Shell.*
- [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) — ★37,360 — A curated collection of 1000+ agent skills from official dev teams and the community, compatible with Claude Code, Codex, Gemini CLI, Cursor, and more.
- [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) — ★30,991 — A list of AI autonomous agents.
- [agentskills/agentskills](https://github.com/agentskills/agentskills) — ★27,465 — Specification and documentation for Agent Skills. *Python.*
- [joonspk-research/generative_agents](https://github.com/joonspk-research/generative_agents) — ★22,398 — Generative Agents: Interactive Simulacra of Human Behavior.
- [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) — ★18,749 — A toolbox of film styles made in code for Claude Code: 99 ready to use, and your own. Each style is a style prompt plus a demo film made entirely in code by Claude Opus 5.5, with no video model. By Lemomo. · 一套用代码做片的风格工具箱：99 种现成风格，也能做出你自己的. *JavaScript.*
- [rehan-remade/universal-modder](https://github.com/rehan-remade/universal-modder) — ★9,796 — Point Claude at any game. Skills, tools and the fal MCP that let Claude Code mod almost any PC game you own: recon, reverse engineering, fal-generated art/3D/audio, in-game testing, showcase videos. *Python.*
- [gamedev-skills/awesome-gamedev-agent-skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) — ★9,585 — Make games with your AI coding agent: 79 game-dev skills and a router for Godot, Unity, Unreal, Roblox, three.js, Phaser and 6 more engines. Checked on the real engines. *Python.*
- [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) — ★5,196 — Awesome list for AI agent harness engineering: tools, patterns, evals, memory, MCP, permissions, observability, and orchestration. *Python.*
- [scenario-labs/skills](https://github.com/scenario-labs/skills) — ★3,915 — Get production-ready images, video, audio, and 3D from any AI agent: skills that pick the right model, price before spending, and keep characters and brands consistent through the Scenario MCP, plus expert teams that drive Blender, Maya, ZBrush, Unreal, and Unity. *Python.*
- [reacher-z/Awesome-REA](https://github.com/reacher-z/Awesome-REA) — ★3,215 — Curated tools, case studies and papers for reverse engineering websites, games, apps, binaries, firmware and protocols. Source-reviewed, English and Chinese. *Python.*
- [EL4CTEO/blender-skills](https://github.com/EL4CTEO/blender-skills) — ★2,454 — Professional Blender 5.3 workflows as Agent Skills for Claude Code, Codex, Gemini CLI, Copilot and Cursor: modeling, UVs, PBR, baking, rigging, animation, export and QA. *Python.*
- [Moh4696/cinematic-skill](https://github.com/Moh4696/cinematic-skill) — ★810 — Agent skill for narrated cinematic films built entirely from code: one continuous camera over photos, maps and cards, timed to the voice. Claude Code, Codex, Cursor, Gemini CLI. *Python.*
- [paladini/harness-score](https://github.com/paladini/harness-score) — ★634 — Your AI coding agent is only as reliable as the harness around it. Measure that harness in seconds with harness-score. *TypeScript.*
- [eudk/awesome-ai-tools](https://github.com/eudk/awesome-ai-tools) — ★613 — 🔴 VERY LARGE AI TOOL LIST! 🔴  Curated list of AI Tools  - Updated 2026.
- [rediumvex/ai-video-generator-claude](https://github.com/rediumvex/ai-video-generator-claude) — ★492 — 10 Claude skills that generate studio-quality AI video prompts for Seedance 2.0 on Higgsfield. Viral hooks, SaaS demos, personal brand, faceless content, luxury aesthetic & more. *Python.*
- [weiwei966/awesome-ai-harness](https://github.com/weiwei966/awesome-ai-harness) — ★137 — The model is the engine; the harness is the car. Curated knowledge on harness engineering — context management, tool design, agent loops, memory, sandboxing, evals. EN/中文.
- [szprivate/agentY](https://github.com/szprivate/agentY) — ★53 — AI agent to iteratively create visual content via comfyui workflows. *Python.*
- [Bogzx/bg3-agent-harness](https://github.com/Bogzx/bg3-agent-harness) — ★35 — An AI agent plays Baldur's Gate 3 on Linux through a Lua mod and an MCP server, seeing only what a player sees. Includes a model benchmark and a playthrough app. *Python.*
- [ianwieds/awesome-ai-agents](https://github.com/ianwieds/awesome-ai-agents) — ★7 — A curated list of AI agent frameworks, coding agents, browser agents, tools, platforms and research.
- [ebluffy/agent-tool-catalog](https://github.com/ebluffy/agent-tool-catalog) — ★2 — Curated public catalog of agent/LLM tooling (skills, MCP, UI, automation). No personal projects.
- [fevziegeyurtsevenler/awesome-agent-supply-chain-security](https://github.com/fevziegeyurtsevenler/awesome-agent-supply-chain-security) — ★2 — A curated list of tools, research, standards and datasets for the security of AI agent extensions — skills, MCP servers, plugins and rules files.
- [stellartune-studio/vision-orchestrator](https://github.com/stellartune-studio/vision-orchestrator) — ★1 — No description on GitHub *TypeScript.*
- [liyangbing/awesome-harness-engineering-yenanjing](https://github.com/liyangbing/awesome-harness-engineering-yenanjing) — ★1 — A curated list of awesome harness engineering frameworks, libraries, tools and resources. 🛠️ 80+ repos covering agent harnesses, evaluation frameworks, CI/CD platforms & more.

### 3D, Animation & World Generation (41)

- [godotengine/godot](https://github.com/godotengine/godot) — ★120,440 — Godot Engine – Multi-platform 2D and 3D game engine. *C++.*
- [mrdoob/three.js](https://github.com/mrdoob/three.js) — ★118,973 — JavaScript 3D Library. *JavaScript.*
- [permissionlesstech/bitchat](https://github.com/permissionlesstech/bitchat) — ★37,188 — bluetooth mesh chat, IRC vibes. *Swift.*
- [pmndrs/react-three-fiber](https://github.com/pmndrs/react-three-fiber) — ★33,838 — 🇨🇭 A React renderer for Three.js. *TypeScript.*
- [img2threejs/img2threejs](https://github.com/img2threejs/img2threejs) — ★21,637 — Rebuild the object in a reference image as a code-only, procedural, quality-gated, animation-ready Three.js model. Token-efficient image-to-3D. *Python.*
- [aframevr/aframe](https://github.com/aframevr/aframe) — ★17,714 — :a: Web framework for building virtual reality experiences. *JavaScript.*
- [CesiumGS/cesium](https://github.com/CesiumGS/cesium) — ★15,969 — An open-source JavaScript library for world-class 3D globes and maps :earth_americas:. *JavaScript.*
- [Tencent-Hunyuan/Hunyuan3D-2](https://github.com/Tencent-Hunyuan/Hunyuan3D-2) — ★15,501 — High-Resolution 3D Assets Generation with Large Scale Hunyuan3D Diffusion Models. *Python.*
- [microsoft/TRELLIS](https://github.com/microsoft/TRELLIS) — ★14,357 — Official repo for paper "Structured 3D Latents for Scalable and Versatile 3D Generation" (CVPR'25 Spotlight). *Python.*
- [o3de/o3de](https://github.com/o3de/o3de) — ★9,892 — Open 3D Engine (O3DE) is an Apache 2.0-licensed multi-platform 3D engine that enables developers and content creators to build AAA games, cinema-quality 3D worlds, and high-fidelity simulations without any fees or commercial obligations. *C++.*
- [ashawkey/stable-dreamfusion](https://github.com/ashawkey/stable-dreamfusion) — ★8,880 — Text-to-3D & Image-to-3D & Mesh Exportation with NeRF + Diffusion. *Python.*
- [veloren/veloren](https://github.com/veloren/veloren) — ★7,705 — [mirror of https://gitlab.com/veloren/veloren] An open world, open source voxel RPG inspired by Dwarf Fortress and Cube World. This repository is a mirror. Please submit all PRs and issues on our GitLab page. *Rust.*
- [agmmnn/awesome-blender](https://github.com/agmmnn/awesome-blender) — ★7,693 — 🪐 A curated list of awesome Blender add-ons, AI/MCP tools, tutorials, and 3D resources. *TypeScript.*
- [MengTo/threeui](https://github.com/MengTo/threeui) — ★7,361 — Open-source ThreeUI Community catalog with live interactive components and complete Community source. *HTML.*
- [Coding-Solo/godot-mcp](https://github.com/Coding-Solo/godot-mcp) — ★6,711 — MCP server for interfacing with Godot game engine. Provides tools for launching the editor, running projects, and capturing debug output. *JavaScript.*
- [Tencent-Hunyuan/Hunyuan3D-2.1](https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1) — ★4,493 — From Images to High-Fidelity 3D Assets with Production-Ready PBR Material. *Python.*
- [dreamgaussian/dreamgaussian](https://github.com/dreamgaussian/dreamgaussian) — ★4,365 — [ICLR 2024 Oral] Generative Gaussian Splatting for Efficient 3D Content Creation. *Python.*
- [mromidev/claude-animated-shorts](https://github.com/mromidev/claude-animated-shorts) — ★4,259 — Free Claude skill: viral animated story shorts (2D characters in a 3D world) with three.js + Remotion. *TypeScript.*
- [AiuniAI/Unique3D](https://github.com/AiuniAI/Unique3D) — ★3,599 — [NeurIPS 2024] Unique3D: High-Quality and Efficient 3D Mesh Generation from a Single Image. *Python.*
- [mkkellogg/GaussianSplats3D](https://github.com/mkkellogg/GaussianSplats3D) — ★2,972 — Three.js-based implementation of 3D Gaussian splatting. *JavaScript.*
- [majidmanzarpour/threejs-game-skills](https://github.com/majidmanzarpour/threejs-game-skills) — ★2,859 — Agent skills for building playable, polished Three.js browser games with gameplay, AAA-style graphics, UI, QA, and optional AI-generated 3D, image, and audio assets. *Python.*
- [ooolabdev/ooosplat](https://github.com/ooolabdev/ooosplat) — ★2,570 — A local desktop app that turns videos and images into 3D Gaussian Splats in one click. *Rust.*
- [ActiveVisionLab/Awesome-LLM-3D](https://github.com/ActiveVisionLab/Awesome-LLM-3D) — ★2,283 — Awesome-LLM-3D: a curated list of Multi-modal Large Language Model in 3D world  Resources.
- [toyxyz/toyxyz_RGBMocap](https://github.com/toyxyz/toyxyz_RGBMocap) — ★2,221 — Native Windows video motion capture with ExMR, FlowHMR and GVHMR, contact correction, humanoid retargeting, and FBX/VMD export. *Python.*
- [3DTopia/LGM](https://github.com/3DTopia/LGM) — ★2,125 — [ECCV 2024 Oral] LGM: Large Multi-View Gaussian Model for High-Resolution 3D Content Creation. *Python.*
- [MaxLiu22/Motion2MixamoRig](https://github.com/MaxLiu22/Motion2MixamoRig) — ★2,038 — Retarget human motion from video to an Adobe Mixamo-rigged 3D character. *Python.*
- [Tencent-Hunyuan/Hunyuan3D-WorldClaw](https://github.com/Tencent-Hunyuan/Hunyuan3D-WorldClaw) — ★1,468 — WorldClaw: Agentic 3D Open-world Generation at Scale.
- [Bingeljell/image-to-3dlab](https://github.com/Bingeljell/image-to-3dlab) — ★1,217 — AssetFurnace: the most complete open-source image-to-3D pipeline (Oct 2026). Prompt or picture → textured, rigged, animated game character, locally on Apple Silicon or NVIDIA. Pixal3D, TRELLIS.2, Hunyuan3D, SF3D, auto-rig and 21 moves. For indie game devs and 3D artists. Free, Apache-2.0. *Python.*
- [scenario-labs/blender-plugin](https://github.com/scenario-labs/blender-plugin) — ★1,058 — Scenario for Blender: AI images, video, 3D and PBR materials in the viewport, plus a local MCP server for agents. Blender 5.0+ extension, GPL-3.0-or-later. *Python.*
- [SkyworkAI/Matrix-3D](https://github.com/SkyworkAI/Matrix-3D) — ★854 — Generate large-scale explorable 3D scenes with high-quality panorama videos from a single image or text prompt. *Python.*
- [codepawl/crucible](https://github.com/codepawl/crucible) — ★815 — 3D engine that AI agents drive. *JavaScript.*
- [islandmed/SculptForge](https://github.com/islandmed/SculptForge) — ★739 — Free, open-source 3D sculpting for Linux, macOS and Windows: dense meshes, remeshing, painting, built-in AI (image/text to 3D), Send to Unreal, game-ready LODs, Gaussian splats and OpenUSD. *C++.*
- [yyeboah/Awesome-Text-to-3D](https://github.com/yyeboah/Awesome-Text-to-3D) — ★616 — A growing curation of Text-to-3D, Diffusion-to-3D works. *TeX.*
- [canitcode/video2rig](https://github.com/canitcode/video2rig) — ★302 — No description on GitHub *Python.*
- [PxTicks/h3-motion](https://github.com/PxTicks/h3-motion) — ★159 — No description on GitHub *TypeScript.*
- [alisson-anjos/Henge](https://github.com/alisson-anjos/Henge) — ★134 — Open studio for motion transfer and video swaps with MiniMax H3 guide latents. *Python.*
- [krazyjakee/DungeonTemplateLibrary-Godot](https://github.com/krazyjakee/DungeonTemplateLibrary-Godot) — ★55 — 🌏: Godot Dungeon free resources (terrain & roguelike generation). *C++.*
- [suvadityamuk/trellis2-cuda](https://github.com/suvadityamuk/trellis2-cuda) — ★38 — TRELLIS.2 image-to-3D in pure CUDA C++: bitwise parity with PyTorch, 5.3x faster on H200. *Cuda.*
- [timscheuerai/worldsplat](https://github.com/timscheuerai/worldsplat) — ★8 — Open-source text-to-3D world generation. One command turns a text prompt into a navigable Gaussian Splat scene. An open-source alternative to World Labs Marble. *Python.*
- [metababe-eth/hero-frame-rig](https://github.com/metababe-eth/hero-frame-rig) — ★4 — Direct the focus of any clip after it's made. Open-weights, ComfyUI local or Cloud. #OpenSourceHiggsfield. *Python.*
- [junco3/motion-guard](https://github.com/junco3/motion-guard) — ★2 — Checks AI video against its 3D motion reference before an expensive upscale - ComfyUI / LTX (#OpenSourceHiggsfield). *Python.*

### Audio, Voice & Music (4)

- [sintetizacom/easycomfee](https://github.com/sintetizacom/easycomfee) — ★23 — Open-source, Higgsfield-style creative studio on ComfyUI: image, video, LTX VFX, lip sync, music and voice, on your GPU or on Comfy Cloud. Easy Windows install with a one-click model installer. *Python.*
- [Nebuluss/H3-AudioRetake-studio](https://github.com/Nebuluss/H3-AudioRetake-studio) — ★22 — A local audio and lip-sync retake studio for ComfyUI and MiniMax H3. *Python.*
- [xentome/EDITS-WITH-AI](https://github.com/xentome/EDITS-WITH-AI) — ★17 — Edits musicales con IA local: MiniMax H3 + LLM local en ComfyUI (provisional). *Python.*
- [nyghtowl/sheep-audio-dreams](https://github.com/nyghtowl/sheep-audio-dreams) — ★3 — Demo of audio agents playing D&D. *Python.*

### Video, Image & ComfyUI (107)

- [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) — ★147,681 — The most powerful and modular diffusion model GUI, api and backend with a graph/nodes interface. The fastest local inference engine in the world. *Python.*
- [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) — ★35,432 — Uncensored Open-source alternative to AI video platforms — Free AI image & video generation studio with 800+ models (Flux, Midjourney, Kling, Sora, Veo). No content filters. Self-hosted, MIT licensed. *JavaScript.*
- [pascalorg/editor](https://github.com/pascalorg/editor) — ★25,639 — Open-source 3D architecture software for AECO, scan-to-BIM. Agent-friendly, browser-first, MCP, CLI. *TypeScript.*
- [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos) — ★15,949 — A growing collection of viral videos made with Claude Opus 5.5 and the prompts behind them. Watch each original next to a live remake on Skillry. Updated regularly.
- [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) — ★9,598 — No description on GitHub *Python.*
- [teamchong/pxpipe](https://github.com/teamchong/pxpipe) — ★7,873 — cut Claude Code token usage by rendering text context as images. *TypeScript.*
- [wide-trace/open-higgsfield](https://github.com/wide-trace/open-higgsfield) — ★6,400 — A studio for image and video generation — one prompt bar, each model’s own settings, and every finished run in one gallery. *TypeScript.*
- [SegFault42/HeliosGen](https://github.com/SegFault42/HeliosGen) — ★3,432 — 🏆 Self Hosted Gen AI desktop app. Free alternative to Higgsfield, OpenArt, Freepik.... *TypeScript.*
- [Tencent-Hunyuan/HunyuanWorld-1.0](https://github.com/Tencent-Hunyuan/HunyuanWorld-1.0) — ★2,979 — Generating Immersive, Explorable, and Interactive 3D Worlds from Words or Pixels with Hunyuan3D World Model. *Python.*
- [nv-tlabs/lyra](https://github.com/nv-tlabs/lyra) — ★2,885 — Project Lyra: Open Generative 3D World Models. *Python.*
- [Tencent-Hunyuan/HY-World-2.0](https://github.com/Tencent-Hunyuan/HY-World-2.0) — ★2,884 — HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds. *Python.*
- [D3voz/openjutsu](https://github.com/D3voz/openjutsu) — ★2,500 — One-click character swap for videos: an open-source, local Higgsfield Genjutsu alternative built on ComfyUI and MiniMax H3, with FLUX.3 Klein relighting. *TypeScript.*
- [Lightricks/LTX-Desktop](https://github.com/Lightricks/LTX-Desktop) — ★2,305 — An open-source desktop app for generating videos with LTX models. *Python.*
- [ZiYang-xie/WorldGen](https://github.com/ZiYang-xie/WorldGen) — ★2,222 — 🌍 WorldGen - Generate Any 3D Scene in Seconds. *Python.*
- [Tencent-Hunyuan/HY-WorldPlay](https://github.com/Tencent-Hunyuan/HY-WorldPlay) — ★1,630 — HY-World 1.5: A Systematic Framework for Interactive World Modeling with Real-Time Latency and Geometric Consistency. *Python.*
- [neuregex/freefield](https://github.com/neuregex/freefield) — ★1,628 — Open-source Higgsfield on ComfyUI: 120 image, video, VFX and audio apps, every model open weights; runs on Modal or your own GPU. *Python.*
- [Tencent-Hunyuan/HunyuanWorld-Voyager](https://github.com/Tencent-Hunyuan/HunyuanWorld-Voyager) — ★1,610 — Voyager is an interactive RGBD video generation model conditioned on camera input, and supports real-time 3D reconstruction. *Python.*
- [microsoft/TextWorld](https://github.com/microsoft/TextWorld) — ★1,466 — ​TextWorld is a sandbox learning environment for the training and evaluation of reinforcement learning (RL) agents on text-based games. *Jupyter Notebook.*
- [Tencent-Hunyuan/HunyuanWorld-Mirror](https://github.com/Tencent-Hunyuan/HunyuanWorld-Mirror) — ★1,234 — [ICML 2026] WorldMirror: Fast and Universal 3D reconstruction model for versatile tasks. *Python.*
- [Keys-Wasserman/Imagination-Studio-by-keys-Wasserman](https://github.com/Keys-Wasserman/Imagination-Studio-by-keys-Wasserman) — ★1,195 — Imagination Studio by keys+Wasserman powered by TensorFold: an AI film studio for Mac and NVIDIA DGX Spark. Plan a film like a crew (Slate workflow by Sam Wasserman), render Qwen-Image-2.1 / FLUX3-K pictures and MiniMax H3 / FastH3 video with sound on TensorFold. *Python.*
- [imlixinyang/FlashWorld](https://github.com/imlixinyang/FlashWorld) — ★882 — Code for "FlashWorld: High-quality 3D Scene Generation within Seconds" (ICLR 2026 Oral). *Python.*
- [Tencent-Hunyuan/Hy-Nomas](https://github.com/Tencent-Hunyuan/Hy-Nomas) — ★596 — Hy-Nomas: Towards Free-form Interactive World Generation. *Python.*
- [jtydhr88/ComfyArt](https://github.com/jtydhr88/ComfyArt) — ★590 — The open-source, fully local design canvas. *TypeScript.*
- [nomadoor/ComfyUI-Panorama-Stickers](https://github.com/nomadoor/ComfyUI-Panorama-Stickers) — ★305 — No description on GitHub *JavaScript.*
- [wexloops/openfield](https://github.com/wexloops/openfield) — ★214 — Open-source studio for video, stills and 3D on your own GPU through ComfyUI. *TypeScript.*
- [Comfy-Org/comfy-openjutsu](https://github.com/Comfy-Org/comfy-openjutsu) — ★161 — A clonable Comfy character-swap app and development guide. *TypeScript.*
- [raph651/open-source-canvas](https://github.com/raph651/open-source-canvas) — ★160 — Open Source Canvas: an open-source node canvas that runs ComfyUI workflows. *TypeScript.*
- [roadmaus/ComfyUI-Continuity](https://github.com/roadmaus/ComfyUI-Continuity) — ★156 — No description on GitHub *Python.*
- [SihanXU/openworld](https://github.com/SihanXU/openworld) — ★131 — OpenWorld RPG: a pixel-art open-world RPG in the browser, with the engine and editor it is built on. The world's rules are data; a language model can add new ones at runtime. *TypeScript.*
- [jutsuhq/open-source-higgsfield](https://github.com/jutsuhq/open-source-higgsfield) — ★128 — Open-source Higgsfield AI alternatives on GitHub: 117 projects, 110 of them from ComfyUI's #OpenSourceHiggsfield challenge, with its 16 prize winners. Character swap (OPENjutsu), effects, camera re-shoots, films and full studios, with stars and licenses. CC0. *JavaScript.*
- [itsmetamike/reshoot-4d](https://github.com/itsmetamike/reshoot-4d) — ★112 — Reshoot any video in 4D. A 4D camera editor inside ComfyUI, running locally on open weights. *JavaScript.*
- [mmlong818/filmgame](https://github.com/mmlong818/filmgame) — ★111 — 面向编剧的 AI 互动影游创作系统 · AI-assisted interactive film game authoring. *TypeScript.*
- [thePloggy/CreatorOS-Studio](https://github.com/thePloggy/CreatorOS-Studio) — ★85 — Open-source Higgsfield on your own GPU: train a recurring character, turn a one-line brief into an edited reel, move the camera, re-shoot an angle, block shots in 3D, sketch to video, restore old footage. Runs on local ComfyUI, open-weights models only. *TypeScript.*
- [rk0neki/OpenKatana](https://github.com/rk0neki/OpenKatana) — ★82 — Agent-driven video editing with Studio, ComfyUI Apps, CLI and MCP. Turn photos, footage and music into finished edits. *Python.*
- [lucataco/open-source-higgsfield](https://github.com/lucataco/open-source-higgsfield) — ★78 — Same take, new cast: open-weights video character recasting on local ComfyUI with SAM 3.1, FLUX 3 Image Klein and SCAIL-2. Built for #OpenSourceHiggsfield. *Python.*
- [navarisun1982/comfyui-motion-previs-studio](https://github.com/navarisun1982/comfyui-motion-previs-studio) — ★59 — Open-source 3D camera, character & motion previs studio replacing Higgsfield 3D-Jutsu for AI video. *TypeScript.*
- [Bambushu/h3-recast](https://github.com/Bambushu/h3-recast) — ★53 — Swap up to three people in a video clip in one pass with MiniMax H3 + the BFS character swap LoRA. Keeps motion, set and audio. ComfyUI App-mode workflow.
- [chenthedesignmaker/ComfyUI-Picky](https://github.com/chenthedesignmaker/ComfyUI-Picky) — ★43 — Render it ten ways, keep the one you love. An open-weights film studio for MiniMax H3 in ComfyUI: takes, lineage, cast and an agent skill. *Python.*
- [Burgstall-labs/ComfyUI-SpEdE](https://github.com/Burgstall-labs/ComfyUI-SpEdE) — ★42 — SpEdE, the Splat Edit Engine: click an object in a Gaussian splat, then Remove, Replace or Extract it. Local ComfyUI nodes + web Studio, open weights only. #OpenSourceHiggsfield. *Python.*
- [Arfolomew/backlot](https://github.com/Arfolomew/backlot) — ★42 — The open-source Higgsfield that runs on a 16 GB card. Local open-weights video + image studio on ComfyUI, driven through the Comfy SDK. *Python.*
- [Tekholms-LW/ReAngle](https://github.com/Tekholms-LW/ReAngle) — ★26 — Open-source re-shoot: change the camera angle of any video with ComfyUI + LTX-2.5 (local 16GB or Comfy Cloud). #OpenSourceHiggsfield. *Python.*
- [jdnichollsc/seam](https://github.com/jdnichollsc/seam) — ★26 — Two shots in, one transition out. Open-source AI video transitions (smoke, water bend, whip pan) from a first and last image, rendered on your own GPU with open-weights LTX models via ComfyUI + the Comfy SDK. Web app, CLI and a AI agent plugin. *Python.*
- [leonardofrito/Directors-Cut](https://github.com/leonardofrito/Directors-Cut) — ★24 — Create locally. A local asset and REF2VA video studio for ComfyUI, powered by Qwen-Image 2.1, MiniMax H3 and the official Comfy SDK. *Python.*
- [hodgemann/mondo-music-video](https://github.com/hodgemann/mondo-music-video) — ★18 — Turn a song into a music video. Beat-aware shot planning, LLM-written prompts, local or hosted rendering, actors that dance, lip-sync and play instruments, Worlds, storyboards, and frame-exact assembly with your original audio. Agent-installable, with MCP tools and Open Actor/Prop Protocols. *Python.*
- [kubakubkub/ComfyUI_KubaNodes](https://github.com/kubakubkub/ComfyUI_KubaNodes) — ★16 — kubakub nodes for ComfyUI: projection mapping with regions, per-region diffusion, the director window, video and 3D scene tools. *Python.*
- [Zitroffi/comfyui-element-forge](https://github.com/Zitroffi/comfyui-element-forge) — ★16 — AI VFX elements for your own footage in ComfyUI: LTX-2.5 generates fire, lightning, smoke or particles; Element Forge tracks, lights and layers them into the shot. Open weights, runs locally. *Python.*
- [fixed-42/comfyui-sameface](https://github.com/fixed-42/comfyui-sameface) — ★14 — Comfyui custom node that measures where an image edit moves the parts of a face, and move them back. Open weights, runs locally. *Python.*
- [doubletwisted/ComfyUI-Spool](https://github.com/doubletwisted/ComfyUI-Spool) — ★13 — A video timeline for ComfyUI. Queue workflows per clip, review generated takes, and assemble a sequence. *JavaScript.*
- [phatstraws/freefield](https://github.com/phatstraws/freefield) — ★13 — Higgsfield-style video effects as ComfyUI workflows. Open weights, runs on your own GPU. *Python.*
- [thekhoma/pickups](https://github.com/thekhoma/pickups) — ★12 — Pickups is a free, open source video app that runs on top of ComfyUI. Pick a shot, change the weather, the lighting, or what's in the frame, and get the same shot back with just that change. Works on your own computer. *Python.*
- [MajoorWaldi/HyperKut-Studio](https://github.com/MajoorWaldi/HyperKut-Studio) — ★11 — A local ComfyUI-powered AI video studio for creating, remixing, and editing videos. Prepared for the Comfy Open Source Higgsfield challenge. *Python.*
- [dougliell/Cheapsfield](https://github.com/dougliell/Cheapsfield) — ★10 — A 100% local, 100% open-weights creative studio for Windows: Higgsfield-style apps and a node canvas on ComfyUI + Comfy SDK. Sketch to packshot, product and architecture renders, AI influencers, character swap and 1080p video with sound. No cloud, no credits. *TypeScript.*
- [NeoMarcoPolo/marcostudio](https://github.com/NeoMarcoPolo/marcostudio) — ★10 — 13 image and video tools that run on your own ComfyUI with open-weight models. Use the hosted app or run it locally. *Python.*
- [FrameDeptCo/freavy](https://github.com/FrameDeptCo/freavy) — ★9 — Free, local-first node canvas for AI image and video generation on top of ComfyUI. *TypeScript.*
- [synthetic-ape/comfield](https://github.com/synthetic-ape/comfield) — ★8 — Open-source, Higgsfield-style creative studio for AI images and video, built on the Comfy Developer Platform (Comfy Router + Comfy SDK). Cloud models or open weights on your own GPU. *TypeScript.*
- [Alvinvision/360-Scout-to-Film-Consistency](https://github.com/Alvinvision/360-Scout-to-Film-Consistency) — ★7 — Camera-controlled 360 location references and multi-shot AI video inside ComfyUI. Open Source Higgsfield submission. *Python.*
- [jhoard/open-ads-studio](https://github.com/jhoard/open-ads-studio) — ★6 — Open-weights rebuild of Higgsfield Ads Studio. Label-exact, compliance-checked product ads via ComfyUI workflows on LTX-2 and MiniMax H3. #OpenSourceHiggsfield. *TypeScript.*
- [TusharTechs/platelock](https://github.com/TusharTechs/platelock) — ★6 — Add the VFX. Keep the shot. Plate-preserving generative VFX for ComfyUI + LTX-2.3 (open weights). #OpenSourceHiggsfield. *Python.*
- [SydFloyd/openjutsu](https://github.com/SydFloyd/openjutsu) — ★6 — Open-source Higgsfield Genjutsu alternative on ComfyUI, open weights only. #OpenSourceHiggsfield. *Python.*
- [D3voz/comfyui-h3-oneclick-swap](https://github.com/D3voz/comfyui-h3-oneclick-swap) — ★6 — ComfyUI nodes for MiniMax H3 character and object swaps, tracked-person matching, Montage and face-refinement chunking. Used by Openjutsu. *Python.*
- [demoncase/kagami](https://github.com/demoncase/kagami) — ★6 — open source version of higgsfield genjutsu. *Python.*
- [ergophobian/comfyfield](https://github.com/ergophobian/comfyfield) — ★5 — No description on GitHub *JavaScript.*
- [pyoonpyoon/open-higgsfield](https://github.com/pyoonpyoon/open-higgsfield) — ★5 — Open-source Higgsfield Reshoot: a 3D virtual film set that re-shoots any photo from any angle and adds cinematic camera moves. Open weights on ComfyUI. #OpenSourceHiggsfield. *TypeScript.*
- [apsolut/one-shot-multicam](https://github.com/apsolut/one-shot-multicam) — ★5 — Multicam from one phone shot — turn a single selfie video into a multi-camera edit with ComfyUI + LTX-2.3 ID LoRA (open weights). #OpenSourceHiggsfield. *Python.*
- [EmmanuelRiveros/TimeFlight](https://github.com/EmmanuelRiveros/TimeFlight) — ★5 — Drone flights over real places that turn back time: open geodata + era geometry + depth-guided LTX-2.5 in ComfyUI. Hero: Mexico City to Tenochtitlan, 1519. *Python.*
- [chinesepowered/hack-comfy](https://github.com/chinesepowered/hack-comfy) — ★5 — No description on GitHub *Python.*
- [codyclack/opensfield](https://github.com/codyclack/opensfield) — ★5 — Open-source Higgsfield rebuilt on ComfyUI (#OpenSourceHiggsfield): 146 tools + all 83 Higgsfield apps, Cinema Studio, Elements. Open weights + partner models. 130 with real renders. MIT. *Python.*
- [rossaai/rosesfield](https://github.com/rossaai/rosesfield) — ★5 — Open-source Higgsfield alternative, built with ComfyUI. 25+ apps for image, video, audio and 3D on your own Comfy key. *TypeScript.*
- [RahmelJackson/frameforge-studio](https://github.com/RahmelJackson/frameforge-studio) — ★5 — An open-source creative studio inspired by Higgsfield, powered by ComfyUI workflows. Create images, video, audio and short films with local models or external cloud handoffs. *JavaScript.*
- [IBFolding/haggs](https://github.com/IBFolding/haggs) — ★4 — Open-source film studio on Comfy: script to screen, every shot and price in the open. Built for Comfy's #OpenSourceHiggsfield challenge. *HTML.*
- [obaidiDev/openfield](https://github.com/obaidiDev/openfield) — ★3 — The Higgsfield Blender MCP stack, modified to be local-first: self-hosted gateway so the add-on runs on your own models (ComfyUI / provider keys / local commands) — no account, no credits. *Python.*
- [crystalattice/CBI_RenderRepo](https://github.com/crystalattice/CBI_RenderRepo) — ★3 — Local-first workflow and dependency manager for ComfyUI. Discover, inspect, install, and open workflows while reusing local models and reviewing proposed changes before installation. *Python.*
- [0xMisterBailey/Boson](https://github.com/0xMisterBailey/Boson) — ★3 — Studios instead of presets: your taste as plain files in git that every next ComfyUI round obeys. *Python.*
- [vidyabharadwaj03/reelmatch](https://github.com/vidyabharadwaj03/reelmatch) — ★3 — Reelmatch: describe a campaign, drop in photos, get a UGC-style ad draft. Matches each brief to the right video model and shows why. Built for the Comfy Open Source Higgsfield build night. *Python.*
- [tysonfarrington-cmyk/xenoform](https://github.com/tysonfarrington-cmyk/xenoform) — ★3 — Song in, music video out, on your own GPU. Open weights only, through the Comfy SDK. #OpenSourceHiggsfield entry. *Python.*
- [smithysw7/openreel](https://github.com/smithysw7/openreel) — ★3 — One logline in, a character-consistent short film out. Open-source AI short-film studio rebuilt on ComfyUI — storyboard, AI casting, shots, assembled cut. Runs fully local on open weights (Z-Image Turbo + MiniMax H3). Open Source Higgsfield entry. *TypeScript.*
- [thaohienhomes/oneliner](https://github.com/thaohienhomes/oneliner) — ★3 — Oneliner: type one line, get a cinematic AI trailer. Comfy Cloud + LTX + ffmpeg.wasm. #OpenSourceHiggsfield. *TypeScript.*
- [jamiejk/earthfall](https://github.com/jamiejk/earthfall) — ★3 — A web app to make 8-10 sec videos featuring a dive from orbit to your character & place. Created with ComfyUI and 100% open models. *Python.*
- [marciano71/forkfield](https://github.com/marciano71/forkfield) — ★3 — Fork any video. Higgsfield-style effects on ComfyUI where every clip carries its own recipe. Open weights: Qwen-Image-Edit + LTX-2.5. #OpenSourceHiggsfield. *JavaScript.*
- [baney75/hildegard](https://github.com/baney75/hildegard) — ★3 — Your own AI studio on your own GPU: AI video, voice, characters and 3D, local and private. A free, open source alternative to Higgsfield and ElevenLabs, with an MCP server for your AI apps. *TypeScript.*
- [mhaihq/hana-comfy-hack](https://github.com/mhaihq/hana-comfy-hack) — ★2 — No description on GitHub *TypeScript.*
- [Soussa4535/SoulPersonEnhance](https://github.com/Soussa4535/SoulPersonEnhance) — ★2 — Enhance each person in a photo on her own, or only the ones you pick. Two custom ComfyUI nodes, open weights, 100% local. *Python.*
- [ZhuEvgeny/Character-lock-comfy](https://github.com/ZhuEvgeny/Character-lock-comfy) — ★2 — No description on GitHub *Python.*
- [moonz-1/open-ad-studio](https://github.com/moonz-1/open-ad-studio) — ★2 — Open Ad Studio — open-source AI creative agency on ComfyUI for Open Source Higgsfield. *JavaScript.*
- [DialloWill/storyboard-studio](https://github.com/DialloWill/storyboard-studio) — ★2 — Open-source rebuild of Higgsfield's Cinema Studio for music-video storyboards. Flask + ComfyUI. #OpenSourceHiggsfield. *Python.*
- [Editorenbici/leafreel](https://github.com/Editorenbici/leafreel) — ★2 — Turn any document into a narrated explainer video in 8 visual styles. Open weights, ComfyUI + Comfy SDK, two nodes, zero cloud. #OpenSourceHiggsfield. *Python.*
- [spiritform/herosjourney](https://github.com/spiritform/herosjourney) — ★2 — Generative AI Monomyth as an experience. Become someone, find your place, cross the threshold…. *JavaScript.*
- [kyungmin-cho/shot-board](https://github.com/kyungmin-cho/shot-board) — ★2 — Write one scene, get six shots. Pick a hero take and the app redraws cuts from it. Open-weight SDXL and Qwen-Image-Edit in ComfyUI via the Comfy SDK. *Python.* *(archived)*
- [LaytonGott/open-cinema](https://github.com/LaytonGott/open-cinema) — ★2 — Direct a shot, then change the lens afterwards: LTX-2 video + physically based depth of field (Open Optics ComfyUI node pack). #OpenSourceHiggsfield. *Python.*
- [norioversoul/susano](https://github.com/norioversoul/susano) — ★2 — An open-weights creative studio on ComfyUI: Openjutsu, Tsukuyomi, Cinematic and Influencer, one cast across apps. *TypeScript.*
- [parametricparadigm/ComfyUI_Parametric_Studio](https://github.com/parametricparadigm/ComfyUI_Parametric_Studio) — ★2 — Every open model. One studio. Your GPU. An open-source creative suite on ComfyUI. *Python.*
- [viriato68/open-studio-for-affinity](https://github.com/viriato68/open-studio-for-affinity) — ★1 — Free, local AI editing for Affinity, powered by ComfyUI. *Python.*
- [GiveMePrompts/crew-cut](https://github.com/GiveMePrompts/crew-cut) — ★1 — A party game that makes a movie. Phones become characters, friends direct scenes, the TV premieres the film. ComfyUI + Comfy SDK, open weights, runs on a MacBook. #OpenSourceHiggsfield. *JavaScript.*
- [Nemont3/cat-tapes](https://github.com/Nemont3/cat-tapes) — ★1 — One cat. One evening. One tape. Lofi VHS cat home videos, made locally with LTX-2.5 + ACE-Step on ComfyUI, open weights. *Python.*
- [mahdi-salmanzade/toybox-director](https://github.com/mahdi-salmanzade/toybox-director) — ★1 — Block your shot with toys on a 3D stage, then render it with open-weight LTX video in your own ComfyUI. Open-source, local-first. *TypeScript.*
- [soft-jelly/shotcheck](https://github.com/soft-jelly/shotcheck) — ★1 — CPU-only ComfyUI camera-motion checker (Comfy SDK): MATCH, MISMATCH, or honest INCONCLUSIVE. *Python.*
- [bolttmade/shot-director](https://github.com/bolttmade/shot-director) — ★1 — Free previs, then one real render: an open-source camera-move studio for Comfy workflows (presets, coverage board, A/B, reel export). Real clips labelled; the rest simulated. *Python.*
- [MVOlekhno/previz2shot](https://github.com/MVOlekhno/previz2shot) — ★1 — Blender grey playblast → FLUX.2 Klein 4B → LTX-2.5 Layout-to-Render. Open weights. #OpenSourceHiggsfield. *Python.*
- [ylchen333/comfy-dial](https://github.com/ylchen333/comfy-dial) — ★1 — for comfy's open source Higgsfield challenge. *TypeScript.*
- [audriu/fxjutsu](https://github.com/audriu/fxjutsu) — ★1 — Open-source Higgsfield-style VFX presets on your own footage, powered by LTX-2.5 on the Comfy Developer Platform. *TypeScript.*
- [designn2future/hoodsfield-ai](https://github.com/designn2future/hoodsfield-ai) — ★1 — Open-source, local-first AI film studio built on ComfyUI. Idea in, finished video out: script, images, video, lip-sync, timeline editing, upscaling and seamless study/lofi loops. Runs on your own GPU. Optional Claude assistant. *JavaScript.*
- [Niutonian/Comfyui_Darius_OS](https://github.com/Niutonian/Comfyui_Darius_OS) — ★1 — No description on GitHub *Python.*
- [MachineLearningAmateur/cinestudio](https://github.com/MachineLearningAmateur/cinestudio) — ★1 — a studio that leverages comfyui to better control scenes rendered with LTX 2.5. *Python.*
- [regiellis/utsushi](https://github.com/regiellis/utsushi) — ★1 — A video studio for your own ComfyUI, in Go: motion transfer, object swap, style, long video, and local tools. Independent; not affiliated with Comfy Org or Higgsfield. *Go.*
- [LLannnn/OSHCharacterStudio](https://github.com/LLannnn/OSHCharacterStudio) — ★1 — #OpenSourceHiggsfield  , make a comfy replace for  Genjutsu. *Python.*
- [SvetimFM/openjutsu-cat](https://github.com/SvetimFM/openjutsu-cat) — ★1 — Openjutsu-style motion transfer driven by depth performances (Kinect or any video) + an LTX cinema camera studio. ComfyUI, open weights, fully local on 8 GB VRAM. *Python.*
- [Ex8-ca/openjutsu](https://github.com/Ex8-ca/openjutsu) — ★1 — Open-source alternative to Higgsfield Genjutsu Motion Transfer — local H3 + H3 Fun ControlNet via Comfy SDK. *Python.*

### LLMs, Models, Training & Inference (10)

- [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) — ★188,108 — AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters. *Python.*
- [ollama/ollama](https://github.com/ollama/ollama) — ★187,673 — Get up and running with Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models. *Go.*
- [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) — ★145,090 — 100+ AI Agents, Agent Skills and RAG Apps - Free and Open Source. *Python.*
- [microsoft/generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners) — ★123,867 — 21 Lessons, Get Started Building with Generative AI. *Jupyter Notebook.*
- [unslothai/unsloth](https://github.com/unslothai/unsloth) — ★79,795 — Local UI to run and train LLMs and diffusion models. Supports GGUF, MLX, Qwen3.8, DeepSeek-V4.1, MiniMax-H3, Gemma 4, FLUX and more. *Python.*
- [Hannibal046/Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) — ★27,510 — Awesome-LLM: a curated list of Large Language Model.
- [uhub/awesome-llm](https://github.com/uhub/awesome-llm) — ★874 — A curated list of awesome LLM frameworks, libraries and software.
- [JAMESYJL/ShapeLLM-Omni](https://github.com/JAMESYJL/ShapeLLM-Omni) — ★583 — [NeurIPS 2025 Spotlight] A Native Multimodal LLM for 3D Generation and Understanding. *Python.*
- [monstercameron/Neural-Sight](https://github.com/monstercameron/Neural-Sight) — ★2 — A first-person browser experiment with Gaussian-splat worlds and generated screen-space weapon footage. *JavaScript.*
- [rollacode/dread-delusion-ai](https://github.com/rollacode/dread-delusion-ai) — ★1 — AI-driven LLM NPC dialogue for Dread Delusion via a CodeTerm external connector. *JavaScript.*

### Games, D&D & Reverse Engineering (64)

- [leereilly/games](https://github.com/leereilly/games) — ★25,010 — Archived — A list of games, add-ons, maps, etc. hosted on GitHub. Any genre. Any platform. Any engine. *(archived)*
- [diasurgical/DevilutionX](https://github.com/diasurgical/DevilutionX) — ★10,029 — Diablo build for modern operating systems. *C++.*
- [OpenMW/openmw](https://github.com/OpenMW/openmw) — ★6,767 — OpenMW is an open-source open-world RPG game engine that supports playing Morrowind. Main repo and issue tracker can be found here: https://gitlab.com/OpenMW/openmw/. *C++.*
- [Azgaar/Fantasy-Map-Generator](https://github.com/Azgaar/Fantasy-Map-Generator) — ★6,228 — Web application generating interactive and highly customizable maps. *TypeScript.*
- [vcmi/vcmi](https://github.com/vcmi/vcmi) — ★6,036 — Open-source engine for Heroes of Might and Magic III. *C++.*
- [ihhub/fheroes2](https://github.com/ihhub/fheroes2) — ★3,730 — fheroes2 is a recreation of Heroes of Might and Magic II game engine. *C++.*
- [Interkarma/daggerfall-unity](https://github.com/Interkarma/daggerfall-unity) — ★3,585 — Open source recreation of Daggerfall in the Unity engine. *C#.*
- [SubmitGame/awesome-decomp-games](https://github.com/SubmitGame/awesome-decomp-games) — ★3,131 — Rated, auto-refreshed list of decompiled, recompiled & reverse-engineered games: decomps, static recomps, source ports, engine remakes, browser ports. *Python.*
- [ondras/rot.js](https://github.com/ondras/rot.js) — ★2,732 — ROguelike Toolkit in JavaScript. Cool dungeon-related stuff, interactive manual, documentation, tests! *JavaScript.*
- [morluto/awesome-reverse-engineering](https://github.com/morluto/awesome-reverse-engineering) — ★2,237 — Curated reverse-engineering tools and learning resources for binaries, apps, firmware, formats, and protocols. *Python.*
- [evennia/evennia](https://github.com/evennia/evennia) — ★2,123 — Python MUD/MUX/MUSH/MU* development system. *Python.*
- [alexgaoth/awesome-reverse-engineered](https://github.com/alexgaoth/awesome-reverse-engineered) — ★1,466 — Don't reverse engineer it twice. 17,000+ open-source tools built by reverse engineering closed apps, APIs, devices, protocols, file formats, games and AI tools. Search site + agent skill + MCP server, refreshed nightly. *Python.*
- [OpenDCAI/GameFactory-3A](https://github.com/OpenDCAI/GameFactory-3A) — ★1,337 — A comprehensive open-source 3A game-generation skill and asset framework. *Python.*
- [flareteam/flare-engine](https://github.com/flareteam/flare-engine) — ★1,312 — Free/Libre Action Roleplaying Engine (engine only). *C++.*
- [gemrb/gemrb](https://github.com/gemrb/gemrb) — ★1,272 — GemRB is a portable open-source implementation of Bioware’s Infinity Engine. *C++.*
- [xoreos/xoreos](https://github.com/xoreos/xoreos) — ★1,198 — A reimplementation of BioWare's Aurora engine (and derivatives). Pre-pre-alpha :P. *C++.*
- [arx/ArxLibertatis](https://github.com/arx/ArxLibertatis) — ★1,121 — Cross-platform port of Arx Fatalis, a first-person role-playing game. *C++.*
- [AnyRPG/AnyRPGCore](https://github.com/AnyRPG/AnyRPGCore) — ★1,038 — Open source Role Playing Game engine for Unity 3D written in C#. *C#.*
- [RPTools/maptool](https://github.com/RPTools/maptool) — ★935 — Virtual Tabletop for playing roleplaying games with remote players or face to face. *Java.*
- [mak-kirkland/chronicler](https://github.com/mak-kirkland/chronicler) — ★745 — Chronicler is a free, offline worldbuilding tool and local wiki for writers, game masters, and tabletop RPG creators. It saves your notes as plain Markdown files on your computer. No sign-up, no subscription, no cloud. Your world stays on your device. *Svelte.*
- [delmarle/RPG-Core](https://github.com/delmarle/RPG-Core) — ★732 — UNITY engine RPG framework. *C#.*
- [HotpotDesign/Game-Assets-And-Resources](https://github.com/HotpotDesign/Game-Assets-And-Resources) — ★730 — Free and paid game assets and game resources for 2D games, 3D games,  mobile games, Steam games, Unity games, and other games.
- [Miserlou/dnd-tldr](https://github.com/Miserlou/dnd-tldr) — ★687 — Dungeons and Dragons - Too Long; Didn't Read.
- [dfabulich/choicescript](https://github.com/dfabulich/choicescript) — ★464 — ChoiceScript is a language for developing multiple-choice games. *JavaScript.*
- [p-e-w/waidrin](https://github.com/p-e-w/waidrin) — ★396 — Next-generation AI roleplay system. *TypeScript.*
- [MinLL/SkyrimNet-GamePlugin](https://github.com/MinLL/SkyrimNet-GamePlugin) — ★385 — AI NPCs for Skyrim that talk, remember, react and act, voiced in real time. By Fateless. *Papyrus.*
- [Zireael07/awesome-tabletop-rpgs](https://github.com/Zireael07/awesome-tabletop-rpgs) — ★313 — Awesome list of free and/or open source tabletop RPGs.
- [flamableconcrete/awesome-dnd](https://github.com/flamableconcrete/awesome-dnd) — ★308 — Resources for Dungeons & Dragons.
- [blendi-remade/interdimensional-game](https://github.com/blendi-remade/interdimensional-game) — ★255 — Create your own adventure with realtime video! *TypeScript.*
- [davemoore22/sorcery](https://github.com/davemoore22/sorcery) — ★251 — An open source remake/remaster of the classic CRPG Wizardry, Proving Grounds of the Mad Overlord. *C++.*
- [opendnd/opendnd](https://github.com/opendnd/opendnd) — ★206 — This is the main collection of OpenDnD Tools with generators for persons, dynasties, cities, towns, and more. *JavaScript.*
- [fvtt-fria-ligan/forbidden-lands-foundry-vtt](https://github.com/fvtt-fria-ligan/forbidden-lands-foundry-vtt) — ★205 — This is a Forbidden Lands game System for the Foundry Virtual Tabletop. Made by @Perfectro, @patrys and @aMediocreDad. Maintained by @Cussa. *JavaScript.*
- [metavert-io/lofp](https://github.com/metavert-io/lofp) — ★186 — Legends of Future Past, the classic commercial MUD form the 1990's. *HTML.*
- [ChessMax/awesome-game-engines](https://github.com/ChessMax/awesome-game-engines) — ★164 — The list of awesome game engines for everything😎. *Markdown.*
- [bernardosulzbach/dungeon](https://github.com/bernardosulzbach/dungeon) — ★153 — Text-based open-world RPG made with Java. *Java.*
- [envy-ai/ai_rpg](https://github.com/envy-ai/ai_rpg) — ★153 — No description on GitHub *JavaScript.*
- [vorpalhex/srd_spells](https://github.com/vorpalhex/srd_spells) — ★147 — A JSON formatted list of all the spells from the 5e SRD. *HTML.* *(archived)*
- [mudcoders/awesome-mud](https://github.com/mudcoders/awesome-mud) — ★147 — 🖥 A curated list of bookmarks, tools, tutorials, and other cool resources for text-based game developers.
- [bryancasler/Bryans-Preferred-Modules-for-FoundryVTT](https://github.com/bryancasler/Bryans-Preferred-Modules-for-FoundryVTT) — ★142 — My personally cultivated list of FoundryVTT Modules for Dungeons and Dragons 5e and Pathfinder 2e that play nicely together without creating an overwhelming amount of UI options or causing noticeable FPS drops. *CSS.*
- [downfallx/dnd-5e-srd-markdown](https://github.com/downfallx/dnd-5e-srd-markdown) — ★112 — D&D 5e (2024) SRD 5.2.1 in Markdown - Complete 5th Edition reference with all classes, 500+ spells, 400+ monsters. Perfect for character builders, VTTs, and D&D apps.
- [Dominowood371/Pixel-Dungeon](https://github.com/Dominowood371/Pixel-Dungeon) — ★102 — List of mods from the game Pixel Dungeon.
- [princeton-nlp/calm-textgame](https://github.com/princeton-nlp/calm-textgame) — ★76 — [EMNLP 2020] Keep CALM and Explore: Language Models for Action Generation in Text-based Games. *Python.*
- [thomascgray/fantasy-content-generator](https://github.com/thomascgray/fantasy-content-generator) — ★69 — Generate D&D 5E-flavoured fantasy content for your app, video game, website, etc. *TypeScript.*
- [iliak/dungeoneye](https://github.com/iliak/dungeoneye) — ★52 — Dungeon Eye is an open source remake of Eye of the beholder II. *C#.*
- [mrlegowatch/RolePlayingCore](https://github.com/mrlegowatch/RolePlayingCore) — ★40 — A Swift package for tabletop RPG character logic: species, classes, backgrounds, feats, ability scores, skills, spells, equipment and currency, loaded from JSON game data. Example data follows the SRD 5.2.1. Includes a SwiftUI character builder app for iOS and macOS. Built on SwiftDice. *Swift.*
- [heaven-hm/awesome-reverse-engineered-games](https://github.com/heaven-hm/awesome-reverse-engineered-games) — ★36 — A curated list and comprehensive guide of awesome reverse-engineered, decompiled, and rebuilt games powered by AI models and agentic tools.
- [Coffee-fueled-deadlines/PyDnD](https://github.com/Coffee-fueled-deadlines/PyDnD) — ★35 — PyDnD is a Dungeons and Dragons SRD Library for Python3. *Python.*
- [quantavil/awesome-android-games](https://github.com/quantavil/awesome-android-games) — ★32 — 🎮 A curated directory of awesome open-source Android games, engines, and codebases with automated live stats. *Python.*
- [kupka/libsrd5](https://github.com/kupka/libsrd5) — ★24 — A System Reference Document 5.1 (SRD) Implementation in C#. *C#.*
- [s-macke/weltendaemmerung](https://github.com/s-macke/weltendaemmerung) — ★21 — Guide to reverse engineer an old computer game with AI and port it to the web. *Assembly.*
- [ObsidianTTRPGProject/Obsidian-TTRPG-Atlas](https://github.com/ObsidianTTRPGProject/Obsidian-TTRPG-Atlas) — ★18 — Repository containing scripts to convert common ttrpg wiki sites to markdown. *Python.*
- [oldmanumby/dnd.srd.5.2.1](https://github.com/oldmanumby/dnd.srd.5.2.1) — ★15 — Dungeons & Dragons 5th Edition (2024) SRD v5.2.1 converted to Markdown.
- [MSanteler/5e-Tools](https://github.com/MSanteler/5e-Tools) — ★12 — A site dedicated to making playing games with your friends as easy as possible. *JavaScript.*
- [agluszak/wizardry-8-decomp](https://github.com/agluszak/wizardry-8-decomp) — ★8 — Faithful source reconstruction of Wizardry 8 (2001) from the original Windows binaries. *C++.*
- [24-ang/earth-0](https://github.com/24-ang/earth-0) — ★5 — The engine owns the physics, LLMs own the stories: A deterministic RPG engine + multi-agent runtime for decentralized AI roleplay. *TypeScript.*
- [azemoning/omni-5e](https://github.com/azemoning/omni-5e) — ★4 — REST API + CLI for the D&D 5e System Reference Document — complete SRD 5.2.1 as structured, queryable JSON. *Go.*
- [DangerBlack/dnd-5-2024-json](https://github.com/DangerBlack/dnd-5-2024-json) — ★3 — Some json of dungeons & dragons 2024 material.
- [bigerbigernerd/awesome-open-games](https://github.com/bigerbigernerd/awesome-open-games) — ★2 — 🎮 A curated collection of open-source games you can actually play, plus engines, frameworks, tutorials, and free assets to build your own.
- [h1994st/chromatron-remake](https://github.com/h1994st/chromatron-remake) — ★2 — Native Apple Silicon macOS remake, in Rust, of Sean Barrett's Chromatron 1–4 laser puzzle games. *Rust.*
- [nooikko/post-map](https://github.com/nooikko/post-map) — ★1 — An interactive map of Faerûn for tabletop D&D — pan and zoom a tiled 3rd-edition map, find any of 297 marked places, measure travel distances, and read that place's Forgotten Realms Wiki article without leaving the map. *TypeScript.*
- [bradleynelson/elf-name-generator](https://github.com/bradleynelson/elf-name-generator) — ★1 — High Elf name generator with authentic Espruar linguistics from D&D Forgotten Realms. *JavaScript.*
- [1ojn/awesome-rpg-resources](https://github.com/1ojn/awesome-rpg-resources) — ★1 — No description on GitHub
- [tannercyost/dnd-vtt](https://github.com/tannercyost/dnd-vtt) — ★1 — An open source virtual tabletop for DND via mostly serverless p2p connections. *TypeScript.*
- [Kamalesh-Kavin/dnd-vtt](https://github.com/Kamalesh-Kavin/dnd-vtt) — ★1 — D&D Virtual Tabletop — play D&D online with friends. Procedural dungeons, combat, fog of war, AI DM. *JavaScript.*

### Data, RAG, Memory & Search (3)

- [trimstray/the-book-of-secret-knowledge](https://github.com/trimstray/the-book-of-secret-knowledge) — ★259,777 — A collection of inspiring lists, manuals, cheatsheets, blogs, hacks, one-liners, cli/web tools and more.
- [facebookresearch/map-anything](https://github.com/facebookresearch/map-anything) — ★3,916 — MapAnything: Universal Feed-Forward Metric 3D Reconstruction. *Python.*
- [bennyschmidt/ragdoll-studio](https://github.com/bennyschmidt/ragdoll-studio) — ★193 — The creative suite for character-driven AI experiences. *Python.* *(archived)*

### Automation, Web & Apps (8)

- [awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted) — ★338,705 — A list of Free Software network services and web applications which can be hosted on your own servers.
- [klembot/twinejs](https://github.com/klembot/twinejs) — ★2,957 — Twine, a tool for telling interactive, nonlinear stories. *TypeScript.*
- [5e-bits/5e-srd-api](https://github.com/5e-bits/5e-srd-api) — ★653 — REST API to access D&D 5th Edition SRD database. *TypeScript.*
- [BeatAPI/BeatDesign](https://github.com/BeatAPI/BeatDesign) — ★369 — Local-first AI canvas and timeline. Any MCP agent. Open-source alternative to Higgsfield. *TypeScript.*
- [HomoLapis/justae-flow](https://github.com/HomoLapis/justae-flow) — ★7 — ComfyUI inside the open-source EffectCraft. Your workflows, any model, on your timeline. *TypeScript.*
- [okkazoo/MOTNGRFX](https://github.com/okkazoo/MOTNGRFX) — ★4 — Open-weights kinetic-type motion graphics: a ComfyUI node pack + browser app (Gemma 4, LTX 2.5, ACE-Step, MOSS). *Python.*
- [welski3/framecommander](https://github.com/welski3/framecommander) — ★2 — Runninghub H3 Wrapper. *JavaScript.*
- [jk-automations/urban-cuts](https://github.com/jk-automations/urban-cuts) — ★2 — Open-source ComfyUI App Mode clone of Higgsfield Urban Cuts: photo + outfits/products + music -> beat-cut looping 9:16 reel. *Python.*

### Everything Else (18)

- [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) — ★563,964 — Master programming by recreating your favorite technologies from scratch. *Markdown.*
- [vinta/awesome-python](https://github.com/vinta/awesome-python) — ★335,915 — The definitive list that answers "I want to do X in Python, which tool should I use?". *Python.*
- [storytold/craft-anything](https://github.com/storytold/craft-anything) — ★38,542 — Craft Anything: understand how any software works, and craft your own. *Rust.*
- [a16z-infra/ai-town](https://github.com/a16z-infra/ai-town) — ★10,832 — A MIT-licensed, deployable starter kit for building and customizing your own version of AI town - a virtual town where AI characters live, chat and socialize. *TypeScript.*
- [inkle/ink](https://github.com/inkle/ink) — ★5,026 — inkle's open source scripting language for writing interactive narrative. *C#.*
- [galaxykate/tracery](https://github.com/galaxykate/tracery) — ★2,221 — Tracery: a story-grammar generation library for javascript. *JavaScript.*
- [5etools-mirror-3/5etools-src](https://github.com/5etools-mirror-3/5etools-src) — ★559 — A mirror. *JavaScript.*
- [5etools-mirror-3/5etools-img](https://github.com/5etools-mirror-3/5etools-img) — ★90 — A mirror. *Dockerfile.*
- [mstan/TombaRecomp](https://github.com/mstan/TombaRecomp) — ★84 — Tomba! (USA) recompiled for the Sony PlayStation using psxrecomp · Part of the R.A.I.D. community. *Python.*
- [abeiro/HerikaServer](https://github.com/abeiro/HerikaServer) — ★40 — No description on GitHub *PLpgSQL.*
- [lvsas/OpenJutsuStudio](https://github.com/lvsas/OpenJutsuStudio) — ★19 — No description on GitHub *Python.*
- [bgstratt/seriesmith](https://github.com/bgstratt/seriesmith) — ★7 — No description on GitHub *Python.*
- [geospatial-grimoire/forgotten-realms-wiki-parser](https://github.com/geospatial-grimoire/forgotten-realms-wiki-parser) — ★4 — A script to parse the Forgotten Realms Wiki XML dump into a single, clean Markdown file. *Python.*
- [Kainotomic/one-take-vfx](https://github.com/Kainotomic/one-take-vfx) — ★3 — No description on GitHub *Python.*
- [Orazen/conjure](https://github.com/Orazen/conjure) — ★2 — No description on GitHub *TypeScript.*
- [fetchloom/OpenJutsu](https://github.com/fetchloom/OpenJutsu) — ★2 — No description on GitHub *JavaScript.*
- [Dwemer-Dynamics/DwemerDynamics](https://github.com/Dwemer-Dynamics/DwemerDynamics) — ★1 — Main Website. *HTML.*
- [dibiccari/ai-vtt](https://github.com/dibiccari/ai-vtt) — ★1 — No description on GitHub *JavaScript.*

## License

This repository is a directory of links to third-party tools.

The list itself (README.md, TOOLS.md, data/starred.json, and the selection/organization of links) is released under CC0 1.0 Universal (public domain dedication).

Linked tools are NOT covered by this license. Each keeps its own license — open-source, free-tier, or commercial — as noted per entry where known.
