# GitHubCard skills for Claude Code

A Claude Code plugin marketplace from [GitHubCard](https://githubcard.com). The
`githubcard` plugin lets Claude create GitHub profile and repository cards and add
them to README files, link previews and social posts.

It has two parts:

- **Skill** (`skills/githubcard/SKILL.md`): when and how to make a card, how to
  edit a layout, how to place it in a README, and what to do for each error code.
  It drives the [`ghcard` CLI](https://github.com/ghcardhq/ghcard), run through
  `npx` when it is not installed.
- **MCP server**: the hosted GitHubCard server at `https://githubcard.com/mcp`,
  so Claude can call the same tools without a shell.

## Install

```bash
claude plugin marketplace add ghcardhq/skills
claude plugin install githubcard@githubcard
```

Or inside Claude Code: `/plugin marketplace add ghcardhq/skills`, then
`/plugin install githubcard@githubcard`.

Claude Code asks for a **GitHubCard API key** when the plugin is enabled. Create
a free one at [githubcard.com/dashboard](https://githubcard.com/dashboard). It is
stored as a secret and sent only to `githubcard.com`. You can skip it and still
browse templates and palettes. Card creation needs the key.

Then ask Claude things like:

> Make a GitHubCard for my profile and put it at the top of my profile README.
>
> Create a repo card for this project with a dark navy background.

## Other agents

The skill is a plain [Agent Skills](https://agentskills.io) folder. To use it
without the plugin, copy `plugins/githubcard/skills/githubcard` into your agent's
skills directory, for example:

```bash
git clone --depth 1 https://github.com/ghcardhq/skills /tmp/ghcard-skills
mkdir -p ~/.claude/skills && rsync -a /tmp/ghcard-skills/plugins/githubcard/skills/githubcard ~/.claude/skills/
```

For MCP setup in Cursor, VS Code, Windsurf, Codex and other clients, see
[ghcardhq/githubcard-mcp](https://github.com/ghcardhq/githubcard-mcp).

## Privacy

Card requests go to githubcard.com and use public GitHub data only. See the
[privacy policy](https://githubcard.com/~privacy).

## License

MIT
