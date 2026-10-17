# Everything Gemini CLI

A comprehensive Gemini CLI extension with commands, skills, and best practices for software development.

## Credits & Attribution

This project is based on **[everything-claude-code](https://github.com/affaan-m/everything-claude-code)** by **[Affaan Mustafa](https://x.com/affaanmustafa)** - an Anthropic hackathon winner who created the complete collection of Claude Code configs evolved over 10+ months of intensive daily use.

Thank you to Affaan for the incredible work and for open-sourcing it under the MIT license, making this Gemini CLI adaptation possible.

**Original Guides by Affaan:**
- [The Shorthand Guide](https://x.com/affaanmustafa/status/2012378465664745795) - Setup, foundations, philosophy
- [The Longform Guide](https://x.com/affaanmustafa/status/2014040193557471352) - Token optimization, memory persistence, evals

## Features

- **15 Commands**: Pre-configured workflows for planning, TDD, code review, testing, and more
- **14 Skills**: Context-aware best practices that activate automatically
- **Combined Guidelines**: Security, coding style, testing, and git workflow rules
- **MCP Integration**: Ready-to-use Model Context Protocol server configurations

## Installation

### One-Line Install (Recommended)

```bash
gemini extensions install pm-bhatt/everything-gemini-cli
```

That's it! No cloning required.

### Alternative Methods

```bash
# Install from full GitHub URL
gemini extensions install https://github.com/pm-bhatt/everything-gemini-cli

# Or clone and install locally
git clone https://github.com/pm-bhatt/everything-gemini-cli.git
gemini extensions install ./everything-gemini-cli
```

### Verify Installation

```bash
gemini extensions list
```

### Update Extension

```bash
gemini extensions update everything-gemini-cli
```

## Quick Start

After installation, the extension provides:

### Commands (invoke with /command-name)

| Command | Description |
|---------|-------------|
| `/plan` | Create implementation plan before coding |
| `/tdd` | Enforce test-driven development workflow |
| `/code-review` | Comprehensive code review |
| `/build-fix` | Fix TypeScript and build errors |
| `/e2e` | Generate and run E2E tests |
| `/refactor-clean` | Safely remove dead code |
| `/checkpoint` | Create/verify workflow checkpoints |
| `/verify` | Run comprehensive verification |
| `/learn` | Extract reusable patterns |
| `/eval` | Manage eval-driven development |
| `/orchestrate` | Sequential multi-step workflows |
| `/test-coverage` | Analyze and improve test coverage |
| `/update-docs` | Sync documentation from source |
| `/update-codemaps` | Update architecture documentation |
| `/setup-pm` | Configure package manager |

### Skills (activate with /skills skill-name)

Skills provide domain-specific best practices:

| Skill | When to Use |
|-------|-------------|
| `tdd-workflow` | Writing new features, fixing bugs |
| `coding-standards` | All development work |
| `backend-patterns` | API and server-side development |
| `frontend-patterns` | React/Next.js development |
| `postgres-patterns` | Database queries and schemas |
| `clickhouse-io` | Analytics and data engineering |
| `security-review` | Auth, user input, sensitive data |
| `iterative-retrieval` | Complex context retrieval |
| `eval-harness` | Evaluation-driven development |
| `verification-loop` | Quality gate verification |
| `continuous-learning` | Extract patterns from sessions |
| `continuous-learning-v2` | Advanced instinct-based learning |
| `strategic-compact` | Context management |
| `project-guidelines-example` | Project-specific template |

## Configuration

### MCP Servers

Edit `gemini-extension.json` to configure MCP servers:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your-token-here"
      }
    }
  }
}
```

### Environment Variables

Set these in your environment or the extension config:

- `GITHUB_PERSONAL_ACCESS_TOKEN` - For GitHub MCP server
- `FIRECRAWL_API_KEY` - For web scraping capabilities
- `SUPABASE_PROJECT_REF` - For Supabase MCP server

## Project Structure

```
everything-gemini-cli/
├── gemini-extension.json     # Extension manifest
├── GEMINI.md                 # Combined context (rules + guidelines)
├── README.md                 # This file
├── LICENSE                   # MIT license
├── commands/                 # TOML command files (15 files)
│   ├── plan.toml
│   ├── tdd.toml
│   └── ...
├── skills/                   # SKILL.md files (14 skills)
│   ├── tdd-workflow/SKILL.md
│   ├── coding-standards/SKILL.md
│   └── ...
├── contexts/                 # Additional context files
│   ├── dev.md
│   ├── review.md
│   └── research.md
├── docs/                     # Documentation
│   ├── migration-from-claude.md
│   └── feature-parity.md
└── examples/
    └── GEMINI.md
```

## Usage Examples

### Planning a New Feature

```
/plan Add user authentication with OAuth
```

### Test-Driven Development

```
/tdd Implement password reset functionality
```

### Code Review

```
/code-review
```

### Running Verification

```
/verify full
```

## Migration from Claude Code

If you're coming from everything-claude-code, see [migration-from-claude.md](docs/migration-from-claude.md) for details on:
- Command format differences (Markdown -> TOML)
- Agent handling (merged into command prompts)
- Hook limitations (BeforeAgent only in Gemini CLI)
- Feature parity notes

## Feature Parity

Some Claude Code features are not available in Gemini CLI:

| Feature | Claude Code | Gemini CLI | Workaround |
|---------|-------------|------------|------------|
| Agents with tool restrictions | Yes | No | Inline in prompts |
| Model selection per command | Yes | No | N/A |
| PreToolUse hooks | Yes | No | Manual checklist |
| PostToolUse hooks | Yes | No | Manual checklist |
| Auto-formatting on edit | Yes | No | Manual or shell alias |

See [feature-parity.md](docs/feature-parity.md) for full details.

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - see [LICENSE](LICENSE) file.

## Credits

- **Original Author**: [Affaan Mustafa](https://github.com/affaan-m) ([@affaanmustafa](https://x.com/affaanmustafa))
- **Original Project**: [everything-claude-code](https://github.com/affaan-m/everything-claude-code)
- **Gemini CLI Adaptation**: Community contribution
