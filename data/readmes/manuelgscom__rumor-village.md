# Rumor Village

**A rumor simulation game with an AI trained for it.** Drop a rumor into a 3D village of up to 100 neighbors and watch it travel from mouth to mouth, get twisted on the way and send people to the wrong place at the wrong time. Every neighbor is driven by a small language model fine-tuned for this game, running on your own graphics card. Offline, no accounts.

[![Play in your browser](https://img.shields.io/badge/play%20in%20your%20browser-web%20demo-1f6feb)](https://manuelgs.com/en/rumor-village/demo/) [![Download for Linux and Windows](https://img.shields.io/badge/download-Linux%20%C2%B7%20Windows-2ea44f)](https://github.com/manuelgscom/rumor-village/releases/latest) [![Model on Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20model-rumor--village--e4b--GGUF-FFD21E)](https://huggingface.co/manuelgscom/rumor-village-e4b-GGUF) [![license: MIT](https://img.shields.io/badge/code-MIT-e36209)](LICENSE) [![model: Apache-2.0](https://img.shields.io/badge/model-Apache--2.0-e36209)](https://huggingface.co/manuelgscom/rumor-village-e4b-GGUF/blob/main/LICENSE) [![llama.cpp: CUDA or Vulkan](https://img.shields.io/badge/llama.cpp-CUDA%20%C2%B7%20Vulkan-8250df)](https://github.com/ggml-org/llama.cpp)

https://github.com/user-attachments/assets/153ea4bf-3702-4a12-9a14-b80c25e7e183

*The trailer: real games played With AI, edited by code from the game's own event logs.*

https://github.com/user-attachments/assets/17f7c9b1-cbb3-46f0-8ddb-758592076aab

*Under the hood: 100 neighbors deciding in one batch on one GPU, the card the model read, the JSON it answered and the engine's verdict, base against fine-tuned.*

**No GPU or no time to download? [Play the web demo](https://manuelgs.com/en/rumor-village/demo/)**: the same village and challenges in your browser, Without AI (rules with dice). With AI needs the downloaded game.

## Download and play

No installer, no account, no internet needed to play. Pick the package for your computer from the [latest release](https://github.com/manuelgscom/rumor-village/releases/latest):

| Your computer | Package | Size |
|---|---|---:|
| Windows with an NVIDIA card | [`rumor-village-windows-cuda-1.0.0.zip`](https://github.com/manuelgscom/rumor-village/releases/latest/download/rumor-village-windows-cuda-1.0.0.zip) | 667 MB |
| Windows with AMD or Intel, or an old NVIDIA driver | [`rumor-village-windows-vulkan-1.0.0.zip`](https://github.com/manuelgscom/rumor-village/releases/latest/download/rumor-village-windows-vulkan-1.0.0.zip) | 18 MB |
| Linux with an NVIDIA card | [`rumor-village-linux-cuda-1.0.0.AppImage`](https://github.com/manuelgscom/rumor-village/releases/latest/download/rumor-village-linux-cuda-1.0.0.AppImage) | 627 MB |
| Linux with AMD or Intel, or an old NVIDIA driver | [`rumor-village-linux-vulkan-1.0.0.AppImage`](https://github.com/manuelgscom/rumor-village/releases/latest/download/rumor-village-linux-vulkan-1.0.0.AppImage) | 15 MB |

**NVIDIA? Take CUDA. Another card, or not sure? Take Vulkan.** CUDA is faster on NVIDIA and needs driver 525.60.13 or later on Linux, 528.33 or later on Windows. Vulkan works on NVIDIA, AMD and Intel. There is no Mac version. Checksums: [`SHA256SUMS`](https://github.com/manuelgscom/rumor-village/releases/latest/download/SHA256SUMS).

- **Windows:** unzip it and double-click `rumor-village.exe`. The program is not signed: if "Windows protected your PC" appears, click "More info" and then "Run anyway".
- **Linux:** allow the AppImage to run (Properties > "Allow executing file as program", or `chmod +x`) and double-click it. Without FUSE: `./rumor-village-linux-*.AppImage --appimage-extract-and-run`.
- **The first time:** the game opens at once and you can play Without AI. If your graphics card can run the AI, the game downloads it (5.34 GB, from [Hugging Face](https://huggingface.co/manuelgscom/rumor-village-e4b-GGUF), checked with SHA-256, resumable) while you play; then press "Turn on With AI". That download is the only time the game goes online.

The full player guide: [docs/guia-jugador.en.md](docs/guia-jugador.en.md).

## How a game goes

```
  prepare ───────────────────► Start ─────────────────────► watch ───────────────────► the end
  what happened (a party,      07:00, the village wakes    bubbles, the rumor's trail,  who heard it, who came
  a lottery prize, a fine…),   up; you only watch          who changed it and why       to the right place and time,
  where and when, and whom                                 ("What did they think?")     stars, "Who did it?",
  you tell it to                                                                        a friend’s challenge
```

- **Six challenges with stars:** *Fill the square*, *Patient zero*, *Against the clock*, *Broken telephone*, *Surprise party* (everyone comes, except the guest of honor) and *Tell the priest* (without telling him yourself), plus a free game and a tutorial.
- **Villages of 10, 25, 50, 70 or 100 neighbors,** each with a name, a job, a character (gossip, discreet, forgetful…), family, friends and rivals.
- **"Who did it?":** at the end, guess which neighbor twisted the rumor. **"Friend’s challenge":** share a code; your friend plays the same village and the same rumor.

**Two modes, always labeled on screen:**

- **With AI:** the fine-tuned model decides what every neighbor does and says. You can type the rumor in your own words, and open "What did they think?" on any neighbor. Needs a graphics card.
- **Without AI:** rules with dice decide. There are no sentences in the bubbles, the game is instant and works on any computer.

| | |
|---|---|
| ![Prepare the game](assets/setup.jpg) | ![What did they think?](assets/what-did-they-think.jpg) |
| *Prepare the game: the rumor, whom you tell it to, and each neighbor's character.* | *"What did they think?": what a neighbor knew, believed and decided.* |
| ![A challenge with stars](assets/challenge-stars.jpg) | ![Who did it?](assets/who-was-it.jpg) |
| *A challenge with stars, and who moved the rumor.* | *"Who did it?": guess who twisted it.* |
| ![Neighbors with AI](assets/how-it-works-ai.jpg) | ![The end of a game](assets/end-who-moved-it.jpg) |
| *With AI and Without AI, with a real moment of a game.* | *The end: who heard it, who came, who moved it.* |

## How it is made

```
  every neighbor, every simulated minute
  ┌───────────────────────┐   ┌─────────────────────────┐   ┌─────────────────────┐   ┌──────────────────┐
  │ card: who I am, what I │──►│ fine-tuned Gemma 4 E4B   │──►│ JSON action, forced │──►│ the engine checks │──► memory, map,
  │ know, who is near me   │   │ (llama.cpp, all the      │   │ by a grammar: say,  │   │ it against the    │    bubbles,
  │ (~256 tokens, shared   │   │ neighbors in one batch)  │   │ go, ask… + a short  │   │ rules and applies │    event log
  │ prefix cached)         │   │                          │   │ sentence            │   │ or rejects it     │
  └───────────────────────┘   └─────────────────────────┘   └─────────────────────┘   └──────────────────┘
                                   the model proposes ─────────────────────────────────► the engine decides
```

- **The model proposes and the engine decides.** No action is applied without validation; the state travels as structured data, and nobody decides from the text of a bubble.
- **Every decision goes through the model**, in one batched loop of llama.cpp embedded in a C++ engine with integer-only simulation, so a game with the same seed replays exactly.
- **A model trained for the game.** The base model needed a 921-token prompt per decision; the fine-tuned one reads a 256-token card and makes far fewer mistakes (below).

![The batch panel: every neighbor deciding in one batch](assets/dev-batch-panel.jpg)

*The technical view of a recorded game: the batch of decisions, tokens per second and VRAM, live.*

## Base against fine-tuned

Gemma 4 E4B in Q4_K_M, the base with its full prompt and the fine-tuned one with its short card. Frozen decision test of 1,000 decisions per language, with the 95 % interval:

![Frozen decision test](assets/quality.png)

| | Spanish | English |
|---|---|---|
| Made-up memories (base → fine-tuned) | 2.0 % → **0 %** | 2.3 % → **0 %** |
| Failures (made up, contradiction or incoherent text), base / fine-tuned | **16.5×** fewer | **5.0×** fewer |
| Rejected actions (base → fine-tuned): **worse** | 0.10 % → 1.0 % | 0.10 % → 0.90 % |
| Naturalness of the dialogue, 1–5, LLM judge, 100 answers | 3.7 → **4.2** | 3.6 → **4.1** |

![Split screen, base against fine-tuned](assets/dev-split-screen.jpg)

*Split screen, same village and seed: the base model gets stuck in endless chats; the fine-tuned one closes them and makes nothing up.*

In the village (`party-100`, 100 neighbors, one simulated day, RTX 5070 Ti, batch up to 16, one run per row), the short card cuts the prompt to a third and halves the time per simulated minute:

![party-100](assets/cost.png)

## For developers

The repository keeps every mode: the game, scenarios, live runs, recordings and the prebuilt packages. Everything builds and runs in Docker; nothing is installed on your system.

```bash
git clone --recursive https://github.com/manuelgscom/rumor-village.git
cd rumor-village
./play.sh --no-ai          # the game, Without AI: builds the engine in Docker and opens the browser
```

| What | Command |
|---|---|
| The game With AI (NVIDIA + NVIDIA Container Toolkit) | download the model to `models/` (below), then `./play.sh` |
| Engine tests (CPU, no model) | `scripts/engine-test.sh` |
| Viewer tests | `scripts/viewer-test.sh` |
| A scenario live in the viewer, rules or model | `scripts/serve.sh party-25 1` · `scripts/serve.sh party-100 1 --model /models/<file>.gguf` |
| The Linux packages | `scripts/dist-build.sh linux-cuda` · `linux-vulkan` |
| The web version, Without AI (WebAssembly) | `scripts/wasm-build.sh` |

```bash
mkdir -p models && curl -L -o models/gemma-4-E4B-it-rumor-Q4_K_M.gguf \
  https://huggingface.co/manuelgscom/rumor-village-e4b-GGUF/resolve/main/gemma-4-E4B-it-rumor-Q4_K_M.gguf
```

The pipeline that built the dataset, fine-tuned the model and ran the benchmark is not part of this repository. Its result is [the model](https://huggingface.co/manuelgscom/rumor-village-e4b-GGUF), with its card and results, and this repository keeps the frozen test and the prompts that the engine tests read.

The player guide is [docs/guia-jugador.en.md](docs/guia-jugador.en.md). The contract between the engine and the model (the card it reads and the action it answers) is summarized in the [model card](https://huggingface.co/manuelgscom/rumor-village-e4b-GGUF).

```
 engine/    C++ engine: simulation, validation, llama.cpp batch loop, server, launcher
 data/      village, neighbors, vocabulary, challenges
 viewer/    3D viewer and the game (three.js, no build step)
 dist/      prebuilt packages: Linux AppImage, Windows .zip, model.json (where the model comes from)
 docker/    build and test images        scripts/   shortcuts: build, test, play, serve, package
 runs/samples/  recorded games for the viewer
```

## License

The code is [MIT](LICENSE). The model is Apache-2.0, fine-tuned from Google's [Gemma 4 E4B](https://huggingface.co/google/gemma-4-E4B-it). Third-party notices travel with every package (`THIRD_PARTY_NOTICES.txt`). The 3D characters and buildings are by Kenney (CC0).

Made by **Manuel García Sanz** · <https://manuelgs.com/en/rumor-village/> · [web demo](https://manuelgs.com/en/rumor-village/demo/)
