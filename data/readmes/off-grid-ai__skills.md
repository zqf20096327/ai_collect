# Stop babysitting your AI. Make it build, test and ship like a senior team.

These are the skills I use every day. I built [Off Grid AI](https://github.com/off-grid-ai/OGAM) on my own with them, and it reached 250,000+ downloads on 7 platforms without spending a dollar on ads. Install them and your AI works the way mine does.

[![Off Grid AI, built by one person with these skills: 250,000+ organic downloads on 7 platforms](assets/built-with-these-skills.png)](https://www.wednesday.is/mcp/)

## What these skills do

Vibe coding gets you a demo in an afternoon. Then your AI breaks things that already worked, every screen looks like every other AI app, and you're asked to approve 50 changed files you can't read.

Each skill is a short playbook your agent reads before it starts, so it tests every change in your real app and checks it before you see anything. They're free, MIT licensed, and work in Claude Code, Codex, Cursor and 60+ other agents.

- [Review like a senior engineer, without reading code](review)
- [Your AI stops breaking things that already worked](testing)
- [Change old code without breaking it](codebase)

![How it works: you ask for a change, your agent maps everything it touches, makes it, checks it, and hands you one page with only the calls that need you](assets/how-it-works.png)

Rather not install anything? Add the free [Wednesday MCP](https://www.wednesday.is/mcp/) to Claude, Claude Code, Cursor or Codex. It takes a minute.

## Install in one line

Paste this into your agent:

```text
Install the skills from github.com/off-grid-ai/skills
```

Or run it yourself:

```bash
npx skills add off-grid-ai/skills
```

<details>
<summary>Other ways: Claude Code plugin, Codex plugin, no Node</summary>

**Claude Code**
```bash
claude plugin marketplace add off-grid-ai/skills
for s in off-grid-review off-grid-testing off-grid-codebase; do claude plugin install $s@off-grid-ai; done
```

**Codex**
```bash
codex plugin marketplace add off-grid-ai/skills
for s in off-grid-review off-grid-testing off-grid-codebase; do codex plugin add $s@off-grid-ai; done
```

Each set is its own plugin, so you can drop any you don't want. Skills call each other across sets, so installing all 3 is the safe choice.

**Any agent, no Node**
```bash
curl -fsSL https://raw.githubusercontent.com/off-grid-ai/skills/main/install.sh | bash
```
It links every skill into each agent it finds on your machine. Run it again to update.

</details>

## Try these first

**[test-like-a-user](testing/skills/test-like-a-user): tests that catch what your users would hit.** It opens the real screen, taps the real button and checks what you'd see. No mocks of your own code, so a green test means it really works.

> *"/test-like-a-user the checkout flow"*

**[blast-radius](codebase/skills/blast-radius): know what a change breaks before you make it.** It finds everything that depends on the file or function you're about to touch, scores the risk, and stops for your yes when it's high.

> *"/blast-radius before I change the auth middleware"*

**[safe-to-merge](review/skills/safe-to-merge): pull requests that are actually ready.** It audits the diff, answers every review comment, fixes behind the checks and re-reviews until nothing blocking is left.

> *"/safe-to-merge this PR"*

## All 15 skills

### [Review like a senior engineer, without reading code](review)

Your AI changes 50 files and you can't tell what broke. Every change gets a pass or fail against one clear bar, and every review comment gets answered and fixed before it merges.

![How review like a senior engineer, without reading code works](assets/sets/review-how-it-works.png)

| Skill | What you get |
| --- | --- |
| [**safe-to-merge**](review/skills/safe-to-merge) | Your pull request gets every review comment answered and fixed until it's safe to merge. |
| [**code-check**](review/skills/code-check) | A pass or fail on every change before it ships, against one clear bar. |
| [**never-twice**](review/skills/never-twice) | Every review teaches your AI, so the same mistake never comes back. |

### [Your AI stops breaking things that already worked](testing)

You fix one bug and two old features break. Every change gets tested by tapping through your app like a real user, with no mocks hiding the breakage.

![How your ai stops breaking things that already worked works](assets/sets/testing-how-it-works.png)

| Skill | What you get |
| --- | --- |
| [**test-like-a-user**](testing/skills/test-like-a-user) | Tests that open the real screen, tap the real button and check what you'd see. No mocks of your own code. |
| [**bug-trap**](testing/skills/bug-trap) | Every bug gets a test that fails first, so it can't sneak back in. |
| [**dont-break-it**](testing/skills/dont-break-it) | Your AI changes, checks and saves code so nothing half-done ships. |
| [**fix-it-for-real**](testing/skills/fix-it-for-real) | It fixes the cause, not the symptom, and reuses what someone already solved. |
| [**click-everything**](testing/skills/click-everything) | It clicks through every page of your web app and fixes what breaks. |

### [Change old code without breaking it](codebase)

You inherit a codebase nobody fully understands, and every change is a guess. Your AI maps it first, shows you what each change will break, and adds tests before it touches anything risky.

| Skill | What you get |
| --- | --- |
| [**learn-this-codebase**](codebase/skills/learn-this-codebase) | Ask anything about a codebase you've never seen, and get answers with the file and line. |
| [**blast-radius**](codebase/skills/blast-radius) | See everything a change will break before it's made. Risky edits wait for your yes. |
| [**tests-for-old-code**](codebase/skills/tests-for-old-code) | Tests for code that never had any, each one run and passing before you see it. |
| [**audit-a-module**](codebase/skills/audit-a-module) | Find out whether to refactor, rewrite or leave a module alone, on one screen. |
| [**stay-in-the-lines**](codebase/skills/stay-in-the-lines) | Your architecture stays the way you drew it, because every change gets checked against your rules. |
| [**plan-from-scratch**](codebase/skills/plan-from-scratch) | Starting fresh? An architect, a product lead and a security lead plan it, and show you where they disagree. |
| [**deploy-without-fear**](codebase/skills/deploy-without-fear) | Deploy on any day. It checks before and after, and tells you the moment to roll back. |

## Get all 15

```bash
npx skills add off-grid-ai/skills
```

Or paste "Install the skills from github.com/off-grid-ai/skills" into your agent.

## Good to know

- Each skill is a folder with a `SKILL.md`, plain Markdown your agent reads when your request matches it. Nothing runs until you ask.
- Review pages publish as Claude Artifacts when you have them, and as a local HTML page when you don't.
- Skills mention each other by name. Install the whole set to get everything working together.
- The codebase skills started at [Wednesday](https://www.wednesday.is/mcp/) and now need nothing else installed.
- MIT licensed. Third-party files keep their own licenses (see `NOTICE` files).

Made by [Mac](https://github.com/alichherawalla). Follow me on GitHub for new skills as they ship.
