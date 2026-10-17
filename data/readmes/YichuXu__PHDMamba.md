

<p align="center">

  <h2 align="center"><strong>PHDMamba: Progressive Hybrid Mamba for
Hyperspectral Image Classification</strong></h2>

<div align="center">
<h5>

<em>Yichu Xu<sup>1</sup>, Chengxi Han<sup>1</sup>, Shi Chen<sup>1</sup>, Yao Jin<sup>1</sup>, Yuchun Miao<sup>1</sup>, Haonan Guo<sup>1</sup>, Di Wang<sup>1 †</sup> </em>
    <br><br>
       	<sup>1</sup> Wuhan University, China, <sup>†</sup>Corresponding author <br> 
    </h5>
[![GRSL paper](https://img.shields.io/badge/GRSL-paper-00629B.svg)](https://ieeexplore.ieee.org/document/11222630) 
</div>



## 📖Overview

* [**PHDMamba**](https://ieeexplore.ieee.org/document/11222630) is a Progressive Hybrid Mamba Module, which performs
stage-wise modeling of long-range dependencies along both spectral
and spatial dimensions. In addition, a dedicated Spectral-Spatial Interaction Module is introduced to adaptively integrate
contextual spectral and spatial features. 

<div align="center">
  <img src="./figures/PHDMamba.png"><br><br>
</div>

## 🚀Let's Get Started!
### `A. Installation`
**Step 1: Clone the repository:**

Clone this repository and navigate to the project directory:
```bash
git clone https://github.com/YichuXu/PHDMamba.git
cd PHDMamba
```

**Step 2: Environment Setup:**

It is recommended to set up a conda environment and installing dependencies via pip. Use the following commands to set up your environment:

***Create and activate a new conda environment***

```bash
conda create -n PHDMamba
conda activate PHDMamba
```

***Install dependencies***

Our method uses python 3.8, pytorch 1.13, other environments are in requirements.txt

**Please use the following mamba version: mamba_ssm==1.2.0 !**
```bash
pip install -r requirements.txt
cd kernels/selective_scan && pip install .
```

### `B. Data Preparation`

Download HSI classification dataset from [Google Drive](https://drive.google.com/drive/folders/1iPFLdrAFUveqwCtMpf5859pQhGXN_z4J?usp=drive_link) or [Baidu Drive (百度网盘)](https://pan.baidu.com/s/1bSqq-Uv3AC5qfRmqxbMjfg?pwd=2025) and put it under the [dataset] folder. It will have the following structure: 
```
${DATASET_ROOT}   # Dataset root directory
├── datasets
│   │
│   ├── pu        # Pavia University data
│   │   ├──PaviaU.mat
│   │   ├──PaviaU_gt.mat
│   │
│   ├── houston13  # Houston 2013 data
│   │   ├──GRSS2013.mat
│   │   ├──GRSS2013_gt.mat 
│   │     
│   ├── whuhc     # Whu-HanChuan data
│   │   ├──WHU_Hi_HanChuan.mat
│   │   ├──WHU_Hi_HanChuan_gt.mat 
│   │
│   ├── other HSI Datasets   
│   │   ├ ... 
│   │    

```

### `C. Performance Evaluation`
- The following commands show how to generate training samples:
```bash
python GenSample.py --train_num 15 --dataID 1
python GenSample.py --train_num 15 --dataID 3
python GenSample.py --train_num 30 --dataID 6
```

- The following commands show how to train and evaluate PHDMamba for HSI classification:
```bash
CUDA_VISIBLE_DEVICES=0 python  main.py --model PHDMamba --dataID 1 --epoch 200 --lr 1e-3 --decay 0 --split False --dataset_name pu --train_num 15
CUDA_VISIBLE_DEVICES=0 python  main.py --model PHDMamba --dataID 3 --epoch 200 --lr 1e-3 --decay 0 --split False --dataset_name houston13 --train_num 15
CUDA_VISIBLE_DEVICES=0 python  main.py --model PHDMamba --dataID 6 --epoch 200 --lr 1e-3 --decay 0 --split False --dataset_name whuhc --train_num 30
```

## 🤠Results Taken Away

* *The visualization results are provided in the results folder.*

* *We'd appreciate it if you could give this repo a ⭐️**star**⭐️ and stay tuned.*





## 📜Reference

if you find it useful for your research, please consider giving this repo a ⭐ and citing our paper! We appreciate your support！😊
```
@ARTICLE{Xu2025PHDMamba,
  author={Xu, Yichu and Han, Chengxi and Chen, Shi and Jin, Yao and Miao, Yuchun and Guo, Haonan and Wang, Di},
  journal={IEEE Geoscience and Remote Sensing Letters}, 
  title={PHDMamba: Progressive Hybrid Mamba for Hyperspectral Image Classification}, 
  year={2025},
  volume={22},
  number={},
  pages={1-5}
  }

```

## 🙋Q & A
**For any questions, please [contact us.](mailto:xuyichu@whu.edu.cn)**

[![Star History Chart](https://api.star-history.com/svg?repos=YichuXu/PHDMamba&type=Date)](https://star-history.com/#YichuXu/PHDMamba&Date)


