# YOLO — A Practical and Technical Guide

> From **YOLOv1** and single-stage detection to **anchor-free, end-to-end, NMS-free, and open-vocabulary** YOLO-family models.

A research-backed, beginner-friendly reference to the **YOLO ecosystem**, covering its architecture, major versions, independent branches, benchmarks, and practical trade-offs.

**Created and maintained by [Ahmad Jeddizahed](https://github.com/AhmadJeddi).**

## What's Included

- YOLO from first principles
- Backbone / Neck / Head architecture
- IoU, AP, mAP, FPS, latency, Params, and FLOPs
- YOLOv1 → YOLOv4
- YOLOv5, YOLOX, PP-YOLOE, YOLOv6, YOLOv7
- YOLOv8, YOLOv9, YOLOv10
- YOLO11, YOLO12, YOLO26
- YOLO-World, YOLOE, and YOLOE-26
- Official and independent YOLO branches
- Anchor-based → Anchor-free → NMS-free evolution
- Architecture comparisons
- Benchmark comparisons
- Advantages, limitations, and licensing considerations
- Primary research papers and official documentation

## Repository Structure

```text
.
├── README.md
├── YOLO_Architecture_Matrix.md
└── assets/
    ├── modern-yolo-architecture.svg
    ├── yolo-family-timeline.svg
    ├── head-evolution-anchor-free-e2e.svg
    └── representative-benchmark-table.svg
```

> For a compact version-by-version architecture comparison, see
> [YOLO Architecture Matrix](YOLO_Architecture_Matrix.md).

> **Benchmark note:** Results in this repository come from different papers and official implementations and may use different hardware, runtimes, batch sizes, precision, and post-processing settings. They should not be treated as a single apples-to-apples leaderboard.

<p align="center">
  <img src="assets/yolo-family-timeline.svg" alt="Timeline showing the evolution of the YOLO family from YOLOv1 to YOLO26 and parallel branches." width="100%">
</p>

---

## Table of Contents

- [1. What is YOLO?](#1-what-is-yolo)
- [2. Object Detection Basics Before YOLO](#2-object-detection-basics-before-yolo)
- [3. What does a YOLO Detector Actually Predict?](#3-what-does-a-yolo-detector-actually-predict)
- [4. YOLO Architecture: Backbone, Neck, Head](#4-yolo-architecture-backbone-neck-head)
- [5. Important Metrics](#5-important-metrics)
- [6. YOLOv1 — The Beginning](#6-yolov1--the-beginning)
- [7. YOLOv2 / YOLO9000 — Better, Faster, Stronger](#7-yolov2--yolo9000--better-faster-stronger)
- [8. YOLOv3 — Multi-Scale Detection](#8-yolov3--multi-scale-detection)
- [9. YOLOv4 — Engineering the Speed/Accuracy Frontier](#9-yolov4--engineering-the-speedaccuracy-frontier)
- [10. Scaled-YOLOv4 — Scaling the Network](#10-scaled-yolov4--scaling-the-network)
- [11. YOLOv5 — The Developer-Ecosystem Milestone](#11-yolov5--the-developer-ecosystem-milestone)
- [12. YOLOX — A Major Independent Branch](#12-yolox--a-major-independent-branch)
- [13. PP-YOLOE — PaddlePaddle Ecosystem](#13-pp-yoloe--paddlepaddle-ecosystem)
- [14. YOLOv6 — Industrial and Deployment Focus](#14-yolov6--industrial-and-deployment-focus)
- [15. YOLOv7 — Trainable Bag-of-Freebies](#15-yolov7--trainable-bag-of-freebies)
- [16. YOLOv8 — The Modern Ultralytics Baseline](#16-yolov8--the-modern-ultralytics-baseline)
- [17. YOLOv9 — PGI + GELAN](#17-yolov9--pgi--gelan)
- [18. YOLOv10 — End-to-End NMS-Free Detection](#18-yolov10--end-to-end-nms-free-detection)
- [19. YOLO11 — More Efficient Ultralytics Models](#19-yolo11--more-efficient-ultralytics-models)
- [20. YOLO12 — Attention-Centric Research Direction](#20-yolo12--attention-centric-research-direction)
- [21. YOLO26 — Current Ultralytics Direction](#21-yolo26--current-ultralytics-direction)
- [22. NMS-Free Is Not the Same as "No Alternative Head"](#22-nms-free-is-not-the-same-as-no-alternative-head)
- [23. YOLO-World — Open-Vocabulary Detection](#23-yolo-world--open-vocabulary-detection)
- [24. YOLOE — Real-Time "Seeing Anything"](#24-yoloe--real-time-seeing-anything)
- [25. YOLOE-26 — Open Vocabulary Meets End-to-End YOLO26](#25-yoloe-26--open-vocabulary-meets-end-to-end-yolo26)
- [26. The Most Important Non-Official / Independent YOLO Branches](#26-the-most-important-non-official--independent-yolo-branches)
- [27. Why There Is No Single "Best YOLO"](#27-why-there-is-no-single-best-yolo)
- [28. Reading the Benchmark Table Correctly](#28-reading-the-benchmark-table-correctly)
- [29. Representative Benchmark Table](#29-representative-benchmark-table)
- [30. Architecture Evolution Summary](#30-architecture-evolution-summary)
- [31. What Actually Improved From Version to Version?](#31-what-actually-improved-from-version-to-version)
- [32. Advantages of YOLO](#32-advantages-of-yolo)
- [33. Limitations](#33-limitations)
- [34. Practical Model Selection Guide](#34-practical-model-selection-guide)
- [35. A Good Learning Path](#35-a-good-learning-path)
- [36. The Biggest Takeaway](#36-the-biggest-takeaway)
- [37. Reference Map](#37-reference-map)
- [38. Citation and Usage Notes](#38-citation-and-usage-notes)
- [39. License](#39-license)

---

## 1. What is YOLO?

**YOLO (You Only Look Once)** is a family of real-time computer-vision models best known for **object detection**.

Object detection answers two questions:

- **What is in the image?** — the object class.
- **Where is it?** — the object's bounding box.

For example:

```text
person       → [x1, y1, x2, y2]
car          → [x1, y1, x2, y2]
traffic light → [x1, y1, x2, y2]
```

The original YOLO paper introduced detection as a **single regression problem**: a single neural network processes the complete image and predicts bounding boxes and class probabilities in one evaluation. That formulation made real-time object detection unusually simple and fast for its time. [1]

### YOLO in one sentence

> **YOLO is a design family for detecting visual objects quickly, with a strong emphasis on the speed–accuracy–deployment trade-off.**

---

# 2. Object Detection Basics Before YOLO

You do not need to know deep learning to understand YOLO, but four concepts are useful.

## 2.1 Classification

Classification answers:

> What is this image?

Example:

```text
image → "cat"
```

There is usually **one class label** for the whole image.

## 2.2 Object Detection

Detection answers:

> Which objects exist, and where are they?

Example:

```text
image
 ├── person → box
 ├── car    → box
 └── dog    → box
```

## 2.3 Segmentation

Segmentation goes further and assigns pixels to objects.

```text
Detection:
[ rectangular box ]

Segmentation:
[ exact object shape ]
```

## 2.4 Pose Estimation

Pose estimation predicts keypoints such as:

```text
head
shoulder
elbow
wrist
hip
knee
ankle
```

Modern YOLO ecosystems support several of these tasks, not only detection. Current Ultralytics YOLO11 and YOLO26 documentation lists detection, segmentation, classification, pose, and oriented bounding boxes; YOLO26 additionally exposes semantic segmentation and monocular depth in its unified task set. [7][8]

---

# 3. What does a YOLO Detector Actually Predict?

A detector can return a set of predictions such as:

```json
[
  {
    "class": "person",
    "confidence": 0.96,
    "box": [105, 72, 318, 540]
  },
  {
    "class": "car",
    "confidence": 0.91,
    "box": [350, 210, 600, 430]
  }
]
```

A production detector therefore needs to solve at least three broad problems:

1. **Feature extraction**
2. **Object localization + classification**
3. **Turning raw predictions into final detections**

That is why YOLO architectures are usually discussed as:

```text
Backbone → Neck → Head → Post-processing / Output
```

<p align="center">
  <img src="assets/modern-yolo-architecture.svg" alt="Backbone, neck, head, and output diagram for a modern YOLO detector." width="100%">
</p>

---

# 4. YOLO Architecture: Backbone, Neck, Head

## 4.1 Backbone

The backbone extracts useful visual features from the image.

Conceptually:

```text
pixels
  ↓
edges / textures
  ↓
shapes
  ↓
parts
  ↓
semantic features
```

Early YOLO generations used Darknet-style networks. Later branches introduced ideas such as CSP-style connections, efficient aggregation, re-parameterization, C2f/C3k2 blocks, and other feature-extraction improvements. [3][4][7][8]

## 4.2 Neck

The neck fuses information from multiple scales.

This matters because:

- a small object needs relatively high-resolution features;
- a large object benefits from deeper semantic features.

FPN/PAN-style multi-scale fusion became a common design pattern across real-time object detectors. [24]

## 4.3 Head

The head turns features into predictions:

```text
features
   ↓
box coordinates
class scores
confidence / objectness
```

One of the biggest changes across YOLO history happened here:

```text
anchor-based
      ↓
anchor-free
      ↓
end-to-end / NMS-free
```

The diagram below summarizes this transition.

<p align="center">
  <img src="assets/head-evolution-anchor-free-e2e.svg" alt="Conceptual diagram of anchor-based, anchor-free, and end-to-end NMS-free detection heads." width="100%">
</p>

---

# 5. Important Metrics

## 5.1 IoU — Intersection over Union

IoU measures the overlap between predicted and ground-truth boxes.

```text
IoU = Area of Intersection / Area of Union
```

A higher IoU means the predicted box is more aligned with the ground truth.

---

## 5.2 AP and mAP

For COCO-style object detection, **AP** is commonly reported as the average precision over IoU thresholds from 0.50 to 0.95.

You may see:

```text
mAP50
```

which refers to AP at IoU = 0.50, while:

```text
mAP50-95
```

is the more demanding COCO-style metric.

**Do not compare mAP numbers without checking the metric.**

---

## 5.3 Parameters

Parameters are the learned weights of the model.

Roughly:

```text
more parameters
   ↕
more capacity / memory / compute
```

but a smaller parameter count does **not** automatically mean a better model.

---

## 5.4 FLOPs

FLOPs estimate computational work.

Lower FLOPs can help efficiency, but actual latency also depends on:

- operator implementation
- GPU/CPU
- runtime
- memory bandwidth
- input resolution
- batch size
- quantization
- post-processing

---

## 5.5 Latency vs FPS

They are related:

```text
FPS ≈ 1000 / latency(ms)
```

for a simple per-image interpretation.

Example:

```text
10 ms → ~100 FPS
5 ms  → ~200 FPS
2 ms  → ~500 FPS
```

But benchmark conditions must always be stated.

---

# 6. YOLOv1 — The Beginning

**Paper:** *You Only Look Once: Unified, Real-Time Object Detection* (2015). [1]

YOLOv1 changed object detection by treating it as a single regression problem.

Instead of a multi-stage pipeline:

```text
image
 ↓
candidate regions
 ↓
classify regions
 ↓
refine boxes
```

YOLO attempted:

```text
image
 ↓
one neural network
 ↓
boxes + classes
```

### Strengths

- Simple end-to-end formulation
- Very fast for its time
- Strong real-time identity

### Weaknesses

- Localization was less precise
- Small objects were difficult
- Multiple close objects could be challenging

### Historical importance

YOLO demonstrated that **speed could be part of the model's core design**, not only an optimization added after the fact. [1]

---

# 7. YOLOv2 / YOLO9000 — Better, Faster, Stronger

**Paper:** *YOLO9000: Better, Faster, Stronger* (2016). [2]

YOLOv2 introduced a large set of improvements, including:

- anchor boxes
- improved training
- better localization
- multi-scale training
- stronger backbone design

YOLO9000 also explored joint detection and classification to greatly expand the number of recognizable categories. [2]

The paper reported a YOLOv2 configuration at **67 FPS / 76.8 mAP on VOC 2007** and another at **40 FPS / 78.6 mAP**. YOLO9000 demonstrated recognition of more than 9,000 categories by combining detection and classification data. [2]

### Architectural lesson

YOLO was no longer just:

> "single-stage = fast"

It was becoming:

> "single-stage + stronger training + better priors + better features."

---

# 8. YOLOv3 — Multi-Scale Detection

**Paper:** *YOLOv3: An Incremental Improvement* (2018). [3]

YOLOv3 introduced a stronger Darknet-53 backbone and **multi-scale prediction**.

Conceptually:

```text
large feature map  → smaller objects
medium feature map → medium objects
small feature map  → larger objects
```

This helped the detector handle objects at different scales more effectively.

### Key ideas

- Darknet-53
- multi-scale prediction
- stronger feature representation
- improved small-object behavior

The paper reported a 320×320 YOLOv3 configuration at **22 ms inference and 28.2 AP**, with substantially stronger AP50. [3]

---

# 9. YOLOv4 — Engineering the Speed/Accuracy Frontier

**Paper:** *YOLOv4: Optimal Speed and Accuracy of Object Detection* (2020). [4]

YOLOv4 combined many improvements rather than relying on one architectural novelty.

Examples included:

- CSP connections
- Weighted Residual Connections
- Cross mini-Batch Normalization
- self-adversarial training
- Mish activation
- Mosaic augmentation
- DropBlock
- CIoU loss

The reported result was **43.5 AP / 65.7 AP50 at ~65 FPS on Tesla V100** for one YOLOv4 configuration. [4]

### Why YOLOv4 matters

It showed how much performance can come from coordinating:

```text
architecture
+
loss
+
augmentation
+
training schedule
+
regularization
+
deployment
```

---

# 10. Scaled-YOLOv4 — Scaling the Network

**Paper:** *Scaled-YOLOv4: Scaling Cross Stage Partial Network* (2020). [5]

The paper explored scaling:

- depth
- width
- resolution
- overall structure

The large YOLOv4 model was reported at **55.5 AP / 73.4 AP50 at ~16 FPS on Tesla V100**, while YOLOv4-tiny was reported at **22.0 AP / 443 FPS on RTX 2080 Ti** in the paper's benchmark. [5]

### Lesson

There is no universal "best" model size.

A model should be selected based on the deployment budget.

---

# 11. YOLOv5 — The Developer-Ecosystem Milestone

**Ultralytics, 2020 onward.**

YOLOv5 is important but should be described carefully:

> It is an Ultralytics YOLO-family implementation/ecosystem, not a formal research-paper continuation written by the original YOLOv1–v4 authors.

Ultralytics' current documentation explicitly notes that it did not publish a formal paper dedicated to YOLOv5. [9]

### Why YOLOv5 became so influential

- PyTorch workflow
- simple CLI/API
- multiple model sizes
- strong community
- convenient export/deployment
- practical training experience

The legacy YOLOv5 family used CSP-style feature extraction, SPPF, PAN-style aggregation, and an anchor-based detection head. [9][10]

### Representative official benchmark

The YOLOv5 README reports for 640×640 COCO:

| Model | mAP50-95 | Params | FLOPs | V100 latency |
|---|---:|---:|---:|---:|
| YOLOv5n | 28.0 | 1.9M | 4.5B | 6.3 ms |
| YOLOv5s | 37.4 | 7.2M | 16.5B | 6.4 ms |
| YOLOv5m | 45.4 | 21.2M | 49.0B | 8.2 ms |
| YOLOv5l | 49.0 | 46.5M | 109.1B | 10.1 ms |
| YOLOv5x | 50.7 | 86.7M | 205.7B | 12.1 ms |

These figures are source-reported V100 measurements; the README states that the GPU speed values use COCO val2017 and that the reported speed excludes about 1 ms of NMS. [9]

---

# 12. YOLOX — A Major Independent Branch

**Paper:** *YOLOX: Exceeding YOLO Series in 2021* (2021). [11]

YOLOX is **not "YOLOv6."** It is an independent and influential YOLO-family branch.

Its central changes include:

- anchor-free detection
- decoupled head
- SimOTA label assignment

The paper reports:

- YOLO-Nano: **0.91M parameters, 1.08G FLOPs, 25.3 AP**
- YOLOX-L: **50.0 AP at 68.9 FPS on Tesla V100**


### Why YOLOX matters

It helped make **anchor-free YOLO-style detection** a mainstream design direction.

---

# 13. PP-YOLOE — PaddlePaddle Ecosystem

PP-YOLOE is another influential YOLO-family line. [12]

It explored:

- anchor-free detection
- stronger training
- improved label assignment
- efficient architecture design

A useful representative benchmark from the Ultralytics comparison page reports PP-YOLOE+:

| Model | mAP50-95 | Params | FLOPs | T4 TensorRT latency |
|---|---:|---:|---:|---:|
| PP-YOLOE+t | 39.9 | 4.85M | 19.15B | 2.84 ms |
| PP-YOLOE+s | 43.7 | 7.93M | 17.36B | 2.62 ms |
| PP-YOLOE+m | 49.8 | 23.43M | 49.91B | 5.56 ms |
| PP-YOLOE+l | 52.9 | 52.2M | 110.07B | 8.36 ms |
| PP-YOLOE+x | 54.7 | 98.42M | 206.59B | 14.3 ms |


---

# 14. YOLOv6 — Industrial and Deployment Focus

YOLOv6 was developed by Meituan as a single-stage detector focused on industrial applications. [13][14]

Its design emphasized:

- EfficientRep-style backbones
- Rep-PAN
- efficient deployment
- hardware-oriented optimization
- later extensions for mobile/CPU and face detection

The YOLOv6 v3.0 benchmark reports:

| Model | mAP50-95 | Params | FLOPs | T4 TensorRT FP16 |
|---|---:|---:|---:|---:|
| YOLOv6-N | 37.5 | 4.7M | 11.4G | 779 FPS |
| YOLOv6-S | 45.0 | 18.5M | 45.3G | 339 FPS |
| YOLOv6-M | 50.0 | 34.9M | 85.8G | 175 FPS |
| YOLOv6-L | 52.8 | 59.6M | 150.7G | 98 FPS |

The project notes that the COCO metrics are from val2017 and the speed tests use TensorRT on T4. [14]

### Architectural idea

One important efficiency concept is **re-parameterization**:

```text
Training:
multi-branch block

       ┌── 3×3 ──┐
input ─┼── 1×1 ──┼→ output
       └── id ───┘

Inference:
        ↓ fuse

        one optimized conv
```

This lets training use a flexible structure while inference can use a simpler one.

---

# 15. YOLOv7 — Trainable Bag-of-Freebies

**Paper:** *YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors* (2022). [15]

YOLOv7 emphasized:

- trainable bag-of-freebies
- re-parameterization
- efficient layer aggregation
- model scaling
- training/inference co-design

The official repository [15][16] reports:

| Model | Input | AP | Batch-1 FPS | Batch-32 avg. |
|---|---:|---:|---:|---:|
| YOLOv7 | 640 | 51.4 | 161 | 2.8 ms |
| YOLOv7-X | 640 | 53.1 | 114 | 4.3 ms |
| YOLOv7-W6 | 1280 | 54.9 | 84 | 7.6 ms |
| YOLOv7-E6 | 1280 | 56.0 | 56 | 12.3 ms |
| YOLOv7-D6 | 1280 | 56.6 | 44 | 15.0 ms |
| YOLOv7-E6E | 1280 | 56.8 | 36 | 18.7 ms |


### Big lesson

YOLOv7 made the idea of a **training–inference gap** especially visible:

> Training can be complicated if that complexity improves the final inference model.

---

# 16. YOLOv8 — The Modern Ultralytics Baseline

**Released:** January 2023.

YOLOv8 broadened the practical YOLO ecosystem considerably and supports:

- detection
- instance segmentation
- classification
- pose
- oriented bounding boxes

The Ultralytics documentation describes the major shift toward **anchor-free detection**, redesigned heads, and C2f-based architecture. [17]

### Official benchmark

| Model | mAP50-95 | Params | FLOPs | A100 TensorRT latency |
|---|---:|---:|---:|---:|
| YOLOv8n | 37.3 | 3.2M | 8.7B | 0.99 ms |
| YOLOv8s | 44.9 | 11.2M | 28.6B | 1.20 ms |
| YOLOv8m | 50.2 | 25.9M | 78.9B | 1.83 ms |
| YOLOv8l | 52.9 | 43.7M | 165.2B | 2.39 ms |
| YOLOv8x | 53.9 | 68.2M | 257.8B | 3.53 ms |


### Why v8 became popular

It packaged many practical capabilities behind one ecosystem:

```text
train()
val()
predict()
export()
track()
segment()
pose()
OBB()
```

That developer experience is a major part of its success.

---

# 17. YOLOv9 — PGI + GELAN

**Paper:** *YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information* (2024). [18]

YOLOv9 introduced:

### PGI — Programmable Gradient Information

The idea is to provide the training process with more reliable information for gradient calculation.

### GELAN — Generalized Efficient Layer Aggregation Network

GELAN focuses on efficient information aggregation and gradient-path design.

The official implementation [19] reports:

| Model | mAP | Params | FLOPs |
|---|---:|---:|---:|
| YOLOv9-T | 38.3 | 2.0M | 7.7G |
| YOLOv9-S | 46.8 | 7.1M | 26.4G |
| YOLOv9-M | 51.4 | 20.0M | 76.3G |
| YOLOv9-C | 53.0 | 25.3M | 102.1G |
| YOLOv9-E | 55.6 | 57.3M | 189.0G |


The README does not provide a directly comparable latency column in the same table, which is why latency is intentionally left out rather than guessed.

---

# 18. YOLOv10 — End-to-End NMS-Free Detection

**Paper:** *YOLOv10: Real-Time End-to-End Object Detection* (2024). [20]

One of YOLOv10's main contributions is the attempt to eliminate the need for traditional NMS in the default detection path.

Traditional:

```text
network
  ↓
many predictions
  ↓
NMS
  ↓
final detections
```

YOLOv10:

```text
network
  ↓
end-to-end predictions
  ↓
final detections
```

The paper introduces **consistent dual assignments** for NMS-free training and a more holistic accuracy/efficiency redesign. [20]

A current Ultralytics comparison page [21] reports the following representative values:

| Model | mAP50-95 | Params | FLOPs | T4 TensorRT10 |
|---|---:|---:|---:|---:|
| YOLOv10n | 39.5 | 2.3M | 6.7B | 1.56 ms |
| YOLOv10s | 46.7 | 7.2M | 21.6B | 2.66 ms |
| YOLOv10m | 51.3 | 15.4M | 59.1B | 5.48 ms |
| YOLOv10b | 52.7 | 24.4M | 92.0B | 6.54 ms |
| YOLOv10l | 53.3 | 29.5M | 120.3B | 8.33 ms |
| YOLOv10x | 54.4 | 56.9M | 160.4B | 12.2 ms |


---

# 19. YOLO11 — More Efficient Ultralytics Models

**Released:** September 10, 2024.

YOLO11 refined the Ultralytics architecture and training pipeline with an emphasis on accuracy per parameter and deployment efficiency. [22]

The official documentation [22] reports:

| Model | mAP50-95 | Params | FLOPs | T4 TensorRT10 |
|---|---:|---:|---:|---:|
| YOLO11n | 39.5 | 2.6M | 6.5B | 1.5 ms |
| YOLO11s | 47.0 | 9.4M | 21.5B | 2.5 ms |
| YOLO11m | 51.5 | 20.1M | 68.0B | 4.7 ms |
| YOLO11l | 53.4 | 25.3M | 86.9B | 6.2 ms |
| YOLO11x | 54.7 | 56.9M | 194.9B | 11.3 ms |


Ultralytics specifically highlights that **YOLO11m achieves higher COCO mAP than YOLOv8m with 22% fewer parameters**. [22]

### Tasks supported

- detection
- segmentation
- classification
- pose
- OBB


> Ultralytics states that it did not publish a formal research paper dedicated to YOLO11; the project is documented and cited as software. [22]

---

# 20. YOLO12 — Attention-Centric Research Direction

**Paper:** *YOLOv12: Attention-Centric Real-Time Object Detectors* (2025). [23]

YOLO12 is best understood as a **research branch**, not simply "the next production Ultralytics version after YOLO11".

Its central theme is bringing more **attention-centric design** into real-time detection.

This is interesting because classic YOLO development was historically dominated by convolutional architectures, while modern vision models increasingly use attention mechanisms.

The key question becomes:

> Can attention improve feature interaction without sacrificing real-time latency?

That research direction is important even when choosing a different YOLO model for production.

---

# 21. YOLO26 — Current Ultralytics Direction

**Ultralytics, 2026.**

As of August 2026, the current Ultralytics documentation describes **YOLO26** as a unified real-time vision family. [8]

Its main ideas are:

### 21.1 Native end-to-end inference

The default one-to-one head produces predictions without NMS.

### 21.2 DFL-free regression

YOLO26 removes Distribution Focal Loss from its default detection head.

### 21.3 New training recipe

The documented recipe combines:

- **MuSGD**
- **Progressive Loss**
- **STAL — Small-Target-Aware Label Assignment**

### 21.4 Task-specific heads

The unified family covers detection, segmentation, semantic segmentation, depth, classification, pose, and OBB. [8]

### Official benchmark

| Model | mAP50-95 | E2E mAP | Params | FLOPs | CPU ONNX | T4 TensorRT10 |
|---|---:|---:|---:|---:|---:|---:|
| YOLO26n | 40.9 | 40.1 | 2.4M | 5.4B | 38.9 ms | 1.7 ms |
| YOLO26s | 48.6 | 47.8 | 9.5M | 20.7B | 87.2 ms | 2.5 ms |
| YOLO26m | 53.1 | 52.5 | 20.4M | 68.2B | 220.0 ms | 4.7 ms |
| YOLO26l | 55.0 | 54.4 | 24.8M | 86.4B | 286.2 ms | 6.2 ms |
| YOLO26x | 57.5 | 56.9 | 55.7M | 193.9B | 525.8 ms | 11.8 ms |


**Important:** Ultralytics states that its Params/FLOPs values are for the **fused model**, where Conv+BN are fused and the auxiliary one-to-many head is removed. [8]

That makes the table more precise, but it also means the numbers should not be blindly compared with an unrelated paper's raw model count.

---

# 22. NMS-Free Is Not the Same as "No Alternative Head"

An interesting detail in YOLO26 is that the model has a **dual-head architecture**:

- **one-to-one head:** default, end-to-end and NMS-free
- **one-to-many head:** traditional-style output that can still use NMS

Ultralytics documents that the one-to-one head prioritizes speed and simplicity, while the one-to-many head can be used when accuracy is the primary concern. [8]

This is a good example of why implementation details matter when discussing "NMS-free YOLO."

---

# 23. YOLO-World — Open-Vocabulary Detection

Traditional detectors generally learn a fixed class set.

For example:

```text
person
car
dog
cat
...
```

YOLO-World introduced an important extension:

> **Detect objects described by language rather than only a fixed training-time label list.**

The paper uses vision-language modeling and introduces **RepVL-PAN** and region-text contrastive learning. [25]

On LVIS, the paper reports **35.4 AP at 52.0 FPS on V100** in its stated benchmark. [25]

Conceptually:

```text
image + text prompt
       ↓
  YOLO-World
       ↓
"helmet", "backpack", "drone", ...
```

### Why this matters

This changes the problem from:

> "Which predefined classes are present?"

to:

> "Which objects matching my description are present?"

---

# 24. YOLOE — Real-Time "Seeing Anything"

YOLOE extends the open-vocabulary direction.

The research supports different prompt modes:

- text prompts
- visual prompts
- prompt-free recognition

The paper [26] introduces components such as:

- RepRTA
- SAVPE
- LRPC


This is a major conceptual step for applications where the target categories change after deployment.

---

# 25. YOLOE-26 — Open Vocabulary Meets End-to-End YOLO26

The current YOLO26 documentation also describes **YOLOE-26**, which combines open-vocabulary capability with the YOLO26 end-to-end design. [8]

Ultralytics reports YOLOE-26x results on LVIS minival under text prompting, visual prompting, and prompt-free settings. [8]

This is an important direction:

```text
YOLO26
  +
open vocabulary
  ↓
dynamic classes
  +
NMS-free deployment path
```

---

# 26. The Most Important Non-Official / Independent YOLO Branches

The YOLO ecosystem is much larger than the numbered sequence alone.

## YOLOX

**Main ideas:**

- anchor-free
- decoupled head
- SimOTA

[11]

**Why famous?**

It became one of the strongest independent real-time YOLO-style detectors and strongly influenced the anchor-free transition.

---

## PP-YOLOE

**Main ideas:**

- anchor-free
- efficient architecture
- strong training recipes
- PaddlePaddle ecosystem

[12]

**Why useful?**

A good example of how teams outside the Ultralytics ecosystem independently pushed the YOLO design space.

---

## YOLOv6

**Main ideas:**

- industrial deployment
- EfficientRep
- Rep-PAN
- quantization
- deployment-oriented optimizations

[13][14]

---

## YOLOv7

**Main ideas:**

- trainable bag-of-freebies
- model scaling
- re-parameterization
- efficient aggregation

[15]

---

## YOLOv9

**Main ideas:**

- GELAN
- PGI

[18][19]

---

## YOLOv10

**Main ideas:**

- consistent dual assignments
- NMS-free end-to-end design
- holistic efficiency/accuracy optimization

[20]

---

## YOLO-World

**Main idea:**

- open-vocabulary detection
- vision-language interaction

[25]

---

## YOLOE

**Main idea:**

- text / visual / prompt-free open-vocabulary detection

[26]

---

## YOLO-NAS

Another well-known YOLO-style branch is **YOLO-NAS**, from Deci, which uses neural architecture search to discover architecture configurations optimized for accuracy and efficiency.

It is useful as an example of a different philosophy:

> instead of manually designing every block, use automated architecture search to explore the design space.

---

# 27. Why There Is No Single "Best YOLO"

A common beginner question is:

> "Which YOLO is the best?"

The correct answer is:

> **Best for what?**

For example:

| Goal | What matters most |
|---|---|
| CCTV on CPU | latency + model size |
| Edge device | memory + supported runtime |
| Drone detection | small objects + speed |
| Industrial inspection | accuracy + deployment stability |
| Open-vocabulary detection | language/visual prompting |
| Research | architectural flexibility |
| Mobile | compute + memory + export support |
| Real-time tracking | detector latency + tracker integration |

A model with the highest mAP may be the wrong choice if it cannot run fast enough on your hardware.

---

# 28. Reading the Benchmark Table Correctly

A benchmark table can be misleading if you ignore the test setup.

For example:

```text
Model A
50 mAP
2 ms
```

looks better than:

```text
Model B
50 mAP
4 ms
```

But you still need to ask:

- Which GPU?
- Which runtime?
- Which precision?
- Which image size?
- Batch 1 or batch 32?
- Does latency include NMS?
- Are both models evaluated on the same COCO split?
- Are both metrics computed using the same evaluation pipeline?

This is why this guide **does not present every historical benchmark as one giant universal leaderboard**.

---

# 29. Representative Benchmark Table

The following table is deliberately limited to **representative source-reported configurations**.

<p align="center">
  <img src="assets/representative-benchmark-table.svg" alt="Representative benchmark comparison of selected YOLO generations, with mAP, parameter count, FLOPs and latency conditions." width="100%">
</p>

| Model | Input | mAP50-95 | Params | FLOPs | Reported speed |
|---|---:|---:|---:|---:|---|
| YOLOv5s | 640 | 37.4 | 7.2M | 16.5B | 6.4 ms V100 |
| YOLOv6-S | 640 | 45.0 | 18.5M | 45.3G | 339 FPS T4 |
| YOLOv7 | 640 | 51.4 | — | — | 161 FPS |
| YOLOv8s | 640 | 44.9 | 11.2M | 28.6B | 1.20 ms A100 TRT |
| YOLOv9-S | 640 | 46.8 | 7.1M | 26.4G | not given in table |
| YOLOv10s | 640 | 46.7 | 7.2M | 21.6B | 2.66 ms T4 TRT10 |
| YOLO11s | 640 | 47.0 | 9.4M | 21.5B | 2.5 ms T4 TRT10 |
| YOLO26s | 640 | 48.6 | 9.5M | 20.7B | 2.5 ms T4 TRT10 |

### Benchmark sources

- YOLOv5: Ultralytics README. [9]
- YOLOv6: Meituan README. [14]
- YOLOv7: official repository. [16]
- YOLOv8: Ultralytics documentation. [17]
- YOLOv9: official repository. [19]
- YOLOv10: Ultralytics comparison page. [21]
- YOLO11: Ultralytics documentation. [22]
- YOLO26: Ultralytics documentation. [8]

### Important warning

**Do not treat this table as an apples-to-apples leaderboard.**

The source environments are different:

- V100 vs T4 vs A100
- TensorRT versions differ
- some rows report FPS, others latency
- batch size can differ
- post-processing treatment can differ

The table is best used for understanding **scale, capacity, and reported efficiency**, not for claiming that one row is universally faster than another.

---

# 30. Architecture Evolution Summary

The broad architectural story is:

```text
YOLOv1
single-stage regression
        ↓
YOLOv2
anchors + improved training
        ↓
YOLOv3
multi-scale prediction
        ↓
YOLOv4
CSP + training/augmentation engineering
        ↓
YOLOv5
practical PyTorch ecosystem
        ↓
YOLOX / v6 / v7
anchor-free + deployment + re-parameterization
        ↓
YOLOv8
anchor-free + modern multi-task ecosystem
        ↓
YOLOv9
GELAN + PGI
        ↓
YOLOv10
end-to-end / NMS-free direction
        ↓
YOLO11
more efficient Ultralytics generation
        ↓
YOLO12
attention-centric research direction
        ↓
YOLO26
NMS-free + DFL-free + modern training recipe
        ↓
YOLOE / YOLOE-26
open-vocabulary detection
```

Again, this is a **conceptual map**, not a strict source-code inheritance graph.

---

# 31. What Actually Improved From Version to Version?

It is tempting to say:

> "Every version just became more accurate."

That is not the full story.

YOLO improvements happened in many areas:

### Backbone

Better feature extraction.

### Neck

Better multi-scale information fusion.

### Head

Better representation of boxes and classes.

### Label assignment

Better answers to:

> Which predicted locations should be treated as positives?

### Loss functions

Better optimization targets.

### Training

Better augmentation, schedules, distillation, and optimization.

### Post-processing

Less dependence on NMS.

### Deployment

Better export, quantization, fusion, and hardware compatibility.

### Task coverage

Detection → segmentation → pose → OBB → depth.

### Vocabulary

Fixed class labels → open vocabulary.

This is the real evolution of the family.

---

# 32. Advantages of YOLO

## Speed

YOLO was created around real-time detection and remains strong when latency matters.

## Versatility

Modern YOLO ecosystems cover several vision tasks.

## Model-size choices

Nano-to-extra-large variants make deployment more flexible.

## Ecosystem

The family has an enormous developer and research ecosystem.

## Deployment

Modern implementations commonly support exports such as ONNX, TensorRT, OpenVINO, CoreML, and edge-oriented runtimes, depending on the specific project/version. [7][8]

## Custom training

YOLO models are widely used for custom datasets, from industrial inspection to drones and robotics.

---

# 33. Limitations

## Small objects remain difficult

Tiny, blurred, or heavily occluded objects remain challenging.

## Benchmarks can be misleading

Hardware and runtime differences can dominate real-world latency.

## "YOLO" is not one codebase

Different branches can have different licenses, architectures, benchmark conventions, and APIs.

## Licensing matters

In particular, current Ultralytics documentation states that YOLO11 and YOLO26 are distributed under **AGPL-3.0 and Enterprise licensing options**. Check the exact repository and model license before commercial deployment. [22][8]

## Higher mAP is not always better for deployment

An edge application may prefer a lower-mAP model if it is dramatically faster and smaller.

---

# 34. Practical Model Selection Guide

## If you are a beginner

Start with a well-documented current implementation such as:

- YOLO11
- YOLO26

because the tooling and docs are integrated. [7][8]

## If you want to understand the research evolution

Study:

1. YOLOv1
2. YOLOv3
3. YOLOv4
4. YOLOX
5. YOLOv7
6. YOLOv9
7. YOLOv10

This sequence exposes most of the important architectural ideas.

## If you care about open vocabulary

Study:

- YOLO-World
- YOLOE
- YOLOE-26

## If you care about edge deployment

Pay attention to:

- model size
- FLOPs
- actual target-hardware latency
- export runtime
- quantization
- NMS/post-processing
- memory footprint

---

# 35. A Good Learning Path

If you are learning YOLO from zero:

```text
Step 1
What is classification?

Step 2
What is object detection?

Step 3
Bounding boxes + IoU + AP

Step 4
YOLOv1 single-stage idea

Step 5
CNN feature maps

Step 6
Backbone / neck / head

Step 7
YOLOv3 multi-scale detection

Step 8
CSP / PAN / SPPF

Step 9
Anchor-based vs anchor-free

Step 10
YOLOv8

Step 11
YOLOv9: GELAN + PGI

Step 12
YOLOv10: NMS-free direction

Step 13
YOLO11 / YOLO26

Step 14
YOLO-World / YOLOE
```

This order gives you the conceptual reasons behind the changes instead of asking you to memorize version numbers.

---

# 36. The Biggest Takeaway

The most useful way to study YOLO is **not**:

> "What changed from v10 to v11?"

It is:

> **Which part of the detection pipeline changed, and why?**

For example:

```text
Feature extraction
      ↓
multi-scale fusion
      ↓
box representation
      ↓
label assignment
      ↓
loss
      ↓
training
      ↓
post-processing
      ↓
deployment
      ↓
open vocabulary
```

Once you start thinking this way, YOLO versions stop looking like a list of names and start looking like a history of solutions to recurring computer-vision problems.

---

# 37. Reference Map

This work uses primary papers and official project documentation wherever possible.

## Foundational YOLO papers

**[1] Redmon et al. — You Only Look Once: Unified, Real-Time Object Detection (2015)**  
https://arxiv.org/abs/1506.02640

**[2] Redmon & Farhadi — YOLO9000: Better, Faster, Stronger (2016)**  
https://arxiv.org/abs/1612.08242

**[3] Redmon & Farhadi — YOLOv3: An Incremental Improvement (2018)**  
https://arxiv.org/abs/1804.02767

**[4] Bochkovskiy et al. — YOLOv4: Optimal Speed and Accuracy of Object Detection (2020)**  
https://arxiv.org/abs/2004.10934

**[5] Wang et al. — Scaled-YOLOv4: Scaling Cross Stage Partial Network (2020)**  
https://arxiv.org/abs/2011.08036

## YOLO family branches and implementations

**[6] Ultralytics YOLOv5 repository**  
https://github.com/ultralytics/yolov5

**[7] Ultralytics YOLO documentation**  
https://docs.ultralytics.com/

**[8] Ultralytics YOLO26 documentation**  
https://docs.ultralytics.com/models/yolo26

**[9] Ultralytics YOLOv5 README / benchmark tables**  
https://github.com/ultralytics/yolov5/blob/master/README.md

**[10] Ultralytics YOLOv5 architecture description**  
https://github.com/ultralytics/ultralytics/blob/main/docs/en/yolov5/tutorials/architecture-description.md

**[11] Ge et al. — YOLOX: Exceeding YOLO Series in 2021**  
https://arxiv.org/abs/2107.08430

**[12] Ultralytics comparison: PP-YOLOE vs YOLOv8**  
https://docs.ultralytics.com/compare/pp-yoloe-vs-yolov8

**[13] Li et al. — YOLOv6: A Single-Stage Object Detection Framework for Industrial Applications**  
https://arxiv.org/abs/2209.02976

**[14] Meituan YOLOv6 repository and benchmark tables**  
https://github.com/meituan/YOLOv6

**[15] Wang et al. — YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors**  
https://arxiv.org/abs/2207.02696

**[16] Official YOLOv7 repository / benchmark**  
https://github.com/WongKinYiu/yolov7

**[17] Ultralytics YOLOv8 documentation**  
https://docs.ultralytics.com/models/yolov8

**[18] Wang et al. — YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information**  
https://arxiv.org/abs/2402.13616

**[19] Official YOLOv9 repository / benchmark**  
https://github.com/WongKinYiu/yolov9

**[20] Wang et al. — YOLOv10: Real-Time End-to-End Object Detection**  
https://arxiv.org/abs/2405.14458

**[21] Ultralytics YOLOv8 vs YOLOv10 benchmark comparison**  
https://docs.ultralytics.com/compare/yolov8-vs-yolov10

**[22] Ultralytics YOLO11 documentation and official benchmark**  
https://docs.ultralytics.com/models/yolo11

**[23] Tian et al. — YOLOv12: Attention-Centric Real-Time Object Detectors**  
https://arxiv.org/abs/2502.12524

## Open-vocabulary branches

**[24] Lin et al. — Feature Pyramid Networks for Object Detection**  
https://arxiv.org/abs/1612.03144

**[25] Cheng et al. — YOLO-World: Real-Time Open-Vocabulary Object Detection**  
https://arxiv.org/abs/2401.17270

**[26] Wang et al. — YOLOE: Real-Time Seeing Anything**  
https://arxiv.org/abs/2503.07465

---

# 38. Citation and Usage Notes

### Research citations

For research writing, cite the paper corresponding to the exact architecture you used.

### Software citations

For software-based experiments, cite the official repository/documentation in addition to the paper when one exists.

### Benchmark rule

Never copy an isolated metric from one source and present it as a universal speed/accuracy ranking.

Always record:

```text
dataset
input size
model variant
runtime
hardware
precision
batch size
post-processing
metric definition
```

That is the difference between a benchmark table that looks impressive and one that is actually useful.

---

# 39. License

This work is licensed under the **MIT License**.

Copyright © 2026 **Ahmad J. Zahed**.

For the full license terms, see the [LICENSE](./LICENSE) file.

> **Third-party materials:** YOLO implementations, models, datasets, papers, trademarks, and other referenced materials may be subject to their own licenses and terms. The MIT License of this repository does not override or replace those licenses.
