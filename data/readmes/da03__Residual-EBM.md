# Residual Energy-Based Models for Text Generation

This repo implements the Residual Energy-Based Model as described in [Residual Energy-Based Models for Text Generation](https://arxiv.org/abs/2004.11714). Note that both data and model (generator+discriminator) are different from the original paper: the goal is just to show how the pipeline works, using much less computational resources.

The training and evaluation scripts can be found in [REBM.ipynb](REBM.ipynb). We suggest opening it using Google Colab with a GPU instance.

## Method and related research

[Energy-based text generation: residual models, resampling and diffusion](https://yuntiandeng.com/research/energy-based-text-generation/) explains the sequence-level energy formulation, noise-contrastive estimation, and importance resampling, with an interactive reweighting example and connections to energy-based diffusion language models.

## Citation

```
@inproceedings{deng2020residual,
  title={Residual Energy-Based Models for Text Generation},
  author={Deng, Yuntian and Bakhtin, Anton and Ott, Myle and Szlam, Arthur and Ranzato, Marc'Aurelio},
  booktitle={International Conference on Learning Representations},
  year={2020}
}

@article{bakhtin2021residual,
  title={Residual Energy-Based Models for Text},
  author={Bakhtin, Anton and Deng, Yuntian and Gross, Sam and Ott, Myle and Ranzato, Marc'Aurelio and Szlam, Arthur},
  journal={Journal of Machine Learning Research},
  volume={22},
  number={40},
  pages={1--41},
  year={2021}
}
```
