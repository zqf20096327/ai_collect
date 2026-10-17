![GitHub Repo stars](https://img.shields.io/github/stars/valeman/awesome-conformal-prediction?style=social)

# Conformal Prediction: The Definitive Resource [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re) [![DOI](https://zenodo.org/badge/436989758.svg)](https://zenodo.org/badge/latestdoi/436989758)

⭐ **The definitive resource for conformal prediction: methods, libraries, tutorials, benchmarks, and production guides.**

🔥 *Updated regularly with the latest conformal prediction research (2025–2026).* The canonical repository for conformal prediction, maintained by a leading researcher in the field — used by researchers, practitioners, and production teams worldwide.

**Topics covered:** conformal prediction · conformal inference · prediction intervals · uncertainty quantification · model calibration · distribution-free inference · selective prediction · trustworthy machine learning · LLM uncertainty · time series forecasting · anomaly detection


**Conformal prediction** (also called **conformal inference**) is a distribution-free, model-agnostic framework for quantifying predictive uncertainty. Instead of returning a single point prediction, a conformal predictor returns a **prediction set** (for classification) or a **prediction interval** (for regression) that is guaranteed to contain the true label with a user-chosen probability — for example 90% or 95% — under the mild assumption that the data are exchangeable. These guarantees hold in **finite samples**, for **any underlying model** (random forests, gradient boosting, deep neural networks, large language models), and **without any distributional assumptions**.


## 🧭 New here? Follow this path

| Step | What to do | Where to look |
|---:|---|---|
| 1 | Understand the core idea in 10 minutes | [Tutorials](#conformal-prediction-tutorials) |
| 2 | Watch a 30-minute talk | [Videos and Talks](#conformal-prediction-videos-and-talks) |
| 3 | Read a gentle introduction | [Articles](#articles-on-conformal-prediction) |
| 4 | Try it in code | [Libraries in Python](#conformal-prediction-libraries-in-python) · [Quickstart](#quickstart) |
| 5 | Go deep | [Courses](#conformal-prediction-courses) · [Books](#books-on-conformal-prediction) · [Papers](#conformal-prediction-papers) |

---

## 📘 Learn from the Experts — Book & Course by Dr. Valeriy Manokhin

<table>
<tr>
<td width="50%" valign="top">

### 🎓 Applied Conformal Prediction — Live Course on Maven

A hands-on, cohort-based course taught by **Dr. Valeriy Manokhin** (PhD, Machine Learning; author of *Practical Guide to Applied Conformal Prediction*; PhD student of Prof. Vladimir Vovk — the creator of conformal prediction).

You will learn how to apply conformal prediction to regression, classification, time series, anomaly detection, and LLM uncertainty, with production-ready Python code and real datasets.

🔥 **[Enroll in the next cohort →](https://maven.com/valeriy-manokhin/applied-conformal-prediction)**
📩 **[Register interest for upcoming cohorts →](https://maven.com/forms/2a53e5)**

</td>
<td width="50%" valign="top">

### 📚 Applied Conformal Prediction — The Book

The definitive practitioner's book on conformal prediction — from first principles to industry-grade applications, with code you can run today. Written by **Dr. Valeriy Manokhin**.

🚀 **[Applied Conformal Prediction — Pro Edition](https://valeman.gumroad.com/l/applied_conformal_prediction_pro)** ⭐ *Recommended*
The most comprehensive edition: extended chapters, advanced methods, and production-grade code.

📘 **[Applied Conformal Prediction — Standard Edition](https://valeman.gumroad.com/l/appliedconformalprediction)**
The core book covering regression, classification, time series, anomaly detection, and LLM uncertainty.

Both editions are available exclusively on **Gumroad**.

🌐 **[valeriy.ai](https://valeriy.ai)** — author's website with research, papers, and updates.

</td>
</tr>
</table>

> *"The most comprehensive practical resource on conformal prediction currently available."*

---

## What is Conformal Prediction?

Conformal prediction wraps any predictive model and converts its outputs into statistically valid prediction sets or intervals. The recipe is simple:

1. Train any model on a training set.
2. Score a held-out **calibration set** with a *nonconformity* function (e.g. absolute residual for regression, 1 − softmax for classification).
3. At test time, output every label whose nonconformity score is no worse than the (1 − α) quantile of the calibration scores.

The resulting prediction set is guaranteed to cover the true label with probability at least 1 − α, regardless of the model or the data distribution. This makes conformal prediction one of the most practical tools for **uncertainty quantification**, **trustworthy machine learning**, **selective prediction**, and **safe deployment of AI systems**.

## Quickstart

A minimal end-to-end example using [crepes](https://github.com/henrikbostrom/crepes):

```python
import numpy as np
from crepes import ConformalRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

X, y = fetch_california_housing(return_X_y=True)
X_train, X_rest, y_train, y_rest = train_test_split(X, y, test_size=0.4, random_state=0)
X_cal,  X_test, y_cal,  y_test  = train_test_split(X_rest, y_rest, test_size=0.5, random_state=0)

model = RandomForestRegressor(n_estimators=200, random_state=0).fit(X_train, y_train)
residuals_cal = np.abs(y_cal - model.predict(X_cal))

cr = ConformalRegressor().fit(residuals=residuals_cal)
intervals = cr.predict(y_hat=model.predict(X_test), confidence=0.9)  # 90% intervals
```

Runnable notebooks live in [`examples/`](examples/). See [`CONTRIBUTING.md`](CONTRIBUTING.md) to add resources.

---

## About this list

This collection is curated by **[Dr. Valeriy Manokhin](https://valeriy.ai)**, who completed his PhD in Machine Learning under the supervision of Prof. Vladimir Vovk — the creator of conformal prediction. It is the culmination of resources gathered since 2015. Conformal prediction has gone from a niche framework to a mainstream method for uncertainty quantification, with dedicated tracks at [ICML 2021](https://icml.cc/Conferences/2021/ScheduleMultitrack?event=8373) and [ICML 2022](https://sites.google.com/berkeley.edu/dfuq-22/home), a NeurIPS 2022 keynote ['Conformal Prediction in 2022'](https://slideslive.com/38996063/conformal-prediction-in-2022?ref=speaker-43789) by Prof. Emmanuel Candes, and the long-running [COPA conference](https://copa-conference.com).

> *"Conformal Prediction ideas are THE answer to UQ, I think it's the best I have seen — its simple, generalisable etc."* — **Prof. Michael I. Jordan**, ICML 2021

> *"The beauty of the conformal thing is how simple it is to do it and how general it is."* — **Prof. Larry Wasserman**, Carnegie Mellon

> *"Conformal inference methods are becoming all the rage in academia and industry alike."* — **Prof. Emmanuel Candes**, Stanford

The author's course **'Applied Conformal Prediction'** is open for enrollment on Maven — [enroll in the next cohort](https://maven.com/valeriy-manokhin/applied-conformal-prediction) or [register interest](https://maven.com/forms/2a53e5). The companion book *'Applied Conformal Prediction: Reliable Uncertainty Quantification for Real-World Machine Learning'* is available on [Gumroad](https://valeman.gumroad.com/l/appliedconformalprediction).

<a href="https://www.buymeacoffee.com/valeman" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

### Citation

```bibtex
@software{manokhin_valery_2022_6467204,
  author  = {Manokhin, Valery},
  title   = {Awesome Conformal Prediction},
  month   = apr,
  year    = 2022,
  publisher = {Zenodo},
  version = {v1.0.0},
  doi     = {10.5281/zenodo.6467204},
  url     = {https://doi.org/10.5281/zenodo.6467204}
}
```

Licensed CC BY-NC-ND 4.0. Academic work must cite.

---

## 💬 Open Questions in Conformal Prediction

These are active research and practitioner questions — contributions, discussion, and PRs welcome:

- What is the best conformal prediction library today for production use?
- Are transformers and LLMs fully compatible with conformal prediction guarantees?
- How should practitioners handle distribution shift and covariate drift in practice?
- What are the tightest known prediction intervals for deep learning models?
- How do conformal methods compare with Bayesian uncertainty quantification on modern benchmarks?

👉 Open a [discussion](https://github.com/valeman/awesome-conformal-prediction/discussions) or [issue](https://github.com/valeman/awesome-conformal-prediction/issues) to contribute.

## Table of Contents

**🚀 Start Here — Learn Conformal Prediction**
* [Tutorials](#conformal-prediction-tutorials)
* [Courses](#conformal-prediction-courses)
* [Books](#books-on-conformal-prediction)
* [Articles](#articles-on-conformal-prediction)
* [Videos and Talks](#conformal-prediction-videos-and-talks)
* [Presentation Slides](#conformal-prediction-presentation-slides)

**🛠 Open-Source Libraries and Tools**
* [Python](#conformal-prediction-libraries-in-python)
* [R](#conformal-prediction-libraries-in-r)
* [Julia](#conformal-prediction-libraries-in-julia)
* [Other Languages](#conformal-prediction-in-other-languages)
* [AI Platforms](#ai-platforms-using-conformal-prediction)
* [Kaggle Notebooks](#conformal-prediction-on-kaggle)

**📚 Research: Papers and Theses**
* [Papers (general)](#conformal-prediction-papers)
* [Time Series Forecasting](#conformal-prediction-for-time-series-forecasting)
* [Anomaly Detection](#conformal-prediction-for-anomaly-detection)
* [PhD Theses](#phd-theses-on-conformal-prediction)

**🌍 Community, Events, and People**
* [Events and Workshops](#conformal-prediction-events-and-workshops)
* [Conferences](#conferences-featuring-conformal-prediction)
* [Researchers](#conformal-prediction-researchers)
* [Websites](#conformal-prediction-websites)
* [Twitter / X](#conformal-prediction-on-twitter--x)


---

## 🚀 Start Here — Learn Conformal Prediction

## Conformal Prediction Tutorials
1. [Conformal Prediction Tutorial](https://www.youtube.com/watch?v=0MsGri8nmJQ) by Henrik Linusson (2021) 🔥🔥🔥🔥
2. [Predicting with Confidence - Henrik Boström](https://www.youtube.com/watch?v=eXU-64dwHmA) by Henrik Boström (2016)  🔥🔥🔥🔥
3. [Henrik Linusson: Conformal Prediction](https://www.youtube.com/watch?v=lQxH-zXrOwI&t=1522s) by Henrik Linusson (2020)  🔥🔥🔥🔥
4. [A Tutorial on Conformal Prediction](https://jmlr.org/papers/v9/shafer08a.html) by Glenn Shafer and Vladimir Vovk (2008) 🔥🔥🔥🔥🔥
5. [Tutorial on Venn-ABERS prediction](https://cml.rhul.ac.uk/people/ptocca/HomePage/Toccaceli_CP___Venn_Tutorial.pdf) by Paolo Toccaceli (Royal Holloway, UK, 2019) 🔥🔥🔥🔥🔥
6. [An Introduction to Conformal Prediction](https://cml.rhul.ac.uk/copa2017/presentations/CP_Tutorial_2017.pdf) by Henrik Linusson (2017) 
🔥🔥🔥🔥
1. [Conformal prediction A Tiny Tutorial on Predicting with Confidence](https://people.dsv.su.se/~henke/DSWS/johansson.pdf) by Henrik Linusson and Ulf Johansson (2014) 🔥🔥🔥🔥
2. [A Tutorial on Conformal Predictive Distributions](https://www.youtube.com/watch?v=FUi5jklGvvo&t=3s) by Paolo Toccaceli (2020) 🔥🔥🔥
3. [Venn Predictors Tutorial](https://www.youtube.com/watch?v=KsQpkjl7u1w) by Ulf Johansson, Cecilia Sönströd, Tuve Löfström, and Henrik Boström (2021)  🔥🔥🔥🔥
4. [Ulf Johansson: Venn Predictors](https://www.youtube.com/watch?v=xxZOLo8wxe0&t=98s) by Ulf Johansson (2020)  🔥🔥🔥🔥
5.   [Conformal prediction A Tiny Tutorial on Predicting with Confidence](https://people.dsv.su.se/~henke/DSWS/johansson.pdf) by Henrik Linusson and Ulf Johansson (2014)
6.   [Conformal Prediction and Venn Predictors A Tutorial on Predicting with Confidence](https://icdatascience.org/wp-content/uploads/2019/07/ICDATA_tutorial_2019_Johansson_U.pdf) by Ulf Johansson, Henrik Linusson, Tuve Löfström, Henrik Boström, Alex Gammerman (2019) 🔥🔥🔥🔥🔥
7.   [A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification](https://arxiv.org/pdf/2107.07511.pdf) by Anastasios N. Angelopoulos and Stephen Bates (2021) [Video](https://www.youtube.com/watch?v=nql000Lu_iE&t=1786s) [Code](https://github.com/aangelopoulos/conformal-prediction) 🔥🔥🔥🔥
8.   [Introduction to Conformal Prediction](https://www.iith.ac.in/~vineethnb/indoukworkshop2015/assets/files/IntroToCP.pdf) by Vineeth N Balasubramanian (Indian Institue of Technology, Hyderabad, 2015)
9. [Conformal Prediction in Spark](https://docs.google.com/presentation/d/1eD1vUJVR3nejyJZsOMfxL-NxrLy7K2UUMSAEMHYLfek/edit#slide=id.g2276269343_0_129) by Marco Capuccini (Uppsala University, 2017)
10. [Uncertainty estimation in NLP](https://sites.google.com/view/uncertainty-nlp#h.is5zc8lcnuki) by Tal Schuster, Adam Fisch (MIT, USC, 2022) 🔥🔥🔥🔥🔥
11. [Distribution-free inference tutorial At the IFDS 2021 Summer School](https://rinafb.github.io/talks/) [Video 1](https://vimeo.com/581870072) [Video 2](https://vimeo.com/581870078)
12. [Conformal Inference Tutorial](https://bkompa.github.io/2020/09/19/Conformal-Inference-Tutorial.html) by Ben Kompa (2020)
13. [Uncertainty Quantification (1): Enter Conformal Predictors](https://www.youtube.com/watch?v=xZbuFKWV5NA&t=25s) by Mahdi Torabi Rad (2023) 🔥🔥🔥
14. [Uncertainty Quantification (2): Full Conformal Predictors](https://www.youtube.com/watch?v=R1dnPAYGwnk) by Mahdi Torabi Rad (2023) 🔥🔥🔥🔥
15. [Uncertainty Quantification (3): From Full to Split Conformal Methods](https://www.youtube.com/watch?v=YigGJfsCjDk) by Mahdi Torabi Rad (2023) 🔥🔥🔥🔥🔥
16. [Conformal Prediction in Genomics](https://github.com/BiolApps/ConformalPrediction/tree/main) by BiolApps (2023)
17. [Conformal Prediction: A Visual Introduction](https://conformal-prediction.streamlit.app/) in [VISxAI](https://visxai.io/) by Mihir Agarwal, Lalit Chandra Routhu, Zeel B Patel and Nipun Batra (IIT Gandhinagar, IIT Patna, 2023)
18. [Conformal Predictions from Scratch in Numpy](https://github.com/joneswack/conformal-predictions-from-scratch) by Jones Wacker (2023) 🔥🔥🔥🔥🔥
19. [A Tutorial on Distribution-Free Uncertainty Quantification Using Conformal Prediction (psychology)](https://journals.sagepub.com/doi/10.1177/25152459251380452) by Tim Kaiser and Philipp Herzog (Freie Universität Berlin, RPTU University Kaiserslautern-Landau, Germany, 2025).

## Conformal Prediction Courses
1. [Applied Conformal Prediction course starts in May 2024!](https://maven.com/forms/2a53e5) 🔥🔥🔥🔥🔥
2. [Uncertain: Modern topics in uncertainty estimation](https://uncertaintyclass.com) [YouTube](https://www.youtube.com/watch?app=desktop&v=M3tkM4dcIPA) [Course notes](https://www.cis.upenn.edu/~aaroth/uncertainty-notes.pdf) by Aaron Roth (University of Pennsylvania, 2022) 🔥🔥🔥🔥🔥
3. [Topics in Modern Statistical Learning](https://github.com/dobriban/Topics-In-Modern-Statistical-Learning) by Edgar Dobriban (Wharton School, University of Pennsylvania, 2022) 🔥🔥🔥🔥🔥
4. [Theory of Statistics](https://candes.su.domains/teaching/stats300c/) Stanford Statistics course by Prof Emmanuel Candes (2022) 🔥🔥🔥🔥🔥
5. [36-708 Statistical Methods for Machine Learning](https://www.stat.cmu.edu/~larry/=sml/) Carnegie-Mellon course by Prof Larry Wasserman (2022)
6. [Course on Conformal Prediction](https://mindfulmodeler.substack.com/p/e-mail-course-on-conformal-prediction) by Christoph Molnar (2022) 
7. [Conformal Prediction - Advanced Topics in Statistical Learning, Spring 2023](https://www.stat.berkeley.edu/~ryantibs/statlearn-s23/lectures/conformal.pdf) by Ryan Tibshirani (2023) 🔥🔥🔥🔥🔥
8. [Conformal Methods for Efficient and Reliable Deep Learning](https://dspace.mit.edu/handle/1721.1/152788) by Adam, Fisch (MIT, 2023) 🔥🔥🔥🔥🔥

## Books on Conformal Prediction
1. [Applied Conformal Prediction — Pro Edition](https://valeman.gumroad.com/l/applied_conformal_prediction_pro) by Dr. Valeriy Manokhin ⭐ **Recommended** — the most comprehensive edition with extended chapters, advanced methods, and production-grade code. 🔥🔥🔥🔥🔥🚀🚀🚀🚀🚀
2. [Applied Conformal Prediction — Standard Edition](https://valeman.gumroad.com/l/appliedconformalprediction) by Dr. Valeriy Manokhin — the core book covering regression, classification, time series, anomaly detection, and LLM uncertainty. 🔥🔥🔥🔥🔥
3. [Algorithmic Learning in a Random World](https://link.springer.com/book/10.1007/978-3-031-06649-8) by Vladimir Vovk, Alex Gammerman, and Glenn Shafer (2022, Second edition). 🔥🔥🔥🔥🔥 Great theory-based book, very math heavy, no applications, no code.
4. [Conformal Prediction for Reliable Machine Learning](https://www.elsevier.com/books/conformal-prediction-for-reliable-machine-learning/balasubramanian/978-0-12-398537-8) by Vineeth Balasubramanian, Shen-Shyang Ho, Vladimir Vovk (2014). Older book, largely out of date, no code.

## Articles on Conformal Prediction
1. [Measuring Models' Uncertainty: Conformal Prediction](https://blog.dataiku.com/measuring-models-uncertainty-conformal-prediction) by 
Leo Dreyfus-Schmidt (Dataiku, 2020). 🔥🔥🔥🔥🔥
1. [Conformal Prediction for Neural Regression Model](https://pkghosh.wordpress.com/2021/12/30/conformal-prediction-for-a-neural-regression-model/) by Pranab Ghosh (2021). 🔥🔥🔥🔥🔥
2. [How to Handle Uncertainty in Forecasts](https://towardsdatascience.com/how-to-handle-uncertainty-in-forecasts-86817f21bb54) by Michael Berk (2021)
3. [How to Add Uncertainty Estimation to your Models with Conformal Prediction](https://towardsdatascience.com/how-to-add-uncertainty-estimation-to-your-models-with-conformal-prediction-a5acdb86ea05) by Zachary Warnes (2021)
4. [nonconformist: An easy way to estimate prediction intervals](https://medium.com/spikelab/nonconformist-an-easy-way-to-estimate-prediction-intervals-b0ded1eb066f) by Maria Jesus Ugarte (2021).
5. [Detecting Weird Data: Conformal Anomaly Detection](https://towardsdatascience.com/detecting-weird-data-conformal-anomaly-detection-20afb36c7bcd) by Matthew Burruss (2020).
6. [How to Predict Risk-Proportional Intervals with Conformal Quantile Regression](https://towardsdatascience.com/how-to-predict-risk-proportional-intervals-with-conformal-quantile-regression-175775840dc4) by Samuele Mazzanti (2022). 🔥🔥🔥🔥🔥
7. [Stanford statisticians and Washington Post data scientists build more honest prediction models](https://news.stanford.edu/2021/03/19/honesty-statistical-models/#) Stanford (2021) 🔥🔥🔥🔥🔥
8. [How to Detect Anomalies — state-of-the-art methods using Conformal Prediction](https://valeman.medium.com/how-to-detect-anomalies-state-of-the-art-methods-using-conformal-prediction-e02691659412) by Valery Manokhin (2021) 🔥🔥🔥🔥🔥
9. [How to calibrate your classifier in an intelligent way](https://medium.com/@valeman/how-to-calibrate-your-classifier-in-an-intelligent-way-a996a2faf718) by Valery Manokhin (2022) 🔥🔥🔥🔥🔥
10. [How to predict full probability distribution using machine learning Conformal Predictive Distributions](https://medium.com/@valeman/how-to-predict-full-probability-distribution-using-machine-learning-conformal-predictive-f8f4d805e420) by Valery Manokhin (2022) 🔥🔥🔥🔥🔥
11. [How to predict quantiles in a more intelligent way (or ‘Bye-bye quantile regression, hello Conformal Quantile Regression](https://valeman.medium.com/how-to-predict-quantiles-in-a-more-intelligent-way-or-bye-bye-quantile-regression-hello-24a65e4c50f) by Valery Manokhin (2022) 🔥🔥🔥🔥🔥
12. [Conformal Prediction in Julia, Part I - Introduction](https://towardsdatascience.com/conformal-prediction-in-julia-351b81309e30) by Patrick Altmeyer (2022)
13. [How to Conformalize a Deep Image Classifier](https://towardsdatascience.com/how-to-conformalize-a-deep-image-classifier-14ead4e1a5a0) by Patrick Altmeyer (2022)
14. [Time Series Forecasting with Conformal Prediction Intervals: Scikit-Learn is All you Need](https://towardsdatascience.com/time-series-forecasting-with-conformal-prediction-intervals-scikit-learn-is-all-you-need-4b68143a027a) by Marco Cerliani (2022)
15. [Conformal Prediction in Julia, Part II - How to conformalize a deep image classifier](https://towardsdatascience.com/how-to-conformalize-a-deep-image-classifier-14ead4e1a5a0) by Patrick Altmeyer (2022)
16. [Conformal Prediction in Julia, Part III - Prediction intervals for any regression model](https://towardsdatascience.com/prediction-intervals-for-any-regression-model-306930d5ad9a) by Patrick Altmeyer (2022)
17. [Probabilistic Forecasting with Conformal Prediction and NeuralProphet](https://medium.com/@valeman/probabilistic-forecasting-with-conformal-prediction-and-neuralprophet-af9c87901d94) by Valery Manokhin (2022) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
18. [Time Series Forecasting with Conformal Prediction Intervals: Scikit-Learn is All you Need](https://towardsdatascience.com/time-series-forecasting-with-conformal-prediction-intervals-scikit-learn-is-all-you-need-4b68143a027a) by Marco Cerliani (2022) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
19. [TQA: Creating Valid Prediction Intervals for Cross-sectional Time Series Regression](https://realsunlab.medium.com/tqa-creating-valid-prediction-intervals-for-cross-sectional-time-series-regression-bd0f2260fae7) by Zhen Lin (UIUC, NeurIPS’22 paper) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
20. [Conformal Prediction: A Critic to Predictive Models](https://medium.com/@data-overload/conformal-prediction-a-critic-to-predictive-models-27501dcc76d4) (2023)
21. [Multi-horizon Probabilistic Forecasting with Conformal Prediction and NeuralProphet](https://valeman.medium.com/multi-horizon-probabilistic-forecasting-with-conformal-prediction-and-neuralprophet-5ec5af3888c8) by Valery Manokhin TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
22. [Putting clear bounds on uncertainty](https://news.mit.edu/2023/putting-clear-bounds-uncertainty-0123) (MIT, 2023)
23. [Conformal prediction theory explained](https://medium.com/low-code-for-advanced-data-science/conformal-prediction-theory-explained-14a35226df80) by Artem Ryasik (2023)
24. [Easy Distribution-Free Conformal Intervals for Time Series](https://towardsdatascience.com/easy-distribution-free-conformal-intervals-for-time-series-665137e4d907) by Michael Keith (2023)
25. [Another (Conformal) Way to Predict Probability Distributions](https://towardsdatascience.com/another-conformal-way-to-predict-probability-distributions-fcc63e78680d) by Harrison Hoffman (2023) 🔥🔥🔥🔥🔥
26. [How to use full (transductive) Conformal Prediction])(https://valeman.medium.com/how-to-use-full-transductive-conformal-prediction-7ed54dc6b72b) by Valery Manokhin (2023) 🔥🔥🔥🔥🔥
27. [Conformal Prediction for Regression](https://medium.com/@artem_ryasik/conformal-prediction-for-regression-1ba24f1442df) (using KNIME) by Artem Ryasik (2023)
28. [Dynamic Conformal Intervals for any Time Series Model](https://towardsdatascience.com/dynamic-conformal-intervals-for-any-time-series-model-d1638aa48527) by Michael Keith (2023) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
29. [Hitting Time Forecasting: The Other Way for Time Series Probabilistic Forecasting](https://towardsdatascience.com/hitting-time-forecasting-the-other-way-for-time-series-probabilistic-forecasting-6c3b6496c353) by Marco Cerliani (2023) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
31. [Stanford statisticians and Washington Post data scientists build more honest prediction models](https://news.stanford.edu/2021/03/19/honesty-statistical-models/) [Code](https://github.com/washingtonpost/elex-live-model) 🔥🔥🔥🔥🔥
32. [Jackknife+ — a Swiss knife of Conformal Prediction for regression](https://medium.com/@valeman/jackknife-a-swiss-knife-of-conformal-prediction-for-regression-ce3b56432f4f) by Valeriy Manokhin (2023) 🔥🔥🔥🔥🔥
33. [Clinical AI tools must convey predictive uncertainty for each individual patient](https://www.nature.com/articles/s41591-023-02562-7) (2023)🔥🔥🔥🔥🔥
34. [How to use Conformal Prediction](https://kiel.ai/conformal-prediction/) by Yannick Kälber (2023) 🔥🔥🔥🔥🔥
35. [Model Diagnostics: Prediction Uncertainty](https://piml.medium.com/model-diagnostics-prediction-uncertainty-990ff0bd2c4e) by PiML team, Wells Fargo (2023).
36. [Make any predictor uncertainty-aware via conformal prediction](https://mlwithouttears.com/2023/11/15/make-any-predictor-uncertainty-aware-via-conformal-prediction/) by Lorenzo Maggi (2023)
37. [Conformal predictive systems - A hands-on codeless example with KNIME](https://medium.com/low-code-for-advanced-data-science/conformal-predictive-systems-895c40bac2ca) by Artem Ryasik  (2023) 🔥🔥🔥🔥🔥
38. [Conformal prediction for classification - A hands-on codeless example with KNIME](https://medium.com/low-code-for-advanced-data-science/conformal-prediction-for-classification-6bf152abb491) by Artem Ryasik  (2023) 🔥🔥🔥🔥🔥
39. [Conformalized quantile regression](https://mlwithouttears.com/2024/01/17/conformalized-quantile-regression/) by Lorenzo Maggi (2024)
40. [Leveraging conformal prediction in Python to accelerate the renewable energy transition](https://medium.com/@icvandenende/leveraging-conformal-prediction-in-python-to-accelerate-the-renewable-energy-transition-09b5c855f69d) by Inge van den Ende (2024)
41. [Fifty (four, actually) shades of conformal prediction](https://mlwithouttears.com/2024/02/04/fifty-four-actually-shades-of-conformal-prediction/) by Lorenzo Maggi (2024)
42. [Use case adapted prediction intervals by means of conformal predictions and a custom non conformity score](https://medium.com/@arnaud.gc.capitaine/use-case-adapted-prediction-intervals-by-means-of-conformal-predictions-and-a-custom-non-conformity-b4fb28d2a4f7) by Arnaud Capitaine (2024)  🔥🔥🔥🔥🔥
43. [Prediction Intervals using Conformalized Quantile Regression](https://vincentwtrs.github.io/2024-03-06-conformal_prediction_prediction_intervals/) by Vincent Wauters (2024).
44. [Conformalized Quantile Regression for Time Series Probabilistic Forecasting](https://dataman-ai.medium.com/conformalized-quantile-regression-for-time-series-probabilistic-forecasting-85a2a1047119) by Chris Kuo (2024) 🔥🔥🔥🔥🔥
45. [Uncertainty Quantification and Why You Should Care](https://towardsdatascience.com/uncertainty-quantification-and-why-you-should-care-3f8a651f1956) by Jonte Dancker (2024)
46. [Probabilistic forecasting I: Temperature](https://stephane-degeye.medium.com/probabilistic-forecasting-i-temperature-f96ded1e7247) by Stephane Degeye (2024) 
47. [Predict CO2 emissions by vehicles with Conformal Prediction](https://medium.com/@c.giancaterino/predict-co2-emissions-by-vehicles-with-conformal-prediction-3d40a5e8c136) by Claudio Giorgio Giancaterino (2024)
48. [Exploring Adaptive and Weighted Conformal Prediction Methods in the Presence of Covariate Shift](https://blog.devgenius.io/exploring-adaptive-and-weighted-conformal-prediction-methods-in-the-presence-of-covariate-shift-38ca04029292) by Peter Tettey Yamak (2024) 🔥🔥🔥🔥🔥
49. [Embracing Uncertainty with Conformal Prediction](https://medium.com/bigdatarepublic/embracing-uncertainty-with-conformal-prediction-099f928bc183) by Robbert van Kortenhof (2024)
50. [Tidymodels and conformal prediction](https://theclarkeorbit.github.io/tidymodels-and-conformal-prediction.html) by Prasanna Bhogale (2024)
51. [Basics of conformal prediction in time series data](https://theclarkeorbit.github.io/basics-of-conformal-prediction-in-time-series-data.html) by Prasanna Bhogale (2024)
52. [Leveraging conformal prediction in Python to accelerate the renewable energy transition](https://medium.com/@icvandenende/leveraging-conformal-prediction-in-python-to-accelerate-the-renewable-energy-transition-09b5c855f69d) by Inge van den Ende (2025)

## Conformal Prediction Videos and Talks
1. [Treatment of Uncertainty in the Foundations of Probability](https://www.youtube.com/watch?v=B7E-QJ9fm4w&t=2297s) by Vladimir Vovk (Royal Holloway, UK, 2017)
2. [Large-Scale Probabilistic Prediction With and Without Validity Guarantees](https://www.youtube.com/watch?v=ksrUJdb2tA8) by Vladimir Vovk (Royal Holloway, UK, NeurIPS 2015) 🔥🔥🔥🔥🔥
3. [Conformal testing in a binary model situation](https://www.youtube.com/watch?v=RTcT4YXRdMg) by Vladimir Vovk (Royal Holloway, UK, 2021)
4. [Protected probabilistic classification](https://www.youtube.com/watch?v=MpP-3suUoLY) by Vladimir Vovk (Royal Holloway, UK, 2021)
5. [Retrain or not retrain: conformal test martingales for change-point detection](https://www.youtube.com/watch?v=4Ra5KnDEfkw&t=1s) by Vladimir Vovk (Royal Holloway, UK, 2021) 🔥🔥🔥🔥🔥
6. [A Tutorial on Conformal Prediction](https://www.youtube.com/watch?v=nql000Lu_iE&t=1786s) by Anastasios Angelopoulos and Stephen Bates (Berkeley, ICML 2021) 🔥🔥🔥🔥🔥
7. [Steps Toward Trustworthy Machine Learning](https://www.youtube.com/watch?v=2iNRSgS7-L4) by Tom Dietterich (2021)
8. [A Tutorial on Conformal Predictive Distributions](https://www.youtube.com/watch?v=FUi5jklGvvo&t=3s) by Paolo Toccaceli (Royal Holloway, UK, 2020) 🔥🔥🔥🔥🔥
9. [Conformal Prediction Tutorial](https://www.youtube.com/watch?v=0MsGri8nmJQ) by Henrik Linusson (2021) 🔥🔥🔥🔥🔥
10. [Henrik Linusson: Conformal Prediction](https://www.youtube.com/watch?v=lQxH-zXrOwI&t=1522s) by Henrik Linusson (2020)
11. [Predicting with Confidence - Henrik Boström](https://www.youtube.com/watch?v=eXU-64dwHmA) by Henrik Boström (2016)
12. [How to increase certainty in predictive modeling](https://www.youtube.com/watch?v=fQQP84yxCRs&t=1277s) by Emmanuel Candes (Stanford, 2021) 🔥🔥🔥🔥🔥
13. [Recent Progress in Predictive Inference](https://www.youtube.com/watch?v=tY73G_UvkAE&t=833s) by Emmanuel Candes (Stanford, 2020) 🔥🔥🔥🔥🔥
14. [Some recent progress in predictive inference" (Stanford) @ MAD+](https://www.youtube.com/watch?v=djgxwpJQyAA) by Emmanuel Candes (Stanford, 2020)
15. [Conformal Prediction in 2020](https://www.youtube.com/watch?v=61tpigfLHso&t=1507s) by Emmanuel Candes (Stanford, 2020) 🔥🔥🔥🔥🔥
16. [Assumption-free prediction intervals for black-box regression algorithms](https://www.youtube.com/watch?v=GMnCO7_HIOY&t=3943s) by Aaditya Ramdas (Carnegie Mellon, 2020) 🔥🔥🔥🔥🔥
17. [Maria Navarro: Quantifying uncertainty in Machine Learning predictions | PyData London 2019](https://www.youtube.com/watch?v=r6bhm_A-YcQ&t=12s) by Maria Navarro (2019)
18. [Conformal Prediction: Enhanced Method for Understanding the Prediction Quality](https://www.youtube.com/watch?v=_ZVuEWEfwuw&t=948s) by Artem Ryasik and Greg Landrum
19. [Venn Predictors Tutorial](https://www.youtube.com/watch?v=KsQpkjl7u1w) by Ulf Johansson, Cecilia Sönströd, Tuwe Löfström, and Henrik Boström (2021)
20. [Mondrian conformal predictive distributions](https://www.youtube.com/watch?v=dHNZxw8WQrs) by Henrik Boström, Ulf Johansson, and Tuwe Löfström (2021) 🔥🔥🔥🔥🔥
21. [Calibrating Multi-Class Models](https://www.youtube.com/watch?v=uCnFgTjUYto) by Ulf Johansson, Tuwe Löfström, and Henrik Boström (2021)
22. [Conformal testing in a binary model situation](https://www.youtube.com/watch?v=RTcT4YXRdMg) by Vladimir Vovk (Royal Holloway, UK, 2021)
23. [Conformal prediction in Orange](https://www.youtube.com/watch?v=qI1jOEour1g&t=14s) by Tomaž Hočevar and Blaž Zupan (2021)
24. [Distribution-Free, Risk-Controlling Prediction Sets](https://www.youtube.com/watch?v=ITJAR3fcNuI) by Anastasios Angelopoulos Berkeley, 2021) 🔥🔥🔥🔥🔥
25. [Conformal Prediction and Distribution-Free Calibration](https://synapse.math.univ-toulouse.fr/s/KDcWmmU9j9zk0rm) by Aaditya Ramdas (Carnegie Mellon, 2021) 🔥🔥🔥🔥🔥
26. [Reliable Diagnostics by Conformal Predictors](https://www.youtube.com/watch?v=zW3R-vbLw58) by Alexander Gammerman (Royal Holloway, UK, 2015)
27. [Conformal Inference of Counterfactuals and Time-to-event Outcomes](https://www.youtube.com/watch?v=nfD3mrSefbI) by Lihua Lei (Stanford, 2021)
28. [Algo Hour – Conformal Inference of Counterfactuals and Individual Treatment Effect](https://www.youtube.com/watch?v=COW2QNBmEMw) by Lihua Lei (Stanford, 2021)
29. [Conformal Inference of Counterfactuals and Individual Treatment effects(Stanford)](https://www.youtube.com/watch?v=8tM4BhONHms) by Lihua Lei (Stanford, 2021)
30. [Approximation to object conditional validity with inductive conformal predictors](https://www.youtube.com/watch?v=pUf7z2vxdi8) by Anthony Bellotti (University of Nottingham Ningbo, China, 2021)
31. [Ulf Johansson: Venn Predictors](https://www.youtube.com/watch?v=xxZOLo8wxe0&t=40s) by Ulf Johansson (Jönköping University, Sweden, 2021) 🔥🔥🔥🔥🔥
32. [Transformer-based conformal predictors for paraphrase detection](https://www.youtube.com/watch?v=HYP1ypxywWo) by Patrizio Giavannotti and Prof. Alexander Gammerman (Royal Holloway, UK, 2021)
33. [Conformal Inference of Counterfactuals and Individual Treatment Effects](https://www.youtube.com/watch?v=jkFs6pLZXBQ) by Lihua Lei (Stanford, 2020)
34. [Model-Free Predictive Inference](https://www.youtube.com/watch?v=8GkhRuWcd0w) by Larry Wasserman (Carnegie Mellon, 2020) 🔥🔥🔥🔥🔥
35. [Shapley-value based inductive conformal prediction](https://www.youtube.com/watch?v=6XUc3HFa_5Q&t=1094s) by William Lopez Jaramillo (2021)
36. [Conformal Training: Learning Optimal Conformal Classifiers | DeepMind](https://www.youtube.com/watch?v=XMa1glDpVtQ&t=318s) by David Stutz (2021) 🔥🔥🔥🔥🔥
37. [Distribution-Free, Risk-Controlling Prediction Sets](https://www.youtube.com/watch?v=z8WDmD5D-I0) by Anastasios Angelopoulos (2021) 🔥🔥🔥🔥🔥
38. [Assumption-Free, High-Dimensional Inference](https://www.youtube.com/watch?v=UOMvUaYfpH4) by Larry Wasserman (2016)
39. [Neural Predictive Monitoring under Partial Observability](https://www.youtube.com/watch?v=JhJXUDPoKCc) by Francesca Cairolli (2021)
40. [Conformalized Kernel Ridge Regression and Its Efficiency](https://www.youtube.com/watch?v=OLeu9TXE5n4) by Evgeny Burnaev (Skolkovo, Russia, 2015)
41. [Fast conformal classification using influence functions](https://www.youtube.com/watch?v=LRwm976poDE) by Giovanni Cherubin (Alan Turing Institute, UK, 2021)
42. [Valid inferential models and conformal prediction](https://www.youtube.com/watch?v=egrLw0CmXTs) by Ryan Martin (North Carolina State University, USA, 2021)
43. [Mondrian conformal predictive distributions](https://www.youtube.com/watch?v=dHNZxw8WQrs&t=1415s) by Henrik Boström, Ulf Johansson and Tuwe Löfström (KTH Royal Institute of Technology, Sweden, 2021) 🔥🔥🔥🔥🔥
44. [Evaluation of updating strategies for conformal predictive systems in the presence of extreme events](https://www.youtube.com/watch?v=Xgs0JqDw8lA) by Hugo Werner, Lars Carlsson, Ernst Ahlberg and and Henrik Boström (KTH Royal Institute of Technology, Sweden, 2021)
45. [Ulf Johansson: Venn Predictors](https://www.youtube.com/watch?v=xxZOLo8wxe0&t=98s) by Ulf Johansson (Jönköping University, Sweden, 2020) 🔥🔥🔥🔥🔥
46. [Class-wise confidence for debt prediction in real estate management](https://www.youtube.com/watch?v=ZVhA8LGXWpc) by Soundouss Messoudi (2021)
47. [How Nonconformity Functions and Difficulty of Datasets Impact the Efficiency of Conformal Classifiers](https://www.youtube.com/watch?v=lLtZkVwxMNw) by Marharyta Aleksandrova (2021)
48. [Nested conformal prediction and quantile out-of-bag ensemble methods](https://www.youtube.com/watch?v=NlUlelNWVMQ) by Chirag Gupta (Carnegie Mellon, 2020) 🔥🔥🔥🔥🔥
49. [Panel with Michael I. Jordan, Vladimir Vovk, and Larry Wasserman, moderated by Aaditya Ramdas](https://slideslive.com/38964850/panel-with-michael-i-jordan-vladimir-vovk-and-larry-wasserman-moderated-by-aaditya-ramdas?ref=account-folder-87373-folders) by Vladimir Vovk, Larry Wasserman, Michael I. Jordan, Aaditya Ramdas, ICML 2021 🔥🔥🔥🔥🔥 🔥🔥🔥🔥🔥
50. [Black-box uncertainty - Anastasios Angelopoulos](https://www.youtube.com/watch?v=jW-mbsVgcIc) by Anastasios Angelopoulos (Berkeley, USA, 2021) 🔥🔥🔥🔥🔥 
51. [P.C. Mahalanobis Memorial Lectures 2020-21](https://www.isibang.ac.in/~statmath/pcm2020/) by Vladimir Vovk (Royal Holloway, UK, 2021)
52. [Rahul Vishwakarma: New Perspective on Machine Learning Predictions Under Uncertainty | SNIA Storage Developer Conference, Santa Clara 2019](https://www.youtube.com/watch?v=T-hG1JyAk4E) by Rahul Vishwakarma (2019)
53. [Fast conformal classification using influence functions](https://www.youtube.com/watch?v=LRwm976poDE) by Umang Bhatt, Adrian Weller and Giovanni Cherubin (Cambridge / Alan Turinig Institute, 2021).
54. [Recent progress in predictive inference](https://www.youtube.com/watch?v=FQxpdMME0qU) by Emmanuel Candes, Stanford University (2022)
55. [Conformalized Survival Analysis with Adaptive Cutoffs](https://youtu.be/bvZ0SZlnkv8) by Rina Foygel Barber, Zhimei Ren, Yu Gui and Rohan Hore, University of Chicago (2022)
56. [Calibrating probabilistic hierarchical forecasts with conformal predictions](https://www.youtube.com/watch?v=VNhgk8Q1VFg) by Daan Ferdinandusse (University of Amsterdam, 2022)
57. [Michael I. Jordan on Conformal Prediction](https://www.youtube.com/watch?v=kSGP4F_ZcBY) by Michael I. Jordan (Berkeley, 2022)
58. [Distribution-free Prediction: Exchangeability and Beyond](https://www.youtube.com/watch?v=HVZDLhW8Kxg) by Rina Foygel Barber (University of Chicago, 2022)
59. [Purdue Statistics Theme Seminar, Conformal Prediction in 2022](https://www.youtube.com/watch?v=pjhp1moPvO4) by Emmanuel Candes (Stanford, 2022)
60. [WILL MY ROBOT ACHIEVE MY GOALS? PREDICTING THE PROBABILITY THAT AN MDP POLICY REACHES A USER-SPECIFIED BEHAVIOR TARGET](https://arxiv.org/pdf/2211.16462.pdf) by Alexander Guyer and Thomas G. Dietterich (University of Oregon, 2022)
61. [Robust and Equitable Uncertainty Estimation](https://www.youtube.com/watch?v=Iznj13jP9ag) by Aaron Roth(2022)
62. [Conformal prediction under feedback covariate shift for biomolecular design](https://www.youtube.com/watch?v=AOyDjBSQjhk) by Clara Wong-Fannjiang (Berkeley, 2022)
63. [Conformal prediction in 2022](https://slideslive.com/38996063/conformal-prediction-in-2022?ref=speaker-43789) invited talk by Emmanuel Candes at NeurIPS2022 🔥🔥🔥🔥🔥
64. [Broadening the Scope of Conformal Inference](https://slideslive.com/38988210/broadening-the-scope-of-conformal-inference?ref=search-presentations-Conformal+prediction) by Michael I. Jordan (University of Berkeley, 2022) 🔥🔥🔥🔥🔥
65. [Paper Reading Group - Fortuna, a Library for Uncertainty Quantification](https://www.youtube.com/watch?app=desktop&v=S_QgP3jBCqw)
66. [CLIMB Evergreen talk with Emmanuel Candès: Conformal Inference when Data is not Exchangeable](https://www.youtube.com/watch?v=D60vtpnkhTU) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
67. [Algo Hour – Conformal Inference of Counterfactuals and Individual Treatment Effects | Lihua Lei](https://www.youtube.com/watch?v=COW2QNBmEMw&t=2s)
68. ['MoroccoAI webinar - Dr. Soundouss Messoudi - 'Confidence learning using conformal prediction'](https://www.youtube.com/watch?v=SypbjiBrt3Q)
69. [Emmanuel Candes - A Taste of Conformal Prediction](https://www.carmin.tv/en/video/a-taste-of-conformal-prediction) by Emmanuel Candes (2023)
70. [Foundations of Conformal Prediction - Full Conformal Predictors](https://www.youtube.com/watch?v=R1dnPAYGwnk) by Mahdi Torabi Rad (2023) 🔥🔥🔥🔥🔥
71. [Max Mergenthaler and Fede Garza - Quantifying Uncertainty in Time Series Forecasting](https://www.youtube.com/watch?v=Bj1U-Rrxk48) by Max Mergenthaler and Fede Garza (Nixtla, 2023) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
72. [Uncertainty Quantification with the Fortuna library by Gianluca Detommaso (AWS)](https://www.youtube.com/watch?v=FEtD6lnsI58) by Gianluca Detommaso (Amazon, 2023)
73. [Quantifying Uncertainty in Time Series Forecasting](https://www.youtube.com/watch?v=Bj1U-Rrxk48) by Max Mergenthaler and Fede Garza (Nixtla, 2023)
74. [NISS/Merck Meetup on Conformal Inference: Advancing the Boundaries of Machine Learning 4.19.2023](https://www.youtube.com/watch?v=SRbqUae9-_o&t=5631s) (2023) 🔥🔥🔥🔥🔥
75. [Max Kuhn - The Post-Modeling Model to Fix the Model](https://www.youtube.com/watch?v=3omi4lm1da0) by Max Kuhn (2023)🔥🔥🔥🔥🔥
76. [ISDFS Talk: Robots that ask for help: Conformal Prediction for LLM Planners](https://www.youtube.com/watch?v=WnQopZKJsTw) by Anirudha Majumdar (Princeton/DeepMind) 🔥🔥🔥🔥🔥(2023)
77. [Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners](https://www.youtube.com/watch?v=xvXrPdPb3Ko) by Allen Z Ren (2023) 🔥🔥🔥🔥🔥
78. [Three Easy Steps to Understand Conformal Prediction (CP), Conformity Score, Python Implementation](https://www.youtube.com/watch?v=oqK6rM8fbkk) by (Dr. Data Science 2023) 🔥🔥🔥🔥🔥
79. [Rising Stars #8: Clara Wong-Fannjiang (Genentech) - Prediction-Powered Inference](https://www.youtube.com/watch?v=TlFpVpFx7JY)
80. [Rising Stars #10 - Special Series on Conformal Prediction: Isaac Gibbs (Stanford University) Conformal Inference with Conditional Guarantees](https://www.youtube.com/watch?v=rvYnR0FGxM4)
81. [Conformal Prediction for Time Series with Modern Hopfield Networks](https://www.youtube.com/watch?v=QhvLaZ1aS6A) by Andreas Auer TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
82. [Introducing Sequential Predictive Conformal Inference (SPCI)](https://www.youtube.com/watch?v=NQHrTMZ2-XA&t=346) by Chen Xu (2023) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
83. [Conformal Prediction Intervals: Empowering Executives for Informed Decision](https://www.youtube.com/watch?v=3StianQJZTk&t=26s) by Matthew Kolakowski (2023) 🔥🔥🔥🔥🔥
84. [Conformal Inference with Tidymodels - posit::conf(2023)](https://www.youtube.com/watch?v=vJ4BYJSg734) by Max Kuhn (2023)
85. [ACon^2: Adaptive Conformal Consensus for Provable Blockchain Oracles](https://www.youtube.com/watch?v=8PwDHAITuwU) by Sangdon Park (2023)
86. [Leveraging conformal prediction for calibrated probabilistic time series forecast](https://www.youtube.com/watch?v=--WcrDRtrYk) by Inge van den Ende (Dexter Energy, 2023) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
87. [Uncertainty Quantification over Graph with Conformalized Graph Neural Networks](https://www.youtube.com/watch?v=Yq9cvqEk2K8&t=8s) by Kexin Huang (Stanford, 2023)  🔥🔥🔥🔥🔥
88. [Selection by Prediction with Conformal p-values](https://www.youtube.com/watch?v=VHcCmkChwTk&t=5s) by Ying Jin (Stanford, 2023)
89. [Trustworthy Retrieval Augmented Chatbots Utilizing Conformal Predictors](https://www.youtube.com/watch?v=JnWXebWUEg4) by Shuo Li (UPenn, 2023).
90. [An introduction to conformal prediction - PyLadies Amsterdam](https://www.youtube.com/watch?v=QFtdTyIWrz8) by Inge van den Ende (2024) 🔥🔥🔥🔥🔥[code](https://github.com/pyladiesams/conformal-prediction-jan2024)
91. [Anushri Dixit - Planning with Confidence: Uncertainty Quantification for Safety-Critical Tasks](https://www.youtube.com/watch?v=hhSejSXde6U) (2024) 🔥🔥🔥🔥🔥
92. [Analítica acelerada con Shapelets y conformal prediction, ~48 mins onwards](https://www.youtube.com/watch?v=4HxTUzPyK9g&t=4854s) by Carl McBride Ellis (2024) [code](https://github.com/Carl-McBride-Ellis/talks) 🔥🔥🔥🔥🔥
93. [Conformal Quantile Estimation in Economics](https://www.youtube.com/watch?v=6Brjt6aM140) by Martin Fankhauser (Bocconi, 2024)
94. [Big Data: 4th lecture (uncertainty in learning, big data for NLP)](https://www.youtube.com/watch?v=ikFkHig5o6g&list=PL8n4sZAL72Dn8GXuC0x9aXyiVGVAbPHz3&index=6) by Prof. Patrick Glauner (2024)
95. [Unveiling Precision: A Novel ML Framework for Accurate Probability Estimates by Abel and Edgar](https://www.youtube.com/watch?v=MuecMDKPqTQ&t=1672s), not CP per se, showing the critical importance of calibration in finance (2024)
96. [Autonomy Talks - Somil Bansal: Safety Assurances for Learning-Enabled Autonomous Systems](https://www.youtube.com/watch?v=3f8Q19-BqRo) by Somil Bansal (USC, 2024) 🔥🔥🔥🔥🔥
97. [Interview with Vladimir Vovk on Conformal Inference](https://www.youtube.com/watch?v=J7o2WJX_xQE) (2024)
98. [Error Embraced: Making Trustworthy Scientific Decisions with Imperfect Predictions](https://www.youtube.com/watch?v=oqLq-DUEP3s) by Clara Wong-fannjiang (Genentech) (2024)
99. [Conformalized Interval Arithmetic with Symmetric Calibration](https://arxiv.org/abs/2408.10939) by Rui Luo, Zhixin Zhou (City University of Hong Kong, 2024)
100. [Robust Yet Efficient Conformal Prediction Sets](https://www.youtube.com/watch?v=b5I_R3S2SdI) by  Soroush H. Zargarbash (2024)
101. [Applications of Conformal Prediction in Medicine | CGSI 2024](https://www.youtube.com/watch?v=xq3utQ12pzM) by Ahmed Alaa (2024)
102. [Mojtaba Farmanbar - Uncertainty quantification: How much can you trust your machine learning model?](https://www.youtube.com/watch?v=sKGtZyVyMM0) by Mojtaba Farmanbar (2024)
103. [Understanding, Generating, and Evaluating Prediction Intervals - posit conf 2024](https://www.youtube.com/watch?v=QT3SsD1kTj8) by Bryan Shalloway (2024)
104. [Install TorchCP Locally - Python Toolbox for Conformal Prediction on Deep Learning Models](https://www.youtube.com/watch?v=kdLnlafHAMI&t=307s) by Fahd Mirza (2024)
105. [Conformal Prediction: uncertainty quantification to humanise models](https://www.youtube.com/watch?v=EJVD-jU1A44) by Vincenzo Ventriglia (2025) 🔥🔥🔥🔥🔥
109.

## Conformal Prediction Presentation Slides
1. [Machine Learning for Probabilistic Prediction, Seattle Artificial Intelligence Workshops Meetup](https://www.researchgate.net/publication/371566526_Machine_Learning_for_Probabilistic_Prediction) by Valery Manokhin, 2023 🔥🔥🔥🔥🔥
2. [Machine Learning for Probabilistic Prediction](https://github.com/valeman/awesome-conformal-prediction/blob/main/assets/Machine%20Learning%20for%20Probabilistic%20Prediction.pdf) by Valery Manokhin, 2022 🔥🔥🔥🔥🔥
3. [Adaptive Conformal Anomaly Detection for Time-series](https://cml.rhul.ac.uk/copa2017/presentations/burnaev.pdf) by Evgeny Burnaev, Alexander Bernstein, Vlad Ishimtsev and Ivan Nazarov (Skoltech, Moscow, Russia, 2017)
4. [Nonparametric predictive distributions based on conformal prediction](https://cml.rhul.ac.uk/copa2017/presentations/vovk.pdf) by Vladimir Vovk, Jieli Shen, Valery Manokhin, Min-ge Xie, Ilia Nouretdinov and Alex Gammerman (Royal Holloway, University of London Rutgers University, 2017)
5. [What Can Conformal Inference Offer to Statistics?](https://lihualei71.github.io/Job_Talk_Lihua_Lei.pdf) by Lihua Lei, Stanford University
6. [Conformal Regressors and Predictive Systems – a Gentle Introduction](https://copa-conference.com/presentations/COPA_2022_Presentation__Conformal_Regressors_and_Predictive_Systems___a_Gentle_Introduction.pdf) by Henrik Bostroem (KTH, Sweden, 2022)
7. [Applications of Conformal Predictors](https://copa-conference.com/presentations/lars_ernst.pdf) by Ernst Ahlberg and Lars Carlsson (Stena Line, 2022)
8. [crepes: a Python Package for Conformal Regressors and Predictive Systems](https://copa-conference.com/presentations/COPA_2022_Presentation__crepes.pdf) by Henrik Bostroem (KTH, Sweden, 2022)
9. [Assessing Explanation Quality by Venn Prediction](https://copa-conference.com/presentations/amr.pdf) by Amr Alkhatib, Henrik Boström and Ulf Johansson (2022)
10. [Well-Calibrated Rule Extractors](https://copa-conference.com/presentations/Johansson_U_COPA2022_pres.pdf) by Ulf Johansson, Tuwe Löfström, Niclas Ståhl (2022)
11. [Calibration of Natural Language Understanding Models with Venn-ABERS Predictors](Calibration of Natural Language Understanding Models with Venn-ABERS Predictors](https://copa-conference.com/presentations/patrizio.pdf) by Patrizio Giovannotti (2022)
12. [Reinforcement Learning Prediction Intervals with Guaranteed Fidelity](https://web.engr.oregonstate.edu/~tgd/talks/dietterich-caml-rl-prediction-intervals.pdf) by Thomas Dietterich (University of Oregon, 2022)
13. [Conformal Prediction beyond exchangeability](https://copa-conference.com/presentations/conformal_UAI_tutorial_2.pdf) by Rina Foygel Barber (University of Chicago, 2022) 🔥🔥🔥🔥🔥
14. [Split conformal prediction for dependant data](http://www.im.ufrj.br/~coloquiomea/apresentacoes/orenstein_2022.pdf) by Roberto I. Oliveira, Paulo Orenstein, Thiago Ramos and João Vitor Romano (2022)
15. [Conformal prediction of small-molecule drug resistance in cancer cell lines](https://copa-conference.com/presentations/saiveth.pdf) by Saiveth Hernandez-Hernandez, Sachin Vishwakarma and Pedro Ballester
16. [Sequential Predictive Conformal Inference for Time Series](https://arxiv.org/pdf/2212.03463.pdf) by Chen Xu, Yao Xie (Georgia Tech, 2022) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
17. [Copula Conformal Prediction for Multi-step Time Series Forecasting](https://arxiv.org/abs/2212.03281) by Sophia Sun, Rose Yu (University of California, San Diego, 2022)
18. [Uncertainty estimation in NLP](https://sites.google.com/view/uncertainty-nlp#h.is5zc8lcnuki) by Tal Schuster, Adam Fisch (MIT, 2022)
19. [Conformal Prediction: an Introduction](https://github.com/online-ml/river/files/10098389/Conformal_Prediction_Presentation.pdf) by Leo Andeol (2022)
20. [EnbPI poster](https://github.com/valeman/awesome-conformal-prediction/blob/main/assets/EnbPI_poster.pdf) by Chen Xu, Yao Xie (2021)
21. [Machine Learning for Probabilistic Prediction](https://www.researchgate.net/publication/370012303_Machine_Learning_for_Probabilistic_Prediction) by Valery Manokhin (2023) 🔥🔥🔥🔥🔥
22. [Conformal Inference with Tidymodels](https://topepo.github.io/posit-2023-conformal/#/title-slide) by Max Kuhn (posit conference 2023) 🔥🔥🔥🔥🔥
23. [Graceful handling of large imbalanced datasets using Conformal Prediction](https://bigchem.eu/sites/default/files/AZ_school_Norinder_public.pdf) by Ulf Norinder and Fredrik Svensson 🔥🔥🔥🔥🔥
24. [Conformalized Quantile Regression](https://arxiv.org/abs/1905.03222) by Yaniv Romano, Evan Patterson, Emmanuel J. Candès (Stanford, 2019)
25. [Leveraging Conformal Prediction for Calibrated Probabilistic Time Series Forecasts to Accelerate the Renewable Energy Transition](https://speakerdeck.com/ingevandenende/leveraging-conformal-prediction-for-calibrated-probabilistic-time-series-forecasts-to-accelerate-the-renewable-energy-transition) by Inge van den Ende (Dexter Energy, 2023).  TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
26. [Application of Conformal Inference in High Energy Physics](https://indico.phys.ethz.ch/event/113/contributions/863/attachments/528/1129/NPML2024_JF_final2.pdf) by Jiri Franc (CTU Prague,Czech Republic)

---

## 🛠 Open-Source Libraries and Tools

## Conformal Prediction Libraries in Python
1. [TorchCP - A library for conformal prediction](https://github.com/ml-stat-Sustech/TorchCP) 🔥🔥🔥🔥🔥
3. [Python implementation of binary and multi-class Venn-ABERS calibration](https://github.com/ip200/venn-abers) by Ivan Petej (2023) [Paper] 🔥🔥🔥🔥
4. [Conformal Tights - A scikit-learn meta-estimator that adds conformal prediction of coherent quantiles and intervals to any scikit-learn regressor](https://github.com/radix-ai/conformal-tights) by Laurent Sorber (Radix AI) (2024) 🔥🔥🔥🔥🔥
5. [Puncc (Predictive uncertainty calibration and conformalization)](https://github.com/deel-ai/puncc) [paper](https://proceedings.mlr.press/v204/mendil23a/mendil23a.pdf) [slides](https://copa-conference.com/presentations/COPA_2023_mouhcine_mendil_puncc.pdf) 🔥🔥🔥🔥🔥
6. [ConformaSight Global Explainer Package 📦](https://github.com/rabia174/ConformaSight) by Fatıma Rabia Yapıcıoğlu (2025)
7. [unquad - Conformal Anomaly Detection](https://github.com/OliverHennhoefer/unquad) 🔥🔥🔥🔥🔥
8. [Puncc (Predictive uncertainty calibration and conformalization)](https://github.com/deel-ai/puncc) [paper](https://proceedings.mlr.press/v204/mendil23a/mendil23a.pdf) [slides](https://copa-conference.com/presentations/COPA_2023_mouhcine_mendil_puncc.pdf) 🔥🔥🔥🔥🔥
9. [Nixtla mlforecast](https://nixtlaverse.nixtla.io/mlforecast/) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
10.   [Nixtla statsforecast](https://nixtla.github.io/statsforecast/docs/tutorials/conformalprediction.html#introduction) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
11.    [Conformal Impact](https://github.com/tblume1992/ConformalImpact) by Tyler Blume (2024) 🔥🔥🔥🔥🔥
10.[Nonconformist](https://github.com/donlnz/nonconformist) by Henrik Linusson (2015) 🚨 The library does not seem to be actively maintained 
1.  [Venn-ABERS Predictor](https://github.com/ptocca/VennABERS) by Paolo Toccaceli (2019) [Paper](https://proceedings.neurips.cc/paper/2015/hash/a9a1d5317a33ae8cef33961c34144f84-Abstract.html) 🔥🔥🔥🔥🔥
2. [Conformalized Quantile Regression](https://github.com/yromano/cqr) by Yaniv Romano (2019) 🔥🔥🔥🔥🔥
3. [Orange3 Conformal Prediction](https://github.com/biolab/orange3-conformal)[Multi-class-probabilistic-classification using Venn-ABERS (Conformal) prediction](https://github.com/valeman/Multi-class-probabilistic-classification) by Valery Manokhin (Royal Holloway, 2022)
4. [Copula Conformal Multi Target Regression](https://github.com/M-Soundouss/CopulaConformalMTR) by Soundouss Messoudi (2021)
5. [Conformalized density- and distance-based anomaly detection in time-series data (KNN-CAD)](https://github.com/numenta/NAB/tree/master/nab/detectors/knncad) by Evgeny Burnaev, Vladislav Ishimtsev (2016). Top #3 winning solution in Numenta competition 🔥🔥🔥🔥🔥
6. [Conformal time-series forecasting](https://github.com/kamilest/conformal-rnn) by Kamile ̇ Stankeviciute (Cambridge, NeurIPS 2021) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
7.  [EnbPI](https://github.com/hamrel-cxu/EnbPI) by Chen Xu (2021) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥 [Paper](https://proceedings.mlr.press/v139/xu21h.html)
8.   [Conformal learning from scratch](https://github.com/marharyta-aleksandrova/conformal-learning/blob/main/theory/conformal_learning_from_scratch.ipynb) by Marharyta Aleksandrova (2021)
9.   [Ensemble Conformalized Quantile Regression for Probabilistic Time Series Forecasting](https://github.com/FilippoMB/Ensemble-Conformalized-Quantile-Regression) Vilde Jensen, Filippo Maria Bianchi and Stian Norman Anfinsen (2022) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
10.   [Conformalized Online Learning: Online Calibration Without a Holdout Set](https://github.com/Shai128/rci) by Shai Feldman, Stephen Bates and Yaniv Romano (2022). TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
11.   [PySloth - Python package for Probabilistic Prediction](https://github.com/PySloth/pysloth) by Valery Manokhin 🚀🚀🚀🚀🚀 🔥🔥🔥🔥
12. [Conformal Prediction in KNIME](https://hub.knime.com/tuwelofstrom/spaces/Predicting%20with%20Confidence/latest/~h8R_oa6iPRTssrYs/) by Tuwe Löfström and Redfield AB (2022)
13. [Nonconformist](https://github.com/donlnz/nonconformist) by Henrik Linusson (2015) 🔥🔥🔥🔥🔥
14. [SKTime](https://www.sktime.net/en/latest/api_reference/auto_generated/sktime.forecasting.conformal.ConformalIntervals.html) by Franz Kiraly (2022)
15. [NeuralProphet](https://github.com/ourownstory/neural_prophet/blob/main/tutorials/feature-use/uncertainty_conformal_prediction.ipynb) (2022) 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
16. [River](https://github.com/online-ml/river/blob/0506ad73e45403638f13d66c6b2d71920d307461/river/conf/jackknife.py#L9) 2022
17. [TorchUQ](https://github.com/TorchUQ/torchuq/blob/5335c5948385c7b9bde4baefc9399d79a7cb07ef/docs/tutorials/1_c_1_conformal/1_c_1_conformal.rst#L17) (2022)
18. [https://github.com/mikekeith52/scalecast](https://github.com/mikekeith52/scalecast) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
19. [plot_utils - Plotting library for conformal prediction metrics, intended to facilitate fast testing in e.g. notebooks](https://github.com/pharmbio/plot_utils) 🔥🔥🔥🔥🔥
20. [calibrated-explanations - Calibrated Explanations for Machine Learning Models using Venn-Abers and Conformal Predictive Systems](https://github.com/Moffran/calibrated_explanations) by Helena Löfström (2023)
21. [Conformers - Unofficial Conformal Language Modelling library](https://github.com/Bradley-Butcher/Conformers/) 🚀🚀🚀🚀
22. [Conformal Predictions from Scratch in Numpy](https://github.com/joneswack/conformal-predictions-from-scratch) by Jones Wacker (2023) 🔥🔥🔥🔥🔥
23. [Conformal Prediction for Digital Soil Mapping](https://github.com/nafisehkakhani/Conformal_Prediction_DSM) by Nafiseh Kakhani (2023)
24. [conformal-prediction-jan2024 - PyLadies Amsterdam](https://github.com/pyladiesams/conformal-prediction-jan2024) by Inge van den Ende (2024) 🔥🔥🔥🔥🔥
25. [MFLES - Gradient Boosted Decomposition for time series forecasting](https://github.com/tblume1992/MFLES) by Tyler Blume (2024) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
26. [confopt - A Library for Conformal Hyperparameter Tuning](https://github.com/rick12000/confopt) by Ricardo Doyle (2024) [paper](https://arxiv.org/abs/2207.03017) 🔥🔥🔥🔥🔥
27. [crepes-weighted Extension of crepes package, to enable weighted conformal prediction and conformal predictive systems that can handle covariate shifts](https://github.com/predict-idlab/crepes-weighted 🔥🔥🔥🔥🔥
28. [pearsonify - Lightweight Python package for generating classification intervals in binary classification tasks using Pearson residuals and conformal prediction](https://github.com/xRiskLab/pearsonify) (2025)
29. [HyperConformal: Conformal Prediction for Hyperdimensional Computing](https://github.com/danieleschmidt/HyperConformal)  🔥🔥🔥🔥🔥 (2025)
30. [(F)FCP : Predictive Inference with (Fast) Feature Conformal Prediction](https://github.com/ElvisWang1111/F-F-CP) 🔥🔥🔥🔥🔥 (2026)

## Conformal Prediction Libraries in R
1. [pintervals - Model agnostic prediction intervals](https://github.com/Doktorandahl/pintervals) [paper](https://arxiv.org/abs/2601.03994) by David Randahl, Anders Hjort, Jonathan P. Williams (2026) 🔥🔥🔥🔥🔥 
2.  [Conformal Prediction ih tidymodels](https://github.com/tidymodels/tidymodels.org/pull/23) by Max Kuhn (Posit/RStudio, 2023) [video](https://www.youtube.com/watch?v=3omi4lm1da0) 🔥🔥🔥🔥🔥
3.  [Modeltime](https://github.com/business-science/modeltime/issues/173#issuecomment-1664681578) (2023) by Matt Dancho (Business Science, 2023) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
4.  [Conformal prediction for 80+ classes of `R` models with the `marginaleffects` package](https://marginaleffects.com/articles/conformal.html) by Vincent Arel-Bundock (2023)  🔥🔥🔥🔥🔥
5. [conformalForecast](https://github.com/xqnwang/conformalForecast) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥 (2024)
6. [AdaptiveConformal](https://github.com/herbps10/AdaptiveConformal) (2023) [paper](https://hal.science/hal-04316544/) 🔥🔥🔥🔥🔥
7. [Conformal Inference R Project](https://github.com/ryantibs/conformal) maintained by Ryan Tibshirani (2016) 🔥🔥🔥🔥🔥
8. [Prediction Bands](https://github.com/rizbicki/predictionBands) by Rafael Izbicki and Benjamin LeRoy (2019)
9. [Conformal: an R package to calculate prediction errors in the conformal prediction framework](https://github.com/isidroc/conformal/) by Isidro Cortes, 2019
10. [Online Time Series Anomaly Detectors](https://github.com/valeman/otsad) by Alaine Iturria, 2021 🔥🔥🔥🔥🔥
11. [piRF - Prediction Intervals for Random Forests](https://github.com/chancejohnstone/piRF) by Chancellor Johnstone and Haozhe Zhang (2019)
12. [conformalClassification: Transductive and Inductive Conformal Predictions for Classification Problems](https://cran.r-project.org/web/packages/conformalClassification/) by Niharika Gauraha and Ola Spjuth (2019)
13. [R Package for Spatial Conformal Prediction](https://github.com/mhuiying/scp)
14. [Conformal: an R package to calculate prediction errors in the conformal prediction framework](https://github.com/isidroc/conformal/) by Isidro Cortes, 2019
15. [cfsurvival - An R package that implements the conformalized survival analysis methodology](https://zhimeir.github.io/cfsurvival/index.html) [Paper](https://arxiv.org/abs/2103.09763)
16. [ClusTorus: An R Package for Prediction and Clustering on the Torus by Conformal Prediction](https://journal.r-project.org/articles/RJ-2022-032/RJ-2022-032.pdf) by Seungki Hong and Sungkyu Jung (2022)
17. [conformal glm - conformal prediction for generalized linear regression models](https://github.com/DEck13/conformal.glm) by Daniel Eck (2019)
18. [caretForecast - Conformal Time Series Forecasting Using State of Art Machine Learning Algorithms](https://github.com/Akai01/caretForecast)
19. [Localized Conformal Prediction - LCP](https://github.com/LeyingGuan/LCP) 
20. [conformalbayes - Jackknife(+) Predictive Intervals for Bayesian Models](https://github.com/CoryMcCartan/conformalbayes) (2022)
21. [conformal.fd Conformal inference prediction regions for Multiple Functional response regression](https://github.com/paolo-vergo/conformal.fd) (2021)
22. [cRepes-R, R implementation of Python crepes package - Conformal prediction for regression, classification, and predictive systems](https://github.com/tuvelofstrom/cRepes-R)

## Conformal Prediction Libraries in Julia
1. [ConformalPrediction.jl](https://github.com/pat-alt/ConformalPrediction.jl) by Patrick Altmeyer (2022) [Article - Conformal Prediction in Julia, Part I - Introduction](https://towardsdatascience.com/conformal-prediction-in-julia-351b81309e30) [Article - Conformal Prediction in Julia, Part II - How to conformalize a deep image classifier](https://towardsdatascience.com/how-to-conformalize-a-deep-image-classifier-14ead4e1a5a0) [Article -  Conformal Prediction in Julia, Part III - Prediction intervals for any regression model](https://towardsdatascience.com/prediction-intervals-for-any-regression-model-306930d5ad9a) 
2. [RandomForest](https://github.com/henrikbostrom/RandomForest) by Henrik Boström (2017) 🔥🔥🔥🔥🔥
3. [PostForecasts.jl](https://github.com/lipiecki/PostForecasts.jl) by Arkadiusz Lipiecki and Rafal Weron (2025) [paper](https://ideas.repec.org/p/ahh/wpaper/worms2502.html) [paper](https://www.sciencedirect.com/science/article/pii/S2352711025001670?via%3Dihub)

## Conformal Prediction in Other Languages
1. [LibCP -- A Library for Conformal Prediction](https://github.com/fated/libcp) 🔥🔥🔥🔥🔥
2. [An Implementation of Venn-ABERS predictor](https://github.com/fated/venn-abers-predictor) 🔥🔥🔥🔥🔥
3. [LibVM -- A Library for Venn Machine](https://github.com/fated/libvm)
4. [Scala-CP](https://github.com/mcapuccini/scala-cp) by Marco Capuccini (2017)' 🔥🔥🔥🔥🔥 (see tutorial section 'Conformal Prediction in Spark')

## AI Platforms Using Conformal Prediction
1. [Conformal Prediction in Knime](https://copa-conference.com/papers/COPA2022_paper_8.pdf) [Presentation](https://copa-conference.com/presentations/tuwe_presentation.pdf) 🔥🔥🔥🔥🔥
2. [Data Robot - Prediction Intervals via Conformal Inference](https://www.datarobot.com/ai-accelerators/prediction-intervals-via-conformal-inference/)
3. [AWS Fortuna](https://aws-fortuna.readthedocs.io/en/latest/) by Amazon, (2022) 🔥🔥🔥🔥🔥
4. [Microsoft Azure](https://learn.microsoft.com/en-gb/archive/blogs/machinelearning/anomaly-detection-using-machine-learning-to-detect-abnormalities-in-time-series-data)

## Conformal Prediction on Kaggle
1. [Kaggle Notebook showcasing Conformal Predictive Distributions on Playground Series Season 3, Episode 1 (California Housing data) competition](https://www.kaggle.com/code/predaddict/conformal-predictive-distributions-pss3-e1) by Valeriy Manokhin (2022)
2. [Kaggle Notebook showcasing Venn-ABERs Conformal Prediction on Playground Series Season 3, Episode 2 (Stroke prediction) competition](https://www.kaggle.com/predaddict/pss-3-episode-2-jan-2023-stroke-prediction/) by Valeriy Manokhin (2022)
3. [Classifier calibration using Venn-ABERS](https://www.kaggle.com/code/carlmcbrideellis/classifier-calibration-using-venn-abers) by Carl McBride Ellis (2024) 🔥🔥🔥🔥🔥
4. [CPB: The Crucial Calibration Set](https://www.kaggle.com/code/elainedazzio/cpb-the-crucial-calibration-set) by L. Elaine Dazzio (2025)
5. [Simplest Conformal Prediction Example](https://www.kaggle.com/code/elainedazzio/simplest-conformal-prediction-example) by L. Elaine Dazzio (2025)

---

## 📚 Research: Papers and Theses

## Conformal Prediction Papers
1. [Classifier Calibration at Scale: An Empirical Study of Model-Agnostic Post-Hoc Methods](https://arxiv.org/abs/2601.19944) by Valeriy Manokhin and Daniel Grønhaug (2026) 🔥🔥🔥🔥🔥🚀🚀🚀🚀🚀
2. [The Manokhin Probability Matrix: A Diagnostic Framework for Classifier Probability Quality](https://zenodo.org/records/19372589) by Valeriy Manokhin (2026) 🔥🔥🔥🔥🔥
3. [A Review and Comparative Analysis of Univariate Conformal Regression Methods](https://proceedings.mlr.press/v266/bao25a.html) by Jie Bao, Nicolò Colombo, Valeriy Manokhin, Suqun Cao, Rui Luo (COPA 2025) 🔥🔥🔥🔥🔥
4. [Cross-conformal predictive distributions](http://proceedings.mlr.press/v91/vovk18a.html) by Vladimir Vovk, Ilia Nouretdinov, Valeriy Manokhin and Alexander Gammerman (Royal Holloway, UK, 2018) 🔥🔥🔥🔥🔥
5. [Nonparametric predictive distributions based on conformal prediction](https://link.springer.com/article/10.1007%2Fs10994-018-5755-8) by Vladimir Vovk, Jieli Shen, Valeriy Manokhin and Min-ge Xie (Royal Holloway, UK / Rutgers, USA, 2018) 🔥🔥🔥🔥🔥
6. [Conformal predictive distributions with kernels](https://arxiv.org/abs/1710.08894) by Vladimir Vovk, Ilia Nouretdinov, Valeriy Manokhin, Alex Gammerman (Royal Holloway, UK, 2017) 🔥🔥🔥🔥🔥
7. [Multi-class probabilistic classification using inductive and cross Venn–Abers predictors](https://proceedings.mlr.press/v60/manokhin17a.html) by Valeriy Manokhin (Royal Holloway, UK, 2017) 🔥🔥🔥🔥🔥
8. [Computationally efficient versions of conformal predictive distributions](https://arxiv.org/abs/1911.00941) by Vladimir Vovk, Ivan Petej, Ilia Nouretdinov, Valeriy Manokhin, Alex Gammerman (Royal Holloway, UK, 2019) 🔥🔥🔥🔥🔥
9. [Introducing Conformal Prediction in Predictive Modeling. A Transparent and Flexible Alternative to Applicability Domain Determination](https://pubs.acs.org/doi/10.1021/ci5001168) by Ulf Norinder, Lars Carlsson, Scott Boyer, and Martin Eklund (2014)
10. [Uncertainty Sets for Image Classifiers using Conformal Prediction](https://arxiv.org/pdf/2009.14193.pdf) by Anastasios N. Angelopoulos, Stephen Bates, Jitendra Malik, & Michael I. Jordan (Berkeley, 2021) 🔥🔥🔥🔥🔥
11. [Conformal Prediction Under Covariate Shift](https://arxiv.org/abs/1904.06019) by Ryan Tibshirani, Rina Foygel Barber, Emmanuel Candes, Aaditya Ramdas (Carnegie Mellon, Stanford, Chicago, 2019) 🔥🔥🔥🔥🔥
12. [Regression Conformal Prediction with Nearest Neighbours](https://arxiv.org/pdf/1401.3880.pdf) by Harris Papadopoulos, Vladimir Vovk and Alex Gammerman (Royal Holloway, UK, 2014) 🔥🔥🔥🔥🔥
13. [Nested conformal prediction and quantile out-of-bag ensemble methods](https://arxiv.org/pdf/1910.10562.pdf) by Chirag Gupta, Arun Kuchibhotla and Aaditya  Ramdas (Carnegie Mellon, 2021) 🔥🔥🔥🔥🔥
14. [Criteria of Efficiency for Conformal Prediction](https://arxiv.org/pdf/1603.04416.pdf) by Vladimir Vovk, Ilia Nouretdinov, Valentina Fedorova,
Ivan Petej, and Alex Gammerman ((Royal Holloway, UK, 2016)
15. [Conformal Prediction for Simulation Models](https://benjaminleroy.github.io/documents/icml2021/conformal_prediction_for_simulation_models.pdf) by Benjamin LeRoy and Chad Schafer (Carnegie Mellon, 2021)
16. [Distribution-free, risk-controlling prediction sets](https://arxiv.org/pdf/2101.02703) Stephen Bates, Anastasios Angelopoulos, Lihua Lei, Jitendra Malik and  Michael I Jordan (Berkeley, 2021) 🔥🔥🔥🔥🔥
17. [Conditional calibration for false discovery rate control under dependence](https://arxiv.org/abs/2007.10438) by William Fithian and Lihua Lei (Stanford, 2021)
18. [Regression conformal prediction with random forests](https://link.springer.com/content/pdf/10.1007%2Fs10994-014-5453-0.pdf) by Ulf Johansson, Henrik Boström,  Tuve Löfström and Henrik Linusson (2014)
19. [A conformal prediction approach to explore functional data](https://arxiv.org/pdf/1302.6452.pdf) by Jing Lei, Alessandro Rinaldo, Larry Wasserman (Carnegie Mellon, 2013)
20. [An electronic nose-based assistive diagnostic prototype for lung cancer detection with conformal prediction](https://pure.royalholloway.ac.uk/portal/files/37171406/Measurement_Manuscript_unmarked_R4.pdf) by Xianghao Zhana,c, Zhan Wanga, Meng Yangb, Zhiyuan Luod, You Wanga, Guang Li (2020)
21. [Predicting the Rate of Skin Penetration Using an Aggregated Conformal Prediction Framework](https://pubmed.ncbi.nlm.nih.gov/28335598/) by Martin Lindh, A. Karlén, Ulf Norinder (2017)
22. [The application of conformal prediction to the drug discovery process](https://link.springer.com/article/10.1007%2Fs10472-013-9378-2) by Martin Eklund, Ulf Norinder, Scott Boyer & Lars Carlsson (2014) 🔥🔥🔥🔥🔥
23. [Anomaly Detection of Trajectories with Kernel Density Estimation by Conformal Prediction](https://link.springer.com/content/pdf/10.1007%2F978-3-662-44722-2_29.pdf) by James Smith, Ilia Nouretdinov, Rachel Craddock, Charles Offer, and Alexander Gammerman (2009)
24. [Conformal prediction interval estimation and applications to day-ahead and intraday power markets](https://arxiv.org/pdf/1905.07886.pdf) by Christopher Kath, Florian Ziel (2019) 🔥🔥🔥🔥🔥
25. [The application of conformal prediction to the drug discovery process](https://link.springer.com/article/10.1007%2Fs10472-013-9378-2) by Martin Eklund, Ulf Norinder, Scott Boyer & Lars Carlsson (2013)
26. [Anomaly Detection of Trajectories with Kernel Density Estimation by Conformal Prediction](https://link.springer.com/chapter/10.1007%2F978-3-662-44722-2_29) by James Smith, Ilia Nouretdinov, Rachel Craddock, Charles Offer, Alexander Gammerman (Royal Holloway, UK, 2014)
27. [Exchangeability, Conformal Prediction, and Rank Tests](https://arxiv.org/pdf/2005.06095.pdf) by Arun Kuchibhotla (Carnegie Mellon, 2021)
28. [Conformal prediction with localization](https://arxiv.org/pdf/1908.08558.pdf) by Leying Guan (Yale, 2020)
29. [Predicting skin sensitizers with confidence - Using conformal prediction to determine applicability domain of GARD](https://pubmed.ncbi.nlm.nih.gov/29374571/) by Andy Forreryd, Ulf Norinder, Tim Lindberg, Malin Lindstedt (2018)
30. [Binary classification of imbalanced datasets using conformal prediction](https://pubmed.ncbi.nlm.nih.gov/28135672/) by 
Ulf Norinder, Scott Boyer (2017)
31. [Discretized conformal prediction for efficient distribution-free inference](https://arxiv.org/pdf/1709.06233.pdf) by Wenyu Chen, Kelli-Jean Chun, and Rina Foygel Barber (2017)
32. [Validity, consonant plausibility measures, and conformal prediction](https://www.sciencedirect.com/science/article/abs/pii/S0888613X21001195?via%3Dihub) by Leonardo Cella. and Ryan Martin (2021)
33. [Conformal Prediction Classification of a Large Data Set of Environmental Chemicals from ToxCast and Tox21 Estrogen Receptor Assays](https://pubmed.ncbi.nlm.nih.gov/27152554/) by Ulf Norinder, Scott Boyer (2016)
34. [Conformal prediction to define applicability domain – A case study on predicting ER and AR binding](https://www.tandfonline.com/doi/full/10.1080/1062936X.2016.1172665) by U. Norinder, A. Rybacka, P.Andersson (2016)
35. [Conformal prediction of biological activity of chemical compounds](https://link.springer.com/article/10.1007%2Fs10472-017-9556-8) by Paolo Toccaceli, Ilia Nouretdinov, Alex Gammerman (Royal Holloway, UK, 2017) 🔥🔥🔥🔥🔥
36. [Introducing conformal prediction in predictive modeling for regulatory purposes. A transparent and flexible alternative to applicability domain determination](https://pubmed.ncbi.nlm.nih.gov/25559551/) by Ulf Norinder, Lars Carlsson, Scott Boyer, Martin Eklund (2015)
37. [Aggregated Conformal Prediction](https://link.springer.com/chapter/10.1007%2F978-3-662-44722-2_25) by Lars CarlssonMartin EklundUlf Norinder (2014)
38. [Interpretation of Conformal Prediction Classification Models](https://link.springer.com/chapter/10.1007%2F978-3-319-17091-6_27) by Ernst Ahlberg, Ola Spjuth, Catrin Hasselgren, Lars Carlsson (2015)
39. [Cross-Conformal Prediction with Ridge Regression](https://link.springer.com/chapter/10.1007%2F978-3-319-17091-6_21) by Harris Papadopoulos (2015)
40. [Sparse conformal prediction for dissimilarity data](https://link.springer.com/article/10.1007%2Fs10472-014-9402-1) by Frank-Michael Schleif, Xibin Zhu and Barbara Hammer (2015)
41. [Effective utilization of data in inductive conformal prediction using ensembles of neural networks](https://ieeexplore.ieee.org/document/6706817) by Tuve Löfström, Ulf Johansson and Henrik Boström (2013)
42. [Beyond the Basic Conformal Prediction Framework](https://www.sciencedirect.com/science/article/pii/B978012398537800002X?via%3Dihub) by Vladimir Vovk (2014)
43. [An electronic nose-based assistive diagnostic prototype for lung cancer detection with conformal prediction](https://pure.royalholloway.ac.uk/portal/files/37171406/Measurement_Manuscript_unmarked_R4.pdf) by Xianghao Zhan, Zhan Wang, Meng Yang, Zhiyuan Luo, You Wang, Guang Li (Stanford, Royal Holloway, China University of Mining and Technology, 2020)
44. [Predicting with confidence: Using conformal prediction in drug discovery](https://jpharmsci.org/article/S0022-3549(20)30589-X/fulltext) by Jonathan Alvarsson, Staffan Arvidsson McShane, Ulf Norinder, Ola Spjuth (2021) 🔥🔥🔥🔥🔥
45. [Inductive conformal prediction for silent speech recognition](https://pubmed.ncbi.nlm.nih.gov/32120355/) by Ming Zhang, You Wang, Zhang Wei, Meng Yang, Zhiyuan Luo, Guang Li (2020)
46. [Large scale comparison of QSAR and conformal prediction methods and their applications in drug discovery](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-018-0325-4) by Nicolas Bosc, Francis Atkinson, Eloy Felix, Anna Gaulton, Anne Hersey and Andrew R. Leach (2019)
47. [Deep Conformal Prediction for Robust Models](https://link.springer.com/chapter/10.1007%2F978-3-030-50146-4_39) by Soundouss Messoudi, Sylvain Rousseau and Sébastien Destercke (2020)
48. [Strong validity, consonance, and conformal prediction](https://arxiv.org/abs/2001.09225) by Leonardo Cella and Ryan Martin (2020)
49. [Skin Doctor CP: Conformal Prediction of the Skin Sensitization Potential of Small Organic Molecules](https://pubs.acs.org/doi/10.1021/acs.chemrestox.0c00253) by Anke Wilm, U. Norinder, M. Agea, Christina de Bruyn Kops, Conrad Stork, J. Kühnl, J. Kirchmair (2020)
50. [Conformal prediction based active learning by linear regression optimization](https://www.sciencedirect.com/science/article/abs/pii/S0925231220300461?via%3Dihub) by Sergio Matiz, Kenneth E.Barner (2020)
51. [Conformal prediction intervals for the individual treatment effect](https://arxiv.org/pdf/2006.01474.pdf) by Danijel Kivaranovic, Robin Ristl, Martin Poschb, Hannes Leeb (2020)
52. [Nearest neighbor based conformal prediction](https://www.f08.uni-stuttgart.de/.content/media/downloads/Mathematik/mathematische_berichte/2020/2020-002.pdf) by László Györfi and Harro Walk (2020)
53. [Concepts and Applications of Conformal Prediction in Computational Drug Discovery](https://arxiv.org/pdf/1908.03569.pdf) by Isidro Cortés-Ciriano and Andreas Bender (2019) 🔥🔥🔥🔥🔥
54. [Predicting Ames Mutagenicity Using Conformal Prediction in the Ames/QSAR International Challenge Project](https://academic.oup.com/mutage/article/34/1/33/5239859) by Ulf Norinder,  Ernst Ahlberg,  Lars Carlsson (2018)
55. [Nested Conformal Prediction and the Generalized Jackknife](https://arxiv.org/pdf/1910.10562v1.pdf) by Arun Kuchibhotla and Aaditya Ramdas (Carnegie Mellon, 2019)
56. [Predictive inference with the jackknife+](https://arxiv.org/abs/1905.02928) by Rina Foygel Barber, Emmanuel Candès, Aaditya Ramdas, and Ryan Tibshirani (2020) 🔥🔥🔥🔥🔥
57. [A Distribution-Free Test of Covariate Shift Using Conformal Prediction](https://arxiv.org/pdf/2010.07147.pdf) by Xiaoyu Hu and Jing Lei (Peking Univerity, China and Carnegie Mellon, USA, 2020) 🔥🔥🔥🔥🔥
58. [Exchangeability, Conformal Prediction, and Rank Tests](https://arxiv.org/pdf/2005.06095.pdf) by Arun Kuchibhotla (Carnegie Mellon, 2021)
59. [Conformal prediction with localization](https://arxiv.org/pdf/1908.08558.pdf) by Leying Guan (2020)
60. [Multitask Modeling with Confidence Using Matrix Factorization and Conformal Prediction](https://pubmed.ncbi.nlm.nih.gov/30908915/) by Ulf Norinder, Fredrik Svensson 
61. [Conformal prediction of HDAC inhibitors](https://www.tandfonline.com/doi/abs/10.1080/1062936X.2019.1591503?journalCode=gsar20) by U. Norinder, J.J.Navaka, E. Lopez-Lopez, D. Mucs & J.L. Medina-Franco (2019)
62. [Computing Full Conformal Prediction Set with Approximate Homotopy](https://arxiv.org/pdf/1909.09365.pdf) by Eugene Ndiaye, Ichiro Takeuchi (2019)
63. [Conformal Prediction Based on Raman Spectra for the Classification of Chinese Liquors](https://journals.sagepub.com/doi/10.1177/0003702819831017) by
Jiao Gu, Huaibo Liu, Chaoqun Ma, Lei Li, Chun Zhu, Christ Glorieux, Guoqing Chen (2019)
64. [Efficient and minimal length parametric conformal prediction regions](https://export.arxiv.org/pdf/1905.03657) by Daniel Eck and Forrest Crawford (2019)
65. [Conformal Prediction for Students' Grades in a Course Recommender System](http://proceedings.mlr.press/v105/morsomme19a/morsomme19a.pdf) by Raphael Morsomme and Evgueni Smirnov (2019)
66. [Efficient iterative virtual screening with Apache Spark and conformal prediction](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-018-0265-z) by Laeeq Ahmed, Valentin Georgiev, Marco Capuccini, Salman Toor, Wesley Schaal, Erwin Laure and Ola Spjuth (2018)
67. [Predicting Off-Target Binding Profiles With Confidence Using Conformal Prediction](https://pubmed.ncbi.nlm.nih.gov/30459617/) by Samuel Lampa, Jonathan Alvarsson, Staffan Arvidsson Mc Shane, Arvid Berg, Ernst Ahlberg, Ola Spjuth (2018)
68. [Maximizing gain in high-throughput screening using conformal prediction](https://jcheminf.biomedcentral.com/track/pdf/10.1186/s13321-018-0260-4.pdf) by Fredrik Svensson, Avid M. Afzal1, Ulf Norinder and Andreas Bender (2018)
69. [Conformalized Survival Analysis](https://arxiv.org/pdf/2103.09763.pdf) by Emmanuel Candès, Lihua Lei and Zhimei Ren (2021) [R-Code](https://github.com/valeman/cfsurv_paper)  🔥🔥🔥🔥🔥
70. [Random Forest Prediction Intervals](https://haozhestat.github.io/files/manuscript_RFIntervals_FinalVersion.pdf) by Haozhe Zhang†, Joshua Zimmerman†, Dan Nettleton† and Daniel J. Nordman† (Iowa State University, USA, 2019)
71. [Conformal Training: Learning Optimal Conformal Classifiers | DeepMind](https://arxiv.org/pdf/2110.09192.pdf) by David Stutz (DeepMind), Krishnamurthy Dvijotham, Ali Taylan Cemgil and Arnaud Doucet (2021)
72. [Comparing the Bayes and typicalness frameworks](https://link.springer.com/content/pdf/10.1007%2F3-540-44795-4_31.pdf) by Thomas Melluish, Craig Saunders, Ilia Nouretdinov, and Volodya Vovk (Royal Holloway, UK, 2001). 🔥🔥🔥🔥🔥
73. [Large-scale probabilistic predictors with and without guarantees of validity](https://papers.nips.cc/paper/2015/file/a9a1d5317a33ae8cef33961c34144f84-Paper.pdf) by Vladimir Vovk, Ivan Petej, and Valentina Fedorova (Royal Holloway, Yandex, NeurIPS) 🔥🔥🔥🔥🔥
74. [Inductive conformal prediction for silent speech recognition](https://iopscience.iop.org/article/10.1088/1741-2552/ab7ba0) by Ming Zhang, You Wang, Wei Zhang, Meng Yang, Zhiyuan Luo and Guang Li (2020)
75. [Valid prediction intervals for regression problems](https://arxiv.org/abs/2107.00363) by Nicolas Dewolf, Bernard De Baets, Willem Waegeman (2021) 🔥🔥🔥🔥🔥
76. [Application of conformal prediction interval estimations to market makers’ net positions](http://proceedings.mlr.press/v128/wisniewski20a.html) by Wojciech Wisniewski, David Lindsay, Sian Lindsay (Royal Holloway, UK, 2020)
77. [Locally Valid and Discriminative Prediction Intervals for Deep Learning Models](https://papers.nips.cc/paper/2021/hash/46c7cb50b373877fb2f8d5c4517bb969-Abstract.html) by Zhen Lin, Shubhendu Trivedi, Jimeng Sun (NeurIPS, 2021) 🔥🔥🔥🔥🔥
78. [Distribution-Free Federated Learning with Conformal Predictions](https://arxiv.org/pdf/2110.07661.pdf) by Charles Lu and Jayashree Kalpathy-Cramer (2022)
79. [Coreset-based Conformal Prediction for Large-scale Learning](https://proceedings.mlr.press/v105/riquelme-granada19a.html) by Nery Riquelme-Granada, Khuong Nguyen, Zhiyuan Luo (Royal Holloway, UK, 2019)
80. [Fast probabilistic prediction for kernel SVM via enclosing balls](https://proceedings.mlr.press/v128/riquelme-granada20a.html) by Nery Riquelme-Granada, Khuong Nguyen, Zhiyuan Luo (Royal Holloway, UK, 2020)
81. [Conformalized density- and distance-based anomaly detection in time-series data](https://arxiv.org/abs/1608.04585) by Evgeny Burnaev, Vladislav Ishimtsev (2016) 
82. [Predictive Inference with Weak Supervision](https://arxiv.org/pdf/2201.08315.pdf) by Maxime Cauchois, Suyash Gupta, Alnur Ali and John Duchi (Stanford, 2022)
83. [Conformal Prediction in Clinical Medical Sciences](https://link.springer.com/10.1007/s41666-021-00113-8) by Janette Vazquez and Julio C. Facelli University of Utah, 2022)
84. [Provably Improving Expert Predictions with Conformal Prediction](https://arxiv.org/pdf/2201.12006.pdf) by Eleni Straitouri, Lequng Wang,  Nastaran Okati and Manuel Gomez Rodriguez (Max Planck Institute for Software Systems / Cornell University, 2021).
85. [Cover your cough: detection of respiratory events with confidence using a smartwatch](https://proceedings.mlr.press/v91/nguyen18a.html) by Khuong An Nguyen, Zhiyuan Luo (Royal Holloway, 2019).
86. [Predicting Amazon customer reviews with deep confidence using deep learning and conformal prediction](https://www.tandfonline.com/doi/full/10.1080/23270012.2022.2031324) by Ulf Norinder and Petra Norinder (2022)
87. [Conformal Prediction for the Design Problem](https://arxiv.org/pdf/2202.03613.pdf) by Clara Fannjianga, Stephen Batesa, Anastasios Angelopoulosa, Jennifer Listgartena and Michael I. Jordan (Berkeley, 2022) 🔥🔥🔥🔥🔥
88. [Image-to-Image Regression with Distribution-Free Uncertainty Quantification and Applications in Imaging](https://arxiv.org/pdf/2202.05265.pdf) by Anastasios N. Angelopoulos, Amit Kohli, Stephen Bates, Michael I. Jordan, Jitendra Malik, Thayer Alshaabi, Srigokul Upadhyayula, Yaniv Romano (Berkeley and Technion, 2022) 🔥🔥🔥🔥🔥
89. [Conformal predictive decision making](http://proceedings.mlr.press/v91/vovk18b/vovk18b.pdf) by Vladimir Vovk and Claus Bendtsen (2018).
90. [The Lifecycle of a Statistical Model: Model Failure Detection, Identification, and Refitting](https://arxiv.org/pdf/2202.04166.pdf) by Alnur Ali1, Maxime Cauchois and John C. Duchi (Stanford, 2022)
91. [E-values: Calibration, combination, and applications](https://arxiv.org/pdf/1912.06116.pdf) by Vladimir Vovk (Royal Holloway) and Ruodu Wang (University of Waterloo) (2019)
92. [Conformal Prediction Sets with Limited False Positives](https://arxiv.org/pdf/2202.07650.pdf) by Adam Fisch, Tal Schuster, Tommi Jaakkola and Regina Barzilay [code](https://github.com/ajfisch/conformal-fp) (MIT / Google Research, 2022) 🔥🔥🔥🔥🔥
93. [Ensemble Conformalized Quantile Regression for
Probabilistic Time Series Forecasting](https://arxiv.org/pdf/2202.08756v1.pdf) by Vilde Jensen, Filippo Maria Bianchi, Stian Norman Anfinsen (Arctic University of Norway, 2022) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥 [Python Code](https://github.com/FilippoMB/Ensemble-Conformalized-Quantile-Regression)
94. [Prediction of Metabolic Transformations using Cross Venn-ABERS Predictors](http://proceedings.mlr.press/v60/arvidsson17a/arvidsson17a.pdf) by Staffan Arvidsson, Ola Spjuth, Lars Carlsson and Paolo Toccaceli (University of Uppsala, Astra Zeneca, Royal Holloway, 2017)
95. [Probabilistic Prediction in scikit-learn](https://www.diva-portal.org/smash/get/diva2:1603345/FULLTEXT01.pdf) by Sweidan, Dirar and Ulf Johansson. 🔥🔥🔥🔥🔥
96. [Conformalized Online Learning: Online Calibration Without a Holdout Set](https://arxiv.org/pdf/2205.09095.pdf) by Shai Feldman, Stephen Bates and Yaniv Romano (2022). TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
97. [Valid model-free spatial prediction](https://arxiv.org/pdf/2006.15640.pdf) by Huiying Mao, Ryan Martin and Brian J Reich (2020)
98. [Conformal Prediction with Temporal Quantile Adjustments](https://arxiv.org/pdf/2205.09940.pdf) by Zhen Lin, Shubhendu Trivedi, Jimeng Sun (2022)  TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
99. [Calibration of Natural Language Understanding Models with Venn–ABERS Predictors](https://arxiv.org/pdf/2205.10586.pdf) by Patrizio Giovannotti (Royal Holloway, UK, 2022) NLP
100. [Conformal prediction interval for dynamic time-series](https://proceedings.mlr.press/v139/xu21h.html) by Chen Xu, Yao Xie (Georgia Tech, 2021) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
101. [Conformal prediction set for time-series](https://arxiv.org/abs/2206.07851) by Chen Xu, Yao Xie (Georgia Tech, 2022) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
102. [Conformal Time-Series Forecasting](https://proceedings.neurips.cc/paper/2021/file/312f1ba2a72318edaaa995a67835fad5-Paper.pdf) by Kamile  Stankeviciu te and Ahmed M. Alaa (2021)  TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
103. [Efficient Conformal Prediction via cascaded inference with expanded admission](https://arxiv.org/pdf/2007.03114.pdf) by Adam Fisch,  Tal Schuster, Tommi Jaakkola, Regina Barzilay (MIT 2021]. [Python Code](https://github.com/ajfisch/conformal-cascades)
104. [Split Localized Conformal Prediction](https://arxiv.org/abs/2206.13092) by Xing Han, Ziyang Tang, Joydeep Ghosh, Qiang Liu (University of Texas, 2022). [Python Code](https://github.com/valeman/SLCP)
105. [Three Applications of Conformal Prediction for Rating Breast Density in Mammography](https://arxiv.org/pdf/2206.12008.pdf) by Charles Lu, Ken Chang, Praveer Singh, Jayashree Kalpathy-Crame (2022)
106. [Conformal prediction set for time-series](https://arxiv.org/abs/2206.07851) by Chen Xu, Yao Xie (Georgia Tech, 2022) [Python Code](hhttps://github.com/valeman/Ensemble-Regularized-Adaptive-Prediction-Set-ERAPS) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
107. [Recommendation systems with distribution-free reliability guarantees](https://arxiv.org/pdf/2207.01609.pdf)) by Anastasious Angelopolous, Karl Krauth, Stephen Bates, Yixin Wang and Michael I. Jordan (Berkeley 2022)
108. [Model Agnostic Conformal Hyperparameter Optimization](https://arxiv.org/pdf/2207.03017.pdf) by Riccardo Doyle (Spotify, 2022)
109. [Improving Trustworthiness of AI Disease Severity Rating in Medical Imaging with Ordinal Conformal Prediction Sets](https://arxiv.org/pdf/2207.02238.pdf) by Charles Lu, Anastasios N. Angelopoulos, Stuart Pomerantz (2022) [code](https://github.com/clu5/lumbar-conformal) 🔥🔥🔥🔥🔥
110. [Conformal Off-Policy Prediction in Contextual Bandits](https://arxiv.org/pdf/2206.04405.pdf) by Muhammad Faaiz Taufiq, Jean-François Ton, Rob Cornish, Yee Whye Teh, Arnaud Doucet (Oxford, 2022) [Video presentation](https://youtu.be/K5RAjP1Ze30)
111. [Semantic uncertainty intervals for disentangled latent space](https://arxiv.org/pdf/2207.10074.pdf) by Swami Sankaranarayanan, Anastasios N. Angelopoulos, Stephen Bates, Yaniv Romano, and Phillip Isola (Unversity of Berkeley, Technion, 2022) 🔥🔥🔥🔥🔥
112. [CODiT: Conformal Out-of-Distribution Detection in Time- Series Data](https://arxiv.org/pdf/2207.11769.pdf) by Ramneet Kaur et.al., Unibersity of Pensylvania (2022). [Code](https://github.com/kaustubhsridhar/time-series-OOD) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
113. [Confident Adaptive Language Modeling](https://arxiv.org/pdf/2207.07061.pdf) by Tal Schuster, Adam Fisch, Jai Gupta, Mostafa Dehghani, Dara Bahri, Vinh Q. Tran, Yi Tay, Donald Metzler (Google, MIT, 2022j
114. [Probabilistic Conformal Prediction Using Conditional Random Samples](https://arxiv.org/pdf/2206.06584.pdf) by Zhendong Wang, Ruijiang Gao, Mingzhang Yin, Mingyuan Zhou, David M. Blei (Columbia University, 2020) [Code](https://github.com/Zhendong-Wang/Probabilistic-Conformal-Prediction)
115. [A general framework for multi-step ahead adaptive conformal heteroscedastic time series forecasting](https://arxiv.org/pdf/2207.14219.pdf) by Martim Sousa, Ana Maria Tome and Jose Moreira (University of Aveiro, 2022) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥  
116. [A novel Deep Learning approach for one-step Conformal Prediction approximation](https://arxiv.org/pdf/2207.12377.pdf) by Julia A. Meister, Khuong An Nguyen, Stelios Kapetanakis and Zhiyuan Luo (University of Brighton, UK, 2022)  🔥🔥🔥🔥🔥
117. [Conformal Risk Control](https://arxiv.org/pdf/2208.02814.pdf) by Anastasious Angelopolous, Stephen Bates, Adam Fisch, Lihua Lei and Tal Schuster (Berkeley, Stanford, MIT and Google Research, 2022) 🔥🔥🔥🔥🔥
118. [CD-split and HPD-split: Efficient Conformal Regions in High Dimensions](https://www.jmlr.org/papers/volume23/20-797/20-797.pdf) by Rafael Izbicki, Gilson Shimizu, Rafael B. Stern (San Carlos University Brazil, 2022) [R code](https://github.com/rizbicki/predictionBands)
119. [Flexible distribution-free conditional predictive bands using density estimators](https://proceedings.mlr.press/v108/izbicki20a.html) by Rafael Izbicki, Gilson Shimizu, and Rafael B.  Stern (San Carlos University Brazil, 2020)
120. [Split Conformal Prediction for Dependent Data](https://arxiv.org/abs/2203.15885) by Roberto I. Oliveira, Paulo Orenstein, Thiago Ramos, João Vitor Romano (IMPA, Rio de Janeiro, Brazil, 2022) 
121. [Conformal Inference for Online Prediction with Arbitrary Distribution Shifts](https://arxiv.org/pdf/2208.08401.pdf) by Isaac Gibbs and Emmanual Candes (Stanford, 2022) 🔥🔥🔥🔥🔥
122. [A General Framework For Multi-step Ahead Adaptive Conformal Heteroscedastic Time Series Forecasting](https://arxiv.org/pdf/2207.14219.pdf) by Martim Sousa, Ana Maria Tomé, University of Aveiro (2022) [Code](https://github.com/Quilograma/AdaptiveEnbMIMOCQR) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
123. [Cough-based COVID-19 detection with audio quality clustering and confidence measure based learning](https://copa-conference.com/papers/COPA2022_paper_13.pdf) by Alice E. Ashby, Julia A. Meister, Khuong An Nguyen, Zhiyuan Luo, Werner Gentzk (University of Brighton, 2022)
124. [Assessing Explanation Quality by Venn Prediction](https://copa-conference.com/papers/COPA2022_paper_10.pdf) by Amr Alkhatib, Henrik Bostroem and Ulf Johansson (2022)
125. [Conformal prediction for hypersonic flight vehicle classification](https://www.copa-conference.com/papers/COPA2022_paper_1.pdf) by Zepu Xi, Xuebin Zhuang, Hongbo Chen (Yat-sen University, Guangzhou, China, 2022) [Slides](https://copa-conference.com/presentations/Zepu.pdf)
126. [Robust Gas Demand Forecasting With Conformal Prediction](https://copa-conference.com/papers/COPA2022_paper_12.pdf) by Mouhcine Mendil, Luca Mossina, Marc Nabhan, Kevin Pasini (2022)
127. [Conformal Prediction Interval Estimations with an Application to Day-Ahead and Intraday Power Markets](https://arxiv.org/pdf/1905.07886.pdf) by Christopher Kath and Florian Ziel (2020)
128. [Conformal Prediciton beyond exchangeability](https://arxiv.org/abs/2202.13415) by Rina Foygel Barber, Emmanuel J. Candes, Aaditya Ramdas, Ryan J. Tibshirani (2022)
129. [Robust Gas Demand Forecasting with Conformal Prediction](https://copa-conference.com/papers/COPA2022_paper_12.pdf) by Mouhcine Mendil, Luca Mossina, Marc Nabhan, Kevin Pasini (2022)
130. [Split conformal prediction for dependant data](https://arxiv.org/pdf/2203.15885.pdf) by Roberto I. Oliveira, Paulo Orenstein, Thiago Ramos and João Vitor Romano (2022) 
131. [Conformal prediction of small-molecule drug resistance in cancer cell lines](https://copa-conference.com/papers/COPA2022_paper_22.pdf) by Saiveth Hernandez-Hernandez, Sachin Vishwakarma and Pedro Ballester (2022)
132. [Ellipsoidal conformal inference for Multi-Target Regression](https://copa-conference.com/papers/COPA2022_paper_7.pdf) by Soundouss Messoudi, Sebastien Destercke, Sylvain Rousseau (2022) [Slides](https://copa-conference.com/presentations/soundouss.pdf) 
133. [Conformal Methods for Quantifying Uncertainty in Spatiotemporal Data: A Survey](https://arxiv.org/abs/2209.03580) by Sophia Sun (UCLA, 2022)
134. [Deep Learning With Conformal Prediction for Hierarchical Analysis of Large-Scale Whole-Slide Tissue Images](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9103229) by Håkan Wieslander , Philip J. Harrison, Gabriel Skogberg, Sonya Jackson, Markus Fridén, Johan Karlsson, Ola Spjuth, and Carolina Wählby (2021)
135. [Audio–visual domain adaptation using conditional semi-supervised Generative Adversarial Networks](https://www.sciencedirect.com/science/article/pii/S0925231219316170) by Christos Athanasiadis, Enrique Hortal, Stylianos Asteriadis (2022)
136. [Conformal Prediction is Robust to Label Noise](https://arxiv.org/pdf/2209.14295.pdf) by Bat-Sheva Einbinder, Stephen Bates, Anastasios N. Angelopoulos, Asaf Gendler, Yaniv Romano (2022)
137. [Copula Conformal Prediction for Multi-step Time Series Forecasting](https://openreview.net/pdf?id=jCdoLxMZxf) TIME SERIES 🚀🚀🚀🚀🚀 🔥🔥🔥🔥🔥
138. [Batch Multivalid Conformal Prediction](https://arxiv.org/abs/2209.15145) by Christopher Jung, Georgy Noarov, Ramya Ramalingam, Aaron Roth (Stanford, university of Pensylvania, 2022)
139. [Selection by Prediction with Conformal p-values](https://arxiv.org/pdf/2210.01408.pdf) by Ying Jin1 and Emmanuel J. Candes, (Stanford, 2022) [Video](https://www.youtube.com/watch?v=YEpvHsHCCvQ) [code](https://github.com/ying531/selcf_paper)
140. [Few-Shot Calibration of Set Predictors via Meta-Learned Cross-Validation-Based Conformal Prediction](https://arxiv.org/pdf/2210.03067v1.pdf) by Sangwoo Park, Kfir M. Cohen, Osvaldo Simeone (2022)
141. [Conformalized Fairness via Quantile Regression](https://web7.arxiv.org/pdf/2210.02015.pdf) by Meichen Liu, Lei Ding,
Dengdeng Yu, Wulong Liu, Linglong Kong, Bei Jiang (University of Alberta, Noah Arc Huawei, 2022)
142. [Test-time recalibration of conformal predictors under distribution shift based on unlabeled examples](https://arxiv.org/pdf/2210.04166.pdf) by Fatih Furkan Yilmaz, and Reinhard Heckel (Rice University / University of Munuch, 2022)
143. [Extending Conformal Prediction to Hidden Markov Models with Exact Validity via de Finetti's Theorem for Markov Chains](https://arxiv.org/abs/2210.02271) by Buddhika Nettasinghe, Samrat Chatterjee, Ramakrishna Tipireddy, Mahantesh Halappanavar (2022)
144. [Predictive inference with feature conformal prediction](https://arxiv.org/pdf/2210.00173.pdf) by Jiaye Teng, Chuan Wen, Dinghuai Zhang,
Yoshua Bengio, Yang Gao, Yang Yuan (Tsinghua University, Mila - Quebec AI Institute, Shanghai Artificial Intelligence Laboratory, Shanghai Qi Zhi Institute, 2022) [code](https://github.com/AlvinWen428/FeatureCP) 🔥🔥🔥🔥🔥
145. [Constructing Prediction Intervals with Neural Networks: An Empirical Evaluation of Bootstrapping and Conformal Inference Methods](https://arxiv.org/pdf/2210.05354.pdf) by Alex Contarino, Christine Schubert Kabban, Chancellor Johnstone and Fairul Mohd-Zaid (2022)
146. [Spatio-Temporal Wildfire Prediction using Multi-Modal Data](https://arxiv.org/pdf/2207.13250.pdf) by Chen Xu1, Yao Xie,
Daniel A. Zuniga Vazquez, Rui Yao, and Feng Qiu (2022)
147. [Calibrating AI models for few-shot demodulation via conformal prediction](https://arxiv.org/pdf/2210.04621.pdf) Kfir M. Cohen1, Sangwoo Park, Osvaldo Simeone, Shlomo Shamai (2022)
148. [Test-time recalibration of conformal predictors under distribution shift based on unlabeled examples](https://arxiv.org/pdf/2210.04166.pdf) 
[Code](https://github.com/MLI-lab/recalibrating_conformal_prediction)
149. [Nonparametric Quantile Regression: Non-Crossing Constraints and Conformal Prediction](https://arxiv.org/pdf/2210.10161.pdf) by Wenlu Tang, Guohao Shen, Yuanyuan Lin and Jian Huang (The Hong Kong Polytechnic University, 2022)
150. [Safe Planning in Dynamic Environments using Conformal Prediction](https://arxiv.org/pdf/2210.10254.pdf) by 
Lars Lindemann, Matthew Cleaveland∗, Gihyun Shim, and George J. Pappas (University of Pensylvania, 2022)
151. [Conformal prediction under feedback covariate shift for biomolecular design](https://www.pnas.org/doi/10.1073/pnas.2204569119) by Clara Fannjiang, Stephen Bates, Anastasios N. Angelopoulos,and Michael I. Jordan (2022) 🔥🔥🔥🔥🔥
152. [Conformal Predictor for Improving Zero-shot Text Classification Efficiency](https://arxiv.org/pdf/2210.12619.pdf) by Prafulla Kumar Choubey, Yu Bai,  Chien-Sheng Wu, Wenhao Liu, Nazneen Rajani (Saleforce AI Research and Hugging Face, 2022)
153. [Bayesian Optimization with Conformal Coverage Guarantees](https://arxiv.org/pdf/2210.12496.pdf) by Samuel Stanton, Wesley Maddox and Andrew Gordon Wilson (Genentech, New York University, 2022) [Code](https://github.com/samuelstanton/conformal-bayesopt) 🔥🔥🔥🔥🔥
154. [Measuring the Confidence of Traffic Forecasting Models: Techniques, Experimental Comparison and Guidelines towards Their Actionability](https://arxiv.org/pdf/2210.16049.pdf) by Ibai Lanaa, Ignacio (In ̃aki) Olabarrietaa, Javier Del Sera (2022)
155. [Conformalized Fairness via Quantile Regression](https://openreview.net/pdf?id=rwyISFoSmXd) by Meichen Liu, Lei Ding, Dengdeng Yu, Wulong Liu, Linglong Kong, Bei Jiang (University of Alberta, Huawei Noah’s Ark Lab Canada, NeurIPS 2022 paper) [Code](https://github.com/Lei-Ding07/Conformal_Quantile_Fairness) 🔥🔥🔥🔥🔥
156. [Engineering Uncertainty Representations to Monitor Distribution Shifts](https://openreview.net/pdf?id=Koug1i2HpH) by Thomas Bonnier and  Benjamin Bosch (Société Générale, 2022)
157. [CONffusion: CONFIDENCE INTERVALS FOR DIFFUSION MODELS](https://arxiv.org/pdf/2211.09795.pdf) [Project](https://www.vision.huji.ac.il/conffusion/)[Code](https://github.com/eliahuhorwitz/Conffusion) by Eliahu Horwitz,  Yedid Hoshen (Hebrew University of Jerusalem, 2022) 🔥🔥🔥🔥🔥
158. [Semantic uncertainty intervals for disentangled latent spaces](https://swamiviv.github.io/semantic_uncertainty_intervals/) by Swami Sankaranarayanan, Anastasios N. Angelopoulos, Stephen Bates, Yaniv Romano, Phillip Isola (MIT, Berkeley, Technion, 2022) 🔥🔥🔥🔥🔥
159. [But are you sure? An uncertainty-aware perspective on explainable AI](https://assets.amazon.science/bf/d0/14c3eb614699909dae8a092b9492/but-are-you-sure-an-uncertainty-aware-perspective-on-explainable-ai.pdf) by Charlie Marx, Youngsuk Park, Hilaf Hasson, Yuyang (Bernie) Wang, Stefano Ermon, Jun Huan (2022)
160. [Calibrating AI Models for Wireless Communications via Conformal Prediction](https://arxiv.org/pdf/2212.07775.pdf) by Kfir M. Cohen, Sangwoo Park, Osvaldo Simeone and Shlomo Shamai (2022)
161. [Predicting Endocrine Disruption Using Conformal Prediction – A Prioritization Strategy to Identify Hazardous Chemicals with Confidence](https://pubs.acs.org/doi/10.1021/acs.chemrestox.2c00267) by Maria Sapounidou, Ulf Norinder and Patrick Andersson (2022)
162. [Conformal Loss-Controlling Prediction](https://arxiv.org/pdf/2301.02424.pdf) by Di Wang, Ping Wang, Zhong Ji, Xiaojun Yang, Hongyue Li (2023)
163. [ROBUST AND SCALABLE UNCERTAINTY ESTIMATION WITH CONFORMAL PREDICTION FOR MACHINE-LEARNED INTERATOMIC POTENTIALS](https://arxiv.org/pdf/2208.08337.pdf) [Code](https://github.com/valeman/conformal_prediction_in_latent_space) by Yuge Hu, Joseph Musielewicz, Zachary Ulissi, Andrew J. Medford (Georgia Institute of Technology/Carnegie Mellon University, 2022)
164. [Clustering of Trajectories using Non-Parametric Conformal DBSCAN Algorithm](https://sites.rutgers.edu/jie-gao/wp-content/uploads/sites/375/2022/03/conformal-DBSCAN-compressed.pdf) by Haotian Wang, Jie Gao, Min-ge Xie Rutgers University, 2022)
165. [But Are You Sure? An Uncertainty-Aware Perspective on Explainable AI](https://assets.amazon.science/bf/d0/14c3eb614699909dae8a092b9492/but-are-you-sure-an-uncertainty-aware-perspective-on-explainable-ai.pdf) by Charlie Marx, Youngsuk Park, Hilaf Hasson, Yuyang Wang, Stefano Ermon, Jun Huan (2022)
166. [Prediction-Powered Inference](https://arxiv.org/pdf/2301.09633.pdf) by Anastasios N. Angelopoulos, Ste