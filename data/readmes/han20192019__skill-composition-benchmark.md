# Compose-by-Focus Benchmark

This repository releases the **benchmark environments** used in  
**Compose by Focus: Scene Graph-based Atomic Skills** (arXiv:2509.16053).

The benchmark is built on **ManiSkill2** and is designed to evaluate
**compositional long-horizon and multi-step manipulation skills**, including both:

- **Atomic skills**: short-horizon manipulation primitives  
- **Composed tasks**: long-horizon tasks formed by composing multiple skills  

We introduce five sets of new compositional tasks for robot manipulation. Please refer to the paper for more concrete task descriptions. Alongside, we release the motion planning scripts for all the tasks. The benchmark emphasizes robustness to scene variation and long-horizon composition.

<img src="figures/task_figure.png" alt="drawing" width="100%"/>

---
## Overview

Each benchmark task is provided in two forms:

- `*_skill_*`: atomic skill environments  
- `*_compose*`: composed, multi-skill environments  

Composed tasks require the sequential execution of multiple atomic skills
under a shared scene context.

### Included Tasks

- **Cube Out and In**
- **Sort by Color**
- **Blocks Stacking Game**
- **Tools Usage**
- **Obstacle Avoidance**

---

## Quick Start
This script executes both atomic skill environments and composed task
environments for all benchmark scenarios.

```
bash scripts/run_all.sh
```

---
## Citation

If you find this benchmark useful, please cite:

```
@article{qi25arxiv-compose,
  title={Compose by Focus: Scene Graph-based Atomic Skills},
  author={Qi, Han and Chen, Changhe and Yang, Heng},
  journal={arXiv preprint arXiv:2509.16053},
  year={2025},
  note={\linkToWeb{https://computationalrobotics.seas.harvard.edu/SkillComposition/}}
}
```
```
@article{gu2023maniskill2,
  title={Maniskill2: A unified benchmark for generalizable manipulation skills},
  author={Gu, Jiayuan and Xiang, Fanbo and Li, Xuanlin and Ling, Zhan and Liu, Xiqiang and Mu, Tongzhou and Tang, Yihe and Tao, Stone and Wei, Xinyue and Yao, Yunchao and others},
  journal={arXiv preprint arXiv:2302.04659},
  year={2023}
}
```
