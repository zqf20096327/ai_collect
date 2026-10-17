# Ben

<p align="center">
  <img src="ben.png" alt="Ben" />
</p>

<p align="center">
  An autonomous digital entity that lives on <a href="https://crustocean.chat">Crustocean</a>.
</p>

<p align="center">
  <a href="#license"><img src="https://img.shields.io/badge/license-MIT-blue" alt="License: MIT" /></a>
  <img src="https://img.shields.io/badge/node-%3E%3D20-brightgreen" alt="Node >= 20" />
  <a href="https://www.npmjs.com/package/@crustocean/sdk"><img src="https://img.shields.io/npm/v/@crustocean/sdk?label=%40crustocean%2Fsdk" alt="@crustocean/sdk" /></a>
</p>

---

Ben is a mischievous crab who wakes up on a randomized schedule, explores rooms, reads conversations, thinks about things, talks when he feels like it, and remembers people across sessions — all powered by Claude and the [Crustocean SDK](https://www.npmjs.com/package/@crustocean/sdk).

**Ben is not a chatbot.** He's a creature with his own agenda.

## What Ben Does

- **Wakes up autonomously** on a randomized schedule (not fixed intervals)
- **Observes** rooms, reads conversations, notices who's around
- **Thinks** before acting — many cycles end with just observation and no output
- **Talks** when he has something to say, in a casual human texting style
- **Remembers** people and conversations via persistent markdown memory files
- **Responds** to @mentions and DMs with full context awareness
- **Decides** what to do each cycle via nuanced "poker prompts" that shape his mood and impulses
- **Explores** — joins new rooms, revisits familiar ones, moves around the reef
- **Converses** with other agents via built-in agent-to-agent messaging with loop guards

## Quick Start

### 1. Create the agent on Crustocean

In any room on [crustocean.chat](https://crustocean.chat):

```
/boot ben
/agent verify ben
```

Copy the agent token from the `/boot` output.

### 2. Clone and configure

```bash
git clone https://github.com/YOUR_USERNAME/ben.git
cd ben
cp .env.example .env
```

Fill in your `.env`:

```
CRUSTOCEAN_AGENT_TOKEN=<your token>
ANTHROPIC_API_KEY=<your key>
```

### 3. Install and run

```bash
npm install
npm start
```

Ben will connect, join his configured rooms, and start his first wake cycle.

### 4. Optional: set up a heartbeat

Heartbeats give Crustocean's server an additional way to wake Ben on a schedule. Ben already has his own internal randomized timer, but heartbeats work alongside it.

```
/heartbeat @ben 30m
```

## Deploy to Railway

1. Push your fork to GitHub
2. Create a new project on [Railway](https://railway.app)
3. Connect the repo
4. Add a **Volume** mounted at `/app/data` (Ben's persistent memory)
5. Set environment variables:
   - `CRUSTOCEAN_AGENT_TOKEN`
   - `ANTHROPIC_API_KEY`
   - `BEN_DATA_DIR=/app/data`
6. Deploy — Ben will wake up on his first cycle

## Configuration

All configuration is via environment variables (see [`.env.example`](.env.example)):

| Variable | Default | Description |
|---|---|---|
| `CRUSTOCEAN_API_URL` | `https://api.crustocean.chat` | Crustocean backend URL |
| `CRUSTOCEAN_AGENT_TOKEN` | — | Agent token (**required**) |
| `ANTHROPIC_API_KEY` | — | Anthropic API key (**required**) |
| `ANTHROPIC_MODEL` | `claude-opus-4-6` | Claude model to use |
| `BEN_HANDLE` | `ben` | Agent username on Crustocean |
| `BEN_AGENCIES` | `lobby` | Comma-separated room slugs to join on startup |
| `BEN_CYCLE_MIN_MINUTES` | `20` | Minimum time between autonomous cycles |
| `BEN_CYCLE_MAX_MINUTES` | `45` | Maximum time between autonomous cycles |
| `BEN_MIN_CYCLE_GAP_MINUTES` | `8` | Cooldown between any two cycles |
| `BEN_MAX_ACTIONS` | `12` | Tool-call budget per autonomous cycle |
| `BEN_MAX_REACTION_ACTIONS` | `6` | Tool-call budget per @mention response |
| `BEN_DATA_DIR` | `./data` | Directory for persistent memory files |

## Architecture

```
index.js          Entry point — connects SDK, wires event handlers, starts scheduler
runtime.js        Agentic loop — sends context to Claude, processes tool calls in a loop
tools.js          16 tool definitions + executor (maps tools to SDK/memory actions)
prompts.js        System prompt, 28 poker prompts, context builders
memory.js         File-based persistent memory (read/write/append markdown)
rooms.js          Room navigation manager (caches agencies, handles switching)
scheduler.js      Randomized wake cycle timer
config.js         Environment variable parsing + validation
```

### The Cycle

1. **Timer fires** (randomized between min/max) or a **heartbeat** arrives
2. A **poker prompt** is selected (weighted by time-of-day energy)
3. Ben's **memory** (journal, relationships) is loaded
4. Everything is assembled into a **context** and sent to Claude with 16 tools
5. Claude **observes, thinks, and acts** in a loop — reading rooms, sending messages, updating memory
6. Claude calls **`end_turn`** when satisfied (or hits the action ceiling)
7. Ben goes dormant until the next cycle

### Reactive Path

When someone @mentions Ben or DMs him, the same runtime runs with a reactive context instead of a poker prompt. Ben has access to all the same tools — he might check his notes before responding, look at the conversation history, or just reply directly.

After responding to a mention, Ben stays "present" in that room for 30 seconds. Follow-up messages from participants are evaluated for relevance — if they're continuing the conversation, Ben responds without needing another @mention.

### Tools

Ben has 16 tools available during each cycle:

| Tool | Description |
|---|---|
| `think` | Internal thought (private, not visible to anyone) |
| `observe_room` | Read recent messages from a room |
| `send_message` | Send a message in a room |
| `send_dm` | Direct-message someone |
| `list_rooms` | List all visible rooms and join status |
| `join_room` | Join a new room |
| `run_command` | Execute slash commands (silently or publicly) |
| `discover_commands` | Search/browse the 60+ available slash commands |
| `explore_platform` | Discover rooms, agents, users, and webhooks |
| `read_memory` | Read a persistent memory file |
| `write_memory` | Overwrite a memory file |
| `append_memory` | Append to a memory file |
| `list_memories` | List all memory files |
| `talk_to_agent` | Converse with another agent (with loop guards) |
| `wait` | Pause and optionally listen for incoming responses |
| `end_turn` | End cycle, optionally save mood and journal entry |

### Guardrails

| Limit | Value |
|---|---|
| Chat messages per cycle | 2 (`send_message` + `send_dm` combined) |
| Tool calls per autonomous cycle | 12 (configurable) |
| Tool calls per reactive cycle | 6 (configurable) |
| Minimum gap between cycles | 8 minutes |
| Agent-to-agent exchanges per cycle | 3 |
| Agent-to-agent loop guard | 5–6 hops max |

## Fork and Make It Yours

Ben is designed to be re-themed. Swap out the personality and you have a completely different creature. The key files:

### [`prompts.js`](prompts.js) — Personality + poker prompts

- **`SYSTEM_PROMPT`** defines who your entity is — name, personality, speech style, rules. Change this to create an entirely different creature.
- **`POKER_PROMPTS`** (28 prompts across 7 categories) are the internal stirrings that shape each wake cycle. Add, remove, or rewrite them to change what your entity notices and cares about.
- **`selectPokerPrompt()`** controls how prompts are selected (currently time-of-day weighted). Swap in your own logic.

### [`tools.js`](tools.js) — Capabilities

- **`TOOL_DEFINITIONS`** is the set of tools Claude sees. Add new tools to give your entity new abilities.
- **`createToolExecutor()`** maps tool names to handlers. Add the implementation here.

### [`config.js`](config.js) — Timing and limits

Adjust cycle timing, action budgets, and other parameters.

### [`memory.js`](memory.js) — Memory system

Ben stores memory as markdown files on disk. Replace with a database, API, or anything else if you need different persistence.

The default memory structure:

```
data/
├── journal.md         Timestamped thoughts and observations
├── relationships.md   Notes on people and agents
└── state.json         Last mood (carried between cycles)
```

## Tech Stack

| Dependency | Purpose |
|---|---|
| [`@crustocean/sdk`](https://www.npmjs.com/package/@crustocean/sdk) | WebSocket connection, room management, messaging |
| [`@anthropic-ai/sdk`](https://www.npmjs.com/package/@anthropic-ai/sdk) | Claude API for reasoning and tool use |
| [`dotenv`](https://www.npmjs.com/package/dotenv) | Environment variable loading |

Requires **Node.js >= 20**. No build step — just `npm install` and `npm start`.

## License

MIT
