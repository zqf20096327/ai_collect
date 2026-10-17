

# Awesome Machine Learning for Combinatorial Optimization Resources
We would like to maintain a list of resources that utilize machine learning technologies to solve combinatorial optimization problems.

We mark work contributed by [Thinklab](http://thinklab.sjtu.edu.cn) with ⭐.

*Maintained by members in SJTU-Thinklab: Chang Liu, Runzhong Wang, Jiayi Zhang, Zelin Zhao, Haoyu Geng, Tianzhe Wang, Wenxuan Guo, Wenjie Wu, Nianzu Yang, Ziao Guo, Yang Li, Hao Xiong, Jiale Ma, Wenzheng Pan and Junchi Yan. We also thank [all contributers from the community](https://github.com/Thinklab-SJTU/awesome-ml4co/graphs/contributors)!*

*We are looking for post-docs interested in machine learning especially for learning combinatorial solvers, dynamic graphs, and reinforcement learning. Please send your up-to-date resume via yanjunchi AT sjtu.edu.cn.*

## [Content](#content)

<table>
<tr><td colspan="2"><a href="#survey-papers">1. Survey</a></td></tr>
<tr><td colspan="2"><a href="#problems">2. Problems</a></td></tr> 
<tr>
	<td>&emsp;<a href=#travelling-salesman-problem>2.1 Travelling Salesman Problem (TSP)</a></td>
	<td>&emsp;<a href=#job-shop-scheduling-problem>2.2 Job Shop Scheduling Problem (JSSP)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#flow-shop-problem>2.3 Flow Shop Problem (FSP)</a></td>
	<td>&emsp;<a href=#sorting-&-ranking>2.4 Sorting & Ranking (Sort&Rank)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#graph-matching>2.5 Graph Matching (GM)</a></td>
	<td>&emsp;<a href=#quadratic-assignment-problem>2.6 Quadratic Assignment Problem (QAP)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#portfolio-optimization>2.7 Portfolio Optimization (PortOpt)</a></td>
	<td>&emsp;<a href=#maximal-cut>2.8 Maximal Cut</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#vehicle-routing-problem>2.9 Vehicle Routing Problem (VRP)</a></td>
	<td>&emsp;<a href=#maximum-independent-set>2.10 Maximum Independent Set</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#generalization>2.11 Generalization</a></td>
	<td>&emsp;<a href=#orienteering-problem>2.12 Orienteering Problem (OP)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#knapsack>2.13 Knapsack</a></td>
	<td>&emsp;<a href=#boolean-satisfiability>2.14 Boolean Satisfiability (SAT)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#computing-resource-allocation>2.15 Computing Resource Allocation</a></td>
	<td>&emsp;<a href=#bin-packing-problem>2.16 Bin Packing Problem (BPP)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#graph-edit-distance>2.17 Graph Edit Distance (GED)</a></td>
	<td>&emsp;<a href=#hamiltonian-cycle-problem>2.18 Hamiltonian Cycle Problem (HCP)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#graph-coloring>2.19 Graph Coloring</a></td>
	<td>&emsp;<a href=#maximal-common-subgraph>2.20 Maximal Common Subgraph (MCS)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#influence-maximization>2.21 Influence Maximization</a></td>
	<td>&emsp;<a href=#max-clique>2.22 Max Clique</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#mixed-integer-programming>2.23 Mixed Integer Programming (MIP)</a></td>
	<td>&emsp;<a href=#causal-discovery>2.24 Causal Discovery</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#game-theoretic-semantics>2.25 Game Theoretic Semantics</a></td>
	<td>&emsp;<a href=#differentiable-optimization>2.26 Differentiable Optimization</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#car-dispatch>2.27 Car Dispatch</a></td>
	<td>&emsp;<a href=#electronic-design-automation>2.28 Electronic Design Automation (EDA)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#conjunctive-query-containment>2.29 Conjunctive Query Containment</a></td>
	<td>&emsp;<a href=#virtual-network-embedding>2.30 Virtual Network Embedding (VNE)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#predict+optimize>2.31 Predict+Optimize</a></td>
	<td>&emsp;<a href=#optimal-power-flow>2.32 Optimal Power Flow</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#facility-location-problem>2.33 Facility Location Problem (FLP)</a></td>
	<td>&emsp;<a href=#combinatorial-drug-recommendation>2.34 Combinatorial Drug Recommendation</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#stochastic-combinatorial-optimization>2.35 Stochastic Combinatorial Optimization</a></td>
	<td>&emsp;<a href=#vertex-cover>2.36 Vertex Cover</a></td>
</tr>
</table>




### [Survey Papers](#content)

1. **Neural Networks for Combinatorial Optimization: A Review of More Than a Decade of Research** INFORMS Journal on Computing, 1999. [journal](https://pubsonline.informs.org/doi/abs/10.1287/ijoc.11.1.15)

    *Kate A. Smith*

2. **Model-Based Search for Combinatorial Optimization: A Critical Survey.** Annals of Operations Research, 2004. [journal](https://link.springer.com/article/10.1023/B:ANOR.0000039526.52305.af)

    *Mark Zlochin, Mauro Birattari, Nicolas Meuleau, Marco Dorigo*

3. **A Survey of Reinforcement Learning and Agent-Based Approaches to Combinatorial Optimization.** Citeseer, 2012. [journal](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.468.5208&rep=rep1&type=pdf)

    *Victor Miagkikh*

4. **Machine Learning Approaches to Learning Heuristics for Combinatorial Optimization Problems.** Procedia Manufacturing, 2018. [journal](https://www.sciencedirect.com/science/article/pii/S2351978918311351)

    *Sadegh Mirshekarian, Dusan Sormaz*

5. **Boosting combinatorial problem modeling with machine learning.** IJCAI, 2018. [paper](https://www.ijcai.org/Proceedings/2018/0772.pdf)

    *Michele Lombardi, Michela Milano*

6. **Deep Reinforcement Learning as a Job Shop Scheduling Solver: A Literature Review** Hybrid Intelligent Systems, 2018. [journal](http://link.springer.com/10.1007/978-3-030-14347-3_34)

    *Bruno Cunha, Ana M. Madureira, Benjamim Fonseca, Duarte Coelho*

7. **A Review of combinatorial optimization with graph neural networks.** BigDIA, 2019. [paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8802843)

    *Tingfei Huang, Yang Ma, Yuzhen Zhou, Honglan Huang Huang, Dongmei Chen, Zidan Gong, Yao Liu*

8. **Machine Learning for Combinatorial Optimization: a Methodological Tour d'horizon.** EJOR, 2020. [journal](https://arxiv.org/abs/1811.06128)

    *Yoshua Bengio, Andrea Lodi, Antoine Prouvost*

9. **Reinforcement Learning for Combinatorial Optimization: A Survey.** Arxiv, 2020. [paper](https://arxiv.org/abs/2003.03600)

    *Nina Mazyavkina, Sergey Sviridov, Sergei Ivanov, Evgeny Burnaev*

10. **⭐Learning Graph Matching and Related Combinatorial Optimization Problems.** IJCAI, 2020. [paper](https://www.ijcai.org/proceedings/2020/0694.pdf)

    *Junchi Yan, Shuang Yang, Edwin R. Hancock*

11. **Learning Combinatorial Optimization on Graphs: A Survey with Applications to Networking.** IEEE ACCESS, 2020. [journal](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9125934)

    *Natalia Vesselinova, Rebecca Steinert, Daniel F. Perez-Ramirez, Magnus Boman*

12. **From Shallow to Deep Interactions Between Knowledge Representation, Reasoning and Machine Learning.** Arxiv, 2020. [paper](https://arxiv.org/abs/1912.06612)

    *Zied Bouraoui, Antoine Cornuéjols, Thierry Denœux, Sébastien Destercke, Didier Dubois, Romain Guillaume, João Marques-Silva, Jérôme Mengin, Henri Prade, Steven Schockaert, Mathieu Serrurier, Christel Vrain*

13. **A Survey on Reinforcement Learning for Combinatorial Optimization.** Arxiv, 2020. [paper](https://arxiv.org/abs/2008.12248v2)

    *Yunhao Yang, Andrew Whinston*

14. **Research Reviews of Combinatorial Optimization Methods Based on Deep Reinforcement Learning. (in chinese)** 自动化学报, 2020. [journal](http://www.aas.net.cn/article/doi/10.16383/j.aas.c200551)

    *Kai-Wen Li, Tao Zhang, Rui Wang, Wei-Jian Qin, Hui-Hui He, Hong Huang*

15. **Graph Learning for Combinatorial Optimization: A Survey of State-of-the-Art.** Data Science and Engineering, 2021. [journal](https://link.springer.com/article/10.1007/s41019-021-00155-3)

    *Yue Peng, Byron Choi, Jianliang Xu*

16. **Machine Learning for Electronic Design Automation (EDA) : A Survey** TODAES, 2021. [journal](https://arxiv.org/abs/2102.03357)

    *Guyue Huang, Jingbo Hu, Yifan He, Jialong Liu, Mingyuan Ma, Zhaoyang Shen, Juejian Wu, Yuanfan Xu, Hengrui Zhang, Kai Zhong, others*

17. **⭐A Survey for Solving Mixed Integer Programming via Machine Learning** Neurocomputing, 2022. [journal](https://www.sciencedirect.com/science/article/pii/S0925231222014035)

    *Jiayi Zhang, Chang Liu, Xijun Li, Hui-Ling Zhen, Mingxuan Yuan, Yawen Li, Junchi Yan*

18. **Combinatorial Optimization and Reasoning with Graph Neural Networks** JMLR, 2023. [journal](https://jmlr.org/papers/volume24/21-0449/21-0449.pdf)

    *Quentin Cappart, Didier Chetelat, Elias B. Khalil, Andrea Lodi, Christopher Morris, Petar Velickovic*

19. **Applicability of Neural Combinatorial Optimization: A Critical View** TELO, 2024. [journal](https://dl.acm.org/doi/pdf/10.1145/3647644), [code](https://github.com/TheLeprechaun25/Applicability-NCO)

    *Andoni I. Garmendia, Josu Ceberio, Alexander Mendiburu*

20. **Survey on Neural Routing Solvers** Arxiv, 2026. [paper](https://arxiv.org/abs/2602.21761)

    *Yunpeng Ba, Xi Lin, Changliang Zhou, Ruihao Zheng, Zhenkun Wang, Xinyan Liang, Zhichao Lu, Jianyong Sun, Yuhua Qian, Qingfu Zhang*

## [Problems](#content)

### [Travelling Salesman Problem](#content)

#### Benchmark Results (Beta)

*Beta feature: benchmark charts are generated from `data/benchmark_results.csv`. The results, sourced directly from original papers using common benchmarks, are presented to directly illustrate the evolution of performance. Runtime is normalized to 1000 instances by instance count only; hardware is not normalized. Gap charts show main-experiment points within benchmark-specific gap bounds (3.5% for TSP-500, 5% otherwise); within each baseline, slower points are shown only when they improve gap.*

##### Uniform TSP-500

[![Uniform TSP-500 benchmark chart](assets/benchmarks/travelling-salesman-problem_uniform-tsp-500_all-baselines.svg)](assets/benchmarks/travelling-salesman-problem_uniform-tsp-500_all-baselines.svg)

##### Uniform TSP-1000

[![Uniform TSP-1000 benchmark chart](assets/benchmarks/travelling-salesman-problem_uniform-tsp-1000_all-baselines.svg)](assets/benchmarks/travelling-salesman-problem_uniform-tsp-1000_all-baselines.svg)

1. **Learning Combinatorial Optimization Algorithms over Graphs.** NeurIPS, 2017. [paper](https://arxiv.org/abs/1704.01665)

    *Hanjun Dai, Elias B Khalil, Yuyu Zhang, Bistra Dilkina, Le Song*

2. **Learning Heuristics for the TSP by Policy Gradient** CPAIOR, 2018. [paper](https://link.springer.com/chapter/10.1007/978-3-319-93031-2_12), [code](https://github.com/MichelDeudon/encode-attend-navigate)

    *Michel DeudonPierre CournutAlexandre Lacoste*

3. **Attention, Learn to Solve Routing Problems!** ICLR, 2019. [paper](https://arxiv.org/abs/1803.08475)

    *Wouter Kool, Herke Van Hoof, Max Welling*

4. **Learning to Solve NP-Complete Problems: A Graph Neural Network for Decision TSP.** AAAI, 2019. [paper](https://ojs.aaai.org/index.php/AAAI/article/view/4399)

    *Marcelo Prates, Pedro HC Avelar, Henrique Lemos, Luis C Lamb, Moshe Y. Vardi*

5. **An Efficient Graph Convolutional Network Technique for the Travelling Salesman Problem** Arxiv, 2019. [paper](https://arxiv.org/abs/1906.01227), [code](https://github.com/chaitjo/graph-convnet-tsp)

    *Chaitanya K. Joshi, Thomas Laurent, Xavier Bresson*

6. **POMO: Policy Optimization with Multiple Optima for Reinforcement Learning.** NeurIPS, 2020. [paper](https://arxiv.org/abs/2010.16011), [code](https://github.com/yd-kwon/POMO/)

    *Yeong-Dae Kwon, Jinho Choo, Byoungjip Kim, Iljoo Yoon, Seungjai Min, Youngjune Gwon*

7. **Generalize a Small Pre-trained Model to Arbitrarily Large TSP Instances.** Arxiv, 2020. [paper](https://arxiv.org/abs/2012.10658)

    *Zhang-Hua Fu, Kai-Bin Qiu, Hongyuan Zha*

8. **A Reinforcement Learning Approach for Optimizing Multiple Traveling Salesman Problems over Graphs** KBS, 2020. [journal](https://www.sciencedirect.com/science/article/pii/S0950705120304445)

    *Yujiao Hu, Yuan Yao, Wee Sun Lee*

9. **Learning 2-opt Heuristics for the Traveling Salesman Problem via Deep Reinforcement Learning** ACML, 2020. [paper](http://proceedings.mlr.press/v129/costa20a), [code](https://github.com/paulorocosta/learning-2opt-drl)

    *d O Costa, Paulo R, Jason Rhuggenaath, Yingqian Zhang, Alp Akcay*

10. **Deep Reinforcement Learning for Combinatorial Optimization: Covering Salesman Problems.** IEEE Trans Cybern, 2021. [journal](https://arxiv.org/abs/2102.05875)

    *Kaiwen Li, Tao Zhang, Rui Wang Yuheng Wang, Yi Han*

11. **The Transformer Network for the Traveling Salesman Problem** IPAM, 2021. [paper](http://helper.ipam.ucla.edu/publications/dlc2021/dlc2021_16703.pdf)

    *Xavier Bresson，Thomas Laurent*

12. **Learning Improvement Heuristics for Solving Routing Problems** TNNLS, 2021. [journal](https://ieeexplore.ieee.org/abstract/document/9393606?casa_token=mFeyLmrOGfIAAAAA:nmAkjUaTSooYurWHuWGYNoguV453anw9Enyv45xG5jb2oCps6QE4A1CFe1EmFmTzbON6cL5maw)

    *Yaoxin Wu, Wen Song, Zhiguang Cao, Jie Zhang, Andrew Lim*

13. **Reversible Action Design for Combinatorial Optimization with Reinforcement Learning** Arxiv, 2021. [paper](https://arxiv.org/abs/2102.07210)

    *Fan Yao, Renqin Cai, Hongning Wang*

14. **Solving Dynamic Traveling Salesman Problems with Deep Reinforcement Learning.** TNNLS, 2021. [journal](https://ieeexplore.ieee.org/document/9537638)

    *Zizhen Zhang, Hong Liu, Meng Chu Zhou, Jiahai Wang*

15. **ScheduleNet: Learn to Solve Multi-agent Scheduling Problems with Reinforcement Learning** Arxiv, 2021. [paper](https://arxiv.org/abs/2106.03051)

    *Junyoung Park, Sanjar Bakhtiyar, Jinkyoo Park*

16. **DAN: Decentralized Attention-based Neural Network to Solve the MinMax Multiple Traveling Salesman Problem** Arxiv, 2021. [paper](https://arxiv.org/abs/2109.04205)

    *Yuhong Cao, Zhanhong Sun, Guillaume Sartoretti*

17. **Reinforcement Learning for Route Optimization with Robustness Guarantees** IJCAI, 2021. [paper](https://www.ijcai.org/proceedings/2021/0357.pdf)

    *Tobias Jacobs, Francesco Alesiani, Gulcin Ermis*

18. **Combining Reinforcement Learning with Lin-Kernighan-Helsgaun Algorithm for the Traveling Salesman Problem** AAAI, 2021. [paper](https://ojs.aaai.org/index.php/AAAI/article/view/17476/17283), [code](https://github.com/JHL-HUST/VSR-LKH-V2)

    *Jiongzhi Zheng, Kun He, Jianrong Zhou, Yan Jin, Chu-Min Li*

19. **Learning to Sparsify Travelling Salesman Problem Instances** CPAIOR, 2021. [paper](https://dx.doi.org/10.1007/978-3-030-78230-6_26)

    *James Fitzpatrick, Deepak Ajwani, Paula Carroll*

20. **Learning TSP Requires Rethinking Generalization** CP, 2021. [paper](https://arxiv.org/pdf/2006.07054.pdf), [code](https://github.com/chaitjo/learning-tsp)

    *Chaitanya K. Joshi, Quentin Cappart, Louis-Martin Rousseau, Thomas Laurent*

21. **The First AI4TSP Competition: Learning to Solve Stochastic Routing Problems** Arxiv, 2022. [paper](https://arxiv.org/abs/2201.10453), [code](https://github.com/paulorocosta/ai-for-tsp-competition)

    *Laurens Bliek, Paulo da Costa, Reza Refaei Afshar, Yingqian Zhang, Tom Catshoek, Daniel Vos, Sicco Verwer, Fynn Schmitt-Ulms, Andre Hottung, Tapan Shah, others*

22. **Graph Neural Network Guided Local Search for the Traveling Salesperson Problem** ICLR, 2022. [paper](https://openreview.net/forum?id=ar92oEosBIg)

    *Benjamin Hudson, Qingbiao Li, Matthew Malencia, Amanda Prorok*

23. **Preference Conditioned Neural Multi-objective Combinatorial Optimization** ICLR, 2022. [paper](https://openreview.net/forum?id=QuObT9BTWo)

    *Xi Lin, Zhiyuan Yang, Qingfu Zhang*

24. **Learning Generalizable Models for Vehicle Routing Problems via Knowledge Distillation** NeurIPS, 2022. [paper](https://openreview.net/forum?id=sOVNpUEgKMp), [code](https://github.com/jieyibi/AMDKD)

    *Jieyi Bi, Yining Ma, Jiahai Wang, Zhiguang Cao, Jinbiao Chen, Yuan Sun, Yeow Meng Chee*

25. **DIMES: A Differentiable Meta Solver for Combinatorial Optimization Problems** NeurIPS, 2022. [paper](https://openreview.net/forum?id=9u05zr0nhx)

    *Ruizhong Qiu, Zhiqing Sun, Yiming Yang*

26. **Sym-NCO: Leveraging Symmetricity for Neural Combinatorial Optimization** NeurIPS, 2022. [paper](https://openreview.net/forum?id=kHrE2vi5Rvs), [code](https://github.com/alstn12088/Sym-NCO)

    *Minsu Kim, Junyoung Park, Jinkyoo Park*

27. **Simulation-guided Beam Search for Neural Combinatorial Optimization** NeurIPS, 2022. [paper](https://openreview.net/forum?id=tYAS1Rpys5), [code](https://github.com/yd-kwon/SGBS)

    *Jinho Choo, Yeong-Dae Kwon, Jihoon Kim, Jeongwoo Jae, Andr{\'e} Hottung, Kevin Tierney, Youngjune Gwon*

28. **Generalization of Neural Combinatorial Solvers Through the Lens of Adversarial Robustness** ICLR, 2022. [paper](https://openreview.net/forum?id=vJZ7dPIjip3)

    *Simon Geisler, Johanna Sommer, Jan Schuchardt, Aleksandar Bojchevski, Stephan Günnemann*

29. **⭐LinSATNet: The Positive Linear Satisfiability Neural Networks** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/25110), [code](https://github.com/Thinklab-SJTU/LinSATNet)

    *Runzhong Wang, Yunhao Zhang, Ziao Guo, Tianyi Chen, Xiaokang Yang, Junchi Yan*

30. **Learning to CROSS exchange to solve min-max vehicle routing problems** ICLR, 2023. [paper](https://openreview.net/forum?id=ZcnzsHC10Y)

    *Minjun Kim, Junyoung Park, Jinkyoo Park*

31. **Generalize Learned Heuristics to Solve Large-scale Vehicle Routing Problems in Real-time** ICLR, 2023. [paper](https://openreview.net/forum?id=6ZajpxqTlQ)

    *Qingchun Hou, Jingwei Yang, Yiqiang Su, Xiaoqing Wang, Yuming Deng*

32. **⭐ROCO: A General Framework for Evaluating Robustness of Combinatorial Optimization Solvers on Graphs** ICLR, 2023. [paper](https://openreview.net/forum?id=2r6YMqz4Mml), [code](https://github.com/Thinklab-SJTU/ROCO)

    *Han Lu, Zenan Li, Runzhong Wang, Qibing Ren, Xijun Li, Mingxuan Yuan, Jia Zeng, Xiaokang Yang, Junchi Yan*

33. **Pointerformer: Deep Reinforced Multi-Pointer Transformer for the Traveling Salesman Problem** Arxiv, 2023. [paper](https://arxiv.org/abs/2304.09407), [code](https://github.com/Pointerformer/Pointerformer)

    *Yan Jin, Yuandong Ding, Xuanhao Pan, Kun He, Li Zhao, Tao Qin, Lei Song, Jiang Bian*

34. **H-tsp: Hierarchically solving the large-scale traveling salesman problem** AAAI, 2023. [paper](https://www.microsoft.com/en-us/research/publication/h-tsp-hierarchically-solving-the-large-scale-traveling-salesman-problem/), [code](https://github.com/Learning4Optimization-HUST/H-TSP)

    *Xuanhao Pan, Yan Jin, Yuandong Ding, Mingxiao Feng, Li Zhao, Lei Song, Jiang Bian*

35. **Select and Optimize: Learning to solve large-scale TSP instances** AISTATS, 2023. [paper](https://proceedings.mlr.press/v206/cheng23a.html)

    *Hanni Cheng, Haosi Zheng, Ya Cong, Weihao Jiang, Shiliang Pu*

36. **Multi-View Graph Contrastive Learning for Solving Vehicle Routing Problems** UAI, 2023. [paper](https://openreview.net/pdf?id=Z-mRKVaxVU3)

    *Yuan Jiang, Zhiguang Cao, Yaoxin Wu, Jie Zhang*

37. **Revisiting Sampling for Combinatorial Optimization** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/23661)

    *Haoran, Goshvadi Katayoon, Nova Azade, Schuurmans Dale Sun, Dai Hanjun.*

38. **Meta-SAGE: Scale Meta-Learning Scheduled Adaptation with Guided Exploration for Mitigating Scale Shift on Combinatorial Optimization** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/25138)

    *Jiwoo Son, Minsu Kim, Hyeonah Kim, Jinkyoo Park*

39. **Towards Omni-generalizable Neural Methods for Vehicle Routing Problems** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/25267), [code](https://github.com/RoyalSkye/Omni-VRP)

    *Zhou Jianan, Yaoxin Wu, Wen Song, Zhiguang Cao, Jie Zhang*

40. **DIFUSCO: Graph-based Diffusion Solvers for Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=JV8Ff0lgVV), [code](https://github.com/Edward-Sun/DIFUSCO)

    *Zhiqing Sun, Yiming Yang*

41. **DeepACO: Neural-enhanced Ant Systems for Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=cd5D1DD923), [code](https://github.com/henry-yeh/DeepACO)

    *Haoran Ye, Jiarui Wang, Zhiguang Cao, Helan Liang, Yong Li*

42. **Winner Takes It All: Training Performant RL Populations for Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=v6VpqGcGAR)

    *Nathan Grinsztajn, Daniel Furelos-Blanco, Shikha Surana, Cl{\'e}ment Bonnet, Thomas D Barrett*

43. **Optimizing Solution-Samplers for Combinatorial Problems: The Landscape of Policy-Gradient Methods** NeurIPS, 2023. [paper](https://openreview.net/forum?id=mmTy1iyU5G), [code](https://openreview.net/attachment?id=mmTy1iyU5G&name=supplementary_material)

    *Constantine Caramanis, Dimitris Fotakis, Alkis Kalavasis, Vasilis Kontonis, Christos Tzamos*

44. **Combinatorial Optimization with Policy Adaptation using Latent Space Search** NeurIPS, 2023. [paper](https://openreview.net/forum?id=vpMBqdt9Hl)

    *Felix Chalumeau, Shikha Surana, Cl{\'e}ment Bonnet, Nathan Grinsztajn, Arnu Pretorius, Alexandre Laterre, Thomas D Barrett*

45. **Efficient Meta Neural Heuristic for Multi-Objective Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=593fc38lhN), [code](https://github.com/bill-cjb/EMNH)

    *Jinbiao Chen, Jiahai Wang, Zizhen Zhang, Zhiguang Cao, Te Ye, Siyuan Chen*

46. **BQ-NCO: Bisimulation Quotienting for Efficient Neural Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=BRqlkTDvvm), [code](https://github.com/naver/bq-nco)

    *Darko Drakulic, Sofia Michel, Florian Mai, Arnaud Sors, Jean-Marc Andreoli*

47. **Neural Combinatorial Optimization with Heavy Decoder: Toward Large Scale Generalization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=RBI4oAbdpm), [code](https://github.com/CIAM-Group/NCO_code/tree/main/single_objective/LEHD)

    *Fu Luo, Xi Lin, Fei Liu, Qingfu Zhang, Zhenkun Wang*

48. **Neural Multi-Objective Combinatorial Optimization with Diversity Enhancement** NeurIPS, 2023. [paper](https://openreview.net/forum?id=N4JkStI1fe), [code](https://github.com/bill-cjb/NHDE)

    *Jinbiao Chen, Zizhen Zhang, Zhiguang Cao, Yaoxin Wu, Yining Ma, Te Ye, Jiahai Wang*

49. **Unsupervised Learning for Solving the Travelling Salesman Problem** NeurIPS, 2023. [paper](https://openreview.net/forum?id=lAEc7aIW20)

    *Yimeng Min, Yiwei Bai, Carla P Gomes*

50. **Ensemble-based Deep Reinforcement Learning for Vehicle Routing Problems under Distribution Shift** NeurIPS, 2023. [paper](https://openreview.net/forum?id=HoBbZ1vPAh)

    *Yuan Jiang, Zhiguang Cao, Yaoxin Wu, Wen Song, Jie Zhang*

51. **Learning to Search Feasible and Infeasible Regions of Routing Problems with Flexible Neural k-Opt** NeurIPS, 2023. [paper](https://openreview.net/forum?id=q1JukwH2yP), [code](https://github.com/yining043/NeuOpt)

    *Yining Ma, Zhiguang Cao, Yeow Meng Chee*

52. **⭐T2T: From Distribution Learning in Training to Gradient Search in Testing for Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=JtF0ugNMv2), [code](https://github.com/Thinklab-SJTU/T2TCO)

    *Yang Li, Jinpei Guo, Runzhong Wang, Junchi Yan*

53. **Reinforced Lin–Kernighan–Helsgaun Algorithms for the Traveling Salesman Problems** Knowledge-Based Systems, 2023. [journal](https://www.sciencedirect.com/science/article/pii/S0950705122012400), [code](https://github.com/JHL-HUST/VSR-LKH-V2)

    *Jiongzhi Zheng, Kun He, Jianrong Zhou, Yan Jin, Chu-Min Li*

54. **Neural Improvement Heuristics for Graph Combinatorial Optimization Problems** TNNLS, 2023. [journal](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10271315&casa_token=Hqn_wH2HAjEAAAAA:rTd6KVaoKVjrFWASa-Ma0vC6CBvsmMUHnoWik2DyD56NbnfNOqBG5qZTBLR5hqf9vpCotivB_BU&tag=1), [code](https://github.com/TheLeprechaun25/neural-improvement-heuristics)

    *Andoni I. Garmendia, Josu Ceberio, Alexander Mendiburu*

55. **GLOP: Learning Global Partition and Local Construction for Solving Large-Scale Routing Problems in Real-Time** AAAI, 2024. [paper](https://arxiv.org/abs/2312.08224), [code](https://github.com/henry-yeh/GLOP)

    *Haoran Ye, Jiarui Wang, Helan Liang, Zhiguang Cao, Yong Li, Fanzhang Li*

56. **Distilling Autoregressive Models to Obtain High-Performance Non-autoregressive Solvers for Vehicle Routing Problems with Faster Inference Speed** AAAI, 2024. [paper](https://arxiv.org/abs/2312.12469), [code](https://github.com/xybFight/GNARKD)

    *Yubin Xiao, Di Wang, Boyang Li, Mingzhao Wang, Xuan Wu, Changliang Zhou, You Zhou*

57. **Position: Rethinking Post-Hoc Search-Based Neural Approaches for Solving Large-Scale Traveling Salesman Problems** ICML, 2024. [paper](https://arxiv.org/abs/2406.03503), [code](https://github.com/xyfffff/rethink_mcts_for_tsp)

    *Yifan Xia, Xianliang Yang, Zichuan Liu, Zhihao Liu, Lei Song, Jiang Bian*

58. **MARCO: A Memory-Augmented Reinforcement Framework for Combinatorial Optimization** IJCAI, 2024. [paper](https://www.ijcai.org/proceedings/2024/0766.pdf), [code](https://github.com/TheLeprechaun25/MARCO)

    *Andoni I. Garmendia, Quentin Cappart, Josu Ceberio, Alexander Mendiburu*

59. **Neural Combinatorial Optimization for Robust Routing Problem with Uncertain Travel Times** NeurIPS, 2024. [paper](https://openreview.net/pdf?id=DoewNm2uT3)

    *Pei Xiao, Zizhen Zhang, Jinbiao Chen, Jiahai Wang, Zhenzhen Zhang*

60. **Collaboration! Towards Robust Neural Methods for Routing Problems** NeurIPS, 2024. [paper](https://openreview.net/forum?id=YfQA78gEFA), [code](https://github.com/RoyalSkye/Routing-CNF)

    *Jianan Zhou, Yaoxin Wu, Zhiguang Cao, Wen Song, Jie Zhang, Zhiqi Shen*

61. **UDC: A Unified Neural Divide-and-Conquer Framework for Large-Scale Combinatorial Optimization Problems** NeurIPS, 2024. [paper](https://openreview.net/pdf?id=dCgbyvmlwL), [code](https://github.com/CIAM-Group/NCO_code/tree/main/single_objective/UDC-Large-scale-CO-master)

    *Zhi Zheng, Changliang Zhou, Tong Xialiang, Mingxuan Yuan, Zhenkun Wang*

62. **Learning to Handle Complex Constraints for Vehicle Routing Problems** NeurIPS, 2024. [paper](https://openreview.net/forum?id=Ktx95ZuRjP)

    *Jieyi Bi, Yining Ma, Jianan Zhou, Wen Song, Zhiguang Cao, Yaoxin Wu, Jie Zhang*

63. **⭐Fast T2T: Optimization Consistency Speeds Up Diffusion-Based Training-to-Testing Solving for Combinatorial Optimization** NeurIPS, 2024. [paper](https://openreview.net/pdf?id=xDrKZOZEOc), [code](https://github.com/Thinklab-SJTU/Fast-T2T)

    *Yang Li, Jinpei Guo, Runzhong Wang, Hongyuan Zha, Junchi Yan*

64. **Evolution of Heuristics: Towards Efficient Automatic Algorithm Design Using Large Language Model** ICML, 2024. [paper](https://openreview.net/forum?id=BwAkaxqiLB), [code](https://github.com/FeiLiu36/EoH)

    *Fei Liu, Xialiang Tong, Mingxuan Yuan, Xi Lin, Fu Luo, Zhenkun Wang, Zhichao Lu, Qingfu Zhang*

65. **ReEvo: Large Language Models as Hyper-Heuristics with Reflective Evolution** NeurIPS, 2024. [paper](https://openreview.net/forum?id=483IPG0HWL), [code](https://github.com/ai4co/reevo)

    *Haoran Ye, Jiarui Wang, Zhiguang Cao, Federico Berto, Chuanbo Hua, Haeyeon Kim, Jinkyoo Park, Guojie Song*

66. **Rethinking Neural Multi-Objective Combinatorial Optimization via Neat Weight Embedding** ICLR, 2025. [paper](https://openreview.net/forum?id=GM7cmQfk2F)

    *Jinbiao Chen, Zhiguang Cao, Jiahai Wang, Yaoxin Wu, Hanzhang Qin, Zizhen Zhang, Yue-Jiao Gong*

67. **Neural Multi-Objective Combinatorial Optimization via Graph-Image Multimodal Fusion** ICLR, 2025. [paper](https://openreview.net/forum?id=4sJ2FYE65U)

    *Jinbiao Chen, Jiahai Wang, Zhiguang Cao, Yaoxin Wu*

68. **Boosting Neural Combinatorial Optimization for Large-Scale Vehicle Routing Problems** ICLR, 2025. [paper](https://openreview.net/forum?id=TbTJJNjumY)

    *Fu Luo, Xi Lin, Yaoxin Wu, Zhenkun Wang, Tong Xialiang, Mingxuan Yuan, Qingfu Zhang*

69. **⭐UniCO: On Unified Combinatorial Optimization via Problem Reduction to Matrix-Encoded General TSP** ICLR, 2025. [paper](https://openreview.net/forum?id=yEwakMNIex), [code](https://github.com/Thinklab-SJTU/UniCO)

    *Wenzheng Pan, Hao Xiong, Jiale Ma, Wentao Zhao, Yang Li, Junchi Yan*

70. **Efficient and Robust Neural Combinatorial Optimization via Wasserstein-Based Coresets** ICLR, 2025. [paper](https://openreview.net/forum?id=F57HPKZ6KD)

    *Xu Wang, Fuyou Miao, Wenjie Liu, Yan Xiong*

71. **⭐Unify ML4TSP: Drawing Methodological Principles for TSP and Beyond from Streamlined Design Space of Learning and Search** ICLR, 2025. [paper](https://openreview.net/pdf?id=grU1VKEOLi), [code](https://github.com/Thinklab-SJTU/ML4TSPBench)

    *Yang Li, Jiale Ma, Wenzheng Pan, Runzhong Wang, Haoyu Geng, Nianzu Yang, Junchi Yan*

72. **⭐ML4CO-Bench-101: Benchmark Machine Learning for Classic Combinatorial Problems on Graphs** NeurIPS, 2025. [paper](https://openreview.net/forum?id=ye4ntB1Kzi), [code](https://github.com/Thinklab-SJTU/ML4CO-Bench-101)

    *Jiale Ma, Wenzheng Pan, Yang Li, Junchi Yan*

73. **⭐COExpander: Adaptive Solution Expansion for Combinatorial Optimization** ICML, 2025. [paper](https://openreview.net/forum?id=KMaBXMWsBM), [code](https://github.com/Thinklab-SJTU/COExpander)

    *Jiale Ma, Wenzheng Pan, Yang Li, Junchi Yan*

74. **Large Language Models as End-to-end Combinatorial Optimization Solvers** NeurIPS, 2025. [paper](https://neurips.cc/virtual/2025/loc/san-diego/poster/115835), [code](https://github.com/Summer142857/LLMCoSolver)

    *Xia Jiang, Yaoxin Wu, Minshuo Li, Zhiguang Cao, Yingqian Zhang*

75. **⭐StruDiCO: Structured Denoising Diffusion with Gradient-free Inference-stage Boosting for Memory and Time Efficient Combinatorial Optimization** NeurIPS, 2025. [paper](https://openreview.net/forum?id=P69X3V4WwH), [code](https://github.com/yuuuuwang/StruDiCO)

    *Yu Wang, Yang Li, Junchi Yan, Yi Chang*

76. **⭐Generation as search operator for test-time scaling of diffusion-based combinatorial optimization** NeurIPS, 2025. [paper](https://openreview.net/forum?id=9JM03CQwzC), [code](https://github.com/Thinklab-SJTU/GenSCO)

    *Yang Li, Lvda Chen, Haonan Wang, Runzhong Wang, Junchi Yan*

77. **Optimization by Parallel Quasi-Quantum Annealing with Gradient-Based Sampling** ICLR, 2025. [paper](https://openreview.net/forum?id=9EfBeXaXf0), [code](https://github.com/Yuma-Ichikawa/QQA4CO)

    *Yuma Ichikawa, Yamato Arai*

78. **BOPO: Neural Combinatorial Optimization via Best-anchored and Objective-guided Preference Optimization** ICML, 2025. [paper](https://openreview.net/forum?id=FLy6yXdrlW), [code](https://github.com/L-Z-7/BOPO)

    *Zijun Liao, Jinbiao Chen, Debing Wang, Zizhen Zhang, Jiahai Wang*

79. **Neural Solver Selection for Combinatorial Optimization** ICML, 2025. [paper](https://openreview.net/forum?id=e0OFWfvLCO)

    *Chengrui Gao, Haopu Shang, Ke Xue, Chao Qian*

80. **Preference Optimization for Combinatorial Optimization Problems** ICML, 2025. [paper](https://openreview.net/forum?id=Jwe5FJ8QGx), [code](https://github.com/MingjunPan/Preference-Optimization-for-Combinatorial-Optimization-Problems)

    *Mingjun Pan, Guanquan Lin, You-Wei Luo, Bin Zhu, Zhien Dai, Lijun Sun, Chun Yuan*

81. **PARCO: Parallel AutoRegressive Models for Multi-Agent Combinatorial Optimization** NeurIPS, 2025. [paper](https://openreview.net/forum?id=9F2Cmgo17M), [code](https://github.com/ai4co/parco)

    *Federico Berto, Chuanbo Hua, Laurin Luttmann, Jiwoo Son, Junyoung Park, Kyuree Ahn, Changhyun Kwon, Lin Xie, Jinkyoo Park*

82. **Differentiable extensions with rounding guarantees for combinatorial optimization over permutations** NeurIPS, 2025. [paper](https://openreview.net/forum?id=aAxk0cw6GW)

    *Robert R Nerem, Zhishang Luo, Akbar Rafiey, Yusu Wang*

83. **Improving Generalization of Neural Combinatorial Optimization for Vehicle Routing Problems via Test-Time Projection Learning** NeurIPS, 2025. [paper](https://openreview.net/forum?id=QPJjiNCRq1), [code](https://github.com/CIAM-Group/TTPL)

    *Yuanyao Chen, Rongsheng Chen, Fu Luo, Zhenkun Wang*

84. **Complexity Scaling Laws for Neural Models using Combinatorial Optimization** NeurIPS, 2025. [paper](https://openreview.net/forum?id=EdKl4PulMX)

    *Lowell Weissman, Michael Krumdick, A. Lynn Abbott*

85. **Solving the Asymmetric Traveling Salesman Problem via Trace-Guided Cost Augmentation** NeurIPS, 2025. [paper](https://openreview.net/forum?id=CNxrp7u5gV)

    *Zhen Zhang, Javen Qinfeng Shi, Wee Sun Lee*

86. **Learning to Insert for Constructive Neural Vehicle Routing Solver** NeurIPS, 2025. [paper](https://openreview.net/forum?id=SXr3Dynctm), [code](https://github.com/CIAM-Group/L2C_Insert)

    *Fu Luo, Xi Lin, Mengyuan Zhong, Fei Liu, Zhenkun Wang, Jianyong Sun, Qingfu Zhang*

87. **Neural Combinatorial Optimization for Time-Dependent Traveling Salesman Problem** NeurIPS, 2025. [paper](https://openreview.net/forum?id=UXTR6ZYV1x)

    *Ruixiao Yang, Chuchu Fan*

88. **Adversarial Generative Flow Network for Solving Vehicle Routing Problems** ICLR, 2025. [paper](https://openreview.net/forum?id=tBom4xOW1H), [code](https://github.com/ZHANG-NI/AGFN)

    *Ni Zhang, Jingfeng Yang, Zhiguang Cao, Xu Chi*

89. **Projecting Latent RL Actions: Towards Generalizable and Scalable Graph Combinatorial Optimization** Arxiv, 2026. [paper](https://arxiv.org/abs/2605.19721), [code](https://github.com/terranovafr/LaGCO-RL)

    *Franco Terranova, Guillermo Bernardez, Albert Cabellos-Aparicio, Nina Miolane, Abdelkader Lahmadi*

90. **Generalizable Heuristic Generation Through LLMs with Meta-Optimization** ICLR, 2026. [paper](https://arxiv.org/abs/2505.20881), [code](https://github.com/yiding-s/MoH)

    *Yiding Shi, Jianan Zhou, Wen Song, Jieyi Bi, Yaoxin Wu, Zhiguang Cao, Jie Zhang*

91. **DRAGON: LLM-Driven Decomposition and Reconstruction Agents for Large-Scale Combinatorial Optimization** AAMAS, 2026. [paper](https://arxiv.org/abs/2601.06502)

    *Shengkai Chen, Zhiguang Cao, Jianan Zhou, Yaoxin Wu, Senthilnath Jayavelu, Zhuoyi Lin, Xiaoli Li, Shili Xiang*

92. **Bridging Synthetic and Real Routing Problems via LLM-Guided Instance Generation and Progressive Adaptation** AAAI, 2026. [paper](https://arxiv.org/abs/2511.10233), [code](https://github.com/HenryZhu1029/EvoReal)

    *Jianghan Zhu, Yaoxin Wu, Zhuoyi Lin, Zhengyuan Zhang, Haiyan Yin, Zhiguang Cao, Senthilnath Jayavelu, Xiaoli Li*

93. **EoH-S: Evolution of Heuristic Set using LLMs for Automated Heuristic Design** AAAI, 2026. [paper](https://arxiv.org/abs/2508.03082), [code](https://github.com/FeiLiu36/EoH-S)

    *Fei Liu, Yilu Liu, Qingfu Zhang, Xialiang Tong, Mingxuan Yuan*

94. **G-LNS: Generative Large Neighborhood Search for LLM-Based Automatic Heuristic Design** Arxiv, 2026. [paper](https://arxiv.org/abs/2602.08253), [code](https://github.com/ZBoyn/G-LNS)

    *Baoyun Zhao, He Wang, Liang Zeng*

95. **Beyond Simple Graphs: Neural Multi-Objective Routing on Multigraphs** ICLR, 2026. [paper](https://arxiv.org/abs/2506.22095), [code](https://github.com/filiprydin/GMS)

    *Filip Rydin, Attila Lischka, Jiaming Wu, Morteza Haghir Chehreghani, Balazs Kulcsar*

96. **⭐MaskCO: Masked Generation Drives Effective Representation Learning and Exploiting for Combinatorial Optimization** ICLR, 2026. [paper](https://openreview.net/forum?id=psUjNnLhl9), [code](https://github.com/Thinklab-SJTU/MaskCO)

    *Lvda Chen, Yang Li, Junchi Yan*

97. **Towards Efficient Constraint Handling in Neural Solvers for Routing Problems** ICLR, 2026. [paper](https://openreview.net/forum?id=raDFGuQxvD), [code](https://github.com/jieyibi/CaR-constraint)

    *Jieyi Bi, Zhiguang Cao, Jianan Zhou, Wen Song, Yaoxin Wu, Jie Zhang, Yining Ma, Cathy Wu*

98. **⭐Native Adaptive Solution Expansion for Diffusion-based Combinatorial Optimization** ICLR, 2026. [paper](https://openreview.net/forum?id=084SvT55yk)

    *Yu Wang, Yang Li, Jiale Ma, Junchi Yan, Yi Chang*

99. **ViTSP: A Vision Language Models Guided Framework for Solving Large-Scale Traveling Salesman Problems** ICLR, 2026. [paper](https://arxiv.org/abs/2509.23465), [code](https://github.itap.purdue.edu/uSMART/ViTSP_ICLR2026)

    *Zhuoli Yin, Yi Ding, Reem Khir, Hua Cai*

100. **FrontierCO: Real-World and Large-Scale Evaluation of Machine Learning Solvers for Combinatorial Optimization** ICLR, 2026. [paper](https://openreview.net/forum?id=BVprkacwFY), [code](https://github.com/sunnweiwei/FrontierCO)

    *Shengyu Feng, Weiwei Sun, Shanda Li, Ameet Talwalkar, Yiming Yang*

101. **Beyond the Heatmap: A Rigorous Evaluation of Component Impact in MCTS-Based TSP Solvers** ICLR, 2026. [paper](https://openreview.net/forum?id=H6PLJnnK6e), [code](https://github.com/LOGO-CUHKSZ/beyond-heatmap-mcts-tsp)

    *Xuanhao Pan, Chenguang Wang, Chaolong Ying, Ye XUE, Tianshu Yu*

102. **LINC: Decoupling Local Consequence Scoring from Hidden Matching in Constructive Neural Routing** NeurIPS, 2026. [paper](https://arxiv.org/abs/2605.06332), [code](https://github.com/Elaina10172004/LINC)

    *Shaofeng Qin, Li Wang*

### [Job Shop Scheduling Problem](#content)

1. **Smart Manufacturing Scheduling With Edge Computing Using Multiclass Deep Q Network** Transactions on Industrial Informatics, 2019. [journal](https://ieeexplore.ieee.org/document/8676376)

    *Chun-Cheng Lin, Der-Jiunn Deng, Yen-Ling Chih, Hsin-Ting Chiu*

2. **Multi-Agent Reinforcement Learning for Job Shop Scheduling in Flexible Manufacturing Systems** International Conference on Artificial Intelligence for Industries (AI4I), 2019. [paper](https://ieeexplore.ieee.org/document/9027776)

    *Schirin Baer, Jupiter Bakakeu, Richard Meyes, Tobias Meisen*

3. **Learning to Dispatch for Job Shop Scheduling via Deep Reinforcement Learning.** NeurIPS, 2020. [paper](https://arxiv.org/abs/2010.12367), [code](https://github.com/zcajiayin/L2D)

    *Cong Zhang, Wen Song, Zhiguang Cao, Jie Zhang, Puay Siew Tan, Chi Xu*

4. **ScheduleNet: Learn to Solve Multi-agent Scheduling Problems with Reinforcement Learning** Arxiv, 2021. [paper](https://arxiv.org/abs/2106.03051)

    *Junyoung Park, Sanjar Bakhtiyar, Jinkyoo Park*

5. **Dynamic job-shop scheduling in smart manufacturing using deep reinforcement learning** Computer Networks, 2021. [journal](https://www.sciencedirect.com/science/article/pii/S1389128621001031)

    *Libing Wang, Xin Hu, Yin Wang, Sujie Xu, Shijun Ma, Kexin Yang, Zhijun Liu, Weidong Wang*

6. **Learning to schedule job-shop problems: Representation and policy learning using graph neural network and reinforcement learning.** International Journal of Production Research, 2021. [journal](https://arxiv.org/abs/2106.01086)

    *Junyoung Park, Jaehyeong Chun, Sang Hun Kim, Youngkook Kim, Jinkyoo Park*

7. **Explainable reinforcement learning in production control of job shop manufacturing system.** International Journal of Production Research, 2021. [journal](https://www.tandfonline.com/doi/abs/10.1080/00207543.2021.1972179?journalCode=tprs20)

    *Andreas Kuhnle, Marvin Carl May, Louis Sch?fer, Gisela Lanza*

8. **DeepACO: Neural-enhanced Ant Systems for Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=cd5D1DD923), [code](https://github.com/henry-yeh/DeepACO)

    *Haoran Ye, Jiarui Wang, Zhiguang Cao, Helan Liang, Yong Li*

9. **Winner Takes It All: Training Performant RL Populations for Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=v6VpqGcGAR)

    *Nathan Grinsztajn, Daniel Furelos-Blanco, Shikha Surana, Cl{\'e}ment Bonnet, Thomas D Barrett*

10. **Combinatorial Optimization with Policy Adaptation using Latent Space Search** NeurIPS, 2023. [paper](https://openreview.net/forum?id=vpMBqdt9Hl)

    *Felix Chalumeau, Shikha Surana, Cl{\'e}ment Bonnet, Nathan Grinsztajn, Arnu Pretorius, Alexandre Laterre, Thomas D Barrett*

11. **Neural DAG Scheduling via One-Shot Priority Sampling** ICLR, 2023. [paper](https://openreview.net/forum?id=WL8FlAugqQ)

    *Wonseok Jeon, Mukul Gagrani, Burak Bartan, Weiliang Will Zeng, Harris Teague, Piero Zappi, Christopher Lott*

12. **Robust Scheduling with GFlowNets** ICLR, 2023. [paper](https://openreview.net/forum?id=ZBUthI6wK9h)

    *David W Zhang, Corrado Rainone, Markus Peschl, Roberto Bondesan*

13. **Continual Task Allocation in Meta-Policy Network via Sparse Prompting** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/24080)

    *Yijun, Tianyi Zhou, Jing Jiang, Guodong Long Yang, Yuhui Shi.*

14. **Applicability of Neural Combinatorial Optimization: A Critical View** TELO, 2024. [journal](https://dl.acm.org/doi/pdf/10.1145/3647644), [code](https://github.com/TheLeprechaun25/Applicability-NCO)

    *Andoni I. Garmendia, Josu Ceberio, Alexander Mendiburu*

15. **Large Language Models as End-to-end Combinatorial Optimization Solvers** NeurIPS, 2025. [paper](https://neurips.cc/virtual/2025/loc/san-diego/poster/115835), [code](https://github.com/Summer142857/LLMCoSolver)

    *Xia Jiang, Yaoxin Wu, Minshuo Li, Zhiguang Cao, Yingqian Zhang*

16. **BOPO: Neural Combinatorial Optimization via Best-anchored and Objective-guided Preference Optimization** ICML, 2025. [paper](https://openreview.net/forum?id=FLy6yXdrlW), [code](https://github.com/L-Z-7/BOPO)

    *Zijun Liao, Jinbiao Chen, Debing Wang, Zizhen Zhang, Jiahai Wang*

17. **Multi-Action Self-Improvement for Neural Combinatorial Optimization** ICLR, 2026. [paper](https://arxiv.org/abs/2510.12273), [code](https://github.com/LTluttmann/macsim)

    *Laurin Luttmann, Lin Xie*

18. **ReSched: Rethinking Flexible Job Shop Scheduling from a Transformer-based Architecture with Simplified States** ICLR, 2026. [paper](https://iclr.cc/virtual/2026/poster/10007089), [code](https://github.com/XiangjieXiao/ReSched)

    *Xiangjie Xiao, Zhiguang Cao, Cong Zhang, Wen Song*

19. **Neural Multi-Objective Combinatorial Optimization for Flexible Job Shop Scheduling Problems** ICLR, 2026. [paper](https://openreview.net/forum?id=YAgOaYedLQ)

    *Igor G. Smit, Yaoxin Wu, Pavel Troubil, Yingqian Zhang, Wim P.M. Nuijten*

### [Flow Shop Problem](#content)

1. **Preference Optimization for Combinatorial Optimization Problems** ICML, 2025. [paper](https://openreview.net/forum?id=Jwe5FJ8QGx), [code](https://github.com/MingjunPan/Preference-Optimization-for-Combinatorial-Optimization-Problems)

    *Mingjun Pan, Guanquan Lin, You-Wei Luo, Bin Zhu, Zhien Dai, Lijun Sun, Chun Yuan*

2. **PARCO: Parallel AutoRegressive Models for Multi-Agent Combinatorial Optimization** NeurIPS, 2025. [paper](https://openreview.net/forum?id=9F2Cmgo17M), [code](https://github.com/ai4co/parco)

    *Federico Berto, Chuanbo Hua, Laurin Luttmann, Jiwoo Son, Junyoung Park, Kyuree Ahn, Changhyun Kwon, Lin Xie, Jinkyoo Park*

3. **Multi-Action Self-Improvement for Neural Combinatorial Optimization** ICLR, 2026. [paper](https://arxiv.org/abs/2510.12273), [code](https://github.com/LTluttmann/macsim)

    *Laurin Luttmann, Lin Xie*

### [Sorting & Ranking](#content)

1. **Ranking via sinkhorn propagation** Arxiv, 2011. [paper](https://arxiv.org/abs/1106.1925#)

    *Ryan Prescott Adams, Richard S. Zemel*

2. **Predict+optimise with ranking objectives: exhaustively learning linear functions** IJCAI, 2019. [paper](https://dl.acm.org/doi/abs/10.5555/3367032.3367186)

    *Emir Demirovic, Peter J. Stuckey, James Bailey, Jeffrey Chan, Christopher Leckie, Kotagiri Ramamohanarao, Tias Guns*

3. **Stochastic Optimization of Sorting Networks via Continuous Relaxations** ICLR, 2019. [paper](https://openreview.net/forum?id=H1eSS3CcKX), [code](https://github.com/ermongroup/neuralsort)

    *Aditya Grover, Eric Wang, Aaron Zweig, Stefano Ermon*

4. **Differentiable Ranking and Sorting using Optimal Transport** NeurIPS, 2019. [paper](https://papers.nips.cc/paper/2019/hash/d8c24ca8f23c562a5600876ca2a550ce-Abstract.html)

    *Marco Cuturi, Olivier Teboul, Jean-Philippe Vert*

5. **Optimizing Rank-Based Metrics With Blackbox Differentiation** CVPR, 2020. [paper](https://openaccess.thecvf.com/content_CVPR_2020/papers/Rolinek_Optimizing_Rank-Based_Metrics_With_Blackbox_Differentiation_CVPR_2020_paper.pdf), [code](https://github.com/martius-lab/blackbox-backprop)

    *Marin Vlastelica, Anselm Paulus, Vít Musil, Georg Martius, Michal Rolínek*

6. **Fast Differentiable Sorting and Ranking** ICML, 2020. [paper](http://proceedings.mlr.press/v119/blondel20a/blondel20a.pdf), [code](https://github.com/google-research/fast-soft-sort/)

    *Mathieu Blondel Olivier Teboul Quentin Berthet Josip Djolonga*

7. **SoftSort: A Continuous Relaxation for the argsort Operator** ICML, 2020. [paper](http://proceedings.mlr.press/v119/prillo20a/prillo20a.pdf), [code](https://github.com/sprillo/softsort)

    *Sebastian Prillo, Julian Martin Eisenschlos*

8. **differentiable top k with optimal transport** NeurIPS, 2020. [paper](https://proceedings.neurips.cc/paper/2020/hash/ec24a54d62ce57ba93a531b460fa8d18-Abstract.html)

    *Yujia Xie, Hanjun Dai, Minshuo Chen, Bo Dai, Tuo Zhao, Hongyuan Zha, Wei Wei, Tomas Pfister*

9. **Automatic Loss Function Search for Predict-Then-Optimize Problems with Strong Ranking Property** ICLR, 2022. [paper](https://openreview.net/forum?id=hSktDu-h94), [code](https://github.com/Microsoft/AutoPredOptConnector)

    *Boshi Wang, Jialin Yi, Hang Dong, Bo Qiao, Chuan Luo, Qingwei Lin*

10. **Decision-Focused Learning: Through the Lens of Learning to Rank** ICML, 2022. [paper](https://proceedings.mlr.press/v162/mandi22a.html), [code](https://github.com/jayman91/ltr-predopt)

    *Jayanta Mandi, Vı́ctor Bucarey, Maxime Mulamba Ke Tchomba, Tias Guns*

11. **PiRank-Scalable Learning To Rank via Differentiable Sorting** NeurIPS, 2022. [paper](https://openreview.net/forum?id=dL8p6rLFTS3), [code](https://github.com/ermongroup/pirank)

    *Robin Marcel Edwin Swezey, Aditya Grover, Bruno Charron, Stefano Ermon*

12. **Neural Improvement Heuristics for Graph Combinatorial Optimization Problems** TNNLS, 2023. [journal](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10271315&casa_token=Hqn_wH2HAjEAAAAA:rTd6KVaoKVjrFWASa-Ma0vC6CBvsmMUHnoWik2DyD56NbnfNOqBG5qZTBLR5hqf9vpCotivB_BU&tag=1), [code](https://github.com/TheLeprechaun25/neural-improvement-heuristics)

    *Andoni I. Garmendia, Josu Ceberio, Alexander Mendiburu*

13. **Applicability of Neural Combinatorial Optimization: A Critical View** TELO, 2024. [journal](https://dl.acm.org/doi/pdf/10.1145/3647644), [code](https://github.com/TheLeprechaun25/Applicability-NCO)

    *Andoni I. Garmendia, Josu Ceberio, Alexander Mendiburu*

### [Graph Matching](#content)

1. **Revised Note on Learning Algorithms for Quadratic Assignment with Graph Neural Networks** Arxiv, 2017. [paper](https://arxiv.org/pdf/1706.07450.pdf), [code](https://github.com/alexnowakvila/QAP_pt)

    *Alex Nowak, Soledad Villar, S. Afonso Bandeira, Joan Bruna*

2. **Deep Learning of Graph Matching.** CVPR, 2018. [paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Zanfir_Deep_Learning_of_CVPR_2018_paper.html)

    *Andrei Zanfir, Cristian Sminchisescu*

3. **⭐Learning Combinatorial Embedding Networks for Deep Graph Matching.** ICCV, 2019. [paper](http://openaccess.thecvf.com/content_ICCV_2019/papers/Wang_Learning_Combinatorial_Embedding_Networks_for_Deep_Graph_Matching_ICCV_2019_paper.pdf), [code](https://github.com/Thinklab-SJTU/ThinkMatch)

    *Runzhong Wang, Junchi Yan, Xiaokang Yang*

4. **Deep Graphical Feature Learning for the Feature Matching Problem.** ICCV, 2019. [paper](https://openaccess.thecvf.com/content_ICCV_2019/papers/Zhang_Deep_Graphical_Feature_Learning_for_the_Feature_Matching_Problem_ICCV_2019_paper.pdf)

    *Zhen Zhang, Wee Sun Lee*

5. **GLMNet: Graph Learning-Matching Networks for Feature Matching.** Arxiv, 2019. [paper](https://arxiv.org/abs/1911.07681)

    *Bo Jiang, Pengfei Sun, Jin Tang, Bin Luo*

6. **⭐Learning deep graph matching with channel-independent embedding and Hungarian attention.** ICLR, 2020. [paper](https://openreview.net/forum?id=rJgBd2NYPH), [code](https://github.com/Thinklab-SJTU/ThinkMatch)

    *Tianshu Yu, Runzhong Wang, Junchi Yan, Baoxin Li*

7. **Deep Graph Matching Consensus.** ICLR, 2020. [paper](http://arxiv.org/abs/2001.09621)

    *Matthias Fey, Jan E. Lenssen, Christopher Morris, Jonathan Masci, Nils M. Kriege*

8. **⭐Graduated Assignment for Joint Multi-Graph Matching and Clustering with Application to Unsupervised Graph Matching Network Learning.** NeurIPS, 2020. [paper](https://papers.NeurIPS.cc/paper/2020/file/e6384711491713d29bc63fc5eeb5ba4f-Paper.pdf), [code](https://github.com/Thinklab-SJTU/ThinkMatch)

    *Runzhong Wang, Junchi Yan, Xiaokang Yang*

9. **⭐Combinatorial Learning of Robust Deep Graph Matching: An Embedding Based Approach.** TPAMI, 2020. [paper](https://doi.org/10.1109/TPAMI.2020.3005590), [code](https://github.com/Thinklab-SJTU/ThinkMatch)

    *Runzhong Wang, Junchi Yan, Xiaokang Yang*

10. **Deep Graph Matching via Blackbox Differentiation of Combinatorial Solvers.** ECCV, 2020. [paper](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123730409.pdf), [code](https://github.com/martius-lab/blackbox-deep-graph-matching)

    *Michal Rolinek, Paul Swoboda, Dominik Zietlow, Anselm Paulus, Vit Musil, Georg Martius*

11. **⭐Neural Graph Matching Network: Learning Lawler's Quadratic Assignment Problem with Extension to Hypergraph and Multiple-graph Matching.** TPAMI, 2021. [paper](https://arxiv.org/abs/1911.11308), [code](https://github.com/Thinklab-SJTU/ThinkMatch)

    *Runzhong Wang, Junchi Yan, Xiaokang Yang*

12. **⭐Deep Latent Graph Matching** ICML, 2021. [paper](http://proceedings.mlr.press/v139/yu21d/yu21d.pdf)

    *Tianshu Yu, Runzhong Wang, Junchi Yan, Baoxin Li*

13. **IA-GM: A Deep Bidirectional Learning Method for Graph Matching** AAAI, 2021. [paper](https://ojs.aaai.org/index.php/AAAI/article/view/16461/16268)

    *Kaixuan Zhao, Shikui Tu, Lei Xu*

14. **Deep Graph Matching under Quadratic Constraint** CVPR, 2021. [paper](https://openaccess.thecvf.com/content/CVPR2021/papers/Gao_Deep_Graph_Matching_Under_Quadratic_Constraint_CVPR_2021_paper.pdf)

    *Quankai Gao, Fudong Wang, Nan Xue, Jin-Gang Yu, Gui-Song Xia*

15. **GAMnet: Robust Feature Matching via Graph Adversarial-Matching Network** MM, 2021. [paper](https://dl.acm.org/doi/pdf/10.1145/3474085.3475669)

    *Bo Jiang, Pengfei Sun, Ziyan Zhang, Jin Tang, Bin Luo*

16. **Hypergraph Neural Networks for Hypergraph Matching** ICCV, 2021. [paper](https://openaccess.thecvf.com/content/ICCV2021/papers/Liao_Hypergraph_Neural_Networks_for_Hypergraph_Matching_ICCV_2021_paper.pdf)

    *Xiaowei Liao, Yong Xu, Haibin Ling*

17. **Learning to Match Features with Seeded Graph Matching Network** ICCV, 2021. [paper](https://openaccess.thecvf.com/content/ICCV2021/html/Chen_Learning_To_Match_Features_With_Seeded_Graph_Matching_Network_ICCV_2021_paper.html)

    *Hongkai Chen, Zixin Luo, Jiahui Zhang, Lei Zhou, Xuyang Bai, Zeyu Hu, Chiew-Lan Tai, Long Quan*

18. **⭐Appearance and Structure Aware Robust Deep Visual Graph Matching: Attack, Defense and Beyond** CVPR, 2022. [paper](https://openaccess.thecvf.com/content/CVPR2022/papers/Ren_Appearance_and_Structure_Aware_Robust_Deep_Visual_Graph_Matching_Attack_CVPR_2022_paper.pdf), [code](https://github.com/Thinklab-SJTU/RobustMatch)

    *Qibing Ren, Qingquan Bao, Runzhong Wang, Junchi Yan*

19. **⭐Self-supervised Learning of Visual Graph Matching** ECCV, 2022. [paper](https://link.springer.com/chapter/10.1007/978-3-031-20050-2_22), [code](https://github.com/Thinklab-SJTU/ThinkMatch-SCGM)

    *Chang Liu, Shaofeng Zhang, Xiaokang Yang, Junchi Yan*

20. **⭐Revocable Deep Reinforcement Learning with Affinity Regularization for Outlier-Robust Graph Matching.** ICLR, 2023. [paper](https://openreview.net/forum?id=QjQibO3scV_), [code](https://github.com/Thinklab-SJTU/RGM)

    *Chang Liu, Zetian Jiang, Runzhong Wang, Junchi Yan, Lingxiao Huang, Pinyan Lu*

21. **SeedGNN: Graph Neural Network for Supervised Seeded Graph Matching** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/24282)

    *Liren Yu, Jiaming Xu, Xiaojun Lin*

22. **D2Match: Leveraging Deep Learning and Degeneracy for Subgraph Matching** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/24358)

    *Xuan Liu, Lin Zhang, Jiaqi Sun, Yujiu Yang, Haiqing Yang*

23. **⭐LinSATNet: The Positive Linear Satisfiability Neural Networks** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/25110), [code](https://github.com/Thinklab-SJTU/LinSATNet)

    *Runzhong Wang, Yunhao Zhang, Ziao Guo, Tianyi Chen, Xiaokang Yang, Junchi Yan*

24. **LVM-Med: Learning Large-Scale Self-Supervised Vision Models for Medical Imaging via Second-order Graph Matching** NeurIPS, 2023. [paper](https://openreview.net/forum?id=xE7oH5iVGK), [code](https://github.com/duyhominhnguyen/LVM-Med)

    *Duy MH Nguyen, Hoang Nguyen, Nghiem T Diep, Tan N Pham, Tri Cao, Binh T Nguyen, Paul Swoboda, Nhat Ho, Shadi Albarqouni, Pengtao Xie, others*

25. **Improving Graph Matching with Positional Reconstruction Encoder-Decoder Network** NeurIPS, 2023. [paper](https://openreview.net/forum?id=28RTu9MOT6)

    *Yixiao Zhou, Ruiqi Jia, Hongxiang Lin, Hefeng Quan, Yumeng Zhao, Xiaoqing Lyu*

26. **Learning to Prune Instances of Steiner Tree Problem in Grap** INOC, 2024. [paper](https://openproceedings.org/2024/conf/inoc/INOC_31.pdf), [code](https://github.com/dajwani/alenex22)

    *Jiwei Zhang, Dena Tayebi, Saurabh Ray, Deepak Ajwani*

### [Quadratic Assignment Problem](#content)

1. **Revised Note on Learning Algorithms for Quadratic Assignment with Graph Neural Networks** Arxiv, 2017. [paper](https://arxiv.org/pdf/1706.07450.pdf), [code](https://github.com/alexnowakvila/QAP_pt)

    *Alex Nowak, Soledad Villar, S. Afonso Bandeira, Joan Bruna*

2. **⭐Neural Graph Matching Network: Learning Lawler's Quadratic Assignment Problem with Extension to Hypergraph and Multiple-graph Matching.** TPAMI, 2021. [paper](https://arxiv.org/abs/1911.11308), [code](https://github.com/Thinklab-SJTU/ThinkMatch)

    *Runzhong Wang, Junchi Yan, Xiaokang Yang*

3. **⭐Revocable Deep Reinforcement Learning with Affinity Regularization for Outlier-Robust Graph Matching.** ICLR, 2023. [paper](https://openreview.net/forum?id=QjQibO3scV_), [code](https://github.com/Thinklab-SJTU/RGM)

    *Chang Liu, Zetian Jiang, Runzhong Wang, Junchi Yan, Lingxiao Huang, Pinyan Lu*

4. **⭐Towards Quantum Machine Learning for Constrained Combinatorial Optimization: a Quantum QAP Solver** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/24148)

    *Xinyu Ye, Ge Yan, Junchi Yan*

5. **Differentiable extensions with rounding guarantees for combinatorial optimization over permutations** NeurIPS, 2025. [paper](https://openreview.net/forum?id=aAxk0cw6GW)

    *Robert R Nerem, Zhishang Luo, Akbar Rafiey, Yusu Wang*

### [Portfolio Optimization](#content)

1. **⭐LinSATNet: The Positive Linear Satisfiability Neural Networks** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/25110), [code](https://github.com/Thinklab-SJTU/LinSATNet)

    *Runzhong Wang, Yunhao Zhang, Ziao Guo, Tianyi Chen, Xiaokang Yang, Junchi Yan*

2. **Integrating prediction in mean-variance portfolio optimization** Quantitative Finance, 2023. [paper](https://arxiv.org/pdf/2102.09287.pdf)

    *Andrew Butler, Roy H Kwon*

3. **⭐Towards One-shot Neural Combinatorial Solvers: Theoretical and Empirical Notes on the Cardinality-Constrained Case** ICLR, 2023. [paper](https://openreview.net/forum?id=h21yJhdzbwz), [code](https://github.com/Thinklab-SJTU/One-Shot-Cardinality-NN-Solver)

    *Runzhong Wang, Li Shen, Yiting Chen, Junchi Yan, Xiaokang Yang, Dacheng Tao*

### [Maximal Cut](#content)

1. **Learning Combinatorial Optimization Algorithms over Graphs.** NeurIPS, 2017. [paper](https://arxiv.org/abs/1704.01665)

    *Hanjun Dai, Elias B Khalil, Yuyu Zhang, Bistra Dilkina, Le Song*

2. **Exploratory Combinatorial Optimization with Reinforcement Learning.** AAAI, 2020. [paper](https://ojs.aaai.org/index.php/AAAI/article/view/5723)

    *Thomas LBarrett, William Clements, Jakob Foerster, Alex Lvovsky*

3. **Erdos Goes Neural: an Unsupervised Learning Framework for Combinatorial Optimization on Graphs.** NeurIPS, 2020. [paper](https://static.aminer.cn/upload/pdf/575/1127/1864/5eede0b791e0116a23aafe7b_1.pdf)

    *Nikolaos Karalias, Andreas Loukas*

4. **Reversible Action Design for Combinatorial Optimization with Reinforcement Learning** Arxiv, 2021. [paper](https://arxiv.org/abs/2102.07210)

    *Fan Yao, Renqin Cai, Hongning Wang*

5. **LeNSE: Learning To Navigate Subgraph Embeddings for Large-Scale Combinatorial Optimisation** ICML, 2022. [paper](https://proceedings.mlr.press/v162/ireland22a.html), [code](https://github.com/davidireland3/LeNSE)

    *David Ireland, G. Montana*

6. **Learning to Solve Combinatorial Graph Partitioning Problems via Efficient Exploration** Arxiv, 2022. [paper](https://arxiv.org/abs/2205.14105), [code](https://github.com/tomdbar/ecord)

    *Thomas D Barrett, Christopher WF Parsonson, Alexandre Laterre*

7. **Revisiting Sampling for Combinatorial Optimization** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/23661)

    *Haoran, Goshvadi Katayoon, Nova Azade, Schuurmans Dale Sun, Dai Hanjun.*

8. **Optimizing Solution-Samplers for Combinatorial Problems: The Landscape of Policy-Gradient Methods** NeurIPS, 2023. [paper](https://openreview.net/forum?id=mmTy1iyU5G), [code](https://openreview.net/attachment?id=mmTy1iyU5G&name=supplementary_material)

    *Constantine Caramanis, Dimitris Fotakis, Alkis Kalavasis, Vasilis Kontonis, Christos Tzamos*

9. **Neural Improvement Heuristics for Graph Combinatorial Optimization Problems** TNNLS, 2023. [journal](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=10271315&casa_token=Hqn_wH2HAjEAAAAA:rTd6KVaoKVjrFWASa-Ma0vC6CBvsmMUHnoWik2DyD56NbnfNOqBG5qZTBLR5hqf9vpCotivB_BU&tag=1), [code](https://github.com/TheLeprechaun25/neural-improvement-heuristics)

    *Andoni I. Garmendia, Josu Ceberio, Alexander Mendiburu*

10. **Let the Flows Tell: Solving Graph Combinatorial Optimization Problems with GFlowNets** NeurlPS, 2023. [paper](https://arxiv.org/abs/2305.17010), [code](https://github.com/zdhNarsil/GFlowNet-CombOpt)

    *Dinghuai Zhang, Hanjun Dai, Nikolay Malkin, Aaron Courville, Yoshua Bengio, Ling Pan*

11. **Variational Annealing on Graphs for Combinatorial Optimization** NeurlPS, 2023. [paper](https://openreview.net/forum?id=SLx7paoaTU), [code](https://github.com/ml-jku/VAG-CO)

    *Sebastian Sanokowski, Wilhelm Franz Berghammer, Sepp Hochreiter, Sebastian Lehner*

12. **DISCS: A Benchmark for Discrete Sampling** NeurlPS, 2023. [paper](https://openreview.net/forum?id=oi1MUMk5NF), [code](https://github.com/google-research/discs)

    *Katayoon Goshvadi, Haoran Sun, Xingchao Liu, Azade Nova, Ruqi Zhang, Will Sussman Grathwohl, Dale Schuurmans, Hanjun Dai*

13. **MARCO: A Memory-Augmented Reinforcement Framework for Combinatorial Optimization** IJCAI, 2024. [paper](https://www.ijcai.org/proceedings/2024/0766.pdf), [code](https://github.com/TheLeprechaun25/MARCO)

    *Andoni I. Garmendia, Quentin Cappart, Josu Ceberio, Alexander Mendiburu*

14. **Controlling Continuous Relaxation for Combinatorial Optimization** NeurlPS, 2024. [paper](https://openreview.net/pdf?id=ykACV1IhjD)

    *Yuma Ichikawa*

15. **Distributed Constrained Combinatorial Optimization leveraging Hypergraph Neural Networks** Nature Machine Intelligence, 2024. [paper](https://arxiv.org/abs/2311.09375), [code](https://github.com/nasheydari/HypOp)

    *Nasimeh Heydaribeni, Xinrui Zhan, Ruisi Zhang, Tina Eliassi-Rad, Farinaz Koushanfar*

16. **Efficient Combinatorial Optimization via Heat Diffusion** NeurIPS, 2024. [paper](https://openreview.net/forum?id=psDrko9v1D), [code](https://github.com/AwakerMhy/HeO)

    *Hengyuan Ma, Wenlian Lu, Jianfeng Feng*

17. **A Diffusion Model Framework for Unsupervised Neural Combinatorial Optimization** ICML, 2024. [paper](https://arxiv.org/abs/2406.01661), [code](https://github.com/ml-jku/DIffUCO)

    *Sebastian Sanokowski, Sepp Hochreiter, Sebastian Lehner*

18. **⭐ML4CO-Bench-101: Benchmark Machine Learning for Classic Combinatorial Problems on Graphs** NeurIPS, 2025. [paper](https://openreview.net/forum?id=ye4ntB1Kzi), [code](https://github.com/Thinklab-SJTU/ML4CO-Bench-101)

    *Jiale Ma, Wenzheng Pan, Yang Li, Junchi Yan*

19. **⭐COExpander: Adaptive Solution Expansion for Combinatorial Optimization** ICML, 2025. [paper](https://openreview.net/forum?id=KMaBXMWsBM), [code](https://github.com/Thinklab-SJTU/COExpander)

    *Jiale Ma, Wenzheng Pan, Yang Li, Junchi Yan*

20. **Scalable Discrete Diffusion Samplers: Combinatorial Optimization and Statistical Physics** ICLR, 2025. [paper](https://openreview.net/pdf?id=peNgxpbdxB)

    *Sebastian Sanokowski, Wilhelm Franz Berghammer, Haoyu Peter Wang, Martin Ennemoser, Sepp Hochreiter, Sebastian Lehner*

21. **Learning to Explore and Exploit with GNNs for Unsupervised Combinatorial Optimization** ICLR, 2025. [paper](https://openreview.net/forum?id=vaJ4FObpXN), [code](https://github.com/utkuumur/X2GNN)

    *Utku Umur Acikalin, Aaron M. Ferber, Carla P. Gomes*

22. **Optimization by Parallel Quasi-Quantum Annealing with Gradient-Based Sampling** ICLR, 2025. [paper](https://openreview.net/forum?id=9EfBeXaXf0), [code](https://github.com/Yuma-Ichikawa/QQA4CO)

    *Yuma Ichikawa, Yamato Arai*

23. **Regularized Langevin Dynamics for Combinatorial Optimization** ICML, 2025. [paper](https://openreview.net/forum?id=bbJ0QCujU4), [code](https://github.com/Shengyu-Feng/RLD4CO)

    *Shengyu Feng, Yiming Yang*

24. **Projecting Latent RL Actions: Towards Generalizable and Scalable Graph Combinatorial Optimization** Arxiv, 2026. [paper](https://arxiv.org/abs/2605.19721), [code](https://github.com/terranovafr/LaGCO-RL)

    *Franco Terranova, Guillermo Bernardez, Albert Cabellos-Aparicio, Nina Miolane, Abdelkader Lahmadi*

### [Vehicle Routing Problem](#content)

1. **Learning to Perform Local Rewriting for Combinatorial Optimization.** NeurIPS, 2019. [paper](https://arxiv.org/abs/1810.00337), [code](https://github.com/facebookresearch/neural-rewriter)

    *Xinyun Chen, Yuandong Tian*

2. **Deep Reinforcement Learning for the Electric Vehicle Routing Problem with Time Windows.** Arxiv, 2020. [paper](https://arxiv.org/abs/2010.02068)

    *Bo Lin, Bissan Ghaddar, Jatin Nathwani*

3. **Efficiently Solving the Practical,Vehicle Routing Problem: A Novel Joint Learning Approach.** KDD, 2020. [paper](https://www.kdd.org/kdd2020/accepted-papers/view/efficiently-solving-the-practical-vehicle-routing-problem-a-novel-joint-lea)

    *Lu Duan, Yang Zhan, Haoyuan Hu, Yu Gong, Jiangwen Wei, Xiaodong Zhang, Yinghui Xu*

4. **Reinforcement Learning with Combinatorial Actions: An Application to Vehicle Routing** NeurIPS, 2020. [paper](https://papers.nips.cc/paper/2020/file/06a9d51e04213572ef0720dd27a84792-Paper.pdf), [code](https://github.com/google-research/tf-opt)

    *Arthur Delarue, Ross Anderson, Christian Tjandraatmadja*

5. **A Learning-based Iterative Method for Solving Vehicle Routing Problems** ICLR, 2020. [paper](https://static.aminer.cn/upload/pdf/program/5e5e18dd93d709897ce3720b_0.pdf)

    *Hao Lu, Xingwen Zhang, Shuang Yang*

6. **Neural Large Neighborhood Search for the Capacitated Vehicle Routing Problem** Arxiv, 2020. [paper](https://arxiv.org/abs/1911.09539)

    *Andre Hottung, Kevin Tierney*

7. **Learning Improvement Heuristics for Solving Routing Problems** TNNLS, 2021. [journal](https://ieeexplore.ieee.org/abstract/document/9393606?casa_token=mFeyLmrOGfIAAAAA:nmAkjUaTSooYurWHuWGYNoguV453anw9Enyv45xG5jb2oCps6QE4A1CFe1EmFmTzbON6cL5maw)

    *Yaoxin Wu, Wen Song, Zhiguang Cao, Jie Zhang, Andrew Lim*

8. **Reinforcement Learning for Route Optimization with Robustness Guarantees** IJCAI, 2021. [paper](https://www.ijcai.org/proceedings/2021/0357.pdf)

    *Tobias Jacobs, Francesco Alesiani, Gulcin Ermis*

9. **Multi-Decoder Attention Model with Embedding Glimpse for Solving Vehicle Routing Problems.** AAAI, 2021. [paper](https://arxiv.org/abs/2012.10638), [code](https://github.com/liangxinedu/MDAM)

    *Liang Xin, Wen Song, Zhiguang Cao, Jie Zhang*

10. **Analytics and Machine Learning in Vehicle Routing Research** Arxiv, 2021. [paper](https://arxiv.org/abs/2102.10012)

    *Ruibin Bai, Xinan Chen, Zhi-Long Chen, Tianxiang Cui, Shuhui Gong, Wentao He, Xiaoping Jiang, Huan Jin, Jiahuan Jin, Graham Kendall, others*

11. **RP-DQN: An application of Q-Learning to Vehicle Routing Problems** Arxiv, 2021. [paper](https://arxiv.org/abs/2104.12226)

    *Ahmad Bdeir, Simon Boeder, Tim Dernedde, Kirill Tkachuk, Jonas K Falkner, Lars Schmidt-Thieme*

12. **Deep Policy Dynamic Programming for Vehicle Routing Problems** Arxiv, 2021. [paper](https://arxiv.org/abs/2102.11756)

    *Wouter Kool, Herke van Hoof, Joaquim Gromicho, Max Welling*

13. **Learning to Delegate for Large-scale Vehicle Routing** NeurIPS, 2021. [paper](https://proceedings.neurips.cc/paper/2021/hash/dc9fa5f217a1e57b8a6adeb065560b38-Abstract.html)

    *Sirui Li, Zhongxia Yan, Cathy Wu*

14. **Learning a Latent Search Space for Routing Problems using Variational Autoencoders** ICLR, 2021. [paper](https://openreview.net/forum?id=90JprVrJBO)

    *Andre Hottung, Bhanu Bhandari, Kevin Tierney*

15. **Preference Conditioned Neural Multi-objective Combinatorial Optimization** ICLR, 2022. [paper](https://openreview.net/forum?id=QuObT9BTWo)

    *Xi Lin, Zhiyuan Yang, Qingfu Zhang*

16. **Learning Generalizable Models for Vehicle Routing Problems via Knowledge Distillation** NeurIPS, 2022. [paper](https://openreview.net/forum?id=sOVNpUEgKMp), [code](https://github.com/jieyibi/AMDKD)

    *Jieyi Bi, Yining Ma, Jiahai Wang, Zhiguang Cao, Jinbiao Chen, Yuan Sun, Yeow Meng Chee*

17. **Sym-NCO: Leveraging Symmetricity for Neural Combinatorial Optimization** NeurIPS, 2022. [paper](https://openreview.net/forum?id=kHrE2vi5Rvs), [code](https://github.com/alstn12088/Sym-NCO)

    *Minsu Kim, Junyoung Park, Jinkyoo Park*

18. **Simulation-guided Beam Search for Neural Combinatorial Optimization** NeurIPS, 2022. [paper](https://openreview.net/forum?id=tYAS1Rpys5), [code](https://github.com/yd-kwon/SGBS)

    *Jinho Choo, Yeong-Dae Kwon, Jihoon Kim, Jeongwoo Jae, Andr{\'e} Hottung, Kevin Tierney, Youngjune Gwon*

19. **Learning to CROSS exchange to solve min-max vehicle routing problems** ICLR, 2023. [paper](https://openreview.net/forum?id=ZcnzsHC10Y)

    *Minjun Kim, Junyoung Park, Jinkyoo Park*

20. **Generalize Learned Heuristics to Solve Large-scale Vehicle Routing Problems in Real-time** ICLR, 2023. [paper](https://openreview.net/forum?id=6ZajpxqTlQ)

    *Qingchun Hou, Jingwei Yang, Yiqiang Su, Xiaoqing Wang, Yuming Deng*

21. **Meta-SAGE: Scale Meta-Learning Scheduled Adaptation with Guided Exploration for Mitigating Scale Shift on Combinatorial Optimization** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/25138)

    *Jiwoo Son, Minsu Kim, Hyeonah Kim, Jinkyoo Park*

22. **Towards Omni-generalizable Neural Methods for Vehicle Routing Problems** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/25267), [code](https://github.com/RoyalSkye/Omni-VRP)

    *Zhou Jianan, Yaoxin Wu, Wen Song, Zhiguang Cao, Jie Zhang*

23. **DeepACO: Neural-enhanced Ant Systems for Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=cd5D1DD923), [code](https://github.com/henry-yeh/DeepACO)

    *Haoran Ye, Jiarui Wang, Zhiguang Cao, Helan Liang, Yong Li*

24. **Winner Takes It All: Training Performant RL Populations for Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=v6VpqGcGAR)

    *Nathan Grinsztajn, Daniel Furelos-Blanco, Shikha Surana, Cl{\'e}ment Bonnet, Thomas D Barrett*

25. **Combinatorial Optimization with Policy Adaptation using Latent Space Search** NeurIPS, 2023. [paper](https://openreview.net/forum?id=vpMBqdt9Hl)

    *Felix Chalumeau, Shikha Surana, Cl{\'e}ment Bonnet, Nathan Grinsztajn, Arnu Pretorius, Alexandre Laterre, Thomas D Barrett*

26. **Efficient Meta Neural Heuristic for Multi-Objective Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=593fc38lhN), [code](https://github.com/bill-cjb/EMNH)

    *Jinbiao Chen, Jiahai Wang, Zizhen Zhang, Zhiguang Cao, Te Ye, Siyuan Chen*

27. **BQ-NCO: Bisimulation Quotienting for Efficient Neural Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=BRqlkTDvvm), [code](https://github.com/naver/bq-nco)

    *Darko Drakulic, Sofia Michel, Florian Mai, Arnaud Sors, Jean-Marc Andreoli*

28. **Neural Combinatorial Optimization with Heavy Decoder: Toward Large Scale Generalization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=RBI4oAbdpm), [code](https://github.com/CIAM-Group/NCO_code/tree/main/single_objective/LEHD)

    *Fu Luo, Xi Lin, Fei Liu, Qingfu Zhang, Zhenkun Wang*

29. **Neural Multi-Objective Combinatorial Optimization with Diversity Enhancement** NeurIPS, 2023. [paper](https://openreview.net/forum?id=N4JkStI1fe), [code](https://github.com/bill-cjb/NHDE)

    *Jinbiao Chen, Zizhen Zhang, Zhiguang Cao, Yaoxin Wu, Yining Ma, Te Ye, Jiahai Wang*

30. **Ensemble-based Deep Reinforcement Learning for Vehicle Routing Problems under Distribution Shift** NeurIPS, 2023. [paper](https://openreview.net/forum?id=HoBbZ1vPAh)

    *Yuan Jiang, Zhiguang Cao, Yaoxin Wu, Wen Song, Jie Zhang*

31. **Learning to Search Feasible and Infeasible Regions of Routing Problems with Flexible Neural k-Opt** NeurIPS, 2023. [paper](https://openreview.net/forum?id=q1JukwH2yP), [code](https://github.com/yining043/NeuOpt)

    *Yining Ma, Zhiguang Cao, Yeow Meng Chee*

32. **Learning to Prune Electric Vehicle Routing Problems** LION, 2023. [paper](https://link.springer.com/chapter/10.1007/978-3-031-44505-7_26)

    *James Fitzpatrick, Deepak Ajwani, Paula Carroll*

33. **GLOP: Learning Global Partition and Local Construction for Solving Large-Scale Routing Problems in Real-Time** AAAI, 2024. [paper](https://arxiv.org/abs/2312.08224), [code](https://github.com/henry-yeh/GLOP)

    *Haoran Ye, Jiarui Wang, Helan Liang, Zhiguang Cao, Yong Li, Fanzhang Li*

34. **Distilling Autoregressive Models to Obtain High-Performance Non-autoregressive Solvers for Vehicle Routing Problems with Faster Inference Speed** AAAI, 2024. [paper](https://arxiv.org/abs/2312.12469), [code](https://github.com/xybFight/GNARKD)

    *Yubin Xiao, Di Wang, Boyang Li, Mingzhao Wang, Xuan Wu, Changliang Zhou, You Zhou*

35. **Neural Combinatorial Optimization for Robust Routing Problem with Uncertain Travel Times** NeurIPS, 2024. [paper](https://openreview.net/pdf?id=DoewNm2uT3)

    *Pei Xiao, Zizhen Zhang, Jinbiao Chen, Jiahai Wang, Zhenzhen Zhang*

36. **Collaboration! Towards Robust Neural Methods for Routing Problems** NeurIPS, 2024. [paper](https://openreview.net/forum?id=YfQA78gEFA), [code](https://github.com/RoyalSkye/Routing-CNF)

    *Jianan Zhou, Yaoxin Wu, Zhiguang Cao, Wen Song, Jie Zhang, Zhiqi Shen*

37. **UDC: A Unified Neural Divide-and-Conquer Framework for Large-Scale Combinatorial Optimization Problems** NeurIPS, 2024. [paper](https://openreview.net/pdf?id=dCgbyvmlwL), [code](https://github.com/CIAM-Group/NCO_code/tree/main/single_objective/UDC-Large-scale-CO-master)

    *Zhi Zheng, Changliang Zhou, Tong Xialiang, Mingxuan Yuan, Zhenkun Wang*

38. **A Scalable Learning Approach for the Capacitated Vehicle Routing Problem** Computers and Operations Research, 2024. [journal](https://dx.doi.org/10.1016/j.cor.2024.106787)

    *James Fitzpatrick, Deepak Ajwani, Paula Carroll*

39. **A Neural Column Generation Approach to the Vehicle Routing Problem with Two-Dimensional Loading and Last-In-First-Out Constraints** IJCAI, 2024. [paper](https://www.ijcai.org/proceedings/2024/0218.pdf), [code](https://github.com/xyfffff/NCG-for-2L-CVRP)

    *Yifan Xia, Xiangyi Zhang*

40. **MVMoE: Multi-Task Vehicle Routing Solver with Mixture-of-Experts** ICML, 2024. [paper](https://openreview.net/forum?id=lsQnneYa8p), [code](https://github.com/RoyalSkye/Routing-MVMoE)

    *Jianan Zhou, Zhiguang Cao, Yaoxin Wu, Wen Song, Yining Ma, Jie Zhang, Xu Chi*

41. **DPN: Decoupling Partition and Navigation for Neural Solvers of Min-max Vehicle Routing Problems** ICML, 2024. [paper](https://openreview.net/forum?id=ar174skI9u)

    *Zhi Zheng, Shunyu Yao, Zhenkun Wang, Xialiang Tong, Mingxuan Yuan, Ke Tang*

42. **Evolution of Heuristics: Towards Efficient Automatic Algorithm Design Using Large Language Model** ICML, 2024. [paper](https://openreview.net/forum?id=BwAkaxqiLB), [code](https://github.com/FeiLiu36/EoH)

    *Fei Liu, Xialiang Tong, Mingxuan Yuan, Xi Lin, Fu Luo, Zhenkun Wang, Zhichao Lu, Qingfu Zhang*

43. **ReEvo: Large Language Models as Hyper-Heuristics with Reflective Evolution** NeurIPS, 2024. [paper](https://openreview.net/forum?id=483IPG0HWL), [code](https://github.com/ai4co/reevo)

    *Haoran Ye, Jiarui Wang, Zhiguang Cao, Federico Berto, Chuanbo Hua, Haeyeon Kim, Jinkyoo Park, Guojie Song*

44. **Rethinking Neural Multi-Objective Combinatorial Optimization via Neat Weight Embedding** ICLR, 2025. [paper](https://openreview.net/forum?id=GM7cmQfk2F)

    *Jinbiao Chen, Zhiguang Cao, Jiahai Wang, Yaoxin Wu, Hanzhang Qin, Zizhen Zhang, Yue-Jiao Gong*

45. **Boosting Neural Combinatorial Optimization for Large-Scale Vehicle Routing Problems** ICLR, 2025. [paper](https://openreview.net/forum?id=TbTJJNjumY)

    *Fu Luo, Xi Lin, Yaoxin Wu, Zhenkun Wang, Tong Xialiang, Mingxuan Yuan, Qingfu Zhang*

46. **⭐ML4CO-Bench-101: Benchmark Machine Learning for Classic Combinatorial Problems on Graphs** NeurIPS, 2025. [paper](https://openreview.net/forum?id=ye4ntB1Kzi), [code](https://github.com/Thinklab-SJTU/ML4CO-Bench-101)

    *Jiale Ma, Wenzheng Pan, Yang Li, Junchi Yan*

47. **⭐COExpander: Adaptive Solution Expansion for Combinatorial Optimization** ICML, 2025. [paper](https://openreview.net/forum?id=KMaBXMWsBM), [code](https://github.com/Thinklab-SJTU/COExpander)

    *Jiale Ma, Wenzheng Pan, Yang Li, Junchi Yan*

48. **Large Language Models as End-to-end Combinatorial Optimization Solvers** NeurIPS, 2025. [paper](https://neurips.cc/virtual/2025/loc/san-diego/poster/115835), [code](https://github.com/Summer142857/LLMCoSolver)

    *Xia Jiang, Yaoxin Wu, Minshuo Li, Zhiguang Cao, Yingqian Zhang*

49. **Neural Solver Selection for Combinatorial Optimization** ICML, 2025. [paper](https://openreview.net/forum?id=e0OFWfvLCO)

    *Chengrui Gao, Haopu Shang, Ke Xue, Chao Qian*

50. **Preference Optimization for Combinatorial Optimization Problems** ICML, 2025. [paper](https://openreview.net/forum?id=Jwe5FJ8QGx), [code](https://github.com/MingjunPan/Preference-Optimization-for-Combinatorial-Optimization-Problems)

    *Mingjun Pan, Guanquan Lin, You-Wei Luo, Bin Zhu, Zhien Dai, Lijun Sun, Chun Yuan*

51. **A Mixed-Curvature based Pre-training Paradigm for Multi-Task Vehicle Routing Solver** ICML, 2025. [paper](https://openreview.net/forum?id=JsPyLqCgks)

    *Suyu Liu, Zhiguang Cao, Shanshan Feng, Yew-Soon Ong*

52. **SHIELD: Multi-task Multi-distribution Vehicle Routing Solver with Sparsity and Hierarchy** ICML, 2025. [paper](https://openreview.net/forum?id=6DJEaz1cCj)

    *Yong Liang Goh, Zhiguang Cao, Yining Ma, Jianan Zhou, Mohammed Haroon Dupty, Wee Sun Lee*

53. **PARCO: Parallel AutoRegressive Models for Multi-Agent Combinatorial Optimization** NeurIPS, 2025. [paper](https://openreview.net/forum?id=9F2Cmgo17M), [code](https://github.com/ai4co/parco)

    *Federico Berto, Chuanbo Hua, Laurin Luttmann, Jiwoo Son, Junyoung Park, Kyuree Ahn, Changhyun Kwon, Lin Xie, Jinkyoo Park*

54. **CaDA: Cross-Problem Routing Solver with Constraint-Aware Dual-Attention** ICML, 2025. [paper](https://openreview.net/forum?id=CS4RyQuTig), [code](https://github.com/CIAM-Group/CaDA)

    *Han Li, Fei Liu, Zhi Zheng, Yu Zhang, Zhenkun Wang*

55. **Rethinking Neural Combinatorial Optimization for Vehicle Routing Problems with Different Constraint Tightness Degrees** NeurIPS, 2025. [paper](https://openreview.net/forum?id=Lwn1rLB8t7), [code](https://github.com/CIAM-Group/Rethinking_Constraint_Tightness)

    *Fu Luo, Yaoxin Wu, Zhi Zheng, Zhenkun Wang*

56. **Improving Generalization of Neural Combinatorial Optimization for Vehicle Routing Problems via Test-Time Projection Learning** NeurIPS, 2025. [paper](https://openreview.net/forum?id=QPJjiNCRq1), [code](https://github.com/CIAM-Group/TTPL)

    *Yuanyao Chen, Rongsheng Chen, Fu Luo, Zhenkun Wang*

57. **Learning to Insert for Constructive Neural Vehicle Routing Solver** NeurIPS, 2025. [paper](https://openreview.net/forum?id=SXr3Dynctm), [code](https://github.com/CIAM-Group/L2C_Insert)

    *Fu Luo, Xi Lin, Mengyuan Zhong, Fei Liu, Zhenkun Wang, Jianyong Sun, Qingfu Zhang*

58. **MTL-KD: Multi-Task Learning Via Knowledge Distillation for Generalizable Neural Vehicle Routing Solver** NeurIPS, 2025. [paper](https://openreview.net/forum?id=rlH3e7VlY8)

    *Yuepeng Zheng, Fu Luo, Zhenkun Wang, Yaoxin Wu, Yu Zhou*

59. **Rethinking Light Decoder-based Solvers for Vehicle Routing Problems** ICLR, 2025. [paper](https://openreview.net/forum?id=4pRwkYpa2u), [code](https://github.com/ziweileonhuang/reld-nco)

    *Ziwei Huang, Jianan Zhou, Zhiguang Cao, Yixin Xu*

60. **Adversarial Generative Flow Network for Solving Vehicle Routing Problems** ICLR, 2025. [paper](https://openreview.net/forum?id=tBom4xOW1H), [code](https://github.com/ZHANG-NI/AGFN)

    *Ni Zhang, Jingfeng Yang, Zhiguang Cao, Xu Chi*

61. **Generalizable Heuristic Generation Through LLMs with Meta-Optimization** ICLR, 2026. [paper](https://arxiv.org/abs/2505.20881), [code](https://github.com/yiding-s/MoH)

    *Yiding Shi, Jianan Zhou, Wen Song, Jieyi Bi, Yaoxin Wu, Zhiguang Cao, Jie Zhang*

62. **DRAGON: LLM-Driven Decomposition and Reconstruction Agents for Large-Scale Combinatorial Optimization** AAMAS, 2026. [paper](https://arxiv.org/abs/2601.06502)

    *Shengkai Chen, Zhiguang Cao, Jianan Zhou, Yaoxin Wu, Senthilnath Jayavelu, Zhuoyi Lin, Xiaoli Li, Shili Xiang*

63. **Bridging Synthetic and Real Routing Problems via LLM-Guided Instance Generation and Progressive Adaptation** AAAI, 2026. [paper](https://arxiv.org/abs/2511.10233), [code](https://github.com/HenryZhu1029/EvoReal)

    *Jianghan Zhu, Yaoxin Wu, Zhuoyi Lin, Zhengyuan Zhang, Haiyan Yin, Zhiguang Cao, Senthilnath Jayavelu, Xiaoli Li*

64. **EoH-S: Evolution of Heuristic Set using LLMs for Automated Heuristic Design** AAAI, 2026. [paper](https://arxiv.org/abs/2508.03082), [code](https://github.com/FeiLiu36/EoH-S)

    *Fei Liu, Yilu Liu, Qingfu Zhang, Xialiang Tong, Mingxuan Yuan*

65. **Refining Hybrid Genetic Search for CVRP via Reinforcement Learning-Finetuned LLM** ICLR, 2026. [paper](https://arxiv.org/abs/2510.11121), [code](https://github.com/zaodushi/RFTHGS)

    *Rongjie Zhu, Cong Zhang, Zhiguang Cao*

66. **RRNCO: Towards Real-World Routing with Neural Combinatorial Optimization** ICLR, 2026. [paper](https://arxiv.org/abs/2503.16159), [code](https://github.com/ai4co/real-routing-nco)

    *Jiwoo Son, Zhikai Zhao, Federico Berto, Chuanbo Hua, Zhiguang Cao, Changhyun Kwon, Jinkyoo Park*

67. **Chain-of-Context Learning: Dynamic Constraint Understanding for Multi-Task VRPs** ICLR, 2026. [paper](https://openreview.net/forum?id=AhE6aSlz5g), [code](https://github.com/gshuangchun/CCL-MTLVRP)

    *Shuangchun Gui, Suyu Liu, Xuehe Wang, Zhiguang Cao*

68. **RADAR: Learning to Route with Asymmetry-aware Distance Representations** ICLR, 2026. [paper](https://openreview.net/forum?id=lWdxX5s9T1), [code](https://github.com/yihang0410/RADAR)

    *Hang Yi, Ziwei Huang, Yining Ma, Zhiguang Cao*

69. **Combination-of-Experts with Knowledge Sharing for Cross-Task Vehicle Routing Problems** ICLR, 2026. [paper](https://openreview.net/forum?id=lHBs9mbgwp), [code](https://github.com/yuzikang0/CoEKS)

    *Zikang Yu, Jinbiao Chen, Jiahai Wang*

70. **An Agentic Framework with LLMs for Solving Complex Vehicle Routing Problems** ICLR, 2026. [paper](https://openreview.net/forum?id=BMOgYw4EhQ), [code](https://github.com/ZHANG-NI/AFL)

    *Ni Zhang, Zhiguang Cao, Jianan Zhou, Cong Zhang, Yew-Soon Ong*

71. **Learning to Segment for Vehicle Routing Problems** ICLR, 2026. [paper](https://arxiv.org/abs/2507.01037), [code](https://github.com/mit-wu-lab/learning-to-segment)

    *Wenbin Ouyang, Sirui Li, Yining Ma, Cathy Wu*

72. **G-LNS: Generative Large Neighborhood Search for LLM-Based Automatic Heuristic Design** Arxiv, 2026. [paper](https://arxiv.org/abs/2602.08253), [code](https://github.com/ZBoyn/G-LNS)

    *Baoyun Zhao, He Wang, Liang Zeng*

73. **Beyond Simple Graphs: Neural Multi-Objective Routing on Multigraphs** ICLR, 2026. [paper](https://arxiv.org/abs/2506.22095), [code](https://github.com/filiprydin/GMS)

    *Filip Rydin, Attila Lischka, Jiaming Wu, Morteza Haghir Chehreghani, Balazs Kulcsar*

74. **⭐MaskCO: Masked Generation Drives Effective Representation Learning and Exploiting for Combinatorial Optimization** ICLR, 2026. [paper](https://openreview.net/forum?id=psUjNnLhl9), [code](https://github.com/Thinklab-SJTU/MaskCO)

    *Lvda Chen, Yang Li, Junchi Yan*

75. **Towards Efficient Constraint Handling in Neural Solvers for Routing Problems** ICLR, 2026. [paper](https://openreview.net/forum?id=raDFGuQxvD), [code](https://github.com/jieyibi/CaR-constraint)

    *Jieyi Bi, Zhiguang Cao, Jianan Zhou, Wen Song, Yaoxin Wu, Jie Zhang, Yining Ma, Cathy Wu*

76. **⭐Native Adaptive Solution Expansion for Diffusion-based Combinatorial Optimization** ICLR, 2026. [paper](https://openreview.net/forum?id=084SvT55yk)

    *Yu Wang, Yang Li, Jiale Ma, Junchi Yan, Yi Chang*

77. **Multi-Action Self-Improvement for Neural Combinatorial Optimization** ICLR, 2026. [paper](https://arxiv.org/abs/2510.12273), [code](https://github.com/LTluttmann/macsim)

    *Laurin Luttmann, Lin Xie*

78. **Multiagent Environments for Vehicle Routing Problems** INFORMS Journal on Computing, 2026. [paper](https://pubsonline.informs.org/doi/10.1287/ijoc.2025.1211), [code](https://github.com/MAEnvs4VRP/maenvs4vrp)

    *Ricardo Gama, Ricardo Cunha, Daniel Fuertes, Carlos R. del-Blanco, Hugo L. Fernandes*

79. **LINC: Decoupling Local Consequence Scoring from Hidden Matching in Constructive Neural Routing** NeurIPS, 2026. [paper](https://arxiv.org/abs/2605.06332), [code](https://github.com/Elaina10172004/LINC)

    *Shaofeng Qin, Li Wang*

### [Maximum Independent Set](#content)

1. **Combinatorial Optimization with Graph Convolutional Networks and Guided Tree Search.** NeurIPS, 2018. [paper](https://arxiv.org/abs/1810.10659)

    *Zhuwen Li, Qifeng Chen, Vladlen Koltun*

2. **Learning What to Defer for Maximum Independent Sets** ICML, 2020. [paper](http://proceedings.mlr.press/v119/ahn20a.html)

    *Sungsoo Ahn, Younggyo Seo, Jinwoo Shin*

3. **Distributed Scheduling Using Graph Neural Networks** ICASSP, 2021. [paper](https://ieeexplore.ieee.org/abstract/document/9414098?casa_token=Q4coRBbINPMAAAAA:0T8L49Kyn9p4CoM20-FqINKCyk_Sm3ye5TemPT8GlG3C3wXXLvn1RGKeHgriiyZIcg_GFB4z1A)

    *Zhongyuan Zhao, Gunjan Verma, Chirag Rao, Ananthram Swami, Santiago Segarra*

4. **Solving Graph-based Public Good Games with Tree Search and Imitation Learning** NeurlPS, 2021. [paper](https://arxiv.org/abs/2106.06762)

    *Victor-Alexandru Darvariu, Stephen Hailes, Mirco Musolesi*

5. **NN-Baker: A Neural-network Infused Algorithmic Framework for Optimization Problems on Geometric Intersection Graphs** NeurlPS, 2021. [paper](https://papers.nips.cc/paper/2021/file/c236337b043acf93c7df397fdb9082b3-Paper.pdf)

    *Evan McCarty, Qi Zhao, Anastasios Sidiropoulos, Yusu Wang*

6. **What's Wrong with Deep Learning in Tree Search for Combinatorial Optimization** ICLR, 2022. [paper](https://openreview.net/forum?id=mk0HzdqY7i1), [code](https://github.com/MaxiBoether/mis-benchmark-framework)

    *Maximilian Bother, Otto Kissig, Martin Taraz, Sarel Cohen, Karen Seidel, Tobias Friedrich*

7. **Optimistic tree search strategies for black-box combinatorial optimization** NeurlPS, 2022. [paper](https://openreview.net/forum?id=JGLW4DvX11F)

    *Cedric Malherbe, Antoine Grosnit, Rasul Tutunov, Haitham Bou Ammar, Jun Wang*

8. **⭐ROCO: A General Framework for Evaluating Robustness of Combinatorial Optimization Solvers on Graphs** ICLR, 2023. [paper](https://openreview.net/forum?id=2r6YMqz4Mml), [code](https://github.com/Thinklab-SJTU/ROCO)

    *Han Lu, Zenan Li, Runzhong Wang, Qibing Ren, Xijun Li, Mingxuan Yuan, Jia Zeng, Xiaokang Yang, Junchi Yan*

9. **Revisiting Sampling for Combinatorial Optimization** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/23661)

    *Haoran, Goshvadi Katayoon, Nova Azade, Schuurmans Dale Sun, Dai Hanjun.*

10. **DIFUSCO: Graph-based Diffusion Solvers for Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=JV8Ff0lgVV), [code](https://github.com/Edward-Sun/DIFUSCO)

    *Zhiqing Sun, Yiming Yang*

11. **⭐T2T: From Distribution Learning in Training to Gradient Search in Testing for Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=JtF0ugNMv2), [code](https://github.com/Thinklab-SJTU/T2TCO)

    *Yang Li, Jinpei Guo, Runzhong Wang, Junchi Yan*

12. **Unsupervised Learning for Combinatorial Optimization Needs Meta Learning** ICLR, 2023. [paper](https://openreview.net/forum?id=-ENYHCE8zBp), [code](https://github.com/Graph-COM/Meta_CO)

    *Haoyu Wang, Pan Li*

13. **Graph-based Deterministic Policy Gradient for Repetitive Combinatorial Optimization Problems** ICLR, 2023. [paper](https://openreview.net/forum?id=yHIIM9BgOo), [code](https://github.com/XzrTGMu/twin-nphard)

    *Zhongyuan Zhao, Ananthram Swami, Santiago Segarra*

14. **Let the Flows Tell: Solving Graph Combinatorial Optimization Problems with GFlowNets** NeurlPS, 2023. [paper](https://arxiv.org/abs/2305.17010), [code](https://github.com/zdhNarsil/GFlowNet-CombOpt)

    *Dinghuai Zhang, Hanjun Dai, Nikolay Malkin, Aaron Courville, Yoshua Bengio, Ling Pan*

15. **Variational Annealing on Graphs for Combinatorial Optimization** NeurlPS, 2023. [paper](https://openreview.net/forum?id=SLx7paoaTU), [code](https://github.com/ml-jku/VAG-CO)

    *Sebastian Sanokowski, Wilhelm Franz Berghammer, Sepp Hochreiter, Sebastian Lehner*

16. **Maximum Independent Set: Self-Training through Dynamic Programming** NeurlPS, 2023. [paper](https://openreview.net/forum?id=igE3Zbxvws), [code](https://github.com/LIONS-EPFL/dynamic-MIS)

    *Lorenzo Brusca, Lars CPM Quaedvlieg, Stratis Skoulakis, Grigorios G Chrysos, Volkan Cevher*

17. **DISCS: A Benchmark for Discrete Sampling** NeurlPS, 2023. [paper](https://openreview.net/forum?id=oi1MUMk5NF), [code](https://github.com/google-research/discs)

    *Katayoon Goshvadi, Haoran Sun, Xingchao Liu, Azade Nova, Ruqi Zhang, Will Sussman Grathwohl, Dale Schuurmans, Hanjun Dai*

18. **MARCO: A Memory-Augmented Reinforcement Framework for Combinatorial Optimization** IJCAI, 2024. [paper](https://www.ijcai.org/proceedings/2024/0766.pdf), [code](https://github.com/TheLeprechaun25/MARCO)

    *Andoni I. Garmendia, Quentin Cappart, Josu Ceberio, Alexander Mendiburu*

19. **⭐Fast T2T: Optimization Consistency Speeds Up Diffusion-Based Training-to-Testing Solving for Combinatorial Optimization** NeurIPS, 2024. [paper](https://openreview.net/pdf?id=xDrKZOZEOc), [code](https://github.com/Thinklab-SJTU/Fast-T2T)

    *Yang Li, Jinpei Guo, Runzhong Wang, Hongyuan Zha, Junchi Yan*

20. **Controlling Continuous Relaxation for Combinatorial Optimization** NeurlPS, 2024. [paper](https://openreview.net/pdf?id=ykACV1IhjD)

    *Yuma Ichikawa*

21. **Distributed Constrained Combinatorial Optimization leveraging Hypergraph Neural Networks** Nature Machine Intelligence, 2024. [paper](https://arxiv.org/abs/2311.09375), [code](https://github.com/nasheydari/HypOp)

    *Nasimeh Heydaribeni, Xinrui Zhan, Ruisi Zhang, Tina Eliassi-Rad, Farinaz Koushanfar*

22. **Efficient Combinatorial Optimization via Heat Diffusion** NeurlPS, 2024. [paper](https://openreview.net/pdf?id=psDrko9v1D)

    *Hengyuan Ma, Wenlian Lu, Jianfeng Feng*

23. **A Diffusion Model Framework for Unsupervised Neural Combinatorial Optimization** ICML, 2024. [paper](https://arxiv.org/abs/2406.01661), [code](https://github.com/ml-jku/DIffUCO)

    *Sebastian Sanokowski, Sepp Hochreiter, Sebastian Lehner*

24. **⭐ML4CO-Bench-101: Benchmark Machine Learning for Classic Combinatorial Problems on Graphs** NeurIPS, 2025. [paper](https://openreview.net/forum?id=ye4ntB1Kzi), [code](https://github.com/Thinklab-SJTU/ML4CO-Bench-101)

    *Jiale Ma, Wenzheng Pan, Yang Li, Junchi Yan*

25. **⭐COExpander: Adaptive Solution Expansion for Combinatorial Optimization** ICML, 2025. [paper](https://openreview.net/forum?id=KMaBXMWsBM), [code](https://github.com/Thinklab-SJTU/COExpander)

    *Jiale Ma, Wenzheng Pan, Yang Li, Junchi Yan*

26. **Large Language Models as End-to-end Combinatorial Optimization Solvers** NeurIPS, 2025. [paper](https://neurips.cc/virtual/2025/loc/san-diego/poster/115835), [code](https://github.com/Summer142857/LLMCoSolver)

    *Xia Jiang, Yaoxin Wu, Minshuo Li, Zhiguang Cao, Yingqian Zhang*

27. **⭐StruDiCO: Structured Denoising Diffusion with Gradient-free Inference-stage Boosting for Memory and Time Efficient Combinatorial Optimization** NeurIPS, 2025. [paper](https://openreview.net/forum?id=P69X3V4WwH), [code](https://github.com/yuuuuwang/StruDiCO)

    *Yu Wang, Yang Li, Junchi Yan, Yi Chang*

28. **⭐Generation as search operator for test-time scaling of diffusion-based combinatorial optimization** NeurIPS, 2025. [paper](https://openreview.net/forum?id=9JM03CQwzC), [code](https://github.com/Thinklab-SJTU/GenSCO)

    *Yang Li, Lvda Chen, Haonan Wang, Runzhong Wang, Junchi Yan*

29. **Scalable Discrete Diffusion Samplers: Combinatorial Optimization and Statistical Physics** ICLR, 2025. [paper](https://openreview.net/pdf?id=peNgxpbdxB)

    *Sebastian Sanokowski, Wilhelm Franz Berghammer, Haoyu Peter Wang, Martin Ennemoser, Sepp Hochreiter, Sebastian Lehner*

30. **Learning to Explore and Exploit with GNNs for Unsupervised Combinatorial Optimization** ICLR, 2025. [paper](https://openreview.net/forum?id=vaJ4FObpXN), [code](https://github.com/utkuumur/X2GNN)

    *Utku Umur Acikalin, Aaron M. Ferber, Carla P. Gomes*

31. **Optimization by Parallel Quasi-Quantum Annealing with Gradient-Based Sampling** ICLR, 2025. [paper](https://openreview.net/forum?id=9EfBeXaXf0), [code](https://github.com/Yuma-Ichikawa/QQA4CO)

    *Yuma Ichikawa, Yamato Arai*

32. **Continuous Parallel Relaxation for Finding Diverse Solutions in Combinatorial Optimization Problems** TMLR, 2025. [journal](https://openreview.net/forum?id=ix33zd5zCw), [code](https://github.com/Yuma-Ichikawa/QQA4CO)

    *Yuma Ichikawa, Hiroaki Iwashita*

33. **Regularized Langevin Dynamics for Combinatorial Optimization** ICML, 2025. [paper](https://openreview.net/forum?id=bbJ0QCujU4), [code](https://github.com/Shengyu-Feng/RLD4CO)

    *Shengyu Feng, Yiming Yang*

34. **Geometric Algorithms for Neural Combinatorial Optimization with Constraints** NeurIPS, 2025. [paper](https://openreview.net/forum?id=EPDLFWyNnF)

    *Nikolaos Karalias, Akbar Rafiey, Yifei Xu, Zhishang Luo, Behrooz Tahmasebi, Connie Jiang, Stefanie Jegelka*

35. **⭐MaskCO: Masked Generation Drives Effective Representation Learning and Exploiting for Combinatorial Optimization** ICLR, 2026. [paper](https://openreview.net/forum?id=psUjNnLhl9), [code](https://github.com/Thinklab-SJTU/MaskCO)

    *Lvda Chen, Yang Li, Junchi Yan*

36. **⭐ConRep4CO: Contrastive Representation Learning of Combinatorial Optimization Instances across Types** ICLR, 2026. [paper](https://openreview.net/forum?id=OXRnvOOiAf), [code](https://github.com/Thinklab-SJTU/ConRep4CO)

    *Ziao Guo, Yang Li, Shiyue Wang, Junchi Yan*

37. **⭐Native Adaptive Solution Expansion for Diffusion-based Combinatorial Optimization** ICLR, 2026. [paper](https://openreview.net/forum?id=084SvT55yk)

    *Yu Wang, Yang Li, Jiale Ma, Junchi Yan, Yi Chang*

38. **FrontierCO: Real-World and Large-Scale Evaluation of Machine Learning Solvers for Combinatorial Optimization** ICLR, 2026. [paper](https://openreview.net/forum?id=BVprkacwFY), [code](https://github.com/sunnweiwei/FrontierCO)

    *Shengyu Feng, Weiwei Sun, Shanda Li, Ameet Talwalkar, Yiming Yang*

### [Generalization](#content)

1. **It's Not What Machines Can Learn It's What We Cannot Teach** ICML, 2020. [paper](http://proceedings.mlr.press/v119/yehuda20a/yehuda20a.pdf)

    *Gal Yehuda, Moshe Gabel, Assaf Schuster*

2. **Learning TSP Requires Rethinking Generalization** CP, 2021. [paper](https://arxiv.org/pdf/2006.07054.pdf), [code](https://github.com/chaitjo/learning-tsp)

    *Chaitanya K. Joshi, Quentin Cappart, Louis-Martin Rousseau, Thomas Laurent*

3. **Generalization of Neural Combinatorial Solvers Through the Lens of Adversarial Robustness** ICLR, 2022. [paper](https://openreview.net/forum?id=vJZ7dPIjip3)

    *Simon Geisler, Johanna Sommer, Jan Schuchardt, Aleksandar Bojchevski, Stephan Günnemann*

4. **Learning for Robust Combinatorial Optimization: Algorithm and Application** INFOCOM, 2022. [journal](https://ieeexplore.ieee.org/abstract/document/9796715/)

    *Zhihui Shao, Jianyi Yang, Cong Shen, Shaolei Ren*

5. **⭐ROCO: A General Framework for Evaluating Robustness of Combinatorial Optimization Solvers on Graphs** ICLR, 2023. [paper](https://openreview.net/forum?id=2r6YMqz4Mml), [code](https://github.com/Thinklab-SJTU/ROCO)

    *Han Lu, Zenan Li, Runzhong Wang, Qibing Ren, Xijun Li, Mingxuan Yuan, Jia Zeng, Xiaokang Yang, Junchi Yan*

6. **Towards Omni-generalizable Neural Methods for Vehicle Routing Problems** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/25267), [code](https://github.com/RoyalSkye/Omni-VRP)

    *Zhou Jianan, Yaoxin Wu, Wen Song, Zhiguang Cao, Jie Zhang*

7. **Evolution of Heuristics: Towards Efficient Automatic Algorithm Design Using Large Language Model** ICML, 2024. [paper](https://openreview.net/forum?id=BwAkaxqiLB), [code](https://github.com/FeiLiu36/EoH)

    *Fei Liu, Xialiang Tong, Mingxuan Yuan, Xi Lin, Fu Luo, Zhenkun Wang, Zhichao Lu, Qingfu Zhang*

8. **ReEvo: Large Language Models as Hyper-Heuristics with Reflective Evolution** NeurIPS, 2024. [paper](https://openreview.net/forum?id=483IPG0HWL), [code](https://github.com/ai4co/reevo)

    *Haoran Ye, Jiarui Wang, Zhiguang Cao, Federico Berto, Chuanbo Hua, Haeyeon Kim, Jinkyoo Park, Guojie Song*

9. **GOAL: A Generalist Combinatorial Optimization Agent Learner** ICLR, 2025. [paper](https://openreview.net/forum?id=z2z9suDRjw)

    *Darko Drakulic, Sofia Michel, Jean-Marc Andreoli*

10. **OPTFM: A Scalable Multi-View Graph Transformer for Hierarchical Pre-Training in Combinatorial Optimization** NeurIPS, 2025. [paper](https://openreview.net/forum?id=24tuzE5KZc)

    *Hao Yuan, Wenli Ouyang, Changwen Zhang, Congrui Li, Yong Sun*

11. **Projecting Latent RL Actions: Towards Generalizable and Scalable Graph Combinatorial Optimization** Arxiv, 2026. [paper](https://arxiv.org/abs/2605.19721), [code](https://github.com/terranovafr/LaGCO-RL)

    *Franco Terranova, Guillermo Bernardez, Albert Cabellos-Aparicio, Nina Miolane, Abdelkader Lahmadi*

### [Orienteering Problem](#content)

1. **A reinforcement learning approach to the orienteering problem with time windows** Computers & Operations Research, 2021. [paper](https://arxiv.org/abs/2011.03647v2), [code](https://github.com/mustelideos/optw_rl)

    *Ricardo Gama, Hugo L. Fernandes*

2. **Meta-SAGE: Scale Meta-Learning Scheduled Adaptation with Guided Exploration for Mitigating Scale Shift on Combinatorial Optimization** ICML, 2023. [paper](https://icml.cc/virtual/2023/poster/25138)

    *Jiwoo Son, Minsu Kim, Hyeonah Kim, Jinkyoo Park*

3. **DeepACO: Neural-enhanced Ant Systems for Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=cd5D1DD923), [code](https://github.com/henry-yeh/DeepACO)

    *Haoran Ye, Jiarui Wang, Zhiguang Cao, Helan Liang, Yong Li*

4. **UDC: A Unified Neural Divide-and-Conquer Framework for Large-Scale Combinatorial Optimization Problems** NeurIPS, 2024. [paper](https://openreview.net/pdf?id=dCgbyvmlwL), [code](https://github.com/CIAM-Group/NCO_code/tree/main/single_objective/UDC-Large-scale-CO-master)

    *Zhi Zheng, Changliang Zhou, Tong Xialiang, Mingxuan Yuan, Zhenkun Wang*

### [Knapsack](#content)

1. **A Pointer Network Based Deep Learning Algorithm  for 0-1 Knapsack Problem** ICACI, 2018. [paper](https://ieeexplore.ieee.org/abstract/document/8377505)

    *Shenshen Gu, Hao Tao*

2. **An Investigation into Prediction + Optimisation for the Knapsack Problem** CPAIOR, 2019. [paper](https://link.springer.com/chapter/10.1007/978-3-030-19212-9_16)

    *Emir Demirovic, Peter J. Stuckey, James Bailey, Jeffrey Chan, Chris Leckie, Kotagiri Ramamohanarao, Tias Guns*

3. **A Novel Method to Solve Neural Knapsack Problems** ICML, 2021. [paper](http://proceedings.mlr.press/v139/li21m.html)

    *Duanshun Li, Jing Liu, Dongeun Lee, Ali Seyedmazloom, Giridhar Kaushik, Kookjin Lee, Noseong Park*

4. **Provably Good Solutions to the Knapsack Problem via Neural Networks of Bounded Size** AAAI, 2021. [paper](https://pubsonline.informs.org/doi/abs/10.1287/ijoc.2021.0225)

    *Christoph Hertrich, Martin Skutella*

5. **DeepACO: Neural-enhanced Ant Systems for Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=cd5D1DD923), [code](https://github.com/henry-yeh/DeepACO)

    *Haoran Ye, Jiarui Wang, Zhiguang Cao, Helan Liang, Yong Li*

6. **Winner Takes It All: Training Performant RL Populations for Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=v6VpqGcGAR)

    *Nathan Grinsztajn, Daniel Furelos-Blanco, Shikha Surana, Cl{\'e}ment Bonnet, Thomas D Barrett*

7. **Efficient Meta Neural Heuristic for Multi-Objective Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=593fc38lhN), [code](https://github.com/bill-cjb/EMNH)

    *Jinbiao Chen, Jiahai Wang, Zizhen Zhang, Zhiguang Cao, Te Ye, Siyuan Chen*

8. **BQ-NCO: Bisimulation Quotienting for Efficient Neural Combinatorial Optimization** NeurIPS, 2023. [paper](https://openreview.net/forum?id=BRqlkTDvvm), [code](https://github.com/naver/bq-nco)

    *Darko Drakulic, Sofia Michel, Florian Mai, Arnaud Sors, Jean-Marc Andreoli*

9. **Neural Multi-Objective Combinatorial Optimization with Diversity Enhancement** NeurIPS, 2023. [paper](https://openreview.net/forum?id=N4JkStI1fe), [code](https://github.com/bill-cjb/NHDE)

    *Jinbiao Chen, Zizhen Zhang, Zhiguang Cao, Yaoxin Wu, Yining Ma, Te Ye, Jiahai Wang*

10. **Rethinking Neural Multi-Objective Combinatorial Optimization via Neat Weight Embedding** ICLR, 2025. [paper](https://openreview.net/forum?id=GM7cmQfk2F)

    *Jinbiao Chen, Zhiguang Cao, Jiahai Wang, Yaoxin Wu, Hanzhang Qin, Zizhen Zhang, Yue-Jiao Gong*

11. **Approximation algorithms for combinatorial optimization with predictions** ICLR, 2025. [paper](https://openreview.net/forum?id=AEFVa6VMu1)

    *Antonios Antoniadis, Marek Elias, Adam Polak, Moritz Venzin*

### [Boolean Satisfiability](#content)

1. **Graph neural networks and boolean satisfiability.** Arxiv, 2017. [paper](https://arxiv.org/pdf/1702.03592)

    *Benedikt Bünz, Matthew Lamm.*

2. **Learning a SAT solver from single-bit supervision.** Arxiv, 2018. [paper](https://arxiv.org/pdf/1903.04671), [code](https://github.com/dselsam/neurosat)

    *Daniel Selsam, Benedikt Bünz Matthew Lamm, Leonardo de Moura Percy Liang, David L. Dill.*

3. **Machine learning-based restart policy for CDCL SAT solvers.** SAT, 2018. [paper](http://www.t-news.cn/Floc2018/FLoC2018-pages/proceedings_paper_477.pdf)

    *Jia Hui Liang, Minu Mathew Chanseok Oh, Chunxiao Li Ciza Thomas, Vijay Ganesh.*

4. **Learning to solve circuit-SAT: An unsupervised differentiable approach.** ICLR, 2019. [paper](https://openreview.net/pdf?id=BJxgz2R9t7), [code](https://github.com/johannaSommer/generalization-neural-co-solvers)

    *Saeed, Sergiy Matusevych Amizadeh, Markus Weimer.*

5. **Learning Local Search Heuristics for Boolean Satisfiability.** NeurIPS, 2019. [paper](https://www.cs.cmu.edu/~eyolcu/papers/learning-local-search-heuristics-sat.pdf), [code](https://github.com/emreyolcu/sat)

    *Emre Yolcu, Barnabas Poczos*

6. **Improving SAT solver heuristics with graph networks and reinforcement learning.** Arxiv, 2019. [paper](https://arxiv.org/pdf/1909.11830)

    *Vitaly Kurin, Shimon Whiteson Saad Godil, Bryan Catanzaro.*

7. **Graph neural reasoning may fail in certifying boolean unsatisfiability.** Arxiv, 2019. [paper](https://arxiv.org/pdf/1909.11588)

    *Ziliang Chen, Zhanfu Yang.*

8. **Guiding high-performance SAT solvers with unsat-core predictions.** SAT, 2019. [paper](https://arxiv.org/pdf/1903.04671)

    *Daniel Selsam, Nikolaj Bjørner.*

9. **G2SAT: Learning to Generate SAT Formulas.** NeurIPS, 2019. [paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7138247/), [code](https://github.com/JiaxuanYou/G2SAT)

    *Jiaxuan, Haoze Wu, Clark Barrett, Raghuram Ramanujan You, Jure Leskovec.*

10. **Learning Heuristics for Quantified Boolean Formulas through Reinforcement Learning.** Arxiv, 2019. [paper](https://arxiv.org/pdf/1807.08058), [code](https://github.com/lederg/learningqbf)

    *Gil Lederman, Edward A. Lee Markus N. Rabe, Sanjit A. Seshia.*

11. **Enhancing SAT solvers with glue variable predictions.** Arxiv, 2020. [paper](https://arxiv.org/pdf/2007.02559)

    *Jesse Michael. Han*

12. **Can Q-Learning with Graph Networks Learn a Generalizable Branching Heuristic for a SAT Solver?** NeurIPS, 2020. [paper](http://www.cs.ox.ac.uk/people/shimon.whiteson/pubs/kurinnips20.pdf)

    *Shimon Whiteson*

13. **Online Bayesian Moment Matching based SAT Solver Heuristics.** ICML, 2020. [paper](http://proceedings.mlr.press/v119/duan20c/duan20c.pdf), [code](https://github.com/saeednj/BMMSAT)

    *Haonan, Saeed Nejati, George Trimponias, Pascal Poupart Duan, Vijay Ganesh.*
