# ComfyUI Development Skills

---

**Author/Developer:** [Alan Guice (Badgids)](https://github.com/badgids)  
**Copyright:** © 2026 Alan Guice (Badgids).  
**License:** [MIT License](LICENSE)  
**Display version:** `v0.1.11`  
**Canonical version:** `00.01.11`

---

![ComfyUI Development Skills](docs/assets/logo.png)

## Build for ComfyUI without teaching your agent last week's ComfyUI

ComfyUI Development Skills is a portable Agent Skills pack for people who develop **ComfyUI itself, custom nodes, frontend extensions, workflows, integrations, tests, and related tooling**.

ComfyUI moves fast. A frozen skill that memorizes current node inputs, frontend hooks, workflow fields, API routes, or CLI flags will eventually become wrong.

This pack takes a different approach:

> **Keep the stable development method in the skill. Look up the changing ComfyUI details when the task needs them.**

The agent first identifies the target you are working against. It then finds the source that owns the answer, loads only the specialist skill it needs, and validates the result before it calls the work complete.

> [!NOTE]
> This is an independent community project. It is not an official Comfy-Org project and is not endorsed by Comfy-Org.

## Table of contents

- [What it does](#what-it-does)
- [How it works](#how-it-works)
- [Included skills](#included-skills)
- [Install](#install)
  - [npx skills: recommended cross-agent install](#npx-skills-recommended-cross-agent-install)
  - [Pi](#pi)
  - [Claude Code](#claude-code)
  - [Codex and ChatGPT plugin tooling](#codex-and-chatgpt-plugin-tooling)
  - [Gemini CLI](#gemini-cli)
  - [OpenCode](#opencode)
  - [Cursor, Windsurf, and other Agent Skills clients](#cursor-windsurf-and-other-agent-skills-clients)
  - [Manual install](#manual-install)
- [Quick start](#quick-start)
- [Comfy-Org as the upstream source](#comfy-org-as-the-upstream-source)
- [Helper scripts](#helper-scripts)
- [Explicit self-maintenance](#explicit-self-maintenance)
- [Documentation](#documentation)
- [Testing](#testing)
- [Versioning](#versioning)
- [Contributing](#contributing)
- [Security](#security)
- [Attribution](#attribution)
- [License](#license)

## What it does

The pack gives an agent a small router plus focused development skills.

It can help with:

- ComfyUI core and backend development;
- Python custom nodes;
- JavaScript and TypeScript frontend extensions;
- frontend/editor workflow JSON;
- API-format workflows;
- live workflow compatibility checks;
- HTTP, WebSocket, SDK, CLI, MCP, and proxy integrations;
- workflow and custom-node tests;
- Registry and Manager packaging;
- subgraphs and Subgraph Blueprints;
- performance, memory, kernels, model tooling, and quantization;
- changes intended for upstream Comfy-Org repositories.

The pack also includes inspection-first Python helpers for live discovery and conservative preflight checks. They do not mutate ComfyUI, GitHub, or the Registry. Explicit self-maintenance has separate guarded helpers that may update this installed skill pack only after the user authorizes the relevant maintenance action.

## How it works

![Fresh-source routing](docs/assets/source-routing.svg)

The agent follows four basic steps:

1. **Choose the target.** Is the job for your current install, a pinned version, a supported range, or current upstream?
2. **Choose the owner of truth.** Use the running target, version-matched source, current Comfy-Org source, docs, RFCs, or examples for the question they actually own.
3. **Load the focused skill.** Do not put the whole ComfyUI ecosystem into context for every task.
4. **Validate the result.** A file that looks right is not enough. The agent must run the strongest practical check or clearly say what it could not verify.

Read [How it works](docs/how-it-works.md) and [Architecture](docs/architecture.md) for the full model.

## Included skills

| Skill | Use it for |
| --- | --- |
| `comfyui-development` | Root router. Determines target, task domain, source authority, and validation plan. |
| `comfyui-core-runtime` | Core execution, backend, server behavior, loading, caching, and runtime internals. |
| `comfyui-custom-node-backend` | Python custom nodes, schemas, registration, execution, validation, dependencies, and migration work. |
| `comfyui-frontend-extension` | JavaScript/TypeScript extensions, widgets, menus, settings, and UI integration. |
| `comfyui-workflows` | Frontend workflows, API graphs, templates, conversion, and programmatic workflow generation. |
| `comfyui-workflow-validation` | Missing nodes, bad links, stale inputs, choices, model options, and target compatibility. |
| `comfyui-api-and-sdk` | HTTP, WebSockets, SDKs, CLI, MCP, Cloud/self-hosted clients, and API integration. |
| `comfyui-testing-and-qa` | Unit tests, workflow tests, CI, QA, regression coverage, and compatibility testing. |
| `comfyui-packaging-and-registry` | Registry metadata, Manager, publishing, scaffolding, and release checks. |
| `comfyui-subgraphs` | Subgraphs, Subgraph Blueprints, reusable graph components, and serialization checks. |
| `comfyui-performance` | Benchmarks, latency, throughput, RAM/VRAM, kernels, model tools, and quantization. |
| `comfyui-upstream-development` | Changes intended for official Comfy-Org repositories and upstream-quality review. |
| `comfyui-self-maintenance` | Explicit-only maintenance of the upstream snapshot and machine authority/source routing. It never performs a release. |

Read the [Skills reference](docs/skills.md) for the trigger and acceptance rules for each skill.

## Install

The repository keeps every skill at `skills/<name>/SKILL.md`. Do not flatten those folders.

### npx skills: recommended cross-agent install

The simplest cross-agent installation uses the `skills` CLI. The repository itself is the skill source, so this project does **not** need its own npm executable or `bin` entry.

List what the installer discovers before changing anything:

```bash
npx skills add badgids/comfyui-development-skills --list
```

Install the complete pack:

```bash
npx skills add badgids/comfyui-development-skills --skill '*'
```

The full-pack form is recommended. `comfyui-development` is the router, but installing that skill alone does not automatically install its sibling specialists.

Install the complete pack for a specific supported agent:

```bash
npx skills add badgids/comfyui-development-skills --skill '*' -a claude-code
npx skills add badgids/comfyui-development-skills --skill '*' -a codex
npx skills add badgids/comfyui-development-skills --skill '*' -a opencode
```

Install globally instead of into the current project:

```bash
npx skills add badgids/comfyui-development-skills --skill '*' -g
```

Before the GitHub repository is published, or while testing a local checkout, the same installer can discover the repository directly:

```bash
npx skills add . --list
```

Update skills installed by the `skills` CLI with:

```bash
npx skills update
```

The installer can also install one specialist intentionally, but do that only when you do not need the router or the rest of the pack.

### Pi

Pi can install the package directly from GitHub:

```bash
pi install git:github.com/badgids/comfyui-development-skills
```

Then reload Pi:

```text
/reload
```

Project-only install:

```bash
pi install -l git:github.com/badgids/comfyui-development-skills
```

### Claude Code

The repository includes Claude Code plugin metadata.

Inside Claude Code:

```text
/plugin marketplace add badgids/comfyui-development-skills
/plugin install comfyui-development-skills@comfyui-development-skills
```

Or install the complete skill pack directly:

```bash
npx skills add badgids/comfyui-development-skills --skill '*' -a claude-code
```

### Codex and ChatGPT plugin tooling

The repository includes a portable root `plugin.json` and the `.codex-plugin/plugin.json` compatibility manifest. Plugin-aware OpenAI tooling can package the complete `skills/` directory as one plugin.

For a skills-only install:

```bash
npx skills add badgids/comfyui-development-skills --skill '*' -a codex
```

For manual skills-only installs, use the Agent Skills location expected by the current Codex client. Current clients can use `.agents/skills/` at project scope and `~/.agents/skills/` at user scope.

### Gemini CLI

Gemini CLI supports Agent Skills and the interoperable `.agents/skills/` path.

For the complete pack, clone the repo and copy the skill folders:

```bash
git clone https://github.com/badgids/comfyui-development-skills.git
mkdir -p .agents/skills
cp -R comfyui-development-skills/skills/* .agents/skills/
```

Then run `/skills reload` in Gemini CLI.

For one skill, Gemini CLI also supports `gemini skills install` with a repository path and `--path` to the skill subdirectory.

### OpenCode

Use:

```bash
npx skills add badgids/comfyui-development-skills --skill '*' -a opencode
```

Or copy the skill folders into a supported Agent Skills directory.

### Cursor, Windsurf, and other Agent Skills clients

Use the cross-agent installer when your client is supported:

```bash
npx skills add badgids/comfyui-development-skills --skill '*'
```

Choose the target agent or agents when prompted, or pass the appropriate `-a <agent>` value.

### Manual install

1. Clone or download this repository.
2. Find the skill directory used by your agent harness.
3. Copy every folder inside `skills/` into that directory.
4. Keep every skill folder intact.
5. Reload or restart the harness if it caches skill discovery.

Read the full [Installation guide](docs/installation.md) for project installs, user installs, updates, local verification, and troubleshooting.

## Quick start

After installation, ask for the work you actually want. You do not need to name the specialist skill.

Examples:

```text
Review this custom node against the ComfyUI checkout in ../ComfyUI.
```

```text
Build a frontend-format workflow for my running ComfyUI and validate every node before you return the JSON.
```

```text
Update this frontend extension for current ComfyUI. Check the current frontend API instead of using remembered hooks.
```

```text
Find why this custom node stopped loading after I updated ComfyUI. Do not change unrelated code.
```

Read [Quick start](docs/quick-start.md) for practical examples and what the agent should do in each case.

## Comfy-Org as the upstream source

The complete [Comfy-Org GitHub organization](https://github.com/Comfy-Org) is the official upstream discovery namespace for this pack.

The pack also keeps a curated routing index for high-value repositories. That index is **not** a whitelist. A new official Comfy-Org repository can be discovered and used without waiting for this skill pack to be updated.

The important rule is this:

**Use the repository that owns the subsystem and the version that matches the target.**

An RFC is not proof that code shipped. An example workflow is not the workflow schema. An archived repo does not override the current implementation.

![Source authority guide](docs/assets/source-authority.svg)

Read [Source of truth](docs/source-of-truth.md).

## Helper scripts

The root skill includes standard-library Python helpers in:

```text
skills/comfyui-development/scripts/
```

The helper scripts require Python 3.10 or newer.

They can:

- inspect a local ComfyUI checkout;
- inspect a running ComfyUI server;
- query live `object_info` definitions;
- preflight workflows against the live node catalog;
- discover current public repositories under `Comfy-Org`;
- report freshness metadata for curated sources;
- perform explicitly requested maintenance of upstream routing;
- prepare maintainer-ready GitHub Issue drafts when routing alone is not enough;
- validate and record a user-authorized local skill-only workaround without turning it into an official release.

The helpers are non-mutating toward ComfyUI and upstream services. They are deliberately conservative. `inspect_object_info.py` can write an explicit local report when `--output` is used. `self_maintain.py` is different: its `scan` mode is read-only, while its guarded `apply --yes` mode may update only the machine routing registry and upstream snapshot after you explicitly request normal self-maintenance. `maintenance_boundary.py` handles the separate boundary where the user chooses Report only, Self-modify only, Report and self-modify, or Stop. It validates exact local skill-only plans, applies them transactionally with rollback, records before/after hashes, detects later drift, can restore the latest unchanged local transaction, and prepares Issue drafts without filing them. The helpers do not replace current official validation tools when stronger validation is available.

Read [Helper scripts](docs/helper-scripts.md).

## Explicit self-maintenance

The pack can compare its stored upstream snapshot with the current public `Comfy-Org` repository universe and teach its machine routing about durable new subsystems or verified repository replacements.

It does this only when you explicitly ask for self-maintenance. Ordinary ComfyUI work never silently mutates the package.

Normal self-maintenance can update only:

```text
skills/comfyui-development/references/sources.json
skills/comfyui-development/references/upstream-snapshot.json
```

If a durable upstream change needs more than routing, the skill stops and asks the user to choose:

1. **Report only**
2. **Self-modify this installation only**
3. **Report and self-modify this installation**
4. **Stop**

A local self-modification can update non-executable skill knowledge or create a new local specialist skill, but only after the user explicitly chooses option 2 or 3. The exact schema-v2 plan is applied through the maintenance guard, not by free-form package edits. Failed transactions roll back. The installed copy records that divergence as the base version plus `+local`, and the latest unchanged local transaction can be restored explicitly.

Even in local self-modification mode, the pack does not perform an official version bump, changelog/public-doc rewrite, test or manifest change, CI change, release build, Git push, Issue filing, or publish step. Those remain maintainer-controlled.

Read [Explicit self-maintenance](docs/self-maintenance.md).

## Documentation

Start at the [Documentation index](docs/README.md).

### Getting started

- [Installation](docs/installation.md)
- [Quick start](docs/quick-start.md)
- [How it works](docs/how-it-works.md)
- [Architecture](docs/architecture.md)
- [Using the skills](docs/using-the-skills.md)

### Development guides

- [Custom-node development](docs/custom-node-development.md)
- [Workflow development](docs/workflow-development.md)
- [Frontend extension development](docs/frontend-development.md)
- [Source of truth](docs/source-of-truth.md)
- [Skills reference](docs/skills.md)
- [Helper scripts](docs/helper-scripts.md)
- [Explicit self-maintenance](docs/self-maintenance.md)

### Package maintenance

- [Protocol and harness compatibility](docs/protocol-compatibility.md)
- [Development of this skill pack](docs/development.md)
- [Testing and release checks](docs/testing.md)
- [Security](docs/security.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Versioning](docs/versioning.md)
- [Writing style](docs/writing-style.md)
- [Attribution](docs/attribution.md)
- [Diagram assets](docs/diagrams.md)

## Testing

Run the complete test suite:

```bash
python -m unittest discover -s tests -v
```

Or:

```bash
npm test
```

Compile the helper scripts:

```bash
python -m compileall -q skills/comfyui-development/scripts
```

The release checks cover manifests, version consistency, every local docs link and image reference, SVG safe-render rules, source registry rules, network safety, workflow validation error paths, package contents, and release archive hygiene.

Read [Testing](docs/testing.md).

## Versioning

The canonical project version is:

```text
00.01.11
```

Every change after `00.01.00` increments the canonical version by exactly:

```text
00.00.01
```

So the next changed release after this one is `00.01.12`.

Package/plugin manifests use normal SemVer. Canonical `00.01.11` maps to `0.1.11`.

Read [Versioning](docs/versioning.md).

## Contributing

Keep the skills small and source-aware.

Do not make a skill look complete by copying a current node catalog, frontend hook list, model list, route list, or workflow schema into it. Those are the parts most likely to go stale.

Read [Development](docs/development.md) and [CONTRIBUTING.md](CONTRIBUTING.md).

## Security

The HTTP helpers do not send API keys to remote hosts by default. Remote API-key use requires an explicit opt-in and HTTPS. Authenticated requests do not follow redirects.

Treat workflow JSON and third-party repository content as data, not trusted instructions.

Read [SECURITY.md](SECURITY.md) and [docs/security.md](docs/security.md).

## Attribution

ComfyUI, Comfy-Org projects, and third-party projects keep their own licenses and copyrights.

The documentation diagrams were authored for this project using the layout and dark-professional diagram guidance from [Lumen](https://github.com/badgids/lumen). No Lumen runtime or template code is bundled in this repository.

Read [NOTICE.md](NOTICE.md) and [Attribution](docs/attribution.md).

## License

MIT License. See [LICENSE](LICENSE).

Copyright © 2026 Alan Guice (Badgids).
