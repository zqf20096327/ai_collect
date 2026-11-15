<div align="center">

# freepi-bridge

**An OpenAI-compatible HTTP API for a FreePi account.**<br>
A single Rust binary, no runtime and no extra services.

![version](https://img.shields.io/badge/version-0.2.1-blue)
![msrv](https://img.shields.io/badge/msrv-1.89%2B-orange)
![license](https://img.shields.io/badge/license-GPL--3.0--only-blue)

</div>

Language: English | [Indonesia](README.id.md)

OpenAI-compatible API for a FreePi account. One static Rust binary, no runtime.

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
   - Model: pick one from `freepi-bridge models`

Test it:

```sh
curl http://127.0.0.1:8787/v1/chat/completions \
  -H 'content-type: application/json' \
  -d '{"model":"particle","messages":[{"role":"user","content":"hi"}]}'
```

`freepi-bridge models` prints the whole catalog. `deepseek-v4.1-flash` is a good
pick for coding.

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
(`FREEPI_AUTO_AD=1`), so it works on headless hosts. This claims ads nobody saw
and can get the account reviewed.

If you can keep a browser open, set `FREEPI_AUTO_AD=0` and open the page printed
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
| `doctor` | check token, upstream, bridge, bind |
| `token`, `ads` | print the JWT in use / the ad page URL |
| `config [--init]` | show or create `config.env` |
| `update [--check] [--tag TAG]` | install the latest (or a pinned) release |

Exit code is `0` on success, `1` on error. Add `--json` to `status`, `models`
and `doctor` for scripts.

## Configuration

Set variables in the environment or in `~/.freepi-bridge/config.env`
(`KEY=VALUE`, one per line). The environment wins. Run `freepi-bridge restart`
after editing.

| Variable | Default | Effect |
| --- | --- | --- |
| `FREEPI_TOKEN` | unset | account JWT |
| `BRIDGE_API_KEY` | unset | key clients must send; also protects `/ads` |
| `HOST`, `PORT` | `127.0.0.1`, `8787` | listen address |
| `FREEPI_AUTO_AD` | `1` | auto-report ads, `0` to disable |
| `FREEPI_AD_REFRESH_SECS` | `600` | seconds between reports (min 30) |
| `FREEPI_AUTO_UPDATE` | unset | `start --bg` and `restart` check at most once a day: unset prints a notice, `1` installs the release, `0` never checks. A running daemon is never checked by itself |
| `FREEPI_BRIDGE_DIR` | `~/.freepi-bridge` | state and log directory |

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

```sh
freepi-bridge update         # latest release; --check to only look
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
| `403 ads_required` | see [Ads](#ads); `FREEPI_AUTO_AD=1` clears it without a browser |
| `403` with a browser open | the page was not counted; keep `/ads` visible and check `freepi-bridge logs \| grep 'ad impression'` |
| `409 concurrent_session` | the account already holds its four CLI session slots; the bridge calls `/session/reset` and retries once, and a retry that still fails means another machine holds a slot |
| `409 model_at_capacity` | that model is busy upstream; wait a few minutes or pick another free model |
| `429 concurrent` | one active request per account; another client or a second agent is using the same FreePi account |
| `429 hourly_ceiling` | hourly cap reached, wait for the reset. Ads cannot be skipped, and the cap is per account |
| `429 premium_allowance` | premium quota spent; move to a model marked `Free Unlimited` in `freepi-bridge models` (`particle`, `deepseek-v4.1-flash`, `glm-5.3-flash`, `deepseek-v4-flash`), since an id ending in `-flash` does not make a model free |
| anything else | `freepi-bridge doctor`, then `freepi-bridge logs` |

## Endpoints

`GET /v1/models` · `POST /v1/chat/completions` (SSE streaming) · `GET /ads` ·
`GET /health`

## Development

```sh
cargo test
cargo build --release
```

MSRV is Rust 1.89. CI runs on stable and 1.89.

## License

GPL-3.0-only. See [LICENSE](LICENSE).
