# DevAgents

[Español](README.es.md)

**DevAgents is a free, open-source agentic development environment (ADE) in beta.** The graphical app is for 64-bit Windows 10/11; the engine, CLI, and MCP server also run on Linux. Work with one model in Direct mode or distribute an order across several models in Orchestrated and Hive modes. Capabilities and their limits are listed below with repository evidence.

> **Documentation snapshot: 20 Nov 2026.** The source code is public under Apache-2.0; there are no published binaries or installer yet: today you build from source. An installable package has been built and tested on the development machine; a clean-machine walkthrough is pending. [Package report](docs/evidencia/FASE0-20261110/T4-informe-20261113.txt).

![DevAgents — multi-agent orchestrator, local and verifiable](docs/img/devagents-portada.png)

![DevAgents app mockup](docs/img/devagents-maqueta.png)

![Orchestration diagram: one central agent distributes work across models and agents](docs/img/devagents-esquema.png)

[App screenshot](docs/img/devagents-cabina.png), taken on 10 Nov 2026 on the development machine. It shows that session, not proof of every current workflow.

The graphical interface is available in English and Spanish (chosen in Settings); the CLI help also answers in English with `DEVAGENTS_LANG=en`, although the rest of the CLI output remains in Spanish. [i18n validation](docs/evidencia/FASE1-20261120/VALIDACION-INTEGRAL-20261120.txt).

## What it does and what was checked

“Tested” refers to the linked, dated run on the development machine. An automated test or code review is not a live walkthrough.

| Piece | Purpose | Status and evidence |
|---|---|---|
| **Direct** (default) | Chat with one model, read and edit the project, and run tools. Does not add Orchestrated mode's audit. | Real orders are documented; this does not mean every provider was tested. [Review A1, A9 and A16](docs/evidencia/FASE0-20261110/R3-anuncio-contra-codigo-20261112.txt). |
| **Orchestrated** | Plan, distribute tasks in Git spaces, and subject delivery to another vendor's audit and deterministic checks. | Earlier walkthroughs exist and real orders delivered files to disk (CLI, 20 Nov 2026); the final current-version walkthrough with an intentional failure is pending. Governance detecting real failures without false alarms has not been demonstrated. [Review A9 and A16](docs/evidencia/FASE0-20261110/R3-anuncio-contra-codigo-20261112.txt), [integral validation](docs/evidencia/FASE1-20261120/VALIDACION-INTEGRAL-20261120.txt). |
| **Hive** | Choose several models and their roles to build and audit. | **Live walkthrough on 20 Nov 2026**: a real order with 4 free models from 2 vendors (OpenRouter and Cohere, no local models), file delivery verified on disk, and the semantic gate passed; the router recovered a provider failure by switching vendors. A run with an audit failure and correction is still pending. [Integral validation](docs/evidencia/FASE1-20261120/VALIDACION-INTEGRAL-20261120.txt). |
| **Best of N** | Compare solutions from several providers in separate spaces. | Built; **not tested live in this review**. No claim of superior quality. [Code review](docs/evidencia/FASE0-20261110/T10-sol-informe.txt). |
| **DevAgents mode** | The main agent delegates independent parts to subagents. | Evidence records two integrated subtasks; built-in delegation has one level, not nested subagents. [Review A16–A17](docs/evidencia/FASE0-20261110/R3-anuncio-contra-codigo-20261112.txt). |
| **APIs and local models** | Register API providers and connect Ollama. | APIs used in real orders. **Ollama tested live**: a real order with a local model that planned and wrote its artifact to disk (17 Nov 2026, B5 close-out). [Review A7 and A12](docs/evidencia/FASE0-20261110/R3-anuncio-contra-codigo-20261112.txt), [integral validation](docs/evidencia/FASE1-20261120/VALIDACION-INTEGRAL-20261120.txt). |
| **External CLIs** | Use Claude Code (Anthropic), Codex (OpenAI), Gemini CLI (Google), or OpenCode with their configuration and model access. | Real matrix: 9 permission combinations with Claude Code, Codex, and OpenCode; does not cover every version or mode. Gemini CLI still lacks a verified real order. [Matrix output](docs/evidencia/FASE0-20261110/T2-matriz/matriz-1.log). |
| **Accounts and project rules** | Isolated Codex and Claude Code accounts, quota rotation, and editable project rules. | Built and tested with doubles; real login and rotation **not tested live**. Isolated Gemini CLI and OpenCode accounts are not offered. Project rules apply across modes and CLIs; repository rules take priority. [T7 report](docs/evidencia/FASE0-20261110/T7-informe-20261113.txt). |
| **Native MCP and CLI** | `devagents-mcp.exe` over stdio; `devagents.exe` aliases `devagents-core.exe`. MCP exposes 121 tools and version negotiation, files, terminal, Git, plans, and spaces; cannot loosen governance. The CLI help also answers in English with `DEVAGENTS_LANG=en`; the rest of the CLI output remains in Spanish. | Protocol and tools checked through tests and a stdio client; **not tested live from a real external IDE**. [Surface and limits](docs/MCP-SURFACE-MAP.md), [stdio test](docs/evidencia/FASE0-20261110/QA-B-mcp-real.txt), [integral validation](docs/evidencia/FASE1-20261120/VALIDACION-INTEGRAL-20261120.txt). |
| **Agent browser** | 15 tools to inspect and interact with pages; support for starting and inspecting an app server. | Host and Chromium tests; the new tools still need a real-order walkthrough inside WebView2. **That workflow is not tested live.** [T6 report](docs/evidencia/FASE0-20261110/T6-informe-20261113.txt). |
| **Order graph** | Show tasks, audits, parallel groups, memory, and replanning using engine events. | Events and rendering tested; the T8 screenshot is synthetic. Final real-order walkthrough pending. [Report](docs/evidencia/FASE0-20261110/T8-eventos-y-grafo.txt), [synthetic screenshot](docs/evidencia/FASE0-20261110/T8-grafo-sintetico.png). |
| **Package and diagnostics** | Windows installer and `doctor` command to inspect the environment. | Installation and smoke test on the development machine; `doctor` actually executed. Clean machine and publication pending. [T4 report](docs/evidencia/FASE0-20261110/T4-informe-20261113.txt). |
| **Updater** | Notify about releases and apply on exit, with consent and no active orders. | Components tested; **a complete update from a published release has not been tested live**. There is no publisher certificate: every update currently requires accepting “no verifiable signature.” SHA-256 does not authenticate the publisher. [T5 report](docs/evidencia/FASE0-20261110/T5-informe-20261113.txt), [consent test](docs/evidencia/FASE0-20261110/T12A-M3-update-ui.txt). |
| **Forge delivery** | Prepare a branch, commit, and pull request after approval. | Built; **not tested live** against real GitHub, GitLab, or Gitea services in this review. [Code review](docs/evidencia/FASE0-20261110/T10-sol-informe.txt). |

## Install and send your first order

**There are no published binary downloads or installer today.** The following instructions are for building from source. The existing package is not a published release or a clean-machine-validated installation. [Package status](docs/evidencia/FASE0-20261110/T4-informe-20261113.txt).

Requirements: 64-bit Windows 10/11, WebView2, Git for spaces, and Zig 0.16.0 and Node.js to build. Keep at least 15 GiB free for builds and tests. These steps were checked against the launcher and build configuration; **a clean installation was not tested live in this review**. [Review details](docs/evidencia/FASE0-20261110/T10-sol-informe.txt).

1. Clone this repository and open its folder.
2. Run `DevAgents.bat`. It checks dependencies; if Zig is missing it offers a download into `toolchain\` and checks its SHA-256. If Node.js is missing it offers to install LTS through `winget`. **Installation prompts default to acceptance after 20 seconds**; use `/nodeps` to prevent automatic dependency installation. The launcher checks/builds and opens the app on every run.
3. Choose a test project folder. Under **Configuración › Proveedores** (Settings › Providers), add your provider, or configure a detected CLI under **Agentes externos** (External agents). Providers or subscriptions may have their own costs.
4. Select **Directo** (Direct) and an available model. Send a small first order: “Read this folder and describe its files without changing them.” Review the response and permission requests before asking for changes.

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

Governance in Orchestrated/Hive combines another vendor's audit, citation checks, budget, command policy, and a chained ledger. If no usable verdict is available, the order shows “unaudited” (`audit_unavailable`) and delivery is blocked. **Direct does not add that audit.** These mechanisms have code review and tests; their effectiveness without false alarms in a controlled case on the current version remains **not tested live**. [Review A9 and A16](docs/evidencia/FASE0-20261110/R3-anuncio-contra-codigo-20261112.txt), [governance guide](docs/USER-GUIDE.md).

MCP keeps permission and spending decisions in the app; its commands may require human approval. It does not have full interface parity. [MCP map](docs/MCP-SURFACE-MAP.md), [pending approvals output](docs/evidencia/FASE0-20261110/QA-B-mcp-real.txt).

## Privacy: what leaves your machine

The app stores its data in **`%LOCALAPPDATA%\DevAgents-Angel`** by default. DevAgents API keys are encrypted with Windows DPAPI; CLI credentials are managed by each CLI. These statements come from code review, not a traffic audit. [Paths and credentials review](docs/evidencia/FASE0-20261110/T10-sol-informe.txt).

**Local does not mean everything runs offline.** Depending on configuration and tools used:

- Messages, context, memory, and file content read by the agent may be sent to the model provider. **Orchestrated and Hive involve several models**: planner, executors, and auditors, potentially from different vendors.
- **Claude Code → Anthropic, Codex → OpenAI, and Gemini CLI → Google**; OpenCode uses the providers/models configured in that CLI. Each external tool has its own data and telemetry rules, which DevAgents does not control.
- **`web_search`** sends queries to Tavily or Brave Search when configured with a key; without that key it uses DuckDuckGo. **`web_fetch`** requests the specified public pages. The integrated browser loads pages opened by you or the agent.
- Model discovery and health checks contact providers; delivery, issues, webhooks, and notifications contact configured services. The updater checks GitHub Releases and can be disabled in Settings. The development launcher downloads dependencies.

[Outbound data review A15](docs/evidencia/FASE0-20261110/R3-anuncio-contra-codigo-20261112.txt), [current search, CLI, and updater review](docs/evidencia/FASE0-20261110/T10-sol-informe.txt).

No session upload to a DevAgents-owned server was found in the reviewed code. This **does not certify the absence of network traffic** or establish the behavior of WebView2 or third-party CLIs. [Review A13–A15](docs/evidencia/FASE0-20261110/R3-anuncio-contra-codigo-20261112.txt).

## Tests and CI

The latest recorded complete suite on `main`, dated **15 Nov 2026**, finished with **151/151 steps, 2512/2518 tests passed, and 6 skipped** (POSIX tests on Windows). It ran on the development machine; it is not a run from this documentation review or proof of every live workflow. [Full output](docs/evidencia/FASE0-20261110/T12A-suite-completa-sobre-main-20261115.txt).

A Windows CI workflow exists: PR/push checks formatting, secrets, build, types, interface, bridge, and quick tests; the full suite runs nightly. Automatic jobs will start running once the repository is published; manual dispatch is supported. Commands were checked locally, **with no evidenced hosted CI run**. Actions remain pinned to major versions; SHA pinning is pending. [CI report](docs/evidencia/FASE0-20261110/T11-T4-informe.txt).

## Not done yet

- Publish binaries, installer, and downloadable releases; obtain a publisher certificate and complete a clean-machine walkthrough.
- Walk through MCP from an external IDE, real account login and rotation, new browser tools, and a complete update.
- Walk through Hive with an intentional audit failure and correction; demonstrate governance without false alarms; real forge delivery.
- An order with a real model on Linux and a Debian 12 measurement; full i18n of the CLI runtime and MCP descriptions.
- Run hosted CI after publication and complete the independent review of the final version.

These limits are not verified features. Documentation scope and consulted outstanding work are detailed in the [report for this review](docs/evidencia/FASE0-20261110/T10-sol-informe.txt).

## License, contributing and support

[Apache 2.0](LICENSE). Third-party components: [NOTICE](NOTICE). Names and logos: [TRADEMARKS.md](TRADEMARKS.md).

To contribute, see [CONTRIBUTING.md](CONTRIBUTING.md) (DCO commit sign-off) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Report vulnerabilities privately as described in [SECURITY.md](SECURITY.md).

You can provide voluntary support on **[Ko-fi](https://ko-fi.com/itlastudent)**, paying what you want (suggested: USD 5). The founder edition proposal is for the first 10,000 supporters; it unlocks no features. DevAgents is intended to remain free, without a paywall; model services may charge for usage. [Support text](docs/evidencia/FASE-X/PUB-005/textos-kofi-y-pagina-20261110.txt).
