<div align="center">

# zij &nbsp;زِيج

Learning state of the art deep learning optimization algorithms.

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](pytorch/pyproject.toml)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.12-ee4c2c.svg)](https://pytorch.org/)

</div>

A *zij* (Arabic: زِيج, pronounced *"zeej"*) is an astronomical handbook from the
Islamic golden age: a set of tables and computational methods that astronomers
consulted instead of re-deriving the field from scratch. The best known is the
*Zīj al-Sindhind* of Muḥammad ibn Mūsā al-Khwārizmī (محمد بن موسى الخوارزمي,
c. 820 CE). His Latinized name, *Algoritmi*, became the word *algorithm*, and his
book *al-Jabr* gave us *algebra*.

This project takes the name in that spirit. It gathers the equation, the paper,
and runnable code for the optimization methods used in machine learning.

## Contents

- [Installation](#installation)
- [Quick start](#quick-start)
- [Library](#library)
- [Canon](#canon)
  - [First-Order Optimizers](#first-order-optimizers) (226)
  - [Memory-Efficient Optimizers](#memory-efficient-optimizers) (90)
  - [Fractional-Order Optimizers](#fractional-order-optimizers) (93)
  - [Distributed and Communication-Efficient Optimizers](#distributed-and-communication-efficient-optimizers) (75)
  - [Second-Order and Orthogonalized Optimizers](#second-order-and-orthogonalized-optimizers) (67)
  - [Zeroth-Order Optimizers](#zeroth-order-optimizers) (38)
  - [Privacy-Preserving Optimizers](#privacy-preserving-optimizers) (40)
  - [Sharpness-Aware Optimizers](#sharpness-aware-optimizers) (28)
  - [Quantum and Quantum-Inspired Optimizers](#quantum-and-quantum-inspired-optimizers) (31)
  - [Learning-Rate-Free Optimizers](#learning-rate-free-optimizers) (24)
  - [Learning Rate Schedulers](#learning-rate-schedulers) (28)
- [How zij compares](#how-zij-compares)
- [Engineering standards](#engineering-standards)
- [Acknowledgments](#acknowledgments)
- [Citation](#citation)
- [License](#license)

## Installation

```bash
pip install zij
```

From source, with the pinned environment:

```bash
git clone https://github.com/junaidaliop/zij.git
cd zij
conda env create -f environment.yml
conda activate zij-optim
```

## Quick start

```python
import zij

# torch.optim, vendored at tag v2.12.0
opt = zij.AdamW(model.parameters(), lr=3e-4)

# research optimizers, same interface
opt = zij.Muon([p for p in model.parameters() if p.ndim == 2], lr=2e-2)
opt = zij.Prodigy(model.parameters())                       # no learning rate to set
opt = zij.SAM(model.parameters(), base_optimizer=zij.SGD, lr=0.1, rho=0.05)

# memory-efficient low-rank training (per-group rank)
opt = zij.GaLoreAdamW(
    [{"params": params, "rank": 128, "update_proj_gap": 200, "scale": 0.25, "proj_type": "std"}],
    lr=1e-2,
)

# look up by name
zij.list_optimizers("adam*")
opt_cls = zij.load_optimizer("soap")
```

`zij.optim` mirrors `torch.optim`, so `zij.optim.AdamW` is the same class as
`zij.AdamW`, and `zij.optim.lr_scheduler` is available. Use whichever import
reads better in your code.

> [!NOTE]
> A few families use a documented non-standard call protocol. Schedule-Free needs
> `opt.train()` and `opt.eval()`; the SAM family takes a closure or an explicit
> `first_step` / `second_step` pair; Adam-mini and LOMO are built from a model
> rather than a parameter list. Each class docstring states which.

## Library

The PyTorch package ships 106 ready-to-use optimizers. `zij.core` mirrors
`torch.optim` at tag v2.12.0 (Adam, AdamW, SGD, Muon, LBFGS, Adafactor, and the
rest, plus `lr_scheduler` and `swa_utils`). `zij.contrib` adds research methods
grouped by family: first-order, second-order, memory-efficient,
learning-rate-free, and sharpness-aware. In every Canon table below, the `zij`
column names the class where an implementation exists; a dash (—) means the
method is listed but not yet implemented (paper-only, or its source is under a
license that cannot be vendored).

zij is a PyTorch library today. The Canon is framework-agnostic: it covers each
method regardless of the framework of its original code. JAX and TensorFlow ports
are planned and will follow the same standards.

## Canon

The Canon below covers 740 methods across 11 categories. Each row
records the canonical name, venue, paper, the best available implementation, and
the `zij` class where one exists.

### First-Order Optimizers

First-order optimizers update parameters using only gradients and accumulated gradient statistics such as momentum and second-moment estimates. This page covers the stochastic gradient descent lineage, the Adam family, and more recent sign-based and variance-reduced methods. The `zij` column gives the class name for optimizers already implemented in the package.

| Optimizer | Venue | Paper | Code | `zij` |
|---|---|---|---|---|
| [ASGD](canon/math/asgd.md) | SIAM Journal on Control and Optimization 1992 | [Acceleration of Stochastic Approximation by Averaging](https://doi.org/10.1137/0330046) | [community](https://github.com/pytorch/pytorch/blob/main/torch/optim/asgd.py) | `ASGD` |
| [Rprop](canon/math/rprop.md) | ICNN 1993 | [A direct adaptive method for faster backpropagation learning: the RPROP algorithm](https://doi.org/10.1109/ICNN.1993.298623) | [community](https://github.com/pytorch/pytorch/blob/main/torch/optim/rprop.py) | `Rprop` |
| [Adagrad](canon/math/adagrad.md) | JMLR 2011 | [Adaptive Subgradient Methods for Online Learning and Stochastic Optimization](https://jmlr.org/papers/v12/duchi11a.html) | [community](https://github.com/pytorch/pytorch/blob/main/torch/optim/adagrad.py) | `Adagrad` |
| [Adadelta](canon/math/adadelta.md) | arXiv 2012 | [ADADELTA: An Adaptive Learning Rate Method](https://arxiv.org/abs/1212.5701) | [community](https://github.com/pytorch/pytorch/blob/main/torch/optim/adadelta.py) | `Adadelta` |
| [RMSprop](canon/math/rmsprop.md) | Lecture notes 2012 | [Lecture 6.5-rmsprop: Divide the gradient by a running average of its recent magnitude](https://www.cs.toronto.edu/~tijmen/csc321/slides/lecture_slides_lec6.pdf) | [community](https://github.com/pytorch/pytorch/blob/main/torch/optim/rmsprop.py) | `RMSprop` |
| [FTRL](canon/math/ftrl.md) | KDD 2013 | [Ad Click Prediction: a View from the Trenches](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/41159.pdf) | — | — |
| [SGD](canon/math/sgd.md) | ICML 2013 | [On the importance of initialization and momentum in deep learning](https://proceedings.mlr.press/v28/sutskever13.html) | [community](https://github.com/pytorch/pytorch/blob/main/torch/optim/sgd.py) | `SGD` |
| [Adam](canon/math/adam.md) | ICLR 2015 | [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980) | [community](https://github.com/pytorch/pytorch/blob/main/torch/optim/adam.py) | `Adam` |
| [AdaMax](canon/math/adamax.md) | ICLR 2015 | [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980) | [community](https://github.com/pytorch/pytorch/blob/main/torch/optim/adamax.py) | `Adamax` |
| [Nadam](canon/math/nadam.md) | ICLR Workshop 2016 | [Incorporating Nesterov Momentum into Adam](https://openreview.net/forum?id=OM0jvwB8jIp57ZJjtNEZ) | [community](https://github.com/pytorch/pytorch/blob/main/torch/optim/nadam.py) | `NAdam` |
| [LARS](canon/math/lars.md) | arXiv 2017 | [Large Batch Training of Convolutional Networks](https://arxiv.org/abs/1708.03888) | [community](https://github.com/huggingface/pytorch-image-models/blob/main/timm/optim/lars.py) | `LARS` |
| [SWATS](canon/math/swats.md) | arXiv 2017 | [Improving Generalization Performance by Switching from Adam to SGD](https://arxiv.org/abs/1712.07628) | [community](https://github.com/jettify/pytorch-optimizer/blob/master/torch_optimizer/swats.py) | `SWATS` |
| [A2Grad](canon/math/a2graduni.md) | arXiv 2018 | [Optimal Adaptive and Accelerated Stochastic Gradient Descent](https://arxiv.org/abs/1810.00553) | [community](https://github.com/severilov/A2Grad_optimizer) | `A2GradUni`, `A2GradInc`, `A2GradExp` |
| [AccSGD](canon/math/accsgd.md) | ICLR 2018 | [On the insufficiency of existing momentum schemes for Stochastic Optimization](https://arxiv.org/abs/1803.05591) | [official](https://github.com/rahulkidambi/AccSGD) | `AccSGD` |
| [AMSGrad](canon/math/amsgrad.md) | ICLR 2018 | [On the Convergence of Adam and Beyond](https://arxiv.org/abs/1904.09237) | [community](https://github.com/pytorch/pytorch/blob/main/torch/optim/adam.py) | — |
| [GADAM](canon/math/gadam.md) | arXiv 2018 | [GADAM: Genetic-Evolutionary ADAM for Deep Neural Network Optimization](https://arxiv.org/abs/1805.07500) | — | — |
| [M-SVAG](canon/math/msvag.md) | ICML 2018 | [Dissecting Adam: The Sign, Magnitude and Variance of Stochastic Gradients](https://arxiv.org/abs/1705.07774) | [official](https://github.com/lballes/msvag) | — |
| [PID](canon/math/pid.md) | CVPR 2018 | [A PID Controller Approach for Stochastic Optimization of Deep Networks](https://openaccess.thecvf.com/content_cvpr_2018/html/An_A_PID_Controller_CVPR_2018_paper.html) | [official](https://github.com/tensorboy/PIDOptimizer) | `PID` |
| [VR-SGD](canon/math/vrsgd.md) | IEEE TKDE 2018 | [VR-SGD: A Simple Stochastic Variance Reduction Method for Machine Learning](https://arxiv.org/abs/1802.09932) | — | — |
| [Yogi](canon/math/yogi.md) | NeurIPS 2018 | [Adaptive Methods for Nonconvex Optimization](https://papers.nips.cc/paper_files/paper/2018/hash/90365351ccc7437a1309dc64e4db32a3-Abstract.html) | [community](https://github.com/jettify/pytorch-optimizer/blob/master/torch_optimizer/yogi.py) | `Yogi` |
| [AdaBound](canon/math/adabound.md) | ICLR 2019 | [Adaptive Gradient Methods with Dynamic Bound of Learning Rate](https://arxiv.org/abs/1902.09843) | [official](https://github.com/Luolc/AdaBound) | `AdaBound`, `AdaBoundW` |
| [AdaMod](canon/math/adamod.md) | arXiv 2019 | [An Adaptive and Momental Bound Method for Stochastic Learning](https://arxiv.org/abs/1910.12249) | [official](https://github.com/lancopku/AdaMod) | `AdaMod` |
| [AdamW](canon/math/adamw.md) | ICLR 2019 | [Decoupled Weight Decay Regularization](https://arxiv.org/abs/1711.05101) | [official](https://github.com/loshchil/AdamW-and-SGDW) | `AdamW` |
| [AdaShift](canon/math/adashift.md) | ICLR 2019 | [AdaShift: Decorrelation and Convergence of Adaptive Learning Rate Methods](https://arxiv.org/abs/1810.00143) | [community](https://github.com/mknbv/adashift) | `AdaShift` |
| [AggMo](canon/math/aggmo.md) | ICLR 2019 | [Aggregated Momentum: Stability Through Passive Damping](https://arxiv.org/abs/1804.00325) | [official](https://github.com/AtheMathmo/AggMo) | `AggMo` |
| [AvaGrad](canon/math/avagrad.md) | arXiv 2019 | [Domain-independent Dominance of Adaptive Methods](https://arxiv.org/abs/1912.01823) | [official](https://github.com/lolemacs/avagrad) | `AvaGrad` |
| [HAdam](canon/math/hadam.md) | NeurIPS Workshop 2019 | [On Higher-order Moments in Adam](https://arxiv.org/abs/1910.06878) | — | — |
| [HyperAdam](canon/math/hyperadam.md) | AAAI 2019 | [HyperAdam: A Learnable Task-Adaptive Adam for Network Training](https://arxiv.org/abs/1811.08996) | — | — |
| [Lookahead](canon/math/lookahead.md) | NeurIPS 2019 | [Lookahead Optimizer: k steps forward, 1 step back](https://arxiv.org/abs/1907.08610) | [community](https://github.com/alphadl/lookahead.pytorch) | `Lookahead` |
| [NosAdam](canon/math/nosadam.md) | IJCAI 2019 | [Nostalgic Adam: Weighting more of the past gradients when designing the adaptive learning rate](https://arxiv.org/abs/1805.07557) | — | — |
| [NovoGrad](canon/math/novograd.md) | arXiv 2019 | [Stochastic Gradient Methods with Layer-wise Adaptive Moments for Training of Deep Networks](https://arxiv.org/abs/1905.11286) | [community](https://github.com/huggingface/pytorch-image-models/blob/main/timm/optim/nvnovograd.py) | `NovoGrad` |
| [QHAdam / QHM](canon/math/qhadam.md) | ICLR 2019 | [Quasi-hyperbolic momentum and Adam for deep learning](https://arxiv.org/abs/1810.06801) | [official](https://github.com/facebookresearch/qhoptim) | `QHAdam`, `QHM` |
| [Ranger](canon/math/ranger.md) | — | RAdam and Lookahead combination | [official](https://github.com/lessw2020/Ranger-Deep-Learning-Optimizer) | `Ranger` |
| [Sadam](canon/math/sadam.md) | arXiv 2019 | [Calibrating the Adaptive Learning Rate to Improve Convergence of ADAM](https://arxiv.org/abs/1908.00700) | — | — |
| [AdaBelief](canon/math/adabelief.md) | NeurIPS 2020 | [AdaBelief Optimizer: Adapting Stepsizes by the Belief in Observed Gradients](https://arxiv.org/abs/2010.07468) | [official](https://github.com/juntang-zhuang/Adabelief-Optimizer) | `AdaBelief` |
| [Adam+](canon/math/adam-v.md) | arXiv 2020 | [Adam+: A Stochastic Method with Adaptive Variance Reduction](https://arxiv.org/abs/2011.11985) | — | — |
| [AdamBS](canon/math/adambs.md) | NeurIPS 2020 | [Adam with Bandit Sampling for Deep Learning](https://arxiv.org/abs/2010.12986) | — | — |
| [AdaSGD](canon/math/adasgd.md) | arXiv 2020 | [AdaSGD: Bridging the gap between SGD and Adam](https://arxiv.org/abs/2006.16541) | — | — |
| [Cayley SGD](canon/math/cayleysgd.md) | ICLR 2020 | [Efficient Riemannian Optimization on the Stiefel Manifold via the Cayley Transform](https://arxiv.org/abs/2002.01113) | [official](https://github.com/JunLi-Galios/Optimization-on-Stiefel-Manifold-via-Cayley-Transform) | — |
| [clipped-SGD](canon/math/clippedsgd.md) | NeurIPS 2020 | [Stochastic Optimization with Heavy-Tailed Noise via Accelerated Gradient Clipping](https://arxiv.org/abs/2005.10785) | [official](https://github.com/eduardgorbunov/accelerated_clipping) | — |
| [DEAM](canon/math/deam.md) | ASONAM 2020 | [DEAM: Adaptive Momentum with Discriminative Weight for Stochastic Optimization](https://arxiv.org/abs/1907.11307) | — | — |
| [diffGrad](canon/math/diffgrad.md) | IEEE TNNLS 2020 | [diffGrad: An Optimization Method for Convolutional Neural Networks](https://arxiv.org/abs/1909.11015) | [official](https://github.com/shivram1987/diffGrad) | `DiffGrad` |
| [EAdam](canon/math/eadam.md) | arXiv 2020 | [EAdam Optimizer: How ε Impact Adam](https://arxiv.org/abs/2011.02150) | [official](https://github.com/yuanwei2019/EAdam-optimizer) | — |
| [Fromage](canon/math/fromage.md) | NeurIPS 2020 | [On the distance between two neural networks and the stability of learning](https://arxiv.org/abs/2002.03432) | [official](https://github.com/jxbz/fromage) | — |
| [Gradient Centralization (GC)](canon/math/gradientcentralizationgc.md) | ECCV 2020 | [Gradient Centralization: A New Optimization Technique for Deep Neural Networks](https://arxiv.org/abs/2004.01461) | [official](https://github.com/Yonghongwei/Gradient-Centralization) | — |
| [LAMB](canon/math/lamb.md) | ICLR 2020 | [Large Batch Optimization for Deep Learning: Training BERT in 76 minutes](https://arxiv.org/abs/1904.00962) | [community](https://github.com/huggingface/pytorch-image-models/blob/main/timm/optim/lamb.py) | `Lamb` |
| [LaProp](canon/math/laprop.md) | arXiv 2020 | [LaProp: Separating Momentum and Adaptivity in Adam](https://arxiv.org/abs/2002.04839) | [official](https://github.com/Z-T-WANG/LaProp-Optimizer) | `LaProp` |
| [NIGT](canon/math/nigt.md) | ICML 2020 | [Momentum Improves Normalized SGD](https://arxiv.org/abs/2002.03305) | [official](https://github.com/google-research/google-research/tree/master/nigt_optimizer) | — |
| [Padam](canon/math/padam.md) | IJCAI 2020 | [Closing the Generalization Gap of Adaptive Gradient Methods in Training Deep Neural Networks](https://arxiv.org/abs/1806.06763) | [official](https://github.com/uclaml/Padam) | `PAdam` |
| [signSGD](canon/math/signsgd.md) | ICML 2018 | [signSGD: Compressed Optimisation for Non-Convex Problems](https://arxiv.org/abs/1802.04434) | [community](https://github.com/kozistr/pytorch_optimizer) | `SignSGD` |
| [pbSGD](canon/math/pbsgd.md) | IJCAI 2020 | [pbSGD: Powered Stochastic Gradient Descent Methods for Accelerated Non-Convex Optimization](https://www.ijcai.org/proceedings/2020/451) | [official](https://github.com/HAIRLAB/pbSGD) | — |
| [PCGrad](canon/math/pcgrad.md) | NeurIPS 2020 | [Gradient Surgery for Multi-Task Learning](https://arxiv.org/abs/2001.06782) | [official](https://github.com/tianheyu927/PCGrad) | — |
| [RAdam](canon/math/radam.md) | ICLR 2020 | [On the Variance of the Adaptive Learning Rate and Beyond](https://arxiv.org/abs/1908.03265) | [official](https://github.com/LiyuanLucasLiu/RAdam) | `RAdam` |
| [SGD-G2](canon/math/sgdg2.md) | ICPR 2020 | [Stochastic Runge-Kutta methods and adaptive SGD-G2 stochastic gradient descent](https://arxiv.org/abs/2002.09304) | — | — |
| [ACMo](canon/math/acmo.md) | AAAI 2021 | [ACMo: Angle-Calibrated Moment Methods for Stochastic Optimization](https://arxiv.org/abs/2006.07065) | — | — |
| [ACProp](canon/math/acprop.md) | NeurIPS 2021 | [Momentum Centering and Asynchronous Update for Adaptive Gradient Methods](https://arxiv.org/abs/2110.05454) | [official](https://github.com/juntang-zhuang/ACProp-Optimizer) | — |
| [AdaL](canon/math/adal.md) | arXiv 2021 | [AdaL: Adaptive Gradient Transformation Contributes to Convergences and Generalizations](https://arxiv.org/abs/2107.01525) | — | — |
| [AdamD](canon/math/adamd.md) | arXiv 2021 | [AdamD: Improved bias-correction in Adam](https://arxiv.org/abs/2110.10828) | — | — |
| [AdamP](canon/math/adamp.md) | ICLR 2021 | [AdamP: Slowing Down the Slowdown for Momentum Optimizers on Scale-invariant Weights](https://arxiv.org/abs/2006.08217) | [official](https://github.com/clovaai/AdamP) | `AdamP` |
| [Adaptive Gradient Clipping (AGC)](canon/math/adaptivegradientclippingagc.md) | ICML 2021 | [High-Performance Large-Scale Image Recognition Without Normalization](https://arxiv.org/abs/2102.06171) | [official](https://github.com/google-deepmind/deepmind-research/tree/master/nfnets) | — |
| [AngularGrad](canon/math/angulargrad.md) | arXiv 2021 | [AngularGrad: A New Optimization Technique for Angular Convergence of Convolutional Neural Networks](https://arxiv.org/abs/2105.10190) | [official](https://github.com/mhaut/AngularGrad) | — |
| [BGADAM](canon/math/bgadam.md) | IJCNN 2021 | [BGADAM: Boosting based Genetic-Evolutionary ADAM for Neural Network Optimization](https://arxiv.org/abs/1908.08015) | — | — |
| [Gravity](canon/math/gravity.md) | arXiv 2021 | [Gravity Optimizer: a Kinematic Approach on Optimization in Deep Learning](https://arxiv.org/abs/2101.09192) | [official](https://github.com/dariush-bahrami/gravity.optimizer) | `Gravity` |
| [MADGRAD](canon/math/madgrad.md) | arXiv 2021 | [Adaptivity without Compromise: A Momentumized, Adaptive, Dual Averaged Gradient Method for Stochastic Optimization](https://arxiv.org/abs/2101.11075) | [official](https://github.com/facebookresearch/madgrad) | `MADGRAD`, `MirrorMADGRAD` |
| [MaxVA](canon/math/maxva.md) | ECML PKDD 2021 | [MaxVA: Fast Adaptation of Step Sizes by Maximizing Observed Variance of Gradients](https://arxiv.org/abs/2006.11918) | [official](https://github.com/zhuchen03/MaxVA) | — |
| [Nero](canon/math/nero.md) | ICML 2021 | [Learning by Turning: Neural Architecture Aware Optimisation](https://arxiv.org/abs/2102.07227) | [official](https://github.com/jxbz/nero) | — |
| [PNM](canon/math/pnm.md) | ICML 2021 | [Positive-Negative Momentum: Manipulating Stochastic Gradient Noise to Improve Generalization](https://arxiv.org/abs/2103.17182) | [official](https://github.com/zeke-xie/Positive-Negative-Momentum) | — |
| [AdaPNM](canon/math/adapnm.md) | ICML 2021 | [Positive-Negative Momentum: Manipulating Stochastic Gradient Noise to Improve Generalization](https://arxiv.org/abs/2103.17182) | [official](https://github.com/zeke-xie/Positive-Negative-Momentum) | `AdaPNM` |
| [Ranger21](canon/math/ranger21.md) | arXiv 2021 | [Ranger21: a synergistic deep learning optimizer](https://arxiv.org/abs/2106.13731) | [official](https://github.com/lessw2020/Ranger21) | `Ranger21` |
| [SGDP](canon/math/sgdp.md) | ICLR 2021 | [AdamP: Slowing Down the Slowdown for Momentum Optimizers on Scale-invariant Weights](https://arxiv.org/abs/2006.08217) | [official](https://github.com/clovaai/AdamP) | `SGDP` |
| [AdaFamily](canon/math/adafamily.md) | arXiv 2022 | [AdaFamily: A family of Adam-like adaptive gradient methods](https://arxiv.org/abs/2203.01603) | — | — |
| [Adai](canon/math/adai.md) | ICML 2022 | [Adaptive Inertia: Disentangling the Effects of Adaptive Learning Rate and Momentum](https://arxiv.org/abs/2006.15815) | [official](https://github.com/zeke-xie/adaptive-inertia-adai) | `Adai` |
| [AdamMC](canon/math/adammc.md) | CVMI 2022 | [Moment Centralization based Gradient Descent Optimizers for Convolutional Neural Networks](https://arxiv.org/abs/2207.09066) | — | — |
| [Adan](canon/math/adan.md) | arXiv 2022 | [Adan: Adaptive Nesterov Momentum Algorithm for Faster Optimizing Deep Models](https://arxiv.org/abs/2208.06677) | [official](https://github.com/sail-sg/Adan) | `Adan` |
| [AdaSmooth](canon/math/adasmooth.md) | arXiv 2022 | [AdaSmooth: An Adaptive Learning Rate Method based on Effective Ratio](https://arxiv.org/abs/2204.00825) | — | `AdaSmooth` |
| [AEGDM](canon/math/aegdm.md) | Annals of Applied Mathematics 2022 | [An Adaptive Gradient Method with Energy and Momentum](https://arxiv.org/abs/2203.12191) | [official](https://github.com/txping/AEGDM) | — |
| [Amos](canon/math/amos.md) | arXiv 2022 | [Amos: An Adam-style Optimizer with Adaptive Weight Decay towards Model-Oriented Scale](https://arxiv.org/abs/2210.11693) | [official](https://github.com/google-research/jestimator) | `Amos` |
| [GDA-AM](canon/math/gdaam.md) | ICLR 2022 | [GDA-AM: On the effectiveness of solving minimax optimization via Anderson Acceleration](https://arxiv.org/abs/2110.02457) | [official](https://github.com/hehuannb/GDA-AM) | — |
| [KOALA](canon/math/koala.md) | AAAI 2022 | [KOALA: A Kalman Optimization Algorithm with Loss Adaptivity](https://arxiv.org/abs/2107.03331) | [official](https://github.com/Araachie/koala) | — |
| [RotoGrad](canon/math/rotograd.md) | ICLR 2022 | [RotoGrad: Gradient Homogenization in Multitask Learning](https://arxiv.org/abs/2103.02631) | [official](https://github.com/adrianjav/rotograd) | — |
| [SRSGD](canon/math/srsgd.md) | SIAM Journal on Imaging Sciences 2022 | [Scheduled Restart Momentum for Accelerated Stochastic Gradient Descent](https://arxiv.org/abs/2002.10583) | — | — |
| [Step-Tuned SGD](canon/math/steptunedsgd.md) | Neural Processing Letters 2022 | [Second-order step-size tuning of SGD for non-convex optimization](https://arxiv.org/abs/2103.03570) | — | — |
| [AdaInject](canon/math/adainject.md) | IEEE TAI 2023 | [AdaInject: Injection Based Adaptive Gradient Descent Optimizers for Convolutional Neural Networks](https://arxiv.org/abs/2109.12504) | [official](https://github.com/shivram1987/AdaInject) | — |
| [AdaNorm](canon/math/adanorm.md) | WACV 2023 | [AdaNorm: Adaptive Gradient Norm Correction based Optimizer for CNNs](https://arxiv.org/abs/2210.06364) | [official](https://github.com/shivram1987/AdaNorm) | `AdaNorm` |
| [AGD](canon/math/agd.md) | NeurIPS 2023 | [AGD: an Auto-switchable Optimizer using Stepwise Gradient Difference for Preconditioning Matrix](https://arxiv.org/abs/2312.01658) | — | — |
| [Aida](canon/math/aida.md) | TMLR 2023 | [A DNN Optimizer that Improves over AdaBelief by Suppression of the Adaptive Stepsize Range](https://arxiv.org/abs/2203.13273) | [official](https://github.com/guoqiang-zhang-x/Aida-Optimizer) | — |
| [Lion](canon/math/lion.md) | NeurIPS 2023 | [Symbolic Discovery of Optimization Algorithms](https://arxiv.org/abs/2302.06675) | [official](https://github.com/google/automl/tree/master/lion) | `Lion` |
| [Lookaround](canon/math/lookaround.md) | NeurIPS 2023 | [Lookaround Optimizer: k steps around, 1 step average](https://arxiv.org/abs/2306.07684) | — | — |
| [MultiAdam](canon/math/multiadam.md) | ICML 2023 | [MultiAdam: Parameter-wise Scale-invariant Optimizer for Multiscale Training of Physics-informed Neural Networks](https://arxiv.org/abs/2306.02816) | — | — |
| [RLEKF](canon/math/rlekf.md) | AAAI 2023 | [RLEKF: An Optimizer for Deep Potential with Ab Initio Accuracy](https://arxiv.org/abs/2212.06989) | — | — |
| [Scheduled Weight Decay (SWD)](canon/math/scheduledweightdecayswd.md) | NeurIPS 2023 | [On the Overlooked Pitfalls of Weight Decay and How to Mitigate Them: A Gradient-Norm Perspective](https://arxiv.org/abs/2011.11152) | [official](https://github.com/zeke-xie/stable-weight-decay-regularization) | — |
| [SGDF](canon/math/sgdf.md) | arXiv 2023 | [Signal Processing Meets SGD: From Momentum to Filter](https://arxiv.org/abs/2311.02818) | — | — |
| [StableAdamW](canon/math/stableadamw.md) | NeurIPS 2023 | [Stable and low-precision training for large-scale vision-language models](https://arxiv.org/abs/2304.13013) | [community](https://github.com/kozistr/pytorch_optimizer) | `StableAdamW` |
| [AdaAct](canon/math/adaact.md) | ICDMW 2024 | [An Adaptive Method Stabilizing Activations for Enhanced Generalization](https://arxiv.org/abs/2506.08353) | — | — |
| [Adam-atan2](canon/math/adamatan2.md) | ICML 2024 | [Scaling Exponents Across Parameterizations and Optimizers](https://arxiv.org/abs/2407.05872) | [community](https://github.com/lucidrains/adam-atan2-pytorch) | `AdamAtan2` |
| [Adam-Rel](canon/math/adamrel.md) | NeurIPS 2024 | [Adam on Local Time: Addressing Nonstationarity in RL with Relative Adam Timesteps](https://arxiv.org/abs/2412.17113) | — | — |
| [AdEMAMix](canon/math/ademamix.md) | arXiv 2024 | [The AdEMAMix Optimizer: Better, Faster, Older](https://arxiv.org/abs/2409.03137) | [official](https://github.com/apple/ml-ademamix) | `AdEMAMix` |
| [ADOPT](canon/math/adopt.md) | NeurIPS 2024 | [ADOPT: Modified Adam Can Converge with Any β₂ with the Optimal Rate](https://arxiv.org/abs/2411.02853) | [official](https://github.com/iShohei220/adopt) | `ADOPT` |
| [AGS-GD](canon/math/agsgd.md) | arXiv 2024 | [Anisotropic Gaussian Smoothing for Gradient-based Optimization](https://arxiv.org/abs/2411.11747) | — | — |
| [BADM](canon/math/badm.md) | arXiv 2024 | [BADM: Batch ADMM for Deep Learning](https://arxiv.org/abs/2407.01640) | — | — |
| [CaAdam](canon/math/caadam.md) | arXiv 2024 | [CaAdam: Improving Adam optimizer using connection aware methods](https://arxiv.org/abs/2410.24216) | [official](https://github.com/remigenet/CaAdam) | — |
| [CAdam](canon/math/cadam.md) | arXiv 2024 | [CAdam: Confidence-Based Optimization for Online Learning](https://arxiv.org/abs/2411.19647) | — | — |
| [Cautious Optimizers](canon/math/cautiousoptimizers.md) | arXiv 2024 | [Cautious Optimizers: Improving Training with One Line of Code](https://arxiv.org/abs/2411.16085) | [official](https://github.com/kyleliang919/C-Optim) | — |
| [EXAdam](canon/math/exadam.md) | arXiv 2024 | [EXAdam: The Power of Adaptive Cross-Moments](https://arxiv.org/abs/2412.20302) | [official](https://github.com/AhmedMostafa16/EXAdam) | `EXAdam` |
| [FAdam](canon/math/fadam.md) | arXiv 2024 | [FAdam: Adam is a natural gradient optimizer using diagonal empirical Fisher information](https://arxiv.org/abs/2405.12807) | [community](https://github.com/lessw2020/FAdam_PyTorch) | `FAdam` |
| [GrokAdamW](canon/math/grokadamw.md) | — | AdamW variant with Grokfast-style gradient amplification | [official](https://github.com/QuixiAI/grokadamw) | `GrokAdamW` |
| [Grokfast](canon/math/grokfast.md) | arXiv 2024 | [Grokfast: Accelerated Grokking by Amplifying Slow Gradients](https://arxiv.org/abs/2405.20233) | [official](https://github.com/ironjr/grokfast) | — |
| [INNAprop](canon/math/innaprop.md) | arXiv 2024 | [A second-order-like optimizer with adaptive gradient scaling for deep learning](https://arxiv.org/abs/2410.05871) | [official](https://github.com/innaprop/innaprop) | — |
| [KATE](canon/math/kate.md) | NeurIPS 2024 | [Remove that Square Root: A New Efficient Scale-Invariant Version of AdaGrad](https://arxiv.org/abs/2403.02648) | [official](https://github.com/nazya/KATE) | — |
| [MADA](canon/math/mada.md) | ICML 2024 | [MADA: Meta-Adaptive Optimizers through hyper-gradient Descent](https://arxiv.org/abs/2401.08893) | — | — |
| [RSGDM](canon/math/rsgdm.md) | CCSB 2024 | [Reducing Bias in Deep Learning Optimization: The RSGDM Approach](https://arxiv.org/abs/2409.15314) | — | — |
| [SET-Adam](canon/math/setadam.md) | ECML PKDD 2024 | [On Suppressing Range of Adaptive Stepsizes of Adam to Improve Generalisation Performance](https://arxiv.org/abs/2302.01029) | — | — |
| [SNGM](canon/math/sngm.md) | Science China Information Sciences 2024 | [Stochastic Normalized Gradient Descent with Momentum for Large-Batch Training](https://arxiv.org/abs/2007.13985) | — | — |
| [SRMM](canon/math/srmm.md) | JMLR 2024 | [Stochastic regularized majorization-minimization with weakly convex and multi-convex surrogates](https://arxiv.org/abs/2201.01652) | [official](https://github.com/HanbaekLyu/SRMM) | — |
| [TAM](canon/math/tam.md) | arXiv 2024 | [Torque-Aware Momentum](https://arxiv.org/abs/2412.18790) | — | — |
| [WarpAdam](canon/math/warpadam.md) | arXiv 2024 | [WarpAdam: A new Adam optimizer based on Meta-Learning approach](https://arxiv.org/abs/2409.04244) | — | — |
| [AbsSADMM](canon/math/abssadmm.md) | arXiv 2025 | [Stochastic ADMM with batch size adaptation for nonconvex nonsmooth optimization](https://arxiv.org/abs/2505.06921) | — | — |
| [AdamC](canon/math/adamc.md) | arXiv 2025 | [Why Gradients Rapidly Increase Near the End of Training](https://arxiv.org/abs/2506.02285) | — | — |
| [AdamNX](canon/math/adamnx.md) | arXiv 2025 | [AdamNX: An Adam improvement algorithm based on a novel exponential decay mechanism for the second-order moment estimate](https://arxiv.org/abs/2511.13465) | [official](https://github.com/mengzhu0308/AdamNX) | — |
| [AdamS](canon/math/adams.md) | EMNLP 2025 | [AdamS: Momentum Itself Can Be A Normalizer for LLM Pretraining and Post-training](https://arxiv.org/abs/2505.16363) | — | — |
| [adaNAPG](canon/math/adanapg.md) | arXiv 2025 | [Boosting Accelerated Proximal Gradient Method with Adaptive Sampling for Stochastic Composite Optimization](https://arxiv.org/abs/2507.18277) | — | — |
| [Ano](canon/math/ano.md) | arXiv 2025 | [ANO : Faster is Better in Noisy Landscape](https://arxiv.org/abs/2508.18258) | [official](https://github.com/adrienkegreisz/ano-optimizer) | — |
| [BCOS](canon/math/bcos.md) | arXiv 2025 | [Stochastic Approximation with Block Coordinate Optimal Stepsizes](https://arxiv.org/abs/2507.08963) | [official](https://github.com/facebookresearch/bcos) | — |
| [Cautious Weight Decay](canon/math/cautiousweightdecay.md) | arXiv 2025 | [Cautious Weight Decay](https://arxiv.org/abs/2510.12402) | [community](https://github.com/kozistr/pytorch_optimizer) | — |
| [Conda](canon/math/conda.md) | arXiv 2025 | [Conda: Column-Normalized Adam for Training Large Language Models Faster](https://arxiv.org/abs/2509.24218) | [official](https://github.com/jie040109/Conda) | — |
| [Coupled Adam](canon/math/coupledadam.md) | ACL 2025 | [Better Embeddings with Coupled Adam](https://arxiv.org/abs/2502.08441) | — | — |
| [DecGD](canon/math/decgd.md) | Machine Learning 2025 | [A New Adaptive Gradient Method with Gradient Decomposition](https://arxiv.org/abs/2107.08377) | — | — |
| [DEO](canon/math/deo.md) | arXiv 2025 | [Dimer-Enhanced Optimization: A First-Order Approach to Escaping Saddle Points in Neural Network Training](https://arxiv.org/abs/2507.19968) | [official](https://github.com/YueHuLab/DimerTrainer) | — |
| [EmoNavi](canon/math/emonavi.md) | — | An emotion-driven optimizer that feels loss and navigates accordingly | [official](https://github.com/muooon/EmoNavi) | — |
| [MARS](canon/math/mars.md) | ICML 2025 | [MARS: Unleashing the Power of Variance Reduction for Training Large Models](https://arxiv.org/abs/2411.10438) | [official](https://github.com/AGI-Arena/MARS) | `MARS` |
| [FOCUS](canon/math/focus.md) | arXiv 2025 | [FOCUS: First Order Concentrated Updating Scheme](https://arxiv.org/abs/2501.12243) | [official](https://github.com/liuyz0/FOCUS) | `FOCUS` |
| [FSGDM](canon/math/fsgdm.md) | ICLR 2025 | [On the Performance Analysis of Momentum Method: A Frequency Domain Perspective](https://arxiv.org/abs/2411.19671) | — | — |
| [Grams](canon/math/grams.md) | ICLR Workshop 2025 | [Grams: Gradient Descent with Adaptive Momentum Scaling](https://arxiv.org/abs/2412.17107) | [official](https://github.com/Gunale0926/Grams) | `Grams` |
| [HGM](canon/math/hgm.md) | arXiv 2025 | [Hindsight-Guided Momentum (HGM) Optimizer: An Approach to Adaptive Learning Rate](https://arxiv.org/abs/2506.22479) | — | — |
| [HVAdam](canon/math/hvadam.md) | AAAI 2025 | [HVAdam: A Full-Dimension Adaptive Optimizer](https://arxiv.org/abs/2511.20277) | — | — |
| [KO](canon/math/ko.md) | arXiv 2025 | [KO: Kinetics-inspired Neural Optimizer with PDE Simulation Approaches](https://arxiv.org/abs/2505.14777) | — | — |
| [KOALA++](canon/math/koala2.md) | NeurIPS 2025 | [KOALA++: Efficient Kalman-Based Optimization with Gradient-Covariance Products](https://arxiv.org/abs/2506.04432) | — | — |
| [Kourkoutas-Beta](canon/math/kourkoutassoftmaxflex.md) | arXiv 2025 | [Kourkoutas-Beta: A Sunspike-Driven Adam Optimizer with Desert Flair](https://arxiv.org/abs/2508.12996) | [official](https://github.com/sck-at-ucy/kbeta) | `KourkoutasSoftmaxFlex` |
| [MIAdam](canon/math/miadam.md) | AAAI 2025 | [A Method for Enhancing Generalization of Adam by Multiple Integrations](https://arxiv.org/abs/2412.12473) | [official](https://github.com/LongJin-lab/MIAdam) | — |
| [μ²-SGD](canon/math/sgd-v.md) | ICLR 2025 | [Do Stochastic, Feel Noiseless: Stable Stochastic Optimization via a Double Momentum Mechanism](https://arxiv.org/abs/2304.04172) | — | — |
| [⊥Grad (OrthoGrad)](canon/math/gradorthograd.md) | ICLR 2025 | [Grokking at the Edge of Numerical Stability](https://arxiv.org/abs/2501.04697) | [official](https://github.com/LucasPrietoAl/grokking-at-the-edge-of-numerical-stability) | — |
| [Overshoot](canon/math/overshoot.md) | arXiv 2025 | [Overshoot: Taking advantage of future gradients in momentum-based stochastic optimization](https://arxiv.org/abs/2501.09556) | [official](https://github.com/kinit-sk/overshoot) | — |
| [PadamP](canon/math/padamp.md) | arXiv 2025 | [Adaptive Moment Estimation Optimization Algorithm Using Projection Gradient for Deep Learning](https://arxiv.org/abs/2503.10005) | — | — |
| [Simplified-AdEMAMix](canon/math/simplifiedademamix.md) | arXiv 2025 | [Connections between Schedule-Free Optimizers, AdEMAMix, and Accelerated SGD Variants](https://arxiv.org/abs/2502.02431) | [official](https://github.com/DepenM/Simplified-AdEMAMix) | — |
| [LyAm](canon/math/lyam.md) | arXiv 2025 | [LyAm: Robust Non-Convex Optimization for Stable Learning in Noisy Environments](https://arxiv.org/abs/2507.11262) | — | — |
| [NIRMAL](canon/math/nirmal.md) | arXiv 2025 | [Comparative Analysis of Novel NIRMAL Optimizer Against Adam and SGD with Momentum](https://arxiv.org/abs/2508.04293) | — | — |
| [SCSAdamW](canon/math/scsadamw.md) | arXiv 2025 | [Beyond First-Order: Training LLMs with Stochastic Conjugate Subgradients and AdamW](https://arxiv.org/abs/2507.01241) | [official](https://github.com/yhz0/scs-experiments) | — |
| [SKA-SGD](canon/math/skasgd.md) | arXiv 2025 | [Streaming Krylov-Accelerated Stochastic Gradient Descent](https://arxiv.org/abs/2505.07046) | — | — |
| [SoftSignSGD (S3)](canon/math/softsignsgds3.md) | arXiv 2025 | [SoftSignSGD(S3): An Enhanced Optimizer for Practical DNN Training and Loss Spikes Minimization Beyond Adam](https://arxiv.org/abs/2507.06464) | — | — |
| [SPAM](canon/math/spam-v.md) | arXiv 2025 | [SPAM: Spike-Aware Adam with Momentum Reset for Stable LLM Training](https://arxiv.org/abs/2501.06842) | [official](https://github.com/TianjinYellow/SPAM-Optimizer) | — |
| [VSGD](canon/math/vsgd.md) | TMLR 2025 | [Variational Stochastic Gradient Descent for Deep Neural Networks](https://arxiv.org/abs/2404.06549) | [official](https://github.com/generativeai-tue/vsgd) | — |
| [ZetA](canon/math/zeta.md) | arXiv 2025 | [ZetA: A Riemann Zeta-Scaled Extension of Adam for Deep Learning](https://arxiv.org/abs/2508.02719) | — | — |
| [AdaGC](canon/math/adagc.md) | ICML 2026 | [AdaGC: Enhancing LLM Pretraining Stability via Adaptive Gradient Clipping](https://arxiv.org/abs/2502.11034) | — | `AdaGC` |
| [Anon](canon/math/anon.md) | arXiv 2026 | [Anon: Extrapolating Adaptivity Beyond SGD and Adam](https://arxiv.org/abs/2605.02317) | — | — |
| [C-Adam](canon/math/cadam2.md) | arXiv 2026 | [A Theoretical and Experimental Study of a Novel Adaptive Learning Algorithm](https://arxiv.org/abs/2605.29273) | — | — |
| [DualAdam](canon/math/dualadam.md) | arXiv 2026 | [Combining Adam and its Inverse Counterpart to Enhance Generalization of Deep Learning Optimizers](https://arxiv.org/abs/2603.07122) | [official](https://github.com/LongJin-lab/DualAdam) | — |
| [FANoS](canon/math/fanos.md) | arXiv 2026 | [FANoS-v2: Feedback-Controlled Momentum with Thermostat Damping for Lightweight Neural Optimization](https://arxiv.org/abs/2601.00889) | [official](https://github.com/nalin-dhiman/fanos) | — |
| [GradPower](canon/math/gradpower.md) | ICML 2026 | [GradPower: Powering Gradients for Faster Language Model Pre-Training](https://arxiv.org/abs/2505.24275) | — | — |
| [HomeAdam](canon/math/homeadam.md) | arXiv 2026 | [HomeAdam: Adam and AdamW Algorithms Sometimes Go Home to Obtain Better Provable Generalization](https://arxiv.org/abs/2603.02649) | — | — |
| [NOVAK](canon/math/novak.md) | arXiv 2026 | [NOVAK: Unified adaptive optimizer for deep neural networks](https://arxiv.org/abs/2601.07876) | — | — |
| [PS-Clip-SGD](canon/math/psclipsgd.md) | arXiv 2026 | [Robust and Fast Training via Per-Sample Clipping](https://arxiv.org/abs/2605.02701) | — | — |
| [SparseOpt](canon/math/sparseopt.md) | ICML 2026 | [SparseOpt: Addressing Normalization-induced Gradient Skew in Sparse Training](https://arxiv.org/abs/2605.27541) | — | — |
| [Stable-SPAM / GradientStabilizer](canon/math/stablespamgradientstabilizer.md) | ICML 2026 | [GradientStabilizer: Fix the Norm, Not the Gradient](https://arxiv.org/abs/2502.17055) | [official](https://github.com/TianjinYellow/StableSPAM) | — |
| [VRAdam](canon/math/vradam.md) | ICLR 2026 | [A Physics-Inspired Optimizer: Velocity Regularized Adam](https://arxiv.org/abs/2505.13196) | [official](https://github.com/pranavjv/vradam) | — |
| [SparseAdam](canon/math/sparseadam.md) | — | Adam variant for sparse gradients | [official](https://github.com/pytorch/pytorch/blob/main/torch/optim/sparse_adam.py) | `SparseAdam` |
| [OptMuon](canon/math/optmuon.md) | arXiv 2026 | [OptMuon: Closed-Loop Orthogonalized Momentum Methods for Stochastic Optimization with Zero-Noise Optimality](https://arxiv.org/abs/2606.08783) | — | — |
| [FOGO](canon/math/fogo.md) | arXiv 2026 | [FOGO: Forgetting-aware Orthogonalization Optimizer](https://arxiv.org/abs/2606.10406) | — | — |
| [AdamO](canon/math/adamo.md) | ICML 2026 | [Preserving Plasticity in Continual Learning via Dynamical Isometry](https://arxiv.org/abs/2606.09762) | — | — |
| [MAdam](canon/math/madam.md) | arXiv 2026 | [MAdam: Metric-Aware Multi-Objective Adam](https://arxiv.org/abs/2606.03904) | — | — |
| [MuCon](canon/math/mucon.md) | arXiv 2026 | [MuCon: Clipped Muon Updates for LLM Training](https://arxiv.org/abs/2605.26459) | — | — |
| [NuMuon](canon/math/numuon.md) | arXiv 2026 | [NuMuon: Nuclear-Norm-Constrained Muon for Compressible LLM Training](https://arxiv.org/abs/2603.03597) | — | — |
| [MiMuon](canon/math/mimuon.md) | arXiv 2026 | [MiMuon: Mixed Muon Optimizer with Improved Generalization for Large Models](https://arxiv.org/abs/2605.19619) | — | — |
| [Pion](canon/math/pion.md) | arXiv preprint (cs.LG, stat.ML) 2026 | [Pion: A Spectrum-Preserving Optimizer via Orthogonal Equivalence Transformation](https://arxiv.org/abs/2605.12492) | [official](https://github.com/Sphere-AI-Lab/pion) | — |
| [iMuon (Intrinsic Muon)](canon/math/imuonintrinsicmuon.md) | arXiv 2026 | [Intrinsic Muon: Spectral Optimization on Riemannian Matrix Manifolds](https://arxiv.org/abs/2605.09238) | [official](https://github.com/1bang118/manifold-intrinsic-muon) | — |
| [Muon-OGD](canon/math/muonogd.md) | arXiv 2026 | [Muon-OGD: Muon-based Spectral Orthogonal Gradient Projection for LLM Continual Learning](https://arxiv.org/abs/2605.08949) | — | — |
| [Newton-Muon](canon/math/newtonmuon.md) | arXiv 2026 | [The Newton-Muon Optimizer](https://arxiv.org/abs/2604.01472) | [official](https://github.com/zhehangdu/Newton-Muon) | — |
| [MuonEq](canon/math/muoneq.md) | arXiv 2026 | [MuonEq: Balancing Before Orthogonalization with Lightweight Equilibration](https://arxiv.org/abs/2603.28254) | [official](https://github.com/MaeChd/muon-eq) | — |
| [RMNP](canon/math/rmnp.md) | arXiv 2026 | [RMNP: Row-Momentum Normalized Preconditioning for Scalable Matrix-Based Optimization](https://arxiv.org/abs/2603.20527) | [official](https://github.com/Dominator-Index/RMNP) | — |
| [MUD](canon/math/mud.md) | arXiv preprint 2026 | [Beyond Muon: MUD (MomentUm Decorrelation) for Faster Transformer Training](https://arxiv.org/abs/2603.17970) | — | — |
| [NAMO](canon/math/namo.md) | arXiv 2026 | [Adam Improves Muon: Adaptive Moment Estimation with Orthogonalized Momentum](https://arxiv.org/abs/2602.17080) | [official](https://github.com/minxin-zhg/namo) | — |
| [SpecMuon](canon/math/specmuon.md) | arXiv 2026 | [Muon with Spectral Guidance: Efficient Optimization for Scientific Machine Learning](https://arxiv.org/abs/2602.16167) | — | — |
| [ARO](canon/math/aro.md) | arXiv 2026 | [ARO: A New Lens On Matrix Optimization For Large Models](https://arxiv.org/abs/2602.09006) | — | — |
| [PRISM](canon/math/prism.md) | arXiv 2026 | [PRISM: Structured Optimization via Anisotropic Spectral Shaping](https://arxiv.org/abs/2602.03096) | — | — |
| [MCSD / SPEL](canon/math/mcsdspel.md) | arXiv 2026 | [Manifold constrained steepest descent](https://arxiv.org/abs/2601.21487) | — | — |
| [Variance-Adaptive Muon (Muon-NSR / Muon-VS)](canon/math/varianceadaptivemuonmuonnsrmuonvs.md) | arXiv 2026 | [Variance-Adaptive Muon: Accelerating LLM Pretraining with NSR-Modulated and Variance-Scaled Momentum](https://arxiv.org/abs/2601.14603) | — | — |
| [MuonAll](canon/math/muonall.md) | arXiv 2025 | [MuonAll: Muon Variant for Efficient Finetuning of Large Language Models](https://arxiv.org/abs/2511.06086) | [official](https://github.com/Saurabh750/optimizer) | — |
| [Gluon](canon/math/gluon.md) | arXiv 2025 (also accepted at ICML 2025 HiLD workshop) | [Gluon: Making Muon & Scion Great Again! (Bridging Theory and Practice of LMO-based Optimizers for LLMs)](https://arxiv.org/abs/2505.13416) | — | — |
| [LPSGD / LPSGDM](canon/math/lpsgdlpsgdm.md) | arXiv 2026 | [Beyond L2-norm and L-infinity-norm: A Curvature-Inspired ell_p-Norm Scheme for Deep Neural Networks](https://arxiv.org/abs/2606.02078) | — | — |
| [ABSignSGD](canon/math/absignsgd.md) | ICLR 2026 | [Arbitrary-Order Block SignSGD for Memory-Efficient LLM Fine-Tuning](https://openreview.net/forum?id=NQsdnYkCar) | — | — |
| [StoSignSGD](canon/math/stosignsgd.md) | arXiv 2026 | [StoSignSGD: Unbiased Structural Stochasticity Fixes SignSGD for Training Large Language Models](https://arxiv.org/abs/2604.15416) | — | — |
| [Hybrid SignSGD-SGD switching](canon/math/hybridsignsgdsgdswitching.md) | arXiv 2026 | [Enhancing SignSGD: Small-Batch Convergence Analysis and a Hybrid Switching Strategy](https://arxiv.org/abs/2604.25550) | — | — |
| [SoftSignum / SoftMuon](canon/math/softsignumsoftmuon.md) | ICML 2026 | [Softsign: Smooth Sign in Your Optimizer For Better Parameter Heterogeneity Handling](https://arxiv.org/abs/2605.31371) | [official](https://github.com/brain-lab-research/softsign) | — |
| [Accelerated SignGD](canon/math/acceleratedsigngd.md) | arXiv 2025 | [Norm-Constrained Flows and Sign-Based Optimization: Theory and Algorithms](https://arxiv.org/abs/2508.18510) | — | — |
| [CLion](canon/math/clion.md) | arXiv 2026 | [CLion: Efficient Cautious Lion Optimizer with Enhanced Generalization](https://arxiv.org/abs/2604.14587) | — | — |
| [OLion](canon/math/olion.md) | arXiv 2026 | [OLion: Approaching the Hadamard Ideal by Intersecting Spectral and ell_{infty} Implicit Biases](https://arxiv.org/abs/2602.01105) | [official](https://github.com/kv-wang/OLion) | — |
| [MGUP](canon/math/mgup.md) | NeurIPS 2025 | [MGUP: A Momentum-Gradient Alignment Update Policy for Stochastic Optimization](https://openreview.net/forum?id=TDFSKAspoQ) | [official](https://github.com/MaeChd/MGUP) | — |
| [Magma](canon/math/magma.md) | arXiv 2026 | [On Surprising Effectiveness of Masking Updates in Adaptive Optimizers](https://arxiv.org/abs/2602.15322) | — | — |
| [AGGC](canon/math/aggc.md) | ACL 2026 | [AGGC: Adaptive Group Gradient Clipping for Stabilizing Large Language Model Training](https://arxiv.org/abs/2601.11864) | [official](https://github.com/ZhiyuanLi218/AGGC) | — |
| [Clipped Scion](canon/math/clippedscion.md) | NeurIPS 2025 | [Generalized Gradient Norm Clipping & Non-Euclidean (L_0,L_1)-Smoothness](https://arxiv.org/abs/2506.01913) | [official](https://github.com/LIONS-EPFL/ClippedScion) | — |
| [SPECTRA](canon/math/spectra.md) | ICML 2026 | [Enhancing LLM Training via Spectral Clipping](https://arxiv.org/abs/2603.14315) | [official](https://github.com/mlolab/llm-spectral-clipping) | — |
| [Spectral Clipping (matrix-valued)](canon/math/spectralclippingmatrixvalued.md) | arXiv 2026 | [Gradient Clipping Beyond Vector Norms: A Spectral Approach for Matrix-Valued Parameters](https://arxiv.org/abs/2605.11838) | — | — |
| [SPAMP](canon/math/spamp.md) | ACM Multimedia Asia 2025 (7th ACM International Conference on Multimedia in Asia) | [Gradient Shaping Beyond Clipping: A Functional Perspective on Update Magnitude Control](https://arxiv.org/abs/2510.01578) | — | — |
| [NucGD](canon/math/nucgd.md) | arXiv 2026 | [Towards The Implicit Bias on Multiclass Separable Data Under Norm Constraints](https://arxiv.org/abs/2603.22824) | [official](https://github.com/Tsokarsic/observing-the-implicit-bias-on-multiclass-seperable-data) | — |
| [Batched / Transported Scion](canon/math/batchedtransportedscion.md) | arXiv 2026 | [Scale-Invariant Neural Network Optimization: Norm Geometry and Heavy-Tailed Noise](https://arxiv.org/abs/2605.18528) | — | — |
| [EMA bias-corrected iterate averaging](canon/math/emabiascorrectediterateaveraging.md) | NeurIPS 2025 Workshop (OPT 2025) | [EMA Without the Lag: Bias-Corrected Iterate Averaging Schemes](https://arxiv.org/abs/2508.00180) | — | — |
| [RGrad-Avg](canon/math/rgradavg.md) | OPT 2025 (17th Annual Workshop on Optimization for Machine Learning, co-located with NeurIPS 2025) | [On Riemannian Gradient Descent Algorithm using gradient averaging](https://opt-ml.org/papers/2025/paper7.pdf) | — | — |
| [SGD with adaptive preconditioning](canon/math/sgdwithadaptivepreconditioning.md) | ICLR 2026 | [SGD with Adaptive Preconditioning: Unified Analysis and Momentum Acceleration](https://arxiv.org/abs/2506.23803) | — | — |
| [HTMuon](canon/math/htmuon.md) | arXiv 2026 | [HTMuon: Improving Muon via Heavy-Tailed Spectral Correction](https://arxiv.org/abs/2603.10067) | [official](https://github.com/TDCSZ327/HTmuon) | — |
| [MARS-M](canon/math/marsm.md) | arXiv 2025 | [MARS-M: When Variance Reduction Meets Matrices](https://arxiv.org/abs/2510.21800) | [official](https://github.com/AGI-Arena/MARS/tree/main/MARS_M) | — |
| [Drop-Muon](canon/math/dropmuon.md) | arXiv 2025 | [Drop-Muon: Update Less, Converge Faster](https://arxiv.org/abs/2510.02239) | — | — |
| [Muon+](canon/math/muon-v.md) | arXiv 2026 | [MUON+: Towards More Effective Muon via One Additional Normalization Step for LLM Pre-training](https://arxiv.org/abs/2602.21545) | [official](https://github.com/K1seki221/MuonPlus) | — |
| [TrasMuon](canon/math/trasmuon.md) | ICLR 2026 Workshop Sci4DL | [TrasMuon: Trust-Region Adaptive Scaling for Orthogonalized Momentum Optimizers](https://arxiv.org/abs/2602.13498) | — | — |
| [Adam-SHANG](canon/math/adamshang.md) | arXiv 2026 | [Adam-SHANG: A Convergent Adam-Type Method for Stochastic Smooth Convex Optimization](https://arxiv.org/abs/2605.12878) | — | — |
| [EMA-Nesterov](canon/math/emanesterov.md) | arXiv 2026 | [EMA-Nesterov: Stabilizing Nesterov's Lookahead for Accelerated Deep Learning Optimization](https://arxiv.org/abs/2605.25395) | — | — |
| [S-Adam](canon/math/sadam2.md) | arXiv 2026 | [Singularity-aware Optimization via Randomized Geometric Probing: Towards Stable Non-smooth Optimization](https://arxiv.org/abs/2605.29547) | — | — |
| [IAdaPID-ADG](canon/math/iadapidadg.md) | arXiv 2026 | [An Improved Adaptive PID Optimizer with Enhanced Convergence and Stability for Deep Learning](https://arxiv.org/abs/2605.21968) | — | — |
| [CT-AGD](canon/math/ctagd.md) | arXiv 2026 | [Accelerated Gradient Descent for Faster Convergence with Minimal Overhead](https://arxiv.org/abs/2605.16017) | — | — |
| [GPA (Generalized Primal Averaging)](canon/math/gpageneralizedprimalaveraging.md) | arXiv 2025 | [Smoothing DiLoCo with Primal Averaging for Faster Training of LLMs](https://arxiv.org/abs/2512.17131) | [official](https://github.com/facebookresearch/optimizers) | — |
| [SNOO](canon/math/snoo.md) | arXiv 2025 | [SNOO: Step-K Nesterov Outer Optimizer - The Surprising Effectiveness of Nesterov Momentum Applied to Pseudo-Gradients](https://arxiv.org/abs/2510.15830) | [official](https://github.com/vishal9-team/torchtitan-snoo) | — |
| [Riemannion](canon/math/riemannion.md) | ICLR 2026 | [LoRA meets Riemannion: Muon Optimizer for Parametrization-independent Low-Rank Adapters](https://arxiv.org/abs/2507.12142) | — | — |
| [Optimal Projection-Free Adaptive SGD](canon/math/optimalprojectionfreeadaptivesgd.md) | arXiv 2026 | [Optimal Projection-Free Adaptive SGD for Matrix Optimization](https://arxiv.org/abs/2604.02505) | — | — |
| [AdamCB](canon/math/adamcb.md) | ICLR 2025 | [ADAM Optimization with Adaptive Batch Selection](https://arxiv.org/abs/2512.06795) | — | — |
| [Kalman-Adam](canon/math/kalmanadam.md) | Knowledge-Based Systems 2026 | [Kalman-Adam: Optimal bayesian moment estimation for memory-Efficient and generalizable deep learning](https://doi.org/10.1016/j.knosys.2026.115907) | — | — |
| [AdamHD (AdamHuberDecay)](canon/math/adamhdadamhuberdecay.md) | NeurIPS 2025 Workshop (ScaleOpt: GPU-Accelerated and Scalable Optimization) | [AdamHD: Decoupled Huber Decay Regularization for Language Model Pre-Training](https://arxiv.org/abs/2511.14721) | — | — |
| [MVN-Grad](canon/math/mvngrad.md) | arXiv 2026 | [Adaptive Optimization via Momentum on Variance-Normalized Gradients](https://arxiv.org/abs/2602.10204) | — | — |
| [Compositional Muon (CM)](canon/math/compositionalmuoncm.md) | Tilde Research blog 2026 | [Towards Compositional Steepest Descent](https://blog.tilderesearch.com/blog/compositional-muon) | [official](https://github.com/tilde-research/comp-muon-release) | — |

### Memory-Efficient Optimizers

Memory-efficient optimizers reduce the optimizer-state memory that dominates large-model training budgets, where Adam-style methods store two extra full-precision values per parameter. The methods below cover factored second moments, 8-bit and 4-bit state quantization, low-rank gradient projection, block-coordinate updates, zeroth-order gradient estimates, and stateless update rules.

| Optimizer | Venue | Paper | Code | `zij` |
|---|---|---|---|---|
| [Adafactor](canon/math/adafactor.md) | ICML 2018 | [Adafactor: Adaptive Learning Rates with Sublinear Memory Cost](https://arxiv.org/abs/1804.04235) | [official](https://github.com/tensorflow/tensor2tensor/blob/master/tensor2tensor/utils/adafactor.py) | `Adafactor` |
| [SM3](canon/math/sm3.md) | NeurIPS 2019 | [Memory-Efficient Adaptive Optimization](https://arxiv.org/abs/1901.11150) | [official](https://github.com/google-research/google-research/tree/master/sm3) | `SM3` |
| [8-bit Optimizers](canon/math/8bitoptimizers.md) | ICLR 2022 | [8-bit Optimizers via Block-wise Quantization](https://arxiv.org/abs/2110.02861) | [official](https://github.com/bitsandbytes-foundation/bitsandbytes) | — |
| [tpSGD](canon/math/tpsgd.md) | arXiv 2022 | [Learning with Local Gradients at the Edge](https://arxiv.org/abs/2208.08503) | — | — |
| [4-bit Optimizers](canon/math/4bitoptimizers.md) | NeurIPS 2023 | [Memory Efficient Optimizers with 4-bit States](https://arxiv.org/abs/2309.01507) | [official](https://github.com/thu-ml/low-bit-optimizers) | — |
| [Adalite](canon/math/adalite.md) | GitHub 2023 | [Adalite: a custom optimizer based on Adafactor and LAMB](https://github.com/euclaise/SlimTrainer) | [official](https://github.com/euclaise/SlimTrainer) | — |
| [AdaLomo](canon/math/adalomo.md) | ACL 2024 Findings | [AdaLomo: Low-memory Optimization with Adaptive Learning Rate](https://arxiv.org/abs/2310.10195) | [official](https://github.com/OpenLMLab/LOMO) | `AdaLomo` |
| [CAME](canon/math/came.md) | ACL 2023 | [CAME: Confidence-guided Adaptive Memory Efficient Optimization](https://arxiv.org/abs/2307.02047) | [official](https://github.com/yangluo7/CAME) | `CAME` |
| [Lion](canon/math/lion-v.md) | NeurIPS 2023 | [Symbolic Discovery of Optimization Algorithms](https://arxiv.org/abs/2302.06675) | [official](https://github.com/google/automl/tree/master/lion) | — |
| [LOMO](canon/math/lomo.md) | ACL 2024 | [Full Parameter Fine-tuning for Large Language Models with Limited Resources](https://arxiv.org/abs/2306.09782) | [official](https://github.com/OpenLMLab/LOMO) | `Lomo` |
| [MeZO](canon/math/mezo.md) | NeurIPS 2023 | [Fine-Tuning Language Models with Just Forward Passes](https://arxiv.org/abs/2305.17333) | [official](https://github.com/princeton-nlp/MeZO) | — |
| [Tiger](canon/math/tiger.md) | GitHub 2023 | [Tiger: A Tight-fisted Optimizer](https://github.com/bojone/tiger/blob/main/README_en.md#citation) | [official](https://github.com/bojone/tiger) | `Tiger` |
| [4-bit Shampoo](canon/math/4bitshampoo.md) | NeurIPS 2024 | [4-bit Shampoo for Memory-Efficient Network Training](https://arxiv.org/abs/2405.18144) | [official](https://github.com/Sike-Wang/low-bit-Shampoo) | — |
| [Adam-mini](canon/math/adammini.md) | ICLR 2025 | [Adam-mini: Use Fewer Learning Rates To Gain More](https://arxiv.org/abs/2406.16793) | [official](https://github.com/zyushun/Adam-mini) | `AdamMini` |
| [Adapprox](canon/math/adapprox.md) | arXiv 2024 | [Adapprox: Adaptive Approximation in Adam Optimization via Randomized Low-Rank Matrices](https://arxiv.org/abs/2403.14958) | — | — |
| [AdaRankGrad](canon/math/adarankgrad.md) | ICLR 2025 | [AdaRankGrad: Adaptive Gradient-Rank and Moments for Memory-Efficient LLMs Training and Fine-Tuning](https://arxiv.org/abs/2410.17881) | — | — |
| [Addax](canon/math/addax.md) | ICLR 2025 | [Addax: Utilizing Zeroth-Order Gradients to Improve Memory Efficiency and Performance of SGD for Fine-Tuning Language Models](https://arxiv.org/abs/2410.06441) | [official](https://github.com/optimization-for-data-driven-science/Addax) | — |
| [APOLLO](canon/math/apollo.md) | MLSys 2025 | [APOLLO: SGD-like Memory, AdamW-level Performance](https://arxiv.org/abs/2412.05270) | [official](https://github.com/zhuhanqing/APOLLO) | `APOLLO` |
| [BAdam](canon/math/blockoptimizer.md) | NeurIPS 2024 | [BAdam: A Memory Efficient Full Parameter Optimization Method for Large Language Models](https://arxiv.org/abs/2404.02827) | [official](https://github.com/Ledzy/BAdam) | `BlockOptimizer` |
| [COAP](canon/math/coap.md) | CVPR 2025 | [COAP: Memory-Efficient Training with Correlation-Aware Gradient Projection](https://arxiv.org/abs/2412.00071) | [official](https://github.com/bytedance/coap) | — |
| [Fira](canon/math/firaadamw.md) | NeurIPS 2025 | [Fira: Can We Achieve Full-rank Training of LLMs Under Low-rank Constraint?](https://arxiv.org/abs/2410.01623) | [official](https://github.com/xichen-fy/Fira) | `FiraAdamW` |
| [Flora](canon/math/flora.md) | ICML 2024 | [Flora: Low-Rank Adapters Are Secretly Gradient Compressors](https://arxiv.org/abs/2402.03293) | [official](https://github.com/BorealisAI/flora-opt) | — |
| [FRUGAL](canon/math/frugal.md) | ICML 2025 | [FRUGAL: Memory-Efficient Optimization by Reducing State Overhead for Scalable Training](https://arxiv.org/abs/2411.07837) | [official](https://github.com/fzmushko/FRUGAL) | — |
| [GaLore](canon/math/galoreadamw.md) | ICML 2024 | [GaLore: Memory-Efficient LLM Training by Gradient Low-Rank Projection](https://arxiv.org/abs/2403.03507) | [official](https://github.com/jiaweizzhao/GaLore) | `GaLoreAdamW` |
| [GoLore](canon/math/golore.md) | ICML 2025 | [Subspace Optimization for Large Language Models with Convergence Guarantees](https://arxiv.org/abs/2410.11289) | [official](https://github.com/pkumelon/Golore) | — |
| [GRASS](canon/math/grass.md) | EMNLP 2024 | [Grass: Compute Efficient Low-Memory LLM Training with Structured Sparse Gradients](https://arxiv.org/abs/2406.17660) | [official](https://github.com/aashiqmuhamed/GRASS) | — |
| [LDAdam](canon/math/ldadamw.md) | ICLR 2025 | [LDAdam: Adaptive Optimization from Low-Dimensional Gradient Statistics](https://arxiv.org/abs/2410.16103) | [official](https://github.com/IST-DASLab/LDAdam) | `LDAdamW` |
| [LoQT](canon/math/loqt.md) | NeurIPS 2024 | [LoQT: Low-Rank Adapters for Quantized Pretraining](https://arxiv.org/abs/2405.16528) | [official](https://github.com/sebulo/LoQT) | — |
| [LoRA-RITE](canon/math/lorarite.md) | ICLR 2025 | [LoRA Done RITE: Robust Invariant Transformation Equilibration for LoRA Optimization](https://arxiv.org/abs/2410.20625) | [official](https://github.com/gkevinyen5418/LoRA-RITE) | — |
| [MicroAdam](canon/math/microadam.md) | NeurIPS 2024 | [MicroAdam: Accurate Adaptive Optimization with Low Space Overhead and Provable Convergence](https://arxiv.org/abs/2405.15593) | [official](https://github.com/IST-DASLab/MicroAdam) | — |
| [Muon](canon/math/muon.md) | Blog 2024 | [Muon: An optimizer for hidden layers in neural networks](https://kellerjordan.github.io/posts/muon/) | [official](https://github.com/KellerJordan/Muon) | `Muon` |
| [Online Subspace Descent](canon/math/onlinesubspacedescent.md) | NeurIPS 2024 | [Memory-Efficient LLM Training with Online Subspace Descent](https://arxiv.org/abs/2408.12857) | [official](https://github.com/kyleliang919/Online-Subspace-Descent) | — |
| [Q-GaLore](canon/math/qgalore.md) | CPAL 2025 | [Q-GaLore: Quantized GaLore with INT4 Projection and Layer-Adaptive Low-Rank Gradients](https://arxiv.org/abs/2407.08296) | [official](https://github.com/VITA-Group/Q-GaLore) | — |
| [SGD-SaI](canon/math/sgdsai.md) | arXiv 2024 | [No More Adam: Learning Rate Scaling at Initialization is All You Need](https://arxiv.org/abs/2412.11768) | [official](https://github.com/AnonymousAlethiometer/SGD_SaI) | `SGDSaI` |
| [SMMF](canon/math/smmf.md) | AAAI 2025 | [SMMF: Square-Matricized Momentum Factorization for Memory-Efficient Optimization](https://arxiv.org/abs/2412.08894) | [official](https://github.com/eai-lab/SMMF) | — |
| [SNSM](canon/math/snsm.md) | ICML 2025 | [Lean and Mean Adaptive Optimization via Subset-Norm and Subspace-Momentum with Convergence Guarantees](https://arxiv.org/abs/2411.07120) | [official](https://github.com/timmytonga/sn-sm) | — |
| [SWAN](canon/math/swan.md) | ICML 2025 | [SWAN: SGD with Normalization and Whitening Enables Stateless LLM Training](https://arxiv.org/abs/2412.13148) | — | — |
| [AlphaGrad](canon/math/alphagrad.md) | arXiv 2025 | [AlphaGrad: Non-Linear Gradient Normalization Optimizer](https://arxiv.org/abs/2504.16020) | — | — |
| [GWT](canon/math/gwt.md) | arXiv 2025 | [GWT: Scalable Optimizer State Compression for Large Language Model Training](https://arxiv.org/abs/2501.07237) | — | — |
| [MLorc](canon/math/mlorc.md) | AISTATS 2026 | [MLorc: Momentum Low-rank Compression for Memory Efficient Large Language Model Adaptation](https://arxiv.org/abs/2506.01897) | [official](https://github.com/weishen-git/MLorc) | — |
| [MoFaSGD](canon/math/mofasgd.md) | TMLR 2025 | [Low-rank Momentum Factorization for Memory Efficient Training](https://arxiv.org/abs/2507.08091) | [official](https://github.com/pmahdavi/MoFaSGD) | — |
| [RACS / Alice](canon/math/racsalice.md) | arXiv 2025 | [Towards Efficient Optimizer Design for LLM via Structured Fisher Approximation with a Low-Rank Extension](https://arxiv.org/abs/2502.07752) | [community](https://github.com/kozistr/pytorch_optimizer) | — |
| [SinkGD](canon/math/sinkgd.md) | arXiv 2025 | [Gradient Multi-Normalization for Stateless and Scalable LLM Training](https://arxiv.org/abs/2502.06742) | — | — |
| [SPAM](canon/math/spam.md) | ICLR 2025 | [SPAM: Spike-Aware Adam with Momentum Reset for Stable LLM Training](https://arxiv.org/abs/2501.06842) | [official](https://github.com/TianjinYellow/SPAM-Optimizer) | `SPAM` |
| [SubTrack++](canon/math/subtrack.md) | NeurIPS 2025 | [SubTrack++ : Gradient Subspace Tracking for Scalable LLM Training](https://arxiv.org/abs/2502.01586) | [official](https://github.com/criticalml-uw/SubTrack) | — |
| [SUMO](canon/math/sumo.md) | NeurIPS 2025 | [SUMO: Subspace-Aware Moment-Orthogonalization for Accelerating Memory-Efficient LLM Training](https://arxiv.org/abs/2505.24749) | — | — |
| [TensorGRaD](canon/math/tensorgrad.md) | arXiv 2025 | [TensorGRaD: Tensor Gradient Robust Decomposition for Memory-Efficient Neural Operator Training](https://arxiv.org/abs/2501.02379) | — | — |
| [FlashOptim](canon/math/flashoptim.md) | arXiv 2026 | [FlashOptim: Optimizers for Memory-Efficient Training](https://arxiv.org/abs/2602.23349) | [official](https://github.com/databricks/flashoptim) | — |
| [Rose](canon/math/rose.md) | GitHub 2026 | [Rose: Range-Of-Slice Equilibration optimizer](https://github.com/MatthewK78/Rose#-citation) | [official](https://github.com/MatthewK78/Rose) | — |
| [SAGE](canon/math/sage.md) | ACL 2026 Findings | [SAGE: Sign-Adaptive Gradient for Memory-Efficient LLM Optimization](https://arxiv.org/abs/2604.07663) | — | — |
| [BlockLLM](canon/math/blockllm.md) | arXiv 2024 | [BlockLLM: Memory-Efficient Adaptation of LLMs by Selecting and Optimizing the Right Coordinate Blocks](https://arxiv.org/abs/2406.17296) | [official](https://github.com/RAmruthaVignesh/blockllm) | — |
| [Natural GaLore](canon/math/naturalgalore.md) | arXiv 2024 | [Natural GaLore: Accelerating GaLore for memory-efficient LLM Training and Fine-tuning](https://arxiv.org/abs/2410.16029) | [official](https://github.com/selfsupervised-ai/Natural-GaLore) | — |
| [SLTrain](canon/math/sltrain.md) | NeurIPS 2024 | [SLTrain: a sparse plus low-rank approach for parameter and memory efficient pretraining](https://arxiv.org/abs/2406.02214) | [official](https://github.com/andyjm3/SLTrain) | — |
| [8-bit Muon](canon/math/8bitmuon.md) | arXiv 2025 | [Effective Quantization of Muon Optimizer States](https://arxiv.org/abs/2509.23106) | — | — |
| [FFT-based Subspace Selection](canon/math/fftbasedsubspaceselection.md) | ICLR 2026 | [FFT-based Dynamic Subspace Selection for Low-Rank Adaptive Optimization of Large Language Models](https://arxiv.org/abs/2505.17967) | [official](https://github.com/IST-DASLab/ISTA-DASLab-Optimizers) | — |
| [FOAM](canon/math/foam.md) | arXiv 2025 | [FOAM: Blocked State Folding for Memory-Efficient LLM Training](https://arxiv.org/abs/2512.07112) | [official](https://github.com/zqOuO/FOAM) | — |
| [GaLore 2](canon/math/galore2.md) | arXiv 2025 | [GaLore 2: Large-Scale LLM Pre-Training by Gradient Low-Rank Projection](https://arxiv.org/abs/2504.20437) | — | — |
| [GradientStabilizer](canon/math/gradientstabilizer.md) | ICML 2026 | [GradientStabilizer: Fix the Norm, Not the Gradient](https://arxiv.org/abs/2502.17055) | [official](https://github.com/TianjinYellow/GradientStabilizer) | — |
| [GUM](canon/math/gum.md) | arXiv 2025 | [Unbiased Gradient Low-Rank Projection](https://arxiv.org/abs/2510.17802) | — | — |
| [I3S](canon/math/i3s.md) | NeurIPS 2025 | [Breaking the Frozen Subspace: Importance Sampling for Low-Rank Optimization in LLM Pretraining](https://arxiv.org/abs/2502.05790) | — | — |
| [LORENZA](canon/math/lorenza.md) | TMLR 2026 | [LORENZA: Enhancing Generalization in Low-Rank Gradient LLM Training via Efficient Zeroth-Order Adaptive SAM](https://arxiv.org/abs/2502.19571) | — | — |
| [ProjFactor (VLoRP)](canon/math/projfactorvlorp.md) | arXiv 2025 | [Memory-Efficient LLM Training by Various-Grained Low-Rank Projection of Gradients](https://arxiv.org/abs/2505.01744) | — | — |
| [RSO](canon/math/rso.md) | arXiv 2025 | [A Memory Efficient Randomized Subspace Optimization Method for Training Large Language Models](https://arxiv.org/abs/2502.07222) | — | — |
| [SCALE](canon/math/scale.md) | ICML 2026 | [Memory-Efficient LLM Pretraining via Minimalist Optimizer Design](https://arxiv.org/abs/2506.16659) | — | — |
| [SlimAdam](canon/math/slimadam.md) | arXiv 2025 | [When Can You Get Away with Low Memory Adam?](https://arxiv.org/abs/2503.01843) | [official](https://github.com/dayal-kalra/low-memory-adam) | — |
| [LoRA-Pre](canon/math/lorapre.md) | ICLR 2026 | [Taming Momentum: Rethinking Optimizer States Through Low-Rank Approximation](https://arxiv.org/abs/2602.24283) | [official](https://github.com/mrflogs/LoRA-Pre) | — |
| [Lotus](canon/math/lotus.md) | arXiv 2026 | [Lotus: Efficient LLM Training by Randomized Low-Rank Gradient Projection with Adaptive Subspace Switching](https://arxiv.org/abs/2602.01233) | — | — |
| [POET-X](canon/math/poetx.md) | ICML 2026 | [POET-X: Memory-efficient LLM Training by Scaling Orthogonal Transformation](https://arxiv.org/abs/2603.05500) | [official](https://github.com/Sphere-AI-Lab/poet) | — |
| [MuonQ](canon/math/muonq.md) | arXiv 2026 | [MuonQ: Enhancing Low-Bit Muon Quantization via Directional Fidelity Optimization](https://arxiv.org/abs/2605.11396) | [official](https://github.com/YupengSu/MuonQ) | — |
| [4-bit-Muon-GRASP](canon/math/4bitmuongrasp.md) | ICLR 2026 | [Achieving low-bit Muon through subspace preservation and grid quantization](https://openreview.net/forum?id=g2l9bg9DWx) | [official](https://github.com/wuhuaijin/lowbit-Muon) | — |
| [IO-Adam](canon/math/ioadam.md) | OpenReview 2026 | [IO-Adam: Rethinking Memory-Efficient Adaptive Optimizers from Gradient Computation](https://openreview.net/forum?id=iCT5xdOlJH) | — | — |
| [H-Fac](canon/math/hfac.md) | AISTATS 2025 | [Memory-Efficient Optimization with Factorized Hamiltonian Descent](https://arxiv.org/abs/2406.09958) | — | — |
| [LiMuon](canon/math/limuon.md) | ICML 2026 | [LiMuon: Light and Fast Muon Optimizer for Large Models](https://arxiv.org/abs/2509.14562) | — | — |
| [M+Adam](canon/math/madam2.md) | OPT 2025: 17th Annual Workshop on Optimization for Machine Learning (NeurIPS 2025 Workshop) | [M+Adam: Stable Low-Precision Training with Combined Adam–Madam Updates](https://opt-ml.org/papers/2025/paper141.pdf) | — | — |
| [SMET](canon/math/smet.md) | ICML 2026 | [Memory-Efficient LLM Training with Dynamic Sparsity: From Stability to Practical Scaling](https://arxiv.org/abs/2606.00888) | [official](https://github.com/QiaoXiao7282/SMET) | — |
| [PowerStep](canon/math/powerstep.md) | arXiv 2026 | [PowerStep: Memory-Efficient Adaptive Optimization via ell_p-Norm Steepest Descent](https://arxiv.org/abs/2605.10335) | [official](https://github.com/yaolubrain/PowerStep) | — |
| [SRON](canon/math/sron.md) | OpenReview 2025 | [SRON: State-free LLM Training via Row-wise Gradient Normalization](https://openreview.net/forum?id=BtQLBWr6zI) | — | — |
| [GradLite](canon/math/gradlite.md) | arXiv 2025 | [Backward-Friendly Optimization: Training Large Language Models with Approximate Gradients under Memory Constraints](https://arxiv.org/abs/2510.22467) | — | — |
| [Optimal Low-Rank SGE](canon/math/optimallowranksge.md) | arXiv preprint 2026 | [Optimal low-rank stochastic gradient estimation for LLM training](https://arxiv.org/abs/2603.20632) | — | — |
| [Spectral Compact Training (SCT)](canon/math/spectralcompacttrainingsct.md) | arXiv 2026 | [Spectral Compact Training: Pre-Training Large Language Models via Permanent Truncated SVD and Stiefel QR Retraction](https://arxiv.org/abs/2604.00733) | [official](https://github.com/EctoSpace/SCT) | — |

#### Trainer integrations

HuggingFace `transformers` exposes many of these methods through the `optim` argument of `TrainingArguments`. Each string value below maps to a memory-efficient optimizer; all backing libraries except the built-in Adafactor must be installed separately.

| `optim` value | Backing library |
|---|---|
| [`adafactor`](canon/math/adafactor.md) | [transformers](https://github.com/huggingface/transformers) ships its own `Adafactor` implementation with relative-step and update-clipping options (Apache-2.0). |
| `adamw_bnb_8bit` / `adamw_8bit` | [bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes) AdamW with block-wise 8-bit quantized state (MIT). |
| `paged_adamw_8bit` / `paged_adamw_32bit` | [bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes) paged AdamW; optimizer state is paged between GPU and CPU memory (MIT). |
| `lion_8bit` / `lion_32bit` / `paged_lion_8bit` / `paged_lion_32bit` | [bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes) Lion, single momentum buffer, with 8-bit and paged variants (MIT). |
| `ademamix_8bit` / `paged_ademamix_8bit` / `paged_ademamix_32bit` | [bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes) AdEMAMix with 8-bit quantized and paged state (MIT). |
| `rmsprop_bnb_8bit` | [bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes) RMSprop with block-wise 8-bit quantized state (MIT). |
| `adamw_torch_4bit` / `adamw_torch_8bit` | [torchao](https://github.com/pytorch/ao) pure-PyTorch AdamW with 4-bit or 8-bit optimizer states (BSD-3-Clause). |
| `galore_adamw` / `galore_adamw_8bit` / `galore_adafactor` and `*_layerwise` variants | [galore-torch](https://github.com/jiaweizzhao/GaLore), the official GaLore release (Apache-2.0). |
| `apollo_adamw` / `apollo_adamw_layerwise` | [apollo-torch](https://github.com/zhuhanqing/APOLLO), the official APOLLO release (CC-BY-NC-4.0). |
| `lomo` / `adalomo` | [lomo-optim](https://github.com/OpenLMLab/LOMO), the official LOMO and AdaLomo release (MIT). |

### Fractional-Order Optimizers

Fractional-order optimizers generalize the integer-order gradient step with fractional-calculus operators, most commonly the Caputo, Riemann-Liouville, or Grünwald-Letnikov derivative, which weight past gradient information through power-law memory kernels. The field is young: the first neural-network training results date to 2015, convergence theory is still being settled, and most papers ship no code.

#### Foundations

| Optimizer | Venue | Paper | Code |
|---|---|---|---|
| [the Fractional Steepest Descent Method (FSDM)](canon/math/x243.md) | IEEE Transactions on Neural Networks and Learning Systems 2015 | [Fractional Extreme Value Adaptive Training Method: Fractional Steepest Descent Approach](https://doi.org/10.1109/TNNLS.2013.2286175) | — |
| [Caputo BP-NN FOGD (ISNN)](canon/math/caputobpnnfogdisnn.md) | Advances in Neural Networks - ISNN 2017 (Lecture Notes in Computer Science) | [A Caputo-Type Fractional-Order Gradient Descent Learning of BP Neural Networks](https://doi.org/10.1007/978-3-319-59072-1_64) | — |
| [Caputo CVNN FOGD](canon/math/caputocvnnfogd.md) | IEEE Access 2017 | [Convergence Analysis of Caputo-Type Fractional Order Complex-Valued Neural Networks](https://doi.org/10.1109/ACCESS.2017.2679185) | — |
| [Caputo fractional-order gradient descent](canon/math/x246.md) | Neural Networks 2017 | [Fractional-order gradient descent learning of BP neural networks with Caputo derivative](https://doi.org/10.1016/j.neunet.2017.02.007) | — |
| [FBPTT](canon/math/fbptt.md) | Circuits, Systems, and Signal Processing 2018 | [A Novel Fractional Gradient-Based Learning Algorithm for Recurrent Neural Networks](https://doi.org/10.1007/s00034-017-0572-z) | — |
| [FGD-RBF](canon/math/fgdrbf.md) | Circuits, Systems, and Signal Processing 2018 | [A Fractional Gradient Descent-Based RBF Neural Network](https://doi.org/10.1007/s00034-018-0835-3) | — |
| [Fractional-Order Deep BP NN](canon/math/fractionalorderdeepbpnn.md) | Computational Intelligence and Neuroscience 2018 | [Fractional-Order Deep Backpropagation Neural Network](https://doi.org/10.1155/2018/7361628) | [official](https://github.com/BaoChunhui/Deep-fractional-BP-neural-networks) |
| [Caputo-Type FOGD (Deep BP)](canon/math/caputotypefogddeepbp.md) | IEEE IMCEC 2019 | [A Caputo-Type Fractional-Order Gradient Descent Learning of Deep BP Neural Networks](https://doi.org/10.1109/IMCEC46724.2019.8984089) | — |
| [FSGD](canon/math/fsgd.md) | Electronic Markets 2019 | [Fractional stochastic gradient descent for recommender systems](https://doi.org/10.1007/s12525-018-0297-2) | — |
| [mF-SGD](canon/math/mfsgd.md) | IEEE Access 2019 | [Design of Momentum Fractional Stochastic Gradient Descent for Recommender Systems](https://doi.org/10.1109/ACCESS.2019.2954859) | — |
| [CFEM-LMS](canon/math/cfemlms.md) | Neurocomputing 2020 | [Combination of fractional FLANN filters for solving the Van der Pol-Duffing oscillator](https://doi.org/10.1016/j.neucom.2020.02.022) | — |
| [FSDM](canon/math/fsdm.md) | Frontiers of Information Technology & Electronic Engineering 2020 | [Fractional-order global optimal backpropagation machine trained by an improved fractional-order steepest descent method](https://doi.org/10.1631/FITEE.1900593) | — |
| [Fractional Order Gradient Method](canon/math/x255.md) | Neurocomputing 2020 | [Convolutional neural networks with fractional order gradient method](https://arxiv.org/abs/1905.05336) | — |
| [Normalized Fractional SGD (NFSGD)](canon/math/x256.md) | Neural Computing and Applications 2020 | [Design of normalized fractional SGD computing paradigm for recommender systems](https://doi.org/10.1007/s00521-019-04562-6) | — |
| [the Fractional Order Gradient Method](canon/math/x257.md) | Journal of the Franklin Institute 2020 | [Generalization of the gradient method with fractional order gradient direction](https://doi.org/10.1016/j.jfranklin.2020.01.008) | — |
| [Fractional Order Gradient Descent with Momentum (FOGDM)](canon/math/x258.md) | Network: Computation in Neural Systems 2020 | [Data classification based on fractional order gradient descent with momentum for RBF neural network](https://doi.org/10.1080/0954898X.2020.1849842) | — |
| [CFGD (Caputo)](canon/math/cfgdcaputo.md) | arXiv 2021 | [A Caputo fractional derivative-based algorithm for optimization](https://arxiv.org/abs/2104.02259) | — |
| [Fractional-Order Momentum (FCM)](canon/math/x260.md) | Neurocomputing 2021 | [Convolutional neural networks based on fractional-order momentum for parameter training](https://doi.org/10.1016/j.neucom.2021.03.075) | — |
| [FOGDM-RBF](canon/math/x261.md) | Soft Computing 2021 | [Fractional-order gradient descent with momentum for RBF neural network-based AIS trajectory restoration](https://doi.org/10.1007/s00500-020-05484-5) | — |
| [Caputron](canon/math/caputron.md) | Electronics (MDPI) 2022 | [Exploring the Effects of Caputo Fractional Derivative in Spiking Neural Network Training](https://doi.org/10.3390/electronics11142114) | [official](https://github.com/nata108/Caputron) |
| [FGD (CNN BP)](canon/math/fgdcnnbp.md) | arXiv 2022 | [Using a novel fractional-order gradient method for CNN back-propagation](https://arxiv.org/abs/2205.00581) | — |
| [FGNN](canon/math/fgnn.md) | Mathematics (MDPI) 2022 | [A Regularized Graph Neural Network Based on Approximate Fractional Order Gradients](https://doi.org/10.3390/math10081320) | — |
| [FracM](canon/math/fracm.md) | Neural Computing and Applications 2022 | [A fractional-order momentum optimization approach of deep neural networks](https://doi.org/10.1007/s00521-021-06765-2) | [community](https://github.com/TruongChien/FracM) |
| [GFSGD](canon/math/gfsgd.md) | Chaos, Solitons & Fractals 2022 | [Generalized fractional strategy for recommender systems with chaotic ratings behavior](https://doi.org/10.1016/j.chaos.2022.112204) | — |
| [Fractional Derivative Gradient Optimizers (FSGD](canon/math/x267.md) | Applied Sciences 2022 | [Fractional Derivative Gradient-Based Optimizers for Neural Networks and Human Activity Recognition](https://doi.org/10.3390/app12189264) | — |
| [Fractional LMS (FLMS)](canon/math/x268.md) | IEEE Transactions on Signal Processing 2022 | [Performance Analysis of Fractional Learning Algorithms](https://arxiv.org/abs/2110.05201) | — |
| [Conformable Fractional Gradient Descent](canon/math/x269.md) | Fuzzy Systems and Data Mining VIII 2022 | [Fractional Gradient Descent Learning of Backpropagation Artificial Neural Networks with Conformable Fractional Calculus](https://doi.org/10.3233/FAIA220372) | — |
| [Fractional Order Gradient Descent with variable initial value](canon/math/x270.md) | Neurocomputing 2022 | [Study on fast speed fractional order gradient descent method and its application in neural networks](https://doi.org/10.1016/j.neucom.2022.02.034) | — |
| [TFGD (Time-fractional)](canon/math/tfgdtimefractional.md) | Axioms 2022 | [Training Neural Networks by Time-Fractional Gradient Descent](https://doi.org/10.3390/axioms11100507) | — |
| [Variable Order Fractional Gradient Descent](canon/math/x272.md) | Chinese Control and Decision Conference 2022 | [Variable Order Fractional Gradient Descent Method and Its Application in Neural Networks Optimization](https://doi.org/10.1109/CCDC55256.2022.10033456) | — |
| [CfGD / CfAdam](canon/math/cfgdcfadam.md) | Neural Networks 2023 | [Accelerating gradient descent and Adam via fractional gradients](https://doi.org/10.1016/j.neunet.2023.01.002) | — |
| [RFGD](canon/math/rfgd.md) | Neural Networks 2023 | [A fractional gradient descent algorithm robust to the initial weights of multilayer perceptron](https://doi.org/10.1016/j.neunet.2022.11.018) | — |
| [FO-RI-FedAvg](canon/math/forifedavg.md) | arXiv 2026 | [Fractional Order Federated Learning for Battery Electric Vehicle Energy Consumption Modeling](https://arxiv.org/abs/2602.12567) | — | — |
| [IHL-Adam](canon/math/ihladam.md) | Expert Systems with Applications 2024 | [Parameter training method for convolutional neural networks based on improved Hausdorff-like derivative](https://doi.org/10.1016/j.eswa.2023.121659) | — | — |

#### Recent advances

| Optimizer | Venue | Paper | Code |
|---|---|---|---|
| [AFOGD / AFOAGD](canon/math/afogdafoagd.md) | arXiv 2023 | [The Novel Adaptive Fractional Order Gradient Decent Algorithms Design via Robust Control](https://arxiv.org/abs/2303.04328) | — |
| [EFSGD / EN-EFSGD](canon/math/efsgdenefsgd.md) | Chaos, Solitons & Fractals 2023 | [Enhanced fractional prediction scheme for effective matrix factorization in chaotic feedback recommender systems](https://doi.org/10.1016/j.chaos.2023.114109) | — |
| [FCGD_G-L](canon/math/fcgdgl.md) | Mathematics 2023 | [A Deep Learning Optimizer Based on Grünwald–Letnikov Fractional Order Definition](https://doi.org/10.3390/math11020316) | — |
| [FGDAM](canon/math/fgdam.md) | Applied Mathematics and Computation 2023 | [Applications of fractional gradient descent method with adaptive momentum in BP neural networks](https://doi.org/10.1016/j.amc.2023.127944) | — |
| [FracG](canon/math/fracg.md) | Chinese Control Conference (CCC) 2023 | [Optimization Method of Neural Networks via Fractional-Order of Gradients](https://doi.org/10.23919/CCC58697.2023.10239893) | — |
| [Fractional Gradient Descent (FSGD)](canon/math/x282.md) | Fractal and Fractional 2023 | [Fractional Gradient Optimizers for PyTorch: Enhancing GAN and BERT](https://doi.org/10.3390/fractalfract7070500) | — |
| [the Improved Stochastic Fractional Order Gradient Descent algorithm](canon/math/x283.md) | Fractal and Fractional 2023 | [The Improved Stochastic Fractional Order Gradient Descent Algorithm](https://doi.org/10.3390/fractalfract7080631) | — |
| [AdaGL](canon/math/adagl.md) | Neural Processing Letters 2024 | [An Adaptive Learning Rate Deep Learning Optimizer Using Long and Short-Term Gradients Based on G–L Fractional-Order Derivative](https://doi.org/10.1007/s11063-024-11571-7) | [community](https://github.com/daddydrac/AdaGL) |
| [GFSGD](canon/math/gfsgd2.md) | Heliyon 2024 | [Fractional gradient optimized explainable convolutional neural network for Alzheimer's disease diagnosis](https://doi.org/10.1016/j.heliyon.2024.e39037) | — |
| [FOAdam](canon/math/x286.md) | Applied Mathematical Modelling 2024 | [A novel gradient descent optimizer based on fractional order scheduler and its application in deep neural networks](https://doi.org/10.1016/j.apm.2023.12.018) | — |
| [Adaptive Terminal Caputo Fractional Gradient Descent (AT-CFGD)](canon/math/x287.md) | TMLR 2024 | [Convergence Analysis of Fractional Gradient Descent](https://arxiv.org/abs/2311.18426) | — |
| [Caputo Fractional-Order Gradient Descent](canon/math/x288.md) | International Journal of Fuzzy Systems 2024 | [A Novel Neuro-fuzzy Learning Algorithm for First-Order Takagi–Sugeno Fuzzy Model: Caputo Fractional-Order Gradient Descent Method](https://doi.org/10.1007/s40815-024-01750-y) | — |
| [FNGD](canon/math/fngd.md) | IEEE Access 2024 | [Improving the Accuracy of Neural Network Pattern Recognition by Fractional Gradient Descent](https://doi.org/10.1109/ACCESS.2024.3491614) | — |
| [MFFGD](canon/math/mffgd.md) | Neurocomputing 2024 | [MFFGD: An adaptive Caputo fractional-order gradient algorithm for DNN](https://doi.org/10.1016/j.neucom.2024.128606) | — |
| [Caputo-based SGD (L1 scheme)](canon/math/caputobasedsgdl1scheme.md) | OpenReview 2024 | [Stochastic Fractional Gradient Descent with Caputo L1 Scheme for Deep Neural Networks](https://openreview.net/forum?id=hCGaySEW9q) | — |
| [C-FOG](canon/math/cfog.md) | Fractal and Fractional 2024 | [Self-Organizing Optimization Based on Caputo's Fractional Order Gradients](https://doi.org/10.3390/fractalfract8080451) | — |
| [CSA-CFGD](canon/math/csacfgd.md) | PeerJ Computer Science 2024 | [Deep ocular tumor classification model using cuckoo search algorithm and Caputo fractional gradient descent](https://doi.org/10.7717/peerj-cs.1923) | [official](https://doi.org/10.7717/peerj-cs.1923/supp-1) |
| [FGD-RBFNN (UAV)](canon/math/fgdrbfnnuav.md) | Computer Modeling in Engineering & Sciences 2024 | [Fractional Gradient Descent RBFNN for Active Fault-Tolerant Control of Plant Protection UAVs](https://doi.org/10.32604/cmes.2023.030535) | — |
| [FOELM](canon/math/foelm.md) | Applied Soft Computing 2024 | [An interval neural network-based Caputo fractional-order extreme learning machine applied to classification](https://doi.org/10.1016/j.asoc.2024.112310) | — |
| [MIF](canon/math/mif.md) | Algorithms 2024 | [An Integer-Fractional Gradient Algorithm for Back Propagation Neural Networks](https://doi.org/10.3390/a17050220) | — |
| [Multi-layer NN FOGD](canon/math/multilayernnfogd.md) | Advanced Theory and Simulations 2024 | [Convergence Analysis and Application for Multi-Layer Neural Network Based on Fractional-Order Gradient Descent Learning](https://doi.org/10.1002/adts.202300662) | — |
| [UCAdam](canon/math/ucadam.md) | Journal of Electrical Systems 2024 | [Improved Adam: Incorporating Unified Conformable Fractional Derivative for fractional-order Momentum](https://journal.esrgroups.org/jes/article/view/5687) | — |
| [2SEDFOSGD](canon/math/2sedfosgd.md) | arXiv 2025 | [Effective Dimension Aware Fractional-Order Stochastic Gradient Descent for Convex Optimization Problems](https://arxiv.org/abs/2503.13764) | — |
| [2SEDFOSGD](canon/math/2sedfosgd2.md) | arXiv 2025 | [More Optimal Fractional-Order Stochastic Gradient Descent for Non-Convex Optimization Problems](https://arxiv.org/abs/2505.02985) | — |
| [AFGD (adaptive Caputo FGD for TCN)](canon/math/afgdadaptivecaputofgdfortcn.md) | Neurocomputing 2025 | [Monotonic convergence of adaptive Caputo fractional gradient descent for temporal convolutional networks](https://doi.org/10.1016/j.neucom.2025.131491) | — |
| [FGDSINN](canon/math/fgdsinn.md) | International Journal of Machine Learning and Cybernetics 2025 | [A smoothing interval neural networks-based Caputo fractional-order gradient learning algorithm](https://doi.org/10.1007/s13042-024-02402-1) | — |
| [FOSGD / FOSGDM / FOSGDME](canon/math/fosgdfosgdmfosgdme.md) | Neural Networks 2025 | [Fractional-order stochastic gradient descent method with momentum and energy for deep neural networks](https://doi.org/10.1016/j.neunet.2024.106810) | — |
| [FracGrad](canon/math/fracgrad.md) | Fractal and Fractional 2025 | [FracGrad: A Discretized Riemann–Liouville Fractional Integral Approach to Gradient Accumulation for Deep Learning](https://doi.org/10.3390/fractalfract9110733) | — |
| [GF-SGD](canon/math/gfsgd3.md) | Computers in Biology and Medicine 2025 | [Generalized fractional optimization-based explainable lightweight CNN model for malaria disease classification](https://doi.org/10.1016/j.compbiomed.2024.109593) | — |
| [IFOGD](canon/math/ifogd.md) | Neural Networks 2025 | [Improved fractional-order gradient descent method based on multilayer perceptron](https://doi.org/10.1016/j.neunet.2024.106970) | — |
| [L2O-CFGD](canon/math/l2ocfgd.md) | arXiv 2025 | [Enhancing Fractional Gradient Descent with Learned Optimizers](https://arxiv.org/abs/2510.18783) | [official](https://github.com/Johnny1188/fractional-learning-to-optimize) |
| [MOAOCFGD](canon/math/moaocfgd.md) | arXiv 2025 | [An Adaptive Order Caputo Fractional Gradient Descent Method for Multi-objective Optimization Problems](https://arxiv.org/abs/2507.07674) | — |
| [NCFDD / NFLightGBM](canon/math/ncfddnflightgbm.md) | Information Fusion 2025 | [Fractional light gradient boosting machine ensemble learning model: A non-causal fractional difference descent approach](https://doi.org/10.1016/j.inffus.2025.102947) | — |
| [a Caputo fractional-order gradient descent for neural network training](canon/math/x310.md) | Chaos, Solitons & Fractals 2025 | [Fractional-order gradient approach for optimizing neural networks: A theoretical and empirical analysis](https://doi.org/10.1016/j.chaos.2025.116009) | — |
| [Fractional-order SGD (FSGD)](canon/math/x311.md) | arXiv 2025 | [Fractional-order Jacobian Matrix Differentiation and Its Application in Artificial Neural Networks](https://arxiv.org/abs/2506.07408) | — |
| [Adaptive Parameter Fractional-Order Gradient Descent Learning](canon/math/x312.md) | European Journal of Operational Research 2025 | [Novel adaptive parameter fractional-order gradient descent learning for stock selection decision support systems](https://doi.org/10.1016/j.ejor.2025.01.013) | — |
| [FAdam](canon/math/x313.md) | Chaos, Solitons & Fractals 2025 | [Parameter training methods for convolutional neural networks with adaptive adjustment method based on Caputo fractional-order differences](https://doi.org/10.1016/j.chaos.2025.116588) | — |
| [SFM](canon/math/sfm.md) | Digital Signal Processing 2025 | [A momentum-based stochastic fractional gradient optimizer with U-net model for brain tumor segmentation in MRI](https://doi.org/10.1016/j.dsp.2025.104983) | — |
| [Caputo Fractional-order Gradient Descent for Ridge Polynomial Neural](canon/math/x315.md) | International Conference on Electronics and Communication, Network and Computer Technology 2025 | [A Novel Method for Ridge Polynomial Neural Network-based Caputo Fractional-order Gradient Descent Algorithm](https://doi.org/10.1109/ECNCT66493.2025.11172593) | — |
| [AOFGD](canon/math/aofgd.md) | SSRN 2025 | [AOFGD: Adaptive order fractional gradient descent method](https://doi.org/10.2139/ssrn.5717167) | — |
| [Frac-Adam](canon/math/x317.md) | Mathematics 2025 | [Fractional Optimizers for LSTM Networks in Financial Time Series Forecasting](https://doi.org/10.3390/math13132068) | — |
| [Caputo Fractional Gradient Descent](canon/math/x318.md) | International Conference on Advanced Algorithms and Control Engineering 2025 | [Fractional Order Gradient Descent with Caputo Derivatives for Product-Unit Neural Networks](https://doi.org/10.1109/ICAACE65325.2025.11020545) | — |
| [FO-STDGD](canon/math/fostdgd.md) | Neurocomputing 2025 | [Fractional-order spike-timing-dependent gradient descent for multi-layer spiking neural networks](https://doi.org/10.1016/j.neucom.2024.128662) | — |
| [Fractional Order Stochastic Gradient Descent (FOSGD)](canon/math/x320.md) | ASME IDETC-CIE 2025 | [Tail-Index-Awareness in Fractional Order Stochastic Gradient Descent](https://doi.org/10.1115/DETC2025-169054) | — |
| [λ-FAdaMax](canon/math/fadamax.md) | Expert Systems with Applications 2025 | [λ-FAdaMax: A novel fractional-order gradient descent method with decaying second moment for neural network training](https://doi.org/10.1016/j.eswa.2025.127156) | — |
| [CFDNN](canon/math/cfdnn.md) | Scientific Reports 2026 | [Conformable Fractional Deep Neural Networks (CFDNN) for high-speed cyber-attack detection](https://doi.org/10.1038/s41598-026-45213-w) | — |
| [CFGD (Compressed)](canon/math/cfgdcompressed.md) | IEEE Transactions on Neural Networks and Learning Systems 2026 | [Fractional Gradient Descent With Matrix Stepsizes for Non-Convex Optimization](https://doi.org/10.1109/TNNLS.2025.3637535) | [official](https://github.com/alokendumazumder/IEEE_TNNLS_Compressed_fractional_GD) |
| [FAdamWav](canon/math/fadamwav.md) | Fractal and Fractional 2026 | [FAdamWav: A Fractional Wavelet Gradient Optimizer for Neural Networks](https://doi.org/10.3390/fractalfract10030149) | — |
| [FOFedAvg](canon/math/fofedavg.md) | arXiv 2026 | [Fractional-Order Federated Learning](https://arxiv.org/abs/2602.15380) | — |
| [Fractional-order FL with adaptive momentum](canon/math/fractionalorderflwithadaptivemomentum.md) | IEEE Transactions on Emerging Topics in Computational Intelligence 2026 | [Communication-Efficient Federated Learning via Fractional-Order Gradient Descent With Adaptive Momentum Under Non-IID Data](https://doi.org/10.1109/TETCI.2026.3692489) | — |
| [TFGD (Tempered)](canon/math/tfgdtempered.md) | Neural Networks 2026 | [Tempered fractional gradient descent: Theory, algorithms, and robust learning applications](https://doi.org/10.1016/j.neunet.2025.108005) | — |
| [FGD-ED](canon/math/x328.md) | Information Processing & Management 2026 | [Fractional-order gradient descent method based on fractional-order term exponential decay and its application in artificial neural networks](https://doi.org/10.1016/j.ipm.2025.104448) | — |
| [the Caputo Fractional-Order Gradient Descent Method (FGDM)](canon/math/x329.md) | Applied Soft Computing 2026 | [A novel gradient learning algorithm based on zero-order Takagi-Sugeno fuzzy model: the caputo fractional-order gradient descent](https://doi.org/10.1016/j.asoc.2025.114430) | — |
| [CFGD (Conformable)](canon/math/cfgdconformable.md) | Journal of Computational and Applied Mathematics 2026 | [Conformable fractional gradient descent: A local optimizer for neural network training](https://doi.org/10.1016/j.cam.2026.117842) | — |
| [NGLFGD](canon/math/x331.md) | Knowledge-Based Systems 2026 | [Fast and accurate fractional order gradient descent algorithm and its application in Extreme Gradient Boosting](https://doi.org/10.1016/j.knosys.2025.114911) | — |
| [FO-Elman](canon/math/x332.md) | Neural Networks 2026 | [Fractional-order gradient descent learning for Elman neural networks](https://doi.org/10.1016/j.neunet.2026.108880) | — |

#### Surveys

| Optimizer | Venue | Paper | Code |
|---|---|---|---|
| [Fractional-Order Gradient Descent for Neural Networks](canon/math/x333.md) | The European Physical Journal Special Topics 2022 | [Artificial neural networks: a practical review of applications involving fractional calculus](https://doi.org/10.1140/epjs/s11734-022-00455-3) | — |
| [Fractional Gradient Descent (FGD)](canon/math/x334.md) | Chaos, Solitons & Fractals 2025 | [A comprehensive survey of fractional gradient descent methods and their convergence analysis](https://doi.org/10.1016/j.chaos.2025.116154) | — |
| [the Fractional Continuous Time Method (FCTM)](canon/math/x335.md) | Journal of Computational and Applied Mathematics 2026 | [An overview of the fractional-order gradient descent method and its applications](https://arxiv.org/abs/2601.03318) | — |

Note: FAdam ([arXiv 2405.12807](https://arxiv.org/abs/2405.12807)) is a Fisher-information variant of Adam and is unrelated to fractional calculus despite the name.

### Distributed and Communication-Efficient Optimizers

Optimizers in this category target training across many devices or nodes, where memory and inter-worker communication are the main bottlenecks. They shard optimizer state, compress gradient exchange, or synchronize infrequently so that training scales without a proportional increase in bandwidth. Some entries are standalone update rules, while others wrap an inner optimizer with a communication-efficient outer loop.

| Optimizer | Venue | Paper | Code | `zij` |
|---|---|---|---|---|
| [signSGD](canon/math/signsgd-v.md) | ICML 2018 | [signSGD: Compressed Optimisation for Non-Convex Problems](https://arxiv.org/abs/1802.04434) | [official](https://github.com/jxbz/signSGD) | — |
| [LD-SGD](canon/math/ldsgd.md) | arXiv 2019 | [Communication-Efficient Local Decentralized SGD Methods](https://arxiv.org/abs/1910.09126) | — | — |
| [Local SGD](canon/math/localsgd.md) | ICLR 2019 | [Local SGD Converges Fast and Communicates Little](https://arxiv.org/abs/1805.09767) | [community](https://github.com/epfml/LocalSGD-Code) | — |
| [PowerSGD](canon/math/powersgd.md) | NeurIPS 2019 | [PowerSGD: Practical Low-Rank Gradient Compression for Distributed Optimization](https://arxiv.org/abs/1905.13727) | — | — |
| [Qsparse-local-SGD](canon/math/qsparselocalsgd.md) | NeurIPS 2019 | [Qsparse-local-SGD: Distributed SGD with Quantization, Sparsification, and Local Computations](https://arxiv.org/abs/1906.02367) | — | — |
| [signProx](canon/math/signprox.md) | ICASSP 2019 | [signProx: One-Bit Proximal Algorithm for Nonconvex Stochastic Optimization](https://arxiv.org/abs/1807.08023) | — | — |
| [APMSqueeze](canon/math/apmsqueeze.md) | arXiv 2020 | [APMSqueeze: A Communication Efficient Adam-Preconditioned Momentum SGD Algorithm](https://arxiv.org/abs/2008.11343) | — | — |
| [DEED-GD](canon/math/deedgd.md) | arXiv 2020 | [DEED: A General Quantization Scheme for Communication Efficiency in Bits](https://arxiv.org/abs/2006.11401) | — | — |
| [FedAC](canon/math/fedac.md) | NeurIPS 2020 | [Federated Accelerated Stochastic Gradient Descent](https://arxiv.org/abs/2006.08950) | — | — |
| [LAGS-SGD](canon/math/lagssgd.md) | ECAI 2020 | [Layer-wise Adaptive Gradient Sparsification for Distributed Deep Learning with Convergence Guarantees](https://arxiv.org/abs/1911.08727) | — | — |
| [rTop-k](canon/math/rtopk.md) | JSAIT 2020 | [rTop-k: A Statistical Estimation Approach to Distributed SGD](https://arxiv.org/abs/2005.10761) | — | — |
| [SCAFFOLD](canon/math/scaffold.md) | ICML 2020 | [SCAFFOLD: Stochastic Controlled Averaging for Federated Learning](https://arxiv.org/abs/1910.06378) | — | — |
| [SlowMo](canon/math/slowmo.md) | ICLR 2020 | [SlowMo: Improving Communication-Efficient Distributed SGD with Slow Momentum](https://arxiv.org/abs/1910.00643) | — | — |
| [ZeRO](canon/math/zero.md) | SC 2020 | [ZeRO: Memory Optimizations Toward Training Trillion Parameter Models](https://arxiv.org/abs/1910.02054) | [official](https://github.com/deepspeedai/DeepSpeed) | — |
| [1-bit Adam](canon/math/1bitadam.md) | ICML 2021 | [1-bit Adam: Communication Efficient Large-Scale Training with Adam's Convergence Speed](https://arxiv.org/abs/2102.02888) | [official](https://github.com/deepspeedai/DeepSpeed) | — |
| [BVR-L-SGD](canon/math/bvrlsgd.md) | ICML 2021 | [Bias-Variance Reduced Local SGD for Less Heterogeneous Federated Learning](https://arxiv.org/abs/2102.03198) | — | — |
| [SQuARM-SGD](canon/math/squarmsgd.md) | JSAIT 2021 | [SQuARM-SGD: Communication-Efficient Momentum SGD for Decentralized Optimization](https://arxiv.org/abs/2005.07041) | — | — |
| [SketchedAMSGrad](canon/math/sketchedamsgrad.md) | ICDM 2022 | [Communication-Efficient Adam-Type Algorithms for Distributed Data Mining](https://arxiv.org/abs/2210.07454) | — | — |
| [0/1 Adam](canon/math/01adam.md) | ICLR 2023 | [Maximizing Communication Efficiency for Large-scale Training via 0/1 Adam](https://arxiv.org/abs/2202.06009) | [official](https://github.com/deepspeedai/DeepSpeed) | — |
| [AdaCGD](canon/math/adacgd.md) | TMLR 2023 | [Adaptive Compression for Communication-Efficient Distributed Training](https://arxiv.org/abs/2211.00188) | — | — |
| [DiLoCo](canon/math/diloco.md) | arXiv 2023 | [DiLoCo: Distributed Low-Communication Training of Language Models](https://arxiv.org/abs/2311.08105) | [community](https://github.com/PrimeIntellect-ai/OpenDiloco) | — |
| [Distributed Shampoo](canon/math/distributedshampoo.md) | arXiv 2023 | [A Distributed Data-Parallel PyTorch Implementation of the Distributed Shampoo Optimizer for Training Neural Networks At-Scale](https://arxiv.org/abs/2309.06497) | [official](https://github.com/facebookresearch/optimizers) | — |
| [SPARQ-SGD](canon/math/sparqsgd.md) | TAC 2023 | [SPARQ-SGD: Event-Triggered and Compressed Communication in Decentralized Stochastic Optimization](https://arxiv.org/abs/1910.14280) | — | — |
| [AdaFedAdam](canon/math/adafedadam.md) | TMLCN 2024 | [Accelerating Fair Federated Learning: Adaptive Federated Adam](https://arxiv.org/abs/2301.09357) | [official](https://github.com/li-ju666/adafedadam) | — |
| [DeMo](canon/math/demo.md) | arXiv 2024 | [DeMo: Decoupled Momentum Optimization](https://arxiv.org/abs/2411.19870) | [official](https://github.com/bloc97/DeMo) | — |
| [FADAS](canon/math/fadas.md) | ICML 2024 | [FADAS: Towards Federated Adaptive Asynchronous Optimization](https://arxiv.org/abs/2407.18365) | [official](https://github.com/yujiaw98/FADAS) | — |
| [FAGH](canon/math/fagh.md) | arXiv 2024 | [FAGH: Accelerating Federated Learning with Approximated Global Hessian](https://arxiv.org/abs/2403.11041) | — | — |
| [Fed-Sophia](canon/math/fedsophia.md) | ICC 2024 | [Fed-Sophia: A Communication-Efficient Second-Order Federated Learning Algorithm](https://arxiv.org/abs/2406.06655) | — | — |
| [FedLion](canon/math/fedlion.md) | ICASSP 2024 | [FedLion: Faster Adaptive Federated Optimization with Fewer Communication](https://arxiv.org/abs/2402.09941) | [official](https://github.com/TZW1998/FedLion) | — |
| [FedRepOpt](canon/math/fedrepopt.md) | ACCV 2024 | [FedRepOpt: Gradient Re-parametrized Optimizers in Federated Learning](https://arxiv.org/abs/2409.15898) | [official](https://github.com/StevenLauHKHK/FedRepOpt) | — |
| [FedSTaS](canon/math/fedstas.md) | arXiv 2024 | [FedSTaS: Client Stratification and Client Level Sampling for Efficient Federated Learning](https://arxiv.org/abs/2412.14226) | [official](https://github.com/askjdasf/FedSTaS) | — |
| [FESS-GDA](canon/math/fessgda.md) | AISTATS 2024 | [Stochastic Smoothed Gradient Descent Ascent for Federated Minimax Optimization](https://arxiv.org/abs/2311.00944) | — | — |
| [FLeNS](canon/math/flens.md) | BigData 2024 | [FLeNS: Federated Learning with Enhanced Nesterov-Newton Sketch](https://arxiv.org/abs/2409.15216) | [official](https://github.com/sunnyinAI/FLeNS) | — |
| [MM-PSGD / MC-PSGD](canon/math/mmpsgdmcpsgd.md) | MMAsia-W 2024 | [Distributed Optimization over Block-Cyclic Data](https://arxiv.org/abs/2002.07454) | — | — |
| [OpenDiLoCo](canon/math/opendiloco.md) | arXiv 2024 | [OpenDiLoCo: An Open-Source Framework for Globally Distributed Low-Communication Training](https://arxiv.org/abs/2407.07852) | [official](https://github.com/PrimeIntellect-ai/OpenDiloco) | — |
| [ADEF](canon/math/adef.md) | arXiv 2025 | [Accelerated Distributed Optimization with Compression and Error Feedback](https://arxiv.org/abs/2503.08427) | — | — |
| [DAT-SGD](canon/math/datsgd.md) | ICML 2025 | [Enhancing Parallelism in Decentralized Stochastic Convex Optimization](https://arxiv.org/abs/2506.00961) | — | — |
| [DeCo-SGD](canon/math/decosgd.md) | arXiv 2025 | [Taming Latency and Bandwidth: A Theoretical Framework and Adaptive Algorithm for Communication-Constrained Training](https://arxiv.org/abs/2507.17346) | — | — |
| [DES-LOC](canon/math/desloc.md) | arXiv 2025 | [DES-LOC: Desynced Low Communication Adaptive Optimizers for Training Foundation Models](https://arxiv.org/abs/2505.22549) | — | — |
| [Dion](canon/math/dion.md) | arXiv 2025 | [Dion: Distributed Orthonormalized Updates](https://arxiv.org/abs/2504.05295) | [official](https://github.com/microsoft/dion) | — |
| [DLAS-R-FTC](canon/math/dlasrftc.md) | CDC 2025 | [Distributed Optimization and Learning for Automated Stepsize Selection with Finite Time Coordination](https://arxiv.org/abs/2508.05887) | — | — |
| [FAdamGC](canon/math/fadamgc.md) | arXiv 2025 | [Gradient Correction in Federated Learning with Adaptive Optimization](https://arxiv.org/abs/2502.02727) | — | — |
| [FedCET](canon/math/fedcet.md) | arXiv 2025 | [Communication Efficient Federated Learning with Linear Convergence on Heterogeneous Data](https://arxiv.org/abs/2503.15804) | — | — |
| [FedIvon](canon/math/fedivon.md) | TMLR 2025 | [Federated Learning with Uncertainty and Personalization via Efficient Second-order Optimization](https://arxiv.org/abs/2411.18385) | — | — |
| [FedMuon](canon/math/fedmuon.md) | arXiv 2025 | [FedMuon: Accelerating Federated Learning with Matrix Orthogonalization](https://arxiv.org/abs/2510.27403) | [official](https://github.com/junkangLiu0/FedMuon) | — |
| [FedOne](canon/math/fedone.md) | ICML 2025 | [FedOne: Query-Efficient Federated Learning for Black-box Discrete Prompt Learning](https://arxiv.org/abs/2506.14929) | — | — |
| [HybridSGD](canon/math/hybridsgd.md) | arXiv 2025 | [Communication-Efficient, 2D Parallel Stochastic Gradient Descent for Distributed-Memory Optimization](https://arxiv.org/abs/2501.07526) | — | — |
| [Kuramoto-FedAvg](canon/math/kuramotofedavg.md) | arXiv 2025 | [Kuramoto-FedAvg: Using Synchronization Dynamics to Improve Federated Learning Optimization under Statistical Heterogeneity](https://arxiv.org/abs/2505.19605) | [official](https://github.com/amuhebwa/Kuramoto-FedAvg) | — |
| [LQ-SGD](canon/math/lqsgd.md) | arXiv 2025 | [Trustworthy Efficient 