# QuantNavigator

An extensible harness for quantitative research.

QuantNavigator is a planned standalone application for running quantitative
research with coding agents. The goal is to keep a research project's questions,
experiments and evidence accessible across sessions, with a person deciding what
to investigate and which conclusions the results support.

## Current status

This repository contains the product vision and roadmap. There is no released
application code, working runtime integration or installation command yet.
All capabilities described below are planned.

## Research workflow

Consider a project testing whether a new feature improves a forecasting model.
The intended workflow starts with a question and a baseline, records the data and
validation protocol, then runs a bounded comparison. You would inspect metrics
and plots, check failures and limitations, and record a decision about the next
step. The project would retain the experiment configuration and result artifacts
needed to revisit that decision later.

QuantNavigator is intended to bring that work into one environment:

- Multiple personal workspaces, each containing separate research projects.
- Persistent project records, experiment history and results that can be
  inspected after an agent session ends.
- Runtime connections for delegating work to coding agents, with visible
  execution status and failures.
- Research tooling for reproducible comparisons, result inspection and reports,
  added through plugins and native components.

## Runtimes and extensibility

Planned external runtimes include Codex, Claude Code and Pi. Each integration
will need its own implementation and verification; support and capabilities will
be documented as they become available.

We are also considering a native QuantNavigator runtime built on Pi or Mastra.
That choice remains open. Project records and result
artifacts are intended to remain independent of the runtime. Transferring a
runtime's complete internal session is outside the current plan.

Research capabilities will be introduced gradually through plugins and native
components. The extension interfaces and the boundary between those components
still need to be designed and tested.

## Roadmap and feedback

See the [roadmap](ROADMAP.md) for planned milestones and the evidence required to
complete them. There are no announced release dates.

Use [GitHub Discussions](https://github.com/rnikitin/QuantNavigator/discussions)
to describe a research workflow you would want to use, a result you need to
inspect, or a runtime requirement.

## Contributing

Prefer small, focused pull requests. For runtime behavior changes or new plugins,
open a discussion first in
[GitHub Discussions](https://github.com/rnikitin/QuantNavigator/discussions).
See the [roadmap](ROADMAP.md) for planned work and use Discussions for deeper topics.

## License

See [LICENSE](LICENSE).
