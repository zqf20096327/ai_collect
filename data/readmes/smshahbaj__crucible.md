<div align="center">

<img src="assets/crucible-banner.svg" alt="Crucible — adaptive decision pressure-testing" width="100%">

### Adaptive decision pressure-testing for Claude Code, OpenCode & Roo Code

**Verify the facts · Challenge the weak point · Find the failure mode · Stop when the decision is stable**

**v1.2.3**

🌐 **Website:** https://crucible.smshahbaj.com

</div>

---

## What is Crucible?

**Crucible is an adaptive decision-review skill for Claude Code, OpenCode, and Roo Code.**

The methodology (routing, evidence gate, anti-anchoring, failure-first
challenge, quality gate) is identical on all three hosts. Only the
delegation mechanism differs — see [Multi-host support](#multi-host-support-claude-code-opencode-roo-code).

It is designed for decisions where reasoning quality matters:

- “Should I take this job?”
- “Should we ship architecture A or B?”
- “Is this investment plan sensible?”
- “Should I sign this agreement?”
- “What am I missing in this strategy?”
- “Pressure-test this proposal before we commit.”

Crucible does **not** turn every request into a large multi-agent debate. It chooses a review depth based on factors such as stakes, uncertainty, reversibility, and evidence needs.

> **More reasoning is not automatically better. The right amount of reasoning is better.**

## Highlights

- **Smart routing** — lightweight decisions stay lightweight; consequential decisions can receive deeper review.
- **14 specialist agents** — distinct lenses for evidence, options, risk, failure, verification, quantitative reasoning, and quality control.
- **Evidence gates** — decision-critical claims receive more scrutiny than optional details.
- **Anti-anchoring** — independent views are formed before a leading conclusion becomes an anchor.
- **Failure-first analysis** — attention goes to the failure mode most capable of changing the action.
- **Counterfactual pressure-testing** — identify the fact that would actually flip the recommendation.
- **Stopping rules** — stop when additional work is unlikely to change the action.
- **Decision Ledger** — optionally record decisions and outcomes locally.

Crucible is not a promise of perfect answers. Its goal is to make important decisions **more defensible, more transparent, and harder to fool** without making every decision unnecessarily slow.

---

# Install

## Requirements

You need:

- **Claude Code** installed and working.
- A local copy of this repository, or network access to add it as a marketplace.
- **Python 3.10+** only if you want to run the included Python tests, benchmarks, or ledger tools.
- No database or separate service is required for normal plugin use.
- Normal plugin loading does not require a separate model API key.

This repository is both a **Claude Code plugin** (`.claude-plugin/plugin.json`) and a **Claude Code marketplace** (`.claude-plugin/marketplace.json`) that catalogs that same plugin. Use whichever install method fits your workflow.

## Option A — Install from this marketplace (recommended)

This is the standard way to install and receive updates for Crucible.

### 1. Add the marketplace

```text
/plugin marketplace add smshahbaj/crucible
```

You can also add it by local path or full URL:

```text
/plugin marketplace add /local/path/to/crucible
/plugin marketplace add https://github.com/smshahbaj/crucible
```

### 2. Install the plugin

```text
/plugin install crucible@crucible-marketplace
```

`crucible-marketplace` is the marketplace name declared in `.claude-plugin/marketplace.json`; `crucible` is the plugin name declared in `.claude-plugin/plugin.json`.

### 3. Use Crucible

```text
/crucible Pressure-test this decision before I commit: should we choose architecture A or B?
```

You can also ask a normal decision-oriented question and allow the skill's routing to determine whether Crucible is relevant.

### 4. Update

```text
/plugin marketplace update crucible-marketplace
/plugin update crucible@crucible-marketplace
```

### 5. Uninstall

```text
/plugin uninstall crucible@crucible-marketplace
/plugin marketplace remove crucible-marketplace
```

(The second command removes the marketplace entry itself; skip it if you just want to remove the plugin.)

---

## Option B — Local / manual install with `--plugin-dir`

Use this if you want to run a local checkout or a downloaded copy directly, without adding a marketplace — for example while developing the plugin itself.

### 1. Get a local copy

**macOS / Linux**

```bash
git clone https://github.com/smshahbaj/crucible.git ~/crucible
```

or, from a ZIP release:

```bash
unzip crucible-*.zip -d ~/crucible
```

**Windows PowerShell**

```powershell
git clone https://github.com/smshahbaj/crucible.git .\crucible
```

### 2. Verify the plugin root

The directory passed to `--plugin-dir` must be the directory that **directly contains** `.claude-plugin/plugin.json`.

You should be able to find:

```text
crucible/
├── .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── agents/
├── skills/
│   └── crucible/
│       └── SKILL.md
└── ...
```

**macOS / Linux**

```bash
ls ~/crucible/.claude-plugin/plugin.json
```

**Windows PowerShell**

```powershell
Test-Path .\crucible\.claude-plugin\plugin.json
```

The Windows command should return:

```text
True
```

### 3. Start Claude Code with the plugin

**macOS / Linux**

```bash
claude --plugin-dir ~/crucible
```

**Windows PowerShell**

```powershell
claude --plugin-dir ".\crucible"
```

If you placed the checkout somewhere else, replace the path with your actual plugin root.

### 4. Use Crucible

```text
/crucible
```

### 5. Reload after local edits

If you are developing the plugin in an existing Claude Code session:

```text
/reload-plugins
```

A fresh Claude Code session is also a clean way to verify a changed package.

> Do not manually copy `SKILL.md` into your project's `.claude/skills/` directory. Load the plugin so its skill, agents, and references stay together.

---

## Multi-host support (Claude Code, OpenCode, Roo Code)

Crucible's methodology is host-independent; `agents/*.md` is the single
source of truth and the OpenCode/Roo Code files are generated from it (see
`skills/crucible/references/platforms.md` for the exact mapping and the
no-delegation fallback behavior).

### Option C — OpenCode

Copy or symlink the plugin root into your project (or `~/.config/opencode/`
for a global install) so OpenCode can see `.opencode/agent/*.md`,
`.opencode/command/review.md`, **and** `skills/crucible/references/` — the
orchestrator agent reads reference files from the latter by a project-root-
relative path, so it must be present alongside `.opencode/`, not left behind:

```bash
git clone https://github.com/smshahbaj/crucible.git ~/crucible
ln -s ~/crucible/.opencode ~/your-project/.opencode
ln -s ~/crucible/skills ~/your-project/skills
```

Then in OpenCode, either talk to the `crucible` primary agent directly, or
run:

```text
/review Should we choose architecture A or B?
```

### Option D — Roo Code

Copy `.roomodes` **and** the `skills/` folder from this repository into your
project root (Roo Code reads project-level `.roomodes` automatically; the
`crucible` mode reads `skills/crucible/references/` by the same
project-root-relative path as OpenCode above), or paste `.roomodes`'
contents into Global Modes via the command palette ("Edit Global Modes")
for a cross-project install — in that case also copy `skills/` into every
project you use it in, since Global Modes has no equivalent for reference
files:

```bash
git clone https://github.com/smshahbaj/crucible.git ~/crucible
cp ~/crucible/.roomodes ~/your-project/.roomodes
cp -r ~/crucible/skills ~/your-project/skills
```

Then select the **🔥 Crucible** mode (or type `/crucible`) and describe the
decision. Bind a fast model to the `crucible-decision-router`,
`crucible-evidence-gate`, `crucible-claim-compressor`, and
`crucible-quality-controller` modes and a stronger model to the rest (see
`references/platforms.md`) to preserve the token-discipline design instead
of running every lens on the same model.

### Regenerating the adapters after an edit

If you edit anything under `agents/` or `skills/crucible/SKILL.md`,
regenerate the OpenCode/Roo Code files so all three hosts stay in sync:

```bash
python3 scripts/gen_platform_adapters.py          # regenerate
python3 scripts/gen_platform_adapters.py --check  # verify in sync (CI-friendly, no writes)
```

`scripts/validate.py` runs the `--check` step automatically, so a
release with out-of-sync adapters fails validation.

---

## Verify the installation

Regardless of install method, start Claude Code with the plugin loaded, then run:

```text
/crucible Pressure-test this decision.
```

If `/crucible` is unavailable, check:

1. `.claude-plugin/plugin.json` exists at the plugin root.
2. `skills/crucible/SKILL.md` exists.
3. Claude Code loaded the plugin or marketplace without an error (check `/plugin` output).
4. You restarted Claude Code or used `/reload-plugins` after local changes.
5. Your installed Claude Code version supports the plugin behavior you are using.

You can also validate the repository structure directly without starting Claude Code:

```bash
python3 scripts/validate.py
```

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `/plugin marketplace add` fails | Path/URL doesn't point at a directory containing `.claude-plugin/marketplace.json` | Confirm you're pointing at the repository root, not a subdirectory |
| Marketplace adds but `crucible` isn't listed | Marketplace `name` in `marketplace.json` doesn't match what you referenced in `install` | Use `crucible@crucible-marketplace` exactly, or run `/plugin marketplace list` to see the registered name |
| `/crucible` command not found after install | Plugin loaded but Claude Code session wasn't reloaded | Run `/reload-plugins` or start a new session |
| `plugin.json` / `marketplace.json` parse errors | Manually edited JSON with a syntax error | Run `python3 -c "import json; json.load(open('.claude-plugin/plugin.json'))"` (and the same for `marketplace.json`) to locate the error |
| Python tests/scripts fail with `ModuleNotFoundError` | No local Python environment set up | Only required for running the test suite/benchmarks, not for normal plugin use; run `pip install pytest` or use `python3 scripts/run_tests_standalone.py`, which has no dependencies |
| Update doesn't pick up new version | Marketplace not refreshed | Run `/plugin marketplace update crucible-marketplace` before `/plugin update` |

---

# How it works

```text
Decision
   │
   ▼
Frame the question
   │
   ▼
Route by stakes, uncertainty,
reversibility & evidence needs
   │
   ├── QUICK
   ├── REVIEW
   └── DEEP
          │
          ▼
   Targeted specialist lenses
          │
          ▼
   Evidence / verification
          │
          ▼
   Challenge / failure test
          │
          ▼
   Quality control
          │
          ▼
   Stable recommendation
```

The core principle is **adaptive scrutiny**: spend review budget where it can plausibly flip the action.

### Review depths

| Depth | Typical use |
|---|---|
| 🟢 **QUICK** | Low-stakes, clear, reversible choices |
| 🟡 **REVIEW** | Meaningful trade-offs or uncertainty |
| 🔴 **DEEP** | High downside, conflicting evidence, irreversible or unusually consequential decisions |

Specialized verification, comparison, or red-team work is conditional—not automatically run for every request.

---

# Decision Ledger

The optional ledger lets you record decisions, reasoning, risks, and outcomes locally.

See:

```text
skills/crucible/references/ledger.md
```

for the exact contract and commands.

Typical commands from the plugin root:

```bash
python3 scripts/decision_ledger.py --add record.json --ledger .crucible/ledger.jsonl
```

```bash
python3 scripts/decision_ledger.py --render record.json
```

```bash
python3 scripts/decision_ledger.py --report --ledger .crucible/ledger.jsonl
```

If you do not need the ledger, no configuration is required.

---

# Testing

From the plugin root:

### Python syntax check

```bash
python3 -m compileall -q .
```

### Core test suite

```bash
python3 -m pytest tests/ -v
```

If pytest is unavailable:

```bash
python3 scripts/run_tests_standalone.py
```

### Package validation

```bash
python3 scripts/validate.py
```

### Routing audit

```bash
python3 scripts/score_routing.py
```

### 120-case benchmark

```bash
python3 scripts/run_benchmark.py --limit 120
```

### Golden benchmark

```bash
python3 scripts/run_golden_benchmark.py
```

### Stress test

```bash
python3 scripts/stress_test.py --iterations 200
```

Use the individual script help/output for any additional options supported by your package version.

---

# Benchmark honesty

Crucible deliberately distinguishes **offline contract validation** from **live model quality**.

Offline benchmarks can validate:

- routing contracts;
- structured output contracts;
- scoring and aggregation;
- required fields;
- regression behavior;
- failure handling;
- benchmark plumbing.

An offline score is **not** proof that a live language model will make the same decision correctly.

For meaningful live evaluation, record:

- model/version;
- evaluation date;
- benchmark version;
- adapter;
- raw outputs;
- score;
- critical failures;
- latency;
- token/cost information when available;
- relevant environment/configuration.

See:

```text
benchmarks/GOLDEN_DATASET.md
benchmarks/GOLDEN_DATASET_RESULTS.md
benchmarks/GOLDEN_RUBRIC.md
```

---

# Live-model evaluation

The package includes an adapter path for external model evaluation:

```text
scripts/claude_adapter.py
```

Read the benchmark documentation before running it. A live adapter may require an API credential in your environment.

**Never put API keys inside the plugin, benchmark cases, README, or ZIP.**

Normal Crucible plugin use is separate from this optional evaluation path.

---

# Safety and limitations

Crucible is a **decision-support system**, not a guarantee of correctness.

For legal, medical, financial, employment, safety, security, or other high-impact matters, use appropriate qualified professionals and primary sources where necessary.

Crucible can help surface:

- missing information;
- assumptions;
- trade-offs;
- failure modes;
- evidence worth checking;
- uncertainty;
- conditions that would flip a recommendation.

It cannot guarantee:

- factual correctness;
- complete information;
- a correct prediction;
- a good outcome;
- professional or legal compliance.

> **The goal: make consequential decisions harder to fool without making every decision unnecessarily slow.**

---

# What Crucible is not

Crucible is not:

- a promise of perfect answers;
- a “run 14 agents on everything” system;
- a majority-vote truth machine;
- a replacement for primary evidence;
- a replacement for qualified professional advice;
- a reason to expose private internal reasoning or hidden agent transcripts.

Multiple agents reaching the same conclusion from the same evidence are not automatically independent evidence.

---

# Project structure

```text
crucible/
├── .claude-plugin/
│   ├── plugin.json         # plugin manifest (Claude Code)
│   └── marketplace.json    # marketplace catalog (lists this plugin)
├── .opencode/               # generated OpenCode adapter (see below)
│   ├── agent/               # 14 specialists + crucible orchestrator
│   └── command/review.md
├── .roomodes                # generated Roo Code adapter (14 specialist modes + crucible mode)
├── agents/                  # canonical specialist source (Claude Code subagents)
├── assets/
│   └── crucible-banner.svg
├── benchmarks/
├── scripts/
│   └── gen_platform_adapters.py  # regenerates .opencode/ and .roomodes from agents/
├── skills/
│   └── crucible/
│       ├── SKILL.md
│       └── references/
│           └── platforms.md      # host mapping + no-delegation fallback
├── tests/
├── README.md
├── LICENSE
├── SECURITY.md
└── CONTRIBUTING.md
```

The main skill is:

```text
skills/crucible/SKILL.md
```

---

## Additional troubleshooting

### Crucible does not trigger automatically

Try:

```text
/crucible Pressure-test this decision.
```

Routine edits, trivial lookups, and low-stakes reversible questions are intentionally kept lightweight.

### Benchmark asks for credentials

Normal plugin usage does not require benchmark credentials.

Only live external-model evaluation needs the relevant adapter and credentials. Keep those credentials in environment variables or a local secret manager.

---

# Release information

**Version:** `1.2.3`

The release contains:

- adaptive decision routing;
- 14 specialist agents;
- multi-host adapters (Claude Code, OpenCode, Roo Code) generated from a single source and kept in sync by `scripts/gen_platform_adapters.py`;
- evidence and verification methodology, including a proactive base-rate check and a stale-by-default rule for fast-decaying facts;
- anti-anchoring controls;
- failure-first pressure testing;
- decision-ledger support, including reversal-rate breakdown by confidence and by route;
- routing and benchmark infrastructure, including explicit VERIFY/REDTEAM/COMPARE mode handling and risk-tolerance-aware routing;
- golden evaluation materials;
- adversarial and robustness testing;
- prompt-content regression snapshots (`tests/test_prompt_snapshots.py`);
- CI (`.github/workflows/test.yml`) enforcing all of the above on every push/PR, plus a golden-benchmark run, a stress-test run, and an automated tagged release on push to `main`;
- release validation tooling.

Offline benchmark results should be interpreted as **engineering/regression evidence**, not as proof of universal model accuracy.

---

# Contributing

Before changing the project:

1. Preserve the adaptive decision-depth philosophy.
2. Do not add agents merely to increase the agent count.
3. Add regression tests for behavior changes.
4. Keep benchmark claims reproducible and honest.
5. Preserve safety and evidence gates.
6. Do not expose private internal reasoning.
7. Run validation and tests before release.

See:

```text
CONTRIBUTING.md
SECURITY.md
```

---

# License

MIT — see `LICENSE`.

---

<div align="center">

### 🔥 Crucible

**Verify. Challenge. Decide.**

**v1.2.3**

</div>

Project site: https://crucible.smshahbaj.com
Developer: SM Shahbaj — https://smshahbaj.com
Contact: contact@smshahbaj.com
