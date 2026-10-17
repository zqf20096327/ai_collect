# 😤 DopeForge

> **Give your AI agent every public API on the internet. One command.**

```bash
pip install "dopeforge[mcp]"
forge mcp    # ← your agent now discovers and calls real public APIs
```

Ask Claude *"what's the weather in Tokyo, the current Bitcoin price, and a cat fact"* —
and watch it **discover and call three public APIs it had never heard of**, live, through
one MCP server. No per-API setup. No keys. Nothing leaves your machine except the API
calls themselves.

## What this is

Every awesome-list on GitHub is discovery **for humans**: a giant markdown file you
Ctrl-F through, full of links that died silently years ago. DopeForge is the opposite —
**a living catalog built for agents (and impatient humans)**:

1. **One registry — 6,623 entries.** The biggest developer catalogs on GitHub, **838k+
   combined stars** of curated markdown, parsed, validated, and merged into one
   searchable database:

   | Source | Entries | Brings |
   |---|---:|---|
   | [public-apis](https://github.com/public-apis/public-apis) ⭐474k | 1,721 | Public APIs + auth/HTTPS/CORS metadata |
   | [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) ⭐93k | 3,482 | MCP servers tagged by language/scope |
   | [free-for-dev](https://github.com/ripienaar/free-for-dev) ⭐136k | 1,304 | Dev services with free tiers |
   | [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) ⭐135k | 116 | LLM apps, agents, RAG examples |

2. **Actually callable.** Catalogs give you a link. DopeForge gives you **blueprints** —
   small, hand-verified specs (base URL, endpoints, params) that make APIs invocable
   right now, from the CLI or from your agent:

   ```bash
   forge try public-apis-open-meteo forecast --param latitude=35.68 --param longitude=139.69
   ```

3. **Proven alive.** `forge check` calls every blueprinted API for real, and a nightly
   CI run does it in the cloud. Awesome lists rot — while building v1 we found entire
   categories of "popular" APIs that are already dead (expired TLS certs, no HTTPS
   listener, deprecation stubs — receipts in
   [docs/blueprint-notes.md](docs/blueprint-notes.md)). Those never made it in. **Your agent is never handed a
   dead tool.**

## For humans: the CLI

```bash
pip install dopeforge           # registry snapshot ships inside — works offline, instantly

forge search "sentiment analysis"            # search all 4 catalogs at once
forge search image --kind api --no-auth      # public APIs needing zero keys
forge search database --kind mcp-server      # MCP servers only
forge info public-apis-open-meteo            # full details for one entry
forge try public-apis-cat-facts-2            # call an API right from your terminal
forge stats                                  # what's in the registry
forge sync                                   # refresh from the live sources
forge check                                  # liveness-test every blueprint
forge random                                 # feeling lucky
```

Kinds: `api` · `mcp-server` · `free-service` · `llm-app`

> Until the first PyPI release lands, install from source:
> `pip install "dopeforge[mcp] @ git+https://github.com/DreadpiratePickles/dopeforge"`

## For agents: the MCP server

```json
{ "mcpServers": { "dopeforge": { "command": "forge", "args": ["mcp"] } } }
```

Three tools, safe by construction:

- **`discover`** — search the whole registry with filters
- **`inspect`** — full metadata + call blueprint for any entry
- **`call_api`** — invoke a blueprinted API (GET-only, no-auth-only, HTTPS-only,
  validated params, bounded responses, explicit timeouts — the agent can't spend your
  money or leak your keys, because there are no keys)

The 15 launch blueprints cover weather, crypto prices, IP/geo, dictionary, books,
exchange rates, trivia, quotes, nationality prediction, ZIP lookup, random users, and an
irresponsible number of jokes and cat facts. Every one is live-verified at build time
and re-verified nightly.

## Make an API callable (the contribution flywheel)

A blueprint is ~20 lines of YAML:

```yaml
id: public-apis-open-meteo        # must match a registry entry id
base_url: https://api.open-meteo.com/v1
auth: none
endpoints:
  - name: forecast
    path: /forecast
    description: Weather forecast for coordinates
    params:
      - {name: latitude,  required: true, type: number, example: 52.52}
      - {name: longitude, required: true, type: number, example: 13.41}
```

Drop it in `src/dopeforge/data/blueprints/`, run `forge check`, open a PR. Every merged
blueprint makes every agent using DopeForge more capable. That's the flywheel.

## Roadmap

```
Phase 1  ✅ Living Registry     4 catalogs → one validated, searchable database
Phase 2  ✅ Agent-native layer  forge mcp · blueprints · forge try · self-testing registry
Phase 3  🚧 Blueprint factory   LLM-assisted blueprint generation from API docs (human-verified)
Phase 4  ⏳ Auth'd blueprints   opt-in local keyring for api-key APIs (keys never touch the agent)
Phase 5  ⏳ Visual composer     chain discovered APIs on a canvas, export Python
```

Endgame: **any API → AI-powered capability in one command** — local-first, your data
stays yours.

## How it works

Each catalog gets a narrow parser adapter (`src/dopeforge/sources/`) that turns its
particular markdown dialect — tables, nested bullets, emoji legends — into one
pydantic-validated schema. Parsers are pure functions tested against real snapshots of
each source (`tests/fixtures/`), extracting 99.6–100% of entries. `forge sync` reports
per-source success/failure explicitly — a source that breaks its format shows up as a
failure, never as silently missing data.

```
Registry resolution: $DOPEFORGE_DATA_DIR → ~/.local/share/dopeforge → packaged snapshot
```

## Development

```bash
git clone https://github.com/DreadpiratePickles/dopeforge && cd dopeforge
python3 -m venv .venv && .venv/bin/pip install -e ".[dev,mcp]"
.venv/bin/pytest -q      # 130 tests, all against real fixture snapshots
.venv/bin/ruff check .
```

Adding a catalog source = one adapter + one fixture + one test. Adding a callable API =
one YAML file. Specs live in [docs/](docs/) and are the binding contracts for each phase.

## License

MIT
