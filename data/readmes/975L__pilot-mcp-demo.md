# Pilot MCP demo

[![CI](https://github.com/975L/pilot-mcp-demo/actions/workflows/ci.yml/badge.svg)](https://github.com/975L/pilot-mcp-demo/actions/workflows/ci.yml)
![PHP 8.5](https://img.shields.io/badge/PHP-8.5-777BB4?logo=php&logoColor=white)
![Symfony 8.1](https://img.shields.io/badge/Symfony-8.1-000000?logo=symfony)
![Symfony AI 1.0.0-BETA1](https://img.shields.io/badge/Symfony%20AI-1.0.0--BETA1-000000?logo=symfony)
![mcp/sdk 0.10](https://img.shields.io/badge/mcp%2Fsdk-0.10-2f6feb)
![License MIT](https://img.shields.io/badge/license-MIT-blue)

**Hand a step of a project card to an AI agent: it does the work on your site, with the rights of one account, and asks you on the card what it still needs. Publishing stays yours.**

[![Watch the demo](docs/video.jpg)](https://youtu.be/SsFu2GmnqA0)

▶ [Watch the 90-second film](https://youtu.be/SsFu2GmnqA0) · [PilotBundle's page](https://bundles.975l.com/pages/pilot-bundle)

Built from the open-source [c975L bundles](https://github.com/975L) for the [Symfony AI & MCP Hackathon](https://symfony.com/hackathon).

## Run it

```bash
git clone https://github.com/975L/pilot-mcp-demo && cd pilot-mcp-demo && composer demo
```

Needs PHP 8.5+ (`pdo_sqlite`, `gd`, `intl`, `zip`), Composer, the [Symfony CLI](https://symfony.com/download) and Python 3; `composer demo` says what is missing. Sign in with `editor@example.com` / `lighthouse-demo`, open the card "Release The Lighthouse at Dawn" and click ▶ on its first step. Run it again for a clean take, `composer demo:stop` to stop.

The press kit PDF lands in `var/runner/site-0/card-<id>/`. For a click on the card to open it, declare the `pilot-open://` handler once (Linux, it writes a desktop entry in your session): `PILOT_RUNNER_CONFIG=$PWD/runner python3 vendor/c975l/pilot-bundle/runner/pilot-open.py --install`.

The agent is Claude Code when `claude` is on the `PATH`, otherwise the Symfony AI agent of this repository with `ANTHROPIC_API_KEY`, or any OpenAI-compatible API (`GENERIC_BASE_URL`, `GENERIC_MODEL`). Without one, everything works but "Send to the AI".

## What it unlocked

- **The site is its own MCP server.** With `mcp/sdk`, `/api/mcp` lives inside [CoreBundle](https://github.com/975L/CoreBundle): each bundle adds its tools ([Pilot](https://github.com/975L/PilotBundle), [Book](https://github.com/975L/BookBundle), [Gallery](https://github.com/975L/GalleryBundle), [Social](https://github.com/975L/SocialBundle)), and every call goes through the same checks as the back office, with no second API to keep in step.
- **The site has its own agent.** With Symfony AI and `symfony/ai-mcp-tool`, `app:agent:run` drives the same endpoint on Anthropic or any OpenAI-compatible model, local ones included.
- **The AI joins the project board.** The agent drafts the book, its gallery and the release posts, ticks its steps and asks on the card. Answer there, press **Hand to the machine**, it edits what it made. Posts stay drafts until the editor approves them.

## How it fits together

```
card step ▶  ──>  Pilot run queue  ──>  runner (machine token, actions.yaml)
                                           ▼
                                        AI agent  ──>  /api/mcp (agent token)  ──>  pilot_*, book_*, gallery_*, social_*
```

- `src/Command/DemoSetupCommand.php`: builds the demo through the bundles' own services.
- `src/Command/AgentRunCommand.php`: the Symfony AI agent, its tools drawn from `/api/mcp`.
- `src/Command/PressKitCommand.php`: a plain machine action, no AI, the PDF listed under its step.
- `runner/agent.sh`: agent-agnostic, `AGENT_COMMAND` plugs any other agent, given `MCP_URL`, `MCP_TOKEN` and `CARD_ID`.

## Security

- `/api/mcp` is off until enabled, behind a stateless firewall, and answers 401 without a token.
- An agent token acts as its account only, is limited to the bundles chosen, can be read-only, expires, and is stored as a sha256 hash.
- Every agent write goes to the activity log; the runner only runs the actions of its own `actions.yaml`.
- `.env` holds demo secrets so a clone runs as is: never reuse them.

## Tests

`php bin/phpunit`, with no model or network call: the setup, the MCP endpoint end to end (tools, 401, scoping), the Symfony AI agent on a scripted model, and the runner's contract. The CI also starts `composer demo` and checks the endpoint.

Written with [Claude Code](https://claude.com/claude-code). MIT-licensed.
