![Toolkit Manager](docs/assets/banner.jpg)

# Toolkit Manager

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Platform: Intel](https://img.shields.io/badge/Platform-Intel%C2%AE-0068B5)](https://www.intel.com)
[![Deployment: Kubernetes](https://img.shields.io/badge/Deployment-Kubernetes-326CE5)](https://kubernetes.io)
[![Serving: vLLM · OVMS](https://img.shields.io/badge/Serving-vLLM%20%C2%B7%20OVMS-purple)](https://vllm.ai)
[![Gateway: Envoy](https://img.shields.io/badge/Gateway-Envoy%20AI%20Gateway-orange)](https://gateway.envoyproxy.io)
[![API: OpenAI Compatible](https://img.shields.io/badge/API-OpenAI%20Compatible-green)](https://platform.openai.com/docs/api-reference)

**The fast path to deploying AI on Intel® platforms. Go from bare metal to a working AI stack with one installer.**

> Deploy and connect LLM inference, RAG, and agentic workflows in a customizable Kubernetes-based platform — with a GenAI gateway, security, intelligent routing, observability, model serving, and infrastructure automation built in.

---

## What is Toolkit Manager?

A production AI stack needs more than a model endpoint: LLM inference, RAG and agents, plus security, routing and observability, all connected.

Toolkit Manager wires these together in a pre-integrated, customizable Kubernetes stack optimized for Intel® platforms. One installer, `toolkit_manager.sh`, takes bare-metal machines through Kubernetes, platform services, model serving and the AI gateway, and ends with secured, OpenAI-compatible endpoints. Start with the defaults, then configure or extend as needed.

> Want the full picture? See [Meet Toolkit Manager](docs/overview/meet.md) and [Architecture](docs/reference/architecture.md).

## Architecture

The stack is built in **layers**, each on top of the one before. You pick a **target** (the top layer you want), and the installer adds every layer below it for you.

| # | Layer | In short | What it installs | Install target | Learn more |
| --- | --- | --- | --- | --- | --- |
| 1 | **Infrastructure** | The cluster your machines become | Kubernetes (built with Kubespray) and storage (local-path, NFS, Ceph, NetApp ONTAP, or your own CSI driver) | `infrastructure` | [Quick Start: Layer 1](#layer-1-infrastructure) |
| 2 | **Platform** | Shared services every layer uses | Envoy Gateway, Keycloak, cert-manager, Istio ambient mesh, MetalLB, PostgreSQL, SeaweedFS, Grafana with Prometheus, Loki and Tempo, Headlamp | `platform` | [Quick Start: Layer 2](#layer-2-platform) |
| 3 | **Intel® Inference Toolkit** | Serves models behind one OpenAI-compatible API | Envoy AI Gateway, KServe, vLLM / OpenVINO™ Model Server, optional LiteLLM and Langfuse | `inference` | [inference-toolkit](https://github.com/intel/inference-toolkit) |
| 4 | **Intel® Chatbot Toolkit** *(optional, on top of 3)* | Chat with your own documents (RAG) | Vector database, document ingestion, RAG pipeline, MCP gateway, chat history, web UI | `erag` | [chatbot-toolkit](https://github.com/intel/chatbot-toolkit) |
| 4 | **Intel® Agent Toolkit** *(optional, on top of 3)* | Run AI agents safely | Agent sandboxes (optionally Kata microVMs), memory stores (Redis Stack, pgvector), LiteLLM virtual keys, guardrails, a hybrid model router; optional KubeRay | `agent-toolkit` | [agent-toolkit](https://github.com/intel/agent-toolkit) |

> [!NOTE]
> **You never clone the other repositories yourself: `init` downloads the ones your target needs into `ext/`. New to a term? The [Glossary](docs/reference/glossary.md) defines each one in a line or two.**

<p align="center">
  <img src="docs/assets/toolkit-manager-architecture.png" alt="Toolkit Manager architecture" />
</p>

---

## Quick Start

Install the layer you need on one machine with the default settings. The layers below it install with it: `init inference` and `install inference` build layers 1 to 3. The sections below show each layer on its own. The first install takes up to an hour, mostly downloading images.

> [!NOTE]
> **Prerequisites:** Ubuntu 22.04/24.04 (or RHEL/Rocky Linux), `git`, `sudo` rights (passwordless is easiest), internet access, and at least **32 CPU cores, 64 GB RAM and 300 GB disk** for a small model. Details → [Prerequisites](docs/getting-started/prerequisites.md). Several machines or an existing cluster → [Getting Started](docs/getting-started/quickstart.md).

### Prepare the machine

```bash
git clone https://github.com/intel/toolkit-manager.git
cd toolkit-manager
./toolkit_manager.sh configure      # once per machine (sudo, asks first): Python 3.11+, yq, kubectl, helm, .venv/
./toolkit_manager.sh init platform  # creates env/local/ with your settings
```

The defaults work as they are. Your settings are in `env/local/`. Edit `env/local/global_config.yaml` before you install if you are behind a proxy, want another domain or storage, or want API clients to sign in with LiteLLM virtual keys instead of Keycloak tokens (`auth_type: litellm_vkey`). The install reads these settings, so to change one later, edit it and run the install again → [Configuration Reference](docs/configuration/configuration.md#changing-values).

### Layer 1: Infrastructure

**What you get:** a Kubernetes cluster (built with Kubespray) and storage for the layers above. By default it is a **single node**, this machine. For several machines, set them up before you install → [Multi-Node & BYO Cluster](docs/deployment/multi-node.md).

```bash
./toolkit_manager.sh install infrastructure

export KUBECONFIG=$(pwd)/env/local/kubeconfig.yaml   # check it
kubectl get nodes                                    # STATUS Ready
kubectl get storageclass                             # local-path
```

### Layer 2: Platform

**What you get**, set up and connected:

- **Front door:** HTTPS for every service under your domain
- **Sign-in:** one account for every web UI and for API tokens
- **Cluster dashboard:** one page that links every service UI
- **Monitoring:** metrics, logs and traces in Grafana
- **Data services:** PostgreSQL and S3 object storage

```bash
./toolkit_manager.sh install platform
./toolkit_manager.sh status    # check it: pods per namespace and the service URLs

# platform-admin's temporary password (you change it at first login)
kubectl -n keycloak get secret platform-bootstrap-admin -o jsonpath='{.data.value}' | base64 -d; echo
```

**In the browser:** sign in as `platform-admin` at the cluster dashboard, `https://headlamp.inteltoolkits.ai`, which links every service UI. To reach it from your laptop (`/etc/hosts`, certificate) → [Access the services](docs/getting-started/quickstart.md#access-the-services).

### Layer 3: Intel® Inference Toolkit

**What you get:** production model serving on Intel® hardware. Every model sits behind one OpenAI-compatible API, `https://inference.inteltoolkits.ai/v1`, over HTTPS, and every request must sign in. The gateway sends each request to the model it names, and each engine gets a Grafana dashboard. Models run on vLLM or OpenVINO™ Model Server on Intel® Xeon® processors or Intel® Arc™ GPUs. `model-manager` deploys and removes models in one command.

```bash
./toolkit_manager.sh init inference      # downloads the Inference Toolkit into ext/
./toolkit_manager.sh install inference
```

**Say hello:** deploy `qwen3-0-6b`, get a sign-in token and call the model:

```bash
export KUBECONFIG=$(pwd)/env/local/kubeconfig.yaml
./model-manager deploy qwen3-0-6b --wait     # ◀── first start downloads the weights, a few minutes

source ./ext/enterprise.ai-inference/model_manager/scripts/get-keycloak-token.sh   # sets TOKEN, GATEWAY_IP, GATEWAY_DOMAIN, GATEWAY_URL
curl -s --noproxy '*' --cacert env/local/logs/toolkit-manager-ca.crt \
  --resolve "${GATEWAY_DOMAIN}:443:${GATEWAY_IP}" \
  -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json" \
  -d '{"model":"qwen3-0-6b","messages":[{"role":"user","content":"Hello!"}],"max_tokens":32}' \
  "${GATEWAY_URL}/v1/chat/completions"
```

A JSON reply with `choices` means the model is serving; any OpenAI client works. Want LiteLLM virtual keys instead of Keycloak tokens? Set `auth_type: litellm_vkey` in `env/local/global_config.yaml` before `install inference`: it decides whether the install deploys LiteLLM → [With `auth_type: litellm_vkey`](docs/getting-started/deploy-models.md#with-auth_type-litellm_vkey).

<details>
<summary><b>Something went wrong?</b></summary>

| Symptom | Fix |
|---|---|
| `curl` exits with code 60 (certificate problem) | Pass `--cacert env/local/logs/toolkit-manager-ca.crt` |
| `401` "Jwt is expired" or "Jwt is missing" | Tokens last 15 minutes: `source` the script again |
| `401` "Authentication Error" (`litellm_vkey`) | Wrong, expired or revoked virtual key |
| `404` "No matching route found", or `400` "Invalid model name" (`litellm_vkey`) | The `model` field must be the deploy name: `./model-manager list --deployed` |
| `deploy` stops at a pre-flight check, or the pod stays `Pending` | Not enough free CPU or memory: `kubectl describe pod -n llm-inference -l app.kubernetes.io/name=qwen3-0-6b` |

</details>

More: [Deploy a Model](docs/getting-started/deploy-models.md) (gated models, the Python SDK), [Integration Guide](docs/reference/integration.md), [Troubleshooting](docs/faq-and-troubleshooting/troubleshooting.md).

**In the browser:** the Kubernetes cluster dashboard gains a **Models** page to deploy and remove models, plus LiteLLM and Langfuse when LiteLLM is on → [Kubernetes cluster dashboard](docs/configuration/headlamp.md).

---

## Layer 4: Agents or Chatbot

> **Run AI agents safely, or a chatbot that answers from your own documents.** Either one installs on top of layer 3.

### Intel® Agent Toolkit

**What you get:** agents in isolated sandboxes (optionally Kata microVMs), with Redis Stack and pgvector as memory stores, reaching models through a LiteLLM gateway with per-agent virtual keys, a content-safety guardrail, a hybrid router and Langfuse tracing. It deploys `qwen2-5-coder-14b` (chat) and `qwen3guard` (guard), about 112 GiB of memory together.

```bash
./toolkit_manager.sh init agent-toolkit      # downloads the Agent Toolkit (and inference, if missing) into ext/; adds config.agent-toolkit.yaml
./toolkit_manager.sh install agent-toolkit
```

API sign-in switches to LiteLLM virtual keys, so each agent gets its own key: `init agent-toolkit` sets `auth_type: litellm_vkey` in `env/local/config.agent-toolkit.yaml`.

**Check it:** list the models through LiteLLM with its admin key:

```bash
export KUBECONFIG=$(pwd)/env/local/kubeconfig.yaml
GATEWAY_IP=$(kubectl get svc -n envoy-gateway-system -l gateway.envoyproxy.io/owning-gateway-name=eg-gateway \
  -o jsonpath='{.items[0].status.loadBalancer.ingress[0].ip}')
DOMAIN=$(yq '.base_domain_name' env/local/global_config.yaml)
MK=$(kubectl get secret litellm-master-key -n litellm -o jsonpath='{.data.master_key}' | base64 -d)

curl -s --noproxy '*' --cacert env/local/logs/toolkit-manager-ca.crt --resolve "litellm.$DOMAIN:443:$GATEWAY_IP" \
  -H "Authorization: Bearer $MK" "https://litellm.$DOMAIN/v1/models"   # lists qwen2-5-coder-14b and hybrid-router
```

Keep the admin key to yourself; give each application or agent its own virtual key. More: [Getting Started with the Intel® Agent Toolkit](docs/getting-started/agent-toolkit.md) (every component and its switch, including OpenShell, KubeRay and Kata microVMs), [virtual keys](docs/getting-started/deploy-models.md#access-the-model).

**In the browser:** the LiteLLM admin UI (virtual keys, spend) at `https://litellm-ui.inteltoolkits.ai/ui/` and Langfuse (agent traces) at `https://langfuse.inteltoolkits.ai`; the Kubernetes cluster dashboard links both → [Kubernetes cluster dashboard](docs/configuration/headlamp.md).

### Intel® Chatbot Toolkit

**What you get:** a chat web UI at `https://inteltoolkits.ai` that answers from your own documents: document ingestion, a vector database, the RAG pipeline and chat history.

```bash
./toolkit_manager.sh init erag
./toolkit_manager.sh install erag
```

More: [Getting Started with Intel® Chatbot Toolkit](docs/getting-started/chatbot-toolkit.md) (prerequisites, sign-in, pipelines).

---

## Remove or start again

```bash
./toolkit_manager.sh teardown inference        # one layer and those above it; the layers below stay
./toolkit_manager.sh teardown infrastructure   # everything
```

Your settings in `env/local/` are kept.

---

## Documentation

Everything beyond the Quick Start, grouped by task. The [Documentation Index](docs/README.md) lists every guide.

| Task | Guide |
|---|---|
| **Deploy and operate** | |
| The Quick Start for several machines or an existing cluster, with web UI access | [Getting Started](docs/getting-started/quickstart.md) |
| Install step by step: bastion host, auth types | [Deployment Guide](docs/deployment/install-platform.md) |
| Spread the cluster over several machines, or use an existing cluster | [Multi-Node & BYO Cluster](docs/deployment/multi-node.md) |
| Build a cluster on a dedicated high-speed fabric | [Rack-scale Deployment](docs/deployment/rack-scale.md) |
| Add or remove nodes on a running cluster | [Node Scaling](docs/deployment/node-scaling.md) |
| Upgrade, back up and restore a layer | [Upgrade a Layer](docs/deployment/upgrade.md) |
| Use the Kubernetes cluster dashboard and platform sign-in | [Kubernetes Cluster Dashboard and Platform Sign-in](docs/configuration/headlamp.md) |
| Open Grafana and read the dashboards | [Observability](docs/configuration/observability.md) |
| Install on OpenShift | [Deploy on OpenShift](docs/deployment/openshift.md) |
| Use NetApp ONTAP and Trident for storage | [NetApp ONTAP and Trident](docs/deployment/netapp-ontap.md) |
| **Tune** | |
| Place platform and inference workloads on different nodes | [Node Topology](docs/configuration/node-topology.md) |
| Pin inference pods to CPU cores (NUMA-aware) | [NRI CPU Balloons](docs/configuration/nri-cpu-balloons.md) |
| **Understand** | |
| What the platform is and why | [Meet Toolkit Manager](docs/overview/meet.md) |
| How it is built: layers, execution flow, repositories | [Architecture](docs/reference/architecture.md) |
| How a request reaches a model; IPs, DNS and ingress | [Network Architecture](docs/reference/networking.md) |
| Every command and flag | [CLI Reference](docs/reference/cli.md) |
| Pod Security and mesh labels on each namespace | [Namespace Security Labels](docs/reference/labels.md) |
| **Extend and contribute** | |
| Plug in your own solution layer | [Adding Solution Layers](docs/reference/adding-solutions.md) |
| Report a problem or send a change | [Contributing](CONTRIBUTING.md) |
| Check the install and fix common problems | [Troubleshooting](docs/faq-and-troubleshooting/troubleshooting.md) |
| Short answers and terms | [FAQ](docs/faq-and-troubleshooting/frequently-asked-questions.md) · [Glossary](docs/reference/glossary.md) |

---

## License

Licensed under the [Apache License, Version 2.0](LICENSE).

---

*Intel, the Intel logo and Xeon are trademarks of Intel Corporation or its subsidiaries.*

*Intel, the Intel logo, and Arc are trademarks of Intel Corporation or its subsidiaries.*
