# ⚡ AutoAdapt

[![arXiv](https://img.shields.io/badge/arXiv-2603.08181-b31b1b.svg)](https://arxiv.org/abs/2603.08181)

This is the official implementation of AutoAdapt: An Automated Domain Adaptation Framework for Large Language Models

Large language models (LLMs) excel in open domains but struggle in specialized settings with limited data and evolving knowledge. Existing domain adaptation practices rely heavily on manual trial-and-error processes, incur significant hyperparameter complexity, and are highly sensitive to data and user preferences, all under the high cost of LLM training. Moreover, the interactions and transferability of hyperparameter choices across domains remain poorly understood, making adaptation gains uncertain even with substantial effort. To solve these challenges, we present AutoAdapt, a novel end-to-end automated framework for efficient and reliable LLM domain adaptation. AutoAdapt leverages curated knowledge bases from literature and open-source resources to reduce expert intervention. To narrow the search space, we design a novel multi-agent debating system in which proposal and critic agents iteratively interact to align user intent and incorporate data signals and best practices into the planning process. To optimize hyperparameters under tight budgets, we propose AutoRefine, a novel LLM-based surrogate that replaces costly black-box search. Across 10 tasks, AutoAdapt achieves a 25% average accuracy improvement over state-of-the-art Automated Machine Learning baselines with minimal optimization overhead.


## Installation and Quick Start

We recommend using a conda environment:

```bash
conda create --name autoadapt python=3.12.3
```

To install AutoAdapt, execute the following command, after cloning the repository:

```bash
pip install .
```

## Usage

AutoAdapt supports **two ways of usage**:
1. A **Command Line Interface (CLI)** 
2. A **React-based UI** that runs locally in your browser

Choose the option that best fits your needs.

### Option 1: Use AutoAdapt via CLI

Follow the steps below to configure and run AutoAdapt:

1. Navigate to the `app/sample` directory and create a `data` subdirectory. Place your training dataset, test dataset, and RAG context files (if needed) within this folder.

2. Update the configuration file located at `app/sample/conf/config.yaml` with the following:
   - Path to the project directory (`general.project_path`)
   - Paths to the respective datasets and context documents (`data.dataset_name_or_path`, `data.test_dataset_name_or_path`)
   - Column nomenclature specifications (`data.input_column`, `data.response_column`)
   - Other optional configurations


3. Set the Hugging Face access token, OpenAI API Key and Serp API Key:

   ```bash
   export HF_ACCESS_TOKEN="your_hf_token"
   export API_KEY="your_openai_key"
   export SERPAPI_KEY="your_serpapi_key"
   ```

3. Customize the configuration file according to your requirements.

4. (Optional) Update the `app/sample/conf/user_preferences.md` file to specify any user preferences.

5. (Optional) Update/Add an evaluation function specific to your task in the `src/autoadapt/utils/template.py` file and specify the function name using the `evaluation.eval_func` config.

6. Navigate to the application directory (`app/sample`) and execute the following command to start AutoAdapt:

   ```bash
   python3 run.py
   ```

### Option 2: Use AutoAdapt via the UI 

Follow the steps below to configure and run AutoAdapt UI:

1. Ensure that [Node.js](https://nodejs.org/en/download) and [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) is installed.

2. Set the Hugging Face access token, OpenAI API Key and Serp API Key:

   ```bash
   export HF_ACCESS_TOKEN="your_hf_token"
   export API_KEY="your_openai_key"
   export SERPAPI_KEY="your_serpapi_key"
   ```

3. Navigate to `app/react` and run the `setup.sh` file:
   ```bash
   cd app/react
   bash setup.sh
   ```

4. Once the servers have started, run the following command:
   ```bash
   bash start.sh
   ```

5. Open browser and navigate to http://localhost:8080.

Note: The templates provided in `src/autoadapt/template` can also be directly used by navigating to the required directory (e.g. `src/autoadapt/template/sft`) and changing the config file (e.g. `src/autoadapt/template/sft/conf/config.yaml`) within the directory, for domain-adaptation of LLM on hyperparameters chosen by the user.

## Folder Structure

```
AutoAdapt/
├── app/                                # Application entry points and data
│   ├── data/
│   │   └── models_data_database/       # Model and dataset metadata (JSON)
│   ├── react/                          # React-based UI
│   │   ├── backend/                    # FastAPI backend server
│   │   │   └── conf/                   # Backend configuration
│   │   ├── frontend/                   # React + Vite frontend
│   │   │   ├── public/
│   │   │   └── src/
│   │   ├── setup.sh                    # UI setup script
│   │   └── start.sh                    # UI start script
│   └── sample/                         # CLI sample application
│       ├── conf/                       # Sample config (config.yaml, user_preference.md)
│       ├── run.py                      # Main CLI entry point
│       ├── run_plan.py                 # Plan-only execution
│       └── run_dashboard.sh            # Dashboard launcher
│
├── src/
│   ├── autoadapt/                      # Core AutoAdapt package
│   │   ├── cli.py                      # CLI interface
│   │   ├── adapt/                      # Adaptation pipeline orchestration
│   │   │   ├── adapt_pipeline.py       # End-to-end adaptation pipeline
│   │   │   ├── adapt_step.py           # Individual adaptation step
│   │   │   ├── autoadapt_executor.py   # AutoAdapt executor
│   │   │   ├── base_executor.py        # Base executor class
│   │   │   ├── extract_dataset_stats.py# Dataset statistics extraction
│   │   │   ├── pipeline.py             # Pipeline definition
│   │   │   └── pipeline_executor.py    # Pipeline execution engine
│   │   ├── agents/                     # Multi-agent system
│   │   │   ├── aggregator_agent.py     # Aggregates agent outputs
│   │   │   ├── base_agent.py           # Base agent class
│   │   │   ├── base_worker.py          # Base worker class
│   │   │   ├── best_practice_agent.py  # Best practices retrieval agent
│   │   │   ├── data_agent.py           # Data analysis agent
│   │   │   ├── knowledge_retriever_agent.py  # Knowledge retrieval agent
│   │   │   ├── messages.py             # Agent message definitions
│   │   │   ├── research_agent.py       # Research/web search agent
│   │   │   ├── user_preference_agent.py# User preference parsing agent
│   │   │   ├── best_practices/         # Best practice retrieval utilities
│   │   │   └── knowledge_retriever/    # Knowledge retrieval utilities
│   │   ├── config/                     # Configuration and knowledge bases
│   │   │   ├── knowledge.md            # Domain adaptation knowledge base
│   │   │   ├── knowledge_hparams.md    # Hyperparameter knowledge base
│   │   │   └── model_selection_kb.md   # Model selection knowledge base
│   │   ├── dashboard/                  # Streamlit dashboard
│   │   │   ├── Home.py                 # Dashboard home page
│   │   │   ├── pages/                  # Dashboard sub-pages
│   │   │   └── static/                 # Static assets
│   │   ├── evaluate/                   # Evaluation module
│   │   │   └── evaluator.py            # Model evaluation logic
│   │   ├── frontend/                   # Frontend message interfaces
│   │   │   ├── cli_message.py          # CLI message formatting
│   │   │   └── streamlit_message.py    # Streamlit message formatting
│   │   ├── hpo/                        # Hyperparameter optimization (AutoRefine)
│   │   │   ├── coreset_selection.py    # Core-set selection for training
│   │   │   ├── gaussian_process.py     # Gaussian process surrogate
│   │   │   ├── hpo_executor.py         # HPO execution engine
│   │   │   ├── llm_gp_sampler.py       # LLM-guided GP sampler
│   │   │   ├── llm_sampler.py          # LLM-based sampler
│   │   │   └── llm_surrogate_sampler.py# LLM surrogate sampler
│   │   ├── memory/                     # Shared state management
│   │   │   └── shared_memory.py        # Shared memory across components
│   │   ├── plan/                       # Planning module
│   │   │   ├── adapt_config_graph.py   # Adaptation configuration graph
│   │   │   ├── base_planner.py         # Base planner class
│   │   │   └── multiagent_debate_planner.py  # Multi-agent debate planner
│   │   ├── template/                   # Standalone adaptation templates
│   │   │   ├── sft/                    # Supervised fine-tuning template
│   │   │   ├── dpo/                    # Direct preference optimization template
│   │   │   └── rag/                    # Retrieval-augmented generation template
│   │   └── utils/                      # Utility modules
│   └── deepcore/                       # Data selection methods
│
├── pyproject.toml                      # Project build configuration
├── requirements.txt                    # Python dependencies
├── README.md
├── LICENSE
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── SECURITY.md
└── SUPPORT.md
```

## Intended Use

This repository provides research-oriented code and reference implementations for studying automated domain adaptation and agent‑based optimization techniques in machine learning systems. The primary goal of this project is to support experimentation, benchmarking, and academic or industrial research into model adaptation workflows, planning strategies, and evaluation methodologies.

The code in this repository is not a production‑ready system and is not intended to be deployed as a live service, integrated into operational decision‑making pipelines, or used to directly make or automate real‑world decisions affecting users, customers, or systems. It does not include hosted services, pretrained proprietary models, or runtime components that operate on live customer or production data. The framework has been tested on benchmark datasets (in English language) for research purposes and academic validation.

This project does not provide end‑user AI applications, decision engines, or autonomous systems. Any outputs generated by experiments using this code are intended solely for offline analysis, research validation, and prototyping. Users are responsible for performing their own validation, safety assessments, and compliance reviews before applying concepts or code from this repository in downstream systems or production environments.

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit [Contributor License Agreements](https://cla.opensource.microsoft.com).

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.

## Third-Party Code

This project uses the following third-party open source packages (installed via `requirements.txt`):

- **openai** — OpenAI Python client (MIT License)
- **azure-identity / azure-core** — Azure SDK authentication (MIT License)
- **tiktoken** — Token counting (MIT License)
- **trl** — Transformer Reinforcement Learning (Apache-2.0 License)
- **deepcore** — Data-efficient learning and coreset selection (MIT License)
- **vllm** — High-throughput LLM serving engine (Apache-2.0 License)
- **optuna** — Hyperparameter optimization framework (MIT License)
- **gpytorch** — Gaussian process inference with PyTorch (MIT License)
- **serpapi** — SerpApi web search client (MIT License)
- **langchain-community / langchain-huggingface** — LLM orchestration framework (MIT License)
- **autogen-core / autogen-ext** — Multi-agent conversation framework (MIT License)

See [requirements.txt](requirements.txt) for the full list of dependencies.

## License

Copyright (c) Microsoft Corporation. All rights reserved.

Licensed under the [MIT](LICENSE) license.

## Citation

If you find this work useful, please cite:

```bibtex
@misc{sinha2026autoadaptautomateddomainadaptation,
      title={AutoAdapt: An Automated Domain Adaptation Framework for LLMs}, 
      author={Sidharth Sinha and Anson Bastos and Xuchao Zhang and Akshay Nambi and Chetan Bansal and Saravan Rajmohan},
      year={2026},
      eprint={2603.08181},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2603.08181}, 
}
```
