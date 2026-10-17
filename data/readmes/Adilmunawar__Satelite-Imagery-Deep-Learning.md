<div align="center">
  <img src="images/logo.png" width="400" alt="Satellite Imagery Deep Learning Logo">
  <h1>Satellite Imagery Deep Learning</h1>
  <p><strong>A comprehensive repository of deep learning architectures, models, and algorithms suited for Earth observation, classification, segmentation, and object detection.</strong></p>
  <br>
</div>

## About

Deep learning has revolutionized the analysis and interpretation of satellite and aerial imagery, addressing unique challenges such as vast image sizes and a wide array of object classes. This repository provides an exhaustive overview of deep learning techniques specifically tailored for satellite and aerial image processing. It covers a range of architectures, models, and algorithms suited for key tasks like classification, segmentation, and object detection.

**How to use this repository:** use `Command + F` (Mac) or `CTRL + F` (Windows) to search this page for e.g. 'SAM'

## Contributing & Code of Conduct

We welcome contributions from the community! If you have a project, tool, or resource that belongs here, please read our [Contribution Guidelines](CONTRIBUTING.md) to get started. 

To ensure our community remains approachable and respectable, all contributors are expected to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## Content Index

- **[Core Vision & Semantic Tasks](#core-vision--semantic-tasks)**

  - **[Classification](#classification)**

  - **[Segmentation](#segmentation)**

  - **[Segmentation Land Use & Land Cover](#segmentation---land-use--land-cover)**

  - **[Segmentation Vegetation, Deforestation, Crops & Field Boundaries](#segmentation---vegetation-deforestation-crops--field-boundaries)**

  - **[Segmentation Water, Coastlines, Rivers & Floods](#segmentation---water-coastlines-rivers--floods)**

  - **[Segmentation Fire, Smoke & Burn Areas](#segmentation---fire-smoke--burn-areas)**

  - **[Segmentation Landslides](#segmentation---landslides)**

  - **[Segmentation Glaciers](#segmentation---glaciers)**

  - **[Segmentation Methane](#segmentation---methane)**

  - **[Segmentation Other Environmental](#segmentation---other-environmental)**

  - **[Segmentation Roads & Sidewalks](#segmentation---roads--sidewalks)**

  - **[Segmentation Buildings & Rooftops](#segmentation---buildings--rooftops)**

  - **[Segmentation Solar Panels](#segmentation---solar-panels)**

  - **[Segmentation Ships & Vessels](#segmentation---ships--vessels)**

  - **[Segmentation Other Manmade](#segmentation---other-manmade)**

  - **[Panoptic Segmentation](#panoptic-segmentation)**

  - **[Segmentation Miscellaneous](#segmentation---miscellaneous)**

  - **[Instance Segmentation](#instance-segmentation)**

  - **[Object Detection](#object-detection)**

  - **[Object Tracking In Videos](#object-tracking-in-videos)**

  - **[Object Detection With Rotated Bounding Boxes](#object-detection-with-rotated-bounding-boxes)**

  - **[Object Detection Enhanced By Super Resolution](#object-detection-enhanced-by-super-resolution)**

  - **[Salient Object Detection](#salient-object-detection)**

  - **[Object Detection Buildings, Rooftops & Solar Panels](#object-detection---buildings-rooftops--solar-panels)**

  - **[Object Detection Ships, Boats, Vessels & Wake](#object-detection---ships-boats-vessels--wake)**

  - **[Object Detection Cars, Vehicles & Trains](#object-detection---cars-vehicles--trains)**

  - **[Object Detection Planes & Aircraft](#object-detection---planes--aircraft)**

  - **[Object Detection Infrastructure & Utilities](#object-detection---infrastructure--utilities)**

  - **[Object Detection Oil Storage Tank Detection](#object-detection---oil-storage-tank-detection)**

  - **[Object Detection Animals](#object-detection---animals)**

  - **[Object Detection Miscellaneous](#object-detection---miscellaneous)**

  - **[Object Counting](#object-counting)**

  - **[Regression](#regression)**

  - **[Image Retrieval](#image-retrieval)**

  - **[Image Captioning](#image-captioning)**

  - **[Visual Question Answering](#visual-question-answering)**

- **[Advanced Architectures & Methodologies](#advanced-architectures--methodologies)**

  - **[Super Resolution](#super-resolution)**

  - **[Multi Image Super Resolution (misr)](#multi-image-super-resolution-misr)**

  - **[Single Image Super Resolution (sisr)](#single-image-super-resolution-sisr)**

  - **[Super Resolution Miscellaneous](#super-resolution---miscellaneous)**

  - **[Pansharpening](#pansharpening)**

  - **[Image To Image Translation](#image-to-image-translation)**

  - **[Data Fusion](#data-fusion)**

  - **[Generative Networks](#generative-networks)**

  - **[Autoencoders, Dimensionality Reduction, Image Embeddings & Similarity Search](#autoencoders-dimensionality-reduction-image-embeddings--similarity-search)**

  - **[Anomaly Detection](#anomaly-detection)**

  - **[Mixed Data Learning](#mixed-data-learning)**

  - **[Few & Zero Shot Learning](#few--zero-shot-learning)**

  - **[Self Supervised, Unsupervised & Contrastive Learning](#self-supervised-unsupervised--contrastive-learning)**

  - **[Weakly & Semi Supervised Learning](#weakly--semi-supervised-learning)**

  - **[Active Learning](#active-learning)**

  - **[Federated Learning](#federated-learning)**

  - **[Adversarial Ml](#adversarial-ml)**

  - **[Large Vision & Language Models (llms & Lvms)](#large-vision--language-models-llms--lvms)**

  - **[Foundational Models](#foundational-models)**

- **[Earth Observation & Application Domains](#earth-observation--application-domains)**

  - **[Cloud Detection & Removal](#cloud-detection--removal)**

  - **[Change Detection](#change-detection)**

  - **[Time Series](#time-series)**

  - **[Crop Classification](#crop-classification)**

  - **[Crop Yield & Vegetation Forecasting](#crop-yield--vegetation-forecasting)**

  - **[Wealth And Economic Activity](#wealth-and-economic-activity)**

  - **[Disaster Response](#disaster-response)**

  - **[Image Registration](#image-registration)**

  - **[Terrain Mapping, Disparity Estimation, Lidar, Dems & Nerf](#terrain-mapping-disparity-estimation-lidar-dems--nerf)**

  - **[Thermal Infrared](#thermal-infrared)**

  - **[Sar](#sar)**

  - **[Ndvi Vegetation Index](#ndvi---vegetation-index)**

  - **[General Image Quality](#general-image-quality)**

  - **[Synthetic Data](#synthetic-data)**

  - **[Explainable Ai (xai)](#explainable-ai-xai)**


---

## Core Vision & Semantic Tasks

> At the heart of satellite imagery analysis lie core computer vision tasks adapted for Earth Observation (EO). These include pixel-wise semantic segmentation, object detection for small and dense objects (like vehicles and buildings), and image-level classification. Challenges such as vast spatial scales, varying resolutions, and multi-spectral bands require specialized architectures (e.g., U-Nets for segmentation, YOLO/Faster-RCNN variants for detection). Recent advancements have shifted towards handling rotational bounding boxes and tackling class imbalance in land-cover mapping.


### Classification

<p align="center">
  <img src="images/merced.png" width="600">
  <br>
  <b>The UC merced dataset is a well known classification dataset.</b>
</p>

Classification is a fundamental task in remote sensing data analysis, where the goal is to assign a semantic label to each image, such as 'urban', 'forest', 'agricultural land', etc. The process of assigning labels to an image is known as image-level classification. However, in some cases, a single image might contain multiple different land cover types, such as a forest with a river running through it, or a city with both residential and commercial areas. In these cases, image-level classification becomes more complex and involves assigning multiple labels to a single image. This can be accomplished using a combination of feature extraction and machine learning algorithms to accurately identify the different land cover types. It is important to note that image-level classification should not be confused with pixel-level classification, also known as semantic segmentation. While image-level classification assigns a single label to an entire image, semantic segmentation assigns a label to each individual pixel in an image, resulting in a highly detailed and accurate representation of the land cover types in an image. Read [A brief introduction to satellite image classification with neural networks](https://medium.com/@robmarkcole/a-brief-introduction-to-satellite-image-classification-with-neural-networks-3ce28be15683)

- **[Eurosat Satellite Cnn And Resnet](https://github.com/Rumeysakeskin/EuroSat-Satellite-CNN-and-ResNet)** — *Classifying custom image datasets by creating Convolutional Neural Networks and Residual Networks from scratch with PyTorch.*

- **[Land Cover Classification Using Sentinel 2 Dataset](https://github.com/raoofnaushad/Land-Cover-Classification-using-Sentinel-2-Dataset)** — *[well written Medium article](https://raoofnaushad7.medium.com/applying-deep-learning-on-satellite-imagery-classification-5f2588b932c1) accompanying this repo but using the EuroSAT dataset.*

- **[Slums Mapping From Pretrained Cnn Network](https://github.com/deepankverma/slums_detection)** — *On VHR (Pleiades: 0.5m) and MR (Sentinel: 10m) imagery.*

- **[Comparing Urban Environments Using Satellite Imagery And Convolutional Neural Networks](https://github.com/adrianalbert/urban-environments)** — *Includes interesting study of the image embedding features extracted for each image on the Urban Atlas dataset.*

- **[Rsi Cb](https://github.com/lehaifeng/RSI-CB)** — *A Large Scale Remote Sensing Image Classification Benchmark via Crowdsource Data. See also [Remote-sensing-image-classification](https://github.com/aashishrai3799/Remote-sensing-image-classification).*

- **[Waternet](https://github.com/treigerm/WaterNet)** — *A CNN that identifies water in satellite images.*

- **[Road Network Classification](https://github.com/ualsg/Road-Network-Classification)** — *Road network classification model using ResNet-34, road classes organic, gridiron, radial and no pattern.*

- **[Sstn](https://github.com/zilongzhong/SSTN)** — *Spectral-Spatial Transformer Network for Hyperspectral Image Classification: A FAS Framework.*

- **[Satellitepollutioncnn](https://github.com/arnavbansal1/SatellitePollutionCNN)** — *A novel algorithm to predict air pollution levels with state-of-the-art accuracy using deep learning and GoogleMaps satellite images.*

- **[Propertyclassification](https://github.com/Sardhendu/PropertyClassification)** — *Classifying the type of property given Real Estate, satellite and Street view Images.*

- **[Remote Sense Quickstart](https://github.com/CarryHJR/remote-sense-quickstart)** — *Classification on a number of datasets, including with attention visualization.*

- **[Igarss2020 Bwms](https://github.com/jiankang1991/IGARSS2020_BWMS)** — *Band-Wise Multi-Scale CNN Architecture for Remote Sensing Image Scene Classification with a novel CNN architecture for the feature embedding of high-dimensional RS images.*

- **[Image.classification.on.eurosat](https://github.com/canturan10/image.classification.on.EuroSAT)** — *Solution in pure pytorch.*

- **[Hurricane Damage](https://github.com/allankapoor/hurricane_damage)** — *Post-hurricane structure damage assessment based on aerial imagery.*

- **[Isprs S2fl](https://github.com/danfenghong/ISPRS_S2FL)** — *Multimodal Remote Sensing Benchmark Datasets for Land Cover Classification with A Shared and Specific Feature Learning Model.*

- **[Ensemble Lclu](https://github.com/burakekim/ensemble_LCLU)** — *Deep neural network ensembles for remote sensing land cover and land use classification.*

- **[Urban Analysis Using Satellite Imagery](https://github.com/mominali12/Urban-Analysis-Using-Satellite-Imagery)** — *Classify urban area as planned or unplanned using a combination of segmentation and classification.*

- **[Mining Discovery With Deep Learning](https://github.com/remis/mining-discovery-with-deep-learning)** — *Mining and Tailings Dam Detection in Satellite Imagery Using Deep Learning.*

- **[Sentinel2 Deep Learning](https://github.com/d-smit/sentinel2-deep-learning)** — *Novel Training Methodologies for Land Classification of Sentinel-2 Imagery.*

- **[Pay More Attention](https://github.com/williamzhao95/Pay-More-Attention)** — *Remote Sensing Image Scene Classification Based on an Enhanced Attention Module.*

- **[Remote Sensing Image Classification Via Improved Cross Entropy Loss And Transfer Learning Strategy Based On Deep Convolutional Neural Networks](https://github.com/AliBahri94/Remote-Sensing-Image-Classification-via-Improved-Cross-Entropy-Loss-and-Transfer-Learning-Strategy)**

- **[Skal](https://github.com/hw2hwei/SKAL)** — *Looking Closer at the Scene: Multiscale Representation Learning for Remote Sensing Image Scene Classification.*

- **[Saff](https://github.com/zh-hike/SAFF)** — *Self-Attention-Based Deep Feature Fusion for Remote Sensing Scene Classification.*

- **[Glnet](https://github.com/wuchangsheng951/GLNET)** — *Convolutional Neural Networks Based Remote Sensing Scene Classification under Clear and Cloudy Environments.*

- **[Remote Sensing Image Classification](https://github.com/hiteshK03/Remote-sensing-image-classification)** — *Transfer learning using pytorch to classify remote sensing data into three classes: aircrafts, ships, none.*

- **[Remote Sensing Pretrained Models](https://github.com/lsh1994/remote_sensing_pretrained_models)** — *As an alternative to fine tuning on models pretrained on ImageNet, here some CNN are pretrained on the RSD46-WHU & AID datasets.*

- **[Obic Gcn](https://github.com/CVEO/OBIC-GCN)** — *Object-based Classification Framework of Remote Sensing Images with Graph Convolutional Networks.*

- **[Aitlas Arena](https://github.com/biasvariancelabs/aitlas-arena)** — *An open-source benchmark framework for evaluating state-of-the-art deep learning approaches for image classification in Earth Observation (EO).*

- **[Droughtwatch](https://github.com/wandb/droughtwatch)** — *Satellite-based Prediction of Forage Conditions for Livestock in Northern Kenya.*

- **[Jstars 2020 Dpn Hra](https://github.com/B-Xi/JSTARS_2020_DPN-HRA)** — *Deep Prototypical Networks With Hybrid Residual Attention for Hyperspectral Image Classification.*

- **[Signa](https://github.com/kyle-one/SIGNA)** — *Semantic Interleaving Global Channel Attention for Multilabel Remote Sensing Image Classification.*

- **[Pbdl](https://github.com/Usman1021/PBDL)** — *Patch-Based Discriminative Learning for Remote Sensing Scene Classification.*

- **[Emergencynet](https://github.com/ckyrkou/EmergencyNet)** — *Identify fire and other emergencies from a drone.*

- **[Satellite Deforestation](https://github.com/drewhibbard/satellite-deforestation)** — *Using Satellite Imagery to Identify the Leading Indicators of Deforestation, applied to the Kaggle Challenge Understanding the Amazon from Space.*

- **[Rsmlc](https://github.com/marjanstoimchev/RSMLC)** — *Deep Network Architectures as Feature Extractors for Multi-Label Classification of Remote Sensing Images.*

- **[Firerisk](https://github.com/CharmonyShen/FireRisk)** — *A Remote Sensing Dataset for Fire Risk Assessment with Benchmarks Using Supervised and Self-supervised Learning.*

- **[Flood Susceptibility Mapping](https://github.com/omarseleem92/flood_susceptibility_mapping)** — *Towards urban flood susceptibility mapping using data-driven models in Berlin, Germany.*

- **[Building Detection And Roof Type Recognition](https://github.com/loosgagnet/Building-detection-and-roof-type-recognition)** — *A CNN-Based Approach for Automatic Building Detection and Recognition of Roof Types Using a Single Aerial Image.*

- **[Snn4space](https://github.com/AndrzejKucik/SNN4Space)** — *Project which investigates the feasibility of deploying spiking neural networks (SNN) in land cover and land use classification tasks.*

- **[Vessel Classification](https://github.com/GlobalFishingWatch/vessel-classification)** — *Classify vessels and identify fishing behavior based on AIS data.*

- **[Rsmamba](https://github.com/KyanChen/RSMamba)** — *Remote Sensing Image Classification with State Space Model.*

- **[Birdsat](https://github.com/mvrl/BirdSAT)** — *Cross-View Contrastive Masked Autoencoders for Bird Species Classification and Mapping.*

- **[Egnna Wnd](https://github.com/stevinc/EGNNA_WND)** — *Estimating the presence of the West Nile Disease employing Graph Neural network.*

- **[Cyfi](https://github.com/drivendataorg/cyfi)** — *Estimate cyanobacteria density based on Sentinel-2 satellite imagery.*

- **[3dgan Vit](https://github.com/aj1365/3DGAN-ViT)** — *A deep learning framework based on generative adversarial networks and vision transformer for complex wetland classification.*

- **[Automatic Solar Pv Detection](https://github.com/KennSmithDS/automatic_solar_pv_detection)** — *Automatic Solar PV Panel Image Classification with Deep Neural Network Transfer Learning.*

- **[U Netr](https://github.com/JonathanVSV/U-netR)** — *Land Use Land Cover Classification with U-Net: Advantages of Combining Sentinel-1 and Sentinel-2 Imagery [paper](https://doi.org/10.3390/rs13183600).*

- **[Nshaud/deepnetsforeo](https://github.com/nshaud/DeepNetsForEO)** — *Deep networks for Earth Observation with PyTorch implementations of state-of-the-art architectures for remote sensing image classification.*

- **[Sentinel Landslide Cls](https://github.com/IoannisNasios/sentinel-landslide-cls)** — *Classification for Landslide Detection, using Sentinel-1 and Sentinel-2 data.*

#


---


### Segmentation

<p align="center">
  <img src="images/segmentation.png" width="500">
  <br>
  <b>(left) a satellite image and (right) the semantic classes in the image.</b>
</p>

Image segmentation is a crucial step in image analysis and computer vision, with the goal of dividing an image into semantically meaningful segments or regions. The process of image segmentation assigns a class label to each pixel in an image, effectively transforming an image from a 2D grid of pixels into a 2D grid of pixels with assigned class labels. One common application of image segmentation is road or building segmentation, where the goal is to identify and separate roads and buildings from other features within an image. To accomplish this task, single class models are often trained to differentiate between roads and background, or buildings and background. These models are designed to recognize specific features, such as color, texture, and shape, that are characteristic of roads or buildings, and use this information to assign class labels to the pixels in an image. Another common application of image segmentation is land use or crop type classification, where the goal is to identify and map different land cover types within an image. In this case, multi-class models are typically used to recognize and differentiate between multiple classes within an image, such as forests, urban areas, and agricultural land. These models are capable of recognizing complex relationships between different land cover types, allowing for a more comprehensive understanding of the image content. Read [A brief introduction to satellite image segmentation with neural networks](https://medium.com/@robmarkcole/a-brief-introduction-to-satellite-image-segmentation-with-neural-networks-33ea732d5bce). **Note** that many articles which refer to 'hyperspectral land classification' are often actually describing semantic segmentation.


---


### Segmentation - Land use & land cover

- **[Automatic Detection Of Landfill Using Deep Learning](https://github.com/AnupamaRajkumar/LandfillDetection_SemanticSegmentation)**

- **[Cdl Segmentation](https://github.com/asimniazi63/CDL-Segmentation)** — *Deep Learning Based Land Cover and Crop Type Classification: A Comparative Study. Compares UNet, SegNet & DeepLabv3+.*

- **[Loveda](https://github.com/Junjue-Wang/LoveDA)** — *A Remote Sensing Land-Cover Dataset for Domain Adaptive Semantic Segmentation.*

- **[Deepglobe Land Cover Classification Challenge Solution](https://github.com/GeneralLi95/deepglobe_land_cover_classification_with_deeplabv3plus)**

- **[Cnn Enhanced Gcn](https://github.com/qichaoliu/CNN_Enhanced_GCN)** — *CNN-Enhanced Graph Convolutional Network With Pixel- and Superpixel-Level Feature Fusion for Hyperspectral Image Classification.*

- **[Lulcmapping Wv3images Corine Dlmethods](https://github.com/esertel/LULCMapping-WV3images-CORINE-DLMethods)** — *Land Use and Land Cover Mapping Using Deep Learning Based Segmentation Approaches and VHR Worldview-3 Images.*

- **[Mcanet](https://github.com/yisun98/SOLC)** — *A joint semantic segmentation framework of optical and SAR images for land use classification. Uses [WHU-OPT-SAR-dataset](https://github.com/AmberHen/WHU-OPT-SAR-dataset).*

- **[Land Cover](https://github.com/lucashu1/land-cover)** — *Model Generalization in Deep Learning Applications for Land Cover Mapping.*

- **[Generalizablersc](https://github.com/dgominski/generalizablersc)** — *Cross-dataset Learning for Generalizable Land Use Scene Classification.*

- **[Ssltransformerrs](https://github.com/HSG-AIML/SSLTransformerRS)** — *Self-supervised Vision Transformers for Land-cover Segmentation and.*
  Classification

- **[Lulcmapping Wv3images Corine Dlmethods](https://github.com/burakekim/LULCMapping-WV3images-CORINE-DLMethods)** — *Land Use and Land Cover Mapping Using Deep Learning Based Segmentation Approaches and VHR Worldview-3 Images.*

- **[Dcsa Net](https://github.com/Julia90/DCSA-Net)** — *Dynamic Convolution Self-Attention Network for Land-Cover Classification in VHR Remote-Sensing Images.*

- **[Chegcn Cnn Enhanced Heterogeneous Graph](https://github.com/Liuzhizhiooo/CHeGCN-CNN_enhanced_Heterogeneous_Graph)** — *CNN-Enhanced Heterogeneous Graph Convolutional Network: Inferring Land Use from Land Cover with a Case Study of Park Segmentation.*

- **[Tcsvt 2022 Dgssc](https://github.com/B-Xi/TCSVT_2022_DGSSC)** — *DGSSC: A Deep Generative Spectral-Spatial Classifier for Imbalanced Hyperspectral Imagery.*

- **[Deepforest Wetland Paper](https://github.com/aj1365/DeepForest-Wetland-Paper)** — *Deep Forest classifier for wetland mapping using the combination of Sentinel-1 and Sentinel-2 data, GIScience & Remote Sensing.*

- **[Wetland Unet](https://github.com/conservation-innovation-center/Wetland_UNet)** — *UNet models that can delineate wetlands using remote sensing data input including bands from Sentinel-2 LiDAR and geomorphons. By the Conservation Innovation Center of Chesapeake Conservancy and Defenders of Wildlife.*

- **[Dpa](https://github.com/x-ytong/DPA)** — *DPA is an unsupervised domain adaptation (UDA) method applied to different satellite images for large-scale land cover mapping.*

- **[Dynamicworld](https://github.com/google/dynamicworld)** — *Dynamic World, global 10 m land use land cover mapping from Google. [dynamic_world_pytorch](https://github.com/calebrob6/dynamic_world_pytorch) is a pytorch implementation.*

- **[Spada](https://github.com/links-ads/spada)** — *Land Cover Segmentation with Sparse Annotations from Sentinel-2 Imagery.*

- **[M3spada](https://github.com/ecapliez/M3SPADA)** — *Multi-Sensor Temporal Unsupervised Domain Adaptation for Land Cover Mapping with spatial pseudo labelling and adversarial learning.*

- **[Glnet](https://github.com/VITA-Group/GLNet)** — *Collaborative Global-Local Networks for Memory-Efﬁcient Segmentation of Ultra-High Resolution Images.*

- **[Lovenas](https://github.com/Junjue-Wang/LoveNAS)** — *LoveNAS: Towards Multi-Scene Land-Cover Mapping via Hierarchical Searching Adaptive Network.*

- **[Flair 2 Challenge](https://github.com/IGNF/FLAIR-2)** — *Semantic segmentation and domain adaptation challenge proposed by the French National Institute of Geographical and Forest Information (IGN).*

- **[Flair 2 8th Place Solution](https://github.com/association-rosia/flair-2)**

- **[Igarss Spada](https://github.com/links-ads/spada)** — *Dataset and code for the paper Land Cover Segmentation with Sparse Annotations from Sentinel-2 Imagery [IGARSS 2023](https://arxiv.org/abs/2306.16252).*

- **[Cnn Land Cover Eco](https://github.com/DGalexander/cnn-land-cover-eco)** — *Multi-stage semantic segmentation of land cover in the Peak District using high-resolution RGB aerial imagery.*

- **[Lale](https://github.com/caglarmert/LALE)** — *A lightweight hybrid ConvMixer-transformer architecture for efficient land-cover segmentation in remote sensing imagery.*


---


### Segmentation - Vegetation, deforestation, crops & field boundaries

Note that deforestation detection may be treated as a segmentation task or a change detection task

- **[Detectree](https://github.com/martibosch/detectree)** — *Tree detection from aerial imagery in Python, a LightGBM classifier of tree/non-tree pixels from aerial imagery.*

- **[Kenya Crop Mask](https://github.com/nasaharvest/kenya-crop-mask)** — *Annual and in-season crop mapping in Kenya - LSTM classifier to classify pixels as containing crop or not, and a multi-spectral forecaster that provides a 12 month time series given a partial input. Dataset downloaded from GEE and pytorch lightning used for training.*

- **[Tree Species Classification From From Airborne Lidar And Hyperspectral Data Using 3d Convolutional Neural Networks](https://github.com/jaeeolma/tree-detection-evo)**

- **[Find Sports Fields Using Mask R Cnn And Overlay On Open Street Map](https://github.com/jremillard/images-to-osm)**

- **[An Lstm To Generate A Crop Mask For Togo](https://github.com/nasaharvest/togo-crop-mask)**

- **[Deepsatmodels](https://github.com/michaeltrs/DeepSatModels)** — *Context-self contrastive pretraining for crop type semantic segmentation.*

- **[Deeptreeattention](https://github.com/weecology/DeepTreeAttention)** — *Implementation of Hang et al. 2020 "Hyperspectral Image Classification with Attention Aided CNNs" for tree species prediction.*

- **[Crop Classification](https://github.com/bhavesh907/Crop-Classification)** — *Crop classification using multi temporal satellite images.*

- **[Crop Mask](https://github.com/nasaharvest/crop-mask)** — *End-to-end workflow for generating high resolution cropland maps, uses GEE & LSTM model.*

- **[Deepcropmapping](https://github.com/Lab-IDEAS/DeepCropMapping)** — *A multi-temporal deep learning approach with improved spatial generalizability for dynamic corn and soybean mapping, uses LSTM.*

- **[Resunet A](https://github.com/Akhilesh64/ResUnet-a)** — *A deep learning framework for semantic segmentation of remotely sensed data.*

- **[Dsd Paper 2020](https://github.com/JacobJeppesen/DSD_paper_2020)** — *Crop Type Classification based on Machine Learning with Multitemporal Sentinel-1 Data.*

- **[Mr Dnn](https://github.com/yasir2afaq/Multi-resolution-deep-neural-network)** — *Extract rice field from Landsat 8 satellite imagery.*

- **[Deep Learning Forest Monitoring](https://github.com/waldeland/deep_learning_forest_monitoring)** — *Forest mapping and monitoring of the African continent using Sentinel-2 data and deep learning.*

- **[Global Cropland Mapping](https://github.com/Charly-tian/global-cropland-mapping)** — *Global multi-temporal cropland mapping.*

- **[Landuse Dl](https://github.com/yghlc/Landuse_DL)** — *Delineate landforms due to the thawing of ice-rich permafrost.*

- **[Canopy](https://github.com/jonathanventura/canopy)** — *A Convolutional Neural Network Classifier Identifies Tree Species in Mixed-Conifer Forest from Hyperspectral Imagery.*

- **[Forest Change Detection](https://github.com/QuantuMobileSoftware/forest_change_detection)** — *Forest change segmentation with time-dependent models, including Siamese, UNet-LSTM, UNet-diff, UNet3D models.*

- **[Cultionet](https://github.com/jgrss/cultionet)** — *Segmentation of cultivated land, built on PyTorch Geometric and PyTorch Lightning.*

- **[Sentinel Tree Cover](https://github.com/wri/sentinel-tree-cover)** — *A global method to identify trees outside of closed-canopy forests with medium-resolution satellite imagery.*

- **[Crop Type Detection Iclr 2020](https://github.com/RadiantMLHub/crop-type-detection-ICLR-2020)** — *Winning Solutions from Crop Type Detection Competition at CV4A workshop, ICLR 2020.*

- **[S4a Models](https://github.com/Orion-AI-Lab/S4A-Models)** — *Various experiments on the Sen4AgriNet dataset.*

- **[Attention Mechanism Unet](https://github.com/davej23/attention-mechanism-unet)** — *An attention-based U-Net for detecting deforestation within satellite sensor imagery.*

- **[Summercrop Deeplearning](https://github.com/AgriRS/SummerCrop_Deeplearning)** — *A Transferable Learning Classification Model and Carbon Sequestration Estimation of Crops in Farmland Ecosystem.*

- **[Deepforest](https://deepforest.readthedocs.io/en/latest/index.html)** — *Is a python package for training and predicting individual tree crowns from airborne RGB imagery.*

- **[Official Repository For The "identifying Trees On Satellite Images" Challenge From Omdena](https://github.com/cienciaydatos/ai-challenge-trees)**

- **[Ptdm](https://github.com/hr8yhtzb/PTDM)** — *Pomelo Tree Detection Method Based on Attention Mechanism and Cross-Layer Feature Fusion.*

- **[Urban Tree Detection](https://github.com/jonathanventura/urban-tree-detection)** — *Individual Tree Detection in Large-Scale Urban Environments using High-Resolution Multispectral Imagery. With [dataset](https://github.com/jonathanventura/urban-tree-detection-data).*

- **[Biomassters Baseline](https://github.com/fnands/BioMassters_baseline)** — *A basic pytorch lightning baseline using a UNet for getting started with the [BioMassters challenge](https://www.drivendata.org/competitions/99/biomass-estimation/) (biomass estimation).*

- **[Biomassters Winners](https://github.com/drivendataorg/the-biomassters)** — *Top 3 solutions.*

- **[Kbrodt Biomassters Solution](https://github.com/kbrodt/biomassters)** — *1st place solution.*

- **[Biomass Estimation](https://github.com/azavea/biomass-estimation)** — *From Azavea, applied to Sentinel 1 & 2.*

- **[3dunetgsformer](https://github.com/aj1365/3DUNetGSFormer)** — *A deep learning pipeline for complex wetland mapping using generative adversarial networks and Swin transformer.*

- **[Seanet Torch](https://github.com/long123524/SEANet_torch)** — *Using a semantic edge-aware multi-task neural network to delineate agricultural parcels from remote sensing images.*

- **[Arborizer](https://github.com/RaffiBienz/arborizer)** — *Tree crowns segmentation and classification.*

- **[Reuse](https://github.com/priamus-lab/ReUse)** — *REgressive Unet for Carbon Storage and Above-Ground Biomass Estimation.*

- **[Unet Sentinel](https://github.com/eliasqueirogavieira/unet-sentinel)** — *UNet to handle Sentinel-1 SAR images to identify deforestation.*

- **[Maskedsst](https://github.com/HSG-AIML/MaskedSST)** — *Masked Vision Transformers for Hyperspectral Image Classification.*

- **[Unet Defmapping](https://github.com/bragagnololu/UNet-defmapping)** — *Master's thesis using UNet to map deforestation using Sentinel-2 Level 2A images, applied to Amazon and Atlantic Rainforest dataset.*

- **[Cvpr Multiearth Deforestation Segmentation](https://github.com/h2oai/cvpr-multiearth-deforestation-segmentation)** — *Multimodal Unet entry to the CVPR Multiearth 2023 deforestation challenge.*

- **[Transunetplus2](https://github.com/aj1365/TransUNetplus2)** — *TransU-Net++: Rethinking attention gated TransU-Net for deforestation mapping. Uses the Amazon and Atlantic forest dataset.*

- **[A High Resolution Canopy Height Model Of The Earth](https://github.com/langnico/global-canopy-height-model#a-high-resolution-canopy-height-model-of-the-earth)** — *A high-resolution canopy height model of the Earth.*

- **[Radiant Earth Spot The Crop Challenge](https://github.com/radiantearth/spot-the-crop-challenge)** — *Winning models from the Radiant Earth Spot the Crop Challenge, uses a time-series of Sentinel-2 multispectral data to classify crops in the Western Cape of South Africa. [Another solution](https://github.com/DariusTheGeek/Radiant-Earth-Spot-the-Crop-XL-Challenge).*

- **[Transfer Field Delineation](https://github.com/kerner-lab/transfer-field-delineation)** — *Multi-Region Transfer Learning for Segmentation of Crop Field Boundaries in Satellite Images with Limited Labels.*

- **[Crop Field Segmentation Ukan](https://github.com/DarthReca/crop-field-segmentation-ukan)** — *KANs and Sentinel for Effective and Explainable Crop Field Segmentation.*

- **[Mowing Detection](https://github.com/lucas-batier/mowing-detection)** — *Automatic detection of mowing and grazing from Sentinel images.*

- **[Ptavit3d And Ptavit3dca](https://github.com/feevos/tfcl)** — *Tackling fluffy clouds: field boundaries detection using time series of S2 and/or S1 imagery.*

- **[Ai4boundaries](https://github.com/waldnerf/ai4boundaries)** — *A Python package that facilitates download of the AI4boundaries data set.*

- **[Nasa Harvest Field Boundary Competition](https://github.com/radiantearth/Nasa_harvest_field_boundary_competition)** — *Nasa Harvest Rwanda Field Boundary Detection Challenge Tutorial.*

- **[Utb Codes](https://github.com/zhu-xlab/UTB_codes)** — *The Urban Tree Canopy Cover in Brazil [article](https://nkszjx.github.io/projects/UTB.html).*

- **[Nasa Harvest Boundary Detection Challenge](https://github.com/geoaigroup/nasa_harvest_boundary_detection_challenge)** — *The 4th place solution for NASA Harvest Field Boundary Detection Challenge on Zindi.*

- **[Rainforest Segmentation](https://github.com/jcblsn/rainforest-segmentation)** — *Identifying and tracking deforestation in the Amazon Rainforest using state-of-the-art deep learning models and multispectral satellite imagery.*

- **[Delineate Anything: Resolution Agnostic Field Boundary Delineation On Satellite Imagery](https://github.com/Lavreniuk/Delineate-Anything)**

- **[Semantic Segmentation For Lcluc](https://github.com/waterdmd/Semantic_segmentation_for_LCLUC)** — *Semantic Segmentation for Simultaneous Crop and Land Cover Land Use Classification Using Multi-Temporal Landsat Imagery.*

- **[Boundary Sam](https://github.com/awadbahaa/boundary-sam)** — *Parcel boundary delineation using SAM, image embeddings and detail enhancement filters.*

- **[Tofmapper](https://github.com/Moerizzy/TOFMapper)** — *A semantic segmentation tool for mapping and classifying Trees outside Forest in high resolution aerial images.*

- **[Mask Pstin](https://github.com/BruceKai/Mask-PSTIN)** — *Improving crop type mapping by integrating LSTM with temporal random masking and pixel-set spatial information.*

- **[Paddy Identification](https://github.com/kayathri4/paddy_identification)** — *Paddy Field Instance Segmentation using Multi-Temporal SAR Time Series.*

- **[Cropsight](https://github.com/rssiuiuc/CropSight)** — *Towards a large-scale operational framework for object-based crop type ground truth retrieval using street view and PlanetScope satellite imagery.*

- **[Ftw Prue](https://github.com/fieldsoftheworld/ftw-prue)** — *PRUE: A Practical Recipe for Field Boundary Segmentation at Scale.*

- **[Agribound](https://github.com/montimaj/agribound)** — *An AI-powered field boundary delineation toolkit combining satellite foundation models, embeddings, and global training data for accurate agricultural parcel/field boundary mapping.*

- **[S2 Forest Browning Monitoring](https://github.com/SamanthaBiegel/s2-forest-browning-monitoring)** — *Monitoring forest browning using Sentinel-2 imagery.*

- **[Lacunalabels](https://github.com/agroimpacts/lacunalabels)** — *A region-wide, multi-year set of crop field boundary labels for Africa.*

- **[Pseudo Fields](https://github.com/philipperufin/pseudo-fields/)** — *Generating pseudo labels for satellite-based crop field delineatio.*


---


### Segmentation - Water, coastlines, rivers & floods

- **[Sat Water](https://github.com/busayojee/sat-water)** — *Semantic segmentation of water bodies in satellite imagery, producing pixel-wise water masks from remote sensing images using a U-Net–style deep learning pipeline (data preparation, training, inference, and evaluation).*

- **[Houston Flooding](https://github.com/Lichtphyz/Houston_flooding)** — *Labeling each pixel as either flooded or not using data from Hurricane Harvey. Dataset consisted of pre and post flood images, and a ground truth floodwater mask was created using unsupervised clustering (with DBScan) of image pixels with human cluster verification/adjustment.*

- **[Ml4floods](https://github.com/spaceml-org/ml4floods)** — *An ecosystem of data, models and code pipelines to tackle flooding with ML.*

- **[Floodmaps](https://github.com/davdma/floodmaps)** — *An end-to-end pipeline and segmentation models for flood-water detection using Sentinel-1 SAR and Sentinel-2 multispectral imagery.*

- **[1st Place Solution For Stac Overflow: Map Floodwater From Radar Imagery Hosted By Microsoft Ai For Earth](https://github.com/sweetlhare/STAC-Overflow)** — *Combines Unet with Catboostclassifier, taking their maxima, not the average.*

- **[Hydra Floods](https://github.com/Servir-Mekong/hydra-floods)** — *An open source Python application for downloading, processing, and delivering surface water maps derived from remote sensing data.*

- **[Coastsat](https://github.com/kvos/CoastSat)** — *Tool for mapping coastlines which has an extension [CoastSeg](https://github.com/dbuscombe-usgs/CoastSeg) using segmentation models.*

- **[Deepwatermap](https://github.com/isikdogan/deepwatermap)** — *A deep model that segments water on multispectral images.*

- **[Rivamap](https://github.com/isikdogan/rivamap)** — *An automated river analysis and mapping engine.*

- **[Deep Water](https://github.com/maxbeber/deep-water)** — *Track changes in water level.*

- **[Watnet](https://github.com/xinluo2018/WatNet)** — *A deep ConvNet for surface water mapping based on Sentinel-2 image, uses the [Earth Surface Water Dataset](https://zenodo.org/record/5205674#.YoMjyZPMK3I).*

- **[A U Net For Flood Extent Mapping](https://github.com/jorgemspereira/A-U-Net-for-Flood-Extent-Mapping)**

- **[Floatingobjects](https://github.com/ESA-PhiLab/floatingobjects)** — *TOWARDS DETECTING FLOATING OBJECTS ON A GLOBAL SCALE WITHLEARNED SPATIAL FEATURES USING SENTINEL 2. Uses U-Net & pytorch.*

- **[Spacenet8](https://github.com/SpaceNetChallenge/SpaceNet8)** — *Baseline Unet solution to detect flooded roads and buildings.*

- **[Dlsim](https://github.com/nyokoya/dlsim)** — *Breaking the Limits of Remote Sensing by Simulation and Deep Learning for Flood and Debris Flow Mapping.*

- **[Water Hrnet](https://github.com/faye0078/Water-Extraction)** — *HRNet trained on Sentinel 2.*

- **[Semantic Segmentation Model To Identify Newly Developed Or Flooded Land](https://github.com/Azure/pixel_level_land_classification)** — *Using NAIP imagery provided by the Chesapeake Conservancy, training on MS Azure.*

- **[Bandnet](https://github.com/IamShubhamGupto/BandNet)** — *Analysis and application of multispectral data for water segmentation using machine learning. Uses Sentinel-2 data.*

- **[Mmflood](https://github.com/edornd/mmflood)** — *MMFlood: A Multimodal Dataset for Flood Delineation From Satellite Imagery (Sentinel 1 SAR).*

- **[Urban Flooding](https://github.com/omarseleem92/Urban_flooding)** — *Towards transferable data-driven models to predict urban pluvial flood water depth in Berlin, Germany.*

- **[Mecnet](https://github.com/zhilyzhang/MECNet)** — *Rich CNN features for water-body segmentation from very high resolution aerial and satellite imagery.*

- **[Swrnet](https://github.com/trongan93/swrnet)** — *A Deep Learning Approach for Small Surface Water Area Recognition Onboard Satellite.*

- **[Elwha Segmentation](https://github.com/StefanTodoran/elwha-segmentation)** — *Fine-tuning Meta's Segment Anything (SAM) for bird's eye view river pixel segmentation.*

- **[Riversnap](https://github.com/ArminMoghimi/RiverSnap)** — *Code for paper: A Comparative Performance Analysis of Popular Deep Learning Models and Segment Anything Model (SAM) for River Water Segmentation in Close-Range Remote Sensing Imagery.*

- **[Sar Water Segmentation](https://github.com/myeungun/SAR-water-segmentation)** — *Deep Learning based Water Segmentation Using KOMPSAT-5 SAR Images.*

- **[Terramind Flood](https://github.com/R1-AK/terramind-flood)** — *DEM-Enhanced Flood Detection with Physics-Aware Learning, applied to Sen1Flood11.*

- **[Prithvi Cafe](https://github.com/Sk-2103/Prithvi-CAFE)** — *Transformer-based global reasoning (Prithvi-EO-2.0) with CNN-based local spatial sensitivity, enabling high-resolution, reliable flood inundation mapping across multi-channel/sensor inputs, applied to Sen1Flood11.*

- **[Smagnet](https://github.com/ASUcicilab/SMAGNet)** — *A Spatially Masked Adaptive Gated Network for Multimodal Post-Flood Water Extent Mapping using SAR and Incomplete Multispectral Data. Uses c2smsfloods dataset.*

- **[Ibm Bluesky Challenge Zeroflood](https://github.com/oroikono/IBM-BlueSky-Challenge-ZeroFlood)**

- **[Omniwatermask Training](https://github.com/DPIRD-DMA/OmniWaterMask-training)** — *Training code for the deep learning model used in [OmniWaterMask](https://github.com/DPIRD-DMA/OmniWaterMask) - a Python library for detecting water bodies in satellite and aerial imagery.*

- **[Utae Water Segmentation](https://github.com/khlaifiabilel/utae-water-segmentation)** — *UTAE-PAPS model for water/land segmentation using Sentinel-1 and Sentinel-2 data with IBM Granite flood detection dataset.*


---


### Segmentation - Fire, smoke & burn areas

- **[Satellitevu Aws Disaster Response Hackathon](https://github.com/SatelliteVu/SatelliteVu-AWS-Disaster-Response-Hackathon)** — *Fire spread prediction using classical ML & deep learning.*

- **[A Practical Method For High Resolution Burned Area Monitoring Using Sentinel 2 And Viirs](https://github.com/mnpinto/FireHR)**

- **[Industrialsmokeplumedetection](https://github.com/HSG-AIML/IndustrialSmokePlumeDetection)** — *Using Sentinel-2 & a modified ResNet-50.*

- **[Burned Area Detection](https://github.com/dymaxionlabs/burned-area-detection)** — *Uses Sentinel-2.*

- **[Rescue](https://github.com/dbdmg/rescue)** — *Attention to fires: multi-channel deep-learning models for wildfire severity prediction.*

- **[Smoke Segmentation](https://github.com/jeffwen/smoke_segmentation)** — *Segmenting smoke plumes and predicting density from GOES imagery.*

- **[Wildfire Detection](https://github.com/amanbasu/wildfire-detection)** — *Using Vision Transformers for enhanced wildfire detection in satellite images.*

- **[Burned Area Detection](https://github.com/prhuppertz/Burned_Area_Detection)** — *Detecting Burned Areas with Sentinel-2 data.*

- **[Burned Area Baseline](https://github.com/lccol/burned-area-baseline)** — *Baseline unet model accompanying the Satellite Burned Area Dataset (Sentinel 1 & 2).*

- **[Burned Area Seg](https://github.com/links-ads/burned-area-seg)** — *Burned area segmentation from Sentinel-2 using multi-task learning.*

- **[Chabud2023](https://github.com/developmentseed/chabud2023)** — *Change detection for Burned area Delineation (ChaBuD) ECML/PKDD 2023 challenge.*

- **[Post Wildfire Burnt Up Detection Using Siamese Unet](https://github.com/kavyagupta/chabud)** — *On Chadbud dataset.*

- **[Vit Burned Detection](https://github.com/DarthReca/vit-burned-detection)** — *Vision transformers in burned area delineation.*

- **[Ai4good25 Wildfire](https://github.com/VSainteuf/ai4good25-wildfire)** — *AI4GOOD Class Fall 2025 : Wildfire spread prediction project.*

- **[Wildfire Lora Gfm](https://github.com/alishibli97/wildfire-lora-gfm)** — *Adapting large Earth-Observation foundation models.*
(Prithvi-v2, TerraMind, DINOv3) using LoRA, to detect wildfire burned areas from bi-temporal (pre-fire / post-fire) Sentinel-2 imagery.


---


### Segmentation - Landslides

- **[Landslide Sar Unet](https://github.com/iprapas/landslide-sar-unet)** — *Deep Learning for Rapid Landslide Detection using Synthetic Aperture Radar (SAR) Datacubes.*

- **[Landslide Mapping With Cnn](https://github.com/nprksh/landslide-mapping-with-cnn)** — *A new strategy to map landslides with a generalized convolutional neural network.*

- **[Landslide Mapping On Sar Data By Attention U Net](https://github.com/lorenzonava96/Landslide-mapping-on-SAR-data-by-Attention-U-Net)** — *Rapid Mapping of landslide on SAR data by Attention U-net.*

- **[Sar Landslide Detection Pretraining](https://github.com/VMBoehm/SAR-landslide-detection-pretraining)** — *SAR-based landslide classification pretraining leads to better segmentation.*

- **[Landslide Mapping From Sentinel 2 Imagery Through Change Detection](https://github.com/links-ads/igarss-landslide-delineation)**

- **[Landslide4sense Solution](https://github.com/iamtekson/landslide4sense-solution)** — *Solution of Tek Kshetri.*

- **[Digate Unet Landslide Segmentation](https://github.com/mishaown/DiGATe-UNet-LandSlide-Segmentation)** — *Lightweight Dual-Stream Framework for Landslide Segmentation.*

- **[Erosion Detection](https://github.com/Andrii-Radyhin/Erosion-detection)** — *Using Sentinel-2 to detect erosion.*


---


### Segmentation - Glaciers

- **[Hed Unet](https://github.com/khdlr/HED-UNet)** — *A model for simultaneous semantic segmentation and edge detection, examples provided are glacier fronts and building footprints using the Inria Aerial Image Labeling dataset.*

- **[Glacier Mapping](https://github.com/krisrs1128/glacier_mapping)** — *Mapping glaciers in the Hindu Kush Himalaya, Landsat 7 images, Shapefile labels of the glaciers, Unet with dropout.*

- **[Glaciersemanticsegmentation](https://github.com/n9Mtq4/GlacierSemanticSegmentation)**

- **[Antarctic Fracture Detection](https://github.com/chingyaolai/Antarctic-fracture-detection)** — *Uses UNet with the MODIS Mosaic of Antarctica to detect surface fractures.*

- **[Sentinel Lakeice](https://github.com/prs-eth/sentinel_lakeice)** — *Lake Ice Detection from Sentinel-1 SAR with Deep Learning.*

- **[Mcd Net](https://github.com/Lyra-alpha/MCD-Net)** — *A lightweight deep learning framework for optical-only moraine segmentation.*

- **[Landslides Segmentation](https://github.com/Eb3ls/landslides_segmentation)** — *Super-resolution and segmentation of multispectral Sentinel-2 satellite imagery, applied to landslide monitoring in Italian municipalities.*

- **[Glaciercastai](https://github.com/Arun-K-Ram/GlacierCastAI)** — *Forecasts glacier boundary retreat from Landsat time series, ERA5 climate data and Copernicus DEM terrain features using a multimodal ConvLSTM model.*


---


### Segmentation - methane

- **[Methane Detection From Hyperspectral Imagery](https://github.com/satish1901/Methane-detection-from-hyperspectral-imagery)** — *Deep Remote Sensing Methods for Methane Detection in Overhead Hyperspectral Imagery.*

- **[Methane Emission Project](https://github.com/stlbnmaria/methane-emission-project)** — *Classification CNNs was combined in an ensemble approach with traditional methods on tabular data.*

- **[Ch4net](https://github.com/annavaughan/CH4Net)** — *A fast, simple model for detection of methane plumes using sentinel-2.*

- **[Starcop: Semantic Segmentation Of Methane Plumes With Hyperspectral Machine Learning Models](https://github.com/spaceml-org/STARCOP)**

- **[Project Eucalyptus](https://github.com/Orbio-Earth/Project-Eucalyptus)** — *Pipelines for satellite-based methane detection. Includes trained segmentation models, a synthetic plume generator, and benchmarking tools for Sentinel-2, Landsat 8/9, and EMIT.*

- **[Plume Hunter: Towards Methane Detection On Board Satellites](https://github.com/spaceml-org/plume-hunter)**


---


### Segmentation - Other environmental

- **[Detection Of Open Landfills](https://github.com/dymaxionlabs/basurales)** — *Uses Sentinel-2 to detect large changes in the Normalized Burn Ratio (NBR).*

- **[Sea Ice Remote Sensing](https://github.com/sum1lim/sea_ice_remote_sensing)** — *Sea Ice Concentration classification.*

- **[Eddynet](https://github.com/redouanelg/EddyNet)** — *A Deep Neural Network For Pixel-Wise Classification of Oceanic Eddies.*

- **[Schisto Vegetation](https://github.com/deleo-lab/schisto-vegetation)** — *Deep Learning Segmentation of Satellite Imagery Identifies Aquatic Vegetation Associated with Snail Intermediate Hosts of Schistosomiasis in Senegal, Africa.*

- **[Earthformer](https://github.com/amazon-science/earth-forecasting-transformer)** — *Exploring space-time transformers for earth system forecasting.*

- **[Weather4cast 2022](https://github.com/iarai/weather4cast-2022)** — *Unet-3D baseline model for Weather4cast Rain Movie Prediction competition.*

- **[Weatherfusionnet](https://github.com/Datalab-FIT-CTU/weather4cast-2022)** — *Predicting Precipitation from Satellite Data. weather4cast-2022 1st place solution.*

- **[Marinedebrisdetector](https://github.com/MarcCoru/marinedebrisdetector)** — *Large-scale Detection of Marine Debris in Coastal Areas with Sentinel-2.*

- **[Kaggle Identify Contrails 4th](https://github.com/selimsef/kaggle-identify-contrails-4th)** — *4th place Solution, Google Research - Identify Contrails to Reduce Global Warming.*

- **[Minesegsat](https://github.com/macdonaldezra/MineSegSAT)** — *An automated system to evaluate mining disturbed area extents from Sentinel-2 imagery.*

- **[Asos](https://gitlab.jsc.fz-juelich.de/kiste/asos)** — *Recognizing protected and anthropogenic patterns in landscapes using interpretable machine learning and satellite imagery.*

- **[Sinksam](https://github.com/osherr1996/SinkSAM)** — *Knowledge-Driven Self-Supervised Sinkhole Segmentation Using Topographic Priors and Segment Anything Model.*

- **[Sense](https://github.com/kailaisun/GenAI4Urban-Energy/)** — *Satellite-based ENergy Synthesis for Sustainable Environment.*


---


### Segmentation - Roads & sidewalks

Extracting roads is challenging due to the occlusions caused by other objects and the complex traffic environment

- **[Chesapeakersc](https://github.com/isaaccorley/ChesapeakeRSC)** — *Segmentation to extract roads from the background but are additionally evaluated by how they perform on the "Tree Canopy Over Road" class.*

- **[Ml Epfl Project 2](https://github.com/LucasBrazCappelo/ML_EPFL_Project_2)** — *U-Net in Pytorch to perform semantic segmentation of roads on satellite images.*

- **[Winning Solutions From Spacenet Road Detection And Routing Challenge](https://github.com/SpaceNetChallenge/RoadDetector)**


- **[Awesome Deep Map](https://github.com/antran89/awesome-deep-map)** — *A curated list of resources dedicated to deep learning / computer vision algorithms for mapping. The mapping problems include road network inference, building footprint extraction, etc.*

- **[Roadtracer: Automatic Extraction Of Road Networks From Aerial Images](https://github.com/mitroadmaps/roadtracer)** — *Uses an iterative search process guided by a CNN-based decision function to derive the road network graph directly from the output of the CNN.*

- **[Road Detection Mtl](https://github.com/ntelo007/road_detection_mtl)** — *Road Detection using a multi-task Learning technique to improve the performance of the road detection task by incorporating prior knowledge constraints, uses the SpaceNet Roads Dataset.*

- **[Road Connectivity](https://github.com/anilbatra2185/road_connectivity)** — *Improved Road Connectivity by Joint Learning of Orientation and Segmentation (CVPR2019).*

- **[Spin Roadmapper](https://github.com/wgcban/SPIN_RoadMapper)** — *Extracting Roads from Aerial Images via Spatial and Interaction Space Graph Reasoning for Autonomous Driving.*

- **[Road Extraction Remote Sensing](https://github.com/jiankang1991/road_extraction_remote_sensing)** — *Pytorch implementation, CVPR2018 DeepGlobe Road Extraction Challenge submission. See also [DeepGlobe-Road-Extraction-Challenge](https://github.com/zlckanata/DeepGlobe-Road-Extraction-Challenge).*

- **[Roaddetections Dataset By Microsoft](https://github.com/microsoft/RoadDetections)**

- **[Coanet](https://github.com/mj129/CoANet)** — *Connectivity Attention Network for Road Extraction From Satellite Imagery. The CoA module incorporates graphical information to ensure the connectivity of roads are better preserved.*

- **[Satellite Imagery Road Segmentation](https://medium.com/@nithishmailme/satellite-imagery-road-segmentation-ad2964dc3812)** — *Intro article on Medium using the kaggle [Massachusetts Roads Dataset](https://www.kaggle.com/datasets/balraj98/massachusetts-roads-dataset).*

- **[Label Pixels](https://github.com/venkanna37/Label-Pixels)** — *For semantic segmentation of roads and other features.*

- **[Satellite Image Road Extraction](https://github.com/amanhari-projects/Satellite-image-road-extraction)** — *Road Extraction by Deep Residual U-Net.*

- **[Road Building Extraction](https://github.com/jeffwen/road_building_extraction)** — *Pytorch implementation of U-Net architecture for road and building extraction.*

- **[Rcfsnet](https://github.com/CVer-Yang/RCFSNet)** — *Road Extraction From Satellite Imagery by Road Context and Full-Stage Feature.*

- **[Sgcn](https://github.com/tist0bsc/SGCN)** — *Split Depth-Wise Separable Graph-Convolution Network for Road Extraction in Complex Environments From High-Resolution Remote-Sensing Images.*

- **[Aspn](https://github.com/pshams55/ASPN)** — *Road Segmentation for Remote Sensing Images using Adversarial Spatial Pyramid Networks.*

- **[Cresi](https://github.com/avanetten/cresi)** — *Road network extraction from satellite imagery, with speed and travel time estimates.*

- **[D Linknet](https://github.com/NekoApocalypse/road-extraction-d-linknet)** — *LinkNet with Pretrained Encoder and Dilated Convolution for High Resolution Satellite Imagery Road Extraction.*

- **[Sat2graph](https://github.com/songtaohe/Sat2Graph)** — *Road Graph Extraction through Graph-Tensor Encoding.*

- **[Roadtracer M](https://github.com/astro-ck/RoadTracer-M)** — *Road Network Extraction from Satellite Images Using CNN Based Segmentation and Tracing.*

- **[Scroadextractor](https://github.com/weiyao1996/ScRoadExtractor)** — *Scribble-based Weakly Supervised Deep Learning for Road Surface Extraction from Remote Sensing Images.*

- **[Roadda](https://github.com/LANMNG/RoadDA)** — *Stagewise Unsupervised Domain Adaptation with Adversarial Self-Training for Road Segmentation of Remote Sensing Images.*

- **[Deepsegmentor](https://github.com/yhlleo/DeepSegmentor)** — *A Pytorch implementation of DeepCrack and RoadNet projects.*

- **[Cascaded Residual Attention Enhanced Road Extraction From Remote Sensing Images](https://github.com/liaochengcsu/Cascade_Residual_Attention_Enhanced_for_Refinement_Road_Extraction)**

- **[Nl Linknet](https://github.com/SIAnalytics/nia-road-baseline)** — *Toward Lighter but More Accurate Road Extraction with Non-Local Operations.*

- **[Irsr Net](https://github.com/yangzhen1252/IRSR-net)** — *Lightweight Remote Sensing Road Detection Network.*

- **[Hironex](https://github.com/johannesuhl/hironex)** — *A python tool for automatic, fully unsupervised extraction of historical road networks from historical maps.*

- **[Road Detection Model](https://github.com/JonasImazon/Road_detection_model)** — *Mapping Roads in the Brazilian Amazon with Artificial Intelligence and Sentinel-2.*

- **[Dtnet](https://github.com/huzican695/DTnet)** — *Road detection via a dual-task network based on cross-layer graph fusion modules.*

- **[Automatic Road Extraction From Historical Maps Using Deep Learning Techniques](https://github.com/UrbanOccupationsOETR/Automatic-Road-Extraction-from-Historical-Maps-using-Deep-Learning-Techniques)** — *Automatic Road Extraction from Historical Maps using Deep Learning Techniques.*

- **[Istanbul Dataset](https://github.com/TolgaBkm/Istanbul_Dataset)** — *Segmentation on the Istanbul, Inria and Massachusetts datasets.*

- **[D Linknet](https://github.com/ShenweiXie/D-LinkNet)** — *1st place solution in DeepGlobe Road Extraction Challenge.*

- **[Park Detect](https://github.com/ShenweiXie/PaRK-Detect)** — *PaRK-Detect: Towards Efficient Multi-Task Satellite Imagery Road Extraction via Patch-Wise Keypoints Detection.*

- **[Tile2net](https://github.com/VIDA-NYU/tile2net)** — *Mapping the walk: A scalable computer vision approach for generating sidewalk network datasets from aerial imagery.*

- **[Sam Road](https://github.com/htcr/sam_road)** — *Segment Anything Model (SAM) for large-scale, vectorized road network extraction from aerial imagery.*

- **[Lrdnet](https://github.com/dyl96/LRDNet)** — *A Lightweight Road Detection Algorithm Based on Multiscale Convolutional Attention Network and Coupled Decoder Head.*

- **[Fine–grained Extraction Of Road Networks Via Joint Learning Of Connectivity And Segmentation](https://github.com/YXu556/RoadExtraction)** — *Uses SpaceNet 3 dataset.*

- **[Satellite Image Road Segmentation](https://github.com/aavek/Satellite-Image-Road-Segmentation)** — *Graph Reasoned Multi-Scale Road Segmentation in Remote Sensing Imagery.*

- **[Pathfinder](https://github.com/Oraegbuayomide10/PathFinder)** — *A Foundation Model for Road Mapping in Support of United Nations Humanitarian Affairs.*


---


### Segmentation - Buildings & rooftops

- **[Road And Building Semantic Segmentation In Satellite Imagery](https://github.com/Paulymorphous/Road-Segmentation)** — *Uses U-Net on the Massachusetts Roads Dataset & keras.*

- **[Find Unauthorized Constructions Using Aerial Photography](https://medium.com/towards-artificial-intelligence/find-unauthorized-constructions-using-aerial-photography-and-deep-learning-with-code-part-2-b56ca80c8c99)** — *[Dataset creation](https://pub.towardsai.net/find-unauthorized-constructions-using-aerial-photography-and-deep-learning-with-code-part-1-6d3ca7ff6fa0).*

- **[Srbuildseg](https://github.com/xian1234/SRBuildSeg)** — *Making low-resolution satellite images reborn: a deep learning approach for super-resolution building extraction.*


- **[Automated Building Detection](https://github.com/rodekruis/automated-building-detection)** — *Input: very-high-resolution (<= 0.5 m/pixel) RGB satellite images. Output: buildings in vector format (geojson), to be used in digital map products. Built on top of robosat and robosat.pink.*

- **[Jointnet A Common Neural Network For Road And Building Extraction](https://github.com/ThomasWangWeiHong/JointNet-A-Common-Neural-Network-for-Road-and-Building-Extraction)**

- **[Mapping Africa’s Buildings With Satellite Imagery: Google Ai Blog Post](https://ai.googleblog.com/2021/07/mapping-africas-buildings-with.html)** — *. See the [open-buildings](https://sites.research.google/open-buildings/) dataset.*

- **[Nz Convnet](https://github.com/weiji14/nz_convnet)** — *A U-net based ConvNet for New Zealand imagery to classify building outlines.*

- **[Polycnn](https://github.com/Lydorn/polycnn)** — *End-to-End Learning of Polygons for Remote Sensing Image Classification.*

- **[Spacenet Building Detection](https://github.com/motokimura/spacenet_building_detection)** — *Solution by [motokimura](https://github.com/motokimura) using Unet.*

- **[Semantic Segmentation Repo By Fuweifu Vtoo](https://github.com/fuweifu-vtoo/Semantic-segmentation)** — *Uses pytorch and the [Massachusetts Buildings & Roads Datasets](https://www.cs.toronto.edu/~vmnih/data/).*

- **[Extracting Buildings And Roads From Aws Open Data Using Amazon Sagemaker](https://aws.amazon.com/blogs/machine-learning/extracting-buildings-and-roads-from-aws-open-data-using-amazon-sagemaker/)** — *With [repo](https://github.com/aws-samples/aws-open-data-satellite-lidar-tutorial).*

- **[Tf Segnet](https://github.com/mathildor/TF-SegNet)** — *AirNet is a segmentation network based on SegNet, but with some modifications.*

- **[Rgb Footprint Extract](https://github.com/aatifjiwani/rgb-footprint-extract)** — *A Semantic Segmentation Network for Urban-Scale Building Footprint Extraction Using RGB Satellite Imagery, DeepLavV3+ module with a Dilated ResNet C42 backbone.*

- **[Spacenetexploration](https://github.com/yangsiyu007/SpaceNetExploration)** — *A sample project demonstrating how to extract building footprints from satellite images using a semantic segmentation model. Data from the SpaceNet Challenge.*

- **[Rooftop Instance Segmentation](https://github.com/MasterSkepticista/Rooftop-Instance-Segmentation)** — *VGG-16, Instance Segmentation, uses the Airs dataset.*

- **[Solar Farms Mapping](https://github.com/microsoft/solar-farms-mapping)** — *An Artificial Intelligence Dataset for Solar Energy Locations in India.*

- **[Poultry Cafos](https://github.com/microsoft/poultry-cafos)** — *This repo contains code for detecting poultry barns from high-resolution aerial imagery and an accompanying dataset of predicted barns over the United States.*

- **[Ssai Cnn](https://github.com/mitmul/ssai-cnn)** — *This is an implementation of Volodymyr Mnih's dissertation methods on his Massachusetts road & building dataset.*

- **[Remote Sensing Building Extraction To 3d Model Using Paddle And Grasshopper](https://github.com/Youssef-Harby/Remote-sensing-building-extraction-to-3D-model-using-Paddle-and-Grasshopper)**

- **[Segmentation Enhanced Resunet](https://github.com/tranleanh/segmentation-enhanced-resunet)** — *Urban building extraction in Daejeon region using Modified Residual U-Net (Modified ResUnet) and applying post-processing.*

- **[Mask Rcnn For Spacenet Off Nadir Building Detection](https://github.com/ashnair1/Mask-RCNN-for-Off-Nadir-Building-Detection)**

- **[Grsl Bfe Ma](https://github.com/jiankang1991/GRSL_BFE_MA)** — *Deep Learning-based Building Footprint Extraction with Missing Annotations using a novel loss function.*

- **[Fer Cnn](https://github.com/runnergirl13/FER-CNN)** — *Detection, Classification and Boundary Regularization of Buildings in Satellite Imagery Using Faster Edge Region Convolutional Neural Networks.*

- **[Vector Map Generation From Aerial Imagery Using Deep Learning Geospatial Unet](https://github.com/ManishSahu53/Vector-Map-Generation-from-Aerial-Imagery-using-Deep-Learning-GeoSpatial-UNET)** — *Applied to geo-referenced images which are very large size > 10k x 10k pixels.*

- **[Building Footprint Segmentation](https://github.com/fuzailpalnak/building-footprint-segmentation)** — *Pip installable library to train building footprint segmentation on satellite and aerial imagery, applied to Massachusetts Buildings Dataset and Inria Aerial Image Labeling Dataset.*

- **[Fcnn Example](https://github.com/emredog/FCNN-example)** — *Overfit to a given single image to detect houses.*

- **[Sat2lod2](https://github.com/gdaosu/lod2buildingmodel)** — *An open-source, python-based GUI-enabled software that takes the satellite images as inputs and returns LoD2 building models as outputs.*

- **[Satfootprint](https://github.com/PriyanK7n/SatFootprint)** — *Building segmentation on the Spacenet 7 dataset.*

- **[Building Detection](https://github.com/EL-BID/Building-Detection)** — *Raster Vision experiment to train a model to detect buildings from satellite imagery in three cities in Latin America.*

- **[Multi Building Tracker](https://github.com/sebasmos/Multi-building-tracker)** — *Multi-target building tracker for satellite images using deep learning.*

- **[Boundary Enhancement Semantic Segmentation For Building Extraction](https://github.com/hin1115/BEmodule-Satellite-Building-Segmentation)**

- **[Spacenet Building Detection](https://github.com/IdanC1s2/Spacenet-Building-Detection)**

- **[Lgpnet Bcd](https://github.com/TongfeiLiu/LGPNet-BCD)** — *Building Change Detection for VHR Remote Sensing Images via Local-Global Pyramid Network and Cross-Task Transfer Learning Strategy.*

- **[Mtl Homoscedastic Srb](https://github.com/burakekim/MTL_homoscedastic_SRB)** — *A Multi-Task Deep Learning Framework for Building Footprint Segmentation.*

- **[Fdanet](https://github.com/daifeng2016/FDANet)** — *Full-Level Domain Adaptation for Building Extraction in Very-High-Resolution Optical Remote-Sensing Images.*

- **[Cbrnet](https://github.com/HaonanGuo/CBRNet)** — *A Coarse-to-fine Boundary Refinement Network for Building Extraction from Remote Sensing Imagery.*

- **[Aslnet](https://github.com/ggsDing/ASLNet)** — *Adversarial Shape Learning for Building Extraction in VHR Remote Sensing Images.*

- **[Brrnet](https://github.com/wangyi111/Building-Extraction)** — *A Fully Convolutional Neural Network for Automatic Building Extraction From High-Resolution Remote Sensing Images.*

- **[Multi Scale Filtering Building Index](https://github.com/ThomasWangWeiHong/Multi-Scale-Filtering-Building-Index)** — *A Multi - Scale Filtering Building Index for Building Extraction in Very High - Resolution Satellite Imagery.*

- **[Models For Remote Sensing](https://github.com/bohaohuang/mrs)** — *Long list of unets etc applied to building detection.*

- **[Boundary Loss For Remote Sensing](https://github.com/yiskw713/boundary_loss_for_remote_sensing)** — *Boundary Loss for Remote Sensing Imagery Semantic Segmentation.*

- **[Open Cities Ai Challenge](https://www.drivendata.org/competitions/60/building-segmentation-disaster-resilience/)** — *Segmenting Buildings for Disaster Resilience. Winning solutions [on Github](https://github.com/drivendataorg/open-cities-ai-challenge/).*

- **[Mapnet](https://github.com/lehaifeng/MAPNet)** — *Multi Attending Path Neural Network for Building Footprint Extraction from Remote Sensed Imagery.*

- **[Dual Hrnet](https://github.com/SIAnalytics/dual-hrnet)** — *Localizing buildings and classifying their damage level.*

- **[Esfnet](https://github.com/mrluin/ESFNet-Pytorch)** — *Efficient Network for Building Extraction from High-Resolution Aerial Images.*

- **[Cvcmffnet](https://github.com/Jiankun-chen/CVCMFFNet-master)** — *Complex-Valued Convolutional and Multifeature Fusion Network for Building Semantic Segmentation of InSAR Images.*

- **[Steb Unet](https://github.com/BrightGuo048/STEB-UNet)** — *A Swin Transformer-Based Encoding Booster Integrated in U-Shaped Network for Building Extraction.*

- **[Dfc2020 Baseline](https://github.com/lukasliebel/dfc2020_baseline)** — *Baseline solution for the IEEE GRSS Data Fusion Contest 2020. Predict land cover labels from Sentinel-1 and Sentinel-2 imagery.*

- **[Fusing Multiple Segmentation Models Based On Different Datasets Into A Single Edge Deployable Model](https://github.com/markusmeingast/Satellite-Classifier)** — *Roof, car & road segmentation.*

- **[Ground Truth Gan Segmentation](https://github.com/zakariamejdoul/ground-truth-gan-segmentation)** — *Use Pix2Pix to segment the footprint of a building. The dataset used is AIRS.*

- **[Unicef Giga Sudan](https://github.com/Kamal-Eldin/UNICEF-Giga_Sudan)** — *Detecting school lots from satellite imagery in Southern Sudan using a UNET segmentation model.*

- **[Building Footprint Extraction](https://github.com/shubhamgoel27/building_footprint_extraction)** — *The project retrieves satellite imagery from Google and performs building footprint extraction using a U-Net.*

- **[Projectregularization](https://github.com/zorzi-s/projectRegularization)** — *Regularization of building boundaries in satellite images using adversarial and regularized losses.*

- **[Polyworldpretrainednetwork](https://github.com/zorzi-s/PolyWorldPretrainedNetwork)** — *Polygonal Building Extraction with Graph Neural Networks in Satellite Images.*

- **[Dl Image Segmentation](https://github.com/harry-gibson/dl_image_segmentation)** — *Uncertainty-Aware Interpretable Deep Learning for Slum Mapping and Monitoring. Uses SHAP.*

- **[Ubc Dataset](https://github.com/AICyberTeam/UBC-dataset)** — *A dataset for building detection and classification from very high-resolution satellite imagery with the focus on object-level interpretation of individual buildings.*

- **[Unetformer](https://github.com/WangLibo1995/GeoSeg)** — *A UNet-like transformer for efficient semantic segmentation of remote sensing urban scene imagery.*

- **[Bes Net](https://github.com/FlyC235/BESNet)** — *Boundary Enhancing Semantic Context Network for High-Resolution Image Semantic Segmentation. Applied to Vaihingen and Potsdam datasets.*

- **[Cvnet](https://github.com/xzq-njust/CVNet)** — *Contour Vibration Network for Building Extraction.*

- **[Cfenet](https://github.com/djzgroup/CFENet)** — *A Context Feature Enhancement Network for Building Extraction from High-Resolution Remote Sensing Imagery.*

- **[Hisup](https://github.com/SarahwXU/HiSup)** — *Accurate Polygonal Mapping of Buildings in Satellite Imagery.*

- **[Buildingextraction](https://github.com/KyanChen/BuildingExtraction)** — *Building Extraction from Remote Sensing Images with Sparse Token Transformers.*

- **[Crossgeonet](https://github.com/lqycrystal/coseg_building)** — *A Framework for Building Footprint Generation of Label-Scarce Geographical Regions.*

- **[Afm Building](https://github.com/lqycrystal/AFM_building)** — *Building Footprint Generation Through Convolutional Neural Networks With Attraction Field Representation.*

- **[Ramp (replicable Ai For Microplanning)](https://github.com/devglobalpartners/ramp-code)** — *Building detection in low and middle income countries.*

- **[Building Instance Segmentation](https://github.com/yuanqinglie/Building-instance-segmentation-combining-anchor-free-detectors-and-multi-modal-feature-fusion)** — *Multi-Modal Feature Fusion Network with Adaptive Center Point Detector for Building Instance Extraction.*

- **[Cgsanet](https://github.com/MrChen18/CGSANet)** — *A Contour-Guided and Local Structure-Aware Encoder–Decoder Network for Accurate Building Extraction From Very High-Resolution Remote Sensing Imagery.*

- **[Building Footprints Update](https://github.com/wangzehui20/building-footprints-update)** — *Learning Color Distributions from Bitemporal Remote Sensing Images to Update Existing Building Footprints.*

- **[Ramp](https://rampml.global/)** — *Model and buildings dataset to support a wide variety of humanitarian use cases.*

- **[Thesis Semantic Image Segmentation On Satellite Imagery Using Unets](https://github.com/rinkwitz/Thesis_Semantic_Image_Segmentation_on_Satellite_Imagery_using_UNets)** — *This master thesis aims to perform semantic segmentation of buildings on satellite images from the SpaceNet challenge 1 dataset using the U-Net architecture.*

- **[Hd Net](https://github.com/danfenghong/ISPRS_HD-Net)** — *High-resolution decoupled network for building footprint extraction via deeply supervised body and boundary decomposition.*

- **[Roofsense](https://github.com/DimitrisMantas/RoofSense/tree/master)** — *A novel deep learning solution for the automatic roofing material classification of the Dutch building stock using aerial imagery and laser scanning data fusion.*

- **[Ibs Aqsnet](https://github.com/zhilyzhang/IBS-AQSNet)** — *Enhanced Automated Quality Assessment Network for Interactive Building Segmentation in High-Resolution Remote Sensing Imagery.*

- **[Deepmao](https://github.com/Sumanth181099/DeepMAO)** — *Deep Multi-scale Aware Overcomplete Network for Building Segmentation in Satellite Imagery.*

- **[Cmgfnet Building Extraction](https://github.com/hamidreza2015/CMGFNet-Building_Extraction)** — *Deep Learning Code for Building Extraction from very high resolution (VHR) remote sensing images.*

- **[Global Collinearity Aware Polygonizer For Polygonal Building Mapping In Remote Sensing](https://github.com/zhu-xlab/GCP)**

- **[Building Segmentation On Lr Hr Sr Satellite Imagery](https://github.com/ESAOpenSR/Segmentation-Models-Benchmark)** — *Perform building delineation on different types of satellite imagery: Low-Resolution (LR), High-Resolution (HR), and Super-Resolution (SR). The goal is to compare the performance of segmentation models across these varying resolutions.*

- **[Urbangraphsage](https://github.com/OMUZ9924/UrbanGraphSAGE)** — *Graph Neural Network (GraphSAGE) for urban building footprint extraction from Sentinel-2 satellite imagery.*

- **[Terratorch Building Segmentation](https://github.com/OMUZ9924/terratorch-building-segmentation)** — *Fine-tuning Geospatial Foundation Models (Prithvi, TerraMind) for building footprint segmentation from Sentinel-2 using TerraTorch — Algiers case study.*


---


### Segmentation - Solar panels

- **[Deep Learning For Solar Panel Recognition](https://github.com/saizk/Deep-Learning-for-Solar-Panel-Recognition)** — *Using both object detection with Yolov5 and Unet segmentation.*

- **[Deepsolar](https://github.com/wangzhecheng/DeepSolar)** — *A Machine Learning Framework to Efficiently Construct a Solar Deployment Database in the United States. [Dataset on kaggle](https://www.kaggle.com/datasets/tunguz/deep-solar-dataset), actually used a CNN for classification and segmentation is obtained by applying a threshold to the activation map. Original code is tf1 but [tf2/kers](https://github.com/aidan-fitz/deepsolar-v2) and a [pytorch implementation](https://github.com/wangzhecheng/deepsolar_pytorch) are available. Also checkout [Visualizations and in-depth analysis .. of the factors that can explain the adoption of solar energy in ..  Virginia].*
  
- **[Hyperion Solar Net](https://github.com/fvergaracontesse/hyperion_solar_net)** — *Trained classificaton & segmentation models on RGB imagery from Google Maps.*

- **[3d Pv Locator](https://github.com/kdmayer/3D-PV-Locator)** — *Large-scale detection of rooftop-mounted photovoltaic systems in 3D.*

- **[Pv Pipeline](https://github.com/kdmayer/PV_Pipeline)** — *DeepSolar for Germany.*

- **[Solar Panels Detection](https://github.com/dbaofd/solar-panels-detection)** — *Using SegNet, Fast SCNN & ResNet.*

- **[Predict Pv Yield](https://github.com/openclimatefix/predict_pv_yield)** — *Using optical flow & machine learning to predict PV yield.*

- **[Large Scale Solar Plant Monitoring](https://github.com/osmarluiz/Large-scale-solar-plant-monitoring)** — *Remote Sensing for Monitoring of Photovoltaic Power Plants in Brazil Using Deep Semantic Segmentation.*

- **[Panel Segmentation](https://github.com/NREL/Panel-Segmentation)** — *Determine the presence of a solar array in the satellite image (boolean True/False), using a VGG16 classification model.*

- **[Roofpedia](https://github.com/ualsg/Roofpedia)** — *An open registry of green roofs and solar roofs across the globe identified by Roofpedia through deep learning.*

- **[Predicting The Solar Potential Of Rooftops Using Image Segmentation And Structured Data](https://medium.com/nam-r/predicting-the-solar-potential-of-rooftops-using-image-segmentation-and-structured-data-61198c39d57c)** — *Medium article, using 20cm imagery & Unet.*

- **[Solar Pv Global Inventory](https://github.com/Lkruitwagen/solar-pv-global-inventory)**

- **[Remote Sensing Solar Pv](https://github.com/Lkruitwagen/remote-sensing-solar-pv)** — *A repository for sharing progress on the automated detection of solar PV arrays in sentinel-2 remote sensing imagery.*

- **[Solar Panel Segmentation)](https://github.com/gabrieltseng/solar-panel-segmentation)** — *Finding solar panels using USGS satellite imagery.*

- **[Solar Plant Detection](https://github.com/Amirmoradi94/solar_plant_detection)** — *Boundary extraction of Photovoltaic (PV) plants using Mask RCNN and Amir dataset.*

- **[Solardetection](https://github.com/A-Stangeland/SolarDetection)** — *Unet on satellite image from the USA and France.*

- **[Adopptrs](https://github.com/francois-rozet/adopptrs)** — *Automatic Detection Of Photovoltaic Panels Through Remote Sensing using unet & pytorch.*

- **[Solar Panel Locator](https://github.com/TorrBorr/solar-panel-locator)** — *The number of solar panel pixels was only ~0.2% of the total pixels in the dataset, so solar panel data was upsampled to account for the class imbalance.*

- **[Projects Solar Panel Detection](https://github.com/top-on/projects-solar-panel-detection)** — *List of project to detect solar panels from aerial/satellite images.*

- **[Satellite Computervision](https://github.com/mjevans26/Satellite_ComputerVision)** — *UNET to detect solar arrays from Sentinel-2 data, using Google Earth Engine and Tensorflow. Also covers parking lot detection.*

- **[Photovoltaic Detection](https://github.com/riccardocadei/photovoltaic-detection)** — *Detecting available rooftop area from satellite images to install photovoltaic panels.*

- **[Solar Unet](https://github.com/mjevans26/Solar_UNet)** — *U-Net models delineating solar arrays in Sentinel-2 imagery.*

- **[Solardetection Solafune](https://github.com/bit-guber/SolarDetection-solafune)** — *Solar Panel Detection Using Sentinel-2 for the Solafune Competition.*

- **[A Comparative Evaluation Of Deep Learning Techniques For Photovoltaic Panel Detection From Aerial Images](https://github.com/links-ads/access-solar-panels)**

- **[Ucsd Mlbootcamp Capstone](https://github.com/FederCO23/UCSD_MLBootcamp_Capstone)** — *Automatic Detection of Photovoltaic Power Stations Using Satellite Imagery and Deep Learning (Sentinel 2).*


---


### Segmentation - Ships & vessels

- **[Universal Segmentation Baseline Kaggle Airbus Ship Detection](https://github.com/OniroAI/Universal-segmentation-baseline-Kaggle-Airbus-Ship-Detection)** — *Kaggle Airbus Ship Detection Challenge - bronze medal solution.*

- **[Airbus Ship Segmentation](https://github.com/TheXirex/Airbus-Ship-Segmentation)** — *Unet.*

- **[Contrastive Ssl Ship Detection](https://github.com/alina2204/contrastive_SSL_ship_detection)** — *Contrastive self supervised learning for ship detection in Sentinel 2 images.*

- **[Airbus Ship Detection](https://github.com/odessitua/airbus-ship-detection)** — *Using DeepLabV3+.*

- **[Unet With Web Application Applied To Airbus Ships](https://github.com/glibesyck/ImageSegmentation)**


---


### Segmentation - Other manmade

- **[Aarsh2001/ml Challenge Nrsc](https://github.com/Aarsh2001/ML_Challenge_NRSC)** — *Electrical Substation detection.*

- **[Electrical Substation Detection](https://github.com/thisishardik/electrical_substation_detection)**

- **[Mcan Oilspilldetection](https://github.com/liyongqingupc/MCAN-OilSpillDetection)** — *Oil Spill Detection with A Multiscale Conditional Adversarial Network under Small Data Training.*

- **[Mining Detector](https://github.com/earthrise-media/mining-detector)** — *Detection of artisanal gold mines in Sentinel-2 satellite imagery for [Amazon Mining Watch](https://amazonminingwatch.org/). Also covers clandestine airstrips.*

- **[Eg Unet](https://github.com/tist0bsc/EG-UNet)** — *Deep Feature Enhancement Method for Land Cover With Irregular and Sparse Spatial Distribution Features: A Case Study on Open-Pit Mining.*

- **[Plastics](https://github.com/earthrise-media/plastics)** — *Detecting and Monitoring Plastic Waste Aggregations in Sentinel-2 Imagery.*

- **[Mados](https://github.com/gkakogeorgiou/mados)** — *Detecting Marine Pollutants and Sea Surface Features with Deep Learning in Sentinel-2 Imagery on the MADOS dataset.*

- **[Sadma](https://github.com/sheikhazhanmohammed/SADMA)** — *Residual Attention UNet on MARIDA: Marine Debris Archive is a marine debris-oriented dataset on Sentinel-2 satellite images.*

- **[Map Mapper](https://github.com/CoDIS-Lab/MAP-Mapper)** — *Marine Plastic Mapper is a tool for assessing marine macro-plastic density to identify plastic hotspots, underpinned by the MARIDA dataset.*

- **[Substation Seg](https://github.com/Lindsay-Lab/substation-seg)** — *Segmenting substations in Sentinel 2 satellite imagery.*

- **[Samselect](https://github.com/geoJoost/SAMSelect)** — *An Automated Spectral Index Search for Marine Debris using Segment-Anything (SAM).*


---


### Panoptic segmentation

- **[Things And Stuff Or How Remote Sensing Could Benefit From Panoptic Segmentation](https://softwaremill.com/things-and-stuff-or-how-remote-sensing-could-benefit-from-panoptic-segmentation/)**

- **[Utae Paps](https://github.com/VSainteuf/utae-paps)** — *PyTorch implementation of U-TAE and PaPs for satellite image time series panoptic segmentation.*

- **[Pastis Benchmark](https://github.com/VSainteuf/pastis-benchmark)**

- **[Panoptic Generator](https://github.com/abilius-app/Panoptic-Generator)** — *This module converts GIS data into panoptic segmentation tiles.*

- **[Bsb Aerial Dataset](https://github.com/osmarluiz/BSB-Aerial-Dataset)** — *An example on how to use Detectron2's Panoptic-FPN in the BSB Aerial Dataset.*


---


### Segmentation - Miscellaneous

- **[Seg Eval](https://github.com/itracasa/seg-eval)** — *SegEval is a Python library that provides tools for evaluating semantic segmentation models. Generate evaluation regions and to analyze segmentation results within them.*

- **[Awesome Satellite Images Segmentation](https://github.com/mrgloom/awesome-semantic-segmentation#satellite-images-segmentation)**

- **[Satellite Image Segmentation: A Workflow With U Net](https://medium.com/vooban-ai/satellite-image-segmentation-a-workflow-with-u-net-7ff992b2a56e)** — *Is a decent intro article.*

- **[Mmsegmentation](https://github.com/open-mmlab/mmsegmentation)** — *Semantic Segmentation Toolbox with support for many remote sensing datasets including LoveDA, Potsdam, Vaihingen & iSAID.*

- **[Segmentation Gym](https://github.com/Doodleverse/segmentation_gym)** — *A neural gym for training deep learning models to carry out geoscientific image segmentation.*

- **[Using A U Net For Image Segmentation, Blending Predicted Patches Smoothly Is A Must To Please The Human Eye](https://github.com/Vooban/Smoothly-Blend-Image-Patches)** — *Python code to blend predicted patches smoothly. See [Satellite-Image-Segmentation-with-Smooth-Blending](https://github.com/MaitrySinha21/Satellite-Image-Segmentation-with-Smooth-Blending).*

- **[Dca](https://github.com/Luffy03/DCA)** — *Deep Covariance Alignment for Domain Adaptive Remote Sensing Image Segmentation.*

- **[Scattnet](https://github.com/lehaifeng/SCAttNet)** — *Semantic Segmentation Network with Spatial and Channel Attention Mechanism.*


- **[Efficient Transformer](https://github.com/zyxu1996/Efficient-Transformer)** — *Efficient Transformer for Remote Sensing Image Segmentation.*

- **[Weakly Supervised](https://github.com/LobellLab/weakly_supervised)** — *Weakly Supervised Deep Learning for Segmentation of Remote Sensing Imagery.*

- **[Hrcnet High Resolution Context Extraction Network](https://github.com/zyxu1996/HRCNet-High-Resolution-Context-Extraction-Network)** — *High-Resolution Context Extraction Network for Semantic Segmentation of Remote Sensing Images.*

- **[Semantic Segmentation Of Sar Images Using A Self Supervised Technique](https://github.com/cattale93/pytorch_self_supervised_learning)**

- **[Satellite Segmentation Pytorch](https://github.com/obravo7/satellite-segmentation-pytorch)** — *Explores a wide variety of image augmentations to increase training dataset size.*

- **[Spectralformer](https://github.com/danfenghong/IEEE_TGRS_SpectralFormer)** — *Rethinking hyperspectral image classification with transformers.*

- **[Unsupervised Segmentation Of Hyperspectral Remote Sensing Images With Superpixels](https://github.com/mpBarbato/Unsupervised-Segmentation-of-Hyperspectral-Remote-Sensing-Images-with-Superpixels)**

- **[Semantic Segmentation With Sparse Labels](https://github.com/Hua-YS/Semantic-Segmentation-with-Sparse-Labels)**

- **[Sndf](https://github.com/mi18/SNDF)** — *Superpixel-enhanced deep neural forest for remote sensing image semantic segmentation.*

- **[Dynamic Rs Segmentation](https://github.com/keillernogueira/dynamic-rs-segmentation)** — *Dynamic Multi-Context Segmentation of Remote Sensing Images based on Convolutional Networks.*

- **[Segmentation Models.pytorch](https://github.com/qubvel/segmentation_models.pytorch)** — *Segmentation models with pretrained backbones, has been used in multiple winning solutions to remote sensing competitions.*

- **[Ssrn](https://github.com/zilongzhong/SSRN)** — *Spectral-Spatial Residual Network for Hyperspectral Image Classification: A 3-D Deep Learning Framework.*

- **[So Dnn](https://github.com/PanXinZebra/SO-DNN)** — *Simplified object-based deep neural network for very high resolution remote sensing image classification.*

- **[Sanet](https://github.com/mrluin/SANet-PyTorch)** — *Scale-Aware Network for Semantic Segmentation of High-Resolution Aerial Images.*

- **[Aerial Segmentation](https://github.com/alpemek/aerial-segmentation)** — *Learning Aerial Image Segmentation from Online Maps.*

- **[Detectron2 Fpn + Pointrend Model For Amazing Satellite Image Segmentation](https://affine.medium.com/detectron2-fpn-pointrend-model-for-amazing-satellite-image-segmentation-183456063e15)** — *15% increase in accuracy when compared to the U-Net model.*

- **[Hybridsn](https://github.com/purbayankar/HybridSN-pytorch)** — *Exploring 3D-2D CNN Feature Hierarchy for Hyperspectral Image Classification.*

- **[Tnnls 2022 X Gpn](https://github.com/B-Xi/TNNLS_2022_X-GPN)** — *Semisupervised Cross-scale Graph Prototypical Network for Hyperspectral Image Classification.*

- **[Singlescenesemsegtgrs2022](https://github.com/sudipansaha/singleSceneSemSegTgrs2022)** — *Unsupervised Single-Scene Semantic Segmentation for Earth Observation.*

- **[A Fast And Compact 3 D Cnn For Hsic](https://github.com/mahmad00/A-Fast-and-Compact-3-D-CNN-for-HSIC)** — *A Fast and Compact 3-D CNN for Hyperspectral Image Classification.*

- **[Hsnrs](https://github.com/Walkerlikesfish/HSNRS)** — *Hourglass-ShapeNetwork Based Semantic Segmentation for High Resolution Aerial Imagery.*

- **[Gigcn](https://github.com/ShuGuoJ/GiGCN)** — *Graph-in-Graph Convolutional Network for Hyperspectral Image Classification.*

- **[Ssan](https://github.com/EtPan/SSAN)** — *Spectral-Spatial Attention Networks for Hyperspectral Image Classification.*

- **[Drone Images Semantic Segmentation](https://github.com/ayushdabra/drone-images-semantic-segmentation)** — *Multiclass Semantic Segmentation of Aerial Drone Images Using Deep Learning.*

- **[Satellite Image Segmentation With Smooth Blending](https://github.com/MaitrySinha21/Satellite-Image-Segmentation-with-Smooth-Blending)** — *Uses [Smoothly-Blend-Image-Patches](https://github.com/Vooban/Smoothly-Blend-Image-Patches).*

- **[Bayesianunet](https://github.com/tha-santacruz/BayesianUNet)** — *Pytorch Bayesian UNet model for segmentation and uncertainty prediction, applied to the Potsdam Dataset.*

- **[Raanet](https://github.com/Lrr0213/RAANet)** — *A Residual ASPP with Attention Framework for Semantic Segmentation of High-Resolution Remote Sensing Images.*

- **[Wheelruts Semanticsegmentation](https://github.com/SmartForest-no/wheelRuts_semanticSegmentation)** — *Mapping wheel-ruts from timber harvesting operations using deep learning techniques in drone imagery.*

- **[Lwn For Uavrsi](https://github.com/syliudf/LWN-for-UAVRSI)** — *Light-Weight Semantic Segmentation Network for UAV Remote Sensing Images, applied to Vaihingen, UAVid and UDD6 datasets.*

- **[Hypernet](https://github.com/ESA-PhiLab/hypernet)** — *Library which implements hyperspectral image (HSI) segmentation.*

- **[St Unet](https://github.com/XinnHe/ST-UNet)** — *Swin Transformer Embedding UNet for Remote Sensing Image Semantic Segmentation.*

- **[Edft](https://github.com/h1063135843/EDFT)** — *Efficient Depth Fusion Transformer for Aerial Image Semantic Segmentation.*

- **[Wiconet](https://github.com/ggsDing/WiCoNet)** — *Looking Outside the Window: Wide-Context Transformer for the Semantic Segmentation of High-Resolution Remote Sensing Images.*

- **[Crgnet](https://github.com/YonghaoXu/CRGNet)** — *Consistency-Regularized Region-Growing Network for Semantic Segmentation of Urban Scenes with Point-Level Annotations.*

- **[Sa Unet](https://github.com/Yancccccc/SA-UNet)** — *Improved U-Net Remote Sensing Classification Algorithm Fusing Attention and Multiscale Features.*

- **[Manet](https://github.com/lironui/Multi-Attention-Network)** — *Multi-Attention-Network for Semantic Segmentation of Fine Resolution Remote Sensing Images.*

- **[Banet](https://github.com/lironui/BANet)** — *Transformer Meets Convolution: A Bilateral Awareness Network for Semantic Segmentation of Very Fine Resolution Urban Scene Images.*

- **[Macu Net](https://github.com/lironui/MACU-Net)** — *MACU-Net for Semantic Segmentation of Fine-Resolution Remotely Sensed Images.*

- **[Dnas](https://github.com/faye0078/DNAS)** — *Decoupling Neural Architecture Search for High-Resolution Remote Sensing Image Semantic Segmentation.*

- **[A2 Fpn](https://github.com/lironui/A2-FPN)** — *A2-FPN for Semantic Segmentation of Fine-Resolution Remotely Sensed Images.*

- **[Maresu Net](https://github.com/lironui/MAResU-Net)** — *Multi-stage Attention ResU-Net for Semantic Segmentation of Fine-Resolution Remote Sensing Images.*

- **[Rsen](https://github.com/YonghaoXu/RSEN)** — *Robust Self-Ensembling Network for Hyperspectral Image Classification.*

- **[Msnet](https://github.com/taochx/MSNet)** — *Multispectral semantic segmentation network for remote sensing images.*

- **[Swin Transformer Semantic Segmentation](https://github.com/koechslin/Swin-Transformer-Semantic-Segmentation)** — *Satellite Image Semantic Segmentation.*

- **[Uda For Rs](https://github.com/Levantespot/UDA_for_RS)** — *Unsupervised Domain Adaptation for Remote Sensing Semantic Segmentation with Transformer.*

- **[A 3d Cnn Am Dsc Model For Hyperspectral Image Classification](https://github.com/hahatongxue/A-3D-CNN-AM-DSC-model-for-hyperspectral-image-classification)** — *Attention Mechanism and Depthwise Separable Convolution Aided 3DCNN for Hyperspectral Remote Sensing Image Classification.*

- **[Contrastive Distillation](https://github.com/edornd/contrastive-distillation)** — *A Contrastive Distillation Approach for Incremental Semantic Segmentation in Aerial Images.*

- **[Segforestnet](https://github.com/gritzner/SegForestNet)** — *SegForestNet: Spatial-Partitioning-Based Aerial Image Segmentation.*

- **[Mfvnet](https://github.com/weichenrs/MFVNet)** — *MFVNet: Deep Adaptive Fusion Network with Multiple Field-of-Views for Remote Sensing Image Semantic Segmentation.*

- **[Wildebeest Unet](https://github.com/zijing-w/Wildebeest-UNet)** — *Detecting wildebeest and zebras in Serengeti-Mara ecosystem from very-high-resolution satellite imagery.*

- **[Segment Anything Eo](https://github.com/aliaksandr960/segment-anything-eo)** — *Earth observation tools for Meta AI Segment Anything (SAM - Segment Anything Model).*

- **[Hr Image Classification Sdf2n](https://github.com/SicongLiuRS/HR-Image-classification_SDF2N)** — *A Shallow-to-Deep Feature Fusion Network for VHR Remote Sensing Image Classification.*

- **[Sink Seg](https://github.com/mvrl/sink-seg)** — *Automatic Segmentation of Sinkholes Using a Convolutional Neural Network.*

- **[Tiling And Stitching Segmentation Output For Remote Sensing: Basic Challenges And Recommendations](https://arxiv.org/abs/1805.12219)**

- **[Emrt](https://github.com/peach-xiao/EMRT)** — *Enhancing Multiscale Representations With Transformer for Remote Sensing Image Semantic Segmentation.*

- **[Uda For Rs](https://github.com/Levantespot/UDA_for_RS)** — *Unsupervised Domain Adaptation for Remote Sensing Semantic Segmentation with Transformer.*

- **[Cmtfnet](https://github.com/DrWuHonglin/CMTFNet)** — *CMTFNet: CNN and Multiscale Transformer Fusion Network for Remote Sensing Image Semantic Segmentation.*

- **[Cm Unet](https://github.com/XiaoBuL/CM-UNet)** — *Hybrid CNN-Mamba UNet for Remote Sensing Image Semantic Segmentation.*

- **[Using Stable Diffusion To Improve Image Segmentation Models](https://medium.com/edge-analytics/using-stable-diffusion-to-improve-image-segmentation-models-1e99c25acbf)** — *Augmenting Data with Stable Diffusion.*

- **[Ssrs](https://github.com/sstary/SSRS)** — *Semantic Segmentation for Remote Sensing, multiple networks implemented.*

- **[Bioscann](https://github.com/BiodiversityLab/bioscann)** — *BIOdiversity Segmentation and Classification with Artificial Neural Networks.*

- **[Resunet A](https://github.com/feevos/resuneta)** — *A deep learning framework for semantic segmentation of remotely sensed data.*

- **[Ssg2](https://github.com/feevos/ssg2)** — *A New Modelling Paradigm for Semantic Segmentation.*

- **[Dbfnet](https://github.com/Luffy03/DBFNet)** — *Deep Bilateral Filtering Network for Point-Supervised Semantic Segmentation in Remote Sensing Images.*

- **[Pgnet](https://github.com/Fhujinwu/PGNet)** — *PGNet: Positioning Guidance Network for Semantic Segmentation of Very-High-Resolution Remote Sensing Images [paper](https://www.mdpi.com/2072-4292/14/17/4219).*

- **[Asd](https://github.com/Jingtao-Li-CVer/ASD)** — *Anomaly Segmentation for High-Resolution Remote Sensing Images Based on Pixel Descriptors.*

- **[U Nets Implementation](https://github.com/Aadit3003/u-nets-implementation)** — *Semantic-Segmentation-with-U-Nets.*

- **[Sdm](https://github.com/caoql98/SDM)** — *Scale-aware Detailed Matching for Few-Shot Aerial Image Semantic Segmentation.*

- **[Transferability Remote Sensing](https://github.com/GDAOSU/Transferability-Remote-Sensing)** — *On the Transferability of Learning Models for Semantic Segmentation for Remote Sensing Data.*

- **[Data Centric Satellite Segmentation](https://github.com/microsoft/data-centric-satellite-segmentation)** — *Contains implementations of data-centric approaches for improving semantic segmentation on satellite imagery, from Microsoft.*

- **[Hslabeling](https://github.com/linjiaxing99/HSLabeling)** — *Towards Efficient Labeling for Large-scale Remote Sensing Image Segmentation with Hybrid Sparse Labeling.*

- **[Remotesam](https://github.com/1e12Leon/RemoteSAM)** — *Towards Segment Anything for Earth Observation (SAM).*

- **[Hierars](https://github.com/AI-Tianlong/HieraRS)** — *A Hierarchical Segmentation Paradigm for Remote Sensing Enabling Multi-Granularity Interpretation and Cross-Domain Transfer.*

- **[Multifrancefences](https://github.com/r-wenger/MultiFranceFences)** — *Large-scale fence detection using deep learning and multimodal aerial imagery.*

#


---


### Instance segmentation

In instance segmentation, each individual 'instance' of a segmented area is given a unique label. For detection of very small objects this may be a good approach, but it can struggle separating individual objects that are closely spaced.

- **[Mask Rcnn](https://github.com/matterport/Mask_RCNN)** — *Generates bounding boxes and segmentation masks for each instance of an object in the image. It is very commonly used for instance segmentation & object detection.*

- **[Building Detection Maskrcnn](https://github.com/Mstfakts/Building-Detection-MaskRCNN)** — *Building detection from the SpaceNet dataset by using Mask RCNN.*

- **[Mask Rcnn For Caravans](https://github.com/OrdnanceSurvey/Mask_RCNN-for-Caravans)** — *Detect caravan footprints from OS imagery.*

- **[Parking Bays Detectron2](https://github.com/spiyer99/parking_bays_detectron2)** — *Detecting parking bays with satellite imagery. Used Detectron2 and synthetic data with Unreal, superior performance to using Mask RCNN.*

- **[Circle Finder](https://github.com/zinsmatt/Circle_Finder)** — *Circular Shapes Detection in Satellite Imagery, 2nd place solution to the Circle Finder Challenge.*

- **[Lawn Maskrcnn](https://github.com/matthewnaples/Lawn_maskRCNN)** — *Detecting lawns from satellite images of properties in the Cedar Rapids area using Mask-R-CNN.*

- **[Cropmask Rcnn](https://github.com/ecohydro/CropMask_RCNN)** — *Segmenting center pivot agriculture to monitor crop water use in drylands with Mask R-CNN and Landsat satellite imagery.*

- **[Mask Rcnn For Spacenet Off Nadir Building Detection](https://github.com/ashnair1/Mask-RCNN-for-Off-Nadir-Building-Detection)**

- **[Catnet](https://github.com/yeliudev/CATNet)** — *Learning to Aggregate Multi-Scale Context for Instance Segmentation in Remote Sensing Images.*

- **[Object Detection On Satellite Images Using Mask R Cnn](https://github.com/ThayN15/Object-Detection-on-Satellite-Images-using-Mask-R-CNN)** — *Detect ships.*

- **[Factseg](https://github.com/Junjue-Wang/FactSeg)** — *Foreground Activation Driven Small Object Semantic Segmentation in Large-Scale Remote Sensing Imagery (TGRS), also see [FarSeg](https://github.com/Z-Zheng/FarSeg) and [FreeNet](https://github.com/Z-Zheng/FreeNet), implementations of research paper.*

- **[Aqua Python](https://github.com/tclavelle/aqua_python)** — *Detecting aquaculture farms using Mask R-CNN.*

- **[Rsprompter](https://github.com/KyanChen/RSPrompter)** — *Learning to Prompt for Remote Sensing Instance Segmentation based on Visual Foundation Model.*

- **[Vmd Mask Rcnn Pipeline](https://github.com/Fen100/VMD-Mask-RCNN-pipeline)** — *Detecting and segmenting sand mining river vessels on the Vietnam Mekong Delta, using PlanetScope imagery and Mask R-CNN.*

- **[Bright Cvprw26](https://github.com/ChenHongruixuan/BRIGHT/tree/master/cvprw26)** — *Mask R-CNN baseline for multimodal building damage instance segmentation on BRIGHT.*

#


---


### Object detection

<p align="center">
  <img src="images/object-detection.png" width="600">
  <br>
  <b>Image showing the suitability of rotated bounding boxes in remote sensing.</b>
</p>

Object detection in remote sensing involves locating and surrounding objects of interest with bounding boxes. Due to the large size of remote sensing images and the fact that objects may only comprise a few pixels, object detection can be challenging in this context. The imbalance between the area of the objects to be detected and the background, combined with the potential for objects to be easily confused with random features in the background, further complicates the task. Object detection generally performs better on larger objects, but becomes increasingly difficult as the objects become smaller and more densely packed. The accuracy of object detection models can also degrade rapidly as image resolution decreases, which is why it is common to use high resolution imagery, such as 30cm RGB, for object detection in remote sensing. A unique characteristic of aerial images is that objects can be oriented in any direction. To effectively extract measurements of the length and width of an object, it can be crucial to use rotated bounding boxes that align with the orientation of the object. This approach enables more accurate and meaningful analysis of the objects within the image. [Image source](https://www.mdpi.com/2072-4292/13/21/4291)


---


### Object tracking in videos

- **[Tctrack](https://github.com/vision4robotics/TCTrack)** — *Temporal Contexts for Aerial Tracking.*

- **[Cfme](https://github.com/SY-Xuan/CFME)** — *Object Tracking in Satellite Videos by Improved Correlation Filters With Motion Estimations.*

- **[Tgram](https://github.com/HeQibin/TGraM)** — *Multi-Object Tracking in Satellite Videos with Graph-Based Multi-Task Modeling.*

- **[Satellite Video Mod Groundtruth](https://github.com/zhangjunpeng9354/satellite_video_mod_groundtruth)** — *Groundtruth on satellite video for evaluating moving object detection algorithm.*

- **[Moving Object Detection Dsfnet](https://github.com/ChaoXiao12/Moving-object-detection-DSFNet)** — *DSFNet: Dynamic and Static Fusion Network for Moving Object Detection in Satellite Videos.*

- **[Hift](https://github.com/vision4robotics/HiFT)** — *Hierarchical Feature Transformer for Aerial Tracking.*


---


### Object detection with rotated bounding boxes

Orinted bounding boxes (OBB) are polygons representing rotated rectangles. For datasets checkout DOTA & HRSC2016. Start with Yolov8

- **[Mmrotate](https://github.com/open-mmlab/mmrotate)** — *Rotated Object Detection Benchmark, with pretrained models and function for inferencing on very large images.*

- **[Orienteddet](https://github.com/DL4EO/oriented-det)** — *A lightweight PyTorch framework for rotated object detection in aerial and satellite imagery, with oriented models, geometry operations and DOTA support.*

- **[Obbdetection](https://github.com/jbwang1997/OBBDetection)** — *An oriented object detection library, which is based on MMdetection.*

- **[Rotate Yolov3](https://github.com/ming71/rotate-yolov3)** — *Rotation object detection implemented with yolov3. Also see [yolov3-polygon](https://github.com/ming71/yolov3-polygon).*

- **[Drbox](https://github.com/liulei01/DRBox)** — *For detection tasks where the objects are orientated arbitrarily, e.g. vehicles, ships and airplanes.*

- **[S2anet](https://github.com/csuhan/s2anet)** — *Align Deep Features for Oriented Object Detection.*

- **[Cfc Net](https://github.com/ming71/CFC-Net)** — *A Critical Feature Capturing Network for Arbitrary-Oriented Object Detection in Remote Sensing Images.*

- **[Redet](https://github.com/csuhan/ReDet)** — *A Rotation-equivariant Detector for Aerial Object Detection.*

- **[Bbavectors Oriented Object Detection](https://github.com/yijingru/BBAVectors-Oriented-Object-Detection)** — *Oriented Object Detection in Aerial Images with Box Boundary-Aware Vectors.*

- **[Csl Retinanet Tensorflow](https://github.com/Thinklab-SJTU/CSL_RetinaNet_Tensorflow)** — *Arbitrary-Oriented Object Detection with Circular Smooth Label.*

- **[R3det On Mmdetection](https://github.com/SJTU-Thinklab-Det/r3det-on-mmdetection)** — *R3Det: Refined Single-Stage Detector with Feature Refinement for Rotating Object.*

- **[R Dfpn Fpn Tensorflow](https://github.com/yangxue0827/R-DFPN_FPN_Tensorflow)** — *Rotation Dense Feature Pyramid Networks (Tensorflow).*

- **[R2cnn Faster Rcnn Tensorflow](https://github.com/DetectionTeamUCAS/R2CNN_Faster-RCNN_Tensorflow)** — *Rotational region detection based on Faster-RCNN.*

- **[Rotated Retinanet](https://github.com/ming71/Rotated-RetinaNet)** — *Implemented in pytorch, it supports the following datasets: DOTA, HRSC2016, ICDAR2013, ICDAR2015, UCAS-AOD, NWPU VHR-10, 