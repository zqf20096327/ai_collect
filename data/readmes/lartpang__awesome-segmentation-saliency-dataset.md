# Another Awesome Dataset List ![Badge](https://img.shields.io/badge/-As%20awesome%20as%20you%20think!-red?style=flat-square)

<div align="center">
  <img src="assets/header.png" alt="Another Awesome Dataset List header" width="100%">
  <p><sub>Header artwork generated with <a href="https://github.com/lartpang/semantic-field-editorial">semantic-field-editorial</a>.</sub></p>
  <p>
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT"></a>
    <img src="https://img.shields.io/github/last-commit/lartpang/awesome-segmentation-saliency-dataset?style=flat-square" alt="GitHub last commit">
    <img src="https://img.shields.io/github/issues/lartpang/awesome-segmentation-saliency-dataset?style=flat-square" alt="GitHub issues">
    <img src="https://img.shields.io/github/stars/lartpang/awesome-segmentation-saliency-dataset?style=flat-square" alt="GitHub stars">
  </p>
</div>

> [!note]
> - 💖 Some great tools can be found at [resource websites](#resource-websites).
> - 😄 Please **cite the related paper** if you **use their dataset**
> - 🌜 I list some other datasets in the issue [https://github.com/lartpang/awesome-segmentation-saliency-dataset/issues/15](https://github.com/lartpang/awesome-segmentation-saliency-dataset/issues/15). I hope it works for you.

- [Another Awesome Dataset List ](#another-awesome-dataset-list-)
  - [Saliency](#saliency)
    - [RGB Saliency](#rgb-saliency)
      - [MSRA(MSRA10K/MSRA-B)](#msramsra10kmsra-b)
      - [SED1/2](#sed12)
      - [ASD(MSRA1000/MSRA1K)](#asdmsra1000msra1k)
      - [DUT-OMRON](#dut-omron)
      - [DUTS](#duts)
      - [DUTS-MM/DUTS-MQ](#duts-mmduts-mq)
      - [SOC (Salient Objects in Clutter)](#soc-salient-objects-in-clutter)
      - [HKU-IS](#hku-is)
      - [SOD (Salient Object Dataset)](#sod-salient-object-dataset)
      - [Infrared](#infrared)
      - [ImgSal](#imgsal)
      - [ECSSD/CSSD](#ecssdcssd)
      - [THUR15K](#thur15k)
      - [Bruce-A](#bruce-a)
      - [Judd-A](#judd-a)
      - [PASCAL-S](#pascal-s)
      - [UCSB](#ucsb)
      - [OSIE](#osie)
      - [ACSD](#acsd)
      - [WXSOD](#wxsod)
    - [RGB-D Saliency](#rgb-d-saliency)
      - [SIP](#sip)
      - [NLPR/RGBD1000](#nlprrgbd1000)
      - [NJU400/2000](#nju4002000)
      - [STEREO/SSB](#stereossb)
      - [LFSD](#lfsd)
      - [RGBD135/DES](#rgbd135des)
      - [DUT-RGBD/DUTLF-Depth](#dut-rgbddutlf-depth)
      - [SSD/SSD100](#ssdssd100)
      - [ReDWeb-S](#redweb-s)
      - [COME15K](#come15k)
    - [RGB-T Saliency](#rgb-t-saliency)
      - [VT-IMAG](#vt-imag)
      - [UVT2000](#uvt2000)
      - [un-VT821/1000/5000](#un-vt82110005000)
      - [VT723](#vt723)
      - [VT5000](#vt5000)
      - [VT1000](#vt1000)
      - [VT821](#vt821)
    - [Underwater Salient Object Detection](#underwater-salient-object-detection)
      - [USOD](#usod)
      - [USOD10K](#usod10k)
      - [CSOD10K for Condition-Constrained SOD](#csod10k-for-condition-constrained-sod)
      - [MAS3K for Marine Animal Segmentation](#mas3k-for-marine-animal-segmentation)
      - [RMAS for Marine Animal Segmentation](#rmas-for-marine-animal-segmentation)
    - [Dichotomous Image Segmentation](#dichotomous-image-segmentation)
      - [DIS5K](#dis5k)
    - [High-Resolution Saliency](#high-resolution-saliency)
      - [HRSOD/DAVIS-S](#hrsoddavis-s)
    - [Co-Saliency](#co-saliency)
      - [ImagePair](#imagepair)
      - [MSRC](#msrc)
      - [WICOS](#wicos)
      - [iCoSeg](#icoseg)
      - [CoCA: Common Category Aggregation (CoCA) dataset](#coca-common-category-aggregation-coca-dataset)
      - [CoSal2015](#cosal2015)
      - [CoSOD3k](#cosod3k)
      - [RGBDCosal150](#rgbdcosal150)
      - [RGBDCoseg183](#rgbdcoseg183)
      - [INCT2016](#inct2016)
    - [Video Saliency](#video-saliency)
      - [RSD(PKU-RSD)](#rsdpku-rsd)
      - [STC](#stc)
      - [SegTrackV1/V2](#segtrackv1v2)
      - [ViSal](#visal)
      - [MCL](#mcl)
      - [UVSD](#uvsd)
      - [VOS](#vos)
    - [RGB-D Video Saliency](#rgb-d-video-saliency)
      - [RDVSv2](#rdvsv2)
    - [Reasoning SOD](#reasoning-sod)
      - [OC-SODBench](#oc-sodbench)
    - [Other](#other)
      - [XPIE](#xpie)
      - [SOS](#sos)
      - [MSO](#mso)
      - [ILSO-1K/2K](#ilso-1k2k)
      - [HS-SOD](#hs-sod)
      - [KAIST Salient Pedestrian Dataset](#kaist-salient-pedestrian-dataset)
      - [Grayscale-Thermal Foreground Detection Dataset](#grayscale-thermal-foreground-detection-dataset)
  - [COD (Camouflaged/Concealed Object Detection)](#cod-camouflagedconcealed-object-detection)
    - [RGB Image COD](#rgb-image-cod)
      - [NC4K](#nc4k)
      - [COD10K](#cod10k)
      - [CAMO](#camo)
      - [CHAMELEON](#chameleon)
      - [CPD1K: Camouflaged People Dataset](#cpd1k-camouflaged-people-dataset)
      - [CPD-UAV](#cpd-uav)
      - [UAV-CPD](#uav-cpd)
      - [COD10K-C for Robustness](#cod10k-c-for-robustness)
      - [OPC16K for Realistic COD](#opc16k-for-realistic-cod)
    - [RGB Video COD](#rgb-video-cod)
      - [MoCA-Mask](#moca-mask)
      - [CAD (Camouflaged Animation Dataset)](#cad-camouflaged-animation-dataset)
      - [YUV20K](#yuv20k)
      - [CAMotion](#camotion)
    - [RGB-T Image COD](#rgb-t-image-cod)
      - [Camo-M3FD](#camo-m3fd)
    - [RGB-D Image COD](#rgb-d-image-cod)
      - [ACOD-12K](#acod-12k)
      - [CODD](#codd)
    - [Terahertz Image COS/COD](#terahertz-image-coscod)
      - [Active Terahertz Imaging Datasets](#active-terahertz-imaging-datasets)
    - [Open-Vocabulary Camouflaged Object Segmentation](#open-vocabulary-camouflaged-object-segmentation)
      - [OVCamo](#ovcamo)
  - [DBD (Defocus Blur Detection)](#dbd-defocus-blur-detection)
    - [CUHK](#cuhk)
    - [DUT](#dut)
      - [Real-V1](#real-v1)
      - [Real-V2](#real-v2)
      - [Simulated Dataset](#simulated-dataset)
    - [CTCUG](#ctcug)
    - [EBD](#ebd)
  - [Industrial Scene](#industrial-scene)
    - [Crack Detection](#crack-detection)
      - [T-CRACK \& C-CRACK](#t-crack--c-crack)
    - [Surface Defect Detection](#surface-defect-detection)
      - [SD-saliency-900](#sd-saliency-900)
    - [AD (Anomaly Detection)](#ad-anomaly-detection)
      - [MVTec AD](#mvtec-ad)
      - [MPDD](#mpdd)
  - [Medical Scene](#medical-scene)
    - [Trichomonas Vaginalis Segmentation](#trichomonas-vaginalis-segmentation)
      - [TVMI3K](#tvmi3k)
    - [Vessel Segmentation](#vessel-segmentation)
      - [XCAD](#xcad)
  - [Segmentation](#segmentation)
    - [VOS (Video Object Segmentation)](#vos-video-object-segmentation)
      - [DAVIS](#davis)
      - [TAO-VOS](#tao-vos)
      - [OVOS](#ovos)
    - [Image Segmentation](#image-segmentation)
      - [aNYU](#anyu)
      - [Supervisely Portrait Dataset](#supervisely-portrait-dataset)
      - [Clothing Parsing](#clothing-parsing)
      - [HumanParsing-Dataset](#humanparsing-dataset)
      - [Look into Person (LIP)](#look-into-person-lip)
      - [Taobao Commodity Dataset (TCD)](#taobao-commodity-dataset-tcd)
      - [Object Extraction Dataset](#object-extraction-dataset)
      - [Clothing Co-Parsing (CCP) Dataset](#clothing-co-parsing-ccp-dataset)
      - [People segmentation dataset](#people-segmentation-dataset)
  - [Matting](#matting)
    - [alphamatting.com](#alphamattingcom)
    - [Composition-1k: Deep Image Matting](#composition-1k-deep-image-matting)
    - [Semantic Human Matting](#semantic-human-matting)
    - [Matting-Human-Datasets](#matting-human-datasets)
    - [PFCN](#pfcn)
    - [Deep Automatic Portrait Matting](#deep-automatic-portrait-matting)
  - [Other](#other-1)
    - [Large-scale Fashion (DeepFashion) Database](#large-scale-fashion-deepfashion-database)
    - [Tencent ML-Images](#tencent-ml-images)
  - [Reference](#reference)
    - [Survey](#survey)
    - [Project](#project)
  - [More](#more)
    - [Similiar Projects](#similiar-projects)
    - [Research Institutes](#research-institutes)
    - [Resource Websites](#resource-websites)


## Saliency

### RGB Saliency

#### MSRA(MSRA10K/MSRA-B)

* Paper: [Learningto detect a salient object](http://mmlab.ie.cuhk.edu.hk/2007/CVPR07_detect.pdf)
* Home: Nankai University Media Computing Laboratory: [https://mmcheng.net/zh/msra10k/](https://mmcheng.net/zh/msra10k/)
* Download:
  + MSRA10K(formally named as THUS10000; [195MB](http://mftp.mmcheng.net/Data/MSRA10K_Imgs_GT.zip): images + binary masks):
    - Pixel accurate salient object labeling for **10000 images** from MSRA dataset.
    - Please cite our paper [https://mmcheng.net/SalObj/] if you use it.
    - Saliency maps and salient object region segmentation for other 20+ alternative methods are also available ([Baidu Yun](http://pan.baidu.com/s/1dEaQqlF#path=%252FShare%252FSalObjRes)).
  + MSRA-B ([111MB](http://mftp.mmcheng.net/Data/MSRA-B.zip): images + binary masks):
    - Pixel accurate salient object labeling for **5000 images** from MSRA-B dataset.
    - Please cite the corresponding paper [https://mmcheng.net/drfi/] if you use it.

We study visual attention by detecting salient objects in input images. We formulate salient object detection as an image segmentation problem, where we separate salient objects from image background. We propose a series of novel features, including multi-scale contrast, center-surround histograms and color space distributions, to describe salient objects locally, regionally and globally. Conditional random fields are learned to efficiently combine these features for salient object detection. We also built an image database containing tens of thousands of fully labeled images tagged by multiple users. To the best of our knowledge, it is the first large-scale image database for quantitative evaluation of visual attention algorithms. We validated our method on this image database, which is publicly available in this paper.

People may have different opinions about salient objects in images. To solve the problem of "what salient objects may look like in a given image", we conduct a voting strategy by labeling "ground truth" salient objects in multiple users' images. In this paper, we focus on the case of a single salient object in an image. Salient object representation. Typically, we represent a given object as a binary mask $A={a_x}$ in a given image I. For each pixel x, $a_x∈{1, 0}$ is a binary label to indicate whether a pixel belongs to a salient object. **For labeling and evaluation, we ask the user to draw a rectangle to specify a salient object. Our detection algorithm also outputs a rectangle.**

Image sources. We collected a very large image database of 130,099 high-quality images from various sources, mainly from image forums and image search engines. We then manually selected more than 60,000 images, each of which contained a salient object or a unique foreground object. We further selected 20,840 images for labeling. During the selection process, we excluded any images containing very large salient objects, allowing for a more accurate assessment of the performance of the detection.

Labeling consistency. For each image to be labeled, we ask the user to draw a rectangle that encloses the largest object in the image according to his/her own understanding. Rectangles labeled by different users are usually not the same. To reduce labeling inconsistency, we select a "real" label from rectangles drawn by multiple users.

<details>
<summary>中文介绍</summary>

我们通过检测输入图像中的显著对象来研究视觉注意力. 我们将显著对象检测表示为图像分割问题, 我们将显著对象与图像背景分开. 我们提出了一系列新颖的特征, 包括多尺度对比度, 中心环绕直方图和颜色空间分布, 以在本地, 区域和全局描述显著对象. 学习条件随机场以有效地组合这些特征以用于显著对象检测. 我们还构建了一个**包含由多个用户标记的数以万计的完全标记图像的图像数据库**. 据我们所知, 它是第一个用于视觉注意算法定量评估的大型图像数据库. 我们在此图像数据库上验证了我们的方法, 该数据库在本文中是公开的.

人们可能对图像中的显著对象有不同的看法. 为了解决"给定图像中可能是什么样的显著对象"的问题, 我们通过在多个用户的图像中标记"真值"显著对象来进行投票策略. 在本文中, 我们关注图像中单个显著对象的情况. 显著性对象表示. 通常, 我们**将给定对象表示为给定image I中的二元mask** $A={a_x}$. 对于每个像素x, $a_x∈{1, 0}$是二进制标签, 以指示像素是否属于显著对象.**为了标记和评估, 我们要求用户绘制一个矩形来指定一个显著对象. 我们的检测算法也输出一个矩形.**

图像来源. 我们收集了一个非常大的图像数据库, 其中130, 099个来自各种来源的高质量图像, 主要来自图像论坛和图像搜索引擎. 然后我们手动选择60, 000多个图像, 每个图像包含一个显著对象或一个独特的前景对象. 我们进一步选择了20, 840张图片进行标记. 在选择过程中, 我们**排除了包含非常大的显著对象的任何图像**, 从而可以更准确地评估检测的性能.

标记一致性. 对于每个要标记的图像, 我们请用户绘制一个矩形, 该矩形包围图像中最大的对象根据他/她自己的理解. 由不同用户标记的矩形通常不相同. 为了减少标签的不一致性, 我们从多个用户绘制的矩形中选择一个"真实"标签.

</details>

#### SED1/2

| Single target | Dual target | The ground truth gives the result of segmenting each image by three different human subjects |
| ------------- | ----------- | -------------------------------------------------------------------------------------------- |

* [Salient objectdetection: A benchmark](https://arxiv.org/abs/1501.02741)
* [Image Segmentation by Probabilistic Bottom-Up Aggregation and Cue Integration](http://www.wisdom.weizmann.ac.il/~meirav/Segmentation_Alpert_Galun_Brandt_Basri.pdf)
* Project: [http://www.wisdom.weizmann.ac.il/~vision/Seg_Evaluation_DB/index.html](http://www.wisdom.weizmann.ac.il/~vision/Seg_Evaluation_DB/index.html)
* Download: [http://www.wisdom.weizmann.ac.il/~vision/Seg_Evaluation_DB/dl.html](http://www.wisdom.weizmann.ac.il/~vision/Seg_Evaluation_DB/dl.html)

The purpose of this work is to provide an empirical and scientific basis for image segmentation research. Evaluating the results produced by segmentation algorithms is challenging because it is difficult to come up with canonical test sets that provide underlying real segmentations. This is partly because manually delineating segments in everyday complex images can be laborious. Furthermore, people often tend to incorporate semantic considerations into their segmentation, which is beyond the scope of data-driven segmentation algorithms. Therefore, many existing algorithms show only few segmentation results. To evaluate segmentations produced by different algorithms, we compiled a database, Currently **contains 200 grayscale images along with ground-truth annotated segmentations**. The database is specifically designed to avoid potential blurring by merging images that clearly depict one or two objects in the foreground that differ from their surroundings solely through intensity, texture, or other low-level cues. Ground-truth segmentations are obtained by asking human subjects to manually separate grayscale images (color sources are also provided) into two or three categories, where each image is segmented by three different human subjects. Segments are evaluated by evaluating their consistency with ground-truth segmentations and their amount of fragmentation. Together with this database evaluation, We provide code for evaluating a given segmentation algorithm. This way, different segmentation algorithms may have comparable results, see the "Evaluation Tests" section for more details.

<details>
<summary>中文介绍</summary>

这项工作的目的是为图像分割研究提供经验和科学依据. 评估分割算法产生的结果具有挑战性, 因为很难提出提供基础真实分割的规范测试集. 这部分是因为在日常复杂图像中手动描绘片段可能是费力的. 此外, 人们往往倾向于将语义考虑纳入其分段中, 这超出了数据驱动的分割算法的范围. 因此, 许多现有算法仅显示很少的分割结果. 为了评估由不同算法产生的分割, 我们编制了一个数据库, 目前**包含200个灰度图像以及真实标注分割**. 该数据库专门设计用于避免潜在的模糊, 仅通过仅通过强度, 纹理或其他低水平线索合并清晰描绘前景中与其周围环境不同的一个或两个物体的图像. 通过要求人类对象手动地将灰度图像(还提供颜色源)分成两个或三个类别来获得地面真实分割, 其中**每个图像由三个不同的人类对象分割**. 通过评估其与真实分割的一致性及其碎片量来评估分割. 与此数据库评估一起, 我们提供了用于评估给定分割算法的代码. 这样, 不同的分割算法可能具有可比较的结果以获得更多细节, 请参阅"评估测试"部分.

</details>

#### ASD(MSRA1000/MSRA1K)

* Paper: [A two-stage approach to saliency detection inimages](https://www.researchgate.net/publication/224312323_A_two-stage_approach_to_saliency_detection_in_images)
* *Related:
  + T. Liu, J. Sun, N.-N. Zheng, X. Tang, and H.-Y. Shum, "[Learning to detect a salient object](http://research.microsoft.com/en-us/um/people/jiansun/salientobject/salient_object.htm), " in *Proc. IEEE Conf. Comput. Vis. Pattern Recognit.*, 2007, pp.1–8.
  + R. Achanta, S. Hemami, F. Estrada, and S. Süsstrunk, "[Frequency-tuned salient region detection](http://ivrlwww.epfl.ch/supplementary_material/RK_CVPR09/), " in *Proc. IEEE Conf. Comput. Vis. Pattern Recognit.*, 2009, pp.1597–1604.
* Download: [http://download.csdn.net/detail/wanyq07/9839322](http://download.csdn.net/detail/wanyq07/9839322)
  + Note on Download: Because it is based on the MSRA image data set, after Sun Jian left, his page disappeared on MARA, and related resources could not be found. A CSDN blog shared it. The original image download address: [MSRA image data set (1000 images with real annotations)](http://download.csdn.net/detail/tuconghuan/8357509). The size of the annotation images downloaded above has been uniformly changed to 512*512. So here is an address: [ASD size is the same](http://download.csdn.net/detail/zzb4702/9559378)

ASD contains 1, 000 images with pixel-wise ground-truths. The images are selected from the MSRA-A dataset, where only the bounding boxes around salient regions are provided. The accurate salient masks in ASD are created based on object contours.

This data set contains 1000 images (MSRA1000). The database comes from the description of the database and the results of some algorithms (IT, MZ, GB, SR, AC, IG) can be found in [Frequency-tuned Salient Region Detection](http://ivrlwww.epfl.ch/supplementary_material/RK_CVPR09/index.html) (FT algorithm => The improved data set here is called ACSD, related information can be found in [ACSD](#acsd), In addition, it also contains the ground truth maps of these 1000 test images.

<details>
<summary>中文介绍</summary>

ASD 包含 1, 000 张具有像素级真实情况的图像。这些图像选自 MSRA-A 数据集，其中仅提供显著区域周围的边界框。 ASD 中准确的显著掩模是根据对象轮廓创建的。

这个数据集包含有1000张图(MSRA1000)这个数据库来自于 该数据库的说明以及一些算法(IT, MZ, GB, SR, AC, IG ) 的结果可以在Frequency-tuned Salient Region Detection (FT算法 => 这里改进的数据集叫做ACSD, 相关可见ACSD, 此外其中还包含了这1000张测试图的真值图.

</details>

#### DUT-OMRON

* Paper: C. Yang, L. Zhang, H. Lu, X. Ruan, and M.-H. Yang, "[Saliency detection via graph-based manifold ranking](http://saliencydetection.net/dut-omron/), " in *Proc. IEEE Conf. Comput. Vis. Pattern Recognit.*, 2013, pp.3166–3173.
* Project: [http://saliencydetection.net/dut-omron/#outline-container-org0e04792](http://saliencydetection.net/dut-omron/#outline-container-org0e04792)
* Download: [http://saliencydetection.net/dut-omron/download/DUT-OMRON-image.zip](http://saliencydetection.net/dut-omron/download/DUT-OMRON-image.zip)

The database consists of 5,168 high-quality images manually selected from over 140,000 images. We resized the images to be 400 pixels wide or 400 pixels high, where the other side is smaller than 400. The images in our database have one or more salient objects and relatively complex backgrounds. We had a total of 25 participants, used to aggregate ground truth, with five participant labels per image. They all had normal or corrected-to-normal vision and were aware of the goals of our experiment. We construct pixel-wise ground-truth annotations, bounding boxes, and eye-fixation ground-truth annotations for the proposed database.

Our dataset is the only one with large-scale ground-truth annotations in terms of eye fixation, bounding boxes and pixels. Compared with the ASD and MSRA datasets and some other eye fixation datasets (i.e. MIT and NUSEF datasets), the images in the dataset are more difficult and therefore more challenging and provide more room for improvement in related saliency studies.

<details>
<summary>中文介绍</summary>

数据库包括从超过140, 000张图像中手动选择的5, 168个高质量图像. 我们将图像的大小调整为宽为400或高为400像素, 其中另一条边小于400. 我们数据库的图像具有一个或多个显著对象和相对复杂的背景. 我们共有25名参与者, 用于汇总真值, 每个图像有五个参与者标签. 他们都有正常或矫正到正常的视力并且意识到我们实验的目标. 我们为提出的数据库构建像素方面的真实标注, 边界框, 和眼睛固定标注真值.

我们的数据集是唯一一个具有眼睛固定, 边界框和像素方面的大规模真实标注的数据集. 与ASD和MSRA数据集以及其他一些眼睛固定数据集(即MIT和NUSEF数据集)相比, 数据集中的图像更加困难, 因此更具挑战性, 并为相关的显著性研究提供了更多的改进空间.

</details>

#### DUTS

* Project: [http://saliencydetection.net/duts/](http://saliencydetection.net/duts/)

We contribute a large scale data set named DUTS, **containing 10, 553 training images and 5, 019 test images**. All training images are collected from the ImageNet DET training/val sets, while test images are collected from the ImageNet DET test set and the SUN data set.
Both the training and test set contain very challenging scenarios for saliency detection. Accurate pixel-level ground truths are manually annotated by 50 subjects.
To our knowledge, DUTS is currently **the largest saliency detection benchmark** with the explicit training/test evaluation protocol.
For fair comparison in the future research, the training set of DUTS serves as a good candidate for learning DNNs, while the test set and other public data sets can be used for evaluation.

<details>
<summary>中文介绍</summary>

我们贡献了一个名为 DUTS 的大规模数据集，**包含 10, 553 个训练图像和 5, 019 个测试图像**。所有训练图像均从 ImageNet DET 训练/验证集收集，而测试图像则从 ImageNet DET 测试集和 SUN 数据集收集。
训练集和测试集都包含显著性检测非常具有挑战性的场景。准确的像素级地面事实由 50 名受试者手动注释。
据我们所知，DUTS 是目前**最大的显著性检测基准**，具有明确的训练/测试评估协议。
为了在未来的研究中进行公平比较，DUTS的训练集可以作为学习DNN的良好候选，而测试集和其他公共数据集可以用于评估。

</details>

#### DUTS-MM/DUTS-MQ

* Paper:
  * [Pluralistic Salient Object Detection](https://ieeexplore.ieee.org/document/10960495)
  * [arXiv](https://arxiv.org/abs/2409.02368)
* Download: Not specified in the paper page.

Pluralistic Salient Object Detection (PSOD) is proposed for generating multiple plausible salient segmentation results for a given image, instead of forcing conventional SOD into a single-mask setting.

DUTS-MM builds upon DUTS and enriches the ground-truth mask annotations by improving mask quality, reducing annotation inconsistency, and providing multiple ground-truth masks for images with saliency ambiguity. DUTS-MQ contains about 100K image-mask pairs with human-annotated preference scores, supporting human-aligned learning and evaluation of mask quality.

<details>
<summary>中文介绍</summary>

提出了多元显著目标检测 (PSOD)，用于为给定图像生成多个合理的显著分割结果，而不是强制传统 SOD 进入单掩模设置。

DUTS-MM 基于 DUTS 构建，通过提高掩模质量、减少注释不一致以及为具有显著性模糊的图像提供多个真值掩模来丰富真值掩模注释。 DUTS-MQ 包含约 100K 个图像-掩模对，具有人工注释的偏好分数，支持人类对齐的掩模质量学习和评估。

</details>

#### SOC (Salient Objects in Clutter)


* Paper: [Salient Objects in Clutter](https://arxiv.org/abs/2105.03053)
  * Chinese Version: [https://dengpingfan.github.io/papers/[2022][TPAMI]SOC_Chinese.pdf](https://dengpingfan.github.io/papers/%5B2022%5D%5BTPAMI%5DSOC_Chinese.pdf)
* Project:
  * [https://github.com/DengPingFan/SOC-DataAug](https://github.com/DengPingFan/SOC-DataAug)
  * [https://mmcheng.net/socbenchmark/](https://mmcheng.net/socbenchmark/)
* Download: See [https://mmcheng.net/socbenchmark/](https://mmcheng.net/socbenchmark/)

We propose a new high-quality dataset and update the previous saliency benchmark. Specifically, our dataset called SOC, Salient Objects in Clutter, includes images with salient and non-salient objects from daily object categories. Beyond object category annotations, each salient image is accompanied by attributes (e.g., appearance change, clutter) that reflect common challenges in real-world scenes, and can help 1) gain a deeper insight into the SOD problem, 2) investigate the pros and cons of the SOD models, and 3) objectively assess models from different perspectives. Finally, we report attribute-based performance assessment on our SOC dataset. We believe that our dataset and results will open new directions for future research on salient object detection.

SOC has 6,000 images with 80 common categories. Half of the images contain salient objects and the others contain none.**Each salient-object-contained image is annotated with instance-level SOD ground-truth, object category (e.g., dog, book), and challenging factors** (e.g., big/small object).**The non-salient object subset has 783 texture images and 2, 217 real-scene images** (e.g., aurora, sky).

<details>
<summary>中文介绍</summary>

我们提出了一个新的高质量数据集并更新了之前的显著性基准。具体来说，我们的数据集名为 SOC（杂乱中的显著对象），包括来自日常对象类别的显著和非显著对象的图像。除了对象类别注释之外，每个显著图像都附有反映现实世界场景中常见挑战的属性（例如外观变化、杂乱），并且可以帮助 1) 更深入地了解 SOD 问题，2) 研究 SOD 模型的优缺点，以及 3) 从不同角度客观评估模型。最后，我们报告了对 SOC 数据集进行基于属性的性能评估。我们相信我们的数据集和结果将为显著目标检测的未来研究开辟新的方向。

SOC 拥有 6,000 张图像，包含 80 个常见类别。一半图像包含显著对象，其他图像不包含。**每个包含显著对象的图像都用实例级 SOD 真值、对象类别（例如狗、书）和挑战性因素**（例如大/小对象）进行注释。**非显著对象子集有 783 个纹理图像和 2, 217 个真实场景图像**（例如极光、天空）。

</details>

#### HKU-IS

* Project: [https://i.cs.hku.hk/~gbli/deep_saliency.html](https://i.cs.hku.hk/~gbli/deep_saliency.html)
* Paper: [Visual Saliency Based on Multiscale Deep Features](http://i.cs.hku.hk/~yzyu/publication/mdfsaliency-cvpr15.pdf)
* Download:
  + [Google Drive](https://drive.google.com/open?id=0BxNhBO0S5JCRQ1N6V25VeVh6cHc&authuser=0)
  + [Baidu Yun](http://pan.baidu.com/s/1c0EpNfM)

The dataset contains 4447 images with pixel annotations of salient objects.
Visual saliency is a fundamental problem in cognitive and computational sciences, including computer vision. In this paper, we find that high-quality visual saliency models can be learned from multi-scale features extracted using deep convolutional neural networks (CNN). Successful in visual recognition tasks. To learn such a saliency model, we introduce a neural network structure with fully connected layers on top of the CNN responsible for feature extraction at three different scales. We then propose an improved method to enhance the spatial consistency of our saliency results. Finally, aggregating multiple saliency maps computed for different levels of image segmentation can further improve performance, resulting in better saliency maps than those produced by a single segmentation. To facilitate further research and evaluation of visual saliency models, **we also constructed a new large database including 4447 challenging images and their pixel saliency annotations**.

<details>
<summary>中文介绍</summary>

数据集包含4447个具有显著对象的像素注释的图像
视觉显著性是包括计算机视觉在内的认知和计算科学中的一个基本问题. 在本文中, 我们发现可以从使用深度卷积神经网络(CNN)提取的多尺度特征中学习高质量的视觉显著性模型. 视觉识别任务的成功. 为了学习这样的显著性模型, 我们引入了一种神经网络结构, 它在CNN顶部具有完全连接的层, 负责三个不同尺度的特征提取. 然后, 我们提出一种改进方法来增强我们的显著性结果的空间一致性. 最后, 针对不同级别的图像分割计算的聚合多个显著性图可以进一步提高性能, 从而产生比由单个分割产生的显著性图更好的显著性图. 为了促进对视觉显著性模型的进一步研究和评估, **我们还构建了一个新的大型数据库, 包括4447个具有挑战性的图像及其像素显著性注释**.

</details>

#### SOD (Salient Object Dataset)

* Project: [http://elderlab.yorku.ca/SOD/](http://elderlab.yorku.ca/SOD/)
* Download
  + Official: [http://elderlab.yorku.ca/SOD/SOD.zip](http://elderlab.yorku.ca/SOD/SOD.zip)
  + Baidu Cloud: [https://pan.baidu.com/s/1IMElTPwD4yTo2TMSRU-keQ](https://pan.baidu.com/s/1IMElTPwD4yTo2TMSRU-keQ)

This dataset is a collection of salient object boundaries based on the Berkeley Segmentation Dataset (BSD). Seven subjects were asked to select salient objects in each image used in BSD. Each subject was randomly shown a subset of the Berkeley Segmentation Dataset as boundaries that overlapped on the corresponding image. You can then select which regions or segments correspond to salient objects by clicking on them.
For each of the 300 images used in BSD, there is a .mat file that can be opened by Matlab. Loading each mat file reads into memory a structure called "SES", which is an array of data collected from each subject's session in SOD.

💝 The original images are available from the Berkely Segmentation Dataset at: [http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/segbench/](http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/segbench/)

<details>
<summary>中文介绍</summary>

此数据集是基于Berkeley Segmentation Dataset(BSD)的显著对象边界的集合. 要求七个对象选择BSD中使用的每个图像中的显著对象. 每个主题随机显示伯克利分割数据集的子集, 作为在相应图像上重叠的边界. 然后, 可以通过单击选择哪些区域或区段对应于显著对象.
对于BSD中使用的300个图像的每个图像, 都有一个.mat文件可以由Matlab打开. 加载每个mat文件会将一个名为"SES"的结构读入内存, 该结构是从SOD中每个主题的会话中收集的数据数组.

</details>

#### Infrared

* Project: [https://ivrl.epfl.ch/research-2/research-downloads/supplementary_material-cvpr11-index-html/](https://ivrl.epfl.ch/research-2/research-downloads/supplementary_material-cvpr11-index-html/)
* Paper: [http://infoscience.epfl.ch/record/167478](http://infoscience.epfl.ch/record/167478)
* Download: [http://ivrgwww.epfl.ch/supplementary_material/cvpr11/nirscene1.zip](http://ivrgwww.epfl.ch/supplementary_material/cvpr11/nirscene1.zip)

We capture hundreds of images of color (RGB) and near-infrared (NIR) scenes using a simple modification of a conventional SLR camera. We show that the addition of near-infrared information leads to a significant improvement in performance in scene recognition tasks, and that the improvement is still greater when using an appropriate 4-dimensional color representation. In particular, we propose MSIFT - a multispectral SIFT descriptor that, when combined with a kernel-based classifier, exceeds the performance of state-of-the-art scene recognition techniques (such as GIST) and their multispectral extensions. We extensively test our algorithm using a new dataset of hundreds of RGB-NIR scene images and benchmark it on Torralba's scene classification dataset.

<details>
<summary>中文介绍</summary>

我们使用对传统SLR相机的简单修改来捕获数百个彩色(RGB)和近红外(NIR)场景的图像. 我们表明, 近红外信息的添加导致场景识别任务中的性能显著提高, 并且当使用适当的4维颜色表示时, 改进仍然更大. 特别地, 我们提出了MSIFT-一种多光谱SIFT描述符, 当与基于内核的分类器结合时, 超过了现有技术的场景识别技术(例如GIST)及其多光谱扩展的性能. 我们使用数百个RGB-NIR场景图像的新数据集对我们的算法进行了广泛的测试, 并对Torralba的场景分类数据集进行了基准测试.

</details>

#### ImgSal

* Project: [https://sites.google.com/site/jianlinudt/saliency-database](https://sites.google.com/site/jianlinudt/saliency-database)
* Author's homepage: [http://www.escience.cn/people/jianli/DataBase.html](http://www.escience.cn/people/jianli/DataBase.html)

Database features

1. A collection of 235 color images, divided into six different categories;
2. Provide human fixed records (saccade data) and human marking results;
3. Easy to use.

We will consider the detection of salient regions of different sizes simultaneously. In fact, an acceptable saliency detector should detect large and small salient regions. In addition, saliency detection should also locate salient regions in cluttered backgrounds and regions with repeated distractors. We also note that for any saliency detector, different images present different difficulties. However, existing saliency benchmarks (such as Bruce's dataset, Hou'dataset, Harel's dataset, etc.) are image collections, No attempt was made to classify the difficulty of the required analysis. Therefore, we created a new saliency benchmark for saliency model validation. This database provides REGION ground truth (human labeling) and FIXATION ground truth (via eye trackers).
Image set A database containing 235 images was collected using Google and referring to recent literature. The images in this database are 480 x 640 pixels and are divided into 6 categories: 1) 50 images with large salient areas; 2) 80 images with intermediate salient areas; 3) 60 images with small salient areas; 4) 15 images with cluttered backgrounds; 5) 15 images with repeated distractors; 6) 15 images with large and small salient areas.

<details>
<summary>中文介绍</summary>

数据库的特点

1. 235个彩色图像的集合, 分为六个不同的类别;
2. 提供人类固定记录(扫视数据)和人类标记结果;
3. 易于使用.

我们将同时考虑不同大小的显著区域的检测. 实际上, 可接受的显著性检测器应该检测大的和小的显著区域. 此外, 显著性检测还应该定位杂乱背景中的显著区域和具有重复干扰物的区域. 我们还注意到, 对于任何显著性检测器, 不同的图像呈现不同的难度. 但是, 现有的显著性基准(例如Bruce的数据集, Hou'dataset, Harel的数据集等)是图像集合, 没有尝试对所需分析的难度进行分类. 因此, 我们为显著性模型验证创建了一个新的显著性基准. 该数据库提供REGION真值(人类标记)和FIXATION真值(通过眼动仪).
图像集使用Google以及参考最近的文献收集了包含235张图像的数据库. 此数据库中的图像为480 x 640像素, 分为6类: 1)50个具有大显著区域的图像; 2)具有中间显著区域的80幅图像; 3)具有小显著区域的60幅图像; 4)背景杂乱的15幅图像; 5)带有重复干扰物的15张图像; 6)具有大和小显著区域的15个图像.

</details>

#### ECSSD/CSSD

* Download: [http://www.cse.cuhk.edu.hk/leojia/projects/hsaliency/dataset.html](http://www.cse.cuhk.edu.hk/leojia/projects/hsaliency/dataset.html)
  + ECSSD (1000 images)
    - [ECSSD images (64.6MB)](http://www.cse.cuhk.edu.hk/leojia/projects/hsaliency/data/ECSSD/images.zip)
    - [ECSSD ground truth masks (1.78MB)](http://www.cse.cuhk.edu.hk/leojia/projects/hsaliency/data/ECSSD/ground_truth_mask.zip) (Updated on 9 April, 2015)
  + CSSD (200 images)
    - [CSSD images (18.7MB)](http://www.cse.cuhk.edu.hk/leojia/projects/hsaliency/data/CSSD/images.zip)
    - [CSSD groud truth masks (0.75MB)](http://www.cse.cuhk.edu.hk/leojia/projects/hsaliency/data/CSSD/ground_truth_mask.zip)

CSSD contains 200 images, while ECSSD is an extension of the former and contains 1,000 images.

Although MSRA-1000 has a wide variety of image content, the background structure is mainly simple and smooth. To represent the situations into which natural images typically fall, we extended the Complex Scene Saliency Dataset (CSSD) to a larger dataset (ECSSD) containing 1000 images, which contains many semantically meaningful but structurally complex images for evaluation. The images were obtained from the Internet and 5 assistants were asked to make ground truth masks. Several examples with corresponding masks are shown above.

<details>
<summary>中文介绍</summary>

其中CSSD包含了200张图, 而ECSSD是前者的扩展集包含有1000张图

虽然MSRA-1000的图像内容种类繁多, 但背景结构主要是简单而流畅. 为了表示自然图像通常落入的情况, 我们将复杂场景显著性数据集(CSSD)扩展到包含1000个图像的更大数据集(ECSSD), 其中包含许多语义上有意义但结构复杂的图像用于评估. 这些图像是从互联网上获取的, 并要求5名助手制作地面真相面具. 上面显示了几个带有相应掩模的例子.

</details>

#### THUR15K

* Paper: [https://mmcheng.net/zh/gsal/](https://mmcheng.net/zh/gsal/)
* Download: [https://mmcheng.net/mftp/Data/THUR15000.zip](https://mmcheng.net/mftp/Data/THUR15000.zip)
  + Baidu Cloud: [https://pan.baidu.com/s/1u-E-8ujnxBz0mdmXsJglvg](https://pan.baidu.com/s/1u-E-8ujnxBz0mdmXsJglvg)

Efficient identification of salient objects in large image sets is essential for many applications, including image retrieval, surveillance, image annotation, and object recognition. We propose a simple, fast, and efficient algorithm to locate and segment salient objects by analyzing collections of images. As a key novelty, we introduce population saliency to achieve superior unsupervised salient object segmentation by extracting salient objects that maximize inter-image similarity and intra-image sharpness (in a collection of pre-filtered images). To evaluate our method, We constructed a large benchmark dataset containing 15K images across multiple categories with over 6000 pixel-accurate ground-truth annotations for salient object regions. In all our tests, group saliency consistently outperformed state-of-the-art single-image saliency algorithms, resulting in higher accuracy and better recall. Our algorithm successfully processed image collections of a larger order than any existing benchmark dataset, including a variety of heterogeneous images from various inter-network sources.
We introduce a labeled dataset of categorical images for evaluating sketch-based image retrieval. We downloaded approximately 3000 images for each of 5 keywords: "butterfly", "coffee cup", "dog jumping", "giraffe" and "plane", together including approximately 15000 images. ** For each image, if there is a non-blurred object with the correct content matching the query keyword and a large part of the object is visible, we label such an object region. Similar to MSRA10K, Salient regions are labeled at the pixel level. We only label salient object regions for objects that are almost fully visible, since partially occluded objects are less useful for shape matching. Unlike MSRA10K, the THUR15K dataset does not contain salient regions labeled for every image in the dataset, i.e., some images may not have any salient regions. This dataset is used to evaluate shape-based image retrieval performance.**

<details>
<summary>中文介绍</summary>

有效识别大型图像集中的显著对象对于许多应用是必不可少的, 包括图像检索, 监视, 图像注释和对象识别. 我们提出了一种简单, 快速, 有效的算法, 通过分析图像集合来定位和分割显著对象. 作为一个关键的新颖性, 我们通过提取最大化图像间相似性和图像内清晰度的显著对象(在预过滤图像的集合中)来引入群体显著性以实现优越的无监督显著对象分割. 为了评估我们的方法, 我们构建了一个大型基准数据集, **该数据集包含多个类别的15K图像, 适用于显著对象区域的6000多个像素精确的真值注释**. 在我们的所有测试中, group saliency 始终优于最先进的单图像显著性算法, 从而实现更高的精度和更好的回忆. 我们的算法成功处理了比任何现有基准数据集更大的订单的图像集合, 包括来自各种网络间源的各种异构图像.
我们引入了分类图像的标记数据集, 用于评估基于草图的图像检索. 我们为5个关键字中的每一个Download了大约3000张图像:"蝴蝶", "咖啡杯", "狗跳", "长颈鹿"和"平面", 一起包括大约15000张图像.**对于每个图像, 如果存在具有与查询关键字匹配的正确内容的非模糊对象并且对象的大部分可见, 则我们标记这样的对象区域. 与MSRA10K类似, 显著区域以像素级别标记. 我们只标记几乎完全可见的对象的显著对象区域, 因为部分遮挡的对象对形状匹配不太有用. 与MSRA10K不同, THUR15K数据集不包含为数据集中的每个图像标记的显著区域, 即, 一些图像可能没有任何显著区域. 该数据集用于评估基于形状的图像检索性能.**

</details>

#### Bruce-A

* Paper: [https://papers.nips.cc/paper/2830-saliency-based-on-information-maximization.pdf](https://papers.nips.cc/paper/2830-saliency-based-on-information-maximization.pdf)

#### Judd-A

* Paper: [http://people.csail.mit.edu/torralba/publications/wherepeoplelook.pdf](http://people.csail.mit.edu/torralba/publications/wherepeoplelook.pdf)

#### PASCAL-S

* Project:
  + [https://ccvl.jhu.edu/datasets/](https://ccvl.jhu.edu/datasets/)
  + [http://www.cbi.gatech.edu/salobj/](http://www.cbi.gatech.edu/salobj/)
* Download:
  + Baidu Yun: [https://pan.baidu.com/s/1DZcfwCYdeMW4EGawhXQyig](https://pan.baidu.com/s/1DZcfwCYdeMW4EGawhXQyig)
  + Page: [http://academictorrents.com/details/6c49defd6f0e417c039637475cde638d1363037e](http://academictorrents.com/details/6c49defd6f0e417c039637475cde638d1363037e)

Free inpainting on a subset of 850 images from PASCAL VOC. Collected with 8 subjects, 3s viewing time, Eyelink II eye tracker. Performance of most algorithms shows that PASCAL-S is less biased than most saliency datasets.

💔 Since its annotated true value has multiple values, a common practice is to use the `255/2` value as the threshold for processing before using this data set

<details>
<summary>中文介绍</summary>

对来自PASCAL VOC的850张图像子集的自由修复. 收集8个主题, 3s观看时间, Eyelink II眼动仪. 大多数算法的性能表明PASCAL-S比大多数显著性数据集偏差更小.

💔 由于其标注的真值有多个值, 常见的做法是使用 `255/2` 值作为阈值进行处理后, 再使用该数据集

</details>

#### UCSB

* Paper: [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3954044/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3954044/)
* Download: [https://labs.psych.ucsb.edu/eckstein/miguel/research_pages/saliencydata.html](https://labs.psych.ucsb.edu/eckstein/miguel/research_pages/saliencydata.html)

#### OSIE

* Paper: [https://jov.arvojournals.org/article.aspx?articleid=2193943](https://jov.arvojournals.org/article.aspx?articleid=2193943)

A large number of previous models are used to predict people's appearance in natural scenes, focusing on pixel-level image attributes. To bridge the semantic gap between the predictive power of computational saliency models and human behavior, we propose a new saliency architecture that divides information into three levels: pixel-level image attributes, object-level attributes, and semantic-level attributes. Object and semantic-level information are usually ignored, or only a few sample object categories are discussed, where scaling to a large number of object categories is not feasible nor neurally justified. To solve this problem, This work builds a principled vocabulary of basic properties to describe object and semantic-level information, thereby not restricting a limited number of object categories. We build a new dataset of 500 images containing eye-tracking data from 15 observers and annotation data for 5,551 segmented objects with fine outlines and 12 semantic attributes (publicly available in the paper). The experimental results demonstrate the importance of object- and semantic-level information in predicting visual attention.

<details>
<summary>中文介绍</summary>

大量先前的模型用于预测人们在自然场景中的外观, 侧重于像素级图像属性. 为了弥合计算显著性模型的预测能力与人类行为之间的语义差距, 我们提出了一种新的显著性体系结构, 它将信息分为三个层次: 像素级图像属性, 对象级属性和语义级属性. 通常忽略对象和语义级别信息, 或者仅讨论少数样本对象类别, 其中缩放到大量对象类别是不可行的, 也不是神经合理的. 为了解决这个问题, 这项工作构建了一个基本属性的原则词汇表来描述对象和语义级信息, 从而不限制有限数量的对象类别. 我们**建立了一个包含500个图像的新数据集, 其中包含15个观察者的眼动追踪数据和5, 551个具有精细轮廓和12个语义属性的分段对象的注释数据**(可在论文中公开获得). 实验结果证明了对象和语义级信息在预测视觉注意力方面的重要性.

</details>

#### ACSD

* Paper: [Frequency-tuned salient region detection](https://infoscience.epfl.ch/record/135217/files/1708.pdf)
* Project: [https://ivrl.epfl.ch/research-2/research-current/research-saliency/supplementary_material-rk_cvpr09-index-html/](https://ivrl.epfl.ch/research-2/research-current/research-saliency/supplementary_material-rk_cvpr09-index-html/)
* Download: [Only GT](https://ivrl.epfl.ch/wp-content/uploads/2018/08/binarymasks.zip)

Made based on the ASD data set (MSRA1K).
We obtained a real database from 1000 images proposed in [Z. Wang and B. Li. A two-stage approach to saliency detection in images. ICASSP 2008.]. The ground truth in [Z. Wang and B. Li. We manually segment salient objects within user-drawn rectangles to obtain binary masks as shown below. Such masks are both accurate and allow us to handle multiple salient objects clearly.

<details>
<summary>中文介绍</summary>

基于ASD数据集(MSRA1K)制作.
我们从[Z. Wang and B. Li. A two-stage approach to saliency detection in images. ICASSP 2008.]中提出的1000个图像中获得了一个真实数据库. [Z. Wang and B. Li. A two-stage approach to saliency detection in images. ICASSP 2008.]中的基本事实是在显著区域周围的用户绘制的矩形. 这是不准确的, 并将多个对象合二为一. 我们手动分割用户绘制的矩形内的显著对象以获得二进制掩码, 如下所示. 这样的掩膜既准确又允许我们清楚地处理多个显著对象.

</details>

#### WXSOD

* Paper: [WXSOD: A Benchmark for Robust Salient Object Detection in Adverse Weather Conditions](https://arxiv.org/abs/2508.12250)
* Project: [https://github.com/C-water/WXSOD](https://github.com/C-water/WXSOD)
* Download: [https://github.com/C-water/WXSOD?tab=readme-ov-file#--dataset-access](https://github.com/C-water/WXSOD?tab=readme-ov-file#--dataset-access)

WXSOD dataset provides a large-scale dataset (14,945 RGB images) for salient object detection under extreme weather conditions. Distinguishing itself from existing RGB-SOD benchmarks, it provides images with ​​diverse degradation​​ patterns and ​​pixel-wise annotations​​. Our dataset contains:
- A synthetic training set consisting of 12,891 images, including 8 types of weather noise and a small amount of clean images.
- A composite test set consisting of 1,500 images, including 8 types of weather noise and a small amount of clean images.
- A real test set consisting of 554 images, including 5 types of weather noise.

<details>
<summary>中文介绍</summary>

WXSOD数据集提供了大规模数据集（14,945张RGB图像），用于极端天气条件下的显著目标检测。与现有的 RGB-SOD 基准不同，它为图像提供了多种退化模式和像素级注释。我们的数据集包含：
- 由 12,891 张图像组成的合成训练集，其中包括 8 种天气噪声和少量干净图像。
- 由 1,500 张图像组成的复合测试集，其中包括 8 种天气噪声和少量干净图像。
- 由 554 张图像组成的真实测试集，其中包括 5 种天气噪声。

</details>

### RGB-D Saliency

Thanks:

* @JXingZhao: [https://github.com/JXingZhao/ContrastPrior](https://github.com/JXingZhao/ContrastPrior)
* @jiwei0921: [https://github.com/jiwei0921/RGBD-SOD-datasets](https://github.com/jiwei0921/RGBD-SOD-datasets)
* More Details can be found at: [http://dpfan.net/d3netbenchmark/](http://dpfan.net/d3netbenchmark/)

#### SIP

* Paper: Rethinking RGB-D Salient Object Detection: Models, Datasets, and Large-Scale Benchmarks:https://arxiv.org/pdf/1907.06781.pdf
* Project: [http://dpfan.net/d3netbenchmark/](http://dpfan.net/d3netbenchmark/)
* Download: See [http://dpfan.net/d3netbenchmark/](http://dpfan.net/d3netbenchmark/)

We carefully collect a new salient person (SIP) dataset, which consists of 1K high-resolution images that cover diverse real-world scenes from various viewpoints, poses, occlusion, illumination, and background.

<details>
<summary>中文介绍</summary>

我们仔细收集了一个新的显著人物（SIP）数据集，该数据集由 1K 高分辨率图像组成，涵盖了来自不同视点、姿势、遮挡、照明和背景的不同现实世界场景。

</details>

#### NLPR/RGBD1000

* Paper: [Rgbd salient object detection: a benchmark and algorithms](https://docs.google.com/uc?authuser=0&id=0B1wzzt1_uP1rb250d0t6dVFXWG8&export=download)
* Project: [https://sites.google.com/site/rgbdsaliency/home](https://sites.google.com/site/rgbdsaliency/home)
* Download: [https://sites.google.com/site/rgbdsaliency/dataset](https://sites.google.com/site/rgbdsaliency/dataset)

NLPR is also called RGBD1000 dataset which including 1,000 images. There may exist multiple salient objects in each image. The structured light depth images are obtained by the Microsoft Kinect under different illumination conditions.

<details>
<summary>中文介绍</summary>

NLPR 也称为 RGBD1000 数据集，包含 1,000 张图像。每幅图像中可能存在多个显著物体。结构光深度图像是通过Microsoft Kinect在不同光照条件下获得的。

</details>

#### NJU400/2000

* Paper:

  + NJU400: [Depth saliency based on anisotropic center-surround difference](http://mcg.nju.edu.cn/publication/2014/icip14-jur.pdf)
  + NJU2000: [Depth-aware salient object detection using anisotropic center-surround difference](http://mcg.nju.edu.cn/publication/2015/spic15-jur.pdf)
* Project:

  * [MGG](http://mcg.nju.edu.cn/index.html)
  * [http://mcg.nju.edu.cn/publication/2014/icip14-jur/index.html](http://mcg.nju.edu.cn/publication/2014/icip14-jur/index.html)
* Download:

  * Official:
    + [http://mcg.nju.edu.cn/resource.html](http://mcg.nju.edu.cn/resource.html)
    + [http://mcg.nju.edu.cn/dataset/nju400.zip](http://mcg.nju.edu.cn/dataset/nju400.zip)
    + [http://mcg.nju.edu.cn/dataset/nju2000.zip](http://mcg.nju.edu.cn/dataset/nju2000.zip)

  + See [http://dpfan.net/d3netbenchmark/](http://dpfan.net/d3netbenchmark/)

NJU2000 contains 2003 stereo image pairs with diverse objects and complex, challenging scenarios, along with ground-truth map. The stereo images are gathered from 3D movies, the Internet, and photographs taken by a Fuji W3 stereo camera.

<details>
<summary>中文介绍</summary>

NJU2000 包含 2003 个立体图像对，其中包含不同的对象和复杂且具有挑战性的场景，以及真值地图。立体图像是从 3D 电影、互联网以及 Fuji W3 立体相机拍摄的照片中收集的。

</details>

#### STEREO/SSB

* Paper: [Leveraging stereopsis for saliency analysis](http://web.cecs.pdx.edu/~fliu/papers/cvpr2012.pdf)
* Project: [http://web.cecs.pdx.edu/~fliu/](http://web.cecs.pdx.edu/~fliu/)
* Download: See [http://dpfan.net/d3netbenchmark/](http://dpfan.net/d3netbenchmark/)

SSB is also called STEREO dataset, which consists of 1000 pairs of binocular images.

<details>
<summary>中文介绍</summary>

SSB也称为STEREO数据集，由1000对双目图像组成。

</details>

#### LFSD

* Paper: [Saliency Detection on Light Field](https://ieeexplore.ieee.org/document/7570181)
* Project: [https://sites.duke.edu/nianyi/publication/saliency-detection-on-light-field/](https://sites.duke.edu/nianyi/publication/saliency-detection-on-light-field/)
* Download:
  * Official: See [https://sites.duke.edu/nianyi/publication/saliency-detection-on-light-field/](https://sites.duke.edu/nianyi/publication/saliency-detection-on-light-field/)
  * See [http://dpfan.net/d3netbenchmark/](http://dpfan.net/d3netbenchmark/)

We acquire 100 light fields using the Lytro light field camera. For each light field, we provide: (a) Raw light field data, (b) A rough focal stack  (c) An all-focus image deriving from focal stack  (d) The ground truth corresponding to all-focus image.

To get a valid ground-truth, we ask three individuals to manually segment the saliency regions from the all-focus image. The result are deemed ground truth only when all three results are consistent (i.e., they have an overlap of over 90%)

<details>
<summary>中文介绍</summary>

我们使用 Lytro 光场相机获取 100 个光场。对于每个光场，我们提供：（a）原始光​​场数据，（b）粗略的焦点堆栈（c）从焦点堆栈导出的全焦点图像（d）与全焦点图像相对应的真值。

为了获得有效的基本事实，我们要求三个人从全焦点图像中手动分割显著区域。仅当所有三个结果一致（即它们重叠超过 90%）时，结果才被视为真实结果

</details>

#### RGBD135/DES

* Paper: [Depth Enhanced Saliency Detection Method](https://dl.acm.org/doi/pdf/10.1145/2632856.2632866)
* Project: [https://github.com/HzFu/DES_code](https://github.com/HzFu/DES_code)
* Download:
  * Official:
    + Baidu Pan: [https://pan.baidu.com/s/1pLv2B8n](https://pan.baidu.com/s/1pLv2B8n)
    + Google Drive: [https://onedrive.live.com/redir?resid=F3A8A31ABFAC51B0!256&amp;authkey=!AC4-yOEjn0bgrCQ&amp;ithint=file%2crar](https://onedrive.live.com/redir?resid=F3A8A31ABFAC51B0!256&authkey=!AC4-yOEjn0bgrCQ&ithint=file%2Crar)
  + See [http://dpfan.net/d3netbenchmark/](http://dpfan.net/d3netbenchmark/)

In our experiments, we provide a new RGB-D saliency detection dataset. We take 135 RGB-D indoor images by Kinect with the resolution 640×480. Then, three users are asked to mark the salient object of each image. We employ the overlapping areas of the manually labelled object as the ground truth.

<details>
<summary>中文介绍</summary>

在我们的实验中，我们提供了一个新的 RGB-D 显著性检测数据集。我们通过Kinect拍摄了135张RGB-D室内图像，分辨率为640×480。然后，要求三名用户标记每张图像的显著对象。我们使用手动标记对象的重叠区域作为基本事实。

</details>

#### DUT-RGBD/DUTLF-Depth

* Paper: [Depth-induced Multi-scale Recurrent Attention Network for Saliency Detection](https://openaccess.thecvf.com/content_ICCV_2019/papers/Piao_Depth-Induced_Multi-Scale_Recurrent_Attention_Network_for_Saliency_Detection_ICCV_2019_paper.pdf)
* Project: [https://github.com/jiwei0921/DMRA_RGBD-SOD](https://github.com/jiwei0921/DMRA_RGBD-SOD)
* Download:
  * Official: [https://pan.baidu.com/s/1FwUFmNBox_gMZ0CVjby2dg](https://pan.baidu.com/s/1FwUFmNBox_gMZ0CVjby2dg)
  * See [http://dpfan.net/d3netbenchmark/](http://dpfan.net/d3netbenchmark/)

The dataset is part of DUTLF dataset captured by Lytro camera, and we selected a more accurate 1200 depth map pairs for more accurate RGB-D saliency detection.
We create a large scale RGB-D dataset(DUTLF-Depth) with 1200 paired images containing more complex scenarios, such as multiple or transparent objects, similar foreground and background, complex background, low-intensity environment. This challenging dataset can contribute to comprehensively evaluating saliency models.
And we split the dataset including 800 training set and 400 test set.

<details>
<summary>中文介绍</summary>

该数据集是Lytro相机捕获的DUTLF数据集的一部分，我们选择了更准确的1200个深度图对来进行更准确的RGB-D显著性检测。
我们创建了一个大规模 RGB-D 数据集（DUTLF-Depth），其中包含 1200 张配对图像，其中包含更复杂的场景，例如多个或透明物体、相似的前景和背景、复杂的背景、低强度环境。这个具有挑战性的数据集有助于全面评估显著性模型。
我们将数据集分为 800 个训练集和 400 个测试集。

</details>

#### SSD/SSD100

* Paper: [A Three-Pathway Psychobiological Framework of Salient Object Detection Using Stereoscopic Technology](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8265566)
* Download: See [http://dpfan.net/d3netbenchmark/](http://dpfan.net/d3netbenchmark/)

Our SSD100 dataset is built on three stereo movies. The movies contain both the indoors and outdoors scenes. We pick up one stereo image pair at each hundred frames. It totally has tens of thousands of stereo image pairs. We make the image acquisition and image annotation independent to each other, we can avoid dataset design bias, namely a specific type of bias that is caused by experimenters unnatural selection of dataset images. The chosen stereo image pairs are based on one principle: choose the one which the computer detect the salient objects within the complex scenes where even the human cannot tell the salient objects at once. After picking up the stereo image pairs, we divide the image pairs into left images and right images both in 960x1080 size. When we build the ground truth of salient objects, we adhere to the following rules: 1) we mark the salient objects, taking the advice of most people; 2) disconnected regions of the same object are labeled separately; 3) we use solid regions to approximate hollow objects, such as bike wheels. Besides, we will expand this dataset continually in future.

<details>
<summary>中文介绍</summary>

我们的 SSD100 数据集基于三部立体电影构建。电影包含室内和室外场景。我们每一百帧拾取一对立体图像。它总共有数万个立体图像对。我们使图像采集和图像注释彼此独立，我们可以避免数据集设计偏差，即由于实验者对数据集图像的不自然选择而引起的特定类型的偏差。所选择的立体图像对基于一个原则：选择计算机在复杂场景中检测到显著对象的一对，即使人类也无法立即分辨出显著对象。拾取立体图像对后，我们将图像对分为左图像和右图像，尺寸均为 960x1080。当我们构建显著对象的基本事实时，我们遵循以下规则：1）我们标记显著对象，听取大多数人的建议； 2）同一物体的不相连区域分别标记； 3）我们使用实心区域来近似空心物体，例如自行车车轮。此外，我们将在未来不断扩展这个数据集。

</details>

#### ReDWeb-S

* Paper: [SMAC: Learning Selective Mutual Attention and Contrast for RGB-D Saliency Detection](https://arxiv.org/abs/2010.05537)
* Download: See [https://github.com/nnizhang/SMAC#redweb-s](https://github.com/nnizhang/SMAC#redweb-s)
* Project: [https://github.com/nnizhang/SMAC](https://github.com/nnizhang/SMAC)

We construct a new large-scale challenging dataset ReDWeb-S and it has totally 3179 images with various real-world scenes and high-quality depth maps. We split the dataset into a training set with 2179 RGB-D image pairs and a testing set with the remaining 1000 image pairs.

<details>
<summary>中文介绍</summary>

我们构建了一个新的大规模具有挑战性的数据集ReDWeb-S，它总共有3179张图像，具有各种真实世界场景和高质量的深度图。我们将数据集分为包含 2179 个 RGB-D 图像对的训练集和包含剩余 1000 个图像对的测试集。

</details>

#### COME15K

* Paper: [Cascaded RGB-D SOD with COME15K dataset](https://arxiv.org/abs/2109.07246)
* Download: See [https://github.com/JingZhang617/cascaded_rgbd_sod#come15k-rgb-d-sod-dataset](https://github.com/JingZhang617/cascaded_rgbd_sod#come15k-rgb-d-sod-dataset)
* Project: [https://github.com/JingZhang617/cascaded_rgbd_sod](https://github.com/JingZhang617/cascaded_rgbd_sod)

Our new COME15K dataset is based on Holo50K, which is a stereo dataset, including scenarios from both indoor and outdoor. We first filter the Holo50K dataset and then obtain 16,000 stereo image pairs for labelling (the candidate labeled set) and another 5,000 image pairs as the unlabeled set. Note that the stereo pairs in Holo50K dataset are directly captured by a stereo camera without rectification, we use a modified version of a SOTA off-the-shelf stereo matching algorithm to compute the depth for both the candidate labeled set and unlabeled set with the left-right view images as input.

<details>
<summary>中文介绍</summary>

我们新的 COME15K 数据集基于 Holo50K，这是一个立体数据集，包括室内和室外的场景。我们首先对 Holo50K 数据集进行过滤，然后获得 16,000 个立体图像对进行标记（候选标记集），另外 5,000 个图像对作为未标记集。请注意，Holo50K 数据集中的立体对是由立体相机直接捕获的，无需进行校正，我们使用 SOTA 现成立体匹配算法的修改版本来计算候选标记集和未标记集的深度，并以左右视图图像作为输入。

</details>

### RGB-T Saliency

#### VT-IMAG

* Paper: [Divide-and-Conquer: Confluent Triple-Flow Network for RGB-T Salient Object Detection](https://arxiv.org/abs/2412.01556)
* Download: [Google Drive](https://drive.google.com/drive/folders/19hoSOwss0usTPOmT8pCv50-T-kbV-YkL?usp=sharing)
* Project: <https://cser-tang-hao.github.io/contrinet.html>
* Code: <https://github.com/CSer-Tang-hao/ConTriNet_RGBT-SOD>

VT-IMAG contains **536 aligned RGB-thermal image pairs with pixel-wise saliency masks**, curated from RGB-T semantic segmentation and object detection datasets for autonomous driving. It covers daytime and nighttime scenes, including vehicles, pedestrians, and roadblocks. Seven challenging attributes are annotated: thermal crossover, image clutter, out of focus, rainy day, foggy day, strong noise, and similar appearance. The benchmark evaluates zero-shot robustness: models are trained on the VT5000 training set and tested on VT-IMAG.

<details>
<summary>中文介绍</summary>

VT-IMAG 包含 **536 对空间对齐的 RGB-热红外图像及像素级显著性掩码**，从自动驾驶领域的 RGB-T 语义分割和目标检测数据集中筛选构建。数据集涵盖白天和夜间场景，包含车辆、行人和路障等目标，并标注了七种挑战属性：热交叉、图像杂乱、失焦、雨天、雾天、强噪声和外观相似。该基准用于评估零样本鲁棒性：模型在 VT5000 训练集上训练，在 VT-IMAG 上测试。

</details>

#### UVT2000

* Paper: [TMM 2024 | Alignment-Free RGBT Salient Object Detection: Semantics-guided Asymmetric Correlation Network and A Unified Benchmark](https://arxiv.org/pdf/2406.00917)
* Download: See <https://github.com/Angknpng/SACNet?tab=readme-ov-file#uvt2000>.
* Project: <https://github.com/Angknpng/SACNet>

UVT2000 contains 2000 unaligned visible-thermal image pairs with ground truth annotations, directly captured by a pair of thermal infrared and CCD cameras without any alignment. Therefore, the misalignment of the image pairs is a natural result of camera shooting and reflects the issues in practical applications. Additionally, the image pairs are collected from a variety of real-world scenarios, which are  annotated with 11 challenge attributes to facilitate the study of specific issues.

<details>
<summary>中文介绍</summary>

UVT2000 包含 2000 个未对齐的可见热图像对，带有真值注释，由一对热红外和 CCD 相机直接捕获，无需任何对齐。因此，图像对的错位是相机拍摄的自然结果，反映了实际应用中的问题。此外，图像对是从各种现实场景中收集的，并注释有 11 个挑战属性，以方便对特定问题的研究。

</details>

#### un-VT821/1000/5000

* Paper: [TIP 2022 | Weakly Alignment-Free RGBT Salient Object Detection With Deep Correlation Network](https://ieeexplore.ieee.org/document/9779787)
* Download: <https://github.com/lz118/Deep-Correlation-Network?tab=readme-ov-file#unaligned-dataset>
* Project: <https://github.com/lz118/Deep-Correlation-Network>

We use the training set of VT5000 to train our network and compare the performances on VT821, VT1000 and VT5000’s testing set. For proving our performance on unaligned image pairs, we randomly make the spatial affine transformation on all the testing data.

<details>
<summary>中文介绍</summary>

我们使用 VT5000 的训练集来训练我们的网络，并比较 VT821、VT1000 和 VT5000 测试集上的性能。为了证明我们在未对齐图像对上的性能，我们对所有测试数据随机进行空间仿射变换。

</details>

#### VT723

* Paper: [Mirror Complementary Transformer Network for RGB-thermal Salient Object Detection](https://arxiv.org/abs/2207.03558)
* Download: See [https://github.com/jxr326/SwinMCNet#the-proposed-dataset](https://github.com/jxr326/SwinMCNet#the-proposed-dataset)
* Project: [https://github.com/jxr326/SwinMCNet](https://github.com/jxr326/SwinMCNet)

To further validate the robustness of the proposed model under common challenging scenes in real world, we build a more challenging RGB-T SOD dataset VT723 based on a large public semantic segmentation RGB-T dataset used in the autonomous driving domain. We pick image pairs in which the salient objects are significant in at least one of their color and thermal modalities. After careful screening, we collectd 723 sets of RGB-thermal image pairs in which 473 are taken during daytime and 250 are taken at night. The SOD ground truths are obtained by professional annotators looking at both modalities, selecting common salient regions, and manually marking pixel by pixel on the original segmentation ground truths.

<details>
<summary>中文介绍</summary>

为了进一步验证所提出的模型在现实世界中常见的挑战性场景下的鲁棒性，我们基于自动驾驶领域使用的大型公共语义分割RGB-T数据集构建了更具挑战性的RGB-T SOD数据集VT723。我们选择图像对，其中显著物体至少在其颜色和热模态之一上具有重要意义。经过仔细筛选，我们收集了723组RGB热图像对，其中473组是白天拍摄的，250组是夜间拍摄的。 SOD 基本事实是由专业注释者通过查看两种模式、选择共同显著区域并在原始分割基本事实上手动逐像素标记来获得的。

</details>

#### VT5000

* Paper: [RGBT Salient Object Detection: A Large-scale Dataset and Benchmark](https://arxiv.org/pdf/2007.03262.pdf)
* Project:
  * [http://chenglongli.cn/code-dataset/](http://chenglongli.cn/code-dataset/)
  * [https://github.com/lz118/RGBT-Salient-Object-Detection](https://github.com/lz118/RGBT-Salient-Object-Detection)
* Download: [https://pan.baidu.com/s/13_9tJXHDmWLNjqkbMNl1hw](https://pan.baidu.com/s/13_9tJXHDmWLNjqkbMNl1hw) (likp)

This work contributes such a RGBT image dataset named VT5000, including 5000 spatially aligned RGBT image pairs with ground truth annotations. VT5000 has 11 challenges collected in different scenes and environments for exploring the robustness of algorithms. With this dataset, we propose a powerful baseline approach, which extracts multi-level features within each modality and aggregates these features of all modalities with the attention mechanism, for accurate RGBT salient object detection.

<details>
<summary>中文介绍</summary>

这项工作贡献了一个名为 VT5000 的 RGBT 图像数据集，其中包括 5000 个空间对齐的 RGBT 图像对，并带有真实注释。 VT5000收集了11个不同场景和环境下的挑战，用于探索算法的鲁棒性。借助该数据集，我们提出了一种强大的基线方法，该方法提取每种模态中的多级特征，并通过注意力机制聚合所有模态的这些特征，以实现准确的 RGBT 显著对象检测。

</details>

#### VT1000

* Paper: [RGB-T Image Saliency Detection via Collaborative Graph Learning](https://ieeexplore.ieee.org/document/8744296)
* Project: [http://chenglongli.cn/code-dataset/](http://chenglongli.cn/code-dataset/)
* Download:
  + Baidu Pan: [https://pan.baidu.com/s/1eGQJhvnKnqV1KJ1GY_63NA](https://pan.baidu.com/s/1eGQJhvnKnqV1KJ1GY_63NA)
  + Google Drive: [https://drive.google.com/file/d/1NCPFNeiy1n6uY74L0FDInN27p6N_VCSd/view?usp=sharing](https://drive.google.com/file/d/1NCPFNeiy1n6uY74L0FDInN27p6N_VCSd/view?usp=sharing)

Existing RGB-T image benchmark dataset for saliency detection has several limitations: i) The alignment errors might be large. The used RGB and thermal cameras have totally different imaging parameters and are mounted on tripods, and they use a homography matrix to approximate the transformations of two images. ii) The aligned method introduces blank boundaries in some modality, which might destroy the boundary prior to some extent. iii) Most of scenes are very simple, which makes the dataset less challenge and diverse. In this paper, we contribute a larger dataset for the purpose of RGB-T image saliency detection. The imaging hardware includes highly aligned RGB and thermal cameras, and the  transformation between two modal images are thus only translation and scale. This setup makes the images of different modalities highly aligned, and have no blank boundaries. Furthermore, we take more challenges and diversities into account when building up the dataset and collect 1000 RGB-T image pairs

<details>
<summary>中文介绍</summary>

现有的用于显著性检测的 RGB-T 图像基准数据集有几个限制： i) 对齐误差可能很大。所使用的RGB和热成像相机具有完全不同的成像参数，并且安装在三脚架上，并且它们使用单​​应矩阵来近似两个图像的变换。 ii）对齐方法在某些模态中引入了空白边界，这可能会在一定程度上破坏先前的边界。 iii）大多数场景都非常简单，这使得数据集的挑战性和多样性较低。在本文中，我们贡献了一个更大的数据集用于 RGB-T 图像显著性检测。成像硬件包括高度对齐的 RGB 和热成像相机，因此两个模态图像之间的转换只是平移和缩放。这种设置使不同模态的图像高度对齐，并且没有空白边界。此外，我们在构建数据集时考虑了更多的挑战和多样性，并收集了 1000 个 RGB-T 图像对

</details>

#### VT821

* Paper: [A Unified RGB-T Saliency Detection Benchmark: Dataset, Baselines, Analysis and A Novel Approach](https://arxiv.org/pdf/1701.02829.pdf)
* Project: [http://chenglongli.cn/code-dataset/](http://chenglongli.cn/code-dataset/)
* Download:
  + Baidu Pan: [http://pan.baidu.com/s/1bpEaeQV](http://pan.baidu.com/s/1bpEaeQV)
  + Google Drive: [https://drive.google.com/file/d/0B4fH4G1f-jjNR3NtQUkwWjFFREk/view?usp=sharing](https://drive.google.com/file/d/0B4fH4G1f-jjNR3NtQUkwWjFFREk/view?usp=sharing)

This work contributes such a RGB-T image dataset, which includes 821 spatially aligned RGB-T image pairs and their ground truth annotations for saliency detection purpose. The image pairs are with high diversity recorded under different scenes and environmental conditions, and we annotate 11 challenges on these image pairs for performing the challengesensitive analysis for different saliency detection algorithms.

<details>
<summary>中文介绍</summary>

这项工作贡献了这样一个 RGB-T 图像数据集，其中包括 821 个空间对齐的 RGB-T 图像对及其用于显著性检测目的的真值注释。在不同场景和环境条件下记录的图像对具有高度多样性，我们在这些图像对上注释了 11 个挑战，以便对不同的显著性检测算法进行挑战敏感分析。

</details>

### Underwater Salient Object Detection

#### USOD

* Paper: [SVAM: Saliency-guided Visual Attention Modeling by Autonomous Underwater Robots](https://arxiv.org/abs/2011.06252)
* Project: [http://irvlab.cs.umn.edu/visual-attention-modeling/svam](http://irvlab.cs.umn.edu/visual-attention-modeling/svam)
* Download: See the [official dataset page](http://irvlab.cs.umn.edu/resources/usod-dataset).

USOD is a test dataset for underwater salient object detection containing 300 natural underwater images at a resolution of 640 × 480, each paired with a pixel-level ground-truth mask. The images were selected from existing underwater enhancement and super-resolution datasets as well as field trials, with an emphasis on diversity in object categories, water bodies, optical distortions, and salient-object aspect ratios. Four participants independently annotated the salient pixels.

<details>
<summary>中文介绍</summary>

USOD 是一个水下显著性目标检测测试数据集，包含 300 张分辨率为 640 × 480 的自然水下图像，每张图像都配有像素级真值掩码。图像来自现有的水下增强与超分辨率数据集以及实地试验，重点覆盖不同的目标类别、水体、光学畸变和显著目标宽高比。显著像素由四名参与者独立标注。

</details>

#### USOD10K

* Paper: [USOD10K: A New Benchmark Dataset for Underwater Salient Object Detection](https://ieeexplore.ieee.org/document/10102831/)
* Project: [https://github.com/LinHong-HIT/USOD10K](https://github.com/LinHong-HIT/USOD10K)
* Download: See the [official repository](https://github.com/LinHong-HIT/USOD10K) for Google Drive and Baidu Netdisk links.

USOD10K is a large-scale underwater salient object detection dataset containing 10,255 images with pixel-level ground truths and estimated depth maps. Its official split contains 7,178 training images, 2,051 validation images, and 1,026 test images, following an approximately 7:2:1 protocol. The release also provides object-boundary annotations for the training and validation sets and uses annotation standards different from the earlier USOD dataset.

<details>
<summary>中文介绍</summary>

USOD10K 是一个大规模水下显著性目标检测数据集，包含 10,255 张图像，并提供像素级真值和估计深度图。其官方划分包括 7,178 张训练图像、2,051 张验证图像和 1,026 张测试图像，比例约为 7:2:1。该数据集还为训练集和验证集提供目标边界标注，并采用了与早期 USOD 数据集不同的标注标准。

</details>

#### CSOD10K for Condition-Constrained SOD

* Paper: [Breaking Barriers, Localizing Saliency: A Large-scale Benchmark and Baseline for Condition-Constrained Salient Object Detection](https://ieeexplore.ieee.org/document/11297835)
* Project: [https://rmcong.github.io/proj_CSOD.html](https://rmcong.github.io/proj_CSOD.html) / [https://github.com/ettof/CSOD](https://github.com/ettof/CSOD)
* Download: See the dataset material on the [official project page](https://rmcong.github.io/proj_CSOD.html).

CSOD10K is a condition-constrained salient object detection benchmark with 10,000 pixel-level annotated images and 101 object categories. It is organized around three main constraint types and eight real-world conditions: low light, fog, rain, snow, underwater scenes, reflections, blur, and overexposure. Because underwater imagery is one condition within a broader benchmark, CSOD10K is useful for cross-condition robustness evaluation rather than being an exclusively underwater dataset.

<details>
<summary>中文介绍</summary>

CSOD10K 是一个条件受限显著性目标检测基准，包含 10,000 张像素级标注图像和 101 个目标类别。数据集围绕三类主要约束以及八种真实环境条件组织，包括低光、雾、雨、雪、水下、反射、模糊和过曝。由于水下场景只是这一综合基准中的一种条件，CSOD10K 更适合跨条件鲁棒性评估，而不是一个纯水下数据集。

</details>

#### MAS3K for Marine Animal Segmentation

* Paper: [MAS3K: An Open Dataset for Marine Animal Segmentation](https://link.springer.com/chapter/10.1007/978-3-030-71058-3_12)
* Project: [https://github.com/LinLi-DL/MAS](https://github.com/LinLi-DL/MAS)
* Download: See the [official repository](https://github.com/LinLi-DL/MAS).

MAS3K is an open marine animal segmentation dataset containing 3,103 underwater images with high-quality masks. It includes camouflaged marine animals, commonly visible marine animals, and underwater scenes without marine animals, spanning varied lighting, water turbidity, photographic distortion, and animal appearance. In addition to object-level masks, the dataset provides category and attribute information for marine-animal analysis.

<details>
<summary>中文介绍</summary>

MAS3K 是一个开放的海洋动物分割数据集，包含 3,103 张具有高质量掩码的水下图像。数据覆盖伪装海洋动物、普通可见海洋动物以及不含海洋动物的水下场景，并涵盖不同的光照、水体浑浊度、拍摄畸变和动物外观。除目标级掩码外，该数据集还提供用于海洋动物分析的类别和属性信息。

</details>

#### RMAS for Marine Animal Segmentation

* Paper: [MASNet: A Robust Deep Marine Animal Segmentation Network](https://ieeexplore.ieee.org/document/10113781)
* Project: [https://github.com/zhenqifu/MASNet](https://github.com/zhenqifu/MASNet)
* Download: See the dataset link in the [official repository](https://github.com/zhenqifu/MASNet).

RMAS is a real-world marine animal segmentation dataset with 3,014 underwater images collected from multiple underwater image-processing datasets, including SUIM, UFO, DeepFish, and URPC. Every image has a pixel-level mask and a class label. The annotations group marine animals into five broad categories: sea products, big fish, small fish, turtles, and other animals, while the images cover diverse scenes and degradation patterns.

<details>
<summary>中文介绍</summary>

RMAS 是一个真实世界海洋动物分割数据集，包含 3,014 张水下图像，图像来自 SUIM、UFO、DeepFish 和 URPC 等多个水下图像处理数据集。每张图像都具有像素级掩码和类别标签。标注将海洋动物划分为海产品、大型鱼类、小型鱼类、海龟和其他动物五个大类，同时覆盖多样场景和不同的图像退化模式。

</details>

### Dichotomous Image Segmentation

#### DIS5K

* Paper: [Highly Accurate Dichotomous Image Segmentation](https://arxiv.org/abs/2203.03041)
* Project: [https://xuebinqin.github.io/dis/index.html](https://xuebinqin.github.io/dis/index.html)
* Download: See [https://github.com/xuebinqin/DIS#11-dis-dataset-v10-dis5k](https://github.com/xuebinqin/DIS#11-dis-dataset-v10-dis5k)

We first manually collected over 12,000 images from Flickr based on our pre-designed keywords. Then, according to the structural complexities of the objects, we obtained 5,470 images covering 225 categories in 22 groups. Note that the adopted selection strategy is similar to Zhou et al. Most selected images only contain single objects  to obtain rich and highly accurate structures and details. Meanwhile, the segmentation and labeling confusions caused by the co-occurrence of multiple objects from different categories are avoided to the greatest extent. Therefore, the labeled targets in our DIS5K are mainly the "foreground objects of the images defined by the predesigned keywords" regardless of their characteristics e.g., salient, common, camouflaged, meticulous, etc.
Each image of DIS5K is manually labeled with pixel-wise accuracy using GIMP The average per-image labeling time is ∼30 minutes and some images cost up to 10 hours. It is worth mentioning that some of our labeled ground truth (GT) masks are visually close to the image matting GT. The labeled targets, including transparent and translucent, are binary masks with one pixel's highest accuracy.

<details>
<summary>中文介绍</summary>

我们首先根据预先设计的关键字从 Flickr 手动收集了 12,000 多张图像。然后，根据对象的结构复杂性，我们获得了涵盖22组225个类别的5,470张图像。请注意，采用的选择策略与 Zhou 等人类似。大多数选定的图像仅包含单个对象，以获得丰富且高度准确的结构和细节。同时，最大程度地避免了不同类别的多个对象共现造成的分割和标注混乱。因此，DIS5K中的标记目标主要是“由预先设计的关键字定义的图像的前景对象”，无论其特征如何，例如显著的、常见的、伪装的、细致的等。
DIS5K 的每张图像均使用 GIMP 以像素级精度手动标记。每张图像的平均标记时间为 ∼30 分钟，某些图像长达 10 小时。值得一提的是，我们的一些标记的真值 (GT) 掩模在视觉上与图像抠图 GT 很接近。标记的目标（包括透明和半透明）是具有单像素最高精度的二值掩模。

</details>

### High-Resolution Saliency

#### HRSOD/DAVIS-S

* Paper: [Towards High-Resolution Salient Object Detection](https://arxiv.org/pdf/1908.07274.pdf)
* Project: [https://github.com/yi94code/HRSOD](https://github.com/yi94code/HRSOD)
* Download:
  + HRSOD: [https://drive.google.com/open?id=1bmDGlkzqHoduNigi_GO4Qy9sA9sIaZcY](https://drive.google.com/open?id=1bmDGlkzqHoduNigi_GO4Qy9sA9sIaZcY)
  + DAVIS-S: [https://drive.google.com/open?id=1q1H7yoITLS6i2n-PhgYMIxLdjyhge5AR](https://drive.google.com/open?id=1q1H7yoITLS6i2n-PhgYMIxLdjyhge5AR)

We contribute a High-Resolution Salient Object Detection (HRSOD) dataset, containing 1610 training images and 400 test images. The total 2010 images are collected from the website of Flickr with the license of all creative commons. Pixel-level ground truths are manually annotated by 40 subjects. The shortest edge of each image in our HRSOD is more than 1200 pixels.

<details>
<summary>中文介绍</summary>

我们贡献了一个高分辨率显著目标检测（HRSOD）数据集，包含 1610 个训练图像和 400 个测试图像。 2010 年的全部图片均来自 Flickr 网站，并获得所有知识共享许可。像素级真实情况由 40 名受试者手动注释。我们的 HRSOD 中每张图像的最短边缘超过 1200 像素。

</details>

### Co-Saliency

Some tools for the evaluation:

* Python:
  + [https://github.com/zzhanghub/eval-co-sod](https://github.com/zzhanghub/eval-co-sod)
    - A GPU-accelerated evaluation tool (based on Python & PyTorch) for co-saliency detection task. It can automatically evaluate 8 metrics and draw 4 types of curves. [http://zhaozhang.net/coca.html](http://zhaozhang.net/coca.html)
  + [https://github.com/lartpang/PySODEvalToolkit](https://github.com/lartpang/PySODEvalToolkit)
    - A Python-based salient object detection evaluation toolbox.
    - Based on [PySODMetrics](https://github.com/lartpang/PySODMetrics): A simple and efficient implementation of SOD metrics.
* MATLAB:
  + [http://dpfan.net/wp-content/uploads/CoSalBenchmark-EvaluationTools.zip](http://dpfan.net/wp-content/uploads/CoSalBenchmark-EvaluationTools.zip)
    - From [http://dpfan.net/CoSOD3K/](http://dpfan.net/CoSOD3K/)

#### ImagePair

* Paper: [A Co-Saliency Model of Image Pairs](https://ieeexplore.ieee.org/document/5771591?arnumber=5771591)
* Download: See [http://dpfan.net/CoSOD3K/](http://dpfan.net/CoSOD3K/)

We collected from various databases such as Microsoft Research Cambridge image database, the Caltech-256 Object Categories database, and PASCAL VOC dataset.

<details>
<summary>中文介绍</summary>

我们从各种数据库中收集数据，例如微软剑桥图像数据库、Caltech-256 对象类别数据库和 PASCAL VOC 数据集。

</details>

#### MSRC

* Paper: [Object Categorization by Learned Universal Visual Dictionary](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/criminisi_iccv2005.pdf)
* Project: [https://www.microsoft.com/en-us/research/project/image-understanding/?from=http%3A%2F%2Fresearch.microsoft.com%2Fvision%2Fcambridge%2Frecognition%2F#overview](https://www.microsoft.com/en-us/research/project/image-understanding/?from=http%3A%2F%2Fresearch.microsoft.com%2Fvision%2Fcambridge%2Frecognition%2F#overview)
* Download: See [http://dpfan.net/CoSOD3K/](http://dpfan.net/CoSOD3K/)

#### WICOS

* Paper: [Co-Saliency Detection within a Single Image](https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewFile/16886/16351)
* Download: See [http://dpfan.net/CoSOD3K/](http://dpfan.net/CoSOD3K/)

Since most existing image datasets used for saliency detection do not consider the within-image co-saliency, we collect a new dataset of 364 images for performance evaluation. In the experiment, we test the proposed method and other comparison methods on the new dataset and quantitatively evaluate their performance based on the annotated ground truth.

<details>
<summary>中文介绍</summary>

由于大多数用于显著性检测的现有图像数据集不考虑图像内的协同显著性，因此我们收集了 364 个图像的新数据集用于性能评估。在实验中，我们在新数据集上测试了所提出的方法和其他比较方法，并根据注释的真值定量评估了它们的性能。

</details>

#### iCoSeg

* Paper: [iCoseg: Interactive Co-segmentation with Intelligent Scribble Guidance](http://users.ece.cmu.edu/~dbatra/publications/assets/bkpcl_cvpr10.pdf)
* Project: [http://chenlab.ece.cornell.edu/projects/touch-coseg/](http://chenlab.ece.cornell.edu/projects/touch-coseg/)
* Download: See [http://dpfan.net/CoSOD3K/](http://dpfan.net/CoSOD3K/)
  + Dataset Samples: [http://chenlab.ece.cornell.edu/projects/touch-coseg/iCoseg_dataset.pdf](http://chenlab.ece.cornell.edu/projects/touch-coseg/iCoseg_dataset.pdf)
  + Official Link: [http://chenlab.ece.cornell.edu/projects/touch-coseg/CMU_Cornell_iCoseg_dataset.zip](http://chenlab.ece.cornell.edu/projects/touch-coseg/CMU_Cornell_iCoseg_dataset.zip)

We introduce and make publicly available the largest co-segmentation dataset yet, the CMU-Cornell iCoseg Dataset, with 38 groups, 643 images, and pixelwise hand-annotated groundtruth. Through machine experiments and real user studies with our developed interface, we show that iCoseg can intelligently recommend regions to scribble on, and users following these recommendations can achieve good quality cutouts with significantly lower time and effort than exhaustively examining all cutouts.

<details>
<summary>中文介绍</summary>

我们引入并公开了迄今为止最大的联合分割数据集，即 CMU-Cornell iCoseg 数据集，其中包含 38 个组、643 张图像和逐像素手工注释的基本事实。通过机器实验和使用我们开发的界面进行的真实用户研究，我们表明 iCoseg 可以智能地推荐要涂鸦的区域，并且遵循这些建议的用户可以获得高质量的剪贴画，而与彻底检查所有剪贴画相比，花费的时间和精力要少得多。

</details>

#### CoCA: Common Category Aggregation (CoCA) dataset

* Paper: [Gradient-Induced Co-Saliency Detection](https://arxiv.org/pdf/2004.13364.pdf)
* Project: [http://zhaozhang.net/coca.html](http://zhaozhang.net/coca.html)
* Download: Our dataset is freely available for research, but not for commercial use.
  + Baidu Pan: [https://pan.baidu.com/s/1tEgkrdaO6HUEzditrcmsJA](https://pan.baidu.com/s/1tEgkrdaO6HUEzditrcmsJA) (iqf3)
  + Google Drive: [https://drive.google.com/file/d/1ImAJmqeOdBSvWUh5InLdrw7dEUHdnb1w/view?usp=sharing](https://drive.google.com/file/d/1ImAJmqeOdBSvWUh5InLdrw7dEUHdnb1w/view?usp=sharing)

CoCA dataset consists of 80 categories with 1295 images, covering everyday indoor and outdoor scenes. It is worth noting that these categories are outright staggered with Microsoft COCO. In our CoCA dataset, except for the co-salient object(s), each image contains at least one extraneous salient object, which enables the dataset to better evaluate the models' ability of discovering co-salient object(s) among multiple foregrounds. We provide four levels of annotations: class level, bounding box level, object level, and instance level. Different levels of annotations of our dataset corresponds to different tasks, such as co-localization, few-shot object segmentation, co-saliency detection, and instance co-segmentation.

<details>
<summary>中文介绍</summary>

CoCA数据集由80个类别、1295张图像组成，涵盖日常的室内和室外场景。值得注意的是，这些类别与 Microsoft COCO 完全交错。在我们的 CoCA 数据集中，除了共同显著对象之外，每张图像都包含至少一个无关的显著对象，这使得数据集能够更好地评估模型在多个前景中发现共同显著对象的能力。我们提供四个级别的注释：类级别、边界框级别、对象级别和实例级别。我们的数据集的不同级别的注释对应于不同的任务，例如协同定位、少镜头对象分割、协同显著性检测和实例协同分割。

</details>

#### CoSal2015

* Paper: [Detection of Co-salient Objects by Looking Deep and Wide](http://dpfan.net/wp-content/uploads/2016IJCVCODW169%E3%80%90CoSal2015-Dataset%E3%80%91Detection-of-co-salient-objects-by-looking-deep-and-wide.pdf)
* Project: [http://www.escience.cn/people/JunweiHan/Co-saliency.html](http://www.escience.cn/people/JunweiHan/Co-saliency.html)
* Download: See [http://dpfan.net/CoSOD3K/](http://dpfan.net/CoSOD3K/)

Additionally, we also evaluated the proposed algorithm on a newly established benchmark dataset, i.e., the Cosal2015 dataset (see Fig. 7). In this dataset, we collected 50 image groups containing totally 2015 images from challenging scenarios in the ILSVRC2014 detection set (Russakovsky et al. 2015) and YouTube video set (Prest et al. 2012). 20 subjects were asked to view these image groups and provide the pixel-level annotation manually. Thus, the established dataset is a bigger and more challenging benchmark that can be used for evaluating the co-saliency detection algorithms.

<details>
<summary>中文介绍</summary>

此外，我们还在新建立的基准数据集 Cosal2015 数据集上评估了所提出的算法（见图 7）。在此数据集中，我们收集了 50 个图像组，其中包含来自 ILSVRC2014 检测集（Russakovsky 等人，2015）和 YouTube 视频集（Prest 等人，2012）中具有挑战性场景的 2015 个图像。 20 名受试者被要求查看这些图像组并手动提供像素级注释。因此，建立的数据集是一个更大、更具挑战性的基准，可用于评估协同显著性检测算法。

</details>

#### CoSOD3k

* Paper:
  + [Taking a Deeper Look at Co-Salient Object Detection](https://openaccess.thecvf.com/content_CVPR_2020/papers/Fan_Taking_a_Deeper_Look_at_Co-Salient_Object_Detection_CVPR_2020_paper.pdf)
  + [Re-thinking Co-Salient Object Detection](https://arxiv.org/pdf/2007.03380.pdf)
* Project: [http://dpfan.net/CoSOD3K/](http://dpfan.net/CoSOD3K/)
* Download: See [http://dpfan.net/CoSOD3K/](http://dpfan.net/CoSOD3K/)

Co-salient object detection (CoSOD) is a newly emerging and rapidly growing branch of salient object detection (SOD), which aims to detect the co-occurring salient objects in multiple images. However, existing CoSOD datasets often have a serious data bias, which assumes that each group of images contains salient objects of similar visual appearances. This bias results in the ideal settings and the effectiveness of the models, trained on existing datasets, may be impaired in real-life situations, where the similarity is usually semantic or conceptual. To tackle this issue, we first collect a new high-quality dataset, named CoSOD3k, which contains 3, 316 images divided in 160 groups with multiple level annotations, i.e., category, bounding box, object, and instance levels. CoSOD3k makes a significant leap in terms of diversity, difficulty and scalability, benefiting related vision tasks. Besides, we comprehensively summarize 34 cutting-edge algorithms, benchmarking 19 of them over four existing CoSOD datasets (MSRC, iCoSeg, Image Pair and CoSal2015) and our CoSOD3k with a total of ∼61K images (largest scale), and reporting group-level performance analysis. Finally, we discuss the challenge and future work of CoSOD. Our study would give a strong boost to growth in the CoSOD community. Benchmark toolbox and results are available on our project page.

<details>
<summary>中文介绍</summary>

共显著目标检测（CoSOD）是显著目标检测（SOD）的一个新兴且快速发展的分支，旨在检测多幅图像中同时出现的显著目标。然而，现有的 CoSOD 数据集通常存在严重的数据偏差，即假设每组图像都包含具有相似视觉外观的显著对象。这种偏差会导致理想的设置和在现有数据集上训练的模型的有效性在现实生活中可能会受到损害，其中相似性通常是语义或概念上的。为了解决这个问题，我们首先收集一个新的高质量数据集，名为 CoSOD3k，其中包含 3, 316 张图像，分为 160 组，具有多个级别注释，即类别、边界框、对象和实例级别。 CoSOD3k 在多样性、难度和可扩展性方面取得了重大飞跃，有利于相关的视觉任务。此外，我们全面总结了 34 种前沿算法，在四个现有 CoSOD 数据集（MSRC、iCoSeg、Image Pair 和 CoSal2015）和我们的 CoSOD3k（总共 61K 图像（最大规模））上对其中 19 种进行了基准测试，并报告了组级性能分析。最后，我们讨论了 CoSOD 的挑战和未来的工作。我们的研究将有力推动 CoSOD 社区的发展。基准工具箱和结果可在我们的项目页面上找到。

</details>

#### RGBDCosal150

* Paper: [Co-saliency Detection for RGBD Images Based on Multi-constraint Feature Matching and Cross Label Propagation](https://arxiv.org/abs/1710.05172)
* Project: [https://rmcong.github.io/proj_RGBD_cosal.html](https://rmcong.github.io/proj_RGBD_cosal.html)
* Download:
  * Official: [https://github.com/rmcong/RGBD-Cosal150-Dataset](https://github.com/rmcong/RGBD-Cosal150-Dataset)

In this dataset, we collected 21 image groups containing totally 150 images from RGBD NJU-1985 (NJU2000) dataset with pixellevel ground truth, and the original depth maps are provided by the dataset itself.

<details>
<summary>中文介绍</summary>

在此数据集中，我们从具有像素级真实值的 RGBD NJU-1985 (NJU2000) 数据集中收集了 21 个图像组，共包含 150 张图像，原始深度图由数据集本身提供。

</details>

#### RGBDCoseg183

* Paper: [Object-based RGBD image co-segmentation with mutex constraint](http://www.cv-foundation.org/openaccess/content_cvpr_2015/html/Fu_Object-Based_RGBD_Image_2015_CVPR_paper.html)
* Download:
  * OneDrive: https://onedrive.live.com/redir?resid=F3A8A31ABFAC51B0!269&authkey=!AHUBN0lk5kQLWzQ&ithint=file%2czip
  * BaiduYun: https://pan.baidu.com/s/1cAMin0

We have constructed one ourselves with some images from the [RGBD Scenes Dataset](http://rgbd-dataset.cs.washington.edu/) and some that were captured by ourselves. The dataset contains 16 image sets, each of 6 to 17 images taken from indoor scenes with one common foreground object (193 images in total). Pixel-level ground-truth is labeled for the common foreground object in each image.

<details>
<summary>中文介绍</summary>

我们自己使用 RGBD 场景数据集 中的一些图像和我们自己捕获的一些图像构建了一个。该数据集包含 16 个图像集，每个图像集有 6 到 17 张图像，取自具有一个共同前景物体的室内场景（总共 193 张图像）。像素级真值标记为每个图像中的常见前景对象。

</details>

#### INCT2016

* Paper: [Unsupervised co-segmentation for indefinite number of common foreground objects](https://pubmed.ncbi.nlm.nih.gov/26886987/)

INCT2016 is a more challenging dataset with larger appearance variation, indefinite number of targets, and complicated backgrounds, which contains 291 images distributed in 12 categories with pixel-level ground truth. INCT2016 is built by expanding the [Coseg-Rep](http://www.jifengdai.org/publications/ICCV_Cosegmentation_2013.pdf) dataset.

<details>
<summary>中文介绍</summary>

INCT2016是一个更具挑战性的数据集，具有较大的外观变化、不确定的目标数量和复杂的背景，其中包含分布在12个类别的291张图像，具有像素级的真实值。 INCT2016是通过扩展Coseg-Rep数据集构建的。

</details>

### Video Saliency

> Dataset backups: The [DAVSOD Downloads section](https://github.com/DengPingFan/DAVSOD#downloads) provides backup download links for multiple video saliency datasets.

#### RSD(PKU-RSD)

* Paper: [A dataset and evaluation methodology for visual saliency in video](https://ieeexplore.ieee.org/document/5202529)
* Project: [https://pkuml.org/resources/dataset.html](https://pkuml.org/resources/dataset.html)
* Download: [https://pkuml.org/resources/pku-rsd.html](https://pkuml.org/resources/pku-rsd.html)

We constructed this PKU-RSD (Region Saliency Dataset) dataset that captures spatiotemporal visual saliency for evaluating different video saliency models. This dataset contains 431 short videos covering various scenarios (surveillance, advertising, news, cartoons, movies, etc.) and the corresponding annotation results of salient objects in sampled keyframes manually labeled by 23 subjects.

<details>
<summary>中文介绍</summary>

我们构建了这个PKU-RSD(区域显著性数据集)数据集, 可以捕获时空视觉显著性, 用于评估不同的视频显著性模型. 该数据集包含431个短视频, 其涵盖各种场景(监视, 广告, 新闻, 卡通, 电影等)以及由23个主题手动标记的采样关键帧中的显著对象的相应注释结果.

</details>

#### STC

* Paper: [Detection of salient objects with focused attention based on spatial and temporal coherence](https://link.springer.com/article/10.1007%2Fs11434-010-4387-1)
* Download: This dataset is freely available from the author.

To demonstrate quantitatively the advantages of using spatial and temporal coherence, we carried out our experiments on 32 video segments with a total of 4820 frames collected from the internet. Each video segment contains a single salient object, which ranges from humans performing various activities and animals in the wild, to vehicles both on the ground and in the air. All the frames are annotated with object bounding boxes, and the detection performance is evaluated in terms of mean precision (P), recall (R), F-measure (F0.5), and boundary displacement errors (BDE).

<details>
<summary>中文介绍</summary>

为了定量地展示使用空间和时间相干性的优势，我们对从互联网收集的 32 个视频片段（总共 4820 帧）进行了实验。每个视频片段都包含一个显著对象，范围从进行各种活动的人类和野外动物，到地面和空中的车辆。所有帧都用对象边界框进行注释，并根据平均精度（P）、召回率（R）、F-measure（F0.5）和边界位移误差（BDE）来评估检测性能。

</details>

#### SegTrackV1/V2

* Paper:
  + V1: [Motion Coherent Tracking with Multi-label MRF Optimization](https://www.bmva-archive.org.uk/bmvc/2010/conference/paper56/index.html)
  + V2: [Video Segmentation by Tracking Many Figure-Ground Segments](https://ieeexplore.ieee.org/document/6751383)
* Project and Download:
  + V1: <https://cpl.cc.gatech.edu/projects/SegTrack/>
  + V2: <https://web.engr.oregonstate.edu/~lif/SegTrack2/dataset.html>

SegTrack was originally introduced for evaluating segmentation accuracy in video tracking and was later adopted for video salient object detection. SegTrack V1 contains six short video sequences with pixel-level foreground annotations. SegTrack V2 extends it to 14 sequences and provides separate pixel-level a