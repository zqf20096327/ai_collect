<p align="center">
    <h1 align="center">SeqTex: Generate Mesh Textures in Video Sequence</h1>
    <h3 align="center"><span style="color: #6e6e6eff; font-size: smaller;">(SIGGRAPH Asia 2025, Conference Track)</span></h3>

  <p align="center">
    <a href="https://scholar.google.com/citations?user=IcLy55oAAAAJ">Ze Yuan<sup>*</sup></a>
    ·
    <a href="https://xinyu-andy.github.io/">Xin Yu<sup>*†</sup></a>
    ·
    <a href="https://sunyangtian.github.io/">Yangtian Sun</a>
    ·
    <a href="https://scholar.google.com/citations?user=b7ZJV9oAAAAJ&hl=en">Yuan-Chen Guo</a>
    ·
    <a href="https://yanpei.me">Yan-Pei Cao</a>
    ·
    <a href="https://scholar.google.com/citations?user=Dqjnn0gAAAAJ&hl=zh-CN">Ding Liang</a>
    ·
    <a href="https://xjqi.github.io/">Xiaojuan Qi<sup>✉</sup></a>
    <br>
    <b>The University of Hong Kong &nbsp; | &nbsp;  VAST </b>
    <br>
    <sup>*</sup>Equal contribution &nbsp;&nbsp; <sup>†</sup>Project lead &nbsp;&nbsp; <sup>✉</sup>Corresponding author
  </p>
  <p align="center">
    <a href="https://arxiv.org/abs/2507.04285"><img src="https://img.shields.io/badge/arXiv-Paper-red?logo=arxiv&logoColor=white" alt="arXiv Paper"></a>
    <a href="https://dl.acm.org/doi/10.1145/3757377.3763863"><img src="https://img.shields.io/badge/ACM-Paper-lightgrey?logo=acm&logoColor=white" alt="Paper"></a>
    <a href="https://yuanze1024.github.io/SeqTex/"><img src="https://img.shields.io/badge/Project_Page-Website-green?logo=googlechrome&logoColor=white" alt="Project Page"></a>
    <a href="https://huggingface.co/VAST-AI/SeqTex-Transformer"><img src="https://img.shields.io/badge/Hugging%20Face-Model_Checkpoint-blue?logo=huggingface&logoColor=white" alt="Model Checkpoint"></a>
    <a href="https://huggingface.co/spaces/VAST-AI/SeqTex"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Live_Demo-blue?logo=huggingface&logoColor=white" alt="Hugging Face Demo"></a>
  </p>
</p>

---

<table align="center">
  <tr>
    <td>
      <img src="assets/teaser.png" alt="SeqTex Teaser">
    </td>
  </tr>
</table>

## News  
- **2025-12-12**: Code release v1.0.0! 🎉

## Requirements  
This repository is tested with 1 × NVIDIA A100 80GB GPU. For training, at least 8 GPUs with 80GB memory each are recommended. You can refer to the [project page](https://yuanze1024.github.io/SeqTex/) for a quick demo.
We used **4 nodes to train for 1 week** to obtain the results presented in the paper. 

## Environment  
```bash
conda create -n seqtex python=3.10 -y
conda activate seqtex
conda install -c nvidia/label/cuda-11.8.0 cuda-toolkit -y
conda install -c conda-forge gxx=11 gcc=11 -y
pip install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu118
pip install -r requirements.txt
```


## Quick Start
### Overfit
```bash
python launch.py --config configs/train.yaml --train \
    --gpu 0,1,2,3,4,5,6,7 trainer.num_nodes=1 name="train" tag="overfit" \
    data.scene_list=["data/indices/train_3d.jsonl","data/indices/train_image.jsonl"] \
    data.train_indices=[[0,1],[0,1]] data.task_list=["img2tex","geo2mv"] \
    data.eval_scene_list=["data/indices/train_3d.jsonl","data/indices/train_image.jsonl"] \
    data.val_indices=[[0,1],[0,1]] data.eval_task_list=["img2tex","geo2mv"] \
    data.extra_prompt_db=["data/indices/prompt_extension.json"] \
    data.repeat=1000 trainer.val_check_interval=1.0 

    # # to resume training, add below
    # system.weights=<main_ckpt_path>.ckpt system.ema_kwargs.cloud_or_local_key=<ema_path>.pth
```
SeqTex training uses FSDP by default; otherwise, it won't fit in 80GB GPU memory. 

### Testing  
```bash
python launch.py --config configs/test.yaml --test \
    --gpu 0 trainer.num_nodes=1 name="test" tag="test_dtc" \
    data.eval_scene_list=["data/indices/test_one.jsonl"] \
    system.seqtex_transformer_name_or_path=VAST-AI/SeqTex-Transformer
```
Try the above command to perform a quick test for image-conditioned texture generation.

Alternatively, if you want more controllability, you can use SDXL to convert your text prompt to an image condition and then generate the texture map.

```bash
python launch.py --config configs/test.yaml --test \
    --gpu 0 trainer.num_nodes=1 name="test" tag="test_dtc_sdxl" \
    data.eval_scene_list=["data/indices/test_one.jsonl"] \
    system.seqtex_transformer_name_or_path=VAST-AI/SeqTex-Transformer \
    system.use_generated_img_cond=true
```
If everything goes well, you should get a result like the one shown [here](assets/it0-test-0_0-mv-taskimg2tex.png). You can use this as a **sanity check**.

### Result Explanation
Each result contains 3-4 files:
```bash
outputs_wan/test/test_dtc_sdxl@20251013-121842/save
├── it0-test-0_0-img_cond.png           # (text2tex ONLY) image condition from SDXL/FLUX.
├── it0-test-0_0-mv-taskimg2tex.png     # please refer to [assets/explain.png](assets/explain.png)
├── it0-test-0_0-prompt.json            # the model id, and text prompt used
└── it0-test-0_0-uv-taskimg2tex.png     # 3 rows: position and normal map, and the final texture map generated
```

## Data Organization  
Two types of datasets are supported: 3D dataset and image dataset. You can prepare the data in the following format. The processing scripts may be partially found in our [HF space demo](https://huggingface.co/spaces/VAST-AI/SeqTex/blob/main/utils/mesh_utils.py) (It has some known issues, e.g., fails to do UV unwrapping for some cases).

**[Note]**: Every 3D model with multiple parts should be merged into a single mesh with a single UV map and a single texture map. The texture map should preferably be an albedo map without lighting/shading. For image datasets, PBR shaded images are also supported.

### 3D Dataset
For 3D datasets, each directory contains a 3D model and a corresponding texture map. This is the **primary** data format we need. It is the data used by the ***img2tex*** task.
```bash
data/examples
└── 99
    └── 999c2f55-0cf6-4d46-913a-7671085d03f6
        ├── model.glb
        └── model.jpeg # preferably an albedo texture map
```
### Image Dataset
For image datasets, each directory contains a set of images. This is an **alternative** data format to improve the generalization ability of the model. It is the data used by the ***geo2mv*** task.
```bash
data/examples_train_image
└── f6
    └── f63290551cac423883742cfdb8acc9ff
        ├── meta.json # transform_matrixs for each image
        ├── color_0000.webp # PBR shaded images are also supported
        ...
        ├── depth_0000.exr
        ...
        └── normal_0005.webp
```

## Citation  
If SeqTex is used in your work, please cite:
```bibtex
@inproceedings{10.1145/3757377.3763863,
  author = {Yuan, Ze and Yu, Xin and Sun, Yangtian and Guo, Yuan-Chen and Cao, Yan-Pei and Liang, Ding and Qi, Xiaojuan},
  title = {SeqTex: Generate Mesh Textures in Video Sequence},
  year = {2025},
  isbn = {9798400721373},
  publisher = {Association for Computing Machinery},
  address = {New York, NY, USA},
  url = {https://dl.acm.org/doi/10.1145/3757377.3763863},
  doi = {10.1145/3757377.3763863},
  booktitle = {Proceedings of the SIGGRAPH Asia 2025 Conference Papers},
  articleno = {25},
  numpages = {12},
  keywords = {Video Diffusion Models, Diffusion Techniques, Texture Generation},
  series = {SA Conference Papers '25}
}
```

## Acknowledgement
We sincerely thank the following open-source projects:
- [MV-Adapter](https://github.com/huanngzh/MV-Adapter) for the coding framework.
- [Wan2.1](https://github.com/Wan-Video/Wan2.1) for the 3D prior from video sequences
- [SDXL](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0) and [FLUX](https://huggingface.co/black-forest-labs/FLUX.1-dev) for high fidelity text-to-image generation
- [diffusers](https://github.com/huggingface/diffusers) for the diffusion model implementation
- [lightning](https://github.com/Lightning-AI/pytorch-lightning) for saving my time

Additionally, we thank the following people for their help:
- Special thanks to [Toshihiro Hayashi](mailto:toshihiro@huggingface.co) for his valuable support and assistance in fixing bugs for our HF demo.
- We thank [EasyMode-AI](https://github.com/easymode-ai) for their efforts in **integrating SeqTex into ComfyUI**. See [here](https://github.com/easymode-ai/comfyui-seqtex).