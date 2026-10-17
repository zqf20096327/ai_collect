# Portable AI

USB'den calisan, %100 offline, sifrelenmis AI asistan. Sohbet gecmisi ve dokumanlar
AES-256 ile, USB volume serial'ina bagli olarak sifrelenmis.

> "ChatGPT'nin yapamadigi sey: USB'ni cikar, hicbir veri arkanda kalmiyor."

---

## Neden bu var?

KVKK uyumlu kullanim icin cloud LLM'ler avukat / doktor / muhasebeci icin
felaket. ChatGPT alternatifi olmaktan cok, **veri sinirinda calisan AI** ihtiyaci
var: USB'yi takip cikariyorsun, sohbetler USB'de kaliyor, internet'e hicbir sey
gitmiyor.

Hedef:
- KVKK uyumu zorunlu olan profesyoneller (avukat, doktor, muhasebeci, gazeteci)
- Kapali ortamlarda calisan kurumlar (ozellikle kamu)
- Veri egemenligi cok kritik olan kullanicilar

---

## Ozellikler

- 🔒 **AES-256 sifreli sohbet gecmisi** — sqlcipher + passphrase + USB volume serial
- 📎 **RAG** — PDF / DOCX / TXT yukle, sohbette uzerinde konus
- 🎭 **9 hazir mod** — Genel, Avukat, Doktor, Muhasebeci, Muhendis, Ogretmen, Akademisyen, Yazar, Cevirmen
- 🧠 **Trendyol-LLM 7B** — Qwen2.5 7B uzerine 13B Turkce token continued pretraining
- 💾 **%100 offline** — internet gerekmez (ilk embedding download haric, sonrasinda kapali)
- 🔐 **USB binding** — DB calinsa baska USB'de acilmaz
- 📦 **PyInstaller bundle** — Python kurulu olmayan PC'de calisir

---

## Stack

| Katman | Teknoloji |
|---|---|
| LLM inference | `llama-cpp-python==0.2.90` (AVX2, AVX-512 yok) |
| Embeddings | `intfloat/multilingual-e5-small` (sentence-transformers) |
| Vector search | `numpy` brute-force (FAISS gerekmez, <10k chunk icin yeterli) |
| Encryption | `sqlcipher3` (AES-256), PBKDF2-SHA256 200k iter |
| Web framework | `FastAPI` + `uvicorn` |
| UI | Vanilla JS + SSE streaming (no React, no build step) |
| Document parsing | `pypdf` + `python-docx` |
| Package manager | `uv` (Astral) |
| Bundling | `PyInstaller --onedir` |

---

## Hizli baslangic (geliştirici icin)

### 1. uv kur

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

### 2. Repo

```powershell
git clone https://github.com/<sen>/portable-ai
cd portable-ai
copy .env.example .env
uv sync
```

`uv sync` su isleri yapar:
- Python 3.11 indirir
- venv olusturur
- `llama-cpp-python==0.2.90` (abetlen CPU index)
- `sqlcipher3>=0.6.2` (Windows wheel)
- `sentence-transformers` + `pypdf` + `python-docx`

İlk sync ~500 MB indirir.

### 3. Model indir

```powershell
uv run python scripts/download_model.py
```

Default: **Trendyol-LLM 7B Q4_K_M** (4.7 GB).

```powershell
# Listele
uv run python scripts/download_model.py --list

# Farkli model
uv run python scripts/download_model.py --model qwen-1.5b
```

### 4. Calistir

```powershell
uv run portable-ai
```

`http://127.0.0.1:8765` → ilk acilis: setup ekrani, passphrase belirle.

---

## USB build pipeline (Faz 3 + 4)

### Build (mevcut platformda)

```powershell
uv sync --extra dev      # PyInstaller dahil dev deps
uv run python scripts/build_release.py
```

Cikti platforma gore:
- Windows: `dist/portable-ai-win/`
- Linux: `dist/portable-ai-linux/`
- macOS: `dist/portable-ai-mac/`

Yaklasik boyut: ~500 MB / platform.

### Linux build — Docker ile (reproducible)

Ubuntu 20.04 base, glibc 2.31 uyumluluk:

```bash
docker build -t portable-ai-linux-builder .
docker run --rm -v "$(pwd)":/build portable-ai-linux-builder
```

Cikti: `dist/portable-ai-linux/`

### Cross-platform build — GitHub Actions

`v0.6.0` gibi bir tag push edin, otomatik 3 platform build alinir + release olusturulur:

```bash
git tag v0.6.0
git push origin v0.6.0
```

GitHub Actions workflow (`.github/workflows/build.yml`):
- Ubuntu 20.04 → `portable-ai-linux.tar.gz`
- Windows latest → `portable-ai-win.zip`
- macOS latest → `portable-ai-mac.tar.gz`

### USB hazirla

```powershell
# Sadece mevcut platform bundle'i
uv run python scripts/prepare_usb.py --target E:\

# Belirli platformlar
uv run python scripts/prepare_usb.py --target E:\ --platforms windows linux

# Tum mevcut bundle'lar (multi-boot USB)
uv run python scripts/prepare_usb.py --target E:\ --all-platforms
```

Otomatik kopyalanir:
- `portable-ai-<platform>/` — exe + dependencies
- `models/Trendyol-LLM-7B...gguf` (~4.7 GB)
- `models/embeddings/` (~470 MB, varsa)
- Platform-spesifik launcher (`start.bat` / `start.sh` / `start-mac.command`)
- `README.txt` — son kullanici kilavuzu
- `data/` — bos, runtime'da kullanilir

### Test — baska PC'de

- **Windows**: USB tak → `start.bat` cift tikla → Defender uyarisi cikarsa "Yine de calistir"
- **Linux**: Terminal → USB dizinine cd → `./start.sh` (executable degilse `chmod +x start.sh`)
- **macOS**: USB tak → `start-mac.command` cift tikla → Gatekeeper uyarisi cikarsa Sistem Ayarlari'ndan "Yine de Ac"

60-90 saniyede tarayici otomatik acilir.

---

## Proje yapisi

```
portable-ai/
├── pyproject.toml
├── entry.py                       # PyInstaller wrapper (package-aware import)
├── portable-ai.spec               # PyInstaller config
├── src/portable_ai/
│   ├── main.py                    # FastAPI entry + lifespan
│   ├── config.py                  # USB-relative path resolution
│   ├── auth.py                    # INITIAL/LOCKED/UNLOCKED state
│   ├── presets.py                 # 9 built-in conversation modes
│   ├── backends/
│   │   ├── base.py                # LLMBackend ABC
│   │   └── llama_cpp.py           # llama-cpp-python backend
│   ├── storage/
│   │   ├── crypto.py              # USB UUID detection + PBKDF2
│   │   ├── db.py                  # sqlcipher async wrapper + migrations
│   │   ├── conversations.py       # Chat CRUD + context window
│   │   └── documents.py           # RAG documents + chunks CRUD
│   ├── rag/
│   │   ├── embeddings.py          # e5-small singleton
│   │   ├── parser.py              # PDF/DOCX/TXT parser
│   │   ├── chunker.py             # Recursive char split (dep-free)
│   │   ├── index.py               # In-memory vector search
│   │   └── retrieval.py           # Ingest + query orchestration
│   └── web/
│       ├── routes.py              # API endpoints + SSE streaming
│       └── templates/index.html
├── scripts/
│   ├── download_model.py
│   ├── build_release.py           # PyInstaller orchestrator
│   └── prepare_usb.py             # USB packaging
├── tests/
└── models/                        # Gitignored (buyuk dosyalar)
```

---

## Mimari kararlar

### Neden FAISS degil numpy?

`faiss-cpu` Windows wheel'i sik sik MSVC ABI sorunlari yasiyor. Bizim use case
dokuman basina 50-500 chunk, toplam belki bir kac bin. numpy.dot ile:
- 384-dim × 10k chunk = ~1 ms brute force
- 100k chunk'a kadar yeterli

FAISS gercekten >100k vector icin gerekli, biz orada degiliz.

### Neden Trendyol 7B?

Test ettim:
- **Qwen 2.5 1.5B**: hizli ama TR kalitesi felaket, repetition + hallucination
- **Qwen 2.5 3B**: TR'de Cince/Japonca token leak (Q4 quantize sonrasi)
- **Llama 3.2 3B**: kendine "Sena" isim uydurdu, repetition loop
- **Trendyol 7B (Qwen2.5 base + 13B TR token CPT)**: temiz, akici, halusinasyon dusuk

Trade-off: 4.7 GB vs ~1-2 GB, hiz vs kalite. 7B kabul edilebilir.

### Neden `llama-cpp-python==0.2.90` pin?

0.3.x AOT weight repacking icin AVX-512 instruction kullaniyor. 12+ gen
Intel'de Intel AVX-512'yi consumer CPU'larda devre disi birakti
(P-core/E-core tutarsizligi). Bu yuzden i5-12600HX gibi yaygin CPU'larda 0.3.x
`STATUS_ILLEGAL_INSTRUCTION (0xc000001d)` ile patliyor. 0.2.90 AVX2 yeter, her
modern CPU calistirir.

### Neden PyInstaller `--onedir` (`--onefile` degil)?

| | onefile | onedir |
|---|---|---|
| Startup | 5-10 sn (extract) | 1-2 sn |
| AV false-positive | yuksek | dusuk |
| Boyut | ayni | ayni |

Hiz ve antivirus uyumlulugu icin `--onedir`.

### Neden in-memory passphrase?

Passphrase asla disk'e yazilmaz. Server lock olunca RAM'den temizlenir.
Unutursan veri kurtarilamaz — bilincli bir guvenlik karari.

---

## Bilinen sorunlar / Bilinen limitler

- **Windows Defender SmartScreen** imzasiz exe icin uyari verir → Faz 5'te code signing
- **macOS / Linux launcher** henuz yok → Faz 4
- **Taranan PDF** (resim layer'i) **calismaz** — OCR yok
- **DOCX**'te image, chart, comment cikariliyor (sadece text + tablo)
- **USB formatlanirsa** UUID degisir → eski DB acilmaz (bilincli, calinma korumasi)
- Trendyol 7B `temperature > 0.7`'de TR'de zayiflar

---

## Roadmap

- [x] **Faz 1**: FastAPI + llama-cpp-python + streaming UI
- [x] **Faz 2**: sqlcipher + USB UUID binding + conversation CRUD
- [x] **Faz 3**: PyInstaller bundle + USB packaging (Windows)
- [x] **Faz 6**: RAG (PDF/DOCX/TXT + e5 embeddings + numpy search)
- [x] **Faz 7**: Konusma presetleri (9 built-in mod)
- [ ] **Faz 4**: Multi-platform build (Linux, macOS) — **in progress**
- [ ] **Faz 5**: Code signing (Authenticode + Apple notarization)
- [ ] **Faz 7.5**: Custom preset olusturma UI
- [ ] **Faz 8**: Conversation export (Markdown / PDF)
- [ ] **Faz 9**: Search bar (sohbet gecmisinde arama)
- [ ] **Faz 10**: Recovery key export

---

## Troubleshooting

### `STATUS_ILLEGAL_INSTRUCTION (0xc000001d)`

llama-cpp-python AVX-512 kullaniyor, CPU desteklemiyor.
Cozum: `pyproject.toml`'da `llama-cpp-python==0.2.90` pin'lendi, repo
yeniyse `uv sync` ile gelir.

### sqlcipher kurulamadi

```powershell
uv pip install sqlcipher3-wheels
```

`db.py` ikisini de destekler.

### Embedding model ilk yukleme yavas

İlk dosya yuklediginde e5-small (470 MB) HuggingFace'ten cekiliyor. `prepare_usb.py`
local cache'i USB'ye kopyalar, baska PC'de indirme gerektirmez.

### Hybrid CPU (Intel 12+ gen) hiz optimizasyonu

`.env`'e ekle:

```env
N_THREADS=6   # P-core sayisi + 2
```

i5-12600HX (4 P-core) → 6, i7-12700H (6 P-core) → 8.

---

## Lisans

MIT — bkz `LICENSE`.

## Katkilar

Issue ve PR'lar kabul edilir. Buyuk degisikliklerden once issue ac.
