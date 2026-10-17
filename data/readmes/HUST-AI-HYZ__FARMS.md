# Eigenspectrum Analysis of Neural Networks without Aspect Ratio Bias [ICML 2025]

Yuanzhe Hu, Kinshuk Goel, Vlad Killiakov, [Yaoqing Yang](https://sites.google.com/site/yangyaoqingcmu/)

[Full paper](https://arxiv.org/abs/2506.06280)

## Introduction 📖
FARMS (Fixed-Aspect-Ratio Matrix Subsampling) is a method that
normalizes the weight matrices by subsampling submatrices with a fixed aspect ratio. Instead of measuring the heavytailness of the original ESD, we measure the average ESD of these subsampled submatrices. 

## Update

- [x] (Nov. 11th, 2025) We released the code for SciML.

- [x] (June 19th, 2025) We released the code for Image Classification / LLM Pruning.

**🌟 More details coming soon! 🌟**

## Image Classification 🖼️

We modify the code based on the open-source code from [TempBalance](https://openreview.net/forum?id=oyV9FslE3j).
### Dataset and Environment Setup

```bash
conda create -n farms_imgcls python=3.8
conda activate farms_imgcls
cd Image_Classification
pip install -r requirements.txt
```

### Experiments 

```bash
#### Main Experiments
bash bash_scripts/tb_farms_imagecls_main.sh
```

```bash
#### Ablation study 
bash bash_scripts/tb_farms_imagecls_ablation.sh
```

### Usage
```python
from tempbalance_farms import Tempbalance_FARMS
import torch
model = ...
# initialize the scheduler
tb_scheduler = Tempbalance_FARMS(net=net, 
                lr_min_ratio=0.5,
                lr_max_ratio=1.5
                )
# initialize optimizer parameter group
tb_param_group = tb_scheduler.build_optimizer_param_group(untuned_lr=0.1)
optimizer = optim.SGD(
    tb_param_group,
    ...
)
# training loop
for epoch in range(1, ...):
    ...
    train()
    test()
    # get global decayed learning rate (optimizer lr should not be updated here)
    untuned_global_lr = some_lr_decay_function(epoch)
    # temperature balancing
    tb_scheduler.step(optimizer, untuned_global_lr)
    ...
```


## LLM Pruning ✂️


### Dataset and Environment Setup

Step 1: Create a new conda environment:
```
conda create -n farms_prune_llm python=3.9
cd LLM_Pruning
conda activate farms_prune_llm
```
Step 2: Install relevant packages (Same as AlphaPruning)
```
pip install torch==2.1.1+cu118 -f https://download.pytorch.org/whl/torch_stable.html
pip install transformers==4.35.2 datasets==2.16.1 wandb sentencepiece
pip install accelerate==0.25.0
pip install weightwatcher
pip install datasets==2.16.1
```

Step 3: Fix the issue with 'numpy<2'
```
pip install "numpy<2"
```

### Experiments 

```bash
## One Example 
bash scripts/llama_prune_wiki_ww_multiple_seeds.sh  
```
You can modify the settings (like random seed) in the bash file


## SciML 

See ReadME.md at DPOT directory.



## Acknowledgement

We thank the open-source code from [AlphaPruning](https://github.com/haiquanlu/AlphaPruning) / [Model Balancing](https://github.com/ZihangHLiu/ModelBalancing) / [TempBlanace](https://github.com/YefanZhou/TempBalance)  / [DPOT](https://github.com/HaoZhongkai/DPOT)


## Citation
We would appreciate it if you could cite the following paper if you found the repository useful for your work:

```bash
@inproceedings{hu2025eigenspectrum,
  title = 	 {Eigenspectrum Analysis of Neural Networks without Aspect Ratio Bias},
  author =       {Hu, Yuanzhe and Goel, Kinshuk and Killiakov, Vlad and Yang, Yaoqing},
  booktitle = 	 {Proceedings of the 42nd International Conference on Machine Learning},
  pages = 	 {24290--24313},
  year = 	 {2025},
  editor = 	 {Singh, Aarti and Fazel, Maryam and Hsu, Daniel and Lacoste-Julien, Simon and Berkenkamp, Felix and Maharaj, Tegan and Wagstaff, Kiri and Zhu, Jerry},
  volume = 	 {267},
  series = 	 {Proceedings of Machine Learning Research},
  month = 	 {13--19 Jul},
  publisher =    {PMLR},
  pdf = 	 {https://raw.githubusercontent.com/mlresearch/v267/main/assets/hu25e/hu25e.pdf},
  url = 	 {https://proceedings.mlr.press/v267/hu25e.html},
}
```
