# skills

**AI skills for engineers who ship to production.**

AI can generate code all day. Production engineers are responsible for what happens when that code meets real users, real data, and real failure.

These skills build that responsibility into the agent’s workflow. They make it read before writing, trace before changing, test before claiming, and prove before shipping. Your codebase sets the rules. The agent does the work.

## Skills

| Skill                                  | What it does                                                                                                                                                                                                                                                                                                                                                 |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [review-pr](skills/review-pr/) | Reviews someone else's pull or merge request, branch, or commit range. Explains what changed and how it fits the requirement, then reports verified findings and check results. Uses hosted context when available and works with local Git alone. |
| [review-local](skills/review-local/) | Review your own changes before you commit or push. Give `review-local` your staged changes, outgoing commits, or working tree, and it runs the project’s checks against that exact version. It looks for things you didn’t mean to ship, like leftover debug code or a secret in an earlier commit. Each finding points to the code, explains why it matters, and suggests a fix. It applies fixes when you ask. |

Use **review-local** on your own changes before you commit or push, and **review-pr** on someone else's change.

## Install

| Agent                         | Command                                                                                        |
| ----------------------------- | ---------------------------------------------------------------------------------------------- |
| Claude Code                   | `/plugin marketplace add nowaliraza/skills` then `/plugin install review-pr@nowaliraza-skills` or `review-local@nowaliraza-skills` |
| GitHub Copilot CLI            | `/plugin marketplace add nowaliraza/skills` (reads `.claude-plugin/marketplace.json`)          |
| Codex CLI                     | `codex plugin marketplace add nowaliraza/skills`                                               |
| Gemini CLI                    | `gemini extensions install https://github.com/nowaliraza/skills`                               |
| Cursor, VS Code, Kiro, others | Agent Plugins 1.0 (`plugin.json`), or `npx skills add nowaliraza/skills`                       |

Or copy `skills/<name>/` into your agent's skills folder.

## Adding a skill

Create `skills/<name>/SKILL.md`, add a row to the table above, and add it to `.claude-plugin/marketplace.json`. The other manifests pick up everything in `skills/` automatically.
