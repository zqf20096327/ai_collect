![Banner](./misc/banner.png)

<div style="display: flex; justify-content: space-between;">
  <div style="flex: 1; padding: 10px;">
    <!-- <a href="todohttps://arxiv.org/abs/YYMM.NNNNN" target="_blank" rel="noreferrer" style="text-decoration:none; ">
      <img src="https://img.shields.io/badge/arXiv-YYMM.NNNNN-b31b1b.svg?logo=arxiv" alt="arXiv Paper" style="vertical-align:middle;">
    </a> -->
    <a href="https://colab.research.google.com/github/encord-team/ebind/blob/main/misc/demo.ipynb" target="_blank" rel="noreferrer" style="text-decoration:none; ">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="vertical-align:middle;">
    </a>
    <a href="https://huggingface.co/encord-team/ebind-full" target="_blank" rel="noreferrer" style="text-decoration:none; ">
    <img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Models-blue" alt="Hugging Face Models" style="vertical-align:middle;">
    </a>
    <a href="https://huggingface.co/datasets/encord-team/E-MM1-100M" target="_blank" rel="noreferrer" style="text-decoration:none; ">
    <img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Datasets-blue" alt="Hugging Face Datasets" style="vertical-align:middle;">
    </a>
    <a href="https://e-mm1.github.io" target="_blank" rel="noreferrer" style="text-decoration:none; ">
    <img src="https://img.shields.io/badge/Project%20Page-blue?logo=github" alt="Blog" style="vertical-align:middle;">
    </a>
    <div style="flex:1"></div>
    <a href="https://encord.com/blog/how-we-built-multimodal-dataset-emm1/" target="_blank" rel="noreferrer" style="text-decoration:none; ">
    <img src="https://img.shields.io/badge/%F0%9F%93%96-Blog-blue" alt="Blog" style="vertical-align:middle;">
    </a>
    <a href="https://twitter.com/encord_team" target="_blank" rel="noreferrer" style="text-decoration:none; ">
      <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/encord_team?label=%40encord_team&amp;style=social" style="vertical-align: middle">
    </a>
    <img alt="PRs Welcome" src="https://img.shields.io/badge/PRs-Welcome-blue" style="vertical-align: middle;">
    <img alt="Licence" src="https://img.shields.io/github/license/encord-team/ebind" style="vertical-align: middle;">
  </div>
</div>


# EBind: Multi-Modal Embeddings


EBind is a multi-modal embedding model that supports image, video, audio, text, and 3D point cloud inputs. All modalities are projected into a shared embedding space, enabling cross-modal similarity computation.


## Installation

**Option 1**   
If you want to work within the repository, use `uv` to install the necessary dependencies.
```bash
uv sync
```

**Option 2**   
You can also install it as an external dependency for another project:

```bash
# Option 2.a
python -m pip install git@https://github.com/encord-team/ebind
# Option 2.b; or install a local, editable version
git clone https://github.com/encord-team/ebind
cd /path/to/your/project
python -m pip install -e /path/to/ebind
```

> [!WARNING]
> If you are running a project with pytorch~=2.8.0, you should install torchcodec~=0.7.0 (as opposed to the ~=0.8.0) 
> which is automatically installed with uv. `torchcodec~=0.8.*` matches `pytorch~=2.9.0`.

> [!NOTE]  
> The 3D point cloud backbone has a few custom CUDA kernels that you might want to [compile][#compile-pointnet2-cuda-ops-optional].
> To do that, you will have to do use Option 1 or Option 2.b above to get a local copy of the repository and compile the kernels.


### Loading the Model
```python
import torch
from ebind import EBindModel, EBindProcessor

model = EBindModel.from_pretrained("encord-team/ebind-full")
processor = EBindProcessor.from_pretrained("encord-team/ebind-full")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device).eval()
processor = processor.to(device)
```

### Processing Multi-Modal Inputs
```python
inputs = {
    "image": ["examples/dog.png", "examples/cat.png"],
    "video": ["examples/dog.mp4", "examples/cat.mp4"],
    "audio": ["examples/dog.mp4", "examples/cat.mp4"],
    "text": ["A dog is howling in the street", "A cat is sleeping on the couch"],
    "points": ["examples/dog_point_cloud.npy", "examples/cat_point_cloud.npy"],
}

with torch.inference_mode():
    batch = processor(inputs, return_tensors="pt")  # set text_file_paths=True if passing text file paths instead of strings
    outputs = model.forward(**batch)
```

### Computing Cross-Modal Similarities
```python
keys = list(outputs.keys())
for i, modality in enumerate(keys):
    for j, modality2 in enumerate(keys[i + 1:]):
        result = outputs[modality] @ outputs[modality2].T
        print(f"{modality} x {modality2}:")
        print(result.cpu().detach().numpy())
        print('='*26)
```

Expected Output:

```
image x video similarity: 
[[0.48 0.42]
 [0.41 0.6 ]]
==========================
image x audio similarity: 
[[0.07 0.05]
 [0.02 0.12]]
==========================
image x text similarity: 
[[0.16 0.07]
 [0.08 0.14]]
==========================
image x points similarity: 
[[0.2  0.19]
 [0.18 0.19]]
==========================
video x audio similarity: 
[[0.19 0.08]
 [0.03 0.16]]
==========================
video x text similarity: 
[[0.26 0.05]
 [0.11 0.14]]
==========================
video x points similarity: 
[[0.24 0.15]
 [0.17 0.26]]
==========================
audio x text similarity: 
[[ 0.12 -0.  ]
 [ 0.07  0.09]]
==========================
audio x points similarity: 
[[0.13 0.06]
 [0.1  0.12]]
==========================
text x points similarity: 
[[0.19 0.14]
 [0.05 0.18]]
==========================
```

**Note:** The image/video similarity is significantly higher because they share the same vision encoder.

### Compile PointNet2 CUDA ops (optional)

If you have CUDA available, consider building the [PointNet2](https://github.com/erikwijmans/Pointnet2_PyTorch/tree/master/pointnet2_ops_lib/pointnet2_ops/_ext-src) custom ops used for embedding point clouds to get faster inference:

```bash
cd src/ebind/models/uni3d/pointnet2_ops && \
    uv run python -c "import torch,sys; sys.exit(0 if torch.cuda.is_available() else 1)" && \
    MAX_JOBS=$(nproc) uv run python setup.py build_ext --inplace
```

> We have modified the code slightly in `src/ebind/models/uni3d/pointnet2_ops/pointnet2_utils.py` to
> have a fallback torch implementation in order for the model to be executable on no-GPU
> hardware.


## Contributing

We welcome contributions! If you have suggestions for improvements, new features, or bug fixes, feel free to open an issue or pull request. Please follow the standard [GitHub workflow](https://guides.github.com/introduction/flow/) and adhere to our code style and guidelines. For major changes, we recommend discussing them in an issue before submitting a PR.

### How to contribute

1. Fork the repository.
2. Create your feature branch: `git checkout -b my-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin my-feature`
5. Open a pull request describing your changes.

## Citation

If you use this codebase in your research or work, please cite it as follows (replace with your own citation when available):

```bibtex
@misc{encord-bind,
  author       = {The Encord Team},
  title        = {{EBind}: Multi-modal binding and inference},
  year         = {2025},
  howpublished = {\url{https://github.com/encord-team/ebind}},
}
```


## License

This project is licensed under the Attribution-NonCommercial-ShareAlike 4.0 International. See the `LICENSE` file for details.

