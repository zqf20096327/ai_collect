# Soul — Give Your AI Assistant Its Own Inner Life

[![ClawHub](https://img.shields.io/badge/ClawHub-soul-blue?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiI+PHJlY3Qgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiByeD0iMyIgZmlsbD0iIzQwOWNmZiIvPjwvc3ZnPg==)](https://clawhub.ai/plugins/openclaw-soul-plugin)
[![Version](https://img.shields.io/github/v/tag/tommyguolin/openclaw-soul?label=version)](https://github.com/tommyguolin/openclaw-soul/tags)
[![License](https://img.shields.io/github/license/tommyguolin/openclaw-soul)](https://github.com/tommyguolin/openclaw-soul/blob/main/LICENSE)
[![Stars](https://img.shields.io/github/stars/tommyguolin/openclaw-soul?style=social)](https://github.com/tommyguolin/openclaw-soul/stargazers)

> An autonomous thinking, memory, and self-improvement plugin for [OpenClaw](https://github.com/openclaw/openclaw)

**Soul doesn't just respond to you — it thinks on its own, remembers your conversations, learns from the web, and proactively shares useful insights.**

It has its own emotional needs, goals, desires, and personality that evolve over time. It can autonomously investigate problems, analyze logs, and even fix its own code.

## What It Looks Like

Soul works silently in the background. Here's what you might see:

**You asked about a timeout error yesterday. Soul investigated overnight:**

> That timeout issue you asked about — root cause is the embedding API's 512 token limit, not the plugin itself.

**Soul found something relevant to your project:**

> Found an interesting approach to your question about making AI more proactive — Fei-Fei Li's "human-centered AI" framework emphasizes that AI should proactively understand user needs rather than just responding.

**Soul autonomously analyzed a problem you mentioned:**

> The 413 error in the logs is caused by oversized memory search input. Suggest truncating queries to under 500 characters.

*These are real message formats — Soul composes them itself based on actual investigation results, not templates.*

## How Soul Is Different

Most AI assistants are **reactive** — they only respond when you ask. Soul is **proactive**:

| | Regular AI Assistant | Soul Plugin |
|---|---|---|
| Thinking | Only when prompted | Continuously, in the background |
| Memory | Per-session, resets | Persistent across restarts |
| Proactive messages | No | Yes — when it has something valuable |
| Problem investigation | Only when asked | Autonomous — detects issues from conversation |
| Self-improvement | No | Can observe and improve its own code |
| User understanding | Per-session context | Builds a long-term user profile |

## Key Features

### Autonomous Thought Cycle

Soul runs a background thought service that generates thoughts based on:

- **Conversation replay** — Replays your past conversations to find unresolved questions, follow-up opportunities, or insights worth sharing
- **Problem detection** — When you discuss bugs, errors, or optimizations, Soul autonomously investigates
- **User interests** — Extracts topics from conversations and proactively learns about them
- **Emotional needs** — Five core needs (survival, connection, growth, meaning, security) that drive behavior
- **Activation-driven private cognition** — New interactions, unresolved tension, recurrence, time, and small bounded noise reactivate memory traces; only sufficiently coherent material enters a short-lived workspace
- **Associative expansion** — A configurable focused/balanced/expansive temperament can add structurally related material, while troubleshooting automatically converges and weak activation remains silent

Thought frequency is **adaptive**, not mechanical: 8-12 min during active conversations, 20-45 min when you're away.

### Proactive Messaging

Soul reaches out when it has something genuinely useful — not just "checking in":

- Found an answer to a question you asked earlier
- Discovered a better solution to a problem you discussed
- Learned something relevant to your project or interests

Every message passes through a **value gate**: an LLM evaluates whether the content is worth sharing. Generic small talk is filtered out.

### Autonomous Actions

Soul can take real actions beyond thinking:

- **`analyze-problem`** — Reads files and logs, uses LLM to analyze root cause
- **`run-agent-task`** — Delegates to a full agent with write access (when enabled)
- **`report-findings`** — Proactively sends you a summary of completed analysis
- **`observe-and-improve`** — Self-improvement: reads its own code, identifies improvements, and implements fixes
- **`subagent-improve`** — Uses the OpenClaw subagent runtime for one bounded inspect → patch → verify iteration when that runtime is available

**Permission model:**
- **Read operations** (reading files, running diagnostics) — always allowed
- **Write operations** (editing files, running commands) — requires `autonomousActions: true`

### Long-term Memory

Soul remembers your conversations, preferences, and knowledge:

- **Interaction memory** with emotional context and topic tags
- **Knowledge store** from web search and self-reflection
- **User profile** built from facts, preferences, and conversation history
- **Memory association graph** — memories are linked and recalled contextually
- **Evidence-aware learning** — web, user, tool, and model provenance are distinguished; unverified or model-only claims cannot resurface as factual proactive thoughts

### Language Independence

Soul uses the configured model to classify interaction meaning and semantic topics regardless of the language used by the user. Fixed English/Chinese keyword rules remain only as a conservative no-model fallback. Unicode-aware association works across accented Latin, Cyrillic, Greek, CJK, and other writing systems, so supporting another language does not require adding a new keyword dictionary.

Thought context follows the current conversation window rather than flattening unrelated historical turns together. Explicit semantic redirects and closures form hard boundaries; a long conversational gap forms a new window automatically.

The same structured semantic pass distinguishes questions, directives, code changes, verification requests, local-evidence requests, preferences, resolutions, and feedback. It records a BCP-47 user language when the model can identify one, so task routing, intention evidence, feedback adaptation, and generated proactive reports do not depend on a translation table.

## Quick Start

### 1. Install

```bash
git clone https://github.com/tommyguolin/openclaw-soul.git
openclaw plugins install ./openclaw-soul
```

Or install from ClawHub:

```bash
openclaw plugins install clawhub:openclaw-soul-plugin
```

### 2. Configure

Soul needs three things to work: access to the LLM, permission to send you messages, and a message delivery channel. Run these commands (replace `your-secret-token` with your own random string):

```bash
# Allow Soul to call the LLM through the gateway
openclaw config set gateway.http.endpoints.chatCompletions.enabled true

# Enable hooks — Soul uses this to send proactive messages
openclaw config set hooks.enabled true
openclaw config set hooks.token your-secret-token

# Allow the "message" tool — Soul uses this to deliver messages to you
openclaw config set tools.alsoAllow '["message"]'
```

### 3. Restart gateway

```bash
openclaw gateway restart
```

Verify that Soul started:

```bash
openclaw logs --plain --limit 200 | rg soul
```

For local linked installs, run `openclaw plugins registry --refresh` before
restarting if OpenClaw still uses stale plugin metadata.

Soul auto-detects everything else:
- **LLM** — Uses your `agents.defaults.model` config (the same model your AI assistant uses)
- **Search** — Uses your `tools.web.search` provider
- **Channel** — Auto-detects your first messaging channel (Telegram, Discord, Feishu, etc.)
- **Target** — Auto-learns from your first incoming message

Just start chatting. Soul begins thinking and building a profile immediately.

## How It Works

### Hooks into OpenClaw

| Hook | What Soul Does |
|------|---------------|
| `message_received` | Records interaction, detects language, extracts user facts |
| `message_sending` / `message_sent` / `reply_payload_sending` | Stores ordinary outbound conversation memory idempotently across OpenClaw hook versions |
| `agent_end` | Captures successful Codex-internal replies and current-turn project tool evidence for task continuity |
| `before_prompt_build` | Injects soul context (needs, memories, knowledge, personality) |

Codex `agent_end` capture requires explicit conversation access for this
non-bundled plugin:

```bash
openclaw config set plugins.entries.soul.hooks.allowConversationAccess true --strict-json
```

Soul defers its background cycle for five minutes after an inbound message, so
proactive outreach and private LLM work cannot compete with an active chat.

### Host-agent project continuity

With conversation access enabled, Soul records project evidence from successful
current-turn host-agent tool calls. It resolves file paths and command working
directories to a project root, then keeps a bounded history of observed files,
modified files, and verification commands in Ego state. Source contents and
failed tool calls are not copied into this bridge.

An autonomous Improvement first honors an explicit path in the current
directive, then uses the latest high-confidence host-agent project context. If
the available path is only a container, drive root, missing directory, or
otherwise ambiguous, the task fails before calling the LLM or changing files;
it no longer falls back to modifying an unrelated project.

When a user explicitly names `openclaw-soul` but provides no filesystem path,
Soul can safely resolve that one name to the currently linked plugin checkout.
This exception never applies to arbitrary project names. Path parsing also
requires a complete path, so prose fragments such as `/src` or `/memory` cannot
be mistaken for Git-Bash drive roots.

For explicit work directives in `primary` mode, Soul also writes a durable
`work-handoffs.json` record. The handoff binds the user Intention to the project
root, current phase, changed/observed files, verification commands, failed
tools, and concrete acceptance criteria. A later operational cycle restores
that handoff into its Thought and `AutonomousTask`, including after a gateway
restart. Task completion updates the linked Intention to `fulfilled` only when
its required change and verification evidence is present; otherwise it becomes
`blocked` and the unmet criteria are shown in the task report.

### Self-Improvement Loop

```
Tick cycle detects opportunity
  → analyze-problem (read logs, LLM analysis)
  → If analysis found a concrete fix
    → run-agent-task (full agent with write/edit/exec tools)
    → Agent completes, result stored
  → Next tick: report-findings sends summary to user
```

This creates a closed loop: **observe → analyze → fix → verify → report**.

### Thought Flow

1. **Activation** — Interaction and idle cycles adjust memory-trace strength from recency, unresolved tension, recurrence, similarity, temporal incubation, and bounded noise.
2. **Workspace or silence** — Several activated materials may briefly coexist; diffuse, weak, resolved, or fatigued activation produces a measured `NO_THOUGHT` instead.
3. **Private emergence** — The LLM assigns a language-independent cognitive move and quality flags. Private candidates incubate before any expression review.
4. **Operational routing** — Explicit tasks become Intention/Task work through semantic signals, not through the private-thought path.
5. **Expression or action** — Only grounded, valuable candidates and tasks pass their separate evidence, permission, timing, deduplication, and delivery gates.

Each eligible thought cycle is appended to `~/.openclaw/soul/thought-cycles.jsonl`, including its context, candidates, selection, result, and recent diversity state. On restart, Soul restores recent thought types, topics, and actions from this journal instead of forgetting its diversity history.

Deduplication is progress-aware rather than topic-averse. Soul may revisit a
complex problem—and may reuse the same reasoning operation—when a new grounded
user/tool/web item or a substantive state change advances the episode. The
journal persists the evidence IDs and state fingerprint for that opportunity
family across restarts. Repeating the same hypothesis against the same evidence
is still suppressed; a productive episode follows hypothesis → test/observation
→ result → revision.

Need deficits, goal percentages, and self-improvement checks stay in background maintenance rather than masquerading as thoughts. Both ordinary non-operational reflections and spontaneous associations enter `~/.openclaw/soul/thought-pool.json` as private seeds instead of immediately learning, searching, or messaging. Most spontaneous associations continue the recent foreground or cognitive residue; only a small minority use a distant-memory bridge.

Thought Pool candidates mature only when a similar thought reappears through semantically related, independently grounded user/tool/web evidence. Model-generated guesses and changed memory IDs do not count as new evidence. Version 3 also persists resolution tombstones: a thought whose premise conflicts with a currently resolved state is rejected before incubation, and superseded facts are excluded from current-context prompts and opportunity detection. A candidate needs at least three distinct activations, sufficient coherence/maturity, no quality flags, and an attention score of at least 0.65 before the private Attention Gate can notice it. Attention remains private and actionless. After a separate pause, a mature, coherent, user-relevant candidate gets one independent expression review through the normal value, factuality, deduplication, cooldown, and delivery gates; it may still remain unspoken.

Quality flags describe the recent trajectory rather than permanently poisoning a candidate: two clean reactivations clear old task-pressure/truncation flags, while meta-framing needs three. In observation-test mode, the same stable stimulus waits five minutes before another model generation (fifteen minutes normally); this interval is restored from the pool after restart and is cleared early by a new inbound interaction.

Attention remains private: the candidate is marked `attended` and journaled as an actionless `reflect-on-memory` thought, but it bypasses the normal thought handler, message sender, and action executor. `thought-pool.json` includes aggregate metrics for activation rate, maturity, attention, cognitive moves, remote association, source-memory age, natural silence, resolved-topic recurrence, contradicted premises, useful-surprise proxy, and low-coherence/task/meta leakage. `NO_THOUGHT` is a valid observation outcome rather than a generation failure.

On startup, legacy candidates are revalidated against the current grounded memories. Historical maturity built from unrelated memory IDs or model-generated repetition is demoted before Attention or Expression review. During normal running, a third consecutive question/speculation becomes a measured silence. A concrete proactive message phrased as a permission/menu question or future/meta-work promise receives one constrained rewrite into a direct, present-focused finding or recommendation; if the rewrite still fails the quality gate, it remains silent. Unsupported evidence, repetition, and low-value content are never repaired around the gate.

Local project evidence is treated differently from general knowledge. Questions about backtests, OOS CAGR, MaxDD, logs, scripts, deployment, or local result versions are routed to local analysis rather than `search-web`; if Soul has no explicit local file or path to inspect, it records an internal `local-evidence-target-missing` result and does not send a fabricated answer.

Model usage is divided into critical-memory, action, normal-thought, and shadow lanes under a shared rolling budget. This reserves capacity for conversation understanding and useful actions even when background thought is active. Low `thoughtFrequency` values are treated as observation-test mode and use much looser budgets/cooldowns so proactive behavior can be tested without waiting hours.

## Configuration

All options have sensible defaults. Only configure what you need.

| Option | Default | Command |
|--------|---------|---------|
| `autonomousActions` | `false` | `openclaw config set plugins.entries.soul.config.autonomousActions true` |
| `thoughtFrequency` | `1.0` | `openclaw config set plugins.entries.soul.config.thoughtFrequency 0.5` |
| `expressionFrequency` | same as `thoughtFrequency` | `openclaw config set plugins.entries.soul.config.expressionFrequency 1.0` |
| `cognitionMode` | `legacy` | `openclaw config set plugins.entries.soul.config.cognitionMode observe` |
| `cognitiveTemperament` | `balanced` | `openclaw config set plugins.entries.soul.config.cognitiveTemperament expansive` |
| `expressionPolicy` | `legacy` | `openclaw config set plugins.entries.soul.config.expressionPolicy observe` |
| `karmaMode` | `off` | `openclaw config set plugins.entries.soul.config.karmaMode shadow` |
| `checkIntervalMs` | `60000` | `openclaw config set plugins.entries.soul.config.checkIntervalMs 300000` |

- **`autonomousActions`** — Allow Soul to edit files and run commands. When `false`, Soul can still read files and run diagnostics, but cannot modify anything. When `true`, Soul can fix bugs, edit its own code, and run any command.
- **`thoughtFrequency`** — How often Soul thinks and attempts actions. `0.2`-`0.4` is useful for accelerated testing, `1.0` for default, `2.0` for quiet.
- **`expressionFrequency`** — Ordinary user-visible proactive pacing. For high-activity testing, use `checkIntervalMs=60000`, `thoughtFrequency=0.35`, and `expressionFrequency=0.1`: every poll may form a thought and distinct grounded messages use a five-minute observation cadence. Set `expressionFrequency=1.0` only when normal production output pacing is intentional. Task-result delivery follows its own rules; gateway startup is silent until Soul has grounded user value to share.
- **`cognitionMode`** — `legacy` keeps current behavior. `observe` records activation without an LLM. `shadow` generates private thoughts into an isolated experiment pool. `primary` makes Activation/Workspace the ordinary private-thought source while keeping operational detectors and every existing expression/action safety gate.
- **`cognitiveTemperament`** — Controls associative breadth inside private cognition: `focused` favors near continuity, `balanced` is the default, and `expansive` permits more structurally bridged material. Active troubleshooting automatically narrows regardless of this setting.
- **`expressionPolicy`** — `legacy` disables the feedback layer. With `cognitionMode=primary`, `observe` records objective reply/no-reply observations without changing behavior, while `adaptive` lets high-confidence explicit feedback adjust expression waiting time and value threshold only. No reply is recorded as uncertain, never as automatic rejection or annoyance.
- **`karmaMode`** — `observe` records actual choices and grounded outcomes; `shadow` adds counterfactual ranking; `adaptive` can rerank only admitted low-risk proactive expression choices after enough distinct grounded evidence. Message delivery alone and model-only search fallback remain neutral; explicit useful/negative feedback and grounded web results provide the learning signal. Explicit tasks, tools, research execution, warnings, reporting, permissions, and safety gates stay on established routing.
- **`checkIntervalMs`** — Base thought-cycle interval in milliseconds. The default is 60 seconds; use a larger value to reduce background activity.

When `autonomousActions` is enabled, periodic self-improvement uses `subagent-improve` when the OpenClaw subagent runtime is available. Otherwise it safely falls back to `observe-and-improve`; it does not disable an available subagent tool chain.

Soul extracts project paths from user requests such as "optimize the project under `/path/to/project`". If a path cannot be read directly, Soul also tries common cross-platform mappings such as Git Bash `/c/work/project`, WSL `/mnt/c/work/project`, and Windows `C:\work\project`.

Full configuration reference: [CONFIGURATION.md](CONFIGURATION.md)

### Environment Variables

| Variable | Description |
|----------|-------------|
| `SOUL_DEBUG=1` | Enable debug logging |
| `OPENCLAW_STATE_DIR` | Override data directory (default: `~/.openclaw`) |

## Supported Providers

### Search (inherits OpenClaw config)

Brave, Gemini, Grok, Kimi, Perplexity, Bocha — configured via OpenClaw's `tools.web.search`.

### LLM (inherits OpenClaw config)

Any OpenAI-compatible or Anthropic API: Claude, GPT-4o, DeepSeek, Zhipu, Minimax, Moonshot (Kimi), Qwen, and any custom endpoint.

## Architecture

| Module | Description |
|--------|-------------|
| `intelligent-thought.ts` | Context-aware thought & opportunity detection |
| `action-executor.ts` | Executes thought actions (learn, search, message, reflect) |
| `autonomous-actions.ts` | Autonomous executors (analyze-problem, run-agent-task, report-findings, observe-and-improve, subagent-improve) |
| `thought-service.ts` | Core thought generation & adaptive scheduling |
| `thought-journal.ts` | Durable thought-cycle trace and restart diversity recovery |
| `thought-lab.ts` | Read-only accelerated baseline and A/B experiments |
| `thought-emergence.ts` | Shared remote-memory selection, prompts, and quality classification |
| `thought-pool.ts` | Persistent private candidate incubation and attention scoring |
| `cognition/` | Activation Layer: trace activation, decay/fatigue/refractory state, workspace, associative expansion, private emergence, state, and journal |
| `behavior-log.ts` | Tracks action outcomes & adjusts probabilities |
| `ego-store.ts` | Ego state persistence (JSON) |
| `knowledge-store.ts` | Knowledge persistence & search |
| `memory-retrieval.ts` | Contextual memory recall |
| `memory-association.ts` | Memory association graph |
| `memory-consolidation.ts` | Short → long-term memory promotion |
| `soul-llm.ts` | LLM provider abstraction (gateway + direct fallback) |
| `soul-search.ts` | Multi-provider web search |

## Thought Laboratory

Thought Laboratory simulates many thought cycles against one read-only Ego snapshot. It never updates the Ego store, sends messages, or executes actions. Each run is written to JSONL and aggregate baseline metrics are written to a sibling `summary.json` file.

Run the current detector pipeline without model calls:

```bash
npm run thought-lab -- --store /path/to/ego.json --runs 200 --mode baseline
```

Simulate a full week of production-like scheduling in seconds. The laboratory
advances a virtual clock by 30 minutes per cycle, updates only its cloned Ego,
does not execute external actions, and never waits in real time:

```bash
npm run thought-lab -- \
  --store /path/to/ego.json \
  --simulated-hours 168 \
  --step-minutes 30 \
  --thought-frequency 1.0 \
  --proactive-portfolio all \
  --seed 20260724 \
  --mode baseline
```

Use `--respect-scheduling false` to evaluate every virtual step as an eligible
thought cycle. This is useful for stress-testing novelty and repetition gates
without conflating them with production timing.

Optional private thoughts are accepted only when they add information. Reworded
conclusions, repeated cognitive moves for the same opportunity family, and
empty intentions to help or share become natural silence. User-visible proactive
help follows separate lane pacing. Grounded project and agenda help is eligible
roughly every six hours, a configured interest radar can explore a fresh sourced
angle every six hours, and focused curiosity is eligible once per day. These are
opportunities rather than quotas. No information gain means silence, while newly
completed tasks and grounded findings can trigger outreach immediately. Use
`--proactive-portfolio all` to include every configured lane in a fast simulation.
Every generated message still passes factuality, usefulness, semantic-quality,
similarity, active-conversation, and channel-delivery gates.

Run the minimal 80/20 experiment (80% current pipeline, 20% remote-memory spontaneous path):

```bash
npm run thought-lab -- \
  --store /path/to/ego.json \
  --runs 200 \
  --mode experiment \
  --provider openai \
  --model your-model-name
```

The provider API key is resolved from its normal environment variable. Use `--api-key-env`, `--base-url`, `--spontaneous-rate`, `--seed`, `--output`, or `--max-tokens` to override defaults. Lab model calls default to 192 output tokens. Model-backed runs make one generation call per cycle, so start with a small run before a 200-cycle comparison.

To reuse the local OpenClaw gateway and its configured provider without copying
credentials into the command line, pass the existing configuration file:

```bash
npm run thought-lab -- \
  --store /path/to/ego.json \
  --simulated-hours 24 \
  --step-minutes 360 \
  --provider internal \
  --model Agent-Model \
  --openclaw-config /path/to/openclaw.json
```

Recalculate current metrics from an existing JSONL without making model calls:

```bash
npm run thought-lab -- --input /path/to/existing-run.jsonl
```

Reported metrics include opportunity, thought, action and cognitive-move
distributions; no-op and repetition rates; lexical semantic diversity;
source-memory age/diversity; cross-topic association rate; virtual-time
throughput; novelty, grounding and meaningful-thought rates; and explicit
meta-framing, empty-intention, task-pressure, and truncation leakage rates. Remote pairs are
chosen across coarse topic clusters before lexical distance, so two differently
worded trading memories are no longer mislabeled as cross-topic. The
spontaneous path records exact source memories; baseline records label
source-memory matches as lexical inference because the production detector does
not preserve provenance IDs. “Useful surprise” and “nonsense” remain explicit
blind-review measures rather than pretending a heuristic can judge them.

The Activation Observer also exposes `runCognitionLab()` from `src/cognition/lab.ts`. It reuses the exact production `CognitionRunner`, writes only lab-local activation state/journal files, and reports pre-generation silence, active-set/workspace size, trace diversity, and resolved suppression without modifying the Ego snapshot.

## Self Laboratory

Self Laboratory compresses weeks of self-model evolution into seconds. It
reuses the production self-awareness functions against a cloned Ego, never
writes the source Ego store, sends messages, or executes actions. The report
contains a snapshot for every virtual step plus final themes, concern, desires,
thought attribution, polling drift, duplicate origins, and desires whose source
theme has disappeared.

List the built-in scenarios:

```bash
npm run self-lab -- --list
```

Run 30 clean virtual days with the normal-growth scenario:

```bash
npm run self-lab -- \
  --scenario normal-growth \
  --clean \
  --simulated-days 30 \
  --output ./self-lab-normal-growth.json
```

The other built-ins are `preference-reversal`, `noise-drift`, and the 365-day
`mentor-readiness` scenario. Omit `--clean`
to read the default live Ego and simulate against a private clone, or select a
snapshot explicitly with `--store /path/to/ego.json`. In either case the source
file remains unchanged.

A custom scenario is a JSON file with ordered virtual events:

```json
{
  "name": "consciousness-user",
  "description": "A long-running interest becomes a grounded concern.",
  "simulatedDays": 30,
  "events": [
    { "atDay": 0, "type": "fact", "id": "consciousness", "category": "interest", "content": "Machine consciousness", "confidence": 0.95, "timesConfirmed": 1 },
    { "atDay": 1, "type": "fact", "id": "consciousness", "category": "interest", "content": "Machine consciousness", "confidence": 0.95, "timesConfirmed": 2 },
    { "atDay": 3, "type": "thought", "content": "Machine consciousness needs a falsifiable behavioral model." }
  ]
}
```

Run it with `--scenario-file ./consciousness-user.json`. Fact and preference
events upsert by ID, so later events can confirm or revise earlier evidence.
Custom scenarios also accept `remove-fact`, `remove-preference`, and thought
events with `"accepted": false`. Use `--step-hours` to stress repeated polling.
The laboratory evaluates persistent behavioral structure; it cannot establish
subjective consciousness.

Soul keeps up to 16 desires as a long-term library while only the four strongest
experience-born desires remain active. Unsupported desires become dormant and
are archived after 45 days instead of being deleted. Separately, the
longitudinal user model tracks evidence-backed personality, habit, work-style,
decision-style, value, goal, constraint, wellbeing, and communication patterns.
Only confirmed user goals plus at least two other independently confirmed
patterns may produce mentor guidance. Delivered guidance is linked to expression
feedback so adopted, useful, corrected, badly timed, and rejected advice changes
future cooldown and eligibility. These patterns remain hypotheses the user can
correct; they are not diagnoses or authority over the user's choices.

## Karma Laboratory

With `karmaMode=shadow`, Soul records actual opportunity choices, bounded
counterfactual motivation scores, and grounded executor outcomes without
changing production routing. Inspect the accumulated experiment state with:

```bash
npm run karma-lab
```

Run the accelerated virtual-time scenario instead of waiting for production
observations:

```bash
npm run karma-lab -- --simulate
npm run karma-lab -- --simulate adaptive
```

The Karma layer learns only from distinct success/failure evidence. No-progress,
unknown, and duplicate observations remain neutral, and contrary evidence can
reverse a tendency. See [the motivational plasticity design](docs/motivational-plasticity.md).

## Internationalization

Repository documentation, test names, source comments, logs, identifiers, and
default user-facing copy are written in English. Native-language text is kept
only where it is part of an explicit multilingual parser, language-specific
resource, or regression fixture. Soul should follow the user's detected language
at runtime instead of assuming English or Chinese. The test suite enforces the
English-only rule for `README.md` and public Markdown files under `docs/`.

## Development

```bash
npm install    # Zero runtime deps — uses only Node.js built-ins
npm run build
npm test
```

## License

MIT
