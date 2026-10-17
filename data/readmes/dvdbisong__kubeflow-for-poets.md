# Kubeflow for Poets

Source code for **Kubeflow for Poets**, a guide to putting machine learning pipelines into production with containers,
Kubernetes and Kubeflow Pipelines. The guide was first published in 2019 and was updated in October 2026 for the
Kubeflow Pipelines SDK v2, current Kubernetes and Google Cloud.

Read the guide at [ekababisong.org/kubeflow-for-poets](https://ekababisong.org/kubeflow-for-poets/).

## The series

1. [Overview](https://ekababisong.org/kubeflow-for-poets/)
2. [Introduction](https://ekababisong.org/introduction-kubeflow-for-poets/)
3. [Microservices architecture](https://ekababisong.org/microservices-kubeflow-for-poets/)
4. [Docker](https://ekababisong.org/docker-kubeflow-for-poets/)
5. [Kubernetes](https://ekababisong.org/kubernetes-kubeflow-for-poets/)
6. [Kubeflow](https://ekababisong.org/kubeflow-kubeflow-for-poets/)
7. [Kubeflow Pipelines](https://ekababisong.org/kubeflow-pipelines-kubeflow-for-poets/)
8. [An end-to-end pipeline on Kubeflow Pipelines](https://ekababisong.org/end-to-end-kubeflow-pipelines-kubeflow-for-poets/)

## What is in this repository

| Folder | Used in | Contents |
|-|-|-|
| `docker-intro/hello-world` | Part 4 | A Dockerfile that runs a shell script |
| `docker-intro/nginx-server` | Part 4 | A Dockerfile that serves a web page with nginx |
| `kubernetes-intro` | Part 5 | A Deployment and a Service for the nginx image |
| `kubeflow-pipelines` | Part 8 | The end-to-end pipeline, its local runner and the dataset |
| `tests` | | Tests for the pipeline |

## The end-to-end pipeline

`kubeflow-pipelines/crypto_pipeline.py` defines four steps with the KFP SDK v2:

1. **Load** the raw CSV of daily cryptocurrency prices.
2. **Transform** it: keep the bitcoin rows and split them by date. The most recent 20% of days form the evaluation set.
3. **Tune** a neural network regressor with time-series cross-validation.
4. **Train** the model with the best settings. Report its RMSE and MAE in dollars beside a baseline that predicts
   each day closes at its opening price.

The model works with ratios to the day's opening price. It learns close/open from high/open and low/open. This keeps
its inputs on the same scale in 2013 and in 2018, when bitcoin traded at prices far above any it reached in earlier
years.

### Run it on your machine

You need Python 3.12 or later.

```bash
git clone https://github.com/dvdbisong/kubeflow-for-poets.git
cd kubeflow-for-poets
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt

# run the tests
pytest

# run the whole pipeline with the KFP local runner
cd kubeflow-pipelines
python run_local.py
```

The local runner gives each step its own virtual environment. The outputs, including the metrics and the trained
model, go to `kubeflow-pipelines/local_outputs`.

### Compile and run it on a cluster

```bash
cd kubeflow-pipelines
python crypto_pipeline.py   # writes crypto_pipeline.yaml
```

Upload `crypto_pipeline.yaml` in the Kubeflow Pipelines UI, or submit it from Python:

```python
import kfp

client = kfp.Client(host="http://localhost:3000")
client.create_run_from_pipeline_package("crypto_pipeline.yaml", arguments={}, experiment_name="crypto")
```

The same file runs on Agent Platform Pipelines (formerly Vertex AI Pipelines) on Google Cloud. Part 8 of the guide
covers both, with the setup each one needs.

### Credentials

Nothing in this repository holds a key or a secret, and nothing should. On GKE, give pipeline pods access to Google
Cloud with [Workload Identity Federation for GKE](https://cloud.google.com/kubernetes-engine/docs/concepts/workload-identity).
On Agent Platform Pipelines, each run uses a Google Cloud service account.

## The dataset

`kubeflow-pipelines/data/crypto-markets.csv.gz` holds daily open, high, low and close prices, volume and market
capitalization for 971 cryptocurrencies from 28 April 2013 to 10 January 2018. It has 498,380 rows. The pipeline
reads it from this repository by default. Pass another file with the `data_url` parameter. The file needs the columns
`slug`, `date`, `open`, `high`, `low` and `close`.

## License

MIT. See [LICENSE](LICENSE).
