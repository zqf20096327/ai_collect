<p align="center">
  <img src="docs/assets/readme/NppAIAssistant-2026-09-30-hero.png" alt="A fox editing companion surrounded by floating pages in a moonlit workspace" width="100%">
</p>

# NppAIAssistant

**AI assistance beside your text. Visible prompts. Deliberate edits.**

A native Notepad++ plugin that helps explain code, rewrite text, and organize drafts. Choose a cloud AI service or connect to a local model.

[Windows downloads & installation](DOWNLOADS.md)

[繁體中文](README_zh-TW.md) · [Download](https://github.com/pingqLIN/NppAIAssistant/releases/latest) · [Report an issue](https://github.com/pingqLIN/NppAIAssistant/issues) · [GPL-3.0](LICENSE)

> **Version guide:** the current GitHub x64 release is **0.2.0.6** (`v0.2.0.6`). The official Notepad++ Plugin List x64 entry has also been updated to **0.2.0.6** through [upstream PR #1196](https://github.com/notepad-plus-plus/nppPluginList/pull/1196); individual installations may see the Plugins Admin update later as the list propagates. The workspace tour below reflects the 0.2.0.6 UI. Screenshots use native controls; release host acceptance was completed separately from screenshot capture.

> **Release behavior:** OpenRouter is included in v0.2.0.6. Press Ctrl + right-click on selected text to open the optional AI context menu; ordinary right-click and keyboard menus keep their native Notepad++ behavior. You can disable the AI context menu entirely in Settings. See [usage](docs/USAGE.md#context-menu-actions).

<br>

## From a question to an edit

1. **Choose a service and model:** use your preferred cloud API or a local LM Studio endpoint.
2. **Shape the request:** select a task preset and output format, then inspect the assembled prompt before sending.
3. **Read the result:** switch between a basic formatted preview and the original response.
4. **Choose where it goes:** keep the answer in the panel, insert at the cursor, replace the selection, or create a new document.

<p align="center">
  <img src="docs/assets/readme/NppAIAssistant-2026-09-30-story.png" alt="The fox editor companion studying illustrated reference cards in a warmly lit archive" width="100%">
</p>

<br>

## Meet the workspace · v0.2.0.6

### Keep the request, response, and destination together

<table>
<tr>
<td width="38%" valign="top" align="center">
  <img src="docs/assets/screenshots/workspace-0.2.0.6-en.png" alt="English native workspace preview showing provider controls, a sample Markdown response, output destination and input box" width="100%">
</td>
<td width="62%" valign="top">

The upper controls select the provider, model, task profile, and output format. The response occupies the center; the destination and input remain below it. Resize the panel, drag the input divider, or use **A+ / A−** to make the text comfortable to read.

<ul>
<li><strong>Preview before send:</strong> check the assembled prompt before it reaches the selected provider.</li>
<li><strong>Formatted / original view:</strong> read basic Markdown or indented JSON while retaining the original response.</li>
<li><strong>Output destination:</strong> explicitly choose panel, cursor, selection, or new document.</li>
<li><strong>Reply selection:</strong> choose which assistant reply to insert.</li>
<li><strong>New / branch conversation:</strong> organize local transcripts. Conversation branches do not automatically become model context.</li>
</ul>

</td>
</tr>
</table>

<br>

<table>
<tr>
<td width="48%" valign="top">

<p align="center"><b>Configure the connection separately from the task</b></p>

<p align="center"><img src="docs/assets/screenshots/settings-0.2.0.6-en.png" alt="Native settings dialog with empty API key fields and local provider settings" width="100%"></p>

Settings separate provider connections from prompt configuration. LM Studio has its own URL, API mode, and model selection. Discover available models first, then explicitly choose a default. The API key fields in this screenshot are empty. Networking was disabled when it was captured, so model discovery appears unavailable.

</td>
<td width="4%"></td>
<td width="48%" valign="top">

<p align="center"><b>Know what you are sending</b></p>

<p align="center"><img src="docs/assets/screenshots/prompt-0.2.0.6-en.png" alt="Native prompt settings showing task presets, output rules and prompt preview" width="100%"></p>

Prompt configuration brings task presets, response language, output rules, and the assembled preview into one place. Built-in template sections are locked by default and require an explicit unlock to edit. Optional visible Memory is disabled by default; it is ordinary local text, so keep secrets out of it.

</td>
</tr>
</table>

<p align="center">
  <img src="docs/assets/readme/NppAIAssistant-2026-09-30-writing.png" alt="The fox companion guiding glowing sheets with a blue-lit wand in a moonlit archive" width="680">
</p>

### Native context-menu workflow

<p align="center">
  <img src="docs/assets/screenshots/context-menu-actions.png" alt="NppAIAssistant context-menu actions for selected text in Notepad++" width="100%">
</p>

Ordinary right-click opens the native Notepad++ menu. **Ctrl + right-click** on selected text opens the AI actions; **Shift+F10 / Menu key** keeps its native behavior. You can disable the AI context menu entirely in Settings.

<br>

## Providers and output

v0.2.0.6 implements OpenAI, Gemini, Claude, OpenRouter, LM Studio, and a generic OpenAI-compatible profile. Availability, model access, and usage charges depend on the selected provider. Copilot is currently paused.

| Output mode | Behavior in v0.2.0.6 |
| --- | --- |
| Text | Plain response for general editing and drafting. |
| Markdown | Basic headings, emphasis, code, lists, and quotes in the panel. HTML, images, links, and tables are not rendered. |
| JSON | Asks for JSON; this alone is not schema enforcement. |
| Structured JSON | Uses native schema transport and local validation for supported OpenAI and LM Studio Chat Completions models. Unsupported routes are blocked. |

Requests are non-streaming: the status strip reports request phases, and the answer appears after the response arrives. In **0.2.0.6**, local loopback generation uses a **900-second timeout for the relevant HTTP phases**; this is not a 900-second total request deadline. Model discovery uses a separate short timeout.

English and Traditional Chinese are supported. Japanese and Spanish cover the main workspace, with English fallback in advanced settings.

<br>

## Install the published release

Use **Plugins → Plugins Admin**, search for **NppAIAssistant**, and install the entry offered by your Notepad++ Plugin List. List updates may reach installations at different times.

For manual installation on **x64 Notepad++**:

1. Download `NppAIAssistant-0.2.0.6-x64.zip` from the [v0.2.0.6 release](https://github.com/pingqLIN/NppAIAssistant/releases/tag/v0.2.0.6).
2. Close Notepad++ and back up any existing plugin DLL.
3. Extract `NppAIAssistant.dll` to `<Notepad++>\plugins\NppAIAssistant\NppAIAssistant.dll`.
4. Restart Notepad++ and open its **Plugins → NppAIAssistant** menu.

The screenshots above correspond to the v0.2.0.6 interface. Match the plugin architecture to your editor; this page does not offer x86 or ARM64 release downloads.

<br>

## Privacy and editing behavior

- A request sends its assembled prompt and included text to the endpoint you choose. A local endpoint keeps that request local only if the configured service itself runs locally.
- v0.2.0.6 protects stored API credentials with Windows DPAPI under `%LocalAppData%\Notepad++\AIAssistant`. Preferences and visible prompt text live under `%AppData%\Notepad++\plugins\config\NppAIAssistant.ini`.
- A portable Notepad++ folder does **not** isolate those production settings paths.
- Editor writes are guarded against changed documents, read-only buffers, and lossy encoding conversion. Review generated text before applying it; supported writes are grouped for undo.
- Requests are single-turn by default. A visible transcript does not mean previous replies are automatically sent again.

<br>

## Build and contribute

Use Windows, Visual Studio with the C++ workload and Windows SDK, and CMake 3.21 or newer. From a source checkout:

```powershell
cmake -S . -B build -A x64
cmake --build build --config Release
```

Build output paths depend on the checked-out revision and generator. Use the repository packaging scripts when preparing a distributable ZIP. For bug reports, include plugin and Notepad++ versions, architecture, provider/API mode, and a minimal reproducible example with credentials and private text removed.

The [visual design notes](docs/VISUAL_DESIGN.md) explain the original AI-generated banner and screenshot provenance. The banner is project artwork; interface screenshots are captured native controls. This project is developed with AI assistance and distributed under [GPL-3.0](LICENSE).
