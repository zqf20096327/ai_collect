<p align="center">
  <img src="assets/clarvis_logo.png" alt="Clarvis AI" width="300">
  <br>
  <strong>OpenClaw X Jarvis = "Clarvis"</strong>
</p>

---

3D Printing Made Easy

Open-source 3D printing assistant powered by AI. Talk to it from Telegram, Discord, or WhatsApp — send a sketch, photo, or describe what you want, and it will create or find a 3D model, slice it, and send it to your printer.

> For a ready-to-use, anything-to-3D-print workflow without the setup, check out [clarv.is](https://clarv.is).

## Demo

<table>
<tr>
<td align="center"><strong>3D Search — find → preview → slice → print</strong></td>
<td align="center"><strong>AI Replication — photo → 3D model → slice → print</strong></td>
</tr>
<tr>
<td>

https://github.com/user-attachments/assets/f709543a-a8f4-4a94-9229-a7b1fdf6ccd2

</td>
<td>

https://github.com/user-attachments/assets/3bb74dca-9b3d-4649-9a4a-780d0cde3f1b

</td>
</tr>
</table>

<table>
<tr>
<td align="center"><strong>Sketch / Image → 3D</strong></td>
<td align="center"><strong>Modify 3D Models</strong></td>
<td align="center"><strong>Multiply, Slice & Print</strong></td>
</tr>
<tr>
<td><img src="assets/demos/sketch_to_3d.gif" alt="Sketch to 3D" width="280"></td>
<td><img src="assets/demos/modify_3d.gif" alt="Modify 3D" width="280"></td>
<td><img src="assets/demos/multiply_slice_print.gif" alt="Multiply, Slice & Print" width="280"></td>
</tr>
</table>

## What it does

- **Video/image/text → 3D model** — AI-powered 3D generation and 3D editing pipeline
- **Search existing models** — Finds matching 3D models on 3D Libraries
- **Slice to G-code** — CuraEngine with configurable profiles
- **Print** — Sends G-code to your printer via Moonraker (Klipper) or PrusaLink (Prusa)
- **All from chat** — Works through any available OpenClaw channel (Telegram, Discord, WhatsApp, etc)

## Quick start

### Prerequisites

- [Docker Desktop](https://docs.docker.com/get-docker/) (or Docker Engine + Compose V2)
- A Google API key ([free](https://aistudio.google.com/apikey)) for the AI agent brain
- A Telegram bot token (from [@BotFather](https://t.me/BotFather)) or Discord bot token

### Install

```bash
git clone --recursive https://github.com/makermate/clarvis-ai.git
cd clarvis-ai
./setup.sh
```

The setup script will:
1. Build Docker images (OpenClaw + claw3d CLI, CuraEngine slicer)
2. Run OpenClaw's setup wizard (gateway, messaging channels, auth)
3. Run claw3d setup (capabilities, providers, API keys, skill modules)
4. Start all services

That's it. Open Telegram and message your bot.

### Manual setup

If you prefer to configure things yourself:

```bash
cp env.example .env
# Edit .env with your API keys

docker compose up -d
```

## Architecture

```
You (Telegram/Discord/WhatsApp)
        │
        ▼
   ┌─────────┐
   │ Gateway  │  OpenClaw + claw3d CLI + AI skill instructions
   └────┬─────┘
        │
        ▼
   ┌─────────┐
   │ Slicer   │  CuraEngine REST API (3D model → G-code)
   └────┬─────┘
        │
        ▼
   3D Printer (on your WiFi network)
```

**Services:**
- `gateway` — OpenClaw agent with claw3d CLI and skill instructions
- `slicer` — CuraEngine 5.6.0 HTTP API for slicing models to G-code

## Configuration

### Default API keys

| Key | Required | Purpose | Get it at |
|-----|----------|---------|-----------|
| `GOOGLE_API_KEY` | Yes | Agent brain (Gemini 2.5 Flash) | [aistudio.google.com/apikey](https://aistudio.google.com/apikey) |
| `FAL_API_KEY` | For AI creation | Image/text → 3D model | [fal.ai/dashboard/keys](https://fal.ai/dashboard/keys) |
| `THINGIVERSE_ACCESS_TOKEN` | For search | Find existing models | [thingiverse.com/apps/create](https://www.thingiverse.com/apps/create) |

### Printer setup

Once Clarvis is running, tell it about your printer from chat:

> "I have a Creality K2 SE at 192.168.1.100 on port 4408"

Or configure via CLI:

```bash
docker compose exec gateway claw3d printer add \
  --name "My Printer" \
  --backend moonraker \
  --host 192.168.1.100 \
  --port 7125
```

**Creating a printer profile for slicing**

<table>
<tr>
<td width="50%">

1. In Cura → **File → Export Universal Cura Project** (`.3mf`)
2. Send the `.3mf` file to the agent in chat
3. Provide your printer's IP address and port

The agent extracts everything from the `.3mf` automatically — build volume, nozzle size, material settings, and all print profiles.

</td>
<td width="50%">
<img src="assets/demos/create_printer_profile.gif" alt="Create printer profile" width="360">
</td>
</tr>
</table>

### Commands

All interaction happens through chat. Just describe what you want:

- *"Make me a phone stand"* — searches Thingiverse or creates via AI
- *Send a photo of a sketch* — converts it to a 3D model
- *"Print it at 60% strength"* — slices and sends to printer
- *"Rotate it 90 degrees"* — adjusts the model orientation
- *"Show me options for a vase"* — searches and shows alternatives

## Built on

<p align="center">
  <a href="https://github.com/openclaw/openclaw">
    <img src="assets/openclaw-logo.png" alt="OpenClaw" height="60">
  </a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/makermate/claw3d">
    <img src="assets/claw3d-logo.png" alt="claw3d" height="60">
  </a>
</p>

<p align="center">
  <a href="https://github.com/openclaw/openclaw">OpenClaw</a> — AI agent platform with Telegram, Discord & WhatsApp
  &nbsp;&nbsp;·&nbsp;&nbsp;
  <a href="https://github.com/makermate/claw3d">claw3d</a> — 3D printing CLI & skills
</p>

## How it's built

Clarvis AI is a distribution that combines three open-source projects into a single, ready-to-run stack:

| Component | Repo | What it does |
|-----------|------|--------------|
| **OpenClaw** | [openclaw/openclaw](https://github.com/openclaw/openclaw) | AI agent platform — gateway, messaging channels (Telegram, Discord, WhatsApp), authentication, and skill execution engine |
| **claw3d** | [makermate/claw3d](https://github.com/makermate/claw3d) | Python CLI that powers the whole workflow — AI model generation (FAL.ai), Thingiverse search, slicing, preview rendering, and printer control (Moonraker/PrusaLink) |
| **claw3d-skill** | [makermate/claw3d-skill](https://github.com/makermate/claw3d-skill) | Modular AI agent instructions that teach the OpenClaw agent how to understand user intent, route requests, and orchestrate the 3D printing workflow |
| **curaengine-slicer-api** | [makermate/curaengine-slicer-api](https://github.com/makermate/curaengine-slicer-api) | FastAPI service wrapping CuraEngine 5.6.0 — handles slicing, mesh conversion (GLB/STL/USDZ), and printer profile management |

This repo (`clarvis-ai`) adds the Docker Compose orchestration, the interactive setup script, and the Dockerfile that layers everything on top of [OpenClaw](https://github.com/openclaw/openclaw). Each component can also be used independently.

## Useful commands

```bash
# View logs
docker compose logs -f gateway

# Stop everything
docker compose down

# Rebuild after pulling updates
git pull --recurse-submodules
docker compose build
docker compose up -d

# Run claw3d CLI directly
docker compose exec gateway claw3d doctor

# Access the interactive CLI
docker compose --profile cli run cli
```

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. Each component has its own repo — open PRs there for component-specific work, or here for setup/integration issues.

## License

MIT
