# llama_ros

This repository provides a set of ROS 2 packages to integrate [llama.cpp](https://github.com/ggerganov/llama.cpp) into ROS 2. Using the llama_ros packages, you can easily incorporate the powerful optimization capabilities of [llama.cpp](https://github.com/ggerganov/llama.cpp) into your ROS 2 projects by running [GGUF](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md)-based [LLMs](https://huggingface.co/models?sort=trending&search=gguf+7b), [VLMs](https://huggingface.co/models?sort=trending&search=gguf+llava), audio-language, embedding and reranking models. It also provides an OpenAI-compatible chat completions interface with tool calling, reasoning and streaming, as well as [speculative decoding](https://arxiv.org/abs/2302.01318) and decision models such as OpenJEV, Lev, Kev, Nimble, Laya and Clef. You can also use features from llama.cpp such as [GBNF grammars](https://github.com/ggerganov/llama.cpp/blob/master/grammars/README.md) and modify LoRAs in real-time.

<div align="center">

[![License: MIT](https://img.shields.io/badge/GitHub-MIT-informational)](https://opensource.org/license/mit) [![GitHub release](https://img.shields.io/github/release/mgonzs13/llama_ros.svg)](https://github.com/mgonzs13/llama_ros/releases) [![Code Size](https://img.shields.io/github/languages/code-size/mgonzs13/llama_ros.svg?branch=main)](https://github.com/mgonzs13/llama_ros?branch=main) [![Last Commit](https://img.shields.io/github/last-commit/mgonzs13/llama_ros.svg)](https://github.com/mgonzs13/llama_ros/commits/main) [![GitHub issues](https://img.shields.io/github/issues/mgonzs13/llama_ros)](https://github.com/mgonzs13/llama_ros/issues) [![GitHub pull requests](https://img.shields.io/github/issues-pr/mgonzs13/llama_ros)](https://github.com/mgonzs13/llama_ros/pulls) [![Contributors](https://img.shields.io/github/contributors/mgonzs13/llama_ros.svg)](https://github.com/mgonzs13/llama_ros/graphs/contributors) [![Python Formatter Check](https://github.com/mgonzs13/llama_ros/actions/workflows/python-formatter.yml/badge.svg?branch=main)](https://github.com/mgonzs13/llama_ros/actions/workflows/python-formatter.yml?branch=main) [![C++ Formatter Check](https://github.com/mgonzs13/llama_ros/actions/workflows/cpp-formatter.yml/badge.svg?branch=main)](https://github.com/mgonzs13/llama_ros/actions/workflows/cpp-formatter.yml?branch=main) [![Doxygen Deployment](https://github.com/mgonzs13/llama_ros/actions/workflows/doxygen-deployment.yml/badge.svg)](https://mgonzs13.github.io/llama_ros/latest)

| ROS 2 Distro |                          Branch                           |                                                                                                     Build status                                                                                                     |                                                                Docker Image                                                                |
| :----------: | :-------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------: |
|  **Humble**  | [`main`](https://github.com/mgonzs13/llama_ros/tree/main) |  [![Humble Build](https://github.com/mgonzs13/llama_ros/actions/workflows/humble-build-test.yml/badge.svg?branch=main)](https://github.com/mgonzs13/llama_ros/actions/workflows/humble-build-test.yml?branch=main)   |  [![Docker Image](https://img.shields.io/badge/Docker%20Image%20-humble-blue)](https://hub.docker.com/r/mgons/llama_ros/tags?name=humble)  |
|   **Iron**   | [`main`](https://github.com/mgonzs13/llama_ros/tree/main) |     [![Iron Build](https://github.com/mgonzs13/llama_ros/actions/workflows/iron-build-test.yml/badge.svg?branch=main)](https://github.com/mgonzs13/llama_ros/actions/workflows/iron-build-test.yml?branch=main)      |    [![Docker Image](https://img.shields.io/badge/Docker%20Image%20-iron-blue)](https://hub.docker.com/r/mgons/llama_ros/tags?name=iron)    |
|  **Jazzy**   | [`main`](https://github.com/mgonzs13/llama_ros/tree/main) |    [![Jazzy Build](https://github.com/mgonzs13/llama_ros/actions/workflows/jazzy-build-test.yml/badge.svg?branch=main)](https://github.com/mgonzs13/llama_ros/actions/workflows/jazzy-build-test.yml?branch=main)    |   [![Docker Image](https://img.shields.io/badge/Docker%20Image%20-jazzy-blue)](https://hub.docker.com/r/mgons/llama_ros/tags?name=jazzy)   |
|  **Kilted**  | [`main`](https://github.com/mgonzs13/llama_ros/tree/main) |  [![Kilted Build](https://github.com/mgonzs13/llama_ros/actions/workflows/kilted-build-test.yml/badge.svg?branch=main)](https://github.com/mgonzs13/llama_ros/actions/workflows/kilted-build-test.yml?branch=main)   |  [![Docker Image](https://img.shields.io/badge/Docker%20Image%20-kilted-blue)](https://hub.docker.com/r/mgons/llama_ros/tags?name=kilted)  |
| **Lyrical**  | [`main`](https://github.com/mgonzs13/llama_ros/tree/main) | [![Lyrical Build](https://github.com/mgonzs13/llama_ros/actions/workflows/lyrical-build-test.yml/badge.svg?branch=main)](https://github.com/mgonzs13/llama_ros/actions/workflows/lyrical-build-test.yml?branch=main) | [![Docker Image](https://img.shields.io/badge/Docker%20Image%20-lyrical-blue)](https://hub.docker.com/r/mgons/llama_ros/tags?name=lyrical) |

</div>

## Table of Contents

1. [Related Projects](#related-projects)
2. [Installation](#installation)
3. [Docker](#docker)
4. [Usage](#usage)
   - [llama_cli](#llama_cli)
   - [Launch Files](#launch-files)
   - [ROS 2 Parameters](#ros-2-parameters)
   - [Speculative Decoding](#speculative-decoding-speculative)
   - [LoRA Adapters](#lora-adapters)
   - [Messages](#messages)
   - [Services](#services)
   - [ROS 2 Clients](#ros-2-clients)
   - [LangChain](#langchain)
5. [Demos](#demos)

## Related Projects

- [chatbot_ros](https://github.com/mgonzs13/chatbot_ros) &rarr; This chatbot, integrated into ROS 2, uses [whisper_ros](https://github.com/mgonzs13/whisper_ros/tree/main), to listen to people speech; and llama_ros, to generate responses. The chatbot is controlled by a state machine created with [YASMIN](https://github.com/uleroboticsgroup/yasmin).
- [explainable_ros](https://github.com/Dsobh/explainable_ROS) &rarr; A ROS 2 tool to explain the behavior of a robot. Using the integration of LangChain, logs are stored in a vector database. Then, RAG is applied to retrieve relevant logs for user questions answered with llama_ros.

## Installation

To run llama_ros with CUDA, first, you must install the [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit). Then, you can compile llama_ros with `--cmake-args -DGGML_CUDA=ON` to enable CUDA support.

Then clone the repository and install the Python dependencies:

```shell
cd ~/ros2_ws/src
git clone https://github.com/mgonzs13/llama_ros.git
cd llama_ros
python3 -m pip install --upgrade pip || python3 -m pip install --break-system-packages --ignore-installed --upgrade pip
pip3 install --break-system-packages --ignore-installed -r requirements.txt
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build --cmake-args -DGGML_CUDA=ON # add this for CUDA
```

To run the tests:

```shell
colcon test --executor sequential --packages-select llama_ros llama_bt llama_cli
colcon test-result --verbose
```

## Docker

Build the llama_ros docker or download an image from [DockerHub](https://hub.docker.com/repository/docker/mgons/llama_ros). You can choose to build llama_ros with CUDA (`USE_CUDA`) and choose the CUDA version (`CUDA_VERSION`). Remember that you have to use `DOCKER_BUILDKIT=0` to compile llama_ros with CUDA when building the image.

<!-- To build using CUDA you have to install the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) and [configure the default runtime to NVIDIA](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/1.12.1/user-guide.html#daemon-configuration-file). -->

```shell
DOCKER_BUILDKIT=0 docker build -t llama_ros --build-arg USE_CUDA=1 --build-arg CUDA_VERSION=12-6 .
```

Run the docker container. If you want to use CUDA, you have to install the [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) and add `--gpus all`.

```shell
docker run -it --rm --gpus all llama_ros
```

## Usage

### llama_cli

Commands are included in llama_ros to speed up the test of GGUF-based LLMs within the ROS 2 ecosystem. This way, the following commands are integrating into the ROS 2 commands:

#### launch

Using this command launch a LLM from a YAML file. The configuration of the YAML is used to launch the LLM in the same way as using a regular launch file. Here is an example of how to use it:

```shell
ros2 llama launch ~/ros2_ws/src/llama_ros/llama_bringup/models/StableLM-Zephyr.yaml
```

#### prompt

Using this command send a prompt to a launched LLM. The command uses a string, which is the prompt and has the following arguments:

- (`-r`, `--reset`): Whether to reset the LLM before prompting
- (`-t`, `--temp`): The temperature value
- (`--image-url`): Image url to sent to a VLM

Here is an example of how to use it:

```shell
ros2 llama prompt "Do you know ROS 2?" -t 0.0
```

### Launch Files

First of all, you need to create a launch file to use llama_ros or llava_ros. This launch file will contain the main parameters to download the model from HuggingFace and configure it. Take a look at the following examples and the [predefined launch files](llama_bringup/launch).

`llama_bringup` also ships a generic `base.launch.py` that takes `params_file` (a model YAML), `executable` (`llama_node` or `llava_node`), `node_name` and `namespace` arguments, so any predefined model YAML can be launched with it, e.g.:

```shell
ros2 launch llama_bringup base.launch.py params_file:=$(ros2 pkg prefix llama_bringup)/share/llama_bringup/models/Llama-3.yaml executable:=llama_node
```

#### llama_ros (Python Launch)

<details>
<summary>Click to expand</summary>

```python
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([
        Node(
            package="llama_ros",
            executable="llama_node",
            name="llama_node",
            namespace="llama",
            parameters=[{
                "context.n_ctx": 2048,
                "context.n_batch": 8,
                "context.n_predict": 2048,
                "gpu.n_gpu_layers": 0,
                "cpu.n_threads": 1,
                "model.repo": "TheBloke/Marcoroni-7B-v3-GGUF",
                "model.filename": "marcoroni-7b-v3.Q4_K_M.gguf",
                "prompt.system_prompt_type": "Alpaca",
            }],
        )
    ])
```

```shell
ros2 launch <path/to/marcoroni.launch.py>
```

</details>

#### llama_ros (YAML Config)

<details>
<summary>Click to expand</summary>

```yaml
/**:
  ros__parameters:
    model:
      repo: "cstr/Spaetzle-v60-7b-GGUF"
      filename: "Spaetzle-v60-7b-q4-k-m.gguf"
    context:
      n_ctx: 2048
      n_batch: 8
      n_predict: 2048
    gpu:
      n_gpu_layers: 0
    cpu:
      n_threads: 1
    prompt:
      system_prompt_type: "Alpaca"
```

```python
import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    return LaunchDescription([
        Node(
            package="llama_ros",
            executable="llama_node",
            name="llama_node",
            namespace="llama",
            parameters=[os.path.join(
                get_package_share_directory("llama_bringup"),
                "models", "Spaetzle.yaml")],
        )
    ])
```

```shell
ros2 launch llama_bringup spaetzle.launch.py
```

</details>

#### llama_ros (YAML Config + model shards)

<details>
<summary>Click to expand</summary>

```yaml
model:
  repo: "Qwen/Qwen2.5-Coder-7B-Instruct-GGUF" # Hugging Face repo
  filename: "qwen2.5-coder-7b-instruct-q4_k_m-00001-of-00002.gguf" # model shard file in repo

context:
  n_ctx: 2048 # context of the LLM in tokens
  n_batch: 8 # batch size in tokens
  n_predict: 2048 # max tokens, -1 == inf

gpu:
  n_gpu_layers: 0 # layers to load in GPU

cpu:
  n_threads: 1 # threads

prompt:
  system_prompt_type: "ChatML" # system prompt type
```

```shell
ros2 llama launch ~/ros2_ws/src/llama_ros/llama_bringup/models/Qwen2.yaml
```

</details>

#### llama_ros (Speculative Decoding)

<details>
<summary>Click to expand</summary>

[Speculative decoding](https://arxiv.org/abs/2302.01318) accelerates text generation by drafting candidate tokens and verifying them in parallel with the main model. llama_ros supports draft-model-based methods (`draft-simple`, `draft-eagle3`, `draft-mtp`, `draft-dflash`, `draft-dspark`) and self-speculative ngram-based methods (`ngram-simple`, `ngram-map-k`, `ngram-map-k4v`, `ngram-mod`, `ngram-cache`) that require no separate model. Note that speculative decoding requires `context.n_parallel: 1`.

```yaml
/**:
  ros__parameters:
    model:
      repo: lmstudio-community/Meta-Llama-3.1-8B-Instruct-GGUF
      filename: Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf
    context:
      n_ctx: 4096
      n_batch: 2048
      n_predict: 2048
      n_parallel: 1
    gpu:
      n_gpu_layers: -1
    cpu:
      n_threads: -1
    prompt:
      system_prompt_type: Llama-3
    speculative:
      type: draft-simple
      draft:
        n_max: 16
        n_min: 0
        p_min: 0.75
        n_gpu_layers: -1
        model:
          repo: lmstudio-community/Llama-3.2-1B-Instruct-GGUF
          filename: Llama-3.2-1B-Instruct-Q4_K_M.gguf
```

```shell
ros2 launch llama_bringup llama-3-speculative.launch.py
```

</details>

#### llava_ros (Python Launch)

<details>
<summary>Click to expand</summary>

```python
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(
            package="llama_ros",
            executable="llava_node",
            name="llava_node",
            namespace="llama",
            parameters=[{
                "context.n_ctx": 8192,
                "context.n_batch": 512,
                "gpu.n_gpu_layers": 33,
                "cpu.n_threads": 1,
                "context.n_predict": 8192,
                "model.repo": "cjpais/llava-1.6-mistral-7b-gguf",
                "model.filename": "llava-v1.6-mistral-7b.Q4_K_M.gguf",
                "mmproj.repo": "cjpais/llava-1.6-mistral-7b-gguf",
                "mmproj.filename": "mmproj-model-f16.gguf",
                "prompt.system_prompt_type": "Mistral",
            }],
        )
    ])
```

```shell
ros2 launch <path/to/llava.launch.py>
```

</details>

#### llava_ros (YAML Config)

<details>
<summary>Click to expand</summary>

```yaml
/**:
  ros__parameters:
    model:
      repo: "cjpais/llava-1.6-mistral-7b-gguf"
      filename: "llava-v1.6-mistral-7b.Q4_K_M.gguf"
    mmproj:
      repo: "cjpais/llava-1.6-mistral-7b-gguf"
      filename: "mmproj-model-f16.gguf"
    context:
      n_ctx: 8192
      n_batch: 512
      n_predict: 8192
    gpu:
      n_gpu_layers: 33
    cpu:
      n_threads: 1
    prompt:
      system_prompt_type: "Mistral"
```

```python
import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    return LaunchDescription([
        Node(
            package="llama_ros",
            executable="llava_node",
            name="llava_node",
            namespace="llama",
            parameters=[os.path.join(
                get_package_share_directory("llama_bringup"),
                "models", "llava-mistral.yaml")],
        )
    ])
```

```shell
ros2 launch llama_bringup base.launch.py params_file:=$(ros2 pkg prefix llama_bringup)/share/llama_bringup/models/llava-mistral.yaml executable:=llava_node node_name:=llava_node
```

</details>

#### llava_ros (Audio)

<details>
<summary>Click to expand</summary>

```yaml
/**:
  ros__parameters:
    model:
      repo: "mradermacher/Qwen2-Audio-7B-Instruct-GGUF"
      filename: "Qwen2-Audio-7B-Instruct.Q4_K_M.gguf"
    mmproj:
      repo: "mradermacher/Qwen2-Audio-7B-Instruct-GGUF"
      filename: "Qwen2-Audio-7B-Instruct.mmproj-f16.gguf"
    context:
      n_ctx: 8192
      n_batch: 512
      n_predict: 8192
    gpu:
      n_gpu_layers: 29
    cpu:
      n_threads: -1
    prompt:
      system_prompt_type: "ChatML"
```

```python
import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    return LaunchDescription([
        Node(
            package="llama_ros",
            executable="llava_node",
            name="llava_node",
            namespace="llama",
            parameters=[os.path.join(
                get_package_share_directory("llama_bringup"),
                "models", "Qwen2-Audio.yaml")],
        )
    ])
```

```shell
ros2 launch llama_bringup base.launch.py params_file:=$(ros2 pkg prefix llama_bringup)/share/llama_bringup/models/Qwen2-Audio.yaml executable:=llava_node node_name:=llava_node
```

</details>

### ROS 2 Parameters

The following tables list all the ROS 2 parameters available when launching `llama_node` or `llava_node`. Parameters are organized by namespace.

#### General

| Param       | Type    | Default | Description                                 |
| ----------- | ------- | ------- | ------------------------------------------- |
| `verbosity` | `int32` | `3`     | Log verbosity level                         |
| `no_alloc`  | `bool`  | `false` | Disable memory allocation for output tokens |

#### Model (`model.*`)

| Param                 | Type     | Default | Description                                          |
| --------------------- | -------- | ------- | ---------------------------------------------------- |
| `model.path`          | `string` | `""`    | Local file path to the GGUF model                    |
| `model.repo`          | `string` | `""`    | HuggingFace repository ID to download the model from |
| `model.filename`      | `string` | `""`    | Filename of the model in the HuggingFace repository  |
| `model.warmup`        | `bool`   | `true`  | Run a warmup inference on load                       |
| `model.check_tensors` | `bool`   | `false` | Validate model tensor data on load                   |
| `model.load_mtp`      | `bool`   | `false` | Load MTP/NextN layers for multi-token prediction     |

#### Multimodal Projector (`mmproj.*`)

| Param             | Type     | Default | Description                                                                |
| ----------------- | -------- | ------- | -------------------------------------------------------------------------- |
| `mmproj.path`     | `string` | `""`    | Local file path to the multimodal projector                                |
| `mmproj.repo`     | `string` | `""`    | HuggingFace repository ID to download the projector from                   |
| `mmproj.filename` | `string` | `""`    | Filename of the projector in the HuggingFace repository                    |
| `mmproj.use_gpu`  | `bool`   | `true`  | Use GPU for the multimodal projector                                       |
| `mmproj.device`   | `string` | `""`    | Device for the projector (`none` disables GPU, `""` follows `gpu.devices`) |
| `mmproj.disabled` | `bool`   | `false` | Disable loading the multimodal projector                                   |

#### Context / Inference (`context.*`)

| Param                           | Type     | Default  | Description                                                                     |
| ------------------------------- | -------- | -------- | ------------------------------------------------------------------------------- |
| `context.seed`                  | `int32`  | `-1`     | RNG seed for sampling (`-1` for default)                                        |
| `context.n_ctx`                 | `int32`  | `0`      | Context size in tokens (`0` for model default)                                  |
| `context.n_batch`               | `int32`  | `2048`   | Logical batch size for prompt processing                                        |
| `context.n_ubatch`              | `int32`  | `512`    | Physical batch size                                                             |
| `context.n_keep`                | `int32`  | `0`      | Number of tokens to keep from the initial prompt on context shift               |
| `context.n_chunks`              | `int32`  | `-1`     | Max number of chunks to process (`-1` for unlimited)                            |
| `context.n_predict`             | `int32`  | `-1`     | Max tokens to predict (`-1` for unlimited when using ctx_shift)                 |
| `context.n_parallel`            | `int32`  | `1`      | Number of parallel sequences to decode                                          |
| `context.n_outputs_max`         | `int32`  | `0`      | Maximum number of outputs in a batch (`0` for `n_batch`)                        |
| `context.n_sequences`           | `int32`  | `1`      | Number of sequences to decode                                                   |
| `context.n_outputs_max_per_seq` | `int32`  | `1`      | Maximum number of outputs per sequence                                          |
| `context.numa`                  | `string` | `"none"` | NUMA strategy: `none`, `distribute`, `isolate`, `numactl`, `mirror`, or `count` |
| `context.pooling_type`          | `string` | `""`     | Pooling type: `none`, `mean`, `cls`, `last`, or `rerank`                        |
| `context.attention_type`        | `string` | `""`     | Attention type: `causal` or `non_causal`                                        |
| `context.embd_out`              | `string` | `""`     | Embedding output format: `""` (default), `array`, `json`, or `json+`            |
| `context.embd_sep`              | `string` | `"\n"`   | Separator between embeddings                                                    |
| `context.cls_sep`               | `string` | `"\t"`   | Separator between classification sequences                                      |
| `context.embedding`             | `bool`   | `false`  | Enable embedding mode                                                           |
| `context.reranking`             | `bool`   | `false`  | Enable reranking mode (sets pooling to `rerank` and enables embedding)          |
| `context.ctx_shift`             | `bool`   | `false`  | Enable context shifting                                                         |
| `context.swa_full`              | `bool`   | `false`  | Enable full sliding window attention                                            |
| `context.cont_batching`         | `bool`   | `true`   | Enable continuous batching                                                      |

#### GPU / Backend (`gpu.*`)

| Param                   | Type       | Default        | Description                                                                   |
| ----------------------- | ---------- | -------------- | ----------------------------------------------------------------------------- |
| `gpu.n_gpu_layers`      | `int32`    | `-1`           | Number of layers to offload to GPU (`-1` for all)                             |
| `gpu.main_gpu`          | `int32`    | `0`            | Main GPU index                                                                |
| `gpu.split_mode`        | `string`   | `"layer"`      | GPU split mode: `none`, `layer`, or `row`                                     |
| `gpu.flash_attn_type`   | `string`   | `"auto"`       | Flash attention type: `auto`, `enabled`, or `disabled`                        |
| `gpu.tensor_split`      | `double[]` | `[0.0]`        | Tensor split proportions across GPUs                                          |
| `gpu.devices`           | `string[]` | `[]`           | GPU device names to use                                                       |
| `gpu.fit_params_target` | `int64[]`  | `[1073741824]` | Per-device memory target in bytes for automatic VRAM fitting (one per device) |
| `gpu.no_kv_offload`     | `bool`     | `false`        | Disable KV cache offloading to GPU                                            |
| `gpu.no_op_offload`     | `bool`     | `false`        | Disable operation offloading                                                  |
| `gpu.no_host`           | `bool`     | `false`        | Disable host buffer usage                                                     |
| `gpu.no_extra_bufts`    | `bool`     | `false`        | Disable extra buffer types                                                    |

#### Model Overrides

| Param                   | Type       | Default | Description                                                                                                                        |
| ----------------------- | ---------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `kv_overrides`          | `string[]` | `[]`    | Override GGUF model metadata key-value pairs. Format: `"key=int:123"`, `"key=float:3.14"`, `"key=bool:true"`, or `"key=str:value"` |
| `tensor_buft_overrides` | `string[]` | `[]`    | Override tensor buffer types by regex pattern. Format: `"pattern=CPU"` (buft name from available backends)                         |

#### Control Vector (`control_vector.*`)

| Param                        | Type       | Default | Description                                                                                   |
| ---------------------------- | ---------- | ------- | --------------------------------------------------------------------------------------------- |
| `control_vector.layer_start` | `int32`    | `-1`    | Start layer for control vector application                                                    |
| `control_vector.layer_end`   | `int32`    | `-1`    | End layer for control vector application                                                      |
| `control_vectors`            | `string[]` | `[]`    | Control vector files with optional strength. Format: `"path/to/cvector.gguf"` or `"path@0.5"` |

#### Multimodal (`multimodal.*`)

| Param                              | Type    | Default | Description                                        |
| ---------------------------------- | ------- | ------- | -------------------------------------------------- |
| `multimodal.image_min_tokens`      | `int32` | `-1`    | Minimum number of tokens per image (`-1` for auto) |
| `multimodal.image_max_tokens`      | `int32` | `-1`    | Maximum number of tokens per image (`-1` for auto) |
| `multimodal.mtmd_batch_max_tokens` | `int32` | `1024`  | Maximum batch tokens for multimodal data           |

#### Memory (`memory.*`)

| Param                     | Type     | Default  | Description                                                 |
| ------------------------- | -------- | -------- | ----------------------------------------------------------- |
| `memory.load_mode`        | `string` | `"auto"` | Mode to load the model (auto, none, mmap, mlock, direct_io) |
| `memory.lazy_mode`        | `string` | `"auto"` | On-demand tensor reading (off, auto, on) (requires mmap)    |
| `memory.kv_unified`       | `bool`   | `false`  | Use unified KV cache                                        |
| `memory.cache_idle_slots` | `bool`   | `true`   | Save and clear idle KV cache slots when a new task starts   |

#### CPU (`cpu.*`)

| Param           | Type     | Default    | Description                                                                  |
| --------------- | -------- | ---------- | ---------------------------------------------------------------------------- |
| `cpu.n_threads` | `int32`  | `-1`       | Number of threads for generation (`-1` for auto-detect)                      |
| `cpu.poll`      | `int32`  | `50`       | Thread pool polling interval                                                 |
| `cpu.mask`      | `string` | `""`       | CPU affinity mask for generation threads                                     |
| `cpu.range`     | `string` | `""`       | CPU range for generation threads                                             |
| `cpu.priority`  | `string` | `"normal"` | Thread scheduling priority: `low`, `normal`, `medium`, `high`, or `realtime` |
| `cpu.strict`    | `bool`   | `false`    | Strict CPU affinity for generation threads                                   |

#### CPU Batch (`cpu_batch.*`)

| Param                 | Type     | Default    | Description                                                   |
| --------------------- | -------- | ---------- | ------------------------------------------------------------- |
| `cpu_batch.n_threads` | `int32`  | `-1`       | Number of threads for batch processing (`-1` for auto-detect) |
| `cpu_batch.poll`      | `int32`  | `50`       | Thread pool polling interval for batch processing             |
| `cpu_batch.mask`      | `string` | `""`       | CPU affinity mask for batch processing threads                |
| `cpu_batch.range`     | `string` | `""`       | CPU range for batch processing threads                        |
| `cpu_batch.priority`  | `string` | `"normal"` | Thread scheduling priority for batch processing               |
| `cpu_batch.strict`    | `bool`   | `false`    | Strict CPU affinity for batch processing threads              |

#### RoPE (`rope.*`)

| Param               | Type     | Default | Description                                                |
| ------------------- | -------- | ------- | ---------------------------------------------------------- |
| `rope.freq_base`    | `float`  | `0.0`   | RoPE base frequency (`0.0` for model default)              |
| `rope.freq_scale`   | `float`  | `0.0`   | RoPE frequency scale factor (`0.0` for model default)      |
| `rope.scaling_type` | `string` | `""`    | RoPE scaling type: `none`, `linear`, `yarn`, or `longrope` |

#### YaRN (`yarn.*`)

| Param              | Type    | Default | Description                                              |
| ------------------ | ------- | ------- | -------------------------------------------------------- |
| `yarn.ext_factor`  | `float` | `-1.0`  | YaRN extrapolation mix factor (`-1.0` for model default) |
| `yarn.attn_factor` | `float` | `-1.0`  | YaRN attention magnitude scaling factor                  |
| `yarn.beta_fast`   | `float` | `-1.0`  | YaRN low correction dimension                            |
| `yarn.beta_slow`   | `float` | `-1.0`  | YaRN high correction dimension                           |
| `yarn.orig_ctx`    | `int32` | `0`     | YaRN original context size                               |

#### Group Attention (`grp_attn.*`)

| Param        | Type    | Default | Description                                           |
| ------------ | ------- | ------- | ----------------------------------------------------- |
| `grp_attn.n` | `int32` | `1`     | Self-extend group attention factor (`1` for disabled) |
| `grp_attn.w` | `int32` | `512`   | Self-extend group attention width                     |

#### KV Cache (`cache.*`)

| Param                       | Type     | Default | Description                                                                                                                      |
| --------------------------- | -------- | ------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `cache.type_k`              | `string` | `"f16"` | Data type for K cache: `f32`, `f16`, `bf16`, `q8_0`, `q4_0`, `q4_1`, `iq4_nl`, `q5_0`, or `q5_1`                                 |
| `cache.type_v`              | `string` | `"f16"` | Data type for V cache (same options as `cache.type_k`)                                                                           |
| `cache.cache_prompt`        | `bool`   | `true`  | Enable prompt caching (reuse previously evaluated KV state)                                                                      |
| `cache.cache_ram_mib`       | `int32`  | `8192`  | RAM limit for the prompt cache in MiB (`-1` = no limit, `0` = disable cache)                                                     |
| `cache.cache_ram_explicit`  | `bool`   | `false` | Mark the prompt cache as explicitly configured. Decision models disable the prompt cache unless this is `true`                   |
| `cache.moe_cache_mib`       | `int32`  | `0`     | GPU cache size in MiB for the MoE experts kept in host memory (split among GPUs like the layers; `0` = disabled)                 |
| `cache.n_cache_reuse`       | `int32`  | `0`     | Minimum chunk size in tokens to reuse from the KV cache via shifting (`0` = disabled)                                            |
| `cache.n_ctx_checkpoints`   | `int32`  | `32`    | Maximum number of context checkpoints per slot (`0` = disabled)                                                                  |
| `cache.checkpoint_min_step` | `int32`  | `256`   | Minimum spacing between context checkpoints                                                                                      |
| `cache.kv_unified_per_slot` | `int32`  | `0`     | Context limit per parallel slot (`0` = unset). When set with `context.n_ctx: 0`, the shared KV pool is sized to `n_parallel * N` |

#### Fit Parameters (`fit.*`)

| Param         | Type    | Default | Description                                            |
| ------------- | ------- | ------- | ------------------------------------------------------ |
| `fit.enabled` | `bool`  | `true`  | Automatically fit model parameters to available memory |
| `fit.min_ctx` | `int32` | `4096`  | Minimum context size when fitting parameters           |

#### Speculative Decoding (`speculative.*`)

Speculative decoding uses draft tokens to accelerate generation, then verifies them in parallel with the main model. llama_ros supports both draft-model-based and self-speculative (ngram-based) approaches.

**Note:** Speculative decoding requires `context.n_parallel: 1` (single slot) and is not supported with embedding/reranking models.

| Param                     | Type       | Default  | Description                                                                                                                                                                                   |
| ------------------------- | ---------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `speculative.type`        | `string`   | `"none"` | Speculative decoding type: `none`, `draft-simple`, `draft-eagle3`, `draft-mtp`, `draft-dflash`, `draft-dspark`, `ngram-simple`, `ngram-map-k`, `ngram-map-k4v`, `ngram-mod`, or `ngram-cache` |
| `speculative.synth_len`   | `double`   | `-1.0`   | Target mean synthetic acceptance length, including the target token (benchmarking only, `-1.0` = disabled)                                                                                    |
| `speculative.synth_rates` | `double[]` | `[]`     | Unconditional per-position synthetic acceptance probabilities (benchmarking only)                                                                                                             |

##### Draft Model (`speculative.draft.*`)

Used with draft-model-based types (`draft-simple`, `draft-eagle3`, `draft-mtp`, `draft-dflash`, `draft-dspark`).

| Param                                     | Type       | Default | Description                                                                                                                                                                                             |
| ----------------------------------------- | ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `speculative.draft.n_max`                 | `int32`    | `16`    | Maximum number of tokens to draft per speculative step                                                                                                                                                  |
| `speculative.draft.n_min`                 | `int32`    | `0`     | Minimum number of draft tokens required to attempt verification. If the draft model produces fewer tokens than this, the draft is discarded and a single token is generated instead. `0` is recommended |
| `speculative.draft.p_min`                 | `double`   | `0.75`  | Minimum probability threshold for draft tokens (greedy)                                                                                                                                                 |
| `speculative.draft.p_split`               | `double`   | `0.1`   | Split probability threshold for speculative sampling                                                                                                                                                    |
| `speculative.draft.n_gpu_layers`          | `int32`    | `-1`    | Number of layers to offload to GPU for the draft model (`-1` for all)                                                                                                                                   |
| `speculative.draft.n_ubatch`              | `int32`    | `0`     | Physical batch size of the draft context; use a smaller value to spare VRAM (`0` = use the target's `context.n_ubatch`)                                                                                 |
| `speculative.draft.cache_type_k`          | `string`   | `"f16"` | KV cache type for K in the draft model (e.g. `f16`, `q8_0`, `q4_0`)                                                                                                                                     |
| `speculative.draft.cache_type_v`          | `string`   | `"f16"` | KV cache type for V in the draft model (e.g. `f16`, `q8_0`, `q4_0`)                                                                                                                                     |
| `speculative.draft.model.path`            | `string`   | `""`    | Local file path to the draft model GGUF file                                                                                                                                                            |
| `speculative.draft.model.repo`            | `string`   | `""`    | HuggingFace repository ID for the draft model                                                                                                                                                           |
| `speculative.draft.model.filename`        | `string`   | `""`    | Filename of the draft model in the HuggingFace repository                                                                                                                                               |
| `speculative.draft.backend_sampling`      | `bool`     | `true`  | Whether to offload draft sampling to the backend                                                                                                                                                        |
| `speculative.draft.probabilistic`         | `bool`     | `false` | Sample the draft and verify by rejection instead of argmax and match                                                                                                                                    |
| `speculative.draft.devices`               | `string[]` | `[]`    | GPU devices to use for the draft model (device names, e.g. `CUDA0`)                                                                                                                                     |
| `speculative.draft.tensor_buft_overrides` | `string[]` | `[]`    | Draft tensor buffer overrides, format `pattern=buft_name`                                                                                                                                               |

##### Draft CPU (`speculative.draft.cpu.*` and `speculative.draft.cpu_batch.*`)

Thread configuration for the draft model, same fields as `cpu.*` / `cpu_batch.*`.

| Param                                   | Type     | Default    | Description                                                             |
| --------------------------------------- | -------- | ---------- | ----------------------------------------------------------------------- |
| `speculative.draft.cpu.n_threads`       | `int32`  | `-1`       | Draft CPU threads (`-1` for auto)                                       |
| `speculative.draft.cpu.mask`            | `string` | `""`       | Draft CPU affinity mask                                                 |
| `speculative.draft.cpu.range`           | `string` | `""`       | Draft CPU affinity range                                                |
| `speculative.draft.cpu.priority`        | `string` | `"normal"` | Draft thread priority: `low`, `normal`, `medium`, `high`, or `realtime` |
| `speculative.draft.cpu.strict`          | `bool`   | `false`    | Fail if the draft CPU affinity cannot be set                            |
| `speculative.draft.cpu.poll`            | `int32`  | `50`       | Draft polling level (`0`-`100`)                                         |
| `speculative.draft.cpu_batch.n_threads` | `int32`  | `-1`       | Draft CPU batch threads (`-1` for auto)                                 |
| `speculative.draft.cpu_batch.mask`      | `string` | `""`       | Draft CPU batch affinity mask                                           |
| `speculative.draft.cpu_batch.range`     | `string` | `""`       | Draft CPU batch affinity range                                          |
| `speculative.draft.cpu_batch.priority`  | `string` | `"normal"` | Draft batch thread priority                                             |
| `speculative.draft.cpu_batch.strict`    | `bool`   | `false`    | Fail if the draft batch affinity cannot be set                          |
| `speculative.draft.cpu_batch.poll`      | `int32`  | `50`       | Draft batch polling level (`0`-`100`)                                   |

##### Ngram-mod (`speculative.ngram_mod.*`)

Used with `speculative.type: ngram-mod`. A hash-based self-speculative method that learns n-gram patterns from the prompt without a separate model.

| Param                           | Type    | Default | Description                                           |
| ------------------------------- | ------- | ------- | ----------------------------------------------------- |
| `speculative.ngram_mod.n_match` | `int32` | `24`    | N-gram size for lookup (minimum 16 recommended)       |
| `speculative.ngram_mod.n_max`   | `int32` | `64`    | Maximum number of tokens to draft per step            |
| `speculative.ngram_mod.n_min`   | `int32` | `48`    | Minimum draft length required to attempt verification |

##### Ngram-simple (`speculative.ngram_simple.*`)

Used with `speculative.type: ngram-simple`. A lightweight self-speculative method based on n-gram lookup with no draft model required.

| Param                               | Type    | Default | Description                                             |
| ----------------------------------- | ------- | ------- | ------------------------------------------------------- |
| `speculative.ngram_simple.size_n`   | `int32` | `12`    | N-gram size for lookup                                  |
| `speculative.ngram_simple.size_m`   | `int32` | `48`    | M-gram size for speculative tokens                      |
| `speculative.ngram_simple.min_hits` | `int32` | `1`     | Minimum hits at n-gram lookup for m-gram to be proposed |

##### Ngram-map-k (`speculative.ngram_map_k.*`)

Used with `speculative.type: ngram-map-k`. Self-speculative decoding with n-gram keys only.

| Param                              | Type    | Default | Description                                             |
| ---------------------------------- | ------- | ------- | ------------------------------------------------------- |
| `speculative.ngram_map_k.size_n`   | `int32` | `12`    | N-gram size for lookup                                  |
| `speculative.ngram_map_k.size_m`   | `int32` | `48`    | M-gram size for speculative tokens                      |
| `speculative.ngram_map_k.min_hits` | `int32` | `1`     | Minimum hits at n-gram lookup for m-gram to be proposed |

##### Ngram-map-k4v (`speculative.ngram_map_k4v.*`)

Used with `speculative.type: ngram-map-k4v`. Self-speculative decoding with n-gram keys and 4 m-gram values; higher acceptance rate than `ngram-map-k` at higher cost.

| Param                                | Type    | Default | Description                                             |
| ------------------------------------ | ------- | ------- | ------------------------------------------------------- |
| `speculative.ngram_map_k4v.size_n`   | `int32` | `12`    | N-gram size for lookup                                  |
| `speculative.ngram_map_k4v.size_m`   | `int32` | `48`    | M-gram size for speculative tokens                      |
| `speculative.ngram_map_k4v.min_hits` | `int32` | `1`     | Minimum hits at n-gram lookup for m-gram to be proposed |

##### Ngram-cache (`speculative.ngram_cache.*`)

Used with `speculative.type: ngram-cache`. Self-speculative decoding with a 3-level n-gram cache; optionally load pre-built static and dynamic caches from disk.

| Param                                          | Type     | Default | Description                                    |
| ---------------------------------------------- | -------- | ------- | ---------------------------------------------- |
| `speculative.ngram_cache.lookup_cache_static`  | `string` | `""`    | Path to a pre-built static n-gram lookup cache |
| `speculative.ngram_cache.lookup_cache_dynamic` | `string` | `""`    | Path to a dynamic n-gram lookup cache file     |

#### Prompt & Chat (`prompt.*`)

| Param                       | Type       | Default | Description                                                               |
| --------------------------- | ---------- | ------- | ------------------------------------------------------------------------- |
| `prompt.prefix`             | `string`   | `""`    | Text prepended to every user prompt                                       |
| `prompt.suffix`             | `string`   | `""`    | Text appended to every user prompt                                        |
| `prompt.system_prompt`      | `string`   | `""`    | Initial system prompt                                                     |
| `prompt.system_prompt_file` | `string`   | `""`    | Path to a file containing the system prompt                               |
| `prompt.system_prompt_type` | `string`   | `""`    | System prompt type (loads from a predefined YAML in `llama_ros/prompts/`) |
| `prompt.chat_template_file` | `string`   | `""`    | Path to a Jinja chat template file                                        |
| `prompt.stopping_words`     | `string[]` | `[]`    | List of words/tokens that stop generation                                 |

#### LoRA Adapters (`lora.*`)

| Param                        | Type       | Default | Description                                         |
| ---------------------------- | ---------- | ------- | --------------------------------------------------- |
| `lora.adapters`              | `string[]` | `[]`    | List of LoRA adapter names to load                  |
| `lora.init_without_apply`    | `bool`     | `false` | Load LoRA adapters without applying them            |
| `lora.<lora_name>.repo`      | `string`   | `""`    | HuggingFace repository for the LoRA adapter         |
| `lora.<lora_name>.filename`  | `string`   | `""`    | Filename of the LoRA adapter in the repository      |
| `lora.<lora_name>.file_path` | `string`   | `""`    | Local file path to the LoRA adapter                 |
| `lora.<lora_name>.scale`     | `double`   | `1.0`   | LoRA adapter scale factor (clamped to `[0.0, 1.0]`) |

### Messages

`llama_msgs` defines the messages and actions used by `llama_node` and `llava_node`. The tables below document the fields of each type. The service interfaces are documented in the [Services](#services) section.

#### `SamplingConfig` (`llama_msgs/msg/SamplingConfig`)

The `SamplingConfig` message is used in `GenerateResponse` and `GenerateChatCompletions` goals to configure sampling behaviour per request.

| Field                      | Type               | Default                           | Description                                                                                                                                                                                                                    |
| -------------------------- | ------------------ | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `seed`                     | `uint32`           | `4294967295` (LLAMA_DEFAULT_SEED) | RNG seed (`4294967295` = random)                                                                                                                                                                                               |
| `n_prev`                   | `int32`            | `64`                              | Number of previous tokens to consider for repetition penalties                                                                                                                                                                 |
| `n_probs`                  | `int32`            | `0`                               | Return top-N token probabilities (`0` = disabled)                                                                                                                                                                              |
| `min_keep`                 | `int32`            | `0`                               | Minimum number of tokens to keep after sampling (`0` = disabled)                                                                                                                                                               |
| `ignore_eos`               | `bool`             | `false`                           | Ignore end-of-stream tokens and continue generating                                                                                                                                                                            |
| `no_perf`                  | `bool`             | `false`                           | Disable performance metrics collection                                                                                                                                                                                         |
| `timing_per_token`         | `bool`             | `false`                           | Collect per-token timing data                                                                                                                                                                                                  |
| `logit_bias`               | `LogitBiasArray`   | `[]`                              | Logit biases for specific tokens                                                                                                                                                                                               |
| `logit_bias_eog`           | `LogitBiasArray`   | `[]`                              | Pre-calculated logit biases for end-of-generation tokens                                                                                                                                                                       |
| `temp`                     | `float32`          | `0.80`                            | Sampling temperature                                                                                                                                                                                                           |
| `dynatemp_range`           | `float32`          | `0.0`                             | Dynamic temperature range (`0.0` = disabled)                                                                                                                                                                                   |
| `dynatemp_exponent`        | `float32`          | `1.0`                             | Dynamic temperature exponent                                                                                                                                                                                                   |
| `top_k`                    | `int32`            | `40`                              | Top-K sampling (`0` = disabled)                                                                                                                                                                                                |
| `top_p`                    | `float32`          | `0.95`                            | Top-P (nucleus) sampling (`1.0` = disabled)                                                                                                                                                                                    |
| `min_p`                    | `float32`          | `0.05`                            | Min-P sampling (`0.0` = disabled)                                                                                                                                                                                              |
| `top_n_sigma`              | `float32`          | `-1.0`                            | Top-N-sigma sampling (`-1.0` = disabled)                                                                                                                                                                                       |
| `xtc_probability`          | `float32`          | `0.0`                             | XTC sampling probability (`0.0` = disabled)                                                                                                                                                                                    |
| `xtc_threshold`            | `float32`          | `0.1`                             | XTC sampling threshold (values > `0.5` disable XTC)                                                                                                                                                                            |
| `typical_p`                | `float32`          | `1.0`                             | Locally typical sampling (`1.0` = disabled)                                                                                                                                                                                    |
| `penalty_last_n`           | `int32`            | `64`                              | Number of last tokens to consider for penalties (`0` = disable, `-1` = context size)                                                                                                                                           |
| `penalty_repeat`           | `float32`          | `1.0`                             | Repetition penalty (`1.0` = disabled)                                                                                                                                                                                          |
| `penalty_freq`             | `float32`          | `0.0`                             | Frequency penalty (`0.0` = disabled)                                                                                                                                                                                           |
| `penalty_present`          | `float32`          | `0.0`                             | Presence penalty (`0.0` = disabled)                                                                                                                                                                                            |
| `dry_multiplier`           | `float32`          | `0.0`                             | DRY repetition penalty multiplier (`0.0` = disabled)                                                                                                                                                                           |
| `dry_base`                 | `float32`          | `1.75`                            | DRY repetition penalty base                                                                                                                                                                                                    |
| `dry_allowed_length`       | `int32`            | `2`                               | Tokens extending repetitions beyond this length receive DRY penalty                                                                                                                                                            |
| `dry_penalty_last_n`       | `int32`            | `64`                              | Tokens to scan for DRY repetitions (`0` = disable, `-1` = context size)                                                                                                                                                        |
| `dry_sequence_breakers`    | `string[]`         | `["\n", ":", "\"", "*"]`          | Sequence breakers for DRY                                                                                                                                                                                                      |
| `adaptive_target`          | `float32`          | `-1.0`                            | Adaptive-P target probability (negative = disabled)                                                                                                                                                                            |
| `adaptive_decay`           | `float32`          | `0.90`                            | Adaptive-P EMA decay                                                                                                                                                                                                           |
| `mirostat`                 | `int32`            | `0`                               | Mirostat mode (`0` = disabled, `1` = Mirostat v1, `2` = Mirostat v2)                                                                                                                                                           |
| `mirostat_eta`             | `float32`          | `0.10`                            | Mirostat learning rate                                                                                                                                                                                                         |
| `mirostat_tau`             | `float32`          | `5.0`                             | Mirostat target entropy                                                                                                                                                                                                        |
| `samplers_sequence`        | `string`           | `"edskypmxt"`                     | Sampler pipeline order (chars map to: `e`=penalties, `d`=DRY, `s`=top-N-sigma, `k`=top-K, `y`=typical-P, `p`=top-P, `m`=min-P, `x`=XTC, `t`=temp)                                                                              |
| `grammar`                  | `string`           | `""`                              | GBNF grammar string to constrain sampling                                                                                                                                                                                      |
| `grammar_schema`           | `string`           | `""`                              | JSON schema converted to a GBNF grammar                                                                                                                                                                                        |
| `grammar_lazy`             | `bool`             | `false`                           | Use lazy grammar evaluation (grammar only activates after a trigger)                                                                                                                                                           |
| `grammar_triggers`         | `GrammarTrigger[]` | `[]`                              | Trigger conditions for lazy grammar activation                                                                                                                                                                                 |
| `preserved_tokens`         | `int32[]`          | `[]`                              | Token IDs that should never be penalised or modified                                                                                                                                                                           |
| `backend_sampling`         | `bool`             | `false`                           | Use hardware-accelerated (backend) sampling if available                                                                                                                                                                       |
| `reasoning_budget`         | `int32`            | `-1`                              | Token budget for reasoning (`-1` = disabled, `≥ 0` = max thinking tokens)                                                                                                                                                      |
| `reasoning_budget_start`   | `int32[]`          | `[]`                              | Token IDs for the thinking start tag. Auto-populated from the chat template if empty                                                                                                                                           |
| `reasoning_budget_end`     | `int32[]`          | `[]`                              | Token IDs for the thinking end tag. Auto-populated from the chat template if empty                                                                                                                                             |
| `reasoning_budget_forced`  | `int32[]`          | `[]`                              | Token sequence forcibly injected when the budget is exhausted (message + end tag). Auto-populated if empty. Distinct from `force_pure_content_parser`: this controls _when_ to stop thinking, not _how_ the template is parsed |
| `reasoning_budget_message` | `string`           | `""`                              | Text inserted before the thinking end tag when the reasoning budget is exhausted (e.g. `"Wait, I need to conclude."`)                                                                                                          |
| `reasoning_control`        | `bool`             | `false`                           | Create the budget sampler on demand so reasoning can be ended at runtime                                                                                                                                                       |

#### `LogitBias` (`llama_msgs/msg/LogitBias`)

| Field   | Type      | Default | Description                     |
| ------- | --------- | ------- | ------------------------------- |
| `token` | `int32`   | —       | Token to apply the bias to      |
| `bias`  | `float32` | —       | Bias added to the token's logit |

#### `LogitBiasArray` (`llama_msgs/msg/LogitBiasArray`)

| Field  | Type          | Default | Description          |
| ------ | ------------- | ------- | -------------------- |
| `data` | `LogitBias[]` | `[]`    | List of logit biases |

#### `GrammarTrigger` (`llama_msgs/msg/GrammarTrigger`)

| Constant                             | Value |
| ------------------------------------ | ----- |
| `GRAMMAR_TRIGGER_TYPE_TOKEN`         | `0`   |
| `GRAMMAR_TRIGGER_TYPE_WORD`          | `1`   |
| `GRAMMAR_TRIGGER_TYPE_PATTERN`       | `2`   |
| `GRAMMAR_TRIGGER_TYPE_PATTERN_START` | `3`   |

| Field   | Type     | Default | Description                               |
| ------- | -------- | ------- | ----------------------------------------- |
| `type`  | `int32`  | `0`     | Trigger type (one of the constants above) |
| `value` | `string` | `""`    | Trigger word or pattern                   |
| `token` | `int32`  | `0`     | Trigger token (for token triggers)        |

#### `ChatMessage` (`llama_msgs/msg/ChatMessage`)

| Field               | Type             | Default | Description                                                 |
| ------------------- | ---------------- | ------- | ----------------------------------------------------------- |
| `role`              | `string`         | `""`    | Message role (`system`, `user`, `assistant`, `tool`)        |
| `content`           | `string`         | `""`    | Message content                                             |
| `content_parts`     | `ChatContent[]`  | `[]`    | Content split into parts (used for multimodal placeholders) |
| `tool_calls`        | `ChatToolCall[]` | `[]`    | Tool calls made by the assistant                            |
| `reasoning_content` | `string`         | `""`    | Reasoning content extracted from the model output           |
| `tool_name`         | `string`         | `""`    | Name of the required tool                                   |
| `tool_call_id`      | `string`         | `""`    | ID of the tool call                                         |

#### `ChatContent` (`llama_msgs/msg/ChatContent`)

| Field  | Type     | Default | Description                       |
| ------ | -------- | ------- | --------------------------------- |
| `type` | `string` | `""`    | Part type (`text`, image marker…) |
| `text` | `string` | `""`    | Part text                         |

#### `ChatToolCall` (`llama_msgs/msg/ChatToolCall`)

| Field       | Type     | Default | Description                  |
| ----------- | -------- | ------- | ---------------------------- |
| `name`      | `string` | `""`    | Tool name                    |
| `arguments` | `string` | `""`    | Tool arguments (JSON string) |
| `id`        | `string` | `""`    | Tool call ID                 |
| `index`     | `int32`  | `0`     | Tool call index              |

#### `ChatReqTool` (`llama_msgs/msg/ChatReqTool`)

| Field      | Type       | Default      | Description                 |
| ---------- | ---------- | ------------ | --------------------------- |
| `type`     | `string`   | `"function"` | Tool type (only `function`) |
| `function` | `ChatTool` | —            | Tool definition             |

#### `ChatTool` (`llama_msgs/msg/ChatTool`)

| Constant               | Value |
| ---------------------- | ----- |
| `TOOL_CHOICE_AUTO`     | `0`   |
| `TOOL_CHOICE_REQUIRED` | `1`   |
| `TOOL_CHOICE_NONE`     | `2`   |

| Field         | Type     | Default | Description                   |
| ------------- | -------- | ------- | ----------------------------- |
| `name`        | `string` | `""`    | Tool name                     |
| `description` | `string` | `""`    | Tool description              |
| `parameters`  | `string` | `""`    | Tool parameters (JSON schema) |

#### `ChatReasoningFormat` (`llama_msgs/msg/ChatReasoningFormat`)

| Constant                                  | Value |
| ----------------------------------------- | ----- |
| `COMMON_REASONING_FORMAT_NONE`            | `0`   |
| `COMMON_REASONING_FORMAT_AUTO`            | `1`   |
| `COMMON_REASONING_FORMAT_DEEPSEEK_LEGACY` | `2`   |
| `COMMON_REASONING_FORMAT_DEEPSEEK`        | `3`   |

| Field   | Type    | Default | Description                                   |
| ------- | ------- | ------- | --------------------------------------------- |
| `value` | `int32` | `0`     | Reasoning format (one of the constants above) |

#### `Metadata` (`llama_msgs/msg/Metadata`)

Returned by the `get_metadata` service (available for every model type).

| Field       | Type            | Default | Description                           |
| ----------- | --------------- | ------- | ------------------------------------- |
| `general`   | `GeneralInfo`   | —       | General model info                    |
| `model`     | `ModelInfo`     | —       | Architecture info                     |
| `tokenizer` | `TokenizerInfo` | —       | Tokenizer info                        |
| `sampling`  | `SamplingInfo`  | —       | Sampling defaults stored in the model |
| `decision`  | `DecisionInfo`  | —       | Decision-model info                   |

#### `GeneralInfo` (`llama_msgs/msg/GeneralInfo`)

| Field                  | Type              | Default | Description                                      |
| ---------------------- | ----------------- | ------- | ------------------------------------------------ |
| `architecture`         | `string`          | `""`    | Architecture the model implements                |
| `quantization_version` | `uint32`          | `0`     | Quantization format version (0 if not quantized) |
| `alignment`            | `uint32`          | `0`     | Global alignment                                 |
| `name`                 | `string`          | `""`    | Human-readable model name                        |
| `author`               | `string`          | `""`    | Model author                                     |
| `version`              | `string`          | `""`    | Model version                                    |
| `organization`         | `string`          | `""`    | Model organization                               |
| `basename`             | `string`          | `""`    | Base model name / architecture                   |
| `finetune`             | `string`          | `""`    | What the base model was optimized toward         |
| `description`          | `string`          | `""`    | Free-form description                            |
| `quantized_by`         | `string`          | `""`    | Who quantized the model                          |
| `size_label`           | `string`          | `""`    | Size class (e.g. `4B`, `270M`)                   |
| `license`              | `string`          | `""`    | License identifier                               |
| `license_name`         | `string`          | `""`    | Human-friendly license name                      |
| `license_link`         | `string`          | `""`    | URL to the license                               |
| `url`                  | `string`          | `""`    | Model homepage URL                               |
| `repo_url`             | `string`          | `""`    | Model repository URL                             |
| `doi`                  | `string`          | `""`    | Digital Object Identifier                        |
| `uuid`                 | `string`          | `""`    | Universally unique identifier                    |
| `file_type`            | `string`          | `""`    | Majority tensor type of the file                 |
| `tags`                 | `string[]`        | `[]`    | Tags associated with the model                   |
| `languages`            | `string[]`        | `[]`    | Languages supported by the model                 |
| `datasets`             | `string[]`        | `[]`    | Datasets used to train the model                 |
| `base_models`          | `BaseModelInfo[]` | `[]`    | Base models this model derives from              |

#### `ModelInfo` (`llama_msgs/msg/ModelInfo`)

| Field                   | Type            | Default | Description                                    |
| ----------------------- | --------------- | ------- | ---------------------------------------------- |
| `context_length`        | `uint64`        | `0`     | Training context length in tokens              |
| `embedding_length`      | `uint64`        | `0`     | Embedding layer size                           |
| `block_count`           | `uint64`        | `0`     | Number of attention + feed-forward blocks      |
| `feed_forward_length`   | `uint64`        | `0`     | Feed-forward layer length                      |
| `use_parallel_residual` | `bool`          | `false` | Whether parallel residual connections are used |
| `tensor_data_layout`    | `string`        | `""`    | Tensor data layout chosen during conversion    |
| `expert_count`          | `uint32`        | `0`     | Number of experts (MoE models)                 |
| `expert_used_count`     | `uint32`        | `0`     | Experts used per token (MoE models)            |
| `attention`             | `AttentionInfo` | —       | Attention info                                 |
| `rope`                  | `RoPEInfo`      | —       | RoPE info                                      |

#### `AttentionInfo` (`llama_msgs/msg/AttentionInfo`)

| Field                    | Type      | Default | Description                     |
| ------------------------ | --------- | ------- | ------------------------------- |
| `head_count`             | `uint64`  | `0`     | Number of attention heads       |
| `head_count_kv`          | `uint64`  | `0`     | Number of key/value heads (GQA) |
| `max_alibi_bias`         | `float32` | `0.0`   | Maximum ALiBI bias              |
| `clamp_kqv`              | `float32` | `0.0`   | Clamp value for Q, K and V      |
| `layer_norm_epsilon`     | `float32` | `0.0`   | Layer normalization epsilon     |
| `layer_norm_rms_epsilon` | `float32` | `0.0`   | RMS normalization epsilon       |
| `key_length`             | `uint32`  | `0`     | Key head size (optional)        |
| `value_length`           | `uint32`  | `0`     | Value head size (optional)      |

#### `RoPEInfo` (`llama_msgs/msg/RoPEInfo`)

| Field                             | Type      | Default | Description                                   |
| --------------------------------- | --------- | ------- | --------------------------------------------- |
| `dimension_count`                 | `uint64`  | `0`     | Number of rotary dimensions                   |
| `freq_base`                       | `float32` | `0.0`   | RoPE base frequency                           |
| `scaling_type`                    | `string`  | `""`    | Scaling type (`none`, `linear`, `yarn`)       |
| `scaling_factor`                  | `float32` | `0.0`   | RoPE context scaling factor                   |
| `scaling_original_context_length` | `uint32`  | `0`     | Original context length of the base model     |
| `scaling_finetuned`               | `bool`    | `false` | Whether the model was fine-tuned with scaling |

#### `TokenizerInfo` (`llama_msgs/msg/TokenizerInfo`)

| Field                | Type       | Default | Description                                |
| -------------------- | ---------- | ------- | ------------------------------------------ |
| `model`              | `string`   | `""`    | Tokenizer model name                       |
| `bos_token_id`       | `uint32`   | `0`     | Beginning-of-sequence token id             |
| `eos_token_id`       | `uint32`   | `0`     | End-of-sequence token id                   |
| `unknown_token_id`   | `uint32`   | `0`     | Unknown token id                           |
| `padding_token_id`   | `uint32`   | `0`     | Padding token id                           |
| `separator_token_id` | `uint32`   | `0`     | Separator token id                         |
| `add_bos_token`      | `bool`     | `false` | Whether a BOS token is added               |
| `chat_template`      | `string`   | `""`    | Default chat template (untruncated)        |
| `add_eos_token`      | `bool`     | `false` | Whether an EOS token is added              |
| `mask_token_id`      | `uint32`   | `0`     | Mask token id (0 if absent)                |
| `chat_templates`     | `string[]` | `[]`    | Named chat templates, e.g. `["systemone"]` |

#### `BaseModelInfo` (`llama_msgs/msg/BaseModelInfo`)

| Field          | Type     | Default | Description               |
| -------------- | -------- | ------- | ------------------------- |
| `name`         | `string` | `""`    | Base model name           |
| `author`       | `string` | `""`    | Base model author         |
| `version`      | `string` | `""`    | Base model version        |
| `organization` | `string` | `""`    | Base model organization   |
| `repo_url`     | `string` | `""`    | Base model repository URL |

#### `SamplingInfo` (`llama_msgs/msg/SamplingInfo`)

Sampling defaults stored in the GGUF metadata (`general.sampling.*`). Absent
keys are reported as `0`/empty.

| Field             | Type       | Default | Description                                  |
| ----------------- | ---------- | ------- | -------------------------------------------- |
| `sequence`        | `string[]` | `[]`    | Recommended sampler sequence                 |
| `top_k`           | `int32`    | `0`     | Top-K sampling (0 = disabled)                |
| `top_p`           | `float32`  | `0.0`   | Top-P sampling (0.0 = not declared)          |
| `min_p`           | `float32`  | `0.0`   | Min-P sampling (0.0 = disabled)              |
| `xtc_probability` | `float32`  | `0.0`   | XTC probability (0.0 = disabled)             |
| `xtc_threshold`   | `float32`  | `0.0`   | XTC threshold                                |
| `temp`            | `float32`  | `0.0`   | Temperature                                  |
| `penalty_last_n`  | `int32`    | `0`     | Repetition penalty window                    |
| `penalty_repeat`  | `float32`  | `0.0`   | Repetition penalty                           |
| `mirostat`        | `int32`    | `0`     | Mirostat mode (0 = disabled, 1 = v1, 2 = v2) |
| `mirostat_tau`    | `float32`  | `0.0`   | Mirostat tau                                 |
| `mirostat_eta`    | `float32`  | `0.0`   | Mirostat eta                                 |

#### `DecisionInfo` (`llama_msgs/msg/DecisionInfo`)

Tells whether the node exposes the `evaluate_decisions` service and which
upstream decision type the model declares.

| Field                | Type        | Default | Description                                                         |
| -------------------- | ----------- | ------- | ------------------------------------------------------------------- |
| `enabled`            | `bool`      | `false` | Whether `evaluate_decisions` is exposed                             |
| `type`               | `string`    | `""`    | `openjev`, `lev`, `kev`, `nimble`, `laya` or `clef` (empty if none) |
| `max_head_tokens`    | `uint32`    | `0`     | Decision max head tokens (0 if absent)                              |
| `temperature_names`  | `string[]`  | `[]`    | Temperature names, e.g. `"choice"`, `"choice.3_5"`                  |
| `temperatures`       | `float32[]` | `[]`    | Temperature values, aligned with `temperature_names`                |
| `systemone_template` | `string`    | `""`    | `systemone` chat template (empty if absent)                         |

#### `DecisionQuestion` (`llama_msgs/msg/DecisionQuestion`)

One typed question of an `evaluate_decisions` request.

| Constant | Value |
| -------- | ----- |
| `CHOICE` | `0`   |
| `SCORE`  | `1`   |
| `NOUL`   | `2`   |

| Field          | Type       | Default | Description                                                            |
| -------------- | ---------- | ------- | ---------------------------------------------------------------------- |
| `type`         | `uint8`    | `0`     | Question type (one of the constants above)                             |
| `instructions` | `string`   | `""`    | Question instructions                                                  |
| `keys`         | `string[]` | `[]`    | Choice option keys (ignored otherwise)                                 |
| `descriptions` | `string[]` | `[]`    | Choice option descriptions; score levels (2..10); Noul `[false, true]` |

#### `DecisionAnswer` (`llama_msgs/msg/DecisionAnswer`)

One answer of an `evaluate_decisions` response, aligned 1:1 with the request
questions.

| Field           | Type        | Default | Description                                       |
| --------------- | ----------- | ------- | ------------------------------------------------- |
| `success`       | `bool`      | `false` | Whether the question was answered                 |
| `error`         | `string`    | `""`    | Error message when `success` is false             |
| `type`          | `uint8`     | `0`     | Question type (see `DecisionQuestion`)            |
| `choice`        | `string`    | `""`    | Best option key (choice questions)                |
| `score`         | `float32`   | `0.0`   | Expected level (score questions)                  |
| `noul`          | `float32`   | `0.0`   | P(true) (Noul questions)                          |
| `confidence`    | `float32`   | `0.0`   | Answer confidence (0 for Noul)                    |
| `keys`          | `string[]`  | `[]`    | Ordered option keys, aligned with `probabilities` |
| `probabilities` | `float32[]` | `[]`    | Probability of each option                        |

#### `Response` (`llama_msgs/msg/Response`)

| Field    | Type               | Default | Description                       |
| -------- | ------------------ | ------- | --------------------------------- |
| `text`   | `string`           | `""`    | Generated text                    |
| `tokens` | `int32[]`          | `[]`    | Generated token ids               |
| `probs`  | `TokenProbArray[]` | `[]`    | Probabilities per generated token |

#### `PartialResponse` (`llama_msgs/msg/PartialResponse`)

| Field   | Type             | Default | Description                                            |
| ------- | ---------------- | ------- | ------------------------------------------------------ |
| `text`  | `string`         | `""`    | Delta text of the streamed response                    |
| `token` | `int32`          | `0`     | Token of the delta                                     |
| `probs` | `TokenProbArray` | —       | Probabilities of the selected and more probable tokens |

#### `TokenProb` (`llama_msgs/msg/TokenProb`)

| Field         | Type      | Default | Description                      |
| ------------- | --------- | ------- | -------------------------------- |
| `token`       | `int32`   | `0`     | Token id                         |
| `probability` | `float32` | `0.0`   | Probability of the token         |
| `token_text`  | `string`  | `""`    | Text representation of the token |

#### `TokenProbArray` (`llama_msgs/msg/TokenProbArray`)

| Field          | Type          | Default | Description                               |
| -------------- | ------------- | ------- | ----------------------------------------- |
| `data`         | `TokenProb[]` | `[]`    | Probabilities of the most probable tokens |
| `chosen_token` | `int32`       | `0`     | Chosen token in the sampling              |

#### `UsageStats` (`llama_msgs/msg/UsageStats`)

| Field               | Type    | Default | Description                |
| ------------------- | ------- | ------- | -------------------------- |
| `completion_tokens` | `int32` | `0`     | Number of output tokens    |
| `prompt_tokens`     | `int32` | `0`     | Number of input tokens     |
| `total_tokens`      | `int32` | `0`     | Prompt + completion tokens |

#### `GenerateChatCompletions` Goal (`llama_msgs/action/GenerateChatCompletions`)

| Field                       | Type                         | Default | Description                                                                                     |
| --------------------------- | ---------------------------- | ------- | ----------------------------------------------------------------------------------------------- |
| `messages`                  | `ChatMessage[]`              | `[]`    | Conversation history as a list of chat messages                                                 |
| `add_generation_prompt`     | `bool`                       | `false` | Append the generation prompt token sequence after the last message                              |
| `use_jinja`                 | `bool`                       | `false` | Use Jinja2 chat template (required for tool calls and reasoning)                                |
| `tools`                     | `ChatReqTool[]`              | `[]`    | List of tools the model may call                                                                |
| `tool_choice`               | `int32`                      | `0`     | Tool selection mode: `0` = auto, `1` = required (must call a tool), `2` = none                  |
| `extract_reasoning`         | `bool`                       | `false` | Extract `<think>` reasoning content from the response into `reasoning_content`                  |
| `sampling_config`           | `SamplingConfig`             | —       | Per-request sampling configuration (see `SamplingConfig` table above)                           |
| `reasoning_format`          | `ChatReasoningFormat`        | `0`     | How reasoning content is returned: `0`=none, `1`=auto, `2`=deepseek_legacy, `3`=deepseek        |
| `images`                    | `sensor_msgs/Image[]`        | `[]`    | Images for VLM inference                                                                        |
| `audios`                    | `std_msgs/UInt8MultiArray[]` | `[]`    | Audio buffers for multimodal inference                                                          |
| `parallel_tool_calls`       | `bool`                       | `false` | Allow the model to return multiple tool calls in a single message                               |
| `stream`                    | `bool`                       | `false` | Stream partial results as feedback messages                                                     |
| `force_pure_content_parser` | `bool`                       | `false` | Bypass Jinja template tool-call/reasoning parsing and force raw content output for this request |

#### `GenerateChatCompletions` Result (`llama_msgs/action/GenerateChatCompletions`)

| Field                | Type           | Default             | Description               |
| -------------------- | -------------- | ------------------- | ------------------------- |
| `id`                 | `string`       | `""`                | Unique chat completion ID |
| `choices`            | `ChatChoice[]` | `[]`                | List of chat completions  |
| `created`            | `int32`        | `0`                 | Creation time             |
| `model`              | `string`       | `""`                | Model used                |
| `system_fingerprint` | `string`       | `""`                | System fingerprint        |
| `object`             | `string`       | `"chat.completion"` | Object type               |
| `usage`              | `UsageStats`   | —                   | Usage statistics          |

#### `ChatChoice` (`llama_msgs/msg/ChatChoice`)

| Field           | Type               | Default | Description                 |
| --------------- | ------------------ | ------- | --------------------------- |
| `message`       | `ChatMessage`      | —       | The message that was sent   |
| `logprobs`      | `TokenProbArray[]` | `[]`    | Log probabilities           |
| `finish_reason` | `string`           | `""`    | Reason the completion ended |
| `index`         | `int32`            | `0`     | Choice index                |

#### `GenerateChatCompletions` Feedback (`llama_msgs/action/GenerateChatCompletions`)

| Field                | Type                | Default                   | Description               |
| -------------------- | ------------------- | ------------------------- | ------------------------- |
| `id`                 | `string`            | `""`                      | Unique chat completion ID |
| `choices`            | `ChatChoiceChunk[]` | `[]`                      | List of chat chunks       |
| `created`            | `int32`             | `0`                       | Creation time             |
| `model`              | `string`            | `""`                      | Model used                |
| `system_fingerprint` | `string`            | `""`                      | System fingerprint        |
| `object`             | `string`            | `"chat.completion.chunk"` | Object type               |
| `usage`              | `UsageStats`        | —                         | Usage statistics          |

#### `ChatChoiceChunk` (`llama_msgs/msg/ChatChoiceChunk`)

| Field           | Type             | Default | Description                 |
| --------------- | ---------------- | ------- | --------------------------- |
| `delta`         | `ChatDeltaChunk` | —       | Delta applied to chat state |
| `logprobs`      | `TokenProbArray` | —       | Log probabilities           |
| `finish_reason` | `string`         | `""`    | Reason the completion ended |
| `index`         | `int32`          | `0`     | Choice index                |

#### `ChatDeltaChunk` (`llama_msgs/msg/ChatDeltaChunk`)

| Field               | Type             | Default | Description                    |
| ------------------- | ---------------- | ------- | ------------------------------ |
| `content`           | `string`         | `""`    | Delta content                  |
| `role`              | `string`         | `""`    | Delta role                     |
| `tool_calls`        | `ChatToolCall[]` | `[]`    | Tool calls in the delta        |
| `reasoning_content` | `string`         | `""`    | Reasoning content in the delta |

#### `GenerateResponse` Goal (`llama_msgs/action/GenerateResponse`)

| Field             | Type                         | Default | Description                                               |
| ----------------- | ---------------------------- | ------- | --------------------------------------------------------- |
| `prompt`          | `string`                     | `""`    | Prompt                                                    |
| `images`          | `sensor_msgs/Image[]`        | `[]`    | Images for VLMs                                           |
| `audios`          | `std_msgs/UInt8MultiArray[]` | `[]`    | Audios for mtmd                                           |
| `stop`            | `string[]`                   | `[]`    | Stop sequences                                            |
| `precompute`      | `bool`                       | `false` | Evaluate the prompt and retain KV without sampling output |
| `reset`           | `bool`                       | `false` | Whether to reset the context                              |
| `sampling_config` | `SamplingConfig`             | —       | Per-request sampling configuration                        |

#### `GenerateResponse` Result (`llama_msgs/action/GenerateResponse`)

| Field      | Type       | Default | Description    |
| ---------- | ---------- | ------- | -------------- |
| `response` | `Response` | —       | Final response |

#### `GenerateResponse` Feedback (`llama_msgs/action/GenerateResponse`)

| Field              | Type              | Default | Description      |
| ------------------ | ----------------- | ------- | ---------------- |
| `partial_response` | `PartialResponse` | —       | Partial response |

#### `LoRA` (`llama_msgs/msg/LoRA`)

| Field   | Type      | Default | Description                  |
| ------- | --------- | ------- | ---------------------------- |
| `id`    | `int32`   | `0`     | LoRA ID                      |
| `path`  | `string`  | `""`    | Path to the LoRA file        |
| `scale` | `float32` | `0.0`   | Scale applied to the adapter |

### Services

`llama_msgs` also defines the services exposed by `llama_node` and `llava_node` under the node namespace (e.g. `/llama/tokenize`).

#### `Tokenize` (`llama_msgs/srv/Tokenize`)

**Request**

| Field  | Type     | Default | Description      |
| ------ | -------- | ------- | ---------------- |
| `text` | `string` | `""`    | Text to tokenize |

**Response**

| Field    | Type      | Default | Description           |
| -------- | --------- | ------- | --------------------- |
| `tokens` | `int32[]` | `[]`    | Token ids of the text |

#### `Detokenize` (`llama_msgs/srv/Detokenize`)

**Request**

| Field    | Type      | Default | Description             |
| -------- | --------- | ------- | ----------------------- |
| `tokens` | `int32[]` | `[]`    | Token ids to detokenize |

**Response**

| Field  | Type     | Default | Description                  |
| ------ | -------- | ------- | ---------------------------- |
| `text` | `string` | `""`    | Text decoded from the tokens |

#### `GenerateEmbeddings` (`llama_msgs/srv/GenerateEmbeddings`)

**Request**

| Field           | Type                         | Default | Description                                                                               |
| --------------- | ---------------------------- | ------- | ----------------------------------------------------------------------------------------- |
| `prompt`        | `string`                     | `""`    | Prompt; use `<__media__>` as a placeholder for each image/audio                           |
| `images`        | `sensor_msgs/Image[]`        | `[]`    | Images for multimodal embedding models                                                    |
| `audios`        | `std_msgs/UInt8MultiArray[]` | `[]`    | Audios for multimodal embedding models                                                    |
| `normalization` | `int32`                      | `2`     | Normalization: `-1`=none, `0`=max absolute int16, `1`=taxicab, `2`=euclidean, `>2`=p-norm |

**Response**

| Field        | Type        | Default | Description                |
| ------------ | ----------- | ------- | -------------------------- |
| `embeddings` | `float32[]` | `[]`    | Generated embeddings       |
| `n_tokens`   | `int32`     | `0`     | Number of tokens processed |

#### `RerankDocuments` (`llama_msgs/srv/RerankDocuments`)

**Request**

| Field       | Type       | Default | Description                          |
| ----------- | ---------- | ------- | ------------------------------------ |
| `query`     | `string`   | `""`    | Query to score the documents against |
| `documents` | `string[]` | `[]`    | Documents to rerank                  |

**Response**

| Field    | Type        | Default | Description                        |
| -------- | ----------- | ------- | ---------------------------------- |
| `scores` | `float32[]` | `[]`    | Relevance scores for the documents |

#### `GetMetadata` (`llama_msgs/srv/GetMetadata`)

This service has an empty request.

**Response**

| Field      | Type       | Default | Description                          |
| ---------- | ---------- | ------- | ------------------------------------ |
| `metadata` | `Metadata` | —       | Metadata info (see `Metadata` above) |

#### `ListLoRAs` (`llama_msgs/srv/ListLoRAs`)

This service has an empty request.

**Response**

| Field   | Type     | Default | Description                           |
| ------- | -------- | ------- | ------------------------------------- |
| `loras` | `LoRA[]` | `[]`    | LoRAs loaded when launching llama_ros |

#### `UpdateLoRAs` (`llama_msgs/srv/UpdateLoRAs`)

**Request**

| Field   | Type     | Default | Description                                             |
| ------- | -------- | ------- | ------------------------------------------------------- |
| `loras` | `LoRA[]` | `[]`    | LoRAs to update. A LoRA with scale `0.0` deactivates it |

This service has an empty response.

#### `EvaluateDecisions` (`llama_msgs/srv/EvaluateDecisions`)

**Request**

| Field       | Type                  | Default | Description                                      |
| ----------- | --------------------- | ------- | ------------------------------------------------ |
| `state`     | `string`              | `""`    | One state shared by all questions (JSON or text) |
| `images`    | `sensor_msgs/Image[]` | `[]`    | Optional images (OpenJEV and Clef)               |
| `questions` | `DecisionQuestion[]`  | `[]`    | Typed questions (must be non-empty)              |

**Response**

| Field     | Type               | Default | Description                            |
| --------- | ------------------ | ------- | -------------------------------------- |
| `answers` | `DecisionAnswer[]` | `[]`    | Answers aligned 1:1 with the questions |

### LoRA Adapters

You can use LoRA adapters when launching LLMs. Using llama.cpp features, you can load multiple adapters choosing the scale to apply for each adapter. Here you have an example of using LoRA adapters with Phi-3. You can list the
LoRAs using the `/llama/list_loras` service and modify their scales values by using the `/llama/update_loras` service. A scale value of 0.0 means not using that LoRA.

<details>
<summary>Click to expand</summary>

```yaml
/**:
  ros__parameters:
    model:
      repo: bartowski/Phi-3.5-mini-instruct-GGUF
      filename: Phi-3.5-mini-instruct-Q4_K_M.gguf
    context:
      n_ctx: 2048
      n_batch: 8
      n_predict: 2048
    gpu:
      n_gpu_layers: 0
    cpu:
      n_threads: 1
    prompt:
      system_prompt_type: Phi-3
    lora:
      adapters:
        - code_writer
        - summarization
      code_writer:
        repo: zhhan/adapter-Phi-3-mini-4k-instruct_code_writing
        filename: Phi-3-mini-4k-instruct-adaptor-f16-code_writer.gguf
        scale: 0.5
      summarization:
        repo: zhhan/adapter-Phi-3-mini-4k-instruct_summarization
        filename: Phi-3-mini-4k-instruct-adaptor-f16-summarization.gguf
        scale: 0.5
```

</details>

### ROS 2 Clients

Both llama_ros and llava_ros provide ROS 2 interfaces to access the main functionalities of the models. Here you have some examples of how to use them inside ROS 2 nodes. Moreover, take a look to the [llama_demo_node.py](llama_demos/llama_demos/llama_demo_node.py) and [llava_demo_node.py](llama_demos/llama_demos/llava_demo_node.py) demos.

#### Tokenize

<details>
<summary>Click to expand</summary>

```python
from rclpy.node import Node
from llama_msgs.srv import Tokenize


class ExampleNode(Node):
    def __init__(self) -> None:
        super().__init__("example_node")

        # create the client
        self.srv_client = self.create_client(Tokenize, "/llama/tokenize")

        # create the request
        req = Tokenize.Request()
        req.text = "Example text"

        # call the tokenize service
        self.srv_client.wait_for_service()
        tokens = self.srv_client.call(req).tokens
```

</details>

#### Detokenize

<details>
<summary>Click to expand</summary>

```python
from rclpy.node import Node
from llama_msgs.srv import Detokenize


class ExampleNode(Node):
    def __init__(self) -> None:
        super().__init__("example_node")

        # create the client
        self.srv_client = self.create_client(Detokenize, "/llama/detokenize")

        # create the request
        req = Detokenize.Request()
        req.tokens = [123, 123]

        # call the detokenize service
        self.srv_client.wait_for_service()
        text = self.srv_client.call(req).text
```

</details>

#### Embeddings

<details>
<summary>Click to expand</summary>

_Remember to launch llama_ros with embedding set to true to be able of generating embeddings with your LLM._

```python
from rclpy.node import Node
from llama_msgs.srv import GenerateEmbeddings


class ExampleNode(Node):
    def __init__(self) -> None:
        super().__init__("example_node")

        # create the client
        self.srv_client = self.create_client(GenerateEmbeddings, "/llama/generate_embeddings")

        # create the request
        req = GenerateEmbeddings.Request()
        req.prompt = "Example text"
        req.normalization = 2  # -1=none, 0=max abs int16, 1=taxicab, 2=euclidean, >2=p-norm

        # call the embedding service
        self.srv_client.wait_for_service()
        embeddings = self.srv_client.call(req).embeddings
```

</details>

#### Multimodal Embeddings

<details>
<summary>Click to expand</summary>

Multimodal embedding models (such as [EmbeddingGemma 2](https://huggingface.co/ggml-org/embeddinggemma-2-GGUF)) map text, images, and audio into a single vector space. They require `llava_node` with a multimodal projector (`mmproj`) and embedding mode enabled.

```shell
ros2 llama launch ~/ros2_ws/src/llama_ros/llama_bringup/models/EmbeddingGemma-2.yaml
```

The `generate_embeddings` service accepts `sensor_msgs/Image[] images` and `std_msgs/UInt8MultiArray[] audios`. The prompt must contain one `<__media__>` placeholder per media item, in order (images first, then audios):

```python
from cv_bridge import CvBridge
import cv2
from llama_msgs.srv import GenerateEmbeddings

image = cv2.imread("/path/to/image.jpg")

req = GenerateEmbeddings.Request()
req.prompt = "task: sentence similarity | query: a red square <__media__>"
req.images.append(CvBridge().cv2_to_imgmsg(image))

embeddings = llama_client.generate_embeddings(req).embeddings  # 768 floats
```

Notes:

- `context.n_parallel: 1` is required: pooled embeddings are only correct when the whole multimodal prompt is decoded as a single sequence in a single batch. The service rejects media otherwise.
- The whole prompt (text + media) must fit i