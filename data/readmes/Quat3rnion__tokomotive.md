<p align="center"><img src="docs/images/wordmark.svg" alt="Tokomotive" width="420"></p>

# Tokomotive

Tokomotive is an LLM router and Proxy with optional cost accounting. Clients
send requests to the Proxy instead of to the Provider. The Proxy chooses a
Deployment, forwards the request, and reads the token usage from the response.
In Full Mode, it also records the Cost, the Price and the Profit for each User
and Model.

You configure everything in the web dashboard. You do not need to edit a file.
The terms in this document are defined in [GLOSSARY.md](GLOSSARY.md).

## Features

### Routing

- Maps a client model name to a Route. A Route has one or more Deployments.
  Each Deployment is a Provider and an upstream model name.
- Selects Deployments with the strategy `priority`, `round_robin` or `weighted`.
- Tries Fallbacks and the next Provider Key when a Deployment fails with a
  connection error, a 429 or a 5xx.
- Uses a Circuit Breaker for each Deployment. A failing Deployment rests for a
  cooldown. Then one probe request tests it.
- Limits the number of upstream attempts for each request with `max_attempts`.
- Sends Provider traffic through an optional HTTP, HTTPS or SOCKS5 egress proxy.
  Each Provider can use the global default, connect directly or use its own
  encrypted proxy URL. See [Egress proxies](docs/usage.md#egress-proxies).
- Accepts `provider/model` names when no Route or catalog Model matches. The
  Proxy removes the Provider prefix before the upstream request.
- Resolves model IDs from connected Providers and supports Provider default
  models and priorities. Unknown names get HTTP 404 with permitted suggestions,
  unless the Operator selects a Route. The Routes page can test a name without
  an upstream request. Success headers identify the Route, Provider and Model.
- Rewrites the Model name of the request to the upstream model name of the
  Deployment.
- Offers an encrypted [exact response cache](docs/usage.md#exact-response-cache)
  for JSON and SSE. Each Route sets its lifetime and Virtual Key, Team or global scope.
  Hits have zero Cost and a configurable Price. The cache is off by default.
- Applies [Guardrails](docs/usage.md#guardrails) to prompts and responses.
  Attach rule sets to Routes, Teams or Virtual Keys. Block, redact or log
  regex, keyword, PII and secret matches. Rules also apply in Simple Mode.

### Compatibility

- Provides an [MCP gateway](docs/usage.md#mcp-gateway) with encrypted upstream
  credentials, Virtual Key and Team tool access, and a tool call log.
- Supports OpenAI-compatible APIs (`/v1/chat/completions`, `/v1/responses`,
  `/v1/embeddings`, `/v1/images/generations`, `/v1/images/edits`) and the
  Anthropic API (`/v1/messages`), with and without streaming.
- Counts input tokens at `POST /v1/messages/count_tokens`. Non-Anthropic
  deployments return a marked estimate without an inference charge.
- Routes `POST /v1/rerank` to Cohere or compatible Providers, with search-unit
  or input-token accounting.
- Supports multipart `POST /v1/audio/transcriptions` and `/v1/audio/translations`,
  plus binary streaming at `/v1/audio/speech`, with Model-level audio rates.
- Supports OpenAI `/v1/files` upload, list, get, delete and content download,
  plus `/v1/batches` create, list, get and cancel. Each Virtual Key owns its
  objects. Batch completion has versioned rates and durable Budget Reservations.
- Translates between Chat Completions and Messages, with streaming and tools.
  A Chat Completions client can use an Anthropic Provider. A Messages client
  can use an OpenAI Provider. See [Translation](docs/usage.md#routing-and-translation)
  for the limits.
- Lists the Routes and Models that a Virtual Key can use at `GET /v1/models`
  and `GET /v1/models/{id}`, in OpenAI or Anthropic format.
- Accepts the Virtual Key in `Authorization: Bearer` or in `x-api-key`.
- Supports [Subscription Providers](docs/usage.md#subscription-providers):
  ChatGPT token sharing, Claude OAuth and optional Codex plan usage, with
  explicit access for each Virtual Key.
- Shows account health and subscription quota windows on Providers and Overview,
  with reset times and Prometheus metrics. Quota scheduling prefers accounts
  with more capacity, preserves session pins, and skips exhausted or invalid accounts.

### Accounting

- Records seven Token Classes: input, output, cache read, cache write
  (5 minutes), cache write (1 hour), image input and image output.
- Uses a Cost Card and a Price Card for each Model. A Price Card is a Markup or
  explicit rates. A Team can override the Price Card of a Model.
- Supports Context Tiers, for example higher rates above 200,000 input tokens.
- Keeps every change to a card as a Card Version. A Ledger Entry does not change
  when you change a card.
- Records Models without cards as Unpriced Entries. You can price them later.
- Applies lifetime, daily, weekly and monthly UTC Budgets to Users, Teams and
  Virtual Keys. Every Budget must cover the worst-case Price (the Reservation).
- Sends Budget threshold and models.dev price alerts to encrypted webhook
  URLs in generic JSON, Discord or Slack format. Delivery runs in the background.
- Supports optional Virtual Key expiry with HTTP 401 after the expiry time.
- Applies RPM and TPM Rate Limits to each Virtual Key and each User. A request
  over a limit gets HTTP 429 and a `Retry-After` header.

### Operations

- Shows ordered attempt timelines and request-log filters in the Ledger.
- Exports request and attempt spans with GenAI attributes through OTLP/HTTP
  JSON. Export is off by default and uses a bounded background queue.
- Captures bodies only when a Route or Virtual Key enables capture. Captures
  are redacted, size-capped, encrypted and retained for 7 days by default.
  Only Admins can read them. See [Request diagnostics](docs/usage.md#request-diagnostics).

- Supports Owner, Admin and read-only Viewer dashboard accounts with Argon2
  passwords. Settings includes account management and own-password changes.
  An upgrade keeps the old password on an Owner named `admin`; an empty login
  username still means `admin`.
- Records dashboard changes in a filterable, paginated audit log for Owners
  and Admins. Public before/after fields exclude secrets and URLs. Retention
  defaults to 365 days. See [Dashboard accounts](docs/usage.md#dashboard-accounts-and-audit-log).
- Stores Providers, Provider Keys, Routes and settings in the database. The
  Operator changes them on the **Providers**, **Routes** and **Settings** pages.
  Changes apply without a restart.
- Encrypts Provider Keys with AES-256-GCM. The Master Key comes from
  `TOKOMOTIVE_SECRET_KEY` or from a generated `secret.key` file.
- Lets a Provider Key refer to an environment variable with `env:NAME`.
- Shows requests, tokens, latency, time to first token, Cost, Price and Profit
  per Model, User and Team in the dashboard.
- Exports Prometheus metrics at `/metrics`, optionally with a token.
- Offers Simple Mode for routing and token metrics without prices or usage
  limits.

### Simple mode

Select **Simple** on `/setup` or in **Settings**. The change applies without a
restart. Virtual Keys, model allowlists, routing and token metrics stay active.
You do not need cards or limits. The dashboard hides financial data and
controls. The default is **Full**. See [usage.md](docs/usage.md#simple-mode).

## Screenshots

The screenshots show demo data from a local test server. The keys are not real.
The dashboard has a dark and a light theme. The two large images show the
theme of your GitHub appearance setting.
The current images do not show the new exact-cache controls, hit flag or hit rate.
The capture manifest records these changes for the next image refresh.

<picture>
  <source media="(prefers-color-scheme: light)" srcset="docs/images/overview-light.png">
  <img alt="The Overview page in Full Mode. It shows the Proxy base URL, the totals for 24 hours, three charts and the By Model table." src="docs/images/overview.png">
</picture>

<picture>
  <source media="(prefers-color-scheme: light)" srcset="docs/images/routes-light.png">
  <img alt="The Routes page. The Route &quot;smart&quot; uses the weighted strategy with three Deployments on two Providers and two Fallbacks." src="docs/images/routes.png">
</picture>

| Page | What it shows |
| ---- | ------------- |
| [Ledger](docs/images/ledger.png) | The newest Ledger Entries with the filters. Each row shows the User, the Model and Provider, the status, the flags, the tokens, the amounts and the latency. |
| [Add a Provider](docs/images/add-provider.png) | The searchable Provider picker. The search "kimi" finds verified presets, the Kimi Code sign-in and entries from models.dev. |
| [Add a Provider form](docs/images/add-provider-form.png) | The guided form for DeepSeek. It shows only the fields that this Provider needs and a summary of the result. |
| [Providers](docs/images/providers.png) | Two API-key Providers and four Subscription Providers. The page shows only the last 4 characters of each key, or the name of its environment variable. |
| [Sign-in](docs/images/signin.png) | The sign-in panel of a Codex Provider. Paste the redirect URL here when device sign-in is not available. |
| [Models](docs/images/models.png) | The Models with their Cost Card rates, Price Cards, Team overrides and the Default Markup. |
| [Model page](docs/images/model.png) | The cards of one Model, a Team override and the Card history. |
| [Users](docs/images/users.png) | The name search, the Users with their Teams, Budgets, Rate Limits and spend, and the pager. |
| [Keys](docs/images/keys.png) | The form to add a Virtual Key with Provider Access and Rate Limits, the active keys and the pager. |
| [Usage](docs/images/usage.png) | The "Show all" view of the Overview: usage by User, sorted by requests, one page at a time. |
| [Overview in Simple Mode](docs/images/overview-simple.png) | The Overview without money data: requests, tokens, latency, errors and attempts. |
| [Teams](docs/images/teams.png) | Teams with their Budgets, spend and member counts. |
| [Settings](docs/images/settings.png) | The operating mode, routing settings, metrics and alert controls. |
| [Audit log](docs/images/audit.png) | The audit log: who changed what and when, with filters and the pager. |
| [Guardrails](docs/images/guardrails.png) | A rule set in the rule editor with a detector, a regex and a keyword rule, its Route attachment and a test box for pasted text. |
| [MCP servers](docs/images/mcp-servers.png) | MCP servers with masked credentials, a connection test and cached tool descriptions. |
| [MCP tool calls](docs/images/mcp-log.png) | The MCP tool call log with key, User, server, tool, status, latency and error class. Arguments and results are not stored. |

## Quick start

Both methods are UI-first. You do not edit a file.

### With Docker Compose

1. Start the Proxy from the root directory of the repository:

   ```sh
   docker compose up -d
   ```

2. Open `http://127.0.0.1:8787/admin`. The page redirects to `/setup`. Enter an
   admin password of at least 8 characters, select **Full** or **Simple**, and
   select **Set password**. Then log in.
3. Go to the next section, "Configure in the dashboard".

Compose keeps the database and the generated `secret.key` file in the volume
`tokomotive-data`. Back up both. See [INSTALL.md](INSTALL.md) for the Master Key
options.

### With Cargo

1. Start the Proxy. The Rust version must be 1.88 or newer:

   ```sh
   cargo run --release
   ```

2. Open `http://127.0.0.1:8787/admin` and complete Setup, as in the Compose
   steps above.
3. Go to the next section, "Configure in the dashboard".

The Proxy creates `tokomotive.db` and `secret.key` in the working directory.
Back up both.

### Configure in the dashboard

1. On **Providers**, add a Provider with its name, kind, base URL and key. Use
   `env:NAME` to refer to an environment variable instead of a key. Select
   **Test** to check the connection.
2. Optional: on **Routes**, add a Route with its Deployments and Fallbacks.
3. In Full Mode, add Models and cards on **Models**. Check the rates against the
   Provider price list. In Simple Mode, skip this step and use `provider/model`
   names or Routes.
4. Add a User on **Users**. Then create a Virtual Key on **Keys**. Copy the key.
   You cannot see it again.
5. Send a request with the Virtual Key:

   ```sh
   curl http://127.0.0.1:8787/v1/chat/completions \
     -H "Authorization: Bearer sk-toko-..." -H "content-type: application/json" \
     -d '{"model":"openai/gpt-4o","messages":[{"role":"user","content":"Hello"}]}'
   ```

   The request appears on the **Ledger** page. The name `openai/gpt-4o` works
   when a Provider named `openai` exists and no Model has that full name.

The default listen address is `127.0.0.1:8787`. Use `--listen` and `--database`
(or `TOKOMOTIVE_LISTEN` and `TOKOMOTIVE_DATABASE`) to change the listen
address and the database. These two options are the only settings outside the
dashboard. An optional `--config PATH` file seeds the database once. See
[docs/configuration.md](docs/configuration.md).

## Documentation

- [INSTALL.md](INSTALL.md): install, configure and verify the Proxy. It is
  written for AI coding agents.
- [docs/usage.md](docs/usage.md): the Operator guide. It covers clients, the
  dashboard pages, routing, Translation, how amounts are calculated, Budgets,
  Rate Limits, metrics and error responses.
- [docs/configuration.md](docs/configuration.md): every setting, every
  environment variable, the Master Key, seeding and Docker.
- [GLOSSARY.md](GLOSSARY.md): the terms of this project.
- [docs/adr/](docs/adr/): the architecture decisions.

## Limits

- File uploads need `x-tokomotive-provider` and keep one Provider Key.
  Batch files support bounded, text-only requests with explicit output limits.
  See [files and batches](docs/usage.md#files-and-batches) for limits and recovery.
- The Proxy reads the Model name from JSON or multipart audio. Other multipart
  requests are Unpriced unless the response names the Model.
- Translation rejects `n` greater than 1 and JSON-schema response formats. It
  drops thinking blocks, signatures and cache hints. It translates choice 0
  only. See [docs/usage.md](docs/usage.md#routing-and-translation).
- The Reservation uses an estimate of the input tokens. A request can cost more
  than its Reservation, for example when it refers to files or cached content
  that is not in the request body. Thus, a Budget can be exceeded by a small
  amount.
- Synchronous Reservations, Rate Limits, Circuit Breaker state and Key Pool
  rotation are in memory. They reset when the process restarts. Batch
  Reservations are stored in the database. Run one Proxy process for each database.
- On the image endpoints, the Proxy treats cached tokens as text tokens. Cached
  image input tokens are recorded as image input, not as cache read.
- `/metrics` has no authentication when no metrics token is set.

## Development

```sh
cargo test
cargo clippy --all-targets
```

The code needs Rust 1.88 or newer (edition 2024).

## License

Licensed under either of [Apache License, Version 2.0](LICENSE-APACHE) or
[MIT license](LICENSE-MIT) at your option.

Unless you explicitly state otherwise, any contribution that you intentionally
submit for inclusion in this work, as defined in the Apache-2.0 license, is
dual licensed as above, without any additional terms or conditions.
