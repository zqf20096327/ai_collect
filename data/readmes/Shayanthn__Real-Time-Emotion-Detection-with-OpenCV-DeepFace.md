# 🎭 Real-Time Facial Expression Recognition
### Bachelor's Computer Engineering Project

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0+-orange.svg)](https://tensorflow.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-green.svg)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<p align="center">
   <img src="https://img.shields.io/badge/Status-Academic%20Project-blue" alt="Status"/>
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey" alt="Platform"/>
</p>

---

## 🌟 Overview

This project classifies visible facial expressions from webcam frames into seven predefined classes using OpenCV, Haar-based face detection, and the FER2013 Mini-XCEPTION model. It is a facial-expression classification system, not a measurement of a person's true internal emotional state.

### ✨ Key Features

- 🧠 **Mini-XCEPTION Model**: Pretrained FER2013 model with verified 64x64 grayscale input
- 🎯 **Seven Classes**: Angry, disgust, fear, happy, sad, surprise, and neutral
- ⚡ **Measured Performance**: Real benchmark results are reported below
- 🎨 **Professional UI**: Cyberpunk-inspired HUD with live emotion probability bars
- 📊 **7 Emotion Classes**: Detects Happy, Sad, Angry, Surprise, Fear, Disgust, and Neutral
- 🎥 **Video Recording**: Built-in screen recording for content creation
- 🔧 **Modular Architecture**: Clean, maintainable code structure following best practices
- 📈 **FER2013 Evaluation**: Separate evaluation and benchmark scripts

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Webcam/Camera
- (Optional) GPU with CUDA for faster processing

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Shayanthn/Real-Time-Emotion-Detection-with-OpenCV-DeepFace.git
   cd Real-Time-Emotion-Detection-with-OpenCV-DeepFace
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download pre-trained model** (Optional)
   
   Download the FER2013 Mini-XCEPTION model from [here](https://github.com/oarriaga/face_classification/blob/master/trained_models/emotion_models/fer2013_mini_XCEPTION.102-0.66.hdf5) and place it in the project root directory.

4. **Run the application**
   ```bash
   python main.py
   ```

---

## 📚 Dataset Setup (Optional)

To train your own models or experiment with the FER2013 dataset:

1. **Get Kaggle API credentials**
   - Go to [Kaggle Account Settings](https://www.kaggle.com/account)
   - Click "Create New API Token"
   - Save the downloaded `kaggle.json` to `~/.kaggle/` (Linux/Mac) or `C:\Users\<YourUser>\.kaggle\` (Windows)

2. **Download the dataset**
   ```bash
   python scripts/download_dataset.py
   ```

For detailed Kaggle setup instructions, see [KAGGLE_SETUP.md](KAGGLE_SETUP.md).

---

## 🎮 Controls

| Key | Action |
|-----|--------|
| `Q` | Quit application |
| `R` | Toggle video recording |

---

## 🏗️ Project Structure

```
Real-Time-Emotion-Detection/
│
├── main.py                          # Main application entry point
├── requirements.txt                 # Python dependencies
├── KAGGLE_SETUP.md                  # Kaggle dataset setup guide
│
├── src/
│   ├── __init__.py
│   ├── config.py                    # Configuration settings
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── analyzer.py              # Emotion analysis engine
│   │   └── camera.py                # Video stream handler
│   │
│   ├── ui/
│   │   ├── __init__.py
│   │   └── visualizer.py            # HUD and visualization
│   │
│   └── utils/
│       ├── __init__.py
│       ├── fps_counter.py           # FPS calculation utility
│       └── logger.py                # Logging utility
│
├── scripts/
│   └── download_dataset.py          # Kaggle dataset downloader
│
├── data/                            # Dataset directory (created after download)
└── LICENSE
```

---

## 🔬 Technical Details

### Architecture

1. **Face Detection**: OpenCV Haar Cascade in the current runtime configuration
2. **Expression Classification**: FER2013 Mini-XCEPTION model
   - DeepFace remains available as a fallback when the custom model is unavailable
3. **Performance Optimization**:
   - Frame throttling (analyze every N frames)
   - Multithreaded analysis pipeline
   - Efficient NumPy operations

### Emotion Classes

The system recognizes 7 fundamental emotions based on Paul Ekman's research:

| Emotion | Color Code | Description |
|---------|-----------|-------------|
| 😊 Happy | Yellow/Cyan | Joy, pleasure, satisfaction |
| 😢 Sad | Blue | Sorrow, grief, melancholy |
| 😠 Angry | Red | Irritation, rage, fury |
| 😲 Surprise | Magenta | Shock, amazement, astonishment |
| 😨 Fear | Orange | Anxiety, terror, apprehension |
| 🤢 Disgust | Green | Revulsion, distaste, aversion |
| 😐 Neutral | Gray | No strong emotion detected |

---

## 📊 Evaluation Results

Measured on the FER2013 `PublicTest` split (`3,589` samples) using the existing Mini-XCEPTION model:

- **Accuracy**: `0.539983`
- **Macro Precision**: `0.505432`
- **Macro Recall**: `0.479214`
- **Macro F1-score**: `0.478924`

These results apply only to this FER2013 split and should not be interpreted as general real-world performance.

## ⚡ Performance

Measured locally using the existing model and runtime pipeline:

- **Mean inference latency**: `214.645 ms`
- **Median inference latency**: `200.438 ms`
- **Minimum inference latency**: `137.137 ms`
- **Maximum inference latency**: `528.956 ms`
- **Average camera-loop FPS**: `2.799`
- **Minimum camera-loop FPS**: `1.511`
- **Maximum camera-loop FPS**: `3.428`

Inference latency and camera-loop FPS are separate measurements. Results are saved in `results/fer2013_metrics.txt` and `results/performance_metrics.txt`.

---

## 🛠️ Configuration

Edit `src/config.py` to customize:

```python
# Camera Settings
CAMERA_WIDTH = 1920
CAMERA_HEIGHT = 1080
FPS = 60

# Analysis Settings
ANALYSIS_INTERVAL = 0.1  # Seconds between emotion checks
ANALYSIS_THROTTLE = 3    # Analyze every N frames

# Visualization
SHOW_FPS = True
SHOW_GRAPH = True
THEME_COLOR = (0, 255, 255)  # Cyan
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **DeepFace**: [serengil/deepface](https://github.com/serengil/deepface)
- **FER2013 Dataset**: [Kaggle FER2013](https://www.kaggle.com/datasets/msambare/fer2013)
- **MediaPipe**: [Google MediaPipe](https://google.github.io/mediapipe/)
- **Mini-XCEPTION**: [oarriaga/face_classification](https://github.com/oarriaga/face_classification)

---

## 👨‍💻 Author

**Shayan Taherkhani**

- Website: [shayantaherkhani.ir](https://shayantaherkhani.ir)
- GitHub: [@Shayanthn](https://github.com/Shayanthn)
- Email: admin@shayantaherkhani.ir

---

## 🐛 Known Issues

- First run may be slow due to model loading
- Requires good lighting for optimal accuracy
- Multiple faces in frame: only the first detected face is analyzed

---

## 🔮 Future Enhancements

- [ ] Multi-face support
- [ ] Age and gender detection
- [ ] Emotion history timeline graph
- [ ] Export analysis data to CSV/JSON
- [ ] Web dashboard for remote monitoring
- [ ] Mobile app (iOS/Android)
- [ ] Cloud deployment (AWS/Azure)

---

## 📞 Support

If you have any questions or need help, please:

1. Check the [Issues](https://github.com/Shayanthn/Real-Time-Emotion-Detection-with-OpenCV-DeepFace/issues) page
2. Create a new issue with detailed information
3. Contact via email: admin@shayantaherkhani.ir

---

<p align="center">
  Made with ❤️ by <a href="https://shayantaherkhani.ir">Shayan Taherkhani</a>
</p>

<p align="center">
  ⭐ Star this repository if you find it helpful!
</p>
