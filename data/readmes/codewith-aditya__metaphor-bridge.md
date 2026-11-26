# metaphor-bridge

OpenAI-compatible local API for [Metaphor](https://withmetaphor.com) models — no macOS or
Windows app required. Mints your own account's WorkOS token with the same OAuth flow the
desktop app uses, keeps it fresh, and proxies `/v1/*` over HTTP/2 on `127.0.0.1`.

![metaphor-bridge demo](docs/demo.gif)

*Terminal capture of the real binary: build → token status → serve → `/v1/models` →
streaming `/v1/chat/completions` (first token ~1.1 s). The clip points the bridge at a live
vLLM upstream with `METAPHOR_UPSTREAM` so it does not touch a Metaphor account quota; the
proxy path, streaming and queue are the same ones used against
`https://llms.withmetaphor.com` by default.*

## Quick start

```bash
go build -o metaphor-go .                       # 1. build (Go 1.22+, no deps beyond x/net)
./metaphor-go auth start                        # 2. open the printed URL, approve on GitHub
./metaphor-go auth finish "<metaphor://…code>"  #    paste the redirect URL (or just the code)
./metaphor-go serve                             # 3. bridge on http://127.0.0.1:8190
```

First request:

```bash
curl -sS http://127.0.0.1:8190/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"minimax-m3","messages":[{"role":"user","content":"hi"}]}'
```

Any OpenAI SDK works: `base_url = http://127.0.0.1:8190/v1`, `api_key` = anything (it is
local). Already have a GitHub browser session? Skip the two auth steps:

```bash
./metaphor-go auth gh "user_session=…; _gh_sess=…"   # walks GitHub → WorkOS → code for you
```

```
your client ──HTTP/1.1 or h2c──> metaphor-bridge :8190 ──HTTP/2──> llms.withmetaphor.com
```

## Features

- `GET /v1/models`, `POST /v1/chat/completions`, `POST /v1/messages`, `POST /v1/responses`
- SSE streaming passed through byte-for-byte, flushed per chunk
- WorkOS PKCE login (`auth start` / `auth finish`) and refresh-token rotation
- Automatic access-token refresh, driven by the JWT `exp` claim
- Request queue — the upstream allows only ~1–2 in-flight requests
- `429`/`503` retry with `Retry-After`
- Egress proxy support — `http://`, `https://` (self-signed allowed) and `socks5://`, applied to the
  gateway *and* the auth hops (useful when GitHub rate-limits your IP)
- HTTP/2 upstream, h2c downstream (`curl --http2-prior-knowledge http://127.0.0.1:8190/v1/models`)
- `/healthz` for token expiry + concurrency, `/debug/ip` to see the egress IP in use

Measured throughput and rate-limit behaviour: **[BENCHMARK.md](BENCHMARK.md)**
(reproduce with `python3 bench/bench.py`).

Working on the code (or driving it with a coding agent)? Read **[AGENTS.md](AGENTS.md)**
— architecture, invariants, verification commands and the failure playbook.

## Benchmarks

Measured 2026-11-18 through this bridge (single-stream, `max_tokens=512`,
`temperature=0`, median of 2 runs, 4 vCPU VPS with US egress). Full methodology and
caveats: [BENCHMARK.md](BENCHMARK.md).

| Model | TPS | Output tokens | Wall | Stream TTFT |
| --- | ---: | ---: | ---: | ---: |
| `glm-5.3` | 135.6 | 512¹ | 3.88 s | 1.28 s |
| `kimi-k3` | 99.2 | 512 | 5.65 s | 0.76 s |
| `qwen3-coder-next` | 88.6 | 374 | 5.25 s | 0.79 s |
| `deepseek-v4-1-flash` | 87.2 | 512¹ | 8.14 s | 0.28 s |
| `kimi-k3-1-pro` | 80.0 | 512 | 6.40 s | 0.81 s |
| `deepseek-v4-pro` | 67.1 | 242 | 4.47 s | 1.13 s |
| `minimax-m3` | 32.7 | 210 | 6.99 s | 1.05 s |

¹ reasoning only — these two spent the whole budget on thinking and returned empty
`content`; give them ≥1–2k `max_tokens` for visible output.

Rate limiter: ~25–30 sequential requests go through, then
`429 Too many concurrent Darwin requests` with `retry-after: 2` until the window
drains — the reason the bridge queues requests (`METAPHOR_CONCURRENCY`, default 1).

## Security and credentials

Short version: the bridge never sees your password, stores one bearer token on your disk,
and talks to exactly two hosts.

**How login works.** `auth start` opens WorkOS's authorize URL for the public client
`client_01KAHJW6K5B09TYCG4P597H63N` with a PKCE challenge; the redirect target is Metaphor's
own deep link (`metaphor://auth/callback`). After you approve on GitHub, the browser lands on
a `metaphor://…?code=…` URL that the OS cannot open — you paste it back, and the binary
exchanges the code with its local `code_verifier`. No client secret exists to leak, and the
code is single-use and useless without the verifier.

**What is stored, where.**

| File | Contents | Permissions |
| --- | --- | --- |
| `$METAPHOR_DIR/tokens.json` | WorkOS access JWT + refresh token | `0600` |
| `$METAPHOR_DIR/pkce.json` | the in-flight PKCE verifier/state | `0600` |
| `$METAPHOR_DIR/login_url.txt` | the last authorize URL (no secret) | `0644` |

`METAPHOR_DIR` defaults to `/root/metaphor` on Linux, `%AppData%\metaphor-bridge` on
Windows, `~/.metaphor` on macOS — always outside the repository. The access token is a ~24 h
JWT; `auth refresh` (and the running bridge) exchanges the refresh token when the `exp`
claim is close. Credentials are only re-read when the file's mtime changes, so minting a
token in another shell does not disturb a running bridge.

**Network.** The process contacts `llms.withmetaphor.com` (inference) and, during login or
refresh only, `api.workos.com` and `github.com`. There is no telemetry, no analytics and no
call home. If you set `-proxy` / `METAPHOR_PROXY`, *every* one of those hops goes through
your proxy, including the auth chain.

**Revoking access.** Delete `tokens.json`, stop the bridge, and sign out of Metaphor (or
sign out of all GitHub sessions used for the login). The old refresh token is invalidated
server-side when the session is revoked.

**Relationship to Metaphor.** This is an independent client for your own account, not
affiliated with or endorsed by Metaphor. It reproduces the OAuth flow their public desktop
build uses; if they change it, the flow breaks (see [AGENTS.md](AGENTS.md) for the failure
playbook). Using it to resell access would violate their terms — keep it personal.

## Build

```bash
go build -o metaphor-go .
```

## Authenticate

```bash
./metaphor-go auth start
# open the printed URL, sign in with GitHub, approve
# the browser ends on metaphor://auth/callback?code=... (it will look blank — that's expected)
./metaphor-go auth finish "<paste the full metaphor:// URL or just the code>"
```

Tokens are written to `$METAPHOR_DIR/tokens.json` (default `/root/metaphor`, mode 0600).

Check state at any time:

```bash
./metaphor-go auth show
./metaphor-go auth refresh      # force a refresh-token exchange
```

### Non-interactive login (CI / headless)

If you already have a GitHub browser session, pass its `user_session` and `_gh_sess`
cookies and the whole GitHub → WorkOS → code chain is walked for you:

```bash
./metaphor-go auth gh "user_session=...; _gh_sess=..."
```

## Run

```bash
./metaphor-go serve                     # 127.0.0.1:8190
METAPHOR_CONCURRENCY=2 ./metaphor-go serve

# egress through a proxy (HTTP CONNECT, HTTPS with a self-signed cert, or SOCKS5)
METAPHOR_PROXY='http://user:pass@host:8080' ./metaphor-go serve
METAPHOR_PROXY='https://user:pass@gw.example.com:443' METAPHOR_PROXY_INSECURE=1 ./metaphor-go serve
METAPHOR_PROXY='socks5://127.0.0.1:1080' ./metaphor-go serve
```

The proxy applies to **every** outbound hop: the model gateway, token refresh, and the
`auth` subcommands (handy when GitHub rate-limits your IP — `auth gh` then runs through
the proxy too). `curl -sS localhost:8190/debug/ip` shows which egress you are on.

Systemd unit: `systemd/metaphor-bridge-go.service` (edit `ExecStart`/`METAPHOR_DIR`).

```bash
curl http://127.0.0.1:8190/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"minimax-m3","messages":[{"role":"user","content":"hi"}]}'
```

Any OpenAI SDK works: `base_url = http://127.0.0.1:8190/v1`, `api_key` = anything.

### Windows

Grab `metaphor-go_1.1.1_windows_amd64.exe` (or `windows_arm64`) from the release and run it
in PowerShell — no installer, single static binary:

```powershell
.\metaphor-go_1.1.1_windows_amd64.exe auth start
.\metaphor-go_1.1.1_windows_amd64.exe auth finish "metaphor://auth/callback?code=..."
.\metaphor-go_1.1.1_windows_amd64.exe serve
```

Tokens land in `%AppData%\metaphor-bridge\tokens.json` (override with `METAPHOR_DIR`).
Defender/SmartScreen may warn because the binary is unsigned — "More info → Run anyway",
or build it yourself with `go build`. To keep it running, either leave a PowerShell window
open or register it as a scheduled task (`schtasks /create /tn metaphor-bridge /tr "<path>\metaphor-go.exe serve" /sc onlogon`).

## Environment

| Var | Default | Meaning |
| --- | --- | --- |
| `METAPHOR_PORT` | `8190` | listen port (127.0.0.1 only) |
| `METAPHOR_UPSTREAM` | `https://llms.withmetaphor.com` | override the upstream base URL (local vLLM, mirror, tests) |
| `METAPHOR_CONCURRENCY` | `1` | max in-flight upstream requests |
| `METAPHOR_PROXY` | *(empty)* | egress proxy: `http://`, `https://`, `socks5://` |
| `METAPHOR_PROXY_INSECURE` | `false` | skip TLS verification of the proxy itself |
| `METAPHOR_DIR` | Linux `/root/metaphor`, Windows `%AppData%\metaphor-bridge`, macOS `~/.metaphor` | where `tokens.json` / `pkce.json` live |

## Things that bite

- **Chrome swallows `metaphor://`** — the redirect ends on a blank page with no URL in the
  address bar. Use Firefox (it renders the attempted URL), or Chrome DevTools →
  Network with *Preserve log* and read the `metaphor://auth/callback?code=...` request.
- **`email_verification_required`** — the WorkOS user has never verified its email.
  Sign in once at <https://withmetaphor.com/signin> and complete the code, then retry.
- **GitHub `429` on `/login/oauth/authorize`** — per-IP rate limit; wait, or run that
  hop through another egress.
- **`Too many concurrent Darwin requests`** — upstream concurrency limit, keep
  `METAPHOR_CONCURRENCY` at 1–2 and let the queue do its job.
- The web dashboard has no API-key page; the token is the only credential.

## Why this exists

The gateway is useful from Linux, where the official app is unavailable. The token is
minted for **your own** account with the same OAuth flow the app uses.

## Disclaimer

Not affiliated with Metaphor. Use it with your own account and within their terms —
this is a client, not a way around them. Publishing or reselling access through the
free tier is on you, and so is anything that happens to your account.

## License

MIT — see [LICENSE](LICENSE). Contributions welcome, read [CONTRIBUTING.md](CONTRIBUTING.md) first.
