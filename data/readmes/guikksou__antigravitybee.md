# Antigravity Bee Companion

![Antigravity Bee Preview](./preview.gif)

A lightweight, 60-FPS pixel-art desktop overlay for Google Antigravity (CLI, IDE, and Antigravity 2.0) on Windows and Linux.

It runs as an always-on-top desktop widget and reacts in real time (with zero token overhead) to the agent's execution loop: thinking, reading files, editing code, running terminal commands, orchestrating subagents, waiting for user input, or completing a task.

## Features

- **Zero-Token Lifecycle Synchronization**
  - Uses Antigravity lifecycle hooks (`hooks.json`) and a live `transcript.jsonl` tailer to update animations locally without querying the model.
  - Auto-launches on `SessionStart` by default. Can be disabled at any time from the right-click context menu or via `/bee auto off`, after which it can be started on demand with `/bee`.
- **State Transitions**
  - Working states: Thinking (glasses), Reading (magnifying glass), Coding (pencil), Terminal (hard-hat and prompt), Web (goggles), Swarm (crown and orbiting worker bees).
  - Notification states: Needs Input (`[!]`) alerts when user approval or an answer is required; Done (`[✓]`) displays a green completion badge, transitions automatically to `Idle` after 45 seconds, and enters `Sleep` after 90 seconds of inactivity.
- **Desktop Interactions**
  - 4 integer pixel-art scale presets: Small (`3x`), Medium (`4x`), Large (`5x`), and Extra Large (`7x`).
  - Subtle 1-pixel eye tracking towards the mouse cursor.
  - Mouse petting detection, click-to-acknowledge alerts, drag-and-drop with leg tilt physics, and Ghost Mode (45% opacity while idle/working, 100% when hovered or alerting).

## Installation

### Option 1: Global Installation (Recommended — Works in ALL Folders & Projects)

Install the plugin once into your global Antigravity configuration (`~/.gemini/config/plugins/antigravitybee`) so the bee is available everywhere, no matter which directory you open Antigravity in:

- **Linux / macOS**:
  ```bash
  git clone https://github.com/guikksou/antigravitybee.git ~/.gemini/config/plugins/antigravitybee
  ```
- **Windows (PowerShell)**:
  ```powershell
  git clone https://github.com/guikksou/antigravitybee.git "$HOME\.gemini\config\plugins\antigravitybee"
  ```

### Option 2: Per-Project Installation (Single Workspace Only)

If you only want the bee inside a specific project folder, clone it as `.agents` at that workspace's root:

```bash
git clone https://github.com/guikksou/antigravitybee.git .agents
```

The widget launches automatically on your next Antigravity session. You can also control it manually using the `/bee` slash command.

## Requirements

- **Windows**: Python 3.10+ (uses standard library `tkinter` and `ctypes`).
- **Linux (X11)**: Python 3.10+ with `tkinter`:
  - Debian / Ubuntu: `sudo apt install python3-tk`
  - Arch Linux: `sudo pacman -S tk`
  - Fedora: `sudo dnf install python3-tkinter`
- **Linux (Wayland / Hyprland / Sway)**: Automatically uses the 32-bit ARGB GTK3/Cairo backend (`wayland_widget.py`) for true per-pixel alpha transparency without XWayland black boxes (falls back to `tkinter` if GTK3/PyGObject is not installed):
  - Arch Linux: `sudo pacman -S python-gobject python-cairo gtk3`
  - Debian / Ubuntu: `sudo apt install python3-gi python3-gi-cairo gir1.2-gtk-3.0`
  - Fedora: `sudo dnf install python3-gobject cairo-gobject-devel gtk3`

## Architecture

```text
.agents/
├── plugin.json                 # Antigravity plugin manifest
├── hooks.json                  # Lifecycle hooks configuration
└── skills/
    └── bee/
        ├── SKILL.md            # /bee slash command specification
        └── scripts/
            ├── platform_adapter.py  # OS abstraction & Wayland/X11/Win32 session detection
            ├── pixel_sprites.py     # Palette, 2D pixel grids, PhotoImage & color-span caches
            ├── state_sync.py        # Config, atomic state I/O, and transcript watcher
            ├── bee_widget.py        # Tkinter 60-FPS GUI & Wayland backend dispatcher
            ├── wayland_widget.py    # 32-bit ARGB GTK3/Cairo 60-FPS GUI for Linux Wayland
            ├── bee_hook.py          # Hook handler and SessionStart auto-launcher
            └── bee_ctl.py           # CLI controller (start, stop, auto, size, honey, mode)
```
