> **Türkçe:** Bu eğitim Türkçe yürütülmektedir. **[Eğitimin Türkçe sayfasına geçin](README.tr.md)**

<div align="center">

# Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists

**Training program, Turkish Society of Cardiology (Türk Kardiyoloji Derneği), Türkiye**

*Eleven weeks of Python and artificial intelligence for cardiologists and other specialist physicians: a virtual cardiology clinic, real ECG data, interactive labs, Jupyter notebooks and safe coding with AI assistants*

![first version: November 2026](https://img.shields.io/badge/first%20version-November%202026-566A73)
![program: Turkish Society of Cardiology](https://img.shields.io/badge/program-Turkish%20Society%20of%20Cardiology-1F5F8B)
![format: 11 weeks, 44 hours](https://img.shields.io/badge/format-11%20weeks%2C%2044%20hours-1F5F8B)
![delivery: weekly live session + self-study](https://img.shields.io/badge/delivery-weekly%20live%20session%20%2B%20self--study-0E7A78)
![notebooks: Google Colab · Jupyter (Anaconda)](https://img.shields.io/badge/notebooks-Google%20Colab%20%C2%B7%20Jupyter%20%28Anaconda%29-F9AB00)
![languages: English · Türkçe](https://img.shields.io/badge/languages-English%20%C2%B7%20T%C3%BCrk%C3%A7e-0E7A78)
[![content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-555555)](LICENSE-CONTENT)
[![code: MIT](https://img.shields.io/badge/code-MIT-555555)](LICENSE)

**This course is updated in line with current developments in the field. First version: November 2026.**

**Prof. Dr. Utku Kose**

Full Professor, Department of Computer Engineering, Süleyman Demirel University, Isparta, Türkiye<br>
Founding Director, AI Application and Research Center (YAZEM), Süleyman Demirel University<br>
Head of the Computer Science Division, Department of Computer Engineering, Süleyman Demirel University<br>
Additional affiliations: University of North Dakota (USA), Universidad Panamericana (Mexico City, Mexico), Vel Tech University (Chennai, India)<br>
IEEE Senior Member, ACM Professional Member

[ORCID 0000-0002-9652-6415](https://orcid.org/0000-0002-9652-6415) | [utkukose.com](https://www.utkukose.com) | [github.com/utkukose](https://github.com/utkukose)

[utkukose@sdu.edu.tr](mailto:utkukose@sdu.edu.tr) | [utku.kose@und.edu](mailto:utku.kose@und.edu) | [ukose@up.edu.mx](mailto:ukose@up.edu.mx) | [utkukose@gmail.com](mailto:utkukose@gmail.com)

[Türkçe sürüm](README.tr.md)

</div>

## About the course

This repository holds the open materials of *Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists*, prepared for the Turkish Society of Cardiology. The program runs for eleven weeks with one four-hour session per week, 44 hours in total, and about 80 percent of the time is hands-on work. Every week combines a clinical case, a lecture page that forms the main route of the week, an interactive lab, a Jupyter notebook with two paths of practice and a weekly project. All materials are available in English and in Turkish, and the training is held in Turkish.

The thread of the course is a virtual cardiology clinic. The course package `vclinic` creates a registry of synthetic patients whose electrocardiograms (ECGs), laboratory values and, in later weeks, images and reports agree with each other. Each week opens one unit of the clinic, from the patient registry and the ECG laboratory in Week 1 to decision support at the bedside in Week 10. Because the true values behind the synthetic data are known, every measurement and every model can be checked against the truth. Real public data sets run alongside in every week, so that each method is also tested on real recordings.

The course also teaches how to work with artificial intelligence (AI) assistants. From the first week, every practice stop can be done on the prompt path, on which an assistant writes the code from ready prompts, or on the Python path, on which the participant writes it. Prompts state units and tests, the code is checked with a code safety checklist, and every use is recorded in an AI usage log. Patient data never enter a prompt.

**Course site (optional).** The flow of the course can also be followed on the course site, [utkukose.github.io/ai-cardiology-tkd-NB-lecture](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/). The site brings the lecture pages, the interactive labs and the Jupyter notebooks of the weeks together, which makes it more practical to move through the course.

## Use in other courses

The materials may be used at any level, in whole or in part, with attribution (see [Citing this course](#citing-this-course)). Errors and suggestions can be reported in the [issues](https://github.com/utkukose/ai-cardiology-tkd-NB-lecture/issues) of the repository. During an active delivery of the course, questions and weekly projects can be sent to utkukose@sdu.edu.tr or utkukose@gmail.com.

## A look inside

<table>
<tr><td width="50%"><img src="en/week-01/figures/w01_scene.png" alt="Lecture page, Week 1: the cardiac cycle in three dimensions. The heart vector sweeps through the beat while the chosen lead is drawn beside it." width="100%"></td><td width="50%"><img src="en/week-01/screenshots/lab_part_b_heart_vector.png" alt="Interactive lab, Week 1, Part B: twelve views of one vector, with the projection on each lead computed step by step." width="100%"></td></tr>
<tr><td>Lecture page, Week 1: the cardiac cycle in three dimensions. The heart vector sweeps through the beat while the chosen lead is drawn beside it.</td><td>Interactive lab, Week 1, Part B: twelve views of one vector, with the projection on each lead computed step by step.</td></tr>
<tr><td width="50%"><img src="en/week-01/screenshots/lab_part_c_calipers.png" alt="Interactive lab, Week 1, Part C: digital calipers on the ECGs of the virtual clinic. The measurements go on to a Bland-Altman analysis in the Jupyter notebook." width="100%"></td><td width="50%"><img src="en/week-01/screenshots/notebook_12lead_ecg.png" alt="Jupyter notebook, Week 1, Section 4: the 12-lead ECG of the case of the week, VC-0317." width="100%"></td></tr>
<tr><td>Interactive lab, Week 1, Part C: digital calipers on the ECGs of the virtual clinic. The measurements go on to a Bland-Altman analysis in the Jupyter notebook.</td><td>Jupyter notebook, Week 1, Section 4: the 12-lead ECG of the case of the week, VC-0317.</td></tr>
<tr><td width="50%"><img src="en/week-01/screenshots/lab_part_f_prompt_workshop.png" alt="Interactive lab, Week 1, Part F: the prompt workshop. The seven fields of the prompt card, a quality meter and a privacy check." width="100%"></td><td width="50%"><img src="en/week-01/screenshots/notebook_prompt_path.png" alt="Jupyter notebook, Week 1, prompt path, Stop 2: a ready prompt, the code of an AI assistant and the check of the course." width="100%"></td></tr>
<tr><td>Interactive lab, Week 1, Part F: the prompt workshop. The seven fields of the prompt card, a quality meter and a privacy check.</td><td>Jupyter notebook, Week 1, prompt path, Stop 2: a ready prompt, the code of an AI assistant and the check of the course.</td></tr>
<tr><td width="50%"><img src="en/week-02/figures/w02_scene.png" alt="Lecture page, Week 2: k-means in three dimensions on the 407 patients with heart failure. The algorithm assigns and moves its centres step by step until the clusters stop changing." width="100%"></td><td width="50%"><img src="en/week-02/screenshots/lab_part_b_threshold.png" alt="Interactive lab, Week 2, Part B: the threshold of a model for coronary artery disease, its confusion matrix, the four measures and the point on the ROC curve." width="100%"></td></tr>
<tr><td>Lecture page, Week 2: k-means in three dimensions on the 407 patients with heart failure. The algorithm assigns and moves its centres step by step until the clusters stop changing.</td><td>Interactive lab, Week 2, Part B: the threshold of a model for coronary artery disease, its confusion matrix, the four measures and the point on the ROC curve.</td></tr>
<tr><td width="50%"><img src="en/week-03/figures/w03_scene.png" alt="Lecture page, Week 3: inside the network of the imaging laboratory. The ED and ES frames of a cine CMR slice of ACDC pass through three blocks of feature maps to the probabilities of a normal heart, DCM and HCM. Images: ACDC, CC BY-NC-SA 4.0." width="100%"></td><td width="50%"><img src="en/week-03/screenshots/lab_part_b_convolution.png" alt="Interactive lab, Week 3, Part B: a 3 × 3 kernel slides over a cine CMR slice of ACDC, with the nine products of one position and the feature map that grows. Images: ACDC, CC BY-NC-SA 4.0." width="100%"></td></tr>
<tr><td>Lecture page, Week 3: inside the network of the imaging laboratory. The ED and ES frames of a cine CMR slice of ACDC pass through three blocks of feature maps to the probabilities of a normal heart, DCM and HCM. Images: ACDC, CC BY-NC-SA 4.0.</td><td>Interactive lab, Week 3, Part B: a 3 × 3 kernel slides over a cine CMR slice of ACDC, with the nine products of one position and the feature map that grows. Images: ACDC, CC BY-NC-SA 4.0.</td></tr>
<tr><td width="50%"><img src="en/week-04/figures/w04_scene.png" alt="Lecture page, Week 4: the left ventricle of patient 201 of CAMUS as 20 discs. Each disc is an ellipse with one diameter from the two-chamber and one from the four-chamber view, and the volume is the sum of the discs. Data: CAMUS, CC BY-NC-SA 4.0." width="100%"></td><td width="50%"><img src="en/week-04/screenshots/lab_part_d_bland_altman.png" alt="Interactive lab, Week 4, Part D: the Bland-Altman plot of the ejection fraction of the U-Net on the 50 test patients of CAMUS, with the bias, the limits of agreement and one patient clicked. Data: CAMUS, CC BY-NC-SA 4.0." width="100%"></td></tr>
<tr><td>Lecture page, Week 4: the left ventricle of patient 201 of CAMUS as 20 discs. Each disc is an ellipse with one diameter from the two-chamber and one from the four-chamber view, and the volume is the sum of the discs. Data: CAMUS, CC BY-NC-SA 4.0.</td><td>Interactive lab, Week 4, Part D: the Bland-Altman plot of the ejection fraction of the U-Net on the 50 test patients of CAMUS, with the bias, the limits of agreement and one patient clicked. Data: CAMUS, CC BY-NC-SA 4.0.</td></tr>
<tr><td width="50%"><img src="en/week-05/figures/w05_scene.png" alt="Lecture page, Week 5: the ST injury vector of an acute infarction and its projections on the twelve leads. The leads that reach the cut-points of the universal definition turn red, and the alarm names the group of contiguous leads." width="100%"></td><td width="50%"><img src="en/week-05/screenshots/lab_part_d_st.png" alt="Interactive lab, Week 5, Part D: the median beats of the twelve leads of record 13913 of PTB-XL, with the PR segment, the J point, the ST deviation of each lead and the decision of the STEMI alarm. Data: PTB-XL, CC BY 4.0." width="100%"></td></tr>
<tr><td>Lecture page, Week 5: the ST injury vector of an acute infarction and its projections on the twelve leads. The leads that reach the cut-points of the universal definition turn red, and the alarm names the group of contiguous leads.</td><td>Interactive lab, Week 5, Part D: the median beats of the twelve leads of record 13913 of PTB-XL, with the PR segment, the J point, the ST deviation of each lead and the decision of the STEMI alarm. Data: PTB-XL, CC BY 4.0.</td></tr>
<tr><td width="50%"><img src="en/week-06/figures/w06_scene.png" alt="Lecture page, Week 6: forty words of the synthetic report archive in three dimensions, placed by their word vectors. With the whole summary as context, the words gather by disease, and apixaban stands next to the other anticoagulants and the irregular rhythm." width="100%"></td><td width="50%"><img src="en/week-06/screenshots/lab_part_d_angiography.png" alt="Interactive lab, Week 6, Part D: a synthetic coronary angiography report with its arteries, segments and stenoses, the sentences as the pipeline reads them and the four territories next to the registry." width="100%"></td></tr>
<tr><td>Lecture page, Week 6: forty words of the synthetic report archive in three dimensions, placed by their word vectors. With the whole summary as context, the words gather by disease, and apixaban stands next to the other anticoagulants and the irregular rhythm.</td><td>Interactive lab, Week 6, Part D: a synthetic coronary angiography report with its arteries, segments and stenoses, the sentences as the pipeline reads them and the four territories next to the registry.</td></tr>
<tr><td width="50%"><img src="en/week-07/figures/w07_scene.png" alt="Lecture page, Week 7: the left angiogram of VC-2427 cut into the 196 patches of ViT-B/16. The bars give the largest attention of the class token, or of a patch chosen with a click, in a single layer or followed through all twelve, and the squares mark the stenoses of the registry." width="100%"></td><td width="50%"><img src="en/week-07/screenshots/lab_part_c_thresholds.png" alt="Interactive lab, Week 7, Part C: the threshold of the hybrid over its probabilities on the test patches of ARCADE, with the sensitivity, the specificity and the positive predictive value at the prevalence of the patches and at 2 percent." width="100%"></td></tr>
<tr><td>Lecture page, Week 7: the left angiogram of VC-2427 cut into the 196 patches of ViT-B/16. The bars give the largest attention of the class token, or of a patch chosen with a click, in a single layer or followed through all twelve, and the squares mark the stenoses of the registry.</td><td>Interactive lab, Week 7, Part C: the threshold of the hybrid over its probabilities on the test patches of ARCADE, with the sensitivity, the specificity and the positive predictive value at the prevalence of the patches and at 2 percent.</td></tr>
<tr><td width="50%"><img src="en/week-08/figures/w08_scene.png" alt="Lecture page, Week 8: the 800 test patients of the chest pain unit in the space of the logits of three single models, the clinical table, the troponin and the ECG. The plane of late fusion, by the mean of the logits or by stacking, separates the patients called high risk at the chosen threshold." width="100%"></td><td width="50%"><img src="en/week-08/screenshots/lab_part_d_discharge.png" alt="Interactive lab, Week 8, Part D: a threshold for discharge over the predicted risks of the 800 test patients, with the patients sent home, the missed events with their Wilson interval, the sensitivity and the net benefit next to HEART 0 to 3." width="100%"></td></tr>
<tr><td>Lecture page, Week 8: the 800 test patients of the chest pain unit in the space of the logits of three single models, the clinical table, the troponin and the ECG. The plane of late fusion, by the mean of the logits or by stacking, separates the patients called high risk at the chosen threshold.</td><td>Interactive lab, Week 8, Part D: a threshold for discharge over the predicted risks of the 800 test patients, with the patients sent home, the missed events with their Wilson interval, the sensitivity and the net benefit next to HEART 0 to 3.</td></tr>
<tr><td width="50%"><img src="en/week-09/figures/w09_scene.png" alt="Lecture page, Week 9: the eight coalitions of three variables of patient 172 as the corners of a cube. Each edge adds one variable, and the six paths from the empty coalition to the full one are the six orders whose mean contributions give the Shapley values." width="100%"></td><td width="50%"><img src="en/week-09/screenshots/notebook_gradcam.png" alt="Jupyter notebook, Week 9, Section 6: Grad-CAM maps of the echo network on test views of CAMUS, with the expert outline of the left ventricle. Data: CAMUS, CC BY-NC-SA 4.0." width="100%"></td></tr>
<tr><td>Lecture page, Week 9: the eight coalitions of three variables of patient 172 as the corners of a cube. Each edge adds one variable, and the six paths from the empty coalition to the full one are the six orders whose mean contributions give the Shapley values.</td><td>Jupyter notebook, Week 9, Section 6: Grad-CAM maps of the echo network on test views of CAMUS, with the expert outline of the left ventricle. Data: CAMUS, CC BY-NC-SA 4.0.</td></tr>
</table>

## Who the course is for

The course is written for cardiologists and other specialist physicians. No programming experience and no previous knowledge of artificial intelligence are needed. The lecture page of each week is the main route: It explains the concepts without code and without prompts. At two or three practice stops of the page, every participant chooses one of two paths in the Jupyter notebook. On the **prompt path** (Part 1 of the notebook), an AI assistant writes the code from ready prompts, and the participant runs it and checks the result; ready code is at hand for every step, so no one gets stuck ([PROMPT_PATH.md](PROMPT_PATH.md)). On the **Python path** (Part 2), the participant learns to write the code with a Python step and exercises ([PYTHON_PATH.md](PYTHON_PATH.md)). Both paths reach the same results, and the path can be changed at any stop. Clinical knowledge of the ECG and of cardiac imaging is assumed, and the mathematics is introduced where it is needed, with worked examples.

## Course learning outcomes

By the end of the course, participants are expected to analyse clinical tables, signals and images with Python, and to build, validate and explain machine learning and deep learning models on cardiology data. They should be able to process the ECG as a signal, train models that detect rhythm disorders and ischaemia, and segment cardiac images to measure the ejection fraction. They should be able to extract information from clinical text, combine data of several kinds in one model and explain the decisions of a model with methods of explainable artificial intelligence (XAI). Finally, they should be able to build a prototype of a clinical decision support system (CDSS), work with AI assistants safely and appraise published AI studies in cardiology critically.

## How the course works

Every week follows the same rhythm. It opens with **the case of the week**, a patient of the virtual clinic whose question is answered by the end of the week. The **lecture page** is the main route: It explains the concepts with formulas, worked examples, a three-dimensional (3D) scene, animations and knowledge checks, and it contains no code. The **interactive lab** turns the key ideas into simulations and step-by-step calculations in the browser. At the **practice stops** of the lecture page, the **Jupyter notebook** carries out the same ideas on synthetic and real data, on the prompt path or on the Python path. A section **with your own data** shows how the methods of the week apply to the data of one's own clinic. **The paper of the week** connects the topic with a published study, and the **weekly project** applies the methods to new patients and real records. Each week ends with a new **stage of the virtual clinic**.

| Material | Role |
|---|---|
| Week page (README) | Overview of the week: materials, learning outcomes, study path, weekly project and submission |
| Lecture page (main route) | Concepts, formulas with worked examples, a 3D scene, animations, knowledge checks, practice stops, the section on your own data and review cards; no code and no prompts |
| Interactive lab | Simulations and calculations in Parts A, B, C and so on, a self-assessment and a learning log to export |
| Jupyter notebook | Part 1, the prompt path: the steps of each practice stop with a ready prompt, an automatic check and ready code. Part 2, the Python path: a Python step and numbered sections with exercises that check themselves. It runs in Google Colab or in Jupyter (Anaconda). |
| Prompt library | Every prompt of the prompt path of the week, with a copy button on GitHub |
| PDF notes | The lecture page for reading and printing, with the prompts and the Python step in two appendices |

The materials link to each other in both directions. The lecture page opens the parts of the interactive lab in the order A, B, C and the practice stops in increasing order. Each practice stop names the step of the prompt path and the sections of the Python path that reach its result. Every part of the lab and every stop in the Jupyter notebook ends with a link back to the lecture page, to the place where reading continues.

## The order of the materials

Every week is worked through in the same order. Each material names the next step and the place to return to, so nobody gets lost between the materials when the order below is followed.

1. **Setup, once.** Install Anaconda, download the course folder and run the [start-here Jupyter notebook](en/start-here/README.md), following the [setup guide](SETUP.md). Those who cannot install anything open the same Jupyter notebooks in Google Colab.
2. **Week page.** Open the week page (README) of the week. Its table «Study path» lists every step of the week in order, with its time.
3. **Lecture page.** Read the lecture page from top to bottom. It is the main route of the week.
4. **Blue boxes: the interactive lab.** At a blue box, open that part of the lab with the button of the box. Do the part, click «Back to the lecture page» at its end and continue reading below the box.
5. **Orange boxes: the practice stops.** At an orange box, open the Jupyter notebook of the week in Colab or in Jupyter and choose your path: the stop in Part 1 on the prompt path, or the sections in Part 2 on the Python path. The link at the end of the stop takes you back to the lecture page, to the place where reading continues.
6. **Finishing the week.** Follow the box «Finishing the week» at the end of the lecture page: Take the self-assessment in the tab «Check yourself» of the lab, export the learning log in the tab «Reflect and export» and submit the weekly project.
7. **Next week.** Go on to the next week with the link in the section «Next week» of the week page.

The PDF notes are the printable version of the lecture page, optional for reading and review. The prompt library gathers every prompt of the prompt path; the prompts are in the Jupyter notebook as well. If you lose your place, return to the table «Study path» on the week page.

## The eleven weeks

The plan follows the program of the Turkish Society of Cardiology. Each week is published with all its materials, and the [syllabus](SYLLABUS.md) describes the content of every session.

| Week | Topic | Stage of the virtual clinic | Weekly project |
|---|---|---|---|
| 1 | [Python and cardiology data basics](en/week-01/README.md) | Patient registry and ECG laboratory | A script that visualises the ECG and calculates its basic measurements, PR, QRS and QT, automatically |
| 2 | [Machine learning fundamentals](en/week-02/README.md) | Risk outpatient clinic | HFpEF vs HFrEF patient clustering with Kaplan-Meier survival analysis |
| 3 | [Deep learning and CNN fundamentals](en/week-03/README.md) | Imaging laboratory | Cardiac MRI, ACDC data set: Automatic classification of dilated and hypertrophic cardiomyopathy |
| 4 | [Transfer learning: Adapting ready-made power to cardiology](en/week-04/README.md) | Echo measurement: Automatic ejection fraction | Left ventricular segmentation with the CAMUS data set and automatic calculation of the EF |
| 5 | [Time series analysis and ECG artificial intelligence](en/week-05/README.md) | Rhythm and STEMI alarm | STEMI alarm system: Automatic detection of ST deviation from AMI ECGs (PTB-XL) |
| 6 | [NLP and clinical text mining](en/week-06/README.md) | Report archive: Clinical text | Cardiac angiography report NLP pipeline: Automatic extraction of the degree of stenosis and the affected vessel |
| 7 | [Vision Transformer (ViT): The new generation in image processing](en/week-07/README.md) | Catheterisation laboratory | Coronary angiography: Stenosis detection, CNN vs ViT vs hybrid comparison + attention maps |
| 8 | [Multimodal artificial intelligence and data fusion](en/week-08/README.md) | Heart team: Data fusion | Real-time MACE prediction model: Simulation of a triage scenario (synthetic MIMIC-IV) |
| 9 | [Model reliability and explainable artificial intelligence (XAI)](en/week-09/README.md) | Quality and safety committee: XAI | Visualising with Grad-CAM where an echocardiography model looks, compared with the reading of an expert |
| 10 | [Clinical decision support systems (CDSS)](en/week-10/README.md) | Decision support at the bedside | User test session: Improving the CDSS prototype with feedback |
| 11 | [Final project and graduation](en/week-11/README.md) | Own units: Final projects | Final project presentation and the personal action plan "How will I use AI in my clinical practice?" |

### Materials of each week

Each material of a week has its own column. The week page gives an overview of the week, and the Jupyter notebook also opens in Google Colab from the week page.

| Week | Lecture page | Interactive lab | Jupyter notebook | Prompt library | PDF notes |
|---|---|---|---|---|---|
| [Week 1](en/week-01/README.md) | [Lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-01/lecture.html) | [Interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-01/lab.html) | [Notebook](en/week-01/NB01_python_and_ecg_basics.ipynb) | [Prompts](en/week-01/PROMPTS.md) | [PDF](en/week-01/Week01_Lecture_Notes.pdf) |
| [Week 2](en/week-02/README.md) | [Lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-02/lecture.html) | [Interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-02/lab.html) | [Notebook](en/week-02/NB02_machine_learning_fundamentals.ipynb) | [Prompts](en/week-02/PROMPTS.md) | [PDF](en/week-02/Week02_Lecture_Notes.pdf) |
| [Week 3](en/week-03/README.md) | [Lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-03/lecture.html) | [Interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-03/lab.html) | [Notebook](en/week-03/NB03_deep_learning_and_cnns.ipynb) | [Prompts](en/week-03/PROMPTS.md) | [PDF](en/week-03/Week03_Lecture_Notes.pdf) |
| [Week 4](en/week-04/README.md) | [Lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-04/lecture.html) | [Interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-04/lab.html) | [Notebook](en/week-04/NB04_transfer_learning.ipynb) | [Prompts](en/week-04/PROMPTS.md) | [PDF](en/week-04/Week04_Lecture_Notes.pdf) |
| [Week 5](en/week-05/README.md) | [Lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-05/lecture.html) | [Interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-05/lab.html) | [Notebook](en/week-05/NB05_time_series_and_ecg_ai.ipynb) | [Prompts](en/week-05/PROMPTS.md) | [PDF](en/week-05/Week05_Lecture_Notes.pdf) |
| [Week 6](en/week-06/README.md) | [Lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-06/lecture.html) | [Interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-06/lab.html) | [Notebook](en/week-06/NB06_clinical_text_mining.ipynb) | [Prompts](en/week-06/PROMPTS.md) | [PDF](en/week-06/Week06_Lecture_Notes.pdf) |
| [Week 7](en/week-07/README.md) | [Lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html) | [Interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lab.html) | [Notebook](en/week-07/NB07_vision_transformers.ipynb) | [Prompts](en/week-07/PROMPTS.md) | [PDF](en/week-07/Week07_Lecture_Notes.pdf) |
| [Week 8](en/week-08/README.md) | [Lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lecture.html) | [Interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lab.html) | [Notebook](en/week-08/NB08_multimodal_ai_and_data_fusion.ipynb) | [Prompts](en/week-08/PROMPTS.md) | [PDF](en/week-08/Week08_Lecture_Notes.pdf) |
| [Week 9](en/week-09/README.md) | [Lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-09/lecture.html) | [Interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-09/lab.html) | [Notebook](en/week-09/NB09_reliability_and_explainable_ai.ipynb) | [Prompts](en/week-09/PROMPTS.md) | [PDF](en/week-09/Week09_Lecture_Notes.pdf) |
| [Week 10](en/week-10/README.md) | [Lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-10/lecture.html) | [Interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-10/lab.html) | [Notebook](en/week-10/NB10_clinical_decision_support.ipynb) | [Prompts](en/week-10/PROMPTS.md) | [PDF](en/week-10/Week10_Lecture_Notes.pdf) |
| [Week 11](en/week-11/README.md) | [Lecture page](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-11/lecture.html) | [Interactive lab](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-11/lab.html) | [Notebook](en/week-11/NB11_final_project_workshop.ipynb) | [Prompts](en/week-11/PROMPTS.md) | [PDF](en/week-11/Week11_Lecture_Notes.pdf) |

## The virtual clinic, the project of the course

![The eleven stages of the virtual cardiology clinic](assets/clinic_stages_en.png)

The clinic grows by one unit every week. Its registry starts with 500 synthetic patients with demographic data, risk factors, laboratory values, an ejection fraction, a main diagnosis and a 12-lead ECG. Week 2 extends it to 2000 patients with echocardiographic variables and five years of follow-up. The effect sizes behind the registry are documented in the package, so that a fitted model can be compared with the truth. From Week 3, the clinic also reads real images from public research archives: cine cardiac magnetic resonance (CMR) examinations of ACDC, which every participant downloads from their public source, and echocardiography videos of EchoNet-Dynamic for participants with a personal registration. From Week 4, it also measures the apical echocardiograms of CAMUS, which every participant downloads from their public source as well. From Week 5, it reads the 12-lead ECGs of PTB-XL, which every participant downloads from PhysioNet. From Week 7, it also reads the X-ray coronary angiograms of ARCADE, which every participant downloads from Zenodo. Week 8 opens a chest pain unit at two hospitals, whose synthetic presentations bring a clinical table, a triage note, a 12-lead ECG, two troponins and a bedside echocardiogram together. Week 10 opens a telemetry ward with four synthetic patients and reads the Holter recordings of the MIT-BIH Atrial Fibrillation Database, which every participant downloads from PhysioNet. The images and the recordings never enter the repository. The table collects the results of the stages published so far.

| Week | Stage | Methods | Result |
|---|---|---|---|
| 1 | [Patient registry and ECG laboratory](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-01/lecture.html#the-virtual-clinic-stage-1-the-clinic-opens) | pandas, a 12-lead ECG model, automatic interval measurement, a simplified Pan-Tompkins detector | 500 patients; mean errors of −1.5 ms (PR), 2.3 ms (QRS) and 2.2 ms (QT) on 100 patients; 2273 of 2273 beats of MIT-BIH record 100 detected |
| 2 | [Risk outpatient clinic](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-02/lecture.html#the-virtual-clinic-stage-2-the-risk-outpatient-clinic-opens) | scikit-learn, logistic regression, cross-validation, random forests, k-means, Kaplan-Meier curves and the log-rank test | 2000 patients with five years of follow-up; cross-validated AUC of 0.871 for coronary artery disease on the Cleveland data; three phenogroups of heart failure with an adjusted Rand index of 0.71 and 64 to 89 percent free of events at 24 months |
| 3 | [Imaging laboratory](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-03/lecture.html#the-virtual-clinic-stage-3-the-imaging-laboratory-opens) | PyTorch, a convolutional neural network with three blocks, dropout, batch normalisation, augmentation and early stopping, precision, recall and F1 | Cine CMR of 90 patients of ACDC (normal, DCM, HCM); on the 30 test patients an accuracy of 0.933 and a macro F1 of 0.933 from three middle slices, against 0.967 for the rules of ACDC on the measurements of the expert contours |
| 4 | [Echo measurement: Automatic ejection fraction](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-04/lecture.html#the-virtual-clinic-stage-4-automatic-ejection-fraction) | EfficientNet-B0 pretrained on ImageNet, feature extraction and fine-tuning, a U-Net, the Dice coefficient, the biplane method of discs and the Bland-Altman analysis | Transfer learning on ACDC with five patients per group: 0.793 for the fine-tuned network against 0.720 for the network of Week 3; on 50 test patients of CAMUS a mean Dice coefficient of 0.924 and an EF bias of −4.2 points with limits of agreement from −20.5 to 12.0 |
| 5 | [Rhythm and STEMI alarm](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-05/lecture.html#the-virtual-clinic-stage-5-rhythm-and-stemi-alarm) | A rule from the RR intervals, a one-dimensional convolutional network, a GRU on the RR intervals, multi-label classification with thresholds from a validation fold, the median beat, the ST criteria of the universal definition, the QTc and a 24-hour Holter recording | On fold 10 of PTB-XL a mean AUC of 0.878 for six labels of rhythm (0.975 for AF), and 0.940 for the GRU on the RR intervals alone; the STEMI alarm on folds 9 and 10 with a sensitivity of 0.538 and a positive predictive value of 0.035, with 96 of 108 recordings with LBBB raising it |
| 6 | [Report archive: Clinical text](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-06/lecture.html#the-virtual-clinic-stage-6-report-archive) | A keyword rule, the assertion of a mention with the scope of a trigger, drugs and laboratory values as evidence, TF-IDF with logistic regression, word vectors, a tiny pretrained Turkish BERT model fine-tuned for named entities, the check of a summary against its report and a pipeline for angiography reports | 3,600 discharge summaries of two hospitals: macro F1 of the rule 0.980 on hospital A and 0.985 on hospital B, of TF-IDF 0.990 and 0.708; entity F1 of the fine-tuned BERT model 0.981 and 0.556; the number of diseased vessels right in 95.9 percent of the test reports of hospital A and in all reports of hospital B |
| 7 | [Catheterisation laboratory](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-07/lecture.html#the-virtual-clinic-stage-7-catheterisation-laboratory) | Attention, the vision transformer ViT-B/16 as a quality gate for echocardiography, synthetic angiograms, a small convolutional network, a small vision transformer and a hybrid on ARCADE, intervals by angiogram, attention rollout and a scan of whole angiograms | A quality gate with an AUC of 0.862 for poor frames on the 100 test frames of CAMUS; on the patches of 300 test angiograms of ARCADE AUCs of 0.810, 0.930 and 0.936 for the three networks, against 0.538 for the network that learned on synthetic angiograms; at the threshold of the patches, 82 percent of the windows of whole angiograms raise an alarm |
| 8 | [Heart team](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-08/lecture.html#the-virtual-clinic-stage-8-heart-team) | Early, late and hybrid fusion, stacking, attention over modality tokens with masks, the HEART score, the calibration intercept, slope and Brier score, bootstrap and Wilson intervals, recalibration at a second hospital, thresholds for discharge and net benefit | A chest pain unit with 4,000 presentations at hospital A and 1,000 at hospital B; on 800 test patients an AUC of 0.914 for early fusion against 0.883 for the troponin and 0.903 for HEART; at the threshold of the same share as HEART 0 to 3, 388 patients sent home with 9 major adverse cardiac events (MACE) against 380 with 8; at hospital B a calibration intercept of 0.62 before and 0.24 after the update with 300 local patients |
| 9 | [Quality and safety committee](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-09/lecture.html#the-virtual-clinic-stage-9-quality-and-safety-committee) | Exact Shapley values and their closed form for a logistic regression, global explanations, LIME and its stability, Grad-CAM against expert outlines with sanity checks over 20 random draws, a domain classifier for dataset shift, observed minus expected events with updates of the intercept, subgroups, fairness through unawareness and the legal frame of the KVKK, the MDR and the AI Act | The chest pain type leads the random forest for coronary artery disease in 56 of 76 test patients; the Grad-CAM maps of an echo network on CAMUS put 31.7 percent of their weight inside expert outlines that cover 21.3 percent of the image, and copies with a random last block reach a median of 27.5 percent; at hospital B the observed MACE leave their band at presentation 253; at a threshold of 98 percent sensitivity on validation, the sensitivity in the test women is 95.6 percent |
| 10 | [Decision support at the bedside](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-10/lecture.html#the-virtual-clinic-stage-10-decision-support-at-the-bedside) | Five numbers of every minute of RR intervals, among them the sample entropy, a logistic regression with a threshold chosen on validation records, alarm episodes and the AF burden, the contributions of an alarm next to its strip, model files with a version and a SHA-256 fingerprint, a model card, an HL7 FHIR report, a prediction service, a web interface in Streamlit, human oversight and a user test with a decision log | On the five test records of the MIT-BIH AFDB, version 1.0 reaches an AUC of 0.979 with a sensitivity of 0.949 and a specificity of 0.935; on the telemetry ward it raises 80 alarm episodes in 24 hours, 76 of them false, and version 1.1 with the sample entropy cuts them to 15, 11 of them false, while its test sensitivity falls to 0.924 |
| 11 | [The clinics of the participants](https://utkukose.github.io/ai-cardiology-tkd-NB-lecture/en/week-11/lecture.html#the-virtual-clinic-stage-11-the-clinics-of-the-participants) | A structured question, a data audit with the timing of the inputs, the sample sizes of Riley and colleagues, a reference model, bootstrap and Wilson intervals, calibration intercept and slope, a rule-out threshold chosen by cross-validation, subgroups, TRIPOD+AI, the stages of a clinical evaluation with DECIDE-AI and CONSORT-AI, the presentation and the personal action plan | On the Cleveland data, the worked final project reaches a test AUC of 0.931 [0.872, 0.977] against 0.900 for age, sex and chest pain type; the gain [−0.020, 0.094] includes zero, and at the rule-out threshold of 0.18 the model would spare 27 of 76 angiographies without missing a patient with disease, with a lower bound of the negative predictive value of 0.875 |

## Working with AI assistants

From the first week, participants write code together with an AI assistant, and the course treats this as a clinical skill with its own safety rules. Three tools support it. The **prompt card** states the task, the data format, the units, the sampling frequency and a test with a known answer, and it never describes the patient. The **code safety checklist** adapts the three pauses of the surgical safety checklist [1]: *sign in* before running the code, *time out* while it runs and *sign out* before its result is used. The **AI usage log** records the tool, the prompt, what was checked and what was changed, and it is part of every weekly project.

The **prompt path** turns these tools into a way of learning. Part 1 of every Jupyter notebook holds the steps of the practice stops. Each step has a ready prompt on the prompt card, a cell for the code of the assistant, a check against a known answer and ready code for participants who get stuck. [PROMPT_PATH.md](PROMPT_PATH.md) describes the path, the assistants that work with it and its rules of privacy.

Real patient data stay on the participant's own computer, under the rules of the institution and of the Turkish Law on the Protection of Personal Data (KVKK) [2]. They never enter a cloud notebook or an AI chat. All data sets of the course are synthetic or come from public research databases.

## With your own data

The course works with synthetic patients and public data, but its aim is the data of the participant's own clinic. Every lecture page ends with a section on applying the methods of the week to one's own data. [OWN_DATA.md](OWN_DATA.md) brings these sections together: which question fits which method, how the data leave the hospital systems, the approval of an ethics committee, the Turkish Law on the Protection of Personal Data (KVKK) and where to compute.

## Python for non-programmers

Part 2 of every Jupyter notebook is the Python path. It opens with a Python step that teaches the constructs of the week with examples from the clinic, and *Python note* cells explain each new construct where it first appears. Every exercise checks the answer at once. The [start-here notebook](en/start-here/NB00_start_here.ipynb) prepares the computer and the first lines of Python before Week 1, and [PYTHON_PATH.md](PYTHON_PATH.md) lists the Python steps of all weeks. Participants who do not want to write code follow the [prompt path](PROMPT_PATH.md), where the language is met by running and checking the code that an assistant writes for a well-described task.

## Assessment and certificate

| Component | Weight | Requirement for the certificate |
|---|---|---|
| Weekly projects (Weeks 1 to 10) | 40 percent | At least 70 percent in each project |
| Final project (presentation and code) | 40 percent | Evaluation by a jury and by the participants |
| Participation and active learning | 20 percent | Attendance of at least 80 percent |

Each weekly project is submitted by e-mail before the session of the following week. The e-mail holds the report written in the [report template](en/templates/Report_Template.docx), the AI usage log, the completed Jupyter notebook and the learning log exported from the interactive lab. The [final project page](en/final-project/README.md) describes the options, the requirements and the rubric of the final project.

## Running the materials

Every Jupyter notebook runs in two places, with the same data and the same results: in Google Colab, with nothing to install, and in Jupyter (Anaconda) on the participant's own computer. Participants choose the one they prefer. [SETUP.md](SETUP.md) explains both step by step. In Colab, the first cell of a notebook downloads the course package and the data files. Work with the data of real patients belongs only in Jupyter on a computer of the institution. The lecture pages and the interactive labs run in any modern browser, on a computer or a phone, without installation.

## Data

[DATASETS.md](DATASETS.md) lists every data set with its source, license and citation. Week 1 uses the Cleveland data of the UCI Heart Disease data set [3], record 100 of the MIT-BIH Arrhythmia Database [4, 5] and one record of the PTB Diagnostic ECG Database [6], published on PhysioNet [7]. These files are included in the [data](data) folder, so the notebooks run without registration.

## Reference integrity

Every source of the course is a published work with a digital object identifier (DOI) or a publisher page, and its details were checked against the publisher. The [references](references) folder holds the full list in APA 7 style, in BibTeX and in JSON. The script [tools/verify_references.py](tools/verify_references.py) compares every entry with Crossref, DataCite and OpenAlex. A GitHub Actions workflow runs it every month and whenever the references change.

## Citing this course

Kose, U. (2026). *Artificial Intelligence with Python: A Hands-on Training Program for Cardiologists: Open course materials* [Course materials]. GitHub. https://github.com/utkukose/ai-cardiology-tkd-NB-lecture

The file [CITATION.cff](CITATION.cff) holds the same information for reference managers.

## License

The content of the course (texts, figures, lecture pages, interactive labs and notes) is licensed under the [Creative Commons Attribution 4.0 International License](LICENSE-CONTENT) (CC BY 4.0). The code, including the package `vclinic` and the code in the Jupyter notebooks, is licensed under the [MIT License](LICENSE). The data sets keep their own licenses, listed in [DATASETS.md](DATASETS.md). The Three.js library embedded in the lecture pages and the interactive labs is distributed under the MIT License ([assets/vendor/LICENSE-three.txt](assets/vendor/LICENSE-three.txt)).

## References cited on this page

1. Haynes, A. B., Weiser, T. G., Berry, W. R., Lipsitz, S. R., Breizat, A.-H. S., Dellinger, E. P., Herbosa, T., Joseph, S., Kibatala, P. L., Lapitan, M. C. M., Merry, A. F., Moorthy, K., Reznick, R. K., Taylor, B., & Gawande, A. A. (2009). A surgical safety checklist to reduce morbidity and mortality in a global population. *New England Journal of Medicine, 360*(5), 491–499. https://doi.org/10.1056/NEJMsa0810119
2. Kişisel Verilerin Korunması Kanunu [Law on the Protection of Personal Data], Law No. 6698. (2016). *Resmî Gazete, 29677 (7 April 2016)*. https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=6698&MevzuatTur=1&MevzuatTertip=5
3. Janosi, A., Steinbrunn, W., Pfisterer, M., & Detrano, R. (1989). *Heart Disease* [Data set]. UCI Machine Learning Repository. https://doi.org/10.24432/C52P4X
4. Moody, G. B., & Mark, R. G. (2005). *MIT-BIH Arrhythmia Database (version 1.0.0)* [Data set]. PhysioNet. https://doi.org/10.13026/C2F305
5. Moody, G. B., & Mark, R. G. (2001). The impact of the MIT-BIH Arrhythmia Database. *IEEE Engineering in Medicine and Biology Magazine, 20*(3), 45–50. https://doi.org/10.1109/51.932724
6. Bousseljot, R., Kreiseler, D., & Schnabel, A. (2004). *The PTB Diagnostic ECG Database (version 1.0.0)* [Data set]. PhysioNet. https://doi.org/10.13026/C28C71
7. Goldberger, A. L., Amaral, L. A. N., Glass, L., Hausdorff, J. M., Ivanov, P. Ch., Mark, R. G., Mietus, J. E., Moody, G. B., Peng, C.-K., & Stanley, H. E. (2000). PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. *Circulation, 101*(23), e215–e220. https://doi.org/10.1161/01.CIR.101.23.e215

## Human-AI collaboration

This course was developed through human-AI collaboration. Human intellectual knowledge and expertise are the fundamental starting point of the course. The course author guides and supervises every stage of its development. The final version is presented only after the course author's review and approval.

---

<div align="center">

**Prof. Dr. Utku Kose**

Full Professor, Department of Computer Engineering, Süleyman Demirel University, Isparta, Türkiye<br>
Founding Director, AI Application and Research Center (YAZEM), Süleyman Demirel University<br>
Head of the Computer Science Division, Department of Computer Engineering, Süleyman Demirel University<br>
Additional affiliations: University of North Dakota (USA), Universidad Panamericana (Mexico City, Mexico), Vel Tech University (Chennai, India)<br>
IEEE Senior Member, ACM Professional Member

[ORCID 0000-0002-9652-6415](https://orcid.org/0000-0002-9652-6415) | [utkukose.com](https://www.utkukose.com) | [github.com/utkukose](https://github.com/utkukose)

[utkukose@sdu.edu.tr](mailto:utkukose@sdu.edu.tr) | [utku.kose@und.edu](mailto:utku.kose@und.edu) | [ukose@up.edu.mx](mailto:ukose@up.edu.mx) | [utkukose@gmail.com](mailto:utkukose@gmail.com)

*This course is updated in line with current developments in the field. First version: November 2026.*

</div>

## Acknowledgments

This training program was prepared for the Turkish Society of Cardiology (Türk Kardiyoloji Derneği). The author thanks the Society for the opportunity to offer it to cardiologists and other specialist physicians. The author also thanks the teams behind PhysioNet and the UCI Machine Learning Repository, whose open data make the hands-on work of the course possible.
