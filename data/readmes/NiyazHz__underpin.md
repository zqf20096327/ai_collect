<h1>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/images/logo/mark-dark.svg">
    <img src="docs/images/logo/mark-light.svg" alt="" width="36" height="36">
  </picture>
  underpin
</h1>

[![CI](https://github.com/NiyazHz/underpin/actions/workflows/ci.yml/badge.svg)](https://github.com/NiyazHz/underpin/actions/workflows/ci.yml)
**Status: experimental, v0.2.** Data format and CLI may still change.

**Your agent said "the tests pass" on Monday and built on it all week. underpin tells you which conclusions to re-check when
that stops being true.**

AI coding agents build on facts they established earlier ("the tests pass", "the limit is 30 %", "the API returns v2"), and when
the code or a source changes, nobody notices which conclusions just went stale. **underpin is a ledger for those claims:** it
records what each claim rests on (commands, sources, other claims), re-checks that evidence when it goes stale, and shows which
conclusions are shaky when a premise breaks. It works from the command line and plugs into Claude Code via MCP and hooks.

![underpin serve replays a small ledger: claims turn green as evidence comes in, then a retracted exchange rate turns the claims built on it amber; the 2D view shows why](docs/images/replay.gif)

*A small example ledger (a currency converter, ECB rates of 2026-11-03 via frankfurter.dev): the timeline replays how claims get
their evidence, then a reviewer retracts the USD rate (#1) and the cascade travels up to "Release 0.3 can ship".*

## Quickstart

Needs Rust (stable, 1.89 or newer). The web UI is prebuilt and embedded; Node is not needed. Building takes a few minutes.

```sh
cargo install --git https://github.com/NiyazHz/underpin    # or: cargo install --path . in a clone
```

A small project: `discount.txt` holds a discount, and `check.sh` passes as long as it is at most 30. The `cite` step reads the
GitHub API, so it needs network access.

```console
$ mkdir underpin-demo && cd underpin-demo
$ echo 30 > discount.txt
$ printf '#!/bin/sh\n[ "$(cat discount.txt)" -le 30 ]\n' > check.sh
$ chmod +x check.sh
$ underpin init
ledger created: …/underpin-demo/.underpin
$ underpin claim 'The discount is capped at 30 %'
#1
#1    grey  0a13ff57  [unsupported]  The discount is capped at 30 %
$ underpin run '#1' --files discount.txt -- ./check.sh
evidence #2 dae298ac: check passed
#1    green 0a13ff57  [verified]  The discount is capped at 30 %
$ underpin claim 'ripgrep is released under the Unlicense'
#3
#3    grey  b32cbb6d  [unsupported]  ripgrep is released under the Unlicense
$ underpin cite '#3' https://api.github.com/repos/BurntSushi/ripgrep --json-path .license.spdx_id --expiry ttl:30d
evidence #4 be253513: check passed
#3    green b32cbb6d  [verified]  ripgrep is released under the Unlicense
$ underpin claim 'Release 1.2 can ship' --on '#1,#3'
#5
#5    grey  15e2a66c  [unsupported]  Release 1.2 can ship
$ underpin derive '#5' --rule 'discount cap tested, dependency license checked'
evidence #6 c06d1bc4: derivation, no check of its own
#5    green 15e2a66c  [verified]  Release 1.2 can ship
$ underpin status
#1    green 0a13ff57  [verified]  The discount is capped at 30 %
#3    green b32cbb6d  [verified]  ripgrep is released under the Unlicense
#5    green 15e2a66c  [verified]  Release 1.2 can ship
```

Now someone raises the discount:

```console
$ echo 45 > discount.txt
$ underpin status
#1    amber 0a13ff57  [stale]  The discount is capped at 30 %
#3    green b32cbb6d  [verified]  ripgrep is released under the Unlicense
#5    amber 15e2a66c  [at-risk]  Release 1.2 can ship
$ underpin audit --yes
1 evidence considered, 1 checked, 1 failed.
evidence #2 dae298ac: FAIL: exit 1  (files changed since last successful check on 2026-11-03T15:04:51Z: discount.txt)
State changes (1):
#1    red   0a13ff57  [refuted]  The discount is capped at 30 %
$ underpin why '#5'
#5    amber 15e2a66c  [at-risk]  Release 1.2 can ship
  - evidence #6 (derivation: discount cap tested, dependency license checked): follows from the premises (no check of its own)
  depends on:
    #1    red   0a13ff57  [refuted]  The discount is capped at 30 %
      - evidence #2 (command: ./check.sh): check on 2026-11-03T15:04:52Z FAILED, value 1, expected exit 0
      - evidence #2 stale: files changed since last successful check on 2026-11-03T15:04:51Z: discount.txt
```

`audit` exits 0 even when a check fails, as here; with `--strict` it exits 3, for scripts and CI
([exit codes](docs/reference.md#exit-codes)). The hashes are deterministic, the timestamps will be yours.

`underpin serve` starts the read-only web UI; open `http://127.0.0.1:7878` in your browser.

With Claude Code, `underpin init --claude --yes` in your project registers the MCP server and the hooks (project-local files
only; without `--yes` it shows the diff). The agent then records claims as it works, every Bash command is observed, and each
session starts with a summary of what is no longer green. Details: [How it works](docs/how-it-works.md#with-claude-code).

## What the measurements say

What it does and does not do, measured. Every study was preregistered and is reported as it came out
([experiments/](experiments/README.md)):
- **It finds what to re-check, with false alarms.** Replaying 12 weeks of GitHub history under 120 agent conclusions, underpin
  flagged all 20 that flipped, and 40 that still held: 35 % fewer false alarms than re-checking everything, short of the predicted
  half. Partial success, replay only.
- **In a coding session, `audit` clears its own false alarms.** After a deliberate break in a small project an agent had recorded
  10 claims about, nothing was missed and re-running the tests cleared every false alarm; one claim about a command's output
  stayed green, the gap that output matching closes. One session, a case study.
- **Green does not mean true.** In 4,924 agent submissions on SWE-bench Verified (10 models), a flag "evidence not fresh" would
  have caught only 26 % of the 1,410 wrong ones: most had a fresh, green check right before submission. underpin promises
  traceability, not truth.

## Documentation

- [How it works](docs/how-it-works.md): the model, Claude Code integration, web UI, FAQ, roadmap.
- [Reference](docs/reference.md): commands, evidence, expiry, exit codes, files, environment variables.
- [Security model](SECURITY.md): what underpin runs and fetches, and what it does not protect against.
- [Experiments](experiments/README.md) · [Changelog](CHANGELOG.md) · [Contributing](CONTRIBUTING.md)

## Security in short

underpin assumes that the agent and the project are not adversarial; it is not a sandbox. `audit` runs a command only from the
allowlist `.underpin/allow` or after you confirm it, the MCP server runs nothing, `serve` is read-only on 127.0.0.1, and `cite`
via MCP refuses local addresses, also behind redirects. Details and limits: [SECURITY.md](SECURITY.md).

## Limitations

- One user, one machine. No sync, no merge; `#n` is not stable across git branches (hashes are).
- Claims are recorded explicitly. underpin does not extract claims from text and does not guess dependencies; forgotten premises are
  the main weakness.
- underpin sees that a premise changed, not whether the conclusion still holds; derivations cannot be re-run and only turn amber.
  That is the source of the false alarms in demo 1.
- The hook only sees Bash commands. Background commands have no exit code; `cmd || true` reports exit 0.
- A claim that asserts more than its evidence checks stays green. A re-run test is only as good as its run (in demo 2b a stale
  Python bytecode cache first made a break look green).
- An agent records claims only if it decides to. In a first live test (2026-11-03) an agent without any hint recorded none;
  with a hint it recorded eight. With the MCP instructions added after that test, an agent recorded claims without any hint
  (2026-11-05). That is one session, n = 1.
- Checked live with Claude Code: the PostToolUse hook and the MCP server (2026-11-03); the MCP instructions (2026-11-05, one
  session); the SessionStart summary reaches the agent (2026-11-06, one session; it named the refuted and at-risk claims when
  asked). Not yet checked live: the one-line SessionStart notice for the human and the Stop hook's message (only with
  reconstructed inputs), frame rates on a real GPU (only software rendering), the `graph --html` file in a browser.

## How this was built

underpin is the work of its author, Niyaz Huseyn-zada, and of AI agents. The author had the idea and set the scope, preregistered
every measurement before it ran, made every decision (what to build, what to drop, how to score the results) and approved every
push. Claude Code wrote most of the code, ran the experiments and drafted the reports. A coordinating agent session planned the
work and checked it; fresh reviewer agents reviewed the specifications and the release independently.
The agents worked under fixed rules: install nothing system-wide, never push without approval, preregister before looking at
results, and publish negative results too. Commits carry only the author's name; assume agent involvement throughout, as
described here. It was built under the principle it implements: what this README says underpin does is backed by a test or a
script you can run from a clone, what it says was measured by a results file in the repository. The demo 2 evaluation and
demo 2b re-run from a clone as they are; for the other studies, [experiments/README.md](experiments/README.md) lists the data
that is not in the repository, and the few live observations that cannot be re-run say so.

## License

Licensed under either of [Apache License, Version 2.0](LICENSE-APACHE) or [MIT license](LICENSE-MIT) at your option.
The web UI bundles third-party JavaScript packages (React, three.js, Radix UI, lucide and others) under their own licenses, listed
in [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md). The embedded Cytoscape.js 3.30.2 is MIT-licensed, see `vendor/cytoscape/`.
