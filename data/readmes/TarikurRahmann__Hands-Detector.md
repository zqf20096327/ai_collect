<div align="center">
  <h1>🖐️ Hands Detector | Real-Time Hand Landmark Tracking</h1>
  <p>High-precision MediaPipe & OpenCV computer vision pipeline for multi-hand tracking.</p>
  <p>
    <a href="https://www.python.org/">
      <img src="https://img.shields.io/badge/Python-3.12+-blue?style=flat&logo=python" alt="Python 3.12+" />
    </a>
    <a href="https://opencv.org/">
      <img src="https://img.shields.io/badge/OpenCV-4.x+-blue?style=flat&logo=opencv" alt="OpenCV 4.x+" />
    </a>
    <a href="https://developers.google.com/mediapipe">
      <img src="https://img.shields.io/badge/MediaPipe-✅-blue?style=flat&logo=google" alt="MediaPipe" />
    </a>
    <a href="/LICENSE">
      <img src="https://img.shields.io/badge/License-MIT-green?style=flat" alt="MIT License" />
    </a>
    <a href="#-open-source-collaboration--call-for-contributors">
      <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen?style=flat" alt="PRs Welcome" />
    </a>
  </p>
</div>

---

## 🌟 Overview & Quick Summary

`Hands_detector` tracks 21 hand landmarks in real time using a MediaPipe-based `HandDetector`. It estimates Left vs. Right hands, overlays visual labels, and auto-resolves between local video files and live webcam sources.

---

## 🔥 Key Features

- 🎥 **Smart Video Source Resolver**
  - Searches `hands.mp4`, `video/hands.mp4`, or a CLI-provided video path
  - Falls back to `Webcam 0` when no file source is available
- 🤚 **21-Landmark Skeleton Tracking**
  - Detects and renders hand joints with cvzone/MediaPipe-style precision
- 🧭 **Spatial Orientation Estimation**
  - Classifies Left vs. Right hands using detected hand type or center position
- 🖼️ **Real-time Visual Overlay**
  - Displays hand labels and landmark visualization in a live OpenCV window

---

## 🛠️ Tech Stack & Dependencies

- Python 3.12+
- OpenCV
- cvzone

Install dependencies:

```powershell
pip install opencv-python cvzone
```

---

## 🚀 How to Run Locally

```powershell
git clone https://github.com/tarikurrahmanbd/YOLO_Projects-main.git
cd YOLO_Projects-main/Hands_detector
pip install opencv-python cvzone
python Hands_detector.py
```

---

## 👨‍💻 Developer & Lead Engineer

<div align="center">
  <strong>Tarikur Rahman</strong><br>
  Computer Vision Engineer | AI & Robotics Developer<br>
  <a href="https://github.com/TarikurRahmanBD">
    <img src="https://img.shields.io/badge/GitHub-TarikurRahmanBD-181717?style=flat&logo=github" alt="GitHub Profile" />
  </a>
</div>

---

## 🤝 Open-Source Collaboration & Call for Contributors

Contributions are welcome for advanced features such as:

- Gesture Recognition
- Virtual Mouse Control
- Sign Language Translation
- AR/VR Controls

---

## 📄 License & Attribution

This project is licensed under the **MIT License**.

**Designed and developed with ❤️ by Tarikur Rahman**
