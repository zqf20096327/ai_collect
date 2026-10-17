<div align="center">

# Claude Code Practices

### A field-tested playbook for using Claude Code without burning tokens.

[![Stars](https://img.shields.io/github/stars/berkcangumusisik/claude-code-practices?style=for-the-badge&logo=github&color=FFD700&labelColor=000)](https://github.com/berkcangumusisik/claude-code-practices/stargazers)
[![Forks](https://img.shields.io/github/forks/berkcangumusisik/claude-code-practices?style=for-the-badge&logo=github&color=blue&labelColor=000)](https://github.com/berkcangumusisik/claude-code-practices/network/members)
[![License](https://img.shields.io/github/license/berkcangumusisik/claude-code-practices?style=for-the-badge&color=green&labelColor=000)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-82%2B-orange?style=for-the-badge&labelColor=000)](skills/README.md)
[![Made with Claude Code](https://img.shields.io/badge/made_with-Claude_Code-7B4FFF?style=for-the-badge&labelColor=000)](https://claude.com/claude-code)
[![Sponsor](https://img.shields.io/badge/sponsor-%E2%9D%A4-ea4aaa?style=for-the-badge&logo=github&labelColor=000)](https://github.com/sponsors/berkcangumusisik)

<br>

**English** · [**Türkçe**](README.tr.md) · [Full Guide](en/README.md) · [Cheatsheet](CHEATSHEET.md) · [Skills](skills/README.md) · [Contributing](CONTRIBUTING.md)

</div>

---

> **Week 1 with Claude Code, I typed:** *"improve this project."*
>
> Claude read 4 files, edited 2, broke 1. **34,000 tokens.** Nothing was fixed.
> I typed `/cost`. **$0.09 for zero work.**

After a month of figuring out what actually works, the same changes now ship with **60–70% fewer tokens**. This repo is the condensed version.

---

## The 3 Things That Mattered Most

### 1. Specific prompts cost 8.5× less

```diff
- "improve this project"                             → 34,000 tokens
+ "add RFC 5322 validation to validateEmail()
+  at src/auth/login.ts:87"                          →  4,000 tokens
```

Same outcome. One-eighth the cost.

### 2. `/compact` is useless without an instruction

```bash
# Trims almost nothing
/compact

# Cuts 70% of context, quality unchanged
/compact Keep only changed functions and relevant test output
```

In one long session this took me from **82,000 → 11,000 tokens**.

### 3. `.claudeignore` is doing nothing for you right now

```gitignore
node_modules/
dist/
*.log
coverage/
*.lock
```

Six lines. File reads drop **3× to 10×** depending on the project.

---

## What's In This Repo

<table>
<tr>
<td width="33%" valign="top">

#### [Skill Library →](skills/README.md)
**82 ready-made slash commands.**
Copy to `.claude/skills/`, invoke with `/name`.

</td>
<td width="33%" valign="top">

#### [Prompt Templates →](prompts/README.md)
Copy-paste prompt shapes for bug fixes, refactors, reviews, migrations.

</td>
<td width="33%" valign="top">

#### [CLAUDE.md Gallery →](templates/claude-md/README.md)
Framework-ready memory files for Next 16, React 19, Django 5.2, Go 1.26, Rust.

</td>
</tr>
<tr>
<td valign="top">

#### [Hook Recipes →](hooks/README.md)
Drop-in `settings.json` snippets: auto-format, auto-test, secret blocker.

</td>
<td valign="top">

#### [Full Guide →](en/README.md)
Shortcuts, CLAUDE.md, permission modes, MCP, subagents — all in one file.

</td>
<td valign="top">

#### [Cheatsheet →](CHEATSHEET.md)
Bookmark-worthy one-pager. Everything you'll reach for twice a day.

</td>
</tr>
</table>

---

## Skill Library

<details open>
<summary><b>82 skills across categories — click to fold</b></summary>

<br>

| Category | Count | Examples |
|---|:-:|---|
| Git & GitHub | 13 | `/fix-issue` · `/pr-review` · `/commit` · `/release-notes` |
| Testing | 7 | `/test-generate` · `/test-coverage` · `/test-e2e` |
| Frontend | 9 | `/component-gen` · `/seo-check` · `/state-audit` |
| Backend | 10 | `/api-endpoint` · `/auth-middleware` · `/rate-limiter` |
| Mobile | 4 | `/react-native-component` · `/mobile-perf` · `/expo-setup` |
| Security | 3 | `/security-audit` · `/secret-scan` · `/dependency-audit` |
| Database | 6 | `/migration-gen` · `/query-optimize` · `/schema-review` |
| + more | ... | [See all →](skills/README.md) |

</details>

---

## The Workflow

```mermaid
flowchart LR
    A["Vague prompt"] -.->|Wastes tokens| X(["Fail"])
    B["CLAUDE.md<br/>+ .claudeignore"] --> C["Specific prompt"]
    C --> D["Run a skill"]
    D -->|Long session| E["compact with hint"]
    E --> F(["Ship"])
    D --> F

    style X fill:#ff6b6b,stroke:#000,color:#fff
    style F fill:#51cf66,stroke:#000,color:#000
    style B fill:#7B4FFF,stroke:#000,color:#fff
```

---

## Quick Start

**One command** (installs core skills, `.claudeignore`, and `CLAUDE.md` scaffold):

```bash
curl -fsSL https://raw.githubusercontent.com/berkcangumusisik/claude-code-practices/main/install.sh | bash
```

Flags: `--all` for every skill, `--skills a,b,c` to pick.

Or manually:

```bash
git clone https://github.com/berkcangumusisik/claude-code-practices.git
cp -r claude-code-practices/skills ./.claude/skills
claude
> /cost-audit
```

---

## Where To Start

| If you're... | Start here |
|---|---|
| New to Claude Code | [Cheatsheet](CHEATSHEET.md) |
| Paying too much in tokens | Run [`/cost-audit`](skills/cost-audit/SKILL.md) on your session |
| Rewriting the same prompts | [Prompt templates](prompts/README.md) · [Skill Library](skills/README.md) |
| Starting a new project | [CLAUDE.md gallery](templates/claude-md/README.md) |
| Tired of running formatters by hand | [Hook recipes](hooks/README.md) |
| Looking for more resources | [Awesome Claude Code](AWESOME.md) |

---

## FAQ

<details>
<summary><b>Does this work with Claude 4.6 / 4.7?</b></summary>

<br>Yes. Every skill and pattern here is model-agnostic — they're about how you prompt Claude Code, not which model it's pointed at.
</details>

<details>
<summary><b>Do I need to copy all 82 skills?</b></summary>

<br>No. Start with 3–5 you'd actually use this week. Add more as the pain points show up.
</details>

<details>
<summary><b>Will <code>.claudeignore</code> break anything?</b></summary>

<br>No. It only controls what Claude reads — your build and editor are unaffected.
</details>

<details>
<summary><b>How do I measure the savings?</b></summary>

<br>Run <code>/cost</code> before and after a session. The numbers in this README are from my own <code>/cost</code> outputs, not estimates.
</details>

<details>
<summary><b>Can I use this for a team?</b></summary>

<br>Yes. Commit <code>.claude/skills/</code> and a <code>CLAUDE.md</code> to your repo and the whole team picks them up automatically.
</details>

---

## Support the project

If this repo saved you tokens or hours, there are three ways to give back:

- [Star the repo](https://github.com/berkcangumusisik/claude-code-practices) so the next person finds it
- [Sponsor on GitHub](https://github.com/sponsors/berkcangumusisik) to keep new skills and templates coming
- Open a PR with your own patterns (see below)

## Contributing

Found a better pattern, wrote a skill, spotted a bug? PRs welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

<a href="https://github.com/berkcangumusisik/claude-code-practices/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=berkcangumusisik/claude-code-practices" alt="Contributors" />
</a>

---

## Star History

<a href="https://www.star-history.com/?repos=berkcangumusisik%2Fclaude-code-practices&type=date&legend=bottom-right">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=berkcangumusisik/claude-code-practices&type=date&theme=dark&logscale&legend=bottom-right" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=berkcangumusisik/claude-code-practices&type=date&logscale&legend=bottom-right" />
    <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=berkcangumusisik/claude-code-practices&type=date&logscale&legend=bottom-right" />
  </picture>
</a>

---

<div align="center">

**If this saved you tokens, drop a star.** That's how the next person finds it.

<sub>Built by <a href="https://github.com/berkcangumusisik">@berkcangumusisik</a> · MIT License</sub>

<br>

[↑ back to top](#claude-code-practices)

</div>
