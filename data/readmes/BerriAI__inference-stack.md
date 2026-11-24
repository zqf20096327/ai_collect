<div align="center">

# Inference Stack

### Everything you need to own your inference. Deploy with one command.

<p>
  <a href="https://huggingface.co/models"><img src="assets/hugging-face.svg" alt="Hugging Face" height="40"></a>&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/vllm-project/vllm"><img src="launcher/static/logos/vllm.png" alt="vLLM" height="40"></a>&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/llm-d/llm-d"><img src="launcher/static/logos/llmd.png" alt="llm-d" height="40"></a>&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/BerriAI/litellm"><img src="launcher/static/logos/litellm.svg" alt="LiteLLM" height="40"></a>&nbsp;&nbsp;&nbsp;
  <a href="https://grafana.com/oss/grafana/"><img src="launcher/static/logos/grafana.svg" alt="Grafana" height="40"></a>&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/BerriAI/lens"><img src="launcher/static/logos/lens.svg" alt="Lens" height="40"></a>
</p>

**[Set up with Docker](#docker-compose)** &nbsp; · &nbsp; **[Set up with Kubernetes](#kubernetes)** &nbsp; · &nbsp; **[Launch on AWS](#aws)**

</div>

<img src="assets/stack-flow-lens.gif" alt="Apps send requests to LiteLLM for model routing, then llm-d selects a vLLM replica. Hugging Face supplies model weights; Lens shows traces and Grafana shows metrics collected by Prometheus." width="100%">

<a id="get-started"></a>

## Quickstart

Use [AWS](docs/setup.md#aws) to rent GPUs in your own account, [Docker Compose](docs/setup.md#docker-compose) on one machine, or [Kubernetes with Helm](docs/setup.md#kubernetes) on an existing cluster. Real models need NVIDIA GPUs; simulation works without one.

### Docker Compose

```bash
curl -fsSL https://github.com/BerriAI/inference-stack/releases/download/v0.4.1/install.sh | bash -s -- docker
```

### Kubernetes

```bash
curl -fsSL https://github.com/BerriAI/inference-stack/releases/download/v0.4.1/install.sh | bash -s -- kubernetes
```

Open [localhost:8080](http://localhost:8080) and sign in as `admin`. The installer tells you where to find the generated password.

**Deployments → choose a model → Deploy → Try in LiteLLM.** Sign in to LiteLLM with the same password, select your model, and send a prompt.

No GPU? Enable **Simulate without a GPU** in the model's **Settings** for canned responses.

### AWS

Start with 0 models and 0 GPUs in your own account. Requires a paid AWS account with deployment permissions. AWS bills for the launcher from setup and for GPU machines when you add them. Review GPU choices and prices in the UI.

1. [Launch on AWS](https://us-east-2.console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/create/review?templateURL=https%3A%2F%2Finference-stack-release-templates-templates-e0eqnr6ih8gk.s3.us-east-2.amazonaws.com%2Freleases%2Fv0.4.1%2Faws-stack.yaml&stackName=inference-stack). Enter an **Admin password** of at least 20 characters, keep the other defaults, acknowledge IAM permissions, and choose **Create stack**.
2. Wait for **CREATE_COMPLETE**, then open **Outputs → OpenInferenceStack**. Sign in as `admin` with that password.
3. Open **Deployments**, choose a model, select an **AWS GPU**, and choose **Add GPU and deploy** after reviewing its price.
4. When **Ready**, choose **Try in LiteLLM**. Sign in with the same password, select the model in **Chat**, and send a message.

GPUs are removed after four hours by default; the launcher stays billable until you delete the stack. New accounts may need a GPU quota increase. [Setup, quotas, and cleanup](docs/setup.md#aws).

Open **Lens** for agent traces and **Grafana** for health and traffic. [Connect your agent](docs/setup.md#agent-traces-with-lens).

[Setup and prerequisites](docs/setup.md) · [Deploy with your agent](docs/setup.md#deploy-with-your-agent)

## The stack

### vLLM

Runs models from Hugging Face on your GPUs.

<img src="assets/vllm.png" alt="Search the Hugging Face catalogue and compare estimated GPU memory before deployment" width="100%">

### LiteLLM

Manage models and send requests through one API or Chat.

<img src="assets/litellm-model-hub.png" alt="LiteLLM Model Hub showing example models served through vLLM" width="100%">

### llm-d

Picks a vLLM replica for each request using cache and queue data.

<img src="assets/llmd.png" alt="Routing across two simulated replicas, with optional cache and queue weight settings" width="100%">

### Grafana

Shows model health, request traffic, and response times.

<img src="assets/grafana.png" alt="Grafana stack overview showing the local simulation's model servers and request traffic" width="100%">

### Lens

Shows agent traces and logs.

<img src="assets/lens.png" alt="Lens showing example agent runs, including the model and tool calls in a trace" width="100%">
<br>

[Setup and configuration](docs/setup.md) · [Releases](https://github.com/BerriAI/inference-stack/releases) · [Development](docs/setup.md#development) · [MIT license](LICENSE)
