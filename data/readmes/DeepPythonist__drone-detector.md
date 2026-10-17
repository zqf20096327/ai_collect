# Drone Detector

High-precision YOLOv8 model for detecting drones, UAVs, birds, and airplanes with **96.1% mAP50** accuracy.

## Motivation

Modern conflicts have demonstrated the critical importance of aerial threat detection. Recent events, including the 12-day Iran-Israel conflict in June 2025, highlighted how drone warfare has become a decisive factor in modern military operations. During this period, Iran's infrastructure faced significant challenges from UAV attacks, with multiple critical facilities being targeted by advanced drone systems.

This model was developed to address the urgent need for:
- **Early Detection**: Identifying aerial threats before they reach critical infrastructure
- **Accurate Classification**: Distinguishing between friendly aircraft, birds, and hostile drones
- **Real-time Response**: Enabling rapid counter-drone measures
- **Civilian Protection**: Safeguarding airports, power plants, and urban areas

The devastating impact of drone strikes on civilian and military targets underscores the necessity for robust, AI-powered detection systems that can operate 24/7 with minimal human intervention.

## Performance

- **Precision**: 94.1%
- **Recall**: 94.1%
- **mAP50**: 96.1%
- **mAP50-95**: 67.4%

## Detectable Classes

- Drone
- Bird
- UAV
- Airplane

## Quick Start

```python
from ultralytics import YOLO

# Load model
model = YOLO('drone_detector.pt')

# Detect in image
results = model('image.jpg')
results[0].show()

# Detect in video
results = model('video.mp4')
```

## Installation

```bash
pip install ultralytics
```

## Sample Detections

<div align="center">

![Detection Sample 1](img1.jpg)
![Detection Sample 2](img2.jpg)

</div>

## Author

**Mohammad Rasol Esfandiari**
- GitHub: [@DeepPythonist](https://github.com/DeepPythonist)
- Email: mrasolesfandiari@gmail.com

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

<div align="center">
Made with ❤️ by Mohammad Rasol Esfandiari using YOLOv8
</div>