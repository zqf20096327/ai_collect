<p align="center">
  <img src="assets/brand/icon-tile-animated.svg" width="96" height="96" alt="">
</p>

<h1 align="center">airgap-anything</h1>

<p align="center">Design any system for air-gapped environments.</p>

<p align="center">
  <a href="https://github.com/mftnakrsu/airgap-anything/actions/workflows/ci.yml"><img src="https://github.com/mftnakrsu/airgap-anything/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <img src="https://img.shields.io/badge/Agent%20Skills-markdown%20only-blue" alt="Agent Skills, markdown only">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT license"></a>
</p>

<p align="center">
  <a href="#install"><b>Install</b></a> ·
  <a href="#use">Use</a> ·
  <a href="examples/department/blueprint.md">Example</a> ·
  <a href="https://airgap-anything.mefby.com">Docs</a> ·
  <a href="CONTRIBUTING.md">Contributing</a> ·
  <a href="#türkçe">Türkçe</a>
</p>

`airgap-anything` is a plugin of agent skills for networks without internet access. You describe your organization; your agent designs the whole system, sizes the GPUs, lists everything that has to be carried in, and packs it into a bundle that checks itself on the other side.

The skills are plain markdown: no scripts, no dependencies, nothing to install but the folder. They work in Claude Code, Codex, Cursor and every agent that reads [Agent Skills](https://agentskills.io), and they work inside the air gap too, on a local model.

<p align="center">
  <img src="assets/brand/how-it-works.svg" alt="Eight steps on a connected workstation, done by the agent and you. The files cross the air gap, and the people or the agent inside build the system without internet." width="880">
</p>

## Skills

| Skill | What it does | Where it runs |
|---|---|---|
| [`airgap-architect`](plugins/airgap-anything/skills/airgap-architect/SKILL.md) | Interviews you, then writes the blueprint: one decision per layer with its reasons and alternatives, GPU sizing with every step shown, and the transfer manifest of what to carry in | A connected workstation |
| [`airgap-transfer`](plugins/airgap-anything/skills/airgap-transfer/SKILL.md) | Turns the transfer manifest into a bundle that checks itself: fetch commands you approve first, a SHA-256 list, a split across media, an inventory, and a runbook or agent rules for the inside | A connected workstation; its runbook runs inside |
| [`airgap-agent`](plugins/airgap-anything/skills/airgap-agent/SKILL.md) | Sets up a coding agent for the network without internet: picks the tool, writes its configuration and central policy with telemetry, updates and web access off, states what the model server must support, chooses MCP servers that work offline, and adds everything to the transfer manifest | A connected workstation; its checks run inside |
| [`airgap-rag`](plugins/airgap-anything/skills/airgap-rag/SKILL.md) | Makes your documents searchable inside the network: asks which platform you want (Open WebUI knowledge bases, a RAG server such as RAGFlow, or your own choice), picks extraction and OCR, embedding and reranker models and the vector store, sizes the first load step by step, writes the configuration and a bulk-load runbook, and adds everything to the transfer manifest | A connected workstation; its checks run inside |
| [`airgap-install`](plugins/airgap-anything/skills/airgap-install/SKILL.md) | Writes the installation for the approved design: the deployment files (Docker Compose, or Kubernetes manifests for k3s, RKE2 or a cluster you already run) and a runbook in which every step is a command, the output to expect and what to do when it differs, with the blueprint's GPU counts copied in and the rows the files need added to the transfer manifest | A connected workstation; its runbook runs inside |

Ideas for more are in [#12](https://github.com/mftnakrsu/airgap-anything/issues/12).

## Why

Architecture skills usually assume internet access and hosted services. Skills for air-gapped work usually explain one tool at a time. `airgap-anything` is the layer above: one interview, one blueprint for the whole stack, written for a network where nothing can be looked up or downloaded.

From memory, an agent writes versions, image names and GPU counts that look right and are not sourced; inside the network a wrong one costs another trip. Here every component, version and image comes from a [catalog](plugins/airgap-anything/skills/airgap-architect/catalog) where each value carries its source, and every number comes from a sizing procedure the agent writes out step by step.

The skills decide; they do not operate. For the details of running each tool, catalog entries point to existing per-tool skills.

## Install

Install it once; after that you only ask (see [Use](#use)).

### Claude Code

In a Claude Code session:

```
/plugin install airgap-anything --marketplace mftnakrsu/airgap-anything
```

Claude Code asks you to confirm the new marketplace, then lets you choose where to install. The plugin carries all five skills. This form needs Claude Code 2.1.275 or newer; from your shell, `claude plugin install airgap-anything --marketplace mftnakrsu/airgap-anything` does the same with 2.1.292 or newer. On older versions, add the marketplace first:

```
/plugin marketplace add mftnakrsu/airgap-anything
/plugin install airgap-anything@airgap-anything-marketplace
```

### Codex

```bash
codex plugin marketplace add mftnakrsu/airgap-anything
```

Then install airgap-anything from the plugin directory in Codex or the ChatGPT desktop app.

### Cursor and other agents that support Agent Skills

```bash
npx skills add mftnakrsu/airgap-anything -g
```

This installs all five skills. To install one, add `--skill`, for example `npx skills add mftnakrsu/airgap-anything -g --skill airgap-transfer`.

`-g` installs them for your user, so every project has them; without `-g` they go into the current project only. Add `-a` and an agent ID to choose the agent, for example `-a cursor`, `-a codex`, `-a opencode` or `-a antigravity`. The [skills CLI](https://github.com/vercel-labs/skills) supports Claude Code, Codex, Cursor, OpenCode and 75 more agents; its [agent list](https://github.com/vercel-labs/skills/blob/main/docs/agents.md) has the IDs. This route needs Node.js 22.20 or newer.

### Without internet

On a connected machine, in a clone of this repository:

```bash
for skill in airgap-architect airgap-transfer airgap-agent airgap-rag airgap-install; do
  git archive --format=tar.gz --prefix=$skill/ -o $skill.tar.gz HEAD:plugins/airgap-anything/skills/$skill
  sha256sum $skill.tar.gz > $skill.tar.gz.sha256
done
```

Carry the ten files in, then:

```bash
for skill in airgap-architect airgap-transfer airgap-agent airgap-rag airgap-install; do
  sha256sum -c $skill.tar.gz.sha256 && mkdir -p ~/.claude/skills && tar -xzf $skill.tar.gz -C ~/.claude/skills/
done
```

`~/.claude/skills/` is where Claude Code keeps personal skills; Codex reads `~/.agents/skills/`. Use your agent's own skills folder if it differs. Nothing else is needed: the skills are markdown.

## Use

Ask your agent, in your own words, on a machine with internet access:

> Design an air-gapped LLM platform for my organization.

You do not need to name the skill. Claude Code picks it when a request is about designing, planning or sizing a system for an air-gapped, offline or on-premises network, and leaves other requests alone; [a test](evals/results/2026-11-24-triggering.md) checks this in English and Turkish. In Claude Code you can also start it directly: with `/airgap-anything:airgap-architect` after the plugin install, or with `/airgap-architect` when it is installed as a personal or project skill.

The agent then works through these steps and ticks them off as it goes:

| # | Step | Who |
|---|---|---|
| 1 | Interview: people, departments, privacy, hardware, operations | the agent, one question at a time |
| 2 | Tier and per-layer floors | the agent, from the tier table |
| 3 | GPU, server and power sizing, every step written out | the agent, from the sizing procedure |
| 4 | One decision per layer, from the layer guides and the catalog | the agent |
| 5 | Transfer manifest | the agent, from the catalog entries |
| 6 | Blueprint, and the agent block in `AGENTS.md` | the agent |
| 7 | Self-review against a checklist, until every item holds | the agent |
| 8 | Your approval, then hand-off to an implementation plan | you |

### Carrying it in

Once the blueprint is approved, ask in your own words, for example "prepare everything in the transfer manifest for our USB disks". `airgap-transfer` then works through these steps:

| # | Step | Who |
|---|---|---|
| 1 | A few questions: where to build the bundle, where each model comes from, the medium or the channel's file limit | the agent |
| 2 | The plan: every item, the tools, the known sizes | the agent |
| 3 | Your approval, then the download | you, or the agent after you approve |
| 4 | Manual items: add files or mark them not needed | you |
| 5 | Checksums, split, volumes, inventory, runbook or agent rules | the agent |
| 6 | Self-check, then one medium at a time, read back | the agent |

Inside, on any Linux host, the runbook checks every file with `sha256sum -c` before anything is loaded. When a file is missing or damaged, it names the file and the volume it came on.

### Coding agents inside

A coding agent installed as-is tries to reach a model catalog, telemetry, update servers and web search on its first start. Once the blueprint exists, ask for it in your own words, for example "set up a coding agent for the developers inside". `airgap-agent` interviews you (eight questions, each with a default), then writes `docs/airgap/agents.md` and the configuration under `docs/airgap/agents/<tool>/user/` and, for central enforcement, `docs/airgap/agents/<tool>/central/`. It adds the tool archives, MCP packages and every outbound switch to the transfer manifest, and `airgap-transfer` carries the configuration folders in as project files.

Which tool:

- **Qwen Code** is the default for an open-weight model.
- **Codex CLI** when the model server passes a `/v1/responses` smoke test and you want central enforcement and a sandbox.
- **opencode** when the team already uses it. Version 2.4.1 is pinned, and its egress check is mandatory.
- **Claude Code** only on a private Claude route. It is never configured against an open-weight model: Anthropic ["doesn't support routing Claude Code to non-Claude models through any gateway"](https://code.claude.com/docs/en/llm-gateway).

Three checks run inside, in order, with no LLM: the install checksum and version, a smoke test that forces a tool call against the internal model, and an egress check that shows every address the tool contacts. A tool whose egress check shows an unexpected address is not released to developers.

### Searchable documents inside

Turn on document features in Open WebUI inside a closed network and it tries to download an embedding model on its first start, scanned PDFs come back empty, and nobody knows how long the first load takes. Once the blueprint exists, ask in your own words, for example "make our documents searchable inside". `airgap-rag` first asks which platform you want and waits for your answer, unless you already named one: Open WebUI knowledge bases (recommended), a RAG server (RAGFlow), or something else. For something else it records the tool's version and documentation link, marks every value it cannot verify as `unverified`, and still applies the air-gap checklist. Its other questions each have a default, and it writes `docs/airgap/rag.md` and the configuration under `docs/airgap/rag/`. It adds the images, models and every outbound switch to the transfer manifest, and `airgap-transfer` carries the two project paths in.

How documents become text:

- **Open WebUI's built-in extractor** (pypdf) for mostly digital PDF and Office files.
- **docling-serve** for scanned PDFs and tables, with OCR models carried in.
- **The local agent with `pdftotext`** for an LLM wiki: markdown files in a git repository that coding agents read.

Documents from inside the network never go to a cloud agent outside it: a copy that has left cannot be taken back. The agent on the connected side may convert only public documents.

The first load is sized step by step: extraction time, chunks, embedding time and index size, each number sourced or marked `estimate`. In a hurry, a fast path shows the same sizing as one summary table with the defaults recorded as assumptions.

Five checks run inside, with no LLM: install, retrieval, OCR for each language, access and egress. A service whose egress check shows an unexpected address is not released to users. The skill writes a bulk-load runbook too; the Open WebUI API endpoints in it were read from source at v0.13.4, because the docs no longer document them.

### Installing inside

The blueprint leaves deployment files out on purpose, and the transfer's runbook ends at "continue with the implementation plan". Without a plan, the people inside write the Compose file or the manifests, place the egress settings, pick a start order and guess what "healthy" looks like, with no internet and often no LLM. Once the blueprint is approved, ask in your own words, for example "write the install for our design". `airgap-install` asks the few questions the blueprint and the manifest leave open (whether the blueprint is approved, the hosts, where data and models live, TLS, who runs the install), each with a default, and writes `docs/airgap/install/plan.md`: the start order, the files, the ports, the health checks and a table that copies the GPUs of blueprint section 5. It shows the plan and waits; nothing else is written before your yes.

Then it writes, under `docs/airgap/install/`:

- **The deployment files.** Docker Compose, or Kubernetes manifests for k3s, RKE2 or an existing cluster. Every image carries the manifest's tag, never `latest`; Compose services have `pull_policy: never` and Kubernetes containers name the local registry, so a missing image fails at once instead of reaching for an internet that is not there. For k3s and RKE2 it also writes the registry and server configuration; for an existing cluster it writes the manifests and a step for the cluster owners' answers, never a cluster install.
- **The runbook.** `INSTALL.md` for people, or `AGENTS-INSTALL.md` for an agent inside, or both. Every step has a Why, the commands, the output to **Expect** and what to do **If not**. Secrets are generated inside, in a step with `openssl rand`; no secret is written to any file.

It deploys the blueprint's server components and those `airgap-rag` chose. The coding agents of `airgap-agent` are command-line programs on each developer's machine, so the runbook hands off to `docs/airgap/agents.md`. It adds the rows the files need to the transfer manifest (the project files `docs/airgap/install/` and, for example, the NVIDIA device plugin image), marked "(from airgap-install)", and `airgap-transfer` carries the folder in like every other project file; its `INSIDE.md` ends with "continue with install/INSTALL.md". It downloads nothing, runs nothing and writes no programs or scripts into the project.

## What you get

```
your-project/
├── docs/airgap/blueprint.md            the blueprint (under docs/superpowers/specs/ with superpowers)
├── docs/airgap/transfer-manifest.md    images, models, packages and settings to carry in
├── docs/airgap/transfer-plan.md        the transfer's answers, items and volumes
├── docs/airgap/agents.md               the coding-agent decisions and the checks to run inside
├── docs/airgap/agents/<tool>/          the configuration (user/) and central policy (central/) per tool
├── docs/airgap/rag.md                  the document-search decisions, the sizing and the checks to run inside
├── docs/airgap/rag/                    the platform's configuration, the bulk-load runbook and the wiki steps
├── docs/airgap/install/                the install plan, the runbook (INSTALL.md), and the Compose or Kubernetes files
└── AGENTS.md                           instructions for the agent that builds it inside the network
```

The bundle itself lives outside the repository, with `SHA256SUMS`, `INVENTORY.md` and `INSIDE.md` (or `AGENTS-INSIDE.md`) on every volume. Inside, people follow the runbook, an agent follows its rules, and nobody needs internet access.

The [department example](examples/department/blueprint.md) is a complete blueprint for 180 people in four departments, one 671-billion-parameter model on eight 141 GB GPUs:

| Layer | Decision |
|---|---|
| `llm-serving` | `vllm`, one replica on all eight GPUs, prefix caching off so departments share no cached prompts |
| `llm-gateway` | `litellm`, for per-department keys, budgets and audit |
| `ui` | `open-webui`, one instance per department |
| `identity` | `keycloak` federated to Active Directory |
| `observability` | `prometheus` and `grafana` |
| `orchestration` | `docker-compose` |
| `state` | `postgresql` and `valkey` |
| `registry` | `harbor` |

Tier T2. Peak concurrency 9 to 18 requests in flight. 8 GPUs in 1 server, about 10.1 kW. Every number has its arithmetic in the blueprint, and every decision lists the alternatives it beat.

## Tiers and sizing are separate

A tier (T1 single team, T2 department, T3 enterprise) measures how complex the organization is: how many people and departments, and whether audit, isolation or zero downtime is required. It selects patterns such as "gateway or not" and "Compose or Kubernetes".

GPU count is a different question. It comes from the size of the model, the kind of usage and the headcount. A small team that serves a very large model needs many GPUs at T1.

Sizing covers memory, not speed. Every blueprint carries a "benchmark before production" step.

## Evidence labels

Every catalog entry, threshold and default carries one label.

| Label | Meaning |
|---|---|
| `field` | Verified in a real deployment by a named person |
| `docs` | Taken from official project or vendor documentation, or, where the documentation is silent, from the project's source code at the release tag; the URL is recorded |
| `estimate` | Reasoned or community-sourced; verify before relying on it |

A decision inherits the weakest label among its inputs. Every decision that rests on an estimate is listed in the blueprint's verification section.

## Scope

In version 0.6:

- Layer guides for the inference engine and the LLM gateway, and per-tier defaults for UI, identity, observability, orchestration, state stores and artifact registry.
- Sizing from organization answers, a transfer manifest, and a self-review.
- `airgap-transfer`: a plan and fetch commands from the transfer manifest, a checked bundle split across media, and a runbook or agent rules for the inside.
- `airgap-agent`: the choice of coding-agent tool, its configuration and central policy with outbound connections off, the model server's requirements, offline MCP servers, and three checks for the inside.
- `airgap-rag`: the choice of platform (the user's), extraction and OCR, embedding and reranker models, the vector store, a sizing of the first load, the configuration, a bulk-load runbook, and five checks for the inside.
- `airgap-install`: an install plan you approve, the deployment files (Docker Compose, or Kubernetes manifests for k3s, RKE2 or an existing cluster), a runbook of commands with the output to expect and what to do when it differs, and the rows the files add to the transfer manifest.

Not in version 0.6:

- Helm charts, upgrades, high availability beyond what the blueprint decides, CI/CD and GitOps. `airgap-install` writes the installation for the design; it installs, runs and downloads nothing and does not operate it.
- A cluster install on a cluster you already run: its owners' process is a step of the runbook.
- A recommendation of which model to run, for the architect, the coding agents or the chat model. The embedding and reranker models of `airgap-rag` are chosen with their reasons, not ranked.
- Guides for data, CI/CD and security layers.
- Compliance mappings.

## Works with superpowers

When [superpowers](https://github.com/obra/superpowers) is installed, the blueprint is written where its specs live and handed to `superpowers:writing-plans` after you approve it. Without superpowers the skills work on their own.

## Privacy and network access

The plugin is Markdown, JSON and an icon: no code, no server, nothing collected, nothing sent to its authors or anyone else. Your agent reads the skills under its own terms.

- `airgap-architect` needs no network access. It writes the blueprint, `docs/airgap/transfer-manifest.md` and an `AGENTS.md` block in your project.
- `airgap-transfer` proposes download commands for what the transfer manifest lists: container images from their registries (for example Docker Hub, `ghcr.io`, `quay.io`), model files from Hugging Face, and packages from the release pages the catalog names. It runs them only after you approve the plan, from your machine straight to those services. A Hugging Face token is read only from `HF_TOKEN` in your environment and never written to a file.
- `airgap-agent` downloads nothing and runs nothing: it writes configuration and the checks, with keys named as environment variables and never written to a file. The tools it sets up have outbound connections of their own; switching them off is its job, and the egress check proves it inside.
- `airgap-rag` downloads nothing and runs nothing: it writes configuration, a bulk-load runbook and the checks, with keys named as environment variables and never written to a file. The platforms and extractors it sets up have outbound connections of their own; its egress check proves they are off inside. Documents from inside the network never go to a cloud agent.
- `airgap-install` downloads nothing and runs nothing: it writes deployment files and a runbook, with secrets generated inside the network by a runbook step and never written to a file. It writes no programs or scripts into your project.
- The interview asks about the organization (headcount, departments, hardware), not about people.

The full policy is on the [privacy page](https://airgap-anything.mefby.com/project/privacy/).

## Disclaimer

airgap-anything is a design aid, not professional advice. Its sizing, component choices, versions and commands come from public documentation and from estimates, and every value is labelled as one or the other. They can be wrong, incomplete or out of date for your environment. Verify every number, choice, version and command, and run the benchmark step of the blueprint, before you buy hardware, sign an order or deploy anything. You use it at your own risk: the software is provided "as is", without warranty of any kind, under the MIT license, and the authors are not liable for any damage, loss or cost arising from its use.

## Contributing

The catalog is the part that ages, and it is markdown: adding or re-verifying a component is a small pull request. [CONTRIBUTING.md](CONTRIBUTING.md) explains how. One rule above all: nothing is written from memory.

Logo files and their usage rules are in the [brand guide](assets/brand/BRAND.md).

## License

MIT. See [LICENSE](LICENSE).

## Türkçe

`airgap-anything`, internete kapalı (air-gapped) ağlar için agent skill'lerinden oluşan bir plugin'dir. Kurumunuzu anlatırsınız; agent'ınız tüm sistemi tasarlar, GPU'ları hesaplar, ağın içine taşınması gereken her şeyi listeler ve bunu öbür tarafta kendini denetleyen bir pakete dönüştürür.

Skill'ler düz markdown'dır: betik yok, bağımlılık yok, klasörden başka kurulacak bir şey yok. Claude Code, Codex, Cursor ve [Agent Skills](https://agentskills.io) okuyan her agent'ta çalışır; internete kapalı ağın içinde, yerel bir modelle de çalışır.

`airgap-architect` kurumunuzla kısa bir görüşme yapar ve bir blueprint yazar: her katman için gerekçesi ve alternatifleriyle bir karar, her adımı yazılmış GPU, sunucu ve güç hesabı, ağa taşınacak her şeyin listesi. `airgap-transfer` bu listeyi kendini denetleyen bir pakete çevirir: önce sizin onayladığınız indirme komutları, SHA-256 listesi, disklere bölme, envanter ve içeride insanlar için bir çalıştırma kılavuzu ya da içerideki agent için kurallar. İçeride hiçbir adım internet ya da LLM gerektirmez. `airgap-agent` ise içerideki geliştiriciler için bir kodlama agent'ı hazırlar: aracı seçer, telemetri, güncelleme ve web erişimini kapatan yapılandırmayı yazar ve tüm dosyaları aktarım listesine ekler; hiçbir şey indirmez ya da çalıştırmaz. `airgap-rag` ise içerideki belgelerinizi aranabilir yapar: platformu siz seçersiniz, ilk yüklemenin süresi adım adım hesaplanır, ağın içindeki belgeler hiçbir zaman dışarıdaki bir bulut agent'a gönderilmez ve hiçbir şey indirilmez ya da çalıştırılmaz. `airgap-install` ise onaylanmış tasarımın kurulumunu yazar: Docker Compose dosyaları ya da Kubernetes manifest'leri ve ağın içindeki kişiler için, her adımında komutu, beklenen çıktıyı ve çıktı farklıysa ne yapılacağını söyleyen bir çalışma kılavuzu; hiçbir şey indirmez ya da çalıştırmaz, projeye betik yazmaz ve hiçbir parolayı dosyaya koymaz.

**Kurulum.** Bir kez kurarsınız; sonrasında yalnızca sorarsınız. Claude Code oturumunda:

```
/plugin install airgap-anything --marketplace mftnakrsu/airgap-anything
```

Bu biçim Claude Code 2.1.275 veya üstünü ister. Daha eski sürümlerde önce marketplace'i ekleyin:

```
/plugin marketplace add mftnakrsu/airgap-anything
/plugin install airgap-anything@airgap-anything-marketplace
```

Codex'te `codex plugin marketplace add mftnakrsu/airgap-anything`, ardından plugin dizininden kurun. Cursor ve Agent Skills standardını destekleyen diğer agent'larda (agent seçmek için `-a`, örneğin `-a cursor`):

```bash
npx skills add mftnakrsu/airgap-anything -g
```

İnternetsiz kurulum için yukarıdaki [Without internet](#without-internet) bölümüne bakın.

**Sorumluluk reddi.** airgap-anything bir tasarım yardımcısıdır, profesyonel tavsiye değildir. Boyutlandırma, bileşen seçimleri, sürümler ve komutlar herkese açık dokümanlardan ve tahminlerden gelir ve hangisi olduğu her değerde yazılıdır; sizin ortamınız için yanlış, eksik ya da güncelliğini yitirmiş olabilirler. Donanım almadan, sipariş vermeden ya da kurulum yapmadan önce her sayıyı, seçimi, sürümü ve komutu doğrulayın ve blueprint'teki benchmark adımını çalıştırın. Kullanım sizin sorumluluğunuzdadır: yazılım MIT lisansıyla "olduğu gibi", hiçbir garanti olmadan sunulur ve kullanımından doğan hiçbir zarar, kayıp ya da maliyetten yazarlar sorumlu değildir.

**Kullanım.** İnternete bağlı bir makinede agent'ınıza kendi cümlenizle sorun, örneğin:

> Kurumum için internete kapalı bir LLM platformu tasarla.

Skill'in adını söylemeniz gerekmez: Claude Code, internete kapalı, çevrimdışı ya da kurum içi bir ağ için sistem tasarlama, planlama veya boyutlandırma isteklerinde skill'i kendisi seçer, başka isteklerde seçmez. Bunu Türkçe ve İngilizce isteklerle ölçen bir test vardır. Claude Code'da skill'i doğrudan da başlatabilirsiniz: plugin olarak kurduysanız `/airgap-anything:airgap-architect`, kişisel ya da proje skill'i olarak kurduysanız `/airgap-architect` yazın.
