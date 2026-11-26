# 小鲸 · XiaoJing

An AI companion for QQ that keeps long-term memory, speaks in short human sentences, and occasionally comes to you on its own.

> 中文版 / Chinese version: [README.zh-CN.md](README.zh-CN.md)
> Install guides under `docs/` are written in Chinese.

> **Status: early test build.** This is the version I use every day while I keep fixing it.
> The first stable release is planned for **mid-2027**. File layout, config keys and plugin
> behaviour can change before then — read it, run it, but do not treat it as production-ready.

**What this repo is — and what it is not.** Everything in this repository is our own work: a heavily modified memory plugin, three smaller plugins, the two-layer language filter, the persona constraints, and the watchdog scripts. It *depends on* two upstream projects that are **not bundled and not re-distributed here**:

- **[AstrBot](https://github.com/AstrBotDevs/AstrBot)** — the chat runtime (upstream, **AGPL-3.0**, actively developed)
- **NapCat** — the OneBot v11 bridge between QQ and AstrBot (upstream **has stopped maintenance** and publishes **no license**; see [docs/napcat.md](docs/napcat.md) for its current status and how to obtain it yourself)

You install both yourself, under their own terms. This repository contains **no upstream binaries, no QQ client, no model files and no upstream source dumps** — only our code, our patches and our documentation.

**The core of this project is the plugin layer we designed ourselves** — long-term memory, the two-layer language filter, and the small QQ-side add-ons — running *on top of* AstrBot and NapCat. Those two give it a host and a connection; everything that makes it behave like a particular someone is ours.

**What this is.** XiaoJing is not a boxed application you double-click. It is a reproducible engineering setup: a chat brain that keeps long-term memory and speaks in short, human sentences, plus a small army of watchdog scripts that keep the whole chain alive. Everything that took weeks of trial and error — the memory pipeline, the persona hygiene rules, the port wiring, the version guards — is written down here as code and documentation.

**Why it feels different.** Most "AI companion" projects stop at a system prompt. This one treats memory as a first-class subsystem: every day gets a first-person diary entry written only from that day's real conversations, those entries are injected into the system prompt (not left to retrieval luck), and the model is explicitly told that anything not in the record did not happen — so it answers "I don't remember" instead of inventing a story. On top of that, a two-layer language filter strips the tell-tale stock phrases that make bots sound like bots, while a set of real, hand-picked example sentences keeps the voice short, dry and human.

**What is actually new here.** (1) A diary-based recall design where "what did we do last night" is answered from a written record rather than vector search. (2) Language hygiene implemented twice over — positive examples in the persona, regex backstops in code — so the same stock phrase can neither come out of the model nor slip through the forwarder.

**Why it is convenient.** Every port is fixed and documented (6099 NapCat, 6185 AstrBot, 6199 reverse WebSocket), one script starts the whole stack in order, one VBS entry point makes it run at login without a console window, and every watchdog knows how to bring its own piece back from the dead. No cloud service, no proprietary API beyond a normal OpenAI-compatible endpoint, no data leaving your machine.

**Deploying it with an agent.** The documentation was written to be executed, not just read: clone the repository, open it in a coding agent such as DeepSeek Harness, Claude Code or Codex CLI, and ask it to deploy the project. The agent can follow ``docs/quickstart.md`` step by step — install Python dependencies, drop the plugins into AstrBot, wire NapCat's reverse WebSocket, edit ``scripts/_config.ps1`` to match your paths, and run ``start-stack.ps1 -DryRun`` to check the result. You still have to log in to QQ once and plug in your own LLM key; everything around that can be handled by the agent.

---

## Architecture

```
                    +------------------------------+
   QQ client ------>|  NapCat (OneBot v11)         |
   (QQNT)          +--------------+---------------+
                                  | reverse WebSocket :6199
                                  v
   +------------------------------------------------+
   |  AstrBot (Python)                              |
   |   +- astrbot_plugin_memories   memory / diary / proactive |
   |   +- astrbot_plugin_forward    message forwarding          |
   |   +- astrbot_plugin_ocr        image text into the chat     |
   |   +- astrbot_plugin_video_bridge  video bridge              |
   +------------------------------------------------+
```

- **AstrBot** — the chat brain on the QQ side (upstream, **AGPL-3.0**, not bundled)
- **NapCat** — turns QQ into an OneBot v11 endpoint (upstream, **maintenance stopped, no license published**; obtain it yourself, see [docs/napcat.md](docs/napcat.md))
- **astrbot_plugin_memories** — the plugin we modified most: event memory, cake weighting, forgetting/merging, daily diary, first-person recall, proactive messages, language filtering
- **scripts/** — keepers and guards (restart AstrBot when it dies, pin the QQ version when QQ tries to auto-upgrade)

---

## What she can do

- Private and group chats, short and colloquial; personality comes from your own persona — the plugins only make sure she does not sound like an AI
- Long-term memory: daily diary (that day only, first person, covering the whole day), weekly reports, people cards, preferred forms of address
- Ask "what did we do last night" and she can answer — the diary is injected into the system prompt, it is not left to retrieval luck
- No fabrication: if it is not in the record she says she does not remember; she never pretends to have gone to school or taken exams
- Language filter: two layers that strip stock bot phrases before and after generation
- Proactive messages: one short line when there is something to say ("are you busy?"), nothing when there is not; a few times a day at most

---

## Quick start

> Full steps in ``docs/quickstart.md``. This is just the map.

0. **The lazy way**: hand the repository to a coding agent (DeepSeek Harness / Claude Code / Codex CLI) and say "deploy this following docs/quickstart.md". You only need to log in to QQ and fill in your model key.
1. Install dependencies: Python 3.10+, QQ (QQNT)
2. Install AstrBot yourself (upstream, AGPL-3.0) as described in ``docs/astrbot.md``, then copy ``astrbot/plugins/*`` into ``AstrBot/data/plugins/``
3. Get an OneBot v11 bridge — we used **NapCat**, whose upstream has stopped and ships no license, so the repo explains three ways to obtain it yourself and how to verify the file: see ``docs/napcat.md`` and ``napcat/CHECKSUMS.txt``. Point its reverse WebSocket at ``ws://127.0.0.1:6199/ws``
4. The persona is not included — write your own and paste it into AstrBot's persona page.
   To keep her from sounding like an AI, copy the banned-phrase list from ``astrbot/persona/banned-phrases.md``.
5. Follow ``docs/autostart.md`` to set up the keeper scripts; after that they keep themselves alive

---

## Repository layout

```
.
+- README.md                  English (this file)
+- README.zh-CN.md            Chinese
+- LICENSE                    our own code (MIT)
+- THIRD-PARTY.md             upstream projects and their licenses
+- docs/                      install, configuration, troubleshooting
+- astrbot/
|  +- plugins/                memory / forwarding / OCR / video bridge
|  +- persona/banned-phrases.md   language constraints only, no identity
|  +- config.example.json     key AstrBot settings
+- napcat/                    QQ version guard + OneBot config sample
+- scripts/                   keeper scripts (PowerShell + VBS)
```

---

## What you have to provide

- A working LLM API (any OpenAI-compatible endpoint) configured as an AstrBot provider
- A QQ account for the bot (a spare one is recommended) plus a NapCat login
- Optional: a Live2D model, if you want her to have a face on your desktop. A free open-source one fits: [「免费 live2D 模型｜Deepseek 小鲸鱼」](https://www.bilibili.com/video/BV1KmxY66EZ3/) by @神宫凉子 (art) and @霓虹猫_NeonNeko (rigging) — read the usage notice inside its zip. This repository contains no model files and no Live2D integration code.

---

## Notes

- This grew out of one person's daily use and constant tinkering: the parameters are tuned for a very specific use case, not general-purpose optima. Changing the model or the persona means re-tuning.
- Third-party upstream parts are shipped as patches and instructions only, never as full re-distributions; fetch them under their own licenses.
- **No binaries are hosted here.** We do not mirror NapCat, the QQ client, AstrBot's source or any Live2D model — every download happens on the upstream or mirror you choose, and you are responsible for checking it (SHA-256 list in `napcat/CHECKSUMS.txt`).
- Commit messages follow `<type>: <one line>` — see [docs/commit-style.md](docs/commit-style.md) and `scripts/commit.ps1`.

---

## Credits and attribution

Nothing third-party is re-published here as a whole; everything borrowed is listed file by file in [THIRD-PARTY.md](THIRD-PARTY.md).

- **astrbot_plugin_memories** — original plugin by **若剑清 (Ruojianqing)**, MIT, v0.5.1. The copy in this repo is a heavily modified version; three attribution lines sit at the top of every `.py` file, `metadata.yaml` keeps the original author, and the original `LICENSE` is preserved.
- **AstrBot**, **NapCat**, **QQNT** — runtime dependencies, fetched by the user, not bundled.
- **Ideas borrowed** (code written by us): pre-send self-check pattern from the `astrbot_plugin_fish_heart` plugin; QQ version guard and OneBot reverse-WS setup from NapCat's docs.
- **Live2D model** recommended in the docs — art by @神宫凉子, rigging by @霓虹猫_NeonNeko, editing by @泣零7ero; not bundled, licensed by its own usage notice.
