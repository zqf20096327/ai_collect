# kaggle-shell-mcp (`kgsh`)

**Turn free 12h Kaggle GPUs into multi-slot live remote terminals, dual-panel file workbenches, and offline competition runners for AI Agents via MCP.**

[![PyPI](https://img.shields.io/pypi/v/kaggle-shell-mcp.svg)](https://pypi.org/project/kaggle-shell-mcp/)
[![CI](https://github.com/NguyenQuocDat06-AI/kaggle-shell-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/NguyenQuocDat06-AI/kaggle-shell-mcp/actions/workflows/ci.yml)
[![Release TUI](https://github.com/NguyenQuocDat06-AI/kaggle-shell-mcp/actions/workflows/release-tui.yml/badge.svg)](https://github.com/NguyenQuocDat06-AI/kaggle-shell-mcp/actions/workflows/release-tui.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-3776AB.svg)](https://www.python.org/)
[![Rust TUI](https://img.shields.io/badge/TUI-Rust%2060FPS-orange.svg)](./tui/)
[![MCP Compatible](https://img.shields.io/badge/MCP-stdio-00A67E.svg)](https://modelcontextprotocol.io/)

[**Tiếng Việt (Vietnamese Guide)**](./docs/README.vi.md) · [**Architecture**](./ARCHITECTURE.md) · [**Changelog**](./CHANGELOG.md) · [**Contributing**](./CONTRIBUTING.md)

---

## Live Screenshots (Native Rust 60-FPS TUI — `kgsh ui`)

### `F1` Cockpit — Real-Time Shell, Live Script Output, MCP Activity & Job Logs
Watch every `[mcp]` tool call from your AI Agent alongside your own `[tui]` commands, live GPU/VRAM/RAM/Disk telemetry, running foreground loop tailing, and live training logs side by side.

![F1 Cockpit — Live Shell, GPU Telemetry & Streaming Logs](./docs/assets/cockpit.svg)

### `F2` Dual-Panel File Manager & Code Preview Drawer
Browse local files (`Left`) and Kaggle `/kaggle/working`, `/kaggle/input`, `/tmp` (`Right`) with Yazi-style `←` / `→` navigation, `DU%` disk micro-bars, multi-select, cross-panel clipboard (`c`/`x`/`p`), `t` push/pull transfers, and `v` syntax preview drawer.

![F2 Dual-Panel File Manager & Preview Drawer](./docs/assets/dual_files.svg)

<details>
<summary><strong>More screenshots: Remote File Editor & Clean Selection · Multi-Slot Workers & Weekly Quota</strong></summary>

#### Remote File Editor (`Enter` / `→` 2x) — Clean `Shift` / `Ctrl+Shift` & Drag Selection
Drag with the mouse or hold `Shift` / `Ctrl+Shift` + arrow keys to select and copy **only clean code** — never capturing the `Path :` header or `1 │ ` line-number gutters.

![Remote File Editor with Clean Selection](./docs/assets/editor_selection.svg)

#### Workers, Cluster & Quota (`Ctrl+W` / `F5`)
Inspect weekly GPU (30h) & TPU (20h) quota, switch or stop parallel slots (`slot="1"`, `"2"`), and boot from saved profiles (`~/.kaggle_mcp/profiles.json`).

![Workers, Cluster & Weekly Quota Modal](./docs/assets/workers_quota.svg)

</details>

---

## Why `kaggle-shell-mcp`?

- **Zero-Black-Box MCP + 60-FPS Rust TUI (`kgsh ui`)**: Watch every command your AI Agent sends in real time, interrupt hung loops (`Ctrl+C`) on an isolated TUI shell without killing Agent sessions, browse/edit/preview remote files safely (`256 KB` cap with automatic Read-Only lock on truncated/binary files & unsaved-edit guard), inspect `.parquet`/`.csv`/`.safetensors`/`.pt`/`.zip` files, and monitor **Multi-GPU VRAM & `°C` telemetry** (`GPU0`, `GPU1`, ...).
- **Zero-Setup Prebuilt Binary Auto-Download (`x86_64` & `ARM64`)**: Running `kgsh ui` after `pip install kaggle-shell-mcp` automatically downloads the matching prebuilt `kgsh-tui` binary for **Windows (`x86_64`), Linux (`x86_64` & `aarch64` static `musl`), or macOS (`arm64` & `x86_64`)** from GitHub Releases with **Fail-Closed `SHA256SUMS.txt` verification** into `~/.kaggle_mcp/bin/` — **no Rust toolchain required**.
- **SSH-Ready Clipboard (`OSC 52` + Internal Yank Buffer)**: `Ctrl+C`, `Ctrl+X`, `Ctrl+V`, mouse drag, and Bracketed Paste work seamlessly even over headless SSH servers without X11/Wayland.
- **One-Line Credentials & Secret-Safe Sync**: Works out of the box with `KAGGLE_USERNAME` and `KAGGLE_KEY` (`KGAT_...` token, legacy key, or `~/.kaggle/kaggle.json`, requiring `kaggle>=2.2.0`). `fs_sync` and TUI Push automatically exclude `.env*` (keeping `.env.example`), `kaggle.json`, SSH/TLS keys, and local pull directories.
- **Dual Concurrent GPU VMs (`4 × Tesla T4 = 60 GB VRAM`) & Verified Shutdown**: Run up to **2 parallel live Kaggle GPU VMs** (`slot="1,2"`), pin individual background jobs (`gpu_ids="0"` / `"1"`), and stop slots via 3-tier verified shutdown (`kgsh down [-f]`) that never wipes `sessions.json` while a GPU VM is still running.
- **Full Hardware & Kaggle Hub Support**: Target `NvidiaTeslaT4` (`2×15 GB`), `NvidiaL4`, `NvidiaL4x4` (`96 GB`), `NvidiaRtxPro6000` (`96 GB`), `NvidiaH100`, `TpuV5E8` / `TpuV6E8`, or `cpu`, with native `competition_sources` and Kaggle Hub `model_sources` mounts.
- **Offline Competition Mode + Auto-Harvest + Host SSE Live Logs**: When `L4x4` / `RTX Pro 6000` enforces `enable_internet=False`, `kaggle_wheelhouse` + `kaggle_batch_run` use isolated per-run slugs (`kgsh-batch-<slot>-<run>`), automatically harvest relative outputs (`submission.csv`, `checkpoints/`) from `/tmp` into `/kaggle/working` on exit, and stream live stdout via Kaggle's Host SSE endpoint (`kaggle_batch_logs`).
- **11h40m (`8h40m` TPU) Safe-Drain Watchdog**: Sends `SIGTERM` at `11h35m` (`8h35m` on TPU) to flush checkpoints and exits cleanly (`exit 0`) at `11h40m` so `/kaggle/working` (19.5 GB) snapshots persist.

---

## Quickstart (30 Seconds)

### Option A: Zero-Install MCP Server for AI Agents (`uvx`)

Add directly to **Claude Desktop / Cursor / Windsurf / Antigravity** (`mcp_config.json`):

```json
{
  "mcpServers": {
    "kgsh": {
      "command": "uvx",
      "args": ["--from", "kaggle-shell-mcp", "kgsh"],
      "env": {
        "KAGGLE_USERNAME": "your_kaggle_username",
        "KAGGLE_KEY": "KGAT_your_api_token_here"
      }
    }
  }
}
```

Or add to **Claude Code CLI** in one line:
```bash
claude mcp add kgsh -e KAGGLE_USERNAME=your_user -e KAGGLE_KEY=KGAT_your_token -- uvx --from kaggle-shell-mcp kgsh
```

### Option B: Install `kgsh` CLI + Native TUI (`pip` / `uv`)

```bash
pip install kaggle-shell-mcp
# or isolated CLI install:
uv tool install kaggle-shell-mcp
```

Configure credentials via any of:
1. `KAGGLE_USERNAME` + `KAGGLE_KEY` environment variables,
2. `.env` in your project directory or `~/.kaggle_mcp/.env`, or
3. Existing `~/.kaggle/kaggle.json`.

Then launch the TUI or CLI:
```bash
# Launch Dual-Panel Rust TUI (auto-downloads prebuilt kgsh-tui binary on first run)
kgsh ui

# Or manage workers directly from CLI
kgsh quota
kgsh up -s 1
kgsh shell -s 1
```

### Option C: Install from Source (Developers)

```bash
git clone https://github.com/NguyenQuocDat06-AI/kaggle-shell-mcp.git
cd kaggle-shell-mcp
python -m venv .venv
.\.venv\Scripts\pip install -e ".[dev]"   # Linux/macOS: ./.venv/bin/pip install -e ".[dev]"
cargo build --release --manifest-path tui/Cargo.toml
.\.venv\Scripts\kgsh ui
```

---

## MCP Tools Reference (13 Tools)

| Tool | Purpose |
| :--- | :--- |
| `kaggle_quota` | Check remaining weekly Kaggle GPU (30h) & TPU (20h) quota hours and reset timestamp |
| `kaggle_up` | Boot 1 or 2 parallel headless workers (`slot="1"`, `"2"`, or `"1,2"`, `accelerator`, `competition`, `mount_datasets`, `mount_models`, opt-in `idle_timeout_min`) |
| `kaggle_status` | Inspect live GPU/VRAM telemetry, RAM, disk, and kernel states across `slot="all"` or a specific slot (auto-cleans stale sessions) |
| `kaggle_down` | Verified 3-tier shutdown for `slot="1"`, `"2"`, or `"all"` (waits for `COMPLETE` before pulling outputs; `force=True` cancels unreachable/queued ephemeral runners) |
| `term_exec` | Run bash commands in a persistent stateful PTY on `slot` (`cwd`, exports, and virtualenvs persist across calls) |
| `job_spawn` | Launch detached background jobs on `slot` with optional `gpu_ids` (`CUDA_VISIBLE_DEVICES="0"` or `"1"`) |
| `job_list` | List active and finished background jobs on `slot` with PID, GPU assignment, runtime, and log size |
| `job_logs` | Read tail lines of a background job log on `slot` (with regex `grep` and automatic `tqdm` `\r` cleanup) |
| `job_kill` | Send `SIGTERM` or `SIGKILL` to a background job's process group on `slot` and release VRAM |
| `fs_sync` | `push` local folders (auto-blocking `.env*`, `kaggle.json`, private keys & caches) or `pull` remote checkpoints/logs on `slot` |
| `kaggle_wheelhouse` | Download Linux `manylinux_x86_64` binary `.whl` packages and publish a private Dataset for offline runs |
| `kaggle_batch_run` | Submit an isolated run-scoped offline competition batch job (`NvidiaL4x4`, `NvidiaRtxPro6000`, `TpuV5E8`, `enable_internet=False`) with automatic `/tmp -> /kaggle/working` artifact harvesting |
| `kaggle_batch_logs` | Stream live or completed logs via Kaggle's Host SSE endpoint—even when container internet is disabled |

---

## TUI Keyboard & Mouse Cheatsheet (`kgsh ui`)

| Context | Keys / Mouse | Action |
| :--- | :--- | :--- |
| **Global** | `F1` / `F2` / `F3` / `F4` | Switch Presets: `Cockpit` · `Dual Files` · `Jobs & GPU` · `Kaggle Hub` |
| | `Tab` / `Alt+←` `Alt+→` | Switch active panel `LEFT <-> RIGHT` |
| | `Ctrl+W` / `F5` / `Ctrl+K` / `?` | Workers & Quota modal / Boot Profiles / Command Palette / Help |
| | `z` / `m` / `a` / `T` | Zoom active panel 100% / Swap panel content / Context actions / Telemetry |
| | `F8` | Toggle TUI MouseCapture vs. native terminal selection anytime |
| **Selection & Copy** | `Shift` / `Ctrl+Shift` + `↑↓←→` | Select clean text in `FileEditor`, `Shell`, `Logs`, `PreviewDrawer`, `Inspect` & inputs |
| | Mouse Drag | Drag inside any content area to auto-copy (auto-strips borders, headers & line gutters) |
| | `Ctrl+A` / `Ctrl+C` / `Ctrl+X` / `y` | Select all / Copy selection (or interrupt live command) / Cut / Copy |
| **Shell (`F1`)** | `i` / `Enter` · `:run <cmd>` · `Alt+Enter` | Enter `INPUT` mode · Stream long `for`/training loops live |
| **Dual Files (`F2`)** | `←` / `→` (`h` / `l`) · `Enter` · `v` | Parent dir (restores cursor) / Enter dir or Preview (2× opens Editor) / Drawer |
| | `Space` / `Shift+A` / `t` / `c` `x` `p` | Mark / Mark all / Transfer opposite panel / Cross-panel Clipboard |
| | `n` / `N` / `R` / `d` / `/` / `u` / `Shift+X` | New file / New dir / Rename / Delete (2×) / Find / `DU%` / Run script with Live Logs |

---

## CLI Workflows (`kgsh`)

### 1. Parallel Multi-Slot Interactive GPUs (`4 × T4 = 60 GB VRAM`)

```bash
kgsh up -s 1,2                                        # Boot 2 Dual-T4 VMs in parallel
kgsh push ./my_project /kaggle/working -s 1
kgsh push ./my_project /kaggle/working -s 2

kgsh spawn -s 1 --gpus 0 "python my_project/train.py --lr 1e-4" --name exp1
kgsh spawn -s 1 --gpus 1 "python my_project/train.py --lr 3e-4" --name exp2
kgsh spawn -s 2 --gpus 0 "python my_project/train.py --lr 5e-4" --name exp3
kgsh spawn -s 2 --gpus 1 "python my_project/train.py --lr 1e-3" --name exp4

kgsh logs <job_id> -s 1 -f                            # Live tail -f log follower
kgsh down -s all                                      # Clean shutdown when done
```

### 2. Offline Competition Batch Runner (`L4x4` / `RTX Pro 6000`)

```bash
kgsh wheels peft accelerate bitsandbytes --slug lora-deps --py 312
kgsh batch-run "torchrun --nproc_per_node=4 solve.py" \
  --path ./comp_solution -a l4x4 --comp arc-prize-2026 \
  --wheels your_username/kgsh-wheels-lora-deps \
  --model qwen-lm/qwen2.5/transformers/7b-instruct/1
kgsh batch-logs -s batch-1 --tail 80
```

---

## Architecture & Responsible Use

See [**ARCHITECTURE.md**](./ARCHITECTURE.md) for system internals (multi-slot file locking, echo-immune PTY sentinel framing, Host SSE log streaming, and prebuilt TUI binary distribution).

`kaggle-shell-mcp` is built for legitimate ML experimentation, model training, and competition workflows on your own Kaggle account. Respect [Kaggle's Terms of Service](https://www.kaggle.com/terms) and shut down active slots (`kgsh down -s all`) when finished.

Released under the [MIT License](./LICENSE).
