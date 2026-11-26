# goose-deuce

**A plain-markdown operating system that keeps AI coding agents from improvising
silently, sprawling across tasks, or declaring broken work "done."**

Drop the markdown files into a new project folder alongside a raw `idea.md` (or
`plan.md`) and point your agent at it. Every session — human-driven or looping,
frontier model or local model — works from one serialized queue (`TASKS.md`),
verifies against runnable commands (`Project snapshot`), writes timestamped
`[YYYY-MM-DD T-###]` design comments, logs every departure from plan in an immutable
audit trail (`goose-deuce.md`), and never pushes without your explicit approval.

> Plain markdown files in git that counter specific LLM failure modes — backed by
> runnable test gates and an adversarial diff review before every commit. No
> scripts, CLI wrappers, or frameworks required.

---

## Why this exists

Left alone in a repo, coding agents fail in predictable ways:

1. **Silent workarounds.** A test OOMs or an API misbehaves, so the agent quietly
   mocks it out, skips an edge case, or swaps approaches — and reports "Done!"
   Three sessions later nobody knows why the code behaves that way.
2. **Breadth-first sprawl.** It opens files across three features, hits the context
   window, and leaves a half-broken tree.
3. **Tautological tests.** The same pass writes code and tests that encode its own
   assumptions, or skips running the real CLI flags.
4. **Context rot.** Every fresh window forgets your build flags, hits solved
   foot-guns again, or trusts stale docs that lie about what shipped.

**goose-deuce** addresses those failure modes structurally in plain markdown.

---

## What it looks like in a repo

Two files drive the workflow: **`TASKS.md`** (one serialized queue with runnable
acceptance criteria) and **`goose-deuce.md`** (the immutable log of every departure
from plan).

**A pickable task (`TASKS.md`):**

```markdown
- [ ] T-014 — Export query results to CSV
      Why: users need offline spreadsheets without hitting API pagination
      Accept: `uv run pytest tests/test_export.py` passes; `uv run app export --rows 1000` exits 0
      Touches: src/export/csv.py, tests/test_export.py   Depends: none   Gated: none
```

**When reality breaks the plan (`goose-deuce.md`):**

```markdown
## 2026-08-15 — CSV export streams to disk instead of building in memory  [approach]
- Task: T-014 (export command; docs/PLAN.md § Export)
- What: `export_csv` writes through a 64 KB buffered stream; one-shot string build removed.
- Why: the 1.2M-row fixture held ~900 MB resident and OOM-killed the 2 GB CI runner.
  Proven: old code fails `test_export_large_fixture`; streaming passes at ~40 MB.
- Where: `src/export/csv.py` (`export_csv`, `_row_stream`); `tests/test_export_large_fixture.py`.
- Plan: T-014 assumed in-memory string build for atomicity → streamed to `export.tmp` +
  atomic rename on success. `TASKS.md` updated in this commit; `docs/PLAN.md` unaffected.
- Commit(s): this commit
- [Correction, 2026-08-17: rename is not atomic on FAT volumes; T-019 filed to warn.]
```

The rule is simple: **the plan is not sacred; *silent* departure from it is the failure
mode.** Work that follows the plan needs no entry. Work that diverges is fine *exactly
when* it is logged with its evidence in the same commit — and any deferred shortcut
**must** create a live `TASKS.md` item (`goose-deuce.md` explains; `TASKS.md` owes).

---

## The six properties behind `AGENTS.md`

- **One active `[~]` task at a time** (`PICK → CLAIM → PLAN → IMPLEMENT → TEST →
  DOCUMENT → RECONCILE → REVIEW → COMMIT → NEXT`), with runnable `Accept:` commands.
- **Exact commands + "Foot-guns already paid for"** in `Project snapshot`, verified
  on a cold clone (`T-002`).
- **Timestamped `[YYYY-MM-DD T-###]` educational comments** on code changes so the
  code teaches its own history — and comments never assert behaviour that was not
  exercised.
- **Tests are the gate:** new behaviour ships with tests; bug fixes ship with a
  regression test seen failing against the old code; nothing commits red.
- **Docs sweep in the same commit** (including a `CHANGELOG.md` entry per task so
  silence is never an answer).
- **Deviations land in `goose-deuce.md` in the same commit**, with the top entries
  read at every session start so fresh windows inherit scar tissue immediately.

**A note on `AGENTS-TEMPLATE.md` size (~31.5 KB raw / ~28.2 KB instantiated):**
All rules stay in **one** `AGENTS.md` file so nothing drifts across multiple rule
files. Once you delete the leading `<!-- TEMPLATE ... -->` instructions, the core
manual is **~28.2 KB** — which fits cleanly on 128k–1M models (for example, Hermes
scales `context_file_max_chars` at ~6% of the model's context window: ~30.7k at 128k,
~48k at 200k, ~240k at 1M). If you run a small/local model with a `20,000`-char cap,
raise `context_file_max_chars` in your harness config or trim verbose examples as your
snapshot grows.

**Why `prompts-template.md` repeats short bounds:**
These scaffolds were originally refined running **local models in Goose** loops,
where smaller models lose the thread faster than frontier cloud models. Echoing the
gate command, `1`-task cap, and stop condition in the opening prompt acts as a
recency pin without creating a competing source of truth.

---

## The files

| File | Role | Copy into your repo? |
|---|---|---|
| `templates/AGENTS-TEMPLATE.md` | Complete operating manual (~31.5 KB raw / ~28.2 KB instantiated) — law, snapshot, 10-step loop, testing, docs, VC, DoD | **Yes** → `AGENTS.md` |
| `templates/TASKS-TEMPLATE.md` | Starter work queue (~2.3 KB) pre-seeded with `T-000`…`T-004` | **Yes** → `TASKS.md` |
| `templates/GOOSE-DEUCE-TEMPLATE.md` | The deviations log (~10.2 KB) — trigger, tags, 6-field entry format, immutable rules | **Yes** → `goose-deuce.md` |
| `templates/LOOP-TEMPLATE.md` | Overlay for unattended `/loop` sessions (~3.1 KB) — autonomy guard, never-push, pace, stuck-loop stop | Only if running loops → `LOOP.md` |
| `templates/HERMES-OVERLAY-TEMPLATE.md` | Overlay for Hermes Agent (~5.6 KB) — `memory` boundary, `delegate_task`, cron sweeps, skills, why not `.hermes.md` | Only if using Hermes → `HERMES-OVERLAY.md` |
| `templates/NEW-PROJECT-GUIDE.md` | 5-step bootstrap (~14.9 KB) — drop-in `idea.md` flow, kit-clone flow, `T-000` existing-repo gate, Step-5 sweep checklist | Follow at setup (remove before `T-000`) |
| `templates/prompts-template.md` | Copy-paste session prompts (~13.7 KB) — Scaffolds A–E (Kickoff, Task, Review, Sweep, Hermes) | Use from kit (remove before `T-000`) |

---

## Harness compatibility

| Harness | How it loads the law | Notes |
|---|---|---|
| **Codex / Cursor / OpenCode** | Reads `AGENTS.md` natively | — |
| **Claude Code** | Reads `CLAUDE.md` | `ln -s AGENTS.md CLAUDE.md` (macOS/Linux) or put `@AGENTS.md` / `"Read AGENTS.md before doing anything else."` in `CLAUDE.md` (Windows-safe). |
| **Goose** | Reads `AGENTS.md` (`.goosehints` on older installs) | Put `Read AGENTS.md before doing anything else.` in `.goosehints` if needed. |
| **Hermes Agent** | Reads `AGENTS.md` (`context_file_max_chars` scales with model window; 20k floor) | Adopt `HERMES-OVERLAY.md` via the hook in `AGENTS.md`; do **not** rename it `.hermes.md` or `HERMES.md` (first-match-wins suppresses `AGENTS.md`). Note `AGENTS.override.md` overrides `AGENTS.md` if present. Use Scaffold E for Hermes sessions. |

---

## Quickstart

```bash
git clone https://github.com/SnoobieJunes/goose-deuce.git
```

### Path A — Drop into a new project folder with `idea.md` *(how it's built to be used)*
1. Copy the files from `templates/` into your new project folder (`~/my-project/`),
   delete `LOOP-TEMPLATE.md` / `HERMES-OVERLAY-TEMPLATE.md` if not using them, and
   write a plain **`idea.md`** (or `plan.md`) braindump of what you want to build.
2. Point your agent at that folder using **Scaffold A (Variant A1)** from
   `prompts-template.md` — or paste:
   > *"I placed the goose-deuce templates and `idea.md` here. Read `idea.md` and
   > `NEW-PROJECT-GUIDE.md` first. Ask me any clarifying questions I have not answered
   > before scaffolding or locking `docs/PLAN.md`, then follow steps 1–3 of
   > `NEW-PROJECT-GUIDE.md` (renaming `*-TEMPLATE.md` to live files and removing
   > `NEW-PROJECT-GUIDE.md` and `prompts-template.md` before committing `T-000`) and
   > stop after `T-002` + the cold-clone gate pass."*

### Path B — Run from one central kit clone
Keep a single clone of `goose-deuce` and paste **Scaffold A (Variant A2)** from
`templates/prompts-template.md` pointing at `~/⟨ProjectName⟩` and your kit path.

### Path C — Adopting an existing repo
1. Copy `AGENTS-TEMPLATE.md` → `AGENTS.md`, `TASKS-TEMPLATE.md` → `TASKS.md`, and
   `GOOSE-DEUCE-TEMPLATE.md` → `goose-deuce.md` in your repo root (plus
   `LOOP-TEMPLATE.md` → `LOOP.md` / `HERMES-OVERLAY-TEMPLATE.md` →
   `HERMES-OVERLAY.md` only if needed).
2. Delete each template's `<!-- TEMPLATE ... -->` header comment (and `WORKED-EXAMPLE`
   in `goose-deuce.md`), and fill every `⟨…⟩` in `AGENTS.md` (plus `LOOP.md` /
   `HERMES-OVERLAY.md` if adopted).
3. Point `CLAUDE.md` at `AGENTS.md` (`ln -s AGENTS.md CLAUDE.md` or `@AGENTS.md`).
4. Create `docs/PLAN.md` and `CHANGELOG.md`, and replace `T-000`..`T-003` in
   `TASKS.md` with **`T-000: establish the gate`**: run the existing suite as-is,
   mark known-red tests `[!]`, set the coverage floor to the measured baseline, and
   verify a cold clone.
5. Verify no placeholders remain:
   `grep -rn "⟨" . --include="*.md" --exclude="CLAUDE.md" --exclude-dir=.git --exclude-dir=.venv --exclude-dir=node_modules`
   returns nothing.

---

## Origin of the name

The kit started on the open-source Goose harness, where the deviations file was
originally called `deviations.md`. The rename came from nihilistic humor and one
debugging session: a feature felt subtly wrong, and tracing the bug left a trail of
goose shit leading straight from the symptom back to the deviations log. Every time,
it was a call the LLM had made where the spec was silent — or a constraint that forced
its hand. Having that breadcrumb trail turned hours of archaeology into a five-second
lookup, so the name stuck.

---

## Status & Contributing

Battle-tested across real projects; extracted into an independent kit. Issues and PRs
welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE) — copy, adapt, and embed in personal, open-source, or commercial repos
without friction.
