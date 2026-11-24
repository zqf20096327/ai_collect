# Sans

[![CI](https://github.com/loicsapone/sans/actions/workflows/ci.yaml/badge.svg)](https://github.com/loicsapone/sans/actions/workflows/ci.yaml)

Paste the URL of a recipe: Sans extracts it, shows which of the 14 EU regulatory allergens it contains, and can propose an adapted version that avoids the allergens you switched off.

Built for the [Symfony AI & MCP Hackathon](https://symfony.com/hackathon) (RAG, MCP, agents). Every allergen verdict comes from a deterministic lookup in PHP; the language model only extracts and normalises ingredients and proposes substitutions.

![Easy pancakes adapted without milk: the milk is swapped for a rice drink and the step that uses it is rewritten](docs/screenshot.png)

## Setup

You need a [Mistral API key](https://console.mistral.ai) and Docker with Compose. Start with the key, the install needs it to build the index:

```bash
git clone https://github.com/loicsapone/sans.git && cd sans
echo "MISTRAL_API_KEY=your-key" > .env.local
```

Then pick one of the two ways to run the app. Both build the index of the ingredient reference with Mistral embeddings, which takes about a minute.

### With the Symfony CLI

Needs PHP 8.5, Composer and the [Symfony CLI](https://symfony.com/download). PHP runs on your machine and only [Meilisearch](https://www.meilisearch.com), which holds the index, runs in Docker: the CLI finds its port by itself and serves the app on a free port.

```bash
composer install
docker compose up -d meilisearch
symfony console doctrine:schema:update --force
symfony console ai:store:setup ingredients --no-debug
symfony console ai:store:index ingredients --no-debug
symfony server:start -d
```

The last command prints the address of the app (http://127.0.0.1:8000 when the port is free).

### With Docker only

Nothing to install but Docker: the app runs in a FrankenPHP container.

```bash
make build up
make install
```

The app is served on https://localhost, with a local certificate your browser asks you to accept. When ports 80 and 443 are taken, choose others (`HTTP_PORT=8080 HTTPS_PORT=8443 make up`) and open https://localhost:8443.

### Try it

Paste the link of a recipe, in French or in English, for example:

- https://www.bbcgoodfood.com/recipes/easy-pancakes
- https://www.marmiton.org/recettes/recette_pate-a-crepes_12372.aspx
- https://www.marmiton.org/recettes/recette_gratin-dauphinois-tres-facile_58956.aspx

Then tap the mark of an allergen to cook without it. `/?url=<recipe link>` shares an analysis: an address that was already analysed is shown at once (analyses are kept for a week).

### Try it from an MCP client

Sans answers the same questions as the page. With Claude Code, once the app runs (`http://127.0.0.1:8000` with the Symfony CLI, `https://localhost` with Docker):

```bash
claude mcp add --transport http sans http://127.0.0.1:8000/mcp
```

Then, in order:

1. `Which allergens are in https://www.bbcgoodfood.com/recipes/easy-pancakes?`
2. `Adapt it to cook without milk and eggs.`
3. `Is a stock cube safe if I avoid celery?`

## How it fits together

```
recipe URL ─► fetch ─► extract (schema.org, or the model) ─► normalise ingredient lines
                                                                  │
                          Meilisearch (hybrid: words + meaning) ◄─┤ matcher agent picks among the results
                                                                  ▼
 allergen verdicts, computed in PHP from the reference ◄── ingredients matched to the reference
        │
        ├─ tap an allergen ─► adapter agent ─► check_ingredients (the matcher, as a tool) ─► swaps checked by PHP
        └─ "may contain" ───► labels agent ─► Open Food Facts MCP server ─► product counts read in PHP

page (Live components)  ·  `bin/console app:analyze`  ·  Sans as an MCP server (`/mcp`, STDIO)
```

Stage by stage: [docs/how-it-works.md](docs/how-it-works.md).

## What Symfony AI unlocked

Sans is five agents, one vector store and one MCP connection, and almost all of it is configuration (`config/packages/ai.yaml`). What made the difference:

- **Typed answers.** Every agent answers with a PHP class given as `response_format` (`IngredientLines`, `MatchChoices`, `AdaptationAnswer`...). A backed enum in that class (`Role`) becomes an `enum` of the JSON schema and comes back as the enum case. There is no JSON to parse or to validate by hand anywhere in the project.
- **A model that can only pick what the search returned.** The matcher's tool implements `HasSourcesInterface`: the documents it found travel with the answer, and PHP only accepts an id that is among them. The allergens are read from those documents, never from the model.
- **Hybrid search without writing a query.** The Store component gives a `HybridQuery` (words and meaning) over Meilisearch, and the index is built by its own commands from a CSV file, with a loader, a transformer and a vectorizer declared in YAML.
- **An agent as the tool of another.** The adapter checks its own proposals with a tool that runs the matcher, so a swap is verified against the reference before the answer is even written.
- **MCP in both directions.** Sans is a server too: three tools, one class, a few lines of YAML (see below).
- **A remote MCP server as a tool belt, and as a plain client.** One line (`mcp_server: food.openfoodfacts`) gives an agent the tools of the Open Food Facts server; the same connection is injected in PHP to call a tool directly, which is how the product counts stay out of the model's hands.

The pattern that runs through all of them: the model proposes, PHP decides. Symfony AI made that cheap enough to apply everywhere.

## Going further

The stages in detail (reference data, matching, analysis, adaptation, labels): [docs/how-it-works.md](docs/how-it-works.md).

## Sans as an MCP server

Sans is also an MCP server, so that an assistant can ask it the same questions as the page. It is declared in `config/packages/mcp.yaml` (`servers.sans`) and its three tools are the methods of one class, `App\Mcp\RecipeTools`, which calls the services the page uses:

| Tool | What it does |
|---|---|
| `analyze_recipe` | Reads the recipe of a web page: its ingredient lines with the allergens each one carries, and a verdict for each of the 14 allergens |
| `adapt_recipe` | Gives the swaps and the rewritten steps to cook that recipe without the given allergens |
| `check_ingredients` | Looks up ingredient names in the reference and returns their allergens |

Analyses and adaptations are shared with the page: a recipe analysed on one side is shown at once on the other.

Over HTTP, the endpoint is `/mcp` on the address of the app (http://127.0.0.1:8000/mcp with the Symfony CLI). Over STDIO, the server is a command:

```json
{
    "mcpServers": {
        "sans": {
            "command": "sh",
            "args": ["-c", "cd /path/to/sans && exec symfony console mcp:server"]
        }
    }
}
```

With Docker only, replace the command with `docker compose exec -T php bin/console mcp:server`. `bin/console debug:mcp` lists the tools.

The endpoint has no authentication and each call costs model requests: it only answers requests made to `localhost` (the DNS rebinding protection of the SDK, `http.allowed_hosts`), and it must stay that way unless it is put behind an authentication.

## Symfony AI: what got in the way

[docs/symfony-ai-limits.md](docs/symfony-ai-limits.md) lists the limits met with the Store, Agent and Platform components, with what Sans does about each and what a fix could look like.

## Quality

```bash
make static   # PHP-CS-Fixer, Twig-CS-Fixer, PHPStan
make test     # PHPUnit
make ci       # both
```

## License

[MIT](LICENSE).
