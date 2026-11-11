# JARVIS

A voice assistant that lives on a Windows 11 PC. Say "hey Jarvis", talk to it
in Italian, English or Russian, and it answers out loud in the same language.
Besides answering, it can write and fix code in a folder you give it, and do
things on the computer for you: open apps and sites, use your Firefox, click
through desktop programs.

It is a personal project, built and used on one machine. Everything that can
run locally does (wake word, speech recognition, memory search); the language
models run on a Claude Pro subscription and the Gemini free tier.

## What it does

**Voice.** Wake word with openwakeword. Speech is transcribed by NVIDIA
Parakeet v3 on the CPU in about a quarter of a second. Replies are spoken with
edge-tts neural voices; each sentence gets a native voice for its language,
and sentences stream into one audio player so there is no gap after every full
stop. Say "hey Jarvis" while it talks and it stops and listens.

**Chat.** Questions, reminders, WhatsApp, Home Assistant, web search and the
rest go to [Hermes Agent](https://hermes-agent.nousresearch.com), which runs
locally as a gateway. Its default model is Gemini Flash; harder turns are
routed to Claude Haiku, Sonnet or Opus through the Pro subscription.

**Code view.** When a request means writing or changing code or files, a
Claude Code session (Claude Agent SDK) opens in its own full-screen view, laid
out like OpenCode: the session with every tool call, a review pane with the
folder's real git diff, a file viewer and a terminal with each command's
output. A small Claude Haiku router decides between chat, code and PC, so you
don't have to say "code mode".

**PC view.** Requests to operate the computer go to a second Claude session
that takes the most direct route: a shell command when one does the job
(opening Gmail is one `Start-Process`), your own Firefox through the Blueprint
extension for websites, and [Cua Driver](https://github.com/trycua/cua) for
desktop apps. Cua Driver works through UI Automation in the background, so it
doesn't move your mouse or steal focus. Sending, buying, deleting or touching
account security asks you first (by voice or with a button), unless you switch
confirmations to "auto". The view shows each step and a live picture of the
screen with the last click marked.

**Memory.** After each reply, Claude Haiku pulls out the facts worth keeping
("the exam is on Monday"). They are embedded locally with a multilingual model
(fastembed) and stored in Qdrant. Before every request the relevant ones are
looked up and handed to the model, so a question in Russian finds a fact said
in Italian weeks earlier. The PC session also keeps short notes on how things
work on this machine.

**Interface.** A React page at `http://127.0.0.1:8765`: a 3D particle sphere
that reacts to listening, thinking and speaking, the clock, the last answer,
system stats, reminders, light and dark themes.

## How it fits together

```
 microphone ──"hey jarvis"──▶ JARVIS server :8765 ──WebSocket──▶ browser UI
                              │  wake word, Parakeet STT, edge-tts
                              │  router (Claude Haiku): chat / code / pc
                              │  memory (Haiku extraction, fastembed, Qdrant)
          ┌───────────────────┼──────────────────────────┐
          ▼                   ▼                          ▼
   Hermes gateway :8642   code session              PC session
   Gemini / Claude        Claude Agent SDK          Claude Agent SDK
   WhatsApp, Home         in a project folder       shell + Firefox (Blueprint)
   Assistant, web…                                  + Cua Driver
```

## Requirements

- Windows 11 (the voice server also starts on Linux, but the PC view is
  Windows-only)
- Python 3.10+ (developed on 3.12), Node.js 20+, ffmpeg (`winget install Gyan.FFmpeg`)
- A Claude Pro or Max subscription, for the code and PC views, the router and
  memory
- A Gemini API key (free tier) for Hermes' default model
- For the PC view: Firefox with the
  [Blueprint MCP extension](https://addons.mozilla.org/firefox/addon/blueprint-mcp-for-firefox/)

## Install

```powershell
git clone https://github.com/EliseyRotar/jarvis-ai
cd jarvis-ai

# venv, Python packages, Hermes Agent, ffmpeg check, setup page
.\start.ps1 -Bootstrap

# speech recognition model (~465 MB)
.\install_stt_model.ps1

# PC view: Cua Driver and the Blueprint server
.\install_pc_tools.ps1

# Claude Pro token for the code view, PC view, router and memory
npm install -g @anthropic-ai/claude-code
claude setup-token
```

Put the token in `~/.jarvis/.env` (start from `.env.example`). The first start
downloads the wake-word and embedding models.

## Run

```powershell
.\start.ps1      # Hermes gateway + JARVIS, then open http://127.0.0.1:8765
.\stop.ps1
```

To have it always on, `.\install_autostart.ps1` adds a Startup entry that runs
`keepalive.ps1` at logon. The keepalive starts the voice server and restarts
it if it dies. It runs in your session on purpose: a Windows service can't
reach the microphone or the speakers. Create `.jarvis.paused` next to the
script to pause it.

## Configuration

- `~/.jarvis/.env`: JARVIS settings; every option is listed in `.env.example`.
- `%LOCALAPPDATA%\hermes\config.yaml`, `.env`, `SOUL.md`: Hermes models, tools,
  MCP servers and personality.
- `~/.jarvis/pc.json`: PC view model and confirmation mode (set from the UI).
- `~/.jarvis/pc_notes.md`: what the PC session learned about this machine.

## Development

```powershell
.venv\Scripts\python.exe -m pytest        # tests
cd jarvis\web; npm run build              # rebuild the UI into jarvis\static\dist
```

The built UI is committed, so a fresh clone works without Node unless you
change the frontend.

```
jarvis/
  main.py            FastAPI server, WebSocket, wake-word loop, turn handling
  hermes_client.py   Hermes sessions API: streaming, model routing
  code_session.py    Claude Code session for the code view, chat/code/pc router
  pc_session.py      Claude session that operates the PC
  memory_store.py    long-term memory
  stt.py, tts.py     speech in and out
  lang.py            Italian / English / Russian detection
  web/               React + Vite frontend
tests/               pytest suite
```

## Security

JARVIS runs commands and edits files without asking, and the PC view can
operate any app you can. It listens only on `127.0.0.1` and has no
authentication, so never expose ports 8765 or 8642. See
[SECURITY.md](SECURITY.md).

## License

MIT, see [LICENSE](LICENSE). `whatsapp-mcp/` is vendored from
[lharries/whatsapp-mcp](https://github.com/lharries/whatsapp-mcp) (MIT, Luke Harries).
