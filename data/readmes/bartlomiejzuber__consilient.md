![Scattered review comments funneled into a single checklist](assets/banner.png)

# Consilient

Every team enforces conventions that never make it into a handbook. They show up as review
comments, get applied, and stay in reviewers' heads. Consilient reads a repository's pull-request
review history, extracts the conventions the team actually enforces, drops everything a linter or
an existing doc already covers, and writes the rest into a ruleset your AI coding assistant loads.
Re-run on a schedule, the ruleset follows the team as new reviews land.

This repository is the build spec, not the tool. Hand `SPEC.md` to a capable coding agent
(Claude Code, or any LLM that can run an agentic workspace), answer a short set of questions about
your setup, and it scaffolds the pipeline against your review history on GitHub, GitLab, or any
other host.

How it works, step by step and with the production numbers, is on the
[project page](https://bartlomiejzuber.github.io/consilient/).

## Using the spec

1. Open `SPEC.md` in your coding agent, for example `claude` in this directory.
2. Answer the decision questions (LLM provider, Git host, models, output format, deployment).
   Each comes with a recommended default.
3. The agent scaffolds the pipeline, by default as a weekly CI job. Review the result and run one
   bounded end-to-end pass before any full run.

## What you get

One ruleset file per repository: one line per rule, each carrying a confidence score, how often
reviewers enforced it, and the pull requests it was learned from. Rules below the enforcement
threshold go to a separate candidates file that is never loaded into sessions. The format is
deliberately small because the ruleset rides along in your coding agent's context on every
session.

## Example

[`examples/react/`](examples/react/) is a complete run against
[React](https://github.com/facebook/react), Meta's UI library: 52 review comments mined from
7 pull requests produce a 4-rule [`AGENTS.md`](examples/react/AGENTS.md), with every rule traced
to its source comment and every suppression checkable against React's own eslint config. The
walkthrough is in [`examples/react/README.md`](examples/react/README.md).
