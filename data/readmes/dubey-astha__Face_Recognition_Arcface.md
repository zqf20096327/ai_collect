# Face Recognition System using ArcFace (InsightFace)

A modular, high-accuracy face recognition system built using **ArcFace (InsightFace – buffalo_l)**.  
The repository is designed around a reusable **core face recognition engine**, with real-world application extensions such as a **Student Attendance System**.

---

## Project Motivation

Face recognition systems often face challenges related to accuracy, scalability, and real-time performance.  
This project focuses on building a **metric-learning-based face recognition pipeline** using ArcFace embeddings, emphasizing reliability, modularity, and practical deployment readiness.

The objective is not just face detection, but **robust identity recognition with confidence-based decision making**.

---

## Key Highlights

- ArcFace (InsightFace `buffalo_l`) for highly discriminative facial embeddings  
- Cosine similarity–based identity matching  
- Configurable similarity threshold for recognition confidence  
- Offline evaluation using stored embeddings  
- Real-time webcam-based face recognition  
- Modular design allowing easy extension into applications  

---

## System Workflow

Input Image / Webcam Frame  
→ Face Detection (InsightFace)  
→ Face Embedding Extraction (ArcFace)  
→ Embedding Storage (CSV)  
→ Cosine Similarity Matching  
→ Threshold-based Decision  
→ Identity with Confidence Score  

---


## Repository Structure
```
Face_Recognition_Arcface/
│
├── core_face_recognition/ # Core ArcFace-based recognition pipeline
├── extras/ # Application use-cases (Student Attendance System)
├── requirements.txt
├── README.md
├── LICENSE
```
---

## Core Features

- ArcFace-based facial embedding generation  
- Similarity-based face recognition (no classifier training required)  
- Threshold-driven identity verification  
- Offline evaluation and testing support  
- Real-time inference using webcam  
- CPU-compatible execution  

---

## Applications

- Student Attendance System (implemented in `extras/`)  
- Identity verification prototypes  
- Academic demonstrations and research  
- Access control proof-of-concepts  

---

## Dataset

The dataset is **not included** in this repository due to privacy and licensing constraints.

### Dataset Used for Testing

This project was tested using a public Kaggle dataset:

https://www.kaggle.com/datasets/cybersimar08/face-recognition-dataset


### Expected Dataset Structure
```
Faces/
├── Person_Name_ID/
│ ├── image1.jpg
│ ├── image2.jpg
│ └── ...
```
---

## Installation

### Requirements

- Python 3.8 or higher  
- Webcam (for real-time recognition)  

### Setup

```bash
pip install -r requirements.txt
```

### How to Run

- Download and prepare the dataset in the expected folder structure
- Update dataset paths inside the code if required
- Run the main recognition script:
  python main.py
- Press q to exit real-time webcam mode

### Results and Observations
- High recognition accuracy using ArcFace embeddings
- Stable confidence-based predictions across identities
- Real-time recognition with bounding boxes and confidence scores
- Effective recognition without training traditional classifiers

### Key Learnings
- Practical understanding of metric learning and facial embeddings
- Hands-on experience with ArcFace and InsightFace
- Design of similarity-based recognition pipelines
- Real-time computer vision system development
- Dataset organization and evaluation strategies

### Future Enhancements
- REST API integration using FastAPI or Flask
- Web-based attendance dashboard
- Database-backed embedding storage
- GPU acceleration support
- Cloud deployment readiness

---

## Disclaimer
This project is intended strictly for educational and research purposes.
Users are responsible for ensuring that face recognition systems comply with ethical, legal, and privacy standards when deployed.

---

## License
This project is licensed under the MIT License.
You are more than welcome to use, modify, and distribute this project with appropriate attribution.

---

## Author
**Astha Dubey**   
Electronics and Telecommunication   
Interests: Machine Learning, AI, and Computer Vision   
linkedin.com/in/astha-dubey
