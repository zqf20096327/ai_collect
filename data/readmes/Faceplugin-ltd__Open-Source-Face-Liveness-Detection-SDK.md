<p align="center">
  <a href="https://faceplugin.com/">
    <img src="https://raw.githubusercontent.com/Faceplugin-ltd/faceplugin-assets/main/brand/logo.png" alt="Faceplugin" width="300">
  </a>
</p>

<h1 align="center">Open Source Face Liveness Detection SDK</h1>

<p align="center">
  <b>A free and open-source face anti-spoofing (liveness detection) model for Windows and Linux from <a href="https://faceplugin.com/">Faceplugin</a></b>
</p>

<p align="center">
  <a href="https://github.com/Faceplugin-ltd/Open-Source-Face-Liveness-Detection-SDK"><img src="https://img.shields.io/badge/platform-Windows%20%7C%20Linux-blue.svg" alt="Platform"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="Python"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT--0-green.svg" alt="License: MIT-0"></a>
  <a href="https://faceplugin.com/"><img src="https://img.shields.io/badge/privacy-On--Premise%20Only-brightgreen.svg" alt="Privacy"></a>
</p>

---

## 🚀 Overview

The Open Source Face Liveness Detection SDK tells a **live face** apart from a **spoofed face** (a printed photo, a replayed video or a picture on a screen). It's built on a MobileNetV2 backbone with a lightweight classification head, so it runs fast on an ordinary CPU and drops easily into any Python project.

### ✨ Key Features

- 🔒 **100% On-Premise**: All processing happens locally, so no data leaves your device
- ⚡ **Lightweight**: A MobileNetV2-based model that runs in real time on the CPU
- 🔧 **Easy Integration**: One class, one weights file and two Python dependencies
- 🌐 **Cross-Platform**: Works on Windows and Linux
- 📱 **GPU Optional**: Runs entirely on the CPU, with no CUDA setup needed
- 📴 **Works Offline**: No downloads or internet connection needed at run time
- 🆓 **Completely Free**: MIT-0 licensed, free for commercial use with no attribution required

### 🎯 Current Capabilities

- Live vs. fake (spoof) classification from a single image
- A spoof score for every image, between 0 and 1
- Batch processing of every image in a folder
- Adjustable decision threshold
- Common image formats (JPG, JPEG, PNG, BMP)

## 🛠️ Installation

### Prerequisites

- Python 3.10 or newer (64-bit)
- Anaconda (recommended)
- Windows or Linux

### Setup

1. **Install Anaconda**
   Download it from [anaconda.com](https://www.anaconda.com/products/distribution).

2. **Create and activate a conda environment**
   ```bash
   conda create -n liveness python=3.10
   conda activate liveness
   ```

3. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the test**
   ```bash
   python main.py
   ```

## 📖 Quick Start

### Command Line

```bash
python main.py                                  # every image in the input folder
python main.py --input photo.jpg                # a single image
python main.py --input my_images --threshold 0.1  # 0.1 is the default
```

| Option | Default | Description |
|---|---|---|
| `--input` | `input` | An image file, or a folder of images |
| `--weights` | `weights/liveness.hdf5` | Path to the model weights |
| `--threshold` | `0.10` | Spoof scores above this are labeled **Fake** |

The default threshold is **0.1**, which you don't need to set. Lower it (e.g. `0.05`) to be stricter and catch more spoofs, or raise it to reject fewer real faces.

Example output:

```
Image                           Result  Spoof score
----------------------------------------------------
fake.jpg                        Fake    <score>
real.jpg                        Live    <score>
```

### Example: Use It in Your Own Code

```python
from liveness_detector import LivenessDetector

detector = LivenessDetector()                     # load the model once

result = detector.predict_file("input/real.jpg")
print(result.label, result.score)                 # e.g. Live 0.0123
```

Already have the image in memory (for example a webcam frame from OpenCV)? Pass it straight in:

```python
result = detector.predict(frame)                  # BGR image, as from cv2
if result.is_live:
    print("Live face")
```

## 🔧 API Reference

### `LivenessDetector(weights_path, threshold)`
Builds the network and loads the trained weights. Create it once and reuse it.
- **weights_path**: path to the weights file (default: `weights/liveness.hdf5`)
- **threshold**: spoof scores above this are labeled Fake (default: `0.10`)

### `detector.predict_file(image_path)`
Runs liveness detection on an image file.
- **Returns**: a `LivenessResult`, or `None` if the image can't be read

### `detector.predict(image_bgr)`
Runs liveness detection on an image already loaded in memory (a BGR NumPy array, as returned by `cv2.imread` or `cv2.VideoCapture`).
- **Returns**: a `LivenessResult`

### `LivenessResult`
- **score**: spoof score from 0 (live) to 1 (fake)
- **is_live**: `True` when the score is at or below the threshold
- **label**: `"Live"` or `"Fake"`

### Configuration

- **Decision rule**: an image is labeled **Fake** when its spoof score is above the threshold (default `0.10`), and **Live** otherwise
- **Input size**: images are resized to 224 × 224 RGB and scaled to the 0–1 range
- **Supported formats**: JPG, JPEG, PNG, BMP
- **Note**: the whole image is classified, and there's no face detection step

## 📁 Project Structure

```
├── liveness_detector.py                 # LivenessDetector class (the SDK)
├── main.py                              # Command-line demo
├── requirements.txt                     # Python dependencies
├── LICENSE                              # MIT No Attribution (MIT-0)
├── weights/
│   └── liveness.hdf5                    # Trained model weights
└── input/
    ├── fake.jpg                         # Sample spoof image
    └── real.jpg                         # Sample live image
```

## 🎯 Use Cases

- 🔐 **Security & Authentication**: Stop photo and video replay attacks at face login, access control and identity verification
- 🏦 **eKYC & Onboarding**: Make sure there's a real person in front of the camera during remote account opening
- 👥 **Business Applications**: Spoof-proof time and attendance systems and visitor check-in
- 📱 **Mobile & IoT**: Add a liveness check to smart devices, kiosks and mobile apps

## 🏢 More Biometric SDKs from Faceplugin

Faceplugin also offers commercial SDKs that go beyond this open-source project:

| | Solution | Description |
|---|---|---|
| 👤 | **Face Recognition** | Face detection, matching and identification |
| 🛡️ | **Face Liveness Detection** | Production-grade anti-spoofing |
| 🆔 | **ID Document Recognition** | Reads ID cards, passports and driver's licenses |
| 🔐 | **ID Document Liveness Detection** | Detects fake and tampered ID documents |

**Face Recognition SDKs**
- [Android](https://github.com/Faceplugin-ltd/FaceRecognition-Android)
- [iOS](https://github.com/Faceplugin-ltd/FaceRecognition-iOS)
- [Flutter](https://github.com/Faceplugin-ltd/FaceRecognition-Flutter)
- [React Native](https://github.com/Faceplugin-ltd/FaceRecognition-React-Native)
- [Ionic Cordova](https://github.com/Faceplugin-ltd/FaceRecognition-Ionic-Cordova)
- [Ionic Capacitor](https://github.com/Faceplugin-ltd/FaceRecognition-Ionic-Capacitor)
- [Docker for Linux](https://github.com/Faceplugin-ltd/FaceRecognition-Docker)
- [Windows](https://github.com/Faceplugin-ltd/FaceRecognition-Windows)
- [.NET MAUI](https://github.com/Faceplugin-ltd/FaceRecognition-.Net)
- [.NET WPF](https://github.com/Faceplugin-ltd/FaceRecognition-WPF-.Net)

**ID Document Recognition SDKs**
- [Android](https://github.com/Faceplugin-ltd/ID-Document-Recognition-Android)
- [iOS](https://github.com/Faceplugin-ltd/ID-Document-Recognition-iOS)
- [Flutter](https://github.com/Faceplugin-ltd/ID-Document-Recognition-Flutter)
- [React Native](https://github.com/Faceplugin-ltd/ID-Document-Recognition-React-Native)
- [Ionic Cordova](https://github.com/Faceplugin-ltd/ID-Document-Recognition-Ionic-Cordova)
- [Ionic Capacitor](https://github.com/Faceplugin-ltd/ID-Document-Recognition-Ionic-Capacitor)
- [Docker for Linux](https://github.com/Faceplugin-ltd/ID-Document-Recognition-Docker)
- [Windows](https://github.com/Faceplugin-ltd/ID-Document-Recognition-Windows)

**ID Document Liveness Detection SDK**
- [Docker for Linux](https://github.com/Faceplugin-ltd/ID-Document-Liveness-Detection-Docker)

## 📄 License

This project, including the source code and the trained model weights, is released under the [MIT No Attribution (MIT-0)](LICENSE) license. You're free to use, copy, modify, merge, publish, distribute, sublicense and sell it, including in commercial products, with no attribution required. The software is provided "as is", without warranty of any kind.

## 🤝 Support & Contact

While there are many ways to support this project, starring ⭐️ this GitHub repository is one of the simplest and most impactful. It increases discoverability and helps the project reach a wider audience. Thank you for your support 🙏

<div align="center">
  <a href="mailto:info@faceplugin.com">
    <img src="https://img.shields.io/badge/Email-info@faceplugin.com-blue.svg?logo=gmail" alt="Email"/>
  </a>
  <a href="https://wa.me/+14692784822">
    <img src="https://img.shields.io/badge/WhatsApp-faceplugin-green.svg?logo=whatsapp" alt="WhatsApp"/>
  </a>
  <a href="https://t.me/FacePluginSupport">
    <img src="https://img.shields.io/badge/telegram-@FacePluginSupport-blue.svg?logo=telegram" alt="Telegram"/>
  </a>
</div>

### 📞 Get in Touch

- **Email**: [info@faceplugin.com](mailto:info@faceplugin.com)
- **WhatsApp**: [+1 (469) 278-4822](https://wa.me/+14692784822)
- **Telegram**: [@FacePluginSupport](https://t.me/FacePluginSupport)
- **Website**: [faceplugin.com](https://faceplugin.com/)

---

<p align="center">Made with ❤️ by <a href="https://faceplugin.com">Faceplugin</a></p>
