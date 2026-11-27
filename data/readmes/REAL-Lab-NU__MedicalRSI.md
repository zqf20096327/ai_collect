<h3 align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/title_dark.svg">
    <img src="docs/assets/title.svg" width="640" alt="MedicalRSI">
  </picture><br>
  Medical Recursive Self-Improving Agents via Clinical Model-Harness Co-Evolution
</h3>

<p align="center">
  <a href="https://arxiv.org/abs/2611.26806"><img src="https://img.shields.io/badge/arXiv-2611.26806-9B2C4E?logo=arxiv&logoColor=white" alt="arXiv 2611.26806"></a>
  <a href="https://real-lab-nu.github.io/MedicalRSI/"><img src="https://img.shields.io/badge/Website-Project%20Page-6F8FC0?logo=googlechrome&logoColor=white" alt="Project page"></a>
  <a href="https://huggingface.co/REAL-LAB-NU/MedicalRSI-MedAgentBench-Qwen3.5-9B"><img src="https://img.shields.io/badge/Model-Hugging%20Face-C9A227?logo=huggingface&logoColor=white" alt="Model on Hugging Face"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-5FA8B8" alt="MIT license"></a>
</p>

<p align="center">
  <a href="https://real-lab-nu.github.io/MedicalRSI/#demo"><img src="https://img.shields.io/badge/%E2%96%B6%20Interactive%20Demo-One%20Round%20of%20MedicalRSI-9B2C4E?style=for-the-badge" alt="Open the interactive demo"></a>
</p>

<p align="center">
  <a href="https://real-lab-nu.github.io/MedicalRSI/#demo"><img src="docs/assets/readme/demo.webp" width="100%" alt="One round of MedicalRSI in nine steps: a clinical workflow arrives, the Solver tries every patient, failures become evidence, the Improver writes candidate harnesses, the Solver tries each candidate, each harness earns its gain, one update trains both roles, the Improver adapts as the agent learns, and at test time a new workflow is fixed from a few failures."></a>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme/highlights_dark.webp">
    <img src="docs/assets/readme/highlights_light.webp" width="100%" alt="One model, two roles. Rewarded by gain. Trained together.">
  </picture>
</p>

## <img src="docs/assets/readme/icons/emergency.svg" height="32"> The Problem

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme/problem_dark.webp">
    <img src="docs/assets/readme/problem_light.webp" width="100%" alt="One workflow, many patients. Fixed after deployment. A fixed improving strategy. Recursive self-improvement: an agent improves not only itself but also its improving strategy.">
  </picture>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme/hard_dark.webp">
    <img src="docs/assets/readme/hard_light.webp" width="100%" alt="Why this is hard in medicine: no reference harness, and errors change as the agent learns. The central question: how can a medical agent continually improve its improving strategy from its own outcomes?">
  </picture>
</p>

## <img src="docs/assets/readme/icons/hub.svg" height="32"> Clinical Model-Harness Co-Evolution

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme/roles_dark.webp">
    <img src="docs/assets/readme/roles_light.webp" width="100%" alt="Solver: the medical agent itself. Improver: its learnable improving strategy.">
  </picture>
</p>

### Overview of MedicalRSI

<p align="center">
  <a href="docs/assets/method.webp"><img src="docs/assets/method.webp" width="100%" alt="Overview of MedicalRSI: the Solver attempts a workflow with H0, the attempts become workflow evidence, the Improver writes candidate harnesses, the Solver evaluates each of them, rewards are computed, and one joint update trains both roles; workflow memory keeps the better harness."></a>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme/components_dark.webp">
    <img src="docs/assets/readme/components_light.webp" width="100%" alt="What makes it work: workflow evidence, skills and tools, workflow memory, counterfactual gain reward, joint dual-role optimization, test-time adaptation.">
  </picture>
</p>

### Details of the Failure-Grounded Medical Harness

<p align="center">
  <a href="docs/assets/harness.webp"><img src="docs/assets/harness.webp" width="100%" alt="Clinical workflow evidence, the medical harness (skills, tools and workflow memory) and test-time adaptation to a new workflow."></a>
</p>

## <img src="docs/assets/readme/icons/insights.svg" height="32"> Results

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme/stats_dark.webp">
    <img src="docs/assets/readme/stats_light.webp" width="100%" alt="85.1% on MedAgentBench, 89.0% on MedAgentGym, 3.3 times the Base Agent on unseen workflows, and 7 of 7 other solvers improve with harnesses from our Improver.">
  </picture>
</p>

### MedicalRSI Outperforms Existing Methods and Keeps Improving

<p align="center">
  <a href="docs/assets/teaser.webp"><img src="docs/assets/teaser.webp" width="100%" alt="Tasks solved on MedAgentBench by method group, and improvement over training rounds for MedicalRSI, the GRPO Improver and the GRPO Solver."></a>
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme/table_dark.webp">
    <img src="docs/assets/readme/table_light.webp" width="100%" alt="Tasks solved on MedAgentBench with Qwen3.5-9B on training and unseen workflows for the Base Agent, harness-only, model-only and MedicalRSI.">
  </picture>
</p>

### Analysis of Co-Evolution

<p align="center">
  <a href="docs/assets/coevo.webp"><img src="docs/assets/coevo.webp" width="100%" alt="Analysis of co-evolution: one solver with two improvers, and the gain of each role over training rounds."></a>
</p>

### Analysis of Transfer Beyond Training

<p align="center">
  <a href="docs/assets/transfer.webp"><img src="docs/assets/transfer.webp" width="100%" alt="Transfer beyond training: new solvers, a new Improver and a new database."></a>
</p>

## <img src="docs/assets/readme/icons/clinical_notes.svg" height="32"> Case Study

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme/case_dark.webp">
    <img src="docs/assets/readme/case_light.webp" width="100%" alt="A task from a workflow never seen in training: the Solver alone passes 2 of 11 checks; with the harness written from these failures it passes 11 of 11, without any retraining.">
  </picture>
</p>

<p align="center">
  <a href="docs/assets/case.webp"><img src="docs/assets/case.webp" width="100%" alt="Case study on an unseen workflow: the Solver's trajectory alone, the harness written by MedicalRSI, and the Solver's trajectory with the harness."></a>
</p>

## <img src="docs/assets/readme/icons/rocket_launch.svg" height="32"> Quick Start

> [!TIP]
> The released MedAgentBench model needs no training: download it and run `evaluate`.

### Installation

```bash
conda create -n medicalrsi python=3.12 -y && conda activate medicalrsi
pip install -e ".[gpu]"        # one environment for both benchmarks
```

### Data

```bash
# MedAgentBench: tasks, split and warm-start data are in data/medagentbench; start its FHIR server
docker run -d -p 8080:8080 jyxsu6/medagentbench:latest
# optional: save the server's data once, then MedicalRSI serves it without Docker (env.fhir_snapshot)
python -m medicalrsi.envs.medagentbench.fhir_snapshot --base http://localhost:8080/fhir/ --out data/medagentbench/fhir_snapshot

# MedAgentGym (MIMIC-III, PhysioNet credentialed access): build the split
python -m medicalrsi.envs.medagentgym.prepare --source <MedAgentGym>/ehr_seqsql \
    --database <EHRSQL>/mimic_iii.sqlite --out data/medagentgym
ln -s <EHRSQL>/mimic_iii.sqlite data/medagentgym/mimic_iii.sqlite
```

### Evaluate the released model

```bash
hf download REAL-LAB-NU/MedicalRSI-MedAgentBench-Qwen3.5-9B --local-dir checkpoints/medagentbench
python -m medicalrsi evaluate --config configs/medagentbench_qwen3.5-9b.yaml \
    --adapter checkpoints/medagentbench/adapter --memory checkpoints/medagentbench/memory
```

### Train

```bash
# MedAgentBench: warm start, then ten rounds of co-evolution and the test
python -m medicalrsi warmstart --config configs/medagentbench_qwen3.5-9b.yaml
python -m medicalrsi train --config configs/medagentbench_qwen3.5-9b.yaml

# MedAgentGym: the warm-start harnesses come from a teacher model (OpenAI-compatible API, OPENAI_API_KEY)
python -m medicalrsi warmstart --config configs/medagentgym_qwen3.5-9b.yaml --set warmstart.teacher_model=<model>
python -m medicalrsi train --config configs/medagentgym_qwen3.5-9b.yaml
```

> [!NOTE]
> MIMIC-III requires PhysioNet credentialed access. Follow PhysioNet's terms when a hosted LLM writes the warm-start
> harnesses.

## <img src="docs/assets/readme/icons/folder_open.svg" height="32"> Repository

```
medicalrsi/
├── coevolve.py     Clinical Model-Harness Co-Evolution: rounds, gain reward, memory, joint update
├── evaluate.py     test-time adaptation to new workflows and the scores
├── warmstart.py    teacher harnesses and the warm start
├── policy.py       the dual-role policy: the Solver's attempts and the Improver's harnesses
├── trainer.py      joint dual-role GRPO and supervised fine-tuning (torchrun)
├── llm.py          vLLM servers with the current LoRA adapter
├── envs/           clinical environments: medagentbench (FHIR), medagentgym (SQL)
└── prompts/        the Improver's prompt for each environment
configs/            the two runs of the paper
data/               MedAgentBench tasks, split and warm-start data
docs/               the project page
```

A new clinical environment is a subclass of `medicalrsi.envs.base.Env` with its Improver prompt in `medicalrsi/prompts`.

## <img src="docs/assets/readme/icons/format_quote.svg" height="32"> Citation

```bibtex
@article{wang2026medicalrsi,
  title   = {MedicalRSI: Medical Recursive Self-Improving Agents via Clinical Model-Harness Co-Evolution},
  author  = {Wang, Ziqing and Palangi, Hamid and Zhao, Lili and Ding, Kaize},
  journal = {arXiv preprint arXiv:2611.26806},
  year    = {2026}
}
```

## License

MIT (see [LICENSE](LICENSE)). The MedAgentBench tasks and graders shipped here keep their upstream terms, listed in [data/medagentbench/LICENSE](data/medagentbench/LICENSE) and [medicalrsi/envs/medagentbench/graders/LICENSE](medicalrsi/envs/medagentbench/graders/LICENSE). MedAgentGym, EHRSQL and MIMIC-III are not included and keep their own terms.
