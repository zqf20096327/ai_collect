<div align="center">

<img src="assets/icon.svg" alt="" width="88">

# CLAgent: A Continually Self-Evolving Agent System

Continually learning new capability from tasks, autonomously extending the agent system

**English** · [简体中文](README.zh-CN.md) · [日本語](README.ja.md)

[![Website](https://img.shields.io/badge/Website-cl--agent.com-2b2f36?style=flat-square)](https://cl-agent.com)
[![App market](https://img.shields.io/badge/App_market-2b2f36?style=flat-square)](https://cl-agent.com/store)
[![Download](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcl-agent.com%2Fdownloads%2Fmanifest.json&query=%24.version&label=Download&prefix=v&color=2b2f36&style=flat-square)](https://cl-agent.com/download.html)
[![Platforms](https://img.shields.io/badge/Platforms-macOS_·_Windows-2b2f36?style=flat-square)](https://cl-agent.com/download.html)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.png">
  <img src="assets/hero.png" alt="The CLAgent window: projects and apps down the left, a conversation with its tool calls on the right" width="100%">
</picture>

</div>

CLAgent runs on the desktop and works inside the project directory on disk. A terminal, a file editor, a browser, memory and standing tasks sit in one window, and every other capability is installed from an app market. What the agent produces in use is kept in two structures: facts and preferences go to memory, capability goes to apps, one capability per app. A new app is a new unit and a rewritten app becomes a new generation with the earlier generations kept, so acquiring a capability does not displace one already held.

## The three layers

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/layers-dark.gif">
  <img src="assets/layers.gif" alt="Memory, apps and system, drawn as the three rows of the CLAgent mark" width="100%">
</picture>

| Layer | Carries | How it changes |
| --- | --- | --- |
| Memory | Facts and preferences | Written, rewritten and forgotten as sessions run; later work retrieves and reuses |
| Apps | Capability | Learned in use, kept as generations that can be returned to |
| System | Loading and adjudication of the changes made by the two layers above | Everything except the system calls evolves on its own; the kernel changes only with product releases |

Every change takes effect only after adjudication. Memory and apps are changed by the agent, with each step entered in a ledger and reversible. System apps ship with product releases and can also be updated from the market. The kernel changes only with product releases.

## Autonomous evolution

A judgement runs at the end of a turn, and most turns produce nothing. What is registered becomes ordinary work: it goes through the same permission gate as anything else, and what it produces is adjudicated before it takes effect.

Memory takes the facts and preferences. Apps take capability, kept as generations, so a change leaves the earlier generation in place and any generation can be returned to. An app built on one machine can be published to the market for another agent to install.

## System design

The agent generates new apps while it is in use, and those apps cannot be reviewed in advance. Security therefore rests on system-layer mechanism rather than on prior review: loading, per-call adjudication, process isolation and accounting throughout are carried out by the kernel.

| Operating system | CLAgent |
| --- | --- |
| Unit of scheduling | The turn |
| Unit of persistence | The session |
| System call | The verbs the kernel provides directly |
| System programs | System apps, shipped with the product |
| User programs | Apps |
| Permission outcome: allow, deny | Allow, deny, ask |
| Storage: files | Files, with a layer of record above them |

Two things depart from the operating-system shape on purpose: the permission gate has a third verdict, `ask`, and storage carries a record layer above the files. The processor at the base of the machine is a language model, which is a probabilistic part, so the constraints are enforced by a deterministic kernel instead of by the model's behavior.

## Permissions

A person is the only grantor. Authorizing, approving, installing and uninstalling can only be initiated by a person. The agent requests actions in the person's name, and what it can do is a subset of what the person has granted. Adjudication has three outcomes: allow, deny, ask.

| Tier | What is exempt from asking |
| --- | --- |
| Normal | Read-only calls run directly. Everything else is asked about each time. |
| Auto | Workspace modification is let through. For a sensitive action the agent judges first, and asks anyway when it cannot produce grounds. |
| Full access | Nothing is asked about. |

Every call runs through one fixed sequence of checks.

| Order | Check | What it decides |
| --- | --- | --- |
| 1 | Deny list | Held in code, it blocks under every tier, full access included |
| 2 | Full access | At this tier the call is let through here |
| 3 | Session allow-list | A call already approved for this session is let through here |
| 4 | Access level | Read-only always passes, workspace modification passes at the auto tier, and a sensitive call at the auto tier is judged by the agent |

The grounds for such a judgment are entered into the record. An approval's scope is either the one call or the current session, and both the allow-list and the tier lapse when the session ends.

## Memory and storage

Memory, tasks, apps and runs are one kind of record with one addressing scheme and one change ledger. The scope is the storage location, and the storage location decides the lifetime.

| Scope | Lives with | Lifetime |
| --- | --- | --- |
| Global | Global storage | Kept long-term |
| Project | The project | As long as the project |
| Session | The session | Until the session is deleted |

Session memory is removed when the session is deleted. Session permission grants lapse when the session ends.

One store is read along two paths. A person reads entries and the ledger: the original text, the difference a rewrite made, and a line-by-line activity feed, where writes, rewrites and forgettings are entered one by one and a forgetting can be undone. The agent reads the assembled result: relevant memory enters the context when a turn is assembled, and the workspace is read and written through file system calls.

## Apps and the app market

Every capability outside the system calls is an app. One capability, one app: its tools, its interface and its skills sit together, and uninstalling removes all of it at once. An app can only offer the tools its manifest declares. Its service process runs on its own, and its state is cleared on uninstall.

Official, third-party and agent-generated apps pass through the same loading, authorization and versioning mechanism. Signing governs distribution rather than admission: an update to a given identity has to come from the same publisher, verified with Ed25519, and unsigned apps can still be installed and run. Installing grants nothing, because permission is adjudicated call by call, and a changed declaration voids every grant already given.

The six apps that ship with the product:

| App | id | What it adds |
| --- | --- | --- |
| Terminal | `terminal` | Shell and Python commands in a terminal the user watches live and can type into |
| Editor | `editor` | Reading, writing, editing, organizing, importing and previewing the files in the workspace |
| Browser | `browser` | Browsing and operating live web pages, web search, page text, downloads |
| Memory | `memory` | Writing, recalling and deleting facts that persist across conversations |
| Tasks | `tasks` | Standing work without supervision: each task starts by the clock, by an event or by the user's press, and reports back with a receipt |
| Apps | `apps` | Installing, creating, updating, evolving and removing apps |

Beyond the six above:

| Group | Entries |
| --- | --- |
| Documents and figures | Office export, Drawing, OCR |
| Devices and browsers | Android emulator or adb device, Chrome through a browser extension, Playwright |
| Messaging and meetings | Connect a phone, WeChat, WeCom, Tencent Meeting |
| Connectors | GitHub, Slack, Notion, Linear, Asana, ClickUp, Figma, Feishu, Amap, Context7 |
| Published by third parties | An industry-news writing procedure, a material archiver |

Each row of the index carries an id, a name, a description and a version, and marks the entries that contribute a user interface. Android is the only entry that currently declares one. Official and user-published apps are listed together at [cl-agent.com/store](https://cl-agent.com/store).

## Model sources

There are two, and they differ in where the model request goes.

| | Official hosting | Own endpoint |
| --- | --- | --- |
| Request path | Forwarded through the official gateway | Sent straight to the user's own service endpoint |
| Interface | The official gateway | An OpenAI-compatible interface |
| Configuration | Model list maintained officially | Model list and parameters set by the user |
| Metering | By token, accounted in real time and readable in the user center | — |

## Download and install

| Platform | Requirement | Installer |
| --- | --- | --- |
| macOS | Apple Silicon, macOS 13+ | `.dmg` |
| Windows | Windows 10 / 11, x64 | `.exe` |

[cl-agent.com/download.html](https://cl-agent.com/download.html) carries the current version, the direct links and their SHA-256 checksums.

First run is three steps: the package for the platform is installed from the download page; signing in through the browser is chosen inside the app, and the session returns to the app once the emailed verification code passes; a model is connected, either official hosting or an OpenAI-compatible endpoint entered in settings.

## This repository

The source code of CLAgent is kept in a separate private repository. What is published here is this page and its Chinese and Japanese translations, a documentation index, the brand assets and the issue templates.

The place to extend CLAgent is the app layer rather than this repository. An app carries its own tools, interface and skills, and an app generated on one machine can be published to the market for another agent to install.

## Feedback

Bug reports and feature requests go to [Issues](../../issues). A search through the open issues comes first, and a reaction on an existing report counts; a repeated comment does not.

A report is easier to act on when it names the platform and its version, the CLAgent version, what was done, and what happened against what was expected.

A security problem goes to [a private advisory](../../security/advisories/new) rather than into a public issue.

## CLLab

CLAgent is built at CLLab, a lab working on continual learning.

| Product | Status |
| --- | --- |
| CLAgent | Released |
| CLOCR | Coming |

## Documentation

The mechanisms above are set out page by page on the site, in Chinese.

| Page | Subject |
| --- | --- |
| [System design](https://cl-agent.com/architecture.html) | The layer-by-layer correspondence with an operating system |
| [Users and permissions](https://cl-agent.com/permissions.html) | Who grants, the three tiers, the fixed check order |
| [Memory and storage](https://cl-agent.com/memory.html) | Scopes, the ledger, the two read paths |
| [The app layer](https://cl-agent.com/apps.html) | What an app is, the three sources, signing |
| [Autonomous evolution](https://cl-agent.com/evolution.html) | How memory and apps change |

## Research background

A network that learns tasks one after another overwrites what it already holds, the phenomenon called catastrophic forgetting (French, 1999). How capability can accumulate across a stream of tasks is the central question of continual learning (Parisi et al., 2019). CLAgent carries it to an agent system: the system keeps learning while it carries out tasks, and its capability grows with them.

French, R. M. (1999). *Catastrophic forgetting in connectionist networks.* Trends in Cognitive Sciences, 3(4), 128-135. [doi:10.1016/S1364-6613(99)01294-2](https://doi.org/10.1016/S1364-6613(99)01294-2)

Parisi, G. I., et al. (2019). *Continual lifelong learning with neural networks: A review.* Neural Networks, 113, 54-71. [arXiv:1802.07569](https://arxiv.org/abs/1802.07569)

## Citation

```bibtex
@software{clagent,
  title  = {CLAgent: A Continually Self-Evolving Agent System},
  author = {CLLab},
  year   = {2026},
  url    = {https://cl-agent.com}
}
```

## License

This repository carries documentation and brand assets. No open-source license is granted here, and nothing published here conveys any right to the CLAgent software. The CLAgent name and mark identify this product and are not for use on another. © 2026 CLLab. All rights reserved.

The user agreement and the privacy policy that govern the product itself are stated in the footer of [cl-agent.com](https://cl-agent.com).
