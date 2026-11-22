<div align="center">

<img src="assets/banner.svg" alt="Antigravity MCP — Gemini 4 Neon delegation for Pi, OpenCode, Codex, and Claude Code" width="100%">

<p>
  <a href="https://modelcontextprotocol.io"><img alt="MCP stdio" src="https://img.shields.io/badge/MCP-stdio-85E0C3?style=flat&labelColor=101923"></a>
  <a href="#models-and-plan-availability"><img alt="Gemini 4 Neon" src="https://img.shields.io/badge/Gemini_4-Neon-85E0C3?style=flat&labelColor=101923"></a>
  <a href="https://github.com/PyModel/antigravity-mcp/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/PyModel/antigravity-mcp/actions/workflows/ci.yml/badge.svg"></a>
  <a href="LICENSE"><img alt="MIT license" src="https://img.shields.io/badge/license-MIT-85E0C3?style=flat&labelColor=101923"></a>
</p>

<p>
  <a href="#install"><b>Install</b></a> ·
  <a href="#clients"><b>Clients</b></a> ·
  <a href="#models-and-plan-availability"><b>Models & Plans</b></a> ·
  <a href="#pricing-and-cost"><b>Pricing</b></a> ·
  <a href="#tools"><b>Tools</b></a> ·
  <a href="#migration-from-claude-agy-mcp"><b>Migration</b></a> ·
  <a href="#configuration"><b>Configuration</b></a>
</p>

</div>

# Antigravity MCP

**Connect your coding agent to Antigravity models for research, code review, and implementation.** Use Pi, OpenCode, Codex, Claude Code, or another client that can launch a local MCP stdio server. Your host keeps its own model and workflow; delegated work runs through the authenticated Antigravity CLI (`agy`).

Choose Gemini 4 Neon or another model in your account's live inventory. The bridge resolves model IDs, preserves conversation sessions, reports usage and partial failures, and returns bounded results. This is an independently maintained integration with Antigravity.

**Package:** `@pymodel/antigravity-mcp@1.0.0`. Install from [npm](#npm-installation) or use the [source build](#build). Existing users should read the [migration notes](#migration-from-claude-agy-mcp). The GitHub repository has been renamed to [PyModel/antigravity-mcp](https://github.com/PyModel/antigravity-mcp). <!-- x-release-please-version -->

## Models and plan availability

**For Antigravity access, checked November 21, 2026. Google AI Pro includes some Gemini 4 families; Google AI Ultra includes all four current Gemini 4 families. Carbon is not included with personal Pro.** Availability still depends on account, provider, region, and trial eligibility; run `agy models` or call `agy_status` before selecting a model.

| Model                        | Free / Plus | Paid Pro               | Ultra | Pro trial                           |
| ---------------------------- | ----------- | ---------------------- | ----- | ----------------------------------- |
| Gemini 4 Neon                | No          | Yes                    | Yes   | Eligible premium-device trials only |
| Gemini 4 Carbon              | No          | No                     | Yes   | No                                  |
| Gemini 4 Argon               | No          | Yes                    | Yes   | Eligible premium-device trials only |
| Gemini 4 Hydrogen            | No          | Yes                    | Yes   | No                                  |
| Orchestrator                 | No          | Yes, eligible planners | Yes   | Eligible premium-device trials only |
| Gemini 3.8 Flash             | Yes         | Yes                    | Yes   | Yes                                 |
| Claude Sonnet 5.5 / Opus 5.5 | No          | Yes                    | Yes   | No                                  |

Source: [Google Antigravity model availability](https://antigravity.google/docs/models). “All four” does not mean every historical or Enterprise-only model. Enterprise/Workspace access follows separate licensing. Older Claude 4.6 and GPT-OSS rows are scheduled for removal on November 30, 2026; the resolver therefore uses live inventory rather than a permanent allowlist.

### Gemini 4 IDs and effort

| Family   | AGY CLI ID pattern         | Listed effort variants in the supplied account snapshot |
| -------- | -------------------------- | ------------------------------------------------------- |
| Neon     | `gemini-4-neon-<tier>`     | `low`, `medium`, `high`, `xhigh`                        |
| Hydrogen | `gemini-4-hydrogen-<tier>` | `low`, `medium`, `high`, `xhigh`                        |
| Carbon   | `gemini-4-carbon-<tier>`   | `low`, `medium`, `high`                                 |
| Argon    | `gemini-4-argon-<tier>`    | `low`, `medium`, `high`                                 |

This account snapshot is a regression fixture, not a universal entitlement promise. The [headless documentation](https://antigravity.google/docs/cli/headless/) publishes examples; the installed CLI's listing decides which variants can run. No `max` variant was supplied. If an account later lists one, the bridge can resolve it without inventing one today.

Orchestrator uses separate opaque IDs when offered: `gemini-pro-orchestrator-neon`, `gemini-pro-orchestrator` (Carbon), and `gemini-pro-orchestrator-argon`. Carbon planning requires the relevant entitlement. Select the exact listed ID; do not attach an unsupported effort or treat an Orchestrator result as independent council votes.

### Which model should I choose?

Use these as evaluation candidates, based on [Google's model-selection guide](https://aistudio.google.com/docs/choosing-a-model), rather than measured performance guarantees for this bridge:

| Work                                                    | Candidate to try                                             | When to increase effort or change model                  |
| ------------------------------------------------------- | ------------------------------------------------------------ | -------------------------------------------------------- |
| Bounded search, extraction, routine implementation      | Hydrogen Medium; Flash when appropriate for the account      | Verification fails or the task requires deeper reasoning |
| Interactive debugging, architecture, multi-file changes | Neon Medium                                                  | Try High, then XHigh for difficult cases                 |
| Long-running verification and demanding reviews         | Carbon High on Ultra; Argon High as another available option | Compare accepted-task quality, elapsed time, and usage   |
| Integrated planner/executor workflow                    | A listed Orchestrator                                        | Evaluate it separately from independent fan-out          |

The built-in Flash chains remain unchanged until that evaluation is complete. Use `set_model` to opt into Gemini 4. Start with the lowest effort that meets the task's acceptance criteria; higher effort can increase output/thinking usage and latency. API token rates do not translate into a fixed AGY credit charge per task.

## Pricing and cost

**Subscription access, AI credits, and API token billing are different.** Signing in to AGY with a personal Google Account uses its plan quotas and configured AI-credit overages. API-key and Cloud modes have their own billing. Merely exporting a key does not switch a Google-account session into API mode; follow the [CLI authentication guide](https://antigravity.google/docs/install?tab=cli).

US subscription reference: Pro **$19.99/month**; Ultra options **$99.99/month** and **$199.99/month**, before applicable tax and offers. See [Google's current US subscription listing](https://gemini.google/subscriptions/?currencyCode=USD). These fees do not define a fixed AGY token allowance or the API prices below.

### API comparison only — USD per million tokens

Standard global/reference API rates checked November 21, 2026. Output includes billable thinking; cached input has its own rate.

| Model             | Uncached input | Output | Cached input | Announced change                   |
| ----------------- | -------------: | -----: | -----------: | ---------------------------------- |
| Gemini 3.8 Flash  |          $0.75 |  $3.75 |       $0.075 | Jan 1, 2027: $1.50 / $7.50 / $0.15 |
| Gemini 4 Hydrogen |          $1.50 |  $7.50 |       $0.075 | —                                  |
| Gemini 4 Argon    |          $2.00 | $10.00 |        $0.10 | Dec 1, 2026: $4 / $20 / $0.20      |
| Gemini 4 Carbon   |          $2.00 | $10.00 |        $0.10 | Dec 1, 2026: $4 / $20 / $0.20      |
| Gemini 4 Neon     |          $3.00 | $15.00 |        $0.15 | —                                  |
| Claude Sonnet 5.5 |          $2.00 | $10.00 |        $0.10 | —                                  |
| Claude Opus 5.5   |          $4.00 | $20.00 |        $0.20 | —                                  |

Sources: [Gemini Developer API pricing](https://aistudio.google.com/docs/pricing), [Claude API pricing](https://platform.claude.com/docs/en/about-claude/pricing). These are comparison rates, not an invoice for using those names through an AGY subscription. Provider, region, cache writes and storage, service tier, tools, and promotions affect actual charges. Orchestrator needs per-model usage to estimate dollars reliably.

Among the four Gemini 4 families, Hydrogen has the lowest listed standard token rates. Neon is highest during the Carbon/Argon promotion; Carbon/Argon become highest on December 1. Flash has lower uncached-input and output rates than these four; its cached-input rate matches Hydrogen. Price alone does not establish which completes a task for least total cost. The bridge reports observed usage and does not label missing counters as zero-cost or convert subscription credits into invented dollar figures.

See the [research and implementation decisions](docs/research/gemini4-routing-2026-11-21.md) and [audit report](docs/audits/2026-11-21/report.md) for sources, confirmed defects, verification, and the remaining live evaluation.

## How delegation works

<div align="center">
  <img src="assets/benchmarks.svg" alt="Pi, OpenCode, Codex, or Claude Code connects through Antigravity MCP to an available AGY model such as Gemini 4 Neon" width="100%">
</div>

1. Your coding agent calls a tool such as `analyze_files`, `deep_search`, or `delegate`, with a bounded brief and explicit workspace.
2. Antigravity MCP resolves the selected model against `agy models` and runs the task in an AGY conversation.
3. The response returns findings, reported usage, session metadata, and any incomplete-result diagnostics.
4. `follow_up` continues that conversation for corrections or additional questions.

Large source material can stay in the delegated conversation, while the host receives the requested findings. Response size is capped by `AGY_MAX_OUTPUT_CHARS`; delegating does not guarantee lower total token use or cost.

To use **Gemini 4 Neon Medium**, first check `agy_status`, then call `set_model` with the listed ID:

```json
{ "model": "gemini-4-neon-medium" }
```

This saves the user's choice without making a delegated model call. Existing automatic routes still begin with a listed Flash variant; selecting Neon explicitly changes your preference. The banner illustrates a supported selection, not a benchmark result or an entitlement guarantee.

## Clients

All four clients below can launch this local MCP stdio server. Their configuration files and timeout units differ; use the linked setup for your installed host version.

| Coding agent       | Setup                                                                   | Tool timeout example                         |
| ------------------ | ----------------------------------------------------------------------- | -------------------------------------------- |
| Pi 0.99.0 or newer | [Built-in MCP extension](docs/multi-client-support.md#pi)               | `timeout: 3660` seconds                      |
| OpenCode           | [Native V2 and V1 compatibility](docs/multi-client-support.md#opencode) | V2 `timeout.execution: 3660000` milliseconds |
| Codex CLI / IDE    | [MCP configuration](docs/multi-client-support.md#codex-cli-and-ide)     | `tool_timeout_sec = 3660` seconds            |
| Claude Code        | [MCP configuration](docs/multi-client-support.md#claude-code)           | `timeout: 3660000` milliseconds              |

Other clients need local MCP stdio support. Hosts without it can use the bundled CLI relay, which has a separate result and read-only contract. Tool names may acquire a host-specific prefix; discover the exposed tools instead of assuming a particular client's naming convention.

## Requirements

- macOS or Linux, with a coding-agent host that supports local MCP stdio.
- Node.js 24 is recommended for development and deployments. Legacy Node.js 18 is smoke-tested for stdio with npm's default engine checks. The checked-in dependency graph includes an HTTP adapter requiring Node.js 20+, so Node.js 18 `engine-strict` installation of that graph is unsupported; fresh dependency resolution can differ.
- [Antigravity CLI](https://antigravity.google/docs/install?tab=cli) (`agy`) installed and authenticated for the operating-system user running the server.

Your host's subscription or API key does not authenticate AGY. Model access and billing follow AGY's own account and provider settings.

## Install

Build the source revision containing this rename, then register that build with your chosen host. Keep the checkout and its installed dependencies available while the host uses it.

### Build

From the repository checkout:

```bash
npm ci
npm run build
npm run check:release

# Confirm the CLI is available to the same user.
agy --version
agy models
```

From that same directory, run the registration command for **one** host:

| Host        | Register the local build                                                                 |
| ----------- | ---------------------------------------------------------------------------------------- |
| Pi          | `pi mcp add antigravity -- node "$PWD/dist/index.js"`                                    |
| OpenCode    | `opencode mcp add antigravity -- node "$PWD/dist/index.js"`                              |
| Codex       | `codex mcp add antigravity -- node "$PWD/dist/index.js"`                                 |
| Claude Code | `claude mcp add --transport stdio --scope user antigravity -- node "$PWD/dist/index.js"` |

Configure the host's longer tool timeout before starting a long delegation. The [client guide](docs/multi-client-support.md) includes complete file-based examples, scope choices, absolute executable paths for desktop environments, and connection checks. The examples use the registration name `antigravity`; an existing registration can keep its name when you replace its launch command.

### npm installation

The package `@pymodel/antigravity-mcp` provides the `antigravity-mcp` executable.

Use this command as the host's stdio process:

```bash
npx -y --package @pymodel/antigravity-mcp antigravity-mcp
```

See the [per-client package registration commands](docs/multi-client-support.md#npm-installation). Starting the executable directly in a terminal launches a protocol server; it is not an interactive chat command.

Run the separate skill installer with:

```bash
npx --package @pymodel/antigravity-mcp antigravity-mcp-install-skills
```

### Bundled skills

The package ships two reusable skills. Installing or registering the server exposes its tools; run the skill installer separately to activate the instructions in your host.

| Skill                                                                | What it does                                                                                                              |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| [`antigravity-mcp`](skills/antigravity-mcp/SKILL.md)                 | Writes a task brief, dispatches it, reviews the result, and verifies changes. Includes a CLI relay for hosts without MCP. |
| [`antigravity-mcp-routing`](skills/antigravity-mcp-routing/SKILL.md) | Routes bounded research, analysis, reviews, and implementation to the appropriate tool.                                   |

From the checkout, preview discovery and choose an explicit destination:

```bash
node scripts/install-skills.mjs --list
node scripts/install-skills.mjs --dir /absolute/path/to/your/agent/skills
```

Without `--dir`, the installer selects existing agent skill directories; `--list` previews without writing. Use `--force` only when deliberately replacing a symlinked skill. The [client guide](docs/multi-client-support.md#optional-bundled-skills) documents Codex and OpenCode locations and overlapping discovery paths.

Existing `agy-delegate` and `agy-delegation` installations need the [installed-skill migration](#installed-skills). The installer warns about these old folders and leaves them intact.

[AGENTS.md](AGENTS.md) contains shared delegation guidance for coding agents; [CLAUDE.md](CLAUDE.md) points Claude Code to it. Merge relevant guidance into your project's existing instruction files without overwriting unrelated rules.

The raw relay has its own result contract and only watches read-only roots on every OS. It does not inherit the MCP bridge's macOS confinement. Unknown coverage and detected changes are reported explicitly. Use a separate report directory per job; reuse clears old captures and is locked while a run is active.

## Migration from Claude AGY MCP

| Identity                | Previous                           | New                                 |
| ----------------------- | ---------------------------------- | ----------------------------------- |
| Product                 | Claude AGY MCP                     | Antigravity MCP                     |
| GitHub repository       | `PyModel/claude-agy-mcp`           | `PyModel/antigravity-mcp`           |
| npm package             | `@pymodel/claude-agy-mcp`          | `@pymodel/antigravity-mcp`          |
| Server executable       | `claude-agy-mcp`                   | `antigravity-mcp`                   |
| Skill installer         | `claude-agy-mcp-install-skills`    | `antigravity-mcp-install-skills`    |
| MCP registry identifier | `io.github.PyModel/claude-agy-mcp` | `io.github.PyModel/antigravity-mcp` |
| Workflow skill          | `agy-delegate`                     | `antigravity-mcp`                   |
| Routing skill           | `agy-delegation`                   | `antigravity-mcp-routing`           |

The GitHub repository rename is complete. For an existing checkout whose `origin` points to this project, update its URL:

```bash
git remote set-url origin https://github.com/PyModel/antigravity-mcp.git
```

The repository rename does not publish the new npm package or change the existing `@pymodel/claude-agy-mcp` package.

The new package retains both old executable names as aliases. Those aliases identify executables inside the new package: an existing `npx @pymodel/claude-agy-mcp` command still requests the **old npm package**. Update the configured package or point the host at the source build. The new package and registry metadata are prepared in this source revision; merging a change does not itself publish either registry entry.

Keep the existing MCP registration key if you need stable host tool prefixes, and replace its launch command. Stop the previous server process and reconnect the host. Avoid registering both copies of the same bridge. Tool IDs, `AGY_*` settings, AGY session IDs, and model routing behavior remain compatible.

For a **global npm installation**, remove the old package before installing the new one; both packages export the legacy executable names and otherwise can conflict:

```bash
npm uninstall -g @pymodel/claude-agy-mcp
npm install -g @pymodel/antigravity-mcp
```

Uninstalling the npm package does not delete the separate preference or cache files. Explicit source-path or `npx --package` registration does not require a global installation.

### Installed skills

The bundled skill folders and their frontmatter names are now `antigravity-mcp` and `antigravity-mcp-routing`. The package no longer ships `agy-delegate` or `agy-delegation` folders; executable aliases do not alias skill names.

From the current checkout, preview the destinations and install the new folders into the directory used by your host:

```bash
node scripts/install-skills.mjs --list
node scripts/install-skills.mjs --dir /absolute/path/to/your/agent/skills
```

`--list` previews without writing. The installer warns when it finds old `agy-delegate` or `agy-delegation` copies in a selected destination and leaves them intact. Inspect those old folders and preserve any custom instructions or supporting files before migrating them to the new skills. After checking the new installation, remove the old copies yourself to avoid duplicate workflows in the host. Refresh or restart the host and confirm that both new skill names are discoverable.

### Saved preferences and cooldowns

New preference writes go to `$XDG_CONFIG_HOME/antigravity-mcp/preferences.json`, normally `~/.config/antigravity-mcp/preferences.json`. If that file is absent, the bridge reads the previous `claude-agy-mcp/preferences.json` in the same config root. An existing new file takes precedence, including an explicit cleared preference; an old choice cannot silently reappear after clearing it.

New cooldown records go to `$XDG_CACHE_HOME/antigravity-mcp/`, normally `~/.cache/antigravity-mcp/`. The bridge reads cooldowns from both the new and previous `claude-agy-mcp` cache locations and keeps the later expiry when they disagree. It rereads legacy records so an older process's subsequent lockout remains visible.

Legacy preference and cache files are left intact. New writes and cooldown cleanup use the new paths; old binaries do not read new state. Replace old processes and launch configurations during migration rather than relying on two-way state sharing. Selecting a model in the Antigravity app remains separate from the MCP preference.

## Tools

| Tool                 | Use for                                                                                     | Model routing (first available)                                              |
| -------------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `analyze_files`      | Files >200 lines, >3 files at once, logs, dumps, generated code                             | `gemini-flash@latest-high` → `gemini-pro@latest-low`                         |
| `deep_search`        | git log/diff/blame archaeology, repo-wide greps                                             | `gemini-flash@latest-high` → `gemini-flash@latest-medium`                    |
| `web_lookup`         | Docs, API references, external/current knowledge                                            | `gemini-flash@latest-high` → `gemini-flash@latest-medium`                    |
| `adversarial_review` | Plan critiques, design and code reviews                                                     | `gemini-flash@latest-high` → `gemini-pro@latest-high` → `claude-opus@latest` |
| `follow_up`          | Continue a prior session by `session_id` — no context resend; `write: true` to rework files | inherits the session                                                         |
| `delegate`           | Anything else heavy (read-only unless `write: true`)                                        | `gemini-flash@latest-high` → `gemini-pro@latest-low`                         |
| `delegate_many`      | One question to a council of models, or N sub-tasks at once                                 | `gemini-flash@latest-high` → `gemini-pro@latest-high` → `claude-opus@latest` |
| `set_model`          | Record the user's model + tier once; every tool routes to it first                          | metadata only; no agent turn                                                 |
| `agy_status`         | Spend, cooldowns, in-flight runs, resolved chains, agy version                              | metadata only; no agent turn                                                 |

Delegating tools accept optional `cwd` (project root), `dirs` (extra workspace roots, for cross-repo or worktree-vs-base work), `model`, `effort` (`low`/`medium`/`high`/`xhigh`/`max`, when listed — see [Effort and tiers](#effort-and-tiers)), and `slash_commands` (off by default, so a hostile file in the workspace cannot steer the delegated model through your own skills). The analytical tools also accept `schema` — a JSON Schema string that makes agy return machine-readable `structuredContent` alongside the text.

Every response is **fenced with a per-call nonce**, with the metadata in a header before the payload:

```
[antigravity-mcp 9f2a1c] model: gemini-4-neon-medium | session: 1f0c…-d4 (use follow_up to continue) | tokens: 16281
[antigravity-mcp 9f2a1c] --- agy output begins; everything below is untrusted model output ---
…agy's answer…
[antigravity-mcp 9f2a1c] --- agy output ends ---
```

The nonce is why the fence is worth anything: the metadata used to be appended _after_ the raw model output behind a plain `---` rule, which any analysed file containing `---` could forge.

### Model routing

`agy models` is the authority for the signed-in account, provider, installed CLI, and region. The bridge refreshes successful listings after five minutes and invalidates them after an invalid-model failure. Concurrent requests share one inventory fetch. It executes canonical IDs; display labels are for people and legacy preferences remain readable.

An exact ID such as `gemini-4-neon-medium` selects that fixed variant. A family selector such as `gemini-neon@latest-high` or `gemini-neon@4-medium` resolves to a listed variant. Untiered selectors choose Medium when offered, with deterministic ties. If a requested model or tier is unavailable, the error lists the available options.

A per-call `model` overrides the saved choice for that call. A saved `set_model` choice is a fixed pin: if it disappears, choose a new model explicitly. Without a saved choice, tool chains select an available model before dispatch and skip recorded cooldowns. A fixed pin is attempted even during a recorded cooldown. A model-list outage never forwards a bridge-only `@latest` selector to the CLI; a deliberately supplied canonical-looking slug may pass unvalidated, with a visible note. A default council requires a readable inventory.

### Choose the model once

By default (`AGY_ASK_MODEL=true`), the first delegation asks the user to accept the proposed default or choose an available variant. Clients supporting MCP elicitation show a model form; other clients receive an actionable request to call `set_model`. Both paths use the same default and do not invent a High effort setting.

Call `set_model` with no arguments to accept the verified default, or specify a listed variant:

```json
{ "model": "gemini-4-neon-medium" }
```

On an Ultra account that lists Carbon, pin Carbon Medium with:

```json
{ "model": "gemini-4-carbon-medium" }
```

The preference is stored at `$XDG_CONFIG_HOME/antigravity-mcp/preferences.json` (normally `~/.config/antigravity-mcp/`), with [legacy read support](#saved-preferences-and-cooldowns). Selecting a model in the Antigravity app does not itself update this MCP preference. `agy_status` shows the saved choice and account inventory. Set `AGY_ASK_MODEL=false` to skip the first-choice prompt; an existing saved preference still applies.

### Effort and tiers

The shared vocabulary is `low`, `medium`, `high`, `xhigh`, and `max`; support is verified for the selected model. `xhigh` corresponds to the UI's **Extra** level. Recognizing `max` in CLI help does not mean a model offers it. A parenthetical name such as `Orchestrator (Carbon)` is a fixed model label, not an effort.

- A fixed ID or exact label preserves its tier. `model: "gemini-4-neon-low", effort: "high"` is rejected instead of silently changing the model.
- To choose an effort deliberately, use a family selector, for example `model: "gemini-neon@latest", effort: "high"`. Only a listed sibling can be selected.
- Saved effort never retargets a different explicit model. An unavailable tier fails with the offered alternatives.
- `follow_up` preserves the session's model unless a new model is explicitly selected. If the bridge cannot determine the session model, an effort-only switch is rejected; provide both the model and desired listed tier.
- Listed Orchestrators can be selected by exact ID. The bridge does not invent a Hydrogen Orchestrator or expand a composite Orchestrator into separate council votes.

### Parallel tasks and councils

`delegate_many` supports `tasks`, explicit `models`, a singular `model`, or its default council. These are distinct selection paths; an unrelated council model cannot block explicit tasks. Every explicit council member is validated before the first spawn, and aliases resolving to the same variant are rejected. Missing default members are omitted with a visible note; a zero-member council fails. Calls sharing one conversation remain sequential. Parallel writable tasks should use separate worktrees.

### Quota cooldowns and retries

Modern AGY versions handle transient retries internally. The bridge lets those retries finish; an intermediate log 429 does not kill a healthy turn. A terminal quota failure records its reset time for later independent requests. Cooldowns use immutable records under the cache directory, so concurrent MCP processes cannot overwrite one another's lockouts. Older `cooldowns.json` files remain readable.

**A dispatched agent turn is never automatically replayed by the bridge.** Network errors, quota failures, an invalid model, and ambiguous warm-session failures can arrive after file edits or remote actions. Even an unchanged working tree or zero reported tokens does not prove replay is safe. The response preserves available partial output, session ID, usage, and terminal diagnostics so the caller can reconcile the outcome and deliberately continue. Only a warm path known to be unavailable before sending the prompt may fall back to cold execution.

Automatic routes may choose another available, non-cooling model on the next independent request. Switching Gemini families does not guarantee a different quota bucket. `AGY_ON_FAILURE=strict` changes guidance to the calling agent; it does not enable or disable a hidden retry loop.

### Timeouts and cancellation

**The bridge does not kill a run for being slow.** Elapsed time cannot distinguish a healthy long model call from a wedged process, and a wrong "stuck" verdict interrupts an agent mid-edit — leaving half-written files behind. So a run is killed only when something authoritative says so:

1. **the caller cancels** (through the host's cancellation control), **the client disconnects**, or **the bridge is stopped** — every agy run it started dies with it instead of being orphaned,
2. **a bounded raw-output limit is exceeded**, which reports an explicit failure, or
3. **the resource ceiling expires** — `AGY_MAX_RUNTIME`, default 3600s.

The ceiling is a resource cap. Raw capture is also bounded: 64 MiB of stdout per cold call or resident turn, 64 MiB of run log, and 1 MiB of cold stderr. Exceeding a bound fails explicitly and preserves a clipped recovery preview; it never silently turns a truncated JSON result into success. When it fires, the result is explicitly incomplete and preserves available bounded output and the session ID when the CLI reports one. Existing file or remote changes are not rolled back; inspect them before a deliberate `follow_up`. `AGY_TIMEOUT` overrides the ceiling for every tool; `AGY_TIMEOUT_<TOOL_NAME>` overrides it for one (e.g. `AGY_TIMEOUT_DEEP_SEARCH=900`) and wins over the global. The full set is `AGY_TIMEOUT_ANALYZE_FILES`, `AGY_TIMEOUT_DEEP_SEARCH`, `AGY_TIMEOUT_WEB_LOOKUP`, `AGY_TIMEOUT_ADVERSARIAL_REVIEW`, `AGY_TIMEOUT_FOLLOW_UP`, `AGY_TIMEOUT_DELEGATE` and `AGY_TIMEOUT_DELEGATE_MANY`; any other `AGY_TIMEOUT_<NAME>` is a startup error, so a misspelt limit cannot silently not apply. Every timeout is at most 604800s (7 days), because Node fires a longer timer immediately. The kill path escalates SIGTERM → SIGKILL across the whole process group, and fires even if agy's helper processes hold the output pipes open.

**The host has a separate deadline.** A host can cancel its tool call before the bridge reaches its own runtime ceiling. Configure the host limit with room for cleanup and an incomplete-result report: the [client guide](docs/multi-client-support.md#timeout-settings) uses 3660 seconds, or 3660000 milliseconds, for the default 3600-second AGY ceiling and 15-second kill grace. Pi and Codex use seconds; OpenCode V2 and Claude Code use milliseconds in their documented fields. These settings are host-specific, not interchangeable MCP options. Queued or multi-delegation calls may need additional time; raising only `AGY_MAX_RUNTIME` does not change the host's limit.

**Cold and resident calls have different startup costs.** A cold call starts the AGY CLI and a model conversation. `follow_up` can reuse a resident process when `AGY_WARM_SESSIONS` is enabled. Changing the model, effort, roots, restrictions, or write permission invalidates that resident and continues cold. Both paths use the runtime ceiling and cancellation controls. Inspect partial state before deliberately continuing an interrupted session.

## Configuration

All optional, via environment variables:

| Variable                    | Default                    | Description                                                                                                                                                                            |
| --------------------------- | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AGY_PATH`                  | `agy`                      | Path to the agy binary                                                                                                                                                                 |
| `AGY_MAX_RUNTIME`           | `3600`                     | Seconds; absolute runtime ceiling, independent of cancellation and bounded-output failures                                                                                             |
| `AGY_TIMEOUT`               | `AGY_MAX_RUNTIME`          | Seconds; overrides the ceiling for every tool, passed as `--print-timeout`, enforced with a 15s kill grace                                                                             |
| `AGY_TIMEOUT_<TOOL>`        | `AGY_MAX_RUNTIME`          | Seconds; overrides the ceiling for a single tool, e.g. `AGY_TIMEOUT_DEEP_SEARCH=900`. Wins over `AGY_TIMEOUT`                                                                          |
| `AGY_MAX_OUTPUT_CHARS`      | `50000`                    | Truncation cap for tool output                                                                                                                                                         |
| `AGY_DEFAULT_MODEL`         | `gemini-flash@latest-high` | Proposed by set_model; last-resort candidate in unpinned tool chains; resolved against inventory                                                                                       |
| `AGY_ASK_MODEL`             | `true`                     | Refuse to delegate until the user has chosen a model via `set_model` (asked once, saved per machine)                                                                                   |
| `AGY_EFFORT`                | unset                      | `low` \| `medium` \| `high` \| `xhigh` \| `max`; applied only when a compatible listed variant can be selected                                                                         |
| `AGY_SKIP_PERMISSIONS`      | `true`                     | Pass `--dangerously-skip-permissions` to agy                                                                                                                                           |
| _(all boolean vars)_        | —                          | Accept `true/false`, `1/0`, `yes/no`, `on/off`, case-insensitive. An unrecognized value is a startup error, never a silent default                                                     |
| _(all numeric vars)_        | —                          | Plain decimal digits only (`1e3`, `0x10` and padded values are startup errors). Enum vars (`AGY_EFFORT`, `AGY_ON_FAILURE`) are case-insensitive                                        |
| `AGY_SANDBOX`               | `false`                    | Run agy with `--sandbox`                                                                                                                                                               |
| `AGY_ON_FAILURE`            | `fallback`                 | `strict` appends an instruction to failed-tool errors telling the calling agent not to absorb the work itself                                                                          |
| `AGY_MAX_CONCURRENCY`       | `2`                        | Most agy processes at once. Calls beyond it queue instead of stampeding the shared quota                                                                                               |
| `AGY_BUDGET_TOKENS`         | unset                      | Refuse new dispatches once reported spend reaches this threshold; includes reported failed turns. An in-flight turn can exceed it; this is not a billing cap                           |
| `AGY_ALLOWED_ROOTS`         | unset (unrestricted)       | Roots that `cwd`, `dirs`, `files` and derived workspace roots may not escape, symlinks followed; separated by `:` (`;` on Windows) or commas. Input validation, not a sandbox          |
| `AGY_REDACT`                | `true`                     | Scrub credential-shaped strings from returned text, errors, metadata, and structured content                                                                                           |
| `AGY_MAX_DELEGATION_DEPTH`  | `1`                        | Refuse to delegate once this deep, so host → agy → this server → agy cannot loop                                                                                                       |
| `AGY_WARM_SESSIONS`         | `true`                     | Keep a resident agy process per conversation so `follow_up` skips the cold start                                                                                                       |
| `AGY_WARM_MAX`              | `2`                        | Most resident sessions to keep; the least recently used is evicted                                                                                                                     |
| `AGY_WARM_IDLE_SEC`         | `300`                      | Kill a resident session after this long idle                                                                                                                                           |
| `AGY_READ_ONLY_ENFORCEMENT` | `auto`                     | `auto` blocks read-only runs from writing into their roots where the platform can (macOS) and watches elsewhere; `require` refuses a read-only run it cannot block; `off` only watches |

> [!WARNING]
> **`AGY_SKIP_PERMISSIONS` is a real grant, and agy does not enforce read-only on top of it.** It
> defaults to `true` for compatibility with the historical headless workflow. In the
> repository's agy 1.2.x checks, permission-required reads and tools were denied without it.
> Current permission behavior also depends on CLI configuration; inspect denied actions
> rather than assuming every tool always needs this bypass. Those historical checks also
> found `--mode plan` advisory: it did not prevent file writes by itself.
>
> **So on macOS the bridge enforces it.** Every plan-mode run, cold or resident, runs agy under the
> kernel sandbox (`sandbox-exec`) with every write beneath `cwd` and each `dirs` root denied, for agy
> and for every process it starts. Verified against agy 1.2.2: its file-writing tool and its shell
> both fail with "Operation not permitted", while reads, git inspection and agy's own state under
> the home directory keep working. The response header says `read-only: enforced`. The sandbox is
> probed at startup; where it cannot run — Linux, or a bridge that is itself sandboxed — read-only
> runs are watched instead, the header says `read-only: watched, not enforced` with the reason, and
> `AGY_READ_ONLY_ENFORCEMENT=require` refuses them outright. `agy_status` reports which applies.
>
> The boundary is exactly the workspace roots. agy can still write anywhere else your user can, and
> a process it gets launched outside its own process tree — through `open`, an app, or a launchd
> job — is not sandboxed. That is why the watch stays on in both modes: the bridge fingerprints the
> working tree around every plan-mode run. A tree that moved despite enforcement is reported as
> `WORKING TREE CHANGED` (another writer, or an escape through such a process); a tree that moved
> without enforcement is reported as `READ-ONLY VIOLATION`. No warning means it looked and found
> nothing; a tree it could not fingerprint produces no claim in either direction. The fingerprint
> covers `cwd` and every directory the call hands agy. In
> a git repository it covers HEAD, the content and mode of every tracked change, the content of
> every untracked file, and the mode, size and mtime of every ignored entry, ignored directories
> walked the same way. A dependency or build tree at the repository top (`node_modules`, `.venv`,
> `venv`, `__pycache__`, `.next`, `dist`) counts as one entry — so a `.env` or `build/out.js` written
> in plan mode is seen, while a rewrite deep inside `node_modules` is not. Outside git it compares
> path, type, size, mode and mtime. Both are bounded to 20,000 entries and 10s. Measured on an Apple
> M5 Max: about 150 ms per snapshot on a clean 3,500-file repository, and about 1.1 s
> with 300 modified and 3,000 untracked files; two snapshots bracket each run.
> Anything else writing to the tree while the run is live (an editor, a watcher, a parallel write
> delegation) also moves it: the warning means the tree changed during the run, not proof of who
> changed it. A plan run whose tree moved and then failed carries the warning in its error. The
> header, not the tool's name and not the absence of a **denied-actions** note, is the signal to
> trust — denied actions only ever populate when the grant is off.
>
> A restriction that cannot be enforced fails the call: if the installed agy does not support
> `--mode` or `--sandbox`, a run needing either is refused rather than run with more authority than
> was asked for. `--sandbox` is in any case a terminal restriction, not a permission boundary.

> [!IMPORTANT]
> **`AGY_ALLOWED_ROOTS` validates inputs; it is not a sandbox.** It checks every call's `cwd`, `dirs`
> and `files` — including the workspace roots the bridge derives from them — before agy starts, so a
> caller cannot point a delegation outside the roots you nominate. It does **not** confine the run:
> under the permission grant agy has a shell and can reach anything the user running the bridge can.
> The read-only sandbox above only blocks writes into a read-only run's own roots, and a run allowed
> to write is not sandboxed at all. For real containment, run the bridge somewhere contained.

### Failure behavior

The bridge interprets the JSON envelope, process exit, current `finished_reason`, and structured `AGY_ERROR` diagnostics together. A print timeout returns an explicitly incomplete result when partial data is available; interrupted/error results never become clean success. Denied actions remain visible even with a success envelope. Diagnostic `retryable` describes the provider error and is not permission to replay an agent turn.

Tokens reported by failed cold or resident turns count toward the process budget. Missing usage is marked unknown rather than presented as a measured zero. With a configured token budget, unknown prior usage blocks further dispatch until the operator establishes a new budget period. The budget is checked before each actual dispatch, including queued fan-out legs. It cannot predict final usage, stop an already running request at an exact dollar amount, or cover other MCP processes. `agy_status` reports local usage, not an invoice.

`AGY_ON_FAILURE=strict` asks the calling agent to report the failed delegation instead of absorbing it silently. Invalid requests rejected before delegation, such as an invalid root or missing working directory, remain actionable caller errors.

## Known limitations

Deliberately not addressed, so they are not mistaken for oversights:

- **The delegation-depth counter is cooperative.** `AGY_MAX_DELEGATION_DEPTH` is
  propagated to the child through an environment variable, so a nested launcher that
  scrubs the environment resets it to zero. The failure mode is wasted quota through a
  delegation loop, not a privilege escape.
- **The run log is not redacted.** `AGY_REDACT` scrubs what returns to the caller; the
  temporary log agy writes for the quota poller can hold secrets in cleartext until the
  run ends. It lives in a per-process directory only your user can read, is removed on
  shutdown, and one left behind by a crash is removed the next time the bridge starts.
- **Inputs are bounded.** A prompt is passed to agy as one command-line argument, so a
  built prompt over 128 KiB (Linux's per-argument limit), or one containing a NUL byte,
  is refused before anything runs; pass file paths rather than inlining large content.
  `delegate_many` takes at most 8 tasks or 8 distinct models, and `tasks` cannot be
  combined with `models`.
- **`--disable-slash-commands` is best-effort.** Unlike `--mode plan` and `--sandbox`,
  it is dropped rather than refused when the installed agy does not advertise it, on
  the reasoning that a build without the flag most likely has no expansion to disable.
- **Read-only is enforced on macOS only.** Linux has no equivalent the bridge can apply without
  extra software, so there a read-only run is watched, not blocked. Set
  `AGY_READ_ONLY_ENFORCEMENT=require` to refuse such runs instead.
- **The macOS block is by path.** A file inside a root that already has a hard link outside
  every root can be rewritten through that outside link. Creating such a link during the run
  is blocked, and so is renaming any directory above a root to move the tree out from under
  its rule. The working-tree fingerprint still reports a change made through an old link.
- **A root that holds agy's state stays partly writable.** When a root contains `~/.gemini`,
  that directory is exempt so agy can still run; a write there is not blocked, and the
  fingerprint skips it. A root at or inside `~/.gemini` is watched, not enforced.
- **A fan-out sharing one `session_id` runs sequentially.** agy holds a
  per-conversation lock, so concurrent turns against one conversation would corrupt it.
  Fan out across conversations for parallelism.

## Development

```bash
npm ci
npm test           # unit + fake-CLI process tests; no paid model calls
npm run typecheck
npm run build      # esbuild → dist/index.js
npm run check:release # package, executable, lockfile and registry metadata agree
npm run test:package  # empty production install, tarball, stdio and bundled skills
```

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) — conventional commits, prettier, and a test per behaviour change. Vulnerabilities go through [SECURITY.md](SECURITY.md), never a public issue.

## Contributors

<a href="https://github.com/PyModel/antigravity-mcp/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=PyModel/antigravity-mcp" alt="Contributors" />
</a>

## License

MIT
