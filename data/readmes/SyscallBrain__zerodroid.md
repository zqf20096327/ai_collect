<img src="docs/images/banner.jpg" alt="ZeroDroid: your ZeroClaw agents, in your pocket" width="100%">

<div align="center">

# ZeroDroid

Your [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw) agents, in your pocket.

[![CI](https://github.com/SyscallBrain/zerodroid/actions/workflows/ci.yml/badge.svg)](https://github.com/SyscallBrain/zerodroid/actions/workflows/ci.yml)
[![Latest release](https://img.shields.io/github/v/release/SyscallBrain/zerodroid?color=38bdf8)](https://github.com/SyscallBrain/zerodroid/releases/latest)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Android 10+](https://img.shields.io/badge/android-10%2B-3ddc84.svg?logo=android&logoColor=white)](#install)
[![Kotlin](https://img.shields.io/badge/kotlin-2.4-7f52ff.svg?logo=kotlin&logoColor=white)](https://kotlinlang.org)
[![Jetpack Compose](https://img.shields.io/badge/Jetpack_Compose-Material_3-4285f4.svg?logo=jetpackcompose&logoColor=white)](https://developer.android.com/compose)
[![ZeroClaw 0.9.0+](https://img.shields.io/badge/ZeroClaw-0.9.0%2B-0ea5e9.svg)](https://github.com/zeroclaw-labs/zeroclaw)

[Install](#install) ·
[Pairing](#pairing) ·
[Screenshots](#screenshots) ·
[Changelog](CHANGELOG.md) ·
[Report a bug](https://github.com/SyscallBrain/zerodroid/issues/new?template=bug_report.yml)

</div>

<p align="center">
  <img src="docs/screenshots/home.jpg" width="24%" alt="Home: daemon status, memory, CPU, uptime, sessions and shortcuts to Automation, Workflows, Canvas and Doctor">
  <img src="docs/screenshots/chat.jpg" width="24%" alt="A chat with an agent, with a shell tool call and a formatted answer">
  <img src="docs/screenshots/code.jpg" width="24%" alt="The Code tab with folder-rooted sessions">
  <img src="docs/screenshots/config.jpg" width="24%" alt="The Config tab with searchable daemon settings">
</p>

ZeroDroid is a native Android client for the [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw)
daemon. Talk to any of your agents, follow their tool calls as they run,
answer approvals from a notification, and check or change the daemon's
configuration, whether the daemon runs in Termux on the same phone or on a
machine at home.

It is a remote control, not a second runtime: agents, tools, channels and
memory all stay on the daemon.

## Features

- **Home**: the daemon at a glance. Memory, CPU, uptime and active sessions,
  shortcuts to Automation, Workflows, Canvas and Doctor (whichever needs a
  look, a failed job or a doctor error, comes first), which subsystems and
  channels are running, today's spend, the next scheduled jobs, and your
  agents with pinned favourites at the top. Each shortcut can be hidden.
- **Chats** with any agent, across many sessions. Answers stream in with
  Markdown and code formatting, every tool call shows its arguments and
  output, and you can steer or stop a running turn. Send images, rename and
  delete chats, search them, and see or change the model in use.
- **Code**: sessions rooted in a folder on the daemon's machine, like
  zerocode. Pick the folder with a browser, or work in the agent's workspace.
  When the agent edits a file, tap the tool call to see the change as a
  diff: removed lines in red, added lines in green, unchanged ones folded,
  with the raw arguments one tap away. This works in chats too.
  Chats and code sessions survive a daemon restart only with
  [the ZeroClaw patch](#keeping-your-sessions-the-zeroclaw-patch).
- **Workflows**: build and run the daemon's SOPs (step-by-step procedures)
  from the phone. Steps sit in a vertical flow you edit by tapping: wire the
  next step, the step to go to on failure, branches by condition and steps
  that wait for others. Each step opens in a sheet with its instructions,
  suggested tools and the outputs of earlier steps. Set triggers, the
  execution mode, the agent and concurrency, run a workflow with optional
  input, and follow its runs and approvals live. If the daemon's SOP engine
  is off, the app can turn it on for you, and its Home shortcut can be hidden if
  you don't use SOPs.
- **Canvas**: when an agent draws something with its `canvas` tool (a chart,
  a table, a diagram) in a chat or code session on the phone, the app keeps a
  copy, so you can open it again later, even after the daemon restarts (the
  daemon keeps canvases in memory only). Open them from Home, from
  the canvas tool call while it is on screen, or from the canvas icon at the
  top of the chat that drew them. HTML and SVG frames open in a sandboxed view
  that can run scripts and load chart libraries but cannot reach the app or
  your files; pages too wide for the phone are zoomed out to fit, and you can
  pinch to zoom. Markdown and text are shown natively. Each canvas keeps its
  last 50 frames. A chat's history comes back from the daemon as text only,
  so a frame is saved only if the app sees it live (open, or in the
  background while the turn runs); code sessions are also picked up from
  their history. Canvases drawn from other channels (Discord, Telegram, the
  web dashboard) are not captured.
- **Automation**: the daemon's scheduled jobs, as on the web dashboard's Cron
  page. Create shell or agent jobs with a cron schedule and timezone, a
  model, session, allowed tools and memory for agent jobs, and delivery to
  one of the agent's channels. Edit any of it later, run a job now, pause and
  resume it, delete it, and read each run's status, duration and full
  output. The scheduler's own switches are there too (they apply after the
  daemon restarts). Jobs defined in `config.toml` are shown read-only, and
  its Home shortcut can be hidden. **Automation needs a patched daemon**: see
  [Automation: the cron patch](#automation-the-cron-patch). If you don't
  want to patch the daemon, don't use Automation; hide its card and nothing
  else changes.
- **Doctor**: run ZeroClaw's own checks (`zeroclaw doctor`) from the phone
  and read the findings grouped by category, filtered by errors, warnings
  and passes. A finding about a channel or a model provider has a Fix button
  that opens that entry in Config. Home shows the last run's result; the
  doctor never runs on its own, only when you ask (Doctor on Home, or
  Config → Doctor).
- **Approvals**: when an agent asks for permission, approve or deny from the
  Inbox or straight from the notification. Nothing is ever approved without
  your tap.
- **Runs in the background**: a running turn keeps its connection through a
  foreground service, so it is not cancelled when you switch apps.
- **Config**: every daemon setting, grouped and searchable, edited with the
  right control for each type (switches, lists, choices, numbers).
- **Secure pairing**: mutual TLS 1.3 with a client key that never leaves the
  Android Keystore, a pinned CA, and an encrypted bearer token. Pairing
  always asks you to compare a short code, so another app cannot pair
  silently.
- **Sign in with OIDC**: for daemons behind an identity provider, sign in
  like `zerocode login`, approving in the browser, with no pairing link. The
  app reminds you before the sign-in expires and renews it without
  interrupting a running turn.

## Screenshots

| | | |
|:-:|:-:|:-:|
| ![Home with the daemon status and the shortcuts list](docs/screenshots/home.jpg) | ![Home with scheduled jobs and pinned agents](docs/screenshots/home-agents.jpg) | ![The list of chats](docs/screenshots/chats.jpg) |
| Home | Up next and pinned agents | Chats |
| ![A chat streaming tool calls](docs/screenshots/chat-working.jpg) | ![A tool call opened with its arguments and output](docs/screenshots/tool-call.jpg) | ![Picking an agent for a new chat](docs/screenshots/new-chat.jpg) |
| A turn running | Tool call details | New chat |
| ![The chat menu with the model, display options and actions](docs/screenshots/chat-menu.jpg) | ![Choosing the folder for a code session](docs/screenshots/folder-picker.jpg) | ![The web fetch settings](docs/screenshots/config-web-fetch.jpg) |
| Chat menu | Choose a folder | Editing a setting |

<details>
<summary>Pairing and sign-in</summary>

| | | |
|:-:|:-:|:-:|
| ![The welcome screen with the pairing and OIDC options](docs/screenshots/onboarding.jpg) | ![Confirming the pairing code](docs/screenshots/pair-confirm.jpg) | ![The paired daemon, its certificate and the Home shortcut switches](docs/screenshots/pairing-settings.jpg) |
| Welcome | Compare the code | Paired daemon |
| ![The OIDC sign-in form with the advanced WSS and gateway URLs](docs/screenshots/oidc-sign-in.jpg) | ![The This phone section with the Unpair this phone button](docs/screenshots/unpair.jpg) | |
| Sign in with OIDC | Unpair this phone | |

</details>

### Workflows

| | | |
|:-:|:-:|:-:|
| ![The list of workflows with their triggers, step count and last run](docs/screenshots/workflows.jpg) | ![A workflow's flow with branches from the first step](docs/screenshots/workflow-flow.jpg) | ![A ten-step workflow zoomed out, with branches merging and a failure path](docs/screenshots/workflow-overview.jpg) |
| Workflows | The flow | The whole workflow |
| ![A step sheet with its kind, instructions, connections and branches](docs/screenshots/workflow-step.jpg) | ![Choosing what happens when a step fails](docs/screenshots/workflow-on-failure.jpg) | ![Tapping a step to connect a failure path](docs/screenshots/workflow-connect.jpg) |
| Editing a step | If a step fails | Tap to connect |
| ![Inserting the output of earlier steps into the instructions](docs/screenshots/workflow-instructions.jpg) | ![Workflow settings with the execution mode, agent, priority and triggers](docs/screenshots/workflow-settings.jpg) | ![Running a workflow with optional input](docs/screenshots/workflow-run.jpg) |
| Outputs of earlier steps | Settings and triggers | Run |

### Canvas

| | | |
|:-:|:-:|:-:|
| ![The list of saved canvases with their type, frame count and agent](docs/screenshots/canvas-list.jpg) | ![A bar chart an agent drew, opened from the list](docs/screenshots/canvas-chart.jpg) | |
| Saved canvases | A chart an agent drew | |

### Automation

| | | |
|:-:|:-:|:-:|
| ![The list of scheduled jobs with their agent, type, schedule, status and next run](docs/screenshots/automation-list.jpg) | ![A new shell job with its name, agent, schedule and command](docs/screenshots/automation-shell-job.jpg) | ![A new agent job with its prompt, model, session, tools, memory and delivery to a channel](docs/screenshots/automation-agent-job.jpg) |
| Scheduled jobs | A shell job | An agent job with delivery |
| ![The scheduler settings sheet](docs/screenshots/automation-scheduler.jpg) | | |
| Scheduler settings | | |

### File edits

| | | |
|:-:|:-:|:-:|
| ![An agent's file_edit shown as a diff: one line removed in red, one added in green, with the file name and +1 -1](docs/screenshots/code-edit-diff.jpg) | ![A new file written by the agent, every line added in green](docs/screenshots/code-file-write.jpg) | |
| An edit as a diff | A new file | |

### Doctor

| | | |
|:-:|:-:|:-:|
| ![Doctor results: one error, two warnings and 151 checks OK, with Fix buttons on the config findings](docs/screenshots/doctor.jpg) | ![Doctor running its checks again after the fixes, with one warning left](docs/screenshots/doctor-running.jpg) | ![All 142 checks passed](docs/screenshots/doctor-passed.jpg) |
| Findings with Fix | Running the checks | All checks passed |

## Install

You need Android 10 or newer and a ZeroClaw daemon, version 0.9.0 or newer,
with its RPC plane (WSS) enabled, plus either its enrollment endpoint (to pair
with a link) or an OIDC provider (to [sign in](#sign-in-with-oidc)).

Download `zerodroid-X.Y.Z.apk` from the
[latest release](https://github.com/SyscallBrain/zerodroid/releases/latest)
and open it on the phone. Android asks you to allow installs from your
browser or file manager the first time. `SHA256SUMS` lists the checksum of
the APK, and every release carries signed build provenance:

```sh
sha256sum -c SHA256SUMS
gh attestation verify zerodroid-X.Y.Z.apk --repo SyscallBrain/zerodroid
```

To build it yourself, see [CONTRIBUTING.md](CONTRIBUTING.md).

### Keeping your sessions: the ZeroClaw patch

Everything in ZeroDroid except Automation works with an unmodified ZeroClaw
0.9.0, with one catch: **chats and code sessions are kept only if the daemon
has the patch below.** Without it, the sessions you started from the phone disappear from
the app every time the daemon restarts, in both the Chats and the Code tabs.

The daemon gives a remote client only the sessions it owns, and it keeps
that ownership in memory. When the daemon restarts, the ownership is lost:
your sessions are still in the daemon's store, but the daemon no longer
lists them for ZeroDroid and refuses to reopen them.

The fix is a small patch to ZeroClaw, in two commits: one for chats and one
for code (ACP) sessions. It records which remote client created each session
and lets that same client list and resume it while no one else has it open.
The patch is not part of an official ZeroClaw release yet. It lives in the
[`zerodroid/remote-durable-session-owner`](https://github.com/SyscallBrain/zeroclaw/tree/zerodroid/remote-durable-session-owner)
branch on my fork, on top of ZeroClaw's current `master`. You need both
commits: a daemon with only the chat one keeps your chats but still loses
your code sessions.

If you run the daemon in Termux on an Android phone, you can build
[`android-master-zerodroid`](https://github.com/SyscallBrain/zeroclaw/tree/android-master-zerodroid)
instead. It is ZeroClaw's `master` with the same two commits and the two
other patches below already merged in.

In Termux, use a daemon built from ZeroClaw's `master` from 23 November 2026
or later. Older builds, the 0.9.0 release included, can't run the shell
tool there because Android's SELinux blocks resolving `/system/bin/sh`.
ZeroClaw fixed that upstream in
[#12080](https://github.com/zeroclaw-labs/zeroclaw/pull/12080), so it no
longer needs a patch of its own.

Build the daemon from either branch as you would build ZeroClaw. The patch
only adds a column to each session store, so you can go back to an official
release at any time; you lose nothing but the ownership, and the sessions
started from the phone stop showing up again after the next restart.

### Automation: the cron patch

Automation is the only feature that needs a second patch, and you need it
only if you want to use Automation. Everything else in the app works without
it.

ZeroDroid talks to the daemon over RPC, and ZeroClaw's RPC can't do what the
web dashboard does over the HTTP gateway: its `cron/add` only creates shell
jobs, and `cron/patch` can't pause or resume a job or change its delivery,
model, session or tools. The
[`zerodroid/cron-rpc-parity`](https://github.com/SyscallBrain/zeroclaw/tree/zerodroid/cron-rpc-parity)
branch adds all of that, on top of `master`. Creating an agent job still
needs an admin pairing, as on the gateway. `android-master-zerodroid`
already includes this patch, so a Termux build from that branch has both.
The patch changes no stored data: the jobs database is the same with or
without it.

On an unpatched daemon the Automation screens still list your jobs and their
runs, and you can run a job now, edit its name, schedule and command, and
delete it. Anything that needs the patch is refused with a message saying
the daemon needs updating, and the app never saves something other than what
you asked for. If you'd rather not patch the daemon, simply don't use
Automation, and hide it from Home in Config → ZeroDroid & pairing →
Home → Automation.

### CPU reading in Termux: the process-stats patch

You need this patch only if the daemon runs in Termux on a phone without
root. On a server, a desktop or a rooted phone, the CPU tile works with an
unmodified daemon.

ZeroClaw works out its own CPU usage from the system-wide times in
`/proc/stat`. Android 8 and later deny that file to apps, Termux included,
so an unpatched daemon finds no CPUs: the Home CPU tile then stays at 0 %
whatever the daemon is doing, and its caption reads "all cores" instead of
the core count. The
[`zerodroid/android-process-cpu`](https://github.com/SyscallBrain/zeroclaw/tree/zerodroid/android-process-cpu)
branch falls back, only when `/proc/stat` can't be read, to the daemon's
own CPU time in `/proc/self/stat` measured against the clock, and to the
number of CPUs the process may run on. `android-master-zerodroid` already
includes this patch. It changes no stored data.

## Pairing

The phone needs two things from the daemon: a client certificate from the
enrollment endpoint and a bearer token from the gateway.
[`tools/pair-phone.sh`](tools/pair-phone.sh) gets both on the machine that
runs ZeroClaw and hands them to the app in a single `zerodroid://pair` link.

**Daemon in Termux on the same phone.** Run the script in Termux; it opens
ZeroDroid with everything filled in:

```sh
tools/pair-phone.sh
```

**Daemon on another machine.** Print the link and get it to the phone, then
use *Paste pairing link* or *Type it* in the app. Set `ZERODROID_HOST` to an
address the phone can reach, such as the machine's Tailscale IP or MagicDNS
name (it must also be in the daemon's `[wss].sans`):

```sh
ZERODROID_HOST=my-server.tailnet.ts.net tools/pair-phone.sh --mode print
```

The app then shows a short code. Pair only if it matches the one the script
printed. The link carries a long-lived token: do not screenshot or share it.

`tools/pair-phone.sh --help` lists the options (ports, data directory,
device name).

### Sign in with OIDC

If the daemon's operator set up an identity provider, ZeroDroid can sign in
the way `zerocode login` does (ZeroClaw v0.9.0 or later), with no pairing link.
Tap *Sign in with OIDC*, enter the daemon host and the provider alias (for
example `corp`), and approve the sign-in in the browser. *Advanced* takes a
custom WSS URL (default `wss://<host>:9781/`) and gateway URL (default
`https://<host>:42617`, or the HTTPS URL of the proxy in front of it). Plain
`http://` is accepted only for a gateway on the phone itself (`127.0.0.1`),
such as a daemon in Termux.

The daemon needs, as for `zerocode login`:

- an `[oidc.<alias>]` provider with the device authorization grant enabled at
  the identity provider;
- a permission mapping for the user. Sign-in itself needs `sessions:create`
  and at least one allowed agent, but the app also reads the daemon's status,
  agents, costs, SOPs and config: with only `sessions` granted, most screens
  say the device is not allowed. ZeroDroid expects operator-level access
  (read on those resources, or `admin = true`);
- WSS enabled, with the host the phone uses in `[wss].sans`;
- the gateway reachable over HTTPS. If Android does not trust its certificate,
  the app shows the SHA-256 fingerprint and pins that exact certificate once
  you accept it.

ZeroClaw does not hand out refresh tokens, so ZeroDroid asks you to renew the
sign-in five minutes before the access token expires (sooner for very short
tokens), and asks again by notification if an agent is working while the app
is in the background. Renewing re-verifies the new token on the open
connection, so a running turn keeps going; if the token runs out, the app
disconnects and waits for you to sign in again. With token introspection the
daemon also asks clients to re-verify every `revalidation_secs` (60 s by
default); ZeroDroid does that on its own, without interrupting you. Give the client an access
token lifetime of **30 to 60 minutes**: with Keycloak's 5-minute default you
would be asked every few minutes.

To retire a phone, revoke its device on the daemon:
`zeroclaw security revoke-client-cert --device <id>` (the device ID is in
*Config → ZeroDroid & pairing*).

## How it works

ZeroDroid speaks the daemon's JSON-RPC protocol over WebSocket with TLS 1.3
and a client certificate (port 9781 by default). On first use it creates a
P-256 key inside the Android Keystore, enrolls a certificate with the
one-time code (port 9782), pins the daemon's CA and stores the token
encrypted with a Keystore key. With OIDC, the gateway relays the identity
provider's device grant (with PKCE) and signs the certificate instead, and the
token is the provider's access token, sent with `auth_provider = "oidc.<alias>"`.

A turn on the daemon belongs to the connection that started it, so the app
keeps that connection alive in a foreground service while a turn or an
approval is pending. Samsung and some other vendors freeze background apps
anyway; turning off battery optimisation for ZeroDroid (Config → ZeroDroid &
pairing) helps.

## Contributing

Bug reports, ideas and pull requests are welcome. Read
[CONTRIBUTING.md](CONTRIBUTING.md) for how to build and test, and
[SECURITY.md](SECURITY.md) to report a vulnerability privately.

ZeroDroid is an independent project and is not affiliated with ZeroClaw Labs.

## License

[MIT](LICENSE) © 2026 Tiago Correia. The bundled Inter and JetBrains Mono
fonts are under the SIL Open Font License ([docs/licenses](docs/licenses)).
