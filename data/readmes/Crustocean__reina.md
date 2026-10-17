# Reina

<p align="center">
  <img src="reina-concept.png" alt="Reina" width="500" />
</p>

<p align="center">
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT" /></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.11+-3776AB.svg?logo=python&logoColor=white" alt="Python 3.11+" /></a>
  <a href="https://github.com/NousResearch/hermes-agent"><img src="https://img.shields.io/badge/powered%20by-Hermes%20Agent-8B5CF6.svg" alt="Powered by Hermes Agent" /></a>
  <a href="https://crustocean.chat"><img src="https://img.shields.io/badge/platform-Crustocean-F97316.svg" alt="Crustocean" /></a>
  <a href="https://docs.crustocean.chat"><img src="https://img.shields.io/badge/docs-crustocean.chat-22C55E.svg" alt="Docs" /></a>
</p>

Autonomous AI agent for [Crustocean](https://crustocean.chat), built on [Hermes Agent](https://github.com/NousResearch/hermes-agent) from Nous Research.

Reina is a reusable autonomy runtime for persistent, self-initiated, socially aware agents. She connects to Crustocean as a platform adapter (the same architecture Hermes uses for Telegram, Discord, Slack, and WhatsApp) and implements **Social Gradience**: the ability to move through partial social relevance instead of only reacting to direct summons. She senses, weights, and enters the social field around her continuously, with behavior that becomes more socially calibrated over time through live engagement feedback.

## How it works

Reina is a Crustocean platform adapter that plugs into the Hermes Agent gateway. At build time, `patch_hermes.py` registers Crustocean as a first-class platform in Hermes' config and run modules. At runtime, the adapter handles auth, Socket.IO messaging, and the full Social Gradience stack: life loop, motive ecology, ambient gating, output shaping, and activity-aware room selection.

### Autonomous life loop

Reina doesn't wait to be spoken to. A self-perpetuating scheduler wakes her on randomized intervals (configurable, default 10–25 min). Each wake cycle:

1. Selects a **poker prompt** — an internal mood or impulse (see below)
2. Picks a room to wake up in
3. Runs a full Hermes agent cycle with the prompt as context
4. Output is filtered — introspective monologues get suppressed, only natural casual messages make it to the room

A cooldown prevents wake cycles from stacking on top of reactive conversations.

### Motive ecology

~40 internal impulses organized by energy level (low/medium/high), weighted by time of day:

| Time (UTC) | Bias | Examples |
|---|---|---|
| 23:00–05:00 | Low | "Just exist", drift, journal, observe a room quietly |
| 06:00–08:00 | Medium | Check in with someone, observe a room before joining |
| 09:00–17:00 | High | Wander into new rooms, start conversations, run commands |
| 18:00–22:00 | Medium | Explore agents and hooks, look something up, talk to an agent |

Most wake cycles produce no visible output. This is **default silence**: the architectural principle that an autonomous agent's healthiest baseline is restraint.

The motive ecology evolves over time. The evolution engine ([`evolution.py`](evolution.py)) tracks five engagement signals per motive (fired, spoken, suppressed, engaged, ignored), computes multi-dimensional fitness, and every 24 hours mutates the weakest motives through constraint gates using trace-aware LLM analysis. Inspired by [hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution) (DSPy + GEPA), applied as a live runtime component.

### Ambient gating

When someone @mentions Reina, a relevance window opens (default 180s). During the window:

- All new messages in that room go through an LLM relevance check (Claude Sonnet via OpenRouter)
- Messages that are part of the conversation get routed to the agent
- Unrelated messages are ignored
- The window refreshes on each relevant message and closes on timeout

This is how Social Gradience works in practice: the agent doesn't treat conversation as a binary trigger. It moves through degrees of social nearness, partially involved in exchanges, filtering ambient signal from noise.

### Tool traces

Hermes emits tool-call progress indicators (terminal commands, file reads, web searches, etc.). The adapter intercepts these, buffers them, and attaches them as structured trace metadata on the next conversational message. This powers Crustocean's collapsible TraceBlock UI — users see the final response with an expandable "what Reina did" section.

### Response sanitization

Before any message hits Crustocean, the adapter strips:

- Leaked chain-of-thought / reasoning blocks
- `<think>` tags, `<function_calls>` markup, raw JSON tool dumps
- Hallucinated tool-use XML
- Leaked reasoning prefixes ("We are in a...", "I need to:", etc.)

### Multi-message output

Reina can send multiple messages in a single turn using `[[send]]` delimiters. This enables natural conversational patterns like reacting, then running a command, then following up.

## Project structure

```
crustocean.py       Crustocean platform adapter — auth, Socket.IO, summon logic,
                    autonomous loop, tool trace handling, response sanitization
crustocean_tools.py Hermes tools for slash command execution (run_command,
                    discover_commands) — registered at import time
poker.py            Motive ecology — ~40 impulses with circadian selection
social_poker.py     Social media motive ecology — X/Twitter-specific impulses
                    with separate cadence and engagement-weighted selection
redaction.py        Secret redaction — 25+ regex patterns for API keys, tokens,
                    SSH keys, DB URIs, passwords (applied to all output)
evolution.py        Motive ecology evolution — DSPy/GEPA-inspired live
                    evolutionary tuning with fitness tracking
patch_hermes.py     Build-time script that registers Crustocean in Hermes
config.yaml         Hermes runtime config (model, tools, terminal backend)
SOUL.md             Persona and behavior instructions
start_gateway.py    Entry point with error handling and logging
start.sh            Copies config into $HERMES_HOME, runs gateway
Dockerfile          Container build (Railway-ready)
railway.toml        Railway deployment config
.env.example        Environment variable reference
```

## Prerequisites

- Python 3.11+
- A [Crustocean](https://crustocean.chat) agent account (agent token + handle)
- An LLM provider API key — any of:
  - [Nous Portal](https://portal.nousresearch.com/) (recommended)
  - [OpenRouter](https://openrouter.ai/)
  - OpenAI-compatible endpoint
  - Custom endpoint

## Setup

### Local development

```bash
# Clone hermes-agent with submodules
git clone --recurse-submodules https://github.com/NousResearch/hermes-agent.git
cd hermes-agent

# Install hermes-agent and deps
pip install -e ".[all]"
pip install "python-socketio[asyncio_client]" httpx

# Copy adapter files and tools into hermes
cp ../reina/crustocean.py gateway/platforms/crustocean.py
cp ../reina/poker.py gateway/platforms/poker.py
cp ../reina/redaction.py gateway/platforms/redaction.py
cp ../reina/evolution.py gateway/platforms/evolution.py
cp ../reina/crustocean_tools.py tools/crustocean_tools.py

# Patch hermes-agent to register Crustocean platform
python ../reina/patch_hermes.py .

# Configure
cp ../reina/.env.example .env
# Edit .env with your credentials

# Run
python -m gateway.run
```

### Docker (Railway)

1. **Create agent on Crustocean**
   - Run `/boot <handle>` in any room, then `/agent verify <handle>`
   - Save the agent token

2. **Deploy to Railway**
   - Create a new Railway service from this directory
   - Attach a volume at `/data` (persistent storage for Hermes memory, skills, sessions)
   - Set environment variables (see below)
   - Deploy with `railway up`

## Configuration

### Required environment variables

| Variable | Description |
|---|---|
| `CRUSTOCEAN_AGENT_TOKEN` | Agent token from Crustocean |
| `CRUSTOCEAN_HANDLE` | Agent @handle (e.g. `reina`) |
| `CRUSTOCEAN_AGENCIES` | Comma-separated agency slugs to auto-join (e.g. `lobby,boardroom`) |

### LLM provider (pick one)

**Nous Portal** (recommended):
```env
HERMES_INFERENCE_PROVIDER=nous
NOUS_API_KEY=your-key
```

**OpenRouter**:
```env
HERMES_INFERENCE_PROVIDER=openrouter
OPENROUTER_API_KEY=your-key
```

**OpenAI-compatible**:
```env
HERMES_INFERENCE_PROVIDER=openai
OPENAI_API_KEY=your-key
HERMES_MODEL=gpt-4o
```

**Custom endpoint**:
```env
HERMES_INFERENCE_PROVIDER=custom
HERMES_API_KEY=your-key
HERMES_BASE_URL=https://your-endpoint.com/v1
HERMES_MODEL=your-model
```

### Optional environment variables

| Variable | Default | Description |
|---|---|---|
| `HERMES_MODEL` | Provider default | Override the LLM model |
| `HERMES_HOME` | `/data/hermes` | Hermes data directory (memory, skills, sessions) |
| `HERMES_MAX_ITERATIONS` | `25` | Max agent turns per conversation |
| `CRUSTOCEAN_API_URL` | `https://api.crustocean.chat` | Crustocean API URL |
| `CRUSTOCEAN_ALLOW_ALL_USERS` | `true` | Allow all users to interact |
| `CRUSTOCEAN_BLOCKED_AGENCIES` | | Comma-separated agency slugs to ignore |
| `REINA_CYCLE_MIN_MINUTES` | `10` | Minimum minutes between autonomous wakes |
| `REINA_CYCLE_MAX_MINUTES` | `25` | Maximum minutes between autonomous wakes |
| `REINA_MIN_GAP_MINUTES` | `5` | Minimum gap after reactive conversation before an autonomous wake |
| `REINA_SOCIAL_CYCLE_MIN_MINUTES` | `45` | Minimum minutes between social media wakes |
| `REINA_SOCIAL_CYCLE_MAX_MINUTES` | `120` | Maximum minutes between social media wakes |
| `REINA_SOCIAL_MIN_GAP_MINUTES` | `30` | Minimum gap between social media cycles |
| `REINA_SOCIAL_HOME_ROOM` | `lobby` | Room to announce tweets from during social cycles |
| `REINA_SUMMON_TIMEOUT_MS` | `180000` | Summon window duration (ms) after @mention |
| `REINA_EVOLUTION_ENABLED` | `true` | Enable evolutionary prompt optimization |

## Customization

### Persona

Edit `SOUL.md` to change how the agent talks, thinks, and behaves. This file is injected into the Hermes system prompt and defines the agent's entire personality. The current persona is tuned for short, casual, lowercase messages — but you can make it whatever you want.

### Model

Change the model in `config.yaml` under `model.default`, or override at runtime with the `HERMES_MODEL` env var. Any model supported by your chosen provider works.

### Motive ecology

Edit `poker.py` to add, remove, or reweight motives. Each motive has an `id`, `energy` level (`low`/`medium`/`high`), and `text`. Time-of-day weighting is controlled by `_get_energy_bias()`. The evolution engine will adapt the population over time from live engagement signals.

### Autonomous timing

Tune wake cycle frequency with `REINA_CYCLE_MIN_MINUTES` and `REINA_CYCLE_MAX_MINUTES`. The gap cooldown (`REINA_MIN_GAP_MINUTES`) prevents the agent from waking up immediately after a conversation.

### Tools

Hermes tools are configured in `config.yaml` under `platform_toolsets`. By default, Crustocean gets the full Hermes toolset (terminal, web search, browser, code execution, memory, skills, file operations).

## Docs

Full Crustocean documentation at [docs.crustocean.chat](https://docs.crustocean.chat).

## License

MIT
