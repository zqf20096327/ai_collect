# Caeser

### Go CI investigation engine

Caeser turns a failed Go CI run into a structured investigation. It connects
the original logs and artifacts to the exact source revision, traces failure
locations and values through the code, and ranks evidence-backed leads. When
deeper investigation is enabled, it can reproduce failures, compare revisions,
run focused experiments, and use a configured model to help assess evidence or
propose a repair. The result is a report developers can inspect, continue with
their own tools or assistant, and verify themselves.

Caeser separates what a run **observed** from what source analysis, experiments,
or a model **infer**, and records unresolved questions explicitly when evidence
runs out. The default GitHub workflow is evidence-first. Reproduction,
cold-path experiments, model analysis, and repair are separate opt-in paths;
see [what runs by default](#default-ci-path-and-deeper-investigations).

**Built for Go**, with detection foundations for other ecosystems on the
[adapter roadmap](#adapter-roadmap).

[Quickstart](#try-it-locally) · [GitHub Actions](#add-it-to-github-actions) ·
[How it works](#why-the-engine-is-structured-this-way) ·
[Capabilities & results](docs/capabilities.md) ·
[Contribute](#contributing)

## What you get

| On the pull request | In the downloadable report | In your own assistant |
| --- | --- | --- |
| A short failure summary and the most likely function to inspect | Failed checks, source excerpts, evidence, and next checks in `caeser-brief.md` | A paste-ready brief from `caeser brief --report report.json --prompt` |
| Ranked function leads with reason, confidence, and evidence IDs | Inspect `caeser-report.json` for the structured `likely_function` and `candidate_report` records | Export locally without calling a model |
| Expand **Diagnosis details** for the reasoning behind a lead | Review observed locations separately from inferred candidates | Export locally without calling a model |

## Default CI path and deeper investigations

The standard GitHub Actions integration runs a fast, evidence-first pass: it
downloads the failed run's logs and artifacts, checks out the failing revision,
builds a structured report, and publishes a pull-request comment. It does not
rerun the target tests when the original failure evidence is usable.

The broader engine can do more, when configured: reproduce the failure, compare
base and head, run bounded Go cold-path checks or runtime probes, ask a configured
model to analyze a bounded evidence package, or enter the separate repair flow.
These actions have execution and iteration boundaries; they are not all
automatically enabled by the default CI integration. Reports preserve the
evidence, hypotheses, activities, experiments, patches, and verification
results so a developer—or another assistant—can continue the investigation.

Caeser can connect to a configured model provider through its harness, or expose
investigation tools through MCP for an agent client. Model analysis is an
optional participant: it does not overwrite deterministic classification or
turn a hypothesis into a verified mechanism. See the
[architecture guide](docs/runtime-architecture.md) for component boundaries and
the [CI options](docs/ci-integration.md) for what can be enabled.

## Why the engine is structured this way

A CI failure gives you several different questions: what failed, which code is
worth inspecting, whether it reproduces, whether the PR introduced it, and what
caused it. Caeser records those questions separately so an answer to one does
not silently become an answer to another.

| Design choice | What it gives you |
| --- | --- |
| Original CI evidence first | An investigation can start from the failure that actually happened, even when its environment cannot be reproduced locally. |
| Source analysis before optional model analysis | Source locations, relationships, excerpts and evidence references are available to a developer or model from the same report. |
| Separate observed and inferred locations | A runtime stack frame and a likely caller have different labels and can be checked separately. |
| Likely-function shortlist | Developers and assistants get a ranked function, reason, confidence, and evidence IDs without waiting for a runtime probe. |
| Shared execution interface | Reproduction, comparisons and probes use execution policies, bounded output and explicit terminal results. |
| Disposable workspaces and a Docker backend | Experiments can use an isolated revision with a documented execution boundary. |
| Recorded investigation state | Evidence, hypotheses, activities and verification results remain inspectable beyond the short comment. |
| Separate analysis and publication jobs | Model credentials and comment credentials stay out of the job that handles target execution. |
| Independent report export | A useful investigation brief can be generated and shared without a model call. |

Localization and verification results are summarized under
[validation](#status-v020).

## Try it locally

Linux x86_64 users can [install the v0.2.0 binary](docs/installation.md#install-a-released-binary).
To build locally, you need Go 1.26, Git, and a C compiler for SQLite. Docker is
needed only when you choose the Docker executor:

```sh
git clone https://github.com/caeser-org/caeser.git
cd caeser
mkdir -p "$HOME/.local/bin"
go build -o "$HOME/.local/bin/caeser" ./cmd/caeser
export PATH="$HOME/.local/bin:$PATH"
caeser version
```

Analyze a saved CI log against the checkout it came from:

```sh
caeser diagnose \
  --repo /path/to/checkout \
  --ci-log /path/to/failed-ci.log \
  --artifact-first --json > report.json
```

Check out the revision that produced the log so source locations can be
matched to the right code. If you only have the log, run
`caeser evidence --ci-log /path/to/failed-ci.log`.

## Add it to GitHub Actions

After installing the CLI, run this from the repository you want to diagnose:

```sh
caeser init
```

It detects project and workflow evidence, then proposes `.caeser.yml` and
`.github/workflows/caeser.yml`. Review the command and watched workflow name,
then commit both files on your default branch. Existing files require
confirmation before replacement. Future failed runs download the prebuilt CLI;
maintainers do not need to rebuild Caeser for each investigation.

<details>
<summary><strong>What init generates: manual caller example</strong></summary>

Save this as `.github/workflows/caeser.yml` if you prefer manual setup. Replace
`CI` with the name of the workflow that runs your Go tests.

```yaml
name: Caeser

on:
  workflow_run:
    workflows: [CI]
    types: [completed]

permissions:
  actions: read
  contents: read
  issues: write
  pull-requests: write

jobs:
  diagnose:
    if: |
      github.event.workflow_run.conclusion == 'failure' &&
      github.event.workflow_run.head_repository.full_name == github.repository
    uses: caeser-org/caeser/.github/workflows/ci-diagnose.yml@v0.2.0
    with:
      run_id: ${{ github.event.workflow_run.id }}
      head_sha: ${{ github.event.workflow_run.head_sha }}
      base_sha: ${{ github.event.workflow_run.pull_requests[0].base.sha }}
```

</details>

**v0.2.0 uses a prebuilt, checksum-verified binary.** Caeser is built once per release,
not once per diagnosis. Target tests may still need their own compilation.
GitHub-hosted runners are supported; Blacksmith is not required.

This example uses evidence from same-repository runs and excludes fork PRs.
Caeser updates its existing comment on later failures. It puts the report and
supporting logs in a workflow artifact. Use `comment_detail: detailed` to show
the evidence section by default, or `comment: false` to publish only the workflow
summary and artifact. For reproducible installs, pin the reusable workflow
reference to a full commit SHA. The binary defaults to `caeser_version: v0.2.0`;
`main` opts into development source builds. See [integration options](docs/ci-integration.md).

For a custom job, use the setup action:

```yaml
steps:
  - uses: caeser-org/caeser@v0.2.0
  - run: caeser version
```

This step installs the CLI. The reusable workflow above handles evidence
collection, artifacts and PR comments. Caeser runs in your Actions account;
the default integration does not require a hosted service or App installation.
An optional repository-owned GitHub App can supply a custom comment author;
see [bot configuration](docs/ci-integration.md#optional-custom-comment-author).

<details>
<summary><strong>Configuration reference</strong></summary>


Run `caeser init` from your repository to review a proposed `.caeser.yml` and
GitHub Actions caller. If it cannot find a test command, add the command from
the failing CI job yourself. You can also write the config by hand.

```yaml
command: go test ./...
attempts: 3
timeout: 10m
executor: local
```

| Setting | When to use it |
| --- | --- |
| `command` | Set the exact test command, including any package or test filter used in CI. |
| `attempts`, `timeout` | Control explicit reproduction runs. |
| `base` | Supply the known base revision for a comparison when you intend to run one. |
| `executor`, `image` | Choose the local or Docker executor. Docker requires an image. |
| `--ci-log`, `--junit`, `--artifact-dir` | Read existing evidence from files. |
| `--artifact-first` | Start from existing evidence. Keep explicit execution options off for log-only triage. |

For a trusted local checkout, running `caeser diagnose --repo . --command
'go test ./...'` explicitly asks Caeser to run the command. See the
[installation guide](docs/installation.md) and
[workflow input reference](docs/ci-integration.md#inputs) for the full setup.

</details>

## Read or share the detailed report

Open the workflow run linked in the PR comment, then download the
`caeser-diagnosis-<run-id>` artifact. Open `caeser-brief.md` to read the
report or `caeser-report.json` for the full structured evidence. See the
[report guide](docs/reports.md) for each output and its location.

You can also export a brief locally. Add `--prompt` when you want a version
you can paste into another assistant. Review the excerpts before sharing
logs or private source code.

```sh
caeser brief --report report.json > caeser-brief.md
caeser brief --report report.json --prompt > caeser-prompt.md
```

## What a comment can tell you

On [Kubernetes PR #143709](https://github.com/kubernetes/kubernetes/pull/143709),
the original failure log showed a race between cacher startup and test cleanup.
Caeser connected the detector markers to overlapping `WaitGroup.Add` and
`Wait` calls. It reported the two stack locations and left the exact call and
PR attribution unresolved. [View the run and report](https://github.com/caeser-org/caeser/actions/runs/44322156729).

On the [Caeser smoke PR](https://github.com/caeser-org/caeser/pull/25#issuecomment-6980363714),
the test expected `"ready"` and got `"pending"`. The assertion line was the
useful location. There was no application call to investigate.

## Status (v0.2.0)

Caeser is a **Go release**. It keeps four things separate: the observed failure,
the observed execution location, inferred causal hypotheses, and a verified
mechanism (which requires the stringent runtime gates).

What the engine computes today:

- A ranked `likely_function` tier: primary suspect plus alternates, each with
  file, function, line, reason, provenance kind, confidence, and evidence IDs.
- A backward `causal_trace` from the failure through value provenance, local
  assignments, caller arguments, and observed stack frames.
- `defect_origin` hypotheses (`later_assignment`, `ignored_error`,
  `missing_guard`, `boundary_guard`) tied to the failing operand.
- Base/head delta correlation and assertion-anchored traces.

**Evaluation:** Caeser is validated on a curated corpus of Go failures —
paired regressions, a 16-case probe rerun, and a frozen ten-case batch. See
[capabilities and results](docs/capabilities.md), [the evaluation guide](docs/diagnosis-evaluation.md),
and the [v0.2.0 notes](docs/releases/v0.2.0.md).

## Architecture

```mermaid
flowchart TD
    CI[Failed CI logs and artifacts] --> N[Normalize failures and provenance]
    REV[Source at the failing revision] --> SRC[Go symbols and typed relationships]
    N --> C[Rank source candidates]
    SRC --> C
    C --> SSA[Bounded SSA and assertion tracing]
    C --> LF[Likely function shortlist]
    SSA --> LF
    C --> REP[Report with observed and inferred leads]
    SSA --> REP
    LF --> REP
    C -. explicit execution .-> EX[Policy-controlled experiments]
    EX --> E[Execution evidence and verification results]
    E --> REP
    REP --> BRIEF[JSON, Markdown brief and replay bundle]
    REP -. optional .-> AI[Model analysis with bounded source retrieval]
    AI --> FINAL[Final report artifact]
    BRIEF --> FINAL
    FINAL --> PR[Separate PR publication job]
```

The engine is implemented in Go. Parsing, repository analysis, execution,
verification, storage and optional model access have separate packages. The
[full architecture guide](docs/runtime-architecture.md) maps them to source files.

### Evidence ingestion and source identity

Log and artifact parsers extract failed tests, expected/actual messages, panic
frames, compiler diagnostics, race accesses and supported coverage records.
The original bounded evidence is retained alongside normalized failure episodes.
Evidence items carry IDs and provenance; source revisions, artifact digests and
execution identifiers are retained where available.

A source line from one revision and a binary offset from another build are not
interchangeable. Caeser keeps that distinction when mapping runtime evidence.
With usable original failure evidence, the report records local reproduction
as deferred instead of counting the original CI failure as a new reproduction.

### Go analysis: file, function, operation

The repository layer uses Go's standard AST parser for declarations and source
locations. Typed call analysis and SSA use `golang.org/x/tools`. They add
receiver/package-aware relationships and bounded value dependencies around
selected functions and failing assertions.

Localized implementation candidates feed operation selection, including when
backward assertion tracing is incomplete. Source fallbacks use implementation
stack frames or executed coverage ranges. SSA and source candidates share the
bounded probe shortlist. When neither supplies an operation, explicit runtime
probing can test returns in exact localized implementation functions as
hypotheses.

The report keeps three distinctions visible:

| Result | What it means |
| --- | --- |
| Observed location | CI output or an execution reported this file, line or stack frame. |
| Inferred candidate | A source relationship or ranking rule points here; inspect it against the failure. |
| Likely function | A ranked function lead with reason, confidence and evidence IDs for handoff to a developer or assistant. |
| Verified mechanism | The required operation, execution, correlation and proof checks support the stronger claim. |

The likely-function tier prefers observed stack locations and exact SSA values
from the failed assertion dependency trace over generic call leads. A candidate
rank is a search priority. A root-cause finding and PR attribution are separate.

### Investigation scheduling and verification

The investigation layer records hypotheses, unresolved objectives, activities
and experiments. Its scheduler ranks available actions using diagnostic
relevance, expected uncertainty reduction, discrimination, evidence quality,
execution cost, risk and latency. Iteration, activity, experiment and time
budgets bound further work. This is an explicit action registry and scoring
policy.

Extra execution paths are selected deliberately:

- Reproduction runs the configured command in a disposable revision workspace.
- Base/head comparison records each revision's outcome for the same command.
- The Go cold path retains the exact focused test binary and its provenance.
- Runtime probes instrument supported operations and record candidate, build,
  execution, failure-preservation and invocation-correlation outcomes.
- Repair is a separate opt-in path with isolated verification results.

Runtime verification requires strong evidence, including the right failing
invocation, source and revision identity, cited evidence and supported
dataflow/mechanism checks.

### Execution and sandbox orchestration

Caeser owns the orchestration: workspace preparation, command policy,
cancellation, output collection, execution records and cleanup. Docker provides
the container boundary. No third-party hosted sandbox account is required.

```mermaid
sequenceDiagram
    participant I as Investigation
    participant W as Disposable workspace
    participant X as Executor
    participant D as Docker container
    participant A as Evidence and artifacts
    I->>W: Prepare exact source revision
    I->>X: Command, directory, environment and limits
    X->>X: Validate execution policy
    X->>D: Start container with workspace mount
    D-->>X: Bounded stdout, stderr and exit outcome
    X->>A: Record timing, limits and execution result
    X->>D: Remove container or force cleanup on timeout
    I->>A: Preserve selected evidence and retained binaries
    I->>W: Remove disposable workspace
```

The diagram shows the Docker path. Local execution uses the same executor
interface but runs directly on the runner.

| Boundary | Local executor | Docker executor |
| --- | --- | --- |
| Process location | Runner host | Disposable container |
| Command/directory/environment policy | Enforced | Enforced |
| Output and time bounds | Enforced | Enforced |
| OS isolation | Runner's existing boundary | Container boundary, sharing the host kernel |
| Network | Host network policy | Disabled for the execution container |
| Filesystem | Host access under runner privileges | Read-only container root; writable workspace mount and temporary filesystem |
| Privileges and resources | Host/runner limits | Dropped capabilities, no privilege escalation, caller UID/GID and configured CPU/memory/process limits |
| Cancellation | Process-group cleanup | Container removal with recorded cleanup outcome |

A temporary worktree protects the source checkout from normal build writes; it
is not an OS security boundary. Local mode is the CLI default. The Go cold path
requires Docker, and the starter workflow excludes fork PRs. Prepared images
must contain the dependencies needed for network-disabled execution.
See [sandbox execution](docs/sandbox-execution.md) for the lifecycle, policies,
artifact capture and failure handling.

### Optional model harness

The model receives a bounded package of failures, candidate functions, source
excerpts, reproduction status and evidence references from the deterministic
report. This reduces the amount of raw investigation material that needs to
be selected manually before asking a model for an explanation.

When enabled, source retrieval lets the model request up to five read-only Go
lookups in a batch: a file excerpt or literal search at the reported Git commit.
Retrieval has path, size and time bounds. Search results are textual leads;
they do not become verified call edges. This is currently Git-based retrieval,
not an embedding index or a general shell tool.

Model interpretation is labeled separately. The harness validates evidence
references and constrains output, but citation validity is not semantic proof.
The model cannot change deterministic classification or verification fields.
The report survives a model-analysis failure. See
[model setup](docs/ci-integration.md#inputs) and
[the retrieval implementation](internal/agent/retrieval.go).

### Persistence, memory and caches

These have different purposes and invalidation rules:

| Layer | Stores | Reuse rule |
| --- | --- | --- |
| Repository artifact cache | Repository overviews and source snapshots | Keyed by repository, commit, analyzer version and artifact identity |
| SQLite investigation state | Executions, evidence, hypotheses, activities, experiments and verification records | Available when the same store is retained |
| Historical incident retrieval | Similar failures and symbol associations from previous investigations | Repository-scoped, with prior revision and uncertainty attached |
| Go module/build caches | Dependencies and compiler output | Managed separately by the target toolchain and workflow |

Historical similarity provides repository-scoped context for an investigation.
Fresh GitHub-hosted jobs do not gain durable incident memory automatically;
you must preserve the relevant store and cache if you want reuse across runs.

The optional gateway exposes model access and persisted investigation events.
A separate stdio MCP server exposes local investigation tools to agent clients.
Neither service is required for the default PR-report integration. See the
[gateway and MCP reference](docs/runtime-architecture.md#gateway).

## Adapter roadmap

| Adapter | Availability |
| --- | --- |
| **Go** | Available in v0.2.0. Go test output, assertion and panic locations, source relationships, and race evidence. |
| JavaScript / TypeScript | Planned. Existing environment detection and report parsing need runner-specific validation. |
| Python | Planned. Existing traceback parsing and environment detection provide a starting point. |
| Java / Kotlin | Planned. Existing JUnit and exception parsing provide a starting point. |
| Rust | Planned. Existing Cargo detection and diagnostic parsing provide a starting point. |

There are no release dates for additional adapters. Contributions with real
failure logs and reproducible tests will help define their scope. See
[adapter coverage](docs/supported-environments.md) for the implementation
foundations already present.

## Troubleshooting

<details>
<summary><strong>Common setup issues</strong></summary>


| Symptom | What to check |
| --- | --- |
| No diagnosis run | The caller must be on the default branch. Check the name under `workflows:` and confirm that the source run failed. |
| Summary exists without a PR comment | Check that GitHub associated the source run with a PR, `comment` is on, and the caller grants the publishing permissions shown above. The example excludes forks. |
| The report points only to a test | Inspect the assertion first. If a stack frame points to application code, check that the source checkout matches the failing revision. |
| A rerun fails during setup | Check the Go version, working directory, dependencies, and required services. Analyze existing logs if a local run cannot match CI. |
| Missing Markdown brief | Open the Caeser run’s diagnosis artifact and check the **Export investigation brief** step. If the artifact contains `caeser-report.json`, use `caeser brief --report caeser-report.json > caeser-brief.md` with a current build. [Details](docs/reports.md#if-the-brief-is-missing). |

Use the documented same-repository workflow guard for the starter setup.
Review logs, source excerpts, and exported briefs before sharing them
outside your project.

</details>

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for setup, where to make changes,
fixture guidelines, and how to submit a useful bug report or PR.

```sh
go test ./...
go vet ./...
go build ./...
```

| Reference | Contents |
| --- | --- |
| [Documentation hub](docs/README.md) | Website-ready docs index: start-here paths, core concepts, pipeline, commands, configuration, outputs and safety |
| [Installation](docs/installation.md) | Source builds, released binaries, and common setup failures |
| [CI integration](docs/ci-integration.md) | Workflow inputs, permissions, and execution options |
| [GitHub Action](docs/github-action.md) | Setup action, custom jobs, release installation and Marketplace |
| [Adapter coverage](docs/supported-environments.md) | Current Go adapter and foundations for planned adapters |
| [Runtime architecture](docs/runtime-architecture.md) | End-to-end flow, source analysis, probes, model harness, trust boundaries and storage |
| [Sandbox execution](docs/sandbox-execution.md) | Workspace lifecycle, executor policy, Docker isolation, artifacts and cleanup |
| [Reports and briefs](docs/reports.md) | Find the artifact, read the report, or export a missing brief |
| [External validation](docs/external-validation.md) | Live PR and upstream CI checks, with limits |
| [Diagnosis evaluation](docs/diagnosis-evaluation.md) | Running and interpreting evaluation checks |
| [Evaluation corpus](evaluation/corpus/) | Saved failures and scoring labels |

[Open an issue](https://github.com/caeser-org/caeser/issues/new) with a CI run
and what you expected the comment to report.

Licensed under [Apache 2.0](LICENSE).
