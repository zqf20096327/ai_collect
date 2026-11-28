<div align="center">
  <img src="website/assets/cover-en.png" alt="Ossia: AI-native music notation software">
  <p><strong>AI-native music notation software, built for a great experience.</strong></p>
  <p>
    <a href="https://github.com/micooz/ossia/actions/workflows/check.yml"><img src="https://img.shields.io/github/actions/workflow/status/micooz/ossia/check.yml?branch=main&amp;label=CI&amp;style=flat-square" alt="CI"></a>
    <a href="https://www.rust-lang.org/"><img src="https://img.shields.io/badge/Rust-1.91%2B-b7410e?style=flat-square&amp;logo=rust&amp;logoColor=white" alt="Rust 1.91 or later"></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-GPL--3.0--or--later-111111?style=flat-square" alt="License: GPL-3.0-or-later"></a>
  </p>
  <p>
    <a href="#features">Features</a> | <a href="#use-cases">Use cases</a> | <a href="#quick-start">Quick start</a> | <a href="#tips">Tips</a> | <a href="#qa">Q&amp;A</a> | <a href="#development">Development</a> | <a href="#license">License</a><br>
    English · <a href="README_zh.md">简体中文</a>
  </p>
</div>

Ossia is AI-native music notation software that gives AI agents the tools and guidance they need to create scores through conversation.

> Ossia is open source under [GPL-3.0-or-later](LICENSE). Commercial use, sale, and distribution are subject to the license, including requirements when distributing the software to retain copyright and license notices, provide recipients with corresponding source code, and license modified versions under the GPL. See the [license](LICENSE) and the [GNU GPL FAQ](https://www.gnu.org/licenses/gpl-faq.html) for details.

| Score library                                                                        | Working with an agent                                                                       |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| <img src="docs/readme-assets/library-en.webp" alt="Ossia score library" width="575"> | <img src="docs/readme-assets/agent-session-zh.webp" alt="Agent and score view" width="575"> |

## Features

Ossia connects to popular AI agents (see [Connect an agent](#2-connect-an-agent) for the full list). It also lets you:

- Create scores for piano, guitar, ukulele, violin, ensembles, and more, including numbered notation.
- Import MusicXML, MIDI, PDF, and images of scores, with help from an Ossia OMR service where appropriate.
- Export scores or audio as PDF, PNG, SVG, MusicXML, MIDI, and WAV.
- Annotate individual score elements and draw freely.
- Browse scores on touchscreens.
- Share scores on your local network.

## Use cases

Start with an existing score or a simple idea and work with your agent to arrange or create music for study, teaching, or professional notation.

### Create scores

<img src="docs/readme-assets/case-find-score.webp" alt="Creating a Bach score" width="720">

Create a score for Bach's <em>Sheep May Safely Graze</em>, BWV 208.

<img src="docs/readme-assets/case-import-image.webp" alt="Importing and checking an image of a score" width="720">

Import this score image, check it carefully against the original, and correct any errors.

<img src="docs/readme-assets/case-import-pdf.webp" alt="Agent transcribing and checking a PDF score in Ossia" width="720">

Ask an agent to transcribe a PDF score without online OMR, then check and refine the result against the original.

### Arrange scores

<img src="docs/readme-assets/case-arrange.webp" alt="Arranging a score for piano four hands" width="720">

Arrange <em>Sheep May Safely Graze</em> for piano four hands and save it as a new score.

<img src="docs/readme-assets/case-guitar-tab.webp" alt="Arranging guitar tablature with chord diagrams" width="720">

Arrange <em>Hollow Knight</em> as a new guitar tablature score and add chord diagrams.

<img src="docs/readme-assets/case-jianpu.webp" alt="Bach’s Prelude in C major in numbered notation" width="720">

Convert Bach’s Prelude in C major, BWV 846, to numbered notation as a new score.

### Compose music

<img src="docs/readme-assets/case-compose.webp" alt="Composing a melody with harmony and accompaniment" width="720">

Write a beautiful melody, add harmony, and create an accompaniment part.

<img src="docs/readme-assets/case-original-piano.webp" alt="Creating and refining an original piano piece with an agent" width="720">

Create a 16-bar original piano piece, then refine its melody and dynamics through conversation.

### Study scores

<img src="docs/readme-assets/case-transpose.webp" alt="Analyzing the key and transposing a score" width="720">

What key is <em>Hollow Knight</em> in? Transpose it to A minor.

<img src="docs/readme-assets/case-harmony-analysis.webp" alt="Analyzing and marking harmony in Bach’s Prelude in C major" width="720">

Analyze and mark the harmony in Bach’s Prelude in C major, BWV 846.

> AI can make mistakes. Review the result carefully and refine it through follow-up requests.

## Quick start

### 1. Install Ossia

> ⚠️ Current installers are unsigned and the macOS app is not notarized. macOS and Windows may block installation. Download from a trusted source and follow the platform instructions to allow installation; this is only needed the first time.

Download an installer for macOS (Apple Silicon or Intel) or Windows x64 from [Releases](https://github.com/micooz/ossia/releases).

### 2. Connect an agent

1. Open Ossia and check that the service is running in the upper-right corner. Start it if necessary.
2. Under **Integrations → Agent**, click the button to connect Ossia to your agent.

<img src="docs/readme-assets/agent-en.webp" alt="Agent integration panel" width="720">

Ossia currently supports:

- Codex
- DeepSeek Harness
- Antigravity
- Antigravity CLI
- Claude Code
- Claude Desktop
- WorkBuddy
- Pi

### 3. Create, import, or edit a score

Start a new agent conversation and begin your task with `$ossia` or `/ossia`. We recommend using it once in each new conversation. For example:

```text
/ossia Create an eight-measure piano exercise in C major for a beginner.
/ossia Create Bach's Prelude in C major.
/ossia Import this MusicXML score and open it for me to review.
```

> Open the score using the agent's link or from your Ossia library.

<img src="docs/readme-assets/create-score-zh.webp" alt="Creating a score with an agent" width="720">

### 4. View the score

On the score page, you can switch scores, restore versions, play music, annotate, draw, export, and adjust score settings.

<img src="docs/readme-assets/score-zh.webp" alt="Score page and drawing tools" width="720">

### 5. Export the score

Ossia supports several export formats, each with its own options.

<img src="docs/readme-assets/export-en.webp" alt="Score export panel" width="720">

## Tips

### Local data

Ossia stores your score library, imported originals, and version history locally. You can open the data directory from the management window. The default locations are:

- macOS: `~/.ossia` (that is, `/Users/<username>/.ossia`)
- Windows: `%USERPROFILE%\.ossia` (usually `C:\Users\<username>\.ossia`)

### Updates

Under **Settings → About**, you can enable automatic update downloads and choose an update source for your network:

- **Ossia**: optimized for mainland China.
- **GitHub**: available globally.

### Other tips

- Use keyboard shortcuts on the desktop score page to work faster.
- Annotations and drawings sync in real time to other devices viewing the same score.
- You can also export a score through your agent conversation.
- Closing the main window normally leaves Ossia running in the system tray. Choose **Quit Ossia** from the tray to stop it completely. The agent integration is unavailable while Ossia is stopped.

## Q&A

### Can Ossia import scores from PDFs or images?

Yes. You can configure an optical music recognition (OMR) service under **Settings → General → Score recognition service (OMR)** to help convert PDFs or images into scores.

OMR is optional. Without it, your agent may still be able to recognize a score when using a capable model.

> To run your own service, see the [Ossia OMR self-hosting guide](packages/ossia-omr/deploy/README.md).

### Can Ossia transcribe audio?

Ossia does not have built-in audio transcription, but your agent may be able to help. Try asking:

> /ossia Import audio.mp3 as a score.

### Why didn't my agent produce the result I expected?

Ossia has been tested and optimized for common requests, but an agent may take a longer path or be unable to complete a task in a scenario that has not been tested.

Try a more capable model, or open an issue describing your use case so we can improve it.

## Development

From the repository root:

```sh
# Install dependencies and download the LilyPond engine and documentation.
pnpm setup

# Start the desktop app.
pnpm dev:desktop
```

- The development app uses the repository's `.ossia` directory, separate from the release app.
- Run `pnpm check`, `cargo test`, and `pnpm test:ui` for the relevant checks.

## Acknowledgments

Ossia is made possible by open-source software and its community. Thanks to these projects and their contributors:

| Project                                                      | Use                                      | License                                                                                                                                                 |
| ------------------------------------------------------------ | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [LilyPond](https://lilypond.org/)                            | Music engraving and format conversion    | The main program is [GPL-3.0-or-later](https://github.com/lilypond/lilypond/blob/master/LICENSE); documentation, fonts, and some files have other terms |
| [Rust](https://www.rust-lang.org/)                           | Core application and backend development | Primarily [MIT and Apache-2.0](https://github.com/rust-lang/rust#license); some components use other licenses                                           |
| [Tauri](https://tauri.app/)                                  | Desktop application framework            | [MIT or Apache-2.0](https://github.com/tauri-apps/tauri/blob/dev/ARCHITECTURE.md#license)                                                               |
| [React](https://react.dev/)                                  | User interface                           | [MIT](https://github.com/facebook/react/blob/main/LICENSE)                                                                                              |
| [Vite](https://vite.dev/)                                    | Frontend build tool                      | [MIT](https://github.com/vitejs/vite/blob/main/LICENSE)                                                                                                 |
| [SQLite](https://sqlite.org/)                                | Local score library                      | [Public domain](https://sqlite.org/copyright.html)                                                                                                      |
| [resvg](https://github.com/linebender/resvg)                 | SVG rendering                            | MIT or Apache-2.0                                                                                                                                       |
| [libimagequant](https://github.com/ImageOptim/libimagequant) | PNG image quantization                   | GPL-3.0-or-later                                                                                                                                        |

- These are major projects, not a complete list.
- The installer includes `THIRD-PARTY-NOTICES.md` and `licenses/` with further dependency and license information.
- Audio sample sources and licenses are listed in the [sample manifest](packages/ui/public/audio/manifest.json).

## License

Ossia is licensed under the [GNU General Public License v3.0 or later](LICENSE).
