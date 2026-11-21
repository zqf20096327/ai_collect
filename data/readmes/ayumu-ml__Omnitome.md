<p align="center">
  <img src="assets/app-icon-1024.png" width="140" alt="Omnitome Logo" />
</p>

<h1 align="center">Omnitome</h1>

<p align="center">
  <strong>A Local-First Neural Reading System with Loss-Bounded Semantic Compression, Deterministic Vector Provenance, and On-Device Speech Synthesis.</strong>
</p>

<p align="center">
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-AGPL--3.0-blue.svg" alt="License: AGPL-3.0" /></a>
  <a href="https://github.com/ayumu-ml/Omnitome/releases/latest"><img src="https://img.shields.io/badge/Release-v1.1.2%20Stable-0052CC" alt="Release: v1.1.2 Stable" /></a>
  <img src="https://img.shields.io/badge/Platform-Windows%20x64-lightgrey" alt="Platform: Windows x64" />
  <img src="https://img.shields.io/badge/Tauri-v2.0%20(Rust)-FFC131?logo=tauri&logoColor=black" alt="Tauri v2" />
  <img src="https://img.shields.io/badge/Orchestrator-Node.js%2022%20LTS-339933?logo=node.js&logoColor=white" alt="Node.js 22 LTS" />
  <img src="https://img.shields.io/badge/Sidecar-PyTorch%20FP16%20CUDA-3776AB?logo=python&logoColor=white" alt="PyTorch FP16 CUDA" />
  <img src="https://img.shields.io/badge/Tests-61%20Unit%20%7C%2017%20Rust%20%7C%2010%2F10%20Corpus-3fb950" alt="Test Suites Pass" />
</p>

<p align="center">
  <a href="https://github.com/ayumu-ml/Omnitome/releases/latest">
    <img src="https://img.shields.io/badge/Download_Omnitome_v1.1.2-Windows_x64_(1.82_GB)-0078D4?style=for-the-badge&logo=windows&logoColor=white" alt="Download Omnitome v1.1.2 for Windows" />
  </a>
  <a href="https://youtu.be/Nmb-qiZpnrk">
    <img src="https://img.shields.io/badge/Watch_Demo-3:44_Master_Walkthrough-E0245E?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch Demo" />
  </a>
  <a href="https://github.com/ayumu-ml/Omnitome/wiki">
    <img src="https://img.shields.io/badge/Documentation-GitHub_Wiki-6f42c1?style=for-the-badge&logo=gitbook&logoColor=white" alt="Omnitome Wiki" />
  </a>
</p>

---

## Why We Built Omnitome: The 4,000-Chapter Problem

Omnitome was born out of a very specific, deeply human frustration.

If you have ever followed a sprawling 4,000-chapter web novel or tackled a 1,000-page distributed systems textbook, you know the feeling. You love the world, the characters, or the subject enough to endure the drag. But between the brilliant tactical battles or core architectural theorems, you are forced to wade through thousands of paragraphs where characters repeat insults for the sixth time, restate facts you learned fifty chapters ago, or engage in circular monologues. Roughly 80% is filler.

Conventional AI summarizers offer an awful bargain: *"Hand over the experience, and we will give you the gist."*

They flatten the narrative into generic bullet points. In fiction, they tell you a hero fought a rival and won, omitting the exact tactical insight that made the battle meaningful. In technical literature, they strip out the mathematical premises that keep a conclusion from being dangerously misleading. Even worse, they hallucinate synthetic connective tissue that never existed in the source.

We did not want to swallow a dictionary just to read a story, but we also refused to accept hallucinated summaries. We wanted the core 20,000 words preserved with mathematical fidelity. 

That conviction became our core architectural thesis: **Loss-bounded semantic compression (~7:1 ratio), NOT summarization.**

And because we believe private reading should stay private, we engineered Omnitome on real, humble hardware: a standard consumer laptop powered by an AMD Ryzen 7 4800H and a 4GB NVIDIA RTX 3050 Laptop GPU. We had no enterprise server racks or infinite H100 clusters. That constraint forced ruthless engineering discipline:

- **The F65 Await Barrier:** When our Node.js ingestion pipeline initially tried to spawn thousands of unconstrained asynchronous promises, Node's heap exploded to a terrifying **14.6 GB RAM**, freezing the machine. We introduced a sequential await barrier that slashed peak RAM to **296 MB** (a 98% drop) while accelerating real-world ingestion by 30x.
- **The 4GB VRAM Governor:** BGE-M3 originally consumed 3,959 MiB VRAM in FP32, causing Windows to page memory over PCIe and taking two minutes to embed 16 chunks. Converting to FP16 CUDA and implementing the **F43 LifecycleManager** dropped active memory to 1,135 MB and reclaimed **3.2 GB of idle VRAM** via automatic model eviction, dropping 16-chunk embedding latency to **under 1 second**.

Competitors sell ephemeral summaries. Omnitome sells **traceable, navigable provenance**.

---

## How Omnitome Works in Practice (In Plain English)

If you've ever tried using generic cloud AI tools to "read" a book, you already know the disappointment: you upload a 400-page book, and the AI spits out six superficial bullet points like *"Chapter 4: Alice travels to the mountains and meets Bob."* They skip 90% of the book, ignore the mathematical formulas, erase character subtleties, and hallucinate details that were never there.

Omnitome takes a completely different, mathematically grounded approach called **Loss-Bounded Semantic Compression**:

```
 Raw Document               Ingestion & Clean                Dynamic Slicing                 Omni Reading Archive
 ┌──────────────┐          ┌───────────────────┐          ┌───────────────────┐          ┌────────────────────────┐
 │ • Clean PDF  │          │ Strips Headers,   │          │ Mathematically    │          │ 250–360 Words/Chapter  │
 │ • Dirty PDF  │ ───────► │ Footers, Artifacts│ ───────► │ Balanced Slices   │ ───────► │ (Dynamic Max 500 W)    │
 │ • EPUB/DOCX  │          │ & Circular Fluff  │          │ Across Whole Book │          │ 100% Clickable Citations│
 └──────────────┘          └───────────────────┘          └───────────────────┘          └────────────────────────┘
```

### 1. Ingestion of Any Document (Even "Dirty" Scans)
Drop in clean PDFs, scanned or "dirty" PDFs with misaligned OCR headers and footers, EPUBs, DOCX, Markdown, or raw TXT. Omnitome's local extraction pipeline isolates the true body text, cleans OCR artifacts, and strips repetitive filler without touching the original source prose.

### 2. Dynamic, Mathematically Balanced Word Slices
Instead of treating a book as disconnected chunks, Omnitome calculates dynamic, equally distributed semantic slices across the **entire length of your document**. It guarantees complete coverage from Page 1 to the final chapter—no chapters are dropped, no subplots are forgotten, and no technical arguments are skipped.

### 3. The 250–360 Word "Omni Chapter" Sweet Spot
Each slice is transformed into a dense, high-clarity **Omni Chapter**:
* **Target Word Count:** **250 to 360 words per chapter** (dynamically expanding up to a hard ceiling of **500 words** for dense technical formulas, mathematical derivations, or complex multi-character dialogues).
* **Why This Specific Range?** Based on cognitive reading retention research and working memory chunking limits (such as cognitive load theory and optimal reading speeds), ~300 words represents the ideal human focus threshold. You can absorb a complete, high-density chapter in under 90 seconds with 100% comprehension, allowing an entire 400-page book to be deeply internalized in a single afternoon.
* **Full Context Preserved:** Creative voice, conceptual depth, key mathematical equations, and tactical maneuvers are preserved—never flattened into generic summaries.

### 4. 100% Verifiable Provenance (The "Anti-Hallucination" Moat)
Every single synthesized sentence in an Omni Chapter carries an interactive, clickable citation badge (e.g., `[p12]`). Clicking any badge immediately brings up the verbatim source paragraph in the side-by-side Research Pane. If a claim cannot be verified against the source text, Omnitome flags it with a dotted underline as an ungrounded defect.

### 5. 100% Local & Private (Zero-Egress by Default)
* **Your Data Stays on Your Disk:** Your documents, reading history, notes, and vector embeddings are stored inside a local SQLite database (`storage/data.db`) on your machine. No telemetry logs, no cloud databases, and zero unconsented data sharing.
* **Bring Your Own Intelligence:** You have total freedom. Run 100% offline and air-gapped using local inference engines like **Ollama** (Local LLaMA, Mistral, Qwen) or **LM Studio**, or plug in your personal API keys for **OpenRouter**, Gemini, Claude, or OpenAI.

### 6. Hardware Requirements: Built for Real Consumer Hardware
You don't need a multi-thousand-dollar server rack to run Omnitome:
* **System RAM:** Light memory footprint! Thanks to the **F65 sequential await barrier**, Node's ingestion orchestrator runs comfortably capped at **~296 MB RAM** (down from 14.6 GB).
* **GPU / VRAM:** Minimum **4 GB VRAM** (e.g., NVIDIA GeForce RTX 3050 Laptop GPU or desktop equivalent). Omnitome uses FP16 CUDA for local BGE-M3 (1024d) vector search, BGE Reranker v2, and Kokoro-82M neural audio, with automatic idle VRAM eviction (**F43 LifecycleManager**) reclaiming 3.2 GB of GPU memory when idle.
* **Storage:** ~3 GB free disk space for the pre-packaged neural models and sidecar runtime.

---

## The Three Foundational Laws

Every pipeline and interface in Omnitome adheres to three inviolable operational laws:

1. **Law 1: Source is paper.** The original document is neutral, book-like, immutable ground truth. The system never mutates, rewrites, or deletes verbatim source text.
2. **Law 2: The lens is tinted.** Derived Omni representations are explicitly identified and calibrated to **250–360 words per chapter**.
3. **Law 3: Derivation never masquerades as source.** Every synthesized claim carries deterministic, clickable citations linking directly back to verbatim source paragraphs. Sentences lacking verified evidence are treated as defects, visually styled with muted ink and a subtle dotted underline.

---

## Interactive Visual Tour

### 1. Library Catalog & Dynamic Tag Filtering
Browse your local collection with instant format filters (Novels, Technical Documents, Web Articles), topic tags, procedural typographic cover art, and non-blocking background queue ingestion.

<p align="center">
  <img src="assets/tour/01_library_catalog.gif" alt="Omnitome Library Catalog and Book Dossier" width="840" style="border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);" />
</p>

### 2. Loss-Bounded Omni Reading & Kokoro Neural Narration
Read dense, loss-bounded chapters (~250–360 words) preserving every core theorem and argument, accompanied by on-device Kokoro-82M neural speech synthesis with synchronized sentence tracking.

<p align="center">
  <img src="assets/tour/02_omni_reading_tts.gif" alt="Omnitome Omni Reading Lens and Kokoro Neural Narration" width="840" style="border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);" />
</p>

### 3. Clickable Provenance & Attribution Badges
Hovering over any synthesized sentence reveals interactive attribution badges (`[p12]`). Clicking jumps directly to the verbatim supporting paragraph in the Original Research pane.

<p align="center">
  <img src="assets/tour/03_clickable_provenance.gif" alt="Interactive Provenance and Attribution Badges" width="840" style="border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);" />
</p>

### 4. Adaptive Reading Themes
Switch seamlessly across four sensory palettes calibrated for zero eye strain: **Spring Botanic** (crisp editorial parchment), **Coffee Archive** (warm mahogany sepia), **Sakura Petal** (delicate washi paper), and **Omni Arcane** (midnight obsidian with violet accents).

<p align="center">
  <img src="assets/tour/04_adaptive_themes.gif" alt="Omnitome Adaptive Reader Themes Montage" width="840" style="border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,0.15);" />
</p>

---

## System Architecture

Omnitome isolates state orchestration from neural compute and native desktop presentation:

```
┌─────────────────────────────────────────────────────────────────┐
│                 Tauri v2 Desktop Shell (Rust)                   │
│             Window Lifecycle & Child-Process Supervisor         │
└────────────────┬───────────────────────────────┬────────────────┘
                 │ Local Webview IPC             │ Supervises & Kills
                 ▼                               ▼
 ┌──────────────────────────────┐ ┌─────────────────────────────┐
 │ Node.js 22 LTS Orchestrator  │ │ FastAPI Python Sidecar      │
 │ • SOLE SQLite WAL writer     │ │ • BGE-M3 (FP16 CUDA)        │
 │ • Sequential Await Barrier   │ │ • BGE Reranker v2           │
 │ • Ingestion Queue Daemon     │ │ • Kokoro-82M Neural TTS     │
 │ • Peak RAM: ~296 MB          │ │ • Idle VRAM Eviction (3.2GB)│
 └──────────────┬───────────────┘ └──────────────┬──────────────┘
                │ HTTP REST                      │ HTTP REST
                ▼                                │
 ┌──────────────────────────────┐                │
 │ SQLite Database (data.db)    │◄───────────────┘ (REST via Node ONLY)
 │ Local WAL Mode               │
 └──────────────────────────────┘
```

### Empirical Performance Highlights

| Metric | Before Optimization | Current Architecture | Measured Impact |
| :--- | :--- | :--- | :---: |
| **508K-Word Book Ingestion** | Multi-hour projection | **~5.9 minutes** | **30x+ faster** |
| **Node.js Peak Memory Under Load** | 14.6 GB (unbounded promises) | **296 MB** (F65 await barrier) | **98% RAM reduction** |
| **BGE-M3 Active VRAM Footprint** | 3,959 MiB (FP32) | **1,135 MB** (FP16 CUDA) | **71% VRAM reduction** |
| **Idle VRAM After Model Eviction** | Permanently resident | **174 MB** (F43 LifecycleManager) | **3.2 GB reclaimed** |
| **16-Chunk Embedding Batch** | ~124 seconds (PCIe paging) | **< 1 second** | **120x+ speedup** |
| **Release Gate Corpus Verification** | n/a | **10/10 fixtures passed** | **1.23M words/sec** |

---

## Technical Documentation & Wiki

For exhaustive architectural deep dives, formal equations, and engineering post-mortems, explore the **[Omnitome GitHub Wiki](https://github.com/ayumu-ml/Omnitome/wiki)** (also mirrored locally in `docs/wiki/`):

- **[Architecture & Multi-Process Supervisor](https://github.com/ayumu-ml/Omnitome/wiki/Architecture-and-Multi-Process-Supervisor)** — Tauri v2 process management, ephemeral port discovery, clean process tree teardown (`taskkill /F /T`), and the Sole SQLite Writer invariant.
- **[Memory Invariants & VRAM Lifecycle](https://github.com/ayumu-ml/Omnitome/wiki/Memory-Invariants-and-VRAM-Lifecycle)** — Operating within 4 GB VRAM on consumer GPUs, the F65 Sequential Await Barrier, and sliding TTL model eviction.
- **[Semantic Compression & Attribution Engine](https://github.com/ayumu-ml/Omnitome/wiki/Semantic-Compression-and-Attribution-Engine)** — Mathematical compression bounds ($C_r \approx 7:1$), BGE-M3 vectorization, CJK multilingual token safety, and deterministic provenance scoring.
- **[Packaging & Windows Distribution](https://github.com/ayumu-ml/Omnitome/wiki/Packaging-and-Windows-Distribution)** — Bypassing the 32-bit NSIS 2 GB installer ceiling via LZMA `sidecar.7z` decompression, PyInstaller cuDNN DLL harvesting, and WebView2 audio unlock.

Additional specifications:
- [System Architecture Specification](./docs/ARCHITECTURE.md)
- [Empirical Benchmarks & Telemetry](./docs/BENCHMARKS.md)
- [Feature Catalog & Invariant Matrix](./docs/FEATURES.md)
- [The Making of Omnitome (Engineering Memoir)](./frontend/public/samples/md/The_Making_of_Omnitome.md)

---

## Quick Start (Windows x64)

1. **Download:** Grab the latest installer from [GitHub Releases](https://github.com/ayumu-ml/Omnitome/releases/latest) (`Omnitome_1.1.2_x64-setup.exe`, ~1.82 GB).
2. **Launch:** Run the installer. On first launch, the Welcome Wizard configures your local environment.
3. **Inference Setup:** Omnitome connects out-of-the-box with local runners like [Ollama](https://ollama.ai/) or [LM Studio](https://lmstudio.ai/) for 100% private offline reading, or with optional cloud API keys.
4. **Drop & Read:** Drag in any PDF, EPUB, DOCX, RTF, Markdown, or text file. Omnitome parses, indexes, and synthesizes traceable chapters in the background.

---

## Developer & Availability

**Ayush Sharma** — *AI Systems Engineer & Full-Stack Developer*

I specialize in bridging the gap between applied AI research (local LLMs, PyTorch, RAG architectures) and production desktop/web applications.

**Available for freelance and remote contract work:**
- Designing local-first AI pipelines (Ollama, LM Studio, PyTorch) with zero data egress.
- Architecting high-throughput RAG systems with deterministic provenance and vector search.
- Packaging complex multi-process AI engines into native desktop applications (Tauri v2, Electron).
- Optimizing GPU/VRAM performance and memory lifecycles for edge and consumer hardware.

[Connect with me on LinkedIn](https://www.linkedin.com/in/ayush-sharma-swe/)

---

## License

Omnitome is open-source software licensed under the **GNU Affero General Public License v3.0** ([AGPL-3.0-only](./LICENSE)).
