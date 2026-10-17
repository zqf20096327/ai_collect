# muxo

[![release](https://img.shields.io/github/v/release/devsoli/muxo?sort=semver)](https://github.com/devsoli/muxo/releases)
[![license](https://img.shields.io/badge/license-MIT-blue)](#license)
[![macOS](https://img.shields.io/badge/platform-macOS-lightgrey)](#requirements)

Give `muxo` an endpoint and API key once. `muxo` handles the rest.

`muxo` is a macOS launcher for CLI coding agents. You point it at a
9Router-compatible (OpenAI-shaped) endpoint one time; after that,
`muxo launch claude` discovers the models the router serves, picks one the
agent can actually run, configures the agent, and hands your terminal over to
it. No environment variables to export, no agent config files to hand-edit,
no API key sitting in a dotfile.

```
muxo setup                  # one time
muxo launch claude          # every time after that
```

## Requirements

- macOS (Apple Silicon or Intel)
- An account on a 9Router-compatible endpoint that exposes `GET /v1/models`
- The agent you want to launch, installed and on your `PATH`

## Installation

**Homebrew** (recommended):

```sh
brew install devsoli/tap/muxo
```

Upgrade and uninstall are the usual Homebrew commands:

```sh
brew upgrade muxo
brew uninstall muxo
```

Installing through Homebrew also avoids the Gatekeeper quarantine prompt a
manually downloaded, unsigned binary would hit.

**Pre-built binary**, if you would rather not use Homebrew — pick the archive
for your architecture from the [latest release](https://github.com/devsoli/muxo/releases/latest),
then:

```sh
tar -xzf muxo_*_darwin_*.tar.gz
xattr -d com.apple.quarantine muxo      # release binaries are unsigned
mv muxo /opt/homebrew/bin/              # or anywhere on your PATH
```

Each release ships a `checksums.txt`; verify with `shasum -a 256 -c checksums.txt`.

**From source** (Go 1.24+):

```sh
git clone https://github.com/devsoli/muxo
cd muxo
make install          # builds and installs to /opt/homebrew/bin (or /usr/local/bin)
```

`make install` picks the Homebrew prefix that exists on your machine, because
`/usr/local/bin` is not on the default `PATH` on Apple Silicon. To choose your
own location:

```sh
make install PREFIX=$HOME/.local
```

**Build only**, without installing:

```sh
make build            # -> dist/muxo
```

Check what you installed:

```sh
muxo version
muxo doctor
```

## Setup

```sh
muxo setup
```

You are asked for your router endpoint and API key. The key is typed
invisibly and never echoed.

```
Welcome to muxo

Router endpoint [https://router.example.com/v1]:
API key: ********

✓ Endpoint reachable
✓ Authentication successful
✓ Models loaded (14 available)

Setup complete. Run: muxo launch claude
```

`muxo` verifies the endpoint and key **before** storing anything, so a typo
never leaves you with a broken configuration.

Endpoints are normalised to a single `/v1` suffix, so all of these are
accepted and mean the same thing:

```
https://router.example.com
https://router.example.com/
https://router.example.com/v1
https://router.example.com/v1/
```

Non-interactive setup, for scripts and CI — the key is read from the named
environment variable, never from an argument (arguments are visible in `ps`):

```sh
MUXO_KEY=sk-... muxo setup --endpoint https://router.example.com --api-key-env MUXO_KEY
```

## Launching an agent

```sh
muxo launch claude
muxo launch codex
muxo launch hermes
```

```
✓ Connected to 9Router
✓ Found 14 models

Which model should Claude Code use?

›  1  claude-sonnet-4-5  (recommended)
   2  claude-opus-4-1
   3  claude-haiku-4-5
   4  gpt-5-codex

Enter number, or press Enter for claude-sonnet-4-5:
> 

✓ Selected claude-sonnet-4-5

Launching Claude Code...
```

The list is the agent's own preference order, so pressing Enter takes the
model `muxo` would have picked anyway. The prompt is skipped when the model is
already decided — `--model`, a configured default, or a non-interactive stdin.

The agent replaces `muxo` in the process table, so your terminal talks to the
agent directly: Ctrl+C reaches the agent, its exit code is yours, and stdin,
stdout, and stderr pass straight through.

**Pass arguments to the agent** after `--`:

```sh
muxo launch claude -- --continue
muxo launch hermes -- chat --resume
```

**Override the model** for one run:

```sh
muxo launch claude --model claude-opus-4-1
```

If that exact model is not served by your router, `muxo` says so and stops —
it never quietly substitutes a different one.

**Pin a default model** per agent:

```sh
muxo config set-model claude claude-opus-4-1
muxo config set-model claude auto            # back to automatic selection
```

Precedence is `--model` → configured default → automatic selection.

## Model discovery

```sh
muxo models              # everything the router serves
muxo models --coding     # only coding-capable models
```

```
MODEL                     PROVIDER    CODING
claude-sonnet-4-5         anthropic   yes
gpt-5-codex               openai      yes
text-embedding-3-large    openai      no
```

Selection is by pattern, not by a pinned list of version numbers, so a new
model release works without a `muxo` update:

| Agent  | Preference order                                                    |
|--------|---------------------------------------------------------------------|
| claude | `claude-sonnet` → `claude-opus` → any `claude` → any coding model    |
| codex  | `gpt-*-codex` → any `codex` → coding `gpt` → any `gpt` → any coding  |
| hermes | `hermes` → any `coder` → any coding model                           |

Within a tier, full-size beats mini/lite/haiku/flash, and stable beats
preview/alpha/beta. Selection is deterministic: the same catalogue always
yields the same model.

## Inspecting configuration

```sh
muxo config
```

```
muxo configuration

Endpoint:
  https://router.example.com/v1

API Key:
  ********configured********

Claude model:
  auto

Codex model:
  auto

Hermes model:
  auto

Config file:
  /Users/you/.muxo/config.json
```

The API key is never printed, by any command, in any mode.

## Troubleshooting

```sh
muxo doctor
```

Each check runs independently, so one failure never hides the others:

```
✓ Configuration found
✓ API key found in macOS Keychain
✓ Endpoint reachable
✓ Authentication successful
✓ Models API available (14 models)
✓ Coding-capable model available
✓ Claude Code installed
✗ Codex installed

✗ Codex not found

muxo looked for "codex" on your PATH and did not find it.

Install it with:

  npm install -g @openai/codex

or see https://developers.openai.com/codex

Then run:

  muxo doctor
```

`muxo doctor` exits non-zero when any check fails, so scripts can gate on it.

Add `--debug` to any command for verbose output. Debug logging prints request
URLs, response codes, and environment variable **names** — never header
values, and never your API key.

```sh
muxo launch claude --debug
```

| Symptom | Cause | Fix |
|---|---|---|
| `Not configured` | No `~/.muxo/config.json` | `muxo setup` |
| `Authentication failed` | Key rejected by the router | `muxo setup` |
| `Cannot reach endpoint` | Wrong URL, or network/VPN | check `muxo config`, then `muxo doctor` |
| `No compatible model` | Router serves nothing the agent can run | `muxo models` to see the catalogue |
| `Model not available` | `--model` names something the router does not serve | `muxo models` |
| `<agent> is not installed` | Binary not on `PATH` | install the agent |
| Hermes: `No active credentials for provider` | Hermes stripped a prefix from the model ID | `brew upgrade muxo` |

### Hermes: model IDs with a `ollama/` or `custom/` prefix

Hermes strips a leading `<provider>/` from a model ID when the prefix names the
provider it is calling, and `ollama` is an alias of the `custom` provider muxo
must use. A router model genuinely named `ollama/kimi-k3` therefore reached the
API as `kimi-k3` and returned HTTP 404. `muxo` now pre-compensates, so the router
receives the ID it actually advertises.

## Security

**Your API key is stored in the macOS Keychain, never in a file.**

- The key goes to the Keychain under service `muxo`. `~/.muxo/config.json`
  holds only the endpoint and model preferences.
- Keychain writes pass the secret hex-encoded (`security -X`), so it never
  appears as readable plaintext in the process argument list.
- The Keychain item's ACL trusts `/usr/bin/security`, so `muxo` reads the key
  back without a Keychain password prompt on every launch. The key stays
  encrypted at rest and locked with your login Keychain, but any process
  running as you can read it back with `security find-generic-password`.
  This is the same posture as `gh` and `aws-vault`; the alternative — a
  password dialog per `muxo launch` — pushes people to paste keys into
  dotfiles instead. If you would rather be prompted every time, run:

  ```
  security delete-generic-password -s muxo -a 9router
  security add-generic-password -s muxo -a 9router -w -T ""
  ```
- The config directory is `0700` and the config file `0600` — user-only.
- No command prints the key: not `config`, not `--debug`, not error messages.
  Network errors are scrubbed before display.
- The key is sent to exactly one place: the router endpoint you configured.
- No telemetry, no analytics, no backend service. `muxo` is entirely local
  apart from requests to your router.

How each agent receives the key:

| Agent | Mechanism | Key on disk? |
|---|---|---|
| Claude Code | generated settings file passed with `--settings` | Yes — see below |
| Codex | generated `CODEX_HOME`; config names an env var, key passed in env | No |
| Hermes | generated `HERMES_HOME`; `config.yaml` (mode `0600`, dir `0700`) | Yes — see below |

Claude Code prefers the `env` block of its own `~/.claude/settings.json` over
the environment it inherits, so environment variables alone cannot configure it
for a user who has already set that block by hand. `--settings` does outrank it,
and is additive: muxo writes a settings file containing nothing but the `env`
block to `~/.muxo/claude-home` (mode `0600`, dir `0700`) and passes it with
`--settings`. Your own `~/.claude/settings.json` is never read, merged or
modified, and your permissions, hooks and agents keep loading from it.

Hermes' `custom` provider reads its credential from the config file and has
no fixed environment variable, so the key must be written there. `muxo` writes
it to a generated config root it owns (`~/.muxo/hermes-home`) with user-only
permissions, and never touches your own `~/.hermes/config.yaml`.

`muxo` never edits your existing agent configuration. For Codex and Hermes it
copies your settings (MCP servers and all) into a generated config root and
overrides only the model and provider keys there. For Claude Code it writes a
separate settings file holding only the router keys.

## Development

```sh
make build     # dist/muxo
make test      # go test ./...
make lint      # gofmt -l . && go vet ./...
make release   # test + lint + both macOS architectures + SHA256SUMS
make clean
```

Optional live tests against a real router are skipped unless both variables
are set:

```sh
MUXO_TEST_ENDPOINT=https://router.example.com/v1 \
MUXO_TEST_API_KEY=sk-... go test ./internal/router/ -run Live -v
```

`MUXO_HOME` overrides the config directory, which is how the test suite stays
away from your real configuration.

### Releasing

Pushing a `v*` tag runs `.github/workflows/release.yml` on a macOS runner:
tests, then GoReleaser builds both macOS architectures, publishes the archives
and `checksums.txt` to GitHub Releases, and updates the formula in
[devsoli/homebrew-tap](https://github.com/devsoli/homebrew-tap).

```sh
git tag v0.2.0 && git push origin v0.2.0
```

The tap update needs a `HOMEBREW_TAP_TOKEN` secret with `contents: write` on
the tap repository. Drop the `brews:` block from `.goreleaser.yaml` to publish
plain release binaries only.

## Project layout

```
cmd/muxo/              entry point
internal/cli/         commands (setup, models, config, launch, doctor, version)
internal/config/      config file, endpoint normalisation
internal/keychain/    macOS Keychain secret store
internal/router/      OpenAI-compatible model listing
internal/model/       capability classification, per-agent selection
internal/launcher/    agent launchers (claude, codex, hermes)
internal/process/     syscall.Exec process replacement
internal/doctor/      diagnostics
internal/ui/          terminal output
```

Each agent's knowledge lives entirely inside its own launcher package.

## License

MIT
