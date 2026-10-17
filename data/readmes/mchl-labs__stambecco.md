<p align="center" width="100%">
  <img src="./assets/Stambecco logo.jpg" alt="Stambecco" style="width: 20%; min-width: 250px; display: block; margin: auto; border-radius: 140px;">
</p>

# 🦌 Stambecco: Italian Instruction-Following LLaMA Model

[![Data License](https://img.shields.io/badge/Data%20License-CC%20BY--NC--SA%204.0-orange.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Hugging Face Models](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Models-blue)](https://huggingface.co/mchl-labs)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mchl-labs/stambecco/blob/main/notebooks/Stambecco_chat.ipynb)

**Stambecco** is an Italian instruction-following language model family based on Meta's LLaMA architecture. Fine-tuned using **Low-Rank Adaptation (LoRA)**, Stambecco presents the first attempt to use `GPT-4` generated data to bring instruction-following capabilities to the Italian language across 7B and 13B parameter sizes, all built and trainable within Google Colab.

---

## 🚀 Models & Resources

Because original LLaMA foundation weights are restricted, we release the trained **PEFT/LoRA adapter weights** ("patches") and the corresponding translated instruction datasets on Hugging Face:

### 🤖 Models

| Model | Base Architecture | Dataset Used | Adapter Weights |
| :--- | :--- | :--- | :--- |
| **Stambecco-7B-Plus** | LLaMA-7B | Stambecco-Plus (GPT-4) | [`mchl-labs/stambecco-7b-plus`](https://huggingface.co/mchl-labs/stambecco-7b-plus) |
| **Stambecco-13B-Plus** | LLaMA-13B | Stambecco-Plus (GPT-4) | [`mchl-labs/stambecco-13b-plus`](https://huggingface.co/mchl-labs/stambecco-13b-plus) |

### 📊 Datasets

| Dataset | Base Source | Target Language | Repository |
| :--- | :--- | :--- | :--- |
| **Stambecco-Cleaned** | Alpaca-Data-Cleaned | Italian (`it`) | [`mchl-labs/stambecco_data_it`](https://huggingface.co/datasets/mchl-labs/stambecco_data_it) |
| **Stambecco-Plus** | Alpaca GPT-4 | Italian (`it`) | [`mchl-labs/stambecco_data_plus_it`](https://huggingface.co/datasets/mchl-labs/stambecco_data_plus_it) |

---

## 📌 Dataset Construction & Lineage

To advance Italian instruction tuning, Stambecco relies on two distinct translated datasets:

1. **Stambecco-Cleaned:** Derived from the community-curated [Alpaca-Data-Cleaned](https://github.com/gururise/AlpacaDataCleaned) dataset to remove hallucinated and noisy outputs from the original Stanford release.
2. **Stambecco-Plus (GPT-4):** Derived from [GPT-4-LLM](https://github.com/Instruction-Tuning-with-GPT-4/GPT-4-LLM), utilizing GPT-4 generated instruction responses for superior reasoning, vocabulary, and generation quality in Italian.

Translation pipelines were executed using OpenAI's `gpt-3.5-turbo`, balancing cost-efficiency and output quality, with custom programmatic heuristics applied (e.g., preserving code snippets untranslated).

---

## ⚙️ Training Details

Stambecco models were fine-tuned using Hugging Face's [`PEFT`](https://github.com/huggingface/peft) library (LoRA). To run the finetuning on Colab, on top of LLaMA-7B and LLaMA-13B, it is recommended an A100 40GB GPU.

* **Base Models:** LLaMA-7B and LLaMA-13B
* **Methodology:** Low-Rank Adaptation (LoRA)
* **Compute:** Single GPU fine-tuning (trainable within hours)

*For detailed hyperparameter configurations, please refer to the individual model cards on Hugging Face.*

---

## 💻 Quickstart & Inference

You can test and interact with Stambecco models directly in your browser or run local inference through a Gradio interface using our Google Colab notebook:

<p align="center">
  <a href="https://colab.research.google.com/github/mchl-labs/stambecco/blob/main/notebooks/Stambecco_chat.ipynb" target="_blank">
    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" height="32">
  </a>
</p>

---

## 📜 Citations

If Stambecco models or code inspire or assist your research, please include a formal citation:

```bibtex
@misc{stambecco,
  author       = {Michael Rottoli},
  title        = {Stambecco: Italian Instruction-following LLaMA Model},
  year         = {2023},
  publisher    = {GitHub},
  howpublished = {\url{https://github.com/mchl-labs/stambecco}}
}
```

If you use the Stambecco datasets in your work, please cite them in your formal paper bibliography (rather than as footnotes) to ensure proper academic indexing:

```bibtex
@misc{stambecco_cleaned_2023,
  author       = {Michael Rottoli},
  title        = {Stambecco-Cleaned: Italian Instruction-Tuning Dataset},
  year         = {2023},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/mchl-labs/stambecco_data_it}}
}
```

```bibtex
@misc{stambecco_plus_2023,
  author       = {Michael Rottoli},
  title        = {Stambecco Plus: Premium Italian Instruction-Tuning Dataset},
  year         = {2023},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/datasets/mchl-labs/stambecco_data_plus_it}}
}
```

## Base Works & Reference Citations

```bibtex
@article{touvron2023llama,
  title={LLaMA: Open and Efficient Foundation Language Models},
  author={Touvron, Hugo and Lavril, Thibaut and Izacard, Gautier and Martinet, Xavier and Lachaux, Marie-Anne and Lacroix, Timoth{\'e}e and Rozi{\`e}re, Baptiste and Goyal, Naman and Hambro, Eric and Azhar, Faisal and Rodriguez, Aurelien and Joulin, Armand and Grave, Edouard and Lample, Guillaume},
  journal={arXiv preprint arXiv:2302.13971},
  year={2023}
}

@misc{selfinstruct,
  title={Self-Instruct: Aligning Language Model with Self Generated Instructions},
  author={Wang, Yizhong and Kordi, Yeganeh and Mishra, Swaroop and Liu, Alisa and Smith, Noah A. and Khashabi, Daniel and Hajishirzi, Hannaneh},
  journal={arXiv preprint arXiv:2212.10560},
  year={2022}
}

@misc{alpaca,
  author = {Rohan Taori and Ishaan Gulrajani and Tianyi Zhang and Yann Dubois and Xuechen Li and Carlos Guestrin and Percy Liang and Tatsunori B. Hashimoto},
  title = {Stanford Alpaca: An Instruction-following LLaMA model},
  year = {2023},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/tatsu-lab/stanford_alpaca}}
}

@article{peng2023gpt4llm,
  title={Instruction Tuning with GPT-4},
  author={Baolin Peng and Chunyuan Li and Pengcheng He and Michel Galley and Jianfeng Gao},
  journal={arXiv preprint arXiv:2304.03277},
  year={2023}
}

@misc{hu2021lora,
  title={LoRA: Low-Rank Adaptation of Large Language Models},
  author={Hu, Edward and Shen, Yelong and Wallis, Phil and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Lu and Chen, Weizhu},
  year={2021},
  eprint={2106.09685},
  archivePrefix={arXiv},
  primaryClass={cs.CL}
}

@inproceedings{wolf-etal-2020-transformers,
  title = "Transformers: State-of-the-Art Natural Language Processing",
  author = "Thomas Wolf and Lysandre Debut and Victor Sanh and Julien Chaumond and Clement Delangue and Anthony Moi and Pierric Cistac and Tim Rault and Rémi Louf and Morgan Funtowicz and Joe Davison and Sam Shleifer and Patrick von Platen and Clara Ma and Yacine Jernite and Julien Plu and Canwen Xu and Teven Le Scao and Sylvain Gugger and Mariama Drame and Quentin Lhoest and Alexander M. Rush",
  booktitle = "Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations",
  month = oct,
  year = "2020",
  address = "Online",
  publisher = "Association for Computational Linguistics",
  url = "https://www.aclweb.org/anthology/2020.emnlp-demos.6",
  pages = "38--45"
}

@misc{peft,
  title = {PEFT: State-of-the-art Parameter-Efficient Fine-Tuning methods},
  author = {Sourab Mangrulkar and Sylvain Gugger and Lysandre Debut and Younes Belkada and Sayak Paul},
  howpublished = {\url{https://github.com/huggingface/peft}},
  year = {2022}
}

```

## 🙏 Acknowledgments

> "If I have seen further it is by standing on the shoulders of Giants."
> — Isaac Newton

This project was made possible through the foundational contributions of the open-source and AI research communities: [LLaMA](https://ai.meta.com/blog/large-language-model-llama-meta-ai/), [Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca), [Alpaca-LoRA](https://github.com/tloen/alpaca-lora), [Cabrita](https://github.com/22-hours/cabrita), [Cleaned Alpaca Dataset](https://github.com/gururise/AlpacaDataCleaned), [GPT-4-LLM](https://github.com/Instruction-Tuning-with-GPT-4/GPT-4-LLM), [Alpaca-LoRA-Serve](https://github.com/deep-diver/Alpaca-LoRA-Serve), [OpenAI](https://openai.com/), and [Hugging Face](https://huggingface.co/).


## ⚖️ Usage, License & Disclaimer

- License: Datasets are released under the CC BY-NC-SA 4.0 license (non-commercial, research use only).
- Model Restrictions: Stambecco models are intended strictly for academic research. Commercial use is prohibited in compliance with LLaMA's foundational release terms and OpenAI's Terms of Use.
- Safety Disclaimer: Model outputs may occasionally produce biased, inaccurate, or inappropriate content. Use with caution for research evaluation.
