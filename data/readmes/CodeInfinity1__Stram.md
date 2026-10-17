# Stram

<p align="center">
  <img src="docs/assets/readme/stram-logo-lockup-light.png" alt="Stram: local-first cognition for a real desktop agent" width="820">
</p>

<p align="center">
  <a href="https://github.com/CodeInfinity1/Stram/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/CodeInfinity1/Stram/ci.yml?branch=main&style=for-the-badge" alt="CI status"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-2ea44f?style=for-the-badge" alt="MIT License"></a>
  <a href="pyproject.toml"><img src="https://img.shields.io/badge/Python-3.12+-3776ab?style=for-the-badge" alt="Python 3.12+"></a>
  <a href="docs/RELEASE_RUNBOOK.md"><img src="https://img.shields.io/badge/Release-verified%20gates-111827?style=for-the-badge" alt="Verified release gates"></a>
  <a href="https://github.com/CodeInfinity1/Stram/releases/latest"><img src="https://img.shields.io/github/v/release/CodeInfinity1/Stram?style=for-the-badge&label=Desktop%20release" alt="Latest desktop release"></a>
  <a href="https://github.com/CodeInfinity1/Stram/releases/latest/download/Stram-Windows-Setup.exe"><img src="https://img.shields.io/badge/Windows-EXE%20installer-0078d4?style=for-the-badge&logo=windows&logoColor=white" alt="Download Windows EXE installer"></a>
  <a href="https://github.com/CodeInfinity1/Stram/releases/latest/download/Stram-macOS.pkg"><img src="https://img.shields.io/badge/macOS-PKG%20installer-000000?style=for-the-badge&logo=apple&logoColor=white" alt="Download macOS PKG installer"></a>
  <a href="https://deepwiki.com/CodeInfinity1/Stram"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki"></a>
</p>

**A proactive, local-first cognitive agent that works with you like a 24/7 assistant companion.**

Stram is both the runtime and the agent that uses it: a local-first cognitive agent, not a chatbot waiting for the next message. It is a human-assistant-like companion for your computer: always available, context-aware, able to collect allowed signals, understand what is happening, decide whether something matters, and take the next safe step through governed tools without needing you to start with a prompt.

The project is built around practical cognition: collectors absorb desktop, browser, file, app, channel, voice, and connector events; the stimulus layer filters and ranks those signals; Stram forms a working scene, chooses a reflex or plan, uses tools, asks before risky actions, records evidence, and remembers the useful result. The goal is simple: an agent that can notice, reason, act, recover, and improve while remaining inspectable.

This is what makes Stram different: it is not flashy automation hidden behind a prompt box. It is a local, auditable cognitive loop with security, risk management, memory, approvals, and real collectors feeding it the context it needs to work beside you 24/7.

[Contributing](CONTRIBUTING.md) · [Security](SECURITY.md) · [Changelog](CHANGELOG.md) · [Roadmap](docs/ROADMAP.md) · [Agent Positioning](docs/AGENT_POSITIONING.md) · [Release Runbook](docs/RELEASE_RUNBOOK.md) · [Agent Guidance](AGENTS.md)

<p align="center">
  <img src="docs/assets/readme/stram-macos-app.png" alt="Stram macOS app showing the local assistant dashboard" width="920">
</p>

<p align="center">
  <sub>Native macOS shell connected to the local Stram daemon.</sub>
</p>

<p align="center">
  <img src="docs/assets/readme/stram-active-assistant-overview.jpg" alt="Stram active assistant connector fabric and collector architecture overview" width="920">
</p>

<p align="center">
  <sub>Stram turns collectors, stimuli, memory, connectors, policy, and approval-gated tools into one active cognitive loop.</sub>
</p>

## What It Is

Stram is a proactive agent system with four jobs, like a careful assistant working beside you:

1. **Observe the allowed environment:** collectors watch opted-in desktop, browser, file, app, voice, channel, connector, and runtime surfaces.
2. **Understand the signal:** stimuli are redacted, deduped, rate-limited, ranked, and converted into compact context instead of dumping raw private data into prompts.
3. **Act through governance:** Stram can answer, wait, ask, draft, monitor, run tools, call connectors, or request approval depending on risk.
4. **Learn from evidence:** outcomes, failures, approvals, useful facts, and repeated workflows are written into durable memory and skills.

## What It Can Do

| Real-world capability | What that means in practice |
| --- | --- |
| Work without a prompt | Wake from a schedule, file change, channel event, browser/app signal, voice transcript, connector event, or task continuation instead of waiting for chat input. |
| Build a working scene | Combine allowed collectors into a local context: active app, browser state, files, shell output, connector events, channel messages, voice, and prior memory. |
| Decide the right posture | Respond immediately, observe quietly, ask for clarification, draft a reply, monitor a condition, queue a task, recover from failure, or request approval. |
| Use real tools | Operate browser, files, shell, code, OS surfaces, channels, voice, memory, providers, and connector-backed SaaS tools through explicit schemas. |
| Manage risk | Label tools by risk, enforce permissions, redact sensitive payloads, pause high-risk actions, keep approvals human-visible, and write an audit trail. |
| Remember useful context | Keep goals, commitments, environment facts, interaction history, outcomes, lessons, and reusable workflows across sessions. |
| Run on desktop | Use the same local backend from Windows and macOS apps for chat, runs, approvals, channels, voice, settings, model routing, and autonomy controls. |

## Why It Is Different

Most assistants are prompt-first: you ask, they answer, they stop. Stram is environment-first: it can absorb signals from the work surface, decide what matters, and continue a goal over time.

- **Proactive by design:** Stram can wake from collectors, schedules, channel events, file changes, voice, and runtime triggers, not only direct messages.
- **Collectors before action:** local and connector-backed collectors create a metadata-first picture of what is happening before the model plans.
- **Attention before noise:** dwell, dedupe, policy, rate limits, privacy tiers, and model-led attention prevent every event from becoming an action.
- **Reflexes for the fast path:** approvals, interrupts, recovery, wakeups, monitoring, and proof checks can route work without losing the active goal.
- **Risk managed at the tool boundary:** shell, browser mutation, screenshots, external sends, destructive operations, code execution, and sensitive data flows can pause for approval.
- **Memory with jobs:** goals, commitments, profile facts, environment notes, lessons, interaction history, and skills are separated so Stram can recall the right thing for the right reason.
- **Evidence before completion:** Stram should not simply say it succeeded; runs carry traces, tool output, approvals, screenshots, logs, and verifier results where applicable.

## Practical Examples

| Scenario | What Stram can do |
| --- | --- |
| You step away during a build | Notice test output or CI status, summarize the failure, prepare a fix plan, and wait for approval before changing files or running risky commands. |
| A teammate messages in Slack | Treat the message as a channel stimulus, inspect relevant project context, draft a response, and require approval before sending. |
| A calendar event or meeting ends | Detect meeting artifacts or transcript availability, extract action-item metadata, create follow-up tasks, and remember commitments. |
| A browser workflow changes | Observe allowed tab/page metadata, connect it with the current goal, and decide whether to monitor, ask, or continue the task. |
| A file or document changes | Convert the event into context, update the working scene, and resume the related task if it affects an active goal. |
| A high-risk action is needed | Pause with an approval request that explains the tool, purpose, risk, and proposed arguments before execution. |

## The Agent Layer

Stram is both the runtime and the agent that uses it, not two separate named things. The runtime provides the body: APIs, collectors, tools, memory, approvals, native apps, connectors, policy, and release surface. Stram's agent behavior uses that body to act like a cognitive assistant that understands the user's working environment without becoming an uncontrolled recorder.

| Agent layer | What it does |
| --- | --- |
| Collectors | Metadata-first collectors watch allowed desktop, browser, file, app, channel, meeting, developer, knowledge, and business surfaces. |
| Stimuli | Events become structured stimuli with source, privacy tier, confidence, timestamps, dedupe keys, and compact evidence. |
| Attention | Stram ranks stimuli by urgency, relevance, source trust, active goals, user state, and risk before deciding whether to act. |
| Reflexes | Fast paths handle wakeups, approvals, interrupts, recovery, monitoring, cancellation, and proof checks. |
| Connectors | Google Workspace, Microsoft 365, Slack, GitHub, Linear, Notion, Zoom, browsers, IDEs, CRMs, file stores, model providers, and local apps expose governed capability surfaces. |
| Memory | Goals, commitments, focus, background learning, profile facts, lessons, summaries, and skill evolution stay durable across sessions. |
| Governance | Tool schemas, risk levels, permission checks, local outbox records, approval gates, timeline evidence, and redacted traces make the agent inspectable before and after it acts. |

## The USP

Most assistants are either chat-first, code-first, or automation-first. Stram is cognition-first: its agent gets a governed perception loop, a durable memory system, a real desktop body, connector-aware tools, and a safety model that treats user trust as part of the product.

| Product shape | Center of gravity | Stram difference |
| --- | --- | --- |
| Chat assistants | Strong conversational answers after a prompt. | Stram can keep watching allowed signals, maintain goals, wake later, and decide whether to observe, ask, draft, monitor, or act. |
| Coding agents | Repo-aware code changes and tests inside a task session. | Stram includes coding workflows, but the core product is a broader active assistant with collectors, reflexes, connectors, voice/channels, memory, and governed desktop tools. |
| Automation tools | Trigger-action workflows that run when a rule matches. | Stram uses model-led attention, memory, policy, approvals, and evidence instead of only static triggers. |
| Agent runtimes | Tool calls, runs, events, approvals, and APIs. | Stram adds the always-on local stimulus loop, native desktop clients, metadata-first collectors, cognitive state, and proactive recovery paths. |

## API Surface Compared

Reference checkouts under `external_repos/` are useful peers, but they expose different product shapes. Hermes Agent has a strong gateway API around `/v1/runs`, run events, approvals, stops, and toolsets. OpenClaw has deep exec/channel approval mechanics and mobile/watch surfaces. Open Interpreter exposes simple chat/history server examples. browser-use and windows-use are focused automation libraries. screenpipe is a local activity capture/search API.

Stram's novelty is the combined loopback API: cognition, native desktop control, update delivery, channels, voice, approvals, tools, memory, browser sessions, workflows, and autonomy are all one governed runtime surface.

| Stram API | Capability exposed to apps | Not observed as a combined desktop REST surface in the local references |
| --- | --- | --- |
| `/stimuli`, `/stimuli/stream` | Normalize user text, voice transcripts, activity, channel events, and other stimuli into one response/observe/monitor harness with live run events. | Peers usually expose chat/run entrypoints, not a stimulus API tied to attention decisions and desktop response modes. |
| `/channels/*` | Channel catalog, requirements, setup save, doctor, smoke test, inbound preview, listener tick, outbox, prepared sends, and approval-gated live sends. | Hermes/OpenClaw have messaging channels, but not this setup/doctor/smoke/outbox contract consumed by both native desktop apps. |
| `/voice/status` | Let desktop clients pass runtime STT/TTS secrets without echoing values, then show provider readiness before voice workflows. | Other refs include voice features or providers, but not this shared app-facing voice readiness API. |
| `/approvals`, `/runs/*/timeline`, `/runs/*/cancel` | Review pending high-risk actions, inspect evidence timelines, approve/reject/edit, and cancel active work from the same UI. | Hermes has run approvals; Stram adds the native desktop timeline/cancel/approval contract across all local tools. |
| `/memory/*`, `/autonomous/*`, `/triggers/evaluate` | Surface durable memory, summaries, autonomous queue state, wakeups, and trigger evaluation for ongoing cognition. | Reference APIs did not show this cognition state as a first-class desktop API. |
| `/collectors/*` | Configure and tick privacy-first local stimulus collectors for active window, browser context, filesystem changes, clipboard, screenshot/OCR keyframes, video keyframes, and audio activity. Sensitive capture stays opt-in; deterministic dwell, dedupe, batching, policy, and rate filters keep raw telemetry local while compact attention batches reach the harness. | Peers expose chat/gateway events, but not a shared desktop collector layer feeding a governed stimulus/attention loop. |
| `/events/status`, `/events/rebuild-context` | Convert compact collector batches and direct text/voice/channel stimuli into semantic events, generated `current_context.md` / `events.md`, and queued autonomous action candidates. | Peers expose run events, but not a privacy-first semantic event layer that turns local stimuli into durable context before autonomous action. |
| `/tools`, `/tools/search`, `/tools/describe`, `/capabilities` | Publish the active governed tool catalog, schemas, risk levels, and capability groups to the UI. | browser-use/windows-use expose tool libraries; Stram exposes a governed cross-domain catalog to native clients. |
| `/browser/sessions`, `/screen/captures`, `/permissions` | Inspect browser sessions, local screen evidence, and permission posture before or after tool use. | screenpipe has local capture APIs and browser-use has browser actions; this ties those surfaces into the agent approval/audit runtime. |
| `/updates/latest` | Existing desktop users can check the latest GitHub release and open the platform-specific download without leaving the app. | The local references checked did not expose a shared release-update endpoint for native desktop shells. |

## Quick Install

Stram currently targets Python 3.12+.

```bash
git clone https://github.com/CodeInfinity1/Stram.git
cd Stram
python3 -m pip install -e ".[browser,pdf,ocr,office,test]"
```

Optional browser support:

```bash
playwright install chromium
```

Copy the example environment file only when you need model, voice, channel, or release settings:

```bash
cp .env.example .env
```

Do not commit `.env` or real secrets.

## Package Manager Installs

Desktop installers are published on the latest GitHub release:

- [Download the Windows EXE installer](https://github.com/CodeInfinity1/Stram/releases/latest/download/Stram-Windows-Setup.exe)
- [Download the Windows ZIP archive](https://github.com/CodeInfinity1/Stram/releases/latest/download/Stram-Windows.zip)
- [Download the macOS PKG installer](https://github.com/CodeInfinity1/Stram/releases/latest/download/Stram-macOS.pkg)
- [Download the macOS ZIP archive](https://github.com/CodeInfinity1/Stram/releases/latest/download/Stram-macOS.zip)
- [Verify release checksums](https://github.com/CodeInfinity1/Stram/releases/latest/download/checksums.txt)

Package-manager metadata is checked into this repository and mirrored to dedicated package-manager repos where needed. See [Package Manager Distribution](docs/PACKAGE_MANAGERS.md) for publishing and registry-submission details.

macOS with Homebrew:

```bash
brew tap CodeInfinity1/stram
brew trust CodeInfinity1/stram
brew install --cask stram
```

Windows with WinGet local manifest:

```powershell
winget install --manifest .\winget\manifests\b\CodeInfinity1\Stram\1.0.0
```

Windows with Scoop:

```powershell
scoop bucket add stram https://github.com/CodeInfinity1/scoop-stram
scoop install stram
```

Windows with Chocolatey package source:

```powershell
choco pack .\chocolatey\stram\stram.nuspec --out .
choco install stram --source . -y
```

Official WinGet and Chocolatey registry availability requires external repository/review or account/API-key submission. Public production macOS installs should use a Developer ID signed and notarized package, and Windows installs should use an Authenticode-signed EXE; until those certificate flows are complete, Gatekeeper and Windows SmartScreen may warn that the publisher is unverified.

**macOS Gatekeeper warning workaround:** the current `.pkg` and `.zip` releases are not yet Developer ID signed/notarized, so opening them will show "Apple could not verify this app is free of malware." This is expected for this release, not a corrupted download. To install anyway:

1. Try opening the `.pkg` normally first, then go to **System Settings → Privacy & Security**, scroll to the Security section, and click **Open Anyway** next to the Stram warning.
2. If macOS blocks it outright with no "Open Anyway" option, clear the quarantine flag from Terminal instead:
   ```bash
   xattr -dr com.apple.quarantine /path/to/Stram-macOS.pkg
   ```
   (or on the installed `.app`, e.g. `xattr -dr com.apple.quarantine "/Applications/Stram.app"`)
3. Always verify the download against [checksums.txt](https://github.com/CodeInfinity1/Stram/releases/latest/download/checksums.txt) before bypassing Gatekeeper — the warning is expected, a checksum mismatch is not.

**Windows SmartScreen warning workaround:** the current `Stram-Windows-Setup.exe` and `.zip` releases are not yet Authenticode-signed, so running the installer will show "Windows protected your PC" / "Microsoft Defender SmartScreen prevented an unrecognized app from starting." This is expected for this release, not a corrupted download. To install anyway:

1. On the SmartScreen dialog, click **More info**, then click **Run anyway**.
2. If the file was blocked on download instead (no SmartScreen dialog appears when double-clicked), right-click the `.exe` → **Properties** → check **Unblock** at the bottom of the General tab → **OK**, then run it again.
3. From PowerShell you can unblock the same way without the UI:
   ```powershell
   Unblock-File -Path .\Stram-Windows-Setup.exe
   ```
4. Always verify the download against [checksums.txt](https://github.com/CodeInfinity1/Stram/releases/latest/download/checksums.txt) before bypassing SmartScreen — the warning is expected, a checksum mismatch is not.

## First Run

Run a safe explicit tool call:

```bash
python3 -m stram run "system_status {}" --workspace . --planner explicit
```

Ask the model-led planner to inspect the project:

```bash
python3 -m stram run "summarize this project and tell me the next best task" --workspace . --planner model
```

Start the local API and dashboard:

```bash
python3 -m stram serve --workspace . --port 8765
```

Then open:

```text
http://127.0.0.1:8765/
```

## Native Desktop Apps

The native clients are optional shells around the same local runtime.

| Platform | Source | Local run |
| --- | --- | --- |
| macOS | `apps/macos` | `swift run --package-path apps/macos StramMac` |
| Windows | `apps/windows/Stram.App` | Build with the .NET 8 SDK on Windows or the release workflow. |

Recommended desktop loop:

```bash
python3 -m stram serve --workspace . --port 8765
swift run --package-path apps/macos StramMac
```

The macOS and Windows apps share backend routes for chat, tools, channels, channel setup, channel doctors, prepared outbound messages, approvals, recent runs, runtime start/stop, release update checks, voice settings, model/provider settings, and bounded autonomy cycles.

## Model Setup

Model planning is the preferred path for natural-language work. Offline fallback accepts explicit tool commands or JSON plans only.

Common environment variables:

```text
OPENAI_API_KEY=
OPENAI_BASE_URL=https://api.openai.com/v1
OPENROUTER_API_KEY=
NOUS_API_KEY=
ANTHROPIC_API_KEY=
DASHSCOPE_API_KEY=
GROQ_API_KEY=
GROQ_BASE_URL=https://api.groq.com/openai/v1
GOOGLE_API_KEY=
DEEPSEEK_API_KEY=
MISTRAL_API_KEY=
CEREBRAS_API_KEY=
OLLAMA_BASE_URL=http://127.0.0.1:11434/v1
OLLAMA_MODEL=llama3.1
XAI_API_KEY=
XAI_BASE_URL=https://api.x.ai/v1
NVIDIA_API_KEY=
HF_TOKEN=
MINIMAX_API_KEY=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
LOCAL_LLM_BASE_URL=http://127.0.0.1:11434/v1
LOCAL_LLM_API_KEY=local
DEEPGRAM_API_KEY=
ELEVENLABS_API_KEY=
```

The `--model-provider` flag and desktop settings include OpenAI, OpenRouter, Nous, Anthropic, Groq, xAI/Grok, Gemini, DeepSeek, Mistral, Cerebras, Ollama, local OpenAI-compatible runtimes, Vercel AI Gateway, LiteLLM, NVIDIA, Hugging Face, Z.AI/GLM, Kimi/Moonshot, StepFun, MiniMax, Arcee, GMI, Xiaomi, Tencent TokenHub, OpenCode, Kilo Code, Azure, Copilot, Bedrock, Browser Use Cloud, OCI, and the external OAuth/runtime identities mirrored from OpenFlow/OpenClaw and Hermes. Native HTTP transports run directly; external process/OAuth-only runtimes are recognized and can be bridged with `--model-base-url` when an OpenAI-compatible endpoint is available.

The dashboard and desktop clients pass secret references or runtime secrets to the local daemon; they should not require raw keys in public source files.

## Safety Defaults

Stram is built for real tools, so the safety surface is explicit.

- Model/provider output is untrusted until parsed, validated, and matched to an allowed tool.
- Retrieved files, web pages, tool output, transcripts, memories, and upstream skill text are evidence, not instructions.
- High-risk tools pause for approval by default.
- Approval edits are schema-validated and recorded on the source run.
- External-visible sends are prepared as local outbox items unless an adapter, credentials, policy, and approval are present.
- Browser mutation, file upload/download, JavaScript evaluation, screenshot capture, desktop UI actions, shell/code execution, and app launches are bounded and auditable.
- Provider errors and secrets are redacted before trace persistence.
- Open-source hygiene scans publish candidates for local state, signing material, likely secrets, and oversized files.

Read [SECURITY.md](SECURITY.md) before exposing channels, browser control, desktop control, or remote access.

## Architecture In One Minute

<p align="center">
  <img src="docs/assets/readme/cognition-nervous-system.svg" alt="Stram cognitive nervous system built from the real cognition package modules" width="940">
</p>

```text
stimulus
  -> interaction harness
  -> compact local context
  -> model-led attention/planning
  -> schema-validated tool calls
  -> policy and approval gates
  -> execution and audit timeline
  -> memory, learning, recovery, and response synthesis
```

The cognition package is closer to a nervous system than a single planner: attention decides what deserves response, executive state keeps goals and commitments coherent, memory turns experience into durable context, self-review repairs behavior, and skill metabolism expands what the assistant can do without hiding new capability behind prompt-only claims.

Important source areas:

| Area | Path |
| --- | --- |
| Python runtime | `stram/` |
| Cognition stores and loops | `stram/cognition/` |
| Tool registry and implementations | `stram/tools/` |
| Policy, approvals, audit, permissions | `stram/safety/` |
| REST API and dashboard | `stram/api.py`, `stram/dashboard/` |
| Prompt resources | `stram/resources/prompts/` |
| Skills | `skills/` |
| Desktop apps | `apps/` |
| Release automation | `script/` |

The hard rule: broad assistant behavior stays model-led and schema-driven. Deterministic code validates, constrains, audits, persists, packages, and executes explicit tools; it does not become a hidden keyword router for natural language.

## Docs By Goal

| Goal | Start here |
| --- | --- |
| Understand agent behavior | [Cognitive architecture](docs/COGNITIVE_AGENT_ARCHITECTURE.md) |
| Understand the no-keyword-routing rule | [Global agent instructions](docs/GLOBAL_AGENT_INSTRUCTIONS.md) |
| Add or review a skill | [Skill authoring standard](docs/AGENT_SKILL_AUTHORING_STANDARD.md) |
| Build or package a release | [Release checklist](docs/RELEASE_CHECKLIST.md) and [release runbook](docs/RELEASE_RUNBOOK.md) |
| See planned work | [Roadmap](docs/ROADMAP.md) |
| Work as a coding agent in this repo | [AGENTS.md](AGENTS.md) |

## Contributor Quick Start

```bash
python3 -m pip install -e ".[browser,pdf,ocr,office,test]"
python3 -m unittest discover -v
python3 script/verify_open_source_hygiene.py
python3 scripts/smoke_real_world_tasks.py --workspace .
```

Before opening a PR, include the real behavior proof: exact commands, OS, model/provider path if relevant, observed result, and what you did not test.

Read [CONTRIBUTING.md](CONTRIBUTING.md) for contribution priorities, tool-vs-skill guidance, tests, and PR expectations.

## Release Readiness

The public release path is intentionally stricter than a source build.

```bash
python3 -m py_compile script/verify_open_source_hygiene.py script/verify_publication_state.py script/verify_release_readiness.py script/generate_release_report.py
python3 -m unittest discover -v
python3 script/verify_desktop_parity.py
python3 script/verify_desktop_runtime_smoke.py
python3 script/verify_package_managers.py
python3 script/verify_open_source_hygiene.py
python3 scripts/smoke_real_world_tasks.py --workspace .
python3 script/verify_release_readiness.py --require-website --release-tag v0.1.0
python3 script/generate_release_report.py --require-website --check-github-release
```

Strict public release completion also requires signed/notarized macOS assets, signed Windows assets, checksums, a published GitHub release, and website download verification. See [docs/RELEASE_RUNBOOK.md](docs/RELEASE_RUNBOOK.md).

## Status

Stram 1.0.0 is the first tagged production release. The local runtime, tool contracts, skills, safety gates, desktop shells, release checks, and smoke coverage are covered by automated tests and release-readiness gates, but live provider/channel/desktop workflows still depend on the credentials and platform-specific signing you configure for your own deployment.

Use it, inspect it, improve it, but do not treat it as a silent background operator until you have reviewed the approval and channel setup for your environment.

## License

MIT. See [LICENSE](LICENSE).
