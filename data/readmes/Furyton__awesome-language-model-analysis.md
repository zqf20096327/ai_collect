# Awesome Language Model Analysis [![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)

This paper list focuses on the **theoretical analysis** of language models, especially **large language models** (LLMs).
The papers in this list investigate the learning behavior, generalization ability, and other properties of language models through formal/mathematical analysis -- proofs, provable guarantees, bounds, expressivity results, convergence analysis, and similar. Papers that also include supporting experiments still count; purely empirical/observational papers do not.

Scope of this list:
- Currently, this list focuses on **transformer-based** models.
- We collect papers with a genuine theoretical contribution, instead of purely empirical studies or papers that aim to improve the performance of language models without theoretically analyzing why.

Limitations of this list:
- This list is not exhaustive, and we may miss some very important papers.
- This list is not well-organized yet, and we may need to reorganize the list in the future.
- Some popular topics are not well-covered yet, such as mechanistic engineering, probing, and interpretability.

Statistics of This paper list:
- Total number of different papers: **721**
- For more detailed statistics, please refer to the end of this page.

If you have any suggestions or want to contribute, please feel free to open an issue or a pull request.

For details on how to contribute, please refer to the [contribution guidelines](CONTRIBUTING.md).

You can also share your thoughts and discuss with others in the [Discussions](https://github.com/Furyton/awesome-language-model-analysis/discussions).

> [!NOTE]  
> For uncategorized version, please refer to [here](README.uncategorized.md).

Table of Content
====================
<!--ts-->
- [Awesome Language Model Analysis](#awesome-language-model-analysis-)
- [Table of Content](#table-of-content)
  - [**Phenomena of Interest**](#phenomena-of-interest)
    - [**In-Context Learning**](#in-context-learning)
    - [**Chain-of-Thought**](#chain-of-thought)
    - [**Hallucination**](#hallucination)
    - [**Reversal Curse**](#reversal-curse)
    - [**Scaling Laws / Emergent Abilities / Grokking / etc.**](#scaling-laws--emergent-abilities--grokking--etc)
    - [**Knowledge / Memory Mechanisms**](#knowledge--memory-mechanisms)
    - [**Training Dynamics / Landscape / Optimization / Fine-tuning / etc.**](#training-dynamics--landscape--optimization--fine-tuning--etc)
    - [**Learning / Generalization / Reasoning / Weak to Strong Generalization**](#learning--generalization--reasoning--weak-to-strong-generalization)
    - [**Other Phenomena / Discoveries**](#other-phenomena--discoveries)
  - [**Representational Capacity**](#representational-capacity)
    - [**What Can Transformer Do? / Properties of Transformer**](#what-can-transformer-do--properties-of-transformer)
    - [**What Can Transformer Not Do? / Limitation of Transformer**](#what-can-transformer-not-do--limitation-of-transformer)
  - [**Architectural Effectivity**](#architectural-effectivity)
    - [**Layer-normalization**](#layer-normalization)
    - [**Tokenization / Embedding**](#tokenization--embedding)
    - [**Linear Attention / State Space Models / Recurrent Language Models / etc.**](#linear-attention--state-space-models--recurrent-language-models--etc)
  - [**Training Paradigms**](#training-paradigms)
  - [**Mechanistic Engineering / Probing / Interpretability**](#mechanistic-engineering--probing--interpretability)
  - [**Miscellanea**](#miscellanea)
<!--te-->


## **Phenomena of Interest**

**[`^        back to top        ^`](#awesome-language-model-analysis-)**

Categories focusing on different phenomena, properties, and behaviors observed in large language models (LLMs) and transformer-based models.

### **In-Context Learning**

**[`^        back to top        ^`](#awesome-language-model-analysis-)**

Papers focusing on the theoretical and empirical analysis of in-context learning in large language models.


<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

- **A Unified Framework for In-Context Learning with Causal and Masked Language Models** [[paper link]](http://arxiv.org/abs/2607.04081v1) 2026-07-05  
Chenrui Liu;Chuanlong Xie;Falong Tan;Yicheng Zeng;Lixing Zhu



- **Sequential Correlations Change In-Context Learning: Effective Context Length and Architectural Mismatch** [[paper link]](http://arxiv.org/abs/2607.03660v1) 2026-07-04  
Mary Letey;Yue M. Lu;Cengiz Pehlevan;Jacob Zavatone-Veth



- **Best-of-Better-$N$: Generating Pre-Aligned Responses with In-Context Learning** [[paper link]](http://arxiv.org/abs/2607.03453v1) 2026-07-03  
Eric Lei;Hsiang Hsu;Chun-Fu Chen



- **Induction Heads Interpolate N-Grams** [[paper link]](http://arxiv.org/abs/2607.02800v1) 2026-07-02  
Francesco D'Angelo;Oguz Kaan Yuksel;Swathi Shree Narashiman;Nicolas Flammarion



- **From Approximation to Emergence: A Theory of Deep Learning** [[paper link]](http://arxiv.org/abs/2607.01311v1) 2026-07-01  
Zhilin Zhao



- **Ghost in the Kernel: In-Context Learning with Efficient Transformers via Domain Generalization** [[paper link]](http://arxiv.org/abs/2607.00479v1) 2026-07-01  
Peilin Liu;Ding-Xuan Zhou



- **Transformers as Bayesian In-Context Experimenters: Smoothness-Adaptive Efficient ATE Estimation** [[paper link]](http://arxiv.org/abs/2606.31184v1) 2026-06-30  
Jiachun Li;David Simchi-Levi



- **A Theoretical Interpretation of In-Context Learning via Probabilistic Modeling** [[paper link]](http://arxiv.org/abs/2606.28926v1) 2026-06-27  
Zhenyu Liu;Huaze Tang;Shao-Lun Huang



- **What Do Safety-Aligned LLMs Learn From Mixed Compliance Demonstrations?** [[paper link]](http://arxiv.org/abs/2606.20508v1) 2026-06-18  
Sihui Dai;Mann Patel



- **Can In-Context Learning Support Intrinsic Curiosity?** [[paper link]](http://arxiv.org/abs/2606.19476v1) 2026-06-17  
Eric Elmoznino;Sangnie Bhardwaj;Johannes von Oswald;Rajai Nasser;Blaise Agüera y Arcas;João Sacramento;Rif A. Saurous;Guillaume Lajoie



- **Revisiting the Systematicity in Negation in the Era of In-Context Learning** [[paper link]](http://arxiv.org/abs/2606.16867v1) 2026-06-15  
Hitomi Yanaka;Taisei Yamamoto



- **Adaptive inference and function vectors in deep transformers** [[paper link]](http://arxiv.org/abs/2606.16694v1) 2026-06-15  
Ravin Raj;Gautam Reddy



- **Where Computation Lives Inside TabPFN: Causal Localisation of Attention Head Function** [[paper link]](http://arxiv.org/abs/2606.12917v1) 2026-06-11  
Atharva Gupta;Dhruv Kumar;Murari Mandal;Saurabh Deshpande



- **The Effect of Training Task Diversity on In-Context Learning through the Lens of Low-Dimensional Subspaces** [[paper link]](http://arxiv.org/abs/2606.06814v1) 2026-06-05  
Soo Min Kwon;Alec S. Xu;Can Yaras;Dogyoon Song;Laura Balzano;Qing Qu



- **Transformers are Deep Optimizers: Provable In-Context Learning for Deep Model Training** [[paper link]](http://arxiv.org/abs/2411.16549) 2024-11-25  
Weimin Wu; Maojiang Su; Jerry Yao-Chieh Hu; Zhao Song; Han Liu



- **Can a Large Language Model Learn Matrix Functions In Context?** [[paper link]](http://arxiv.org/abs/2411.15675) 2024-11-24  
Paimon Goulart; Evangelos E. Papalexakis



- **Transformers as Game Players: Provable In-context Game-playing Capabilities of Pre-trained Models** [[paper link]](http://arxiv.org/abs/2410.09701) 2024-11-13  
Chengshuai Shi; Kun Yang; Jing Yang; Cong Shen



- **Adversarial Robustness of In-Context Learning in Transformers for Linear Regression** [[paper link]](http://arxiv.org/abs/2411.05189) 2024-11-07  
Usman Anwar; Johannes Von Oswald; Louis Kirsch; David Krueger; Spencer Frei



- **Provable In-Context Learning with Transformers: A Case Study on Linear Regression** [[paper link]](http://arxiv.org/abs/2411.02199) 2024-11-04  
Dake Bu; Wei Huang; Andi Han; Atsushi Nitanda; Taiji Suzuki; Qingfu Zhang; Hau-San Wong



- **Pretrained transformer efficiently learns low-dimensional target functions in-context** [[paper link]](http://arxiv.org/abs/2411.02544) 2024-11-04  
Kazusato Oko; Yujin Song; Taiji Suzuki; Denny Wu



- **Toward Understanding In-context vs. In-weight Learning** [[paper link]](http://arxiv.org/abs/2410.23042) 2024-10-30  
Bryan Chan; Xinyi Chen; András György; Dale Schuurmans



- **On the Role of Depth and Looping for In-Context Learning with Task Diversity** [[paper link]](http://arxiv.org/abs/2410.21698) 2024-10-29  
Khashayar Gatmiry; Nikunj Saunshi; Sashank J. Reddi; Stefanie Jegelka; Sanjiv Kumar



- **Mechanisms of Symbol Processing for In-Context Learning in Transformer Networks** [[paper link]](http://arxiv.org/abs/2410.17498) 2024-10-23  
Paul Smolensky; Roland Fernandez; Zhenghao Herbert Zhou; Mattia Opper; Jianfeng Gao



- **Can Transformers In-Context Learn Behavior of a Linear Dynamical System?** [[paper link]](http://arxiv.org/abs/2410.16546) 2024-10-21  
Usman Akram; Haris Vikalo



- **Bayesian scaling laws for in-context learning** [[paper link]](http://arxiv.org/abs/2410.16531) 2024-10-21  
Aryaman Arora; Dan Jurafsky; Christopher Potts; Noah D. Goodman



- **Provable In-context Learning for Mixture of Linear Regressions using Transformers** [[paper link]](http://arxiv.org/abs/2410.14183) 2024-10-18  
Yanhao Jin; Krishnakumar Balasubramanian; Lifeng Lai



- **In-context learning and Occam's razor** [[paper link]](http://arxiv.org/abs/2410.14086) 2024-10-17  
Eric Elmoznino; Tom Marty; Tejas Kasetty; Leo Gagnon; Sarthak Mittal; Mahan Fathi; Dhanya Sridhar; Guillaume Lajoie



- **Context-Scaling versus Task-Scaling in In-Context Learning** [[paper link]](http://arxiv.org/abs/2410.12783) 2024-10-16  
Amirhesam Abedsoltan; Adityanarayanan Radhakrishnan; Jingfeng Wu; Mikhail Belkin



- **Bypassing the Exponential Dependency: Looped Transformers Efficiently Learn In-context by Multi-step Gradient Descent** [[paper link]](http://arxiv.org/abs/2410.11268) 2024-10-15  
Bo Chen; Xiaoyu Li; Yingyu Liang; Zhenmei Shi; Zhao Song



- **How Transformers Implement Induction Heads: Approximation and Optimization Analysis** [[paper link]](http://arxiv.org/abs/2410.11474) 2024-10-15  
Mingze Wang; Ruoxi Yu; Weinan E; Lei Wu



- **On the Training Convergence of Transformers for In-Context Classification** [[paper link]](http://arxiv.org/abs/2410.11475) 2024-10-15  
Wei Shen; Ruida Zhou; Jing Yang; Cong Shen



- **Transformers learn variable-order Markov chains in-context** [[paper link]](http://arxiv.org/abs/2410.05493) 2024-10-07  
Ruida Zhou; Chao Tian; Suhas Diggavi



- **Revisiting In-context Learning Inference Circuit in Large Language Models** [[paper link]](http://arxiv.org/abs/2410.04468) 2024-10-06  
Hakaze Cho; Mariko Kato; Yoshihiro Sakai; Naoya Inoue



- **Trained Transformer Classifiers Generalize and Exhibit Benign Overfitting In-Context** [[paper link]](http://arxiv.org/abs/2410.01774) 2024-10-02  
Spencer Frei; Gal Vardi



- **Transformers Handle Endogeneity in In-Context Linear Regression** [[paper link]](http://arxiv.org/abs/2410.01265) 2024-10-02  
Haodong Liang; Krishnakumar Balasubramanian; Lifeng Lai



- **Unveiling Induction Heads: Provable Training Dynamics and Feature Learning in Transformers** [[paper link]](http://arxiv.org/abs/2409.10559) 2024-09-10  
Siyu Chen; Heejune Sheen; Tianhao Wang; Zhuoran Yang



- **Learning vs Retrieval: The Role of In-Context Examples in Regression with LLMs** [[paper link]](http://arxiv.org/abs/2409.04318) 2024-09-06  
Aliakbar Nafar; Kristen Brent Venable; Parisa Kordjamshidi



- **Transformers are Minimax Optimal Nonparametric In-Context Learners** [[paper link]](http://arxiv.org/abs/2408.12186) 2024-08-22  
Juno Kim; Tai Nakamaki; Taiji Suzuki



- **Memorisation In In-Context Learning** [[paper link]](http://arxiv.org/abs/2408.11546) 2024-08-21  
Shahriar Golchin; Mihai Surdeanu; Steven Bethard; Eduardo Blanco; Ellen Riloff



- **In-Context Learning with Representations: Contextual Generalization of Trained Transformers** [[paper link]](http://arxiv.org/abs/2408.10147) 2024-08-19  
Tong Yang; Yu Huang; Yingbin Liang; Yuejie Chi



- **Fast Training Dataset Attribution via In-Context Learning** [[paper link]](http://arxiv.org/abs/2408.11852) 2024-08-14  
Milad Fotouhi; Mohammad Taha Bahadori; Oluwaseyi Feyisetan; Payman Arabshahi; David Heckerman



- **How Transformers Utilize Multi-Head Attention in In-Context Learning? A Case Study on Sparse Linear Regression** [[paper link]](http://arxiv.org/abs/2408.04532) 2024-08-08  
Xingwu Chen; Lei Zhao; Difan Zou



- **Transformers are Universal In-context Learners** [[paper link]](http://arxiv.org/abs/2408.01367) 2024-08-02  
Takashi Furuya; Maarten V. de Hoop; Gabriel Peyré



- **Polynomial Regression as a Task for Understanding In-context Learning Through Finetuning and Alignment** [[paper link]](http://arxiv.org/abs/2407.19346) 2024-07-27  
Max Wilcoxson; Morten Svendgård; Ria Doshi; Dylan Davis; Reya Vir; Anant Sahai



- **Unveiling In-Context Learning: A Coordinate System to Understand Its Working Mechanism** [[paper link]](http://arxiv.org/abs/2407.17011) 2024-07-24  
Anhao Zhao; Fanghua Ye; Jinlan Fu; Xiaoyu Shen



- **One-Layer Transformer Provably Learns One-Nearest Neighbor In Context** [[paper link]](https://klusowski.princeton.edu/sites/g/files/toruqf5901/files/documents/li2024one.pdf) 2024-07-24  
Zihao Li; Yuan Cao; Cheng Gao; Yihan He; Han Liu; Jason M. Klusowski; Jianqing Fan; Mengdi Wang



- **When can transformers compositionally generalize in-context?** [[paper link]](http://arxiv.org/abs/2407.12275) 2024-07-17  
Seijin Kobayashi; Simon Schug; Yassir Akram; Florian Redhardt; Johannes von Oswald; Razvan Pascanu; Guillaume Lajoie; João Sacramento



- **In-Context In-Context Learning with Transformer Neural Processes** [[paper link]](http://arxiv.org/abs/2406.13493) 2024-06-19  
Matthew Ashman; Cristiana Diaconu; Adrian Weller; Richard E. Turner



- **Probing the Decision Boundaries of In-context Learning in Large Language Models** [[paper link]](http://arxiv.org/abs/2406.11233) 2024-06-17  
Siyan Zhao; Tung Nguyen; Aditya Grover



- **State Soup: In-Context Skill Learning, Retrieval and Mixing** [[paper link]](http://arxiv.org/abs/2406.08423) 2024-06-12  
Maciej Pióro; Maciej Wołczyk; Razvan Pascanu; Johannes von Oswald; João Sacramento



- **Estimating the Hallucination Rate of Generative AI** [[paper link]](http://arxiv.org/abs/2406.07457) 2024-06-11  
Andrew Jesson; Nicolas Beltran-Velez; Quentin Chu; Sweta Karlekar; Jannik Kossen; Yarin Gal; John P. Cunningham; David Blei



- **BERTs are Generative In-Context Learners** [[paper link]](http://arxiv.org/abs/2406.04823) 2024-06-07  
David Samuel



- **Enhancing In-Context Learning Performance with just SVD-Based Weight Pruning: A Theoretical Perspective** [[paper link]](http://arxiv.org/abs/2406.03768) 2024-06-06  
Xinhao Yao; Xiaolin Hu; Shenzhi Yang; Yong Liu



- **What Do Language Models Learn in Context? The Structured Task Hypothesis** [[paper link]](http://arxiv.org/abs/2406.04216) 2024-06-06  
Jiaoda Li; Yifan Hou; Mrinmaya Sachan; Ryan Cotterell



- **Exact Conversion of In-Context Learning to Model Weights in Linearized-Attention Transformers** [[paper link]](http://arxiv.org/abs/2406.02847) 2024-06-05  
Brian K Chen; Tianyang Hu; Hui Jin; Hwee Kuan Lee; Kenji Kawaguchi



- **Learning to grok: Emergence of in-context learning and skill composition in modular arithmetic tasks** [[paper link]](http://arxiv.org/abs/2406.02550) 2024-06-04  
Tianyu He; Darshil Doshi; Aritra Das; Andrey Gromov



- **Why Larger Language Models Do In-context Learning Differently?** [[paper link]](http://arxiv.org/abs/2405.19592) 2024-05-30  
Zhenmei Shi; Junyi Wei; Zhuoyan Xu; Yingyu Liang



- **Is In-Context Learning Sufficient for Instruction Following in LLMs?** [[paper link]](http://arxiv.org/abs/2405.19874) 2024-05-30  
Hao Zhao; Maksym Andriushchenko; Francesco Croce; Nicolas Flammarion



- **Does learning the right latent variables necessarily improve in-context learning?** [[paper link]](http://arxiv.org/abs/2405.19162) 2024-05-29  
Sarthak Mittal; Eric Elmoznino; Leo Gagnon; Sangnie Bhardwaj; Dhanya Sridhar; Guillaume Lajoie



- **A Theory of In-Context Learning in Transformers** [[paper link]](http://arxiv.org/abs/2405.18634) 2024-05-29  
Yifei Wang; Yuyang Wu; Zeming Wei; Stefanie Jegelka; Yisen Wang



- **On Mesa-Optimization in Autoregressively Trained Transformers: Emergence and Capability** [[paper link]](http://arxiv.org/abs/2405.16845) 2024-05-27  
Chenyu Zheng; Wei Huang; Rongzhen Wang; Guoqiang Wu; Jun Zhu; Chongxuan Li



- **Transformer In-Context Learning for Categorical Data** [[paper link]](http://arxiv.org/abs/2405.17248) 2024-05-27  
Aaron T. Wang; Ricardo Henao; Lawrence Carin



- **Automatic Domain Adaptation by Transformers in In-Context Learning** [[paper link]](http://arxiv.org/abs/2405.16819) 2024-05-27  
Ryuichiro Hataya; Kota Matsui; Masaaki Imaizumi



- **Unifying Demonstration Selection and Compression for In-Context Learning** [[paper link]](http://arxiv.org/abs/2405.17062) 2024-05-27  
Jun Gao



- **On the Noise Robustness of In-Context Learning for Text Generation** [[paper link]](http://arxiv.org/abs/2405.17264) 2024-05-27  
Hongfu Gao; Feipeng Zhang; Wenyu Jiang; Jun Shu; Feng Zheng; Hongxin Wei



- **MLPs Learn In-Context** [[paper link]](http://arxiv.org/abs/2405.15618) 2024-05-24  
William L. Tong; Cengiz Pehlevan



- **Towards Better Understanding of In-Context Learning Ability from In-Context Uncertainty Quantification** [[paper link]](http://arxiv.org/abs/2405.15115) 2024-05-24  
Shang Liu; Zhongze Cai; Guanting Chen; Xiaocheng Li



- **Can Looped Transformers Learn to Implement Multi-step Gradient Descent for In-context Learning?** [[paper link]](https://openreview.net/pdf?id=o8AaRKbP9K) 2024-05-02  
Khashayar Gatmiry; Nikunj Saunshi; Sashank J. Reddi; Stefanie Jegelka; Sanjiv Kumar



- **In-context Learning on Function Classes Unveiled for Transformers** [[paper link]](https://openreview.net/pdf?id=rJkGOARXns) 2024-05-02  
Zhijie Wang; Bo Jiang; Shuai Li



- **In-Context Learning with Long-Context Models: An In-Depth Exploration** [[paper link]](http://arxiv.org/abs/2405.00200) 2024-04-30  
Amanda Bertsch; Maor Ivgi; Uri Alon; Jonathan Berant; Matthew R. Gormley; Graham Neubig



- **What needs to go right for an induction head? A mechanistic study of in-context learning circuits and their formation** [[paper link]](http://arxiv.org/abs/2404.07129) 2024-04-10  
Aaditya K. Singh; Ted Moskovitz; Felix Hill; Stephanie C. Y. Chan; Andrew M. Saxe



- **Is attention required for ICL? Exploring the Relationship Between Model Architecture and In-Context Learning Ability** [[paper link]](http://arxiv.org/abs/2310.08049) 2024-04-01  
Ivan Lee; Nan Jiang; Taylor Berg-Kirkpatrick



- **Training Dynamics of Multi-Head Softmax Attention for In-Context Learning: Emergence, Convergence, and Optimality** [[paper link]](http://arxiv.org/abs/2402.19442) 2024-02-29  
Siyu Chen; Heejune Sheen; Tianhao Wang; Zhuoran Yang



- **How Transformers Learn Causal Structure with Gradient Descent** [[paper link]](http://arxiv.org/abs/2402.14735) 2024-02-22  
Eshaan Nichani; Alex Damian; Jason D. Lee



- **In-Context Learning of a Linear Transformer Block: Benefits of the MLP Component and One-Step GD Initialization** [[paper link]](http://arxiv.org/abs/2402.14951) 2024-02-22  
Ruiqi Zhang; Jingfeng Wu; Peter L. Bartlett



- **Identifying Semantic Induction Heads to Understand In-Context Learning** [[paper link]](http://arxiv.org/abs/2402.13055) 2024-02-20  
Jie Ren; Qipeng Guo; Hang Yan; Dongrui Liu; Xipeng Qiu; Dahua Lin



- **How do Transformers perform In-Context Autoregressive Learning?** [[paper link]](http://arxiv.org/abs/2402.05787) 2024-02-08  
Michael E. Sander; Raja Giryes; Taiji Suzuki; Mathieu Blondel; Gabriel Peyré



- **Can Mamba Learn How to Learn? A Comparative Study on In-Context Learning Tasks** [[paper link]](http://arxiv.org/abs/2402.04248) 2024-02-06  
Jongho Park; Jaeseung Park; Zheyang Xiong; Nayoung Lee; Jaewoong Cho; Samet Oymak; Kangwook Lee; Dimitris Papailiopoulos



- **An Information-Theoretic Analysis of In-Context Learning** [[paper link]](http://arxiv.org/abs/2401.15530) 2024-01-28  
Hong Jun Jeon; Jason D. Lee; Qi Lei; Benjamin Van Roy



- **The Transient Nature of Emergent In-Context Learning in Transformers** [[paper link]](http://arxiv.org/abs/2311.08360) 2023-12-11  
Aaditya K. Singh; Stephanie C. Y. Chan; Ted Moskovitz; Erin Grant; Andrew M. Saxe; Felix Hill



- **In-Context Learning Functions with Varying Number of Minima** [[paper link]](http://arxiv.org/abs/2311.12538) 2023-11-21  
David Oniani; Yanshan Wang



- **Exploring the Relationship between In-Context Learning and Instruction Tuning** [[paper link]](http://arxiv.org/abs/2311.10367) 2023-11-17  
Hanyu Duan; Yixuan Tang; Yi Yang; Ahmed Abbasi; Kar Yan Tam



- **When does In-context Learning Fall Short and Why? A Study on Specification-Heavy Tasks** [[paper link]](http://arxiv.org/abs/2311.08993) 2023-11-15  
Hao Peng; Xiaozhi Wang; Jianhui Chen; Weikai Li; Yunjia Qi; Zimu Wang; Zhili Wu; Kaisheng Zeng; Bin Xu; Lei Hou; Juanzi Li



- **In-context Learning Generalizes, But Not Always Robustly: The Case of Syntax** [[paper link]](http://arxiv.org/abs/2311.07811) 2023-11-13  
Aaron Mueller; Albert Webson; Jackson Petty; Tal Linzen



- **Transformers learn to implement preconditioned gradient descent for in-context learning** [[paper link]](http://arxiv.org/abs/2306.00297) 2023-11-09  
Kwangjun Ahn; Xiang Cheng; Hadi Daneshmand; Suvrit Sra



- **Transformers Learn Higher-Order Optimization Methods for In-Context Learning: A Study with Linear Models** [[paper link]](https://arxiv.org/abs/2310.17086v1) 2023-10-26  
Deqing Fu; Tian-Qi Chen; Robin Jia; Vatsal Sharan



- **In-Context Learning Creates Task Vectors** [[paper link]](http://arxiv.org/abs/2310.15916) 2023-10-24  
Roee Hendel; Mor Geva; Amir Globerson



- **Function Vectors in Large Language Models** [[paper link]](http://arxiv.org/abs/2310.15213) 2023-10-23  
Eric Todd; Millicent L. Li; Arnab Sen Sharma; Aaron Mueller; Byron C. Wallace; David Bau



- **In-context Learning with Transformer Is Really Equivalent to a Contrastive Learning Pattern** [[paper link]](http://arxiv.org/abs/2310.13220) 2023-10-19  
Ruifeng Ren; Yong Liu



- **Trained Transformers Learn Linear Models In-Context** [[paper link]](http://arxiv.org/abs/2306.09927) 2023-10-19  
Ruiqi Zhang; Spencer Frei; Peter L. Bartlett



- **How Do Transformers Learn In-Context Beyond Simple Functions? A Case Study on Learning with Representations** [[paper link]](http://arxiv.org/abs/2310.10616) 2023-10-16  
Tianyu Guo; Wei Hu; Song Mei; Huan Wang; Caiming Xiong; Silvio Savarese; Yu Bai



- **Understanding In-Context Learning in Transformers and LLMs by Learning to Learn Discrete Functions** [[paper link]](https://openreview.net/forum?id=ekeyCgeRfC) 2023-10-13  
Satwik Bhattamishra; Arkil Patel; Phil Blunsom; Varun Kanade



- **How Many Pretraining Tasks Are Needed for In-Context Learning of Linear Regression?** [[paper link]](https://openreview.net/forum?id=vSh5ePa0ph) 2023-10-13  
Jingfeng Wu; Difan Zou; Zixiang Chen; Vladimir Braverman; Quanquan Gu; Peter Bartlett



- **In-Context Learning Learns Label Relationships but Is Not Conventional Learning** [[paper link]](https://openreview.net/forum?id=YPIA7bgd5y) 2023-10-13  
Jannik Kossen; Yarin Gal; Tom Rainforth



- **In-context Convergence of Transformers** [[paper link]](https://openreview.net/forum?id=kxpswbhr1r) 2023-10-13  
Yu Huang; Yuan Cheng; Yingbin Liang



- **In-Context Learning through the Bayesian Prism** [[paper link]](https://openreview.net/forum?id=HX5ujdsSon) 2023-10-13  
Madhur Panwar; Kabir Ahuja; Navin Goyal



- **Do pretrained Transformers Really Learn In-context by Gradient Descent?** [[paper link]](http://arxiv.org/abs/2310.08540) 2023-10-12  
Lingfeng Shen; Aayush Mishra; Daniel Khashabi



- **What and How does In-Context Learning Learn? Bayesian Model Averaging, Parameterization, and Generalization** [[paper link]](http://arxiv.org/abs/2305.19420) 2023-10-10  
Yufeng Zhang; Fengzhuo Zhang; Zhuoran Yang; Zhaoran Wang



- **Explaining Emergent In-Context Learning as Kernel Regression** [[paper link]](http://arxiv.org/abs/2305.12766) 2023-10-05  
Chi Han; Ziqi Wang; Han Zhao; Heng Ji



- **CausalLM is not optimal for in-context learning** [[paper link]](http://arxiv.org/abs/2308.06912) 2023-09-02  
Nan Ding; Tomer Levinboim; Jialin Wu; Sebastian Goodman; Radu Soricut



- **One Step of Gradient Descent is Provably the Optimal In-Context Learner with One Layer of Linear Self-Attention** [[paper link]](http://arxiv.org/abs/2307.03576) 2023-07-07  
Arvind Mahankali; Tatsunori B. Hashimoto; Tengyu Ma



- **Transformers as Statisticians: Provable In-Context Learning with In-Context Algorithm Selection** [[paper link]](http://arxiv.org/abs/2306.04637) 2023-07-06  
Yu Bai; Fan Chen; Huan Wang; Caiming Xiong; Song Mei



- **Transformers Learn In-Context by Gradient Descent** [[paper link]](https://openreview.net/forum?id=tHvXrFQma5) 2023-06-15  
Johannes Von Oswald; Eyvind Niklasson; Ettore Randazzo; Joao Sacramento; Alexander Mordvintsev; Andrey Zhmoginov; Max Vladymyrov



- **The Closeness of In-Context Learning and Weight Shifting for Softmax Regression** [[paper link]](http://arxiv.org/abs/2304.13276) 2023-04-26  
Shuai Li; Zhao Song; Yu Xia; Tong Yu; Tianyi Zhou



- **A Theory of Emergent In-Context Learning as Implicit Structure Induction** [[paper link]](http://arxiv.org/abs/2303.07971) 2023-03-14  
Michael Hahn; Navin Goyal



- **The Learnability of In-Context Learning** [[paper link]](http://arxiv.org/abs/2303.07895) 2023-03-14  
Noam Wies; Yoav Levine; Amnon Shashua



- **What Can Transformers Learn In-Context? A Case Study of Simple Function Classes** [[paper link]](http://arxiv.org/abs/2208.01066) 2023-01-14  
Shivam Garg; Dimitris Tsipras; Percy Liang; Gregory Valiant



- **Transformers generalize differently from information stored in context vs in weights** [[paper link]](http://arxiv.org/abs/2210.05675) 2022-10-13  
Stephanie C. Y. Chan; Ishita Dasgupta; Junkyung Kim; Dharshan Kumaran; Andrew K. Lampinen; Felix Hill



- **In-Context Learning and Induction Heads** [[paper link]](http://arxiv.org/abs/2209.11895) 2022-09-24  
Catherine Olsson; Nelson Elhage; Neel Nanda; Nicholas Joseph; Nova DasSarma; Tom Henighan; Ben Mann; Amanda Askell; Yuntao Bai; Anna Chen; Tom Conerly; Dawn Drain; Deep Ganguli; Zac Hatfield-Dodds; Danny Hernandez; Scott Johnston; Andy Jones; Jackson Kernion; Liane Lovitt; Kamal Ndousse; Dario Amodei; Tom Brown; Jack Clark; Jared Kaplan; Sam McCandlish; Chris Olah

</details>


### **Chain-of-Thought**

**[`^        back to top        ^`](#awesome-language-model-analysis-)**

Papers analyzing the chain-of-thought phenomenon in large language models, exploring theoretical and empirical perspectives.


<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

- **Geometric Signatures of Reasoning: A Spectral Perspective on Task Hardness** [[paper link]](http://arxiv.org/abs/2607.01571v1) 2026-07-02  
Aria Masoomi;Mahsa Bazzaz;Adel Javanmard;Vahab Mirrokni



- **What LLMs explain is not what they believe: Evaluating explanation sufficiency under models' own input beliefs** [[paper link]](http://arxiv.org/abs/2606.28615v1) 2026-06-26  
Nhi Nguyen;Shauli Ravfogel;Rajesh Ranganath



- **Scheduling Thoughts: Learning the Order of Thought in Diffusion Language Models** [[paper link]](http://arxiv.org/abs/2606.23567v1) 2026-06-22  
Jiawei Xu;Minghui Liu;Aakriti Agrawal;Yifan Chen;Furong Huang



- **Provable Benefits of RLVR over SFT for Reasoning Models: Learning to Backtrack Efficiently** [[paper link]](http://arxiv.org/abs/2606.22938v1) 2026-06-22  
Stanley Wei;Juno Kim



- **A Verifiable Search Is Not a Learnable Chain-of-Thought** [[paper link]](http://arxiv.org/abs/2606.21884v1) 2026-06-20  
Harsh Patel



- **Learning through Internalization** [[paper link]](http://arxiv.org/abs/2606.20937v1) 2026-06-18  
Nikolaos Tsilivis;Nirmit Joshi;Marko Medvedev;Julia Kempe;Nati Srebro



- **What Makes Effective Supervision in Latent Chain-of-Thought: An Information-Theoretic Analysis** [[paper link]](http://arxiv.org/abs/2606.20075v1) 2026-06-18  
Xinghao Chen;Chak Tou Leong;Wenjin Guo;Jian Wang;Wenjie Li;Xiaoyu Shen



- **Efficiently Representing Algorithms With Chain-of-Thought Transformers** [[paper link]](http://arxiv.org/abs/2606.19697v1) 2026-06-18  
Yanhong Li;Anej Svete;Ashish Sabharwal;William Merrill



- **Free Energy Heuristics: Fast-And-Frugal Cognition as Active Inference Under Uncertain Precision** [[paper link]](http://arxiv.org/abs/2606.15877v1) 2026-06-14  
Alex Bogdan



- **Tight Sample Complexity of Transformers** [[paper link]](http://arxiv.org/abs/2606.09731v1) 2026-06-08  
Chenxiao Yang;Nathan Srebro;Zhiyuan Li



- **Rethinking Thinking Tokens: Understanding Why They Underperform in Practice** [[paper link]](http://arxiv.org/abs/2411.11371) 2024-11-18  
Sreeram Vennam; David Valente; David Herel; Ponnurangam Kumaraguru



- **What Happened in LLMs Layers when Trained for Fast vs. Slow Thinking: A Gradient Perspective** [[paper link]](http://arxiv.org/abs/2410.23743) 2024-10-31  
Ming Li; Yanhong Li; Tianyi Zhou



- **A Theoretical Understanding of Chain-of-Thought: Coherent Reasoning and Error-Aware Demonstration** [[paper link]](https://arxiv.org/abs/2410.16540v1) 2024-10-21  
Yingqian Cui; Pengfei He; Xianfeng Tang; Qi He; Chen Luo; Jiliang Tang; Yue Xing



- **Transformers Provably Solve Parity Efficiently with Chain of Thought** [[paper link]](http://arxiv.org/abs/2410.08633) 2024-10-11  
Juno Kim; Taiji Suzuki



- **From Sparse Dependence to Sparse Attention: Unveiling How Chain-of-Thought Enhances Transformer Sample Efficiency** [[paper link]](http://arxiv.org/abs/2410.05459) 2024-10-07  
Kaiyue Wen; Huaqing Zhang; Hongzhou Lin; Jingzhao Zhang



- **Training Nonlinear Transformers for Chain-of-Thought Inference: A Theoretical Generalization Analysis** [[paper link]](http://arxiv.org/abs/2410.02167) 2024-10-03  
Hongkang Li; Meng Wang; Songtao Lu; Xiaodong Cui; Pin-Yu Chen



- **Autoregressive + Chain of Thought (CoT) ≃ Recurrent: Recurrence's Role in Language Models and a Revist of Recurrent Transformer** [[paper link]](http://arxiv.org/abs/2409.09239) 2024-09-14  
Xiang Zhang; Muhammad Abdul-Mageed; Laks V.S. Lakshmanan



- **Unveiling the Statistical Foundations of Chain-of-Thought Prompting Methods** [[paper link]](http://arxiv.org/abs/2408.14511) 2024-08-25  
Xinyang Hu; Fengzhuo Zhang; Siyu Chen; Zhuoran Yang



- **Deciphering the Factors Influencing the Efficacy of Chain-of-Thought: Probability, Memorization, and Noisy Reasoning** [[paper link]](http://arxiv.org/abs/2407.01687) 2024-07-01  
Akshara Prabhakar; Thomas L. Griffiths; R. Thomas McCoy



- **On the Representational Capacity of Neural Language Models with Chain-of-Thought Reasoning** [[paper link]](http://arxiv.org/abs/2406.14197) 2024-06-20  
Franz Nowak; Anej Svete; Alexandra Butoi; Ryan Cotterell



- **Iteration Head: A Mechanistic Study of Chain-of-Thought** [[paper link]](http://arxiv.org/abs/2406.02128) 2024-06-04  
Vivien Cabannes; Charles Arnal; Wassim Bouaziz; Alice Yang; Francois Charton; Julia Kempe



- **Let's Think Dot by Dot: Hidden Computation in Transformer Language Models** [[paper link]](http://arxiv.org/abs/2404.15758) 2024-04-24  
Jacob Pfau; William Merrill; Samuel R. Bowman



- **Chain of Thought Empowers Transformers to Solve Inherently Serial Problems** [[paper link]](http://arxiv.org/abs/2402.12875) 2024-02-20  
Zhiyuan Li; Hong Liu; Denny Zhou; Tengyu Ma



- **Towards Revealing the Mystery behind Chain of Thought: A Theoretical Perspective** [[paper link]](http://arxiv.org/abs/2305.15408) 2023-12-22  
Guhao Feng; Bohang Zhang; Yuntian Gu; Haotian Ye; Di He; Liwei Wang



- **Why Can Large Language Models Generate Correct Chain-of-Thoughts?** [[paper link]](http://arxiv.org/abs/2310.13571) 2023-10-20  
Rasul Tutunov; Antoine Grosnit; Juliusz Ziomek; Jun Wang; Haitham Bou-Ammar



- **How Large Language Models Implement Chain-of-Thought?** [[paper link]](https://openreview.net/forum?id=b2XfOm3RJa) 2023-10-13  
Yiqun Wang; Sile Hu; Yonggang Zhang; Xiang Tian; Xuesong Liu; Yaowu Chen; Xu Shen; Jieping Ye



- **The Expressive Power of Transformers with Chain of Thought** [[paper link]](https://openreview.net/forum?id=NjNGlPh8Wh) 2023-10-13  
William Merrill; Ashish Sabharwal

</details>


### **Hallucination**

**[`^        back to top        ^`](#awesome-language-model-analysis-)**

Papers examining the hallucination phenomenon in language models, including both theoretical and empirical analysis.


<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

- **Statistically Meaningful Geometry (SMG) Beyond the Euclidean Paradigm, with Application to Generative AI** [[paper link]](http://arxiv.org/abs/2607.03329v1) 2026-07-03  
Bing Cheng;Yi-Shuai Niu;Howell Tong;Shing-Tung Yau



- **Statistically Meaningful Geometry and Gauge Symmetry Breaking: A Geometric Foundation for Scientific Discovery and Intelligence Emergence** [[paper link]](http://arxiv.org/abs/2607.05436v1) 2026-07-03  
Bing Cheng;Yi-Shuai Niu;Howell Tong;Shing-Tung Yau



- **Delayed Verification Destabilizes Multi-Agent LLM Belief: Instability Thresholds and Optimal Corrector Placement** [[paper link]](http://arxiv.org/abs/2606.27409v1) 2026-06-25  
Igor Itkin



- **Pre-Generation Hallucination Detection in Large Language Models via Soft-Target Attention Probing** [[paper link]](http://arxiv.org/abs/2606.21917v1) 2026-06-20  
Amina Miftakhova;Alexey Zaytsev



- **Quickest Detection of Hallucination Onset: Delay Bounds and Learned CUSUM Statistics** [[paper link]](http://arxiv.org/abs/2606.12476v3) 2026-06-10  
Igor Itkin



- **How Many Counterfactuals Does It Take? Probing VLM Hallucinations Through Circuits and Causal Effects** [[paper link]](http://arxiv.org/abs/2606.08777v1) 2026-06-07  
Abhivansh Gupta;Simardeep Singh;Advika Sinha;Shreyansh Modi;Akshat Tomar



- **Analyzing the Correlation Between Hallucinations and Knowledge Conflicts in Large Language Models** [[paper link]](http://arxiv.org/abs/2606.08705v1) 2026-06-07  
Lucrezia Laraspata;Giovanna Castellano;Gennaro Vessio



- **On the Limits of Language Generation: Trade-Offs Between Hallucination and Mode Collapse** [[paper link]](http://arxiv.org/abs/2411.09642) 2024-11-14  
Alkis Kalavasis; Anay Mehrotra; Grigoris Velegkas



- **No Free Lunch: Fundamental Limits of Learning Non-Hallucinating Generative Models** [[paper link]](http://arxiv.org/abs/2410.19217) 2024-10-24  
Changlong Wu; Ananth Grama; Wojciech Szpankowski



- **Shared Imagination: LLMs Hallucinate Alike** [[paper link]](http://arxiv.org/abs/2407.16604) 2024-07-23  
Yilun Zhou; Caiming Xiong; Silvio Savarese; Chien-Sheng Wu



- **Estimating the Hallucination Rate of Generative AI** [[paper link]](http://arxiv.org/abs/2406.07457) 2024-06-11  
Andrew Jesson; Nicolas Beltran-Velez; Quentin Chu; Sweta Karlekar; Jannik Kossen; Yarin Gal; John P. Cunningham; David Blei



- **Does Fine-Tuning LLMs on New Knowledge Encourage Hallucinations?** [[paper link]](http://arxiv.org/abs/2405.05904) 2024-05-09  
Zorik Gekhman; Gal Yona; Roee Aharoni; Matan Eyal; Amir Feder; Roi Reichart; Jonathan Herzig



- **Mechanisms of non-factual hallucinations in language models** [[paper link]](http://arxiv.org/abs/2403.18167) 2024-03-26  
Lei Yu; Meng Cao; Jackie Chi Kit Cheung; Yue Dong



- **Unfamiliar Finetuning Examples Control How Language Models Hallucinate** [[paper link]](http://arxiv.org/abs/2403.05612) 2024-03-08  
Katie Kang; Eric Wallace; Claire Tomlin; Aviral Kumar; Sergey Levine



- **In-Context Sharpness as Alerts: An Inner Representation Perspective for Hallucination Mitigation** [[paper link]](http://arxiv.org/abs/2403.01548) 2024-03-05  
Shiqi Chen; Miao Xiong; Junteng Liu; Zhengxuan Wu; Teng Xiao; Siyang Gao; Junxian He



- **Calibrated Language Models Must Hallucinate** [[paper link]](http://arxiv.org/abs/2311.14648) 2023-11-24  
Adam Tauman Kalai; Santosh S. Vempala



- **The Curious Case of Hallucinatory Unanswerablity: Finding Truths in the Hidden States of Over-Confident Large Language Models** [[paper link]](http://arxiv.org/abs/2310.11877) 2023-10-18  
Aviv Slobodkin; Omer Goldman; Avi Caciularu; Ido Dagan; Shauli Ravfogel

</details>


### **Reversal Curse**

**[`^        back to top        ^`](#awesome-language-model-analysis-)**

Papers that analyze the reversal curse phenomenon in large language models.


<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

- **Towards a Theoretical Understanding of the 'Reversal Curse' via Training Dynamics** [[paper link]](http://arxiv.org/abs/2405.04669) 2024-05-07  
Hanlin Zhu; Baihe Huang; Shaolun Zhang; Michael Jordan; Jiantao Jiao; Yuandong Tian; Stuart Russell



- **The Reversal Curse: LLMs trained on "A is B" fail to learn "B is A"** [[paper link]](http://arxiv.org/abs/2309.12288) 2024-04-04  
Lukas Berglund; Meg Tong; Max Kaufmann; Mikita Balesni; Asa Cooper Stickland; Tomasz Korbak; Owain Evans



- **An Investigation of LLMs' Inefficacy in Understanding Converse Relations** [[paper link]](https://aclanthology.org/2023.emnlp-main.429) 2023-12-01  
Chengwen Qi; Bowen Li; Binyuan Hui; Bailin Wang; Jinyang Li; Jinwang Wu; Yuanjun Laili



- **Physics of Language Models: Part 3.2, Knowledge Manipulation** [[paper link]](http://arxiv.org/abs/2309.14402) 2023-09-25  
Zeyuan Allen-Zhu; Yuanzhi Li



- **The Reversal Curse: Which Tokens You Predict Underlie the Factorization Curse and More** [[paper link]](http://arxiv.org/abs/2306.05183) 2023-06-07  
Ouail Kitouni; Niklas Nolte; Diane Bouchacourt; Adina Williams; Mike Rabbat; Mark Ibrahim

</details>


### **Scaling Laws / Emergent Abilities / Grokking / etc.**

**[`^        back to top        ^`](#awesome-language-model-analysis-)**

Papers exploring how model performance scales with model size, data size, or computational resources, and the emergence of unexpected abilities.


<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

- **From Approximation to Emergence: A Theory of Deep Learning** [[paper link]](http://arxiv.org/abs/2607.01311v1) 2026-07-01  
Zhilin Zhao



- **Radial Suppression Accelerates Algorithmic Generalization: A Geometric Analysis of Delayed Generalization** [[paper link]](http://arxiv.org/abs/2606.32000v1) 2026-06-30  
Srijan Tiwari;Aditya Chauhan;Manjot Singh



- **A Stochastic--Geometric Theory of Scaling Laws in Grokking** [[paper link]](http://arxiv.org/abs/2606.30388v2) 2026-06-29  
Róisín Luo;Christian Gagné;Jonas Ngnawé;Ihsan Ullah;Karyn Morrissey



- **Smooth Scaling Laws Hide Stepwise Token Learning** [[paper link]](http://arxiv.org/abs/2606.29858v1) 2026-06-29  
Pingjie Wang;Zechen Hu;Peiru Yang;Fu Guo;Debing Zhang



- **On the Nonlinearity of Learning Rate Scaling for LLM Training** [[paper link]](http://arxiv.org/abs/2606.29158v1) 2026-06-28  
Zaiwen Yang;Huaqing Zhang;Jing Xu;Jingzhao Zhang



- **Internal Data Repetition Destroys Language Models** [[paper link]](http://arxiv.org/abs/2606.24998v1) 2026-06-23  
Jessica Chudnovsky;Joshua Kazdan;Noam Levi;Rylan Schaeffer;Yegor Denisov-Blanch;Bo He;Mehmet Donmez;Sanmi Koyejo;David Donoho



- **Noise-Driven Escape from Metastable Phases explains Grokking in Deep Neural Networks** [[paper link]](http://arxiv.org/abs/2606.17120v1) 2026-06-15  
Ibrahim Talha Ersoy;Karoline Wiesner



- **Rethinking the Role of Efficient Attention in Hybrid Architectures** [[paper link]](http://arxiv.org/abs/2606.15378v1) 2026-06-13  
Ziqing Qiao;Yinuo Xu;Chaojun Xiao;Zhou Su;Zihan Zhou;Yingfa Chen;Xiaoyue Xu;Xu Han;Zhiyuan Liu



- **Explaining Data Mixing Scaling Laws** [[paper link]](http://arxiv.org/abs/2606.08167v1) 2026-06-06  
Rui Dai;Shuran Zheng



- **Phase Transitions in Large Language Models and the $O(N)$ Model** [[paper link]](http://arxiv.org/abs/2501.16241) 2025-01-27  
Youran Sun; Babak Haghighat



- **Understanding Scaling Laws with Statistical and Approximation Theory for Transformer Neural Networks on Intrinsically Low-dimensional Data** [[paper link]](http://arxiv.org/abs/2411.06646) 2024-11-11  
Alex Havrilla; Wenjing Liao



- **Scaling Laws for Precision** [[paper link]](http://arxiv.org/abs/2411.04330) 2024-11-07  
Tanishq Kumar; Zachary Ankner; Benjamin F. Spector; Blake Bordelon; Niklas Muennighoff; Mansheej Paul; Cengiz Pehlevan; Christopher Ré; Aditi Raghunathan



- **Unlocking the Theory Behind Scaling 1-Bit Neural Networks** [[paper link]](http://arxiv.org/abs/2411.01663) 2024-11-03  
Majid Daliri; Zhao Song; Chiwun Yang



- **How Does Critical Batch Size Scale in Pre-training?** [[paper link]](http://arxiv.org/abs/2410.21676) 2024-10-29  
Hanlin Zhang; Depen Morwani; Nikhil Vyas; Jingfeng Wu; Difan Zou; Udaya Ghai; Dean Foster; Sham Kakade



- **An Information Theory of Compute-Optimal Size Scaling, Emergence, and Plateaus in Language Models** [[paper link]](https://arxiv.org/abs/2410.01243) 2024-10-15  
Anuj K. Nayak; Lav R. Varshney



- **A Hitchhiker's Guide to Scaling Law Estimation** [[paper link]](http://arxiv.org/abs/2410.11840) 2024-10-15  
Leshem Choshen; Yang Zhang; Jacob Andreas



- **Scaling Laws Across Model Architectures: A Comparative Analysis of Dense and MoE Models in Large Language Models** [[paper link]](https://arxiv.org/abs/2410.05661) 2024-10-08  
Siqi Wang; Zhengyu Chen; Bei Li; Keqing He; Min Zhang; Jingang Wang



- **Grokking at the Edge of Linear Separability** [[paper link]](https://arxiv.org/abs/2410.04489) 2024-10-06  
Alon Beck; Noam Levi; Yohai Bar-Sinai



- **An Empirical Study of Scaling Laws for Transfer** [[paper link]](https://arxiv.org/abs/2408.16947) 2024-08-30  
Matthew Barnett



- **A Percolation Model of Emergence: Analyzing Transformers Trained on a Formal Language** [[paper link]](http://arxiv.org/abs/2408.12578) 2024-08-22  
Ekdeep Singh Lubana; Kyogo Kawaguchi; Robert P. Dick; Hidenori Tanaka



- **Scaling Law with Learning Rate Annealing** [[paper link]](http://arxiv.org/abs/2408.11029) 2024-08-20  
Howe Tissue; Venus Wang; Lu Wang



- **Performance Law of Large Language Models** [[paper link]](http://arxiv.org/abs/2408.09895) 2024-08-19  
Chuhan Wu; Ruiming Tang



- **Information-Theoretic Progress Measures reveal Grokking is an Emergent Phase Transition** [[paper link]](http://arxiv.org/abs/2408.08944) 2024-08-16  
Kenzo Clauw; Sebastiano Stramaglia; Daniele Marinazzo



- **Large Language Monkeys: Scaling Inference Compute with Repeated Sampling** [[paper link]](http://arxiv.org/abs/2407.21787) 2024-07-31  
Bradley Brown; Jordan Juravsky; Ryan Ehrlich; Ronald Clark; Quoc V. Le; Christopher Ré; Azalia Mirhoseini



- **Emergence in non-neural models: grokking modular arithmetic via average gradient outer product** [[paper link]](http://arxiv.org/abs/2407.20199) 2024-07-29  
Neil Mallinar; Daniel Beaglehole; Libin Zhu; Adityanarayanan Radhakrishnan; Parthe Pandit; Mikhail Belkin



- **Exploring Scaling Trends in LLM Robustness** [[paper link]](http://arxiv.org/abs/2407.18213) 2024-07-25  
Nikolaus Howe; Michał Zajac; Ian McKenzie; Oskar Hollinsworth; Tom Tseng; Pierre-Luc Bacon; Adam Gleave



- **Understanding the Interplay of Scale, Data, and Bias in Language Models: A Case Study with BERT** [[paper link]](http://arxiv.org/abs/2407.21058) 2024-07-25  
Muhammad Ali; Swetasudha Panda; Qinlan Shen; Michael Wick; Ari Kobren



- **Scaling Laws with Vocabulary: Larger Models Deserve Larger Vocabularies** [[paper link]](http://arxiv.org/abs/2407.13623) 2024-07-18  
Chaofan Tao; Qian Liu; Longxu Dou; Niklas Muennighoff; Zhongwei Wan; Ping Luo; Min Lin; Ngai Wong



- **Why Do You Grok? A Theoretical Analysis of Grokking Modular Addition** [[paper link]](http://arxiv.org/abs/2407.12332) 2024-07-17  
Mohamad Amin Mohamadi; Zhiyuan Li; Lei Wu; Danica J. Sutherland



- **Predicting Emergent Capabilities by Finetuning** [[paper link]](https://openreview.net/pdf?id=vL8BIGuFTF) 2024-07-10  
Charlie Victor Snell; Eric Wallace; Dan Klein; Sergey Levine



- **Resolving Discrepancies in Compute-Optimal Scaling of Language Models** [[paper link]](http://arxiv.org/abs/2406.19146) 2024-06-25  
Tomer Porian; Mitchell Wortsman; Jenia Jitsev; Ludwig Schmidt; Yair Carmon



- **Scaling Laws for Linear Complexity Language Models** [[paper link]](http://arxiv.org/abs/2406.16690) 2024-06-24  
Xuyang Shen; Dong Li; Ruitao Leng; Zhen Qin; Weigao Sun; Yiran Zhong



- **Scaling Laws for Fact Memorization of Large Language Models** [[paper link]](http://arxiv.org/abs/2406.15720) 2024-06-22  
Xingyu Lu; Xiaonan Li; Qinyuan Cheng; Kai Ding; Xuanjing Huang; Xipeng Qiu



- **Reconciling Kaplan and Chinchilla Scaling Laws** [[paper link]](http://arxiv.org/abs/2406.12907) 2024-06-12  
Tim Pearce; Jinyeop Song



- **Deep Grokking: Would Deep Neural Networks Generalize Better?** [[paper link]](http://arxiv.org/abs/2405.19454) 2024-05-29  
Simin Fan; Razvan Pascanu; Martin Jaggi



- **Linguistic Collapse: Neural Collapse in (Large) Language Models** [[paper link]](https://arxiv.org/abs/2405.17767) 2024-05-28  
Robert Wu; Vardan Papyan



- **Scaling Laws and Compute-Optimal Training Beyond Fixed Training Durations** [[paper link]](http://arxiv.org/abs/2405.18392) 2024-05-28  
Alexander Hägele; Elie Bakouch; Atli Kosson; Loubna Ben Allal; Leandro Von Werra; Martin Jaggi



- **gzip Predicts Data-dependent Scaling Laws** [[paper link]](http://arxiv.org/abs/2405.16684) 2024-05-26  
Rohan Pandey



- **Emergence of a High-Dimensional Abstraction Phase in Language Transformers** [[paper link]](http://arxiv.org/abs/2405.15471) 2024-05-24  
Emily Cheng; Diego Doimo; Corentin Kervadec; Iuri Macocco; Jade Yu; Alessandro Laio; Marco Baroni



- **A rationale from frequency perspective for grokking in training neural network** [[paper link]](http://arxiv.org/abs/2405.17479) 2024-05-24  
Zhangchen Zhou; Yaoyu Zhang; Zhi-Qin John Xu



- **Grokked Transformers are Implicit Reasoners: A Mechanistic Journey to the Edge of Generalization** [[paper link]](http://arxiv.org/abs/2405.15071) 2024-05-23  
Boshi Wang; Xiang Yue; Yu Su; Huan Sun



- **Data Mixing Made Efficient: A Bivariate Scaling Law for Language Model Pretraining** [[paper link]](http://arxiv.org/abs/2405.14908) 2024-05-23  
Ce Ge; Zhijian Ma; Daoyuan Chen; Yaliang Li; Bolin Ding



- **4+3 Phases of Compute-Optimal Neural Scaling Laws** [[paper link]](http://arxiv.org/abs/2405.15074) 2024-05-23  
Elliot Paquette; Courtney Paquette; Lechao Xiao; Jeffrey Pennington



- **Slaves to the Law of Large Numbers: An Asymptotic Equipartition Property for Perplexity in Generative Language Models** [[paper link]](http://arxiv.org/abs/2405.13798) 2024-05-22  
Raghu Mudumbai; Tyler Bell



- **Quantifying Emergence in Large Language Models** [[paper link]](http://arxiv.org/abs/2405.12617) 2024-05-21  
Hang Chen; Xinyu Yang; Jiaying Zhu; Wenya Wang



- **Beyond Scaling Laws: Understanding Transformer Performance with Associative Memory** [[paper link]](http://arxiv.org/abs/2405.08707) 2024-05-14  
Xueyan Niu; Bo Bai; Lei Deng; Wei Han



- **More Compute Is What You Need** [[paper link]](http://arxiv.org/abs/2404.19484) 2024-04-30  
Zhen Guo



- **An exactly solvable model for emergence and scaling laws** [[paper link]](http://arxiv.org/abs/2404.17563) 2024-04-26  
Yoonsoo Nam; Nayara Fonseca; Seok Hyeong Lee; Ard Louis



- **Why do small language models underperform? Studying Language Model Saturation via the Softmax Bottleneck** [[paper link]](http://arxiv.org/abs/2404.07647) 2024-04-11  
Nathan Godey; Éric de la Clergerie; Benoît Sagot



- **A Large-Scale Exploration of $\mu$-Transfer** [[paper link]](http://arxiv.org/abs/2404.05728) 2024-04-08  
Lucas Lingle



- **Emergent Abilities in Reduced-Scale Generative Language Models** [[paper link]](http://arxiv.org/abs/2404.02204) 2024-04-02  
Sherin Muckatira; Vijeta Deshpande; Vladislav Lialin; Anna Rumshisky



- **Understanding Emergent Abilities of Language Models from the Loss Perspective** [[paper link]](http://arxiv.org/abs/2403.15796) 2024-03-23  
Zhengxiao Du; Aohan Zeng; Yuxiao Dong; Jie Tang



- **Unraveling the Mystery of Scaling Laws: Part I** [[paper link]](http://arxiv.org/abs/2403.06563) 2024-03-21  
Hui Su; Zhi Tian; Xiaoyu Shen; Xunliang Cai



- **Language models scale reliably with over-training and on downstream tasks** [[paper link]](http://arxiv.org/abs/2403.08540) 2024-03-13  
Samir Yitzhak Gadre; Georgios Smyrnis; Vaishaal Shankar; Suchin Gururangan; Mitchell Wortsman; Rulin Shao; Jean Mercat; Alex Fang; Jeffrey Li; Sedrick Keh; Rui Xin; Marianna Nezhurina; Igor Vasiljevic; Jenia Jitsev; Alexandros G. Dimakis; Gabriel Ilharco; Shuran Song; Thomas Kollar; Yair Carmon; Achal Dave; Reinhard Heckel; Niklas Muennighoff; Ludwig Schmidt



- **When Scaling Meets LLM Finetuning: The Effect of Data, Model and Finetuning Method** [[paper link]](http://arxiv.org/abs/2402.17193) 2024-02-26  
Biao Zhang; Zhongtao Liu; Colin Cherry; Orhan Firat



- **Interpreting Grokked Transformers in Complex Modular Arithmetic** [[paper link]](https://arxiv.org/abs/2402.16726v2) 2024-02-26  
Hiroki Furuta; Gouki Minegishi; Yusuke Iwasawa; Yutaka Matsuo



- **A Tale of Tails: Model Collapse as a Change of Scaling Laws** [[paper link]](https://arxiv.org/abs/2402.07043) 2024-02-10  
Elvis Dohmatob; Yunzhen Feng; Pu Yang; Francois Charton; Julia Kempe



- **Scaling Data-Constrained Language Models** [[paper link]](http://arxiv.org/abs/2305.16264) 2023-10-25  
Niklas Muennighoff; Alexander M. Rush; Boaz Barak; Teven Le Scao; Aleksandra Piktus; Nouamane Tazi; Sampo Pyysalo; Thomas Wolf; Colin Raffel



- **The Cost of Down-Scaling Language Models: Fact Recall Deteriorates before In-Context Learning** [[paper link]](http://arxiv.org/abs/2310.04680) 2023-10-06  
Tian Jin; Nolan Clement; Xin Dong; Vaishnavh Nagarajan; Michael Carbin; Jonathan Ragan-Kelley; Gintare Karolina Dziugaite



- **Are Emergent Abilities of Large Language Models a Mirage?** [[paper link]](https://arxiv.org/abs/2304.15004v2) 2023-04-28  
Rylan Schaeffer; Brando Miranda; Sanmi Koyejo



- **Training Compute-Optimal Large Language Models** [[paper link]](http://arxiv.org/abs/2203.15556) 2022-03-29  
Jordan Hoffmann; Sebastian Borgeaud; Arthur Mensch; Elena Buchatskaya; Trevor Cai; Eliza Rutherford; Diego de Las Casas; Lisa Anne Hendricks; Johannes Welbl; Aidan Clark; Tom Hennigan; Eric Noland; Katie Millican; George van den Driessche; Bogdan Damoc; Aurelia Guy; Simon Osindero; Karen Simonyan; Erich Elsen; Jack W. Rae; Oriol Vinyals; Laurent Sifre



- **Scaling Laws for Neural Language Models** [[paper link]](http://arxiv.org/abs/2001.08361) 2020-01-22  
Jared Kaplan; Sam McCandlish; Tom Henighan; Tom B. Brown; Benjamin Chess; Rewon Child; Scott Gray; Alec Radford; Jeffrey Wu; Dario Amodei

</details>


### **Knowledge / Memory Mechanisms**

**[`^        back to top        ^`](#awesome-language-model-analysis-)**

Papers focusing on how large language models store, retrieve, and utilize knowledge, analyzing the memory mechanisms involved.


<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

- **Revocable Learned State via Process Sidecars** [[paper link]](http://arxiv.org/abs/2606.30788v1) 2026-06-29  
John Sweeney



- **Parallel Manifold Steering: Efficient Adaptation of Large Associative Memories via Residual Energy Shaping** [[paper link]](http://arxiv.org/abs/2606.24396v1) 2026-06-23  
Kanishk Awadhiya



- **Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets** [[paper link]](http://arxiv.org/abs/2606.23961v1) 2026-06-22  
Duc Duong;Hoang Anh Duy Le;Jianwen Xie;Anshumali Shrivastava;Zhaozhuo Xu



- **A theoretical model for task routing in mixture-of-expert transformers** [[paper link]](http://arxiv.org/abs/2606.14398v2) 2026-06-12  
Vinoth Nandakumar;Yongli Xiang;Yunzhi Yao;Peike Li;Tongliang Liu



- **A Geometric Framework for Understanding Memorization in Generative Models** [[paper link]](http://arxiv.org/abs/2411.00113) 2024-10-31  
Brendan Leigh Ross; Hamidreza Kamkari; Tongzi Wu; Rasa Hosseinzadeh; Zhaoyan Liu; George Stein; Jesse C. Cresswell; Gabriel Loaiza-Ganem



- **Optimal Memorization Capacity of Transformers** [[paper link]](http://arxiv.org/abs/2409.17677) 2024-09-26  
Tokio Kajitsuka; Issei Sato



- **Schrodingers Memory: Large Language Models** [[paper link]](https://arxiv.org/pdf/2409.10482) 2024-09-16  
Wei Wang; Qing Li



- **Self-Attention Limits Working Memory Capacity of Transformer-Based Models** [[paper link]](http://arxiv.org/abs/2409.10715) 2024-09-16  
Dongyu Gong; Hantao Zhang



- **Great Memory, Shallow Reasoning: Limits of kNN-LMs** [[paper link]](http://arxiv.org/abs/2408.11815) 2024-08-21  
Shangyi Geng; Wenting Zhao; Alexander M Rush



- **Memorisation In In-Context Learning** [[paper link]](http://arxiv.org/abs/2408.11546) 2024-08-21  
Shahriar Golchin; Mihai Surdeanu; Steven Bethard; Eduardo Blanco; Ellen Riloff



- **Generalisation First, Memorisation Second? Memorisation Localisation for Natural Language Classification Tasks** [[paper link]](http://arxiv.org/abs/2408.04965) 2024-08-09  
Verna Dankers; Ivan Titov



- **Understanding Memorisation in LLMs: Dynamics, Influencing Factors, and Implications** [[paper link]](http://arxiv.org/abs/2407.19262) 2024-07-27  
Till Speicher; Mohammad Aflah Khan; Qinyuan Wu; Vedant Nanda; Soumi Das; Bishwamittra Ghosh; Krishna P. Gummadi; Evimaria Terzi



- **Demystifying Verbatim Memorization in Large Language Models** [[paper link]](http://arxiv.org/abs/2407.17817) 2024-07-25  
Jing Huang; Diyi Yang; Christopher Potts



- **From Internal Conflict to Contextual Adaptation of Language Models** [[paper link]](http://arxiv.org/abs/2407.17023) 2024-07-24  
Sara Vera Marjanović; Haeun Yu; Pepa Atanasova; Maria Maistro; Christina Lioma; Isabelle Augenstein



- **Generalization v.s. Memorization: Tracing Language Models' Capabilities Back to Pretraining Data** [[paper link]](http://arxiv.org/abs/2407.14985) 2024-07-20  
Antonis Antoniades; Xinyi Wang; Yanai Elazar; Alfonso Amayuelas; Alon Albalak; Kexun Zhang; William Yang Wang



- **Physics of Language Models: Part 3.1, Knowledge Storage and Extraction** [[paper link]](http://arxiv.org/abs/2309.14316) 2024-07-16  
Zeyuan Allen-Zhu; Yuanzhi Li



- **Induction Heads as an Essential Mechanism for Pattern Matching in In-context Learning** [[paper link]](http://arxiv.org/abs/2407.07011) 2024-07-09  
J. Crosbie; E. Shutova



- **Do LLMs dream of elephants (when told not to)? Latent concept association and associative memory in transformers** [[paper link]](http://arxiv.org/abs/2406.18400) 2024-06-26  
Yibo Jiang; Goutham Rajendran; Pradeep Ravikumar; Bryon Aragam



- **Scaling Laws for Fact Memorization of Large Language Models** [[paper link]](http://arxiv.org/abs/2406.15720) 2024-06-22  
Xingyu Lu; Xiaonan Li; Qinyuan Cheng; Kai Ding; Xuanjing Huang; Xipeng Qiu



- **Connecting the Dots: LLMs can Infer and Verbalize Latent Structure from Disparate Training Data** [[paper link]](http://arxiv.org/abs/2406.14546) 2024-06-20  
Johannes Treutlein; Dami Choi; Jan Betley; Cem Anil; Samuel Marks; Roger Baker Grosse; Owain Evans



- **Uncovering Latent Memories: Assessing Data Leakage and Memorization Patterns in Large Language Models** [[paper link]](http://arxiv.org/abs/2406.14549) 2024-06-20  
Sunny Duan; Mikail Khona; Abhiram Iyer; Rylan Schaeffer; Ila R Fiete



- **Understanding Finetuning for Factual Knowledge Extraction** [[paper link]](http://arxiv.org/abs/2406.14785) 2024-06-20  
Gaurav Ghosal; Tatsunori Hashimoto; Aditi Raghunathan



- **Estimating Knowledge in Large Language Models Without Generating a Single Token** [[paper link]](http://arxiv.org/abs/2406.12673) 2024-06-18  
Daniela Gottesman; Mor Geva



- **How Do Large Language Models Acquire Factual Knowledge During Pretraining?** [[paper link]](http://arxiv.org/abs/2406.11813) 2024-06-17  
Hoyeon Chang; Jinho Park; Seonghyeon Ye; Sohee Yang; Youngkyung Seo; Du-Seong Chang; Minjoon Seo



- **Be like a Goldfish, Don't Memorize! Mitigating Memorization in Generative LLMs** [[paper link]](http://arxiv.org/abs/2406.10209) 2024-06-14  
Abhimanyu Hans; Yuxin Wen; Neel Jain; John Kirchenbauer; Hamid Kazemi; Prajwal Singhania; Siddharth Singh; Gowthami Somepalli; Jonas Geiping; Abhinav Bhatele; Tom Goldstein



- **Knowledge Circuits in Pretrained Transformers** [[paper link]](http://arxiv.org/abs/2405.17969) 2024-05-28  
Yunzhi Yao; Ningyu Zhang; Zekun Xi; Mengru Wang; Ziwen Xu; Shumin Deng; Huajun Chen



- **Upper and lower memory capacity bounds of transformers for next-token prediction** [[paper link]](http://arxiv.org/abs/2405.13718) 2024-05-22  
Liam Madden; Curtis Fox; Christos Thrampoulidis



- **A Multi-Perspective Analysis of Memorization in Large Language Models** [[paper link]](http://arxiv.org/abs/2405.11577) 2024-05-19  
Bowen Chen; Namgi Han; Yusuke Miyao



- **Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws** [[paper link]](http://arxiv.org/abs/2404.05405) 2024-04-08  
Zeyuan Allen-Zhu; Yuanzhi Li



- **Memorization Capacity of Multi-Head Attention in Transformers** [[paper link]](http://arxiv.org/abs/2306.02010) 2024-03-02  
Sadegh Mahdavi; Renjie Liao; Christos Thrampoulidis



- **Birth of a Transformer: A Memory Viewpoint** [[paper link]](http://arxiv.org/abs/2306.00802) 2023-11-06  
Alberto Bietti; Vivien Cabannes; Diane Bouchacourt; Herve Jegou; Leon Bottou



- **Physics of Language Models: Part 3.2, Knowledge Manipulation** [[paper link]](http://arxiv.org/abs/2309.14402) 2023-09-25  
Zeyuan Allen-Zhu; Yuanzhi Li



- **Can Neural Network Memorization Be Localized?** [[paper link]](http://arxiv.org/abs/2307.09542) 2023-07-18  
Pratyush Maini; Michael C. Mozer; Hanie Sedghi; Zachary C. Lipton; J. Zico Kolter; Chiyuan Zhang



- **Quantifying Memorization Across Neural Language Models** [[paper link]](http://arxiv.org/abs/2202.07646) 2022-02-15  
Nicholas Carlini; Daphne Ippolito; Matthew Jagielski; Katherine Lee; Florian Tramer; Chiyuan Zhang

</details>


### **Training Dynamics / Landscape / Optimization / Fine-tuning / etc.**

**[`^        back to top        ^`](#awesome-language-model-analysis-)**

Papers discussing various aspects of the training process, including optimization, fine-tuning, and the training landscape of large language models.


<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

- **No Subspace to Track: Non-Identifiability and Optimizer State in Low-Rank Training** [[paper link]](http://arxiv.org/abs/2607.05872v1) 2026-07-07  
Noel Thomas



- **What Does a Discrete Diffusion Model Learn?** [[paper link]](http://arxiv.org/abs/2607.05381v1) 2026-07-06  
Rodrigo Casado Noguerales;Bernhard Schölkopf;Thomas Hofmann;Aran Raoufi



- **Turning Off-Policy Tokens On-Policy: A Plug-in Approach for Improving LLM Alignment** [[paper link]](http://arxiv.org/abs/2607.04728v1) 2026-07-06  
Yu Li;Xiuyu Li;Mingyang Yi;Jiaxing Wang; zhangliangxu;Zhaolong Xing;Zhen Chen



- **Statistically Meaningful Geometry (SMG) Beyond the Euclidean Paradigm, with Application to Generative AI** [[paper link]](http://arxiv.org/abs/2607.03329v1) 2026-07-03  
Bing Cheng;Yi-Shuai Niu;Howell Tong;Shing-Tung Yau



- **Unbiased Alignment for Large Language Models with Noisy Preferences** [[paper link]](http://arxiv.org/abs/2607.03248v1) 2026-07-03  
Jialiang Wang;Xianming Liu;Xiong Zhou;Hui Liu;Haoliang Li



- **DemoPSD: Disagreement-Modulated Policy Self-Distillation** [[paper link]](http://arxiv.org/abs/2607.02502v2) 2026-07-02  
Yunhe Li;Hao Shi;Wenhao Liu;Mengzhe Ruan;Hanxu Hou;Zhongxiang Dai;Shuang Qiu;Linqi Song



- **ZO-Act: Efficient Zeroth-Order Fine-Tuning via One-Shot Activation-Informed Low-Rank Subspaces** [[paper link]](http://arxiv.org/abs/2607.01125v1) 2026-07-01  
Xun Dong;Yibo Xu;Naigang Wang;Xin Li;Penghang Yin;Zi Yang



- **Measuring Dead Directions: Decomposing and Classifying Singular Structure off Canonical Alignment** [[paper link]](http://arxiv.org/abs/2607.00603v1) 2026-07-01  
Tejas Pradeep Shirodkar



- **GRPO, Dr. GRPO, and DAPO Are Three Operations on One Number: The Group-Standard-Deviation Identity** [[paper link]](http://arxiv.org/abs/2607.00152v1) 2026-06-30  
Yong Yi Bay;Kathleen A. Yearick



- **Geometry-Preserving Orthonormal Initialization for Low-Rank Adaptation in RLVR** [[paper link]](http://arxiv.org/abs/2606.31813v1) 2026-06-30  
Ruijia Zhang;Jiacheng Zhu;Hanqing Zhu;Laixi Shi



- **CHERRY: Compressed Hierarchical Experts with Recurrent Representational Yield** [[paper link]](http://arxiv.org/abs/2606.31796v1) 2026-06-30  
Dohyeon Kwon;Youngjin Park



- **Behavior Cloning is Not All You Need: The Optimality of On-Policy Distillation for Noisy Expert Feedback** [[paper link]](http://arxiv.org/abs/2606.30923v1) 2026-06-29  
Ved Sriraman;Peihan Liu;Daniel Hsu;Adam Block



- **Revocable Learned State via Process Sidecars** [[paper link]](http://arxiv.org/abs/2606.30788v1) 2026-06-29  
John Sweeney



- **Optimization Dynamics Imprint Semantic Specificity in Contrastive Embedding Norms** [[paper link]](http://arxiv.org/abs/2606.30625v1) 2026-06-29  
Ziwei Su;Junyu Ren;Victor Veitch



- **MuonSSM: Orthogonalizing State Space Models for Sequence Modeling** [[paper link]](http://arxiv.org/abs/2606.30461v1) 2026-06-29  
Thai-Khanh Nguyen;Ngoc-Bich-Uyen Vo;Thieu N. Vo;Tan M. Nguyen;Cuong Pham



- **Online Data Selection for Instruction Tuning via Gaussian Processes** [[paper link]](http://arxiv.org/abs/2606.30077v1) 2026-06-29  
Jun Wang;Quoc Phong Nguyen;Julien Monteil;Vu Nguyen



- **Adaptive Block Diffusion: Resolving Training-Inference Mismatch in Diffusion Language Models** [[paper link]](http://arxiv.org/abs/2606.29275v1) 2026-06-28  
Gagan Jain



- **On the Policy Gradient Foundations of Group Relative Policy Optimization: Credit Assignment, Gradient Sparsity, and Rank Collapse** [[paper link]](http://arxiv.org/abs/2606.29238v1) 2026-06-28  
Amritansh Mishra;Supriyo Chakraborty;Berkcan Kapusuzoglu



- **Dead-Direction Conditioners: Gauge-Equivariant Preconditioning for Deep Networks** [[paper link]](http://arxiv.org/abs/2606.29176v1) 2026-06-28  
Tejas Pradeep Shirodkar



- **On the Nonlinearity of Learning Rate Scaling for LLM Training** [[paper link]](http://arxiv.org/abs/2606.29158v1) 2026-06-28  
Zaiwen Yang;Huaqing Zhang;Jing Xu;Jingzhao Zhang



- **The Weakest Link Tells It All: Outcome-Supervised Process Reward Modeling via Learnable Credit Assignment** [[paper link]](http://arxiv.org/abs/2606.27739v1) 2026-06-26  
Tianyu Jia;Yue Fang;Hongxin Ding;Rihong Qiu;Zhibang Yang;Zhijing Wu;Xu Chu;Junfeng Zhao;Yasha Wang



- **Reasoning Quality Emerges Early: Data Curation for Reasoning Models** [[paper link]](http://arxiv.org/abs/2606.26797v1) 2026-06-25  
Hongyi Henry Jin;Wenhan Yang;Meysam Ghaffari;Carlos Morato;Baharan Mirzasoleiman



- **CascadeFormer: Depth-Tapered Transformers Motivated by Gradient Fan-in Asymmetry** [[paper link]](http://arxiv.org/abs/2606.26538v1) 2026-06-25  
Huzama Ahmad;Cao Viet Hai Nam;Se-Young Yun



- **Learning with a Single Rollout via Monte Carlo Pass@k Critic** [[paper link]](http://arxiv.org/abs/2606.25451v1) 2026-06-24  
Fengdi Che;Yang Liu;Lei Yu;Meng Cao;Tong Che;Rupam Mahmood;Dale Schuurmans



- **Training for the Model You Return: Improving Optimization for Iterate-Averaged Language Models** [[paper link]](http://arxiv.org/abs/2606.25086v2) 2026-06-23  
Kwok Chun Au;Adam Block



- **Internal Data Repetition Destroys Language Models** [[paper link]](http://arxiv.org/abs/2606.24998v1) 2026-06-23  
Jessica Chudnovsky;Joshua Kazdan;Noam Levi;Rylan Schaeffer;Yegor Denisov-Blanch;Bo He;Mehmet Donmez;Sanmi Koyejo;David Donoho



- **Parallel Manifold Steering: Efficient Adaptation of Large Associative Memories via Residual Energy Shaping** [[paper link]](http://arxiv.org/abs/2606.24396v1) 2026-06-23  
Kanishk Awadhiya



- **Curvature-Guided Mixing for MLLM Adaptation** [[paper link]](http://arxiv.org/abs/2606.24963v1) 2026-06-23  
Jinglong Yang;Jiaxuan He;Wenjian Huang;Zhan Zhuang;Jianguo Zhang



- **Open Problem: Is AdamW Effective Under Heavy-Tailed Noise?** [[paper link]](http://arxiv.org/abs/2606.23676v1) 2026-06-22  
Dingzhi Yu;Hongyi Tao;Yuanyu Wan;Luo Luo;Lijun Zhang



- **Convergence of Gradient Descent for General Neural Network Architectures Beyond the NTK Regime** [[paper link]](http://arxiv.org/abs/2606.23364v1) 2026-06-22  
Yuqing Wang



- **A First-Order Mean Field Control Analysis of Transformer Layers under Cross-Entropy Training** [[paper link]](http://arxiv.org/abs/2606.23235v1) 2026-06-22  
Cheng Huan;Hongwei Yuan



- **On the Position Bias of On-Policy Distillation** [[paper link]](http://arxiv.org/abs/2606.22600v3) 2026-06-21  
Yan Xie;Sijie Zhu;Tiansheng Wen;Bo Chen;Yifei Wang



- **What are Key Factors for Updates in RL for LLM Reasoning?** [[paper link]](http://arxiv.org/abs/2606.22570v1) 2026-06-21  
Peidong Wang;Demi Wang;Xufang Luo;Jiahang Xu;Xiaocui Yang;Shi Feng;Yuqing Yang;Dongsheng Li



- **Asymptotic Signal Subspace Recovery in Softmax Attention Models** [[paper link]](http://arxiv.org/abs/2606.22406v2) 2026-06-21  
Lan V. Truong



- **Towards Understanding the Power and Limits of the Muon Optimizer: A River-Valley Perspective** [[paper link]](http://arxiv.org/abs/2606.21514v1) 2026-06-19  
Tianqi Shen;Jinji Yang;Runze Shi;Jianhao Ma;Jiaye Teng;Ziye Ma



- **Conservation Laws for Modern Neural Architectures** [[paper link]](http://arxiv.org/abs/2606.17816v1) 2026-06-16  
Viet-Hoang Tran;Vinh Khanh Bui;Tan Lai Ngoc;Nam Nguyen;Tuan Dam;Tan M. Nguyen



- **A Link between Shock-wave Theory and Symmetry-reduced Stochastic Gradient Descent for Artificial Neural Networks** [[paper link]](http://arxiv.org/abs/2606.18303v1) 2026-06-16  
Taiki Miyagawa



- **A Decision-Theoretic View of Test-Time Training: When, How Far, and Which Directions to Adapt** [[paper link]](http://arxiv.org/abs/2606.15569v1) 2026-06-14  
Tomoya Wakayama



- **Understanding Diversity Collapse in RLVR via the Lens of Overtraining** [[paper link]](http://arxiv.org/abs/2606.15455v1) 2026-06-13  
Suqin Yuan;Jinkun Chen;Jiyang Zheng;Muyang Li;Lei Feng;Dadong Wang;Tao Xiang;Tongliang Liu;Bo An



- **Free Heavy-Tailed Lunch for Muon: A Theoretical Justification of Empirical Success** [[paper link]](http://arxiv.org/abs/2606.14560v1) 2026-06-12  
Florian Hübler;Thomas Pethick;Suvrit Sra



- **Phase Transitions in Attention: A Bayesian Theory of Copy Head Emergence** [[paper link]](http://arxiv.org/abs/2606.12058v1) 2026-06-10  
Itay Lavie;Kirsten Fischer;Andrey Lekov;Frederic Van Maele;Zohar Ringel;Moritz Helias



- **Recoverable but Not Stationary:Local Linear Structures in Weights and Activations** [[paper link]](http://arxiv.org/abs/2606.10929v1) 2026-06-09  
Irina Piontkovskaia;Sergey Nikolenko



- **A Mean-Field Analysis of Multi-Head Self-Attention under Cross-Entropy Training** [[paper link]](http://arxiv.org/abs/2606.10469v1) 2026-06-09  
Cheng Huan;Hongfwei Yuan



- **Muon Learns More Robust and Transferable Features than Adam** [[paper link]](http://arxiv.org/abs/2606.09658v1) 2026-06-08  
Tianyu Ruan;Fengzhuo Zhang;Shuche Wang;Shihua Zhang



- **Understanding Quantization-Aware Training: Gradients at Quantized Weights Bias to the Low-Loss Basin** [[paper link]](http://arxiv.org/abs/2606.09012v1) 2026-06-08  
Hanyang Li;Jianhao Ma;Ying Cui



- **Multilingual Sentiment Aware Text Summarization A Reinforcement Learning Approach for Consistency Maintenance** [[paper link]](http://arxiv.org/abs/2606.08940v1) 2026-06-08  
Mikhail Krasitskii;Alexander Gelbukh;Olga Kolesnikova;Grigori Sidorov



- **On the Geometry of On-Policy Distillation** [[paper link]](http://arxiv.org/abs/2606.07082v3) 2026-06-05  
Zhennan Shen;Yanshu Li;Qingyu Yin;Chak Tou Leong;Zhilin Wang;Yanxu Chen;Rongduo Han;Sunbowen Lee;Yi R. Fung



- **Gradient dynamics for low-rank fine-tuning beyond kernels** [[paper link]](http://arxiv.org/abs/2411.15385) 2024-11-23  
Arif Kerem Dayi; Sitan Chen



- **Unraveling the Gradient Descent Dynamics of Transformers** [[paper link]](http://arxiv.org/abs/2411.07538) 2024-11-12  
Bingqing Song; Boran Han; Shuai Zhang; Jie Ding; Mingyi Hong



- **What Do Learning Dynamics Reveal About Generalization in LLM Reasoning?** [[paper link]](http://arxiv.org/abs/2411.07681) 2024-11-12  
Katie Kang; Amrith Setlur; Dibya Ghosh; Jacob Steinhardt; Claire Tomlin; Sergey Levine; Aviral Kumar



- **Training Dynamics of Transformers to Recognize Word Co-occurrence via Gradient Flow Analysis** [[paper link]](http://arxiv.org/abs/2410.09605) 2024-11-12  
Hongru Yang; Bhavya Kailkhura; Zhangyang Wang; Yingbin Liang



- **Global Convergence in Training Large-Scale Transformers** [[paper link]](http://arxiv.org/abs/2410.23610) 2024-10-31  
Cheng Gao; Yuan Cao; Zihao Li; Yihan He; Mengdi Wang; Han Liu; Jason Matthew Klusowski; Jianqing Fan



- **What Happened in LLMs Layers when Trained for Fast vs. Slow Thinking: A Gradient Perspective** [[paper link]](http://arxiv.org/abs/2410.23743) 2024-10-31  
Ming Li; Yanhong Li; Tianyi Zhou



- **Learning and Transferring Sparse Contextual Bigrams with Linear Transformers** [[paper link]](http://arxiv.org/abs/2410.23438) 2024-10-30  
Yunwei Ren; Zixuan Wang; Jason D. Lee



- **Abrupt Learning in Transformers: A Case Study on Matrix Completion** [[paper link]](http://arxiv.org/abs/2410.22244) 2024-10-29  
Pulkit Gopalani; Ekdeep Singh Lubana; Wei Hu



- **LoRA vs Full Fine-tuning: An Illusion of Equivalence** [[paper link]](http://arxiv.org/abs/2410.21228) 2024-10-28  
Reece Shuttleworth; Jacob Andreas; Antonio Torralba; Pratyusha Sharma



- **A distributional simplicity bias in the learning dynamics of transformers** [[paper link]](http://arxiv.org/abs/2410.19637) 2024-10-25  
Riccardo Rende; Federica Gerace; Alessandro Laio; Sebastian Goldt



- **Active-Dormant Attention Heads: Mechanistically Demystifying Extreme-Token Phenomena in LLMs** [[paper link]](http://arxiv.org/abs/2410.13835) 2024-10-17  
Tianyu Guo; Druv Pai; Yu Bai; Jiantao Jiao; Michael I. Jordan; Song Mei



- **How Transformers Implement Induction Heads: Approximation and Optimization Analysis** [[paper link]](http://arxiv.org/abs/2410.11474) 2024-10-15  
Mingze Wang; Ruoxi Yu; Weinan E; Lei Wu



- **What Does It Mean to Be a Transformer? Insights from a Theoretical Hessian Analysis** [[paper link]](http://arxiv.org/abs/2410.10986) 2024-10-14  
Weronika Ormaniec; Felix Dangel; Sidak Pal Singh



- **Adaptation Odyssey in LLMs: Why Does Additional Pretraining Sometimes Fail to Improve?** [[paper link]](http://arxiv.org/abs/2410.05581) 2024-10-08  
Fırat Öncel; Matthias Bethge; Beyza Ermis; Mirco Ravanelli; Cem Subakan; Çağatay Yıldız



- **On the Optimization and Generalization of Two-layer Transformers with Sign Gradient Descent** [[paper link]](http://arxiv.org/abs/2410.04870) 2024-10-07  
Bingrui Li; Wei Huang; Andi Han; Zhanpeng Zhou; Taiji Suzuki; Jun Zhu; Jianfei Chen



- **Understanding Warmup-Stable-Decay Learning Rates: A River Valley Loss Landscape Perspective** [[paper link]](http://arxiv.org/abs/2410.05192) 2024-10-07  
Kaiyue Wen; Zhiyuan Li; Jason Wang; David Hall; Percy Liang; Tengyu Ma



- **Training Nonlinear Transformers for Chain-of-Thought Inference: A Theoretical Generalization Analysis** [[paper link]](http://arxiv.org/abs/2410.02167) 2024-10-03  
Hongkang Li; Meng Wang; Songtao Lu; Xiaodong Cui; Pin-Yu Chen



- **Theoretical Insights into Fine-Tuning Attention Mechanism: Generalization and Optimization** [[paper link]](http://arxiv.org/abs/2410.02247) 2024-10-03  
Xinhao Yao; Hongjin Qian; Xiaolin Hu; Gengze Xu; Yong Liu



- **Trained Transformer Classifiers Generalize and Exhibit Benign Overfitting In-Context** [[paper link]](http://arxiv.org/abs/2410.01774) 2024-10-02  
Spencer Frei; Gal Vardi



- **Towards a Theoretical Understanding of Synthetic Data in LLM Post-Training: A Reverse-Bottleneck Perspective** [[paper link]](http://arxiv.org/abs/2410.01720) 2024-10-02  
Zeyu Gan; Yong Liu



- **Investigating the Impact of Model Complexity in Large Language Models** [[paper link]](http://arxiv.org/abs/2410.00699) 2024-10-01  
Jing Luo; Huiyuan Wang; Weiran Huang



- **Benigh or Not-Benign Overfitting in Token Selection of Attention Mechanism** [[paper link]](http://arxiv.org/abs/2409.17625) 2024-09-26  
Keitaro Sakamoto; Issei Sato



- **Non-asymptotic Convergence of Training Transformers for Next-token Prediction** [[paper link]](http://arxiv.org/abs/2409.17335) 2024-09-25  
Ruiquan Huang; Yingbin Liang; Jing Yang



- **Optimization Hyper-parameter Laws for Large Language Models** [[paper link]](http://arxiv.org/abs/2409.04777) 2024-09-07  
Xingyu Xie; Kuangyu Ding; Shuicheng Yan; Kim-Chuan Toh; Tianwen Wei



- **The AdEMAMix Optimizer: Better, Faster, Older** [[paper link]](http://arxiv.org/abs/2409.03137) 2024-09-05  
Matteo Pagliardini; Pierre Ablin; David Grangier



- **Clustering and Alignment: Understanding the Training Dynamics in Modular Addition** [[paper link]](http://arxiv.org/abs/2408.09414) 2024-08-18  
Tiberiu Musat



- **Global Convergence in Training Large-Scale Transformers** [[paper link]](https://klusowski.princeton.edu/sites/g/files/toruqf5901/files/documents/gao2024global.pdf) 2024-08  
Cheng Gao; Yuan Cao; Zihao Li; Yihan He; Mengdi Wang; Han Liu; Jason M. Klusowski; Jianqing Fan



- **On the Convergence of Encoder-only Shallow Transformers** [[paper link]](https://proceedings.neurips.cc/paper_files/paper/2023/file/a3cf318fbeec1126da21e9185ae9908c-Paper-Conference.pdf) 2024-08  
Yongtao Wu; Fanghui Liu; Grigorios G Chrysos; Volkan Cevher



- **Parameter-Efficient Fine-Tuning for Continual Learning: A Neural Tangent Kernel Perspective** [[paper link]](http://arxiv.org/abs/2407.17120) 2024-07-24  
Jingren Liu; Zhong Ji; YunLong Yu; Jiale Cao; Yanwei Pang; Jungong Han; Xuelong Li



- **Learning Dynamics of LLM Finetuning** [[paper link]](http://arxiv.org/abs/2407.10490) 2024-07-15  
Yi Ren; Danica J. Sutherland



- **Deconstructing What Makes a Good Optimizer for Language Models** [[paper link]](http://arxiv.org/abs/2407.07972) 2024-07-10  
Rosie Zhao; Depen Morwani; David Brandfonbrener; Nikhil Vyas; Sham Kakade



- **Zero-Shot Generalization during Instruction Tuning: Insights from Similarity and Granularity** [[paper link]](http://arxiv.org/abs/2406.11721) 2024-06-17  
Bingxiang He; Ning Ding; Cheng Qian; Jia Deng; Ganqu Cui; Lifan Yuan; Huan-ang Gao; Huimin Chen; Zhiyuan Liu; Maosong Sun



- **Understanding Linear Probing then Fine-tuning Language Models from NTK Perspective** [[paper link]](http://arxiv.org/abs/2405.16747) 2024-05-27  
Akiyoshi Tomihari; Issei Sato



- **Infinite Limits of Multi-head Transformer Dynamics** [[paper link]](http://arxiv.org/abs/2405.15712) 2024-05-24  
Blake Bordelon; Hamza Tahir Chaudhry; Cengiz Pehlevan



- **Towards a Theoretical Understanding of the 'Reversal Curse' via Training Dynamics** [[paper link]](http://arxiv.org/abs/2405.04669) 2024-05-07  
Hanlin Zhu; Baihe Huang; Shaolun Zhang; Michael Jordan; Jiantao Jiao; Yuandong Tian; Stuart Russell



- **Control Theoretic Approach to Fine-Tuning and Transfer Learning** [[paper link]](http://arxiv.org/abs/2404.11013) 2024-04-16  
Erkan Bayram; Shenyu Liu; Mohamed-Ali Belabbas; Tamer Başar



- **Look at the Text: Instruction-Tuned Language Models are More Robust Multiple Choice Selectors than You Think** [[paper link]](http://arxiv.org/abs/2404.08382) 2024-04-12  
Xinpeng Wang; Chengzhi Hu; Bolei Ma; Paul Röttger; Barbara Plank



- **On Training Data Influence of GPT Models** [[paper link]](http://arxiv.org/abs/2404.07840) 2024-04-11  
Qingyi Liu; Yekun Chai; Shuohuan Wang; Yu Sun; Keze Wang; Hua Wu



- **Best Practices and Lessons Learned on Synthetic Data for Language Models** [[paper link]](http://arxiv.org/abs/2404.07503) 2024-04-11  
Ruibo Liu; Jerry Wei; Fangyu Liu; Chenglei Si; Yanzhe Zhang; Jinmeng Rao; Steven Zheng; Daiyi Peng; Diyi Yang; Denny Zhou; Andrew M. Dai



- **How Bad is Training on Synthetic Data? A Statistical Analysis of Language Model Collapse** [[paper link]](http://arxiv.org/abs/2404.05090) 2024-04-07  
Mohamed El Amine Seddik; Suei-Wen Chen; Soufiane Hayou; Pierre Youssef; Merouane Debbah



- **Unveiling the Generalization Power of Fine-Tuned Large Language Models** [[paper link]](http://arxiv.org/abs/2403.09162) 2024-03-14  
Haoran Yang; Yumeng Zhang; Jiaqi Xu; Hongyuan Lu; Pheng Ann Heng; Wai Lam



- **Transformers Get Stable: An End-to-End Signal Propagation Theory for Language Models** [[paper link]](http://arxiv.org/abs/2403.09635) 2024-03-14  
Akhil Kedia; Mohd Abbas Zaidi; Sushil Khyalia; Jungho Jung; Harshith Goka; Haejun Lee



- **Linear Attention is (Maybe) All You Need (to Understand Transformer Optimization)** [[paper link]](http://arxiv.org/abs/2310.01082) 2024-03-13  
Kwangjun Ahn; Xiang Cheng; Minhak Song; Chulhee Yun; Ali Jadbabaie; Suvrit Sra



- **Hallmarks of Optimization Trajectories in Neural Networks and LLMs: The Lengths, Bends, and Dead Ends** [[paper link]](http://arxiv.org/abs/2403.07379) 2024-03-12  
Sidak Pal Singh; Bobby He; Thomas Hofmann; Bernhard Schölkopf



- **The Heuristic Core: Understanding Subnetwork Generalization in Pretrained Language Models** [[paper link]](http://arxiv.org/abs/2403.03942) 2024-03-06  
Adithya Bhaskar; Dan Friedman; Danqi Chen



- **Training Dynamics of Multi-Head Softmax Attention for In-Context Learning: Emergence, Convergence, and Optimality** [[paper link]](http://arxiv.org/abs/2402.19442) 2024-02-29  
Siyu Chen; Heejune Sheen; Tianhao Wang; Zhuoran Yang



- **How Transformers Learn Causal Structure with Gradient Descent** [[paper link]](http://arxiv.org/abs/2402.14735) 2024-02-22  
Eshaan Nichani; Alex Damian; Jason D. Lee



- **LoRA Training in the NTK Regime has No Spurious Local Minima** [[paper link]](http://arxiv.org/abs/2402.11867) 2024-02-19  
Uijeong Jang; Jason D. Lee; Ernest K. Ryu



- **On the Emergence of Cross-Task Linearity in the Pretraining-Finetuning Paradigm** [[paper link]](http://arxiv.org/abs/2402.03660) 2024-02-06  
Zhanpeng Zhou; Zijun Chen; Yilan Chen; Bo Zhang; Junchi Yan



- **Transformers learn through gradual rank increase** [[paper link]](http://arxiv.org/abs/2306.07042) 2023-12-10  
Enric Boix-Adsera; Etai Littwin; Emmanuel Abbe; Samy Bengio; Joshua Susskind



- **Mechanistically analyzing the effects of fine-tuning on procedurally defined tasks** [[paper link]](http://arxiv.org/abs/2311.12786) 2023-11-21  
Samyak Jain; Robert Kirk; Ekdeep Singh Lubana; Robert P. Dick; Hidenori Tanaka; Edward Grefenstette; Tim Rocktäschel; David Scott Krueger



- **Connecting Pre-trained Language Model and Downstream Task via Properties of Representation** [[paper link]](https://openreview.net/forum?id=YLOJ4aKAka) 2023-11-02  
Chenwei Wu; Holden Lee; Rong Ge



- **Scan and Snap: Understanding Training Dynamics and Token Composition in 1-layer Transformer** [[paper link]](http://arxiv.org/abs/2305.16380) 2023-07-02  
Yuandong Tian; Yiping Wang; Beidi Chen; Simon Du



- **A Kernel-Based View of Language Model Fine-Tuning** [[paper link]](https://openreview.net/forum?id=49dTFIGdx8) 2023-06-15  
Sadhika Malladi; Alexander Wettig; Dingli Yu; Danqi Chen; Sanjeev Arora



- **A Stability Analysis of Fine-Tuning a Pre-Trained Model** [[paper link]](https://arxiv.org/abs/2301.09820v2) 2023-01-24  
Zihao Fu; Anthony Man-Cho So; Nigel Collier

</details>


### **Learning / Generalization / Reasoning / Weak to Strong Generalization**

**[`^        back to top        ^`](#awesome-language-model-analysis-)**

Papers analyzing the learning capabilities and generalization performance of language models, from weak to strong generalization.


<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

- **Uncertainty-Aware Abstention in Large Language Models with Provable Alignment Guarantees** [[paper link]](http://arxiv.org/abs/2607.04430v1) 2026-07-05  
Sijin Dong;Hiroyuki Shinnou



- **Statistically Meaningful Geometry and Gauge Symmetry Breaking: A Geometric Foundation for Scientific Discovery and Intelligence Emergence** [[paper link]](http://arxiv.org/abs/2607.05436v1) 2026-07-03  
Bing Cheng;Yi-Shuai Niu;Howell Tong;Shing-Tung Yau



- **Grounding LLM Reasoning under Incomplete Graph Evidence** [[paper link]](http://arxiv.org/abs/2606.30247v1) 2026-06-29  
Jiaqi Li;Fanghui Song



- **Generalization Analysis of Transformers in Distribution Regression** [[paper link]](http://arxiv.org/abs/2606.29256v1) 2026-06-28  
Peilin Liu;Ding-Xuan Zhou



- **When Can Conformal Risk Control Certify LLM Outputs? Bounds, Impossibility, and Adaptation for Structured Generation** [[paper link]](http://arxiv.org/abs/2606.29054v1) 2026-06-27  
Varun Kotte



- **Reasoning Quality Emerges Early: Data Curation for Reasoning Models** [[paper link]](http://arxiv.org/abs/2606.26797v1) 2026-06-25  
Hongyi Henry Jin;Wenhan Yang;Meysam Ghaffari;Carlos Morato;Baharan Mirzasoleiman



- **VeriBound: PAC-Bayesian Generalization Bounds for Process Reward Models Trained with Formal Verification Tools** [[paper link]](http://arxiv.org/abs/2606.20740v1) 2026-06-17  
Amirul Rahman;Mohammed Sabih Alsharari



- **From Reasoning Traces to Reusable Modules: Understanding Compositional Generalization in Language Model Reasoning** [[paper link]](http://arxiv.org/abs/2606.18089v2) 2026-06-16  
Lingjing Kong;Xin Liu;Guangyi Chen;Martin Q. Ma;Xiangchen Song;Yuekai Sun;Mikhail Yurochkin;Taylor W. Killian;Ruslan Salakhutdinov;Kun Zhang;Eric P. Xing;Zhengzhong Liu



- **Is Code Better Than Language for Algorithmic Reasoning** [[paper link]](http://arxiv.org/abs/2606.15589v1) 2026-06-14  
Terry Tong;Yu Feng;Surbhi Goel;Dan Roth



- **Causally Evaluating the Learnability of Formal Language Tasks** [[paper link]](http://arxiv.org/abs/2606.09822v1) 2026-06-08  
Vésteinn Snæbjarnarson;Anej Svete;Josef Valvoda;Reda Boumasmoud;Brian DuSell;Ryan Cotterell



- **How Language Models Fail: Token-Level Signatures of Committed and Persistent Reasoning Failures** [[paper link]](http://arxiv.org/abs/2606.06635v1) 2026-06-04  
Tanvi Thoria;Kiana Jafari;Marc R. Schlichting;Mykel J. Kochenderfer



- **The Tell-Tale Norm: $\ell_2$ Magnitude as a Signal for Reasoning Dynamics in Large Language Models** [[paper link]](http://arxiv.org/abs/2606.06188v1) 2026-06-04  
Jinyang Zhang;Hongxin Ding;Yue Fang;Weibin Liao;Muyang Ye;Junfeng Zhao;Yasha Wang



- **An In-depth Investigation of Sparse Rate Reduction in Transformer-like Models** [[paper link]](http://arxiv.org/abs/2411.17182) 2024-11-26  
Yunzhe Hu; Difan Zou; Dong Xu



- **What Do Learning Dynamics Reveal About Generalization in LLM Reasoning?** [[paper link]](http://arxiv.org/abs/2411.07681) 2024-11-12  
Katie Kang; Amrith Setlur; Dibya Ghosh; Jacob Steinhardt; Claire Tomlin; Sergey Levine; Aviral Kumar



- **Generalization and Risk Bounds for Recurrent Neural Networks** [[paper link]](http://arxiv.org/abs/2411.02784) 2024-11-05  
Xuewei Cheng; Ke Huang; Shujie Ma



- **Provable Length Generalization in Sequence Prediction via Spectral Filtering** [[paper link]](http://arxiv.org/abs/2411.01035) 2024-11-01  
Annie Marsden; Evan Dogariu; Naman Agarwal; Xinyi Chen; Daniel Suo; Elad Hazan



- **RL-STaR: Theoretical Analysis of Reinforcement Learning Frameworks for Self-Taught Reasoner** [[paper link]](http://arxiv.org/abs/2410.23912) 2024-10-31  
Fu-Chieh Chang; Yu-Ting Lee; Hui-Ying Shih; Pei-Yuan Wu



- **Mixture of Parrots: Experts improve memorization more than reasoning** [[paper link]](http://arxiv.org/abs/2410.19034) 2024-10-24  
Samy Jelassi; Clara Mohri; David Brandfonbrener; Alex Gu; Nikhil Vyas; Nikhil Anand; David Alvarez-Melis; Yuanzhi Li; Sham M. Kakade; Eran Malach



- **How Numerical Precision Affects Mathematical Reasoning Capabilities of LLMs** [[paper link]](http://arxiv.org/abs/2410.13857) 2024-10-17  
Guhao Feng; Kai Yang; Yuntian Gu; Xinyue Ai; Shengjie Luo; Jiacheng Sun; Di He; Zhenguo Li; Liwei Wang



- **On Rank-Dependent Generalisation Error Bounds for Transformers** [[paper link]](http://arxiv.org/abs/2410.11500) 2024-10-15  
Lan V. Truong



- **Benign Overfitting in Single-Head Attention** [[paper link]](http://arxiv.org/abs/2410.07746) 2024-10-10  
Roey Magen; Shuning Shang; Zhiwei Xu; Spencer Frei; Wei Hu; Gal Vardi



- **Dynamics of Concept Learning and Compositional Generalization** [[paper link]](http://arxiv.org/abs/2410.08309) 2024-10-10  
Yongyi Yang; Core Francisco Park; Ekdeep Singh Lubana; Maya Okawa; Wei Hu; Hidenori Tanaka



- **Benign Overfitting for Regression with Trained Two-Layer ReLU Networks** [[paper link]](http://arxiv.org/abs/2410.06191) 2024-10-08  
Junhyung Park; Patrick Bloebaum; Shiva Prasad Kasiviswanathan



- **Provable Weak-to-Strong Generalization via Benign Overfitting** [[paper link]](http://arxiv.org/abs/2410.04638) 2024-10-06  
David X. Wu; Anant Sahai



- **A Formal Framework for Understanding Length Generalization in Transformers** [[paper link]](http://arxiv.org/abs/2410.02140) 2024-10-03  
Xinting Huang; Andy Yang; Satwik Bhattamishra; Yash Sarrof; Andreas Krebs; Hattie Zhou; Preetum Nakkiran; Michael Hahn



- **Trained Transformer Classifiers Generalize and Exhibit Benign Overfitting In-Context** [[paper link]](http://arxiv.org/abs/2410.01774) 2024-10-02  
Spencer Frei; Gal Vardi



- **Lines of Thought in Large Language Models** [[paper link]](http://arxiv.org/abs/2410.01545) 2024-10-02  
Raphaël Sarfati; Toni J. B. Liu; Nicolas Boullé; Christopher J. Earls



- **Investigating the Impact of Model Complexity in Large Language Models** [[paper link]](http://arxiv.org/abs/2410.00699) 2024-10-01  
Jing Luo; Huiyuan Wang; Weiran Huang



- **Benign or Not-Benign Overfitting in Token Selection of Attention Mechanism** [[paper link]](http://arxiv.org/abs/2409.17625) 2024-09-26  
Keitaro Sakamoto; Issei Sato



- **Understanding Simplicity Bias towards Compositional Mappings via Learning Dynamics** [[paper link]](http://arxiv.org/abs/2409.09626) 2024-09-15  
Yi Ren; Danica J. Sutherland



- **Unforgettable Generalization in Language Models** [[paper link]](http://arxiv.org/abs/2409.02228) 2024-09-03  
Eric Zhang; Leshem Chosen; Jacob Andreas



- **The Many Faces of Optimal Weak-to-Strong Learning** [[paper link]](http://arxiv.org/abs/2408.17148) 2024-08-30  
Mikael Møller Høgsgaard; Kasper Green Larsen; Markus Engelund Mathiasen



- **Physics of Language Models: Part 2.2, How to Learn From Mistakes on Grade-School Math Problems** [[paper link]](http://arxiv.org/abs/2408.16293) 2024-08-29  
Tian Ye; Zicheng Xu; Yuanzhi Li; Zeyuan Allen-Zhu



- **Out-of-distribution generalization via composition: a lens through induction heads in Transformers** [[paper link]](http://arxiv.org/abs/2408.09503) 2024-08-18  
Jiajun Song; Zhuoyan Xu; Yiqiao Zhong



- **On the Generalization of Preference Learning with DPO** [[paper link]](http://arxiv.org/abs/2408.03459) 2024-08-06  
Shawn Im; Yixuan Li



- **Inductive or Deductive? Rethinking the Fundamental Reasoning Abilities of LLMs** [[paper link]](http://arxiv.org/abs/2408.00114) 2024-07-31  
Kewei Cheng; Jingfeng Yang; Haoming Jiang; Zhengyang Wang; Binxuan Huang; Ruirui Li; Shiyang Li; Zheng Li; Yifan Gao; Xian Li; Bing Yin; Yizhou Sun



- **Physics of Language Models: Part 2.1, Grade-School Math and the Hidden Reasoning Process** [[paper link]](http://arxiv.org/abs/2407.13123) 2024-07-29  
Tian Ye; Zicheng Xu; Yuanzhi Li; Zeyuan Allen-Zhu



- **Unlocking Tokens as Data Points for Generalization Bounds on Larger Language Models** [[paper link]](http://arxiv.org/abs/2407.18158) 2024-07-25  
Sanae Lotfi; Yilun Kuang; Brandon Amos; Micah Goldblum; Marc Finzi; Andrew Gordon Wilson



- **On Initialization of Transformers with Pre-trained Embeddings** [[paper link]](http://arxiv.org/abs/2407.12514) 2024-07-17  
Ha Young Kim; Niranjan Balasubramanian; Byungkon Kang



- **When can transformers compositionally generalize in-context?** [[paper link]](http://arxiv.org/abs/2407.12275) 2024-07-17  
Seijin Kobayashi; Simon Schug; Yassir Akram; Florian Redhardt; Johannes von Oswald; Razvan Pascanu; Guillaume Lajoie; João Sacramento



- **Reasoning in Large Language Models: A Geometric Perspective** [[paper link]](http://arxiv.org/abs/2407.02678) 2024-07-02  
Romain Cosentino; Sarath Shekkizhar



- **Learning on Transformers is Provable Low-Rank and Sparse: A One-layer Analysis** [[paper link]](http://arxiv.org/abs/2406.17167) 2024-06-24  
Hongkang Li; Meng Wang; Shuai Zhang; Sijia Liu; Pin-Yu Chen



- **How Truncating Weights Improves Reasoning in Language Models** [[paper link]](http://arxiv.org/abs/2406.03068) 2024-06-05  
Lei Chen; Joan Bruna; Alberto Bietti



- **Understanding Transformer Reasoning Capabilities via Graph Algorithms** [[paper link]](http://arxiv.org/abs/2405.18512) 2024-05-28  
Clayton Sanford; Bahare Fatemi; Ethan Hall; Anton Tsitsulin; Mehran Kazemi; Jonathan Halcrow; Bryan Perozzi; Vahab Mirrokni



- **Linguistic Collapse: Neural Collapse in (Large) Language Models** [[paper link]](https://arxiv.org/abs/2405.17767) 2024-05-28  
Robert Wu; Vardan Papyan



- **Reality Only Happens Once: Single-Path Generalization Bounds for Transformers** [[paper link]](http://arxiv.org/abs/2405.16563) 2024-05-26  
Yannick Limmer; Anastasis Kratsios; Xuwei Yang; Raeid Saqur; Blanka Horvath



- **A statistical framework for weak-to-strong generalization** [[paper link]](http://arxiv.org/abs/2405.16236) 2024-05-25  
Seamus Somerstep; Felipe Maia Polo; Moulinath Banerjee; Ya'acov Ritov; Mikhail Yurochkin; Yuekai Sun



- **Theoretical Analysis of Weak-to-Strong Generalization** [[paper link]](http://arxiv.org/abs/2405.16043) 2024-05-25  
Hunter Lang; David Sontag; Aravindan Vijayaraghavan



- **Quantifying the Gain in Weak-to-Strong Generalization** [[paper link]](http://arxiv.org/abs/2405.15116) 2024-05-24  
Moses Charikar; Chirag Pabbaraju; Kirankumar Shiragur



- **Towards Understanding How Transformer Perform Multi-step Reasoning with Matching Operation** [[paper link]](http://arxiv.org/abs/2405.15302) 2024-05-24  
Zhiwei Wang; Yunji Wang; Zhongwang Zhang; Zhangchen Zhou; Hui Jin; Tianyang Hu; Jiacheng Sun; Zhenguo Li; Yaoyu Zhang; Zhi-Qin John Xu



- **Initialization is Critical to Whether Transformers Fit Composite Functions by Inference or Memorizing** [[paper link]](http://arxiv.org/abs/2405.05409) 2024-05-08  
Zhongwang Zhang; Pengxiao Lin; Zhiwei Wang; Yaoyu Zhang; Zhi-Qin John Xu



- **On the Empirical Complexity of Reasoning and Planning in LLMs** [[paper link]](http://arxiv.org/abs/2404.11041) 2024-04-17  
Liwei Kang; Zirui Zhao; David Hsu; Wee Sun Lee



- **When can transformers reason with abstract symbols?** [[paper link]](http://arxiv.org/abs/2310.09753) 2024-04-16  
Enric Boix-Adsera; Omid Saremi; Emmanuel Abbe; Samy Bengio; Etai Littwin; Joshua Susskind



- **A Mechanistic Analysis of a Transformer Trained on a Symbolic Multi-Step Reasoning Task** [[paper link]](http://arxiv.org/abs/2402.11917) 2024-02-19  
Jannik Brinkmann; Abhay Sheshadri; Victor Levoso; Paul Swoboda; Christian Bartelt



- **Provably learning a multi-head attention layer** [[paper link]](http://arxiv.org/abs/2402.04084) 2024-02-06  
Sitan Chen; Yuanzhi Li



- **Mechanistically analyzing the effects of fine-tuning on procedurally defined tasks** [[paper link]](http://arxiv.org/abs/2311.12786) 2023-11-21  
Samyak Jain; Robert Kirk; Ekdeep Singh Lubana; Robert P. Dick; Hidenori Tanaka; Edward Grefenstette; Tim Rocktäschel; David Scott Krueger



- **The Impact of Depth and Width on Transformer Language Model Generalization** [[paper link]](http://arxiv.org/abs/2310.19956) 2023-10-30  
Jackson Petty; Sjoerd van Steenkiste; Ishita Dasgupta; Fei Sha; Dan Garrette; Tal Linzen



- **Implicit meta-learning may lead language models to trust more reliable sources** [[paper link]](http://arxiv.org/abs/2310.15047) 2023-10-23  
Dmitrii Krasheninnikov; Egor Krasheninnikov; Bruno Mlodozeniec; Tegan Maharaj; David Krueger



- **On the Optimization and Generalization of Multi-head Attention** [[paper link]](http://arxiv.org/abs/2310.12680) 2023-10-19  
Puneesh Deora; Rouzbeh Ghaderi; Hossein Taheri; Christos Thrampoulidis



- **Large Language Models Cannot Self-Correct Reasoning Yet** [[paper link]](https://openreview.net/forum?id=IkmD3fKBPQ) 2023-10-13  
Jie Huang; Xinyun Chen; Swaroop Mishra; Huaixiu Steven Zheng; Adams Wei Yu; Xinying Song; Denny Zhou



- **How Abilities in Large Language Models are Affected by Supervised Fine-tuning Data Composition** [[paper link]](http://arxiv.org/abs/2310.05492) 2023-10-09  
Guanting Dong; Hongyi Yuan; Keming Lu; Chengpeng Li; Mingfeng Xue; Dayiheng Liu; Wei Wang; Zheng Yuan; Chang Zhou; Jingren Zhou



- **A Theory for Emergence of Complex Skills in Language Models** [[paper link]](http://arxiv.org/abs/2307.15936) 2023-07-29  
Sanjeev Arora; Anirudh Goyal



- **On the Power of Foundation Models** [[paper link]](https://proceedings.mlr.press/v202/yuan23b.html) 2023-07-03  
Yang Yuan



- **Task-Specific Skill Localization in Fine-tuned Language Models** [[paper link]](https://openreview.net/forum?id=Rgnaj43Pk0) 2023-06-15  
Abhishek Panigrahi; Nikunj Saunshi; Haoyu Zhao; Sanjeev Arora



- **Towards Understanding Why Mask-Reconstruction Pretraining Helps in Downstream Tasks** [[paper link]](http://arxiv.org/abs/2206.03826) 2023-02-11  
Jiachun Pan; Pan Zhou; Shuicheng Yan



- **Same Pre-training Loss, Better Downstream: Implicit Bias Matters for Language Models** [[paper link]](http://arxiv.org/abs/2210.14199) 2022-10-25  
Hong Liu; Sang Michael Xie; Zhiyuan Li; Tengyu Ma



- **Why Do Pretrained Language Models Help in Downstream Tasks? An Analysis of Head and Prompt Tuning** [[paper link]](http://arxiv.org/abs/2106.09226) 2022-04-20  
Colin Wei; Sang Michael Xie; Tengyu Ma



- **A Mathematical Exploration of Why Language Models Help Solve Downstream Tasks** [[paper link]](http://arxiv.org/abs/2010.03648) 2021-04-14  
Nikunj Saunshi; Sadhika Malladi; Sanjeev Arora



- **Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning** [[paper link]](http://arxiv.org/abs/2012.13255) 2020-12-22  
Armen Aghajanyan; Luke Zettlemoyer; Sonal Gupta



- **How fine can fine-tuning be? Learning efficient language models** [[paper link]](https://proceedings.mlr.press/v108/radiya-dixit20a.html) 2020-06-03  
Evani Radiya-Dixit; Xin Wang

</details>


### **Other Phenomena / Discoveries**

**[`^        back to top        ^`](#awesome-language-model-analysis-)**

Papers discussing other interesting phenomena or discoveries related to the behavior and properties of language models.


<details open>
<summary><em>paper list (click to fold / unfold)</em></summary>
<br>

- **The yes-no bias of large language models reflects answer order and wording, not shifts in moral judgment** [[paper link]](http://arxiv.org/abs/2607.05552v1) 2026-07-06  
Haonan Huang



- **Social Networks of LLM Agents** [[paper link]](http://arxiv.org/abs/2607.03695v1) 2026-07-04  
Kaixuan Liu;Guojun Xiong;Weinan Zhang;Shengpu Tang



- **How Much of the Routing Gap Is Real? Decomposing the Router-to-Oracle Gap into Reproducible Specialist Advantage and Single-Draw Label Noise** [[paper link]](http://arxiv.org/abs/2607.03436v2) 2026-07-03  
Teng-Ruei Chen



- **Spectral Signatures of Large Language Models** [[paper link]](http://arxiv.org/abs/2607.03377v1) 2026-07-03  
Zhuoying Zhang;Ishan V. Prasad;Yuanzhe Hu;Zihang Liu;Hengrui Luo;Pu Ren;Yaoqing Yang



- **Measuring Dead Directions: Decomposing and Classifying Singular Structure off Canonical Alignment** [[paper link]](http://arxiv.org/abs/2607.00603v1) 2026-07-01  
Tejas Pradeep Shirodkar



- **SemRF: A Semantic Reference Frame for Residual-Stream Dynamics in Language Models** [[paper link]](http://arxiv.org/abs/2606.32022v1) 2026-06-30  
Jian Gu;Aldeida Aleti;Chunyang Chen;Hongyu Zhang



- **When Calibration Rankings Reverse: Accuracy-Controlled Evaluation for Fair Comparison of LLMs** [[paper link]](http://arxiv.org/abs/2606.30814v1) 2026-06-29  
Zhichao Yang;Caiqi Zhang;Ruihan Yang;Chengzu Li;Nigel Collier;Deqing Yang



- **Spectral Perturbation of the Empirical Fisher Information Matrix under Weight Quantization** [[paper link]](http://arxiv.org/abs/2606.28432v1) 2026-06-26  
Rahid Zahid Alekberli;Hikmat Karimov



- **Why Do Accumulated Transformations Extrapolate?** [[paper link]](http://arxiv.org/abs/2606.24975v1) 2026-06-23  
Mahesh Godavarti



- **Deeper is Not Always Better: Mitigating the Alignment Tax via Confident Layer Decoding** [[paper link]](http://arxiv.org/abs/2606.21906v1) 2026-06-20  
Xuanming Zhang;Sining Zhoubian;Yuxuan Chen;Tianyi Tang;An Yang;Sean Du;Chujie Zheng;Fei Huang;Dayiheng Liu;Gao Huang;Jingren Zhou



- **Beyond Hooking Onto the World: Referential Profiles and the Numerical Structure of LLM Grounding** [[paper link]](http://arxiv.org/abs/2606.21195v1) 2026-06-19  
Joo Yull Rhee



- **Contagion Networks: Evaluator Preference Propagation in Multi-Agent LLM Systems** [[paper link]](http://arxiv.org/abs/2606.20493v2) 2026-06-18  
Zewen Liu



- **From Drift to Coherence: Stabilizing Beliefs in LLMs** [[paper link]](http://arxiv.org/abs/2606.17832v2) 2026-06-16  
SongEun Kim;Seungyoo Lee;Edwin Fong;Hyungi Lee;Juho Lee



- **Service-Induced Congestion in Memory-Constrained LLM Serving** [[paper link]](http://arxiv.org/abs/2606.15555v1) 2026-06-14  
Ruicheng Ao;Jing Dong;Gan Luo;David Simchi-Levi



- **Beyond Layer Importance in Layer-wise Sparsity: An Inter-Layer Perturbation-Absorption Perspective** [[paper link]](http://arxiv.org/abs/2606.15161v1) 2026-06-13  
Tao Jing;Ningxin Wu;Chen Kang;Dong Yu;Changliang Li;Pengyuan Liu



- **Multilingual Sentiment Aware Text Summarization A Reinforcement Learning Approach for Consistency Maintenance** [[paper link]](http://arxiv.org/abs/2606.08940v1) 2026-06-08  
Mikhail Krasitskii;Alexander Gelbukh;Olga Kolesnikova;Grigori Sidorov



- **On the loss of context-awareness in general instruction fine-tuning** [[paper link]](http://arxiv.org/abs/2411.02688) 2024-11-05  
Yihan Wang; Andrew Bai; Nanyun Peng; Cho-Jui Hsieh



- **Weight decay induces low-rank attention layers** [[paper link]](http://arxiv.org/abs/2410.23819) 2024-10-31  
Seijin Kobayashi; Yassir Akram; Johannes Von Oswald



- **All or None: Identifiable Linear Properties of Next-token Predictors in Language Modeling** [[paper link]](http://arxiv.org/abs/2410.23501) 2024-10-30  
Emanuele Marconato; Sébastien Lachapelle; Sebastian Weichwald; Luigi Gresele



- **Looking Beyond The Top-1: Transformers Determine Top Tokens In Order** [[paper link]](http://arxiv.org/abs/2410.20210) 2024-10-26  
Daria Lioubashevski; Tomer Schlank; Gabriel Stanovsky; Ariel Goldstein



- **Active-Dormant Attention Heads: Mechanistically Demystifying Extreme-Token Phenomena in LLMs** [[paper link]](http://arxiv.org/abs/2410.13835) 2024-10-17  
Tianyu Guo; Druv Pai; Yu Bai; Jiantao Jiao; Michael I. Jordan; Song Mei



- **Emergent properties with repeated examples** [[paper link]](http://arxiv.org/abs/2410.07041) 2024-10-09  
François Charton; Julia Kempe



- **Masked Mixers for Language Generation and Retrieval** [[paper link]](http://arxiv.org/abs/2409.01482) 2024-09-02  
Benjamin L. Badger



- **Monotonic Representation of Numeric Properties in Language Models** [[paper link]](http://arxiv.org/abs/2408.10381) 2024-08-15  
Benjamin Heinzerling; Kentaro Inui



- **Does Liking Yellow Imply Driving a School Bus? Semantic Leakage in Language Models** [[paper link]](http://arxiv.org/abs/2408.06518) 2024-08-12  
Hila Gonen; Terra Blevins; Alisa Liu; Luke Zettlemoyer; Noah A. Smith



- **Large Language Monkeys: Scaling Inference Compute with Repeated Sampling** [[paper link]](http://arxiv.org/abs/2407.21787) 2024-07-31  
Bradley Brown; Jordan Juravsky; Ryan Ehrlich; Ronald Clark; Quoc V. Le; Christopher Ré; Azalia Mirhoseini



- **Transformers on Markov Data: Constant Depth Suffices** [[paper link]](http://arxiv.org/abs/2407.17686) 2024-07-25  
Nived Rajaraman; Marco Bondaschi; Kannan Ramchandran; Michael Gastpar; Ashok Vardhan Makkuva



- **On the Benefits of Rank in Attention Layers** [[paper link]](http://arxiv.org/abs/2407.16153) 2024-07-23  
Noah Amsel; Gilad Yehudai; Joan Bruna



- **Transformer Alignment in Large Language Models** [[paper link]](http://arxiv.org/abs/2407.07810) 2024-07-10  
Murdock Aubry; Haoming Meng; Anton Sugolov; Vardan Papyan



- **Understanding Transformers via N-gram Statistics** [[paper link]](http://arxiv.org/abs/2407.12034) 2024-06-30  
Timothy Nguyen



- **Large Vocabulary Size Improves Large Language Models** [[paper link]](http://arxiv.org/abs/2406.16508) 2024-06-24  
Sho Takase; Ryokan Ri; Shun Kiyono; Takuya Kato



- **Connecting the Dots: LLMs can Infer and Verbalize Latent Structure from Disparate Training Data** [[paper link]](http://arxiv.org/abs/2406.14546) 2024-06-20  
Johannes Treutlein; Dami Choi; Jan Betley; Cem Anil; Samuel Marks; Roger Baker Grosse; Owain Evans



- **Distributional reasoning in LLMs: Parallel reasoning processes in multi-hop reasoning** [[paper link]](http://arxiv.org/abs/2406.13858) 2024-06-19  
Yuval Shalev; Amir Feder; Ariel Goldstein



- **Transcendence: Generative Models Can Outperform The Experts That Train Them** [[paper link]](http://arxiv.org/abs/2406.11741) 2024-06-17  
Edwin Zhang; Vincent Zhu; Naomi Saphra; Anat Kleiman; Benjamin L. Edelman; Milind Tambe; Sham M. Kakade; Eran Malach



- **Taking a Deep Breath: Enhancing Language Modeling of Large Language Models with Sentinel Tokens** [[paper link]](http://ar