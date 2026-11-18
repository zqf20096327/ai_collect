# LocalSutra AI

> **Know your hardware. Choose your model. Keep AI local.**

[![CI](https://github.com/shahvatsalofficial/localsutra-ai/actions/workflows/ci.yml/badge.svg)](https://github.com/shahvatsalofficial/localsutra-ai/actions/workflows/ci.yml)
[![npm](https://img.shields.io/npm/v/localsutra-ai)](https://www.npmjs.com/package/localsutra-ai)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)
![Dependencies: 0](https://img.shields.io/badge/runtime%20dependencies-0-brightgreen)
![Node >=22](https://img.shields.io/badge/node-%3E%3D22-339933)

**Website:** [shahvatsalofficial.github.io/localsutra-ai](https://shahvatsalofficial.github.io/localsutra-ai/) · **npm:** [localsutra-ai](https://www.npmjs.com/package/localsutra-ai)

**LocalSutra AI** is an offline-first command-line tool that answers the questions people ask before running an LLM on their own machine: *Can my computer run this model? Why does it (not) fit? Is my Ollama or llama.cpp server really local? How fast is it on my hardware? What does the report actually prove?*

It needs **no API key, no account and no network** (the only network calls are explicit requests to a service on `127.0.0.1`). It has **zero npm dependencies**. Every result states whether it is *measured*, *estimated*, *reported by the runtime*, *not run* or *unknown*, so you never mistake a guess for a benchmark.

It also ships **25 portable Agent Skills** (`SKILL.md`) for Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot and OpenCode, and an **independent audit command** that runs 37 adversarial checks against its own safety rules and writes the result as **HTML, Markdown and JSON**.

## Quick start

```bash
npx localsutra-ai doctor                       # hardware profile: OS, CPU, RAM, free disk, NVIDIA GPU if nvidia-smi exists
npx localsutra-ai audit --out my-audit         # independent audit -> my-audit/audit-report.html (+ .md, .json)
```

Install globally if you prefer: `npm install -g localsutra-ai`, then use `localsutra` (alias `localsutra-ai`). Requires Node.js 22+ (Node 20 reached end of life in April 2026).

## What it does

| Command | What you get | Honest label |
|---|---|---|
| `doctor` | OS, architecture, WSL flag, CPU, RAM total/free, free disk, NVIDIA GPU name/VRAM/driver (via `nvidia-smi`), tools on PATH | Measured. AMD/Intel/Apple GPUs and NPUs are reported **unknown**, not absent |
| `fit --catalog FILE` | Per-model memory estimate: weights, KV cache, overhead, RAM fit, single-GPU VRAM fit | **Heuristic**, never a promise. Speed and quality are `unknown` |
| `probe --runtime ollama\|llama` | Is a loopback Ollama/llama.cpp server up, which models are listed, stable failure codes | Service health only. Inference is *not tested* |
| `infer --model NAME` | Opt-in timing of a real, already-installed Ollama model (cold vs warm runs, runtime-reported tokens/s) | Prompt and output text are **never stored** (hash only) |
| `benchmark` | Synthetic CPU loop with median, p95, stdev | Explicitly **not AI inference** |
| `compare --a --b` | Ratio of two benchmark reports, only if workload and platform match | Refuses unlike inputs |
| `privacy` | Endpoint rule check and a data inventory (what is collected, where, retention) | Does **not** prove an external runtime has no egress |
| `audit` | 37 adversarial checks, sample outputs, evidence tiers, a not-tested list | Verdict `APPROVED_WITH_EVIDENCE`, `REVIEW_REQUIRED` or `BLOCKED_UNSAFE` |
| `verify --report FILE` | Checks a report's SHA-256 seal | Detects change, **not** who made it |
| `install-skills` | Copies the 25 skills into a project for six IDE layouts (`--dry-run` supported) | File placement verified; native activation is **not** claimed |
| `serve` | Read-only `127.0.0.1` API for one sealed report, bearer-token protected | Not a production service |

All report commands accept `--out FILE` (writes `.json`, `.md` and `.html`; refuses to overwrite unless `--force`) or `--format json|md|html` for printing.

## Example: will these models fit?

```text
$ localsutra fit --catalog fixtures/model-catalog.json --format md

| Model         | Params | Bits | Weights GB | Required GB | Free RAM GB | RAM fit                 | VRAM          |
|---------------|--------|------|-----------:|------------:|------------:|-------------------------|---------------|
| EXAMPLE-3B-Q4 | 3B     | 4    | 1.50       | 3.13        | 6.28        | possibly_fits           | not_evaluated |
| EXAMPLE-7B-Q4 | 7B     | 4    | 3.50       | 6.23        | 6.28        | possibly_fits           | not_evaluated |
| EXAMPLE-8B-Q8 | 8B     | 8    | 8.00       | 12.80       | 6.28        | likely_insufficient_ram | not_evaluated |
```

The formula is `weights x 1.35 + overhead + KV cache`. The 1.35 headroom and the overhead are **assumptions**, printed in every report. The catalog descriptors are synthetic examples, not endorsed downloads.

## Proof, not promises

| Evidence | Where |
|---|---|
| 126 automated tests, 0 failed, 0 skipped on the recorded run | [`docs/proof/test-run.tap`](docs/proof/test-run.tap) |
| 9,500 seeded hostile inputs, 0 unexpected crashes | [`docs/proof/fuzz-results.json`](docs/proof/fuzz-results.json) |
| A real audit report (HTML, Markdown, JSON) | [`docs/proof/audit-sample/`](docs/proof/audit-sample/) |
| Raw CLI transcripts | [`docs/proof/`](docs/proof/) |
| SHA-256 of every proof file | [`docs/proof/SHA256SUMS.txt`](docs/proof/SHA256SUMS.txt) |
| CI matrix on Linux, Windows, macOS (Node 22/24) | [GitHub Actions](https://github.com/shahvatsalofficial/localsutra-ai/actions) |

Reproduce everything yourself: `npm test`, `npm run proof`, `npm run audit`. The audit report lists what it did **not** test: live inference on a real model, non-NVIDIA GPUs, native IDE skill activation, external-runtime network egress, and independent third-party review.

## Safety model

- **Loopback only.** Endpoints must be `http://127.0.0.1:PORT/` or `http://[::1]:PORT/`: no credentials, path, query, redirects, `localhost`, public hosts or `0.0.0.0`. Blocked endpoints never reach the network layer.
- **Bounded.** Timeouts, a 256 KB response cap, run/iteration/catalog limits, 1 MB JSON import cap.
- **Read-only by default.** No installs, downloads, driver changes, open ports or telemetry. `serve` binds `127.0.0.1` only and needs a 24+ character token.
- **Create-only outputs.** Reports and installed skills never overwrite existing files; installers refuse symlinked paths.
- **No fabricated results.** No GPU is invented, no token/s without a runtime counter, no "private/secure/air-gapped" claim without external proof.

Details: [`docs/THREAT_MODEL.md`](docs/THREAT_MODEL.md), [`SECURITY.md`](SECURITY.md), [`docs/LEGAL_AND_TRUST.md`](docs/LEGAL_AND_TRUST.md).

## Agent Skills

`skills/` holds 25 portable skills (a Prime orchestrator, 19 specialists and 5 capability skills such as `localsutra-model-fit`). Copy them into a project:

```bash
localsutra install-skills --project . --ide claude --dry-run   # preview
localsutra install-skills --project . --ide claude              # claude | cursor | codex | gemini | copilot | opencode
```

Skills are instructions for your coding agent, not running processes. The CLI works without any agent. Native discovery inside each IDE is **not** verified by this project.

## Documentation

Full documentation set (executive, functional, architecture, technical, user guide, security, evidence, test report, operations, legal, roadmap, glossary, assurance) lives in [`documents/`](documents/) with a designed HTML edition at `documents/html/index.html`. Repository docs: [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md), [`docs/STATUS.md`](docs/STATUS.md), [`docs/AUDIT_REPORTS.md`](docs/AUDIT_REPORTS.md), [`docs/EVIDENCE_MODEL.md`](docs/EVIDENCE_MODEL.md), [`ROADMAP.md`](ROADMAP.md).

## FAQ

**Can my computer run a 7B or 13B model?** `localsutra fit` gives an approximate memory answer with its assumptions shown. For a real answer, load the model in Ollama or llama.cpp, then use `infer`.
**Does it send my hardware profile anywhere?** No. There is no telemetry and no network access beyond the loopback requests you ask for.
**Is this a benchmark leaderboard?** No. It will not rank models across unlike hardware, context lengths or quantizations.
**Does it download models or install Ollama?** No. It never installs or pulls anything.

## Contributing, support, license

See [CONTRIBUTING.md](CONTRIBUTING.md), [SUPPORT.md](SUPPORT.md), [GOVERNANCE.md](GOVERNANCE.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Licensed under [Apache-2.0](LICENSE); see [NOTICE](NOTICE). Created by **Vatsal Shah**. Third-party names (Ollama, llama.cpp, NVIDIA, Claude, Cursor, Codex, Gemini, GitHub Copilot, OpenCode, Node.js, npm) belong to their owners and are used only to describe compatibility; no affiliation is implied. The name "LocalSutra" has not been trademark-cleared.

If you use this software in research, cite it via [CITATION.cff](CITATION.cff).
