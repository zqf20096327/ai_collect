<p align="center">
  <img src="https://raw.githubusercontent.com/vanszs/tiktok-viral-factory/main/docs/banner.png" alt="TikTok Viral Factory" width="800">
</p>

<h1 align="center"> TikTok Viral Factory</h1>

<p align="center">
  <b>Multi-Agent AI System that generates, produces, and publishes TikTok Shop Affiliate videos — fully automated.</b><br>
  <sub>7 AI Agents · LangGraph · Kling AI · ElevenLabs · MCP Protocol</sub>
</p>

<p align="center">
  <a href="https://github.com/vanszs/tiktok-viral-factory/stargazers"><img src="https://img.shields.io/github/stars/vanszs/tiktok-viral-factory?style=for-the-badge&color=FF0050&logo=github" alt="Stars"></a>
  <a href="https://github.com/vanszs/tiktok-viral-factory/network/members"><img src="https://img.shields.io/github/forks/vanszs/tiktok-viral-factory?style=for-the-badge&color=25F4EE&logo=github" alt="Forks"></a>
  <a href="https://github.com/vanszs/tiktok-viral-factory/blob/main/LICENSE"><img src="https://img.shields.io/github/license/vanszs/tiktok-viral-factory?style=for-the-badge&color=white" alt="License"></a>
  <a href="#"><img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <a href="#"><img src="https://img.shields.io/badge/LangGraph-Powered-orange?style=for-the-badge" alt="LangGraph"></a>
</p>

<p align="center">
  <a href="#-quick-start"><img src="https://img.shields.io/badge/Quick_Start-FF0050?style=for-the-badge" alt="Quick Start"></a>
  <a href="#-architecture"><img src="https://img.shields.io/badge/Architecture-25F4EE?style=for-the-badge" alt="Architecture"></a>
  <a href="plan.md"><img src="https://img.shields.io/badge/Full_Plan_(1200_lines)-white?style=for-the-badge" alt="Full Plan"></a>
</p>

---

## What is this?

A **fully autonomous AI workforce** that runs 7 specialized agents working together to:

1. **Research** trending TikTok Shop products in Beauty & Personal Care
2. **Plan** viral content strategies based on TikTok algorithm signals
3. **Write** hook-optimized scripts with karaoke-style word timestamps
4. **Generate** product hero shots using Kling AI (cinematic, not AI slop)
5. **Compose** full videos with ElevenLabs voiceover, stock footage, text overlays, SFX
6. **Optimize** SEO (hashtags, captions, posting time)
7. **Publish** to TikTok via Content Posting API

**You provide the API keys. It does everything else.**

```
Input:  TikTok Shop product URL
Output: Ready-to-post 15-60s TikTok video + optimized caption + hashtags
```

> [!NOTE]
> This is **not** a "type your prompt, get a video" wrapper. This is a **multi-agent system** with real market research, content strategy, deduplication, cost tracking, and TikTok compliance built in.

---

## Why this exists

| Problem | Solution |
|---|---|
| Creating TikTok content manually = 2-4 hours/video | **100 videos/month, fully automated** |
| AI-generated videos get flagged as "AI slop" and throttled | **Mixed pipeline**: stock footage + AI hero shots + text overlays = human-feeling |
| Most AI video tools produce generic, soulless content | **7 specialized agents** — each one does ONE thing well |
| TikTok Shop Affiliate is lucrative but hard to scale | **Beauty & Personal Care** niche = #1 GMV category, 15-25% commission |
| GPU requirements block most developers | **Cloud APIs** (Kling, ElevenLabs) — runs on any laptop |

---

## Architecture

```
                        YOU (CLI)
                            │
                ┌───────────▼───────────┐
                │   SUPERVISOR          │
                │   (Marketing Director)│
                │   Routes + monitors   │
                └───────────┬───────────┘
                            │
         ┌──────────────────┼──────────────────┐
         │                  │                  │
         ▼                  ▼                  ▼
    RESEARCH          STRATEGY           ANALYTICS
    Market Intel      Content Plan       Performance
         │                  │
         │           ┌──────┴──────┐
         │           ▼             ▼
         │      SCRIPT         SEO AGENT
         │      WRITER         (Hashtags,
         │                     Captions)
         │           │
         └───────────▼
                PRODUCER
             (Video Engine)
             Kling AI + Stock +
             ElevenLabs + FFmpeg
                   │
                   ▼
               PUBLISHER
            (Upload to TikTok)

    ┌────────────────────────────────┐
    │        MCP BRIDGE              │
    │   Client ↔ Server              │
    │   Connect external tools       │
    │   Expose agents as MCP tools   │
    └────────────────────────────────┘
```

### 7 Agents

| Agent | Role | Tools |
|---|---|---|
| **Supervisor** | Marketing Director — routes tasks, monitors quality | LLM + Router |
| **Research** | Trending products, competitor analysis, market intel | LLM + TikTok Research |
| **Strategy** | Content calendar, hook library, posting schedule | LLM + Trend DB |
| **Script Writer** | 15-60s scripts with word timestamps, hook optimization | LLM |
| **SEO** | Hashtags, captions, posting time, TikTok algorithm signals | LLM |
| **Producer** | Video generation — Kling AI + stock footage + ElevenLabs TTS + FFmpeg | Kling, Pixabay, Pexels, ElevenLabs, FFmpeg |
| **Publisher** | Upload to TikTok, or export package for manual upload | TikTok API |
| **Analytics** | Track views, engagement, revenue, optimize strategy | LLM + Analytics DB |

---

## Video Pipeline (Mixed Approach)

The key insight: **pure AI-generated videos get throttled by TikTok**. Our mixed approach feels human:

```
Stock Footage (60%)          AI Product Shots (20%)      Overlays (20%)
─────────────────────────    ────────────────────────    ─────────────────────
Pixabay/Pexels               Kling AI 2.5 Turbo Pro      FFmpeg
"woman applying cream"       "serum bottle, slow-mo      Text overlays
"close-up skincare routine"   cinematic, 9:16"           Subtitles (karaoke)
"glowing skin result"        $0.07/sec via fal.ai       SFX (whoosh, ding)
```

### Video Output Example

```
[0-3s]   HOOK:   Stock footage + bold text overlay + whoosh SFX
[3-8s]   PROBLEM: Stock footage + voiceover "Punya masalah kulit kusam?"
[8-18s]  PRODUCT: Kling AI hero shot + ingredient callouts + voiceover
[18-25s] PROOF:   Stock "glowing skin" + voiceover "Coba ini..."
[25-30s] CTA:    Text overlay "Link di bio!" + product image + sparkle SFX
```

---

## Tech Stack

| Layer | Technology | Why |
|---|---|---|
| **Framework** | LangGraph | Supervisor pattern, native streaming, persistence |
| **LLM** | OpenAI-compatible API | Works with any provider (OpenAI, Groq, Together, local) |
| **AI Video** | Kling 2.5 Turbo Pro (fal.ai) | Best e-commerce product shots, $0.07/sec |
| **Stock Footage** | Pixabay + Pexels | FREE, HD, 100+ req/min |
| **Voice** | ElevenLabs `eleven_multilingual_v2` | Natural voice, Indonesian support, word timestamps |
| **Video Engine** | FFmpeg + moviepy | Text overlays, composition, SFX, subtitles |
| **Image Tools** | rembg | Background removal for product photos |
| **Protocol** | MCP (Model Context Protocol) | Connect to any MCP server, expose agents as tools |
| **Config** | Pydantic Settings | Type-safe, .env driven |

---

## Cost Breakdown (100 videos/month)

| Service | Cost | Notes |
|---|---|---|
| Kling AI | ~$35/mo | 5 sec product shots × 100 videos |
| ElevenLabs | ~$10/mo | 30s voiceover × 100 videos |
| LLM API | ~$5/mo | OpenAI-compatible, varies by provider |
| Stock Footage | **FREE** | Pixabay + Pexels |
| **Total** | **~$50/month** | |

---

## Quick Start

### Prerequisites

- Python 3.11+
- FFmpeg installed (`apt install ffmpeg` / `brew install ffmpeg`)
- API keys: OpenAI-compatible LLM, fal.ai (Kling), ElevenLabs, Pixabay, Pexels

### 1. Clone & Install

```bash
git clone https://github.com/vanszs/tiktok-viral-factory.git
cd tiktok-viral-factory
pip install -r requirements.txt
```

### 2. Configure

```bash
cp .env.example .env
# Edit .env with your API keys
```

### 3. Run

```bash
# Generate a single video from a TikTok Shop product
python -m workflows.faceless --product-url "https://shop.tiktok.com/..."

# Batch generate from product list
python -m workflows.batch --input products.json --count 10

# Clip pipeline (transform existing content)
python -m workflows.clipping --source video.mp4

# Start MCP server (expose agents as tools)
python -m mcp_bridge.server

# Connect to external MCP tools
python -m mcp_bridge.client --config mcp_servers.json
```

### 4. Output

```
output/
├── video_20240115_143022.mp4     # Final video (1080x1920, 9:16)
├── video_20240115_143022.srt     # Subtitle file
├── metadata.json                  # Product data, SEO, timestamps
└── thumbnail.jpg                  # Auto-generated thumbnail
```

---

## Project Structure

```
tiktok-viral-factory/
├── agents/              # 7 LangGraph agent nodes
├── config/
│   ├── prompts/         # System prompts for each agent
│   └── settings.py      # Pydantic settings (60+ config fields)
├── mcp_bridge/
│   ├── client.py        # Connect to external MCP servers
│   └── server.py        # Expose agents as MCP tools
├── models/
│   └── schemas.py       # 22 Pydantic models (state, products, videos)
├── tools/               # Image search, Kling, TTS, FFmpeg, SEO
├── utils/
│   └── llm.py           # OpenAI-compatible LLM factory
├── workflows/           # 3 pipelines: faceless, clipping, batch
├── fonts/               # Custom .ttf for text overlays
├── sfx/                 # Sound effects (whoosh, ding, sparkle)
├── output/              # Generated videos + metadata
├── plan.md              # Full 1200-line implementation plan
└── .env.example         # All config fields documented
```

---

## Key Features

- **Anti-AI-Slop**: Mixed pipeline (stock + AI hero shots + overlays) avoids TikTok's AI content throttling
- **Content Deduplication**: Hash-based tracking prevents generating duplicate content across runs
- **Cost Tracking**: Real-time budget monitoring per video and monthly cap ($50 default)
- **Kling AI Fallback**: If AI video fails, automatically falls back to static product image with FFmpeg zoom + sparkle
- **Smart Stock Search**: Searches vertical first → smart crop → letterbox → pan&scan for any orientation
- **Word-Level Subtitles**: ElevenLabs timestamps enable karaoke-style subtitle sync
- **MCP Protocol**: Full MCP Bridge — connect to any tool ecosystem, expose your agents to other systems
- **Multi-LLM**: Works with OpenAI, Groq, Together AI, Ollama, or any OpenAI-compatible API

---

## Roadmap

- [x] Architecture & PRD (1200+ lines)
- [x] Data models (22 Pydantic schemas)
- [x] Configuration system (60+ typed settings)
- [ ] MCP Bridge (Client + Server)
- [ ] Tools layer (Kling, ElevenLabs, Pixabay, FFmpeg)
- [ ] 7 Agents implementation
- [ ] 3 Video pipelines (faceless, clipping, batch)
- [ ] TikTok Content Posting API integration
- [ ] Analytics dashboard
- [ ] Batch mode (100 videos/month)
- [ ] Multi-niche support (beyond Beauty & Personal Care)

---

## Contributing

PRs welcome! Areas where help is most needed:

- **More niches**: Extend beyond Beauty & Personal Care
- **More stock sources**: Additional free stock footage APIs
- **Better prompts**: Improve agent system prompts with real-world results
- **UI**: Simple web dashboard for monitoring

---

## License

MIT — do whatever you want with it. If you make money from it, that's the point.

---

<p align="center">
  <b>If this helps you build your TikTok empire, drop a star.</b><br>
  <a href="https://github.com/vanszs/tiktok-viral-factory/stargazers">
    <img src="https://img.shields.io/badge/Star_this_repo-FF0050?style=for-the-badge&logo=github" alt="Star">
  </a>
</p>

<p align="center">
  <sub>Built with caffeine and LangGraph in Indonesia</sub>
</p>
