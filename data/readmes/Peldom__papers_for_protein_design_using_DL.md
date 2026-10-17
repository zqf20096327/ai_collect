# List of papers about Protein Design using Deep Learning

> This repository is inspired by the remarkable work of [Kevin Kaichuang Yang](https://github.com/yangkky) and their outstanding project [Machine-learning-for-proteins](https://github.com/yangkky/Machine-learning-for-proteins). We have established this repository to provide a specialized and focused platform for the field of **Deep Learning for Protein Design**, a rapidly advancing domain in computational biology.
>
> [Contributions](https://github.com/Peldom/papers_for_protein_design_using_DL/blob/main/CONTRIBUTING.md) and [suggestions](https://github.com/Peldom/papers_for_protein_design_using_DL/issues) are warmly welcome!
> Community Values, Guiding Principles, and Commitments for the Responsible Development of AI for Protein Design: [details](https://responsiblebiodesign.ai/)

<!-- >
>1. Mini protein, binders, metalloprotein, antibody, peptide & molecule designs are included  
>2. More de novo protein design paper list at [Wangchentong](https://github.com/Wangchentong)'s GitHub repo: [paper_for_denovo_protein_design](https://github.com/Wangchentong/paper_for_denovo_protein_design)  
>3. Our notes of these papers are shared in a **[Zhihu Column](https://www.zhihu.com/column/c_1475864742820929537)** (simplified Chinese/English), more suggested notes at [RosettAI](https://www.zhihu.com/column/rosettastudy)   -->

*Papers last week, updated on 2026.08.02:*
+   Generative artificial intelligence for enzyme design and biocatalysis
    + [[Current Opinion in Chemical Biology](https://www.sciencedirect.com/science/article/pii/S1367593126000773)]
+   The Human Bindome: A Proteome-scale Atlas of Designed Binder Candidates
    + [[bioRxiv 2026.07.30.741542](https://www.biorxiv.org/content/10.64898/2026.07.30.741542v1)] • [[code](https://github.com/wejulius/Bindome)] • [[website](https://bindome.epfl.ch)]


---

<p align="center">
  <br>
  <!-- <img src="dl_pd.png" alt="deep learning for protein design" width="500"> -->
  <img src="cover.jpg" alt="deep learning for protein design">
</p>
<!-- ## Menu -->
<!-- > Heading [[2]](#2-model-based-design) follows a **"generator-predictor-optimizer" paradigm**, Heading [[3]](#3-function-to-scaffold), [[4]](#4scaffold-to-sequence)&[[6]](#6-function-to-structure) follow ["Inside-out" paradigm](https://www.nature.com/articles/nature19946)(*function-scaffold-sequence*) from [RosettaCommons](https://www.rosettacommons.org/), Heading [[5]](#5function-to-sequence)&[[7]](#7-other-tasks) follow other ML/DL strategies   -->
<p align='center'>
  <strong><a href='#0-benchmarks-and-datasets'>0) Benchmarks and datasets </a></strong>
  <br>
  <a href="#01-sequence-datasets-benchmarks">Sequence dataset/benchmarks</a> •
  <a href="#02-structure-datasets-benchmarks">Structure datasets/benchmarks</a> •
  <a href="#03-databases">Public database</a> •
  <a href="#04-similar-list">Similar list</a> •
  <a href="#05-guides">Guides</a>
  <br>
  <strong><a href="#1-reviews">1) Reviews and surveys</a></strong>
  <br>
  <a href="#11-de-novo-protein-design">De novo design</a> •
  <a href="#12-antibody-design">Antibody design</a> •
  <a href="#13-peptide-design">Peptide design</a> •
  <a href="#14-binder-design">Binder design</a> •
  <a href="#15-enzyme-design">Enzyme design</a>
  <br>
  <strong><a href="#2-model-based-design">2) Model-based design</a></strong>
  <br>
  <a href="#21-structure-prediction-model-based">Structure Prediction Model-based</a> •
  <a href="#22-cm-align">CM-Align</a> •
  <a href="#23-msa-transformer-based">MSA transformer-based</a> •
  <a href="#24-llm-based">LLM-based</a> •
  <a href="#25-sampling-algorithms">Sampling-algorithms</a>
  <br>
  <strong><a href="#3-function-to-scaffold" class="large-link">3) Function to Scaffold</a></strong>
  <br>
  <a href="#31-gan-based">GAN-based</a> •
  <a href="#32-autoencoder-based">AutoEncoder-based</a> •
  <a href="#33-mlp-based">MLP-based</a> •
  <a href="#34-diffusion-based">Diffusion-based</a> •
  <a href="#35-rl-based">RL-based</a> •
  <a href="#36-flow-based">Flow-based</a> •
  <a href="#37-score-based">Score-based</a> •
  <a href="#38-autoregressive">Autoregressive</a>
  <br>
  <strong><a href="#4scaffold-to-sequence">4) Scaffold to Sequence</a></strong>
  <br>
  <a href="#40-review">Review</a> •
  <a href="#41-mlp-based">MLP-based</a> •
  <a href="#42-vae-based">VAE-based</a> •
  <a href="#43-lstm-based">LSTM-based</a> •
  <a href="#44-cnn-based">CNN-based</a> •
  <a href="#45-gnn-based">GNN-based</a> •
  <a href="#46-gan-based">GAN-based</a> •
  <a href="#47-transformer-based">Transformer-based</a> •
  <a href="#48-resnet-based">ResNet-based</a> •
  <a href="#49-diffusion-based">Diffusion-based</a> •
  <a href="#410-bayesian-based">Bayesian method</a> •
  <a href="#411-flow-based">Flow-based</a> •
  <a href="#412-rl-based">RL-based</a> •
  <a href="#413-train-method">Train method</a>
  <br>
  <strong><a href="#5function-to-sequence">5) Function to Sequence</a></strong>
  <br>
  <a href="#51-cnn-based">CNN-based</a> •
  <a href="#52-vae-based">VAE-based</a> •
  <a href="#53-gan-based">GAN-based</a> •
  <a href="#54-transformer-based">Transformer-based</a> •
  <a href="#55-bayesian-based">Bayesian method</a> •
  <a href="#56-rl-based">Reinforcement Learning</a> •
  <a href="#57-flow-based">Flow-based</a> •
  <a href="#58-rnn-based">RNN-based</a> •
  <a href="#59-lstm-based">LSTM-based</a> •
  <a href="#510-autoregressive-models">Autoregressive</a> •
  <a href="#511-boltzmann-machine-based">Boltzmann machine</a> •
  <a href="#512-diffusion-based">Diffusion-based</a> •
  <a href="#513-gnn-based">GNN-based</a> •
  <a href="#514-score-based">Score-based</a>
  <br>
  <strong><a href="#6-function-to-structure">6) Function to Structure</a></strong>
  <br>
  <a href="#60-review">Review</a> •
  <a href="#61-lstm-based">LSTM-based</a> •
  <a href="#62-diffusion-based">Diffusion-based</a> •
  <a href="#63-rosettafold-based">RoseTTAFold-based</a> •
  <a href="#64-cnn-based">CNN-based</a> •
  <a href="#65-gnn-based">GNN-based</a> •
  <a href="#66-transformer-based">Transformer-based</a> •
  <a href="#67-mlp-based">MLP-based</a> •
  <a href="#68-flow-based">Flow-based</a> •
  <a href="#69-alphafold-based">AlphaFold-based</a>
  <br>
  <strong><a href="#7-other-tasks">7) Other</a></strong>
  <br>
  <a href="#71-effects-of-mutation--fitness-landscape">Effects of mutations & Fitness Landscape</a>  •
  <a href="#72-protein-language-models-plm-and-representation-learning">Protein Language Model & Representation Learning</a>  •
  <a href="#73-molecular-design-models">Molecular Design Model</a> •
  <a href="#74-framework">Framework</a> •
  <a href="#75-unclassified">Unclassified</a>
</p>

---

## 0. Benchmarks and datasets

### 0.1 Sequence Datasets, Benchmarks

**FLIP: Benchmark tasks in fitness landscape inference for proteins**
Christian Dallago, Jody Mou, Kadina E Johnston, Bruce Wittmann, Nick Bhattacharya, Samuel Goldman, Ali Madani, Kevin K Yang
[NeurIPS 2021 Datasets and Benchmarks Track](https://openreview.net/forum?id=p2dMLEwL8tF)/[bioRxiv 2021](https://www.biorxiv.org/content/10.1101/2021.11.09.467890v2) • [website](https://benchmark.protein.properties/) • [code](https://github.com/J-SNACKKB/FLIP) • [Supplementary](https://www.biorxiv.org/content/biorxiv/early/2022/01/19/2021.11.09.467890/DC1/embed/media-1.pdf)

**A Benchmark Framework for Evaluating Structure-to-Sequence Models for Protein Design**
Jeffrey Chan, Seyone Chithrananda, David Brookes, Sam Sinai
Paper unavailable at [Machine Learning in Structural Biology Workshop 2022](https://nips.cc/Conferences/2022/ScheduleMultitrack?event=50005)

**PDBench: Evaluating Computational Methods for Protein-Sequence Design**
Leonardo V Castorina, Rokas Petrenas, Kartic Subr, Christopher W Wood
[Bioinformatics, 2023;, btad027](https://academic.oup.com/bioinformatics/advance-article/doi/10.1093/bioinformatics/btad027/6986968) • [code](https://github.com/wells-wood-research/PDBench)

**Benchmarking deep generative models for diverse antibody sequence design**
Igor Melnyk, Payel Das, Vijil Chenthamarakshan, Aurelie Lozano
[arXiv:2111.06801](https://arxiv.org/abs/2111.06801)

**The Protein Engineering Tournament: An Open Science Benchmark for Protein Modeling and Design**
Chase Armer, Hassan Kane, Dana Cortade, Dave Estell, Adil Yusuf, Radhakrishna Sanka, Henning Redestig, TJ Brunette, Pete Kelly, Erika DeBenedictis
[arXiv:2309.09955](https://arxiv.org/abs/2309.09955v2)

**Computational Scoring and Experimental Evaluation of Enzymes Generated by Neural Networks**
Sean R.Johnson, Xiaozhi Fu, Sandra Viknander, Clara Goldin, Sarah Monaco, Aleksej Zelezniak, Kevin K. Yang
[bioRxiv (2023)](https://www.biorxiv.org/content/10.1101/2023.03.04.531015v2) • [code](https://github.com/seanrjohnson/protein_scoring)

**FLOP: Tasks for Fitness Landscapes Of Protein Wildtypes**
Peter Mørch Groth, Richard Michael, Jesper Salomon, Pengfei Tian, Wouter Boomsma
[bioRxiv 2023.06.21.545880](https://www.biorxiv.org/content/10.1101/2023.06.21.545880v2) • [code](https://github.com/petergroth/FLOP)

**ProteinGym: Large-Scale Benchmarks for Protein Design and Fitness Prediction**
Pascal Notin, Aaron W Kollasch, Daniel Ritter, Lood van Niekerk, Steffanie Paul, Hansen Spinner, Nathan Rollins, Ada Shaw, Ruben Weitzman, Jonathan Frazer, Mafalda Dias, Dinko Franceschi, Rose Orenbuch, Yarin Gal, Debora S Marks
[bioRxiv 2023.12.07.570727](https://biorxiv.org/content/10.1101/2023.12.07.570727v1) • [code](https://github.com/OATML-Markslab/ProteinGym)

**Results of the Protein Engineering Tournament: An Open Science Benchmark for Protein Modeling and Design**
Chase Armer, Hassan Kane, Dana L. Cortade, Henning Redestig, David A. Estell, Adil Yusuf, Nathan Rollins, Hansen Spinner, Debora Marks, TJ Brunette, Peter J. Kelly, Erika DeBenedictis
[bioRxiv 2024.08.12.606135](https://www.biorxiv.org/content/10.1101/2024.08.12.606135v1)/[Proteins: Structure, Function, and Bioinformatics (2025)](https://onlinelibrary.wiley.com/doi/10.1002/prot.70008) • [code](https://github.com/the-protein-engineering-tournament/pet-pilot-2023) • [Supplementary](https://www.biorxiv.org/content/biorxiv/early/2024/08/12/2024.08.12.606135/DC1/embed/media-1.pdf)

**Generative AI Models for the Protein Scaffold Filling Problem**
Letu Qingge, Kushal Badal, Richard Annan, Jordan Sturtz, Xiaowen Liu, and Binhai Zhu
[Journal of Computational Biology](https://www.liebertpub.com/doi/10.1089/cmb.2024.0510)

**Benchmarking Inverse Folding Models for Antibody CDR Sequence Design**
Per Junior Greisen, Yifan Li, Yuxiang Lang, Chenrui Xu, Yi Zhou, Ziwei Pang
[bioRxiv 2024.12.16.628614](https://www.biorxiv.org/content/10.1101/2024.12.16.628614v1)

**Self-supervised machine learning methods for protein design improve sampling but not the identification of high-fitness variants**
Moritz Ertelt, Rocco Moretti, Jens Meiler, and Clara T. Schoeder
[Science Advances 11.7 (2025)](https://www.science.org/doi/10.1126/sciadv.adr7338) • [code](https://github.com/meilerlab/probabilities_design)

**Crowdsourced Protein Design: Lessons From the Adaptyv EGFR Binder Competition**
Tudor-Stefan Cotet, Igor Krawczuk, Filippo Stocco, Noelia Ferruz, Anthony Gitter, Yoichi Kurumida, Lucas de Almeida Machado, Francesco Paesani, Cianna N. Calia, Chance A. Challacombe, Nikhil Haas, Ahmad Qamar, Bruno E. Correia, Martin Pacesa, Lennart Nickel, Kartic Subr, Leonardo V. Castorina, Maxwell J. Campbell, Constance Ferragu, Patrick Kidger, Logan Hallee, Christopher W. Wood, Michael J. Stam, Tadas Kluonis, Suleyman Mert Unal, Elian Belot, Alexander Naka, Adaptyv Competition Organizers
[bioRxiv 2025.04.17.648362](https://www.biorxiv.org/content/10.1101/2025.04.17.648362v2) • [github](https://github.com/adaptyvbio/egfr2024_post_competition)

**Experimental Evaluation of AI-Driven Protein Design Risks Using Safe Biological Proxies**  
Svetlana P. Ikonomova, Bruce J. Wittmann, Fernanda Piorino, David J. Ross, Samuel W. Schaffter, Olga Vasilyeva, Eric Horvitz, James Diggans, Elizabeth A. Strychalski, Sheng Lin-Gibson, Geoffrey J. Taghon  
[bioRxiv 2025.05.15.654077](https://www.biorxiv.org/content/10.1101/2025.05.15.654077v1) • [code](https://github.com/usnistgov/AIPD_TEVV/)

**Benchmark for Antibody Binding Affinity Maturation and Design**  
Xinyan Zhao, Yi-Ching Tang, Akshita Singh, Victor J Cantu, KwanHo An, Junseok Lee, Adam E Stogsdill, Ashwin Kumar Ramesh, Zhiqiang An, Xiaoqian Jiang, Yejin Kim  
[arXiv:2506.04235](https://arxiv.org/abs/2506.04235) • [dataset](https://huggingface.co/datasets/AbBibench/Antibody_Binding_Benchmark_Dataset) • [code](https://github.com/MSBMI-SAFE/AbBiBench)

**The Dayhoff Atlas: scaling sequence diversity for improved protein generation**  
Kevin K. Yang, Sarah Alamdari, Alex J. Lee, Kaeli Kaymak-Loveless, Samir Char, Garyk Brixi, Carles Domingo-Enrich, Chentong Wang, Suyue Lyu, Nicolo Fusi, Neil Tenenholtz, Ava P. Amini  
[bioRxiv 2025.07.21.665991](https://www.biorxiv.org/content/10.1101/2025.07.21.665991v1) • [code](https://github.com/microsoft/dayhoff) • [dataset](https://huggingface.co/collections/microsoft/dayhoff-atlas-6866d679465a2685b06ee969)

**Consistent Synthetic Sequences Unlock Structural Diversity in Fully Atomistic De Novo Protein Design**  
Danny Reidenbach, Zhonglin Cao, Zuobai Zhang, Kieran Didi, Tomas Geffner, Guoqing Zhou, Jian Tang, Christian Dallago, Arash Vahdat, Emine Kucukbenli, Karsten Kreis  
[arXiv:2512.01976](https://arxiv.org/abs/2512.01976)

**Benchmarking Generative AI Protein Models Reveals Differences Between Structural and Sequence-based Approaches**  
Alexander J Barnett , Rajendra KC , Pratikshya Pandey , Pamodha Somasiri , Kirsten A Fairfax , Sandy Hung , Alex W Hewitt  
[Genomics, Proteomics & Bioinformatics (2026)](https://academic.oup.com/gpb/advance-article/doi/10.1093/gpbjnl/qzag014/8487189)

**AFD-INSTRUCTION: A Comprehensive Antibody Instruction Dataset with Functional Annotations for LLM-Based Understanding and Design**  
Ling Luo, Wenbin Jiang, Hongyuan Chang, Xinkang Wang, Xushi Zhang, Yueting Xiong, Mengsha Tong, Rongshan Yu  
[arXiv:2602.04916](https://arxiv.org/abs/2602.04916) • [code](https://github.com/dumbgoos/Afd-Instruction/) • [dataset](https://huggingface.co/datasets/LLMasterLL/AFD) • [website](https://afd-instruction.github.io/)

**Benchmarking and behavioral characterization of LLM agents for protein design**  
Jeonghyeon Kim, Philip Romero  
[bioRxiv 2026.05.06.723381](https://www.biorxiv.org/content/10.64898/2026.05.06.723381v2) • [code](https://github.com/RomeroLab/BioDesignBench)

### 0.2 Structure Datasets, Benchmarks

**AlphaDesign: A graph protein design method and benchmark on AlphaFoldDB**
Zhangyang Gao, Cheng Tan, Stan Z. Li
[arxiv (2022)](https://arxiv.org/abs/2202.01079)

**SidechainNet: An All-Atom Protein Structure Dataset for Machine Learning**
Jonathan E. King, David Ryan Koes
[arxiv](https://arxiv.org/abs/2010.08162) • [github::sidechainnet](https://github.com/jonathanking/sidechainnet)

[TDC](https://tdcommons.ai/overview/) maintains a resource list that currently contains 22 tasks (and its datasets) related to small molecules and macromolecules, including PPI, DDI and so on. [MoleculeNet](https://github.com/GLambard/Molecules_Dataset_Collection) published a small molecule related benchmark four years ago.

> In terms of datasets and benchmarks, protein design is far less mature than drug discovery ([paperwithcode drug discovery benchmarks](https://paperswithcode.com/task/drug-discovery)). (Maybe should add the evaluation of protein design for deep learning method (especially deep generative model))
> Difficulties and opportunities always coexist. Happy to see the work of [Christian Dallago, Jody Mou, Kadina E. Johnston, Bruce J. Wittmann, Nicholas Bhattacharya, Samuel Goldman, Ali Madani, Kevin K. Yang](https://www.biorxiv.org/content/10.1101/2021.11.09.467890v1) and [Zhangyang Gao, Cheng Tan, Stan Z. Li](https://arxiv.org/abs/2202.01079).

**Sampling of structure and sequence space of small protein folds**
Thomas W. Linsky, Kyle Noble, Autumn R. Tobin, Rachel Crow, Lauren Carter, Jeffrey L. Urbauer, David Baker & Eva-Maria Strauch
[Nat Commun 13, 7151 (2022)](https://www.nature.com/articles/s41467-022-34937-8) • [code](https://github.com/strauchlab/scaffold_design) • [Supplementary](https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-022-34937-8/MediaObjects/41467_2022_34937_MOESM1_ESM.pdf)

**OpenProteinSet: Training data for structural biology at scale**
Gustaf Ahdritz, Nazim Bouatta, Sachin Kadyan, Lukas Jarosch, Daniel Berenberg, Ian Fisk, Andrew M. Watkins, Stephen Ra, Richard Bonneau, Mohammed AlQuraishi
[arXiv:2308.05326](https://arxiv.org/abs/2308.05326) • [OpenFold](https://github.com/aqlaboratory/openfold)

**ProteinInvBench: Benchmarking Protein Design on Diverse Tasks, Models, and Metrics**
Zhangyang Gao, Cheng Tan, Yijie Zhang, Xingran Chen, Stan Z. Li
[GitHub](https://github.com/A4Bio/ProteinInvBench)

**PDB-Struct: A Comprehensive Benchmark for Structure-based Protein Design**
Chuanrui Wang, Bozitao Zhong, Zuobai Zhang, Narendra Chaudhary, Sanchit Misra, Jian Tang
[arXiv preprint arXiv:2312.00080 (2023)](https://arxiv.org/abs/2312.00080) • [code](https://github.com/WANG-CR/PDB-Struct)

**Scaffold-Lab: Critical Evaluation and Ranking of Protein Backbone Generation Methods in A Unified Framework**
Zhuoqi Zheng, Bo Zhang, Bozitao Zhong, Kexin Liu, Jinyu Yu, Zhengxin Li, JunJie Zhu, Ting Wei, Hai-Feng Chen
[bioRxiv 2024.02.10.579743](https://www.biorxiv.org/content/10.1101/2024.02.10.579743v1) • [code](https://github.com/Immortals-33/Scaffold-Lab) • [Supplementary](https://www.biorxiv.org/content/biorxiv/early/2024/02/12/2024.02.10.579743/DC1/embed/media-1.pdf)

**Antibody DomainBed: Out-of-Distribution Generalization in Therapeutic Protein Design**
Nataša Tagasovska, Ji Won Park, Matthieu Kirchmeyer, Nathan C. Frey, Andrew Martin Watkins, Aya Abdelsalam Ismail, Arian Rokkum Jamasb, Edith Lee, Tyler Bryson, Stephen Ra, Kyunghyun Cho
[arXiv:2407.21028](https://arxiv.org/abs/2407.21028) • [code](https://github.com/prescient-design/antibody-domainbed) • [dataset](https://www.dropbox.com/scl/fo/e670i9adp29yv2knfu6wd/h?rlkey=uax6phjjfumkk8xoxrbwcit1h&e=1&dl=0)

**Large protein databases reveal structural complementarity and functional locality**
Paweł Szczerbiak, Lukasz Szydlowski, Witold Wydmański, P. Douglas Renfrew, Julia Koehler Leman, Tomasz Kosciolek
[bioRxiv 2024.08.14.607935](https://www.biorxiv.org/content/10.1101/2024.08.14.607935v1) • [code](https://github.com/Tomasz-Lab/protein-structure-landscape) • [Supplementary](https://www.biorxiv.org/content/biorxiv/early/2024/08/14/2024.08.14.607935/DC1/embed/media-1.pdf) • [website](https://protein-structure-landscape.sano.science/)

**The Protein Design Archive (PDA): insights from 40 years of protein design**
Marta Chronowska, Michael J. Stam, Derek N. Woolfson, Luigi F. Di Constanzo, Christopher W. Wood
[bioRxiv 2024.09.05.611465](https://www.biorxiv.org/content/10.1101/2024.09.05.611465v1)/[Nat Biotechnol (2025)](https://www.nature.com/articles/s41587-025-02607-x) • [code](https://github.com/wells-wood-research/chronowska-stam-wood-2024-protein-design-archive) • [Supplementary](hhttps://www.biorxiv.org/content/biorxiv/early/2024/09/07/2024.09.05.611465/DC1/embed/media-1.docx) • [website](https://pragmaticproteindesign.bio.ed.ac.uk/pda/)

**ProteinBench: A Holistic Evaluation of Protein Foundation Models**
Fei Ye, Zaixiang Zheng, Dongyu Xue, Yuning Shen, Lihao Wang, Yiming Ma, Yan Wang, Xinyou Wang, Xiangxin Zhou, Quanquan Gu
[arXiv:2409.06744](https://arxiv.org/abs/2409.06744) • [code](https://proteinbench.github.io/)

**Benchmarking Generative Models for Antibody Design & Exploring Log-Likelihood for Sequence Ranking**
Talip Uçar, Cedric Malherbe, Ferran Gonzalez
[bioRxiv 2024.10.07.617023](https://www.biorxiv.org/content/10.1101/2024.10.07.617023v3) • [code](https://github.com/AstraZeneca/DiffAbXL)

**Towards Robust Evaluation of Protein Generative Models: A Systematic Analysis of Metrics**
Pavel Strashnov, Andrey Shevtsov, Viacheslav Meshchaninov, Maria Ivanova, Fedor Nikolaev, Olga Kardymon, Dmitry Vetrov
[bioRxiv 2024.10.25.620213](https://www.biorxiv.org/content/10.1101/2024.10.25.620213v1)

**MotifBench: A standardized protein design benchmark for motif-scaffolding problems**
Zhuoqi Zheng, Bo Zhang, Kieran Didi, Kevin K. Yang, Jason Yim, Joseph L. Watson, Hai-Feng Chen, Brian L. Trippe
[arXiv:2502.12479](https://arxiv.org/abs/2502.12479) • [code](https://github.com/blt2114/MotifBench)

**Systematic comparison of Generative AI-Protein Models reveals fundamental differences between structural and sequence-based approaches**
Alexander J Barnett, KC Rajendra, Pratikshya Pandey, Pamodha Somasiri, Kirsten A Fairfax, Sandy Hung, Alex W Hewitt
[bioRxiv 2025.03.23.644844](https://www.biorxiv.org/content/10.1101/2025.03.23.644844v1) • [code](https://github.com/hewittlab/Systematic-comparison-of-Generative-AI-Protein-Models) • [Supplementary](https://www.biorxiv.org/content/biorxiv/early/2025/03/24/2025.03.23.644844/DC1/embed/media-1.docx)

**Conformation-specific Design: a New Benchmark and Algorithm with Application to Engineer a Constitutively Active Map Kinase**  
Jacob A. Stern, Siba Alharbi, Anandsukeerthi Sandholu, Stefan T. Arold, Dennis Della Corte  
[bioRxiv 2025.04.23.650138](https://www.biorxiv.org/content/10.1101/2025.04.23.650138v1) • [code](https://github.com/dellacortelab/cs_design) • [dataset](https://github.com/dellacortelab/motif_div)

**PRIDE-New-Benchmark-Dataset-For-Protein-Structural-Design**  
Hanqun CAO, dchenhe  
[github](https://github.com/chq1155/PRIDE_Benchmark_ProteinDesign)

**Protein FID: Improved Evaluation of Protein Structure Generative Models**  
Felix Faltings, Hannes Stark, Tommi Jaakkola, Regina Barzilay  
[arXiv:2505.08041](https://arxiv.org/abs/2505.08041)

**PDFBench: A Benchmark for De novo Protein Design from Function**  
Jiahao Kuang, Nuowei Liu, Changzhi Sun, Tao Ji, Yuanbin Wu  
[arXiv:2505.20346](https://arxiv.org/abs/2505.20346) • [website](https://pdfbench.github.io/) • [code](https://github.com/pdfbench/PDFBench)

**An improved model for prediction of de novo designed proteins with diverse geometries**  
Benjamin Orr, Stephanie E Crilly, Deniz Akpinaroglu, Eleanor Zhu, Michael J. Keiser, Tanja Kortemme  
[bioRxiv 2025.06.02.657515](https://www.biorxiv.org/content/10.1101/2025.06.02.657515v1)

**Protein-SE(3): Benchmarking SE(3)-based Generative Models for Protein Structure Design**  
Lang Yu, Zhangyang Gao, Cheng Tan, Qin Chen, Jie Zhou, Liang He
[arXiv:2507.20243](https://arxiv.org/abs/2507.20243v1)

**Evaluating zero-shot prediction of protein design success by AlphaFold, ESMFold, and ProteinMPNN**  
Mario Garcia, Gabriel Jacob Rocklin, Sugyan Dixit  
[bioRxiv 2025.07.29.667290](https://www.biorxiv.org/content/10.1101/2025.07.29.667290v1)

**Predicting Experimental Success in De Novo Binder Design: A Meta-Analysis of 3,766 Experimentally Characterised Binders**  
Max Daniel Overath, Andreas Rygaard, Christian Peder Jacobsen, Valentas Brasas, Oliver Morell, Pietro Sormanni, Timothy Patrick Jenkins  
[bioRxiv 2025.08.14.670059](https://www.biorxiv.org/content/10.1101/2025.08.14.670059v1) • [dataset](https://zenodo.org/records/15722219)

**Limitations of the refolding pipeline for de novo protein design**  
Kerlen T. Korbeld, Vsevolod Viliuga, Maximilian J.L.J. Fürst  
[bioRxiv 2025.12.09.693122](https://www.biorxiv.org/content/10.64898/2025.12.09.693122v1) • [Supplementary](https://www.biorxiv.org/content/biorxiv/early/2025/12/11/2025.12.09.693122/DC1/embed/media-1.pdf) • [data](https://github.com/kt-korbeld/Limitations-refolding-pipeline-data)

**Assessment of Generative De Novo Peptide Design Methods for G Protein-Coupled Receptors**  
Hannes Junker, Clara T. Schoeder  
[bioRxiv 2026.02.26.708415](https://www.biorxiv.org/content/10.64898/2026.02.26.708415v1)

**ProtDBench: A Unified Benchmark of Protein Binder Design and Evaluation**  
Cong Liu, Milong Ren, Jiaqi Guan, Chengyue Gong, Jinyuan Sun, Xinshi Chen, Wenzhi Xiao  
[arXiv:2605.04118](https://arxiv.org/abs/2605.04118)

### 0.3 Databases

> A list of suggested protein databases, more lists at [CNCB](https://ngdc.cncb.ac.cn/databasecommons/).

#### 0.3.1 Sequence Database

1. [UniProt](https://www.uniprot.org/downloads)
2. [DisProt](https://disprot.org)
3. [MobiDB](https://mobidb.bio.unipd.it/)
4. [Peptipedia](https://app.peptipedia.cl/)

#### 0.3.2 Structure Database

| Database                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [PDB](https://www.rcsb.org/)                                   | The Protein Data Bank (PDB) is a database of 3D structural data of large biological molecules, such as proteins and nucleic acids. These data are gathered using experimental methods such as X-ray crystallography, NMR spectroscopy, or cryo-electron microscopy                                                                                                                                                                                                                                                                |
| [AlphaFoldDB](https://alphafold.ebi.ac.uk/)                    | AlphaFoldDB is a database of protein structure predictions produced by DeepMind's AlphaFold system. It provides highly accurate predictions of protein 3D structures                                                                                                                                                                                                                                                                                                                                                              |
| [PDBbind](http://www.pdbbind.org.cn/download.php)              | PDBbind is a comprehensive collection of the binding data of all types of biomolecular complexes in the PDB database. It is primarily used for the development and validation of computational methods for predicting molecular interactions                                                                                                                                                                                                                                                                                      |
| [AB-Bind](https://github.com/sarahsirin/AB-Bind-Database)      | AB-Bind is a database for antibody binding affinity data. It offers a curated set of experimental binding data and corresponding antibody-protein complex structures                                                                                                                                                                                                                                                                                                                                                              |
| [AntigenDB](http://crdd.osdd.net/raghava/antigendb/)           | AntigenDB is a manually curated database of experimentally verified antigens that includes detailed information about the antigen, the source organism, and the associated antibodies                                                                                                                                                                                                                                                                                                                                             |
| [CAMEO](https://www.cameo3d.org/)                              | CAMEO (Continuous Automated Model EvaluatiOn) is a project for the automated evaluation of methods predicting macromolecular structure. It continuously assesses the performance of automated protein structure prediction servers                                                                                                                                                                                                                                                                                                |
| [CAPRI](https://www.ebi.ac.uk/msd-srv/capri/)                  | The Critical Assessment of PRediction of Interactions (CAPRI) is a community-wide experiment to evaluate protein-protein interaction prediction methods                                                                                                                                                                                                                                                                                                                                                                           |
| [PIFACE](http://prism.ccbb.ku.edu.tr/piface)                   | PIFACE is a web server for the prediction of protein-protein interactions. It identifies potential interaction interfaces on protein surfaces                                                                                                                                                                                                                                                                                                                                                                                     |
| [SAbDab](http://opig.stats.ox.ac.uk/webapps/newsabdab/sabdab/) | The Structural Antibody Database (SAbDab) is an automatically updated resource for the structural information of antibodies from the PDB. It allows for easy access to curated, annotated, and classified antibody structures                                                                                                                                                                                                                                                                                                     |
| [SKEMPI v2.0](https://life.bsc.es/pid/skempi2)                 | SKEMPI 2.0 is a database of experimental measurements of the change in binding free energy caused by mutations in protein-protein complexes                                                                                                                                                                                                                                                                                                                                                                                       |
| [ProtCAD](http://dunbrack2.fccc.edu/protcad/)                  | ProtCAD is a suite of tools for the design and engineering of novel protein structures, sequences, and functions. It allows users to build and manipulate complex protein structures, generate and evaluate sequence libraries, and simulate mutational effects. ProtCAD is a suite of tools for the design and engineering of novel protein structures, sequences, and functions. It allows users to build and manipulate complex protein structures, generate and evaluate sequence libraries, and simulate mutational effects. |
| [Proteinbase](https://proteinbase.com/)|The home of protein design data. An open platform by [adaptyvbio](http://adaptyvbio.com/) for sharing protein designs, their experimental validation and their design methods.|

### 0.4 Similar List

> Some similar GitHub lists that include papers about protein design using deep learning:

1. [design_tools](https://github.com/hefeda/design_tools/blob/main/README.md)
2. [awesome-AI-based-protein-design](https://github.com/opendilab/awesome-AI-based-protein-design)
3. [ProteinStructureWithDL](https://github.com/Yang-J-LIN/ProteinStructureWithDL)
4. [List of available bioinformatic tools and services](https://neurosnap.ai/services)

### 0.5 Guides

Guides/Tutorials for beginners on GitHub:

1. [how_to_create_a_protein](https://github.com/universvm/how_to_create_a_protein)
2. [protein-design-tutorials](https://github.com/ProteinDesignLab/protein-design-tutorials)
3. [AI-driven-protein-design](https://github.com/miangoar/AI-driven-protein-design/tree/main)
4. [Deep Learning for Proteins Notebook Series Teaches AI for Biomolecular Structure Prediction and Design](https://thebiophysicist.kglmeridian.com/view/journals/biop/7/1/article-p16.xml)

Collection of Protein Design Labs:

- [ProteinDesignLabs](https://github.com/Zuricho/ProteinDesignLabs)
- [proteindesigngroups](https://ullahsamee.github.io/proteindesigngroups/)

## 1. Reviews

### 1.1 De novo protein design

**Protein design: from computer models to artificial intelligence**
Antonella Paladino, Filippo Marchetti, Silvia Rinaldi, Giorgio Colombo
[Wiley Interdisciplinary Reviews: Computational Molecular Science 7.5 (2017): e1318](https://wires.onlinelibrary.wiley.com/doi/10.1002/wcms.1318)

**Advances in protein structure prediction and design**
Brian Kuhlman, Philip Bradley
[Nat Rev Mol Cell Biol 20, 681-697 (2019)](https://www.nature.com/articles/s41580-019-0163-x)

**Deep learning in protein structural modeling and design**
Wenhao Gao, Sai Pooja Mahajan, Jeremias Sulam, and Jeffrey J. Gray
[Patterns 1.9](https://www.sciencedirect.com/science/article/pii/S2666389920301902) • 2020

**100th anniversary of macromolecular science viewpoint: Data-driven protein design**
Ferguson, Andrew L., and Rama Ranganathan
[ACS Macro Letters 10.3 (2021)](https://pubs.acs.org/doi/abs/10.1021/acsmacrolett.0c00885)

**Artificial intelligence in early drug discovery enabling precision medicine**
Fabio Bonioloa, Emilio Dorigattia, Alexander J. Ohnmachta, Dieter Saurb, Benjamin Schuberta, and Michael P. Menden
[Expert Opinion on Drug Discovery 16.9 (2021)](https://www.tandfonline.com/doi/full/10.1080/17460441.2021.1918096)

**Protein design with deep learning**
Defresne, Marianne, Sophie Barbe, and Thomas Schiex
[International Journal of Molecular Sciences 22.21 (2021)](https://www.mdpi.com/1422-0067/22/21/11741)

**Protein sequence design with deep generative models**
Zachary Wu, Kadina E. Johnston, Frances H. Arnold, Kevin K. Yang
[Current Opinion in Chemical Biology 65](https://www.sciencedirect.com/science/article/pii/S136759312100051X) • [note](https://zhuanlan.zhihu.com/p/466616309) • 2021

**Structure-based protein design with deep learning**
Ovchinnikov, Sergey, and Po-Ssu Huang
[Current opinion in chemical biology 65](https://www.sciencedirect.com/science/article/pii/S1367593121001125) • [note](https://zhuanlan.zhihu.com/p/467001175) • 2021

**Deep learning techniques have significantly impacted protein structure prediction and protein design**
Pearce, Robin, and Yang Zhang
[Current opinion in structural biology 68 (2021)](https://www.sciencedirect.com/science/article/pii/S0959440X21000142)

**Recent advances in de novo protein design: Principles, methods, and applications**
Pan, Xingjie, and Tanja Kortemme
[Journal of Biological Chemistry 296 (2021)](https://www.sciencedirect.com/science/article/pii/S0021925821003367)

**Protein design via deep learning**
Wenze Ding, Kenta Nakai, Haipeng Gong
[Briefings in Bioinformatics](https://academic.oup.com/bib/advance-article/doi/10.1093/bib/bbac102/6554124) • 25 March 2022

**Deep generative modeling for protein design**
Strokach, Alexey, and Philip M. Kim
[Current Opinion in Structural Biology](https://www.sciencedirect.com/science/article/pii/S0959440X21001573) • 2022

**Dawn of a new era for membrane protein design**
Sowlati-Hashjin, Shahin, Aanshi Gandhi, and Michael Garton
[BioDesign Research (2022)](https://spj.science.org/doi/10.34133/2022/9791435)

**Deep learning approaches for conformational flexibility and switching properties in protein design**
Rudden, Lucas SP, Mahdi Hijazi, and Patrick Barth
[Frontiers in Molecular Biosciences](https://www.frontiersin.org/articles/10.3389/fmolb.2022.928534/full)

**Computational protein design with evolutionary-based and physics-inspired modeling: current and future synergies**
Cyril Malbranke, David Bikard, Simona Cocco, Rémi Monasson, Jérôme Tubiana
[arXiv:2208.13616v2](https://arxiv.org/abs/2208.13616v2)

**From sequence to function through structure: deep learning for protein design**
Noelia Ferruz, Michael Heinzinger, Mehmet Akdel, Alexander Goncearenco, Luca Naef, Christian Dallago
[bioRxiv 2022.08.31.505981](https://www.biorxiv.org/content/10.1101/2022.08.31.505981v1)/[Computational and Structural Biotechnology Journal Volume 21, 2023](https://www.sciencedirect.com/science/article/pii/S2001037022005086) • [Supplementary](https://www.biorxiv.org/content/biorxiv/early/2022/09/03/2022.08.31.505981/DC1/embed/media-1.pdf) • [accompanying list](https://github.com/hefeda/design_tools/blob/main/README.md)

**Computational protein design with data-driven approaches: Recent developments and perspectives**
Haiyan Liu, Quan Chen
[WIREs Comput Mol Sci. 2022. e1646](https://wires.onlinelibrary.wiley.com/doi/10.1002/wcms.1646)

**Understanding by design: Implementing deep learning from protein structure prediction to protein design**
Gao, Yuanxu, Jiangshan Zhan, and Albert CH Yu
[MedComm-Future Medicine 1.2 (2022): e22](https://onlinelibrary.wiley.com/doi/full/10.1002/mef2.22)

**Diffusion Models in Bioinformatics: A New Wave of Deep Learning Revolution in Action**
Zhiye Guo, Jian Liu, Yanli Wang, Mengrui Chen, Duolin Wang, Dong Xu, Jianlin Cheng
[arXiv:2302.10907](https://arxiv.org/abs/2302.10907)

**Machine learning for evolutionary-based and physicsinspired protein design: Current and future synergies**
Cyril Malbranke, David Bikard, Simona Cocco, Rémi Monasson, Jérôme Tubiana
[Current Opinion in Structural Biology](https://www.sciencedirect.com/science/article/pii/S0959440X23000453)

**De novo design of polyhedral protein assemblies: before and after the AI revolution**
Bhoomika Basu Mallik, Jenna Stanislaw, Tharindu Madhusankha Alawathurage, and Alena Khmelinskaia
[ChemBioChem 2023, e202300117](http://dx.doi.org/10.1002/cbic.202300117)

**Research progress of artificial intelligence in protein design**
CHEN Zhihang, JI Menglin, QI Yifei
[Synthetic Biology Journal (2023)](https://synbioj.cip.com.cn/article/2023/2096-8280/2023-008.shtml)

**A Survey on Graph Diffusion Models: Generative AI in Science for Molecule, Protein and Material**
Mengchun Zhang, Maryam Qamar, Taegoo Kang, Yuna Jung, Chenshuang Zhang, Sung-Ho Bae, Chaoning Zhang
[https://arxiv.org/abs/2304.01565](https://arxiv.org/pdf/2304.01565.pdf)

**Exploring the Protein Sequence Space with Global Generative Models**
Sergio Romero-Romero, Sebastian Lindner, Noelia Ferruz
[arXiv:2305.01941](https://arxiv.org/abs/2305.01941)

**The Era of Machine Learning for Protein Design, Summarized in Four Key Methods**
LucianoSphere
[Towards Data Science](https://towardsdatascience.com/the-era-of-machine-learning-for-protein-design-summarized-in-four-key-methods-d6f1dac5de96)

**Is novelty predictable?**
Clara Fannjiang, Jennifer Listgarten
[arXiv:2306.00872](https://arxiv.org/abs/2306.00872)

**Computational protein design - where it goes?**
Xu Binbin, Chen Yingjun and Xue Weiwei
[Current Medicinal Chemistry 2023](https://www.eurekaselect.com/article/132267)

**How can the protein design community best support biologists who want to harness AI tools for protein structure prediction and design?**
Birte Höcker, Peilong Lu, Anum Glasgow, Debora S. Marks
Pranam Chatterjee, Joanna S.G. Slusky, Ora Schueler-Furman, Possu Huang
[Cell Systems 14.8 (2023)](https://www.cell.com/cell-systems/fulltext/S2405-4712(23)00212-0)

**De novo 設計ナノポアの創製**
新津藍
[生物工学会誌 101.8 (2023)](https://www.jstage.jst.go.jp/article/seibutsukogaku/101/8/101_101.8_431/_article/-char/ja/)

**Generative artificial intelligence for de novo protein design**
Adam Winnifrith, Carlos Outeiral, Brian Hie
[arXiv:2310.09685](https://arxiv.org/abs/2310.09685)

**Intelligent Protein Design and Molecular Characterization Techniques: A Comprehensive Review**
Jingjing Wang, Chang Chen, Ge Yao, Junjie Ding, Liangliang Wang and Hui Jiang
[Molecules 28.23 (2023)](https://www.mdpi.com/1420-3049/28/23/7865)

**Generative models for protein sequence modeling: recent advances and future directions**
Mehrsa Mardikoraem, Zirui Wang, Nathaniel Pascual, Daniel Woldring
[Briefings in Bioinformatics](https://academic.oup.com/bib/article/24/6/bbad358/7325909)

**A new age in protein design empowered by deep learning**
Hamed Khakzad, Ilia Igashov, Arne Schneuing, Casper Goverde, Michael Bronstein, Bruno Correia
[Cell Systems, Volume 14, Issue 11](https://www.cell.com/cell-systems/fulltext/S2405-4712(23)00298-3)

**Deep learning for protein structure prediction and design—progress and applications**
Jürgen Jänes and Pedro Beltrao
[Mol Syst Biol(2024)](https://www.embopress.org/doi/full/10.1038/s44320-024-00016-x)

**De novo protein design—From new structures to programmable functions**
Tanja Kortemme
[Cell 187.3 (2024)](https://www.cell.com/cell/fulltext/S0092-8674(23)01402-2)

**Generative models for protein structures and sequences**
Chloe Hsu, Clara Fannjiang & Jennifer Listgarten
[Nat Biotechnol 42, 196–199 (2024)](https://www.nature.com/articles/s41587-023-02115-w)

**What does it take for an ‘AlphaFold Moment’ in functional protein engineering and design?**
Roberto A. Chica & Noelia Ferruz
[Nat Biotechnol 42, 173–174 (2024)](https://www.nature.com/articles/s41587-023-02120-z)

**Protein design: the experts speak**
Anne Doerr
[Nat Biotechnol 42, 175–178 (2024)](https://www.nature.com/articles/s41587-023-02111-0)

**Machine learning for functional protein design**
Pascal Notin, Nathan Rollins, Yarin Gal, Chris Sander & Debora Marks
[Nat Biotechnol 42, 216–228 (2024)](https://www.nature.com/articles/s41587-024-02127-0)

**Sparks of function by de novo protein design**
Alexander E. Chu, Tianyu Lu & Po-Ssu Huang
[Nat Biotechnol 42, 203–215 (2024)](https://www.nature.com/articles/s41587-024-02133-2) • [poster](https://drive.google.com/file/d/1sG3OlEWvhHcWAdtf7RTcCawAapDmyeEx/view)

**A Survey of Generative AI for De Novo Drug Design: New Frontiers in Molecule and Protein Generation**
Xiangru Tang, Howard Dai, Elizabeth Knight, Fang Wu, Yunyang Li, Tianxiao Li, Mark Gerstein
[arXiv:2402.08703](https://arxiv.org/abs/2402.08703)

**Security challenges by AI-assisted protein design**
Philip Hunter
[EMBO Rep(2024)](https://www.embopress.org/doi/full/10.1038/s44319-024-00124-7)

**Opportunities and challenges in design and optimization of protein function**
Dina Listov, Casper A. Goverde, Bruno E. Correia & Sarel Jacob Fleishman
[Nat Rev Mol Cell Biol (2024)](https://www.nature.com/articles/s41580-024-00718-y)

**The State-of-the-Art Overview to Application of Deep Learning in Accurate Protein Design and Structure Prediction**
Saber Saharkhiz, Mehrnaz Mostafavi, Amin Birashk, Shiva Karimian, Shayan Khalilollah, Sohrab Jaferian, Yalda Yazdani, Iraj Alipourfard, Yun Suk Huh, Marzieh Ramezani Farani & Reza Akhavan-Sigari
[Top Curr Chem (Z) 382, 23 (2024)](https://link.springer.com/article/10.1007/s41061-024-00469-6)

**Computational methods for protein design**
Noelia Ferruz, Amelie Stein
[Protein Engineering, Design and Selection, Volume 37, 2024](https://academic.oup.com/peds/article/doi/10.1093/protein/gzae011/7710436)

**Structure-based protein and small molecule generation using EGNN and diffusion models: A comprehensive review**
Farzan Soleymani, Eric Paquet, Herna Lydia Viktor, Wojtek Michalowski
[Computational and Structural Biotechnology Journal (2024)](https://www.sciencedirect.com/science/article/pii/S2001037024002228)

**Machine learning in biological physics: From biomolecular prediction to design**
Jonathan Martin, Marcos Lequerica Mateos, José N. Onuchic, and Faruck Morcos
[Proceedings of the National Academy of Sciences 121.27 (2024)](https://www.pnas.org/doi/10.1073/pnas.2311807121)

**AI has dreamt up a blizzard of new proteins. Do any of them actually work?**
Ewen Callaway
[Nature 634.8034 (2024)](https://www.nature.com/articles/d41586-024-03335-z)

**Five protein-design questions that still challenge AI**
Sara Reardon
[Nature 635.8037 (2024)](https://www.nature.com/articles/d41586-024-03595-9)

**De novo protein design in the age of artificial intelligence**
Nan Liu, Xiaocheng Jin, Chongzhou Yang, Ziyang Wang, Xiaoping Min, Shengxiang Ge
[Sheng Wu Gong Cheng Xue Bao](https://doi.org/10.13345/j.cjb.240087)

**Generative Models in Protein Engineering: A Comprehensive Survey**
Chen Xinhui, Yiwen Yuan, Joseph Liu, Chak Tou Leong, Xiaoye Zhu, Jiaqi Chen
[Neurips 2024 Workshop](https://openreview.net/forum?id=Xc7l84S0Ao)

**A Survey of Deep Learning Methods in Protein Bioinformatics and its Impact on Protein Design**
Weihang Dai
[arXiv:2501.01477](https://arxiv.org/abs/2501.01477)

**The Promise of Protein Design: A Q&A with Nobel Laureate David Baker**
David Baker and Fay Lin
[GEN Biotechnology (2025)](https://www.liebertpub.com/doi/abs/10.1089/genbio.2025.0004?journalCode=genbio)

**Protein design and structure solution for drug discovery**
Petra Bombicz
[Crystallography Reviews (2024)](https://www.tandfonline.com/doi/full/10.1080/0889311X.2024.2461923)

**A Model-Centric Review of Deep Learning for Protein Design**
Gregory W. Kyro, Tianyin Qiu, Victor S. Batista
[arXiv:2502.19173](https://arxiv.org/abs/2502.19173)

**Computational protein design**
Katherine I. Albanese, Sophie Barbe, Shunsuke Tagami, Derek N. Woolfson & Thomas Schiex
[Nature Reviews Methods Primers 5.1 (2025)](https://www.nature.com/articles/s43586-025-00383-1)

**Exploring the Blueprint of Life: The Innovation in Antibody and Protein Design**
Yang, Zhiwei, and Gerald H. Lushington
[Combinatorial chemistry &amp; high throughput screening](https://www.eurekaselect.com/article/146786)

**Advanced Deep Learning Methods for Protein Structure Prediction and Design**
Yichao Zhang, Ningyuan Deng, Xinyuan Song, Ziqian Bi, Tianyang Wang, Zheyu Yao, Keyu Chen, Ming Li, Qian Niu, Junyu Liu, Benji Peng, Sen Zhang, Ming Liu, Li Zhang, Xuanhe Pan, Jinlang Wang, Pohsun Feng, Yizhu Wen, Lawrence KQ Yan, Hongming Tseng, Yan Zhong, Yunze Wang, Ziyuan Qin, Bowen Jing, Junjie Yang, Jun Zhou, Chia Xin Liang, Junhao Song
[arXiv:2503.13522](https://arxiv.org/abs/2503.13522)

**Deep Learning-Driven Protein Structure Prediction and Design: Key Model Developments by Nobel Laureates and Multi-Domain Applications**
Wanqing Yang, Yanwei Wang, Yang Wang
[arXiv:2504.01490](https://arxiv.org/abs/2504.01490)

**Intelligent mining, engineering, and de novo design of proteins**
LIU Cui, SHI Zhenkun, MA Hongwu, LIAO Xiaoping
[Sheng wu gong cheng xue bao= Chinese journal of biotechnology 41.3 (2025)](https://cjb.ijournals.cn/html/cjbcn/2025/3/07240629.htm)

**Protein-based Materials: Applications, Modification and Molecular Design**  
Alitenai Tunuhe, Ze Zheng, Xinran Rao, Hongbo Yu, Fuying Ma, Yaxian Zhou, Shangxian Xie  
[BioDesign Research (2025)](https://www.sciencedirect.com/science/article/pii/S2693125725000056)

**Artificial intelligence is transforming the study of proteins: Structures and beyond**  
Haiyan Liu, Quan Chen, and Yufeng Liu  
[hLife (2025)](https://www.sciencedirect.com/science/article/pii/S2949928325000021)

**Artificial intelligence methods for protein folding and design**  
Zhidian Zhang, Chenxi Ou, Yehlin Cho, Yo Akiyama, Sergey Ovchinnikov  
[Current Opinion in Structural Biology 93 (2025)](https://www.sciencedirect.com/science/article/abs/pii/S0959440X25000843)

**AI4Protein: transforming the future of protein design**  
Dequan Wang, Zheling Tan, Jin Gao, Shaoting Zhang, Jiaqi Shen & Yuming Lu  
[Science China Life Sciences (2025)](https://link.springer.com/article/10.1007/s11427-024-2906-3)

**Comment on the Use of AI-based Protein Design for Autoimmune Encephalitis: Exciting Possibilities and Practical Considerations**  
Zengwei Kou  
[Multiple Sclerosis and Related Disorders (2025)](https://www.msard-journal.com/article/S2211-0348(25)00335-9/fulltext)

**Computational Protein Design: Advancing Biotechnology through In Silico Engineering**  
Ranjit Ranbhor, Ruthvik Venkatesan, Amay Sanjay Redkar, Vibin Ramakrishnan  
[Progress in Biophysics and Molecular Biology (2025)](https://www.sciencedirect.com/science/article/pii/S0079610725000380)

**Advances of computational protein design: Principles, strategies and applications in nutrition and health**  
Ziling Zhao, Qiyang Qu, Fuwei Sun, Jiachen Zang, Bowen Zheng, Tuo Zhang, 
Guanghua Zhao, Chenyan Lv, Zhongjiang Wang  
[Biotechnology Advances (2025)](https://www.sciencedirect.com/science/article/pii/S0734975025001429)

**Artificial intelligence in de novo protein design**  
Yao, Jiawei, and Xiaogang Wang  
[Medicine in Novel Technology and Devices (2025)](https://www.sciencedirect.com/science/article/pii/S2590093525000177)

**AI-driven protein design**  
Huan Yee Koh, Yizhen Zheng, Madeleine Yang, Rohit Arora, Geoffrey I. Webb, Shirui Pan, Li Li & George M. Church  
[Nat Rev Bioeng (2025)](https://www.nature.com/articles/s44222-025-00349-8)

**DL4Proteins Jupyter Notebooks Teach how to use Artificial Intelligence for Biomolecular Structure Prediction and Design**  
Michael Chungyoun, Gabe Au, Britnie Carpentier, Sreevarsha Puvada, Courtney Thomas, Jeffrey J. Gray  
[arXiv:2511.02128](https://arxiv.org/abs/2511.02128v1)

**Guiding Generative Models for Protein Design: Prompting, Steering and Aligning**  
Filippo Stocco, Michele Garibbo, Noelia Ferruz  
[arXiv:2511.21476](https://arxiv.org/abs/2511.21476)

**RFDiffusion: Revolutionizing Protein Design with Generative AI**  
Zhangzhi(Fred) Peng  
[Serican Journal of Medicine 2.4 (2025)](https://journals.ku.edu/sjm/article/view/23410)

**Protein design drives synthetic biology research of plant natural products**  
Xiaopeng Zhang, Yinying Yao, Ye Wang, Yongshuo Ma, Yi Shang  
[BioDesign Research (2025)](https://www.sciencedirect.com/science/article/pii/S2693125725000494)

**The role of ai-driven de novo protein design in the exploration of the protein functional universe**  
Guohao Zhang,Chuanyang Liu, Jiajie Lu, Shaowei Zhang and Lingyun Zhu  
[Biology 14.9 (2025): 1268](https://www.mdpi.com/2079-7737/14/9/1268)

**Protein design and RNA design: Perspectives**  
Xi Chen, Xu Dai, Peilong Lu  
[Quantitative Biology 14.2 (2026)](https://onlinelibrary.wiley.com/doi/10.1002/qub2.70029)

**Transformation of Protein Design: From Traditional Approaches to AI-Driven Precision Engineering**  
Xin Fang  
[MedScien 1.1 (2025)](https://lseee.net/index.php/ms/article/view/1426)

**Harnessing advances in artificial intelligence for protein design**  
Russell Johnson  
[Nature Chemical Biology (2025): 1-4](https://www.nature.com/articles/s41589-025-02110-z)

**De novo protein design: a transformative frontier in clinical protein applications**  
Jie Gao, Zaiyong Zheng, Xueting Yu, Yamei Luo, Yang Yu & Chunxiang Zhang  
[J Transl Med (2026)](https://link.springer.com/article/10.1186/s12967-026-07784-0)

**Designing de novo TIM barrels: insights into stabilization, diversification, and functionalization strategies**  
Julian Beck, Sergio Romero-Romero  
[Biochem Soc Trans](https://portlandpress.com/biochemsoctrans/article/54/2/BST20253060/237195/Designing-de-novo-TIM-barrels-insights-into)

**AI-enabled protein design facilitates future plant research and crop breeding**  
Yuxuan Lou, Tianhao Wu, Fan Xia, Anwen Zhao, Xiangfeng Wang  
[Plant Physiology](https://academic.oup.com/plphys/advance-article/doi/10.1093/plphys/kiag147/8528248)

**Frontiers and challenges in the design of binders for intrinsically disordered proteins**  
Chentong Wang, Yanzhe Zhang, Minchao Fang, Zhangzhi Peng, Longxing Cao  
[Current Opinion in Structural Biology](https://www.sciencedirect.com/science/article/abs/pii/S0959440X26000382)

**Closing the loop: Experimentally validated methods in artificial intelligence–driven protein design**  
Clayton W. Kosonocky, Sarah Alamdari, Kevin K. Yang, Ava P. Amini  
[Current Opinion in Structural Biology 98 (2026)](https://www.sciencedirect.com/science/article/pii/S0959440X26000540)

**Protein design, generative AI and biological security**  
Maximilian Brackmann, Sophie Reiners, Masja Hoogendoorn, Michel Moser  
[Frontiers in Microbiology 17 (2026)](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2026.1817535/full)

**The past, present and future of de novo protein design**  
Wei Yang, Shunzhi Wang, Gyu Rie Lee, Jason Z. Zhang, Alexis Courbet, David Juergens, Xinru Wang, Thomas Schlichthaerle, Mohamad Abedi, Robert Ragotte, Linna An, Indrek Kalvet, Sam Pellock, Ljubica Mihaljevic, Cameron Glasscock, Arvind Pillai, Adam Broerman, Nathan Ennist, Ella Haefner, Nora McNamara-Bordewick, Ian Haydon, Lance Stewart, Gaurav Bhardwaj & David Baker  
[Nature 652, 1139–1152 (2026)](https://www.nature.com/articles/s41586-026-10328-7)

**Generative Protein Design: From Deep Learning Algorithms to Translational Applications**  
Shaotong Luo, Bo Zhou  
[International Journal of Molecular Sciences 27.9 (2026)](https://www.mdpi.com/1422-0066/27/9/2859)

**Machine-guided design for bioengineering gene therapy vectors: Where are we and what lies ahead?**  
Ana F. Rodrigues, Lucas Ferraz, Catia Pesquita  
[Biotechnology Advances (2026)](https://www.sciencedirect.com/science/article/pii/S073497502600131X)

**Protein Design Enters the Artificial Intelligence Era: Foundations, Tools, and Emerging Paradigms**  
Yanlin Mi, Arpit Shukla, Mark Tangney, Sabin Tabirca, and Venkata VB Yallapragada  
[Comput Struct Biotechnol J. 2026](https://spj.science.org/doi/10.34133/csbj.0105)

**Membrane Protein Design: From Reprogramming Functions to AI-Guided De Novo Design Approaches**  
Robert E. Jefferson, Patrick Barth  
[Chem. Rev. 2026](https://pubs.acs.org/doi/10.1021/acs.chemrev.5c01105)

**Artificial Intelligence and Protein Design: A retrospective study on 20-year emerging trends and core research areas from bibliometric perspectives**  
Wenjuan Zhao, Xiuwu Pan, Wei Yang, Zichang Liu, Xiyi Wei, Anqi Lin, Bufu Tang, Lin Zhang, Mingjia Xiao, Qing Zeng, Quan Cheng, Weiming Mou, Xiaofan Lu, Kai Miao, Peng Luo, Xin-gang Cui & Wen-jin Chen  
[Probiotics & Antimicro. Prot. (2026)](https://link.springer.com/article/10.1007/s12602-026-11131-6)

**De Novo Design of Protein Nanopores: From Minimal Peptides to AI-Driven Design**  
Anastassia A. Vorobieva, Rituparna Samanta, Toon Van Thillo  
[Chem. Rev. (2026)](https://pubs.acs.org/chreay/article-abstract/doi/10.1021/acs.chemrev.5c00990/5221890/De-Novo-Design-of-Protein-Nanopores-From-Minimal)

### 1.2 Antibody design

**A review of deep learning methods for antibodies**
Jordan Graves, Jacob Byerly, Eduardo Priego, Naren Makkapati , S. Vince Parish, Brenda Medellin and Monica Berrondo
[Antibodies 9.2 (2020)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7344881/pdf/antibodies-09-00012.pdf)

**Progress and challenges for the machine learning-based design of fit-for-purpose monoclonal antibodies**
Rahmad Akbar, Habib Bashour, Puneet Rawat, Philippe A. Robert, Eva Smorodina, Tudor-Stefan Cotet, Karine Flem-Karlsen, Robert Frank, Brij Bhushan Mehta, Mai Ha Vu, Talip Zengin, Jose Gutierrez-Marcos, Fridtjof Lund-Johansen,  Jan Terje Andersen, and Victor Greif
[Mabs. Vol. 14. No. 1. Taylor &amp; Francis, 2022](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8928824/)

**Advances in computational structure-based antibody design**
Hummer, Alissa M., Brennan Abanades, and Charlotte M. Deane
[Current Opinion in Structural Biology 74 (2022)](https://www.sciencedirect.com/science/article/pii/S0959440X22000586)

**Computational and artificial intelligence-based methods for antibody development**
Jisun Kim, Matthew McFee, Qiao Fang, Osama Abdin, Philip M. Kim
[Trends in Pharmacological Sciences (2023)](https://www.sciencedirect.com/science/article/pii/S0165614722002796)

**Leveraging deep learning to improve vaccine design**
Andrew P. Hederman, Margaret E. Ackerman
[Trends in immunology (2023)](https://www.cell.com/trends/immunology/fulltext/S1471-4906(23)00046-7)

**In Silico Approaches to Deliver Better Antibodies by Design: The Past, the Present and the Future**
Andreas Evers, Shipra Malhotra, Vanita D. Sood
[arXiv:2305.07488](https://arxiv.org/abs/2305.07488)

**AI Models for Protein Design are Driving Antibody Engineering**
Michael Chungyoun, Jeffrey J. Gray
[Current Opinion in Biomedical Engineering (2023): 100473](https://www.sciencedirect.com/science/article/abs/pii/S2468451123000296)

**Computational Methods in Immunology and Vaccinology: Design and Development of Antibodies and Immunogens**
Federica Guarra and Giorgio Colombo
[Journal of Chemical Theory and Computation (2023)](https://pubs.acs.org/doi/10.1021/acs.jctc.3c00513)

**Simplifying complex antibody engineering using machine learning**
Makowski, Emily K., Hsin-Ting Chen, and Peter M. Tessier
[Cell Systems 14.8 (2023)](https://www.cell.com/cell-systems/fulltext/S2405-4712(23)00118-7)/[2022 AIChE Annual Meeting. AIChE, 2022.](https://aiche.confex.com/aiche/2022/meetingapp.cgi/Paper/650993)

**AI driven B-cell Immunotherapy Design**
Bruna Moreira da Silva, David B. Ascher, Nicholas Geard, Douglas E. V. Pires
[arXiv:2309.01122](https://arxiv.org/abs/2309.01122)

**Best practices for machine learning in antibody discovery and development**
Leonard Wossnig, Norbert Furtmann, Andrew Buchanan, Sandeep Kumar, Victor Greiff
[arXiv:2312.08470](https://arxiv.org/abs/2312.08470)/[Drug Discovery Today (2024)](https://www.sciencedirect.com/science/article/pii/S1359644624001508)

**Next generation of multispecific antibody engineering**
Daniel Keri, Matt Walker, Isha Singh, Kyle Nishikawa, Fernando Garces
[Antibody Therapeutics (2023): tbad027](https://academic.oup.com/abt/article/7/1/37/7463325)

**A primer on ML in antibody engineering**
[ABHISHAIKE MAHAJAN](https://substack.com/@abhishaikemahajan)
[Substack](https://www.abhishaike.com/p/a-primer-on-ai-in-antibody-engineering) • blog

**Antibody design using deep learning: from sequence and structure design to affinity maturation**
Sara Joubbi, Alessio Micheli, Paolo Milazzo, Giuseppe Maccari, Giorgio Ciano, Dario Cardamone, Duccio Medini
[Briefings in Bioinformatics, Volume 25, Issue 4, July 2024, bbae307](https://academic.oup.com/bib/article/25/4/bbae307/7705535)

**AI-accelerated therapeutic antibody development: practical insights**
Luca Santuari, Marianne Bachmann Salvy, Ioannis Xenarios, Bulak Arpat
[Frontiers in Drug Discovery 4 (2024)](https://www.frontiersin.org/journals/drug-discovery/articles/10.3389/fddsv.2024.1447867/full)

**AI-driven antibody design with generative diffusion models: current insights and future directions**
Xin-heng He, Jun-rui Li, James Xu, Hong Shan, Shi-yi Shen, Si-han Gao & H. Eric Xu
[Acta Pharmacologica Sinica (2024)](https://www.nature.com/articles/s41401-024-01380-y)

**Applying computational protein design to therapeutic antibody discovery -- current state and perspectives**
Weronika Bielska, Igor Jaszczyszyn, Pawel Dudzic, Bartosz Janusz, Dawid Chomicz, Sonia Wrobel, Victor Greiff, Ryan Feehan, Jared Adolf-Bryfogle, Konrad Krawczyk
[arXiv:2503.00913](https://arxiv.org/abs/2503.00913)/[Frontiers in Immunology 16 (2025)](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2025.1571371/full)

**Artificial intelligence-driven computational methods for antibody design and optimization**  
Luiz Felipe Vecchietti, Bryan Nathanael Wijaya, Azamat Armanuly,Begench Hangeldiyev, Hyunkyu Jung, Sooyeon Lee, Meeyoung Cha & Ho Min Kim  
[mAbs, 2025](https://www.tandfonline.com/doi/full/10.1080/19420862.2025.2528902)

**In Silico Peptide Design: Methods, Resources, and Role of AI**  
Priyanka Ray Choudhury, Sai Kumar Mishra, Siddharth Yadav, Shubhi Singh, Puniti Mathur  
[Journal of Peptide Science 31.12 (2025)](https://onlinelibrary.wiley.com/doi/10.1002/psc.70063)

**Artificial intelligence in antibody design and development: harnessing the power of computational approaches**  
Soudabeh Kavousipour, Mahdi Barazesh, Shiva Mohammadi  
[Medical & Biological Engineering & Computing (2025)](https://link.springer.com/article/10.1007/s11517-025-03429-4)

**Harnessing deep learning to accelerate the development of antibodies and aptamers**
Pan Tan, Song Li, Jin Huang, Ziyi Zhou, Liang Hong  
[Acta Pharmaceutica Sinica B (2025)](https://www.sciencedirect.com/science/article/pii/S2211383525008251)

**Artificial intelligence advancements in monoclonal antibody development technology**  
Ammar M, Samsonov M, Gurylina E and Bayzigitov D  
[Front. Immunol](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2026.1802038/full)

### 1.3 Peptide design

**Deep generative models for peptide design**
Wan, Fangping, Daphne Kontogiorgos-Heintz, and Cesar de la Fuente-Nunez
[Digital Discovery (2022)](https://pubs.rsc.org/en/content/articlehtml/2022/dd/d1dd00024a)

**Design of protein segments and peptides for binding to protein targets**
Gupta, Suchetana, Noora Azadvari, and Parisa Hosseinzadeh
[BioDesign Research 2022 (2022)](https://spj.science.org/doi/10.34133/2022/9783197)

**Revolutionizing peptide-based drug discovery: Advances in the post-AlphaFold era**
Liwei Chang, Arup Mondal, Bhumika Singh, Yisel Martínez-Noa, Alberto Perez
[Wiley Interdisciplinary Reviews: Computational Molecular Science](https://wires.onlinelibrary.wiley.com/doi/epdf/10.1002/wcms.1693)

**Peptide-based drug discovery through artificial intelligence: towards an autonomous design of therapeutic peptides**
Montserrat Goles, Anamaría Daza, Gabriel Cabas-Mora, Lindybeth Sarmiento-Varón, Julieta Sepúlveda-Yañez, Hoda Anvari-Kazemabad, Mehdi D Davari, Roberto Uribe-Paredes, Álvaro Olivera-Nappa, Marcelo A Navarrete, David Medina-Ortiz
[Briefings in Bioinformatics 25.4 (2024)](https://academic.oup.com/bib/article/25/4/bbae275/7690345)

**Accelerating antimicrobial peptide design: Leveraging deep learning for rapid discovery**
Ahmad M. Al-Omari ,Yazan H. Akkam,Ala’a Zyout,Shayma’a Younis,Shefa M. Tawalbeh,Khaled Al-Sawalmeh,Amjed Al Fahoum ,Jonathan Arnold
[PloS one 19.12 (2024): e0315477](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0315477)

**Trends in the Research and Development of Peptide Drug Conjugates: Artificial Intelligence Aided Design**
Dong-E Zhang, Dong-E Zhang, Tong He, Tong He, Tianyi Shi, Tianyi Shi, Kun Huang, Kun Huang, Anlin Peng, Anlin Peng
[Frontiers in Pharmacology 16](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2025.1553853/full)

**Generative models for antimicrobial peptide design: auto-encoders and beyond**  
Lukas Beierle, Julian Hahnfeld, Alexander Goesmann, Reihaneh Mostolizadeh, Franz Cemič  
[bioRxiv 2025.10.29.685317](https://www.biorxiv.org/content/10.1101/2025.10.29.685317v1)/[BioData Mining (2026)](https://link.springer.com/article/10.1186/s13040-026-00558-w) • [Supplementary](https://www.biorxiv.org/content/biorxiv/early/2025/10/30/2025.10.29.685317/DC1/embed/media-1.pdf) • [code](https://github.com/devshibe/amp-autencoders)

**Contemporary data-driven innovations in peptide-based therapeutic design**  
Lipsa Priyadarsinee, Vyacheslav Kungurtsev, Vibhor Kumar, Bapi Chatterjee, Garikapati Narahari Sastry, Natarajan Arul Murugan  
[Briefings in Bioinformatics](https://academic.oup.com/bib/article/27/3/bbag220/8687186)

### 1.4 Binder design

**Improving de novo Protein Binder Design with Deep Learning**
Nathaniel Bennett, Brian Coventry, Inna Goreshnik, Buwei Huang, Aza Allen, Dionne Vafeados, Ying Po Peng, Justas Dauparas, Minkyung Baek, Lance Stewart, Frank DiMaio, Steven De Munck, Savvas Savvides, David Baker
[bioRxiv 2022.06.15.495993](https://www.biorxiv.org/content/10.1101/2022.06.15.495993v1)/[Nat Commun 14, 2625 (2023)](https://www.nature.com/articles/s41467-023-38328-5) • [code](https://github.com/nrbennet/dl_binder_design) • [news](https://phys.org/news/2023-08-deep-protein.html)

**Data and AI-driven synthetic binding protein discovery**
Yanlin Li, Zixin Duan, Zhenwen Li, Weiwei Xue
[Trends in Pharmacological Sciences (2025)](https://www.cell.com/trends/pharmacological-sciences/abstract/S0165-6147(24)00268-2)

**Code to complex: AI-driven de novo binder design**  
Daniel R. Fox, Cyntia Taveneau, Janik Clement, Rhys Grinter, Gavin J. Knott  
[Structure (2025)](https://www.cell.com/structure/fulltext/S0969-2126(25)00311-9)

**The latest AI breakthroughs in structural biology: protein binder design and conformational state prediction**  
Luciano A. Abriata  
[Commun Biol 9, 627 (2026)](https://www.nature.com/articles/s42003-026-10112-3)

### 1.5 Enzyme design

**A review of enzyme design in catalytic stability by artificial intelligence**
Yongfan Ming, Wenkang Wang, Rui Yin, Min Zeng, Li Tang, Shizhe Tang, Min Li
[Briefings in Bioinformatics, 2023](https://academic.oup.com/bib/advance-article-abstract/doi/10.1093/bib/bbad065/7086816)

**Application of "foldability" in the intelligent of enzymes engineering and design: take AlphaFold2 for example**
MENG Qiaozhen, GUO Fei
[Synthetic Biology Journal (2023)](https://synbioj.cip.com.cn/article/2023/2096-8280/2023-011.shtml)

**AlphaFold2 and Deep Learning for Elucidating Enzyme Conformational Flexibility and Its Application for Design**
Casadevall, Guillem, Cristina Duran, and Sí­lvia Osuna
[JACS Au (2023)](https://pubs.acs.org/doi/10.1021/jacsau.3c00188)

**Accelerating Biocatalysis Discovery with Machine Learning: A Paradigm Shift in Enzyme Engineering, Discovery, and Design**
Braun Markus, Gruber Christian C, Krassnigg Andreas, Kummer Arkadij, Lutz Stefan, Oberdorfer Gustav, Siirola Elina, and Snajdrova Radka
[ACS Catal. 2023](https://pubs.acs.org/doi/10.1021/acscatal.3c03417)

**Building Enzymes through Design and Evolution**
Hossack, Euan J., Florence J. Hardy, and Anthony P. Green
[ACS Catalysis 13.19 (2023)](https://pubs.acs.org/doi/10.1021/acscatal.3c02746)

**Advances in generative modeling methods and datasets to design novel enzymes for renewable chemicals and fuels**
Rana A Barghout, Zhiqing Xu, Siddharth Betala, Radhakrishnan Mahadevan
[Current Opinion in Biotechnology, Volume 84, 2023](https://www.sciencedirect.com/science/article/abs/pii/S0958166923001179)

**Opportunites and Challenges for Machine Learning-Assisted Enzyme Engineering**
Jason Yang, Francesca-Zhoufan Li, Frances H. Arnold
[ACS Central Science (2024)](https://pubs.acs.org/doi/10.1021/acscentsci.3c01275)

**Navigating the landscape of enzyme design: from molecular simulations to machine learning**
Jiahui Zhoua, Meilan Huang
[Chemical Society Reviews (2024)](https://pubs.rsc.org/en/Content/ArticleLanding/2024/CS/D4CS00196F)

**Structure Prediction and Computational Protein Design for Efficient Biocatalysts and Bioactive Proteins**
Rebecca Buller, Jiri Damborsky, Donald Hilvert, Uwe Bornscheuer
[Angewandte Chemie (International ed. in English)](https://onlinelibrary.wiley.com/doi/10.1002/anie.202421686)

**Generative AI for Enzyme Design and Biocatalysis**  
Lasse Middendorf, Noelia Ferruz  
[arXiv:2602.03779](https://arxiv.org/abs/2602.03779)

**Generative artificial intelligence for enzyme design and biocatalysis**  
Lasse Middendorf, Noelia Ferruz  
[Current Opinion in Chemical Biology](https://www.sciencedirect.com/science/article/pii/S1367593126000773)

## 2. Model-based design

> Invert trained models with optimize algorithms through iterations for sequence design. Inverted structure prediction models are known as **Hallucination**.

### 2.1 Structure Prediction Model-based

### 2.1.1 trRosetta-based

**Design of proteins presenting discontinuous functional sites using deep learning**
Doug Tischer, Sidney Lisanza, Jue Wang, Runze Dong,  View ORCID ProfileIvan Anishchenko, Lukas F. Milles, Sergey Ovchinnikov, David Baker
[bioRxiv (2020)](https://www.biorxiv.org/content/10.1101/2020.11.29.402743v1)

**Fast differentiable DNA and protein sequence optimization for molecular design**
Linder, Johannes, and Georg Seelig
[arXiv preprint arXiv:2005.11275 (2020)](https://arxiv.org/abs/2005.11275)

**De novo protein design by deep network hallucination**
Ivan Anishchenko, Samuel J. Pellock, Tamuka M. Chidyausiku, Theresa A. Ramelot, Sergey Ovchinnikov, Jingzhou Hao, Khushboo Bafna, Christoffer Norn, Alex Kang, Asim K. Bera, Frank DiMaio, Lauren Carter, Cameron M. Chow, Gaetano T. Montelione & David Baker
[Nature (2021)](https://doi.org/10.1038/s41586-021-04184-w)  • [code](https://github.com/gjoni/trDesign) • [trRosetta](https://yanglab.nankai.edu.cn/trRosetta/download/)

**Protein sequence design by conformational landscape optimization**
Christoffer Norn, Basile I. M. Wicky, David Juergens, and Sergey Ovchinnikov
[Proceedings of the National Academy of Sciences 118.11 (2021)](https://www.pnas.org/content/118/11/e2017228118) • [code](https://github.com/gjoni/trDesign)

**De novo design of small beta barrel proteins**
David E. Kim, Davin R. Jensen, David Feldman, Doug Tischer  and Ayesha Saleem, Cameron M. Chow, Xinting Li, Lauren Carter, Lukas Milles, Hannah Nguyen, Alex Kang, Asim K. Bera, Francis C. Peterson, Brian F. Volkman, Sergey Ovchinnikov, David Baker
[PNAS(2023),e2207974120](https://www.pnas.org/doi/10.1073/pnas.2207974120) • [code](https://github.com/sokrypton/TrDesign_partialhal)

**Exploring "dark matter" protein folds using deep learning**
Zander Harteveld, Alexandra Van Hall-Beauvais, Irina Morozova, Joshua Southern, Casper Alexander Goverde, Sandrine Georgeon, Stephane Rosset, Andreas Loukas, Pierre Vandergheynst, Michael Bronstein, Bruno Correia
[bioRxiv 2023.08.30.555621](https://www.biorxiv.org/content/10.1101/2023.08.30.555621v1)/[Cell Systems](https://www.cell.com/cell-systems/fulltext/S2405-4712(24)00270-9) • [Suppplymentary](https://www.biorxiv.org/content/biorxiv/early/2023/09/01/2023.08.30.555621/DC1/embed/media-1.pdf) • [code](https://github.com/zanderharteveld/genesis)

**Carving out a Glycoside Hydrolase Active Site for Incorporation into a New Protein Scaffold Using Deep Network Hallucination**
Anders Lønstrup Hansen, Frederik Friis Theisen, Ramon Crehuet, Enrique Marcos, Nushin Aghajari, and Martin Willemoës
[ACS Synth. Biol. 2024](https://pubs.acs.org/doi/10.1021/acssynbio.3c00674)

**Implicit modeling of the conformational landscape and sequence allows scoring and generation of stable proteins**
Yehlin Cho, Justas Dauparas, Kotaro Tsuboyama, Gabriel Rocklin, Sergey Ovchinnikov
[bioRxiv 2024.12.20.629706](https://www.biorxiv.org/content/10.1101/2024.12.20.629706v1)/[Nat Commun (2025)](https://www.nature.com/articles/s41467-025-66526-w) • [code](https://github.com/yehlincho/Joint_Model_Stability) • [Supplementary](https://www.biorxiv.org/content/biorxiv/early/2024/12/22/2024.12.20.629706/DC1/embed/media-1.pdf)

#### 2.1.2 AlphaFold-based

**End-to-end learning of multiple sequence alignments with differentiable Smith-Waterman**
Petti, Samantha, Bhattacharya, Nicholas, Rao, Roshan, Dauparas, Justas, Thomas, Neil, Zhou, Juannan, Rush, Alexander M, Koo, Peter K, Ovchinnikov, Sergey
[bioRxiv (2021)](http://repository.cshl.edu/id/eprint/40409/)/[Bioinformatics, 2022;, btac724](https://academic.oup.com/bioinformatics/advance-article/doi/10.1093/bioinformatics/btac724/6820925) • [ColabDesign](https://github.com/sokrypton/ColabDesign), [SMURF](https://github.com/spetti/SMURF), [AF2 back propagation](https://github.com/sokrypton/af_backprop) • [our notes1](https://zhuanlan.zhihu.com/p/468219547), [notes2](https://zhuanlan.zhihu.com/p/472037977) • [lecture1](https://www.youtube.com/watch?v=2HmXwlKWMVs), [lecture2](https://www.youtube.com/watch?v=BJdRvODiDnk) • [Discord](https://discord.com/invite/FpYPneYB)

**AlphaDesign: A de novo protein design framework based on AlphaFold**
Jendrusch, Michael, Jan O. Korbel, and S. Kashif Sadiq
[bioRxiv (2021)](https://www.biorxiv.org/content/10.1101/2021.10.11.463937v1)/[Molecular Systems Biology (2025)](https://www.embopress.org/doi/full/10.1038/s44320-025-00119-z)

**Using AlphaFold for Rapid and Accurate Fixed Backbone Protein Design**
Moffat, Lewis, Joe G. Greener, and David T. Jones
[bioRxiv (2021)](https://www.biorxiv.org/content/10.1101/2021.08.24.457549v1)

**State-of-the-art estimation of protein model accuracy using AlphaFold**
James P. Roney, Sergey Ovchinnikov
[bioRxiv 2022.03.11.484043](https://www.biorxiv.org/content/10.1101/2022.03.11.484043v3)/[Physical Review Letters 129.23 (2022)](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.129.238101) • [code](https://github.com/jproney/AF2Rank)

**Solubility-aware protein binding peptide design using AlphaFold**
Takatsugu Kosugi, Masahito Ohue
[bioRxiv 2022.05.14.491955](https://doi.org/10.1101/2022.05.14.491955)/[Biomedicines 10.7 (2022)](https://www.mdpi.com/2227-9059/10/7/1626) • [Supplemental Materials](https://www.biorxiv.org/content/biorxiv/early/2022/05/15/2022.05.14.491955/DC1/embed/media-1.pdf) • [code](https://github.com/ohuelab/Solubility_AfDesign)

**Hallucinating protein assemblies**
Basile I M Wicky, Lukas F Milles, Alexis Courbet, Robert J Ragotte, Justas Dauparas, Elias Kinfu, Sam Tipps, Ryan D Kibler, Minkyung Baek, Frank DiMaio, Xinting Li, Lauren Carter, Alex Kang, Hannah Nguyen, Asim K Bera, David Baker
[bioRxiv 2022.06.09.493773](https://www.biorxiv.org/content/10.1101/2022.06.09.493773v1)/[Science (2022)](https://www.science.org/doi/10.1126/science.add1964) • [related slides](https://docs.google.com/presentation/d/1_tvzLKks83sYOKemfFeImCPnWtCQ-CHqmKK_3IQI1so/) • [our notes](https://zhuanlan.zhihu.com/p/527152827) • [news](https://www.nature.com/articles/d41586-022-02947-7)

**EvoBind: in silico directed evolution of peptide binders with AlphaFold**
Patrick Bryant, Arne Elofsson
[bioRxiv 2022.07.23.501214](https://www.biorxiv.org/content/10.1101/2022.07.23.501214v1) • [code](https://github.com/patrickbryant1/EvoBind)

**Hallucination of closed repeat proteins containing central pockets**
Linna An, Derrick R Hicks, Dmitri Zorine, Justas Dauparas, Basile I. M. Wicky, Lukas F Milles, Alexis Courbet, Asim K. Bera, Hannah Nguyen, Alex Kang, Lauren Carter, David Baker
[bioRxiv 2022.09.01.506251](https://www.biorxiv.org/content/10.1101/2022.09.01.506251v1)/[Nat Struct Mol Biol 30, 1755-1760 (2023)](https://www.nature.com/articles/s41594-023-01112-6) • [Supplementary data](https://static-content.springer.com/esm/art%3A10.1038%2Fs41594-023-01112-6/MediaObjects/41594_2023_1112_MOESM1_ESM.pdf)

**Predicting the structure of large protein complexes using AlphaFold and Monte Carlo tree search**
Patrick Bryant, Gabriele Pozzati, Wensi Zhu, Aditi Shenoy, Petras Kundrotas & Arne Elofsson
[Nature communications 13.1 (2022)](https://www.nature.com/articles/s41467-022-33729-4) • [gitlba](https://gitlab.com/patrickbryant1/molpc), [github](https://github.com/patrickbryant1/MoLPC) • [Supplementary data1](https://doi.org/10.5281/zenodo.6367019), [Supplementary data2](https://doi.org/10.17044/scilifelab.19375172)

**De novo protein design by inversion of the AlphaFold structure prediction network**
Casper Goverde, Benedict Wolf, Hamed Khakzad, Stephane Rosset, Bruno E Correia
[bioRxiv 2022.12.13.520346](https://www.biorxiv.org/content/10.1101/2022.12.13.520346v1) • [code](https://github.com/bene837/af_gradmcmc) • [lecture1](https://www.youtube.com/watch?v=aUMGuogMZCA) • [lecture2](https://www.youtube.com/watch?v=4S4J7gbhAa0)

**Code of OpenComplex**
Jingcheng, Yu and Zhaoming, Chen and Zhaoqun, Li and Mingliang, Zeng and Wenjun, Lin and He, Huang and Qiwei, Ye
[code](https://github.com/baaihealth/OpenComplex)

**Efficient and scalable de novo protein design using a relaxed sequence space**
Christopher Josef Frank, Ali Khoshouei, Yosta de Stigter, Dominik Schiewitz, Shihao Feng, Sergey Ovchinnikov, Hendrik Dietz
[bioRxiv 2023.02.24.529906](https://www.biorxiv.org/content/10.1101/2023.02.24.529906v1) • [code](https://github.com/sokrypton/ColabDesign/blob/main/af/examples/af_relax_design.ipynb)

**Cyclic peptide structure prediction and design using AlphaFold**
Stephen A. Rettie, Katelyn V. Campbell, Asim K. Bera, Alex Kang, Simon Kozlov, Joshmyn De La Cruz, Victor Adebomi, Guangfeng Zhou, Frank DiMaio, Sergey Ovchinnikov, Gaurav Bhardwaj
[bioRxiv](https://www.biorxiv.org/content/10.1101/2023.02.25.529956v1)/[Nat Commun 16, 4730 (2025)](https://www.nature.com/articles/s41467-025-59940-7) • [Code](https://github.com/sokrypton/ColabDesign/blob/main/af/examples/af_cyc_design.ipynb) • [Supplementary](https://www.biorxiv.org/content/biorxiv/early/2023/02/26/2023.02.25.529956/DC1/embed/media-1.xlsx)

**De novo design of luciferases using deep learning**
Andy Hsien-Wei Yeh, Christoffer Norn, Yakov Kipnis, Doug Tischer, Samuel J. Pellock, Declan Evans, Pengchen Ma, Gyu Rie Lee, Jason Z. Zhang, Ivan Anishchenko, Brian Coventry, Longxing Cao, Justas Dauparas, Samer Halabiya, Michelle DeWitt, Lauren Carter, K. N. Houk & David Baker
[Nature](https://www.nature.com/articles/s41586-023-05696-3) • [Code](https://files.ipd.uw.edu/pub/luxSit/scaffold_generation.tar.gz) • [Supplementary Materials](https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-023-05696-3/MediaObjects/41586_2023_5696_MOESM1_ESM.pdf)

**In silico evolution of protein binders with deep learning models for structure prediction and sequence design**
Odessa J Goudy, Amrita Nallathambi, Tomoaki Kinjo, Nicholas Randolph, Brian Kuhlman
[bioRxiv 2023.05.03.539278](https://www.biorxiv.org/content/10.1101/2023.05.03.539278v1) • [Supplementary](https://www.biorxiv.org/content/biorxiv/early/2023/05/03/2023.05.03.539278/DC1/embed/media-1.pdf) • [code](https://github.com/KuhlmanLab/evopro)

**Computational design of soluble analogues of integral membrane protein structures**
Casper Alexander Goverde, Martin Pacesa, Lars Jeremy Dornfeld, Sandrine Georgeon, Stephane Rosset, Justas Dauparas, Christian Shellhaas, Simon Kozlov, David Baker, Sergey Ovchinnikov, Bruno Correia
[bioRxiv 2023.05.09.540044](https://www.biorxiv.org/content/10.1101/2023.05.09.540044v2)/[Nature (2024)](https://www.nature.com/articles/s41586-024-07601-y) • [code](https://github.com/bene837/af2seq) • [Supplementary](https://www.biorxiv.org/content/biorxiv/early/2023/05/09/2023.05.09.540044/DC1/embed/media-1.pdf)

**Antibody Complementarity-Determining Region Sequence Design using AlphaFold2 and Binding Affinity Prediction Model**
Takafumi Ueki, Masahito Ohue
[bioRxiv 2023.06.02.543382](https://www.biorxiv.org/content/10.1101/2023.06.02.543382v1)

**Context-Dependent Design of Induced-fit Enzymes using Deep Learning Generates Well Expressed, Thermally Stable and Active Enzymes**
Lior Zimmerman, Noga Alon, Itay Levin, Anna Koganitsky, Nufar Shpigel, Chen Brestel, Gideon David Lapidoth
[bioRxiv 2023.07.27.550799](https://www.biorxiv.org/content/10.1101/2023.07.27.550799v2) • [Supplementary](https://www.biorxiv.org/content/biorxiv/early/2023/07/31/2023.07.27.550799/DC1/embed/media-1.xlsx)

**Highly accurate and robust protein sequence design with CarbonDesign**/**Accurate and robust protein sequence design with CarbonDesign**
Milong Ren, Chungong Yu, Dongbo Bu, Haicang Zhang
[bioRxiv 2023.08.07.552204](https://www.biorxiv.org/content/10.1101/2023.08.07.552204v1)/[Nat Mach Intell 6, 536–547 (2024)](https://www.nature.com/articles/s42256-024-00838-2) • [code](https://github.com/zhanghaicang/carbonmatrix_public)

**Design of Cyclic Peptides Targeting Protein-Protein Interactions using AlphaFold**
Takatsugu Kosugi, Masahito Ohue
[bioRxiv 2023.08.20.554056](https://www.biorxiv.org/content/10.1101/2023.08.20.554056v1) • [Supplementary](https://www.biorxiv.org/content/biorxiv/early/2023/08/21/2023.08.20.554056/DC1/embed/media-1.pdf) • [code](https://github.com/YoshitakaMo/localcolabfold/)

**MetaPPI: In Silico Screen for Novel CRBN-based Substrates**
neoxbio
[website](https://www.neoxbio.com/platform-technology.html) • [news](https://mp.weixin.qq.com/s/Kb4EQ0YvYDvoLZ_cnAlUPw) • masif-based • commercial

**AlphaFold Distillation for Protein Design**
Anonymous
[ICLR 2024](https://openreview.net/forum?id=3pgJNIx3gc) • [code](https://anonymous.4open.science/r/AFDistill-28C3)

**High-throughput computational discovery of inhibitory protein fragments with AlphaFold**
Andrew Savinov, Sebastian Swanson, Amy E. Keating, Gene-Wei Li
[bioRxiv 2023.12.19.572389](https://www.biorxiv.org/content/10.1101/2023.12.19.572389v1) • [code](https://github.com/swanss/FragFold)

**An integrative approach to protein sequence design through multiobjective optimization**
Lu Hong, Tanja Kortemme
[bioRxiv 2024.03.01.582670](https://www.biorxiv.org/content/10.1101/2024.03.01.582670v1)/[PLOS Computational Biology 20(7)](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011953) • [code](https://github.com/luhong88/int_seq_des) • [Supplementary](https://www.biorxiv.org/content/biorxiv/early/2024/03/04/2024.03.01.582670/DC1/embed/media-1.pdf)

**Protein Design Using Structure-Prediction Networks: AlphaFold and RoseTTAFold as Protein Structure Foundation Models**
Jue Wang, Joseph L. Watson and Sidney L. Lisanza
[Cold Spring Harbor Perspectives in Biology(2024)](https://cshperspectives.cshlp.org/content/early/2024/03/01/cshperspect.a041472.short)

**Context-dependent design of induced-fit enzymes using deep learning generates well-expressed, thermally stable and active enzymes**
Lior Zimmerman, Noga Alon, Itay Levin, and Gideon D. Lapidoth
[Proceedings of the National Academy of Sciences 121.11(2024)](https://www.pnas.org/doi/10.1073/pnas.2313809121)

**Design of Repeat Alpha-Beta Proteins with Capping Helices**
Dmitri Zorine, David Baker
[bioRxiv 2024.06.15.590358](https://www.biorxiv.org/content/10.1101/2024.06.15.590358v1) • [code](https://github.com/dmitropher/af2_multistate_hallucination)

**Design of linear and cyclic peptide binders of different lengths only from a protein target sequence**
Qiuzhen Li, Efstathios Nikolaos Vlachos, Patrick Bryant
[bioRxiv 2024.06.20.599739](https://www.biorxiv.org/content/10.1101/2024.06.20.599739v1) • [code](https://zenodo.org/records/11543503) • [Supplementary](https://www.biorxiv.org/content/biorxiv/early/2024/06/22/2024.06.20.599739/DC1/embed/media-1.pdf)

**BindCraft: one-shot design of functional protein binders**
Martin Pacesa, Lennart Nickel, Joseph Schmidt, Ekaterina Pyatova, Christian Schellhaas, Lucas Kissling, Ana Alcaraz-Serna, Yehlin Cho, Kourosh H. Ghamary, Laura Vinue, Brahm J. Yachnin, Andrew M. Wollacott, Stephen Buckley, Sandrine Georgeon, Casper A. Goverde, Georgios N. Hatzopoulos, Pierre Gonczy, Yannick D. Muller, Gerald Schwank, Sergey Ovchinnikov, Bruno E. Correia
[bioRxiv 2024.09.30.615802](https://www.biorxiv.org/content/10.1101/2024.09.30.615802v1)/[Nature (2025)](https://www.nature.com/articles/s41586-025-09429-6) • [code](https://github.com/martinpacesa/BindCraft)

**Design of linear and cyclic peptide binders of different lengths from protein sequence information**
Qiuzhen Li, Efstathios Nikolaos Vlachos, Patrick Bryant
[bioRxiv 2024.06.20.599739](https://www.biorxiv.org/content/10.1101/2024.06.20.599739v2) • [code](https://zenodo.org/records/13913345)

**Scalable protein design using optimization in a relaxed sequence space**
Christopher Frank, Ali Khoshouei , Lara Fub , Dominik Schiwietz , Dominik Putz, Lara Weber, Zhixuan Zhao, Motoyuki Hattori, Shihao Feng, Yosta de Stigter, Sergey Ovchinnikov, Hendrik Dietz
[Science386,439-445(2024)](https://www.science.org/doi/10.1126/science.adq1741) • [code](https://github.com/sokrypton/ColabDesign)

**Alphafold2 refinement improves designability of large de novo proteins**
Christopher Josef Frank, Dominik Schiwietz, Lara Fuss, Sergey Ovchinnikov, Hendrik Dietz
[bioRxiv 2024.11.21.624687](https://www.biorxiv.org/content/10.1101/2024.11.21.624687v1) • [colab](https://colab.research.google.com/drive/14ULdrjOmH-XMtGDrikzjDF1FLegZg3-a?usp=sharing)

**Low-N OpenFold fine-tuning improves peptide design without additional structures**
Theodore Sternlieb, Jakub Otwinowski, Sam Sinai, Jeffrey Chan
[Machine Learning for Structural Biology Workshop, NeurIPS 2024](https://www.mlsb.io/papers_2024/Low-N_OpenFold_fine-tuning_improves_peptide_design_without_additional_structures.pdf)

**HighPlay: Cyclic Peptide Sequence Design Based on Reinforcement Learning and Protein Structure Prediction**
Huitian Lin, Cheng Zhu, Tianfeng Shang, Ning Zhu, Kang Lin, Xiang Shao, Xudong Wang, Hongliang Duan
[bioRxiv 2025.03.17.643626](http://biorxiv.org/content/10.1101/2025.03.17.643626v1)

**Designing Novel Solenoid Proteins with In Silico Evolution**
Daniella Pretorius, Georgi Ivanov Nikov, Kono Washio, Steve-William Florent, Henry Taunt, Sergey Ovchinnikov, James William Murray
[bioRxiv 2025.04.23.646631](https://www.biorxiv.org/content/10.1101/2025.04.23.646631v1) • [Supplementary](https://www.biorxiv.org/content/biorxiv/early/2025/04/24/2025.04.23.646631/DC1/embed/media-1.pdf)

**Single-Shot Design of a Cyclic Peptide Inhibitor of HIV-1 Membrane Fusion with EvoBind**  
Diandra Daumiller, Federica Giammarino, Qiuzhen Li, Anders Sönnerborg, Rafael Ceña Diez, Patrick Bryant  
[bioRxiv 2025.04.30.651413](https://www.biorxiv.org/content/10.1101/2025.04.30.651413v1)

**BindEnergyCraft: Casting Protein Structure Predictors as Energy-Based Models for Binder Design**  
Divya Nori, Anisha Parsan, Caroline Uhler, Wengong Jin  
[arXiv:2505.21241](https://arxiv.org/abs/2505.21241)

**Blind De Novo Design of Dual Cyclic Peptide Agonists Targeting GCGR and GLP1R**  
Qiuzhen Li, Elisee Wiita, Thomas Helleday, Patrick Bryant  
[bioRxiv 2025.06.06.658268](https://www.biorxiv.org/content/10.1101/2025.06.06.658268v1) • [code](https://zenodo.org/records/13933365)

**AlphaFold distillation for inverse protein design**  
Igor Melnyk, Aurélie Lozano, Payel Das & Vijil Chenthamarakshan  
[Sci Rep 15, 21743 (2025)](https://www.nature.com/articles/s41598-025-00436-1) • [code](https://github.com/IBM/AFDistill)

**Fold-Conditioned De Novo Binder Design via AlphaFold2-Multimer Hallucination**  
Khondamir. R. Rustamov, Artyom Y. Baev  
[bioRxiv 2025.07.02.662497](https://www.biorxiv.org/content/10.1101/2025.07.02.662497v1) • [Supplementary](https://www.biorxiv.org/content/biorxiv/early/2025/07/05/2025.07.02.662497/DC1/embed/media-1.docx) • [code](https://github.com/KhondamirRustamov/FoldCraft)

**Design of linear and cyclic peptide binders from protein sequence  information**  
Qiuzhen Li, Efstathios Nikolaos Vlachos & Patrick Bryant  
[Commun Chem 8, 211 (2025)](https://www.nature.com/articles/s42004-025-01601-3)

**Generative Design of High-Affinity Peptides Using BindCraft**  
Mike Filius, Thanasis Patsos, Hugo Minee, Gianluca Turco, Jingming Liu, Monika Gnatzy, Ramon S.M. Rooth, Andy C. H. Liu, Rosa D.T. Ta, Isa H. A. Rijk, Safiya Ziani, Femke J. Boxman, Sebastian J. Pomplun  
[bioRxiv 2025.07.23.666285](https://www.biorxiv.org/content/10.1101/2025.07.23.666285v1) • [Supplementary](https://www.biorxiv.org/content/biorxiv/early/2025/07/25/2025.07.23.666285/DC1/embed/media-1.pdf)

**Computational Design of Soluble CCR8 Analogues with Preserved Antibody Binding**  
Trang Nguyen, Songming Liu, Yifan Li, Longfei Cong, Roger Shek, Tek Hyang Lee, Li Yi, Per Greisen  
[bioRxiv 2025.08.18.670068](https://www.biorxiv.org/content/10.1101/2025.08.18.670068v1)

**De novo design of a peptide modulator to reverse sodium channel dysfunction linked to cardiac arrhythmias and epilepsy**  
Ryan Mahling, Bence Hegyi, Erin R. Cullen, Timothy M. Cho, Aaron R. Rodriques, Lucile Fossier, Marc Yehya, Lin Yang, Bi-Xing Chen, Alexander N. Katchman, Nourdine Chakouri, Ruiping Ji, Elaine Y. Wan, Jared Kushner, Steven O. Marx, Sergey Ovchinnikov, Christopher D. Makinson, Donald M. Bers, Manu Ben-Johny  
[Cell (2025)](https://www.cell.com/cell/fulltext/S0092-8674(25)00860-8)

**Efficient generation of epitope-targeted de novo antibodies with Germinal**  
Luis Santiago Mille-Fragoso, John N Wang, Claudia L Driscoll, Haoyu Dai, Talal M Widatalla, Xiaowei Zhang, Brian L Hie, Xiaojing J Gao  
[bioRxiv 2025.09.19.677421](https://www.biorxiv.org/content/10.1101/2025.09.19.677421v2) • [Supplementary](https://www.biorxiv.org/content/biorxiv/early/2025/09/25/2025.09.19.677421/DC1/embed/media-1.pdf) • [code](https://github.com/SantiagoMille/germinal)

**mBER: Controllable de novo antibody design with million-scale experimental screening**  
Erik Swanson, Michael Nichols, Supriya Ravichandran, Pierce Ogden  
[bioRxiv 2025.09.26.678877](https://www.biorxiv.org/content/10.1101/2025.09.26.678877v1)

**Automated Deep Learning-Based Pipelines for Multi-Objective De Novo Protein Design**  
Amrita Nallathambi, Brian Kuhlman  
[Current protocols 5.10 (2025)](https://currentprotocols.onlinelibrary.wiley.com/doi/10.1002/cpz1.70208)

**Protein Hunter: exploiting structure hallucination within diffusion for protein design**  
Yehlin Cho, Griffin Rangel, Gaurav Bhardwaj, Sergey Ovchinnikov  
[bioRxiv 2025.10.10.681530](https://www.biorxiv.org/content/10.1101/2025.10.10.681530v2) • [code](https://github.com/yehlincho/Protein-Hunter)

**De novo protein design enables targeting of intractable oncogenic interfaces**  
Varshika Ram Prakash, Yusuf Najy, Kalel Garrett, Brian F.P. Edwards, Benjamin L Kidder  
[bioRxiv 2025.10.22.683953](https://www.biorxiv.org/content/10.1101/2025.10.22.683953v1) • [Supplementary](https://www.biorxiv.org/content/biorxiv/early/2025/10/23/2025.10.22.683953/DC1/embed/media-1.pdf)

**HalluDesign: Protein Optimization and de novo Design via Iterative Structure Hallucination and Sequence design**  
Minchao Fang, Chentong Wang, Jungang Shi, Fangbai Lian, Qihan Jin, Zhe Wang, Yanzhe Zhang, Zhanyuan Cui, YanJun Wang, Yitao Ke, Qingzheng Han, Longxing Cao  
[bioRxiv 2025.11.08.686881](https://www.biorxiv.org/content/10.1101/2025.11.08.686881v1) • [code](https://github.com/MinchaoFang/HalluDesign)

**Sequence and structural determinants of efficacious de novo chimeric antigen receptors**  
Arthur Chow, Hoyin Chu, Ruofan Li, Benan Nalbant, Abdul Dozic, Laura Kida, Caleb Lareau  
[bioRxiv 2025.12.12.694033](https://www.biorxiv.org/content/10.64898/2025.12.12.694033v1) • [code](https://github.com/clareaulab/denovo-cart-reproducibility)

**De novo design of protein competitors for small molecule immunosensing**  
Yosta de Stigter, Tallie Godschalk, Maarten Merkx  
[bioRxiv 2025.12.16.694474](https://www.biorxiv.org/content/10.64898/2025.12.16.694474v1) • [Supplementary](https://www.biorxiv.org/content/biorxiv/early/2025/12/16/2025.12.16.694474/DC1/embed/media-1.pdf)

**A Rapid and Universal Pipeline for High-Resolution GPCR Structure Determination through In Silico Construct Optimization and de novo Protein Design**  
Asato Kojima, Kouki Kawakami, Naoya Kobayashi, Kazuhiro Kobayashi, Toshiki E. Matsui, Kohei Uemoto, Yuzhong Gu, Masahiro Fukuda, Hideaki E. Kato  
[bioRxiv 2026.04.02.716066](https://www.biorxiv.org/content/10.64898/2026.04.02.716066v1) • [Supplementary](https://www.biorxiv.org/content/biorxiv/early/2026/04/06/2026.04.02.716066/DC1/embed/media-1.pdf)

**Computational design of an ultrapotent deltacoronavirus miniprotein inhibitor**  
Nathan G. Avery, Courtney N. Yoshiyama, Ashley L. Taylor, Young-Jun Park, Daniel Asarnow, Lisa Perruzza, Jack T. Brown, Davide Corti, Fabio Benigni, Tyler N. Starr, and David Veesler  
[Proceedings of the National Academy of Sciences 123.18 (2026)](https://www.pnas.org/doi/10.1073/pnas.2533456123)

**AI-Guided De Novo Design of a Caffeine-Induced Protein Dissociation System**。
Tatsuki Nonomura, Brendan McKee, Anna Price, Mingguang Cui, Zaynah Yousuf, Faith Tran, Lian He, Tianlu Wang, Yubin Zhou  
[J. Am. Chem. Soc. 2026](https://pubs.acs.org/doi/10.1021/jacs.6c02343)

**SwitchCraft: Training-Free Multi-Event Video Generation with Attention Controls**  
Qianxun Xu, Chenxi Song, Yujun Cai, Chi Zhang  
[arXiv:2602.23956](https://arxiv.org/abs/2602.23956)

**ComplexDesign: sequence-hallucination design of protein binders bridging multiple proteins**  
Jing Xu, Milong Ren, Ning Qi, Xinru Zhang, Zaikai He, Chungong Yu, Dongbo Bu  
[bioRxiv 2026.06.21.733655](https://www.biorxiv.org/content/10.64898/2026.06.21.733655v1) • [Supplementary](https://www.biorxiv.org/content/biorxiv/early/2026/06/24/2026.06.21.733655/DC1/embed/media-1.pdf)

**Efficient generation of epitope-targeted antibodies with Germinal**  
Luis S. Mille-Fragoso, Claudia L. Driscoll, John N. Wang, Haoyu Dai, Talal Widatalla, Jim L. Zhang, Xiaowei Zhang, Bing Rao, Liang Feng, Brian L. Hie & Xiaojing J. Gao  
[Nat Biotechnol (2026)](https://www.nature.com/articles/s41587-026-03187-0) • [code](https://github.com/SantiagoMille/germinal)

**Programmable design of synthetic plant immune receptors for pathogen protein recognition**  
Haocheng Zhu, Dandan Jiang, Qiao Zhang, Kang Zhang, Kevin Tianmeng Zhao, Jin-Long Qiu, and Caixia Gao  
[Science](https://www.science.org/doi/10.1126/science.aee1792)

**The Human Bindome: A Proteome-scale Atlas of Designed Binder Candidates**  
Julius Wenckstern, Anna M. Diaz-Rovira, Julia Kuhn, Arvid Ban, Rahma Hamdani, Roser Pruano-Milla, Evgenia Elizarova, Sandrine Georgeon, Kaiden Thompson, Matthias Hinterndorfer, Devanarayanan Siva Sankar, Maximilian Dunnebacke, David Desscan, Sreenath Nair, Marcelo Querino Lima Afonso, Jennifer Fleming, Sameer Velankar, Andrea Ablasser, Paola Picotti, Georg Winter, Mikko Taipale, Bruno E. Correia  
[bioRxiv 2026.07.30.741542](https://www.biorxiv.org/content/10.64898/2026.07.30.741542v1) • [code](https://github.com/wejulius/Bindome) • [website](https://bindome.epfl.ch)

#### 2.1.3 DMPfold2-based

**Design in the DARK: Learning Deep Generative Models for De Novo Protein Design**
Moffat, Lewis, Shaun M. Kandathil, and David T. Jones
[bioRxiv (2022)](https://www.biorxiv.org/content/10.1101/2022.01.27.478087v1) • [DMPfold2](https://github.com/psipred/DMPfold2)

#### 2.1.4 DeepAb-based

**Towards deep learning models for target-specific antibody design**
Sai Pooja Mahajan, Jeffrey Ruffolo, Rahel Frick, Jeffrey J. Gray
[Biophysical Journal 121.3 (2022)](https://www.cell.com/biophysj/pdf/S0006-3495(21)03758-9.pdf) • [DeepAb](https://github.com/RosettaCommons/DeepAb) • [lecture](https://www.youtube.com/watch?v=LIo-1jPfrns)

**Hallucinating structure-conditioned antibody libraries for target-specific binders**
Sai Pooja Mahajan, Jeffrey A Ruffolo, Rahel Frick, Jeffrey J. Gray
[bioRxiv 2022.06.06.494991](https://www.biorxiv.org/content/10.1101/2022.06.06.494991v1)/[Front. Immunol. 13:999034](https://www.frontiersin.org/articles/10.3389/fimmu.2022.999034/full) • [Supplementary](https://www.biorxiv.org/content/biorxiv/early/2022/06/06/2022.06.06.494991/DC1/embed/media-1.pdf) • [code](https://github.com/RosettaCommons/FvHallucinator)

#### 2.1.5 TRFold2-based

[News of TRDesign](https://mp.weixin.qq.com/s/OQzKawtL9RdK9HzYsfu80g)
[TIANRANG XLab](https://xlab.tianrang.com/)
paper unavailable • [slides](https://pan.baidu.com/share/init?surl=4AOW_D9dwlvC7VGGZA2tmQ&pwd=ffui) • [website](https://xcreator.tianrang.com/auth/login) • commercial • [news](https://mp.weixin.qq.com/s/45Gz7GWOGxHl0i6LXxTUpw)

#### 2.1.6 Boltz-based

**Boltzdesign1: Inverting All-Atom Structure Prediction Model for Generalized Biomolecular Binder Design**
Yehlin Cho, Martin Pacesa, Zhidian Zhang, Bruno E. Correia, Sergey Ovchinnikov
[bioRxiv 2025.04.06.647261](https://www.biorxiv.org/content/10.1101/2025.04.06.647261v1) • [code](https://github.com/yehlincho/BoltzDesign1)

**BoltzProt-1: Towards Efficient De Novo Binder Design with Good Developability**  
Talip Uçar, Jack Bates, Yunguan Fu, Wenxian Shi, Hannes Stark, Demitri Nava, Luca Cavalleri, Jeremy Wohlwend, Gabriele Corso, Saro Passaro  
[technical report](https://boltz.bio/boltzprot1-technical-report.pdf)/[bioRxiv 2026.06.23.733997](https://www.biorxiv.org/content/10.64898/2026.06.23.733997v1)

#### 2.1.7 RareFold-based

**RareFold: Structure prediction and design of proteins with noncanonical amino acids**  
Qiuzhen Li, Diandra Daumiller, Patrick Bryant  
[bioRxiv 2025.05.19.654846](https://www.biorxiv.org/content/10.1101/2025.05.19.654846v1) • [code](https://github.com/patrickbryant1/RareFold)

#### 2.1.8 HelixFold-based

**HelixDesign-Binder: A Scalable Production-Grade Platform for Binder Design Built on HelixFold3**  
Jie Gao, Jun Li, Jing Hu, Shanzhuo Zhang, Kunrui Zhu, Yueyang Huang, Xiaonan Zhang, Xiaomin Fang  
[arXiv:2505.21873](https://arxiv.org/abs/2505.21873) • ESM-IF-based

**HelixDesign-Antibody: A Scalable Production-Grade Platform for Antibody Design Built on HelixFold3**  
Jie Gao, Jing Hu, Shanzhuo Zhang, Kunrui Zhu, Sheng Qian, Yueyang Huang, Xiaonan Zhang, Xiaomin Fang  
[arXiv:2507.02345](https://arxiv.org/abs/2507.02345) • [website](https://paddlehelix.baidu.com/)

#### 2.1.9 ESMfold-based

**Design of proteins by parallel tempering in the sequence space**  
Preet Kalani, Vojtěch Spiwok  
[Protein Science 34.10 (2025)](https://onlinelibrary.wiley.com/doi/10.1002/pro.70246)

#### 2.1.10 tFold-based

**De novo design of epitope-specific antibodies via a structure-driven computational workflow**  
Fandi Wu, Yu Zhao, JiaXiang Wu, Biaobin Jiang, Bing He, Longkai Huang, Chenchen Qin, Yang Xiao, Fan Yang, Rubo Wang, Ningqiao Huang, Huaxian Jia, Yuyi Liu, Houtim Lai, Tingyang Xu, Fang Wang, Zihan Wu, Yidong Song, Shaoning Li, Wei Liu, Yu Rong, Peilin Zhao & Jianhua Yao  
[Nat Commun (2025)](https://www.nature.com/articles/s41467-025-67361-9) • [code](https://github.com/TencentAI4S/tfold)

#### 2.1.11 Chai-based

**De novo protein ligand design including protein flexibility and conformational adaptation**  
Jakob Agamia, Martin Zacharias  
[bioRxiv 2026.01.08.698398](https://www.biorxiv.org/content/10.64898/2026.01.08.698398v1) • [code](https:/github.com/JakobAgamia/AI-MCLig) • [Supplementary](https://www.biorxiv.org/content/biorxiv/early/2026/01/08/2026.01.08.698398/DC1/embed/media-1.pdf)

### 2.2 CM-Align

**AutoFoldFinder: An Automated Adaptive Optimization Toolkit for De Novo Protein Fold Design**
Shuhao Zhang, Youjun Xu, Jianfeng Pei, Luhua Lai
[NeurIPS 2021](https://www.mlsb.io/papers_2021/MLSB2021_AutoFoldFinder.pdf)

### 2.3 MSA-transformer-based

**Protein language models trained on multiple sequence alignments learn phylogenetic relationships**
Damiano Sgarbossa, Umberto Lupo, Anne-Florence Bitbol
[arXiv preprint arXiv:2203.15465 (2022)](https://arxiv.org/abs/2203.15465)/[bioRxiv 2022.04.14.488405](https://www.biorxiv.org/content/10.1101/2022.04.14.488405v1)

**EvoOpt: an MSA-guided, fully unsupervised sequence optimization pipeline for protein design**
Hideki Yamaguchi, Yutaka Saito
[NeurIPS 2022](https://www.mlsb.io/papers_2022/EvoOpt_an_MSA_guided_fully_unsupervised_sequence_optimization_pipeline_for_protein_design.pdf)

**Generative power of a protein language model trained on multiple sequence alignments**
Sgarbossa, Damiano, Umberto Lupo, and Anne-Florence Bitbol
[Elife 12 (2023): e79854](https://elifesciences.org/articles/79854) • [code](https://github.com/Bitbol-Lab/Iterative_masking)

### 2.4 LLM-based

#### 2.4.1 GPT-based

**Multi-segment preserving sampling for deep manifold sampler**
Daniel Berenberg, Jae Hyeon Lee, Simon Kelow, Ji Won Park, Andrew Watkins, Vladimir Gligorijević, Richard Bonneau, Stephen Ra, Kyunghyun Cho
[arXiv preprint arXiv:2205.04259 (2022)](https://arxiv.org/abs/2205.04259)

**Preference optimization of protein language models as a multi-objective binder design paradigm**
Pouria Mistani, Venkatesh Mysore
[arXiv:2403.04187](https://arxiv.org/abs/2403.04187)

**HMAMP: Hypervolume-Driven Multi-Objective Antimicrobial Peptides Design**
Li Wang, Yiping Li, Xiangzheng Fu, Xiucai Ye, Junfeng Shi, Gary G. Yen, Xiangxiang Zeng
[arXiv:2405.00753](https://arxiv.org/abs/2405.00753)

#### 2.4.2 ESM-based

**Generating novel protein sequences using Gibbs sampling of masked language models**
Sean R. Johnson, Sarah Monaco, Kenneth Massie, Zaid Syed
[bioRxiv 2021.01.26.428322](https://www.biorxiv.org/content/10.1101/2021.01.26.428322v1) • [code](https://github.com/seanrjohnson/protein_gibbs_sampler)

**A high-level programming language for generative protein design**
Brian Hie, Salvatore Candido, Zeming Lin, Ori Kabeli, Roshan Rao, Nikita Smetanin, Tom Sercu, Alexander Rives
[bioRxiv 2022.12.21.521526](https://www.biorxiv.org/content/10.1101/2022.12.21.521526v1)

**Language models generalize beyond natural proteins**
Robert Verkuil, Ori Kabeli, Yilun Du, Basile IM Wicky, Lukas F Milles, Justas Dauparas, David Baker, Sergey Ovchinnikov, Tom Sercu, Alexander Rives
[bioRxiv 2022.12.21.521521](https://www.biorxiv.org/content/10.1101/2022.12.21.521521v1)

**ESMFold Hallucinates Native-Like Protein Sequences**
Jeliazko R Jeliazkov, Diego del Alamo, Joel D Karpiak
[bioRxiv 2023.05.23.541774](https://www.biorxiv.org/content/10.1101/2023.05.23.541774v1)

**Protein Language Model Supervised Precise and Efficient Protein Backbone Design Method**
Bo Zhang, Kexin Liu, Zhuoqi Zheng, Yunfeiyang L