<h1 align="center">Need for Speed: Zero-Shot Depth Completion with Single-Step Diffusion</h1>
<p align="center">
  <a href="https://dtu-pas.github.io/marigold-ssd"><img alt="Homepage" src="https://img.shields.io/badge/Visit-Homepage-blue"></a>
  <a href="https://arxiv.org/abs/2603.10584v2"><img alt="Paper (arXiv)" src="https://img.shields.io/badge/Read-Paper_(arXiv)-yellow"></a>
  <a href="https://dtu-pas.github.io/marigold-ssd/supplementary.pdf"><img alt="Supplementary (IEEE)" src="https://img.shields.io/badge/Read-Supplementary_(PDF)-green"></a>
</p>

This is the official implementation of "Need for Speed: Zero-Shot Depth Completion with Single-Step Diffusion"
paper authored by:
[Jakub Gregorek](https://scholar.google.com/citations?user=Afmk1FYAAAAJ),
[Paraskevas Pegios](https://scholar.google.com/citations?user=LVACmX4AAAAJ),
[Nando Metzger](https://nandometzger.github.io/),
[Konrad Schindler](https://scholar.google.com/citations?user=FZuNgqIAAAAJ), 
[Theodora Kontogianni](https://theodorakontogianni.github.io/) and 
[Lazaros Nalpantidis](https://lanalpa.github.io/).

# Dependencies

The project uses Python 3.11, you may create a Conda environment as follows:

`conda env create -f environment.yml`

activate it:

`conda activate ssd`

and install pip dependencies:

`pip install -r requirements.txt`

You will need to define two environment variables:

- `DATASETS_DIR` - pointing to the directory containing training and evaluation datasets
- `MODELS_DIR` - pointing to the directory where the models are to be stored

# Datasets

For training you will need to download the following datasets:

- [Hypersim](https://github.com/apple/ml-hypersim)
    - download and preprocess the dataset as described in:
      
      [VisualComputingInstitute/diffusion-e2e-ft: Fine-Tuning Image-Conditional Diffusion Models](https://github.com/VisualComputingInstitute/diffusion-e2e-ft)
    - place the preprocessed dataset to:

      `${DATASETS_DIR}/diffusion-e2e-ft-datasets/hypersim/processed`

- [Virtual KITTI](https://europe.naverlabs.com/proxy-virtual-worlds-vkitti-2/)
    - download the following files from the [official site](https://europe.naverlabs.com/proxy-virtual-worlds-vkitti-2/): 
        - vkitti_2.0.3_rgb.tar
        - vkitti_2.0.3_depth.tar
    - extract the archives to:

      `${DATASETS_DIR}/diffusion-e2e-ft-datasets/virtual_kitti_2`

For evaluation you will need to download the following datasets:

- [ScanNet](http://www.scan-net.org)
  - download test subset (scannet-dc2.zip) of the dataset from the following link:

    `https://drive.google.com/drive/folders/1xvQ1_pXGCI0iIp7xyajgFhqFmLb9_cxX?usp=share_link`
  - extract the files to:

    `${DATASETS_DIR}/scannet-dc2/`

- [IBims-1](https://mediatum.ub.tum.de/1455541)
  - download the dataset from the [official site](https://mediatum.ub.tum.de/1455541)
  - place the files to:
    
    `${DATASETS_DIR}/ibims-1/`

- [NYUv2](https://cs.nyu.edu/~fergus/datasets/nyu_depth_v2.html)
  - download the labeled dataset from the [official site](https://cs.nyu.edu/~fergus/datasets/nyu_depth_v2.html)
  - place the `nyu_depth_v2_labeled.mat` file to:
    
    `${DATASETS_DIR}/nyu-v2/`

- [VOID](https://github.com/alexklwong/void-dataset)
  - download the labeled dataset from as described in the [official repository](https://github.com/alexklwong/void-dataset)
  - place the three density directories to:

    `${DATASETS_DIR}/void`

- [KITTI DC](https://www.cvlibs.net/datasets/kitti/)
  - download the validation selection from the [official page](https://www.cvlibs.net/datasets/kitti/eval_depth.php?benchmark=depth_completion)
  - place the files to:
    
    `${DATASETS_DIR}/kitti-depth/data_depth_selection/val_selection_cropped`

- [DDAD](https://github.com/TRI-ML/DDAD)
  - download the dataset preprocessed by:
    
    [bartn8/vppdc: Revisiting Depth Completion from a Stereo Matching Perspective for Cross-domain Generalization (3DV 2024)](https://github.com/bartn8/vppdc)

  - place the files to:

    `${DATASETS_DIR}/ddad-ogni-dc/val`

Furthermore, files with sparsely sampled depth points (sampled-points.zip) need to be downloaded from:

`https://drive.google.com/drive/folders/1xvQ1_pXGCI0iIp7xyajgFhqFmLb9_cxX?usp=share_link`

and extracted to the datasets directory.

The directory tree with training and evaluation datasets should look as follows:

```
${DATASETS_DIR}
├── diffusion-e2e-ft-datasets
│   ├── hypersim
│   │   └── processed
│   │       ├── normals
│   │       ├── test
│   │       ├── train
│   │       └── val
│   └── virtual_kitti_2
│       ├── vkitti_2.0.3_depth
│       └── vkitti_2.0.3_rgb
├── scannet-dc2
│   └── test
│       ├── groundtruth
│       ├── images
│       └── intrinsics
├── scannet-dc2-depth1000
├── scannet-dc2-depth1500
├── scannet-dc2-depth15360
├── scannet-dc2-depth500
├── ibims-1
│   ├── evaluation_scripts
│   ├── ibims1_aux_augmented
│   ├── ibims1_aux_mvs
│   ├── ibims1_aux_patterns
│   ├── ibims1_core_mat
│   ├── ibims1_core_raw
│   └── imagelist.txt
├── ibims-1-dc2-depth1000
├── ibims-1-dc2-depth1500
├── ibims-1-dc2-depth15360
├── ibims-1-dc2-depth500
├── nyu-v2
│   └── nyu_depth_v2_labeled.mat
├── nyu-v2-depth1000
├── nyu-v2-depth1500
├── nyu-v2-depth15360
├── nyu-v2-depth500
├── void
│   ├── void_150
│   ├── void_1500
│   └── void_500
├── kitti-depth
│   └── data_depth_selection
│       └── val_selection_cropped
│           ├── groundtruth_depth
│           ├── image
│           ├── intrinsics
│           └── velodyne_raw
├── ddad-ogni-dc
│   └── val
│       ├── gt
│       ├── hints
│       ├── intrinsics
│       └── rgb
├── ddad-ogni-dc-depth1000
├── ddad-ogni-dc-depth1500
└── ddad-ogni-dc-depth500
```

# Training & Evaluation

The models can be trained by the following scripts:

`./scripts/ssd_train`

and evaluated under multiple sparsity levels by running:

`./scripts/ssd_eval`

The pretrained models (ssd.zip, ssd-sparser.zip) can be downloaded from:

`https://drive.google.com/drive/folders/1xvQ1_pXGCI0iIp7xyajgFhqFmLb9_cxX?usp=share_link`

# Acknowledgments

This project takes an inspiration from the following projects:
- [prs-eth/Marigold: Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation](https://github.com/prs-eth/marigold)
- [VisualComputingInstitute/diffusion-e2e-ft: Fine-Tuning Image-Conditional Diffusion Models](https://github.com/VisualComputingInstitute/diffusion-e2e-ft)
- [bartn8/vppdc: Revisiting Depth Completion from a Stereo Matching Perspective for Cross-domain Generalization (3DV 2024)](https://github.com/bartn8/vppdc)
- [mediaTUM IBims-v1](https://mediatum.ub.tum.de/1455541)