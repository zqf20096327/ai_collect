<img src="./fig2.png" width="400px"></img>

## Supermimic - Pytorch

Unofficial implementation of [Supermimic, Scaling Humanoid Whole-Body Control with One Differentiable World Model](https://supermimic.github.io/), from Qiayuan Liao et al. of Berkeley

## Install

```bash
$ pip install supermimic-pytorch
```

## Usage

```python
import torch
from torch import nn
from x_mlps_pytorch import MLP
from supermimic_pytorch import WorldModel, SuperMimic

world_model = WorldModel(
    dim_state = 71,
    dim_action = 29,
    dim_sim_context = 33
)

actor = MLP(71 + 71, 2048, 1024, 512, 256, 29, activation = nn.GELU())

supermimic = SuperMimic(
    actor = actor,
    world_model = world_model,
    observation_noise_scale = 0.05
)

# logged transitions from any non-differentiable simulator

state = torch.randn(4, 71)
sim_context = torch.randn(4, 33)
logged_actions = torch.randn(4, 32, 29)
logged_next_states = torch.randn(4, 32, 71)
logged_terminals = torch.randint(0, 2, (4, 32)).float()

# fit world model autoregressively on k = 32 window

wm_loss, _, _ = world_model.rollout(
    state,
    logged_actions,
    logged_next_states,
    sim_context = sim_context,
    next_terminals = logged_terminals
)
wm_loss.backward()

# imagine H = 32 steps through frozen world model and train actor via bptt

goals = torch.randn(4, 33, 71)

rollout = supermimic(
    state,
    sim_context = sim_context,
    actor_goals = goals,
    num_rollout_timesteps = 32
)

rewards = -(rollout.states[:, 1:] - goals[:, :-1]).square().mean(dim = -1)

actor_loss = supermimic.actor_loss(
    rewards,
    rollout.terminals
)

actor_loss.backward()
```

## Experiments

Toy `HalfCheetah-v5` experiment - trains an `x-ppo` expert, then tracks an 8-dim pose subset (no velocities or task reward) through the learned world model

```bash
$ uv run train_cheetah.py
```

<img src="./assets/cheetah/cheetah_expert_vs_supermimic.webp" width="500px"></img>

<img src="./assets/cheetah/cheetah_convergence.png" width="500px"></img>

[RUKA-v2](https://github.com/ruka-hand-v2/RUKA-v2) hand experiment - tracks real human hand motion under MuJoCo torque control

```bash
$ uv run train_ruka_hand.py
```

<img src="./assets/ruka/human_vs_ruka_supermimic.webp" width="700px"></img>

<img src="./assets/ruka/ruka_convergence.png" width="500px"></img>

[Unitree Go2](https://github.com/google-deepmind/mujoco_menagerie/tree/main/unitree_go2) quadruped experiment - tracks held-out real German Shepherd motion capture under MuJoCo rigid-body ground contact physics

```bash
$ uv run train_unitree_dog.py
```

<img src="./assets/go2/dog_vs_go2_supermimic.webp" width="700px"></img>

<img src="./assets/go2/go2_convergence.png" width="500px"></img>

## Citations

```bibtex
@misc{liao2026supermimicscalinghumanoidwholebody,
    title   = {SuperMimic: Scaling Humanoid Whole-Body Control with One Differentiable World Model},
    author  = {Qiayuan Liao and Yiyang Shao and Junfeng Long and Kevin Zakka and Roberto Horowitz and Pieter Abbeel and Koushil Sreenath},
    year    = {2026},
    eprint  = {2610.28480},
    archivePrefix = {arXiv},
    primaryClass = {cs.RO},
    url     = {https://arxiv.org/abs/2610.28480},
}
```

```bibtex
@misc{xu2022acceleratedpolicylearningparallel,
    title   = {Accelerated Policy Learning with Parallel Differentiable Simulation},
    author  = {Jie Xu and Viktor Makoviychuk and Yashraj Narang and Fabio Ramos and Wojciech Matusik and Animesh Garg and Miles Macklin},
    year    = {2022},
    eprint  = {2204.07137},
    archivePrefix = {arXiv},
    primaryClass = {cs.LG},
    url     = {https://arxiv.org/abs/2204.07137},
}
```

```bibtex
@misc{georgiev2025pwmpolicylearningmultitask,
    title    = {PWM: Policy Learning with Multi-Task World Models},
    author   = {Ignat Georgiev and Varun Giridhar and Nicklas Hansen and Animesh Garg},
    year     = {2025},
    eprint   = {2407.02466},
    archivePrefix = {arXiv},
    primaryClass = {cs.LG},
    url      =  {https://arxiv.org/abs/2407.02466},
}
```

```bibtex
@article{Peng2021AMPAM,
    title   = {AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control},
    author  = {Xue Bin Peng and Ze Ma and Pieter Abbeel and Sergey Levine and Angjoo Kanazawa},
    year    = {2021},
    eprint  = {2104.02180},
    archivePrefix = {arXiv},
    primaryClass = {cs.GR},
    url     = {https://arxiv.org/abs/2104.02180},
}
```

```bibtex
@misc{gladstone2026explorativemodelingunlockingpretraining,
    title   = {Explorative Modeling: Unlocking a Third Pretraining Axis and End-to-End Generation},
    author  = {Alexi Gladstone and Heng Ji and Yilun Du},
    year    = {2026},
    eprint  = {2607.27372},
    archivePrefix = {arXiv},
    primaryClass = {cs.LG},
    url     = {https://arxiv.org/abs/2607.27372},
}
```

```bibtex
@misc{jia2025antitheticnoisediffusionmodels,
    title   = {Antithetic Noise in Diffusion Models},
    author  = {Jing Jia and Sifan Liu and Bowen Song and Wei Yuan and Liyue Shen and Guanyang Wang},
    year    = {2025},
    eprint  = {2506.06185},
    archivePrefix = {arXiv},
    primaryClass = {cs.LG},
    url     = {https://arxiv.org/abs/2506.06185},
}
```

```bibtex
@misc{zorin2025rukarethinkingdesignhumanoid,
    title   = {RUKA: Rethinking the Design of Humanoid Hands with Learning},
    author  = {Anya Zorin and Irmak Guzey and Billy Yan and Aadhithya Iyer and Lisa Kondrich and Nikhil X. Bhattasali and Lerrel Pinto},
    year    = {2025},
    eprint  = {2504.13165},
    archivePrefix = {arXiv},
    primaryClass = {cs.RO},
    url     = {https://arxiv.org/abs/2504.13165},
}
```

```bibtex
@misc{liu2026rukav2tendondrivenopensource,
    title   = {Ruka-v2: Tendon Driven Open-Source Dexterous Hand with Wrist and Abduction for Robot Learning},
    author  = {Xinqi Lucas Liu and Ruoxi Hu and Alejandro Ojeda Olarte and Zhuoran Chen and Kenny Ma and Charles Cheng Ji and Lerrel Pinto and Raunaq Bhirangi and Irmak Guzey},
    year    = {2026},
    eprint  = {2603.26660},
    archivePrefix = {arXiv},
    primaryClass = {cs.RO},
    url     = {https://arxiv.org/abs/2603.26660},
}
```

```bibtex
@inproceedings{peng2020learningagileroboticlocomotion,
    title     = {Learning Agile Robotic Locomotion Skills by Imitating Animals},
    author    = {Xue Bin Peng and Erwin Coumans and Tingnan Zhang and Tsang-Wei Edward Lee and Jie Tan and Sergey Levine},
    booktitle = {Robotics: Science and Systems (RSS)},
    year      = {2020},
    eprint    = {2004.00784},
    archivePrefix = {arXiv},
    primaryClass = {cs.RO},
    url       = {https://arxiv.org/abs/2004.00784},
}
```

```bibtex
@article{tessler2024maskedmimic,
    title   = {MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting},
    author  = {Chen Tessler and Yunrong Guo and Ofir Nabati and Gal Chechik and Xue Bin Peng},
    journal = {ACM Transactions on Graphics (TOG)},
    volume  = {43},
    number  = {6},
    year    = {2024},
    eprint  = {2409.14393},
    archivePrefix = {arXiv},
    primaryClass = {cs.GR},
    url     = {https://arxiv.org/abs/2409.14393},
}
```
