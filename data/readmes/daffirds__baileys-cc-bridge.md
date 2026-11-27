<p align="center">
  <img alt="A WhatsApp group on movie night. Ben says there's nothing to eat, you ask if anyone wants to order, and Rina wants pizza with extra cheese. Mochi Bot, an AI agent with its own number, sends a screenshot of the pizza cart it filled on GrabFood and asks whether to order. You say go, and it confirms the order, signed Assisted by Claude. Next to the chat, the agent as a robot on a sofa, ordering on a food delivery site from its laptop." src="assets/banner.svg" width="100%">
</p>

<p align="center">
  <b>Put Claude Code or Codex in your WhatsApp group. It does the work on your Mac and answers in the chat.</b>
</p>

<p align="center">
  <img alt="macOS" src="https://img.shields.io/badge/OS-macOS-6e7681">
  <img alt="Claude Code and Codex" src="https://img.shields.io/badge/engines-Claude%20Code%20%7C%20Codex-d97757">
  <a href="LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-25d366"></a>
</p>

A small daemon for your Mac, written in Go. It links a WhatsApp number to the Mac the way WhatsApp Web
does, through [Baileys](https://github.com/WhiskeySockets/Baileys), and gives each WhatsApp chat you pick its own
Claude Code or Codex session.

## How it works

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/how-it-works.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/how-it-works-light.svg">
    <img alt="Every message in the WhatsApp group goes into the agent's Claude Code session on your Mac; it stays quiet on Ben's. On yours it opens GrabFood in the browser and fills a cart, reacting to Rina's extra cheese on the way. Its tool calls come back as the chat's next bubbles: send_file as the cart screenshot asking whether to order, and after your go, send_message as the order confirmation." src="assets/how-it-works-light.svg" width="100%">
  </picture>
</p>

- The bridge is a linked device of the number, the way WhatsApp Web is, through
  [Baileys](https://github.com/WhiskeySockets/Baileys).
- Each chat you pick gets its own CLI session (`claude -p` or `codex app-server`), started by its
  first message and resumed after a restart.
- Every new message goes into that session, even while the agent is in the middle of a task.
- The agent acts on WhatsApp through MCP tools tied to its chat. Nothing is sent unless the agent
  calls one; the bridge never posts anything of its own.
- The CLIs use their own logins, so the work counts against your Claude or ChatGPT plan. The bridge
  talks only to WhatsApp and `127.0.0.1`.

## Get started

You need macOS, Node 22.18+, and Claude Code and/or Codex installed and logged in.

> [!TIP]
> _Run this on your always-on Mac mini server._

In the terminal:

```sh
npm install -g baileys-cc-bridge
baileys-cc-bridge install        # runs in the background from now on, and opens its panel
```

The panel opens in your browser on `127.0.0.1:9999` and shows a QR code. Scan it from the phone whose 
number the agent will use (WhatsApp → Settings → Linked devices). A spare number works best. Your own 
works too, but then the agent writes as you.

Then pick the chats it listens to; it ignores every other chat. Each one gets its own engine, model,
folder and prompt.

<p align="center">
  <img alt="The panel: the linked account, Mochi Bot, with Claude and Codex both ready, and three conversations. The open one, a group, shows its engine, permissions, model, effort, footer, folder and system prompt." src="assets/panel.png" width="760">
</p>

Before you add a group: anyone in it can ask the agent to do things on your Mac. Keep groups on
`auto` or `readonly` ([Settings](#settings)), and use `full` only where you trust everyone.

In a group it reads along and joins in when it can help, no tag needed, as in the picture at the
top. In a direct chat every message is for it, and the chat's folder can be a project of yours:

> **You:** run the tests and tell me what fails<br>
> **Mochi Bot (_Assisted by Claude_):** 2 of 148 fail, both in `auth_test.go`. The token expiry check ignores timezones 🕐<br>
> **You:** fix it and send me the diff<br>
> **Mochi Bot (_Assisted by Claude_):** 📄 token-expiry.diff<br>
> **Mochi Bot (_Assisted by Claude_):** all green now ✅ 

## Tools

| Tool | |
|---|---|
| `send_message` | text; `reply_to` quotes, `mentions` @-mentions by number, `mention_all` the whole group |
| `send_file` | photos, videos and audio inline, anything else as a document; `voice` for voice notes |
| `send_sticker` | any image, as a sticker |
| `react` | an emoji on a message (default: the latest) |
| `chat_info` | a group's name, description and members, or who a direct chat is with |
| `schedule_job` · `list_jobs` · `cancel_job` | a task back in the chat later: once (`in 10m`, `at` a local time) or on `cron` (`0 8 * * 1-5`) |

A tool acts on its own chat. The send tools and `chat_info` also take `chat`, to act on another chat
instead, but only one you picked in the panel. Incoming attachments are saved in the agent's folder,
and the agent gets the path.

## Settings

The panel edits `~/.baileys-cc-bridge/<number>/config.yaml` ([example](config.example.yaml)). A change
applies from the chat's next message, after the agent has finished what it was doing.

| Key | Default | |
|---|---|---|
| `engine` | `claude` | `claude` or `codex` |
| `model`, `effort` | the CLI's | |
| `autonomy` | `full` | `full`: no prompts, no sandbox · `auto`: the engine's own reviewer · `readonly` |
| `workdir` | the chat's own folder | where the agent runs |
| `system_prompt` | one for groups, one for direct chats | added after the bridge's fixed instructions on how to use WhatsApp |
| `footer` | `true` | _Assisted by Claude_ (or _Codex_) under what the agent sends; handy on your own number |

## Good to know

- If the bridge or the Mac is off, the messages that arrive meanwhile are lost. It doesn't catch up
  afterwards.
- Only one process can be connected to WhatsApp at a time, and `run`, `login`, `logout` and `chats`
  each connect. While the bridge is running, the others refuse to start.

## Commands

| | |
|---|---|
| `install` · `uninstall` | run in the background (launchd), or stop |
| `ui` | open the panel |
| `run [-debug] [-addr] [-open]` | run in this terminal instead |
| `login [-phone N]` · `logout` | link or unlink the number from the terminal |
| `chats [filter]` | the number's JID and its groups' JIDs |

After `npm update -g baileys-cc-bridge`, run `install` again to restart on the new version. Everything
lives in `~/.baileys-cc-bridge/`: the linked device, `bridge.log`, and one folder per linked number
with its settings and its chats' sessions. The transcripts stay where Claude Code and Codex keep
their own.

## Building from source

With Go 1.26: `go build -o ~/.local/bin/baileys-cc-bridge ./cmd/baileys-cc-bridge`. `web/` is the
panel (Vite + React; `npm run build` writes the embedded `internal/webui/dist`), `sidecar/` the
Baileys side, and `scripts/build-npm.sh` builds the binary the npm package ships.

## Bottom note

Personally I built this as my home agent, it pays bills, buys things on Shopee, etc. It lives on my home server and hangs out in our family group, telling everyone to chill when we start arguing. 😅 My mom also uses it for our prayer reminders.

## License

[MIT](LICENSE)
