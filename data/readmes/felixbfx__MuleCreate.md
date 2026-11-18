<p align="center">
  <img src="sketch_machine/assets/mule_icon.png" alt="Mule Create logo" width="150">
</p>

<h1 align="center">Mule Create</h1>

<p align="center"><b>Sketch in 3D space with lines – and hand the sketch to an AI that builds it.</b></p>

<h3 align="center"><a href="https://github.com/felixbfx/MuleCreate/releases/latest/download/Mule_Windows.zip">⬇ Download Mule for Windows</a></h3>

<p align="center">The newest version in one click: unzip, start <code>Mule\Mule.exe</code> – no installation, no Python.<br>
<a href="https://github.com/felixbfx/MuleCreate/releases">All versions, source code, Linux</a></p>

![Mule Create with the Alpaca Monowheel: modes, tools, viewport, outliner and status line](docs/handbook/readme_overview.png)

**[All releases](https://github.com/felixbfx/MuleCreate/releases)** · **[Introduction in pictures](docs/INTRODUCTION.md)** (19 pictures, two
minutes) · **[Example scene](https://github.com/felixbfx/MuleCreate/releases/download/v0.99.255/Example_Alpaca_Monowheel.zip)** · Questions about Mule: give [`AI_HANDBOOK.md`](AI_HANDBOOK.md) to your AI and ask it.

Mule Create (short: Mule) is a standalone program for technical sketching in 3D. You draw lines on planes that you
place in space, like tracing paper. Lines can become surfaces, lofts and curve nets. You attach notes, reference
pictures, videos and spoken feedback to the parts of the drawing. Then you export a **Sketch Brief**: a folder with
pictures, notes, a USD file of the scene and working rules, from which an AI (for example Claude Code or Codex)
rebuilds the object in Houdini or Blender. While Mule is open, the AI can also look at the scene directly through a
local MCP server.

**Status: Alpha.** Expect bugs. The Windows package is tested; Linux runs from source and is hardly tested;
macOS is not tested. Scene files may change between alpha versions.

## What you can do

- **Draw** with pen and brush on ground planes, your own planes, curved drawing surfaces or imported meshes – or
  freely in space. Holding still at the end of a stroke makes a straight line or a clean shape.
- **Edit** points, edges and surfaces; build fill surfaces, curve surfaces, lofts and extrusions that follow their
  lines; group with nulls, mirror with symmetry, repeat with arrays.
- **Notes**: headings in space with leader lines to the parts they mean; each note has a board (like PureRef) for
  text, pictures, videos, sketches and arrows. Screenshots can become hero cameras for the AI.
- **Review**: walk through the scene and talk your feedback; Mule records voice, camera and pointer, and the AI
  turns it into draft notes at the right parts.
- **Shots** (prototype): show what happens when, with flipbook planes and camera positions, without animating.
- **Export**: Sketch Brief, scene as USD, curves.

## Example scene

![Example scene Alpaca Monowheel: the sketch and the two finished models](docs/example_alpaca_monowheel.png)

**[Example_Alpaca_Monowheel.zip](https://github.com/felixbfx/MuleCreate/releases/download/v0.99.255/Example_Alpaca_Monowheel.zip)** (130 MB) – a one-wheeled expedition vehicle, sketched in Mule and then
built by an AI from the Sketch Brief. One scene holds the sketch (lines, surfaces, groups with symmetry) and the
finished model as USD, with and without cargo. Unzip, keep the folder together and open `Alpaca_Monowheel.mule`.
Free to use, also commercially, under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) – credit:
"Alpaca Monowheel by Felix Barthel (Mule Create), CC BY 4.0".

## Install and start

**Windows (recommended):** **[download `Mule_Windows.zip`](https://github.com/felixbfx/MuleCreate/releases/latest/download/Mule_Windows.zip)** (always the newest version; older ones are under
[releases](https://github.com/felixbfx/MuleCreate/releases)), unzip it into a folder of its own and start `Mule\Mule.exe`. No Python needed. The program is not signed yet: on the first start Windows SmartScreen warns –
click "More info", then "Run anyway".

**From source (Windows):**

```
py -3.14 -m venv .venv
.venv\Scripts\pip install -r requirements.txt
.venv\Scripts\python -m sketch_machine
```

or double-click `start.bat`: on the first start it sets up `.venv` itself (needs Python 3.14 from python.org
and internet once; keep the folder on a short path such as `C:\Mule`, Windows limits path length).

**From source (Linux):** `./start.sh`. On the first start it sets up its own Python 3.14 inside the project folder
with [uv](https://docs.astral.sh/uv/) (internet needed once; the system Python is not touched). If Qt reports
"Could not load the Qt platform plugin xcb", install `libxcb-cursor0`; under Wayland try `QT_QPA_PLATFORM=xcb ./start.sh`.

Mule needs a graphics card with **OpenGL 3.3**. The interface is available in English and German:
View → Sprache / Language, then restart.

Mule has no installer and writes nothing into its program folder. Your data go to `%APPDATA%\Mule` (recipes,
reviews, optional speech recognition), the settings to the registry, backups next to your scenes. Help → **Where
Mule keeps its files …** lists all of it; the [guide](GUIDE.md#where-mule-keeps-its-files) says how to remove Mule
completely.

## Working with an AI

1. Sketch, and write notes where something matters.
2. **File → Export Sketch Brief** (`Ctrl+E`): write the task in one sentence and choose a folder.
3. Start Claude Code or Codex **in that brief folder**. The folder contains the rules and the MCP entry; the AI
   asks about whatever your notes leave open, then builds.

The MCP server runs while Mule is open, at `http://127.0.0.1:8770/mcp` (this computer only). To use it from another
project, register it once:

```
claude mcp add --transport http sketch_machine http://127.0.0.1:8770/mcp
```

For Codex, add to `~/.codex/config.toml`:

```toml
[mcp_servers.sketch_machine]
url = "http://127.0.0.1:8770/mcp"
```

Review transcripts use [faster-whisper](https://github.com/SYSTRAN/faster-whisper) locally; Mule sets it up for you
(Review → Set Up Transcription …, needs a Python 3.10–3.13 from python.org once, about 2–4 GB of downloads).

## Documentation

- **`docs/INTRODUCTION.md`** – start here: 19 pictures of the main functions to click through
  (or open `docs/introduction.html` as a slide show).
- **`AI_HANDBOOK.md`** – the complete reference, written for AI assistants. If you have a question about Mule, give
  this file to your AI (Claude, ChatGPT, Codex, …) and ask it. It covers every function, shortcut, workflow, the
  brief format and the MCP tools.
- **F1** in the program – the manual (English and German).
- `GUIDE.md` – short guide: install, main workflows, reporting problems.
- `CHANGELOG.md` – changes per release.
- `docs/recipes.md` – brief recipes: swap the AI's way of working, write your own;
  `docs/mule_default_recipe.md` – how Mule's own recipe works, and why.
- `bible/sketch_machine_bible.md` – lessons from AI build sessions, kept by the AIs that worked with Mule.

## For developers

Tests: `python tests/run.py --core` (fast, no window), `python tests/run.py` (core plus the real program in
off-screen windows with real mouse events). Details in `tests/README.md`. The code layout is described in
`AI_HANDBOOK.md`, chapter "Source code". Some test names and the German UI strings (which are also the keys of the
English translation in `sketch_machine/i18n_en.py`) stay German.

Internally the package, settings, scene format and MCP server are still called "Sketch Machine" / `sketch_machine`.

## Contributing

During the alpha, please report bugs and ideas as **GitHub issues**; pull requests are not accepted yet
(see `CONTRIBUTING.md`). Useful in a bug report: what you did, what you expected, what happened, the version, the
file `mule.log` from `%APPDATA%\Mule`, and if possible the scene and a screenshot.

Contact for anything that does not fit an issue: **mulecreate@gmail.com**.

## License

Copyright (C) 2026 Felix Barthel

Mule Create is free software under the **GNU General Public License v3.0** (see `LICENSE`). Third-party software in
the package is listed with its licenses in `THIRD_PARTY_NOTICES.md` and the folder `licenses/` next to `Mule.exe`.
The name **Mule Create** and the Mule logo are not covered by the license and are reserved.
