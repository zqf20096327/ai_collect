# Switchyard

<a href="https://github.com/cyruspastelero/switchyard/releases/download/demo/switchyard-demo.mp4">
  <img src="docs/img/switchyard-demo-v3.gif" alt="Switchyard sorting every window onto its project's desktop, switching projects with Option 1 to 3, and the dashboard" width="960">
</a>

[Watch the full demo (36 s, with music)](https://github.com/cyruspastelero/switchyard/releases/download/demo/switchyard-demo.mp4)

Switchyard gives each of your projects its own macOS desktop. A small menu bar app reads your Chrome, Arc, Ghostty and editor windows, a local server works out which project each one belongs to, and Sort puts every window on its project's desktop. You switch projects with one key. The same server runs a dashboard for your Claude Code agents: what each one is doing, what it costs, and which ones are waiting on you.

Everything runs on your Mac. Nothing is sent anywhere.

## Requirements

- macOS 14 or newer, on Apple silicon or Intel.
- Node.js 22.18 or newer. The server has no runtime dependencies.
- [Claude Code](https://docs.claude.com/en/docs/claude-code), if you want the agent dashboard. Window sorting works without it.
- To build from source: Xcode or the Xcode Command Line Tools.

## Install

### Download

The app is signed with a Developer ID but not notarized yet, so macOS blocks the first open. After step 1, open **System Settings → Privacy & Security** and click **Open Anyway** next to Switchyard (or run `xattr -dr com.apple.quarantine /Applications/Switchyard.app`).

1. Download `Switchyard-<version>.dmg` from [Releases](https://github.com/cyruspastelero/switchyard/releases), open it and drag Switchyard to Applications.
2. Open Switchyard from Applications and click its menu bar icon. The panel says the server isn't reachable and shows the command that starts it. Click **Copy command**, then paste it into Terminal and run it. It looks like this:

   ```bash
   node "/Applications/Switchyard.app/Contents/Resources/server/src/index.ts" install-service
   ```

   That installs a login service that runs the server bundled inside the app on `127.0.0.1:4280`, using the `node` from your Terminal.
3. If you use Claude Code, add its hooks with the same path and `install` instead of `install-service`.

The server lives inside the app, so drag Switchyard to Applications before you run the command, not from the mounted disk image. Installing a newer `.dmg` over the old app keeps the service working, because the path stays the same.

### Build from source

```bash
git clone https://github.com/cyruspastelero/switchyard.git
cd switchyard
npm test                                 # optional; needs no npm install
node src/index.ts install                # add the Claude Code hooks (skip if you don't use Claude Code)
node src/index.ts install-service        # run the server at login, on 127.0.0.1:4280
bash macos/build-app.sh                  # build macos/build/Switchyard.app
open macos/build/Switchyard.app
```

A source build is signed ad hoc, so macOS asks for Accessibility again after every rebuild. To keep the grant, set `SWITCHYARD_SIGN_IDENTITY` to a code-signing identity from your keychain (a self-signed one works) before running `build-app.sh`.

### Either way

`install` edits `~/.claude/settings.json` and keeps a backup next to it. To undo the steps, run the same command with `uninstall` and `uninstall-service`.

If you'd rather not run a background service, start the server by hand (`node src/index.ts`, or the bundled path without `install-service`) and leave the terminal open.

## Use

| Key or place | What it does |
|---|---|
| <kbd>⌥</kbd><kbd>1</kbd> to <kbd>⌥</kbd><kbd>9</kbd> | Switch to the project on that desktop. |
| <kbd>⌥</kbd><kbd>Space</kbd> | Search your projects and switch. |
| <kbd>⌥</kbd><kbd>T</kbd> | Tidy the current desktop: lay its windows out side by side. |
| Menu bar icon | Sort windows, tidy, open the dashboard, copy the access code. |
| <http://localhost:4280> | The dashboard. |

The dashboard has two views. **Contexts** shows one card per project with its desktop, windows and agents. From there you can Sort, move a window to another project, rename Chrome windows, or park a project (close its browser windows and save the tabs for later). **Activity** shows your agents live, a timeline of their tool calls, alerts for stuck or looping agents, and token costs. See [docs/dashboard.md](docs/dashboard.md) for the panels, alerts, shortcuts and environment variables.

The dashboard asks for a 6-digit access code. It changes every time the server starts. Copy it from the menu bar icon, or run `node src/index.ts access-code`. It is printed when you start the server in a terminal, but never written to `~/.switchyard/server.log`; that log is trimmed to about 512 KB on each start.

Windows Switchyard can't place go to the last desktop as Unsorted, and you can assign them by hand. It never re-sorts a window you placed yourself.

### Desktops

A project's key is both its shortcut and its desktop: the project on <kbd>⌥</kbd><kbd>2</kbd> lives on Desktop 2. The last desktop is shared. Unsorted windows go there, and so does any project without a desktop of its own.

To choose which project is Desktop N, use the desktop select on the project's card (**Desktop 2 · ⌥2**). If another project already has that desktop, the two swap, and the select says so before you pick (**aral — swaps**). Pick **No desktop (shared)** to move a project to the shared desktop. After a change, Switchyard carries both projects' windows to their new desktops, as Sort would, and tidies if Auto-tidy is on. No other window moves. The menu bar's <kbd>⌥</kbd> keys follow within a few seconds.

The **Desktops** strip in the dashboard shows one tile per desktop, in <kbd>Ctrl</kbd>+number order: which project owns it (Shared or Free otherwise), how many windows it has, and which one is on screen now. Click a tile to go there. Drag a tile's project onto another tile to swap the two projects, or onto a free desktop to move the project there. Dragging needs a mouse; from the keyboard or on a phone, use the desktop select on the project's card.

- **Click a tile** (or Tab to its **Desktop N** and press Enter) to switch to that desktop.
- **+ Add desktop** (or **+ Add to Laptop** / **+ Add to Monitor** with two screens), the last tile, adds one at the end of that screen's row.
- **Select** appears when at least one desktop can be closed. Tick one or more tiles (a click on a tile ticks it) and click **Close N desktops** below them. It asks once, saying how many will close and how many are skipped, then closes them through Mission Control one at a time from the highest number down, waiting for each. macOS moves their windows to another desktop on that screen. **Done** leaves Select mode and clears the ticks; adding and dragging are off while it is on.

To move a window to a project, drag its row (from Unsorted or from a card) onto that project's card, or onto its tile in the Desktops strip. It is assigned and carried there at once, and **Undo** shows at the bottom for 10 seconds. Drop it on **Unsorted** to take it out of its project. While you drag, the places that take the window light up and the rest dim: the window's own card says "Already in …", and free desktops and the shared desktop can't take it. Grab the row anywhere, or by the ⠿ grip at its left edge (the most reliable spot in Firefox). Drag works with a mouse only. **Assign to…** and **Move** do the same from the keyboard or on a phone.

**New context** in the Contexts header makes a project from scratch. Name it, keep the next free desktop or pick another, then tick the windows that belong to it: Unsorted windows grouped by app, and windows from other projects (marked with where they are now). Search narrows the list. Create assigns the ticked windows and carries them to the new desktop; the rest stay where they are.

Close is off for a desktop a project owns, for the shared desktop while it holds windows, and for the only desktop on a screen. An empty shared desktop can close, so a desktop you just added can be removed again; the one before it becomes the shared desktop. It is also off when closing would renumber a later project's desktop, since that would put the project on the wrong one. In Select mode, hover a faded tile to see why and which project to move: give that project another desktop (or No desktop) first. A batch close skips these desktops by the same rule, and never closes the last desktop on a screen. Add is off for the same reason on a screen whose new desktop would land before a project's desktop.

macOS has no public way to add or remove a desktop, so Switchyard opens Mission Control and uses its buttons through Accessibility. Mission Control flashes on screen for a moment. Before closing, the app checks that the desktop is still the one you picked and stops if anything changed.

### Layout presets

Tidy lays out windows on its own, but you can teach it your own arrangement.

1. Arrange the windows on a desktop by hand. Say Ghostty on the laptop screen and Chrome on the monitor.
2. Save it: **Save layout…** in the menu bar panel, or **Save layout** under Layouts in the dashboard. Give it a name.
3. Pick where it applies. **Default layout** in the dashboard is used for every project. A project card's **Layout** select overrides it for that project: pick a preset, or Auto for the automatic layout.

From then on Tidy (<kbd>⌥</kbd><kbd>T</kbd>, the panel, the dashboard, and the tidy after Sort) puts each app's windows back in their saved spots. Apps the preset doesn't know get the automatic layout. Undo tidy still works.

A preset that spans two screens needs one desktop across both. Turn off **System Settings → Desktop & Dock → Displays have separate Spaces**, then log out and back in. With it on, each screen has its own desktops and a preset only places windows on the desktop's own screen.

## Permissions

| Permission | Why |
|---|---|
| Accessibility | To read window titles, and to move and resize windows. macOS has no public API for moving a window to another desktop, so Sort drags it there: you'll see the pointer grab each window's title bar for about a second. |
| Automation (Chrome, Arc) | To read tab titles and URLs, and to name Chrome windows. Asked the first time the app talks to each browser. |
| Notifications | One notice when an agent starts waiting on you. Optional. |

The keyboard shortcuts need no permission. The app never records the screen.

## Security

The server listens on `127.0.0.1` only, refuses requests from other websites, and keeps its data in `~/.switchyard` with owner-only file modes. Tool calls are stored as short summaries with secrets redacted, and deleted after 7 days. See [SECURITY.md](SECURITY.md) for the full list of checks and how to report a problem. The HTTP API is in [docs/API.md](docs/API.md).

## Limitations

- Desktops on every display count, numbered in <kbd>Ctrl</kbd>+number order. Only the first 16 are used.
- Ghostty has no scripting interface, so its windows are matched by title (the folder or the Claude session name).
- Chrome can't move a tab between windows through AppleScript. Moving a tab reopens its URL, so page state is lost.
- Arc windows can't be named.

## License

Apache 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE). Switchyard was called Claude Mission Control before; data in `~/.claude-mission-control` and old `MC_*` environment variables are picked up automatically.
