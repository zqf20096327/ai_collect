[![License: GPL](https://img.shields.io/badge/License-GPL-yellow)](https://github.com/AspirinCode/awesome-AI4MolConformation-MD)

## awesome-AI4MolConformation-MD
List of **molecules ( small molecules, RNA, peptide, protein, enzymes, antibody, and PPIs) conformations** and **molecular dynamics (force fields)** using **generative artificial intelligence** and **deep learning**


![Protein Space and Conformations](https://github.com/AspirinCode/awesome-AI4MolConformation-MD/blob/main/figure/afpro.png)


**Updating ...**  


## Menu

  - [Deep Learning-molecular conformations](#deep-learning-molecular-conformations)

| Menu | Menu | Menu | Menu |
| ------ | :---------- | ------ | ------ |
| [Reviews](#reviews) | [Datasets and Package](#datasets-and-package) | [Molecular dynamics](#molecular-dynamics) | [Molecular Force Fields](#molecular-force-fields) |
| [Neural Molecular Force Fields](#neural-molecular-force-fields) | [MD Engines-Frameworks](#md-engines-frameworks) | [AI4MD Engines-Frameworks](#ai4md-engines-frameworks) | [MD Trajectory Processing-Analysis](#md-trajectory-processing-analysis) |
| [Visualization](#visualization) | [CGMD](#cgmd) | [AI4MD](#ai4md) | [Neural Network Potentials](#neural-network-potentials) |
| [Neural Reactive Potential](#neural-reactive-potential) | [Reactive Force Fields](#reactive-force-fields) | [Free Energy Perturbation](#free-energy-perturbation) | [Solvent Potential](#solvent-potential) |
| [Theoretical Chemistry](#theoretical-chemistry) | [QuantumChem](#quantumchem) | [Ab Initio](#ab-initio) | [AI-QuantumChem](#ai-quantumchem) |
| [AlphaFold-based](#alphaFold-based) | [Autoregressive-Based](#autoregressive-Based)  | [LSTM-based](#lstm-based) | [Transformer-based](#transformer-based) |
| [VAE-based](#vae-based) | [GAN-based](#gan-based) | [Flow-based](#flow-based) | [Flow Matching-based](#flow-matching-based) |
| [Diffusion-based](#diffusion-based) | [Score-Based](#score-Based) | [Energy-based](#energy-based) | [Bayesian-based](#bayesian-based) |
| [Active Learning-based](#active-learning-based) | [GNN-based](#gnn-based) | [LLM-MD](#llm-md) | [Agent-based-MD](#agent-based-md) |

                                       
  - [Molecular conformational dynamics by methods](#molecular-conformational-dynamics-by-methods)

| Menu | Menu | Menu |
| ------ | :---------- | ------ |
| [Small molecule conformational dynamics](#small-molecule-conformational-dynamics) | [RNA conformational dynamics](#rna-conformational-dynamics) | [Peptide conformational dynamics](#peptide-conformational-dynamics) |
| [Protein conformational dynamics](#protein-conformational-dynamics) | [Enzymes conformational dynamics](#enzymes-conformational-dynamics)  | [Antibody conformational dynamics](#antibody-conformational-dynamics) |
| [Ligand-Protein conformational dynamics](#ligand-protein-conformational-dynamics) | [RNA-Peptide conformational dynamics](#rna-peptide-conformational-dynamics) | [PPI conformational dynamics](#ppi-conformational-dynamics) |
| [Antibody-Protein conformational dynamics](#antibody-protein-conformational-dynamics) | [Nucleic acid-Protein conformational dynamics](#nucleic-acid-protein-conformational-dynamics) | [Material ensembles](#material-dynamics) |
| [Nucleic acid-Ligand conformational dynamics](#nucleic-acid-ligand-conformational-dynamics) |  |  |








## Reviews





* **Benchmarking Generative AI and Physics-Based Molecular Simulation for Sampling Conformational Heterogeneity in T4 Lysozyme** [2026]  
Soumendranath Bhakat.  
[J. Chem. Inf. Model.(2026)](https://doi.org/10.1021/acs.jcim.6c02044)  

* **The Allosteric Revolution: From Static Structures to Conformational Ensembles and Next-Generation Therapeutics** [2026]  
Nussinov, Ruth, and Hyunbum Jang.  
[Journal of Molecular Biology(2026)](https://doi.org/10.1016/j.jmb.2026.169985)  

* **Predicting Biomolecular Interactions in the Next Decade: Physics-Based Methods Meet AI-Driven Approaches** [2026]  
Ruqaiya Khalil, Elena Frasnetti, Han Kurt, Tareq Hameduh, Mohd Athar, Giorgio Colombo, and Attilio Vittorio Vargiu.  
[J. Phys. Chem. Lett. (2026)](https://doi.org/10.1021/acs.jpclett.6c01412)  

* **Replacing Quantum Chemistry With Machine-Learned Interatomic Potentials: Revolution or Evolution?** [2026]  
Andrew J. Medford and David S. Sholl.  
[ACS Cent. Sci.(2026)](https://doi.org/10.1021/acscentsci.6c00615)  

* **Toward a unified framework for determining conformational ensembles of disordered proteins** [2026]  
Ghafouri, H., Kadeřávek, P., Melo, A.M. et al.  
[Nat Methods (2026)](https://doi.org/10.1038/s41592-026-03003-2)  

* **Graph neural networks for molecular dynamics simulations** [2026]  
Ahsan, Mohd, Chinmai Pindi, Souvik Sinha, Amun C. Patel, and Giulia Palermo.  
[Current Opinion in Structural Biology (2026)](https://doi.org/10.1016/j.sbi.2026.103238)  

* **Enhanced Sampling in the Age of Machine Learning: Algorithms and Applications** [2025]  
Kai Zhu, Enrico Trizio, Jintu Zhang, Renling Hu, Linlong Jiang, Tingjun Hou, Luigi Bonati.  
[arXiv:2509.04291 (2025)](https://doi.org/10.48550/arXiv.2509.04291)  

* **Generative AI techniques for conformational diversity and evolutionary adaptation of proteins** [2025]  
Brownless, Alfie-Louise R., Dariia Yehorova, Colin L. Welsh, and Shina Caroline Lynn Kamerlin.  
[Curr Opin Struct Biol. (2025)](https://doi.org/10.1016/j.sbi.2025.103135)  

* **Generation of protein dynamics by machine learning** [2025]  
Janson G, Feig M..  
[Curr Opin Struct Biol. (2025)](https://doi.org/10.1016/j.sbi.2025.103115)  

* **A critical review of machine learning interatomic potentials and Hamiltonian** [2025]  
Li, Y.; Zhang, X.; Liu, M.; Shen, L.  
  [J. Mater. Inf. (2025)](http://dx.doi.org/10.20517/jmi.2025.17)  

* **Generation of protein dynamics by machine learning** [2025]  
Janson, Giacomo, and Michael Feig.  
  [Current Opinion in Structural Biology 93 (2025)](https://doi.org/10.1016/j.sbi.2025.103115)  

* **Beyond static structures: protein dynamic conformations modeling in the post-AlphaFold era** [2025]  
 Xinyue Cui, Lingyu Ge, Xia Chen, Zexin Lv, Suhui Wang, Xiaogen Zhou, Guijun Zhang.  
  [Briefings in Bioinformatics (2025)](https://doi.org/10.1093/bib/bbaf340)  

* **From sequence to protein structure and conformational dynamics with artificial intelligence/machine learning** [2025]  
 Alexander M. Ille, Emily Anas, Michael B. Mathews, Stephen K. Burley.  
  [Struct. Dyn. 12, 030902 (2025)](https://doi.org/10.1063/4.0000765)  

* **Application of machine learning interatomic potentials in heterogeneous catalysis** [2025]  
 Olajide, Gbolagade, Khagendra Baral, Sophia Ezendu, Ademola Soyemi, and Tibor Szilvasi.  
  [Journal of Catalysis (2025)](https://doi.org/10.1016/j.jcat.2025.116202)  

* **The evolution of machine learning potentials for molecules, reactions and materials** [2025]   
 Xia, Junfan and Zhang, Yaolong and Jiang, Bin.  
  [Chem. Soc. Rev. (2025)](https://doi.org/10.1039/D5CS00104H)  

* **Advancing Molecular Simulations: Merging Physical Models, Experiments, and AI to Tackle Multiscale Complexity** [2025]   
 Giorgio Bonollo, Gauthier Trèves, Denis Komarov, Samman Mansoor, Elisabetta Moroni, and Giorgio Colombo.  
  [J. Phys. Chem. Lett. (2025)](https://doi.org/10.1021/acs.jpclett.5c00652)  

* **A comparison of probabilistic generative frameworks for molecular simulations** [2025]   
 Richard John, Lukas Herron, Pratyush Tiwary.  
  [J. Chem. Phys. (2025)](https://doi.org/10.1063/5.0249683)  

* **Recent Advances in Machine Learning and Coarse-Grained Potentials for Biomolecular Simulations and Their Applications** [2025]   
 B. Poma A, Hinostroza Caldas A, Cofas-Vargas L, Jones M, L. Ferguson A, Medrano Sandonas L.  
  [JChemRxiv. (2025)](https://doi.org/10.26434/chemrxiv-2025-vxjlk)  

* **Recent Advances in Simulation Software and Force Fields: Their Importance in Theoretical and Computational Chemistry and Biophysics** [2024]   
 Christophe Chipot.  
  [J. Phys. Chem. B (2024)](https://doi.org/10.1021/acs.jpcb.4c06231)  

* **Graph theory approaches for molecular dynamics simulations** [2024]   
 Patel AC, Sinha S, Palermo G.  
  [Quarterly Reviews of Biophysics. (2024)](https://doi.org/10.1017/S0033583524000143)  

* **Deep learning for intrinsically disordered proteins: From improved predictions to deciphering conformational ensembles** [2024]   
 Erdős, G., & Dosztányi, Z.   
  [Current opinion in structural biology (2024)](https://doi.org/10.1016/j.sbi.2024.102950)  

* **Recent advances in protein conformation sampling by combining machine learning with molecular simulation** [2024]   
 Tang, Y., Yang, Z., Yao, Y., Zhou, Y., Tan, Y., Wang, Z., Pan, T., Xiong, R., Sun, J. and Wei, G.   
  [Chinese Physics B. (2024)](https://iopscience.iop.org/article/10.1088/1674-1056/ad1a92)  

* **Alchemical Transformations and Beyond: Recent Advances and Real-World Applications of Free Energy Calculations in Drug Discovery** [2024]   
 Qian, Runtong, Jing Xue, You Xu, and Jing Huang.   
  [J. Chem. Inf. Model. (2024)](https://doi.org/10.1021/acs.jcim.4c01024)  

* **The need to implement FAIR principles in biomolecular simulations** [2024]   
 Amaro, Rommie, Johan Åqvist, Ivet Bahar, Federica Battistini, Adam Bellaiche, Daniel Beltran, Philip C. Biggin et al.   
  [arXiv:2407.16584 (2024)](https://arxiv.org/abs/2407.16584)  

* **An overview about neural networks potentials in molecular dynamics simulation** [2024]   
 Martin‐Barrios, Raidel, Edisel Navas‐Conyedo, Xuyi Zhang, Yunwei Chen, and Jorge Gulín‐González.   
  [International Journal of Quantum Chemistry 124.11 (2024)](https://doi.org/10.1002/qua.27389)  

* **Artificial Intelligence Enhanced Molecular Simulations** [2023]   
 Zhang, Jun, Dechin Chen, Yijie Xia, Yu-Peng Huang, Xiaohan Lin, Xu Han, Ningxi Ni et al.   
  [J. Chem. Theory Comput. (2023)](https://doi.org/10.1021/acs.jctc.3c00214)  

* **Machine Learning Generation of Dynamic Protein Conformational Ensembles** [2023]   
 Zheng, Li-E., Shrishti Barethiya, Erik Nordquist, and Jianhan Chen.   
  [Molecules 28.10 (2023)](https://doi.org/10.3390/molecules28104047)  





## Datasets and Package


### Datasets




* **DynaRepo: The repository of macromolecular conformational dynamics** [2025]  
Omid Mokhtari, Emmanuelle Bignon, Hamed Khakzad, Yasaman Karami.   
[Nucleic Acids Research (2025)](https://doi.org/10.1093/nar/gkaf1130) | [bioRxiv (2025)](https://doi.org/10.1101/2025.08.14.670260) | [data](https://dynarepo.inria.fr/)  

* **MS25: Materials Science-Focused Benchmark Data Set for Machine Learning Interatomic Potentials** [2025]  
Tristan Maxson, Ademola Soyemi, Xinglong Zhang, Benjamin W. J. Chen, and Tibor Szilvási.   
[J. Chem. Inf. Model. (2025)](https://doi.org/10.1021/acs.jcim.5c01262) | [data](https://doi.org/10.5281/zenodo/10901820)  

* **A Benchmark for Quantum Chemistry Relaxations via Machine Learning Interatomic Potentials** [2025]  
Fu, Cong, Yuchao Lin, Zachary Krueger, Wendi Yu, Xiaoning Qian, Byung-Jun Yoon, Raymundo Arróyave et al.  
[arXiv:2506.23008 (2025)](https://doi.org/10.48550/arXiv.2506.23008) | [data](https://huggingface.co/divelab)  

* **The Open Molecules 2025 (OMol25) Dataset, Evaluations, and Models** [2025]  
Levine, Daniel S., Muhammed Shuaibi, Evan Walter Clark Spotte-Smith, Michael G. Taylor, Muhammad R. Hasyim, Kyle Michel, Ilyes Batatia, G'abor Cs'anyi, Misko Dzamba, Peter K. Eastman, Nathan C. Frey, Xiang Fu, Vahe Gharakhanyan, Aditi S. Krishnapriyan, Joshua A. Rackers, Sanjeev Raja, Ammar Rizvi, Andrew S. Rosen, Zachary W. Ulissi, Santiago Vargas, C. Lawrence Zitnick, Samuel M. Blau and Brandon M. Wood.   
[arXiv:2505.08762 (2025)](https://arxiv.org/abs/2505.08762) | [data](https://huggingface.co/facebook/OMol25)  

* **Enhanced Sampling, Public Dataset and Generative Model for Drug-Protein Dissociation Dynamics** [2025]  
Maodong Li, Jiying Zhang, Bin Feng, Wenqi Zeng, Dechin Chen, Zhijun Pan, Yu Li, Zijing Liu, Yi Isaac Yang.   
[arXiv:2504.18367 (2025)](https://arxiv.org/abs/2504.18367) | [data](https://huggingface.co/SZBL-IDEA)  

* **QMe14S: A Comprehensive and Efficient Spectral Data Set for Small Organic Molecules** [2025]  
Cristian Gabellini, Nikhil Shenoy, Stephan Thaler, Semih Canturk, Daniel McNeela, Dominique Beaini, Michael Bronstein, Prudencio Tossou.   
[J. Phys. Chem. Lett. (2025)](https://doi.org/10.1021/acs.jpclett.5c00839) | [data](https://figshare.com/s/889262a4e999b5c9a5b3)  

* **UniSim: A Unified Simulator for Time-Coarsened Dynamics of Biomolecules** [2025]  
Ziyang Yu, Wenbing Huang, Yang Liu.  
[ICML 2025 (2025)](https://doi.org/10.48550/arXiv.2506.03157) | [code&data](https://zenodo.org/records/15394209)  

* **The QCML dataset, Quantum chemistry reference data from 33.5M DFT and 14.7B semi-empirical calculations** [2025]  
Ganscha, S., Unke, O.T., Ahlin, D. et al.  
[Sci Data 12, 406 (2025)](https://doi.org/10.1038/s41597-025-04720-7) | [data](https://zenodo.org/records/14859804)  

* **OpenQDC: Open Quantum Data Commons** [2024]  
Cristian Gabellini, Nikhil Shenoy, Stephan Thaler, Semih Canturk, Daniel McNeela, Dominique Beaini, Michael Bronstein, Prudencio Tossou.   
[arXiv:2411.19629 (2024)](https://arxiv.org/abs/2411.19629) | [data](https://github.com/valence-labs/openQDC)  

* **Molecular Quantum Chemical Data Sets and Databases for Machine Learning Potentials** [2024]  
Antonio Mirarchi, Toni Giorgino, G. D. Fabritiis.   
[ChemRxiv. (2024)](https://doi.org/10.26434/chemrxiv-2024-w3ld0-v2) | [code](https://github.com/Arif-PhyChem/datasets_and_databases_4_MLPs)  

* **mdCATH: A Large-Scale MD Dataset for Data-Driven Computational Biophysics** [2024]  
Antonio Mirarchi, Toni Giorgino, G. D. Fabritiis.   
[	arXiv:2407.14794 (2024)](https://arxiv.org/abs/2407.14794) | [code](https://github.com/compsciencelab/mdCATH)  

* **nablaDFT: Large-Scale Conformational Energy and Hamiltonian Prediction benchmark and dataset** [2022]  
Khrabrov, Kuzma and Shenbin, Ilya and Ryabov, Alexander and Tsypin, Artem and Telepov, Alexander and Alekseev, Anton and Grishin, Alexander and Strashnov, Pavel and Zhilyaev, Petr and Nikolenko, Sergey and Kadurin, Artur.   
[Phys. Chem. Chem. Phys. (2022)](https://doi.org/10.1039/D2CP03966D) | [code](https://github.com/AIRI-Institute/nablaDFT)  




### Package




**MMolearn**  
a Python package streamlining the design of generative models of biomolecular dynamics  

https://github.com/LumosBio/MolData   










## Molecular dynamics






* **PySTARC: GPU-accelerated Brownian dynamics for bimolecular association rate constants** [2026]  
Anupam Anand Ojha, Gary Huber, Shiksha Dutta, Sonya M. Hanson.  
[bioRxiv (2026)](https://doi.org/10.64898/2026.09.28.754770) | [code](https://github.com/anandojha/PySTARC)  

* **Large integration time-step in molecular dynamics simulation artificially enhances the strength of hydrophobic interaction** [2026]  
Dilipkumar N. Asthagiri.  
[arXiv:2609.30109(2026)](https://doi.org/10.48550/arXiv.2609.30109)  

* **Early-Enrichment Hit Discovery via Reversible-Work c(t) Estimation in Metadynamics (CTMD)** [2026]  
Venkata Sai Sreyas Adury, Pratyush Tiwary, Xinyu Gu, Mrinal Shekhar.  
[bioRxiv (2026)](https://doi.org/10.64898/2026.02.05.703972) | [code](https://github.com/mrinal-shekhar/CTMD)  

* **Gaussian Accelerated Molecular Dynamics in GROMACS** [2026]  
Yuefeng Yang.  
[bioRxiv (2026)](https://doi.org/10.64898/2026.08.10.743837)  

* **Ab Initio Molecular Dynamics Simulations for Organic Chemists─It is About Time!** [2026]  
Nielsen, M.M., Wagen, C.C., Gomes, L.A., Tantillo, D.J., Lopez, S.A. and Jacobsen, E.N.  
[J. Am. Chem. Soc. (2026)](https://doi.org/10.1021/jacs.5c20878)  

* **High-Performance Semiempirical Excited-State Molecular Dynamics: A Step Toward Data-Driven Photodynamics** [2025]  
Athavale V, Kulichenko M, Fernandez-Alberti S, Niklasson A, Tretiak S.  
[ChemRxiv. (2025)](https://doi.org/10.26434/chemrxiv-2025-6h565)  

* **STORMM: Structure and topology replica molecular mechanics for chemical simulations** [2024]  
David S. Cerutti, Rafal Wiewiora, Simon Boothroyd, Woody Sherman.  
[J. Chem. Phys. (2024)](https://doi.org/10.1063/5.0211032) | [code](https://github.com/psivant/stormm)  







### Molecular Force Fields









* **Leveraging Machine Learning Interatomic Potentials into Fitting Fast and Accurate AMBER-Compatible Precise Force Field** [2026]  
Xuchao Zhou, Xujian Wang, Jiahao Xie, et al.  
[ChemRxiv. (2026)](https://doi.org/10.26434/chemrxiv.15008812/v1) | [code](https://github.com/ClickFF/MAPLE) | [Zenodo](https://doi.org/10.5281/zenodo.21428725)  

* **Quantum Field Approaches to Chemical Systems** [2026]  
Reza Karimpour, Matteo Gori, Alexandre Tkatchenko.  
[Journal American Chemical Society (2026)](https://doi.org/10.1021/jacs.6c02077)  

* **Stapline: Development of a Force Field Library for Stapled Peptide Residues** [2026]  
Dr. Evangelia Notari, Dr. Marie T. J. Bluntzer, Prof. Julien Michel, et al.  
[ChemRxiv. (2026)](https://doi.org/10.26434/chemrxiv-2025-xfcnm/v2) | [code](https://github.com/michellab/Stapline)  

* **Force Field and Membrane Patch Size Effects on Atomistic Models of Aquaporin-7** [2026]  
Marta S. P. Batista, Miguel Machuqueiro, and Bruno L. Victor.  
[J. Chem. Inf. Model. (2026)](https://doi.org/10.1021/acs.jcim.6c00007)  

* **Automated Force Field Developer and Optimizer Platform: Torsion Reparameterization** [2026]  
Alejandro Blanco-Gonzalez, William Betancourt, Ryan Michael Snyder, Shi Zhang, Timothy J. Giese, Zeke A. Piskulich, Andreas W. Götz, Kenneth M. Merz Jr., Darrin M. York, Hasan Metin Aktulga, and Madushanka Manathunga.  
[J. Chem. Inf. Model. (2026)](https://doi.org/10.1021/acs.jcim.6c00528) | [web](https://www.attmosdiscovery.com/tools)  

* **LignAmb25: A Comprehensive AMBER Force Field Addressing Lignin's Structural and Chemical Diversity** [2026]  
Marco Lapsien, Michele Bonus, Julian Greb, Holger Gohlke.  
[bioRxiv (2026)](https://doi.org/10.64898/2026.01.03.697499)  

* **Charge Scaling Force Field for Biologically Relevant Ions Utilizing a Global Optimization Method** [2025]  
Shujie Fan, Philip E. Mason, Victor Cruces Chamorro, Brennon L. Shanks, Hector Martinez-Seara, and Pavel Jungwirth.  
[J. Chem. Theory Comput. (2025)](https://doi.org/10.1021/acs.jctc.5c00873)  

* **ABEEM Polarizable Force Field for PC Lipids: Parameterization and Molecular Dynamics Simulations** [2025]  
Xiaoyu Wang, Linlin Liu, Peiran Meng, Jian Zhao, Lei Wang, Cui Liu, Lidong Gong, and Zhongzhi Yang.  
[J. Chem. Theory Comput. (2025)](https://doi.org/10.1021/acs.jctc.4c01704)  

* **The PHAST 2.0 Force Field for General Small Molecule and Materials Simulations** [2025]  
Adam Hogan, Logan Ritter, and Brian Space.  
[J. Chem. Theory Comput. (2025)](https://doi.org/10.1021/acs.jctc.5c00134)  

* **Martini3-IDP: improved Martini 3 force field for disordered proteins** [2025]  
Wang, L., Brasnett, C., Borges-Araújo, L. et al.  
[Nat Commun 16, 2874 (2025)](https://doi.org/10.1038/s41467-025-58199-2) | [code](https://github.com/Martini-Force-Field-Initiative/Martini3-IDP-parameters)  















### Neural Molecular Force Fields








* **Learning consistent molecular mechanics force fields from first principles** [2026]  
Berkay Günes, Leif Seute, Jigyasa Nigam, Frauke Gräter.  
[arXiv:2610.08020(2026)](https://doi.org/10.48550/arXiv.2610.08020)  

* **Machine-learning force-field scoring rivals free-energy perturbation for congeneric ligand ranking across public benchmarks** [2026]  
Kevin Ryczko, Sarah Maier, Amogh Sood, et al.  
[ChemRxiv. (2026)](https://doi.org/10.26434/chemrxiv.15008810/v1)  

* **UniFlow: Unifying protein conformational ensemble generation and machine-learned force fields with a scalable normalizing Flow** [2026]  
Yikai Liu, Ming Chen, Guang Lin.  
[bioRxiv (2026)](https://doi.org/10.64898/2026.07.17.739266) | [code](https://github.com/Harrydirk41/UniFlow)  

* **Full-data accuracy with fewer labels for training and fine-tuning machine-learning force fields** [2026]  
Sheng Bi, Yi-Ze Wang, Jun Cheng.  
[arXiv:2607.14486 (2026)(2026)](https://doi.org/10.48550/arXiv.2607.14486)  

* **UniFFBench: evaluating universal machine learning force fields against experimental measurements** [2026]  
Mannan, S., Bihani, V., Gonzales, C. et al.  
[Nat Comput Sci (2026)(2026)](https://doi.org/10.1038/s43588-026-01019-4) | [code](https://github.com/M3RG-IITD/UniFFBench) | [Zenodo](https://doi.org/10.5281/zenodo.20165458)  

* **seekrflow: Towards end-to-end automated simulation pipeline with machine-learned force fields for accelerated drug-target kinetic and thermodynamic predictions** [2026]  
Anupam A. Ojha, Lane W. Votapka, Shiksha Dutta, Anson F. Noland, Sonya M. Hanson, Rommie E. Amaro.  
[J. Chem. Theory Comput. (2026)](https://doi.org/10.1021/acs.jctc.6c00659) | [bioRxiv. (2026)](https://doi.org/10.1101/2025.08.13.669965) | [code](https://github.com/seekrcentral/seekrflow)  

* **Fast training of bespoke SMIRNOFF-format molecular mechanics force fields using machine learning potentials** [2026]  
Finlay Clark, Thomas Pope, Sarah Maier, et al.  
[ChemRxiv. (2026)](https://doi.org/10.26434/chemrxiv.15004169/v1) | [code](https://github.com/cole-group/presto)  

* **Bridging quantum mechanics to liquid properties via a universal organic force field** [2026]  
  Zheng, T., Xu, X., Wang, Z. et al.  
  [Nat Commun (2026)](https://doi.org/10.1038/s41467-026-73566-3) | [code](https://github.com/ByteDance-Seed/byteff2)  

* **MAPLE: a machine-learning force-field-native platform for automated reaction modeling and enzyme design** [2026]  
  Wang, Xujian, Zeyu Sun, Yilu Zhang, Carlo Asam, Ruzhan Zhu, Wan-Lu Li, and Junmei Wang.  
  [Chemical Science (2026)](https://doi.org/10.1039/D6SC01279E) | [code](https://github.com/ClickFF/MAPLE)  

* **aims-PAX: Parallel Active Exploration Enables Expedited Construction of Machine Learning Force Fields for Molecules and Materials** [2026]  
Henkes, Tobias, Shubham Sharma, Alexandre Tkatchenko, Mariana Rossi, and Igor Poltavsky..  
[J. Chem. Inf. Model. (2026)](https://doi.org/10.1021/acs.jcim.5c02682) | [code](https://github.com/tohenkes/aims-PAX)  

* **DeFecT-FF: a machine learning force field framework for high throughput defect modeling in CdTe-based solar cells** [2026]  
Rahman, Md Habibur, Maitreyo Biswas, and Arun Mannodi-Kanakkithodi.  
[Phys. Chem. Chem. Phys. (2026)](https://doi.org/10.1039/D6CP00170J) | [data](https://nanohub.org/resources/defectdatabase)  

* **Accurate Hydration Free Energy Calculations for Diverse Organic Molecules With a Machine Learning Force Field** [2026]  
Xiaowei Xie, John L. Weber, Mats Svensson, Ryne C. Johnston, Edward D. Harder, and Leif D. Jacobson.  
[J. Chem. Theory Comput. (2026)](https://doi.org/10.1021/acs.jctc.5c02019) | [code](https://github.com/leifjacobson/MLFF_HFE/)  

* **Training a force field for proteins and small molecules from scratch** [2026]  
Alexandre Blanco-González, Thea K Schulze, Evianne Rovers, Joe G Greener.  
[arXiv:2603.16770 (2026)](https://doi.org/10.48550/arXiv.2603.16770) | [code](https://github.com/greener-group/garnet)  

* **A scalable and quantum-accurate foundation model for biomolecular force fields via linearly tensorized quadrangle attention** [2026]  
Su, Q., Zhu, K., Gou, Q. et al.  
[Nat Commun (2026)](https://doi.org/10.1038/s41467-026-70377-4) | [code](https://github.com/lingcon01/LiTEN/tree/master)  

* **Machine Learning Accelerated Finite-Field Simulations for Electrochemical Interfaces** [2025]  
Chaoqiang Feng and Bin Jiang.  
[JACS Au (2025)](https://doi.org/10.1021/jacsau.5c00792) | [code](https://github.com/bjiangch/FIREANN)  

* **Bayesian learning for accurate and robust biomolecular force fields** [2025]  
Vojtech Kostal, Brennon L. Shanks, Pavel Jungwirth, Hector Martinez-Seara.  
[arXiv:2511.05398 (2025)](https://doi.org/10.48550/arXiv.2511.05398)  

* **Physical embedding machine learning force fields for organic systems** [2025]  
Junbao Hu, Dingyu Hou, Jian Jiang.  
[arXiv:2509.10270 (2025)](https://doi.org/10.48550/arXiv.2509.10270)  

* **DEQuify your force field: More efficient simulations using deep equilibrium models** [2025]  
Andreas Burger, Luca Thiede, Alán Aspuru-Guzik, Nandita Vijaykumar.  
[arXiv:2509.08734 (2025)](https://doi.org/10.48550/arXiv.2509.08734)  

* **Deep Residual Learning for Molecular Force Fields** [2025]  
Jiang X, Chen M, Cao D, Yu J, Zhang R, Fu Z, et al.  
[ChemRxiv. (2025)](https://doi.org/10.26434/chemrxiv-2025-003lg-v2) | [code](https://github.com/Ameki0/ResFF)  

* **aims-PAX: Parallel Active eXploration for the automated construction of Machine Learning Force Fields** [2025]  
Tobias Henkes, Shubham Sharma, Alexandre Tkatchenko, Mariana Rossi, Igor Poltavskyi.  
[arXiv:2508.12888 (2025)](https://doi.org/10.48550/arXiv.2508.12888) | [code](https://github.com/tohenkes/aims-PAX)  

* **A density based machine learning force field for molecule-molecule nonbonded interactions** [2025]  
Wang L-W.  
[ChemRxiv. (2025)](https://doi.org/10.26434/chemrxiv-2025-83grg)  

* **Force field optimization by end-to-end differentiable atomistic simulation** [2025]  
Abhijeet Sadashiv Gangan, Ekin Dogus Cubuk, Samuel S. Schoenholz, Mathieu Bauchy, and N. M. Anoop Krishnan.  
[J. Chem. Theory Comput. (2025)](https://doi.org/10.1021/acs.jctc.4c01784) | [code](https://github.com/M3RG-IITD/Force-field-optimization)  

* **Operator Forces For Coarse-Grained Molecular Dynamics** [2025]  
Klein, Leon, Atharva Kelkar, Aleksander Durumeric, Yaoyi Chen, and Frank Noé.  
[arXiv:2506.19628 (2025)](https://doi.org/10.48550/arXiv.2506.19628) | [code](https://github.com/noegroup/OperatorForces4CG)  

* **Evolutionary machine learning of physics-based force fields in high-dimensional parameter-space** [2025]  
van der Spoel D, Marrades J, Kriz K, Hosseini AN, Nordman A, Ateide Martins JP, et al.  
[	Digital Discovery (2025)](https://doi.org/10.1039/D5DD00178A) | [code](https://github.com/AlexandriaChemistry/ACT)  

* **To Use or Not to Use a Universal Force Field** [2025]  
Denan Li, Jiyuan Yang, Xiangkai Chen, Lintao Yu, Shi Liu.  
[arXiv:2503.08207 (2025)](https://arxiv.org/abs/2503.08207)  

* **Understanding and Mitigating Distribution Shifts For Machine Learning Force Fields** [2025]  
Kreiman, Tobias, and Aditi S. Krishnapriyan.  
[arXiv:2503.08674 (2025)](https://arxiv.org/abs/2503.08674) | [code](https://github.com/ASK-Berkeley/MLFF-distribution-shifts)  

* **Accelerating CO2 direct air capture screening for metal-organic frameworks with a transferable machine learning force field** [2025]  
Yunsung Lim and Hyunsoo Park and Aron Walsh and Jihan Kim.  
[Matter (2025)](https://doi.org/10.1016/j.matt.2025.102203) | [code](https://github.com/hspark1212/DAC-SIM)  

* **On the design space between molecular mechanics and machine learning force fields** [2025]  
Wang, Yuanqing, Kenichiro Takaba, Michael S. Chen, Marcus Wieder, Yuzhi Xu, Tong Zhu, John ZH Zhang et al.  
[Appl. Phys. Rev. (2025)](https://doi.org/10.1063/5.0237876)  

* **ABFML: A problem-oriented package for rapidly creating, screening, and optimizing new machine learning force fields** [2025]  
Xingze Geng, Jianing Gu, Gaowu Qin, Lin-Wang Wang, Xiangying Meng.  
[J. Chem. Phys. (2025)](https://doi.org/10.1063/5.0247559) | [code](https://github.com/gengxingze/ABFML)  

* **Reversible molecular simulation for training classical and machine-learning force fields** [2025]  
Greener, Joe G.   
[Proc. Natl. Acad. Sci. (2025)](https://doi.org/10.1073/pnas.2426058122) | [code](https://github.com/greener-group/rev-sim)  

* **Artificial Intelligence for Direct Prediction of Molecular Dynamics Across Chemical Space** [2025]  
Ge F, Dral PO.  
[ChemRxiv. (2025)](https://doi.org/10.26434/chemrxiv-2025-kc7sn) | [code](https://github.com/dralgroup/mlatom)  

* **NepoIP/MM: Toward Accurate Biomolecular Simulation with a Machine Learning/Molecular Mechanics Model Incorporating Polarization Effects** [2025]  
Ge Song and Weitao Yang.  
[J. Chem. Theory Comput. (2025)](https://doi.org/10.1021/acs.jctc.5c00372) | [code](https://github.com/Yang-Laboratory/NepoIP)  

* **Efficient Long-Range Machine Learning Force Fields for Liquid and Materials Properties** [2025]  
Weber, John L., Rishabh D. Guha, Garvit Agarwal, Yujing Wei, Aidan A. Fike, Xiaowei Xie, James Stevenson et al.  
[arXiv:2505.06462 (2025)](https://arxiv.org/abs/2505.06462) | [code](https://github.com/leifjacobson/MLFF_test_data)  

* **MACE-OFF: Short-Range Transferable Machine Learning Force Fields for Organic Molecules** [2025]  
Dávid Péter Kovács, J. Harry Moore, Nicholas J. Browning, Ilyes Batatia, Joshua T. Horton, Yixuan Pu, Venkat Kapil, William C. Witt, Ioan-Bogdan Magdău, Daniel J. Cole, and Gábor Csányi.  
[J. Am. Chem. Soc. (2025)](https://doi.org/10.1021/jacs.4c07099) | [code](https://github.com/ACEsuit/mace-off)  

* **Grappa--A Machine Learned Molecular Mechanics Force Field** [2025]  
Seute, Leif, Eric Hartmann, Jan Stühmer, and Frauke Gräter.  
[Chemical Science 16.6 (2025)](https://doi.org/10.1039/D4SC05465B) | [arXiv:2404.00050 (2024)](https://arxiv.org/abs/2404.00050) | [code](https://github.com/graeter-group/grappa)  

* **ILVES: Accurate and efficient bond length and angle constraints in molecular dynamics** [2025]  
López-Villellas, L., Mikkelsen, C.C.K., Galano-Frutos, J.J., Marco-Sola, S., Alastruey-Benedé, J., Ibáñez, P., Moretó, M., De Rosa, M.C. and García-Risueño, P.  
[arXiv:2503.13075 (2025)](https://arxiv.org/abs/2503.13075)  

* **Towards Fast, Specialized Machine Learning Force Fields: Distilling Foundation Models via Energy Hessians** [2025]  
Ishan Amin, Sanjeev Raja, Aditi Krishnapriyan.  
[arXiv:2501.09009 (2025)](https://arxiv.org/abs/2501.09009) | [code](https://github.com/ASK-Berkeley/MLFF-distill)  

* **BoostMD: Accelerated Molecular Sampling Leveraging ML Force Field Features** [2025]  
Zhaoxin Xie, Yanheng Li, Yijie Xia, Jun Zhang, Sihao Yuan, Cheng Fan, Yi Isaac Yang, and Yi Qin Gao.  
[J. Chem. Theory Comput. (2025)](https://doi.org/10.1021/acs.jctc.4c01449)  

* **Efficient and Precise Force Field Optimization for Biomolecules Using DPA-2** [2024]  
Junhan Chang, Duo Zhang, Yuqing Deng, Hongrui Lin, Zhirong Liu, Linfeng Zhang, Hang Zheng, Xinyan Wang.   
[arXiv:2406.09817 (2024)](https://arxiv.org/abs/2406.09817) | [code](https://github.com/deepmodeling/DeePDih)  

* **FeNNol: An efficient and flexible library for building force-field-enhanced neural network potentials** [2024]  
Thomas Plé, Olivier Adjoua, Louis Lagardère, Jean-Philip Piquemal.   
[J. Chem. Phys. (2024)](https://doi.org/10.1063/5.0217688) | [code](https://github.com/thomasple/FeNNol)  

* **Reversible molecular simulation for training classical and machine learning force fields** [2024]  
Joe G Greener.   
[arXiv:2412.04374 (2024)](https://arxiv.org/abs/2412.04374) | [code](https://github.com/JuliaMolSim/Molly.jl)  

* **HessFit: A Toolkit to Derive Automated Force Fields from Quantum Mechanical Information** [2024]  
Falbo, E. and Lavecchia, A.   
[J. Chem. Inf. Model. (2024)](https://doi.org/10.1021/acs.jcim.4c00540) | [code](https://github.com/emanuelefalbo/HessFit)  

* **A Euclidean transformer for fast and stable machine learned force fields** [2024]  
Frank, J.T., Unke, O.T., Müller, KR. et al.   
[Nat Commun 15, 6539 (2024)](https://doi.org/10.1038/s41467-024-50620-6) | [code](https://github.com/microsoft/AI2BMD/tree/ViSNet/chignolin_data)

* **Differentiable simulation to develop molecular dynamics force fields for disordered proteins** [2024]  
Greener, Joe G.   
[Chemical Science 15.13 (2024)](https://doi.org/10.1039/D3SC05230C) | [code](https://github.com/greener-group/GB99dms)  

* **Grappa--A Machine Learned Molecular Mechanics Force Field** [2024]  
Seute, Leif, Eric Hartmann, Jan Stühmer, and Frauke Gräter.  
[arXiv:2404.00050 (2024)](https://arxiv.org/abs/2404.00050) | [code](https://github.com/graeter-group/grappa)  

* **An implementation of the Martini coarse-grained force field in OpenMM** [2023]  
MacCallum, J. L., Hu, S., Lenz, S., Souza, P. C., Corradi, V., & Tieleman, D. P.   
[Biophysical Journal 122.14 (2023)](https://doi.org/10.1016/j.bpj.2023.04.007)  

* **Improving machine learning force fields for molecular dynamics simulations with fine-grained force metrics** [2023]  
Zun Wang, Hongfei Wu, Lixin Sun, Xinheng He, Zhirong Liu, Bin Shao, Tong Wang, Tie-Yan Liu.   
[J. Chem. Phys. (2023)](https://doi.org/10.1063/5.0147023) | [data](https://figshare.com/articles/dataset/Revised_MD17_dataset_rMD17_/12672038)    

* **End-to-end differentiable construction of molecular mechanics force fields** [2022]  
Wang, Yuanqing, Josh Fass, Benjamin Kaminow, John E. Herr, Dominic Rufa, Ivy Zhang, Iván Pulido et al.   
[Chemical Science (2022)](https://doi.org/10.1039/D2SC02739A) | [code](https://github.com/openforcefield/openff-nagl)  

* **Improving molecular force fields across configurational space by combining supervised and unsupervised machine learning** [2021]  
Gregory Fonseca, Igor Poltavsky, Valentin Vassilev-Galindo, Alexandre Tkatchenko.   
[J. Chem. Phys. (2021)](https://doi.org/10.1063/5.0035530)  




### MD Engines-Frameworks

* [Amber](http://ambermd.org/) - A suite of biomolecular simulation programs.  
* [Gromacs](http://www.gromacs.org/) - A molecular dynamics package mainly designed for simulations of proteins, lipids and nucleic acids.
* [OpenMM](http://openmm.org/) - A toolkit for molecular simulation using high performance GPU code.  
* [CHARMM](https://www.charmm.org/) - A molecular simulation program with broad application to many-particle systems.  
* [HTMD](https://github.com/Acellera/htmd) - Programming Environment for Molecular Discovery.  
* [ACEMD](https://www.acellera.com/acemd) - The next generation molecular dynamic simulation software.  
* [NAMD](https://www.ks.uiuc.edu/Research/namd/) - A parallel molecular dynamics code for large biomolecular systems.
* [StreaMD](https://github.com/ci-lab-cz/streamd) - A tool to perform high-throughput automated molecular dynamics simulations.
* [BEMM-GEN](https://github.com/y4suda/BEMM-GEN) - A Toolkit for Generating a Biomolecular Environment-Mimicking Model for Molecular Dynamics Simulation.
* [BioSimSpace](https://github.com/OpenBioSim/biosimspace) - An interoperable Python framework for biomolecular simulation.
* [STORMM](https://github.com/Psivant/stormm) - Structure and TOpology Replica Molecular Mechanics.
* [multiSMD](https://github.com/kszewc/multiSMD) - A Python Toolset for Multidirectional Steered Molecular Dynamics.
* [CCD2MD](https://github.com/keb721/CCD2MD) - A Suite of Packages for Preparing Co-Folded Outputs for Molecular Dynamics Simulations.





* **CCD2MD: A Suite of Packages for Preparing Co-Folded Outputs for Molecular Dynamics Simulations** [2025]  
Katarina E. Blow, Matyas Parrag, and Phillip J. Stansfeld.  
[J. Chem. Inf. Model. (2025)](https://doi.org/10.1021/acs.jcim.5c02066) | [code](https://github.com/keb721/CCD2MD)  

* **multiSMD – A Python Toolset for Multidirectional Steered Molecular Dynamics** [2025]  
Katarzyna Walczewska-Szewc, Beata Niklas, Kamil Szewc, and Wiesław Nowak.  
[J. Chem. Inf. Model. (2025)](https://doi.org/10.1021/acs.jcim.5c01742) | [code](https://github.com/kszewc/multiSMD)  

* **OpenCafeMol: A GPU-accelerated coarse-grained biomolecular dynamics simulator with OpenMM library** [2025]  
Barnett, Simon, and John D. Chodera.  
[bioRxiv. (2025)](https://doi.org/10.1101/2025.02.20.639390)  





### AI4MD Engines-Frameworks

* [OpenMM 8](https://github.com/openmm/openmm) - Molecular Dynamics Simulation with Machine Learning Potentials.  
* [DeePMD-kit](https://github.com/deepmodeling/deepmd-kit) - A deep learning package for many-body potential energy representation and molecular dynamics.  
* [TorchMD](https://github.com/torchmd/torchmd) - End-To-End Molecular Dynamics (MD) Engine using PyTorch.  
* [TorchMD-NET](https://github.com/torchmd/torchmd-net) - TorchMD-NET provides state-of-the-art neural networks potentials (NNPs) and a mechanism to train them.  
* [OpenMM-Torch](https://github.com/openmm/openmm-torch) - OpenMM plugin to define forces with neural networks.  
* [AI<sup>2</sup>BMD](https://github.com/microsoft/AI2BMD) - AI-powered ab initio biomolecular dynamics simulation.  
* [NeuralMD](https://github.com/chao1224/NeuralMD) - A Multi-Grained Symmetric Differential Equation Model for Learning Protein-Ligand Binding Dynamics.  
* [TorchSim](https://github.com/Radical-AI/torch-sim) - A next-generation open-source atomistic simulation engine for the MLIP era.  




### MD Trajectory Processing-Analysis


* [MDAnalysis](https://www.mdanalysis.org/) - An object-oriented Python library to analyze trajectories from molecular dynamics (MD) simulations in many popular formats.  
* [MDTraj](http://mdtraj.org/) - A python library that allows users to manipulate molecular dynamics (MD) trajectories.  
* [PyTraj](https://amber-md.github.io/pytraj/) - A Python front-end package of the popular cpptraj program.  
* [CppTraj](https://github.com/Amber-MD/cpptraj) - Biomolecular simulation trajectory/data analysis.  
* [WEDAP](https://github.com/chonglab-pitt/wedap) - A Python Package for Streamlined Plotting of Molecular Simulation Data. 
* [Melodia](https://github.com/rwmontalvao/Melodia_py) - A Python library for protein structure analysis. 
* [MDANCE](https://github.com/mqcomplab/MDANCE) - A flexible n-ary clustering package that provides a set of tools for clustering Molecular Dynamics trajectories.  
* [PENSA](https://github.com/drorlab/pensa) - A collection of python methods for exploratory analysis and comparison of biomolecular conformational ensembles.
* [eRMSF](https://github.com/pablo-arantes/ermsfkit) - A Python Package for Ensemble-Based RMSF Analysis of Biomolecular Systems.







* **Pharmacon: A Molecular Dynamics Simulation Analysis Toolkit** [2026]  
Kyriakos Georgiou and Antonios Kolocouris.  
[J. Chem. Inf. Model. (2026)](https://doi.org/10.1021/acs.jcim.6c00837) | [code](https://github.com/k-georgiou/pharmacon)  

* **Accelerating molecular dynamics simulations using fast Ewald summation with prolates** [2026]  
Liang, J., Lu, L., Barnett, A. et al.  
[Nat Commun (2026)](https://doi.org/10.1038/s41467-026-73232-8)  

* **MonicaMD: Molecules and Internal Cluster Analysis of Molecular Dynamics Simulations** [2026]  
Ferdinand L. Pointner, Sebastian Reiter, Benjamin P. Fingerhut, and Regina de Vivie-Riedle.  
[J. Chem. Inf. Model. (2026)](https://doi.org/10.1021/acs.jcim.6c00502)  

* **CRISP: Enhancing ASE Workflows With Advanced Molecular Simulation Post-Processing** [2026]  
I.Saha, D.Willimetz, and L.Grajciar.  
[Journal of Computational Chemistry (2026)](https://doi.org/10.1002/jcc.70384)  

* **Ensemble Analyzer: An Open-Source Python Framework for Automated Conformer Ensemble Refinement** [2026]  
Andrea Pellegrini, Paolo Righi, Andrea Mazzanti, and Michele Mancinelli.  
[J. Chem. Inf. Model. (2026)](https://doi.org/10.1021/acs.jcim.6c00273) | [code](https://github.com/andre-cloud/ensemble_analyzer)  

* **FastMDAnalysis: Software for Automated Analysis of Molecular Dynamics Trajectories** [2026]  
A.Aina and D.Kwan.  
[Journal of Computational Chemistry (2026)](https://doi.org/10.1002/jcc.70350) | [code](https://github.com/aai-research-lab/FastMDAnalysis)  

* **Hierarchical geometric deep learning enables scalable analysis of molecular dynamics** [2025]  
Zihan Pengmei, Spencer C. Guo, Chatipat Lorpaiboon, Aaron R. Dinner.  
[arXiv:2512.06520(2025)](https://doi.org/10.48550/arXiv.2512.06520) | [code](https://github.com/dinner-group/geom2vec)  

* **eRMSF: A Python Package for Ensemble-Based RMSF Analysis of Biomolecular Systems** [2025]  
Pablo Ricardo Arantes, Rodrigo Ligabue-Braun, and Conrado Pedebos.  
[J. Chem. Inf. Model. (2025)](https://doi.org/10.1021/acs.jcim.5c02413) | [code](https://github.com/pablo-arantes/ermsfkit)  

* **apoCHARMM: High-performance molecular dynamics simulations on GPUs for advanced simulation methods** [2025]  
Samarjeet Prasad, Felix Aviat, James E. Gonzales, Bernard R. Brooks.  
[J. Chem. Phys. (2025)](https://doi.org/10.1063/5.0264937) | [code](https://github.com/samarjeet/apocharmm)  

* **Self-Supervised Evolution Operator Learning for High-Dimensional Dynamical Systems** [2025]  
Giacomo Turri, Luigi Bonati, Kai Zhu, Massimiliano Pontil, Pietro Novelli.  
[arXiv:2505.18671 (2025)](https://doi.org/10.48550/arXiv.2505.18671) | [code](https://github.com/pietronvll/encoderops)  

* **NeuralTSNE: A Python Package for the Dimensionality Reduction of Molecular Dynamics Data Using Neural Networks** [2025]  
Patryk Tajs, Mateusz Skarupski, Jakub Rydzewski.  
[arXiv:2505.16476(2025)](https://doi.org/10.48550/arXiv.2505.16476) | [code](https://github.com/NeuralTSNE/NeuralTSNE)  

* **GEODES: Geometric Descriptors for the Assessment of Global and Local Flexibility of Proteins During Molecular Dynamics Simulation** [2025]  
Pats, Karina and Glukhov, Igor and Petrosian, Stepan and Mamaeva, Maria and Sergushichev, Alexey and Devignes, Marie-Dominique and Molnár, Ferdinand.  
[IEEE Access (2025)](https://doi.org/10.1109/ACCESS.2025.3558781) | [code](https://github.com/rinnifox/GEODES)  

* **gmx_RRCS: a precision tool for detecting subtle conformational dynamics in molecular simulations** [2025]  
Wei Han, Zhenghan Chen, Ming-Wei Wang, Qingtong Zhou.  
[Journal of Molecular Biology (2025)](https://doi.org/10.1016/j.jmb.2025.169129) | [code](https://github.com/RuijinHospitalRCMSB/gmx_RRCS)  

* **Systematic analysis of biomolecular conformational ensembles with PENSA** [2025]  
Vögele, Martin, Neil J. Thomson, Sang T. Truong, Jasper McAvity, Ulrich Zachariae, and Ron O. Dror.  
[The Journal of Chemical Physics 162.1 (2025)](https://doi.org/10.1063/5.0235544) | [code](https://github.com/drorlab/pensa)  

* **MDRefine: a Python package for refining Molecular Dynamics trajectories with experimental data** [2024]  
Ivan Gilardoni, Valerio Piomponi, Thorben Fröhlking, Giovanni Bussi.   
[	arXiv:2411.07798 (2024)](https://arxiv.org/abs/2411.07798) | [code](https://github.com/bussilab/MDRefine)  

* **NRIMD, a Web Server for Analyzing Protein Allosteric Interactions Based on Molecular Dynamics Simulation** [2024]  
He, Yi, Shuang Wang, Shuai Zeng, Jingxuan Zhu, Dong Xu, Weiwei Han, and Juexin Wang.   
[J. Chem. Inf. Model. (2024)](https://doi.org/10.1021/acs.jcim.4c00783) | [web](https://nrimd.luddy.indianapolis.iu.edu/)  





### Reference

https://github.com/ipudu/awesome-molecular-dynamics  



### Visualization

* [VMD](http://www.ks.uiuc.edu/Research/vmd/) - A molecular visualization program for displaying, animating, and analyzing large biomolecular systems using 3-D graphics and built-in scripting.  
* [NGLview](https://github.com/arose/nglview) - IPython widget to interactively view molecular structures and trajectories.  
* [PyMOL](https://pymol.org/2/) - A user-sponsored molecular visualization system on an open-source foundation, maintained and distributed by Schrödinger.  
* [Avogadro](https://avogadro.cc/) - An advanced molecule editor and visualizer designed for cross-platform use in computational chemistry, molecular modeling, bioinformatics, materials science, and related areas.  






## CGMD
**Coarse-Grained Molecular Dynamics Simulations**







* **Light Martini water accelerates sampling in coarse-grained molecular dynamics simulations** [2026]  
Aladdin Elgendy, André P. Zeipelt, Lars V. Schäfer.  
[bioRxiv (2026)](https://doi.org/10.64898/2026.08.03.741232) | [code](https://doi.org/10.17877/RESOLV-2026-MS4UJFFM)  

* **CTGoMartini: A Python Framework for Simulating Biomolecular Conformational Transitions with Gō-Martini Models** [2026]  
Song Yang, Chen Song.  
[bioRxiv (2026)](https://doi.org/10.64898/2026.04.30.721921) | [code](https://github.com/ComputBiophys/CTGoMartini)  

* **Learning chemically transferable protein-protein binding energetics from peptide potential of mean force building blocks** [2026]  
Tariq Shereef, Emiel Kram, Alexander J. Pak.  
[ChemRxiv. (2026)](https://doi.org/10.26434/chemrxiv.15004324/v1) | [code](https://gitlab.com/pak-group/pebble_m01)  

* **StruCloze: A Unified Framework for Backmapping and Inpainting Biomolecule Structures** [2026]  
Junjie Zhu, Zirui Fan, Zhengxin Li, Zhuoqi Zheng, Kresten Lindorff-Larsen, and Hai-Feng Chen.  
[J. Chem. Theory Comput. (2026)](https://doi.org/10.1021/acs.jctc.6c00214) | [code](https://github.com/Junjie-Zhu/StruCloze)  

* **Martini Mapper: An Automated Fragment-Based Mapping Algorithm for Developing Coarse-Grained Models within the Martini 3 Framework** [2026]  
Kevin V. Bigting, Shubhadeep Nag, and Yaxin An.  
[J. Chem. Inf. Model. (2026)](https://doi.org/10.1021/acs.jcim.5c02903) | [code](https://github.com/eliobaby/Martini_mapper)  

* **Probabilistic Forecasting for Coarse-Grained Molecular Dynamics** [2026]  
Luc F. Christians, Anna Wojnar, and Alexander J. Pak.  
[J. Chem. Theory Comput. (2026)](https://doi.org/10.1021/acs.jctc.5c02131) | [code](https://gitlab.com/pak-group/pfcg_m01)  

* **Learning data-efficient coarse-grained molecular dynamics from forces and noise** [2026]  
Durumeric, A.E.P., Chen, Y., Pasos-Trejo, A.S. et al.  
[Nat Commun (2026)](https://doi.org/10.1038/s41467-026-70818-0) | [data](https://zenodo.org/records/18784685)  

* **Probabilistic Forecasting for Coarse-Grained Molecular Dynamics** [2025]  
Christians L, Wojnar A, Pak A.  
[ChemRxiv. (2025)](https://doi.org/10.26434/chemrxiv-2025-vn440)  

* **RNA phase separation with Martini 3** [2025]  
Zhang Q, Valério M, Grünewald L, Borges-Araújo L, Grünewald F, Wang S, et al.  
[ChemRxiv. (2025)](https://doi.org/10.26434/chemrxiv-2025-ggcq2)  

* **An optimized contact map for GōMartini 3 enabling conformational changes in protein assemblies** [2025]  
Gustavo E. Olivos-Ramirez, Luis F. Cofas-Vargas, Siewert J. Marrink, Adolfo B. Poma.  
[bioRxiv. (2025)](https://doi.org/10.1101/2025.11.14.688437) | [code](https://github.com/GoMartini3-tools/ContactFreq)  

* **CGBack: Diffusion Model for Backmapping Large-Scale and Complex Coarse-Grained Molecular Systems** [2025]  
Diego Ugarte La Torre and Yuji Sugita.  
[J. Chem. Inf. Model. (2025)](https://doi.org/10.1021/acs.jcim.5c01281) | [data](https://github.com/genesis-release-r-ccs/cgback)  

* **Data-driven particle dynamics: Structure-preserving coarse-graining for emergent behavior in non-equilibrium systems** [2025]  
Quercus Hernandez, Max Win, Thomas C. O'Connor, Paulo E. Arratia, Nathaniel Trask.  
[arXiv:2508.12569 (2025)](https://doi.org/10.48550/arXiv.2508.12569) | [code](https://github.com/PIMILab/DataDrivenParticleDynamics)  

* **Understanding Viscoelasticity of an Entangled Silicone Copolymer via Coarse-Grained Molecular Dynamics Simulations** [2025]  
Weikang Xian, Amitesh Maiti, Andrew P. Saab, and Ying Li.  
[Macromolecules (2025)](https://doi.org/10.1021/acs.macromol.5c01192)  

* **Navigating protein landscapes with a machine-learned transferable coarse-grained model** [2025]  
Charron, N.E., Bonneau, K., Pasos-Trejo, A.S. et al.  
[Nat. Chem. (2025)](https://doi.org/10.1038/s41557-025-01874-0) | [data](https://github.com/ClementiGroup/mlcg)  

* **Graph-Coarsening for Machine Learning Coarse-grained Molecular Dynamics** [2025]  
Soumya Mondal, Subhanu Halder, Debarchan Basu, Sandeep Kumar, Tarak Karmakar.  
[arXiv:2507.16531 (2025)](https://doi.org/10.48550/arXiv.2507.16531)  

* **Fast parameterization of Martini3 models for fragments and small molecules** [2025]  
Magdalena Szczuka, Gilberto P. Pereira, Luis J. Walter, Marc Gueroult, Pierre Poulain, Tristan Bereau, Paulo C. T. Souza, Matthieu Chavent.  
[bioRxiv (2025)](https://doi.org/10.1101/2025.07.13.664596) | [data](https://github.com/Martini-Force-Field-Initiative/Automartini_M3)  

* **Martini Mapper: An Automated Fragment-Based Framework for Developing Coarse-Grained Models within the Martini 3 Framework** [2025]  
Kevin V. Bigting, Shubhadeep Nag, Yaxin An.  
[arXiv:2511.11859 (2025)](https://doi.org/10.48550/arXiv.2511.11859) | [code](https://github.com/eliobaby/Martini_mapping)  














## AI4MD










* **Seamless QM/MM Simulations via a GROMACS-CP2K Interface** [2026]  
Dmitry Morozov, Christian Blau, Ole Schütt, Vladimir Mironov, Arno Proeme, Holly Judge, Thomas D. Kühne, Berk Hess, Gerrit Groenhof.  
[J. Chem. Inf. Model. (2026)](https://doi.org/10.1021/acs.jcim.6c02073)  

* **Enabling Biomolecular Simulations with Neural Network Potentials in GROMACS** [2026]  
Lukas Müllender, Berk Hess, Erik Lindahl.  
[J. Chem. Theory Comput. (2026)](https://doi.org/10.1021/acs.jctc.6c00808) | [Code](https://github.com/lmuellender/gmx-nnpot-tools) | [Zenodo](https://doi.org/10.5281/zenodo.19663881)  

* **Edge-Aware Graph Attention Networks for Interpreting Biophysical Mechanisms from Molecular Dynamics Simulations** [2026]  
Mohd Ahsan, Chinmai Pindi, Giulia Palermo.  
[bioRxiv (2026)](https://doi.org/10.64898/2026.09.03.749137)  

* **MDArena: Evaluating Coding Agents on Realistic Molecular Dynamics Workflows** [2026]  
Nithishwer Mouroug Anand, Wei-Tse Hsu, Kyle Vaccaro, Eden James Gage, Jonathan David Colburn, Linda Xi Phan, Minjoon Seo, Kevin Guan, Philip C. Biggin.  
[arXiv:2608.02642(2026)](https://doi.org/10.48550/arXiv.2608.02642) | [code](https://github.com/weitse-hsu/MDArena)  

* **Speculative Sampling For Faster Molecular Dynamics** [2026]  
Arthur Kosmala, Stephan Günnemann, Meng Gao, Brandon Wood.  
[arXiv:2606.02455 (2026)](https://doi.org/10.48550/arXiv.2606.02455) | [code](https://github.com/facebookresearch/LSD)  

* **MDForge: Agentic Molecular Dynamics Pipeline Design under Sparse Simulator Feedback** [2026]  
Zehong Wang, Yijun Ma, Connor R. Schmidt, Tianyi Ma, Weixiang Sun, Ziming Li, Xiaoguang Guo, Chuxu Zhang, Matthew J. Webber, Yanfang Ye.  
[arXiv:2606.12916 (2026)](https://doi.org/10.48550/arXiv.2606.12916) | [code](https://github.com/Zehong-Wang/MDForge)  

* **Scaling k-Means for Multi-Million Frames: A Stratified NANI Approach for Large-Scale MD Simulations** [2026]  
herome Brylle Woody Santos, Lexin Chen, and Ramón Alain Miranda-Quintana.  
[J. Chem. Inf. Model. (2026)](https://doi.org/10.1021/acs.jcim.5c02741) | [code](https://github.com/mqcomplab/MDANCE)  

* **QUASAR: A Universal Autonomous System for Atomistic Simulation and a Benchmark of Its Capabilities** [2026]  
Fengxu Yang and Jack D. Evans.  
[J. Chem. Inf. Model. (2026)](https://doi.org/10.1021/acs.jcim.6c00295)  

* **Understanding Adsorption and Reactions at Aqueous Oxide Interfaces with Neural Network Potential Molecular Dynamics** [2026]  
Sanghyun J. Park, Abhinav S. Raman, and Annabella Selloni.  
[Acc. Mater. Res. (2026)](https://doi.org/10.1021/accountsmr.6c00001) | [code](https://github.com/sanghyunjonathan/Methanol-Adsorbed-TiO2-Interface)  

* **Force-free molecular dynamics through autoregressive equivariant networks** [2026]  
Thiemann, F.L., Reschützegger, T., Esposito, M. et al.  
[Nat Mach Intell (2026)](https://doi.org/10.1038/s42256-026-01227-7) | [code](http://github.com/IBM/trajcast)  

* **Machine learning enabled molecular dynamics-Monte Carlo framework for nanoconfined fluid adsorption** [2026]  
Liu, J., Chen, G., He, S. et al.  
[Commun Chem (2026)](https://doi.org/10.1038/s42004-026-02053-z) | [Zenodo](https://zenodo.org/records/19488275)  

* **Learning Structure, Energy, and Dynamics: A Survey of Artificial Intelligence for Protein Dynamics** [2026]  
Haocheng Tang, Liang Shi, Ya-Shi Zhang, Xixian Liu, Jian Tang, Jiarui Lu.  
[arXiv:2604.25244 (2026)](https://doi.org/10.48550/arXiv.2604.25244)  

* **Faster Molecular Dynamics with Neural Network Potentials via Distilled Multiple Time-Stepping and Non-Conservative Forces** [2026]  
Nicolaï Gouraud, Côme Cattin, Thomas Plé, Olivier Adjoua, Louis Lagardère, Jean-Philip Piquemal.  
[J. Chem. Theory Comput.(2026)](https://doi.org/10.1021/acs.jctc.6c00653) | [arXiv:2602.14975 (2026)](https://doi.org/10.48550/arXiv.2602.14975) | [code](https://github.com/FeNNol-tools/FeNNol)  

* **Transferable generative models bridge femtosecond to nanosecond time-step molecular dynamics** [2026]  
Juan Viguera Diez et al.  
[Sci. Adv.12,eaed2333(2026)](https://doi.org/10.1126/sciadv.aed2333) | [code](https://github.com/olsson-group/tito)  

* **MDAgent2: Large Language Model for Code Generation and Knowledge Q&A in Molecular Dynamics** [2026]  
Zhuofan Shi, Hubao A, Yufei Shao, Mengyan Dai, Yadong Yu, Pan Xiang, Dongliang Huang, Hongxu An, Chunxiao Xin, Haiyang Shen, Zhenyu Wang, Yunshan Na, Gang Huang, Xiang Jing.  
[arXiv:2601.02075 (2026)](https://doi.org/10.48550/arXiv.2601.02075) | [code](https://github.com/FredericVAN/PKU_MDAgent2)  

* **LAMMPS-ANI: Large Scale Molecular Dynamics Simulations with ANI Neural Network Potential** [2025]  
Xue J, Terrel N, Pickering I, Roitberg A.  
[ChemRxiv. (2025)](https://doi.org/10.26434/chemrxiv-2025-8v03m) | [code](https://github.com/roitberg-group/lammps-ani)  

* **Data-driven enhanced sampling of mechanistic pathways** [2025]  
R. Elangovan,S. Chatterjee, & D. Ray.  
[Proc. Natl. Acad. Sci. (2025)](https://doi.org/10.1073/pnas.2517169122) | [code](https://github.com/Revanth27-08/Multitask_MFEP)  

* **Machine learning driven advances in molecular dynamics of bulk and interfacial aqueous systems** [2025]  
Wang R, Meraz VJ, Tiwary P.  
[ChemRxiv. (2025)](https://doi.org/10.26434/chemrxiv-2025-6vdl2-v2)  

* **Hierarchical geometric deep learning enables scalable analysis of molecular dynamics** [2025]  
Zihan Pengmei, Spencer C. Guo, Chatipat Lorpaiboon, Aaron R. Dinner.  
[arXiv:2512.06520(2025)](https://doi.org/10.48550/arXiv.2512.06520) | [code](https://github.com/dinner-group/geom2vec)  

* **Accelerating Molecular Dynamics Simulations with Foundation Neural Network Models using Multiple Time-Step and Distillation** [2025]  
Côme Cattin, Thomas Plé, Olivier Adjoua, Nicolaï Gouraud, Louis Lagardère, Jean-Philip Piquemal.  
[arXiv:2510.06562 (2025)](https://doi.org/10.48550/arXiv.2510.06562)  

* **MOLECULE: Molecular-dynamics and Optimized deep Learning for Entropy-regularized Classification and Uncertainty-aware Ligand Evaluation** [2025]  
Ivan Cucchi, Elena Frasnetti, Francesco Frigerio, Fabrizio Cinquini, Silvia Pavoni, Luca F. Pavarino, and Giorgio Colombo.  
[J. Chem. Theory Comput. (2025)](https://doi.org/10.1021/acs.jctc.5c01140)  

* **NVNMD-v2: Scalable and Accurate Deep Learning Molecular Dynamics Model Based on Non-Von Neumann Architectures** [2025]  
Xiaoyun Yu, Guang Yang, Zhuoying Zhao, Junhua Li, Xinyu Xiao, Xin Zhang, Jie Liu, and Pinghui Mo.  
[J. Chem. Theory Comput. (2025)](https://doi.org/10.1021/acs.jctc.5c01050) | [code](https://github.com/LiuGroupHNU/deepmd-kit)  

* **TorchSim: An efficient atomistic simulation engine in PyTorch** [2025]  
Orion Cohen, Janosh Riebesell, Rhys Goodall, Adeesh Kolluru, Stefano Falletta, Joseph Krause, Jorge Colindres, Gerbrand Ceder, Abhijeet S. Gangan.  
[arXiv:2508.06628 (2025)](https://doi.org/10.48550/arXiv.2508.06628) | [code](https://github.com/Radical-AI/torch-sim)  

* **TorchSim: An efficient atomistic simulation engine in PyTorch** [2025]  
Orion Cohen, Janosh Riebesell, Rhys Goodall, Adeesh Kolluru, Stefano Falletta, Joseph Krause, Jorge Colindres, Gerbrand Ceder, Abhijeet S. Gangan.  
[arXiv:2508.06628 (2025)](https://doi.org/10.48550/arXiv.2508.06628) | [code](https://github.com/Radical-AI/torch-sim)  

* **chemtrain-deploy: A parallel and scalable framework for machine learning potentials in million-atom MD simulations** [2025]  
Paul Fuchs, Weilong Chen, Stephan Thaler, Julija Zavadlav.  
[J. Chem. Theory Comput. (2025)](https://doi.org/10.1021/acs.jctc.5c00996) | [arXiv:2506.04055 (2025)](https://doi.org/10.48550/arXiv.2506.04055) | [data](https://github.com/tummfm/chemtrain)  

* **Action-Minimization Meets Generative Modeling: Efficient Transition Path Sampling with the Onsager-Machlup Functional** [2025]  
Sanjeev Raja, Martin Šípka, Michael Psenka, Tobias Kreiman, Michal Pavelka, Aditi S. Krishnapriyan.  
[ICML 2025 (2025)](https://arxiv.org/abs/2504.18506) | [data](https://github.com/ASK-Berkeley/OM-TPS)  

* **Operator Forces For Coarse-Grained Molecular Dynamics** [2025]  
Leon Klein, Atharva Kelkar, Aleksander Durumeric, Yaoyi Chen, Frank Noé.  
[arXiv:2506.19628 (2025)](https://doi.org/10.48550/arXiv.2506.19628) | [data](https://github.com/noegroup/OperatorForces4CG)  

* **Memory kernel minimization-based neural networks for discovering slow collective variables of biomolecular dynamics** [2025]  
Liu, B., Cao, S., Boysen, J.G. et al.  
[Nat Comput Sci (2025)](https://doi.org/10.1038/s43588-025-00815-8) | [code](https://github.com/markovmodel/mdshare)  

* **UniSim: A Unified Simulator for Time-Coarsened Dynamics of Biomolecules** [2025]  
Ziyang Yu, Wenbing Huang, Yang Liu.  
[ICML 2025 (2025)](https://doi.org/10.48550/arXiv.2506.03157) | [code](https://github.com/yaledeus/UniSim) | [data](https://zenodo.org/records/15394209)  

* **FlashMD: long-stride, universal prediction of molecular dynamics** [2025]  
Bigi, Filippo, Sanggyu Chong, Agustinus Kristiadi, and Michele Ceriotti.  
[arXiv:2505.19350 (2025)](https://arxiv.org/abs/2505.19350) | [code](https://github.com/lab-cosmo/flashmd)  

* **Investigating the Nature of PRM:SH3 Interactions Using Artificial Intelligence and Molecular Dynamics** [2025]  
Se-Jun Kim, Da-Eun Hwang, Hyungjun Kim, and Jeong-Mo Choi.  
[J. Chem. Inf. Model. (2025)](https://doi.org/10.1021/acs.jcim.5c00342) | [code](https://github.com/sejunkim6370/AlphaFold2-and-Molecular-Dynamics)  

* **Towards Unraveling Biomolecular Conformational Landscapes with a Generative Foundation Model** [2025]  
The OpenComplex Team, Qiwei Ye.  
[bioRxiv. (2025)](https://doi.org/10.1101/2025.05.01.651643)  

* **Deep Signature: Characterization of Large-Scale Molecular Dynamics** [2025]  
Tiexin Qin, Mengxu ZHU, Chunyang Li, Terry Lyons, Hong Yan, Haoliang Li.  
[ICLR (2025)](https://openreview.net/forum?id=xayT1nn8Mg) | [code](https://github.com/WonderSeven/Deep-Signature)  

* **A Foundation Model for Accurate Atomistic Simulations in Drug Design** [2025]  
Plé T, Adjoua O, Benali A, Posenitskiy E, Villot C, Lagardère L, et al.  
[ChemRxiv. (2025)](https://doi.org/10.26434/chemrxiv-2025-f1hgn) | [code](https://github.com/thomasple/FeNNol-PMC)  

* **Orb-v3: atomistic simulation at scale** [2025]  
Benjamin Rhodes, Sander Vandenhaute, Vaidotas Šimkus, James Gin, Jonathan Godwin, Tim Duignan, Mark Neumann.  
[arXiv:2504.06231 (2025)](https://arxiv.org/abs/2504.06231) | [code](https://github.com/orbital-materials/orb-models)  

* **A predictive machine learning force-field framework for liquid electrolyte development** [2025]  
Gong, S., Zhang, Y., Mu, Z. et al.  
[Nat Mach Intell (2025)](https://doi.org/10.1038/s42256-025-01009-7) | [code](https://github.com/bytedance/bamboo)  

* **Fast, Modular, and Differentiable Framework for Machine Learning-Enhanced Molecular Simulations** [2025]  
Henrik Christiansen, Takashi Maruyama, Federico Errica, Viktor Zaverkin, Makoto Takamoto, Francesco Alesiani.  
[arXiv:2503.20541 (2025)](https://arxiv.org/abs/2503.20541) | [code](https://github.com/nec-research/DIMOS)  

* **Kinetically Consistent Coarse Graining using Kernel-based Extended Dynamic Mode Decomposition** [2025]  
Vahid Nateghi, Feliks Nüske.   
[arXiv:2409.16396 (2025)](https://arxiv.org/abs/2409.16396) | [code](https://zenodo.org/records/13808938)  

* **Advancing nonadiabatic molecular dynamics simulations in solids with E(3) equivariant deep neural hamiltonians** [2025]  
Zhang, C., Zhong, Y., Tao, ZG. et al.   
[Nat Commun 16, 2033 (2025)](https://doi.org/10.1038/s41467-025-57328-1) | [code](https://github.com/QuantumLab-ZY/HamGNN)  

* **BoostMD: Accelerated Molecular Sampling Leveraging ML Force Field Features** [2024]  
Schaaf, Lars Leon, Ilyes Batatia, Jules Tilly, and Thomas D. Barrett.   
[NeurIPS 2024 Workshop on Data-driven and Differentiable Simulations, Surrogates, and Solvers. (2024)](https://openreview.net/forum?id=H0USH61HnF)  

* **A Multi-Grained Symmetric Differential Equation Model for Learning Protein-Ligand Binding Dynamics** [2024]  
Shengchao Liu, Weitao Du, Hannan Xu, Yanjing Li, Zhuoxinran Li, Vignesh Bhethanabotla, Divin Yan, Christian Borgs, Anima Anandkumar, Hongyu Guo, Jennifer Chayes.   
[arXiv:2401.15122 (2024)](https://arxiv.org/abs/2401.15122) | [code](https://github.com/chao1224/NeuralMD)  

* **Accelerating Molecular Dynamics Simulations with Quantum Accuracy by Hierarchical Classification** [2024]  
Brunken, Christoph, Sebastien Boyer, Mustafa Omar, Bakary N'tji Diallo, Karim Beguir, Nicolas Lopez Carranza, and Oliver Bent.   
[ChemRxiv. (2024)](https://doi.org/10.26434/chemrxiv-2024-20q1v) | [code](https://github.com/multiscale-modelling/humf)  

* **Machine learning of force fields towards molecular dynamics simulations of proteins at DFT accuracy** [2024]  
Brunken, Christoph, Sebastien Boyer, Mustafa Omar, Bakary N'tji Diallo, Karim Beguir, Nicolas Lopez Carranza, and Oliver Bent.   
[ICLR 2024 Workshop on Generative and Experimental Perspectives for Biomolecular Design (2024)](https://openreview.net/forum?id=hrvvIOx7EM) | [code](https://github.com/ACEsuit/mace-jax)  

* **Unsupervised and supervised AI on molecular dynamics simulations reveals complex characteristics of HLA-A2-peptide immunogenicity** [2024]  
Jeffrey K Weber, Joseph A Morrone, Seung-gu Kang, Leili Zhang, Lijun Lang, Diego Chowell, Chirag Krishna, Tien Huynh, Prerana Parthasarathy, Binquan Luan, Tyler J Alban, Wendy D Cornell, Timothy A Chan.   
[Briefings in Bioinformatics (2024)](https://doi.org/10.1093/bib/bbad504) | [code](https://github.com/BiomedSciAI)

* **Biomolecular dynamics with machine-learned quantum-mechanical force fields trained on diverse chemical fragments** [2024]  
Unke, Oliver T., Martin Stöhr, Stefan Ganscha, Thomas Unterthiner, Hartmut Maennel, Sergii Kashubin, Daniel Ahlin et al.   
[Science Advances 10.14 (2024)](https://www.science.org/doi/10.1126/sciadv.adn4397) | [data](https://zenodo.org/records/10720941)

* **DeePMD-kit v2: A software package for deep potential models** [2023]  
Zeng, Jinzhe, Duo Zhang, Denghui Lu, Pinghui Mo, Zeyu Li, Yixiao Chen, Marián Rynik et al.   
[The Journal of Chemical Physics 159.5 (2023)](https://doi.org/10.1063/5.0155600) | [code](https://github.com/deepmodeling/deepmd-kit)  

* **Enhancing Biomolecular Sampling with Reinforcement Learning: A Tree Search Molecular Dynamics Simulation Method** [2019]  
Kento Shin, Duy Phuoc Tran, Kazuhiro Takemura, Akio Kitao, Kei Terayama, and Koji Tsuda.   
[ACS Omega (2019)](https://doi.org/10.1021/acsomega.9b01480) | [code](https://github.com/tsudalab/TSMD)  

* **DeePMD-kit: A deep learning package for many-body potential energy representation and molecular dynamics** [2018]  
Wang, Han, Linfeng Zhang, Jiequn Han, and E. Weinan.   
[Computer Physics Communications 228 (2018)](https://doi.org/10.1016/j.cpc.2018.03.016) | [code](https://github.com/deepmodeling/deepmd-kit)  














### Neural Network Potentials







* **Physics-Aligned Electronic Ground-State Learning Improves Generalization** [2026]  
Eike S. Eberhard, Xaver Kainz, Viktor Kotsev, Abdulrahman Aldossary, Stephan Günnemann.  
[arXiv:2610.10298(2026)](https://doi.org/10.48550/arXiv.2610.10298) | [Code](https://github.com/ESEberhard/ML4DFT)  

* **Enabling Biomolecular Simulations with Neural Network Potentials in GROMACS** [2026]  
Lukas Müllender, Berk Hess, Erik Lindahl.  
[J. Chem. Theory Comput. (2026)](https://doi.org/10.1021/acs.jctc.6c00808) | [Code](https://github.com/lmuellender/gmx-nnpot-tools) | [Zenodo](https://doi.org/10.5281/zenodo.19663881)  

* **Train for Accuracy, Execute at Scale: Architecture-Preserving Inference for Equivariant Atomistic Foundation Models** [2026]  
Lei Fu, Zihui Feng, Yongheng Li, Hongwei Du, Xin He, Junyi Wu, Kejie Bao, Yueyu Zhang, Zeyu Deng, Ziheng Lu, Bonan Zhu.  
[arXiv:2610.01036 (2026)](https://doi.org/10.48550/arXiv.2610.01036) | [Code](https://github.com/bonan-group/symmetrix-xl)  

* **Dielectric Response of Short and Long Range Models of Nonuniform Liquids and Implications for Machine Learned Interatomic Potentials** [2026]  
Atul C. Thakur, Harender S. Dhattarwal, Richard C. Remsing.  
[arXiv:2610.04224 (2026)](https://doi.org/10.48550/arXiv.2610.04224)  

* **Leveraging Machine Learning Interatomic Potentials into Fitting Fast and Accurate AMBER-Compatible Precise Force Field** [2026]  
Xuchao Zhou, Xujian Wang, Jiahao Xie, et al.  
[ChemRxiv. (2026)](https://doi.org/10.26434/chemrxiv.15008812/v1) | [code](https://github.com/ClickFF/MAPLE) | [Zenodo](https://doi.org/10.5281/zenodo.21428725)  

* **Advancing density functional tight-binding method for large organic molecules through equivariant neural networks** [2026]  
Leonardo Medrano Sandonas, Mirela Puleva, Zekiye Erarslan, Ricardo Parra Payano, Martin Stöhr, Gianaurelio Cuniberti, Alexandre Tkatchenko.  
[Phys. Chem. Chem. Phys.(2026)](https://doi.org/10.1039/d6cp00038j) | [Code](https://github.com/lmedranos/EquiDTB)  

* **El Agente Potente: High-Throughput Agentic Atomistic Simulations** [2026]  
Tsz Wai Ko, Jiaru Bai, Thomas Swanick, Yeonghun Kang, Changhyeok Choi, Angelina Qihong Jiang, Aiwei Yin, Varinia Bernales, Alán Aspuru-Guzik.  
[arXiv:2609.14840 (2026)](https://doi.org/10.48550/arXiv.2609.14840)  

* **Universal Thermodynamic Interatomic Potentials for Crystalline Materials** [2026]  
Juno Nam, Bowen Deng, Xiaochen Du, Luis Barroso-Luque, Benjamin Kurt Miller, Rafael Gómez-Bombarelli.  
[arXiv:2608.14502 (2026)](https://doi.org/10.48550/arXiv.2608.14502)  

* **GRACE-OFF: A Machine-Learned Interatomic Potential for Organic Liquids Using the GRACE Architecture** [2026]  
Anna Katharina Picha, Johannes Karwounopoulos, Linus C. Erhard, Stefan Boresch, Esther Heid.  
[J. Chem. Theory Comput. (2026)](https://doi.org/10.1021/acs.jctc.6c01169) | [Code](https://github.com/heid-lab/grace-off/)  

* **pdb2reaction: End-to-End Reaction-Path Elucidation from PDB Structures Using Machine-Learning Interatomic Potentials** [2026]  
Takuto Ohmura, Hajime Sato, Tohru Terada.  
[ChemRxiv. (2026)](https://doi.org/10.26434/chemrxiv.15003538/v2) | [Code](https://github.com/t-0hmura/pdb2reaction)  

* **Quantum-accurate atomistic modeling of enzyme catalysis using a machine learned potential** [2026]  
Meng Gao, Armin Shayesteh Zadeh, Aniruddha Seal, Siva Dasetty, Siddarth K. Achar, Misko Dzamba, Benjamin K. Miller, Leif D. Jacobson, C. Lawrence Zitnick, Brandon M. Wood, Zachary W. Ulissi, Daniel S. Levine, Andrew L. Ferguson.  
[arXiv:2609.09293(2026)](https://doi.org/10.48550/arXiv.2609.09293) | [Code](https://github.com/facebookresearch/fairchem)  

* **MLIP Detective: Active Failure Mode Discovery Beyond Benchmark Scores for Machine-Learning Interatomic Potentials** [2026]  
Ryuhei Okuno, Nontawat Charoenphakdee, Kaoru Hisama, Yuta Tsuboi.  
[arXiv:2609.08399 (2026)](https://doi.org/10.48550/arXiv.2609.08399)  

* **AdaptNTK: Adaptive Uncertainty Quantification and Active Learning for Neural Network Potentials** [2026]  
Prajwal Ananth, Shuwen Yue.  
[arXiv:2609.00488(2026)](https://doi.org/10.48550/arXiv.2609.00488)  

* **Atomistic machine learning with irreducible Cartesian natural tensors** [2026]  
Chen, Q., Pattamatta, A.S.L.S., Wang, B. et al.  
[Nat Commun (2026)](https://doi.org/10.1038/s41467-026-77263-z) | [Code](https://github.com/wengroup/carnet)  

* **Accurate and Transferable Intermolecular Potential Based on Machine-Learned Molecular Electron Density** [2026]  
Dahvyd Wing, Mihail Bogojeski, Szabolcs Goger, Klaus-Robert Müller, Alexandre Tkatchenko.  
[arXiv:2608.20753 (2026)](https://doi.org/10.48550/arXiv.2608.20753)  

* **Exploring Conformational Transitions of Adenine RNA Dimer via Machine Learning Potentials** [2026]  
Leonardo Medrano Sandonas, Macarena Tolmos Nehme, Luis Fernando Cofas-Vargas, Gustavo E. Olivos-Ramirez, Gianaurelio Cuniberti, Simón Poblete, Adolfo B. Poma.  
[J. Chem. Theory Comput.(2026)](https://doi.org/10.1021/acs.jctc.6c01213) | [Zenodo](https://doi.org/10.5281/zenodo.20838383)  

* **Quantum machine learning interatomic potential: Application of variational quantum algorithm** [2026]  
Kohei Numata, Wataru Mizukami, Kosuke Mitarai, Keisuke Fujii, Yutaka Imamura.  
[arXiv:2607.27841 (2026)](https://doi.org/10.48550/arXiv.2607.27841)  

* **Chemical intuition on bond-dissociation energies as an emergent ability of universal machine-learning interatomic potentials** [2026]  
Hattori, S., Shimamura, K., Nomura, Ki. et al..  
[Nat Commun (2026)](https://doi.org/10.1038/s41467-026-74919-8) | [code](https://doi.org/10.5281/zenodo.20264297) | [Zenodo](https://doi.org/10.5281/zenodo.20264297)  

* **Reaction Pathway Detection using Machine-Learned Energy Potentials -- Decomposition of Energized CF3CHOO** [2026]  
Cangtao Yin, Markus Meuwly.  
[arXiv:2607.06380 (2026)](https://doi.org/10.48550/arXiv.2607.06380)  

* **Dyna-Mat: End-to-end benchmarking of foundation machine learning interatomic potentials in finite-temperature ensembles** [2026]  
Gawkowski, M.J., Artrith, N., Bonfanti, S., Gangan, A., Heenen, H.H., Kioseoglou, J., Lonvcari'c, I., Myneni, H., Riebesell, J., Rossi, M., Rupp, M., Schmidt, J., Sharma, S., Shi, B.X., Wadowski, A., Hormann, L., & Kapil, V.  
[arXiv:2607.03433 (2026)](https://doi.org/10.48550/arXiv.2607.03433)  

* **Machine learning potentials for modeling alloys across compositions** [2026]  
Killian Sheriff et al.  
[Sci. Adv. (2026)](https://doi.org/10.1126/sciadv.aea9951) | [code](https://github.com/killiansheriff/ChemicalMotifIdentifier) | [Zenodo](https://doi.org/10.5281/zenodo.16129603)  

* **Replacing Quantum Chemistry With Machine-Learned Interatomic Potentials: Revolution or Evolution?** [2026]  
Andrew J. Medford and David S. Sholl.  
[ACS Cent. Sci.(2026)](https://doi.org/10.1021/acscentsci.6c00615)  

* **Bias in Universal Machine-Learned Interatomic Potentials and Its Effects on Fine-Tuning** [2026]  
Nicolas H. Wong and Julia H. Yang.  
[J. Chem. Theory Comput. (2026)](https://doi.org/10.1021/acs.jctc.6c00425) | [code](https://github.com/YangLab-GT/umlip_bias_finetuning)  

* **Universal Interatomic Potentials as Configuration-Space Generators for One-Shot and Iterative Fine-Tuning of Ab Initio-Accurate Material-Specific Models** [2026]  
Jonas Hänseroth, Aaron Flötotto, Christian Dreßler.  
[arXiv:2606.23214 (2026)](https://doi.org/10.48550/arXiv.2606.23214) | [code](https://github.com/microsoft/mattersim) | [Zenodo](https://zenodo.org/records/20792778)  

* **Leveraging neural network interatomic potentials for a foundation model of chemistry** [2026]  
Kim, S.Y., Park, Y.J. & Li, J.  
[npj Comput Mater (2026)](https://doi.org/10.1038/s41524-026-02167-x) | [code](https://github.com/parkyjmit/HackNIP)  

* **How Long Is Long Enough? Extrapolation of Machine-Learning Interatomic Potentials for Oligomeric and Polymeric Systems** [2026]  
Natalie E. Hooven, Arthur Y. Lin, Charles H. Carroll, and Rose K. Cersonsky.  
[J. Chem. Theory Comput. (2026)](https://doi.org/10.1021/acs.jctc.6c00365) | [code](https://doi.org/10.5281/zenodo.17227874)  

* **Angular relational knowledge distillation of machine learning interatomic potentials for scalable catalyst exploration** [2026]  
Natalie E. Hooven, Arthur Y. Lin, Charles H. Carroll, and Rose K. Cersonsky.  
[J. Chem. Theory Comput. (2026)](https://doi.org/10.1021/acs.jctc.6c00365) | [code](https://doi.org/10.5281/zenodo.17227874)  

* **Fine-tuning MLIP foundation models: strategies for accuracy and transferability** [2026]  
Tamás Lajos Tompa, Eszter Varga-Umbrich, Ilyes Batatia, Alin M. Elena, Noam Bernstein, Gábor Csányi.  
[arXiv:2606.12704 (2026)](https://doi.org/10.48550/arXiv.2606.12704)  

* **Angular relational knowledge distillation of machine learning interatomic potentials for scalable catalyst exploration** [2026]  
Lim, H., Choung, S., Moon, J. et al.  
[npj Comput Mater 12, 193 (2026)](https://doi.org/10.1038/s41524-026-02062-5) | [code](https://github.com/hyukjunlim/ARK)  

* **Transferable Machine Learning of Electronic Hamiltonians with Superposition-of-Atomic-Potentials Features** [2026]  
Chaoqun Zhang, Christian Venturella, Enzhi Chen, Tianyu Zhu.  
[arXiv:2606.12326 (2026)](https://doi.org/10.48550/arXiv.2606.12326)  

* **Six Open Questions in Machine-Learned Interatomic Potential Foundation Models** [2026]  
Isabel Creed, Tim Rein, Ingvars Vitenburgs, Wojciech G. Stark, Viktor Ellingsson, Ahmed Y. Ismail, Guangyu Liu, Yuchen Lou, Bradley A. A. Martin, Cyprien Bone, Matthew A. H. Walker, Mueen Taj, Shirui Wang, Kelvin Wong, Ruiqi Wu, Prakriti Kayastha, Bingqing Cheng, Aditi Krishnapriyan, Michele Ceriotti, Marcel F. Langer, Jarvist Moore Frost, Alex M. Ganose, Venkat Kapil, Keith T. Butler.  
[arXiv:2606.07327 (2026)](https://doi.org/10.48550/arXiv.2606.07327)  

* **Accuracy and Efficiency Benchmarks of Pretrained Machine Learning Potentials for Molecular Simulations** [2026]  
Peter Eastman, Evan Pretti, and Thomas E. Markland.  
[J. Chem. Theory Comput.(2026)](https://doi.org/10.1021/acs.jctc.6c00130) | [code](https://github.com/peastman/mlipbenchmarks)  

* **Transferable Neural Network Potential for Elastic and Vibrational Properties of Carbon, Hydrogen, Oxygen, and Nitrogen-Based Two Dimensional Covalent Organic Frameworks** [2026]  
Yunrui Yan, Somayeh Faraji, and Mingjie Liu.  
[Chem. Mater. (2026)](https://doi.org/10.1021/acs.chemmater.6c00169)  

* **Fast training of bespoke SMIRNOFF-format molecular mechanics force fields using machine learning potentials** [2026]  
Finlay Clark, Thomas Pope, Sarah Maier, et al.  
[ChemRxiv. (2026)](https://doi.org/10.26434/chemrxiv.15004169/v1) | [code](https://github.com/cole-group/presto)  

* **DPA4: Pushing the Accuracy-Cost Frontier of Interatomic Potentials with EMFA SO(2) Convolution** [2026]  
Tiancheng Li, Wentao Li, Anyang Peng, Jianming Xue, Linfeng Zhang, Duo Zhang, Han Wang.  
[arXiv:2606.02419 (2026)](https://doi.org/10.48550/arXiv.2606.02419) | [code](https://github.com/deepmodeling/deepmd-kit)  

* **Understanding Adsorption and Reactions at Aqueous Oxide Interfaces with Neural Network Potential Molecular Dynamics** [2026]  
Sanghyun J. Park, Abhinav S. Raman, and Annabella Selloni.  
[Acc. Mater. Res. (2026)](https://doi.org/10.1021/accountsmr.6c00001) | [code](https://github.com/sanghyunjonathan/Methanol-Adsorbed-TiO2-Interface)  

* **Benchmarking machine-learned interatomic potentials for molecular infrared spectroscopy** [2026]  
Nitik Bhatia, Ondrej Krejci, Patrick Rinke.  
[arXiv:2605.22367 (2026)](https://doi.org/10.48550/arXiv.2605.22367) | [code](https://gitlab.com/cest-group/ml4ir-bench)  

* **Machine Learning Interatomic Potentials: Advancing Open-Source Software for Efficient and Scalable Molecular Simulation** [2026]  
Christoph Brunken, Titouan Cormier, Lucien Walewski, Marco Carobene, Yessine Khanfir, Zachary Weller-Davies, Miguel Bragança, Armand Picard, Adrien Pichard, Leon Wehrhan, Heloise Chomet, Eszter Varga-Umbrich, Marie Bluntzer, Massimo Bortone, Valentin Heyraud, Silvia Acosta-Gutiérrez, Jules Tilly, Olivier Peltre.  
[arXiv:2605.22698 (2026)](https://doi.org/10.48550/arXiv.2605.22698) | [code](https://huggingface.co/collections/InstaDeepAI/ml-interatomic-potentials)  

* **Reweighting free energy profiles between universal machine learning interatomic potentials for fast consensus building** [2026]  
Sauradeep Majumdar, Miguel Steiner, Johannes C. B. Dietschreit, Swagata Roy, Daniel Willimetz, Lukaš Grajciar, Rafael Gómez-Bombarelli.  
[arXiv:2605.15630 (2026)](https://doi.org/10.48550/arXiv.2605.15630) | [code](https://github.com/sauradeep93/Reweighting-free-energies) | [Zenodo](https://zenodo.org/records/20142456)  

* **MLIP-Enhanced Thermochemistry Predictions across Organic Chemical Space** [2026]  
Rishabh Dey, Salvina Sharipova, Konstantin Popov.  
[ChemRxiv. (2026)](https://doi.org/10.26434/chemrxiv.15003003/v2) | [code](https://github.com/chimie-paristech-CTM/ThermoMLIP)  

* **All-atomistic Transferable Neural Potentials for Protein Solvation** [2026]  
Rishabh Dey, Salvina Sharipova, Konstantin Popov.  
[arXiv:2605.14584 (2026)](https://doi.org/10.48550/arXiv.2605.14584)  

* **Systematic Fine-Tuning of MACE Interatomic Potentials for Catalysis** [2026]  
Nima Karimitari, Jacob Clary, Derek Vigil-Fowler, Ravishankar Sundararaman, Gábor Csányi, Christopher Sutton.  
[arXiv:2605.09394 (2026)](https://doi.org/10.48550/arXiv.2605.09394) | [Zenodo](https://doi.org/10.5281/zenodo.20043317)  

* **Integrating Machine Learning Interatomic Potentials with MMPBSA for Accurate Protein–Ligand Binding Free Energy Calculations** [2026]  
Wei, Xue-Xin, Yuxinxin Chen, Yuedong Yang, Mingyuan Xu, Pavlo O. Dral, and Hongming Chen.  
[J. Phys. Chem. B (2026)](https://doi.org/10.1021/acs.jpcb.6c00306) | [code](https://github.com/XueXinWei-AI4S/AIQM-PBSA)  

* **AiiDA-TrainsPot: towards automated training of neural-network interatomic potentials** [2026]  
Bidoggia, Davide and Manko, Nataliia and Peressi, Maria and Marrazzo, Antimo.  
[Digital Discovery (2026)](https://doi.org/10.1039/D6DD00005C) | [code](https://github.com/aiida-trieste-developers/aiida-trains-pot)  

* **Platonic representation of foundation machine learning interatomic potentials** [2026]  
Li, Z., Walsh, A.  
[Nat Mach Intell (2026)](https://doi.org/10.1038/s42256-026-01235-7) | [code](https://github.com/WMD-group/PlatonicRep)  

* **Evaluating mechanical property prediction across material classes using molecular dynamics simulations with universal machine-learned interatomic potentials** [2026]  
Stracke, K., Edwards, C.W. & Evans, J.D.  
[Commun Chem (2026)](https://doi.org/10.1038/s42004-026-02057-9) | [Zenodo](https://zenodo.org/records/17730689)  

* **Knowing when to trust machine-learned interatomic potentials** [2026]  
Shams Mehdi, Ilkwon Cho, Olexandr Isayev.  
[arXiv:2605.00640 (2026)](https://doi.org/10.48550/arXiv.2605.00640) | [code](https://github.com/isayevlab/PROBE)  

* **Anchor-Based Relative Free Energy Simulations using Machine-Learned Interatomic Potentials** [2026]  
Anna Katharina Picha, Stefan Boresch.  
[ChemRxiv (2026)](https://doi.org/10.26434/chemrxiv.15001438/v1) | [code](https://github.com/cbc-univie/anchor-4D)  

* **Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry** [2026]  
Connor W. Edwards, Jack D. Evans.  
[arXiv:2604.25262 (2026)](https://doi.org/10.48550/arXiv.2604.25262) | [code](https://doi.org/10.25909/32061111)  

* **Faster Molecular Dynamics with Neural Network Potentials via Distilled Multiple Time-Stepping and Non-Conservative Forces** [2026]  
Nicolaï Gouraud, Côme Cattin, Thomas Plé, Olivier Adjoua, Louis Lagardère, Jean-Philip Piquemal.  
[J. Chem. Theory Comput.(2026)](https://doi.org/10.1021/acs.jctc.6c00653) | [arXiv:2602.14975 (2026)](https://doi.org/10.48550/arXiv.2602.14975) | [code](https://github.com/FeNNol-tools/FeNNol)  

* **Generalization of long-range machine learning potentials in complex chemical spaces** [2026]  
Sanocki, M. and Zavadlav, J..  
[Digital Discovery (2026)](https://doi.org/10.1039/D5DD00570A) | [code](https://github.com/msan9908/MLIP_generalizability)  

* **Machine-Learned Electrostatic Potentials for Accurate Hydration Free Energy Calculations** [2026]  
Mathias Hilfiker, Leonardo Medrano Sandonas, Alexandre Tkatchenko, Ola Engkvist, and Marco Klähn.  
[J. Chem. Theory Comput. (2026)](https://doi.org/10.1021/acs.jctc.5c02086) | [code](https://github.com/mathilfiker/ml_for_charges)  

* **Extending AIMNet2 to Macrocyclic Peptides Through Data-Efficient Continual Training** [2026]  
Runtian Gao, Roman Zubatyuk, Olexandr Isayev.  
[ChemRxiv. (2026)](https://doi.org/10.26434/chemrxiv.15002334/v1)  

* **MolCryst-MLIPs: A Machine-Learned Interatomic Potentials Database for Molecular Crystals** [2026]  
Lahouari, Adam, Shen Ai, Jihye Han, Jillian Hoffstadt, Philipp Hoellmer, Charlotte Infante, Pulkita Jain et al.  
[arXiv:2604.13897 (2026)](https://doi.org/10.48550/arXiv.2604.13897) | [code](https://github.com/adamlaho/MolCryst)  

* **Quantum-Accurate Enhanced Sampling and Mini-Protein Folding through Replica Exchange for Multiscale Neural Network Potentials** [2026]  
Riccardo Solazzo, Igor Gordiy, Sereina Riniker.  
[ChemRxiv (2026)](https://doi.org/10.26434/chemrxiv.15001723/v1) | [code](https://github.com/rinikerlab/rest2_ampmm)  

* **Performance-Based Selection of Machine Learning Interatomic Potentials for Studying Solid-State Electrolytes** [2026]  
Donghee Chang, Amir Taqieddin, and Forrest Laskowski.  
[Chem. Mater. (2026)](https://doi.org/10.1021/acs.chemmater.5c02352)  

* **Importance of Electronic Entropy for Machine Learning Interatomic Potentials** [2026]  
Martin Hoffmann Petersen, Steen Lysgaard, Arghya Bhowmik, Kedar Hippalgaonkar, Juan Maria Garcia Lastra.  
[arXiv:2603.26471 (2026)](https://doi.org/10.48550/arXiv.2603.26471)  

* **PFP/MM: A Hybrid Approach Combining a Universal Neural Network Potential with Classical Force Fields for Large-Scale Reactive Simulations** [2026]  
Yu Miyazaki, Atsuhiro Tomita, Akihide Hayashi, So Takemoto, Mizuki Takemoto, Hodaka Mori.  
[arXiv:2603.16061 (2026)](https://doi.org/10.48550/arXiv.2603.16061)  

* **Design Space of Self--Consistent Electrostatic Machine Learning Interatomic Potentials** [2026]  
William J. Baldwin, Ilyes Batatia, Martin Vondrák, Johannes T. Margraf, Gábor Csányi.  
[arXiv:2603.14700 (2026)](https://doi.org/10.48550/arXiv.2603.14700)  

* **Simulating enzyme catalysis with electrostatically embedded machine learning potentials** [2026]  
Gradisteanu, Valentin, Elliot W. Chan, Lester Hedges, Meritxell Malagarriga, Rolf David, Miguel de la Puente, Damien Laage, Iñaki Tuñón, Marc W. van der Kamp, and Kirill Zinovjev.  
[Chem. Sci. (2026)](https://doi.org/10.1039/D6SC01156J) | [code](https://github.com/chemle/emle-enzymes-paper)  

* **Bias in Universal Machine-Learned Interatomic Potentials and its Effects on Fine-Tuning** [2026]  
Nicolas Wong, Julia H. Yang.  
[arXiv:2603.10159 (2026)](https://doi.org/10.48550/arXiv.2603.10159) | [code](https://github.com/YangLab-GT/uMLIP_Finetuning)  

* **Constructing Diabatic Potential Energy Matrices with Quantum Dynamic Accuracy: A Neural Network Based Δ-Machine Learning Approach** [2026]  
Siting Hou, Zejie Zhang, and Changjian Xie.  
[J. Chem. Theory Comput. (2026)](https://doi.org/10.1021/acs.jctc.5c01758)  

* **Resolving the body-order paradox of machine learning interatomic potentials** [2026]  
Sanggyu Chong, Tong Jiang, Michelangelo Domina, Filippo Bigi, Federico Grasselli, Joonho Lee, Michele Ceriotti.  
[J. Chem. Phys.(2026)](https://doi.org/10.1063/5.0303302)  

* **AceFF: A State-of-the-Art Machine Learning Potential for Small Molecules** [2026]  
Stephen E. Farr, Stefan Doerr, Antonio Mirarchi, Francesc Sabanes Zariquiey, Gianni De Fabritiis.  
[arXiv:2601.00581 (2026)](https://doi.org/10.48550/arXiv.2601.00581) | [code](https://huggingface.co/Acellera/AceFF-2.0)  

* **MAPLE: A General Framework for Automated Molecular Modeling across Machine-Learning Potentials** [2026]  
Wang X, Zhang Y, Sun Z, Zhu R, Asam C, Li W-L, et al.  
[ChemRxiv. (2026)](https://doi.org/10.26434/chemrxiv-2026-k7znx) | [code](https://github.com/ClickFF/MAPLE)  

* **Ab Initio Melting Properties of Water and Ice from Machine Learning Potentials** [2025]  
Yifan Li, Bingjia Yang, Chunyi Zhang, Axel Gomez, Pinchen Xie, Yixiao Chen, Pablo M. Piaggi, Roberto Car.  
[arXiv:2512.23939 (2025)](https://doi.org/10.48550/arXiv.2512.23939)  

* **Advanced Machine Learning Interatomic Potential for Accelerated Atomistic Simulations of Lithiation Dynamics in Large-Scale Si@C Core–Shell Anodes** [2025]  
Yujie Liao, Pengfei Suo, Changhao Wang, Jincang Zhang, and Yunsong Li.  
[ACS Appl. Mater. Interfaces (2025)](https://doi.org/10.1021/acsami.5c18142)  

* **LAMMPS-ANI: Large Scale Molecular Dynamics Simulations with ANI Neural Network Potential** [2025]  
Xue J, Terrel N, Pickering I, Roitberg A.  
[ChemRxiv. (2025)](https://doi.org/10.26434/chemrxiv-2025-8v03m) | [code](https://github.com/roitberg-group/lammps-ani)  

* **Domain oriented universal machine learning potential enables fast exploration of chemical space of battery electrolytes** [2025]  
Wang, F., Tang, YH., Ma, ZB. et al.  
[Nat Commun (2025)](https://doi.org/10.1038/s41467-025-67982-0) | [code](https://doi.org/10.12463/AI4EC/QZCYP1)  

* **Automated Machine Learning Pipeline: Large Language Models-Assisted Automated Data set Generation for Training Machine-Learned Interatomic Potentials** [2025]  
Adam Lahouari, Jutta Rogal, and Mark E. Tuckerman.  
[J. Chem. Theory Comput. (2025)](https://doi.org/10.1021/acs.jctc.5c01610) | [code](https://github.com/adamlaho/AMLP)  

* **Node-Equivariant Message Passing for Efficient and Accurate Machine Learning Interatomic Potentials** [2025]  
Yaolong Zhang* and Hua Guo.  
[Chem. Sci.(2025)](https://doi.org/10.1039/D5SC07248D) | [code](https://github.com/zhangylch/NEMP)  

* **Enhanced Sampling for Efficient Learning of Coarse-Grained Machine Learning Potentials** [2025]  
Weilong Chen, Franz Görlich, Paul Fuchs, and Julija Zavadlav.  
[J. Chem. Theory Comput. (2025)](https://doi.org/10.1021/acs.jctc.5c01712) | [code](https://github.com/tummfm/biased-force-matching)  

* **Benchmarking Universal Interatomic Potentials on Elemental Systems** [2025]  
Hossein Tahmasbi, Andreas Knüpfer, Thomas D. Kühne, Hossein Mirhosseini.  
[arXiv:2512.20230 (2025)](https://doi.org/10.48550/arXiv.2512.20230) | [code](https://codebase.helmholtz.cloud/casus-datalad/atomistic_foundation_model.datalad/project)  

* **Machine learning interatomic potentials at the centennial crossroads of quantum mechanics** [2025]  
Kalita, B., Gokcan, H. & Isayev, O.  
[Nat Comput Sci 5, 1120–1132 (2025)](https://doi.org/10.1038/s43588-025-00930-6)  

* **Evidential deep learning for interatomic potentials** [2025]  
Dongjin Kim, Bingqing Cheng.  
[Nat Commun (2025)](https://doi.org/10.1038/s41467-025-67663-y) | [code](https://github.com/xuhan323/eIP) | [Zenodo](https://doi.org/10.5281/zenodo.17730621)  

* **Challenges and Opportunities of Machine Learning Interatomic Potentials in Heterogeneous Catalysis** [2025]  
Loveday O, Kazmierczak K, López N.  
[ChemRxiv. (2025)](https://doi.org/10.26434/chemrxiv-2025-vk805)  

* **Long-range electrostatics for machine learning interatomic potentials is easier than we thought** [2025]  
Dongjin Kim, Bingqing Cheng.  
[arXiv:2512.18029 (2025)](https://doi.org/10.48550/arXiv.2512.18029) | [code](https://github.com/ChengUCB/les)  

* **Thermal dynamics and coalescence of Au144(SR)60 clusters from a machine-learned potential** [2025]  
Sabooni Asre Hazer, M., Malola, S. & Häkkinen, H.  
[Nat Commun (2025)](https://doi.org/10.1038/s41467-025-67700-w) | [data](https://doi.org/10.23729/fd-a31ffb92-7fd0-33c0-bcd9-100d48367687)  

* **Generalization of Long-Range Machine Learning Potentials in Complex Chemical Spaces** [2025]  
Michal Sanocki, Julija Zavadlav.  
[arXiv:2512.10989 (2025)](https://doi.org/10.48550/arXiv.2512.10989) | [code](https://github.com/tummfm/chemtrain)  

* **Platonic representation of foundation machine learning interatomic potentials** [2025]  
Zhenzhu Li, Aron Walsh.  
[arXiv:2512.05349 (2025)](https://doi.org/10.48550/arXiv.2512.05349) | [code](https://github.com/WMD-group/PlatonicRep)  

* **Accurate machine learning interatomic potentials for polyacene molecular crystals: application to single molecule host-guest systems** [2025]  
Gurlek, B., Sharma, S., Lazzaroni, P. et al.  
[npj Comput Mater 11, 318 (2025)](https://doi.org/10.1038/s41524-025-01825-w) | [Zenodo](https://doi.org/10.5281/zenodo.17100564)  

* **Modeling Equilibrium Solid–Liquid Interfaces under Effective Constant Chemical Potential Using Machine Learning Interatomic Potentials** [2025]  
Ademola Soyemi, Khagendra Baral, and Tibor Szilvási.  
[J. Phys. Chem. A (2025)](https://doi.org/10.1021/acs.jpca.5c06453) | [code](https://zenodo.org/records/17088343)  

* **A foundation model for atomistic materials chemistry** [2025]  
Batatia, Ilyes, Philipp Benner, Yuan Chiang, Alin M. Elena, Dávid P. Kovács, Janosh Riebesell, Xavier R. Advincula et al.  
[J. Chem. Phys. 163, 184110 (2025)](https://doi.org/10.1063/5.0297006) | [code](http://github.com/acesuit/mace-mp)  

* **Peering inside the black box by learning the relevance of many-body functions in neural network potentials** [2025]  
Bonneau, K., Lederer, J., Templeton, C. et al.  
[Nat Commun 16, 9898 (2025)](https://doi.org/10.1038/s41467-025-65863-0) | [code](https://github.com/jnsLs/gnn-lrp-cg.git)  

* **TorchANI 2.0: An extensible, high performance library for the design, training, and use of NN-IPs** [2025]  
Pickering I, Xue J, Huddleston K, Terrel N, Roitberg A.  
[J. Chem. Inf. Model. (2025)](https://doi.org/10.1021/acs.jcim.5c01853) | [ChemRxiv. (2025)](https://doi.org/10.26434/chemrxiv-2025-w0w7d) | [code](https://github.com/aiqm/torchani)  

* **Python Library for Monte Carlo Simulations with Ab Initio and Machine-Learned Interatomic Potentials** [2025]  
Woodrow N. WilsonVivek S. BharadwajNeeraj Rai*.  
[J. Chem. Theory Comput. (2025)](https://doi.org/10.1021/acs.jctc.5c01148) | [code](https://github.com/MSELRai/ASE-MC_ESI)  

* **Anticipating the Selectivity of Cyclization Reaction Pathways with Neural Network Potentials** [2025]  
Nicholas Casetti, Dylan Anstine, Olexandr Isayev, and Connor W. Coley.  
[J. Chem. Theory Comput. (2025)](https://doi.org/10.1021/acs.jctc.5c01161) | [code](https://github.com/ncasetti7/REVAMP)  

* **Weighted active space protocol for multireference machine-learned potentials** [2025]  
A. Seal,S. Perego,M.R. Hennefarth,U. Raucci,L. Bonati,A.L. Ferguson,M. Parrinello, & L. Gagliardi.  
[Proc. Natl. Acad. Sci. (2025)](https://doi.org/10.1073/pnas.2513693122) | [code](https://github.com/GagliardiGroup/wasp)  

* **Machine learning of charges and long-range interactions from energies and forces** [2025]  
King, D.S., Kim, D., Zhong, P. et al.  
[Nat Commun 16, 8763 (2025)](https://doi.org/10.1038/s41467-025-63852-x) | [code](https://github.com/BingqingCheng/cace-lr-fit)  

* **Learning non-local molecular interactions via equivariant local representations and charge equilibration** [2025]  
Fuchs, P., Sanocki, M. & Zavadlav, J.  
[npj Comput Mater 11, 287 (2025)](https://doi.org/10.1038/s41524-025-01790-4) | [code](https://github.com/tummfm/chemtrain)  

* **Scalable Foundation Interatomic Potentials via Message-Passing Pruning and Graph Partitioning** [2025]  
Lingyu Kong, Jaeheon Shim, Guoxiang Hu, Victor Fung.  
[arXiv:2509.21694 (2025)](https://doi.org/10.48550/arXiv.2509.21694) | [code](https://github.com/Fung-Lab/MatterTune)  

* **Weighted active space protocol for multireference machine-learned potentials** [2025]  
A. Seal,S. Perego,M.R. Hennefarth,U. Raucci,L. Bonati,A.L. Ferguson,M. Parrinello, & L. Gagliardi.  
[Proc. Natl. Acad. Sci. (2025)](https://doi.org/10.1073/pnas.2513693122) | [code](https://github.com/GagliardiGroup/wasp)  

* **One to Rule Them All: A Universal Interatomic Potential Learning across Quantum Chemical Levels** [2025]  
Yuxinxin Chen and Pavlo O. Dral.  
[J. Chem. Theory Comput. (2025)](https://doi.org/10.1021/acs.jctc.5c00858) | [code](https://github.com/dralgroup/aio-ani)  

* **Learning Long-Range Interactions in Equivariant Machine Learning Interatomic Potentials via Electronic Degrees of Freedom** [2025]  
Maruf, Moin Uddin, Sungmin Kim, and Zeeshan Ahmad.  
[J. Phys. Chem. Lett. (2025)](https://doi.org/10.1021/acs.jpclett.5c02352) | [code](https://github.com/ahmad-research-group/nequip-charge/tree/charge-encoding)  

* **Graph atomic cluster expansion for foundational machine learning interatomic potentials** [2025]  
Yury Lysogorskiy, Anton Bochkarev, Ralf Drautz.  
  [arXiv:2508.17936 (2025)](https://doi.org/10.48550/arXiv.2508.17936)  

* **A critical review of machine learning interatomic potentials and Hamiltonian** [2025]  
Li, Y.; Zhang, X.; Liu, M.; Shen, L.  
  [J. Mater. Inf. (2025)](http://dx.doi.org/10.20517/jmi.2025.17)  

* **PIL-Net: a physics-informed graph convolutional network for predicting atomic multipoles** [2025]  
Dario Coscia, Pim de Haan, Max Welling.  
[arXiv:2508.14022 (2025)](https://arxiv.org/abs/2508.14022) | [code](https://github.com/dario-coscia/blip)  

* **FastTrack: a fast method to evaluate mass transport in solid leveraging universal machine learning interatomic potential** [2025]  
Hanwen Kang, Tenglong Lu, Zhanbin Qi, Jiandong Guo, Sheng Meng, Miao Liu.  
[arXiv:2508.10505 (2025)](https://doi.org/10.48550/arXiv.2508.10505)  

* **PIL-Net: a physics-informed graph convolutional network for predicting atomic multipoles** [2025]  
Whitter, Caitlin, Alex Pothen, and Aurora Clark.  
[Digital Discovery (2025)](https://doi.org/10.1039/D5DD00228A) | [code](https://github.com/rinikerlab/EquivariantMultipoleGNN)  

* **Performance of universal machine-learned potentials with explicit long-range interactions in biomolecular simulations** [2025]  
Viktor Zaverkin, Matheus Ferraz, Francesco Alesiani, Mathias Niepert.  
[arXiv:2508.10841 (2025)](https://doi.org/10.48550/arXiv.2508.10841) | [code](https://github.com/nec-research/ictp)  

* **chemtrain-deploy: A parallel and scalable framework for machine learning potentials in million-atom MD simulations** [2025]  
Paul Fuchs, Weilong Chen, Stephan Thaler, Julija Zavadlav.  
[J. Chem. Theory Comput. (2025)](https://doi.org/10.1021/acs.jctc.5c00996) | [arXiv:2506.04055 (2025)](https://doi.org/10.48550/arXiv.2506.04055) | [data](https://github.com/tummfm/chemtrain)  

* **Augmenting Molecular Graphs with Geometries via Machine Learning Interatomic Potentials** [2025]  
Fu, Cong, Yuchao Lin, Zachary Krueger, Haiyang Yu, Maho Nakata, Jianwen Xie, Emine Kucukbenli, Xiaofeng Qian, and Shuiwang Ji.  
[arXiv:2507.00407 (2025)](https://doi.org/10.48550/arXiv.2507.00407) | [data](https://huggingface.co/divelab)  

* **Tensor Decomposition Networks for Fast Machine Learning Interatomic Potential Computations** [2025]  
Lin, Yuchao, Cong Fu, Zachary Krueger, Haiyang Yu, Maho Nakata, Jianwen Xie, Emine Kucukbenli, Xiaofeng Qian, and Shuiwang Ji.  
[arXiv:2507.01131 (2025)](https://doi.org/10.48550/arXiv.2507.01131) | [data](https://huggingface.co/divelab)  

* **A Benchmark for Quantum Chemistry Relaxations via Machine Learning Interatomic Potentials** [2025]  
Fu, Cong, Yuchao Lin, Zachary Krueger, Wendi Yu, Xiaoning Qian, Byung-Jun Yoon, Raymundo Arróyave et al.  
[arXiv:2506.23008 (2025)](https://doi.org/10.48550/arXiv.2506.23008) | [data](https://huggingface.co/divelab)  

* **Enhancing Machine Learning Potentials through Transfer Learning across Chemical Elements** [2025]  
Sebastien Röcken and Julija Zavadlav.  
[J. Chem. Inf. Model. (2025)](https://doi.org/10.1021/acs.jcim.5c00293) | [code](https://github.com/tummfm/TL_MLP)  

* **Distillation of atomistic foundation models across architectures and chemical domains** [2025]  
Gardner, John LA, Daniel F. Toit, Chiheb Ben Mahmoud, Zoé Faure Beaulieu, Veronika Juraskova, Laura-Bianca Paşca, Louise AM Rosset et al.  
[arXiv:2506.10956 (2025)](https://arxiv.org/abs/2506.10956) | [code](https://github.com/jla-gardner/augment-atoms)  

* **Spin-informed universal graph neural networks for simulating magnetic ordering** [2025]  
W. Xu,R.Y. Sanspeur,A. Kolluru,B. Deng,P. Harrington,S. Farrell,K. Reuter,& J.R. Kitchin.  
[Proc. Natl. Acad. Sci. (2025)](https://doi.org/10.1073/pnas.2422973122) | [code](https://github.com/Wenbintum/ocp_mag)  

* **UMA: A Family of Universal Models for Atoms** [2025]  
Brandon M. Wood, Misko Dzamba, Xiang Fu, Meng Gao, Muhammed Shuaibi, Luis Barroso-Luque, Kareem Abdelmaqsoud, Vahe Gharakhanyan, John R. Kitchin, Daniel S. Levine, Kyle Michel, Anuroop Sriram, Taco Cohen, Abhishek Das, Ammar Rizvi, Sushree Jagriti Sahoo, Zachary W. Ulissi, C. Lawrence Zitnick.  
[arXiv:2506.23971(2025)](https://doi.org/10.48550/arXiv.2506.23971) | [code](https://huggingface.co/facebook/UMA)  

* **Application-specific Machine-Learned Interatomic Potentials: Exploring the Trade-off Between Precision and Computational Cost** [2025]  
Baghishov, Ilgar, Jan Janssen, Graeme Henkelman, and Danny Perez.  
[arXiv:2506.05646 (2025)](https://arxiv.org/abs/2506.05646)  

* **DeePEST-OS: A Generic Machine Learning Potential for Accelerating Transition State Search in Organic Synthesis** [2025]  
Ren K, Tang K, Zhao Y, Zhang L, Du J, Meng Q, et al.  
[ChemRxiv. (2025)](https://doi.org/10.26434/chemrxiv-2025-mzz6w)  

* **AIMNet2-rxn: A Machine Learned Potential for Generalized Reaction Modeling on a Millions-of-Pathways Scale** [2025]  
Anstine DM, Zhao Q, Zubatiuk R, Zhang S, Singla V, Nikitin F, et al.  
[ChemRxiv. (2025)](https://doi.org/10.26434/chemrxiv-2025-hpdmg) | [code](https://github.com/isayevlab/aimnetcentral)  

* **Global universal scaling and ultrasmall parameterization in machine-learning interatomic potentials with superlinearity** [2025]  
Y. Hu,Y. Sheng,J. Huang,X. Xu,Y. Yang,M. Zhang,Y. Wu,C. Ye,J. Yang,& W. Zhang,  
[Proc. Natl. Acad. Sci. (2025)](https://doi.org/10.1073/pnas.2503439122) | [code](https://github.com/hu-yanxiao/SUS2-MLIP)  

* **Machine Learning Potentials for Alloys: A Detailed Workflow to Predict Phase Diagrams and Benchmark Accuracy** [2025]  
Siya Zhu and Doğuhan Sarıtürk and Raymundo Arroyave.  
[arXiv:2506.16771(2025)](https://arxiv.org/abs/2506.16771) | [code](https://github.com/dogusariturk/PhaseForge)  

* **DistMLIP: A Distributed Inference Platform for Machine Learning Interatomic Potentials** [2025]  
Kevin Han, Bowen Deng, Amir Barati Farimani, Gerbrand Ceder.  
[arXiv:2506.02023 (2025)](https://doi.org/10.48550/arXiv.2506.02023)  

* **Weighted Active Space Protocol for Multireference Machine-Learned Potentials** [2025]  
Aniruddha Seal, Simone Perego, Matthew R. Hennefarth, Umberto Raucci, Luigi Bonati, Andrew L. Ferguson, Michele Parrinello, Laura Gagliardi.  
[arXiv:2505.10505 (2025)](https://arxiv.org/abs/2505.10505)  

* **Discovering High-Entropy Oxides with a Machine-Learning Interatomic Potential** [2025]  
Sivak, Jacob T., Saeed SI Almishal, Mary Kathleen Caucci, Yueze Tan, Dhiya Srikanth, Joseph Petruska, Matthew Furst et al.  
[Phys. Rev. Lett. (2025)](https://doi.org/10.1103/PhysRevLett.134.216101)  

* **Fast and Fourier Features for Transfer Learning of Interatomic Potentials** [2025]  
Pietro Novelli, Giacomo Meanti, Pedro J. Buigues, Lorenzo Rosasco, Michele Parrinello, Massimiliano Pontil, Luigi Bonati.  
[arXiv:2505.05652 (2025)](https://doi.org/10.48550/arXiv.2505.05652) | [code](https://franken.readthedocs.io/)  

* **Practical Machine Learning Strategies. 2. Accurate Prediction of ωB97X-V/6-311+G(2df,2p), ωB97M-V/6-311+G(2df,2p) and ωB97M(2)/6-311+G(2df,2p) Energies From Neural Networks Trained From ωB97X-D/6-31G* Equilibrium Geometries and Energies** [2025]  
Philip Klunzinger, Thomas Hehre, Bernard Deppmeier, William Ohlinger, Warren Hehre.  
[Computer Physics Communications (2025)](https://doi.org/10.1002/jcc.70129)  

* **Structure and Dynamics of CO2 at the Air–Water Interface from Classical and Neural Network Potentials** [2025]  
Nitesh Kumar and Vyacheslav S. Bryantsev.  
[J. Phys. Chem. Lett. (2025)](https://doi.org/10.1021/acs.jpclett.5c01206)  

* **chemtrain: Learning deep potential models via automatic differentiation and statistical physics** [2025]  
Fuchs, Paul, Stephan Thaler, Sebastien Röcken, and Julija Zavadlav.  
[Computer Physics Communications (2025)](https://doi.org/10.1016/j.cpc.2025.109512) | [code](https://github.com/tummfm/chemtrain)  

* **Accurate and efficient machine learning interatomic potentials for finite temperature modelling of molecular crystals** [2025]  
Della Pia, Flaviano and Shi, Benjamin X. and Kapil, Venkat and Zen, Andrea and Alfè, Dario and Michaelides, Angelos.  
[Chem. Sci. (2025)](https://doi.org/10.1039/D5SC01325A) | [code](https://github.com/water-ice-group/MolCrys-MACE)  

* **Impact of Derivative Observations on Gaussian Process Machine Learning Potentials: A Direct Comparison of Three Modeling Approaches** [2025]  
Yulian T. Manchev and Paul L. A. Popelier.  
[J. Chem. Theory Comput. (2025)](https://doi.org/10.1021/acs.jctc.5c00344)  

* **INN-FF: A Scalable and Efficient Machine Learning Potential for Molecular Dynamics** [2025]  
Taskin Mehereen, Sourav Saha, Intesar Jawad Jaigirdar, Chanwook Park.  
[arXiv:2505.18141 (2025)](https://doi.org/10.48550/arXiv.2505.18141)  

* **Transferability of MACE Graph Neural Network for Range Corrected Δ-Machine Learning Potential QM/MM Applications** [2025]  
Timothy J. Giese, Jinzhe Zeng, and Darrin M. York.  
[J. Phys. Chem. B (2025)](https://doi.org/10.1021/acs.jpcb.5c02006)  

* **OMNI-P2x: A Universal Neural Network Potential for Excited-State Simulations** [2025]  
Martyka M, Tong X-Y, Jankowska J, Dral PO.  
[ChemRxiv. (2025)](https://doi.org/10.26434/chemrxiv-2025-j207x) | [code](https://github.com/dralgroup/omni-p2x)  

* **Interpolation and differentiation of alchemical degrees of freedom in machine learning interatomic potentials** [2025]  
Nam, J., Peng, J. & Gómez-Bombarelli, R.  
[Nat Commun 16, 4350 (2025)](https://doi.org/10.1038/s41467-025-59543-2) | [code](https://github.com/learningmatter-mit/alchemical-mlip)  

* **Uncertainty quantification for neural network potential foundation models** [2025]  
Bilbrey, J.A., Firoz, J.S., Lee, MS. et al..  
[npj Comput Mater 11, 109 (2025)](https://doi.org/10.1038/s41524-025-01572-y) | [code](https://github.com/pnnl/SNAP)  

* **DeePMD-kit v3: A Multiple-Backend Framework for Machine Learning Potentials** [2025]  
Zeng, Jinzhe, Duo Zhang, Anyang Peng, Xiangyu Zhang, Sensen He, Yan Wang, Xinzijian Liu et al.  
[J. Chem. Theory Comput. (2025)](https://arxiv.org/abs/2502.19161) | [arXiv:2502.19161 (2025)](https://arxiv.org/abs/2502.19161) | [code](https://github.com/njzjz/benchmark-dpv3)  

* **Multi-fidelity learning for interatomic p