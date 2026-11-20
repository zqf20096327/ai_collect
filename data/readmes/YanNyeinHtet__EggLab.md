# EggLab

**Local AI image generation and editing for Windows.** A floating egg opens a design agent
for **PhotoCraft** — chat, generate, edit layers, and place results straight onto the canvas.

Everything runs on your own GPU: [Qwen-Image-2.1](https://huggingface.co/Qwen) on
[stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp). No ComfyUI, no
Python, no cloud rendering.

![EggLab panel](docs/panel.png)

## What it can do

- **Chat with a design agent** that knows PhotoCraft: layers, masks, text, exports.
- **Generate images** (quality 40-step or turbo 8-step LoRA) at up to 2048 px.
- **Edit images** — reference photos, multi-reference compositions, transparent cut-outs.
- **Place results** on the PhotoCraft canvas as layers, or export flat/layered files.
- **Local-first** — models and renders stay on your disk; only chat text goes to the model
  provider you pick.

## Requirements

- Windows 10 or 11 (x64)
- **PhotoCraft** installed ([download free](https://getartcraft.com/)) — the canvas app EggLab drives; not bundled
- ~25 GB free disk: engine (17 MB–1.5 GB depending on GPU) + models (~20 GB, your choice)
- A GPU is strongly recommended:
  - NVIDIA → CUDA engine (fastest, ~1.4 GB download)
  - Any DX12 GPU → Vulkan engine (~29 MB)
  - CPU works but is slow
- Internet for the engine download and the model downloads

## Install

1. Download **`EggLab-Setup-<version>.exe`** from [Releases](../../releases).
2. Windows SmartScreen will warn because the installer is not code-signed yet:
   **More info → Run anyway**. This is an unsigned-publisher warning, not a
   virus detection; verify `SHA256SUMS.txt` if you want to check the download.
   The fix and the signing options are in [docs/SIGNING.md](docs/SIGNING.md).
3. The installer copies the app (~77 MB) and downloads the engine that matches your GPU
   (SHA-256 verified, resumable; CUDA → Vulkan → CPU fallback if a download fails).
4. Launch EggLab and finish the setup wizard (below).

`SHA256SUMS.txt` is attached to every release if you want to verify the download:

```powershell
Get-ChildItem .\EggLab-Setup-*.exe | Get-FileHash -Algorithm SHA256
```

## First run

![EggLab setup](docs/setup.png)

The wizard checks the four pieces EggLab needs:

| Piece | What it is | What the wizard does |
|---|---|---|
| **PhotoCraft** | The canvas app ([download free](https://getartcraft.com/)) | Detects it, or lets you locate `photocraft.exe` |
| **OpenCode** | The agent runtime | Detects an existing install, or downloads the standalone build (~78 MB) |
| **Engine** | stable-diffusion.cpp | Usually installed already; can re-download and switch GPU variant |
| **Models** | Qwen-Image-2.1 + VAE + text encoder + turbo LoRA | Downloads missing files (resumable) or imports files you already have |

After that, open **Settings** and pick a chat model under **Agent model**. EggLab uses
your OpenCode providers — the free models that ship with OpenCode work, and paid
providers/API keys are configured inside OpenCode itself.

Both the Models and OpenCode steps accept an existing installation:

- **Models** → **Use existing folder…** points EggLab at the folder you already
  use (no copy). **Choose files…** maps individual files if their names differ.
  The default folder is created with `diffusion`, `vae`, `text_encoder`,
  `vision` and `lora` subfolders; **Download missing** writes into them.
- **OpenCode** → **Use existing…** selects your own `opencode.exe`; **Refresh
  models** reads the providers and models from that exact binary.

## Chats are scoped to your document

![Chat list grouped by document](docs/sessions.png)

Every PhotoCraft document keeps its own conversations. Pressing **+** starts a new
thread and leaves the previous one intact in the chat list; the list is grouped by
document, and reopening a document resumes the chat you were reading last (not merely
the one that was messaged most recently). Renders and previews opened by the agent are
folded into one “Generated images” group so they cannot flood the list.

## Auto-update

Installed copies check the GitHub releases of this repository about 12 seconds after launch
and every 6 hours after that. Updates download in the background and ask for a restart;
chats, settings, models and the engine are kept. You can also trigger a check from
**Settings → Check for updates**.

## Where things live

| Path | Contents |
|---|---|
| `%LOCALAPPDATA%\Programs\egglab` | Program files |
| `%LOCALAPPDATA%\EggLab\engine` | Image engine (downloaded, never packaged) |
| `%LOCALAPPDATA%\EggLab\models` | Models, grouped into `diffusion`, `vae`, `text_encoder`, `vision`, `lora` — or the folder you choose |
| `%APPDATA%\EggLab` | Chats, settings, logs, renders (`out`) |

Uninstalling removes the app and the engine, keeps your chats/settings, and asks before
deleting models.

## Build from source

```powershell
cd panel
npm install
npm start          # dev panel (uses the repo checkout layout)
npm run test:agent # agent/tool/config regression gate (no GPU)
npm run dist       # one-click installer in ..\dist
```

Node 20+ is required for development only; the released installer needs nothing but Windows.

Releases are published by pushing a `v*` tag — see
[`.github/workflows/release.yml`](.github/workflows/release.yml). The workflow
runs the agent gate, builds the installer on a Windows runner, and uploads the
installer, `latest.yml` and `SHA256SUMS.txt` to the release. Bump the version in
`panel/package.json`, commit, then push the matching tag.

## Project layout

```
egglab.ps1              engine runner (text-to-image, edit, turbo)
panel/                  Electron panel + agent + service layer
panel/build/            NSIS customization + engine downloader
panel/service/          settings, engine, chat, models, setup, updater
panel/skills/           progressive agent skills
panel/references/       knowledge references
panel/templates/        document templates
```

## Performance

The **Official Q4_K_M** model is available as a beta in Settings → Models. On an
8 GB RTX 4060 Ti it measured ~35% faster than the FP8 default for Turbo
text-to-image (29 s vs 47 s at 864×1152) and ~10% faster for one-reference
edits, because the diffusion weights are 2.9 GB smaller. It is the official
(non-uncensored) checkpoint; install it alongside FP8 and switch only when you
want the speed.

The diffusion menu is kept to three curated variants: **Uncensored FP8**,
**Official Q4_K_M (Beta)** and **Uncensored Q5_K_M**. BF16, Q8_0 and Q4_K_S are
no longer offered.

Every job records the diffusion file it actually loaded, and the job card shows
a small model tag (FP8 / Q4_K_M / Q5_K_M). Manual renders and agent renders use
the same engine config, so switching the model in Settings applies to both.
A 2.5 s settle window protects the first render after a switch from racing the
previous engine's teardown.

Measured engine/backend/flag results and sources are in
[PERFORMANCE-RESEARCH.md](PERFORMANCE-RESEARCH.md). The UI/function fixes from
the same audit are in [UI-AUDIT.md](UI-AUDIT.md).

## Troubleshooting

**“qwen3vl … failed during workspace capacity check” / “failed during weight preparation” (8 GB cards).** The diffusion model (6.6 GB), the text encoder (6 GB) and multi-reference edits all compete for VRAM. EggLab now:
- retries a failed render with the text encoder in RAM (the job detail says “Text encoder on CPU”);
- scales reference photos to 768 px on the long side before the engine sees them (Settings → Output → **Reference size**), because a 1080×1700 export becomes ~7300 latent tokens per reference and makes four-reference edits exceed an 8 GB card;
- closes leftover engine processes at startup and after every render — a stray `sd-cli` holding 3 GB of VRAM used to make later jobs fail at random stages.

If a render still hits the wall, EggLab automatically retries it at up to 1024×1280 with the same
aspect ratio (the job reports the reduced size); if it still fails, lower the output size or
reference size manually.

**Chat says the OpenCode data is outdated.** OpenCode keeps all sessions in one shared
SQLite database and newer clients upgrade its schema. EggLab picks the newest installed
OpenCode automatically; if only an old one exists, open Setup and install it again.

## License

MIT — see [LICENSE](LICENSE).
