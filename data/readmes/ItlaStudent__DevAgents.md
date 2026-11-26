# DevAgents

[Español](README.es.md)

**DevAgents is a free, open-source agentic development environment (ADE) in beta.** The graphical app is for 64-bit Windows 10/11; the engine, CLI, and MCP server also run on Linux. Work with one model in Direct mode or distribute an order across several models in Orchestrated and Hive modes. Capabilities and their limits are listed below.

> **Documentation snapshot: 23 Nov 2026.** The source code is public under Apache-2.0; there are no published binaries or installer yet: today you build from source. An installable package has been built and tested on the development machine; a clean-machine walkthrough is pending. [Package report](docs/evidencia/FASE0-20261110/T4-informe-20261113.txt).

![DevAgents — multi-agent orchestrator, local and verifiable](docs/img/devagents-portada.png)

![DevAgents app mockup](docs/img/devagents-maqueta.png)

![Orchestration diagram: one central agent distributes work across models and agents](docs/img/devagents-esquema.png)

[App screenshot](docs/img/devagents-cabina.png), taken on 10 Nov 2026 on the development machine.

The graphical interface is available in English and Spanish (chosen in Settings); the CLI help also answers in English with `DEVAGENTS_LANG=en`, although the rest of the CLI output remains in Spanish.

## What you can do today

- **Direct** (default): chat with a model, read and edit the project, and run tools, with permissions and approvals.
- **Orchestrated**: plan an order, distribute tasks across Git spaces, and subject delivery to another vendor's audit and deterministic checks.
- **Hive**: choose several models and their roles to build and audit in parallel.
- **Best of N**: compare solutions from several providers in separate spaces.
- **DevAgents mode**: the main agent delegates independent parts to subagents.
- **APIs and local models**: register API providers and connect Ollama.
- **External CLIs**: use Claude Code, Codex, Gemini CLI, or OpenCode with their configuration and model access.
- **Accounts and project rules**: isolated Codex and Claude Code accounts, quota rotation, and editable project rules.
- **Native MCP and CLI**: `devagents-mcp.exe` over stdio and `devagents.exe` as the CLI, with files, terminal, Git, plans, and spaces.
- **Agent browser**: tools to inspect and interact with pages and with an app server.
- **Order graph**: see tasks, audits, parallel groups, memory, and replanning.
- **Package and diagnostics**: an installable package on the development machine and a `doctor` command to inspect the environment.
- **Updater**: notify about releases and apply on exit, with consent and no active orders.
- **Forge delivery**: prepare a branch, commit, and pull request after approval.
- **Student mode** (turned on in Settings › Student mode): study a folder or a project with a topic route, step-by-step lessons that cite your files, practice, a lab, notes with spaced review, and a tutor. The placement exam is optional. Studies are saved in the folder's `.student/`. See the [user guide](docs/USER-GUIDE.md#student-mode).

The piece-by-piece detail, with status and evidence, is in the [capability table](#evidence-and-status-of-each-piece) and the [user guide](docs/USER-GUIDE.md).

## Install and send your first order

**There are no published binary downloads or installer today.** The following instructions are for building from source. The existing package is not a published release or a clean-machine-validated installation. [Package status](docs/evidencia/FASE0-20261110/T4-informe-20261113.txt).

Requirements: 64-bit Windows 10/11, WebView2, Git for spaces, and Zig 0.16.0 and Node.js to build. Building and running the app takes about **1.8 GiB**, measured on 23 Nov 2026 in a clean clone of the public repository: clone 0.83 GiB, build cache 0.71 GiB, and binaries 0.22 GiB, not counting the Zig and Node.js installations or the interface's `node_modules`. The full test suite also uses its own cache of about **1.3 GiB** (measured on 23 Nov 2026). [Measurement](docs/evidencia/FASE1-20261121/DV-R1-espacio.txt). The launcher warns when fewer than 3 GiB remain. These steps were checked against the launcher and build configuration; **a clean installation was not tested live in this review**. [Review details](docs/evidencia/FASE0-20261110/T10-sol-informe.txt).

1. Clone this repository and open its folder.
2. Run `DevAgents.bat`. It checks dependencies; if Zig is missing it offers a download into `toolchain\` and checks its SHA-256. If Node.js is missing it offers to install LTS through `winget`. **Installation prompts wait for your answer for 20 seconds and, with no answer, install nothing** (the default option is No); use `/nodeps` to prevent automatic dependency installation. The launcher checks/builds and opens the app on every run.
3. Choose a test project folder. Under **Settings › Providers**, add your provider, or configure a detected CLI under **External agents**. Providers or subscriptions may have their own costs.
4. Select **Direct** and an available model. Send a small first order: "Read this folder and describe its files without changing them." Review the response and permission requests before asking for changes.

Options read in the launcher are `/rebuild` (full build), `/ui` (interface only), `/nodeps` (do not install dependencies), `/devtools` (debugging), and `/limpiar` (delete cache and binaries, then exit). This is a getting-started guide, **not tested live end to end in this review**. [Launcher review](docs/evidencia/FASE0-20261110/T10-sol-informe.txt).

With Zig and Node.js ready, from the repository root:

```powershell
zig build runtime-binaries -j1
.\zig-out\bin\devagents-core.exe doctor
.\zig-out\bin\devagents-host.exe
```

Names and destinations were checked against `build.zig`; these commands were not executed in this review. [Review details](docs/evidencia/FASE0-20261110/T10-sol-informe.txt).

| File in `zig-out\bin` | Intended use |
|---|---|
| `devagents-host.exe` | Windows graphical app |
| `devagents-engine.exe` | Engine process |
| `devagents_core.dll` | Engine library |
| `devagents-core.exe` / `devagents.exe` | CLI; the latter aliases the same binary |
| `devagents-mcp.exe` | MCP server over stdio |

For MCP configuration, see the [surface and authentication matrix](docs/MCP-SURFACE-MAP.md). Connecting from a real external IDE remains **not tested live**.

### Linux (engine, CLI and MCP; beta)

**Beta: engine, CLI, and MCP; no graphical app.** In an Ubuntu 24.04 container (Docker on WSL2, no network) the engine suite passed on 17 Nov 2026: 24/24 steps, 2276/2492 tests, and 216 skipped, each with its reason (Windows-only semantics or an external CLI that is not available). A `.tar.gz` package with `devagents`, `devagents-mcp`, `key-admin`, `LICENSE`, and `NOTICE` was tested in a clean container: `--version`, `doctor`, keys in `~/.config/devagents` with 0700/0600 permissions, and MCP over stdio with 121 tools. An order with the test worker plans and dispatches, but without a real model there is no audit and delivery stays blocked ("unaudited"); **an order with a real model on Linux is not yet tested live**. Containment is partial (`posix_partial`: process group and per-process limits; without cgroup v2 delegation there is no process cap). Debian 12 is a target that has **not been measured**. No package is published. The graphical app remains Windows-only. [Linux suite](docs/evidencia/FASE0-20261110/T9-B-suite-linux-sol-4c.txt), [package](docs/evidencia/FASE0-20261110/T9-B-paquete-sol.txt), [order and MCP](docs/evidencia/FASE0-20261110/T9-B-orden-mcp-sol.txt).

## Governance

Governance in Orchestrated/Hive combines another vendor's audit, citation checks, budget, command policy, and a chained ledger. If no usable verdict is available, the order shows "unaudited" (`audit_unavailable`) and delivery is blocked. **Direct does not add that audit.** These mechanisms have code review and tests; their effectiveness without false alarms in a controlled case on the current version remains **not tested live**. [Governance guide](docs/USER-GUIDE.md).

MCP keeps permission and spending decisions in the app; its commands may require human approval. It does not have full interface parity. [MCP map](docs/MCP-SURFACE-MAP.md).

## Privacy: what leaves your machine

The app stores its data in **`%LOCALAPPDATA%\DevAgents-Angel`** by default. DevAgents API keys are encrypted with Windows DPAPI; CLI credentials are managed by each CLI. These statements come from code review, not a traffic audit.

**Local does not mean everything runs offline.** Depending on configuration and tools used:

- Messages, context, memory, and file content read by the agent may be sent to the model provider. **Orchestrated and Hive involve several models**: planner, executors, and auditors, potentially from different vendors.
- **Claude Code → Anthropic, Codex → OpenAI, and Gemini CLI → Google**; OpenCode uses the providers/models configured in that CLI. Each external tool has its own data and telemetry rules, which DevAgents does not control.
- **`web_search`** sends queries to Tavily or Brave Search when configured with a key; without that key it uses DuckDuckGo. **`web_fetch`** requests the specified public pages. The integrated browser loads pages opened by you or the agent.
- Model discovery and health checks contact providers; delivery, issues, webhooks, and notifications contact configured services. The updater checks GitHub Releases and can be disabled in Settings. The development launcher downloads dependencies.

No session upload to a DevAgents-owned server was found in the reviewed code. This **does not certify the absence of network traffic** or establish the behavior of WebView2 or third-party CLIs.

## Tests and CI

There is continuous integration on GitHub Actions (`.github/workflows/ci.yml`, actions pinned by commit SHA): every push and PR runs formatting, secrets, build, types, interface, bridge, and quick tests; the full suite runs nightly. **The nightly run has been red since 21 Nov 2026** (21 and 22 Nov) because of one integration test in the Codex profile that only fails in the hosted runner's environment (`external_cli_policy.test.RELOJ Codex profile integration accepts resolved local sandbox writers`; on 22 Nov, 1 of 2547 tests; the rest pass). The test has not been excluded: from this version on it prints the sandbox identifiers before failing, to locate the cause on the hosted runner. The latest complete suite on the development machine, dated **23 Nov 2026** and run on this version's code, finished with **151/151 steps, 2565/2573 tests passed, and 8 skipped**. [Suite summary](docs/evidencia/FASE1-20261121/OP-suite-20261123.txt); the run history is in [GitHub Actions](https://github.com/ItlaStudent/DevAgents/actions).

## Known limitations

Everything below is still unresolved today; none of these lines is a verified feature:

- There are no published binaries or installer, and no publisher certificate: builds are from source and every update requires accepting "no verifiable signature."
- The graphical app is Windows-only; there is no Linux interface.
- An order with a real model on Linux is untested live; Debian 12 has not been measured.
- Best of N, real forge delivery, real account login and rotation, the new browser tools inside WebView2, and a complete update from a published release are untested live.
- Hive with an intentional audit failure and correction, governance without false alarms, and MCP from a real external IDE are pending walkthroughs.
- i18n of the CLI runtime and MCP descriptions is incomplete (the CLI help does answer in English with `DEVAGENTS_LANG=en`).
- The nightly CI suite is red because of the failure described above.
- Verification pending items and each piece's limits are in the [capability table](#evidence-and-status-of-each-piece); details of this documentation review are in the [T10 report](docs/evidencia/FASE0-20261110/T10-sol-informe.txt).

## Evidence and status of each piece

"Tested" refers to the linked, dated run on the development machine. An automated test or code review is not a live walkthrough.

| Piece | Purpose | Status and evidence |
|---|---|---|
| **Direct** (default) | Chat with one model, read and edit the project, and run tools. Does not add Orchestrated mode's audit. | Real orders are documented; this does not mean every provider was tested. [Review A1, A9 and A16](docs/evidencia/FASE0-20261110/R3-anuncio-contra-codigo-20261112.txt). |
| **Orchestrated** | Plan, distribute tasks in Git spaces, and subject delivery to another vendor's audit and deterministic checks. | Earlier walkthroughs exist and real orders delivered files to disk (CLI, 20 Nov 2026); the final current-version walkthrough with an intentional failure is pending. [Review A9 and A16](docs/evidencia/FASE0-20261110/R3-anuncio-contra-codigo-20261112.txt). |
| **Hive** | Choose several models and their roles to build and audit. | Live walkthrough on 20 Nov 2026: a real order with 4 free models from 2 vendors, file delivery verified on disk, and the semantic gate passed. An audit-failure-and-correction run is still pending. [Integral validation](docs/evidencia/FASE1-20261120/VALIDACION-INTEGRAL-20261120.txt). |
| **Best of N** | Compare solutions from several providers in separate spaces. | Built; not tested live. [Code review](docs/evidencia/FASE0-20261110/T10-sol-informe.txt). |
| **DevAgents mode** | The main agent delegates independent parts to subagents. | Evidence records two integrated subtasks; built-in delegation has one level. [Review A16–A17](docs/evidencia/FASE0-20261110/R3-anuncio-contra-codigo-20261112.txt). |
| **APIs and local models** | Register API providers and connect Ollama. | APIs used in real orders; Ollama tested live on 17 Nov 2026. [Review A7 and A12](docs/evidencia/FASE0-20261110/R3-anuncio-contra-codigo-20261112.txt). |
| **External CLIs** | Use Claude Code, Codex, Gemini CLI, or OpenCode with their configuration. | Real matrix: 9 permission combinations with Claude Code, Codex, and OpenCode; Gemini CLI lacks a verified real order. [Matrix output](docs/evidencia/FASE0-20261110/T2-matriz/matriz-1.log). |
| **Accounts and project rules** | Isolated accounts, quota rotation, and per-project rules. | Built and tested with doubles; real login and rotation not tested live. [T7 report](docs/evidencia/FASE0-20261110/T7-informe-20261113.txt). |
| **Native MCP and CLI** | `devagents-mcp.exe` over stdio; `devagents.exe` aliases `devagents-core.exe`. MCP exposes 117 tools; the CLI help answers in English with `DEVAGENTS_LANG=en`. | Protocol and tools checked through tests and a stdio client; not tested live from a real external IDE. [Surface and limits](docs/MCP-SURFACE-MAP.md), [stdio test](docs/evidencia/FASE0-20261110/QA-B-mcp-real.txt). |
| **Agent browser** | 15 tools to inspect and interact with pages. | Host and Chromium tests; the walkthrough with a real order inside WebView2 is pending. [T6 report](docs/evidencia/FASE0-20261110/T6-informe-20261113.txt). |
| **Order graph** | Tasks, audits, parallel groups, memory, and replanning using engine events. | Events and rendering tested; the T8 screenshot is synthetic. [Report](docs/evidencia/FASE0-20261110/T8-eventos-y-grafo.txt), [synthetic screenshot](docs/evidencia/FASE0-20261110/T8-grafo-sintetico.png). |
| **Package and diagnostics** | Installable package on the development machine and `doctor` command. | Installation and smoke test on the development machine; clean machine and publication pending. [T4 report](docs/evidencia/FASE0-20261110/T4-informe-20261113.txt). |
| **Updater** | Notify about releases and apply on exit, with consent. | Components tested; no live complete update. There is no publisher certificate: every update requires accepting "no verifiable signature." [T5 report](docs/evidencia/FASE0-20261110/T5-informe-20261113.txt). |
| **Forge delivery** | Prepare a branch, commit, and pull request after approval. | Built; not tested live against real services. [Code review](docs/evidencia/FASE0-20261110/T10-sol-informe.txt). |

## License, contributing and support

[Apache 2.0](LICENSE). Third-party components: [NOTICE](NOTICE). Names and logos: [TRADEMARKS.md](TRADEMARKS.md).

To contribute, see [CONTRIBUTING.md](CONTRIBUTING.md) (DCO commit sign-off) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Report vulnerabilities privately as described in [SECURITY.md](SECURITY.md).

You can provide voluntary support on **[Ko-fi](https://ko-fi.com/itlastudent)**, paying what you want (suggested: USD 5). The founder edition proposal is for the first 10,000 supporters; it unlocks no features. DevAgents is intended to remain free, without a paywall; model services may charge for usage. [Support text](docs/evidencia/FASE-X/PUB-005/textos-kofi-y-pagina-20261110.txt).
