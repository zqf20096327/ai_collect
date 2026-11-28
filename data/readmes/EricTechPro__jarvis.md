<div align="center">

<img src="docs/art/jarvis-orb.gif" width="180" alt="JARVIS, a glowing orb of light that ripples as it speaks">

<h1>Jarvis</h1>

<p><strong>Talk to your computer like Jarvis.</strong></p>

<p>It sees your screen, points, draws, clicks and calls tools, all grounded in your second brain.</p>

<p>
<img alt="Platforms" src="https://img.shields.io/badge/macOS%20%C2%B7%20Windows%20%C2%B7%20Linux-desktop-1f883d?style=flat-square">
<img alt="Models" src="https://img.shields.io/badge/Gemini%20%C2%B7%20Claude%20%C2%B7%20ChatGPT%20%C2%B7%20local-models-d97757?style=flat-square">
<img alt="License" src="https://img.shields.io/badge/license-AGPL--3.0-0969da?style=flat-square">
</p>

<p>⭐ Star it · <a href="https://www.skool.com/erictech">Join the community →</a></p>

<p>🎤 DevFest Vancouver 2026 talk: <a href="slides/Gemini%20Live%20Agents.pdf"><strong>Gemini Live Agents slides (PDF)</strong></a> · <a href="slides/">deck folder</a></p>

<p><a href="#install">Install</a> · <a href="#how-it-works">How it works</a> · <a href="#second-brain">Second brain</a> · <a href="#models">Models</a> · <a href="#safety">Safety</a></p>

</div>

## Install

macOS and Linux:

```bash
curl -fsSL https://raw.githubusercontent.com/EricTechPro/jarvis/main/get.sh | bash
```

Windows (PowerShell):

```powershell
curl.exe -fsSL https://raw.githubusercontent.com/EricTechPro/jarvis/main/get.ps1 | powershell -NoProfile -ExecutionPolicy Bypass -Command -
```

Build from source instead:

```bash
git clone https://github.com/EricTechPro/jarvis.git
cd jarvis/showcase/tauri
(cd sidecar && npm ci && npm test)
./build.sh
```

- Needs Rust, Node.js 22+, [Tauri prerequisites](https://v2.tauri.app/start/prerequisites/)

## How it works

```md
# how-it-works.md

1. Hold ⌃ + ⌥ and talk
2. Jarvis reads your notes
3. It answers out loud
4. It points, draws or clicks
```

<p align="center"><img src="docs/art/jarvis-shows-you-how.gif" width="49%" alt="Jarvis rings the button to click"> <img src="docs/art/jarvis-explains.gif" width="49%" alt="Jarvis sketches an answer on screen"></p>

## Second brain

Your notes folder is the memory.

```
your-notes/
├── AGENTS.md
├── _context/
│   └── index.md
├── _raw/
├── _research/
├── projects/
│   └── index.md
└── .agents/
```

```md
# AGENTS.md

- Read _context first
- Cite _raw, never edit it
- Put outputs in _research
```

- Every chat starts with your `AGENTS.md`

## Shortcuts

```md
# shortcuts.md

talk       ⌃ + ⌥        Ctrl + Alt
highlight  ⌃ + ⌘        (Mac: hold and circle)
type       ⌥ + ⌘        Ctrl + Shift
show       ⌃ + ⌥ + S    Ctrl + Shift + S
```

## Models

```md
# models.md

- Gemini    free key, AI Studio
- Claude    subscription
- ChatGPT   subscription
- Local     Ollama, LM Studio
```

- Free Gemini key: [AI Studio](https://aistudio.google.com/apikey)
- Local models need vision, tool calls, **32k+ context**

## Safety

Risky things start off. Defaults:

```jsonc
// Change them in the panel. Fixed rules can't be turned off.
{
  "allowActions": false, // file edits, commands, app control
  "skipAllow":    false, // risky steps ask you first
  "rawReadOnly":  true,  // fixed: _raw is never written
  "telemetry":    false  // fixed: nothing goes to the developer
}
```

- Data goes only to the model you pick ([PRIVACY.md](PRIVACY.md))

## Settings

- Starters to copy into `~/Jarvis/Data/settings.json` (keys stay in the keychain): [Classic](docs/settings.classic.example.json), [Live](docs/settings.live.example.json)

---

## Credits

- Based on [Roamies](https://github.com/KenKaiii/Roamies) by Ken Kai
- Agent: Ken Kai's [gg-framework](https://github.com/KenKaiii/gg-framework)
- Modified by Eric Tech, 2026-11-22: renamed, second brain, updater off
- License: [AGPL-3.0](LICENSE). Share source if you ship changes
- Other licenses: [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)

<sub>Art by Ken Kai. Not affiliated with Marvel, Disney or Valve. [Takedown request](https://github.com/EricTechPro/jarvis/issues)</sub>

<p align="center"><sub>Made by Eric Tech</sub></p>
