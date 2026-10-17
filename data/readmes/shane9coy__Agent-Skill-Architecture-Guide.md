# Agent Skills Architecture Guide

![Agent Skills Architecture Guide cover](assets/title-cover.png)

📄 Get the Full Guide

[Download the Agent Skills Architecture Guide v2 PDF](Agent-Skills-Architecture-Guide-v2.pdf)

The guide covers agent folder structure, `AGENTS.md`, `SKILL.md` anatomy, frontmatter reference, orchestration folders, command-folder equivalents, self-hosted model notes, troubleshooting, and reusable skill patterns.

> Copy the included `AGENTS.md` and skill file set into your canonical global agent folders, then replace the placeholder Git identity fields with your own name, email, and GitHub username.

`AGENTS.md` solves the following issues with your coding agent:

- Git branch chaos and generated branch pollution
- Agents treating Git branches like disposable sandboxes
- Context mangling and drift between passes
- Speed running without step by step updates or explaining architecture and the why behind it
- Yes-man loops and reflex apology responses; No more "You're absolutely right!"
- Pausing after every section of a long prompt instead of finishing the full task
- Weak self-review and missed requirements from long or detailed prompts
- Overbuilding,  bloated abstractions, and undocumented codebases

This repo now focuses on a simplified layout:

- `AGENTS.md`: public template for agent behavior, Git hygiene, contextual editing, implementation review, and handoff discipline.
- `skills/agent-copy/`: reusable skill for copying your canonical global instructions into any project repo and appending repo-specific guidance.
- `skills/new-skill-builder/`: reusable skill for creating, installing, validating, and auditing agent skills.
- `skills/new-mcp-builder/`: reusable skill for planning and building MCP server integrations.
- `Agent-Skills-Architecture-Guide.md`: Markdown source for the guide.
- `Agent-Skills-Architecture-Guide-v2.pdf`: PDF version of the guide.

For quick, optimized subagent execution after your base instructions are installed, also check out [Subagent-Driven Development](https://github.com/shane9coy/subagent-driven-development). It adds scoped workers, branch/worktree discipline, progress tracking, and review gates for multi-agent implementation work.

## Install

The easiest install path is to give this repo to your coding agent and let it copy the instruction file and skills into the right local folders.

Copy this prompt into Codex, Claude Code, or another local coding agent:

```text
Install the Agent Skills Architecture Guide into my local agent setup.

Repo: https://github.com/shane9coy/Agent-Skill-Architecture-Guide

Tasks:
1. Clone or download the repo.
2. Copy the repo's AGENTS.md into my canonical global agent instruction file.
   - Default Codex target: ~/.codex/AGENTS.md
   - If I use Claude Code or another agent, ask me to confirm the correct global instruction path before writing.
3. Copy these skills into my agent skills folder:
   - skills/agent-copy
   - skills/new-skill-builder
   - skills/new-mcp-builder
4. Default Codex skills target: ~/.codex/skills/
5. Claude Code skills example: ~/.claude/skills/
6. Do not overwrite an existing AGENTS.md or skill folder without showing me what will change first.
7. Verify the installed files exist and report the final paths.
```

### Manual Install

Codex is the default example in this repo. The manual install copies:

```text
AGENTS.md -> ~/.codex/AGENTS.md
skills/*  -> ~/.codex/skills/
```

Run from the directory where you want to download the repo:

```bash
git clone https://github.com/shane9coy/Agent-Skill-Architecture-Guide.git
cd Agent-Skill-Architecture-Guide

mkdir -p "$HOME/.codex" "$HOME/.codex/skills"

cp AGENTS.md "$HOME/.codex/AGENTS.md"
cp -R skills/agent-copy "$HOME/.codex/skills/"
cp -R skills/new-skill-builder "$HOME/.codex/skills/"
cp -R skills/new-mcp-builder "$HOME/.codex/skills/"
```

Then open `~/.codex/AGENTS.md` and replace:

- `<YOUR_GIT_AUTHOR_NAME>`
- `<YOUR_GIT_AUTHOR_EMAIL>`
- `<YOUR_GITHUB_USERNAME>`

Claude Code users can use the same repo files, but the destination folders are different. Common examples:

```text
Claude skills folder: ~/.claude/skills/
Claude project instructions: CLAUDE.md or the project instruction file your Claude setup uses
```

Keep the same model no matter which agent you use:

```text
canonical global instructions -> repo-local AGENTS.md -> repo-specific tail
```

## Recommended Workflow

1. Install `AGENTS.md` globally so every agent session starts with the same operating rules.
2. Install `agent-copy` so your agent can create repo-local `AGENTS.md` files without manual copy/paste.
3. Run `agent-copy` inside each important repo so local sessions have a reliable fallback.
4. Add repo-specific guidance underneath the global rules: stack, commands, branch rules, build/test flow, project boundaries, and known risks.
5. Install `new-skill-builder` when you want your agent to create or validate skills.
6. Install `new-mcp-builder` when you want your agent to plan or build MCP integrations.

After installing `agent-copy`, open a target project and ask your agent:

```text
Use agent-copy to create or refresh this repo's AGENTS.md from my canonical global instructions, then add repo-specific guidance based on the files in this project.
```

If your canonical source is not `~/.codex/AGENTS.md`, provide the exact source path:

```text
Use agent-copy with SOURCE_AGENTS=/path/to/my/global/instructions.md to create or refresh this repo's AGENTS.md, then add repo-specific guidance based on the files in this project.
```

## What's Inside

```text
Agent-Skill-Architecture-Guide/
├── AGENTS.md
├── Agent-Skills-Architecture-Guide.md
├── Agent-Skills-Architecture-Guide-v2.pdf
├── README.md
├── LICENSE
└── skills/
    ├── agent-copy/
    │   └── SKILL.md
    ├── new-mcp-builder/
    │   ├── SKILL.md
    │   └── references/
    └── new-skill-builder/
        ├── SKILL.md
        └── references/
```

## What The Skills Do

### `agent-copy`

Use this skill when you want an agent to:

- Copy your canonical global instructions into the current repo's `AGENTS.md`.
- Preserve the canonical rules exactly.
- Add repo-specific guidance based on the current codebase.
- Keep future repo-local `AGENTS.md` files aligned with your global operating rules.
- Use Codex's `~/.codex/AGENTS.md` by default, while allowing another canonical source path when needed.

### `new-skill-builder`

Use this skill when you want an agent to:

- Create a new skill from scratch.
- Install a skill from GitHub, ZIP, or Markdown.
- Validate a skill's structure and frontmatter.
- Audit an agent skill folder.
- Move long reference material out of `SKILL.md` and into `references/`.

### `new-mcp-builder`

Use this skill when you want an agent to:

- Plan a new MCP server.
- Define tool surfaces and schemas.
- Document setup, auth, environment variables, and safety boundaries.
- Create implementation notes for MCP integrations.
- Review an MCP server for usability and agent compatibility.

## Compatibility

This repo uses the shared AgentSkills pattern:

| Tool | Suggested instruction file | Suggested skill folder |
|------|----------------------------|------------------------|
| OpenAI Codex | `AGENTS.md` | `.codex/skills/`, `.agents/skills/`, or repo `skills/` |
| Hermes Agent | `AGENTS.md` or context files | Hermes skills path or repo `skills/` |
| KiloCode | `AGENTS.md` | `.kilocode/skills/` |
| Claude Code | `CLAUDE.md` / project instructions | `.claude/skills/` |
| OpenCode | tool-specific context | `.opencode/skills/` |
| Cursor / Windsurf / Cline | tool-specific context | compatible imported skills folder |
| Any AgentSkills agent | tool-specific context | repo `skills/` |

## Key Concepts

- **`AGENTS.md`**: Durable agent instructions for behavior, Git hygiene, contextual editing, stack conventions, verification, and handoff expectations.
- **`SKILL.md`**: Skill entrypoint with YAML frontmatter for discovery and Markdown body for instructions.
- **`references/`**: Supporting material loaded only when needed.
- **Progressive disclosure**: Keep the core skill short and move deeper examples or guides into references.
- **Description is the trigger**: The model matches the request against skill descriptions, so put "when to use" guidance in the description.

## Credits

Compiled by [@shaneswrld_](https://github.com/shane9coy)

## License

MIT — use it, fork it, ship it. All I ask for is credit where credit is due.
