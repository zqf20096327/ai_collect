# Laravel ML

[![tests](https://github.com/beziworld/laravel-ml/actions/workflows/tests.yml/badge.svg)](https://github.com/beziworld/laravel-ml/actions/workflows/tests.yml)
[![Latest Version](https://img.shields.io/packagist/v/beziworld/laravel-ml.svg)](https://packagist.org/packages/beziworld/laravel-ml)
[![License](https://img.shields.io/packagist/l/beziworld/laravel-ml.svg)](LICENSE.md)

Laravel-first machine learning in plain PHP. Everything [php-ml](https://github.com/jorgecasas/php-ml) offered
(classification, regression, clustering, Apriori, cross validation, TF-IDF, preprocessing, metrics, persistence,
neural networks), built on the maintained [Rubix ML](https://rubixml.com) 3 engine and wrapped in the things a Laravel
application actually needs:

- datasets straight from Eloquent (`fromQuery()` streams with `lazy()`), collections, arrays and CSV files
- feature casting: numbers, categories, booleans, dates, free text; imputation, one-hot encoding, normalisation, TF-IDF
- model definitions as classes (`ChurnModel extends ClassificationModel`) or an ad-hoc fluent builder
- presets: classifier, regressor, clusterer, anomaly detector, KNN recommender, text classifier (spam / sentiment)
- Apriori association rules over Laravel collections (Rubix has none, php-ml had one)
- holdout and k-fold cross validation with a typed `TrainingReport` (accuracy, precision, recall, F1, MCC, confusion
  matrix, MAE, RMSE, R², silhouette, V-measure)
- versioned models on any filesystem disk (`v1`, `v2`, ...), metadata JSON, promotion, rollback, pruning
- signed model files: SHA-256 + HMAC verification and a restricted `allowed_classes` list before `unserialize()`
- predictions as JSON-friendly DTOs, `HasPredictions` trait, `AsPrediction` cast, `ClassifiedAs` and `NotAnomalous`
  validation rules
- queued training (`TrainModel` job), events, Artisan commands, a data drift check for nightly monitoring

[Polska wersja dokumentacji](README.pl.md)

## Why this package

| | php-ml | Rubix ML alone | laravel-ml |
| --- | --- | --- | --- |
| Maintained, PHP 8.3+ | no (abandoned, last fork push 2023) | yes | yes (Rubix 3.3) |
| Algorithms | ~25 | 40+ | Rubix + Apriori + silhouette |
| Eloquent / collections as data source | no | no | yes, streamed |
| Feature casting (dates, enums, text, missing values) | manual | manual | declarative |
| Model versions, promotion, rollback | no | no | yes |
| Safe loading of model files | no | crc32 checksum only | SHA-256 + HMAC + class allowlist |
| Queue, events, Artisan, validation rules, casts | no | no | yes |

Existing Laravel packages (checked on Packagist and GitHub in November 2026): a search for `php-ml laravel` returns
nothing; `torian257x/ai-php-rubix-wrap-laravel` (72 downloads, last change 2022) is a thin wrapper without
persistence, versioning or validation; `divineomega/eloquent-attribute-value-prediction` predicts a single Eloquent
attribute. Neither covers cross validation reports, versioned storage, text classification, recommendations,
association rules or drift checks.

## Installation

```bash
composer require beziworld/laravel-ml
php artisan vendor:publish --tag=ml-config   # optional
```

Requirements: PHP 8.3+, Laravel 12 or 13, `ext-zlib`. The optional
[Tensor extension](https://github.com/RubixML/Tensor) speeds up linear models and neural networks considerably.

Everything works without configuration. Optional `.env` settings:

```dotenv
ML_DISK=local              # filesystem disk for model files
ML_PATH=ml-models          # directory on that disk
ML_AUTO_PROMOTE=true       # activate every freshly trained version
ML_KEEP_VERSIONS=5         # versions kept by ml:prune
ML_VALIDATION=holdout      # holdout, kfold or none
ML_HOLDOUT_RATIO=0.2
ML_FOLDS=5
ML_SEED=42                 # reproducible training (mt_srand)
ML_MEMORY_LIMIT=2G         # applied while training
ML_TIME_LIMIT=1800         # set_time_limit() and the queued job timeout
ML_QUEUE=ml                # queue of the TrainModel job
ML_QUEUE_CONNECTION=redis
ML_SIGNING_KEY=            # HMAC key for model files, defaults to APP_KEY
ML_PREDICTION_EVENTS=false # dispatch PredictionMade
ML_PREDICTION_SAMPLE_RATE=0.05
```

Short aliases for Artisan commands go to `config/ml.php`: `'models' => ['churn' => App\Ml\ChurnModel::class]`.

## Quick start: churn prediction

```php
namespace App\Ml;

use App\Models\User;
use Beziworld\Ml\Dataset\Feature;
use Beziworld\Ml\Models\ClassificationModel;
use Illuminate\Database\Eloquent\Builder;

final class ChurnModel extends ClassificationModel
{
    public function features(): array
    {
        return [
            'plan' => 'categorical',
            'age',                                   // type inferred from the data
            'monthly_spend' => 'numeric',
            'last_login_at' => 'date',               // days since epoch
            Feature::numeric('orders', fn (User $user) => $user->orders_count),
        ];
    }

    public function label(): string
    {
        return 'churned';                           // bool attribute, classes "true" / "false"
    }

    public function query(): Builder
    {
        return User::query()->withCount('orders')->whereNotNull('churned');
    }
}
```

```php
use App\Ml\ChurnModel;
use Beziworld\Ml\Facades\Ml;
use Beziworld\Ml\Training\Validation;

$report = Ml::train(ChurnModel::class);                       // holdout validation by default
$report = Ml::train(ChurnModel::class, validation: Validation::kFold(5));

$report->version;                    // "v3"
$report->metric('accuracy');         // 0.93
$report->metric('f1');
$report->confusionMatrix;            // ['true' => ['true' => 41, 'false' => 3], 'false' => [...]] (actual => predicted)

$prediction = Ml::predict(ChurnModel::class, $user);
$prediction->value;                  // "true"
$prediction->is(true);               // true
$prediction->probabilities;          // ['true' => 0.87, 'false' => 0.13]
$prediction->confidence;             // 0.87
$prediction->toArray();              // JSON-friendly, ready for an API response

Ml::predictMany(ChurnModel::class, User::query()->active()->cursor());   // Collection<Prediction>
```

The default classifier is a random forest. Override `estimator()` to choose another one, either a Rubix object or a
preset name from `Estimators`:

```php
use Beziworld\Ml\Models\Estimators;
use Rubix\ML\Classifiers\KNearestNeighbors;

public function estimator(): Learner&Estimator
{
    return new KNearestNeighbors(7, weighted: true);   // or Estimators::classifier('naive_bayes')
}
```

`estimator()` and `transformers()` are called once per cross validation fold, so always return new instances.

## Quick start: spam filter (text classification)

```php
use Beziworld\Ml\Models\TextClassificationModel;

final class SpamFilter extends TextClassificationModel
{
    public function text(): string { return 'body'; }
    public function label(): string { return 'is_spam'; }
    public function stopWords(): string { return 'english'; }   // or 'polish', 'french', or a list
    public function ngrams(): int { return 2; }                 // words and word pairs

    public function query(): Builder { return Message::query()->whereNotNull('is_spam'); }
}
```

The text is lower-cased, stop words are removed, tokens are counted (`WordCountVectorizer`) and weighted with TF-IDF
before a softmax classifier is trained. Use it in validation:

```php
use Beziworld\Ml\Rules\ClassifiedAs;

$request->validate([
    'body' => ['required', new ClassifiedAs(SpamFilter::class, 'false', minConfidence: 0.7)],
]);
```

## Quick start: product recommendations

```php
use Beziworld\Ml\Models\RecommendationModel;

final class SimilarProducts extends RecommendationModel
{
    public function features(): array
    {
        return ['category_id' => 'categorical', 'price' => 'numeric', 'rating' => 'numeric', 'description' => 'text'];
    }

    public function query(): Builder { return Product::query()->where('active', true); }
    public function neighbours(): int { return 4; }
}

Ml::train(SimilarProducts::class);

$product->recommendations(SimilarProducts::class);    // Collection<Recommendation>, the product itself excluded
// [Recommendation{key: 18, distance: 0.21, similarity: 0.83}, ...]
```

Items are indexed by their transformed feature vectors in a ball tree; the nearest items are recommended. For
"customers who bought X also bought Y" use Apriori (below).

## Quick start: anomaly detection on orders

```php
use Beziworld\Ml\Models\AnomalyDetectionModel;

final class OrderAnomalies extends AnomalyDetectionModel
{
    public function features(): array
    {
        return ['total' => 'numeric', 'items_count' => 'numeric', 'country' => 'categorical', 'created_at' => 'date'];
    }

    public function contamination(): ?float { return 0.02; }   // expected share of anomalies
    public function query(): Builder { return Order::query()->where('created_at', '>', now()->subYear()); }
}

$order->isAnomalous(OrderAnomalies::class);                 // bool
Ml::predict(OrderAnomalies::class, $order)->score;          // higher means more unusual

$request->validate(['order' => ['array', new NotAnomalous(OrderAnomalies::class)]]);
```

A label is optional: when the query returns a `label()` (e.g. a confirmed fraud flag), the report adds accuracy,
precision, recall and F1 next to the anomaly rate.

## Quick start: customer segmentation

```php
use Beziworld\Ml\Models\ClusteringModel;

final class CustomerSegments extends ClusteringModel
{
    public function features(): array { return ['recency_days' => 'numeric', 'orders' => 'numeric', 'revenue' => 'numeric']; }
    public function clusters(): int { return 4; }
    public function query(): Builder { return Customer::query(); }
}

$report = Ml::train(CustomerSegments::class);
$report->metric('silhouette');                               // -1..1, higher is better separated

Ml::predict(CustomerSegments::class, $customer)->value;      // cluster number, e.g. 2
```

## Ad-hoc models

No class needed for quick experiments:

```php
$report = Ml::model('lead-scoring')
    ->classifier('random_forest')                 // preset, Rubix object or factory closure
    ->features(['source' => 'categorical', 'visits' => 'numeric'])
    ->label('converted')
    ->using(Ml::dataset()->fromQuery(Lead::query()))
    ->train();

Ml::predict('lead-scoring', ['source' => 'ads', 'visits' => 7]);   // stored models are found by name
```

Presets: `classifier()` (`knn`, `naive_bayes`, `gaussian_nb`, `tree`, `random_forest`, `adaboost`, `bagging`,
`logistic`, `softmax`, `mlp`), `regressor()` (`ridge`, `least_squares`, `knn`, `tree`, `gradient_boost`, `adaline`,
`mlp`), `clusterer()` (`kmeans`, `dbscan`, `fuzzy_cmeans`, `gaussian_mixture`, `mean_shift`), `anomalyDetector()`
(`isolation_forest`, `local_outlier_factor`, `loda`, `gaussian_mle`, `robust_zscore`), `recommender()`,
`textClassifier()`. Neural networks: `Estimators::neuralNetwork([64, 32], epochs: 200)`.

## Datasets and preprocessing

```php
$dataset = Ml::dataset()
    ->fromQuery(User::query(), features: ['age', 'plan', 'signed_up_at'], label: 'churned', chunk: 500)
    ->get();

Ml::dataset()->fromCollection($rows, ['area', 'rooms'], 'price');
Ml::dataset()->fromCsv(storage_path('houses.csv'), ['area', 'rooms'], 'price', delimiter: ';');   // streamed
Ml::dataset()->fromArray([[1, 3], [1, 4], [2, 4]], ['a', 'a', 'b']);                            // php-ml style

$dataset->count(); $dataset->statistics(); $dataset->hash(); $dataset->toArray();
```

| Type | Accepted values | Sample value | Missing |
| --- | --- | --- | --- |
| `numeric` | int, float, numeric string, bool, int-backed enum | float | `NAN` |
| `categorical` | string, int, bool, enum, Stringable | string | `"?"` |
| `boolean` | bool, 0/1, "yes"/"no", "true"/"false", "on"/"off" | 1.0 / 0.0 | `NAN` |
| `date` | DateTimeInterface (Carbon), date string, Unix timestamp | days since epoch | `NAN` |
| `text` | string, array of strings | token counts / TF-IDF | `""` |

The automatic preprocessing (per feature group, built from the schema) imputes missing values (mean / most likely
category), normalises numeric columns (`zscore` by default, `minmax`, `robust`, `maxabs`), one-hot encodes categories
and turns text into TF-IDF weighted token counts. Configure it per model or per dataset:

```php
use Beziworld\Ml\Preprocessing\Preprocessing;

public function preprocessing(): ?Preprocessing
{
    return Preprocessing::defaults()->withNormalization('minmax')->withText(tfidf: true, stopWords: 'polish', ngrams: 2);
}

// or take full control with Rubix transformers:
public function transformers(): ?array
{
    return [new MissingDataImputer(), new OneHotEncoder(), new PrincipalComponentAnalysis(10)];
}

// exploratory: the transformed Rubix dataset
Ml::dataset()->fromCollection($rows, ['plan', 'spend'])->impute()->oneHot()->normalize('minmax')->toRubix();
```

## Cross validation and reports

`Validation::holdout(0.2)` (stratified for classifiers), `Validation::kFold(5)` (stratified, metrics from out-of-fold
predictions) or `Validation::none()`. Transformers are fitted inside every fold, so no information leaks from the test
data. After validation the final model is fitted on all samples.

| Task | Metrics in `TrainingReport::$metrics` |
| --- | --- |
| classifier | `accuracy`, `precision`, `recall`, `f1` (macro), `mcc`; plus `confusionMatrix` |
| regressor | `mae`, `rmse`, `r2` |
| clusterer | `silhouette`, `clusters`; with a label also `v_measure`, `homogeneity`, `completeness` |
| anomaly detector | `anomaly_rate`; with a label also `accuracy`, `precision`, `recall`, `f1` |
| recommender | `items` |

`Ml::evaluate(ChurnModel::class)` scores the active (or a given) version on the current data and returns an
`EvaluationReport`.

## Versions and persistence

```
storage/app/ml-models/churn-model/v1/model.bin       gzip-compressed model
storage/app/ml-models/churn-model/v1/metadata.json   features, label, metrics, statistics, hashes, versions
storage/app/ml-models/churn-model/active.json        {"version": "v1", "previous": null, ...}
```

`metadata.json` records the features and types, the label, the metrics and validation, `trained_at`, the SHA-256
dataset hash, feature statistics, the estimator class, the package, Rubix and PHP versions, the SHA-256 checksum, the
HMAC signature and the list of serialized classes.

```php
Ml::versions(ChurnModel::class);           // list<ModelMetadata>, ->active flags the active one
Ml::promote(ChurnModel::class, 'v2');
Ml::rollback(ChurnModel::class);           // activates the version before the active one
Ml::prune(ChurnModel::class, keep: 3);     // never deletes the active version
Ml::predict(ChurnModel::class, $user, version: 'v1');
```

Loaded models are cached per process (long-running workers and Octane reuse them).

## Security of model files

Model files are PHP serialized objects, and `unserialize()` on attacker-controlled data can lead to remote code
execution through magic methods of classes available in the application. Rubix's own `RBX` format only adds a crc32
checksum, which detects corruption but not tampering. This package therefore:

1. verifies the SHA-256 checksum of `model.bin` against the metadata,
2. verifies an HMAC-SHA256 signature (over the checksum and the class list) made with `ML_SIGNING_KEY` or `APP_KEY`;
   unsigned files are refused while `ML_REQUIRE_SIGNATURE=true` (the default),
3. refuses any recorded class outside `ml.security.allowed_namespaces` (`Rubix\ML\`, `Tensor\`, `OkBloomer\`,
   `Beziworld\Ml\`),
4. calls `unserialize()` with `allowed_classes` restricted to the recorded classes.

Still: never load model files that come from users, uploads or other applications, keep the model disk private, and
rotate the signing key together with retraining (files signed with an old key are refused). Anyone who can read
`APP_KEY` and write to the model disk can forge a model.

## Laravel extras

```bash
php artisan ml:train churn                      # alias from ml.models or a class name
php artisan ml:train "App\Ml\ChurnModel" --folds=10 --no-promote
php artisan ml:train churn --queue              # TrainModel job on ML_QUEUE
php artisan ml:evaluate churn v2                # metrics and confusion matrix on current data
php artisan ml:models                           # all models; ml:models churn lists versions with metrics
php artisan ml:promote churn v2
php artisan ml:rollback churn
php artisan ml:prune --keep=3
php artisan ml:drift churn                      # exit code 1 when the current data drifted
```

Nightly retraining and monitoring in `routes/console.php`:

```php
use Illuminate\Support\Facades\Schedule;

Schedule::command('ml:drift churn')->dailyAt('01:30')->onFailure(fn () => /* notify the team */ null);
Schedule::command('ml:train churn --queue')->dailyAt('02:00');
Schedule::command('ml:prune --keep=7')->weekly();
```

Jobs and events:

```php
Ml::queue(ChurnModel::class, Validation::kFold(5));   // TrainModel job: tries = 1, timeout = ML_TIME_LIMIT
```

| Event | Payload |
| --- | --- |
| `ModelTrained` | `TrainingReport $report`, `ModelMetadata $metadata` |
| `ModelPromoted` | `string $model`, `string $version`, `?string $previous` (also on rollback) |
| `PredictionMade` | `Prediction $prediction`, `array $features`; only with `ML_PREDICTION_EVENTS=true`, sampled by `ML_PREDICTION_SAMPLE_RATE` |

Eloquent integration:

```php
use Beziworld\Ml\Casts\AsPrediction;
use Beziworld\Ml\Concerns\HasPredictions;

class User extends Model
{
    use HasPredictions;

    protected function casts(): array
    {
        return ['churn_prediction' => AsPrediction::class];   // text / json column
    }
}

$user->churn_prediction = $user->predict(ChurnModel::class);
$user->save();
$user->churn_prediction->confidence;
```

## Data drift

```php
$report = Ml::drift(ChurnModel::class, User::query()->where('created_at', '>', now()->subMonth())->cursor());

$report->drifted();           // bool
$report->driftedFeatures();   // ['monthly_spend']
$report->feature('plan');     // FeatureDrift: meanShift, distributionShift, missingShift
```

Numeric, boolean and date features drift when the mean moves by more than `ML_DRIFT_MEAN_SHIFT` (0.5) training
standard deviations; categorical features when the total variation distance of category shares exceeds
`ML_DRIFT_DISTRIBUTION_SHIFT` (0.2); text when the average length changes by more than 50%; any feature when the
missing value rate changes by more than `ML_DRIFT_MISSING_SHIFT` (0.1). It is a simple statistical alarm, not a
replacement for monitoring model accuracy on labelled outcomes.

## Association rules (Apriori)

```php
$apriori = Ml::apriori(support: 0.02, confidence: 0.4)
    ->train(Order::with('items')->lazy()->map(fn ($order) => $order->items->pluck('sku')));

$apriori->frequentItemsets();   // Collection of ['items' => [...], 'support' => 0.031]
$apriori->rules();              // Collection<AssociationRule>: antecedent, consequent, support, confidence, lift
$apriori->predict(['SKU-1', 'SKU-7'], limit: 3);   // recommended SKUs for a basket
```

## Coming from php-ml

| php-ml | laravel-ml |
| --- | --- |
| `Classification\KNearestNeighbors` | `Estimators::classifier('knn')` / `Rubix\ML\Classifiers\KNearestNeighbors` |
| `Classification\NaiveBayes` | `Estimators::classifier('naive_bayes')` (categorical) or `'gaussian_nb'` |
| `Classification\SVC` | `Rubix\ML\Classifiers\SVC` (needs the `svm` extension) |
| `Classification\DecisionTree` | `Estimators::classifier('tree')` (CART) |
| `Classification\Ensemble\RandomForest` / `Bagging` / `AdaBoost` | `'random_forest'` / `'bagging'` / `'adaboost'` |
| `Classification\Linear\LogisticRegression` | `'logistic'` (binary) or `'softmax'` (multiclass) |
| `Classification\Linear\Adaline`, `Perceptron`, `DecisionStump` | `Estimators::regressor('adaline')`, `'logistic'`, `new ClassificationTree(1)` |
| `Classification\MLPClassifier` | `Estimators::neuralNetwork([hidden...])` |
| `Regression\LeastSquares` | `Estimators::regressor('least_squares')` / `'ridge'` |
| `Regression\SVR` | `Rubix\ML\Regressors\SVR` (needs `svm`) |
| `Regression\DecisionTreeRegressor` | `Estimators::regressor('tree')` / `'gradient_boost'` |
| `Clustering\KMeans` / `DBSCAN` / `FuzzyCMeans` | `Estimators::clusterer('kmeans' / 'dbscan' / 'fuzzy_cmeans')`, `ClusteringModel` |
| `Association\Apriori` | `Ml::apriori()` (`Beziworld\Ml\Association\Apriori`) |
| `CrossValidation\RandomSplit` / `StratifiedRandomSplit` | `Validation::holdout()` (stratified for classifiers), `Validation::kFold()` |
| `Metric\Accuracy`, `ConfusionMatrix`, `ClassificationReport` | `TrainingReport::$metrics`, `$confusionMatrix`; Rubix `MulticlassBreakdown` |
| `Metric\Regression` | `mae`, `rmse`, `r2` in the report |
| `FeatureExtraction\TokenCountVectorizer` + tokenizers | `text` features, `Preprocessing::withText(ngrams: n)` |
| `FeatureExtraction\TfIdfTransformer` | `Preprocessing::withText(tfidf: true)` |
| `FeatureExtraction\StopWords\English/French/Polish` | `StopWords::english()/french()/polish()`, `stopWords: 'polish'` |
| `Preprocessing\Normalizer` | `Preprocessing::withNormalization('zscore' / 'minmax' / 'robust' / 'maxabs')` |
| `Preprocessing\Imputer` | `Preprocessing::withImputation()` (`MissingDataImputer`) |
| `Preprocessing\OneHotEncoder`, `LabelEncoder`, `NumberConverter` | automatic per feature type |
| `Preprocessing\LambdaTransformer`, `ColumnFilter` | `Feature::numeric('x', fn ($row) => ...)`, the feature list itself |
| `Pipeline`, `FeatureUnion` | model definition + `transformers()`, `Preprocessing\ColumnTransformer` |
| `DimensionReduction\PCA` / `KernelPCA` / `LDA` | `Rubix\ML\Transformers\PrincipalComponentAnalysis` / `LinearDiscriminantAnalysis` in `transformers()` (no kernel PCA) |
| `FeatureSelection\VarianceThreshold` / `SelectKBest` | not covered; use tree feature importances (`RanksFeatures`) or a custom transformer |
| `Dataset\ArrayDataset` / `CsvDataset` / `FilesDataset` | `Ml::dataset()->fromArray()` / `fromCsv()` / `fromCollection()` |
| `ModelManager::saveToFile()` / `restoreFromFile()` | automatic versioned storage, `Ml::versions()`, `Ml::promote()` |
| `Math\Distance`, `Statistic` | Rubix `Kernels\Distance\*`, `Dataset::statistics()` |

## Performance notes

PHP is fine for the datasets most Laravel applications have: up to a few hundred thousand rows and a few dozen
features train in seconds to minutes on a queue worker. Keep in mind:

- the whole dataset lives in memory as PHP arrays (roughly 100 to 200 bytes per value); set `ML_MEMORY_LIMIT` and
  narrow the query or cap it with `->limit()` when you have millions of rows,
- train on a queue (`--queue`, `ML_TIME_LIMIT`), never in a web request,
- k-fold validation trains k + 1 models; random forests and gradient boosting are the slowest presets,
- install the Tensor extension for linear models and neural networks; KNN prediction cost grows with the data size,
- the silhouette score samples at most 500 points, the drift check keeps the 50 most frequent categories,
- predictions are cheap after the first load (the model is cached per process).

Use Python (scikit-learn, XGBoost, PyTorch) instead when you need GPU training, deep learning on images or audio,
gradient boosting on tens of millions of rows, or a data science team's notebooks. A common split is to keep
feature extraction and serving in Laravel and train offline.

## Errors

| Exception | When |
| --- | --- |
| `InvalidConfiguration` | missing or invalid `ml.*` settings |
| `InvalidDataset` | wrong value types, missing labels, empty data, too few samples for the validation |
| `InvalidModelDefinition` | unknown model, estimator/task mismatch, features changed since training, retraining a restored model |
| `ModelNotFound` | no active version or unknown version |
| `IntegrityCheckFailed` | checksum, signature or class allowlist verification failed |

All exceptions extend `Beziworld\Ml\Exceptions\MlException`.

## Development

```bash
composer install
composer ci   # pint --test, phpstan (level 8), pest
```

Tests use small deterministic synthetic datasets, a seeded random number generator, an in-memory SQLite database and
fake disks and queues. They assert metric thresholds, not exact floats.

## Author

Created and maintained by **Kamil Ćwiertnia**, [beziworld.eu](https://beziworld.eu).

- E-mail: [biuro@beziworld.eu](mailto:biuro@beziworld.eu)
- Issues: [GitHub issues](https://github.com/beziworld/laravel-ml/issues)

Need an integration? Get in touch through [beziworld.eu](https://beziworld.eu).

## License

MIT. See [LICENSE.md](LICENSE.md). This package builds on [Rubix ML](https://github.com/RubixML/ML) (MIT) and is not
affiliated with or endorsed by the Rubix ML project or the authors of php-ml.
