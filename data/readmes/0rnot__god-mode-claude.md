<div align="center">

# ⚡ GOD MODE CLAUDE

### One file. Drop it in. Claude Code mass levels up.

<br>

```
Before: "Claude, build a login page"  →  gets spaghetti, breaks half your app
After:  "Claude, build a login page"  →  clean code, tests pass, docs updated
```

<br>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Claude Code](https://img.shields.io/badge/Claude_Code-2025+-blueviolet.svg)](https://docs.anthropic.com/en/docs/claude-code)
[![Lines](https://img.shields.io/badge/CLAUDE.md-under_200_lines-brightgreen.svg)](#why-under-200-lines)

</div>

---

## What is this?

A single `CLAUDE.md` file that makes Claude Code mass dramatically better at its job.

Not a collection. Not a framework. **One file.**

```bash
curl -o CLAUDE.md https://raw.githubusercontent.com/0rnot/god-mode-claude/main/CLAUDE.md
```

Drop it into your project root. Done.

---

## What changes?

| Without | With God Mode |
|:--------|:-------------|
| Claude edits files it shouldn't | ✅ Hard file boundaries enforced |
| Writes code, doesn't test it | ✅ Forced verification loop — tests before marking done |
| Guesses when confused | ✅ Asks clarifying questions when <95% confident |
| Bloated output, repeats your code back | ✅ Lean output, diff-only changes |
| Ignores project conventions | ✅ Reads and follows your stack's patterns |
| One massive commit "fix everything" | ✅ Conventional commits, atomic changes |
| Hallucinates API signatures | ✅ Checks actual source files before writing imports |
| Breaks existing tests | ✅ Runs full suite before and after changes |

---

## The Rules Inside

<details>
<summary><strong>🧠 The Thinking Rules</strong> — How Claude reasons about your code</summary>

```
1. Read before you write — always check existing code patterns first
2. If confidence < 95%, ask clarifying questions before touching files
3. Verify imports and API signatures from actual source, never from memory
4. Explain non-obvious decisions in code comments
```

</details>

<details>
<summary><strong>🛡️ The Safety Rules</strong> — What Claude must never do</summary>

```
1. Never modify: generated files, lock files, .env, migrations, vendor/
2. Before destructive operations: always ask for explicit confirmation
3. Never use bare except/catch — always handle specific errors
4. Never commit secrets, API keys, or credentials
```

</details>

<details>
<summary><strong>⚡ The Quality Rules</strong> — How Claude writes better code</summary>

```
1. Write tests for every new function — run them before marking done
2. Keep functions under 50 lines, files under 300 lines
3. Use the project's existing patterns — don't introduce new paradigms
4. Prefer explicit over clever — readable beats concise
```

</details>

<details>
<summary><strong>📦 The Output Rules</strong> — How Claude communicates</summary>

```
1. Show only changed lines, not entire files
2. Use Conventional Commits: feat/fix/docs/refactor(scope): description
3. One logical change per commit — no "fix everything" commits
4. Don't repeat code the user just showed you
```

</details>

---

## Why under 200 lines?

Anthropic's own engineers found that **CLAUDE.md files over 200 lines degrade Claude's performance**. The model starts ignoring or "forgetting" rules. God Mode stays lean by design — every line earns its place.

> "The best CLAUDE.md is short, opinionated, and enforces verification."
> — Anthropic internal best practice

---

## Customize It

The file has clearly marked sections. Swap in your stack:

```markdown
## Tech Stack          ← Change this
## Commands            ← Change this
## Rules               ← Keep most of these
## Off-Limits          ← Add your generated/vendor paths
```

---

## FAQ

**Q: Does this work with Cursor / Windsurf / other AI editors?**
A: It's optimized for Claude Code, but most rules are universal. Rename to `.cursorrules` or equivalent.

**Q: Will this conflict with my existing CLAUDE.md?**
A: Merge the rules you like. The [Safety Rules](#the-rules-inside) and [Quality Rules](#the-rules-inside) are the highest-impact additions.

**Q: What if my project is huge?**
A: Use `.claude/rules/` directory for topic-specific rules. Keep the root `CLAUDE.md` as the master controller under 200 lines.

---

## Contributing

Found a rule that improves Claude Code's output? Open a PR. But:
- ✅ Must be battle-tested in a real project
- ✅ Must fit within the 200-line budget (something else gets cut)
- ❌ No language/framework-specific rules (keep it universal)

---

<div align="center">

**One file. Massive difference.**

**⭐ Star if Claude Code just got better for you.**

*Made by [0rnot](https://github.com/0rnot)*

</div>
