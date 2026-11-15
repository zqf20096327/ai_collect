# ⚔️ The Churn Boosting Showdown

**XGBoost vs LightGBM vs CatBoost: same churn-prediction task, same data, head to head.**

This project uses the Telco customer churn dataset (7,043 customers; contract type, tenure, internet service, monthly charges, payment method, add-on services and other categorical-heavy fields) to predict which customers will cancel. About 26.5% of customers churn. The *same* task is trained on all three major boosting libraries so the comparison itself is the point, not three isolated tutorials.

---

![Training and validation log loss for XGBoost, LightGBM and CatBoost](outputs/figures/all_libraries_loss.png)

## 🎯 Project Questions

- How does a single tree's errors get corrected by the next tree, and can you see that in a training loss curve?
- How much does tuning max_depth, learning_rate, and subsample actually move validation ROC-AUC?
- How much faster is LightGBM than XGBoost/CatBoost on this dataset, and does CatBoost's native categorical handling actually help accuracy?
- Where does early stopping kick in for each library, and what happens to validation loss if you ignore it?

## Findings

1. **The three libraries land in the same place:** test ROC-AUC is 0.8474 (XGBoost), 0.8376 (LightGBM) and 0.8477 (CatBoost). XGBoost and CatBoost are a tie, and LightGBM is about 0.01 lower. With a 1,409-row test set, differences this small should not be over-read.
2. **Native categorical handling gave CatBoost no clear accuracy edge on the test set:** it has the best accuracy (0.8062), precision (0.6747) and F1 (0.5882), but only slightly. Its benefit here is convenience: no manual one-hot encoding. It did reach the lowest validation log loss (0.418, against 0.446 for XGBoost and 0.442 for LightGBM).
3. **Speed:** single-fit training times were 2.74 s for LightGBM, 4.14 s for XGBoost and 11.89 s for CatBoost. LightGBM was about 1.5x faster than XGBoost and about 4x faster than CatBoost. Each model uses its own settings, so this is a practical comparison, not a controlled benchmark.
4. **Shallow trees won the tuning:** the best XGBoost model used `max_depth=3`, `learning_rate=0.03` and 100 trees (validation AUC 0.8130). Very deep trees (depth 40 to 50) scored about 0.75 to 0.77. After roughly 1,900 more fits, a much larger grid ended at the same validation AUC (about 0.813), so this feature set has a ceiling that tuning alone does not lift.
5. **Boosting curves flatten quickly:** validation loss drops steeply over the first tens of trees, then levels off as each new tree fits smaller residuals. XGBoost's curve was nearly flat from about tree 400, and CatBoost's best validation loss came at tree 464.
6. **Ignoring early stopping means overfitting:** LightGBM's training loss keeps falling (to about 0.33) while its validation loss stays flat near 0.44. The widening gap is memorization, not learning.
7. **Recall is the weak spot:** at the default 0.5 threshold, every model catches only about half of the churners (recall 0.49 to 0.53). A real retention campaign would tune the threshold to the cost of missing a churner versus contacting a loyal customer.

| Library | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---|---|---|---|---|
| XGBoost | 0.7991 | 0.6631 | 0.4947 | 0.5666 | 0.8474 |
| LightGBM | 0.8006 | 0.6545 | 0.5267 | 0.5837 | 0.8376 |
| CatBoost | 0.8062 | 0.6747 | 0.5214 | 0.5882 | 0.8477 |

*Test-set metrics, scored once after all tuning decisions were made on the validation set.*

---

## 📁 Repository Structure

```
churn-boosting-showdown/
├── data/
│   ├── raw/                   # Untouched source churn dataset
│   └── processed/             # Cleaned, encoded (where needed), train/val/test split
│
├── notebooks/                  # Step-by-step, one notebook per phase
│   ├── 01_load_explore.ipynb
│   ├── 02_boosting_theory_single_tree.ipynb
│   ├── 03_xgboost_tuning.ipynb
│   ├── 04_lightgbm_vs_catboost.ipynb
│   ├── 05_early_stopping_regularization.ipynb
│   └── 06_final_comparison.ipynb
│
├── src/                         # Reusable code, imported by notebooks/scripts (not copy-pasted)
│   ├── __init__.py
│   ├── data_load.py            # Load raw dataset, drop customerID, map Churn to 0/1
│   ├── preprocess.py            # Cleaning, stratified split, encoding (differs per library, see notes below)
│   ├── train_xgboost.py          # XGBoost training function
│   ├── train_lightgbm.py          # LightGBM training function (manual categorical encoding)
│   ├── train_catboost.py           # CatBoost training function (native categorical handling)
│   └── evaluate.py                  # Test metrics, training timing, and loss-curve comparison plot
│
├── tests/                       # Unit tests for src/ functions
│   ├── __init__.py
│   └── test_preprocess.py
│
├── models/                      # Saved trained models per library (.joblib), gitignored
│
├── outputs/
│   └── figures/                   # Overlaid train/val loss curves, comparison charts
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠️ Setup

```bash
git clone https://github.com/hexsyro/churn-boosting-showdown
cd churn-boosting-showdown
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🚀 Usage

1. **Add the raw dataset**: download [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn/data) and place it at `data/raw/Telco_customer_churn.csv`. Keep the original file unchanged, since the pipeline reads it.
2. **Run the pipeline** from the project root, in this order:
   ```bash
   python -m src.data_load        # drop customerID, map Churn to 0/1
   python -m src.preprocess       # stratified train/val/test split + encoding
   python -m src.train_xgboost
   python -m src.train_lightgbm
   python -m src.train_catboost
   python -m src.evaluate         # test metrics + loss-curve figure
   ```
   `preprocess` writes two versions of each split: one-hot encoded for XGBoost/LightGBM, and the original categorical columns for CatBoost, which handles them natively.
3. **Explore in notebooks**, in order, starting with `notebooks/01_load_explore.ipynb`

   | Notebook | Open |
   |---|---|
   | 01 Load and explore | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/hexsyro/churn-boosting-showdown/blob/main/notebooks/01_load_explore.ipynb) |
   | 02 Boosting theory: single tree | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/hexsyro/churn-boosting-showdown/blob/main/notebooks/02_boosting_theory_single_tree.ipynb) |
   | 03 XGBoost tuning | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/hexsyro/churn-boosting-showdown/blob/main/notebooks/03_xgboost_tuning.ipynb) |
   | 04 LightGBM vs CatBoost | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/hexsyro/churn-boosting-showdown/blob/main/notebooks/04_lightgbm_vs_catboost.ipynb) |
   | 05 Early stopping and regularization | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/hexsyro/churn-boosting-showdown/blob/main/notebooks/05_early_stopping_regularization.ipynb) |
   | 06 Final comparison | [![Open in Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/hexsyro/churn-boosting-showdown/blob/main/notebooks/06_final_comparison.ipynb) |

4. `notebooks/06_final_comparison.ipynb` produces the final comparison table and overlaid
   loss-curve plot

---

## 📊 Skills Practiced

| Skill | Where |
|---|---|
| Boosting theory (sequential tree building) | `notebooks/02` |
| XGBoost parameters and tuning basics | `notebooks/03`, `src/train_xgboost.py` |
| LightGBM vs. CatBoost tradeoffs (speed, categorical handling) | `notebooks/04`, `src/train_lightgbm.py`, `src/train_catboost.py` |
| Early stopping and regularization | `notebooks/05`, all `src/train_*.py` |
| Train/validation/test discipline (tune on validation, score test once) | `src/preprocess.py`, `src/evaluate.py` |

---

## 📈 Sample Finding

> LightGBM trained about 1.5x faster than XGBoost and about 4x faster than CatBoost, but XGBoost
> and CatBoost tied on test ROC-AUC (0.847 vs 0.848) with LightGBM slightly behind (0.838).
> CatBoost, using native categorical handling with zero manual encoding, matched XGBoost's
> accuracy. The real tradeoff here was engineering convenience and training time, not accuracy.

---

## 📄 Data Sources

- Churn dataset: [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn/data)

---

## 🔭 Possible Extensions

- Add SHAP values to compare which features each library considers most important
- Run a larger RandomizedSearchCV per library and see if the ranking changes with more
  tuning budget
- Tune the decision threshold (or use `scale_pos_weight`) to raise churner recall, and compare
  libraries on precision-recall AUC, not only ROC-AUC
- Test all three on a much larger synthetic version of the dataset to see if the speed
  gap widens or narrows