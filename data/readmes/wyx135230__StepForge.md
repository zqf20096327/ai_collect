<p align="center">
  <img src="docs/branding/stepforge-icon.png" width="96" alt="StepForge logo">
</p>

<h1 align="center">StepForge</h1>

<p align="center"><strong>English</strong> · <a href="README.zh-CN.md">简体中文</a></p>

**Capture your workflow. Turn it into an editable, shareable step-by-step guide.**

StepForge is a local-first workflow documentation tool for Windows. Record desktop or browser actions, save steps and screenshots, edit instructions and annotations, redact sensitive areas, and export documents, interactive HTML, or narrated videos. Use it for software tutorials, onboarding, training materials, handovers, and standard operating procedures (SOPs).

**Windows x64 · .NET 10 / WPF · Local storage · Optional AI · MIT**

[Quick start](#quick-start) · [See it in action](#see-it-in-action) · [User guide (中文)](docs/USAGE.md) · [Contributing](CONTRIBUTING.md) · [Documentation](docs/README.md)

![The StepForge guide editor running with sample content](docs/media/editor.png)

## Quick start

> **The easiest path: download the complete Windows package → extract it → open `StepForge.exe` → Start capture → finish recording → export HTML.**
>
> You do not need to compile the source, install a browser extension, or configure AI to get started. Core recording, editing, and export work offline.

1. Obtain the complete **`StepForge-win-x64.zip`** package and extract it to a permanent folder, such as `D:\Apps\StepForge`.[Download for Windows](https://github.com/wyx135230/StepForge/releases/download/v0.1.0/StepForge-win-x64.zip)
2. Open **`StepForge.exe`** in that folder. Keep the helper programs, runtime files, `speech/`, and other resources alongside it.
3. Click **Start capture**, choose a display or window, and perform the task you want to document.
4. Finish from the recording toolbar or press **Ctrl + Alt + F10** to open the guide editor.
5. Review the text and screenshots, then select **HTML → Export**, or use **Save & read** to save the guide and open it in a browser.

Complete application packages are distributed by the maintainer through repository Releases or another delivery channel. GitHub's **Code → Download ZIP downloads the source**, not a ready-to-run application. If no application package is available, follow [Running from source](#running-from-source).

If you have already generated a release package in a source checkout, **`Start-StepForge.cmd`** at the repository root is the fixed preview launcher.

<details>
<summary>System requirements and installation notes</summary>

- The desktop application targets **Windows 10 / 11 x64**. macOS and Linux are outside the current desktop support scope.
- The complete self-contained package does not require a separately installed .NET SDK. It includes the local narration engine and models.
- The Chrome / Edge extension is optional; install it when you need browser capture and Sidekick.
- AI is optional and requires your own provider configuration and consent. Remote providers require a network connection and may charge for usage.
- MP4 export uses Windows Media Foundation and requires the corresponding Windows media components.
- Do not copy just the main `.exe` or run the application from inside the ZIP archive.

</details>

## See it in action

These assets come from actual StepForge windows and exported files, using dedicated sample content rather than personal data. The theme and display scaling may differ from your setup.

### GIF: playback of an actual export

![GIF preview of an MP4 exported by StepForge](docs/media/export-demo.gif)

This silent GIF previews an actual MP4 export, including content transitions and captions. **It is not a screen recording of mouse interactions.**

### Video: the original MP4 with audio

[![Open the video exported by StepForge](docs/media/export-poster.png)](docs/media/export-demo.mp4)

**[Watch or download the MP4 sample (about 11 seconds, 567 KiB)](docs/media/export-demo.mp4)**. This is an actual H.264 / AAC export. GIFs have no audio; use the MP4 for the complete output. If GitHub does not play it inline, download it from the file page.

### More application views

| Capture panel | Screenshot editor |
| --- | --- |
| ![The StepForge capture panel](docs/media/recorder.png) | ![The StepForge screenshot editor](docs/media/image-editor.png) |

| Pages handbook | HTML reading and sharing |
| --- | --- |
| ![The StepForge Pages editor](docs/media/pages.png) | ![The exported HTML reader](docs/media/reader.png) |

See [Media sources](docs/media/README.md) for provenance, processing details, and reuse notes.

## Features

| Feature | What it does |
| --- | --- |
| Desktop capture | Records actions such as clicks, saves their screenshots and local step drafts, and supports pause, resume, finish, and additional capture |
| Browser capture and Sidekick | Captures browser workflows through the Chrome / Edge extension; searches and reads local guides in the side panel |
| Guide editing | Edits instructions, reorders or duplicates steps, merges screenshot groups, and adds notes and rich content blocks |
| Screenshot tools | Crops, scales, annotates with arrows, shapes, text, and click markers, and permanently redacts sensitive areas |
| AI-generated instructions | Uses your DeepSeek Flash or compatible provider, action facts, and optional screenshots to generate wording; supports manual edits and restoring AI changes |
| Pages handbooks | Combines guides, nested Pages, notes, tables, images, and a table of contents into maintainable documentation |
| Local library | Searches saved visible content, organizes guides, and imports or exports `.stepforge` projects |
| Import and branding | Imports DOCX / text-based PDFs as Pages and applies local logos, colors, fonts, and layout templates |
| Local narration and movies | Generates Chinese or English narration and exports captioned HTML Movies or offline MP4 files |

Core features do not require a StepForge account or depend on Scribe services. Team accounts and cloud collaboration are outside the current local feature scope; planned UI entries do not imply an available online service.

## Your first guide

### 1. Capture

Choose a display or window from **Start capture**. Perform your task normally, using the floating toolbar or system tray to pause and resume.

| Default shortcut | Action |
| --- | --- |
| `Ctrl + Alt + F9` | Start / pause / resume |
| `Ctrl + Alt + F10` | Finish recording |
| `Ctrl + Alt + F8` | Take a manual screenshot |

Shortcuts can be changed in Settings. Start with automatic screenshots; see [Feature status](docs/feature-status.md) for known issues, including manual screenshot behavior.

### 2. Edit

Review each step's **Instructions** and screenshot, adjust the order, and add any missing explanation. Use **Edit screenshot / redact** for annotations and privacy edits, then **Save and return**.

### 3. Share

For your first export, choose **HTML**: recipients can open a single file in their browser without installing StepForge. Choose a **`.stepforge` project** when the recipient needs to continue editing in StepForge.

The [User guide (中文)](docs/USAGE.md) covers the full workflow, Pages, imports, narration, and troubleshooting.

## Optional: generate richer instructions with AI

Without AI, StepForge still creates local step drafts. To generate more detailed descriptions:

1. Open **Settings → AI provider** and choose DeepSeek or a custom compatible endpoint.
2. Enter the base URL, model, and your own API key. The new DeepSeek preset uses **`deepseek-flash`**.
3. Read and accept the text-sharing consent, then enable automatic initial step wording.
4. For visual assistance, **separately enable click screenshot consent**, allowing the event images and their visible content to be sent to the configured model.
5. Choose **Save settings**, then start a new recording.

On desktop, finishing a recording displays **Finishing guide wording** and waits for the current wording work before opening the guide. Choose **Skip and open guide** if you need to edit immediately. Persistent provider failures leave the local text in place for a later retry. Browser Finish saves first; wording continues asynchronously in the current host session.

AI wording is applied automatically and can be inaccurate. Review it before sharing. You can edit it manually or use **AI wording / restore** to undo applicable AI changes. Restore records belong to the current session and are not a backup history across restarts.

## Choose an export format

| Format | Best for | Recipient needs |
| --- | --- | --- |
| **HTML** | Default sharing; Scroll / Slides reading and Movie playback with saved narration | A browser |
| **MP4** | Training, presentations, and video platforms; optional captions and valid saved narration | A video player |
| **PDF** | Fixed layouts, archiving, and printing; searchable and selectable body text | A PDF reader |
| **DOCX** | Further formatting in Word or another word processor | Compatible document software |
| **Markdown ZIP** | Documentation sites, knowledge bases, and version control | Markdown tools |
| **Image ZIP** | Reusing edited step images | An image viewer |
| **`.stepforge`** | Continuing work in StepForge on another computer | StepForge |

PDF export does not automatically OCR text inside screenshots. MP4 uses valid saved narration; it does not silently call AI or generate missing narration during export. See [Export and sharing (中文)](docs/USAGE.md#导出与分享) for details.

## Data and privacy

- The default library is `%LOCALAPPDATA%\StepForge\Library`; settings are stored under `%LOCALAPPDATA%\StepForge`. You can select another library in Settings.
- Without remote AI, core recording, editing, export, and local narration run on your computer. Initial downloads of source dependencies or models require network access.
- Text and screenshot sharing have separate AI consent controls. Images may contain visible account or business information; review your chosen provider's data handling before enabling remote processing.
- API keys are protected with Windows current-user DPAPI and are not included in exported guides or projects.
- **Permanent redaction cannot be undone.** It removes affected original images, recovery history, and generated content such as the current document's narration. Review the text afterward and regenerate narration as needed.
- **Exported HTML, MP4, PDF, and other files are independent copies.** Editing or redacting the library later does not update or revoke files already shared.

## Running from source

You need Windows and PowerShell. Browser extension development and Node tests also require Node.js. The repository uses a private .NET SDK; see [`global.json`](global.json) for the version.

Run from the repository root:

```powershell
# Run once if .tools/dotnet is missing; installs locally without changing global PATH
./scripts/bootstrap.ps1

./scripts/build.ps1 -Configuration Release
./scripts/run.ps1 --configuration Release --no-build
```

A source build differs from the complete application package: local speech models, OCR, and other additional resources need their own preparation steps. A successful build does not automatically create a release under `dist/`. See [CONTRIBUTING.md (中文)](CONTRIBUTING.md) for development and packaging instructions.

## Contributing

**The easiest contributions are improving a tutorial, reporting a reproducible issue, or adding a real screenshot without personal information.** You do not need to understand the entire C# codebase first.

The usual workflow is: **check existing issues → agree on scope → fork and create a branch → make the change and appropriate checks → open a pull request → respond to review**.

Environment setup, module boundaries, branch and commit conventions, checks by change type, PR guidance, and media requirements are documented in the root **[CONTRIBUTING.md (中文)](CONTRIBUTING.md)**, which also serves as GitHub's contribution entry point.

## FAQ

**Do I have to configure or pay for AI?** No. Start with local capture, editing, and HTML export. Remote AI is optional, and your chosen provider may charge for it.

**Why is there no StepForge.exe in the source download?** Source archives do not include `dist/` or build outputs. Obtain a complete application package or follow the source build instructions above.

**Does it support Chinese?** You can edit and export Chinese content and generate Chinese narration. The main application UI is currently English. The [Chinese README](README.zh-CN.md) and [user guide](docs/USAGE.md) retain English button names so you can find them in the application.

**Are there known limitations?** Yes. See [Feature status (中文)](docs/feature-status.md) for browser capture scope, platform boundaries, and known issues, and [Current handoff (中文)](docs/handoff/CURRENT.md) for development status. Report issues with minimal reproduction steps; do not upload private business data.

## Documentation and license

The supporting guides below are currently written in Simplified Chinese.

- [User guide](docs/USAGE.md): from your first guide to Pages, AI, narration, and video.
- [Contributing](CONTRIBUTING.md): how to participate and submit a PR.
- [Documentation index](docs/README.md) · [Architecture](docs/architecture.md) · [Feature status](docs/feature-status.md) · [Roadmap](docs/stepforge-parity-roadmap.md).
- [Media sources](docs/media/README.md) · [More application screenshots](docs/screenshots/README.md).

StepForge project code is licensed under the **[MIT License](LICENSE)**. Fonts, models, speech runtimes, and other dependencies retain their own licenses; see [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md).
