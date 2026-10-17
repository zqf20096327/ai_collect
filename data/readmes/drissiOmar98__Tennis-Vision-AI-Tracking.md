# 🎾 Tennis-Vision-AI-Tracking

An **end-to-end, production-grade tennis video analysis system** leveraging state-of-the-art computer vision and deep learning. This repository integrates **Ultralytics YOLOv8** for robust player detection and tracking, a fine-tuned model for **high-velocity ball detection**, and a **custom ResNet50-based CNN** for precise court keypoint extraction. The system transforms raw match video into **physics-aware metrics** (e.g., shot speed, per-player distance covered, trajectory reconstructions) and **tactical visualizations** suitable for coaching, scouting, and advanced analytics workflows.  


---

## 🌟 Executive Summary

**Tennis-Vision-AI** solves the complex computer vision challenges inherent to court sports analytics: maintaining **persistent player identity** during rapid interactions, detecting **high-velocity, small-object balls** amidst motion blur, and establishing a **geometrically accurate mapping** from video pixels to real-world court coordinates.

The system is engineered for **determinism and auditability**—from annotated training sets and serialized model weights to final exported telemetry—making it suitable for both **academic research** and **applied deployment** in professional sports environments.

---

## 🚀 Core Capabilities

| Feature | Description | Key Benefit |
| :--- | :--- | :--- |
| **🎯 Dual-Model Detection** | Separate YOLOv8 (players) and fine-tuned YOLOv5 (ball) models. | Optimized precision for both large, persistent objects and small, fast-moving ones. |
| **🧭 Identity-Aware Tracking** | DeepSORT-inspired tracking with `persist=True` on player detections. | Stable Track IDs enable accurate per-player metric aggregation over entire rallies. |
| **📐 Court Coordinate Regression** | ResNet50 backbone outputs 14 (x, y) court keypoints for homography estimation. | Enables pixel→meter transformation and bird's-eye-view generation without manual court tagging. |
| **⚡ Trajectory Reconstruction** | Rolling-window smoothing + intelligent interpolation for ball path. | Produces continuous, physically plausible ball trajectories even with transient detection loss. |
| **🧮 Physics-Aware Metrics** | Calculates shot speed (km/h), player distance (m), court coverage (%) from calibrated coordinates. | Delivers actionable, validated insights comparable to radar/lidar systems. |
| **🗺️ Tactical Visualization** | Live mini-court overlay, player heatmaps, and shot spray charts. | Provides immediate visual feedback and strategic overviews. |
| **🧰 High-Velocity Stub System** | Serialize/deserialize detection outputs to `.pkl` for rapid iteration. | Decouples CV development from analytics/UI work, slashing iteration time. |
| **📦 Multi-Format Export** | Annotated MP4, frame-by-frame CSV, structured JSON telemetry, static plots. | Facilitates integration with existing databases, dashboards, and coaching software. |

## 📊 Data & Datasets

To ensure high-precision tennis analytics, this project relies on carefully curated datasets for **ball detection**, **player tracking**, and **court keypoint regression**.  

### 🎾 Ball Dataset
- Exported from **Roboflow** with ~428 annotated images used for fine-tuning.  
- Captures challenging conditions: **motion blur**, varying **lighting**, and **partial occlusions**.  
- Optimized for **high-velocity small-object detection**.  

### 🏃 Player Dataset
- Based on standard **person/player annotations**, adapted to tennis-specific viewpoints.  
- Handles **close-contact scenarios** and **occlusions** typical of tennis matches.  

### 📐 Court Keypoint Annotations
- **14 labeled points per frame** representing canonical court lines and intersections.  
- Enables **accurate homography-like mapping** from video pixels → real-world court coordinates.  

### ✅ Best Practices
- Maintain **train/validation/test splits**, plus a dedicated **evaluation set** with **high-velocity rallies**.  
- Ensure dataset balance across:  
  - **Camera angles**  
  - **Court surfaces**  
  - **Lighting conditions**  
- This supports robust **generalization** for diverse match scenarios.
