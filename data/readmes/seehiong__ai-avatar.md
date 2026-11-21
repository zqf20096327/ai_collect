# AI Interviewer Avatar

A video-call style AI interviewer: a talking 3D head (or a photoreal face) that holds a spoken mock interview
grounded in your resume and a job description, then scores you against a rubric. Everything runs locally, either
with a local server or entirely in the browser (WebGPU).

```
Browser (web/: Three.js head, open mic, Setup / Interview / Feedback tabs)
   │  WebSocket: config · 16 kHz PCM · nudge · complete      ▲ captions · say (WAV + visemes + emotion)
   ▼                                                          │
backend/server.py ── Silero VAD turn-taking ── faster-whisper STT (primed with resume/JD terms)
                  ── Ollama LLM (interviewer persona, streamed per sentence, emotion tags)
                  ── Kokoro TTS (exact phoneme durations → visemes) + wav2arkit neural lip sync
                     — or, with no server, the same pipeline in-browser (web/browser-engine.js)
```

## Quick start

Requirements: Python 3.10+ and [Ollama](https://ollama.com) with a chat model pulled.

```bash
ollama pull nemotron-3.5-lightning:30b     # default; or a small one: ollama pull llama3.2:3b
./run.sh                                   # Windows: run.bat   (add --model llama3.2:3b for the small model)
```

Open **http://127.0.0.1:8080**, fill in **Setup** (or click **Load sample**), then **Start interview** and just talk.
The first run creates `backend/.venv` and downloads the Kokoro/Piper voices and the neural lip-sync model.

Useful options: `--model qwen3.8:27b` (deeper, slower), `--whisper base.en` (faster STT), `--tts piper` or `--tts zonos`,
`--no-stt` (typed answers only), `--no-neural-lipsync`, `--photoreal` (see below).

The mic only works on `localhost`/`127.0.0.1` or over HTTPS.

**Optional: ZONOS3-Mini voice** (Setup → Voice provider). More natural than Kokoro, 44.1 kHz, about 3× faster than real
time on the CPU, with no GPU needed. Build its server once (needs cmake, a C++ compiler and Rust):

```bash
git clone https://github.com/Zyphra/ZONOS3-Mini ~/github/ZONOS3-Mini && cd ~/github/ZONOS3-Mini
git submodule update --init servers/ggml/ggml third_party/zyphra-textnorm
cd servers/ggml && cmake -B build -DCMAKE_BUILD_TYPE=Release && cmake --build build -j
hf download Zyphra/ZONOS3-Mini gguf/backbone-ptq.gguf gguf/zac-keep2.gguf gguf/spk-encoder.gguf --include 'gguf/voices/*' --local-dir .
```

The backend starts it on first use (`ZONOS3_HOME` / `ZONOS3_URL` to change where it looks).

## Two engines

The **local server** is the full app. The **in-browser engine is experimental**: a taster that runs with nothing
installed, but with a small model (simpler questions, rougher feedback), and it depends on your browser's WebGPU
support. It works best in Chrome or Edge on Windows or macOS. On Linux, WebGPU is still behind flags and the GPU
driver can drop the model mid-interview. For a real practice interview, use the local server.

| | Local server (`./run.sh`) | In-browser, experimental (WebGPU, e.g. GitHub Pages) |
| --- | --- | --- |
| Interviewer model | Ollama, 30B by default | Qwen2.5-1.5B via WebLLM (`?llm=<id>` to change) |
| Live captions, "unfinished thought" hold | ✅ | — |
| Lip sync | exact phoneme timings + neural (wav2arkit) | estimated timings (`?arkit=1` for in-browser neural) |
| Feedback report | solid | demo quality |
| Setup | Python + Ollama | ~1.5 GB model download on first visit, then cached |

The page uses the local server when it can reach one, and otherwise falls back to the browser engine. On Linux,
Chrome/Edge need `chrome://flags/#enable-unsafe-webgpu` (and `#enable-vulkan`) for the browser engine.

## Avatars

Choose under **Setup → Avatar**, or with `?avatar=`:

| Key | Avatar | Voice / name |
| --- | --- | --- |
| `photoreal` | **1. Photoreal (local GPU)**: a real portrait animated live with LivePortrait and MuseTalk. Needs `./run.sh --photoreal`. | `af_heart` / Claire |
| `mpfb-live-male` | **2. MPFB male**: our own MakeHuman/MPFB head (52 ARKit shapes + 15 visemes), CPU-only animation. | `am_michael` / Alex |
| `metahuman` (default) | **3. Unreal MetaHuman**: exported from Unreal Engine with 51 ARKit shapes, CPU-only animation. | `af_heart` / Claire |

Both 3D heads share the same browser animation (`web/avatar.js`, `web/behaviour.js`): coarticulated lip sync,
blinks and saccades timed like real video calls, nods and brow raises on pitch accents, listening backchannels,
breathing and posture, and per-sentence emotions from the LLM's tags (`[warm]`, `[curious]`, ...).
`?model=<url.glb>` loads any GLB with ARKit/viseme blendshape names. `?bg=studio` swaps the room background
for a plain backdrop.

## Interview features

- **Setup:** role, seniority, company, interview type, difficulty, style, JD, resume (paste or PDF/TXT/MD) and an
  optional [ATS Buddy](https://github.com/seehiong/ats-buddy) gap report. Stored in the browser only.
- **Turn-taking:** open mic with barge-in, adjustable patience, an "unfinished thought" hold, and silence nudges.
- **Interviewer behaviour:** plans 4–6 topics, follows up on vague answers, stays neutral (praise is trimmed in
  code), covers new ground, asks one design question in technical interviews, watches the clock and closes properly.
- **Question bank:** about 40 common questions in six categories (`web/question-bank.js`), plus your own must-asks.
- **Feedback:** rubric scores with quotes checked against the transcript (✓ / ⚠), advice and questions to practise.
  Downloadable as Markdown with the transcript.
- **History:** past interviews stay in the browser; **Adapt to my past interviews** steers the next session towards
  your weak areas.
- **▶ Watch AI demo:** an AI candidate answers the interviewer, as a model answer key.

## Photoreal face (local GPU)

`./run.sh --photoreal` also starts `tools/photoreal/photoreal_server.py`, which renders the whole face live from
`assets/ai-interviewer.png`: LivePortrait for head, eyes, brows and smile, MuseTalk for the mouth, driven by the
conversation (`behaviour.py`). Frames stream to the page and are shown by the audio clock.

- Tested on Linux with an AMD Radeon 8060S (ROCm nightly PyTorch, fp16). NVIDIA/CUDA should work but is untested.
- Uses about 4 GB of GPU memory; the first start takes about 1.5 min. Set `AVATAR_GPU_PY` if the GPU Python isn't
  `~/miniforge3/envs/avatar-gpu/bin/python`, and `PHOTOREAL_ARGS` to tune frame strides (`--library` uses
  pre-rendered clips for smaller GPUs).
- Large generated files (motion library, prep cache, model weights) live under `~/models/` and are not committed.
- LivePortrait's InsightFace detector weights are for non-commercial research only.

## Building the heads

**MPFB male** (headless Blender):

```bash
tools/setup_mpfb.sh          # one time: MPFB extension, asset packs and rig
tools/build_mpfb_avatar.sh   # writes assets/models/mpfb.glb; see --help for body, skin, hair, clothes options
```

**MetaHuman** — exported from Unreal Engine 5 with
[metahuman-to-glb](https://github.com/creategamecharacters/metahuman-to-glb) (it bakes the 51 ARKit shapes
through UE's Sequencer, since MetaHuman faces have no morph targets of their own), then finished in Blender:

1. metahuman-to-glb stage 01 (in the editor) and stage 02.
2. `tools/make_suit.py`: an original business suit built from the outfit and arm skin.
3. `tools/makehuman_hair.py --hair <MPFB data>/hair/toigo_blunt_bob`: replaces the UE groom with a CC0 MakeHuman
   hair mesh fitted to the head (check each hair's `.mhclo` licence: several community hairs are AGPL3).
4. metahuman-to-glb stage 03 (Draco GLB).
5. `tools/fix_metahuman_glb.py`: fixes UE's shifted face materials, swaps in the DCC export's skin maps,
   and drops unused images.

Brow and lash atlases go in `assets/models/metahuman-v2/`; hair and brow colours are set in `AVATARS` in `web/index.html`.

## Layout

| Path | What it does |
| --- | --- |
| `web/index.html` | The page: scene, lighting, materials, audio, open mic, tabs, avatar registry (`AVATARS`). |
| `web/avatar.js`, `web/behaviour.js` | Face and head animation and the conversational behaviour model. |
| `web/persona.js`, `web/question-bank.js`, `web/history.js` | Prompts, question bank, interview history and coaching. |
| `web/browser-engine.js` | In-browser engine: Silero VAD, Whisper, WebLLM and Kokoro on WebGPU. |
| `web/photo-avatar-gpu.js` | Browser side of the photoreal avatar: shows the streamed frames by the audio clock. |
| `backend/` | WebSocket server, turn-taking, STT, LLM, TTS, visemes, pacing. |
| `tools/` | Head builds (MPFB, MetaHuman finishing) and the photoreal service. |
| `assets/` | Head GLBs and textures, the portrait and photoreal assets, the room HDRI. |
| `.github/workflows/pages.yml` | Publishes `web/` and `assets/` to GitHub Pages. |

## Known limitations

- Fast models sometimes run longer than asked; feedback scores are the model's judgement.
- Short words can be misheard by Whisper; Setup terms are recognised much better. Use headphones if the
  interviewer interrupts itself.
- Ollama swapping between the interview and feedback models slows replies when both don't fit in memory.
- In-browser engine (experimental): on the tested Linux/AMD machine, Chrome's WebGPU lost the GPU device
  (`VK_ERROR_DEVICE_LOST`) even with the default 1.5B model, so expect it to stop mid-interview there. A
  different model can be tried with `?llm=<WebLLM model id>`.

## Licences

The source code is [MIT](LICENSE). Some assets are **not** MIT: the MetaHuman head and its textures (Epic's
MetaHuman licence), and the interviewer portrait, its photoreal derivatives and the MPFB texture images. Bundled
third-party code (coi-serviceworker, a shader ported from metahuman-to-glb, TalkingHead's rig) and all asset
terms are listed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
