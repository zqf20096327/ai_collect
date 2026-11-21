<p align="center"><img src="assets/banner.png" alt="Godot Skills" width="640"></p>

<p align="center">
  <a href="https://github.com/EL4CTEO/godot-skills/releases"><img alt="Release" src="https://img.shields.io/github/v/release/EL4CTEO/godot-skills"></a>
  <a href="https://github.com/EL4CTEO/godot-skills/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/EL4CTEO/godot-skills/actions/workflows/ci.yml/badge.svg"></a>
  <img alt="Godot 4.7.2" src="https://img.shields.io/badge/Godot-4.7.2-478cbf?logo=godotengine&logoColor=white">
  <img alt="GDScript and C#" src="https://img.shields.io/badge/GDScript%20%7C%20C%23-supported-478cbf">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-green"></a>
</p>

# Godot Agent Skills

Godot **4.7** skills for AI coding agents (Claude Code, Codex, OpenCode, Gemini CLI, GitHub Copilot, Cursor), based on **Godot 4.7.2**. They cover GDScript and C#/.NET equally.

There are 27 compact skills. Agents look up exact APIs from **your installed engine** instead of guessing, edit scenes safely through Godot itself, and check their work with real compile, test and export runs. Every code example in the skills is compiled on Godot 4.7.2 by the test suite.

## Recommended: Godot .NET (C#)

I suggest using the **.NET build of Godot with C#**. AI models have seen far more C# than GDScript, and the C# compiler catches mistakes (wrong types, missing members) before the game runs, so agents fix their own errors faster.

GDScript is fully supported too. Pick it if you need **web export**, which C# projects don't support in Godot 4.x.

## Install

**Claude Code** (plugin):
```
/plugin marketplace add EL4CTEO/godot-skills
/plugin install godot-agent-skills@godot-agent-skills
```

**Any agent** (clone, then run the installer):
```bash
git clone https://github.com/EL4CTEO/godot-skills
./godot-skills/install/install.sh          # macOS / Linux
.\godot-skills\install\install.ps1         # Windows
```
The default installs into `~/.claude/skills` and `~/.agents/skills`. `.agents/skills` is read by Codex, OpenCode, Gemini CLI, Copilot and Cursor. Options: `--agent claude|codex|opencode|gemini|copilot|cursor|all`, `--project DIR` for a single project, `--uninstall`.

**Requirements:** Godot 4.7+ (standard or .NET) and Python 3.9+. For C#, the .NET 8+ SDK. If Godot isn't found automatically, set `GODOT_EXE`.

## Skills

| Skill | What it does |
|---|---|
| `godot-core` | Start here: API lookup, headless runs, scene editing, what's new |
| `godot-gdscript` | Typed GDScript, signals, await, compile check |
| `godot-csharp` | .NET setup, signals, interop, build errors |
| `godot-architecture` | Project structure, autoloads, Resources, saves |
| `godot-2d` | TileMapLayer, Parallax2D, cameras, pixel art |
| `godot-3d-rendering` | Renderers, lighting, GI, materials, import |
| `godot-physics` | Jolt, character controllers, raycasts, ragdolls |
| `godot-ui` | Menus, themes, gamepad focus, localization |
| `godot-input` | Rebinding, gamepads, gyro, touch |
| `godot-animation` | AnimationTree, Tweens, root motion, IK |
| `godot-shaders-vfx` | Shaders, particles, post effects, shader check |
| `godot-audio` | Buses, 3D sound, adaptive music |
| `godot-networking` | Multiplayer, RPCs, replication, HTTP |
| `godot-performance` | Profiling, MultiMesh, threads |
| `godot-export-ci` | Exports, signing, GitHub Actions |
| `godot-editor-tooling` | Tool scripts, editor plugins, importers |
| `godot-testing-debug` | GdUnit4, gdUnit4Net, debugging |
| `godot-xr` | OpenXR VR/AR |
| `godot-navigation-ai` | Pathfinding, avoidance, enemy AI, behavior trees |
| `godot-3d-gameplay` | Third-person cameras, GridMap and CSG levels |
| `godot-procedural` | Noise, dungeons, caves, terrain meshes, chunks |
| `godot-migration` | Godot 3 or older 4.x to 4.7, Unity porting, API scanner |
| `godot-mobile-web` | Safe areas, app lifecycle, purchases, Web hosting |
| `godot-narrative` | Dialogue, choices, quests, cutscenes |
| `godot-modding-dlc` | Mod loading, PCK packs, DLC, patches |
| `godot-game-feel` | Screen shake, hit-stop, juice, trailer capture |
| `godot-addons` | Vetting and installing plugins, curated 4.7 list |

## Try it

> "Add a player with coyote-time jumping and a camera that shakes on landing."
> "My C# build fails after upgrading to 4.7, fix it."
> "Make a main menu that works with a gamepad, then export for Windows and Android."
> "Upgrade my Godot 3 project to 4.7 and list what the converter missed."
> "Add enemies that patrol, spot the player and chase them around obstacles."

## Development

```bash
python tools/validate_skills.py --strict   # spec, token budgets, links
python tools/trigger_check.py              # skill routing
python tools/run_tests.py                  # real-engine tests (set GODOT_EXE if needed)
```

## Credits

Godot logo by Andrea Calabró, licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
