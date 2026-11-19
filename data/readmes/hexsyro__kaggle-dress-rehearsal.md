# 🏆 Kaggle Dress Rehearsal

**Does your validation score actually predict your true held-out performance, or is it lying to you?**

This project runs a full, disciplined model-selection pipeline that mimics exactly what a real Kaggle competition demands: rigorous cross-validation (plain vs. stratified), three hyperparameter search strategies compared head-to-head (GridSearchCV, RandomizedSearchCV, Optuna), and a simulated public/private leaderboard split to catch leaderboard overfitting as it happens.

The dataset is the Telco Customer Churn data (7,043 customers, about 26.5% churners), reused from an earlier project. The point isn't the dataset; it's the validation discipline.

---

![Leaderboard overfitting simulation: cross-validation, public and private AUC after 10 to 50 tuning trials](outputs/figures/leaderboard_probing.png)

## 🎯 Project Questions

- Does StratifiedKFold actually produce more stable fold-to-fold scores than plain KFold on an imbalanced target?
- Given the same search space, how do GridSearchCV, RandomizedSearchCV, and Optuna compare on best score found vs. time spent?
- Does Optuna converge to a good score in meaningfully fewer trials than random search?
- If you tune aggressively against a fake "public" leaderboard split, does your score on a true untouched "private" split end up worse, and does a properly cross-validated model avoid that trap?

## Findings

All scores are ROC-AUC. Seed 42 is used everywhere.

1. **StratifiedKFold fixes fold balance, but barely changes the AUC spread.** The share of churners per validation fold varied with a standard deviation of 0.0072 under plain KFold (folds ranged from 25.3% to 27.5%) and 0.0002 under StratifiedKFold (every fold about 26.5%). That is roughly 30x more consistent. The AUC itself moved much less: standard deviation 0.0143 (KFold) vs 0.0134 (stratified), mean 0.8462 vs 0.8450. With about 7,000 rows and a 26.5% positive rate, plain KFold is already good enough; the benefit grows as the positive class gets rarer.
2. **The three search strategies end up in the same place.** Grid Search found 0.8479 in 109.8 s, Optuna found 0.8469 in 129.5 s (30 trials), and Randomized Search reported 0.8360 in 271.1 s. The fold-to-fold AUC spread is about 0.013, which is larger than the gap between Grid and Optuna (0.001), so those two should be read as a tie.
3. **Shallow trees win every time.** Grid Search, Randomized Search and Optuna all picked `max_depth=3`, with a small learning rate (0.01 to 0.07). The two best leaderboard-simulation trials used depth 3 and 4. Deep trees (depth 10 to 15) scored 0.80 to 0.83 in the Optuna study, so this feature set rewards simple models.
4. **Optuna learns fast, then plateaus.** Its random start (the first 10 trials) already reached 0.8463 by trial 7, and the final best (0.8469, trial 27) is only 0.0006 higher. After the first handful of trials, extra search bought almost nothing. I did not run a trial-for-trial comparison against random search, so this does not prove Optuna needs fewer trials than random search; it only shows how quickly this particular search saturates.
5. **No leaderboard overfitting showed up in this run.** After 50 trials scored only on the public split, the best public AUC was 0.8410, up just 0.0008 from the best at trial 10 (0.8402). The private score of that tuned model was 0.8471, slightly higher than the public one. Public and private splits are different random samples of 1,409 rows each, so a gap of this size is sampling noise, not evidence of overfitting.
6. **Why the trap didn't spring here:** the search space has only three parameters, the model family is already near its ceiling (about 0.845 to 0.848), and 50 trials is not many. Leaderboard overfitting needs room to overfit. The extensions below (a much smaller public split, a wider search space) are the way to provoke it.
7. **Takeaway:** on this dataset, careful cross-validation and public-score probing agree, and the honest ceiling for this feature set is about 0.845 AUC. Differences below about 0.005 AUC between any two setups are within noise.

---

## 📁 Repository Structure

```
kaggle-dress-rehearsal/
├── data/
│   ├── raw/                   # Untouched source dataset
│   └── processed/             # Cleaned, encoded and scaled feature/target files
│
├── notebooks/                  # Step-by-step, one notebook per phase
│   ├── 01_load_explore.ipynb
│   ├── 02_kfold_vs_stratified.ipynb
│   ├── 03_gridsearch_vs_randomsearch.ipynb
│   ├── 04_optuna_bayesian_optimization.ipynb
│   └── 05_leaderboard_overfitting_simulation.ipynb
│
├── src/                         # Reusable code, imported by notebooks/scripts (not copy-pasted)
│   ├── __init__.py
│   ├── data_load.py            # Load, clean, encode and scale the raw dataset
│   ├── cv_strategies.py          # KFold and StratifiedKFold comparison helpers
│   ├── search_grid_random.py      # GridSearchCV / RandomizedSearchCV runners, timed
│   ├── search_optuna.py            # Optuna study setup, objective function, TPESampler
│   └── leaderboard_sim.py           # Public/private split creation + overfitting tracker
│
├── tests/                       # Unit tests for src/ functions
│   ├── __init__.py
│   └── test_cv_strategies.py
│
├── models/                      # Saved best models per search strategy (.pkl), gitignored
│
├── outputs/
│   └── figures/                   # Fold-variance plot, search comparison plot, the
│                                    centerpiece 3-line leaderboard-overfitting plot
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠️ Setup

```bash
git clone https://github.com/hexsyro/kaggle-dress-rehearsal
cd kaggle-dress-rehearsal
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🚀 Usage

1. **Prepare the dataset.** Download the [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn/data) CSV and save it as `data/raw/Telco_Customer_Churn.csv`. Then clean, encode and scale it (writes four files into `data/processed/`):
   ```bash
   python -m src.data_load
   ```

2. **Run the experiments**, in this order:
   ```bash
   python -m src.cv_strategies         # KFold vs StratifiedKFold
   python -m src.search_grid_random    # GridSearchCV vs RandomizedSearchCV, timed
   python -m src.search_optuna         # Optuna (TPE) study and history plot
   python -m src.leaderboard_sim       # 60/20/20 split and public-score tuning
   ```

3. **Or explore in notebooks**, in order, starting with `notebooks/01_load_explore.ipynb`

   | Notebook | Open |
   |---|---|
   | 01 Load and explore | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/hexsyro/kaggle-dress-rehearsal/blob/main/notebooks/01_load_explore.ipynb) |
   | 02 KFold vs StratifiedKFold | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/hexsyro/kaggle-dress-rehearsal/blob/main/notebooks/02_kfold_vs_stratified.ipynb) |
   | 03 GridSearch vs RandomSearch | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/hexsyro/kaggle-dress-rehearsal/blob/main/notebooks/03_gridsearch_vs_randomsearch.ipynb) |
   | 04 Optuna Bayesian optimization | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/hexsyro/kaggle-dress-rehearsal/blob/main/notebooks/04_optuna_bayesian_optimization.ipynb) |
   | 05 Leaderboard overfitting simulation | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/hexsyro/kaggle-dress-rehearsal/blob/main/notebooks/05_leaderboard_overfitting_simulation.ipynb) |

4. `notebooks/05_leaderboard_overfitting_simulation.ipynb` produces the centerpiece plot (saved to `outputs/figures/leaderboard_probing.png`).
   Run it last, after the CV and search-strategy notebooks.

---

## 📊 Skills Practiced

| Skill | Where |
|---|---|
| k-fold and stratified k-fold CV | `notebooks/02`, `src/cv_strategies.py` |
| GridSearchCV vs. RandomizedSearchCV | `notebooks/03`, `src/search_grid_random.py` |
| Bayesian optimization with Optuna | `notebooks/04`, `src/search_optuna.py` |
| Avoiding leaderboard overfitting | `notebooks/05`, `src/leaderboard_sim.py` |

---

## 📈 Sample Finding

> StratifiedKFold made the churn share in each fold about 30x more consistent than plain KFold
> (standard deviation 0.0002 vs 0.0072), but the AUC spread only dropped from 0.0143 to 0.0134.
> Grid Search (0.8479), Optuna (0.8469) and Randomized Search all chose shallow trees (`max_depth=3`),
> and Optuna was within 0.0006 of its final best by trial 8. After 50 trials tuned against the fake
> public split, the public AUC rose only from 0.8402 to 0.8410, while the untouched private AUC was
> 0.8471. In this setup, probing the public score did not create a misleading gain, because the
> search space was small and the model was already near its ceiling.

---

## 📄 Data Sources

- Churn dataset: [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn/data)

---

## 🔭 Possible Extensions

- Repeat the leaderboard-overfitting simulation with a MUCH smaller fake public split
  (e.g. 100 rows) to see the overfitting gap widen even faster
- Widen the search space (`subsample`, `colsample_bytree`, `min_child_weight`, `gamma`) so
  public-score probing has more room to overfit
- Try Optuna's pruning callback to stop unpromising trials early and compare wall-clock
  time savings
- Extend to multi-metric optimization (e.g. optimize for both ROC-AUC and training time)