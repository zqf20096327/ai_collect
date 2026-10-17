# Awesome Tensorial Neural Networks [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)


Tensorial neural networks (TNNs) combine tensor-network structure with
trainable neural components. This list follows the revised survey taxonomy
and covers:

- Data processing: multi-source fusion, multimodal pooling, tensor
  compression, multi-task learning, and quantum data.
- Model architectures: CNNs, RNNs, Transformers, GNNs, LLMs/MoE, and
  quantum neural networks/circuits.
- Model lifecycle: stable training, rank and structure search,
  parameter-efficient adaptation, and hardware acceleration.
- Software: basic tensor operations, deep-model implementation, and quantum simulation.
- Analysis and synthesis: interpretability, topology and contraction,
  inductive bias, and scientific machine learning.

The list prioritizes peer-reviewed publications. Entries that are only
available as preprints are explicitly marked.

## Contents

- [Survey and citation](#survey-and-citation)
- [Recent 2025-2026 highlights](#recent-2025-2026-highlights)
- [Data processing with TNNs](#data-processing-with-tnns)
- [TNN model architectures](#tnn-model-architectures)
- [Training and model lifecycle](#training-and-model-lifecycle)
- [Toolboxes](#toolboxes)
- [Interpretability and analysis](#interpretability-and-analysis)
- [Cross-cutting insights](#cross-cutting-insights)
- [Related surveys](#related-surveys)

## Survey and Citation

This repository is maintained alongside the substantially revised version of:

**Tensor Networks Meet Neural Networks: A Survey and Future Perspectives**  
[arXiv:2302.09019](https://arxiv.org/abs/2302.09019)

Until a final journal record is available, please cite the current manuscript as:

```bibtex
@article{wang2026tensor_networks_meet_neural_networks,
  author  = {Maolin Wang and Yu Pan and Zenglin Xu and Guangxi Li and
             Xiangli Yang and Danilo Mandic and Andrzej Cichocki},
  title   = {Tensor Networks Meet Neural Networks: A Survey and Future Perspectives},
  journal = {arXiv preprint arXiv:2302.09019},
  year    = {2026},
  note    = {Substantially revised version}
}
```

## Recent 2025-2026 Highlights

These papers are integrated into the relevant sections below rather than
treated as isolated one-paper categories.

| Paper | Main role | Venue | Year |
| --- | --- | --- | --- |
| Klein et al., ["Tucker Attention: A Generalization of Approximate Attention Mechanisms"](https://icml.cc/virtual/2026/poster/65314) | Tucker-structured approximate attention | ICML | 2026 |
| Xie et al., ["Self-Supervised Weight Templates for Scalable Vision Model Initialization"](https://icml.cc/virtual/2026/poster/63459) | Reusable Tucker weight templates across model scales | ICML | 2026 |
| Maolin et al., ["T-GINEE: A Tensor-Based Multi-Graph Representation Learning"](https://icml.cc/virtual/2026/poster/62311) | Tensor-based multi-graph representation learning | ICML | 2026 |
| Pham et al., ["Coupled Tensor Decomposition for Compact Network Representation"](https://doi.org/10.1109/TNNLS.2025.3609797) | Joint low-rank structure across network parameter tensors | IEEE TNNLS | 2026 |
| Ye et al., ["TRAC: Tensor-Train Based Across-Layer Compression for Parameter-Efficient Fine-Tuning"](https://iclr.cc/virtual/2026/poster/10006929) | Across-layer TT parameter-efficient fine-tuning | ICLR | 2026 |
| Xu et al., ["TD-MoE: Tensor Decomposition for MoE Models"](https://iclr.cc/virtual/2026/poster/10010804) | Joint tensor decomposition for mixture-of-experts models | ICLR | 2026 |
| Loconte et al., ["What Is the Relationship Between Tensor Factorizations and Circuits (and How Can We Exploit It)?"](https://iclr.cc/virtual/2026/poster/10014069) | Unified view of tensor factorizations and tractable circuits | ICLR | 2026 |
| Zhou et al., ["Tucker-FNO: Tensor Tucker-Fourier Neural Operator and Its Universal Approximation Theory"](https://iclr.cc/virtual/2026/poster/10009240) | Tucker-compressed Fourier neural operators | ICLR | 2026 |
| Li et al., ["LeSTD: LLM Compression via Learning-Based Sparse Tensor Decomposition"](https://iclr.cc/virtual/2026/poster/10011895) | Sparse tensor decomposition for LLM compression | ICLR | 2026 |
| Xu et al., ["LEGO: An LLM-Enabled Hierarchical Optimizer for Tensor Computation Graphs"](https://icml.cc/virtual/2026/poster/62027) | Structure-aware tensor computation and GPU kernel optimization | ICML | 2026 |
| Xu et al., ["TIME: Tensor-Factorized Mixture-of-Experts with Intrinsic Routing"](https://icml.cc/virtual/2026/poster/64179) | Tensor-factorized MoE for lifelong multimodal knowledge editing | ICML | 2026 |
| Heidari and Rabusseau, ["TN-SHAP-G: Graph-Structured Tensor Network Surrogates for Shapley Values and Interactions"](https://icml.cc/virtual/2026/poster/64574) | Deterministic Shapley interaction recovery from TN surrogates | ICML | 2026 |
| Zeng et al., ["MTNL: A Unified Modeling Perspective for Enhancing Tensor Network Learning"](https://icml.cc/virtual/2026/poster/62604) | Unified supervised and unsupervised TN learning | ICML | 2026 |
| Yang et al., ["Kronecker Generative Networks"](https://icml.cc/virtual/2026/poster/61891) | Parameter-efficient architecture generation through Kronecker structure | ICML | 2026 |
| Zheng et al., ["ReFTA: Breaking the Weight Reconstruction Bottleneck in Tensorized Parameter-Efficient Fine-Tuning"](https://cvpr.thecvf.com/virtual/2026/poster/38595) | Reconstruction-free tensorized PEFT | CVPR | 2026 |
| Zhang et al., ["Tensor Product Attention Is All You Need"](https://proceedings.neurips.cc/paper_files/paper/2025/hash/a301ec7cb9e07dc050403e2eb11d0041-Abstract-Conference.html) | Tensor-product attention for efficient sequence modeling | NeurIPS | 2025 |

## Data Processing with TNNs

### Multi-Source Fusion and Multimodal Pooling

| Paper | Contribution | Venue | Year |
| --- | --- | --- | --- |
| Varshneya et al., ["Interpretable Tensor Fusion"](https://www.ijcai.org/proceedings/2024/0557.pdf) | Interpretable high-order interaction modeling for multimodal fusion | IJCAI | 2024 |
| Hou et al., ["Deep Multimodal Multilinear Fusion with High-Order Polynomial Pooling"](https://proceedings.neurips.cc/paper/2019/hash/f56d8183992b6c54c92c16a8519a6e2b-Abstract.html) | Polynomial tensor pooling for high-order multimodal interactions | NeurIPS | 2019 |
| Do et al., ["Compact Trilinear Interaction for Visual Question Answering"](https://openaccess.thecvf.com/content_ICCV_2019/html/Do_Compact_Trilinear_Interaction_for_Visual_Question_Answering_ICCV_2019_paper.html) | Compact trilinear interaction via structured tensor factorization | ICCV | 2019 |
| Liu et al., ["Efficient Low-Rank Multimodal Fusion with Modality-Specific Factors"](https://aclanthology.org/P18-1209/) | Low-rank multimodal fusion without materializing the full interaction tensor | ACL | 2018 |
| Ben-Younes et al., ["MUTAN: Multimodal Tucker Fusion for Visual Question Answering"](https://openaccess.thecvf.com/content_ICCV_2017/html/Ben-younes_MUTAN_Multimodal_Tucker_ICCV_2017_paper.html) | Tucker-factorized bilinear interactions | ICCV | 2017 |
| Zadeh et al., ["Tensor Fusion Network for Multimodal Sentiment Analysis"](https://aclanthology.org/D17-1115/) | Explicit intra- and inter-modality tensor interactions | EMNLP | 2017 |
| Fukui et al., ["Multimodal Compact Bilinear Pooling"](https://arxiv.org/abs/1606.01847) | Compact bilinear pooling for vision-language tasks | EMNLP | 2016 |

### Tensor Data Compression and Multi-Task Learning

| Paper | Contribution | Venue | Year |
| --- | --- | --- | --- |
| Kwon et al., ["TensorCodec: Compact Lossy Compression of Tensors without Strong Data Assumptions"](https://doi.org/10.1109/ICDM58522.2023.00032) | Compact lossy tensor compression | ICDM | 2023 |
| Kwon et al., ["NeuKron: Constant-Size Lossy Compression of Sparse Reorderable Matrices and Tensors"](https://doi.org/10.1145/3543507.3583226) | Constant-size neural compression for reorderable sparse data | The Web Conference | 2023 |
| Zhang et al., ["Generalized Tensor Decomposition for Multi-Task Learning"](https://proceedings.mlr.press/v139/zhang21e.html) | Tensor-network sharing across multiple tasks | ICML | 2021 |
| Wang et al., ["Concatenated Tensor Networks for Deep Multi-Task Learning"](https://link.springer.com/chapter/10.1007/978-3-030-63823-8_59) | PEPS-like tensor-network structure for multi-task models | ICONIP | 2020 |
| Ballester-Ripoll et al., ["TTHRESH: Tensor Compression for Multidimensional Visual Data"](https://doi.org/10.1109/TVCG.2019.2904063) | Error-bounded compression for multidimensional visual tensors | IEEE TVCG | 2020 |
| Yang and Hospedales, ["Deep Multi-Task Representation Learning: A Tensor Factorisation Approach"](https://openreview.net/forum?id=SkhU2fcll) | Tucker and TT parameter sharing across tasks | ICLR | 2017 |

### Quantum Data and Probabilistic Modeling

| Paper | Contribution | Venue | Year |
| --- | --- | --- | --- |
| Chen et al., ["ANTN: Bridging Autoregressive Neural Networks and Tensor Networks for Quantum Many-Body Simulation"](https://dblp.org/rec/conf/nips/ChenNCLS23) | Combines autoregressive models with TNs for quantum simulation | NeurIPS | 2023 |
| Liu et al., ["Tensor Networks for Unsupervised Machine Learning"](https://doi.org/10.1103/PhysRevE.107.L012103) | MPS-based autoregressive unsupervised learning | Physical Review E | 2023 |
| Miller et al., ["Tensor Networks for Probabilistic Sequence Modeling"](https://proceedings.mlr.press/v130/miller21a.html) | Conditional sequence generation with uniform MPS | AISTATS | 2021 |
| Glasser et al., ["Expressive Power of Tensor-Network Factorizations for Probabilistic Modeling"](https://proceedings.neurips.cc/paper/2019/hash/b86e8d03fe992d1b0e19656875ee557c-Abstract.html) | Locally purified states for probabilistic modeling | NeurIPS | 2019 |
| Han et al., ["Unsupervised Generative Modeling Using Matrix Product States"](https://doi.org/10.1103/PhysRevX.8.031012) | Generative modeling and sampling with MPS | Physical Review X | 2018 |
| Stoudenmire and Schwab, ["Supervised Learning with Tensor Networks"](https://proceedings.neurips.cc/paper/2016/hash/5314b9674c86e3f9d1ba25ef9bb32895-Abstract.html) | Foundational MPS classifier for classical data | NeurIPS | 2016 |

## TNN Model Architectures

### Tensorial CNNs and Compact Vision Models

| Paper | Contribution | Venue | Year |
| --- | --- | --- | --- |
| Xie et al., ["Self-Supervised Weight Templates for Scalable Vision Model Initialization"](https://icml.cc/virtual/2026/poster/63459) | Shared Tucker templates for initialization across model sizes | ICML | 2026 |
| Pham et al., ["Coupled Tensor Decomposition for Compact Network Representation"](https://doi.org/10.1109/TNNLS.2025.3609797) | Coupled low-rank structure across related parameter tensors | IEEE TNNLS | 2026 |
| Yang et al., ["Kronecker Generative Networks"](https://icml.cc/virtual/2026/poster/61891) | Kronecker-structured generation of parameter-efficient architectures | ICML | 2026 |
| Pan et al., ["A Unified Weight Initialization Paradigm for Tensorial Convolutional Neural Networks"](https://proceedings.mlr.press/v162/pan22b.html) | General initialization theory for TCNNs | ICML | 2022 |
| Yin et al., ["Towards Efficient Tensor Decomposition-Based DNN Model Compression"](https://openaccess.thecvf.com/content/CVPR2021/html/Yin_Towards_Efficient_Tensor_Decomposition-Based_DNN_Model_Compression_With_Optimization_Framework_CVPR_2021_paper.html) | Optimization framework for decomposition-based compression | CVPR | 2021 |
| Ye et al., ["Block-Term Tensor Neural Networks"](https://doi.org/10.1016/j.neunet.2020.08.016) | BTT parameterization for compact neural layers | Neural Networks | 2020 |
| Kossaifi et al., ["Factorized Higher-Order CNNs"](https://openaccess.thecvf.com/content_CVPR_2020/html/Kossaifi_Factorized_Higher-Order_CNNs_With_an_Application_to_Spatio-Temporal_Emotion_Estimation_CVPR_2020_paper.html) | CP-factorized higher-order convolution | CVPR | 2020 |
| Hayashi et al., ["Einconv: Exploring Unexplored Tensor Network Decompositions for CNNs"](https://proceedings.neurips.cc/paper/2019/hash/2bd2e3373dce441c6c3bfadd1daa953e-Abstract.html) | General tensor-diagram search space for convolution | NeurIPS | 2019 |
| Wang et al., ["Wide Compression: Tensor Ring Nets"](https://openaccess.thecvf.com/content_cvpr_2018/html/Wang_Wide_Compression_Tensor_CVPR_2018_paper.html) | TR compression of convolutional and fully connected layers | CVPR | 2018 |
| Novikov et al., ["Tensorizing Neural Networks"](https://proceedings.neurips.cc/paper/2015/hash/6855456e2fe46a9d49d3d3af4f57443d-Abstract.html) | Foundational TT parameterization of neural layers | NeurIPS | 2015 |

### Tensorial RNNs

| Paper | Contribution | Venue | Year |
| --- | --- | --- | --- |
| Lizaire et al., ["A Tensor Decomposition Perspective on Second-Order RNNs"](https://proceedings.mlr.press/v235/lizaire24a.html) | Connects second-order RNNs to tensor decomposition | ICML | 2024 |
| Yin et al., ["Towards Extremely Compact RNNs for Video Recognition with Fully Decomposed Hierarchical Tucker Structure"](https://openaccess.thecvf.com/content/CVPR2021/html/Yin_Towards_Extremely_Compact_RNNs_for_Video_Recognition_With_Fully_Decomposed_CVPR_2021_paper.html) | Fully decomposed HT recurrent models | CVPR | 2021 |
| Su et al., ["Convolutional Tensor-Train LSTM for Spatio-Temporal Learning"](https://proceedings.neurips.cc/paper/2020/hash/9e1a36515d6704d7eb7a30d783400e5d-Abstract.html) | Conv-TT recurrence for spatiotemporal prediction | NeurIPS | 2020 |
| Pan et al., ["Compressing Recurrent Neural Networks with Tensor Ring for Action Recognition"](https://ojs.aaai.org/index.php/AAAI/article/view/4393) | TR-LSTM recurrent compression | AAAI | 2019 |
| Jose et al., ["Kronecker Recurrent Units"](https://proceedings.mlr.press/v80/jose18a.html) | Kronecker-factorized recurrent matrices | ICML | 2018 |
| Ye et al., ["Learning Compact Recurrent Neural Networks with Block-Term Tensor Decomposition"](https://openaccess.thecvf.com/content_cvpr_2018/html/Ye_Learning_Compact_Recurrent_CVPR_2018_paper.html) | BTT recurrent layers | CVPR | 2018 |
| Yang et al., ["Tensor-Train Recurrent Neural Networks for Video Classification"](https://proceedings.mlr.press/v70/yang17e.html) | TT input-to-hidden transformations | ICML | 2017 |

### Tensorial Transformers and Attention

| Paper | Contribution | Venue | Year |
| --- | --- | --- | --- |
| Klein et al., ["Tucker Attention"](https://icml.cc/virtual/2026/poster/65314) | Tucker generalization of approximate attention mechanisms | ICML | 2026 |
| Zhang et al., ["Tensor Product Attention Is All You Need"](https://proceedings.neurips.cc/paper_files/paper/2025/hash/a301ec7cb9e07dc050403e2eb11d0041-Abstract-Conference.html) | Tensor-product attention with structured interactions | NeurIPS | 2025 |
| Pan et al., ["Reusing Pretrained Models by Multi-Linear Operators for Efficient Training"](https://dblp.org/rec/conf/nips/0005YYXSJL23) | TR-MPO mapping between pretrained model scales | NeurIPS | 2023 |
| Liu et al., ["Tuformer: Data-Driven Design of Transformers for Improved Generalization or Efficiency"](https://openreview.net/forum?id=V0A5g83gdQ_) | Tensor-diagram design across attention heads | ICLR | 2022 |
| Ren et al., ["Exploring Extreme Parameter Compression for Pre-Trained Language Models"](https://openreview.net/forum?id=lpjEhotFI1) | Tucker compression of pretrained Transformers | ICLR | 2022 |
| Li et al., ["Hypoformer: Hybrid Decomposition Transformer for Edge-Friendly Neural Machine Translation"](https://aclanthology.org/2022.emnlp-main.475/) | Hybrid tensor-train Transformer compression | EMNLP | 2022 |
| Liu et al., ["Enabling Lightweight Fine-Tuning for Pre-Trained Language Model Compression Based on MPOs"](https://aclanthology.org/2021.acl-long.355/) | MPO compression with lightweight fine-tuning | ACL-IJCNLP | 2021 |
| Ma et al., ["A Tensorized Transformer for Language Modeling"](https://proceedings.neurips.cc/paper/8495-a-tensorized-transformer-for-language-modeling) | BTT-based multilinear attention | NeurIPS | 2019 |

### Tensorial Graph Neural Networks

| Paper | Contribution | Venue | Year |
| --- | --- | --- | --- |
| Wang et al. ["T-GINEE: A Tensor-Based Multi-Graph Representation Learning"](https://icml.cc/virtual/2026/poster/62311) | Tensor representation learning over multiple graphs | ICML | 2026 |
| Hua et al., ["High-Order Pooling for Graph Neural Networks with Tensor Decomposition"](https://openreview.net/forum?id=N7-EIciq3R) | High-order nonlinear graph interactions through tensor pooling | NeurIPS | 2022 |
| Zhao et al., ["Multi-View Tensor Graph Neural Networks through Reinforced Aggregation"](https://doi.org/10.1109/TKDE.2022.3142179) | Tucker-structured aggregation for multi-view graphs | IEEE TKDE | 2022 |
| Yin et al., ["Nimble GNN Embedding with Tensor-Train Decomposition"](https://dl.acm.org/doi/10.1145/3534678.3539403) | TT-compressed scalable GNN embeddings | KDD | 2022 |
| Jia et al., ["Dynamic Spatiotemporal Graph Neural Network with Tensor Network"](https://arxiv.org/abs/2003.08729) | PEPS-inspired spatial and temporal graph correlations | Preprint | 2020 |

### LLMs, Mixture-of-Experts, and Parameter-Efficient Adaptation

| Paper | Contribution | Venue | Year |
| --- | --- | --- | --- |
| Ye et al., ["TRAC"](https://iclr.cc/virtual/2026/poster/10006929) | Across-layer TT compression for PEFT | ICLR | 2026 |
| Xu et al., ["TD-MoE"](https://iclr.cc/virtual/2026/poster/10010804) | Tensor decomposition tailored to MoE models | ICLR | 2026 |
| Li et al., ["LeSTD"](https://iclr.cc/virtual/2026/poster/10011895) | Learned sparse tensor decomposition for LLM compression | ICLR | 2026 |
| Xu et al., ["TIME"](https://icml.cc/virtual/2026/poster/64179) | Tensor-factorized MoE with intrinsic routing | ICML | 2026 |
| Zheng et al., ["ReFTA"](https://cvpr.thecvf.com/virtual/2026/poster/38595) | Reconstruction-free tensorized PEFT | CVPR | 2026 |
| Yang et al., ["LoRETTA: Low-Rank Economic Tensor-Train Adaptation for Ultra-Low-Parameter Fine-Tuning of LLMs"](https://aclanthology.org/2024.naacl-long.180/) | TT-based ultra-low-parameter adaptation | NAACL | 2024 |

### Quantum Neural Networks and Circuit Connections

| Paper | Contribution | Venue | Year |
| --- | --- | --- | --- |
| Loconte et al., ["What Is the Relationship Between Tensor Factorizations and Circuits?"](https://iclr.cc/virtual/2026/poster/10014069) | Generalized framework connecting tensor factorizations and tractable circuits | ICLR | 2026 |
| Chen et al., ["ANTN"](https://dblp.org/rec/conf/nips/ChenNCLS23) | Autoregressive and TN hybrid for many-body simulation | NeurIPS | 2023 |
| Levine et al., ["Quantum Entanglement in Deep Learning Architectures"](https://doi.org/10.1103/PhysRevLett.122.065301) | Entanglement interpretation of deep architectures | Physical Review Letters | 2019 |
| Levine et al., ["Deep Learning and Quantum Entanglement"](https://openreview.net/forum?id=S1WRibb0Z) | Links convolutional arithmetic circuits and many-body wave functions | ICLR | 2018 |
| Cohen and Shashua, ["Convolutional Rectifier Networks as Generalized Tensor Decompositions"](https://proceedings.mlr.press/v48/cohenb16.html) | Generalized tensor decomposition view of convolutional networks | ICML | 2016 |
| Cohen et al., ["On the Expressive Power of Deep Learning: A Tensor Analysis"](https://proceedings.mlr.press/v49/cohen16.html) | CP versus hierarchical tensor decompositions for depth separation | COLT | 2016 |

### Scientific Machine Learning

| Paper | Contribution | Venue | Year |
| --- | --- | --- | --- |
| Zhou et al., ["Tucker-FNO"](https://iclr.cc/virtual/2026/poster/10009240) | Tucker decomposition of high-dimensional Fourier neural operators with approximation theory | ICLR | 2026 |
| Ganahl et al., ["Density Matrix Renormalization Group with Tensor Processing Units"](https://doi.org/10.1103/PRXQuantum.4.010317) | TPU-accelerated DMRG and tensor computation | PRX Quantum | 2023 |

## Training and Model Lifecycle

### Stable Training and Initialization

| Paper | Contribution | Venue | Year |
| --- | --- | --- | --- |
| Xie et al., ["Self-Supervised Weight Templates for Scalable Vision Model Initialization"](https://icml.cc/virtual/2026/poster/63459) | Cross-scale self-supervised weight initialization | ICML | 2026 |
| Pan et al., ["Reusing Pretrained Models by Multi-Linear Operators"](https://dblp.org/rec/conf/nips/0005YYXSJL23) | Efficient model growth and parameter reuse | NeurIPS | 2023 |
| Pan et al., ["A Unified Weight Initialization Paradigm for TCNNs"](https://proceedings.mlr.press/v162/pan22b.html) | Variance-preserving initialization across tensor formats | ICML | 2022 |
| Panagakis et al., ["Tensor Methods in Computer Vision and Deep Learning"](https://doi.org/10.1109/JPROC.2021.3074329) | Mixed-precision and broader tensor learning guidance | Proceedings of the IEEE | 2021 |

### Rank and Tensor-Network Structure Search

| Paper | Contribution | Venue | Year |
| --- | --- | --- | --- |
| Wang et al., ["Renormalization Group Guided Tensor Network Structure Search"](https://doi.org/10.1609/aaai.v40i31.39840) | Renormalization-guided automated TN structure search | AAAI | 2026 |
| Zeng et al., ["MTNL"](https://icml.cc/virtual/2026/poster/62604) | Mixed TN structures and structure-search priors | ICML | 2026 |
| Ghadiri et al., ["Approximately Optimal Core Shapes for Tensor Decompositions"](https://proceedings.mlr.press/v202/ghadiri23a.html) | Core-shape optimization beyond rank selection | ICML | 2023 |
| Li et al., ["Solving Tensor Network Structure Search with Fewer Evaluations"](https://proceedings.mlr.press/v202/li23ar.html) | Alternating local enumeration for efficient structure search | ICML | 2023 |
| Li et al., ["Permutation Search of Tensor Network Structures via Local Sampling"](https://proceedings.mlr.press/v162/li22m.html) | Local-sampling mode permutation search | ICML | 2022 |
| Li et al., ["Evolutionary Topology Search for Tensor Network Decomposition"](https://proceedings.mlr.press/v119/li20l.html) | Evolutionary search over TN topologies | ICML | 2020 |
| Yuan et al., ["Tensor Ring Decomposition with Rank Minimization on Latent Space"](https://doi.org/10.1609/aaai.v33i01.33019151) | Latent-space rank minimization for TR | AAAI | 2019 |

### Hardware, Contraction, and Tensor Computation

| Paper | Contribution | Venue | Year |
| --- | --- | --- | --- |
| Xu et al., ["LEGO"](https://icml.cc/virtual/2026/poster/62027) | Hierarchical search and synthesis for tensor GPU kernels | ICML | 2026 |
| Gray and Chan, ["Hyperoptimized Approximate Contraction of Tensor Networks with Arbitrary Geometry"](https://doi.org/10.1103/PhysRevX.14.011009) | Hyperoptimized contraction for arbitrary TN geometries | Physical Review X | 2024 |
| Memmel et al., ["Position: Tensor Networks Are a Valuable Asset for Green AI"](https://proceedings.mlr.press/v235/memmel24a.html) | Efficiency- and deployment-aware evaluation of TN models | ICML | 2024 |
| Meirom et al., ["Optimizing Tensor Network Contraction Using Reinforcement Learning"](https://proceedings.mlr.press/v162/meirom22a.html) | RL-based contraction-order optimization | ICML | 2022 |
| Qu et al., ["Hardware-Enabled Efficient Data Processing with Tensor-Train Decomposition"](https://doi.org/10.1109/TCAD.2021.3056337) | Customized TT processing engine | IEEE TCAD | 2022 |
| Deng et al., ["TIE: Energy-Efficient Tensor Train-Based Inference Engine"](https://doi.org/10.1145/3307650.3322258) | Hardware inference engine for TT layers | ISCA | 2019 |

## Toolboxes

### Basic Tensor Operations

| Toolbox | Main capability | Backend |
| --- | --- | --- |
| [TensorLy](https://tensorly.org/) | Tensor algebra, decomposition, regression, and backend abstraction | Python: NumPy, PyTorch, JAX, TensorFlow, CuPy |
| [Tensor Toolbox](https://www.tensortoolbox.org/) | General multidimensional arrays and tensor decompositions | MATLAB |
| [tntorch](https://github.com/rballester/tntorch) | Differentiable TT, CP, and Tucker modeling | PyTorch |
| [ITensor](https://itensor.org/) | Diagram-oriented tensor-network algorithms | C++ and Julia |
| [TensorNetwork](https://github.com/google/TensorNetwork) | General tensor-network construction and contraction | Python |
| [Scikit-TT](https://github.com/PGelss/scikit_tt) | TT solvers, data-driven methods, and model construction | Python |
| [TT-Toolbox](https://github.com/oseledets/TT-Toolbox) | Core TT operations and algorithms | MATLAB |
| [TenDeC++](https://github.com/XiaoYangLiu-FinRL/TensorLet_in_C_C_PlusPlus) | CP, Tucker, t-SVD, and TT decomposition | C++ |

### Deep-Model Implementations

| Toolbox | Main capability | Backend |
| --- | --- | --- |
| [TensorLy-Torch](https://tensorly.org/torch/) | Tensorized neural layers and factorized parameters | PyTorch |
| [TedNet](https://github.com/tnbar/tednet) | CP, BTT, Tucker-2, TT, and TR neural layers | PyTorch |

### Quantum and Tensor-Network Simulation

| Toolbox | Main capability | Backend |
| --- | --- | --- |
| [TensorNetworkQuantumSimulator.jl](https://github.com/JoeyT1994/TensorNetworkQuantumSimulator.jl) | Quantum-circuit simulation with PEPS-style tensor-network backends | Julia |
| [ITensor](https://itensor.org/) | MPS/MPO and general TN simulation | C++ and Julia |
| [TensorNetwork](https://github.com/google/TensorNetwork) | General quantum-circuit tensor contraction | Python |
| [TeD-Q](https://github.com/amore-upf/ted-q) | Differentiable quantum machine learning and TN simulation | Python |
| [Yao](https://github.com/QuantumBFS/Yao.jl) | Extensible quantum algorithm simulation | Julia |
| [lambeq](https://github.com/CQCL/lambeq) | Quantum natural language processing | Python |

## Interpretability and Analysis

| Paper | Contribution | Venue | Year |
| --- | --- | --- | --- |
| Heidari and Rabusseau, ["TN-SHAP-G"](https://icml.cc/virtual/2026/poster/64574) | Graph-aligned TN surrogate for exact first- and higher-order Shapley interactions | ICML | 2026 |
| Pareja Monturiol et al., ["Tensorization of Neural Networks for Improved Privacy and Interpretability"](https://scipost.org/SciPostPhysCore.8.4.095) | Black-box MPS construction for privacy and interpretability | SciPost Physics Core | 2025 |
| Puljak et al., ["Tensor Network for Anomaly Detection in the Latent Space of Proton Collision Events at the LHC"](https://doi.org/10.1088/2632-2153/ae0243) | Interpretable MPS representations for anomaly detection | Machine Learning: Science and Technology | 2025 |
| Varshneya et al., ["Interpretable Tensor Fusion"](https://www.ijcai.org/proceedings/2024/0557.pdf) | Interpretable multimodal tensor interactions | IJCAI | 2024 |
| Hamdi and Angryk, ["Interpretable Feature Learning of Graphs Using Tensor Decomposition"](https://doi.org/10.1109/ICDM.2019.00038) | Tensor-factorized latent structure in graph data | ICDM | 2019 |

## Cross-Cutting Insights

These works support the revised survey's five synthesis themes in Sections 7.1-7.5.

| Theme | Representative paper | Venue | Year |
| --- | --- | --- | --- |
| Tensorization design beyond rank | Ghadiri et al., ["Approximately Optimal Core Shapes for Tensor Decompositions"](https://proceedings.mlr.press/v202/ghadiri23a.html) | ICML | 2023 |
| Tensorization design beyond rank | Li et al., ["Permutation Search of Tensor Network Structures via Local Sampling"](https://proceedings.mlr.press/v162/li22m.html) | ICML | 2022 |
| Expressiveness versus contractibility | Gray and Chan, ["Hyperoptimized Approximate Contraction of Tensor Networks with Arbitrary Geometry"](https://doi.org/10.1103/PhysRevX.14.011009) | Physical Review X | 2024 |
| Algorithmic shift | Bharadwaj et al., ["Efficient Leverage Score Sampling for Tensor Train Decomposition"](https://doi.org/10.52202/079017-2345) | NeurIPS | 2024 |
| Algorithmic shift | Tao et al., ["Undirected Probabilistic Model for Tensor Decomposition"](https://doi.org/10.52202/075280-1124) | NeurIPS | 2023 |
| Tensorization as inductive bias | Wang et al., ["Transformed Low-Rank Parameterization Can Help Robust Generalization for Tensor Neural Networks"](https://doi.org/10.52202/075280-0135) | NeurIPS | 2023 |
| Unified TN learning | Zeng et al., ["MTNL"](https://icml.cc/virtual/2026/poster/62604) | ICML | 2026 |
| Scientific machine learning | Zhou et al., ["Tucker-FNO"](https://iclr.cc/virtual/2026/poster/10009240) | ICLR | 2026 |

### Reviewer-Requested Foundations

| Paper | Status | Year |
| --- | --- | --- |
| Hong et al., ["Generalized Canonical Polyadic Tensor Decomposition"](https://doi.org/10.1137/18M1203626) | SIAM Review | 2020 |
| Falco et al., ["Geometric Structures in Tensor Representations"](https://arxiv.org/abs/1505.03027) | Preprint | 2015 |
| Ghadiri et al., ["Approximately Optimal Core Shapes for Tensor Decompositions"](https://proceedings.mlr.press/v202/ghadiri23a.html) | ICML | 2023 |
| Gray and Chan, ["Hyperoptimized Approximate Contraction of Tensor Networks with Arbitrary Geometry"](https://doi.org/10.1103/PhysRevX.14.011009) | Physical Review X | 2024 |
| Li et al., ["Permutation Search of Tensor Network Structures via Local Sampling"](https://proceedings.mlr.press/v162/li22m.html) | ICML | 2022 |
| Yuan et al., ["Tensor Ring Decomposition with Rank Minimization on Latent Space"](https://doi.org/10.1609/aaai.v33i01.33019151) | AAAI | 2019 |
| Hameed and Rabusseau, ["Efficient Probabilistic Tensor Networks"](https://arxiv.org/abs/2510.00382) | Preprint | 2025 |

## Related Surveys

| Survey | Focus | Year |
| --- | --- | --- |
| Biamonte and Bergholm, ["Tensor Networks in a Nutshell"](https://arxiv.org/abs/1708.00006) | Quantum TN foundations, diagrams, contraction, and entanglement | 2017 |
| Panagakis et al., ["Tensor Methods in Computer Vision and Deep Learning"](https://doi.org/10.1109/JPROC.2021.3074329) | Tensor methods for representation learning, vision, and deep learning | 2021 |
| Panagakis et al., ["Tensor Methods in Deep Learning"](https://doi.org/10.1016/B978-0-32-391772-8.00021-1) | Broad tensor methods, applications, and quantum-network material | 2024 |
