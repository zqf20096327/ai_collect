Anomaly Detection for Autonomous Driving
==========

## Introduction

I developed my PhD dissertation titled [Anomaly Detection for Autonomous Driving](https://publikationen.bibliothek.kit.edu/1000189348) as a PhD student within the research group [Applied Technical Cognitive Systems ATKS](https://atks.aifb.kit.edu/english/index.php) within the [Institute of Applied Informatics and Formal Description Methods AIFB](https://www.aifb.kit.edu/english/index.php) at the [Karlsruhe Institute of Technology KIT](https://www.kit.edu/english/index.php). During this time, I was a research scientist in the group [Technical Cognitive Systems TKS](https://www.fzi.de/en/team/marius-zoellner/) at the [FZI Research Center for Information Technology](https://www.fzi.de/en/). My thesis was supervised by [J. Marius Zöllner](https://www.aifb.kit.edu/english/21_88.php) and [Hanno Gottschalk](https://www.tu.berlin/en/milz/about-us/head-of-chair).

BibTeX Citation:
```
@phdthesis{Bogdoll_PhD_2025,
    author = {Bogdoll, Daniel},
    title = {{Anomaly Detection for Autonomous Driving}}, 
    school = {Karlsruhe Institute of Technology (KIT)},
    year = {2025}
  }
```

This repository lists all the accepted publications, supervised theses and patents that I had produced by the time I defended my PhD. More up-to-date overviews can be found on [Google Scholar](https://scholar.google.com/citations?user=epFVqnIAAAAJ&hl=en&oi=ao), [Semantic Scholar](https://www.semanticscholar.org/author/Daniel-Bogdoll/73381787), or [arXiv](https://arxiv.org/a/bogdoll_d_1.html). \* denotes equal contribution.

## Publications

### Mcity Data Engine: Iterative Model Improvement Through Open-Vocabulary Data Selection
03/2026 • Daniel Bogdoll, Rajanikant Patnaik Ananta, Abeyankar Giridharan, Isabel Moore, Gregory Stevens, Henry X. Liu

<img width="100%" src="https://github.com/user-attachments/assets/13623a1f-bf87-40c6-b43b-bf66b1afb799">

[arXiv](https://arxiv.org/abs/2504.21614) | [Proceeding](https://ieeexplore.ieee.org/document/11423797) | [Code](https://github.com/mcity/mcity_data_engine)

:white_check_mark: Accepted at [International Conference on Intelligent Transportation Systems (ITSC)](https://ieee-itsc.org/2025/)

<details>
  <summary markdown="span">BibTeX Citation</summary>
  
  ```
  @InProceedings{Bogdoll_Mcity_2026_ITSC,
    author={Bogdoll, Daniel and Patnaik Ananta, Rajanikant and Giridharan, Abeyankar and Moore, Isabel and Stevens, Gregory and Liu, Henry X.},
    title     = {{Mcity Data Engine: Iterative Model Improvement Through Open-Vocabulary Data Selection}}, 
    booktitle = {International Conference on Intelligent Transportation Systems (ITSC)},
    year      = {2026}
  }
  ```
</details>

<details>
  <summary>
    :red_circle: Single-Blind
    :green_circle: High Quality Reviews
</summary>

### Reviewer 1

Summary:
This paper proposes a comprehensive workflow for
intelligent transportation systems, including data
acquisition, annotation, model training, and deployment.
Strengths:
1. The proposed Mcity Data Engine is the first open-source
data engine, which could support subsequent research in the
field.
2. The author uses the open-vocabulary detection models to
assist with data annotation.
Questions:
1. The core innovations are limited. While I understand the
substantial amount of work the author has done, it
resembles more of an engineering implementation.
2. All the work is conducted in the 2D image domain, which
limits its scope of application. There is a lack of depth
information or 3D annotations, limiting its use to video
surveillance and preventing its application in fields like
autonomous driving.
3. There is no explanation on how to address the long-tail
problem, yet the abstract mentions that it "focuses on rare
and novel classes". Although the open-vocabulary model can
detect arbitrary categories, the author does not provide a
detailed explanation on how it is used to address the
long-tail effect. Moreover, occupancy prediction can
effectively address the long-tail problem in 3D space. The
significance of the rare classes in 2D space, as discussed
by the author, is questionable.
4. There is no definition of the similarity score in the
class alignment process. In addition, considering the need
for high-quality annotations, the significance of such
label mapping is questionable.
5. I can see that many similar works, like X-AnyLabeling,
use open-vocabulary models to assist with annotation, and
the author does not emphasize the distinction of this work.
While the complete workflow is certainly an advantage, the
core module still lies in the data annotation.
6. The dataset is relatively small, containing only 1,260
instances. There is no specific description of the scene
setup, such as the height of the roadside camera, image
resolution, etc.
7. The detection performance of the open-vocabulary model
is limited, as shown in Table 2, and the inference time is
relatively long. For example, Grounding DINO 1.6 Pro
exhibits strong detection performance, while the
performance of Grounding DINO 1.0 is not as strong.

### Reviewer 2

The paper introduces the Mcity Data Engine (MDE) to address
a key challenge in Intelligent Transportation Systems
(ITS): selecting and labeling useful data from massive,
unlabeled datasets. This is especially difficult for
identifying rare or novel events (long-tail classes),
essential for safety and reliability in real-world
scenarios.
The authors note that while companies like Nvidia and Tesla
have proprietary data engines, researchers have no
comparable open-source solution. MDE fills this gap by
offering a complete, modular framework—from data collection
to model deployment—designed to support open-vocabulary
selection for rare events.
Table I (Page 2) shows that MDE is the only open-source
tool covering all development stages: acquisition, storage,
selection, labeling, training, validation, and deployment.
This makes it especially useful for tasks like detecting
rare road users (e.g., pedestrians, cyclists) in autonomous
driving.
The MDE is open-sourced under the MIT license on GitHub,
promoting transparency and collaboration. However, the
paper’s claim that MDE is the “first” holistic open-source
engine is debatable. Other tools like VLM-C4L also cover
several stages, and the paper doesn’t fully explain why MDE
is superior.
While the paper highlights the importance of long-tail
data, it doesn’t provide data on how frequent or impactful
these rare events are. It also briefly mentions other
techniques like active learning but doesn’t explain why
they fall short.
MDE’s modular design (Fig. 1) makes it adaptable across
applications. Its use of an ensemble of open-vocabulary
models (Fig. 2) allows flexible querying without fixed
class sets—helpful for identifying rare classes. The system
uses model consensus and instance-based selection to reduce
noise and labeling effort. It can process up to 1.3 million
samples per day using 8 Nvidia H100 GPUs.
However, the criteria for selecting the 12 models in the
ensemble aren’t clearly explained, and the semantic
disagreement between models (e.g., "person" vs.
"pedestrian") could lead to missed detections. Only 100
frames were evaluated, despite the system’s high processing
capacity, raising concerns about scalability and
generalization.
Although the framework supports 22 model architectures,
only one (YOLOv11_N) is trained and tested. Testing more
models would better demonstrate MDE’s flexibility. Also,
the paper doesn’t compare MDE’s performance against other
methods like CLIP-based or VLM-based selection, making it
difficult to assess its true effectiveness.
In the end, while MDE is a useful and comprehensive tool
built on existing models and ideas, its innovations are
incremental rather than groundbreaking.

The authors should expand further on the following;
1. Clarify Novelty: Explicitly compare MDE with VLM-C4L and
other academic data engines, justifying why MDE is uniquely
holistic or superior.
2. Expand Evaluation: Include experiments with additional
models (e.g., Co-DETR), datasets (e.g., non-fisheye data),
and multiple iterations to demonstrate scalability and
generalizability.
3. Add Baselines: Compare MDE’s data selection against
random sampling, active learning, or other VLM-based
methods (e.g., [18], [19]).
4. Improve Transparency: Detail the ensemble selection
criteria and consensus filter’s handling of semantic
disagreements.
5. Address Accessibility: Discuss lighter computational
alternatives or configurations for resource-constrained
settings.
6. Evaluate Auto-Labeling: Quantify the impact of
auto-labeling errors and describe human review processes to
ensure quality.
7. Clarify Crowd Data: Either justify the inclusion of
\(\mathcal{D}_{\text{iter}}^{\text{crowd}}\) with
crowd-specific metrics or remove it to focus on non-crowd
VRUs.
8. Add Statistical Tests: Include statistical significance
tests (e.g., t-tests, confidence intervals) for the results
in Table III.
9. Strengthen Conclusion: Discuss practical challenges,
broader impact, and potential extensions to non-vision
data.

### Reviewer 3

This paper introduces the Mcity Data Engine (MDE), an
open-source framework designed to address the challenge of
iterative model improvement, particularly for detecting
rare and novel (long-tail) classes within large volumes of
unlabeled data, with a focus on Intelligent Transportation
Systems. The authors highlight the gap between proprietary
industrial data engines and often incomplete or unavailable
academic solutions. The MDE provides a comprehensive suite
of modules covering the entire data-centric development
lifecycle: data acquisition, storage, selection, labeling,
training, validation, and deployment. A core technical
contribution is its open-vocabulary data selection module,
which utilizes an ensemble of state-of-the-art
open-vocabulary object detection models to query data based
on natural language class descriptions.the MDE employs a
consensus-based filtering stage to reduce false
positives/negatives. The paper details the architecture and
functionalities of each MDE module, emphasizing its
domain-agnostic nature and integration with tools like CVAT
for labeling and Voxel51 for dataset representation. The
utility of the MDE is demonstrated through a real-world
case study on improving Vulnerable Road User (VRU)
detection using unlabeled fisheye camera data from the
Smart Intersections Project.
1. While the ensemble of OWL-ViT/OWLv2/Grounding-DINO
models improves rare-class selection, the authors admit
current open-vocabulary models exhibit "suboptimal
prediction quality" (Sec. III-B). The consensus-based
filtering (e.g., 3/5 majority) mitigates noise but lacks
stress testing under cross-domain shifts (e.g., weather
variations or unseen sensor types).
2.Evaluation solely focuses on VRU detection in fisheye
data from one project (Smart Intersections). No tests on:
a)Truly novel classes beyond {pedestrian, cyclist} (e.g.,
animals or construction objects).
b)Multi-modal data (LiDAR/radar) despite MDE claiming
"domain-agnostic" support (Sec. III-A).
c)Cross-dataset benchmarks (e.g., Waymo or nuScenes) to
validate scalability.

### Reviewer 4

The authors created Mcity Data Engine which poses itself to
be the open-source solution to the communities lack of
openly available data engines. While there are several
proprietary data-engines which offer a complete end-to-end
pipeline from data acquisition to model deployment, these
solutions are not open sourced which make it difficult to
customize for a variety of different datasets. Meanwhile,
academic solutions consider isolated aspect of data
engines, drastically reducing their utility. The authors
then proposed Mcity data engine to combine the best aspects
of both existing solutions. Allowing work to be done from
data acquisition to model deployment while being
open-sourced. 

Strengths:

1. They claim to be the first open-source data engine for
holistic data-based development cycles. Their solution is
domain-agnostic, offer a host of open-vocabulary object
detection models, and follow unified dataset format. This
makes it easier for other researchers to use their solution
out-of-the-box.
2. MDE includes a variety of model architectures for object
detection and open vocabulary models which make it easy to
validate and benchmark.
3. They have released v1.1 of their solution on github,
with adequate documentation, proving that their claims at
least can be substantiated by other researchers. It has
substantial wiki entries (which is out of the scope of this
review).
4. There are plenty of references which demonstrate the
knowledge of the authors in this domain. 
5. Clear comparison of existing state-of-the-art data
engines in Table 1.

Weaknesses:
1. The technical novelty of their approach is not that
strong due to the fact that MDE is less of technical
solution and more of a pipeline that combines the
approaches of different existing solutions. Did the authors
propose or define a novel solution within the modules of
MDE?
2. The authors did not highlight how other external models
can be injected into their framework (or was this the
compatiblity mentioned in the last paragraph of Section
III.D?) which would allow other researchers, using MDE to
easily benchmark their models alongside other
state-of-the-art approaches. This will make their solution
much more usable outside their own research.
3. They did not include a discussion on how model
deployment is handled by MDE (aside from uploading the
weights and deploying it on the edge).
4. Figure 4 is not very clear to me. What is the key
takeaway from this figure? Is it just meant to show that
additional VRU instances make the data embeddings richer?

Overall it is a well written paper with a very mature and
complete looking data engine. The main concern is the lack
of technological novelty, but I think the availability of
their code with documentation makes up for it. This is very
relevant to the field of intelligent transport systems.

### Associate Editor

The authors introduce the MCity Data Engine (MDE), which is
an open-source solution providing modules for the complete
data-based development cycle. The MDE provides a
comprehensive suite of modules covering the entire
data-centric development lifecycle: data acquisition,
storage, selection, labeling, training, validation, and
deployment. 
There are some comments that authors should consider. Major
concerns are especially related to:
1) Clarity of the novelties
2) All the work is conducted in the 2D image domain, which
limits its scope of application. There is a lack of depth
information or 3D annotations, limiting its use to video
surveillance and preventing its application in fields like
autonomous driving.
3) no explanation on how to address the long-tail problem

</details>

&nbsp;
&nbsp;


### MUVO: A Multimodal Generative World Model for Autonomous Driving with Geometric Representations
08/2025 • Daniel Bogdoll*, Yitian Yang*, Tim Joseph, Melih Yazgan, J. Marius Zöllner

<img width="100%" src="https://github.com/user-attachments/assets/ffd79b7b-7d6e-449d-bb69-8d754792198a">

[arXiv](https://arxiv.org/abs/2311.11762) | [Proceeding](https://ieeexplore.ieee.org/document/11097718) | [Code](https://github.com/fzi-forschungszentrum-informatik/muvo)

:white_check_mark: Accepted at [IEEE Intelligent Vehicles Symposium (IV)](https://ieee-iv.org/2025/)

<details>
  <summary markdown="span">BibTeX Citation</summary>
  
  ```
  @InProceedings{Bogdoll_MUVO_2025_IV,
    author={Bogdoll, Daniel and Yang, Yitian and Joseph, Tim and Yazgan, Melih and Zollner, J. Marius},
    title     = {{MUVO: A Multimodal Generative World Model for Autonomous Driving with Geometric Representations}}, 
    booktitle = {IEEE Intelligent Vehicles Symposium (IV)},
    year      = {2025}
  }
  ```
</details>

<details>
  <summary>
    :red_circle: Single-Blind
    :orange_circle: Medium Quality Reviews
</summary>

### Associate Editor

The paper proposes a sensor fusion strategy for predictive
world models using transformer-based fusion and 3D
occupancy prediction. Strengths include a good experimental
setup, useful comparisons across fusion strategies, and
relevance of the topic.
Yet, the paper needs improvement in regard to clarity of
the presentation and a more comprehensive real-world
evaluation. The authors should carefully take the
reviewers' questions and comments into account.

### Reviewer 1

Strengths:
The authors provide an evaluation protocol and a problem
that is important for practical application and also for
the current research from interest.
The authors motivate the research idea and explain their
experiment steps clearly. They give a detailed description
about the dataset creation. Furthermore, they introduce the
results shortly but clearly and do a wide range of
experiments with different components. 

Weakness: 
 Didactic rewriting is necessary to rate the paper. In
detail: 
 The didactic guiding through paper should be improved by: 
 - clearly stating the contributions in the introduction.
 - distinguish between new methods aspects and evaluation
settings.
 - putting the paper in context in the related work section
rather then listing models and approaches without relation
or grouping.
 - minimize variables & description of method to those
actually needed for evaluation purpose.
The overall writing quality needs to be improved, like
L^pred is not introduces, reference and wording style
inconsistency e.g. multimodal or multi-modal, plot
description... 
 
 To increase the benefits for research community providing
code would be helpful. 

Questions: 
What are the advantages of using an RL agent for recording
actions instead of the autopilot provided by CARLA, that
can also returns the action?

### Reviewer 2

This paper presents a well-structured study on sensor
fusion strategies for generative predictive world models,
offering valuable insights into the advantages of
transformer-based fusion over traditional BEV-based
approaches. The experimental design is thorough, comparing
multiple fusion strategies and evaluating the impact of 3D
occupancy prediction.

However, there are some limitations that should be
addressed. (1) The experiments are conducted solely in a
simulated environment (CARLA) without validation on
real-world datasets. Even if real-world experiments are not
feasible, a discussion on potential challenges and expected
performance differences in real-world applications would be
beneficial. (2) Computational cost is not analyzed, despite
the use of transformer-based fusion, which can be
resource-intensive. Reporting FLOPs and inference time for
different fusion strategies would improve clarity on
practical feasibility. (3) The contribution of 3D occupancy
prediction appears limited, showing minimal impact on
sensor data prediction performance. Further optimization of
its integration could strengthen the argument for its
inclusion.

To improve the paper, the following additions are
recommended: (1) A discussion on how the proposed method
might generalize to real-world scenarios, along with
potential challenges. (2) A computational efficiency
analysis, including FLOPs and inference time comparisons.
(3) A more detailed discussion in the conclusion on the
method's limitations and possible extensions to more
complex multi-sensor setups.

</details>

:x: Previous version rejected at [IEEE Robotics and Automation Letters (RA-L)](https://www.ieee-ras.org/publications/ra-l)

<details>
  <summary>
    :orange_circle: Double-Blind
    :green_circle: High Quality Reviews
</summary>

### Reviewer 1

The paper proposed an architecture that focuses on the world’s physical
attributes to make future environment predictions. The architecture
takes RGB images, pointclounds, and acceleration-steer actions to
perform world predictions. 

It is unclear why the entire 3D environment prediction is required to
improve the reasoning ability of an agent. In most of the cases, the
agent will only be interacting with the proximate environment.

Figure 3 and Figure 4 lack a description of key takeaways. It would be
great if the authors could point out what is being predicted accurately
and what is not being predicted. 

Additionally, indicating which images represent ground truth and which
are predictions in Figures 3 and 4 would be helpful to the reader.

The authors provide several ablation studies however the takeaways are
not strongly backed by the results. 

The inference time of the architecture would be useful to know if we
want to put this architecture on a real vehicle. 

### Reviewer 2

Summary: The authors propose MUVO, an unsupervised world model for
autonomous driving. This model jointly predicts future camera and LiDAR
sensor observations, together with a 3D occupancy representation
conditioned on the vehicle's future actions. The authors train and
evaluate it with the CARLA simulator on synthetic data.

Related Work: The authors provide a comprehensive section on related
work for world models in autonomous driving and various
representations. I am unaware of highly associated papers that still
need to be addressed. 

Strengths:
- World modelling is important as an unsupervised task. Existing work
on the CARLA simulator relies on labels (or privileged information),
which might not be available in real-world or large-scale settings.
- The prediction of 3D occupancy seems advantageous for downstream
tasks, e.g. planning or simulation. 
- Extensive experiments show the impact of several architectural
choices. 

Weaknesses:
- The camera, LiDAR, and 3D occupancy predictions in Fig. 3 appear to
have low fidelity compared to the state-of-the-art single-sensor
models. That being said, the model jointly predicts multiple modalities
without computationally expensive methods, such as diffusion models. 
- The introduction needs more motivation on possible downstream
applications of the model. Concrete experiments, e.g., using the world
model to pre-train an imitation policy in CARLA, would significantly
strengthen the paper.
- Some technical aspects are not clearly described in the manuscript.
How is the range view LiDAR representation calculated in Sec. III A?
Are the velocity and route mentioned in Sec IV A part of the model
input? What loss component is L^{pcd} in Equation 1?

Style: The paper is well-written and structured, with clear figures and
adequate length. 

Evaluation: Unsupervised world modelling for autonomous driving is an
interesting topic. The proposed method is novel in terms of considering
multiple sensor modalities. The qualitative results have limitations
and experiments are only conducted on synthetic data, but show a great
start for unsupervised representation learning.

### Reviewer 3:

This paper introduced MUVO, a multimodal world model designed to
predict future states for autonomous driving by leveraging spatial
voxel representations from high-resolution camera and lidar data. The
experiments demonstrated that MUVO effectively improves prediction
quality for both sensor modalities and advances the state of the art in
action-conditioned 3D occupancy forecasting. However, the model's
overfitting to simulated environments and limited real-world validation
highlight areas that require further research investment.
1) In Section I, Introduction, some parts should be rewritten to better
emphasize the main motivations and contributions. The abstract should
also include the overall method in a clearer presentation.
2)  In Section II, Related Works, the related works section is very
limited and should typically include more types of studies, such as an
overview of existing solutions in BEV methods, supervised methods for
autonomous driving, domain adaptation in deep learning, as well as the
limitation for the recent works.
3) In Sections III. Please add more symbol explanations under the
framework figure. Authors mentioned that the previous works are based
on low-resolution inputs. What’s the resolution for the previous work?
How much accuracy is affected by the low-resolution? Except for fusing
the point cloud and the RGB image, why could the action features help
for the prediction?
4) From Equation 1, the loss function is simply adding all the features
in different weights, what are the hyper-parameters for each part? In
Figure 6, the “Pre-Trained-O” achieved the highest IoU and recall, why
the precision is lower than other methods? 
5) In Section V, The model's validation and testing appear to be
limited to simulated environments (CARLA), with no mention of testing
on real-world datasets. Is it possible to test the current model in any
real world dataset? .
6)  In Section V, the training data is collected under a limited set of
conditions (e.g., specific towns and weather conditions in CARLA). This
may lead to a lack of robustness in the model when exposed to
environments. Is it possible to simulate more different environments to
improve the robustness?  
7)  The novel contribution is using action as the multimodal input.
Could you please add an ablation study for investigating how much
influence for using the action features? 
  The method is a good solution to address the computational complexity
problem. However, the settings of experiments might have some weak
points. Authors should present more ablation studies of experiments and
address issues.

### Editor

Dear Mr. Daniel Bogdoll,

Your paper submitted to the IEEE Robotics and Automation Letters (RA-L) has been
reviewed by the Associate Editor and selected Reviewers. The reviews of
the paper are attached.

On the basis of the reviewers' ratings and comments, I regret to inform
you that your paper is not suitable for publication in RA-L.

We thank you for your interest in the IEEE Robotics and Automation
Letters, and hope that you will consider publishing future papers here.

Sincerely, Editor (Autonomy for Mobility and Manipulation)
IEEE Robotics and Automation Letters
 
Report	
The authors present MUVO, an unsupervised world model that predicts
future camera and LiDAR sensor observations and a 3D occupancy
representation conditioned on the vehicle's future actions.

The paper is well-written and adequately situates itself with respect
to the existing works in the field. The work itself is novel due to its
consideration of multimodal inputs. It is of relevance to the real
world, given its unsupervised nature. The reviewers appreciated the
extensive ablation experiments but also raised sincere concerns as
follows:

1. Additional motivation regarding the usability of the model would be
helpful (R3, R4, R5) in the introduction section and through
experimental evaluation. R4 provides a specific suggestion (using the
world model to pre-train an imitation policy in the simulator).

2. The model predictions appear to be low-fidelity as compared to the
state-of-the-art single-sensor models. Addressing this observation in
light of the multimodal nature and/or computational expense would be
helpful (R4,R5). 

3. The ablation experiments show the impact of architectural choices.
However, key takeaways regarding the model's overall performance are
not clearly highlighted (R3). 

4. Ablation studies highlighting the benefit of using actions as input
would be helpful (R5).

5. In relation with concern #2, #3, and #4, the key differentiators of
this work are its multimodal nature and the world-modeling based
approach. However, all the reported experiments are ablation-style
experiments that justify the design choices but do not highlight the
benefits of MUVO as compared to other world models. It is crucial to
provide experimental evaluations and/or discussion (preferably both)
that highlight these key differentiators of MUVO through comparison
with a single-sensor approach and a pattern recognition-based approach
(i.e., approaches that the authors claim learn patterns in the data
rather than modeling the real world). This will help the authors
demonstrate the superiority of their approach. 

6. The entire approach is trained and tested in simulation. While such
training and testing are useful, including qualitative results on
real-world data (certainly using one of the existing real-world
datasets
mentioned in Section II) needs to strengthen the paper (R5).
Furthermore,
it will also be necessary to make a case for the applicability of the
work to the real world (R3) with robotics experiments. 

7. Several technical aspects and hyperparameters are not clearly
described in the manuscript (R4, R5).

Minor suggestions:

1. Labeling and captioning of Figures 3 and 4 can be altered to improve
clarity (R3,R5)
2. Some typos need to be fixed (e.g., the first sentence in Section
VA-1)
3. It may be helpful to provide a couple of sentences in the abstract
summarizing the proposed approach (R5).
4. It might be useful to add a couple of sentences situating MUVO with
respect to existing BEV-based and supervised approaches (R5).

</details>

&nbsp;
&nbsp;

### Label-Free Model Failure Detection for Lidar-based Point Cloud Segmentation
09/2025 • Daniel Bogdoll*, Finn Sartoris*, Vincent Geppert*, Svetlana Pavlitska, J. Marius Zöllner

<img width="100%" src="https://github.com/user-attachments/assets/2df14ada-2429-43b5-9e76-0964a2a6504f">

[arXiv](https://arxiv.org/abs/2407.14306) | [Proceeding](https://ieeexplore.ieee.org/document/11163519) | [Code](https://github.com/daniel-bogdoll/model_contradictions)

:white_check_mark: Accepted at [IEEE Intelligent Vehicles Symposium (IV)](https://ieee-iv.org/2025/)

<details>
  <summary markdown="span">BibTeX Citation</summary>
  
  ```
  @InProceedings{Bogdoll_Labelfree_2025_IV,
    author={Bogdoll, Daniel and Sartoris, Finn and Geppert, Vincent and Pavlitska, Svetlana and Zöllner, J. Marius},
    title     = {{Label-Free Model Failure Detection for Lidar-based Point Cloud Segmentation}}, 
    booktitle = {IEEE Intelligent Vehicles Symposium (IV)},
    year      = {2025}
  }
  ```
</details>

<details>
  <summary>
    :red_circle: Single-Blind
    :green_circle: High Quality Reviews
</summary>

### Associate Editor

This work performed a large-scale qualitative analysis and
presented LidarCODA, the first public dataset with labeled
anomalies in real-world lidar data. The paper is well
written and presents a valid failure detection method. The
reviewers raised concerns regarding the presentation, the
analyses and explanations, the comparison to other
approaches, and the adaptations to sensor domain shifts in
real-world applications. These concerns should be addressed
in the final version.

### Reviewer 1

Summary of the review :
 
The idea for the first contribution is promising and the
dataset proposed in the second contribution looks
interesting, however, several critical problems appear. The
evaluation method proposed as first contribution is poorly
framed (it is difficult even to understand what is
evaluated and how it could be re-used for another method),
and the task for which models are supposedly evaluated is
not the one described in the title, abstract and
introduction (moving object segmentation and not claimed
“lidar-based point cloud segmentation”). The validation of
the evaluation method relies on a qualitative approach and
a quantitative approach. The qualitative approach seems too
ambitious and provides weak conclusions. The quantitative
approach is based on their own provided anomalies dataset.
Although the dataset looks interesting (but its description
is very brief in this paper), sadly, there is no attempt to
compare their method to other methods on this new dataset
(or other data). Overall, this evaluation seems
insufficient.
 
Summary of the paper :
 
The paper addresses the issue of failure detection for
moving object segmentation models. For this, the paper
proposes 2 contributions : 
- A “Label-free evaluation for lidar-based point cloud
segmentation based on complementary learning with a super-
vised and a self-supervised model”
- A publicly available dataset named “LidarCODA” for
“real-world anomaly dataset with labeled lidar data, to
quantitatively evaluate the sensitivity of the approach to
outliers”
 
It starts with an introduction and related works detailing
other approaches to detect failure modes in models. The
method’s section then presents a pipeline for comparing two
specific moving object segmentation methods that they
detail. Both methods are seemingly proposed by the authors
(although built by parts from other works). 
 
The evaluation section consists of a qualitative evaluation
where the authors “manually analyse 20,000 frames” from the
KITTI dataset, then a quantitative evaluation with no
comparison to other methods on their own proposed dataset.
 
Full review :
 
1st contribution :
Content : 
The first contribution is an evaluation method for MOVING
OBJECT SEGMENTATION (and not "point cloud segmentation”).
In the paper, they propose to compare a given supervised
moving object segmentation method to another
self-supervised moving object segmentation method.
Observing the cases where both methods disagree allows to
identify failure modes.
 
Innovation : 
The idea does seem innovative in that usual such failure
modes detectors have relied on finding discrepancies
between predictions from methods using different sensor
systems or ensemble learning, and not different approaches
to the same task like they do here (supervised pipeline VS
different unsupervised pipeline).
 
Relevancy: 
(Wrong angle) : The core idea is interesting, but the angle
is wrong in my opinion. The method is presented as an
evaluation method, but the authors don’t explicitly explain
what is the object of the evaluation ! What is evaluated ?
Is it the supervised moving object segmentation pipeline ?
or just parts of it, e.g. the semantic segmentation model ?
For an evaluation tool, there is little detail about how to
use it to evaluate any other method than the one introduced
in the paper (the reader is left to guess that you could
substitute their supervised method with yours). As an
evaluation tool, then, the focus should be placed on the
unsupervised method used to compare with, (e.g. why do you
choose this specific unsupervised method to compare with ?
Have you tried other methods ? Why not more methods ?) the
analysis of the discrepancies (which is only quickly
covered in III.C, where the instance clustering part is
barely explained). To illustrate my point : Visualize Fig.
2, giving an overview of the evaluation pipeline. Can you
understand, without reading the paper, what “model” is
evaluated by this evaluation method ? Even after reading,
I’m not sure.
 
(Wrong explanation) There are various critical presentation
mistakes. The first one is in the first contribution, where
the authors claim to propose an evaluation method for
“lidar-based point cloud segmentation”. The method proposed
is entirely focused on motion segmentation (also called
“moving object segmentation” from a quick research). “lidar
point cloud segmentation” is poorly defined in my opinion
as it may refer to semantic, instance, panoptic or other
types of segmentations, and in this case, there is no
explanation given for how the evaluation method would apply
to any other case than moving object segmentation. 
 
(Wrong explanation) Secondly, The authors introduce a new
concept named “complementary training”. The problem is that
this new concept is practically never explained. The only
other mention of “complementary” is in the introduction of
III. where they explain that they perform “complementary
training for the same task in order to detect model
failures”. This seems  insufficient to explain a new
proposed concept.
 
(Qualitative Validation and Lack of Comparison) The first
qualitative evaluation has significant limitations that the
authors do not adequately emphasize. They claim to have
"manually analyzed their method on over 20,000 frames" from
KITTI's test sequences. Their approach involves projecting
colored point clouds onto RGB images, with colors
indicating failure detections. If my understanding is
correct, this would require reviewing each of the 20,000 3D
LiDAR scans, which can only be properly inspected by
examining multiple camera images from KITTI for each
scan—potentially amounting to approximately 100,000 images.
For each image, reviewing the method's output would mean
examining individual points and verifying their
classification accuracy. With ground truth unavailable for
this data, the authors would need to manually determine
which objects are moving and which are stationary in each
scene! This task seems infeasible for such a large dataset,
even with substantial resources. Furthermore, the nature of
this "analysis" is poorly explained, as the only apparent
result from this evaluation consists of comments on a few
selected cases. That kind of evaluation would also largely
ignore the problem of False Positives where both methods
agreed but were both wrong.
There is nothing wrong with qualitatively evaluating some
output to provide intuition on the result, but this does
not constitute a strong evaluation.
The next quantitative evaluation is more interesting,
however it is unfortunate that the failure mode detection
method is not compared to any other existing methods, like
the ones mentioned in the introduction that rely on
ensemble learning or other types of discrepancy analysis.
There is no way to place the proposed method compared to
state of the art methods.
(LidarCODA dataset) The proposed dataset seems interesting,
but the section describing it is very short, and a
reference to a prior publication for details is not
receivable if that is one of the main contributions of the
paper.
 
Form :
 
(Related works section) The related works' section is hard
to read, as there are no subsections structuring it.
 
(Method section) The method section in generally hard to
understand, but most importantly it is hard to understand
what the authors propose VS what they re-use. They re-use
and cite many articles, but in the end, what is part of the
evaluation method and what is not is unclear.
 
Quotes of Fig parts like ‘a',’b','c','d', but not appearing
of figures.
 
Few English mistakes e.g. “anomlies” in IV.

### Reviewer 2

The paper presents a model evaluation pipeline for
assessing model errors without requiring annotated data.
Additionally, it introduces a real-world anomaly dataset
derived from an existing dataset.
 
The paper has a well-structured format; however, it can be
difficult to read at times due to the numerous model
representations within the pipeline.
 
I have some questions regarding the evaluation:
 
How do you conduct a qualitative evaluation on 20,000
frames? That is a substantial number of frames for a human
to review. Please clarify the process of this evaluation.
Figure 6 and Tables I and II are not well explained. I
suggest avoiding some of the qualitative results and
instead focusing on them to demonstrate the performance of
your methods through statistical analysis. 

### Reviewer 3

This paper proposes a label-free model failure detection
method for Lidar-based point cloud segmentation in
autonomous driving, demonstrating innovation and improved
robustness. However, several aspects require further
clarification.
 
Major Issues and Suggestions:
1. Figure Annotations
The color scheme in Figure 1 is unclear, which may cause
confusion.
It is suggested to add a brief explanation in the figure
legend or mention where the color scheme is described
(e.g., Section III-C).
2. Failure Case Analysis
The paper presents failure cases but lacks detailed
analysis. Are the model failures of the supervised stream
primarily due to the limitations of the scene flow model or
the clustering method? Or is it a combination of both?
For both self-supervised and supervised models, what are
the higher-level insights into the failure cases? Do these
errors predominantly occur in low-reflectivity objects,
dynamic objects, or specific complex scenarios (e.g., busy
intersections)?
3. Sensor Domain Shift
The poor performance on the nuScenes subset is attributed
to sensor domain shift, but the paper does not analyze:
How do self-supervised and supervised models perform on
this subset?
If deployed in real-world autonomous driving systems, how
would the method adapt to different sensor domain shifts? 

### Reviewer 4

The paper proposed a valid failure detection method. The
technical exposition of the paper is clear, and overall, it
is well-written with commendable innovative value in the
research work.
However, there are a few shortcomings:
1.           The detection performance for the "animal" category
in Table II is notably poor. Why is this the case? Please
provide an analysis and explanation.
2.           Section IV, EVALUATION, lacks comparative results
with other benchmark methods, which diminishes the
persuasiveness of the paper.

### Reviewer 5

Overall, the work is of interest to the research community
and provides with a novel methodology on model failure
detection. The paper is well-organized and mostly clearly
written. However, I have some concerns and suggestions to
authors which may help to further improve the work: 
 
- For Fig.6, I suggest to merge 4 parts of the bar plot
into one, so it is clearer to readers how agreement and
discrepancy are distributed under different scenarios and
it is worth to add a note to distinguish between “regular
scenarios” and “outlier scenarios”.  And it is of interest
to demonstrate the percentage of “Simultaneous Model
Failures" which is more critical to all scenarios.
- The evaluation in Fig.6 and section IV is based on the
point cloud rather than the instance of object. As it is
shown that static objects have larger number of points than
dynamic ones in those datasets, thus, gives more agreement
between unsupervised and self-supervised models, while the
dynamic objects are generally unbalanced in terms of the
number of point clouds, contributing less in agreement
between the two models. Therefore, the evaluation on
instance-level may be more appropriate to show the effect
of agreement and discrepancy of models.
- Although Fig.7 and Fig.8 show some exemplary scenarios
when supervised and self-supervised models disagree, it is
not so clear to me how they are representative in the whole
dataset. Besides, the resource of such disagreement or
agreement but with wrong labeling, is not so obvious to me.
It can be further illustrated or improved with more
detailed analysis of results.
- In Section IV-A, the paragraph states “Scenes 3, 4, and 5
show walking pedestrians or moving cars incorrectly
classified as dynamic.” when analyzing “scenarios where
self-supervised model failures occur”. As these objects
e.g. moving pedestrians are marked as yellow, which means
the supervised model indicates dynamic while the
self-supervised model indicates static (wrong), then the
sentence should change to “incorrectly classified as
static”.
- In Section IV-B, authors mention that “This is reflected
in Fig. 6, where the CODA subsets also show much higher
detection rates compared to the analysis with regular
scenarios”. What does the detection rate refer to? And when
mentioning “moderate correlation between model
disagreements and anomalies present”, it is hard for
readers to believe such correlation without proven evidence
or illustration.
- In Section IV-B, I suggest to add further explanations on
Table I and II especially the numbers are highlighted or
underscored when drawing the conclusion that “our approach
shows different levels of sensitivity given different types
of anomalies“.
- Besides, according to “CODA defines an anomaly as an
object that “blocks or is about to block a potential path
of the self- driving vehicle” [68] and/or “does not belong
to any of the common classes of autonomous driving
benchmarks”, the “anomaly” object, e.g. a truck laying down
on a highway, may not necessarily lead to disagreement
between supervised and self-supervised models. On the other
hand, a novel class, e.g. a trailer, can be difficult for
supervised models, while easy for self-supervised models,
may contribute towards discrepancy between models. It is of
interest to readers to see such detailed analysis to
demonstrate the effectiveness of the proposed method
- Current experiments limit the combination of specific
choices of supervised and self-supervised models.
Therefore, the scalability of such methodology on model
failure detection as a benchmarking is still questionable.
If more supervised and self-supervised models can be
evaluated and demonstrated, the contribution of the work
will be further elevated. 

### Reviewer 6

Your paper presents an interesting approach to model
failure detection. The text has a good structure and is
clearly formulated.
However, there are some points that should be corrected or
where I believe you should make some thoughts about. I will
order my comments based on the flow of the paper, so there
is no order between minor or more serious comments.
 
Figure 1 is not referenced. I think in III C you referenced
FIg. 2 instead of 1. The description of the colors should
be in the caption of the figure, not only in the text.
 
From your dataflow in Figure 2 I do not get how there are
points that do not get a label. Do you use further filter?
 
Please explain the usage of the "oracle" already in the
introduction to chapter III. The explanation comes quite
late in the paper and I was a little bit confused at the
beginning.
 
In the text you referer to subfigures 4 a to d. Although
the structure of the figure is divided in to 4 blocks,
there is no a) to d) in the figure.
 
 
The evaluation is in my eyes the weakest part of the
paper. 
As there is no comparison to e.g. using the model trained
with different seeds or other hyperparameters, there is no
prove for the claim, that using different training
paradigms lets the model leverage different data statistics
and that this is better for model failure detection. From
my point of view this ends in the same setup as using
different architectures or losses as already done for
example in medical imaging.
 
In IV A under "Evaluation." you state that "in most cases"
both streams were correctly consistent. Cant you give
percentages here as the human oracle labled the data now?
 
For scene 9 of figure 8: this is known as parallax. Quite a
common problem.
 
Your quantitative analysis is quite confusing considering
the task. I dont understand why we compare the detection
qualitiy here. Given data with labeled annotations I would
like to see actual numbers here of how many frames with
anomalies had discrepancies in the models outputs. Could be
even done on a point basis. "We generally observe a
moderate correlation between model disagreements and
anomalies present in the environment." should be underlined
with  suitable metrics.
 
Would one apply a threshold of how many points are allowed
to deviate locally? There will always be some noise in the
labeling of each point, right? Could outlier filtering help
here? 
 
In V you say that your method "disregards 95 % of the data
as typical, which makes human analysis of the remaining 5 %
feasible even for larger datasets", please use the
quantitative analysis to show how many false positives this
contains.
 
Overall I think you're presenting an interesting approach,
with some drawbacks in your current evaluation. As this is
a workshop paper, I think this is enough to present your
rough idea at the conference.
Until then it would be nice to see a comparison to other
approaches. 

</details>

:x: Previous version rejected at [IEEE Robotics and Automation Letters (RA-L)](https://www.ieee-ras.org/publications/ra-l)

<details>
  <summary>
    :orange_circle: Double-Blind
    :green_circle: High Quality Reviews
</summary>

### Reviewer 1

The article introduces the concept of complementary learning,
leveraging the differences between supervised and self-supervised
paradigms to detect model failures. The proposed method has been
applied to a real-world autonomous driving task, motion segmentation.
Additionally, a new dataset, LidarCODA is provided for future research
in anomaly detection.

I have multiple significant concerns:

1. The LidarCODA dataset is one of the two contributions, but it is not
currently available to the public. The description of how anomalies are
labeled and used for evaluation could be clearer. This lack of open
access and details leads to ambiguity regarding the dataset's
reliability for future work.
2. The claim regarding the first real-world anomaly dataset for
autonomous driving should be weakened, as similar datasets and tasks
have already been proposed in [1, 2].
3. The other contribution focuses on using complementary learning to
detect model failures, but this is applied and demonstrated only to the
motion segmentation (MOS) task. Therefore, I recommend clarifying this
by specifically stating that complementary learning is used for the
LiDAR-based MOS task in this paper to avoid over-claiming.
4. The authors claim that all code is available on GitHub, but no link
to the code is provided in the manuscript.
5. It is not clear about the green points in the top right figure in
Fig. 1. Are the green points representing static points? Why are other
static points in gray?
6. The proposed method compares the results of a supervised model [46]
with a multi-step clustering-based method for detecting model failures.
This idea is quite similar to the work [3], which also uses multi-step
clustering to automatically generate MOS labels to enhance the
performance of the same supervised model [46]. The differences between
[3] and the proposed method should be further discussed in the paper.
7. The final failure detection relies on a human oracle, which
decreases the technical contribution of this paper. A more automated
approach should be proposed to enable autonomous failure classification
and resolution.

[1] Cen, et al.Open-world Semantic Segmentation for LIDAR Point Clouds,
ECCV, 2022
[2] Deng, et al. ElC-OIS: Ellipsoidal Clustering for Open-World
Instance Segmentation on LiDAR Data, IROS, 2023
[3] Chen, et al. Automatic labeling to generate training data for
online LiDAR-based moving object segmentation, RAL, 2023 

### Reviewer 2

	
This article proposes a complementary learning approach to detect model
anomalies by utilizing two streams, supervised learning and
self-supervised learning, to segment point clouds and identify
discrepancies between the two models. The specific implementation
relies on existing methods such as SalsaNext, GndNet, and FlowStep3D,
which limits the overall novelty of this article. However, the concept
of using multiple streams for detecting model failures is innovative.
Additionally, a new dataset, LidarCODA, was proposed, which can be used
for anomaly detection.

1. In Section Ⅳ-A, although the authors provide some image
examples of anomaly detection, there is a lack of accurate evaluation
of the performance of this anomaly detection method. For example, if a
supervised stream is used as the main model and a self-supervised
stream is used to detect model failure, what are the true
positives (TP), false positives (FP), true negatives (TN), and false
negatives (FN)? In addition, corresponding discussions should be
conducted on these metrics.

2. In Section Ⅳ-B, some evaluation metrics, such as mIoU, mP, mR,
and mF1, should be explained in detail, including how they were
obtained.

3. In Section Ⅲ-D, the authors mention, "More details can be
found in [48]." Some important details, such as hyperparameters, should
be provided directly instead of asking readers to search for them in
other literature.

4. In the main text, the authors mentioned Figure 10 first and then
Figure 9. It is suggested that the order of the figures be modified.

5. The expression of figures should be unified in the main text, such
as Figure 7 and Fig. 7.

6. The information in some citations is incomplete. It is suggested to
complete them.

### Reviewer 3

The majority of this paper's content comes from the thesis [1].
Although the content itself is interesting and valuable, the current
manuscript is clearly not complete enough to be published on RA-L.

1. The title of this paper is about "Model Failure Detection", which is
too broad and not precise enough. This paper mainly talks about the
discrepancy between the supervised and self-supervised motion
classification model, which is a specific and narrow task. So the
general expression is not reasonable in the title.

2. From my perspective, the reason to detect the discrepancy between
the supervised and self-supervised motion classification models is to
minimize the error of either model. However, this paper does not
discuss a key problem: how to determine the final result if the
supervised and self-supervised models do not agree with each other? If
there is no such solution, detecting the discrepancy is not useful
since it is straightforward that the two model have the distinct
results. The
paper shows the quantitative results of when the two models have
distinct results, but does not show which model is correct.

3. The introduction of LidarCODA is confusing. This paper mainly
discusses the discrepancy between the supervised and self-supervised
motion classification models, but this part talks a lot about the
domain gap on the semantic segmentation task, which seems to have no
direct relation to the core idea of this paper.

### Reviewer 4

The authors propose a method to detect model errors and a real-world
anomaly LiDAR dataset.
The proposed method consists of using a self-supervised and a
self-supervised network to leverage different data characteristics. The
authors compare point-wise the discrepancy of the two predictions and
cluster them.
For the proposed dataset, the authors take an already existing anomaly
dataset CODA, which provides 2D bounding box annotations and performs
filtering and clustering plus manual inspection to transfer the 2D
labels to 3D point-wise labels.

Contributions:
    * The authors provide experiments on semantic motion segmentation,
analyze model discrepancies, and provide qualitative analysis. 
    * The proposed dataset extends the 2D labels to 3D point-wise
labels.
    * The authors provide good-quality figures to understand the
different steps of the proposed method.


Weaknesses:
    * The paper is not well structured. First, it focuses on how to
detect model errors and later it changes completely the focus to
anomaly detection, which makes it very hard to follow.
    * The contribution of the proposed method is not clear. The authors
used already existing methods and combined them together without any
new insight.
    * The authors claim that usually test splits are typically very
small and not representative, yet they evaluate their method in a
subset (only two sequences) of the SemanticKITTI test set and use the
rest of the test set for qualitative analysis.
    * The authors propose a new method to detect model errors but they
only provide an analysis for a single task. Further experiments would
be required to validate the method.

    * The authors use outdated methods, particularly for motion
segmentation (2021), which does not provide a good comparison of
supervised vs self-supervised methods.
    * In the introduction, the authors give a summary of related work,
which should be contained in that section.

    * The proposed dataset is introduced in the evaluation section
    * In the evaluation section, under "Oracle", they only explain the
qualitative results of the figures and provide some examples of failure
cases for the supervised and self-supervised methods, which is not a
sufficient evaluation process.
    * The evaluation part is not well structured and hard to follow.
    * The motivation behind the experiments in section IV-C is not
clear.
    * The evaluation of the proposed method on the LidarCODA dataset is
not clear. The authors should provide a more detailed explanation about
how they adapted their approach to this task and why is this relevant.

### Editor

Dear Mr. Daniel Bogdoll,

Your paper submitted to the IEEE Robotics and Automation Letters (RA-L) has been
reviewed by the Associate Editor and selected Reviewers. The reviews of
the paper are attached.

On the basis of the reviewers' ratings and comments, I regret to inform
you that your paper is not suitable for publication in RA-L.

We thank you for your interest in the IEEE Robotics and Automation
Letters, and hope that you will consider publishing future papers here.

Sincerely,

Editor (Applications)
IEEE Robotics and Automation Letters
 
Report: This paper proposes a method by learning characteristics from different
training paradigms to detect model errors. As indicated by the review
comments, the contributions of this paper are limited. The general
quality is below RAL. It is suggested that the authors consider the
review comments and submit the paper to other venues.

</details>

&nbsp;
&nbsp;

### AnoVox: A Benchmark for Multimodal Anomaly Detection in Autonomous Driving
05/2025 • Daniel Bogdoll*, Iramm Hamdard*, Lukas Namgyu Rößler*, Felix Geisler, Muhammed Bayram, Felix Wang, Jan Imhof, Miguel de Campos, Anushervon Tabarov, Yitian Yang, Martin Gontscharow, Hanno Gottschalk, J. Marius Zöllner

<img width="100%" src="https://github.com/user-attachments/assets/9e1cb92b-651e-4c0a-b536-0f33fa0343ae">

[arXiv](https://arxiv.org/abs/2405.07865) | [Proceeding](https://link.springer.com/chapter/10.1007/978-3-031-91767-7_15) | [Code](https://github.com/fzi-forschungszentrum-informatik/anovox) | [Dataset](https://zenodo.org/communities/anovox/)

:white_check_mark: Accepted at [ECCV Workshop on Multimodal Perception and Comprehension of Corner Cases in Autonomous Driving (W-CODA)](https://coda-dataset.github.io/w-coda2024/)

<details>
  <summary markdown="span">BibTeX Citation</summary>
  
  ```
  @InProceedings{Bogdoll_Anovox_2025_ECCVW,
    author={Bogdoll, Daniel and Hamdard, Iramm and R\"{o}ßler, Lukas N. and Geisler, Felix and Bayram, Muhammed and Wang, Felix and Imhof, Jan and de Campos, Miguel and Tabarov, Anushervon and Yang, Yitian and Gontscharow, Martin and Gottschalk, Hanno and Z\"{o}llner, J. Marius},
    title     = {{AnoVox: A Benchmark for Multimodal Anomaly Detection in Autonomous Driving}}, 
    booktitle = {European Conference on Computer Vision (ECCV) Workshop},
    year      = {2025}
  }
  ```
</details>

<details>
  <summary>
    :orange_circle: Double-Blind
    :orange_circle: Medium Quality Reviews
</summary>
  
### Reviewer 1

#### Strengths：

First benchmark to integrate content and temporal anomalies for a comprehensive evaluation platform.
Supports various sensor configurations and environmental conditions, allowing anomaly detection under domain shifts.
Offers a formal definition of normality for consistency between training and test data, aiding research in unsupervised learning.

#### Weaknesses：
Dependency on simulation may lead to a Sim2Real gap.
#### Rating:
9: Top 15% of accepted papers, strong accept
#### Confidence:
3: The reviewer is fairly confident that the evaluation is correct

### Reviewer 2

#### Strength:
The first benchmark to provide ground truth in the form of semantic masks for RGB images and lidar point clouds as well as spatial VOXels.
The paper is well-written with a highly readable style and a logical structure.

#### Weakness:
Since the classes of animal or home cannot be fully enumerated, how can content anomalies be determined?
The corner cases in the data are mainly generated by the engine, which may still have a gap with real-world autonomous driving scenarios. Therefore, are they only used as pre-training data for the model in practical applications?

#### Rating:
7: Good paper, accept

#### Confidence:
4: The reviewer is confident but not absolutely certain that the evaluation is correct

### Reviewer 3

#### Summary:
The paper titled "AnoVox: A Benchmark for Multimodal Anomaly Detection in Autonomous Driving" introduces a comprehensive benchmark for anomaly detection in the context of autonomous vehicles. AnoVox is positioned as a significant advancement over existing benchmarks due to its incorporation of multimodal sensor data, including both RGB cameras and LiDAR, and its innovative use of voxelized ground truth. The benchmark is designed to address the limitations of current datasets, particularly the over-reliance on camera data and the lack of temporal anomalies in existing benchmarks.

#### Strengths:
Comprehensive Comparison with Other Datasets: The paper provides an extensive comparison with existing datasets, clearly demonstrating that AnoVox stands out due to its incorporation of more modalities, such as RGB, LiDAR, and depth sensors. This positions AnoVox as a more versatile and robust benchmark.

Larger and More Detailed Dataset: AnoVox is presented as significantly larger than many existing benchmarks, offering a wide range of scenarios that include both content and temporal anomalies. This breadth and depth of data seem to provide a more rigorous test for anomaly detection methods.

Variety of Ground Truth Representations: The benchmark includes multiple forms of ground truth, such as voxelized data and semantic masks, allowing for a more comprehensive evaluation of different anomaly detection methods. This diversity in ground truth representation is a strong point in its favor.

Inclusion of Both Content and Temporal Anomalies: The paper highlights that AnoVox is one of the few benchmarks to include both content and temporal anomalies, which is crucial for testing the robustness of autonomous driving systems under varied and challenging conditions.

#### Weaknesses:
Simulation-Based Dataset: One potential limitation is that AnoVox is entirely based on simulation. While the dataset is extensive and detailed, there may be concerns about how well the results generalize to real-world cases. Simulated environments, despite their advantages, might not fully capture the complexities and unpredictabilities of real-world driving.

#### Rating:
7: Good paper, accept

#### Confidence:
2: The reviewer is willing to defend the evaluation, but it is quite likely that the reviewer did not understand central parts of the paper

### Meta Review

This paper constructs a novel benchmark for Multimodal Anomaly Detection in Autonomous Driving, receiving positive opinions from all reviewers. The Area Chair agrees with the reviewers and decides to accept this paper.

Recommendation: Accept (Poster)

</details>

:x: Previous version rejected at [European Conference on Computer Vision (ECCV)](https://eccv.ecva.net/Conferences/2024)

<details>
  <summary>
    :orange_circle: Double-Blind
    :green_circle: High Quality Reviews
</summary>

### Reviewer #1

#### 1. Summary. In 5-7 sentences, describe the key ideas, experimental or theoretical results, and their significance.
The paper introduces a new dataset and benchmark for anomaly detection in autonomous driving. This contribution originates from the observation that current benchmarks have several limitations, the major one being that they typically include camera-only data. Another limitation of previous benchmarks discussed in the manuscript is the lack of a “normality” definition, that is necessary to define the concept of anomaly. Lastly, existing benchmarks do not consider temporal anomalies, as defined in this paper, e.g., the case of a leading vehicle performing an emergency brake.
Hinging on these notions, the proposed AnoVox benchmark leverages the notorious CARLA simulator to create a new dataset that can overcome the previously mentioned limitations.

The CARLA simulator allows to create scenarios representing normal operation of the system (including the location, weather condition, sensor configuration, other agents). Concerning anomalies, AnoVox enables users to include two types of anomalies: static objects (mostly classes unseen during training, although there is also a fallen class with objects falling to the ground) and temporal anomalies (only one type, that is the case of cars performing an emergency braking).
Using this system, this work builds a large dataset that includes different scenarios, multimodal data (camera, lidar, depth, ego-motion information), and has ground truth annotations. Additionally, the system introduces a spatial voxel representation that allows to compare methods using lidar and/or RGB images (the 2D anomaly scores are lifted to 3D using the ground truth depth data).

The paper lastly showcases an experiment on a small sample of the collected data, using two methods: RbA as representative for camera-based anomaly detection, and REAL as a method that processes a Lidar point-cloud.

Both the code of the system and the data are submitted.

#### 2. Strengths. Consider the significance of key ideas, experimental or theoretical validation, writing quality, data contribution. Explain clearly why these aspects of the paper are valuable. Short bullet lists do NOT suffice.
I think that this work is pointing towards an interesting and frankly needed direction for the community. So far, the problem of anomaly detection for autonomous driving applications has been supported mostly by datasets with camera data only (RGB images), yet an autonomous car would (likely) use other sensors (radars, lidars, ...).
Another aspect that is somewhat raised by the paper, and that I agree with, is the fact that the current benchmarks used in this field have a very narrow representation of anomalies as classes that are not present in the training set. The reality is however more nuanced than that, and an anomaly may be an object from the closed set training data but that has characteristics that do not match the normality of operations (training distribution): for example, a fallen tree or a popped tire or a pedestrian crossing a street not on a cross walk or even a car suddenly braking.

Another problem with current benchmarks is that they are starting to become saturated with methods achieving near perfect scores, and this dataset with its numerous scenarios may offer a more challenging benchmark to evaluate and assess methods.

#### 3. Weaknesses. Consider the significance of key ideas, experimental or theoretical validation, writing quality, data contribution. Clearly explain why these are weak aspects of the paper, e.g., why a specific prior work has already demonstrated the key contributions, or why the experiments are insufficient to validate the claims, etc. Short bullet lists do NOT suffice. Be specific!
Despite the interesting premise of the paper, I find that it has a couple of problems that are difficult to overlook.

- Benchmark and results: the main motivation of the paper is to overcome some limitations of existing benchmarks, and proposes to do so by creating a new, extensive and well curated dataset. However, this dataset is not accompanied by the experimentation that would be expected by a benchmark: the paper only presents an experiment with 2 methods (one using RGB images, the other using point-clouds) and only on a small fraction of the dataset (which makes me question if the large dataset is useful in itself as a contribution).
I do not mean to detract from the usefulness of the dataset, but when presenting new data (and especially when trying to establish a benchmark) the paper should support it with enough experiments to demonstrate its usefulness, to show how it opens up the possibility to investigate new problems and also to establish the proper protocols to use it. For example, you may look at the paper from the SegmentMeIfYouCan Benchmark, or even from the MUAD dataset. This paper, as it is in its current form, unfortunately does nothing of that, even though I agree with the reasoning behind the creation of the dataset.
- AnoVox: the system proposed in this paper, builds heavily on CARLA, just like many other papers have done before it (as correctly pointed out by the authors). Following on the previous point, only proposing a dataset using this open-source simulator, without extensive experimentation that demonstrates its value, is not a contribution that helps pushing forward the field. I understand that producing AnoVox may have required some customization of the simulation, but many others have already done it (e.g. [a]) and I do not think this is enough on its own to justify the publication.
- Definition of normality: the paper also claims the definition of the concept of normality as its own contribution. This is something that I find to be a stretch. Defining the “normality” as the standard operational situation (represented by the training data) is a rather intuitive and straightforward concept, nothing that I would deem innovative. I do understand the point that the authors are making, comparing to previous benchmarks where there is a narrow view on what an anomaly is (an object from a new class unseen at training time), but this sounds almost like taking the shortcoming of these previous benchmarks as a contribution for this paper. Besides, the way this idea of normality is implemented may be debated. For example, one may argue that considering a single scenario with one weather condition and only a single geographical area may be too restrictive to be representative of a normal way of operation. As a matter of fact, for an autonomous car we expect it to recognize anomalies despite these kinds of domain shifts. Similarly, the paper mentions that the behaviour of the ego agent counts towards normality, but this is not really demonstrated.
Again, I understand the perspective of the paper, especially with respect to previous benchmarks, but the definition of normality on its own is not something that I deem a noteworthy contribution. On the contrary, what is a contribution is to expand what is narrowly considered an anomaly in previous benchmarks, not restricting anomalies to an open set problem, but considering things such as fallen objects or abrupt behaviors of other agents (emergency braking).


- In the comments to the authors, I provide some further comments on some specific points.

[a] SELMA: SEmantic Large-Scale Multimodal Acquisitions in Variable Weather, Daytime and Viewpoints

#### 4. Paper rating (pre-rebuttal).
Strong Reject

#### 5. Justification of rating. What are the most important factors in your rating?
As mentioned in the strengths, I think that this paper has merit in trying to push the field of anomaly detection for autonomous driving in interesting directions (multimodal data, allowing the comparison of methods using different modalities, considering a more nuanced notion of anomalies). The potential of this kind of endeavor is significant. Unfortunately, I think that the paper is not ready for publication at this venue in its current form (see weaknesses) and implementing the necessary changes, especially an extended experimental part with the necessary discussion, is something that realistically is not feasible within the limits of a rebuttal.

#### 6. Are there any serious ethical/privacy/transparency/fairness concerns? If yes, please also discuss below in Question 9.
No

#### 7. Limitations and Societal Impact. Have the authors adequately addressed the limitations and potential negative societal impact of their work? Discuss any serious ethical/privacy/transparency/fairness concerns here. Also discuss if there are important limitations that are not apparent from the paper.
The papers addresses the limitations adequately.

#### 8. Is the contribution of a new dataset a main claim for this paper? Have the authors indicated so in the submission form?
Dataset contribution claim in the paper. Indicated in the submission form

#### 9. Additional comments to author(s). Include any comments that may be useful for revision but should not be considered in the paper decision.
- To make this paper impactful, I recommend adding an extended experimental section, which defines the protocols and data split used, and possibly considers many methods from the literature. It would also be important to demonstrate the utilization and importance of all available data modalities, including the ego-motion information.

- Concerning the methods for anomaly detection using RGB information, it is true that it is a common praxis to use OOD data during training to improve results. While I agree that ideally it would be best to not to resort to extra data, I don’t see any good reason why such methods should not be included in the experiments. Moreover, it is typically possible to use these same methods without fine-tuning them with OOD supervision.

- It seems, judging from Fig. 4 and from L.225-226, that the anomalies are always spawning near the middle of the road. If this is true, it is a strong bias that limits the variety of this benchmark. For example, it would be good to have anomalies also on the sidewalk.

- It would help the reader if there were more qualitative examples. For example, it is not clear what are all the objects considered in the fallen category (which was interesting to me)

- I think that the paper points to the right direction in considering not just anomalies that are classes unseen during training. The Fallen class or the temporal anomaly with the vehicle performing an emergency braking are very good additions. A good way to develop this framework further would be to include more of these anomalies (e.g., a car driving in the opposite direction with respect to the traffic, a fallen traffic sign, a motorbike with multiple riders ....)

- Typo at L.264 “CALRA”

- The dataset contains a lot of scenes, yet the experiments use a very small subset of data that is comparable in size to Cityscapes. This makes me wonder “what is the point of the large dataset?”

- Regarding the presented results, the paper states that “To emphasize the definition of normality based on training data alone, we then neglected all methods that require auxiliary data with anomalies during training”. Aside from the fact that I am not exactly convinced from this choice, the chosen RbA method has indeed very good results on the previous benchmarks, but for what I am aware it also uses additional In Distribution data (it is not trained only on Cityscapes, but it also uses data from BDD100k as far as I remember). This also would break the assumption of method trained only on the normality (Cityscapes). So perhaps other methods would perform better in the proposed test. This also reinforces the need for a much more extended and well curated experimental section.

### Reviewer #3

#### 1. Summary. In 5-7 sentences, describe the key ideas, experimental or theoretical results, and their significance.
1. The author proposed the largest synthetic dataset for anomaly detection in autonomous driving, consisting of content and temporal anomalies.
2. The dataset consists of large-scale multimodal sensor data and spatial voxel ground truth.
3. The paper introduced normality that denotes a domain shift between the normal data and the proposed dataset.

#### 2. Strengths. Consider the significance of key ideas, experimental or theoretical validation, writing quality, data contribution. Explain clearly why these aspects of the paper are valuable. Short bullet lists do NOT suffice.
1. The dataset is significantly large compared to the existing anomaly segmentation dataset.
2. It covers a large variety of anomalies along with multi-modal and multi-sensorial data.
3. The authors introduced the concept of normality which is important for anomaly segmentation but was not addressed in prior works.

#### 3. Weaknesses. Consider the significance of key ideas, experimental or theoretical validation, writing quality, data contribution. Clearly explain why these are weak aspects of the paper, e.g., why a specific prior work has already demonstrated the key contributions, or why the experiments are insufficient to validate the claims, etc. Short bullet lists do NOT suffice. Be specific!
1. The paper lacks extensive benchmarking results needed for anomaly segmentation. The authors can borrow the ideas from the prior work: a) Segment Me If You Can, b) Fishyscapes that extensively benchmarked all the existing anomaly segmentation methods.
2. A lack of ablation studies regarding how each modalities could help improve anomaly segmentation.
3. In Table 4, the FPR95 is 100 for all the methods. This could be caused by domain shift since the model training was done on cityscapes and tested on AnoVox. It would be interesting to see if the model was trained and tested on AnoVox.

#### 4. Paper rating (pre-rebuttal).
Weak Reject

#### 5. Justification of rating. What are the most important factors in your rating?
The paper requires extensive benchmarking on the current anomaly segmentation methods. In addition, it needs to show with the addition of each modality how the anomaly segmentation improves.

#### 6. Are there any serious ethical/privacy/transparency/fairness concerns? If yes, please also discuss below in Question 9.
No

#### 7. Is the contribution of a new dataset a main claim for this paper? Have the authors indicated so in the submission form?
Dataset contribution claim in the paper. Indicated in the submission form

### Reviewer #4

#### 1. Summary. In 5-7 sentences, describe the key ideas, experimental or theoretical results, and their significance.
The paper introduces AnoVox, the largest and first benchmark for anomaly detection in autonomous vehicles, incorporating extensive multimodal sensor data and spatial voxel ground truth. AnoVox aims to overcome existing benchmarks' limitations, such as a lack of a clear normality definition and an overreliance on RGB data, by providing comprehensive semantic masks for various sensors. The benchmark not only formalizes normality but also compares how current models perform, highlighting the importance of learning normality from training data to improve anomaly detection.

#### 2. Strengths. Consider the significance of key ideas, experimental or theoretical validation, writing quality, data contribution. Explain clearly why these aspects of the paper are valuable. Short bullet lists do NOT suffice.
-The paper effectively compares existing datasets to the proposed dataset, highlighting that while existing works mainly use camera-based semantic masks, the proposed dataset offers 3D voxel ground truth.

-The paper defined the nomality well: Ego, Domain, pysical entities.

-It is notably beneficial and practical that scenario description files are shareable and can be used to generate data

-The proposed dataset introduces a more challenging environment for anomaly detection. Anomalies are identified not by their exclusion from Cityscapes classes but by their absence in the training set. Moreover, there is no domain shift for the anomaly classes since they are rendered using the same engine as training data.

#### 3. Weaknesses. Consider the significance of key ideas, experimental or theoretical validation, writing quality, data contribution. Clearly explain why these are weak aspects of the paper, e.g., why a specific prior work has already demonstrated the key contributions, or why the experiments are insufficient to validate the claims, etc. Short bullet lists do NOT suffice. Be specific!
-The paper briefly discusses the performance of the REAL and RbA methods on the proposed dataset in Table 4. However, the significance of the differences in performance between columns is unclear. It would be helpful if the paper provided more explanation on how to interpret these results, especially for those unfamiliar with Anomaly Detection.

-It would be beneficial to demonstrate the models' performance across different scenarios, specifically separating evaluations into 1) only content anomaly 2) only temporal anomaly 3) both types of anomalies. Additionally, for evluations focusing solely on content anomalies, analyzing performance across six super classes would provide a more comprehensive understanding of the dataset and models.

-Temporal anomaly lacks the diversity.

#### 4. Paper rating (pre-rebuttal).
Borderline

#### 5. Justification of rating. What are the most important factors in your rating?
The paper proposes useful dataset but it lacks diversity and analysis mentioned in the weakness

#### 6. Are there any serious ethical/privacy/transparency/fairness concerns? If yes, please also discuss below in Question 9.
No

#### 7. Is the contribution of a new dataset a main claim for this paper? Have the authors indicated so in the submission form?
Dataset contribution claim in the paper. Indicated in the submission form

</details>

&nbsp;
&nbsp;

### Hybrid Video Anomaly Detection for Anomalous Scenarios in Autonomous Driving
12/2024 • Daniel Bogdoll*, Jan Imhof*, Tim Joseph, Svetlana Pavlitska, J. Marius Zöllner

<img width="100%" src="https://github.com/user-attachments/assets/aa683894-0abd-4340-9d02-3bbac988a147">

[Proceeding](https://bmva-archive.org.uk/bmvc/2024/workshops/RROW/04_Hybrid_Video_Anomaly_Detecti.pdf) | [arXiv](https://arxiv.org/abs/2406.06423)

:white_check_mark: Accepted at [BMVC Workshop on Robust Recognition in the Open World](https://rrow2024.github.io/)

<details>
  <summary markdown="span">BibTeX Citation</summary>
  
  ```
  @InProceedings{Bogdoll_Hybrid_2024_BMVC,
    author={Bogdoll, Daniel and Imhof, Jan and Joseph, Tim and Pavlitska, Svetlana and Zöllner, J. Marius},
    title     = {{Hybrid Video Anomaly Detection for Anomalous Scenarios in Autonomous Driving}}, 
    booktitle = {British Machine Vision Conference (BMVC) Workshop},
    year      = {2024}
  }
  ```
</details>

<details>
  <summary>
    :orange_circle: Double-Blind
    :orange_circle: Medium Quality Reviews
</summary>
  
### Reviewer 1

Nice framework for anomaly detection using temporal information

#### Review
This paper adapts the anomaly detection framework 
 to autonomous driving and proposes a pixel-wise evaluation to localize anomalies. The innovation lies in modifying the framework to handle the complexities of high-resolution real-world driving scenes. The paper is well-written and easy to follow. Given the increasing importance of reliable anomaly detection in autonomous driving systems, the work is also significant. Additionally, I find the idea of using temporal anomalies innovative.

Weaknesses:

In the introduction, five techniques for anomaly detection are mentioned; however, only two are elaborated on. It would be beneficial to elaborate on the others as well and draw a clear line where this work differentiates from the others. I see later in the related work that HF2-VAD is a combination of reconstruction and prediction. Maybe it would be beneficial to expand on this in the introduction as well.

I find Figure 1 to be somewhat confusing, given its positioning in the paper. The right frame should show the anomaly score for all instances of the class vehicle, but it seems the anomaly mask has been cut out in a perfect square. In the first reference of the paper, the paper states: " we adapt HF2-VAD to autonomous driving by generating dense, pixel-wise anomaly scores for the whole frame rather than focusing on the content of unlocalized, detected bounding boxes alone, as can be seen in Figure 1. " at first I found this very confusing, but only after reading along the paper do I understand that the image I see on the right this is due to the bounding boxes from the object detector (this information is only given in page 5). I think this information should somehow be summarized in the caption such that the reader gets a complete understanding from the caption alone. Additionally, the ordering of the figures and tables should be adjusted so that the reader does not need to scroll through multiple pages to find the referenced figure.

The paper mentions a limitation when turning vehicles are detected as anomalies. It would be useful to elaborate on why this happens. Is the model overfitting to straight-moving vehicles?

For future work, it would also be interesting to see how well this method generalizes to real-world data; since strong breaking maneuvers are taken as anomalous scenarios, this method can be applied to a real-world dataset and analyzed when it triggers an anomaly.

#### Rating
6: Marginally above acceptance threshold

#### Confidence
4: The reviewer is confident but not absolutely certain that the evaluation is correct

### Reviewer 2

Review of Hybrid Video Anomaly Detection for Autonomous Driving

#### Review
Overview:
The presented paper proposes a method for detecting anomalous driving patterns in road traffic scenarios based on camera data recorded from an ego vehicle. An adaptation of the HF2-VAD model is proposed in order to obtain pixel-wise anomaly scores which are aggregated over bounding box predictions per frame. Scenario evaluation is carried out on the AnoVox benchmark.

Strengths:
Detecting anomalous traffic patterns is an important and relevant objective for automated driving and the presented work addresses this problem successfully
The proposed adaptation of the HF2-VAD method seems sound conceptually and the shown anomaly score heatmaps indicate that the localization aspect is meritous.
Weaknesses:
Despite the considerable list of related methods there is no experimental comparison with any of the other methods in Table 1. Although there are no methods that tick exactly the same boxes as the proposed method, having no direct comparison with any of the methods leaves the experimental evaluation unanchored. Therefore, in my understanding the only result that is not an ablation of the proposed method are the shown anomaly heatmaps which are of qualitative character.
The presentation of the method and the results seems quite opaque. Equation 2 which shows the computation of the pixel-wise score mentions "robustly scaled MSE" which is nothing that has a unique meaning to me. I would like to see a clearer description of how the final scores are computed. Section 4 mentions that "We extended the available pixel-wise ground truth, as shown in Figure 3 by frame-wise annotations.". Does that mean that ground truth for IoU computation was added to the AnoVox benchmark? If so, how? This seems like an important detail since the computed evaluation is based on this ground truth information.
Minor Comments:
The formatting seems a bit unfortunate since referenced Tables and Figures are often far from the text referencing them. It feels like there should be a reference to Table 2 again in the ablation paragraph of section 4.1.
The difference between the two graphs in Fig. 5 should be emphasized and font sizes enlaged.

#### Rating
6: Marginally above acceptance threshold

#### Confidence
3: The reviewer is fairly confident that the evaluation is correct

### Program Chairs

#### Decision
Accept (Oral)

#### Comment
The reviewers lean toward accepting the paper, however we would appreciate to take into account the reviewer's comments for the camera ready version.

</details>

&nbsp;
&nbsp;

### UMAD: Unsupervised Mask-Level Anomaly Detection for Autonomous Driving
12/2024 • Daniel Bogdoll*, Noël Ollick*, Tim Joseph, J. Marius Zöllner

<img width="100%" src="https://github.com/user-attachments/assets/77a6fc26-5c5c-4129-9590-0d796750f88d">

[Proceeding](https://bmva-archive.org.uk/bmvc/2024/workshops/RROW/03_UMAD_Unsupervised_Mask_Level.pdf) | [arXiv](https://arxiv.org/abs/2406.06370v1)

:white_check_mark: Accepted at [BMVC Workshop on Robust Recognition in the Open World](https://rrow2024.github.io/)

<details>
  <summary markdown="span">BibTeX Citation</summary>
  
  ```
  @InProceedings{Bogdoll_UMAD_2024_BMVC,
    author={Bogdoll, Daniel and Ollick, Noël and Joseph, Tim and Zöllner, J. Marius},
    title     = {{UMAD: Unsupervised Mask-Level Anomaly Detection for Autonomous Driving}}, 
    booktitle = {British Machine Vision Conference (BMVC) Workshop},
    year      = {2024}
  }
  ```
</details>

<details>
  <summary>
    :orange_circle: Double-Blind
    :green_circle: High Quality Reviews
</summary>
  
### Reviewer 1

This paper proposes the UMAD method for anomaly detection. UMAD reconstructs sensory data using a world model to detect anomalies through visual and temporal comparisons, combined with a weighted fusion of pixel-wise scores. The results are further refined by masks generated by a segmentation model.

#### Review
Pros:
UMAD is an unsupervised method, it minimizes the need of labeled data for anomaly detection, which is typically scarce in autonomous driving scenarios.

Cons:
The problem statement is not defined.
The writing could be improved, such as: unexplained abbreviation 'OOD' in line 41, redundant text in lines 114-117 repeated in lines 133-136.
The Abstract and Introduction lack detail and clarity, for example, it could benefit from information regarding the models and the type of data used in the paper.
Claims made in lines 97-104 of the text could use some relevant citations.
Certain parts of the paper are difficult to comprehend, for example: terms like 'raw sensor recordings', 'multimodal sensor data' are vaguely used without clarification. Table. 2 is missing a clear explanation; what does 'Max. Value' mean?

#### Rating
6: Marginally above acceptance threshold

#### Confidence
3: The reviewer is fairly confident that the evaluation is correct

### Reviewer 2

Valuable idea and study, though the practical performance and generality is limited.

#### Review
This paper attempts to detect anomalous objects in driving scenes in a completely unsupervised manner. It relies on the idea that the anomalies will not be correctly reconstructed by a MUVO "world model" trained purely on the non-anomalous sensor data. Specifically, sensor inputs from a simulated self driving vehicle are fed to the MUVO to predict future camera frames, these predicted frames are then compared with actual input frames, and discrepancies in appearance are detected.

Strengths:
(S1) Extensive comparison of multiple appearance difference metrics. Interesting finding that the perceptual difference (difference in features on a pretrained CNN) is the best at finding anomalous differences, compared to pixel-focused distances such L1, L2, or SSIM.

(S2) The idea of comparing the predictions to the real images. Comparing the predictions to the actual inputs validates the extent to which the "world model" models the scene. Thus finding things which do not construct correctly is of interest not only just as an anomaly detection method but as a validation module too. Therefore it is a good idea to propose, especially with the showing how to meaningfully find those differences with the perceptual distance.

(S3) Clear description of the method

(S4) Furthering the underexplored field of purely unsupervised driving anomaly detection, providing a reasonable method to build upon.

Weaknesses:
(W1) All experiments are on synthetic data from the CARLA simulator. While it is understandable that the "world model" requires LiDAR and driving path which are not available in current real anomaly datasets, the generality of the study conclusion is really limited by that setup.

(W2) The performance reported is quite low, and it might be that the method just detects dynamic objects as opposed to backgrounds.

Qualitatively, it appears that the reconstruction error is correlated with all dynamic/discrete objects - it shows up on pedestrians and vehicles too in Fig2. In constrast, the prediction of the road region is much more similar to the real image. It might be that predicting the future of dynamic objects in general (both known and anomalous) is more uncertain than predicting the future of static roads and backgrounds. The system might end up doing just foreground vs background scene segmentation. The evaluation metrics are calculated with respect to all images in the pixel. The staic background pixels greatelny outnumber the foreground ones. So the results of around 80% AUROC might just be achieved by selecting all foreground objects.

It would be good to measure the performance on just the dynamic objects - precision of distinguishing anomalies from cars, pedestrians, etc.

(W3) LiDAR is not used The experiments are done on camera alone even though the simulation and MUVO include LIDAR.

#### Rating
7: Good paper, accept

#### Confidence
4: The reviewer is confident but not absolutely certain that the evaluation is correct

### Reviewer 3

Interesting problem, but the manuscript has some flaws

#### Review
Summary: The paper considers the problem of unsupervised anomaly detection in dense prediction for autonomous driving. It argues that the most of the recent autonomous driving research considers the anomaly detection problem given the supervised segmentation model. These methods, especially those trained with outlier exposure, are more likely to fail when deployed to the open world because of the limited training data. On the other hand, unsupervised training has access to practically unlimited data. The proposed method observes multimodal sensor data (images, lidar point clouds, planned vehicle routes) and provides a dense anomaly map. In the first stage, the world model observes the sensor data and provides an RGB reconstruction of the current frame, as well as multiple future predictions. The per-pixel anomaly scores are obtained by computing different sorts of reconstruction errors (absolute, squared, SSIM, VGG perceptual distance) with respect to the current frame. Besides that, the per-pixel anomaly score is also estimated as a level of disagreement between the future predictions from previous frames and the current reconstruction. Finally, all of the anomaly scores are combined with a weighted sum and refined using the mask predictions from the unsupervised segmentation model. The experiments were conducted on a custom dataset generated with the AnoVox benchmark.

Strenghts: The paper considers an underexplored problem of unsupervised anomaly detection for autonomous driving. The proposed method seems sound and simple. Presented results outperform the considered baseline MNAD.

Weaknesses: The manuscript is hard to read at times and requires an improvement in writing. For example, using index x to denote ground truth, and index y to denote predicted value seems uncommmon. Usually, the predicted value is denoted with hat, while the ground truth is written without the hat. Table 2 is shown before it is mentioned in the text. The same table could probably fit in two row-sections, which may be more visually pleasing. This way it is hard to understand which numbers should be compared to which. The corresponding section 5 "Evaluation" is also confusing, as it is often not clear which section of the Table 2 it refers to.

While the method considers different reconstruction errors to estimate the anomaly score, the experiments reveal the best results when relying solely on the perceptual difference. Although the method is described as unsupervised, the VGG used to compute this metric is pre-trained on ImageNet labels. This should be discussed and clarified.

It is not clear whether the comparison to MNAD is fair, because line 228 claims that the MUVO is trained on a much larger dataset. The data subsampling to prevent overfitting is unusual and should be better explained.

The paper should discuss differences to other reconstruction-based anomaly detection methods such as [1,2,3]. The results from Table 2 would be more convincing if it considered other methods from the literature as well.

Comment: I wonder if self-supervised would be a better attribute than unsupervised to describe this method. It seems to me that both the world model and the segmentation model are trained in a self-supervised manner.

[1] Eli Schwartz, Assaf Arbelle, Leonid Karlinsky, Sivan Harary, Florian Scheidegger, Sivan Doveh, Raja Giryes. MAEDAY: MAE for few- and zero-shot AnomalY-Detection. Computer Vision and Image Understanding.

[2] Vitjan Zavrtanik, Matej Kristan, Danijel Skočaj. Reconstruction by inpainting for visual anomaly detection. Pattern Recognition.

[3] Jiang, J., Zhu, J., Bilal, M., Cui, Y., Kumar, N., Dou, R., ... & Xu, X. (2022). Masked swin transformer unet for industrial anomaly detection. IEEE Transactions on Industrial Informatics.

#### Rating
5: Marginally below acceptance threshold

#### Confidence
3: The reviewer is fairly confident that the evaluation is correct

### Program Chairs

#### Decision
Accept (Oral)

#### Comment
The reviewers lean toward accepting the paper, however we would appreciate to take into account the reviewer's comments for the camera ready version.

</details>

&nbsp;
&nbsp;

### Informed Reinforcement Learning for Situation-Aware Traffic Rule Exceptions
08/2024 • Daniel Bogdoll*, Jing Qin*, Moritz Nekolla, Ahmed Abouelazm, Tim Joseph, J. Marius Zöllner

<img width="100%" src="https://github.com/user-attachments/assets/6fc197d5-caae-47d3-b340-57305c8d5dae">

[Proceeding](https://ieeexplore.ieee.org/document/10610842) | [Code](https://github.com/fzi-forschungszentrum-informatik/informed_rl) | [arXiv](https://arxiv.org/abs/2402.04168)

:white_check_mark: Accepted at [IEEE International Conference on Robotics and Automation (ICRA)](https://2024.ieee-icra.org/)

<details>
  <summary markdown="span">BibTeX Citation</summary>
  
  ```
  @InProceedings{Bogdoll_Informed_2024_ICRA,
    author={Bogdoll, Daniel and Qin, Jing and Nekolla, Moritz and Abouelazm, Ahmed and Joseph, Tim and Zöllner, J. Marius},
    title     = {{Informed Reinforcement Learning for Situation-Aware Traffic Rule Exceptions}}, 
    booktitle = {IEEE International Conference on Robotics and Automation (ICRA)},
    year      = {2024}
  }
  ```
</details>

<details>
  <summary>
    :red_circle: Single-Blind
    :orange_circle: Medium Quality Reviews
</summary>
  
### Reviewer 1

The authors propose an Informed reward function with a rule
book for situation-aware driving. The authors did an
excellent job of explaining each section in short and
sweet. The concept of Rule realization and rulebook is used
here and is implemented within the reward function. As
written in the paper, Rule realization and rulebooks were
already introduced by Censi et al. So the main
contribution, I think, is including them in the reward
function. Curriculum learning is used where the agents are
trained in a regular environment first and then introduced
to situations that require controlled traffic rule
exceptions. The results show that including the rulebook
does improve performance for the dreamer algorithm, but for
the rainbow algorithm, it didn’t. As mentioned adding just
the rulebook didn’t make the performance go up. Why was
Rainbow+rulebook+trajectory or rainbow+trajectory not
studied?
1.	The introduction does not have any references for
the statements made. 
2.	While the authors have identified unstructured
reward designs as a limitation in previous work and propose
a structured reward function as one of their contributions,
the introduction of numerous heuristic parameters in
Equation 3 seems to compromise this. Basically, the reward
function should still be improved.  
3.	In section 3. c, line 9, it should be “similar to”
4.	The plots are hard to look at, authors should
consider smoothening the lines and make the size bigger.

#### Reviewer 2

This paper introduces a situation-dependent reward function
structure, allowing human logic to be combined with Deep RL
in autonomous driving applications.  The method seems
highly useful in scenarios which are poorly represented by
the training dataset. This method is likely useful in
non-AV applications.

I have several comments/questions:

1) The authors should briefly explain their decision to
model this problem as POMDP.  For example, perhaps mention
RGB data alone not enough to infer velocity, etc. 

2) What is the network architecture?  Are CNN's used to
process the raw images?  If these details are explained in
the Dreamer and Rainbow papers, please indicate.  

3) In Figure 1, does the hierarchical rulebook not need to
"see" the observation o_t so as to correctly assign weights
p_j?  Alternatively, does the HRB receive some ground truth
input during training to correctly assign weights p_j?	If
so, please indicate in the Figure.  To promote learning
convergence the reward should be correlated with the
observation in some way.

4) Figure 7 is confusing.  Are the Frenet coordinates not
v,d,t?	I'm not seeing v in the bottom trajectory plot. 
Maybe state the trajectory is plotted in d and t only. 
Also, do the red triangles represent the start and end of
the activation range? The top figure does not appear to
align with the placement of these triangles.

5) Reference [34] should be updated to its IEEE
Transactions on Aerospace and Electronic Systems version.

6) Depending on the page limit, a brief description of the
Frenet Space would improve the quality of the paper.  

7) In the Conclusion section, the following statement is
made without reference: "As already shown in
the literature, a continuous action space for the
generation of trajectories could be implemented into our
work." Please include a reference.  

8) Figure 5 is a bit difficult to read.  The noise should
be plotted with a higher transparency (behind the filtered
means) for readability.

#### Associate Editor

I appreciate the innovative approach presented in your
paper, incorporating a rulebook into the reward function
for situation-aware driving. Both reviewers commend the
clarity of the explanations and the utilization of
curriculum learning. However, some concerns need
addressing. First, the introduction lacks proper
references, and the reward function, while structured,
introduces heuristic parameters, prompting the need for
refinement. Clarifications are sought on the absence of
Rainbow+rulebook+