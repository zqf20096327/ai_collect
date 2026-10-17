# B2B Agents

A white-label, **platform-neutral** multi-agent system. 56 specialized agents covering
engineering, product, marketing, design, operations, and testing — plus a company builder
that configures the whole system for your organization in one session, and a compile
pipeline that targets the platform you actually run on.

Author your agents once. Ship them to **Claude Code**, the **OpenAI Agents SDK**, or a
**Custom GPT** — the pipeline handles the differences and tells you exactly what changes per
platform.

## What's new in this version

Earlier versions were Claude Code only. This version separates the agent *content* (the
portable persona, knowledge, and examples) from the platform *wiring* (model names, tool
bindings, orchestration mechanism). A small pipeline compiles the neutral source to each
target:

```
.md agents ──(extract)──► neutral/*.agent.yaml ──(adapter)──► Claude Code  (.md)
                                                ├─────────────► OpenAI Agents SDK (Python)
                                                └─────────────► Custom GPT (instruction blobs)
```

- **One source, many platforms.** The same agent library runs on full multi-agent
  frameworks or a single no-code GPT.
- **Honest degradation.** Limited platforms (e.g. Custom GPTs, which can't orchestrate) get
  a build report listing exactly what was flattened, dropped, or needs manual setup —
  nothing fails silently.
- **`company-builder` picks the target for you.** It asks where you'll run the agents during
  intake and compiles to the matching platform(s) automatically.

See [`docs/neutral-agent-schema.md`](docs/neutral-agent-schema.md) for the full design and
[`scripts/README.md`](scripts/README.md) for the pipeline.

## Quick Start

```bash
git clone https://github.com/alyssonfranklin/b2b-agents.git
cd b2b-agents
```

Then, in Claude Code:

```
Use the company-builder agent
```

It asks ~9 questions (including which platform you run on), generates your company folder,
recommends which agents fit your workflow, rewrites `CLAUDE.md` with your context, compiles
to your target platform(s), and produces an install path.

### Manual install for Claude Code (skip the builder)

```bash
cp -r b2b-agents/*.md ~/.claude/agents/
for d in engineering product marketing design project-management studio-operations testing bonus; do
  cp -r "b2b-agents/$d" ~/.claude/agents/
done
```

Or copy only the agents relevant to your workflow — fewer agents means faster routing and
less decision overhead.

## Multi-Platform Pipeline

The agent `.md` files are the source of truth. To run on another platform, compile them.

| Target | Capability | Output |
|--------|-----------|--------|
| **`claude`** | Native subagents, full fidelity | Claude Code `.md` agents |
| **`sdk`** | Code-orchestrated multi-agent | OpenAI Agents SDK package (also fits LangGraph / CrewAI) |
| **`gpt`** | Single-agent, instructions-only | Custom GPT / Gemini Gem instruction blobs |

```bash
pip install pyyaml --break-system-packages

python3 scripts/extract_neutral.py --src .       --out neutral      # agents → neutral
python3 scripts/adapter_claude.py  --src neutral --out dist/claude  # → Claude Code
python3 scripts/adapter_sdk.py     --src neutral --out dist/sdk     # → OpenAI Agents SDK
python3 scripts/adapter_gpt.py     --src neutral --out dist/gpt     # → Custom GPT
```

What survives the trip:

| Neutral concept | `claude` | `sdk` | `gpt` |
|-----------------|----------|-------|-------|
| Reasoning tier (`fast`/`balanced`/`deep`) | haiku / sonnet / opus(+thinking) | model tier + `reasoning_effort` | manual model choice (warns on `deep`) |
| File/web/shell capabilities | native tools | runtime function tools + hosted tools | Code Interpreter / Knowledge / Web Browsing (warns where unsupported) |
| Orchestration | `Task` delegation | `handoffs` | flattened into one agent + warning |
| Structured input (`input_schema`) | passthrough | documented | "Expected input" section |

The `claude` round-trip is verified lossless (`neutral → claude → neutral` is
byte-identical). `neutral/` and `dist/` are generated and git-ignored — rebuild them, don't
edit by hand.

## Architecture

### Repository structure

```
b2b-agents/
├── company-builder.md           # Run this first — intake, customize, compile
├── b2b-orchestrator.md          # Multi-domain task coordinator
├── company/                     # Template agents (filled in by the builder)
├── space-industries/            # Reference example (DXP consulting firm)
├── engineering/                 # 16 agents
├── product/                     # 7 agents
├── marketing/                   # 9 agents
├── design/                      # 5 agents
├── project-management/          # 3 agents
├── studio-operations/           # 7 agents
├── testing/                     # 5 agents
├── bonus/                       # 2 agents
├── scripts/                     # Compile pipeline (extractor + 3 adapters)
├── docs/
│   ├── neutral-agent-schema.md  # The multi-platform schema + adapter spec
│   ├── architecture.md          # How the agent system works
│   ├── writing-agents.md        # How to author effective agents
│   ├── eval/                    # Test prompts per agent category
│   └── compliance/              # ISO/ISMS documentation (not agents)
├── neutral/                     # Generated: neutral agent YAML (git-ignored)
└── dist/                        # Generated: per-platform builds (git-ignored)
```

`space-industries/` shows what a completed company setup looks like for a DXP consulting
firm. Use it as a reference when customizing your own.

### Reasoning tiers

Each agent declares a reasoning tier rather than a hardcoded model, so the same agent maps
to the right model on every platform. On the `claude` target the tiers resolve as:

| Tier | Claude model | Used for |
|------|-------------|---------|
| **deep** | `claude-opus-4-6` (+ thinking) | Security review, legal, compliance, backend architecture, AI engineering, pricing strategy |
| **balanced** | `claude-sonnet-4-6` | Most engineering, product, design, marketing, testing agents |
| **fast** | `claude-haiku-4-5-20251001` | Social content, support responses, coordination, jokes |

On `sdk` the `deep` tier requests `reasoning_effort="high"`; on `gpt` it prompts you to pick
a reasoning model by hand.

### Extended thinking (deep tier)

These agents reason with a 10k-token thinking budget on Claude:
`enterprise-security-reviewer`, `backend-architect`, `ai-engineer`, `data-privacy-engineer`,
`legal-advisor`, `compliance-automation-specialist`, `pricing-packaging-strategist`.

### Orchestrator

`b2b-orchestrator.md` coordinates tasks that span more than one department. Its prompt
describes delegation generically ("delegate to a specialist"), so it compiles correctly to
each platform — `Task` on Claude, `handoffs` on the SDK, and an inlined single agent on
Custom GPT.

```
"We're launching enterprise SSO next week — handle everything"
→ decomposes → delegates to security-reviewer + devops-automator + content-creator +
  project-shipper in parallel → synthesizes into a launch brief
```

## Company Builder

`company-builder.md` runs at fork time (or any time you reconfigure):

1. **Intake** — 9 questions: name, type, domain, tech stack, business model, deal size, top
   use cases, and the platform you'll run on.
2. **Recommendation** — maps your answers to the relevant subset of the agents.
3. **Generation** — creates `[your-company]/` with the 4 business agents customized to your
   context, and rewrites `CLAUDE.md`.
4. **Compile** — builds for your chosen platform(s) and surfaces any degradation report.
5. **Install** — for Claude, an `install.sh`; for SDK/GPT, the compiled package or blobs.

## Agent Catalog

### Orchestrator
- **b2b-orchestrator** — Decomposes complex multi-domain tasks, coordinates specialists, synthesizes results

### Company (generated by builder, see `space-industries/` for a reference example)
- **proposal-writer** — Proposals, SOWs, retainer agreements in your company's format and voice
- **discovery-facilitator** — Discovery workshops, stakeholder interviews, findings reports
- **rfp-powerhouse** *(deep)* — Full RFP assembly, compliance matrices, win strategy
- **client-presentation-builder** — Executive decks, status updates, proposal presentations

### Engineering (16 agents)
- **accessibility-expert** — WCAG 2.1, Section 508, LGPD accessibility compliance
- **ai-engineer** *(deep)* — LLM integration, ML pipelines, RAG systems
- **ai-ethics-governance-specialist** — AI bias detection, algorithmic transparency
- **api-integration-specialist** — REST/GraphQL design, SDK development, developer experience
- **backend-architect** *(deep)* — Scalable B2B APIs, multi-tenant systems, SSO
- **data-privacy-engineer** *(deep)* — GDPR, CCPA, LGPD, privacy-by-design
- **database-performance-optimizer** — Multi-tenant DB optimization, query tuning
- **devops-automator** — CI/CD pipelines, cloud infrastructure, IaC
- **enterprise-integration-architect** — Salesforce, SAP, Microsoft 365 integrations
- **enterprise-security-reviewer** *(deep)* — SOC2, GDPR, ISO 27001 compliance
- **frontend-developer** — React/Vue/Angular enterprise UIs
- **mobile-app-builder** — B2B React Native applications
- **monitoring-observability-specialist** — APM, SLA monitoring, distributed tracing
- **rapid-prototyper** — B2B MVPs and enterprise feature POCs
- **technical-sales-engineer** — Demos, RFP technical responses, solution architecture
- **test-writer-fixer** — Enterprise test suites, failure diagnosis, test repair

### Product (7 agents)
- **b2b-onboarding-optimizer** — Activation flows, time-to-value, enterprise setup
- **enterprise-onboarding-strategist** — Large-scale enterprise rollouts, change management
- **feedback-synthesizer** — Customer feedback analysis, pattern extraction
- **pricing-packaging-strategist** *(deep)* — Value-based pricing, enterprise contracts
- **product-sales-specialist** — Product design for sales, RFP creative responses
- **sprint-prioritizer** — Backlog prioritization, feature trade-offs, sprint planning
- **trend-researcher** — B2B market opportunities, competitive intelligence

### Marketing (9 agents)
- **app-store-optimizer** *(fast)* — B2B SaaS app store presence
- **content-creator** — Blog posts, thought leadership, multi-format content
- **enterprise-content-strategist** — B2B content strategy, SEO, buyer journey
- **growth-hacker** — Viral loops, PLG, enterprise acquisition
- **linkedin-content-curator** *(fast)* — LinkedIn posts, articles, thought leadership
- **partnership-channel-manager** — B2B partnerships, channel programs
- **reddit-community-builder** *(fast)* — Authentic Reddit community engagement
- **tiktok-strategist** *(fast)* — B2B TikTok content strategy
- **twitter-engager** *(fast)* — Twitter/X B2B engagement and content

### Design (5 agents)
- **brand-guardian** — B2B brand identity consistency
- **ui-designer** — Enterprise UI components, design systems
- **ux-researcher** — Enterprise user research, usability testing
- **visual-storyteller** — Data visualization, pitch decks
- **whimsy-injector** *(fast)* — Professional delight and micro-interactions

### Project Management (3 agents)
- **experiment-tracker** — A/B testing, feature flag management
- **project-shipper** — B2B feature launches, go-to-market coordination
- **studio-producer** — Cross-team coordination, resource management

### Studio Operations (7 agents)
- **analytics-reporter** — B2B usage data, business metrics dashboards
- **compliance-automation-specialist** *(deep)* — Automated SOC2, ISO 27001
- **customer-success-manager** — Enterprise account health, churn prevention, expansion
- **finance-tracker** — MRR, unit economics, B2B financial modeling
- **infrastructure-maintainer** — Cloud cost, capacity planning, infrastructure scaling
- **legal-advisor** *(deep)* — Enterprise contracts, RFP legal, procurement compliance
- **support-responder** *(fast)* — B2B customer support, issue resolution

### Testing (5 agents)
- **api-tester** — B2B API load testing, enterprise reliability
- **performance-benchmarker** — Application performance, enterprise load testing
- **test-results-analyzer** — Test failure pattern analysis
- **tool-evaluator** — B2B development tool assessment and selection
- **workflow-optimizer** — Human-agent collaboration, process automation

### Bonus (2 agents)
- **studio-coach** *(fast)* — Team motivation, multi-agent coordination support
- **joker** *(fast)* — Tech humor for stressed teams

## Authoring Agents

Agents are authored as Claude `.md` files (the source of truth); the pipeline lifts them
into neutral form for compiling to other platforms. Keep agent bodies **platform-neutral** —
no tool names, no model names, no runtime references. Refer to delegation generically
("delegate to a security specialist"), and the adapters bind it per platform.

```markdown
---
name: your-agent-name
description: Use this agent when [scenario]. Examples:

<example>
Context: [situation]
user: "[request]"
assistant: "[what you'll do — no self-reference]"
<commentary>
[why this example matters]
</commentary>
</example>
color: blue
model: claude-sonnet-4-6
tools: Read, Write, Bash, Grep
---

You are a [role] specializing in [domain]...
```

For deep-reasoning agents add extended thinking; for agents invoked with structured inputs
add an `input_schema`:

```yaml
model: claude-opus-4-6
thinking:
  type: enabled
  budget_tokens: 10000
input_schema:
  type: object
  properties:
    required_field:
      type: string
      description: "What this field means and example values"
  required:
    - required_field
```

After editing any agent, re-run the pipeline so the per-platform builds stay in sync.

## Documentation

| Doc | What it covers |
|-----|---------------|
| [`docs/neutral-agent-schema.md`](docs/neutral-agent-schema.md) | The multi-platform schema, the three target buckets, and adapter mappings |
| [`scripts/README.md`](scripts/README.md) | The compile pipeline: extractor + adapters, usage, per-target output |
| [`docs/architecture.md`](docs/architecture.md) | How the agent system works: routing, frontmatter, orchestration, input_schema, white-label layers |
| [`docs/writing-agents.md`](docs/writing-agents.md) | Writing effective agents: description as routing logic, examples, model/tool selection, prompt design |
| [`docs/agent-intelligence-architecture.md`](docs/agent-intelligence-architecture.md) | Blueprint for evolving the system: Memory, Hierarchical Specialization, Quality Gates, Context Amplifiers |
| [`docs/eval/README.md`](docs/eval/README.md) | How to run agent evaluations |

## Notes

- `neutral/` and `dist/` are generated by the pipeline and git-ignored — rebuild, don't commit.
- `docs/compliance/` contains ISO/ISMS documentation — not agents.
- `marketing/instagram-curator.md` is deprecated; use `marketing/linkedin-content-curator.md`.
- `base22/` is deprecated; see `space-industries/` for the reference example.
- `space-industries/` is a generated example — a DXP consulting firm configured via company-builder.
