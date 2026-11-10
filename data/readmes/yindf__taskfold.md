<p align="center">
  <img src="https://raw.githubusercontent.com/yindf/taskfold/master/assets/banner.png" width="100%" alt="taskfold — effectively infinite context for your coding agent" />
</p>

<p align="center"><b>effectively infinite context for your coding agent</b></p>

<p align="center">
  <a href="README.zh.md">简体中文</a> ·
  <a href="https://github.com/yindf/taskfold/releases/latest">Releases</a> ·
  <a href="CHANGELOG.md">Changelog</a>
</p>

<p align="center">
  <a href="https://github.com/yindf/taskfold/releases/latest"><img src="https://img.shields.io/github/v/release/yindf/taskfold?style=flat-square&color=4c8dff" alt="Latest release"></a>
  <a href="https://www.npmjs.com/package/dsh-taskfold"><img src="https://img.shields.io/npm/v/dsh-taskfold?style=flat-square&color=cb3837" alt="npm"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="MIT license"></a>
  <a href="https://github.com/topics/dsh-plugin"><img src="https://img.shields.io/badge/DeepSeek%20Harness-plugin-4c8dff?style=flat-square" alt="DeepSeek Harness plugin"></a>
</p>

**Your agent compacts its own context, as it works.** It wraps each piece of work in a named task, closes it when the work is done, and the closed span becomes one short titled summary — written while that span is still in context, so it is accurate by construction. There is no command to run, and nothing you must manage.

Nothing is thrown away: every fold is archived in full, and `fold_recall` brings any of it back exactly as it was.

For [DeepSeek Harness](https://www.npmjs.com/package/@deepseek-ai/dsh) (DSH).

> **Latest supported dsh: `0.2.2-rc.1`.** dsh rc builds are supported on this branch; dsh alpha builds are supported on the [`alpha` branch](https://github.com/yindf/taskfold/blob/alpha/README.md#supported-dsh-versions).

## What it does

Long sessions drown in their own history: every request re-sends hours of finished work — old tool outputs, debug logs, abandoned attempts. Costs climb, the model gets distracted, and the window eventually fills.

taskfold takes finished work off the surface at the moment it finishes:

```
task_begin("fix the login bug")   … the work …   task_end("fix the login bug")

→  "fix the login bug" — one titled summary: what was tried, what failed and why,
   what changed, what the user decided
```

The agent opens a task before starting and closes it when done. Closing **is** the fold: the span collapses into that summary, and the original messages are archived untouched.

## Autonomous compaction

The agent compacts on its own initiative, at task boundaries — not when a token counter decides the window is nearly full. That is the difference from dsh's built-in compaction, and the two compose:

| | dsh built-in compaction | taskfold |
| --- | --- | --- |
| Trigger | token pressure | the agent, at each task boundary |
| Fires when | the window is nearly full | the work is finished |
| Summary written | from history that has already gone stale | while the span is still in context |
| Scope | a token-sized range | one named task, with a title |
| Reading the original | re-summarized | `fold_recall({ fold: N })` returns the exact messages |
| Context window | fills until it fires | rarely fills, so it fires later or not at all |

- **Accurate by construction.** The summary is written once, while the span it describes is still in context — never a summary of a summary.
- **Navigable.** Every fold carries a title, so a long session stays scannable.
- **Cache-friendly.** Folding rewrites a middle chunk of history; the stable prefix (system prompt, tools, earlier context) stays cache-friendly.
- **Guardrails, not noise.** If the agent forgets the discipline, a short hint appears in its context. Hints are events, not state: one is published when the condition appears or its wording changes, nothing is published once it clears, and there is no wrapper, supersession header or expiry notice.

## What it saves (measured)

One real session — 411 model steps, 26 folds — read from the harness's own usage records:

| | Without folding | With taskfold |
| --- | --- | --- |
| Total prompt tokens | 142,654,308 | 52,127,098 (**−63.5%**) |
| Largest single request | 594,909 | 206,896 (−65%) |
| Context window used at peak | 59.5% | 20.7% |

- Folding moved **441,100 tokens** of finished work off the surface; because that history would otherwise be re-sent on every later request, it added up to **90,527,210 tokens never sent**.
- Producing the 26 summaries cost 3,550,270 tokens — 3.9% of the saving, and most of it cache reads.
- The biggest single fold took 40,422 tokens out of the conversation in one call.

Most of those tokens would have been cache *reads* rather than fresh input — cheaper, but still billed and still occupying the window. In longer sessions that is the difference between staying inside the context window and not.

One session, one task shape — your numbers will differ. The mechanism is the point: finished work leaves the surface, the stable prefix stays cached, and the model keeps the lessons instead of the transcript.

## Install

### dsh Desktop (recommended)

1. Open dsh Desktop and go to the **Plugins** page in the sidebar.
2. Click **Add plugin** in the top-right corner.
3. In **Package name or address**, enter `dsh-taskfold`. The dialog runs pnpm for you:
   - **want the newest release the moment it ships?** pin it — `dsh-taskfold@<version>` from the [versions list](https://www.npmjs.com/package/dsh-taskfold?activeTab=versions). pnpm 11 (bundled with dsh Desktop) leaves a release younger than 24 h out of the bare name's reach, and an explicit version overrides that; pnpm records it in the profile's `minimumReleaseAgeExclude` too. Never install **0.37.7** or **0.38.0** — uninstallable (`ERR_PNPM_LINKED_PKG_DIR_NOT_FOUND`) and deprecated on npm;
   - **skip npm entirely:** paste the prebuilt `.tgz` from the [newest Release](https://github.com/yindf/taskfold/releases/latest) — a tarball is not subject to the release-age policy;
   - **follow a branch:** `github:yindf/taskfold#master` (rc channel) or `github:yindf/taskfold#alpha` (alpha channel) — needs direct GitHub access from this machine;
   - a **local path** must point at a *copy*, never at your working checkout: the plugin manager treats whatever it installs as its own (it leaves `dsh-taskfold.frozen-*.bak` snapshots beside it and replaces the directory on upgrade).
4. Leave **Registry** on **Default registry**; mainland-China networks can pick **Mainland China mirror** and retry.
5. Click **Install**, wait for "Installed; it loads at the next start.", then click **Enable now**.
6. **Restart dsh Desktop** — plugin composition is evaluated only at startup. Back on the Plugins page you should see a **Taskfold** card reading *Components · 2 total · 2 running* (`taskfold` and `taskfold-client`); the fold floor and the task-bar switch live on that card (see [Settings](#settings)).
7. To upgrade, **uninstall** and install the new version — the dialog states that automatic updates are not supported yet, and uninstalling takes its features away.

The dialog writes the dependency and the bundle entry into the active profile (`desktop` for dsh Desktop); nothing else needs configuring by hand.

### Command line

`dsh plugin --profile <name> add` is the shell equivalent of the dialog. `desktop` is dsh Desktop's profile and `web` is the DSH Web GUI's — use whichever one you actually run:

```sh
# the newest npm release
dsh plugin --profile desktop add dsh-taskfold

# a pinned version — required while the release is younger than 24 h; 0.37.7/0.38.0 cannot be installed
dsh plugin --profile desktop add dsh-taskfold@<version>

# a channel branch (keep the quotes: # starts a comment in sh)
dsh plugin --profile web add "github:yindf/taskfold#master"
dsh plugin --profile web add "github:yindf/taskfold#alpha"
```

Whichever way you install, restart dsh afterwards: every session on that profile then gets the tools.

### Channels, the npm package, and release assets

- [`dsh-taskfold`](https://www.npmjs.com/package/dsh-taskfold) on npm is a **prebuilt** package — it skips dsh's `allowBuilds` build approval.
- Since 0.37.6 the release pipeline publishes to npm for the **rc channel** (`master`) only: alpha-channel releases ship as GitHub Releases and never reach npm. The bare package name therefore follows the rc channel's newest release — pin `@version` for determinism, or enter the branch's Git address.
- **Channel branches:** `master` carries the rc channel, `alpha` carries the alpha channel. This branch records the rc channel's support range (see [Supported dsh versions](#supported-dsh-versions)); the alpha channel's record lives on the [alpha branch](https://github.com/yindf/taskfold/blob/alpha/README.md#supported-dsh-versions).
- Every release attaches a prebuilt `dsh-taskfold-<version>.tgz`. Plugin storefronts offer that asset — or the npm package — instead of the build-from-source command, which also skips dsh's `allowBuilds` approval step. See the [latest release](https://github.com/yindf/taskfold/releases/latest).

## Tools

Four agent tools (plus the hints above):

| Tool | One-liner |
| --- | --- |
| `task_begin({ name })` | Open a named task. |
| `task_end({ name })` | Close it and fold its whole span into one titled summary. |
| `list_folds` | List all folds (number, size, title). |
| `fold_recall({ fold })` | Bring back any fold's original content on demand. |

- Open tasks survive restarts; closing is well-ordered (innermost first), and a failed close never corrupts anything — just retry.
- Summaries are instructed to preserve user decisions and feedback (verbatim where wording matters), pitfalls and *why* things failed, what changed, and the outcome.

In the Web GUI, the current open-task stack can also show as a live dock above the composer (like the todo panel) — hidden by default, switched on with `showTaskBar` on the Plugins page: outermost first, the innermost task highlighted, with the closing/pending counts — read straight from the session's `taskMarks` projection, no extra events.

<img src="https://raw.githubusercontent.com/yindf/taskfold/master/assets/screenshot-tasks.png" width="100%" alt="the live task stack, docked above the composer: nested open tasks with the innermost highlighted, and one folding row per task that has already ended">

<img src="https://raw.githubusercontent.com/yindf/taskfold/master/assets/screenshot-tasks-collapsed.png" width="100%" alt="the same stack collapsed to one line, next to the task-stack line the lifecycle hint hands to the model">

## Settings

Two settings, on the host's **Plugins page** as a "Taskfold" card (the browser half registers it while the host serves the taskfold namespace — no environment variables, no restart):

| Setting | Default | Accepted | What it does |
| --- | --- | --- | --- |
| `minSpanTokens` | `2000` | integer `0`–`1000000` | Minimum estimated tokens a closed task's span must carry before it is worth a summarization call. |
| `showTaskBar` | `false` | on / off | Shows the task-stack dock beside the conversation input. |

**`minSpanTokens`** counts a CJK-aware character heuristic over the span's message text before any model call — its rate constants are calibrated against measured `shadowedTokenCount` values, and estimates read ~7% low, a conservative direction. Edits are validated by the form's schema, persisted in the active profile's config, and applied **live**: the next close (or fallback settle) judges under the new floor.

- **Below the floor a span closes unfolded — permanently.** The verdict is made at close time and recorded in the `Task ended` result itself (0.37.6): the span never enters the archival queue, so no reopen path exists. Retro-folding settled spans would rewrite the surface and invalidate the provider prefix cache behind them, a cost no small fold can repay.
- **Edge cases.** `0` folds everything; an unmeasurable span always folds; a value that is not a usable number (non-integer, negative) falls back to the default instead of throwing, and the form blocks a save outside `0`–`1000000`.
- **Closes that carry other tool calls** — their partner results have not landed when `task_end` executes — fall back to drain-time, in-memory settling, re-measured after a restart.
- **Why 2000:** measured over two weeks of session logs, a summary call's fixed overhead makes spans under ~1000 tokens a net loss, and 2000 keeps a 2× margin. Derivation in [docs/fold-floor.md](docs/fold-floor.md).

**`showTaskBar`** is hidden by default, so a fresh profile carries no dock until it is switched on; showing or hiding it does not affect folding. The one visible fallback is deliberate: an unserved namespace or a missing settings service still means visible, because the dock's registration never depends on settings to render.

## Supported dsh versions

Re-verified against `@deepseek-ai/dsh-app-boot@0.2.2-rc.1` by reading the host's own sources — this was a minor step with real host-surface movement, so the surface was re-read rather than assumed:

| What was checked | Result |
| --- | --- |
| Compatibility gate | `semver.satisfies(runtimeVersion, range, { includePrerelease: true })` — `lib/index.js:1095`, real `semver` 7.8.6. That option is what admits this host: a 0.2.x prerelease is allowed anywhere inside the caret's `<0.3.0-0` bound; without it node-semver's same-tuple prerelease rule would reject it. |
| `peerDependencies` | `@deepseek-ai/dsh`, `@deepseek-ai/dsh-compaction-basic`, `@deepseek-ai/dsh-llm` — all `^0.2.0-rc.1`, all unmet-free, gate returns `undefined`. The manifest declares no `engines`. |
| Host APIs the plugin binds | **27/27 present, 0 absent** — 7 services, 3 hooks, 6 methods, the `BasicCompactionEngine` subclass contract, `BlockAssembler`, schemastery's CJS chain, both gate exports. |
| Client contracts | **16/16 present** — `conversation.input.dock`, `plugins.bundle.config`, `slots.inject`/`register`, `configForms`/`whileServed`, `window.__ModuleLoader__`, `ctx.provide("locale", …)`. `@deepseek-ai/dsh-client-ui-primitives` is shell-inlined, so a filesystem check for it is a false negative. |
| The live host | It boots the published `dsh-taskfold@0.40.1` — the same version as this checkout, whose installed client bundle matched it at all 28 anchors across the same 753 lines. A rejected row would be dropped with `disabling profile plugin …`, so the running row is the gate's own verdict; no `compatibility.json` exemption exists anywhere under `~/.dsh`. |
| Non-lockstep neighbours | `schemastery` `3.18.5` → `3.19.0`; `@deepseek-ai/cordis` `4.0.5` → `4.1.0`. |
| Drift found | Deprecation, not breakage: `sessionProjections.register()` is now a legacy wrapper over `acquire()`, which requires an integer `stateVersion` (0.40.1 declares `stateVersion: 11`); `stateOf()` logs one deprecation warning per key from three call sites. |
| Not re-run | The rc.5 probe battery — shape battery, gate script, e2e probe host, 239-test offline suite. This environment had no usable shell (no node/npm/git), so the record rests on source reads plus the live host. |

- **rc channel — supported through `0.2.2-rc.1`** (verified 2026-11-07). Desktop payload: `@deepseek-ai/dsh-desktop-runtime@0.2.2-rc.1` (`desktopVersion` in its runtime manifest).
- **alpha channel — use the `#alpha` install** (`dsh plugin --profile web add "github:yindf/taskfold#alpha"`, the alpha branch); the alpha build's supported-version record lives in [the alpha branch's README](https://github.com/yindf/taskfold/blob/alpha/README.md#supported-dsh-versions).
- **Bounds: enforced floor, untested ceiling.** The plugin declares its host surface in `peerDependencies` (`^0.2.0-rc.1`): dsh 0.2.0+ hosts check those ranges at install and at startup/recomposition, so an incompatible host now gets the bundle skipped with an `incompatible-version` verdict instead of loading it — 0.1.7-rc.* hosts should install v0.37.0, whose `^0.1.7-rc.1` floor matches them. Hosts older than the check itself negotiate nothing — on those, folds degrade (tasks still close, unfolded) rather than corrupt. After each dsh upgrade, re-check this section and update it with test results.
- **Optional hook: `agent/turn-stopping`** — since 0.26.0 the archive drain also runs at turn end, folding turn-final deliverables while the provider prefix cache is still hot. Hosts without the hook simply keep the previous pre-step-only semantics (folds still happen, one turn later); the registration is wrapped so its absence never breaks `apply()`.

## For maintainers

**Layout**

- `plugins/` — ONE mounted host row, `taskfold.mjs`, mounted as the package subpath `dsh-taskfold/plugins`. The bundle patch declares one host component, so the Plugins page shows two rows: this one and the client row, which is mounted by its own component package name `dsh-taskfold-client`. `compact-stats.mjs` is a plain module imported by the row, not a row.
- `plugins/` shared plain modules — `events.mjs`, `task-marks.mjs`, `fold-instruction.mjs`, `fold-engine.mjs`, `fold-drain.mjs`, `fold-settings.mjs`, `lifecycle-nudges.mjs`, `lifecycle-injection.mjs`, `span-preview.mjs`; browser half: `task-stack-ui.mjs` (the dock's source of truth) and `fold-settings-ui.mjs` (the Plugins-page settings card), both generated into `client/taskfold-client.mjs` by `scripts/build-client.mjs`.
- `client/` — the nested `dsh-taskfold-client` package, owning the browser bundle. A client package may have exactly ONE owning Loader row, and the host half already owns the root package row. It is **published as its own npm package**, and the root declares it under `dependencies` as a registry version range, so dsh-app-boot's dependency closure publishes the name, the row mounts the bare name instead of a `file:///` path, and a consumer's pnpm can install it — a `file:`/`link:` specifier is resolved against the INSTALLER's workspace root, never against this package, which is why 0.38.0 could not be installed at all.
- `scripts/` — `release.mjs`, `verify-cache.mjs`, `build-client.mjs`; `test/` (`npm test`); `assets/` (README banner, the social-preview image to upload in repo settings, and the store screenshots listed in `screenshots.json`); `docs/` (`docs/README.md` index plus the `docs/design/` notes and `docs/adr/` decisions — deliberately kept out of the npm package); `CHANGELOG.md`.

**Localization**

- Every user-facing surface ships English and Simplified Chinese. The settings card resolves its copy through the host's locale service (dictionary `settings.taskfold`).
- The dock's registration deliberately carries no locale requirement — the bundle wires a locale-bound reader for dictionary `ui.taskfold` while the locale service is available, and prints its built-in English copy otherwise, so it renders on every deployment.
- The package exports `locale/en.json` + `locale/zh.json` (the package page header and the npm listing) plus one row locale per mounted component: `plugins/locale/*.json` for the host row, reached through the subpath it mounts (`dsh-taskfold/plugins`), and `client/locale/*.json` for the client row, reached through its own package name. The Plugins page therefore shows each row's title and one-line introduction in the active language instead of the English `package.json` fallback.
- Both row titles deliberately differ from their row id and their module name: `client.js` prints the id only when the title differs from it and the module name only when the title differs from that, so each row renders the same four lines the official bundles' rows use — title, introduction, row id, module name. The client half's `package.json` still carries no description, so a row introduction can only ever come from its locale file.

**Releasing**

- `node scripts/release.mjs draft` → review the CHANGELOG entry → `node scripts/release.mjs release`. CHANGELOG is the single source of truth for versions.
- `release` (and its PENDING resume) also publishes to npm when the `NPM_TOKEN` environment variable is set — an **automation-type** token, because 2FA accounts reject publish-time OTPs for granular tokens. The step is idempotent (a version already on the registry is a no-op) and its failure never rolls back the git-side release; the token comes from the process environment or, on Windows, the user-level variable.
- If that step was skipped or failed, `node scripts/release.mjs npm [--version X.Y.Z]` (re)publishes an already-released version on its own — it refuses unless `package.json`, the local `v<version>` tag, a clean tree and a tree identical to that tag all say this checkout really is that release.
- **Two packages publish, and the client goes FIRST**: the root's manifest names `dsh-taskfold-client`'s version, so a root published ahead of its client would 404 for every consumer until the client landed (each package is probed and published on its own, so a re-run finishes whichever half is missing). Before publishing, `assertClientDependencyResolvable` refuses a client dependency that is not a registry version range — a `file:`/`link:`/`workspace:` specifier is resolved against the CONSUMER's workspace root and makes every install fail, which is exactly what 0.38.0 shipped.
- **Channel branches** (since 0.34.6): `master` carries only rc-channel releases — it stays at the newest verified-rc version; alpha-channel releases happen on the `alpha` branch, whose commits and tags carry the alpha-verified work (run draft/release ON the `alpha` branch; the script pushes the current branch and the tag).
- If a release changes which dsh versions are supported, update the "Supported dsh versions" section in **both** READMEs (README.md + README.zh.md) before releasing — the release script reminds you. Each branch records only what was verified **on that branch**: one newest verified version for its own channel (superseded entries are deleted), and a **link** to the other branch's README for the other channel — never a copied version number.

**Fold cache verification is part of the flow.** After every dsh upgrade — and before any release that touches the fold envelope — run `node scripts/verify-cache.mjs --since-restart` against a live session log, and record the numbers in the CHANGELOG entry. It exits non-zero when a fold's summarizer call re-pays its span — the test is `uncached − span > --tail-budget`, i.e. a positive tail, the signature of the prefix envelope no longer matching the host's summarization input. The offline suite pins the structural precondition (one system message, strict prefix); only a live log can show the actual cache read.

Design decisions and history live in `CHANGELOG.md` and in `docs/` (`docs/README.md` is the index; the `docs/design/` notes and `docs/adr/` decisions ship with the repo, not with the npm package).

## If this saves you tokens

A star helps other dsh users find it — in this ecosystem, that is how a plugin gets discovered. Numbers from your own sessions are welcome in [Discussions](https://github.com/yindf/taskfold/discussions).

## License

MIT. Developed against the DeepSeek Harness (`@deepseek-ai/*`, MIT) public packages.
