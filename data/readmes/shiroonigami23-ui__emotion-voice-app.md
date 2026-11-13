<div align="center">

<img src="visuals/app_ui/how_ai_sees_sound.png" alt="Speech Emotion Recognition Engine" width="85%">

# 🎙️ Speech Emotion Recognition Engine

### Deep-learning engine that hears emotion in voice — MFCC features, balanced data, 91.6 % validation accuracy

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white) ![Keras](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) ![scikit--learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE) ![Last commit](https://img.shields.io/github/last-commit/shiroonigami23-ui/emotion-voice-app?style=flat-square) ![Repo size](https://img.shields.io/github/repo-size/shiroonigami23-ui/emotion-voice-app?style=flat-square) ![Top language](https://img.shields.io/github/languages/top/shiroonigami23-ui/emotion-voice-app?style=flat-square) ![Status](https://img.shields.io/badge/status-active-blueviolet?style=flat-square)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/shiroonigami23-ui/emotion-voice-app?quickstart=1) [![Download ZIP](https://img.shields.io/badge/Download-ZIP-2ea44f?style=flat-square&logo=github)](https://github.com/shiroonigami23-ui/emotion-voice-app/archive/refs/heads/main.zip)

[**Overview**](#-overview) · [**Features**](#-features) · [**Architecture**](#-architecture) · [**Getting Started**](#-getting-started) · [**Roadmap**](#-roadmap)

</div>

---

## 📸 Preview

<p align="center"><img src="assets/showcase.gif" alt="Speech Emotion Recognition Engine showcase" width="85%"></p>

## 📖 Overview

A professional **speech emotion recognition** system. Audio is resampled and converted into **MFCC** and related spectral features with **Librosa**, then classified by a **dense neural network** trained on a **perfectly balanced dataset (496 samples per class)**. It reaches **91.6 % validation accuracy** with sub-100 ms inference and ships with a **Streamlit** scientific dashboard that shows how the AI "sees" sound and its thinking process.

### ✨ Highlights

- **91.6 %** validation accuracy
- **Balanced** training data — 496 samples per class
- **< 100 ms** inference
- **Explainable dashboard** — spectral views and model reasoning

## 🧩 Features

| Feature | What it does |
|---|---|
| **Feature extraction** | MFCC + spectral features with Librosa / Resampy |
| **DNN classifier** | TensorFlow 2.15 / Keras 3 |
| **Dashboard** | Streamlit app with visual explanations |
| **Reports** | Architecture, features and summary docs in `Documentation/` |
| **Evaluation** | Confusion matrix, classification report, training curves |

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Audio | Librosa, Resampy |
| Model | TensorFlow, Keras |
| Prep | scikit-learn, joblib |
| UI | Streamlit |

## 🏗 Architecture



```mermaid
flowchart LR
  A[Voice clip] --> R[Resample]
  R --> F[MFCC + spectral features]
  F --> SC[Scaler]
  SC --> DNN[Dense network]
  DNN --> E[Emotion + confidence]
  E --> UI[Streamlit dashboard]
```

➡️ Full design notes, data flow and design decisions: **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)**

## 📁 Project Structure

```text
emotion-voice-app/
├── app.py
├── Documentation/{technical,features,summary}.md
├── visuals/
└── requirements.txt · packages.txt
```

## 🚀 Getting Started

### 1. Get the code

Pick whichever method suits you:

| Method | Command |
|---|---|
| **HTTPS** | `git clone https://github.com/shiroonigami23-ui/emotion-voice-app.git` |
| **SSH** | `git clone git@github.com:shiroonigami23-ui/emotion-voice-app.git` |
| **GitHub CLI** | `gh repo clone shiroonigami23-ui/emotion-voice-app` |
| **ZIP** | [Download](https://github.com/shiroonigami23-ui/emotion-voice-app/archive/refs/heads/main.zip) and extract |
| **Codespaces** | [Open in browser](https://codespaces.new/shiroonigami23-ui/emotion-voice-app?quickstart=1) — zero local setup, dev container preconfigured |

> 🔑 **Using SSH for the first time?** Generate a key with `ssh-keygen -t ed25519 -C "you@example.com"`, add the `.pub` contents at **GitHub → Settings → SSH and GPG keys**, then test with `ssh -T git@github.com`.

### 2. Install & set up

```bash
cd emotion-voice-app
pip install -r requirements.txt
```

### 3. Run

```bash
streamlit run app.py
```
See [technical.md](Documentation/technical.md), [features.md](Documentation/features.md) and [summary.md](Documentation/summary.md).

## 🗺 Roadmap

**v1 (done)**

- [x] Balanced dataset, DNN, 91.6 % accuracy
- [x] Streamlit dashboard and reports

**v1.1**

- [ ] CNN/transformer on spectrograms (wav2vec2 baseline)
- [ ] Live microphone mode
- [ ] Cross-dataset testing (CREMA-D, TESS)

**v2.0**

- [ ] Merged into the multimodal app
- [ ] On-device model for Android

➡️ Detailed plan, milestones and long-term vision: **[docs/ROADMAP.md](docs/ROADMAP.md)**

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m "feat: add amazing feature"`
4. Push the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request against `main`

Check the [issues page](https://github.com/shiroonigami23-ui/emotion-voice-app/issues) and the [roadmap](docs/ROADMAP.md) for ideas on where to help.

## 📜 Changelog

See [CHANGELOG.md](CHANGELOG.md) for the release history.

## 📄 License

Distributed under the **MIT** license. See [LICENSE](LICENSE) for details.

## 👤 Author

**Aryan Singh Chandel** (Shiro)

[![GitHub](https://img.shields.io/badge/GitHub-shiroonigami23--ui-181717?style=flat-square&logo=github)](https://github.com/shiroonigami23-ui)

<div align="center">

⭐ **If you find this project useful, consider giving it a star!** ⭐

</div>
