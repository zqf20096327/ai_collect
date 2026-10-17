# Skills

[![NVIDIA SkillSpector audit](https://img.shields.io/github/actions/workflow/status/wquguru/skills/security-audit.yml?branch=main&logo=nvidia&label=NVIDIA%20SkillSpector%20audit)](https://github.com/wquguru/skills/actions/workflows/security-audit.yml)
[![AI review by Claude](https://img.shields.io/badge/AI%20review-Claude-d97757?logo=claude)](https://github.com/anthropics/claude-code-security-review)

A small collection of practical Agent Skills.

> **Public monorepo.** Anyone can clone this repo, run `just add`, or install
> individual skills with `npx skills add`. It does not depend on any private
> tooling. The install loop links into Claude Code, Codex, and Grok skill dirs.

**Catalog:** self-authored skills live under [`skills/`](./skills/) (see also the
[GitHub Pages registry](https://wquguru.github.io/skills/)). Highlighted ones
below; the full set is every folder with a `SKILL.md`. Third-party modules are
declared in [`external.yml`](./external.yml) and materialised by `just vendor`.

## Skills

### `claude-5-best-practice`

> Renamed from `fable-5-best-practice` in July 2026, when Claude Opus 5 shipped
> near-Fable capability at half the price and the routing advice stopped being
> about one model. Reinstall under the new name.

Optimizes the cost of an *accepted result* across the Claude 5 generation —
Haiku 4.5 / Sonnet 5 / Opus 5 / Fable 5 — rather than the price of a token. It
treats Opus 5 as the default lead, makes Fable 5 something you justify instead
of assume, and prefers climbing the effort ladder (`low` → `max`) on Opus 5
before escalating a tier. It also walks a diagnose-before-escalating loop for
failures, routes subagents with pinned worker models, covers Claude 5 API
behavior (adaptive thinking, effort and prompt caching, refusal stop reasons,
fallback, ZDR and Priority Tier constraints), and keeps progress claims tied to
real tool evidence. Volatile facts such as pricing, retention, and beta headers
live in a dated `references/evidence-notes.md` provenance snapshot.

The skill is especially useful when migrating older prompts or skills forward:
it calls out over-constrained legacy prompting, the Opus 4.8 → Opus 5 thinking
and effort breaks, refusal risks, verifier agents, long-running run design, and
long-run communication style.

Install:

```bash
npx skills add https://github.com/wquguru/skills --skill claude-5-best-practice
```

Ask for help with prompts like:

- "Does this task actually need Fable 5, or is Opus 5 enough?"
- "Help me write an Opus 5 prompt for a multi-day coding task."
- "Review this old skill before migrating to Claude 5."
- "My run missed the acceptance criteria — raise effort or change model?"

### `gpt-5-6-best-practice`

A routing and evaluation overlay for GPT-5.6 in Codex. It optimizes the cost of
an accepted result — not the price of a token — across the Sol, Terra, and Luna
capability tiers: choosing the initial tier and reasoning-effort lane,
diagnosing failures before escalating, keeping prompts and worker packets lean,
using subagents economically, and evaluating routes on real work. Benchmark
provenance and confidence levels live in `references/evidence-notes.md`, and
`references/prompt-patterns.md` provides reusable task-prompt and worker-packet
templates.

Install:

```bash
npx skills add https://github.com/wquguru/skills --skill gpt-5-6-best-practice
```

Ask for help with prompts like:

- "Which GPT-5.6 tier and effort should this task start on?"
- "This Codex run failed — raise effort, or move from Terra to Sol?"
- "Is Ultra worth it for this task, or should one agent handle it?"
- "Design a worker packet for this subagent."

### `english-swe-daily`

A practical English coach for everyday engineering communication. Built for
developers who can already work in English but want to sound less textbook-like
and more like a real teammate in standups, Slack threads, 1:1s, code reviews,
and meetings.

Many engineers do not struggle with grammar — they struggle with sounding
natural. This skill teaches the kind of English people actually use in software
teams, with a strong focus on natural phrasing, collaboration tone, and
day-to-day workplace situations.

Install:

```bash
npx skills add https://github.com/wquguru/skills --skill english-swe-daily
```

Ask for help with prompts like:

- "Teach me English for standups."
- "Help me sound more natural in Slack."
- "Practice English for code reviews."
- "How do I say this more naturally at work?"
- "Give me today's SWE English session."

### `pi-setup`

Configures Pi Agent (`@earendil-works/pi-coding-agent`) with DeepSeek V4
(built-in provider) and Ant-Ling Ring-2.6-1T (custom OpenAI-compatible
provider), plus a curated extension set, while automatically working around 7
known pitfalls.

It detects before it acts: it probes whether pi is installed, whether config
already exists, and where keys live before changing anything. Keys are never
written in plaintext — pi config only stores lazy `!shell` commands and the key
stays in the user's original file. Model selection, default model, default
thinking tier, and the extension set are all confirmed interactively.

Install:

```bash
npx skills add https://github.com/wquguru/skills --skill pi-setup
```

Trigger it in Claude Code by saying "配置 pi", "setup pi agent", "把
ring/deepseek 配到 pi", or run `/pi-setup` manually.

Prerequisites:

- Node.js / npm (to install pi)
- A DeepSeek key (in `~/.deepseek` or an environment variable)
- An Ant-Ling/Ling key (`LING_API_KEY`, in a shell rc or environment
  variable) — only needed when enabling Ring

### `free-my-cpu`

Safely audits CPU, load average, I/O wait, and Docker container pressure on
Linux hosts, especially production-like servers over SSH. It follows the same
read-only-first posture as `free-my-disk`: collect repeated samples, separate
CPU-bound work from I/O pressure, inspect hot containers and logs, then classify
possible fixes by impact before changing anything.

Install:

```bash
npx skills add https://github.com/wquguru/skills --skill free-my-cpu
```

Ask for help with prompts like:

- "Use free-my-cpu to inspect this remote Docker host."
- "Why is this Docker host load average so high?"
- "Find which container is burning CPU."
- "Use this Grafana URL and the last 6 hours to check whether monitoring queries are causing load."

### `youtube-toolkit`

Downloads YouTube videos with `yt-dlp` and post-processes them with `ffmpeg`:
fetch best-quality streams, convert containers (e.g. AV1/webm → H.264 mp4),
extract audio, and burn in translated subtitles with a translator watermark.

It is macOS-first and bakes in the gotchas learned the hard way — chiefly that
Homebrew's lean `ffmpeg` ships without libass/drawtext (so subtitle burn-in
needs `ffmpeg-full`), that YouTube auto-captions are overlapping rolling cues
that must be re-segmented before they read cleanly, and that styling via an ASS
file avoids the `force_style` comma-parsing trap. Two helper scripts do the
deterministic work: `install-tools.sh` and `burn-subs.sh`.

Install:

```bash
npx skills add https://github.com/wquguru/skills --skill youtube-toolkit
```

Ask for help with prompts like:

- "Download this YouTube video to ~/Downloads."
- "Convert it to mp4."
- "Add Chinese subtitles and a @handle 翻译 watermark."

Prerequisites:

- Homebrew (macOS) or apt/pip (Linux)
- `yt-dlp` and a libass-enabled `ffmpeg` — `install-tools.sh` sets both up

## Local Development

For local hacking, the `Justfile` is **self-contained**: it symlinks every skill
under `skills/` **and** `external/` into Claude Code (`~/.claude/skills/`),
Codex (`~/.codex/skills/`), and Grok (`~/.grok/skills/`), so edits take effect
immediately without re-publishing. No private sibling repo is required.

```bash
just add      # symlink all skills (skills/ + external/) into agent dirs
just remove   # remove only the symlinks that point back into this repo
just status   # show install status for each skill in all destinations
just vendor   # pull third-party skills declared in external.yml into external/
just          # list available recipes
```

`add` is idempotent and never clobbers: an existing real directory or a symlink
from another install tree is left untouched and reported as skipped
(`foreign symlink`). `remove` only removes symlinks that point back into this
repo. After adding a new skill folder, re-run `just add`.

## External (third-party) skills

`skills/` holds the skills authored here (and published via `npx skills add`).
Third-party skills from other repos are **not** copied into git — they are
vendored separately so this public repo stays purely self-written and free of
foreign licenses:

1. Declare sources in `external.yml` — a repo, a `ref` (branch/tag/commit), and
   the sub-paths to pull. Each dir's basename, prefixed with `3rd-`, becomes the
   skill name (e.g. `dashboarding` → `3rd-dashboarding`).
2. `just vendor` shallow/sparse-clones each source, copies the named skill dirs
   into `external/` (git-ignored) under their prefixed names, rewrites each
   `SKILL.md` frontmatter `name` to match, and records the exact upstream commit
   SHA in `external.lock`.
3. `just add` symlinks them alongside the self-written skills.

Only `external.yml` + `external.lock` are committed; the vendored code is not.
Re-run `just vendor` any time to refresh (or after pinning a `ref`). A name that
would collide with a self-written `skills/<name>` is skipped; entries removed
from `external.yml` are pruned from `external/` on the next `just vendor`.

## Repository Structure

```text
Justfile          # add / remove / status / vendor (self-contained)
external.yml      # third-party skill sources (repo + ref + sub-paths)
external.lock     # resolved upstream commit SHAs (auto-generated)
scripts/
  vendor.sh       # pulls external.yml sources into external/
skills/           # self-written skills (published)
  claude-5-best-practice/
  gpt-5-6-best-practice/
  english-swe-daily/
  …
external/         # vendored third-party skills (git-ignored; just vendor)
index.html        # public site
```

## License

Self-authored skills under `skills/` are intended for public use via this repo
and `npx skills add`. Third-party code under `external/` is **not** redistributed
in git — only `external.yml` / `external.lock` are tracked; run `just vendor` to
fetch upstream under their own licenses.
