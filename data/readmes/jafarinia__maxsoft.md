# Navigating the MIL Trade-Off: Flexible Pooling for Whole Slide Image Classification 🌟
**NeurIPS 2025**  
**Authors:** Hossein Jafarinia, Danial Hamdi*, Amirhossein Alamdar*, Elahe Zahiri, Soroush Vafaie Tabar, Alireza Alipanah, Nahal Mirzaei, Saeed Razavi, Amir Najafi, Mohammad Hossein Rohban  
[[arXiv]](https://openreview.net/forum?id=RIL1vOuZOC) 📖

--- 

## Overview 📝
This repository provides a complete, runnable implementation of the paper "Navigating the MIL Trade-Off: Flexible Pooling for Whole Slide Image Classification." To reproduce the results presented in the paper, please follow each of the steps outlined below. Detailed explanations for each step are available in their respective README files.

### Steps to Reproduce Results 🔄
0. [Requirements](./requirements/readme.md)
1. [Download Each Dataset](./datasets/readme.md) 📥
2. [Break Slides into Patches](./CLAM/readme.md) 🛠️
3. [Fold and Split Each Dataset](./datasets/readme.md) 🔀
4. [Train SSL](./dino/readme.md) 🚀
5. [Extract Features](./NavMIL/readme.md) ✨
6. [Train MIL Models](./NavMIL/readme.md) 🏋️‍
7. [Citation](https://github.com/jafarinia/maxsoft#citation)

If you prefer not to train DINO from scratch, you can use the final weights or embeddings available here:

| Dataset    | Embedder Weights | Embeddings |
|------------|------------------|------------|
| CAMELYON16 | [weights](https://huggingface.co/Amirhosseinalamdar/NavMIL/resolve/main/weights/cm16/checkpoint0099.pth) | [Embeddings](https://huggingface.co/Amirhosseinalamdar/NavMIL/tree/main/embeddings/camelyon16_subset50) 🌐 |
| CAMELYON17 | [weights](https://huggingface.co/Amirhosseinalamdar/NavMIL/resolve/main/weights/cm17/checkpoint0099.pth) | [Embeddings](https://huggingface.co/Amirhosseinalamdar/NavMIL/tree/main/embeddings/camelyon17_annotatedset100) 🌟 |
| TCGA-LUNG  | [weights](https://huggingface.co/Amirhosseinalamdar/NavMIL/resolve/main/weights/tcga/checkpoint0099.pth) | [Embeddings](https://huggingface.co/Amirhosseinalamdar/NavMIL/tree/main/embeddings/tcga) 💭 |
| SICAP-MIL  | [weights](https://huggingface.co/Amirhosseinalamdar/NavMIL/resolve/main/weights/sicapmil/checkpoint0799.pth) | [Embeddings](https://huggingface.co/Amirhosseinalamdar/NavMIL/tree/main/embeddings/sicapmil) 🔍 |

---

## Visuals 📊
![Figure 1](figure.png)
Maxsoft pooling uses max pooling for the forward pass of Multiple Instance Learning (MIL) training, and the gradient of LSE (which is equivalent to Softmax) with a moderate temperature for the backward pass. This compensates for the non-differentiability of max pooling. For more details, please see Theorems 1 and 2 in the paper.

![Detection Heatmap](detection.png)

---

For any additional information or queries, feel free to reach out! Thank you for your interest in our work! 😊

## Acknowledgments
This codebase is built upon the work of Snuffy, DINO, and CLAM. We extend our gratitude to the authors for their valuable contributions.

## Citation

If you find our work helpful for your research, please consider giving a star to this repository and
citing the following BibTeX entry.

```bibtex
@inproceedings{jafarinia‌navigating,
  title={‌Navigating the MIL Trade-Off: Flexible Pooling for Whole Slide Image Classification},
  author={Jafarinia, Hossein and Hamdi, Danial and Alamdar, Amirhossein and Zahiri, Elahe and Tabar, Soroush Vafaie and Alipanah, Alireza and Mirzaie, Nahal and Razavi, Saeed and Najafi, Amir and Rohban, Mohammad Hossein},
  booktitle={The Thirty-ninth Annual Conference on Neural Information Processing Systems}
}
```

