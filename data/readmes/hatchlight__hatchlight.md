<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/logo-dark.svg">
    <img src=".github/assets/logo-light.svg" alt="Hatchlight" width="360">
  </picture>
</p>

<p align="center">
  <a href="https://github.com/hatchlight/hatchlight/releases/latest"><strong>Download</strong></a> ·
  <a href="docs/getting-started.md">Getting started</a> ·
  <a href="https://hatchlight.app">Website</a> ·
  <a href="CONTRIBUTING.md">Contribute</a>
</p>

<p align="center">
  <a href="https://github.com/hatchlight/hatchlight/actions/workflows/ci.yml"><img src="https://github.com/hatchlight/hatchlight/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://scorecard.dev/viewer/?uri=github.com/hatchlight/hatchlight"><img src="https://api.scorecard.dev/projects/github.com/hatchlight/hatchlight/badge" alt="OpenSSF Scorecard"></a>
  <a href="https://www.bestpractices.dev/projects/16935"><img src="https://www.bestpractices.dev/projects/16935/badge" alt="OpenSSF Best Practices"></a>
  <a href="https://www.npmjs.com/package/hatchlight"><img src="https://img.shields.io/npm/v/hatchlight" alt="hatchlight on npm"></a>
  <a href="https://glama.ai/mcp/servers/hatchlight/hatchlight"><img src="https://glama.ai/mcp/servers/hatchlight/hatchlight/badges/score.svg" alt="Hatchlight MCP server on Glama"></a>
</p>

![Hatchlight: one prompt sent to SDXL Turbo and Stable Diffusion XL on this computer, both pictures forming side by side, each with its time (the wait is sped up 7×, as the video says)](.github/assets/compare.gif)

Make pictures and videos with many AI models, side by side. Run them on your
own graphics card for free, or use the services you already pay for with your
own keys. Open source, no account, no telemetry.

- **Compare models side by side.** One prompt goes to several models, and each
  result shows its time and cost.
- **Learn which model you prefer.** Pick the best result of a comparison,
  blind if you like, and Hatchlight ranks the models by your picks, with the
  median time and cost on your computer. Share the ranking as an image or
  Markdown.
- **Saved characters and styles.** Keep a character's pictures, LoRAs and
  words, or a style, and use them by name in the app, the chat, the terminal
  and other apps.
- **Runs on your graphics card.** Hatchlight looks at your computer, picks the
  version of each model that fits it, downloads and checks the files, and runs
  them. Free, private, and offline once downloaded.
- **Your own keys, no middleman.** Cloud models are called straight from your
  computer with your key.

| SDXL Turbo                                                    | Stable Diffusion XL                                              | FLUX.1 schnell                                                      | Z-Image Turbo                                                       |
| ------------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| ![Fox by SDXL Turbo](apps/web/public/samples/sdxl-turbo.webp) | ![Fox by Stable Diffusion XL](apps/web/public/samples/sdxl.webp) | ![Fox by FLUX.1 schnell](apps/web/public/samples/flux-schnell.webp) | ![Fox by Z-Image Turbo](apps/web/public/samples/z-image-turbo.webp) |

_One prompt, four models, one RTX 4070 SUPER: "a red fox curled up in fresh
snow, soft morning light"._

## What it does

**Models on your computer.** Picture and video models from the catalog, many
of them in 16, 8 and 4 bit versions for different amounts of memory:

- pictures: SDXL Turbo, Stable Diffusion XL and 1.5, FLUX.1 schnell, FLUX.2
  klein, Z-Image, Qwen-Image, Chroma1, LongCat-Image, HiDream-O1, PixArt-Σ and
  more;
- editing by instruction: Qwen-Image-Edit, LongCat-Image-Edit, FLUX.2 klein
  and more;
- video: Wan 2.1 and Wan 2.2, from words or from a first frame;
- Real-ESRGAN to upscale ×4.

Pictures sharpen on screen while they form. A model stays loaded between
pictures, and several Hatchlight windows share one graphics card without
running out of memory.

**Models in the cloud, on your keys.** [fal](https://fal.ai),
[Replicate](https://replicate.com), [OpenRouter](https://openrouter.ai), OpenAI
and Google Gemini: FLUX, GPT Image, Nano Banana, Veo, Kling, Hailuo, Wan,
Seedream, Runway and more. Each result shows what it cost.

**Edit what you made.** Any picture can be the reference for the next prompt or
the first frame of a video. Change it a little or a lot, paint a mask and redraw
only that part, make room around it, crop, turn or flip it, or upscale it.
A guide picture sets the outlines, pose or depth of a new one, with Z-Image
Turbo, guided: on your card it finds outlines itself and takes a ready pose
or depth map, and through fal it makes the map from any photo. Models that
follow given pictures, such as FLUX.2 klein, keep the person from a
reference in new scenes.

**Your own styles.** Load LoRAs and your own SDXL or SD 1.5 checkpoints, or
train an SDXL LoRA from your pictures: Hatchlight writes the captions, shows
sample pictures while it learns, and lets you keep an earlier step. Already
have models in ComfyUI, AUTOMATIC1111, Forge, Forge Neo, SwarmUI or Stability Matrix? Point
Hatchlight at that folder and it uses them where they are, without copying.
From Hugging Face, `hatchlight install hf:owner/repo` (or a
`hatchlight://hf/owner/repo` link) adds a catalog model, an SDXL or SD 1.5
checkpoint, or a LoRA, once it has shown you the size and license.

**An assistant.** Talk to it in the Chat view: "make the fox bigger", "now in
16:9, with FLUX". It picks models, writes the prompts and makes the pictures.
When an idea leaves something open (the shape, the look, which model), it asks
first, with answers you pick in one click. It can look at what came out and
suggest a fix. Making a series with one character, such as a comic or a
mascot, it checks that each new picture still shows the same character and
fixes what drifted. The Advanced view
shows the same session with every setting. It asks before anything paid and
keeps to a spend limit. Write in your own language: each model gets the prompt
in the words it understands, and **Improve prompt** turns a short idea into a
detailed one. The language models that do this on your computer are chosen
in **Settings**, as cards to install: Qwen3 4B writes, and Qwen2.5-VL or
Qwen3-VL (4B or 8B) look at pictures.

![Hatchlight: a chat with the assistant, showing three takes of a fox in the snow from three models on this computer](.github/assets/chat.webp)

![The Advanced view: next-prompt settings on the left, results per model in the middle, the chosen picture on the right](.github/assets/advanced.webp)

**A gallery.** Every result is saved on your computer with the prompt and
settings that made it, and you can search it.

<p align="center">
  <img src=".github/assets/gallery.webp" alt="The gallery: every picture made, in a grid" width="68%">
  <img src=".github/assets/phone.webp" alt="Hatchlight on a phone: the chat with a bottom bar" width="28%">
</p>

A short guided tour, offered after the first picture and kept under
**Tutorial**, shows where models, styles, cloud keys and the gallery are.

The interface speaks English and Brazilian Portuguese, works on phones and
tablets as well as desktops, and can be used with the keyboard and a screen
reader. More languages are welcome: see [Translate](CONTRIBUTING.md#translate).

## Where it runs

| System               | The app | Models on your computer                              |
| -------------------- | ------- | ---------------------------------------------------- |
| Windows              | Yes     | NVIDIA (CUDA), AMD (ROCm), other cards (Vulkan), CPU |
| macOS, Apple Silicon | Yes     | Metal                                                |
| Linux                | Yes     | NVIDIA (CUDA), CPU                                   |
| macOS, Intel         | Yes     | Not yet: cloud models only for now                   |

Under WSL on Windows, the Windows engines run. On Linux itself, local models
are new and still being tested on real machines
([#36](https://github.com/hatchlight/hatchlight/issues/36)).

About 8 GB of graphics card memory runs the quick models, such as SDXL Turbo;
4 to 6 GB runs Stable Diffusion 1.5 and the smallest version of Z-Image
Turbo. With
less, or no graphics card, cloud models still work. See
[Which model to start with](docs/getting-started.md#which-model-to-start-with).

Some parts need more:

- training a LoRA needs Windows (or WSL) and an NVIDIA card with 12 GB of
  memory, and downloads about 6 GB of tools the first time;
- prompt translation and Improve prompt run on your computer on Windows and
  WSL, and the local assistant only in the Windows app; elsewhere they can use
  a cloud key instead.

## Install

**Desktop app:** download the installer for your system from the
[latest release](https://github.com/hatchlight/hatchlight/releases/latest). It
updates itself when a new version comes out. The installers are not signed
yet: if Windows or macOS warns you,
[Getting started](docs/getting-started.md#install) says what to do. Why, and
how signing will work: the [code signing policy](CODE_SIGNING_POLICY.md).

**New to Hatchlight?** [Getting started](docs/getting-started.md) walks you
from the first picture to editing, styles of your own, and what to do when
something goes wrong.

**From source**, with [Bun](https://bun.sh) 1.4 or newer:

```sh
git clone https://github.com/hatchlight/hatchlight.git && cd hatchlight
bun install
bun run build
bun run start
```

This opens `http://localhost:4096`. `bun run start --help` lists the options.
Keys can also come from the environment: `FAL_KEY`, `OPENAI_API_KEY`,
`GEMINI_API_KEY`, `REPLICATE_API_TOKEN`, `OPENROUTER_API_KEY`.

**As a server** for the people of your home or a small team, on a home
server or NAS with an NVIDIA card: run the Docker image, with accounts and a
private gallery for each person. See [Self-hosting](docs/self-hosting.md).

## Use it from the terminal or an AI agent

The same program makes pictures from the command line, and lets agents that
speak the [Model Context Protocol](https://modelcontextprotocol.io), such as
Claude Code or Claude Desktop, use your models. With [Bun](https://bun.sh)
installed:

```sh
bunx hatchlight generate "a lighthouse at dusk" -m local/sdxl-turbo -o out/
claude mcp add hatchlight -- bunx hatchlight mcp
```

In the app, **Settings > Use with AI agents** connects Claude Desktop for you.
[Command line and agents](docs/command-line.md) covers every command, setting
up from the terminal, and spending limits for agents.

`hatchlight check ast_… --like ast_…` and the agents' `check_consistency`
tool score how much a picture shows the same character as earlier ones, and
say what differs.

Other apps can use your models too: Hatchlight answers OpenAI's image API
and AUTOMATIC1111's, so Open WebUI, LibreChat and scripts (OpenAI) and
SillyTavern (AUTOMATIC1111, the API Forge and SD.Next answer too) make
pictures with it. See [Use it from other apps](docs/other-apps.md).

## Your data

Sessions, pictures and keys stay on your computer:

| System  | Directory                                                  |
| ------- | ---------------------------------------------------------- |
| Windows | `%APPDATA%\hatchlight`                                     |
| macOS   | `~/Library/Application Support/hatchlight`                 |
| Linux   | `$XDG_DATA_HOME/hatchlight` or `~/.local/share/hatchlight` |

On Windows, models and the LoRA trainer live in `%LOCALAPPDATA%\hatchlight`.
`HATCHLIGHT_DATA_DIR` or `--data-dir` puts the data elsewhere, and
`HATCHLIGHT_MODELS_DIR` moves only the models; the app can also move them to
another disk for you. Under WSL, models stay on the Windows side. The graphics
card driver reads them fastest there. Installs made before the rename to
Hatchlight keep using their `open-reel` folders and `OPEN_REEL_*` variables.

Keys are sent only to the provider they belong to and are never returned by
the API. The server listens on `127.0.0.1` only and refuses requests that do
not come from its own page, so other websites cannot use your keys. Nothing is
collected about you: Hatchlight has no telemetry. Besides the providers you
use, it only connects to the sites that host the models, the engines and their
sample pictures, to PyTorch's and Python's package sites when you install the
LoRA trainer, and to GitHub to check for updates.

## Responsible use

You are responsible for what you make with Hatchlight. Do not make pictures of
real people without their consent, and do not use it to deceive or harm
anyone. Training a LoRA asks you to confirm that you may use the pictures.

Each model has its own license, set by its authors. The Models screen shows
whether commercial use is allowed; SDXL Turbo, for example, is free for
commercial use only under a yearly revenue limit. Check the license before you
sell what you make.

## Built with

The interface is React with [shadcn/ui](https://ui.shadcn.com) on
[Base UI](https://base-ui.com) for accessible components,
[prompt-kit](https://www.prompt-kit.com) for the chat, and Tailwind CSS. The
server and the command line run on [Bun](https://bun.sh); the desktop app is
[Tauri](https://tauri.app).

## Contribute

Bug reports, translations, new providers and new local models are all
welcome. [CONTRIBUTING.md](CONTRIBUTING.md) explains how the project is laid
out, how to run it while developing, and what a pull request needs. Everyone
taking part follows the [code of conduct](CODE_OF_CONDUCT.md). To report a
security problem, see [SECURITY.md](SECURITY.md).

## License

[MIT](LICENSE). The models and engines the app downloads keep their own
licenses: see [THIRD_PARTY.md](THIRD_PARTY.md).

## Code signing policy

The installers are not signed yet. Why, who builds, reviews and approves
releases, and what Hatchlight sends over the network:
[CODE_SIGNING_POLICY.md](CODE_SIGNING_POLICY.md).
