# ZLoop — a lab for ZCode Desktop

Session-scoped programmatic history, a persistent IPython kernel, and an
evidence-backed research loop for [ZCode Desktop](https://zcode.z.ai), built as a
thin plugin on top of the official runtime — plus the lab harness used to develop
and verify it.

This repository is the **ZLoop lab**. It contains the installable plugin, the
documentation that records what was actually measured, the canary that gates
version switches, and the two independent research packages the design was built
from.

> **Status: experimental, single-machine, Windows-first.** Everything here was
> developed against ZCode Desktop 3.12.3 on one Windows machine. `zloop/docs/ACCEPTANCE.json`
> records 67 acceptance items with per-item evidence, including the ones that
> **failed** or were **never run**. Read it before trusting any capability claim.
> Nothing marked `NOT_RUN` in that ledger is claimed as working.

## What ZLoop adds

The plugin adds three capabilities the host lacks, and deliberately nothing else:

1. **Programmatic history** — search earlier conversation content by exact string,
   read a window around a hit, and find workspace checkpoints. Read-only: the
   official session database is opened `mode=ro` and is never written, migrated,
   or repaired.
2. **Persistent IPython** — a real Jupyter kernel that keeps variables, functions
   and large objects alive across cells, across tool calls, and — from a snapshot —
   across restarts. Restore reports what it could not recover rather than hiding
   the loss.
3. **Evidence-backed research** — a session-scoped loop that archives what was
   actually fetched and refuses a decision written before its observation
   returned. A search snippet is a pointer; only an archived original counts as a
   read.

Plus bookkeeping tools that make verification honest: receipts that go stale when
the code changes, and effect records that separate "did the call finish" from "did
the world change".

**Not included, deliberately:** no hooks, no context compressor, no second agent
loop or model call, no semantic search, no trajectory manager, no memory product.

## Repository layout

```
zloop/                       the plugin and its lab harness
├─ README.md                 the main document: capabilities, config, tool surface, status
├─ canary.py                 behaviour gate run before switching ZCode versions (990 lines)
├─ marketplace.json          local marketplace pointing at ./plugin
├─ docs/                     the measured record — see "Documentation" below
├─ plugin/                   the installable ZCode plugin (self-contained)
│  ├─ .zcode-plugin/plugin.json    name, version, userConfig
│  ├─ .mcp.json                    the stdio MCP server definition
│  ├─ commands/                    /react-start, /react-status
│  ├─ skills/evidence-react/       the model-facing evidence-loop policy
│  └─ runtime/                     Python package (src/zloop/, tests/)
└─ vendor-patches/           pristine upstream bridge kept for diffing + attribution

reference/                   independent research packages this work was built from
├─ zcode-harness-audit-20260918/     audit + execution plan (14 findings, P0–P7)
└─ zcode-react-research-20260918/    ReAct control model, schema, prompts, tests

zcode-version.cmd            version manager: list / canary / switch / rollback / stage
launch-zloop-lab.cmd         isolated launcher (separate HOME, data root, plugin dir)
fix-zcode-registry.cmd       restores the live install as owner of the zcode:// scheme
```

## Requirements

- **Windows 10/11 x64** — the launcher, version manager and canary are `.cmd`
  scripts and the isolation mechanism relies on Windows environment variables.
- **ZCode Desktop** installed separately. Not included here.
- **Python 3.11+** for the plugin runtime. The plugin's dependencies are declared
  in `zloop/plugin/runtime/pyproject.toml` (`mcp`, `jupyter_client`, `ipykernel`,
  `pyzmq`, `cloudpickle`, `dill`, `httpx`, `lxml`, `readability-lxml`).
  No virtualenv or lockfile is shipped — create one and point the plugin's
  `python` userConfig field at it.

## Installing the plugin

1. Create a Python environment and install the runtime:
   ```
   cd zloop\plugin\runtime
   python -m venv .venv
   .venv\Scripts\python -m pip install -e .
   ```
2. Point ZCode at the local marketplace in `zloop/marketplace.json`, or add the
   plugin directory directly via `plugins.dirs`.
3. Set the plugin's **Python interpreter** userConfig field to the interpreter you
   just created. No default is shipped, because the correct path is machine-specific.
4. Optionally set `data_root` to a directory **outside** the plugin directory, so
   snapshots and receipts survive a plugin reinstall.

## The lab harness

`zloop/` is developed inside a versioned lab rather than in the live install:

```
E:\zcode-labs\
├─ zcode-version.cmd         version manager
├─ current ──junction──> versions\3.12.3
├─ versions\3.12.3\          a full ZCode build, one per version
├─ zloop\                    ZLoop source (outside the app directory)
├─ zloop-data\               all runtime data (outside the app directory)
└─ zloop-home\               isolated HOME
```

Because the data root and the isolated `HOME` live **outside** the app directory,
switching or rolling back a ZCode version never touches ZLoop state. The paths
above are the lab's own convention; `zcode-version.cmd` has `ROOT` at the top if
you want to relocate the tree.

`canary.py` is the gate: it probes the eight host interfaces ZLoop depends on
using **live behaviour** rather than version numbers or schema fingerprints, on the
reasoning that an interface can keep its name and change semantics. It exits
non-zero when a check fails, and `switch` aborts on that code. `docs/CANARY_GAPS.md`
is its own adversarial review and lists what a green canary still does not prove.

## Documentation

The `zloop/docs/` set is a measured record, not marketing. Every claim carries a
receipt, and claims that could not be verified are labelled rather than omitted.

| Document | What it covers |
|---|---|
| `ACCEPTANCE.json` | 67 acceptance items with per-item evidence and status |
| `RESEARCH.md` | the research layer: provenance, SSRF model, rejection codes, divergences |
| `UPSTREAM_DEFECTS.md` | 13 confirmed upstream defects, 3 **refuted** claims, known limitations |
| `CANARY_GAPS.md` | adversarial review of the canary: what it cannot see |
| `ISOLATION.md` | the isolation variables, each measured |
| `IPYTHON_GUIDE.md` | the snapshot/restore contract and its limits |
| `HISTORY_GUIDE.md` | the trust model for history: "coordinates are trustworthy, text is not" |
| `IDENTITY.md` | what the session-identity claim actually means, and what it does not |
| `DEPENDENCIES.md` | 6 hard vs 8 silent host dependencies |
| `UPGRADE.md` | the switch/rollback runbook |
| `LAYOUT.md` | the on-disk tree, measured |
| `HANDOFF.md` | state of play for a new contributor |

## Verifying it

The test suites are **script-style, not pytest-style**: each file is a standalone
program with its own `record()` PASS/FAIL/SKIP printer. Run them directly with the
plugin's interpreter, from `zloop/plugin/runtime`:

```
set PYTHONPATH=src
.venv\Scripts\python -X utf8 tests\test_lanes.py
.venv\Scripts\python -X utf8 tests\test_gate_adversarial.py
.venv\Scripts\python -X utf8 tests\test_bridge_fixes.py
.venv\Scripts\python -X utf8 tests\test_lane_verdict.py
.venv\Scripts\python -X utf8 tests\test_interrupt_no_deadlock.py
```

Offline suites (no network, no live session database) and their most recent
observed results on the development machine:

| Suite | Checks |
|---|---|
| `test_lanes.py` | 108/108 passed |
| `test_gate_adversarial.py` | 15 adversarial rows, 11 BLOCKED / 3 expected-limitation / 1 nit |
| `test_bridge_fixes.py` | 17/17 passed |
| `test_lane_verdict.py` | 6/6 passed |
| `test_interrupt_no_deadlock.py` | PASS, no orphan kernel |

Two further suites — `test_e2e.py` and `test_mcp_stdio.py` — require a live ZCode
session database and are not runnable from a fresh clone. They default to a lab
path, not to your personal ZCode data. `test_mcp_stdio.py` and
`test_research_stdio.py` also need the `mcp` package, so they only run under the
plugin's own interpreter, not a bare system Python.

The reference package `reference/zcode-react-research-20260918/` ships a normal
unittest suite and is self-contained:

```
cd reference\zcode-react-research-20260918
python -m unittest discover -s tests      # 22 tests, OK
```

## Honest limitations

These are recorded in the ledger and repeated here so they are not missed:

- **Multi-window contention is unresolved.** Two ZCode windows on one session are
  two MCP processes with two independent registries. A cross-process `SessionLease`
  is implemented and now wired into the kernel start path, but the end-to-end
  desktop case has **not been re-measured** since, so the item stays `FAIL`.
- **No real web search has ever been exercised.** Every search test uses the stub
  provider; no search endpoint was reachable during development.
- **The upgrade path has never been run against a real newer ZCode build.**
- **`text_complete: true` does not mean the text is complete.** The field is
  declared as always-`True` and no code path ever assigns `False`.
- **This is not a sandbox.** The lab runs as the same OS user as the live install.
- **The gate validates structure and timing, not truth.** A model can write a
  long-but-empty memo that satisfies the research gate.
- **The vendored bridge is third-party code.** See `zloop/vendor-patches/README.md`
  for upstream, commit, hash and license.

## License

MIT — see [LICENSE](LICENSE). The vendored upstream file in
`zloop/vendor-patches/` is MIT-licensed third-party code and is attributed in
`zloop/vendor-patches/README.md`.
