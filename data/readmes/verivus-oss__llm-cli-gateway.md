# llm-cli-gateway

[![CI](https://github.com/verivus-oss/llm-cli-gateway/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/verivus-oss/llm-cli-gateway/actions/workflows/ci.yml)
[![Security](https://github.com/verivus-oss/llm-cli-gateway/actions/workflows/security.yml/badge.svg?branch=main)](https://github.com/verivus-oss/llm-cli-gateway/actions/workflows/security.yml)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/verivus-oss/llm-cli-gateway/badge)](https://scorecard.dev/viewer/?uri=github.com/verivus-oss/llm-cli-gateway)
[![npm](https://img.shields.io/npm/v/llm-cli-gateway.svg)](https://www.npmjs.com/package/llm-cli-gateway)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> _"Without consultation, plans are frustrated, but with many counselors they succeed."_
> — Proverbs 15:22 (LSB)

**Secure local control plane for AI coding agents.**

`llm-cli-gateway` lets supported MCP clients operate Claude Code, Codex, Gemini/Antigravity, Grok Build, Mistral Vibe, Cognition Devin, Cursor Agent, and configured HTTP API providers through one user-owned gateway while preserving native CLI sessions, local credentials, durable async jobs, validation receipts, and review workflows.

**Why developers try it:** use the client you are already in to delegate work to local coding agents, scope remote execution to registered workspaces, gate risky actions, survive disconnects, and collect auditable review evidence without turning those agents into a generic chat proxy.

**Current signals:** CI and security workflows pass on `main`, OpenSSF Scorecard is published, OpenSSF Best Practices is passing, releases use Sigstore signing, and the package is MIT licensed.

## Quick Start

```bash
npm install -g llm-cli-gateway
```

Or use directly with `npx` from an MCP client:

```json
{
  "mcpServers": {
    "llm-gateway": {
      "command": "npx",
      "args": ["-y", "llm-cli-gateway"]
    }
  }
}
```

## What It Provides Today

`llm-cli-gateway` is a single-user MCP control plane for operating AI coding agents from supported local or remote clients. It is more than a thin CLI wrapper:

- Runs registered provider CLIs and configured HTTP API providers through consistent sync and async MCP tools.
- Persists long-running jobs, supports restart-safe result collection, deduplication, cancellation, and sync-to-async deferral.
- Tracks sessions, real CLI resume paths, structured response metadata, and cache telemetry.
- Supports cache-aware `promptParts`, including explicit Claude `cache_control` when opted in.
- Can run supported provider requests inside gateway-managed git worktrees for isolated multi-agent review and implementation loops with either the local file-backed or PostgreSQL session manager. Session-bound reuse and cleanup remain limited to the host that owns the filesystem artifact, even when PostgreSQL shares the session row across hosts. After session deletion, `session_clear_all`, or file-backed TTL eviction, both session managers retain a failed cleanup for retry by the host that owns the worktree. Deletion processed from another host removes no worktree and leaves that record intact. The database-side `cleanup_expired_sessions` function stages the same record instead of deleting a worktree-bearing session; it invokes no gateway observer and so attempts no removal itself. Grok, Devin, and Mistral require an explicit provider-native `sessionId` for a gateway worktree; fresh, `createNewSession`, and `resumeLatest`-only worktree requests fail closed because they cannot durably reselect it. Materialization suppresses repository, system, and global Git hooks, configured clean, smudge, and process checkout filters, sparse checkout, and lazy object fetching. Filter-dependent content such as Git LFS remains in its repository representation instead of executing host commands.
- Ships personal-appliance setup surfaces: HTTP transport with bearer-token auth, `doctor --json`, setup UI artifacts, provider setup snippets, Docker fallback, and checked release bundles.
- Remote web connectors use MCP OAuth discovery and authorization-code setup with static client or shared-secret gates. Client secrets are generated locally, stored only as hashes, and printed only by explicit copy-once commands.
- Provider CLI requests can select registered workspaces by alias via `workspace`; every HTTP/tunnel request must use a registered alias, session workspace, or `[workspaces].default` before provider execution. Local unrestricted filesystem access is the stdio transport.

## Workflow Assets

The repo ships agent-ready workflow skills under [`.agents/skills`](.agents/skills) for async orchestration, session continuity, multi-LLM review, implement-review-fix loops, retrospective evidence walks, secure approval-gated dispatch, and Personal Agent Config Kit operations. Nine caller-facing skills are bundled in the published npm package: `async-job-orchestration`, `multi-llm-review`, `session-workflow`, `secure-orchestration`, `implement-review-fix`, `retrospective-walk`, `public-demo-session`, `least-cost-routing`, and `personal-agent-config-kit`. Machine-readable DAG-TOML plans live under [`docs/plans`](docs/plans) and [`setup/install-plan.dag.toml`](setup/install-plan.dag.toml) for workflows that need deterministic sequencing and verification gates.

Skill packs can be updated outside the core npm release by placing skill
directories in local, operator-controlled paths. The gateway loads bundled
skills first, then `[skills].paths`, then `LLM_GATEWAY_SKILLS_PATH`, then
`~/.llm-cli-gateway/skills` when it exists; later roots override earlier skills
by name. Each skill is a directory containing `SKILL.md`. A root may also carry
`skill-pack.json` to pin expected `SKILL.md` hashes:

```toml
[skills]
paths = ["/opt/llm-cli-gateway/skills"]
```

```bash
export LLM_GATEWAY_SKILLS_PATH="/opt/team-skill-pack:/opt/incident-skill-pack"
```

```json
{
  "name": "team-pack",
  "version": "1.0.0",
  "skills": [
    {
      "name": "incident-retrospective",
      "sha256": "<sha256 of incident-retrospective/SKILL.md>"
    }
  ]
}
```

The loader is intentionally local-only: it never fetches remote Markdown at
startup. To update a pack, install or replace files through your package manager
or deployment system, then restart the gateway so the advertised `skills://...`
resources refresh.

The next documentation focus is provider-specific skill and DAG-TOML pairs for each outbound CLI and API-provider family: Claude, Codex, Gemini/Antigravity, Grok, Mistral Vibe, Devin, Cursor Agent, OpenAI-compatible endpoints, Anthropic Messages, and xAI Responses. The implementation plan is tracked in [`docs/plans/provider-workflow-assets.dag.toml`](docs/plans/provider-workflow-assets.dag.toml), with each provider asset expected to cover install/login checks or token-env checks, session behavior, approval modes, cache/telemetry surfaces, failure modes, and a smoke-test gate.

## Trust & Supply Chain

[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/13025/badge)](https://www.bestpractices.dev/projects/13025)
[![Releases: Sigstore signed](https://img.shields.io/badge/releases-Sigstore%20signed-2e7d32.svg)](SECURITY.md#release-signing)

- CI runs build, lint, format, tests, package checks, and npm audit.
- Security CI runs actionlint, zizmor, shellcheck, typos, osv-scanner, gitleaks, and lychee.
- GitHub release installer artifacts are checksummed and signed with Sigstore keyless signing.
- npm releases use a generated prod-only shrinkwrap and release security audit; GitHub Actions Trusted Publishing exchanges the job's OIDC identity for short-lived npm publish credentials.
- The npm package intentionally ships a generated, prod-only `npm-shrinkwrap.json` so registry installs resolve the audited release tree. Release gates regenerate it from `package-lock.json`, compare for parity, and run a registry-fidelity consumer install before publishing.
- Socket behavioural alerts are documented in [`socket.yml`](./socket.yml) and under "Security Considerations" below. `shellAccess` and `shrinkwrap` are reviewed package capabilities/configuration for this CLI appliance, not hidden install behaviour.

## Personal MCP Appliance

The personal-appliance contract keeps that surface intentionally narrow: one trusted user runs the gateway on a machine or volume they own, connects one MCP endpoint, and lets supported clients operate local coding agents through workspace-scoped, approval-gated, auditable requests.

The product contract is documented in [docs/personal-mcp/PRODUCT_CONTRACT.md](docs/personal-mcp/PRODUCT_CONTRACT.md). It defines the single-user scope, security posture, target support matrix, and provider-support verification gates. Public setup guides must not claim ChatGPT, Claude web, Claude Desktop, Codex, Gemini CLI, Gemini web, or Grok inbound support until the corresponding provider/client path has been verified.

This project does not provide hosted multi-tenant credential custody. Provider credentials stay on the user's machine or user-owned deployment volume.

For a single developer who works on several workstations and repositories, the [Personal Agent Config Kit guide](docs/guides/PERSONAL_AGENT_CONFIG_KIT.md) explains the Git-synchronised personal baseline, repository overlays, immutable context stamps, and workstation-safe provider continuity model. The baseline directory is confined to a non-symlinked descendant of the local home directory, and every publish or sync revalidates its configured `origin` fetch and push URLs against the HTTPS/SSH-only policy. The Kit is intentionally local-caller-only; Kit provider execution and recovery of an unadmitted attempt require healthy durable SQLite or PostgreSQL async-job admission. Kit mode supports Claude, Codex, and Mistral; every other provider fails closed while it is enabled. Kit scope never inherits the gateway process cwd: Claude and Mistral require a registered workspace selection or configured default, while Codex can also use an explicit absolute `workingDir`. Relative Kit `workingDir` values are rejected before filesystem or Git inspection. It disables cross-model validation tools while enabled and is not an HTTP/OAuth configuration or remote execution feature.

For a retention-pinned non-Kit Claude MCP request configuration, follow the local-only [same-host recovery procedure](docs/guides/PERSONAL_AGENT_CONFIG_KIT.md#same-host-mcp-cleanup-pin-recovery). It accepts no SQL or arbitrary-path override. A valid recovery invocation emits JSON and exits 0 after success or 2 for a safe refusal; invalid usage or unavailable durable storage exits 1.

Release-readiness history is tracked in [docs/personal-mcp/RELEASE_READINESS.md](docs/personal-mcp/RELEASE_READINESS.md). Dogfooding evidence (which target LLMs guided setup, what unsafe suggestions were captured, and which findings were deferred from the initial personal-appliance rollout) is in [docs/personal-mcp/DOGFOODING_RESULTS.md](docs/personal-mcp/DOGFOODING_RESULTS.md).

Current personal-appliance artifacts include:

- Streamable HTTP startup: `LLM_GATEWAY_AUTH_TOKEN=<token> npm run start:http`
- Machine-readable diagnostics: `npm run doctor`
- Go bootstrapper: `installer/` with `setup`, `doctor --json`, `start`, `stop`, `status`, `repair`, `upgrade`, `uninstall`, `print-client-config`, and verified bundle download commands.
- Release packaging: on the public mirror, the release workflow builds Linux binaries on GitHub-hosted `ubuntu-latest` and builds Windows/macOS binaries on their GitHub-hosted platform runners. The private upstream uses its internal self-hosted Linux runner. Each release publishes checksummed platform bundles with the gateway, production dependencies, and a managed Node runtime; see [installer/packaging/README.md](installer/packaging/README.md).
- Docker Compose fallback: [docker/personal.compose.yml](docker/personal.compose.yml) + [docker/Dockerfile.personal](docker/Dockerfile.personal) for users who already manage containers.
- Local setup UI artifact: [setup/ui/index.html](setup/ui/index.html)
- Provider setup snippets: [setup/providers/](setup/providers/)
- Cross-validation tools: `review_changes`, `validate_with_models`, `second_opinion`, `compare_answers`, `red_team_review`, `consensus_check`, `ask_model`, `synthesize_validation`, `job_status`, `job_result`, and `validation_receipt` (plus the `validation-receipt://{validationId}` resource). `review_changes` and durable receipts require a SQLite or PostgreSQL validation-run store and are absent in Personal Agent Config Kit mode.

### Install / Upgrade / Uninstall (single binary)

Windows PowerShell:

```powershell
$Version = '<version>'
$Base = "https://github.com/verivus-oss/llm-cli-gateway/releases/download/v$Version"
$InstallDir = Join-Path (Join-Path $env:LOCALAPPDATA 'Programs') 'llm-cli-gateway'
$ExeName = "llm-cli-gateway-$Version-windows-amd64.exe"
$BundleName = "llm-cli-gateway-bundle-$Version-windows-amd64.tar.gz"
$Exe = Join-Path $InstallDir 'llm-cli-gateway.exe'
$Checksums = Join-Path $InstallDir 'SHA256SUMS'
$ChecksumBundle = Join-Path $InstallDir 'SHA256SUMS.sigstore.json'
New-Item -ItemType Directory -Force $InstallDir | Out-Null
Invoke-WebRequest -UseBasicParsing "$Base/$ExeName" -OutFile $Exe
Invoke-WebRequest -UseBasicParsing "$Base/SHA256SUMS" -OutFile $Checksums
Invoke-WebRequest -UseBasicParsing "$Base/SHA256SUMS.sigstore.json" -OutFile $ChecksumBundle
cosign verify-blob $Checksums --bundle $ChecksumBundle --certificate-identity "https://github.com/verivus-oss/llm-cli-gateway/.github/workflows/release-installer.yml@refs/tags/v$Version" --certificate-oidc-issuer "https://token.actions.githubusercontent.com"
if ($LASTEXITCODE -ne 0) { throw "Sigstore verification failed for SHA256SUMS" }
function Get-ReleaseSha256($Name) {
  $line = Select-String -Path $Checksums -Pattern "^[a-fA-F0-9]{64}\s+$([regex]::Escape($Name))$" | Select-Object -First 1
  if (-not $line) { throw "No SHA256SUMS entry found for $Name" }
  return (($line.Line -split "\s+")[0]).ToLowerInvariant()
}
if ((Get-FileHash $Exe -Algorithm SHA256).Hash.ToLowerInvariant() -ne (Get-ReleaseSha256 $ExeName)) { throw "Checksum mismatch for $ExeName" }
$env:RVWR_GATEWAY_BUNDLE_URL = "$Base/$BundleName"
$env:RVWR_GATEWAY_BUNDLE_SHA256 = Get-ReleaseSha256 $BundleName
& $Exe setup
& $Exe stop
& $Exe install-bundle
& $Exe start
& $Exe status
& $Exe doctor
```

The Windows installer keeps a stable `llm-cli-gateway.exe` command in
`%LOCALAPPDATA%\Programs\llm-cli-gateway` and adds that directory to the user
PATH. Do not script against release-versioned exe names after install.

```bash
# After downloading the binary that matches your OS/arch from a release:
cosign verify-blob SHA256SUMS --bundle SHA256SUMS.sigstore.json \
  --certificate-identity "https://github.com/verivus-oss/llm-cli-gateway/.github/workflows/release-installer.yml@refs/tags/v<version>" \
  --certificate-oidc-issuer "https://token.actions.githubusercontent.com"
sha256sum --check SHA256SUMS            # verify before run (or `shasum -a 256 --check` on macOS)
chmod +x llm-cli-gateway-<ver>-<os>-<arch>
./llm-cli-gateway-<ver>-<os>-<arch> setup
./llm-cli-gateway-<ver>-<os>-<arch> install-bundle    # uses the platform bundle URL/SHA256
./llm-cli-gateway-<ver>-<os>-<arch> start
./llm-cli-gateway-<ver>-<os>-<arch> doctor

# Upgrade: replace the binary, set the new bundle env vars, run upgrade.
./llm-cli-gateway-<new>-<os>-<arch> upgrade

# Uninstall: dry-run first, then run with --yes.
./llm-cli-gateway-<ver>-<os>-<arch> uninstall
./llm-cli-gateway-<ver>-<os>-<arch> uninstall --yes
```

Docker fallback:

```bash
LLM_GATEWAY_AUTH_TOKEN=$(openssl rand -hex 32) \
  docker compose -f docker/personal.compose.yml up -d
docker compose -f docker/personal.compose.yml run --rm doctor
```

## Features

### Core Capabilities

- **Multi-LLM Orchestration**: Unified interface for Claude Code, Codex, Gemini, Grok, Mistral (Vibe), Devin, and Cursor Agent CLIs
- **Session Management**: Track gateway session metadata and provider-specific continuity with persistent storage
- **Gateway-owned worktrees**: Run supported sync or async provider requests inside a managed git worktree with either the local file-backed or PostgreSQL session manager. Same-session reuse requires same-host durable ownership plus a matching live Git registration and gateway branch; manager-level named path collisions fail closed. A shared PostgreSQL session row does not transfer ownership of its filesystem-local worktree to another host. Grok, Devin, and Mistral require an explicit provider-native `sessionId`; fresh, `createNewSession`, and `resumeLatest`-only worktree requests fail closed. A worktree requires a registered workspace selected explicitly, through caller-owned session metadata, or by the configured default; it never inherits process cwd or combines with `workingDir`, `addDir`, or `includeDirs`. Materialization suppresses repository, system, and global Git hooks, configured clean, smudge, and process checkout filters, sparse checkout, and lazy object fetching. Filter-dependent content such as Git LFS remains in its repository representation instead of executing host commands. Session deletion, `session_clear_all`, and file-backed TTL eviction hide a durably owned worktree session while cleanup runs, under either session manager. If Git removal fails, the manager retains a durable cleanup-pending tombstone, blocks reuse, and retries cleanup when a manager is registered on the owning host. The record is finalized only once Git no longer registers the worktree, read back rather than inferred from the recorded path being absent: a worktree that was moved, or whose owner marker cannot be read, is not a removal. Deletion processed by a different host removes no worktree and leaves the owning host's record intact. The database-side `cleanup_expired_sessions` function stages the same tombstone instead of deleting a worktree-bearing session; it invokes no gateway observer and so attempts no removal itself. A tombstone is not bounded by retention.
- **Token Optimization**: opt-in prompt/response compaction via `optimizePrompt` / `optimizeResponse`, both defaulting to **false**. The 44% / 37% figures are v1.0.0 measurements on a specific corpus, not a guarantee: `src/optimizer.ts` is a deterministic phrase-stripper, and nothing measures a ratio at runtime.
- **Correlation ID Tracking**: Full request tracing across all LLM interactions
- **Cross-Tool Collaboration**: LLMs can use each other via MCP (validated through dogfooding)

### Observability

- **Durable Flight Recorder**: Provider requests and responses follow `[persistence].backend`: SQLite writes to `~/.llm-cli-gateway/logs.db` by default, while PostgreSQL writes them to the configured database with the other durable subsystems. A PostgreSQL failure leaves the recorder unavailable or degraded and is reported generically on health surfaces; it never falls back to SQLite. Existing rows are not migrated or dual-read when the backend changes. Records include correlation IDs, duration, and token usage where the provider emits it (today: claude on `stream-json`/`json`, codex, and the API providers; grok, gemini, mistral, devin and cursor emit no usage on their CLI wire). Two exclusions are worth knowing: **cross-LLM validation seats write no flight-recorder row at all**, so `llm_request_result` cannot read one back by correlation ID, and repository-review seats are additionally excluded by design so review evidence is not retained in a non-expiring table. The `retry_count` and `circuit_breaker_state` columns are constants on the async path, which is the production path; retry and circuit breaking apply only to the direct-execute fallback. Read history through `llm_request_list` and `llm_request_result` so per-principal ownership checks remain in force. For human browsing of a SQLite deployment: `datasette ~/.llm-cli-gateway/logs.db`
- **Structured Metadata**: Tool responses include machine-readable `structuredContent` (model, cli, correlationId, sessionId, durationMs, token counts)
- **Cache observability resources**: `cache-state://global`, `cache-state://session/{id}`, and `cache-state://prefix/{hash}` MCP resources return aggregate cache hit/miss/savings — tokens and hashes only, no prompt text. `session_get` includes a `cacheState` block when the session has prior requests.
- **Provider capability inventory**: `provider_tool_capabilities` and `provider-tools://catalog` expose the gateway request fields, supported/degraded provider controls, local skill/tool discovery, and safe config-surface hints for Claude Code, Codex CLI, Gemini/Antigravity, Grok CLI/API, Mistral Vibe, Cognition Devin, and Cursor Agent. `doctor --json` includes a compact `provider_capabilities` summary for setup assistants.

### Cache-aware operation

Every `*_request` and `*_request_async` tool except `devin_request` / `devin_request_async` and `cursor_request` / `cursor_request_async` accepts an optional `promptParts` field that structures the prompt for better cache hit rates (the Devin and Cursor headless paths take a plain `prompt` only). The gateway concatenates the parts in canonical order (`system → tools → context → task`) so that the stable prefix bytes precede the volatile task tail unchanged across calls, letting each provider's automatic prompt-caching land on the same content hash each time.

```json
{
  "promptParts": {
    "system": "You are a helpful code reviewer.",
    "tools": "You have access to Read, Grep, Bash.",
    "context": "<long stable context block — file dumps, etc.>",
    "task": "Review the changes in src/foo.ts for security issues."
  }
}
```

`prompt` and `promptParts` are mutually exclusive — pass exactly one.

Per-CLI capability matrix (prefix discipline is automatic via `promptParts` for all providers except Devin and Cursor, which have no `promptParts` surface; explicit levers are provider-specific):

| CLI     | Prefix discipline | Explicit lever(s)                                                                                                                      |
| ------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| claude  | yes               | `promptParts.cacheControl` + `outputFormat: "stream-json"` (Anthropic `cache_control` breakpoints on stable blocks; `ttl="1h"` forced) |
| codex   | yes               | none (OpenAI implicit)                                                                                                                 |
| gemini  | yes               | none (implicit server-side)                                                                                                            |
| grok    | yes               | `compactionMode` / `compactionDetail` (context compaction: `summary                                                                    | transcript | segments`; `segments` writes per-segment markdown) |
| mistral | yes               | none (implicit)                                                                                                                        |
| devin   | no                | plain `prompt` only                                                                                                                    |
| cursor  | no                | plain `prompt` only                                                                                                                    |

**Claude example (explicit cacheControl)**

```ts
claude_request({
  promptParts: {
    system: "You are a helpful code reviewer.",
    context: "<long stable file dump>",
    task: "Review the diff.",
    cacheControl: { system: true, context: true }, // task is never marked
  },
  outputFormat: "stream-json",
});
```

Gateway emits the `stream-json` stdin path with `cache_control: {type:"ephemeral", ttl:"1h"}` on marked blocks only.

**Grok example (compaction)**

```ts
grok_request({
  promptParts: { system: "...", context: "...", task: "..." },
  compactionMode: "segments",
  compactionDetail: "balanced",
});
```

Emits `--compaction-mode segments --compaction-detail balanced`.

See `docs/personal-mcp/PROVIDER_CACHE_SURFACES.md` for full surfaces, telemetry differences (e.g. Grok `-p` vs ACP), exact stream-json payload shapes, and cross-LLM review notes.

Opt-in flags (all default off) live under `[cache_awareness]` in `~/.llm-cli-gateway/config.toml`.

### Reliability & Performance

- **Retry Logic**: Exponential backoff with circuit breaker for transient failures
- **Atomic File Writes**: Process-specific temp files with fsync for data integrity
- **Host-protection backpressure**: bounded HTTP session lifecycle (max sessions + idle reaper), global and per-provider job-execution limits with a bounded FIFO queue, and a configurable per-job output cap (default 50MB). See [Host-protection limits](#host-protection-limits-http-and-limits).
- **NVM Path Caching**: Eliminates I/O overhead on every request
- **Long-Running Jobs**: Non-time-bound async execution via `*_request_async` + polling tools

### Security & Quality

- **Comprehensive Testing**: 1,700+ tests covering unit, integration, and regression scenarios with real CLI execution
- **Input Validation**: Zod schemas prevent injection attacks
- **No Secret Leakage**: Generic session descriptions only (file permissions 0o600)
- **No ReDoS**: Bounded regex patterns prevent catastrophic backtracking
- **Type Safety**: Strict TypeScript with comprehensive error handling
- **Supply-chain hardening**: a dedicated `.github/workflows/security.yml` runs actionlint, zizmor, shellcheck, typos, osv-scanner, gitleaks, and lychee on every push and PR (see `SECURITY.md` for the threat model)

## Provider capability surface

Every provider is reachable through the same request, session, job, and validation machinery, but the underlying CLIs differ in what they natively expose. The table records what actually shipped per provider; discover the live surface at runtime with `provider_tool_capabilities`, `list_models`, and the `provider-acp://<provider>` / `provider-tools://<provider>` resources.

| Provider                               | CLI request tools                                                                     | Native ACP                                                                             | Live model discovery                                                     | Admin surface                                              |
| -------------------------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------- |
| Claude Code (`claude`)                 | `claude_request` / `_async`                                                           | None (CLI-first; no ACP entrypoint at its tracked version)                             | model aliases, reasoning-effort levels, fallback model                   | read-only via `provider_admin_list` / `provider_admin_run` |
| OpenAI Codex (`codex`)                 | `codex_request` / `_async`, `codex_fork_session`                                      | None (codex-cli advertises mcp-server / app-server transports, not native ACP)         | `codex debug models`                                                     | read-only via `provider_admin_list` / `provider_admin_run` |
| Gemini / Antigravity (`gemini`, `agy`) | `gemini_request` / `_async`                                                           | None (agy exposes no ACP entrypoint; legacy Gemini CLI ACP evidence does not transfer) | `agy models`                                                             | read-only via `provider_admin_list` / `provider_admin_run` |
| xAI Grok (`grok`)                      | `grok_request` (sync `transport: "acp"`) / `_async`                                   | Native via `grok agent stdio`                                                          | `grok models` + `~/.grok/config.toml`                                    | read-only via `provider_admin_list` / `provider_admin_run` |
| Mistral Vibe (`mistral`)               | `mistral_request` (sync `transport: "acp"`) / `_async`                                | Native via `vibe-acp`                                                                  | Vibe config plus the `VIBE_ACTIVE_MODEL` active model and agent profiles | read-only via `provider_admin_list` / `provider_admin_run` |
| Cognition Devin (`devin`)              | `devin_request` (sync `transport: "acp"`, `agentType: summarizer\|review`) / `_async` | Native via `devin acp`                                                                 | `--model` / `DEVIN_MODEL`                                                | read-only via `provider_admin_list` / `provider_admin_run` |
| Cursor Agent (`cursor`)                | `cursor_request` (sync `transport: "acp"`) / `_async`                                 | Native via `cursor-agent acp` (companion-owned)                                        | model aliases                                                            | read-only via `provider_admin_list` / `provider_admin_run` |

- **Native ACP** is reported honestly. `grok`, `mistral`, `devin`, and `cursor` expose a native ACP entrypoint, so `provider-acp://<provider>` carries the negotiated `initialize` capability set and the derived session-method availability, and the sync `*_request` accepts `transport: "acp"` (fails closed unless `[acp]` and the provider's `runtime_enabled` gate are set). ACP routing is sync-only: the `*_request_async` variants always run the CLI transport and do not accept `transport: "acp"` (nor Devin's `agentType`); async ACP parity is a later phase. ACP workspace selection is gateway-owned: an explicit ACP `workspace` must be a registered alias. A fresh remote ACP request uses that alias or `[workspaces].default`; a remote resume is fixed to its recorded canonical alias and cwd, and a different or unbound workspace is rejected. Local ACP may omit `workspace`; each unscoped process then gets a fresh private `0o700` neutral directory that is removed after the process exits, never a shared predictable temp path. `claude`, `codex`, and `gemini` have no native ACP entrypoint at their target CLI versions; their `provider-acp://` records report `native: false` with no methods and no adapter-as-native masquerade, and they expose no `transport: "acp"` selector.
- **Managed approval is Claude-only today.** `approvalStrategy:"mcp_managed"` is executable only by the Claude CLI adapter, which launches Claude with a request-scoped generated MCP configuration and `--strict-mcp-config`. It permits only provisioned, gateway-owned MCP definitions and rejects dynamic `npx`, ambient-PATH, and Codex-config overrides. Codex, Gemini, Grok, Mistral, Devin, and Cursor reject `mcp_managed` before launching a provider because their current adapters cannot isolate ambient MCP configuration. For those adapters, use `approvalStrategy:"legacy"`; `approvalPolicy` has no effect.
- **ACP has its own permission bridge.** `approvalStrategy:"mcp_managed"` and any `approvalPolicy` are rejected when `transport:"acp"` is selected. Use the Claude CLI transport for managed approval. ACP host services fail closed, gated by the tool-call category the agent declares: `write` is denied unless `allow_write_host_services` is set, `execute` unless `allow_terminal_host_services` is set, and **any other category is denied outright**, including `fetch` and every unrecognised kind, so a new upstream tool kind cannot be auto-approved by default. Approval is expressed only by selecting an agent-offered single-use allow option; an agent that offers only a persistent `allow_always` grant is denied, so ACP never maps a raw CLI bypass input to a standing permission grant. Note the boundary is this category gate: it constrains what the agent may ask the **gateway** to do, not what the agent does in its own process.
- **Resources** are generated from the provider registry for every CLI provider: `models://<provider>`, `sessions://<provider>`, `provider-acp://<provider>`, `provider-tools://<provider>`, and `provider-subcommands://<provider>`.
- **Model discovery** is live and account-aware: the discovery listed above reaches `models://<provider>` and `list_models`, degrading to static registry facts when a live probe is unavailable (a resource read never spawns a CLI).
- **Admin surfaces** are discovery-driven and output-redacted. `provider_admin_list` and `provider_admin_run` are read-only for every provider. State-mutating admin operations are exposed only through `provider_admin_mutate`, gated behind `[admin] allow_mutating_cli_admin_ops`, the remote `cli:admin` scope, an approval gate, and an audit record. Mutating ACP session operations are likewise gated behind `[acp] allow_mutating_session_ops`.
- **Validation** commands work across every provider: `review_changes`, `validate_with_models`, `second_opinion`, `compare_answers`, `red_team_review`, `consensus_check`, `ask_model`, and `synthesize_validation`, with canonically hashed immutable receipts via `validation_receipt` and the `validation-receipt://{validationId}` resource. `review_changes` captures a complete, hashed Git artifact and starts repository-bound read-only reviewers.

## Prerequisites

**Node.js >= 24.4.0** is required (`engines.node` in `package.json`). The SQLite backend uses Node's built-in `node:sqlite` module, so there is no native binding to compile and no install scripts run. The 24.4 floor is where `allowBareNamedParameters` defaults to `true`, which the SQLite persistence layer relies on.

Running the source-tree release audit also requires Bash and `flock` from
util-linux. This prerequisite was verified against commit
`242e7669565ecc7c71183f5f7133791a1384ca7c`. Release automation runs the audit
on Ubuntu. On macOS, install a compatible `flock` before running
`npm run security:audit` or the full `npm run check` gate.

Before using this gateway, you need to install the CLI tools you want to use:

### Claude Code CLI

```bash
# Installation instructions for Claude Code
# Visit: https://docs.anthropic.com/claude-code
npm install -g @anthropic-ai/claude-code
```

### Codex CLI

```bash
npm install -g @openai/codex
codex login
```

### Gemini (Google Antigravity CLI)

The Gemini provider runs through Google Antigravity CLI (`agy`).

```bash
curl -fsSL https://antigravity.google/cli/install.sh | bash
# Docs: https://antigravity.google/docs
```

### Grok Build CLI (xAI)

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
grok login   # OAuth flow; for headless auth, set XAI_API_KEY
# Docs: https://docs.x.ai/build/overview
```

### Mistral Vibe CLI

```bash
# Pick one — the gateway's cli_upgrade auto-detects which one you used.
curl -LsSf https://mistral.ai/vibe/install.sh | bash
pip install mistral-vibe
uv tool install mistral-vibe
brew install mistral-vibe

vibe --setup
# Complete the API-key setup locally. Do not paste the key into a chat.
# Current Vibe defaults session logging to enabled. If an older config disabled it,
# edit ~/.vibe/config.toml and set:
# [session_logging]
# enabled = true
```

Vibe-specific notes:

- **Model selection is via the `VIBE_ACTIVE_MODEL` environment variable** —
  Vibe has no `--model` flag. The gateway discovers `~/.vibe/config.toml` /
  `VIBE_MODELS`, injects `VIBE_ACTIVE_MODEL` only when a model is explicitly
  requested or Vibe config needs recovery, and retries once after a
  model-not-found failure with refreshed discovery.
- **`permissionMode` is the Vibe `--agent` name.** Builtins are
  `default | plan | accept-edits | auto-approve`; Vibe also accepts install-gated
  builtins (e.g. `lean`) and custom agents from `~/.vibe/agents`. Requests pass
  the selected name through for Vibe to validate. `mcp_managed` is not available
  for Vibe.
- **Tool controls use Vibe's native flags.** The gateway emits one
  `--enabled-tools <tool>` flag per `allowedTools` entry and one
  `--disabled-tools <tool>` flag per `disallowedTools` entry. Vibe applies
  disabled tools after enabled-tool filtering.
- **Usage telemetry is best-effort.** Vibe does not emit token or cost data in
  programmatic stdout. When the gateway knows Vibe's native session UUID, it
  reads `~/.vibe/logs/session/session_<...>/meta.json` for usage and cost.
  A missing, malformed, or not-yet-known session log leaves those fields empty.
- **No self-update**: `cli_upgrade --cli mistral` detects whether you used
  pip / uv / brew and dispatches the matching upgrade command. Running
  `vibe update` is not a thing.

## Installation

### As an MCP server (npm)

```bash
npm install -g llm-cli-gateway
```

Or use directly with `npx`:

```json
{
  "mcpServers": {
    "llm-gateway": {
      "command": "npx",
      "args": ["-y", "llm-cli-gateway"]
    }
  }
}
```

### From source

```bash
git clone https://github.com/verivus-oss/llm-cli-gateway.git
cd llm-cli-gateway
npm install
npm run build
```

## Usage

### As an MCP Server

For clients that already support local stdio MCP servers, add a configuration like:

```json
{
  "mcpServers": {
    "llm-cli-gateway": {
      "command": "node",
      "args": ["/path/to/llm-cli-gateway/dist/index.js"]
    }
  }
}
```

Stdio is the recommended path for unrestricted machine-local development access. HTTP MCP, including localhost HTTP and tunneled HTTPS, is treated as remote-capable for provider execution: provider tools must resolve a registered workspace alias, a session workspace, or `[workspaces].default` before spawning a CLI. Remote clients should pass relative `workingDir`, `addDir`, and include-directory values inside the selected workspace, and may resume only gateway-tracked sessions they own. Raw native provider session IDs are local-only. Disabling auth or using a no-auth connector path is not a filesystem bypass.

For a local CLI request with no resolved `workingDir`, registered `workspace`,
or gateway-managed `worktree`, the child runs in a fresh private `0o700`
temporary directory that is removed after the process exits. It never inherits
the gateway repository cwd or its provider-native instruction context. The
gateway canonicalizes the temp root and rejects or relocates it when any
ancestor contains `.git`, `AGENTS.md`, `AGENTS.override.md`, `Agents.md`,
`AGENT.md`, `CLAUDE.md`, `Claude.md`, `CLAUDE.local.md`,
`.claude/CLAUDE.md`, `.claude/rules/`, `.cursor/rules/`, `.cursorrules`,
`GEMINI.md`, or `.vibe/config.toml`, including through a symlinked or custom
`TMPDIR` beneath that context. The list covers entries a provider discovers by
walking up from its cwd. User-scope configuration such as
`~/.claude/settings.json` is deliberately absent: it loads on every invocation
regardless of cwd, so relocating the workspace would not isolate it.
Provider-native `resumeLatest` operations that use a cwd-scoped latest-session
pointer therefore require an explicit `workingDir`, `workspace`, or configured
default workspace and fail closed when none is available. Use explicit target
selection whenever several repositories are active at once.

CLI request schemas accept prompts up to 100,000 characters, but operating
systems also impose byte limits on individual argv elements. Codex new and
resume requests stream the exact prompt over stdin. `codex_fork_session`
remains argv-bound and rejects an oversized UTF-8 prompt before spawn as
non-retryable `input_too_large`. Other providers whose current CLI contracts
require an argv prompt use the same admission rule. Every other
caller-controlled argv value is checked on its final encoded form too,
including serialized agent/schema JSON, joined tool lists, instruction
overrides, paths, model names, and native session IDs. The final spawn boundary
checks every argv element plus the aggregate resolved command line against a
conservative platform-specific byte budget and a 2,048-element cap. The
aggregate byte budget excludes the environment but reserves headroom for it;
on Windows, pre-resolution admission assumes the smaller npm `.cmd`/`.bat`
wrapper limit until command resolution proves a native executable. Native
session and resume flags on non-Kit requests are included before workspace,
session, provider-artifact handoff, or durable job side effects. Claude Kit
projects its eventual argv before materializing its compiled context artifact
or allocating a durable Kit session.
An embedded NUL byte in the command or any argv element is rejected before
spawn as non-retryable `invalid_input`. Caller-facing results, long-lived job
memory, durable job args, and async flight rows use a fixed invalid-argv marker;
the optional duplicate durable payload is suppressed. None retains the rejected
vector or Node's value-echoing native error.
Native `E2BIG`, including an environment-driven failure, is normalized without
retaining the native `spawnargs`. The gateway never truncates instructions or
other values to make them fit. For stdin-backed requests, a clean provider exit
is accepted only after the complete payload write callback succeeds. A closed
or still-pending pipe becomes a fixed, non-sensitive incomplete-delivery
failure; timeout, cancellation, and provider nonzero exits remain authoritative.

This generic stdio example is not provider-support verification for the Personal MCP Appliance. Client-specific setup guides for ChatGPT, Claude web, Claude Desktop, Codex, Gemini CLI, Gemini web, and Grok remain gated by the provider-support matrix in [docs/personal-mcp/PRODUCT_CONTRACT.md](docs/personal-mcp/PRODUCT_CONTRACT.md).

### Available Tools

#### Cross-LLM Validation Tools

The personal-appliance surface exposes simplified validation tools for non-developer clients. These tools start provider CLI jobs through the durable async job manager and return normalized provider status plus raw job references.

- `validate_with_models`: ask two or more providers to independently validate a question.
- `review_changes`: capture one complete Git review artifact, fence repository
  content as untrusted data, and start read-only independent reviewers. See
  [Repository change review](#repository-change-review).
- `second_opinion`: ask one provider to review an answer.
- `red_team_review`: challenge a plan, answer, or document for risks and failure modes.
- `consensus_check`: check whether providers agree with a claim.
- `ask_model`: ask one provider through the simplified surface.
- `synthesize_validation`: run an explicit judge model after provider results have
  been collected. General validation requires the caller's question and terminal
  normalized results. A `review_changes` run instead reloads its exact owned
  durable results from `validationId`; caller-supplied question/results are ignored.
- `list_available_models`: list the models each provider CLI exposes through the simplified surface.
- `job_status` and `job_result`: poll and collect validation job outputs.
- `validation_receipt`: retrieve the canonically hashed immutable receipt of a terminal cross-LLM validation run by `validationId` (returns `minted | pending | verification_failed | expired_unminted | not_found`, own-or-not-found). `verification_failed` means a stored receipt exists but disagrees with its durable run, which is a defect to investigate; `expired_unminted` only ever means absence. `format: "markdown"` renders a human-readable report; `includeRawResponses` inlines complete provider answer text when the linked job still exposes identity-verified output. Registered only when the attached job store provides the durable validation-run store capability (`sqlite` and `postgres`).

The same receipt is also exposed as the `validation-receipt://{validationId}` MCP resource (same durable gate and own-or-not-found owner scoping).

The validation report preserves per-provider disagreement. Optional judge synthesis is explicit about which provider produced the judge job.

##### Repository change review

`review_changes` accepts an absolute local `workingDir` or a registered
`workspace`, then resolves `scope: "auto" | "uncommitted" | "branch" |
"commit"`. It can take an explicit Git `base`, literal repository-relative
`paths`, `stance: "standard" | "adversarial"`, reviewer `models`, an optional
`judgeModel`, `trustCursorWorkspace`, and fail-closed artifact/prompt byte
ceilings.

Cursor refuses to review a directory it does not trust, so a cursor seat is
granted `--trust` only when the reviewed directory is a registered
`[[workspaces.repos]]` path whose `providers` include cursor (a gateway worktree
beneath one counts, and the nearest enclosing registration decides). On any
other directory the cursor seat is skipped with an actionable reason, and the
rest of the roster still runs. `trustCursorWorkspace: true` accepts the grant
for one durable review run. The consent applies to Cursor seats in that run's
reviewer roster and to its planned Cursor judge when `synthesize_validation`
launches it later. It is bound to the run owner, repository, and planned judge,
so another principal or review run cannot replay it. That is a real decision
rather than a formality: a trusted folder is also where cursor loads project
rules and `AGENTS.md`, so the repository under review gains some influence over
its own reviewer, which the fenced review prompt otherwise forbids. The artifact keeps
committed, staged, unstaged, and regular non-ignored untracked file evidence separate. It
forces tracked diffs to remain readable even when in-tree attributes mark them
as non-diffable. The `review-evidence.v2` artifact exposes `committedPatch`,
`stagedPatch`, and `unstagedPatch` independently; each segment carries its
sorted path inventory, encoding, exact byte length, SHA-256 identity, and
content. This prevents an index change and its worktree-only reversal from
canceling out. The artifact is collision-fenced, byte-counted, SHA-256
identified, race-checked, and never truncated. In `auto` mode, a diverged branch is
reviewed from its merge base with working-tree evidence included. Otherwise,
a dirty tree selects uncommitted changes, while a clean tree falls back to the
last commit (`HEAD^..HEAD`) without working-tree evidence. Unsafe untracked
file types or a repository mutation during capture cause a refusal.

The tool starts asynchronous provider jobs and returns a `validationId`, exact
artifact and prompt identities, file inventory, and one `rawJobReference` per
reviewer. Poll those references with validation `job_status` and collect them
with validation `job_result`, not the similarly named `llm_job_*` tools. If a
judge was requested, wait for every reviewer to become terminal, then call
`synthesize_validation` with the `validationId` and the same `workingDir` or
`workspace` selector. Continue collecting results for progress and human
visibility, but do not pass them as review evidence: for a `review_changes` run,
the gateway ignores caller-supplied `question` and `providerResults`, reloads
the exact owned durable linked terminal jobs, and reconstructs requested but
unavailable seats as skipped. General validation synthesis still requires a
caller-supplied question and terminal normalized results.

The review surface is registered only with durable SQLite or PostgreSQL job and
validation-run storage. Each CLI review job retains the exact fenced prompt in
its expiry-bound `payload_json`; its persisted argv contains only a hash marker.
The non-expiring flight recorder does not receive repository-review prompts.
Configured HTTP/API reviewer seats require explicit `allowApiUpload:true`
because the complete artifact leaves the local CLI boundary. Remote HTTP/OAuth
workspace reviews reject API reviewer uploads even with that flag. Treat the
durable job store as sensitive. Its retention is unbounded by default, and an
operator can set `[persistence.retention].jobs` when a bounded record is
required.
When `judgeModel` is an HTTP/API provider, `review_changes` binds that explicit
consent, the judge provider, the resolved repository, and the caller identity to
the durable `validationId`. The later `synthesize_validation` call must provide
that id and the same repository selector. The stored judge, repository, owner,
and upload consent are authoritative. The gateway atomically claims the planned
judge once, so concurrent or repeated synthesis cannot start a second judge.
A follow-up argument cannot grant or override upload consent.

#### LLM Request Tools

##### `claude_request`

Execute a Claude Code request with optional session management.

**Parameters:**

- `prompt` (string, optional*): The prompt to send (1-100,000 chars). *Exactly one of `prompt` or `promptParts` is required (mutually exclusive)
- `model` (string, optional): Model name or alias (use `list_models` for available values; supports `latest`)
- `outputFormat` (string, optional): Output format (`text|json|stream-json`), default: `stream-json` — the gateway parses NDJSON usage events for token/cost observability; override to `text` only when you want unparsed stdout
- `sessionId` (string, optional): Specific session ID to use. Under `mcp_managed`, native continuation is a high-risk input because it can inherit an unverified provider posture; it requires approval and `LLM_GATEWAY_APPROVAL_ALLOW_BYPASS=1`, but does not select a full-permission profile.
- `continueSession` (boolean, optional): Continue the active session. It has the same managed-approval requirement as `sessionId`. Because Claude `--continue` selects by cwd, it requires `workingDir` or a registered workspace selected explicitly, through caller-owned session metadata, or by the configured default. That workspace may optionally supply a gateway worktree. The request fails closed when no selection supplies a stable cwd.
- `createNewSession` (boolean, optional): Always create a new session
- `forkSession` (boolean, optional): Fork the resumed session instead of appending to it. Under `mcp_managed`, it is a high-risk native-fork input that requires approval and `LLM_GATEWAY_APPROVAL_ALLOW_BYPASS=1`, but stays bounded.
- `allowedTools` (string[], optional): Restrict Claude tools to this allow-list. A non-empty allow-list is a high-risk managed input because it can change the tool posture.
- `disallowedTools` (string[], optional): Explicitly deny listed Claude tools
- `permissionMode` (string, optional): Claude permission mode (`default|acceptEdits|plan|auto|dontAsk|bypassPermissions`); preferred over `dangerouslySkipPermissions`. `bypassPermissions` is a direct full-permission request under `mcp_managed`.
- `dangerouslySkipPermissions` (boolean, optional): Deprecated, maps to `permissionMode: "bypassPermissions"`; `permissionMode` wins when both are set. It is a direct full-permission request under `mcp_managed`.
- `agent` (string, optional): Named sub-agent to run as. A non-empty value is a high-risk managed input because it can change tool and permission posture.
- `agents` (string, optional): Inline agent definitions JSON. A non-empty value is a high-risk managed input for the same reason.
- `systemPrompt` / `appendSystemPrompt` (string, optional): Replace or extend the system prompt. A non-empty value is a high-risk managed input.
- `systemPromptFile` / `appendSystemPromptFile` (string, optional): Replace or extend the system prompt from a file. A non-empty file path is a high-risk managed input.
- `safeMode` (boolean, optional): Start Claude with local customizations disabled, including `CLAUDE.md`, skills, plugins, hooks, MCP, commands, and agents. `true` is a high-risk managed input.
- `bare` (boolean, optional): Start Claude in minimal mode, skipping local customization discovery. `true` is a high-risk managed input.
- `debugFile` (string, optional): Write Claude debug output to a file. A non-empty path is a high-risk managed input.
- `maxBudgetUsd` (number, optional): Budget cap in USD for the request
- `maxTurns` (integer, optional): Agent-loop turn cap
- `effort` (string, optional): Reasoning effort (`low|medium|high|xhigh|max`)
- `fallbackModel` (string, optional): Auto-fallback model when the default is overloaded
- `jsonSchema` (string, optional): JSON Schema literal constraining structured output
- `addDir` (string[], optional): Additional workspace directories. A non-empty value is a high-risk managed input.
- `noSessionPersistence` (boolean, optional): Ephemeral session (not persisted to disk)
- `settingSources` / `settings` / `tools` (optional): Setting sources to load, settings JSON path/literal, built-in tool restriction. Non-empty setting sources, settings, or tool selections are high-risk managed inputs.
- `pluginDir` / `pluginUrl` (string[], optional): Load Claude plugins from local directories or URLs. Non-empty values are high-risk managed inputs.
- `excludeDynamicSystemPromptSections` (boolean, optional): Trim dynamic system prompt sections
- `approvalStrategy` (string, optional): `"legacy"` (default) or `"mcp_managed"`. Managed mode uses `acceptEdits` by default and forces `strictMcpConfig:true`, so Claude uses only the gateway-generated MCP configuration. A direct full-permission request requires all of an explicit caller request, an approval-manager approval, and `LLM_GATEWAY_APPROVAL_ALLOW_BYPASS=1`. Other high-risk inputs require the approval and operator setting too, but remain bounded and do not themselves select full permission.
- `approvalPolicy` (string, optional): `"strict"`, `"balanced"`, or `"permissive"`
- `mcpServers` (string[], optional): Names of MCP servers to expose to Claude (default: none). Legacy requests resolve names from the local registry or Codex MCP config; unknown names are reported as unavailable. Under `mcp_managed`, Claude uses only the generated configuration and only registry entries explicitly provisioned as gateway-owned local commands are eligible. Dynamic `npx` launchers, ambient-PATH commands, and Codex-config overrides are rejected. Configure and deploy the managed entries in the gateway environment.
- `strictMcpConfig` (boolean, optional): In legacy mode this defaults to `false`; set `true` to require only the generated MCP config and fail if requested servers are unavailable. Under `mcp_managed`, the gateway forces it to `true` and a caller-supplied `false` cannot weaken that boundary.
- `optimizePrompt` (boolean, optional): Optimize prompt for token efficiency (44% reduction), default: false
- `optimizeResponse` (boolean, optional): Optimize response for token efficiency (37% reduction), default: false
- `correlationId` (string, optional): Request trace ID (auto-generated if omitted)
- `idleTimeoutMs` (integer, optional): Kill a stuck process after output inactivity; 30,000 to 3,600,000 ms. Idle enforcement applies only when `outputFormat` is `stream-json`; it is ignored for text/json, which produce no output until the run completes
- `worktree` (boolean|object, optional): Run inside a gateway-owned git worktree (slice λ). A worktree requires a registered workspace selected explicitly, through caller-owned session metadata, or by the configured default; it never inherits process cwd or combines with `workingDir`, `addDir`, or `includeDirs`. Materialization suppresses repository, system, and global Git hooks and configured clean, smudge, and process checkout filters, so filter-dependent content such as Git LFS remains in its repository representation instead of executing host commands. Requesting a worktree is a high-risk managed input that requires approval and `LLM_GATEWAY_APPROVAL_ALLOW_BYPASS=1`, but remains bounded.
- `promptParts` (object, optional): Cache-aware structured prompt `{ system?, tools?, context?, task }`; mutually exclusive with `prompt`
- `forceRefresh` (boolean, optional): Bypass dedup and force a fresh CLI run, default: false

Workspace boundary: stdio callers may use machine-local paths directly. HTTP/tunnel callers must pass `workspace` or rely on a configured default/session workspace; path fields are then validated relative to that workspace. `[workspaces].allow_unregistered_working_dir` is an inert legacy key: it is still accepted so old configs keep loading, but nothing reads it at either value, and setting it now logs a warning at startup. It never allowed arbitrary HTTP working directories or additional directories.

**Response extras:**

- `approval`: Approval decision record when `approvalStrategy="mcp_managed"`
- `mcpServers`: Requested/enabled/missing MCP servers for this call

**Example:**

```json
{
  "prompt": "Write a Python function to calculate fibonacci numbers",
  "model": "sonnet",
  "continueSession": true,
  "optimizePrompt": true,
  "optimizeResponse": true
}
```

##### `codex_request`

Execute a Codex request with optional session tracking.

**Parameters:**

- `prompt` (string, optional*): The prompt to send (1-100,000 chars). *Exactly one of `prompt` or `promptParts` is required (mutually exclusive)
- `model` (string, optional): Model name or alias (use `list_models` for available values; supports `latest`, recommended: `gpt-5.5`)
- `fullAuto` (boolean, optional): Deprecated — expands to `--sandbox workspace-write` only (current Codex no longer accepts approval-policy flags); prefer `sandboxMode`
- `sandboxMode` (string, optional): Codex sandbox (`read-only|workspace-write|danger-full-access`).
- `dangerouslyBypassApprovalsAndSandbox` (boolean, optional): Request Codex's full approvals-and-sandbox bypass.
- `dangerouslyBypassHookTrust` (boolean, optional): Request Codex hook-trust bypass.
- `approvalStrategy` (string, optional): `"legacy"` is the only executable strategy. `"mcp_managed"` is rejected before Codex launches because the adapter cannot isolate ambient MCP configuration.
- `approvalPolicy` (string, optional): Has no effect for Codex because `mcp_managed` is unavailable.
- `mcpServers` (string[], optional): Metadata only. It does not configure or isolate Codex MCP servers.
- `sessionId` (string, optional): Session identifier for tracking.
- `resumeLatest` (boolean, optional): Resume a previous Codex session (`codex exec resume --last`). Do not rely on which session `--last` selects or on the resumed working directory (#258): `--last` is cwd-filtered upstream and the child is still spawned with the gateway-resolved cwd. Verify the target, or start a fresh session when it must be certain. Ignored if `sessionId` is set.
- `createNewSession` (boolean, optional): Always create a new session
- `forceRefresh` (boolean, optional): Bypass dedup and force a fresh CLI run, default: false
- `outputFormat` (string, optional): `text` (default) or `json` (`--json` JSONL events for token usage extraction)
- `outputSchema` (string|object, optional): Codex `--output-schema`, path or inline JSON Schema.
- `workingDir` (string, optional): Working root for this session (`-C`/`--cd`; new sessions only). Personal Agent Config Kit mode requires an absolute path.
- `addDir` (string[], optional): Additional writable workspace directories (one `--add-dir` per entry; new sessions only).
- `ephemeral` (boolean, optional): Codex `--ephemeral` (no session persistence)
- `images` (string[], optional): Image attachments (one `-i <path>` per entry).
- `profile` (string, optional): Codex `--profile <name>` (new sessions only; ignored with a logged warning on resume).
- `configOverrides` (object, optional): Codex `-c key=value` overrides. Local callers only; remote HTTP/OAuth requests are rejected.
- `enable` / `disable` (string[], optional): Codex `--enable` / `--disable` feature overrides. They are `-c features.*` equivalents and are also local-only.
- `ignoreRules` / `ignoreUserConfig` (boolean, optional): Codex `--ignore-rules` / `--ignore-user-config`.
- `outputLastMessage` (string, optional): Codex `--output-last-message <path>`.
- `oss` (boolean, optional): Codex `--oss`, selecting the open-source provider.
- `localProvider` (string, optional): Codex `--local-provider <name>`.
- `worktree` (boolean|object, optional): Run inside a gateway-owned git worktree (slice λ). A worktree requires a registered workspace selected explicitly, through caller-owned session metadata, or by the configured default; it never inherits process cwd or combines with `workingDir`, `addDir`, or `includeDirs`. Materialization suppresses repository, system, and global Git hooks and configured clean, smudge, and process checkout filters, so filter-dependent content such as Git LFS remains in its repository representation instead of executing host commands.
- `promptParts` (object, optional): Cache-aware structured prompt `{ system?, tools?, context?, task }`; mutually exclusive with `prompt`
- `optimizePrompt` (boolean, optional): Optimize prompt for token efficiency, default: false
- `optimizeResponse` (boolean, optional): Optimize response for token efficiency, default: false
- `correlationId` (string, optional): Request trace ID (auto-generated if omitted)
- `idleTimeoutMs` (integer, optional): Kill a stuck Codex process after output inactivity; 30,000 to 3,600,000 ms

**Response extras:**

- `mcpServers`: Requested MCP-server metadata for this call

**Example:**

```json
{
  "prompt": "Create a REST API endpoint",
  "model": "gpt-5.5",
  "sandboxMode": "workspace-write",
  "optimizePrompt": true
}
```

##### `codex_fork_session`

Fork an existing Codex session into a new branch (`codex fork <SESSION_ID|--last> <prompt>`), preserving the original session's history while the fork diverges. Unlike Codex new and resume requests, this command remains argv-bound and rejects oversized UTF-8 prompts as non-retryable `input_too_large`.

**Parameters:**

- `prompt` (string, required): Prompt text for the forked session (1-100,000 chars)
- `sessionId` (string, optional): Codex session UUID to fork from (mutually exclusive with `forkLast`).
- `forkLast` (boolean, optional): Fork the most recent Codex session instead of naming one.
- `model` (string, optional): Model name or alias (e.g. `gpt-5.5`, `latest`)
- `sandboxMode` (string, optional): Codex sandbox (`read-only|workspace-write|danger-full-access`).
- `approvalStrategy` (string, optional): `"legacy"` is the only executable strategy. `"mcp_managed"` is rejected before Codex launches because the adapter cannot isolate ambient MCP configuration.
- `approvalPolicy` (string, optional): Has no effect for Codex because `mcp_managed` is unavailable.
- `correlationId` (string, optional): Request trace ID (auto-generated if omitted)
- `idleTimeoutMs` (number, optional): Idle timeout in ms (30s-1h, omit for CLI default)

##### `gemini_request`

Execute a Google Antigravity CLI (`agy`) request with session support.

**Parameters:**

- `prompt` (string, optional*): The prompt to send (1-100,000 chars). *Exactly one of `prompt` or `promptParts` is required (mutually exclusive)
- `model` (string, optional): Model name or alias (use `list_models` for available values; supports `latest`, `pro`, `flash`)
- `sessionId` (string, optional): Session ID to resume.
- `resumeLatest` (boolean, optional): Resume the latest session automatically.
- `createNewSession` (boolean, optional): Always create a new session
- `approvalMode` (string, optional): Antigravity approval mode in legacy mode: `default` leaves agy prompted, `auto_edit` emits `--mode accept-edits`, `plan` emits `--mode plan`, and `yolo` emits `--dangerously-skip-permissions`.
- `approvalStrategy` (string, optional): `"legacy"` is the only executable strategy. `"mcp_managed"` is rejected before Antigravity launches because the adapter cannot isolate ambient MCP configuration.
- `approvalPolicy` (string, optional): Has no effect for Antigravity because `mcp_managed` is unavailable.
- `includeDirs` (string[], optional): Additional workspace directories (passed as `--add-dir`).
- `project` (string, optional): Select the Antigravity project for this session (`--project <ID>`); mutually exclusive with `newProject`.
- `newProject` (boolean, optional): Create a new Antigravity project for this session (`--new-project`); mutually exclusive with `project`.
- `sandbox` (boolean, optional): Run Antigravity in sandbox mode (`--sandbox`)
- `workingDir` (string, optional): Local Antigravity process working directory.
  Stdio/local callers may pass local paths directly; remote HTTP/OAuth callers
  must use relative paths inside a selected registered workspace. `includeDirs`
  adds read paths but does not select cwd.
- `workspace` (string, optional): Registered gateway workspace alias that selects
  the Antigravity process cwd for remote HTTP/OAuth callers.
- `outputFormat` (string, optional): `text` (default), `json`, or `stream-json`. The async job recorder launches the transcript-capable `stream-json` wire independently of the requested presentation.
- `mcpServers` (string[], optional): Metadata only. Antigravity manages its own MCP configuration; this field does not create an allowlist.
- `allowedTools`, `policyFiles`, `adminPolicyFiles`, `attachments` (string[], optional) and `skipTrust` (boolean, optional): **Unsupported by Antigravity CLI**. Non-empty values, or `skipTrust: true`, are rejected with an explanatory error.
- `yolo` (boolean, optional): Auto-approve all; equivalent to `approvalMode: "yolo"`. Emits `--dangerously-skip-permissions` in legacy mode.
- `worktree` (boolean|object, optional): Run inside a gateway-owned git worktree (slice λ). A worktree requires a registered workspace selected explicitly, through caller-owned session metadata, or by the configured default; it never inherits process cwd or combines with `workingDir`, `addDir`, or `includeDirs`. Materialization suppresses repository, system, and global Git hooks and configured clean, smudge, and process checkout filters, so filter-dependent content such as Git LFS remains in its repository representation instead of executing host commands.
- `promptParts` (object, optional): Cache-aware structured prompt `{ system?, tools?, context?, task }`; mutually exclusive with `prompt`
- `optimizePrompt` (boolean, optional): Optimize prompt for token efficiency, default: false
- `optimizeResponse` (boolean, optional): Optimize response for token efficiency, default: false
- `correlationId` (string, optional): Request trace ID (auto-generated if omitted)
- `idleTimeoutMs` (integer, optional): Total-runtime bound, not an idle timer: this provider emits no output until it exits, so the process is killed after this duration even while healthy. 30,000 to 3,600,000 ms, default 3,600,000 ms
- `forceRefresh` (boolean, optional): Bypass dedup and force a fresh CLI run, default: false

**Response extras:**

- `mcpServers`: Requested MCP-server metadata for this call

**Example:**

```json
{
  "prompt": "Explain quantum computing",
  "model": "latest",
  "resumeLatest": true,
  "optimizePrompt": true
}
```

##### `grok_request`

Execute a Grok CLI (xAI) request with session support.

**Parameters:**

- `prompt` (string, optional*): The prompt to send (1-100,000 chars). *Exactly one of `prompt` or `promptParts` is required (mutually exclusive)
- `model` (string, optional): Model name or alias (e.g. `grok-4.6`, `grok-4.5`). Prefer live discovery via `list_models` or `models://grok`: the legacy `grok-build` id was removed upstream and now hard-fails with `Invalid params: "unknown model id"`.
- `transport` (string, optional): `"cli"` (default) runs the Grok CLI; `"acp"` routes through Grok's native `grok agent stdio` transport when `[acp].enabled` and the provider's `runtime_enabled` are set (fails closed otherwise). Both transports reject `approvalStrategy:"mcp_managed"`; `approvalPolicy` has no effect. Sync-only: `grok_request_async` always runs the CLI transport and does not accept `transport`
- `outputFormat` (string, optional): `"plain"` (default), `"json"`, or `"streaming-json"`
- `sessionId` (string, optional): Session ID to resume (`--resume <id>`).
- `resumeLatest` (boolean, optional): Resume the most recent session in the current cwd (`--continue`).
- `createNewSession` (boolean, optional): Always create a new session
- `alwaysApprove` (boolean, optional): Auto-approve all tool executions (`--always-approve`) in legacy mode.
- `permissionMode` (string, optional): `default|acceptEdits|auto|dontAsk|bypassPermissions|plan`.
- `effort` (string, optional): `low|medium|high|xhigh|max`
- `reasoningEffort` (string, optional): Reasoning effort for reasoning models
- `approvalStrategy` (string, optional): `"legacy"` is the only executable strategy. `"mcp_managed"` is rejected before Grok launches because the adapter cannot isolate ambient MCP configuration.
- `approvalPolicy` (string, optional): Has no effect for Grok because `mcp_managed` is unavailable.
- `mcpServers` (string[], optional): Metadata only. Grok manages its own MCP configuration via `grok mcp`; this field does not create an allowlist.
- `allowedTools` (string[], optional): Allowed built-in tools (passed as `--tools` comma list).
- `disallowedTools` (string[], optional): Disallowed built-in tools (passed as `--disallowed-tools` comma list)
- `maxTurns` (integer, optional): Agent-loop iteration cap (`--max-turns`)
- `workingDir` (string, optional): Working directory for this invocation (`--cwd`)
- `sandbox` (string, optional): Sandbox profile for filesystem/network access (`--sandbox`, freeform; also via `GROK_SANDBOX`).
- `rules` (string, optional): Extra rules appended to the system prompt (`--rules`; supports `@file` prefix).
- `systemPromptOverride` (string, optional): Replace the agent's system prompt entirely.
- `allow` / `deny` (string[], optional): Permission allow/deny rules (one `--allow`/`--deny` per entry).
- `compactionMode` (string, optional): `summary` (default) `|transcript|segments`
- `compactionDetail` (string, optional): `none|minimal|balanced|verbose` (segments mode only)
- `agent` (string, optional): Agent name or definition file path.
- `agents` (string|object, optional): Inline subagent definitions JSON.
- `disableWebSearch` (boolean, optional): Disable web search and remote retrieval tools
- `todoGate` (boolean, optional): Enable runtime turn-end TodoGate (session-scoped)
- `verbatim` (boolean, optional): Send the prompt exactly as given (also skips gateway prompt optimisation)
- `promptFile` / `promptJson` / `single` (optional): Single-turn prompt from a file / JSON blocks / literal.
- `experimentalMemory` / `noMemory` (boolean, optional): Enable/disable cross-session memory.
- `noAltScreen` / `noPlan` / `noSubagents` (boolean, optional): Disable alt screen / plan mode / subagent spawning
- `oauth` (boolean, optional): Use OAuth during authentication.
- `restoreCode` (boolean, optional): Check out the original session commit when resuming.
- `leaderSocket` (string, optional): Custom leader socket path (`--leader-socket`, Grok 0.2.32+; default `~/.grok/leader.sock`) targeting an isolated leader process, for example a local or branch Grok build.
- `nativeWorktree` (boolean|string, optional): Grok's own `--worktree` flag (`true` means bare, string means named); distinct from the gateway `worktree` option.
- `worktreeRef` (string, optional): Branch/tag/commit to base the native worktree on (`--worktree-ref`); requires `nativeWorktree`.
- `forkSession` (boolean, optional): Fork the resumed session into a new branch instead of appending to it.
- `jsonSchema` (string|object, optional): JSON Schema (string or object) constraining structured output (`--json-schema`)
- `worktree` (boolean|object, optional): Run inside a gateway-owned git worktree (slice λ). Grok requires an explicit provider-native `sessionId`; fresh, `createNewSession`, and `resumeLatest`-only worktree requests are rejected because they cannot durably reselect the worktree. A worktree requires a registered workspace selected explicitly, through caller-owned session metadata, or by the configured default; it never inherits process cwd or combines with `workingDir`, `addDir`, or `includeDirs`. Materialization suppresses repository, system, and global Git hooks and configured clean, smudge, and process checkout filters, so filter-dependent content such as Git LFS remains in its repository representation instead of executing host commands.
- `promptParts` (object, optional): Cache-aware structured prompt `{ system?, tools?, context?, task }`; mutually exclusive with `prompt`
- `optimizePrompt` (boolean, optional): Optimize prompt for token efficiency, default: false
- `optimizeResponse` (boolean, optional): Optimize response for token efficiency, default: false
- `correlationId` (string, optional): Request trace ID (auto-generated if omitted)
- `idleTimeoutMs` (integer, optional): Kill a stuck process after output inactivity; 30,000 to 3,600,000 ms
- `forceRefresh` (boolean, optional): Bypass dedup and force a fresh CLI run, default: false

**Example:**

```json
{
  "prompt": "Summarize the latest commit message in 1 sentence",
  "model": "grok-4.6",
  "effort": "low"
}
```

#### Durable job results & automatic dedup

Every async job is persisted to a job store as it transitions through running → completed/failed/canceled. This makes the gateway a durable collection layer:

- **Re-issuing a request is safe.** Identical `*_request` / `*_request_async` calls within the dedup window (default 1 hour) short-circuit onto the existing running or completed job — the caller gets back the same job ID instead of starting a duplicate run. This directly fixes the "agent times out polling, re-issues, and the whole job starts over" failure mode.
- **`llm_job_status` and `llm_job_result` work across gateway restarts.** Job rows are retained until an operator configures a bound; callers can collect results long after the in-memory cache has evicted them.
- **A job is marked `orphaned` only when its owning gateway instance is provably gone**, never because another instance restarted. Each instance holds a periodic heartbeat lease and stamps every job it owns; the recovery sweep orphans a `queued`/`running` job only when that job's own lease has expired. On a shared store (`backend = "postgres"`) this means a fresh instance never orphans another live instance's in-flight jobs. The captured partial output of a genuinely orphaned job remains readable, and a stale-then-reviving owner that later finishes self-heals to the correct terminal state (issue #139).
- **Pass `forceRefresh: true`** on any request tool to bypass dedup and force a fresh CLI run.

##### Persistence configuration

The durable backend is configured by `~/.llm-cli-gateway/config.toml` (override with `LLM_GATEWAY_CONFIG=/path/to/config.toml`). Example:

```toml
[persistence]
backend = "sqlite"                          # "sqlite" | "memory" | "postgres" | "none"
path = "~/.llm-cli-gateway/logs.db"         # for sqlite
# dsn = "postgresql://user:pw@host/db"      # for postgres
# retentionDays = 30                       # optional legacy JOB-store bound; omitted means unbounded
dedupWindowMs = 3600000
acknowledgeEphemeral = false                # required to enable async tools with memory backend

# One retention policy, over every subsystem. Every destructive bound is OFF
# unless you write a number, because deleting prompt, response, or transcript
# history is destructive and no upgrade should do it for you. Unknown keys are
# refused rather than silently applying no bound.
# `llm-cli-gateway doctor --json` -> .storage.retention reports what each bound
# would delete BEFORE you set it.
[persistence.retention]
# jobs = 30                                 # overrides retentionDays above
# requests = 90                             # flight-recorder transcripts, incl. bodies
# wedgedValidationRuns = 30                 # validation runs nothing can ever finalize
# sweepIntervalMs = 3600000                 # how often the sweeper ticks

# Issue #139 durable orphan-recovery lease (defaults shown). Each instance
# advances a per-job lease on every heartbeat; the sweep orphans a job only
# after its own lease expires, so a fresh instance never orphans another live
# instance's jobs on a shared store. Validated: leaseTtl >= 2*heartbeat and
# httpJobGrace >= leaseTtl.
instanceHeartbeatMs = 15000                 # heartbeat cadence
instanceLeaseTtlMs = 90000                  # per-job lease TTL (6x heartbeat)
httpJobGraceMs = 300000                     # extra grace for no-pid http jobs (5 min)
orphanSweepIntervalMs = 30000               # reaper cadence
instanceGcMs = 3600000                      # gateway_instances GC horizon
# ownsOrphanRecovery = false                # DEPRECATED (#139): superseded by the lease; parsed + warned, no longer used

# Optional, postgres only. One credential per class of work, for a deployment
# that has provisioned the RBAC in docs/plans/postgres-security-hardening.md.
# `app` is not a key here: the runtime credential is [persistence].dsn above.
# `migrate` is not a key either, and must not be held by a running gateway.
# A role left out degrades onto `app`, which llm_process_health reports as
# `persistence.roles.degraded` rather than implying separation is in force.
# [persistence.roles]
# reader = "postgresql://llmgw_reader@host/db"       # transcript read-back
# analytics = "postgresql://llmgw_analytics@host/db" # aggregates, no body text
# retention = "postgresql://llmgw_retention@host/db" # job expiry
```

Backends:

- **`sqlite`** (default) — durable, file-backed. Safe for single-instance deployments.
- **`postgres`**: PostgreSQL is authoritative for every backend-governed durable subsystem, including async jobs, dedup, orphan recovery, HTTP jobs, validation state, session metadata, and the flight recorder. File-backed operator records such as approvals, admin audit, and the workspace registry are not SQLite/PostgreSQL engine choices. Use this for multi-instance or service deployments. Requires the optional peer dependency `pg` to be installed alongside the gateway.
- **`memory`** — in-process Map. Lost on gateway exit. Requires `acknowledgeEphemeral = true` to be loaded. Suitable for tests and ephemeral CI gateways.
- **`none`** — no store. **`*_request_async`, `llm_job_status`, `llm_job_result`, and `llm_job_cancel` are NOT registered on the gateway.** This is a structural invariant: agents that try to call async tools against a gateway with `backend = "none"` get a clean "tool not found" at connect time instead of silent in-memory loss after the 1-hour TTL. Use `llm_process_health` to inspect the resolved persistence state programmatically.

**`backend = "postgres"` is the whole engine decision.** The configured `dsn` must be a PostgreSQL URL. The gateway does not infer deployment topology, resolve the host, restrict PostgreSQL to a local target, or render a DSN-derived target on diagnostics. If migration, connection, or an operation fails, the affected PostgreSQL subsystem fails closed and the gateway does not open SQLite as a fallback. Health surfaces identify the selected engine and report PostgreSQL failures generically.

**Changing engines does not move data.** Existing SQLite and PostgreSQL rows stay where they are: there is no automatic migration, dual-write, or cross-engine read. Plan and execute any data move separately before cutover if old history must remain available through the gateway.

**`backend = "none"` and `LLM_GATEWAY_LOGS_DB=none` are different switches.** The first disables async job persistence; the second disables request history. Setting the backend to `"none"` leaves the flight recorder writing, and disabling the recorder leaves the job store alone. Both are stated at startup in the `Storage:` block on stderr. `llm_process_health` reports the selected engine, recorder state, role configuration, and deprecated-input decisions without rendering the configured PostgreSQL target.

**`DATABASE_URL` is deprecated and never overrides `[persistence]`.** When it is the only selector, it acts as a deprecated alias for `backend = "postgres"` plus `dsn`, so sessions, jobs, validation state, and request history stay on one engine. Against an explicit backend, or against a `dsn` it disagrees with, it is ignored with a reason: the gateway does not abort, because the outcome is fully determined and is the one the config file describes.

For PostgreSQL, apply the schema with a schema-owner or dedicated migration role before starting a DML-only gateway role:

```bash
DATABASE_URL='postgresql://<user>:<password>@<host>/<database>' npm run migrate
```

The runner serializes migration work with an advisory lock and records a SHA-256
of each migration in `schema_migrations.checksum_sha256`. On later runs, a
malformed or mismatched recorded checksum stops the runner before it calculates
or applies pending migrations. A `NULL` checksum is an explicit legacy row from
before checksum recording. It is allowed with a warning but is never backfilled,
because current source files cannot prove what SQL ran historically. Do not edit
released migration files or populate ledger checksums manually. The runner
preserves the historical 002/003 SQL and applies compatibility only while one
of those legacy versions remains pending; forward migration 018 repairs an
already-recorded legacy session/view layout. Release checks reject a source edit
to a published migration file.

Legacy environment variables (deprecated; emit a warning at startup):

- `LLM_GATEWAY_LOGS_DB` / `LLM_GATEWAY_JOBS_DB`: when no backend is explicitly configured, `none` selects `backend = "none"` and any other value selects `backend = "sqlite"` with that path. An explicit `[persistence].backend` wins. `LLM_GATEWAY_LOGS_DB` still independently disables the recorder on every backend and paths it when the selected recorder engine is SQLite.
- `LLM_GATEWAY_JOB_RETENTION_DAYS` — overrides `retentionDays`.
- `LLM_GATEWAY_DEDUP_WINDOW_MS` — overrides `dedupWindowMs`.
- `LLM_GATEWAY_ACKNOWLEDGE_EPHEMERAL` — `1`/`true`/`yes` sets `acknowledgeEphemeral = true`.

##### Host-protection limits (`[http]` and `[limits]`)

The gateway bounds HTTP session growth and async/sync job execution so a burst of
clients or requests cannot drive unbounded memory, process, CPU, or provider-request
growth. All keys live in the same `~/.llm-cli-gateway/config.toml`; defaults are
conservative but chosen not to surprise local stdio development.

```toml
[http]                              # HTTP MCP transport session lifecycle
max_sessions = 100                  # max concurrent live sessions; excess initialize returns HTTP 429
session_idle_ttl_ms = 1800000       # 30 min: reap a session idle longer than this (no client DELETE needed)
session_reaper_interval_ms = 60000  # 1 min: how often the idle reaper sweeps

[limits]                            # async + sync job-execution backpressure (per gateway process)
max_running_jobs = 32               # global concurrent running jobs (process CLI + HTTP API)
max_running_jobs_per_provider = 16  # per-provider concurrent running jobs
max_queued_jobs = 128               # bounded wait queue; a full queue rejects new work
queue_timeout_ms = 120000           # 2 min: max time a job waits in the queue before failing
completed_job_memory_ttl_ms = 3600000  # 1 h: in-memory retention for finished jobs (durable rows kept separately)
max_job_output_bytes = 52428800     # 50 MB: per-job stdout+stderr cap
```

Failure modes (all deterministic and safe to retry):

- **HTTP session cap reached**: the initialize request returns `429` with `Retry-After: 5` and a structured `{ error, code: "session_capacity", retryable: true }` body. No new session is created.
- **Idle HTTP session**: the reaper closes it (transport + gateway server) once idle past `session_idle_ttl_ms`, independent of the client sending `DELETE`. A session with an in-flight request is never reaped mid-request.
- **Job limiter saturated**: when the running limit is reached and the queue is full, `*_request` / `*_request_async` and the direct-sync fallback return a retryable `saturated` error (`structuredContent.errorCategory = "saturated"`, `retryable: true`). Nothing is spawned. When the queue has room the job waits (FIFO, per-provider fair) up to `queue_timeout_ms`, then fails with the same category.
- **Sync direct execution**: the `SYNC_DEADLINE_MS=0` and storeless/`backend="none"` paths acquire the same process permit before spawning, so no execution bypasses the limiter.
- **Output overflow**: a job whose combined stdout+stderr exceeds `max_job_output_bytes` is failed (exit code 126), its process terminated, its completion persisted, and its run slot released.
- **In-memory vs durable retention**: `completed_job_memory_ttl_ms` only ages finished jobs out of the in-memory map. The durable job store is unbounded by default and can be bounded with `[persistence.retention].jobs` or the legacy `[persistence].retentionDays`, so results stay readable via `llm_job_result` / `llm_request_result` after in-memory eviction.

Live counters are exposed on `GET /healthz` (unauthenticated, HTTP transport) and via the `llm_process_health` tool `backpressure` block: session current/max/oldest-age/idle-TTL/saturation, running and queued job counts globally and per provider, limiter saturation counters, configured TTL/output caps, and parent-process RSS/heap. These surfaces report **counts, ages, and bytes only**, never prompt text, response content, tokens, session IDs, bearer/OAuth tokens, API keys, or machine secrets.

For production user services, pair the in-process limits above with systemd's
outer guardrails so an unexpected bug, provider CLI leak, or evaluation burst
cannot consume the host:

```bash
systemctl --user edit llm-cli-gateway.service
```

```ini
[Service]
MemoryMax=2G
TasksMax=512
```

Choose values for your workload: `MemoryMax` should cover the gateway process,
the configured `max_running_jobs` provider children, and normal output buffering;
`TasksMax` should exceed the process/thread count implied by `max_running_jobs`
plus the HTTP server and SQLite work, but still be far below host exhaustion. If
systemd terminates the service at those limits, durable jobs can be inspected
after restart and `llm_process_health.backpressure` should be used to tune
`[http]`, `[limits]`, `MemoryMax`, and `TasksMax` together.

##### Per-project isolation

By default, **gateway state is global per user**, not per project. With no overrides, every Claude Code window across every repo spawns its own gateway subprocess but they all read and write the same state:

- `~/.llm-cli-gateway/logs.db` when `[persistence].backend = "sqlite"` (async jobs + flight recorder). With `backend = "postgres"`, those rows live in the configured database instead. **All destructive retention bounds default to OFF.** `[persistence.retention].jobs` prunes complete job records, `[persistence.retention].requests` prunes the flight recorder's `requests` and `gateway_metadata` tables, and `[persistence.retention].wedgedValidationRuns` prunes validation runs that can never be finalized with their `validation_run_jobs` links. An operator must opt in to each bound. `validation_receipts` is immutable by design and is never pruned; a finalized run is never pruned either, so no receipt is ever orphaned.

  Deleting rows frees SQLite pages but never bytes, so the file does not shrink. `llm-cli-gateway storage compact --yes` returns the space, with the gateway stopped, because a `VACUUM` holds an exclusive lock for the length of a full rewrite. `doctor --json` -> `.storage.retention` reports the resolved bounds, what a sweep would delete, and how many bytes a compaction would return. See `docs/plans/durable-state-lifecycle.dag.toml`.

- `~/.llm-cli-gateway/sessions.json` (gateway session metadata when using the default file session backend)
- `~/.llm-cli-gateway/config.toml` (resolved config)

When `[persistence].backend = "postgres"` selects the PostgreSQL session manager, the session metadata lives in PostgreSQL instead of `sessions.json`. This is usually what you want: `session_list` from repo A can show sessions from repo B, an async job started in window A can be polled from window B, and the 1-hour dedup window catches re-issues across windows. Gateway-managed worktrees work with PostgreSQL session storage, but their filesystem ownership remains host-local: another host sharing the database cannot reuse or clean up the worktree. A failed worktree removal is retained for retry by the owning host, and deletion processed elsewhere leaves that record intact. The database-side `cleanup_expired_sessions` function stages the same record instead of deleting a worktree-bearing session; it invokes no gateway observer and so attempts no removal itself. SQLite WAL mode protects the default job/flight-recorder database, while the file session manager uses locked atomic writes.

##### Per-project durable-job isolation

If unrelated repositories should not share async jobs, flight-recorder rows, or deduplication, point each project at its own persistence config. In `.claude/settings.local.json` for the project:

```json
{
  "mcpServers": {
    "llm-gateway": {
      "env": {
        "LLM_GATEWAY_CONFIG": "${workspaceFolder}/.gateway/config.toml"
      }
    }
  }
}
```

…and put a per-project `config.toml` in the repo:

```toml
[persistence]
backend = "sqlite"
path = "/srv/repos/.../my-repo/.gateway/logs.db"
```

Now every gateway subprocess spawned for _this_ repo's Claude Code window reads its own config and writes its durable jobs, flight-recorder rows, and deduplication state to its own SQLite file. Other repos keep using the global default. This `[persistence]` override does not move the default file-backed `sessions.json`, so it does not isolate session lists. `llm_process_health.persistence.sources.configFile` lets an agent confirm which persistence config it is actually running under.

###### Agent-executable spec (DAG-TOML)

If you want an LLM agent to perform this setup deterministically — rather than reading the prose above and guessing — copy the following DAG-TOML into the repo (e.g. `docs/planning/per-project-gateway-isolation.toml`) and point your agent at it. The schema is [`agent-assurance`](https://github.com/verivus-oss/agent-assurance/blob/main/SPEC.md) `template_kind = "implementation-dag"`. The agent MUST execute units in layer order, must not skip the verification unit, and must treat any failed gate as blocking.

```toml
[meta]
schema_version    = "1.0.0"
template_kind     = "implementation-dag"
docs              = "https://github.com/verivus-oss/agent-assurance/blob/main/SPEC.md"
confidentiality   = "public"
title             = "Per-project llm-cli-gateway durable-job isolation"
spec              = "https://github.com/verivus-oss/llm-cli-gateway#per-project-durable-job-isolation"
created           = "YYYY-MM-DD"
total_units       = 5
tier1_units       = ["U01","U02","U03","U04","U05"]
tier2_units       = []
tier3_units       = []

# ============================================================================
# [policy.agent] — persona for the agent performing the configuration.
# ============================================================================

[policy.agent]
name                 = "Gateway Persistence Isolator"
role                 = "Configuration Engineer"
purpose              = "Configure the llm-cli-gateway MCP server so its SQLite durable state is scoped to THIS repository instead of the per-user default at ~/.llm-cli-gateway/. The default file-backed session metadata remains shared."
validation_type      = "Structural + Runtime Verification"
workflow_initiator   = false
description          = "Writes a repo-local config.toml, registers an LLM_GATEWAY_CONFIG override in .claude/settings.local.json, restarts the MCP server, and confirms via llm_process_health that the gateway is now reading the repo-local config and writing to the repo-local SQLite path."

[policy.agent.orchestration]
consumes_events      = ["PerProjectIsolationRequested"]
produces_events      = ["PerProjectDurableJobIsolationComplete"]

[policy.agent.responsibilities]
items = [
  "Create the repo-local gateway data directory and add it to .gitignore.",
  "Write a config.toml that pins backend=sqlite to a repo-local path.",
  "Register the LLM_GATEWAY_CONFIG env override in .claude/settings.local.json (NOT .mcp.json — that file is committed and shared).",
  "Trigger an MCP server reconnect.",
  "Verify via llm_process_health that the resolved configFile and dbPath are the repo-local values.",
]

# ============================================================================
# [policy.instance] — concrete paths the agent fills in for THIS repo.
# Agent MUST replace <REPO_ABS_PATH> with the absolute path to the repo
# before emitting any artefact. Relative paths in config.toml MUST be
# expanded to absolute — the gateway does not re-resolve them per cwd.
# ============================================================================

[policy.instance]
repo_abs_path                  = "<REPO_ABS_PATH>"           # e.g. /srv/repos/me/my-project
gateway_data_dir_relative      = ".gateway"                  # repo-relative directory
config_toml_relative           = ".gateway/config.toml"
sqlite_db_relative             = ".gateway/logs.db"
claude_local_settings_relative = ".claude/settings.local.json"
gitignore_relative             = ".gitignore"
mcp_server_name                = "llm-gateway"               # must match the entry in .mcp.json

# ============================================================================
# [policy.gates] — blocking checks. Any failure stops the workflow.
# ============================================================================

[policy.gates]
gate_repo_abs_path_resolved    = "policy.instance.repo_abs_path must NOT be the literal string '<REPO_ABS_PATH>' when U01 starts."
gate_config_is_committed       = "policy.instance.config_toml_relative MAY be committed. policy.instance.claude_local_settings_relative MUST NOT be committed (it is per-developer). Agent MUST verify .gitignore covers .claude/settings.local.json if absent."
gate_no_legacy_env_leak        = "Agent MUST grep the shell init files for LLM_GATEWAY_LOGS_DB / LLM_GATEWAY_JOBS_DB. An explicit [persistence].backend wins for job persistence, but LLM_GATEWAY_LOGS_DB still disables the recorder on every backend and paths it when SQLite is selected. Both variables remain deprecated. The agent reports either as a finding and asks the operator to unset it before proceeding."
gate_health_confirms_isolation = "U05 MUST observe llm_process_health.persistence.sources.configFile == policy.instance.repo_abs_path + '/' + policy.instance.config_toml_relative AND llm_process_health.persistence.path == policy.instance.repo_abs_path + '/' + policy.instance.sqlite_db_relative. Anything else means the override did not take effect."

# ============================================================================
# [policy.evidence] — what each unit must emit so the work is auditable.
# ============================================================================

[policy.evidence]
per_unit_required_fields = [
  "unit_id",                  # U01..U05
  "status",                   # "completed" | "failed"
  "artefact_paths",           # files written / modified
  "stdout_tail",              # last 20 lines of any command output
  "verification_quote",       # for U05, the verbatim llm_process_health.persistence block
]
findings_required_fields = [
  "gate_id",                  # which gate failed
  "observed",
  "expected",
  "remediation",
]

# ============================================================================
# Units. Execute in layer order. U01..U03 modify the working tree; U04
# triggers a reconnect; U05 is the verification gate that decides success.
# ============================================================================

[units.U01]
name           = "create-repo-local-data-dir"
summary        = "mkdir -p <repo>/.gateway and append /.gateway/ to .gitignore (creating .gitignore if missing). The gateway will write logs.db, logs.db-wal, logs.db-shm here — none should be committed."
layer          = 0
tier           = 1
status         = "pending"
depends_on     = []
blocks         = ["U02"]
estimated_loc  = 5
files_modify   = [".gitignore"]
produces       = ["ART:gateway-data-dir"]
consumes       = []

[units.U02]
name           = "write-config-toml"
summary        = "Write <repo>/.gateway/config.toml with [persistence] backend='sqlite' and path=<absolute-path-to-repo>/.gateway/logs.db. Path MUST be absolute. Do NOT use ~ — the gateway expands ~ but [persistence].path is read literally if not prefixed with ~/, and Claude Code may launch the gateway with a HOME that surprises you."
layer          = 1
tier           = 1
status         = "pending"
depends_on     = ["U01"]
blocks         = ["U03"]
estimated_loc  = 10
files_modify   = [".gateway/config.toml"]
produces       = ["ART:gateway-config"]
consumes       = ["ART:gateway-data-dir"]

[units.U03]
name           = "register-llm-gateway-config-env-in-claude-local-settings"
summary        = "Add (or merge) an mcpServers.<mcp_server_name>.env entry in .claude/settings.local.json that sets LLM_GATEWAY_CONFIG to the absolute path of .gateway/config.toml. Do NOT modify .mcp.json — that file is committed and the path would be wrong for every other developer. If .claude/settings.local.json already has an mcpServers.<mcp_server_name> entry, the agent MUST merge into the existing env map (preserving other keys), not overwrite the whole entry."
layer          = 2
tier           = 1
status         = "pending"
depends_on     = ["U02"]
blocks         = ["U04"]
estimated_loc  = 20
files_modify   = [".claude/settings.local.json"]
produces       = ["ART:claude-local-settings"]
consumes       = ["ART:gateway-config"]

[units.U04]
name           = "trigger-mcp-reconnect"
summary        = "Ask the operator to run /mcp in Claude Code (or restart Claude Code) so the gateway subprocess is re-spawned under the new env. The agent cannot do this itself — MCP server lifecycle is owned by the host."
layer          = 3
tier           = 1
status         = "pending"
depends_on     = ["U03"]
blocks         = ["U05"]
estimated_loc  = 0
files_modify   = []
produces       = ["OUT:mcp-reconnected"]
consumes       = ["ART:claude-local-settings"]

[units.U05]
name           = "verify-via-llm-process-health"
summary        = "Call llm_process_health and assert the returned persistence block satisfies policy.gates.gate_health_confirms_isolation. Quote the verbatim persistence block in evidence. If the assertion fails, the agent MUST NOT mark the workflow complete — it must emit a finding under policy.evidence.findings_required_fields, naming the observed vs. expected configFile/path, and stop."
layer          = 4
tier           = 1
status         = "pending"
depends_on     = ["U04"]
blocks         = []
estimated_loc  = 5
files_modify   = []
produces       = ["ART:durable-isolation-verification","OUT:per-project-durable-isolation-complete"]
consumes       = ["OUT:mcp-reconnected"]
```

**Why this matters for agents:** the gateway has multiple configuration surfaces (TOML file, env-var overrides, two different MCP settings files) and one easy mistake, editing the committed `.mcp.json` instead of the local-only `.claude/settings.local.json`, will silently break the per-project persistence scope for every other developer on the repo. The DAG above encodes the correct sequence, the verification gate, and the failure modes explicitly so an agent can execute it without inference. It deliberately does not claim to isolate the default file-backed session store.

##### `mistral_request`

Run a Mistral Vibe agentic coding request. Like `grok_request` in shape, but with Vibe's specific surface:

- `model` (string, optional): Vibe model alias (for example `mistral-medium-3.5` or `latest`). The resolved value is injected via the `VIBE_ACTIVE_MODEL` environment variable; omit it to let the gateway discover Vibe config and avoid stale hardcoded defaults.
- `transport` (string, optional): `"cli"` (default) runs the Vibe CLI; `"acp"` routes through Vibe's native `vibe-acp` transport when `[acp].enabled` and the provider's `runtime_enabled` are set (fails closed otherwise). Both transports reject `approvalStrategy:"mcp_managed"`; `approvalPolicy` has no effect. Sync-only: `mistral_request_async` always runs the CLI transport and does not accept `transport`
- `permissionMode`: the Vibe `--agent` name: builtins `default | plan | accept-edits | auto-approve`, or any install-gated/custom agent. Requests emit the supplied name in legacy mode.
- `allowedTools` (string[], optional): One `--enabled-tools <tool>` flag per entry.
- `disallowedTools` (string[], optional): One `--disabled-tools <tool>` flag per entry, applied after the enabled-tool filter.
- `outputFormat` (string, optional): Vibe 2.x values are `"text"`, `"json"`, or `"streaming"`; legacy aliases `"plain"` and `"stream-json"` are accepted and normalized before spawn.
- `sessionId` / `resumeLatest` / `createNewSession`: standard session controls. Current Vibe defaults session logging to enabled; if an older config has `[session_logging] enabled = false`, `doctor --json` surfaces an actionable next-action.
- `trust` (boolean, optional): Emit `--trust` so Vibe trusts the cwd for this invocation only (not persisted; skips the interactive trust prompt).
- `maxTurns` (integer, optional): Agent-loop iteration cap (`--max-turns`, programmatic mode only)
- `maxPrice` (number, optional): Interrupt when cumulative cost crosses this USD cap (`--max-price`, programmatic mode only)
- `maxTokens` (integer, optional): Cap cumulative prompt + completion tokens (`--max-tokens`, programmatic mode only)
- `workingDir` (string, optional): Change to this directory before running (`--workdir`)
- `addDir` (string[], optional): Additional writable workspace directories (one `--add-dir` per entry).
- `approvalStrategy` (string, optional): `"lega