## PlanningBench: Generating Scalable and Verifiable Planning Data for Evaluating and Training Large Language Models

<p align="center">
  <img src="asset/hunyuanlogo.png" alt="Tencent Hunyuan" height="54"/>
  <img src="asset/cn_ruc_logo.png" alt="Renmin University of China" height="54"/>
</p>

<p align="center">
  <a href="https://arxiv.org/abs/2605.20873"><img src="https://img.shields.io/badge/arXiv-PlanningBench-b31b1b.svg" alt="arXiv"/></a>
  <a href="https://huggingface.co/datasets/tencent/PlanningBench"><img src="https://img.shields.io/badge/HuggingFace-Dataset-yellow" alt="Hugging Face"/></a>
  <a href="./LICENSE-PlanningBench.txt"><img src="https://img.shields.io/badge/Licence-PlanningBench-blue.svg" alt="Licence"/></a>
  <a href="./data/PlanningBench-eval.jsonl"><img src="https://img.shields.io/badge/Data-467%20Planning%20Data-green" alt="Data"/></a>
PlanningBench is a synthetic planning benchmark and data construction framework for evaluating and training large language models on complex, text-based planning tasks. It focuses on whether a model can coordinate goals, constraints, resources, time windows, dependencies, priorities, and objectives into an executable and verifiable plan.

Unlike fixed collections of hand-written planning examples, PlanningBench abstracts real planning scenarios into reusable task taxonomies, constraint families, and difficulty factors. The benchmark is designed to test complete-plan success under coupled constraints rather than only local requirement satisfaction.

### Overview

<div align="center">
  <img src="asset/planningbench-logo.png" alt="PlanningBench logo" width="400"/>
</div>
PlanningBench targets self-contained text-based planning problems where all information needed to construct and verify a plan is provided in the input. Each instance contains a planning question and corresponding verification checklists, so that model outputs can be evaluated for constraint satisfaction and objective quality.

The current repository releases **467 synthetic planning instances**, and all 467 instances are intended for **evaluation**. They should be treated as benchmark/test data rather than training data.

The released data is written and checked manually. It does **not** contain proprietary business data, user logs, customer data, production data, or enterprise workflow records. Human annotators are involved in quality control and review; they do not create the benchmark instances from scratch.

### What We Release

This repository contains:

```text
PlanningBench/
├── data/
│   └── PlanningBench-eval.jsonl         # 467 synthetic evaluation instances\
├── asset/
│   ├── planningbench-logo.png           # PlanningBench benchmark logo
│   ├── hunyuanlogo.png                  # Tencent Hunyuan logo
│   ├── cn_ruc_logo.png                  # Renmin University of China logo
│   ├── figure-data.png                  # Task taxonomy and data distribution figure
│   └── figure-framework.png             # Data construction framework figure
├── LICENSE-PlanningBench.txt
└── README.md
```

### Task Taxonomy and Data Distribution

We define the task space used by PlanningBench. It organizes planning problems into six high-level planning families, more than 30 concrete task types, and multiple subtask variants.

The taxonomy is organized by planning structure rather than only surface application domain. It covers temporal conflicts, resource assignment, coverage and fairness, route coordination, production dependencies, emergency response priorities, and other sources of planning difficulty.

<p align="center">
  <img src="asset/figure-data.png" alt="PlanningBench task taxonomy and data distribution" width="760"/>
</p>

The six high-level families are:

- **Scheduling and Timetabling**: temporal conflicts, time windows, and execution order.
- **Project and Production Operations**: milestones, dependencies, capacity, and continuity.
- **Routing and Travel**: route selection, spatiotemporal coordination, and transfers.
- **Emergency Response and Public Service**: timeliness, priority allocation, and replanning.
- **Allocation and Matching**: resource assignment under compatibility and capacity limits.
- **Shift and Workforce Scheduling**: coverage, rotation fairness, and availability.

### Data Construction Framework

PlanningBench follows a constraint-driven synthesis pipeline. The construction process abstracts realistic planning scenarios into task and constraint taxonomies, samples task-constraint configurations, generates self-contained planning questions, attaches verification checklists or rubrics, and applies automatic filtering plus human quality-control review.

<p align="center">
  <img src="asset/figure-framework.png" alt="PlanningBench construction framework" width="760"/>
</p>

The pipeline contains two main stages:

1. **Task and constraint taxonomy construction**: representative planning scenarios are summarized into task families, concrete tasks, subtask variants, general constraints, task-specific constraints, and specialized stateful constraints.
2. **Constraint-driven synthesis and difficulty enhancement**: a Generator creates candidate planning instances, a Responder attempts to solve them, and a Critic verifies outputs against the checklist. Feedback from solved or unsolved instances is used to adjust sampling toward appropriate difficulty.

This design supports controllable diversity across tasks, constraints, and solution structures. Difficulty can be adjusted through factors such as constraint tightness, resource scarcity, objective conflicts, subtask dependencies, and global coordination requirements.

### Citation

If you use PlanningBench, please cite:

```bibtex
@article{zhao2026planningbench,
  title={PlanningBench: Generating Scalable and Verifiable Planning Data for Evaluating and Training Large Language Models},
  author={Zhao, Ziliang and Xu, Zenan and Wang, Shuting and Qian, Hongjin and Lei, Yan and Hu, Minda and Wang, Zhao and Dou, Shihan and Dou, Zhicheng and Zhou, Pluto},
  journal={arXiv preprint arXiv:2605.20873},
  year={2026}
}
```

### License

Please refer to [`LICENSE.txt`](./LICENSE.txt) for license information.
