# lan-control

**lan-control** is a local-first Python CLI (and OpenClaw agent skill) for people who want to control smart home devices on their LAN without a cloud account or a Home Assistant server: it discovers devices through your router's DHCP table (SSH) or the local ARP cache, identifies them with community YAML profiles, and controls LG webOS TVs, BroadLink IR remotes (incl. IR air conditioners), Android TV boxes and OpenWrt routers — with JSON output for AI agents.

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg?style=flat-square)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-green.svg?style=flat-square)](https://www.python.org)
[![OpenClaw Skill](https://img.shields.io/badge/OpenClaw-Skill-blue.svg?style=flat-square)](https://github.com/openclaw/openclaw)

## 中文简介

lan-control 是一个本地优先、无需云端的局域网设备发现与智能家居控制命令行工具，同时也是 AI Agent 技能（OpenClaw skill）。它通过路由器 SSH 读取 DHCP 租约（或本机 ARP 兜底）发现局域网设备，用社区维护的 YAML 档案识别设备，并支持 OpenWrt 路由器、LG 电视遥控（webOS）、BroadLink 红外遥控、空调红外控制，以及通过 ADB 控制安卓电视盒。`control` 命令输出 JSON，方便 AI Agent 调用。

---

## Table of Contents

- [Highlights](#highlights)
- [Requirements](#requirements)
- [Quick Start](#quick-start)
- [Usage examples](#usage-examples)
- [Supported Devices](#supported-devices)
- [Built-in Commands](#built-in-commands)
- [Add Your Device](#add-your-device)
- [How It Works](#how-it-works)
- [When to use lan-control (vs. alternatives)](#when-to-use-lan-control-vs-alternatives)
- [FAQ](#faq)
- [Anti-patterns We Handle](#anti-patterns-we-handle)
- [Documentation](#documentation)
- [License](#license)

---

## Highlights

- **Universal** — Not tied to any router brand or SSH. Controls OpenWrt / GL.iNet routers over SSH, detects several other router brands, and still lists devices without router access (ARP fallback).
- **Multi-method discovery** — Router SSH (DHCP leases) → local ARP fallback. nmap / mDNS / UPnP are planned.
- **Zero config** — Auto-discovers your router and devices. No manual IP entry.
- **YAML-driven** — Each device type is a `.yaml` file. Adding support = adding a file. No code changes.
- **Community-driven** — MAC prefix + hostname pattern matching. Drop a YAML, submit a PR, done.
- **Local-first** — Runs on your Mac/Linux. No cloud, no VPS, no account. Your router, your data.
- **Agent-ready** — `discover`, `connect`, `devices` and `control` print JSON to stdout; human-readable logs go to stderr.

## Requirements

- Python 3.8+ and `pyyaml` (`pip install -r requirements.txt`)
- System tools used by the scripts: `ssh`, `nc`, `curl`, `ping`, `arp`
- Optional: `adb` (Android TV boxes), `expect` or `sshpass` (router password login), `cryptography` or the `openssl` CLI (BroadLink encryption)
- macOS and Linux (the scripts have `Darwin` and `Linux` branches)

## Quick Start

```bash
git clone https://github.com/ythx-101/lan-control.git
cd lan-control
pip install -r requirements.txt
```

```bash
python3 cli.py discover                    # Find your router
python3 cli.py connect                     # SSH into router (auto key/password)
python3 cli.py devices                     # List all LAN devices
python3 cli.py commands lg-webos           # Show available commands
python3 cli.py control openwrt uptime      # Execute command on device
python3 cli.py health                      # Router health check
```

Illustrative output (IPs are placeholders; `discover` and `devices` print their human-readable log to stderr, JSON to stdout):

```
$ python3 cli.py discover
🔍 Default gateway: 192.168.1.1
📡 Local IP: 192.168.1.50
🔑 SSH: open (SSH-2.0-dropbear)
🌐 HTTP: open (title: ...)

✅ Router discovered: 192.168.1.1 (<model>)

$ python3 cli.py devices
📱 4 devices found:
  📺 192.168.1.100  LGwebOSTV            LG
  🎛️ 192.168.1.101  BroadLink-Remote    BroadLink
  ...

$ python3 cli.py commands lg-webos
# LG webOS TV (LG)
Protocol: ssap
Connection: websocket:3001

## Commands:
  power_off
    Power off
  ...
  volume_up
    Volume +
  ...
  set_volume
    Set volume (0-100)
    Params: ['volume']
  ...
```

`commands lg-webos` lists 39 commands in total.

## Usage examples

```bash
# Router (OpenWrt over SSH)
python3 cli.py control openwrt uptime
python3 cli.py control openwrt dhcp_leases

# LG webOS TV — the first command asks you to confirm pairing on the TV
# (see the docstring in drivers/ssap.py)
python3 cli.py control lg-webos set_volume 20
python3 cli.py control lg-webos launch_app <app_id>

# BroadLink: learn an IR code (press the remote button within 15 s), then send it
python3 cli.py control broadlink-rm4 learn tv_power
python3 cli.py control broadlink-rm4 send tv_power

# IR air conditioner, routed through the BroadLink RM4 via the `bridge` field
python3 cli.py control generic-ir-ac power_on

# From an agent: JSON on stdout, logs on stderr
python3 cli.py control openwrt uptime 2>/dev/null | jq .ok
```

## Supported Devices

| Type | Devices | Protocol | Control | Status |
|------|---------|----------|---------|--------|
| **Router** | OpenWrt, GL.iNet | SSH | `ssh` driver | ✅ Verified |
| **Router** | ASUS Merlin, TP-Link, Xiaomi, Ubiquiti | Detected by `discover` (HTTP title); control via `ssh` if the router allows SSH | — | 🔍 Detect only |
| **TV** | LG webOS | WebSocket (SSAP) | `ssap` driver | ✅ Verified |
| **TV** | Samsung Tizen, Roku | HTTP | planned | 📝 Planned |
| **IR Remote** | BroadLink RM4 / RM Mini | UDP (AES-128) | `broadlink` driver | ✅ Verified |
| **Android Box** | H616/H618/S905/RK3566 | ADB/SSH | `adb` driver | ✅ Verified |
| **E-ink** | ESP32 displays (Waveshare, LilyGo, TRMNL) | HTTP | `http` driver | ✅ Profile |
| **Speaker** | Google Nest, Amazon Echo | Cast/HTTP | planned | 📝 Planned |
| **Camera** | Reolink, Hikvision | HTTP | `http` driver | 📝 Planned |
| **AC** | Generic IR (bridged via BroadLink) | IR Bridge | `broadlink` driver | ✅ Profile |
| **IoT** | ESP/Tuya, Tasmota | HTTP/MQTT | `http` driver | 📝 Planned |

> **✅ Verified** = tested on real hardware with working driver. **✅ Profile** = YAML profile exists, driver in progress. **🔍 Detect only** = recognized by `discover`, no device profile. **📝 Planned** = PRs welcome.

## Built-in Commands

| Command | Description |
|---------|-------------|
| `discover` | Auto-detect router (gateway → fake-IP check → SSH/HTTP probe) |
| `connect [password]` | SSH into router (key → password → defaults, auto-fallback) |
| `devices` | Scan LAN devices (SSH DHCP → ARP fallback) |
| `supported` | List all supported device types from YAML profiles |
| `commands <device>` | List available commands for a device type |
| `control <device> <cmd> [params]` | **Execute command on a device** (SSH/ADB/HTTP/SSAP/BroadLink) |
| `health` | Router health (memory, WireGuard, DNS, device ping) |
| `ping <ip\|hostname>` | Check if a device is online |

## Add Your Device

Your device isn't listed? **5 minutes:**

### 1. Create a YAML file

```yaml
# devices/tv/my-smart-tv.yaml
device:
  name: "My Smart TV"
  type: tv
  vendor: MyBrand
  protocol: http

discovery:
  mac_prefixes:
    - "aa:bb:cc"           # First 3 bytes of MAC
  hostname_patterns:
    - "(?i)mysmartv"       # Regex for DHCP hostname

connection:
  method: http
  port: 8080

commands:
  power_off:
    description: "Power off"
    action: "POST /api/power/off"
  volume_up:
    description: "Volume +"
    action: "POST /api/volume/up"
```

### 2. Test

```bash
python3 cli.py supported    # Your device should appear
```

### 3. Submit PR

That's it. The registry auto-scans all YAML files in `devices/`.

## How It Works

### Discovery Methods (auto-fallback)

| Method | Status | Needs Router SSH? | What you get | Best for |
|--------|:-:|:-:|-------------|----------|
| **SSH DHCP scan** | ✅ Implemented | ✅ | All devices with MAC + hostname + IP | OpenWrt, GL.iNet |
| **ARP table** | ✅ Implemented | ❌ | Devices your machine has talked to (MAC + IP) | Any network, no router access |
| **nmap scan** | 📝 Planned | ❌ | — | — |
| **mDNS/Bonjour** | 📝 Planned | ❌ | — | — |
| **UPnP/SSDP** | 📝 Planned | ❌ | — | — |
| **Router HTTP API** | 📝 Planned | ❌ | — | — |

> **No SSH? No problem.** lan-control tries router SSH first (most complete data), then falls back to the local ARP cache. You get MAC + IP, but no hostnames.

### Architecture

```
lan-control
   │
   ├── SSH → router DHCP table     (best: full MAC + hostname)
   ├── ARP → local ARP cache       (good: MAC + IP)
   ├── nmap → subnet scan           (planned)
   ├── mDNS → service discovery     (planned)
   └── UPnP → SSDP broadcast       (planned)
   │
   ▼
MAC prefix + hostname → match devices/*.yaml
   │
   ▼
Identified devices → native protocol commands
   📺 LG TV      → WebSocket (SSAP)
   🎛️ BroadLink  → UDP (AES-128-CBC)
   ❄️ IR AC      → bridged through BroadLink
   📷 Camera     → HTTP API (planned)
   📦 Android    → ADB
```

```
devices/             ← Community contributes HERE
  router/            openwrt.yaml
  tv/                lg-webos.yaml          (Samsung Tizen, Roku: planned)
  ir-remote/         broadlink-rm4.yaml
  ac/                generic-ir-ac.yaml     (bridged through BroadLink)
  speaker/           (empty, planned: Google Nest, Amazon Echo)
  camera/            (empty, planned: Reolink, Hikvision)
  iot/               android-tv-box.yaml, eink-display.yaml
  _schema.yaml       Template for new devices
drivers/             ← Protocol implementations
  ssh.py             OpenWrt / Linux shells
  adb.py             Android TV boxes
  http.py            REST / webhook devices
  ssap.py            LG webOS over WebSocket (pair → store key)
  broadlink.py       BroadLink RM4 UDP (AES-128-CBC)
registry.py          ← Auto-scans devices/
cli.py               ← CLI entry point
scripts/             ← Shell scripts (discover, connect, health)

~/.lan-control/      ← User-local state (never committed)
  state.json         Discovered devices from last `devices` run
  secrets.yaml       LG webOS client-keys, chmod 0600
  ir_codes/          Learned IR codes, one JSON per device
```

## When to use lan-control (vs. alternatives)

- **vs Home Assistant** — Home Assistant is a full, always-on home automation platform (UI, many integrations). lan-control is a CLI that needs no resident service, suited to scripts, AI agents and ad-hoc LAN troubleshooting.
- **vs single-protocol libraries** (e.g. python-broadlink, webOS client libraries) — those focus on one protocol. lan-control puts discovery, identification and multi-protocol control behind one command line, extended through YAML. Its SSAP and BroadLink drivers are its own implementations and do not depend on those libraries.
- **Not a fit for** automation rules, a graphical UI, cloud remote access, or Zigbee / Z-Wave.

## FAQ

**How do I find all devices on my home network from the command line? / 怎么在命令行列出家里局域网的所有设备？**
Run `python3 cli.py discover` then `python3 cli.py devices`. Devices come from the router's DHCP leases over SSH, or from the local ARP cache.

**Does it work without SSH access to my router?**
Yes. `devices` falls back to the local ARP table, which gives MAC + IP only (no hostnames).

**How do I control an LG webOS TV from Python/CLI? What about first-time pairing?**
`python3 cli.py control lg-webos <command>`. On first use the TV asks you to confirm pairing on screen; the client-key is stored in `~/.lan-control/secrets.yaml` (file mode 0600).

**Can I control an IR air conditioner?**
Yes, through a BroadLink RM4: learn the IR codes with `control broadlink-rm4 learn <name>`, then use the `generic-ir-ac` profile, whose `bridge` field routes commands via the BroadLink's IP.

**How do I add support for a new device?**
Write one YAML file under `devices/<type>/` — see [Add Your Device](#add-your-device) and [references/contributing.md](references/contributing.md).

**Where is data stored? Does it send anything to the cloud?**
State lives only on your machine in `~/.lan-control/` (`state.json`, `secrets.yaml`, `ir_codes/`). The code makes no cloud calls; it talks to your router and devices on the LAN.

**Is it safe?**
Use it only on networks you own. `connect` tries SSH key auth first, then a password you provide, then a few common default passwords; its SSH calls use `StrictHostKeyChecking=no`, so host keys are not verified. Keep this in mind before running it on an untrusted network.

**Can an AI agent use it?**
Yes. It is an OpenClaw skill (see [SKILL.md](SKILL.md)), and `control` prints JSON to stdout.

## Anti-patterns We Handle

| Trap | What happens | Solution |
|------|-------------|----------|
| Clash/Surge fake IP | Gateway shows 198.18.0.1 (TUN) | Auto-detect fake-ip range, find real gateway |
| ISP port blocking | WireGuard on 51820 silently fails | Documented in troubleshooting.md |
| Double NAT | Router WAN is private 192.168.x.x | Documented in troubleshooting.md |
| Router OOM | Services crash with <512MB RAM | Documented in troubleshooting.md |
| Dropbear SSH | Different auth flow than OpenSSH | Multi-method auth (key → password → defaults) |

## Documentation

- [Contributing Guide](references/contributing.md)
- [Device Schema](references/device-schema.md)
- [Router Profiles](references/router-profiles.md)
- [Troubleshooting](references/troubleshooting.md)

## License

[Apache-2.0](LICENSE)
