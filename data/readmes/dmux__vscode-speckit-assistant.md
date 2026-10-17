# Spec Kit Assistant for VS Code

![VS Code](https://img.shields.io/badge/VS%20Code-%5E1.93.0-007ACC?logo=visualstudiocode)
![Version](https://img.shields.io/badge/version-0.1.2-5E5CE6)
![License](https://img.shields.io/badge/license-MIT-2ea043)

Visual orchestrator for Spec-Driven Development with Spec Kit, directly inside VS Code.

Spec Kit Assistant gives you a guided phase-by-phase workflow in the sidebar — from constitution to implementation — with review gates, live console feedback, an interactive task checklist, stale-phase alerts, and a full DAG visualization of your entire project.

![SDD Workflow Map showing Constitution node connected to two feature rows with Spec, Plan, Tasks and Implementation phases, task progress bars, and phase status colours](resources/screenshot-workflow-map.png)

## Why use this extension

- Run the full SDD flow without leaving VS Code.
- Keep generated artifacts organized under `.specify/` and `specs/`.
- Approve or discard each phase with explicit review gates.
- Reply to AI terminal prompts directly from the sidebar UI.
- Switch AI backends (`claude`, `gemini`, `copilot`, `openai`) with one setting.
- Visualize your entire project as an interactive DAG with live status.

## Features

### Guided SDD Workflow

Dedicated activity bar view with five sequential phases per feature:

| Phase | Artifact |
|---|---|
| Constitution | `.specify/memory/constitution.md` |
| Specification | `specs/<feature>/spec.md` |
| Planning | `specs/<feature>/plan.md` |
| Tasks | `specs/<feature>/tasks.md` |
| Implementation | Code changes in your workspace |

Each phase moves through four states: **idle → running → awaiting review → approved**.

### SDD Workflow Map (DAG)

Open a full-screen interactive graph of your entire project via the toolbar button or **Spec Kit: Open Workflow Map** from the Command Palette.

- Constitution node at the top, with one feature row per feature below.
- Phase nodes colour-coded by status (idle / running / awaiting review / approved).
- Animated edges while a phase is running.
- **Tasks node** shows the total task count derived from `tasks.md`.
- **Implementation node** shows a live progress bar (`X/N tasks`) that updates as you tick checkboxes in the sidebar.
- Click any artifact link (📄) to open it in the editor.
- Minimap and zoom controls included.

### Inline Task Checklist

When the Tasks phase has content, the sidebar renders an interactive checklist directly from `tasks.md`:

- Tick checkboxes without opening the file — changes are written to disk immediately.
- Progress bar (`done / total`) updates in real time.
- The DAG Implementation node reflects the same progress.

### Stale Phase Alerts

If you discard and re-run a phase after downstream phases were already approved, those phases are automatically flagged with a visible warning:

> ⚠ An earlier phase was re-run — this approved output may be outdated. Consider re-running.

Discarding the Constitution marks every feature phase as stale. The flag clears when you approve or discard the stale phase.

### Clarification Templates

Each feature phase offers a **↙ template** button that pre-fills the clarification field with a structured scaffold:

| Phase | Template sections |
|---|---|
| Specification | Goal / User persona / Acceptance criteria / Out of scope |
| Planning | Stack & constraints / Architecture / Dependencies / Open questions |
| Tasks | Task preferences / Steps to expand / Steps to skip |
| Implementation | Patterns to follow / Conventions / Do not change |

### Console Panel

- Live terminal output stream from the AI agent.
- Automatic prompt detection with quick-reply buttons (`y`, `n`, numbered options).
- Manual input field for custom replies.

### File Explorer

Browse all generated markdown artifacts grouped by feature, with kind icons (📜 constitution, 📋 spec, 🗺 plan, ✅ tasks).

## Requirements

- VS Code `^1.93.0`
- A workspace folder open in VS Code
- `specify` CLI available in your shell PATH
- At least one configured AI CLI:
  - `claude` (Anthropic)
  - `gemini` (Google)
  - `ghcs` (GitHub Copilot CLI)
  - `codex` (OpenAI Codex CLI)

## Quick Start

1. Open your project folder in VS Code.
2. Click the Spec Kit icon in the activity bar.
3. If `.specify/` is missing, choose an AI agent and click **Initialize Spec Kit**.
4. Run the **Constitution** phase and approve it.
5. Create a feature, then run each phase in sequence and approve.
6. Open the **Workflow Map** (toolbar button) to see the full DAG at any time.

Generated docs are organized as:

```text
.specify/memory/constitution.md
specs/<feature-name>/spec.md
specs/<feature-name>/plan.md
specs/<feature-name>/tasks.md
```

## Commands

| Command | Description |
|---|---|
| `speckit.openDag` | Open the SDD Workflow Map in a new editor tab |
| `speckit.refreshFiles` | Refresh Spec Kit files and workflow state |
| `speckit.openInEditor` | Open a generated file in the editor |

## Extension Settings

| Setting | Type | Default | Description |
|---|---|---|---|
| `speckit.aiAgent` | `string` | `claude` | AI backend to run workflow phases (`claude`, `gemini`, `copilot`, `openai`) |
| `speckit.agentPath` | `string` | `""` | Optional custom executable path for the selected AI agent |

## Development

### Install dependencies

```bash
npm install
```

### Build

```bash
npm run build
```

### Watch mode

```bash
npm run dev
```

### Type check

```bash
npm run typecheck
```

### Tests

```bash
npm test
npm run test:coverage
```

## Package as VSIX

```bash
npm run vsix
```

This generates a `.vsix` file at the project root.

Install locally:

```bash
code --install-extension speckit-assistant-0.1.2.vsix
```

## Troubleshooting

### `specify` command not found

Install Spec Kit CLI and make sure it is available in your PATH:

```bash
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git
```

### Agent CLI not found

Set `speckit.agentPath` to the full executable path, or install the default CLI for your selected `speckit.aiAgent`.

### No files appearing in the sidebar

- Confirm your workspace is open as a folder.
- Run **Spec Kit: Refresh Files** from the Command Palette.
- Verify `.specify/` and `specs/` exist and are readable.

### Shell integration not available

The live console output requires VS Code shell integration (bash, zsh, fish, or PowerShell). If output is not streaming, ensure your terminal shell is supported and shell integration is enabled.

## License

MIT. See `LICENSE.md`.
