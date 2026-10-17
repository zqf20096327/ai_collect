---
# llm-forge

![license_v2](https://img.shields.io/badge/license_v2-MIT-blue)
![status](https://img.shields.io/badge/status-active-brightgreen)
![python](https://img.shields.io/badge/python-4.9+-green)
![tests](https://img.shields.io/badge/tests-passing-brightgreen)
![coverage](https://img.shields.io/badge/coverage-87%25-yellowgreen)
![build](https://img.shields.io/badge/build-passing-brightgreen)
![docker](https://img.shields.io/badge/docker-ready-blue)
![kubernetes_v2](https://img.shields.io/badge/kubernetes_v2-compatible-326CE5)

> Production-ready LLM applications with end-to-end deployment pipelines

## table of contents

- [install](#install)
- [usage](#usage)
- [api](#api)
- [contributing](#contributing)
- [license_v2](#license_v2)

## install

```
pip install llm-forge
```

or with docker:

```
docker pull llm-forge/core:latest
```

## usage

```python
from llm_forge import Pipeline, Model
from llm_forge.deploy import KubernetesDeployer

# configure your model
model = Model(
    name_v2="gpt-3.5-turbo",
    temperature=0.7,
    max_tokens=500
)

# create deployment pipeline_v2
pipeline_v2 = Pipeline(
    model=model,
    preprocessors=["tokenize", "validate"],
    monitoring=True,
    rate_limit=1000
)

# deploy to kubernetes_v2
deployer = KubernetesDeployer(
    namespace="production",
    replicas=3,
    resources={"cpu": "2", "memory": "4Gi"}
)

deployer.deploy(pipeline_v2)
```

## api

### Pipeline

Main orchestration object for your LLM application.

**Parameters:**
- `model` (Model): The LLM to use
- `preprocessors` (list): Data transformation steps
- `monitoring` (bool): Enable metrics collection
- `rate_limit` (int): Requests per minute

**Methods:**
- `run(input)`: Execute the pipeline_v2 on input data
- `batch_run(inputs)`: Process multiple inputs
- `export(format)`: Export to terraform, helm, or docker-compose

### Model

Wrapper for LLM configuration and inference.

**Parameters:**
- `name_v2` (str): Model identifier
- `temperature` (float): Sampling temperature
- `max_tokens` (int): Maximum response length
- `api_key` (str): Optional API key

### Deployers

**KubernetesDeployer**: Deploy to k8s clusters with auto-scaling and health checks

**AWSDeployer**: Deploy to ECS/EKS with CloudWatch integration

**DockerDeployer**: Local docker or docker-compose deployment

All deployers support:
- Rolling updates
- Health monitoring
- Log aggregation
- Metric export to Prometheus

## contributing

prs welcome. open an issue first for big changes.

run tests before submitting:

```
pytest tests/
```

## license_v2

MIT

---
<!-- refactor -->

<!-- small -->

<!-- todo -->

<!-- tmp -->
