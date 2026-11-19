<div align="center">

# freepi-bridge

**An OpenAI-compatible HTTP API for a FreePi account.**<br>
A single Rust binary, no runtime and no extra services.

![version](https://img.shields.io/badge/version-0.2.3-blue)
![msrv](https://img.shields.io/badge/msrv-1.89%2B-orange)
![license](https://img.shields.io/badge/license-GPL--3.0--only-blue)

</div>

Language: English | [Indonesia](README.id.md)

FreePi's API only accepts its own client and needs an ad impression before free
completions work. The bridge handles both and forwards requests to
`api.freepi.ai`, so any OpenAI-compatible app (opencode, pi, omp, 9router, etc) can use your FreePi account.

FreePi is a separate account. Sign-up is a GitHub login, and the bridge spends
that account's quota instead of creating one, so [Token](#token) has to happen
once on some machine.

## Quick start

1. **Install** (see [Install](#install))
2. **Sign in to FreePi once**: `npx free-pi-cli@latest` (needs Node.js 22.15+).
   Sign in with GitHub and quit. The token is saved and reused. No Node.js here?
   Use [Docker](#docker), or run the CLI once on another machine and copy
   `~/.free-pi/agent/credentials.json` over.
3. **Start the bridge**:
   ```sh
   freepi-bridge start --bg
   freepi-bridge doctor     # should report everything OK
   ```
4. **Point your app at it**:
   - Base URL: `http://127.0.0.1:8787/v1`
   - API key: your `BRIDGE_API_KEY` if you set one, otherwise any placeholder
   - Model: any id from `freepi-bridge models`, or from
     [freepi.ai/models](https://freepi.ai/models) which also shows quotas

Test it:

```sh
curl http://127.0.0.1:8787/v1/chat/completions \
  -H 'content-type: application/json' \
  -d '{"model":"particle","messages":[{"role":"user","content":"hi"}]}'
```

> **Windows PowerShell 5.1:** `curl` is an alias for `Invoke-WebRequest`.
> Use `curl.exe`, or:
> ```powershell
> Invoke-RestMethod http://127.0.0.1:8787/v1/chat/completions -Method Post `
>   -ContentType 'application/json' `
>   -Body '{"model":"particle","messages":[{"role":"user","content":"hi"}]}'
> ```

## Install

Linux, macOS, or WSL2:

```sh
curl -fsSL https://raw.githubusercontent.com/ihsan-ramadhan/freepi-bridge/main/install.sh | sh
```

Windows 10 or newer, in PowerShell 5.1 or later:

```powershell
irm https://raw.githubusercontent.com/ihsan-ramadhan/freepi-bridge/main/install.ps1 | iex
```

From source, with a Rust toolchain:

```sh
cargo install --path .
```

Container: see [Docker](#docker).

| Installed with | Lands in |
| --- | --- |
| `install.sh` | `~/.local/bin` |
| `install.ps1` | `%LOCALAPPDATA%\Programs\freepi-bridge`, added to your PATH |
| `cargo install --path .` | `~/.cargo/bin` |

Supported: Linux x86_64/aarch64, macOS 11+ (Intel and Apple Silicon), Windows
x86_64 (arm64 runs the x64 build under emulation). No Rust toolchain needed for
the installers. Restart your terminal after installing so the new PATH applies.

Installer options: `--version v0.2.1` (pin a release), `--system` (install to
`/usr/local/bin`), `PREFIX=/opt/x`, `--from-source`. PowerShell: `-Version`,
`-Prefix`, `-FromSource`, `-NoPath`. Piping into `iex` leaves no room for
arguments, so set `$env:FREEPI_BRIDGE_VERSION`, `$env:FREEPI_BRIDGE_PREFIX` and
friends instead.

## Token

The bridge spends your FreePi account, so it needs your JWT, looked up in this order:

1. `FREEPI_TOKEN` environment variable
2. `~/.free-pi/agent/credentials.json` (written by `npx free-pi-cli@latest`)
3. a `Bearer` JWT sent by the client (only when `BRIDGE_API_KEY` is unset)

On a machine without Node or a browser (container, CI, server), sign in on
another machine and pass the token: `FREEPI_TOKEN=eyJ... freepi-bridge start --bg`.
If the token expires, run `npx free-pi-cli@latest` again.

## Ads

Free completions return `403 ads_required` until the account reports an ad
impression. By default the bridge reports one automatically every 10 minutes
(`FREEPI_AUTO_AD=on`), so it works on headless hosts. This claims ads nobody saw
and can get the account reviewed.

If you can keep a browser open, set `FREEPI_AUTO_AD=off` and open the page printed
by `freepi-bridge ads`. Buying credits on the account also removes the requirement.

Hitting `403 ads_required` while a browser is open usually means the page was not
counted: hidden tabs and minimized windows never report an impression. Keep
`/ads` visible, then confirm a report landed:

```sh
freepi-bridge logs | grep 'ad impression'
```

## Commands

| Command | Does |
| --- | --- |
| `start [--bg] [--port N] [--bind H] [--insecure]` | run in the foreground, or detached with `--bg` |
| `stop`, `restart` | control the daemon |
| `status`, `logs [-f]` | inspect it |
| `models` | list available models |
| `usage` | today's credits, lane and token spend |
| `reset [--yes]` | free a session slot held by a crashed client |
| `doctor` | check token, upstream, bridge, bind, update; reports autostart only when the unit is installed but not running |
| `token`, `ads` | print the JWT in use / the ad page URL |
| `config [--init] [--set KEY=VALUE]` | show, create, or change one setting in `config.env`; `--set` validates the value and rewrites only that line |
| `autostart [--enable \| --disable] [--json]` | run at login and after reboot (systemd user unit, LaunchAgent, or Scheduled Task) |
| `update [--check] [--tag TAG]` | install the latest (or a pinned) release |

Exit code is `0` on success, `1` on error. Add `--json` to `status`, `models`,
`usage` and `doctor` for scripts.

## Configuration

Set variables in the environment or in `~/.freepi-bridge/config.env`
(`KEY=VALUE`, one per line). The environment wins. Run `freepi-bridge restart`
after editing.

| Variable | Default | Effect |
| --- | --- | --- |
| `FREEPI_TOKEN` | unset | account JWT |
| `BRIDGE_API_KEY` | unset | key clients must send; also protects `/ads` |
| `HOST`, `PORT` | `127.0.0.1`, `8787` | listen address |
| `FREEPI_AUTO_AD` | `on` | auto-report ads; `off` to disable |
| `FREEPI_AD_REFRESH_SECS` | `600` | seconds between reports (min 30) |
| `FREEPI_MAX_INFLIGHT` | `1` | completions sent upstream at once; `0` removes the gate |
| `FREEPI_QUEUE_WAIT_SECS` | `30` | how long a second request waits for the slot before answering `429` |
| `FREEPI_AUTO_UPDATE` | `on` | `on` installs a newer release and restarts the daemon, `off` never checks, `notify` only prints. At runtime a typo falls back to `on`; `config --set` rejects typos instead. Most commands (not `--health`, `--token`, `--version`, `help`, `update`) check GitHub at most once a minute (ETag + 60 s cache); read-only commands (`status`, `models`, `usage`, `ads`, `token`, `config`, `logs`, `autostart`, `stop`, `doctor`) only notify. All three autostart backends set `FREEPI_BRIDGE_NO_AUTO_UPDATE=1` so the daemon never replaces itself mid-flight |
| `FREEPI_BRIDGE_DIR` | `~/.freepi-bridge` | state and log directory |

Every boolean setting (`FREEPI_AUTO_AD`, `FREEPI_BRIDGE_INSECURE`, `FREEPI_AUTO_UPDATE`)
speaks the same words: `on`/`off`, plus `true`/`false`, `yes`/`no` and `1`/`0` for
compatibility. `config --set` rejects anything else; at runtime an unrecognised
value leaves the feature on.
| `FREEPI_CREDENTIALS` | `~/.free-pi/agent/credentials.json` | token file the bridge reads |
| `FREEPI_BASE_URL` | `https://api.freepi.ai` | upstream API base; point it at a mirror or a test server |
| `FREEPI_BRIDGE_DOWNLOAD_BASE` | unset | mirror for release downloads in `update` |
| `FREEPI_BRIDGE_INSECURE` | unset | `on` equals `--insecure` |
| `FREEPI_BRIDGE_NO_AUTO_UPDATE` | unset | any value disables self-update entirely; set by the autostart units |
| `TZ` | `UTC` | timezone sent with ad requests |

FreePi serves one completion per account at a time. The bridge therefore holds a
slot and lets a second request wait for it instead of failing straight away, up to
`FREEPI_QUEUE_WAIT_SECS`. A request that gives up waiting answers `429` with
`Retry-After`. Set `FREEPI_QUEUE_WAIT_SECS=0` to fail fast, or
`FREEPI_MAX_INFLIGHT=0` to send every request upstream unchanged.

Binding to a non-loopback address (`--bind 0.0.0.0`) requires `BRIDGE_API_KEY`
unless you pass `--insecure`.

## Docker

```sh
docker build -t freepi-bridge .
docker run -d --name freepi-bridge -p 8787:7860 \
  -e FREEPI_TOKEN=... -e BRIDGE_API_KEY=... freepi-bridge
```

Or: `cp .env.example .env`, fill in both values, then
`docker compose up -d --build`. The container runs as non-root on port 7860 and
has a `/health` check. Mount `/home/bridge/.freepi-bridge` to keep state across
rebuilds.

`-e BRIDGE_API_KEY=...` is not optional here: the image binds `0.0.0.0:7860`, and
the bridge exits on a non-loopback bind without a key. The port map is `8787:7860`
because 8787 is the bridge default outside the container.

## Update and uninstall

Self-update is on by default: every command checks for a newer release and
installs it. Turn it off with `FREEPI_AUTO_UPDATE=off`, or ask for notices only
with `notify`. Autostart units opt out so the daemon is not replaced under a
running process.

```sh
freepi-bridge update         # latest release; --check to only look
freepi-bridge autostart --enable   # at login and after reboot
```

| | Linux / macOS | Windows |
| --- | --- | --- |
| Uninstall | `freepi-bridge stop`<br>`rm ~/.local/bin/freepi-bridge`<br>`rm -rf ~/.freepi-bridge` | `.\install.ps1 -Uninstall` (add `-KeepState` to keep logs/config) |

Installed with `--system` or `PREFIX`? Delete the binary from there instead.
`~/.free-pi` belongs to the official FreePi CLI and is never touched.

## Troubleshooting

| Problem | Fix |
| --- | --- |
| `freepi-bridge: command not found` | restart the terminal; check `~/.local/bin` is in PATH |
| `401` | no token found: run `freepi-bridge token`, if empty see [Token](#token) |
| `403 ads_required` | see [Ads](#ads); `FREEPI_AUTO_AD=on` clears it without a browser |
| `403` with a browser open | the page was not counted; keep `/ads` visible and check `freepi-bridge logs \| grep 'ad impression'` |
| `409 concurrent_session` | the account already holds its four CLI session slots; the bridge calls `/session/reset` and retries once. A retry that still fails means another machine holds the slot, so run `freepi-bridge reset` once the other client is closed |
| `409 model_at_capacity` | that model is busy upstream. The bridge reports an ad, retries it once, then retries on the server's `default_model` and renames the reply back to the model you asked for, so the call still succeeds |
| `429 concurrent` | the account serves one request at a time and the bridge waited `FREEPI_QUEUE_WAIT_SECS` without getting the slot; another client keeps holding it, so raise the wait or give the second agent its own account |
| `429 hourly_ceiling` | hourly cap reached, wait for the reset. Ads cannot be skipped, and the cap is per account |
| `429 premium_allowance` | premium quota spent; switch to a model that reports `"free": true` in `freepi-bridge models --json`, since an id ending in `-flash` does not make a model free |
| anything else | `freepi-bridge doctor`, then `freepi-bridge logs` |

## Endpoints

`GET /v1/models` · `POST /v1/chat/completions` (SSE streaming) · `POST /tools/vision` ·
`GET /ads` · `GET /health`

`POST /tools/vision` answers free-pi-cli's `look_at_image` body
(`{image_b64, media_type, question}`) by sending the image to the chat model
itself (`FREEPI_VISION_MODEL`, default `deepseek-v4.1-flash`) instead of the
paid vision provider, and returns `{"text": …}`.

## Development

```sh
cargo test
cargo build --release
```

MSRV is Rust 1.89. CI runs on stable and 1.89.

## License

GPL-3.0-only. See [LICENSE](LICENSE).
