<div align="center">

<img src="docs/images/icon.png" width="96" alt="Phrasor icon">

# Phrasor

**Turn the rough prompt you're typing into a clear one without leaving the app you're in.**

Type naturally, press <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>P</kbd>, review the rewrite, press <kbd>Ctrl</kbd>+<kbd>Enter</kbd>.

[![Latest release](https://img.shields.io/github/v/release/Maneet7805/Phrasor?label=download&color=F58E4C)](https://github.com/Maneet7805/Phrasor/releases/latest)
[![CI](https://github.com/Maneet7805/Phrasor/actions/workflows/ci.yml/badge.svg)](https://github.com/Maneet7805/Phrasor/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Platform](https://img.shields.io/badge/platform-Windows%2010%20%7C%2011-0078d4)
![.NET 10](https://img.shields.io/badge/.NET-10-512bd4)

[**Download**](https://github.com/Maneet7805/Phrasor/releases/latest) · [Quick start](#quick-start) · [How it works](#how-it-works) · [FAQ](#troubleshooting) · [Contributing](CONTRIBUTING.md)

<img src="docs/images/main-home.webp" width="720" alt="Phrasor main window: Home page with the shortcut, status and the Try it box">

</div>

---

## Why

Most prompts are typed in a hurry: no deliverable, missing context, details buried in a run-on sentence. Phrasor is a small Windows tray app that fixes that in place, following [Anthropic's prompt engineering guidance](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview). It never sends anything for you: you always see the rewrite first and decide.

## Features

- **Works where you type.** ChatGPT, Claude, Gemini, Perplexity, VS Code, Word, email, Notepad: any normal text box, with no browser extension or per-app plugin.
- **Review before replace.** See the improved prompt, a word-level diff and the original side by side. Edit it, re-run it, copy it, or keep your original.
- **Doesn't invent things.** When details are missing it asks you questions instead of making them up. Simple questions stay simple, and good prompts come back unchanged.
- **Keeps exact details.** URLs, file paths, identifiers, numbers and quoted text are checked after every rewrite. Pasted code, stack traces and logs are held back and restored byte-for-byte.
- **Your clipboard is safe.** It's saved before and restored after every operation.
- **Voice dictation.** Tap or hold a shortcut, speak, and the transcript is typed (or optimised) for you.
- **Free to run.** Uses [Groq's](https://console.groq.com) free API tier by default. No card, no account with us, no server.
- **Private by design.** Keys are encrypted with Windows DPAPI, and prompt text is never logged. A rewrite is kept only if you press Save to History (see Privacy).

<details>
<summary><b>See the review window and the word-level diff view</b></summary>
<br>
<img src="docs/images/review-improved.png" width="640" alt="Phrasor review window showing an improved prompt, follow-up questions and what changed">
<br><br>
<img src="docs/images/review-changes.png" width="640" alt="Changes tab showing removed words in red and added words in green">
</details>

## The main window

Phrasor lives in the tray. **Open Phrasor** in the tray menu (or starting it a second time) opens its main window. Closing the window does not quit the app: the shortcuts keep working.

| Page | What it does |
| --- | --- |
| **Home** | Your shortcut, whether Phrasor is running or paused (with a **Pause shortcuts** button, the same as the tray's), your model and whether an API key is saved, a **Try it** box, and your three latest saved rewrites |
| **Try it** (on Home) | Rewrites a draft the same way the shortcut does and shows the result in the window with **Copy** and **Save to History**. It never pastes into another app |
| **History** | Rewrites you pressed Save on, by day, with search, Copy, Delete, **Delete all**, and an option to remove items after 30 or 90 days (off by default) |
| **Quality check** | Runs the test set against your own key. It shows what the run will cost in requests and minutes, and only starts when you press **Start** (see [Quality](#quality)) |
| **Settings** | General (theme, default mode, review window, start with Windows, update check), Model (main and fallback model, keys, **Test connection**), Shortcuts, Voice, Requirements, and Data. Nothing changes until you press **Save** |

Nothing is saved to History unless you press **Save to History**. A saved key is never shown again, not even to the window itself: it only says whether it is set.

<details>
<summary><b>See Try it, History, Quality check, Settings and first run</b></summary>
<br>
<img src="docs/images/main-tryit.webp" width="640" alt="Home page scrolled to the Try it box, with Task and Mode choices and a Rewrite button">
<br><br>
<img src="docs/images/main-history.webp" width="640" alt="History page with search, an empty state and the Manage options">
<br><br>
<img src="docs/images/main-quality.webp" width="640" alt="Quality check page with the judge model and the test set to run">
<br><br>
<img src="docs/images/main-settings.webp" width="640" alt="Settings page, General group, with Theme, Default mode and review window options">
<br><br>
<img src="docs/images/main-firstrun.webp" width="640" alt="First run: step 1 of 3, get a free API key from Groq or Google Gemini">
<br>
<sub>Screenshots are of a fresh copy with no API key and nothing saved, so the status says so and the lists are empty.</sub>
</details>

## Quick start

1. **Get a free API key** at <https://console.groq.com/keys>. It takes about a minute, and no card is needed.
2. **Download [`Phrasor.exe`](https://github.com/Maneet7805/Phrasor/releases/latest/download/Phrasor.exe)** from the latest release and double-click it. It is about 83 MB.
   - Windows SmartScreen may say *"Windows protected your PC"*, because the app isn't code-signed (signing needs a paid certificate). Click **More info → Run anyway**.
3. Choose **Yes** to install. Phrasor copies itself to `%LOCALAPPDATA%\Programs\Phrasor`, adds a Start menu shortcut, and can start with Windows. It doesn't need admin rights or a separate .NET install.
4. With no API key yet, Phrasor opens its main window on three steps: get a free key (the links open in your browser), paste it and test it (it is saved only after a passing test, and you can **Skip for now**), then see your shortcuts. You can also add a key later in **Settings → Model**.
5. Click into any text box, type a rough prompt, and press <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>P</kbd>.

**The main window needs the Microsoft Edge WebView2 runtime.** It is part of Windows 11 and of most Windows 10 PCs. If it is missing, the window says so and offers **Install now** (it downloads Microsoft's small installer after your click, checks that it is signed by Microsoft, and runs it without admin rights), **Open Microsoft's page**, or **Use classic settings**. The shortcuts, the review window and voice dictation do not need it.

**Coming from PromptForge?** The app was renamed to Phrasor. Earlier installed copies don't offer the update: install Phrasor once by hand. On first start it copies your settings and re-saves your API keys from the old `PromptForge` data folder (the old folder is left untouched, and nothing is copied if Phrasor already has settings). Phrasor does not remove an old PromptForge install: uninstall it yourself in Settings → Apps.

**Update:** from 1.1.0 on, Phrasor checks for a new release once a day and shows a notification. Click it (or **Update to …** in the tray menu), and it downloads the new exe, checks it against the release's `SHA256SUMS.txt`, and asks **Yes** to update. Your settings and keys are kept. You can also download the newer `Phrasor.exe` yourself, run it, and choose **Yes**. To turn the daily check off: Settings → General.
**Uninstall:** run `uninstall.cmd` from the release zip. It removes the app, the shortcut and start-with-Windows, and asks whether to delete settings, keys and logs.

## Usage

| Shortcut (changeable in Settings) | What it does |
| --- | --- |
| <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>P</kbd> | Optimise everything in the text box you're typing in |
| <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> | Optimise only the selected text. Use this in Word, code editors and long documents |
| <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>D</kbd> | Voice: tap to start and tap again to stop, or hold while talking and release |

In the review window:

| Key | Action |
| --- | --- |
| <kbd>Ctrl</kbd>+<kbd>Enter</kbd> | Replace your text with the (edited) improved prompt |
| <kbd>Esc</kbd> | Keep your original |
| <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>C</kbd> | Copy the improved prompt instead |
| <kbd>Ctrl</kbd>+<kbd>R</kbd> | Re-run, e.g. after answering the questions or changing Mode or Task |
| <kbd>Ctrl</kbd>+<kbd>1</kbd> / <kbd>2</kbd> / <kbd>3</kbd> | Improved / Changes / Original |

**Modes:**
- *Light*: minimal edits.
- *Standard* (default): clarity, plus structure where it helps.
- *Detailed*: full structure for complex tasks.

Set the default mode from the tray icon. The tray menu also has *Open Phrasor*, *Settings…*, *Copy last original text* as an undo safety net, *Pause shortcuts*, *Check for updates*, *Open logs folder* and *Exit*.

## Where it works

Phrasor reads and writes text by sending <kbd>Ctrl</kbd>+<kbd>A</kbd> / <kbd>C</kbd> / <kbd>V</kbd> to the focused app. It then reads the field back to confirm the replacement actually happened.

| Where | Status | Notes |
| --- | --- | --- |
| Browser AI chats (ChatGPT, Claude, Gemini, Perplexity) | ✅ Tested | |
| Notepad and other native Windows text boxes | ✅ Tested | Including Windows 11 Notepad's delayed paste |
| VS Code / Cursor chat panels | ✅ Tested | In the code editor itself, use *Optimise selection* |
| Microsoft Word | ✅ Tested | Use *Optimise selection*, because select-all would take the whole document |
| Voice dictation | ✅ Tested | Uses the same Groq key (Whisper) |
| Terminals (Windows Terminal, cmd, PowerShell, Claude Code / Codex CLI) | ⚠️ Copy only, by design | Keystrokes in a terminal could interrupt or run commands. Copy your prompt, press the shortcut, then paste the result yourself |
| Password fields | 🚫 Refused | Detected via UI Automation |
| Apps running as administrator | ❌ Not possible | Windows blocks input from normal apps into elevated ones. You get a message and can copy instead |

If a replacement can't be confirmed, the improved prompt goes to your clipboard and a notification tells you. Your original text is never lost.

## How it works

```mermaid
flowchart LR
    A[Hotkey] --> B[Capture text<br/>clipboard saved]
    B --> C[Mask code, traces,<br/>documents]
    C --> D[One LLM call<br/>JSON result]
    D --> E{Exact details<br/>kept?}
    E -- no --> F[One repair call]
    E -- yes --> G[Review window]
    F --> G
    G -- Ctrl+Enter --> H[Paste, verify,<br/>restore clipboard]
```

1. **Mask pasted material.** Fenced code, stack traces, logs and `<document>` blocks are swapped for `[[BLOCK_n]]` markers. They come back byte-for-byte, and the request uses fewer tokens.
2. **One model call** with a static system prompt (`src/Phrasor.Core/Optimization/SystemPrompt.cs`). The prompt is static so it can be cached. The call classifies the task, decides how much to change, rewrites, and lists missing details as questions, all as JSON.
3. **Check exact details.** URLs, paths, file names, identifiers, quoted text and numbers from your draft must survive. If any were dropped, one repair call fixes them; otherwise the review window warns you.
4. **Fallback.** If the main model is rate-limited or down, a second model with its own limits is tried.

The rewriting rules:
- Be clear and direct, and state the deliverable.
- Keep the user's reasons.
- Say what to do rather than what to avoid.
- Add structure only when there are several requirements.
- Put pasted material before the request.
- No shouting, no "world-class expert" filler, nothing invented.

## Quality

A test set of 128 prompts (13 of them held out for final measurements) runs with code-graded checks, three times each by default, so a change shows up as a per-case pass rate rather than one lucky or unlucky run. It covers simple, vague, coding, debugging, research, writing, study, planning, image-generation, template placeholders, references to material that isn't included, casually stated rules, questions, answers, statements and standing instructions that must keep their type, strict constraints, already-good, long, prompt-injection and non-English drafts. The checks look for:
- dropped details (including the user's own `[slots]` and `{{slots}}`) and leftover markers
- inserted placeholders and filler phrases
- invented numbers and over-expansion
- rewriting prompts that were already good
- missing questions on vague drafts

With `--judge`, a second model also checks for answering instead of rewriting, invented details, dropped requirements (a rule or condition the user stated that the rewrite left out), changed intent (a question turned into an instruction, "fix" turned into "explain", a standing instruction turned into a one-off task, or pasted context turned into the task), rewrites written as the AI's reply, and added requests (deliverables, formats or "ask me first" steps the draft didn't ask for). Set the judge on the **Quality check** page to a different provider from the main model, so it isn't grading its own model family.

| Version | Passed all checks | Median / p95 latency |
| --- | --- | --- |
| 0.2 | 48/53 (91%) | 830 ms / 1.5 s |
| 0.3 – 1.0 | 50/53 (94%) | 914 ms / 1.7 s |

The tests used `openai/gpt-oss-120b` on Groq's free tier, with one run per case; later results use repeats. Run it yourself: open the **Quality check** page of the main window, pick `eval/cases.json`, and press **Start** after it shows what the run will cost. It uses your own key and the free allowance, and a cancelled run saves nothing. To compare two versions of the rewriting rules, see [eval/README.md](eval/README.md).

## Models and free-tier limits

| Provider | Default model | Notes |
| --- | --- | --- |
| **Groq** (default) | `openai/gpt-oss-120b`, fallback `openai/gpt-oss-20b` | Free tier: 30 requests/min, 1,000/day and 8K tokens/min per model. That comfortably covers personal use |
| Gemini | `gemini-3.5-flash-lite` | Free tier available. Google may use free-tier prompts to improve its products |
| Ollama | any local model | Fully offline, but slower and RAM-hungry |
| Custom | any OpenAI-compatible API | Set the base URL, model and key |

A typical rewrite uses about 1,200 input tokens, most of which is the cached system prompt, plus 150–300 output tokens. Free-tier limits change, so check your provider's docs.

## Privacy

- Your text never leaves your PC until you press a shortcut. Then only the text you chose goes to your model provider, and dictated audio goes to your voice provider.
- The update check (on by default, Settings → General) asks `api.github.com` once a day which release is newest. It sends no prompt text, settings or keys.
- API keys are encrypted with Windows DPAPI for your Windows account (`%APPDATA%\Phrasor\secrets.dat`).
- Nothing is saved automatically. A draft and its rewrite are kept only when you press **Save to History** (review window or Try it). They go to `%LOCALAPPDATA%\Phrasor\History\history.dat` on this PC, encrypted with Windows DPAPI for your Windows account: up to 500 items, each side cut at 20,000 characters. The History page can delete one item, delete all, or remove items after 30 or 90 days (off by default). Delete all data in Settings removes them too.
- Logs (`%APPDATA%\Phrasor\logs`, kept 7 days) contain events and timings only: never prompt text, transcripts or keys.
- Text Phrasor puts on the clipboard is marked to stay out of Windows clipboard history and cloud sync.
- The main window is a web page that loads only files inside Phrasor (including its fonts); the page can make no network requests, and it uses the Microsoft Edge WebView2 runtime that ships with Windows. Font licences are in [THIRD-PARTY.md](THIRD-PARTY.md).

## Troubleshooting

| Problem | Fix |
| --- | --- |
| Shortcut does nothing | Another app may own it. Settings → Shortcuts shows conflicts. Also check *Pause shortcuts* in the tray menu |
| "Couldn't read text here" | The field is empty, or the app runs as administrator. Select the text and use *Optimise selection*, or copy it manually |
| "Rate limit reached" | Wait a few seconds; the fallback model is used automatically |
| Result copied instead of replaced | Focus changed, the field changed, or the app rejected the paste. Press <kbd>Ctrl</kbd>+<kbd>V</kbd> |
| A shortcut types a character (e.g. <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>D</kbd> types "ḍ") | Your keyboard layout uses <kbd>Ctrl</kbd>+<kbd>Alt</kbd> as AltGr. Phrasor warns about this at startup and in Settings; pick a shortcut without <kbd>Ctrl</kbd>+<kbd>Alt</kbd>, e.g. <kbd>Alt</kbd>+<kbd>V</kbd> |
| Voice records the wrong microphone | Phrasor uses Windows' default recording device: Settings → System → Sound → Input |
| Voice: "Couldn't start the microphone" | Windows Settings → Privacy & security → Microphone → allow desktop apps |
| Anything else | Tray icon → *Open logs folder*, check the latest `phrasor-*.log`, and [open an issue](https://github.com/Maneet7805/Phrasor/issues/new/choose) |

## Build from source

You need the [.NET 10 SDK](https://dotnet.microsoft.com/download). The code builds on Windows, Linux or macOS; the app runs on Windows 10/11 x64.

```bash
git clone https://github.com/Maneet7805/Phrasor.git
cd Phrasor
dotnet test tests/Phrasor.Core.Tests
dotnet publish src/Phrasor.App -c Release -o publish
```

The output is a single self-contained `publish/Phrasor.exe` (about 83 MB; 83,304,426 bytes measured on main at 8582739). Releases are built by [GitHub Actions](.github/workflows/release.yml) whenever a `v*` tag is pushed.

```
src/Phrasor.Core     optimiser pipeline, provider client, settings, eval runner (cross-platform, unit-tested)
src/Phrasor.App      Windows tray app: hotkeys, text capture/replace, review window, main window (WebView2 pages in Web/), classic settings, voice, self-install
tests/                   unit tests for the core
eval/cases.json          optimiser test set
installer/               uninstall script
```

## Contributing

Bug reports, ideas and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). Please report security issues privately as described in [SECURITY.md](SECURITY.md).

## License

[MIT](LICENSE) © 2026 Maneet Arvind Mehta

## Acknowledgements

- [Anthropic's prompt engineering guide](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview), the basis of the rewriting rules
- [Groq](https://groq.com) for the free inference tier
- [DiffPlex](https://github.com/mmanela/diffplex) (word diff) and [NAudio](https://github.com/naudio/NAudio) (microphone capture)
