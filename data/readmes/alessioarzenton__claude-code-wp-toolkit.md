<p align="center">
  <img src="https://img.shields.io/badge/Claude_Code-WP_Kit-7c3aed?style=for-the-badge&logo=anthropic&logoColor=white" alt="Claude WP Kit" />
</p>

<h1 align="center">Claude WP Kit</h1>

<p align="center">
  <strong>A production-ready starter kit to configure <a href="https://claude.ai/code">Claude Code</a> for WordPress projects.</strong>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#installation-options">Options</a> •
  <a href="#whats-included">What's Included</a> •
  <a href="#contributing">Contributing</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue?style=flat-square" alt="Version" />
  <img src="https://img.shields.io/badge/license-GPL--3.0-green?style=flat-square" alt="License" />
  <img src="https://img.shields.io/badge/WordPress-6.x-21759b?style=flat-square&logo=wordpress" alt="WordPress" />
  <img src="https://img.shields.io/badge/PHP-8.2+-777BB4?style=flat-square&logo=php&logoColor=white" alt="PHP" />
  <img src="https://img.shields.io/badge/Bash-3.2+-4EAA25?style=flat-square&logo=gnubash&logoColor=white" alt="Bash" />
</p>

---

Claude WP Kit generates a complete `.claude/` configuration directory tailored to your WordPress project. It provides Claude Code with **skills**, **slash commands**, **subagents**, **hooks**, and **documentation** so it can generate correct, accessible, and performant WordPress code — out of the box.

Supports **Bedrock** and **standard WordPress** installations, with two theme types: **Sage** and **Classic PHP**.

## Features

- **Smart scaffolding** — One interactive script generates a full `.claude/` config customized for your project's stack, theme type, and ACF setup
- **Stack-aware skills** — Claude knows the conventions for Sage + Blade + Tailwind 4 or Classic PHP templates
- **Figma-to-code bridge** — Slash commands to extract design specs from Figma and create UI components directly
- **Accessibility-first** — WCAG 2.2 AA rules baked into every code generation, plus a dedicated audit command
- **Security hooks** — Blocks dangerous bash commands, detects secrets before commits, enforces permission denylists
- **Auto-formatting** — Post-edit hooks run Laravel Pint (PHP) and Prettier (CSS/JS) automatically
- **Community skills** — SEO, performance, systematic debugging, TDD, WP-CLI ops, and more

## Quick Start

### Prerequisites

- An existing WordPress project (Bedrock or standard installation)
- [Claude Code](https://claude.ai/code) installed
- Bash 3.2+

### Install

```bash
# Clone the kit
git clone https://github.com/alessioarzenton/claude-code-wp-toolkit.git ~/claude-wp-kit

# Navigate to your WordPress project root
cd /path/to/my-wordpress-project

# Run the interactive installer
bash ~/claude-wp-kit/bin/init.sh
```

The installer will ask you a few questions about your project (name, theme type, ACF config, etc.) and generate all configuration files.

### Post-install

1. **Install the [WordPress MCP Adapter](https://github.com/WordPress/mcp-adapter/releases)** in your mu-plugins directory
2. **Authenticate Figma MCP** (optional): `/mcp → figma → Authenticate`
3. **Ask Claude Code to populate** the generated scaffold files:
   ```
   "Analyze the theme CSS and fill in memory.md"
   "Analyze the codebase and complete architecture.md"
   ```
4. **Commit** the generated config:
   ```bash
   git add .claude/ CLAUDE.md .mcp.json
   git commit -m "feat: add Claude Code configuration"
   ```

## Installation Options

### Installation Type

| # | Type | Description |
|---|------|-------------|
| 1 | **Bedrock** | Composer-managed structure (`web/app/themes/`) |
| 2 | **Standard WordPress** | Classic installation (`wp-content/themes/`) |

### Theme Type

| # | Theme | Description |
|---|-------|-------------|
| 1 | **Sage** | Blade + Acorn ^5 + Vite + Tailwind CSS 4 |
| 2 | **Classic WP** | PHP templates, no Acorn/Blade |

### ACF Configuration

| # | Option | Availability |
|---|--------|--------------|
| 1 | **ACF Composer** | Sage only (requires Acorn) |
| 2 | **Standard ACF** | All themes |
| 3 | **No ACF** | All themes |

### Valid Combinations

Both themes work with both Bedrock and standard WordPress.

| Theme | ACF Composer | Standard ACF | No ACF |
|-------|:---:|:---:|:---:|
| Sage | ✅ | ✅ | ✅ |
| Classic WP | ❌ | ✅ | ✅ |

## What's Included

### Skills (Rules for Claude)

| Skill | Type | Loading | Description |
|-------|------|---------|-------------|
| `wp-sage` | Stack | Always-active | Sage + Acorn + Blade + TW4 + Vite conventions |
| `wp-classic` | Stack | Always-active | Classic WP PHP template conventions |
| `accessibility` | Core | Always-active | WCAG 2.2 AA — accessible markup rules |
| `wp-rest-api` | Core | Always-active | REST endpoint development & debugging |
| `wp-plugin-development` | Core | Always-active | Plugin architecture, Settings API, security |
| `wp-performance-backend` | Core | Always-active | Profiling, queries, object cache, cron |
| `figma-bridge` | Core | On-demand | Figma → Code workflow with MCP server |
| `code-review` | Project | On-demand | Code review checklist (per-stack variant) |
| `component-workflow` | Project | On-demand | Component creation workflow (per-stack variant) |
| `community/*` | Community | Always-active | Performance, SEO, debugging, TDD, Tailwind DS, WP-CLI ops |

> **On-demand** = `disable-model-invocation: true`. The skill is not loaded until explicitly invoked.
>
> **One stack skill** is installed per project (based on your theme choice).

### Slash Commands

| Command | Description |
|---------|-------------|
| `/component` | Create a UI component from a Figma link |
| `/setup-css` | Import CSS from the design folder into the theme (Sage + design dir only) |
| `/a11y-audit` | Run a WCAG 2.2 AA accessibility audit |
| `/figma` | Analyze a Figma node and extract design specs |

### Custom Subagents

| Subagent | Model | Description |
|----------|-------|-------------|
| `a11y-checker` | Haiku | Scans templates for WCAG 2.2 AA issues (read-only) |
| `figma-analyzer` | Haiku | Analyzes Figma designs and maps to project design tokens |

### Hooks & Automations

| Hook | Event | Description |
|------|-------|-------------|
| `pre-bash-validation.sh` | PreToolUse (Bash) | Blocks dangerous commands (`rm -rf /`, `git push --force main`, etc.) |
| `pre-commit-secrets.sh` | PreToolUse (Bash) | Detects secrets in staged files before `git commit` |
| `post-edit-format.sh` | PostToolUse (Write/Edit) | Auto-format: Pint for PHP/Blade, Prettier for CSS/JS |
| Stop prompt | Stop | Reminds Claude to update `.claude/memory.md` with discoveries |

### Security

| Feature | Description |
|---------|-------------|
| **Permission denylist** | Blocks reading `.env`, `auth.json`, `node_modules/`, `vendor/` |
| **Bash safety** | Prevents destructive shell commands before execution |
| **Secret detection** | Scans staged files for passwords, API keys, tokens before commit |
| **StatusLine** | Shows active model and context usage % in terminal |

### Generated Files

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Main project configuration for Claude Code |
| `.claude/memory.md` | Shared memory (key facts, decisions, patterns) |
| `.claude/settings.json` | Claude Code permissions + hook configuration |
| `.claude/agents/` | Custom subagents (a11y-checker, figma-analyzer) |
| `.claude/hooks/` | Hook scripts (bash validation, secrets, auto-format) |
| `.claude/commands/` | Slash command definitions |
| `.claude/skills/` | Stack, core, project, and community skills |
| `.claude/docs/architecture.md` | Project architecture scaffold |
| `.claude/docs/a11y-known-issues.md` | Accessibility issue tracker |
| `.mcp.json` | MCP server configuration (Figma + WordPress) |

## Project Structure

```
claude-wp-kit/
├── bin/
│   └── init.sh                       # Interactive CLI installer (v1.0.0)
├── core/                             # Files copied as-is to the project
│   └── claude/
│       ├── agents/                   # Custom subagents
│       ├── commands/                 # Slash commands
│       ├── hooks/                    # Hook scripts
│       └── skills/
│           ├── core/                 # Accessibility, Figma, REST API, plugins, performance
│           ├── stacks/              # wp-sage, wp-classic
│           └── community/           # SEO, performance, debugging, TDD, WP-CLI
├── templates/                        # Files processed with variable substitution
│   ├── CLAUDE.md.tmpl
│   └── claude/
│       ├── memory.md.tmpl
│       ├── settings.json.tmpl
│       ├── docs/
│       └── skills/project/
│           ├── code-review/         # Variants: .sage, .classic
│           └── component-workflow/  # Variants: .sage, .classic
├── README.md
├── LICENSE
└── package.json
```

### Core vs Templates

- **`core/`** — Files using Claude's `{{VAR}}` placeholders (double curly braces). Copied as-is — Claude resolves them at runtime.
- **`templates/`** — Project-specific files. The installer replaces placeholders with your values and selects the right variant for your stack/ACF choice.

### Bedrock vs Standard WordPress

The installation type affects:
- **Theme path**: `web/app/themes/` (Bedrock) vs `wp-content/themes/` (standard)
- **MU-plugins path**: `web/app/mu-plugins/` vs `wp-content/mu-plugins/`
- **MCP server**: `--path=web/wp` flag included only for Bedrock

## Configuration

### Tailwind CSS Prefix (optional)

If your project uses a Tailwind CSS 4 prefix (e.g., `rtds`):
- BEM classes will use the prefix: `.rtds-component__element`
- Tailwind utilities will be prefixed: `rtds:flex`, `rtds:md:grid`

### Design System Folder (optional)

If designers maintain a local component library (e.g., `design/`), specifying the path enables:
- The `/setup-css` command for importing CSS from the design into the theme
- Design folder references in documentation
- Component existence checks before creating new ones

### Automatic Compilation with Claude Code

Generated files contain scaffold sections. Instead of filling them manually, just ask Claude Code:

```
"Analyze the theme CSS and fill in the font section in memory.md"
"Analyze the codebase and complete the CPT list in architecture.md"
```

## Updating

To update core skills, subagents, and hooks in an existing project:

```bash
# From your project root
cp -r ~/claude-wp-kit/core/claude/skills/core .claude/skills/
cp -r ~/claude-wp-kit/core/claude/skills/community .claude/skills/
cp -r ~/claude-wp-kit/core/claude/commands/ .claude/commands/
cp -r ~/claude-wp-kit/core/claude/agents/ .claude/agents/
cp -r ~/claude-wp-kit/core/claude/hooks/ .claude/hooks/
chmod +x .claude/hooks/*.sh
```

> Template files (`CLAUDE.md`, `memory.md`, `settings.json`, etc.) should **not** be overwritten — they contain project-specific data.

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feat/my-feature`
3. **Commit** your changes: `git commit -m "feat: add my feature"`
4. **Push** to the branch: `git push origin feat/my-feature`
5. **Open** a Pull Request

### Ideas for Contributions

- New community skills (testing frameworks, CI/CD, Docker, etc.)
- Support for additional theme frameworks
- Translations of skills documentation
- Bug fixes and improvements to the installer

## License

[GPL-3.0](LICENSE) — free to use, modify, and distribute. Derivative works must remain open-source under the same license.

## Credits

Created by [Alessio Arzenton](https://github.com/alessioarzenton).
