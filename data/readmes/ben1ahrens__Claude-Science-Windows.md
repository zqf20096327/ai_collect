<div align="center">

<img src="windows/icon-src/claude-science.png" width="120" alt="Claude Science Win-Wrapper">

# Claude Science Windows Launcher

**Run [Claude Science](https://claude.com/product/claude-science) on Windows, as a real desktop app.**

*Anthropic ships Claude Science for macOS and Linux only. This gives Windows users a first-class
launcher, backed by WSL2.*

</div>

---

## Overview

### What is Claude Science?

[Claude Science](https://claude.com/product/claude-science) is Anthropic's *"research partner for
rigorous science."* It runs analyses, searches databases, and **traces every step from data wrangling
to publication**, so you can spend your time on the science instead of the plumbing.

It is built for life-sciences researchers (genomics, single-cell, proteomics, structural biology, and
cheminformatics), and includes:

- **Native scientific visualization**: proteins, structures, molecules, alignments, genomic tracks, chemical structures
- **Full reproducibility**: code, environment, and conversation history attached to every artifact
- **A background reviewer** that flags incorrect citations and untraceable data
- **Direct figure editing** via plain-language annotations
- **Manuscript drafting** alongside your analyses
- **Compute management** across laptop, clusters, HPC, and GPUs
- **60+ scientific databases**, persistent **Python and R kernels**, and reusable **skill pipelines**

### Why this project exists

Claude Science is currently in **beta, with official installers for macOS (Apple Silicon + Intel) and
Linux. Windows is not supported.**

But Windows users already have a first-class Linux environment sitting right there: **WSL2**. This
project installs Claude Science *inside* a WSL distribution and gives you a **pinnable Windows
launcher** with the Claude Science icon. Click it, and the app opens in your normal Windows browser.
No terminal, no `wsl` commands, no fuss.

```
Click the taskbar icon  ->  WSL wakes up  ->  daemon starts  ->  browser opens
```

> **Not affiliated with Anthropic.** This is an unofficial community wrapper. It ships **no Anthropic
> binaries**. It downloads and runs the *official* Claude Science installer inside your WSL distro.

---

## Requirements

| | |
|---|---|
| **OS** | Windows 10 (version 2004+) or Windows 11 |
| **WSL** | WSL2 with a Debian/Ubuntu distro (the installer can create one for you) |
| **Account** | A Claude account. Claude Science sign-in requires a paid plan (Pro / Max / Team / Enterprise) |
| **Disk** | ~2 GB inside the WSL distro |

---

## Step 0: Install WSL2 (skip if you already have it)

Open **PowerShell as Administrator** and run:

```powershell
wsl --install
```

Then **reboot**. On first launch you will be asked to create a UNIX username and password. Remember
that password, you will need it once during installation.

Check it worked:

```powershell
wsl --list --verbose      # your distro should show VERSION 2
```

📚 **Official Microsoft guides:**
- [Install WSL](https://learn.microsoft.com/windows/wsl/install): the canonical walkthrough
- [Set up a WSL development environment](https://learn.microsoft.com/windows/wsl/setup/environment): best practices
- [WSL troubleshooting](https://learn.microsoft.com/windows/wsl/troubleshooting): when things go wrong
- [Basic WSL commands](https://learn.microsoft.com/windows/wsl/basic-commands): handy reference

---

## Step 1: Install Claude Science

In **Windows PowerShell** (no admin needed if you are using an existing distro):

```powershell
irm https://raw.githubusercontent.com/ben1ahrens/Claude-Science-Windows/main/install.ps1 | iex
```

The setup wizard will:

1. ✅ **Check WSL** is installed and working.
2. 🐧 **Ask which distro to use.** It detects the ones you already have, or offers to create a fresh
   `Ubuntu-24.04` for you.
3. 📦 **Provision Claude Science** inside that distro (installs `bubblewrap`, `socat`, `curl`, then the
   official Claude Science installer). *You will be asked for your WSL password once, for `sudo`.*
4. 🚀 **Create a "Claude Science" launcher** in your Start Menu.

### Preview without changing anything

To pass options you need a script block rather than a bare pipe into `iex` (`iex` has no parameters
of its own):

```powershell
& ([scriptblock]::Create((irm https://raw.githubusercontent.com/ben1ahrens/Claude-Science-Windows/main/install.ps1))) -DryRun
```

### Installer options

Use the script-block form above, or download `install.ps1` and run it with
`powershell -ExecutionPolicy Bypass -File .\install.ps1 <flags>`.

| Flag | Purpose |
|------|---------|
| `-DryRun` | Preview every action; change nothing |
| `-Distro <name>` | Skip the menu and target a specific distro |
| `-CreateNew` | Skip the menu and create a new distro |
| `-NewDistroImage <name>` | Which image to create (default `Ubuntu-24.04`) |
| `-Root <path>` | Use a local checkout instead of downloading (see [Development](#development)) |

---

## Step 2: Pin it and launch

1. Open the **Start Menu** and type **Claude Science**.
2. **Right-click** the result, then **Pin to taskbar**.
3. **Click it.**

A console window flashes briefly (that is WSL waking up), then Claude Science opens in your default
browser. Each click generates a **fresh single-use login link**, which is by design.

On the very first click the daemon has to cold-start, so give it a few seconds.

---

## How it works

```
Taskbar click
  └─ Claude Science.lnk  ->  wsl.exe -d <distro> -- science-launch
        ├─ science-url   ->  start the claude-science daemon, return a single-use login URL
        └─ rundll32 url.dll,FileProtocolHandler <url>   ->  open the Windows default browser
```

The launcher is a plain Windows **shortcut to Microsoft's own `wsl.exe`**. There is no custom
executable to install, sign, or get quarantined by antivirus. The browser is opened from *inside* WSL
via `rundll32`, whose URL handler correctly handles `&` in login URLs.

Two small helpers are installed into the distro at `/usr/local/bin`:

| Helper | Does |
|--------|------|
| `science-url` | Starts the daemon if needed, prints a single-use login URL |
| `science-launch` | Calls `science-url`, then opens that URL in your Windows browser |

Both are usable on their own from any WSL shell.

---

## Troubleshooting

<details>
<summary><b>Clicking the launcher does nothing</b></summary>

Run the underlying command directly to see the real error:

```powershell
wsl -d <your-distro> -- science-launch
```

Check the shortcut points where you expect:

```powershell
$s = (New-Object -ComObject WScript.Shell).CreateShortcut("$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Claude Science.lnk")
$s.TargetPath; $s.Arguments
```

`TargetPath` should be `C:\Windows\System32\wsl.exe` and `Arguments` should be
`-d <distro> -- science-launch`, **with no quotes around the distro name**. `wsl.exe` does not strip
them, and a quoted name fails with `WSL_E_DISTRO_NOT_FOUND`.
</details>

<details>
<summary><b><code>WSL_E_DISTRO_NOT_FOUND</code> / "There is no distribution with the supplied name"</b></summary>

Confirm the exact name. It is case-sensitive and must be unquoted:

```powershell
wsl --list --quiet
wsl -d Ubuntu-24.04 -- echo hi
```
Then re-run the installer with `-Distro <exact-name>`.
</details>

<details>
<summary><b>Antivirus flags the launcher</b></summary>

It should not. The default launcher is a shortcut to Microsoft's `wsl.exe`, with no custom binary.
If you built the **optional** `.exe` variant yourself, an *unsigned* build will trip SmartScreen and
many AV engines. See [Optional: signed .exe launcher](#optional-signed-exe-launcher).
</details>

<details>
<summary><b>"Failed to start the systemd user session"</b></summary>

A WSL warning, generally harmless here: Claude Science sandboxes with **bubblewrap**, not systemd.
If the distro misbehaves in other ways, try `wsl --shutdown` and relaunch.
</details>

<details>
<summary><b>Two distros, one port</b></summary>

WSL2 distros share a network namespace, so **only one distro at a time** can run the Claude Science
daemon (it binds `localhost:8765`). If you installed into more than one, stop the other:

```powershell
wsl -d <other-distro> -- claude-science stop
```
</details>

<details>
<summary><b>Inspecting the daemon</b></summary>

```powershell
wsl -d <your-distro> -- claude-science status
wsl -d <your-distro> -- claude-science logs
wsl -d <your-distro> -- claude-science stop
```
</details>

---

## Uninstall

```powershell
# Remove the launcher
Remove-Item "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Claude Science.lnk"
Remove-Item -Recurse "$env:LOCALAPPDATA\Programs\ClaudeScienceLauncher"

# Remove the WSL-side helpers (Claude Science itself stays)
wsl -d <your-distro> -- sudo rm -f /usr/local/bin/science-url /usr/local/bin/science-launch
```

Unpin from the taskbar by right-clicking the icon, then **Unpin**.

---

## Development

Clone into WSL (not `/mnt/c`; ext4 is much faster), then drive the installer from your checkout:

```bash
# WSL side: preview, then run for real
bash wsl-setup.sh --dry-run
bash wsl-setup.sh
wsl -d <distro> -- science-url        # prints a http://localhost:<port>/?nonce=... URL
wsl -d <distro> -- science-launch     # opens it in the Windows browser

# Regenerate the icon from source art (pads to square, never stretches)
uv run tools/png-to-ico.py windows/icon-src/claude-science.png windows/claude-science.ico
```

```powershell
# Windows side: install from the local checkout (works even if the repo is private)
$root = '\\wsl.localhost\<distro>\home\<you>\path\to\Claude-Science-Windows'
powershell -ExecutionPolicy Bypass -File "$root\install.ps1" -Root "$root" -DryRun
```

Every mutating script supports `--dry-run` / `-DryRun` and changes nothing in that mode.

### Layout

| Path | What |
|------|------|
| `install.ps1` | Windows installer + setup wizard; creates the `.lnk` |
| `wsl-setup.sh` | Distro-agnostic provisioner; installs Claude Science + the two helpers |
| `windows/claude-science.ico` | App icon (generated) |
| `windows/icon-src/claude-science.png` | Source art |
| `tools/png-to-ico.py` | PNG to multi-resolution ICO converter |
| `windows/Launcher.cs`, `windows/build.ps1` | *Optional* signed-`.exe` launcher variant (unused by default) |

### Optional: signed `.exe` launcher

The default `.lnk` needs no binary. If you want a flash-free `.exe` instead, `windows/` has a tiny C#
launcher and a `build.ps1` that compiles it (icon embedded) with the `csc.exe` that ships with
Windows. **Only ship it code-signed.** An unsigned build is reliably flagged as a false positive by
SmartScreen and antivirus. Free and cheap options:
[Azure Trusted Signing](https://learn.microsoft.com/azure/trusted-signing/) (~$10/mo) or
[SignPath Foundation](https://signpath.org/) (free for public open source). The built `.exe` is
git-ignored so an unsigned artifact is never committed.

---

## Status

🚧 **Beta.** Installer, provisioner, launcher, and icon tooling are working and tested end-to-end.
Known rough edge: the *create a new distro* path requires you to complete WSL's interactive first-run
user setup before installation continues.

## Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the development
setup, how to test a change, and the conventions this repo follows. Bugs in Claude Science itself
belong with Anthropic rather than here.

## License

[MIT](LICENSE) (c) Ben Ahrens.

Claude, Claude Science, and Anthropic are trademarks of Anthropic. This project is an unofficial
community wrapper, is not affiliated with or endorsed by Anthropic, and ships no Anthropic software.
It invokes the official Claude Science installer. Your use of Claude Science is governed by
Anthropic's own terms.
