<div align="center">

# freepi-bridge

**An OpenAI-compatible HTTP API for a FreePi account.**<br>
A single Rust binary, no runtime and no extra services.

![version](https://img.shields.io/badge/version-0.2.0-blue)
![msrv](https://img.shields.io/badge/msrv-1.89%2B-orange)
![license](https://img.shields.io/badge/license-GPL--3.0--only-blue)

</div>

Language: English | [Indonesia](README.id.md)

FreePi's API expects its own client. Every completion needs `x-client-version` and `x-session-id` headers, and free completions stay paused until the account has shown an ad (`403 ads_required`). The bridge adds those headers, serves the ad page, and forwards completions to `api.freepi.ai`. Any OpenAI-compatible client works once it points at the bridge.

```
client ──/v1/chat/completions──▶ freepi-bridge ──▶ api.freepi.ai
                                     │
                              /ads (web page)
```

## Prerequisites

The bridge has no login of its own. It spends a FreePi account, so it needs that account's JWT: either `FREEPI_TOKEN` in the environment, or the credentials file the official CLI writes to `~/.free-pi/agent/credentials.json`. Without one of the two, `freepi-bridge token` prints nothing and every completion fails with `401`.

The easiest way to get the file is to run the official CLI once. You do not have to keep it or use it as your editor:

```bash
npx free-pi-cli@latest      # needs Node.js 22.15+; downloads, runs, stores the token
```

That is a one-off: sign in with GitHub, accept the consent screen, and quit. `~/.free-pi/agent/credentials.json` now holds the token and the bridge reuses it forever. Running `npx free-pi-cli@latest` again later is also how you re-sign in if the token expires.

Install it globally instead if you would rather not download it each time, or if you also want to use it as a coding agent:

```bash
npm install -g free-pi-cli
free-pi-cli
```

On a machine that cannot run Node or a browser (a container, a CI runner), skip the CLI and pass the JWT directly:

```bash
FREEPI_TOKEN=eyJ... freepi-bridge start --bg
```

## Install

A prebuilt binary exists for every supported system, so no Rust toolchain is needed. Pick your platform:

| System | Installer | Lands in |
|---|---|---|
| Linux x86_64, aarch64 | `install.sh` | `~/.local/bin` |
| macOS 11+ on arm64, x86_64 | `install.sh` | `~/.local/bin` |
| WSL2 | `install.sh` (same as Linux) | `~/.local/bin` |
| Windows 10+ on x86_64 | `install.ps1` | `%LOCALAPPDATA%\Programs\freepi-bridge`, added to the user PATH |
| Windows on arm64 | `install.ps1` (x64 build, under emulation) | `%LOCALAPPDATA%\Programs\freepi-bridge` |
| Docker, any host | `docker run`, see [Docker](#docker) | container only |
| Anything else | `cargo install --path .` from a clone | `~/.cargo/bin` |

Linux, macOS and WSL2:

```bash
curl -fsSL https://raw.githubusercontent.com/ihsan-ramadhan/freepi-bridge/main/install.sh | sh
```

Windows, in PowerShell 5.1 or newer:

```powershell
irm https://raw.githubusercontent.com/ihsan-ramadhan/freepi-bridge/main/install.ps1 | iex
```

Both installers fetch the release binary and check its `.sha256` when the release publishes one.

| Flag or variable | Effect |
|---|---|
| `--version v0.1.0` | install a pinned release instead of the latest |
| `--from-source` | skip the release and build with `cargo` |
| `--system` | install into `/usr/local/bin` |
| `PREFIX=/opt/x` | install into `PREFIX/bin` |
| `FREEPI_BRIDGE_DOWNLOAD_BASE` | mirror base URL, default `https://github.com/ihsan-ramadhan/freepi-bridge/releases` |

The PowerShell script takes `-Prefix`, `-Version`, `-FromSource` and `-NoPath`. Piping into `iex` leaves no room for arguments, so the same values come from `FREEPI_BRIDGE_PREFIX`, `FREEPI_BRIDGE_VERSION` and `FREEPI_BRIDGE_DOWNLOAD_BASE`.

Running `./install.sh` from a clone builds locally instead. If no release is reachable, both scripts fall back to `git clone` plus `cargo build --release`. `cargo install --path .` also works.

### Uninstall

Linux and macOS: stop the daemon, delete the binary, delete the state directory.

```bash
freepi-bridge stop
rm ~/.local/bin/freepi-bridge
rm -rf ~/.freepi-bridge
```

If you installed with `PREFIX=/opt/x` or `--system`, delete the binary from there instead, and if you set `FREEPI_BRIDGE_DIR`, delete that directory instead of `~/.freepi-bridge`.

Windows: the installer also edits your user PATH, so uninstall through the script.

```powershell
irm https://raw.githubusercontent.com/ihsan-ramadhan/freepi-bridge/main/install.ps1 -OutFile install.ps1
.\install.ps1 -Uninstall
```

`-Uninstall` stops the daemon, deletes `%LOCALAPPDATA%\Programs\freepi-bridge`, removes that folder from the user PATH, and deletes `%USERPROFILE%\.freepi-bridge`. Add `-KeepState` to keep the state directory with its log and config, and `-Prefix <dir>` if you installed somewhere else. Piped usage works too: set `$env:FREEPI_BRIDGE_UNINSTALL='1'` before `irm … | iex`.

Both paths leave `~/.free-pi` alone; that directory belongs to the official FreePi CLI.

### Details per platform

| Platform | What you get |
|---|---|
| Linux x86_64, aarch64 | static musl binary; no glibc version to match |
| macOS 11+ on arm64 and x86_64 | release binary; the installer picks by `uname -m` |
| Windows 10+ on x86_64 | release `.exe`; the daemon is managed with `tasklist` and `taskkill` |
| Windows on arm64 | the x64 build, under emulation |
| WSL2 | use the Linux build |
| Docker | `debian-bookworm-slim` runtime |

`install.sh` is POSIX `sh`, so it also runs under `dash`, `busybox sh` and `zsh`. It reads checksums with `sha256sum` or `shasum -a 256`, and skips verification on machines that have neither. `install.ps1` needs PowerShell 5.1, which ships with Windows 10. State and log paths follow `HOME`, or `USERPROFILE` on Windows.

## Quick start

```bash
freepi-bridge start --bg     # daemon on 127.0.0.1:8787
freepi-bridge doctor         # token, upstream, bridge, bind
```

Point your client at `http://127.0.0.1:8787/v1`:

```bash
curl http://127.0.0.1:8787/v1/chat/completions \
  -H 'content-type: application/json' \
  -d '{"model":"particle","messages":[{"role":"user","content":"hi"}]}'
```

With `BRIDGE_API_KEY` set, send it as the bearer token:

```bash
curl http://127.0.0.1:8787/v1/chat/completions \
  -H "authorization: Bearer $BRIDGE_API_KEY" \
  -H 'content-type: application/json' \
  -d '{"model":"particle","messages":[{"role":"user","content":"hi"}]}'
```

On Windows, `curl` is an alias for `Invoke-WebRequest` in PowerShell 5.1, so call `curl.exe` or use the native cmdlet:

```powershell
$body = '{"model":"particle","messages":[{"role":"user","content":"hi"}]}'
Invoke-RestMethod http://127.0.0.1:8787/v1/chat/completions `
  -Method Post -ContentType 'application/json' -Body $body
```

The bridge reuses the account JWT that the official FreePi CLI already stored in `~/.free-pi/agent/credentials.json`. If `freepi-bridge token` prints nothing, see [Prerequisites](#prerequisites).

The bridge reports ads by itself, so a container, VM or remote box gets completions without a browser; `FREEPI_AUTO_AD=0` turns that off and leaves `/ads` as the only way to clear `403 ads_required`. See [Automatic reports](#automatic-reports).

## Commands

| Command | What it does |
|---|---|
| `freepi-bridge start [--bg] [--port N] [--bind H] [--insecure]` | Run the bridge in the foreground, or detached with `--bg`. A non-loopback bind requires `BRIDGE_API_KEY` unless you pass `--insecure` |
| `freepi-bridge stop` | Stop the detached process recorded in `state.json`: graceful signal first, forced kill after 5 s |
| `freepi-bridge restart [--port N] [--bind H]` | Stop, then start detached again |
| `freepi-bridge status [--json]` | pid, URL, health and model count of the daemon |
| `freepi-bridge models [--json]` | Live model catalog from the FreePi `/client-version` endpoint |
| `freepi-bridge doctor [--json]` | Check token, upstream, bridge and bind safety |
| `freepi-bridge logs [-f]` | Print the last 200 log lines; `-f` follows |
| `freepi-bridge token` | Print the JWT the bridge uses |
| `freepi-bridge ads` | Print the ad page URL, with the key when one is set |
| `freepi-bridge config [--init]` | Print the local config file; `--init` creates it when it is missing |
| `freepi-bridge update [--check] [--tag TAG]` | Install the newest release in place; `--check` only reports, `--tag` pins a release |
| `freepi-bridge version`, `--version` | Print the version |
| `freepi-bridge help`, `--help` | Global help; `<command> --help` for one command |

Exit code is `0` on success and `1` on error: daemon down, bad flag, failed check.

### Environment

Every variable here can also live in [the config file](#configuration); the environment wins.

| Variable | Default | Effect |
|---|---|---|
| `FREEPI_BASE_URL` | `https://api.freepi.ai` | Upstream API |
| `FREEPI_TOKEN` | unset | Account JWT; overrides the credentials file |
| `FREEPI_CREDENTIALS` | `~/.free-pi/agent/credentials.json` | Token file written by the official CLI |
| `BRIDGE_API_KEY` | unset | Shared key clients must send; also gates `/ads` |
| `HOST`, `PORT` | `127.0.0.1`, `8787` | Listen address |
| `FREEPI_BRIDGE_DIR` | `~/.freepi-bridge` | State and log directory |
| `FREEPI_BRIDGE_INSECURE` | unset | `1` behaves like `--insecure` |
| `FREEPI_AUTO_AD` | `1` | `1` on by default, `0` off; the bridge reports an ad without the ad page |
| `FREEPI_AD_REFRESH_SECS` | `600` | Seconds between automatic ad reports; values under 30 are ignored |
| `FREEPI_AUTO_UPDATE` | unset | `start --bg` checks once a day: unset prints a notice, `1` installs the update, `0` never checks |
| `FREEPI_BRIDGE_DOWNLOAD_BASE` | GitHub releases | Mirror base URL for update downloads |
| `TZ` | `UTC` | Sent as `x-client-timezone` on ad requests |

## Configuration

Settings can live in `~/.freepi-bridge/config.env` (or `$FREEPI_BRIDGE_DIR/config.env`) instead of your shell, so a daemon started by a supervisor, a cron job, or after a reboot keeps them. Both installers create the file, and a plain `start` creates it too, so there is always something to edit. It is written `0600` on Linux and macOS (Windows uses the user's default ACL) because it may hold `FREEPI_TOKEN` or `BRIDGE_API_KEY`.

```ini
# freepi-bridge configuration
FREEPI_AUTO_AD=1
FREEPI_AD_REFRESH_SECS=300
BRIDGE_API_KEY=
# PORT=8787
```

`KEY=VALUE` per line, `#` starts a comment (put a space before it, or quote the value, to keep a `#` inside one), and matching quotes around a value are stripped. Unknown keys are reported on stderr and ignored, so a typo cannot quietly change how the bridge runs. The real environment wins over the file, which keeps one-off overrides working (`FREEPI_AUTO_AD=0 freepi-bridge start --bg`). Edits apply on the next start: `freepi-bridge restart`.

```bash
freepi-bridge config            # print the path and the current contents
freepi-bridge config --init     # create it if it is missing; never overwrites
```

`FREEPI_BRIDGE_DIR` is the one variable the file cannot set, because it decides where the file is read from.

## Updates

`freepi-bridge update` replaces the running binary with the newest release: it reads `releases/latest` from GitHub, downloads the asset built for this platform, checks the published `.sha256`, swaps the binary, and restarts the daemon if one was running.

```bash
freepi-bridge update                # install the latest release
freepi-bridge update --check        # only say whether a newer one exists
freepi-bridge update --tag v0.1.2   # install a specific release, or roll back
```

The same command works on Linux x86_64/aarch64, macOS arm64/x86_64 and Windows 10+ x86_64. It only writes next to the binary, so an install that needed root (`/usr/local/bin`) has to be updated with `sudo`. A failed download or a checksum mismatch leaves the current binary untouched. On Windows the running image is renamed to `freepi-bridge.exe.old` and removed on the next start.

`start --bg`, and therefore `restart`, checks at most once a day (the stamp lives in the state directory) and prints one line when a newer release exists. `FREEPI_AUTO_UPDATE=1` installs it before the daemon starts; `FREEPI_AUTO_UPDATE=0` never checks. A foreground `start`, which is what Docker and process supervisors run, never self-updates: build a new image or re-run the installer there.

## Endpoints

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/v1/models` | Model list from FreePi `/client-version`, cached for 5 minutes |
| `POST` | `/v1/chat/completions` | Chat completions, including streaming SSE passthrough |
| `GET` | `/ads/next?slot=inline\|banner` | Ad creative for this account |
| `POST` | `/ads/impression` | Report `{ad_id, click_token, imp_fired}` |
| `GET` | `/ads` | Page that renders an ad and reports the impression |
| `GET` | `/health`, `/healthz` | Liveness probe |

The bridge looks for a token in this order:

1. a JWT from the client in `Authorization: Bearer eyJ...`, accepted only when `BRIDGE_API_KEY` is unset
2. `FREEPI_TOKEN`
3. the credentials file (`FREEPI_CREDENTIALS`, else `~/.free-pi/agent/credentials.json`)

## Ads

FreePi is ad-funded. An account with no recent impression gets `403 ads_required` and completions stay paused until the ad page runs. The bridge follows the same protocol as the official CLI:

- `GET /ads/next?slot=inline` returns `{ad_id, click_token, creative:{headline,body,cta}, click_url, imp_url, source}`
- `POST /ads/impression {ad_id, click_token, imp_fired}` reports the view
- `GET /ads?key=<BRIDGE_API_KEY>` renders the creative, waits until it is visible (`IntersectionObserver` plus page visibility), fires the ad network pixel, then reports the impression

```bash
freepi-bridge ads     # prints the URL to open
```

Keep the page open while you work. Reporting an impression for a creative nobody saw is impression fraud and can get the account reviewed. Credits bought on the account remove the requirement.

### Headless hosts

`/ads` only listens on the bridge's own port. A container or a CI runner cannot open it, so the bridge reports an ad by itself and retries a gated completion once, which is what `FREEPI_AUTO_AD` does and why it starts out on. `FREEPI_AUTO_AD=0` leaves the account alone, and such a host then keeps answering `403 ads_required`.

### Automatic reports

The bridge reports an ad by itself every `FREEPI_AD_REFRESH_SECS` seconds, so completions keep working on a container, a CI runner or any host where no browser can open `/ads`. `FREEPI_AUTO_AD` is read once, when the process starts, from the environment or [the config file](#configuration); `0` turns the reports off.

```bash
freepi-bridge token          # empty? see Prerequisites
freepi-bridge start --bg
freepi-bridge logs | grep 'ad impression'
# ad impression reported (session ..., gravity false)
```

`start --bg` copies its environment into the detached child, so the setting survives. `restart` re-reads the shell and the config file of the command that runs it, not the daemon it replaced, so `FREEPI_AUTO_AD=0 freepi-bridge restart` switches one run to real ad views; put `FREEPI_AUTO_AD=0` in `~/.freepi-bridge/config.env` to make it stick. Supervisors work the same way: `Environment=FREEPI_AUTO_AD=0` in a systemd unit, `-e FREEPI_AUTO_AD=0` for `docker run`.

`freepi-bridge ads` prints the page to open when you would rather see the ad for real.

Automatic reports claim an ad nobody saw, which is impression fraud and can get the account reviewed; set `FREEPI_AUTO_AD=0` on any machine where a browser can keep `/ads` open.

## Docker

```bash
docker build -t freepi-bridge .
docker run -d --name freepi-bridge -p 8787:7860 \
  -e FREEPI_TOKEN=... -e BRIDGE_API_KEY=... freepi-bridge
```

## Docker Compose

```bash
cp .env.example .env      # set FREEPI_TOKEN and BRIDGE_API_KEY
docker compose up -d --build
docker compose logs -f
```

The container runs as a non-root user, binds `0.0.0.0:7860`, and ships a `/health` healthcheck. Binding `0.0.0.0` makes the bridge require `BRIDGE_API_KEY` (or `FREEPI_BRIDGE_INSECURE=1`), so a run without either exits on start. State and `config.env` live inside the container; mount `/home/bridge/.freepi-bridge` if you want them to survive a rebuild. The token arrives through `FREEPI_TOKEN`.

## Development

```bash
cargo test                       # mock upstream: auth, header injection, SSE, ads
cargo build --release
PREFIX=/tmp/out ./install.sh     # local build, no release download
```

The MSRV is 1.89, set by `uuid` 1.29. CI runs the suite on stable and on 1.89, so the badge cannot drift without a red build.

Measured on an i5-13420H against a local mock upstream at 50 concurrent connections: about 30k req/s, 1.5 ms p50 added per request, 6.8 MB RSS, 2.8 MB binary. Real FreePi completions take seconds, so the proxy hop does not show up in practice.

## License

GPL-3.0-only. See [LICENSE](LICENSE).
