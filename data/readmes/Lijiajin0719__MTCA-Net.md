# MTCA-Net

A multi-task cascaded analysis network (MTCA-Net) for real-time tracking and segmentating sperm under high-resolution conditions.

## 📄 Corresponding Publication
This repository contains the implementation of the method described in our paper:

***MTCA-Net: Multi-Task Cascade Analysis Network for Real-Time Sperm Quality Analysis***

## 🛠 Environment Setup

This project requires Python 3.9 and PyTorch 2.0.1. Follow these steps to set up the environment:

### 1. Clone Repository
```bash
git clone https://github.com/Lijiajin0719/MTCA-Net.git
cd MTCA-Net
```
### 2. Create Conda Environment
```bash
conda create -n MTCA-Net python=3.9
conda activate MTCA-Net
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
## 📊 Dataset
1.Download datasets from **[SHDet](https://www.kaggle.com/datasets/lijiajin521314/sperm-head-detection-shdet-dataset)**, **[SHSeg](https://www.kaggle.com/datasets/lijiajin521314/sperm-head-segmentation-shseg-dataset)** and **[SHSegHR](https://www.kaggle.com/datasets/lijiajin521314/high-resolution-sperm-head-seg-shseghr-dataset)**

2.Extract files to the **datasets** directory

## 🏋️ MTCA-Net train/test
### 1. Train
#### (1) Train Detection Module
```bash
python train_detect.py
```
To see more intermediate results, check out `./runs/detect/AMF-YOLO...`.

#### (2) Train Segmentation Module
```bash
python train_seg.py --batch_size 32 --epochs 300 --val_interval 5 --save_interval 50
```
To see more intermediate results, check out `./seg/run/Effusion_U2Net...`.

### 2. Test
#### (1) Test Detection Module
```bash
python test_detect.py
```
The test results will be saved to file here: `./runs/detect/test...`.

#### (2) Test Segmentation Module
```bash
python test_seg.py --model_path seg/run/EffiFusion_U2Net_.../weights/best_model.pth --ap50_threshold 0.5
```
The test results will be saved to file here: `./seg/run/EffiFusion_U2Net_test...`.

#### (3) Test MTCA-Net
```bash
python test_MTCA.py --detect_model_path runs/detect/AMF-YOLO/weights/best.pt --seg_model_path seg/run/EffiFusion_U2Net_test.../weights/best_model.pth --conf_threshold 0.6 --seg_threshold 0.5
```
The test results will be saved to file here: `./MTCA-Net/run/...`.

## 📧 Contact
For any questions regarding the paper or this implementation, please feel free to contact the authors.

📩 **Email:** [15563866837@163.com](15563866837@163.com)

## 📚 Acknowledgements
Our codebase is built with references to the following open-source projects:
- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics): The most popular real-time object detection model repository.

We sincerely appreciate the authors for open-sourcing their valuable work.

## 📝 Citation
If you use this code for your research, please cite our paper.
```bash
@article{
  title={MTCA-Net: Multi-Task Cascade Analysis Network for Real-Time Sperm Quality Analysis},
  author={Li, Jiajin and Sun, Wenwen and He, Jun and Fan, Xinyu and Ge, Xuecheng and Lu, Fengya and Wang, Yadan and Wang, Yi and Zhang, Zhiguo and Wu, Qibing and Zhou, Jinhua},
  journal={Advanced Intelligent Systems},
  pages={e202501452},
  year={2026},
  doi={https://doi.org/10.1002/aisy.202501452},
  url={https://advanced.onlinelibrary.wiley.com/doi/abs/10.1002/aisy.202501452},
  publisher={Wiley Online Library}
}
```

---
*🌟 We appreciate your interest in our work!*
