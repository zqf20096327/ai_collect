# Nautobot Agent

![Nautobot Agent banner](docs/media/repo-banner.png)

<p align="center">
  <a href="https://github.com/gt732/nautobot-app-nautobot-agent/actions/workflows/ci.yml"><img src="https://github.com/gt732/nautobot-app-nautobot-agent/actions/workflows/ci.yml/badge.svg?branch=main" alt="CI"></a>
  <a href="https://github.com/gt732/nautobot-app-nautobot-agent/actions/workflows/docs.yml"><img src="https://github.com/gt732/nautobot-app-nautobot-agent/actions/workflows/docs.yml/badge.svg?branch=main" alt="Documentation"></a>
  <a href="https://pypi.org/project/nautobot-agent/"><img src="https://img.shields.io/pypi/v/nautobot-agent" alt="PyPI"></a>
  <a href="https://pypi.org/project/nautobot-agent/"><img src="https://img.shields.io/pypi/pyversions/nautobot-agent" alt="Python"></a>
  <a href="https://gt732.github.io/nautobot-app-nautobot-agent/"><img src="https://img.shields.io/badge/docs-live-brightgreen" alt="Docs"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/gt732/nautobot-app-nautobot-agent" alt="License"></a>
</p>

Nautobot Agent is a general-purpose conversational agent integrated into Nautobot. Use it to ask questions, explore ideas, and get explanations or code examples in chat; connect conversations to Nautobot inventory and installed-App knowledge through permission-aware built-in tools.

**Privacy and trust:** Messages, relevant Nautobot data, and authorized source text are sent to the configured model provider. Tracing is enabled by default and may contain unredacted prompts and tool data. Built-in tools are permission-aware and read-only; optional MCP servers are a separate trust boundary and may have broader access or external effects. Review [Privacy and data handling](https://gt732.github.io/nautobot-app-nautobot-agent/user/privacy/) before use.

## See it in action

https://github.com/user-attachments/assets/22389952-30f5-4630-96a9-60aab28e4081

## How it works

![Nautobot Agent chat lifecycle: from question to answer](docs/media/nautobot-agent-from-question-to-answer.gif)

## What you can do

- Get help with general questions, explanations, and code examples in chat; use permission-aware, read-only built-in tools for Nautobot inventory and authorized installed-App source.
- Use native integrations for OpenAI, Anthropic, Google Gemini Developer API, Ollama, OpenRouter, and DeepSeek.
- Explore results with charts and Mermaid diagrams, and save conversations.
- Extend the assistant with optional custom skills and MCP integrations.
- Inspect execution traces with bounded previews and authorized full JSON view or download.

The default scope policy admits Nautobot-related requests. Administrators can change it to allow broader, general-purpose requests; this does not broaden built-in Nautobot data permissions. See [Scope policy](https://gt732.github.io/nautobot-app-nautobot-agent/admin/configuration/#scope-policy).

Built-in tools cannot create or modify files. File operations are possible only if an administrator enables MCP tools that provide them; those tools are a separate trust boundary.

### Screenshots

Chat with Nautobot Agent:
![Nautobot Agent screenshot](docs/media/nautobot-agent-screenshot.png)

Chart rendering:
![Nautobot Agent Chart screenshot](docs/media/nautobot-agent-chart-screenshot.png)

Mermaid diagram rendering:
![Nautobot Agent Mermaid screenshot](docs/media/nautobot-agent-mermaid-screenshot.png)

MCP Integration with Nautobot Agent:
![Nautobot Agent MCP screenshot](docs/media/nautobot-agent-mcp-screenshot.png)

Agent Observability and tracing with Nautobot Agent:
![Nautobot Agent Trace screenshot](docs/media/nautobot-agent-trace-screenshot.png)

## Documentation

- [Overview](https://gt732.github.io/nautobot-app-nautobot-agent/user/app_overview/)
- [Getting started](https://gt732.github.io/nautobot-app-nautobot-agent/user/getting_started/)
- [Installation](https://gt732.github.io/nautobot-app-nautobot-agent/admin/install/)
- [Configuration](https://gt732.github.io/nautobot-app-nautobot-agent/admin/configuration/)
- [Integrations](https://gt732.github.io/nautobot-app-nautobot-agent/admin/integrations/)
- [Operations](https://gt732.github.io/nautobot-app-nautobot-agent/admin/operations/)
- [Compatibility](https://gt732.github.io/nautobot-app-nautobot-agent/admin/compatibility/)
- [FAQ](https://gt732.github.io/nautobot-app-nautobot-agent/user/faq/)

For how this documentation is maintained, see [Building documentation](https://gt732.github.io/nautobot-app-nautobot-agent/dev/documentation/).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for our branching and pull request policy.

With Docker and Docker Compose installed, copy
`development/nautobot_config.example.py` to `development/nautobot_config.py`
once, then run `docker compose up` from the repository root. The local
configuration is ignored by Git and can be edited freely.
Open <http://localhost:8080> and sign in with `admin` / `admin`.
The stack installs the app and its pinned Nautobot development version.
See [Docker development](https://gt732.github.io/nautobot-app-nautobot-agent/dev/docker/) for requirements, checks, and
local-only security restrictions.

## License

MIT
