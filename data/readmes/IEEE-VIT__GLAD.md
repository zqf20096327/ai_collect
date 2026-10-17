# GLAD (Gas Leak Aerial Detector)

---

## Project Description

**GLAD (Gas Leak Aerial Detector)** is an IoT-based aerial inspection system designed to safely monitor, localize, and report hazardous gas emissions in high-risk industrial environments such as oil refineries, pipelines, chemical plants, and mining facilities. 

The platform combines a manually piloted quadcopter with onboard gas sensing, computer vision, and machine learning to detect atmospheric anomalies while keeping human personnel entirely out of harm's way. 

The system leverages a distributed edge-computing architecture: an **ESP32** handles real-time, low-latency sensor acquisition (NDIR gas and MLX thermal arrays), while an onboard **Raspberry Pi 4** acts as the main brain for computer vision and machine learning-driven sensor fusion. Telemetry is streamed wirelessly via an MQTT pipeline to a live web dashboard, allowing operators to monitor gas concentrations, leak confidence scores, environmental metrics, and live visual feeds in real time.

---
## Features & Completed Functionality

* **Edge AI Inference:** Raspberry Pi 4 edge computing for machine learning inference without cloud dependence.
* **Multi-Modal Sensor Fusion:** Intelligent algorithms combining gas, temperature, and vision data.
* **Remote Inspection Video:** Live digital camera stream enabling safe structural and infrastructure inspection.
* **Vegetation Chlorosis Detection:** Automated computer vision pipeline (OpenCV) evaluating aerial imagery.
* **Leak Confidence Score:** Generation of a definitive hazard metric fusing deterministic hard thresholds with ML insights.
* **Zero Worker Exposure:** Drone-based inspection eliminating direct worker exposure to hazardous environments.

---

## Technology Stack & Hardware

### Software & Protocols
* **Embedded System:** ESP32 (C++)
* **Edge Computing:** Raspberry Pi 4 (Python)
* **Communication Protocols:** MQTT, WebSockets
* **Computer Vision:** OpenCV
* **Machine Learning:** PyTorch (Sensor Fusion / CNN / MobileNetV2)
* **Frontend:** HTML, CSS

### Drone Hardware & Propulsion
* **Airframe:** Custom Quadcopter Frame
* **Motors:** Holybro 2216-880KV Brushless Motors
* **ESCs:** 30A Electronic Speed Controllers
* **Propellers:** 10×4.5 Propellers

### Sensors & Vision
* **Primary Sensors:** NDIR Gas Sensor, MLX Thermal Sensor
* **Onboard Vision:** Raspberry Pi Camera Module

---

## System Architecture Diagram

The system operates via a distributed data pipeline, shifting heavy processing loads to the edge computer while keeping the data collection layer lightweight and rapid:

<img width="340" height="244" alt="System Architecture" src="https://github.com/user-attachments/assets/16e1cfc4-605e-4169-aee1-afdf7a3a437f" />




---

## System Architecture

### 1. Data Acquisition
The ESP32 continuously acquires gas concentration and temperature data from onboard sensors. These sensor readings are dynamically packaged into lightweight JSON messages to minimize network overhead.

### 2. Communication Layer
Telemetry is transmitted over Wi-Fi using the publish-subscribe MQTT protocol, ensuring reliable data delivery with low communication overhead.

### 3. Edge Processing
The Raspberry Pi serves as the core processing hub:
* Processes live camera footage using OpenCV.
* Visual analysis identifies vegetation chlorosis as a secondary indicator of underground gas leakage.
* Gas sensor readings, thermal information, and computer vision outputs are fused using a machine learning model to generate a Leak Confidence Score.

### 4. Visualization
Processed telemetry is streamed to a browser-based dashboard via WebSockets. Operators receive live gas concentration graphs, environmental readings, and hazard notifications instantly.

---

## Machine Learning Model

The project utilizes a CNN-based image classification model specifically trained for chlorosis detection in vegetation to identify prolonged gas exposure.

* **Architecture:** Built using MobileNetV2 with transfer learning in PyTorch.
* **Function:** Analyzes aerial images captured by the onboard camera to identify vegetation stress caused by prolonged gas exposure. The model output is fused with gas concentration and temperature data to generate a leak confidence score.
* **Performance:** Achieved **80.56% validation accuracy** and **82.08% test accuracy** on a custom dataset of 5,348 banana leaf images.
* **Documentation:** Detailed information on the dataset, model architecture, training process, and evaluation metrics is available in the `ML_Model` directory.

---

## 3D Hardware & Frame Design

Below are the Fusion360 renders and schematics detailing the custom quadcopter frame assembly and sensor arrays:

<p align="center">
  <img width="48%" alt="Fusion360 Model Top View" src="https://github.com/user-attachments/assets/0efa8a44-ac9c-4f52-a0bf-bc2aea5a041a" />
  <img width="48%" alt="Fusion360 Model Isometric" src="https://github.com/user-attachments/assets/92cb1539-8ba1-47da-b2a0-fe5cfc1c1906" />
</p>
<p align="center">
  <img width="98%" alt="Frame Assembly View" src="https://github.com/user-attachments/assets/720d60b5-fdee-4ffc-a03f-8bbbc502b117" />
</p>
<p align="center">
  <img width="98%" alt="Component Side View" src="https://github.com/user-attachments/assets/d314f90b-5f03-436f-b4f0-2c0f0ca51535" />
</p>

---

## Demo Images
<img width="477" height="383" alt="Warning" src="https://github.com/user-attachments/assets/7b9811ba-a032-4df6-95b8-e4999e7089bd" />
<img width="475" height="371" alt="Gas_Detected" src="https://github.com/user-attachments/assets/afbd11f1-d49b-419c-abfc-382282ef28f7" />
<img width="950" height="446" alt="Dashboard" src="https://github.com/user-attachments/assets/fe5796a2-b8d6-463b-b060-69dff07e7f6a" />


---

## Setup & Installation

### 1. Prerequisites
Ensure you have the following installed:
* PlatForm Io
* Python 3.10+
* Visual Studio Code
* MQTT Broker (Mosquitto)
* Raspberry Pi
* OpenCv
* Torch Vision

### 2. Clone the Repository
```bash
git clone [https://github.com/]/<username>/GLAD.git
cd GLAD
```

---

# ESP32 Firmware Setup (PlatformIO)

1. Open **Visual Studio Code**.
2. Install the **PlatformIO IDE** extension.
3. Open the `Drone Gas Leak/src` folder.
4. Wait for PlatformIO to initialize.
5. Connect the ESP32 via USB.
6. Build the firmware:

```bash
pio run
```

or click **Build** in PlatformIO.

7. Upload firmware:

```bash
pio run --target upload
```

8. Monitor Serial Output

```bash
pio device monitor
```

---

# Raspberry Pi Setup

Install dependencies:

```bash
pip install opencv-python
pip install paho-mqtt
pip install flask
pip install numpy
pip install torch torchvision
```


Run processing:

```bash
python sensor_fusion.py
```

---

# Dashboard Setup

```bash
cd Dashboard
```

Open

```Terminal
python -m http.server 8000
http://localhost:8000/Dashboard.html
```

---

# System Workflow

1. Power on ESP32.
2. Boot Raspberry Pi.
3. Start Mosquitto Broker.
4. Run `main.py`.
5. Launch dashboard.
6. Start drone.
7. Monitor telemetry.

---

