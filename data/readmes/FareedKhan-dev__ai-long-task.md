# An AI-Native System for Solving Long-Horizon Tasks

<div align="center">

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Follow on Medium](https://img.shields.io/badge/Read%20the%20Blog-Medium-black?logo=medium)](https://medium.com/@fareedkhandev/e48b8b39cc9e)

**An open-source implementation of AlphaEvolve-inspired architecture for tackling complex, multi-day engineering and scientific discovery tasks with an AI-native engineering team.**

</div>

---

## Table of Contents

- [Introduction: Beyond Single-Prompt Agents](#introduction-beyond-single-prompt-agents)
- [Core Philosophy: An Algorithmic Approach to AI Engineering](#core-philosophy-an-algorithmic-approach-to-ai-engineering)
- [Key Features](#key-features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
  - [Command-Line Interface (CLI)](#command-line-interface-cli)
  - [Using LongHorizon as a Library (API)](#using-longhorizon-as-a-library-api)
- [Configuration Deep Dive](#configuration-deep-dive)
- [Architectural Concepts Explained](#architectural-concepts-explained)
  - [The Compute Layer: Resilient LLM Ensembles](#the-compute-layer-resilient-llm-ensembles)
  - [Evolutionary Memory: MAP-Elites & Island Models](#evolutionary-memory-map-elites--island-models)
  - [Multi-Stage Evaluation Pipeline](#multi-stage-evaluation-pipeline)
  - [Research Layer: Autonomous SOTA Hunting](#research-layer-autonomous-sota-hunting)
  - [Prompt Engineering as Infrastructure](#prompt-engineering-as-infrastructure)
- [How to Contribute](#how-to-contribute)

## Introduction: Beyond Single-Prompt Agents

State-of-the-art AI models can maintain reasoning chains for hours, but achieving reliable, multi-day performance on complex engineering tasks requires a systems approach. LongHorizon is an AI-native framework designed to solve this exact class of **long-horizon tasks** problems that require sustained, iterative optimization over hours or even days.

Inspired by Google's AlphaEvolve, LongHorizon treats AI-driven development as an evolutionary simulation, creating a "team" of AI agents that collaborate, compete, and evolve solutions over time. This is not about better prompting; it's an algorithmic engine for automated engineering.

![LongHorizon Architecture](https://miro.medium.com/v2/resize:fit:3100/format:webp/1*EHB79ltAiPOWdCPUgEwcHQ.png)

## Core Philosophy: An Algorithmic Approach to AI Engineering

At its core, LongHorizon is built on the principle that agents capable of long-term reasoning require an algorithmic-based approach. This includes:

-   **MAP-Elites**: To explore and preserve a diverse archive of high-quality solutions, avoiding premature convergence on a single "good enough" answer.
-   **Island Model Evolution**: To run parallel, isolated populations with controlled migration, enhancing exploration and preventing catastrophic forgetting.
-   **Multi-Stage Evaluation**: To intelligently filter solutions using a cascade of tests, performance profiling, visual inspection, and LLM-based judging, saving vast amounts of compute.
-   **Stateful Memory & Artifacts**: To persist execution traces, logs, and learned behaviors across long runs, enabling checkpointing and deep analysis.
-   **Autonomous Research**: To empower agents to browse the web, read documentation, and incorporate state-of-the-art knowledge *before* starting the evolution.

## Key Features

-   **Multi-Model LLM Ensembles**: Mix cheap/fast and expensive/powerful models with weighted sampling to optimize cost and performance.
-   **Island-Based Evolution**: Maintain genetic diversity by evolving multiple populations in parallel.
-   **MAP-Elites for Diversity**: Preserves not just the "best" solution, but the best solution for different niches (e.g., "fastest," "most concise," "most novel").
-   **Cascade Evaluation**: Fails fast on bad solutions with a multi-stage evaluation pipeline, saving compute.
-   **Visual QA with Computer Use**: Empowers agents to "see" and evaluate GUIs, plots, and other visual outputs.
-   **Autonomous Web Research**: An integrated "SOTA Hunter" agent browses the web to find cutting-edge solutions before evolution begins.
-   **Diff-Based Evolution**: Radically reduces token cost and improves precision by evolving code via `SEARCH/REPLACE` blocks instead of full rewrites.
-   **Stateful & Resumable**: Checkpointing system allows you to stop and resume multi-day runs without losing progress.
-   **Comprehensive Tracing**: Logs every evolutionary step (parent, child, prompt, metrics) to a JSONL file for analysis and reinforcement learning.
-   **Containerized & Deployable**: Comes with a `Dockerfile` for easy deployment on local machines or cloud clusters.

## Project Structure

The project is organized into modular components, each with a clear responsibility, enabling scalability and maintainability.

```
longhorizon/
├── api.py                          # Public API for using LongHorizon as a library
├── cli.py                          # Command-line interface
├── config.py                       # Configuration data classes and loader
├── Dockerfile                      # Docker definition for containerized deployment
├── longhorizon-run.py              # Main executable script
├── pyproject.toml                  # Project dependencies and metadata
│
├── configs/
│   └── default_config.yaml         # Baseline configuration template
│
├── core/
│   ├── controller.py               # Orchestrates the main evolutionary loop
│   ├── researcher.py               # Autonomous web research agent (SOTA Hunter)
│   └── iteration.py                # Logic for a single evolutionary step
│
├── data/
│   ├── database.py                 # Implements evolutionary memory (MAP-Elites, Islands)
│   └── evolution_trace.py          # Logs evolutionary steps for analysis and RL
│
├── evaluation/
│   ├── evaluator.py                # Main evaluation runner with cascade logic
│   ├── visual_evaluator.py         # Visual QA using multimodal models
│   └── novelty_judge.py            # LLM-based diversity/novelty assessment
│
├── llm/
│   ├── base.py                     # Abstract LLMInterface for provider-agnostic calls
│   ├── ensemble.py                 # Manages multi-model weighted sampling
│   └── openai.py                   # OpenAI/Azure/Groq/etc. compatible client
│
├── prompts/
│   └── defaults/                   # Built-in default prompt templates and fragments
│
└── utils/
    ├── async_utils.py              # Concurrency tools like TaskPool and retry logic
    └── code_utils.py               # Helpers for parsing diffs and code blocks
```

## Getting Started

### Prerequisites

-   Python 3.10+
-   Git
-   An API key for an OpenAI-compatible LLM provider (e.g., OpenAI, Gemini, Groq, Together).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/FareedKhan-dev/ai-long-task.git
    cd ai-long-task
    ```

2.  **Install the package in editable mode:**
    This will install all required dependencies from `pyproject.toml`.
    ```bash
    pip install -e .
    ```

3.  **(Optional for Dev)** Install development dependencies for testing and linting:
    ```bash
    pip install -e ".[dev]"
    ```

### Configuration

1.  **Set up Environment Variables:**
    LongHorizon securely loads API keys from environment variables. Create a `.env` file in the root directory:
    ```env
    # For OpenAI models
    OPENAI_API_KEY="sk-..."

    # For Gemini models (via Google AI Studio's OpenAI-compatible endpoint)
    GEMINI_API_KEY="..."

    # For separate embedding models (optional)
    OPENAI_EMBEDDING_API_KEY="sk-..."
    ```
    The application will automatically load these variables.

2.  **Customize the Configuration (Optional):**
    Copy the default configuration file to create your own experimental setup.
    ```bash
    cp longhorizon/configs/default_config.yaml my_experiment_config.yaml
    ```
    Now, you can edit `my_experiment_config.yaml` to change models, evolutionary parameters, and more.

## Usage

LongHorizon can be used both as a command-line tool for running full experiments and as a Python library for integration into other projects.

### Command-Line Interface (CLI)

The CLI is the primary way to run an evolutionary experiment.

**Basic Syntax:**
```bash
longhorizon-run <initial_program> <evaluation_file> [options]
```

**Example: Optimizing a GPU Kernel (from the blog post)**

Let's run the MLX kernel optimization example. The necessary files are already in the repository.

```bash
longhorizon-run \
    examples/mlx_problem/initial_program.py \
    examples/mlx_problem/evaluator.py \
    --config examples/mlx_problem/config.yaml \
    --output mlx_optimization_run
```

-   `initial_program.py`: The baseline, unoptimized GQA implementation.
-   `evaluator.py`: The "bulletproof" evaluator that benchmarks speed and correctness.
-   `--config config.yaml`: Specifies the evolutionary strategy (models, prompts, etc.).
-   `--output mlx_optimization_run`: The directory where all results, checkpoints, and logs will be saved.

**Resuming from a Checkpoint:**

If your run is interrupted, you can resume it from the last checkpoint:
```bash
longhorizon-run \
    examples/mlx_problem/initial_program.py \
    examples/mlx_problem/evaluator.py \
    --config examples/mlx_problem/config.yaml \
    --output mlx_optimization_run \
    --checkpoint mlx_optimization_run/checkpoints/checkpoint_100
```

### Using LongHorizon as a Library (API)

You can easily integrate LongHorizon's evolutionary engine into your own Python code using the high-level API in `longhorizon.api`.

**Example 1: General-purpose code evolution**

```python
from longhorizon.api import evolve_code, EvolutionResult

# 1. Define your initial code
initial_code = """
def slow_sort(arr):
    # EVOLVE-BLOCK-START
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
    # EVOLVE-BLOCK-END
"""

# 2. Define your evaluator function
def sorting_evaluator(program_path: str):
    # This function will be executed in a separate process
    import importlib.util
    import random
    
    # Load the evolved module
    spec = importlib.util.spec_from_file_location("evolved_module", program_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    # Test with random data
    test_data = [random.randint(0, 1000) for _ in range(100)]
    expected = sorted(test_data.copy())
    
    try:
        result = module.slow_sort(test_data.copy())
        correctness = 1.0 if result == expected else 0.0
    except Exception:
        correctness = 0.0
        
    return {"score": correctness}

# 3. Run the evolution!
result: EvolutionResult = evolve_code(
    initial_code=initial_code,
    evaluator=sorting_evaluator,
    iterations=50
)

print(f"Evolution complete! Best score: {result.best_score}")
print("--- Best Code ---")
print(result.best_code)
```

**Example 2: Evolving a specific function with test cases**

```python
from longhorizon.api import evolve_function

# The function we want to optimize
def add(a, b):
    return a + b

# A set of test cases to guide evolution
test_cases = [
    ((2, 3), 5),
    ((-1, 1), 0),
    ((100, 200), 300)
]

# Evolve the function
result = evolve_function(
    func=add,
    test_cases=test_cases,
    iterations=100
)

print(f"Best score (test pass rate): {result.best_score}")
print("--- Evolved Function ---")
print(result.best_code)
```

## Configuration Deep Dive

The behavior of LongHorizon is controlled by a single YAML file. The `longhorizon/configs/default_config.yaml` file is heavily commented and serves as the best reference. Here are the key sections:

-   **`llm`**: Configures the LLM ensembles.
    -   `models`: A list of models for code generation. Each has a `name` and `weight`.
    -   `evaluator_models`: A separate list of models for LLM-as-a-Judge.
    -   `api_base` / `api_key`: Can be set here or resolved from `${ENV_VAR}`.
    -   `temperature`, `timeout`, `retries`: Default generation parameters.

-   **`database`**: Controls the evolutionary memory and strategy.
    -   `population_size`: Total number of programs to keep.
    -   `num_islands`: Number of parallel populations to evolve.
    -   `migration_interval`: How often (in generations) to share best solutions between islands.
    -   `feature_dimensions`: Defines the axes for the MAP-Elites grid (e.g., `["complexity", "diversity"]`).

-   **`evaluator`**: Configures the evaluation pipeline.
    -   `timeout`: Max time in seconds for a single evaluation to run.
    -   `parallel_evaluations`: How many programs to evaluate concurrently.
    -   `cascade_evaluation`: Set to `true` to enable multi-stage evaluation.
    -   `cascade_thresholds`: A list of scores a program must achieve to proceed to the next stage.

-   **`browser_use` / `computer_use`**: Enable the advanced research and visual QA agents.
    -   `enabled`: Set to `true` to activate these capabilities.
    -   `model`: The multimodal model to use (e.g., `gpt-4o`).

## Architectural Concepts Explained

### The Compute Layer: Resilient LLM Ensembles

The `llm/` module provides a resilient, provider-agnostic interface for interacting with language models.

-   **`llm.base.LLMInterface`**: An abstract base class that defines the contract for all LLM clients, ensuring our core logic doesn't depend on a specific provider.
-   **`llm.openai.OpenAILLM`**: A concrete implementation for any OpenAI-compatible API. It handles timeouts, retries, and special parameter handling for different model types (e.g., reasoning models like `o1`).
-   **`llm.ensemble.LLMEnsemble`**: The core of the compute layer. It takes a list of model configurations and performs weighted random sampling for each generation request. This allows you to balance cost and capability, using cheaper models for exploration and expensive models for targeted refinement.

### Evolutionary Memory: MAP-Elites & Island Models

The `data/database.py` module is the heart of the evolutionary engine. It's not just a database; it's the environment where solutions live, compete, and reproduce.

-   **Island Model**: The `islands` attribute partitions the population into isolated sets. The main controller rotates through these islands, evolving them independently. The `migrate_programs` method periodically shares the best individuals between islands, cross-pollinating ideas and preventing monocultures.
-   **MAP-Elites**: Instead of just tracking the single best program, we maintain a feature map (`island_feature_maps`). Each program is mapped to a cell in a grid based on its features (e.g., `code_length`, `diversity_score`). We only keep the highest-scoring program *for each cell*. This preserves interesting but currently lower-scoring solutions that might be valuable evolutionary stepping stones.

### Multi-Stage Evaluation Pipeline

The `evaluation/evaluator.py` module is the system's "fitness function." It's designed to be efficient and multi-modal.

-   **Cascade Evaluation**: The `_cascade_evaluate` method implements a funnel. It runs a cheap `evaluate_stage1` function first. Only if the score passes a configured threshold does it proceed to the more expensive `evaluate_stage2`, and so on. This saves enormous amounts of compute by discarding bad solutions early.
-   **LLM-as-a-Judge**: `_llm_evaluate` uses a separate LLM ensemble to grade code on qualitative metrics like readability and maintainability. This ensures the final solution is not just correct but also well-engineered.
-   **Visual QA**: `visual_evaluator.py` integrates multimodal models to "look at" and grade visual outputs like UIs and plots, enabling evolution on a whole new class of problems.

### Research Layer: Autonomous SOTA Hunting

The `core/researcher.py` module gives LongHorizon the ability to learn before it acts.

-   The `ResearchAgent` uses the `browser-use` library to control a headless browser.
-   Before starting an evolution, the controller can ask an LLM to formulate a research query based on the initial code.
-   The `ResearchAgent` then executes this query, browsing GitHub and arXiv to find state-of-the-art information.
-   This summarized knowledge is injected into the system prompt, priming the evolutionary process with cutting-edge information that may not have been in the LLM's training data.

### Prompt Engineering as Infrastructure

The `prompts/` directory treats prompts as a core part of the infrastructure, not just static text.

-   **`prompts.templates.TemplateManager`**: Loads `.txt` and `.json` files from disk, allowing prompts to be edited without changing Python code.
-   **`prompts.sampler.PromptSampler`**: Dynamically assembles the final prompt for each generation. It injects:
    -   **Metrics & Feedback**: How the previous attempt performed.
    -   **Evolution History**: Snippets of past failures and top-performing solutions.
    -   **Inspirations**: Diverse solutions from other islands to spark creativity.
    -   **Artifacts**: Error messages or tracebacks from the last run, so the LLM can debug itself.

## How to Contribute

Contributions are welcome! Whether it's improving the core algorithms, adding support for new LLM providers, or fixing bugs, your help is appreciated.

1.  **Fork the repository.**
2.  **Create a new branch** for your feature or bug fix.
3.  **Make your changes** and ensure the existing tests pass.
4.  **Submit a pull request** with a clear description of your changes.

Please open an issue first to discuss any major architectural changes.