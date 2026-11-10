<div align="center">

# DoubleCrawl CLI

**Ask for a page. Get the page. From your terminal, your scripts or your AI agent, and pay only for pages that arrive.**

[![Latest release](https://img.shields.io/github/v/release/doubledata/doublecrawl-cli?label=release&color=2f6feb)](https://github.com/doubledata/doublecrawl-cli/releases/latest)
[![Platforms](https://img.shields.io/badge/platforms-macOS%20%7C%20Linux%20%7C%20Windows-555)](https://github.com/doubledata/doublecrawl-cli/releases/latest)
[![Signed with Sigstore](https://img.shields.io/badge/releases-cosign%20signed%20%2B%20SBOM-4c1)](https://github.com/doubledata/doublecrawl-cli#security)
[![GitHub stars](https://img.shields.io/github/stars/doubledata/doublecrawl-cli?style=social)](https://github.com/doubledata/doublecrawl-cli)

[Website](https://doublecrawl.com) · [Console](https://app.doublecrawl.com) · [Docs](https://doublecrawl.com/docs/) · [Releases](https://github.com/doubledata/doublecrawl-cli/releases)

</div>

```sh
curl -fsSL https://github.com/doubledata/doublecrawl-cli/releases/latest/download/install.sh | sh
doublecrawl login
doublecrawl fetch https://example.com
```

**500 free credits when you sign up, no card required.** Earn up to 850 more in your first session,
including **+250 for starring this repo** ([how](#free-credits)).

---

## Why DoubleCrawl

- **Pages, not proxy plumbing.** Send a URL, get the page back. DoubleCrawl handles the route to the target;
  you pick an exit country with one flag when you need one.
- **Failed pages cost 0.** You pay for pages that arrive (and for a truthful "page missing" answer).
  Failed tries, timeouts and our own retries are on us.
- **Built for agents.** Every command speaks `--json`, exit codes are documented, and the same account works
  from the CLI, the [hosted MCP server](#use-with-ai-agents) and the Claude Code plugin.
- **One account everywhere.** Sign in once in the browser. Credits, API keys, usage and request logs are the
  same in the terminal and in the [console](https://app.doublecrawl.com).
- **One static binary.** No runtime, no daemon. Credentials live in your OS keychain, and every release is
  signed with Sigstore and ships with SBOMs.

## Contents

- [Install](#install)
- [Quickstart](#quickstart)
- [Commands](#commands)
- [Scripting and JSON output](#scripting-and-json-output)
- [Use with AI agents](#use-with-ai-agents)
- [Configuration](#configuration)
- [Exit codes](#exit-codes)
- [Free credits](#free-credits) and [pricing](#pricing)
- [Security](#security)
- [Troubleshooting](#troubleshooting)

## Install

| Platform | How |
| --- | --- |
| macOS, Linux | `curl -fsSL https://github.com/doubledata/doublecrawl-cli/releases/latest/download/install.sh \| sh` |
| Windows | Download `doublecrawl_windows_amd64.zip` (or `_arm64.zip`) from the [latest release](https://github.com/doubledata/doublecrawl-cli/releases/latest) and put `doublecrawl.exe` on your `PATH` |

Every platform has `amd64` and `arm64` builds. Check the install with `doublecrawl version`.

<details>
<summary><b>What the install script does, and its options</b></summary>

The script detects your OS and CPU, downloads the matching archive and `checksums.txt`, and checks the
archive's SHA-256 before installing anything. If [`cosign`](https://docs.sigstore.dev/cosign/system_config/installation/)
(v2.6 or newer) is on your `PATH`, it also verifies the Sigstore signature of `checksums.txt` and stops if it
does not match.

It installs to `/usr/local/bin` when that is writable, and to `~/.local/bin` otherwise (it tells you if that
directory is not on your `PATH`).

| Variable | Default | Effect |
| --- | --- | --- |
| `DOUBLECRAWL_VERSION` | `latest` | Install a specific version, e.g. `0.1.0` |
| `DOUBLECRAWL_INSTALL_DIR` | `/usr/local/bin` | Where to put the binary |

```sh
curl -fsSL https://github.com/doubledata/doublecrawl-cli/releases/latest/download/install.sh \
  | DOUBLECRAWL_VERSION=0.1.0 DOUBLECRAWL_INSTALL_DIR="$HOME/bin" sh
```

</details>

**Upgrading.** `doublecrawl update` prints the upgrade command (re-running the install script).

**Shell completion.** `doublecrawl completion bash|zsh|fish|powershell` prints a completion script;
`doublecrawl completion zsh --help` shows where to put it.

## Quickstart

**1. Sign in.** This opens your browser on the DoubleCrawl console. Confirm the code, pick a workspace, done.
New here? You can create a free account on the same page.

```console
$ doublecrawl login
Your code: WDJB-MJHT
Open https://app.doublecrawl.com/device and confirm the code.
Signed in as you@example.com · Acme (credentials in the keychain)
```

On a remote machine or over SSH, add `--no-browser` and open the printed URL on any device.

**2. Fetch a page.** The page body goes to stdout, so it pipes and redirects like `curl`.

```console
$ doublecrawl fetch https://example.com -i
HTTP 200 · delivered · req_abc123def456
content-type: text/html; charset=UTF-8
...

<!doctype html>
<html>
<head>
    <title>Example Domain</title>
...
```

**3. See your credits.**

```console
$ doublecrawl balance
1,000 credits
SOURCE               REMAINING  EXPIRES
Sign-up              500        Never
Agent bonus          250        2027-02-08
First request bonus  250        2027-02-08
```

The agent and first-request bonuses are paid automatically: `login` connects the CLI as an agent, and your
first `fetch` is your first request.

## Commands

| Command | What it does |
| --- | --- |
| [`login`](#login-and-logout) | Sign this terminal in through the browser |
| [`logout`](#login-and-logout) | Disconnect the CLI agent, end the session and forget the credentials |
| [`fetch <url>`](#fetch) | Fetch a page through DoubleCrawl |
| [`balance`](#balance) | Show the credits left and where they come from |
| [`usage`](#usage) | Show requests, success rate and credits per domain or key |
| [`logs`](#logs) | List recent requests, or stream new ones with `--follow` |
| [`keys`](#keys) | Manage the workspace's API keys: `list`, `create`, `rotate`, `revoke` |
| [`topup`](#topup) | Open the console's top-up page |
| `update` | Print the command that upgrades the CLI |
| `version` | Print the CLI version |
| `completion` | Generate the autocompletion script for your shell |

Every command accepts `--json` (machine-readable output) and `-h, --help`.

### `fetch`

```text
doublecrawl fetch <url> [flags]

      --country string       exit country: us, de, gb, es, pl or jp
  -H, --header stringArray   request header 'Name: value' (repeatable)
  -i, --include              print the status line and response headers
      --method string        GET or POST (default "GET")
      --session-id string    reuse one exit IP across requests
```

```sh
# Save a page
doublecrawl fetch https://example.com > page.html

# Fetch from Germany, with a German Accept-Language
doublecrawl fetch https://example.com --country de -H 'Accept-Language: de-DE'

# Keep the same exit IP across a multi-step flow
doublecrawl fetch https://example.com/step-1 --session-id checkout-42
doublecrawl fetch https://example.com/step-2 --session-id checkout-42

# Status, headers and body as one JSON object
doublecrawl fetch https://example.com --json | jq '{status, targetOutcome, requestId}'
```

Good to know:

- The URL must be a full public `http://` or `https://` address. Local and private addresses (`localhost`,
  `10.0.0.0/8`, `*.internal`, ...) are rejected before anything is sent, so they cost nothing.
- `Authorization`, `Host`, `Cookie`, hop-by-hop, `Proxy-*`, `X-Forwarded-*` and `X-DD-*` headers are set by
  DoubleCrawl and can't be overridden with `-H`.
- The status line shows the outcome: **delivered** (you got the page), **absent** (the target says the page
  does not exist; billed, exit code `7`) or **refused** (the page did not arrive; not billed).
- `fetch` waits up to 2 minutes. If no answer comes back the request may still finish and be billed: check
  `doublecrawl logs` before retrying.

### `login` and `logout`

```sh
doublecrawl login                      # opens the browser
doublecrawl login --no-browser         # prints the URL instead
doublecrawl login --workspace "Acme"   # preselect a workspace by name or id
doublecrawl logout                     # disconnects this terminal everywhere
```

`login` creates a CLI agent for this machine (you can see and disconnect it in the console under
**Agents & MCP**). If your role in the workspace can't connect agents, you are signed in read-only: `balance`,
`usage` and `logs` work, and `fetch` needs an API key in `DOUBLECRAWL_API_KEY`.

### `balance`

Shows the total and every credit lot with its source and expiry date. `--json` returns the raw lots.

### `usage`

```console
$ doublecrawl usage --range 7d
42 requests · 97.6% success · 63 credits · <$0.01
DOMAIN        REQUESTS  SUCCESS  CREDITS
example.com   30        100.0%   45
example.org   12        91.7%    18
```

`--range` takes `24h`, `7d`, `30d` (default) or `90d`. `--group` takes `domain` (default), `key` or `both`.

### `logs`

```console
$ doublecrawl logs --limit 3
TIME                  RESULT        STATUS  CREDITS  URL
2026-11-10 09:12:44Z  Delivered     200     1        https://example.com/
2026-11-10 09:12:40Z  Missing       404     1        https://example.com/old-page
2026-11-10 09:12:31Z  Refused       403     0        https://example.org/
```

```sh
doublecrawl logs --follow                    # stream new requests until Ctrl-C
doublecrawl logs --outcome refused           # delivered, absent, refused or requester_gone
doublecrawl logs -q example.com --limit 100  # search the URL or request id
doublecrawl logs --key <key-id>              # one API key only
```

### `keys`

API keys let servers, CI jobs and other tools call DoubleCrawl without a browser login.

```sh
doublecrawl keys list                          # active keys (--all includes revoked ones)
doublecrawl keys create ci --monthly-cap 50000 # print the new key once
doublecrawl keys rotate ci                     # new key now, old one stops in 24h (--old-stops now)
doublecrawl keys revoke ci --yes               # stop a key immediately
```

`create` and `rotate` print only the key on stdout (the notes go to stderr), so you can capture it directly:

```sh
export DOUBLECRAWL_API_KEY="$(doublecrawl keys create ci)"
```

A key created from the CLI has a monthly credit limit of at most 100,000 credits, which is also the default.
Manage all keys in the [console](https://app.doublecrawl.com/keys).

### `topup`

Opens the top-up page for the CLI's workspace in the browser (`--no-browser` prints the URL).

## Scripting and JSON output

- **stdout is data, stderr is talk.** Page bodies, tables and JSON go to stdout. Prompts, warnings and errors
  go to stderr.
- **`--json` on every command.** Errors become JSON too, on stderr, with the HTTP status and a stable code:

  ```json
  {"error":{"status":402,"code":"credits_exhausted","title":"Out of credits: top up with doublecrawl topup or https://app.doublecrawl.com/topup.","detail":""}}
  ```

- **Exit codes mean something.** A script can tell "out of credits" from "page missing" without parsing text.
  See [Exit codes](#exit-codes).

```sh
# Fetch a list of URLs, keep going on missing pages, stop when credits run out
while read -r url; do
  doublecrawl fetch "$url" --json > "out/$(echo "$url" | shasum | cut -c1-12).json"
  case $? in
    0|7) ;;               # delivered, or the page doesn't exist
    4) echo "out of credits"; break ;;
    *) echo "failed: $url" >&2 ;;
  esac
done < urls.txt
```

In CI, skip the browser: create a key once with `doublecrawl keys create ci`, store it as a secret, and expose
it as `DOUBLECRAWL_API_KEY`. `fetch` uses it; the account commands (`balance`, `usage`, `logs`, `keys`) need a
`login`.

## Use with AI agents

**Agents that run shell commands** (Claude Code, Codex, Cursor, Gemini CLI, ...) can use the CLI as-is:
`doublecrawl fetch <url>` returns the page, `--json` gives structured output, and exit codes tell the agent what
happened. Signing in with `doublecrawl login` registers the terminal as an agent you can see, limit and
disconnect in the console.

**Agents that speak MCP** can use the hosted server at `https://mcp.doublecrawl.com/mcp` (OAuth sign-in, no key
to paste):

```sh
# Claude Code: install the plugin
/plugin marketplace add doubledata/doublecrawl
/plugin install doublecrawl@doublecrawl

# Codex
codex mcp add doublecrawl --url https://mcp.doublecrawl.com/mcp

# VS Code
code --add-mcp '{"name": "doublecrawl", "type": "http", "url": "https://mcp.doublecrawl.com/mcp"}'
```

```jsonc
// Cursor (~/.cursor/mcp.json) and most other clients
{ "mcpServers": { "doublecrawl": { "url": "https://mcp.doublecrawl.com/mcp" } } }
```

The MCP server gives the agent `fetch_page`, `get_balance`, `get_usage`, `list_requests`, `list_invoices`,
`request_top_up` and `get_top_up_status`. Agents can **ask** for a top-up but never move money on their own: a
person approves it in the console. Setup for ChatGPT, Windsurf, Gemini CLI, Zed and others is in the console
under [Agents & MCP](https://app.doublecrawl.com/connect).

## Configuration

The CLI needs no config file. Everything is a flag or an environment variable.

| Variable | Default | Purpose |
| --- | --- | --- |
| `DOUBLECRAWL_API_KEY` | | API key for `fetch`. Takes precedence over the login's agent token |
| `DOUBLECRAWL_CREDENTIALS` | keychain, then file | `keychain` or `file`: where `login` stores credentials |
| `DOUBLECRAWL_CONFIG_DIR` | your OS config dir + `/doublecrawl` | Where the credentials file lives |
| `DOUBLECRAWL_CONSOLE_URL` | `https://app.doublecrawl.com` | Console to sign in to |
| `DOUBLECRAWL_ROUTER_URL` | `https://double-router-eu.doubledata.com` | Endpoint `fetch` sends requests to |

**Credentials.** `login` saves to the OS keychain (macOS Keychain, Windows Credential Manager, Secret Service
on Linux). When no keychain is available it falls back to `credentials.json` with mode `0600` in the config
directory, and refuses to read that file if other users can.

## Exit codes

| Code | Meaning |
| --- | --- |
| `0` | Success |
| `1` | Any other error (network, unexpected server response) |
| `2` | Usage error: bad flag, argument or URL |
| `3` | Not signed in, session expired, or the API key was rejected |
| `4` | Out of credits |
| `5` | The key's or agent's monthly credit limit is reached |
| `6` | Suspended, or turned off for agents by a workspace policy |
| `7` | `fetch` only: the page does not exist (the request was billed) |

## Free credits

| How | Credits |
| --- | --- |
| Sign up (Free plan, no card) | **500**, never expire |
| Connect an agent (`doublecrawl login` counts) | +250 |
| Make your first request | +250 |
| Turn on two-step verification | +100 |
| **Star [doublecrawl-cli](https://github.com/doubledata/doublecrawl-cli) on GitHub** | **+250** |

To claim the star bonus, star this repository, then press **Verify** in the console's onboarding (you'll be
asked to connect your GitHub account once). Bonus credits expire after 90 days; each bonus is paid once.

## Pricing

You pay in credits. Delivered pages and truthful "page missing" answers are billed; requests the target
refuses are not. Each request's credits show up in `doublecrawl logs` and `doublecrawl usage`.

After the free credits, choose a monthly plan or top up as you go; see plans in the
[console](https://app.doublecrawl.com/billing/plan) and at [doublecrawl.com](https://doublecrawl.com).
Run `doublecrawl topup` to add credits.

## Security

- **Signed releases.** Every release's `checksums.txt` is signed keyless with
  [Sigstore cosign](https://docs.sigstore.dev/) from GitHub Actions, and the install script checks it when
  `cosign` is installed.
- **SBOMs.** Each archive ships with a software bill of materials, attached to the
  [release](https://github.com/doubledata/doublecrawl-cli/releases/latest).
- **Static builds.** Pure Go, no cgo, built with `-trimpath`.
- **Your credentials stay local.** Stored in the OS keychain (or a `0600` file), never printed. `logout`
  revokes the CLI agent and the session on the server, not just locally.
- **No look-alike login pages.** The CLI only opens the browser on the console's own origin.

Verify a download by hand (cosign v2.6+):

```sh
VERSION=0.1.0
BASE=https://github.com/doubledata/doublecrawl-cli/releases/download/v$VERSION
curl -fsSLO "$BASE/checksums.txt" -O "$BASE/checksums.txt.sigstore.json" -O "$BASE/doublecrawl_linux_amd64.tar.gz"

cosign verify-blob checksums.txt \
  --bundle checksums.txt.sigstore.json \
  --certificate-identity https://github.com/DoubleData/double-crawl-console/.github/workflows/cli-release.yml@refs/heads/main \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com

sha256sum --check --ignore-missing checksums.txt   # macOS: shasum -a 256 -c --ignore-missing checksums.txt
```

## Troubleshooting

**`Error: not signed in: run doublecrawl login`** (exit 3). `DOUBLECRAWL_API_KEY` only covers `fetch`; the
account commands need a login.

**`this login has no router token`** (exit 3). Your role (billing or viewer) can't connect agents, so `fetch`
needs `DOUBLECRAWL_API_KEY` from a teammate who can create keys.

**`Out of credits`** (exit 4). Run `doublecrawl topup`, or check what is left with `doublecrawl balance`.

**`reached its monthly credit limit`** (exit 5). Raise the limit of the key in the console's
[API keys](https://app.doublecrawl.com/keys), or of the CLI agent in [Agents & MCP](https://app.doublecrawl.com/connect).

**`This terminal's CLI agent was disconnected`** (exit 3). Someone disconnected it in the console, or your
role changed. Run `doublecrawl login` again.

**`keychain unavailable ... credentials saved to ...`** Common on headless Linux without Secret Service. It's
a warning, not an error; set `DOUBLECRAWL_CREDENTIALS=file` to silence it.

**The browser doesn't open.** Use `doublecrawl login --no-browser` and open the printed URL yourself.

**`No answer from the router`.** The request may still finish and be billed. Look it up with
`doublecrawl logs -q <url>` before retrying.

## Support

- Docs: [doublecrawl.com/docs](https://doublecrawl.com/docs/)
- Console: [app.doublecrawl.com](https://app.doublecrawl.com)
- Bugs and feature requests: [open an issue](https://github.com/doubledata/doublecrawl-cli/issues)

<div align="center">

If the CLI saves you time, [give it a star](https://github.com/doubledata/doublecrawl-cli): it helps others
find it, and it's worth 250 credits to you.

</div>
