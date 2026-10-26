# About

I categorize, annotate and write comments for all research papers I read (600+ papers since 2018).

_In June 2023, I wrote the blog post [The How and Why of Reading 300 Papers in 5 Years](https://www.fregu856.com/post/phd_of_reading/) (why I think it’s important to read a lot of papers + how I organize my reading + paper statistics + a list of 30 particularly interesting papers)._

#### Categories:

[Uncertainty Estimation], [Ensembling], [Stochastic Gradient MCMC], [Variational Inference], [Out-of-Distribution Detection], [Theoretical Properties of Deep Learning], [VAEs], [Normalizing Flows], [ML for Medicine/Healthcare], [Object Detection], [3D Object Detection], [3D Multi-Object Tracking], [3D Human Pose Estimation], [Visual Tracking], [Sequence Modeling], [Reinforcement Learning], [Energy-Based Models], [Neural Processes], [Neural ODEs], [Transformers], [Implicit Neural Representations], [Distribution Shifts], [Social Consequences of ML], [Diffusion Models], [Graph Neural Networks], [Selective Prediction], [Language Models], [Representation Learning], [Vision-Language Models], [Image Restoration], [Computational Pathology], [Survival Analysis], [Time Series], [ECGs], [EHRs], [ML for Drug Discovery], [Miscellaneous].


### Papers:

- [Papers Read in 2026](#papers-read-in-2026)
- [Papers Read in 2025](#papers-read-in-2025)
- [Papers Read in 2024](#papers-read-in-2024)
- [Papers Read in 2023](#papers-read-in-2023)
- [Papers Read in 2022](#papers-read-in-2022)
- [Papers Read in 2021](#papers-read-in-2021)
- [Papers Read in 2020](#papers-read-in-2020)
- [Papers Read in 2019](#papers-read-in-2019)
- [Papers Read in 2018](#papers-read-in-2018)

#### Papers Read in 2026:

##### [26-10-26] [paper601]
- Pan-Cancer Virtual Spatial Transcriptomics From Routine Histology With Phoenix
 [[pdf]](https://www.biorxiv.org/content/10.64898/2026.04.25.720812v2) [[annotated pdf]](https://drive.google.com/file/d/1Nf6sdePLC5oVCrpfPBE8qQIG8v-IqFTB/view?usp=sharing)
- `biorxiv, 2026-04`
- [Computational Pathology]
```
Well-written and interesting paper. Took a while to read, and I definitely didn't understand absolutely everything (or am able to judge exactly how interesting/impressive/impactful all these results are), but I'm pretty happy that I read this. The model seems to perform well, in particular the 0.66 Spearman corr for pseudobulk predictions of 373 genes across all 9.5 TCGA samples seems quite impressive indeed to me. The "we concluded that lower sensitivity is the main shortcoming of Xenium 5K Prime" in the Discussion is interesting as well.
```

##### [26-10-26] [paper600]
- Nationwide HER2 Testing, Prospective Trastuzumab-Based Therapy, and Deep Visual Proteomics in Esophageal Squamous Cell Carcinoma
 [[pdf]](https://www.medrxiv.org/content/10.64898/2026.10.14.26365244v1) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Nationwide%20HER2%20Testing%2C%20Prospective%20Trastuzumab-Based%20Therapy%2C%20and%20Deep%20Visual%20Proteomics%20in%20Esophageal%20Squamous%20Cell%20Carcinoma.pdf)
- `medrxiv, 2026-10`
- [Computational Pathology]
```
Fairly interesting paper. I wanted to learn a bit more about "deep visual proteomics" after the previous paper I read, but this was a bit less interesting. They don't do unsupervised clustering of tile-level PFM (H-optimus-0) features here, but instead use a cell segmentation and classification model, and cluster tiles based on the cell type abundance/proportions in some way.
```

##### [26-10-25] [paper599]
- AI-Powered Deep Visual Proteomics Reveals Critical Molecular Transitions in Pancreatic Cancer Precursors 
 [[pdf]](https://aacrjournals.org/cancerdiscovery/article/16/7/1323/786251/AI-Powered-Deep-Visual-Proteomics-Reveals-Critical) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/AI-Powered%20Deep%20Visual%20Proteomics%20Reveals%20Critical%20Molecular%20Transitions%20in%20Pancreatic%20Cancer%20Precursors.pdf)
- `Cancer Discovery, 2026`
- [Computational Pathology]
```
Quite interesting paper, even though I definitely didn't understand absolutely everything, and it's difficult for me to judge how interesting/important/impactful these results and findings actually are. Main claimed finding: "histologically normal ducts from patients with cancer display significantly different molecular profiles than those from cancer-free individuals despite identical histopathologic presentation", which seems interesting. I've heard of "deep visual proteomics" before but didn't really know what this means until now.
```

##### [26-10-23] [paper598]
- Data-Efficient Pathology Whole-Slide Image Segmentation With Slide-Level Conditioning
 [[pdf]](https://www.nature.com/articles/s44303-026-00201-7) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Data-Efficient%20Pathology%20Whole-Slide%20Image%20Segmentation%20With%20Slide-Level%20Conditioning.pdf)
- `npj Imaging, 2026`
- [Computational Pathology]
```
Well-written and quite interesting paper, pretty happy that I decided to read this. The main idea makes sense to me, to do tile-level segmentation/prediction and aggregate these into a segmentation of the full WSI as usual, but to condition the tile-level predictions on the slide-level feature vector. The analysis in Section 2.4 - 2.7 is all quite interesting. Encouraging results in Figure 3, seems like you don't need too much annotated data. Somewhat strange results when comparing "w/o FiLM" in Supplementary Table 7 & 8 with the results in Table 1 & 2 though, as this variant often is worse than all baselines, even the most basic U-Net. Section 2.7 is interesting, using mean-pooled UNI2 patch-level features as the slide-level features instead of Prov-Gigapath's slide-level.
```

##### [26-10-23] [paper597]
- TiSAM: Fusing Spatial and Histopathology Foundation Models for Whole-Slide Image Segmentation
 [[pdf]](https://www.biorxiv.org/content/10.64898/2026.10.16.759688v1) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/TiSAM%20Fusing%20Spatial%20and%20Histopathology%20Foundation%20Models%20for%20Whole-Slide%20Image%20Segmentation.pdf)
- `biorxiv, 2026-10`
- [Computational Pathology]
```
Fairly interesting paper. Figure 1.B is interesting, that UNI-only is quite a lot better than SAM3-only, whereas UNI + SAM3 doesn't add that much more. TiSAM with UNI2-h is substantially better than with Resnet-50 in Figure 2, but not really in Figure 3.B. Figure 4.C seems encouraging, that not too much annotated data is needed for good performance (would like to see results for TiSAM with Resnet-50 here as well though, but I guess that might perform similarly to DeeplabV3+).
```

##### [26-10-18] [paper596]
- A Multimodal Whole-Slide Foundation Model for Pathology
 [[pdf]](https://www.nature.com/articles/s41591-025-03982-3) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/A%20Multimodal%20Whole-Slide%20Foundation%20Model%20for%20Pathology.pdf)
- `Nature Medicine, 2025`
- [Computational Pathology], [Vision-Language Models]
```
Interesting and well-written paper, I really enjoyed reading this. The TITAN paper from the Mahmood lab, super solid / comprehensive / high-quality work. I read everything until the end of the "TITAN improves region and slide-level diagnostic capabilities" section in Results in a lot of detail (and also all figures in the main paper), then I had to go through the rest a bit quicker. In particular, I didn't have much time to read the Methods. The one main thing I don't understand is the "Rare cancer external" results in Figure 4.a, why is the vision-only TITAN_v suddenly quite a lot better than TITAN there?
```

##### [26-10-18] [paper595]
- Incorporating Pathomics Into IgAN Risk Prediction
 [[pdf]](https://www.sciencedirect.com/science/article/pii/S2468024926029402) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Incorporating%20Pathomics%20Into%20IgAN%20Risk%20Prediction.pdf)
- `Kidney International Reports, 2026`
- [Computational Pathology]
```
Quite interesting paper, further evaluation/application of the approach from "Next-Generation Morphometry for Pathomics-Data Mining in Histopathology" that I read previously, so these three papers directly build on each other. I think it was pretty useful for me to read all three. Here they use 10 segmentation-based features, and compare the performance with established risk scores.
```

##### [26-10-18] [paper594]
- Next-Generation Morphometry for Pathomics-Data Mining in Histopathology
 [[pdf]](https://www.nature.com/articles/s41467-023-36173-0) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Next-Generation%20Morphometry%20for%20Pathomics-Data%20Mining%20in%20Histopathology.pdf)
- `Nature Communications, 2023`
- [Computational Pathology]
```
Quite interesting paper, directly builds upon "Deep Learning-Based Segmentation and Quantification in Experimental Kidney Histopathology" that I read previously. I do think that this overall approach makes some sense, and the results in Figure 4 seem relatively strong. I don't understand how they actually do the pseudotime stuff in Figure 5 though.
```

##### [26-10-16] [paper593]
- Deep Learning-Based Segmentation and Quantification in Experimental Kidney Histopathology
 [[pdf]](https://www.ovid.com/jnls/jasn/fulltext/10.1681/asn.2020050597~deep-learningbased-segmentation-and-quantification-in) [_unfortunately not open access, thus no annotated pdf_]
- `Journal of the American Society of Nephrology, 2021`
- [Computational Pathology]
```
Quite interesting paper, probably pretty useful for me to read. Gives a bit of general kidney pathology background, neat to see some examples of what structures might make sense to segment here etc. Relatively small amounts of annotated data that's needed actually, just 2100 annotated patches, and using just ~30% of that mostly works well too. And, this when training from scratch without using any PFM.
```

##### [26-10-15] [paper592]
- From Cosmos to Clinic: Interpretable Spatial Statistics for Histopathology Prognosis
 [[pdf]](https://openaccess.thecvf.com/content/ICCV2025W/CVAMD/html/Barna_From_Cosmos_to_Clinic_Interpretable_Spatial_Statistics_for_Histopathology_Prognosis_ICCVW_2025_paper.html) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/From%20Cosmos%20to%20Clinic%20Interpretable%20Spatial%20Statistics%20for%20Histopathology%20Prognosis.pdf)
- `ICCV Workshops 2025`
- [Computational Pathology]
```
Quite interesting paper. It's not clear exactly how they create those textual descriptions ("each reconstructed correlation function is matched against our predefined taxonomy of spatial relationship patterns based on curve characteristics", so I guess that they have a number of curve templats they compare with? But how many, and how did they define these?), and I'm not sure how useful those actually would be in practice. But other than that I think their approach makes some sense and was quite interesting, seems like a reasonable way to compute handcrafted features. Would be interesting to see how well a linear classifier on top of their 100-dim features would perform on other tasks as well, not just this one platinum response prediction task.
```

##### [26-10-14] [paper591]
- Human-Interpretable Image Features Derived From Densely Mapped Cancer Pathology Slides Predict Diverse Molecular Phenotypes
 [[pdf]](https://www.nature.com/articles/s41467-021-21896-9) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Human-Interpretable%20Image%20Features%20Derived%20From%20Densely%20Mapped%20Cancer%20Pathology%20Slides%20Predict%20Diverse%20Molecular%20Phenotypes.pdf)
- `Nature Communications, 2021`
- [Computational Pathology]
```
Fairly interesting paper. Quite a lot of details that I didn't fully follow. But nice to see an example of what type of features can be computed, and what these can be used to predict. I was perhaps hoping for this paper to feel a bit more practically relevant/useful, but I don't regret reading it.
```

##### [26-10-14] [paper590]
- Sparse Concept Attribution for Histomorphological Hypothesis Generation From Whole-Slide Classifiers
 [[pdf]](https://arxiv.org/abs/2609.02985) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Sparse%20Concept%20Attribution%20for%20Histomorphological%20Hypothesis%20Generation%20From%20Whole-Slide%20Classifiers.pdf)
- `arxiv, 2026-09`
- [Computational Pathology]
```
Well-written and quite interesting paper. Quite long, so I didn't read absolutely everything in detail. I do think the overall approach is interesting and makes some sense. Feel like it's difficult for me to judge how useful generated short hypotheses like those in Table S3 actually might be in practice though, but maybe this could be combined with other methods in some way at least.
```

##### [26-10-12] [paper589]
- Toward Comprehensive Cellular Characterization of H&E Slides
 [[pdf]](https://www.sciencedirect.com/science/article/pii/S2153353926001562) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Toward%20Comprehensive%20Cellular%20Characterization%20of%20H%26E%20Slides.pdf)
- `Journal of Pathology Informatics, 2026`
- [Computational Pathology]
```
Somewhat interesting paper. I was expecting something a bit different, I was hoping for much more in the "HistoPLUS allows interpretable biomarker discovery in downstream tasks" direction. Now they just have the "Resullts - HistoPLUS enables interpretable biomarker analysis in downstream clinical tasks" section, and I don't even fully understand what they do there, exactly what the "72 histomorphometric covariates from HistoPLUS outputs" are or how they are computed. Otherwise what they actually do and their approach makes sense, to create a better train dataset and utilize pathology FMs. Neat that the small distilled H0-mini performs well also in this application.
```

##### [26-10-12] [paper588]
- Designing Protein Structures from Natural Language
 [[pdf]](https://arxiv.org/abs/2610.13917) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Designing%20Protein%20Structures%20from%20Natural%20Language.pdf)
- `arxiv, 2026-10`
- [ML for Drug Discovery]
```
Well-written and quite interesting paper. All figures are really nice. The basic idea of text-conditioned protein structure generation is definitely cool/nice and makes quite a lot of sense. The agent-guided, iterative approach also makes sense, and the application of it to design binders for GM2A in 3.3 is cool. Difficult for me to judge exactly how impressive these results are though, or how useful/impactful this text-conditioned approach actually will be in practice moving forwards. This from the conclusion makes some sense to me, "As language-model agents improve, specialist generative models need interfaces that let agents use scientific knowledge and language-based reasoning to guide generation. Prompteina makes this connection more seamless [...] these results establish natural language as an effective, powerful conditioning interface that lets agents directly connect scientific knowledge, language-based reasoning, and experimental results to protein structure generation and design", but is a natural language interface really a necessary requirement for this?
```

##### [26-10-11] [paper587]
- The Past, Present and Future of de Novo Protein Design
 [[pdf]](https://www.nature.com/articles/s41586-026-10328-7) [_unfortunately not open access, thus no annotated pdf_]
- `Nature, 2026`
- [ML for Drug Discovery]
```
Fairly interesting paper. Figure 1 - 4 are all really nice, if nothing else, it was interesting to just go through these in detail. I was probably expecting/hoping to get a bit more out of reading this, feels like you need to know this stuff quite well already from before to really appreciate this paper. But still quite useful for me I think, quite a few seemingly interesting references that I will look up in a bit more detail as well.
```

##### [26-10-09] [paper586]
- Spatial Biomarker Discovery via Interpretable Semantic Learning in Histopathology
 [[pdf]](https://www.sciencedirect.com/science/article/pii/S153561082600259X) [[annotated pdf]](https://drive.google.com/file/d/1ObxHmtk4KMlflLhku85gn25dWZJv_1kI/view?usp=sharing)
- `Cancer Cell, 2026`
- [Computational Pathology]
```
Well-written and interesting paper, happy that I decided to read this (quite a lot of details though, I probably spent a bit too much time on this, but I also quite enjoyed it). The approach definitely makes some intuitive sense, and seems to work quite well in different settings.
```

##### [26-10-06] [paper585]
- Stateful Visual Encoders for Vision-Language Models
 [[pdf]](https://arxiv.org/abs/2606.04433) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Stateful%20Visual%20Encoders%20for%20Vision-Language%20Models.pdf)
- `arxiv, 2026-06`
- [Vision-Language Models] 
```
Quite interesting paper. Nice, simple and intuitive idea, feels like it should work. The performance gains seem to be pretty marginal though. Table 3, their model "Cross+FFN" is quite clearly better than "Baseline (Stateless)", yes, but the difference compared to "Capacity-controlled baseline Self+FFN" is small. The performance gains on all three real-world tasks in Table 6 - 8 are also pretty small, and the "Capacity controlled baseline" would probably be even closer to their model, I suppose.
```

##### [26-10-06] [paper584]
- Personalized Care in CKD: Moving Beyond Traditional Biomarkers
 [[pdf]](https://karger.com/nef/article/149/6/339/919567/Personalized-Care-in-CKD-Moving-Beyond-Traditional) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Personalized%20Care%20in%20CKD%20Moving%20Beyond%20Traditional%20Biomarkers.pdf)
- `Nephron, 2025`
- [ML for Medicine/Healthcare] 
```
Fairly interesting paper. I wanted to get some more general background on CKD, which I think it did a pretty good job for.  So, not overly interesting, but I don't regret deciding to read this.
```

##### [26-10-05] [paper583]
- Biomarkers of Kidney Failure and All-Cause Mortality in CKD
 [[pdf]](https://www.ovid.com/jnls/jasn/fulltext/10.1681/asn.0000000767~biomarkers-of-kidney-failure-and-all-cause-mortality-in-ckd) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Biomarkers%20of%20Kidney%20Failure%20and%20All-Cause%20Mortality%20in%20CKD.pdf)
- `Journal of the American Society of Nephrology, 2025`
- [ML for Medicine/Healthcare] 
```
Quite interesting paper, and definitely useful for me read. Good background info on CKD, the Nurture dataset, etc. Good for me to see how difficult the standard risk factors (UACR + eGFR, and sex + age + ethnicity) are to beat in terms of pure predictive performance of kidney failure or all-cause mortality, and how the authors here argue that other urine/blood biomarkers still could be useful.
```

##### [26-10-04] [paper582]
- Coevolution Took Us Here, but It’s Not Enough
 [[pdf]](https://couteiral.substack.com/p/coevolution-took-us-here-but-its) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Coevolution%20Took%20Us%20Here%2C%20but%20It%E2%80%99s%20Not%20Enough.pdf)
- `(Blog post, 2026-08)`
- [ML for Drug Discovery] 
```
A blog post and not a paper, but I still wanted to include it here because I enjoyed reading it and found it interesting/informative. Third blog post from Carlos Outeiral that I read, and I will definitely try to read future posts as well. Interesting, and I feel like they give good insights into how the field has developed and might progress moving forward.
```

##### [26-10-02] [paper581]
- Drug Discovery & Development Basics
 [[pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Drug%20Discovery%20%26%20Development%20Basics.pdf)
- `(Generated document, 2026-10)`
- [ML for Drug Discovery] 
```
A long ChatGPT-generated document (400 pages) I have used to just get some basic understanding of the overall drug discovery/development process. The most important is part IV which mainly contains short summaries of various recent papers. There, I've asked ChatGPT to summarize and help me understand the basic underlying biology of papers I spotted in Nature, Nature Medicine, Nature Communications, npj Precision Oncology, etc. These are papers I just found interesting based on the titles, often papers which evaluated different types of drugs that I wanted to understand better (immune checkpoint inhibitors, CAR-T cell therapy, T-cell engagers, DNA damage response inhibitors, antibody-drug conjugates, PROTACs, molecular glues, etc). I have read the full document in detail using my tablet. I definitely don't remember/understand absolutely everything, but I did find it very useful to go through all this over the past month or so. Spotting new papers which seem to cover something I'd like to understand better / learn more about, asking ChatGPT to quickly summarize them, saving these summaries in a document, and then reading these in detail. I have found this process very useful, and I feel like I have learned a lot in a quite short time.
```

##### [26-09-23] [paper580]
- Self-Supervised DXA Representations Encode Multi-System Disease Risk, Biological Aging and Heritability
 [[pdf]](https://arxiv.org/abs/2608.02208) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Self-Supervised%20DXA%20Representations%20Encode%20Multi-System%20Disease%20Risk%2C%20Biological%20Aging%20and%20Heritability.pdf)
- `arxiv, 2026-08`
- [ML for Medicine/Healthcare]
```
Fairly interesting paper. Quite long, and I didn't read absolutly everything in full detail. I was not familiar with this type of data before, DXA scans. Quite interesting that they use LeJEPA to train their model from scratch, I was not overly familiar with LeJEPA/JEPA either. Looks solid overall, seems to perform quite well, and they compare with reasonable baselines. They don't really mention that DINOv3 actually outperforms their model for mortality prediction though (Figure 3a). And while the age gap results (Figure 5) are neat, I suspect that you probably would achieve pretty similar results based on DINOv3 as well.
```

##### [26-09-08] [paper579]
- Multimodality as Supervision: Self-Supervised Specialization to the Test Environment via Multimodality
 [[pdf]](https://openreview.net/forum?id=4dMlAKBwrA) [[annotated pdf]](https://drive.google.com/file/d/1-t7h3aYKtBICG5LK7TPHDvb5hp5y9piv/view?usp=sharing)
- `ICLR 2026`
- [Representation Learning]
```
Quite interesting paper. They study this with the robotics setting in mind, but it made me think about how one could/should adapt a general pathology FM to a tissue-specific model, a certain deployment setting with fixed staining and scanning processes or similar, I think what they analyze in this paper potentially could be interesting/relevant for that as well. I don't understand how this ICLR paper can be 13.5 pages long though?
```

##### [26-09-06] [paper578]
- Miniproteins are the TikZ Unicorn of Biology
 [[pdf]](https://couteiral.substack.com/p/miniproteins-are-the-tikz-unicorn) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Miniproteins%20are%20the%20TikZ%20Unicorn%20of%20Biology.pdf)
- `(Blog post, 2026-09)`
- [ML for Drug Discovery] 
```
A blog post and not a paper, but I wanted to include it here as well. Not quite as interesting/informative as the previous one, and it didn't actually cover quite what I thought that it would, but I'm still pretty happy that I decided to read this.
```

##### [26-09-04] [paper577]
- The Antibody Revolution is Real. The Business, Less So
 [[pdf]](https://couteiral.substack.com/p/the-antibody-revolution-is-real-the) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/%20The%20Antibody%20Revolution%20is%20Real.%20The%20Business%2C%20Less%20So.pdf)
- `(Blog post, 2026-07)`
- [ML for Drug Discovery] 
```
A blog post and not a paper, but I still wanted to include this here because I enjoyed reading it and found it both really interesting and informative.
```

##### [26-08-28] [paper576]
- End-To-End Multimodal Pathology Foundation Model With Clinical Dialogue
 [[pdf]](https://www.nature.com/articles/s41591-026-04521-4) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/End-To-End%20Multimodal%20Pathology%20Foundation%20Model%20With%20Clinical%20Dialogue.pdf)
- `Nature Medicine, 2026`
- [Computational Pathology], [Vision-Language Models]
```
Quite interesting and well-written paper. Slide-level VLMs are definitely interesting, to be able to do "prompt-based inference" directly on the slide-level could definitely be very useful. Not entirely sure how well report generation, open-ended Q&A and multiple-choice Q&A etc actually can be expected to work though, given that Phi-3-Mini still is a relatively small and not overly powerful LLM.
```

##### [26-08-24] [paper575]
- Target Identification and Assessment in the Era of AI
 [[pdf]](https://www.nature.com/articles/s41573-026-01412-8) [_unfortunately not open access, thus no annotated pdf_]
- `Nature Reviews Drug Discovery, 2026`
- [ML for Drug Discovery]
```
Fairly interesting paper. The "Key considerations in target identification" section was quite interesting and felt like good background material for me, but then the rest of the paper didn't really give me that much.
```

##### [26-08-23] [paper574]
- Impact of a Five-Dimensional Framework on R&D Productivity at AstraZeneca
 [[pdf]](https://www.nature.com/articles/nrd.2017.244) [_unfortunately not open access, thus no annotated pdf_]
- `Nature Reviews Drug Discovery, 2018`
- [ML for Drug Discovery]
```
Interesting paper. Basically a direct follow-up to "Lessons Learned From the Fate of AstraZeneca's Drug Pipeline: A Five-Dimensional Framework" that I read before. This also felt like good background material for me, and I quite enjoyed reading this as well.
```

##### [26-08-20] [paper573]
- Achieving End-To-End Success in the Clinic: Pfizer's Learnings on R&D Productivity
 [[pdf]](https://www.sciencedirect.com/science/article/pii/S1359644621005444) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Achieving%20End-To-End%20Success%20in%20the%20Clinic%20Pfizer's%20Learnings%20on%20R%26D%20Productivity.pdf)
- `Drug Discovery Today, 2022`
- [ML for Drug Discovery]
```
Pretty short paper that was quick/easy to read, and at least quite interesting. If nothing else, interesting to read a bit about the Pfizer/Biontech COVID-19 vaccine and just how quickly they were able to develop this (and then also ship 2 billion doses), super impressive actually.
```

##### [26-08-20] [paper572]
- Artificial Intelligence in Drug Discovery — What It Is, Where We Stand and the Path Forward
 [[pdf]](https://www.nature.com/articles/s41573-026-01496-2) [_unfortunately not open access, thus no annotated pdf_]
- `Nature Reviews Drug Discovery, 2026`
- [ML for Drug Discovery]
```
Quite interesting paper, but I was probably expecting / hoping for a bit more. I found it less interesting starting from roughly the halfway point. I appreciate the authors' critical, non-hype-driven perspective on the field, but some things also seem a bit basic/obvious to me (e.g., "The performance of a model therefore needs to be evaluated in the context of its eventual use case").
```

##### [26-08-19] [paper571]
- Lessons Learned From the Fate of AstraZeneca's Drug Pipeline: A Five-Dimensional Framework
 [[pdf]](https://www.nature.com/articles/nrd4309) [_unfortunately not open access, thus no annotated pdf_]
- `Nature Reviews Drug Discovery, 2014`
- [ML for Drug Discovery]
```
Interesting paper, I definitely found this useful. Good background material for me, I quite enjoyed reading it. 
```

##### [26-06-27] [paper570]
- Proteina: Scaling Flow-based Protein Structure Generative Models
 [[pdf]](https://arxiv.org/abs/2503.00710) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Proteina%20Scaling%20Flow-based%20Protein%20Structure%20Generative%20Models.pdf)
- `ICLR 2025`
- [ML for Drug Discovery], [Diffusion Models] 
```
Well-written and fairly interesting paper. Definitely solid work and a bunch of different types of contributions which all make sense, but I personally didn't find the technical details overly interesting at this stage. But I think/hope this can probably be a pretty good starting point for some other recent papers.
```

##### [26-06-27] [paper569]
- Accurate Predictions of Novel Biomolecular Interactions with IsoDDE
 [[pdf]](https://storage.googleapis.com/isomorphiclabs-website-public-artifacts/isodde_technical_report.pdf) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Accurate%20Predictions%20of%20Novel%20Biomolecular%20Interactions%20with%20IsoDDE.pdf)
- `Technical report, 2026-02`
- [ML for Drug Discovery] 
```
Interesting paper, I enjoyed reading this. No model/method details whatsoever, which of course is too bad, but still interesting. Things are explained well and easy to follow. Figure 15 is quite odd though, they write "showing that confidence score is well calibrated to success rate even for examples with low similarity to the training set", but this is true just for High similarity? For both Medium and Low, the model is quite clearly overconfident (e.g., confidence of 0.6 gives a success rate much lower than 60%)?
```

##### [26-06-26] [paper568]
- Protenix-v2: Broadening the Reach of Structure Prediction and Biomolecular Design
 [[pdf]](https://www.biorxiv.org/content/10.64898/2026.04.10.717613v1) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Protenix-v2%20Broadening%20the%20Reach%20of%20Structure%20Prediction%20and%20Biomolecular%20Design.pdf)
- `biorxiv, 2026-04`
- [ML for Drug Discovery] 
```
Fairly interesting paper. No model/method details whatsoever, they just state that it's improved compared to the v1 version. Pretty quick to read, and I feel like I become a bit more familiar/comfortable with all the biology-related background with every paper, but this probably didn't give that much compared to similar papers I've read before.
```

##### [26-06-26] [paper567]
- Latent-Y: A Lab-Validated Autonomous Agent for De Novo Drug Design
 [[pdf]](https://arxiv.org/abs/2603.29727) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Latent-Y%20A%20Lab-Validated%20Autonomous%20Agent%20for%20De%20Novo%20Drug%20Design.pdf)
- `arxiv, 2026-03`
- [ML for Drug Discovery] 
```
Quite interesting paper. Not a lot of details, but on the other hand quick and easy to read. Technically, this is definitely an interesting/impressive system, but very difficult for me to judge if their claims regarding speed-ups are realistic/fair, and whether this actually is a type of product that would be useful/valuable for companies in practice, etc (in particular, the experiments where they give a paper as input to the system, technically impressive and cool, but would this actually be used in practice?).
```

##### [26-06-24] [paper566]
- BoltzMol-1: Towards Reliable Virtual Screening for Fast and Cost-Effective Hit Discovery
 [[pdf]](https://boltz.bio/boltzmol1-technical-report.pdf) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/BoltzMol-1%20Towards%20Reliable%20Virtual%20Screening%20for%20Fast%20and%20Cost-Effective%20Hit%20Discovery.pdf)
- `Technical report, 2026-06`
- [ML for Drug Discovery] 
```
Quite interesting paper, to see a concrete applicaton/evaluation of their Boltz-2 model. Of course a bunch of things in Section 2 that I don't understand, but still a bit interesting, it gives some background. Section 3 is quite interesting. In particular, this highlights a pretty interesting limitation / failure case of the Boltz-2 model: "we identify and exclude a set of structures we term virtual PAINS: compounds that the model systematically scores as strong binders across unrelated targets, independent of any genuine target-specific interaction signal [...] by aggregating Boltz-2 scores across a diverse panel of held-out targets and flagging compounds that consistently appear in the top ranks regardless of target identity".
```

##### [26-06-23] [paper565]
- Drug-Like Antibodies with Low Immunogenicity in Human Panels Designed with Latent-X2
 [[pdf]](https://arxiv.org/abs/2512.20263) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Drug-Like%20Antibodies%20with%20Low%20Immunogenicity%20in%20Human%20Panels%20Designed%20with%20Latent-X2.pdf)
- `arxiv, 2025-12`
- [ML for Drug Discovery] 
```
Quite interesting paper. Interesting to see that multiple companies are working on similar problems at the moment, to demonstrate that their models can generate structures that not only bind well to various targets, but also pass common requirements for actual use as drugs in practice (good "developability" properties, low immunogenicity). Of course very difficult for someone with my background to judge how impressive these results are though, if they actually have a strong product to sell. But quite interesting to read either way, and I feel like I gain a better understanding of this space step by step.
```

##### [26-06-21] [paper564]
- Drug-Like Antibody Design Against Challenging Targets with Atomic Precision
 [[pdf]](https://www.biorxiv.org/content/10.1101/2025.11.29.691346v2) [[annotated pdf]](https://drive.google.com/file/d/1J-10I7c95YNTI1TfzZNObuo-bfI8eXKs/view?usp=sharing)
- `biorxiv, 2025-12`
- [ML for Drug Discovery] 
```
Quite interesting paper. This is a technical report from Chai Discovery, doing further validation and proof-of-concept demonstrations of their previously published Chai-2 model. I definitely don't have the background necessary to understand and appreciate everything here, but I still found it quite interesting to read, I feel like learned quite a lot. Glad I decided to read this.
```

##### [26-06-21] [paper563]
- Latent-X: An Atom-level Frontier Model for De Novo Protein Binder Design
 [[pdf]](https://arxiv.org/abs/2507.19375) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Latent-X%20An%20Atom-level%20Frontier%20Model%20for%20De%20Novo%20Protein%20Binder%20Design.pdf)
- `arxiv, 2025-07`
- [ML for Drug Discovery] 
```
Quite interesting paper. Basically no technical details on their model, but still some pretty interesting/useful background on the problem they're trying to solve and the field in general. Difficult for me to judge how impressive their results actually are though, whether they indeed have a strong product to sell here. Nice figures/visualizations.
```

##### [26-06-21] [paper562]
- BoltzProt-1: Towards Efficient De Novo Binder Design with Good Developability
 [[pdf]](https://boltz.bio/boltzprot1-technical-report.pdf) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/BoltzProt-1%20Towards%20Efficient%20De%20Novo%20Binder%20Design%20with%20Good%20Developability.pdf)
- `Technical report, 2026-06`
- [ML for Drug Discovery] 
```
Quite interesting paper. However, I should probably have read the BoltzGen paper and some more other papers before reading this one, to better appreciate what they're doing and the importance of it.
```

##### [26-06-20] [paper561]
- Boltz-2: Towards Accurate and Efficient Binding Affinity Prediction
 [[pdf]](https://www.biorxiv.org/content/10.1101/2025.06.14.659707v1) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Boltz-2%20Towards%20Accurate%20and%20Efficient%20Binding%20Affinity%20Prediction.pdf)
- `biorxiv, 2025-06`
- [ML for Drug Discovery] 
```
Interesting paper, I quite enjoyed reading this. Binding affinity prediction definitely seems like an interesting problem/application to me. Things are clearly explained overall, I feel like this provided some pretty good background for me.
```

##### [26-06-17] [paper560]
- Boltz-1: Democratizing Biomolecular Interaction Modeling
 [[pdf]](https://www.biorxiv.org/content/10.1101/2024.11.19.624167v4) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Boltz-1%20Democratizing%20Biomolecular%20Interaction%20Modeling.pdf)
- `biorxiv, 2024-11`
- [ML for Drug Discovery] 
```
Quite interesting paper, I found this quite useful to read. The conclusion summarizes the paper well, they basically create an open-source version of AlphaFold3, and then also add various tweaks/improvements/optimizations. Their model does indeed seem to perform competitively to AlphaFold (Figure 5 and 6). Figure 7 is neat. 
```

##### [26-06-17] [paper559]
- Accurate Structure Prediction of Biomolecular Interactions with AlphaFold 3
 [[pdf]](https://www.nature.com/articles/s41586-024-07487-w) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Accurate%20Structure%20Prediction%20of%20Biomolecular%20Interactions%20with%20AlphaFold%203.pdf)
- `Nature, 2024`
- [ML for Drug Discovery] 
```
Fairly interesting paper for me. I didn't check the supplementary material in detail this time either, I just wanted an overview. Not sure how much I gained by reading this compared to the previous AlphaFold 2 paper.
```

##### [26-06-17] [paper558]
- Highly Accurate Protein Structure Prediction With AlphaFold
 [[pdf]](https://www.nature.com/articles/s41586-021-03819-2) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Highly%20Accurate%20Protein%20Structure%20Prediction%20With%20AlphaFold.pdf)
- `Nature, 2021`
- [ML for Drug Discovery] 
```
I found this quite interesting/useful to read. I just scrolled through the supplementary material super quickly, so I didn't even really try to understand the model in detail. It's definitely quite complex, not "clean" or straightforward. But still quite interesting to read, just to get an overview of the model and what they actually did.
```

##### [26-06-16] [paper557]
- Machine Learning in Preclinical Drug Discovery
 [[pdf]](https://www.nature.com/articles/s41589-024-01679-1) [_unfortunately not open access, thus no annotated pdf_]
- `Nature Chemical Biology, 2024 (Perspective)`
- [ML for Drug Discovery] 
```
Fairly interesting review paper. Well-written overall and with nice figures etc, and gives a pretty good high-level overview of the field, but I think there probably are papers I would find more interesting/useful.
```

##### [26-06-16] [paper556]
- Diffusion Models in Protein Structure and Docking
 [[pdf]](https://wires.onlinelibrary.wiley.com/doi/10.1002/wcms.1711) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Diffusion%20Models%20in%20Protein%20Structure%20and%20Docking.pdf)
- `Wiley Interdisciplinary Reviews: Computational Molecular Science, 2024`
- [Diffusion Models], [ML for Drug Discovery] 
```
Quite interesting paper, a well-written review. I found it quite useful. Section 2 is nice, I think they explain things in a good/clear way. Overall happy that I decided to read this.
```

##### [26-06-15] [paper555]
- Equivariant Diffusion for Molecule Generation in 3D
 [[pdf]](https://arxiv.org/abs/2203.17003) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Equivariant%20Diffusion%20for%20Molecule%20Generation%20in%203D.pdf)
- `ICML 2022`
- [Diffusion Models], [ML for Drug Discovery]
```
Quite interesting paper. I just wanted to start somewhere, with a well-cited paper, from a couple of years back, starting to get a basic understanding of the whole ML for drug discovery/design area.
```

##### [26-03-05] [paper554]
- PulseLM: A Foundation Dataset and Benchmark for PPG-Text Learning
 [[pdf]](https://arxiv.org/abs/2603.03331) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/PulseLM%20A%20Foundation%20Dataset%20and%20Benchmark%20for%20PPG-Text%20Learning.pdf)
- `arxiv, 2026-02`
- [ML for Medicine/Healthcare], [Language Models], [Time Series] 
```
Interesting paper. Seems like a potentially useful dataset. The model/approach they use is simple and makes sense (frozen PaPaGei as PPG encoder, and then they train a mapping/projection layer while fine-tuning the LLM using LoRA). Some pretty nice scaling results for LLama 3.2 1B, 3B, 8B.
```

#### Papers Read in 2025:

##### [25-09-20] [paper553]
- Contrastive Multi-Modal Training With Electrocardiography and Natural Language Echocardiography Reports for Zero-Shot Prediction of Structural Heart Disease
 [[pdf]](https://www.medrxiv.org/content/10.1101/2025.09.16.25335870v1) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Contrastive%20Multi-Modal%20Training%20With%20Electrocardiography%20and%20Natural%20Language%20Echocardiography%20Reports%20for%20Zero-Shot%20Prediction%20of%20Structural%20Heart%20Disease.pdf)
- `medrxiv, 2025-09`
- [ML for Medicine/Healthcare], [ECGs] 
```
Quite interesting and well-written paper. They take the MERL model and train it further on 45k ECG-text data pairs, with the text data extracted from echocardiography reports. The external test data is from EchoNext, but then I don't quite understand why they only have 5.4k ECGs, EchoNext is much bigger than that?
```

##### [25-09-18] [paper552]
- Multimodal Clinical Benchmark for Emergency Care (MC-BEC): A Comprehensive Benchmark for Evaluating Foundation Models in Emergency Medicine
 [[pdf]](https://arxiv.org/abs/2311.04937) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Multimodal%20Clinical%20Benchmark%20for%20Emergency%20Care%20(MC-BEC)%20A%20Comprehensive%20Benchmark%20for%20Evaluating%20Foundation%20Models%20in%20Emergency%20Medicine.pdf)
- `NeurIPS 2023 (Track on Datasets and Benchmarks)`
- [ML for Medicine/Healthcare], [ECGs], [Time Series] 
```
I wanted to read this because they use an earlier version of the MC-MED dataset. They evaluate on three specific tasks (1. Decompensation: "predict which patients are likely to experience clinical decompensation, defined as new onset of tachycardia (heart rate [HR] > 110), hypotension (mean arterial pressure [MAP] < 65 mmHg), or hypoxia (oxygen saturation by pulse oximetry [SpO2] < 90%) in patients with initially normal vital signs". 2. Disposition: "predict the binary outcome of a patient’s disposition from the ED: whether they will be discharged home or admitted to the hospital". 3. Revisit: "predict whether a patient will revisit the ED within a 3, 7, or 14-day period after being discharged") which all are pretty interesting and seem to make sense. But, a ton of details are missing? I would definitely not be able to implement their model just based on this paper at least. For example, what's even the format of the ECG/PPG data? Do they have one long, continuous signal for each ED visit? If so, exactly how do they extract features from these long signals then? In conclusion, I'm not sure how much I learned from this compared to just reading the MC-MED paper.
```

##### [25-09-18] [paper551]
- MC-MED, Multimodal Clinical Monitoring in the Emergency Department
 [[pdf]](https://www.nature.com/articles/s41597-025-05419-5) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/MC-MED%2C%20Multimodal%20Clinical%20Monitoring%20in%20the%20Emergency%20Department.pdf)
- `Scientific Data, 2025`
- [ML for Medicine/Healthcare], [ECGs], [Time Series]
```
Short paper describing the MC-MED dataset. Not a ton of details (for example, not clear how many ECG segments there typically are for a visit, or how long these segments typically are), but yes, this seems like an interesting/useful dataset and resource.
```

##### [25-09-17] [paper550]
- BenchECG and xECG: A Benchmark and Baseline for ECG Foundation Models
 [[pdf]](https://arxiv.org/abs/2509.10151) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/BenchECG%20and%20xECG%20A%20Benchmark%20and%20Baseline%20for%20ECG%20Foundation%20Models.pdf)
- `arxiv, 2025-09`
- [ML for Medicine/Healthcare], [ECGs] 
```
Well-written and interesting paper, overall I quite enjoyed reading this. But then towards the end I got somewhat confused and perhaps a bit less impressed. Interesting that they use an xLSTM model instead of a transformer, and interesting that they use a DINOv2 variant to pretrain the model instead of random masking / reconstruction etc. I don't think I've seen DINO being applied to ECGs before? I think that this approach might make sense. I was a bit confused by the evaluation though, how they use different "window len" for different models (Table 15 - 18). I thought that they were gonna be able to directly apply their xLSTM model to ~really~ long signals (even multiple hours perhaps), but if I understand correctly, they never feed their model longer subsegments than 3 minutes. But yes, still interesting, made think quite a lot, in a good way.
```

##### [25-09-15] [paper549]
- Predicting Future Hospital Antimicrobial Resistance Prevalence Using Machine Learning
 [[pdf]](https://www.nature.com/articles/s43856-024-00606-8) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Predicting%20Future%20Hospital%20Antimicrobial%20Resistance%20Prevalence%20Using%20Machine%20Learning.pdf)
- `Communications Medicine, 2024`
- [ML for Medicine/Healthcare] 
```
Quite interesting, I'm reading this to get a sense of what type of problems David Eyre and his group are working on. The abstract/introduction was pretty good/useful/interesting medical background for me.
```

##### [25-09-13] [paper548]
- ECG Semantic Integrator (ESI): A Foundation ECG Model Pretrained with LLM-Enhanced Cardiological Text
 [[pdf]](https://openreview.net/forum?id=giEbq8Khcf) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/ECG%20Semantic%20Integrator%20(ESI)%20A%20Foundation%20ECG%20Model%20Pretrained%20with%20LLM-Enhanced%20Cardiological%20Text.pdf)
- `TMLR, 2024`
- [ML for Medicine/Healthcare], [ECGs]
```
Well-written and interesting paper, I quite enjoyed reading this. Everything is explained well and makes sense overall. Multiple interesting and neat ablations/experiments in Section 5. Just a very solid paper overall.
```

##### [25-09-08] [paper547]
- MEETI: A Multimodal ECG Dataset from MIMIC-IV-ECG with Signals, Images, Features and Interpretations
 [[pdf]](https://arxiv.org/abs/2507.15255) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/MEETI%20A%20Multimodal%20ECG%20Dataset%20from%20MIMIC-IV-ECG%20with%20Signals%2C%20Images%2C%20Features%20and%20Interpretations.pdf)
- `arxiv, 2025-07`
- [ML for Medicine/Healthcare], [ECGs] 
```
Pretty short paper, quick to read. They describe how they extend the MIMIC-IV-ECG dataset with basic per-lead ECG parameters/features, plotted ECG images, and more detailed text descriptions generated by GPT-4o (based on the original short ECG text reports and the extracted ECG parameters/features).
```

##### [25-09-06] [paper546]
- OneCAT: Decoder-Only Auto-Regressive Model for Unified Understanding and Generation
 [[pdf]](https://arxiv.org/abs/2509.03498) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/OneCAT%20Decoder-Only%20Auto-Regressive%20Model%20for%20Unified%20Understanding%20and%20Generation.pdf)
- `arxiv, 2025-09`
- [Vision-Language Models]
```
Well-written and interesting paper. Interesting approach, seemingly impressive results. I wanted to read another unified multimodal model paper, to compare with "Muddit: Liberating Generation Beyond Text-to-Image with a Unified Discrete Diffusion Model". The related work in Section 2 was good background for me. Not the most straightforward training setup perhaps, incorporating distillation from a pretrained ViT/MLLM. Also, I didn't realize until reaching the "Text-to-Image Generation" paragraph in Section 3.1 that they also utilize a pretrained image VAE, although just the decoder at test-time.
```

##### [25-09-05] [paper545]
- Neural Discrete Representation Learning
 [[pdf]](https://arxiv.org/abs/1711.00937) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Neural%20Discrete%20Representation%20Learning.pdf)
- `NeurIPS 2017`
- [Miscellaneous] 
```
The VQ-VAE paper, fairly interesting. I read this as background for the work on unified discrete diffusion models, but I'm not sure this gave that much compared to the papers I've already read. Very quick to read though, and still a bit interesting.
```

##### [25-09-05] [paper544]
- MaskGIT: Masked Generative Image Transformer 
 [[pdf]](https://openaccess.thecvf.com/content/CVPR2022/html/Chang_MaskGIT_Masked_Generative_Image_Transformer_CVPR_2022_paper.html) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/MaskGIT%20Masked%20Generative%20Image%20Transformer.pdf)
- `CVPR 2022`
- [Miscellaneous]
```
Quite interesting paper. I read this as background for the work on unified discrete diffusion models, but it did perhaps seem a bit less relevant/useful than I had expected. Still pretty happy that I chose to read this though.
```

##### [25-09-02] [paper543]
- Muddit: Liberating Generation Beyond Text-to-Image with a Unified Discrete Diffusion Model
 [[pdf]](https://arxiv.org/abs/2505.23606) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Muddit%20Liberating%20Generation%20Beyond%20Text-to-Image%20with%20a%20Unified%20Discrete%20Diffusion%20Model.pdf)
- `arxiv, 2025-05`
- [Vision-Language Models], [Diffusion Models] 
```
Well-written and interesting paper, I enjoyed reading this. Pretty much everything is clearly explained and easy to follow, and makes intuitive sense as well. Happy that I decided to read this. The results in Table 2 are perhaps not overly impressive though, and the image captioning examples in Figure 5 also contain quite a few small errors? The step-by-step generation examples in Figure 11 and 12 are interesting, would be nice to see more similar examples, also for the text-to-image setting.
```

##### [25-09-02] [paper542]
- Unified Multimodal Discrete Diffusion
 [[pdf]](https://arxiv.org/abs/2503.20853) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Unified%20Multimodal%20Discrete%20Diffusion.pdf)
- `arxiv, 2025-03`
- [Vision-Language Models], [Diffusion Models] 
```
Somewhat interesting paper. Section 3 is pretty interesting, but then it feels like quite a few things were a bit unclear, at least to me. Not sure if this helped me understand these types of models better, not as much as I was hoping for at least. The results don't seem overly encouraging, their diffusion-based model is 13x slower to train, and at least not clearly faster for the same performance at test-time (compared to the AR baseline)?
```

##### [25-09-01] [paper541]
- LaViDa: A Large Diffusion Language Model for Multimodal Understanding
 [[pdf]](https://arxiv.org/abs/2505.16839) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/LaViDa%20A%20Large%20Diffusion%20Language%20Model%20for%20Multimodal%20Understanding.pdf)
- `arxiv, 2025-05`
- [Language Models], [Vision-Language Models], [Diffusion Models] 
```
Well-written and quite interesting paper. Everything in Section 1 - 3 is clearly explained and easy to follow, I quite enjoyed reading it. This approach is basically the same as LLaVA but using a diffusion LLM instead of a regular one, with some proposed tweaks. These tweaks (complementary masking, Prefix-DLM) also make sense I think. Not entirely sure how much a diffusion VLM like this adds compared e.g. LLaVA in practice though, it's not even faster when they set K = L (unmask one token per iteration) (see Figure 4.b). But either way, I found the paper interesting overall and quite enjoyed reading it, I think this was a good second paper to read after that survey on diffusion language models, it summarized and explained some things well.
```

##### [25-08-31] [paper540]
- Discrete Diffusion in Large Language and Multimodal Models: A Survey
 [[pdf]](https://arxiv.org/abs/2506.13759) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Discrete%20Diffusion%20in%20Large%20Language%20and%20Multimodal%20Models%20A%20Survey.pdf)
- `arxiv, 2025-06`
- [Language Models], [Vision-Language Models], [Diffusion Models]
```
Quite long survey paper, I didn't read absolutely everything in detail. Overall well-written and quite interesting. I haven't read anything about discrete diffusion models / diffusion language models before and I was just curious about all this, feels like a lot of things are happening within this space atm. And yes, this survey provided a pretty good introduction I think, showed what the main existing models are and what people are working on. Not a perfect survey, but it did the job. In particular, I found Section 1, Figure 1, Section 2.A, Section 2.C, Figure 1 and Figure 3 useful/interesting.
```

##### [25-08-31] [paper539]
- BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models
 [[pdf]](https://proceedings.mlr.press/v202/li23q/li23q.pdf) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/BLIP-2%20Bootstrapping%20Language-Image%20Pre-training%20with%20Frozen%20Image%20Encoders%20and%20Large%20Language%20Models.pdf)
- `ICML 2023`
- [Language Models], [Vision-Language Models]
```
Well-written and quite interesting. As a ~paper~ I definitely liked this more than the LLaVA papers, feels more high-quality overall, and I quite enjoyed reading this. The ~method~ is probably a bit more complex though, uses a much bigger model to align image and text. Still think it was pretty useful to read this though.
```

##### [25-08-31] [paper538]
- Improved Baselines with Visual Instruction Tuning
 [[pdf]](https://arxiv.org/abs/2310.03744) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Improved%20Baselines%20with%20Visual%20Instruction%20Tuning.pdf)
- `CVPR 2024`
- [Language Models], [Vision-Language Models]
```
The LLaVA-1.5 paper, quite interesting. Just small tweaks/improvements compared to LLaVA really (2-layer MLP projector instead of single linear layer, VQA and some other datasets added to the instruction-following data, higher-res CLIP model for the image encoder, later version of Vicuna for the LLM with 13B params instead of 7B), the overall approach is still very simple. Not sure how much reading this added compared to the LLaVA paper, but quick to read and still quite interesting, it also summarizes LLaVA well.
```

##### [25-08-30] [paper537]
- Visual Instruction Tuning
 [[pdf]](https://arxiv.org/abs/2304.08485) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Visual%20Instruction%20Tuning.pdf)
- `NeurIPS 2023`
- [Language Models], [Vision-Language Models]
```
The LLaVA paper, quite interesting. Doesn't quite "feel" like a typical NeurIPS paper though, not a lot of method details, not an overly extensive evaluation etc. But, the core approach in Section 4 is interesting, conceptually simple. Probably good to have read this, to know exactly what other papers are referring to etc.
```

##### [25-08-29] [paper536]
- MEIT: Multimodal Electrocardiogram Instruction Tuning on Large Language Models for Report Generation
 [[pdf]](https://arxiv.org/abs/2403.04945) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/MEIT%20Multimodal%20Electrocardiogram%20Instruction%20Tuning%20on%20Large%20Language%20Models%20for%20Report%20Generation.pdf)
- `ACL 2025`
- [ML for Medicine/Healthcare], [ECGs], [Language Models]
```
Quite interesting paper. Overall quite similar compared to other papers on ECGs + language that I've read recently. Very difficult to know how well this approach actually works though, they just compare using different LLMs within their own approach, and the metrics are just general text generation quality metrics. This is true for basically all these ECG + language models, at least personally I find it difficult to know how well they actually work, how close they are to something that would be practically useful.
```

##### [25-08-29] [paper535]
- anyECG-Chat: A Generalist ECG-MLLM for Flexible ECG Input and Multi-Task Understanding
 [[pdf]](https://arxiv.org/abs/2506.00942) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/anyECG-Chat%20A%20Generalist%20ECG-MLLM%20for%20Flexible%20ECG%20Input%20and%20Multi-Task%20Understanding.pdf)
- `arxiv, 2025-06`
- [ML for Medicine/Healthcare], [ECGs], [Language Models]
```
Well-written and quite interesting paper. The approach makes sense overall I think. They create quite interesting datasets, seems reasonable to try and extend with more varying types of ECG inputs. I didn't analyze the results in a lot of details, I find it a bit difficult to judge how impressive the performance actually is for these types of models.
```

##### [25-08-28] [paper534]
- ECG-Chat: A Large ECG-Language Model for Cardiac Disease Diagnosis
 [[pdf]](https://arxiv.org/abs/2408.08849) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/ECG-Chat%20A%20Large%20ECG-Language%20Model%20for%20Cardiac%20Disease%20Diagnosis.pdf)
- `ICME 2025`
- [ML for Medicine/Healthcare], [ECGs], [Language Models] 
```
Interesting paper. Quite a lot of things here which intuitively makes sense to me. Interesting that they used NeuroKit2 to extend the text report for each ECG in the ECG encoder training, and that this seems to make such a big difference in Table 1. Interesting that they use GPT-4o to create instruction tuning datasets based on MIMIC-IV-ECG. However, seems like the report generation doesn't really work without DDP (Table 2), RAG or DSPy (Table 7)? These approaches in general are probably limited by the available public datasets atm?
```

##### [25-08-28] [paper533]
- ECG-LM: Understanding Electrocardiogram with a Large Language Model
 [[pdf]](https://spj.science.org/doi/10.34133/hds.0221) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/ECG-LM%20Understanding%20Electrocardiogram%20with%20a%20Large%20Language%20Model.pdf)
- `Health Data Science, 2025`
- [ML for Medicine/Healthcare], [ECGs], [Language Models] 
```
Quite interesting and quite well-written paper. The general approach is interesting, but I found some things a bit unclear, especially how they used the PTB-XL+ dataset to extract lead-specific text descriptions. Also, they both pretrain the model and then evaluate zero-shot classification on PTB-XL, but they don't really specify any train/test splits?
```

##### [25-08-25] [paper532]
- Q-Heart: ECG Question Answering via Knowledge-Informed Multimodal LLMs
 [[pdf]](https://arxiv.org/abs/2505.06296) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Q-Heart%20ECG%20Question%20Answering%20via%20Knowledge-Informed%20Multimodal%20LLMs.pdf)
- `arxiv, 2025-05`
- [ML for Medicine/Healthcare], [ECGs], [Language Models]
```
Well-written and interesting paper, I quite enjoyed reading this. The approach is interesting and overall makes intuitive sense to me. Things are explained well overall. Seems to perform well compared to baselines, but difficult for me to judge how significant these performance differences are, or to judge how close this is to something that actually would be useful in practice. The ablation in Table 4 is interesting, but I don't understand what "w/o ET-Mapper" means, is the ECG embedding not incorporated at all then? The ECG info is only given indirectly via the retrieved top text report which is included in the prompt? But if so, shouldn't this give worse performance than "w/o Pos-Encoder"?
```

##### [25-08-25] [paper531]
- Electrocardiogram-Language Model for Few-Shot Question Answering with Meta Learning
 [[pdf]](https://arxiv.org/abs/2410.14464) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Electrocardiogram-Language%20Model%20for%20Few-Shot%20Question%20Answering%20with%20Meta%20Learning.pdf)
- `CHIL 2025`
- [ML for Medicine/Healthcare], [ECGs], [Language Models]
```
Fairly interesting paper, but unfortunately I didn't really understand the overall meta-learning setup, I guess I don't know the meta-learning basics well enough. Therefore, it's very difficult for me to judge how impressive these results are, if the model actually seems to work. Figure 1 with the general approach illustrated there is quite interesting though, to combine a frozen LLM with a frozen ECG feature extractor in that way, this makes some sense to me.
```

##### [25-08-25] [paper530]
- Predicting Cardiovascular Disease Risk Using Photoplethysmography and Deep Learning
 [[pdf]](https://journals.plos.org/globalpublichealth/article?id=10.1371/journal.pgph.0003204) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Predicting%20Cardiovascular%20Disease%20Risk%20Using%20Photoplethysmography%20and%20Deep%20Learning.pdf)
- `PLOS Global Public Health, 2024`
- [ML for Medicine/Healthcare], [Time Series]
```
Somewhat interesting paper. The performance of their PPG-based model doesn't seem overly impressive, basically the same as for the baseline that replaces their 5 PPG features with height, weight and systolic blood pressure. And, I'm not quite sure if I buy that it would be easier to collect PPG measurements than height/weight and blood pressure in resource-limited settings.
```

##### [25-08-24] [paper529]
- Beyond Sensor Data: Foundation Models of Behavioral Data from Wearables Improve Health Predictions
 [[pdf]](https://arxiv.org/abs/2507.00191) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Beyond%20Sensor%20Data%20Foundation%20Models%20of%20Behavioral%20Data%20from%20Wearables%20Improve%20Health%20Predictions.pdf)
- `ICML 2025`
- [ML for Medicine/Healthcare], [Time Series]
```
Interesting paper, a natural follow-up for "Large-scale Training of Foundation Models for Wearable Biosignals" (ICLR 2024) from Apple. Again, cool to see what data they can extract directly from Apple watch users, and what this data can be used for. Nothing groundbreaking in terms of models/methods, and there are probably details missing if one actually would want to implement something similar in practice, but I still quite enjoyed reading this. Easy to follow, and just quite interesting to get an overview of Apple's data and what they're working on within this domain.
```

##### [25-08-23] [paper528]
- MOMENT: A Family of Open Time-series Foundation Models
 [[pdf]](https://arxiv.org/abs/2402.03885) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/MOMENT%20A%20Family%20of%20Open%20Time-series%20Foundation%20Models.pdf)
- `ICML 2024`
- [Time Series] 
```
Well-written overall, somewhat interesting. I read this mostly just to get a sense of what data these general-purpose time-series FMs are trained on, how they are evaluated etc. I didn't analyze the results in much detail.
```

##### [25-08-22] [paper527]
- Large-scale Training of Foundation Models for Wearable Biosignals
 [[pdf]](https://arxiv.org/abs/2312.05409) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Large-scale%20Training%20of%20Foundation%20Models%20for%20Wearable%20Biosignals.pdf)
- `ICLR 2024`
- [ML for Medicine/Healthcare], [ECGs], [Time Series] 
```
Interesting paper, cool to see what data Apple can extract directly from Apple Watch users. 4-channel PPG and 1-channel ECG (user wears the watch and then also puts a finger on the crown). Interesting that the model trained on PPG is more predictive than the ECG model. I was not overly interested in the model/method specifics, I mainly focused on the data and the downstream tasks.
```

##### [25-08-22] [paper526]
- PaPaGei: Open Foundation Models for Optical Physiological Signals
 [[pdf]](https://arxiv.org/abs/2410.20542) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/PaPaGei%20Open%20Foundation%20Models%20for%20Optical%20Physiological%20Signals.pdf)
- `ICLR 2025`
- [ML for Medicine/Healthcare], [Time Series] 
```
Well-written and quite interesting paper. The proposed PaPaGei-S does perhaps seem a bit ad hoc (adding MAE losses for predicting IPA and SQI), but at the same time it generally makes sense to utilize domain-specific knowledge I think. The performance gain compared to PaPaGei-P (Table 3 & 4) is not huge, but quite consistently a bit better at least. Sensible evaluation, good baselines, and seems to perform well overall. I found Figure 6 a bit odd though, it seems strange that both "sVRI + SQI+ and "sVRI + IPA" are worse than "sVRI", but "sVRI + SQI + IPA" is better than "sVRI"? Also seems strange that the 35M param model is worse than the 5M model, but 139M model is better than 35M model?
```

##### [25-08-21] [paper525]
- SuPreME: A Supervised Pre-training Framework for Multimodal ECG Representation Learning
 [[pdf]](https://arxiv.org/abs/2502.19668) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/SuPreME%20A%20Supervised%20Pre-training%20Framework%20for%20Multimodal%20ECG%20Representation%20Learning.pdf)
- `arxiv, 2025-02`
- [ML for Medicine/Healthcare], [ECGs]
```
Quite interesting paper. Figure 1 - 3 are small and very dense, contain a lot of information, but overall illustrate things well once you zoom in and study them carefully. I liked Section 3.2, they explain things with a lot of details there, but still easy to follow. I don't understand the zero-shot classification thing though, how do they construct these dataset-specific query lists? Based on what? "SuPreME is evaluated on six ~unseen~ datasets using ~dataset-specific~ prompts", isn't this a bit of a contradiction? Also, in Table 4 - 9 the performance of their method drops significantly when they make different modifications, drops well below the MERL baseline for example. I.e., seems like their method is quite sensitive? Isn't this is a pretty clear weakness?
```

##### [25-08-21] [paper524]
- From Token to Rhythm: A Multi-Scale Approach for ECG-Language Pretraining
 [[pdf]](https://openreview.net/forum?id=fUjkoGUre0) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/From%20Token%20to%20Rhythm%20A%20Multi-Scale%20Approach%20for%20ECG-Language%20Pretraining.pdf)
- `ICML 2025`
- [ML for Medicine/Healthcare], [ECGs]
```
Quite interesting paper, but very similar to the previous paper I read "Boosting Masked ECG-Text Auto-Encoders as Discriminative Learners". They evaluate their models in basically the same way, Table 2, 3 & 4 in the two papers can be directly compared, and they achieve very similar performance. It's probably sufficient to read just one of these two papers.
```

##### [25-08-20] [paper523]
- Boosting Masked ECG-Text Auto-Encoders as Discriminative Learners
 [[pdf]](https://openreview.net/forum?id=mM65b81LdM) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Boosting%20Masked%20ECG-Text%20Auto-Encoders%20as%20Discriminative%20Learners.pdf)
- `ICML 2025`
- [ML for Medicine/Healthcare], [ECGs]
```
Interesting and quite well-written paper, but at least I personally found parts of the method description confusing. I don't quite understand why the ETM loss is used? Yes I see in Table 12 that it improves the performance a tiny bit, but the motivation for it is not clear to me? Where does this come from? Is it standard to include this when doing masked modelling with two modalities? I don't really think I've seen this before? Also, is the cross-attention fusion module really needed? This is only used during the pretraining, or?
```

##### [25-08-17] [paper522]
- Knowledge-Enhanced Multimodal ECG Representation Learning with Arbitrary-Lead Inputs
 [[pdf]](https://arxiv.org/abs/2502.17900) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Knowledge-Enhanced%20Multimodal%20ECG%20Representation%20Learning%20with%20Arbitrary-Lead%20Inputs.pdf)
- `arxiv, 2025-02`
- [ML for Medicine/Healthcare], [ECGs]
```
Interesting and quite well-written paper. This is an extension of MERL ("Zero-Shot ECG Classification with Multimodal Learning and Test-time Clinical Knowledge Enhancement" (ICML 2024)) from the same group. The changes compared to MERL are not huge, but make sense overall and seem to improve the performance at least to some extent. Figure 7 Right is interesting, I was surprised that doing such aggressive lead masking (masking at least 9 leads) is optimal, also for the performance on 12-lead ECGs. Their performance with missing leads in Figure 6 does also seem quite impressive, it doesn't drop that much from 12-lead to single-lead. Although the baseline there, just filling missing leads with zeros for MERL, doesn't seem like the strongest possible baseline.
```

##### [25-08-17] [paper521]
- Wearable-Echo-FM: An ECG-Echo Foundation Model for Single Lead Electrocardiography
 [[pdf]](https://www.medrxiv.org/content/10.1101/2025.06.10.25329163v2) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Wearable-Echo-FM%20An%20ECG-Echo%20Foundation%20Model%20for%20Single%20Lead%20Electrocardiography.pdf)
- `medrxiv, 2025-06`
- [ML for Medicine/Healthcare], [ECGs]
```
Interesting paper, pretty quick and easy to read. Quite impressive datasets, interesting that they pretrain the model using text reports and a CLIP loss, results look pretty good etc.
```

##### [25-08-16] [paper520]
- Artificial Intelligence for Hemodynamic Monitoring With a Wearable Electrocardiogram Monitor
 [[pdf]](https://www.nature.com/articles/s43856-024-00730-5) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Artificial%20Intelligence%20for%20Hemodynamic%20Monitoring%20With%20a%20Wearable%20Electrocardiogram%20Monitor.pdf)
- `Communications Medicine, 2025`
- [ML for Medicine/Healthcare], [ECGs]
```
Interesting and really well-written paper, I enjoyed reading this. Everything is clearly explained, the medical background is interesting and easy to understand, the approach makes sense, interesting datasets etc. High-quality stuff.
```

##### [25-08-15] [paper519]
- SensorLM: Learning the Language of Wearable Sensors
 [[pdf]](https://arxiv.org/abs/2506.09108) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/SensorLM%20Learning%20the%20Language%20of%20Wearable%20Sensors.pdf)
- `NeurIPS 2025`
- [ML for Medicine/Healthcare], [Time Series], [Vision-Language Models]
```
Interesting paper, the general idea of signal-language models is definitely interesting, just not entirely sure how useful it would be in practice? The zero-shot classification capability seems like it could be useful, I think. The results in Figure 5, Table 19 and Table 20 are not overly impressive though, if you compare with the results for LSM-1 and LSM-2 in Table 2 and Table 4 in "LSM-2: Learning from Incomplete Wearable Sensor Data". SensorLM has similar performance to all the SSL baselines, which are clearly outperformed by both LSM-1 and LSM-2. I.e., it seems like the masked autoencoder approach of LSM is more effective. But of course, the signal-language approach also adds novel capabilities (in particular, zero-shot prediction), some kind of trade-off I suppose.
```

##### [25-08-15] [paper518]
- LSM-2: Learning from Incomplete Wearable Sensor Data
 [[pdf]](https://arxiv.org/abs/2506.05321) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/LSM-2%20Learning%20from%20Incomplete%20Wearable%20Sensor%20Data.pdf)
- `arxiv, 2025-06`
- [ML for Medicine/Healthcare], [Time Series]
```
Quite interesting and well-written paper, this is a direct follow-up of "Scaling Wearable Foundation Models" (LSM-1). The method difference compared to LSM-1 seems reasonable, to better handle missingness in the input data, relatively small/simple changes. The difference in performance on the downstream tasks (Table 2 and 4) is quite small indeed though. But both LSM-1 and LSM-2 clealry outperform the contrastive-based baselines (SimCLR, DINO, MSN) here at least. Not sure how much reading this paper added compared to just reading the LSM-1 paper, but still quite interesting to see Google's most recent model within this domain.
```

##### [25-08-15] [paper517]
- Scaling Wearable Foundation Models
 [[pdf]](https://openreview.net/forum?id=yb4QE6b22f) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Scaling%20Wearable%20Foundation%20Models.pdf)
- `ICLR 2025`
- [ML for Medicine/Healthcare], [Time Series]
```
Quite interesting and overall well-written paper. Mostly focusing on scaling results (as the title suggests, of course), not a lot of downstream tasks. So, that could be more interesting. Cool dataset though, collected from real-world users of Fitbit Sense 2 and Google Pixel Watch 2. I was surprised that they use ViT models for this type of data, the input is a "sensor matrix" of 26 signals (derived from 5 sensors) x 300 minutes. Pretty good introduction to this type of data, I think, pretty good background.
```

##### [25-08-14] [paper516]
- Large Language Models are Powerful Electronic Health Record Encoders
 [[pdf]](https://arxiv.org/abs/2502.17403) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Large%20Language%20Models%20are%20Powerful%20Electronic%20Health%20Record%20Encoders.pdf)
- `arxiv, 2025-02`
- [ML for Medicine/Healthcare], [Language Models], [EHRs] 
```
Well-written and interesting paper. Longer than what I usually read, 20+ pages, but I still quite enjoyed reading this. Everything is clearly explained, and I do think this approach makes quite a lot of sense, especially in terms of its flexibility ("This limitation underscores a key challenge in adapting domain-specific models to external datasets, even with considerable manual effort. In contrast, the LLM-based models required only a mapping from clinical concepts to their natural language descriptions, which were directly incorporated into the Markdown-based serialization. This simplified integration process substantially reduced implementation overhead and emphasized the strong generalization ability of LLM-based encodings across diverse coding systems and healthcare domains"). The LLM-based approach also seems to perform quite well compared to reasonable baselines.
```

##### [25-08-13] [paper515]
- Benchmarking Foundation Models with Multimodal Public Electronic Health Records
 [[pdf]](https://arxiv.org/abs/2507.14824) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Benchmarking%20Foundation%20Models%20with%20Multimodal%20Public%20Electronic%20Health%20Records.pdf)
- `arxiv, 2025-07`
- [ML for Medicine/Healthcare], [EHRs]
```
Quite interesting paper, their code looks potentially useful. The results in Table 2 & 3 and Figure 4 are quite interesting, that "Baseline + Text" is better than both "Baseline + Image" and "Baseline + Image + Text". Images seem to add basically no information once the text notes are available here.
```

##### [25-08-13] [paper514]
- Agent-Based Feature Generation from Clinical Notes for Outcome Prediction
 [[pdf]](https://www.arxiv.org/abs/2508.01956) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Agent-Based%20Feature%20Generation%20from%20Clinical%20Notes%20for%20Outcome%20Prediction.pdf)
- `arxiv, 2025-08`
- [ML for Medicine/Healthcare], [Language Models], [EHRs] 
```
Quite interesting paper, the proposed approach is conceptually interesting and makes some sense, the results seem quite promising etc. HOWEVER, they provide no technical details whatsoever? They don't specify which LLMs are used in their different agents? They don't describe how these are prompted? Basically, they give no detailed description of how their agent-based system actually works, at all? Also, the evaluation is only performed on a single small dataset of 147 patients.
```

##### [25-08-12] [paper513]
- Mixture-of-Agents Enhances Large Language Model Capabilities
 [[pdf]](https://openreview.net/forum?id=h0ZfDIrj7T) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Mixture-of-Agents%20Enhances%20Large%20Language%20Model%20Capabilities.pdf)
- `ICLR 2025`
- [Language Models] 
```
Quite interesting and well-written paper. Conceptually simple and quite intuitive approach, neat that it also seems to work well overall. (seems like Figure 3 is covering the bottom row of Table 2 though^^)
```

##### [25-08-12] [paper512]
- MoMA: A Mixture-of-Multimodal-Agents Architecture for Enhancing Clinical Prediction Modelling
 [[pdf]](https://arxiv.org/abs/2508.05492) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/MoMA%20A%20Mixture-of-Multimodal-Agents%20Architecture%20for%20Enhancing%20Clinical%20Prediction%20Modelling.pdf)
- `arxiv, 2025-08`
- [ML for Medicine/Healthcare], [Language Models], [EHRs]
```
Well-written and quite interesting paper. Things are explained well, Figure 1 gives a good overview. The approach is conceptually quite straightforward, seems to perform quite well compared to a vision-language model at least. A pretty nice paper to read.
```

##### [25-08-11] [paper511]
- Decoding-Based Regression
 [[pdf]](https://openreview.net/forum?id=avUQ8jguxg) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Decoding-Based%20Regression.pdf)
- `TMLR, 2025`
- [Language Models]
```
Quite interesting paper. Everything is solid and results are reasonable etc, but I was just hoping for a bit more, not entirely sure how much this added compared to "Performance Prediction for Large Systems via Text-to-Text Regression" and "OmniPred: Language Models as Universal Regressors" which I already have read. I did not follow much at all in Secton 3.3, difficult for me to judge how valuable this theoretical analysis is.
```

##### [25-08-10] [paper510]
- OmniPred: Language Models as Universal Regressors
 [[pdf]](https://openreview.net/forum?id=t9c3pfrR1X) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/OmniPred%20Language%20Models%20as%20Universal%20Regressors.pdf)
- `TMLR, 2024`
- [Language Models] 
```
Quite interesting paper. I thought this was going to provide some more method details and background than "Performance Prediction for Large Systems via Text-to-Text Regression" which I read before, but this didn't really give that much more. Still a solid paper though.
```

##### [25-08-10] [paper509]
- Performance Prediction for Large Systems via Text-to-Text Regression
 [[pdf]](https://arxiv.org/abs/2506.21718) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Performance%20Prediction%20for%20Large%20Systems%20via%20Text-to-Text%20Regression.pdf)
- `arxiv, 2025-06`
- [Language Models] 
```
Well written and interesting paper, I quite enjoyed reading it. Everything is explained well, but I should probably go back and read "OmniPred: Language Models as Universal Regressors" from the same group for more details about the actual method.
```

##### [25-08-09] [paper508]
- Large Language Models for Medical Forecasting -- Foresight 2
 [[pdf]](https://arxiv.org/abs/2412.10848) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Large%20Language%20Models%20for%20Medical%20Forecasting%20--%20Foresight%202.pdf)
- `arxiv, 2024-12`
- [ML for Medicine/Healthcare], [Language Models], [EHRs]
```
Interesting paper, overall I quite enjoyed reading this. But, I still don't understand what the input to their model is?! Is it the actual patient timeline with temporal separator tokens etc, or is it just the reconstructed clinical note at the bottom of Figure 1? Also, what loss is used in the risk forecasting fine-tuning in Section 2.4?
```

##### [25-08-08] [paper507]
- SurvivEHR: A Competing Risks, Time-To-Event Foundation Model for Multiple Long-Term Conditions From Primary Care Electronic Health Records
 [[pdf]](https://www.medrxiv.org/content/10.1101/2025.08.04.25332916v1) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/SurvivEHR%20A%20Competing%20Risks%2C%20Time-To-Event%20Foundation%20Model%20for%20Multiple%20Long-Term%20Conditions%20From%20Primary%20Care%20Electronic%20Health%20Records.pdf)
- `medrxiv, 2025-08`
- [ML for Medicine/Healthcare], [EHRs] 
```
Interesting paper. Quite long, took me a while to get through everything, and I was pretty tired towards the end. Trained on a lot of data, primary care data, which is cool. Figure 1 is nice. Figure 4 is quite messy, difficult to interpret. I'm confused by the "Causal value prediction" paragraph in "Model architecture implementation", is this regression NLL loss added to the survival loss? What is actually the final loss that's used to train the model? Not clear to me how different their approach actually is compared to MOTOR ("Recently, this limitation has been overcome with MOTOR [45], a self-supervised, time-to-event (TTE) foundation model but this is limited to approximations of time-to-event distributions using Piecewise Exponential Artificial Neural Networks"), would have been interesting to see a direct comparison. I also don't quite understand why their model can't do zero-shot prediction?
```

##### [25-08-08] [paper506]
- FoMoH: A Clinically Meaningful Foundation Model Evaluation for Structured Electronic Health Records
 [[pdf]](https://arxiv.org/abs/2505.16941) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/FoMoH%20A%20Clinically%20Meaningful%20Foundation%20Model%20Evaluation%20for%20Structured%20Electronic%20Health%20Records.pdf)
- `arxiv, 2025-05`
- [ML for Medicine/Healthcare], [EHRs] 
```
Quite well written and quite interesting paper. What they set out to do is great and very interesting (training and evaluating 6 EHR FMs on in-house data from than 5 million patients, on different downstream prediction tasks), but then I feel like it's a bit difficult to know what main conclusions to draw. CEHR-GPT and MOTOR seems to be the two top-performing models, but can we say anything about the next-token prediction vs time-to-event pretraining loss? Would have been nice with a direct comparison of the these two.
```

##### [25-08-07] [paper505]
- Adaptable Cardiovascular Disease Risk Prediction from Heterogeneous Data using Large Language Models
 [[pdf]](https://arxiv.org/abs/2505.24655) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Adaptable%20Cardiovascular%20Disease%20Risk%20Prediction%20from%20Heterogeneous%20Data%20using%20Large%20Language%20Models.pdf)
- `arxiv, 2025-05`
- [ML for Medicine/Healthcare], [Language Models] 
```
Well written and interesting paper. Everything is solid, I quite enjoyed reading it (although I did get pretty tired towards the end, it's a quite long paper). A conceptually straightforward approach, and seems to work well overall. Not sure how impressive/surprising the "adapting to textual patient representations" results in Figure 6 are though, given that the textual representations are LLM-generated from the structured patient representations that the original AdaCVD model is fine-tuned on.
```

##### [25-08-07] [paper504]
- MedMod: Multimodal Benchmark for Medical Prediction Tasks with Electronic Health Records and Chest X-Ray Scans
 [[pdf]](https://raw.githubusercontent.com/mlresearch/v287/main/assets/elsharief25a/elsharief25a.pdf) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/MedMod%20Multimodal%20Benchmark%20for%20Medical%20Prediction%20Tasks%20with%20Electronic%20Health%20Records%20and%20Chest%20X-Ray%20Scans.pdf)
- `CHIL 2025`
- [ML for Medicine/Healthcare], [EHRs] 
```
Quite interesting, well written and solid overall. 18k unique patients with both EHR and CXR data in the data they use. For "In-hospital mortality" in Table 3, CXR-only is quite a lot worse than EHR-only, but still EHR + CXR improves over EHR-only, which I find a bit interesting.
```

##### [25-08-07] [paper503]
- Assessing the Importance of Primary Care Diagnoses in the UK Biobank
 [[pdf]](https://link.springer.com/article/10.1007/s10654-023-01095-0) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Assessing%20the%20Importance%20of%20Primary%20Care%20Diagnoses%20in%20the%20UK%20Biobank.pdf)
- `European Journal of Epidemiology, 2024`
- [Miscellaneous]
```
I read this just to get some additional background on the UK biobank study and data. Of course I'm not able to fully appreciate everything in an epidemiology paper like this, but still somewhat interesting.
```

##### [25-08-06] [paper502]
- Foundation Model of Electronic Medical Records for Adaptive Risk Estimation
 [[pdf]](https://arxiv.org/abs/2502.06124) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Foundation%20Model%20of%20Electronic%20Medical%20Records%20for%20Adaptive%20Risk%20Estimation.pdf)
- `GigaScience, 2025`
- [ML for Medicine/Healthcare], [EHRs] 
```
Well written and quite interesting paper. Everything is clearly explained, I quite enjoyed reading this. Also provides a good summary of the ETHOS model, I think it helped me understand how that works a bit better. Simulating >= 100 future patient timelines and estimating probabilities for different critical events based on these is a quite intuitive approach, albeit somewhat computationally inefficient I suppose. Really neat that this can be done zero-shot without any re-training though.
```

##### [25-08-06] [paper501]
- MOTOR: A Time-to-Event Foundation Model For Structured Medical Records
 [[pdf]](https://openreview.net/forum?id=NialiwI2V6) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/MOTOR%20A%20Time-to-Event%20Foundation%20Model%20For%20Structured%20Medical%20Records.pdf)
- `ICLR 2024`
- [ML for Medicine/Healthcare], [EHRs] 
```
 Well written and quite interesting paper. Their approach turned out to be more similar to the other EHR-based FM papers I've read though, I think. I just expected this to stand out a bit more. Like for those other papers, I also feel like there's quite a lot of details which are still missing here. At least personally, I feel like I wouldn't know exactly how to apply this in practice just by reading the paper. Overall, it also feels like this paper is a bit too long for the 9 page conference format, they have to refer to the appendix quite a lot. But overall this seems like very solid work, definitely.
```

##### [25-08-05] [paper500]
- LabTOP: A Unified Model for Lab Test Outcome Prediction on Electronic Health Records
 [[pdf]](https://arxiv.org/abs/2502.14259) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/LabTOP%20A%20Unified%20Model%20for%20Lab%20Test%20Outcome%20Prediction%20on%20Electronic%20Health%20Records.pdf)
- `CHIL 2025`
- [ML for Medicine/Healthcare], [EHRs] 
```
Well written and interesting paper, I enjoyed reading it. Novel and interesting approach (I've never seen anyone regressing continuous values in this way at least), sensible baselines, reasonable looking results, interesting ablations, everything just seems solid here.
```

##### [25-08-05] [paper499]
- Zero Shot Health Trajectory Prediction Using Transformer
 [[pdf]](https://www.nature.com/articles/s41746-024-01235-0) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Zero%20Shot%20Health%20Trajectory%20Prediction%20Using%20Transformer.pdf)
- `npj Digital Medicine, 2024`
- [ML for Medicine/Healthcare], [EHRs]
```
Well written and interesting paper, I quite enjoyed reading it. All figures etc are really neat. The method is pretty cool, that you can get zero-shot predictions of different things by simulating multiple future patient timelines (albeit a somewhat computationally inefficient approach, I suppose).
```

##### [25-08-03] [paper498]
- Foresight—A Generative Pretrained Transformer for Modelling of Patient Timelines Using Electronic Health Records: A Retrospective Modelling Study
 [[pdf]](https://www.thelancet.com/journals/landig/article/PIIS2589-7500(24)00025-6/fulltext) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Foresight%E2%80%94A%20Generative%20Pretrained%20Transformer%20for%20Modelling%20of%20Patient%20Timelines%20Using%20Electronic%20Health%20Records%20A%20Retrospective%20Modelling%20Study.pdf)
- `The Lancet Digital Health, 2024`
- [ML for Medicine/Healthcare], [EHRs]  
```
Quite interesting paper. Neat that they use both the free text and structured data in the EHRs ("uses named entity recognition and linking tools to convert EHR document text into structured, coded concepts"). But then I got a bit confused, found it difficult to understand exactly how the model actually works. Does the model just iteratively output tokens? I.e., for generating the "top N forecasts", they just run the model to output N tokens? But so how do they generate timelines as in Figure 4 in that case? The output tokens/concepts have no time information? But, output tokens can also be "patient demographics, such as age, gender, or ethnicity"? So, the second output token can thus be e.g. "age 50 years" as in the top example of Figure 4? And those put all other output tokens on a timeline like that? I also find it a bit difficult to interpret the results, how well the model actually works.
```

##### [25-08-03] [paper497]
- TransformEHR: Transformer-Based Encoder-Decoder Generative Model to Enhance Prediction of Disease Outcomes Using Electronic Health Records
 [[pdf]](https://www.nature.com/articles/s41467-023-43715-z) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/TransformEHR%20Transformer-Based%20Encoder-Decoder%20Generative%20Model%20to%20Enhance%20Prediction%20of%20Disease%20Outcomes%20Using%20Electronic%20Health%20Records.pdf)
- `Nature Communications, 2023`
- [ML for Medicine/Healthcare], [EHRs] 
```
Well written and quite interesting paper, gives a pretty good introduction to pretraining methods for EHR data I think. 255 million visits from 6.5 million patients, seems like a lot of data. The evaluation is not super extensive, but yes, seems to consistently outperform the BERT baseline. I don't quite understand how the model handles that different visits can have different numbers of ICD codes though, are the code embeddings just added together?
```

##### [25-08-01] [paper496]
- Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation
 [[pdf]](https://arxiv.org/abs/2302.09664) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Semantic%20Uncertainty%20Linguistic%20Invariances%20for%20Uncertainty%20Estimation%20in%20Natural%20Language%20Generation.pdf)
- `ICLR 2023`
- [Language Models], [Uncertainty Estimation] 
```
Well written and interesting paper. Yes, I should have read this before "Semantic Volume: Quantifying and Detecting both External and Internal Uncertainty in LLMs", this provided more background. The method here makes sense overall I think, but seems somewhat inconvenient having to "manually" classify each par of sentences, whether they ~mean~ the same thing or not. So yes, my initial impression is that the Semantic Volume method actually might be more neat, that you there sort of do this automatically by embedding sentences in a semantic space and measuring the volume. But yes, interesting stuff.
```

##### [25-08-01] [paper495]
- Deep Learning-based Prediction of Clinical Trial Enrollment with Uncertainty Estimates
 [[pdf]](https://arxiv.org/abs/2507.23607) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Deep%20Learning-based%20Prediction%20of%20Clinical%20Trial%20Enrollment%20with%20Uncertainty%20Estimates.pdf)
- `arxiv, 2025-07`
- [ML for Medicine/Healthcare]
```
Fairly interesting paper. Kind of neat to get some background info about this type of problem, clinical trials etc, but perhaps not exactly the type of paper I had expected. The method overall makes some sense though I think.
```

##### [25-07-31] [paper494]
- Semantic Volume: Quantifying and Detecting both External and Internal Uncertainty in LLMs
 [[pdf]](https://arxiv.org/abs/2502.21239) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Semantic%20Volume%20Quantifying%20and%20Detecting%20both%20External%20and%20Internal%20Uncertainty%20in%20LLMs.pdf)
- `arxiv, 2025-02`
- [Language Models], [Uncertainty Estimation]
```
Interesting paper, made me think quite a lot, in a good way. Would probably have been better to read some of the eariler papers first (especially "Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation"), but this is still a good starting point I think. There are probably aspects of all this which I'm unable to properly evaluate/appreciate atm, but the method overall mostly makes sense to me, and the results do seem promising. Seems like it performs well compared to good baselines.
```

##### [25-07-31] [paper493]
- TabLLM: Few-shot Classification of Tabular Data with Large Language Models
 [[pdf]](https://arxiv.org/abs/2210.10723) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/TabLLM%20Few-shot%20Classification%20of%20Tabular%20Data%20with%20Large%20Language%20Models.pdf)
- `AISTATS 2023`
- [Language Models]
```
Well written and fairly interesting paper. Things are clearly explained, Figure 1 illustrates what they do in a good way. Interesting to see this general method, that standard tabular data can be converted into text and fed as input to LLMs for classification tasks, and that this works quite well compared to standard, especially for few-shot settings. But then I lost interest a bit when getting to the detailes results and discussion etc.
```

##### [25-07-30] [paper492]
- Large Language Models Lack Essential Metacognition for Reliable Medical Reasoning
 [[pdf]](https://www.nature.com/articles/s41467-024-55628-6) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Large%20Language%20Models%20Lack%20Essential%20Metacognition%20for%20Reliable%20Medical%20Reasoning.pdf)
- `Nature Communications, 2025`
- [ML for Medicine/Healthcare], [Language Models] 
```
Well written and quite interesting paper. Nothing super special, but solid, I quite enjoyed reading it, I think it gave a pretty good introduction to these type of issues in LLMs. Quite interesting that GPT-4o actually is capable of outputting a confidence scores which are relatively accurate.
```

##### [25-07-29] [paper491]
- Foundation Models for Clinical Records at Health System Scale
 [[pdf]](https://arxiv.org/abs/2507.00574) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Foundation%20Models%20for%20Clinical%20Records%20at%20Health%20System%20Scale_2.pdf)
- `ICML Workshops 2025`
- [ML for Medicine/Healthcare], [EHRs]
```
Fairly interesting paper, just 4 pages long. Impressive dataset with 1.29 million unique patients. The overall pretraining approach makes sense, and neat that they can make predictions entirely zero-shot.
```

##### [25-07-29] [paper490]
- Towards Physician-Centered Oversight of Conversational Diagnostic AI
 [[pdf]](https://arxiv.org/abs/2507.15743) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Towards%20Physician-Centered%20Oversight%20of%20Conversational%20Diagnostic%20AI.pdf)
- `arxiv, 2025-07`
- [ML for Medicine/Healthcare], [Language Models] 
```
Well written and interesting paper. Quite long, I read Section 5 - 7 in less detail. Everything in Section 1 - 4 is clearly explained, very easy to follow and understand everything. Just reading Section 1 and looking at Figure 1 gives a good understanding of the core method, evaluation and results. I quite enjoyed reading this.
```

##### [25-07-27] [paper489]
- MedAgentBench: A Realistic Virtual EHR Environment to Benchmark Medical LLM Agents
 [[pdf]](https://arxiv.org/abs/2501.14654) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/MedAgentBench%20A%20Realistic%20Virtual%20EHR%20Environment%20to%20Benchmark%20Medical%20LLM%20Agents.pdf)
- `arxiv, 2025-01`
- [ML for Medicine/Healthcare], [Language Models] 
```
Quite interesting paper, pretty quick to read. Methods/datasets/results are not described in a lot of details, but everything seems reasonable. They evaluate many of the recent SOTA LLMs, still room to improve the performance. Nothing groundbreaking, but seems like a solid and probably quite useful benchmark.
```

##### [25-07-27] [paper488]
- ReAct: Synergizing Reasoning and Acting in Language Models
 [[pdf]](https://arxiv.org/abs/2210.03629) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/ReAct%20Synergizing%20Reasoning%20and%20Acting%20in%20Language%20Models.pdf)
- `ICLR 2023`
- [Language Models]
```
Well written and quite interesting paper. Illustrative and pretty cool examples in Figure 1. Don't think I can fully appreciate this, feel like there's some assumed LLM-related background knowledge that I lack, but still think this was fairly useful for me to read.
```

##### [25-07-26] [paper487]
- MedRAX: Medical Reasoning Agent for Chest X-ray
 [[pdf]](https://arxiv.org/abs/2502.02673) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/MedRAX%20Medical%20Reasoning%20Agent%20for%20Chest%20X-ray.pdf)
- `ICML 2025`
- [ML for Medicine/Healthcare], [Language Models] 
```
Well written and interesting paper, I quite enjoyed reading it. This overall approach is interesting, I must say, it definitely makes some intuitive sense to me. The performance gain compared to GPT-4o (the underlying LLM used in their agent) in Table 1 and 2 is not exactly huge though, how much is the performance actually improved by plugging GPT-4o into this agent system? A bit difficult for me to judge this I think.
```

##### [25-07-25] [paper486]
- Role of Large Language Models in the Multidisciplinary Decision-Making Process for Patients With Renal Cell Carcinoma: A Pilot Experience
 [[pdf]](https://www.nature.com/articles/s41698-025-01014-4) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Role%20of%20Large%20Language%20Models%20in%20the%20Multidisciplinary%20Decision-Making%20Process%20for%20Patients%20With%20Renal%20Cell%20Carcinoma%20A%20Pilot%20Experience.pdf)
- `npj Precision Oncology, 2025 (Brief Communication)`
- [ML for Medicine/Healthcare], [Language Models] 
```
Just 3 pages, very quick to read. Quite interesting, it gave a quick overview which I think is somewhat useful at least for me. They also describe a few other papers doing similar evaluations for other cancer types, with similar results overall.
```

##### [25-07-25] [paper485]
- Development and Validation of an Autonomous Artificial Intelligence Agent for Clinical Decision-Making in Oncology
 [[pdf]](https://www.nature.com/articles/s43018-025-00991-6) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Development%20and%20Validation%20of%20an%20Autonomous%20Artificial%20Intelligence%20Agent%20for%20Clinical%20Decision-Making%20in%20Oncology.pdf)
- `Nature Cancer, 2025`
- [ML for Medicine/Healthcare], [Language Models] 
```
Well written and interesting paper, I enjoyed reading it. Who knows how long it's going to take before an approach like this actually can be used in real-world clinical practice, demonstrated to be safe and effective, I guess I'm still a bit skeptical. But, just from a purely technical standpoint, this is actually really interesting and pretty cool! In particular, I find this really cool: "GPT-4 invoked the MedSAM tool twice to obtain segmentation masks from two images taken at different time points. Subsequently, GPT-4 used the calculator function with the appropriate values from MedSAM to determine that the tumor had grown by a factor of 2.14". I do also think that the agent-based approach makes some sense, as it enables multiple specialized models to be utilized in a really flexible way ("....preventing a singular entity from developing an all-encompassing foundational model. Instead, entities can leverage smaller, specialized models developed by those with direct access to the respective data.... this modular approach allows for individual validation, updating and regulatory compliance of each tool.... this modular approach also offers far superior explainability compared to a large, generalist black-box model, as physicians can investigate the output from each individual tool separately").
```

##### [25-07-25] [paper484]
- The Use of Artificial Intelligence for Cancer Therapeutic Decision-Making
 [[pdf]](https://ai.nejm.org/doi/full/10.1056/AIra2401164) [_unfortunately not open access, thus no annotated pdf_]
- `NEJM AI, 2025`
- [ML for Medicine/Healthcare], [Language Models] 
```
A non-technical review paper, fairly interesting. Just 6 pages long, very quick to read. I tend to find that it's pretty nice/useful to read these types of papers every once in a while, even though I'm not sure there are any major actionable takeaways for me here.
```

##### [25-07-24] [paper483]
- Large Language Models Are Poor Clinical Decision-Makers: A Comprehensive Benchmark
 [[pdf]](https://aclanthology.org/2024.emnlp-main.759/) [[annotated pdf]](https://github.com/fregu856/papers/blob/master/commented_pdfs/Large%20Language%20Models%20Are%20Poor%20Clinical%20Decision-Makers%20A%20Comprehensive%20Benchmark.pdf)
- `EMNLP 2024`
- [ML for Medicine/Healthcare], [Language Models] 
```
Quite interesting paper, overall a good paper for me to read I think, to get a better sense of how LLMs typi