# Awesome ML Positive Unlabeled learning

### Papers
<!-- MarkdownTOC depth=4 -->
- [Papers \\w code](#papers)
  - [Overview](#overview)
    - [Theoretical Comparisons of Positive-Unlabeled Learning against Positive-Negative Learning(2016)](https://proceedings.neurips.cc/paper/2016/file/be3159ad04564bfb90db9e32851ebf9c-Paper.pdf)
    - [Learning from positive and unlabeled data: a survey(2018)](https://arxiv.org/abs/1811.04820)
    - [Positive and unlabeled learning algorithms and applications: A survey(2019)](https://www.researchgate.net/profile/Kristen-Jaskie/publication/337503578_Positive_And_Unlabeled_Learning_Algorithms_And_Applications_A_Survey/links/609b0124458515d31513c2e9/Positive-And-Unlabeled-Learning-Algorithms-And-Applications-A-Survey.pdf)
    - [Exploring Positive Unlabeled Machine Learning(2021)](https://digital.wpi.edu/downloads/vq27zr55f)
    - [Positive Unlabeled Learning - Synthesis Lectures on AI and ML(2022)](https://link.springer.com/book/10.1007/978-3-031-79178-9)
    - [A recent survey on instance-dependent positive and unlabeled learning(2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11997483/)
  - [Cost-sensitive methods](#cost-sensitive)
    - [Learning Classifiers from Only Positive and Unlabeled Data(2008)](https://cseweb.ucsd.edu/~elkan/posonly.pdf)\[[pulearn](https://github.com/pulearn/pulearn#31elkanoto)\]
    - [Analysis of Learning from Positive and Unlabeled Data(2014)](https://papers.nips.cc/paper/2014/file/35051070e572e47d2c26c241ab88307f-Paper.pdf)
    - [A Modified Logistic Regression for Positive and Unlabeled Learning(2019)](https://www.researchgate.net/profile/Kristen-Jaskie/publication/340306999_A_Modified_Logistic_Regression_for_Positive_and_Unlabeled_Learning/links/609b0152a6fdccaebd2525d1/A-Modified-Logistic-Regression-for-Positive-and-Unlabeled-Learning.pdf) \[[video](https://www.youtube.com/watch?v=uk6SlTzfbUY)\]
    - [DEDPUL: Difference-of-Estimated-Densities-based Positive-Unlabeled Learning(2019)](https://arxiv.org/abs/1902.06965)\[[source](https://github.com/dimonenka/DEDPUL)\]
    - [PULSNAR: Positive Unlabeled Learning Selected Not At Random(2023)](https://arxiv.org/abs/2303.08269)
    - [PUe: Biased Positive-Unlabeled Learning Enhancement by Causal Inference(2023)](https://proceedings.neurips.cc/paper_files/paper/2023/hash/3efb4bdc6bfe13e1ff95b4407c37961d-Abstract-Conference.html)\[[source](https://github.com/huawei-noah/Noah-research/tree/master/PUe)\]
    - [Contrastive Approach to Prior Free Positive Unlabeled Learning(2024)](https://arxiv.org/abs/2402.06038)
    - [Positive and Unlabeled Learning with Controlled Probability Boundary Fence(2024)](https://proceedings.mlr.press/v235/li24p.html)
    - [A boosting framework for positive-unlabeled learning - AdaPU(2024)](https://link.springer.com/article/10.1007/s11222-024-10529-y)
    - [Class prior estimation for positive-unlabeled learning when label shift occurs(2025)](https://arxiv.org/abs/2502.21194)
  - [Sample-selection/Two-step methods](#sample-selection)
    - [Positive-unlabeled learning for disease gene identification(2012)](https://academic.oup.com/bioinformatics/article/28/20/2640/206620?login=true)
    - [A bagging SVM to learn from positive and unlabeled examples(2013)](https://members.cbio.mines-paristech.fr/~jvert/svn/bibli/local/Mordelet2013bagging.pdf) \[[pulearn](https://github.com/pulearn/pulearn#32bagging-based-pu-learning)\]
    - [Revisiting Sample Selection Approach to Positive-Unlabeled Learning: Turning Unlabeled Data into Positive rather than Negative(2019)](https://arxiv.org/pdf/1901.10155.pdf)
    - [Improving Positive Unlabeled Learning: Practical AUL Estimation and New Training Method for Extremely Imbalanced Data Sets(2020)](https://arxiv.org/pdf/2004.09820.pdf)
    - [PULNS: Positive-Unlabeled Learning with Effective Negative Sample Selector(2021)](https://ojs.aaai.org/index.php/AAAI/article/view/17064/16871)\[[slides](https://slideslive.com/38948747/pulns-positiveunlabeled-learning-with-effective-negative-sample-selector)\]
    - [Positive-Unlabeled Learning by Latent Group-Aware Meta Disambiguation(2024)](https://openaccess.thecvf.com/content/CVPR2024/papers/Long_Positive-Unlabeled_Learning_by_Latent_Group-Aware_Meta_Disambiguation_CVPR_2024_paper.pdf)
  - [Deep Learning methods](#deep-learning)
    - [Positive-Unlabeled Learning with Non-Negative Risk Estimator - nnPU(2017)](https://arxiv.org/abs/1703.00593)\[[source](https://github.com/kiryor/nnPUlearning)\]
    - [Variational approach for learning from positive and unlabeled data - VPU(2020)](https://proceedings.neurips.cc/paper/2020/hash/aa0d2a804a3510442f2fd40f2100b054-Abstract.html)\[[source](https://github.com/HC-Feynman/vpu)\]
    - [Improving Non-Negative Positive-Unlabeled Learning for News Headline Classification - FLPU(2023)](https://ieeexplore.ieee.org/document/10106254/)
    - [Multiscale Positive-Unlabeled Framework for AI-Generated Text Detection - MPU(2024)](https://proceedings.iclr.cc/paper_files/paper/2024/file/95ab5c3e26fd82c7de3230bbad087d2d-Paper-Conference.pdf)
  - [Graph Neural Networks](#gnn)
    - [Learning Graph Neural Networks with Positive and Unlabeled Nodes - LSDAN(2021)](https://arxiv.org/abs/2103.04683)
    - [PU-GNN: Polypharmacy Side-Effects Detection Based on Graph Neural Networks(2024)](https://onlinelibrary.wiley.com/doi/full/10.1155/2024/4749668)
    - [Bootstrap Latent Prototypes for graph positive-unlabeled learning(2024)](https://www.sciencedirect.com/science/article/abs/pii/S1566253524003312)
    - [Unraveling the impact of heterophilic structures on graph positive-unlabeled learning(2024)](https://arxiv.org/abs/2405.19919)
    - [Graph neural networks for positive and unlabeled learning: a rewiring approach(2025)](https://link.springer.com/article/10.1007/s10115-025-02547-7)
  - [Anomaly Detection](#anomaly-detection)
    - [Boosting Positive and Unlabeled Learning for Anomaly Detection With Multi-Features(2017)](https://ieeexplore.ieee.org/document/8467985/)
    - [Deep Positive-Unlabeled Anomaly Detection for Contaminated Unlabeled Data(2024)](https://arxiv.org/abs/2405.18929)
    - [Few-shot anomaly detection using positive unlabeled learning with cycle consistency - PUFAD(2024)](https://www.sciencedirect.com/science/article/abs/pii/S0957417424017573)


### Implementations
- [Frameworks](#frameworks)
  - [Python](#frameworks-python)
    - [`nnPUlearning`](https://github.com/kiryor/nnPUlearning) - Non-negative PU learning (Chainer)
    - [`pulearn`](https://github.com/pulearn/pulearn) - Elkan & Noto, Bagging-based methods
    - [`dedpul`](https://github.com/dimonenka/DEDPUL) - Density-based PU learning
    - [`vpu`](https://github.com/HC-Feynman/vpu) - Variational PU learning (PyTorch)
    - [`PUe`](https://github.com/huawei-noah/Noah-research/tree/master/PUe) - Causal Inference PU (NeurIPS 2023)
    - [`pulse`](https://github.com/nobutaka-ito/pulse) - Audio Signal Enhancement (ICASSP 2023 Best Paper)
    - [`Active_PU_Learning`](https://github.com/Lorenzo-Perini/Active_PU_Learning) - Class Prior Estimation in Active PU
    - [`pu-learning`](https://github.com/cimeister/pu-learning) - PyTorch implementation of nnPU/uPU
  - [Spark](#frameworks-spark)
    - [`pu4spark`](https://github.com/ispras/pu4spark)

### Tutorials

- [An introductory tutorial to the "Learning from Positive and Unlabeled Data" field.](https://dtai.cs.kuleuven.be/tutorials/pulearning/)
- [tinyML Talks Phoenix: Positive Unlabeled Learning for Tiny ML](https://www.youtube.com/watch?v=uk6SlTzfbUY)
- [Semi-Supervised Classification of Unlabeled Data (PU Learning)](https://towardsdatascience.com/semi-supervised-classification-of-unlabeled-data-pu-learning-81f96e96f7cb)

### Concepts
- [Class prior and label frequency](https://youtu.be/mSoeaYt6Oi8?t=1282)
- Cost-sensitive and sample-selection methods
- Inductive vs Transductive PU learning. a.k.a(?) [(Single-training set vs case-control scenario)](https://youtu.be/mSoeaYt6Oi8?t=823)
- [Labelling mechanism](https://youtu.be/mSoeaYt6Oi8?t=419)
- Assumptions
  - [Partial Seperability](https://youtu.be/uk6SlTzfbUY?t=1129)
  - [SCAR(Selected Completely At Random)](https://youtu.be/uk6SlTzfbUY?t=1243) - assumes all positive examples have equal probability of being labeled
  - Non-SCAR / Instance-dependent labeling - labeling probability depends on instance features
    - In healthcare: severe cases more likely to be diagnosed than mild ones
    - In e-commerce: popular items more likely to receive reviews
    - Examples far from decision boundary have higher labeling probability
    - [Instance-dependent PU learning survey(2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11997483/)

### Cases/Applications
- [Positive Unlabeled Learing, MegaFon, ODS.ai(2020)\[RU\]](https://youtu.be/7nKswav3Zrw)
- [FedPU: Federated Learning with Positive and Unlabeled Data(2022)](https://icml.cc/virtual/2022/spotlight/17090)
- [PULSE: Positive-Unlabelled Learning for audio Signal Enhancement(2023)](https://github.com/nobutaka-ito/pulse) - ICASSP 2023 Best Paper Award
- [Fairness-Aware Online Positive-Unlabeled Learning(2024)](https://aclanthology.org/2024.emnlp-industry.14/)
- [Applications of PU and NU Learning in Cybersecurity(2024)](https://arxiv.org/abs/2412.06203)
- [Positive-Unlabeled Learning in Implicit Feedback Recommendation Systems(2025)](https://www.mdpi.com/1099-4300/28/1/41)
