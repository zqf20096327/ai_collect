# 🧠 Distraction Monitor — AI-Powered Attention Tracker

> **Stop doomscrolling. Start focusing.**  
> A real-time AI system that detects short-form content (YouTube Shorts, Instagram Reels) on your screen and alerts you before your productivity disappears.

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-orange?style=flat-square&logo=tensorflow)
![Flask](https://img.shields.io/badge/Backend-Flask-black?style=flat-square&logo=flask)
![CI](https://github.com/PRABHUSIDDARTH/distraction-monitor-v1/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![AICTE Capstone](https://img.shields.io/badge/AICTE-Capstone%20Project-purple?style=flat-square)

---

## 🚨 The Problem

Short-form video platforms are engineered to hijack attention. The average user spends **2+ hours/day** on Reels and Shorts — often without realizing it. Existing tools like screen time trackers are passive and manual. There's no system that **actively detects** what you're watching and intervenes in real time.

---

## ✅ The Solution

Distraction Monitor uses a **custom-trained CNN model** to classify your screen content every few seconds. The moment it detects a Short or Reel, it increments a counter. Once you hit your self-set threshold — it alerts you. No app store. No subscriptions. Just Python, running locally.

---

## 🎯 Key Features

- 🔍 **Real-time screen monitoring** using `mss` screen capture
- 🤖 **CNN classifier** trained on custom dataset: `short`, `reel`, `non_short`
- 🔔 **Threshold-based alerts** — visual + audio notifications
- 📊 **Live web dashboard** — view distraction count, set threshold, start/stop monitoring
- ⚙️ **Adjustable interval** — control how frequently the screen is scanned
- �� **100% validation accuracy** on custom dataset (10 epochs)

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| ML Model | TensorFlow / Keras (CNN) |
| Screen Capture | MSS |
| Image Processing | PIL + NumPy |
| Backend | Flask (Python) |
| Frontend | HTML, CSS, JavaScript |
| Model Format | `.keras` |
| Linting | Ruff |
| Testing | pytest |
| CI | GitHub Actions |

---

## 🧬 Model Architecture

```
Input Image (resized + normalized)
       ↓
   Conv2D Layer
       ↓
  MaxPooling2D
       ↓
   Dense Layer
       ↓
Softmax Output → [non_short, reel, short]
```

- **Loss Function:** Categorical Crossentropy  
- **Optimizer:** Adam  
- **Epochs:** 10  
- **Validation Accuracy:** ~100%  
- **Dataset:** Custom-curated screenshots manually labeled into 3 classes

---

## ⚙️ How It Works

```
Screen Captured (every N seconds via mss)
        ↓
Image Preprocessed (resize → normalize)
        ↓
CNN Model Predicts Class
        ↓
  ┌─────────────────────┐
  │  short / reel?      │──→ Counter++
  │  non_short?         │──→ No action
  └─────────────────────┘
        ↓
Counter >= Threshold?
        ↓
   🔔 Alert Triggered (visual + audio)
```

---

## 📁 Project Structure

```
distraction-monitor-v1/
├── backend/
│   ├── app.py              # Flask backend + monitoring logic
│   ├── screen_capture.py   # Dataset collection helper
│   ├── test_model.py       # Quick model sanity check script
│   ├── dataset/            # Training screenshots (short / reel / non_short)
│   └── Dockerfile          # Backend container image
├── frontend/
│   ├── index.html          # Web dashboard UI
│   ├── style.css           # Frontend styles
│   ├── script.js           # Frontend logic
│   └── Dockerfile          # Standalone nginx frontend image
├── model/                  # ⚠️  Place distraction_meter_model.keras here (not tracked)
├── docs/                   # Additional documentation
├── tests/
│   ├── conftest.py         # Pytest fixtures / mocks
│   └── test_api.py         # Smoke tests for API endpoints
├── Outputs/                # Sample output screenshots
├── docker-compose.yml      # One-command startup
├── .env.example            # Environment variable reference
├── pyproject.toml          # Ruff + pytest config
├── requirements.txt        # Python dependencies
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI (lint + tests)
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

| Tool | Version |
|---|---|
| Python | 3.10+ |
| pip | latest |
| Docker + Docker Compose | optional, for containerised run |

> **Model required:** The trained `.keras` model is not included in the repo (large binary).  
> Place it at `model/distraction_meter_model.keras` before starting the server.

### 1 — Clone & configure

```bash
git clone https://github.com/PRABHUSIDDARTH/distraction-monitor-v1.git
cd distraction-monitor-v1

# Copy the environment variable template and adjust if needed
cp .env.example .env
```

### 2 — Install dependencies

```bash
pip install -r requirements.txt
```

### 3 — Run locally

```bash
cd backend
python app.py
```

Open your browser at **http://localhost:5000**

---

## 🐳 Docker Quickstart

```bash
# Build and start the backend (serves frontend at http://localhost:5000)
docker compose up --build

# Stop
docker compose down
```

> The `model/` directory is volume-mounted read-only into the container.  
> Make sure `model/distraction_meter_model.keras` exists before running.

To build images manually:

```bash
# Backend image (serves both API and frontend)
docker build -f backend/Dockerfile -t distraction-monitor-backend .

# Standalone frontend image (nginx, optional)
docker build -f frontend/Dockerfile -t distraction-monitor-frontend .
```

---

## 🔧 Environment Variables

Copy `.env.example` to `.env` and adjust as needed:

| Variable | Default | Description |
|---|---|---|
| `FLASK_PORT` | `5000` | Port the Flask server listens on |
| `FLASK_DEBUG` | `0` | `1` = debug mode (never use in prod) |
| `MODEL_PATH` | `../model/distraction_meter_model.keras` | Path to the `.keras` model (relative to `backend/`) |
| `MONITOR_INTERVAL` | `5` | Seconds between screen captures |

---

## 🧪 Running Tests

Tests mock TensorFlow and MSS so they run without a GPU or display.

```bash
# Install test/lint dependencies (if not already done)
pip install pytest ruff

# Run all tests
pytest tests/ -v

# Lint
ruff check backend/ tests/
```

---

## 🔮 Future Scope

- 🎙️ Sound-based detection for audio recognition of Reels
- 📱 Android/iOS mobile deployment
- 🧬 Biometric attention tracking (eye gaze)
- 🚫 Auto-block distraction apps post-threshold
- 🌐 Browser extension version (Chrome/Edge)

---

## 👨‍💻 Author

**Prabhu Siddarth A V**  
B.Tech Information Technology — Sri Shakthi Institute of Engineering and Technology, Coimbatore  
AICTE Capstone Project | Azure AI Virtual Internship

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/prabhu-siddarth-157a00338/)
[![GitHub](https://img.shields.io/badge/GitHub-PRABHUSIDDARTH-black?style=flat-square&logo=github)](https://github.com/PRABHUSIDDARTH)
[![YouTube](https://img.shields.io/badge/YouTube-psthetech-red?style=flat-square&logo=youtube)](https://www.youtube.com/@psthetech)

---

## 📄 License

MIT License — feel free to use, modify, and distribute with attribution.

---

> ⭐ If this helped you reclaim your focus, give it a star!
