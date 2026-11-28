<p align="center"><img src="docs/assets/wacrew-mark.svg" alt="WACrew" width="96"></p>

<h1 align="center">WACrew</h1>

<p align="center">
  <b>An AI that answers your WhatsApp in your own voice, so clients talk to you, not to a bot.</b><br>
  It sorts every group and chat by who has waited longest, writes with your punctuation and rhythm,<br>
  and delivers at a human pace. You approve each reply or leave a chat on auto.<br>
  Open source, self-hosted, with an MCP server so Claude Code, Cursor or Codex can work the chats too.
</p>

<p align="center">
  <a href="https://railway.com/deploy/wacrew?referralCode=8ZIi5q&utm_medium=integration&utm_source=template&utm_campaign=readme"><img alt="Deploy on Railway" src="https://railway.com/button.svg" height="32"></a>
  <a href="https://www.hostinger.com/vps-hosting?REFERRALCODE=ORISHODIRBUH"><img alt="Deploy on Hostinger" src="docs/assets/deploy-hostinger-en.svg" height="32"></a>
  <br><sub>One click on Railway, a VPS with 20% off on Hostinger (referral links that help fund the project), or <a href="#quick-start">run it on your machine</a>.</sub>
</p>

<p align="center">
  <a href="./LICENSE"><img alt="License: Apache 2.0" src="https://img.shields.io/badge/license-Apache_2.0-blue.svg" height="20"></a>
  <a href="https://nodejs.org"><img alt="Node 20+" src="https://img.shields.io/badge/node-%E2%89%A520-43853d.svg" height="20"></a>
  <a href="https://github.com/WhiskeySockets/Baileys"><img alt="Built with Baileys" src="https://img.shields.io/badge/built%20with-Baileys-25D366.svg" height="20"></a>
  <a href="https://github.com/sponsors/sumioshi"><img alt="Sponsor" src="https://img.shields.io/github/sponsors/sumioshi?label=Sponsor&logo=githubsponsors&color=ea4aaa" height="20"></a>
  <a href="https://modelcontextprotocol.io"><img alt="MCP server" src="https://img.shields.io/badge/MCP-37%20tools-6366f1.svg" height="20"></a>
  <a href="https://www.npmjs.com/package/wacrew-mcp"><img alt="npm" src="https://img.shields.io/npm/v/wacrew-mcp.svg?label=npm" height="20"></a>
  <a href="https://glama.ai/mcp/servers/sumioshi/wacrew"><img alt="Glama score" src="https://glama.ai/mcp/servers/sumioshi/wacrew/badges/score.svg" height="20"></a>
</p>

<p align="center">
  <a href="https://m8ven.ai/mcp/sumioshi-wacrew-nirsqy?s=readme"><img alt="M8ven Score" src="https://m8ven.ai/badge/mcp/sumioshi-wacrew-nirsqy" height="20"></a>
</p>

<p align="center"><a href="https://vibehub.academy/"><img alt="Supported by Vibehub Academy" src="docs/assets/apoio-vibehub-en.svg" height="32"></a></p>

<p align="center"><a href="https://wacrew.com.br">wacrew.com.br</a> · <a href="./README.pt-BR.md">Leia em português</a> · ⭐ <b>If WACrew helps you, a star helps others find it.</b></p>

<p align="center"><img src="docs/screenshots/demo-auto.gif" width="551" alt="The AI drafts a reply; flipping AUTO on, it types and answers on its own"></p>

<p align="center"><a href="https://wacrew.com.br/en/#video"><img src="docs/assets/vsl-en.jpg" width="640" alt="Watch the 55-second video: from WhatsApp chaos to every client answered"></a><br><sub>▶ Watch the 55-second video</sub></p>

## Why

If you sell or deliver work over WhatsApp, you know the scene: forty client groups, a four-minute voice note in the middle of a thread, the bug screenshot lost in the scroll, and the client who wrote three days ago that nobody saw.

A chatbot does not fix that. Canned answers read like a robot, clients notice, and the relationship cools down. WACrew works differently:

- **Nobody waits.** Every group and chat goes into one queue, oldest wait first, with voice notes already transcribed.
- **It sounds like you.** Replies follow your punctuation, openings and rhythm, measured on your own messages, and pass a review that blocks robotic tells before they leave.
- **It moves like a person.** Read receipt, typing, pauses between bubbles, and it stops if the client writes again or you answer from your phone.
- **You stay in charge.** Confirm mode is the default: nothing goes out without your OK. If a client asks whether it is AI, it does not lie; it stops and hands the chat back to you.

![A client conversation in WACrew: AI replies delivered in bubbles, with the client's contract, people and notes on the side](docs/screenshots/caixa-conversa.webp)

**The engine that makes it read like a person:**

| 2 | 25+ | 60 | ~30 s |
|:---:|:---:|:---:|:---:|
| writing skills: your voice and client conduct | code rules that block robot tells | history messages read before replying | median until typing starts in a live chat |

## What it does

**Nobody waits.** Every group and direct chat lands in one queue sorted by waiting time. A client's group and their private chats show up together, back-to-back messages collapse into one block, and voice notes arrive transcribed.

**Writes like you, delivers like a person.** The AI reads the history and writes with your punctuation, openings and rhythm, measured on your own past messages. Before anything leaves, a deterministic review blocks robot clichés, repeated apologies and duplicate bubbles (the generic part of it is also a standalone library, [botsmell](https://github.com/sumioshi/botsmell)). Delivery comes with read receipt, typing indicator and pauses, and it stops on its own if the client writes again or you answer from your phone.

**You stay in control.** In *Confirm* mode (the default) nothing is sent without your OK. *Autonomous* mode is turned on per chat. Every message records who wrote it: you on the phone, you on the panel, a teammate, or the AI.

| | |
|---|---|
| ![Today view: who is waiting, AI activity, signals and today's calendar](docs/screenshots/hoje.webp) **Today.** Who is waiting and for how long, what the AI is doing, signals and today's agenda. | ![2D pixel-art office with one desk per client project](docs/screenshots/escritorio.webp) **2D office.** One desk per project. When a client writes, the desk turns red right away, with sound. |
| ![Dashboard with message volume, first-reply time and who replied](docs/screenshots/dashboard.webp) **Dashboard.** Volume, first-reply time, who answered, busiest clients and deliveries per month. | ![Clients kanban board with waiting time, tags and last message](docs/screenshots/clientes-quadro.webp) **Clients.** Table and board views with contract, deliveries and waiting time per client. |
| ![Client drawer with the coding agent running in the project's repository](docs/screenshots/ficha-agente-orca.webp) **Agent bridge (optional).** If you use [Orca](https://onorca.dev), the client drawer shows the coding agent working on that project's repo and lets you send it commands. | ![Weekly Google Calendar view inside the panel](docs/screenshots/agenda.webp) **Calendar.** Your Google Calendar inside the panel, editable by you or by the AI. |

More screens in [`docs/screenshots/`](docs/screenshots): org chart, team access, notifications, project links, settings and the command palette.

## How it works

```
                          ┌────────────────────────────┐
  WhatsApp ─► collector ─►│  data/<chat>/              │◄─► web panel (Next.js, :3000)
  (Baileys)   (daemon)    │  messages.jsonl + media    │
                          │  transcripts, notes, state │◄─► MCP server (your coding agent)
                          └─────────────┬──────────────┘
                     transcriber (MLX on Apple Silicon, or an API)
```

- **Collector** (`src/`): a Baileys daemon (WhatsApp Web multi-device, no browser). Baileys is isolated behind ports and adapters in `src/whatsapp/`. It writes every message, reaction and media file to `data/<chat>/` and runs the delivery queue that sends replies at a human pace.
- **Panel** (`web/`): Next.js 16 + React 19. Inbox, conversation view, clients, dashboard, calendar, team, 2D office, settings. Live updates over SSE.
- **MCP server** (`web/mcp/server.ts`): 37 tools over the same data, for Claude Code, Codex, Antigravity, Gemini CLI, Qwen Code or any MCP client.
- **Transcriber** (`transcriber/`): Whisper large-v3 via MLX, loaded on demand and released when idle. Off a Mac, set `TRANSCRIBE_BACKEND=openrouter`.
- **Local or cloud.** Run everything on your machine, or deploy the collector and panel 24/7 with the included `Dockerfile` (a `railway.json` is provided). The local MCP can read straight from the cloud panel (`WAC_MCP_REMOTE=1`), downloading media on demand.

## Quick start

Requirements: Node.js 20+, `ffmpeg`, and a WhatsApp account to pair. Local transcription needs Apple Silicon (`uv tool install mlx-whisper`).

```bash
git clone https://github.com/sumioshi/wacrew && cd wacrew
npm install && npm --prefix web install
cp .mcp.json.example .mcp.json
npm run dev          # collector + panel + transcriber + notifier
```

Open `http://localhost:3000/config`, scan the QR code (WhatsApp › Linked devices › Link a device), pick the groups to follow and mark who is on your team. The session is saved in `auth/` and reconnects on its own.

**Run it 24/7 on a VPS.** WACrew only records what arrives while it is running: if your computer is off, messages from that period never reach the history or the queue. The repo ships a `docker-compose.yml` with a persistent volume for the WhatsApp session and data:

```bash
cp .env.example .env   # set PANEL_USER and PANEL_PASS
docker compose up -d
```

**Without compose.** The same image runs with plain Docker. The named volume keeps the WhatsApp session and data when the container is recreated:

```bash
docker run -d --name wacrew --restart unless-stopped \
  -p 3000:3000 \
  -v wacrew-data:/data \
  -e NODE_ENV=production -e PORT=3000 \
  -e AUTH_DIR=/data/auth -e DATA_DIR=/data/data \
  -e WAC_DATA_DIR=/data/data \
  -e GROUPS_CONFIG=/data/groups.config.json \
  -e WAC_GROUPS_CONFIG=/data/groups.config.json \
  -e PANEL_USER=admin -e PANEL_PASS='change-this-password' \
  ghcr.io/sumioshi/wacrew:latest
```

Then open `http://localhost:3000/config` to scan the QR code.

<a href="https://www.hostinger.com/vps-hosting?REFERRALCODE=ORISHODIRBUH"><img alt="Deploy on Hostinger" src="docs/assets/deploy-hostinger-en.svg" height="32"></a> <a href="https://railway.com/deploy/wacrew?referralCode=8ZIi5q&utm_medium=integration&utm_source=template&utm_campaign=generic"><img alt="Deploy on Railway" src="https://railway.com/button.svg" height="32"></a>

<sub>Referral links: you get a discount or credits, and the project earns a commission that helps keep it maintained. On Railway the template sets up the volume, the login and a generated password for you.</sub>

**Other clouds.** Run the prebuilt image `ghcr.io/sumioshi/wacrew` or build the `Dockerfile` on any host with a volume at `/data`. Set `PANEL_USER` and `PANEL_PASS` to protect the panel with login; without them the panel is open, which is only fine on localhost.

## MCP tools

The server is registered by `.mcp.json` (project scope). Claude Code and Qwen Code read it and ask for approval on first use.

**From npm, without cloning.** With the panel running on a VPS, add the MCP to any client with [`wacrew-mcp`](./packages/mcp):

```bash
claude mcp add wacrew -e WAC_CLOUD_URL=https://your-panel.example.com \
  -e WAC_CLOUD_USER=admin -e WAC_CLOUD_PASS=change-me -- npx -y wacrew-mcp
```

**Antigravity plugin.** The repo is also an Antigravity plugin, with the MCP and the skills (`plantao`, `autonomo`, `link-whatsapp`, `comunicacao-cliente`):

```bash
agy plugin install https://github.com/sumioshi/wacrew
```

It installs turned off. Open `/plugin` (or Customizations in the editor), turn on WACrew and fill in the panel URL, login and password; other accounts go in the URL field after a space, as below. To add only the MCP, flags go before the name:

```bash
agy mcp add -e WAC_CLOUD_URL=https://your-panel.example.com \
  -e WAC_CLOUD_USER=admin -e WAC_CLOUD_PASS=change-me wacrew npx -y wacrew-mcp
```

**More than one WhatsApp.** One server can talk to several panels. Add the others in `WAC_CONTAS` as `name=https://login:password@address`, separated by spaces (or put them after the main address in `WAC_CLOUD_URL`). Every tool then takes an optional `conta` parameter, and the agent picks the account per call. `WAC_CONTA_NOME` names the default one:

```bash
claude mcp add wacrew -e WAC_CLOUD_URL=https://work.example.com \
  -e WAC_CLOUD_USER=admin -e WAC_CLOUD_PASS=change-me -e WAC_CONTA_NOME=work \
  -e WAC_CONTAS="personal=https://admin:other-pass@personal.example.com" -- npx -y wacrew-mcp
```

| Area | Tools |
|---|---|
| Read | `listar_grupos`, `ler_mensagens`, `buscar`, `listar_contatos`, `caixa_de_entrada`, `novidades`, `resumo_do_dia`, `ler_notas`, `estado_triagem` |
| Media | `transcrever`, `ver_imagem`, `ver_video`, `assistir_video`, `ler_documento` |
| Reply | `preparar_resposta`, `revisar_texto`, `responder`, `responder_midia`, `editar_mensagem`, `reagir`, `status_envio`, `cancelar_envio`, `gerar_voz` |
| Triage and CRM | `marcar_resolvido`, `silenciar_grupo`, `anotar`, `etiquetar`, `alertar_chat`, `definir_modo`, `definir_contrato`, `registrar_feature`, `dashboard`, `editar_perfil` |
| Calendar | `agenda_ver`, `agenda_marcar`, `agenda_editar`, `agenda_apagar` |

Highlights:

- `buscar` finds text **inside transcripts** too.
- `ver_imagem` and `ver_video` hand the media to the model, which is handy for bug screenshots. `assistir_video` has a Gemini model watch a video with its audio, attached or from a link.
- `responder` returns a **ticket**. The message leaves later at a human pace: seconds in a live chat, minutes to hours in a cold one. The ticket is interrupted if the client writes or you answer by hand. `status_envio` tracks it and `cancelar_envio` cancels it.
- `gerar_voz` measures how you write from the messages you typed yourself (what the automation sent is left out) and returns a ready voice skill for your agent, split into work and personal.
- `preparar_resposta` returns your recent style and what the client left open. Pass 2 or 3 `candidatos` to `responder` and the least out-of-character one is sent.

Tool names are in Portuguese because the project started in Brazil. Descriptions are clear enough for any model, but if you are writing English prompts, here is what each name means.

<details>
<summary><strong>All 37 tools, with the English meaning and when to use them</strong></summary>

| Tool | English | When to use it |
|---|---|---|
| `listar_grupos` | list groups | Start here: lists every collected chat (groups and DMs) and the `slug` the other tools take. |
| `ler_mensagens` | read messages | Read one chat's history, text plus transcripts already made; filter by date and limit. |
| `buscar` | search | Find a term in messages and transcripts. |
| `transcrever` | transcribe | Transcribe one audio/video by `mediaPath` or `id`, or a batch of up to 8 pending ones; reuses the cache. |
| `resumo_do_dia` | summary of the day | Get every message of one chat on a given day so you can summarize it. |
| `ver_imagem` | see image | Hand a real image (screenshot, sticker) to the model. |
| `ver_video` | see video | Pull a few still frames out of a video or GIF, no audio and no cost. |
| `assistir_video` | watch video | Have Gemini watch the whole video with audio and report what is shown and said, with timestamps. |
| `ler_documento` | read document | Read the text content of a document a client sent (PDF, .docx, .txt, .csv). |
| `listar_contatos` | list contacts | Find who is who: name, role (me/team/client), DM jid and the DM slug. Always pass `busca`. |
| `preparar_resposta` | prepare reply | Step 1 of sending: call before writing anything; returns recent style and what the client left open. |
| `revisar_texto` | review text | Step 2: reviews an already written draft without sending it. |
| `responder` | reply | Send text to a group or a DM; returns a ticket and the message leaves at a human pace. |
| `responder_midia` | reply with media | Send a file: image with caption, document/PDF, voice note or video. |
| `cancelar_envio` | cancel send | Cancel a scheduled or in-flight delivery; balloons that already left stay. |
| `status_envio` | send status | Check the state of a delivery, by chat or by ticket. |
| `editar_mensagem` | edit message | Edit a message already sent by you or by the automation. |
| `reagir` | react | React to a message with an emoji. |
| `editar_perfil` | edit profile | Change the operator's WhatsApp profile: name, about/status and/or photo. |
| `marcar_resolvido` | mark resolved | Take a chat out of the pending queue until a given moment; a later client message puts it back. |
| `silenciar_grupo` | mute group | Mute or unmute a chat: messages are still collected, but it leaves the queue and stops alerting. |
| `anotar` | annotate | Write the free-form mini-CRM note of a chat, replacing the whole previous note. |
| `ler_notas` | read notes | Read the notes saved with `anotar`. |
| `alertar_chat` | alert chat | Turn the Mac notification for the human on or off when a client writes in a chat. |
| `definir_modo` | set mode | Set a chat to autonomous (the AI sends without asking) or confirm (default: waits for your OK). |
| `novidades` | what's new | Pull new messages from the chats marked for alert since the last check, and mark them seen. |
| `etiquetar` | tag | Set the tags of a chat (company/contract/personal). |
| `definir_contrato` | set contract | Set the commercial state of a chat: state, start/end, monthly value and note. |
| `registrar_feature` | register feature | Record a feature delivered to a client. |
| `dashboard` | dashboard | Business view per client: activity, contract, deliveries and the warning signals. |
| `caixa_de_entrada` | inbox | Who is waiting for a reply, and in which project, across every collected chat. |
| `estado_triagem` | triage state | Full triage state: resolved, muted, notes, last seen, copilot, alert, autonomy, tags, agent and executor. |
| `agenda_ver` | view calendar | Read the operator's Google Calendar over a date window (default today plus 7 days). |
| `agenda_marcar` | create event | Create an event in the Google Calendar. |
| `agenda_editar` | edit event | Change an event; only the fields you pass. |
| `agenda_apagar` | delete event | Delete an event from the Google Calendar. |
| `gerar_voz` | generate voice | Measure how the operator writes and return a ready voice skill, split into work and personal. |

</details>

## Configuration

Everything has a default. Copy `.env.example` to `.env` and adjust what you need.

| Variable | What it does |
|---|---|
| `PANEL_USER`, `PANEL_PASS` | Panel login. Required when the panel is reachable from the internet. |
| `OPENROUTER_API_KEY` | Posture check before sending, video watching and API transcription. |
| `COPILOT_PROVIDER`, `ANTHROPIC_API_KEY`, `COPILOT_OPENAI_API_KEY` | The in-panel copilot (Anthropic or any OpenAI-compatible API). |
| `TRANSCRIBE_BACKEND` | `mlx` (local, default on a Mac) or `openrouter`. |
| `WAC_MCP_REMOTE`, `WAC_CLOUD_URL`, `WAC_CLOUD_USER`, `WAC_CLOUD_PASS` | Point the local MCP and sync at your cloud panel. |
| `WAC_NOME_OPERADOR`, `WAC_SKILL_VOZ` | Your first name and the voice skill the AI loads before writing. |
| `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET` | Calendar and Google sign-in. |
| `CONTROL_TOKEN` | Bearer token for the external control API. |
| `DATA_DIR`, `AUTH_DIR`, `LOG_LEVEL` | Where data and the session live, and log verbosity. |

There is also a public REST API documented in [`docs/api-v1.md`](docs/api-v1.md).

## What gets stored

```
data/<chat>/
  messages.jsonl     one line per message (the AI's "database")
  reactions.jsonl    emoji reactions
  log.md             the same conversation, human-readable
  audio/ video/ image/ document/ transcripts/
```

`data/`, `auth/`, `.env` and `groups.config.json` are git-ignored. Never commit them.

## Read this before using it

- **This is not the official WhatsApp API.** WACrew links to your account as one more device, through Baileys. It is built to answer people who already talk to you. Bulk messaging and cold outreach can get your number banned.
- **No old history.** Capture starts when you pair the number.
- **Sending is real.** The panel and the control API send messages as you. Keep them on localhost or behind login.
- WACrew is an independent project, not affiliated with WhatsApp or Meta.

## Contributing

If WACrew saves you time, consider [sponsoring the project](https://github.com/sponsors/sumioshi). It pays for the hours that keep it maintained.

Issues and pull requests are welcome.

```bash
npm test            # Vitest
npx tsc --noEmit    # typecheck
```

Shared logic between the panel and the MCP lives in `web/lib/`. See [CONTRIBUTING.md](./CONTRIBUTING.md).

## Sponsors

WACrew is free and open source. Sponsors keep it maintained and get their name or logo here.

<a href="https://github.com/sponsors/sumioshi"><img src="https://img.shields.io/badge/Become%20the%20first%20sponsor-ea4aaa?style=for-the-badge&logo=githubsponsors&logoColor=white" alt="Become the first sponsor" height="28"></a>

## License

[Apache 2.0](./LICENSE) © [Rodrigo Sumioshi](https://rodrigosumioshi.com). See [NOTICE](./NOTICE).
