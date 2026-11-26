<div align="center">
  <img src="assets/logo.svg" width="128" alt="cui-skills">
</div>

# cui-skills

<p align="center"><b><a href="#setup">Install</a></b> · <a href="commands/cui-setup.md">/cui-setup</a> · <a href="#the-four-skills">Skills</a>: <a href="#cui-app--native-desktop-cc">cui-app</a> · <a href="#cui-web--webassembly-in-the-browser">cui-web</a> · <a href="#cui-py--desktop-apps-in-python-nexa">cui-py</a> · <a href="#cui-style--the-cui-look-in-plain-css">cui-style</a> · <a href="https://yappologistic.github.io/CUI/">CUI docs</a> · <a href="LICENSE">MIT</a></p>

<p align="center"><a href="https://skills.sh/ChiakoRh/cui-skills"><img src="https://skills.sh/b/ChiakoRh/cui-skills?style=flat-square" alt="skills.sh"></a> <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-f4c430?style=flat-square" alt="MIT license"></a></p>

Four agent skills for building UIs with [CUI](https://github.com/yappologistic/CUI) — one visual language across **C**, **WebAssembly**, **Python** and **plain CSS**, written from real build and test sessions (Windows and Linux), not from reading docs alone.

- **~210 native components** in C99, zero dependencies, ~250 KB apps — see `cui-app`
- **The same C app in the browser** with plain clang + `wasm32`, no Emscripten — see `cui-web`
- **Desktop apps in Python** via [nexa](https://github.com/x017/nexa), the CUI port — see `cui-py`
- **The CUI look in HTML/CSS** for sites and web UIs without any C — see `cui-style`

## Contents

- [The four skills](#the-four-skills)
  - [cui-app — native desktop (C/C++)](#cui-app--native-desktop-cc)
  - [cui-web — WebAssembly in the browser](#cui-web--webassembly-in-the-browser)
  - [cui-py — desktop apps in Python (nexa)](#cui-py--desktop-apps-in-python-nexa)
  - [cui-style — the CUI look in plain CSS](#cui-style--the-cui-look-in-plain-css)
- [How the layers fit together](#how-the-layers-fit-together)
- [Requirements per skill](#requirements-per-skill)
- [Setup](#setup)
- [Recorded clone paths (`paths.json`)](#recorded-clone-paths-pathsjson)
- [Installing the skills into an agent](#installing-the-skills-into-an-agent)
- [RTL / Persian support](#rtl--persian-support)
- [Repository layout](#repository-layout)

---

## The four skills

### cui-app — native desktop (C/C++)

The main skill. CUI is an immediate-mode UI library for native apps, written in C99, built with CMake, zero external dependencies.

**Contains:**

- The mental model (immediate mode, tokens, springs, hit rects)
- Full **component map** of all ~210 components by category (`api.md`)
- **Copyable UI patterns**: app skeleton, sidebar, list+detail, forms, tables, threads, RTL (`patterns.md`)
- **Working CMake template**: `template/CMakeLists.txt` + `template/main.c`
- The Windows/MSVC build recipe and the pitfalls actually hit (`C2099` on compound literals, multi-config generators)
- Icons (Lucide), theming, fonts, screenshots, headless testing

**When to use:** "build me a desktop tool/app in C", "add a component to my CUI app", questions about CUI itself.

### cui-web — WebAssembly in the browser

The web layer only: the same C codebase compiled to WebAssembly with plain clang and drawn with WebGL2.

**Contains:**

- The contract your app must satisfy (`int main(void)` + `cui_app_run`, no manual loop)
- Build & run: `web/tools/build.sh app my_app.c` + `serve.sh` → `http://localhost:8765/#/app/my_app`
- **Browser constraints** verified in the source, not guessed: `fopen` always returns `NULL`, `cui_app_file_dialog` / `cui_app_open_url` are no-ops
- Hosting: `web/site/` is plain static files — any static host works
- Toolchain notes (clang `wasm32` + `wasm-ld` + `llvm-ar` + python3; Windows gotchas)

**When to use:** "run my C/C++ app in the browser", "build it as WASM".

### cui-py — desktop apps in Python (nexa)

[nexa](https://github.com/x017/nexa) (`pip install nexa-ui`) is the Python port of CUI: same components, same tokens, zero Python dependencies.

**Contains:**

- Install and the value-returning immediate-mode mental model
- The two scope kinds (unconditional vs. conditional — the #1 beginner bug) and ID rules
- **Theming from Python**: `Accent`, `Tone`, `Token`, `ThemeMode`
- OOP layer with a working example: `Application`, `Component`, `Router`/`View`, `Store[T]`
- **RTL/Persian shaping** (on by default), headless screenshot testing
- Docs map: which file in `docs/` answers which question
- Windows build troubleshooting

**When to use:** "make me a Python GUI", "port this CUI app to Python", anything with `nexa`.

### cui-style — the CUI look in plain CSS

The theme layer as CSS: the same tokens `cui-app` uses, implemented with CSS variables — for sites and UIs with no C or WASM.

**Contains:**

- Dark + light token sets, Geist typography, pill controls, 1px-bordered surfaces, word-blur motion
- Lucide mechanics (re-running `createIcons()`, pinned CDN, self-hosting)
- **Persian/RTL section**: tested font URLs, `@font-face`, logical properties, always-RTL rules, Latin digits
- React/Tailwind recipes, a restyle workflow for existing projects
- Scaffolder script (`cui.py`), starter `tokens.css` / `components.css`, `example.html`

**When to use:** "style this site like CUI", "make a landing page in this look" — no build step involved.

---

## How the layers fit together

| You want | Skill |
|---|---|
| A desktop window (Windows/macOS/Linux) in C/C++ | `cui-app` |
| The same C app running in the browser (WASM) | `cui-web` |
| A desktop app in Python | `cui-py` |
| A plain HTML/CSS site or UI in the CUI look | `cui-style` |

One codebase can ship both ways: a `cui_app_run` app builds natively with CMake **and** as WASM with `build.sh app`. All four skills share one token system — `cui-app` is the reference for components and theming; the others cover their own layer and point back to it.

## Requirements per skill

| Skill | Needs installed | Needs cloned |
|---|---|---|
| `cui-app` | git, CMake 3.14+, a C compiler (Visual Studio Build Tools / gcc / clang) | CUI |
| `cui-web` | git, clang with `wasm32` target (LLVM), Git Bash, python3 | CUI |
| `cui-py` | Python 3.9+ (`pip install nexa-ui`); a C compiler only when building from source | nexa (development only) |
| `cui-style` | nothing — a browser | no |

## Setup

Two ways:

1. **Slash command** — copy [`commands/cui-setup.md`](commands/cui-setup.md) into your agent's command directory (OpenCode: `~/.config/opencode/command/`), then run `/cui-setup`.
2. **Ask your agent directly** — say "set up the CUI skills"; the flow below is written for agents to follow.

Or, without an agent, the bundled setup script (checks tools, clones the projects, writes `paths.json`, then installs the skills through `npx skills add` so installs are counted on skills.sh):

```sh
npx github:ChiakoRh/cui-skills        # or: git clone … && node setup.mjs
```

### The flow (for AI agents)

1. **Ask which skill branch the user wants** (multiple is fine): `cui-app` (native C), `cui-web` (WASM), `cui-py` (Python), `cui-style` (CSS only).
2. **Check what already exists** before installing anything:
   `git --version`, `cmake --version`, `clang --version` (for `cui-web`, also `clang --print-targets` and look for `wasm32`), `python --version`.
3. **Install only the missing tools for the chosen branches:**
   - Debian/Ubuntu: `sudo apt install git cmake clang lld llvm python3`
   - Windows: git, CMake, LLVM, Python from official installers; Visual Studio Build Tools for `cui-app`
   - `cui-style` alone needs nothing
4. **Clone the projects** into a location the user approves (suggest `~/Git/CUI` and `~/Git/nexa`):
   ```sh
   git clone https://github.com/yappologistic/CUI.git   # cui-app, cui-web
   git clone https://github.com/x017/nexa.git           # cui-py development only
   ```
   For `cui-py` alone, `pip install nexa-ui` is enough — no clone needed.
5. **Record the paths** in `paths.json` at the repo root (see below).
6. **Install the skills** into the agent's skills directory if not already there.
7. **Verify** one cheap check per branch — configure the template (`cui-app`), `clang --print-targets | grep wasm32` (`cui-web`), `python -c "import nexa"` (`cui-py`); `cui-style` needs nothing.

Finish with a table: branch → tools found/installed → clone path → verified or not.

## Recorded clone paths (`paths.json`)

Each skill points at a local clone of the upstream project as its source of truth. Instead of hardcoding paths (which differ on every machine), setup writes them here:

```json
{
  "cui_clone": "/home/you/Git/CUI",
  "nexa_clone": null
}
```

`paths.json` is **gitignored** — it holds machine-local paths, so it is not part of a fresh clone; the setup flow creates it and fills in the values. The skills themselves never hardcode paths: if the file is missing (you installed the skills by copying folders only), just ask the user where their CUI clone is — or clone it.

## Installing the skills into an agent

Copy (or symlink) the four skill folders into your agent's skills directory:

| Agent | Destination |
|---|---|
| OpenCode | `~/.config/opencode/skills/` |
| Claude Code | `~/.claude/skills/` |
| Codex / others | any directory your agent reads skills from |

The files are plain Markdown — any agent that can follow instructions can use them even outside these formats.

## RTL / Persian support

Covered at every layer, because CUI ships real BiDi + OpenType shaping:

- **`cui-app`**: `CUI_DIRECTION_RTL` / `AUTO`, `CUI_TEXT_SHAPING` build option, font-fallback recipe
- **`cui-py`**: shaping is on by default (`fonts.supports_text_shaping()`), `direction=` on containers, `ctx.use_rtl_font()`, localized calendars
- **`cui-style`**: tested webfont URLs, `@font-face`, logical properties, always-RTL rules, Latin digits in Persian prose

## Repository layout

```
cui-skills/
├── README.md            ← you are here
├── setup.mjs            ← agent-less setup (npx github:ChiakoRh/cui-skills)
├── package.json         ← makes the npx invocation work
├── paths.json           ← written by setup (gitignored, not in a fresh clone)
├── commands/
│   └── cui-setup.md     ← /cui-setup slash command
├── cui-app/
│   ├── SKILL.md         ← the main guide
│   ├── api.md           ← ~210 components by category
│   ├── patterns.md      ← copyable UI shapes
│   └── template/        ← CMakeLists.txt + main.c starter
├── cui-web/
│   └── SKILL.md         ← build, browser constraints, hosting
├── cui-py/
│   └── SKILL.md         ← nexa: install, model, theming, RTL, docs map
└── cui-style/
    ├── SKILL.md         ← tokens, Lucide, RTL, restyle workflow
    ├── tokens.css       ← the design tokens
    ├── components.css   ← ready-made components
    ├── react-tailwind.md
    ├── cui.py           ← scaffolder
    ├── example.html     ← full styled demo page
    └── fonts/           ← Geist + OFL license
```

Upstream: [CUI](https://github.com/yappologistic/CUI) · docs: https://yappologistic.github.io/CUI/ · Python port: [nexa](https://github.com/x017/nexa)
