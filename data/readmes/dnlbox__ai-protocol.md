# ![AI Protocol, illustrated with watercolor systems and architectural linework](./assets/hero.png)

When I start a new project now, I do not open with a prompt. I open with a blank concept folder.

This is a pragmatic experiment in building greenfield projects from a concept rather than from a chain of prompts. The code comes later: first you get the intent right, in plain markdown, where the agent can read it.

## The Problem

A chain of prompts feels productive. You ask an agent to "build a web app", it generates boilerplate, and you are moving within seconds.

Then the problems begin. Halfway through you realize the database was the wrong call. You switch libraries. You rewrite core logic. You spend more time correcting the agent's assumptions than building the product, all because the requirements were never broken down before the code started. Each prompt is a local decision with no shared plan behind it, so the project drifts.

## The Shift

This protocol flips the workflow. It is built on a simple thesis: if you do the rigorous thinking upfront in a concept document, you can largely hand off the execution to an AI agent.

You start with a blank concept folder. You write the problem statement and the constraints. You use the AI purely as a sounding board. You run theoretical pen tests and look for holes in your logic before a single line of code is written.

Because the protocol handles the mechanics of how work gets executed (scope, authority, startup identity, self-healing, and continuity), the actual coding phase becomes mechanical. The repository-owned contract also makes the workflow portable across coding harnesses that load project instructions, including Cursor, Claude Code, and Antigravity.

## A concept layer, not a loop

"Loop" has become the shorthand for the agentic execution cycle: the model acts, observes the result, and goes again until the work is done (Anthropic's agentic loop; tools like Claude Code even expose a `/loop`). ai-protocol is not that, and it is not an interval runner either. It is the layer the loop runs against.

It shares the loop's instincts (durable, verifiable iteration with recovery), but it puts the thinking before the cycle rather than inside it. The concept docs fix intent up front, `AGENTS.md` fixes the contract, and `BUILD_STATE.md` holds the latest meaningful checkpoint. A compatible agent loop can then plan and execute an approved objective autonomously, validate the integrated result, and checkpoint only when durable state changes. The loop is the engine; ai-protocol is the track it runs on.

## Atomic instructions

The protocol writes one independently testable instruction per bullet. The heading supplies scope, while rationale, examples, evidence, and current state remain visibly separate from normative instructions.

This structure is designed for both readers of the contract. A person can inspect one obligation at a time. A model can compare obligations, identify competing authority, and avoid treating narrative explanation as another command. Each obligation has one canonical owner, so roles and skills reference boundaries instead of repeating them.

Atomic does not mean exhaustive. The protocol keeps only safety boundaries, authority boundaries, non-obvious project rules, and procedures that materially improve execution. The model retains freedom to plan, decompose, choose tools, and orchestrate the approved objective.

## Setup

The starter is deliberately small: `AGENTS.md`, three startup roles under `.agents/roles/`, and five reviewable lifecycle skills under `.agents/skills/`. Everything else appears only when the project reaches the stage that needs it.

To try it, [download the latest starter ZIP](https://github.com/dnlbox/ai-protocol/releases/latest/download/ai-protocol-starter.zip), extract it, rename the folder, and open it in your preferred AI coding environment. The archive is not executable. Each GitHub Release also publishes `ai-protocol-starter.zip.sha256` so you can verify the download.

If you prefer, copy the root `AGENTS.md`, `.agents/roles/`, and `.agents/skills/` manually. The optional [`kickstart.sh`](./kickstart.sh) helper downloads that same release, verifies its checksum, and extracts it into a new project folder.

```bash
curl -fsSL https://raw.githubusercontent.com/dnlbox/ai-protocol/main/kickstart.sh | bash -s -- my-project
```

## The Lifecycle

![AI Protocol, illustrated with watercolor systems and architectural linework](./assets/lifecycle.png)

### Stage 1: Concept Intake

Invoke `/concept-intake` and talk through the idea. The agent works in short, focused rounds, challenges gaps without scattering the conversation, and keeps a temporary `docs/intake/concept-intake.md`. It stops when the product core is covered and further rounds would only refine existing material.

### Stage 2: Concept Shaping

Run `/shape-concept` when the intake is accepted. The agent proposes a small document structure, waits for approval, and turns the intake into canonical `docs/concept/`. You can keep exploring, researching, and resolving product tensions here without drifting into implementation planning.

### Stage 3: Lock-in

When the concept is solid, run `/plan-implementation`. The agent creates the minimum execution contract needed for the accepted intent: stable Project Specifics in `AGENTS.md`, a focused `BUILD_STATE.md` when continuity is needed, and `EXPERIENCE.md`, `DESIGN.md`, `GOVERNANCE.md`, or `ROADMAP.md` only when each earns a distinct responsibility. The [`EXPERIENCE.md` example](./examples/EXPERIENCE.md), [`GOVERNANCE.md` example](./examples/GOVERNANCE.md), and [`ROADMAP.md` example](./examples/ROADMAP.md) show how interaction, policy, objective dependencies, and current state remain separate.

Running `/plan-implementation` again on an operationally planned project performs an in-place re-plan. It preserves accepted intent, implementation, history, and verified evidence; reconciles experience traces against the running product; and revises only the open objectives and affected dependencies.

Planning is proportional to the next claim the product needs to earn. A learning-ready prototype carries only the experience, validation, and safeguards needed to test the product early; it does not inherit production obligations before the product is proven. When evidence justifies a more mature target, run `/plan-implementation` again to preserve accepted work and add only the hardening, operational evidence, and release gates required for that promotion.

Approve a bounded implementation objective. The Leader plans when needed, executes the complete objective, validates the integrated result, and delivers a clean green branch without requiring another approval after each internal step.

### Stage 4: Building (The Mechanics)

This is where the protocol shines. The project now carries its intent, stable operating contract, validation gates, and latest meaningful checkpoint. You approve the product outcome, then let the Leader choose the plan, decomposition, tools, teammates, and verification strategy inside that boundary.

Nine key mechanics, baked into `AGENTS.md` and the startup roles, make that safe:

- **Self-healing:** when a validation gate fails, the agent gets back to green before it moves on. It never leaves a broken tree behind.
- **Objective autonomy:** approval of a bounded objective authorises planning, implementation, repair, validation, cohesive commits, and delivery without routine continuation prompts.
- **Startup identity:** the primary agent loads the Leader role at the beginning; teammates and adjudicators receive their identity before bounded work begins.
- **Persistent state:** `BUILD_STATE.md` records current verified truth, material decisions, active ownership, and the next meaningful action. It is not a task transcript or permission ledger.
- **Lazy procedures:** lifecycle skills load only when their trigger applies. Ordinary feature work does not automatically run planning, synchronisation, or state-maintenance ceremonies.
- **Governance when needed:** projects with delivery claims beyond local validation can carry a generated `GOVERNANCE.md`. Maturity envelopes set evidence expectations for a promotion target, not roadmap phases; project-derived capability packs add only the obligations that apply.
- **Experience contracts when needed:** interaction-bearing projects can carry a generated `EXPERIENCE.md` with modality-aware entry points, traces, feedback, recovery, completion evidence, and cross-surface relationships. Web, CLI, API, game, automation, and artefact workflows activate only the lenses they need.
- **Outcome graphs when needed:** complex projects can carry a generated `ROADMAP.md` of observable objectives, material dependencies, acceptance conditions, experience references, and validation boundaries. The Leader chooses runtime decomposition during execution.
- **Evidence ownership:** teammates produce bounded evidence, adjudicators provide independent judgement when useful, and the Leader owns integration and final acceptance.

During execution, `/sync-protocol` reconciles stable repository instructions after a material contract change. It does not run after ordinary feature work. `/consolidate-state` repairs `BUILD_STATE.md` when the checkpoint becomes stale, contradictory, or difficult to scan. A runtime may own live scheduling, model routing, and context continuity, but only the Leader accepts verified facts into the repository checkpoint. There is no separate prompt file: `AGENTS.md` owns the stable contract, startup roles own execution identity, and `BUILD_STATE.md` owns the latest meaningful checkpoint.

The protocol does not discover or install third-party skills. External examples can inspire a locally authored project skill, but every instruction that enters the workflow remains reviewable in the repository.

### Stage 5: Ejecting

Eventually, the project matures and the concept documents may stop representing its accepted intent. Ejection must be deliberate: update or replace the source-of-truth rules in `AGENTS.md`, archive or remove stale concept documents, and retain only the instructions and skills that still describe reality. Standard tests and CI/CD pipelines can then carry more of the execution contract without leaving agents bound to obsolete product intent.

## Nesting and workspaces

A project does not have to be one repo. An umbrella project (a workspace) can hold child projects, each its own ai-protocol scope, each often its own repo, nested as deep as you need: a monorepo of services, a set of sibling repos coordinated from above, or a personal workshop of independent tools.

The layers compose rather than collide:

- The nearest `AGENTS.md` above you is the contract for that directory tree.
- Each level owns its own `BUILD_STATE.md` when durable continuity is needed.
- Roles provide startup identity across levels without duplicating project rules.
- Skills compose and load lazily: generic capabilities live at the workspace, project-specific capabilities live at the child, and the nearest name wins on a clash.

Open a harness at the workspace to coordinate across children, or inside a child to build it. Either way the agent finds the nearest contract and the right state.

## Target Audience

This is explicitly for **greenfield** projects. Do not try to backfill this rigor into legacy monoliths. Retroactively writing concept documentation to satisfy an agentic workflow rarely pays off.

This workflow cut down the friction in my own daily operations, but it is an ongoing experiment. Try it out, pull it apart, and see where it breaks for you.

![AI Protocol, illustrated with watercolor systems and architectural linework](./assets/target-audience.png)
