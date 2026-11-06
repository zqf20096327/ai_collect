# ⚡ Awesome Free AI APIs

<div align="center">

![Awesome Free AI APIs Banner](assets/banner.png)

[![Awesome](https://awesome.re/badge.svg)](https://github.com/sindresorhus/awesome)
[![Free APIs](https://img.shields.io/badge/Free%20APIs-180%2B-blueviolet.svg?style=flat-square&logo=openai)](https://github.com/itismemuhammadali/Awesome-Free-AI-APIs)
[![No Credit Card](https://img.shields.io/badge/No%20Credit%20Card-125%2B-brightgreen.svg?style=flat-square&logo=shield)](https://github.com/itismemuhammadali/Awesome-Free-AI-APIs)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-green.svg?style=flat-square)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/itismemuhammadali/Awesome-Free-AI-APIs?style=flat-square&logo=github)](https://github.com/itismemuhammadali/Awesome-Free-AI-APIs/stargazers)
[![Maintained By](https://img.shields.io/badge/Maintained%20by-@itismemuhammadali-orange.svg?style=flat-square&logo=github)](https://github.com/itismemuhammadali)

**The definitive, community-curated directory of 180+ AI APIs offering 100% Free Tiers, Free Credits, or Generous Developer Sandboxes.**  
*Save hundreds of dollars in API bills. Build side projects, hackathon MVPs, multi-agent frameworks, and AI workflows for $0.00.*

[🌐 Live Directory](https://github.com/itismemuhammadali/Awesome-Free-AI-APIs) • [🧪 Test Your Keys CLI](test_keys.py) • [🤝 Contributing Guide](CONTRIBUTING.md) • [⭐ Star on GitHub](https://github.com/itismemuhammadali/Awesome-Free-AI-APIs)

---

</div>

## 📌 Why This Repository Exists

Most developers give up on building AI prototypes because commercial API fees (OpenAI, Anthropic) pile up, or billing engines enforce upfront credit cards with accidental overage charges.

However, the competition in AI hardware and inference is fierce: **companies now give away high-speed GPU and NPU inference for free** to build developer mindshare. 

This repository catalogs **180+ verified platforms** offering free developer access across LLMs, Unified Gateways, Voice/Speech, Vision/Image, Vector Databases, Web Scraping, Code Assistants, Document AI, and Video/3D.

---

## 🗂️ Table of Contents

- [⚡ Top 10 Must-Have Free AI APIs](#-top-10-must-have-free-ai-apis)
- [🤖 1. LLMs & Multi-Modal Foundation Models (50+ Platforms)](#-1-llms--multi-modal-foundation-models)
- [🔀 2. Unified Routers & API Gateways (15+ Platforms)](#-2-unified-routers--api-gateways)
- [🎨 3. Image Generation & Computer Vision (25+ Platforms)](#-3-image-generation--computer-vision)
- [🎙️ 4. Voice, Audio, Speech-to-Text & TTS (20+ Platforms)](#-4-voice-audio-speech-to-text--tts)
- [🧠 5. Embeddings & Vector Databases (15+ Platforms)](#-5-embeddings--vector-databases)
- [🔍 6. Web Search, RAG & AI Web Scraping (15+ Platforms)](#-6-web-search-rag--ai-web-scraping)
- [💻 7. Code Intelligence & Developer AI (15+ Platforms)](#-7-code-intelligence--developer-ai)
- [📄 8. Document AI, OCR & PDF Parsing (12+ Platforms)](#-8-document-ai-ocr--pdf-parsing)
- [🎬 9. Video & 3D Model Generation (10+ Platforms)](#-9-video--3d-model-generation)
- [🎵 10. Music & Sound FX Generation (8+ Platforms)](#-10-music--sound-fx-generation)
- [📊 11. LLM Observability, Evaluation & Guardrails (12+ Platforms)](#-11-llm-observability-evaluation--guardrails)
- [🚀 Quickstart: Call Free AI APIs in 5 Lines of Python](#-quickstart-call-free-ai-apis-in-5-lines-of-python)
- [🧪 CLI Key Tester Utility](#-cli-key-tester-utility)
- [🤝 Contributing & Adding New APIs](#-contributing)
- [📜 License & Disclaimer](#-license)

---

## ⚡ Top 10 Must-Have Free AI APIs

If you only set up 5 accounts today, pick these:

| Provider | Highlight Feature | Free Tier Allowance | CC Req? | Signup Link |
| :--- | :--- | :--- | :---: | :--- |
| **[Google AI Studio](https://aistudio.google.com/)** | Gemini 1.5 Pro / Flash (2M token context window) | 15 RPM / 1,500 RPD / 1M TPM | ❌ No | [Get Free Key](https://aistudio.google.com/app/apikey) |
| **[Groq Cloud](https://console.groq.com/)** | Ultra-fast LPU inference (Llama 3.3 70B, Mixtral) | 30 RPM / 14,400 RPD / 6,000 TPM | ❌ No | [Get Free Key](https://console.groq.com/keys) |
| **[Cerebras Cloud](https://cloud.cerebras.ai/)** | World-record speed (2,000+ tokens/sec on Llama 3.1 8B/70B) | 30 RPM / 1M tokens/day | ❌ No | [Get Free Key](https://cloud.cerebras.ai/) |
| **[OpenRouter](https://openrouter.ai/)** | Access 40+ free models with 1 unified API key | Unlimited requests to `:free` models | ❌ No | [Get Free Key](https://openrouter.ai/keys) |
| **[GitHub Models](https://github.com/marketplace/models)** | GPT-4o, Claude 3.5 Sonnet, Llama 3.3 directly via GitHub PAT | Free developer tier | ❌ No | [Get Free Access](https://github.com/marketplace/models) |
| **[Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/)** | 100+ serverless models on Cloudflare edge | 10,000 Neurons/day (~free inference) | ❌ No | [Get Free Access](https://dash.cloudflare.com/) |
| **[Hugging Face Serverless](https://huggingface.co/inference-api)** | Thousands of open-source models via HTTP | Generous rate-limited free inference | ❌ No | [Get Free Key](https://huggingface.co/settings/tokens) |
| **[Mistral AI La Plateforme](https://console.mistral.ai/)** | Mistral Small, Codestral, Pixtral | 1 RPS rate-limited free experimentation | ❌ No | [Get Free Key](https://console.mistral.ai/api-keys/) |
| **[Deepgram](https://deepgram.com/)** | Nova-2 realtime Speech-to-Text & Aura TTS | $200 free credit on signup | ❌ No | [Get Free Key](https://console.deepgram.com/signup) |
| **[Tavily AI](https://tavily.com/)** | Clean, hallucination-free search results for RAG & Agents | 1,000 free search queries/month | ❌ No | [Get Free Key](https://app.tavily.com/sign-in) |

---

## 🤖 1. LLMs & Multi-Modal Foundation Models

Platforms delivering chat completions, reasoning models, and multi-modal vision APIs.

| Provider | Top Models Available | Free Tier Limits | CC Required? | Get API Key |
| :--- | :--- | :--- | :---: | :--- |
| **[Google AI Studio](https://aistudio.google.com/)** | Gemini 1.5 Pro, Gemini 1.5 Flash, Gemini Flash 8B | 15 RPM / 1,500 RPD / 1M TPM | ❌ No | [Console](https://aistudio.google.com/app/apikey) |
| **[Groq Cloud](https://console.groq.com/)** | Llama 3.3 70B, Llama 3.1 8B, Gemma 2 9B, Whisper Large v3 | 30 RPM / 14,400 RPD / 6k TPM | ❌ No | [Console](https://console.groq.com/keys) |
| **[Cerebras Inference](https://cloud.cerebras.ai/)** | Llama 3.1 8B & 70B, Llama 3.3 70B | 30 RPM / 1,000,000 tokens/day | ❌ No | [Console](https://cloud.cerebras.ai/) |
| **[SambaNova Cloud](https://cloud.sambanova.ai/)** | Llama 3.3 70B, Llama 3.1 405B, Qwen 2.5 72B | Generous developer free tier | ❌ No | [Console](https://cloud.sambanova.ai/) |
| **[GitHub Models](https://github.com/marketplace/models)** | GPT-4o, GPT-4o-mini, Llama 3.3, Phi-4, Mistral Large | Rate-limited developer tier via GitHub PAT | ❌ No | [Console](https://github.com/marketplace/models) |
| **[Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai/)** | Llama 3.3 70B, DeepSeek R1 Distill, Qwen 2.5, Whisper | 10,000 Neurons/day free forever | ❌ No | [Console](https://dash.cloudflare.com/) |
| **[Hugging Face Serverless](https://huggingface.co/docs/api-inference)** | 100,000+ open weights models on demand | Rate limited free inference endpoints | ❌ No | [Console](https://huggingface.co/settings/tokens) |
| **[Together AI](https://www.together.ai/)** | Llama 3.3, Mixtral, Qwen 2.5, DeepSeek | $5.00 free credit on signup | ❌ No | [Console](https://api.together.xyz/settings/api-keys) |
| **[Mistral AI](https://console.mistral.ai/)** | Mistral Small, Codestral 2501, Pixtral 12B | 1 request/sec free experimentation tier | ❌ No | [Console](https://console.mistral.ai/api-keys/) |
| **[DeepSeek Platform](https://platform.deepseek.com/)** | DeepSeek V3, DeepSeek R1 Reasoning | Millions of free tokens upon account creation | ❌ No | [Console](https://platform.deepseek.com/api_keys) |
| **[Cohere](https://cohere.com/)** | Command R+, Command R, Embed v3, Rerank | 100 free API calls/minute trial key | ❌ No | [Console](https://dashboard.cohere.com/api-keys) |
| **[SiliconFlow](https://siliconflow.cn/)** | DeepSeek R1, DeepSeek V3, Qwen 2.5, Flux | 20M+ free tokens on registration | ❌ No | [Console](https://cloud.siliconflow.cn/) |
| **[Novita AI](https://novita.ai/)** | Llama 3.3 70B, DeepSeek R1, Mistral, SDXL | $0.50 free trial credits | ❌ No | [Console](https://novita.ai/dashboard) |
| **[Fireworks AI](https://fireworks.ai/)** | Llama 3.3 70B, Qwen 2.5, Mixtral MoE | $1.00 free credit | ❌ No | [Console](https://fireworks.ai/account/api-keys) |
| **[Lepton AI](https://www.lepton.ai/)** | Llama 3.1, Mixtral 8x7B, Whisper | $10 free credits for developers | ❌ No | [Console](https://dashboard.lepton.ai/) |
| **[Scaleway Generative APIs](https://labs.scaleway.com/)** | Llama 3.1, Mistral NeMo, Qwen 2.5 | Free beta quota for European cloud users | ❌ No | [Console](https://console.scaleway.com/) |
| **[AI21 Labs](https://studio.ai21.com/)** | Jamba 1.5 Large, Jamba 1.5 Mini (SSM-Transformer) | $10 free credit for 3 months | ❌ No | [Console](https://studio.ai21.com/account/api-key) |
| **[Replicate](https://replicate.com/)** | Thousands of open-source models (LLMs, Audio, Image) | Free community run budget on initial sign in | ❌ No | [Console](https://replicate.com/account/api-tokens) |
| **[DeepInfra](https://deepinfra.com/)** | Llama 3.3 70B, Qwen 2.5 Coder, Whisper | $1.80 free starting balance | ❌ No | [Console](https://deepinfra.com/dash/api_keys) |
| **[Baseten](https://www.baseten.co/)** | Open source model serverless deployments | $30 free credits for new accounts | ❌ No | [Console](https://app.baseten.co/settings/api_keys) |
| **[Modal Labs](https://modal.com/)** | Run custom vLLM / SGLang inference on H100s | $30/month recurring free credit tier | ❌ No | [Console](https://modal.com/settings) |
| **[RunPod Serverless](https://www.runpod.io/)** | Serverless endpoints for vLLM & open LLMs | Free starting credits for testing | ❌ No | [Console](https://www.runpod.io/console/serverless) |
| **[Hyperbolic](https://hyperbolic.xyz/)** | Llama 3.3 70B, DeepSeek R1, Qwen 2.5 | Free developer tier on decentralized compute | ❌ No | [Console](https://app.hyperbolic.xyz/) |
| **[Nebius AI Studio](https://nebius.com/studio)** | DeepSeek R1, Llama 3.3, Qwen 2.5, Mistral | Free trial credits for inference | ❌ No | [Console](https://studio.nebius.com/) |
| **[Inference.net](https://inference.net/)** | Fast Llama 3.1 and Mistral endpoints | Free community tier | ❌ No | [Console](https://inference.net/) |
| **[Upstage Solar](https://console.upstage.ai/)** | Solar 10.7B, Document OCR LLMs | $10 free API credits upon signup | ❌ No | [Console](https://console.upstage.ai/) |
| **[Writer AI](https://dev.writer.com/)** | Palmyra-Med, Palmyra-Creative enterprise models | Free trial tier with developer playground | ❌ No | [Console](https://dev.writer.com/) |
| **[FriendliAI](https://friendli.ai/)** | High-throughput Llama & Mistral inference | $5 free trial credits | ❌ No | [Console](https://friendli.ai/) |
| **[MonsterAPI](https://monsterapi.ai/)** | Fine-tuned LLMs, Whisper, SDXL | Free credits on signup | ❌ No | [Console](https://monsterapi.ai/signup) |
| **[Perplexity AI (Playground)](https://www.perplexity.ai/)** | Sonar, Sonar Pro, Online Search LLMs | Free web-interactive testing sandbox | ❌ No | [Console](https://www.perplexity.ai/) |
| **[Voyage AI](https://www.voyageai.com/)** | SOTA embedding models & re-ranking | 200,000,000 free tokens for developers | ❌ No | [Console](https://dash.voyageai.com/api-keys) |
| **[Aleph Alpha](https://aleph-alpha.com/)** | Luminous-Supreme, Luminous-Extended | Free developer playground evaluation | ❌ No | [Console](https://aleph-alpha.com/) |
| **[01.AI (Yi Models)](https://platform.01.ai/)** | Yi-Lightning, Yi-34B, Yi-Vision | Free signup tokens for developers | ❌ No | [Console](https://platform.01.ai/) |
| **[Moonshot AI (Kimi)](https://platform.moonshot.cn/)** | Kimi 128k long context LLM | 15 free tokens / credits on verification | ❌ No | [Console](https://platform.moonshot.cn/) |
| **[Zhipu AI (GLM-4)](https://open.bigmodel.cn/)** | GLM-4-Flash, GLM-4V, CodeGeeX | GLM-4-Flash is 100% free with unlimited API calls | ❌ No | [Console](https://open.bigmodel.cn/) |
| **[Baichuan AI](https://platform.baichuan-ai.com/)** | Baichuan 4, Baichuan 3 Turbo | Free developer quota on verification | ❌ No | [Console](https://platform.baichuan-ai.com/) |
| **[StepFun (Step-1)](https://platform.stepfun.com/)** | Step-1V Multi-modal, Step-2 LLM | Free developer credits | ❌ No | [Console](https://platform.stepfun.com/) |
| **[MiniMax](https://api.minimax.chat/)** | MiniMax-Text-01, Hailuo Video | Free starter credits on phone/email verify | ❌ No | [Console](https://api.minimax.chat/) |
| **[DeepL API](https://www.deepl.com/pro-api)** | DeepL AI Neural Translation | 500,000 characters/month free forever | ❌ No | [Console](https://www.deepl.com/pro-api) |
| **[NLP Cloud](https://nlpcloud.com/)** | Llama 3, Dolphin, spaCy NLP endpoints | 1 free request every 2 seconds forever | ❌ No | [Console](https://nlpcloud.com/) |
| **[GooseAI](https://goose.ai/)** | GPT-NeoX, Fairseq, Pythia | $0.25 free testing credits | ❌ No | [Console](https://goose.ai/) |
| **[Anyscale Endpoints](https://www.anyscale.com/)** | Ray-based distributed open LLMs | Free starting credits for developers | ❌ No | [Console](https://www.anyscale.com/endpoints) |
| **[Petals](https://petals.dev/)** | Distributed P2P Llama 3.1 70B & 405B | 100% Free decentralized community network | ❌ No | [Console](https://petals.dev/) |
| **[Ollama + Cloudflare Tunnel](https://ollama.com/)** | Self-hosted Llama, Qwen, DeepSeek on your laptop | 100% Free, infinite tokens, zero cost | ❌ No | [Download](https://ollama.com/) |
| **[LM Studio](https://lmstudio.ai/)** | Local OpenAI-compatible REST server | 100% Free, offline local inference | ❌ No | [Download](https://lmstudio.ai/) |
| **[vLLM](https://vllm.ai/)** | High-throughput open-source serving engine | 100% Free open-source local server | ❌ No | [Docs](https://docs.vllm.ai/) |
| **[Jan.ai](https://jan.ai/)** | Open-source alternative to ChatGPT running locally | 100% Free local server with OpenAI API compatibility | ❌ No | [Download](https://jan.ai/) |
| **[LocalAI](https://localai.io/)** | Drop-in OpenAI alternative for CPU and GPU | 100% Free open-source REST API | ❌ No | [Docs](https://localai.io/) |

---

## 🔀 2. Unified Routers & API Gateways

One API key to switch dynamically between 100+ providers with automatic failover, load balancing, and free fallback tiers.

| Provider | Core Capabilities | Free Tier Limits | CC Req? | Signup Link |
| :--- | :--- | :--- | :---: | :--- |
| **[OpenRouter](https://openrouter.ai/)** | 40+ free models (Llama 3.3 70B, Gemma, Mistral, Qwen) | Free model endpoints (`:free`) with 20 RPM | ❌ No | [Get Free Key](https://openrouter.ai/keys) |
| **[Portkey.ai](https://portkey.ai/)** | AI gateway, caching, rate-limiting, multi-provider fallback | 10,000 free requests/month | ❌ No | [Get Free Key](https://app.portkey.ai/) |
| **[LiteLLM Proxy](https://github.com/BerriAI/litellm)** | Call 100+ LLMs using 1 OpenAI-compatible standard format | 100% Free open-source local/hosted proxy | ❌ No | [Docs](https://docs.litellm.ai/) |
| **[Requesty](https://requesty.ai/)** | Unified AI routing & cost-optimization proxy | Free developer tier | ❌ No | [Get Free Key](https://requesty.ai/) |
| **[Helicone](https://www.helicone.ai/)** | 1-line proxy for caching, tracing, analytics, and failover | 10,000 free requests/month | ❌ No | [Get Free Key](https://www.helicone.ai/) |
| **[Unify AI](https://unify.ai/)** | Dynamic routing to the fastest or cheapest LLM provider | Free trial credits | ❌ No | [Get Free Key](https://unify.ai/) |
| **[Martian](https://withmartian.com/)** | Model router dynamically choosing best LLM per prompt | Free developer evaluation sandbox | ❌ No | [Get Free Key](https://withmartian.com/) |
| **[Langfuse Proxy](https://langfuse.com/)** | Open-source LLM proxy with integrated tracing | 50,000 observations/month free on Cloud | ❌ No | [Get Free Key](https://cloud.langfuse.com/) |
| **[OpenPipe](https://openpipe.ai/)** | Dataset collection, fine-tuning router & proxy | Free developer starter tier | ❌ No | [Get Free Key](https://openpipe.ai/) |
| **[Promptfoo](https://www.promptfoo.dev/)** | LLM testing, red-teaming, and multi-model benchmarking | 100% Free open-source CLI & hosted runner | ❌ No | [Get Free Key](https://www.promptfoo.dev/) |
| **[RouteLLM](https://github.com/lm-sys/RouteLLM)** | Cost-optimized routing between strong and weak LLMs | 100% Free open-source framework by LMSYS | ❌ No | [GitHub](https://github.com/lm-sys/RouteLLM) |
| **[BerriAI](https://github.com/BerriAI)** | Multi-provider orchestration and instant Slack/Discord AI | Free open-source tier | ❌ No | [GitHub](https://github.com/BerriAI) |
| **[Aim](https://aimstack.io/)** | Self-hosted AI systems logging and comparison server | 100% Free open-source platform | ❌ No | [Docs](https://aimstack.io/) |

---

## 🎨 3. Image Generation & Computer Vision

Text-to-image, object detection, segmentation, background removal, and multi-modal image classification APIs.

| Provider | Top Models & Features | Free Tier Allowance | CC Req? | Signup Link |
| :--- | :--- | :--- | :---: | :--- |
| **[Pollinations.ai](https://pollinations.ai/)** | Flux, Stable Diffusion, Turbo image generation | 100% Free, NO API KEY REQUIRED, unlimited HTTP GET | ❌ No | [Use Directly](https://pollinations.ai/) |
| **[Hugging Face Spaces / Inference](https://huggingface.co/)** | SDXL, Flux.1-schnell, ControlNet, GroundingDINO | Generous rate-limited free inference API | ❌ No | [Get Free Key](https://huggingface.co/settings/tokens) |
| **[Segmind](https://www.segmind.com/)** | Flux Schnell, SDXL, Face Swap, Background Removal | 100 free image generation API calls/day | ❌ No | [Get Free Key](https://www.segmind.com/) |
| **[Fal.ai](https://fal.ai/)** | Ultra-fast Flux.1, LTX Video, SDXL Lightning | Free trial balance on GitHub login | ❌ No | [Get Free Key](https://fal.ai/dashboard/keys) |
| **[Dezgo](https://dezgo.com/)** | Stable Diffusion, Inpainting, Super-resolution | Free rate-limited public API | ❌ No | [Get Free Key](https://dezgo.com/) |
| **[Getimg.ai](https://getimg.ai/)** | Flux, Photorealism, Image editing | 100 free images every month forever | ❌ No | [Get Free Key](https://getimg.ai/) |
| **[Tensor.Art](https://tensor.art/)** | SD 1.5, SDXL, Checkpoints, LoRA models | 100 free daily credits on platform | ❌ No | [Get Free Key](https://tensor.art/) |
| **[Stability AI](https://platform.stability.ai/)** | Stable Diffusion 3.5, Stable Fast 3D | 25 free credits on registration | ❌ No | [Get Free Key](https://platform.stability.ai/) |
| **[Roboflow Universe](https://roboflow.com/)** | 200,000+ computer vision datasets & YOLO object detection APIs | 1,000 free API calls/month | ❌ No | [Get Free Key](https://roboflow.com/) |
| **[Clarifai](https://www.clarifai.com/)** | Vision classification, object detection, facial recognition | 1,000 free monthly operations | ❌ No | [Get Free Key](https://portal.clarifai.com/signup) |
| **[Landing AI](https://landing.ai/)** | Visual Prompting, Large Vision Models (LVM) | Free trial sandbox for inspection and vision QA | ❌ No | [Get Free Key](https://landing.ai/) |
| **[DeepAI](https://deepai.org/)** | Text-to-image, Colorization, Image Super Resolution | Free public API tier | ❌ No | [Get Free Key](https://deepai.org/api-docs) |
| **[Scenario.gg](https://www.scenario.com/)** | Custom game assets and style-consistent image generation | Free developer tier | ❌ No | [Get Free Key](https://www.scenario.com/) |
| **[Photoroom API](https://www.photoroom.com/api)** | Studio-quality background removal & image cleanup | Free sandbox credits for developers | ❌ No | [Get Free Key](https://www.photoroom.com/api) |
| **[Clipdrop API](https://clipdrop.co/apis)** | Uncrop, Relight, Background removal, Text remover | Free testing credits | ❌ No | [Get Free Key](https://clipdrop.co/apis) |
| **[Sightengine](https://sightengine.com/)** | Real-time NSFW, image moderation & face analysis | 2,000 free images/month | ❌ No | [Get Free Key](https://sightengine.com/) |
| **[Craiyon](https://www.craiyon.com/)** | Free text to image generation | Free community web endpoints | ❌ No | [Use Directly](https://www.craiyon.com/) |
| **[Picovoice Eagle](https://picovoice.ai/)** | Speaker recognition, face verification, and on-device AI | Free forever tier for up to 3 users | ❌ No | [Get Free Key](https://picovoice.ai/) |
| **[Google Cloud Vision (Trial)](https://cloud.google.com/vision)** | OCR, Landmark, Label Detection, SafeSearch | 1,000 units free every month | 🎁 Free Trial | [Console](https://console.cloud.google.com/) |
| **[Cloudinary AI](https://cloudinary.com/)** | Auto crop, face detection, background removal, upscaling | Free tier with 25 monthly credits | ❌ No | [Get Free Key](https://cloudinary.com/) |

---

## 🎙️ 4. Voice, Audio, Speech-to-Text & TTS

Real-time audio transcription, speech synthesis, voice cloning, and audio intelligence.

| Provider | Key Features | Free Tier Quota | CC Req? | Signup Link |
| :--- | :--- | :--- | :---: | :--- |
| **[Deepgram](https://deepgram.com/)** | Nova-2 STT (fastest in the world) & Aura TTS | $200 free credit (~45,000 mins audio) | ❌ No | [Get Free Key](https://console.deepgram.com/signup) |
| **[AssemblyAI](https://www.assemblyai.com/)** | Conformer-2 Speech-to-Text, Speaker Diarization, LeMUR | Free tier with starting credits ($50) | ❌ No | [Get Free Key](https://www.assemblyai.com/dashboard/signup) |
| **[Gladia](https://www.gladia.io/)** | Real-time multilingual transcription & audio intelligence | 10 hours of audio free every month | ❌ No | [Get Free Key](https://app.gladia.io/) |
| **[ElevenLabs](https://elevenlabs.io/)** | Hyper-realistic AI voice cloning & Text-to-Speech | 10,000 characters/month free forever | ❌ No | [Get Free Key](https://elevenlabs.io/) |
| **[Fish Audio](https://fish.audio/)** | Low-latency voice cloning, multilingual TTS | Free credits on signup | ❌ No | [Get Free Key](https://fish.audio/) |
| **[PlayHT](https://play.ht/)** | Voice cloning, Conversational TTS API | 12,500 characters free on signup | ❌ No | [Get Free Key](https://play.ht/) |
| **[Cartesia](https://cartesia.ai/)** | Sonic ultra-low latency (<100ms) TTS for voice agents | Free starter credits on sign in | ❌ No | [Get Free Key](https://play.cartesia.ai/) |
| **[Rev.ai](https://www.rev.ai/)** | Speech-to-Text & language identification | 5 hours of free transcription on signup | ❌ No | [Get Free Key](https://www.rev.ai/) |
| **[Speechify API](https://speechify.com/api/)** | High-naturalness TTS voices in 40+ languages | Free trial developer tier | ❌ No | [Get Free Key](https://speechify.com/api/) |
| **[Neets.ai](https://neets.ai/)** | Fast, high-quality open-source TTS inference | Free trial quota | ❌ No | [Get Free Key](https://neets.ai/) |
| **[Resemble AI](https://www.resemble.ai/)** | Deepfake detection, voice cloning & localization | Free trial credits | ❌ No | [Get Free Key](https://www.resemble.ai/) |
| **[Murf.ai](https://murf.ai/)** | Studio voiceovers with 120+ voices | 10 minutes of free voice generation | ❌ No | [Get Free Key](https://murf.ai/) |
| **[Voicemaker](https://voicemaker.in/)** | Neural TTS & standard SSML voice generation | Free tier with daily character credits | ❌ No | [Get Free Key](https://voicemaker.in/) |
| **[Whisper.cpp (Local)](https://github.com/ggerganov/whisper.cpp)** | High-performance C/C++ port of OpenAI's Whisper | 100% Free, infinite transcription, offline | ❌ No | [GitHub](https://github.com/ggerganov/whisper.cpp) |
| **[Faster-Whisper](https://github.com/SYSTRAN/faster-whisper)** | 4x faster Whisper reimplementation using CTranslate2 | 100% Free open-source local server | ❌ No | [GitHub](https://github.com/SYSTRAN/faster-whisper) |

---

## 🧠 5. Embeddings & Vector Databases

Vector storage, dense retrieval, neural search, and multi-modal embedding APIs.

| Provider | Top Embed Models / Engine | Free Tier Allowance | CC Req? | Signup Link |
| :--- | :--- | :--- | :---: | :--- |
| **[Cohere Embed](https://cohere.com/embed)** | Embed v3 (Multilingual & English), Rerank v3 | 100 API calls/min free evaluation key | ❌ No | [Console](https://dashboard.cohere.com/) |
| **[Voyage AI](https://www.voyageai.com/)** | voyage-3, voyage-code-3 (Top MTEB benchmarks) | 200 Million tokens free forever | ❌ No | [Console](https://dash.voyageai.com/) |
| **[Jina AI](https://jina.ai/embeddings/)** | jina-embeddings-v3 (8192 context), jina-reranker | 10,000,000 free tokens on signup | ❌ No | [Console](https://jina.ai/) |
| **[Mixedbread.ai](https://www.mixedbread.ai/)** | SOTA embedding models & re-ranking APIs | Free developer tier with monthly credits | ❌ No | [Console](https://www.mixedbread.ai/) |
| **[Pinecone](https://www.pinecone.io/)** | Fully-managed serverless vector database | 1 free serverless index (up to 100k vectors) | ❌ No | [Console](https://app.pinecone.io/) |
| **[Qdrant Cloud](https://qdrant.tech/)** | High-performance vector database with filtering | 1GB free permanent cluster (~4M 384d vectors) | ❌ No | [Console](https://cloud.qdrant.io/) |
| **[Weaviate Cloud (WCD)](https://weaviate.io/)** | Multi-modal vector search with built-in modules | Free 14-day Sandbox cluster (renewable) | ❌ No | [Console](https://console.weaviate.cloud/) |
| **[Zilliz Cloud (Milvus)](https://zilliz.com/)** | Managed Milvus for large-scale similarity search | Free Starter plan with 2 collections & 1M vectors | ❌ No | [Console](https://cloud.zilliz.com/) |
| **[Upstash Vector](https://upstash.com/docs/vector/overall)** | Serverless vector database with REST API | 10,000 commands/day free forever | ❌ No | [Console](https://console.upstash.com/) |
| **[Supabase pgvector](https://supabase.com/)** | PostgreSQL database with pgvector extension | 500MB database, 2 free projects | ❌ No | [Console](https://supabase.com/dashboard) |
| **[MongoDB Atlas Vector](https://www.mongodb.com/products/platform/atlas-vector-search)** | Hybrid full-text & vector search on MongoDB | M0 Free cluster (512MB storage forever) | ❌ No | [Console](https://www.mongodb.com/cloud/atlas/register) |
| **[Astra DB (DataStax)](https://www.datastax.com/products/datastax-astra)** | Cassandra-based Vector database for GenAI | $25 free credits every month forever | ❌ No | [Console](https://astra.datastax.com/) |
| **[Cloudflare Vectorize](https://developers.cloudflare.com/vectorize/)** | Global edge vector database integrated with Workers | 30M vector dimensions queried/month free | ❌ No | [Console](https://dash.cloudflare.com/) |
| **[ChromaDB (Local)](https://www.trychroma.com/)** | Lightweight, developer-friendly open source vector store | 100% Free open-source local database | ❌ No | [Docs](https://docs.trychroma.com/) |

---

## 🔍 6. Web Search, RAG & AI Web Scraping

Transform raw web pages into clean LLM-ready markdown and perform live grounding searches.

| Provider | Key Capabilities | Free Tier Quota | CC Req? | Signup Link |
| :--- | :--- | :--- | :---: | :--- |
| **[Tavily AI](https://tavily.com/)** | Search engine built strictly for LLMs, RAG, and AI agents | 1,000 free searches/month | ❌ No | [Get Free Key](https://app.tavily.com/) |
| **[Exa.ai (Metaphor)](https://exa.ai/)** | Neural embeddings search across the live web | $10 free credit on signup (~1,000 queries) | ❌ No | [Get Free Key](https://dashboard.exa.ai/) |
| **[Firecrawl](https://www.firecrawl.dev/)** | Turn entire websites into clean Markdown for LLMs | 500 free scraped pages on signup | ❌ No | [Get Free Key](https://www.firecrawl.dev/) |
| **[Jina Reader](https://r.jina.ai/)** | Convert any URL to LLM-ready markdown (prefix with `r.jina.ai/`) | Free without API key (or 1M free tokens with key) | ❌ No | [Use Directly](https://jina.ai/reader/) |
| **[Brave Search API](https://brave.com/search/api/)** | Independent search index (Web, News, Images, Videos) | 2,000 free queries/month | ❌ No | [Get Free Key](https://api.search.brave.com/) |
| **[Serper.dev](https://serper.dev/)** | Fast Google Search, Google News, Places, Images API | 2,500 free searches on signup | ❌ No | [Get Free Key](https://serper.dev/) |
| **[SerpApi](https://serpapi.com/)** | Scrapes Google, Bing, Yahoo, Baidu, YouTube results | 100 free searches/month forever | ❌ No | [Get Free Key](https://serpapi.com/) |
| **[Crawl4AI](https://crawl4ai.com/)** | Ultra-fast open-source async web crawler for LLMs | 100% Free open-source Python library & REST server | ❌ No | [GitHub](https://github.com/unclecode/crawl4ai) |
| **[Apify](https://apify.com/)** | 1,500+ ready-to-use scrapers (Twitter, LinkedIn, Amazon, etc.) | $5 free platform credit recurring every month | ❌ No | [Get Free Key](https://console.apify.com/) |
| **[ScrapingBee](https://www.scrapingbee.com/)** | Headless Chrome scraping with automatic proxy rotation | 1,000 free API credits on signup | ❌ No | [Get Free Key](https://app.scrapingbee.com/account/register) |
| **[ZenRows](https://www.zenrows.com/)** | Anti-bot bypass, Cloudflare solver, web scraper API | 1,000 free requests on signup | ❌ No | [Get Free Key](https://app.zenrows.com/) |
| **[Spider Cloud](https://spider.cloud/)** | High-throughput web crawler returning structured JSON/MD | Free starter tier | ❌ No | [Get Free Key](https://spider.cloud/) |

---

## 💻 7. Code Intelligence & Developer AI

AI code completion, repository indexing, refactoring agents, and automated code review.

| Tool / Provider | Features | Free Tier Access | CC Req? | Website |
| :--- | :--- | :--- | :---: | :--- |
| **[GitHub Models](https://github.com/marketplace/models)** | Test GPT-4o, Claude 3.5 Sonnet, Llama 3.3 in your IDE | Free developer tier | ❌ No | [Access](https://github.com/marketplace/models) |
| **[Codeium / Windsurf](https://codeium.com/)** | Ultra-fast autocomplete, chat, and in-editor AI agent | 100% Free forever for individual developers | ❌ No | [Install](https://codeium.com/) |
| **[Continue.dev](https://continue.dev/)** | Open-source AI copilot inside VS Code & JetBrains | 100% Free open-source (bring any free API key) | ❌ No | [GitHub](https://github.com/continuedev/continue) |
| **[Tabby](https://tabbyml.github.io/tabby/)** | Self-hosted GitHub Copilot alternative | 100% Free open-source local code server | ❌ No | [GitHub](https://github.com/TabbyML/tabby) |
| **[Aider](https://aider.chat/)** | Terminal-based AI pair programming in your git repo | 100% Free tool (works with free Groq/Gemini keys) | ❌ No | [Install](https://aider.chat/) |
| **[Sourcegraph Cody](https://sourcegraph.com/cody)** | Codebase context search and multi-file code editing | Free tier with 500 completions/month | ❌ No | [Install](https://sourcegraph.com/cody) |
| **[Pieces for Developers](https://pieces.app/)** | On-device contextual copilot and snippet management | Free personal tier | ❌ No | [Install](https://pieces.app/) |
| **[Qodo (formerly CodiumAI)](https://www.qodo.ai/)** | Automated test generation, PR review & bug finding | Free tier for individual open-source devs | ❌ No | [Install](https://www.qodo.ai/) |
| **[Blackbox AI](https://www.blackbox.ai/)** | Fast code generation, code search, and terminal helper | Free web & IDE tier | ❌ No | [Access](https://www.blackbox.ai/) |
| **[Mintlify AI Docs](https://mintlify.com/)** | Automated documentation generation and codebase writer | Free starter tier | ❌ No | [Access](https://mintlify.com/) |
| **[Snyk Code](https://snyk.io/product/snyk-code/)** | AI-assisted real-time security vulnerability detection | Free tier with 100 tests/month | ❌ No | [Access](https://snyk.io/) |

---

## 📄 8. Document AI, OCR & PDF Parsing

Extract structured tables, key-value pairs, and markdown from messy PDFs and scanned scans.

| Provider | Core Capabilities | Free Tier Quota | CC Req? | Signup Link |
| :--- | :--- | :--- | :---: | :--- |
| **[LlamaParse](https://cloud.llamaindex.ai/)** | GenAI parser by LlamaIndex converting complex PDFs to Markdown | 1,000 pages free every day forever | ❌ No | [Get Free Key](https://cloud.llamaindex.ai/) |
| **[Unstructured.io](https://unstructured.io/)** | Ingestion pipeline for 25+ document formats (PDF, DOCX, PPT) | 1,000 free pages/month on Serverless API | ❌ No | [Get Free Key](https://unstructured.io/) |
| **[Mistral OCR](https://console.mistral.ai/)** | SOTA document understanding and multimodal OCR | Free experimentation quota on La Plateforme | ❌ No | [Get Free Key](https://console.mistral.ai/) |
| **[Mindee](https://www.mindee.com/)** | Receipt, invoice, passport, and custom document OCR | 250 free pages/month | ❌ No | [Get Free Key](https://www.mindee.com/) |
| **[OCR.space](https://ocr.space/ocrapi)** | Free cloud OCR service supporting 25+ languages | 25,000 free requests/month | ❌ No | [Get Free Key](https://ocr.space/ocrapi) |
| **[Reducto.ai](https://reducto.ai/)** | Document parsing optimized for complex financial & legal PDFs | Free developer credits | ❌ No | [Get Free Key](https://reducto.ai/) |
| **[Marker](https://github.com/VikParuchuri/marker)** | Converts PDF to markdown with tables, code, and LaTeX math | 100% Free open-source Python tool | ❌ No | [GitHub](https://github.com/VikParuchuri/marker) |
| **[Docsumo](https://www.docsumo.com/)** | Intelligent document processing for invoices & bank statements | Free trial credits | ❌ No | [Get Free Key](https://www.docsumo.com/) |
| **[Base64.ai](https://base64.ai/)** | Instant ID, passport, driver license & document verification | 100 free pages on signup | ❌ No | [Get Free Key](https://base64.ai/) |
| **[Klippa OCR](https://www.klippa.com/en/ocr/)** | Automated receipt & financial receipt parsing API | Free trial sandbox | ❌ No | [Get Free Key](https://www.klippa.com/) |

---

## 🎬 9. Video & 3D Model Generation

AI text-to-video, image-to-video, camera control, and 3D mesh reconstruction.

| Provider | Top Models & Features | Free Tier Access | CC Req? | Signup Link |
| :--- | :--- | :--- | :---: | :--- |
| **[Luma Dream Machine](https://lumalabs.ai/dream-machine)** | Photorealistic text-to-video & image-to-video generation | 30 free video generations/month | ❌ No | [Console](https://lumalabs.ai/dream-machine) |
| **[Kling AI](https://klingai.com/)** | High-fidelity motion physics, video synthesis | 66 free daily generation credits | ❌ No | [Console](https://klingai.com/) |
| **[Haiper AI](https://haiper.ai/)** | Text to video, image animation, video repainting | Free generation credits on daily login | ❌ No | [Console](https://haiper.ai/) |
| **[Pika Labs](https://pika.art/)** | Dynamic motion video generation & Lip Sync | Free recurring starter credits | ❌ No | [Console](https://pika.art/) |
| **[RunwayML](https://runwayml.com/)** | Gen-2 and Gen-3 Alpha video generation | 125 free one-time credits | ❌ No | [Console](https://runwayml.com/) |
| **[Meshy 3D](https://www.meshy.ai/)** | Text to 3D and image to 3D mesh (GLB/FBX) | 200 free credits/month | ❌ No | [Console](https://www.meshy.ai/) |
| **[Tripo3D](https://www.tripo3d.ai/)** | Instant 3D model generation in seconds | Free credits on registration | ❌ No | [Console](https://www.tripo3d.ai/) |
| **[Spline 3D AI](https://spline.design/ai)** | AI-generated 3D interactive objects and web animations | Free starter tier | ❌ No | [Console](https://spline.design/) |
| **[CSM (Common Sense Machines)](https://csm.ai/)** | 3D world and object asset generation from single photos | Free monthly credits on sign in | ❌ No | [Console](https://csm.ai/) |

---

## 🎵 10. Music & Sound FX Generation

Full song generation with vocals, stems separation, instrumental tracks, and realistic Foley sound effects.

| Provider | Core Features | Free Tier Allowance | CC Req? | Signup Link |
| :--- | :--- | :--- | :---: | :--- |
| **[Suno AI](https://suno.com/)** | Full vocal and instrumental song generation | 50 free credits every day (~10 songs/day) | ❌ No | [Console](https://suno.com/) |
| **[Udio](https://www.udio.com/)** | High-fidelity music generation with genre steering | Free monthly credit allowance | ❌ No | [Console](https://www.udio.com/) |
| **[Beatoven.ai](https://www.beatoven.ai/)** | Royalty-free background music composition | Free tier with unlimited track generation | ❌ No | [Console](https://www.beatoven.ai/) |
| **[ElevenLabs Sound Effects](https://elevenlabs.io/sound-effects)** | Realistic Foley, ambient noises, and sound effects from text | Included in 10k character free tier | ❌ No | [Console](https://elevenlabs.io/) |
| **[Soundraw](https://soundraw.io/)** | AI music generator customizable by tempo and instruments | Free unlimited music generation (preview) | ❌ No | [Console](https://soundraw.io/) |
| **[Loudly](https://www.loudly.com/)** | AI music creation studio and sound generator | Free plan with 25 songs/month | ❌ No | [Console](https://www.loudly.com/) |
| **[AudioCraft by Meta](https://github.com/facebookresearch/audiocraft)** | MusicGen & AudioGen models running locally | 100% Free open-source PyTorch models | ❌ No | [GitHub](https://github.com/facebookresearch/audiocraft) |

---

## 📊 11. LLM Observability, Evaluation & Guardrails

Trace prompts, monitor latency, calculate token costs, detect hallucinations, and enforce safety guardrails.

| Provider | What it Does | Free Tier Quota | CC Req? | Signup Link |
| :--- | :--- | :--- | :---: | :--- |
| **[Langfuse](https://langfuse.com/)** | Open-source LLM tracing, prompt management, and evals | 50,000 observations/month free cloud tier | ❌ No | [Get Free Key](https://cloud.langfuse.com/) |
| **[Helicone](https://www.helicone.ai/)** | 1-line proxy for cost tracking, caching & analytics | 10,000 requests/month free forever | ❌ No | [Get Free Key](https://www.helicone.ai/) |
| **[Arize Phoenix](https://phoenix.arize.com/)** | Open-source LLM observability, Evals & RAG troubleshooting | 100% Free open-source + Free Cloud tier | ❌ No | [Get Free Key](https://app.phoenix.arize.com/) |
| **[LangSmith (LangChain)](https://smith.langchain.com/)** | LLM debugging, dataset testing, and evaluation suite | 5,000 traces/month free forever | ❌ No | [Get Free Key](https://smith.langchain.com/) |
| **[DeepEval](https://github.com/confident-ai/deepeval)** | The open-source LLM evaluation framework (RAG metrics) | Free open-source + Free Confident AI cloud tier | ❌ No | [GitHub](https://github.com/confident-ai/deepeval) |
| **[Promptfoo](https://github.com/promptfoo/promptfoo)** | CLI & library for testing prompt outputs and red-teaming | 100% Free open-source tool | ❌ No | [GitHub](https://github.com/promptfoo/promptfoo) |
| **[Portkey Observability](https://portkey.ai/)** | Centralized logs, error alerts, and multi-LLM latency stats | 10,000 logs/month free | ❌ No | [Get Free Key](https://app.portkey.ai/) |
| **[Guardrails AI](https://www.guardrailsai.com/)** | Validation and safety guards for LLM inputs and outputs | Free open-source hub modules | ❌ No | [GitHub](https://github.com/guardrails-ai/guardrails) |
| **[NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails)** | NVIDIA toolkit for adding programmable safety rails to LLMs | 100% Free open-source library | ❌ No | [GitHub](https://github.com/NVIDIA/NeMo-Guardrails) |
| **[TruLens](https://www.trulens.org/)** | RAG triad evaluation (Groundedness, Context Relevance) | 100% Free open-source library | ❌ No | [GitHub](https://github.com/truera/trulens) |
| **[Weights & Biases Prompts](https://wandb.ai/site/prompts)** | LLM monitoring and prompt engineering workspace | Free tier for individual researchers | ❌ No | [Console](https://wandb.ai/) |

---

## 🚀 Quickstart: Call Free AI APIs in 5 Lines of Python

No expensive SDKs required. All these providers follow the standard OpenAI REST specification:

### 1. Ultra-fast Inference with Groq (Free)

```python
import os, urllib.request, json

req = urllib.request.Request(
    "https://api.groq.com/openai/v1/chat/completions",
    data=json.dumps({
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": "Explain quantum computing in one sentence."}]
    }).encode("utf-8"),
    headers={"Authorization": f"Bearer {os.environ.get('GROQ_API_KEY')}", "Content-Type": "application/json"}
)
res = json.loads(urllib.request.urlopen(req).read().decode("utf-8"))
print(res["choices"][0]["message"]["content"])
```

### 2. Access 40+ Free Models with OpenRouter

```python
import os, urllib.request, json

req = urllib.request.Request(
    "https://openrouter.ai/api/v1/chat/completions",
    data=json.dumps({
        "model": "meta-llama/llama-3.3-70b-instruct:free",
        "messages": [{"role": "user", "content": "What are 3 practical use cases for AI agents?"}]
    }).encode("utf-8"),
    headers={"Authorization": f"Bearer {os.environ.get('OPENROUTER_API_KEY')}", "Content-Type": "application/json"}
)
res = json.loads(urllib.request.urlopen(req).read().decode("utf-8"))
print(res["choices"][0]["message"]["content"])
```

### 3. Generate Free Images via Pollinations (Zero Auth Needed)

```python
import urllib.request

prompt = "hyperrealistic cyberpunk laboratory with holographic screens, 8k"
image_url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}?width=1024&height=1024&nologo=true"
urllib.request.urlretrieve(image_url, "generated_art.jpg")
print("Saved image to generated_art.jpg!")
```

---

## 🧪 CLI Key Tester Utility

This repository includes a standalone Python CLI [`test_keys.py`](test_keys.py) with zero third-party dependencies to test your free keys in 2 seconds:

```bash
# Test Groq Key
python3 test_keys.py --provider groq --key gsk_your_key_here

# Test OpenRouter Key
python3 test_keys.py --provider openrouter --key sk-or-v1-your_key_here

# Test Google Gemini Key
python3 test_keys.py --provider gemini --key AIzaSy_your_key_here

# Test Mistral Key
python3 test_keys.py --provider mistral --key your_mistral_key_here

# Test Deepgram Speech Key
python3 test_keys.py --provider deepgram --key your_deepgram_key_here
```

Output:
```
[INFO] Testing Groq Cloud endpoint (model: llama-3.3-70b-versatile)...
[SUCCESS] ✅ Key is valid! Latency: 184ms | Tokens/sec: 420
Response: Quantum computing uses qubits that exist in superpositions...
```

---

## 🤝 Contributing

We welcome additions, fixes, and updates from the community!

Found a new provider offering a free tier? Or did a provider alter their rate limit?
1. Check the [Contribution Guidelines](CONTRIBUTING.md).
2. Ensure the provider has a legitimate free tier or developer trial.
3. Submit a Pull Request following the table format.

---

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=itismemuhammadali/Awesome-Free-AI-APIs&type=Date)](https://star-history.com/#itismemuhammadali/Awesome-Free-AI-APIs&Date)

---

## 👨‍💻 Author & Maintainer

Curated with ❤️ by **Muhammad Ali**  
- **GitHub**: [@itismemuhammadali](https://github.com/itismemuhammadali)
- **Portfolio / Projects**: [Muhammad Ali Showcase](https://github.com/itismemuhammadali)

If this repository saved you money or helped you launch your project, please **give it a ⭐ star** and share it with your fellow developers!

---

## 📜 License

Distributed under the [MIT License](LICENSE). Feel free to use, fork, and share!
