# AI FDE Engineering Library
> A community-built prompt, skill, and agent reference for Palantir's AI Forward Deployed Engineer (AI FDE) — generally available on Foundry + AIP since March 12, 2026.

---

## Why This Exists

Palantir's AI FDE is an autonomous agent embedded in Foundry that executes data engineering, ontology editing, function creation, governance audits, and React app development through natural-language commands. It entered General Availability on **March 12, 2026** for all Foundry enrollments with AIP enabled.

The tool is powerful and largely undocumented by the community. This library exists to change that.

**Goals:**
- Reduce variability in AI FDE outputs by standardizing how prompts are written
- Give teams a repeatable, governed approach to deploying AI FDE at scale
- Establish benchmarks and known failure modes from real usage
- Grow into a community reference that any Foundry user can contribute to

---

## Library Structure

```
/ai-fde-library
├── README.md              ← You are here
├── skill.md               ← Atomic capability registry (all AI FDE skills)
├── agents.md              ← Full session blueprints for known use cases
└── /prompts
    ├── data-integration/  ← Pipelines, ingestion, transforms
    ├── ontology-editing/  ← Object types, link types, actions
    ├── functions-editing/ ← TypeScript, Python, Logic functions
    ├── exploration/       ← Read-only discovery and lineage mapping
    ├── governance/        ← Permissions, markings, audit trails
    ├── osdk-react/        ← React widgets, OSDK hooks, forms
    ├── platform-qa/       ← Foundry concept Q&A for onboarding
    └── erp-migrations/    ← SAP ECC → S/4HANA and similar patterns
```

---

## The Operator Framing Convention

AI FDE is an **operator, not a chat assistant.** It performs real Foundry operations at machine speed. Prompts written as questions produce weaker, less deterministic results than prompts written as deployment commands.

### Standard Prompt Structure

```
[ACTION VERB] + [RESOURCE TYPE] + [SPECIFICATION] + [OUTPUT TARGET] + [BRANCH NAME]
```

| Quality | Example |
|---------|---------|
| ❌ Weak | "Can you help me create a pipeline for customer data?" |
| ✅ Strong | "Create a Python transform that ingests CSV from SFTP path `/data/customers/`, deduplicates on composite key `(customer_id, created_date)`, drops nulls in the `email` column, and outputs to the `Customer` object type. Use branch: `feature/customer-ingest-v1`." |

**Every prompt in this library follows Operator Framing.**

### Why It Matters
The agent uses your prompt to determine which tools to activate, which context to load, and how to sequence actions. Vague inputs produce vague tool selections and wide context windows — increasing both token cost and infrastructure strain. Precise operator commands narrow the action surface and improve determinism.

---

## Prompt Template

Every prompt file in this library follows this standard:

```markdown
## Prompt: [Short Name]
**Mode:** [Official Palantir Mode]
**Skill(s):** [From skill.md]
**Complexity:** [Low / Medium / High]
**Estimated Session Duration:** [e.g., 10 min / 1 hr / 4+ hrs]
**Infrastructure Risk:** [Low / Medium / High]
**Branch Required:** [Yes / No]

### Minimum Viable Context
> List only what the agent needs. Nothing more.
- [Dataset / folder / documentation file]

### Tools Required
- [Explicit list from Foundry Tools menu]

### Prompt
> [Exact natural-language operator command]

### Expected Agent Behavior
[Step-by-step description of what the agent should do]

### Verification Checklist
- [ ] [Human review step before branch merge]

### Known Failure Modes
| Failure | Likely Cause | Recovery |
|---------|-------------|----------|
| [Description] | [Root cause] | [Fix] |

### Benchmarks
| Metric | Value | Source |
|--------|-------|--------|
| [e.g., Objects created] | [e.g., 18] | [e.g., Ramamurthy, Feb 2026] |

### Verified By
[Contributor name / date / Foundry version]
```

---

## User Personas

This library is built for five distinct personas. Each section of `agents.md` and `/prompts/` is tagged accordingly.

| Persona | Role | Primary Library Sections |
|---------|------|--------------------------|
| **Human FDE** | Power user; uses AI FDE to 10x throughput | `agents.md`, erp-migrations/, ontology-editing/ |
| **Data Engineer** | Builds and maintains pipelines | data-integration/, functions-editing/ |
| **Ontology Owner** | Designs and governs schema | ontology-editing/, governance/, exploration/ |
| **App Developer** | Builds OSDK React widgets and tools | osdk-react/ |
| **Platform Admin** | Manages sessions, quotas, access policies | governance/, `agents.md` infrastructure sections |

---

## Infrastructure Awareness

AI FDE operates at machine speed. Where a human developer pauses to think, the agent executes continuously — potentially running dozens of operations in minutes. Running multiple sessions in parallel can strain GPU compute, storage I/O, and network capacity.

**Rules of thumb:**
- Sessions estimated at 4+ hours should be decomposed into discrete branch-proposal checkpoints
- High-complexity agents (e.g., ERP migrations, full backend builds) should be scheduled off-peak
- Limit enabled tools to only what the task requires — wider tool sets = more agent actions per step
- Use `Minimum Viable Context` discipline: share only the folders/datasets the agent needs

---

## Benchmarks (Community Reference)

| Benchmark | Result | Source |
|-----------|--------|--------|
| Full enterprise app backend (18 objects, 20+ actions) | 14 hours | Ramamurthy, Medium, Feb 2026 |
| Data migration (ERP) | 5 months → 5 days | Palantir DevCon 5 demo, March 2026 |
| Function debug loop (90% fail → 90% pass) | Single iteration | Palantir DevCon 5 demo, March 2026 |
| Orchestration network (API ingest + ontology cross-ref + mitigations) | 2 days (team with no prior agentic experience) | Palantir DevCon 5 demo, March 2026 |

---

## Supported Models (as of March 2026)

AI FDE supports multiple model families. Model choice affects reasoning quality, speed, and cost.

| Model Family | Best For |
|---|---|
| Anthropic (Claude) | Long-context reasoning, complex ontology work |
| OpenAI (GPT) | Code generation, function debugging |
| Google Gemini | High-volume, cost-sensitive sessions |
| xAI (Grok) | Emerging; monitor for Foundry-specific tuning |

---

## MCP Integration (Forward-Looking)

Palantir has shipped an MCP (Model Context Protocol) server alongside AI FDE. MCP is an open standard that allows **external agents** (Claude Desktop, LangGraph pipelines, custom agentic systems) to call tools exposed by a Foundry MCP server. This means AI FDE capabilities may be invokable from **outside Foundry entirely**.

A dedicated `/mcp-integration/` folder will be added as documentation becomes available. Monitor:
- Palantir Developer Community: `mcp` + `ai-fde` tags
- Palantir Developers YouTube channel
- @HansCNelson and early-adopter accounts on X

---

## Contributing

1. Fork this repository
2. Add or improve a prompt using the standard template above
3. Run the prompt in a real AI FDE session (sandbox branch recommended)
4. Fill in `Expected Agent Behavior`, `Verification Checklist`, and `Known Failure Modes` from observation — not assumption
5. Submit a PR with your Foundry enrollment type and model used
6. Cross-post high-performing prompts to the Palantir Developer Community using tag: `ai-fde`

**Do not submit prompts that have not been tested in a live session.**

---

## License
MIT — use freely, contribute back.
