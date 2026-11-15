<p align="center">
  <img src="docs/assets/noda-logo.svg" width="96" alt="Noda logo">
</p>

<h1 align="center">Noda — Local AI Notes for Windows</h1>

<p align="center"><strong>Local AI for your Markdown notes.</strong></p>

<p align="center">Capture an idea. Find its connections. Ask your own library.</p>

<p align="center">Windows x64 · local inference · Markdown files · noncommercial source license</p>

<p align="center"><strong><a href="https://github.com/Timaga/noda-local-ai-notes/releases">Download Windows Setup (x64)</a></strong> · <a href="docs/releases/1.0.2.md">1.0.2 release notes</a> · <a href="docs/USER_GUIDE.md">User guide</a> · <a href="#build-from-source">Build from source</a></p>

![Noda library with projects, a note list and an editable Markdown note](docs/assets/screenshots/library.png)

Noda is a local-first AI note-taking app for Windows that keeps your personal knowledge base in Markdown files. It combines quick capture, a Markdown editor, optional AI titles and tags, a knowledge graph, semantic search and chat with cited source notes.

The app runs note processing and chat on your computer using installed models. Initial setup and model downloads require internet access.

## What you can do

| Task | How Noda helps |
| --- | --- |
| Save a thought while working | Open quick capture with `Ctrl + Shift + Space`, type, and press Enter. The queue saves the source before processing. |
| Keep a readable library | Open formatted Markdown, switch to editing, and choose autosave or manual save. |
| Organize without tagging every sentence | Enable AI titles, existing tags, links, and experimental new topics separately. A note can have no tags or links. |
| Keep different subjects apart | Give each project its own Markdown folder, queue, search index and chat history. |
| Follow a connection | Open saved connections and backlinks below a note or explore them in the graph. |
| Ask a question across your notes | Use local retrieval and chat with clickable source notes and quotations. |

## See your notes in context

![The Noda knowledge graph showing connected and unconnected notes](docs/assets/screenshots/graph.png)

The graph displays saved relationships. Shared names or broad topics alone should not force a connection. AI suggestions remain editable metadata.

![Noda chat answering a question with two cited source notes](docs/assets/screenshots/chat.png)

Chat retrieves note fragments from the current project and includes source links. Check the cited text when accuracy matters; generated answers and metadata can be wrong.

Screenshots use synthetic demo notes in an isolated application profile. The displayed chat answer is demonstration data, not a model evaluation.

## Install on Windows

**[Windows x64 Setup, releases and checksums](https://github.com/Timaga/noda-local-ai-notes/releases)** · [Noda 1.0.2 release notes](docs/releases/1.0.2.md)

1. Download the current version's `Noda-Setup-<version>-x64.exe` and run it.
2. Follow the installation steps, then open **Noda** from the Start menu.
3. Let Noda prepare its local runtime and the models you choose. Initial downloads require internet access.

The Windows build is unsigned while code-signing arrangements are pending. Review [known security issues](docs/security-known-issues.md) before installing.

### Update to a newer version

Back up your projects and app profile, fully exit Noda through its tray menu, then run the new version's **Setup**. Project folders and profile data are kept separately from the installed program. After installation, launch Noda from the Start menu. See [all versions](https://github.com/Timaga/noda-local-ai-notes/releases) to choose a release. Automatic application updates are not included.

### First run

1. Start in English and create a project or connect a Markdown folder. Other interface languages remain available in Settings.
2. Let initial preparation download the semantic-search model (about 1.1 GB), then choose processing models or disable optional AI stages. Setup does not bundle model weights.
3. Create a quick note, watch its queue entry, then open the result in the library.

The base runtime requires Windows 10 or 11 x64 and an AVX2-capable processor. **16 GB RAM is a useful starting point for the recommended local model profile.** Larger models need more resources. Download sizes are shown before model installation; leave additional disk space for the runtime, model weights and temporary downloads.

You can browse, edit and use text search without the semantic search model. Semantic search and note-based chat require their corresponding local models. CPU processing can take minutes; speed depends on the model and the computer.

## Local files, explicit setup

- Notes remain in the project folders you choose, with Markdown content and Noda metadata.
- Windows profile data, including settings and chat history, is kept separately from the project notes.
- The app manages local Python and Qdrant components; models and runtime dependencies are downloaded during setup.
- Noda does not require a hosted model API for its normal local workflow. Model downloads still contact their download providers.
- Project files are not encrypted by Noda. Use your operating system's storage protection and keep backups.

See the [user guide](docs/USER_GUIDE.md) for data locations, project copies and recovery.

## Languages

The interface includes English, Russian, Spanish, French, German, Brazilian Portuguese, Italian, Simplified Chinese, Japanese and Korean. Save a language change and fully restart Noda to apply it. Windows system dialogs follow the Windows language.

The supplied note-processing profiles support **Russian and English**. Changing the interface language does not translate your notes.

## Project status

Current source version: **1.0.2**. The supported workflow uses ready-made local models for note processing, indexing and chat. Fine-tuning is disabled. Source and native checks cover isolated workflows, renderer trust boundaries and installer lifecycle scenarios. Exact-binary clean-machine validation and broader model evaluation remain documented limitations.

See the [compliance and publication status](docs/COMPLIANCE.md) for the reviewed licenses, privacy scope and open release findings.

Useful contributions include reproducible bugs, accessibility improvements, translations and small tests for real workflows. Please use synthetic notes or remove private information before sharing a report.

## Build from source

Developers need Windows x64, Git, Node.js 22.12 or newer within the 22.x line, and npm. Build in PowerShell:

```powershell
git clone https://github.com/Timaga/noda-local-ai-notes.git
cd noda-local-ai-notes
npm --prefix frontend ci
npm --prefix frontend run build
```

The script prints the generated Setup path and does not publish it. See [DEVELOPMENT.md](docs/DEVELOPMENT.md) for tests and [RELEASING.md](docs/RELEASING.md) for preparing another version.

## License and credits

Noda's own code is provided under the [PolyForm Noncommercial License 1.0.0](LICENSE). You may use, study, modify and share it for permitted noncommercial purposes under those terms. Commercial use is not granted by this license.

This is **source-available software with a noncommercial restriction**, rather than an OSI open-source license. Third-party code, runtimes, models and assets retain their own licenses; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

Created by **Tim Buglaev / buglAI**. Support: [tim@buglai.com](mailto:tim@buglai.com). For security reports, follow [SECURITY.md](SECURITY.md).

If Noda is useful to you, a star helps other people discover the project. Reproducible feedback and thoughtful contributions help improve the next release.
