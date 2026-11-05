# Awesome Conformal Prediction

[![GitHub stars](https://img.shields.io/github/stars/valeman/awesome-conformal-prediction?style=social)](https://github.com/valeman/awesome-conformal-prediction)
[![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)
[![DOI](https://zenodo.org/badge/436989758.svg)](https://zenodo.org/badge/latestdoi/436989758)

A curated guide to **conformal prediction**, also known as conformal inference. Find tutorials, research papers, Python and R libraries, and runnable examples for prediction intervals, classification sets, time-series forecasting, anomaly detection, and LLM uncertainty. Curated by [Valery Manokhin, PhD][author].

Valery's resources lead each relevant section. The other entries prioritise editorial importance and recent work. 🔥 marks a reviewed core reference. 🕒 marks time-series resources.

**Explore the collection** · [Start here](#start-here) · [Python libraries](#conformal-prediction-libraries-in-python) · [Recent research](#recent-conformal-prediction-research) · [All topics](#table-of-contents)

<a name="learn-from-the-experts--book--course-by-dr-valeriy-manokhin"></a>

## Books and live course by Valery Manokhin

**[Apply for the live Applied Conformal Prediction course on Maven][maven-course]**. Work through regression, classification, forecasting, and LLM examples in Python. See the course page for cohort dates and updates. Explore [TinyCP](#conformal-prediction-libraries-in-python), an experimental Python library created by course alum Lucas Leão.

| | Book and editions |
| :---: | --- |
| <a href="https://www.amazon.com/dp/1809100607"><img src="docs/assets/applied-conformal-prediction-cover.jpg" alt="Applied Conformal Prediction book cover by Valery Manokhin" width="115"></a> | **Applied Conformal Prediction**<br>Build and evaluate prediction intervals and sets for real machine learning problems.<br>**[Amazon paperback][applied-paperback]** · **[Amazon hardcover][applied-hardcover]**<br>[Gumroad Core][applied-core] · [Gumroad Pro][applied-pro] |
| <a href="https://valeman.gumroad.com/l/intro_conformal_prediction"><img src="docs/assets/introduction-to-conformal-prediction-cover.png" alt="Introduction to Conformal Prediction book artwork by Valery Manokhin" width="155"></a> | **Introduction to Conformal Prediction**<br>Learn the finite-sample guarantees and implement the methods in Python.<br>Early access on Gumroad.<br>**[Gumroad Core][intro-core]** · **[Gumroad Pro][intro-pro]**<br>Amazon print listings forthcoming. |

<!-- Introduction to Conformal Prediction Amazon paperback: add verified direct product URL here. -->
<!-- Introduction to Conformal Prediction Amazon hardcover: add verified direct product URL here. -->

**[Author website][author]** · [Newsletter][newsletter] · [LinkedIn][linkedin] · [X][twitter]

---

<a name="-new-here-follow-this-path"></a>

## Start here

| If you want to… | Start with |
| --- | --- |
| Understand the guarantee | [What is conformal prediction?](#what-is-conformal-prediction) · [Browse tutorials](#conformal-prediction-tutorials) |
| Build your first prediction interval or set | [Python quickstart](#quickstart) and the [regression and classification notebook](docs/examples/quickstart.ipynb) |
| Choose a method or package | [Python](#conformal-prediction-libraries-in-python), [R](#conformal-prediction-libraries-in-r), and [Julia](#conformal-prediction-libraries-in-julia) |
| Work with a specific application | [Time series](#conformal-prediction-for-time-series-forecasting), [anomaly detection](#conformal-prediction-for-anomaly-detection), and [recent research](#recent-conformal-prediction-research) |

## Recent conformal prediction research

The papers below cover coverage diagnostics, LLM configuration changes, and applications in vision, healthcare, science, and robotics. See also the new entries in [forecasting](#conformal-prediction-for-time-series-forecasting), [anomaly detection](#conformal-prediction-for-anomaly-detection), and the [COPA proceedings](#conferences-featuring-conformal-prediction).

### Coverage diagnostics and risk control

- [Label-Free Distribution Shift Detection in Truck Mode Classification via Uncertainty-Gap Monitors](https://proceedings.mlr.press/v329/nurmatov26a.html) by Bek-Myrza Nurmatov, Valery Manokhin and Jens Heger (COPA 2026 extended abstract). Uses Venn–Abers interval widths to monitor shift in truck accelerometer data.
- [RSA-CP: Efficient Conformal Prediction in Small-Sample Regimes via Random Score Alignment](https://proceedings.mlr.press/v306/bhagwat26a.html) by Pankaj Bhagwat et al. (ICML 2026). Aligns real calibration scores with a reference score distribution to improve interval efficiency with small calibration sets.
- [SpeedCP: Fast Kernel-based Conditional Conformal Prediction](https://proceedings.mlr.press/v306/liu26bq.html) by Yating Liu et al. (ICML 2026). Computes a kernel conformal solution path to make conditional calibration under covariate shift more tractable.
- [Transfer Conformal Predictive Inference for Regression](https://www.jmlr.org/papers/v27/24-1899.html) by Ce Zhang et al. (JMLR 2026). Uses related source data to narrow conformal regression intervals when target data are scarce and analyzes coverage under source–target differences.
- [Provably Label-Efficient Conformal Prediction](https://proceedings.mlr.press/v306/ilyas26a.html) by Andrew Ilyas et al. (ICML 2026). Uses an online stopping rule to balance labelling cost and prediction-set size while preserving coverage.
- [Mask-Conditional Conformal Prediction: Valid Uncertainty For All Missing Data Mechanisms](https://proceedings.mlr.press/v300/fan26a.html) by Jiarong Fan et al. (AISTATS 2026). Combines imputation and weighted calibration to target coverage by missingness pattern.
- [Adaptive Coverage Policies in Conformal Prediction](https://proceedings.mlr.press/v300/gauthier26a.html) by Etienne Gauthier, Francis Bach and Michael I. Jordan (AISTATS 2026). Learns instance-dependent coverage levels using post-hoc conformal guarantees.
- [Conditional Coverage Diagnostics for Conformal Prediction](https://proceedings.mlr.press/v306/braun26c.html) by Sacha Braun et al. (ICML 2026). Uses a classification diagnostic to identify where prediction sets undercover. [Code](https://github.com/ElSacho/covmetrics)
- [Questioning the Coverage-Length Metric in Conformal Prediction: When Shorter Intervals Are Not Better](https://proceedings.mlr.press/v306/min26c.html) by Yizhou Min et al. (ICML 2026). Studies stability of prediction intervals alongside coverage and average length. [Code](https://github.com/benben-cd/PT-Conformal-Prediction)
- [Conformal Prediction with Corrupted Labels](https://proceedings.iclr.cc/paper_files/paper/2026/hash/3446f5683cee5e6a0484a3bd0706e8f0-Abstract-Conference.html) by Shai Feldman, Stephen Bates and Yaniv Romano (ICLR 2026). Studies calibration with noisy or missing labels using imputation and reweighting.
- [Conformal Risk Control for Non-Monotonic Losses](https://arxiv.org/abs/2602.20151) by Anastasios N. Angelopoulos (Phil. Trans. R. Soc. A, 2026). Treats nonmonotone losses and multiparameter tuning with stability-based guarantees. [Journal article](https://doi.org/10.1098/rsta.2025.0068)

### Conformal prediction for LLMs

- [Conformalized Large Language Models under Configuration Shift](https://aclanthology.org/2026.emnlp-main.786/) by Yuqicheng Zhu et al. (EMNLP 2026). Measures coverage after changes to prompt templates, decoding temperature, and weight quantization.
- [Auditing RAG Necessity: A Conformal Test for Source-Independent Answers](https://aclanthology.org/2026.emnlp-main.1820/) by Dongxin Guo et al. (EMNLP 2026). Uses counterfactual changes to retrieved context and split-conformal p-values to test whether an answer depends on the source.
- [Conformal Thinking: Risk Control for Reasoning on a Compute Budget](https://proceedings.mlr.press/v306/wang26hd.html) by Xi Wang et al. (ICML 2026). Calibrates when to stop model reasoning under a compute budget while controlling a specified error risk.
- [SCOPE: Selective Conformal Optimized Pairwise LLM Judging](https://proceedings.mlr.press/v306/badshah26a.html) by Sher Badshah et al. (ICML 2026). Uses both response orders to score pairwise LLM judgments and calibrates when to abstain under an exchangeability assumption.
- [Per-Step Conformal Calibration Does Not Transfer to Agent Trajectories](https://aclanthology.org/2026.emnlp-main.1808/) by Li Ning et al. (EMNLP 2026). Shows theoretically and in a web-navigation benchmark how per-step calibration can fail at trajectory level.
- [Conformal Certification of Reasoning Trace Prefixes](https://aclanthology.org/2026.emnlp-main.1776/) by Matt Y. Cheung et al. (EMNLP 2026). Calibrates a reasoning-prefix acceptance rule and controls the chance of retaining an annotated error under exchangeability.
- [CiteGuard: Conformal False-Discovery Control for Faithful Retrieval-Augmented Generation](https://proceedings.mlr.press/v306/jiang26f.html) by Xiangyu Jiang (ICML 2026). Uses conformal calibration to control false discoveries in retrieval-augmented answers.
- [CAS: Conformalized Agentic Search via Adaptive Retrieval and Policy Weighting](https://aclanthology.org/2026.emnlp-main.1054/) by Zixi Zhu et al. (EMNLP 2026). Uses conformal uncertainty for adaptive document retrieval and policy updates.
- [CoFact: Conformal Factuality Guarantees for Language Models under Covariate Shift](https://proceedings.iclr.cc/paper_files/paper/2026/hash/bd074b828bbd782d4bece89306caff84-Abstract-Conference.html) by Hu et al. (ICLR 2026). Studies how weighted calibration controls factuality risk under a shift in the prompt distribution.

### Computer vision, healthcare, science, and robotics

- [Probabilistic Object Detection with Conformal Prediction](https://proceedings.mlr.press/v329/ries26a.html) by Christopher Ries et al. (COPA 2026). Calibrates bounding-box coordinates and class sets on driving datasets. [Code](https://github.com/mos-ks/OD-CP)
- [CalPro: Prior-Aware Evidential Conformal Prediction with Structure-Aware Sensitivity Bounds for Protein Structures](https://proceedings.mlr.press/v306/shihab26b.html) by Ibne Farabi Shihab et al. (ICML 2026). Uses biological priors and split conformal calibration to quantify protein structure uncertainty and evaluates shifts across measurement settings.
- [Conformal Prediction Sets for Instance Segmentation](https://proceedings.mlr.press/v337/lu26b.html) by Kerri Lu et al. (UAI 2026). For a queried pixel, returns candidate instance masks and bounds the probability that none reaches a target overlap with the true mask.
- [What Can Conformal Risk Control Certify for PET/CT Tumour Segmentation?](https://proceedings.mlr.press/v329/zheng26a.html) by Weiyue Zheng and Surajit Ray (COPA 2026 extended abstract). Compares what risk-controlling segmentation sets can certify for missed lesions and voxel-level loss on autoPET cases.
- [Decision-Informed Online Conformal Prediction for ICU Resource Allocation](https://proceedings.mlr.press/v340/dronavajjala26a.html) by Chandra Dronavajjala (MLHC 2026). Uses downstream allocation decisions to reshape uncertainty margins and evaluates the result on three clinical datasets.
- [Guarantees That Survive a Missing Scan: Modality-Conditional Conformal Prediction for Multimodal Medical Diagnosis](https://papers.miccai.org/miccai-2026-sat/MLMI_024.html) by Aaron Ajit (MLMI at MICCAI 2026). Evaluates modality-specific calibration for diagnosis with missing inputs.
- [Improving the Sensitivity of Gravitational Wave Detection with Weighted Conformal Prediction](https://proceedings.mlr.press/v329/malz26a.html) by Ann-Kristin Malz, Gregory Ashton and Nicolo Colombo (COPA 2026). Evaluates likelihood-ratio weighting under shift on simulated data.
- [Particle-Based Conformal Prediction for Contact-Aware Uncertainty Calibration in Stratified Configuration Spaces](https://proceedings.mlr.press/v329/marques26a.html) by Marques, Popov and Berenson (COPA 2026). Calibrates predictions of future robot configurations in contact-rich simulations.

---

## Table of Contents

**Recent research and practical tools**

* [Recent research](#recent-conformal-prediction-research)
* [Python](#conformal-prediction-libraries-in-python) · [R](#conformal-prediction-libraries-in-r) · [Julia](#conformal-prediction-libraries-in-julia) · [Other languages](#conformal-prediction-in-other-languages)
* [AI platforms](#ai-platforms-using-conformal-prediction) · [Kaggle notebooks](#conformal-prediction-on-kaggle)
* [Time-series forecasting](#conformal-prediction-for-time-series-forecasting) · [Anomaly detection](#conformal-prediction-for-anomaly-detection)

**Learning and reference**

* [Tutorials](#conformal-prediction-tutorials) · [Courses](#conformal-prediction-courses) · [Books](#books-on-conformal-prediction) · [Articles](#articles-on-conformal-prediction)
* [Videos and talks](#conformal-prediction-videos-and-talks) · [Presentation slides](#conformal-prediction-presentation-slides)
* [Full paper catalogue](#conformal-prediction-papers) · [Theses](#phd-theses-on-conformal-prediction)

**Community**

* [Events and workshops](#conformal-prediction-events-and-workshops) · [Conferences](#conferences-featuring-conformal-prediction)
* [Researchers](#conformal-prediction-researchers) · [Websites](#conformal-prediction-websites)
* [About and citation](#about-this-list)

---

## What is Conformal Prediction?

Conformal prediction turns a model's outputs into **prediction intervals** for regression or **prediction sets** for classification. In split conformal prediction, fit the model on training data and use a separate calibration set to score its errors. The calibration scores determine a threshold for which candidate outcomes to include.

If the calibration and test examples are exchangeable, the standard split conformal construction gives finite-sample **marginal coverage** of at least the target level, such as 90%. Coverage is averaged over the calibration sample and a new test example. Coverage in particular subgroups or under distribution shift requires separate evaluation and, where applicable, a method with the appropriate assumptions. Interval width and set size measure how informative the outputs are.

## Quickstart

Use the [runnable notebook](docs/examples/quickstart.ipynb) for regression and classification with NumPy and scikit-learn. Install the [example requirements](docs/examples/requirements.txt) with `python -m pip install -r docs/examples/requirements.txt`.

The regression example fits a model, calibrates on held-out absolute residuals, and measures coverage and width on a third split. It uses synthetic data and runs without a dataset download.

```python
import numpy as np
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X, y = make_regression(n_samples=1500, n_features=6, noise=20, random_state=7)
X_train, X_rest, y_train, y_rest = train_test_split(X, y, test_size=0.4, random_state=7)
X_cal, X_test, y_cal, y_test = train_test_split(X_rest, y_rest, test_size=0.5, random_state=7)

model = LinearRegression().fit(X_train, y_train)
scores = np.abs(y_cal - model.predict(X_cal))
alpha = 0.1
rank = int(np.ceil((len(scores) + 1) * (1 - alpha)))
radius = np.partition(scores, rank - 1)[rank - 1] if rank <= len(scores) else np.inf

predictions = model.predict(X_test)
lower, upper = predictions - radius, predictions + radius
print(f"Test coverage: {np.mean((lower <= y_test) & (y_test <= upper)):.1%}")
print(f"Mean interval width: {np.mean(upper - lower):.2f}")
```

---

## 🛠 Open-Source Libraries and Tools

## Conformal Prediction Libraries in Python
1. [CSP Forecaster](https://github.com/valeman/csp-forecaster) by Valery Manokhin (2026). A Python implementation of Conformal Seasonal Pools for probabilistic time-series forecasting. [Preprint](https://arxiv.org/abs/2605.03789)
2. [Multi-class-probabilistic-classification using Venn-ABERS (Conformal) prediction](https://github.com/valeman/Multi-class-probabilistic-classification) by Valery Manokhin (Royal Holloway, 2022)
3. [PySloth - Python package for Probabilistic Prediction](https://github.com/PySloth/pysloth) by Valery Manokhin
4. [online-cp](https://pypi.org/project/online-cp/) by Johan Hallberg Szabadváry, Tuve Löfström and Rudy Matela. Online conformal prediction, predictive distributions and change-detection martingales. [COPA paper](https://proceedings.mlr.press/v266/hallberg-szabadvary25a.html)
5. [tsbootstrap](https://pypi.org/project/tsbootstrap/) by Sankalp Gilda. Dependent resampling with EnbPI and adaptive conformal calibrators. [2026 preprint](https://arxiv.org/abs/2607.06690) 🕒
6. [Puncc (Predictive uncertainty calibration and conformalization)](https://github.com/deel-ai/puncc) [paper](https://proceedings.mlr.press/v204/mendil23a/mendil23a.pdf) [slides](https://cml.rhul.ac.uk/copa2023/presentations/COPA_2023_mouhcine_mendil_puncc.pdf)
7. [venn-abers](https://github.com/ip200/venn-abers) by Ivan Petej (2024). Python calibration for binary and multiclass classifiers. [Foundational Venn–Abers paper](https://proceedings.mlr.press/r12/holloway14a.html) · [Multiclass extension by Valery Manokhin](https://proceedings.mlr.press/v60/manokhin17a.html)
8. [Conformal Predictions from Scratch in Numpy](https://github.com/joneswack/conformal-predictions-from-scratch) by Jones Wacker (2023)
9. [TorchCP - A library for conformal prediction](https://github.com/ml-stat-Sustech/TorchCP)
10. [Nixtla mlforecast](https://nixtlaverse.nixtla.io/mlforecast/) 🕒
11. [Nixtla statsforecast](https://nixtla.github.io/statsforecast/docs/tutorials/conformalprediction.html#introduction) 🕒
12. [nonconform](https://github.com/OliverHennhoefer/nonconform) by Oliver Hennhöfer. Python tools for conformal anomaly detection. [COPA 2026 paper](https://proceedings.mlr.press/v329/hennhofer26a.html)
13. [TinyCP](https://github.com/HeyLucasLeao/tinycp) by Lucas Leão. Experimental tools for binary classification and regression with optional random forest out-of-bag calibration. [PyPI](https://pypi.org/project/tinycp/)
14. [(F)FCP : Predictive Inference with (Fast) Feature Conformal Prediction](https://github.com/ElvisWang1111/F-F-CP)  (2026)
15. [ConformaSight Global Explainer Package](https://github.com/rabia174/ConformaSight) by Fatıma Rabia Yapıcıoğlu (2025)
16. [pearsonify - Lightweight Python package for generating classification intervals in binary classification tasks using Pearson residuals and conformal prediction](https://github.com/xRiskLab/pearsonify) (2025)
17. [HyperConformal: Conformal Prediction for Hyperdimensional Computing](https://github.com/danieleschmidt/HyperConformal)   (2025)
18. [confopt - A Library for Conformal Hyperparameter Tuning](https://github.com/rick12000/confopt) by Ricardo Doyle (2024) [paper](https://arxiv.org/abs/2207.03017)
19. [Conformal Tights - A scikit-learn meta-estimator that adds conformal prediction of coherent quantiles and intervals to any scikit-learn regressor](https://github.com/radix-ai/conformal-tights) by Laurent Sorber (Radix AI) (2024)
20. [Conformal Impact](https://github.com/tblume1992/ConformalImpact) by Tyler Blume (2024)
21. [conformal-prediction-jan2024 - PyLadies Amsterdam](https://github.com/pyladiesams/conformal-prediction-jan2024) by Inge van den Ende (2024)
22. [MFLES - Gradient Boosted Decomposition for time series forecasting](https://github.com/tblume1992/MFLES) by Tyler Blume (2024) 🕒
23. [calibrated-explanations - Calibrated Explanations for Machine Learning Models using Venn-Abers and Conformal Predictive Systems](https://github.com/Moffran/calibrated_explanations) by Helena Löfström (2023)
24. [Conformal Prediction for Digital Soil Mapping](https://github.com/nafisehkakhani/Conformal_Prediction_DSM) by Nafiseh Kakhani (2023)
25. [EnbPI](https://github.com/hamrel-cxu/EnbPI) by Chen Xu (2021) 🕒   [Paper](https://proceedings.mlr.press/v139/xu21h.html)
26. [Venn-ABERS Predictor](https://github.com/ptocca/VennABERS) by Paolo Toccaceli (2019) [Paper](https://proceedings.neurips.cc/paper/2015/hash/a9a1d5317a33ae8cef33961c34144f84-Abstract.html)
27. [Ensemble Conformalized Quantile Regression for Probabilistic Time Series Forecasting](https://github.com/FilippoMB/Ensemble-Conformalized-Quantile-Regression) Vilde Jensen, Filippo Maria Bianchi and Stian Norman Anfinsen (2022) 🕒
28. [Risk-controlling calibration (rrc)](https://github.com/Shai128/rrc) by Shai Feldman, Liran Ringel, Stephen Bates and Yaniv Romano. Code for the [published extension](https://openreview.net/forum?id=5Y04GWuoJu) of their online calibration work. 🕒
29. [NeuralProphet](https://neuralprophet.com/how-to-guides/feature-guides/uncertainty_quantification.html) (2022)
30. [River](https://github.com/online-ml/river/blob/0506ad73e45403638f13d66c6b2d71920d307461/river/conf/jackknife.py#L9) 2022
31. [TorchUQ](https://github.com/TorchUQ/torchuq/blob/5335c5948385c7b9bde4baefc9399d79a7cb07ef/docs/tutorials/1_c_1_conformal/1_c_1_conformal.rst#L17) (2022)
32. [Copula Conformal Multi Target Regression](https://github.com/M-Soundouss/CopulaConformalMTR) by Soundouss Messoudi (2021)
33. [Conformal time-series forecasting](https://github.com/kamilest/conformal-rnn) by Kamile ̇ Stankeviciute (Cambridge, NeurIPS 2021) 🕒
34. [Conformal learning from scratch](https://github.com/marharyta-aleksandrova/conformal-learning/blob/main/theory/conformal_learning_from_scratch.ipynb) by Marharyta Aleksandrova (2021)
35. [Conformalized Quantile Regression](https://github.com/yromano/cqr) by Yaniv Romano (2019)
36. [Conformalized density- and distance-based anomaly detection in time-series data (KNN-CAD)](https://github.com/numenta/NAB/tree/master/nab/detectors/knncad) by Evgeny Burnaev, Vladislav Ishimtsev (2016). Top #3 winning solution in Numenta competition
37. [Nonconformist](https://github.com/donlnz/nonconformist) by Henrik Linusson (2015)
38. [Orange3 Conformal Prediction](https://github.com/biolab/orange3-conformal)
39. [https://github.com/mikekeith52/scalecast](https://github.com/mikekeith52/scalecast) 🕒
40. [plot_utils - Plotting library for conformal prediction metrics, intended to facilitate fast testing in e.g. notebooks](https://github.com/pharmbio/plot_utils)
41. [Conformers - Unofficial Conformal Language Modelling library](https://github.com/Bradley-Butcher/Conformers/)
42. [crepes-weighted Extension of crepes package, to enable weighted conformal prediction and conformal predictive systems that can handle covariate shifts](https://github.com/predict-idlab/crepes-weighted)
43. [Conformal Prediction in KNIME](https://hub.knime.com/tuwelofstrom/spaces/Predicting%20with%20Confidence/latest/~h8R_oa6iPRTssrYs/) by Tuwe Löfström and Redfield AB (2022)

## Conformal Prediction Libraries in R
1. [probably for tidymodels](https://probably.tidymodels.org/reference/index.html). Split, full, CV+, and quantile conformal methods for regression. [Tutorial](https://www.tidymodels.org/learn/models/conformal-regression/index.html) · [Talk](https://www.youtube.com/watch?v=3omi4lm1da0)
2. [pintervals - Model agnostic prediction intervals](https://github.com/Doktorandahl/pintervals) [paper](https://arxiv.org/abs/2601.03994) by David Randahl, Anders Hjort, Jonathan P. Williams (2026)
3. [conformalForecast](https://github.com/xqnwang/conformalForecast) 🕒   (2024)
4. [AdaptiveConformal](https://github.com/herbps10/AdaptiveConformal) (2023) [paper](https://hal.science/hal-04316544/)
5. [Conformal prediction for 80+ classes of `R` models with the `marginaleffects` package](https://marginaleffects.com/chapters/uncertainty.html#conformal-prediction) by Vincent Arel-Bundock (2023)
6. [cfsurvival - An R package that implements the conformalized survival analysis methodology](https://zhimeir.github.io/cfsurvival/index.html) [Paper](https://arxiv.org/abs/2103.09763)
7. [ClusTorus: An R Package for Prediction and Clustering on the Torus by Conformal Prediction](https://journal.r-project.org/articles/RJ-2022-032/) by Seungki Hong and Sungkyu Jung (2022)
8. [conformalbayes - Jackknife(+) Predictive Intervals for Bayesian Models](https://github.com/CoryMcCartan/conformalbayes) (2022)
9. [Online Time Series Anomaly Detectors](https://github.com/alaineiturria/otsad) by Alaine Iturria, 2021
10. [conformal.fd Conformal inference prediction regions for Multiple Functional response regression](https://github.com/paolo-vergo/conformal.fd) (2021)
11. [Prediction Bands](https://github.com/rizbicki/predictionBands) by Rafael Izbicki and Benjamin LeRoy (2019)
12. [Conformal: an R package to calculate prediction errors in the conformal prediction framework](https://github.com/isidroc/conformal/) by Isidro Cortes, 2019
13. [piRF - Prediction Intervals for Random Forests](https://github.com/chancejohnstone/piRF) by Chancellor Johnstone and Haozhe Zhang (2019)
14. [conformal glm - conformal prediction for generalized linear regression models](https://github.com/DEck13/conformal.glm) by Daniel Eck (2019)
15. [Conformal Inference R Project](https://github.com/ryantibs/conformal) maintained by Ryan Tibshirani (2016)
16. [R Package for Spatial Conformal Prediction](https://github.com/mhuiying/scp)
17. [caretForecast - Conformal Time Series Forecasting Using State of Art Machine Learning Algorithms](https://github.com/Akai01/caretForecast)
18. [Localized Conformal Prediction - LCP](https://github.com/LeyingGuan/LCP)
19. cRepes-R, R implementation of Python crepes package - Conformal prediction for regression, classification, and predictive systems. Link unavailable.
20. [conformalClassification: Transductive and Inductive Conformal Predictions for Classification Problems](https://cran.r-project.org/package=conformalClassification) by Niharika Gauraha and Ola Spjuth (2019)
21. [Modeltime conformal prediction](https://business-science.github.io/modeltime/articles/modeltime-conformal-prediction.html). Worked R example for time-series forecast intervals.

## Conformal Prediction Libraries in Julia
1. [PostForecasts.jl](https://github.com/lipiecki/PostForecasts.jl) by Arkadiusz Lipiecki and Rafal Weron (2025) [paper](https://ideas.repec.org/p/ahh/wpaper/worms2502.html) [paper](https://www.sciencedirect.com/science/article/pii/S2352711025001670?via%3Dihub)
2. [ConformalPrediction.jl](https://github.com/pat-alt/ConformalPrediction.jl) by Patrick Altmeyer (2022) [Article - Conformal Prediction in Julia, Part I - Introduction](https://towardsdatascience.com/conformal-prediction-in-julia-351b81309e30) [Article - Conformal Prediction in Julia, Part II - How to conformalize a deep image classifier](https://towardsdatascience.com/how-to-conformalize-a-deep-image-classifier-14ead4e1a5a0) [Article -  Conformal Prediction in Julia, Part III - Prediction intervals for any regression model](https://towardsdatascience.com/prediction-intervals-for-any-regression-model-306930d5ad9a)
3. [RandomForest](https://github.com/henrikbostrom/RandomForest) by Henrik Boström (2017)

## Conformal Prediction in Other Languages
1. [Scala-CP](https://github.com/mcapuccini/scala-cp) by Marco Capuccini (2017)'  (see tutorial section 'Conformal Prediction in Spark')
2. [LibCP -- A Library for Conformal Prediction](https://github.com/fated/libcp)
3. [An Implementation of Venn-ABERS predictor](https://github.com/fated/venn-abers-predictor)
4. [LibVM -- A Library for Venn Machine](https://github.com/fated/libvm)

## AI Platforms Using Conformal Prediction
1. [AWS Fortuna](https://aws-fortuna.readthedocs.io/en/latest/) by Amazon, (2022)
2. [Conformal Prediction in Knime](https://proceedings.mlr.press/v179/lofstrom22a.html) [Presentation](https://cml.rhul.ac.uk/copa2022/presentations/tuwe_presentation.pdf)
3. [Data Robot - Prediction Intervals via Conformal Inference](https://docs.datarobot.com/en/docs/api/dev-learning/accelerators/adv-analytics-tools/pred-intervals-inf.html)
4. [Microsoft Azure](https://learn.microsoft.com/en-gb/archive/blogs/machinelearning/anomaly-detection-using-machine-learning-to-detect-abnormalities-in-time-series-data)

## Conformal Prediction on Kaggle
1. [Probabilistic Forecasting I starter notebook using StatsForecast and TBATS](https://www.kaggle.com/code/predaddict/pfi-starter-nixtla-statsforecast-tbats) by Valery Manokhin (2024).
2. [Kaggle Notebook showcasing Conformal Predictive Distributions on Playground Series Season 3, Episode 1 (California Housing data) competition](https://www.kaggle.com/code/predaddict/conformal-predictive-distributions-pss3-e1) by Valery Manokhin (2022)
3. [Kaggle Notebook showcasing Venn-ABERs Conformal Prediction on Playground Series Season 3, Episode 2 (Stroke prediction) competition](https://www.kaggle.com/predaddict/pss-3-episode-2-jan-2023-stroke-prediction/) by Valery Manokhin (2022)
4. CPB: The Crucial Calibration Set by L. Elaine Dazzio (2025). Link unavailable.
5. Simplest Conformal Prediction Example by L. Elaine Dazzio (2025). Link unavailable.
6. [Classifier calibration using Venn-ABERS](https://www.kaggle.com/code/carlmcbrideellis/classifier-calibration-using-venn-abers) by Carl McBride Ellis (2024)

---

## Conformal prediction applications

## Conformal Prediction for Time Series Forecasting
1. [Training-Free Probabilistic Time-Series Forecasting with Conformal Seasonal Pools](https://arxiv.org/abs/2605.03789) by Valery Manokhin (2026 manuscript). Uses seasonal draws and signed residuals for forecast distributions across horizons. [Code](https://github.com/valeman/csp-forecaster)
2. [Report the Floor: A Training-Free Conformal Interval Is a Mandatory Baseline for Probabilistic Time-Series Forecasting](https://arxiv.org/abs/2606.09473) by Valery Manokhin (2026 preprint). Evaluates a conformalized last-value baseline across 2,217 series for one-step forecasting.
3. [Conformal prediction interval for dynamic time-series](https://proceedings.mlr.press/v139/xu21h.html) by Chen Xu, Yao Xie (Georgia Tech, 2021) 🕒   [Python Code](https://github.com/hamrel-cxu/EnbPI) [Video](https://vimeo.com/583595474) [Video ICML2021](https://papertalk.org/papertalks/32044) 🔥
4. [Sequential Predictive Conformal Inference for Time Series](https://arxiv.org/abs/2212.03463) by Chen Xu, Yao Xie (Georgia Tech) [code](https://github.com/hamrel-cxu/SPCI-code/tree/main) 🕒
5. [Delving into Non-Exchangeability for Conformal Prediction in Graph-Structured Multivariate Time Series](https://proceedings.mlr.press/v306/guo26d.html) by Ruichao Guo et al. (ICML 2026). Uses graph wavelets to model cross-series dependence before conformal calibration.
6. [Efficient conformal prediction intervals for time series: Online PID-Expert aggregation](https://arxiv.org/abs/2610.02777) by Guodong Liu, Yanfei Kang, Ren Miao and Xiaoqian Wang (2026 preprint). Combines online PID calibrators using interval width and miscoverage feedback.
7. [Distribution-informed Online Conformal Prediction](https://proceedings.iclr.cc/paper_files/paper/2026/hash/5f8241131e6fd428aa49914da76b8ad0-Abstract-Conference.html) by Dongjian Hu et al. (ICLR 2026). Uses distribution information in online conformal prediction to reduce conservativeness while retaining a coverage analysis. 🕒 [Open preprint](https://arxiv.org/abs/2512.07770)
8. [Rigorous uncertainty quantification of probabilistic AI weather forecasts with conformal prediction](https://arxiv.org/abs/2606.19642) by Anna Asch et al. (2026 preprint). Studies conformal calibration of probabilistic AI weather forecasts and the distinction between ensemble spread and verified coverage. 🕒
9. [Adaptive Conformal Prediction for Full-Scale Plant pH Forecasting under Process Drift](https://proceedings.mlr.press/v329/lee26a.html) by Jongyeop Lee and Jong Min Lee (COPA 2026 extended abstract). Compares static, weighted and online conformal intervals for reactor pH forecasting across a wastewater plant under process drift. 🕒
10. [Conditional Quantile Adjusted Conformal Prediction for Time Series](https://proceedings.mlr.press/v306/yu26by.html) by Cheng Yu et al. (ICML 2026). Uses a monotone conditional quantile curve to stabilize sequential conformal intervals and gives an asymptotic result under dependence. 🕒
11. [DistMatch: Adaptive Binning via Distribution Matching for Robust Sequential Conformal Prediction](https://proceedings.mlr.press/v306/menadjiev26a.html) by Enver Menadjiev et al. (ICML 2026). Partitions forecast residuals by distributional similarity and updates quantiles online to adapt to changing series. 🕒
12. [Lightweight Online Multivariate Conformal Prediction](https://proceedings.mlr.press/v329/hourani26a.html) by Abd Al-Rahman Hourani et al. (COPA 2026). Adapts two-dimensional conformal regions online for vehicle trajectory forecasts and evaluates them on Renault driving data. 🕒
13. [Weighted Conformal Prediction for Lab-to-Track Thermal Transfer in EV Motorsport Powertrains](https://arxiv.org/abs/2607.02722) by Varshith Roy Kotla (2026 preprint). Documents loss of EnbPI coverage under measured battery drive-cycle shift and the limited recovery obtained with estimated density-ratio weights. 🕒
14. [Prequential Streaming Evaluation of Stateful Time-Series Forecasters with Online Conformal Calibration: A Diagnostic Atlas and the preqts Harness](https://zenodo.org/records/22825217) by Felipe Santibañez-Leal (2026 preprint). Benchmarks rolling coverage, width, forecast error, and computation. [Python package](https://pypi.org/project/preqts/)
15. [Conformal Prediction Algorithms for Time Series Forecasting: Methods and Benchmarking](https://arxiv.org/abs/2601.18509) by Andro Sabashvili (2026 preprint). Compares approaches to temporal dependence and online adaptation.
16. [Optimal training-conditional regret for online conformal prediction](https://arxiv.org/abs/2602.16537) by Jiadong Liang, Zhimei Ren, Yuxin Chen (University of Pennsylvania, 2026)
17. [Error-quantified Conformal Inference for Time Series](https://arxiv.org/abs/2502.00818) by Junxi Wu, Dongjian Hu, Yajie Bao, Shu-Tao Xia, Changliang Zou (Nankai University, Tsinghua University, China, 2025) 🕒  [code](https://github.com/creator-xi/Error-quantified-Conformal-Inference)
18. [Flow-based Conformal Prediction for Multi-dimensional Time Series](https://arxiv.org/abs/2502.05709) by Junghwan Lee, Chen Xu, Yao Xie (Georgia Tech, 2025) [code](https://github.com/Jayaos/flow_cp)
19. [Feature Fitted Online Conformal Prediction for Deep Time Series Forecasting Model](https://arxiv.org/abs/2505.08158) by Xiannan Huang, Shuhan Qiu (Tongji University, 2025) [code](https://github.com/xiannanhuang/FFDCI)
20. [Foundation models for time series forecasting: Application in conformal prediction](https://arxiv.org/abs/2507.08858) by Sami Achour, Yassine Bouher, Duong Nguyen, Nicolas Chesneau (Ekimetrics, Ecole Polytechnique, 2025) [code](https://github.com/ekimetrics/ts-genai-conformal)
21. [Error-quantified Conformal Inference for Time Series](https://openreview.net/pdf?id=RD9q5vEe1Q) [code](https://github.com/creator-xi/Error-quantified-Conformal-Inference) ICLR 2025 paper by Junxi Wu, Dongjian Hu, Yajie Bao,  Shu-Tao Xia, , Changliang Zou (Nankai University, Tsinghua University)
22. [Temporal Conformal Prediction (TCP): A Distribution-Free Statistical and Machine Learning Framework for Adaptive Risk Forecasting](https://arxiv.org/abs/2507.05470) by Agnideep Aich, Ashit Baran Aich, Dipak C. Jain (University of Louisiana at Lafayette,
Louisiana, USA; CEIBS, Shanghai, China) [code](https://arxiv.org/abs/2507.05470)
23. [Conformal Prediction for Hierarchical Data](https://arxiv.org/abs/2411.13479) by Guillaume Principato, Gilles Stoltz, Yvenn Amara-Ouali, Yannig Goude, Bachir Hamrouche, Jean-Michel Poggi (Université Paris-Saclay, EDF R&D, Inria, Laboratoire de mathématiques d’Orsay, France, 2025) [code](https://github.com/PrincipatoG/Conformal-Prediction-for-Hierarchical-Data) 🕒
24. [Relational Conformal Prediction for Correlated Time Series](https://arxiv.org/abs/2502.09443) by Andrea Cini, Alexander Jenkins, Danilo Mandic, Cesare Alippi, Filippo Maria Bianchi (2025) 🕒
25. [Dual-Splitting Conformal Prediction for Multi-Step Time Series Forecasting](https://arxiv.org/abs/2503.21251) by Qingdi Yu, Zhiwei Cao, Ruihang Wang, Zhen Yang, Lijun Deng, Min Hu, Yong Luo, Xin Zhou, (2025) 🕒
26. [STACI: Spatio-Temporal Aleatoric Conformal Inference](https://arxiv.org/abs/2505.21658) by Brandon R. Feng, David Keetae Park, Xihaier Luo, Arantxa Urdangarin, Shinjae Yoo, and Brian J. Reich (North Carolina State University, Brookhaven National Laboratory. 2025)
27. [Kernel-based Optimally Weighted Conformal Time-Series Prediction](https://openreview.net/forum?id=oP7arLOWix) by Jonghyeok Lee,  Chen Xu, Yao Xie (Georgia Tech, 2025).
28. [Predictive inference for time series: why is split conformal effective despite temporal dependence?](https://arxiv.org/abs/2510.02471) by Rina Foygel Barber, Ashwin Pananjady (University of Chicago, Georgia Tech, 2025)
29. [Relevance-Aware Thresholding in Online Conformal Prediction for Time Series](https://arxiv.org/abs/2510.02809) by Théo Dupuy, Binbin Xu, Stéphane Perrey, Jacky Montmain, Abdelhak Imoussaten (IMT Mines Ales, 2025)
30. [Enhanced Renewable Energy Forecasting using Context-Aware Conformal Prediction](https://arxiv.org/abs/2510.15780) by Alireza Moradi, Mathieu Tanneau, Reza Zandehshahvar, Pascal Van Hentenryck (Georgia Tech, 2025) 🕒
31. [Conformalized Time Series with Semantic Features](https://proceedings.neurips.cc/paper_files/paper/2024/file/dbfb7b1443583fc7ab87e8b1b4f48c9c-Paper-Conference.pdf) Baiting Chen, Zhimei Ren, Lu Cheng (UCLA, University of Pennsylvania, University of Illinois Chicago, 2025) 🕒
32. [Relevance-Aware Thresholding in Online Conformal Prediction for Time Series](https://arxiv.org/abs/2510.02809) by Théo Dupuy, Binbin Xu, Stéphane Perrey, Jacky Montmain, Abdelhak Imoussaten (IMT Mines Ales, France) 🕒
33. [Forecasting Melting Points in Svalbard, Norway Using Quantile Gradient Boosting and Adaptive Conformal Prediction Region](https://arxiv.org/abs/2510.23976) by
Richard Berk (University of Pennsylvania, 2025)
34. [Adaptive Regime-Switching Forecasts with Distribution-Free Uncertainty: Deep Switching State-Space Models Meet Conformal Prediction](https://arxiv.org/abs/2512.03298) by Echo Diyun LU, Charles Findling, Marianne Clausel, Alessandro Leite, Wei Gong, Pierric Kersaudy (University of Lorraine, Pernod Ricard, INSA Rouen Normandy, 2025) 🕒
35. [Flow-based Conformal Prediction for Multi-dimensional Time Series](https://arxiv.org/abs/2502.05709) by Junghwan Lee, Chen Xu, Yao Xie (Georgia Tech, 2025) 🕒
36. [Conformal Prediction for Time-series Forecasting with Change Points](https://arxiv.org/abs/2509.02844v4) by Sophia Sun, Rose Yu (University of California, San Diego, 2025) 🕒
37. [Online conformal inference for multi-step time series forecasting](https://arxiv.org/abs/2410.13115) by Xiaoqian Wang, Rob J Hyndman (Monash University, 2024) [Code](https://github.com/xqnwang/cpts) 🕒 [conformalForecast R package](https://github.com/xqnwang/conformalForecast)
38. [Distribution-Free Conformal Joint Prediction Regions for Neural Marked Temporal Point Processes](https://arxiv.org/abs/2401.04612) by Victor Dheur, Tanguy Bosser, Rafael Izbicki, Souhaib Ben Taieb (Universidade Federal de Sao Carlos, Brazil and University of Mons, Belgium, 2024) [code](https://github.com/tanguybosser/conf_tpp) 🕒
39. [Bellman Conformal Inference: Calibrating Prediction Intervals For Time Series](https://arxiv.org/abs/2402.05203) by Zitong Yang, Emmanuel Candès, Lihua Lei (Stanford, 2024)  🕒  [code](https://github.com/ZitongYang/bellman-conformal-inference)
40. [Conformal prediction for multi-dimensional time series by ellipsoidal sets](https://arxiv.org/abs/2403.03850) by Chen Xu, Hanyang Jiang, and Yao Xie (Georgia Tech, 2024) [code](https://github.com/hamrel-cxu/MultiDimSPCI) 🕒
41. [Transformer Conformal Prediction for Time Series](https://arxiv.org/abs/2406.05332) by Jonghyeok Lee, Chen Xu, Yao Xie (Georgia Tech, 2024) 🕒   [code](https://github.com/Jayaos/TCPTS)
42. [Conformal time series decomposition with component-wise exchangeability](https://arxiv.org/abs/2406.16766) by Derck W. E. Prinzhorn, Thijmen Nijdam, Putri A. van der Linden, Alexander Timans (University of Amsterdam, 2024) 🕒   [code](https://github.com/dweprinz/CP-TSD)
43. [Enhancing reliability in prediction intervals using point forecasters: Heteroscedastic Quantile Regression and Width-Adaptive Conformal Inference](https://arxiv.org/abs/2406.14904) Carlos Sebastiana,Carlos E. Gonzalez-Guillenc, Jesus Juane (Fortia Energıa, Universidad Politecnica de Madrid, Instituto de Ciencias Matematicas, Madrid) [code](https://github.com/CCaribe9/HQR-WACI) (2024) 🕒
44. [Split Conformal Prediction and Non-Exchangeable Data](https://www.jmlr.org/papers/v25/23-1553.html) by Roberto I. Oliveira, Paulo Orenstein, Thiago Ramos, João Vitor Romano (IMPA, Brazil, 2024) [code](https://github.com/jv-rv/split-conformal-nonexchangeable)
45. [Neural Conformal Control for Time Series Forecasting](https://arxiv.org/abs/2412.18144) by Ruipu Li, Alexander Rodrıguez (University of Michigan, 2024) [code](https://github.com/complex-ai-lab/ncc) 🕒
46. [Split Conformal Prediction and Non-Exchangeable Data](https://jmlr.org/papers/v25/23-1553.html) by Roberto I. Oliveira, Paulo Orenstein, Thiago Ramos, João Vitor Romano (IMPA, Rio de Janeiro, Brazil, 2024) [code](https://github.com/jv-rv/split-conformal-nonexchangeable)
47. [Conformal Prediction for Hierarchical Data](https://arxiv.org/abs/2411.13479) by Guillaume Principato, Gilles Stoltz, Yvenn Amara-Ouali, Yannig Goude, Bachir Hamrouche, Jean-Michel Poggi (EDF R&D, Universit´e Paris-Saclay, CNRS, Inria, Laboratoire de math´ ematiques d’Orsay,Universit´e Paris Cit´e, France [code](https://github.com/PrincipatoG/Conformal-Prediction-for-Hierarchical-Data)
48. [Conformalized predictive simulations for univariate time series](https://www.researchgate.net/publication/379643443_Conformalized_predictive_simulations_for_univariate_time_series) by Thierry Moudiki (2024)
49. [Kernel-based optimally weighted conformal prediction intervals](https://arxiv.org/abs/2405.16828) by Jonghyeok Lee, Chen Xu, Yao Xie (Georgia Tech, 2024) 🕒
50. [Conformal prediction for multi-dimensional time series by ellipsoidal sets](https://openreview.net/forum?id=uN39Tt9P8b) by Chen Xu, Hanyang Jiang, Yao Xie (Georgia Tech, 2024) 🕒
51. [ConForME: Multi-horizon conformal time series forecasting](https://raw.githubusercontent.com/mlresearch/v230/main/assets/galvao-lopes24a/galvao-lopes24a.pdf) by Aloysio Galvao Lopes, Eric Goubault, Sylvie Putot, Laurent Pautet (Institut Polytechnique de Paris, LTCI, Telecom Paris, 2024) 🕒
52. [Conformal Prediction for Hierarchical Data](https://arxiv.org/abs/2411.13479) by Guillaume Principato, Yvenn Amara-Ouali, Yannig Goudee, Bachir Hamrouche, Jean-Michel Poggi, Gilles Stolz (EDF R&D, Laboratoire de mathe ́matiques d’Orsay, INRIA, France)
53. [Adaptive Conformal Inference by Betting](https://arxiv.org/abs/2412.19318) by Aleksandr Podkopaev, Darren Xu, Kuang-chih Lee (Wallmart Global Tech, 2024) 🕒
54. [Conformalized Time Series with Semantic Features](https://proceedings.neurips.cc/paper_files/paper/2024/hash/dbfb7b1443583fc7ab87e8b1b4f48c9c-Abstract-Conference.html) by Baiting Chen, Zhimei Ren, Lu Cheng (2024) 🕒
55. [Conformalized Time Series with Semantic Features](https://proceedings.neurips.cc/paper_files/paper/2024/hash/dbfb7b1443583fc7ab87e8b1b4f48c9c-Abstract-Conference.html) by Baiting Chen, Zhimei Ren, Lu Cheng (2024) 🕒
56. [Improved Online Conformal Prediction via Strongly Adaptive Online Learning](https://arxiv.org/abs/2302.07869) by Aadyot Bhatnagar, Huan Wang, Caiming Xiong, Yu Bai (2023) [code](https://github.com/salesforce/online_conformal) 🕒
57. [Conformal Prediction for Time Series with Modern Hopfield Networks](https://arxiv.org/pdf/2303.12783.pdf) by Andreas Auer, Martin Gauch, Daniel Klotz, Sepp Hochreiter (Johannes Kepler University, Linz, 2023) [code](https://github.com/ml-jku/HopCPT) [blogpost](https://ml-jku.github.io/HopCPT/)  🕒
58. [Conformal Predictions for longitudinal data](https://arxiv.org/pdf/2310.02863.pdf) by Devesh Batra, Salvatore Mercuri and Raad Khraishi (Data Science & Innovation - NatWest Group, Institute of Finance and Technology, UCL, UK, 2023) 🕒   [code](https://github.com/EconAIorg/LPCI)
59. [Conformal PID Control for Time Series Prediction](https://arxiv.org/abs/2307.16895) by Anastasios N. Angelopoulos, Emmanuel J. Candes, Ryan J. Tibshirani (Berkeley/Stanford, NeurIPS2023) [code](https://github.com/aangelopoulos/conformal-time-series) 🕒
60. [Conformal prediction set for time-series](https://arxiv.org/abs/2206.07851) by Chen Xu, Yao Xie (Georgia Tech, 2022) [Python Code](https://github.com/hamrel-cxu/Ensemble-Regularized-Adaptive-Prediction-Set-ERAPS) 🕒
61. [Conformalized Online Learning: Online Calibration Without a Holdout Set](https://arxiv.org/abs/2205.09095v1) by Shai Feldman, Stephen Bates and Yaniv Romano (2022 preprint). 🕒  [Published extension](https://openreview.net/forum?id=5Y04GWuoJu)
62. [CODiT: Conformal Out-of-Distribution Detection in Time- Series Data](https://arxiv.org/pdf/2207.11769.pdf) by Ramneet Kaur et.al., Unibersity of Pensylvania (2022). [Code](https://github.com/kaustubhsridhar/time-series-OOD) 🕒
63. [A General Framework For Multi-step Ahead Adaptive Conformal Heteroscedastic Time Series Forecasting](https://www.sciencedirect.com/science/article/pii/S0925231224012050/pdfft?md5=2f884ccf3a69148127232428fbf2042a&pid=1-s2.0-S0925231224012050-main.pdf) by Martim Sousa, Ana Maria Tomé, University of Aveiro (2022) [Code](https://github.com/Quilograma/AdaptiveEnbMIMOCQR) 🕒
64. [Copula Conformal Prediction for Multi-step Time Series Forecasting](https://openreview.net/pdf?id=jCdoLxMZxf) by Sophia Sun, Rose Yu (University of California, San Diego, 2022) [code](https://github.com/Rose-STL-Lab/CopulaCPTS) 🕒
65. [Conformal Time-Series Forecasting](https://proceedings.neurips.cc/paper/2021/file/312f1ba2a72318edaaa995a67835fad5-Paper.pdf) by Kamile  Stankeviciu te and Ahmed M. Alaa (2021) [Video NeurIPS2021](https://papertalk.org/papertalks/36577) [Video](https://www.youtube.com/watch?v=xmPDk4QRAAI) 🕒
66. [Ensemble Conformalized Quantile Regression for Probabilistic Time Series Forecasting](https://arxiv.org/pdf/2202.08756.pdf) by Vilde Jensen, Filippo Maria Bianchi, Stian Norman Anfinsen (2022). 🕒
67. [Conformal Prediction with Temporal Quantile Adjustments](https://arxiv.org/pdf/2205.09940.pdf) by Zhen Lin, Shubhendu Trivedi, Jimeng Sun (2022)  🕒
68. [Robust Gas Demand Forecasting With Conformal Prediction](https://proceedings.mlr.press/v179/mendil22a.html) by Mouhcine Mendil, Luca Mossina, Marc Nabhan, Kevin Pasini (2022)
69. [Conformal Prediction Interval Estimations with an Application to Day-Ahead and Intraday Power Markets](https://arxiv.org/pdf/1905.07886.pdf) by Christopher Kath and Florian Ziel (2020)
70. [Amazon Fortuna](https://aws-fortuna.readthedocs.io/en/latest/examples/enbpi_ts_regression.html)

## Conformal Prediction for Anomaly Detection

1. [How to Detect Anomalies with Conformal Prediction](https://valeman.medium.com/how-to-detect-anomalies-state-of-the-art-methods-using-conformal-prediction-e02691659412) by Valery Manokhin (2021).
2. [Testing For Distribution Shifts with Conditional Conformal Test Martingales](https://proceedings.mlr.press/v306/shaer26a.html) by Shalev Shaer, Yarin Bar, Drew Prinster and Yaniv Romano (ICML 2026). Uses a fixed reference set to avoid contamination after a shift, with anytime-valid false-alarm control.
3. [Optimal distribution-free sequential change detection with conformal martingales](https://arxiv.org/abs/2609.27179) by Swapnaneel Bhattacharyya and Aaditya Ramdas (2026 preprint). Analyses detection delays of standard martingales and derives asymptotically optimal alternatives under stated conditions.
4. [Exploring the Link Between Out-of-Distribution Detection and Conformal Prediction with Illustrations of Its Benefits](https://proceedings.mlr.press/v329/novello26a.html) by Paul Novello et al. (COPA 2026). Develops conformal corrections for out-of-distribution benchmark metrics and tests OOD scores in conformal prediction sets.
5. [Distribution-free inference on the number of changepoints](https://arxiv.org/abs/2609.08234) by Rohan Hore and Aaditya Ramdas (2026 preprint). Uses conformal p-values to bound the number of changepoints from below when segments are exchangeable within themselves and mutually independent.
6. [Conformal Prediction for Multi-Source Detection on a Network](https://arxiv.org/abs/2511.08867) by Xingchao Jian et al. (2025 preprint). Uses conformal inference to quantify uncertainty when identifying multiple diffusion sources from a network snapshot.
7. [Conformal C2ST: Turning weak classifiers into strong two-sample tests](https://proceedings.mlr.press/v306/bansal26a.html) by Vansh Bansal et al. (ICML 2026). Turns classifier scores into finite-sample two-sample tests and studies how classifier quality affects test power.
8. [Detecting Adversarial Attacks in Image Sequences with Conformal Test Martingales](https://proceedings.mlr.press/v329/dong26a.html) by Genghua Dong et al. (COPA 2026). Evaluates conformal test martingales for detecting white-box adversarial attacks in ImageNet-100 sequences.
9. [Finite-Sample-Corrected Conformal Test Martingales for Wireless Link Adaptation](https://proceedings.mlr.press/v329/wu26a.html) by Peixuan Wu et al. (COPA 2026 extended abstract). Corrects a conformal test martingale for finite calibration and illustrates the resulting monitoring rule in a simulated wireless replay.
10. [Predictive Conformal Slip Monitoring: An Empirical Evaluation of Rolling Split Conformal Prediction for Pre-Incident Traction Loss Detection](https://arxiv.org/abs/2607.02124) by Varshith Roy Kotla (2026 preprint). Reports a negative result for a rolling conformal traction-loss alarm against timestamped racing incidents and a static threshold baseline.
11. [Distribution-Free Process Monitoring with Conformal Prediction](https://arxiv.org/abs/2512.23602) by Christopher Burger (2025 preprint). Applies conformal calibration to statistical process-control charts for manufacturing monitoring.
12. [Multivariate Change-Point Detection Using Feature-Based Inductive Conformal Martingales](https://proceedings.mlr.press/v329/eliades26a.html) by Charalambos Eliades and Harris Papadopoulos (COPA 2026). Tests a distance-based conformal martingale on multivariate streams.
13. [Detecting Label Shift for Large Language Models with Conformal Test Martingales](https://proceedings.mlr.press/v329/bostrom26b.html) by Henrik Boström (COPA 2026). Uses sequential testing to detect label shift in LLM classification.
14. [Conformal prediction for trustworthy detection of railway signals](https://link.springer.com/article/10.1007/s43681-023-00400-7) by Léo Andéol, Thomas Fel, Flornce de Grancey, Luca Mossina (Institut de Mathématiques de Toulouse, SNCF,Brown University,Thales, AVS France, IRT Saint Exupéry, Toulouse; France/USA 2024)
15. [Detecting Railway Track Irregularities Using Conformal Prediction](https://tik-old.ee.ethz.ch/db/public/tik/?db=publications&form=report_single_publication&publication_id=5176) by Andreas Plesner, Allan P. Engsig-Karup, Hans True (ETH Zurich, Technical University of Denmark) (2024)
16. [CoPAL: Conformal Prediction in Active Learning An Algorithm for Enhancing Remaining Useful Life Estimation in Predictive Maintenance](https://proceedings.mlr.press/v230/kharazian24a.html) by Zahra Kharazian, Tony Lindgren, Sindri Magnusson, Henrik Boström (Stockholm University, KTH, 2024)
17. [Testing Exchangeability On-Line](https://aaai.org/papers/icml03-100-testing-exchangeability-on-line/) by Vladimir Vovk, Ilia Nouretdinov, Alex Gammerman (Royal Holloway, UK, 2023)
18. [Conformalized density- and distance-based anomaly detection in time-series data](https://arxiv.org/abs/1608.04585) by Evgeny Burnaev, Vladislav Ishimtsev (Skoprech 2016) one of top methods in high profile Numenta Anomaly Detection competition [code](https://github.com/numenta/NAB/tree/master/nab/detectors/knncad) 🕒
19. [Inductive conformal anomaly detection for sequential detection of anomalous sub-trajectories](https://www.researchgate.net/publication/258244052_Inductive_conformal_anomaly_detection_for_sequential_detection_of_anomalous_sub-trajectories) by Rikkard Laxhammar nd Goran Falkman (2013)
20. [Plug-in martingales for testing exchangeability on-line](https://icml.cc/2012/papers/808.pdf) by Valentina Fedorova, Alex Gammerman, Ilia Nouretdinov, Vladimir (Vovk Royal Holloway, UK, 2012)
21. [Conformal Anomaly Detection](https://www.diva-portal.org/smash/get/diva2:690997/FULLTEXT02.pdf) PhD dissertation by Rikkard Laxhammar (University of Skovde, 2012)
22. [Microsoft Azure](https://learn.microsoft.com/en-gb/archive/blogs/machinelearning/anomaly-detection-using-machine-learning-to-detect-abnormalities-in-time-series-data) Microsoft Azure Anomaly Detection powered by Conformal Prediction

---

<a name="-start-here--learn-conformal-prediction"></a>

## Learn Conformal Prediction

## Conformal Prediction Tutorials

1. [How to use full (transductive) conformal prediction](https://valeman.medium.com/how-to-use-full-transductive-conformal-prediction-7ed54dc6b72b) by Valery Manokhin (2023).
2. [A Tutorial on Conformal Prediction](https://jmlr.org/papers/v9/shafer08a.html) by Glenn Shafer and Vladimir Vovk (2008) 🔥
3. [Conformal Predictions from Scratch in Numpy](https://github.com/joneswack/conformal-predictions-from-scratch) by Jones Wacker (2023)
4. [Conformal Prediction: A Visual Introduction](https://github.com/agarwal-mihir/Conformal-Prediction) (source code) from [VISxAI 2023](https://visxai.io/2023) by Mihir Agarwal, Lalit Chandra Routhu, Zeel B Patel and Nipun Batra (IIT Gandhinagar, IIT Patna, 2023)
5. [Conformal Prediction in R](https://github.com/adhjort/ConformalPredictionTutorial) by Anders Hjort. Workshop code for split conformal prediction, normalized scores, and groupwise calibration.
6. [Mini-tutorial on Conformal Prediction](https://www.cmap.polytechnique.fr/~aymeric.dieuleveut/talks.html) by Aymeric Dieuleveut (SIAM UQ 2026). Slides are linked from the author’s talks page.
7. [A Tutorial on Distribution-Free Uncertainty Quantification Using Conformal Prediction (psychology)](https://journals.sagepub.com/doi/10.1177/25152459251380452) by Tim Kaiser and Philipp Herzog (Freie Universität Berlin, RPTU University Kaiserslautern-Landau, Germany, 2025).
8. [Conformal Prediction in Genomics](https://github.com/BiolApps/ConformalPrediction/tree/main) by BiolApps (2023)
9. [Uncertainty Quantification (1): Enter Conformal Predictors](https://www.youtube.com/watch?v=xZbuFKWV5NA&t=25s) by Mahdi Torabi Rad (2023)
10. [Uncertainty Quantification (2): Full Conformal Predictors](https://www.youtube.com/watch?v=R1dnPAYGwnk) by Mahdi Torabi Rad (2023)
11. [Uncertainty Quantification (3): From Full to Split Conformal Methods](https://www.youtube.com/watch?v=YigGJfsCjDk) by Mahdi Torabi Rad (2023)
12. [Distribution-free inference tutorial At the IFDS 2021 Summer School](https://rinafb.github.io/talks/) [Video 1](https://vimeo.com/581870072) [Video 2](https://vimeo.com/581870078)
13. [Uncertainty estimation in NLP](https://sites.google.com/view/uncertainty-nlp#h.is5zc8lcnuki) by Tal Schuster, Adam Fisch (MIT, USC, 2022)
14. [Conformal Prediction Tutorial](https://www.youtube.com/watch?v=0MsGri8nmJQ) by Henrik Linusson (2021)
15. [Venn Predictors Tutorial](https://www.youtube.com/watch?v=KsQpkjl7u1w) by Ulf Johansson, Cecilia Sönströd, Tuve Löfström, and Henrik Boström (2021)
16. [Henrik Linusson: Conformal Prediction](https://www.youtube.com/watch?v=lQxH-zXrOwI&t=1522s) by Henrik Linusson (2020)
17. [A Tutorial on Conformal Predictive Distributions](https://www.youtube.com/watch?v=FUi5jklGvvo&t=3s) by Paolo Toccaceli (2020)
18. [Ulf Johansson: Venn Predictors](https://www.youtube.com/watch?v=xxZOLo8wxe0&t=98s) by Ulf Johansson (2020)
19. Conformal Inference Tutorial by Ben Kompa (2020). Link unavailable.
20. [Tutorial on Venn-ABERS prediction](https://cml.rhul.ac.uk/people/ptocca/HomePage/Toccaceli_CP___Venn_Tutorial.pdf) by Paolo Toccaceli (Royal Holloway, UK, 2019)
21. [Conformal Prediction and Venn Predictors A Tutorial on Predicting with Confidence](https://icdatascience.org/wp-content/uploads/2019/07/ICDATA_tutorial_2019_Johansson_U.pdf) by Ulf Johansson, Henrik Linusson, Tuve Löfström, Henrik Boström, Alex Gammerman (2019)
22. [An Introduction to Conformal Prediction](https://cml.rhul.ac.uk/copa2017/presentations/CP_Tutorial_2017.pdf) by Henrik Linusson (2017)
23. [Conformal Prediction in Spark](https://docs.google.com/presentation/d/1eD1vUJVR3nejyJZsOMfxL-NxrLy7K2UUMSAEMHYLfek/edit#slide=id.g2276269343_0_129) by Marco Capuccini (Uppsala University, 2017)
24. [Predicting with Confidence - Henrik Boström](https://www.youtube.com/watch?v=eXU-64dwHmA) by Henrik Boström (2016)
25. [Introduction to Conformal Prediction](https://www.iith.ac.in/~vineethnb/indoukworkshop2015/assets/files/IntroToCP.pdf) by Vineeth N Balasubramanian (Indian Institue of Technology, Hyderabad, 2015)
26. [Conformal prediction A Tiny Tutorial on Predicting with Confidence](https://people.dsv.su.se/~henke/DSWS/johansson.pdf) by Henrik Linusson and Ulf Johansson (2014)

## Conformal Prediction Courses
1. [Applied Conformal Prediction on Maven][maven-course] by Valery Manokhin (paid live course). See Maven for the next cohort and course updates.
2. [Uncertain: Modern topics in uncertainty estimation](https://uncertaintyclass.com/lectures/) [YouTube](https://www.youtube.com/watch?app=desktop&v=M3tkM4dcIPA) [Course notes](https://www.cis.upenn.edu/~aaroth/uncertainty-notes.pdf) by Aaron Roth (University of Pennsylvania, 2022)
3. [Conformal Prediction - Advanced Topics in Statistical Learning, Spring 2023](https://www.stat.berkeley.edu/~ryantibs/statlearn-s23/lectures/conformal.pdf) by Ryan Tibshirani (2023)
4. [Conformal Methods for Efficient and Reliable Deep Learning](https://dspace.mit.edu/handle/1721.1/152788) by Adam, Fisch (MIT, 2023)
5. [Topics in Modern Statistical Learning](https://github.com/dobriban/Topics-In-Modern-Statistical-Learning) by Edgar Dobriban (Wharton School, University of Pennsylvania, 2022)
6. [Theory of Statistics](https://candes.su.domains/teaching/stats300c/) Stanford Statistics course by Prof Emmanuel Candes (2022)
7. [36-708 Statistical Methods for Machine Learning](https://www.stat.cmu.edu/~larry/=sml/) Carnegie-Mellon course by Prof Larry Wasserman (2022)

## Books on Conformal Prediction
1. **Applied Conformal Prediction** by Valery Manokhin (paid). [Amazon paperback][applied-paperback] · [Amazon hardcover][applied-hardcover] · [Gumroad Core][applied-core] · [Gumroad Pro][applied-pro].
2. **Introduction to Conformal Prediction** by Valery Manokhin (paid). [Gumroad Core][intro-core] · [Gumroad Pro][intro-pro]. Amazon print listings forthcoming.
3. [Algorithmic Learning in a Random World](https://link.springer.com/book/10.1007/978-3-031-06649-8) by Vladimir Vovk, Alex Gammerman, and Glenn Shafer (2022, Second edition).  Great theory-based book, very math heavy, no applications, no code. 🔥
4. [Theoretical Foundations of Conformal Prediction](https://arxiv.org/abs/2411.11824) by Anastasios N. Angelopoulos, Rina Foygel Barber and Stephen Bates. Open manuscript with proofs and statistical foundations. [Publisher](https://www.cambridge.org/core/books/theoretical-foundations-of-conformal-prediction/E7467F79253078E47AAA916A3BE245C6)
5. [Conformal Prediction for Reliable Machine Learning](https://www.elsevier.com/books/conformal-prediction-for-reliable-machine-learning/balasubramanian/978-0-12-398537-8) by Vineeth Balasubramanian, Shen-Shyang Ho, Vladimir Vovk (2014). Older book, largely out of date, no code.

## Articles on Conformal Prediction
1. [How to use full (transductive) Conformal Prediction](https://valeman.medium.com/how-to-use-full-transductive-conformal-prediction-7ed54dc6b72b) by Valery Manokhin (2023)
2. [Jackknife+ — a Swiss knife of Conformal Prediction for regression](https://medium.com/@valeman/jackknife-a-swiss-knife-of-conformal-prediction-for-regression-ce3b56432f4f) by Valery Manokhin (2023)
3. [How to calibrate your classifier in an intelligent way](https://medium.com/@valeman/how-to-calibrate-your-classifier-in-an-intelligent-way-a996a2faf718) by Valery Manokhin (2022)
4. [How to predict full probability distribution using machine learning Conformal Predictive Distributions](https://medium.com/@valeman/how-to-predict-full-probability-distribution-using-machine-learning-conformal-predictive-f8f4d805e420) by Valery Manokhin (2022)
5. [How to predict quantiles in a more intelligent way (or ‘Bye-bye quantile regression, hello Conformal Quantile Regression](https://valeman.medium.com/how-to-predict-quantiles-in-a-more-intelligent-way-or-bye-bye-quantile-regression-hello-24a65e4c50f) by Valery Manokhin (2022)
6. [Probabilistic Forecasting with Conformal Prediction and NeuralProphet](https://medium.com/@valeman/probabilistic-forecasting-with-conformal-prediction-and-neuralprophet-af9c87901d94) by Valery Manokhin (2022) 🕒
7. [How to Detect Anomalies — state-of-the-art methods using Conformal Prediction](https://valeman.medium.com/how-to-detect-anomalies-state-of-the-art-methods-using-conformal-prediction-e02691659412) by Valery Manokhin (2021)
8. [Multi-horizon Probabilistic Forecasting with Conformal Prediction and NeuralProphet](https://valeman.medium.com/multi-horizon-probabilistic-forecasting-with-conformal-prediction-and-neuralprophet-5ec5af3888c8) by Valery Manokhin 🕒
9. [Leveraging conformal prediction in Python to accelerate the renewable energy transition](https://medium.com/@icvandenende/leveraging-conformal-prediction-in-python-to-accelerate-the-renewable-energy-transition-09b5c855f69d) by Inge van den Ende (2025)
10. [Conformalized quantile regression](https://mlwithouttears.com/2024/01/17/conformalized-quantile-regression/) by Lorenzo Maggi (2024)
11. [Leveraging conformal prediction in Python to accelerate the renewable energy transition](https://medium.com/@icvandenende/leveraging-conformal-prediction-in-python-to-accelerate-the-renewable-energy-transition-09b5c855f69d) by Inge van den Ende (2024)
12. [Fifty (four, actually) shades of conformal prediction](https://mlwithouttears.com/2024/02/04/fifty-four-actually-shades-of-conformal-prediction/) by Lorenzo Maggi (2024)
13. [Use case adapted prediction intervals by means of conformal predictions and a custom non conformity score](https://medium.com/@arnaud.gc.capitaine/use-case-adapted-prediction-intervals-by-means-of-conformal-predictions-and-a-custom-non-conformity-b4fb28d2a4f7) by Arnaud Capitaine (2024)
14. [Prediction Intervals using Conformalized Quantile Regression](https://vincentwtrs.github.io/2024-03-06-conformal_prediction_prediction_intervals/) by Vincent Wauters (2024).
15. [Conformalized Quantile Regression for Time Series Probabilistic Forecasting](https://dataman-ai.medium.com/conformalized-quantile-regression-for-time-series-probabilistic-forecasting-85a2a1047119) by Chris Kuo (2024)
16. [Uncertainty Quantification and Why You Should Care](https://towardsdatascience.com/uncertainty-quantification-and-why-you-should-care-3f8a651f1956) by Jonte Dancker (2024)
17. [Probabilistic forecasting I: Temperature](https://stephane-degeye.medium.com/probabilistic-forecasting-i-temperature-f96ded1e7247) by Stephane Degeye (2024)
18. [Predict CO2 emissions by vehicles with Conformal Prediction](https://medium.com/@c.giancaterino/predict-co2-emissions-by-vehicles-with-conformal-prediction-3d40a5e8c136) by Claudio Giorgio Giancaterino (2024)
19. [Exploring Adaptive and Weighted Conformal Prediction Methods in the Presence of Covariate Shift](https://blog.devgenius.io/exploring-adaptive-and-weighted-conformal-prediction-methods-in-the-presence-of-covariate-shift-38ca04029292) by Peter Tettey Yamak (2024)
20. [Embracing Uncertainty with Conformal Prediction](https://medium.com/bigdatarepublic/embracing-uncertainty-with-conformal-prediction-099f928bc183) by Robbert van Kortenhof (2024)
21. [Tidymodels and conformal prediction](https://theclarkeorbit.github.io/tidymodels-and-conformal-prediction.html) by Prasanna Bhogale (2024)
22. [Basics of conformal prediction in time series data](https://theclarkeorbit.github.io/basics-of-conformal-prediction-in-time-series-data.html) by Prasanna Bhogale (2024)
23. [Conformal Prediction: A Critic to Predictive Models](https://medium.com/@data-overload/conformal-prediction-a-critic-to-predictive-models-27501dcc76d4) (2023)
24. [Putting clear bounds on uncertainty](https://news.mit.edu/2023/putting-clear-bounds-uncertainty-0123) (MIT, 2023)
25. [Conformal prediction theory explained](https://medium.com/low-code-for-advanced-data-science/conformal-prediction-theory-explained-14a35226df80) by Artem Ryasik (2023)
26. [Easy Distribution-Free Conformal Intervals for Time Series](https://towardsdatascience.com/easy-distribution-free-conformal-intervals-for-time-series-665137e4d907) by Michael Keith (2023)
27. [Another (Conformal) Way to Predict Probability Distributions](https://towardsdatascience.com/another-conformal-way-to-predict-probability-distributions-fcc63e78680d) by Harrison Hoffman (2023)
28. [Conformal Prediction for Regression](https://medium.com/@artem_ryasik/conformal-prediction-for-regression-1ba24f1442df) (using KNIME) by Artem Ryasik (2023)
29. [Dynamic Conformal Intervals for any Time Series Model](https://towardsdatascience.com/dynamic-conformal-intervals-for-any-time-series-model-d1638aa48527) by Michael Keith (2023) 🕒
30. [Hitting Time Forecasting: The Other Way for Time Series Probabilistic Forecasting](https://towardsdatascience.com/hitting-time-forecasting-the-other-way-for-time-series-probabilistic-forecasting-6c3b6496c353) by Marco Cerliani (2023) 🕒
31. [Clinical AI tools must convey predictive uncertainty for each individual patient](https://www.nature.com/articles/s41591-023-02562-7) (2023)
32. [How to use Conformal Prediction](https://coding.waterkant.sh/blog/conformal-prediction/) by Yannick Kälber (2023)
33. [Model Diagnostics: Prediction Uncertainty](https://piml.medium.com/model-diagnostics-prediction-uncertainty-990ff0bd2c4e) by PiML team, Wells Fargo (2023).
34. [Make any predictor uncertainty-aware via conformal prediction](https://mlwithouttears.com/2023/11/15/make-any-predictor-uncertainty-aware-via-conformal-prediction/) by Lorenzo Maggi (2023)
35. [Conformal predictive systems - A hands-on codeless example with KNIME](https://medium.com/low-code-for-advanced-data-science/conformal-predictive-systems-895c40bac2ca) by Artem Ryasik  (2023)
36. [Conformal prediction for classification - A hands-on codeless example with KNIME](https://medium.com/low-code-for-advanced-data-science/conformal-prediction-for-classification-6bf152abb491) by Artem Ryasik  (2023)
37. [Stanford statisticians and Washington Post data scientists build more honest prediction models](https://news.stanford.edu/2021/03/19/honesty-statistical-models/) [Code](https://github.com/washingtonpost/elex-live-model)
38. [How to Predict Risk-Proportional Intervals with Conformal Quantile Regression](https://towardsdatascience.com/how-to-predict-risk-proportional-intervals-with-conformal-quantile-regression-175775840dc4) by Samuele Mazzanti (2022).
39. [Conformal Prediction in Julia, Part I - Introduction](https://towardsdatascience.com/conformal-prediction-in-julia-351b81309e30) by Patrick Altmeyer (2022)
40. [How to Conformalize a Deep Image Classifier](https://towardsdatascience.com/how-to-conformalize-a-deep-image-classifier-14ead4e1a5a0) by Patrick Altmeyer (2022)
41. [Time Series Forecasting with Conformal Prediction Intervals: Scikit-Learn is All you Need](https://towardsdatascience.com/time-series-forecasting-with-conformal-prediction-intervals-scikit-learn-is-all-you-need-4b68143a027a) by Marco Cerliani (2022)
42. [Conformal Prediction in Julia, Part II - How to conformalize a deep image classifier](https://towardsdatascience.com/how-to-conformalize-a-deep-image-classifier-14ead4e1a5a0) by Patrick Altmeyer (2022)
43. [Conformal Prediction in Julia, Part III - Prediction intervals for any regression model](https://towardsdatascience.com/prediction-intervals-for-any-regression-model-306930d5ad9a) by Patrick Altmeyer (2022)
44. [Time Series Forecasting with Conformal Prediction Intervals: Scikit-Learn is All you Need](https://towardsdatascience.com/time-series-forecasting-with-conformal-prediction-intervals-scikit-learn-is-all-you-need-4b68143a027a) by Marco Cerliani (2022) 🕒
45. [Conformal Prediction for Neural Regression Model](https://pkghosh.wordpress.com/2021/12/30/conformal-prediction-for-a-neural-regression-model/) by Pranab Ghosh (2021).
46. [How to Handle Uncertainty in Forecasts](https://towardsdatascience.com/how-to-handle-uncertainty-in-forecasts-86817f21bb54) by Michael Berk (2021)
47. [How to Add Uncertainty Estimation to your Models with Conformal Prediction](https://towardsdatascience.com/how-to-add-uncertainty-estimation-to-your-models-with-conformal-prediction-a5acdb86ea05) by Zachary Warnes (2021)
48. [nonconformist: An easy way to estimate prediction intervals](https://medium.com/spikelab/nonconformist-an-easy-way-to-estimate-prediction-intervals-b0ded1eb066f) by Maria Jesus Ugarte (2021).
49. [Stanford statisticians and Washington Post data scientists build more honest prediction models](https://news.stanford.edu/2021/03/19/honesty-statistical-models/#) Stanford (2021)
50. [Measuring Models' Uncertainty: Conformal Prediction](https://blog.dataiku.com/measuring-models-uncertainty-conformal-prediction) by
Leo Dreyfus-Schmidt (Dataiku, 2020).
51. [Detecting Weird Data: Conformal Anomaly Detection](https://towardsdatascience.com/detecting-weird-data-conformal-anomaly-detection-20afb36c7bcd) by Matthew Burruss (2020).
52. [TQA: Creating Valid Prediction Intervals for Cross-sectional Time Series Regression](https://realsunlab.medium.com/tqa-creating-valid-prediction-intervals-for-cross-sectional-time-series-regression-bd0f2260fae7) by Zhen Lin (UIUC, NeurIPS’22 paper) 🕒

## Conformal Prediction Videos and Talks

1. [Machine Learning for Probabilistic and Conformal Prediction](https://www.youtube.com/watch?v=Cla7b6UYees) by Valery Manokhin (Seattle AI Workshops, 2023).
2. [Conformal Prediction: uncertainty quantification to humanise models](https://www.youtube.com/watch?v=EJVD-jU1A44) by Vincenzo Ventriglia (2025)
3. [An introduction to conformal prediction - PyLadies Amsterdam](https://www.youtube.com/watch?v=QFtdTyIWrz8) by Inge van den Ende (2024) [code](https://github.com/pyladiesams/conformal-prediction-jan2024)
4. [Analítica acelerada con Shapelets y conformal prediction, ~48 mins onwards](https://www.youtube.com/watch?v=4HxTUzPyK9g&t=4854s) by Carl McBride Ellis (2024) [code](https://github.com/Carl-McBride-Ellis/talks)
5. [Anushri Dixit - Planning with Confidence: Uncertainty Quantification for Safety-Critical Tasks](https://www.youtube.com/watch?v=hhSejSXde6U) (2024)
6. [Conformal Quantile Estimation in Economics](https://www.youtube.com/watch?v=6Brjt6aM140) by Martin Fankhauser (Bocconi, 2024)
7. [Big Data: 4th lecture (uncertainty in learning, big data for NLP)](https://www.youtube.com/watch?v=ikFkHig5o6g&list=PL8n4sZAL72Dn8GXuC0x9aXyiVGVAbPHz3&index=6) by Prof. Patrick Glauner (2024)
8. [Unveiling Precision: A Novel ML Framework for Accurate Probability Estimates by Abel and Edgar](https://www.youtube.com/watch?v=MuecMDKPqTQ&t=1672s), not CP per se, showing the critical importance of calibration in finance (2024)
9. [Autonomy Talks - Somil Bansal: Safety Assurances for Learning-Enabled Autonomous Systems](https://www.youtube.com/watch?v=3f8Q19-BqRo) by Somil Bansal (USC, 2024)
10. [Interview with Vladimir Vovk on Conformal Inference](https://www.youtube.com/watch?v=J7o2WJX_xQE) (2024)
11. [Error Embraced: Making Trustworthy Scientific Decisions with Imperfect Predictions](https://www.youtube.com/watch?v=oqLq-DUEP3s) by Clara Wong-fannjiang (Genentech) (2024)
12. [Conformalized Interval Arithmetic with Symmetric Calibration](https://arxiv.org/abs/2408.10939) by Rui Luo, Zhixin Zhou (City University of Hong Kong, 2024)
13. [Robust Yet Efficient Conformal Prediction Sets](https://www.youtube.com/watch?v=b5I_R3S2SdI) by  Soroush H. Zargarbash (2024)
14. [Applications of Conformal Prediction in Medicine | CGSI 2024](https://www.youtube.com/watch?v=xq3utQ12pzM) by Ahmed Alaa (2024)
15. [Mojtaba Farmanbar - Uncertainty quantification: How much can you trust your machine learning model?](https://www.youtube.com/watch?v=sKGtZyVyMM0) by Mojtaba Farmanbar (2024)
16. [Understanding, Generating, and Evaluating Prediction Intervals - posit conf 2024](https://www.youtube.com/watch?v=QT3SsD1kTj8) by Bryan Shalloway (2024)
17. [Install TorchCP Locally - Python Toolbox for Conformal Prediction on Deep Learning Models](https://www.youtube.com/watch?v=kdLnlafHAMI&t=307s) by Fahd Mirza (2024)
18. [Three Easy Steps to Understand Conformal Prediction (CP), Conformity Score, Python Implementation](https://www.youtube.com/watch?v=oqK6rM8fbkk) by (Dr. Data Science 2023)
19. [Emmanuel Candes - A Taste of Conformal Prediction](https://www.carmin.tv/en/video/a-taste-of-conformal-prediction) by Emmanuel Candes (2023)
20. [Foundations of Conformal Prediction - Full Conformal Predictors](https://www.youtube.com/watch?v=R1dnPAYGwnk) by Mahdi Torabi Rad (2023)
21. [Max Mergenthaler and Fede Garza - Quantifying Uncertainty in Time Series Forecasting](https://www.youtube.com/watch?v=Bj1U-Rrxk48) by Max Mergenthaler and Fede Garza (Nixtla, 2023) 🕒
22. [Uncertainty Quantification with the Fortuna library by Gianluca Detommaso (AWS)](https://www.youtube.com/watch?v=FEtD6lnsI58) by Gianluca Detommaso (Amazon, 2023)
23. [Quantifying Uncertainty in Time Series Forecasting](https://www.youtube.com/watch?v=Bj1U-Rrxk48) by Max Mergenthaler and Fede Garza (Nixtla, 2023)
24. [NISS/Merck Meetup on Conformal Inference: Advancing the Boundaries of Machine Learning 4.19.2023](https://www.youtube.com/watch?v=SRbqUae9-_o&t=5631s) (2023)
25. [Max Kuhn - The Post-Modeling Model to Fix the Model](https://www.youtube.com/watch?v=3omi4lm1da0) by Max Kuhn (2023)
26. [ISDFS Talk: Robots that ask for help: Conformal Prediction for LLM Planners](https://www.youtube.com/watch?v=WnQopZKJsTw) by Anirudha Majumdar (Princeton/DeepMind) (2023)
27. [Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners](https://www.youtube.com/watch?v=xvXrPdPb3Ko) by Allen Z Ren (2023)
28. [Introducing Sequential Predictive Conformal Inference (SPCI)](https://www.youtube.com/watch?v=NQHrTMZ2-XA&t=346) by Chen Xu (2023) 🕒
29. [Conformal Prediction Intervals: Empowering Executives for Informed Decision](https://www.youtube.com/watch?v=3StianQJZTk&t=26s) by Matthew Kolakowski (2023)
30. [Conformal Inference with Tidymodels - posit::conf(2023)](https://www.youtube.com/watch?v=vJ4BYJSg734) by Max Kuhn (2023)
31. [ACon^2: Adaptive Conformal Consensus for Provable Blockchain Oracles](https://www.youtube.com/watch?v=8PwDHAITuwU) by Sangdon Park (2023)
32. [Leveraging conformal prediction for calibrated probabilistic time series forecast](https://www.youtube.com/watch?v=--WcrDRtrYk) by Inge van den Ende (Dexter Energy, 2023) 🕒
33. [Uncertainty Quantification over Graph with Conformalized Graph Neural Networks](https://www.youtube.com/watch?v=Yq9cvqEk2K8&t=8s) by Kexin Huang (Stanford, 2023)
34. [Selection by Prediction with Conformal p-values](https://www.youtube.com/watch?v=VHcCmkChwTk&t=5s) by Ying Jin (Stanford, 2023)
35. [Trustworthy Retrieval Augmented Chatbots Utilizing Conformal Predictors](https://www.youtube.com/watch?v=JnWXebWUEg4) by Shuo Li (UPenn, 2023).
36. [Recent progress in predictive inference](https://www.youtube.com/watch?v=FQxpdMME0qU) by Emmanuel Candes, Stanford University (2022)
37. [Conformalized Survival Analysis with Adaptive Cutoffs](https://youtu.be/bvZ0SZlnkv8) by Rina Foygel Barber, Zhimei Ren, Yu Gui and Rohan Hore, University of Chicago (2022)
38. [Calibrating probabilistic hierarchical forecasts with conformal predictions](https://www.youtube.com/watch?v=VNhgk8Q1VFg) by Daan Ferdinandusse (University of Amsterdam, 2022)
39. [Michael I. Jordan on Conformal Prediction](https://www.youtube.com/watch?v=kSGP4F_ZcBY) by Michael I. Jordan (Berkeley, 2022)
40. [Distribution-free Prediction: Exchangeability and Beyond](https://www.youtube.com/watch?v=HVZDLhW8Kxg) by Rina Foygel Barber (University of Chicago, 2022)
41. [Purdue Statistics Theme Seminar, Conformal Prediction in 2022](https://www.youtube.com/watch?v=pjhp1moPvO4) by Emmanuel Candes (Stanford, 2022)
42. [WILL MY ROBOT ACHIEVE MY GOALS? PREDICTING THE PROBABILITY THAT AN MDP POLICY REACHES A USER-SPECIFIED BEHAVIOR TARGET](https://arxiv.org/pdf/2211.16462.pdf) by Alexander Guyer and Thomas G. Dietterich (University of Oregon, 2022)
43. [Robust and Equitable Uncertainty Estimation](https://www.youtube.com/watch?v=Iznj13jP9ag) by Aaron Roth(2022)
44. [Conformal prediction under feedback covariate shift for biomolecular design](https://www.youtube.com/watch?v=AOyDjBSQjhk) by Clara Wong-Fannjiang (Berkeley, 2022)
45. [Conformal prediction in 2022](https://slideslive.com/38996063/conformal-prediction-in-2022?ref=speaker-43789) invited talk by Emmanuel Candes at NeurIPS2022
46. [Broadening the Scope of Conformal Inference](https://slideslive.com/38988210/broadening-the-scope-of-conformal-inference?ref=search-presentations-Conformal+prediction) by Michael I. Jordan (University of Berkeley, 2022)
47. [Conformal testing in a binary model situation](https://www.youtube.com/watch?v=RTcT4YXRdMg) by Vladimir Vovk (Royal Holloway, UK, 2021)
48. [Protected probabilistic classification](https://www.youtube.com/watch?v=MpP-3suUoLY) by Vladimir Vovk (Royal Holloway, UK, 2021)
49. [Retrain or not retrain: conformal test martingales for change-point detection](https://www.youtube.com/watch?v=4Ra5KnDEfkw&t=1s) by Vladimir Vovk (Royal Holloway, UK, 2021)
50. [Steps Toward Trustworthy Machine Learning](https://www.youtube.com/watch?v=2iNRSgS7-L4) by Tom Dietterich (2021)
51. [Conformal Prediction Tutorial](https://www.youtube.com/watch?v=0MsGri8nmJQ) by Henrik Linusson (2021)
52. [How to increase certainty in predictive modeling](https://www.youtube.com/watch?v=fQQP84yxCRs&t=1277s) by Emmanuel Candes (Stanford, 2021)
53. [Venn Predictors Tutorial](https://www.youtube.com/watch?v=KsQpkjl7u1w) by Ulf Johansson, Cecilia Sönströd, Tuwe Löfström, and Henrik Boström (2021)
54. [Mondrian conformal predictive distributions](https://www.youtube.com/watch?v=dHNZxw8WQrs) by Henrik Boström, Ulf Johansson, and Tuwe Löfström (2021)
55. [Calibrating Multi-Class Models](https://www.youtube.com/watch?v=uCnFgTjUYto) by Ulf Johansson, Tuwe Löfström, and Henrik Boström (2021)
56. [Conformal testing in a binary model situation](https://www.youtube.com/watch?v=RTcT4YXRdMg) by Vladimir Vovk (Royal Holloway, UK, 2021)
57. [Conformal prediction in Orange](https://www.youtube.com/watch?v=qI1jOEour1g&t=14s) by Tomaž Hočevar and Blaž Zupan (2021)
58. [Distribution-Free, Risk-Controlling Prediction Sets](https://www.youtube.com/watch?v=ITJAR3fcNuI) by Anastasios Angelopoulos Berkeley, 2021)
59. Conformal Prediction and Distribution-Free Calibration by Aaditya Ramdas (Carnegie Mellon, 2021). Recording link unavailable.
60. [Conformal Inference of Counterfactuals and Time-to-event Outcomes](https://www.youtube.com/watch?v=nfD3mrSefbI) by Lihua Lei (Stanford, 2021)
61. [Algo Hour – Conformal Inference of Counterfactuals and Individual Treatment Effect](https://www.youtube.com/watch?v=COW2QNBmEMw) by Lihua Lei (Stanford, 2021)
62. [Conformal Inference of Counterfactuals and Individual Treatment effects(Stanford)](https://www.youtube.com/watch?v=8tM4BhONHms) by Lihua Lei (Stanford, 2021)
63. [Approximation to object conditional validity with inductive conformal predictors](https://www.youtube.com/watch?v=pUf7z2vxdi8) by Anthony Bellotti (University of Nottingham Ningbo, China, 2021)
64. [Ulf Johansson: Venn Predictors](https://www.youtube.com/watch?v=xxZOLo8wxe0&t=40s) by Ulf Johansson (Jönköping University, Sweden, 2021)
65. [Transformer-based conformal predictors for paraphrase detection](https://www.youtube.com/watch?v=HYP1ypxywWo) by Patrizio Giavannotti and Prof. Alexander Gammerman (Royal Holloway, UK, 2021)
66. [Shapley-value based inductive conformal prediction](https://www.youtube.com/watch?v=6XUc3HFa_5Q&t=1094s) by William Lopez Jaramillo (2021)
67. [Conformal Training: Learning Optimal Conformal Classifiers | DeepMind](https://www.youtube.com/watch?v=XMa1glDpVtQ&t=318s) by David Stutz (2021)
68. [Distribution-Free, Risk-Controlling Prediction Sets](https://www.youtube.com/watch?v=z8WDmD5D-I0) by Anastasios Angelopoulos (2021)
69. [Neural Predictive Monitoring under Partial Observability](https://www.youtube.com/watch?v=JhJXUDPoKCc) by Francesca Cairolli (2021)
70. [Fast conformal classification using influence functions](https://www.youtube.com/watch?v=LRwm976poDE) by Giovanni Cherubin (Alan Turing Institute, UK, 2021)
71. [Valid inferential models and conformal prediction](https://www.youtube.com/watch?v=egrLw0CmXTs) by Ryan Martin (North Carolina State University, USA, 2021)
72. [Mondrian conformal predictive distributions](https://www.youtube.com/watch?v=dHNZxw8WQrs&t=1415s) by Henrik Boström, Ulf Johansson and Tuwe Löfström (KTH Royal Institute of Technology, Sweden, 2021)
73. [Evaluation of updating strategies for conformal predictive systems in the presence of extreme events](https://www.youtube.com/watch?v=Xgs0JqDw8lA) by Hugo Werner, Lars Carlsson, Ernst Ahlberg and and Henrik Boström (KTH Royal Institute of Technology, Sweden, 2021)
74. [Class-wise confidence for debt prediction in real estate management](https://www.youtube.com/watch?v=ZVhA8LGXWpc) by Soundouss Messoudi (2021)
75. [How Nonconformity Functions and Difficulty of Datasets Impact the Efficiency of Conformal Classifiers](https://www.youtube.com/watch?v=lLtZkVwxMNw) by Marharyta Aleksandrova (2021)
76. [Panel with Michael I. Jordan, Vladimir Vovk, and Larry Wasserman, moderated by Aaditya Ramdas](https://slideslive.com/38964850/panel-with-michael-i-jordan-vladimir-vovk-and-larry-wasserman-moderated-by-aaditya-ramdas?ref=account-folder-87373-folders) by Vladimir Vovk, Larry Wasserman, Michael I. Jordan, Aaditya Ramdas, ICML 2021
77. [Black-box uncertainty - Anastasios Angelopoulos](https://www.youtube.com/watch?v=jW-mbsVgcIc) by Anastasios Angelopoulos (Berkeley, USA, 2021)
78. [P.C. Mahalanobis Memorial Lectures 2020-21](https://www.isibang.ac.in/~statmath/pcm2020/) by Vladimir Vovk (Royal Holloway, UK, 2021)
79. [Fast conformal classification using influence functions](https://www.youtube.com/watch?v=LRwm976poDE) by Umang Bhatt, Adrian Weller and Giovanni Cherubin (Cambridge / Alan Turinig Institute, 2021).
80. [A Tutorial on Conformal Predictive Distributions](https://www.youtube.com/watch?v=FUi5jklGvvo&t=3s) by Paolo Toccaceli (Royal Holloway, UK, 2020)
81. [Henrik Linusson: Conformal Prediction](https://www.youtube.com/watch?v=lQxH-zXrOwI&t=1522s) by Henrik Linusson (2020)
82. [Recent Progress in Predictive Inference](https://www.youtube.com/watch?v=tY73G_UvkAE&t=833s) by Emmanuel Candes (Stanford, 2020)
83. [Some recent progress in predictive inference" (Stanford) @ MAD+](https://www.youtube.com/watch?v=djgxwpJQyAA) by Emmanuel Candes (Stanford, 2020)
84. [Conformal Prediction in 2020](https://www.youtube.com/watch?v=61tpigfLHso&t=1507s) by Emmanuel Candes (Stanford, 2020)
85. [Assumption-free prediction intervals for black-box regression algorithms](https://www.youtube.com/watch?v=GMnCO7_HIOY&t=3943s) by Aaditya Ramdas (Carnegie Mellon, 2020)
86. [Conformal Inference of Counterfactuals and Individual Treatment Effects](https://www.youtube.com/watch?v=jkFs6pLZXBQ) by Lihua Lei (Stanford, 2020)
87. [Model-Free Predictive Inference](https://www.youtube.com/watch?v=8GkhRuWcd0w) by Larry Wasserman (Carnegie Mellon, 2020)
88. [Ulf Johansson: Venn Predictors](https://www.youtube.com/watch?v=xxZOLo8wxe0&t=98s) by Ulf Johansson (Jönköping University, Sweden, 2020)
89. [Nested conformal prediction and quantile out-of-bag ensemble methods](https://www.youtube.com/watch?v=NlUlelNWVMQ) by Chirag Gupta (Carnegie Mellon, 2020)
90. [Maria Navarro: Quantifying uncertainty in Machine Learning predictions | PyData London 2019](https://www.youtube.com/watch?v=r6bhm_A-YcQ&t=12s) by Maria Navarro (2019)
91. [Rahul Vishwakarma: New Perspective on Machine Learning Predictions Under Uncertainty | SNIA Storage Developer Conference, Santa Clara 2019](https://www.youtube.com/watch?v=T-hG1JyAk4E) by Rahul Vishwakarma (2019)
92. [Treatment of Uncertainty in the Foundations of Probability](https://www.youtube.com/watch?v=B7E-QJ9fm4w&t=2297s) by Vladimir Vovk (Royal Holloway, UK, 2017)
93. [Predicting with Confidence - Henrik Boström](https://www.youtube.com/watch?v=eXU-64dwHmA) by Henrik Boström (2016)
94. [Assumption-Free, High-Dimensional Inference](https://www.youtube.com/watch?v=UOMvUaYfpH4) by Larry Wasserman (2016)
95. [Large-Scale Probabilistic Prediction With and Without Validity Guarantees](https://www.youtube.com/watch?v=ksrUJdb2tA8) by Vladimir Vovk (Royal Holloway, UK, NeurIPS 2015)
96. [Reliable Diagnostics by Conformal Predictors](https://www.youtube.com/watch?v=zW3R-vbLw58) by Alexander Gammerman (Royal Holloway, UK, 2015)
97. [Conformalized Kernel Ridge Regression and Its Efficiency](https://www.youtube.com/watch?v=OLeu9TXE5n4) by Evgeny Burnaev (Skolkovo, Russia, 2015)
98. [Conformal Prediction: Enhanced Method for Understanding the Prediction Quality](https://www.youtube.com/watch?v=_ZVuEWEfwuw&t=948s) by Artem Ryasik and Greg Landrum
99. [Paper Reading Group - Fortuna, a Library for Uncertainty Quantification](https://www.youtube.com/watch?app=desktop&v=S_QgP3jBCqw)
100. [CLIMB Evergreen talk with Emmanuel Candès: Conformal Inference when Data is not Exchangeable](https://www.youtube.com/watch?v=D60vtpnkhTU) 🕒
101. [Algo Hour – Conformal Inference of Counterfactuals and Individual Treatment Effects | Lihua Lei](https://www.youtube.com/watch?v=COW2QNBmEMw&t=2s)
102. ['MoroccoAI webinar - Dr. Soundouss Messoudi - 'Confidence learning using conformal prediction'](https://www.youtube.com/watch?v=SypbjiBrt3Q)
103. [Rising Stars #8: Clara Wong-Fannjiang (Genentech) - Prediction-Powered Inference](https://www.youtube.com/watch?v=TlFpVpFx7JY)
104. [Rising Stars #10 - Special Series on Conformal Prediction: Isaac Gibbs (Stanford University) Conformal Inference with Conditional Guarantees](https://www.youtube.com/watch?v=rvYnR0FGxM4)
105. [Conformal Prediction for Time Series with Modern Hopfield Networks](https://www.youtube.com/watch?v=QhvLaZ1aS6A) by Andreas Auer 🕒
109.

## Conformal Prediction Presentation Slides
1. [Machine Learning for Probabilistic Prediction, Seattle Artificial Intelligence Workshops Meetup](https://www.researchgate.net/publication/371566526_Machine_Learning_for_Probabilistic_Prediction) by Valery Manokhin, 2023
2. [Machine Learning for Probabilistic Prediction](https://www.researchgate.net/publication/370012303_Machine_Learning_for_Probabilistic_Prediction) by Valery Manokhin (2023)
3. [Machine Learning for Probabilistic Prediction](docs/assets/Machine%20Learning%20for%20Probabilistic%20Prediction.pdf) by Valery Manokhin (Stony Brook University webinar slides, 2022)
4. [Nonparametric predictive distributions based on conformal prediction](https://cml.rhul.ac.uk/copa2017/presentations/vovk.pdf) by Vladimir Vovk, Jieli Shen, Valery Manokhin, Min-ge Xie, Ilia Nouretdinov and Alex Gammerman (Royal Holloway, University of London Rutgers University, 2017)
5. [Conformalized Quantile Regression](https://arxiv.org/abs/1905.03222) by Yaniv Romano, Evan Patterson, Emmanuel J. Candès (Stanford, 2019) 🔥
6. [Sequential Predictive Conformal Inference for Time Series](https://arxiv.org/pdf/2212.03463.pdf) by Chen Xu, Yao Xie (Georgia Tech, 2022) 🕒
7. [Conformal Inference with Tidymodels](https://topepo.github.io/posit-2023-conformal/#/title-slide) by Max Kuhn (posit conference 2023)
8. [Leveraging Conformal Prediction for Calibrated Probabilistic Time Series Forecasts to Accelerate the Renewable Energy Transition](https://speakerdeck.com/ingevandenende/leveraging-conformal-prediction-for-calibrated-probabilistic-time-series-forecasts-to-accelerate-the-renewable-energy-transition) by Inge van den Ende (Dexter Energy, 2023).  🕒
9. [crepes: a Python Package for Conformal Regressors and Predictive Systems](https://cml.rhul.ac.uk/copa2022/presentations/COPA_2022_Presentation__crepes.pdf) by Henrik Bostroem (KTH, Sweden, 2022)
10. [Conformal Prediction: an Introduction](https://github.com/online-ml/river/files/10098389/Conformal_Prediction_Presentation.pdf) by Leo Andeol (2022)
11. [EnbPI poster](https://sites.gatech.edu/chenxu97/files/2023/01/EnbPI_poster.pdf) by Chen Xu, Yao Xie (2021)
12. [Conformal Regressors and Predictive Systems – a Gentle Introduction](https://cml.rhul.ac.uk/copa2022/presentations/COPA_2022_Presentation__Conformal_Regressors_and_Predictive_Systems___a_Gentle_Introduction.pdf) by Henrik Bostroem (KTH, Sweden, 2022)
13. [Applications of Conformal Predictors](https://cml.rhul.ac.uk/copa2022/presentations/lars_ernst.pdf) by Ernst Ahlberg and Lars Carlsson (Stena Line, 2022)
14. [Assessing Explanation Quality by Venn Prediction](https://cml.rhul.ac.uk/copa2022/presentations/amr.pdf) by Amr Alkhatib, Henrik Boström and Ulf Johansson (2022)
15. [Well-Calibrated Rule Extractors](https://cml.rhul.ac.uk/copa2022/presentations/Johansson_U_COPA2022_pres.pdf) by Ulf Johansson, Tuwe Löfström, Niclas Ståhl (2022)
16. [Calibration of Natural Language Understanding Models with Venn-ABERS Predictors](https://cml.rhul.ac.uk/copa2022/presentations/patrizio.pdf) by Patrizio Giovannotti (2022)
17. [Reinforcement Learning Prediction Intervals with Guaranteed Fidelity](https://web.engr.oregonstate.edu/~tgd/talks/dietterich-caml-rl-prediction-intervals.pdf) by Thomas Dietterich (University of Oregon, 2022)
18. [Conformal Prediction beyond exchangeability](https://cml.rhul.ac.uk/copa2022/presentations/conformal_UAI_tutorial_2.pdf) by Rina Foygel Barber (University of Chicago, 2022)
19. [Split conformal prediction for dependant data](https://www.im.ufrj.br/coloquiomea/apresentacoes/orenstein_2022.pdf) by Roberto I. Oliveira, Paulo Orenstein, Thiago Ramos and João Vitor Romano (2022)
20. [Copula Conformal Prediction for Multi-step Time Series Forecasting](https://arxiv.org/abs/2212.03281) by Sophia Sun, Rose Yu (University of California, San Diego, 2022)
21. [Uncertainty estimation in NLP](https://sites.google.com/view/uncertainty-nlp#h.is5zc8lcnuki) by Tal Schuster, Adam Fisch (MIT, 2022)
22. [Adaptive Conformal Anomaly Detection for Time-series](https://cml.rhul.ac.uk/copa2017/presentations/burnaev.pdf) by Evgeny Burnaev, Alexander Bernstein, Vlad Ishimtsev and Ivan Nazarov (Skoltech, Moscow, Russia, 2017)
23. [What Can Conformal Inference Offer to Statistics?](https://lihualei71.github.io/Job_Talk_Lihua_Lei.pdf) by Lihua Lei, Stanford University
24. [Conformal prediction of small-molecule drug resistance in cancer cell lines](https://cml.rhul.ac.uk/copa2022/presentations/saiveth.pdf) by Saiveth Hernandez-Hernandez, Sachin Vishwakarma and Pedro Ballester
25. [Graceful handling of large imbalanced datasets using Conformal Prediction](https://bigchem.eu/sites/default/files/AZ_school_Norinder_public.pdf) by Ulf Norinder and Fredrik Svensson
26. [Application of Conformal Inference in High Energy Physics](https://indico.phys.ethz.ch/event/113/contributions/863/attachments/528/1129/NPML2024_JF_final2.pdf) by Jiri Franc (CTU Prague,Czech Republic)

---

## 📚 Research: Papers and Theses

## Conformal Prediction Papers
1. [Nonparametric predictive distributions based on conformal prediction](https://link.springer.com/article/10.1007%2Fs10994-018-5755-8) by Vladimir Vovk, Jieli Shen, Valery Manokhin and Min-ge Xie (Royal Holloway, UK / Rutgers, USA, 2018) 🔥
2. [Classifier Calibration at Scale: An Empirical Study of Model-Agnostic Post-Hoc Methods](https://arxiv.org/abs/2601.19944) by Valery Manokhin and Daniel Grønhaug (2026)  [Related COPA 2026 extended abstract](https://proceedings.mlr.press/v329/manokhin26a.html)
3. [A Review and Comparative Analysis of Univariate Conformal Regression Methods](https://proceedings.mlr.press/v266/bao25a.html) by Jie Bao, Nicolò Colombo, Valery Manokhin, Suqun Cao, Rui Luo (COPA 2025)
4. [Multi-class probabilistic classification using inductive and cross Venn–Abers predictors](https://proceedings.mlr.press/v60/manokhin17a.html) by Valery Manokhin (Royal Holloway, UK, 2017)
5. [The Manokhin Probability Matrix: A Diagnostic Framework for Classifier Probability Quality](https://zenodo.org/records/19372589) by Valery Manokhin (2026)
6. [Computationally efficient versions of conformal predictive distributions](https://arxiv.org/abs/1911.00941) by Vladimir Vovk, Ivan Petej, Ilia Nouretdinov, Valery Manokhin, Alex Gammerman (Royal Holloway, UK, 2019)
7. [Cross-conformal predictive distributions](http://proceedings.mlr.press/v91/vovk18a.html) by Vladimir Vovk, Ilia Nouretdinov, Valery Manokhin and Alexander Gammerman (Royal Holloway, UK, 2018)
8. [Conformal predictive distributions with kernels](https://arxiv.org/abs/1710.08894) by Vladimir Vovk, Ilia Nouretdinov, Valery Manokhin, Alex Gammerman (Royal Holloway, UK, 2017)
9. [Conformal Risk Control](https://arxiv.org/pdf/2208.02814.pdf) by Anastasious Angelopolous, Stephen Bates, Adam Fisch, Lihua Lei and Tal Schuster (Berkeley, Stanford, MIT and Google Research, 2022) 🔥
10. [Conformalized Quantile Regression](https://arxiv.org/abs/1905.03222) by Yaniv Romano, Evan Patterson, Emmanuel J. Candès (Stanford, 2019) [code](https://github.com/yromano/cqr) [project](https://sites.google.com/view/cqr) 🔥
11. [Predictive inference with the jackknife+](https://arxiv.org/abs/1905.02928) by Rina Foygel Barber, Emmanuel Candès, Aaditya Ramdas, and Ryan Tibshirani (2020) 🔥
12. [Conformal prediction interval for dynamic time-series](https://proceedings.mlr.press/v139/xu21h.html) by Chen Xu, Yao Xie (Georgia Tech, 2021) 🕒 🔥
13. [Conformal Prediction Under Covariate Shift](https://arxiv.org/abs/1904.06019) by Ryan Tibshirani, Rina Foygel Barber, Emmanuel Candes, Aaditya Ramdas (Carnegie Mellon, Stanford, Chicago, 2019) 🔥
14. [Uncertainty Sets for Image Classifiers using Conformal Prediction](https://arxiv.org/pdf/2009.14193.pdf) by Anastasios N. Angelopoulos, Stephen Bates, Jitendra Malik, & Michael I. Jordan (Berkeley, 2021)
15. [Inductive Venn–Abers and related regressors](https://proceedings.mlr.press/v329/petej26a.html) by Ivan Petej and Vladimir Vovk (COPA 2026). Extends Venn–Abers methods to unbounded regression by combining them with conformal prediction.
16. [Selection-Safe Conformal Early Exit: Distribution-Free Coverage under Adaptive Depth](https://arxiv.org/abs/2610.20773) by Adria Binte Habib and Ibne Farabi Shihab (2026 preprint). Calibrates nested sets to preserve coverage for label-free stopping rules that keep the terminal set contained.
17. [On Optimal Data Splitting for Split Conformal Prediction](https://arxiv.org/abs/2606.31600) by Sayan Das, Bahram Yaghooti, Todd A. Kuffner and Soumendra N. Lahiri (2026 preprint). Derives training-calibration split choices aimed at reducing interval length.
18. [Aggregation in conformal e-classification](https://proceedings.mlr.press/v329/vovk26a.html) by Vladimir Vovk (COPA 2026). Compares cross-conformal e-classification with simpler aggregation rules and tests their predictive efficiency.
19. [Conformal Calibration for Multi-Modal Regression with Missing Modalities](https://proceedings.mlr.press/v329/azizi26a.html) by Ilia Azizi (COPA 2026). Calibrates multimodal regression intervals using model disagreement and the availability of modalities.
20. [Conformal Prediction in Hierarchical Classification with Constrained Representation Complexity](https://proceedings.mlr.press/v300/mortier26a.html) by Thomas Mortier et al. (AISTATS 2026). Develops two split-conformal algorithms for hierarchical classification and compares prediction set size at different representation complexities.
21. [Conformal prediction or the good old DKW from the 50s?](https://proceedings.mlr.press/v329/johnstone26a.html) by Chancellor Johnstone and Eugene Ndiaye (COPA 2026). Compares conformal prediction, DKW bounds and tolerance regions on a common scale and distinguishes marginal from training-conditional coverage.
22. [Conformal Prediction via Transported Beta Laws](https://proceedings.mlr.press/v329/r-ramos26a.html) by Thiago R. Ramos et al. (COPA 2026). Uses a beta reference law and Wasserstein distance to quantify how calibration dependence and test shift affect conditional coverage.
23. [Conformal Privacy Auditing: Calibrated Re-identification Attacks with Statistical Guarantees](https://aclanthology.org/2026.emnlp-main.58/) by Shuo Huang et al. (EMNLP 2026). Constructs sets of candidate identities with marginal coverage under exchangeability to audit text re-identification risk from LLM-enabled attackers.
24. [Conformal Robust Control of Linear Systems](https://proceedings.mlr.press/v300/patel26b.html) by Yash Patel et al. (AISTATS 2026). Builds data-driven uncertainty regions for robust linear-quadratic control and analyzes controller regret under dynamics misspecification.
25. [Corrected Max-Rank for Finite-Sample Conformal Prediction](https://proceedings.mlr.press/v329/schlembach26a.html) by Filip Schlembach et al. (COPA 2026). Corrects the Max-Rank threshold by one order statistic and proves finite-sample validity for multi-target prediction under exchangeability.
26. [Counterfactually Fair Conformal Prediction](https://proceedings.mlr.press/v300/guldogan26a.html) by Ozgur Guldogan et al. (AISTATS 2026). Symmetrizes conformity scores across protected-attribute interventions to obtain counterfactually fair sets with marginal coverage under the stated assumptions.
27. [Efficient Confidence Set Enumeration for Multi-label Conformal Classification](https://proceedings.mlr.press/v337/ledaguenel26a.html) by Arthur Ledaguenel et al. (UAI 2026). Gives a linear-delay algorithm for modular nonconformity losses and efficient enumeration conditions when Boolean circuits constrain valid label combinations.
28. [Feedback-Enhanced Online Multiple Testing with Applications to Conformal Selection](https://www.jmlr.org/papers/v27/25-2123.html) by Lin Lu et al. (JMLR 2026). Builds online conformal selection rules that use revealed outcomes to adapt thresholds and control marginal false discovery rate.
29. [MuLaConf: Multi-label Conformal Prediction](https://proceedings.mlr.press/v329/katsios26a.html) by Kostas Katsios and Harris Papadopoulos (COPA 2026). Introduces a scikit-learn-compatible package for multilabel conformal prediction with distance scores, structural penalties and accelerated tensor operations.
30. [No Free Lunch in Few-Step Flow Matching for Conformal Prediction](https://proceedings.mlr.press/v329/li26b.html) by Ziyun Li and Henrik Boström (COPA 2026 extended abstract). Tests how sampler step count affects conformal set size and demonstrates coverage loss when calibration and deployment use different samplers.
31. [Partial Causal Structure Learning for Valid Selective Conformal Inference under Interventions](https://proceedings.mlr.press/v337/asiaee26b.html) by Amir Asiaee et al. (UAI 2026). Quantifies how selective conformal coverage degrades when calibration includes target-affecting interventions and gives a correction when contamination can be bounded.
32. [Principled Context Engineering for RAG: Statistical Guarantees via Conformal Prediction](https://arxiv.org/abs/2511.17908) by Debashish Chakraborty et al. (ECIR 2026). Applies conformal thresholds to filter retrieved context before generation and evaluates the retained evidence and downstream answers.
33. [Reliable Conformal Prediction for Ordinal Classification Using the Ranked Probability Score](https://proceedings.mlr.press/v337/haas26a.html) by Stefan Haas et al. (UAI 2026). Uses the ranked probability score to produce contiguous prediction sets for ordered labels and evaluates the magnitude of ordinal miscoverage.
34. [SafeImpute: Reliable Clinical Data Imputation via Conformal Selection](https://arxiv.org/abs/2607.05613) by Xinrui He et al. (KDD 2026). Uses conformal p-values and multiple-testing correction to control unacceptable errors among released clinical imputations.
35. [Spectral and Conformal: Neural Network Methods for Calibrated Trajectory Prediction and Control-Point Intervals](https://tmlr.infinite-conf.org/paper_pages/zKLMev1mnQ.html) by Jasmine Ratchford and Raffaele Romagnoli (TMLR 2026). Uses modified conformal quantile regression for trajectory-level coverage and interval arithmetic to extend the result to control points under the specified dynamics.
36. [Uncertainty Quantification for Named Entity Recognition via Conformal Prediction](https://proceedings.mlr.press/v300/singer26a.html) by Matthew Singer et al. (AISTATS 2026). Calibrates prediction sets over complete named-entity label sequences and tests scores tailored to sentence length and language.
37. [A Quiet Failure in Calibrated Virtual Screening: Marginal Conformal Prediction Under-Covers the Minority Class, and a Class-Conditional Fix Recovers It](https://arxiv.org/abs/2607.06605) by Muhammadjon Tursunbadalov and Mustafojon Tursunbadalov (2026 preprint). Documents rare-class undercoverage in virtual screening under marginal calibration and tests class-conditional calibration as a remedy.
38. [Abstention Spends Its Budget on Local Label Variance More Than on Novelty: Auditing Conformal Calibration and Selective Prediction under Molecular Scaffold Shift](https://arxiv.org/abs/2611.01512) by Arnav Srivastava and Krishna Kassetty (2026 p