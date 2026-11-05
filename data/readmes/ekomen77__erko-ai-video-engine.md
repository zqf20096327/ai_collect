# Erko AI Video Engine

![Erko AI Video Engine banner](assets/banner.jpg)

**[Türkçe](#türkçe) · [English](#english)** · [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Türkçe

**Ses kaydınızı ekomen77 tarzı 1080p anlatım videosuna dönüştürün.** Stüdyo beyaz tahtaları, tebeşir kâğıt diyagramları, koyu decompiler terminalleri, kanıt kartları, mürekkepli damgalar ve YouTube arayüz kaplamaları — Headless Chrome + FFmpeg ile kare kare render edilir, sesinizle milisaniye hassasiyetinde prosedürel SFX ile senkronize edilir.

**Ajan becerisi (skill)** olarak (opencode / Claude / herhangi bir kodlama ajanı) ya da düz CLI hattı olarak çalışır.

![Türkçe demo — 32 saniyelik tanıtım](assets/demo_tr.gif)

**[▶ 32 saniyelik 1080p Türkçe tanıtımı izle](assets/demo_tr.mp4)** — tamamen Türkçe metinlerle üretilmiş, seslendirme miksli sürüm · **[Storyboard](assets/storyboard.jpg)** · **[English demo](assets/demo.mp4)**

### Öne çıkanlar

- **20 sahada test edilmiş altın kural** (`SKILL.md`) — gerçek render turlarından damıtıldı: tipografi, pozlama, ışık, damgalar, kamera işi, yasak desenler.
- **13 normalize edilmiş karakter pozu** (`700×780`, kilitli taban çizgileri) + prosedürel el çizimi asistan **Clawd** (`drawClawd`, `drawEmote`, `drawBrushWipe`, `drawIris`).
- **19 font dosyası** — Türkçe glif desteği doğrulanmış, hepsi SIL OFL.
- **İki ses hattı**: numpy destekli SFX mikseri ve numpy gerektirmeyen stereo miks (sıcak bir arka plan ambiyansıyla) — ikisi de aynı 30 fps RMS zarfını üretir.
- **İki üretim şablonu** (`intro_bomba`, `chapter_01`) ve `SKILL.md`'de anlatılan tüm stüdyo/kara tahta arketip sistemi.
- **Tek komutla ses değiştirme** — seslendirmeyi değiştir, 30 saniyenin altında yeniden miksle ve render et.
- **Tanıtımın kaynak projesi dahil** — `examples/trailer/`: kendi sesinle üç komutta yeniden üret.

### Nasıl çalışır

```
 voice.mp3 ─► build_audio_with_sfx.py ─► intro_audio_mix.wav + intro_envelope.json
               (48 kHz normalise,          (30 fps RMS envelope,
                procedural SFX)             timing data for the renderer)

 intro_animation.html ─► render_video.js ─► Headless Chrome (1920×1080)
   (Canvas timeline,       local HTTP server    │  JPEG frames over loopback
    window.renderAtTime)    + FFmpeg pipe        ▼
                                          FFmpeg (H.264 + AAC, faststart)
                                                     │
                                                     ▼
                                          out/intro_1080p.mp4
```

Motor küçük bir yerel HTTP sunucusu çalıştırır, headless Chrome'u kare döngüsünde sürer (`window.renderAtTime(t, amp)` → `canvas.toBlob` → POST) ve her JPEG'i doğrudan FFmpeg'e aktarır — diske ara kare yazılmaz. Yukarıdaki 960 karelik demo yaklaşık 65 saniyede render edildi.

### Hızlı başlangıç

#### Seçenek A — ajan becerisi olarak kur

```bash
npx skills@latest add ekomen77/erko-ai-video-engine
```

Sonra ajanına videoyu üretmesini söyle (örn. *"bu ses dosyası için intro videosu render et"*) — beceri ona tüm hattı, kuralları ve varlıkları öğretir.

#### Seçenek B — CLI'yi kendin çalıştır

Gereksinimler: **Node 18+**, `PATH`'te **FFmpeg**, **Chrome/Chromium** (otomatik bulunur), **Python 3.8+** (numpy yalnızca `build_audio_with_sfx.py` için).

```bash
# 1) Tek bir düz proje klasörü, örn. my-video/
#    Bu depodan kopyala (intro şablonu örneği):
#      examples/intro_bomba_animation.html  ->  intro_animation.html
#      resources/fonts/Kalam-Bold.ttf, PatrickHand-Regular.ttf, JetBrainsMono-Bold.ttf
#      resources/clawd_assistant.js
#      resources/studio_background_1080p.jpg
#      resources/slate_chalkboard_1080p.png
#      resources/pure_poses/               ->  pure_poses/   (alt klasör olarak kalsın)
#      scripts/*.py, scripts/render_video.js
#      ses dosyanız: my_voice.mp3

# 2) Ses master'ı + zarf
python build_audio_with_sfx.py my_voice.mp3 intro

# 3) 1080p MP4'ü render et
node render_video.js intro
# -> out/intro_1080p.mp4  (+ still_*.jpg önizleme kareleri)
```

Sesi sonradan, başka hiçbir şeye dokunmadan değiştir:

```bash
python ses_degistir.py new_voice.mp3 intro
```

Render edilen bölümleri tek videoda birleştir:

```bash
python birlestir.py full_video.mp4
```

Opsiyonel ortam değişkenleri:

| Değişken | Etkisi |
| :--- | :--- |
| `CHROME_PATH` | Otomatik arama yerine belirli bir Chrome/Chromium ikilisi kullanır |
| `ERKO_DELIVER_DIR` | Biten MP4'ün bir kopyasını bu klasöre de bırakır (örn. masaüstü) |

### Depo düzeni

```
.
├── SKILL.md                  # ajan becerisi: 20 altın kural + üretim iş akışı
├── docs/
│   └── LESSONS-LEARNED.md    # kare incelemelerinden çıkan dersler (EN + TR orijinal)
├── examples/
│   ├── intro_bomba_animation.html    # 19,5 sn intro şablonu (damgalar, Clawd, geçiş)
│   ├── chapter_01_animation.html     # bölüm şablonu (stüdyo + kâğıt/siber sahneler)
│   └── trailer/                      # README demosunun tanıtımı + ses değiştirme rehberi
├── resources/
│   ├── clawd_assistant.js    # asistan rig: drawClawd / drawEmote / geçişler
│   ├── fonts/                # 17 font dosyası + LICENSES.md + OFL.txt
│   ├── pure_poses/           # 13 normalize poz (700×780, kilitli taban çizgileri)
│   ├── Fredoka-Bold.ttf, JetBrainsMono-Bold.ttf
│   ├── studio_background_1080p.jpg
│   └── slate_chalkboard_1080p.png
├── scripts/
│   ├── build_audio_with_sfx.py       # ses -> SFX miks + zarf (numpy)
│   ├── build_audio_and_envelope.py   # stdlib hattı: stereo miks + ambiyans
│   ├── render_video.js               # canvas -> 1080p MP4 (Chrome + FFmpeg)
│   ├── ses_degistir.py               # tek komutla ses değiştirme
│   └── birlestir.py                  # kayıpsız bölüm birleştirme
└── assets/                   # demo video, GIF, storyboard
```

### Kurallar tarzı belirler

Bu motorun ruhu `SKILL.md`: her render'ı tutarlı tutan 20 altın kural — sprite'larda yüze sıfır müdahale, sahne başına tek sabit poz, tahtada native poligon kırpma, keski uçlu fosforlu yıkama, damga disiplini, kamera snap-zoom'ları, zorunlu 15 saniyelik kanca formülü, "Doğal Tebeşir & Sıcak Amber" tipografi hiyerarşisi ve gerçek render'lardan sonra yasaklanan anti-desenler.

`docs/LESSONS-LEARNED.md` kare incelemelerinde yakalanan somut hataları — kesilen harfleri, senkronsuz tahtaları, yanlış butondaki imleçleri — ve her birinin çözümünü toplar. İlk gerçek videonuzdan önce okuyun.

### Lisans

- **Kod ve paketlenmiş varlıklar:** MIT — bkz. [LICENSE](LICENSE).
- **Fontlar:** SIL Open Font License 1.1 — bkz. [resources/fonts/LICENSES.md](resources/fonts/LICENSES.md).

### Emeği geçenler

- Görsel tarz: **ekomen77** anlatım formatı.
- Bu README'nin başındaki demo, bu motorun kendisiyle üretilmiştir.

---

## English

**[Türkçe](#türkçe) · English**

**Turn a voiceover into a ekomen77-style 1080p explainer video.** Studio whiteboards, chalk paper diagrams, dark decompiler terminals, evidence cards, ink stamps and YouTube UI overlays — rendered frame by frame with Headless Chrome + FFmpeg and synchronised to your voice with millisecond-accurate procedural SFX.

Works as an **agent skill** (opencode / Claude / any coding agent) or as a plain CLI pipeline.

![Demo — 32-second trailer rendered 100% by the engine](assets/demo.gif)

**[▶ Watch the 32-second 1080p demo](assets/demo.mp4)** · **[Storyboard](assets/storyboard.jpg)** · **[Türkçe tanıtım](assets/demo_tr.mp4)**

### Highlights

- **20 battle-tested golden rules** (`SKILL.md`) distilled from real render iterations — typography, posing, lighting, stamps, camera work, anti-patterns.
- **13 normalised character poses** (`700×780`, locked baselines) + **Clawd**, the procedural hand-painted assistant rig (`drawClawd`, `drawEmote`, `drawBrushWipe`, `drawIris`).
- **19 bundled font files**, Turkish glyph coverage verified — all SIL OFL.
- **Two audio lanes**: a numpy-powered SFX mixer and a stdlib-only stereo mixer with cozy background ambience — both emit the same 30 fps RMS envelope.
- **Two production templates** (`intro_bomba`, `chapter_01`) plus the full studio/chalkboard archetype system described in `SKILL.md`.
- **Single-command voice swap** — replace the voiceover, re-mix and re-render in under 30 seconds.
- **The trailer's full source included** — `examples/trailer/`: re-render the demo with your own recorded voice in three commands.

### How it works

```
 voice.mp3 ─► build_audio_with_sfx.py ─► intro_audio_mix.wav + intro_envelope.json
               (48 kHz normalise,          (30 fps RMS envelope,
                procedural SFX)             timing data for the renderer)

 intro_animation.html ─► render_video.js ─► Headless Chrome (1920×1080)
   (Canvas timeline,       local HTTP server    │  JPEG frames over loopback
    window.renderAtTime)    + FFmpeg pipe        ▼
                                          FFmpeg (H.264 + AAC, faststart)
                                                     │
                                                     ▼
                                          out/intro_1080p.mp4
```

The engine runs a tiny local HTTP server, drives headless Chrome through the frame loop (`window.renderAtTime(t, amp)` → `canvas.toBlob` → POST), and pipes every JPEG straight into FFmpeg — no intermediate frames on disk — the 960-frame demo above rendered in about 65 seconds.

### Quickstart

#### Option A — install as an agent skill

```bash
npx skills@latest add ekomen77/erko-ai-video-engine
```

Then just ask your agent to produce a video (e.g. *"render an intro video for this voice file"*) — the skill teaches it the whole pipeline, rules and assets.

#### Option B — run the CLI yourself

Requirements: **Node 18+**, **FFmpeg** on `PATH`, **Chrome/Chromium** (auto-detected), **Python 3.8+** (numpy only needed for `build_audio_with_sfx.py`).

```bash
# 1) One flat project folder, e.g. my-video/
#    Copy from this repo (intro template example):
#      examples/intro_bomba_animation.html  ->  intro_animation.html
#      resources/fonts/Kalam-Bold.ttf, PatrickHand-Regular.ttf, JetBrainsMono-Bold.ttf
#      resources/clawd_assistant.js
#      resources/studio_background_1080p.jpg
#      resources/slate_chalkboard_1080p.png
#      resources/pure_poses/               ->  pure_poses/   (keep as subfolder)
#      scripts/*.py, scripts/render_video.js
#      your voice file: my_voice.mp3

# 2) Audio master + envelope
python build_audio_with_sfx.py my_voice.mp3 intro

# 3) Render the 1080p MP4
node render_video.js intro
# -> out/intro_1080p.mp4  (+ still_*.jpg preview frames)
```

Swap the voice later without touching anything else:

```bash
python ses_degistir.py new_voice.mp3 intro
```

Merge rendered chapters into one full video:

```bash
python birlestir.py full_video.mp4
```

Optional environment variables:

| Variable | Effect |
| :--- | :--- |
| `CHROME_PATH` | Use a specific Chrome/Chromium binary instead of auto-detection |
| `ERKO_DELIVER_DIR` | An extra folder (e.g. your Desktop) that also receives the finished MP4 |

### Repository layout

```
.
├── SKILL.md                  # the agent skill: 20 golden rules + production workflow
├── docs/
│   └── LESSONS-LEARNED.md    # hard-won frame-review lessons (EN + TR original)
├── examples/
│   ├── intro_bomba_animation.html    # 19.5s intro template (stamps, Clawd, fade)
│   ├── chapter_01_animation.html     # chapter template (studio + paper/cyber scenes)
│   └── trailer/                      # the 32s README demo trailer + voiceover swap guide
├── resources/
│   ├── clawd_assistant.js    # assistant rig: drawClawd / drawEmote / transitions
│   ├── fonts/                # 17 font files + LICENSES.md + OFL.txt
│   ├── pure_poses/           # 13 normalised poses (700×780, locked baselines)
│   ├── Fredoka-Bold.ttf, JetBrainsMono-Bold.ttf
│   ├── studio_background_1080p.jpg
│   └── slate_chalkboard_1080p.png
├── scripts/
│   ├── build_audio_with_sfx.py       # voice -> SFX mix + envelope (numpy)
│   ├── build_audio_and_envelope.py   # stdlib lane: stereo mix + ambience
│   ├── render_video.js               # canvas -> 1080p MP4 (Chrome + FFmpeg)
│   ├── ses_degistir.py               # one-command voice swap
│   └── birlestir.py                  # lossless chapter merge
└── assets/                   # demo video, GIF, storyboard
```

### The rules make the style

The soul of this engine is `SKILL.md`: 20 golden rules that keep every render consistent — zero face modification on sprites, one steady pose per scene, native whiteboard polygon clipping, chisel-tip highlighter washes, rubber-stamp discipline, camera snap-zooms, the mandatory 15-second hook formula, the "Doğal Tebeşir & Sıcak Amber" typography hierarchy, and the anti-patterns that were banned after real renders.

`docs/LESSONS-LEARNED.md` collects the concrete mistakes caught in frame reviews — cut letters, unsynced boards, cursors on the wrong button — and the fix for each. Read it before your first real video.

### License

- **Code and bundled assets:** MIT — see [LICENSE](LICENSE).
- **Fonts:** SIL Open Font License 1.1 — see [resources/fonts/LICENSES.md](resources/fonts/LICENSES.md).

### Credits

- Visual style: the **ekomen77** explainer format.
- The demo at the top of this README was produced with this engine itself.
