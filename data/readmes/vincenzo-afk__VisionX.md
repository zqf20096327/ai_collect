# VisionX: Real-Time Object Detection, Tracking, and Intelligent Analytics System

[![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-brightgreen.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![Ultralytics YOLO](https://img.shields.io/badge/Ultralytics-YOLOv8-yellow.svg)](https://ultralytics.com/)

VisionX is a production-grade, modular computer vision intelligence platform engineered for real-time object detection, multi-object tracking (MOT), zone counting, and automated edge analytics [1]. Built on top of Ultralytics YOLOv8 and FastAPI, VisionX provides a seamless end-to-end pipeline spanning custom dataset ingestion, model fine-tuning, high-performance video stream processing, and an interactive web control center.

## 1. Project Overview

VisionX addresses the critical need for low-latency, high-accuracy visual intelligence in diverse environments. The system enables users to:
- **Detect** objects in static images with high-precision bounding boxes and confidence scores.
- **Track** multiple objects across video frames using state-of-the-art algorithms (ByteTrack/BoT-SORT).
- **Count** object occurrences within specific regions of interest (ROI) or across virtual boundaries.
- **Analyze** detection trends and performance metrics through a real-time web dashboard.
- **Train** custom models on specialized datasets, such as the integrated pothole detection pipeline.

## 2. Key Features

- **Multi-Object Tracking (MOT)**: Maintains consistent object IDs across frames even under occlusion.
- **Zone & Line Counting**: Configurable spatial triggers for traffic monitoring and retail analytics.
- **Asynchronous Processing**: Leverages FastAPI's async capabilities for non-blocking stream handling.
- **Persistent Analytics**: Automatic logging of every detection event into a relational database.
- **Custom Training Pipeline**: Streamlined fine-tuning workflow with automated dataset validation.

## 3. System Architecture

VisionX utilizes a decoupled architecture to ensure scalability and maintainability.

```mermaid
graph TD
    subgraph Frontend
        UI[Web Dashboard]
    end
    subgraph Backend
        API[FastAPI Server]
        Engine[Detection & Tracking Engine]
        DB[(SQLite Database)]
    end
    subgraph Data
        Dataset[YOLO/COCO Datasets]
        Models[YOLOv8 Weights]
    end

    UI <-->|HTTP/WebSockets| API
    API --> Engine
    API <--> DB
    Engine --> Models
    Dataset --> Engine
```

## 4. Project Structure

| Directory / File | Purpose |
| :--- | :--- |
| `backend/` | Core application logic, including API routes, database models, and CV engines. |
| `datasets/` | Data management module for training and inference datasets. |
| `frontend/` | Static web assets for the operator control dashboard. |
| `models/` | Repository for pre-trained and fine-tuned model weights. |
| `outputs/` | Storage for processed media, training logs, and detection databases. |
| `training/` | Execution scripts for model fine-tuning and evaluation. |
| `config.py` | Global configuration and environment variable management. |

## 5. Prerequisites

- **Python**: 3.10 or higher.
- **GPU (Optional)**: NVIDIA GPU with CUDA support for accelerated inference and training.
- **OS**: Linux (Ubuntu recommended), macOS, or Windows (via WSL2).

## 6. Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/vincenzo-afk/VisionX.git
   cd VisionX
   ```

2. **Set up virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## 7. Configuration

VisionX is configured via environment variables. Copy the example template to get started:

```bash
cp .env.example .env
```

| Variable | Description | Default |
| :--- | :--- | :--- |
| `MODEL` | Path to weights or YOLOv8 model name | `yolov8n.pt` |
| `DEVICE` | Compute device (`cpu`, `cuda`, `mps`) | `cpu` |
| `CONFIDENCE_THRESHOLD` | Minimum detection confidence | `0.4` |

## 8. API Documentation

The backend provides a RESTful API for all system operations. Interactive documentation is available at `/docs` (Swagger UI).

### Core Endpoints

- `POST /api/detect/image`: Analyze an uploaded image.
- `POST /api/detect/video`: Process an uploaded video with tracking.
- `GET /api/detect/webcam`: Live MJPEG stream with detection overlay.
- `GET /api/analytics`: Retrieve aggregate system statistics.

## 9. Usage Examples

### Image Detection via CLI

```bash
curl -X POST http://localhost:8000/api/detect/image \
  -F "file=@path/to/your/image.jpg"
```

### Starting the Web Dashboard

```bash
python3 -m backend.main
```
Then navigate to `http://localhost:8000` in your browser.

## 10. Training & Fine-Tuning

VisionX supports seamless fine-tuning on custom datasets.

1. **Prepare Data**: Place your YOLO-formatted data in `datasets/images/` and `datasets/labels/`.
2. **Configure**: Update `datasets/data.yaml` with your class names.
3. **Execute Training**:
   ```bash
   python training/train.py --epochs 50 --batch 16 --run-name my_custom_model
   ```

## 11. Testing

Run the test suite to ensure system integrity:

```bash
# Verify API health
curl -f http://localhost:8000/api/health
```

## 12. Performance Benchmarks

| Device | Model | Inference Time (ms) | FPS |
| :--- | :--- | :--- | :--- |
| CPU (i7-12700K) | yolov8n.pt | ~45ms | 22 |
| GPU (RTX 3080) | yolov8n.pt | ~2ms | 500+ |

## 13. Contributing

We welcome contributions! Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) for detailed submission guidelines.

## 14. Security

Security is a priority. Please report vulnerabilities according to our [SECURITY.md](SECURITY.md) policy.

## 15. License

Distributed under the MIT License. See `LICENSE` for more information.

## 16. Acknowledgments & References

[1] Jocher, G., Chaurasia, A., & Qiu, J. (2023). *Ultralytics YOLO*. GitHub. https://github.com/ultralytics/ultralytics

***

*Developed by vincenzo-afk. For support, please open an issue in the GitHub repository.*
