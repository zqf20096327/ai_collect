# Medical Datasets for Machine Learning

> **Language / 语言**: [English](README.md) | [中文](README.zh-CN.md)

> Curated catalog of medical datasets for machine learning research. For informational purposes only; respect each dataset's license and access restrictions.

This catalog extends [beamandrew/medical-data](https://github.com/beamandrew/medical-data) with structured metadata, DOI-first citations, bilingual documentation, and Asia-Pacific resources. See [CONTRIBUTING.md](CONTRIBUTING.md) to add entries.

## Table of contents

- [Medical Imaging](#medical-imaging)
  - [Radiology](#radiology)
  - [Pathology](#pathology)
  - [Ophthalmology](#ophthalmology)
  - [Cardiac](#cardiac)
  - [Neuroimaging](#neuroimaging)
  - [Dermatology](#dermatology)
- [Physiological Signals](#physiological-signals)
- [Electronic Health Records](#electronic-health-records)
- [Clinical NLP & Literature](#clinical-nlp--literature)
- [Public Health & Population Data](#public-health--population-data)
- [Challenges & Benchmarks](#challenges--benchmarks)
- [Tabular / Classic ML](#tabular--classic-ml)
- [Meta-Catalogs & Repositories](#meta-catalogs--repositories)
- [References](#references)
- [Legacy index](#legacy-index)


<a id="medical-imaging"></a>


## Medical Imaging

<a id="radiology"></a>


### Radiology

### MedPix — NLM MedPix

| Field | Value |
|-------|-------|
| **Modality** | Multi-modality images |
| **Task** | Retrieval, education |
| **Size** | 59k images, 12k cases |
| **Access** | Registration |
| **License** | NLM terms |
| **Last verified** | 2026-06-01 |

**Description.** NLM-hosted teaching cases with integrated text metadata.

**Primary reference.** NLM. *MedPix*. https://medpix.nlm.nih.gov/

**Access.** [MedPix](https://medpix.nlm.nih.gov/home)

### ABIDE — Autism Brain Imaging Data Exchange

| Field | Value |
|-------|-------|
| **Modality** | fMRI |
| **Task** | Connectivity, classification |
| **Size** | 1,112 subjects |
| **Access** | Registration |
| **License** | ABIDE DUA |
| **Last verified** | 2026-06-01 |

**Description.** Resting-state and structural MRI with phenotypes for ASD research.

**Primary reference.** Di Martino A, et al. *Mol Psychiatry*. 2014. [DOI:10.1038/mp.2013.78](https://doi.org/10.1038/mp.2013.78)

**Access.** [ABIDE](http://fcon_1000.projects.nitrc.org/indi/abide/)

### ADNI — Alzheimer's Disease Neuroimaging Initiative

| Field | Value |
|-------|-------|
| **Modality** | MRI, PET, clinical, omics |
| **Task** | Classification, progression |
| **Size** | 1,000+ subjects |
| **Access** | Registration |
| **License** | ADNI DUA |
| **Last verified** | 2026-06-01 |

**Description.** Longitudinal multi-modal AD and MCI cohort.

**Primary reference.** Jack CR Jr, et al. *Alzheimer's Dement*. 2008. [DOI:10.1016/j.jalz.2008.07.003](https://doi.org/10.1016/j.jalz.2008.07.003)

**Access.** [ADNI](https://adni.loni.usc.edu/)

### CT Colonography — TCIA CT Colonography

| Field | Value |
|-------|-------|
| **Modality** | CT |
| **Task** | Polyp detection, segmentation |
| **Size** | Various |
| **Access** | Open (TCIA) |
| **License** | TCIA terms |
| **Last verified** | 2026-06-01 |

**Description.** CT colonography for polyp size classes.

**Primary reference.** TCIA Collection. [CT COLONOGRAPHY](https://www.cancerimagingarchive.net/collection/ct-colonography/)

**Access.** [CT Colonography](https://www.cancerimagingarchive.net/collection/ct-colonography/)

### LIDC-IDRI — Lung Image Database Consortium

| Field | Value |
|-------|-------|
| **Modality** | CT |
| **Task** | Nodule detection, annotation |
| **Size** | 1,018 cases |
| **Access** | Open (TCIA) |
| **License** | TCIA terms |
| **Last verified** | 2026-06-01 |

**Description.** Thoracic CT with radiologist nodule outlines and ratings.

**Primary reference.** Armato SG III, et al. *Med Phys*. 2011. [DOI:10.1118/1.3528204](https://doi.org/10.1118/1.3528204)

**Access.** [LIDC-IDRI](https://www.cancerimagingarchive.net/collection/lidc-idri/)

### TCIA — The Cancer Imaging Archive

| Field | Value |
|-------|-------|
| **Modality** | Multi-modality |
| **Task** | Oncology imaging research |
| **Size** | Many collections |
| **Access** | Open / mixed |
| **License** | Per-collection |
| **Last verified** | 2026-06-01 |

**Description.** Cancer imaging collections with DOI-backed subsets.

**Primary reference.** Clark K, et al. *J Digit Imaging*. 2013. [DOI:10.1007/s10278-013-9622-7](https://doi.org/10.1007/s10278-013-9622-7)

**Access.** [TCIA](https://www.cancerimagingarchive.net/)

### DDSM — Digital Database for Screening Mammography

| Field | Value |
|-------|-------|
| **Modality** | Mammography |
| **Task** | Detection, CAD |
| **Size** | ~2,500 studies |
| **Access** | Open |
| **License** | Research use |
| **Last verified** | 2026-06-01 |

**Description.** Screening mammograms with ROI truth.

**Primary reference.** Heath M, et al. *DMKD*. 2000.

**Access.** [DDSM](http://marathon.csee.usf.edu/Mammography/Database.html)

### INbreast — INbreast Mammography

| Field | Value |
|-------|-------|
| **Modality** | Mammography |
| **Task** | Mass, calcification |
| **Size** | 115 cases, 410 images |
| **Access** | Registration |
| **License** | Research agreement |
| **Last verified** | 2026-06-01 |

**Description.** Digital mammography with XML contours.

**Primary reference.** Moreira IC, et al. *J Digit Imaging*. 2012. [DOI:10.1007/s10278-012-9475-8](https://doi.org/10.1007/s10278-012-9475-8)

**Access.** [INbreast](http://medicalresearch.inescporto.pt/breastresearch/index.php/Get_INbreast_Database)

### mini-MIAS — MIAS Mini-Mammographic

| Field | Value |
|-------|-------|
| **Modality** | Mammography |
| **Task** | Detection |
| **Size** | 322 images |
| **Access** | Open |
| **License** | MIAS terms |
| **Last verified** | 2026-06-01 |

**Description.** Classic mammography benchmark (1024×1024).

**Primary reference.** Suckling J, et al. *ExaByte*. 1994.

**Access.** [mini-MIAS](http://peipa.essex.ac.uk/info/mias.html)

### ChestX-ray14 — NIH ChestX-ray14

| Field | Value |
|-------|-------|
| **Modality** | CXR |
| **Task** | Multi-label classification |
| **Size** | 112,120 images |
| **Access** | Open |
| **License** | CC0 / NIH |
| **Last verified** | 2026-06-01 |

**Description.** 14 thoracic disease labels from reports.

**Primary reference.** Wang X, et al. *CVPR*. 2017.

**Access.** [ChestX-ray14](https://nihcc.app.box.com/v/ChestXray-NIHCC)

### CheXpert — CheXpert

| Field | Value |
|-------|-------|
| **Modality** | CXR |
| **Task** | Classification, uncertainty |
| **Size** | 224,316 studies |
| **Access** | Open (with rules) |
| **License** | Stanford agreement |
| **Last verified** | 2026-06-01 |

**Description.** Large chest X-ray set with uncertainty labels.

**Primary reference.** Irvin J, et al. *AAAI*. 2019. [arXiv:1901.07031](https://arxiv.org/abs/1901.07031)

**Access.** [CheXpert](https://stanfordmlgroup.github.io/competitions/chexpert/)

### MIMIC-CXR — MIMIC-CXR-JPG

| Field | Value |
|-------|-------|
| **Modality** | CXR |
| **Task** | Classification, report generation |
| **Size** | 377,110 images |
| **Access** | Credentialed |
| **License** | PhysioNet DUA |
| **Last verified** | 2026-06-01 |

**Description.** De-identified chest X-rays linked to MIMIC-IV reports.

**Primary reference.** Johnson AEW, et al. *Radiology*. 2019. [DOI:10.1148/radiol.2019182748](https://doi.org/10.1148/radiol.2019182748)

**Access.** [MIMIC-CXR](https://physionet.org/content/mimic-cxr-jpg/)

### PadChest — PadChest

| Field | Value |
|-------|-------|
| **Modality** | CXR |
| **Task** | Multi-label |
| **Size** | 160k+ images |
| **Access** | Registration |
| **License** | Hospital terms |
| **Last verified** | 2026-06-01 |

**Description.** Large Spanish hospital chest X-ray corpus.

**Primary reference.** Bustos A, et al. *Med Image Anal*. 2020. [DOI:10.1016/j.media.2020.101796](https://doi.org/10.1016/j.media.2020.101796)

**Access.** [PadChest](https://bimcv.cipf.es/bimcv-projects/padchest/)

### VinDr-CXR — VinDr-CXR

| Field | Value |
|-------|-------|
| **Modality** | CXR |
| **Task** | Detection, localization |
| **Size** | 18k studies |
| **Access** | Open |
| **License** | VinDr license |
| **Last verified** | 2026-06-01 |

**Description.** Multi-annotator Vietnamese chest radiographs.

**Primary reference.** Nguyen HT, et al. *Sci Data*. 2022. [DOI:10.1038/s41597-022-01655-8](https://doi.org/10.1038/s41597-022-01655-8)

**Access.** [VinDr-CXR](https://vindr.ai/datasets/cxr)

### NSCLC Radiogenomics — TCIA NSCLC Radiogenomics

| Field | Value |
|-------|-------|
| **Modality** | CT, PET/CT |
| **Task** | Radiogenomics |
| **Size** | 211 subjects |
| **Access** | Open (TCIA) |
| **License** | TCIA terms |
| **Last verified** | 2026-06-01 |

**Description.** CT/PET-CT with genomic correlates for NSCLC.

**Primary reference.** Bakr S, et al. *Data Brief*. 2018.

**Access.** [NSCLC Radiogenomics](https://www.cancerimagingarchive.net/collection/nsclc-radiogenomics/)

### DeepLesion — NIH DeepLesion

| Field | Value |
|-------|-------|
| **Modality** | CT |
| **Task** | Lesion detection |
| **Size** | 32,735 CTs, 4,427 patients |
| **Access** | Open (box) |
| **License** | NIH CC terms |
| **Last verified** | 2026-06-01 |

**Description.** Large-scale lesion annotations on clinical CT.

**Primary reference.** Yan K, et al. *IEEE TMI*. 2018. [DOI:10.1109/TMI.2018.2805949](https://doi.org/10.1109/TMI.2018.2805949)

**Access.** [DeepLesion](https://nihcc.app.box.com/v/DeepLesion)

### CT-RATE — CT-RATE

| Field | Value |
|-------|-------|
| **Modality** | CT |
| **Task** | Report generation, VQA |
| **Size** | 25,692 volumes |
| **Access** | Registration |
| **License** | CT-RATE terms |
| **Last verified** | 2026-06-01 |

**Description.** Chest CT volumes with radiology reports.

**Primary reference.** Hamamci IE, et al. *Med Image Anal*. 2024. [DOI:10.1016/j.media.2024.103411](https://doi.org/10.1016/j.media.2024.103411)

**Access.** [CT-RATE](https://huggingface.co/datasets/ibrahimhamamci/CT-RATE)

### TotalSegmentator — TotalSegmentator CT

| Field | Value |
|-------|-------|
| **Modality** | CT |
| **Task** | Segmentation |
| **Size** | 1,228 CTs |
| **Access** | Open |
| **License** | CC-BY 4.0 |
| **Last verified** | 2026-06-01 |

**Description.** 104 anatomical structures annotated on CT.

**Primary reference.** Wasserthal J, et al. *Nat Methods*. 2023. [DOI:10.1038/s41592-023-01905-0](https://doi.org/10.1038/s41592-023-01905-0)

**Access.** [TotalSegmentator](https://github.com/wasserth/TotalSegmentator)

### AMOS — AMOS22

| Field | Value |
|-------|-------|
| **Modality** | CT, MRI |
| **Task** | Abdominal segmentation |
| **Size** | 500 cases |
| **Access** | Open |
| **License** | AMOS license |
| **Last verified** | 2026-06-01 |

**Description.** Abdominal multi-organ segmentation challenge data.

**Primary reference.** Ji Y, et al. *arXiv preprint*. [2206.08023](https://arxiv.org/abs/2206.08023)

**Access.** [AMOS](https://amos22.grand-challenge.org/)

### BTCV — Beyond the Cranial Vault

| Field | Value |
|-------|-------|
| **Modality** | CT |
| **Task** | Abdominal segmentation |
| **Size** | 50 subjects |
| **Access** | Open |
| **License** | BTCV terms |
| **Last verified** | 2026-06-01 |

**Description.** Multi-organ abdominal CT segmentation.

**Primary reference.** Landman B, et al. *MICCAI Challenge*. 2015.

**Access.** [BTCV](https://www.synapse.org/#!Synapse:syn3193805/wiki/89480)

### WORD — Whole abdominal ORgan Dataset

| Field | Value |
|-------|-------|
| **Modality** | CT |
| **Task** | Segmentation |
| **Size** | 150 volumes |
| **Access** | Open |
| **License** | WORD terms |
| **Last verified** | 2026-06-01 |

**Description.** Whole-abdominal organ segmentation.

**Primary reference.** Xiong Y, et al. *Med Image Anal*. 2023.

**Access.** [WORD](https://github.com/HiLab-git/WORD)

### KiTS — Kidney Tumor Segmentation

| Field | Value |
|-------|-------|
| **Modality** | CT |
| **Task** | Renal tumor seg |
| **Size** | 300 cases |
| **Access** | Open |
| **License** | KiTS terms |
| **Last verified** | 2026-06-01 |

**Description.** Kidney and tumor segmentation benchmark.

**Primary reference.** Heller N, et al. *arXiv preprint*. [1909.01093](https://arxiv.org/abs/1909.01093)

**Access.** [KiTS](https://kits-challenge.org/)

### LiTS — Liver Tumor Segmentation

| Field | Value |
|-------|-------|
| **Modality** | CT |
| **Task** | Liver lesion seg |
| **Size** | 131 volumes |
| **Access** | Open |
| **License** | LiTS terms |
| **Last verified** | 2026-06-01 |

**Description.** Liver and tumor CT segmentation challenge.

**Primary reference.** Bilic P, et al. *Med Image Anal*. 2019.

**Access.** [LiTS](http://www.lits-challenge.com/)

### DIR-Lab — Deformable Image Registration Lab

| Field | Value |
|-------|-------|
| **Modality** | CT |
| **Task** | Registration |
| **Size** | 20 cases |
| **Access** | Open |
| **License** | DIR-Lab terms |
| **Last verified** | 2026-06-01 |

**Description.** Reference for thoracic DIR evaluation.

**Primary reference.** Castillo R, et al. *Med Phys*. 2013.

**Access.** [DIR-Lab](https://www.dir-lab.com/)

### VIA Lung CT — VIA Public Databases

| Field | Value |
|-------|-------|
| **Modality** | CT |
| **Task** | CAD |
| **Size** | Multiple |
| **Access** | Open |
| **License** | VIA terms |
| **Last verified** | 2026-06-01 |

**Description.** Lung CT with radiologist annotations (I-ELCAP related).

**Primary reference.** VIA Group, Cornell.

**Access.** [VIA Lung CT](http://www.via.cornell.edu/databases/)

### Belarus TB Portal — Belarus Tuberculosis Portal

| Field | Value |
|-------|-------|
| **Modality** | CXR, CT |
| **Task** | TB imaging |
| **Size** | Clinical cohort |
| **Access** | Open |
| **License** | Portal terms |
| **Last verified** | 2026-06-01 |

**Description.** MDR/XDR TB radiology with clinical data.

**Primary reference.** Sergeev R, et al. *ISBRA*. 2016.

**Access.** [Belarus TB Portal](http://tuberculosis.by/)

### I2CVB — Imaging and I2CVB Prostate

| Field | Value |
|-------|-------|
| **Modality** | MRI |
| **Task** | CAD, segmentation |
| **Size** | Multi-parametric |
| **Access** | Registration |
| **License** | I2CVB terms |
| **Last verified** | 2026-06-01 |

**Description.** Multi-parametric MRI for prostate CAD research.

**Primary reference.** Lemaitre G, et al. *TPAMI*. 2015.

**Access.** [I2CVB](http://i2cvb.github.io/)

### SCR — Segmentation in Chest Radiographs

| Field | Value |
|-------|-------|
| **Modality** | CXR |
| **Task** | Segmentation |
| **Size** | 247 images |
| **Access** | Open |
| **License** | SCR terms |
| **Last verified** | 2026-06-01 |

**Description.** Lung, heart, clavicle segmentation in CXR.

**Primary reference.** van Ginneken B, et al. *IEEE TMI*. 2006.

**Access.** [SCR](http://www.isi.uu.nl/Research/Databases/SCR/)

### CIMA Histology — CIMA Histology Registration

| Field | Value |
|-------|-------|
| **Modality** | Microscopy |
| **Task** | Registration |
| **Size** | 108 image pairs |
| **Access** | Open |
| **License** | Research |
| **Last verified** | 2026-06-01 |

**Description.** Multi-stain histology slice registration.

**Primary reference.** Borovec R, et al. *Scientific Reports*. 2020.

**Access.** [CIMA Histology](http://cmp.felk.cvut.cz/~borovji3/?page=dataset)

### MURA — MURA

| Field | Value |
|-------|-------|
| **Modality** | X-ray |
| **Task** | Abnormality detection |
| **Size** | 40,895 images |
| **Access** | Open |
| **License** | MURA license |
| **Last verified** | 2026-06-01 |

**Description.** Musculoskeletal radiograph benchmark.

**Primary reference.** Rajpurkar P, et al. *arXiv preprint*. [1712.06957](https://arxiv.org/abs/1712.06957)

**Access.** [MURA](https://stanfordmlgroup.github.io/competitions/mura/)

### Cholec80 — Cholec80

| Field | Value |
|-------|-------|
| **Modality** | Laparoscopic video |
| **Task** | Phase, tool detection |
| **Size** | 80 videos |
| **Access** | Open |
| **License** | Research |
| **Last verified** | 2026-06-01 |

**Description.** Cholecystectomy video with phase labels.

**Primary reference.** Twinanda AP, et al. *Med Image Anal*. 2017.

**Access.** [Cholec80](http://camma.u-strasbg.fr/datasets)

### JIGSAWS — JIGSAWS

| Field | Value |
|-------|-------|
| **Modality** | Surgical kinematics |
| **Task** | Skill assessment |
| **Size** | 103 trials |
| **Access** | Open |
| **License** | Research |
| **Last verified** | 2026-06-01 |

**Description.** da Vinci surgical gesture dataset.

**Primary reference.** Gao Y, et al. *IJRR*. 2014.

**Access.** [JIGSAWS](https://cirl.lcsr.jhu.edu/research/hmm/datasets/jigsaws_release/)

### KID — KID Capsule Endoscopy

| Field | Value |
|-------|-------|
| **Modality** | Capsule endoscopy |
| **Task** | Decision support |
| **Size** | Video studies |
| **Access** | Open |
| **License** | Research |
| **Last verified** | 2026-06-01 |

**Description.** Capsule endoscopy for medical decision support.

**Primary reference.** Koulaouzidis A, Iakovidis I.

**Access.** [KID](http://is-innovation.eu/kid)

### Cell Tracking Challenge — Cell Tracking Challenge

| Field | Value |
|-------|-------|
| **Modality** | Microscopy video |
| **Task** | Tracking |
| **Size** | Multiple |
| **Access** | Open |
| **License** | Challenge |
| **Last verified** | 2026-06-01 |

**Description.** 2D/3D cell tracking benchmarks.

**Primary reference.** Ulman V, et al. *Nat Methods*. 2017.

**Access.** [Cell Tracking Challenge](https://celltrackingchallenge.net/)

### COPD ML — COPD ML Features

| Field | Value |
|-------|-------|
| **Modality** | CT |
| **Task** | Weakly supervised |
| **Size** | 1,000+ scans |
| **Access** | Open |
| **License** | Research |
| **Last verified** | 2026-06-01 |

**Description.** Weak labels for COPD on lung CT.

**Primary reference.** Cheplygina V, et al. *Med Image Anal*. 2014.

**Access.** [COPD ML](http://bigr.nl/research/projects/copd)

### CT Emphysema — CT Emphysema Database

| Field | Value |
|-------|-------|
| **Modality** | CT |
| **Task** | Emphysema quantification |
| **Size** | HRCT scans |
| **Access** | Open |
| **License** | Research |
| **Last verified** | 2026-06-01 |

**Description.** Emphysema quantification on CT.

**Primary reference.** Sorensen L, et al. *IEEE ISBI*. 2012.

**Access.** [CT Emphysema](http://image.diku.dk/emphysema_database/)

### IRMA — IRMA Radiology

| Field | Value |
|-------|-------|
| **Modality** | X-ray |
| **Task** | Retrieval |
| **Size** | 10k+ images |
| **Access** | Open |
| **License** | Research |
| **Last verified** | 2026-06-01 |

**Description.** Anonymous radiographs for retrieval.

**Primary reference.** Deserno TM, et al. *Int J CARS*. 2012.

**Access.** [IRMA](https://ganymed.imib.rwth-aachen.de/irma/datasets_en.php)

### NIH ChestX-ray (Kaggle) — NIH ChestX-ray14 on Kaggle

| Field | Value |
|-------|-------|
| **Modality** | CXR |
| **Task** | Classification |
| **Size** | 112,120 images |
| **Access** | Open |
| **License** | CC0 |
| **Last verified** | 2026-06-01 |

**Description.** Kaggle mirror of ChestX-ray14.

**Primary reference.** Wang X, et al. *CVPR*. 2017.

**Access.** [NIH ChestX-ray (Kaggle)](https://www.kaggle.com/nih-chest-xrays/data)

### DICOM Samples — OsiriX DICOM Library

| Field | Value |
|-------|-------|
| **Modality** | DICOM |
| **Task** | Education |
| **Size** | Sample sets |
| **Access** | Open |
| **License** | Research only |
| **Last verified** | 2026-06-01 |

**Description.** Sample DICOM for teaching and R&D.

**Primary reference.** OsiriX.

**Access.** [DICOM Samples](https://www.osirix-viewer.com/resources/dicom-image-library/)

### mammoimage.org — Mammographic Image Analysis

| Field | Value |
|-------|-------|
| **Modality** | Mammography |
| **Task** | Index |
| **Size** | Many links |
| **Access** | Open |
| **License** | Various |
| **Last verified** | 2026-06-01 |

**Description.** Index of mammography databases.

**Primary reference.** mammoimage.org.

**Access.** [mammoimage.org](http://www.mammoimage.org/databases/)

### USC-SIPI — USC-SIPI Image Database

| Field | Value |
|-------|-------|
| **Modality** | General images |
| **Task** | Texture, aerial |
| **Size** | Multiple volumes |
| **Access** | Open |
| **License** | Research |
| **Last verified** | 2026-06-01 |

**Description.** Classic image processing volumes including textures.

**Primary reference.** USC-SIPI.

**Access.** [USC-SIPI](http://sipi.usc.edu/database/)

### SLP — SLP Multimodal In-Bed Pose

| Field | Value |
|-------|-------|
| **Modality** | RGB, depth, pressure |
| **Task** | Pose estimation |
| **Size** | 109 subjects |
| **Access** | Open |
| **License** | Research |
| **Last verified** | 2026-06-01 |

**Description.** Multimodal in-bed human pose.

**Primary reference.** Liu Y, Ostadabbas S. *IEEE*. 2019.

**Access.** [SLP](https://web.northeastern.edu/ostadabbas/2019/06/27/multimodal-in-bed-pose-estimation/)

<a id="pathology"></a>


### Pathology

### CAMELYON16 — CAMELYON16

| Field | Value |
|-------|-------|
| **Modality** | WSI |
| **Task** | Metastasis detection |
| **Size** | 400 slides |
| **Access** | Open |
| **License** | CAMELYON terms |
| **Last verified** | 2026-06-01 |

**Description.** Lymph node metastasis in H&E slides.

**Primary reference.** Bejnordi BE, et al. *Med Image Anal*. 2017.

**Access.** [CAMELYON16](https://camelyon16.grand-challenge.org/)

### CAMELYON17 — CAMELYON17

| Field | Value |
|-------|-------|
| **Modality** | WSI |
| **Task** | Patient-level classification |
| **Size** | 1,000+ slides |
| **Access** | Open |
| **License** | CAMELYON terms |
| **Last verified** | 2026-06-01 |

**Description.** Patient-level WSI classification challenge.

**Primary reference.** CAMELYON17 Challenge.

**Access.** [CAMELYON17](https://camelyon17.grand-challenge.org/)

### ADP — Atlas of Digital Pathology

| Field | Value |
|-------|-------|
| **Modality** | Histology patches |
| **Task** | Multi-label tissue |
| **Size** | 17,668 patches |
| **Access** | Open |
| **License** | ADP terms |
| **Last verified** | 2026-06-01 |

**Description.** Hierarchical tissue type labels on patches.

**Primary reference.** Hosseini MS, et al. *Scientific Reports*. 2019.

**Access.** [ADP](https://www.dsp.utoronto.ca/projects/ADP/)

### CAMEL — CAMEL Colorectal Adenoma

| Field | Value |
|-------|-------|
| **Modality** | WSI |
| **Task** | Weakly supervised |
| **Size** | 177 WSIs |
| **Access** | Open |
| **License** | CAMEL terms |
| **Last verified** | 2026-06-01 |

**Description.** Weak labels for colorectal adenoma WSIs.

**Primary reference.** Song Y, Wang H. *GitHub*.

**Access.** [CAMEL](https://github.com/ThoroughImages/CAMEL)

### CRCHistoPhenotypes — CRCHistoPhenotypes

| Field | Value |
|-------|-------|
| **Modality** | Histology |
| **Task** | Nuclei classification |
| **Size** | ~30k nuclei |
| **Access** | Open |
| **License** | Research |
| **Last verified** | 2026-06-01 |

**Description.** Colorectal nuclei with cell-type labels.

**Primary reference.** Sirinukunwattana K, et al. *Med Image Anal*. 2016.

**Access.** [CRCHistoPhenotypes](https://warwick.ac.uk/fac/cross_fac/tia/data/crchistolenamednucleihe/)

### FocusPath — FocusPath

| Field | Value |
|-------|-------|
| **Modality** | Pathology microscopy |
| **Task** | Focus quality |
| **Size** | 864 patches |
| **Access** | Open |
| **License** | Research |
| **Last verified** | 2026-06-01 |

**Description.** Digital pathology focus quality assessment.

**Primary reference.** Hosseini MS, et al. *IEEE JBHI*. 2020.

**Access.** [FocusPath](https://github.com/mahdihosseini/FoucsPath)

### Quilt-1M — Quilt-1M

| Field | Value |
|-------|-------|
| **Modality** | Pathology images + text |
| **Task** | VLM pretraining |
| **Size** | 1M image-text pairs |
| **Access** | Open |
| **License** | Quilt terms |
| **Last verified** | 2026-06-01 |

**Description.** Large pathology vision-language corpus.

**Primary reference.** Ikezogwo WC, et al. *NeurIPS D&B*. 2023.

**Access.** [Quilt-1M](https://github.com/wisdomikezogwo/quilt1m)

### PathMMU — PathMMU Benchmark

| Field | Value |
|-------|-------|
| **Modality** | Pathology WSI + text |
| **Task** | Multimodal QA, reasoning |
| **Size** | Multi-source pathology VQA |
| **Access** | Open |
| **License** | Research |
| **Last verified** | 2026-06-01 |

**Description.** Benchmark for pathology visual question answering and multimodal reasoning.

**Primary reference.** Sun J, et al. *arXiv preprint*. 2024. [arXiv:2407.06505](https://arxiv.org/abs/2407.06505)

**Access.** [PathMMU](https://github.com/PathMMU-Benchmark/PathMMU)

<a id="ophthalmology"></a>


### Ophthalmology

### DRIVE — Digital Retinal Images for Vessel Extraction

| Field | Value |
|-------|-------|
| **Modality** | Fundus |
| **Task** | Vessel segmentation |
| **Size** | 40 images |
| **Access** | Open |
| **License** | DRIVE terms |
| **Last verified** | 2026-06-01 |

**Description.** Standard retinal vessel segmentation set.

**Primary reference.** Staal JJ, et al. *IEEE TMI*. 2004. [DOI:10.1109/TMI.2004.825627](https://doi.org/10.1109/TMI.2004.825627)

**Access.** [DRIVE](https://drive.grand-challenge.org/)

### STARE — Structured Analysis of the Retina

| Field | Value |
|-------|-------|
| **Modality** | Fundus |
| **Task** | Vessel segmentation |
| **Size** | 400+ images |
| **Access** | Open |
| **License** | STARE terms |
| **Last verified** | 2026-06-01 |

**Description.** Retinal vessel analysis with expert labels.

**Primary reference.** Hoover A, et al. *IEEE TMI*. 2000.

**Access.** [STARE](https://cecas.clemson.edu/~ahoover/stare/)

### IDRID — Indian Diabetic Retinopathy

| Field | Value |
|-------|-------|
| **Modality** | Fundus |
| **Task** | DR grading, segmentation |
| **Size** | 516 images |
| **Access** | Open |
| **License** | IDRID terms |
| **Last verified** | 2026-06-01 |

**Description.** Pixel-level DR lesions and disease grades.

**Primary reference.** Porwal P, et al. *Med Image Anal*. 2020.

**Access.** [IDRID](https://ieee-dataport.org/open-access/indian-diabetic-retinopathy-image-dataset-idrid)

### DIARETDB1 — Standard Diabetic Retinopathy

| Field | Value |
|-------|-------|
| **Modality** | Fundus |
| **Task** | DR detection |
| **Size** | 89 images |
| **Access** | Open |
| **License** | Research |
| **Last verified** | 2026-06-01 |

**Description.** Classic DR detection benchmark.

**Primary reference.** Kauppi T, et al. *LUT*. 2007.

**Access.** [DIARETDB1](https://www.it.lut.fi/project/imageret/diaretdb1)

### ISIC Archive — ISIC Archive

| Field | Value |
|-------|-------|
| **Modality** | Dermoscopy |
| **Task** | Skin lesion classification |
| **Size** | 23k+ images |
| **Access** | Open |
| **License** | CC-BY-NC |
| **Last verified** | 2026-06-01 |

**Description.** Melanoma and benign skin lesion archive.

**Primary reference.** ISIC Archive. [DOI:10.34970/350250](https://doi.org/10.34970/350250)

**Access.** [ISIC Archive](https://www.isic-archive.com/)

### EyePACS — EyePACS

| Field | Value |
|-------|-------|
| **Modality** | Fundus |
| **Task** | DR screening |
| **Size** | 3M+ images |
| **Access** | Registration |
| **License** | EyePACS terms |
| **Last verified** | 2026-06-01 |

**Description.** Large-scale diabetic retinopathy screening images.

**Primary reference.** EyePACS LLC.

**Access.** [EyePACS](http://www.eyepacs.com/data-analysis)

### FIRE — Fundus Image Registration

| Field | Value |
|-------|-------|
| **Modality** | Fundus |
| **Task** | Registration |
| **Size** | 134 pairs |
| **Access** | Open |
| **License** | FIRE terms |
| **Last verified** | 2026-06-01 |

**Description.** Retinal image pairs with ground truth.

**Primary reference.** FORTH-ICS.

**Access.** [FIRE](https://www.ics.forth.gr/cvrl/fire)

### REFUGE — REFUGE

| Field | Value |
|-------|-------|
| **Modality** | Fundus |
| **Task** | Glaucoma, segmentation |
| **Size** | 1,200 images |
| **Access** | Open |
| **License** | REFUGE terms |
| **Last verified** | 2026-06-01 |

**Description.** Optic disc/cup segmentation and glaucoma.

**Primary reference.** Orlando JI, et al. *Med Image Anal*. 2020.

**Access.** [REFUGE](https://refuge.grand-challenge.org/)

### APTOS — APTOS 2019 Blindness

| Field | Value |
|-------|-------|
| **Modality** | Fundus |
| **Task** | DR grading |
| **Size** | 3,662 images |
| **Access** | Open |
| **License** | Kaggle terms |
| **Last verified** | 2026-06-01 |

**Description.** Kaggle DR severity classification set.

**Primary reference.** APTOS 2019 Challenge.

**Access.** [APTOS](https://www.kaggle.com/c/aptos2019-blindness-detection)

<a id="cardiac"></a>


### Cardiac

### EchoNet-Dynamic — EchoNet-Dynamic

| Field | Value |
|-------|-------|
| **Modality** | Echo video |
| **Task** | EF prediction |
| **Size** | 10,030 videos |
| **Access** | Open |
| **License** | Research |
| **Last verified** | 2026-06-01 |

**Description.** Echocardiogram videos with EF labels.

**Primary reference.** Ouyang D, et al. *Nature*. 2020. [DOI:10.1038/s41586-020-2147-y](https://doi.org/10.1038/s41586-020-2147-y)

**Access.** [EchoNet-Dynamic](https://echonet.github.io/dynamic/)

### EchoNet-Pediatric — EchoNet-Pediatric

| Field | Value |
|-------|-------|
| **Modality** | Echo video |
| **Task** | Segmentation, EF |
| **Size** | 7,643 exams |
| **Access** | Open |
| **License** | Research |
| **Last verified** | 2026-06-01 |

**Description.** Pediatric echocardiography benchmark.

**Primary reference.** Garg R, et al. *JAMA Cardiol*. 2023.

**Access.** [EchoNet-Pediatric](https://echonet.github.io/pediatric/)

### AMRG Cardiac Atlas — AMRG Cardiac Atlas

| Field | Value |
|-------|-------|
| **Modality** | MRI |
| **Task** | Atlas |
| **Size** | Single atlas |
| **Access** | Open |
| **License** | Research |
| **Last verified** | 2026-06-01 |

**Description.** Labeled cardiac MRI from Auckland group.

**Primary reference.** Fonseca CG, et al. *J Cardiovasc Magn Reson*. 2011.

**Access.** [AMRG Cardiac Atlas](https://www.cardiacatlas.org/amrg/)

### CHD Atlas — Congenital Heart Disease Atlas

| Field | Value |
|-------|-------|
| **Modality** | MRI |
| **Task** | CHD modeling |
| **Size** | Multi-center |
| **Access** | Registration |
| **License** | Atlas terms |
| **Last verified** | 2026-06-01 |

**Description.** CHD MRI with clinical and models.

**Primary reference.** CHD Atlas Consortium.

**Access.** [CHD Atlas](https://www.cardiacatlas.org/)

### SCMR Consensus — SCMR Consensus Cardiac MRI

| Field | Value |
|-------|-------|
| **Modality** | MRI |
| **Task** | Segmentation |
| **Size** | 15 studies |
| **Access** | Open |
| **License** | SCMR terms |
| **Last verified** | 2026-06-01 |

**Description.** Multi-vendor cardiac MRI segmentation.

**Primary reference.** Suinesiaputra A, et al. *Med Image Anal*. 2014.

**Access.** [SCMR Consensus](https://www.synapse.org/#!Synapse:syn3193805/wiki/217789)

### Sunnybrook Cardiac — 2009 Cardiac MR LV Challenge

| Field | Value |
|-------|-------|
| **Modality** | MRI cine |
| **Task** | LV segmentation |
| **Size** | 45 studies |
| **Access** | Open |
| **License** | Challenge terms |
| **Last verified** | 2026-06-01 |

**Description.** Mixed pathology LV segmentation.

**Primary reference.** Radau P, et al. *MICCAI Challenge*. 2009.

**Access.** [Sunnybrook Cardiac](https://www.cardiacatlas.org/sunnybrook-cardiac-data/)

### York Cardiac MRI — York Cardiac MRI

| Field | Value |
|-------|-------|
| **Modality** | MRI |
| **Task** | Segmentation |
| **Size** | Multi-subject |
| **Access** | Open |
| **License** | Research |
| **Last verified** | 2026-06-01 |

**Description.** Cardiac MRI segmentation dataset.

**Primary reference.** Andreopoulos A, Tsotsos JK. *York University*.

**Access.** [York Cardiac MRI](https://www.cse.yorku.ca/~mridataset/)

### DETERMINE — DETERMINE Trial Imaging

| Field | Value |
|-------|-------|
| **Modality** | MRI |
| **Task** | Cardiovascular trial |
| **Size** | Clinical trial |
| **Access** | Registration |
| **License** | Trial DUA |
| **Last verified** | 2026-06-01 |

**Description.** CAD patients with MRI for defibrillator trials.

**Primary reference.** DETERMINE Study.

**Access.** [DETERMINE](https://www.cardiacatlas.org/determine/)

### MESA — Multi-Ethnic Study of Atherosclerosis

| Field | Value |
|-------|-------|
| **Modality** | CT, MRI |
| **Task** | Cardiovascular risk |
| **Size** | 6,500+ participants |
| **Access** | Registration |
| **License** | MESA terms |
| **Last verified** | 2026-06-01 |

**Description.** Population cardiovascular imaging cohort.

**Primary reference.** Bild DE, et al. *Am J Epidemiol*. 2002.

**Access.** [MESA](https://mesa-nhlbi.org/)

<a id="neuroimaging"></a>


### Neuroimaging

### OASIS — Open Access Series of Imaging Studies

| Field | Value |
|-------|-------|
| **Modality** | MRI |
| **Task** | Dementia, aging |
| **Size** | 600+ subjects |
| **Access** | Open |
| **License** | OASIS terms |
| **Last verified** | 2026-06-01 |

**Description.** Cross-sectional and longitudinal brain MRI.

**Primary reference.** Marcus DS, et al. *J Cogn Neurosci*. 2007.

**Access.** [OASIS](https://www.oasis-brains.org/)

### BraTS — Brain Tumor Segmentation Challenge

| Field | Value |
|-------|-------|
| **Modality** | MRI |
| **Task** | Tumor segmentation |
| **Size** | Annual cohorts |
| **Access** | Registration |
| **License** | Challenge terms |
| **Last verified** | 2026-06-01 |

**Description.** Glioma segmentation benchmark (updated yearly).

**Primary reference.** Menze BH, et al. *IEEE TMI*. 2015.

**Access.** [BraTS](https://www.synapse.org/brats)

### BraTS 2024 — BraTS 2024

| Field | Value |
|-------|-------|
| **Modality** | MRI, foundation tasks |
| **Task** | Segmentation, synthesis |
| **Size** | 2024 tasks |
| **Access** | Registration |
| **License** | Challenge terms |
| **Last verified** | 2026-06-01 |

**Description.** 2024 BraTS tasks including sub-Saharan cohorts.

**Primary reference.** Baid U, et al. *Scientific Data*. 2024.

**Access.** [BraTS 2024](https://www.synapse.org/brats2024)

### SynthStrip — SynthStrip

| Field | Value |
|-------|-------|
| **Modality** | MRI, CT, PET |
| **Task** | Skull stripping |
| **Size** | 600+ scans |
| **Access** | Open |
| **License** | Permissive |
| **Last verified** | 2026-06-01 |

**Description.** Brain extraction training data across modalities.

**Primary reference.** Hoopes A, et al. *NeuroImage*. 2022. [DOI:10.1016/j.neuroimage.2022.119474](https://doi.org/10.1016/j.neuroimage.2022.119474)

**Access.** [SynthStrip](https://w3id.org/synthstrip)

### OpenNeuro — OpenNeuro

| Field | Value |
|-------|-------|
| **Modality** | MRI, PET, EEG, etc. |
| **Task** | Neuroimaging archive |
| **Size** | 1,000+ datasets |
| **Access** | Open / mixed |
| **License** | Per-dataset |
| **Last verified** | 2026-06-01 |

**Description.** Open neuroimaging data repository.

**Primary reference.** Markiewicz CJ, et al. *Sci Data*. 2021. [DOI:10.1038/s41597-021-00870-6](https://doi.org/10.1038/s41597-021-00870-6)

**Access.** [OpenNeuro](https://openneuro.org/)

### UK Biobank Imaging — UK Biobank Imaging

| Field | Value |
|-------|-------|
| **Modality** | MRI, DXA |
| **Task** | Population imaging |
| **Size** | 100k+ planned |
| **Access** | Registration |
| **License** | UKB access |
| **Last verified** | 2026-06-01 |

**Description.** Population multimodal imaging substudy.

**Primary reference.** Miller KL, et al. *Nat Neurosci*. 2016.

**Access.** [UK Biobank Imaging](https://www.ukbiobank.ac.uk/enable-your-research/about-our-data/imaging-data)

### Calgary-Campinas — Calgary-Campinas Brain MR

| Field | Value |
|-------|-------|
| **Modality** | MRI |
| **Task** | Vendor harmonization |
| **Size** | 359 subjects |
| **Access** | Open |
| **License** | CC-BY |
| **Last verified** | 2026-06-01 |

**Description.** Multi-vendor brain MRI for harmonization.

**Primary reference.** Souza R, et al. *NeuroImage*. 2018.

**Access.** [Calgary-Campinas](https://sites.google.com/view/calgary-campinas-dataset/home)

### MSSEG — MICCAI MS Lesion Segmentation

| Field | Value |
|-------|-------|
| **Modality** | MRI |
| **Task** | MS lesion seg |
| **Size** | 30 subjects |
| **Access** | Open |
| **License** | Challenge |
| **Last verified** | 2026-06-01 |

**Description.** MS lesion segmentation challenge data.

**Primary reference.** Commowick O, et al. *MICCAI*. 2018.

**Access.** [MSSEG](https://www.nitrc.org/projects/msseg)

### CREMI — CREMI Challenge

| Field | Value |
|-------|-------|
| **Modality** | EM |
| **Task** | Neuron segmentation |
| **Size** | 6 volumes |
| **Access** | Open |
| **License** | CREMI terms |
| **Last verified** | 2026-06-01 |

**Description.** EM neural tissue segmentation.

**Primary reference.** Funke J, et al. *IEEE TMI*. 2018.

**Access.** [CREMI](https://cremi.org/data)

### SNEMI3D — SNEMI3D

| Field | Value |
|-------|-------|
| **Modality** | EM |
| **Task** | 3D neurite seg |
| **Size** | 6 volumes |
| **Access** | Open |
| **License** | SNEMI terms |
| **Last verified** | 2026-06-01 |

**Description.** 3D EM neurite segmentation benchmark.

**Primary reference.** Arganda-Carreras I, et al. *IEEE ISBI*. 2013.

**Access.** [SNEMI3D](https://snemi3d.grand-challenge.org/)

### SpineWeb — Annotated Spine CT

| Field | Value |
|-------|-------|
| **Modality** | CT |
| **Task** | Vertebra localization |
| **Size** | 125 patients |
| **Access** | Open |
| **License** | SpineWeb terms |
| **Last verified** | 2026-06-01 |

**Description.** Vertebra localization and segmentation.

**Primary reference.** Glocker B, et al. *MICCAI*. 2013.

**Access.** [SpineWeb](https://spineweb.digitalimaginggroup.ca/)

### IVDM3Seg — IVDM3Seg

| Field | Value |
|-------|-------|
| **Modality** | MRI |
| **Task** | IVD segmentation |
| **Size** | 24 datasets |
| **Access** | Open |
| **License** | Research |
| **Last verified** | 2026-06-01 |

**Description.** Intervertebral disc multi-modality MRI.

**Primary reference.** Zheng Y, et al. *IEEE JBHI*. 2021.

**Access.** [IVDM3Seg](https://ivdm3seg.weebly.com/data.html)

### DIADEM — DIADEM Challenge

| Field | Value |
|-------|-------|
| **Modality** | Microscopy |
| **Task** | Reconstruction |
| **Size** | Competition |
| **Access** | Open |
| **License** | Challenge |
| **Last verified** | 2026-06-01 |

**Description.** Axonal and dendritic morphology reconstruction.

**Primary reference.** Gillette TA, et al. *Neuron*. 2011.

**Access.** [DIADEM](https://diademchallenge.org/)

### CRIM13 — CRIM13 Mouse Behavior

| Field | Value |
|-------|-------|
| **Modality** | Video |
| **Task** | Action recognition |
| **Size** | 237 videos |
| **Access** | Open |
| **License** | Research |
| **Last verified** | 2026-06-01 |

**Description.** Mouse social behavior videos.

**Primary reference.** Burgos-Artizzu X, et al. *CVPR*. 2012.

**Access.** [CRIM13](https://www.vision.caltech.edu/Video_Datasets/CRIM13/)

<a id="dermatology"></a>


### Dermatology

### DERMOFIT — DERMOFIT Skin Cancer

| Field | Value |
|-------|-------|
| **Modality** | Dermoscopy |
| **Task** | Lesion classification |
| **Size** | 1,300 lesions |
| **Access** | Open |
| **License** | Research |
| **Last verified** | 2026-06-01 |

**Description.** Controlled dermoscopy with masks.

**Primary reference.** Fisher B, et al. *BMVC*. 2014.

**Access.** [DERMOFIT](http://homepages.inf.ed.ac.uk/rbf/DERMOFIT/)

### HAM10000 — HAM10000

| Field | Value |
|-------|-------|
| **Modality** | Dermoscopy |
| **Task** | 7-class lesion |
| **Size** | 10,015 images |
| **Access** | Open |
| **License** | CC-BY-NC |
| **Last verified** | 2026-06-01 |

**Description.** Dermatoscopic lesions with histology.

**Primary reference.** Tschandl P, et al. *Sci Data*. 2018. [DOI:10.1038/sdata.2018.161](https://doi.org/10.1038/sdata.2018.161)

**Access.** [HAM10000](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T)

### ISIC 2018 — ISIC 2018 Challenge

| Field | Value |
|-------|-------|
| **Modality** | Dermoscopy |
| **Task** | Segmentation, classification |
| **Size** | Challenge sets |
| **Access** | Open |
| **License** | Challenge terms |
| **Last verified** | 2026-06-01 |

**Description.** ISIC challenge tasks on skin lesions.

**Primary reference.** Codella NCF, et al. *arXiv preprint*. [1710.05006](https://arxiv.org/abs/1710.05006)

**Access.** [ISIC 2018](https://challenge.isic-archive.com/)

<a id="physiological-signals"></a>


## Physiological Signals

### PTB-XL — PTB-XL

| Field | Value |
|-------|-------|
| **Modality** | 12-lead ECG |
| **Task** | Classification |
| **Size** | 21,799 records |
| **Access** | Open |
| **License** | PhysioNet ODC |
| **Last verified** | 2026-06-01 |

**Description.** Large annotated 12-lead ECG database.

**Primary reference.** Wagner P, et al. *Sci Data*. 2020. [DOI:10.1038/s41597-020-0495-6](https://doi.org/10.1038/s41597-020-0495-6)

**Access.** [PTB-XL](https://physionet.org/content/ptb-xl/)

### PTB-XL+ — PTB-XL+

| Field | Value |
|-------|-------|
| **Modality** | ECG features |
| **Task** | Explainability |
| **Size** | Same cohort |
| **Access** | Open |
| **License** | PhysioNet ODC |
| **Last verified** | 2026-06-01 |

**Description.** PTB-XL with extensive feature annotations.

**Primary reference.** Strodthoff N, et al. *Physiol Meas*. 2023.

**Access.** [PTB-XL+](https://physionet.org/content/ptb-xl-plus/)

### MIMIC-IV-ECG — MIMIC-IV-ECG

| Field | Value |
|-------|-------|
| **Modality** | ECG waveforms |
| **Task** | Diagnosis, signals |
| **Size** | 800,000+ recordings |
| **Access** | Credentialed |
| **License** | PhysioNet DUA |
| **Last verified** | 2026-06-01 |

**Description.** ECG matched to MIMIC-IV hospitalizations.

**Primary reference.** Gow B, et al. *Circulation*. 2023.

**Access.** [MIMIC-IV-ECG](https://physionet.org/content/mimic-iv-ecg/)

### Symile-MIMIC — Symile-MIMIC

| Field | Value |
|-------|-------|
| **Modality** | ECG, CXR, labs |
| **Task** | Multimodal ICU |
| **Size** | 9,573 patients |
| **Access** | Credentialed |
| **License** | PhysioNet DUA |
| **Last verified** | 2026-06-01 |

**Description.** Multimodal ECG, chest X-ray, and labs.

**Primary reference.** Symile-MIMIC Contributors. *PhysioNet*. 2024.

**Access.** [Symile-MIMIC](https://physionet.org/content/symile-mimic/)

### SHDB-AF — Saitama Holter AF

| Field | Value |
|-------|-------|
| **Modality** | Holter ECG |
| **Task** | AF detection |
| **Size** | Holter records |
| **Access** | Open |
| **License** | PhysioNet ODC |
| **Last verified** | 2026-06-01 |

**Description.** Long-term Holter for atrial fibrillation.

**Primary reference.** Tsutsui Y, et al. *PhysioNet*. 2024.

**Access.** [SHDB-AF](https://physionet.org/content/shdb-af/)

### PhysioNet/CinC 2020 — PhysioNet Challenge 2020

| Field | Value |
|-------|-------|
| **Modality** | ECG |
| **Task** | Classification |
| **Size** | Multiple |
| **Access** | Open |
| **License** | Challenge |
| **Last verified** | 2026-06-01 |

**Description.** Classification of 12-lead ECG diagnoses.

**Primary reference.** Reyna MA, et al. *CinC*. 2020.

**Access.** [PhysioNet/CinC 2020](https://physionet.org/content/challenge-2020/)

### WESAD — WESAD

| Field | Value |
|-------|-------|
| **Modality** | Wearable sensors |
| **Task** | Stress detection |
| **Size** | 15 subjects |
| **Access** | Open |
| **License** | Research |
| **Last verified** | 2026-06-01 |

**Description.** Wearable stress and affect dataset.

**Primary reference.** Schmidt P, et al. *UCI / arXiv*. 2018.

**Access.** [WESAD](https://archive.ics.uci.edu/dataset/465/wesad+wearable+stress+and+affect+detection)

### PPG-DaLiA — PPG-DaLiA

| Field | Value |
|-------|-------|
| **Modality** | PPG, IMU |
| **Task** | Activity, HR |
| **Size** | 15 subjects |
| **Access** | Open |
| **License** | Research |
| **Last verified** | 2026-06-01 |

**Description.** PPG during daily activities.

**Primary reference.** Reiss A, et al. *ACM IMWUT*. 2019.

**Access.** [PPG-DaLiA](https://archive.ics.uci.edu/dataset/495/ppg+dalia)

### BIDMC PPG — BIDMC PPG and Respiration

| Field | Value |
|-------|-------|
| **Modality** | PPG, respiration |
| **Task** | Waveform ML |
| **Size** | 53 records |
| **Access** | Open |
| **License** | PhysioNet ODC |
| **Last verified** | 2026-06-01 |

**Description.** PPG and respiration from ICU patients.

**Primary reference.** Pimentel MA, et al. *Sci Rep*. 2016.

**Access.** [BIDMC PPG](https://physionet.org/content/bidmc/)

### MIMIC-III Waveform — MIMIC-III Waveform Database

| Field | Value |
|-------|-------|
| **Modality** | ICU waveforms |
| **Task** | Forecasting |
| **Size** | ~67k records |
| **Access** | Credentialed |
| **License** | PhysioNet DUA |
| **Last verified** | 2026-06-01 |

**Description.** High-resolution ICU waveform data.

**Primary reference.** Moody GB, Mark RG. *PhysioNet*.

**Access.** [MIMIC-III Waveform](https://physionet.org/content/mimic3wdb/)

### Sleep-EDF — Sleep-EDF Expanded

| Field | Value |
|-------|-------|
| **Modality** | EEG, EOG |
| **Task** | Sleep staging |
| **Size** | 197 whole-night |
| **Access** | Open |
| **License** | PhysioNet ODC |
| **Last verified** | 2026-06-01 |

**Description.** Sleep staging benchmark.

**Primary reference.** Goldberger AL, et al. *PhysioNet*. 2000.

**Access.** [Sleep-EDF](https://physionet.org/content/sleep-edfx/)

### CHB-MIT — CHB-MIT Scalp EEG

| Field | Value |
|-------|-------|
| **Modality** | EEG |
| **Task** | Seizure detection |
| **Size** | 24 subjects |
| **Access** | Open |
| **License** | PhysioNet ODC |
| **Last verified** | 2026-06-01 |

**Description.** Pediatric seizure EEG corpus.

**Primary reference.** Shoeb A, Guttag J. *PhysioNet*. 2010.

**Access.** [CHB-MIT](https://physionet.org/content/chbmit/)

### TUAB — Temple University Hospital EEG Abnormal

| Field | Value |
|-------|-------|
| **Modality** | EEG |
| **Task** | Abnormality detection |
| **Size** | Large corpus |
| **Access** | Open |
| **License** | TUH EEG license |
| **Last verified** | 2026-06-01 |

**Description.** Abnormal vs normal EEG benchmark.

**Primary reference.** Lopez S, et al. *IEEE EMBC*. 2017.

**Access.** [TUAB](https://isip.piconepress.com/projects/tuh_eeg/)

### UBFC-rPPG — UBFC-rPPG

| Field | Value |
|-------|-------|
| **Modality** | Video, PPG |
| **Task** | rPPG |
| **Size** | 42 subjects |
| **Access** | Open |
| **License** | Research |
| **Last verified** | 2026-06-01 |

**Description.** Remote PPG from facial video.

**Primary reference.** Bobbia S, et al. *IEEE FG*. 2019.

**Access.** [UBFC-rPPG](https://sites.google.com/view/ybenezeth/ubfcrppg)

### MIMIC PERform AF — MIMIC PERform AF

| Field | Value |
|-------|-------|
| **Modality** | ECG |
| **Task** | AF detection |
| **Size** | Training subset |
| **Access** | Credentialed |
| **License** | PhysioNet DUA |
| **Last verified** | 2026-06-01 |

**Description.** AF detection from MIMIC waveforms.

**Primary reference.** Perez MV, et al. *NPJ Digit Med*. 2023.

**Access.** [MIMIC PERform AF](https://physionet.org/content/mimic-perform-af/)

<a id="electronic-health-records"></a>


## Electronic Health Records

### MIMIC-III — MIMIC-III Clinical Database

| Field | Value |
|-------|-------|
| **Modality** | EHR |
| **Task** | ICU research |
| **Size** | 40,000+ patients |
| **Access** | Credentialed |
| **License** | PhysioNet DUA |
| **Last verified** | 2026-06-01 |

**Description.** De-identified ICU EHR through 2012.

**Primary reference.** Johnson AEW, et al. *Sci Data*. 2016. [DOI:10.1038/sdata201635](https://doi.org/10.1038/sdata201635)

**Access.** [MIMIC-III](https://physionet.org/content/mimiciii/)

### MIMIC-IV — MIMIC-IV

| Field | Value |
|-------|-------|
| **Modality** | EHR |
| **Task** | ICU + ED research |
| **Size** | 364,627 admissions |
| **Access** | Credentialed |
| **License** | PhysioNet DUA |
| **Last verified** | 2026-06-01 |

**Description.** Updated ICU/ED/hospital EHR through 2019.

**Primary reference.** Johnson AEW, et al. *Sci Data*. 2023. [DOI:10.1038/s41597-022-01899-3](https://doi.org/10.1038/s41597-022-01899-3)

**Access.** [MIMIC-IV](https://physionet.org/content/mimiciv/)

### MIMIC-IV-Note — MIMIC-IV-Note

| Field | Value |
|-------|-------|
| **Modality** | Clinical notes |
| **Task** | NLP |
| **Size** | 331,794 notes |
| **Access** | Credentialed |
| **License** | PhysioNet DUA |
| **Last verified** | 2026-06-01 |

**Description.** De-identified discharge and radiology notes.

**Primary reference.** Johnson AEW, et al. *PhysioNet*. 2023.

**Access.** [MIMIC-IV-Note](https://physionet.org/content/mimic-iv-note/)

### eICU-CRD — eICU Collaborative Research Database

| Field | Value |
|-------|-------|
| **Modality** | EHR |
| **Task** | Multi-center ICU |
| **Size** | 200,000+ admissions |
| **Access** | Credentialed |
| **License** | PhysioNet DUA |
| **Last verified** | 2026-06-01 |

**Description.** Multi-center ICU EHR across the US.

**Primary reference.** Pollard TJ, et al. *Sci Data*. 2018. [DOI:10.1038/sdata2018178](https://doi.org/10.1038/sdata2018178)

**Access.** [eICU-CRD](https://physionet.org/content/eicu-crd/)

### HiRID — High Time Resolution ICU Dataset

| Field | Value |
|-------|-------|
| **Modality** | EHR, waveforms |
| **Task** | Forecasting |
| **Size** | 33,000+ admissions |
| **Access** | Registration |
| **License** | HiRID DUA |
| **Last verified** | 2026-06-01 |

**Description.** Swiss ICU high-resolution data.

**Primary reference.** Hyland SL, et al. *Sci Data*. 2020.

**Access.** [HiRID](https://physionet.org/content/hirid/)

### AmsterdamUMCdb — AmsterdamUMCdb

| Field | Value |
|-------|-------|
| **Modality** | EHR |
| **Task** | ICU research |
| **Size** | 23,000+ admissions |
| **Access** | Registration |
| **License** | Amsterdam UMC DUA |
| **Last verified** | 2026-06-01 |

**Description.** European ICU database from Amsterdam.

**Primary reference.** Thoral PJ, et al. *Crit Care*. 2021.

**Access.** [AmsterdamUMCdb](https://amsterdammedicaldatascience.nl/)

### OMOP CDM — OMOP Common Data Model

| Field | Value |
|-------|-------|
| **Modality** | EHR (standardized) |
| **Task** | Observational research |
| **Size** | Network-dependent |
| **Access** | DUA / varies |
| **License** | OMOP license |
| **Last verified** | 2026-06-01 |

**Description.** Standardized observational health data model.

**Primary reference.** OHDSI Community. *J Am Med Inform Assoc*. 2015.

**Access.** [OMOP CDM](https://www.ohdsi.org/data-standardization/)

### Clinical Concept Embeddings — Clinical ML Embeddings

| Field | Value |
|-------|-------|
| **Modality** | Claims + notes |
| **Task** | Representation learning |
| **Size** | Millions of patients |
| **Access** | Open (code) |
| **License** | MIT license |
| **Last verified** | 2026-06-01 |

**Description.** Embeddings from claims and clinical text.

**Primary reference.** Choi Y, et al. *AMIA*. 2016.

**Access.** [Clinical Concept Embeddings](https://github.com/clinicalml/embeddings)

### Graph of Medicine — Graph of Medicine co-occurrence

| Field | Value |
|-------|-------|
| **Modality** | EHR co-occurrence |
| **Task** | Network analysis |
| **Size** | 260k patients |
| **Access** | Open |
| **License** | Dryad |
| **Last verified** | 2026-06-01 |

**Description.** Co-occurrence statistics from clinical narratives.

**Primary reference.** Finlayson SG, et al. *Sci Data*. 2014. [DOI:10.1038/sdata201432](https://doi.org/10.1038/sdata201432)

**Access.** [Graph of Medicine](https://datadryad.org/stash/dataset/doi:10.5061/dryad.jp917)

### cui2vec — cui2vec

| Field | Value |
|-------|-------|
| **Modality** | Concept embeddings |
| **Task** | NLP features |
| **Size** | 108k concepts |
| **Access** | Open |
| **License** | MIT |
| **Last verified** | 2026-06-01 |

**Description.** Embeddings for UMLS concepts from multi-source data.

**Primary reference.** Beam A, et al. *JAMIA Open*. 2020.

**Access.** [cui2vec](https://github.com/beamandrew/cui2vec)

### n2c2 NLP — n2c2 Shared Tasks

| Field | Value |
|-------|-------|
| **Modality** | Clinical notes |
| **Task** | NLP tasks |
| **Size** | Task-dependent |
| **Access** | DUA |
| **License** | n2c2 DUA |
| **Last verified** | 2026-06-01 |

**Description.** Harvard n2c2 de-identified clinical NLP corpora.

**Primary reference.** n2c2 Consortium.

**Access.** [n2c2 NLP](https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/)

### MIMIC-IV-ED — MIMIC-IV-ED

| Field | Value |
|-------|-------|
| **Modality** | ED EHR |
| **Task** | Emergency research |
| **Size** | 425,000+ visits |
| **Access** | Credentialed |
| **License** | PhysioNet DUA |
| **Last verified** | 2026-06-01 |

**Description.** Emergency department subset of MIMIC-IV.

**Primary reference.** Johnson AEW, et al. *PhysioNet*. 2023.

**Access.** [MIMIC-IV-ED](https://physionet.org/content/mimic-iv-ed/)

<a id="clinical-nlp--literature"></a>


## Clinical NLP & Literature

### PMC Open Access — PMC Open Access Subset

| Field | Value |
|-------|-------|
| **Modality** | Full text |
| **Task** | IR, NLP |
| **Size** | Millions of articles |
| **Access** | Open (subset) |
| **License** | PMC license |
| **Last verified** | 2026-06-01 |

**Description.** Open-access full-text biomedical literature.

**Primary reference.** PMC. NLM.

**Access.** [PMC Open Access](https://www.ncbi.nlm.nih.gov/pmc/tools/openftlist/)

### PubMed 200k RCT — PubMed 200k RCT

| Field | Value |
|-------|-------|
| **Modality** | Abstracts |
| **Task** | Sentence classification |
| **Size** | 200k abstracts |
| **Access** | Open |
| **License** | MIT |
| **Last verified** | 2026-06-01 |

**Description.** RCT abstracts with sentence labels.

**Primary reference.** Dernoncourt F, et al. *arXiv preprint*. [1710.06071](https://arxiv.org/abs/1710.06071)

**Access.** [PubMed 200k RCT](https://github.com/Franck-Dernoncourt/pubmed-rct)

### LitCovid — LitCovid

| Field | Value |
|-------|-------|
| **Modality** | Literature |
| **Task** | COVID IR |
| **Size** | Curated set |
| **Access** | Open |
| **License** | NLM |
| **Last verified** | 2026-06-01 |

**Description.** COVID-19 literature hub.

**Primary reference.** Chen Q, et al. *Nature*. 2021.

**Access.** [LitCovid](https://www.ncbi.nlm.nih.gov/research/coronavirus/)

### CliCR — CliCR

| Field | Value |
|-------|-------|
| **Modality** | Clinical case reports |
| **Task** | Reading comprehension |
| **Size** | ~100k queries |
| **Access** | Open |
| **License** | Research |
| **Last verified** | 2026-06-01 |

**Description.** Gap-filling queries on clinical case reports.

**Primary reference.** Suster S, et al. *ACL*. 2018.

**Access.** [CliCR](https://github.com/clips/clicr)

### CBLUE — CBLUE Benchmark

| Field | Value |
|-------|-------|
| **Modality** | Chinese clinical text |
| **Task** | NLP benchmark |
| **Size** | 8 tasks |
| **Access** | Open |
| **License** | CBLUE terms |
| **Last verified** | 2026-06-01 |

**Description.** Chinese biomedical language understanding benchmark.

**Primary reference.** Zhang N, et al. *arXiv preprint*. [2106.08087](https://arxiv.org/abs/2106.08087)

**Access.** [CBLUE](https://github.com/CBLUEbenchmark/CBLUE)

### CHIP — CHIP Challenges

| Field | Value |
|-------|-------|
| **Modality** | Chinese EHR |
| **Task** | NLP tasks |
| **Size** | Annual |
| **Access** | Registration |
| **License** | CHIP terms |
| **Last verified** | 2026-06-01 |

**Description.** China health information processing shared tasks.

**Primary reference.** CHIP Conference.

**Access.** [CHIP](https://chip.cips-cl.org/)

### i2b2 2010 — i2b2/VA Challenge 2010

| Field | Value |
|-------|-------|
| **Modality** | De-identified notes |
| **Task** | Concept extraction |
| **Size** | De-id notes |
| **Access** | DUA |
| **License** | i2b2 DUA |
| **Last verified** | 2026-06-01 |

**Description.** Medication and problem entity extraction.

**Primary reference.** Uzuner O, et al. *JAMIA*. 2011.

**Access.** [i2b2 2010](https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/)

### TREC Clinical Decision Support — TREC CDS Tracks

| Field | Value |
|-------|-------|
| **Modality** | Literature + EHR |
| **Task** | Clinical IR |
| **Size** | 2014–2017 tracks |
| **Access** | Open |
| **License** | TREC terms |
| **Last verified** | 2026-06-01 |

**Description.** Clinical decision support retrieval benchmarks.

**Primary reference.** Roberts K, et al. *TREC*.

**Access.** [TREC Clinical Decision Support](http://www.trec-cds.org/)

### CORD-19 — COVID-19 Open Research Dataset

| Field | Value |
|-------|-------|
| **Modality** | Literature |
| **Task** | COVID NLP |
| **Size** | 400k+ papers |
| **Access** | Open |
| **License** | CC0 |
| **Last verified** | 2026-06-01 |

**Description.** Scholarly articles for COVID-19 research.

**Primary reference.** Wang LL, et al. *arXiv preprint*. [2004.10706](https://arxiv.org/abs/2004.10706)

**Access.** [CORD-19](https://allenai.org/data/cord-19)

### BioASQ — BioASQ

| Field | Value |
|-------|-------|
| **Modality** | Literature |
| **Task** | QA, IR |
| **Size** | Annual |
| **Access** | Open |
| **License** | BioASQ terms |
| **Last verified** | 2026-06-01 |

**Description.** Biomedical semantic indexing and QA challenge.

**Primary reference.** Tsatsaronis G, et al. *J Biomed Semant*. 2015.

**Access.** [BioASQ](http://bioasq.org/)

### TORGO — TORGO Dysarthric Speech

| Field | Value |
|-------|-------|
| **Modality** | Speech audio |
| **Task** | ASR |
| **Size** | Speakers with CP/ALS |
| **Access** | Open |
| **License** | Research |
| **Last verified** | 2026-06-01 |

**Description.** Dysarthric speech acoustic and articulatory data.

**Primary reference.** Rudzicz F, et al. *Computer Speech & Language*. 2012.

**Access.** [TORGO](http://www.cs.toronto.edu/~complingweb/data/TORGO/torgo.html)

### NKI-CCRT — NKI-CCRT Corpus

| Field | Value |
|-------|-------|
| **Modality** | Speech |
| **Task** | Intelligibility |
| **Size** | 55 patients |
| **Access** | Registration |
| **License** | Scientific use |
| **Last verified** | 2026-06-01 |

**Description.** Head and neck cancer speech before/after CCRT.

**Primary reference.** Rietveld T, et al. *LREC*. 2012.

**Access.** [NKI-CCRT](https://www.ru.nl/languageandspeech/)

### Interspeech Atypical — Interspeech Atypical Speech

| Field | Value |
|-------|-------|
| **Modality** | Speech |
| **Task** | Emotion classification |
| **Size** | EMOTASS |
| **Access** | Registration |
| **License** | Challenge |
| **Last verified** | 2026-06-01 |

**Description.** Atypical speech emotion sub-challenge.

**Primary reference.** Schuller B, et al. *Interspeech*. 2018.

**Access.** [Interspeech Atypical](http://emotion-research.net/sigs/speech-sig/is18-compare)

### Interspeech Autism — Interspeech Autism Sub-Challenge

| Field | Value |
|-------|-------|
| **Modality** | Speech |
| **Task** | Classification |
| **Size** | CPSD subset |
| **Access** | Registration |
| **License** | Challenge |
| **Last verified** | 2026-06-01 |

**Description.** Autism speech sub-challenge on CPSD.

**Primary reference.** Schuller B, et al. *Interspeech*. 2013.

**Access.** [Interspeech Autism](http://emotion-research.net/sigs/speech-sig/is13-compare)

<a id="public-health--population-data"></a>


## Public Health & Population Data

### CDC Data Catalog — CDC Data Catalog

| Field | Value |
|-------|-------|
| **Modality** | Public health |
| **Task** | Epidemiology |
| **Size** | Many datasets |
| **Access** | Open |
| **License** | US public domain |
| **Last verified** | 2026-06-01 |

**Description.** CDC open data across domains.

**Primary reference.** CDC.

**Access.** [CDC Data Catalog](https://data.cdc.gov/browse)

### Medicare Data — CMS Medicare Data

| Field | Value |
|-------|-------|
| **Modality** | Claims, quality |
| **Task** | Health services |
| **Size** | National |
| **Access** | Open / restricted |
| **License** | CMS terms |
| **Last verified** | 2026-06-01 |

**Description.** Medicare provider and utilization data.

**Primary reference.** CMS.

**Access.** [Medicare Data](https://data.cms.gov/)

### Texas Inpatient PUDF — Texas Public Use Inpatient

| Field | Value |
|-------|-------|
| **Modality** | Claims |
| **Task** | Utilization |
| **Size** | 11M+ visits 2006–2009 |
| **Access** | Registration |
| **License** | Texas DSHS |
| **Last verified** | 2026-06-01 |

**Description.** Texas inpatient discharge public use file.

**Primary reference.** Texas DSHS.

**Access.** [Texas Inpatient PUDF](https://www.dshs.texas.gov/thcic/hospitals/Inpatientpudf.shtm)

### HCUP — Healthcare Cost and Utilization Project

| Field | Value |
|-------|-------|
| **Modality** | Claims |
| **Task** | Outcomes research |
| **Size** | National samples |
| **Access** | Purchase / DUA |
| **License** | AHRQ terms |
| **Last verified** | 2026-06-01 |

**Description.** US hospital discharge databases.

**Primary reference.** AHRQ.

**Access.** [HCUP](https://www.hcup-us.ahrq.gov/)

### SEER — SEER Program

| Field | Value |
|-------|-------|
| **Modality** | Cancer registry |
| **Task** | Survival, epidemiology |
| **Size** | Population |
| **Access** | Registration |
| **License** | SEER terms |
| **Last verified** | 2026-06-01 |

**Description.** US cancer incidence and survival.

**Primary reference.** Surveillance, Epidemiology, and End Results.

**Access.** [SEER](https://seer.cancer.gov/)

### WHO GHO — WHO Global Health Observatory

| Field | Value |
|-------|-------|
| **Modality** | Global health |
| **Task** | Indicators |
| **Size** | Global |
| **Access** | Open |
| **License** | WHO terms |
| **Last verified** | 2026-06-01 |

**Description.** WHO global health indicators.

**Primary reference.** WHO.

**Access.** [WHO GHO](https://www.who.int/data/gho)

### MIMIC-IV Oncology — MIMIC-IV Oncology Module

| Field | Value |
|-------|-------|
| **Modality** | EHR + oncology |
| **Task** | Cancer outcomes |
| **Size** | Subset of MIMIC-IV |
| **Access** | Credentialed |
| **License** | PhysioNet DUA |
| **Last verified** | 2026-06-01 |

**Description.** Oncology concepts in MIMIC-IV.

**Primary reference.** Johnson AEW, et al. *PhysioNet*. 2024.

**Access.** [MIMIC-IV Oncology](https://physionet.org/content/mimic-iv-oncology/)

### Synthea — Synthea Synthetic Patients

| Field | Value |
|-------|-------|
| **Modality** | Synthetic EHR |
| **Task** | Simulation |
| **Size** | Unlimited |
| **Access** | Open |
| **License** | Apache 2.0 |
| **Last verified** | 2026-06-01 |

**Description.** Synthetic patient records via simulation.

**Primary reference.** Walonoski J, et al. *JAMIA Open*. 2018.

**Access.** [Synthea](https://github.com/synthetichealth/synthea)

<a id="challenges--benchmarks"></a>


## Challenges & Benchmarks

### Grand Challenge — Grand-Challenge.org

| Field | Value |
|-------|-------|
| **Modality** | Multi-modality |
| **Task** | Benchmarks |
| **Size** | 92+ challenges |
| **Access** | Open / mixed |
| **License** | Per-challenge |
| **Last verified** | 2026-06-01 |

**Description.** Biomedical imaging challenge platform.

**Primary reference.** Grand Challenge Team.

**Access.** [Grand Challenge](https://grand-challenge.org/)

### DREAM Challenges — DREAM Challenges

| Field | Value |
|-------|-------|
| **Modality** | Multi-omics |
| **Task** | Systems biology |
| **Size** | Many |
| **Access** | Open / mixed |
| **License** | Per-challenge |
| **Last verified** | 2026-06-01 |

**Description.** Community challenge series in translational medicine.

**Primary reference.** Saez-Rodriguez J, et al. *Nat Methods*. 2016.

**Access.** [DREAM Challenges](https://dreamchallenges.org/)

### VISCERAL — VISCERAL Challenge

| Field | Value |
|-------|-------|
| **Modality** | CT, MR |
| **Task** | Anatomy segmentation |
| **Size** | Benchmark |
| **Access** | Closed |
| **License** | Archive |
| **Last verified** | 2026-06-01 |

**Description.** Multi-modality anatomy segmentation benchmark.

**Primary reference.** Jimenez-del-Toro O, et al. *IEEE TMI*. 2016.

**Access.** [VISCERAL](http://www.visceral.eu/)

### Kaggle DR — Kaggle Diabetic Retinopathy

| Field | Value |
|-------|-------|
| **Modality** | Fundus |
| **Task** | DR grading |
| **Size** | 35k+ images |
| **Access** | Open |
| **License** | Kaggle |
| **Last verified** | 2026-06-01 |

**Description.** Classic Kaggle DR detection competition data.

**Primary reference.** Kaggle.

**Access.** [Kaggle DR](https://www.kaggle.com/c/diabetic-retinopathy-detection)

### Kaggle Cervical — Intel Mobile ODT Cervical

| Field | Value |
|-------|-------|
| **Modality** | Cervical imaging |
| **Task** | Classification |
| **Size** | Kaggle set |
| **Access** | Open |
| **License** | Kaggle |
| **Last verified** | 2026-06-01 |

**Description.** Cervical cancer screening imaging challenge.

**Primary reference.** Kaggle.

**Access.** [Kaggle Cervical](https://www.kaggle.com/c/intel-mobileodt-cervical-cancer-screening)

### BraTS Challenge — BraTS

| Field | Value |
|-------|-------|
| **Modality** | MRI |
| **Task** | Segmentation |
| **Size** | Annual |
| **Access** | Registration |
| **License** | Challenge |
| **Last verified** | 2026-06-01 |

**Description.** Brain tumor segmentation challenge series.

**Primary reference.** Menze BH, et al.

**Access.** [BraTS Challenge](https://braintumorsegmentation.org/)

### MICCAI Challenges — MICCAI Satellite Challenges

| Field | Value |
|-------|-------|
| **Modality** | Medical imaging |
| **Task** | Various |
| **Size** | Annual |
| **Access** | Mixed |
| **License** | Per-event |
| **Last verified** | 2026-06-01 |

**Description.** MICCAI workshop challenge listings.

**Primary reference.** MICCAI Society.

**Access.** [MICCAI Challenges](https://www.miccai.org/)

### ISBI Challenges — ISBI Challenges

| Field | Value |
|-------|-------|
| **Modality** | Biomedical imaging |
| **Task** | Various |
| **Size** | Annual |
| **Access** | Mixed |
| **License** | Per-event |
| **Last verified** | 2026-06-01 |

**Description.** IEEE ISBI challenge programs.

**Primary reference.** IEEE ISBI.

**Access.** [ISBI Challenges](https://biomedicalimaging.org/)

### CRC — Continuous Registration Challenge

| Field | Value |
|-------|-------|
| **Modality** | CT |
| **Task** | Registration |
| **Size** | 7 datasets |
| **Access** | Open |
| **License** | Challenge |
| **Last verified** | 2026-06-01 |

**Description.** Pulmonary and brain registration benchmark.

**Primary reference.** Hering A, et al. *WBIR*. 2018.

**Access.** [CRC](https://continuousregistration.grand-challenge.org/)

### Kaggle Seizure — Kaggle Seizure Prediction

| Field | Value |
|-------|-------|
| **Modality** | iEEG |
| **Task** | Seizure prediction |
| **Size** | Competition data |
| **Access** | Open |
| **License** | Kaggle |
| **Last verified** | 2026-06-01 |

**Description.** Intracranial EEG seizure prediction.

**Primary reference.** Kaggle.

**Access.** [Kaggle Seizure](https://www.kaggle.com/c/seizure-prediction)

### RSNA Pneumonia — RSNA Pneumonia Detection

| Field | Value |
|-------|-------|
| **Modality** | CXR |
| **Task** | Detection |
| **Size** | 26,684 images |
| **Access** | Open |
| **License** | RSNA |
| **Last verified** | 2026-06-01 |

**Description.** RSNA pneumonia detection challenge.

**Primary reference.** RSNA.

**Access.** [RSNA Pneumonia](https://www.kaggle.com/c/rsna-pneumonia-detection-challenge)

### RSNA ICH — RSNA Intracranial Hemorrhage

| Field | Value |
|-------|-------|
| **Modality** | CT |
| **Task** | Detection |
| **Size** | 25k+ scans |
| **Access** | Open |
| **License** | RSNA |
| **Last verified** | 2026-06-01 |

**Description.** ICH detection in CT.

**Primary reference.** Flanders AE, et al. *Radiology*. 2020.

**Access.** [RSNA ICH](https://www.rsna.org/education/ai-resources-and-training/ai-image-challenge)

### LUNA16 — LUNA16

| Field | Value |
|-------|-------|
| **Modality** | CT |
| **Task** | Nodule detection |
| **Size** | 888 scans |
| **Access** | Open |
| **License** | LUNA terms |
| **Last verified** | 2026-06-01 |

**Description.** LIDC-derived nodule detection challenge.

**Primary reference.** Setio AAA, et al. *Med Image Anal*. 2017.

**Access.** [LUNA16](https://luna16.grand-challenge.org/)

### CHAOS — CHAOS Challenge

| Field | Value |
|-------|-------|
| **Modality** | CT, MRI |
| **Task** | Abdominal seg |
| **Size** | Combined |
| **Access** | Open |
| **License** | CHAOS |
| **Last verified** | 2026-06-01 |

**Description.** Combined abdominal organ segmentation.

**Primary reference.** Kavur AE, et al. *Med Image Anal*. 2021.

**Access.** [CHAOS](https://chaos.grand-challenge.org/)

### Medical Segmentation Decathlon — MSD

| Field | Value |
|-------|-------|
| **Modality** | CT, MRI |
| **Task** | Multi-organ seg |
| **Size** | 10 tasks |
| **Access** | Open |
| **License** | MSD terms |
| **Last verified** | 2026-06-01 |

**Description.** Decathlon-style segmentation tasks.

**Primary reference.** Simpson AL, et al. *arXiv preprint*. [1902.09063](https://arxiv.org/abs/1902.09063)

**Access.** [Medical Segmentation Decathlon](http://medicaldecathlon.com/)

### FeTA — Fetal Brain Tissue Annotation

| Field | Value |
|-------|-------|
| **Modality** | MRI |
| **Task** | Fetal brain seg |
| **Size** | 80 scans |
| **Access** | Open |
| **License** | FeTA |
| **Last verified** | 2026-06-01 |

**Description.** Fetal brain tissue segmentation.

**Primary reference.** Payette K, et al. *NeuroImage*. 2021.

**Access.** [FeTA](https://feta.grand-challenge.org/)

### Seg.A. — Seg.A. Cardiac MRI

| Field | Value |
|-------|-------|
| **Modality** | MRI |
| **Task** | Segmentation |
| **Size** | Multi-vendor |
| **Access** | Open |
| **License** | Challenge |
| **Last verified** | 2026-06-01 |

**Description.** Cardiac MRI segmentation across vendors.

**Primary reference.** Zhuang X, et al. *MICCAI*. 2023.

**Access.** [Seg.A.](https://seg-a.grand-challenge.org/)

### COVID-19 CT — COVID-19 CT Segmentation

| Field | Value |
|-------|-------|
| **Modality** | CT |
| **Task** | Infection seg |
| **Size** | Multiple collections |
| **Access** | Open |
| **License** | Various |
| **Last verified** | 2026-06-01 |

**Description.** COVID lung infection segmentation collections.

**Primary reference.** Multiple authors. See TCIA COVID collections.

**Access.** [COVID-19 CT](https://www.cancerimagingarchive.net/collections/)

<a id="tabular--classic-ml"></a>


## Tabular / Classic ML

### UCI Liver Disorders — Liver Disorders

| Field | Value |
|-------|-------|
| **Modality** | Tabular |
| **Task** | Diagnosis |
| **Size** | 345 instances |
| **Access** | Open |
| **License** | UCI |
| **Last verified** | 2026-06-01 |

**Description.** BUPA liver disorders dataset.

**Primary reference.** UCI ML Repository.

**Access.** [UCI Liver Disorders](https://archive.ics.uci.edu/dataset/58/liver+disorders)

### UCI Thyroid Disease — Thyroid Disease

| Field | Value |
|-------|-------|
| **Modality** | Tabular |
| **Task** | Diagnosis |
| **Size** | 3,772 instances |
| **Access** | Open |
| **License** | UCI |
| **Last verified** | 2026-06-01 |

**Description.** Thyroid disease records.

**Primary reference.** UCI ML Repository.

**Access.** [UCI Thyroid Disease](https://archive.ics.uci.edu/dataset/102/thyroid+disease)

### UCI Breast Cancer — Breast Cancer Wisconsin

| Field | Value |
|-------|-------|
| **Modality** | Tabular |
| **Task** | Classification |
| **Size** | 699 instances |
| **Access** | Open |
| **License** | UCI |
| **Last verified** | 2026-06-01 |

**Description.** Breast cancer diagnostic features.

**Primary reference.** UCI ML Repository.

**Access.** [UCI Breast Cancer](https://archive.ics.uci.edu/dataset/14/breast+cancer)

### UCI Heart Disease — Heart Disease

| Field | Value |
|-------|-------|
| **Modality** | Tabular |
| **Task** | Classification |
| **Size** | 303 instances |
| **Access** | Open |
| **License** | UCI |
| **Last verified** | 2026-06-01 |

**Description.** Cleveland heart disease dataset.

**Primary reference.** UCI ML Repository.

**Access.** [UCI Heart Disease](https://archive.ics.uci.edu/dataset/45/heart+disease)

### UCI Lymphography — Lymphography

| Field | Value |
|-------|-------|
| **Modality** | Tabular |
| **Task** | Classification |
| **Size** | 148 instances |
| **Access** | Open |
| **License** | UCI |
| **Last verified** | 2026-06-01 |

**Description.** Lymphography domain classification.

**Primary reference.** UCI ML Repository.

**Access.** [UCI Lymphography](https://archive.ics.uci.edu/dataset/63/lymphography)

### UCI Parkinsons — Parkinsons

| Field | Value |
|-------|-------|
| **Modality** | Tabular |
| **Task** | Classification |
| **Size** | 197 instances |
| **Access** | Open |
| **License** | UCI |
| **Last verified** | 2026-06-01 |

**Description.** Voice features for Parkinson's detection.

**Primary reference.** UCI ML Repository.

**Access.** [UCI Parkinsons](https://archive.ics.uci.edu/dataset/174/parkinsons)

### UCI Parkinsons Telemonitoring — Parkinsons Telemonitoring

| Field | Value |
|-------|-------|
| **Modality** | Tabular |
| **Task** | Regression |
| **Size** | 5,875 instances |
| **Access** | Open |
| **License** | UCI |
| **Last verified** | 2026-06-01 |

**Description.** Telemonitoring motor UPDRS scores.

**Primary reference.** UCI ML Repository.

**Access.** [UCI Parkinsons Telemonitoring](https://archive.ics.uci.edu/dataset/189/parkinsons+telemonitoring)

### UCI Parkinsons Speech — Parkinsons Speech Multi-Sound

| Field | Value |
|-------|-------|
| **Modality** | Tabular |
| **Task** | Classification |
| **Size** | 756 instances |
| **Access** | Open |
| **License** | UCI |
| **Last verified** | 2026-06-01 |

**Description.** Multiple sound recordings for PD.

**Primary reference.** UCI ML Repository.

**Access.** [UCI Parkinsons Speech](https://archive.ics.uci.edu/dataset/381/parkinsons+speech+dataset+with++multiple+types+of+sound+recordings)

### UCI Parkinsons Disease Classification — Parkinsons Disease Classification

| Field | Value |
|-------|-------|
| **Modality** | Tabular |
| **Task** | Classification |
| **Size** | 757 instances |
| **Access** | Open |
| **License** | UCI |
| **Last verified** | 2026-06-01 |

**Description.** 3D voice measurements for PD status.

**Primary reference.** UCI ML Repository.

**Access.** [UCI Parkinsons Disease Classification](https://archive.ics.uci.edu/dataset/174/parkinsons)

### mHealth — mHealth Dataset

| Field | Value |
|-------|-------|
| **Modality** | Wearable |
| **Task** | Activity recognition |
| **Size** | 10 subjects |
| **Access** | Open |
| **License** | UCI |
| **Last verified** | 2026-06-01 |

**Description.** Body motion and vital signs from wearables.

**Primary reference.** UCI ML Repository.

**Access.** [mHealth](https://archive.ics.uci.edu/dataset/319/mhealth+dataset)

### Opportunity — Opportunity Activity Recognition

| Field | Value |
|-------|-------|
| **Modality** | Wearable |
| **Task** | Activity recognition |
| **Size** | 4 subjects |
| **Access** | Open |
| **License** | UCI |
| **Last verified** | 2026-06-01 |

**Description.** Complex activity recognition on-body sensors.

**Primary reference.** UCI ML Repository.

**Access.** [Opportunity](https://archive.ics.uci.edu/dataset/226/opportunity+activity+recognition)

<a id="meta-catalogs--repositories"></a>


## Meta-Catalogs & Repositories

### PhysioNet — PhysioNet

| Field | Value |
|-------|-------|
| **Modality** | Multi-signal, EHR |
| **Task** | Repository |
| **Size** | 1,000+ projects |
| **Access** | Open / credentialed |
| **License** | Per-project |
| **Last verified** | 2026-06-01 |

**Description.** Primary repository for physiological and clinical data.

**Primary reference.** Goldberger AL, et al. *Circulation*. 2000.

**Access.** [PhysioNet](https://physionet.org/)

### TCIA — The Cancer Imaging Archive

| Field | Value |
|-------|-------|
| **Modality** | Oncology imaging |
| **Task** | Repository |
| **Size** | Many collections |
| **Access** | Open / mixed |
| **License** | Per-collection |
| **Last verified** | 2026-06-01 |

**Description.** NCI-funded cancer imaging archive.

**Primary reference.** Clark K, et al. *J Digit Imaging*. 2013.

**Access.** [TCIA](https://www.cancerimagingarchive.net/)

### NLM Dataset Catalog — NLM Dataset Catalog

| Field | Value |
|-------|-------|
| **Modality** | Biomedical |
| **Task** | Discovery |
| **Size** | Growing |
| **Access** | Open |
| **License** | NLM |
| **Last verified** | 2026-06-01 |

**Description.** NLM cross-repository dataset discovery (beta).

**Primary reference.** NLM.

**Access.** [NLM Dataset Catalog](https://datasetcatalog.nlm.nih.gov/)

### Project Imaging-X — Project Imaging-X

| Field | Value |
|-------|-------|
| **Modality** | Medical imaging |
| **Task** | Survey index |
| **Size** | 1,000+ datasets |
| **Access** | Open |
| **License** | Various |
| **Last verified** | 2026-06-01 |

**Description.** Survey and index of open medical imaging datasets.

**Primary reference.** Project Imaging-X Contributors. *GitHub*. 2025.

**Access.** [Project Imaging-X](https://github.com/uni-medical/Project-Imaging-X)

### Grand Challenge — Grand Challenge Platform

| Field | Value |
|-------|-------|
| **Modality** | Imaging |
| **Task** | Challenges |
| **Size** | 92+ active |
| **Access** | Mixed |
| **License** | Per-challenge |
| **Last verified** | 2026-06-01 |

**Description.** Biomedical challenge hosting and leaderboards.

**Primary reference.** Grand Challenge.

**Access.** [Grand Challenge](https://grand-challenge.org/)

### Google Dataset Search — Google Dataset Search

| Field | Value |
|-------|-------|
| **Modality** | All domains |
| **Task** | Discovery |
| **Size** | Web-scale |
| **Access** | Open |
| **License** | N/A |
| **Last verified** | 2026-06-01 |

**Description.** Dataset search engine for research.

**Primary reference.** Google Research.

**Access.** [Google Dataset Search](https://datasetsearch.research.google.com/)

### ECGDatasets — ECGDatasets Catalog

| Field | Value |
|-------|-------|
| **Modality** | ECG |
| **Task** | Index |
| **Size** | 64+ datasets |
| **Access** | Open |
| **License** | Catalog CC |
| **Last verified** | 2026-06-01 |

**Description.** Community ECG dataset catalog with DOIs.

**Primary reference.** Thambawita V, et al. *GitHub*.

**Access.** [ECGDatasets](https://github.com/vlbthambawita/ECGDatasets)

### OpenNeuro — OpenNeuro

| Field | Value |
|-------|-------|
| **Modality** | Neuroimaging |
| **Task** | Repository |
| **Size** | 1,000+ studies |
| **Access** | Mixed |
| **License** | Per-study |
| **Last verified** | 2026-06-01 |

**Description.** Open neuroimaging data archive.

**Primary reference.** Markiewicz CJ, et al. *Sci Data*. 2021.

**Access.** [OpenNeuro](https://openneuro.org/)

### beamandrew/medical-data — Medical Data (Beam)

| Field | Value |
|-------|-------|
| **Modality** | Multi-domain |
| **Task** | Curated list |
| **Size** | Hundreds |
| **Access** | Mixed |
| **License** | Various |
| **Last verified** | 2026-06-01 |

**Description.** Influential upstream curated medical data list.

**Primary reference.** Beam AL. *GitHub*.

**Access.** [beamandrew/medical-data](https://github.com/beamandrew/medical-data)

### awesome-healthcare-datasets — Awesome Healthcare Datasets

| Field | Value |
|-------|-------|
| **Modality** | Healthcare |
| **Task** | Curated list |
| **Size** | Growing |
| **Access** | Mixed |
| **License** | Various |
| **Last verified** | 2026-06-01 |

**Description.** Community healthcare dataset awesome list.

**Primary reference.** geniusrise contributors.

**Access.** [awesome-healthcare-datasets](https://github.com/geniusrise/awesome-healthcare-datasets)

### OHDSI — OHDSI Data Network

| Field | Value |
|-------|-------|
| **Modality** | EHR |
| **Task** | Observational research |
| **Size** | Global network |
| **Access** | DUA |
| **License** | OHDSI |
| **Last verified** | 2026-06-01 |

**Description.** Observational health data sciences collaborative.

**Primary reference.** OHDSI.

**Access.** [OHDSI](https://www.ohdsi.org/)

### Academic Torrents — Academic Torrents

| Field | Value |
|-------|-------|
| **Modality** | Large files |
| **Task** | Distribution |
| **Size** | Many |
| **Access** | Open |
| **License** | Various |
| **Last verified** | 2026-06-01 |

**Description.** Peer-assisted distribution of large research datasets.

**Primary reference.** Academic Torrents.

**Access.** [Academic Torrents](https://academictorrents.com/)

<a id="references"></a>

## References

Key DOIs cited in this catalog are listed in dataset entries. When citing this repository, use [CITATION.cff](CITATION.cff).

<a id="legacy-index"></a>

## Legacy index

The 2019 CVonline biomedical snapshot from v1.0 is archived in [docs/legacy-cvonline-index.md](docs/legacy-cvonline-index.md). Prefer verified entries above or [Meta-Catalogs](#meta-catalogs--repositories) for discovery.

## Acknowledgments

- [beamandrew/medical-data](https://github.com/beamandrew/medical-data) — upstream curated list
- [Project Imaging-X](https://github.com/uni-medical/Project-Imaging-X) — imaging survey
- Community contributors (see [CHANGELOG.md](docs/CHANGELOG.md))
