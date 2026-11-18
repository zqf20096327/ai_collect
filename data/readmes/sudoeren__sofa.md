# Sofa

Stop planning in the group chat. Ask for a poll, a trip plan, a cost splitter or a small game, and it appears for everyone at once. Open source and self-hosted.

**Try it: [sofa.erencakar.com](https://sofa.erencakar.com)** (public demo; spaces are deleted after 24 hours without changes)

![Sofa demo](docs/media/demo.gif)

## What it is

You open a space and share its link with your group. People drop in what they already
have: notes, links, files. Then anyone can ask for a tool: "a poll for Friday's dinner",
"split the cabin costs between five of us", "a bracket for the office table tennis cup".
The tool appears in the space and everyone edits it live. Asking again changes the tool
and keeps what people already entered.

## What you can build

Built-in tools, which also work without any AI key:

- **Poll**: ask a question, everyone votes, results update live.
- **Checklist**: things to do or bring, check them off and claim who does what.
- **Availability**: everyone marks the times they can make, the best slot stands out.
- **Table**: a small shared table for anything structured.
- **Expense split**: who paid for what, balances and the shortest way to settle up.
- **Itinerary**: a day-by-day plan with times, places and who is joining.
- **Bracket**: a knockout tournament with byes and automatic advancement.
- **Seating plan**: put guests at tables by dragging them.

Anything else, such as a small game or an unusual layout, is written by the AI as a
free-form tool that runs in a sandboxed frame.

## Quick start

With Docker:

```sh
docker run -d --name sofa -p 8787:8787 -v sofa-data:/data \
  -e OPENROUTER_API_KEY=sk-or-... \
  ghcr.io/sudoeren/sofa:latest
```

Then open http://localhost:8787. Leave out the key to run with the built-in tools only.

With Docker Compose, from a clone of this repository:

```sh
cp .env.example .env    # optional: add an AI key
docker compose up -d
```

Put it behind a reverse proxy for anything beyond your own network:
[docs/self-hosting.md](docs/self-hosting.md).

## AI setup

Sofa works with four kinds of providers, configured on the server:

| Provider                                                 | Variables                                                                                             |
| -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Anthropic                                                | `ANTHROPIC_API_KEY`, optional `SOFA_AI_MODEL` (default `claude-fable-5-2`)                            |
| OpenAI                                                   | `OPENAI_API_KEY`, optional `SOFA_AI_MODEL` (default `gpt-5`)                                          |
| OpenRouter                                               | `OPENROUTER_API_KEY`, optional `SOFA_AI_MODEL` (default `anthropic/claude-haiku-5.5`)                 |
| Any OpenAI-compatible endpoint (Ollama, LM Studio, vLLM) | `SOFA_AI_PROVIDER=openai-compatible`, `SOFA_AI_BASE_URL`, optional `SOFA_AI_API_KEY`, `SOFA_AI_MODEL` |

Members can also bring their own Anthropic, OpenAI or OpenRouter key. It is stored only in their
browser and sent with each request they make; the server uses it for that request and
does not store or log it. A member's key takes precedence over the server's.

With no key at all, requests are matched to the closest built-in tool by keyword.

All variables are listed in [docs/configuration.md](docs/configuration.md).

## How it works

- Each space is one [Yjs](https://yjs.dev) document, synced over a WebSocket and stored in
  SQLite. Every tool keeps its shared data in that document, one key per independently
  edited item, so two people editing at once do not overwrite each other.
- Built-in tools are React components configured by the AI. Free-form tools are complete
  HTML documents that run in an `<iframe sandbox="allow-scripts">` with a Content Security
  Policy that blocks all network access, and talk to the page through a small message API.
- One Node process serves the web app, the REST API and the collaboration socket.

More detail: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) and
[docs/tool-sandbox.md](docs/tool-sandbox.md).

## Security and privacy

- A space's link is its key. Anyone with the link can read and change everything in it.
  Set a password when you create a space if the link might travel further than you want.
- Spaces, files and AI requests stay on your server, apart from what is sent to the AI
  provider you configure.
- Generated tools run sandboxed without network access. A hostile tool could still send its
  own data out by navigating its frame; Sofa detects and resets this, but cannot prevent
  the first request. See [docs/tool-sandbox.md](docs/tool-sandbox.md).
- To report a vulnerability, see [SECURITY.md](SECURITY.md).

## Development

Requires Node 22.5 or newer and pnpm.

```sh
pnpm install
cp .env.example .env    # optional: add an AI key
pnpm dev                # server on :8787, web app on :5173
```

Checks: `pnpm lint`, `pnpm typecheck`, `pnpm test`, `pnpm build`. See
[CONTRIBUTING.md](CONTRIBUTING.md).

## Status

Early. Known gaps:

- No accounts: identity is a name kept in the browser.
- Single process; no horizontal scaling.
- Tested on desktop and narrow browser windows, not yet on real phones.

## Acknowledgements

Inspired by Google Labs' Tabletop experiment. Sofa is an independent project and is not
affiliated with Google.

## License

[MIT](LICENSE)
