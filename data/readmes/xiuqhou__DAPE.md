**DAPE**
===

By [Xiuquan Hou](https://github.com/xiuqhou), [Meiqin Liu](https://scholar.google.com/citations?user=T07OWMkAAAAJ&hl=zh-CN&oi=ao), Senlin Zhang, [Shaoyi Du](https://scholar.google.com/citations?user=r2bk4sQAAAAJ&hl=zh-CN&oi=ao).

This repo is the official implementation of **DAPE: Harmonizing Content-Position Encoding for Versatile Dense Visual Prediction** accepted to **AAAI2026** (score **76665**).

💖 If our [DAPE](https://github.com/xiuqhou/DAPE) is helpful to your researches or projects, please star this repository. Thanks! 🤗

### Feature

- **Harmonized Sampling**: Strictly aligning content and position distributions for superior Transformer performance.
- **Memory-Efficient Training**: Reducing VRAM usage via low-rank positional encoder.
- **Unified Architecture**: One architecture for detection and all-in-one segmentation (semantic/instance/panoptic).

<div align="center">
  <img src="images/dist_compare.png" height="154">
  <img src="images/ap_comparison.png" height="154">

  <img src="images/dape.png" width="700">
</div>

## Update

- [2026-01-13] Code for semantic segmentation and panoptic segmentation is available now!
- [2026-01-07] We release the configs and weights for large relation ranks, which further increases the performance. 
- [2026-01-07] Code for object detection and instance segmentation is available now!
- [2024-01-06] The pretrained weights for DAPE are available [here](https://github.com/xiuqhou/DAPE/releases/tag/v1.0.0)!
- [2025-11-08] DAPE is accepted to AAAI2026.

## Model ZOO

### Object Detection

#### COCO
| Model               | Backbone             | Epoch |                                                                                                                                                 Download                                                                                                                                                 |  mAP  | AP<sub>50 | AP<sub>75 | AP<sub>S | AP<sub>M | AP<sub>L |
| ------------------- | -------------------- | :---: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---: | :-------: | :-------: | :------: | :------: | :------: |
| DAPE       | ResNet50             |  12   | [config](configs/dape/object_detection/coco/dape_r50_rank16_coco_1x.py) / [checkpoint](https://github.com/xiuqhou/DAPE/releases/download/v1.0.0/dape_r50_rank16_coco_1x.pth) |  51.8 |   69.7  |   56.5  |  36.0  |  55.5  |  66.0  |
| DAPE<sub>r=64       | ResNet50  |  12   | [config](configs/dape/object_detection/coco/dape_r50_rank64_coco_1x.py)  /  [checkpoint](https://github.com/xiuqhou/DAPE/releases/download/v1.0.0/dape_r50_rank64_coco_1x.pth)                                                      | 51.9  |   69.5    |   56.5    |   35.7   |   55.7   |   66.4   |
| DAPE<sub>r=128      | ResNet50  |  12   | [config](configs/dape/object_detection/coco/dape_r50_rank128_coco_1x.py) / [checkpoint](https://github.com/xiuqhou/DAPE/releases/download/v1.0.0/dape_r50_rank128_coco_1x.pth)  |  52.0   |  69.7  |  56.8  |  36.3  |  55.5  | 66.1 |

### Instance Segmentation
#### COCO
| Model               | Backbone             | Epoch |                                                                                                                                                 Download                                                                                                                                                 |  mAP<sup>m | mAP<sup>b | <h>AP<sub>50</h><sup>m | <h>AP<sub>75</h><sup>m | <h>AP<sub>S</h><sup>m | <h>AP<sub>M</h><sup>m | <h>AP<sub>L</h><sup>m |
| ------------------- | -------------------- | :---: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---: | :-------: | :-------: | :------: | :------: | :------: | :------: |
| Mask-DAPE       | ResNet50             |  12   | [config](configs/dape/instance_segmentation/coco/mask_dape_r50_ins_seg_coco_1x.py) / [checkpoint](https://github.com/xiuqhou/DAPE/releases/download/v1.0.0/mask_dape_r50_rank16_ins_seg_coco_1x.pth) | 44.3  |   50.6  |  66.2   | 47.7 |  23.9  |  47.5  |  64.1  | 

The superscripts <sup>m</sup> and <sup>b</sup> represent the results for mask-style IoU and box-style IoU respectively.

#### Cityscapes
| Model               | Backbone             | Iteration |  Download   |  AP | AP<sub>50 | person| rider | car | trunk | bus | train | motocycle | bicycle |
| :---: | :---: | :---: | :--------: | :---: | :-------: | :-------: | :------: | :------: | :------: | :------: | :------: | :------: | :------: |
| Mask-DAPE       | ResNet50             |  90k   | [config](configs/dape/instance_segmentation/cityscapes/mask_dape_r50_ins_seg_cityscapes_90ki.py) / [checkpoint](https://github.com/xiuqhou/DAPE/releases/download/v1.0.0/mask_dape_r50_rank16_ins_seg_cityscapes_1x.pth) | 38.2 | 62.6 | 35.0 | 29.0 | 55.6 | 39.2 | 59.3 | 43.6 | 21.7 | 22.5 |

## Get started

<details>
<summary>1. Installation</summary>

  1. Clone the repository:

    ```shell
    git clone https://github.com/xiuqhou/DAPE
    cd DAPE
    ```

  2. Install PyTorch and Torchvision following the instruction on https://pytorch.org/get-started/locally/. We provide the version used for our experiments below. Other versions may also work.

    ```shell
    pip install torch==2.7.1 torchvision==0.22.1 torchaudio==2.7.1 --index-url https://download.pytorch.org/whl/cu126
    ```

  3. Install other requirements:

    ```shell
    pip install -r requirements.txt
    ```

</details>

<details>
<summary>2. Prepare datasets</summary>

### COCO

For instance segmentation and object detection, download instance files `train2017`, `val2017`, `instances_train2017.json`, `instances_val2017.json`, and panoptic files `panoptic_train2017`, `panoptic_val2017`, `panoptic_train2017.json`, `panoptic_val2017.json` from [https://cocodataset.org/](https://cocodataset.org/).

```shell
coco/
  ├── train2017/
  ├── val2017/
  ├── panoptic_train2017/
  ├── panoptic_val2017/
  └── annotations/
         ├── instances_train2017.json
         ├── instances_val2017.json
         ├── panoptic_train2017.json
         └── panoptic_val2017.json
```

### LVIS

LVIS share the same samples with `COCO`, you only need to download annotations `lvis_v1_train.json`, `lvis_v1_val.json` from [https://www.lvisdataset.org](https://www.lvisdataset.org) and `lvis_v1_minival_inserted_image_name.json` from [https://huggingface.co/GLIPModel/GLIP/tree/main](https://huggingface.co/GLIPModel/GLIP/tree/main). Put them into the `annotations` subdirectory of the COCO dataset, as follows:

```shell
coco/
  ├── ... 
  └── annotations/
         ├── ... 
         ├── lvis_v1_train.json
         ├── lvis_v1_val.json
         └── lvis_v1_minival_inserted_image_name.json
```

### Cityscapes

Download `leftImg8bit_trainvaltest.zip` and `gtFine_trainvaltest.zip` from [https://www.cityscapes-dataset.com/downloads/](https://www.cityscapes-dataset.com/downloads/).

```python
 cityscapes/
  ├── gtFine/
  │     ├── train/
  │     ├── val/
  │     └── test/
  │ 
  └── leftImg8bit/
        ├── train/
        ├── val/
        └── test/
```

The final datasets should be organized as follows:

```shell

data/
  ├─ coco/
  │  ├── train2017/
  │  ├── val2017/
  │  ├── panoptic_train2017/
  │  ├── panoptic_val2017/
  │  └── annotations/
  │         ├── instances_train2017.json
  │         ├── instances_val2017.json
  │         ├── lvis_v1_train.json
  │         ├── lvis_v1_minival_inserted_image_name.json
  │         ├── lvis_v1_val.json
  │         ├── panoptic_train2017.json
  │         └── panoptic_val2017.json
  │
  └─ cityscapes/
      ├── gtFine/
      └── leftImg8bit/
```

</details>

<details>
<summary>3. Train a model</summary>

Use `CUDA_VISIBLE_DEVICES` to specify GPU/GPUs and run the following script to start training. If not specified, the script will use all available GPUs on the node to train. Replace `<config_file>` with the path to the config file.

```shell
CUDA_VISIBLE_DEVICES=0 accelerate launch train.py <config_file>   # train with 1 GPU
CUDA_VISIBLE_DEVICES=0,1 accelerate launch train.py <config_file>  # train with 2 GPUs

# example:
# CUDA_VISIBLE_DEVICES=0,1,2,3 accelerate launch train.py configs/dape/object_detection/coco/dape_r50_rank16_coco_1x.py
```

</details>

<details>
<summary>4. Evaluate pretrained models</summary>

To evaluate a model with one or more GPUs, specify `CUDA_VISIBLE_DEVICES`, `<config_file>`, `<checkpoint_file>`.

```shell
CUDA_VISIBLE_DEVICES=<gpu_ids> accelerate launch test.py <config_file> --checkpoint <checkpoint_file>

# example:
# CUDA_VISIBLE_DEVICES=0,1,2,3 \
#   accelerate launch test.py \
#   configs/dape/object_detection/coco/dape_r50_rank16_coco_1x.py \
#   --checkpoint https://github.com/xiuqhou/DAPE/releases/download/v1.0.0/dape_r50_rank16_coco_1x.pth
```

</details>

## License

DAPE is released under the Apache 2.0 license. Please see the [LICENSE](LICENSE) file for more information.

## Bibtex

If you find out work helpful, please consider citing:

```bibtex
@article{hou2025dape,
  title={DAPE: Harmonizing Content-Position Encoding for Versatile Dense Visual Prediction},
  author={Hou, Xiuquan and Liu, Meiqin and Zhang, Senlin and Du, Shaoyi},
  journal={Proceedings of the AAAI conference on artificial intelligence},
  year={2025}
}
```


<details>
<summary>If you find out work helpful, please also consider citing our previous papers related to this work:</summary>

```bibtex
@inproceedings{hou2024relation,
  title={Relation DETR: Exploring Explicit Position Relation Prior for Object Detection},
  author={Hou, Xiuquan and Liu, Meiqin and Zhang, Senlin and Wei, Ping and Chen, Badong and Lan, Xuguang},
  booktitle={European conference on computer vision},
  year={2024},
  organization={Springer}
}

@InProceedings{Hou_2024_CVPR,
    author    = {Hou, Xiuquan and Liu, Meiqin and Zhang, Senlin and Wei, Ping and Chen, Badong},
    title     = {Salience DETR: Enhancing Detection Transformer with Hierarchical Salience Filtering Refinement},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
    month     = {June},
    year      = {2024},
    pages     = {17574-17583}
}
```

</details>

## Acknowledge

Many thanks to these excellent open-source projects.

- [MaskDINO](https://github.com/IDEA-Research/MaskDINO)
- [detrex](https://github.com/IDEA-Research/detrex)
- [Relation-DETR](https://github.com/xiuqhou/Relation-DETR)
- [transformers](https://github.com/huggingface/transformers)
- [detectron2](https://github.com/facebookresearch/detectron2)
