# Ralphy

Ralphy gives your coding agent a trend base that refreshes itself and watches your own niche, a local panel with **Content** and **Accounts**, and the ability to post to your own accounts through your agent. A component base (reusable effects, layouts and assets) is coming.

It is a plugin: agent skills plus the `ralphy` command-line program. You ask in chat; the agent drives the CLI.

## Install

**Claude Code**

```
/plugin marketplace add alecs5am/ralphy
/plugin install ralphy@ralphy
```

A SessionStart hook downloads the `ralphy` binary for the plugin's version on first run and puts it on PATH for the session. Nothing happens when a new enough binary is already installed.

**Codex**

```
codex plugin marketplace add alecs5am/ralphy
```

Codex does not run the hook, so install the binary yourself:

```
curl -fsSL https://raw.githubusercontent.com/alecs5am/ralphy/main/install.sh | sh
```

**Other agents**

```
npx skills add alecs5am/ralphy
curl -fsSL https://raw.githubusercontent.com/alecs5am/ralphy/main/install.sh | sh
```

`install.sh` accepts `RALPHY_VERSION=v0.4.0` (pin a release), `RALPHY_BIN_DIR` (default `~/.local/bin`) and `RALPHY_NO_RC=1` (leave shell rc files alone).

## First run

```
ralphy setup      # creates your data root; FAL_KEY is required, ElevenLabs and OpenRouter are optional
ralphy panel      # opens the local panel on 127.0.0.1
```

`ralphy setup` initializes the data root and prints how to store provider keys (`ralphy provider auth set <provider> --stdin`, typed in your own terminal, never in chat). Without a source checkout the data root is `~/.ralphy`.

Then ask your agent, for example:

- "What is trending in my niche this week? Show me the three scripts worth copying."
- "Make a 30-second short from the best one, for my UI Effects account, and show me the cost first."

## What it stores and sends

All data stays in the local data root. Provider calls go to the services whose keys you set; nothing goes to the Ralphy authors. Details in [PRIVACY.md](PRIVACY.md).

## Developing Ralphy

See [docs/developing-ralphy.md](docs/developing-ralphy.md). Checks: `bun run lint`, `bun test tests/unit`.

License: [Apache-2.0](LICENSE).
