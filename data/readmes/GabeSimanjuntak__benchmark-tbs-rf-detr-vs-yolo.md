# Benchmark Lintas Domain Deteksi Kematangan Tandan Buah Segar Kelapa Sawit: RF-DETR vs YOLO pada Data Pabrik dan Kebun

## 1. Deskripsi Project

Penelitian ini bertujuan untuk membandingkan kemampuan model object detection RF-DETR, YOLO11, dan YOLOv8 dalam mendeteksi tingkat kematangan Tandan Buah Segar (TBS) kelapa sawit pada lingkungan dan domain yang berbeda.

Penelitian berfokus pada kemampuan generalisasi model melalui pengujian lintas dataset dari lingkungan pabrik dan perkebunan di Indonesia serta Malaysia.

## 2. Tujuan Penelitian

1. Menyelaraskan taksonomi kelas dari tiga dataset publik.
2. Menguji generalisasi model pada skenario lintas domain.
3. Membandingkan performa RF-DETR, YOLO11, dan YOLOv8.
4. Mengevaluasi akurasi dan kecepatan inferensi model.

## 3. Dataset

1. TBS Pabrik Kalimantan Selatan (2023).
2. TBS Kebun Kalimantan Tengah (2025).
3. Outdoor Oil Palm Malaysia (2024).

## 4. Models

- RF-DETR
- YOLO11
- YOLOv8

## 5. Evaluation Metrics

- mAP@0.5
- mAP@0.5:0.95
- FPS (Frames Per Second)

## 6. Repository Structure

- `datasets/`: Dataset documentation.
- `notebooks/`: Experiment notebooks.
- `src/`: Source code.
- `configs/`: Experiment configurations.
- `results/`: Experiment results.
- `docs/`: Research documentation.

## 7. Research Environment

- Python
- Google Colab
- PyTorch
- GitHub

## 8. Project Status

Currently in the initial preparation and dataset collection stage.