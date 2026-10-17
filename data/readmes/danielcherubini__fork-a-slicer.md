# Fork a Slicer

> Documentation and step-by-step plans that walk you through forking OrcaSlicer and adding Bambu printer support — using a process isolation bridge that runs Bambu's network plugin in a separate process. Based on the FULU-Foundation architecture.

Takes you through forking [OrcaSlicer](https://github.com/SoftFever/OrcaSlicer) and setting up a bridge that runs Bambu Lab's closed-source network plugin in a separate process. Gives you full printer control — ARM Linux, process isolation, camera, cloud, the works.

## Quick Start

```bash
git clone https://github.com/your-account/fork-a-slicer
cd fork-a-slicer
```

Then feed each plan to your AI agent in order. Example:

```
"Read plans/00-overview.md, then follow it step by step in my OrcaSlicer fork at /path/to/OrcaSlicer."
```

## Plans

| # | Plan | What It Does |
|---|------|-------------|
| 00 | [Overview & Architecture](plans/00-overview.md) | Context, legal basis, bridge architecture, file map |
| 01 | [Extract X.509 Certificate](plans/01-extract-cert.md) | Extract cert + private key from Bambu Connect (needed by bridge host) |
| 02 | [Bridge Infrastructure](plans/02-bridge-infrastructure.md) | Shared core protocol, bridge client (RPC + launcher + event pump + forwarder), bridge host, apply script |
| 03 | [Wire Bridge into OrcaSlicer](plans/03-wire-bridge.md) | Patch BBLNetworkPlugin, register sources in CMake, build bridge host |
| 04 | [Build and Verify](plans/04-build-verify.md) | Build everything, smoke tests, functional tests, troubleshooting |

Each plan builds on the previous. Based on the [FULU-Foundation](https://github.com/FULU-Foundation/OrcaSlicer-bambulab) architecture.

## Legal Framework

This project operates under well-established legal provisions for reverse engineering software to achieve interoperability.

### Norwegian Law (Åndsverkloven)

**§41 — Right to observe, study, and test:**

> A person who has the right to use a copy of a computer program may, in connection with reading, display on screen, running, transferring, or storing the program that the user is entitled to perform, **observe, study, or test how the program works** in order to determine the ideas and principles underlying any part of the program.

**§42 — Reverse engineering for interoperability:**

> It is permitted to reproduce a computer program's code and translate its form when this is a prerequisite for obtaining the information necessary to achieve **functional interoperability** between an independently developed computer program and other programs.

**§41(5) / §42(3) — Cannot be contracted away:**

> The provisions of this paragraph cannot be waived by agreement.

This means EULA clauses forbidding reverse engineering are **unenforceable** in Norway.

### EU Software Directive (2009/24/EC)

Norway implements [Directive 2009/24/EC](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32009L0024) (the Software Directive) via the EEA agreement. Article 6 explicitly permits decompilation and reverse engineering for interoperability. Article 5 permits observing, studying, and testing to determine ideas and principles.

### What We Are Doing

- Providing **instructions** on how to extract the certificate from Bambu Connect
- Guiding the setup of a **process isolation bridge** that loads your legally obtained Bambu network plugin in a separate process
- Documenting the **integration process** (CMake changes, BBLNetworkPlugin patching, build steps)
- Sharing **knowledge** about how to achieve Bambu printer interoperability from OrcaSlicer

### What We Are Not Doing

- We are **not distributing** Bambu Lab's closed-source network plugin
- We are **not distributing** the extracted certificate or private key
- We are **not distributing** any copyrighted code from Bambu Connect

Everything you need to extract the certificate yourself is documented in the plan files. The extraction is performed on software you legally obtained, for the purpose of interoperability with hardware you own.

## Key Resources

| Resource | Link |
|----------|------|
| OrcaSlicer | [GitHub](https://github.com/SoftFever/OrcaSlicer) |
| Bambu Lab Cloud API docs | [coelacant1/Bambu-Lab-Cloud-API](https://github.com/coelacant1/Bambu-Lab-Cloud-API) |
| Open Bambu API reference | [Doridian/OpenBambuAPI](https://github.com/Doridian/OpenBambuAPI) |
| Open Bambu Networking | [ClusterM/open-bambu-networking](https://github.com/ClusterM/open-bambu-networking) |
| FULU-Foundation fork (bridge approach) | [OrcaSlicer-bambulab](https://github.com/FULU-Foundation/OrcaSlicer-bambulab) |
| Bambu Connect RE guide | [Consumer Rights Wiki](https://consumerrights.wiki) |

## License

This repository contains documentation and plan files only. All code you produce by following these plans is your own independent implementation.
