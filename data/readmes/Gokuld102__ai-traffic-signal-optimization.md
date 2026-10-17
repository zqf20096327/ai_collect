# AI-Powered Adaptive Traffic Signal Optimization System

Real-time intelligent traffic management system using AI, Computer Vision, Machine Learning, and a modern web dashboard.

The system supports:

* Real-time vehicle detection
* Adaptive traffic signal timing
* Emergency vehicle prioritization
* Traffic congestion prediction
* Four-way junction simulation

---

## Features

* **Vehicle Detection (YOLOv8 + OpenCV)**
  Detects and counts vehicles from video streams in real time.

* **Adaptive Signal Optimization**
  Dynamically adjusts traffic signal timings based on traffic density.

* **Emergency Vehicle Detection**
  Detects ambulances, police vehicles, and fire trucks to create a virtual green corridor.

* **ML-Based Traffic Prediction**
  Predicts congestion levels using a machine learning model trained on synthetic traffic data.

* **MongoDB Integration**
  Stores traffic counts, signal logs, and prediction history.

* **Modern Web Dashboard**
  Displays live traffic counts, signal states, congestion levels, charts, and emergency alerts.

* **4-Way Junction Simulation**
  Simulates intelligent signal behavior for a four-lane traffic junction.

---

## Project Structure

```text
project-root
 ├── backend/
 │    ├── app.py
 │    ├── routes/
 │    │    └── traffic_routes.py
 │    ├── services/
 │    │    ├── traffic_service.py
 │    │    └── emergency_service.py
 │    ├── models/
 │    │    └── mongo_models.py
 │    └── utils/
 │         └── config.py
 │
 ├── ai/
 │    ├── yolo_detection.py
 │    ├── traffic_model.py
 │    └── dataset/
 │         ├── traffic_data.csv
 │         └── sample_traffic.mp4
 │
 ├── frontend/
 │    ├── index.html
 │    ├── style.css
 │    └── script.js
 │
 ├── database/
 │    └── mongo_setup.py
 │
 ├── requirements.txt
 └── README.md
```

---

## Technologies Used

* Python
* Flask
* OpenCV
* YOLOv8 (Ultralytics)
* scikit-learn
* MongoDB
* HTML/CSS/JavaScript
* Chart.js

---

## Prerequisites

* Python 3.10+

* MongoDB running locally:

  ```text
  mongodb://localhost:27017
  ```

* Sample traffic video:

  ```text
  ai/dataset/sample_traffic.mp4
  ```

> YOLOv8 weights will automatically download during the first execution if not already available.

---

## Installation & Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Using virtual environment (recommended):

```bash
python -m venv .venv
.\.venv\Scripts\activate

pip install -r requirements.txt
```

---

## MongoDB Setup (Optional)

Run:

```bash
python database/mongo_setup.py
```

This verifies the MongoDB connection and creates required collections automatically.

---

## Running the Project

Start the backend server:

```bash
cd backend
python app.py
```

Open in browser:

```text
http://127.0.0.1:5000/
```

The Flask backend serves the frontend dashboard directly.

---

## Core API Endpoints

### Process Traffic Video

```http
POST /api/process_video
```

Example body:

```json
{
  "source": "file",
  "path": "../ai/dataset/sample_traffic.mp4"
}
```

---

### Get Signal State

```http
GET /api/get_signal
```

Returns:

* Active signal
* Signal timings
* Traffic density

---

### Emergency Corridor Control

```http
POST /api/emergency
```

Example:

```json
{
  "active": true
}
```

---

### Predict Congestion

```http
POST /api/predict
```

Returns:

* Congestion level
* Prediction score
* ML analysis

---

## System Workflow

```text
Traffic Video
      ↓
YOLO Vehicle Detection
      ↓
Traffic Density Analysis
      ↓
ML Congestion Prediction
      ↓
Adaptive Signal Optimization
      ↓
Dashboard Visualization
```

---

## Sample Dataset & ML Model

### Dataset

Located at:

```text
ai/dataset/traffic_data.csv
```

Contains:

* Vehicle counts
* Time-based traffic patterns
* Synthetic traffic congestion data

### ML Model

Located at:

```text
ai/traffic_model.py
```

Uses:

* RandomForestRegressor
* RandomForestClassifier

The model is retrained on startup for demonstration purposes.

---

## Notes & Limitations

This project is intended as an educational and research-oriented prototype.

Current limitations:

* Uses a single sample traffic video
* Lane detection is region-based approximation
* Emergency detection depends on YOLO object labels
* Designed for simulation/demo purposes

---

## Future Improvements

* Real CCTV camera integration
* Multi-junction coordination
* Cloud-based analytics
* Edge AI deployment
* Advanced deep learning models
* Real-time traffic heatmaps
* Authentication & admin panel

---

## Screenshots

### Dashboard Preview

![Dashboard](images/app_prev.png)

### Detailed View

![Details](images/detail.png)

### Graph Analytics

![Graph](images/graph.png)

---

## Author

Developed for intelligent traffic management research and educational purposes.
