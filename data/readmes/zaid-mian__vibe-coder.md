# Vibe Coder

**A planning and unblocking skill for AI coding assistants. Interview → verify → plan → build.**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Claude-Agent%20Skill-blueviolet)](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
[![No dependencies](https://img.shields.io/badge/dependencies-none-brightgreen)](scripts/)
[![Works offline](https://img.shields.io/badge/network-not%20required-lightgrey)](scripts/)

Vibe coding fails for two boring reasons: the assistant started before the decisions were made, and it
guessed at facts about the repository instead of looking. This skill fixes both. It interviews you
until nothing is left to guess, reads and runs things to establish fact, and writes the documents your
coding assistant needs — plus focused recovery plans for the six situations where AI-assisted projects
actually get stuck.

**It never writes application code without your approval.**

<p align="center">
   <img src="assets/vibe-coder-demo.gif" alt="Vibe Coder workflow: idea to questions to project brain to structured development" width="360" />
</p>

Vibe Coder makes Claude understand the work before it starts doing the work: ask the right questions,
verify the repository, build a project brain, then use the workflow that matches the task.

---

## Quickstart (60 seconds)

```bash
git clone https://github.com/zaid-mian/vibe-coder.git
cd vibe-coder

# see what it would tell you about any project
python scripts/scan_project.py /path/to/some/repo
```

No dependencies. Python 3.9+, standard library only. Nothing to install.

**Use it as a skill:** zip the folder and upload it at **Settings → Capabilities → Skills**. The
included packager does the layout correctly:

```bash
python scripts/package_skill.py        # writes dist/vibe-coder.zip with the folder as zip root
```

Then in a chat, say `/vibe-coder` or just describe what you want — "help me plan my app", "why is this
broken", "review my diff", "add tests".

For the complete Claude upload, first-use, workflow, safety, and troubleshooting instructions, see
[`docs/complete-guide.md`](docs/complete-guide.md).

---

## What it does that a prompt does not

| Plain prompt | This skill |
|---|---|
| Invents a stack in the first sentence | Asks, or uses a labelled `Default (changeable)` |
| Assumes your framework | `scan_project.py` reports what is actually there |
| Starts coding immediately | Stops after `prd.md` for approval |
| Ships `TBD` and empty sections | Deterministic validator fails the build on placeholders |
| Says "fixed!" without checking | Root cause with a reproduction, plus a check that can fail |
| Forgets last session | `session_brief.py` rebuilds state from git + `brain/` |

Full side-by-side: [`examples/before-after.md`](examples/before-after.md)

---

## The nine modes

Routing is by intent, so only the mode file you need enters context.

| Intent | Mode | Output |
|---|---|---|
| Start a project / write a spec | [`plan`](references/mode-plan.md) | `brain/prd.md` → approval → architecture, tasks, database |
| "What is this codebase?" | [`audit`](references/mode-audit.md) | `brain/audit.md` — inventory, gaps, risks |
| "Why is this broken?" | [`debug`](references/mode-debug.md) | `brain/debug/<slug>.md` + verified fix |
| Add or fix tests | [`test`](references/mode-test.md) | `brain/testing.md` + tests that can fail |
| Clean up code safely | [`refactor`](references/mode-refactor.md) | step plan + guarded edits |
| Review a diff or PR | [`review`](references/mode-review.md) | `brain/reviews/<rev>.md` |
| Change a schema | [`migrate`](references/mode-migrate.md) | reversible migration plan |
| Security pass | [`security`](references/mode-security.md) | `brain/security.md` — findings with severity |
| Resume previous work | [`resume`](references/mode-resume.md) | one-screen brief + next action |

---

## The five laws

1. **Facts come from the repo, not from memory.** Run `scan_project.py` first. Anything it cannot
   establish is marked `NOT VERIFIED` — never invented.
2. **Ask until nothing is left to guess.** No question budget, no cap. Scale to the ambiguity. Stop when
   documenting what remains would mean inventing a behaviour.
3. **`prd.md` is the single source of truth.** Everything else derives from it. A missing decision is a
   question, not an invention.
4. **No placeholders.** `TBD`, `TODO`, `lorem`, empty sections — the validator fails on all of them.
5. **Touching code needs explicit permission.** Planning modes are documentation-only. Every code change
   is shown before it is made.

---

## What it refuses to do

The point of the safety rules is that they are enforced, not aspirational.

- Never invents a command, path, version, service, or environment variable
- Never reproduces a secret value — file path and line number only
- Never claims a test passed without running it
- Never marks a failing test as skipped to get a green build
- Never edits a migration that has already been applied
- Never creates a `NOT NULL` column without a default on a populated table
- Never runs a migration or backfill against production
- Never force-pushes, rewrites history, or rotates a credential
- Never says a system is secure — it states the scope reviewed

---

## Scripts

Deterministic tools beat model guesses. Run them.

| Script | Purpose |
|---|---|
| [`scan_project.py`](scripts/scan_project.py) | Factual repo inventory: languages, manifests, entry points, CI, infra, migrations, tests, env var **names**, secret locations |
| [`session_brief.py`](scripts/session_brief.py) | "Where was I" from git state + `brain/` headings. Read-only git only |
| [`validate_blueprint.py`](scripts/validate_blueprint.py) | Required sections, placeholder scan, empty sections, cross-file entity names. Exit 1 = fix first |
| [`check_links.py`](scripts/check_links.py) | Every relative path and `##` reference inside generated docs resolves |
| [`init_blueprint.py`](scripts/init_blueprint.py) | Heading-only stubs; never overwrites |
| [`package_skill.py`](scripts/package_skill.py) | Build a correctly laid-out upload zip |

All standard-library Python. No network. No telemetry.

---

## Repository layout

```
vibe-coder/
├── SKILL.md                 entry point: laws, routing, safety, output contract
├── references/
│   ├── mode-*.md            nine modes, loaded one at a time
│   ├── interview.md         question bank + coverage gate
│   ├── *-template.md        exact document shapes
│   ├── stack-defaults.md    boring defaults, used only on request
│   └── quality-bar.md       the anti-slop pass
├── scripts/                 six dependency-free tools
├── examples/
│   ├── before-after.md      the same request, two worlds
│   └── planning/            a complete validated brain/ set
├── docs/                    faq, how it works, contributing a mode
└── .github/                 CI, issue and PR templates
```

---

## Verified, not asserted

The claims above are checked by tests in this repository:

```bash
python -m unittest discover -s tests -t .                      # 15 tests, exit 0
python scripts/validate_blueprint.py --dir examples/planning   # exit 0
python scripts/check_links.py .                                # exit 0
python scripts/scan_project.py . > /dev/null                   # exit 0
python scripts/package_skill.py                                # exit 0, layout asserted
```

CI runs exactly these on Python 3.9 and 3.12. The suite exists to test the **safety claims** rather
than to raise a number: the validator must reject an empty stub set, reject a banned placeholder,
reject a missing file, and accept the reference example; the scanner must report a secret's location
and **never its value**, and must report environment variable names only; the link checker must catch
a broken path inside this repository and ignore a path belonging to the user's project; `SKILL.md`
must satisfy the Agent Skills field limits; and no instruction file may reintroduce a question cap.
A check that cannot fail proves nothing, so `test_empty_stub_set_fails` asserts the failure.

---

## Honest limitations

- **It plans; it does not build your app.** That is the design, not a gap.
- **Python 3.9+ required** for the scripts. The instructions work without them, with less rigour.
- **The skill cannot verify itself inside a host's uploader.** First-run behaviour in a new assistant is
  unconfirmed until you try it.
- **No stars, no forks, guaranteed.** No repository can promise that. What this repo does control is
  the set of things that actually drive adoption in this niche: a README that states the problem in one
  screen, a quickstart under a minute, no dependencies, a license, CI that runs the checks, issue and PR
  templates, a changelog, and examples that show the difference. Those are present; the rest is earned.
- **The 9 modes are not 9 different tools.** Nine situations share one contract, deliberately.

---

## Contributing

New modes and sharper questions are the most valuable contributions. See
[`CONTRIBUTING.md`](CONTRIBUTING.md) and [`docs/contributing-a-mode.md`](docs/contributing-a-mode.md).
Every mode has the same contract: read-only or approval-gated, evidence or `NOT VERIFIED`, no invented
commands.

## License

[MIT](LICENSE).
