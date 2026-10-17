# 🚦 AI Traffic Violation Monitoring System

> **An intelligent computer vision system for automated traffic monitoring, vehicle tracking, and real-time violation detection using YOLOv8, ByteTrack, OpenCV, and Streamlit.**

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-111111?style=for-the-badge)](https://github.com/ultralytics/ultralytics)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge\&logo=opencv\&logoColor=white)](https://opencv.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)](https://streamlit.io/)
[![ByteTrack](https://img.shields.io/badge/Tracking-ByteTrack-00A67E?style=for-the-badge)](https://github.com/ifzhang/ByteTrack)

---

## 📌 Overview

The **AI Traffic Violation Monitoring System** is a computer vision-based application designed to automate the monitoring of road traffic and identify potential traffic violations from video footage.

The system combines **real-time object detection**, **multi-object tracking**, **rule-based violation analysis**, and an interactive **Streamlit dashboard** to transform raw traffic video into meaningful monitoring and analytics information.

Instead of relying entirely on manual observation, the system provides an automated pipeline capable of:

* 🚗 Detecting vehicles in traffic footage
* 🎯 Assigning persistent tracking IDs to detected vehicles
* 🛣️ Monitoring vehicle movement across defined traffic regions
* ⚠️ Identifying configurable traffic violations
* 📊 Generating traffic statistics and analytical summaries
* 🎥 Processing uploaded or sample traffic videos
* 🖥️ Presenting results through an interactive web interface
* 💾 Exporting processed monitoring results for further analysis

The project demonstrates how modern **deep learning and computer vision techniques** can be integrated into a practical intelligent transportation monitoring workflow.

---

## ✨ Key Features

### 🔍 Vehicle Detection

The system uses **YOLOv8n** for fast and efficient object detection.

It can identify relevant road users from traffic footage and generate bounding boxes around detected objects.

Each detection provides information such as:

* Object class
* Bounding box coordinates
* Detection confidence
* Object position

---

### 🎯 Multi-Object Tracking

Detection alone cannot determine whether an object appearing in consecutive frames is the same vehicle.

To solve this, the system integrates **ByteTrack** for multi-object tracking.

Each tracked vehicle receives a persistent identifier:

```text
Vehicle #1
Vehicle #2
Vehicle #3
...
```

This allows the system to maintain vehicle identities while they move through the scene.

---

### ⚠️ Traffic Violation Detection

The monitoring pipeline analyzes tracked vehicle behavior against predefined traffic-monitoring rules.

The violation detection layer can be used to identify events such as:

* 🚫 Restricted-zone movement
* 🛑 Stop-line violations
* 🚦 Signal-related violations
* 🛣️ Lane or region violations
* 📍 Other configurable rule-based traffic events

The violation logic is separated from the detection and tracking components, making the system easier to extend and maintain.

---

### 📊 Traffic Analytics

The analytics module transforms detection and violation information into useful statistics.

Possible analytical information includes:

* Total detected vehicles
* Unique tracked vehicles
* Vehicle-category counts
* Violation counts
* Violation frequency
* Frame-level monitoring information
* Traffic activity summaries

These metrics provide a high-level view of the traffic scene and system activity.

---

### 🖥️ Interactive Streamlit Dashboard

The project includes a Streamlit-based interface for interacting with the monitoring system.

The dashboard provides a convenient way to:

1. Select or provide traffic footage
2. Run the monitoring pipeline
3. Visualize processed results
4. Review detected violations
5. Inspect analytical information
6. Interact with the system without requiring a command-line workflow

---

## 🧠 System Architecture

The overall processing pipeline follows this architecture:

```text
                   ┌─────────────────────┐
                   │    Traffic Video    │
                   └──────────┬──────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │   Video Processing  │
                   │      OpenCV         │
                   └──────────┬──────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │     YOLOv8n         │
                   │  Object Detection   │
                   └──────────┬──────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │      ByteTrack      │
                   │   Object Tracking   │
                   └──────────┬──────────┘
                              │
                              ▼
                   ┌─────────────────────┐
                   │ Violation Detection │
                   │     Rule Engine     │
                   └──────────┬──────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
          ┌─────────────────┐   ┌─────────────────┐
          │    Analytics    │   │ Processed Video │
          └────────┬────────┘   └────────┬────────┘
                   │                     │
                   └──────────┬──────────┘
                              ▼
                   ┌─────────────────────┐
                   │ Streamlit Dashboard │
                   └─────────────────────┘
```

---

## 🛠️ Technology Stack

| Technology       | Purpose                              |
| ---------------- | ------------------------------------ |
| **Python**       | Core programming language            |
| **YOLOv8**       | Real-time object detection           |
| **ByteTrack**    | Multi-object tracking                |
| **OpenCV**       | Video processing and computer vision |
| **Streamlit**    | Interactive web application          |
| **NumPy**        | Numerical and array-based processing |
| **Ultralytics**  | YOLO model implementation            |
| **Git & GitHub** | Version control and project hosting  |

---

## 📁 Project Structure

```text
AI-Traffic-Violation-Monitoring-System/
│
├── app.py
│   └── Streamlit application and user interface
│
├── tracker.py
│   └── Vehicle detection and object-tracking functionality
│
├── traffic_violation.py
│   └── Traffic violation detection and rule-based monitoring logic
│
├── analytics.py
│   └── Traffic statistics and analytical processing
│
├── test_traffic_violation.py
│   └── Tests for traffic violation functionality
│
├── requirements.txt
│   └── Python project dependencies
│
├── yolov8n.pt
│   └── YOLOv8 Nano model weights
│
├── sample_videos/
│   └── Sample traffic footage for testing and demonstration
│
├── screenshots/
│   └── Application and output screenshots
│
├── outputs/
│   └── Generated monitoring results
│
├── .streamlit/
│   └── Streamlit configuration
│
├── .gitignore
│   └── Git ignore rules
│
└── README.md
    └── Project documentation
```

---

## ⚙️ How the System Works

### 1. Video Input

A traffic video is provided to the application as the primary input.

The video is processed frame by frame using OpenCV.

```python
video = cv2.VideoCapture(video_path)
```

---

### 2. Object Detection

Each frame is passed through the YOLOv8 model.

```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
results = model(frame)
```

The detector identifies objects and returns their locations, classes, and confidence scores.

---

### 3. Object Tracking

The detected objects are passed through the tracking pipeline.

ByteTrack associates detections between consecutive frames and maintains a unique identity for each tracked object.

Conceptually:

```text
Frame 001 → Vehicle ID 12
Frame 002 → Vehicle ID 12
Frame 003 → Vehicle ID 12
Frame 004 → Vehicle ID 12
```

This allows the system to reason about vehicle movement over time rather than treating every detection as a new vehicle.

---

### 4. Violation Analysis

Tracked vehicles are evaluated against traffic-monitoring rules.

The system uses spatial and temporal information from tracked objects to determine whether a monitored event has occurred.

A simplified workflow is:

```text
Tracked Vehicle
      │
      ▼
Determine Position
      │
      ▼
Check Traffic Rule
      │
      ├── No Violation ──► Continue Monitoring
      │
      └── Violation ─────► Record Event
                              │
                              ▼
                         Update Analytics
```

---

### 5. Analytics

Recorded detections and violations are processed to produce useful traffic statistics.

This separates raw computer vision output from higher-level information that can be presented to users.

---

### 6. Visualization

The Streamlit interface brings the complete workflow together and provides an accessible interface for running and reviewing the monitoring system.

---

## 🚀 Getting Started

### Prerequisites

Make sure the following are installed:

* Python 3.9 or newer
* pip
* Git
* A machine capable of running YOLO inference

For improved performance, a CUDA-compatible NVIDIA GPU can be used, although the system can also operate on CPU.

---

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/HadeedJalani/AI-Traffic-Violation-Monitoring-System.git
```

Navigate into the project:

```bash
cd AI-Traffic-Violation-Monitoring-System
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

For macOS/Linux:

```bash
source .venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

Streamlit will launch the application in your default browser.

The dashboard can then be used to provide traffic footage and inspect the generated monitoring results.

---

## 🧪 Testing

The project includes automated tests for traffic violation functionality.

Run the test suite with:

```bash
pytest
```

For a more detailed test output:

```bash
pytest -v
```

---

## 🎥 Input and Output

### Input

The system is designed to process traffic video footage containing vehicles and road activity.

Supported video formats depend on the installed OpenCV codecs and environment.

Example:

```text
sample_videos/
├── traffic_video_01.mp4
├── traffic_video_02.mp4
└── traffic_video_03.mp4
```

### Output

The processing pipeline can generate annotated traffic footage containing information such as:

```text
Vehicle Bounding Box
        +
Tracking ID
        +
Detection Information
        +
Violation Information
```

The resulting information can also be used by the analytics layer to generate traffic summaries.

---

## 🔧 Configuration and Extensibility

The project is designed with modular components so individual parts of the system can be improved without redesigning the entire application.

### Detection Layer

The YOLO model can be replaced or upgraded with another compatible Ultralytics detection model.

### Tracking Layer

The tracking implementation can be extended to support different tracking strategies or additional object metadata.

### Violation Layer

New traffic rules can be implemented independently within the violation-analysis logic.

Examples include:

```text
Speed-related rules
Lane restrictions
Restricted-zone entry
Traffic signal compliance
Stop-line monitoring
Vehicle classification rules
```

### Analytics Layer

Additional metrics and visualizations can be introduced without modifying the underlying detection model.

---

## 📈 Performance Considerations

Real-time computer vision performance depends on several factors:

* Input video resolution
* Video frame rate
* YOLO model size
* CPU/GPU performance
* Number of objects in each frame
* Tracking complexity
* Video encoding and decoding performance

For environments where inference speed is important, lightweight models such as **YOLOv8n** provide a practical balance between detection speed and accuracy.

For more demanding deployments, the detection model can be upgraded depending on available hardware and accuracy requirements.

---

## 🔐 Data and Privacy

This project is designed around locally processed video footage.

Traffic footage can contain sensitive information such as:

* Vehicle license plates
* Faces
* Locations
* Road activity

When using real-world traffic footage, appropriate privacy, security, and legal requirements should be considered.

Do not upload or distribute footage containing personally identifiable information without the necessary authorization.

---

## ⚠️ Limitations

The system is a computer vision monitoring solution and should not be considered a perfect replacement for certified traffic enforcement systems.

Performance can be affected by:

* Poor lighting
* Heavy rain or fog
* Occluded vehicles
* Camera movement
* Low-resolution footage
* Unusual camera angles
* Dense traffic
* Incorrect scene configuration
* Detection errors
* Tracking ID switches

Violation detection is therefore dependent on the quality of both object detection and tracking.

---

## 🔮 Future Improvements

Potential future enhancements include:

* 🚘 Automatic license plate recognition
* 📸 Violation evidence snapshots
* 🕒 Timestamped violation records
* 🚦 Advanced traffic-signal recognition
* 🛣️ Automatic lane detection
* 📏 Speed estimation
* 🗺️ Geographic traffic monitoring
* 🗄️ Database integration
* 📊 Advanced analytics dashboards
* 🔔 Real-time violation notifications
* ☁️ Cloud deployment
* 🎥 Live CCTV stream integration
* 🧠 Advanced deep-learning-based violation classification
* 🔐 Role-based access control
* 📑 Automated violation reports

---

## 🧩 Design Philosophy

The project follows a modular computer vision architecture:

```text
Detection
    ↓
Tracking
    ↓
Rule Evaluation
    ↓
Analytics
    ↓
Visualization
```

This separation improves:

* Maintainability
* Debugging
* Scalability
* Testing
* Reusability
* Future model integration

Each component has a clearly defined responsibility, allowing the system to evolve from a prototype into a more comprehensive intelligent transportation platform.

---

## 📚 Core Concepts Demonstrated

This project demonstrates practical implementation of:

* Computer Vision
* Deep Learning
* Object Detection
* YOLO
* Multi-Object Tracking
* ByteTrack
* Video Processing
* Spatial Analysis
* Rule-Based Event Detection
* Data Analytics
* Python Application Development
* Streamlit Application Development
* Automated Testing
* Modular Software Architecture

---

## 🏗️ Development Workflow

A typical development workflow for extending the system is:

```text
Define Requirement
       ↓
Implement Detection / Rule
       ↓
Test on Sample Footage
       ↓
Evaluate Detection Accuracy
       ↓
Tune Parameters
       ↓
Validate Tracking
       ↓
Integrate Analytics
       ↓
Update Streamlit Interface
       ↓
Run Tests
       ↓
Document Changes
```

---

## 🤝 Contributing

Contributions and improvements are welcome.

A typical contribution workflow is:

```bash
git clone https://github.com/HadeedJalani/AI-Traffic-Violation-Monitoring-System.git

cd AI-Traffic-Violation-Monitoring-System

git checkout -b feature/your-feature
```

After making changes:

```bash
git add .
git commit -m "Add your feature"
git push origin feature/your-feature
```

When contributing, please keep changes focused, maintain the existing project structure, and include appropriate tests where applicable.

---

## 📄 License

This project is provided for educational, research, and development purposes.

If you intend to deploy the system for real-world traffic enforcement or commercial use, review the applicable software, model, dataset, video, privacy, and regulatory licensing requirements.

---

## 👨‍💻 Author

### Hadeed Jalani

**AI / Machine Learning Developer**

Focused on building practical solutions using:

```text
Python
Machine Learning
Deep Learning
Computer Vision
Artificial Intelligence
Data Analytics
```

---

## ⭐ Acknowledgements

This project builds upon the work of the open-source computer vision and machine learning ecosystem, particularly:

* Ultralytics YOLO
* ByteTrack
* OpenCV
* Streamlit
* Python

Their respective projects provide important foundations for modern computer vision and interactive machine-learning applications.

---

## 🚦 Final Note

The **AI Traffic Violation Monitoring System** demonstrates how object detection, multi-object tracking, rule-based reasoning, analytics, and an interactive interface can be combined into a single intelligent traffic-monitoring workflow.

The architecture is intentionally modular, making the project suitable as a foundation for further experimentation in **intelligent transportation systems, computer vision, and automated traffic analysis**.

---

<p align="center">
  <strong>🚦 AI Traffic Violation Monitoring System</strong>
  <br>
  Intelligent Vision • Vehicle Tracking • Traffic Analytics
  <br><br>
  <strong>Built with Python, YOLOv8, ByteTrack, OpenCV & Streamlit</strong>
</p>
