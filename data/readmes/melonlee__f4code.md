# F4code

<p align="center">
  <img src="f4code.png" alt="F4code" width="100%">
</p>

A GUI for coding agents that puts models on your own hardware first. A Node WebSocket server wraps
provider CLIs and agents (Codex, Claude Code, Cursor, Grok, OpenCode, Antigravity, Kiro, Pi, Muse
Code, fx) and serves web, desktop and mobile clients from one place.

Think of it as a bring-your-own-subscription alternative to apps like Claude Desktop, Codex App,
Cursor Glass and Conductor — except the model you point it at can be one running on your laptop.

## Local models come first

- **One step to a local model.** From first run, Settings, the model picker, or the command
  palette, F4code finds the servers on your machine (Ollama, LM Studio, llama.cpp, vLLM, SGLang,
  TensorFold), links an agent to the one you pick, and makes its model the default for new threads.
- **Repair instead of "Unreachable".** When a server stops answering, **Find server** looks for where
  it moved and moves it there, keeping its name, key and linked agents.
- **Never quietly cloud.** **Local models only** holds even before any local model is set up, and a
  Codex instance linked to a server waits for it instead of falling back to a cloud login.
- **Background writing stays local.** Thread titles, commit messages, PR text, branch names and
  voice cleanup use a local model; **Settings → Threads → Text generation fallback** defaults to
  **Local models only**, so your diffs never leave the machine on their own.
- **The picker says where a model runs**, and local models show **Local** instead of a cloud price.

## Three surfaces, one server

- **Web** — served locally by the `f4` command, or pointed at any environment you run.
- **Desktop** — an Electron app that bundles the server runner and can host remote connections.
- **Mobile** — a React Native app for iOS and Android that drives any F4code server.

## Remote work, encrypted if you want

Connect over your local network, Tailscale, SSH, or a tunnel. In **Settings → Sharing & access**,
both **Private transports only** (refuse tunnels, proxies and plain LAN) and **End-to-end
encryption** are available and off by default. Limits are in
[Encrypted remote control](./docs/user/encrypted-remote-control.md).

## No telemetry

This fork's telemetry, analytics, tracing and identity collection were deleted from the code rather
than switched off: no analytics, no crash reporting, no install IDs. The only network traffic is
traffic you create — your prompts and files to the model providers you configure, tunnel traffic
when you link environments, model-catalog and price fetches, and update checks. The complete list is
in [docs/user/network-calls.md](./docs/user/network-calls.md).

## Run it

Requirements: Node 26 and pnpm 12 (`pnpm install -g pnpm@12`; the repo pins `pnpm@12.14.0`).

```sh
pnpm install
pnpm dev          # server + web; prints a pairing URL to open
```

Other entry points:

```sh
pnpm dev:web      # web client only
pnpm dev:desktop  # Electron shell
pnpm typecheck    # whole monorepo
```

### Build a desktop app

Linux AppImage (needs a recent Rust, `libsecret-1-dev` and ImageMagick):

```sh
vp i
vp run dist:desktop:linux   # artifacts land in release/
```

No prebuilt binaries are published for this fork yet, and the update check is not wired to a real
server — rebuild to update.

## Layout

| Path                      | What lives there                                                                         |
| ------------------------- | ---------------------------------------------------------------------------------------- |
| `apps/server`             | WebSocket server, provider adapters, orchestration, checkpointing                        |
| `apps/web`                | React/Vite client                                                                        |
| `apps/desktop`            | Electron shell around the web client                                                     |
| `apps/mobile`             | React Native client                                                                      |
| `apps/marketing`          | Marketing site                                                                           |
| `packages/contracts`      | Wire contracts shared by every client and the server                                     |
| `packages/client-runtime` | Connection and domain state shared by web and mobile                                     |
| `packages/provider-*`     | One adapter per agent                                                                    |
| `docs/`                   | [User docs](./docs/user), [internals](./docs/internals), [operations](./docs/operations) |

`AGENTS.md` records the conventions this codebase is maintained with; `MIA_CHANGELOG.md` records what
changed in this fork, newest first.

## Credits and license

F4code is an unofficial fork of [T3 Code](https://github.com/pingdotgg/t3code), built by T3 Tools
Inc. and its contributors. This fork keeps their copyright notice and is not affiliated with or
endorsed by T3 Tools; it follows their branding policy, so the name, wordmark and icons here are
F4code's own. [TRADEMARK.md](./TRADEMARK.md) holds the upstream policy on the T3 marks.

Released under the [MIT License](./LICENSE), the same as upstream. That license covers source code
only, not either project's trademarks or branding. Third-party notices are in
[third-party-licenses](./third-party-licenses).
