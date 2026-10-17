# SkillGym: Training Skill-Use Agents with Automatic Verifiable Environment Generation

[![Paper](https://img.shields.io/badge/arXiv-2609.37539-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2609.37539) [![Models](https://img.shields.io/badge/Hugging%20Face-Models-ffd21e?logo=huggingface&logoColor=black)](https://huggingface.co/collections/reasonwang/skillgym) [![Evaluation set](https://img.shields.io/badge/Hugging%20Face-Evaluation%20set-ffd21e?logo=huggingface&logoColor=black)](https://huggingface.co/datasets/reasonwang/skillgym-test) [![Training trajectories](https://img.shields.io/badge/Hugging%20Face-Training%20trajectories-ffd21e?logo=huggingface&logoColor=black)](https://huggingface.co/datasets/reasonwang/skillgym-sft)

SkillGym is an automatic pipeline that turns community-written agent skills into executable, verifiable training tasks. A builder-reviewer agent system constructs skill-critical tasks across four reasoning structures (procedural, abductive, constraint satisfaction, and partial order), each with a reference solution and an executable verifier. Finetuning on trajectories collected from these tasks improves how LLM agents use skills, across model families and sizes.

![Overview of SkillGym](assets/skillgym_overview.png)

## Models

All models are finetuned with supervised finetuning (SFT) on SkillGym trajectories for 2 epochs.


| Model                      | Base model  | Size              | Link                                               |
| -------------------------- | ----------- | ----------------- | -------------------------------------------------- |
| SkillGym-MiniCPM5-2B       | MiniCPM5    | 2B                | Not released yet     |
| SkillGym-Qwen3.5-4B        | Qwen3.5     | 4B                | [reasonwang/SkillGym-Qwen3.5-4B](https://huggingface.co/reasonwang/SkillGym-Qwen3.5-4B)         |
| SkillGym-Ministral-3-8B    | Ministral-3 | 8B                | [reasonwang/SkillGym-Ministral-3-8B](https://huggingface.co/reasonwang/SkillGym-Ministral-3-8B) |
| SkillGym-Qwen3.5-9B        | Qwen3.5     | 9B                | [reasonwang/SkillGym-Qwen3.5-9B](https://huggingface.co/reasonwang/SkillGym-Qwen3.5-9B)         |
| SkillGym-Qwen3.5-27B       | Qwen3.5     | 27B               | [reasonwang/SkillGym-Qwen3.5-27B](https://huggingface.co/reasonwang/SkillGym-Qwen3.5-27B)       |
| SkillGym-Qwen3.5-122B-A10B | Qwen3.5     | 122B (10B active) | [reasonwang/SkillGym-Qwen3.5-122B-A10B](https://huggingface.co/reasonwang/SkillGym-Qwen3.5-122B-A10B)     |




## Evaluation set

The SkillGym test set contains 400 tasks: 200 on skills seen during training (held-in) and 200 on skills excluded from training (held-out), covering all four reasoning structures. Each task ships with an instruction, an initial workspace, a container environment, the source skill, and an executable verifier.

- Download: [reasonwang/skillgym-test](https://huggingface.co/datasets/reasonwang/skillgym-test)
- Tasks are in Harbor task format, organized as `tasks/<profile>/<held_in|held_out>/<task>/`, with 50 held-in and 50 held-out tasks per profile. `manifest.jsonl` lists every task with its profile, split, skill, and domain. See the dataset card for the layout of a task package.



## Training trajectories

The SFT data contains 19,053 successful agent trajectories on SkillGym tasks, one JSONL file per agent harness (AgentFly, mini-swe-agent, and Terminus-2).

- Download: [reasonwang/skillgym-sft](https://huggingface.co/datasets/reasonwang/skillgym-sft)

## Results

Scores are on a 0-100 scale, higher is better. SkillGym is task success on our test set. SkillEval and SkillsBench report the mean and standard deviation over three runs. Skill-Use-Bench reports the skill-use (SU) score. All models are evaluated with skills available.


| Model          | Size     | SkillGym | SkillEval      | SkillsBench    | Skill-Use-Bench |
| -------------- | -------- | -------- | -------------- | -------------- | --------------- |
| MiniCPM5       | 2B       | 33.2     | 63.0 ± 0.6     | 10.8 ± 2.7     | 24.1            |
| + SkillGym SFT | 2B       | 33.2     | **68.1 ± 2.0** | 6.1 ± 0.8      | **44.7**        |
| Ministral-3    | 8B       | 17.5     | 55.7 ± 3.1     | 3.9 ± 2.7      | 4.3             |
| + SkillGym SFT | 8B       | **49.5** | **77.5 ± 0.4** | **16.9 ± 1.3** | **55.1**        |
| Qwen3.5        | 4B       | 33.8     | 62.8 ± 1.5     | 10.1 ± 1.3     | 8.8             |
| + SkillGym SFT | 4B       | **47.0** | **70.8 ± 1.6** | **14.3 ± 1.0** | **48.7**        |
| Qwen3.5        | 9B       | 41.3     | 65.7 ± 1.1     | 14.8 ± 3.5     | 14.8            |
| + SkillGym SFT | 9B       | **59.5** | **74.7 ± 1.2** | **22.4 ± 4.2** | **49.6**        |
| Qwen3.5        | 27B      | 55.3     | 76.2 ± 1.1     | 32.6 ± 2.3     | 28.3            |
| + SkillGym SFT | 27B      | **62.8** | **80.1 ± 1.5** | **47.4 ± 5.1** | **74.2**        |
| Qwen3.5        | 122B/10B | 53.0     | 69.8 ± 1.1     | 30.1 ± 2.5     | 16.8            |
| + SkillGym SFT | 122B/10B | **65.0** | **80.0 ± 0.3** | **53.6 ± 5.2** | **72.2**        |


See the paper for reference models, held-out results, and analysis.

## Citation

```bibtex
@article{wang2026skillgym,
  title   = {{SkillGym}: Training Skill-Use Agents with Automatic Verifiable Environment Generation},
  author  = {Wang, Renxi and Hee, Mingshan and Koto, Fajri and Baldwin, Timothy and Li, Haonan},
  journal = {arXiv preprint arXiv:2609.37539},
  year    = {2026}
}
```



## Contact

Questions and issues are welcome through GitHub issues, or by email to [renxi.wang@mbzuai.ac.ae](mailto:renxi.wang@mbzuai.ac.ae).