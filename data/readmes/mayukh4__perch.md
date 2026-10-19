# Perch

A quiet instrument for your desk. It shows the handful of things you actually
want at a glance, and it has one button you press to talk to whatever AI you
already own.

Built on a Raspberry Pi 5 and a 7-inch touchscreen — and not fussy about
either: any Linux board that can drive a screen runs it, an older Pi, an
Orange Pi, a Rockchip box ([docs/OTHER_BOARDS.md](docs/OTHER_BOARDS.md)).
Arrange it from your laptop; the screen on your desk updates as you drag.

[![ci](https://github.com/mayukh4/perch/actions/workflows/ci.yml/badge.svg)](https://github.com/mayukh4/perch/actions/workflows/ci.yml)
[![release](https://img.shields.io/github/v/release/mayukh4/perch)](https://github.com/mayukh4/perch/releases)
[![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![discussions](https://img.shields.io/badge/community-discussions-1b1d20)](https://github.com/mayukh4/perch/discussions)

<!-- HERO: replace with the real photo of the device on the desk before flipping public.
<img src="docs/media/hero.jpg" alt="Perch on a desk at night" width="100%">
-->

| Day | Night |
|---|---|
| ![The panel by day](docs/media/instrument-day.png) | ![The panel at night](docs/media/instrument-night.png) |

*Real screenshots from the panel — the same instrument under different
light. It follows the sun, and the physical backlight follows it.*

---

## Watch the build

[![I Built a Raspberry Pi Desk Display That Actually Talks Back!](https://i.ytimg.com/vi/us_HFad-EFI/maxresdefault.jpg)](https://youtu.be/us_HFad-EFI)

**▶ [I Built a Raspberry Pi Desk Display That Actually Talks Back!](https://youtu.be/us_HFad-EFI)** —
the whole build start to finish, from a bare Pi to a desk that answers back.
Dead ends included, because that is where the learning is.

---

## What it is

- **A widget grid**, on a screen with no notifications, no browser and no feed
- **A talk button** that reaches your endpoint — OpenAI, Anthropic, Groq,
  Ollama, LM Studio, a webhook, or an agent with a command line
- **A config app** on your phone or laptop, where you drag tiles around and
  watch the desk screen follow
- **A widget folder** that is genuinely one folder: a manifest, a component,
  and about forty lines

It follows the sun — the palette inverts at dusk and the panel's actual
backlight comes down with it, because a desk display at full brightness in a
dark room is the main reason these things end up unplugged.

## Looks

The palette is a choice. Four looks ship, each with its own day and night,
switchable live from the console — and
[making your own is one CSS block](docs/DESIGN.md#looks), no code.

| Phosphor | Ledger | Meridian |
|---|---|---|
| ![Phosphor at night](docs/media/phosphor-night.png) | ![Ledger at night](docs/media/ledger-night.png) | ![Meridian at night](docs/media/meridian-night.png) |

## What it is not

Not low-power. It is plugged into the wall, it is bright, and it needs a
real Linux board.
If you want a thing that sips a battery for six months on a shelf, buy an
e-ink display — that is a different product and neither is wrong.

How it sits next to the things you might be choosing between, honestly:

| | Perch | MagicMirror² | TRMNL | a wall tablet |
|---|---|---|---|---|
| Screen | colour, touch | usually no touch | e-ink, 1-bit | colour, touch |
| Voice → your own AI | yes — any endpoint, incl. local | via modules | no | an assistant, theirs |
| Refresh | live (WebSocket) | live | minutes | live |
| Power | wall | wall | months on battery | wall |
| Config | web console, drag | config file | web, hosted or BYOS | per app |
| Cost past the Pi | a screen (~$60) | a screen | $139 device | an old tablet |

If "months on a battery" or "e-paper on a shelf" is what you want, buy the
TRMNL — it is good at exactly that. Perch is for the desk you sit at all
day, in colour, that you can touch and talk to.

---

## Install

On a Raspberry Pi with a display attached:

```bash
git clone https://github.com/mayukh4/perch && cd perch
bash install/install.sh
```

That builds it, installs a service, sets up the kiosk browser, adds a `perch`
command and a desktop icon, and tells you the address of the console. Reboot
and the screen comes up on its own — dark, and then at whatever brightness the
hour calls for, rather than flashing white at you for half a minute first.

Requires **Node 22 or newer** and about 1.5 GB free. The installer checks
both and stops with a useful message rather than halfway through.

Then open **`http://<your-pi>.local/console`** from anything on your network.
No port: Perch binds 80 as well as 7878 when the system lets it, and falls
back quietly when it cannot. Use the `.local` name rather than the IP — if you
run a VPN, and Tailscale in particular, the IP is the one that gets
intercepted. See [docs/KIOSK.md](docs/KIOSK.md) if a browser cannot reach it
but `curl` can.

**If you do not know the address**, the screen does. Hold the connection dot
on the left of the panel and it shows its own console address as a QR code —
point a phone at it. Over SSH there is `perch url`, and `perch status` for
whether the thing is running at all.

The installer also leaves a **Perch icon** on the device's desktop. Most
people will never need it, because the kiosk restarts itself; it is for the
day it does not, when a screen with no keyboard needs something to press.

Clock, weather and news work immediately with **no keys and no accounts**, so
a fresh clone shows something real on first boot.

Perch has no login — it is a desk device that trusts your LAN, refuses
requests from anywhere that does not look like your LAN, and must never be
port-forwarded to the internet. The kiosk also pre-grants itself microphone
access (it has no keyboard to click "Allow" with) and the installer makes
the panel backlight writable so night mode can dim the real hardware. The
whole model is written down in [SECURITY.md](SECURITY.md).

## Hardware

| | |
|---|---|
| Board | Raspberry Pi 5 (a 4 works; a 3 will be slow) — or any Linux SBC with a screen: [docs/OTHER_BOARDS.md](docs/OTHER_BOARDS.md) |
| Display | 7-inch 800×480 MIPI DSI touchscreen — the common Freenove and Waveshare panels |
| Audio | Any USB speaker and USB microphone, for the talk button |

Verified on Raspberry Pi OS 13 (trixie), Wayland + labwc, Chromium 144. The
installer automates Pi OS; on other boards the same app runs with one manual
kiosk step, written down in [docs/OTHER_BOARDS.md](docs/OTHER_BOARDS.md).
Other resolutions work — the grid is proportional and the console's preview
uses whatever size the panel reports.

---

## The widgets

| | needs |
|---|---|
| **Clock** | nothing — time, date, a second timezone, and a calendar that needs no account |
| **Weather** | nothing — Open-Meteo, no account |
| **News** | nothing — any RSS or Atom URL |
| **Machines** | nothing for this Pi; a one-line agent on any other box |
| **YouTube** | a Data API key, or your own Google account for revenue |
| **Home Assistant** | your address and a long-lived token — it finds the house itself ([docs](docs/HOMEASSISTANT.md)) |
| **Custom** | a URL — a Grafana panel, a camera feed, a page you wrote |
| **Stripe** | a restricted, read-only key — your income on the desk ([docs](widgets/stripe/README.md)) |

The YouTube widget shows any public channel with an API key. Your own revenue
and 28-day numbers need a Google account, which is five minutes once:
**[docs/YOUTUBE.md](docs/YOUTUBE.md)** walks it end to end, including the two
places Google makes it stranger than it should be.

### Making your own

A widget is one folder on your own device — a manifest, a component, about
forty lines. No repo, no publishing, nothing to sign up for: drop a folder
in `widgets/`, run `npm run registry`, and it is on your desk.

The fastest way is to not write it yourself. Paste this to Claude Code,
codex, or whatever agent lives in your terminal, from a Perch checkout:

```
Read docs/WIDGETS.md, then widgets/weather/ as a worked example.
Create widgets/<id>/ that shows <the thing you want on your desk>.
Run npm run registry && npm run typecheck and fix anything they flag.
```

The manifest generates the settings UI and the contract is complete, so an
agent gets it right in one or two passes — the Stripe widget in the table
above started life exactly this way.

### Sharing it

If a widget is worth other desks having, put it in its own repo (start
from the **[widget template](https://github.com/mayukh4/perch-widget-template)**)
and list it in **[perch-widgets](https://github.com/mayukh4/perch-widgets)**
with one JSON file — your repo, your name, your license, no review queue.
Next in-tree, and open if you want them:
[Now Playing and Calendar](https://github.com/mayukh4/perch/issues).

## Other machines

Anything running the agent shows up on the screen:

```bash
curl -fsSL http://your-pi.local:7878/agent.sh | \
  PERCH_URL=http://your-pi.local:7878 PERCH_TOKEN=... PERCH_INSTALL=1 sh
```

POSIX shell, no dependencies past `curl`. It reports CPU, memory, disk and
temperature every thirty seconds, opens no ports and accepts no commands.
The console shows you the exact line with your token in it.

## The AI

Two settings, deliberately separate: what transcribes you, and what answers.
Every question carries a digest of what is on the screen, which is what makes
"what's the weather doing, and how hot is the Pi?" work with a model that has
no tools.

An 0.6B model on the Pi itself answers that in about nine seconds, with
nothing leaving the house. A cloud endpoint answers in under two. Same
device, one field.

Details, and the reason `exec` is off by default, in [docs/AI.md](docs/AI.md).

### Already have an agent?

If Hermes, OpenClaw, Claude Code or codex is already running somewhere — this
Pi, your desktop, a box in a datacentre — you do not port anything. Give it
this and it wires itself up:

```
Read https://perchondesk.com/connect.md and connect the agent running on
this machine to my Perch at http://perch.local:7878
```

[docs/CONNECT_AN_AGENT.md](docs/CONNECT_AN_AGENT.md) is written to be read by
an agent: the config shape, the two routes that write it, the host rules it
will trip over, and a test it has to pass before it can claim to be done. A
running Perch serves it at `/connect.md`, so the device hands out its own
instructions.

---

## How it is built

```
apps/kiosk      the screen            vite + react + ts
apps/console    the config app        vite + react + ts
packages/ui     tokens + primitives   the design system
packages/board  the grid              shared by both apps
server          one node process      hono + ws, port 7878
widgets         eight folders         the extensible part
```

One process, one port, no native dependencies, no database — config is JSON
you can read and hand-edit. `npm run dev` runs everything with hot reload;
`npm run deploy` rsyncs to the Pi and rebuilds there, which is the same path
a stranger takes so it breaks for you first.

## Docs

- [Writing a widget](docs/WIDGETS.md) — the contract, and the checklist
- [Design](docs/DESIGN.md) — tokens, type, and what each primitive is for
- [Pointing it at an AI](docs/AI.md) — providers, context, and the exec rules
- [Connecting your own agent](docs/CONNECT_AN_AGENT.md) — hand this to the agent
- [Running it on the Pi](docs/KIOSK.md) — kiosk setup, and what costs people days
- [Security](SECURITY.md) — the trust model: no login, LAN only, never port-forward

## Community

- **[Discussions](https://github.com/mayukh4/perch/discussions)** — setup
  questions, what you built, show your desk.
- **[perch-widgets](https://github.com/mayukh4/perch-widgets)** — the widget
  registry. Your widget, your repo, one JSON file to list it.
- **[Contributing](CONTRIBUTING.md)** — a widget is one folder; a look is one
  CSS block.
- **[perchondesk.com](https://perchondesk.com)** — the site, the parts list,
  and the build video.

Perch is free and stays free. If it earns a place on your desk, the
[Sponsor button](https://github.com/sponsors/mayukh4) keeps it moving —
and building a widget is worth more than money.

## Thanks

To the projects that walked this road first and generously in the open:
[MagicMirror²](https://github.com/MagicMirrorOrg/MagicMirror),
[InkyPi](https://github.com/fatihak/InkyPi),
[TRMNL](https://github.com/usetrmnl), and
[Home Assistant](https://github.com/home-assistant) — whose registry design
taught Perch's a few things.

## Licence

MIT. Archivo and JetBrains Mono are bundled under the SIL Open Font License;
their licences are in `packages/ui/fonts/`.
