# agent-runner

[![CI](https://github.com/marcus-beauregard/agent-runner/actions/workflows/ci.yml/badge.svg)](https://github.com/marcus-beauregard/agent-runner/actions/workflows/ci.yml)
[![License: GPL-2.0-or-later](https://img.shields.io/badge/license-GPL--2.0--or--later-blue.svg)](LICENSE)

Point it at an issue or a pull request. It works, runs the repo's own gates, and leaves something a maintainer can review, plus a run record of what it did.

**Status: early.** The loop, the tool registry and the command runner work. The worker is specified and mostly unbuilt. `dev` and `resolve` parse flags and print a plan (the planner is a deterministic mock, so no model is called yet). Do not aim this at someone else's repository.

What it is meant to become is in [PRD.md](PRD.md). That file is the source of truth for behaviour; this one is a signpost.

## Layout

Plain Go layout, nothing invented:

```
cmd/agent-runner/     the binary
internal/agent/       the loop: plan, act, observe, reflect
internal/tools/       tool registry and the argv-only command runner
internal/policy/      what a tool may do
internal/report/      plans and run reports
```

Everything sits under `internal/` because the design still moves and there is no API to keep compatible.

## Build and test

```bash
go build -o agent-runner ./cmd/agent-runner
./agent-runner run "List the files in this project"
go test -race ./...
```

The default entry point runs offline against the mock planner, so a run is reproducible without a key.

CI runs these three:

```bash
test -z "$(gofmt -l .)" && go vet ./... && go test -race ./...
```

## Contributing

Humans and automated agents both. No CLA; commits carry a DCO sign-off (`git commit -s`).

Keep changes small, and open an issue before writing code unless the fix is one obvious line. [CONTRIBUTING.md](CONTRIBUTING.md) has the details, and [AGENTS.md](AGENTS.md) is the same contract written for coding agents.

## Licence

GPL-2.0-or-later. See [LICENSE](LICENSE).
