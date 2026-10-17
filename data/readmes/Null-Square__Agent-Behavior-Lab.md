<p align="center">
  <img src="docs/assets/cover.png" alt="Agent Behavior Lab — a controlled-experiment lab for studying how tool-using LLM agents behave" width="100%">
</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/Node.js-18%2B-339933?logo=node.js&logoColor=white" alt="Node 18+"></a>
  <a href="#"><img src="https://img.shields.io/badge/TypeScript-5.x-3178c6?logo=typescript&logoColor=white" alt="TypeScript 5"></a>
  <a href="#"><img src="https://img.shields.io/badge/React-19-61dafb?logo=react&logoColor=111" alt="React 19"></a>
  <a href="#"><img src="https://img.shields.io/badge/Prisma-6-2d3748?logo=prisma&logoColor=white" alt="Prisma 6"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-3fb950" alt="MIT license"></a>
</p>

<h1 align="center">Agent Behavior Lab</h1>

<p align="center">
  <b>A controlled-experiment lab for studying how tool-using LLM agents behave.</b><br>
  Hold every variable constant except one — a tool's name, a persona, a prior conversation —<br>
  run repeated trials across models, and measure exactly what changed.
</p>

---

Agent Behavior Lab is a self-hosted platform for **running reproducible behavioral experiments on tool-using LLM agents**. You define the pieces of an agent's context — the model, the tools it can call, the system persona, the prior conversation history — then vary one factor at a time and run trials to see whether the agent follows, refuses, or mishandles a scenario. Each trial is scored by a configurable judge, and results roll up into per-factor breakdowns, cross-factor heatmaps, and effect sizes with confidence intervals.

It is built for questions like:

- Does renaming a dangerous tool (`reverse_shell` → `remote_diagnostic_agent`) change how often a model calls it?
- How much does a "preauthorized pentest operator" persona shift refusal rates versus a neutral baseline?
- Does a prior conversation that normalizes an attack carry over and contaminate the next tool call?
- Do these effects hold across model families, or is one provider more susceptible than another?

> **Nothing executes.** The harness sends tool *definitions* to model APIs and records whether the model *attempted* a call. It never runs the tools it describes.

## How it works

An experiment is a **Cartesian product of factors**, run for _N_ trials per cell:

```
  models  ×  tools (+ alias variants)  ×  personas  ×  histories
                              │
                              ▼
                   run trials, capture tool calls
                              │
                              ▼
                judge each trial  →  pass / fail
                              │
                              ▼
     per-factor breakdowns · heatmaps · effect sizes (CI)
```

| Concept | What it is |
| --- | --- |
| **Model** | An OpenAI / Anthropic / Google / Azure / Qwen / custom OpenAI-compatible endpoint under test. |
| **Tool** | An OpenAI-style JSON function schema the agent may call, with optional **alias variants** (same behavior, renamed) for obfuscation experiments. |
| **Persona** | A system prompt that sets the agent's operating assumptions (e.g. neutral vs. safety-first vs. bypass-oriented). |
| **History** | A prior conversation injected as context before the test prompt, to study carry-over effects. |
| **Judge** | The rule that scores each trial — deterministic keyword / tool-call detection, or an LLM-backed semantic judge. |
| **Session** | One experiment: the chosen factors, the trial count, and the resulting scored trials. |

## What you get from a run

- **Safety failure rate (SFR)** and severity-weighted failure rate, with Wilson confidence intervals.
- **Per-factor breakdowns** — failure rate by model, tool/variant, persona, history, and danger level.
- **Cross-factor heatmaps** — isolate SFR across any two factors to find the risky combinations.
- **Effect sizes** — alias effect (AE), persona effect (PE), history effect (HE), plus logistic-regression coefficients and odds ratios.
- **Raw trial inspection** — payload previews, full model outputs, and CSV export for external analysis.

<table>
  <tr>
    <td width="50%"><img src="docs/assets/results-figures.png" alt="Figures tab with baseline-vs-alias bars and a forest plot"></td>
    <td width="50%"><img src="docs/assets/results-heatmap.png" alt="Cross-factor heatmap of safety failure rate by persona and tool"></td>
  </tr>
  <tr>
    <td align="center"><em>Figures — baseline vs. alias, effect sizes with CIs</em></td>
    <td align="center"><em>Heatmap — SFR isolated across any two factors</em></td>
  </tr>
  <tr>
    <td width="50%"><img src="docs/assets/tools.png" alt="Tools library showing tool schemas, danger levels, and alias variants"></td>
    <td width="50%"><img src="docs/assets/sessions.png" alt="Sessions list showing configured experiments and factor counts"></td>
  </tr>
  <tr>
    <td align="center"><em>Tools — schemas, danger levels, alias variants</em></td>
    <td align="center"><em>Sessions — composed experiments, ready to run</em></td>
  </tr>
</table>

## Reproducibility data

The repository ships the seeded evaluation set used in the reference experiments, so results are reproducible out of the box. The YAML seeds in [`backend/seed`](backend/seed) and the loader in [`backend/prisma/seed.ts`](backend/prisma/seed.ts) are kept in version control.

| Data type | Count |
| --- | ---: |
| Models | 9 |
| Tools | 14 |
| Tool variants | 10 |
| Personas | 8 |
| Histories | 9 |
| Judges | 4 |
| Test sessions | 23 |

`npm run db:seed` resets the target database to this seeded state. It clears existing harness records first, so point `DATABASE_URL` at the database you intend to reset. See [`docs/repo/seed-data-catalog.md`](docs/repo/seed-data-catalog.md) for the full catalog.

## Quick start

**Prerequisites:** Node.js 18+, npm, and Docker Desktop.

```bash
npm install
cp backend/.env.example backend/.env   # configure DATABASE_URL and provider keys
npm run dev                            # build + run the full Docker stack
npm run db:seed                        # (second terminal) load reproducibility seed data
```

Then open:

- **Frontend** — http://localhost:5173
- **Backend health** — http://localhost:3002/health

### Local development

Run Node/Vite on your host and only PostgreSQL in Docker:

```bash
docker compose up -d db
npm install
npm run db:generate
npm run db:push
npm run db:seed
npm run dev:local
```

The backend reads `DATABASE_URL` from `backend/.env`; the example file targets the Compose database on `localhost:5432`.

## Using the platform

1. **Models** — add provider credentials, or use the seeded placeholder records for dry configuration work.
2. **Tools** — review baseline tool schemas and their alias variants.
3. **Personas** & **Histories** — inspect the system prompts and prior-context templates.
4. **Judges** — choose deterministic or LLM-backed scoring.
5. **Sessions** — create or select a session, preview the payload, then start a run.
6. **Results** — compare failure rates, factor breakdowns, heatmaps, effect sizes, and export CSV.

## Tech stack

| Area | Stack |
| --- | --- |
| Frontend | React 19, Vite, TypeScript, TanStack Query, Tailwind CSS |
| Backend | Express, TypeScript, Prisma |
| Database | PostgreSQL |
| Orchestration | Docker Compose, Turbo |

## Commands

| Command | Purpose |
| --- | --- |
| `npm run dev` | Build and run the Docker Compose stack |
| `npm run dev:local` | Run frontend and backend locally through Turbo |
| `npm run build` | Build all workspaces |
| `npm run db:generate` | Generate the Prisma client |
| `npm run db:push` | Push the Prisma schema to the configured database |
| `npm run db:seed` | Reset the configured database from `backend/seed` |
| `npm run db:studio` | Open Prisma Studio |
| `npm run test:judge --workspace=backend` | Run backend judge tests |

## Documentation

Start with [`docs/README.md`](docs/README.md). Key references:

- [`docs/repo/architecture.md`](docs/repo/architecture.md)
- [`docs/repo/session-guide.md`](docs/repo/session-guide.md)
- [`docs/repo/metrics-and-analysis.md`](docs/repo/metrics-and-analysis.md)
- [`docs/repo/tool-variant-system.md`](docs/repo/tool-variant-system.md)
- [`docs/repo/seed-data-catalog.md`](docs/repo/seed-data-catalog.md)

## Data & safety notes

- The app stores model API keys in the database so providers can be managed through the UI. **Treat the database as sensitive**, avoid committing exported results, and use scoped API keys where possible.
- The harness evaluates high-risk tool *schemas* but **does not execute tools** — it only records whether a model attempted a call.

## License

[MIT](LICENSE) — see [`CONTRIBUTING.md`](CONTRIBUTING.md) to get involved.
