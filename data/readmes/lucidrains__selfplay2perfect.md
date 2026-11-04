## selfplay2perfect (wip)

Implementation of [Play2Perfect](https://play2perfect.github.io/), from Tyler Ga Wei Lum et al. of Stanford, with a Self Play element and [AlphaNIST](https://arxiv.org/abs/2610.13354) Success-Guided Sampling (SGS).

## install

```shell
$ pip install selfplay2perfect
```

## usage

```python
from selfplay2perfect import (
    ActorCritic,
    PickAndPlaceCurriculum,
    PointCloudEncoder,
    Population,
    make_single_arm_env,
    train
)

model = ActorCritic(
    dim_obs = 46,
    dim_action = 29,
    dim_priv_obs = 8,
    num_blocks = 4,
    dim_scene_embed = 96,
    dim_embed = 192,
    scene_encoder = PointCloudEncoder(dim_point = 6, dim_hidden = 128, dim_embed = 96)
)

policy = train(
    Population(model, size = 4),                                      # or just `model`
    curriculum = PickAndPlaceCurriculum(ladder_size = 55, native_size = 11),
    self_play = False,
    envs = make_single_arm_env(num_envs = 64, use_sim2real = True)    # one env or many
)

# policy.pt
```

## citations

```bibtex
@misc{lum2026play2perfectmattersdexterousplay,
    title   = {Play2Perfect: What Matters in Dexterous Play Pretraining for Precise Assembly?}, 
    author  = {Tyler Ga Wei Lum and Kushal Kedia and C. Karen Liu and Jeannette Bohg},
    year    = {2026},
    eprint  = {2606.26428},
    archivePrefix = {arXiv},
    primaryClass = {cs.RO},
    url     = {https://arxiv.org/abs/2606.26428}, 
}
```

```bibtex
@misc{zhang2026alphanistemergentassemblyskills,
    title     = {AlphaNIST: Emergent Assembly Skills from Binary Task Rewards}, 
    author    = {Octi Zhang and Iretiayo Akinola and Rosario Scalise and Mateo Guaman Castro and Patrick Yin and Tobias Widmer and Miles Macklin and Chris Amevor and Dylan Turpin and Dirk Van Gelder and Jan Carius and Ankur Handa and Gavriel State and Yunrong Guo and Yashraj Narang},
    year      = {2026},
    eprint    = {2610.13354},
    archivePrefix = {arXiv},
    primaryClass = {cs.AI},
    url       = {https://arxiv.org/abs/2610.13354}, 
}
```

```bibtex
@misc{zhang2026omnireset,
    title     = {OmniReset: Success-Guided Sampling for Reinforcement Learning},
    author    = {Octi Zhang and others},
    year      = {2026},
    eprint    = {2610.12465},
    archivePrefix = {arXiv},
    primaryClass = {cs.LG},
    url       = {https://arxiv.org/abs/2610.12465},
}
```

```bibtex
@inproceedings{singla2024sapg,
    title     = {SAPG: Split and Aggregate Policy Gradients},
    author    = {Jayesh Singla and Ananye Agarwal and Deepak Pathak},
    booktitle = {International Conference on Machine Learning (ICML)},
    year      = {2024},
    url       = {https://arxiv.org/abs/2407.20230},
}
```
