# mineral-exploration-machine-learning
This page lists resources for mineral exploration and machine learning, generally with useful code and examples. 
ML and Data Science is a huge field, these are resources I have found useful and/or interesting to me in practice.
Links currently to a fork of a repository are because I have changed something to use and put in a list for reference.
Resources are also given for data analysis, transformation and visualisation as that is most of the work.

Suggestions welcome: open a discussion, issue or pull request.

# Table of Contents

* [Prospectivity](https://github.com/RichardScottOZ/mineral-exploration-machine-learning#prospectivity)
* [Geology](https://github.com/RichardScottOZ/mineral-exploration-machine-learning#geology)
* [Natural Language Processing](https://github.com/RichardScottOZ/mineral-exploration-machine-learning#natural-language-processing)
* [Remote Sensing](https://github.com/RichardScottOZ/mineral-exploration-machine-learning#remote-sensing)
* [Data Quality](https://github.com/RichardScottOZ/mineral-exploration-machine-learning#data-quality)
* [Community](https://github.com/RichardScottOZ/mineral-exploration-machine-learning#communit)
* [Cloud providers](https://github.com/RichardScottOZ/mineral-exploration-machine-learning#cloud-providers)
* [Domains](https://github.com/RichardScottOZ/mineral-exploration-machine-learning#domains)
* [Overview](https://github.com/RichardScottOZ/mineral-exploration-machine-learning#overview)
* [Web Services](https://github.com/RichardScottOZ/mineral-exploration-machine-learning#web-services)
* [Data Portals](https://github.com/RichardScottOZ/mineral-exploration-machine-learning#data-portals)
* [Tools](https://github.com/RichardScottOZ/mineral-exploration-machine-learning#tools)
* [Ontologies](https://github.com/RichardScottOZ/mineral-exploration-machine-learning#ontologies)
* [Books](https://github.com/RichardScottOZ/mineral-exploration-machine-learning#books)
* [Datasets](https://github.com/RichardScottOZ/mineral-exploration-machine-learning#datasets)
* [Papers](https://github.com/RichardScottOZ/mineral-exploration-machine-learning#papers)
* [Other](https://github.com/RichardScottOZ/mineral-exploration-machine-learning#other)
* [General Interest](https://github.com/RichardScottOZ/mineral-exploration-machine-learning#general-interest)

# Map
* [Map of Github](https://anvaka.github.io/map-of-github/#10.26/28.263/19.7499)
* [DeepWiki](https://github.com/AsyncFuncAI/deepwiki-open) -> automagic wiki style analysis of a repo via llm

# Frameworks
* [UNCOVER-ML Framework](https://github.com/RichardScottOZ/uncover-ml)
  * [Geo-Wavelets](https://github.com/RichardScottOZ/geo-wavelets)
  * [ML-Preprocessing](https://github.com/GeoscienceAustralia/ML-preprocessing)
  * [Landshark](https://github.com/data61/landshark) -> Large-scale spatial inference with tensorflow
  * [GIS ML Workflow](https://github.com/sheecegardezi/GIS-ML-Workflow)
* [EIS Toolkit](https://github.com/GispoCoding/eis_toolkit/tree/master) -> Python library for mineral prospectivity mapping from EIS Horizon EU Project
* [PySpatialML](https://github.com/RichardScottOZ/Pyspatialml) -> Library that facilitates prediction and handling for raster machine learning automatically to geotiff, etc.
* [DARPA Criticalmaas](https://github.com/DARPA-CRITICALMAAS)
  * [competition info](file:///C:/Users/rscott/Downloads/DARPA-PA-22-02-01.pdf)
  * [uncharted T1](https://github.com/DARPA-CRITICALMAAS/uncharted-ta1) ->  Automated feature extraction and georeferencing of geologic maps
  * [paper](www.sciencedirect.com/science/article/pii/S2590197425000564) -> Extracting data from maps: Lessons learned from the artificial intelligence for critical mineral 
  assessment competition
  * [training data](https://data.usgs.gov/datacatalog/data/USGS:63a100d6d34e0de3a1f2794f)
  * [QueryPlot](https://github.com/DARPA-CRITICALMAAS/sri-ta2-mappable-criteria) - Generating mineral evidence maps from geological queries
    * [paper](https://arxiv.org/abs/2602.17784) - Generating mineral evidence maps from geological queriesGenerating mineral evidence maps from geological queries
* [scikit-map](https://github.com/scikit-map/scikit-map/tree/master)
* [TorchGeo](https://github.com/microsoft/torchgeo) -> Pytorch library for remote sensing style models
 * [terratorch](https://github.com/IBM/terratorch) -> Flexible fine-tuning framework for Geospatial Foundation Models
  * [TorchSpatial](https://github.com/seai-lab/TorchSpatial)
	* [paper](https://arxiv.org/abs/2406.15658)
* [torch-harmonics](https://github.com/NVIDIA/torch-harmonics) -> Differentiable signal processing on the sphere for PyTorch
* [geodl](https://eartharxiv.org/repository/view/7417/)  
* [Geo Deep Learning](https://github.com/RichardScottOZ/geo-deep-learning) -> Simple deep learning framework based on RGB
* [AIDE: Artificial Intelligence for Disentangling Extremes](https://github.com/RichardScottOZ/AIDE?tab=readme-ov-file)
	* [paper](https://www.researchgate.net/profile/Miguel-Angel-Fernandez-Torres/publication/381917888_The_AIDE_Toolbox_Artificial_intelligence_for_disentangling_extreme_events/links/66846648714e0b03153f38ae/The-AIDE-Toolbox-Artificial-intelligence-for-disentangling-extreme-events.pdf)
* [ExPloRA](https://github.com/samar-khanna/ExPLoRA) -> ExPLoRA: Parameter-Efficient Extended Pre-training to Adapt Vision Transformers under Domain Shifts
	* [Website](https://www.samarkhanna.com/ExPLoRA/)
	* [paper](https://arxiv.org/abs/2406.10973)
* [truly spatial random forest](https://github.com/RichardScottOZ/truly-spatial-random-forest)
  * [paper](https://www.researchgate.net/publication/353253570_A_Truly_Spatial_Random_Forests_Algorithm_for_Geoscience_Data_Analysis_and_Modelling)

 * [pyClusterwise](https://pypi.org/project/pyClusterWise/)
  * [paper] -> https://www.sciencedirect.com/science/article/pii/S0169136825001519?via%3Dihub -> Clustering in geo-data science: Navigating uncertainty to select the most reliable method
* [GeoStat Framework](https://github.com/GeoStat-Framework) -> Group of repositories with kriging and other
* [CoreJepa](https://github.com/galilai-group/lejepa) - LeJea for Remote Sensing
  * [HuggingFace](https://huggingface.co/gajeshladhar/core-jepa)
* [Perceiver](https://github.com/RichardScottOZ/deepmind-research/tree/master/perceiver)
  * [perceiver pytorch](https://github.com/RichardScottOZ/perceiver-pytorch) 
* [Senseiver](https://github.com/je-santos/DOI4Senseiver/tree/v1.0.0) -> Development of the Senseiver for efficient field reconstruction from sparse observations
  * [paper](https://www.nature.com/articles/s42256-023-00746-x)
    * [Zenodo](https://zenodo.org/records/8364148)
    *
## R
* [CAST](https://github.com/RichardScottOZ/CAST) -> Caret Applications for Spatio-Temporal models
* [geodl](https://github.com/maxwell-geospatial/geodl) -> semantic segmentation of geospatial data using convolutional neural network-based deep learning
	* [paper](https://arxiv.org/html/2404.06978v1)
### Pipelines
* [geotargets](https://github.com/RichardScottOZ/geotargets) -> Extension of targets to terra and stars

# Prospectivity
## World
* [Porphyry prospectivity global](https://github.com/EarthByte/porphyry-prospectivity-global) -> Spatio-temporal global mapping
  * [zenodo](https://zenodo.org/record/8157691)
* [Spatiotemporal-Data-Mining-of-Sediment-Hosted-Deposits-Subduction-Craton-Distance Public](https://github.com/Hojat-Shirmard/Spatiotemporal-Data-Mining-of-Sediment-Hosted-Deposits-Subduction-Craton-Distance)
  * [paper](https://www.researchgate.net/publication/390283561_Spatio-temporal_data_mining_of_craton_edge-related_mineralisation_Unveiling_the_dynamics_of_sediment-hosted_and_IOCG_deposits)


## Oceania
### Australia
* [Iron oxide copper-gold mineral potential maps](https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/149222)
* [Lateritic Ni-Co prospectivity modeling in eastern Australia using an enhanced generative adversarial network and positive-unlabeled bagging] -> (https://zenodo.org/records/14037494)
  * [paper](https://link.springer.com/article/10.1007/s11053-024-10423-4)
* [Machine learning for geological mapping : algorithms and applications](https://eprints.utas.edu.au/18571/) -> PhD thesis with code and data
* [minpot-toolkit](https://github.com/GeoscienceAustralia/minpot-toolkit/tree/main) -> Example of Hoggard et al Lab Boundary analysis with Sedimentary copper
* [MPM-WofE](https://github.com/GeoscienceAustralia/MPM-WofE) -> Mineral Potential Mapping - Weights of Evidence
* [Porphyry Copper Spatio-Temporal Exploration](https://github.com/EarthByte/porphyry_copper_spatiotemporal_exploration)  
	* [paper](https://www.earthbyte.org/predicting-the-emplacement-of-cordilleran-porphyry-copper-systems-using-a-spatio-temporal-machine-learning-model/)
* [Prospectivity Mapping of Ni-Co Laterites](https://github.com/EarthByte/Lachlan_Laterite_Ni_Co)
* [Transform 2022 Tutorial](https://github.com/Solve-Geosolutions/transform_2022) -> Random forest example
	* [Video](https://www.youtube.com/watch?v=C4YvnLMzYDc)
* [Tin-Tungsten](https://medium.com/@thomas.ostersen/tin-tungsten-prospecting-with-machine-learning-in-northeast-tasmania-australia-3c23519f81cf)
	* [Collab](https://colab.research.google.com/drive/168PSo21-Jkwdz8xOmr5-rX9_DL3SInCN?usp=sharing)
#### Explorer Challenge
* [Explorer Challenge](https://github.com/RichardScottOZ/explore_australia) -> OZ Minerals run competition with Data Science introduction
#### South Australia
* [DEEP-SEAM](https://github.com/EarthByte/MPM_Curnamona_REE) -> An explainable semi-supervised deep learning framework for mineral prospectivity mapping: DEEP-SEAM v1.0
  * [publication]https://egusphere.copernicus.org/preprints/2025/egusphere-2025-3283/
* [Gawler_MPM](https://github.com/e-farahbakhsh/Gawler_MPM) -> Cobalt, Chromium, Nickel
	* [Paper](https://www.researchgate.net/publication/373954003_Critical_mineral_prospectivity_mapping_on_the_Gawler_craton_using_a_new_machine_learning_framework)
* [Geophysical Data Clustering in the Gawler Craton](https://github.com/EarthByte/geophysical_image_clustering_exploration)
	* [Zenodo Data](Automated detection of mineralization-related craton structures using geophysical data and unsupervised machine learning)
#### Explore SA - South Australian Department of Energy and Mining Competition
* [Winners](https://catalog.sarig.sa.gov.au/geonetwork/srv/eng/catalog.search#/metadata/abba4f54-b6ef-4fe4-b951-57f11299d490) -> SARIG data information
* [Caldera](https://github.com/mrodda117/CalderaPublic) -> Caldera Analytics analysis
* [IncertoData](https://github.com/RichardScottOZ/ExploreSA/tree/master/Data_submission_competition)
* [Butterworth and Barnett](https://github.com/RichardScottOZ/gawler-exploration) -> Butterworth and Barnett entry
* [Data Driven Mineralisation Mapping](https://github.com/Abdallah-M-Ali/mman4020_Data_Driven_Mineralisation_Mapping/blob/main/docs/tensor.ipynb)

### Papua New Guinea
* [SpatioTemporAl Mineral Prospectivity (STAMP) Modelling](https://github.com/EarthByte/STAMP_PNG)
	* [Zenodo Data](https://zenodo.org/records/14189755)

## North America
### Canada
* [Generative Neural Network for Mineral Prospectivity with Uncertainty Quantification](https://github.com/RichardScottOZ/generative-neural-network-mineral-prospectivity-uncertainty)
  * [paper](https://www.sciencedirect.com/science/article/pii/S0169136825004044) -> A generative neural network approach to uncertainty and risk-return analysis in mineral prospectivity modelling

* [Transfer Prospectivity Learnnig](https://github.com/Anagabrielamantilla/TransferProspectivityLearning)
	* [paper](https://www.sciencedirect.com/science/article/pii/S1342937X24002727)  -> Porphyry-type mineral prospectivity mapping with imbalanced data via prior geological transfer learning
* [Probabilistic mineral prospectivity modelling with TAGI, BNN, and MC dropout](https://github.com/Laish93/probabilistic_mpm)
  * [paper](https://www.sciencedirect.com/science/article/pii/S2590197426000169) -> Tractable approximate Gaussian inference for interpretable mineral prospectivity modelling

## South America
* [Machine learning to classify ore deposits from tectonomagmatic properties](https://github.com/intelligent-exploration/mineralexplorationcourse/tree/master/Week10)
## Brazil
* [Mapa Preditivo](https://github.com/fnaghetini/Mapa-Preditivo) -> Brazil student project
* [Course_Predictive_Mapping_USP](https://github.com/victsnet/Curso_Mapeamento_Preditivo_USP) -> Course Project
* [Mineral Prospectivity Mapping](https://github.com/Eliasmgprado/MineralProspectivityMapping)
* [3D Weights of Evidence](https://github.com/e-farahbakhsh/3DWofE)
* [Geological Complexity SMOTE](https://github.com/Eliasmgprado/GeologicalComplexity_SMOTE) -> includes fractal analysis
	* [paper](https://doi.org/10.1016/j.oregeorev.2020.103611)
* [MPM Jurena](https://github.com/victsnet/MPM---Juruena-Mineral-Province ) -> Jurena Mineral Province
## Colombia
* [mapo_prospectivo](https://github.com/francobr991/Mapeo_prospectivo) -> Machine Learning-Based Prospective Modeling for Alluvial Gold Mining: A Study Area in Colombia
  * [paper](https://link.springer.com/article/10.1007/s00024-025-03830-y)

## China
* [MPM by ensemble learning](https://github.com/ZhiqiangZhangCUGB/MPM-by-ensemble-learning) -> Qingchengzi Pb-Zn-Ag-Au polymetallic district China
* [Mineral Prospectivity Prediction Convolutional Neural Networks](https://github.com/yangna815/Mineral-Prospectivity-Prediction-Convolutional-Neural-Networks) -> CNN Example with a few architectures [a paper by this author uses GoogleNet]
* [Mineral Prospectivity Prediction by CSAE](https://github.com/yangna815/Mineral-Prospectivity-Prediction-by-CSAE)
* [Mineral Prospectivity Prediction by CAE](https://github.com/yangna815/Mineral-Prospectivity-Prediction-by-CAE)
 	* [paper](https://www.researchgate.net/publication/350817877_Mineral_Prospectivity_Prediction_via_Convolutional_Neural_Networks_Based_on_Geological_Big_Data)

# India
* [mineral_mapping](https://github.com/sharonchrista/mineral_mapping) -> Mineral Prospectivity Mapping — Deep Multi-Modal Fusion
  * [paper](https://link.springer.com/article/10.1007/s11053-026-10771-3) -> Self-Supervised Multi-modal Fusion for Mineral Prospectivity Mapping Using Vision Transformers Integrating Multi-scale Geological Maps with Aeromagnetic Data [UNSEEN]
* [MPM-Gold](https://github.com/Venkatasaimudili/MPM_Gold) -> gold mineral prospectivity mapping using multiple machine learning models (FKELM and WGAN others are baselines)
  * [paper](https://www.mdpi.com/2075-163X/15/11/1125) -> A Hybrid Framework for Detecting Gold Mineralization Zones in G.R. Halli, Western Dharwar Craton, Karnataka, India 

## Norway
* [A machine learning–based approach to regional-scale mapping of sensitive glaciomarine clay combining airborne electromagnetics and geotechnical data](https://github.com/emerald-geomodelling/publication-NSG2021-Christensen-QuickClayML)
	* [paper](https://onlinelibrary.wiley.com/doi/10.1002/nsg.12166)

# Africa
## Namibia
* [data_and_code_of_narr](https://github.com/soeaxy/data_and_code_of_narr) -> Uranium Mineral Prospectivity Modeling – Husab Deposit, Namibia
* [paper](https://link.springer.com/article/10.1007/s11053-026-10661-8) - > Integrating Cost-Sensitive Ensemble Learning and Geoscience Big Data for Uranium Prospectivity Mapping in the Husab Uranium Deposit, Namibia

## Sudan
* [Mineral Prospectivity Mapping ML](https://github.com/Abdallah-M-Ali/Mineral-Prospectivity-Mapping-ML)


## Europe
## Russia
* [Korznhinskii-Net](https://github.com/BorisKriuk/KORZHINSKII-Net) -> Physics-Informed Neural Network for Sub-Surface Mineral Prospectivity Modelling
  * [paper](https://arxiv.org/abs/2606.13695)


## Uncertainty
* [MPM-uncertainty](https://github.com/ziyewangcug/MPM-uncertainty-quantification) -> Mineral Potential Mapping uncertainty quantification

# Geology
* [autoencoders_remotesensing](https://github.com/sydney-machine-learning/autoencoders_remotesensing)
	* [paper](https://arxiv.org/abs/2404.02180v1) -> Remote sensing framework for geological mapping via stacked autoencoders and clustering
* [Bedrock-vs-sediment](https://github.com/alexandra-jarna/Bedrock-vs-sediment)
	* [paper](https://www.researchgate.net/publication/370929945_Where_are_the_outcrops_Automatic_delineation_of_bedrock_from_sediments_using_Deep-Learning_techniques
* [Brazil Predictive Geology Maps](https://github.com/marcosbr/predictive-geology-maps) -> Work by the Brazil geological survey
* [depth to bedrock](https://github.com/Alberta-Geological-Survey/depth-to-bedrock)(Evaluating spatially enabled machine learning approaches for depth to bedrock mapping) 
	* [paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0296881)
* [DL-RMD](https://github.com/rizwanasif/DL-RMD) -> A geophysically constrained electromagnetic resistivity model database for deep learning applications
* [Earthscape](https://github.com/masseygeo/earthscape) -> EarthScape: A Multimodal Dataset for Surficial Geologic Mapping and Earth Surface Analysis
  * [paper](https://arxiv.org/abs/2503.15625)
* [Geological Image Classifier](https://github.com/PCleverleyGeol/Geological-Image-Classifier)
* [geological map explanatory power](https://github.com/charliekirkwood/geological-map-explanatory-power)
  * [paper](https://www.lyellcollection.org/doi/full/10.1144/esss2024-005) -> Quantifying the limited explanatory power of geological maps
* [Geological mapping in the age of artificial intelligence](https://geoscientist.online/sections/features/geological-mapping-in-the-age-of-artificial-intelligence/) -> Geological mapping in the age of artificial intelligence
* [GeolNR](https://github.com/MichaelHillier/GeoINR) -> Geological Implicit Neural Representation for three-dimensional structural geological modelling applications
	* [paper](https://gmd.copernicus.org/articles/16/6987/2023/)
  * [paper](https://www.sciencedirect.com/science/article/pii/S0098300426000208) -> Uncertainty quantification using Hamiltonian Monte Carlo for structural geological modelling with implicit neural representations
* [Geological Section Generated based on per-pixel linked lists](https://github.com/Dy111111/Geological-Sections_Generation_based_on_PPLL )
  * [paper](https://www.researchgate.net/publication/391580813_A_real-time_geological_sections_generation_method_for_geological_3D_models_based_on_per-pixel_linked_lists)
* [Geoscience Transformers for Predictive Mapping of Critical Minerals](https://github.com/RichardScottOZ/geoscience-transformers-for-predictive-mapping-of-critical-minerals) 
  * [paper](https://link.springer.com/article/10.1007/s11053-025-10564-0) -> Large Language Models and Geoscience Transformers for Predictive Mapping of Canadian Critical Minerals
* [mapeamento_litologico_preditivo](https://github.com/Gabriel-Goes/mapeamento_litologico_preditivo)
* [Mapping Global Lithospheric Mantle Pressure-Temperature Conditions by Machine-Learning Thermobarometry](https://zenodo.org/records/8353966)
	* [paper](https://www.researchgate.net/publication/379639953_Mapping_Global_Lithospheric_Mantle_Pressure-Temperature_Conditions_by_Machine-Learning_Thermobarometry)
* [MGALNet](https://github.com/Candy-CY/MGALNet) - Multisource Remote Sensing Interpretation of Geological Lithology via Multigranularity Adaptive Learning
  * [paper](https://ieeexplore.ieee.org/abstract/document/11408228) [UNSEEN] 
* [Non Stationarity Mitigation Transformer](https://github.com/LeiLiu-cloud/NonstationarityMitigation_Transformer)
  * [Collab](https://colab.research.google.com/drive/1pPZCSjlNPn7_n8GLGCxY0bo7QmbVU65G?usp=sharing) -> Notebook
	* [paper](https://www.sciencedirect.com/science/article/abs/pii/S0098300423001164)
* [Neural Rock Typing](https://github.com/LukasMosser/neural_rock_typing)
* [PEACE](https://github.com/microsoft/PEACE) -> Empowering Geologic Map Holistic Understanding with MLLMs)
  *[paper](https://github.com/microsoft/PEACE) -> GeoMap-Bench
* [SimCLR Core Disturbance](simclr_core_disturbance)
  * [paper](https://www.sciencedirect.com/science/article/pii/S2590197424000636?via%3Dihub)
* [Uncertainty Driven Geoogical Mapping](https://github.com/ziyewangcug/uncertainty-driven-lithological-mapping)
* [West Musgraves Geology Uncertainty](https://medium.com/@thomas.ostersen/uncertainty-mapping-in-the-west-musgraves-australia-988fc49ce1e4) -> Uncertainty map prediction with entropy analysis: highly useful

## Training Data
* [Into the Noddyverse](https://github.com/Loop3D/noddyverse/tree/1.0) -> a massive data store of 3D geological models for machine learning and inversion applications
  * [Original Zenondo repository](https://zenodo.org/record/4589883#.YvYk23ZByUk)  
  * [website](https://tectonique.net/noddy)
  * [New Geonetwork Location](https://geonetwork.nci.org.au/geonetwork/srv/eng/catalog.search#/metadata/f3570_5134_6366_9231)
* [Geo-Bench](https://huggingface.co/datasets/microsoft/PEACE)

## Lithology
* [CMGAT](https://github.com/Y0901/A-contrastive-multimodal-graph-attention-network)
  * [paper](https://www.sciencedirect.com/science/article/abs/pii/S0013795225006040) -> Interpretable regional-scale geological mapping using a contrastive graph attention network for multimodal data fusion and recognition of controlling factors [UNSEEN]
  * [deepwiki](https://deepwiki.com/Y0901/A-contrastive-multimodal-graph-attention-network)
* [litho2strat](https://gmd.copernicus.org/articles/19/1007/2026/) -> Estimate stratigraphy from drillhole logs using Loop techniques
  * [paper]([Automated stratigraphic interpretation from drillhole lithological descriptions with uncertainty quantification: litho2strat 1.0](https://gmd.copernicus.org/articles/19/1007/2026/) -> Automated stratigraphic interpretation from drillhole lithological descriptions with uncertainty quantification: litho2strat 1.0

* [Deep Learning Lithology](https://github.com/RichardScottOZ/deeplearning_lithology)
* [Rock Protolith Predictor](https://github.com/RichardScottOZ/Rock_protolith_predictor)
* [SA Geology Lithology Predictions](https://github.com/RADutchie/SA-geology-litho-predictions)
* [Automated Well Log Correlation](https://github.com/dudley-fitzgerald/AutomatedWellLogCorrelation)
* [dawson-facies-2022](https://github.com/johnlab-research/dawson-facies-2022) -> Transfer learning for geological images
	* [paper](https://www.sciencedirect.com/science/article/pii/S0098300422002333) - > Impact of dataset size and convolutional neural network architecture on transfer learning for carbonate rock classification
* [Litho-Classification](https://github.com/luthfigeo/Litho-Classification) -> Volcanic facies Classification using Random Forest
* [Multi-view ensemble machine learning approach for 3D modeling using geological and geophysical data](https://doi.org/10.6084/m9.figshare.23647590.v1)
* [Petromind](https://github.com/connamulder/PetroMind) -> PetroMind: A multimodal petrographic model for rock image classification and lithological description generation
  * [paper](https://www.sciencedirect.com/science/article/pii/S2590197425000965)
	* [paper](https://www.tandfonline.com/doi/abs/10.1080/13658816.2024.2394228)
* [SedNet](https://github.com/MudRocw1/SedNet_explainable-deep-learning-network)
	* [paper](https://www.sciencedirect.com/science/article/abs/pii/S0098300423002157?via%3Dihub)
* [SCB-Net](https://github.com/victsnet/SCB-Net) -> Lithological mapping using Spatially Constrained Bayesian Network
  * [paper](https://www.sciencedirect.com/science/article/pii/S0098300425001141?via%3Dihub)

## Mineralogy
* [hywiz][(https://github.com/samthiele/hywiz/tree/v0.15)] - Predicting Mineralogy with Hyperspectral Data: A Benchmark Dataset and Machine Learning Framework to Enable Hyperspectral Geometallurgy 
  * [zenodo](https://rodare.hzdr.de/record/4582)
  * [hywiz-zenodo](https://zenodo.org/records/20714783)
  * [hklearn-zendo](https://zenodo.org/records/20714783)
  * [paper](https://www.mdpi.com/2075-163X/16/7/674)
    * [data](https://rodare.hzdr.de/record/4582)

## Drilling
* [drillbench]() - repository stub - not yet existing - could be yet another project with no info until some pulication somewhere
  * [paper](https://arxiv.org/abs/2610.01204) -> Autoregressive Drillhole Modelling Under Distribution Shift
* https://arxiv.org/abs/2610.01204
* [Heterogenous Drilling](https://geoscienceaustralia.github.io/uncover-ml/projectreport.html#uncoverml-project-report-nicta) - Nicta/Data61 project report for looking at modelling using drillholes that don't go far enough
* [corel](https://github.com/RichardScottOZ/corel) -> smart computer vision model that identifies facies and performs rock typing on core images
* [baselode](https://github.com/darkmine-oss/baselode) -> processing, managing, and visualizing geological and mining data

## Paleovalleys
* [Sub3DNet1.0: a deep-learning model for regional-scale 3D subsurface structure mapping](https://gmd.copernicus.org/articles/14/3421/2021/)

## Stratigraphy
* [Predicatops](https://github.com/JustinGOSSES/predictatops) -> Stratigraphic predication designed for hydrocarbon
* [stratal-geometries](https://github.com/jessepisel/stratal-geometries) -> Predicting Stratigraphic Geometries from Subsurface Well Logs

## Structural
* [APGS](https://github.com/ondrolexa/apsg) -> Structural geology package
* [Assessing plate reconstruction models using plate driving force consistency tests](https://zenodo.org/records/7904975) -> Jupyter notebook and data
	* [paper](https://www.nature.com/articles/s41598-023-37117-w)
* [CIG-Bench](https://github.com/douyimin/CIG-bench) -> 
  * [website](https://douyimin.github.io/CIG-bench/)
  * [paper](https://arxiv.org/abs/2606.09094)
* [Curlew](https://gmd.copernicus.org/articles/19/3455/2026/) -> Spatio-temporal implicit geological modelling with neural fields in python
  * [curlew_examples](https://github.com/k4m4th/curlew_examples)
* [gplately](https://github.com/GPlates/gplately)
* [structural geology cookbook](https://github.com/gcmatos/structural-geology-cookbook]
* [GEOMAPLEARN 1.0](https://doi.org/10.18144/8aee-7b77) -> Detecting geological structures from geological maps with machine learning
* [GemPy Model Mexico Basin(https://github.com/Nauj29/GemPy_Model_Mexico_Basin)
  * [zenodo](https://zenodo.org/records/16423800)
  * [paper](https://link.springer.com/article/10.1007/s12145-025-02064-9#data-availability) -> Implicit 3D structural geological modeling of the Mexico Basin: a scalable and reproducible open-source workflow
* [Lineament Learning](https://github.com/RichardScottOZ/Lineament-Learning) -> Fault prediction and mapping via potential field deep learning and clustering Update
  * [Lineament Learning](https://github.com/aminrd/LineamentLearning) -> original version
* [Lineament DEM Extractor](https://github.com/PedroRossi99/Lineament_DEM_extractor) -> Topographic lineaments extraction in digital elevation model
  * [paper](https://www.researchgate.net/publication/397085283_Topographic_lineaments_extraction_in_digital_elevation_modelLineamentos_topograficos_em_modelos_digitais_de_elevacao_a_comparison_between_human_interpretation_and_a_convolutional_neural_network_output)
* [LitMod3D](https://github.com/javfurchu/LitMod3D_V3.1) -> 3D integrated geophysical-petrological interactive modelling of the lithosphere and underlying upper mantle
* [Machine Learning Based Mohometry](https://github.com/EarthByte/Machine-Learning-Based-Mohometry/tree/main) -> Paleo Crustal Thickness Estimation and Evolution Visualization
  * [paper](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JB030404)
* [others](https://www.bgh.org.au/software/)
* [StructuralGeo](https://github.com/eldadHaber/StructuralGeo)
  * [zenodo](https://zenodo.org/records/15244035)
  * [paper](https://arxiv.org/abs/2506.11164) -> Synthetic Geology: Structural Geology Meets Deep Learning
  
  

## Simulation
* [GebPy](https://github.com/MABeeskow/GebPy) -> generation of geological data for rocks and minerals
* [OpenGeoSys](https://gitlab.opengeosys.org/ogs/ogs) -> development of numerical methods for the simulation of thermo-hydro-mechanical-chemical (THMC) processes in porous and fractured media
* [Stratigraphics.jl](https://github.com/JuliaEarth/StratiGraphics.jl) -> Creating 3D stratigraphy from 2D geostatistical processes
* [SubsurfaceGen](https://anonymous.4open.science/r/subsurfacegen-8961/README.md) -> SubsurfaceGen: Procedural Generation of Field-Scale Earth Models and Seismic Data
  * [paper](https://arxiv.org/abs/2605.30541) 

## Geodynamics
* [Badlands](https://github.com/badlands-model/badlands) -> Basin and Landscape Dynamics
* [CitcomS](https://github.com/geodynamics/citcoms) -> Finite element code designed to solve compressible thermochemical convection problems relevant to Earth's mantle.
* [LaMEM](https://github.com/UniMainzGeo/LaMEM) -> simulate various thermo-mechanical geodynamical processes such as mantle-lithosphere interaction
* [PTatin3D](https://bitbucket.org/ptatin/ptatin3d/src/master/) -> studying long time-scale processes relevant to geodynamics [original motivation :toolkit capable of studying high-resolution, three-dimensional models of lithospheric deformation]
* [underworld](https://github.com/underworldcode/underworld2) -> Finite element modelling of geodynamics
* [Discern detachment of the subducting slab in an ancient subduction zone using machine learning](https://zenodo.org/records/14059244)
  * [paper](https://agupubs.onlinelibrary.wiley.com/doi/pdf/10.1029/2024JH000400)
* [ThermoPlates](https://github.com/samuelcboone/ThermoPlates) -> integrate thermochronology data with plate tectonic, mantle dynamics, and paleoclimate model outputs for interpreting long-term exhumation histories
  * [paper](https://www.nature.com/articles/s43247-025-03005-6)
* [HalTracks](https://github.com/samuelcboone/HALtracks) -> AI-based approach for constraining the thermal evolution of Earth's upper crust through automated digital fission-track analysis
  * [paper](https://www.sciencedirect.com/science/article/pii/S0098300425002468?via%3Dihub)
* [Paleocoordinates Calculator](https://zenodo.org/records/19332776) -> A user-friendly online tool for paleocoordinate calculation and 3D visualization 
  * [paper](https://www.nature.com/articles/s41598-026-46309-z#ref-CR30)
  
## Geophysics
### General
* [Feature fusion-enhanced t-SNE image atlas for geophysical features discovery](https://github.com/ll-portes/t-sne_atlas)
  * [paper](https://www.nature.com/articles/s41598-025-01333-3)
* [Geophysics Blakey](https://github.com/RichardScottOZ/geophysics-blakely)
  * [Fortran version](https://github.com/VictorCarreira/Geophysics) -> ports of Blakely geophysics algorithms
* [Gridmerger](https://github.com/RichardScottOZ/Gridmerger) -> Merge many overlapping grids with polynomial fitting and blending

### Structural
* [Structural Geophysics Tools](https://github.com/swaxi/SGTool) -> QGIS aimed
### Foundation Models
* [Cross-Domain Foundation Model Adaptation: Pioneering Computer Vision Models for Geophysical Data Analysis](https://github.com/programmerzxg/cross-domain-foundation-model-adaptation) -> some of code to come
	* [paper](https://arxiv.org/pdf/2408.12396)
* [Seismic Foundation Model](https://github.com/shenghanlin/SeismicFoundationModel) -> "a new generation deep learning model in geophysics"
* [Geological Everything Model](https://arxiv.org/abs/2507.00419) -> Geological Everything Model 3D: A Physics-informed Promptable Foundation Model for Unified and Zero-Shot Subsurface Understanding
  * [Paper Implementation Repo](https://github.com/RichardScottOZ/GEM-Paper)
* [SeismicFoundationModel-01-2025](https://github.com/julaborde/SeismicFoundationModel-01-2025) -> development of a multimodal AI model combining seismic waveforms and geophysical images, based on two foundation models: Seismic Foundation Model (SFM) and SeisLM
* [NCS-Model](https://github.com/NorskRegnesentral/NCS_models) -> The NCS-Model: A seismic foundation model trained on the Norwegian repository of public data
  * [model](https://huggingface.co/NorskRegnesentralSTI)
  * [paper](https://arxiv.org/abs/2603.23211)

### Australia
#### Regolith Depth
* [Regolith Depth](https://data.csiro.au/collection/csiro:11393v6) -> Model
* [Complete Radiometrics Grid of Australia with modelled infill](https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/144413)
#### AEM Interpolation
* [High resolution conductivity mapping using regional AEM survey](https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/146163)
	* [Abstract](https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/146380)
  
### Electromagnetics
* [AEM-Assist](https://github.com/GeoscienceAustralia/AEM-assist)
  * [extended abstract](https://ecat.ga.gov.au/geonetwork/srv/api/records/9090de3e-1edc-47f3-a8c0-cd13c73972bc)
* [TEM-NLnet: A Deep Denoising Network for Transient Electromagnetic Signal with Noise Learning](https://github.com/wmyCDUT/TEM-NLnet_demo)
* [OpenEM](https://github.com/WAL-l/OpenEM) -> Large-scale multi-structural 3D datasets for electromagnetic methods
  * [Geoelectrical3D](https://github.com/WAL-l/Geoelectrical3D) -> Model generation tool for OpenEM
  * [OpenEM Dataset](https://zenodo.org/records/17141981)

### Inversion
* [Machine Learning and Geophysical Inversion](https://github.com/ezygeo-ai/machine-learning-and-geophysical-inversion) -> reconstruct paper from Y. Kim and N. Nakata (The Leading Edge, Volume 37, Issue 12, Dec 2018)
* [Deep Learning for Magnetotelluric Data Inversion](https://github.com/aeh1707/1DMD_inversion)
  * [paper](https://www.researchgate.net/profile/Hakim-Saibi-2/publication/392579623_Comparison_of_Deep_Learning_Models_for_1D_Magnetotelluric_Inversion/links/6849494ac33afe388acb5380/Comparison-of-Deep-Learning-Models-for-1D-Magnetotelluric-Inversion.pdf)
* [GP-Cubed](https://github.com/williamjsdavis/GP-cubed/tree/main/neural-operator-geophysics) -> Gaussian Processes for GeoPhysics and Geology Playground
  * [article](https://posgeo.wordpress.com/2026/02/13/using-neuraloperator-for-geophysical-surrogate-modeling/) -> Using NeuralOperator for Geophysical Surrogate Modeling

#### Euler deconvolution
- https://legacy.fatiando.org/gallery/gravmag/euler_moving_window.html
	- Harmonica version eventually? https://hackmd.io/@fatiando/development-calls-2024?utm_source=preview-mode&utm_medium=rec
- https://notebook.community/joferkington/tutorials/1404_Euler_deconvolution/euler-deconvolution-examples
- https://github.com/ffigura/Euler-deconvolution-plateau


### Gravity
* [Recovering 3D Basement Relief Using Gravity Data Through Convolutional Neural Networks]
	* [Data](10.5281/zenodo.5543969)
	* [paper](https://www.researchgate.net/publication/355118950_Recovering_3D_Basement_Relief_Using_Gravity_Data_Through_Convolutional_Neural_Networks)
* [Stable downward continuation of the gravity potential field implemented using deep learning](https://github.com/LiYongbo-geo/DC-Net-code)
	* [paper](https://www.researchgate.net/publication/366965954_Stable_downward_continuation_of_the_gravity_potential_field_implemented_using_deep_learning)
* [Fast imaging for the 3D density structures by machine learning approach](https://github.com/LiYongbo-geo/GV-Net-code)
	* [paper](https://www.researchgate.net/publication/366922016_Fast_imaging_for_the_3D_density_structures_by_machine_learning_approach)
- [Gravity Geophysics](https://github.com/JuliaGeophysics/GravityGeophysics.jl) -> Julia package for 3D gravity forward modeling and analysis with UBC-GIF format support
 
### Magnetics
* [High-resolution aeromagnetic map through Adapted-SRGAN](https://github.com/MBS1984/Adapted-SRGAN)
	* [paper](https://www.sciencedirect.com/science/article/pii/S0098300423000675)
* [MagImage2Geo3D](https://github.com/neu-gjt/MagImage2Geo3D)
	* [paper](https://www.researchgate.net/publication/348697645_3D_geological_structure_inversion_from_Noddy-generated_magnetic_data_using_deep_learning_methods)

### Seismic
* [StorSeismic](https://github.com/swag-kaust/storseismic) -> An approach to pre-train a neural network to store seismic data features
* [PINNtomo](https://github.com/tianyining/PINNtomo) -> Seismic tomography using physics-informed neural networks
	* [paper](https://arxiv.org/abs/2104.01588)
### Seismology
* [obspy](https://github.com/obspy/obspy) -> framework for processing seismological

### Petrophysics
* [ML4Rocks](https://github.com/clberube/ml4rocks) -> Some intro work

### Seismic
* [torchseis](https://github.com/JintaoLee-Roger/torchseis) -> 3D Deep Learning Framework for Seismic and Subsurface Modeling
  * [paper](https://www.nature.com/articles/s44172-025-00576-2) -> Memory-efficient full-volume inference for large-scale 3D dense prediction without performance degradation

### Tectonics
* [Discern detachment of the subducting slab in an ancient subduction zone using machine learning](https://github.com/dzheng2333/basalt_geochemistry) -> Notebook
	* [figshare](https://figshare.com/articles/dataset/Supporting_information_for_A_machine_learning_approach_to_identify_the_abrupt_transition_of_tectonic_settings_using_trace_elemental_dataset_of_basalts_/24015024)
* [Colab notebook](https://data.csiro.au/collection/csiro:61119) -> Google Colab input file for benchmark results of ML-SEISMIC publication
	* [paper](https://www.researchgate.net/publication/376892064_Physics-informed_neural_network_reconciles_Australian_displacements_and_tectonic_stresses)
* [Unleashing the power of Machine
Learning in Geodynamics](https://github.com/GiteonCaulfied/COMP4560_stokes_ml_project])
	* [Honours Thesis](https://www.researchgate.net/profile/Xuzeng-He/publication/380316113_Unleashing_the_power_of_Machine_Learning_in_Geodynamics/links/6634eac535243041535c878b/Unleashing-the-power-of-Machine-Learning-in-Geodynamics.pdf)
  [related](https://github.com/GiteonCaulfied/COMP4560_stokes_ml_project/blob/main/misc_pdfs/Atkins_Thesis_Finding_the_patterns_in_mantle_convection.pdf)
* [Physics-Infomred Neural Networks for fault slip simulation with rate and state friction law](https://github.com/RichardScottOZ/PINN_3DSSE/tree/main)
	* [simulation and frictional paramter estimation on slow slip events](https://zenodo.org/records/13731480)
	* [paper](https://d197for5662m48.cloudfront.net/documents/publicationstatus/223843/preprint_pdf/29c1d7b3b99de49d81f41725303268db.pdf) -> Physics-Informed Deep Learning for Estimating the Spatial Distribution of Frictional Parameters in Slow Slip Regions
	
  
# Geochemistry
* [CODAinPractice](https://github.com/michaelgreenacre/CODAinPractice) -> Compositional Data Analysis in Practice
* [GeoCoDa](https://www.researchgate.net/publication/372487589_GeoCoDA_Recognizing_and_Validating_Structural_Processes_in_Geochemical_Data_A_Workflow_on_Compositional_Data_Analysis_in_Lithogeochemistry)
* [DAN-GRF](https://github.com/Saeid1986/DAN-GRF) -> Deep autoencoder network connected to geographical random forest for spatially aware geochemical anomaly detection
	* [paper](https://www.sciencedirect.com/science/article/pii/S0098300424001407)
* [Dash Geochemical Prospection](https://github.com/pvabreu7/DashGeochemicalProspection) -> Web-app classifying stream sediments with K-means
* [DZ-ML](https://github.com/jackfekete01/DZ_ML) -> Classifying Detrital Zircon U-Pb Age Distributions using Automated Machine Learning
  * [paper](https://www.sciencedirect.com/science/article/pii/S2590197425000333?via%3Dihub) -> Classifying detrital zircon U-Pb age distributions using automated machine learning
  * [zenodo](https://zenodo.org/records/14532918) -> Synthetic Fixed Age Mode Data
* [Enhancing machine learning thermobarometry for clinopyroxene-bearing magmas](https://github.com/magredal/Enhancing-ML-Thermobarometry-for-Clinopyroxene-Bearing-Magmas)
	* [paper](https://www.sciencedirect.com/science/article/pii/S0098300424001900) -> Enhancing-ML-Thermobarometry-for-Clinopyroxene-Bearing-Magmas
* [Zircon fertility models](https://github.com/cicarrascog/Zircon_fertility_models) -> Decision trees to predict fertile zircon from porphyry copper deposits
	* [paper](https://www.researchgate.net/publication/382089226_Quantifying_the_Criteria_Used_to_Identify_Zircons_from_Ore-Bearing_and_Barren_Systems_in_Porphyry_Copper_Exploration)
* [Machine Learning Zircon Trace Element Tool to Predict Porphyry Deposit Type and Resource Size](https://github.com/ZihaoWen123/PDT_PCR_PMR/tree/v0.01	)
	* [zenodo archive](https://zenodo.org/records/10292176)
	* [paper](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2024JH000180)
* [geology_class0](https://github.com/ZihaoWen123/geology_class) -> A machine learning approach to discrimination of igneous rocks and ore deposits by zircon trace elements 
	* [paper](https://www.degruyter.com/document/doi/10.2138/am-2022-8899/html)
	* [Demo application](http://60.205.170.161:8001/)
	* https://colab.research.google.com/drive/1-bOZgG6Nxt2Rp1ueO1SYmzIqCRiyyYcT
* [geochemical anomaly detection](https://github.com/MinersAI/geochemical_anomaly_detection) -> Multivariate Outlier Detection in Geochemical Datasets
* [GeochemPrint](https://colab.research.google.com/drive/1nX0vip0VS3f-GjL9l5femBiRcMwMGe_Y) 
	* [paper](https://www.researchgate.net/publication/363754140_Geochemical_fingerprinting_of_continental_and_oceanic_basalts_A_machine_learning_approach)
* [Global geochemistry](https://github.com/dhasterok/global_geochemistry)
* [ICBMS Jacobina](https://github.com/gferrsilva/icpms-jacobina) -> Analysis of pyrite chemistry from a gold deposit
* [indicator_minerals](https://github.com/DinaKlim/indicator_minerals) -> Can PCA can tell the story of the origin of tourmaline?
* [Interpretation of Trace Element Chemistry of Zircons from Bor and Cukaru Peki: Conventional Approach and Random Forest Classification](https://www.mdpi.com/2076-3263/12/11/396)
* [Journal of Geochemical Exploration - Manifold](https://github.com/geometatqueens/2020---Journal-of-Geochemical-Exploration--Manifold)
* [LewisML](https://github.com/RichardScottOZ/LewisML) -> Analysis of the Lewis Formation
* [MICA](https://github.com/bluetyson/MICA_shiny) -> Chemical composition, in Shiny
* [Multivariate statistical analysis and bespoke deviation network modeling for geochemical anomaly detection of rare earth elements](https://github.com/EarthByte/MPM_Geochemistry_Curnamona_REE/tree/main)
	* [paper](https://www.sciencedirect.com/science/article/pii/S0883292724002518?dgcid=coauthor)
* [Prospectivity mapping of rare earth elements through geochemical data analysis](https://github.com/EarthByte/MPM_Geochemistry_Curnamona_REE) -> Prospectivity mapping of rare earth elements through geochemical data analysis
* [QMineral Modeller](https://github.com/gferrsilva/QMineral_Modeller) -> Mineral Chemistry virtual assistant from the Brazilian geological survey
* [Recognizing-geochemical-spatial-patterns-using-DCN-guided-with-geological-knowledge](https://github.com/Aleksiyu/)
  * [paper](https://gmd.copernicus.org/articles/19/2219/2026/)
  * [Zenodo](https://zenodo.org/records/18454129)
* [Secular Changes in the Occurrence of Subduction During the Archean](https://zenodo.org/records/10418615) -> Zenodo code archive
	* [paper] https://www.researchgate.net/publication/380289934_Secular_Changes_in_the_Occurrence_of_Subduction_During_the_ArcheanA machine learning approach to discrimination of igneous rocks and ore deposits by zircon trace elements 
 
# Kriging
* [DKNN: deep kriging neural network for interpretable geospatial interpolation](https://github.com/in1311/DKNN)
	* [paper](https://www.tandfonline.com/doi/full/10.1080/13658816.2024.2347316 )

# Natural Language Processing
## Frameworks
* [spacy](https://github.com/explosion/spaCy) -> NLP Library
## Text Extraction
* [Automated Extraction of Mining Company Drillhole Results](https://github.com/RichardScottOZ/Automatic-Extraction-of-Mining-Company-Drillhole-Results)
	* [Conference Paper](https://aclanthology.org/2022.wnut-1.16/)
* [BERT CWS](https://github.com/cugdeeplearn/BERTCWS)
	* [paper](https://www.researchgate.net/publication/352009328_Chinese_Word_Segmentation_Based_on_Self-Learning_Model_and_Geological_Knowledge_for_the_Geoscience_Domain)
* [Geocorpus](https://github.com/jneto04/geocorpus)
* [Geological-table-analysis](https://github.com/CUGdjhz/Geological-table-analysis) -> Understanding table content for mineral exploration reports using deep learning and natural language processing
  * [paper](https://www.sciencedirect.com/science/article/pii/S0169136823000987)
* [NASA Concept Tagging](https://github.com/RichardScottOZ/concept-tagging-training) -> Keyword prediction 
	* [API](https://github.com/nasa/concept-tagging-api) -> API web service
	* [Presentation](https://datascience.jpl.nasa.gov/aiworkshop/presentation-27)
* [Petrography Report Data Extractor](https://github.com/RichardScottOZ/Petrography-report-data-extractor)
* [Portuguese BERT](https://github.com/neuralmind-ai/portuguese-bert)
* [SA Exploration Topic Modelling](https://github.com/RADutchie/SA-exploration-topic-modelling) -> Topic modelling from exploration reports
* [Stratigraph](https://github.com/BritishGeologicalSurvey/stratigraph)
* [Text Extraction](https://github.com/RichardScottOZ/amazon-textract-textractor) -> Text extraction from documents : paid ML as a service, but works very well, can extract tables efficiently
	* [Large Scale](https://github.com/RichardScottOZ/amazon-textract-serverless-large-scale-document-processing) -> Large scale version

### PDF handling
* [pdfminer](https://github.com/pdfminer/pdfminer.six)
* [pdfplumber](https://github.com/jsvine/pdfplumber) -> pdf table extraction
* [pikepdf](https://github.com/RichardScottOZ/pikepdf) -> pdf image extraction
* [PyMuPDF](https://github.com/pymupdf/PyMuPDF) -> pdf parser
#### Tables
* [camelot](https://github.com/camelot-dev/camelot) -> pdf text table extraction
* [layoutparser](https://github.com/Layout-Parser/layout-parser) -> deep learning layhout detection
* [messytables](https://github.com/okfn/messytables?tab=readme-ov-file) -> find headers and datatypes

## Heuristic Aids
### Java
* [GeoTopicParser](https://cwiki.apache.org/confluence/display/TIKA/GeoTopicParser)
### Python
* [GIS Metadata parsing](https://github.com/RichardScottOZ/gis-metadata-parser) -> extract data from xml etc.
### R
* [crssuggest](https://github.com/walkerke/crsuggest) -> coordinate reference system suggerstions
* [tidyxl](https://github.com/cran/tidyxl)
### OCR
* [Apache Tika](https://tika.apache.org/) -> OCR, content analysis
* [Parsee PDF Reader](https://github.com/parsee-ai/parsee-pdf-reader) - PDF Reading/OCR
* [Tesseract](https://github.com/tesseract-ocr/tesseract) -> OCR
## Word Embeddings
* [Geoscience Language Models](https://github.com/NRCan/geoscience_language_models) -> processing code pipeline and models [Glove, BERT) retrained on geoscience documents from Canada
	* [Datasets](https://geoscan.nrcan.gc.ca/starweb/geoscan/servlet.starweb?path=geoscan/downloade.web&search1=R=329265) -> Data to support models
	* [paper](https://doi.org/10.1016/j.acags.2022.100084) -> Geoscience language models and their intrinsic evaluation
	* [paper](https://link.springer.com/article/10.1007/s11053-023-10216-1) -> Applications of Natural Language Processing to Geoscience Text Data and Prospectivity Modeling
* [GeoVec](https://github.com/spadarian/GeoVec) -> Word embedding model trained on 300K geoscience papers
	* [GeoVec Model](https://osf.io/4uyeq/) -> OSF Storage for GeoVec model
   	* [paper](https://soil.copernicus.org/articles/5/177/2019/)
    * [GeoVecto Litho](https://github.com/IFuentesSR/GeoVectoLitho) -> 3D Models interpolation from word embeddings
	* [GeoVEC Playground](https://github.com/RichardScottOZ/geoVec-playground) -> Working with the Padarian GeoVec glove word embeddings model
* [GloVe](https://github.com/stanfordnlp/GloVe) -> Standford library for producing word embeddings
	* [gloVE python](https://pypi.org/project/glove-python-binary/) glove, glove-python highly problematic on windows: here Binary version for Windows installs:
* [Mittens](https://github.com/roamanalytics/mittens) -> In memory vectorized glove implementation 
* [PetroNLP](https://github.com/Petroles/PetroNLP) -> Organisation
  * [PetroVec](https://github.com/Petroles/Petrovec) -> Portuguese Word Embeddings for the Oil and Gas Industry: development and evaluation
  * [Petro KGraph](https://github.com/Petroles/Petro_KGraph) -> Ontological work with petrovec
  * [paper](https://www.sciencedirect.com/science/article/abs/pii/S0098300424001973) -> [UNSEEN]
* [wordembeddingsOG](https://github.com/diogosmg/wordEmbeddingsOG) -> Portuguese Oil and Gas word embeddings
* [Portuguese Word Embeddings](https://github.com/nathanshartmann/portuguese_word_embeddings) 
	* [Portuguese models](http://nilc.icmc.usp.br/embeddings)
* [Spanish Word Embeddings](https://github.com/dccuchile/spanish-word-embeddings)
* [Multilingual alignment](https://github.com/babylonhealth/fastText_multilingual/blob/master/align_your_own.ipynb)
	* [Overview of approaches](https://www.jair.org/index.php/jair/article/view/11640/26511)
* [Application-of-natural-language-processing-for-finding-semantic-relation-of-elusive-natural-resource](https://github.com/NanmanasLin/Application-of-natural-language-processing-for-finding-semantic-relation-of-elusive-natural-resource)
  * [paper](https://arxiv.org/abs/2504.07490) -> Geological Inference from Textual Data using Word Embeddings
## Named Entity Recognition
* [Geo NER Model](https://github.com/BritishGeologicalSurvey/geo-ner-model) -> Named entity recognition
* [GeoBERT](https://huggingface.co/botryan96/GeoBERT) - hugging face repo for model in  
	* [paper]https://www.researchgate.net/publication/359186219_Few-shot_learning_for_name_entity_recognition_in_geological_text_based_on_GeoBERT
* [GLiNER](https://github.com/urchade/GLiNER) -> Few shot deep learning NER
  * [GLiNKER](https://github.com/Knowledgator/GLinker) -> Entity linking framework combining NER, multi-layer database search, and neural entity disambiguation.
* [INDUS](https://huggingface.co/nasa-impact/nasa-smd-ibm-v0.1) -> NASA science tailored LLM suite
	* [paper](https://arxiv.org/html/2405.10725v2)
* [How to find key geoscience terms in text without mastering NLP using Amazon Comprehend](https://github.com/aws-samples/amazon-comprehend-energy-geoscience-nlp)
* [OzRock](https://github.com/majiga/OzROCK) - OzRock: A labeled dataset for entity recognition in geological (mineral exploration) domain
* [EntityTextMatchProject](https://github.com/zccodehub/EntityTextMatchProject)
  * [paper](https://link.springer.com/article/10.1007/s12145-026-02081-2) -> A deep learning matching method for geological spatial entities and descriptive texts
## Ontology
* [GAKG](https://github.com/geobrain-ai/gakg?tab=readme-ov-file) -> A Multimodal Geoscience Academic Knowledge Graph (Chinese)
* [GeoERE-Net](https://github.com/GISer-WB/GeoERE-Net) -> Understanding geological reports based on knowledge graphs using a deep learning approach
	* [paper](https://www.researchgate.net/publication/363408251_Understanding_geological_reports_based_on_knowledge_graphs_using_a_deep_learning_approach)
* [GeoFault Ontology](https://github.com/Yuanwei-Q/GeoFault-Ontology) 
* [geosim](https://github.com/smolang/SemanticObjects/tree/geosim) -> Semantically Triggered Qualitative Simulation of a Geological Process
	* [https://www.duo.uio.no/handle/10852/111467](Knowledge Modelling for Digital Geology) -> PhD thesis with two papers
	* [SIRIUS GeoAnnotator](http://158.37.63.37:8081/gic) -> Website example from above
* [Ontology CWS](https://github.com/cugdeeplearn/OntologyCWS)
* [Stratigraphic Knowledge Graph (StraKG)](https://github.com/IGCCP/StraKG)
	* [paper](https://www.sciencedirect.com/science/article/pii/S2590197424000119)
## Spelling
* [pyenchant](https://github.com/pyenchant/pyenchant) -> spelling checker

## Large Language Models
* [GeoChat](https://github.com/mbzuai-oryx/geochat) -> grounded Large Vision Language Model for Remote Sensing
* [GeoGalactica](https://github.com/geobrain-ai/geogalactica) -> A Larger foundation language model in Geoscience
	* [technical report](https://arxiv.org/abs/2401.00434)
* [GeoLLM](https://github.com/AshkanTaghipour/GeoLLM-Qwen3.5-FineTune) -> Qwen3.5-FineTune on WA Exploration Reports
* [Geo-MAG](https://github.com/Geo3D-AI-CSU/Geo-MAG) -> Knowledge Graph-Enhanced Multimodal Retrieval-Augmented Generation Framework for Geological Map Understanding
  * [paper](https://onlinelibrary.wiley.com/doi/abs/10.1111/tgis.70226)
* [GeoMinLM](https://github.com/wangcug/GeoMinLM) -> GeoMinLM: A Large Language Model in Geology and Mineral Survey in Yunnan Province
  * [paper](https://www.sciencedirect.com/science/article/pii/S0169136825001982)
* [JiuZhou](https://github.com/THU-ESIS/JiuZhou) -> Open Foundation Language Models for Geoscience
  * [paper](https://www.tandfonline.com/doi/pdf/10.1080/17538947.2025.2449708)
* [LAGDAL](https://github.com/JustinGOSSES/LAGDAL) -> LLM Matching geology map information to location experiments
* [Large Language Model for Geoscience](https://github.com/davendw49/k2)
	* [Learning Foundation Language Models for Geoscience Knowledge Understanding and Utilization paper](https://arxiv.org/pdf/2306.05064.pdf)
* [MetalGPT](https://huggingface.co/nn-tech/MetalGPT-1) ->  built on Qwen/Qwen3-32B and incorporates both continual pre-training and supervised fine-tuning on domain-specific data from mining and metallurgy (Norilsk)
  * [4-bit Quant](https://huggingface.co/nn-tech/MetalGPT-1-AWQ)
* [OmniGeo](https://arxiv.org/abs/2503.16326) -> Towards a Multimodal Large Language Models for Geospatial Artificial Intelligence
* [GeoAssist](https://github.com/PCleverleyGeol/GeoAssist---An-open-source-autonomous-research-agent-for-geoscience-data-and-literature) ->  

### Chatbots
* [GeoGPT](https://geogpt.deep-time.org/universal-login) -> Deep Time Digital Earth Research Group from China project
* [GeoGPT](https://geogpt.zero2x.org/) -> Deep Time Digital Earth Research Group from China project
* [GeoGPT-Research-Project](https://github.com/GeoGPT-Research-Project/GeoGPT)
  * [RAG Report](https://arxiv.org/pdf/2509.09686)

### Cross-Section
* [GeoSirr](https://github.com/CPG-KFUPM/GeoSIRR) -> Translate free-form geological narratives into structured, coordinate-based cross-section geometries
  * [GeoSIRR: Geological Section Interpretation, Reconstruction & Refinement](https://zenodo.org/records/18097054) -> Zenodo Code 
  * [paper](https://egusphere.copernicus.org/preprints/2026/egusphere-2025-6545/) -> GeoSIRR 1.0: Conversational Geological Cross-Section Modeling Using Large Language Models 


### Agents
* [GeoAgent](https://github.com/Yusin2Chen/GeoAgent) -> An LLM Agent for Automatic Geospatial Data Analysis
  * [paper](https://arxiv.org/abs/2410.18792)

# Remote Sensing
* [AiTLAS](https://github.com/biasvariancelabs/aitlas-arena) -> an open-source benchmark suite for evaluating state-of-the-art deep learning approaches for image classification in Earth Observation
* [CIMAE](https://github.com/Modexus/torchgeo) -> CIMAE - Channel Independent Masked Autoencoder
 * [fork](https://github.com/RichardScottOZ/torchgeo-cimae) -> to give it the name for reference
 * [Self-Supervised Representation Learning for Remote Sensing] -> Master's thesis includes the above and comparisons of several models
* [CNN Sentinel](https://github.com/jensleitloff/CNN-Sentinel) -> Overview about land-use classification from satellite data with CNNs based on an open dataset
* [Core-JEPA: LeJEPA for Earth Observation]()
* [DEA notebooks](https://github.com/GeoscienceAustralia/dea-notebooks/tree/develop/Real_world_examples/Scalable_machine_learning) -> Scalable machine learning example but lots of useful things here
* [deep_learning_alteration_zones](https://github.com/sydney-machine-learning/deeplearning_alteration_zones)
  * [zenodo](https://zenodo.org/records/7792676)
  * [paper](https://www.researchgate.net/publication/391945910_Convolutional_Neural_Networks_for_Mineral_Prospecting_Through_Alteration_Mapping_with_Remote_Sensing_Data) -> Convolutional Neural Networks for Mineral Prospecting Through Alteration Mapping with Remote Sensing Data 
* [DS_UNet](https://github.com/SebastianHafner/DS_UNet) -> Unet fusing Sentinel-1 Synthetic Aperture Radar (SAR) and Sentinel-2 Multispectral Imager 
* [EASI cookbook notebooks](https://github.com/csiro-easi/easi-notebooks/) -> CSIRO Earth Analytics platform introductions for ODC style analysis
* [FSDFirner](https://github.com/Sichen-Lu/FSDFormer) -> FSDFormer: A Frequency-Selected Differential Fusion Transformer for Remote Sensing Image Spatiotemporal Fusion
  * [paper](https://ieeexplore.ieee.org/abstract/document/11124232)
* [GeoAI](https://github.com/opengeos/geoai) -> Artificial intelligence and geospatial intelligence - remote sensing
* [GeoTorchAI](https://github.com/wherobots/GeoTorchAI) -> GeoTorchAI: A Spatiotemporal Deep Learning Framework
* [GHFMP](https://github.com/RSFubolin/GFHMP) -> Gradual Fusion Framework of Hyperspectral, Multispectral, and Panchromatic Images Using a Novel Spatial–Spectral Cross-Fusion Network
  * [paper](https://ieeexplore.ieee.org/document/11126176)
* [Multi Pretext Masked Autoencoder (MP-MAE)](https://github.com/vishalned/MMEarth-train)
 * [data](https://github.com/vishalned/MMEarth-data)
 * [SamGIS](https://github.com/trincadev/samgis-be) -> Segment Anything applied to GIS
* [EarthFoundationModels](https://github.com/zhu-xlab/EarthFoundationModels)  -> On the foundations of Earth foundation models
  * [paper](https://www.nature.com/articles/s43247-025-03127-x) -> On the foundations of Earth foundation models
* [PCP](https://github.com/wchh-2000/PCP) -> Prompt-Based Cartographic-Level Polygonal Vector Extraction Framework for Remote Sensing Images
  * [paper](https://ieeexplore.ieee.org/abstract/document/11181141)
* [pytorcheo](https://github.com/earthpulse/pytorchEO -> Deep Learning for Earth Observation applications and research
* [pytorch cloud geotiff optimization](https://github.com/microsoft/pytorch-cloud-geotiff-optimization)
  * [paper](https://arxiv.org/pdf/2506.06235) -> Optimizing Cloud-to-GPU Throughput for Deep Learning With Earth Observation Data
* [SatMAE++](https://github.com/techmn/satmae_pp) -> Rethinking Transformers Pre-training for Multi-Spectral Satellite Imagery
  * [grid-mae](https://github.com/RichardScottOZ/grid-mae) -> Investigate using multiscale grids in a Vision Transformer Masked Autoencoder
* [SpecPool-Former](https://github.com/SineyHang/SpecPool-Former) ->  Research on hyperspectral remote sensing alteration mineral mapping using an improved ViT model
  * [paper]((https://www.sciencedirect.com/science/article/pii/S0098300425001876))
* [ScaleMae](https://github.com/bair-climate-initiative/scale-mae)
	* [paper](https://openaccess.thecvf.com/content/ICCV2023/papers/Reed_Scale-MAE_A_Scale-Aware_Masked_Autoencoder_for_Multiscale_Geospatial_Representation_Learning_ICCV_2023_paper.pdf)
* [segment-geospatial](https://github.com/opengeos/segment-geospatial) -> Segment anything for geospatial uses
* [U Barn](https://src.koda.cnrs.fr/iris.dumeur/ssl_ubarn)
	* [paper](https://www.researchgate.net/publication/377712228_Self-Supervised_Spatio-Temporal_Representation_Learning_Of_Satellite_Image_Time_Series) 
* [earthnets](https://earthnets.nicepage.io/ )
* [Segmentation Gym](https://github.com/Doodleverse/segmentation_gym) ->  Gym is designed to be a "one stop shop" for image segmentation on "N-D" - any number of coincident 
* [SynFSNet](https://github.com/Xinmu-Tantai/SynFSNet/tree/main) -> SynFSNet AFSIFormer: Adaptive Frequency–Spatial Interaction Attention Mechanism for Aerial Image Semantic Segmentation
  * [paper](https://ieeexplore.ieee.org/abstract/document/11126528)
bands in a multispectral image
* [awesome mining band ratio collection](https://github.com/rodreras/awesome-mining-band-ratio) -> collection of simple band ratio uses for highlight various minerals
## Foundation Models
* [awesome remote sensing foundation models](https://github.com/Jack-bo1220/Awesome-Remote-Sensing-Foundation-Models)
  * [ChatEarthNet](https://github.com/zhu-xlab/ChatEarthNet)
  * [Zenodo](https://zenodo.org/records/11004358)
    * [paper] -> a global-scale image–text dataset empowering vision–language geo-foundation models
 * [Clay](https://github.com/Clay-foundation/model) -> An open source AI model and interface for Earth
 * [CROMA](https://github.com/antofuller/CROMA) -> Remote Sensing Representations with Contrastive Radar-Optical Masked Autoencoders
  * [PAPER](https://arxiv.org/abs/2311.00566)
 * [GeoDINO]A Vision Foundation Model for Earth Observation Leveraging DINO Architecture and Sentinel-2 Multi-Spectral Data
 * [IBM-NASA-GEOSPATIAL Prithvi](https://huggingface.co/ibm-nasa-geospatial)
  * [Image segmentation by foundation model finetuning](https://github.com/NASA-IMPACT/hls-foundation-os) -> For Prithvi
 * [AM-RADIO: Agglomerative Vision Foundation Model](https://github.com/NVlabs/RADIO)
 * [nasa-ibm-ai4science/NASA-IBM-Lunar-Foundation-Model](https://huggingface.co/nasa-ibm-ai4science/NASA-IBM-Lunar-Foundation-Model) -> nasa-ibm-ai4science/NASA-IBM-Lunar-Foundation-Model
 	* [paper](https://arxiv.org/abs/2312.06709) ->  - Reduce All Domains Into One
 * [RemoteCLIP](https://github.com/ChenDelong1999/RemoteCLIP) -> A Vision Language Foundation Model for Remote Sensing
 * [SpectralGPT](https://github.com/danfenghong/IEEE_TPAMI_SpectralGPT)
  * [zenodo](https://zenodo.org/records/8412455))  -> remote sensing foundation model customized for spectral data
 	* [paper](https://ieeexplore.ieee.org/document/10490262) -> Unseen
* [TerraFM](https://github.com/mbzuai-oryx/TerraFM) -> A Scalable Foundation Model for Unified Multisensor Earth Observation
  * [paper](https://arxiv.org/abs/2506.06281)
* [Terramind]  (https://github.com/IBM/terramind) -> any-to-any generative foundation model for Earth Observation
  * [paper](https://arxiv.org/abs/2504.11171) -> Terramind paper
* [Scaling Remote Sensing Foundation Models](https://arxiv.org/abs/2512.23903) -> paper

  
 ## Processing
 * [ASTER Conversion](https://git.earthdata.nasa.gov/projects/LPDUR/repos/aster-l1t/browse) -> Conversion from ASTER hd5 to geotiff NASA github
 * [HLS Data Resources](https://github.com/nasa/HLS-Data-Resources) -> Harmonized Landsat Sentinel wrangling
 * [sarsen](https://github.com/bopen/sarsen) -> xarray based SAR image processing and correction
 * [openEO](https://github.com/Open-EO) -> openEO develops an open API to connect R, Python, JavaScript and other clients to EO cloud back-ends
 
## Spectral Unmixing
* [Conventional-to-Transformer-for-Hyperspectral-Image-Classification-Survey-2024](https://github.com/mahmad00/Conventional-to-Transformer-for-Hyperspectral-Image-Classification-Survey-2024)
	* [paper](https://arxiv.org/abs/2404.14955)
* [Hyperspectral Deep Learning Review](https://github.com/mhaut/hyperspectral_deeplearning_review)
* [Hyperspectral Autoencoders](https://github.com/RichardScottOZ/hyperspectral-autoencoders)
* [Deeplearn HSI](https://github.com/hantek/deeplearn_hsi)
* [3DCAE-hyperspectral-classification](https://github.com/MeiShaohui/3DCAE-hyperspectral-classification)
* [DeHIC](https://github.com/jingge326/DeHIC)
* [Rev-Net](https://github.com/Lab-PANbin/Rev-Net)
	* [paper](https://ieeexplore.ieee.org/document/10536904) -> A Reversible Generative Network for Hyperspectral Unmixing With Spectral Variability
* [Pysptools](https://github.com/RichardScottOZ/pysptools) -> also has useful heuristic algorithms
* [Spectral Python](https://github.com/spectralpython/spectral)
* [Spectral Dataset RockSL](https://github.com/RichardScottOZ/spectral-dataset-RockSL) -> Open spectral dataset
* [Unmixing](https://github.com/RichardScottOZ/unmixing)
* [Unmamba](https://github.com/Preston-Dong/UNMamba) -> Cascaded Spatial–Spectral Mamba for Blind Hyperspectral Unmixing
  * [paper](https://ieeexplore.ieee.org/document/10902420)

A Joint Multi-Scale Graph Attention and Classify-Driven Autoencoder Framework for Hyperspectral Unmixing

## Hyperspectral
* [CasFormer: Cascaded Transformers for Fusion-aware Computational Hyperspectral Imaging](https://github.com/danfenghong/Information_Fusion_CasFormer)
* [Spectral Normalization for Keras](https://github.com/IShengFang/SpectralNormalizationKeras) 
	* [paper](https://arxiv.org/abs/1802.05957)
* [S^2HM^2](https://github.com/tulilin/S2HM2) -> S2HM2: A Spectral-Spatial Hierarchical Masked Modeling Framework for Self-Supervised Feature Learning and Classification of Large-Scale Hyperspectral Image
	* [paper](https://ieeexplore.ieee.org/abstract/document/10508226)


## Visualisation
* [Deep Colormap Extraction from Visualizations](https://github.com/yuanlinping/deep_colormap_extraction)
	* [paper](https://arxiv.org/pdf/2103.00741.pdf)
* [Semantic Segmentation for Extracting Historic Surface Mining Disturbance from Topographic Maps](https://github.com/maxwell-geospatial/topoDL) -> Example is for coal mines
	* [paper](https://www.mdpi.com/2072-4292/12/24/4145)
* [International Chronostratigraphic Color Codes](https://stratigraphy.org/chart) -> RGB codes and others in spreadsheet and other formats
* [LithClass](https://mrdata.usgs.gov/catalog/lithrgb.txt) -> USGS version of lithology color codes
 * [color version](https://mrdata.usgs.gov/catalog/lithclass-color.php)
* [SeisWiz](https://github.com/amustafa9/SeisWiz) -> Lightweight python SEG-Y viewer

## Texture
* [Mineral Texture Classification Using Deep Convolutional Neural Networks: An Application to Zircons From Porphyry Copper Deposits](https://github.com/ChetanNathwani/zirconCNN)
	* [paper](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2022JB025933)
  
## Simulation
* [Intelligent Prospector](https://github.com/sisl/MineralExploration) -> Sequential data acquisition planning
 * [Zenodo](https://zenodo.org/records/6727378)
	* [paper](https://gmd.copernicus.org/articles/16/289/2023/gmd-16-289-2023.html)
	
## Geometry
* [Deep Angle](https://github.com/ArashRabbani/DeepAngle) -> Fast calculation of contact angles in tomography images using deep learning	

## Other
* [Network Analysis of Mineralogical Systems](https://github.com/lic10/DTDI-DataAnalysis)
  * [Data](http://www.minsocam.org/MSA/AmMin/TOC/2017/Aug2017_data/AM-17-86104.zip) -> Data from paper here
* [GeospanNN](https://github.com/WentaoZhan1998/geospaNN) 
  * [paper](https://www.tandfonline.com/doi/abs/10.1080/01621459.2024.2356293) -> Neural Networks for Geospatial Data
* [Geoanalytics and machine learning](https://github.com/victsnet/Geoanalytics-and-Machine-Learning)
* [Machine Learning Subsurface](https://github.com/PyBrown/Machine-Learning)
* [ML Geoscience](https://github.com/DIG-Kaust/MLgeoscience)
* [Be a Geoscience Detective](https://github.com/bluetyson/Be-a-geoscience-detective)
* [Earth ML](http://earthml.holoviz.org/tutorial/Machine_Learning.html) -> Some basic tutorials in PyData approaches
* [GeoMLA](https://github.com/thengl/GeoMLA) -> Machine Learning algorithms for spatial and spatiotemporal data
* [open-geospatial](https://github.com/opengeos/python-geospatial) -> Install multiple common packages at once


## Platforms

## Guides
* [Geospatial CLI](https://github.com/JakobMiksch/geospatial-cli) - List of geospatial command line tools 
* [Satellite Image Deep Learning](https://github.com/robmarkcole/satellite-image-deep-learning)
* [Earth Observation](https://github.com/RichardScottOZ/awesome-earthobservation-code)
* [Earth Artificial Intelligence](Awesome-Earth-Artificial-Intelligence)
* [Open Source GIS](https://link.springer.com/chapter/10.1007/978-3-030-53125-6_30) -> Comprehensive overview of the ecosystem

# Data Quality
* [Geoscience Data Quality for Machine Learning](https://github.com/RichardScottOZ/Geoscience-Data-Quality-for-Machine-Learning) -> Geoscience Data Quality for Machine Learning Package
* [Australian Gravity Data](https://github.com/RichardScottOZ/australia-gravity-data) -> Overview and analysis of gravity station data
* [Geodiff](https://github.com/MerginMaps/geodiff) -> Comparison of vector data
* [Redflag](https://github.com/agilescientific/redflag) -> Analysis of data and an overview to detect problems
# Machine Learning
* [CuML](https://github.com/rapidsai/cuml) -> CUDA accelerated
  * [scikit-learn acceleration notebook](https://colab.research.google.com/github/rapidsai-community/showcase/blob/main/getting_started_tutorials/cuml_sklearn_colab_demo.ipynb#scrollTo=fqJC2jtmqpva)
* [Dask-ml](https://github.com/dask/dask-ml) -> Distributed versions of some common ML algorithms
	* [paper](https://joss.theoj.org/papers/10.21105/joss.06889.pdf)
* [geospatial-rf](https://github.com/BritishGeologicalSurvey/geospatial-rf) -> Functions and wrappers to assist with random forest applications in a spatial context
* [Geospatial-ml](https://github.com/giswqs/geospatial-ml) -> Install multiple common packages at once

# Latent Space
* [Nested Fusion](https://github.com/pixlise/NestedFusion)
	* [paper](https://github.com/pixlise/NestedFusion/blob/main/24_KDD_Nested_Fusion_paper.pdf) -> Nested Fusion: Dimensionality Reduction and Latent Structure Analysis of Multi-Scale Nested Data for M2020 PIXL RGBU and XRF Data
## Metrics
* [scores](https://github.com/nci/scores) -> Verifying and evaluating models and predictions with xarray
## Probabilistic
* [NG Boost](https://github.com/stanfordmlgroup/ngboost) -> probabilistic regression
* [Probabilistic ML](https://github.com/ZhiqiangZhangCUGB/Probabilistic-machine-learning)
* [Bagging PU with BO](https://github.com/ZhiqiangZhangCUGB/Bagging-PU-with-BO) -> Positive Unlabeled Bagging with Bayesian Optimisation
## Spatial
* [Spatial-Random-Forest](https://github.com/AhmedMerz/Spatial-Random-Forest)
  * [paper](https://link.springer.com/article/10.1007/s10596-025-10388-0) -> Beyond random forest: how spatial bagging and spatial random forest dominate for subsurface applications?
## Clustering  
### Self Organising Maps
* [GisSOM](https://github.com/RichardScottOZ/GisSOM) -> Geospatial centred Self Organising Maps from Finland Geological Survey
  * [paper](https://www.lyellcollection.org/doi/pdf/10.1144/geochem2024-055) -> example of GisSOM example
* [SimpSOM](https://github.com/fcomitani/SimpSOM) -> Self Organising Maps 
### GPU Accelerated
* [GPU_PROCLUS](https://github.com/jakobrj/GPU_PROCLUS) -> gpu accelerated kmediods variant on subspaces
  * [GPU_PROCLUS](https://github.com/RichardScottOZ/GPU_PROCLUS) -> Windows 11 / MVCC version
### Self Organising Maps
* [TorchSOM](https://github.com/RichardScottOZ/TorchSOM) -> Self Organising Maps in Torch
* [aweSOM](https://github.com/tvh0021/aweSOM/tree/public-release) -> Accelerated Self-organizing Map (SOM) and Statistically Combined Ensemble (SCE)
  * [paper](https://joss.theoj.org/papers/10.21105/joss.07613)

### Other
* [hdbscan](https://github.com/scikit-learn-contrib/hdbscan)
* [kmedoids](https://github.com/letiantian/kmedoids)
  * [kmedoids](https://github.com/kno10/python-kmedoids)
* [Picasso](https://github.com/pachterlab/picasso)
### Bayesian
* [Bayseg](https://github.com/cgre-aachen/bayseg) -> Spatial segmentation
## Explainability
* [InterpretML](https://github.com/interpretml/interpret) -> Interpreting models of tabular data
 * [InterpretML](https://github.com/interpretml/interpret-community) -> Community addition

## Deep Learning
* [Deep Colormap Extraction](https://github.com/RichardScottOZ/deep_colormap_extraction) -> Trying to extract a data scale from pictures
* [Extract and Classify Images from Geoscience Documents](https://github.com/bolgebrygg/extract-and-classify-images-from-geoscience-documents)
### Data
* [Xbatcher](https://github.com/RichardScottOZ/xbatcher) -> Xarray based data reading for deep learning
	* [Cloud native data loaders for machine learning using Zarr and Xarray](https://earthmover.io/blog/cloud-native-dataloader)
* [zen3geo](https://github.com/weiji14/zen3geo) -> Xbatcher style data science with pytorch
### Explainability
* [Shap Values](https://github.com/slundberg/shap)
* [Weight Watcher](https://github.com/CalculatedContent/WeightWatcher) -> Analyse how well networks are trained
 * [weightwatcher.ai](https://weightwatcher.ai/)
 * [weightwatcher-ai.com](https://weightwatcher-ai.com/) -> Professional web version
### Self-supervised learning
* [Self Supervised](https://github.com/untitled-ai/self_supervised) -> Pytorch lightning implementations of multiple algorithms
* [Simclr](https://github.com/google-research/simclr)
* [Awesome self-supervised learning](https://github.com/jason718/awesome-self-supervised-learning) -> Curated list
### Hyperparameters
* [Hyperopt](https://github.com/hyperopt/hyperopt)
* [TPOT Automated ML](https://github.com/trhallam/tpot)
  
## Coding Environments
* [DEA Sandbox](https://docs.dea.ga.gov.au/setup/Sandbox/sandbox.html)
* [Cube In A Box](https://github.com/RichardScottOZ/cube-in-a-box)

# Community
* [Software Underground](https://softwareunderground.org/) - Community of people interested in exploring the intersection of the subsurface and code
  * [Chat Signup](https://softwareunderground.org/mattermost) - SWUNG community chat signup
  * [Mattermost](https://mattermost.softwareunderground.org/)- Community chat service
	* [Old Slack Channel](https://softwareunderground.org/slack)(deprecated, see mattermost above)
  * [Geoscience Open Source Tie-In](https://github.com/RichardScottOZ/gostin)
  * [Videos](https://www.youtube.com/c/SoftwareUnderground/videos)
    * [Transform 2022](https://www.youtube.com/playlist?list=PLgLft9vxdduDFkG9gtuNicNmb2YUzWqSQ)
  * [Awesome Open Geoscience](https://github.com/softwareunderground/awesome-open-geoscience )[note Oil and Gas Biased]
  * [Transform 2021 Hacking Examples](https://github.com/RichardScottOZ/Transform-2021)
  * [Segysak 2021 Tutorial](https://github.com/trhallam/segysak-t21-tutorial)
  * [T21 Seismic Notebook](https://github.com/stevejpurves/t21-seismic-notebook)
  * [Practical Seismic with Python](https://github.com/gmac161/practical-seismic-t21-tutorial)
  * [Transform 2021 Simpeg](https://github.com/simpeg/transform-2021-simpeg)
* [Pangeo](https://pangeo.io/)
  * [Forum](https://discourse.pangeo.io/)
  * [COG Best Practices](https://github.com/pangeo-data/cog-best-practices)
* [Digital Earth Australia](https://www.dea.ga.gov.au/)
  * [Slack Channel](https://opendatacube.slack.com/)
* [Open Source Geospatial Foundation](https://github.com/OSGeo/osgeo)
 * [OSGeoLive](https://github.com/OSGeo/OSGeoLive) -> Bootable DVD/USB with lots of open source geospatial software
* [ASEG](https://www.youtube.com/c/ASEGVideos/videos) -> videos from Australia Society of Exploration Geoscientists
* [AI for Geological Modelling and Mapping](https://www.youtube.com/@AI-GMM/videos) -> videos from the conference day
 * [conference](https://www.exeter.ac.uk/research/institutes/idsai/events/artificialintelligenceforgeologicalmodellingandmapping22-23may2024/)

# Cloud Providers
## AWS
* [ec2 Spot Labs](https://github.com/awslabs/ec2-spot-labs) -> Making automatically working sith Spot instances easier
* [Sagemaker Geospatial ML](https://aws.amazon.com/sagemaker/geospatial/)
* [Sagemaker](https://github.com/aws/amazon-sagemaker-examples) -> ML Managed Service
  * [SDK](https://github.com/aws/sagemaker-python-sdk)
  * [Entrypoint Utilities](https://github.com/aws-samples/amazon-sagemaker-entrypoint-utilities)
  * [Workshop 101](https://github.com/RichardScottOZ/sagemaker-workshop-101)
  * [Training Toolkit](https://github.com/aws/sagemaker-training-toolkit)
### Batch
* [Shepard](https://github.com/RichardScottOZ/shepard) -> Automated cloud formation setup of AWS Batch Pipelines: this is great
### Packages
* [Mlmax](https://github.com/awslabs/mlmax) - Start fast library
* [Smallmatter](https://github.com/aws-samples/smallmatter-package)
* [Pyutil](https://github.com/verdimrc/pyutil)
## General
* [Deep Learning Containers](https://github.com/aws/deep-learning-containers)
* [Loguru](https://github.com/Delgan/loguru) -> Logging library
* [AWS GDAL Robot](https://github.com/mblackgeo/aws-gdal-robot) -> Lambda and batch processing of geotiffs
* [Serverless Seismic Processing](https://github.com/vavourak/serverless_seismic_processing)
* [Lithops](https://github.com/lithops-cloud/lithops) -> multi-cloud distributed computing framework

# Overviews
* [Mineral Exploration](https://www.ga.gov.au/scientific-topics/minerals/mineral-exploration)
## Domains
* [Geology](https://en.wikipedia.org/wiki/Geology)
  * [Geologic Ages](https://en.wikipedia.org/wiki/Geologic_time_scale)
  * [Lithology](https://en.wikipedia.org/wiki/Lithology)
  * [Stratigraphy](https://en.wikipedia.org/wiki/Stratigraphy) 
* [Geochemistry](https://en.wikipedia.org/wiki/Geochemistry)
* [Geophysics](https://en.wikipedia.org/wiki/Geophysics)
* [Remote Sensing](https://en.wikipedia.org/wiki/Remote_sensing)

# Web Services
If listed it is assumed they are generally data, if just pictures like WMS it will say so.

## World
* [Critical Minerals and Deposits](https://portal.ga.gov.au/metadata/geochemistry/inorganic-geochemistry/critical-minerals-deposits-and-geochemistry/345cfeb7-9832-4c95-9f2e-59ec20cb1d91)
* [PANGAEA](https://www.pangaea.de/api/v1/) -> Data Publisher for Earth & Environmental Science

## Australia
* [AusGIN](https://www.geoscience.gov.au/web-services)
* [Geoscience Australia](http://services.ga.gov.au/)
 * [Mineral Potential](https://ecat.ga.gov.au/geonetwork/srv/api/records/f4bd18f3-5688-4c4d-8072-bdedc49a29e6) -> WMS
* [Geoscience Australia Catalogue Service](https://ecat.ga.gov.au/geonetwork/srv/eng/csw?request=GetCapabilities&service=CSW&acceptVersions=2.0.2&acceptFormats=application%2Fxml)
### Geology
* [AUSLAMP](http://services.ga.gov.au/gis/rest/services/AusLAMP_TISA_Stations/MapServer) - > Tennant Creek - MtIsa
* [Field Geology](https://services.ga.gov.au/gis/field-geology/wfs)
* [Deep Lithosphere](http://deep-lithospheric-structure.gs.cloud.ga.gov.au/ows) -> Deep Lithospheric Mineral Potential
* [Geochronology](http://geochronology-isotopes.gs.cloud.ga.gov.au/ows) -> Geochronology
* [Geological Provinces](https://services.ga.gov.au/gis/services/australian_geological_provinces/mapserver/wfsserver?version=2.0.0)
* [WMS](https://services.ga.gov.au/gis/rest/services/Australian_Geological_Provinces/MapServer) -> WMS picture
* [EGGS](http://services.ga.gov.au/gis/eggs/wms) -> Estimates of Geological and Geophysical Surfaces
* [Chronostratigraphic Surfaces](https://services.ga.gov.au/gis/eggs/aus_chronostrat_v1/wms) -> 3D Chronostratigraphic Model of Australia 
* [Proterozoic Alkaline Rocks](https://services.ga.gov.au/gis/services/ProterozoicAlkalineAndRelatedIgneousRocksOfAustralia/MapServer/WFSServer) - Proterozoic Alkaline Rocks Dataset WFS {also has WMS}
 * [Cenozoic](https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/92b76dbc-95a7-4bf9-84f7-34d7602e66eb)
 * [Mesozoic](https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/e63b4771-cd18-4241-94b0-4e87708b4694)
 * [Paleozoic](https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/1f7163a7-12b0-44b1-bb8c-468641f34226)
 * [Archaean](https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/ae37b73a-d5d6-4a48-a4db-4bb6bc0aec39)
* [Stratigraphy](https://services.ga.gov.au/gis/stratunits/ows) -> Stratigraphic Units
### Geophysics
* [Geophysics Surveys](https://services.ga.gov.au/gis/geophysical-surveys/ows?VERSION=2.0.0)
* [Seismic Surveys](https://services.ga.gov.au/gis/rest/services/Australian_Geological_Provinces/MapServer) -> Onshore seismic surveys
* [Magnetotelluric](https://services.ga.gov.au/gis/magnetotellurics/wfs) -> Northern Australia AUSLAMP Stations
### Other
* [Ni-Cu-PEGE](http://services.ga.gov.au/gis/services/MineralPotentialMapper/MapServer/WMSServer) -> Intrusion hosted Nickel Copper PGE Deposits
* [EFTF Area](http://services.ga.gov.au/gis/rest/services/ExploringForTheFutureProjectAreas/MapServer) -> Exploring for the future areas
* [Temperature](http://services.ga.gov.au/gis/rest/services/OZTemp_Interpreted_Temperature_5km_Depth/MapServer) -> Interpreted temperature
* [DEA](https://ows.dea.ga.gov.au/) -> Digital Earth Australia
 * [Land Cover](https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/146197)
 * [Waterbodies](https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/146197)
* [BOM](https://hosting.wsapi.cloud.bom.gov.au/arcgis/rest/services/groundwater/Bore_Hydrochemistry/FeatureServer) -> Bureau of Meteorology Hydrogeochemistry
### New South Wales
* [NSW](https://www.regional.nsw.gov.au/meg/geoscience/products-and-data/gis-web-services)
 * [WCS](https://gs.geoscience.nsw.gov.au/geoserver/ows?version=1.1.0)
 * [WFS Mineral Drillholes](https://gs.geoscience.nsw.gov.au/geoserver/ows?service=wfs&version=1.1.0&request=GetCapabilities)
 * [WFS Petroleum Drillholes](https://gs.geoscience.nsw.gov.au/geoserver/ows?service=wfs&version=1.1.0&request=GetCapabilities)
 * [WFS Coal Drillholes](https://gs.geoscience.nsw.gov.au/geoserver/ows?service=wfs&version=1.1.0&request=GetCapabilities)
 * [Seismic](https://gs-mv.geoscience.nsw.gov.au/geoserver/gsnsw/ows?version=1.0.0&typeName=gsnsw:dw_seismic_lines&outputFormat=shape-zip) -> Seismic and others
### Queensland
* [Queensland](https://gisservices.information.qld.gov.au/arcgis/rest/services)
 * [Geoscientific](https://spatial-gis.information.qld.gov.au/arcgis/rest/services/GeoscientificInformation) -> Geophysics and Report Index
 * [Geology](https://spatial-gis.information.qld.gov.au/arcgis/rest/services/GeoscientificInformation/GeologyDetailed/MapServer)
  * [Regional](https://spatial-gis.information.qld.gov.au/arcgis/rest/services/GeoscientificInformation/GeologyRegional/MapServer)
  * [State](https://spatial-gis.information.qld.gov.au/arcgis/rest/services/GeoscientificInformation/GeologyState/MapServer)
 * [Tenements](https://spatial-gis.information.qld.gov.au/arcgis/rest/services/Economy/MineralTenement/FeatureServer)
 * [Roads](https://spatial-gis.information.qld.gov.au/arcgis/rest/services/Transportation/Roads/MapServer)
 * [Watercourse](https://spatial-gis.information.qld.gov.au/arcgis/rest/services/InlandWaters/WaterCoursesAndBodies/MapServer)
 
### South Australia
* [SARIG](https://map.sarig.sa.gov.au/MapViewer/StartUp/?siteParams=WebServicesWidget)
 * [Drillholes](https://services.sarig.sa.gov.au/vector/drillholes/wfs?version=1.1.0)
 * [Geology](https://services.sarig.sa.gov.au/vector/geology/wfs?version=1.1.0)
 * [Geophysics](https://services.sarig.sa.gov.au/vector/geophysical_data/wfs?version=1.1.0)
 * [Prospectivity](https://services.sarig.sa.gov.au/raster/ProspectivityModelling/wms?version=1.1.1)
 * [Minerals and Mines](https://services.sarig.sa.gov.au/vector/mines_and_mineral_deposits/wfs?version=1.1.0)
 * [Remote Sensing](https://services.sarig.sa.gov.au/raster/RemoteSensing/wms?version=1.1.1)
 * [Seismic](https://services.sarig.sa.gov.au/vector/south_australia_seismic_data/wfs?version=1.1.0)
 * [Tenements](https://services.sarig.sa.gov.au/vector/mineral_tenements/wfs?version=1.1.0)
### Northern Territory
* [NTGS](http://geology.data.nt.gov.au/geoserver/wfs) -> Northern Territory Geological Survey
### Tasmania
* [Tasmania WFS](https://www.mrt.tas.gov.au/products/digital_data/web_feature_service)
* [Tasmania REST](https://data.stategrowth.tas.gov.au/ags/rest/services)
 * [Boreholes](https://data.stategrowth.tas.gov.au/ags/rest/services/MRT/Boreholes_and_Traces/MapServer)
### Victoria
* [Victoria Geonetwork](http://geology.data.vic.gov.au/)
### Western Australia
* [Western Australia](https://services.slip.wa.gov.au/public/services/SLIP_Public_Services/Industry_and_Mining_WFS/MapServer/WFSServer)
 * [Rest](https://services.slip.wa.gov.au/public/rest/services/SLIP_Public_Services)
## New Zealand
* [GNS](https://maps.gns.cri.nz/) -> List of web services
 
## South America
### Brazil
* [Brazil Geoportal](https://geoportal.cprm.gov.br/server/rest/services)
* [Brazil CPRM](https://geoportal.cprm.gov.br/image/rest/services)
### Peru
* [Ingement](https://geocatmin.ingemmet.gob.pe/arcgis/rest/services)
 * [Mineral Occurrences](https://geocatmin.ingemmet.gob.pe/arcgis/rest/services/SERV_OCURRENCIA_MINERAL/MapServer)
* [Environmental](https://geo.serfor.gob.pe/geoservicios/rest/services)
### Mexico
* [GeoInfo](https://mapasims.sgm.gob.mx/arcgis/rest/services) -> Rest services
### Argentina
* [SIGAM](https://sigam.segemar.gov.ar/https://sigam.segemar.gov.ar/geoserver217/wfs)
### Colombia
* [Rest](https://srvags.sgc.gov.co/arcgis/rest/services)
 * [Deposits 2018](https://srvags.sgc.gov.co/arcgis/rest/services/Mapa_metalogenico_2018/Mapa_Metalogenico_2018/MapServer)
### Uruguay
* [Rest](http://mapas.dinamige.gub.uy/arcgis/rest/services)
### Other
* [SIG Andes](http://mapsref.brgm.fr/wxs/1GG/SIGAndes_BRGM) -> Andes geology

## Europe
[EGDI](maps.europe-geology.eu/wfs/) -> EGDI Minerals
### Britain
* [BGS](https://ogcapi.bgs.ac.uk/collections?f=html) -> British Geological Survey
 * [Geoindex](https://mapapps2.bgs.ac.uk/geoindex/home.html?topic=Minerals&_ga=2.203824336.1992427000.1668901218-659606051.1668901218) -> mineral occurrence example
 * [Rest](https://map.bgs.ac.uk/arcgis/rest/services) -> BGS Rest services
 * [Inspire 625](http://ogc.bgs.ac.uk/digmap625k_gsml_insp_gs/wfs?service=WFS&request=GetCapabilities&AcceptVersions=2.0.0)
### Czech Republic
* [Rest](https://ags.cuzk.cz/arcgis/rest/services/zm/MapServer?f=json)
### Denmark
* [deus](http://data.geus.dk/geusmap/ows/25832.jsp?whoami=[email]) -> Greenland WMS/WFS
* [Deus](https://data.geus.dk/geusmap/ows/help/?mapname=oil_and_gas&epsg=25832)  - Update? (needs checking)
* [Greemin](http://www.greenmin.gl/) -> Greenland mineral resources portal
### Iceland
[web map](https://www.map.is/os/@656678,471081,z0,0)
### Ireland
* [Rest](https://gsi.geodata.gov.ie/server/rest/services)
 * [Mineral Locations](https://gsi.geodata.gov.ie/server/rest/services/Minerals/IE_GSI_Mineral_Locations_IE26_ITM/MapServer/0)
### Finland
* [GTK](https://www.gtk.fi/en/services/data-sets-and-online-services-geo-fi/map-services/) -> Geological Survey of Finland
  * [Finland](https://gtkdata.gtk.fi/arcgis/rest/services)
    * [Bedrock Geology](http://gtkdata.gtk.fi/arcgis/services/Rajapinnat/GTK_Kalliopera_WFS/MapServer/WFSServer_)
	* [Geophysics](http://gtkdata.gtk.fi/ArcGIS/services/Rajapinnat/GTK_Geofysiikka_WMS/MapServer/WMSServer)
	* [Ground Surveys](http://gtkdata.gtk.fi/arcgis/services/Rajapinnat/GTK_Pohjatutkimukset_WMS/MapServer/WMSServer)
* [Arctic Minerals](http://13.95.69.121:80/geoserver/erl/ows) -> Arctic 1M Mineral Occurrences
### Germany
* [BRG](https://services.bgr.de/uebersicht/kurzlinks)
### Greenland
* [Greenmin](https://maps.greenmin.gl) -> Web map portal
### Hungary
* [MBFZ OGC](https://map.mbfsz.gov.hu/)
* [MBFZ Rest](https://map.mbfsz.gov.hu/arcgis/rest/services)
### Poland
* [Rest example](https://cbdgmapa.pgi.gov.pl/arcgis/rest/services/midas/MapServer/1?f=json) -> Many more mapservers
### Portugal
* [Portugal Geology](https://inspire.lneg.pt/arcgis/rest/services/CartografiaGeologica/CGP1M/MapServer)
 * [Mineral Occurrences](https://sig.lneg.pt/server/services/OcorrenciasMinerais/MapServer/WMSServer?request=GetCapabilities&service=WMS) -> WMS
 * [Cities and Town](https://inspire.lneg.pt/arcgis/rest/services/CartografiaGeologica/CGP1M/MapServer)
### Romania
* [IGR](https://inspire.igr.ro/geoserver/Test/wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities) -> WMS only
 * [IGR minres](https://inspire.igr.ro/geoserver/minerals4eu/wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities) -> WMS only
### Slovakia
* [Rest](https://gis.geology.sk/arcgis/rest/services)
### Spain
* [Spain](https://mapas.igme.es/gis/rest/services)
 * [Geology](https://mapas.igme.es/gis/rest/services/Cartografia_Geologica/IGME_Geologico_200/MapServer) -> 200K
  * [1M](http://mapas.igme.es/gis/rest/services/Cartografia_Geologica/IGME_Geologico_1M/MapServer) -> 1M
  * [50K](https://mapas.igme.es/gis/rest/services/Cartografia_Geologica/IGME_MAGNA_50/MapServer) -> 50K
  * [IGME Geode](https://mapas.igme.es/gis/rest/services/Cartografia_Geologica/IGME_Geode_50/MapServer)
 * [Geophysics](https://mapas.igme.es/gis/rest/services/BasesDatos/IGME_SIGEOF/MapServer)
 * [Copper](https://mapas.igme.es/gis/rest/services/AtlasGeoquimico/IGME_MapaIsovalores2012_Cu/MapServer) - Copper
 * [GeoFPI](https://mapas.igme.es/gis/rest/services/GeoFPI) - > Geology and Minerals South Portuguese Zone
 * [Water](https://mapas.igme.es/gis/rest/services/InfoIGME/AmbEsp_03/MapServer)
### Sweden
* [SGU Magnetics WMS](https://resource.sgu.se/service/wms/130/flyggeofysik-magnet)
* [SGU Uranium](https://resource.sgu.se/service/wms/130/flyggeofysik-gammastralning-uran)
* [SGU Borehole](https://api.sgu.se/oppnadata/borrhal/ogc/features/v1)
 * [Geophysics metadata](https://resource.sgu.se/dokument/produkter/geofysiska-flygmatningar-metadata-wms-beskrivning.pdf)
### Ukraine
* [Geoinform](https://geoinf.kiev.ua/wp/index.html) -> [currently suspended]

## North America
* [USGS Boreholes](https://services.arcgis.com/v01gqwM5QqNysAAi/ArcGIS/rest/services/NIBI_Borehole_Prod/FeatureServer/0)
### Canada
* [Manitoba](https://rdmaps.gov.mb.ca/arcgis/rest/services/MapGallery/MG_GEOLOGY_CLIENT/MapServer/)
* [Newfoundland & Labrador](https://dnrmaps.gov.nl.ca/arcgis/rest/services/GeoAtlas/Map_Layers/MapServer)
* [NWT](https://services3.arcgis.com/GSr8HAQhtEt4sNnv/arcgis/rest/services/)
  * [Rest](https://www.maps.geomatics.gov.nt.ca/Geocortex/Essentials/REST/sites/Spatial_Data_Warehouse/map)
  * [References](https://hosting.wsapi.cloud.bom.gov.au/arcgis/rest/services/groundwater/Bore_Hydrochemistry/FeatureServer)
* [Quebec](https://servicesvectoriels.atlas.gouv.qc.ca/IDS_SGM_WMS/service.svc/get)
* [Yukon](https://mapservices.gov.yk.ca/arcgis/rest/services/GeoYukon/GY_Geological/MapServer)
### USA
* [USGS World Mineral](https://mrdata.usgs.gov/services/wfs/ofr20051294?version=1.1.0)
* [USGS MRDS](https://mrdata.usgs.gov/services/mrds?request=getcapabilities&service=WFS&version=1.0.0&)
* [Minnesota](https://mngs-umn.opendata.arcgis.com/)
### Asia
* [China](http://data.ngac.org.cn/mineralresource/index.html?id=302c137ee126465095b3df8e68168d8c) -> WMS mineral deposit wap
 * [orefield](http://219.142.81.85/arcgis/rest/services/矿产地数据库2019/orefield2019/MapServer/0) -> Mineral occurrence points
* [India Mineral](https://bhukosh.gsi.gov.in/arcgis/services/Mineral/Mineral/MapServer/WmsServer) -> WMS
* [India Geophysics](https://bhukosh.gsi.gov.in/wms/en)
* [Korea](https://data.kigam.re.kr/mgeo/geoserver/ows?service=wfs&version=1.0.0&request=GetCapabilities)
* [ASEAN wms](https://geohazards-info.gsj.jp/amdis/index.php) -> no data, just picture
### Africa
* [Africa Geoportal](https://services8.arcgis.com/oTalEaSXAuyNT7xf/ArcGIS/rest/services) -> Rest services
* [Africa 10M](http://mapsref.brgm.fr/wxs/1GG/SIGAfrique_BRGM_Africa_MineralResources) -> Africa 10M Mineral Occurrences
https://pubs.usgs.gov/of/2005/1294/e/OF05-1294-E.pdf
* [IPIS Artisanal Mines](http://geo.ipisresearch.be/geoserver/wfs) - > There is a WMS version too
 * [github](https://github.com/IPISResearch)
* [Uganda](https://gmis.beak.de/geoserver/uganda/wms?VERSION=1.3.0) -> GMIS WMS

### General
* [Mineral Exploration Web Services](https://github.com/jack-tuna/Mineral_Exploration_Web_Services) -> QGIS plugin with access to many relevant web services

## Other
* [Open Street Map](https://tile.openstreetmap.org/{z}/{x}/{y}.png) -> useful general tile service

# APIs
* [Open Data API](https://github.com/RichardScottOZ/open-data-api) -> GSQ Open Data Portal API
  * [Geochemistry parsing](https://github.com/geological-survey-of-queensland/geochemistry_parsing)
* [CORE](https://core.ac.uk/data) -> Open Research Texts
  * [API Notebook](https://colab.research.google.com/drive/1_bjqDQhqj7AnSfoCAXDCMOnGZLPQWKfu?usp=sharing) -> Example and fucntions
* [SHARE](https://share.osf.io/discover?q=mineral%20AND%20exploration) -> Open Science API
* [USGS Publications](https://pubs.er.usgs.gov/documentation/web_service_documentation)
* [CROSSREF](https://api.crossref.org/swagger-ui/index.html)
* [xDD](https://xdd.wisc.edu/api/v1) -> former GeoDeepDive
 * [ADEPT](https://xdd.wisc.edu/adept/) -> GUI to xDD to search 15M harvested papers
* [OpenAlex](https://docs.openalex.org/api)
  * [api](https://api.openalex.org/)
  * [diophila Python Library](https://github.com/smierz/diophila)
  * [Python Library](https://github.com/dpriskorn/OpenAlexAPI)
 	* [paper](https://arxiv.org/abs/2205.01833)
* [Macrostrat](https://macrostrat.org/api)
	* [paper](https://rmets.onlinelibrary.wiley.com/doi/10.1002/gdj3.189) 
  * [Macrostrat-xvec](https://github.com/RichardScottOZ/macrostrat-xvec) -> Macrostrat style data adaptation to xarray xvec
* [OpenMinData](https://github.com/ChuBL/OpenMindat) -> facilitate querying and retrieving data on minerals and geomaterials from the Mindat API
* [Iceland Geological Society](https://api.orkustofnun.is/)
 
# Data Portals
## World
* [Earth Model Collaboration](https://ds.iris.edu/ds/products/emc/) -> access to various Earth models, visualization tools for model preview, facilities to extract model data/metadata and access to the contributed processing software and scripts.
* [ISC Bulletin](https://www.isc.ac.uk/iscbulletin/search/fmechanisms/) -> Earthquake focal mechanism search
* [Magnetics Information Consortium](https://www2.earthref.org/MagIC/search) -> paleomagnetic, geomagnetic, rock magnetic
* [Earthchem](https://www.earthchem.org/) -> Community-driven preservation, discovery, access, and visualization of geochemical, geochronological, and petrological data
* [PANGAEA](https://www.pangaea.de/) -> Earth and environmental science data 

## Australia
### Geoscience Australia
* [Geoscience Australia Data Catalogue](https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/)
 * [AusAEM](https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/search?resultType=details&sortBy=relevance&fast=index&_content_type=json&from=1&to=20&title_OR_altTitle_OR_any=AusAEM)
* [Geoscience Australia Portal](https://portal.ga.gov.au/)
 * [Exploring for the Future Portal](https://portal.ga.gov.au//eftf) -> Geoscience Australia web portal with download information
  * [AusAEM](https://www.eftf.ga.gov.au/ausaem)
  * [AusLAMP](https://www.eftf.ga.gov.au/auslamp)
 * [Geochronology and Isotopes](https://portal.ga.gov.au/persona/geochronology)
 * [Hydrogeology Catchments](https://portal.ga.gov.au/) -> search for catchments layer
 * [Critical Minerals Mapping Initiative](https://portal.ga.gov.au/persona/cmmi)
 * [Australian Stratigraphic Units](https://asud.ga.gov.au/search-stratigraphic-units)
  * [Australian Borehole Stratigraphic Units](https://ecat.ga.gov.au/geonetwork/srv/eng/catalog.search#/metadata/147641) -> Compilation for groundwater of sedimentary units
 * [Geoscience Australia Geophysics thredds](https://dapds00.nci.org.au/thredds) -> OpendDAP and https access
 * [MORPH gdb](https://github.com/Neil-Symington/MORPH_gdb) -> Officer Musgrave drilling data
### CSIRO
* [CSIRO Data Access Portal](https://data.csiro.au/)
 * [Regolith Depth](https://data.csiro.au/collection/csiro:11393)
 * [TWI](https://data.csiro.au/collection/csiro:5588?_st=browse&_str=1&_si=1&browseType=kw&browseValue=Topographic%20Wetness%20Index) -> Topographic Wetness Index
* [ASTER Geoscience Maps](https://confluence.csiro.au/public/SpecSens/aster-geoscience-maps) -> Website
	* [FTP](ftp://ftp.arrc.csiro.au/arrc/Australian_ASTER_Geoscience_Map/) -> CSIRO ftp site
	* [ASTER Maps notes](https://confluence.csiro.au/public/SpecSens/files/276430859/276430921/1/1426138425933/Australian+ASTER+Geoscience+Product+Notes+FINALx.pdf) -> Notes for the above
### AuScope
* [3D Geology](http://geomodels.auscope.org.au/) -> Models from multiple areas
### TERN
* [Enhanced Bare Earth Covariates for Soil and Lithological Modelling](https://portal.tern.org.au/metadata/21910)
### Bureau of Meteorology
* [Groundwater Explorer](http://www.bom.gov.au/water/groundwater/explorer/map.shtml) -> Bureau of Meteorology
### Foundational Spatial Data
* [Elvis](https://elevation.fsdf.org.au/)
### South Australia
* [SARIG](https://map.sarig.sa.gov.au/) -> South Australia Geological Survey geospatial map based search
* [SARIG Catalogue](https://catalog.sarig.sa.gov.au/geonetwork/srv/eng/catalog.search#/search) -> data catalogue
  * [3D Models](https://catalog.sarig.sa.gov.au/geonetwork/srv/eng/catalog.search#/search?facet.q=type%2Fmodel&resultType=details&sortBy=popularity&from=1&to=20&fast=index&_content_type=json)
	* [SA Wide](https://sarigbasis.pir.sa.gov.au/WebtopEw/ws/samref/sarig1/cat0/Record?w=catno%3D2036881+OR+catno%3D2036883+OR+catno%3D2036887&sid=c2ca73f5685c43249e6c1ab5ec7dc2e5&set=1&m=3)
	 * [s3 location](https://dsd-gdp.s3.amazonaws.com/GDP00022.zip)
  * [Data Packages](https://dem-sdp.s3-ap-southeast-2.amazonaws.com/index.html) - Annual update
  * [s3 Reports](http://mer-env.s3-website-ap-southeast-2.amazonaws.com/) -> Reports and textracted versions in s3 bucket with web interface)
  * [Reports](https://sarigbasis.pir.sa.gov.au/WebtopEw/ws/samref/sarig1/cat0/MSearch;jsessionid=492C6538B64080CE8B13E91C79F8B1BA)
  * [Seismic](https://www.petroleum.sa.gov.au/data-centre/seismic-data)
    * [Seismic downloads](https://sarigbasis.pir.sa.gov.au/WebtopEw/ws/segy2d/web/segy/ResultSet?siblingtreeid=e6d6d3af10d149d39ba2141b9d1ce660&sid=6fac787ca578408bad6cfb514eb15498&order=NATIVE%28%27LINE%2Fascend%27%29&rpp=-1&set=1&reorder=1&bclabel=Result+Set) -> One page of links
### Northern Territory
* [STRIKE](https://strike.nt.gov.au/wss.html) -> Northern Territory Geological Survey
* [GEMIS](https://geoscience.nt.gov.au/gemis/)
  * [McArthur Basin](https://geoscience.nt.gov.au/gemis/ntgsjspui/handle/1/81751) -> 3D Model
  * [Geophysical Surveys](https://geoscience.nt.gov.au/downloads/NTWideDownloads.html)
  * [Geophysics](https://geoscience.nt.gov.au/gemis/ntgsjspui/handle/1/81428) -> reference
  * [Drilling and Geochemistry](https://geoscience.nt.gov.au/gemis/ntgsjspui/handle/1/81743) -> reference
	  * [Data Package](https://geoscience.nt.gov.au/gemis/ntgsjspui/bitstream/1/81743/2/DIP001.zip) -> data package
### Queensland
* [Geological Survey of Queensland](https://geoscience.data.qld.gov.au/)
* [Geophysical Surveys](http://qldspatial.information.qld.gov.au/catalogue/custom/search.page?q=%22Airborne%20geophysical%20survey%20-%20Queensland%22)
* [Drilling and geochemistry](https://geoscience.data.qld.gov.au/data/geochemistry/whole-of-queensland-geochemistry-databases)
### Western Australia
* [GEOVIEW](https://geoview.dmp.wa.gov.au/geoview/?Viewer=GeoView) -> Western Australia Geological Survey
* [DMIRS](https://dasc.dmirs.wa.gov.au/) -> DMIRS Data and Software Centre
 * [Download URLS](https://dasc.dmirs.wa.gov.au/Download/File/3599) -> dataset of download links
* [Drilling and Geochemistry](https://wamexgeochem.net.au/)
 * [Download package](https://exp-gswa-mdhdb-bkt01.s3.ap-southeast-2.amazonaws.com/GSWA_Nov2022_FlatTables.zip) - improvement?
 * [Geochemistry](https://wamexgeochem.net.au/)
 * [Petroleum Wells with depths](https://wapims.dmp.wa.gov.au/WAPIMS/)
* [data WA subset](https://catalogue.data.wa.gov.au/org/department-of-mines-industry-regulation-and-safety)
## NSW
* [MINVIEW](https://minview.geoscience.nsw.gov.au/) -> New South Wales Geological Survey
* [DiGS](https://search.geoscience.nsw.gov.au/) -> Publications and Geotechnical collections
## Tasmania
* [MRT](https://www.mrt.tas.gov.au/products)
* [MRT Maps](https://www.mrt.tas.gov.au/mrt_maps/app/list/map) -> Webmap
## Victoria
* [Earth Resources](https://earthresources.vic.gov.au/geology-exploration/maps-reports-data)
  * [Geophysics](http://earthresources.efirst.com.au/categories.asp?cID=13)
* [GeoVIC](https://earthresources.vic.gov.au/geology-exploration/maps-reports-data/geovic) -> Webmaps needs registration to be more useful
## New Zealand
* [Exploration Database](https://data.nzpam.govt.nz/GOLD/system/mainframe.asp) -> Online
* [GERM](https://data.gns.cri.nz/germ/submitQuery.html) -> Geological Resource Map of New Zealand
* [Geology](https://data.gns.cri.nz/geology/) -> Web Map
  * https://maps.gns.cri.nz/gns/wfs 

## South America
### Argentina
* [SIGAM](https://sigam.segemar.gov.ar/wordpress) -> Argentina Geological Survey
 * [SIGAM](https://sigam.segemar.gov.ar/wordpress/geoservicios/)
### Bolivia
* [SERGEOMIN IDE](http://ide.sergeomin.gob.bo/) -> Bolivia Geological Mining Service geospatial data
### Brazil
* [CPRM](https://www.cprm.gov.br/en/Geology-53) -> Brazil Geological Survey
 * [Downloads](https://geosgb.cprm.gov.br/geosgb/downloads_en.html) -> Brazil Geological Survey Downloads
* [Rigeo](https://rigeo.cprm.gov.br/) -> Institutional Repository of Geosciences
### Chile
* [Portalgeomin](https://portalgeomin.sernageomin.cl/)
### Colombia
* [Geportal](https://srvags.sgc.gov.co/JSViewer/Recursos_Minerales_Ingles/)
### Ecuador
* [IIGE Geoenergia](https://www.geoenergia.gob.ec/) -> Ecudaor energy institute geological, mineral and energy resources
### Mexico
* [GeoInfo](https://www.sgm.gob.mx/GeoInfoMexGobMx/)
### Paraguay
* [Geology of Paraguay](https://www.geologiadelparaguay.com.py/Mapas.htm)
### Peru
* [Ingemmet GeoPROMINE](https://ingemmet-peru.maps.arcgis.com/apps/webappviewer/index.html?id=95abc980a2ad441191fde60d66266d2b) -> Geological Survey of Peru
 * [GeoMAPE](https://ingemmet-peru.maps.arcgis.com/apps/webappviewer/index.html?id=6581aa545eca4547acdc1fc7136f1fcd)
### Uruguay
* [Dimage](http://visualizadorgeominero.dinamige.gub.uy/DINAMIGE_mvc2/)

## Europe
* [EGDI](https://www.europe-geology.eu/) -> European Geological Data Infrastructure Pan-European geological data portal with 800+ map layers including mineral occurrences and critical raw materials; OGC WFS/WMS services at https://www.europe-geology.eu/data-tools/
  * [WFS](https://data.geus.dk/egdi/wfs/help/?layers=egdi_mineraloccurr_base_metals)
  * [Promine](https://servicesvectoriels.atlas.gouv.qc.ca/IDS_SGM_WMS/service.svc/get) -> Quebec-Atlas-hosted WMS for ProMine European mineral occurrence data
* [Insp