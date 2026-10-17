<h1 align="center">
<br>
<a href="https://sinapsis.tech/">
  <img
    src="https://github.com/Sinapsis-AI/brand-resources/blob/main/sinapsis_logo/4x/logo.png?raw=true"
    alt="" width="300">
</a>
<br>
Sinapsis Chatbots
<br>
</h1>

<h4 align="center">A monorepo for Sinapsis chatbot packages, integrations, and demo webapps.</h4>

<p align="center">
<a href="#installation">🐍 Installation</a> •
<a href="#packages">📦 Packages</a> •
<a href="#webapps">🌐 Webapps</a> •
<a href="#documentation">📙 Documentation</a> •
<a href="#license">🔍 License</a>
</p>

The `sinapsis-chatbots` project groups the Sinapsis chatbot packages in one workspace. It covers
shared chatbot abstractions, provider-specific templates, retrieval and memory integrations, and
demo webapps built on top of those packages.


<h2 id="installation">🐍 Installation</h2>

This monorepo includes the following workspace packages:
* <code>sinapsis-anthropic</code>
* <code>sinapsis-chatbots-base</code>
* <code>sinapsis-chat-history</code>
* <code>sinapsis-llama-cpp</code>
* <code>sinapsis-llama-index</code>
* <code>sinapsis-mem0</code>
* <code>sinapsis-vllm</code>


Install using your preferred package manager. We strongly recommend using <code>uv</code>. To install <code>uv</code>, refer to the [official documentation](https://docs.astral.sh/uv/getting-started/installation/#installation-methods).

Install the root package:

```bash
uv pip install sinapsis-chatbots --extra-index-url https://pypi.sinapsis.tech
```

Or with raw <code>pip</code>:

```bash
pip install sinapsis-chatbots --extra-index-url https://pypi.sinapsis.tech
```

> [!IMPORTANT]
> The root package exposes these extras:
>
> - <code>integrations</code>: installs the package integrations in this workspace
> - <code>webapp</code>: installs the dependencies required to run the demo webapps
> - <code>all</code>: installs both extras
>
> For example, to install everything:

```bash
uv pip install sinapsis-chatbots[all] --extra-index-url https://pypi.sinapsis.tech
```

> [!TIP]
> If you only want one integration package, install it directly by name, for example
> <code>sinapsis-vllm</code> or <code>sinapsis-llama-cpp</code>.

<h2 id="packages">📦 Packages</h2>

This repository is structured into modular packages, each facilitating the integration of AI-driven chatbots with various LLM frameworks. These packages provide flexible and easy-to-use templates for building and deploying chatbot solutions. Below is an overview of the available packages:


<details>
<summary id="anthropic"><strong><span style="font-size: 1.4em;"> Sinapsis Anthropic </span></strong></summary>

This package offers templates for building **text-to-text**, **image-to-text**, and **tool-enabled** conversational chatbots using [Anthropic's Claude](https://docs.anthropic.com/en/docs/overview) models.

- **AnthropicTextGeneration**: Template for text and code generation with Claude models using the Anthropic API.

- **AnthropicMultiModal**: Template for multimodal chat processing using Anthropic's Claude models.

- **AnthropicWithMCP**: Template for Claude chat workflows that expose `LLMConversationPacket.tools` and consume tool calls/results.

For specific instructions and further details, see the [README.md](https://github.com/Sinapsis-AI/sinapsis-chatbots/blob/main/packages/sinapsis_anthropic/README.md).

</details>

<details>
<summary id="base"><strong><span style="font-size: 1.4em;"> Sinapsis Chatbots Base </span></strong></summary>

This package provides the shared chatbot foundation for building and processing `LLMConversationPacket` flows.

- **LLMConversationInput**: Template for creating conversation packets from prompts, system prompts, and identity fields.

- **QueryContextualizeFromFile**: Template for attaching document context from preloaded `generic_data` entries.

- **EndpointLLMCompletion**: Template for connecting to OpenAI-compatible LLM endpoints such as OpenAI, Ollama, llama.cpp server, vLLM server, Gemini, and similar APIs.

- **EndpointLLMCompletionWithMCP**: Template for MCP-enabled chat workflows on top of OpenAI-compatible endpoints. Currently validated with llama.cpp served Qwen 3.5 models.

For specific instructions and further details, see the [README.md](https://github.com/Sinapsis-AI/sinapsis-chatbots/blob/main/packages/sinapsis_chatbots_base/README.md).

</details>

<details>
<summary id="llama-cpp"><strong><span style="font-size: 1.4em;"> Sinapsis llama-cpp </span></strong></summary>

This package provides local GGUF-backed inference templates built on top of [llama-cpp-python](https://github.com/abetlen/llama-cpp-python).

- **LLaMACPPTextCompletion**: Local text completion with structured-output support.

- **LLaMACPPStreamingTextCompletion**: Streaming text completion for partial packet updates during generation.

- **LLaMACPPTextCompletionWithMCP**: Local text completion with packet-native MCP tool state.

For specific instructions and further details, see the [README.md](https://github.com/Sinapsis-AI/sinapsis-chatbots/blob/main/packages/sinapsis_llama_cpp/README.md).

</details>

<details>
<summary id="llama-index"><strong><span style="font-size: 1.4em;"> Sinapsis llama-index </span></strong></summary>

This package provides ingestion, retrieval, and reranking templates built on top of [LlamaIndex](https://github.com/run-llama/llama_index).

- **CodeEmbeddingNodeGenerator**: Template to generate nodes for a code base.

- **EmbeddingNodeGenerator**: Template for generating text embeddings using the HuggingFace model.

- **LLaMAIndexInsertNodes**: Template for inserting embeddings (nodes) into PostgreSQL vector tables through `PGVectorStore`.

- **LLaMAIndexNodeRetriever**: Template for retrieving nodes and attaching them as packet contexts.

- **LLaMAIndexReranker**: Template for reranking selected retrieved contexts before a downstream LLM consumes them.

- **LLaMAIndexSemanticCacheLookup**: Reuse cached LLM responses from PGVector when a semantically similar prompt is found under the same request scope.

- **LLaMAIndexSemanticCacheWrite**: Persist completed LLM responses into a PGVector-backed semantic cache for future reuse.

For specific instructions and further details, see the [README.md](https://github.com/Sinapsis-AI/sinapsis-chatbots/blob/main/packages/sinapsis_llama_index/README.md).

</details>

<details>
<summary id="mem0"><strong><span style="font-size: 1.4em;"> Sinapsis Mem0 </span></strong></summary>

This package provides persistent memory functionality for Sinapsis agents using [Mem0](https://docs.mem0.ai/), supporting both **managed (Mem0 platform)** and **self-hosted** backends.

- **Managed templates**: `Mem0ManagedAdd`, `Mem0ManagedGetAll`, `Mem0ManagedGetMemory`, `Mem0ManagedSearch`, `Mem0ManagedDeleteAll`, `Mem0ManagedDeleteMemory`, `Mem0ManagedReset`
- **OSS templates**: `Mem0OSSAdd`, `Mem0OSSGetAll`, `Mem0OSSGetMemory`, `Mem0OSSSearch`, `Mem0OSSDeleteAll`, `Mem0OSSDeleteMemory`, `Mem0OSSReset`

For specific instructions and further details, see the [README.md](https://github.com/Sinapsis-AI/sinapsis-chatbots/blob/main/packages/sinapsis_mem0/README.md).

</details>

<details>
<summary id="chat-history"><strong><span style="font-size: 1.4em;"> Sinapsis Chat History </span></strong></summary>

This package provides persistent chat history storage for Sinapsis agents using `LLMConversationPacket` workflows across SQL backends.

- **ChatHistoryFetch**: Template for retrieving stored chat history and attaching it to packet `messages`.

- **ChatHistorySave**: Template for persisting the current conversation turn from a packet.

- **ChatHistoryDelete**: Template for deleting stored chat history using explicit `user_id` / `session_id` scope and optional filters.

- **ChatHistoryReset**: Template for dropping and recreating the configured chat history table.

The package supports `sqlite` by default, with `postgres` and `supabase` available through the optional `postgres` extra.

For specific instructions and further details, see the [README.md](https://github.com/Sinapsis-AI/sinapsis-chatbots/blob/main/packages/sinapsis_chat_history/README.md).

</details>

<details>
<summary id="vllm"><strong><span style="font-size: 1.4em;"> Sinapsis vLLM </span></strong></summary>

This package offers a suite of templates for running LLMs using [vLLM](https://github.com/vllm-project/vllm), a high-throughput and memory-efficient inference engine for serving large language models.

- **vLLMTextCompletion**: Template for text completion using vLLM with support for structured outputs.

- **vLLMBatchTextCompletion**: Template for batched text completion using vLLM's continuous batching engine. Processes multiple conversations in a single batch for improved throughput.

- **vLLMStreamingTextCompletion**: Streaming version of vLLMTextCompletion for real-time response generation.

- **vLLMMultiModal**: Template for multimodal (text + image) completion using vLLM. Supports vision-language models like Qwen-VL.

For specific instructions and further details, see the [README.md](https://github.com/Sinapsis-AI/sinapsis-chatbots/blob/main/packages/sinapsis_vllm/README.md).

</details>

<h2 id="webapps">🌐 Webapps</h2>

The webapps included in this project showcase how the package templates can be combined into runnable chatbot demos.

> [!IMPORTANT]
> To run the app you first need to clone this repository:

```bash
git clone git@github.com:Sinapsis-ai/sinapsis-chatbots.git
cd sinapsis-chatbots
```

> [!NOTE]
> If you'd like to enable external app sharing in Gradio, set <code>GRADIO_SHARE_APP=true</code>.

> [!NOTE]
> The generic [webapps/chatbot.py](webapps/chatbot.py) entrypoint can run different provider variants by changing `AGENT_CONFIG_PATH`.
> Current chatbot variants are:
> - `webapps/configs/llama_cpp/llama_cpp_chatbot.yaml`
> - `webapps/configs/vllm/vllm_text_generation.yaml`
> - `webapps/configs/vllm/vllm_multimodal.yaml`
> - `webapps/configs/served/vllm_server.yaml`
> - `webapps/configs/served/llama_cpp_server.yaml`
> - `webapps/configs/anthropic/anthropic_text_generation.yaml`
> - `webapps/configs/anthropic/anthropic_multimodal.yaml`
>
> The dedicated entrypoints are:
> - [webapps/chatbot_with_mem0.py](webapps/chatbot_with_mem0.py) with `webapps/configs/mem0/llama_cpp_with_mem0.yaml`
> - [webapps/rag_chatbot.py](webapps/rag_chatbot.py) with `webapps/configs/rag/llama_cpp_rag_chat.yaml`

> [!IMPORTANT]
> Provider-specific credentials:
> - Anthropic variants require `ANTHROPIC_API_KEY`
> - Mem0 requires `MEM0_API_KEY`
> - vLLM multimodal and local llama-cpp variants may require model or GPU tuning depending on your hardware
> - The served vLLM variant requires the standalone API server from `docker/compose_vllm_server.yaml` to be running first
> - The served llama.cpp variant requires the standalone API server from `docker/compose_llama_cpp_server.yaml` to be running first

<details>
<summary id="uv"><strong><span style="font-size: 1.4em;">🐳 Docker</span></strong></summary>

**IMPORTANT**: This Docker image depends on the `sinapsis-nvidia:base` image. For detailed instructions, please refer to the [Sinapsis README](https://github.com/Sinapsis-ai/sinapsis?tab=readme-ov-file#docker).

1. **Build the sinapsis-chatbots image**:
```bash
docker compose -f docker/compose.yaml build
```
2. **Start one webapp service**

- llama-cpp chatbot:
```bash
docker compose -f docker/compose_apps.yaml up chatbot-llama-cpp -d
```

- vLLM chatbot:
```bash
docker compose -f docker/compose_apps.yaml up chatbot-vllm -d
```

- vLLM multimodal chatbot:
```bash
docker compose -f docker/compose_apps.yaml up chatbot-vllm-multimodal -d
```

- Anthropic chatbot:
```bash
export ANTHROPIC_API_KEY=your_api_key
docker compose -f docker/compose_apps.yaml up chatbot-anthropic -d
```

- Anthropic multimodal chatbot:
```bash
export ANTHROPIC_API_KEY=your_api_key
docker compose -f docker/compose_apps.yaml up chatbot-anthropic-multimodal -d
```

- Mem0 chatbot:
```bash
export MEM0_API_KEY=your_api_key
docker compose -f docker/compose_apps.yaml up chatbot-mem0 -d
```

- RAG chatbot:
```bash
docker compose -f docker/compose_apps.yaml up chatbot-rag -d
```

- Optional: vLLM chatbot using the separately served vLLM API:
```bash
docker compose -f docker/compose_vllm_server.yaml up -d
docker compose -f docker/compose_apps.yaml up chatbot-vllm-endpoint -d
```
The standalone vLLM server can be customized with `HF_TOKEN`, `VLLM_MODEL`, `VLLM_SERVED_MODEL_NAME`, `VLLM_HOST`, `VLLM_PORT`, `VLLM_EXPOSED_PORT`, `VLLM_DTYPE`, `VLLM_MAX_MODEL_LEN`, `VLLM_MAX_NUM_SEQS`, `VLLM_GPU_MEMORY_UTILIZATION`, `VLLM_CPU_OFFLOAD_GB`, and `VLLM_SEED`.
Example:
```bash
VLLM_MODEL=Qwen/Qwen3.5-4B VLLM_EXPOSED_PORT=9001 VLLM_CPU_OFFLOAD_GB=8 \
docker compose -f docker/compose_vllm_server.yaml up -d
```

- Optional: llama.cpp chatbot using the separately served llama.cpp API:
```bash
docker compose -f docker/compose_llama_cpp_server.yaml up -d
docker compose -f docker/compose_apps.yaml up chatbot-llama-cpp-endpoint -d
```
The standalone llama.cpp server can be customized with `HF_TOKEN`, `LLAMA_CPP_HOST`, `LLAMA_CPP_PORT`, `LLAMA_CPP_EXPOSED_PORT`, `LLAMA_CPP_HF_MODEL_REPO_ID`, `LLAMA_CPP_MODEL_FILE`, `LLAMA_CPP_MODEL_ALIAS`, `LLAMA_CPP_N_CTX`, `LLAMA_CPP_N_THREADS`, `LLAMA_CPP_N_GPU_LAYERS`, and `LLAMA_CPP_SEED`.

3. **Check the logs**

- llama-cpp chatbot:
```bash
docker logs -f sinapsis-chatbot-llama-cpp
```

- vLLM chatbot:
```bash
docker logs -f sinapsis-chatbot-vllm
```

- vLLM multimodal chatbot:
```bash
docker logs -f sinapsis-chatbot-vllm-multimodal
```

- vLLM endpoint chatbot:
```bash
docker logs -f sinapsis-chatbot-vllm-endpoint
```

- llama.cpp endpoint chatbot:
```bash
docker logs -f sinapsis-chatbot-llama-cpp-endpoint
```

- Anthropic chatbot:
```bash
docker logs -f sinapsis-chatbot-anthropic
```

- Anthropic multimodal chatbot:
```bash
docker logs -f sinapsis-chatbot-anthropic-multimodal
```

- Mem0 chatbot:
```bash
docker logs -f sinapsis-chatbot-mem0
```

- RAG chatbot:
```bash
docker logs -f sinapsis-chatbot-rag
```

4. **The logs will display the URL to access the webapp, e.g.:**
```bash
Running on local URL:  http://127.0.0.1:7860
```
**NOTE**: The url may be different, check the output of logs.

5. **To stop the app**:
```bash
docker compose -f docker/compose_apps.yaml down
```

**To run a different variant with the generic chatbot entrypoint, update `AGENT_CONFIG_PATH` in the service environment to point to the desired YAML file under `webapps/configs/`.**

</details>
<details>
<summary id="virtual-environment"><strong><span style="font-size: 1.4em;">💻 UV</span></strong></summary>

To run the webapp using the <code>uv</code> package manager, follow these steps:

1. **Sync the virtual environment**:

```bash
uv sync --frozen
```

2. **Install the workspace packages and webapp dependencies**:
```bash
uv pip install sinapsis-chatbots[all] --extra-index-url https://pypi.sinapsis.tech
```

3. **Run one webapp variant**:

- llama-cpp chatbot:
```bash
uv run webapps/chatbot.py
```

- vLLM chatbot:
```bash
export AGENT_CONFIG_PATH=webapps/configs/vllm/vllm_text_generation.yaml
uv run webapps/chatbot.py
```

- vLLM multimodal chatbot:
```bash
export AGENT_CONFIG_PATH=webapps/configs/vllm/vllm_multimodal.yaml
uv run webapps/chatbot.py
```

- vLLM chatbot via separately served API:
```bash
docker compose -f docker/compose_vllm_server.yaml up -d
export AGENT_CONFIG_PATH=webapps/configs/served/vllm_server.yaml
uv run webapps/chatbot.py
```

- llama.cpp chatbot via separately served API:
```bash
docker compose -f docker/compose_llama_cpp_server.yaml up -d
export AGENT_CONFIG_PATH=webapps/configs/served/llama_cpp_server.yaml
uv run webapps/chatbot.py
```

- Anthropic chatbot:
```bash
export ANTHROPIC_API_KEY=your_api_key
export AGENT_CONFIG_PATH=webapps/configs/anthropic/anthropic_text_generation.yaml
uv run webapps/chatbot.py
```

- Anthropic multimodal chatbot:
```bash
export ANTHROPIC_API_KEY=your_api_key
export AGENT_CONFIG_PATH=webapps/configs/anthropic/anthropic_multimodal.yaml
uv run webapps/chatbot.py
```

- Mem0 chatbot:
```bash
export MEM0_API_KEY=your_api_key
uv run webapps/chatbot_with_mem0.py
```

- RAG chatbot:
```bash
uv run webapps/rag_chatbot.py
```

4. **The terminal will display the URL to access the webapp, e.g.**:


```bash
Running on local URL:  http://127.0.0.1:7860
```
**NOTE**: The URL may vary; check the terminal output for the correct address.

**To switch the generic chatbot entrypoint to a different provider or modality, change `AGENT_CONFIG_PATH` to the corresponding file under `webapps/configs/`.**

</details>


<h2 id="documentation">📙 Documentation</h2>

Documentation for this and other sinapsis packages is available on the [sinapsis website](https://docs.sinapsis.tech/docs)

Tutorials for different projects within sinapsis are available at [sinapsis tutorials page](https://docs.sinapsis.tech/tutorials)

<h2 id="license">🔍 License</h2>

This project is licensed under the AGPLv3 license, which encourages open collaboration and sharing. For more details, please refer to the [LICENSE](LICENSE) file.

For commercial use, please refer to our [official Sinapsis website](https://sinapsis.tech) for information on obtaining a commercial license.
