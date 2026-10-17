<p align="center">
  <img src="assets/banner.webp" alt="GEO-SEO Codex Skill" width="900"/>
</p>

<h1 align="center">geo-seo-codex</h1><br/>
<p align="center">
  GEO-first, SEO-supported website analysis for Codex.
</p>

<p align="center">
  Optimize websites for AI-powered discovery across ChatGPT, Perplexity,
  Gemini, Google AI Overviews, Bing Copilot, and traditional search.
</p>

---

## What This Project Does

**[geo-seo-codex](https://github.com/bytefer/geo-seo-codex.git)** is a Codex skill bundle for Generative Engine Optimization
(GEO) and SEO analysis. It installs `$geo` and `$geo-*` skill invocations into Codex and coordinates
specialized skills, optional Codex subagents, Python utilities, schema templates, and
report templates to audit a website and produce practical recommendations.

Use it to:

- Run full GEO + SEO audits with a composite GEO Score from 0-100
- Check whether AI crawlers can access important pages
- Score content for AI citation readiness
- Generate or validate `llms.txt`
- Audit brand authority signals across AI-cited platforms
- Validate and generate Schema.org JSON-LD
- Review technical SEO foundations that affect AI visibility
- Produce client-ready Markdown and PDF reports
- Manage prospects, proposals, and monthly progress reports for GEO services

---

## Quick Start

### macOS / Linux

```bash
curl -fsSL https://raw.githubusercontent.com/bytefer/geo-seo-codex/main/install.sh | bash
```

### macOS / Linux — Manual

```bash
git clone https://github.com/bytefer/geo-seo-codex.git
cd geo-seo-codex
./install.sh
```

### Windows

Use Git Bash from Git for Windows. PowerShell and Command Prompt are not
supported by the shell installer.

```bash
git clone https://github.com/bytefer/geo-seo-codex.git
cd geo-seo-codex
./install-win.sh
```

After installing, restart Codex so it reloads the new skills and agents.

### Codex Plugin

Use this mode if you want Codex to load the project through
`.codex-plugin/plugin.json` instead of copying skill files directly into
`~/.codex/skills/`.

```bash
mkdir -p ~/plugins
git clone https://github.com/bytefer/geo-seo-codex.git ~/plugins/geo-seo-codex
cd ~/plugins/geo-seo-codex
python3 scripts/install_plugin.py
```

Restart Codex, enable **GEO SEO Codex** from the Personal marketplace, then run:

```text
$geo-setup
```

Plugin mode exposes the skills and works without external agent files. For the
fastest full `$geo-audit` runs, use the classic installer above as well; it
copies the optional parallel agents into `~/.codex/agents/`.

For manual marketplace setup, see [Getting Started](docs/getting-started.md).

---

## Requirements

- Python 3.8+
- Codex CLI
- Git
- Optional: `uv` for faster Python dependency installation
- Optional: Playwright Chromium for screenshot-enabled workflows
- Optional for PDF reports: Pandoc and Google Chrome or compatible Chromium

Install or verify Codex:

```bash
npm install -g @openai/codex
codex --version
```

The shell installer creates an isolated virtual environment at:

```text
~/.codex/skills/geo/.venv/
```

Project dependencies are installed there, so your system Python environment is
not modified.

When used as a Codex plugin, run `$geo-setup` if a workflow needs the bundled
Python utilities and dependencies. Plugin mode keeps scripts, schema templates,
and report templates in the plugin root and can place the runtime venv under
`~/.codex/geo-seo-codex/.venv/`.

---

## Commands

Open Codex in any project directory and run `$geo` skill invocations.

| Command | What it does |
|---------|--------------|
| `$geo-setup` | Initialize plugin/classic runtime dependencies |
| `$geo-audit <url>` | Full GEO + SEO audit with parallel agents first and skills fallback |
| `$geo quick <url>` | 60-second GEO visibility snapshot |
| `$geo-citability <url>` | Score page content for AI citation readiness |
| `$geo-crawlers <url>` | Check robots.txt, meta robots, headers, and AI crawler access |
| `$geo-llmstxt <url>` | Analyze or generate `llms.txt` |
| `$geo-brand-mentions <url>` | Scan brand/entity signals across AI-cited platforms |
| `$geo-platform-optimizer <url>` | Platform-specific readiness for AIO, ChatGPT, Perplexity, Gemini, and Copilot |
| `$geo-schema <url>` | Detect, validate, and generate structured data |
| `$geo-technical <url>` | Technical SEO audit with AI-crawler visibility checks |
| `$geo-content <url>` | Content quality and E-E-A-T assessment |
| `$geo-report <url>` | Generate a client-ready Markdown report |
| `$geo-report-pdf <url>` | Generate a styled PDF report with charts and score visuals |
| `$geo-prospect <cmd>` | CRM-lite prospect pipeline management |
| `$geo-proposal <domain>` | Generate a client proposal from audit data |
| `$geo-compare <domain>` | Generate monthly delta and progress reports |
| `$geo-update` | Update the installed Codex skill bundle |

Example:

```text
$geo quick https://example.com
$geo-audit https://example.com
$geo-report-pdf https://example.com
```

---

## Architecture

```text
geo-seo-codex/
├── .codex-plugin/               # Codex plugin manifest
├── skills/                      # Plugin-discoverable skills and specialized GEO sub-skills
│   ├── geo/                     # Main Codex skill orchestrator
│   └── geo-*/                   # Specialized GEO sub-skills
├── agents/                      # Optional Codex TOML agent definitions
├── scripts/                     # Python utilities
├── schema/                      # JSON-LD templates
├── templates/                   # HTML/CSS report templates
├── white-label/                 # Optional branding configuration
├── docs/                        # User and contributor documentation
├── install.sh                   # macOS/Linux installer
├── install-win.sh               # Windows Git Bash installer
├── uninstall.sh                 # Uninstaller
└── requirements.txt             # Python dependencies
```

### Codex Plugin Packaging

This repository includes a Codex plugin manifest at
`.codex-plugin/plugin.json`. The plugin exposes the GEO skills through
`skills/`, while the existing `install.sh` and `install-win.sh` scripts remain
available for classic installation. In plugin mode, `$geo-setup` initializes or
repairs the local runtime used by script-backed workflows.

Installed layout:

```text
~/.codex/
├── skills/
│   ├── geo/
│   └── geo-*/
└── agents/
    └── geo-*.toml
```

---

## Scoring

The composite GEO Score is calculated from six weighted categories:

| Category | Weight |
|----------|--------|
| AI Citability and Visibility | 25% |
| Brand Authority Signals | 20% |
| Content Quality and E-E-A-T | 20% |
| Technical Foundations | 15% |
| Structured Data | 10% |
| Platform Optimization | 10% |

---

## Local Data Storage

Prospect, audit, proposal, and report data is stored outside the Codex skill
installation directory:

```text
~/.geo-prospects/
├── prospects.json
├── audits/
├── proposals/
└── reports/
```

The uninstaller does not remove this directory. Keep it when backing up or
migrating client data, and delete it manually only if you no longer need your
prospect and reporting records.

---

## Documentation

- [Getting Started](docs/getting-started.md)
- [Commands Reference](docs/commands-reference.md)
- [Architecture](docs/architecture.md)
- [Skills and Agents](docs/skills-and-agents.md)
- [Scoring Methodology](docs/scoring-methodology.md)
- [FAQ](docs/faq.md)
- [Contributing](CONTRIBUTING.md)

---

## Uninstall

Run from the cloned repository:

```bash
./uninstall.sh
```

The uninstaller removes only files marked as installed by this project, so it will skip unmarked `geo-*` skills or agents that may belong to you or another plugin.

Or remove the installed files manually after reviewing the paths:

```bash
rm -rf ~/.codex/skills/geo ~/.codex/skills/geo-* ~/.codex/agents/geo-*.toml
```

To remove prospect and report data:

```bash
rm -rf ~/.geo-prospects
```

---

## Acknowledgements

This project is adapted from
[zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude),
which provided the original GEO/SEO workflow foundation.

Thanks to the original project and its author. `geo-seo-codex` builds on that
work and refactors the workflow, skills, agents, installation scripts, and
runtime setup so the toolkit can be used more naturally inside Codex.

If you use Claude Code, the original
[geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude)
project may be the better fit.

---

## License

See [LICENSE](LICENSE).
