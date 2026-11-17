[![LinkedIn][linkedin-shield]][linkedin-url]
[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![MIT License][license-shield]][license-url]
[![Downloads][downloads-shield]][downloads-url]
[![Month Downloads][downloads-month-shield]][downloads-month-url]

[contributors-shield]: https://img.shields.io/github/contributors/TsLu1s/MLimputer.svg?style=for-the-badge&logo=github&logoColor=white
[contributors-url]: https://github.com/TsLu1s/MLimputer/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/TsLu1s/MLimputer.svg?style=for-the-badge&logo=github&logoColor=white
[stars-url]: https://github.com/TsLu1s/MLimputer/stargazers
[license-shield]: https://img.shields.io/github/license/TsLu1s/MLimputer.svg?style=for-the-badge&logo=opensource&logoColor=white
[license-url]: https://github.com/TsLu1s/MLimputer/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/luisfssantos98/
[downloads-shield]: https://static.pepy.tech/personalized-badge/mlimputer?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Total%20Downloads
[downloads-url]: https://pepy.tech/project/mlimputer
[downloads-month-shield]: https://static.pepy.tech/personalized-badge/mlimputer?period=month&units=international_system&left_color=grey&right_color=blue&left_text=Month%20Downloads
[downloads-month-url]: https://pepy.tech/project/mlimputer

<br>
<p align="center">
  <h2 align="center"> MLimputer: Missing Data Imputation Framework for Machine Learning
  <br>
  
## Framework Contextualization: Advanced Missing Data Imputation for Tabular Data

The `MLimputer` project provides a comprehensive and integrated framework to automate the handling of missing values in datasets through advanced machine learning imputation. It aims to reduce bias and increase the precision of imputation results compared to traditional methods by leveraging supervised learning algorithms.

This package offers multiple algorithm options to impute your data, where each column with missing values is predicted using robust preprocessing and state-of-the-art machine learning models.

The architecture includes three main components:
* **Missing Data Analysis**: Automatic detection and pattern analysis of missing values
* **Data Preprocessing**: Intelligent handling of categorical and numerical features
* **Supervised Model Imputation**: Multiple ML algorithms for accurate value prediction

### Key Capabilities

* **General applicability on tabular datasets**: Works with any tabular data for both regression and classification tasks
* **Robust preprocessing**: Automatic handling of categorical encoding (`AutoLabelEncoder`) and per-column feature-side fill (`AutoSimpleImputer`) — both are *helpers*; the selected `imput_model` writes every imputed value
* **Multiple imputation strategies**: Choose from 6 different ML algorithms (`RandomForest`, `ExtraTrees`, `GBR`, `KNN`, `XGBoost`, `CatBoost`) based on your data characteristics
* **Configurable feature-side fill**: `feature_fill_strategy` lets you pick `mean` (default), `median`, or `most_frequent` for the per-column bridge
* **No NaN left behind in numeric columns**: a numeric column that only shows missing values *after* fitting is covered by the `unseen_missing` policy (`"fill"` by default, or `"ignore"` / `"raise"`)
* **scikit-learn compatible**: `MLimputer` is a scikit-learn transformer — use it in a `Pipeline`, `clone` it, or tune it with `GridSearchCV`
* **Leakage-free evaluation**: `Evaluator` fits the imputer **per fold** on training rows only — no validation data leaks into the imputation step; classification folds are stratified and every score is reported with its fold-to-fold standard deviation
* **Reproducible**: every strategy is seeded by default, so two fits on the same data give identical imputations
* **Production ready**: Save and load fitted imputers for deployment with `ModelSerializer` (joblib + metadata sidecar recording the package version)

## Framework Workflow

The diagram below follows one small table through the whole pipeline — six rows with missing cells — and shows, layer by layer, how each column is fitted, how the missing cells are filled, and how imputation strategies are compared. Every value in it is real MLimputer output on that table.

<p align="center">
  <a href="https://github.com/TsLu1s/mlimputer/blob/main/docs/mlimputer_workflow.drawio.png">
    <img src="https://raw.githubusercontent.com/TsLu1s/mlimputer/main/docs/mlimputer_workflow.drawio.png" alt="MLimputer pipeline: preparation, per-column fitting traced layer by layer on an example table, imputation before and after, leakage-free evaluation with a leaderboard, and outputs" width="100%"/>
  </a>
</p>

### Relevant Point

> **The selected `imput_model` (`RandomForest`, `ExtraTrees`, `GBR`, `KNN`, `XGBoost`, or `CatBoost`) is what writes every imputed missing value.** `AutoLabelEncoder` and `AutoSimpleImputer` are *per-column feature-side helpers* — they prepare the feature matrix so the model can train and predict, and they **never touch the target column being imputed**.

### Pipeline at a glance

| Stage | What happens | Key components |
|-------|--------------|----------------|
| ① **Preparation** | Validate the input (pandas DataFrame, unique column names, no all-NaN column) · resolve the strategy name and validate its hyperparameters · classify columns: numeric columns with NaN become **targets**, categorical and boolean columns are features only, datetime columns pass through · order targets by missing share. | `StrategyMapper` · Pydantic schemas |
| ② **Per-Column Fitting** | For each target column: take the rows where it is observed → encode categorical features (`AutoLabelEncoder`) → fill NaN in the *other* features (`AutoSimpleImputer`, `feature_fill_strategy`) → **fit the selected `imput_model` (features → this column)** → store the bundle `{model, encoder, simple_imputer, feature_columns}`. | `AutoLabelEncoder` · `AutoSimpleImputer` · **`imput_model`** |
| ③ **Imputation** | `transform(X)` replays each bundle in fit order on the rows where that column is missing and writes the predictions into those cells only, keeping the column dtype. A numeric column that had no NaN at fit time has no model and follows `unseen_missing` (`fill` · `ignore` · `raise`). | `ImputationState` |
| ④ **Evaluation** *(optional)* | `Evaluator` compares strategies by the score of the model trained afterwards: per strategy and per fold, the imputer is fitted on the training fold only, both halves are imputed, and a fresh clone of each model is scored. Results are ranked by MAE (regression) or F1 (classification) with mean ± std; `evaluate_test_set` scores the winner on held-out data. | `Evaluator` · `CrossValidator` · `MetricsCalculator` |
| ⑤ **Output** | `transform(X)` returns the imputed DataFrame (nothing is written automatically) · `ModelSerializer.save` writes `<name>.joblib` (or `.pkl`) plus a `<name>.meta.json` sidecar · the `Evaluator` returns the leaderboard and the best strategy. | `ModelSerializer` · optional `RunOutputManager` |

### Why per-column?

Each numeric column with missing values gets its **own** fitted `imput_model`, `AutoLabelEncoder`, and `AutoSimpleImputer` — all trained only on the rows where that specific column is non-null. The missing pattern of column A never contaminates the model for column B, and `column_order` is preserved so transform-time replay is deterministic and leakage-free.

### Main Development Tools

Major frameworks used to build this project:
* [Pandas](https://pandas.pydata.org/) - Data manipulation and analysis
* [Scikit-learn](https://scikit-learn.org/stable/) - Core ML algorithms
* [XGBoost](https://xgboost.ai/) - Gradient boosting
* [CatBoost](https://catboost.ai/) - Gradient boosting with categorical support
* [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation

## Installation

Binary installer for the latest released version is available at the Python Package Index [(PyPI)](https://pypi.org/project/mlimputer/).

```bash
pip install mlimputer
```

GitHub Project Link: [https://github.com/TsLu1s/MLimputer](https://github.com/TsLu1s/MLimputer)

## Quick Start Guide

### Basic Usage Example

The first step is to import the package, load your dataset, and choose an imputation model. Available imputation models are:
* `RandomForest`
* `ExtraTrees`
* `GBR`
* `KNN`
* `XGBoost`
* `CatBoost`

```python
import pandas as pd
from mlimputer import MLimputer
from mlimputer.schemas.parameters import imputer_parameters
from mlimputer.utils.splitter import DataSplitter
import warnings
warnings.filterwarnings("ignore")

# Load your data
data = pd.read_csv('your_dataset.csv')

# Split with automatic index reset (a convenience — MLimputer works with any index)
splitter = DataSplitter(random_state=42)
X_train, X_test, y_train, y_test = splitter.split(
    data.drop(columns=['target']), 
    data['target'], 
    test_size=0.2
)

# Configure imputation parameters (optional)
params = imputer_parameters()
params["RandomForest"]["n_estimators"] = 50
params["RandomForest"]["max_depth"] = 10

# Create and fit imputer
# (feature_fill_strategy controls the per-column AutoSimpleImputer bridge:
#  "mean" (default), "median", or "most_frequent";
#  unseen_missing decides what happens to NaN in a numeric column that had no
#  missing value at fit time: "fill" (default), "ignore" or "raise")
imputer = MLimputer(
    imput_model="RandomForest",
    imputer_configs=params,
    feature_fill_strategy="mean",
    unseen_missing="fill",
)
imputer.fit(X=X_train)

# Transform datasets — the selected imput_model writes every imputed value
X_train_imputed = imputer.transform(X=X_train)
X_test_imputed = imputer.transform(X=X_test)

# Save fitted imputer for production use
import pickle
with open("fitted_imputer.pkl", 'wb') as f:
    pickle.dump(imputer, f)
```

### Advanced Configuration

Customize imputation model hyperparameters for better performance:

```python
from mlimputer.schemas.parameters import imputer_parameters, update_model_config

# Get default parameters
params = imputer_parameters()

# Method 1: Direct modification
params["KNN"]["n_neighbors"] = 7
params["KNN"]["weights"] = "distance"

# Method 2: Using update function with validation
params["RandomForest"] = update_model_config(
    "RandomForest",
    {"n_estimators": 100, "max_depth": 15, "min_samples_split": 5}
)

# Method 3: any other option of the underlying estimator is passed through
params["RandomForest"]["n_jobs"] = -1          # scikit-learn option, not in the schema
params["XGBoost"]["tree_method"] = "hist"      # XGBoost option

# Apply different strategies
strategies = ["RandomForest", "KNN", "XGBoost"]
for strategy in strategies:
    imputer = MLimputer(imput_model=strategy, imputer_configs=params)
    imputer.fit(X=X_train)
    print(f"{strategy}: {imputer.get_summary()['n_columns_imputed']} columns imputed")

# A flat dict is read as hyperparameters of the selected model
imputer = MLimputer(imput_model="KNN", imputer_configs={"n_neighbors": 7})
```

Hyperparameters are checked when `MLimputer` is constructed: an out-of-range value or a misspelled name (`n_estimatorz`) raises immediately instead of being ignored. `KNN` standardises features before measuring distances (`scale_features=True`); set it to `False` for raw distances.

### Use in a scikit-learn Pipeline

`MLimputer` follows the scikit-learn transformer protocol (`fit(X, y=None)`, `transform`, `get_params`, `set_params`), so it can be cloned, grid-searched and chained. It takes and returns pandas DataFrames.

```python
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

pipeline = Pipeline([
    ("impute", MLimputer(imput_model="ExtraTrees", show_progress=False)),
    ("model", RandomForestRegressor(n_estimators=100, random_state=42)),
])
pipeline.fit(X_train, y_train)            # numeric features; encode categoricals before the model
predictions = pipeline.predict(X_test)

# The imputation strategy is just another hyperparameter
search = GridSearchCV(pipeline, {"impute__imput_model": ["ExtraTrees", "KNN", "XGBoost"]}, cv=3)
```

## Performance Evaluation

The MLimputer framework includes a robust evaluation module to assess and compare different imputation strategies. This helps you select the most effective approach for your specific dataset.

### Evaluation Framework

```python
from mlimputer.evaluation.evaluator import Evaluator
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression

# Define evaluation parameters
imputation_strategies = ["RandomForest", "ExtraTrees", "GBR", "KNN"]

# Evaluator takes FULL DataFrames that still contain the supervised target column
train_data, test_data = splitter.split(data, test_size=0.2)

# Choose models based on your task
from mlimputer.evaluation.detection import detect_problem_type

if detect_problem_type(train_data['target']).value != "regression":  # Classification
    models = [
        LogisticRegression(max_iter=1000),
        RandomForestClassifier(n_estimators=50)
    ]
else:  # Regression
    models = [
        LinearRegression(),
        RandomForestRegressor(n_estimators=50)
    ]

# Initialize evaluator
evaluator = Evaluator(
    imputation_models=imputation_strategies,
    train=train_data,
    target="target",
    n_splits=3,  # Cross-validation folds
    hparameters=params
)

# Run cross-validation evaluation
# (each fold trains fresh clones, so `models` stays unfitted; aggregate rows
#  carry "<METRIC> Mean" and "<METRIC> Std" columns)
cv_results = evaluator.evaluate_imputation_models(models=models)

# Get best performing imputation strategy
best_imputer = evaluator.get_best_imputer()
print(f"Best imputation strategy: {best_imputer}")
print(evaluator.get_metric_comparison())   # mean ± std per (model, imputer)
print(evaluator.get_failures())            # folds that could not be evaluated, if any

# Evaluate on test set
test_results = evaluator.evaluate_test_set(
    test=test_data,
    imput_model=best_imputer,
    models=models
)
```

### Custom Cross-Validation

For more control over the evaluation process:

```python
from mlimputer.evaluation.cross_validation import CrossValidator, CrossValidationConfig

# Configure custom cross-validation
custom_config = CrossValidationConfig(
    n_splits=5,
    shuffle=True,
    random_state=42,
    verbose=1,
    fold_strategy="auto",  # stratified for classification, K-fold for regression
)                          # ("kfold" / "stratified" force one or the other)

# Create validator
validator = CrossValidator(config=custom_config)

# CrossValidator takes ONE frame holding the features AND the supervised target column
imputed_train = imputer.transform(X=train_data)

# Run validation
results = validator.validate(
    X=imputed_train,
    target='target',
    models=models,
    problem_type="regression"  # or "binary_classification", "multiclass_classification"
)

# Get leaderboard
leaderboard = validator.get_leaderboard()
print(leaderboard.head())
```

## Working with Generated Data

MLimputer includes utilities for generating datasets with missing values for testing:

> Example data only — bring your own real dataset for actual use.

```python
from mlimputer.data.data_generator import ImputationDatasetGenerator

generator = ImputationDatasetGenerator(random_state=42)

# Regression dataset
X_reg, y_reg = generator.quick_regression(
    n_samples=2000, 
    missing_rate=0.15
)

# Binary classification
X_bin, y_bin = generator.quick_binary(
    n_samples=2000, 
    missing_rate=0.15
)

# Multiclass classification
X_multi, y_multi = generator.quick_multiclass(
    n_samples=2000,
    n_classes=4,
    missing_rate=0.15,
    n_categorical=3  # Include categorical features
)
```

## Production Deployment

### Saving and Loading Models
```python
from mlimputer.utils.serialization import ModelSerializer

# Save with metadata
ModelSerializer.save(
    obj=imputer,
    filepath="production_imputer.joblib",
    format="joblib",
    metadata={
        "model": "RandomForest",
        "train_shape": X_train.shape,
        "version": "1.0"
    }
)

# Load with metadata
loaded_imputer, metadata = ModelSerializer.load_with_metadata(
    filepath="production_imputer.joblib",
    format="joblib"
)

# Use loaded imputer on new, unseen data (same feature columns as training)
new_data_imputed = loaded_imputer.transform(X_test)
```

## Important Notes

* **Index-safe by construction**: The per-column fit loop uses positional indices internally (`np.where` on the null mask), so a non-default DataFrame index will not misalign training rows. `DataSplitter` is still convenient but no longer required for correctness.
* **Categorical Handling**: The framework automatically detects and encodes categorical *features* (`AutoLabelEncoder`). Categorical columns are never themselves ML-imputed; only numeric columns with NaN become targets. The same holds for boolean columns, and columns of any other dtype (datetime, timedelta, …) are passed through unchanged and not used as features.
* **Dtype preservation**: imputed values are written back in the column's own dtype — `float32` stays `float32`, and nullable integer columns (`Int64`) receive rounded integers.
* **Unseen missing values**: a numeric column with no missing value at fit time has no model. If NaN shows up in it at transform time, `unseen_missing="fill"` (default) fills it with that column's fit-time `feature_fill_strategy` statistic and logs a warning; `"ignore"` leaves the NaN, `"raise"` raises. Fit on data that contains missing values in a column to get model-based imputation for it.
* **Column-drift guardrail**: `transform()` raises `ValueError` if any column the imputer was fit on (a fitted target or one of its features) is missing from the input — silent partial imputation is not allowed. Extra columns are passed through; column order does not matter.
* **Unseen-category warning**: At transform time, `AutoLabelEncoder` logs a warning when it sees a categorical value that was not present at fit time (the value is mapped to the reserved `Unknown` index).
* **Missing Pattern Preservation**: The imputer learns missing patterns from training data for consistent imputation. At transform time, feature extraction uses a frozen baseline of the input — column B's model never sees column A's ML-imputed value as a feature, matching what fit-time saw.
* **Leakage-free CV**: When you use `Evaluator.evaluate_imputation_models`, imputation and label encoding are fit *per fold* on training rows only. Failures are captured in `evaluator.get_failures()` instead of being silently dropped. Invalid inputs (unknown strategy name, bad hyperparameter, missing target column, NaN in the target) raise when the `Evaluator` is created.
* **Logging**: progress messages go to stdout at `INFO`; silence them with `from mlimputer import logger; logger.set_level("WARNING")`. A rotating log file is written to `~/.mlimputer/logs` when that location is writable — redirect it with `MLIMPUTER_LOG_DIR` or turn it off with `MLIMPUTER_DISABLE_FILE_LOGS=1`.
* **Loading saved imputers**: `joblib`/`pickle` files execute code when loaded — only load files from a source you trust. Imputers saved with MLimputer 2.1.0 still load and transform identically.

## Example Notebooks

### 1. Basic Usage Example
A complete walkthrough demonstrating fundamental imputation workflow:
- Dataset generation with controlled missing patterns
- Train/test splitting with automatic index handling  
- Model configuration and fitting
- Imputation and evaluation
- Saving fitted models for production

[View Basic Example](https://github.com/TsLu1s/mlimputer/blob/main/examples/basic_usage.py) 

### 2. Performance Evaluation Example
Comprehensive evaluation comparing multiple imputation strategies:
- Cross-validation setup for robust evaluation
- Comparison of 6 different imputation algorithms
- Custom evaluation configurations
- Best model selection based on metrics
- Production deployment preparation

[View Evaluation Example](https://github.com/TsLu1s/mlimputer/blob/main/examples/performance_evaluation.py)

### 3. Detailed Analysis Example
In-depth analysis of a single imputation strategy:
- Column-wise missing data patterns
- Fold-by-fold cross-validation results
- Feature importance analysis
- Test set predictions and metrics
- Comprehensive performance reporting

[View Detailed Analysis →](https://github.com/TsLu1s/MLimputer/blob/main/examples/singular_analysis.py)

## Interactive Notebooks

For a more interactive experience, feel free to explore the Jupyter notebooks with step-by-step execution and guidelines:

📓 **[Interactive Notebooks](https://github.com/TsLu1s/mlimputer/blob/main/examples/notebooks)**

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Citation

If you use MLimputer in your research, please cite:
```bibtex
@software{mlimputer,
  author = {Luis Fernando Santos},
  title = {MLimputer: Missing Data Imputation Framework for Supervised Machine Learning},
  year = {2023},
  url = {https://github.com/TsLu1s/MLimputer}
}
```
    
## License

Distributed under the MIT License. See [LICENSE](https://github.com/TsLu1s/MLimputer/blob/main/LICENSE) for more information.

## Contact 
 
Luis Santos - [LinkedIn](https://www.linkedin.com/in/luisfssantos98/)
