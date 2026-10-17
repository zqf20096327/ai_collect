<div align="center">

# worldlink-agent

English | [中文](README.zh.md)

## Cursor for the physical world

Connecting AI to the physical world.

**worldlink-agent** is a **Physical Agent Runtime**.
It takes AI from understanding a goal to acting in the world, and holding the result to account.

![License](https://img.shields.io/badge/license-Apache--2.0-2f6feb)
![Python](https://img.shields.io/badge/Python-3.12%2B-3776ab)
![Node.js](https://img.shields.io/badge/Node.js-22%2B-339933)
![FastAPI](https://img.shields.io/badge/FastAPI-runtime-009688)
![React](https://img.shields.io/badge/React-console-61dafb)

[Quick start](#quick-start) · [Architecture](#architecture) · [Scenarios](#scenarios) · [Docs](#docs) · [Contributing](#contributing)

<table>
  <tr>
    <td width="33%" align="center">
      <img src="docs/media/01-high-voltage-grid-inspection.png" alt="High-voltage grid inspection" />
      <br /><sub>01 · High-voltage grid inspection</sub>
    </td>
    <td width="33%" align="center">
      <img src="docs/media/02-utility-tunnel-inspection.jpg" alt="Utility tunnel inspection" />
      <br /><sub>02 · Utility tunnel inspection</sub>
    </td>
    <td width="33%" align="center">
      <img src="docs/media/03-rail-inspection.png" alt="Rail inspection" />
      <br /><sub>03 · Rail inspection</sub>
    </td>
  </tr>
  <tr>
    <td width="33%" align="center">
      <img src="docs/media/04-flexible-manufacturing.png" alt="Smart production line" />
      <br /><sub>04 · Smart production line</sub>
    </td>
    <td width="33%" align="center">
      <img src="docs/media/05-facility-inspection.jpg" alt="Facility inspection" />
      <br /><sub>05 · Facility inspection</sub>
    </td>
    <td width="33%" align="center">
      <img src="docs/media/06-customer-visit.png" alt="Smart office" />
      <br /><sub>06 · Smart office</sub>
    </td>
  </tr>
  <tr>
    <td width="33%" align="center">
      <img src="docs/media/07-disaster-search-rescue.png" alt="Disaster search and rescue" />
      <br /><sub>07 · Disaster search and rescue</sub>
    </td>
    <td width="33%" align="center">
      <img src="docs/media/08-deep-sea-exploration.jpg" alt="Deep-sea exploration" />
      <br /><sub>08 · Deep-sea exploration</sub>
    </td>
    <td width="33%" align="center">
      <img src="docs/media/09-mars-settlement.png" alt="Mars colonization" />
      <br /><sub>09 · Mars colonization</sub>
    </td>
  </tr>
  <tr>
    <td width="33%" align="center">
      <img src="docs/media/10-defense-resilience.jpg" alt="Defense self-protection" />
      <br /><sub>10 · Defense self-protection</sub>
    </td>
    <td width="33%" align="center">
      <img src="docs/media/11-police-apprehension.png" alt="Smart police capture" />
      <br /><sub>11 · Smart police capture</sub>
    </td>
    <td width="33%" align="center" valign="middle">
      <sub><strong>Same Runtime</strong><br />Evidence closes the loop</sub>
    </td>
  </tr>
</table>

</div>

---

## From understanding a goal to finishing a real task

Cursor shows you the diff before you accept a change. WorldLink shows you **Evidence** before a physical task can close.

Today's AI can already understand information, produce a plan, and call tools. Real tasks still have a harder step: what happened after the action? Did the goal actually complete? Should work continue after the environment changed?

worldlink-agent provides that Runtime layer:

- Compile a natural-language goal into a constrained task graph;
- Select executors from software, device, robot, and human Providers, and delegate subgoals through a Sub-Agent contract when needed;
- Query a physical knowledge graph (capabilities, Providers, dependencies, and compensations) for discovery, without treating it as current World State;
- Continuously ingest Observation and maintain current World State;
- Verify physical effects and business outcomes with Evidence;
- Re-assess the goal gap on every world feedback through the Physical Agent Loop: gather more sensing, retry, switch Provider, or replan when Evidence is insufficient or the site has changed;
- Rebuild working context with L1 / L2 / L3 memory and keep recoverable, replayable, auditable Mission state; cross-Mission experience is advisory only.

<p align="center">
  <img src="docs/media/loop-en.svg" alt="Loop from goal to Evidence" width="980" />
</p>

> A model may propose a plan. It cannot grant itself authority, declare facts about the world, or bypass Runtime policy gates.

## Current capabilities

| Capability | Current implementation |
| --- | --- |
| Mission Runtime | Goal compilation, task graphs, lifecycle, recovery, and governance |
| Physical Agent Loop | Observe → Assess → Decide → Act → Verify |
| Physical knowledge graph | Workspace, capability, and Provider topology; `/physical-knowledge/query` |
| Three-layer memory | L1 rebuilt on wakeup, L2 Mission snapshot, L3 terminal experience summaries |
| Capability and experience retrieval | Deterministic lexical matching; the adapter can later be replaced with semantic retrieval, and never overrides current Observation |
| World state | Workspace revision, Observation ingest, and retained conflicts |
| Outcome verification | Effect contract, Evidence, Outcome Gate |
| Execution system | Software, Mock, device, robot, and human Providers |
| Sub-Agent | `AgentContract`: subgoal, capability allowlist, budget, escalation; completion still passes Evidence |
| Failure recovery | Additional sensing, Provider switch, retry, compensation, and reconciliation |
| State storage | In-memory, atomic files, and PostgreSQL |
| Workflow | Local wakeup and Temporal coordination interface |
| Hardware boundary | LHI v0.1, reference manifests, and Simulator |
| Console | React, TypeScript, Three.js / GLB digital twins |
| Scenarios | 11 independent controlled-simulation Mission Templates |

Default executors are simulated. The project does not currently control real robots, vehicles, power grids, access control, or critical infrastructure. Live device integration requires a vendor Adapter, authorization, a security review, and on-site validation.

## Architecture

<p align="center">
  <img src="docs/media/arch-en.svg" alt="worldlink-agent architecture" width="960" />
</p>

Runtime owns task-level decisions and outcome verification. The physical knowledge graph describes capability and Provider relationships; it is not live World State. L3 experience can hint, and cannot rewrite authority. Flight control, PLC interlocks, collision avoidance, emergency stop, and robot joint control remain on the device's native controller.

### Three-layer memory

<p align="center">
  <img src="docs/media/mem-en.svg" alt="L1 L2 L3 memory" width="800" />
</p>

- **L1**: short-lived working context rebuilt from authoritative state whenever Mission Executive wakes.
- **L2**: the full recoverable snapshot of one Mission; can be stored in files or PostgreSQL.
- **L3**: terminal Mission experience summaries; currently in-memory or file storage with text matching retrieval.

Historical experience is advisory only. It cannot override current Observation, authority, or Evidence.

### Physical knowledge graph

The physical knowledge graph is a capability topology. It is not a general encyclopedia, and it is not current site state. Nodes are Workspaces, capabilities, and Providers. Edges include `authorized_for`, `executed_by`, `requires_capability`, and `compensated_by`.

The query entry point is `/physical-knowledge/query`. A request may attach a Mission's current World State, but the response states that the graph is not an accepted Observation projection. Planning and scheduling still follow Workspace revision and Evidence.

### Sub-Agent

A Provider executes a capability; it is not an autonomous agent. Complex goals can be split into `PlanFragment`s by domain and merged by Runtime before execution.

Live subgoals are delegated through `AgentContract`: an explicit subgoal, capability allowlist, authority envelope, resource budget, and escalation policy. A Sub-Agent may report progress or a completion claim, but it cannot close the Mission by itself. Results still pass the Runtime Evidence gate. The API exposes `delegate` and `redelegate`.

### Capability and experience retrieval

Retrieval is for discovering capabilities and reviewing experience. It does not replace current facts:

- Capability discovery uses deterministic lexical scoring over the capability manifest (`/capabilities/search`);
- Similar Missions use text matching over L3 summaries (`/physical-knowledge/similar-missions`).

This is the interface shape for retrieval-augmented planning: the retrieval adapter can later be replaced with semantic retrieval, but model planning does not currently inject retrieval results into the prompt automatically. Historical experience cannot override current Observation, authority, or Evidence.

## Scenarios

Smart office is the default public console entry. High-voltage grid inspection is the first commercial closed-loop scenario. The 11 templates below follow console catalog order (`01`–`11`).

| Scenario | Template ID | What it verifies |
| --- | --- | --- |
| High-voltage grid inspection | `high-voltage-grid-inspection` | Multimodal inspection, defect work orders, and post-repair recheck |
| Utility tunnel inspection | `utility-tunnel-inspection` | Confined-space preconditions, gas checks, and comms recovery |
| Rail inspection | `rail-inspection` | Work protection, part Evidence, and platform recovery |
| Smart production line | `flexible-manufacturing` | AGVs, robot arms, quality gates, and multi-cell coordination |
| Facility inspection | `facility-inspection` | Equipment status, access control, and sensor isolation |
| Smart office | `customer-visit` | Space, access, meetings, service robots, and human collaboration |
| Disaster search and rescue | `disaster-search-rescue` | Multi-source sensing, risk assessment, and rescue authorization |
| Deep-sea exploration | `deep-sea-exploration` | Low bandwidth, energy budget, and sampling gates |
| Mars colonization | `mars-settlement` | Long-delay supervision, resource ledger, and irreversible authorization |
| Defense self-protection | `defense-resilience` | Protection of people and critical sites, unarmed reconnaissance |
| Smart police capture | `police-apprehension` | Anonymized situational awareness, risk flags, and human command |

3D animation in a scenario only projects Runtime state. It never generates task results or Evidence.

## Quick start

Requirements:

- Python 3.12+
- Node.js 22+
- [uv](https://docs.astral.sh/uv/)

~~~bash
# Install backend and frontend dependencies
uv sync --dev --locked
npm --prefix frontend ci

# Local config is optional; defaults are in-memory state, deterministic planning, and simulated execution
cp .env.example .env

# Terminal 1: start the API
npm run api

# Terminal 2: start the console
npm run web
~~~

Open <http://localhost:5173>. Local simulation does not need a database or a model API key.

### Model planning

The project supports an OpenAI-compatible model API:

~~~bash
SPATIAL_MODEL_MODE=optional
SPATIAL_MODEL_BASE_URL=https://your-model-endpoint.example/v1
SPATIAL_MODEL_NAME=your-model
SPATIAL_MODEL_API_KEY=your-secret
~~~

Model secrets belong only in the backend runtime environment. Do not set `VITE_SPATIAL_MODEL_API_KEY`, and do not bake long-lived credentials into the frontend build.

## Automated verification

~~~bash
uv sync --dev --locked
npm --prefix frontend ci

uv run ruff check backend
uv run pytest -q
npm --prefix frontend test
npm --prefix frontend run typecheck
npm --prefix frontend run build
~~~

Latest verification baseline:

- Backend: 451 tests;
- Frontend: 52 test files, 292 tests;
- Ruff, TypeScript, and the Vite production build passed;
- npm dependency audit: 0 known vulnerabilities.

Full record: [Verification](docs/VERIFICATION.md).

## Repository layout

~~~text
backend/spatial_os/domain       Domain models and state contracts
backend/spatial_os/runtime      Mission Runtime, Loop, physical knowledge graph, and verification
backend/spatial_os/storage      Mission / Workspace / L3 experience storage
backend/spatial_os/templates    Scenario templates and capability catalogs
backend/spatial_os/executors    Simulated executors and human executors
backend/spatial_os/hardware     LHI hardware protocol and Adapter boundary
backend/spatial_os/api          FastAPI API and WebSocket
backend/migrations              PostgreSQL schema migrations
frontend/src                    React console and digital twins
schemas                         LHI JSON Schema
~~~

## Docs

Longer design documents below are currently in Chinese.

| Document | Contents |
| --- | --- |
| [Architecture](docs/ARCHITECTURE.md) | Runtime boundary, Mission lifecycle, Providers, and persistence |
| [Physical Agent Loop](docs/PHYSICAL_AGENT_LOOP_DESIGN.md) | Observe, Assess, Decide, Act, Verify |
| [Scenario catalog](docs/SCENARIO_CATALOG.md) | 11 templates and public capability boundaries |
| [Office Capability Catalog](docs/OFFICE_CAPABILITY_CATALOG.md) | 69 Mock-first office capabilities |
| [Mars colonization](docs/MARS_SETTLEMENT.md) | Long delay, resource ledger, and authorization model |
| [LHI spec](docs/LHI_SPEC.md) | Hardware discovery, command, event, and Evidence contracts |
| [LHI security model](docs/LHI_SECURITY_MODEL.md) | Trust boundary, action modes, and safety controls |
| [LHI implementation](docs/LHI_IMPLEMENTATION.md) | Reference implementation and live-device admission |
| [Cross-scenario hardware matrix](docs/LHI_SCENARIO_MATRIX.md) | hardware, software, human, and runtime boundaries |
| [Deployment](docs/DEPLOYMENT.md) | Production topology and Tencent Cloud rollout steps |

## Security boundary

worldlink-agent defaults to `simulate` mode. Model output, device discovery, UI state, and `command.completed` cannot by themselves authorize or prove a real-world action.

Production deployments should enable authentication, restrict CORS, use dedicated database credentials, and keep PostgreSQL, Temporal, and internal API ports on a private network. Any `approval` or `live` hardware deployment needs a separate device-level security review.

See [SECURITY.md](SECURITY.md) to report a security issue.

## Contributing

New scenario templates, Provider Adapters, LHI implementations, digital twins, and documentation are welcome.

Read [CONTRIBUTING.md](CONTRIBUTING.md) before you start.

## License

This project is licensed under [Apache License 2.0](LICENSE). Commercial use, modification, and distribution are allowed, subject to the notice-preservation requirements in the license. Third-party dependencies follow their own licenses.
