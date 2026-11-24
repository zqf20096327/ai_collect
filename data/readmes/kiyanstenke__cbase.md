<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="web/public/cbase-lens.png">
    <img src="web/public/cbase-lens-ink.png" alt="cbase" width="96">
  </picture>
</p>

# cbase

**A self-hosted workbench for long-running coding agents.** Let Claude Code, Codex and OpenRouter models work for hours in an
isolated container of their own, and check in from the browser, a Mac app or your iPhone to read along, step in or approve.
Everyone brings their own provider subscription or API key; cbase runs on your server.

Why not just the CLI in a terminal? Because a run outlives your laptop lid: sessions keep going when you disconnect, every user
and every project gets its own container, approvals reach you on your phone, and the same agents can run on a schedule or in a
workflow while you do something else.

## What you get

- **Agents** — Claude Code and Codex through their official CLIs (pinned versions), OpenRouter models through a built-in engine.
  Subagents, skills, effort levels, slash commands, a message queue, approval cards and automatic context compaction.
- **A place to work** — workspaces with projects; a project can get its own container with its own Docker daemon. In the browser:
  a file explorer and editor with language services, terminals, a Git view with branches and diffs, and the agent's
  own browser to watch and take over; preview links through your own ngrok account. VS Code can attach through Remote Tunnels.
- **Automation** — scheduled tasks (one chat per job, each run a message), graph and scripted workflows, and channels through
  which chats hand work to each other.
- **Clients** — the web UI, a macOS desktop app around it, and a native iOS app with push notifications. English and German.
- **Operation** — a gateway with user management, one long-lived container per user with its own limits, idle stop, and runs
  that resume after a restart.

## How it works

```
 browser · macOS app · iOS app
              │  HTTPS (TLS at your reverse proxy)
           gateway  ── users, sessions, containers, reverse proxy for HTTP and SSE
              │
   ┌──────────┴──────────┐
 user container A     user container B      one backend per user (Sysbox: its own inner Docker)
   │  agents, files, tools, the user's provider logins
   └─ project containers                  optional: one Docker daemon per project
```

- **One container per user.** The backend is single-tenant and runs unchanged inside it; multi-tenancy comes from the container
  boundary, not from a `user_id` on every query.
- **Own credentials.** Every user signs in to their providers inside their own container. cbase never shares or proxies a login.
- **One UI.** `web/` is the only source of the interface; the desktop app loads it from the gateway, the iOS app talks to the same API.

## Status

cbase is pre-1.0. The author uses it daily on one self-hosted server; there are no stability guarantees yet, and
`main` is the only supported branch. The provider CLIs are pinned and moved deliberately. Parts are macOS-only: the desktop app,
the iOS build and the macOS test suite.

## Requirements

- **Server:** Linux x86_64 with Docker. [Sysbox](https://github.com/nestybox/sysbox) is recommended: it gives every user container
  its own inner Docker without `--privileged`. Without it (`GW_RUNTIME` empty) the gateway runs plain Docker containers: not
  privileged, no Docker socket, ports bound to `127.0.0.1`, but weaker isolation against a container escape and no project
  containers. The gateway warns at start. Use Sysbox for anything shared.
- The OS user running the gateway must be able to run `docker`.
- **Node.js 22** (22.13 or later in the 22.x line; `node:sqlite`) for the gateway and the tools (the backend image brings its own).
- **Clients:** any current browser; the desktop app needs macOS, the iOS app Xcode 26 or newer.
- **Providers:** each user needs their own Claude and/or ChatGPT/Codex subscription, or API keys (OpenRouter).

## Quick start

```sh
git clone https://github.com/kiyanstenke/cbase.git && cd cbase
server/backend/build.sh                     # build the backend image (once, and after changes; the first build takes minutes)
(cd web && npm ci && npm run build)         # build the UI; the gateway serves web/out

GW_RUNTIME=sysbox-runc node server/gateway/index.js   # with Sysbox (check: docker info | grep -i sysbox)
node server/gateway/index.js                          # or without Sysbox (no project containers)
```

If you build with `CBASE_IMAGE=<name>`, start the gateway with `GW_IMAGE=<name>` (default for both: `cbase-backend`), or creating
a user's container fails.

The gateway listens on `127.0.0.1:7719`. Its log prints a **setup token** (also stored in `<GW_DATA>/setup-token`,
by default `server/gateway/data/setup-token`, unless you set `GW_SETUP_TOKEN`).

1. Open `http://127.0.0.1:7719`, enter the setup token and create the admin account.
2. Under **Settings → Providers**, sign in to Claude or Codex, or add an OpenRouter key. The Codex browser sign-in works from the
   macOS desktop app; from a browser or iPhone run `codex login --device-auth` in a cbase terminal.
3. Create a workspace, add a project, start a chat.
4. Add more users under **Settings → Admin**; a user's first request starts their container.

Desktop app: `(cd client && npm ci && npm start)` — it asks for the gateway address. iOS: open `mobile/CbaseMobile.xcodeproj` in
Xcode, set your team and run; if Xcode reports the bundle ID as taken, use your own and set `GW_APNS_TOPIC` to it for push
([mobile/README.md](mobile/README.md)). Installing the backend's own dependencies on the host (`server/backend`, `npm ci`) is only
needed for development and the tests — see [CONTRIBUTING.md](CONTRIBUTING.md).

Project containers need the project-box image inside each user container. `./deploy server` distributes it (see
[DEPLOY.md](DEPLOY.md)); with the manual start, load the image `build.sh` built into a running user container yourself:

```sh
docker save cbase-projectbox:hand | docker exec -i cbase-u-<id> docker load
docker exec cbase-u-<id> docker tag cbase-projectbox:hand cbase-projectbox:latest
```

Without it, projects run inside the user container.

## Running it for real

Put the gateway behind a TLS reverse proxy (Caddy, nginx, Traefik) and start it with `GW_SECURE=1` (required behind TLS, otherwise
the session cookie lacks `Secure`; the gateway warns at start when `GW_HOST` is not loopback and it is unset). Keep
`GW_HOST=127.0.0.1` when the proxy runs on the same host; use `0.0.0.0` only for a proxy elsewhere and list that proxy in
`GW_TRUSTED_PROXYS`. The proxy must overwrite `CF-Connecting-IP` with the client address (Caddy `header_up CF-Connecting-IP
{remote_host}`, nginx `proxy_set_header CF-Connecting-IP $remote_addr;`) — the login brake counts failures per that address.
`./deploy` builds, checks and rolls out web, backend and desktop app to a server over SSH — [DEPLOY.md](DEPLOY.md). Every gateway
setting (`GW_*`) and the server layout: [server/README.md](server/README.md).

## Security

Agents run shell commands with full rights inside their user's container — that is the point, and it is also the boundary. Use
Sysbox (without it, containers are plain Docker containers with weaker isolation), give each container sensible limits, and keep the
host's Docker socket away from anything else: the gateway's Docker access is root-equivalent on the host. Report vulnerabilities as
described in [SECURITY.md](SECURITY.md).

## Provider terms

cbase ships no model access and proxies no login. Each user signs in inside their own container with the providers' official
tools or an API key, and each user is responsible for following their provider's terms. Consumer subscriptions are licensed to
the person who holds them; whether a provider allows using one through a self-hosted tool like this is for the provider to decide.
For shared, team or commercial use, use API keys.

Images built from `server/backend/Dockerfile` install the Claude Code CLI (proprietary, Anthropic's terms apply) and the Codex CLI
(Apache-2.0), and download Microsoft's VS Code CLI (Microsoft Software License Terms, <https://aka.ms/vscode-server-license>; the
VS Code tunnel asks each user to accept them once). Such images are for your own use: do not push them to a public registry.

## Documentation

| | |
|---|---|
| [server/README.md](server/README.md) | gateway, user containers, settings, provider sign-in |
| [DEPLOY.md](DEPLOY.md) | the deploy tool: building, checking and rolling out to a server |
| [DESIGN.md](DESIGN.md) | the interface: colour roles, building blocks, the iOS kit |
| [AGENTS.md](AGENTS.md) | for coding agents (and their people): how the system is built, the rules and the traps |
| [tools/check/README.md](tools/check/README.md) | the gate and every guard in it |
| [docs/](docs/) | the project's GitHub Pages site: [privacy policy](https://kiyanstenke.github.io/cbase/privacy/) and [support](https://kiyanstenke.github.io/cbase/support/) of the iOS app |

## Contributing

`./check` is the gate for the whole tree; `./check --quick` runs everything but the test suites in seconds. Setup, the full gate
and how to send a change: [CONTRIBUTING.md](CONTRIBUTING.md). Conduct: [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Licence and trademarks

cbase is free software under the GNU Affero General Public License, version 3 (AGPL-3.0-only) — [LICENSE](LICENSE),
[NOTICE](NOTICE). You may use, change and run it, also commercially; if you offer a modified version to users over a network, you
must give them its source code (section 13) — build the UI with `NEXT_PUBLIC_SOURCE_URL=<your repository>` so that **Settings →
Third-Party Notices** points your users at your source, not at this repository. Third-party notices are in
[web/public/THIRD_PARTY_NOTICES.txt](web/public/THIRD_PARTY_NOTICES.txt). cbase is not affiliated with or endorsed by Anthropic,
OpenAI, Microsoft or any other provider it works with; their names describe compatibility. See [TRADEMARKS.md](TRADEMARKS.md).
