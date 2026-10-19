# Kolmogorov-Arnold Network Papers
A complete list of papers on KANs. Papers with submission dates before the original KAN papers are excluded. You might find [this awesome list](https://github.com/mintisan/awesome-kan) useful as well. You can find the papers and their titles, abstracts, authors, links, and dates stored in [this csv file](https://github.com/RamtinMoslemi/KAN-Papers/blob/main/kan_papers.csv).

## Papers by Month
Number of papers submitted to arXiv by month.

![monthly_papers](figures/papers_by_month.svg)

## Word Clouds
Word clouds of KAN paper titles and abstracts.

![word_clouds](figures/word_clouds.png)

## Notebook
You can play with the notebook:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/RamtinMoslemi/KAN-Papers/blob/main/KAN_Papers.ipynb) [![Open In kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://raw.githubusercontent.com/RamtinMoslemi/KAN-Papers/main/KAN_Papers.ipynb)


# 2024
## April
### [KAN: Kolmogorov-Arnold Networks](https://arxiv.org/abs/2404.19756)

**Authors:**
Ziming Liu, Yixuan Wang, Sachin Vaidya, Fabian Ruehle, James Halverson, Marin Soljačić, Thomas Y. Hou, Max Tegmark

**Venue:**
International Conference on Learning Representations

**Citation Count:**
534

**Abstract:**
Inspired by the Kolmogorov-Arnold representation theorem, we propose Kolmogorov-Arnold Networks (KANs) as promising alternatives to Multi-Layer Perceptrons (MLPs). While MLPs have fixed activation functions on nodes ("neurons"), KANs have learnable activation functions on edges ("weights"). KANs have no linear weights at all -- every weight parameter is replaced by a univariate function parametrized as a spline. We show that this seemingly simple change makes KANs outperform MLPs in terms of accuracy and interpretability. For accuracy, much smaller KANs can achieve comparable or better accuracy than much larger MLPs in data fitting and PDE solving. Theoretically and empirically, KANs possess faster neural scaling laws than MLPs. For interpretability, KANs can be intuitively visualized and can easily interact with human users. Through two examples in mathematics and physics, KANs are shown to be useful collaborators helping scientists (re)discover mathematical and physical laws. In summary, KANs are promising alternatives for MLPs, opening opportunities for further improving today's deep learning models which rely heavily on MLPs.
       


## May
### [Biology-inspired joint distribution neurons based on Hierarchical Correlation Reconstruction allowing for multidirectional propagation of values and densities](https://arxiv.org/abs/2405.05097)

**Author:**
Jarek Duda

**Citation Count:**
2

**Abstract:**
Recently a million of biological neurons (BNN) has turned out better from modern RL methods in playing Pong~\cite{RL}, reminding they are still qualitatively superior e.g. in learning, flexibility and robustness - suggesting to try to improve current artificial e.g. MLP/KAN for better agreement with biological. There is proposed extension of KAN approach to neurons containing model of local joint distribution: $ρ(\mathbf{x})=\sum_{\mathbf{j}\in B} a_\mathbf{j} f_\mathbf{j}(\mathbf{x})$ for $\mathbf{x} \in [0,1]^d$, adding interpretation and information flow control to KAN, and allowing to gradually add missing 3 basic properties of biological: 1) biological axons propagate in both directions~\cite{axon}, while current artificial are focused on unidirectional propagation - joint distribution neurons can repair by substituting some variables to get conditional values/distributions for the remaining. 2) Animals show risk avoidance~\cite{risk} requiring to process variance, and generally real world rather needs probabilistic models - the proposed can predict and propagate also distributions as vectors of moments: (expected value, variance) or higher. 3) biological neurons require local training, and beside backpropagation, the proposed allows many additional ways, like direct training, through tensor decomposition, or finally local and promising: information bottleneck. Proposed approach is very general, can be also used as extension of softmax in embeddings of e.g. transformer, suggesting interpretation that features are mixed moments of joint density of real-world properties.
       


### [Kolmogorov-Arnold Networks are Radial Basis Function Networks](https://arxiv.org/abs/2405.06721)

**Author:**
Ziyao Li

**Citation Count:**
76

**Abstract:**
This short paper is a fast proof-of-concept that the 3-order B-splines used in Kolmogorov-Arnold Networks (KANs) can be well approximated by Gaussian radial basis functions. Doing so leads to FastKAN, a much faster implementation of KAN which is also a radial basis function (RBF) network.
       


### [Chebyshev Polynomial-Based Kolmogorov-Arnold Networks: An Efficient Architecture for Nonlinear Function Approximation](https://arxiv.org/abs/2405.07200)

**Authors:**
Sidharth SS, Keerthana AR, Gokul R, Anas KP

**Citation Count:**
85

**Abstract:**
Accurate approximation of complex nonlinear functions is a fundamental challenge across many scientific and engineering domains. Traditional neural network architectures, such as Multi-Layer Perceptrons (MLPs), often struggle to efficiently capture intricate patterns and irregularities present in high-dimensional functions. This paper presents the Chebyshev Kolmogorov-Arnold Network (Chebyshev KAN), a new neural network architecture inspired by the Kolmogorov-Arnold representation theorem, incorporating the powerful approximation capabilities of Chebyshev polynomials. By utilizing learnable functions parametrized by Chebyshev polynomials on the network's edges, Chebyshev KANs enhance flexibility, efficiency, and interpretability in function approximation tasks. We demonstrate the efficacy of Chebyshev KANs through experiments on digit classification, synthetic function approximation, and fractal function generation, highlighting their superiority over traditional MLPs in terms of parameter efficiency and interpretability. Our comprehensive evaluation, including ablation studies, confirms the potential of Chebyshev KANs to address longstanding challenges in nonlinear function approximation, paving the way for further advancements in various scientific and engineering applications.
       


### [TKAN: Temporal Kolmogorov-Arnold Networks](https://arxiv.org/abs/2405.07344)

**Authors:**
Remi Genet, Hugo Inzirillo

**Venue:**
Social Science Research Network

**Citation Count:**
72

**Abstract:**
Recurrent Neural Networks (RNNs) have revolutionized many areas of machine learning, particularly in natural language and data sequence processing. Long Short-Term Memory (LSTM) has demonstrated its ability to capture long-term dependencies in sequential data. Inspired by the Kolmogorov-Arnold Networks (KANs) a promising alternatives to Multi-Layer Perceptrons (MLPs), we proposed a new neural networks architecture inspired by KAN and the LSTM, the Temporal Kolomogorov-Arnold Networks (TKANs). TKANs combined the strenght of both networks, it is composed of Recurring Kolmogorov-Arnold Networks (RKANs) Layers embedding memory management. This innovation enables us to perform multi-step time series forecasting with enhanced accuracy and efficiency. By addressing the limitations of traditional models in handling complex sequential patterns, the TKAN architecture offers significant potential for advancements in fields requiring more than one step ahead forecasting.
       


### [Predictive Modeling of Flexible EHD Pumps using Kolmogorov-Arnold Networks](https://arxiv.org/abs/2405.07488)

**Authors:**
Yanhong Peng, Yuxin Wang, Fangchao Hu, Miao He, Zebing Mao, Xia Huang, Jun Ding

**Venue:**
Biomimetic Intelligence and Robotics

**Citation Count:**
54

**Abstract:**
We present a novel approach to predicting the pressure and flow rate of flexible electrohydrodynamic pumps using the Kolmogorov-Arnold Network. Inspired by the Kolmogorov-Arnold representation theorem, KAN replaces fixed activation functions with learnable spline-based activation functions, enabling it to approximate complex nonlinear functions more effectively than traditional models like Multi-Layer Perceptron and Random Forest. We evaluated KAN on a dataset of flexible EHD pump parameters and compared its performance against RF, and MLP models. KAN achieved superior predictive accuracy, with Mean Squared Errors of 12.186 and 0.001 for pressure and flow rate predictions, respectively. The symbolic formulas extracted from KAN provided insights into the nonlinear relationships between input parameters and pump performance. These findings demonstrate that KAN offers exceptional accuracy and interpretability, making it a promising alternative for predictive modeling in electrohydrodynamic pumping.
       


### [Kolmogorov-Arnold Networks (KANs) for Time Series Analysis](https://arxiv.org/abs/2405.08790)

**Authors:**
Cristian J. Vaca-Rubio, Luis Blanco, Roberto Pereira, Màrius Caus

**Citation Count:**
102

**Abstract:**
This paper introduces a novel application of Kolmogorov-Arnold Networks (KANs) to time series forecasting, leveraging their adaptive activation functions for enhanced predictive modeling. Inspired by the Kolmogorov-Arnold representation theorem, KANs replace traditional linear weights with spline-parametrized univariate functions, allowing them to learn activation patterns dynamically. We demonstrate that KANs outperforms conventional Multi-Layer Perceptrons (MLPs) in a real-world satellite traffic forecasting task, providing more accurate results with considerably fewer number of learnable parameters. We also provide an ablation study of KAN-specific parameters impact on performance. The proposed approach opens new avenues for adaptive forecasting models, emphasizing the potential of KANs as a powerful tool in predictive analytics.
       


### [Smooth Kolmogorov Arnold networks enabling structural knowledge representation](https://arxiv.org/abs/2405.11318)

**Authors:**
Moein E. Samadi, Younes Müller, Andreas Schuppert

**Citation Count:**
18

**Abstract:**
Kolmogorov-Arnold Networks (KANs) offer an efficient and interpretable alternative to traditional multi-layer perceptron (MLP) architectures due to their finite network topology. However, according to the results of Kolmogorov and Vitushkin, the representation of generic smooth functions by KAN implementations using analytic functions constrained to a finite number of cutoff points cannot be exact. Hence, the convergence of KAN throughout the training process may be limited. This paper explores the relevance of smoothness in KANs, proposing that smooth, structurally informed KANs can achieve equivalence to MLPs in specific function classes. By leveraging inherent structural knowledge, KANs may reduce the data required for training and mitigate the risk of generating hallucinated predictions, thereby enhancing model reliability and performance in computational biomedicine.
       


### [Wav-KAN: Wavelet Kolmogorov-Arnold Networks](https://arxiv.org/abs/2405.12832)

**Authors:**
Zavareh Bozorgasl, Hao Chen

**Venue:**
Social Science Research Network

**Citation Count:**
109

**Abstract:**
In this paper, we introduce Wav-KAN, an innovative neural network architecture that leverages the Wavelet Kolmogorov-Arnold Networks (Wav-KAN) framework to enhance interpretability and performance. Traditional multilayer perceptrons (MLPs) and even recent advancements like Spl-KAN face challenges related to interpretability, training speed, robustness, computational efficiency, and performance. Wav-KAN addresses these limitations by incorporating wavelet functions into the Kolmogorov-Arnold network structure, enabling the network to capture both high-frequency and low-frequency components of the input data efficiently. Wavelet-based approximations employ orthogonal or semi-orthogonal basis and maintain a balance between accurately representing the underlying data structure and avoiding overfitting to the noise. While continuous wavelet transform (CWT) has a lot of potentials, we also employed discrete wavelet transform (DWT) for multiresolution analysis, which obviated the need for recalculation of the previous steps in finding the details. Analogous to how water conforms to the shape of its container, Wav-KAN adapts to the data structure, resulting in enhanced accuracy, faster training speeds, and increased robustness compared to Spl-KAN and MLPs. Our results highlight the potential of Wav-KAN as a powerful tool for developing interpretable and high-performance neural networks, with applications spanning various fields. This work sets the stage for further exploration and implementation of Wav-KAN in frameworks such as PyTorch and TensorFlow, aiming to make wavelets in KAN as widespread as activation functions like ReLU and sigmoid in universal approximation theory (UAT). The codes to replicate the simulations are available at https://github.com/zavareh1/Wav-KAN.
       


### [Endowing Interpretability for Neural Cognitive Diagnosis by Efficient Kolmogorov-Arnold Networks](https://arxiv.org/abs/2405.14399)

**Authors:**
Shangshang Yang, Linrui Qin, Xiaoshan Yu

**Citation Count:**
10

**Abstract:**
In the realm of intelligent education, cognitive diagnosis plays a crucial role in subsequent recommendation tasks attributed to the revealed students' proficiency in knowledge concepts. Although neural network-based neural cognitive diagnosis models (CDMs) have exhibited significantly better performance than traditional models, neural cognitive diagnosis is criticized for the poor model interpretability due to the multi-layer perception (MLP) employed, even with the monotonicity assumption. Therefore, this paper proposes to empower the interpretability of neural cognitive diagnosis models through efficient kolmogorov-arnold networks (KANs), named KAN2CD, where KANs are designed to enhance interpretability in two manners. Specifically, in the first manner, KANs are directly used to replace the used MLPs in existing neural CDMs; while in the second manner, the student embedding, exercise embedding, and concept embedding are directly processed by several KANs, and then their outputs are further combined and learned in a unified KAN to get final predictions. To overcome the problem of training KANs slowly, we modify the implementation of original KANs to accelerate the training. Experiments on four real-world datasets show that the proposed KA2NCD exhibits better performance than traditional CDMs, and the proposed KA2NCD still has a bit of performance leading even over the existing neural CDMs. More importantly, the learned structures of KANs enable the proposed KA2NCD to hold as good interpretability as traditional CDMs, which is superior to existing neural CDMs. Besides, the training cost of the proposed KA2NCD is competitive to existing models.
       


### [A First Look at Kolmogorov-Arnold Networks in Surrogate-assisted Evolutionary Algorithms](https://arxiv.org/abs/2405.16494)

**Authors:**
Hao Hao, Xiaoqun Zhang, Bingdong Li, Aimin Zhou

**Citation Count:**
6

**Abstract:**
Surrogate-assisted Evolutionary Algorithm (SAEA) is an essential method for solving expensive expensive problems. Utilizing surrogate models to substitute the optimization function can significantly reduce reliance on the function evaluations during the search process, thereby lowering the optimization costs. The construction of surrogate models is a critical component in SAEAs, with numerous machine learning algorithms playing a pivotal role in the model-building phase. This paper introduces Kolmogorov-Arnold Networks (KANs) as surrogate models within SAEAs, examining their application and effectiveness. We employ KANs for regression and classification tasks, focusing on the selection of promising solutions during the search process, which consequently reduces the number of expensive function evaluations. Experimental results indicate that KANs demonstrate commendable performance within SAEAs, effectively decreasing the number of function calls and enhancing the optimization efficiency. The relevant code is publicly accessible and can be found in the GitHub repository.
       


### [An Innovative Networks in Federated Learning](https://arxiv.org/abs/2405.17836)

**Authors:**
Zavareh Bozorgasl, Hao Chen

**Citation Count:**
2

**Abstract:**
This paper presents the development and application of Wavelet Kolmogorov-Arnold Networks (Wav-KAN) in federated learning. We implemented Wav-KAN \cite{wav-kan} in the clients. Indeed, we have considered both continuous wavelet transform (CWT) and also discrete wavelet transform (DWT) to enable multiresolution capabaility which helps in heteregeneous data distribution across clients. Extensive experiments were conducted on different datasets, demonstrating Wav-KAN's superior performance in terms of interpretability, computational speed, training and test accuracy. Our federated learning algorithm integrates wavelet-based activation functions, parameterized by weight, scale, and translation, to enhance local and global model performance. Results show significant improvements in computational efficiency, robustness, and accuracy, highlighting the effectiveness of wavelet selection in scalable neural network design.
       


### [DeepOKAN: Deep Operator Network Based on Kolmogorov Arnold Networks for Mechanics Problems](https://arxiv.org/abs/2405.19143)

**Authors:**
Diab W. Abueidda, Panos Pantidis, Mostafa E. Mobasher

**Venue:**
Computer Methods in Applied Mechanics and Engineering

**Citation Count:**
63

**Abstract:**
The modern digital engineering design often requires costly repeated simulations for different scenarios. The prediction capability of neural networks (NNs) makes them suitable surrogates for providing design insights. However, only a few NNs can efficiently handle complex engineering scenario predictions. We introduce a new version of the neural operators called DeepOKAN, which utilizes Kolmogorov Arnold networks (KANs) rather than the conventional neural network architectures. Our DeepOKAN uses Gaussian radial basis functions (RBFs) rather than the B-splines. RBFs offer good approximation properties and are typically computationally fast. The KAN architecture, combined with RBFs, allows DeepOKANs to represent better intricate relationships between input parameters and output fields, resulting in more accurate predictions across various mechanics problems. Specifically, we evaluate DeepOKAN's performance on several mechanics problems, including 1D sinusoidal waves, 2D orthotropic elasticity, and transient Poisson's problem, consistently achieving lower training losses and more accurate predictions compared to traditional DeepONets. This approach should pave the way for further improving the performance of neural operators.
       


## June
### [Kolmogorov-Arnold Network for Satellite Image Classification in Remote Sensing](https://arxiv.org/abs/2406.00600)

**Author:**
Minjong Cheon

**Citation Count:**
47

**Abstract:**
In this research, we propose the first approach for integrating the Kolmogorov-Arnold Network (KAN) with various pre-trained Convolutional Neural Network (CNN) models for remote sensing (RS) scene classification tasks using the EuroSAT dataset. Our novel methodology, named KCN, aims to replace traditional Multi-Layer Perceptrons (MLPs) with KAN to enhance classification performance. We employed multiple CNN-based models, including VGG16, MobileNetV2, EfficientNet, ConvNeXt, ResNet101, and Vision Transformer (ViT), and evaluated their performance when paired with KAN. Our experiments demonstrated that KAN achieved high accuracy with fewer training epochs and parameters. Specifically, ConvNeXt paired with KAN showed the best performance, achieving 94% accuracy in the first epoch, which increased to 96% and remained consistent across subsequent epochs. The results indicated that KAN and MLP both achieved similar accuracy, with KAN performing slightly better in later epochs. By utilizing the EuroSAT dataset, we provided a robust testbed to investigate whether KAN is suitable for remote sensing classification tasks. Given that KAN is a novel algorithm, there is substantial capacity for further development and optimization, suggesting that KCN offers a promising alternative for efficient image analysis in the RS field.
       


### [Enhancing Graph Collaborative Filtering with FourierKAN Feature Transformation](https://arxiv.org/abs/2406.01034)

**Authors:**
Jinfeng Xu, Zheyu Chen, Jinze Li, Shuo Yang, Wei Wang, Xiping Hu, Edith Ngai

**Citation Count:**
67

**Abstract:**
Graph Collaborative Filtering (GCF) has emerged as a dominant paradigm in modern recommendation systems, excelling at modeling complex user-item interactions and capturing high-order collaborative signals through graph-structured learning. Most existing GCF models predominantly rely on simplified graph architectures like LightGCN, which strategically remove feature transformation and activation functions from vanilla graph convolution networks. Through systematic analysis, we reveal that feature transformation in message propagation can enhance model representation, though at the cost of increased training difficulty. To this end, we propose FourierKAN-GCF, a novel GCN framework that adopts Fourier Kolmogorov-Arnold Networks as efficient transformation modules within graph propagation layers. This design enhances model representation while decreasing training difficulty. Our FourierKAN-GCF can achieve higher recommendation performance than most widely used GCF backbone models. In addition, it can be integrated into existing advanced self-supervised models as a backbone, replacing their original backbone to achieve enhanced performance. Extensive experiments on three public datasets demonstrate the superiority of FourierKAN-GCF.
       


### [iKAN: Global Incremental Learning with KAN for Human Activity Recognition Across Heterogeneous Datasets](https://arxiv.org/abs/2406.01646)

**Authors:**
Mengxi Liu, Sizhen Bian, Bo Zhou, Paul Lukowicz

**Venue:**
International Workshop on the Semantic Web

**Citation Count:**
20

**Abstract:**
This work proposes an incremental learning (IL) framework for wearable sensor human activity recognition (HAR) that tackles two challenges simultaneously: catastrophic forgetting and non-uniform inputs. The scalable framework, iKAN, pioneers IL with Kolmogorov-Arnold Networks (KAN) to replace multi-layer perceptrons as the classifier that leverages the local plasticity and global stability of splines. To adapt KAN for HAR, iKAN uses task-specific feature branches and a feature redistribution layer. Unlike existing IL methods that primarily adjust the output dimension or the number of classifier nodes to adapt to new tasks, iKAN focuses on expanding the feature extraction branches to accommodate new inputs from different sensor modalities while maintaining consistent dimensions and the number of classifier outputs. Continual learning across six public HAR datasets demonstrated the iKAN framework's incremental learning performance, with a last performance of 84.9\% (weighted F1 score) and an average incremental performance of 81.34\%, which significantly outperforms the two existing incremental learning methods, such as EWC (51.42\%) and experience replay (59.92\%).
       


### [ReLU-KAN: New Kolmogorov-Arnold Networks that Only Need Matrix Addition, Dot Multiplication, and ReLU](https://arxiv.org/abs/2406.02075)

**Authors:**
Qi Qiu, Tao Zhu, Helin Gong, Liming Chen, Huansheng Ning

**Citation Count:**
25

**Abstract:**
Limited by the complexity of basis function (B-spline) calculations, Kolmogorov-Arnold Networks (KAN) suffer from restricted parallel computing capability on GPUs. This paper proposes a novel ReLU-KAN implementation that inherits the core idea of KAN. By adopting ReLU (Rectified Linear Unit) and point-wise multiplication, we simplify the design of KAN's basis function and optimize the computation process for efficient CUDA computing. The proposed ReLU-KAN architecture can be readily implemented on existing deep learning frameworks (e.g., PyTorch) for both inference and training. Experimental results demonstrate that ReLU-KAN achieves a 20x speedup compared to traditional KAN with 4-layer networks. Furthermore, ReLU-KAN exhibits a more stable training process with superior fitting ability while preserving the "catastrophic forgetting avoidance" property of KAN. You can get the code in https://github.com/quiqi/relu_kan
       


### [A Temporal Kolmogorov-Arnold Transformer for Time Series Forecasting](https://arxiv.org/abs/2406.02486)

**Authors:**
Remi Genet, Hugo Inzirillo

**Citation Count:**
43

**Abstract:**
Capturing complex temporal patterns and relationships within multivariate data streams is a difficult task. We propose the Temporal Kolmogorov-Arnold Transformer (TKAT), a novel attention-based architecture designed to address this task using Temporal Kolmogorov-Arnold Networks (TKANs). Inspired by the Temporal Fusion Transformer (TFT), TKAT emerges as a powerful encoder-decoder model tailored to handle tasks in which the observed part of the features is more important than the a priori known part. This new architecture combined the theoretical foundation of the Kolmogorov-Arnold representation with the power of transformers. TKAT aims to simplify the complex dependencies inherent in time series, making them more "interpretable". The use of transformer architecture in this framework allows us to capture long-range dependencies through self-attention mechanisms.
       


### [Kolmogorov-Arnold Networks for Time Series: Bridging Predictive Power and Interpretability](https://arxiv.org/abs/2406.02496)

**Authors:**
Kunpeng Xu, Lifei Chen, Shengrui Wang

**Citation Count:**
59

**Abstract:**
Kolmogorov-Arnold Networks (KAN) is a groundbreaking model recently proposed by the MIT team, representing a revolutionary approach with the potential to be a game-changer in the field. This innovative concept has rapidly garnered worldwide interest within the AI community. Inspired by the Kolmogorov-Arnold representation theorem, KAN utilizes spline-parametrized univariate functions in place of traditional linear weights, enabling them to dynamically learn activation patterns and significantly enhancing interpretability. In this paper, we explore the application of KAN to time series forecasting and propose two variants: T-KAN and MT-KAN. T-KAN is designed to detect concept drift within time series and can explain the nonlinear relationships between predictions and previous time steps through symbolic regression, making it highly interpretable in dynamically changing environments. MT-KAN, on the other hand, improves predictive performance by effectively uncovering and leveraging the complex relationships among variables in multivariate time series. Experiments validate the effectiveness of these approaches, demonstrating that T-KAN and MT-KAN significantly outperform traditional methods in time series forecasting tasks, not only enhancing predictive accuracy but also improving model interpretability. This research opens new avenues for adaptive forecasting models, highlighting the potential of KAN as a powerful and interpretable tool in predictive analytics.
       


### [Exploring the Potential of Polynomial Basis Functions in Kolmogorov-Arnold Networks: A Comparative Study of Different Groups of Polynomials](https://arxiv.org/abs/2406.02583)

**Author:**
Seyd Teymoor Seydi

**Citation Count:**
17

**Abstract:**
This paper presents a comprehensive survey of 18 distinct polynomials and their potential applications in Kolmogorov-Arnold Network (KAN) models as an alternative to traditional spline-based methods. The polynomials are classified into various groups based on their mathematical properties, such as orthogonal polynomials, hypergeometric polynomials, q-polynomials, Fibonacci-related polynomials, combinatorial polynomials, and number-theoretic polynomials. The study aims to investigate the suitability of these polynomials as basis functions in KAN models for complex tasks like handwritten digit classification on the MNIST dataset. The performance metrics of the KAN models, including overall accuracy, Kappa, and F1 score, are evaluated and compared. The Gottlieb-KAN model achieves the highest performance across all metrics, suggesting its potential as a suitable choice for the given task. However, further analysis and tuning of these polynomials on more complex datasets are necessary to fully understand their capabilities in KAN models. The source code for the implementation of these KAN models is available at https://github.com/seydi1370/Basis_Functions .
       


### [Leveraging KANs For Enhanced Deep Koopman Operator Discovery](https://arxiv.org/abs/2406.02875)

**Authors:**
George Nehma, Madhur Tiwari

**Citation Count:**
11

**Abstract:**
Multi-layer perceptrons (MLP's) have been extensively utilized in discovering Deep Koopman operators for linearizing nonlinear dynamics. With the emergence of Kolmogorov-Arnold Networks (KANs) as a more efficient and accurate alternative to the MLP Neural Network, we propose a comparison of the performance of each network type in the context of learning Koopman operators with control. In this work, we propose a KANs-based deep Koopman framework with applications to an orbital Two-Body Problem (2BP) and the pendulum for data-driven discovery of linear system dynamics. KANs were found to be superior in nearly all aspects of training; learning 31 times faster, being 15 times more parameter efficiency, and predicting 1.25 times more accurately as compared to the MLP Deep Neural Networks (DNNs) in the case of the 2BP. Thus, KANs shows potential for being an efficient tool in the development of Deep Koopman Theory.
       


### [A comprehensive and FAIR comparison between MLP and KAN representations for differential equations and operator networks](https://arxiv.org/abs/2406.02917)

**Authors:**
Khemraj Shukla, Juan Diego Toscano, Zhicheng Wang, Zongren Zou, George Em Karniadakis

**Venue:**
Computer Methods in Applied Mechanics and Engineering

**Citation Count:**
80

**Abstract:**
Kolmogorov-Arnold Networks (KANs) were recently introduced as an alternative representation model to MLP. Herein, we employ KANs to construct physics-informed machine learning models (PIKANs) and deep operator models (DeepOKANs) for solving differential equations for forward and inverse problems. In particular, we compare them with physics-informed neural networks (PINNs) and deep operator networks (DeepONets), which are based on the standard MLP representation. We find that although the original KANs based on the B-splines parameterization lack accuracy and efficiency, modified versions based on low-order orthogonal polynomials have comparable performance to PINNs and DeepONet although they still lack robustness as they may diverge for different random seeds or higher order orthogonal polynomials. We visualize their corresponding loss landscapes and analyze their learning dynamics using information bottleneck theory. Our study follows the FAIR principles so that other researchers can use our benchmarks to further advance this emerging topic.
       


### [U-KAN Makes Strong Backbone for Medical Image Segmentation and Generation](https://arxiv.org/abs/2406.02918)

**Authors:**
Chenxin Li, Xinyu Liu, Wuyang Li, Cheng Wang, Hengyu Liu, Yifan Liu, Zhen Chen, Yixuan Yuan

**Venue:**
AAAI Conference on Artificial Intelligence

**Citation Count:**
130

**Abstract:**
U-Net has become a cornerstone in various visual applications such as image segmentation and diffusion probability models. While numerous innovative designs and improvements have been introduced by incorporating transformers or MLPs, the networks are still limited to linearly modeling patterns as well as the deficient interpretability. To address these challenges, our intuition is inspired by the impressive results of the Kolmogorov-Arnold Networks (KANs) in terms of accuracy and interpretability, which reshape the neural network learning via the stack of non-linear learnable activation functions derived from the Kolmogorov-Anold representation theorem. Specifically, in this paper, we explore the untapped potential of KANs in improving backbones for vision tasks. We investigate, modify and re-design the established U-Net pipeline by integrating the dedicated KAN layers on the tokenized intermediate representation, termed U-KAN. Rigorous medical image segmentation benchmarks verify the superiority of U-KAN by higher accuracy even with less computation cost. We further delved into the potential of U-KAN as an alternative U-Net noise predictor in diffusion models, demonstrating its applicability in generating task-oriented model architectures. These endeavours unveil valuable insights and sheds light on the prospect that with U-KAN, you can make strong backbone for medical image segmentation and generation. Project page:\url{https://yes-u-kan.github.io/}.
       


### [GKAN: Graph Kolmogorov-Arnold Networks](https://arxiv.org/abs/2406.06470)

**Authors:**
Mehrdad Kiamari, Mohammad Kiamari, Bhaskar Krishnamachari

**Citation Count:**
42

**Abstract:**
We introduce Graph Kolmogorov-Arnold Networks (GKAN), an innovative neural network architecture that extends the principles of the recently proposed Kolmogorov-Arnold Networks (KAN) to graph-structured data. By adopting the unique characteristics of KANs, notably the use of learnable univariate functions instead of fixed linear weights, we develop a powerful model for graph-based learning tasks. Unlike traditional Graph Convolutional Networks (GCNs) that rely on a fixed convolutional architecture, GKANs implement learnable spline-based functions between layers, transforming the way information is processed across the graph structure. We present two different ways to incorporate KAN layers into GKAN: architecture 1 -- where the learnable functions are applied to input features after aggregation and architecture 2 -- where the learnable functions are applied to input features before aggregation. We evaluate GKAN empirically using a semi-supervised graph learning task on a real-world dataset (Cora). We find that architecture generally performs better. We find that GKANs achieve higher accuracy in semi-supervised learning tasks on graphs compared to the traditional GCN model. For example, when considering 100 features, GCN provides an accuracy of 53.5 while a GKAN with a comparable number of parameters gives an accuracy of 61.76; with 200 features, GCN provides an accuracy of 61.24 while a GKAN with a comparable number of parameters gives an accuracy of 67.66. We also present results on the impact of various parameters such as the number of hidden nodes, grid-size, and the polynomial-degree of the spline on the performance of GKAN.
       


### [fKAN: Fractional Kolmogorov-Arnold Networks with trainable Jacobi basis functions](https://arxiv.org/abs/2406.07456)

**Author:**
Alireza Afzal Aghaei

**Venue:**
Neurocomputing

**Citation Count:**
50

**Abstract:**
Recent advancements in neural network design have given rise to the development of Kolmogorov-Arnold Networks (KANs), which enhance speed, interpretability, and precision. This paper presents the Fractional Kolmogorov-Arnold Network (fKAN), a novel neural network architecture that incorporates the distinctive attributes of KANs with a trainable adaptive fractional-orthogonal Jacobi function as its basis function. By leveraging the unique mathematical properties of fractional Jacobi functions, including simple derivative formulas, non-polynomial behavior, and activity for both positive and negative input values, this approach ensures efficient learning and enhanced accuracy. The proposed architecture is evaluated across a range of tasks in deep learning and physics-informed deep learning. Precision is tested on synthetic regression data, image classification, image denoising, and sentiment analysis. Additionally, the performance is measured on various differential equations, including ordinary, partial, and fractional delay differential equations. The results demonstrate that integrating fractional Jacobi functions into KANs significantly improves training speed and performance across diverse fields and applications.
       


### [Unveiling the Power of Wavelets: A Wavelet-based Kolmogorov-Arnold Network for Hyperspectral Image Classification](https://arxiv.org/abs/2406.07869)

**Authors:**
Seyd Teymoor Seydi, Zavareh Bozorgasl, Hao Chen

**Citation Count:**
27

**Abstract:**
Hyperspectral image classification is a crucial but challenging task due to the high dimensionality and complex spatial-spectral correlations inherent in hyperspectral data. This paper employs Wavelet-based Kolmogorov-Arnold Network (wav-kan) architecture tailored for efficient modeling of these intricate dependencies. Inspired by the Kolmogorov-Arnold representation theorem, Wav-KAN incorporates wavelet functions as learnable activation functions, enabling non-linear mapping of the input spectral signatures. The wavelet-based activation allows Wav-KAN to effectively capture multi-scale spatial and spectral patterns through dilations and translations. Experimental evaluation on three benchmark hyperspectral datasets (Salinas, Pavia, Indian Pines) demonstrates the superior performance of Wav-KAN compared to traditional multilayer perceptrons (MLPs) and the recently proposed Spline-based KAN (Spline-KAN) model. In this work we are: (1) conducting more experiments on additional hyperspectral datasets (Pavia University, WHU-Hi, and Urban Hyperspectral Image) to further validate the generalizability of Wav-KAN; (2) developing a multiresolution Wav-KAN architecture to capture scale-invariant features; (3) analyzing the effect of dimensional reduction techniques on classification performance; (4) exploring optimization methods for tuning the hyperparameters of KAN models; and (5) comparing Wav-KAN with other state-of-the-art models in hyperspectral image classification.
       


### [Suitability of KANs for Computer Vision: A preliminary investigation](https://arxiv.org/abs/2406.09087)

**Authors:**
Basim Azam, Naveed Akhtar

**Citation Count:**
30

**Abstract:**
Kolmogorov-Arnold Networks (KANs) introduce a paradigm of neural modeling that implements learnable functions on the edges of the networks, diverging from the traditional node-centric activations in neural networks. This work assesses the applicability and efficacy of KANs in visual modeling, focusing on fundamental recognition and segmentation tasks. We mainly analyze the performance and efficiency of different network architectures built using KAN concepts along with conventional building blocks of convolutional and linear layers, enabling a comparative analysis with the conventional models. Our findings are aimed at contributing to understanding the potential of KANs in computer vision, highlighting both their strengths and areas for further research. Our evaluation point toward the fact that while KAN-based architectures perform in line with the original claims, it may often be important to employ more complex functions on the network edges to retain the performance advantage of KANs on more complex visual data.
       


### [SCKansformer: Fine-Grained Classification of Bone Marrow Cells via Kansformer Backbone and Hierarchical Attention Mechanisms](https://arxiv.org/abs/2406.09931)

**Authors:**
Yifei Chen, Zhu Zhu, Shenghao Zhu, Linwei Qiu, Binfeng Zou, Fan Jia, Yunpeng Zhu, Chenyan Zhang, Zhaojie Fang, Feiwei Qin, Jin Fan, Changmiao Wang, Yu Gao, Gang Yu

**Abstract:**
The incidence and mortality rates of malignant tumors, such as acute leukemia, have risen significantly. Clinically, hospitals rely on cytological examination of peripheral blood and bone marrow smears to diagnose malignant tumors, with accurate blood cell counting being crucial. Existing automated methods face challenges such as low feature expression capability, poor interpretability, and redundant feature extraction when processing high-dimensional microimage data. We propose a novel fine-grained classification model, SCKansformer, for bone marrow blood cells, which addresses these challenges and enhances classification accuracy and efficiency. The model integrates the Kansformer Encoder, SCConv Encoder, and Global-Local Attention Encoder. The Kansformer Encoder replaces the traditional MLP layer with the KAN, improving nonlinear feature representation and interpretability. The SCConv Encoder, with its Spatial and Channel Reconstruction Units, enhances feature representation and reduces redundancy. The Global-Local Attention Encoder combines Multi-head Self-Attention with a Local Part module to capture both global and local features. We validated our model using the Bone Marrow Blood Cell Fine-Grained Classification Dataset (BMCD-FGCD), comprising over 10,000 samples and nearly 40 classifications, developed with a partner hospital. Comparative experiments on our private dataset, as well as the publicly available PBC and ALL-IDB datasets, demonstrate that SCKansformer outperforms both typical and advanced microcell classification methods across all datasets. Our source code and private BMCD-FGCD dataset are available at https://github.com/JustlfC03/SCKansformer.
       


### [Kolmogorov Arnold Informed neural network: A physics-informed deep learning framework for solving forward and inverse problems based on Kolmogorov Arnold Networks](https://arxiv.org/abs/2406.11045)

**Authors:**
Yizheng Wang, Jia Sun, Jinshuai Bai, Cosmin Anitescu, Mohammad Sadegh Eshaghi, Xiaoying Zhuang, Timon Rabczuk, Yinghua Liu

**Venue:**
Computer Methods in Applied Mechanics and Engineering

**Citation Count:**
39

**Abstract:**
AI for partial differential equations (PDEs) has garnered significant attention, particularly with the emergence of Physics-informed neural networks (PINNs). The recent advent of Kolmogorov-Arnold Network (KAN) indicates that there is potential to revisit and enhance the previously MLP-based PINNs. Compared to MLPs, KANs offer interpretability and require fewer parameters. PDEs can be described in various forms, such as strong form, energy form, and inverse form. While mathematically equivalent, these forms are not computationally equivalent, making the exploration of different PDE formulations significant in computational physics. Thus, we propose different PDE forms based on KAN instead of MLP, termed Kolmogorov-Arnold-Informed Neural Network (KINN) for solving forward and inverse problems. We systematically compare MLP and KAN in various numerical examples of PDEs, including multi-scale, singularity, stress concentration, nonlinear hyperelasticity, heterogeneous, and complex geometry problems. Our results demonstrate that KINN significantly outperforms MLP regarding accuracy and convergence speed for numerous PDEs in computational solid mechanics, except for the complex geometry problem. This highlights KINN's potential for more efficient and accurate PDE solutions in AI for PDEs.
       


### [BSRBF-KAN: A combination of B-splines and Radial Basis Functions in Kolmogorov-Arnold Networks](https://arxiv.org/abs/2406.11173)

**Author:**
Hoang-Thang Ta

**Citation Count:**
30

**Abstract:**
In this paper, we introduce BSRBF-KAN, a Kolmogorov Arnold Network (KAN) that combines B-splines and radial basis functions (RBFs) to fit input vectors during data training. We perform experiments with BSRBF-KAN, multi-layer perception (MLP), and other popular KANs, including EfficientKAN, FastKAN, FasterKAN, and GottliebKAN over the MNIST and Fashion-MNIST datasets. BSRBF-KAN shows stability in 5 training runs with a competitive average accuracy of 97.55% on MNIST and 89.33% on Fashion-MNIST and obtains convergence better than other networks. We expect BSRBF-KAN to open many combinations of mathematical functions to design KANs. Our repo is publicly available at: https://github.com/hoangthangta/BSRBF_KAN.
       


### [Realizability-Informed Machine Learning for Turbulence Anisotropy Mappings](https://arxiv.org/abs/2406.11603)

**Authors:**
Ryley McConkey, Nikhila Kalia, Eugene Yee, Fue-Sang Lien

**Citation Count:**
1

**Abstract:**
Within the context of machine learning-based closure mappings for RANS turbulence modelling, physical realizability is often enforced using ad-hoc postprocessing of the predicted anisotropy tensor. In this study, we address the realizability issue via a new physics-based loss function that penalizes non-realizable results during training, thereby embedding a preference for realizable predictions into the model. Additionally, we propose a new framework for data-driven turbulence modelling which retains the stability and conditioning of optimal eddy viscosity-based approaches while embedding equivariance. Several modifications to the tensor basis neural network to enhance training and testing stability are proposed. We demonstrate the conditioning, stability, and generalization of the new framework and model architecture on three flows: flow over a flat plate, flow over periodic hills, and flow through a square duct. The realizability-informed loss function is demonstrated to significantly increase the number of realizable predictions made by the model when generalizing to a new flow configuration. Altogether, the proposed framework enables the training of stable and equivariant anisotropy mappings, with more physically realizable predictions on new data. We make our code available for use and modification by others. Moreover, as part of this study, we explore the applicability of Kolmogorov-Arnold Networks (KAN) to turbulence modeling, assessing its potential to address non-linear mappings in the anisotropy tensor predictions and demonstrating promising results for the flat plate case.
       


### [Initial Investigation of Kolmogorov-Arnold Networks (KANs) as Feature Extractors for IMU Based Human Activity Recognition](https://arxiv.org/abs/2406.11914)

**Authors:**
Mengxi Liu, Daniel Geißler, Dominique Nshimyimana, Sizhen Bian, Bo Zhou, Paul Lukowicz

**Venue:**
Companion of the 2024 on ACM International Joint Conference on Pervasive and Ubiquitous Computing

**Citation Count:**
11

**Abstract:**
In this work, we explore the use of a novel neural network architecture, the Kolmogorov-Arnold Networks (KANs) as feature extractors for sensor-based (specifically IMU) Human Activity Recognition (HAR). Where conventional networks perform a parameterized weighted sum of the inputs at each node and then feed the result into a statically defined nonlinearity, KANs perform non-linear computations represented by B-SPLINES on the edges leading to each node and then just sum up the inputs at the node. Instead of learning weights, the system learns the spline parameters. In the original work, such networks have been shown to be able to more efficiently and exactly learn sophisticated real valued functions e.g. in regression or PDE solution. We hypothesize that such an ability is also advantageous for computing low-level features for IMU-based HAR. To this end, we have implemented KAN as the feature extraction architecture for IMU-based human activity recognition tasks, including four architecture variations. We present an initial performance investigation of the KAN feature extractor on four public HAR datasets. It shows that the KAN-based feature extractor outperforms CNN-based extractors on all datasets while being more parameter efficient.
       


### [Convolutional Kolmogorov-Arnold Networks](https://arxiv.org/abs/2406.13155)

**Authors:**
Alexander Dylan Bodner, Antonio Santiago Tepsich, Jack Natan Spolski, Santiago Pourteau

**Citation Count:**
68

**Abstract:**
In this paper, we present Convolutional Kolmogorov-Arnold Networks, a novel architecture that integrates the learnable spline-based activation functions of Kolmogorov-Arnold Networks (KANs) into convolutional layers. By replacing traditional fixed-weight kernels with learnable non-linear functions, Convolutional KANs offer a significant improvement in parameter efficiency and expressive power over standard Convolutional Neural Networks (CNNs). We empirically evaluate Convolutional KANs on the Fashion-MNIST dataset, demonstrating competitive accuracy with up to 50% fewer parameters compared to baseline classic convolutions. This suggests that the KAN Convolution can effectively capture complex spatial relationships with fewer resources, offering a promising alternative for parameter-efficient deep learning models.
       


### [GraphKAN: Enhancing Feature Extraction with Graph Kolmogorov Arnold Networks](https://arxiv.org/abs/2406.13597)

**Authors:**
Fan Zhang, Xin Zhang

**Citation Count:**
29

**Abstract:**
Massive number of applications involve data with underlying relationships embedded in non-Euclidean space. Graph neural networks (GNNs) are utilized to extract features by capturing the dependencies within graphs. Despite groundbreaking performances, we argue that Multi-layer perceptrons (MLPs) and fixed activation functions impede the feature extraction due to information loss. Inspired by Kolmogorov Arnold Networks (KANs), we make the first attempt to GNNs with KANs. We discard MLPs and activation functions, and instead used KANs for feature extraction. Experiments demonstrate the effectiveness of GraphKAN, emphasizing the potential of KANs as a powerful tool. Code is available at https://github.com/Ryanfzhang/GraphKan.
       


### [rKAN: Rational Kolmogorov-Arnold Networks](https://arxiv.org/abs/2406.14495)

**Author:**
Alireza Afzal Aghaei

**Citation Count:**
19

**Abstract:**
The development of Kolmogorov-Arnold networks (KANs) marks a significant shift from traditional multi-layer perceptrons in deep learning. Initially, KANs employed B-spline curves as their primary basis function, but their inherent complexity posed implementation challenges. Consequently, researchers have explored alternative basis functions such as Wavelets, Polynomials, and Fractional functions. In this research, we explore the use of rational functions as a novel basis function for KANs. We propose two different approaches based on Pade approximation and rational Jacobi functions as trainable basis functions, establishing the rational KAN (rKAN). We then evaluate rKAN's performance in various deep learning and physics-informed tasks to demonstrate its practicality and effectiveness in function approximation.
       


### [A Benchmarking Study of Kolmogorov-Arnold Networks on Tabular Data](https://arxiv.org/abs/2406.14529)

**Authors:**
Eleonora Poeta, Flavio Giobergia, Eliana Pastor, Tania Cerquitelli, Elena Baralis

**Venue:**
Advanced Industrial Conference on Telecommunications

**Citation Count:**
21

**Abstract:**
Kolmogorov-Arnold Networks (KANs) have very recently been introduced into the world of machine learning, quickly capturing the attention of the entire community. However, KANs have mostly been tested for approximating complex functions or processing synthetic data, while a test on real-world tabular datasets is currently lacking. In this paper, we present a benchmarking study comparing KANs and Multi-Layer Perceptrons (MLPs) on tabular datasets. The study evaluates task performance and training times. From the results obtained on the various datasets, KANs demonstrate superior or comparable accuracy and F1 scores, excelling particularly in datasets with numerous instances, suggesting robust handling of complex data. We also highlight that this performance improvement of KANs comes with a higher computational cost when compared to MLPs of comparable sizes.
       


### [Demonstrating the Efficacy of Kolmogorov-Arnold Networks in Vision Tasks](https://arxiv.org/abs/2406.14916)

**Author:**
Minjong Cheon

**Citation Count:**
39

**Abstract:**
In the realm of deep learning, the Kolmogorov-Arnold Network (KAN) has emerged as a potential alternative to multilayer projections (MLPs). However, its applicability to vision tasks has not been extensively validated. In our study, we demonstrated the effectiveness of KAN for vision tasks through multiple trials on the MNIST, CIFAR10, and CIFAR100 datasets, using a training batch size of 32. Our results showed that while KAN outperformed the original MLP-Mixer on CIFAR10 and CIFAR100, it performed slightly worse than the state-of-the-art ResNet-18. These findings suggest that KAN holds significant promise for vision tasks, and further modifications could enhance its performance in future evaluations.Our contributions are threefold: first, we showcase the efficiency of KAN-based algorithms for visual tasks; second, we provide extensive empirical assessments across various vision benchmarks, comparing KAN's performance with MLP-Mixer, CNNs, and Vision Transformers (ViT); and third, we pioneer the use of natural KAN layers in visual tasks, addressing a gap in previous research. This paper lays the foundation for future studies on KANs, highlighting their potential as a reliable alternative for image classification tasks.
       


### [How to Learn More? Exploring Kolmogorov-Arnold Networks for Hyperspectral Image Classification](https://arxiv.org/abs/2406.15719)

**Authors:**
Ali Jamali, Swalpa Kumar Roy, Danfeng Hong, Bing Lu, Pedram Ghamisi

**Venue:**
Remote Sensing

**Citation Count:**
28

**Abstract:**
Convolutional Neural Networks (CNNs) and vision transformers (ViTs) have shown excellent capability in complex hyperspectral image (HSI) classification. However, these models require a significant number of training data and are computational resources. On the other hand, modern Multi-Layer Perceptrons (MLPs) have demonstrated great classification capability. These modern MLP-based models require significantly less training data compared to CNNs and ViTs, achieving the state-of-the-art classification accuracy. Recently, Kolmogorov-Arnold Networks (KANs) were proposed as viable alternatives for MLPs. Because of their internal similarity to splines and their external similarity to MLPs, KANs are able to optimize learned features with remarkable accuracy in addition to being able to learn new features. Thus, in this study, we assess the effectiveness of KANs for complex HSI data classification. Moreover, to enhance the HSI classification accuracy obtained by the KANs, we develop and propose a Hybrid architecture utilizing 1D, 2D, and 3D KANs. To demonstrate the effectiveness of the proposed KAN architecture, we conducted extensive experiments on three newly created HSI benchmark datasets: QUH-Pingan, QUH-Tangdaowan, and QUH-Qingyun. The results underscored the competitive or better capability of the developed hybrid KAN-based model across these benchmark datasets over several other CNN- and ViT-based algorithms, including 1D-CNN, 2DCNN, 3D CNN, VGG-16, ResNet-50, EfficientNet, RNN, and ViT. The code are publicly available at (https://github.com/aj1365/HSIConvKAN)
       


### [CEST-KAN: Kolmogorov-Arnold Networks for CEST MRI Data Analysis](https://arxiv.org/abs/2406.16026)

**Authors:**
Jiawen Wang, Pei Cai, Ziyan Wang, Huabin Zhang, Jianpan Huang

**Citation Count:**
7

**Abstract:**
Purpose: This study aims to propose and investigate the feasibility of using Kolmogorov-Arnold Network (KAN) for CEST MRI data analysis (CEST-KAN). Methods: CEST MRI data were acquired from twelve healthy volunteers at 3T. Data from ten subjects were used for training, while the remaining two were reserved for testing. The performance of multi-layer perceptron (MLP) and KAN models with the same network settings were evaluated and compared to the conventional multi-pool Lorentzian fitting (MPLF) method in generating water and multiple CEST contrasts, including amide, relayed nuclear Overhauser effect (rNOE), and magnetization transfer (MT). Results: The water and CEST maps generated by both MLP and KAN were visually comparable to the MPLF results. However, the KAN model demonstrated higher accuracy in extrapolating the CEST fitting metrics, as evidenced by the smaller validation loss during training and smaller absolute error during testing. Voxel-wise correlation analysis showed that all four CEST fitting metrics generated by KAN consistently exhibited higher Pearson coefficients than the MLP results, indicating superior performance. Moreover, the KAN models consistently outperformed the MLP models in varying hidden layer numbers despite longer training time. Conclusion: In this study, we demonstrated for the first time the feasibility of utilizing KAN for CEST MRI data analysis, highlighting its superiority over MLP in this task. The findings suggest that CEST-KAN has the potential to be a robust and reliable post-analysis tool for CEST MRI in clinical settings.
       


### [KANQAS: Kolmogorov-Arnold Network for Quantum Architecture Search](https://arxiv.org/abs/2406.17630)

**Authors:**
Akash Kundu, Aritra Sarkar, Abhishek Sadhu

**Venue:**
EPJ Quantum Technology

**Citation Count:**
31

**Abstract:**
Quantum architecture Search (QAS) is a promising direction for optimization and automated design of quantum circuits towards quantum advantage. Recent techniques in QAS emphasize Multi-Layer Perceptron (MLP)-based deep Q-networks. However, their interpretability remains challenging due to the large number of learnable parameters and the complexities involved in selecting appropriate activation functions. In this work, to overcome these challenges, we utilize the Kolmogorov-Arnold Network (KAN) in the QAS algorithm, analyzing their efficiency in the task of quantum state preparation and quantum chemistry. In quantum state preparation, our results show that in a noiseless scenario, the probability of success is 2 to 5 times higher than MLPs. In noisy environments, KAN outperforms MLPs in fidelity when approximating these states, showcasing its robustness against noise. In tackling quantum chemistry problems, we enhance the recently proposed QAS algorithm by integrating curriculum reinforcement learning with a KAN structure. This facilitates a more efficient design of parameterized quantum circuits by reducing the number of required 2-qubit gates and circuit depth. Further investigation reveals that KAN requires a significantly smaller number of learnable parameters compared to MLPs; however, the average time of executing each episode for KAN is higher.
       


### [SigKAN: Signature-Weighted Kolmogorov-Arnold Networks for Time Series](https://arxiv.org/abs/2406.17890)

**Authors:**
Hugo Inzirillo, Remi Genet

**Citation Count:**
12

**Abstract:**
We propose a novel approach that enhances multivariate function approximation using learnable path signatures and Kolmogorov-Arnold networks (KANs). We enhance the learning capabilities of these networks by weighting the values obtained by KANs using learnable path signatures, which capture important geometric features of paths. This combination allows for a more comprehensive and flexible representation of sequential and temporal data. We demonstrate through studies that our SigKANs with learnable path signatures perform better than conventional methods across a range of function approximation challenges. By leveraging path signatures in neural networks, this method offers intriguing opportunities to enhance performance in time series analysis and time series forecasting, among other fields.
       


### [Kolmogorov-Arnold Graph Neural Networks](https://arxiv.org/abs/2406.18354)

**Authors:**
Gianluca De Carlo, Andrea Mastropietro, Aris Anagnostopoulos

**Citation Count:**
28

**Abstract:**
Graph neural networks (GNNs) excel in learning from network-like data but often lack interpretability, making their application challenging in domains requiring transparent decision-making. We propose the Graph Kolmogorov-Arnold Network (GKAN), a novel GNN model leveraging spline-based activation functions on edges to enhance both accuracy and interpretability. Our experiments on five benchmark datasets demonstrate that GKAN outperforms state-of-the-art GNN models in node classification, link prediction, and graph classification tasks. In addition to the improved accuracy, GKAN's design inherently provides clear insights into the model's decision-making process, eliminating the need for post-hoc explainability techniques. This paper discusses the methodology, performance, and interpretability of GKAN, highlighting its potential for applications in domains where interpretability is crucial.
       


### [KAGNNs: Kolmogorov-Arnold Networks meet Graph Learning](https://arxiv.org/abs/2406.18380)

**Authors:**
Roman Bresson, Giannis Nikolentzos, George Panagopoulos, Michail Chatzianastasis, Jun Pang, Michalis Vazirgiannis

**Citation Count:**
49

**Abstract:**
In recent years, Graph Neural Networks (GNNs) have become the de facto tool for learning node and graph representations. Most GNNs typically consist of a sequence of neighborhood aggregation (a.k.a., message-passing) layers, within which the representation of each node is updated based on those of its neighbors. The most expressive message-passing GNNs can be obtained through the use of the sum aggregator and of MLPs for feature transformation, thanks to their universal approximation capabilities. However, the limitations of MLPs recently motivated the introduction of another family of universal approximators, called Kolmogorov-Arnold Networks (KANs) which rely on a different representation theorem. In this work, we compare the performance of KANs against that of MLPs on graph learning tasks. We implement three new KAN-based GNN layers, inspired respectively by the GCN, GAT and GIN layers. We evaluate two different implementations of KANs using two distinct base families of functions, namely B-splines and radial basis functions. We perform extensive experiments on node classification, link prediction, graph classification and graph regression datasets. Our results indicate that KANs are on-par with or better than MLPs on all tasks studied in this paper. We also show that the size and training speed of RBF-based KANs is only marginally higher than for MLPs, making them viable alternatives. Code available at https://github.com/RomanBresson/KAGNN.
       


### [Finite basis Kolmogorov-Arnold networks: domain decomposition for data-driven and physics-informed problems](https://arxiv.org/abs/2406.19662)

**Authors:**
Amanda A. Howard, Bruno Jacob, Sarah Helfert, Alexander Heinlein, Panos Stinis

**Citation Count:**
28

**Abstract:**
Kolmogorov-Arnold networks (KANs) have attracted attention recently as an alternative to multilayer perceptrons (MLPs) for scientific machine learning. However, KANs can be expensive to train, even for relatively small networks. Inspired by finite basis physics-informed neural networks (FBPINNs), in this work, we develop a domain decomposition method for KANs that allows for several small KANs to be trained in parallel to give accurate solutions for multiscale problems. We show that finite basis KANs (FBKANs) can provide accurate results with noisy data and for physics-informed training.
       


## July
### [SpectralKAN: Weighted Activation Distribution Kolmogorov-Arnold Network for Hyperspectral Image Change Detection](https://arxiv.org/abs/2407.00949)

**Authors:**
Yanheng Wang, Xiaohan Yu, Yongsheng Gao, Jianjun Sha, Jian Wang, Shiyong Yan, Kai Qin, Yonggang Zhang, Lianru Gao

**Citation Count:**
7

**Abstract:**
Kolmogorov-Arnold networks (KANs) represent data features by learning the activation functions and demonstrate superior accuracy with fewer parameters, FLOPs, GPU memory usage (Memory), shorter training time (TraT), and testing time (TesT) when handling low-dimensional data. However, when applied to high-dimensional data, which contains significant redundant information, the current activation mechanism of KANs leads to unnecessary computations, thereby reducing computational efficiency. KANs require reshaping high-dimensional data into a one-dimensional tensor as input, which inevitably results in the loss of dimensional information. To address these limitations, we propose weighted activation distribution KANs (WKANs), which reduce the frequency of activations per node and distribute node information into different output nodes through weights to avoid extracting redundant information. Furthermore, we introduce a multilevel tensor splitting framework (MTSF), which decomposes high-dimensional data to extract features from each dimension independently and leverages tensor-parallel computation to significantly improve the computational efficiency of WKANs on high-dimensional data. In this paper, we design SpectralKAN for hyperspectral image change detection using the proposed MTSF. SpectralKAN demonstrates outstanding performance across five datasets, achieving an overall accuracy (OA) of 0.9801 and a Kappa coefficient (K) of 0.9514 on the Farmland dataset, with only 8 k parameters, 0.07 M FLOPs, 911 MB Memory, 13.26 S TraT, and 2.52 S TesT, underscoring its superior accuracy-efficiency trade-off. The source code is publicly available at https://github.com/yanhengwang-heu/SpectralKAN.
       


### [Kolmogorov-Arnold Convolutions: Design Principles and Empirical Studies](https://arxiv.org/abs/2407.01092)

**Author:**
Ivan Drokin

**Citation Count:**
20

**Abstract:**
The emergence of Kolmogorov-Arnold Networks (KANs) has sparked significant interest and debate within the scientific community. This paper explores the application of KANs in the domain of computer vision (CV). We examine the convolutional version of KANs, considering various nonlinearity options beyond splines, such as Wavelet transforms and a range of polynomials. We propose a parameter-efficient design for Kolmogorov-Arnold convolutional layers and a parameter-efficient finetuning algorithm for pre-trained KAN models, as well as KAN convolutional versions of self-attention and focal modulation layers. We provide empirical evaluations conducted on MNIST, CIFAR10, CIFAR100, Tiny ImageNet, ImageNet1k, and HAM10000 datasets for image classification tasks. Additionally, we explore segmentation tasks, proposing U-Net-like architectures with KAN convolutions, and achieving state-of-the-art results on BUSI, GlaS, and CVC datasets. We summarized all of our findings in a preliminary design guide of KAN convolutional models for computer vision tasks. Furthermore, we investigate regularization techniques for KANs. All experimental code and implementations of convolutional layers and models, pre-trained on ImageNet1k weights are available on GitHub via this https://github.com/IvanDrokin/torch-conv-kan
       


### [SineKAN: Kolmogorov-Arnold Networks Using Sinusoidal Activation Functions](https://arxiv.org/abs/2407.04149)

**Authors:**
Eric A. F. Reinhardt, P. R. Dinesh, Sergei Gleyzer

**Venue:**
Frontiers Artif. Intell.

**Citation Count:**
12

**Abstract:**
Recent work has established an alternative to traditional multi-layer perceptron neural networks in the form of Kolmogorov-Arnold Networks (KAN). The general KAN framework uses learnable activation functions on the edges of the computational graph followed by summation on nodes. The learnable edge activation functions in the original implementation are basis spline functions (B-Spline). Here, we present a model in which learnable grids of B-Spline activation functions are replaced by grids of re-weighted sine functions (SineKAN). We evaluate numerical performance of our model on a benchmark vision task. We show that our model can perform better than or comparable to B-Spline KAN models and an alternative KAN implementation based on periodic cosine and sine functions representing a Fourier Series. Further, we show that SineKAN has numerical accuracy that could scale comparably to dense neural networks (DNNs). Compared to the two baseline KAN models, SineKAN achieves a substantial speed increase at all hidden layer sizes, batch sizes, and depths. Current advantage of DNNs due to hardware and software optimizations are discussed along with theoretical scaling. Additionally, properties of SineKAN compared to other KAN implementations and current limitations are also discussed
       


### [KAN-ODEs: Kolmogorov-Arnold Network Ordinary Differential Equations for Learning Dynamical Systems and Hidden Physics](https://arxiv.org/abs/2407.04192)

**Authors:**
Benjamin C. Koenig, Suyong Kim, Sili Deng

**Venue:**
Computer Methods in Applied Mechanics and Engineering

**Citation Count:**
54

**Abstract:**
Kolmogorov-Arnold networks (KANs) as an alternative to multi-layer perceptrons (MLPs) are a recent development demonstrating strong potential for data-driven modeling. This work applies KANs as the backbone of a neural ordinary differential equation (ODE) framework, generalizing their use to the time-dependent and temporal grid-sensitive cases often seen in dynamical systems and scientific machine learning applications. The proposed KAN-ODEs retain the flexible dynamical system modeling framework of Neural ODEs while leveraging the many benefits of KANs compared to MLPs, including higher accuracy and faster neural scaling, stronger interpretability and generalizability, and lower parameter counts. First, we quantitatively demonstrated these improvements in a comprehensive study of the classical Lotka-Volterra predator-prey model. We then showcased the KAN-ODE framework's ability to learn symbolic source terms and complete solution profiles in higher-complexity and data-lean scenarios including wave propagation and shock formation, the complex Schrödinger equation, and the Allen-Cahn phase separation equation. The successful training of KAN-ODEs, and their improved performance compared to traditional Neural ODEs, implies significant potential in leveraging this novel network architecture in myriad scientific machine learning applications for discovering hidden physics and predicting dynamic evolution.
       


### [RPN: Reconciled Polynomial Network Towards Unifying PGMs, Kernel SVMs, MLP and KAN](https://arxiv.org/abs/2407.04819)

**Author:**
Jiawei Zhang

**Citation Count:**
4

**Abstract:**
In this paper, we will introduce a novel deep model named Reconciled Polynomial Network (RPN) for deep function learning. RPN has a very general architecture and can be used to build models with various complexities, capacities, and levels of completeness, which all contribute to the correctness of these models. As indicated in the subtitle, RPN can also serve as the backbone to unify different base models into one canonical representation. This includes non-deep models, like probabilistic graphical models (PGMs) - such as Bayesian network and Markov network - and kernel support vector machines (kernel SVMs), as well as deep models like the classic multi-layer perceptron (MLP) and the recent Kolmogorov-Arnold network (KAN).
  Technically, RPN proposes to disentangle the underlying function to be inferred into the inner product of a data expansion function and a parameter reconciliation function. Together with the remainder function, RPN accurately approximates the underlying functions that governs data distributions. The data expansion functions in RPN project data vectors from the input space to a high-dimensional intermediate space, specified by the expansion functions in definition. Meanwhile, RPN also introduces the parameter reconciliation functions to fabricate a small number of parameters into a higher-order parameter matrix to address the ``curse of dimensionality'' problem caused by the data expansions. Moreover, the remainder functions provide RPN with additional complementary information to reduce potential approximation errors. We conducted extensive empirical experiments on numerous benchmark datasets across multiple modalities, including continuous function datasets, discrete vision and language datasets, and classic tabular datasets, to investigate the effectiveness of RPN.
       


### [HyperKAN: Kolmogorov-Arnold Networks make Hyperspectral Image Classificators Smarter](https://arxiv.org/abs/2407.05278)

**Authors:**
Valeriy Lobanov, Nikita Firsov, Evgeny Myasnikov, Roman Khabibullin, Artem Nikonorov

**Citation Count:**
8

**Abstract:**
In traditional neural network architectures, a multilayer perceptron (MLP) is typically employed as a classification block following the feature extraction stage. However, the Kolmogorov-Arnold Network (KAN) presents a promising alternative to MLP, offering the potential to enhance prediction accuracy. In this paper, we propose the replacement of linear and convolutional layers of traditional networks with KAN-based counterparts. These modifications allowed us to significantly increase the per-pixel classification accuracy for hyperspectral remote-sensing images. We modified seven different neural network architectures for hyperspectral image classification and observed a substantial improvement in the classification accuracy across all the networks. The architectures considered in the paper include baseline MLP, state-of-the-art 1D (1DCNN) and 3D convolutional (two different 3DCNN, NM3DCNN), and transformer (SSFTT) architectures, as well as newly proposed M1DCNN. The greatest effect was achieved for convolutional networks working exclusively on spectral data, and the best classification quality was achieved using a KAN-based transformer architecture. All the experiments were conducted using seven openly available hyperspectral datasets. Our code is available at https://github.com/f-neumann77/HyperKAN.
       


### [TCKAN:A Novel Integrated Network Model for Predicting Mortality Risk in Sepsis Patients](https://arxiv.org/abs/2407.06560)

**Author:**
Fanglin Dong

**Citation Count:**
2

**Abstract:**
Sepsis poses a major global health threat, accounting for millions of deaths annually and significant economic costs. Accurately predicting the risk of mortality in sepsis patients enables early identification, promotes the efficient allocation of medical resources, and facilitates timely interventions, thereby improving patient outcomes. Current methods typically utilize only one type of data--either constant, temporal, or ICD codes. This study introduces a novel approach, the Time-Constant Kolmogorov-Arnold Network (TCKAN), which uniquely integrates temporal data, constant data, and ICD codes within a single predictive model. Unlike existing methods that typically rely on one type of data, TCKAN leverages a multi-modal data integration strategy, resulting in superior predictive accuracy and robustness in identifying high-risk sepsis patients. Validated against the MIMIC-III and MIMIC-IV datasets, TCKAN surpasses existing machine learning and deep learning methods in accuracy, sensitivity, and specificity. Notably, TCKAN achieved AUCs of 87.76% and 88.07%, demonstrating superior capability in identifying high-risk patients. Additionally, TCKAN effectively combats the prevalent issue of data imbalance in clinical settings, improving the detection of patients at elevated risk of mortality and facilitating timely interventions. These results confirm the model's effectiveness and its potential to transform patient management and treatment optimization in clinical practice. Although the TCKAN model has already incorporated temporal, constant, and ICD code data, future research could include more diverse medical data types, such as imaging and laboratory test results, to achieve a more comprehensive data integration and further improve predictive accuracy.
       


### [Enhancing Long-Range Dependency with State Space Model and Kolmogorov-Arnold Networks for Aspect-Based Sentiment Analysis](https://arxiv.org/abs/2407.10347)

**Authors:**
Adamu Lawan, Juhua Pu, Haruna Yunusa, Aliyu Umar, Muhammad Lawan

**Citation Count:**
5

**Abstract:**
Aspect-based Sentiment Analysis (ABSA) evaluates sentiments toward specific aspects of entities within the text. However, attention mechanisms and neural network models struggle with syntactic constraints. The quadratic complexity of attention mechanisms also limits their adoption for capturing long-range dependencies between aspect and opinion words in ABSA. This complexity can lead to the misinterpretation of irrelevant contextual words, restricting their effectiveness to short-range dependencies. To address the above problem, we present a novel approach to enhance long-range dependencies between aspect and opinion words in ABSA (MambaForGCN). This approach incorporates syntax-based Graph Convolutional Network (SynGCN) and MambaFormer (Mamba-Transformer) modules to encode input with dependency relations and semantic information. The Multihead Attention (MHA) and Selective State Space model (Mamba) blocks in the MambaFormer module serve as channels to enhance the model with short and long-range dependencies between aspect and opinion words. We also introduce the Kolmogorov-Arnold Networks (KANs) gated fusion, an adaptive feature representation system that integrates SynGCN and MambaFormer and captures non-linear, complex dependencies. Experimental results on three benchmark datasets demonstrate MambaForGCN's effectiveness, outperforming state-of-the-art (SOTA) baseline models.
       


### [Kolmogorov-Arnold Networks: A Critical Assessment of Claims, Performance, and Practical Viability](https://arxiv.org/abs/2407.11075)

**Authors:**
Yuntian Hou, Tianrui Ji, Di Zhang, Angelos Stefanidis

**Citation Count:**
31

**Abstract:**
Kolmogorov-Arnold Networks (KANs) have gained significant attention as an alternative to traditional multilayer perceptrons, with proponents claiming superior interpretability and performance through learnable univariate activation functions. However, recent systematic evaluations reveal substantial discrepancies between theoretical claims and empirical evidence. This critical assessment examines KANs' actual performance across diverse domains using fair comparison methodologies that control for parameters and computational costs. Our analysis demonstrates that KANs outperform MLPs only in symbolic regression tasks, while consistently underperforming in machine learning, computer vision, and natural language processing benchmarks. The claimed advantages largely stem from B-spline activation functions rather than architectural innovations, and computational overhead (1.36-100x slower) severely limits practical deployment. Furthermore, theoretical claims about breaking the "curse of dimensionality" lack rigorous mathematical foundation. We systematically identify the conditions under which KANs provide value versus traditional approaches, establish evaluation standards for future research, and propose a priority-based roadmap for addressing fundamental limitations. This work provides researchers and practitioners with evidence-based guidance for the rational adoption of KANs while highlighting critical research gaps that must be addressed for broader applicability.
       


### [DP-KAN: Differentially Private Kolmogorov-Arnold Networks](https://arxiv.org/abs/2407.12569)

**Authors:**
Nikita P. Kalinin, Simone Bombari, Hossein Zakerinia, Christoph H. Lampert

**Citation Count:**
1

**Abstract:**
We study the Kolmogorov-Arnold Network (KAN), recently proposed as an alternative to the classical Multilayer Perceptron (MLP), in the application for differentially private model training. Using the DP-SGD algorithm, we demonstrate that KAN can be made private in a straightforward manner and evaluated its performance across several datasets. Our results indicate that the accuracy of KAN is not only comparable with MLP but also experiences similar deterioration due to privacy constraints, making it suitable for differentially private model training.
       


### [A Survey on Universal Approximation Theorems](https://arxiv.org/abs/2407.12895)

**Author:**
Midhun T Augustine

**Citation Count:**
4

**Abstract:**
This paper discusses various theorems on the approximation capabilities of neural networks (NNs), which are known as universal approximation theorems (UATs). The paper gives a systematic overview of UATs starting from the preliminary results on function approximation, such as Taylor's theorem, Fourier's theorem, Weierstrass approximation theorem, Kolmogorov - Arnold representation theorem, etc. Theoretical and numerical aspects of UATs are covered from both arbitrary width and depth.
       


### [DropKAN: Regularizing KANs by masking post-activations](https://arxiv.org/abs/2407.13044)

**Author:**
Mohammed Ghaith Altarabichi

**Citation Count:**
10

**Abstract:**
We propose DropKAN (Dropout Kolmogorov-Arnold Networks) a regularization method that prevents co-adaptation of activation function weights in Kolmogorov-Arnold Networks (KANs). DropKAN functions by embedding the drop mask directly within the KAN layer, randomly masking the outputs of some activations within the KANs' computation graph. We show that this simple procedure that require minimal coding effort has a regularizing effect and consistently lead to better generalization of KANs. We analyze the adaptation of the standard Dropout with KANs and demonstrate that Dropout applied to KANs' neurons can lead to unpredictable behavior in the feedforward pass. We carry an empirical study with real world Machine Learning datasets to validate our findings. Our results suggest that DropKAN is consistently a better alternative to using standard Dropout with KANs, and improves the generalization performance of KANs. Our implementation of DropKAN is available at: \url{https://github.com/Ghaith81/dropkan}.
       


### [Reduced Effectiveness of Kolmogorov-Arnold Networks on Functions with Noise](https://arxiv.org/abs/2407.14882)

**Authors:**
Haoran Shen, Chen Zeng, Jiahui Wang, Qiao Wang

**Venue:**
IEEE International Conference on Acoustics, Speech, and Signal Processing

**Citation Count:**
12

**Abstract:**
It has been observed that even a small amount of noise introduced into the dataset can significantly degrade the performance of KAN. In this brief note, we aim to quantitatively evaluate the performance when noise is added to the dataset. We propose an oversampling technique combined with denoising to alleviate the impact of noise. Specifically, we employ kernel filtering based on diffusion maps for pre-filtering the noisy data for training KAN network. Our experiments show that while adding i.i.d. noise with any fixed SNR, when we increase the amount of training data by a factor of $r$, the test-loss (RMSE) of KANs will exhibit a performance trend like $\text{test-loss} \sim \mathcal{O}(r^{-\frac{1}{2}})$ as $r\to +\infty$. We conclude that applying both oversampling and filtering strategies can reduce the detrimental effects of noise. Nevertheless, determining the optimal variance for the kernel filtering process is challenging, and enhancing the volume of training data substantially increases the associated costs, because the training dataset needs to be expanded multiple times in comparison to the initial clean data. As a result, the noise present in the data ultimately diminishes the effectiveness of Kolmogorov-Arnold networks.
       


### [Deep State Space Recurrent Neural Networks for Time Series Forecasting](https://arxiv.org/abs/2407.15236)

**Author:**
Hugo Inzirillo

**Citation Count:**
6

**Abstract:**
We explore various neural network architectures for modeling the dynamics of the cryptocurrency market. Traditional linear models often fall short in accurately capturing the unique and complex dynamics of this market. In contrast, Deep Neural Networks (DNNs) have demonstrated considerable proficiency in time series forecasting. This papers introduces novel neural network framework that blend the principles of econometric state space models with the dynamic capabilities of Recurrent Neural Networks (RNNs). We propose state space models using Long Short Term Memory (LSTM), Gated Residual Units (GRU) and Temporal Kolmogorov-Arnold Networks (TKANs). According to the results, TKANs, inspired by Kolmogorov-Arnold Networks (KANs) and LSTM, demonstrate promising outcomes.
       


### [Inferring turbulent velocity and temperature fields and their statistics from Lagrangian velocity measurements using physics-informed Kolmogorov-Arnold Networks](https://arxiv.org/abs/2407.15727)

**Authors:**
Juan Diego Toscano, Theo Käufer, Zhibo Wang, Martin Maxey, Christian Cierpka, George Em Karniadakis

**Citation Count:**
16

**Abstract:**
We propose the Artificial Intelligence Velocimetry-Thermometry (AIVT) method to infer hidden temperature fields from experimental turbulent velocity data. This physics-informed machine learning method enables us to infer continuous temperature fields using only sparse velocity data, hence eliminating the need for direct temperature measurements. Specifically, AIVT is based on physics-informed Kolmogorov-Arnold Networks (not neural networks) and is trained by optimizing a combined loss function that minimizes the residuals of the velocity data, boundary conditions, and the governing equations. We apply AIVT to a unique set of experimental volumetric and simultaneous temperature and velocity data of Rayleigh-Bénard convection (RBC) that we acquired by combining Particle Image Thermometry and Lagrangian Particle Tracking. This allows us to compare AIVT predictions and measurements directly. We demonstrate that we can reconstruct and infer continuous and instantaneous velocity and temperature fields from sparse experimental data at a fidelity comparable to direct numerical simulations (DNS) of turbulence. This, in turn, enables us to compute important quantities for quantifying turbulence, such as fluctuations, viscous and thermal dissipation, and QR distribution. This paradigm shift in processing experimental data using AIVT to infer turbulent fields at DNS-level fidelity is a promising avenue in breaking the current deadlock of quantitative understanding of turbulence at high Reynolds numbers, where DNS is computationally infeasible.
       


### [Sparks of Quantum Advantage and Rapid Retraining in Machine Learning](https://arxiv.org/abs/2407.16020)

**Author:**
William Troy

**Citation Count:**
5

**Abstract:**
The advent of quantum computing holds the potential to revolutionize various fields by solving complex problems more efficiently than classical computers. Despite this promise, practical quantum advantage is hindered by current hardware limitations, notably the small number of qubits and high noise levels. In this study, we leverage adiabatic quantum computers to optimize Kolmogorov-Arnold Networks, a powerful neural network architecture for representing complex functions with minimal parameters. By modifying the network to use Bezier curves as the basis functions and formulating the optimization problem into a Quadratic Unconstrained Binary Optimization problem, we create a fixed-sized solution space, independent of the number of training samples. This strategy allows for the optimization of an entire neural network in a single training iteration in which, due to order of operations, a majority of the processing is done using a collapsed version of the training dataset. This inherently creates extremely fast training speeds, which are validated experimentally, compared to classical optimizers including Adam, Stochastic Gradient Descent, Adaptive Gradient, and simulated annealing. Additionally, we introduce a novel rapid retraining capability, enabling the network to be retrained with new data without reprocessing old samples, thus enhancing learning efficiency in dynamic environments. Experiments on retraining demonstrate a hundred times speed up using adiabatic quantum computing based optimization compared to that of the gradient descent based optimizers, with theoretical models allowing this speed up to be much larger! Our findings suggest that with further advancements in quantum hardware and algorithm optimization, quantum-optimized machine learning models could have broad applications across various domains, with initial focus on rapid retraining.
       


### [Image Classification using Fuzzy Pooling in Convolutional Kolmogorov-Arnold Networks](https://arxiv.org/abs/2407.16268)

**Authors:**
Ayan Igali, Pakizar Shamoi

**Venue:**
2024 Joint 13th International Conference on Soft Computing and Intelligent Systems and 25th International Symposium on Advanced Intelligent Systems (SCIS&ISIS)

**Citation Count:**
3

**Abstract:**
Nowadays, deep learning models are increasingly required to be both interpretable and highly accurate. We present an approach that integrates Kolmogorov-Arnold Network (KAN) classification heads and Fuzzy Pooling into convolutional neural networks (CNNs). By utilizing the interpretability of KAN and the uncertainty handling capabilities of fuzzy logic, the integration shows potential for improved performance in image classification tasks. Our comparative analysis demonstrates that the modified CNN architecture with KAN and Fuzzy Pooling achieves comparable or higher accuracy than traditional models. The findings highlight the effectiveness of combining fuzzy logic and KAN to develop more interpretable and efficient deep learning models. Future work will aim to expand this approach across larger datasets.
       


### [KAN or MLP: A Fairer Comparison](https://arxiv.org/abs/2407.16674)

**Authors:**
Runpeng Yu, Weihao Yu, Xinchao Wang

**Abstract:**
This paper does not introduce a novel method. Instead, it offers a fairer and more comprehensive comparison of KAN and MLP models across various tasks, including machine learning, computer vision, audio processing, natural language processing, and symbolic formula representation. Specifically, we control the number of parameters and FLOPs to compare the performance of KAN and MLP. Our main observation is that, except for symbolic formula representation tasks, MLP generally outperforms KAN. We also conduct ablation studies on KAN and find that its advantage in symbolic formula representation mainly stems from its B-spline activation function. When B-spline is applied to MLP, performance in symbolic formula representation significantly improves, surpassing or matching that of KAN. However, in other tasks where MLP already excels over KAN, B-spline does not substantially enhance MLP's performance. Furthermore, we find that KAN's forgetting issue is more severe than that of MLP in a standard class-incremental continual learning setting, which differs from the findings reported in the KAN paper. We hope these results provide insights for future research on KAN and other MLP alternatives. Project link: https://github.com/yu-rp/KANbeFair
       


### [2D and 3D Deep Learning Models for MRI-based Parkinson's Disease Classification: A Comparative Analysis of Convolutional Kolmogorov-Arnold Networks, Convolutional Neural Networks, and Graph Convolutional Networks](https://arxiv.org/abs/2407.17380)

**Authors:**
Salil B Patel, Vicky Goh, James F FitzGerald, Chrystalina A Antoniades

**Citation Count:**
3

**Abstract:**
Parkinson's Disease (PD) diagnosis remains challenging. This study applies Convolutional Kolmogorov-Arnold Networks (ConvKANs), integrating learnable spline-based activation functions into convolutional layers, for PD classification using structural MRI. The first 3D implementation of ConvKANs for medical imaging is presented, comparing their performance to Convolutional Neural Networks (CNNs) and Graph Convolutional Networks (GCNs) across three open-source datasets. Isolated analyses assessed performance within individual datasets, using cross-validation techniques. Holdout analyses evaluated cross-dataset generalizability by training models on two datasets and testing on the third, mirroring real-world clinical scenarios. In isolated analyses, 2D ConvKANs achieved the highest AUC of 0.99 (95% CI: 0.98-0.99) on the PPMI dataset, outperforming 2D CNNs (AUC: 0.97, p = 0.0092). 3D models showed promise, with 3D CNN and 3D ConvKAN reaching an AUC of 0.85 on PPMI. In holdout analyses, 3D ConvKAN demonstrated superior generalization, achieving an AUC of 0.85 on early-stage PD data. GCNs underperformed in 2D but improved in 3D implementations. These findings highlight ConvKANs' potential for PD detection, emphasize the importance of 3D analysis in capturing subtle brain changes, and underscore cross-dataset generalization challenges. This study advances AI-assisted PD diagnosis using structural MRI and emphasizes the need for larger-scale validation.
       


### [Adaptive Training of Grid-Dependent Physics-Informed Kolmogorov-Arnold Networks](https://arxiv.org/abs/2407.17611)

**Authors:**
Spyros Rigas, Michalis Papachristou, Theofilos Papadopoulos, Fotios Anagnostopoulos, Georgios Alexandridis

**Venue:**
IEEE Access

**Citation Count:**
24

**Abstract:**
Physics-Informed Neural Networks (PINNs) have emerged as a robust framework for solving Partial Differential Equations (PDEs) by approximating their solutions via neural networks and imposing physics-based constraints on the loss function. Traditionally, Multilayer Perceptrons (MLPs) have been the neural network of choice, with significant progress made in optimizing their training. Recently, Kolmogorov-Arnold Networks (KANs) were introduced as a viable alternative, with the potential of offering better interpretability and efficiency while requiring fewer parameters. In this paper, we present a fast JAX-based implementation of grid-dependent Physics-Informed Kolmogorov-Arnold Networks (PIKANs) for solving PDEs, achieving up to 84 times faster training times than the original KAN implementation. We propose an adaptive training scheme for PIKANs, introducing an adaptive state transition technique to avoid loss function peaks between grid extensions, and a methodology for designing PIKANs with alternative basis functions. Through comparative experiments, we demonstrate that the adaptive features significantly enhance solution accuracy, decreasing the L^2 error relative to the reference solution by up to 43.02%. For the studied PDEs, our methodology approaches or surpasses the results obtained from architectures that utilize up to 8.5 times more parameters, highlighting the potential of adaptive, grid-dependent PIKANs as a superior alternative in scientific and engineering applications.
       


### [Kolmogorov--Arnold networks in molecular dynamics](https://arxiv.org/abs/2407.17774)

**Authors:**
Yuki Nagai, Masahiko Okumura

**Citation Count:**
3

**Abstract:**
We explore the integration of Kolmogorov Networks (KANs) into molecular dynamics (MD) simulations to improve interatomic potentials. We propose that widely used potentials, such as the Lennard-Jones (LJ) potential, the embedded atom model (EAM), and artificial neural network (ANN) potentials, can be interpreted within the KAN framework. Specifically, we demonstrate that the descriptors for ANN potentials, typically constructed using polynomials, can be redefined using KAN's non-linear functions. By employing linear or cubic spline interpolations for these KAN functions, we show that the computational cost of evaluating ANN potentials and their derivatives is reduced.
       


### [Exploring the Limitations of Kolmogorov-Arnold Networks in Classification: Insights to Software Training and Hardware Implementation](https://arxiv.org/abs/2407.17790)

**Authors:**
Van Duy Tran, Tran Xuan Hieu Le, Thi Diem Tran, Hoai Luan Pham, Vu Trung Duong Le, Tuan Hai Vu, Van Tinh Nguyen, Yasuhiko Nakashima

**Venue:**
2024 Twelfth International Symposium on Computing and Networking Workshops (CANDARW)

**Citation Count:**
16

**Abstract:**
Kolmogorov-Arnold Networks (KANs), a novel type of neural network, have recently gained popularity and attention due to the ability to substitute multi-layer perceptions (MLPs) in artificial intelligence (AI) with higher accuracy and interoperability. However, KAN assessment is still limited and cannot provide an in-depth analysis of a specific domain. Furthermore, no study has been conducted on the implementation of KANs in hardware design, which would directly demonstrate whether KANs are truly superior to MLPs in practical applications. As a result, in this paper, we focus on verifying KANs for classification issues, which are a common but significant topic in AI using four different types of datasets. Furthermore, the corresponding hardware implementation is considered using the Vitis high-level synthesis (HLS) tool. To the best of our knowledge, this is the first article to implement hardware for KAN. The results indicate that KANs cannot achieve more accuracy than MLPs in high complex datasets while utilizing substantially higher hardware resources. Therefore, MLP remains an effective approach for achieving accuracy and efficiency in software and hardware implementation.
       


### [Physics Informed Kolmogorov-Arnold Neural Networks for Dynamical Analysis via Efficent-KAN and WAV-KAN](https://arxiv.org/abs/2407.18373)

**Authors:**
Subhajit Patra, Sonali Panda, Bikram Keshari Parida, Mahima Arya, Kurt Jacobs, Denys I. Bondar, Abhijit Sen

**Citation Count:**
12

**Abstract:**
Physics-informed neural networks have proven to be a powerful tool for solving differential equations, leveraging the principles of physics to inform the learning process. However, traditional deep neural networks often face challenges in achieving high accuracy without incurring significant computational costs. In this work, we implement the Physics-Informed Kolmogorov-Arnold Neural Networks (PIKAN) through efficient-KAN and WAV-KAN, which utilize the Kolmogorov-Arnold representation theorem. PIKAN demonstrates superior performance compared to conventional deep neural networks, achieving the same level of accuracy with fewer layers and reduced computational overhead. We explore both B-spline and wavelet-based implementations of PIKAN and benchmark their performance across various ordinary and partial differential equations using unsupervised (data-free) and supervised (data-driven) techniques. For certain differential equations, the data-free approach suffices to find accurate solutions, while in more complex scenarios, the data-driven method enhances the PIKAN's ability to converge to the correct solution. We validate our results against numerical solutions and achieve $99 \%$ accuracy in most scenarios.
       


### [Gaussian Process Kolmogorov-Arnold Networks](https://arxiv.org/abs/2407.18397)

**Author:**
Andrew Siyuan Chen

**Abstract:**
In this paper, we introduce a probabilistic extension to Kolmogorov Arnold Networks (KANs) by incorporating Gaussian Process (GP) as non-linear neurons, which we refer to as GP-KAN. A fully analytical approach to handling the output distribution of one GP as an input to another GP is achieved by considering the function inner product of a GP function sample with the input distribution. These GP neurons exhibit robust non-linear modelling capabilities while using few parameters and can be easily and fully integrated in a feed-forward network structure. They provide inherent uncertainty estimates to the model prediction and can be trained directly on the log-likelihood objective function, without needing variational lower bounds or approximations. In the context of MNIST classification, a model based on GP-KAN of 80 thousand parameters achieved 98.5% prediction accuracy, compared to current state-of-the-art models with 1.5 million parameters.
       


### [F-KANs: Federated Kolmogorov-Arnold Networks](https://arxiv.org/abs/2407.20100)

**Authors:**
Engin Zeydan, Cristian J. Vaca-Rubio, Luis Blanco, Roberto Pereira, Marius Caus, Abdullah Aydeger

**Venue:**
Consumer Communications and Networking Conference

**Citation Count:**
8

**Abstract:**
In this paper, we present an innovative federated learning (FL) approach that utilizes Kolmogorov-Arnold Networks (KANs) for classification tasks. By utilizing the adaptive activation capabilities of KANs in a federated framework, we aim to improve classification capabilities while preserving privacy. The study evaluates the performance of federated KANs (F- KANs) compared to traditional Multi-Layer Perceptrons (MLPs) on classification task. The results show that the F-KANs model significantly outperforms the federated MLP model in terms of accuracy, precision, recall, F1 score and stability, and achieves better performance, paving the way for more efficient and privacy-preserving predictive analytics.
       


### [COEFF-KANs: A Paradigm to Address the Electrolyte Field with KANs](https://arxiv.org/abs/2407.20265)

**Authors:**
Xinhe Li, Zhuoying Feng, Yezeng Chen, Weichen Dai, Zixu He, Yi Zhou, Shuhong Jiao

**Citation Count:**
8

**Abstract:**
To reduce the experimental validation workload for chemical researchers and accelerate the design and optimization of high-energy-density lithium metal batteries, we aim to leverage models to automatically predict Coulombic Efficiency (CE) based on the composition of liquid electrolytes. There are mainly two representative paradigms in existing methods: machine learning and deep learning. However, the former requires intelligent input feature selection and reliable computational methods, leading to error propagation from feature estimation to model prediction, while the latter (e.g. MultiModal-MoLFormer) faces challenges of poor predictive performance and overfitting due to limited diversity in augmented data. To tackle these issues, we propose a novel method COEFF (COlumbic EFficiency prediction via Fine-tuned models), which consists of two stages: pre-training a chemical general model and fine-tuning on downstream domain data. Firstly, we adopt the publicly available MoLFormer model to obtain feature vectors for each solvent and salt in the electrolyte. Then, we perfo