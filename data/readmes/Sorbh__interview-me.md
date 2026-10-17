# interview-me

**A Claude Code skill that interviews you like a senior architect before you write code.**

[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-blue)](https://docs.anthropic.com/en/docs/claude-code) &nbsp; [![MIT License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

![interview-me in action](assets/interview-me-preview.gif)

## Why This Exists

When you're building alone, there's no one to challenge your assumptions. Requirements start as vague ideas, edge cases get discovered in production, and security concerns become afterthoughts.

**interview-me** is the senior architect you wish you had on the team. It reads your requirement, checks whether your existing code is even relevant (and asks before scanning it — or runs in greenfield mode if there's nothing yet), then asks hard questions one at a time — pushing back on contradictions, probing edge cases, and hard-blocking on security gaps. Outputs a production-grade markdown spec with decisions log and implementation order.

Optionally publishes a **diagram-first spec preview as a shareable Claude Artifact** — flow diagrams, an at-a-glance summary, and a dependency graph on a private claude.ai link you can share with teammates for review before finalizing.

## Install

**As a plugin (recommended)** — one command, versioned updates:

```
/plugin marketplace add Sorbh/interview-me
/plugin install interview-me@sorbh
```

**Manual install** — copy the skill files directly:

```bash
mkdir -p ~/.claude/skills/interview-me
curl -o ~/.claude/skills/interview-me/SKILL.md \
  https://raw.githubusercontent.com/Sorbh/interview-me/main/skills/interview-me/SKILL.md
curl -o ~/.claude/skills/interview-me/STYLE_PRESETS.md \
  https://raw.githubusercontent.com/Sorbh/interview-me/main/skills/interview-me/STYLE_PRESETS.md
curl -o ~/.claude/skills/interview-me/VERIFY.md \
  https://raw.githubusercontent.com/Sorbh/interview-me/main/skills/interview-me/VERIFY.md
```

Use one method or the other — installing both ways gives you duplicate skills.

## Usage

```
/interview-me path/to/requirements.md
/interview-me "I want to build a user auth system with OAuth"
/interview-me #42
/interview-me https://github.com/owner/repo/issues/42
/interview-me --verify spec-user-auth.md
```

Point it at a GitHub issue and it pulls the title, body, and comments as the requirement — and offers to post the finished spec back to the issue.

## Drift Detection

Specs rot. Three months after you write one, some of it was never built, some of the code grew past it, and a decision or two got quietly reversed — and nothing tells you which.

```
/interview-me --verify spec-user-auth.md
```

`--verify` re-reads the spec, re-scans the code, and reports where the two disagree:

```
DRIFT REPORT · spec-user-auth.md
baseline 1feea3b → HEAD  ·  11 claims  ·  3 findings  ·  incremental

⚠ major   contradicted  C7   "Sessions are stateless JWTs"
                             src/auth/session.ts:34   [needs-human]
○ minor   relocated     C1   auth/ → src/auth/   (R092)
○ minor   exceeded      —    src/auth/mfa.ts
```

Every finding carries a `file:line` or the searches that came up empty — nothing is reported on vibes. Renames are adjudicated by `git diff -M` first, so moving a file is **one** finding rather than a phantom deletion plus a phantom addition. The report is read-only; nothing is written until you pick a follow-up: re-interview the drifted areas and rewrite those spec sections in place, or record the drift as accepted so it stays quiet on the next run.

Works on specs written before the feature existed, and on greenfield specs with no codebase analysis at all — it derives the claim table from the spec prose on the first run.

---

If this saves you from one bad architectural decision, consider giving it a star.

## License

MIT
