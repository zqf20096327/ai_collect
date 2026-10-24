<img src="./assets/img/cover.jpg" alt="Awesome AI Tools for Game Developers"/>

# Awesome AI Tools for Game Developers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Originally created by [Thomas Simonini (@simoninithomas)](https://github.com/simoninithomas) at [simoninithomas/awesome-ai-tools-for-game-dev](https://github.com/simoninithomas/awesome-ai-tools-for-game-dev); refreshed and maintained by [aigamedevs](https://github.com/aigamedevs). Released under [CC0 1.0](LICENSE).

This is a curated **collection of AI tools that speed up and improve game development**: 3D models, sprites, textures, animation, voices, music, NPC dialogue, engine assistants, and automated playtesting.

Whether you're an indie developer or part of a studio, **this list helps you find tools that save time, automate the boring parts, and open up new creative options**.

If it helps you, please ⭐ star the repo. Have a tool to add? **[Please contribute](#contributing)**.

## What's new (2026 refresh)

- **Reviewed the upstream PR backlog:** merged 11 useful contributions with their original authors credited in the git history, and declined spam, off-topic tools and dead links.
- **Added new categories:** 3D Model Generation, 2D Sprites & Pixel Art, World & Level Generation, Engine Integrations & MCP Servers, Music & Sound Effects, Playtesting & QA, and Showcases & Galleries.
- **Added 2025–2026 tools**, including Hunyuan3D 2.1, TRELLIS.2, Meshy, Tripo, PixelLab, Retro Diffusion, Unity AI, Bezi, Blender/Unity/Godot/Unreal MCP servers, Chatterbox, Kokoro, ACE-Step, NobodyWho, LLMUnity and nunu.ai.
- **Fixed dead links and removed tools that have shut down, been abandoned or been superseded.**
- **The numbers (counted from this file):** the list has **94 unique tools** in **98 entries**; Ludo.ai, Rosebud AI, Stable Diffusion 3.5 and ChatGPT each appear in two sections. The original list had 35 tools. **18** of them are still listed (Stable Diffusion is now Stable Diffusion 3.5, Claude 100k is now Claude, and GPT-4 32k is now OpenAI API models). **76** tools are new, and **17** of the original tools were removed.
- **Removed from the original list (17):**
  - Shut down: Ready Player Me, Luma Genie, Charmed Texture Generator, Charmed Tilemap Generator, RADiCAL, Coqui Studio and Replica Studios.
  - Abandoned (no updates since 2023–2024): Haddock, Plask, eastworld and UnityMLPySocket.
  - Archived: Hugging Face API Unity Integration.
  - Outdated models with better replacements: MPT-7B-StoryWriter, StarCoder, ControlNet v1.1, Facebook Wav2Vec2 and Bark.
- **Added during the refresh and later removed (4):** Stable Fast 3D (no updates since January 2025; TRELLIS.2 and Hunyuan3D 2.1 do the job better), chongdashu unreal-mcp (no updates since April 2025; the actively maintained Unreal-MCP is listed instead), Udio (downloads and commercial use ended after the October 2025 UMG settlement) and Aicade (no sign of activity since 2024).

## Contents

- [Asset Generation](#asset-generation-)
- [3D Model Generation](#3d-model-generation-)
- [2D Sprites & Pixel Art](#2d-sprites--pixel-art-)
- [Texture Generation](#texture-generation-%EF%B8%8F%EF%B8%8F)
- [Image Generation](#image-generation-%EF%B8%8F)
- [World & Level Generation](#world--level-generation-)
- [Code Generation/Assistant](#code-generationassistant-)
- [Engine Integrations & MCP Servers](#engine-integrations--mcp-servers-)
- [Animation Video Mocap](#animation-video-mocap-)
- [Voice Generation](#voice-generation-%EF%B8%8F)
- [Music & Sound Effects](#music--sound-effects-)
- [Speech Recognition](#speech-recognition-)
- [Conversational Models](#conversational-models)
- [Story Telling Models](#story-telling-models)
- [Game Design & Prompt-to-Game](#game-design--prompt-to-game-)
- [AI NPC](#ai-npc)
- [Playtesting & QA](#playtesting--qa-)
- [Showcases & Galleries](#showcases--galleries)
- [Python Libraries](#python-libraries)
- [C# Libraries](#c-libraries)
- [Contributing](#contributing)

## Asset Generation 🪄

➡️ When you want to **create a 2D or 3D asset for your game**.

- [Scenario.com](https://www.scenario.com/) (Proprietary, Sign Up, Free): Generate assets such as textures, concept art, and background assets.
- [Ludo.ai](https://ludo.ai/) (Proprietary, Sign Up, Free, Paid): Generate game-ready sprites, icons, UI, textures, music, 3D models and video, in 30+ art styles or matched to your own style references. MCP server, REST API and Unity plugin.
- [CharGen](https://getchargen.com) (Proprietary, Free): AI character generator that creates portraits, backstories, and full character sheets for DnD, anime, fantasy, and game characters.
- [Rosebud AI](https://rosebud.ai/) (Proprietary, Sign Up, Free): Generate 2D or 3D assets for free in prompt to game creator.

## 3D Model Generation 🧊

➡️ When you want to **turn a text prompt or an image into a 3D model**.

- [Meshy](https://www.meshy.ai/) (Proprietary, Sign Up, Free, Paid): Text- and image-to-3D with texturing, rigging and animation; exports FBX, OBJ, GLB and STL.
- [Tripo](https://www.tripo3d.ai/) (Proprietary, Sign Up, Free, Paid): Text- and image-to-3D model generation for games, animation and 3D printing.
- [Hyper3D Rodin](https://hyper3d.ai/) (Proprietary, Sign Up, Free, Paid): High-quality text- and image-to-3D asset generation.
- [Sloyd](https://www.sloyd.ai/) (Proprietary, Sign Up, Free, Paid): Generate and refine 3D models from text or images.
- [Kaedim](https://www.kaedim3d.com/) (Proprietary, Paid): AI-assisted 3D asset production service for studios.
- [Hunyuan3D 2.1](https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1) (Open Weights, Tencent Hunyuan Community License, Free): Tencent's image-to-3D model with PBR texture generation. See also [Hunyuan3D 2.0](https://github.com/Tencent-Hunyuan/Hunyuan3D-2).
- [TRELLIS.2](https://github.com/microsoft/TRELLIS.2) (Open Source, MIT, Free): Microsoft's image-to-3D generation model, successor to [TRELLIS](https://github.com/microsoft/TRELLIS).
- [TripoSR](https://github.com/VAST-AI-Research/TripoSR) (Open Source, MIT, Free): Fast single-image 3D reconstruction.

## 2D Sprites & Pixel Art 👾

➡️ When you want **sprites, sprite sheets and pixel art animations**.

- [PixelLab](https://www.pixellab.ai/) (Proprietary, Sign Up, Free, Paid): Pixel art character, animation, sprite sheet and environment generator; works in the browser or as an Aseprite plugin.
- [Retro Diffusion](https://retrodiffusion.ai/) (Proprietary, Sign Up, Free credits, Paid): Pixel art generation designed by pixel artists, for sprites, characters and animations.
- [God Mode AI](https://www.godmodeai.co/) (Proprietary, Sign Up, Paid): Sprite and looping animation generator for games with multiple camera views.
- [SpriteCook](https://www.spritecook.ai) (Proprietary, Sign Up, Free): Generate and animate pixel art sprites from text prompts; includes an MCP server so AI agents can generate pixel art for you.
- [FrameSprite](https://www.framesprite.com/character) (Proprietary, Sign Up, Paid; free browser tools): Generate or upload a 2D character, create short AI action animations, remove solid-color backgrounds, and export PNG sequences, GIFs, or sprite sheets.

## Texture Generation 🖼️🖌️

➡️ When you want to **generate textures for your assets**

- [DreamTextures](https://github.com/carson-katri/dream-textures) (Open Source, GPL-3.0, Free): Blender add-on to create textures with a **simple text prompt**.
- [Adobe Substance 3D Sampler](https://www.adobe.com/products/substance3d/apps/sampler.html) (Proprietary, Paid): Turn photos into tileable PBR materials with AI-powered image-to-material.
- [Stable Diffusion 3.5](https://huggingface.co/stabilityai/stable-diffusion-3.5-large) (Open Weights, Stability AI Community License, Free)

## Image Generation 🖼️🪄

➡️ When you want to create concept art, portraits of characters, or pictures of suspects in a detective game.

- [Midjourney](https://www.midjourney.com/home/) (Proprietary, Sign Up, Paid)
- [Stable Diffusion 3.5](https://huggingface.co/stabilityai/stable-diffusion-3.5-large) (Open Weights, Stability AI Community License, Free)
- [FLUX](https://github.com/black-forest-labs/flux) (Open Weights, Free; license varies by model): Black Forest Labs' image generation and editing models.
- [ComfyUI](https://github.com/Comfy-Org/ComfyUI) (Open Source, GPL-3.0, Free): Node-based interface for running and chaining local image, video, audio and 3D models.
- [Leonardo AI](https://app.leonardo.ai/) (Proprietary, Sign Up, Paid, Free Limited daily generations)
- [Krea](https://www.krea.ai/) (Proprietary, Sign Up, Free, Paid): Real-time image generation, editing and upscaling.

## World & Level Generation 🌍

➡️ When you want to **generate environments, skyboxes, or whole explorable worlds**.

- [Prometheanai](https://www.prometheanai.com/) (Proprietary, Sign Up, Freemium): AI assistant for teams building virtual 3D worlds.
- [Marble by World Labs](https://marble.worldlabs.ai/) (Proprietary, Sign Up, Free, Paid): Generate and edit persistent 3D worlds from text, images or video.
- [HunyuanWorld 1.0](https://github.com/Tencent-Hunyuan/HunyuanWorld-1.0) (Open Weights, Tencent Hunyuan Community License, Free): Generate explorable 3D worlds from text or images.
- [Skybox AI](https://www.blockadelabs.com/) (Proprietary, Sign Up, Free, Paid): Generate 360° skyboxes and environments from text prompts.

## Code Generation/Assistant 👩‍💻

➡️ When you want **help in coding a function or there’s a bug in your code** and you want to know why.

- [ChatGPT](https://chatgpt.com/) (Proprietary, Free, Paid, Sign Up)
- [Copilot](https://github.com/features/copilot) (Proprietary, Free, Paid, Sign Up)
- [Cursor](https://cursor.com/) (Proprietary, Free, Paid, Sign Up): AI code editor with agent mode, works well with Unity C#, Godot and C++ projects.
- [Claude Code](https://claude.com/product/claude-code) (Proprietary, Paid, Sign Up): Terminal-based coding agent that can work across a whole game codebase.
- [Unity AI](https://unity.com/features/ai) (Proprietary, Paid, Sign Up): Unity's agentic assistant inside the Editor, plus a CLI, MCP server and official plugins.
- [Bezi](https://www.bezi.com/) (Proprietary, Sign Up, Free, Paid): AI assistant for Unity and Unreal Engine that understands your project for debugging, code generation, shaders and prototyping.
- [Aura](https://www.tryaura.dev/) (Proprietary, Sign Up, Free trial, Paid): Agentic AI for Unreal Engine and Unity that builds features, playtests them and finds bugs.
- [Ludus AI](https://ludusengine.com/) (Proprietary, Sign Up, Free, Paid): Unreal Engine toolkit that generates C++, Blueprints, scenes and answers UE5 questions.
- [Coplay](https://coplay.dev) (Proprietary, Free, Paid, Sign Up): Native AI assistant for Unity development.
- [GameDev Assistant](https://gamedevassistant.com/) (Proprietary, Sign Up, Paid): AI coding assistant for Godot by Zenva that knows your project.
- [Godot AI Assistant Hub](https://github.com/FlamxGames/godot-ai-assistant-hub) (Open Source, MIT, Free): Godot plugin to chat with local or remote LLMs (Ollama and others) inside the editor.
- [Roblox GUI Maker](https://robloxguimaker.dev/) (Proprietary, Free): Generate Roblox Studio GUI layouts and Lua starter code for menus, HUDs, shops, and inventory screens from a text prompt.

## Engine Integrations & MCP Servers 🔌

➡️ When you want **AI agents (Claude, Cursor, Copilot, etc.) to directly control your engine or DCC tool** through the [Model Context Protocol](https://modelcontextprotocol.io/).

- [Unity-MCP](https://github.com/IvanMurzak/Unity-MCP) (Open Source, Apache-2.0, Free): MCP server connecting AI agents (Claude, Cursor, GitHub Copilot, Gemini, and more) to the Unity Editor and runtime, with 100+ built-in tools.
- [MCP Unity](https://github.com/CoderGamester/mcp-unity) (Open Source, MIT, Free): MCP server that lets AI agents manipulate scenes, GameObjects and tests in the Unity Editor.
- [Godot-MCP](https://github.com/IvanMurzak/Godot-MCP) (Open Source, Apache-2.0, Free): MCP server connecting AI agents to the Godot Editor and runtime (Godot 4.x, C#).
- [Coding-Solo godot-mcp](https://github.com/Coding-Solo/godot-mcp) (Open Source, MIT, Free): MCP server to launch the Godot editor, run projects and read debug output from AI assistants.
- [Unreal-MCP](https://github.com/IvanMurzak/Unreal-MCP) (Open Source, Apache-2.0, Free): MCP server connecting AI agents to Unreal Engine 5.7, editor and runtime (C++ plugin + .NET sidecar).
- [Blender MCP](https://github.com/ahujasid/mcp-for-blender) (Open Source, MIT, Free): Connect Claude and other agents to Blender for prompt-assisted 3D modeling and scene creation.

## Animation Video Mocap 💃📹

➡️ You want to **generate 3D animations from a video you’ve made without a motion capture suit**, or from a text prompt.

- [Move AI](https://move.ai/) (Proprietary, Free, Paid, Sign Up): Markerless motion capture from video, from a single phone up to multi-camera setups.
- [Rokoko Vision](https://www.rokoko.com/products/vision) (Proprietary, Free, Paid, Sign Up): Free AI motion capture from webcam or video.
- [DeepMotion](https://www.deepmotion.com/) (Proprietary, Free, Paid, Sign Up): Animate 3D turns video into 3D animation; SayMotion generates animation from text.
- [Cascadeur](https://cascadeur.com/) (Proprietary, Free, Paid): Physics-based keyframe animation software with AI-assisted posing, motion generation and mocap cleanup.
- [Uthana](https://uthana.com/) (Proprietary, Sign Up, Free, Paid): Generate 3D human motion from text or video and retarget it across characters.
- [Autodesk Flow Studio](https://www.autodesk.com/products/flow-studio) (Proprietary, Sign Up, Free, Paid): Formerly Wonder Studio; AI that extracts motion from live-action video and puts CG characters in the shot.
- [Mixamo](https://www.mixamo.com/) (Proprietary, Free, Sign Up): Automatic character rigging and a large free animation library.

## Voice Generation 🗣️

➡️ You want to create **voice dialogues in my game using AI actors**.
➡️ [How does it work](https://huggingface.co/tasks/text-to-speech)

- [ElevenLabs](https://elevenlabs.io/) (Proprietary, Sign Up, Free, Paid): Expressive text-to-speech, voice design and voice cloning in many languages.
- [Inworld TTS](https://inworld.ai/tts) (Proprietary, Sign Up, Paid): Low-latency realtime text-to-speech with voice cloning and voice design.
- [Fish Audio](https://fish.audio/) (Proprietary, Sign Up, Free, Paid): Text-to-speech and voice cloning with emotion control.
- [Chatterbox](https://github.com/resemble-ai/chatterbox) (Open Source, MIT, Free): Resemble AI's open TTS with zero-shot voice cloning and emotion exaggeration control.
- [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) (Open Weights, Apache 2, Free): Tiny, fast TTS model, light enough to run locally alongside a game.
- [F5-TTS](https://github.com/SWivid/F5-TTS) (Open Source, MIT code, Free): Zero-shot voice cloning TTS.
- [Coqui TTS](https://github.com/idiap/coqui-ai-TTS) (Open Source, MPL-2.0, Free): Maintained fork of the Coqui TTS toolkit (XTTS and other models).

## Music & Sound Effects 🎵

➡️ You want **background music, jingles, or sound effects** for your game.

- [Suno](https://suno.com/) (Proprietary, Sign Up, Free, Paid): Generate full songs and instrumentals from text prompts.
- [ElevenLabs Sound Effects](https://elevenlabs.io/sound-effects) (Proprietary, Sign Up, Free, Paid): Generate sound effects from text descriptions.
- [Stable Audio Open](https://huggingface.co/stabilityai/stable-audio-open-1.0) (Open Weights, Stability AI Community License, Free): Generate short sound effects, loops and ambience from text.
- [AudioCraft](https://github.com/facebookresearch/audiocraft) (Open Source, MIT code, Free): Meta's MusicGen and AudioGen for local music and sound generation.
- [ACE-Step](https://github.com/ace-step/ACE-Step) (Open Source, Apache 2, Free): Open-source music generation foundation model.
- [MMAudio](https://github.com/hkchengrex/MMAudio) (Open Source, MIT, Free): Generate synchronized audio and Foley for video clips (handy for trailers and cutscenes).

## Speech Recognition 💬

➡️ You want the player to be able to give orders using his voice.
➡️ [How does it work](https://huggingface.co/tasks/automatic-speech-recognition)

- [OpenAI Whisper](https://github.com/openai/whisper) (Open Source, MIT, Free): model for automatic speech recognition (ASR) and speech translation.
- [whisper.cpp](https://github.com/ggml-org/whisper.cpp) (Open Source, MIT, Free): Fast C/C++ port of Whisper that runs on CPU, GPU, mobile and the web.
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper) (Open Source, MIT, Free): Faster Whisper inference with CTranslate2.
- [whisper.unity](https://github.com/Macoron/whisper.unity) (Open Source, MIT, Free): Run Whisper locally inside Unity.

## Conversational models

➡️ You want your NPC to be able to have conversations with the player.
➡️ [How does it work](https://huggingface.co/tasks/text-generation)

- [ChatGPT](https://chatgpt.com/) (Proprietary, Free, Paid, Sign Up): Conversational model for chat-based interactions.
- [HuggingChat 🤗](https://huggingface.co/chat/) (Open Source, Sign Up, Free credits, Paid): Hugging Face's chat app that routes prompts across 100+ open models.
- [Ollama](https://ollama.com/) (Open Source, MIT, Free): Run open models (Llama, Qwen, Gemma, Mistral, etc.) locally with a simple API.

## Story Telling Models

➡️ Want to make that crazy lore for your world with a lot of text?

- [Claude](https://claude.ai/) (Proprietary, Free, Paid, Sign Up): Long-context assistant well suited to lore bibles, quest writing and dialogue drafts.
- [Gemini](https://gemini.google.com/) (Proprietary, Free, Paid, Sign Up): Very long context window for working with entire design docs and scripts.
- [OpenAI API models](https://platform.openai.com/docs/models) (Proprietary, Paid, API access)

## Game Design & Prompt-to-Game 🎮

➡️ You want to generate game mechanics, game ideas, or other components of your game (characters, story, items, etc.), or go from a prompt to a playable prototype.

- [Ludo.ai](https://ludo.ai/) (Proprietary, Sign Up, Free, Paid): Game Ideator that generates game concepts from keywords, themes or existing titles, plus an AI game design document editor that embeds generated assets in the doc.
- [Rosebud AI](https://rosebud.ai/) (Proprietary, Sign Up, Free): Create via prompt to game. Then publish and share your 2D or 3D game via url (host for free).
- [OhMyGame](https://www.ohmygame.ai/) (Open Source, Apache-2.0, Free app, Bring Your Own Model): Desktop game studio where an AI agent drafts design documents, generates assets, writes code, playtests, and publishes games. Model-provider usage may incur separate costs.
- [Summoned Games](https://summoned.games) (Proprietary, Sign Up, Free): Prompt to game through your own coding agent (Claude Code, Codex, any MCP client). The platform hosts the result with leaderboards, save data and up to 16 player multiplayer, and publishes it as a browser game anyone can play without an account.
- [Seele AI](https://seeles.ai/) (Proprietary, Sign Up, Free): Chat to create 3D and 2D games and assets with no coding, then publish them.
- [OmGithub](https://omgithub.com/) (Sign Up via GitHub): Prompt to game: describe a game and it generates the project, builds and runs it in a cloud runner and publishes it, then you keep changing it by chat. Also a gallery of open-source AI-made browser games with their GitHub source.

## AI NPC

➡️ You want **NPCs that talk, remember and act**, in the cloud or running locally on the player's machine.

- [Convai](https://convai.com/) (Proprietary, Sign Up, Free, Paid): Conversational AI characters with voice, actions and Unity/Unreal plugins.
- [Inworld](https://inworld.ai) (Proprietary, Sign Up, Paid): Realtime voice and conversational AI for interactive characters and apps.
- [Player2](https://player2.game/) (Proprietary, Free): Free AI APIs for building AI NPCs in games and mods, no API keys needed.
- [NVIDIA ACE](https://developer.nvidia.com/ace-for-games) (Proprietary, Free SDKs): Suite of on-device and cloud models for speech, intelligence and facial animation of digital humans.
- [NobodyWho](https://github.com/nobodywho-ooo/nobodywho) (Open Source, EUPL-1.2, Free): Run local LLMs on-device for NPC dialogue directly in your game — bindings for Godot, Flutter, React Native and Swift, with streaming, tool calling, structured output, plus built-in Whisper speech-to-text and text-to-speech. No API keys, no server.
- [LLMUnity](https://github.com/undreamai/LLMUnity) (Open Source, Apache 2, Free): Run LLMs locally inside Unity for AI characters, with RAG support.
- [llama.cpp](https://github.com/ggml-org/llama.cpp) (Open Source, MIT, Free): The C/C++ LLM inference engine behind most local, in-game LLM integrations.

## Playtesting & QA 🧪

➡️ You want **AI agents to play, test, and break your game** before players do.

- [nunu.ai](https://nunu.ai/) (Proprietary, Paid): AI agents that test games like a human player across real iOS, Android and PC devices.
- [modl.ai](https://modl.ai/) (Proprietary, Paid): AI agents for automated game testing and QA, finding bugs and performance issues.
- [Unity ML-Agents](https://github.com/Unity-Technologies/ml-agents) (Open Source, Free): Train game-playing agents with reinforcement and imitation learning for testing, balancing or NPC behavior.

## Showcases & Galleries

➡️ You want to **see what people are making with AI**: playable AI-made games for inspiration and benchmarking.

- [LOL Games](https://lolgames.net/) (Free, No Sign Up): Swipe through hundreds of free browser games and play them instantly, with no downloads. Most games are tagged with the AI model that made them (Claude, GPT, Gemini) and link to their source.

## Python Libraries

- [NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails) (Open Source, Apache 2, Free): Limit what a NPC could talk about
- [Guidance](https://github.com/guidance-ai/guidance) (Open Source, MIT, Free): A library to help your LLM to understand your prompts

## C# Libraries

- [Python.Net](https://github.com/pythonnet/pythonnet) (Open Source, MIT): Integrate Python libraries with .Net and .Net Libraries with Python

## Contributing

Contributions are welcome! Please open a pull request at **[aigamedevs/awesome-ai-tools-for-game-dev](https://github.com/aigamedevs/awesome-ai-tools-for-game-dev/pulls)**.

- Add **one tool per line** in the most relevant category, using the existing format: `- [Name](link) (License/Pricing, Sign Up?): One-line description.`
- The tool must be **live, relevant to game development**, and usable today (no waitlists, dead links, or unreleased products).
- Keep descriptions short, factual and free of marketing speak. Disclose if you're the maker.
- No duplicates, affiliate or tracking links, crypto/token tools, or general-purpose SaaS unrelated to making games.

## Credits

Originally created by [Thomas Simonini](https://github.com/simoninithomas) ([upstream repo](https://github.com/simoninithomas/awesome-ai-tools-for-game-dev)). Thanks to everyone who contributed to the original list and to the upstream PR authors whose additions were merged here. Refreshed and maintained by [aigamedevs](https://github.com/aigamedevs).

## License

[CC0 1.0 Universal](LICENSE): to the extent possible under law, the authors have waived all copyright and related rights to this work.
