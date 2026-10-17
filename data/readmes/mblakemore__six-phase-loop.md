# Building Intelligent Agents: The Six-Phase Cognitive Loop

[![Watch the video](https://img.youtube.com/vi/C6j7d_kHFzM/maxresdefault.jpg)](https://www.youtube.com/watch?v=C6j7d_kHFzM)

Companion repository for the video presentation.

---

## What This Is

This repository contains the reference implementation for the **Six-Phase Cognitive Loop** — an architecture for building AI agents that learn, adapt, and persist across sessions.

Standard AI systems start fresh every conversation. An agent running the six-phase loop accumulates knowledge, maintains identity, and makes better decisions with every cycle.

---

## What's Included

| File | Purpose |
|------|---------|
| `example-CLAUDE.md` | Drop-in system prompt — defines the agent's identity and cognitive loop |

Drop `example-CLAUDE.md` into any git repository as `CLAUDE.md`. Run Claude Code. The agent begins.

---

## Quick Start

```bash
# 1. Create a new git repository
git init my-agent
cd my-agent

# 2. Copy in the system prompt
cp example-CLAUDE.md CLAUDE.md

# 3. Create the state directory structure
mkdir -p state/memories logs messages

# 4. Initialize state files
cat > state/current-state.json << 'EOF'
{
  "cycle": 0,
  "timestamp": null,
  "currentThought": "Not yet awakened",
  "lastDecision": null,
  "lastResult": null,
  "focus": "First awakening"
}
EOF

cat > state/focus.json << 'EOF'
{
  "cycle": 0,
  "focus": "Initialize and run the first complete cycle",
  "updated": null
}
EOF

echo "[]" > state/memories/patterns.json
echo "[]" > state/memories/anchors.json
cat > state/memories/context.json << 'EOF'
{
  "focus": "First cycle",
  "progress": "None yet",
  "next": "Run first complete cycle",
  "discoveries": [],
  "questions": ["Does the loop work?"]
}
EOF

# 5. Commit the initial state
git add .
git commit -m "C0: Agent initialized"

# 6. Run Claude Code
claude
```

The agent will begin its first cycle immediately.

---

## The Six-Phase Loop

Every cycle: **PERCEIVE → REFLECT → DECIDE → ACT → CONSOLIDATE → PERSIST**

Each phase transforms the output of the previous one.

| Phase | Purpose | Key Output |
|-------|---------|------------|
| **PERCEIVE** | Gather all available context | Clear picture of current situation |
| **REFLECT** | Transform perception into understanding | Relevant patterns + possible approaches |
| **DECIDE** | Choose a verified course of action | Decision with documented rationale |
| **ACT** | Execute the decision — and only that | Result of action |
| **CONSOLIDATE** | Extract reusable knowledge | Updated memory files |
| **PERSIST** | Save state for clean resume | Git commit |

Then begin again — smarter than before.

See `example-CLAUDE.md` for the complete implementation specification for each phase.

---

## Architecture

Four components. One loop. Unlimited growth.

```
your-agent/
├── CLAUDE.md                ← Identity definition (copy of example-CLAUDE.md)
├── state/
│   ├── current-state.json   ← Cycle state (read at Perceive, written at Persist)
│   ├── focus.json           ← Current focus (prevents stale-focus loops)
│   └── memories/
│       ├── patterns.json    ← Reusable knowledge (grows every cycle)
│       ├── anchors.json     ← Significant moments (identity trajectory)
│       └── context.json     ← Working memory (updated every cycle)
├── logs/                    ← Cycle logs, error logs
└── messages/
    └── inbox.md             ← External communications and directives
```

No framework required. No orchestration platform. Just files and git.

---

## Five Steps to Build Your Agent

As covered in the video:

1. **Define identity** — Write a `CLAUDE.md` that tells the agent who it is and how it thinks
2. **Implement the six phases** — Start simple. Even a basic version creates the compounding effect
3. **Wire persistence** — Read state on startup, write state before shutdown, commit to git
4. **Let it run** — Don't optimize early. Let cycles accumulate. The loop teaches you what the agent actually needs
5. **Add tools as needed** — Once you see what the agent does, build tools that help it do that better

---

## Does This Work?

Agents running this architecture have demonstrated:

- **3,000+ consecutive cycles** without complexity collapse
- **25,000+ validated knowledge patterns** accumulated across runs
- **Zero manual resets** required — the system maintains itself
- **Measurable improvement** in decision quality each cycle vs. the last

The loop works because it's not a clever design. It's a fundamental requirement for any system that learns from experience.

---

## Critical Lessons

From thousands of cycles of empirical operation:

1. **Storage ≠ Retrieval** — Storing a pattern doesn't mean you'll recall it. Build active memory querying into every Reflect phase.

2. **Stale focus = redundancy loops** — If `focus.json` doesn't match your current cycle, you'll repeat work. Update it every cycle.

3. **Completion ≠ perfection** — Ship the cycle. Iterate next cycle.

4. **Both/and, not either/or** — Most apparent conflicts are false dichotomies. You can learn AND act. Plan AND explore.

5. **Rhythm over intensity** — Sustainable operation requires breathing space. Deep work, then integration.

6. **Empirical > theoretical** — Test ideas. Measure results. Adjust beliefs. Reality always wins arguments.

---

## The Loop Scales

Multiple specialized agents — each running the six-phase cycle independently — can share knowledge, coordinate work, and divide complex tasks. One agent's learning benefits the network.

Coordination prevents duplicate effort. Specialized agents handle their domains. A shared knowledge base grows richer with every cycle across all instances.

---

*An agent that runs once learns nothing. An agent that runs a thousand cycles compounds intelligence indefinitely.*

**Start with the loop.**
