<div align="center">

# NetSim — Browser-Based Network Simulator with a Cisco-Style CLI & On-Device AI Tutor

**Practice CCNA-level networking in your browser. No installs, no VMs, no license.**
Build a topology, configure routers and switches with real Cisco IOS-style commands, capture packets to Wireshark `.pcap`, and ask a built-in AI tutor *why* your lab isn't working.

[![Live Demo](https://img.shields.io/badge/Live_Demo-netsim--lab-2ea44f?style=for-the-badge&logo=googlechrome&logoColor=white)](https://netsim-lab.osc-fr1.scalingo.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

![CI](https://github.com/joxorsayan/netsim/actions/workflows/ci.yml/badge.svg)
![NetDevOps](https://github.com/joxorsayan/netsim/actions/workflows/netdevops.yml/badge.svg)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

[**🚀 Try the live demo**](https://netsim-lab.osc-fr1.scalingo.io) · [Features](#-features) · [Quickstart](#-quickstart) · [Automation](#-network-automation-netdevops) · [Architecture](#-architecture) · [AI tutor pipeline](#-ai-tutor--on-device-ml-pipeline) · [Why NetSim?](#-why-netsim)

![NetSim topology editor and Cisco-style CLI](docs/img/hero-cli.png)

</div>

---

## 📖 Overview

**NetSim** is an open-source, browser-based **network simulator** (a lightweight, web-native alternative to Cisco Packet Tracer / GNS3) for learning and teaching networking. The protocol behaviour — switching, routing, ARP, ICMP, DHCP, spanning tree — is modelled in pure Python, so the whole simulator runs as an ordinary web app with **zero installation**: open a URL and start configuring a router.

It covers a **CCNA-level** feature set (VLANs & 802.1Q trunking, STP, OSPF/EIGRP/RIP/BGP routing, DHCP, NAT/PAT, ACLs, IPv6 dual-stack, FHRP, EtherChannel) and ships with three things most free simulators lack: a **packet capture exporter** (`.pcap` for Wireshark), an **on-device AI tutor** that explains misconfigurations, and **labs-as-code with auto-grading**.

> **Keywords:** network simulator, Cisco Packet Tracer alternative, CCNA lab, OSPF/BGP/EIGRP, VLAN, spanning tree, packet capture, Wireshark, FastAPI, on-device LLM, WebGPU, transformers.js, network automation, NetDevOps, Python network automation, Jinja2 config templating, config-as-code, drift detection, intent-based networking, pyATS, Batfish.

## 🎯 Why NetSim?

Powerful simulators already exist (Cisco Packet Tracer, GNS3, EVE-NG). NetSim doesn't try to beat them on protocol fidelity — it targets a different niche:

- **Zero install, browser-native.** Packet Tracer needs a NetAcad account and a desktop install; GNS3/EVE-NG need heavy VMs and licensed IOS images. NetSim is a single URL — ideal for students, interviews, and quick "what does this command do?" checks.
- **An integrated AI tutor.** Most free simulators have no teaching layer. NetSim runs a fine-tuned LLM *in the browser* that explains *why* a lab is broken, grounded by a deterministic rules engine so the facts stay correct.
- **Labs-as-code + auto-grading.** Declarative topologies and grading checks make it a self-study and assessment tool, not just a sandbox.
- **Open source & hackable.** Read the engine, add a protocol, self-host it. The commercial tools are closed.

It's also a from-scratch demonstration that core networking — packet forwarding, OSPF/BGP/STP/VLAN/DHCP, a Cisco-style CLI, `.pcap` export — can be modelled cleanly in code and shipped end-to-end, alongside an applied-ML pipeline (dataset → fine-tuning → quantization → on-device deploy).

## ✨ Features

| | |
|---|---|
| 🖧 **Topology editor** | Drag-and-drop PCs, switches and routers; cable them; arrange visually. Live link-state colouring. |
| ⌨️ **Cisco IOS-style CLI** | Per-device console with prefix abbreviation (`conf t`, `int g0/0`), `?` context help, Tab-completion and command history. |
| 🔀 **Real simulation engine** | Discrete-event frame forwarding: MAC learning, flooding, VLAN isolation, 802.1Q tagging, **spanning tree** root election, longest-prefix L3 routing with **admin distance**, route redistribution, **DHCP DORA**, and IPv6 dual-stack reachability. |
| 📡 **Packet capture** | Every frame hop is logged, replayable, and exportable as a **`.pcap`** that opens directly in **Wireshark**. |
| 🤖 **AI tutor** | Ask *"why can't PC1 ping PC2?"* — it scans your live topology (interfaces down, subnet/area mismatch, missing gateway, duplicate IP) and explains the fix. Runs a fine-tuned LLM **on-device in your browser** (no API key), with a deterministic rules engine for ground truth. |
| 🎓 **Labs-as-code + auto-grading** | Export a lab to JSON, apply a spec (devices + links + config), and grade student configs against checks (`ping`, `route`, `interface_up`) for a 0–100 score. |
| 🔧 **Network automation (NetDevOps)** | A **Python SDK + CLI** that drives the sim like real gear: **Jinja2 config templating** from per-device vars, config **push**, **drift detection**, structured **intent** (YANG-ish), and **intended-state validation** (routes/reachability) — with a **CI pipeline** that fails on misconfig and an in-app **Automation** tab. |

### Supported CLI (highlights)

- **Interfaces & addressing:** `interface`, `ip address <ip> <mask>|dhcp`, `no shutdown`, `ip helper-address`
- **Switching:** `switchport mode access|trunk`, `switchport access vlan`, `switchport trunk native vlan`, `vlan`, `spanning-tree [vlan N] priority`
- **Routing:** `ip route`, `router ospf|bgp|eigrp|rip`, `network …`, `redistribute connected|static|ospf|bgp|eigrp|rip`
- **IPv6:** `ipv6 unicast-routing`, `ipv6 address <addr>/<len>`, `ipv6 route`, `ipv6 default-gateway`
- **Edge/security:** ACLs (`access-list`, `ip access-group`), NAT/PAT (`ip nat …`), FHRP (`standby`/`vrrp`), EtherChannel (`channel-group`)
- **Show:** `show ip interface brief | route | ospf neighbor | eigrp neighbors | bgp summary | dhcp binding | nat translations`, `show ipv6 route`, `show standby | etherchannel | spanning-tree | vlan | mac address-table | arp | running-config`

## 🖼️ Screenshots

| Cisco-style CLI + live ping/ARP | Topology-grounded AI tutor |
|---|---|
| ![CLI](docs/img/hero-cli.png) | ![AI tutor](docs/img/ai-tutor.png) |

## 🚀 Quickstart

```bash
git clone https://github.com/joxorsayan/netsim.git
cd netsim
pip install -r requirements.txt
uvicorn app.main:app --reload
# open http://localhost:8000  → click "Load sample topology"
```

Run the test suite:

```bash
pip install pytest
python -m pytest
```

## 🧱 Architecture

```
app/
  engine/        pure-Python simulation engine (no web deps)
    packet.py    frames / ARP / IP / ICMP / DHCP units + capture entries
    models.py    Device (Host/Switch/Router), Interface, Link, DHCP pools
    simulator.py Network: event loop, switching, STP, routing, OSPF, DHCP, ping
    cli.py       Cisco IOS-like command interpreter
    pcap.py      serialise a capture to a libpcap (.pcap) for Wireshark
    tutor.py     rule-based analyzer + optional Cloudflare Workers AI tutor
    labs.py      lab-as-code auto-grading checks
    automation.py  config templating, intent↔CLI, snapshot/drift, validation
  tutor_ai/      training-data generators for the on-device tutor model
  workspace.py   in-memory, per-client isolated topologies + lab apply/export
  main.py        FastAPI REST API + static SPA
  static/        vanilla-JS topology editor, CLI console, capture/tutor/lab/automation tabs
automation/      Python automation toolkit: SDK + CLI + Jinja2 templates + network defs
  client.py      NetSimClient — typed REST SDK
  cli.py         `python -m automation.cli` (render/deploy/validate/drift/intent)
  netdevops.py   render → push → validate pipeline
  labs/          declarative network definitions (topology + vars + assertions)
examples/        runnable automation examples (provision_and_verify.py)
ai/              ML pipeline: dataset → Kaggle T4 training → ONNX → CDN delivery
tests/           engine + CLI + advanced-feature + automation toolkit tests
```

**Tech stack:** Python 3.12 · FastAPI · vanilla JS/SVG front-end · Qwen2.5 LoRA fine-tune · ONNX Runtime + transformers.js (WebGPU/WASM) · Scalingo (app) + Cloudflare Pages/Backblaze B2 (model CDN).

## 🤖 AI tutor & on-device ML pipeline

The tutor works **offline** with a built-in rules engine, and optionally runs a **fine-tuned LLM directly in your browser** — no API key, no per-query cost.

The full, reproducible pipeline lives in [`ai/`](ai/README.md):

1. **Dataset** — generators in `app/tutor_ai/` produce *verified* Q&A across three pillars: fault **diagnosis** (the simulator is the oracle), **CLI** (walks the live `?` grammar so answers match the console), and **knowledge** (authored concepts + procedurally-computed subnetting + IANA ports).
2. **Training** — a LoRA fine-tune of `Qwen2.5-Instruct` on a free **Kaggle T4 GPU**, with teacher distillation, then held-out **key-token-recall** evaluation.
3. **Export** — ONNX (4-bit) in transformers.js layout.
4. **Delivery** — model files served from a CDN; `app/static/tutor_ai.js` loads them with **transformers.js** and runs inference via **WebGPU** (with a WASM fallback).

> The tutor *explains*; the deterministic engine supplies exact facts — so numbers (subnet math, ranges) stay correct by construction.

To use a hosted LLM instead (Cloudflare Workers AI, free tier), set `CF_ACCOUNT_ID` + `CF_API_TOKEN`; it calls `@cf/meta/llama-3.1-8b-instruct` and falls back to the rules engine on any error.

## 🔧 Network automation (NetDevOps)

NetSim isn't just clickable — its REST API is driven by a small **Python automation toolkit** ([`automation/`](automation/)), so you can treat the network as code the way you would with netmiko/NAPALM + Jinja2 + pyATS:

- **Config as code** — render Cisco configs from **Jinja2 templates** + per-device variables.
- **Push** — apply config to devices (netmiko `send_config_set` style).
- **Validate intended state** — assert interfaces up, routes present, hosts reachable (Batfish/pyATS style).
- **Drift detection** — snapshot a running-config baseline and diff against it.
- **Structured intent** — a YANG-ish JSON view of a device, and the reverse (intent → CLI).

One declarative file describes the whole network ([`automation/labs/two_router_ospf.yaml`](automation/labs/two_router_ospf.yaml)); a single command deploys **and** verifies it:

```bash
pip install -r automation/requirements.txt
uvicorn app.main:app --port 8000 &
python -m automation.cli deploy automation/labs/two_router_ospf.yaml --url http://localhost:8000
```

```
=== NetDevOps deploy: two-router-ospf ===
[OK] topology: 4 devices, 3 links
[OK] push R1: 13 lines   [OK] push R2: 13 lines   [OK] push PC1/PC2
[OK] saved running-config baseline
[OK] validation: 8/8 passed (score 100/100)
=== result: PASS ===
```

The **[NetDevOps CI workflow](.github/workflows/netdevops.yml)** runs this on every push (render → push → validate), failing the build on any misconfiguration. The live app's **Automation** tab exposes the same flow in the browser. More in [`examples/automation/`](examples/automation/).

```python
from automation import NetSimClient

nc = NetSimClient("http://localhost:8000")
nc.push_config("R1", ["interface g0/0", "ip address 10.0.0.1 255.255.255.252", "no shutdown"])
print(nc.validate([{"type": "reachable", "src": "PC1", "dst": "192.168.2.10"}]))
```

## ☁️ Deploy (Scalingo / any buildpack host)

The repo is buildpack-ready (`requirements.txt`, `.python-version`, `Procfile`):

```bash
scalingo create netsim
git push scalingo main
```

`Procfile` runs a single worker (`--workers 1`) because topology state is in-process (see `app/workspace.py`); multiple workers would each hold a divergent copy.

## 🗺️ Roadmap

- [x] L2: 802.1Q trunking, STP root election + port states
- [x] L3: DHCP server, OSPF/EIGRP/RIP/BGP, route redistribution, IPv6 dual-stack
- [x] `.pcap` export for Wireshark
- [x] AI tutor — on-device LLM + rules engine
- [x] Labs-as-code + auto-grading
- [ ] Persistence (Postgres) + share topologies by URL
- [ ] DHCP relay across subnets (`ip helper-address` forwarding)
- [ ] Multi-area OSPF cost + passive interfaces

## 🤝 Contributing

Contributions are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Open an issue or PR for bugs, new protocols, or lab templates.

## 📄 License

Released under the [MIT License](LICENSE).

## 👤 Author

**Sayan Roy Chowdhury** — Infrastructure & Network Engineer (CCNA, Aruba ACMA, Azure Fundamentals).
[LinkedIn](https://www.linkedin.com/in/sayan-roy-chowdhury-523b97319) · [GitHub](https://github.com/joxorsayan)

Built to show that production networking concepts (OSPF/BGP/STP/VLAN/DHCP, packet forwarding, Cisco CLI) can be modelled from first principles and shipped as an accessible, zero-install learning tool — combining networking depth with full-stack and applied-ML engineering.
</content>
</invoke>
