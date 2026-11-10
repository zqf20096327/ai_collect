# Kraken CLI

[![GitHub stars](https://img.shields.io/github/stars/krakenfx/kraken-cli?style=social)](https://github.com/krakenfx/kraken-cli)
[![version](https://img.shields.io/github/v/release/krakenfx/kraken-cli?color=blue)](https://github.com/krakenfx/kraken-cli/releases)
[![downloads](https://img.shields.io/github/downloads/krakenfx/kraken-cli/total?color=blue)](https://github.com/krakenfx/kraken-cli/releases)
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey)](#installation)

Trade on Kraken from your terminal, or let your AI agent trade for you. One
install covers crypto, tokenized U.S. stocks and ETFs (for non-U.S. customers),
forex, and futures. Every command can answer in JSON. A built-in MCP server
connects the CLI to Claude, Cursor, Codex and other agents, and paper trading
runs on live prices with no account.

```bash
curl --proto '=https' --tlsv1.2 -LsSf https://github.com/krakenfx/kraken-cli/releases/latest/download/kraken-cli-installer.sh | sh
source "$HOME/.cargo/env"   # puts kraken on your PATH in this terminal
kraken ticker BTCUSD        # live price, no account needed
```

<!-- prettier-ignore -->
> [!TIP]
> **New: sign in with OAuth.** You no longer have to fumble around for API
> keys. `kraken auth login` opens Kraken in your browser, you approve, and the
> CLI saves a restricted Spot API key for you. The key can't withdraw funds,
> and it expires on its own. [See how it works](#sign-in-with-oauth).

With kraken-cli you can:

- Trade 1,400+ crypto pairs, 170+ tokenized U.S. stocks and ETFs (xStocks), 12
  forex pairs and 200+ futures contracts.
  [What you can trade](#what-you-can-trade)
- Practice on paper first. Paper orders fill at live prices and need no Kraken
  account, and the basic order commands are the same as live.
  [Paper trading](#paper-trading)
- Connect Claude, Cursor, Codex, Gemini and other MCP clients through
  `kraken-mcp`, which serves up to 152 MCP tools. On clients that support MCP
  elicitation, calls that move money ask you first; the `kraken` CLI itself
  places orders without a prompt. [MCP server](#mcp-server)
- Script it: every command takes `-o json`, and a failure comes back as JSON
  with a stable `error` field and a non-zero exit code.
  [For AI agents](#for-ai-agents)
- Record live market data and replay it into paper sessions, then score a
  strategy against pass criteria you fixed before the first run.
  [Workspaces, sessions, and research](#workspaces-sessions-and-research)
- Start from 59 agent skills for DCA, grid trading, rebalancing, futures risk
  and more. [Agent skills](#agent-skills)

| You are                      | Start here                                                                                                                                                                                                                                                                                                                    |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A person at a terminal       | [Install](#installation), then follow the [Quick start](#quick-start) from sign-in to your first order.                                                                                                                                                                                                                       |
| An AI agent, or building one | Read [For AI agents](#for-ai-agents) and [AGENTS.md](AGENTS.md). Ask your human to open a new terminal and run `kraken auth login` there, then call `kraken <command> -o json 2>/dev/null`. Orders trade real money with no confirmation prompt, so follow the [rules for trading real money](#rules-for-trading-real-money). |
| Just looking around          | Market data and paper trading need no account. Try steps 1 and 2 of the [Quick start](#quick-start).                                                                                                                                                                                                                          |

Paste one of these prompts into Claude Code, Codex, Cursor, or another AI coding
agent. No agent yet? Install [Claude Code](https://claude.com/claude-code)
first.

```text
Install kraken-cli (https://github.com/krakenfx/kraken-cli) and tell me how to sign in with OAuth.
```

```text
Install kraken-cli (https://github.com/krakenfx/kraken-cli) and build me a morning market brief.
```

```text
With kraken-cli, watch ETH, SOL, and BTC for 30 seconds. What are the pros and cons of buying each right now?
```

```text
With kraken-cli, look up AAPLx, TSLAx, and SPYx on xStocks. Summarize how each is performing today.
```

```text
You are a Wall Street veteran with 20 years of experience. You have 1 minute. Paper trade BTC with kraken-cli and show me your P&L.
```

```text
With kraken-cli futures paper trading, open a 10x leveraged long on BTC with $5,000 collateral. Set a trailing stop at 3%.
```

If kraken-cli is useful to you,
[star the repo](https://github.com/krakenfx/kraken-cli) so other traders and
agent builders can find it. To hear about new releases, choose **Watch >
Custom > Releases** on the repo page.

<!-- prettier-ignore -->
> [!CAUTION]
> Experimental software. It interacts with the live Kraken exchange and can
> execute real financial transactions. Read [DISCLAIMER.md](DISCLAIMER.md)
> before using it with real funds or AI agents.

## Contents

- [Installation](#installation)
- [Quick start](#quick-start)
- [Sign in with OAuth](#sign-in-with-oauth)
- [API keys & configuration](#api-keys--configuration)
- [What you can trade](#what-you-can-trade)
- [Paper trading](#paper-trading)
- [For AI agents](#for-ai-agents)
- [Output and errors](#output-and-errors)
- [MCP server](#mcp-server)
- [Workspaces, sessions, and research](#workspaces-sessions-and-research)
- [Commands](#commands)
- [Examples](#examples)
- [Agent skills](#agent-skills)
- [Troubleshooting](#troubleshooting)
- [Star history](#star-history)
- [Development](#development)
- [Contributing](#contributing)
- [License & disclaimer](#license--disclaimer)

## Installation

One install, no runtime dependencies. It puts three binaries on your PATH:
`kraken`, `kraken-mcp` (the MCP server) and `kraken-shell` (an interactive
shell).

### One-liner

```bash
curl --proto '=https' --tlsv1.2 -LsSf https://github.com/krakenfx/kraken-cli/releases/latest/download/kraken-cli-installer.sh | sh
```

The installer detects your OS and architecture, downloads the right build, and
installs it. macOS (Apple Silicon and Intel) and Linux (x86_64 and ARM64) are
supported. On Windows, use WSL. AI agents: ask your human before you run the
installer on their machine.

Open a new terminal (or run `source "$HOME/.cargo/env"`), then check that it
works:

```bash
kraken status && kraken ticker BTCUSD
```

<!-- prettier-ignore -->
> [!NOTE]
> `command not found: kraken` right after install? The installer puts the
> binaries in `~/.cargo/bin` (or `$CARGO_HOME/bin` if you set it) and adds that
> folder to your PATH for new terminals only.
>
> - AI agent in the middle of a task: call `~/.cargo/bin/kraken` (or
>   `$CARGO_HOME/bin/kraken`) by its full path for the rest of the session.
> - Terminal: open a new window, or run `source "$HOME/.cargo/env"`
>   (`$CARGO_HOME/env` if you set it, `env.fish` for fish).
> - Claude Code, Codex, or another agent you start in a terminal: quit it, open
>   a new terminal window, and start it there. The old window keeps the old
>   PATH.
> - Cursor, VS Code, Claude Desktop, or another desktop app: quit it and open
>   it again. If it still can't find `kraken`, use the full path that
>   `command -v kraken` prints in a new terminal.

Pre-built binaries are also on the
[GitHub Releases](https://github.com/krakenfx/kraken-cli/releases) page.

### Verifying binaries

Releases are signed with [minisign](https://jedisct1.github.io/minisign/). Every
release archive, its `.sha256` file, the installer script and `SHA256SUMS.txt`
on the [Releases](https://github.com/krakenfx/kraken-cli/releases) page has a
matching `.minisig` signature file.

Download the archive and its `.minisig` into the same folder, then check it
against the public key:

```bash
minisign -Vm kraken-cli-aarch64-apple-darwin.tar.gz -P RWQJue8SwPzZBZO8Up5ppAUqm0wM/gK5yjnam+Dbf7KbY0utkiO+7XCd
```

Public key:

```text
RWQJue8SwPzZBZO8Up5ppAUqm0wM/gK5yjnam+Dbf7KbY0utkiO+7XCd
```

Install minisign with `brew install minisign` (macOS) or `apt install minisign`
(Linux). To check the installer before you run it:

```bash
curl -LO https://github.com/krakenfx/kraken-cli/releases/latest/download/kraken-cli-installer.sh
curl -LO https://github.com/krakenfx/kraken-cli/releases/latest/download/kraken-cli-installer.sh.minisig
minisign -Vm kraken-cli-installer.sh -P RWQJue8SwPzZBZO8Up5ppAUqm0wM/gK5yjnam+Dbf7KbY0utkiO+7XCd && sh kraken-cli-installer.sh
```

<details>
<summary>Build from source</summary>

Requires [Rust](https://rustup.rs/) 1.97 or later. If cargo says a newer rustc
is required, run `rustup update`. A clone pins its toolchain in
`rust-toolchain.toml`, so rustup may download that version on the first build.

A source build is DuckDB-free by default, because the bundled DuckDB C++ build
dominates compile time and only DuckDB tapes need it: writing one
(`kraken record --to duckdb`) or reading one, such as a 0.4.x tape. Pass
`--features record-duckdb` to any command below to include it; the released
binaries already carry it.

Both commands install all three binaries: `kraken`, `kraken-mcp` and
`kraken-shell`.

```bash
cargo install --locked --git https://github.com/krakenfx/kraken-cli kraken-cli
```

Or clone and build:

```bash
git clone https://github.com/krakenfx/kraken-cli.git
cd kraken-cli
cargo install --locked --path crates/kraken-cli
```

If an earlier source install added `kraken-mcp` or `kraken-shell`, cargo stops
with "binary already exists". Run `cargo uninstall kraken-mcp kraken-shell`
first, or add `--force`.

</details>

## Quick start

Steps 1 and 2 need no account. To trade real money you need a verified Kraken
account with funds in it; you can
[create one on kraken.com](https://www.kraken.com/sign-up).

### 1. Look at the market

Public market data needs no credentials, so nothing here can touch an account.

```bash
kraken ticker BTCUSD
kraken orderbook BTCUSD --count 10
kraken ohlc BTCUSD --interval 60
```

Output is a table. Add `-o json` to any command for JSON. REST commands accept
`BTCUSD`, `BTC/USD` or `XBTUSD`; the examples for streaming commands (`ws`,
`record`, `session`) use `BTC/USD`.

### 2. Practice with paper trading

```bash
kraken workspace create sandbox --capital 10000 --mode paper
export KRAKEN_WORKSPACE=sandbox
kraken paper buy BTCUSD 0.01
kraken workspace status
unset KRAKEN_WORKSPACE
```

Paper orders fill at live prices with simulated money. `paper buy` may log a
warning that no session is recording; you can ignore it here.

While `KRAKEN_WORKSPACE` names a paper workspace, `kraken order buy` and
`kraken balance` act on the simulated account as well. The last line unsets it
so the next steps reach your real account. [Paper trading](#paper-trading)
covers the rest.

### 3. Sign in

```bash
kraken auth login
kraken auth test
```

`kraken auth login` opens Kraken's sign-in page in your browser. Sign in,
approve access, and the CLI saves a Spot API key for you. The key covers spot
crypto, xStocks and forex, can't withdraw funds, and expires after 90 days. Run
it yourself in an interactive terminal: it refuses to run from a script, a CI
job or an AI agent's shell. `kraken auth test` checks the saved key against your
account. [Sign in with OAuth](#sign-in-with-oauth) covers each step.

- Trading futures? The sign-in key is Spot only. Create a Futures key and set
  `KRAKEN_FUTURES_API_KEY` and `KRAKEN_FUTURES_API_SECRET`, or add it to
  `config.toml` (see [API keys & configuration](#api-keys--configuration)).
- Prefer a key you created yourself? Run `kraken setup` in a terminal, or store
  it with [`kraken auth set`](#store-a-key-you-created).
- Using an AI agent? Sign in in your own terminal, and the agent uses the stored
  key. Never paste an API key into an AI chat.

### 4. Check your account

```bash
kraken balance
kraken open-orders
```

Balance empty? Fund the account on kraken.com, or list your deposit options with
`kraken deposit methods USD`.

### 5. Preview an order

```bash
kraken ticker BTCUSD                                                # check the price
kraken order buy BTCUSD 20 --type market --oflags viqc --validate  # $20 of BTC, checked only
```

`--validate` asks Kraken to check the order without placing it, so nothing
trades. `--oflags viqc` makes the volume a quote-currency amount, here 20 USD.
Leave the flag off and `20` means 20 BTC. Kraken accepts `viqc` on market buys
only. For a limit order, give the volume in BTC and a price:

```bash
kraken order buy BTCUSD 0.0005 --type limit --price 75000 --validate
```

`kraken order buy` defaults to `--type limit`, which needs `--price`. To see the
smallest order a pair accepts, run `kraken pairs --pair BTCUSD -o json` and read
`ordermin` (volume) and `costmin` (cost in the quote currency).

### 6. Place your first order

Drop `--validate`. This places a real order with real money, and there is no
confirmation prompt: it goes to Kraken when you press Enter. Check that
`echo $KRAKEN_WORKSPACE` prints nothing first, so the order reaches your real
account:

```bash
kraken order buy BTCUSD 20 --type market --oflags viqc
```

The receipt starts with `Mode  [LIVE] Real Money` and shows the order ID, which
is Kraken's transaction ID. With `-o json`, check that `mode` is `"live"` and
read `order_id`. Then check it:

```bash
kraken query-orders <ORDER_ID>     # status "closed" means it filled
kraken balance
```

A limit order that hasn't filled stays open; cancel it with
`kraken order cancel <ORDER_ID>`.

Futures orders use `kraken futures order buy` and `sell` with your Futures key.
They have no `--validate`, so rehearse them with
[futures paper trading](#futures-paper-trading) first. Sizes are in contracts:
one `PF_XBTUSD` contract is 1 BTC.

## Sign in with OAuth

`kraken auth login` signs you in with OAuth. You approve access on Kraken's own
sign-in page, and the CLI creates and saves a restricted Spot API key for you.
You skip the API settings page and the copy and paste.

```bash
kraken auth login
```

### What the key can do

- It can query balances, place, amend and cancel orders, read trades and ledger
  entries, use deposits and Earn, request exports, and open authenticated
  WebSocket streams.
- It has no withdrawal rights.
- It covers Spot only: spot crypto, xStocks and forex. Futures commands still
  use their own key (see [API keys & configuration](#api-keys--configuration)).
- It expires after 90 days. `--valid-for` sets a shorter life, from 1 minute up
  to 90 days.

| Option                   | What it does                                                                                          |
| ------------------------ | ----------------------------------------------------------------------------------------------------- |
| `--read-only`            | Creates a key that can read balances, orders, trades, and ledger entries, but cannot trade.           |
| `--valid-for <DURATION>` | Sets how long the key stays valid, for example `30d` or `12h`. The default and the maximum are `90d`. |
| `--no-browser`           | Prints the sign-in URL without opening a browser.                                                     |

```bash
kraken auth login --read-only --valid-for 30d
```

You have 5 minutes to approve in the browser. After that the command stops with
a `timeout` error, and you run it again.

<details>
<summary>What happens when you sign in</summary>

1. You run `kraken auth login` in a terminal. It refuses to run without one.
2. The CLI starts a listener on your own machine, on the first free port from
   27461 to 27463, and opens Kraken's sign-in page in your browser. If all three
   ports are busy, sign-in fails.
3. You sign in on Kraken and approve access.
4. Kraken sends your browser back to `http://localhost:<port>/callback` with a
   one-time code.
5. The CLI exchanges the code for permission to create a key. This is a standard
   OAuth authorization-code flow with PKCE (S256). The CLI is a public OAuth
   client, so there is no client secret.
6. The CLI creates a restricted Spot API key and saves it to `config.toml`,
   which is created with `0600` permissions.
7. If you already had a sign-in key, the new one replaces it and the CLI deletes
   the old one. Anything still signing with the old key stops working. If the
   delete fails, the old key stays on your account until it expires.

</details>

### Signing in over SSH

Forward the three callback ports, then ask the CLI to print the sign-in URL and
open it on your own machine. The listener takes the first free port of the
three, so forward all of them.

```bash
# On your own machine: connect with the callback ports forwarded.
ssh -L 27461:localhost:27461 -L 27462:localhost:27462 -L 27463:localhost:27463 <host>

# On the remote machine: print the sign-in URL, then open it on your own machine.
kraken auth login --no-browser
```

### Checking, switching, and removing keys

```bash
kraken auth show              # which key is in use, and whether a flag or env var overrides it (alias: auth status)
kraken auth test              # checks the key in use against your account
kraken auth switch sign-in    # signs requests with the OAuth sign-in key
kraken auth switch api-key    # signs requests with the key from `kraken auth set` or `kraken setup`
kraken auth reset             # deletes every stored key from config.toml; revokes nothing on Kraken
```

Your config can hold a sign-in key and an API key at the same time.
[Credential resolution](#credential-resolution) explains which one signs.

`auth reset` deletes every stored key from `config.toml`: the API key, the
sign-in key, and the Futures key. It revokes nothing on Kraken, so the sign-in
key keeps working until it expires. To revoke it at once, delete it where you
manage API keys on kraken.com. An older release ignores the sign-in key and can
drop it from `config.toml`, so delete the key in the Kraken UI before you
downgrade.

### Using OAuth with AI agents

OAuth sign-in is for a person at a terminal. `kraken auth login` refuses to run
without one, the catalog marks it `dangerous`, and the MCP server does not serve
it. An agent can't start it and should never try.

A person signs in once, and the agent reuses the key:

1. A person runs `kraken auth login` once, in their own terminal.
2. The agent calls commands as usual, for example
   `kraken balance -o json 2>/dev/null`. The CLI signs with the stored OAuth
   key.
3. A key from a flag or an environment variable wins over the stored key.
4. When the sign-in key expires, calls that need a key return an `auth` error
   envelope. The CLI does not fall back to another stored key. Tell the person
   to run `kraken auth login` again.

## API keys & configuration

Authenticated commands (trading, balances, order management) need a Kraken API
key pair. Public market data and paper trading work without credentials.

The easiest way to get a key is [OAuth sign-in](#sign-in-with-oauth). Create one
by hand when you need a Futures key, specific permissions, or credentials for
automation.

### Getting API keys

**Spot** (covers trading, balances, funding, earn, subaccounts): **Settings >
API** on kraken.com. Step-by-step guide:
[How to create a spot API key](https://support.kraken.com/articles/360000919966-how-to-create-an-api-key).

**Futures** (only for `kraken futures` commands):
[sign in to Kraken Futures](https://www.kraken.com/login-futures), then go to
**Settings > Create Key**. Full guide:
[How to create a Futures API key](https://support.kraken.com/hc/en-us/articles/360022839451-How-to-create-an-API-key-for-Kraken-Futures).

Grant the minimum permissions your workflow needs:

- Read-only monitoring: "Query Funds" and "Query Open Orders & Trades" cover
  balances and open orders. Add "Query Closed Orders & Trades" for trade history
  and "Query Ledger Entries" for ledgers.
- Trading: add the permissions to create, modify, cancel and close orders.
- Leave withdrawal permission off unless a script needs to withdraw.

### Store a key you created

`kraken setup` is an interactive wizard. It asks for your Spot key and,
optionally, a Futures key. Run it in a normal terminal, because it reads your
input.

`kraken auth set` stores a key without asking you to type it. It always needs a
Spot key and its secret. Pass the secret on stdin or from a file so it stays out
of your shell history and process list, and add the Futures flags to store a
Futures key in the same call:

```bash
kraken auth set --api-key <YOUR_KEY> --api-secret-stdin
kraken auth set --api-key <YOUR_KEY> --api-secret-file ~/kraken-secret.txt \
  --futures-api-key <FUTURES_KEY> --futures-api-secret-file ~/kraken-futures-secret.txt
```

Delete the secret files once the keys are stored. `kraken setup` and
`kraken auth set` write the same API key slot. If a working sign-in key is
already active, the CLI asks which key to use in a terminal and keeps the active
key in a script. To add only a Futures key and keep your sign-in key, use the
Futures environment variables or the `config.toml` fields below.

### Environment variables (recommended for agents and automation)

```bash
export KRAKEN_API_KEY="your-key"
export KRAKEN_API_SECRET="your-secret"
export KRAKEN_FUTURES_API_KEY="your-futures-key"       # optional
export KRAKEN_FUTURES_API_SECRET="your-futures-secret"  # optional
```

Set them in the environment that the agent or script starts from. A secrets
manager keeps the secret out of your shell history, for example
`export KRAKEN_API_SECRET="$(op read 'op://Private/Kraken/secret')"` with the
1Password CLI. An agent that is already running won't see variables you export
afterwards. Never paste API keys into an AI chat.

### Config file

Credentials live in `~/.config/kraken/config.toml` (Linux) or
`~/Library/Application Support/kraken/config.toml` (macOS):

```toml
[auth]
api_key = "your-api-key"
api_secret = "your-api-secret"
futures_api_key = "your-futures-key"         # optional
futures_api_secret = "your-futures-secret"   # optional
```

### Credential resolution

Highest precedence first:

1. Command-line flags (`--api-key`, `--api-secret`). Spot and Futures commands
   share this pair.
2. Environment variables: `KRAKEN_API_KEY` and `KRAKEN_API_SECRET` for Spot,
   `KRAKEN_FUTURES_API_KEY` and `KRAKEN_FUTURES_API_SECRET` for Futures.
3. The stored key in `config.toml`. For Spot that is the active one of the API
   key (from `kraken auth set` or `kraken setup`) and the OAuth sign-in key
   (from `kraken auth login`).

Which stored Spot key is active:

| Situation                                                            | Active key                                                          |
| -------------------------------------------------------------------- | ------------------------------------------------------------------- |
| Only one key is stored                                               | That key                                                            |
| Both are stored and you never chose                                  | The API key                                                         |
| You store a new key while another key is active and working          | In a terminal the CLI asks you; in a script it keeps the active key |
| The active key has expired or is missing when you store a new one    | The new key, without a prompt                                       |
| You run `kraken auth switch api-key` or `kraken auth switch sign-in` | The key you chose                                                   |

The CLI changes the active key only when you choose one, or when you store a new
key while the active one is expired or missing. It never falls back to the other
key: an expired sign-in key stays active and fails with an `auth` error until
you sign in again or run `kraken auth switch api-key`. `kraken auth show` tells
you which key is in use.

### Security

- The config file is created with `0600` permissions (owner read/write only).
- Secrets are never logged, printed, or included in error messages.
- Use `--api-secret-stdin` or `--api-secret-file` instead of `--api-secret` to
  keep secrets out of process listings.
- For automation, prefer environment variables over command-line flags.

<details>
<summary>Advanced: API endpoint overrides</summary>

| Variable                   | Default                                         | Description                           |
| -------------------------- | ----------------------------------------------- | ------------------------------------- |
| `KRAKEN_SPOT_URL`          | `https://api.kraken.com`                        | Spot REST API base URL                |
| `KRAKEN_FUTURES_URL`       | `https://futures.kraken.com/derivatives/api/v3` | Futures REST API base URL             |
| `KRAKEN_WS_PUBLIC_URL`     | `wss://ws.kraken.com/v2`                        | Public WebSocket endpoint             |
| `KRAKEN_WS_AUTH_URL`       | `wss://ws-auth.kraken.com/v2`                   | Authenticated Spot WebSocket endpoint |
| `KRAKEN_WS_L3_URL`         | `wss://ws-l3.kraken.com/v2`                     | Level 3 order book WebSocket endpoint |
| `KRAKEN_FUTURES_WS_URL`    | `wss://futures.kraken.com/ws/v1`                | Futures WebSocket endpoint            |
| `KRAKEN_FEEDBACK_ENDPOINT` | `https://cli-feedback.kraken.com/v1/feedback`   | Product feedback ingest URL           |

Resolution: CLI flag (`--api-url`, `--futures-url`, `--ws-public-url`,
`--ws-auth-url`, `--ws-l3-url`, `--ws-futures-url`) > environment variable >
default. `KRAKEN_FEEDBACK_ENDPOINT` has no flag. Every override must use
`https://` or `wss://` and point at a Kraken host.
`KRAKEN_DANGER_ALLOW_ANY_URL_HOST=1` (`--danger-allow-any-url-host`) lifts the
host check, and for `KRAKEN_FEEDBACK_ENDPOINT` it also allows `http://`. Use it
for local testing only.

</details>

## What you can trade

Spot crypto, xStocks and forex share `kraken order` (add
`--asset-class tokenized_asset` for xStocks; forex pairs such as `EURUSD` need
no asset class to trade). Futures use `kraken futures order` with a separate
Futures API key, and Earn has its own `kraken earn` commands. The spot and
xStocks examples below use `--validate`, so Kraken checks them without placing
them.

| Asset class                                                                  | Instruments                                                                                                                                      | Margin                                                                       | Commands                                     | Example                                                                                            |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- | -------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **Crypto spot**                                                              | 1,400+ pairs (BTC, ETH, SOL, and hundreds more)                                                                                                  | Up to 10x on major pairs                                                     | `kraken order`                               | `kraken order buy BTCUSD 0.001 --type limit --price 50000 --validate`                              |
| **Tokenized U.S. stocks & ETFs ([xStocks](https://www.kraken.com/xstocks))** | 170+ xStocks: AAPL, NVDA, TSLA, GOOGL, AMZN, MSFT, SPY, QQQ, and more                                                                            | Up to 3x on select xStocks                                                   | `kraken order --asset-class tokenized_asset` | `kraken order buy AAPLx/USD 0.1 --type limit --price 200 --asset-class tokenized_asset --validate` |
| **Forex**                                                                    | 12 fiat pairs: EUR/USD, GBP/USD, USD/JPY, AUD/USD, and more                                                                                      | None                                                                         | `kraken order`                               | `kraken ticker EURUSD --asset-class forex`                                                         |
| **Perpetual futures**                                                        | 200+ contracts: crypto, 3 forex perps (EUR, GBP, CHF), stock, ETF and index perps (AAPL, NVDA, TSLA, SPY, QQQ, US 100), commodities, and pre-IPO | Up to 100x (BTC, ETH, SOL); 10x to 50x on most others; lower in some regions | `kraken futures order`                       | `kraken futures ticker PF_XBTUSD`                                                                  |
| **Inverse & fixed-date futures**                                             | 22 contracts on BTC, ETH, SOL, LTC, XRP: inverse perpetuals (`PI_`), inverse fixed-date (`FI_`), and fixed-date (`FF_`)                          | Varies                                                                       | `kraken futures order`                       | `kraken futures instruments`                                                                       |
| **Earn / staking**                                                           | Flexible, bonded, timed and instant strategies across multiple assets                                                                            | n/a                                                                          | `kraken earn`                                | `kraken earn strategies --asset ETH`                                                               |

Futures sizes are in contracts: one `PF_XBTUSD` contract is 1 BTC, and `FI_`
contracts are 1 USD each. Fixed-date symbols end in their expiry date
(`YYMMDD`). `kraken futures instruments` lists the contracts that are trading
now. Futures orders have no `--validate`, so rehearse them with
[futures paper trading](#futures-paper-trading).

_xStocks are not available in the USA. Availability for all products varies by
jurisdiction._

## Paper trading

Paper trading tests trading logic against live Kraken prices with simulated
money. It needs no API key and no Kraken account. Spot and futures each have
their own paper engine.

### Spot paper trading

There are two ways to place a spot paper order:

- `kraken paper buy` and `kraken paper sell` always simulate.
- Inside a paper workspace (`KRAKEN_WORKSPACE` or `--workspace`), the live verbs
  `kraken order buy`, `balance`, `open-orders` and `trades-history` act on the
  simulated account too. A strategy that sticks to these verbs, with `--type`
  and `--price`, runs unchanged once you promote it to live (see Strategy
  workspaces in the [full command reference](#commands)). Inside a workspace,
  `order buy` and `sell` refuse `--cl-ord-id`, `--oflags` and most other
  advanced flags.

`paper buy` defaults to a market order and `order buy` to a limit order, so pass
`--type` when you switch. Paper supports `market` and `limit` orders, a
configurable flat slippage model, and no partial fills.

**Agent pattern:**

```bash
kraken workspace create sandbox --capital 10000 --mode paper -o json
export KRAKEN_WORKSPACE=sandbox
kraken paper buy BTCUSD 0.01 -o json
kraken paper sell BTCUSD 0.005 --type limit --price 90000 -o json
kraken workspace status -o json
kraken workspace reset --yes -o json   # dangerous: only when your human asks for a reset
unset KRAKEN_WORKSPACE
```

**Human pattern:**

```bash
kraken workspace create sandbox-eur --capital 5000 --currency EUR --mode paper
export KRAKEN_WORKSPACE=sandbox-eur
kraken paper buy BTCEUR 0.01
kraken paper balance
kraken paper status
kraken paper orders
kraken paper history
kraken workspace reset
unset KRAKEN_WORKSPACE
```

| Command                                                                                               | Description                                                                                                                                  |
| ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `kraken paper init [NAME] [--capital 10000] [--currency USD] [--fee-rate 0.0026] [--slippage-rate 0]` | Older shortcut for `workspace create --mode paper`. With no workspace selected it creates one named `global`                                 |
| `kraken paper reset [NAME] [--capital N] [--currency C] [--fee-rate R] [--slippage-rate S] [--yes]`   | Shortcut for `workspace reset`: starts a new capital epoch. Open orders are dropped unfilled; `paper orders` and `paper history` start empty |
| `kraken paper balance`                                                                                | All balances (total, reserved, available)                                                                                                    |
| `kraken paper buy <PAIR> <VOL> [--type limit --price P]`                                              | Paper buy (market or limit)                                                                                                                  |
| `kraken paper sell <PAIR> <VOL> [--type limit --price P]`                                             | Paper sell (market or limit)                                                                                                                 |
| `kraken paper orders`                                                                                 | Open limit orders                                                                                                                            |
| `kraken paper cancel <ORDER_ID>`                                                                      | Cancel a limit order                                                                                                                         |
| `kraken paper cancel-all`                                                                             | Cancel all limit orders                                                                                                                      |
| `kraken paper history`                                                                                | Filled trade history                                                                                                                         |
| `kraken paper status`                                                                                 | Portfolio value, unrealized P&L, trade count                                                                                                 |

Prices come from the public Kraken Ticker API (no auth needed). By default a
0.26% taker fee applies to every fill; set another rate with `--fee-rate`.
Optional slippage simulation applies a flat rate to market orders: buys fill at
`ask * (1 + slippage_rate)`, sells at `bid * (1 - slippage_rate)`. Default
slippage is 0.0 (no simulation). A limit order always rests when placed, even
when the market is already through its price. The next `paper buy`, `sell`,
`orders`, `cancel`, `cancel-all`, `history` or `status` checks it against the
live price, and once the market has crossed the limit it fills at the limit
price, not at the better market price.

In table mode, `paper buy`, `sell`, `cancel`, `cancel-all` and `status` lead
with a `[PAPER] Simulated Trading` row, and `paper orders` and `history` put
`[PAPER]` in their first column header. Their JSON carries `"mode": "paper"`, as
does the JSON of `paper balance` and `paper init`. `paper init` shows a plain
`Mode` row; the `paper balance` table and all `paper reset` output carry no
marker.

### Futures paper trading

Near-parity with live `kraken futures order` commands. Supports all 8 order
types (market, limit, post, stop, take-profit, ioc, trailing-stop, fok),
leverage and margin tracking, position aggregation/netting, liquidation
simulation, and funding rate accrual. `--type` defaults to `limit`, and the fee
rate to 0.05% (`--fee-rate 0.0005`). Known differences: `order-status` accepts a
single ID (live accepts multiple), post-only orders are cancelled rather than
simulating maker queue priority, and fills use the bid/ask snapshot with no
depth-based slippage. Only IOC orders fill partially: they take the book depth
available at the limit price and cancel the rest.

The live commands differ in more than the prefix. `futures paper buy`/`sell`
become `futures order buy`/`sell`, which take no `--leverage` (set it with
`futures set-leverage`), and `futures paper orders` becomes
`futures open-orders`. `edit-order`, `cancel`, `cancel-all`, `batch-order`,
`order-status`, `positions`, `fills`, `leverage` and `set-leverage` keep their
names under `futures`. `init`, `reset`, `balance` and `status` are paper-only;
`futures accounts` shows the live wallet. Live `futures history` is public trade
history; your own past orders and fills are in `futures history-orders` and
`futures history-executions`.

Futures paper state is global, not per workspace. Run it with no workspace
selected (`unset KRAKEN_WORKSPACE` if an earlier example exported it): inside a
workspace only `balance`, `status`, `orders`, `order-status`, `positions` and
`fills` run; `history`, `leverage` and every mutation are refused.

Successful JSON responses include `"mode": "futures_paper"`. Most table views
are labeled `[FUTURES PAPER]` or `[FP]`.

**Agent pattern:**

```bash
kraken futures paper init --balance 10000 -o json
kraken futures paper buy PF_XBTUSD 1 --leverage 10 --type market -o json
kraken futures paper sell PF_ETHUSD 5 --leverage 20 --type market -o json
kraken futures paper positions -o json
kraken futures paper status -o json
kraken futures paper reset -o json
```

**Human pattern:**

```bash
kraken futures paper init --balance 10000 --currency USD
kraken futures paper buy PF_XBTUSD 1 --leverage 10 --type market
kraken futures paper sell PF_XBTUSD 1 --leverage 10 --type limit --price 70000
kraken futures paper positions
kraken futures paper balance
kraken futures paper fills
kraken futures paper history
kraken futures paper reset
```

| Command                                                                                    | Description                                                    |
| ------------------------------------------------------------------------------------------ | -------------------------------------------------------------- |
| `kraken futures paper init [--balance B] [--currency C] [--fee-rate R]`                    | Initialize futures paper account                               |
| `kraken futures paper reset [--balance B] [--currency C] [--fee-rate R]`                   | Reset account (clear positions, orders, fills)                 |
| `kraken futures paper balance`                                                             | Collateral, used margin, available margin, unrealized P&L      |
| `kraken futures paper status`                                                              | Equity, P&L since start, unrealized P&L, position/order counts |
| `kraken futures paper buy <SYM> <SIZE> [--leverage L] [--type TYPE] ...`                   | Paper long (all 8 order types)                                 |
| `kraken futures paper sell <SYM> <SIZE> [--leverage L] [--type TYPE] ...`                  | Paper short (all 8 order types)                                |
| `kraken futures paper orders`                                                              | Open resting orders                                            |
| `kraken futures paper order-status <ID>`                                                   | Query specific order                                           |
| `kraken futures paper edit-order --order-id <ID> [--size S] [--price P] [--stop-price SP]` | Edit a resting order                                           |
| `kraken futures paper cancel --order-id <ID>`                                              | Cancel order (also supports `--cli-ord-id`)                    |
| `kraken futures paper cancel-all [--symbol SYM]`                                           | Cancel all (optional symbol filter)                            |
| `kraken futures paper batch-order '<JSON>'`                                                | Batch order placement                                          |
| `kraken futures paper positions`                                                           | Open positions with mark price, liquidation, P&L               |
| `kraken futures paper fills`                                                               | Fill history                                                   |
| `kraken futures paper history`                                                             | Closed positions and cancelled orders                          |
| `kraken futures paper leverage [--symbol SYM]`                                             | Current leverage preferences                                   |
| `kraken futures paper set-leverage <SYM> <LEV>`                                            | Set default leverage per symbol                                |

`futures paper buy` and `sell` also take `--stop-price`,
`--trigger-signal mark|index|last`, `--client-order-id`, `--reduce-only`,
`--trailing-stop-max-deviation` and
`--trailing-stop-deviation-unit percent|quote_currency`, the same as the live
order commands.

Prices come from the public Kraken Futures Ticker API (no auth needed). Taker
fees are simulated. Positions track leverage, margin, and liquidation prices.
Funding rates are accrued based on the public funding rate API. Spot paper and
futures paper are fully independent: resetting one does not affect the other.

## For AI agents

If you're an AI agent or building one, read [AGENTS.md](AGENTS.md) first: it is
the full integration contract. [CONTEXT.md](CONTEXT.md) is a shorter version for
tool-use prompts.

| Resource                                               | Description                                                           |
| ------------------------------------------------------ | --------------------------------------------------------------------- |
| [AGENTS.md](AGENTS.md)                                 | Full integration guide: auth, invocation, errors, rate limits         |
| [CONTEXT.md](CONTEXT.md)                               | Runtime context for tool-using agents                                 |
| [agents/tool-catalog.json](agents/tool-catalog.json)   | 188 commands with generated argument schemas, types, and safety flags |
| [agents/error-catalog.json](agents/error-catalog.json) | 10 error categories with retry guidance                               |
| [skills/](skills/)                                     | Goal-oriented SKILL.md workflow packages                              |
| [CLAUDE.md](CLAUDE.md)                                 | Claude-specific integration guidance                                  |

### Authenticating as an agent

- A person is with you: ask them to open a new terminal window and run
  `kraken auth login` there. Never start it yourself. It needs an interactive
  terminal, and the catalog marks it `dangerous`. Then confirm with
  `kraken auth test -o json` (exit code 0 means the key works) and run
  `kraken auth show -o json`: `active_spot_source` names the key that signs,
  `overridden` is `true` when a flag or environment variable wins over the
  stored key, and `sign_in_key` carries `valid_until` and `expired`. See
  [Using OAuth with AI agents](#using-oauth-with-ai-agents).
- Running unattended (CI, a server): the operator sets `KRAKEN_API_KEY` and
  `KRAKEN_API_SECRET` in the environment the agent starts from. Flags and
  environment variables take priority over stored keys.
- Never ask for, accept, or paste API keys in a chat.

### Invocation

```bash
kraken <command> [args...] -o json 2>/dev/null
```

- stdout carries one JSON document on success, or a JSON error envelope on
  failure. Streaming commands such as `kraken ws ticker` write JSONL: one JSON
  object per line.
- Exit code 0 means success, 1 a runtime or API failure, and 2 a usage error
  such as a bad flag or a missing argument.
- stderr carries diagnostics only: structured JSON logs (warnings and errors by
  default, more with `-v` or `RUST_LOG`). Real-account orders and cancels, and
  commands in a live workspace, also print a plain-text `live:` banner there
  (not for `--validate` orders). Never parse stderr for data; read the `mode`
  field in the JSON to tell paper from live. For orders, capture stderr to a
  file instead of discarding it, so you can show your human any banner or
  warning.

### Rules for trading real money

1. The CLI places orders without a confirmation prompt. Before any command the
   catalog marks `dangerous`, confirm the pair, side, size and estimated cost
   with your human.
2. Run the order with `--validate` first. A validated order places nothing, so
   on the CLI it needs no approval (over MCP it is gated like the real order);
   confirm with your human between the validation and the real order.
3. Check where it goes. `KRAKEN_WORKSPACE` or `--workspace` decides, and the
   receipt's `mode` field says `paper` or `live`.
4. Give every order a new `--cl-ord-id`, such as a fresh UUID, and never reuse
   one. After a `network` error or an envelope with `"verify_first": true`, look
   the order up with `kraken open-orders --cl-ord-id <ID> -o json` and then
   `closed-orders` before you resubmit. For futures orders, withdrawals,
   transfers and Earn, use the lookups in the `network` row of the
   [error table](#error-envelopes). (Inside a workspace, `order buy` and `sell`
   refuse `--cl-ord-id` and most other advanced flags.)
5. Over MCP, set `acknowledged=true` only after your human approved that exact
   call.
6. Call `feedback` only when your human asks, and never put secrets or personal
   data in it.

### Reading results

- `balance` is keyed by asset code (`BTC`, `USD`, `ETH`), and on the real
  account its values are JSON numbers. Outside a workspace the result has no
  `mode` field, so confirm that `KRAKEN_WORKSPACE` is unset and no `--workspace`
  flag is passed before you call it real money. Inside a workspace it returns
  `{"workspace": ..., "mode": ..., "balances": {"USD": {"total", "reserved", "available"}}}`
  instead.
- Market data is keyed by the pair name Kraken returns: `XXBTZUSD` when you ask
  for `BTCUSD`, `BTC/USD` when you ask for `BTC/USD`. Read it with `.[]`.
- An order receipt carries `mode`, `status` and `order_id` (Kraken's transaction
  ID). `kraken query-orders <ID> -o json` returns an object keyed by order ID,
  so read it with `.[]`. Each order carries `status` (`open`, `closed`,
  `canceled`, ...), `volume`, `volume_executed`, `cost`, `fee`, and `price` (the
  average fill price).
- Workspace amounts are decimal strings, unlike the real-account `balance`
  values: `backing`, and the `total`, `reserved` and `available` of a workspace
  `balance`. Convert them with `tonumber` in jq before you compare them.

To buy a dollar amount, make the volume a quote-currency amount with
`--oflags viqc` (market buys only):

```bash
kraken order buy BTCUSD 25 --type market --oflags viqc --validate -o json 2>/dev/null
# after your human confirms; use a new client order ID for every order:
CLID=$(uuidgen | tr 'A-Z' 'a-z')
kraken order buy BTCUSD 25 --type market --oflags viqc --cl-ord-id "$CLID" -o json 2>>kraken-order.log
kraken query-orders <ORDER_ID> -o json 2>/dev/null
```

<details>
<summary>Why agent-first?</summary>

Most CLIs are built for humans at a terminal. This one is built for LLM-based
agents, MCP tool servers, and automated pipelines that need to call Kraken
reliably without custom API clients.

- Structured output on request. Every command supports `-o json` (the default is
  a table), so agents don't scrape screens or run regex over table borders.
- Consistent error envelopes. Errors are JSON objects with a stable `error`
  field (`auth`, `rate_limit`, `validation`, `api`, `network`, and more). Agents
  route on `error` without parsing human sentences.
- Predictable exit codes: 0 for success, 1 for a runtime failure, 2 for a usage
  error. Combined with JSON errors on stdout, agents detect and classify
  failures programmatically.
- Paper trading for safe iteration. Test strategies against live prices with
  `kraken paper` (spot) and `kraken futures paper` (perpetual futures) commands.
  Paper trading needs no API keys and no real money, and it uses the same basic
  order commands as live trading.
- Market memory. `kraken record` captures live streams into a local DuckDB/JSONL
  tape library with integrity counters; finalized tapes replay into paper
  sessions and feed the autoresearch lab.
- Full API surface. The catalog lists all 188 commands, covering Spot, Futures,
  xStocks, Forex, Funding, Earn, Subaccounts, and paper trading.
  `kraken-mcp -s all` serves 152 MCP tools; the default services (market,
  account, paper, workspace, feedback) serve the subset in their groups. Streams
  (Spot and Futures WebSocket, recording, replay, session start, playground,
  recipe run, the stream daemon), interactive commands, and the local credential
  commands `auth switch` and `auth reset` stay CLI-only; each catalog entry's
  `reach` field says which.
- Built-in MCP server. Native Model Context Protocol support over stdio, with no
  subprocess wrapper.
- Rate-limit aware. No client-side throttling. When the Kraken API rejects a
  request due to rate limits, the CLI returns an enriched error with
  `suggestion`, `retryable`, and `docs_url` fields so agents can read the
  documentation and adapt their strategy.

Humans benefit from the same design: `--output table` renders clean tables,
`kraken-shell` provides a REPL, and `kraken setup` walks through configuration.

</details>

## Output and errors

### JSON (`-o json`)

Every request/response command returns one JSON document on stdout.

```bash
kraken ticker BTCUSD -o json
# {"XXBTZUSD":{"ask_price":81401.4,"bid_price":81401.3,"last_price":81401.3,"volume_24h":1371.77,...}}
```

Results are keyed by the pair name Kraken returns (`XXBTZUSD` here), with named
fields and numeric values. WebSocket and other streaming commands emit JSONL
(one JSON object per line).

### Table (`-o table`)

Human-readable tables. This is the default when `-o` is not specified.

```text
┌──────────┬─────────┬─────────┬─────────┬───────────────┬────────────┬───────────┐
│ Pair     ┆ Ask     ┆ Bid     ┆ Last    ┆ Volume (24h)  ┆ High (24h) ┆ Low (24h) │
╞══════════╪═════════╪═════════╪═════════╪═══════════════╪════════════╪═══════════╡
│ XXBTZUSD ┆ 79707.1 ┆ 79707.0 ┆ 79707.0 ┆ 1996.38136702 ┆ 81709.1    ┆ 79614.8   │
└──────────┴─────────┴─────────┴─────────┴───────────────┴────────────┴───────────┘
```

### Error envelopes

With `-o json`, a failure prints a JSON envelope on stdout with a stable `error`
category and exits 1:

```json
{ "error": "auth", "message": "Authentication failed: EAPI:Invalid key" }
```

In table mode, the default, the error is a plain `Error: ...` line on stderr.
Argument and usage errors exit 2, and with `-o json` they also put a
`validation` envelope on stdout.

Route on `error`, not on `message`. The `message` field is human-readable and
not stable.

| Category     | Retryable | Action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------------ | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `auth`       | No        | Check API key and secret. If the OAuth sign-in key expired, run `kraken auth login` again                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `rate_limit` | Yes       | Error includes `suggestion` with tier-specific limits, `docs_url` pointing to Kraken documentation, and `retryable` flag. Read `suggestion` and adapt strategy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `network`    | Yes       | Without `verify_first`, nothing was sent or the call was a read: retry with exponential backoff, max 5 retries. With `"verify_first": true`, a write may already have executed, so check its state before you resend it. Spot orders: `open-orders` and `closed-orders` (match on `--cl-ord-id` or `--userref`), then `trades-history` (match on the `ordertxid` from `closed-orders`). Futures orders: `futures open-orders`, `futures fills`, `futures history-orders`. Withdrawals and transfers: `withdrawal status`, `ledgers`, `futures transfers`. Earn: compare `amount_allocated.total.native` and `amount_allocated.pending.native` for the same `strategy_id` in `earn allocations` with the values recorded before the call (a missing `pending`, or a strategy that is not listed, counts as zero), and check `ledgers`; `earn allocate-status` and `earn deallocate-status` only say whether a known move is still pending. Resend only if the write is absent everywhere |
| `validation` | No        | Fix input parameters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `api`        | No        | Inspect request and parameters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `config`     | No        | Check config file or env vars                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `websocket`  | Yes       | Spot streams reconnect with backoff until interrupted. `futures ws` stops after 12 failed reconnects in a row. `ws` order methods: if the envelope has `"verify_first": true`, check open orders before resubmitting                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `io`         | No        | Check file paths and permissions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `timeout`    | Yes       | An operation ran past its time budget (`session stop`, a WebSocket token request, browser sign-in). Re-run; if `session stop` keeps timing out, check `kraken session show`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `parse`      | No        | Log raw response, possible API maintenance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

A `futures ws` reconnect counts as failed unless the new connection stays up for
30 seconds.

Full error catalog with envelopes and backoff strategies:
[agents/error-catalog.json](agents/error-catalog.json).

<details>
<summary>Logging: -v, --log-format, RUST_LOG</summary>

Diagnostics go through `tracing` to stderr only, so stdout stays the pure result
and JSON channel. Logging is off by default except warnings and errors, so the
`2>/dev/null` pattern is unaffected. The CLI never logs secrets or credentials,
and private API response bodies are left out even at trace level. `kraken-mcp`
also writes one `mcp_audit` JSONL line per tool call to stderr. The line records
the argument names and the values of order and transfer fields (amounts, prices,
pairs, addresses), never credentials, and `RUST_LOG` does not silence it. MCP
clients often keep server stderr in their own log files.

Format: logs are structured JSON (JSONL, one object per line) by default, so
machines can parse them out of the box. A human-readable format is opt-in:

```bash
kraken balance -o json -v 2>/dev/null | jq .   # result on stdout; logs (JSON) on stderr
kraken balance -v --log-format pretty           # human-readable logs instead
export KRAKEN_LOG_FORMAT=pretty                 # ...or via env (e.g. a dev shell profile)
```

`--log-format` accepts `json` (default), `pretty`, or `compact`, and is
independent of `-o`/`--output` (which formats the command result on stdout).

Level: `RUST_LOG` (the standard `tracing` filter) controls it and wins whenever
it is set. With `RUST_LOG` unset, `-v`/`--verbose` is a shortcut for debug-level
kraken-cli logs:

```bash
kraken balance -v                                  # kraken-cli at debug, dependencies at warn
RUST_LOG=warn,kraken=debug kraken balance          # same, explicit
RUST_LOG=kraken_rest=trace kraken ticker BTCUSD   # HTTP request/response detail
```

Note: a bare `RUST_LOG=debug` enables debug for _every_ crate (including
dependencies like `tungstenite`); scope it to `kraken`, which matches every
`kraken_*` crate, or just use `-v` for our diagnostics alone.

</details>

## MCP server

`kraken-mcp` is a built-in
[Model Context Protocol](https://modelcontextprotocol.io/) server over stdio, so
MCP clients can call Kraken as tools without a subprocess wrapper. Tool calls
run through the same command path as CLI commands and inherit the same error
handling and rate-limit behavior.

<!-- prettier-ignore -->
> [!WARNING]
> MCP is local-first and designed for your own machine. Any agent connected to
> this MCP server uses the same configured Kraken account and API key
> permissions. Do not expose, tunnel, or share this server outside systems you
> control. Always use `https://` and `wss://` endpoints. Treat this integration
> as alpha and use least-privilege API keys.

```bash
kraken-mcp                                          # default: market, account, paper, workspace, feedback
kraken-mcp -s market,account,paper,workspace,trade  # adds live spot trading
kraken-mcp -s all                                   # all services; dangerous calls need approval (see below)
kraken-mcp -s all --allow-dangerous                 # DANGER: no approval step; an agent can trade, withdraw and transfer
```

`-s all` serves all 152 MCP tools; the default services serve the subset in
their groups.

`kraken-mcp` signs with `KRAKEN_API_KEY` and `KRAKEN_API_SECRET` (and
`KRAKEN_FUTURES_API_KEY` and `KRAKEN_FUTURES_API_SECRET` for futures) when they
are set in the server's environment. Otherwise it signs with the active stored
key, including the OAuth sign-in key from `kraken auth login`, and reads that
key again on every call that can sign. When a stored sign-in key expires, calls
that need a key fail with an `auth` error, and a person runs `kraken auth login`
again. The `auth login`, `auth set`, `auth switch`, and `auth reset` commands
are not served over MCP.

### Approval for dangerous calls

Dangerous tools carry the `destructive_hint` annotation and include
`[DANGEROUS: requires human confirmation]` in the description. Unless you pass
`--allow-dangerous`, the server runs in guarded mode, whichever services you
load:

- On a client that supports MCP elicitation, the server puts each dangerous call
  to you and runs it only if you approve. A prompt that gets no answer within
  300 seconds fails closed.
- Inside a paper workspace, `order buy`, `order sell`, `order cancel` and
  `order cancel-all` fill on the simulator, so they drop both markers and run
  without approval. Every other dangerous tool stays gated there.
- `workspace create` with `mode: live` also asks for approval, because it
  allocates real money.

<!-- prettier-ignore -->
> [!WARNING]
> A client that cannot present an elicitation gets no prompt from the server.
> The call runs when the model sets `acknowledged=true` in its arguments. A
> model should set it only after its human approved that exact call, and on
> such a client your client's own tool-approval prompt is the only real check.
> Keep it turned on. In autonomous mode (`--allow-dangerous`), neither is asked
> for.

### Claude Code

Install `kraken-cli` with the one-liner first, because the plugin starts the
`kraken-mcp` binary that the installer puts on your PATH. Then install the
plugin, which adds the MCP server and the agent skills. Its server runs
`market,paper,feedback`, with no account access, so balances and live orders go
through the `kraken` CLI unless you widen `-s`:

```text
/plugin marketplace add krakenfx/kraken-cli
/plugin install kraken-cli@kraken
```

Or add only the MCP server. The full path works even before `kraken-mcp` is on
your PATH:

```bash
claude mcp add kraken -- "$HOME/.cargo/bin/kraken-mcp" -s market,paper,feedback
```

If you set `CARGO_HOME`, use `$CARGO_HOME/bin/kraken-mcp` instead.

If you installed `kraken-cli` while Claude Code was running, quit Claude Code
and start it again from a new terminal window.

### Other MCP clients

Claude Desktop, Cursor, Windsurf, Gemini CLI and other clients that read
`mcpServers` JSON take this entry:

```json
{
  "mcpServers": {
    "kraken": {
      "command": "kraken-mcp",
      "args": ["-s", "market,paper,feedback"]
    }
  }
}
```

VS Code takes the same entry under a top-level `"servers"` key in
`.vscode/mcp.json`. Codex reads TOML in `~/.codex/config.toml`:

```toml
[mcp_servers.kraken]
command = "kraken-mcp"
args = ["-s", "market,paper,feedback"]
```

This set starts market data, paper trading, and the feedback tool, which uploads
text, or a local file it names, to Kraken with no approval step (see
[Service groups](#service-groups)). It needs no credentials. Add `account` to
read your balances and orders, and `workspace` for paper workspaces. For live
trading, use `market,account,paper,workspace,trade` with a least-privilege API
key. If the client shows "Failed to connect", set `command` to the full path
that `command -v kraken-mcp` prints.

Gemini CLI users can install directly:
`gemini extensions install https://github.com/krakenfx/kraken-cli`

### Service groups

| Service       | Auth  | Risk                                                                                                                                                                              |
| ------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| market        | No    | None                                                                                                                                                                              |
| account       | Yes   | Read-only, except `export-retrieve` and `export-delete` (dangerous)                                                                                                               |
| trade         | Yes   | Orders (dangerous)                                                                                                                                                                |
| funding       | Yes   | Withdrawals, withdrawal cancel, and wallet transfers (dangerous)                                                                                                                  |
| earn          | Yes   | Staking (dangerous)                                                                                                                                                               |
| subaccount    | Yes   | Creating subaccounts and transfers (dangerous)                                                                                                                                    |
| futures       | Mixed | Orders, cancels, transfers, and leverage/PnL/subaccount settings (dangerous)                                                                                                      |
| futures-paper | No    | None (simulation)                                                                                                                                                                 |
| paper         | No    | Simulation; `reset` is dangerous; in a live workspace `status`/`balance` read the real account                                                                                    |
| workspace     | No    | `reset` and `promote` are dangerous, and `create --mode live` needs the same approval (it allocates real money and needs credentials); live workspaces gate like the real account |
| feedback      | No    | Uploads text, or a local file, to Kraken (see below)                                                                                                                              |
| auth          | Mixed | Read-only                                                                                                                                                                         |

Default: `market,account,paper,workspace,feedback`. The `feedback` tool calls
the same upload path as `kraken feedback`. It sends the text you give it (at
most 8192 bytes after trimming), the feedback type, the optional `--llm-model`
value, the CLI version, the OS and architecture, the detected agent client, a
stable install ID, a random event ID and a timestamp to
`https://cli-feedback.kraken.com/v1/feedback` over HTTPS. Do not put secrets or
personal data in it. Over MCP the tool also accepts `input_file`: it reads that
local file and uploads its contents, with no approval step, so a model could
upload any file it can name, including the config file that holds your stored
keys. A failed upload fails the command and is not retried. Drop `feedback` from
`-s` to turn the tool off, especially for an agent that reads untrusted input.
The streaming groups (`websocket`, `futures-ws`) and `utility` (the setup
wizard) are not served over MCP.

## Workspaces, sessions, and research

Beyond single orders, the CLI runs a research loop on paper:

1. A **workspace** gives a strategy its own capital and ledger.
2. A **session** records an evaluation window.
3. A **tape** preserves replayable market data.
4. A **lab experiment** seals the hypothesis and pass criteria before the first
   run.

```bash
# Create a paper workspace with its own $10,000.
kraken workspace create momentum --capital 10000 --mode paper -o json
export KRAKEN_WORKSPACE=momentum

# Record in one terminal.
kraken session start --symbols BTC/USD --channels ticker,trade \
  --label baseline --to jsonl -o json

# Trade in another terminal and preserve the rationale.
export KRAKEN_WORKSPACE=momentum
kraken paper buy BTC/USD 0.01 -o json
kraken session note --kind buy --symbol BTC/USD \
  --reason "breakout held above the prior high" -o json
kraken session stop -o json

# Review the closed window.
kraken session show --session baseline -o json
kraken explain pnl --session baseline -o json
kraken workspace report momentum -o json
```

For repeatable experiments, freeze the plan before the first session. A replay
leg names a finalized tape: `replay:session:s1` is the baseline session above,
the first one in this workspace (`kraken session list` shows each ordinal).

```bash
kraken lab new breakout-v1 \
  --hypothesis "a confirmed breakout produces positive net return" \
  --min-return-pct 0 --max-drawdown-pct 2 --min-fills 1 \
  --session live:5m --session replay:session:s1 -o json

kraken lab next breakout-v1 -o json
kraken lab compare breakout-v1 -o json
```

`--session live:5m` plans a 5-minute session on live prices inside the paper
workspace; it places no real orders. When you are done, run
`unset KRAKEN_WORKSPACE` so later commands reach your real account again.

The command tables below cover each surface. Machine-readable contracts live in
[agents/tool-catalog.json](agents/tool-catalog.json).

## Commands

The published catalog contains 188 commands across 15 groups; 152 of them are
callable as MCP tools, and the rest say why they are not. Parameter schemas live
in [agents/tool-catalog.json](agents/tool-catalog.json). Long-running streams
are in the catalog too, with `reach: stream`, and are documented below. They
stay CLI-only.

| Group         | Commands | Auth  | Description                                                                                                                                        |
| ------------- | -------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| market        | 11       | No    | Ticker, orderbook, OHLC, trades, spreads, asset info, tape library                                                                                 |
| account       | 18       | Yes   | Balances, orders, trades, ledgers, positions, exports                                                                                              |
| trade         | 9        | Yes   | Order placement, amendment, cancellation (spot, xStocks, forex)                                                                                    |
| funding       | 10       | Yes   | Deposits, withdrawals, wallet transfers                                                                                                            |
| earn          | 6        | Yes   | Staking strategies and allocations                                                                                                                 |
| subaccount    | 2        | Yes   | Create subaccounts, transfer between accounts                                                                                                      |
| futures       | 39       | Mixed | Futures market data and trading                                                                                                                    |
| futures-paper | 17       | No    | Futures paper trading simulation with live prices                                                                                                  |
| futures-ws    | 9        | Mixed | Futures WebSocket streaming                                                                                                                        |
| websocket     | 17       | Mixed | Spot WebSocket v2 streaming and request/response                                                                                                   |
| paper         | 17       | No    | Spot paper trading simulation with live prices, P&L explanation, and the Autoresearch Lab                                                          |
| workspace     | 25       | No    | Strategy workspaces, recorded sessions, recipes, and extension scaffolds: per-strategy ledgers, session windows, decision logs, reports, promotion |
| feedback      | 1        | No    | Product feedback upload to Kraken                                                                                                                  |
| auth          | 6        | Mixed | OAuth browser sign-in and credential management                                                                                                    |
| utility       | 1        | No    | Interactive setup (the REPL is the `kraken-shell` binary)                                                                                          |

43 commands are marked `dangerous`: orders and cancels (including the `ws` order
methods), withdrawals, transfers, staking, futures leverage/PnL/subaccount
settings, export retrieval and deletion, subaccount creation, paper and
workspace resets, workspace promotion, browser sign-in, and switching or
resetting the stored key. The CLI places orders without a confirmation prompt;
only some destructive commands, such as `cancel-all` and the resets, ask first
(skip the question with `--yes`). The MCP server gates the ones it serves (see
[Approval for dangerous calls](#approval-for-dangerous-calls)). The
authoritative list is the `dangerous` field in
[agents/tool-catalog.json](agents/tool-catalog.json).

<details>
<summary>Full command reference</summary>

### Market data (public)

| Command                                                                     | Description                                                     |
| --------------------------------------------------------------------------- | --------------------------------------------------------------- |
| `kraken status`                                                             | System status                                                   |
| `kraken server-time`                                                        | Server time                                                     |
| `kraken assets [--asset BTC,ETH] [--asset-class CLASS]`                     | Asset info                                                      |
| `kraken pairs [--pair BTCUSD] [--asset-class CLASS]`                        | Tradable pairs                                                  |
| `kraken ticker <PAIR...> [--asset-class tokenized_asset\|forex]`            | Ticker data                                                     |
| `kraken ohlc <PAIR> [--interval 60] [--asset-class tokenized_asset\|forex]` | OHLC candles                                                    |
| `kraken orderbook <PAIR> [--count 25] [--asset-class tokenized_asset]`      | L2 order book                                                   |
| `kraken orderbook-grouped <PAIR> [--depth 10] [--grouping 1]`               | Grouped order book                                              |
| `kraken trades <PAIR> [--count 1000] [--asset-class tokenized_asset]`       | Recent trades                                                   |
| `kraken spreads <PAIR> [--since TS] [--asset-class tokenized_asset]`        | Recent spreads                                                  |
| `kraken tape list`                                                          | Every recorded tape in the library: ref, backend, state, in use |

### Account data (private)

| Command                                                                                                                                                                                                  | Description                               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| `kraken orderbook-l3 <PAIR> [--depth 100]`                                                                                                                                                               | L3 order book                             |
| `kraken balance [--rebase-multiplier rebased\|base]`                                                                                                                                                     | All balances                              |
| `kraken extended-balance`                                                                                                                                                                                | Extended balances (balance, credit, held) |
| `kraken credit-lines [--rebase-multiplier rebased\|base]`                                                                                                                                                | Credit line details (VIP)                 |
| `kraken trade-balance [--asset USD] [--rebase-multiplier rebased\|base]`                                                                                                                                 | Margin/equity summary                     |
| `kraken open-orders [--trades] [--cl-ord-id ID] [--rebase-multiplier rebased\|base]`                                                                                                                     | Open orders                               |
| `kraken closed-orders [--start TS] [--end TS] [--offset N] [--userref REF] [--cl-ord-id ID] [--closetime open\|close\|both] [--consolidate-taker] [--without-count] [--rebase-multiplier rebased\|base]` | Closed orders                             |
| `kraken query-orders <TXID...> [--trades] [--userref REF] [--consolidate-taker] [--rebase-multiplier rebased\|base]`                                                                                     | Query specific orders                     |
| `kraken trades-history [--type TYPE] [--trades] [--offset N] [--consolidate-taker] [--without-count] [--ledgers] [--rebase-multiplier rebased\|base]`                                                    | Trade history                             |
| `kraken query-trades <TXID...> [--trades] [--rebase-multiplier rebased\|base]`                                                                                                                           | Query specific trades                     |
| `kraken positions [--txid ID] [--show-pnl] [--consolidation market] [--rebase-multiplier rebased\|base]`                                                                                                 | Open positions                            |
| `kraken ledgers [--asset BTC --type trade] [--asset-class CLASS] [--start TS] [--end TS] [--offset N] [--without-count] [--rebase-multiplier rebased\|base]`                                             | Ledger entries                            |
| `kraken query-ledgers <ID...> [--trades] [--rebase-multiplier rebased\|base]`                                                                                                                            | Query specific ledger entries             |
| `kraken volume [--pair BTCUSD] [--rebase-multiplier rebased\|base]`                                                                                                                                      | Trade volume & fees                       |
| `kraken export-report --report trades --description "desc" [--format CSV\|TSV] [--fields F] [--starttm TS] [--endtm TS]`                                                                                 | Request export                            |
| `kraken export-status --report trades`                                                                                                                                                                   | Export status                             |
| `kraken export-retrieve <ID>`                                                                                                                                                                            | Download export                           |
| `kraken export-delete <ID>`                                                                                                                                                                              | Delete export                             |

### Trading

| Command                                                                                                                                     | Description                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `kraken order buy <PAIR> <VOL> [--type TYPE] [--price P] [--oflags viqc] [--cl-ord-id ID] [--asset-class tokenized_asset] [--validate] ...` | Buy order. `--type` defaults to `limit`, which needs `--price`; `--type market --oflags viqc` buys a quote-currency amount |
| `kraken order sell <PAIR> <VOL> [--type TYPE] [--price P] [--cl-ord-id ID] [--asset-class tokenized_asset] [--validate] ...`                | Sell order (same `--type`/`--price` rule)                                                                                  |
| `kraken order batch <JSON_FILE> [--pair P] [--asset-class tokenized_asset] [--deadline DL] [--validate]`                                    | Batch orders (2-15)                                                                                                        |
| `kraken order amend --txid <TXID> [--order-qty Q --limit-price P ...]`                                                                      | Amend order in-place                                                                                                       |
| `kraken order amend --cl-ord-id <ID> [--limit-price P ...]`                                                                                 | Amend by client order ID                                                                                                   |
| `kraken order edit <TXID> [--price P]`                                                                                                      | Edit order (cancel+replace)                                                                                                |
| `kraken order cancel <TXID...>`                                                                                                             | Cancel by txid(s)                                                                                                          |
| `kraken order cancel --cl-ord-id <ID>`                                                                                                      | Cancel by client order ID                                                                                                  |
| `kraken order cancel-batch <TXID...> [--cl-ord-ids ID...]`                                                                                  | Cancel batch (max 50 total)                                                                                                |
| `kraken order cancel-all [--yes]`                                                                                                           | Cancel all                                                                                                                 |
| `kraken order cancel-after <SECS>`                                                                                                          | Dead man's switch                                                                                                          |

### Funding

| Command                                                                                                                                                        | Description                                                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `kraken deposit methods <ASSET> [--asset-class currency\|tokenized_asset] [--rebase-multiplier rebased\|base]`                                                 | Deposit methods                                                                                                                                                                                                                    |
| `kraken deposit addresses <ASSET> <METHOD> [--new] [--asset-class CLASS] [--amount AMT]`                                                                       | Deposit addresses                                                                                                                                                                                                                  |
| `kraken deposit status [--asset A] [--asset-class CLASS] [--method M] [--start TS] [--end TS] [--cursor C] [--limit N] [--rebase-multiplier rebased\|base]`    | Deposit status                                                                                                                                                                                                                     |
| `kraken withdraw <ASSET> <KEY> <AMOUNT> [--asset-class CLASS] [--address ADDR] [--max-fee F] [--rebase-multiplier rebased\|base]`                              | Withdraw funds                                                                                                                                                                                                                     |
| `kraken withdrawal methods [--asset A] [--asset-class CLASS] [--network N] [--rebase-multiplier rebased\|base]`                                                | Withdrawal methods                                                                                                                                                                                                                 |
| `kraken withdrawal addresses [--asset A] [--asset-class CLASS] [--method M] [--key K] [--verified true\|false]`                                                | Withdrawal addresses                                                                                                                                                                                                               |
| `kraken withdrawal info <ASSET> <KEY> <AMOUNT>`                                                                                                                | Withdrawal fee info                                                                                                                                                                                                                |
| `kraken withdrawal status [--asset A] [--asset-class CLASS] [--method M] [--start TS] [--end TS] [--cursor C] [--limit N] [--rebase-multiplier rebased\|base]` | Withdrawal status                                                                                                                                                                                                                  |
| `kraken withdrawal cancel <ASSET> <REFID>`                                                                                                                     | Cancel pending withdrawal                                                                                                                                                                                                          |
| `kraken wallet-transfer <ASSET> <AMT> --from <SOURCE_WALLET> --to <DEST_WALLET>`                                                                               | Move funds from your Spot wallet to your Futures wallet (`--from` and `--to` take wallet names as Kraken spells them: `--from "Spot Wallet" --to "Futures Wallet"`; for account-to-account moves use `kraken subaccount transfer`) |

### Earn

| Command                                                                                                    | Description         |
| ---------------------------------------------------------------------------------------------------------- | ------------------- |
| `kraken earn strategies [--asset ETH] [--lock-type flex bonded...] [--ascending] [--cursor C] [--limit N]` | List strategies     |
| `kraken earn allocate <ID> <AMT>`                                                                          | Allocate funds      |
| `kraken earn deallocate <ID> <AMT>`                                                                        | Deallocate funds    |
| `kraken earn allocate-status <ID>`                                                                         | Allocation status   |
| `kraken earn deallocate-status <ID>`                                                                       | Deallocation status |
| `kraken earn allocations [--ascending] [--converted-asset USD] [--hide-zero-allocations]`                  | Current allocations |

### Subaccounts

| Command                                                                                     | Description               |
| ------------------------------------------------------------------------------------------- | ------------------------- |
| `kraken subaccount create <USERNAME> <EMAIL>`                                               | Create sub account        |
| `kraken subaccount transfer <ASSET> <AMOUNT> --from IIBAN --to IIBAN [--asset-class CLASS]` | Transfer between accounts |

### Futures: public market data

| Command                                                      | Description              |
| ------------------------------------------------------------ | ------------------------ |
| `kraken futures instruments`                                 | All contracts            |
| `kraken futures tickers`                                     | All tickers              |
| `kraken futures ticker <SYMBOL>`                             | Single ticker            |
| `kraken futures orderbook <SYMBOL>`                          | Order book               |
| `kraken futures history <SYMBOL> [--since TS] [--before TS]` | Trade history            |
| `kraken futures feeschedules`                                | Fee schedules            |
| `kraken futures instrument-status [--symbol SYM]`            | Instrument status        |
| `kraken futures historical-funding-rates <SYMBOL>`           | Historical funding rates |

### Futures: trading (private)

| Command                                                                                                                                                                                                                                                     | Description               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| `kraken futures order buy <SYM> <SIZE> [--type limit] [--price P] [--stop-price SP] [--trigger-signal mark\|index\|last] [--client-order-id ID] [--reduce-only] [--trailing-stop-max-deviation V] [--trailing-stop-deviation-unit percent\|quote_currency]` | Buy futures               |
| `kraken futures order sell <SYM> <SIZE> [--type limit] [--price P] [--stop-price SP] ...`                                                                                                                                                                   | Sell futures              |
| `kraken futures edit-order --order-id ID [--size S] [--price P] [--stop-price SP]`                                                                                                                                                                          | Edit existing order       |
| `kraken futures cancel --order-id ID`                                                                                                                                                                                                                       | Cancel by order ID        |
| `kraken futures cancel --cli-ord-id ID`                                                                                                                                                                                                                     | Cancel by client order ID |
| `kraken futures cancel-all [--symbol SYM] [--yes]`                                                                                                                                                                                                          | Cancel all orders         |
| `kraken futures cancel-after <SECS>`                                                                                                                                                                                                                        | Dead man's switch         |
| `kraken futures batch-order '<JSON>'` or `kraken futures batch-order @file.json`                                                                                                                                                                            | Batch order placement     |

### Futures: account data (private)

| Command                                                                           | Description                          |
| ----------------