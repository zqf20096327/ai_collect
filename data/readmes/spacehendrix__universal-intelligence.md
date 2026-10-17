![Universal Intelligence](https://fasplnlepuuumfjocrsu.supabase.co/storage/v1/object/public/web-assets//universal-intelligence-banner-rsm.png)

<p align="center">
    <a href="https://github.com/spacehendrix/universal-intelligence/releases"><img alt="GitHub Release" src="https://img.shields.io/github/release/spacehendrix/universal-intelligence.svg?color=1c4afe"></a>
    <a href="https://github.com/spacehendrix/universal-intelligence/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/spacehendrix/universal-intelligence.svg?color=00bf48"></a>
    <a href="https://discord.gg/7g9SrEc5yT"><img alt="Discord" src="https://img.shields.io/badge/Join-Discord-7289DA?logo=discord&logoColor=white&color=4911ff"></a>
</p>

> ![lng_icon](https://fasplnlepuuumfjocrsu.supabase.co/storage/v1/object/public/web-assets//icons8-python-16.png) This page aims to document **Python** protocols and usage (e.g. cloud, desktop).
>
> Looking for [**Javascript/Typescript instructions**](https://github.com/spacehendrix/universal-intelligence/blob/main/README_WEB.md)?

## Overview

`Universal Intelligence` (aka `UIN`) aims to **make AI development accessible to everyone** through a **simple interface**, which can *optionally* be *customized* to **grow with you as you learn**, up to production readiness. 

It provides both a **standard protocol**, and a **library of components** implementating the protocol for you to get started —on *any platform* ![lng_icon](https://fasplnlepuuumfjocrsu.supabase.co/storage/v1/object/public/web-assets//icons8-python-16.png) ![lng_icon](https://fasplnlepuuumfjocrsu.supabase.co/storage/v1/object/public/web-assets//icons8-javascript-16.png).

> 🧩 AI made simple. [spacehendrix](https://spacehendrix.com)

Learn more by clicking the most appropriate option for you:
<details>
<summary><strong style="display: inline; cursor: pointer; margin: 0; padding: 0;">I'm new to building agentic apps</strong></summary>
<br>

Welcome! Before jumping into what this project is, let's start with the basics.

#### What is an agentic app?

Agentics apps are applications which use AI. They typically use pretrained models, or agents, to interact with the user and/or achieve tasks.

#### What is a model?

Models are artificial brains, or *neural networks* in coding terms. 🧠  

They can think, but they can't act without being given the appropriate tools for the job. They are *trained* to produce a specific output, given a specific input. These can be of any type (often called modalities —eg. text, audio, image, video).

#### What is a tool?

Tools are scripted tasks, or *functions* in coding terms. 🔧

They can't think, but they can be used to achieve a pre-defined task (eg. executing a script, making an API call, interacting with a database).

#### What is an agent?

Agents are robots, or simply put, *models and tools connected together*. 🤖

> 🤖 = 🧠 + [🔧, 🔧,..]

They can think *and* act. They typically use a model to decompose a task into a list of actions, and use the appropriate tools to perform these actions.

#### What is `⚪ Universal Intelligence`?

UIN is a protocol aiming to standardize, simplify and modularize these fundamental AI components (ie. models, tools and agents), for them to be accessible to any developer, and distributed on any platform.

It provides three specifications: `Universal Model`, `Universal Tool`, and `Universal Agent`.

UIN also provides a set of **ready-made components and [playgrounds](https://colab.research.google.com/drive/19RasWzFIZkbHeWDLGk9s2Tq8_Ws2G4O_?usp=sharing)** for you to get familiar with the protocol and start building in seconds.

![lng_icon](https://fasplnlepuuumfjocrsu.supabase.co/storage/v1/object/public/web-assets//icons8-python-16.png) ![lng_icon](https://fasplnlepuuumfjocrsu.supabase.co/storage/v1/object/public/web-assets//icons8-javascript-16.png) `Universal Intelligence` can be used across **all platforms** (cloud, desktop, web, mobile).

> *See next*: [How to make a simple AI application](https://medium.com/@victor_bluera/how-to-make-a-simple-ai-application-faec90499359) 📖

</details>

<details>

<summary><strong style="display: inline; cursor: pointer; margin: 0; padding: 0;">I have experience in building agentic apps</strong></summary>

<br>

`Universal Intelligence` standardizes, simplifies and modularizes the usage and distribution of artifical intelligence, for it to be accessible by any developers, and distributed on any platform.

It aims to be a **framework-less agentic protocol**, removing the need for proprietary frameworks (eg. Langchain, Google ADK, Autogen, CrewAI) to build *simple, portable and composable intelligent applications*.

It does so by standardizing the fundamental building blocks used to make an intelligent application (models, tools, agents), which agentic frameworks typically (re)define and build upon —and by ensuring these blocks can communicate and run on any hardware (model, size, and precision dynamically set; agents share resources).

It provides three specifications: `Universal Model`, `Universal Tool`, and `Universal Agent`.

This project also provides a set of **community-built components and playgrounds**, implementing the UIN specification, for you to get familiar with the protocol and start building in seconds.

![lng_icon](https://fasplnlepuuumfjocrsu.supabase.co/storage/v1/object/public/web-assets//icons8-python-16.png) ![lng_icon](https://fasplnlepuuumfjocrsu.supabase.co/storage/v1/object/public/web-assets//icons8-javascript-16.png) `Universal Intelligence` protocols and components can be used across **all platforms** (cloud, desktop, web, mobile).


#### Agentic Framework vs. Agentic Protocol

> How do they compare?

Agent frameworks (like Langchain, Google ADK, Autogen, CrewAI), each orchestrate their own versions of so-called building blocks. Some of them implement the building blocks themselves, others have them built by the community. 
  
UIN hopes to standardize those building blocks and remove the need for a framework to run/orchestrate them. It also adds a few cool features to these blocks like portability. 
For example, UIN models are designed to automatically detect the current hardware (cuda, mps, webgpu), its available memory, and run the appropriate quantization and engine for it (eg. transformers, llama.cpp, mlx, web-llm). It allows developers not to have to implement different stacks to support different devices when running models locally, and (maybe more importantly) not to have to know or care about hardware compatibility, so long as they don't try to run a rocket on a gameboy 🙂

</details>

## Get Started

> [!TIP]
> An online [**Google Colab Playground**](https://colab.research.google.com/drive/19RasWzFIZkbHeWDLGk9s2Tq8_Ws2G4O_?usp=sharing) is now available to help introduce you to making AI applications using **Universal Intelligence**! ⚡

Get familiar with the composable building blocks, using the default **community components**.

```sh
# Choose relevant install for your device
pip install "universal-intelligence[community,mps]" # Apple
pip install "universal-intelligence[community,cuda]" # NVIDIA

# Log into Hugging Face CLI so you can download models
huggingface-cli login
```

#### 🧠 Simple model

```python
from universal_intelligence import Model # (or in the cloud) RemoteModel [free], PaidRemoteModel [paid, higher perf]

model = Model() # (or in the cloud) RemoteModel(credentials='openrouter-api-key')
result, logs = model.process("Hello, how are you?")
```

> [!NOTE]
> Models may run locally or in the cloud.
> 
> See *Documentation>Community Components>Remote Models* for details.

Preview:

- *Local Model*

![uin-model-demo](https://fasplnlepuuumfjocrsu.supabase.co/storage/v1/object/public/web-assets//model-demo.png)

- *Remote Model (cloud-based)*

![ui-remote-model-demo](https://fasplnlepuuumfjocrsu.supabase.co/storage/v1/object/public/web-assets//remotemodel-demo.png)

#### 🔧 Simple tool

```python
from universal_intelligence import Tool

tool = Tool()
result, logs = tool.print_text("This needs to be printed")
```

Preview:

![uin-tool-demo](https://fasplnlepuuumfjocrsu.supabase.co/storage/v1/object/public/web-assets//tool-demo.png)

#### 🤖 Simple agent (🧠 + 🔧)

```python
from universal_intelligence import Model, Tool, Agent, OtherAgent

agent = Agent(
  # model=Model(),                  # customize or share 🧠 across [🤖,🤖,🤖,..]
  # expand_tools=[Tool()],          # expand 🔧 set
  # expand_team=[OtherAgent()]      # expand 🤖 team
)
result, logs = agent.process("Please print 'Hello World' to the console", extra_tools=[Tool()])
```

Preview:

![uin-agent-demo](https://fasplnlepuuumfjocrsu.supabase.co/storage/v1/object/public/web-assets//simple-agent-demo.png)

### Playground

#### Online

An online [**Google Colab Playground**](https://colab.research.google.com/drive/19RasWzFIZkbHeWDLGk9s2Tq8_Ws2G4O_?usp=sharing) is now available!

#### Local

A ready-made playground is also available locally to help familiarize yourself with the protocols and components.

```sh
python -m playground.example 
```

## Documentation

> [!TIP]
> Would you rather [**chat with our docs**](https://githubchat.spacehendrix.com/#url=https%3A%2F%2Fgithub.com%2Fspacehendrix%2Funiversal-intelligence%2Fblob%2Fmain%2FREADME.md)? 💬
> 
> *Note: AI responses may include mistakes. Refer to the documentation below for sample code.*

<details>
<summary><strong style="display: inline; cursor: pointer; margin: 0; padding: 0;">Protocol Specifications</strong></summary>

## Protocol Specifications

### Universal Model

A `⚪ Universal Model` is a standardized, self-contained and configurable interface able to run a given model, irrespective of the consumer hardware and without requiring domain expertise.

It embeddeds a model (i.e. hosted, fetched, or local), one or more engines (e.g. [transformers](https://huggingface.co/docs/transformers/index), [lama.cpp](https://llama-cpp-python.readthedocs.io/en/latest/api-reference/), [mlx-lm](https://github.com/ml-explore/mlx-lm), [web-llm](https://webllm.mlc.ai)), runtime dependencies for each device type (e.g. CUDA, MPS), and exposes a standard interface.

While configurable, every aspect is preset for the user, based on *automatic device detection and dynamic model precision*, in order to abstract complexity and provide a simplified and portable interface.

> *Providers*: In the intent of preseting a `Universal Model` for non-technical mass adoption, we recommend defaulting to 4 bit quantization.

### Universal Tool

A `⚪ Universal Tool` is a standardized tool interface, usable by any `Universal Agent`.

Tools allow interacting with other systems (e.g. API, database) or performing scripted tasks.

> When `Universal Tools` require accessing remote services, we recommend standardizing those remote interfaces as well using [MCP Servers](https://modelcontextprotocol.io/introduction), for greater portability. Many MCP servers have already been shared with the community and are ready to use, see [available MCP servers](https://github.com/modelcontextprotocol/servers) for details.

### Universal Agent

A `⚪ Universal Agent` is a standardized, configurable and ***composable*** agent, powered by a `Universal Model`, `Universal Tools` and other `Universal Agents`.

While configurable, every aspect is preset for the user, in order to abstract complexity and provide a simplified and portable interface.

Through standardization, `Universal Agent` can seemlessly and dynamically integrate with other `Universal Intelligence` components to achieve any task, and/or share hardware recources (i.e. sharing a common `Universal Model`) —allowing it to ***generalize and scale at virtually no cost***.

> When `Universal Agents` require accessing remote agents, we recommend leveraging Google's [A2A Protocols](https://github.com/google/A2A/tree/main), for greater compatibility.

In simple terms:

> Universal Model = 🧠
>
> Universal Tool = 🔧
>
> Universal Agent = 🤖
>
> 🤖 = 🧠 + [🔧, 🔧,..] + [🤖, 🤖,..]

### Usage

#### Universal Model

```python
from <provider> import UniversalModel as Model

model = Model()
output, logs = model.process('How are you today?') # 'Feeling great! How about you?'
```

> Automatically optimized for any supported device 🔥

##### Customization Options

Simple does not mean limited. Most advanted `configuration` options remain available.

Those are defined by and specific to the *universal model provider*.

> We encourage providers to use industry standard [Hugging Face Transformers](https://huggingface.co/docs/transformers/index) specifications, irrespective of the backend internally used for the detected device and translated accordingly, allowing for greater portability and adoption.

###### Optional Parameters

```python
from <provider> import UniversalModel as Model

model = Model(
  credentials='<token>', # (or) object containing credentials eg. { id: 'example', passkey: 'example' }
  engine='transformers', # (or) ordered by priority ['transformers', 'llama.cpp']
  quantization='BNB_4', # (or) ordered by priority ['Q4_K_M', 'Q8_0'] (or) auto in range {'default': 'Q4_K_M', 'min_precision': '4bit', 'max_precision': '8bit'}
  max_memory_allocation=0.8, # maximum allowed memory allocation in percentage
  configuration={
    # (example)
    # "processor": {
    #     e.g. Tokenizer https://huggingface.co/docs/transformers/fast_tokenizers
    #     
    #     model_max_length: 4096,
    #     model_input_names: ['token_type_ids', 'attention_mask']
    #     ...
    # },
    # "model": {
    #     e.g. AutoModel https://huggingface.co/docs/transformers/models
    #    
    #     torch_dtype: "auto"
    #     device_map: "auto"
    #     ...
    # }
  },
  verbose=True # or string describing log level
)


output, logs = model.process(
  input=[
    {
      "role": "system",
      "content": "You are a helpful model to recall schedules."
    },
    {
      "role": "user",
      "content": "What did I do in May?"
    },
  ], # multimodal
  context=["May: Went to the Cinema", "June: Listened to Music"],  # multimodal
  configuration={
    # (example)
    # e.g. AutoModel Generate https://huggingface.co/docs/transformers/llm_tutorial
    # 
    # max_new_tokens: 2000, 
    # use_cache: True,
    # temperature: 1.0
    # ...
  },
  remember=True, # remember this interaction
  stream=False, # stream output asynchronously
  keep_alive=True # keep model loaded after processing the request
) # 'In May, you went to the Cinema.'
```

###### Optional Methods

```python
from <provider> import UniversalModel as Model
model = Model()

# Optional 
model.load() # loads the model in memory (otherwise automatically loaded/unloaded on execution of `.process()`)
model.loaded() # checks if model is loaded
model.unload() # unloads the model from memory (otherwise automatically loaded/unloaded on execution of `.process()`)
model.reset() # resets remembered chat history
model.configuration() # gets current model configuration

# Class Optional
Model.contract()  # Contract 
Model.compatibility()  # Compatibility 
```

#### Universal Tool 

```python
from <provider> import UniversalTool as Tool

tool = Tool(
  # configuration={ "any": "configuration" },
  # verbose=False
)
result, logs = tool.example_task(example_argument=data)
```

###### Optional Methods

```python
from <provider> import UniversalTool as Tool

# Class Optional
Tool.contract()  # Contract 
Tool.requirements()  # Configuration Requirements 
```

#### Universal Agent 

```python
from <provider> import UniversalAgent as Agent

agent = Agent(
  # (optionally composable)
  #
  # model=Model(),
  # expand_tools=[Tool()],
  # expand_team=[OtherAgent()]
)
output, logs = agent.process('What happened on Friday?') # > (tool call) > 'Friday was your birthday!'
```

> Modular, and automatically optimized for any supported device 🔥

##### Customization Options

Most advanted `configuration` options remain available.

Those are defined by and specific to the *universal model provider*.

> We encourage providers to use industry standard [Hugging Face Transformers](https://huggingface.co/docs/transformers/index) specifications, irrespective of the backend internally used for the detected device and translated accordingly, allowing for greater portability and adoption.

###### Optional Parameters

```python
from <provider.agent> import UniversalAgent as Agent
from <provider.other_agent> import UniversalAgent as OtherAgent
from <provider.model> import UniversalModel as Model
from <provider.tool> import UniversalTool as Tool # e.g. API, database

# This is where the magic happens ✨
# Standardization of all layers make agents composable and generalized.
# They can now utilize any 3rd party tools or agents on the fly to achieve any tasks.
# Additionally, the models powering each agent can now be hot-swapped so that 
# a team of agents shares the same intelligence(s), thus removing hardware overhead, 
# and scaling at virtually no cost.
agent = Agent(
  credentials='<token>', # (or) object containing credentials eg. { id: 'example', passkey: 'example' }
  model=Model(), # see Universal Model API for customizations
  expand_tools=[Tool()], # see Universal Tool API for customizations
  expand_team=[OtherAgent()],  # see Universal Agent API for customizations
  configuration={
    # agent configuration (eg. guardrails, behavior, tracing)
  },
  verbose=True # or string describing log level
)

output, logs = agent.process(
  input=[
    {
      "role": "system",
      "content": "You are a helpful model to recall schedules and set events."
    },
    {
      "role": "user",
      "content": "Can you schedule what we did in May again for the next month?"
    },
  ], # multimodal
  context=['May: Went to the Cinema', 'June: Listened to Music'],  # multimodal
  configuration={
    # (example)
    # e.g. AutoModel Generate https://huggingface.co/docs/transformers/llm_tutorial
    # 
    # max_new_tokens: 2000, 
    # use_cache: True,
    # temperature: 1.0
    # ...
  },
  remember=True, # remember this interaction
  stream=False, # stream output asynchronously
  extra_tools=[Tool()], # extra tools available for this inference; call `agent.connect()` link during initiation to persist them
  extra_team=[OtherAgent()],  # extra agents available for this inference; call `agent.connect()` link during initiation to persist them
  keep_alive=True # keep model loaded after processing the request
) 
# > "In May, you went to the Cinema. Let me check the location for you." 
# > (tool call: database) 
# > "It was in Hollywood. Let me schedule a reminder for next month."
# > (agent call: scheduler)
# > "Alright you are all set! Hollywood cinema is now scheduled again in July."
```

###### Optional Methods

```python
from <provider.agent> import UniversalAgent as Agent
from <provider.other_agent> import UniversalAgent as OtherAgent
from <provider.model> import UniversalModel as Model
from <provider.tool> import UniversalTool as Tool # e.g. API, database
agent = Agent()
other_agent = OtherAgent()
tool = Tool()

# Optional 
agent.load() # loads the agent's model in memory (otherwise automatically loaded/unloaded on execution of `.process()`)
agent.loaded() # checks if agent is loaded
agent.unload() # unloads the agent's model from memory (otherwise automatically loaded/unloaded on execution of `.process()`)
agent.reset() # resets remembered chat history
agent.connect(tools=[tool], agents=[other_agent]) # connects additionnal tools/agents
agent.disconnect(tools=[tool], agents=[other_agent]) # disconnects tools/agents

# Class Optional
Agent.contract()  # Contract 
Agent.requirements()  # Configuration Requirements 
Agent.compatibility()  # Compatibility 
```

### API

#### Universal Model

A self-contained environment for running AI models with standardized interfaces.

| Method | Parameters | Return Type | Description |
|--------|------------|-------------|-------------|
| `__init__` | • `credentials: str \| Dict = None`: Authentication information (e.g. authentication token (or) object containing credentials such as  *{ id: 'example', passkey: 'example' }*)<br>• `engine: str \| List[str] = None`: Engine used (e.g., 'transformers', 'llama.cpp', (or) ordered by priority *['transformers', 'llama.cpp']*). Prefer setting quantizations over engines for broader portability.<br>• `quantization: str \| List[str] \| QuantizationSettings = None`: Quantization specification (e.g., *'Q4_K_M'*, (or) ordered by priority *['Q4_K_M', 'Q8_0']* (or) auto in range *{'default': 'Q4_K_M', 'min_precision': '4bit', 'max_precision': '8bit'}*)<br>• `max_memory_allocation: float = None`: Maximum allowed memory allocation in percentage<br>• `configuration: Dict = None`: Configuration for model and processor settings<br>• `verbose: bool \| str = "DEFAULT"`: Enable/Disable logs, or set a specific log level | `None` | Initialize a Universal Model |
| `process` | • `input: Any \| List[Message]`: Input or input messages<br>• `context: List[Any] = None`: Context items (multimodal supported)<br>• `configuration: Dict = None`: Runtime configuration<br>• `remember: bool = False`: Whether to remember this interaction. Please be mindful of the available context length of the underlaying model.<br>• `stream: bool = False`: Stream output asynchronously<br>• `keep_alive: bool = None`: Keep model loaded for faster consecutive interactions | `Tuple[Any, Dict]` | Process input through the model and return output and logs. The output is typically the model's response and the logs contain processing metadata |
| `load` | None | `None` | Load model into memory |
| `loaded` | None | `bool` | Check if model is currently loaded in memory |
| `unload` | None | `None` | Unload model from memory |
| `reset` | None | `None` | Reset model chat history |
| `configuration` | None | `Dict` | Get current model configuration |
| `(class).contract` | None | `Contract` | Model description and interface specification |
| `(class).compatibility` | None | `List[Compatibility]` | Model compatibility specification |

#### Universal Tool

A standardized interface for tools that can be used by models and agents.

| Method | Parameters | Return Type | Description |
|--------|------------|-------------|-------------|
| `__init__` | • `configuration: Dict = None`: Tool configuration including credentials | `None` | Initialize a Universal Tool |
| `(class).contract` | None | `Contract` | Tool description and interface specification |
| `(class).requirements` | None | `List[Requirement]` | Tool configuration requirements |

Additional methods are defined by the specific tool implementation and documented in the tool's contract.

Any tool specific method _must return_ a `tuple[Any, dict]`, respectively `(result, logs)`.

#### Universal Agent

An AI agent powered by Universal Models and Tools with standardized interfaces.

| Method | Parameters | Return Type | Description |
|--------|------------|-------------|-------------|
| `__init__` | • `credentials: str \| Dict = None`: Authentication information (e.g. authentication token (or) object containing credentials such as  *{ id: 'example', passkey: 'example' }*)<br>• `model: UniversalModel = None`: Model powering this agent<br>• `expand_tools: List[UniversalTool] = None`: Tools to connect<br>• `expand_team: List[UniversalAgent] = None`: Other agents to connect<br>• `configuration: Dict = None`: Agent configuration (eg. guardrails, behavior, tracing)<br>• `verbose: bool \| str = "DEFAULT"`: Enable/Disable logs, or set a specific log level | `None` | Initialize a Universal Agent |
| `process` | • `input: Any \| List[Message]`: Input or input messages<br>• `context: List[Any] = None`: Context items (multimodal)<br>• `configuration: Dict = None`: Runtime configuration<br>• `remember: bool = False`: Remember this interaction. Please be mindful of the available context length of the underlaying model.<br>• `stream: bool = False`: Stream output asynchronously<br>• `extra_tools: List[UniversalTool] = None`: Additional tools<br>• `extra_team: List[UniversalAgent] = None`: Additional agents<br>• `keep_alive: bool = None`: Keep underlaying model loaded for faster consecutive interactions | `Tuple[Any, Dict]` | Process input through the agent and return output and logs. The output is typically the agent's response and the logs contain processing metadata including tool/agent calls |
| `load` | None | `None` | Load agent's model into memory |
| `loaded` | None | `bool` | Check if the agent's model is currently loaded in memory |
| `unload` | None | `None` | Unload agent's model from memory |
| `reset` | None | `None` | Reset agent's chat history |
| `connect` | • `tools: List[UniversalTool] = None`: Tools to connect<br>• `agents: List[UniversalAgent] = None`: Agents to connect | `None` | Connect additional tools and agents |
| `disconnect` | • `tools: List[UniversalTool] = None`: Tools to disconnect<br>• `agents: List[UniversalAgent] = None`: Agents to disconnect | `None` | Disconnect tools and agents |
| `(class).contract` | None | `Contract` | Agent description and interface specification |
| `(class).requirements` | None | `List[Requirement]` | Agent configuration requirements |
| `(class).compatibility` | None | `List[Compatibility]` | Agent compatibility specification |

#### Data Structures

##### Message

| Field | Type | Description |
|-------|------|-------------|
| `role` | `str` | The role of the message sender (e.g., "system", "user") |
| `content` | `Any` | The content of the message (multimodal supported) |

##### Schema

| Field | Type | Description |
|-------|------|-------------|
| `maxLength` | `Optional[int]` | Maximum length constraint |
| `minLength` | `Optional[int]` | Maximum length constraint |
| `pattern` | `Optional[str]` | Pattern constraint |
| `nested` | `Optional[List[Argument]]` | Nested argument definitions for complex types |
| `properties` | `Optional[Dict[str, Schema]]` | Property definitions for object types |
| `items` | `Optional[Schema]` | Schema for array items |

> Expandable as needed

##### Argument

| Field | Type | Description |
|-------|------|-------------|
| `name` | `str` | Name of the argument |
| `type` | `str` | Type of the argument |
| `schema` | `Optional[Schema]` | Schema constraints |
| `description` | `str` | Description of the argument |
| `required` | `bool` | Whether the argument is required |

##### Output

| Field | Type | Description |
|-------|------|-------------|
| `type` | `str` | Type of the output |
| `description` | `str` | Description of the output |
| `required` | `bool` | Whether the output is required |

##### Method

| Field | Type | Description |
|-------|------|-------------|
| `name` | `str` | Name of the method |
| `description` | `str` | Description of the method |
| `arguments` | `List[Argument]` | List of method arguments |
| `outputs` | `List[Output]` | List of method outputs |
| `asynchronous` | `Optional[bool]` | Whether the method is asynchronous (default: False) |

##### Contract

| Field | Type | Description |
|-------|------|-------------|
| `name` | `str` | Name of the contract |
| `description` | `str` | Description of the contract |
| `methods` | `List[Method]` | List of available methods |

> When describing a Universal Model, we encourage providers to document core information such as parameter counts and context sizes.

##### Requirement

| Field | Type | Description |
|-------|------|-------------|
| `name` | `str` | Name of the requirement |
| `type` | `str` | Type of the requirement |
| `schema` | `Schema` | Schema constraints |
| `description` | `str` | Description of the requirement |
| `required` | `bool` | Whether the requirement is required |

##### Compatibility

| Field | Type | Description |
|-------|------|-------------|
| `engine` | `str` | Supported engine |
| `quantization` | `str` | Supported quantization |
| `devices` | `List[str]` | List of supported devices |
| `memory` | `float` | Required memory in GB |
| `dependencies` | `List[str]` | Required software dependencies |
| `precision` | `int` | Precision in bits |

##### QuantizationSettings

| Field | Type | Description |
|-------|------|-------------|
| `default` | `Optional[str]` | Default quantization to use (e.g., 'Q4_K_M'), otherwise using defaults set in `sources.yaml` |
| `min_precision` | `Optional[str]` | Minimum precision requirement (e.g., '4bit'). Default: Lowest between 4 bit and the default's precision if explicitly provided. |
| `max_precision` | `Optional[str]` | Maximum precision requirement (e.g., '8bit'). Default: 8 bit or the default's precision if explicitly provided.  |

> Expandable as needed

### Development

Abstract classes and types for `Universal Intelligence` components are made available by the package if you wish to develop and publish your own.

```sh
# Install abstracts
pip install universal-intelligence
```

```python
from universal_intelligence.core import AbstractUniversalModel, AbstractUniversalTool, AbstractUniversalAgent, types

class UniversalModel(AbstractUniversalModel):
  # ...
  pass

class UniversalTool(AbstractUniversalTool):
  # ...
  pass

class UniversalAgent(AbstractUniversalAgent):
  # ...
  pass
```

If you wish to contribute to community based components, [mixins](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/__utils__/mixins) are made available to allow quickly bootstrapping new `Universal Models`.

> See *Community>Development* section below for additional information.

</details>

<details>
<summary><strong style="display: inline; cursor: pointer; margin: 0; padding: 0;">Community Components</strong></summary>

## Community Components

The `universal-intelligence` package provides several community-built models, agents, and tools that you can use out of the box.

### Installation

```sh
# Install with device optimizations
pip install "universal-intelligence[community,mps]" # Apple
pip install "universal-intelligence[community,cuda]" # NVIDIA
```

Some components may require additional dependencies. These can be installed on demand.

```sh
# Install MCP specific dependencies
pip install "universal-intelligence[community,mps,mcp]" # Apple
pip install "universal-intelligence[community,cuda,mcp]" # NVIDIA
```

> Some of the community components interface with gated models, in which case you may have to accept the model's terms on [Hugging Face](https://huggingface.co/docs/hub/en/models-gated) and log into that approved account. 
> 
> You may do so in your terminal using `huggingface-cli login`
> 
> or in your code: 
> ```python
> from huggingface_hub import login
> login()
> ```

### Playground

You can get familiar with the library using our ready-made playground

```sh
python -m playground.example 
```

or online using our [**Google Colab Playground**](https://colab.research.google.com/drive/19RasWzFIZkbHeWDLGk9s2Tq8_Ws2G4O_?usp=sharing)!

### Usage

#### Local Models

```python
from universal_intelligence.community.models.local.default import UniversalModel as Model

model = Model()
output, logs = model.process("How are you doing today?")
```

> View [Universal Intelligence Protocols](https://github.com/spacehendrix/universal-intelligence/blob/main/README.md) for additional information.

#### Remote Models

```python
from universal_intelligence.community.models.remote.default import UniversalModel as Model # (or) .default__free

model = Model(credentials='your-openrouter-api-key-here')
output, logs = model.process("How are you doing today?")
```

> View [Universal Intelligence Protocols](https://github.com/spacehendrix/universal-intelligence/blob/main/README.md) for additional information.

#### Tools

```python
from universal_intelligence.community.tools.simple_printer import UniversalTool as Tool

tool = Tool()
result, logs = tool.print_text("This needs to be printed")
```

> View [Universal Intelligence Protocols](https://github.com/spacehendrix/universal-intelligence/blob/main/README.md) for additional information.

#### Agents

```python
from universal_intelligence.community.agents.default import UniversalAgent as Agent

agent = Agent(
  # model=Model(),                  # customize or share 🧠 across [🤖,🤖,🤖,..]
  # expand_tools=[Tool()],          # expand 🔧 set
  # expand_team=[OtherAgent()]      # expand 🤖 team
)
result, logs = agent.process("Please print 'Hello World' to the console", extra_tools=[Tool()])
```

> View [Universal Intelligence Protocols](https://github.com/spacehendrix/universal-intelligence/blob/main/README.md) for additional information.

### Supported Components

#### Models

##### Local Models

> Import path: `universal_intelligence.community.models.local.<import>`
> 
> (eg. *universal_intelligence.community.models.local.default*)

| I/O | Name | Import | Description | Supported Configurations |
|------|------|------|-------------|-----------|
| Text/Text | *Qwen2.5-7B-Instruct* (default)| `default`<br> or `qwen2_5_7b_instruct` | Small powerful model by Alibaba Cloud |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/qwen2_5_7b_instruct/sources.yaml)<br><br>Default:<br>`cuda:BNB_4:transformers`<br>`mps:MLX_4:mlx`<br>`cpu:Q4_K_M:llama.cpp` |
| Text/Text | *Qwen2.5-32B-Instruct* | `qwen2_5_32b_instruct` | Large powerful model by Alibaba Cloud |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/qwen2_5_32b_instruct/sources.yaml)<br><br>Default:<br>`cuda:BNB_4:transformers`<br>`mps:MLX_4:mlx`<br>`cpu:Q4_K_M:llama.cpp` |
| Text/Text | *Qwen2.5-14B-Instruct* | `qwen2_5_14b_instruct` | Medium powerful model by Alibaba Cloud |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/qwen2_5_14b_instruct/sources.yaml)<br><br>Default:<br>`cuda:BNB_4:transformers`<br>`mps:MLX_4:mlx`<br>`cpu:Q4_K_M:llama.cpp` |
| Text/Text | *Qwen2.5-14B-Instruct-1M* | `qwen2_5_14b_instruct_1m` | Medium powerful model with 1M context by Alibaba Cloud |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/qwen2_5_14b_instruct_1m/sources.yaml)<br><br>Default:<br>`cuda:BNB_4:transformers`<br>`mps:MLX_4:mlx`<br>`cpu:Q4_K_M:llama.cpp` |
| Text/Text | *Qwen2.5-7B-Instruct-1M* | `qwen2_5_7b_instruct_1m` | Small powerful model with 1M context by Alibaba Cloud |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/qwen2_5_7b_instruct_1m/sources.yaml)<br><br>Default:<br>`cuda:BNB_4:transformers`<br>`mps:MLX_4:mlx`<br>`cpu:Q4_K_M:llama.cpp` |
| Text/Text | *Qwen2.5-3B-Instruct* | `qwen2_5_3b_instruct` | Compact powerful model by Alibaba Cloud |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/qwen2_5_3b_instruct/sources.yaml)<br><br>Default:<br>`cuda:BNB_4:transformers`<br>`mps:MLX_4:mlx`<br>`cpu:Q4_K_M:llama.cpp` |
| Text/Text | *Qwen2.5-1.5B-Instruct* | `qwen2_5_1d5b_instruct` | Ultra-compact powerful model by Alibaba Cloud |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/qwen2_5_1d5b_instruct/sources.yaml)<br><br>Default:<br>`cuda:bfloat16:transformers`<br>`mps:MLX_8:mlx`<br>`cpu:Q4_K_M:llama.cpp` |
| Text/Text | *gemma-3-27b-it* | `gemma3_27b_it` | Large powerful model by Google |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/gemma3_27b_it/sources.yaml)<br><br>Default:<br>`cuda:Q4_K_M:llama.cpp`<br>`mps:Q4_K_M:llama.cpp`<br>`cpu:Q4_K_M:llama.cpp` |
| Text/Text | *gemma-3-12b-it* | `gemma3_12b_it` | Medium powerful model by Google |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/gemma3_12b_it/sources.yaml)<br><br>Default:<br>`cuda:Q4_K_M:llama.cpp`<br>`mps:MLX_4:mlx`<br>`cpu:Q4_K_M:llama.cpp` |
| Text/Text | *gemma-3-4b-it* | `gemma3_4b_it` | Small powerful model by Google |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/gemma3_4b_it/sources.yaml)<br><br>Default:<br>`cuda:Q4_K_M:llama.cpp`<br>`mps:MLX_4:mlx`<br>`cpu:Q4_K_M:llama.cpp` |
| Text/Text | *gemma-3-1b-it* | `gemma3_1b_it` | Ultra-compact powerful model by Google |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/gemma3_1b_it/sources.yaml)<br><br>Default:<br>`cuda:bfloat16:transformers`<br>`mps:bfloat16:transformers`<br>`cpu:bfloat16:transformers` |
| Text/Text | *falcon-3-10b-instruct* | `falcon3_10b_instruct` | Medium powerful model by TII |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/falcon3_10b_instruct/sources.yaml)<br><br>Default:<br>`cuda:AWQ_4:transformers`<br>`mps:MLX_4:mlx`<br>`cpu:Q4_K_M:llama.cpp` |
| Text/Text | *falcon-3-7b-instruct* | `falcon3_7b_instruct` | Small powerful model by TII |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/falcon3_7b_instruct/sources.yaml)<br><br>Default:<br>`cuda:Q4_K_M:llama.cpp`<br>`mps:Q4_K_M:llama.cpp`<br>`cpu:Q4_K_M:llama.cpp` |
| Text/Text | *falcon-3-3b-instruct* | `falcon3_3b_instruct` | Compact powerful model by TII |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/falcon3_3b_instruct/sources.yaml)<br><br>Default:<br>`cuda:bfloat16:transformers`<br>`mps:bfloat16:transformers`<br>`cpu:bfloat16:transformers` |
| Text/Text | *Llama-3.3-70B-Instruct* | `llama3_3_70b_instruct` | Large powerful model by Meta |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/llama3_3_70b_instruct/sources.yaml)<br><br>Default:<br>`cuda:BNB_4:transformers`<br>`mps:MLX_4:mlx`<br>`cpu:Q4_K_M:llama.cpp` |
| Text/Text | *Llama-3.1-8B-Instruct* | `llama3_1_8b_instruct` | Small powerful model by Meta |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/llama3_1_8b_instruct/sources.yaml)<br><br>Default:<br>`cuda:BNB_4:transformers`<br>`mps:MLX_4:mlx`<br>`cpu:Q4_K_M:llama.cpp` |
| Text/Text | *Llama-3.2-3B-Instruct* | `llama3_2_3b_instruct` | Compact powerful model by Meta |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/llama3_2_3b_instruct/sources.yaml)<br><br>Default:<br>`cuda:BNB_4:transformers`<br>`mps:MLX_4:mlx`<br>`cpu:Q4_K_M:llama.cpp` |
| Text/Text | *Llama-3.2-1B-Instruct* | `llama3_2_1b_instruct` | Ultra-compact powerful model by Meta |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/llama3_2_1b_instruct/sources.yaml)<br><br>Default:<br>`cuda:bfloat16:transformers`<br>`mps:bfloat16:transformers`<br>`cpu:Q4_K_M:llama.cpp` |
| Text/Text | *phi-4* | `phi4` | Small powerful model by Microsoft |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/phi4/sources.yaml)<br><br>Default:<br>`cuda:BNB_4:transformers`<br>`mps:MLX_4:mlx`<br>`cpu:Q4_K_M:llama.cpp` |
| Text/Text | *phi-4-mini-instruct* | `phi4_mini_instruct` | Compact powerful model by Microsoft |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/phi4_mini_instruct/sources.yaml)<br><br>Default:<br>`cuda:Q4_K_M:llama.cpp`<br>`mps:MLX_4:mlx`<br>`cpu:Q4_K_M:llama.cpp` |
| Text/Text | *smollm2-1.7b-instruct* | `smollm2_1d7b_instruct` | Small powerful model by SmolLM |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/smollm2_1d7b_instruct/sources.yaml)<br><br>Default:<br>`cuda:bfloat16:transformers`<br>`mps:MLX_8:mlx`<br>`cpu:Q4_K_M:llama.cpp` |
| Text/Text | *smollm2-360m-instruct* | `smollm2_360m_instruct` | Ultra-compact powerful model by SmolLM |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/smollm2_360m_instruct/sources.yaml)<br><br>Default:<br>`cuda:bfloat16:transformers`<br>`mps:MLX_8:mlx`<br>`cpu:Q4_K_M:llama.cpp` |
| Text/Text | *smollm2-135m-instruct* | `smollm2_135m_instruct` | Ultra-compact powerful model by SmolLM |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/smollm2_135m_instruct/sources.yaml)<br><br>Default:<br>`cuda:bfloat16:transformers`<br>`mps:MLX_8:mlx`<br>`cpu:bfloat16:transformers` |
| Text/Text | *mistral-7b-instruct-v0.3* | `mistral_7b_instruct_v0d3` | Small powerful model by Mistral |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/mistral_7b_instruct_v0d3/sources.yaml)<br><br>Default:<br>`cuda:Q4_K_M:llama.cpp`<br>`mps:MLX_4:mlx`<br>`cpu:Q4_K_M:llama.cpp` |
| Text/Text | *mistral-nemo-instruct-2407* | `mistral_nemo_instruct_2407` | Small powerful model by Mistral |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/mistral_nemo_instruct_2407/sources.yaml)<br><br>Default:<br>`cuda:AWQ_4:transformers`<br>`mps:MLX_3:mlx`<br>`cpu:Q4_K_M:llama.cpp` |
| Text/Text | *OpenR1-Qwen-7B* | `openr1_qwen_7b` | Medium powerful model by Open R1 |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/openr1_qwen_7b/sources.yaml)<br><br>Default:<br>`cuda:BNB_4:transformers`<br>`mps:MLX_4:mlx`<br>`cpu:Q4_K_M:llama.cpp` |
| Text/Text | *QwQ-32B* | `qwq_32b` | Large powerful model by Qwen |  [Supported Configurations](https://github.com/spacehendrix/universal-intelligence/blob/main/universal_intelligence/community/models/qwq_32b/sources.yaml)<br><br>Default:<br>`cuda:BNB_4:transformers`<br>`mps:MLX_4:mlx`<br>`cpu:Q4_K_M:llama.cpp` |

##### Remote Models

> Import path: `universal_intelligence.community.models.remote.<import>`
> 
> (eg. *universal_intelligence.community.models.remote.default*)

| I/O | Name | Import | Description | Provider |
|------|------|------|-------------|-----------|
| Text/Text | *deepseek/deepseek-r1:free* | `default__free` (default free) | DeepSeek R1 is here: Performance on par with [OpenAI o1](/openai/o1), but open-sourced and with fully open reasoning tokens. It's 671B parameters in size, with 37B active in an inference pass. Fully open-source model & [technical report](https://api-docs.deepseek.com/news/news250120). MIT licensed: Distill & commercialize freely! |  `openrouter` |
| Text/Text | *openrouter/auto* | `default` (default paid) | Your prompt will be processed by a meta-model and routed to one of dozens of models (see below), optimizing for the best possible output. To see which model was used, visit [Activity](/activity), or read the `model` attribute of the response. Your response will be priced at the same rate as the routed model. The meta-model is powered by [Not Diamond](https://docs.notdiamond.ai/docs/how-not-diamond-works). Learn more in our [docs](/docs/model-routing). Requests will be routed to the following models:- [openai/gpt-4o-2024-08-06](/openai/gpt-4o-2024-08-06)- [openai/gpt-4o-2024-05-13](/openai/gpt-4o-2024-05-13)- [openai/gpt-4o-mini-2024-07-18](/openai/gpt-4o-mini-2024-07-18)- [openai/chatgpt-4o-latest](/openai/chatgpt-4o-latest)- [openai/o1-preview-2024-09-12](/openai/o1-preview-2024-09-12)- [openai/o1-mini-2024-09-12](/openai/o1-mini-2024-09-12)- [anthropic/claude-3.5-sonnet](/anthropic/claude-3.5-sonnet)- [anthropic/claude-3.5-haiku](/anthropic/claude-3.5-haiku)- [anthropic/claude-3-opus](/anthropic/claude-3-opus)- [anthropic/claude-2.1](/anthropic/claude-2.1)- [google/gemini-pro-1.5](/google/gemini-pro-1.5)- [google/gemini-flash-1.5](/google/gemini-flash-1.5)- [mistralai/mistral-large-2407](/mistralai/mistral-large-2407)- [mistralai/mistral-nemo](/mistralai/mistral-nemo)- [deepseek/deepseek-r1](/deepseek/deepseek-r1)- [meta-llama/llama-3.1-70b-instruct](/meta-llama/llama-3.1-70b-instruct)- [meta-llama/llama-3.1-405b-instruct](/meta-llama/llama-3.1-405b-instruct)- [mistralai/mixtral-8x22b-instruct](/mistralai/mixtral-8x22b-instruct)- [cohere/command-r-plus](/cohere/command-r-plus)- [cohere/command-r](/cohere/command-r) |  `openrouter` |
| Text/Text | *01-ai/yi-large* | `yi_large` | The Yi Large model was designed by 01.AI with the following usecases in mind: knowledge search, data classification, human-like chat bots, and customer service. It stands out for its multilingual proficiency, particularly in Spanish, Chinese, Japanese, German, and French. Check out the [launch announcement](https://01-ai.github.io/blog/01.ai-yi-large-llm-launch) to learn more. |  `openrouter` |
| Text/Text | *aetherwiing/mn-starcannon-12b* | `mn_starcannon_12b` | Starcannon 12B v2 is a creative roleplay and story writing model, based on Mistral Nemo, using [nothingiisreal/mn-celeste-12b](/nothingiisreal/mn-celeste-12b) as a base, with [intervitens/mini-magnum-12b-v1.1](https://huggingface.co/intervitens/mini-magnum-12b-v1.1) merged in using the [TIES](https://arxiv.org/abs/2306.01708) method. Although more similar to Magnum overall, the model remains very creative, with a pleasant writing style. It is recommended for people wanting more variety than Magnum, and yet more verbose prose than Celeste. |  `openrouter` |
| Text/Text | *agentica-org/deepcoder-14b-preview:free* | `deepcoder_14b_preview__free` | DeepCoder-14B-Preview is a 14B parameter code generation model fine-tuned from DeepSeek-R1-Distill-Qwen-14B using reinforcement learning with GRPO+ and iterative context lengthening. It is optimized for long-context program synthesis and achieves strong performance across coding benchmarks, including 60.6% on LiveCodeBench v5, competitive with models like o3-Mini |  `openrouter` |
| Text/Text | *ai21/jamba-1.6-large* | `jamba_1_6_large` | AI21 Jamba Large 1.6 is a high-performance hybrid foundation model combining State Space Models (Mamba) with Transformer attention mechanisms. Developed by AI21, it excels in extremely long-context handling (256K tokens), demonstrates superior inference efficiency (up to 2.5x faster than comparable models), and supports structured JSON output and tool-use capabilities. It has 94 billion active parameters (398 billion total), optimized quantization support (ExpertsInt8), and multilingual proficiency in languages such as English, Spanish, French, Portuguese, Italian, Dutch, German, Arabic, and Hebrew. Usage of this model is subject to the [Jamba Open Model License](https://www.ai21.com/licenses/jamba-open-model-license). |  `openrouter` |
| Text/Text | *ai21/jamba-1.6-mini* | `jamba_1_6_mini` | AI21 Jamba Mini 1.6 is a hybrid foundation model combining State Space Models (Mamba) with Transformer attention mechanisms. With 12 billion active parameters (52 billion total), this model excels in extremely long-context tasks (up to 256K tokens) and achieves superior inference efficiency, outperforming comparable open models on tasks such as retrieval-augmented generation (RAG) and grounded question answering. Jamba Mini 1.6 supports multilingual tasks across English, Spanish, French, Portuguese, Italian, Dutch, German, Arabic, and Hebrew, along with structured JSON output and tool-use capabilities. Usage of this model is subject to the [Jamba Open Model License](https://www.ai21.com/licenses/jamba-open-model-license). |  `openrouter` |
| Text/Text | *ai21/jamba-instruct* | `jamba_instruct` | The Jamba-Instruct model, introduced by AI21 Labs, is an instruction-tuned variant of their hybrid SSM-Transformer Jamba model, specifically optimized for enterprise applications.- 256K Context Window: It can process extensive information, equivalent to a 400-page novel, which is beneficial for tasks involving large documents such as financial reports or legal documents- Safety and Accuracy: Jamba-Instruct is designed with enhanced safety features to ensure secure deployment in enterprise environments, reducing the risk and cost of implementation Read their [announcement](https://www.ai21.com/blog/announcing-jamba) to learn more. Jamba has a knowledge cutoff of February 2024. |  `openrouter` |
| Text/Text | *aion-labs/aion-1.0* | `aion_1_0` | Aion-1.0 is a multi-model system designed for high performance across various tasks, including reasoning and coding. It is built on DeepSeek-R1, augmented with additional models and techniques such as Tree of Thoughts (ToT) and Mixture of Experts (MoE). It is Aion Lab's most powerful reasoning model. |  `openrouter` |
| Text/Text | *aion-labs/aion-1.0-mini* | `aion_1_0_mini` | Aion-1.0-Mini 32B parameter model is a distilled version of the DeepSeek-R1 model, designed for strong performance in reasoning domains such as mathematics, coding, and logic. It is a modified variant of a FuseAI model that outperforms R1-Distill-Qwen-32B and R1-Distill-Llama-70B, with benchmark results available on its [Hugging Face page](https://huggingface.co/FuseAI/FuseO1-DeepSeekR1-QwQ-SkyT1-32B-Preview), independently replicated for verification. |  `openrouter` |
| Text/Text | *aion-labs/aion-rp-llama-3.1-8b* | `aion_rp_llama_3_1_8b` | Aion-RP-Llama-3.1-8B ranks the highest in the character evaluation portion of the RPBench-Auto benchmark, a roleplaying-specific variant of Arena-Hard-Auto, where LLMs evaluate each other's responses. It is a fine-tuned base model rather than an instruct model, designed to produce more natural and varied writing. |  `openrouter` |
| Text/Text | *alfredpros/codellama-7b-instruct-solidity* | `codellama_7b_instruct_solidity` | A finetuned 7 billion parameters Code LLaMA - Instruct model to generate Solidity smart contract using 4-bit QLoRA finetuning provided by PEFT library. |  `openrouter` |
| Text/Text | *all-hands/openhands-lm-32b-v0.1* | `openhands_lm_32b_v0_1` | OpenHands LM v0.1 is a 32B open-source coding model fine-tuned from Qwen2.5-Coder-32B-Instruct using reinforcement learning techniques outlined in SWE-Gym. It is optimized for autonomous software development agents and achieves strong performance on SWE-Bench Verified, with a 37.2% resolve rate. The model supports a 128K token context window, making it well-suited for long-horizon code reasoning and large codebase tasks. OpenHands LM is designed for local deployment and runs on consumer-grade GPUs such as a single 3090. It enables fully offline agent workflows without dependency on proprietary APIs. This release is intended as a research preview, and future updates aim to improve generalizability, reduce repetition, and offer smaller variants. |  `openrouter` |
| Text/Text | *allenai/olmo-7b-instruct* | `olmo_7b_instruct` | OLMo 7B Instruct by the Allen Institute for AI is a model finetuned for question answering. It demonstrates **notable performance** across multiple benchmarks including TruthfulQA and ToxiGen.**Open Source**: The model, its code, checkpoints, logs are released under the [Apache 2.0 license](https://choosealicense.com/licenses/apache-2.0).- [Core repo (training, inference, fine-tuning etc.)](https://github.com/allenai/OLMo)- [Evaluation code](https://github.com/allenai/OLMo-Eval)- [Further fine-tuning code](https://github.com/allenai/open-instruct)- [Paper](https://arxiv.org/abs/2402.00838)- [Technical blog post](https://blog.allenai.org/olmo-open-language-model-87ccfc95f580)- [W&B Logs](https://wandb.ai/ai2-llm/OLMo-7B/reports/OLMo-7B--Vmlldzo2NzQyMzk5) |  `openrouter` |
| Text/Text | *alpindale/goliath-120b* | `goliath_120b` | A large LLM created by combining two fine-tuned Llama 70B models into one 120B model. Combines Xwin and Euryale. Credits to- [@chargoddard](https://huggingface.co/chargoddard) for developing the framework used to merge the model - [mergekit](https://github.com/cg123/mergekit).- [@Undi95](https://huggingface.co/Undi95) for helping with the merge ratios.#merge |  `openrouter` |
| Text/Text | *alpindale/magnum-72b* | `magnum_72b` | From the maker of [Goliath](https://openrouter.ai/models/alpindale/goliath-120b), Magnum 72B is the first in a new family of models designed to achieve the prose quality of the Claude 3 models, notably Opus & Sonnet. The model is based on [Qwen2 72B](https://openrouter.ai/models/qwen/qwen-2-72b-instruct) and trained with 55 million tokens of highly curated roleplay (RP) data. |  `openrouter` |
| Text/Text | *amazon/nova-lite-v1* | `nova_lite_v1` | Amazon Nova Lite 1.0 is a very low-cost multimodal model from Amazon that focused on fast processing of image, video, and text inputs to generate text output. Amazon Nova Lite can handle real-time customer interactions, document analysis, and visual question-answering tasks with high accuracy. With an input context of 300K tokens, it can analyze multiple images or up to 30 minutes of video in a single input. |  `openrouter` |
| Text/Text | *amazon/nova-micro-v1* | `nova_micro_v1` | Amazon Nova Micro 1.0 is a text-only model that delivers the lowest latency responses in the Amazon Nova family of models at a very low cost. With a context length of 128K tokens and optimized for speed and cost, Amazon Nova Micro excels at tasks such as text summarization, translation, content classification, interactive chat, and brainstorming. It has  simple mathematical reasoning and coding abilities. |  `openrouter` |
| Text/Text | *amazon/nova-pro-v1* | `nova_pro_v1` | Amazon Nova Pro 1.0 is a capable multimodal model from Amazon focused on providing a combination of accuracy, speed, and cost for a wide range of tasks. As of December 2024, it achieves state-of-the-art performance on key benchmarks including visual question answering (TextVQA) and video understanding (VATEX). Amazon Nova Pro demonstrates strong capabilities in processing both visual and textual information and at analyzing financial documents.**NOTE**: Video input is not supported at this time. |  `openrouter` |
| Text/Text | *anthracite-org/magnum-v2-72b* | `magnum_v2_72b` | From the maker of [Goliath](https://openrouter.ai/models/alpindale/goliath-120b), Magnum 72B is the seventh in a family of models designed to achieve the prose quality of the Claude 3 models, notably Opus & Sonnet. The model is based on [Qwen2 72B](https://openrouter.ai/models/qwen/qwen-2-72b-instruct) and trained with 55 million tokens of highly curated roleplay (RP) data. |  `openrouter` |
| Text/Text | *anthracite-org/magnum-v4-72b* | `magnum_v4_72b` | This is a series of models designed to replicate the prose quality of the Claude 3 models, specifically Sonnet(https://openrouter.ai/anthropic/claude-3.5-sonnet) and Opus(https://openrouter.ai/anthropic/claude-3-opus). The model is fine-tuned on top of [Qwen2.5 72B](https://openrouter.ai/qwen/qwen-2.5-72b-instruct). |  `openrouter` |
| Text/Text | *anthropic/claude-2* | `claude_2` | Claude 2 delivers advancements in key capabilities for enterprises—including an industry-leading 200K token context window, significant reductions in rates of model hallucination, system prompts and a new beta feature: tool use. |  `openrouter` |
| Text/Text | *anthropic/claude-2.0* | `claude_2_0` | Anthropic's flagship model. Superior performance on tasks that require complex reasoning. Supports hundreds of pages of text. |  `openrouter` |
| Text/Text | *anthropic/claude-2.0:beta* | `claude_2_0__beta` | Anthropic's flagship model. Superior performance on tasks that require complex reasoning. Supports hundreds of pages of text. |  `openrouter` |
| Text/Text | *anthropic/claude-2.1* | `claude_2_1` | Claude 2 delivers advancements in key capabilities for enterprises—including an industry-leading 200K token context window, significant reductions in rates of model hallucination, system prompts and a new beta feature: tool use. |  `openrouter` |
| Text/Text | *anthropic/claude-2.1:beta* | `claude_2_1__beta` | Claude 2 delivers advancements in key capabilities for enterprises—including an industry-leading 200K token context window, significant reductions in rates of model hallucination, system prompts and a new beta feature: tool use. |  `openrouter` |
| Text/Text | *anthropic/claude-2:beta* | `claude_2__beta` | Claude 2 delivers advancements in key capabilities for enterprises—including an industry-leading 200K token context window, significant reductions in rates of model hallucination, system prompts and a new beta feature: tool use. |  `openrouter` |
| Text/Text | *anthropic/claude-3-haiku* | `claude_3_haiku` | Claude 3 Haiku is Anthropic's fastest and most compact model for near-instant responsiveness. Quick and accurate targeted performance. See the launch announcement and benchmark results [here](https://www.anthropic.com/news/claude-3-haiku)#multimodal |  `openrouter` |
| Text/Text | *anthropic/claude-3-haiku:beta* | `claude_3_haiku__beta` | Claude 3 Haiku is Anthropic's fastest and most compact model for near-instant responsiveness. Quick and accurate targeted performance. See the launch announcement and benchmark results [here](https://www.anthropic.com/news/claude-3-haiku)#multimodal |  `openrouter` |
| Text/Text | *anthropic/claude-3-opus* | `claude_3_opus` | Claude 3 Opus is Anthropic's most powerful model for highly complex tasks. It boasts top-level performance, intelligence, fluency, and understanding. See the launch announcement and benchmark results [here](https://www.anthropic.com/news/claude-3-family)#multimodal |  `openrouter` |
| Text/Text | *anthropic/claude-3-opus:beta* | `claude_3_opus__beta` | Claude 3 Opus is Anthropic's most powerful model for highly complex tasks. It boasts top-level performance, intelligence, fluency, and understanding. See the launch announcement and benchmark results [here](https://www.anthropic.com/news/claude-3-family)#multimodal |  `openrouter` |
| Text/Text | *anthropic/claude-3-sonnet* | `claude_3_sonnet` | Claude 3 Sonnet is an ideal balance of intelligence and speed for enterprise workloads. Maximum utility at a lower price, dependable, balanced for scaled deployments. See the launch announcement and benchmark results [here](https://www.anthropic.com/news/claude-3-family)#multimodal |  `openrouter` |
| Text/Text | *anthropic/claude-3-sonnet:beta* | `claude_3_sonnet__beta` | Claude 3 Sonnet is an ideal balance of intelligence and speed for enterprise workloads. Maximum utility at a lower price, dependable, balanced for scaled deployments. See the launch announcement and benchmark results [here](https://www.anthropic.com/news/claude-3-family)#multimodal |  `openrouter` |
| Text/Text | *anthropic/claude-3.5-haiku* | `claude_3_5_haiku` | Claude 3.5 Haiku features offers enhanced capabilities in speed, coding accuracy, and tool use. Engineered to excel in real-time applications, it delivers quick response times that are essential for dynamic tasks such as chat interactions and immediate coding suggestions. This makes it highly suitable for environments that demand both speed and precision, such as software development, customer service bots, and data management systems. This model is currently pointing to [Claude 3.5 Haiku (2024-10-22)](/anthropic/claude-3-5-haiku-20241022). |  `openrouter` |
| Text/Text | *anthropic/claude-3.5-haiku-20241022* | `claude_3_5_haiku_20241022` | Claude 3.5 Haiku features enhancements across all skill sets including coding, tool use, and reasoning. As the fastest model in the Anthropic lineup, it offers rapid response times suitable for applications that require high interactivity and low latency, such as user-facing chatbots and on-the-fly code completions. It also excels in specialized tasks like data extraction and real-time content moderation, making it a versatile tool for a broad range of industries. It does not support image inputs. See the launch announcement and benchmark results [here](https://www.anthropic.com/news/3-5-models-and-computer-use) |  `openrouter` |
| Text/Text | *anthropic/claude-3.5-haiku-20241022:beta* | `claude_3_5_haiku_20241022__beta` | Claude 3.5 Haiku features enhancements across all skill sets including coding, tool use, and reasoning. As the fastest model in the Anthropic lineup, it offers rapid response times suitable for applications that require high interactivity and low latency, such as user-facing chatbots and on-the-fly code completions. It also excels in specialized tasks like data extraction and real-time content moderation, making it a versatile tool for a broad range of industries. It does not support image inputs. See the launch announcement and benchmark results [here](https://www.anthropic.com/news/3-5-models-and-computer-use) |  `openrouter` |
| Text/Text | *anthropic/claude-3.5-haiku:beta* | `claude_3_5_haiku__beta` | Claude 3.5 Haiku features offers enhanced capabilities in speed, coding accuracy, and tool use. Engineered to excel in real-time applications, it delivers quick response times that are essential for dynamic tasks such as chat interactions and immediate coding suggestions. This makes it highly suitable for environments that demand both speed and precision, such as software development, customer service bots, and data management systems. This model is currently pointing to [Claude 3.5 Haiku (2024-10-22)](/anthropic/claude-3-5-haiku-20241022). |  `openrouter` |
| Text/Text | *anthropic/claude-3.5-sonnet* | `claude_3_5_sonnet` | New Claude 3.5 Sonnet delivers better-than-Opus capabilities, faster-than-Sonnet speeds, at the same Sonnet prices. Sonnet is particularly good at:- Coding: Scores ~49% on SWE-Bench Verified, higher than the last best score, and without any fancy prompt scaffolding- Data science: Augments human data science expertise; navigates unstructured data while using multiple tools for insights- Visual processing: excelling at interpreting charts, graphs, and images, accurately transcribing text to derive insights beyond just the text alone- Agentic tasks: exceptional tool use, making it great at agentic tasks (i.e. complex, multi-step problem solving tasks that require engaging with other systems)#multimodal |  `openrouter` |
| Text/Text | *anthropic/claude-3.5-sonnet-20240620* | `claude_3_5_sonnet_20240620` | Claude 3.5 Sonnet delivers better-than-Opus capabilities, faster-than-Sonnet speeds, at the same Sonnet prices. Sonnet is particularly good at:- Coding: Autonomously writes, edits, and runs code with reasoning and troubleshooting- Data science: Augments human data science expertise; navigates unstructured data while using multiple tools for insights- Visual processing: excelling at interpreting charts, graphs, and images, accurately transcribing text to derive insights beyond just the text alone- Agentic tasks: exceptional tool use, making it great at agentic tasks (i.e. complex, multi-step problem solving tasks that require engaging with other systems) For the latest version (2024-10-23), check out [Claude 3.5 Sonnet](/anthropic/claude-3.5-sonnet).#multimodal |  `openrouter` |
| Text/Text | *anthropic/claude-3.5-sonnet-20240620:beta* | `claude_3_5_sonnet_20240620__beta` | Claude 3.5 Sonnet delivers better-than-Opus capabilities, faster-than-Sonnet speeds, at the same Sonnet prices. Sonnet is particularly good at:- Coding: Autonomously writes, edits, and runs code with reasoning and troubleshooting- Data science: Augments human data science expertise; navigates unstructured data while using multiple tools for insights- Visual processing: excelling at interpreting charts, graphs, and images, accurately transcribing text to derive insights beyond just the text alone- Agentic tasks: exceptional tool use, making it great at agentic tasks (i.e. complex, multi-step problem solving tasks that require engaging with other systems) For the latest version (2024-10-23), check out [Claude 3.5 Sonnet](/anthropic/claude-3.5-sonnet).#multimodal |  `openrouter` |
| Text/Text | *anthropic/claude-3.5-sonnet:beta* | `claude_3_5_sonnet__beta` | New Claude 3.5 Sonnet delivers better-than-Opus capabilities, faster-than-Sonnet speeds, at the same Sonnet prices. Sonnet is particularly good at:- Coding: Scores ~49% on SWE-Bench Verified, higher than the last best score, and without any fancy prompt scaffolding- Data science: Augments human data science expertise; navigates unstructured data while using multiple tools for insights- Visual processing: excelling at interpreting charts, graphs, and images, accurately transcribing text to derive insights beyond just the text alone- Agentic tasks: exceptional tool use, making it great at agentic tasks (i.e. complex, multi-step problem solving tasks that require engaging with other systems)#multimodal |  `openrouter` |
| Text/Text | *anthropic/claude-3.7-sonnet* | `claude_3_7_sonnet` | Claude 3.7 Sonnet is an advanced large language model with improved reasoning, coding, and problem-solving capabilities. It introduces a hybrid reasoning approach, allowing users to choose between rapid responses and extended, step-by-step processing for complex tasks. The model demonstrates notable improvements in coding, particularly in front-end development and full-stack updates, and excels in agentic workflows, where it can autonomously navigate multi-step processes.  Claude 3.7 Sonnet maintains performance parity with its predecessor in standard mode while offering an extended reasoning mode for enhanced accuracy in math, coding, and instruction-following tasks. Read more at the [blog post here](https://www.anthropic.com/news/claude-3-7-sonnet) |  `openrouter` |
| Text/Text | *anthropic/claude-3.7-sonnet:beta* | `claude_3_7_sonnet__beta` | Claude 3.7 Sonnet is an advanced large language model with improved reasoning, coding, and problem-solving capabilities. It introduces a hybrid reasoning approach, allowing users to choose between rapid responses and extended, step-by-step processing for complex tasks. The model demonstrates notable improvements in coding, particularly in front-end development and full-stack updates, and excels in agentic workflows, where it can autonomously navigate multi-step processes.  Claude 3.7 Sonnet maintains performance parity with its predecessor in standard mode while offering an extended reasoning mode for enhanced accuracy in math, coding, and instruction-following tasks. Read more at the [blog post here](https://www.anthropic.com/news/claude-3-7-sonnet) |  `openrouter` |
| Text/Text | *anthropic/claude-3.7-sonnet:thinking* | `claude_3_7_sonnet__thinking` | Claude 3.7 Sonnet is an advanced large language model with improved reasoning, coding, and problem-solving capabilities. It introduces a hybrid reasoning approach, allowing users to choose between rapid responses and extended, step-by-step processing for complex tasks. The model demonstrates notable improvements in coding, particularly in front-end development and full-stack updates, and excels in agentic workflows, where it can autonomously navigate multi-step processes.  Claude 3.7 Sonnet maintains performance parity with its predecessor in standard mode while offering an extended reasoning mode for enhanced accuracy in math, coding, and instruction-following tasks. Read more at the [blog post here](https://www.anthropic.com/news/claude-3-7-sonnet) |  `openrouter` |
| Text/Text | *arcee-ai/arcee-blitz* | `arcee_blitz` | Arcee Blitz is a 24 B‑parameter dense model distilled from DeepSeek and built on Mistral architecture for 'everyday' chat. The distillation‑plus‑refinement pipeline trims compute while keeping DeepSeek‑style reasoning, so Blitz punches above its weight on MMLU, GSM‑8K and BBH compared with other mid‑size open models. With a default 128 k context window and competitive throughput, it serves as a cost‑efficient workhorse for summarization, brainstorming and light code help. Internally, Arcee uses Blitz as the default writer in Conductor pipelines when the heavier Virtuoso line is not required. Users therefore get near‑70 B quality at ~⅓ the latency and price.  |  `openrouter` |
| Text/Text | *arcee-ai/caller-large* | `caller_large` | Caller Large is Arcee's specialist 'function‑calling' SLM built to orchestrate external tools and APIs. Instead of maximizing next‑token accuracy, training focuses on structured JSON outputs, parameter extraction and multi‑step tool chains, making Caller a natural choice for retrieval‑augmented generation, robotic process automation or data‑pull chatbots. It incorporates a routing head that decides when (and how) to invoke a tool versus answering directly, reducing hallucinated calls. The model is already the backbone of Arcee Conductor's auto‑tool mode, where it parses user intent, emits clean function signatures and hands control back once the tool response is ready. Developers thus gain an OpenAI‑style function‑calling UX without handing requests to a frontier‑scale model.  |  `openrouter` |
| Text/Text | *arcee-ai/coder-large* | `coder_large` | Coder‑Large is a 32 B‑parameter offspring of Qwen 2.5‑Instruct that has been further trained on permissively‑licensed GitHub, CodeSearchNet and synthetic bug‑fix corpora. It supports a 32k context window, enabling multi‑file refactoring or long diff review in a single call, and understands 30‑plus programming languages with special attention to TypeScript, Go and Terraform. Internal benchmarks show 5–8 pt gains over CodeLlama‑34 B‑Python on HumanEval and competitive BugFix scores thanks to a reinforcement pass that rewards compilable output. The model emits structured explanations alongside code blocks by default, making it suitable for educational tooling as well as production copilot scenarios. Cost‑wise, Together AI prices it well below proprietary incumbents, so teams can scale interactive coding without runaway spend.  |  `openrouter` |
| Text/Text | *arcee-ai/maestro-reasoning* | `maestro_reasoning` | Maestro Reasoning is Arcee's flagship analysis model: a 32 B‑parameter derivative of Qwen 2.5‑32 B tuned with DPO and chain‑of‑thought RL for step‑by‑step logic. Compared to the earlier 7 B preview, the production 32 B release widens the context window to 128 k tokens and doubles pass‑rate on MATH and GSM‑8K, while also lifting code completion accuracy. Its instruction style encourages structured 'thought → answer' traces that can be parsed or hidden according to user preference. That transparency pairs well with audit‑focused industries like finance or healthcare where seeing the reasoning path matters. In Arcee Conductor, Maestro is automatically selected for complex, multi‑constraint queries that smaller SLMs bounce.  |  `openrouter` |
| Text/Text | *arcee-ai/virtuoso-large* | `virtuoso_large` | Virtuoso‑Large is Arcee's top‑tier general‑purpose LLM at 72 B parameters, tuned to tackle cross‑domain reasoning, creative writing and enterprise QA. Unlike many 70 B peers, it retains the 128 k context inherited from Qwen 2.5, letting it ingest books, codebases or financial filings wholesale. Training blended DeepSeek R1 distillation, multi‑epoch supervised fine‑tuning and a final DPO/RLHF alignment stage, yielding strong performance on BIG‑Bench‑Hard, GSM‑8K and long‑context Needle‑In‑Haystack tests. Enterprises use Virtuoso‑Large as the 'fallback' brain in Conductor pipelines when other SLMs flag low confidence. Despite its size, aggressive KV‑cache optimizations keep first‑token latency in the low‑second range on 8× H100 nodes, making it a practical production‑grade powerhouse. |  `openrouter` |
| Text/Text | *arcee-ai/virtuoso-medium-v2* | `virtuoso_medium_v2` | Virtuoso‑Medium‑v2 is a 32 B model distilled from DeepSeek‑v3 logits and merged back onto a Qwen 2.5 backbone, yielding a sharper, more factual successor to the original Virtuoso Medium. The team harvested ~1.1 B logit tokens and applied 'fusion‑merging' plus DPO alignment, which pushed scores past Arcee‑Nova 2024 and many 40 B‑plus peers on MMLU‑Pro, MATH and HumanEval. With a 128 k context and aggressive quantization options (from BF16 down to 4‑bit GGUF), it balances capability with deployability on single‑GPU nodes. Typical use cases include enterprise chat assistants, technical writing aids and medium‑complexity code drafting where Virtuoso‑Large would be overkill.  |  `openrouter` |
| Text/Text | *arliai/qwq-32b-arliai-rpr-v1:free* | `qwq_32b_arliai_rpr_v1__free` | QwQ-32B-ArliAI-RpR-v1 is a 32B parameter model fine-tuned from Qwen/QwQ-32B using a curated creative writing and roleplay dataset originally developed for the RPMax series. It is designed to maintain coherence and reasoning across long multi-turn conversations by introducing explicit reasoning steps per dialogue turn, generated and refined using the base model itself. The model was trained using RS-QLORA+ on 8K sequence lengths and supports up to 128K context windows (with practical performance around 32K). It is optimized for creative roleplay and dialogue generation, with an emphasis on minimizing cross-context repetition while preserving stylistic diversity. |  `openrouter` |
| Text/Text | *cognitivecomputations/dolphin-mixtral-8x22b* | `dolphin_mixtral_8x22b` | Dolphin 2.9 is designed for instruction following, conversational, and coding. This model is a finetune of [Mixtral 8x22B Instruct](/models/mistralai/mixtral-8x22b-instruct). It features a 64k context length and was fine-tuned with a 16k sequence length using ChatML templates. This model is a successor to [Dolphin Mixtral 8x7B](/models/cognitivecomputations/dolphin-mixtral-8x7b). The model is uncensored and is stripped of alignment and bias. It requires an external alignment layer for ethical use. Users are cautioned to use this highly compliant model responsibly, as detailed in a blog post about uncensored models at [erichartford.com/uncensored-models](https://erichartford.com/uncensored-models).#moe #uncensored |  `openrouter` |
| Text/Text | *cognitivecomputations/dolphin3.0-mistral-24b:free* | `dolphin3_0_mistral_24b__free` | Dolphin 3.0 is the next generation of the Dolphin series of instruct-tuned models.  Designed to be the ultimate general purpose local model, enabling coding, math, agentic, function calling, and general use cases. Dolphin aims to be a general purpose instruct model, similar to the models behind ChatGPT, Claude, Gemini.  Part of the [Dolphin 3.0 Collection](https://huggingface.co/collections/cognitivecomputations/dolphin-30-677ab47f73d7ff66743979a3) Curated and trained by [Eric Hartford](https://huggingface.co/ehartford), [Ben Gitter](https://huggingface.co/bigstorm), [BlouseJury](https://huggingface.co/BlouseJury) and [Cognitive Computations](https://huggingface.co/cognitivecomputations) |  `openrouter` |
| Text/Text | *cognitivecomputations/dolphin3.0-r1-mistral-24b:free* | `dolphin3_0_r1_mistral_24b__free` | Dolphin 3.0 R1 is the next generation of the Dolphin series of instruct-tuned models.  Designed to be the ultimate general purpose local model, enabling coding, math, agentic, function calling, and general use cases. The R1 version has been trained for 3 epochs to reason using 800k reasoning traces from the Dolphin-R1 dataset. Dolphin aims to be a general purpose reasoning instruct model, similar to the models behind ChatGPT, Claude, Gemini. Part of the [Dolphin 3.0 Collection](https://huggingface.co/collections/cognitivecomputations/dolphin-30-677ab47f73d7ff66743979a3) Curated and trained by [Eric Hartford](https://huggingface.co/ehartford), [Ben Gitter](https://huggingface.co/bigstorm), [BlouseJury](https://huggingface.co/BlouseJury) and [Cognitive Computations](https://huggingface.co/cognitivecomputations) |  `openrouter` |
| Text/Text | *cohere/command* | `command` | Command is an instruction-following conversational model that performs language tasks with high quality, more reliably and with a longer context than our base generative models. Use of this model is subject to Cohere's [Usage Policy](https://docs.cohere.com/docs/usage-policy) and [SaaS Agreement](https://cohere.com/saas-agreement). |  `openrouter` |
| Text/Text | *cohere/command-a* | `command_a` | Command A is an open-weights 111B parameter model with a 256k context window focused on delivering great performance across agentic, multilingual, and coding use cases. Compared to other leading proprietary and open-weights models Command A delivers maximum performance with minimum hardware costs, excelling on business-critical agentic and multilingual tasks. |  `openrouter` |
| Text/Text | *cohere/command-r* | `command_r` | Command-R is a 35B parameter model that performs conversational language tasks at a higher quality, more reliably, and with a longer context than previous models. It can be used for complex workflows like code generation, retrieval augmented generation (RAG), tool use, and agents. Read the launch post [here](https://txt.cohere.com/command-r/). Use of this model is subject to Cohere's [Usage Policy](https://docs.cohere.com/docs/usage-policy) and [SaaS Agreement](https://cohere.com/saas-agreement). |  `openrouter` |
| Text/Text | *cohere/command-r-03-2024* | `command_r_03_2024` | Command-R is a 35B parameter model that performs conversational language tasks at a higher quality, more reliably, and with a longer context than previous models. It can be used for complex workflows like code generation, retrieval augmented generation (RAG), tool use, and agents. Read the launch post [here](https://txt.cohere.com/command-r/). Use of this model is subject to Cohere's [Usage Policy](https://docs.cohere.com/docs/usage-policy) and [SaaS Agreement](https://cohere.com/saas-agreement). |  `openrouter` |
| Text/Text | *cohere/command-r-08-2024* | `command_r_08_2024` | command-r-08-2024 is an update of the [Command R](/models/cohere/command-r) with improved performance for multilingual retrieval-augmented generation (RAG) and tool use. More broadly, it is better at math, code and reasoning and is competitive with the previous version of the larger Command R+ model. Read the launch post [here](https://docs.cohere.com/changelog/command-gets-refreshed). Use of this model is subject to Cohere's [Usage Policy](https://docs.cohere.com/docs/usage-policy) and [SaaS Agreement](https://cohere.com/saas-agreement). |  `openrouter` |
| Text/Text | *cohere/command-r-plus* | `command_r_plus` | Command R+ is a new, 104B-parameter LLM from Cohere. It's useful for roleplay, general consumer usecases, and Retrieval Augmented Generation (RAG). It offers multilingual support for ten key languages to facilitate global business operations. See benchmarks and the launch post [here](https://txt.cohere.com/command-r-plus-microsoft-azure/). Use of this model is subject to Cohere's [Usage Policy](https://docs.cohere.com/docs/usage-policy) and [SaaS Agreement](https://cohere.com/saas-agreement). |  `openrouter` |
| Text/Text | *cohere/command-r-plus-04-2024* | `command_r_plus_04_2024` | Command R+ is a new, 104B-parameter LLM from Cohere. It's useful for roleplay, general consumer usecases, and Retrieval Augmented Generation (RAG). It offers multilingual support for ten key languages to facilitate global business operations. See benchmarks and the launch post [here](https://txt.cohere.com/command-r-plus-microsoft-azure/). Use of this model is subject to Cohere's [Usage Policy](https://docs.cohere.com/docs/usage-policy) and [SaaS Agreement](https://cohere.com/saas-agreement). |  `openrouter` |
| Text/Text | *cohere/command-r-plus-08-2024* | `command_r_plus_08_2024` | command-r-plus-08-2024 is an update of the [Command R+](/models/cohere/command-r-plus) with roughly 50% higher throughput and 25% lower latencies as compared to the previous Command R+ version, while keeping the hardware footprint the same. Read the launch post [here](https://docs.cohere.com/changelog/command-gets-refreshed). Use of this model is subject to Cohere's [Usage Policy](https://docs.cohere.com/docs/usage-policy) and [SaaS Agreement](https://cohere.com/saas-agreement). |  `openrouter` |
| Text/Text | *cohere/command-r7b-12-2024* | `command_r7b_12_2024` | Command R7B (12-2024) is a small, fast update of the Command R+ model, delivered in December 2024. It excels at RAG, tool use, agents, and similar tasks requiring complex reasoning and multiple steps. Use of this model is subject to Cohere's [Usage Policy](https://docs.cohere.com/docs/usage-policy) and [SaaS Agreement](https://cohere.com/saas-agreement). |  `openrouter` |
| Text/Text | *deepseek/deepseek-chat* | `deepseek_chat` | DeepSeek-V3 is the latest model from the DeepSeek team, building upon the instruction following and coding abilities of the previous versions. Pre-trained on nearly 15 trillion tokens, the reported evaluations reveal that the model outperforms other open-source models and rivals leading closed-source models. For model details, please visit [the DeepSeek-V3 repo](https://github.com/deepseek-ai/DeepSeek-V3) for more information, or see the [launch announcement](https://api-docs.deepseek.com/news/news1226). |  `openrouter` |
| Text/Text | *deepseek/deepseek-chat-v3-0324* | `deepseek_chat_v3_0324` | DeepSeek V3, a 685B-parameter, mixture-of-experts model, is the latest iteration of the flagship chat model family from the DeepSeek team. It succeeds the [DeepSeek V3](/deepseek/deepseek-chat-v3) model and performs really well on a variety of tasks. |  `openrouter` |
| Text/Text | *deepseek/deepseek-chat-v3-0324:free* | `deepseek_chat_v3_0324__free` | DeepSeek V3, a 685B-parameter, mixture-of-experts model, is the latest iteration of the flagship chat model family from the DeepSeek team. It succeeds the [DeepSeek V3](/deepseek/deepseek-chat-v3) model and performs really well on a variety of tasks. |  `openrouter` |
| Text/Text | *deepseek/deepseek-chat:free* | `deepseek_chat__free` | DeepSeek-V3 is the latest model from the DeepSeek team, building upon the instruction following and coding abilities of the previous versions. Pre-trained on nearly 15 trillion tokens, the reported evaluations reveal that the model outperforms other open-source models and rivals leading closed-source models. For model details, please visit [the DeepSeek-V3 repo](https://github.com/deepseek-ai/DeepSeek-V3) for more information, or see the [launch announcement](https://api-docs.deepseek.com/news/news1226). |  `openrouter` |
| Text/Text | *deepseek/deepseek-coder* | `deepseek_coder` | DeepSeek-Coder-V2, an open-source Mixture-of-Experts (MoE) code language model. It is further pre-trained from an intermediate checkpoint of DeepSeek-V2 with additional 6 trillion tokens. The original V1 model was trained from scratch on 2T tokens, with a composition of 87% code and 13% natural language in both English and Chinese. It was pre-trained on project-level code corpus by employing a extra fill-in-the-blank task. |  `openrouter` |
| Text/Text | *deepseek/deepseek-prover-v2* | `deepseek_prover_v2` | DeepSeek Prover V2 is a 671B parameter model, speculated to be geared towards logic and mathematics. Likely an upgrade from [DeepSeek-Prover-V1.5](https://huggingface.co/deepseek-ai/DeepSeek-Prover-V1.5-RL) Not much is known about the model yet, as DeepSeek released it on Hugging Face without an announcement or description. |  `openrouter` |
| Text/Text | *deepseek/deepseek-prover-v2:free* | `deepseek_prover_v2__free` | DeepSeek Prover V2 is a 671B parameter model, speculated to be geared towards logic and mathematics. Likely an upgrade from [DeepSeek-Prover-V1.5](https://huggingface.co/deepseek-ai/DeepSeek-Prover-V1.5-RL) Not much is known about the model yet, as DeepSeek released it on Hugging Face without an announcement or description. |  `openrouter` |
| Text/Text | *deepseek/deepseek-r1* | `deepseek_r1` | DeepSeek R1 is here: Performance on par with [OpenAI o1](/openai/o1), but open-sourced and with fully open reasoning tokens. It's 671B parameters in size, with 37B active in an inference pass. Fully open-source model & [technical report](https://api-docs.deepseek.com/news/news250120). MIT licensed: Distill & commercialize freely! |  `openrouter` |
| Text/Text | *deepseek/deepseek-r1-distill-llama-70b* | `deepseek_r1_distill_llama_70b` | DeepSeek R1 Distill Llama 70B is a distilled large language model based on [Llama-3.3-70B-Instruct](/meta-llama/llama-3.3-70b-instruct), using outputs from [DeepSeek R1](/deepseek/deepseek-r1). The model combines advanced distillation techniques to achieve high performance across multiple benchmarks, including:- AIME 2024 pass@1: 70.0- MATH-500 pass@1: 94.5- CodeForces Rating: 1633 The model leverages fine-tuning from DeepSeek R1's outputs, enabling competitive performance comparable to larger frontier models. |  `openrouter` |
| Text/Text | *deepseek/deepseek-r1-distill-llama-70b:free* | `deepseek_r1_distill_llama_70b__free` | DeepSeek R1 Distill Llama 70B is a distilled large language model based on [Llama-3.3-70B-Instruct](/meta-llama/llama-3.3-70b-instruct), using outputs from [DeepSeek R1](/deepseek/deepseek-r1). The model combines advanced distillation techniques to achieve high performance across multiple benchmarks, including:- AIME 2024 pass@1: 70.0- MATH-500 pass@1: 94.5- CodeForces Rating: 1633 The model leverages fine-tuning from DeepSeek R1's outputs, enabling competitive performance comparable to larger frontier models. |  `openrouter` |
| Text/Text | *deepseek/deepseek-r1-distill-llama-8b* | `deepseek_r1_distill_llama_8b` | DeepSeek R1 Distill Llama 8B is a distilled large language model based on [Llama-3.1-8B-Instruct](/meta-llama/llama-3.1-8b-instruct), using outputs from [DeepSeek R1](/deepseek/deepseek-r1). The model combines advanced distillation techniques to achieve high performance across multiple benchmarks, including:- AIME 2024 pass@1: 50.4- MATH-500 pass@1: 89.1- CodeForces Rating: 1205 The model leverages fine-tuning from DeepSeek R1's outputs, enabling competitive performance comparable to larger frontier models. Hugging Face: - [Llama-3.1-8B](https://huggingface.co/meta-llama/Llama-3.1-8B) - [DeepSeek-R1-Distill-Llama-8B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-8B)   | |  `openrouter` |
| Text/Text | *deepseek/deepseek-r1-distill-qwen-1.5b* | `deepseek_r1_distill_qwen_1_5b` | DeepSeek R1 Distill Qwen 1.5B is a distilled large language model based on  [Qwen 2.5 Math 1.5B](https://huggingface.co/Qwen/Qwen2.5-Math-1.5B), using outputs from [DeepSeek R1](/deepseek/deepseek-r1). It's a very small and efficient model which outperforms [GPT 4o 0513](/openai/gpt-4o-2024-05-13) on Math Benchmarks. Other benchmark results include:- AIME 2024 pass@1: 28.9- AIME 2024 cons@64: 52.7- MATH-500 pass@1: 83.9 The model leverages fine-tuning from DeepSeek R1's outputs, enabling competitive performance comparable to larger frontier models. |  `openrouter` |
| Text/Text | *deepseek/deepseek-r1-distill-qwen-14b* | `deepseek_r1_distill_qwen_14b` | DeepSeek R1 Distill Qwen 14B is a distilled large language model based on [Qwen 2.5 14B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B), using outputs from [DeepSeek R1](/deepseek/deepseek-r1). It outperforms OpenAI's o1-mini across various benchmarks, achieving new state-of-the-art results for dense models. Other benchmark results include:- AIME 2024 pass@1: 69.7- MATH-500 pass@1: 93.9- CodeForces Rating: 1481 The model leverages fine-tuning from DeepSeek R1's outputs, enabling competitive performance comparable to larger frontier models. |  `openrouter` |
| Text/Text | *deepseek/deepseek-r1-distill-qwen-14b:free* | `deepseek_r1_distill_qwen_14b__free` | DeepSeek R1 Distill Qwen 14B is a distilled large language model based on [Qwen 2.5 14B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-14B), using outputs from [DeepSeek R1](/deepseek/deepseek-r1). It outperforms OpenAI's o1-mini across various benchmarks, achieving new state-of-the-art results for dense models. Other benchmark results include:- AIME 2024 pass@1: 69.7- MATH-500 pass@1: 93.9- CodeForces Rating: 1481 The model leverages fine-tuning from DeepSeek R1's outputs, enabling competitive performance comparable to larger frontier models. |  `openrouter` |
| Text/Text | *deepseek/deepseek-r1-distill-qwen-32b* | `deepseek_r1_distill_qwen_32b` | DeepSeek R1 Distill Qwen 32B is a distilled large language model based on [Qwen 2.5 32B](https://huggingface.co/Qwen/Qwen2.5-32B), using outputs from [DeepSeek R1](/deepseek/deepseek-r1). It outperforms OpenAI's o1-mini across various benchmarks, achieving new state-of-the-art results for dense models. Other benchmark results include:- AIME 2024 pass@1: 72.6- MATH-500 pass@1: 94.3- CodeForces Rating: 1691 The model leverages fine-tuning from DeepSeek R1's outputs, enabling competitive performance comparable to larger frontier models. |  `openrouter` |
| Text/Text | *deepseek/deepseek-r1-distill-qwen-32b:free* | `deepseek_r1_distill_qwen_32b__free` | DeepSeek R1 Distill Qwen 32B is a distilled large language model based on [Qwen 2.5 32B](https://huggingface.co/Qwen/Qwen2.5-32B), using outputs from [DeepSeek R1](/deepseek/deepseek-r1). It outperforms OpenAI's o1-mini across various benchmarks, achieving new state-of-the-art results for dense models. Other benchmark results include:- AIME 2024 pass@1: 72.6- MATH-500 pass@1: 94.3- CodeForces Rating: 1691 The model leverages fine-tuning from DeepSeek R1's outputs, enabling competitive performance comparable to larger frontier models. |  `openrouter` |
| Text/Text | *deepseek/deepseek-r1-zero:free* | `deepseek_r1_zero__free` | DeepSeek-R1-Zero is a model trained via large-scale reinforcement learning (RL) without supervised fine-tuning (SFT) as a preliminary step. It's 671B parameters in size, with 37B active in an inference pass. It demonstrates remarkable performance on reasoning. With RL, DeepSeek-R1-Zero naturally emerged with numerous powerful and interesting reasoning behaviors. DeepSeek-R1-Zero encounters challenges such as endless repetition, poor readability, and language mixing. See [DeepSeek R1](/deepseek/deepseek-r1) for the SFT model. |  `openrouter` |
| Text/Text | *deepseek/deepseek-r1:free* | `deepseek_r1__free` | DeepSeek R1 is here: Performance on par with [OpenAI o1](/openai/o1), but open-sourced and with fully open reasoning tokens. It's 671B parameters in size, with 37B active in an inference pass. Fully open-source model & [technical report](https://api-docs.deepseek.com/news/news250120). MIT licensed: Distill & commercialize freely! |  `openrouter` |
| Text/Text | *deepseek/deepseek-v3-base:free* | `deepseek_v3_base__free` | Note that this is a base model mostly meant for testing, you need to provide detailed prompts for the model to return useful responses.  DeepSeek-V3 Base is a 671B parameter open Mixture-of-Experts (MoE) language model with 37B active parameters per forward pass and a context length of 128K tokens. Trained on 14.8T tokens using FP8 mixed precision, it achieves high training efficiency and stability, with strong performance across language, reasoning, math, and coding tasks.  DeepSeek-V3 Base is the pre-trained model behind [DeepSeek V3](/deepseek/deepseek-chat-v3) |  `openrouter` |
| Text/Text | *eleutherai/llemma_7b* | `llemma_7b` | Llemma 7B is a language model for mathematics. It was initialized with Code Llama 7B weights, and trained on the Proof-Pile-2 for 200B tokens. Llemma models are particularly strong at chain-of-thought mathematical reasoning and using computational tools for mathematics, such as Python and formal theorem provers. |  `openrouter` |
| Text/Text | *eva-unit-01/eva-llama-3.33-70b* | `eva_llama_3_33_70b` | EVA Llama 3.33 70b is a roleplay and storywriting specialist model. It is a full-parameter finetune of [Llama-3.3-70B-Instruct](https://openrouter.ai/meta-llama/llama-3.3-70b-instruct) on mixture of synthetic and natural data. It uses Celeste 70B 0.1 data mixture, greatly expanding it to improve versatility, creativity and 'flavor' of the resulting model This model was built with Llama by Meta. |  `openrouter` |
| Text/Text | *eva-unit-01/eva-qwen-2.5-32b* | `eva_qwen_2_5_32b` | EVA Qwen2.5 32B is a roleplaying/storywriting specialist model. It's a full-parameter finetune of Qwen2.5-32B on mixture of synthetic and natural data. It uses Celeste 70B 0.1 data mixture, greatly expanding it to improve versatility, creativity and 'flavor' of the resulting model. |  `openrouter` |
| Text/Text | *eva-unit-01/eva-qwen-2.5-72b* | `eva_qwen_2_5_72b` | EVA Qwen2.5 72B is a roleplay and storywriting specialist model. It's a full-parameter finetune of Qwen2.5-72B on mixture of synthetic and natural data. It uses Celeste 70B 0.1 data mixture, greatly expanding it to improve versatility, creativity and 'flavor' of the resulting model. |  `openrouter` |
| Text/Text | *featherless/qwerky-72b:free* | `qwerky_72b__free` | Qwerky-72B is a linear-attention RWKV variant of the Qwen 2.5 72B model, optimized to significantly reduce computational cost at scale. Leveraging linear attention, it achieves substantial inference speedups (>1000x) while retaining competitive accuracy on common benchmarks like ARC, HellaSwag, Lambada, and MMLU. It inherits knowledge and language support from Qwen 2.5, supporting approximately 30 languages, making it suitable for efficient inference in large-context applications. |  `openrouter` |
| Text/Text | *google/gemini-2.0-flash-001* | `gemini_2_0_flash_001` | Gemini Flash 2.0 offers a significantly faster time to first token (TTFT) compared to [Gemini Flash 1.5](/google/gemini-flash-1.5), while maintaining quality on par with larger models like [Gemini Pro 1.5](/google/gemini-pro-1.5). It introduces notable enhancements in multimodal understanding, coding capabilities, complex instruction following, and function calling. These advancements come together to deliver more seamless and robust agentic experiences. |  `openrouter` |
| Text/Text | *google/gemini-2.0-flash-exp:free* | `gemini_2_0_flash_exp__free` | Gemini Flash 2.0 offers a significantly faster time to first token (TTFT) compared to [Gemini Flash 1.5](/google/gemini-flash-1.5), while maintaining quality on par with larger models like [Gemini Pro 1.5](/google/gemini-pro-1.5). It introduces notable enhancements in multimodal understanding, coding capabilities, complex instruction following, and function calling. These advancements come together to deliver more seamless and robust agentic experiences. |  `openrouter` |
| Text/Text | *google/gemini-2.0-flash-lite-001* | `gemini_2_0_flash_lite_001` | Gemini 2.0 Flash Lite offers a significantly faster time to first token (TTFT) compared to [Gemini Flash 1.5](/google/gemini-flash-1.5), while maintaining quality on par with larger models like [Gemini Pro 1.5](/google/gemini-pro-1.5), all at extremely economical token prices. |  `openrouter` |
| Text/Text | *google/gemini-2.5-flash-preview* | `gemini_2_5_flash_preview` | Gemini 2.5 Flash is Google's state-of-the-art workhorse model, specifically designed for advanced reasoning, coding, mathematics, and scientific tasks. It includes built-in 'thinking' capabilities, enabling it to provide responses with greater accuracy and nuanced context handling.  Note: This model is available in two variants: thinking and non-thinking. The output pricing varies significantly depending on whether the thinking capability is active. If you select the standard variant (without the ':thinking' suffix), the model will explicitly avoid generating thinking tokens.  To utilize the thinking capability and receive thinking tokens, you must choose the ':thinking' variant, which will then incur the higher thinking-output pricing.  Additionally, Gemini 2.5 Flash is configurable through the 'max tokens for reasoning' parameter, as described in the documentation (https://openrouter.ai/docs/use-cases/reasoning-tokens#max-tokens-for-reasoning). |  `openrouter` |
| Text/Text | *google/gemini-2.5-flash-preview:thinking* | `gemini_2_5_flash_preview__thinking` | Gemini 2.5 Flash is Google's state-of-the-art workhorse model, specifically designed for advanced reasoning, coding, mathematics, and scientific tasks. It includes built-in 'thinking' capabilities, enabling it to provide responses with greater accuracy and nuanced context handling.  Note: This model is available in two variants: thinking and non-thinking. The output pricing varies significantly depending on whether the thinking capability is active. If you select the standard variant (without the ':thinking' suffix), the model will explicitly avoid generating thinking tokens.  To utilize the thinking capability and receive thinking tokens, you must choose the ':thinking' variant, which will then incur the higher thinking-output pricing.  Additionally, Gemini 2.5 Flash is configurable through the 'max tokens for reasoning' parameter, as described in the documentation (https://openrouter.ai/docs/use-cases/reasoning-tokens#max-tokens-for-reasoning). |  `openrouter` |
| Text/Text | *google/gemini-2.5-pro-exp-03-25* | `gemini_2_5_pro_exp_03_25` | Gemini 2.5 Pro is Google's state-of-the-art AI model designed for advanced reasoning, coding, mathematics, and scientific tasks. It employs 'thinking' capabilities, enabling it to reason through responses with enhanced accuracy and nuanced context handling. Gemini 2.5 Pro achieves top-tier performance on multiple benchmarks, including first-place positioning on the LMArena leaderboard, reflecting superior human-preference alignment and complex problem-solving abilities. |  `openrouter` |
| Text/Text | *google/gemini-2.5-pro-preview* | `gemini_2_5_pro_preview` | Gemini 2.5 Pro is Google's state-of-the-art AI model designed for advanced reasoning, coding, mathematics, and scientific tasks. It employs 'thinking' capabilities, enabling it to reason through responses with enhanced accuracy and nuanced context handling. Gemini 2.5 Pro achieves top-tier performance on multiple benchmarks, including first-place positioning on the LMArena leaderboard, reflecting superior human-preference alignment and complex problem-solving abilities. |  `openrouter` |
| Text/Text | *google/gemini-flash-1.5* | `gemini_flash_1_5` | Gemini 1.5 Flash is a foundation model that performs well at a variety of multimodal tasks such as visual understanding, classification, summarization, and creating content from image, audio and video. It's adept at processing visual and text inputs such as photographs, documents, infographics, and screenshots. Gemini 1.5 Flash is designed for high-volume, high-frequency tasks where cost and latency matter. On most common tasks, Flash achieves comparable quality to other Gemini Pro models at a significantly reduced cost. Flash is well-suited for applications like chat assistants and on-demand content generation where speed and scale matter. Usage of Gemini is subject to Google's [Gemini Terms of Use](https://ai.google.dev/terms).#multimodal |  `openrouter` |
| Text/Text | *google/gemini-flash-1.5-8b* | `gemini_flash_1_5_8b` | Gemini Flash 1.5 8B is optimized for speed and efficiency, offering enhanced performance in small prompt tasks like chat, transcription, and translation. With reduced latency, it is highly effective for real-time and large-scale operations. This model focuses on cost-effective solutions while maintaining high-quality results.[Click here to learn more about this model](https://developers.googleblog.com/en/gemini-15-flash-8b-is-now-generally-available-for-use/). Usage of Gemini is subject to Google's [Gemini Terms of Use](https://ai.google.dev/terms). |  `openrouter` |
| Text/Text | *google/gemini-pro-1.5* | `gemini_pro_1_5` | Google's latest multimodal model, supports image and video[0] in text or chat prompts. Optimized for language tasks including:- Code generation- Text generation- Text editing- Problem solving- Recommendations- Information extraction- Data extraction or generation- AI agents Usage of Gemini is subject to Google's [Gemini Terms of Use](https://ai.google.dev/terms).* [0]: Video input is not available through OpenRouter at this time. |  `openrouter` |
| Text/Text | *google/gemma-2-27b-it* | `gemma_2_27b_it` | Gemma 2 27B by Google is an open model built from the same research and technology used to create the [Gemini models](/models?q=gemini). Gemma models are well-suited for a variety of text generation tasks, including question answering, summarization, and reasoning. See the [launch announcement](https://blog.google/technology/developers/google-gemma-2/) for more details. Usage of Gemma is subject to Google's [Gemma Terms of Use](https://ai.google.dev/gemma/terms). |  `openrouter` |
| Text/Text | *google/gemma-2-9b-it* | `gemma_2_9b_it` | Gemma 2 9B by Google is an advanced, open-source language model that sets a new standard for efficiency and performance in its size class. Designed for a wide variety of tasks, it empowers developers and researchers to build innovative applications, while maintaining accessibility, safety, and cost-effectiveness. See the [launch announcement](https://blog.google/technology/developers/google-gemma-2/) for more details. Usage of Gemma is subject to Google's [Gemma Terms of Use](https://ai.google.dev/gemma/terms). |  `openrouter` |
| Text/Text | *google/gemma-2-9b-it:free* | `gemma_2_9b_it__free` | Gemma 2 9B by Google is an advanced, open-source