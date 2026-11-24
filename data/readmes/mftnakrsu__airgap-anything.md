<p align="center">
  <img src="assets/brand/icon-tile-animated.svg" width="96" height="96" alt="">
</p>

<h1 align="center">airgap-anything</h1>

<p align="center">Design any system for air-gapped environments.</p>

<p align="center">
  <a href="https://github.com/mftnakrsu/airgap-anything/actions/workflows/ci.yml"><img src="https://github.com/mftnakrsu/airgap-anything/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <img src="https://img.shields.io/badge/python-3.11%2B-blue" alt="Python 3.11+">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT license"></a>
</p>

<p align="center">
  <a href="#install"><b>Install</b></a> ·
  <a href="#use">Use</a> ·
  <a href="CONTRIBUTING.md">Contributing</a> ·
  <a href="#türkçe">Türkçe</a>
</p>

`airgap-anything` is a home for agent skills that design systems for networks without internet access. Its first skill, `airgap-architect`, interviews you about your organization and writes a blueprint: one component per layer, GPU sizing, the reason for each choice, and the list of everything that has to be carried into the network.

Version 0.2 covers the core pipeline and the LLM platform layer, and adds a second skill, `airgap-transfer`, that prepares what the blueprint lists for the trip into the network. See [Scope](#scope).

<p align="center">
  <img src="assets/brand/how-it-works.svg" alt="Eight steps on a connected workstation, done by the model, the scripts and you. The files cross the air gap, and the people or the agent inside build the system without internet." width="880">
</p>

## Why

Architecture skills usually assume internet access and hosted services. Skills for air-gapped work usually explain one tool at a time. `airgap-architect` is the layer above: one interview, one blueprint for the whole stack, written for a network where nothing can be looked up or downloaded.

It decides; it does not operate. For the details of running each tool, catalog entries point to existing per-tool skills.

## Skills

| Skill | What it does | Where it runs |
|---|---|---|
| `airgap-architect` | Interviews you and writes the blueprint, GPU sizing, the agent block and the transfer manifest (`transfer-manifest.md` and `.json`) | A connected workstation |
| `airgap-transfer` | Turns the transfer manifest into a bundle that checks itself: a fetch script, checksums, a split across media, an inventory, and `verify.sh`, `load.sh` and a runbook or agent rules for the inside | A connected workstation; its two shell scripts run inside |

Inside the network nothing needs internet or an LLM. The architect interview asks who works inside: people, an agent on a local model, or people first and an agent later. The bundle carries a runbook for people, rules for an agent, or both.

## Install

Install it once; after that you only ask (see [Use](#use)). The skill needs Python 3.11 or newer on the machine where the design is made. It has no other dependency and makes no network calls.

### Claude Code

In a Claude Code session:

```
/plugin install airgap-anything --marketplace mftnakrsu/airgap-anything
```

Claude Code asks you to confirm the new marketplace, then lets you choose where to install. The plugin carries both skills. This form needs Claude Code 2.1.275 or newer; from your shell, `claude plugin install airgap-anything --marketplace mftnakrsu/airgap-anything` does the same with 2.1.292 or newer. On older versions, add the marketplace first:

```
/plugin marketplace add mftnakrsu/airgap-anything
/plugin install airgap-anything@airgap-anything-marketplace
```

### Other agents that support Agent Skills

```bash
npx skills add mftnakrsu/airgap-anything -g
```

This installs both skills. To install one, add the option `--skill`, for example `npx skills add mftnakrsu/airgap-anything -g --skill airgap-transfer`.

`-g` installs it for your user, so every project has it; without `-g` it goes into the current project only. Add `-a` and an agent ID to choose the agent, for example `-a codex`, `-a cursor`, `-a opencode` or `-a gemini-cli`. The [skills CLI](https://github.com/vercel-labs/skills) supports Claude Code, Codex, Cursor, OpenCode and 75 more agents; its [agent list](https://github.com/vercel-labs/skills/blob/main/docs/agents.md) has the IDs. This route needs Node.js 22.20 or newer. `npx skills update` updates the skill later.

### Without internet

On a connected machine, in a clone of this repository:

```bash
for skill in airgap-architect airgap-transfer; do
  git archive --format=tar.gz --prefix=$skill/ -o $skill.tar.gz HEAD:plugins/airgap-anything/skills/$skill
  sha256sum $skill.tar.gz > $skill.tar.gz.sha256
done
```

Carry the four files in, then:

```bash
for skill in airgap-architect airgap-transfer; do
  sha256sum -c $skill.tar.gz.sha256 && mkdir -p ~/.claude/skills && tar -xzf $skill.tar.gz -C ~/.claude/skills/
done
```

`~/.claude/skills/` is where Claude Code keeps personal skills. Use your agent's own skills directory if it differs.

## Use

Ask your agent, in your own words, on a machine with internet access:

> Design an air-gapped LLM platform for my organization.

You do not need to name the skill. Claude Code picks it when a request is about designing, planning or sizing a system for an air-gapped, offline or on-premises network, and leaves other requests alone; [a test](evals/results/2026-11-23-triggering.md) checks this in English and Turkish. In Claude Code you can also start it directly: with `/airgap-anything:airgap-architect` after the plugin install, or with `/airgap-architect` when it is installed as a personal or project skill (the `npx skills` and offline routes).

The skill then works through these steps:

| # | Step | Who |
|---|---|---|
| 1 | Interview: people, departments, privacy, hardware, operations | the agent, one question at a time |
| 2 | Tier and per-layer floors | `tier.py` |
| 3 | GPU, server and power sizing | `size.py` |
| 4 | One decision per layer, from decision tables and the catalog | the agent |
| 5 | Transfer manifest | `manifest.py` |
| 6 | Blueprint, and the agent block in `AGENTS.md` | the agent |
| 7 | Consistency check | `lint.py` |
| 8 | Your approval, then hand-off to an implementation plan | you |

### Carrying it in

Once the blueprint is approved, ask in your own words, for example "prepare everything in the transfer manifest for our USB disks". `airgap-transfer` then works through these steps:

| # | Step | Who |
|---|---|---|
| 1 | A few questions: where to build the bundle, where each model comes from, the medium or the channel's file limit | the agent |
| 2 | The plan and `fetch.sh` | `plan.py` |
| 3 | Your approval, then the download | you, or the agent after you approve |
| 4 | Manual items: add files or mark them not needed | you |
| 5 | Checksums, volumes, inventory, runbook or agent rules, inside scripts | `pack.py` |
| 6 | Bundle check | `check.py` |
| 7 | One medium at a time, read back | `pack.py --write-volume` |

Inside, on any host with a POSIX shell and coreutils:

```bash
sh verify.sh /srv/airgap-bundle
sh load.sh /srv/airgap-bundle /srv/models
```

`verify.sh` joins split files and checks every SHA-256; when something is missing or damaged it writes `MISSING.txt` with what to bring next time.

## What you get

```
your-project/
├── docs/airgap/blueprint.json          answers, tier, sizing, decisions
├── docs/airgap/transfer-manifest.md    images, models, packages and settings to carry in
├── docs/airgap/transfer-manifest.json  the manifest as JSON, for airgap-transfer
├── docs/airgap/transfer.json           the transfer's answers and plan
├── docs/airgap/blueprint.md            the blueprint (under docs/superpowers/specs/ with superpowers)
└── AGENTS.md                           instructions for the agent that builds it inside the network
```

These files travel into the network together with the artifacts the manifest lists. Inside, people follow the bundle's `INSIDE.md`, an agent follows `AGENTS-INSIDE.md` and `AGENTS.md`, and nobody needs internet access.

## Tiers and sizing are separate

A tier (T1 single team, T2 department, T3 enterprise) measures how complex the organization is: how many people and departments, and whether audit, isolation or zero downtime is required. It selects patterns such as "gateway or not" and "Compose or Kubernetes".

GPU count is a different question. It comes from the size of the model, the kind of usage and the headcount, and `size.py` computes it. A small team that serves a very large model needs many GPUs at T1.

Sizing covers memory, not speed. Every blueprint carries a "benchmark before production" step.

The agent runs the scripts itself; you never type these commands. This recording shows what they compute on the `department` example: 180 people in four departments, one 671-billion-parameter model on eight 141 GB GPUs. [design/demo/build_demo.py](design/demo/build_demo.py) runs the four scripts and draws it.

<p align="center">
  <img src="assets/demo/terminal-dark.svg" alt="The four scripts run on the department example: base tier T2, eight GPUs in one server, the sections of the transfer manifest, and lint reporting no findings" width="880">
</p>

## Evidence labels

Every catalog entry, threshold and decision-table row carries one label.

| Label | Meaning |
|---|---|
| `field` | Verified in a real deployment by a named person |
| `docs` | Taken from official project or vendor documentation, or, where the documentation is silent, from the project's source code at the release tag; the URL is recorded |
| `estimate` | Reasoned or community-sourced; verify before relying on it |

A decision inherits the weakest label among its inputs. Every decision that rests on an estimate is listed in the blueprint's verification section.

## Scope

In version 0.2:

- Decision tables for the inference engine and the LLM gateway.
- Fixed per-tier defaults for UI, identity, observability, orchestration, state stores and artifact registry.
- Sizing from organization answers, a transfer manifest, and lint.
- `airgap-transfer`: a plan and fetch script from the transfer manifest, a checked bundle split across media, and `verify.sh` and `load.sh` for the inside.

Not in version 0.2:

- Deployment files such as Docker Compose or Helm.
- A recommendation of which model to run.
- Decision tables for data, CI/CD and security layers.
- Compliance mappings.

## Works with superpowers

When [superpowers](https://github.com/obra/superpowers) is installed, the blueprint is written where its specs live and handed to `superpowers:writing-plans` after you approve it. Without superpowers the skill works on its own.

## Contributing

The catalog is the part that ages. [CONTRIBUTING.md](CONTRIBUTING.md) explains how to add or verify an entry. One rule above all: nothing is written from memory.

Logo files and their usage rules are in the [brand guide](assets/brand/BRAND.md).

## License

MIT. See [LICENSE](LICENSE).

## Türkçe

`airgap-anything`, internete kapalı (air-gapped) ağlarda çalışacak sistemleri tasarlayan agent skill'lerini bir araya getirir. İlk skill olan `airgap-architect`, kurumunuzla kısa bir görüşme yapar ve bir blueprint yazar: her katman için tek bir bileşen, GPU, sunucu ve güç hesabı, her seçimin gerekçesi ve ağın içine taşınması gereken her şeyin listesi.

Tasarım internete bağlı bir makinede yapılır. Ağın içine blueprint dosyaları ile manifestin listelediği imajlar, modeller ve paketler taşınır; içeride bu dosyaları insanlar, bir agent ya da önce insanlar sonra agent internet olmadan izler. Betikler yalnızca Python 3.11 veya üstünün standart kütüphanesini kullanır ve ağa bağlanmaz.

Sürüm 0.2 ikinci skill'i ekler: `airgap-transfer`, transfer manifestini kendini denetleyen bir pakete çevirir (indirme betiği, SHA-256 listesi, disklere bölme, envanter, içeride çalışan `verify.sh` ve `load.sh`, insanlar için bir çalıştırma kılavuzu ya da içerideki agent için kurallar). İçeride hiçbir adım internet ya da LLM gerektirmez.

**Kurulum.** Bir kez kurarsınız; sonrasında yalnızca sorarsınız. Claude Code oturumunda:

```
/plugin install airgap-anything --marketplace mftnakrsu/airgap-anything
```

Bu biçim Claude Code 2.1.275 veya üstünü ister. Daha eski sürümlerde önce marketplace'i ekleyin:

```
/plugin marketplace add mftnakrsu/airgap-anything
/plugin install airgap-anything@airgap-anything-marketplace
```

Agent Skills standardını destekleyen diğer agent'larda (Codex, Cursor, OpenCode, Gemini CLI ve diğerleri; agent seçmek için `-a`, örneğin `-a codex`):

```bash
npx skills add mftnakrsu/airgap-anything -g
```

`-g` skill'i kullanıcınız için kurar, böylece her projede hazır olur.

İnternetsiz kurulum için yukarıdaki [Without internet](#without-internet) bölümüne bakın.

**Kullanım.** İnternete bağlı bir makinede agent'ınıza kendi cümlenizle sorun, örneğin:

> Kurumum için internete kapalı bir LLM platformu tasarla.

Skill'in adını söylemeniz gerekmez: Claude Code, internete kapalı, çevrimdışı ya da kurum içi bir ağ için sistem tasarlama, planlama veya boyutlandırma isteklerinde skill'i kendisi seçer, başka isteklerde seçmez. Bunu Türkçe ve İngilizce isteklerle ölçen bir test vardır. Claude Code'da skill'i doğrudan da başlatabilirsiniz: plugin olarak kurduysanız `/airgap-anything:airgap-architect`, kişisel ya da proje skill'i olarak kurduysanız (`npx skills` veya internetsiz kurulum) `/airgap-architect` yazın.
