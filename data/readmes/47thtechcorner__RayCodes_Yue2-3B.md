<div align="center">
  <a href="https://youtu.be/nvYxy_4t3Zw">
    <img src="https://img.youtube.com/vi/nvYxy_4t3Zw/0.jpg" alt="YuE2-3B Destroys Suno: Full Music Generation on 4GB GPU!">
  </a>
  <h3>📺 <a href="https://youtu.be/nvYxy_4t3Zw">Watch the full tutorial on YouTube</a></h3>
</div>

# 🎵 Yue2-3B Tweet Songwriter

An autonomous AI music generator that turns live social media posts into complete 48kHz stereo radio songs and audio promos using local YuE2-3B audio models.

| Step 1: Input | Step 2: AI Action | Step 3: Result |
| :--- | :--- | :--- |
| Paste any trending post text | YuE2-3B plans lyrics, tempo & melody notes | Instant 48kHz stereo radio song MP3 |

---

## ⚡ Quick Setup & Download

Run this single PowerShell command to install dependencies and download the YuE2-3B model directly into your local `models/` directory:

```powershell
pip install ctransformers colorama; mkdir -Force models; curl -L -o models/yue2-3b-q4_0.gguf https://huggingface.co/audio-cpp/Yue2-3B-GGUF/resolve/main/yue2-3b-q4_0.gguf
```

---

## 🚀 How to Run

Register the local model weight into Ollama (optional):

```powershell
ollama create yue2-3b -f Modelfile
```

Run the AI Song pipeline:

```powershell
python main.py "AI agents are now coding entire web apps while developers sip coffee on the beach ☕"
```

---

## 🎼 AI Song Lyrics & Style

### [Verse]
Attention listeners! AI agents are now coding entire web apps while developers sip coffee on the beach!

### [Chorus]
From a single tweet to a 5-second broadcast sound, YuE2-3B brings the newest rhythm around!

---

## 🛠️ Project Structure

```
Yue2-3B/
├── main.py
├── Modelfile
└── README.md
```

---

## 💡 Tech Stack

- **Audio AI Model**: YuE2-3B (3.0 Billion Parameter AR-NAR Mixture-of-Transformers)
- **Quantization Engine**: Low-VRAM 4GB Mode (2.67 GB Compressed Weights)
- **Audio Output**: 48 kHz Stereo MP3 Latent Flow Matching (`outputs/song.mp3`)
- **Language & Runtime**: Python 3.10+ / Ollama C++ Backend

---

## 🌟 5 Practical Use Cases

1. **Viral Social Radio Song**: Create instant customized radio jingles for viral social media campaigns.
2. **Podcast Broadcast Intro**: Produce unique radio-style broadcast promos matched to podcast episode topics.
3. **Indie Game Soundtracks**: Generate thematic song clips from written game lore descriptions.
4. **Personalized Radio Greetings**: Turn heartfelt social posts into personalized radio song audio clips.
5. **Content Creator Jingles**: Craft signature channel radio songs directly from top community comment threads.

---

## 🔮 5 Future Features

1. **Multi-Voice Duets**: Support dual vocal song generation for male and female presenters.
2. **Interactive Audio Visualizer**: Render real-time 3D sound waves alongside generated radio songs.
3. **MIDI Score Exporter**: Export raw MIDI tracks to edit inside digital audio workstations (DAWs).
4. **Genre Auto-Tuning**: Automatically detect the best matching musical genre from social hashtag trends.
5. **Live Stream Integration**: Process live twitch chat commands into continuous real-time radio songs.

---

### 🏷️ Keywords
`YuE2-3B` `YuE2` `AI Music Generator` `Audio Generation` `Suno v5 Alternative` `Open Source Music AI` `Ollama` `audio.cpp` `4GB VRAM GPU` `Tweet to Song` `GGUF Audio`
