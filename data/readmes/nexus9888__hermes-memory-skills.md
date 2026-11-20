# Hermes Agent Memory Skills (Memory-Agnostic)

Memory hygiene skills for [Hermes Agent](https://github.com/NousResearch/hermes-agent) that work with **any memory backend** — built-in MEMORY.md and Holographic.

These are the memory-agnostic versions of the original [hermes-memory-skills](https://github.com/nexus9888/hermes-memory-skills). They auto-detect which memory provider is active and route operations to the correct toolset.

## Why Memory-Agnostic?

The original skills assume the built-in `memory()` tool — they read/write `MEMORY.md` directly. That works great for the default backend, but Hermes Agent supports 8 external memory providers. Holographic, the most interesting one, stores facts in SQLite with HRR vector algebra and trust scoring. It has completely different tools (`fact_store`, `fact_feedback`), no character limit, and no `§` delimiter format.

Rather than making users choose between backends OR skills, these skills detect the active backend at runtime and adapt:

| Backend | Detection | Phase 2 tool | Capacity model | Bloat handling |
|---------|-----------|-------------|----------------|----------------|
| **Built-in** (default) | `memory.provider` empty/null | `memory()` | 2,200 char limit | Phase 2.5 Condensation (built into dreaming) |
| **Holographic** | `memory.provider: holographic` | `fact_store()` + `fact_feedback()` | Trust scores (0.0–1.0) | `fact_feedback(action='unhelpful')` decay |
| **Other providers** | Detected but unsupported | No promotion until supported | — | — |

## Skills

### 🌙 Agent Dreaming (Memory-Agnostic)

Three-phase background memory consolidation — same Light/Deep/REM structure as the original, but with backend detection as Phase 0, dual routing in Phase 2, and a built-in **Phase 2.5 Condensation** that replaces the deprecated `memory-lean-check` skill.

```
Phase 0:   Detect backend (built-in or holographic)
Phase 1:   Light — review sessions, stage candidates
Phase 2:   Deep — score candidates, promote via correct backend tools
Phase 2.5: Condensation — trim bloat / decay stale facts (built into dreaming)
Phase 3:   REM — extract patterns, propose structural changes
```

**What's different from the original:**
- Phase 0 backend detection from `config.yaml`
- Phase 2 routes to `memory()` or `fact_store()`/`fact_feedback()` automatically
- Capacity check adapts: char limit for built-in, trust score distribution for holographic
- New entries in holographic always include `entities` for compositional recall
- **Phase 2.5 Condensation** built in — no separate `memory-lean-check` skill needed
- Unsupported providers are reported as blocked; no fallback writes

## Installation

```bash
# Clone the repo
git clone https://github.com/nexus9888/hermes-memory-skills.git
cd hermes-memory-skills

# Copy the agnostic dreaming skill into your Hermes skills directory
cp -r agent-dreaming-agnostic ~/.hermes/skills/management/

# Verify it's installed
hermes skills list | grep agnostic
```

Or install directly from the repo:

```bash
hermes skills tap add https://github.com/nexus9888/hermes-memory-skills
hermes skills install agent-dreaming-agnostic
```

## Cron Setup

Recommended schedule (works regardless of backend):

```bash
# Dream — handles both promotion AND condensation
hermes cron create \
  --schedule "0 */6 * * *" \
  --name "agent-dreaming" \
  --skill agent-dreaming-agnostic \
  "Run memory consolidation with the active backend"
```

> **No separate lean-check cron needed.** Phase 2.5 Condensation runs as part of dreaming whenever capacity thresholds are breached (built-in >60%) or every cycle (holographic).

### Cron and memory-provider contract

Cron runs use normal tool resolution, and memory tools are available to scheduled
jobs. Hermes Agent PR [#91447](https://github.com/NousResearch/hermes-agent/pull/91447)
(merge `ef04d846e9505388d8eab61b7c6608acb652bf59`) changed the cron contract: the
scheduler no longer skips memory (`skip_memory=False`), memory is not denylisted,
and user `agent.disabled_toolsets` restrictions are still respected. `allow_memory`
is not a supported flag and is not needed.

`hermes cron run <job-id>` is a cron execution, not an interactive bypass or a
way to recover tools excluded by the configured tool restrictions. Follow the
configured backend and available tools; if the required tool is unavailable,
stage candidates and report `BLOCKED`. Never patch MEMORY.md or access provider
files/SQLite as a workaround.

## Requirements

- Hermes Agent (any version with `memory` tool)
- `session_search` tool enabled
- `llm-wiki` skill installed (for wiki pointer creation in Phase 2)
- For Holographic backend: `memory.provider: holographic` in config.yaml + plugin installed

## How It Detects the Backend

The skill reads `memory.provider` from `$HERMES_HOME/config.yaml`:

```yaml
# Built-in (default — no provider set):
memory:
  memory_enabled: true

# Holographic:
memory:
  provider: holographic
```

The detection logic:

```
memory.provider == "" or null → built-in
memory.provider == "holographic" → holographic
unsupported provider → BLOCKED; stage candidates and report
```

Never route an unsupported provider to another backend or storage layer.

## Architecture

```
┌─────────────────────────────────────────────────────┐
│           agent-dreaming-agnostic                    │
│                                                      │
│  Phase 0: Backend Detection                          │
│    └─ read memory.provider from config.yaml          │
│                                                      │
│  Phase 1: Light (same regardless of backend)         │
│    ├─ session_search() → recent sessions             │
│    ├─ deep-dive signal sessions                      │
│    └─ stage candidates → dream artifact              │
│                                                      │
│  Phase 2: Deep (backend-routed)                      │
│    ├─ score candidates (4 dimensions)                │
│    ├─ built-in → memory() tool                       │
│    ├─ holographic → fact_store/fact_feedback         │
│    └─ post-promotion capacity check                  │
│                                                      │
│  Phase 2.5: Condensation (built in)                  │
│    ├─ built-in: merge/shorten/remove bloat           │
│    └─ holographic: trust decay + contradiction check │
│                                                      │
│  Phase 3: REM (pattern extraction)                   │
│    ├─ cross-dream pattern detection                  │
│    ├─ propose structural changes                     │
│    └─ user approval gate                             │
└─────────────────────────────────────────────────────┘
```

## License

MIT — same as the original hermes-memory-skills.

## Contributing

This is a shared workspace. If you add support for Honcho, Mem0, or another backend:

1. Update Phase 0 detection with the new provider
2. Add Phase 2 routing for the new backend's tools
3. Update the compatibility matrix in SKILL.md
4. Test with that backend active

PRs welcome.
