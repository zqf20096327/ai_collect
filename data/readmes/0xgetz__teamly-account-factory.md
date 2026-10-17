<p align="center"><a href="README.md">
  <img src="docs/assets/logo.svg" alt="Teamly Account Factory" width="150">
</a></p>

<p align="center"><img src="docs/assets/banner.svg" alt="Teamly Account Factory banner"></p>

<p align="center">
  <a href="https://go.dev/"><img src="https://img.shields.io/badge/Go-1.21%2B-00ADD8?style=for-the-badge&logo=go&logoColor=white" alt="Go"></a>
  <img src="https://img.shields.io/badge/dependencies-zero-22e6a5?style=for-the-badge" alt="Zero dependencies">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-22e6a5?style=for-the-badge" alt="MIT License"></a>
  <img src="https://img.shields.io/badge/browser-not%20required-7c5cff?style=for-the-badge" alt="No browser">
  <img src="https://img.shields.io/badge/9router-ready-12b5ff?style=for-the-badge" alt="9Router ready">
  <img src="https://img.shields.io/badge/CI-none-6b7280?style=for-the-badge" alt="No CI">
</p>

# Teamly Account Factory

> Bulk-provision Teamly accounts, publish an agent endpoint for each, mint an API key, and wire every key into 9Router — all over plain HTTP.

<p><strong>English</strong> · <a href="readme/README.id.md">Indonesia</a> · <a href="readme/README.zh.md">简体中文</a> · <a href="readme/README.ja.md">日本語</a> · <a href="readme/README.ko.md">한국어</a></p>

---

`teamly-account-factory` is a single, dependency-free Go program that takes a
count and returns that many working `tmly_sk_live_…` keys, each bound to its own
agent and already registered in your local 9Router. It talks to five systems in
one reproducible pipeline:

1. **mail.tm** — a fresh disposable inbox per account.
2. **Teamly userCenter** — account creation and the emailed verification code.
3. **Supabase** — the swarm session that Teamily issues after login.
4. **Teamly swarm** — agent creation, endpoint publishing and key minting.
5. **9Router** — every key becomes its own OpenAI-compatible provider node.

No browser, no Playwright, no headless Chromium. Every call is reverse-engineered
from Teamily's own web client and replayed as HTTP.

> This tool is intended for legitimate automation, internal testing and research
> on accounts you own. You are responsible for complying with Teamly's terms of
> service and any applicable law.

---

## Why plain HTTP?

The Teamly web app is a client-rendered SPA, but its signup, verification and
agent flows are ordinary JSON calls. Two authorization schemes are in play:

| Layer | Endpoint group | Authorization header |
|-------|----------------|----------------------|
| Account | `open.teamly.ai/userCenter/...` | raw JWT — **no** `Bearer` |
| Agents / keys | `teamly.ai/swarm/api/...` | `Bearer <supabase access_token>` |
| Model calls | `teamly.ai/v1/...` | `Bearer tmly_sk_live_…` |

The only non-obvious step is the **swarm credential exchange**: `getSwarmCredential`
returns a derived Supabase email/password pair, which is then exchanged for a
Supabase access token that authorizes the whole swarm API. Once that is clear,
the pipeline is fully scriptable.

## Features

- **Disposable inboxes** — one mail.tm address per account, created with retry
  and backoff when mail.tm throttles (HTTP 429).
- **Automatic verification** — polls the inbox and extracts the 6-digit code
  (the CSS-safe parser skips the `#111827` colour literal in the email body).
- **Full onboarding** — register → verify → swarm session → agent → endpoint →
  publish → key, end to end.
- **Random identities** — inbox local-parts, passwords and slugs are unique per
  run and per account.
- **Router wiring built in** — each key becomes its own 9Router provider node
  with a unique prefix, so `tm74211/tm74211` always hits account 1.
- **Self-checking** — every account is probed with a live `PONG` chat through the
  router before it is reported as OK.
- **Concurrency** — bounded worker pool (`-concurrency`), default 2.
- **Structured JSON output** — rewritten at the end of the run; failures are
  recorded with their error.
- **Zero dependencies** — only the Go standard library.

## Architecture

```
cmd/teamly/            # CLI entry point (flags, worker pool, report writer)
internal/
├── config/            # endpoints, flags, env, defaults
├── mailbox/           # mail.tm inbox + verification-code reader
├── teamly/            # account, swarm session, agent, endpoint, key
└── router/            # 9Router provider-node + connection client
docs/assets/           # logo.svg, banner.svg
examples/              # run.sh, curl-usage.sh
```

See [STRUCTURE.md](STRUCTURE.md) for full component, sequence and routing
diagrams (Mermaid, rendered by GitHub).

## Requirements

- **Go 1.21+** (only the standard library — no `go get` needed)
- Network access to `api.mail.tm`, `open.teamly.ai`, `teamly.ai` and Supabase
- A reachable **9Router** instance (default `http://127.0.0.1:20128`)

## Installation

```bash
git clone https://github.com/0xgetz/teamly-account-factory.git
cd teamly-account-factory
go build -o teamly ./cmd/teamly
```

## Usage

```bash
# 5 accounts, 2 workers, written to accounts.json
./teamly -n 5 -concurrency 2 -out accounts.json
```

### Flags

| Flag | Default | Description |
|------|---------|-------------|
| `-n` | `5` | number of accounts to provision |
| `-concurrency` | `2` | parallel workers (1–5) |
| `-mail-domain` | `maxxspace.com` | mail.tm domain for inboxes |
| `-router-url` | `http://127.0.0.1:20128` | 9Router base URL |
| `-router-password` | `Router9Pass!` | 9Router dashboard password |
| `-router-api-key` | `sk-…` | 9Router client API key |
| `-router-prefix` | `tm` | base prefix for per-account nodes |
| `-agent-name` | `teamly-agent` | name for each provisioned agent |
| `-out` | `accounts.json` | JSON result file path |
| `-timeout` | `45s` | per-request HTTP timeout |
| `-keep-failed` | `true` | include failed accounts in the output |

Environment variables (`MAIL_DOMAIN`, `ROUTER_URL`, `ROUTER_PASSWORD`,
`ROUTER_API_KEY`, `ROUTER_PREFIX`) are honoured; flags override them. See
[`.env.example`](.env.example).

## Output

`accounts.json`:

```json
{
  "generated_at": "2026-10-10T11:12:00Z",
  "router": "http://127.0.0.1:20128",
  "router_api_key": "sk-13295da0418e0160-im4r6k-4398b09c",
  "total": 5,
  "succeeded": 5,
  "failed": 0,
  "accounts": [
    {
      "index": 1,
      "email": "tmh0u8moinosq@maxxspace.com",
      "password": "Tmly!30652419x",
      "account_id": 164438,
      "agent_id": "6542e0c2-4b11-487f-b702-be798e3f0eb8",
      "endpoint_id": "84a0ec40-301c-40b5-808c-dc71a1306128",
      "slug": "tm306524",
      "api_key": "tmly_sk_live_pd-UOlq-QiSCZw6L5-liQmB2dv7DBYKkF1_Cq4XC2bk",
      "node_id": "openai-compatible-chat-4d4a7ecc-…",
      "connection_id": "82ecf875-b86a-4919-8c30-35b4c9776eae",
      "model": "tm306524/tm306524",
      "router_probe": "PONG"
    }
  ]
}
```

The API key (`api_key`) is only ever returned **once** by Teamly, at creation
time — this JSON is the only copy. Keep it safe.

## Using a generated key

Through 9Router (recommended — one base URL for the whole pool):

```bash
curl http://127.0.0.1:20128/v1/chat/completions \
  -H "Authorization: Bearer sk-13295da0418e0160-im4r6k-4398b09c" \
  -H "Content-Type: application/json" \
  -d '{"model":"tm306524/tm306524","messages":[{"role":"user","content":"hello"}]}'
```

Directly against Teamly's OpenAI-compatible gateway:

```bash
curl https://teamly.ai/v1/chat/completions \
  -H "Authorization: Bearer tmly_sk_live_…" \
  -H "Content-Type: application/json" \
  -d '{"model":"tm306524","messages":[{"role":"user","content":"hello"}]}'
```

## Programmatic use

The `internal` packages are importable:

```go
import (
    "github.com/0xgetz/teamly-account-factory/internal/mailbox"
    "github.com/0xgetz/teamly-account-factory/internal/teamly"
)

box := mailbox.New(45 * time.Second)
email, _ := box.Create("maxxspace.com")

tc := teamly.New(45 * time.Second)
tc.Register(email, "Tmly!secret9x", box)
tc.AuthorizeSwarm()

agentID, _ := tc.CreateAgent("my-agent")
endpointID, slug, _ := tc.PublishEndpoint(agentID, "my-slug")
key, _ := tc.CreateKey(endpointID, "router")
```

## Notes and limits

- Teamly issues each account's API key exactly once; re-running mints **new**
  accounts, not re-usable keys.
- mail.tm rate-limits inbox creation; with `-concurrency 2` a 5-account run may
  pause up to a couple of minutes on retries.
- Passwords are transmitted as `sha256(plaintext)` hex, matching the web client.

## Development

```bash
go vet ./...
go build ./cmd/teamly
```

## License

Released under the [MIT License](LICENSE).
