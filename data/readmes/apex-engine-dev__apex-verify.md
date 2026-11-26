<p align="center"><img src="docs/assets/logo.svg" alt="Apex logo" width="96" height="96"></p>
<h1 align="center">Apex verify</h1>
<p align="center"><b>Your AI said it's done. Is it really done?</b></p>
<p align="center">Catch the AI code changes that pass your tests and are still wrong.<br>A different AI writes the checks your tests are missing, proves they can fail, and gives a verdict with the evidence.</p>
<p align="center">
  <a href="https://github.com/apex-engine-dev/apex-verify/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/apex-engine-dev/apex-verify/actions/workflows/ci.yml/badge.svg"></a>
  <a href="https://github.com/apex-engine-dev/apex-verify/releases/latest"><img alt="Release" src="https://img.shields.io/github/v/release/apex-engine-dev/apex-verify"></a>
  <a href="https://github.com/marketplace/actions/apex-verify-ai-change-checker"><img alt="GitHub Marketplace" src="https://img.shields.io/badge/marketplace-apex--verify-blue?logo=github"></a>
  <a href="LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/badge/license-Apache--2.0-blue.svg"></a>
  <a href="https://github.com/apex-engine-dev/apex-verify/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/apex-engine-dev/apex-verify?style=social"></a>
</p>

<p align="center"><img src="docs/assets/demo.gif" alt="Terminal: the agent says done and npm test passes; apex verify, with no API key, uses the signed-in Claude Code to write checks and answers NOT READY: a run of spaces should become one dash, expected hello-world, actual hello----world" width="800"></p>

<p align="center">A real run, no API key: the agent's own test passes, and 8 checks written from the task say otherwise.</p>

## Try it now

**See it catch a wrong change** (5 seconds, no key, no project):

```sh
npx --yes https://github.com/apex-engine-dev/apex-verify/releases/latest/download/apex-verify.tgz verify --demo
```

**Check the change an AI just made in your project** (Node 20+ and git):

```sh
cd your-project
npx --yes https://github.com/apex-engine-dev/apex-verify/releases/latest/download/apex-verify.tgz verify "what you asked the AI to do"
```

**No API key needed.** If you have **Claude Code** or **Gemini CLI** signed in, Apex verify uses it to write the checks, on the subscription you already have. With a key, it calls the API directly (Gemini by default; OpenAI, Anthropic, OpenRouter or any OpenAI-compatible endpoint with `--provider` / `--base-url`). It changes nothing in your project and exits `0` ready, `1` not ready, `3` unknown.

## Why it works

| | |
|---|---|
| 🧪 **A different AI writes the missing checks** | from your task text, never from the agent's own tests. A model grading its own work shares its blind spots. |
| 🔍 **Every check is proven able to fail** | each one runs on the old code first; a check that cannot tell old from new proves nothing and is thrown away. |
| 🛡️ **Your project is never touched** | everything runs on a copy, in a sandbox where the platform allows (macOS Seatbelt, Linux bubblewrap, Windows AppContainer). |

It also scans for the ways an agent can game a test run (tests deleted, skipped, `.only`, assertions weakened, a test script that cannot fail), runs your own tests before and after, and answers **`ready`, `not ready` or `unknown`, never a silent pass**.

## Does it work? The honest numbers

We collected AI-written changes and knew which were wrong from hidden tests Apex verify never saw.

<p align="center"><img src="docs/assets/results.svg" alt="Out of 100 wrong AI changes: on small projects tests stop 8 and Apex verify 65; on real libraries tests stop 75 and Apex verify 91" width="760"></p>

| | Wrong changes stopped | Good changes wrongly stopped |
|---|---|---|
| **17 small projects** (108 changes): tests + cheating scan | about 8 in 100 | not measured separately |
| 17 small projects: **Apex verify** | **about 65 in 100** (52 on the 12 public projects you can rerun) | about 3 in 100 |
| **23 real libraries** (200 changes, each a real historical bug fix): tests + cheating scan | 75 in 100 | 11 in 100 |
| 23 real libraries: Apex verify 0.2.4, Gemini API checker | 91 in 100 | 23 in 100 |
| 23 real libraries: **Apex verify 0.3.1, no key** (Claude Code) | **106 of 107 (99 in 100)** | **16 of 93 (17 in 100)** |

- **It helps most where tests are thin.** On the small projects the tests caught almost nothing and the checks did the work. On real libraries the tests are good, and the checks close the gap: in the latest run (0.3.1, no key) only 1 of 107 wrong changes got through ([details](benchmark/results/real-libraries-experiments)).
- **Out-of-date tests no longer count as a regression without a second look.** When a library's old test asserts exactly what the task asks to change, 0.3.1 says so (`unknown`, "update the test") instead of `not ready`. That cut false alarms on real libraries from 25 to 17 in 100 with no wrong change let through.
- **False alarms are still the open problem.** In the 0.2.4 run, 13 in 100 good changes that pass a real library's tests were stopped by a generated check; in about 7 of 10 of those the change really did not do what the task says, which leaves 4 or 5 in 100 as the checker's own mistakes (that rests on our reading of the tasks, so quote both). Three attempts to cut it did not beat the unchanged tool ([details](benchmark/results/false-alarms-real-libraries)). `APEX_MODE=warn` or `fail-on: never` never blocks.
- **It still misses things**: about a third of wrong changes on the small projects.
- **No key, no loss:** with a signed-in Claude Code as the checker, 0.3.0 stopped 19 of 31 wrong changes on the public small projects, against 16 for the Gemini API checker on the same changes, and stopped none of the 48 good ones ([details](benchmark/results/no-key-claude-cli)). One run, so "about as good".
- **A checker from another company works about as well** (Claude 55 in 100 vs Gemini 63 on the same changes); two checkers that must agree did not help ([experiments, including failures](docs/EXPERIMENTS.md)).
- Limits: Gemini models wrote every change, one run each. Everything reruns with `node benchmark/run-gate.mjs`. A correction we made on 2026-11-23 is [here](benchmark/results/real-projects/README.md).

**Please try to break it**: a wrong `ready`, or a `not ready` on a good change, is the most useful bug report we can get.

## Put it where the change happens

| Where | How | Tested |
|---|---|---|
| **Claude Code** | `/plugin marketplace add apex-engine-dev/apex-verify` then `/plugin install apex-verify@apex`: a Stop hook blocks "done" until the change is ready (at most 3 times) | in a real session |
| **GitHub pull requests** | the [Action](https://github.com/marketplace/actions/apex-verify-ai-change-checker): one verdict comment, kept up to date, and a check you can make required | on real pull requests |
| **Gemini CLI** | an `AfterAgent` hook | in real sessions |
| **Any MCP client** | the `verify_change` tool | with real MCP input |
| **Codex CLI, Cursor** | stop hooks in their documented formats | synthetic input only, **not yet in the apps** |

Copy-paste configs: [docs/INTEGRATIONS.md](docs/INTEGRATIONS.md). What is tested, per use case: [docs/USE-CASES.md](docs/USE-CASES.md).

<details>
<summary><b>The GitHub Action, and what its comment looks like</b></summary>

```yaml
# .github/workflows/apex-verify.yml
name: Apex verify
on: pull_request
permissions: { contents: read, pull-requests: write }
jobs:
  apex-verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with: { fetch-depth: 0 }
      - uses: apex-engine-dev/apex-verify@v1
        with:
          api-key: ${{ secrets.GEMINI_API_KEY }}
```

The task is the pull request's title and description. It fails the job on `not ready` (or when it could not run). Real output on the demo change:

> ### ❌ Apex verify: **NOT READY**
> - **2 checks written from the task fail on the new code**
>   ```
>   check: slugify('Hello, World!') is 'hello-world'
>     expected: hello-world
>     actual:   hello-world!
>   ```
>   - fix: Make the change satisfy the behaviour in the task; the failing check output shows what is expected.
>
> tests: 2 passed, 0 failed · checks: 5 passed, 2 failed; written from the task by gemini-3.1-pro-preview; they fail on the old code

</details>

<details>
<summary><b>Options: checkers, shared settings, signing</b></summary>

- **Checker**: with no provider and no key, Gemini CLI (if signed in with a Google account) or Claude Code writes the checks: `--provider claude-cli` / `gemini-cli` to choose, `--model` optional. The CLI gets only the prompt, in a new empty folder, with its tools, settings and MCP servers off (Claude Code) or its agent prompt replaced and no extensions (Gemini CLI). With a key: `GEMINI_API_KEY` (default), or `--provider openai|anthropic|openrouter --model <id>`, or `--base-url` for any OpenAI-compatible endpoint. Pick a checker from a different company than the agent that made the change. `--no-model` runs only your tests and the cheating scan (the verdict is then at most `unknown`).
- **What gets checked**: the working tree an agent just edited, a branch (`--base`), or a diff from any tool or person (`--diff`).
- **Languages**: checks are written for node:test, pytest, Jest, Vitest, Rust (`cargo test`) and Go (`go test`); other stacks still get your tests and the scan.
- **Team settings**: a committed `.apex-verify.json` (`provider`, `model`, `testCommand`, `timeout`, `lockTests`), read from the commit being compared with, so a change cannot rewrite its own rules. Flags win.
- **Evidence**: `--sign-key` signs the report, `--badge-out` writes a README badge, `--lock-tests` restores the original tests before they run.

</details>

## What it will not do

- **Prove correctness.** It raises the bar; a check can be wrong in both directions.
- **Replace review or CI.** It runs next to them (and *in* CI with the Action).
- **Send your code anywhere but the checker you choose**: your task and the relevant source files (about 24 KB at most) go to that model. No telemetry.

## Questions

**Isn't this just CI?** CI runs the tests that exist. The pain is the change nobody wrote a test for, or the test the agent deleted or skipped. Apex verify writes the missing checks, proves they can fail, and flags tampering.

**What does it cost?** One model call per task to write the checks (reused while an agent retries), plus a short second look when a check fails: seconds, and cents or a little of your subscription. Your tests run locally.

**What if the checker is wrong?** The table above shows how often. A suspect check is turned into `unknown` by a second look, the hook never blocks more than 3 times, and `APEX_MODE=warn` never blocks.

## Contribute

If it catches something for you, a ⭐ helps others find it. If it gets something wrong, [open an issue](https://github.com/apex-engine-dev/apex-verify/issues/new/choose): we add your case to the benchmark and credit you.

| You can | Where |
|---|---|
| **Send a change Apex verify wrongly blocked** (real examples are what would help most) | [what was tried](benchmark/results/false-alarms-real-libraries), then an issue |
| **Try the OpenAI or Anthropic API checker once** and record what happened | [issue #30](https://github.com/apex-engine-dev/apex-verify/issues/30) |
| **Run the Codex or Cursor hook** inside the real app | a pull request or issue |
| **Add a language or test runner** | issues labelled `good first issue` |
| **Be a second maintainer** | [GOVERNANCE.md](GOVERNANCE.md) |

There is currently **one maintainer**; expect replies in days, not hours.

<details>
<summary><b>What is in this repository</b></summary>

- **[`packages/cli`](packages/cli)**: `apex verify`, the stop hook, the MCP server, the output formats.
- **[`packages/engine`](packages/engine)**: the verification engine (writes and runs the checks, runs your tests, the sandboxes). See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).
- **[`benchmark/`](benchmark)**: labelled AI-written changes, the 12 public projects and 23 real-library tasks, results, and the script that re-measures the gate.
- **`action.yml`, [`integrations/`](integrations), [`.claude-plugin/`](.claude-plugin), [`docker/`](docker)**: the GitHub Action, the Claude Code plugin, the container recipe.
- **[`docs/`](docs)**: [integrations](docs/INTEGRATIONS.md), [what works and how we know](docs/USE-CASES.md), [sandbox](docs/SANDBOX.md), [related work](docs/RELATED-WORK.md), [experiments including failures](docs/EXPERIMENTS.md).

[Contributing](CONTRIBUTING.md) · [Roadmap](ROADMAP.md) · [Security](SECURITY.md) · [Status](docs/STATUS.md) · [Changelog](CHANGELOG.md)

</details>

## Licence

**Apache-2.0**: use it, modify it, ship it, at work or in your own products. The Apex verify name and logo are trademarks, not part of that grant ([TRADEMARKS.md](TRADEMARKS.md)). Contributions use a DCO sign-off (`git commit -s`) and you keep your copyright.
