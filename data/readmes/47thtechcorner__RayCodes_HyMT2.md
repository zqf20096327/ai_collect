<div align="center">
  <a href="https://youtu.be/z1E6h2Rc-j0">
    <img src="https://img.youtube.com/vi/z1E6h2Rc-j0/0.jpg" alt="Destroys Google Translate? Tencent’s New 440MB AI Runs 100% Offline (Hy-MT2 Review)">
  </a>
  <h3>📺 <a href="https://youtu.be/z1E6h2Rc-j0">Watch the full tutorial on YouTube</a></h3>
</div>

---

# 🎬 Hy-MT2 Subtitle Translator

An offline machine translation tool powered by **Tencent Hy-MT2 1.8B Q4_K_M GGUF** that translates video SRT subtitle files across 33 languages while preserving exact timestamp bounds, sequence formatting, and terminology rules.

| 📥 Step 1: Input | ⚡ Step 2: AI Action | 📤 Step 3: Result |
| :--- | :--- | :--- |
| Load English `.srt` video subtitle file from `inputs/` directory. | Hy-MT2 1.8B GGUF model translates text while locking timestamps. | Frame-perfect translated `.srt` subtitles exported to `outputs/` folder. |

---

## 🛠️ Tech Stack & Requirements

- **Translation Engine**: Tencent Hy-MT2 1.8B Q4_K_M GGUF (`Hy-MT2-1.8B-Q4_K_M.gguf` via Ollama)
- **Model Source**: [Tencent Hy-MT2 1.8B GGUF on Hugging Face](https://huggingface.co/tencent/Hy-MT2-1.8B-GGUF/blob/main/Hy-MT2-1.8B-Q4_K_M.gguf)
- **Runtime Environment**: Python 3.10+ & Ollama
- **Supported Formats**: SRT Video Subtitle Files, JSON, Plain Text
- **Languages Supported**: 33 Languages (English, Hindi, Spanish, French, German, Japanese, etc.)

---

## ⚡ Quick Start & GGUF Model Setup

### 1. Download GGUF Model Weights

Download the official `Hy-MT2-1.8B-Q4_K_M.gguf` file into the `models/` directory:

```powershell
mkdir models -Force
Invoke-WebRequest -Uri "https://huggingface.co/tencent/Hy-MT2-1.8B-GGUF/resolve/main/Hy-MT2-1.8B-Q4_K_M.gguf" -OutFile "models/Hy-MT2-1.8B-Q4_K_M.gguf"
```

*(Alternatively, download manually from [Hugging Face Hy-MT2-1.8B-GGUF](https://huggingface.co/tencent/Hy-MT2-1.8B-GGUF/blob/main/Hy-MT2-1.8B-Q4_K_M.gguf) and place the file in `models/Hy-MT2-1.8B-Q4_K_M.gguf`)*

### 2. Modelfile Configuration

The root `Modelfile` is pre-configured for the `Hy-MT2-1.8B-Q4_K_M.gguf` weight file:

```text
FROM ./models/Hy-MT2-1.8B-Q4_K_M.gguf

PARAMETER temperature 0.7
PARAMETER top_p 0.6
PARAMETER top_k 20
PARAMETER repetition_penalty 1.05
PARAMETER num_predict 4096
```

### 3. Register GGUF Model in Ollama

Run this command in PowerShell to build and register the model tag in local Ollama:

```powershell
ollama create hy-mt2-1.8b-q4 -f Modelfile
```

---

## 🚀 Running the Translator

To run batch translation into Hindi and Spanish using the local `hy-mt2-1.8b-q4` GGUF model:

```powershell
python main.py --input inputs/subtitles_en.srt --model hy-mt2-1.8b-q4
```

To translate into a specific language (e.g., Hindi):

```powershell
python main.py --input inputs/subtitles_en.srt --lang Hindi --code hi --model hy-mt2-1.8b-q4
```

To translate into Spanish:

```powershell
python main.py --input inputs/subtitles_en.srt --lang Spanish --code es --model hy-mt2-1.8b-q4
```

---

## 📁 Repository Structure

```text
.
├── inputs/
│   └── subtitles_en.srt
├── models/
│   └── Hy-MT2-1.8B-Q4_K_M.gguf
├── outputs/
│   ├── subtitles_hi.srt
│   ├── subtitles_es.srt
│   └── metrics.md
├── main.py
├── Modelfile
├── requirements.txt
└── README.md
```

### File Explanations
- `main.py`: Core Python script that parses SRT structure, queries `hy-mt2-1.8b-q4` via Ollama, and exports localized `.srt` files and `metrics.md`.
- `Modelfile`: Configures token sampling parameters and points to `./models/Hy-MT2-1.8B-Q4_K_M.gguf`.
- `inputs/subtitles_en.srt`: Input video subtitle file containing timing bounds and text blocks.
- `outputs/metrics.md`: Automatically generated performance and execution metrics report.

---

## 🌟 5 Practical Use Cases

1. **Automated YouTube Video Localization**: Offline translation of video subtitle scripts for global YouTube channel reach.
2. **Software UI File Translation**: Translates user-facing JSON UI values while preserving code key names and placeholders.
3. **Markdown Documentation Engine**: Translates GitHub project README files without breaking markdown tables or code syntax.
4. **Offline Desktop Subtitle Helper**: Runs locally on low-spec PCs without internet connectivity using ~1.15GB VRAM/RAM.
5. **Private Enterprise Document Translation**: Translates sensitive business documents locally with zero cloud data transmission.

---

## 🔮 5 Future Enhancements

1. **Automatic VTT & ASS Format Support**: Expand subtitle parser to support WebVTT and Advanced SubStation Alpha formats.
2. **Audio Waveform Auto-Alignment**: Integrate Whisper automatic speech recognition to re-time shifted subtitle blocks.
3. **GUI Desktop Dashboard**: Build a drag-and-drop desktop application interface for batch video translation.
4. **Multi-Speaker Diarization Tagging**: Identify speaker tags (`[Speaker 1]`) and maintain distinct translation styles per speaker.
5. **Real-Time Live Video Overlay**: Translate live video streams in real-time with zero-latency sub-second subtitle rendering.

---

## 🔑 SEO Keywords & Search Tags

`tencent-hymt2` · `hy-mt2-1.8b` · `offline-ai-translation` · `ollama-gguf` · `srt-subtitle-translator` · `angelslim-stq` · `local-machine-translation` · `wmt26-translation` · `low-vram-ai` · `python-srt-parser`
