# <img src="engineering/assets/dantetl.png" width="40" height="40" align="absmiddle" alt=""> DanteTL

DanteTL translates on-screen game text in a click-through Windows overlay. It reads Japanese
and 34 Latin-script languages on your PC. Choose from 19 output languages, depending on your
translator.

![English translations over the menu labels and profile text on Saber's character screen in Honkai: Star Rail](engineering/assets/hsr_dantetl.png)

## Get started on Windows

1. Extract the entire `DanteTL-windows-x64.zip` and open `DanteTL.exe`. Keep the `_internal`
   folder beside it. The ZIP includes text recognition (OCR) and runs without a separate Python
   installation. [GitHub releases](https://github.com/nhmelo/dantejp/releases)
2. In the **Setup assistant**, choose **Next** to pick your models. You can combine choices across tabs.
   - **Local models** starts with the recommended translator selected. Choose **None** to skip the local translator. You can review acceleration and download size before starting.
   - Under **Ollama API**, connect to your server. Use the default address for this PC or enter
     your server’s HTTP or HTTPS address. Click **Find models**, check the models you want in
     the translation picker. The same controls are available directly in **Settings → Models → Ollama API**.
   - Under **Cloud models**, sign in with an eligible ChatGPT account or enter an
     OpenAI, Gemini, DeepSeek or Claude API key and choose a model. To configure several, save each additional profile in the tab. Cloud requests can consume
     plan allowance or incur API charges.
   - Choose **Next** to apply your selections. With **None** selected locally, a compatible NVIDIA PC can still opt into CUDA for text recognition. The guide reviews the runtime and any missing OCR files before downloading. If OCR is ready and no runtime is needed, setup finishes here.
3. Run the game in windowed or borderless fullscreen mode. In DanteTL, select the game window.
   Under **Translation**, choose your model, **Game text language** and **Output language**.
   Click **Start capture**, then return to the game.

Screenshots stay on your PC. With Ollama or cloud translation, the selected server or provider receives recognized
text and, when available, a game-name hint and recent dialogue for context.

## Model recommendations

| Local model | Download | When to choose it |
| --- | ---: | --- |
| **Gemma 4 E2B** | 3.35 GB | Start here for a balance of speed and accurate game terminology. |
| Gemma 4 E4B | 5.15 GB | Good for game terminology if you have more memory available. |
| PLaMo 3 Translate 2B | 1.81 GB | Fast for dialogue. Mixed results for stats and game terms. |
| PLaMo 3 Translate 0.8B | 0.57 GB | Smallest download. Fast, with weaker phrasing and mixed results for game terms. |
| Qwen3.5 4B | 2.74 GB | An alternative if you dislike Gemma’s wording. Slower in DanteTL’s tests. |

| Cloud provider | Recommended model |
| --- | --- |
| ChatGPT / OpenAI | [GPT-6 Luna](https://developers.openai.com/api/docs/models/gpt-6-luna) |
| Gemini | [Gemini 3.5 Flash-Lite](https://aistudio.google.com/docs/models/gemini-3.5-flash-lite) |
| DeepSeek | [DeepSeek Flash](https://api-docs.deepseek.com/quick_start/pricing/) |
| Claude | [Claude Haiku 5.5](https://platform.claude.com/docs/en/models/haiku-5-5/overview) |

Use **Refresh models** in the cloud model editor to see which models your account can access.

## During play

| Default shortcut | Action |
| --- | --- |
| **Ctrl+Alt+F8** | Hide or show the overlay. Translation continues while hidden. |
| **Ctrl+Alt+F9** | Start capture on the focused window, or stop the current capture. |

Change shortcuts in **Settings → Hotkeys**. To compare a translation with the recognized text,
enable **Settings → Experimental → Inspection and diagnostics**, then expand the section in
the main window. To record the overlay, enable **Include in
screen capture** and record the entire display.

Manage translators in **Settings → Models**. For GPU acceleration, open **Settings →
Acceleration**. NVIDIA CUDA can accelerate recognition and translation. Vulkan accelerates
supported local translators and keeps OCR on CPU.

## Updates and recovery

The portable app checks GitHub for a stable release at startup. Choose **Yes** to download,
verify, and restart into an update. **Ask me later** reminds you after a week. **No** skips
that release. Use the **About** ⓘ button beside Settings to check again or update a skipped version.
You can also close DanteTL and extract a release ZIP into a fresh folder. The standalone app
reuses your models and settings in `%LOCALAPPDATA%\DanteTL`. If a GPU runtime fails to start, launch
`DanteTL.exe --cpu`.

## Run from source

On Windows x64, install Visual Studio C++ Build Tools and either uv or Python 3.12+.
Open `Run DanteTL.cmd` to set up the environment and launch the app. Use the Setup assistant
to download OCR files for your game text language.

For development, testing and packaging, see the [engineering guide](engineering/README.md).

## License

Copyright 2026 Nuno Melo. DanteTL's original code is licensed under the
[Apache License, Version 2.0](LICENSE). Forks and pull requests are welcome.
Third-party libraries, models, and assets retain their own terms.
See the [third-party notices](packaging/THIRD-PARTY.txt) for bundled components.
