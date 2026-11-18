# Blender AI Agent

A local, safety-oriented AI-to-3D pipeline that connects LLM planning, Blender generation, visual review, semantic motion, artifact export, and a browser-based Web Studio.

The project uses **MCP (Model Context Protocol)** as the tool boundary between the AI layer and Blender. The model does not get unrestricted `bpy` or arbitrary Python execution during normal operation; it plans against validated, allowlisted tools.

## What it does

```text
Prompt
  ↓
LLM planning
  ↓
Semantic structure / generation blueprint
  ↓
Controlled geometry + refinement
  ↓
Blender via MCP bridge
  ↓
Read-only vision review
  ↓
Semantic motion / animation
  ↓
PNG + GLB + MP4 artifacts
  ↓
FastAPI + React / Three.js Web Studio
```

Current capabilities include:

- Prompt-driven semantic 3D generation
- Reusable geometry and refinement systems
- Creature, robot, vehicle, prop, and architecture workflows
- Read-only visual critique with Qwen-VL
- Semantic articulation and motion planning
- Dragon wing, tail, locomotion, and reference-inspired motion experiments
- Robot walking and articulated arm actions
- Spaceship / prop / architecture presentation motion
- Controlled preview, GLB, and H.264 MP4 artifact generation
- Job orchestration, revisions, confirmation, rollback, and artifact tracking
- FastAPI backend and React + Three.js Web Studio

> This is an experimental procedural 3D system, not a production sculpting or game-asset pipeline. Geometry and locomotion quality are still being actively improved.

## Core idea

A normal LLM tool call is the easy part. The harder problem is building a system around the model that is **structured, controllable, measurable, and safe**.

This repository therefore keeps Blender mutation behind typed tools, validation, ownership, confirmation, and rollback rather than exposing arbitrary scene scripting.

## Architecture

```text
User / Web Studio
        │
        ▼
FastAPI / Job Runtime
        │
        ▼
LLM Planner (Ollama / Qwen)
        │
        ▼
Generation + Refinement + Motion Engines
        │
        ▼
MCP Tool Layer
        │
        ▼
Socket Bridge
        │
        ▼
Blender Runtime
        │
        ├── PNG previews
        ├── GLB exports
        └── MP4 renders

Read-only Vision (Qwen-VL) reviews rendered output but does not mutate Blender directly.
```

## Main packages

| Package | Purpose |
|---|---|
| `core/` | shared models, configuration, DI, tools, bridges, validation |
| `mcp_server/` | MCP tool registration and server boundary |
| `mcp_client/` | MCP client / smoke paths |
| `blender_addon/` | Blender-side runtime and controlled scene operations |
| `generation_engine/` | generation planning and compilation |
| `general_3d_engine/` | reusable semantic composition / recipes / camera logic |
| `geometry_engine/` | controlled geometry representation and planning |
| `shape_refinement_engine/` | refinement policies, articulation readiness, efficiency |
| `anatomy_engine/` | reusable anatomy/layout systems |
| `animation_engine/` | controlled animation/video primitives |
| `motion_engine/` | semantic motion, interpolation, chains, validation, sequencing |
| `reference_engine/` | reference-video motion analysis and style extraction |
| `vision_engine/` | read-only visual critique and comparison |
| `platform_runtime/` | projects, jobs, revisions, artifacts, workers |
| `web_backend/` | FastAPI API, SSE, artifact delivery |
| `web_studio/` | React/Vite product UI |
| `web_viewer/` | Three.js viewer utilities |
| `tests/` | unit and Blender integration validation |

## Requirements

- Windows is the most-tested development environment
- Python 3.11+
- Blender 5.x (parts of the add-on are compatible with 4.2+)
- Node.js + npm
- Ollama

Python dependencies:

```powershell
python -m pip install -r requirements.txt
```

Frontend dependencies:

```powershell
cd web_studio
npm install
```

## Local models

Model weights are **not stored in this repository**. Install them locally with Ollama.

Example setup:

```powershell
ollama pull qwen3-coder-next:latest
ollama pull qwen3-vl:8b
```

Optional larger vision audit model:

```powershell
ollama pull qwen3-vl:32b
```

The exact model names can be changed through runtime configuration / environment variables.

## Quick start

### 1. Start the Blender bridge

From the repository root, use the bridge runtime appropriate for your local Blender installation. A development example is:

```powershell
$env:BAA_BLENDER_PORT="8770"
& "C:\path\to\blender.exe" --background --factory-startup --python "tests\blender\run_bridge_runtime.py"
```

Do not copy that Blender path literally; point it at your own installation.

### 2. Start the API

Open a second terminal:

```powershell
cd C:\path\to\Blender-AI-Agent
$env:BAA_BLENDER_PORT="8770"
python -m uvicorn web_backend.app:create_app --factory --host 127.0.0.1 --port 8000
```

### 3. Start Web Studio

Open a third terminal:

```powershell
cd C:\path\to\Blender-AI-Agent\web_studio
npm.cmd run dev
```

Vite will print the local Web Studio URL (commonly `http://127.0.0.1:5174/`).

## Tests

Python:

```powershell
python -m pytest -q
python -m unittest discover -s tests -v
```

Frontend:

```powershell
cd web_studio
npm.cmd run test
npm.cmd run build
```

Blender integration validators live under `tests/blender/` and require a compatible Blender runtime.

## Safety model

Normal operation intentionally avoids exposing:

- arbitrary model-generated Python
- unrestricted `bpy`
- unrestricted Blender operators / BMesh
- arbitrary F-curves, drivers, or constraints
- arbitrary filesystem paths
- arbitrary FFmpeg arguments

Instead, the project uses bounded semantic structures and allowlisted tools with validation, revision ownership, confirmation, and rollback.

Vision remains read-only.

## Generated data

The following are intentionally excluded from Git:

- Ollama / Qwen model weights
- `node_modules`
- generated `artifacts/`
- runtime SQLite databases
- logs and caches
- Blender autosaves
- environment / secret files

See `.gitignore`.

## Documentation

Detailed implementation notes are under [`docs/`](docs/), including geometry, animation, vision feedback, backend/API, Web Studio, GLB export, safety-oriented generation, and migration notes.

## Project status

This is an active experimental project. The repository currently demonstrates an end-to-end local AI → Blender → Vision → Motion → Web workflow, while areas such as higher-fidelity modeling, contact-aware IK, motion polish, and richer interactive animation export remain ongoing work.

## License

[GNU General Public License v3.0](LICENSE).

`blender_addon/` imports `bpy` and registers through `bl_info`, which makes it
a Blender add-on rather than an independent program. Blender is GPL-licensed
and the Blender Foundation treats add-ons that import `bpy` as needing to be
GPL-compatible, so the repository is released under GPL-3.0 to stay clearly
within those terms.

Third-party components keep their own licences and none are vendored here:
Blender (GPL), Ollama and the Qwen models it serves, FastAPI, React, and
Three.js.
