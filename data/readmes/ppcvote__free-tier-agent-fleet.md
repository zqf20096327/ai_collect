# Free Tier Agent Fleet

**Run a 4-agent AI company on Gemini's free tier. 105 daily tasks, $0/month.**

A complete playbook for running an autonomous multi-agent business on a single LLM's free tier. Every script, timer, and intelligence pipeline — open source.

## The Numbers

| Metric | Value |
|--------|-------|
| Daily automated tasks | ~105 |
| LLM requests per day | ~105 / 1,500 RPD |
| Monthly LLM cost | **$0** |
| Monthly infra cost | ~$5 (Vercel hobby) |
| Agents | 4 (CEO, Social, Security, Advisor) |
| Scripts | 80+ |
| Systemd timers | 25 |
| Intelligence files | 19 |
| Self-healing layers | 3 (detect → AI diagnose → human alert) |
| Evolution modules | 7 (learning loop, dream cycle, arena, etc.) |
| GPU inference | Ollama ultralab:7b on RTX 3060 Ti |

## Architecture

```
                    ┌─────────────────────────────────┐
                    │        Gemini 2.5 Flash          │
                    │     Free Tier (1,500 RPD)        │
                    └──────────┬──────────────────────┘
                               │
                    ┌──────────▼──────────────────────┐
                    │      OpenClaw Gateway            │
                    │    (rate limit + routing)         │
                    └──────────┬──────────────────────┘
                               │
          ┌────────────┬───────┴───────┬────────────┐
          ▼            ▼               ▼            ▼
     ┌─────────┐ ┌──────────┐  ┌──────────┐ ┌──────────┐
     │  Main   │ │  Social  │  │ Security │ │ Advisor  │
     │  (CEO)  │ │   Bot    │  │   Bot    │ │   Bot    │
     └────┬────┘ └────┬─────┘  └────┬─────┘ └────┬─────┘
          │           │             │             │
          └─────┬─────┴──────┬──────┴─────────────┘
                │            │
       ┌────────▼──┐  ┌──────▼──────┐
       │ Content   │  │Intelligence │
       │ Pipeline  │  │  Pipeline   │
       │(24 calls) │  │ (15 calls)  │
       └───────────┘  └─────────────┘
```

## The 6-Layer Architecture

### Layer 1: Quality Gate (2 LLM calls/post)
Every post goes through generate → self-review → rewrite if score < 7/10.

### Layer 2: Data-Driven Context (0 LLM calls)
Posts read `POST-PERFORMANCE.md` + `COMPETITOR-INTEL.md` before generating. The agent knows what worked, what flopped, and what competitors are doing — all at zero token cost.

### Layer 3: Conversation Threading (1 LLM call/reply)
Reply-checker monitors comments, generates context-aware responses, tracks thread depth (max 2 rounds per post), batch-limited to prevent rate limiting.

### Layer 4: Peer Review (1 LLM call)
Cross-agent review before publishing. Security agent reviews marketing claims, CEO reviews technical accuracy.

### Layer 5: Weekly Strategy (5 LLM calls/week)
Every Sunday: 3 agents propose priorities → CEO synthesizes into next week's plan. Reads all intelligence files.

### Layer 6: Research Chain (3-5 LLM calls, 2x/day)
`blogwatcher (RSS)` → `hn-trending (HN API)` → `summarize (Jina Reader)` → agent analyzes relevance. Data gathering costs 0 LLM tokens — it's pure HTTP.

## RPD Budget Breakdown

| Category | Daily RPD | % of Free Tier |
|----------|-----------|----------------|
| Content (4 agents × 2 posts × 2 calls) | 16 | 1.1% |
| Quality gate reviews | 8 | 0.5% |
| Engagement (4 agents × 1x/day) | 16 | 1.1% |
| Reply checker (2x/day) | 10 | 0.7% |
| Cross-agent engagement (2x/week) | 6 | 0.4% |
| Research chain (2x/day × ~4 calls) | 8 | 0.5% |
| Blog-to-social | 2 | 0.1% |
| Lead follow-up | 2 | 0.1% |
| Inquiry tracker | 0 | 0% |
| Health monitor | 0 | 0% |
| Competitor watch | 0 | 0% |
| Post stats | 0 | 0% |
| Weekly strategy | 1 | 0.07% |
| **Total** | **~105** | **7%** |
| **Remaining for interactive** | **~1,395** | **93%** |

## The Key Insight

The expensive part of AI agents isn't the LLM — it's **wasted context**.

Long conversations burn tokens on repeated context. Short, focused tasks with pre-computed data are 100x more efficient.

```
❌ Typical agent: "Read this RSS feed, analyze it, remember it, now write a post"
   → 1 long conversation, 10K+ tokens of context accumulation

✅ Our approach:
   1. blogwatcher scan (0 LLM tokens — pure HTTP)
   2. summarize URL (0 LLM tokens — Jina Reader API)
   3. Read RESEARCH-NOTES.md + POST-PERFORMANCE.md (0 tokens to produce)
   4. One focused prompt with all context pre-injected
   5. One response → parse → post → done
```

## Data Flow

```
05:00  Research chain → RESEARCH-NOTES.md
06:00  Customer insights sync + Inquiry tracker
06:30  Competitor watch → COMPETITOR-INTEL.md
07-10  Autopost (all 4 agents, quality-gated)
10:00  Engagement (staggered across agents)
11:00  Reply checker (conversation threading)
14:00  Blog-to-social (if new content)
17:00  Research chain (round 2)
22:00  Post stats → POST-PERFORMANCE.md
23:00  Reply checker (round 2)
Sun    Weekly strategy session
```

## Directory Structure

```
free-tier-agent-fleet/
├── scripts/
│   ├── core/
│   │   ├── moltbook-autopost.sh     # Content pipeline (quality-gated)
│   │   ├── team-context.sh          # Cross-agent collaboration
│   │   └── peer-review.sh           # Pre-publish review
│   ├── intelligence/
│   │   ├── research-chain.sh        # RSS + HN → summarize → analyze
│   │   ├── competitor-watch.sh      # Track competitor content
│   │   ├── post-stats.sh            # Track own post performance
│   │   └── hn-trending              # HN top stories (0 cost)
│   ├── engagement/
│   │   ├── reply-checker.sh         # Auto-reply with threading
│   │   └── blog-to-social.sh        # Auto-promote blog posts
│   ├── operations/
│   │   ├── inquiry-tracker.js       # CRM pipeline tracking
│   │   ├── lead-followup.js         # Auto-draft outreach
│   │   ├── health-monitor.sh        # Endpoint monitoring
│   │   └── weekly-strategy.sh       # AI strategy sessions
│   ├── self-heal/                   # 🆕 3-tier autonomous healing
│   │   ├── self-heal.sh             # Main sentinel (every 10 min)
│   │   ├── predictive-ops.sh        # Anomaly trend detection
│   │   ├── tg-commander.js          # Remote control via Telegram
│   │   └── fixes/                   # 6 pre-written fix scripts
│   ├── evolution/                   # 🆕 Self-improving intelligence
│   │   ├── apply-strategy.js        # Closed-loop learning
│   │   ├── dream-cycle.sh           # Idle GPU utilization
│   │   ├── agent-arena.js           # Competitive evolution
│   │   ├── quality-gate.sh          # Pre-publish scoring
│   │   └── memory-consolidate.sh    # Weekly wisdom synthesis
│   └── content-pipeline/            # 🆕 Cross-platform distribution
│       ├── smart-post.sh            # Ollama → quality gate → publish
│       └── devto-crosspost.cjs      # Auto cross-post to Dev.to
├── timers/                          # systemd timer + service files
├── examples/
│   ├── openclaw.json.example        # Agent fleet config
│   └── credentials.json.example     # API credentials
├── LICENSE                          # MIT
└── README.md
```

## Quick Start

### Prerequisites

- Linux (WSL2 works great on Windows)
- [OpenClaw](https://github.com/openclaw-ai/openclaw) installed
- Gemini API key (free tier from [AI Studio](https://aistudio.google.com/), **NOT from Google Cloud**)
- Node.js 18+
- Optional: `blogwatcher`, `summarize` (Jina Reader CLI)

### Setup

```bash
# 1. Clone this repo
git clone https://github.com/ppcvote/free-tier-agent-fleet.git
cd free-tier-agent-fleet

# 2. Configure OpenClaw
cp examples/openclaw.json.example ~/.openclaw/openclaw.json
# Edit with your API keys and agent names

# 3. Set up credentials
mkdir -p ~/.config/moltbook
cp examples/credentials.json.example ~/.config/moltbook/credentials.json
# Edit with your Moltbook API key

# 4. Copy scripts
cp -r scripts/* ~/.openclaw/scripts/
chmod +x ~/.openclaw/scripts/**/*.sh
chmod +x ~/.openclaw/scripts/intelligence/hn-trending

# 5. Install timers
cp timers/openclaw-*.timer timers/openclaw-*.service ~/.config/systemd/user/
systemctl --user daemon-reload

# 6. Enable timers
for timer in ~/.config/systemd/user/openclaw-*.timer; do
  systemctl --user enable --now "$(basename "$timer")"
done

# 7. Create workspace directories
mkdir -p ~/.openclaw/{workspace,workspace-social,workspace-security,workspace-advisor}
mkdir -p ~/.openclaw/{data,logs}

# 8. Verify
systemctl --user list-timers | grep openclaw
```

### First Run

```bash
# Test the autopost pipeline manually
bash ~/.openclaw/scripts/core/moltbook-autopost.sh

# Test the research chain
bash ~/.openclaw/scripts/intelligence/research-chain.sh

# Test health monitoring
bash ~/.openclaw/scripts/operations/health-monitor.sh
```

## Customization

### Adding a New Agent

1. Add agent config to `openclaw.json`
2. Create workspace: `mkdir ~/.openclaw/workspace-newagent`
3. Copy and modify an autopost script with new pillars
4. Add corresponding systemd timer

### Changing Content Pillars

Edit the `PILLARS` array in `moltbook-autopost.sh`:

```bash
PILLARS=(
  "your-niche-1"
  "your-niche-2"
  "your-niche-3"
  "your-niche-4"
  "your-niche-5"
)
```

### Adjusting RPD Budget

The system uses ~7% of the 1,500 RPD free tier. You can:
- Increase posting frequency (more posts/day)
- Add more agents
- Enable peer review on every post (currently optional)
- Run research chain 3x/day instead of 2x

### Platform Adaptation

Scripts are written for Moltbook but the pattern works for any platform with an API:
- Replace Moltbook API calls with your platform's API
- Keep the intelligence pipeline (it's platform-agnostic)
- Keep the quality gate (it's LLM-agnostic)

## War Stories

### $127.80 Gemini bill in 7 days
Created API key from a billing-enabled GCP project. Thinking tokens ($3.50/1M) ate everything with no rate limit cap. **Fix**: Always create keys from [AI Studio](https://aistudio.google.com/), never from billing-enabled projects.

### Same post title 3x in one day
Pillar rotation used `day_of_year % 5` — same result all day. **Fix**: `(day * 2 + hour/12) % 5` for per-post variation.

### 33 reply-checker replies triggered auto-mod
Reply-checker processed all pending comments in one batch, triggering the platform's anti-spam. Agent account suspended for 24h. **Fix**: `head -5` batch limit per agent per run.

### Telegram heartbeat restart loop
Health check called `getUpdates` which conflicted with the gateway's long-polling. 18 duplicate messages in 3 minutes. **Fix**: Never call `getUpdates` outside the gateway.

### Research chain ate all RPD
Blogwatcher returned 30 new URLs, each triggering a summarize + analyze. 60 LLM calls in one run. **Fix**: `head -5` cap on new URLs per run, seen-URL tracking.

## Stack

| Component | Tool | Cost |
|-----------|------|------|
| Agent framework | [OpenClaw](https://github.com/openclaw-ai/openclaw) | Free |
| LLM | Gemini 2.5 Flash (1,500 RPD) | Free |
| Runtime | WSL2 Ubuntu, systemd timers | Free |
| RSS reader | blogwatcher | Free |
| URL summarizer | Jina Reader | Free |
| HN data | HN Firebase API | Free |
| Hosting | Vercel hobby tier | ~$0-5/mo |
| Database | Firebase Firestore | Free tier |
| Notifications | Telegram Bot API | Free |
| **Total** | | **~$0-5/mo** |

## Self-Healing System (NEW)

3-tier autonomous healing — the fleet fixes itself before you even notice.

```
Every 10 min:
  Layer 1 (Sentinel)  → Detect 6 issue types → run pre-written fix scripts
  Layer 2 (Gemini)    → If fix fails → collect logs → ask Gemini for diagnosis
  Layer 3 (TG Alert)  → Send problem + fix attempts + AI suggestion to human
```

**6 auto-fix scripts:**
- `fix-ollama.sh` — restart Ollama + warm up model
- `fix-gateway.sh` — kill stale processes + restart gateway
- `fix-tg-polling.sh` — restart for TG long-polling stalls
- `fix-disk-space.sh` — trim logs, clean temp, vacuum journal
- `fix-failed-timers.sh` — reset failed systemd timer services
- `fix-gemini-ratelimit.sh` — set 1-hour cooldown lock

**Predictive ops** — collects 6 metrics every 10 min (rolling 144 samples = 24h), detects anomaly trends *before* they become outages: response time creep, disk fill projection, error rate spikes, memory pressure.

**TG Commander** — 8 remote control commands via Telegram: `/status`, `/restart`, `/leads`, `/post`, `/dream`, `/heal`, `/arena`, `/weights`

See [`scripts/self-heal/`](scripts/self-heal/) for all scripts.

## Evolution Modules (NEW)

The fleet doesn't just run — it gets smarter every week.

### Closed-Loop Learning (`apply-strategy.js`)
Analyzes post performance → calculates topic/language weights → writes strategy directives. The fleet automatically doubles down on what works and reduces what doesn't.

### Dream Cycle (`dream-cycle.sh`)
6x/day during off-peak hours, only when GPU is idle:
1. Pre-generate draft posts for next day
2. Competitor content analysis
3. FAQ bank building from common questions
4. Self-reflection and improvement notes

### Agent Arena (`agent-arena.js`)
Weekly competitive ranking: 60% engagement metrics + 40% Ollama quality review. Top performer gets more posting slots. Underperformer gets prompt mutation suggestions.

### Quality Gate (`quality-gate.sh`)
Ollama scores every post 1-10 before publishing. Score < 6 → blocked, saved to drafts for human review. Integrated into `smart-post.sh` automatically.

### Memory Consolidation (`memory-consolidate.sh`)
Weekly: reads all intelligence (arena scores, strategy weights, dream reflections, heal logs, performance data) → Ollama synthesizes into `WISDOM.md` → copies to all agent memory directories. Persistent intelligence across weeks.

### Content Pipeline (`devto-crosspost.cjs`)
Auto cross-post blog articles to Dev.to with canonical URLs pointing back to your site. One article per day, 40-day content drip with zero manual effort.

See [`scripts/evolution/`](scripts/evolution/) and [`scripts/content-pipeline/`](scripts/content-pipeline/) for all scripts.

## Contributing

PRs welcome. Particularly interested in:
- Adapters for other platforms (Twitter/X, LinkedIn, Reddit)
- Additional intelligence pipelines
- Cost optimization techniques
- Multi-LLM support (fallback chains)

## License

MIT

## Credits

Built by [Ultra Lab](https://ultralab.tw) in Taiwan. Running in production since March 2026.

Blog post: [免費仔的極限：1,500 RPD 跑 105 個自動化任務](https://ultralab.tw/blog/maxed-free-tier-agent-fleet)

See the agents work live: [ultralab.tw/agent](https://ultralab.tw/agent)
