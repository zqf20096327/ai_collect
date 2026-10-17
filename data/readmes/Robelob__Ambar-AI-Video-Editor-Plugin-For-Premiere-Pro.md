# Ambar — AI Vlog Editor for Premiere Pro

Ambar is a Premiere Pro UXP + CEP hybrid plugin that uses AI to automatically edit talking-head vlogs: detecting and removing silence, suggesting and placing B-roll, generating captions, and organising your project bins — all without uploading your video to the cloud.

---

## Features

| Panel | What it does |
|---|---|
| **Edit** | Three-layer audio pipeline: RMS silence detection → Whisper transcription → LLM editorial decisions. Places markers for review, then ripple-deletes on commit. |
| **B-roll** | Vision model classifies each clip frame, LLM matches B-roll clips to transcript, places them on V2. |
| **Captions** | Generates word-level SRT captions or places `.mogrt` templates on V3. Six built-in styles. |
| **Organise** | Vision-scans every bin clip and moves them into labelled bins automatically. |

**No full video or audio is ever uploaded to the cloud — only ~2KB of transcript text.**

---

## How It Works (Edit Panel)

```
User clicks Analyze
       ↓
LAYER 1 — AudioAnalyzer.findSilences()        [UXP, pure JS math]
  Reads source PCM via AudioContext
  Returns: silence ranges in ticks + speech segments in ms
       ↓
LAYER 2 — WhisperService.transcribeSegments() [UXP, speech-only WAV blobs]
  Sends small speech-only WAV blobs to Whisper (Groq / OpenAI / local)
  Returns: word-level timestamps
       ↓
LAYER 3 — AIService.sendPrompt()              [UXP, text only ~2KB]
  Sends transcript summary to Ollama / Groq / Gemini / Claude / OpenAI
  Returns: confirmedCuts + retakes + broll suggestions as JSON
       ↓
TimelineEditor.analyzeAndMark()               [UXP]
  Places markers on the timeline ruler — no cuts yet
       ↓
User reviews markers → clicks Commit
       ↓
CEPBridge.razorAndDelete(segments)
host.jsx: razor + ripple delete               [ExtendScript / QE DOM]
```

The plugin is non-destructive until you click **Commit edits**. Every proposed cut is a marker you can delete before committing.

---

## Requirements

| Component | Minimum version |
|---|---|
| Adobe Premiere Pro | 25.x (UXP panels) |
| CEP Bridge support | 22.0+ |
| OS | Windows 10/11 or macOS 12+ |
| AI provider | One of: Ollama (local), Google Gemini, OpenAI, Anthropic Claude, Groq, or any OpenAI-compatible endpoint |
| Whisper provider | One of: Groq (cloud, recommended), OpenAI, or local whisper.cpp |
| Vision model | Ollama with llava:7b, moondream, or llava:13b (for B-roll and Organise panels) |

---

## Installation

### Part 1 — UXP Plugin

1. Open Premiere Pro
2. Go to **Window > UXP Developer Tools**
3. Click **Add Plugin**
4. Navigate to the repo root and select `manifest.json`
5. The **Ambar** panel appears under **Window > Extensions (UXP)**

### Part 2 — CEP Bridge (required for timeline cuts and B-roll placement)

The CEP bridge is a hidden background panel that performs destructive timeline operations (razor, ripple delete) via ExtendScript. Without it, the plugin can analyze and place markers but cannot commit edits.

#### Step 1 — Enable CEP debug mode

**Windows** — open PowerShell and run:
```powershell
New-ItemProperty -Path "HKCU:\SOFTWARE\Adobe\CSXS.11" -Name PlayerDebugMode -Value "1" -PropertyType String -Force
```

**macOS** — run in Terminal:
```bash
defaults write com.adobe.CSXS.11 PlayerDebugMode 1
```

#### Step 2 — Install the bridge panel

**Windows:**
```powershell
Copy-Item -Path "C:\path\to\cep-bridge\*" -Destination "$env:APPDATA\Adobe\CEP\extensions\ambar-bridge" -Recurse -Force
```

**macOS:**
```bash
cp -R /path/to/cep-bridge/ ~/Library/Application\ Support/Adobe/CEP/extensions/ambar-bridge/
```

Replace the path with the actual location of the `cep-bridge/` folder in this repo.

#### Step 3 — Restart Premiere Pro

After restarting, verify the bridge is alive:
1. Open the Ambar panel
2. Open the UXP Developer Tools console for the plugin
3. Type `CEPBridge.ping()` — you should see `{ success: true, message: 'bridge alive' }`

If ping fails, check **Window > Extensions > Ambar Bridge** — it should be listed (even though it is invisible by design).

---

## API Key Setup

Open the **Settings** panel inside the plugin and configure your AI providers. Alternatively, edit `js/utils/constants.js` directly — constants take priority over UI/localStorage values.

### Text LLM (Edit, B-roll, Captions, Organise)

| Provider | Where to get a key | Default model |
|---|---|---|
| **Ollama** (local, free) | [ollama.com](https://ollama.com) — install then `ollama pull llama3.2` | llama3.2 |
| **Google Gemini** | aistudio.google.com | gemini-2.0-flash |
| **OpenAI** | platform.openai.com | gpt-4o |
| **Anthropic Claude** | console.anthropic.com | claude-opus-4-7 |
| **OpenAI-compatible** | Groq, LM Studio, Mistral, etc. | set in UI |

### Whisper Transcription (Edit panel, Layer 2)

| Provider | Notes |
|---|---|
| **Groq** (default) | Fast, free tier, uses same API key as Groq LLM |
| **OpenAI** | Uses your OpenAI key |
| **local-whisper** | whisper.cpp running locally, set base URL in Settings |

### Vision Model (B-roll + Organise panels)

Requires Ollama running locally with a multimodal model pulled:
```bash
ollama pull llava:7b    # recommended
ollama pull moondream   # smaller / faster
ollama pull llava:13b   # higher quality
```

---

## Usage

### Edit Panel — Silence Removal

1. Open a sequence in Premiere Pro — Ambar detects it automatically
2. Click **Analyze** — the three-step pipeline runs:
   - RMS energy scan finds silence regions
   - Whisper transcribes speech-only segments
   - LLM confirms cuts and identifies retakes
3. Orange markers appear on the timeline ruler at each proposed cut
4. Scrub through and **delete any marker** you want to keep
5. Click **Commit edits** — segments are ripple-deleted and gaps are closed

### B-roll Panel

1. Make sure B-roll clips are imported into your project bin
2. Click **Suggest B-roll** — Ollama vision-classifies each clip and the LLM matches them to your transcript
3. Review the suggestions in the log
4. Click **Place on timeline** — clips are placed on V2 at the suggested in-points

### Captions Panel

1. Choose a caption style (six built-in options, or import a `.mogrt`)
2. Click **Generate captions** — word-level timestamps from Whisper are used to create the caption track
3. Styles 01–05 write an SRT caption track; the Mogrt style places one template per line on V3
4. Click **Export SRT** to save the SRT file

### Organise Panel

1. Click **Organise project bins** — Ollama vision-scans a representative frame from every clip
2. Clips are classified by content type and moved into labelled bins automatically
3. New footage is flagged in the Project.Memory sidebar

---

## Settings

All settings are available in the **Settings** panel. Key constants in `js/utils/constants.js`:

| Constant | Default | Effect |
|---|---|---|
| `AI_PROVIDER` | `'gemini'` | Text LLM: `ollama` / `gemini` / `openai` / `anthropic` / `openai-compatible` |
| `AI_MODEL` | `''` | Leave blank for provider default |
| `WHISPER_PROVIDER` | `'groq'` | Transcription: `groq` / `openai` / `local-whisper` |
| `VISION_MODEL` | `'llava:7b'` | Ollama vision model for B-roll and Organise |
| `MIN_SILENCE_SECONDS` | `1.2` | Ignore silences shorter than this |
| `PADDING_SECONDS` | `0.15` | Breath room kept on each side of every cut |
| `MIN_CONFIDENCE` | `0.75` | Ignore AI suggestions below this score (0–1) |

**CONSTANTS are source of truth.** Changing a value in `constants.js` and reloading the plugin overrides any UI or localStorage setting.

---

## Project Structure

```
(repo root)
  manifest.json              ← Plugin ID: com.robelaipremiereassistant.plugin.v2
  index.html                 ← UXP panel entry point
  css/
    variables.css
    main.css
    components.css
  js/
    utils/
      constants.js           ← All tuneable values and provider config
      logger.js
      error-handler.js
      validators.js
      capabilities.js        ← Runtime feature detection
    core/
      project-memory.js      ← Per-sequence session state (Project.Memory panel)
      cep-bridge.js          ← UXP side of file-based IPC
      audio-analyzer.js      ← Layer 1: RMS silence detection via AudioContext
      frame-extractor.js     ← Extracts frames for vision classification
      premiere-api.js        ← UXP Premiere API wrapper
      project-reader.js      ← Reads sequences, clips, tracks
      timeline-editor.js     ← Orchestrates all three edit layers
      broll-placer.js        ← Places B-roll clips on V2
      caption-engine.js      ← Writes SRT tracks and places mogrt clips
      project-organizer.js   ← Moves clips into labelled bins
    ai/
      ai-service.js          ← Layer 3: multi-provider text LLM client
      gemini-service.js      ← Gemini-specific alias (re-exports ai-service)
      whisper-service.js     ← Layer 2: Whisper audio transcription
      vision-service.js      ← Vision model client (Ollama multimodal)
      prompt-templates.js    ← System prompts for editorial analysis
      response-parser.js     ← parseEditPlan(), validates AI JSON output
    ui/
      ui-state.js            ← State machine: READY / ANALYZING / MARKERS_PLACED / COMMITTING / COMMITTED
      ui-controller.js       ← All button handlers and panel switching
    index.js                 ← Plugin entry point

cep-bridge/                  ← CEP panel (install to CEP extensions folder)
  CSXS/manifest.xml          ← CEP 11 hidden panel config
  jsx/host.jsx               ← ExtendScript: razor, ripple delete (ES3 only)
  js/main.js                 ← 200ms polling loop
```

---

## Architecture Notes

### UXP + CEP Hybrid
UXP cannot razor clips at arbitrary positions (confirmed missing from Adobe's v1 roadmap). The hidden CEP bridge fills this gap using the QE DOM. When UXP ships a split/razor API, `CEPBridge.razorAndDelete()` callsites (marked `// TODO(MIGRATE-TO-UXP)`) can be replaced with a native call and the CEP bridge removed.

### File-Based IPC
UXP and CEP run in separate JavaScript engines with no shared memory. Commands are written as JSON to a shared temp directory; the CEP bridge polls every 200ms, executes, and writes a response. UXP times out after 10 seconds.

### Reverse-Order Processing
All edit segments are processed from end-of-timeline toward the start. This is required because each ripple delete shifts all subsequent timecodes left — forward processing would apply cuts at wrong positions.

### Two-Step Commit Flow
Analyze places markers; Commit executes cuts. This is intentional — it lets the editor review and remove any proposed cut before anything is changed on the timeline.

### No Bundler
Plain `<script>` tags in `index.html`. No webpack or build step. Edit a file, reload the panel in UXP Developer Tools.

---

## Known Limitations

- **Audio crossfades at cut points** — `track.addTransition()` is not exposed in the QE DOM in the current Premiere build. Add crossfades manually with **Sequence > Apply Default Transitions to Selection** after committing.
- **Undo** — each cut is a separate undo step (no batched `beginUndoableAction()`). Use **Edit > History** to revert to the state before Commit.
- **Vision classification requires Ollama** — the B-roll and Organise panels need a local Ollama instance with a multimodal model. Cloud-only setups cannot use these panels.

---

## Troubleshooting

**"CEP Bridge not found" after Commit**
- Verify debug mode is enabled (see installation Step 1)
- Verify the `ambar-bridge` folder exists in `%APPDATA%\Adobe\CEP\extensions\` (Windows) or `~/Library/Application Support/Adobe/CEP/extensions/` (macOS)
- Restart Premiere Pro after installing the bridge

**"No active sequence" on Analyze**
- Click your sequence in the Timeline panel to bring it into focus

**Markers placed but 0 cuts applied**
- The bridge may have timed out (default 10s). Try committing fewer segments at a time by removing most markers before each commit.

**Whisper transcription fails**
- Check that your Whisper provider API key is set in Settings
- For Groq: ensure you have a valid Groq API key and internet access
- For local-whisper: ensure whisper.cpp is running and the base URL is set correctly

**B-roll or Organise panel shows vision errors**
- Confirm Ollama is running: `ollama serve`
- Confirm the vision model is pulled: `ollama list`
- Check that the vision model selected in Settings matches what you have pulled

**AI returns unexpected results**
- Try a higher-quality model (e.g. `gemini-1.5-pro` instead of `flash`, or `llava:13b` instead of `llava:7b`)
- The system prompt assumes talking-head footage — results on music or heavily cut timelines will vary

---

## Version

0.2.0 — three-layer audio pipeline, B-roll panel, Captions panel, Organise panel, Project.Memory sidebar
