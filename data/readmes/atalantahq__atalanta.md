<h1 align="center"><img src="logo/logo.png" alt="" width="36" height="35" align="center"> Atalanta</h1>

**Mobile, web and API tests in YAML, from one static binary.**

[![CI](https://github.com/atalantahq/atalanta/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/atalantahq/atalanta/actions/workflows/ci.yml)
[![Security](https://github.com/atalantahq/atalanta/actions/workflows/security.yml/badge.svg?branch=main)](https://github.com/atalantahq/atalanta/actions/workflows/security.yml)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/17034/badge)](https://www.bestpractices.dev/projects/17034)
[![Licence](https://img.shields.io/badge/licence-AGPL--3.0--only-blue)](LICENSE)
[![Platforms](https://img.shields.io/badge/platforms-Android%20%C2%B7%20iOS%20%C2%B7%20Chrome-blue)](docs/DRIVERS.md)
[![Rust](https://img.shields.io/badge/rust-1.89%2B-blue?logo=rust)](Cargo.toml)

**[Docs](docs/README.md) · [How it works](#how-it-works) · [Example](#example) · [FAQ](#faq) · [Status](docs/STATUS.md) · [Changelog](CHANGELOG.md)**

Atalanta runs test suites on Android emulators, iOS simulators and Chrome. It is written in Rust: no JVM, no Node, no Appium server. Write the tests in YAML, or let an AI agent drive your app and write them for you. An agent-written test is checked before it is saved, and a saved test replays in CI without calling a model.

<p align="center">
  <img src="assets/hero.gif" width="100%" alt="A four-step YAML test opens Settings, General and About on an iOS 26 simulator and checks that the iOS version is shown; the terminal reports 1 passed in 8.2 seconds">
  <br>
  <sub>A real run on an iOS 26 simulator. The phone is the video Atalanta recorded of the test.</sub>
</p>

The latest release is [0.2.0](https://github.com/atalantahq/atalanta/releases/latest). [docs/STATUS.md](docs/STATUS.md) lists what has been verified, and on which devices.

## What it does

- **No sleeps.** Every step waits for its element and for the screen to settle.
- **Agent-written tests.** `atalanta explore "<goal>"` drives the app and saves the session as a YAML test.
- **Checked before saving.** An agent-written test is kept only if it passes five replays with no model and fails when its last tap is moved to a neighbouring element.
- **No model in CI.** The model picks an operation and an element number; code builds every selector and fills every value. Saved tests make no model calls.
- **APIs in the same suite.** An `http` step checks the response and captures values for later UI steps.
- **Evidence on your machine.** A failed test keeps a video, the device and app logs, and one `trace.html`. No cloud account.
- **A local console.** It mirrors every device and browser, shows the selector under the cursor, and runs suites and agent sessions.
- **Agent tooling.** Agents drive devices through an MCP server or plain shell commands.
- **Fast CI.** Run in parallel across devices, shard by past durations, or run only the tests a change can affect.
- **Your model.** Use any of 19 AI providers, local models included.

| Platform | Driven with | Requires | Verified on |
|---|---|---|---|
| Android | adb and Atalanta's on-device UI server | Android SDK platform-tools | 100+ devices (emulators API 33–34; physical phones and tablets through Android 14) |
| iOS | WebDriverAgent or Atalanta's own XCUITest runner | macOS with Xcode | iOS 26 simulators; multiple iPhones (12 and later) |
| Web | Chrome DevTools Protocol | Chrome or Chromium | Headless Chrome on macOS and Linux |
| API | HTTP | Nothing | |

## Quick start

Install on macOS or Linux:

```bash
brew install atalantahq/tap/atalanta
# or
curl -fsSL https://atalanta.sh/install.sh | sh
```

Or build from a checkout: `cargo install --path atalanta-cli --locked`.

To try the YAML first, the [playground](https://atalanta.sh/playground/) checks a suite in your browser and runs API tests there.

Start an emulator or simulator with your app installed, then:

```bash
atalanta doctor          # checks adb, Xcode, devices, Chrome and AI keys; --fix applies the safe fixes
atalanta init --run      # writes a first test from the app's launch screen and runs it
atalanta explore "open Network & internet" --app-id com.android.settings   # an agent writes a test
atalanta run open-network-internet.yaml                                    # replays it, no model
```

In CI:

```bash
atalanta run tests/ --parallel 4 --report junit,github --retries 1
atalanta run tests/ --shard 2/4 --shard-timings history/
atalanta run tests/ --changed-since origin/main
```

`atalanta init` also writes a sharded GitHub Actions example to `atalanta/ci/`. See [docs/CI.md](docs/CI.md).

## Install

Every route installs the same binary:

```bash
curl -fsSL https://atalanta.sh/install.sh | sh   # macOS / Linux
brew install atalantahq/tap/atalanta
npm install --save-dev @atalantahq/cli
cargo install atalanta-cli --locked
```

The first iOS run builds WebDriverAgent, which takes about a minute once per Xcode version. Signing, checksums and attestations are under [Install details](#install-details).

## How it works

<p align="center"><img src="assets/how-it-works.svg" width="100%" alt="Write a YAML test by hand or with atalanta explore; an agent-written test is checked by five model-free replays and a moved-tap check; run it on Android, iOS, Chrome and HTTP; read the video, logs and trace.html when it fails"></p>

## Example

```yaml
appId: com.example.app
tests:
  - name: Log in and open an order
    steps:
      - launchApp: { clearState: true }
      - inputText: { selector: { id: email }, text: "qa@example.com" }
      - inputText: { selector: { id: password }, text: "${LOGIN_PASSWORD}" }
      - tap: { id: login_button }
      - assertVisible: { text: "Welcome" }
      - do: "open the first order"          # natural language, cached once verified
      - http:
          method: GET
          url: https://api.example.com/orders/latest
          expect: { status: 200 }
          capture: { ORDER_ID: id }
      - assertVisible: { text: "${ORDER_ID}" }
```

Secrets are typed by name (`${LOGIN_PASSWORD}`) and masked in every report, log and trace. The full format is in [docs/DSL.md](docs/DSL.md), and [examples/](examples/README.md) has suites you can run as they are: Android, web, API only, and API plus web.

## When a test fails

```text
● about_lists_carrier ... FAILED 17.3s
  └ tests/settings.yaml:16: assertVisible { text: "Carrier" }: Element not found: text="Carrier" after 9999ms
```

Each failed test gets a `trace.html`: the steps with their timings, the video, the screen at the failing step, the selector and the closest elements that were on screen.

<p align="center"><img src="assets/trace.png" width="100%" alt="trace.html for a failed iOS test: four steps on the left, the last one red; the recorded video and the screenshot of the About screen; the failing selector text=Carrier and a table of the closest elements on screen"></p>

## Console and agents

```bash
atalanta inspect --open   # the console
atalanta mcp install      # registers the MCP server with your coding agents
```

The console is one browser page for every booted device and the web browser: a live mirror you can click and type on, an element overlay that shows the selector Atalanta would use, and panels to run suites, watch an agent explore and read a failure's trace. See [docs/CLI.md](docs/CLI.md#inspect).

`atalanta mcp install` covers Claude Code, Cursor, Codex, Windsurf, VS Code, Cline and Gemini CLI. It serves five tools by default; `--profile full` serves all 33. An agent reads the screen as one line per element, acts by reference, and exports what it did as a YAML test. Agents with a shell can skip MCP: `atalanta snapshot`, `atalanta tap @e7`, `atalanta export --out flow.yaml`. See [docs/MCP.md](docs/MCP.md).

## Why not Maestro or Appium?

| | Atalanta | Maestro | Appium |
|---|---|---|---|
| Tests are written in | YAML | YAML | Code, through a WebDriver client |
| Runs as | One static binary | A Java CLI | A Node.js server plus a driver per platform |

Atalanta's YAML takes ideas from Maestro, so moving over is short: `atalanta migrate maestro ./flows/` converts your flows and lists anything it skipped.

## Limits

- Pre-1.0: minor releases can change behaviour. Tested on 100+ real Android devices and multiple iPhones; [STATUS.md](docs/STATUS.md) lists specifics.
- Windows is not supported. WSL2 works as Linux.
- Web tests run on Chrome and Chromium only.

## FAQ

### Does a saved test call an AI model?

No. A model is used to write a test with `atalanta explore` and to resolve a `do:` step before it is cached. Replays make no model calls.

### Do I need an API key?

Only for `explore` and `do:` steps. Plain YAML tests need none. Local models work too: see [AI providers](docs/AI-PROVIDERS.md).

### Can my company use it? It's AGPL.

Yes. Running `atalanta` against your app, locally or in CI, puts no AGPL obligations on your app, your tests or your pipeline: they are not derived from Atalanta's code. The AGPL applies only if you change Atalanta itself and ship it or offer it as a network service. See [Licence](#licence).

## Documentation

- [Guide](docs/GUIDE.md): selectors, natural-language steps, visual checks, sharding, configuration and troubleshooting.
- [Explore](docs/EXPLORE.md): how agent-written tests are checked.
- [AI providers](docs/AI-PROVIDERS.md): models, keys and local models.
- [Drivers](docs/DRIVERS.md): what each platform needs and supports.
- [Security](docs/SECURITY.md): the threat model. Report vulnerabilities through [SECURITY.md](SECURITY.md).
- [Status](docs/STATUS.md): what has been verified, and on what.
- [All docs](docs/README.md).

## Install details

- **Install script.** Checks the download against the release's `SHA256SUMS` and installs into `~/.atalanta/bin` without sudo. Flags: `--dir DIR`, `--version X.Y.Z`, `--no-modify-path`, `--keep-quarantine`.
- **macOS signing.** Release binaries are ad-hoc signed, not notarised. If the binary carries the quarantine flag, the script removes it after the checksum check. With `--keep-quarantine`, approve it in System Settings > Privacy & Security on first run.
- **Release archives.** Built for macOS (arm64, x86_64) and static Linux (arm64, x86_64), each with a build provenance attestation: `gh attestation verify <file> --repo atalantahq/atalanta`.
- **Console UI from source.** `brew install --HEAD atalantahq/tap/atalanta` includes it. A plain `cargo build` does not; run `npm ci && npm run build` in `crates/atalanta-inspector/frontend` first.

## Feedback and contributing

- **Report a bug:** open an issue with the [bug report form](https://github.com/atalantahq/atalanta/issues/new?template=bug_report.yml). [SUPPORT.md](SUPPORT.md) says what to include.
- **Ask for a feature:** use the [feature request form](https://github.com/atalantahq/atalanta/issues/new?template=feature_request.yml).
- **Report a vulnerability:** follow [SECURITY.md](SECURITY.md). Do not open a public issue.
- **Contribute:** [CONTRIBUTING.md](CONTRIBUTING.md) covers the build, tests and pull requests. Please also read the [code of conduct](CODE_OF_CONDUCT.md).

## Star history

<a href="https://star-history.com/#atalantahq/atalanta&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=atalantahq/atalanta&type=Date&theme=dark">
    <img alt="Star history chart" src="https://api.star-history.com/svg?repos=atalantahq/atalanta&type=Date">
  </picture>
</a>

## Acknowledgements

Atalanta's Android screen streaming is adapted from [scrcpy](https://github.com/Genymobile/scrcpy). Its iOS runner speaks the API of [WebDriverAgent](https://github.com/appium/WebDriverAgent). The YAML format takes ideas from [Maestro](https://github.com/mobile-dev-inc/maestro). Visual diffs use the anti-aliasing detector from [pixelmatch](https://github.com/mapbox/pixelmatch). Web device profiles come from [Playwright](https://github.com/microsoft/playwright). Details are in [NOTICE](NOTICE).

## Licence

Atalanta is licensed under the GNU Affero General Public License, version 3 only (`AGPL-3.0-only`): see [LICENSE](LICENSE), and [NOTICE](NOTICE) for third-party material. Using the binary to test your own apps puts no obligations on those apps or their tests. Copying or adapting Atalanta's code into another project, or running a modified version as a network service, means releasing that work's source under the AGPL-3.0 and keeping the copyright notices. AI agents: read [AGENTS.md](AGENTS.md) before copying code from this repository.
