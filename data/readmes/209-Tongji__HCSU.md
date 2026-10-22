---
language:
- zh
- en
license: cc-by-nc-4.0
size_categories:
- 10K<n<100K
task_categories:
- image-classification
- image-to-text
pretty_name: 'HCSU: Fine-Grained Historical Calligraphy Style Understanding Dataset and Benchmark'
tags:
- image
- calligraphy
- chinese-calligraphy
- historical-documents
- fine-grained-recognition
- cultural-heritage
- style-understanding
---

# HCSU: A Dataset and Benchmark for Fine-Grained Historical Calligraphy Style Understanding

<div align="center">

[![Paper](https://img.shields.io/badge/Paper-PDF-red.svg)](https://arxiv.org/abs/2607.04147)
[![DOI](https://img.shields.io/badge/DOI-10.1007%2F978--3--032--37461--5__5-blue.svg)](https://doi.org/10.1007/978-3-032-37461-5_5)
[![GitHub](https://img.shields.io/badge/GitHub-209--Tongji%2FHCSU-black.svg?logo=github)](https://github.com/209-Tongji/HCSU)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Dataset-blue.svg)](https://huggingface.co/datasets/Tongji209/HCSU)
[![ModelScope](https://img.shields.io/badge/ModelScope-Dataset-624AFF.svg)](https://www.modelscope.cn/datasets/Tongji209/HCSU_Fine-Grained_Historical_Calligraphy_Style_Understanding_Dataset)
[![Code License](https://img.shields.io/badge/Code%20License-Apache_2.0-green.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![Data License](https://img.shields.io/badge/Data%20License-CC%20BY--NC_4.0-yellow.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

<p><strong>ECCV 2026</strong></p>
<p>Yinsheng Yao<sup>*</sup>, Yan Liu<sup>*</sup>, Chen Ye<sup>†</sup></p>
<p><sup>*</sup> Equal contribution. <sup>†</sup> Corresponding author.</p>

</div>

This repository provides the HCSU dataset documentation and HCSU-Bench evaluation code for fine-grained historical calligraphy style understanding.

## Dataset Access

The HCSU dataset is available through the following channels:

- Hugging Face: https://huggingface.co/datasets/Tongji209/HCSU
- ModelScope: https://www.modelscope.cn/datasets/Tongji209/HCSU_Fine-Grained_Historical_Calligraphy_Style_Understanding_Dataset

## Repository Structure

- [Dataset](./Dataset/README.md): dataset overview, annotation schema, data processing pipeline, and dataset release notes.
- [Benchmark](./Benchmark/README.md): HCSU-Bench evaluation protocols, leaderboard, and implementation entry points.

Chinese documentation is available in [Dataset/README-ch.md](./Dataset/README-ch.md) and [Benchmark/README-ch.md](./Benchmark/README-ch.md).

## Publication

- **Paper:** [HCSU: A Dataset and Benchmark for Fine-Grained Historical Calligraphy Style Understanding](https://link.springer.com/chapter/10.1007/978-3-032-37461-5_5)
- **DOI:** [10.1007/978-3-032-37461-5_5](https://doi.org/10.1007/978-3-032-37461-5_5)
- **Published:** 25 September 2026
- **Proceedings:** *Computer Vision – ECCV 2026*, Lecture Notes in Computer Science, vol. 17025
- **Publisher:** Springer, Cham
- **ISBN:** 978-3-032-37461-5 (online); 978-3-032-37460-8 (print)

## Citation

If you use HCSU, HCSU-Bench, or find this work helpful, please cite:

```bibtex
@inproceedings{hcsu2026,
  title={HCSU: A Dataset and Benchmark for Fine-Grained Historical Calligraphy Style Understanding},
  author={Yao, Yinsheng and Liu, Yan and Ye, Chen},
  editor={Favaro, Paolo and Kukelova, Zuzana and Maki, Atsuto and Rohrbach, Anna and Schindler, Konrad and Tombari, Federico},
  booktitle={Computer Vision -- ECCV 2026},
  series={Lecture Notes in Computer Science},
  volume={17025},
  publisher={Springer},
  address={Cham},
  year={2026},
  doi={10.1007/978-3-032-37461-5_5},
  url={https://doi.org/10.1007/978-3-032-37461-5_5},
  isbn={978-3-032-37461-5}
}
```

## License

This repository uses separate licenses for code and data:

- **Code, scripts, and repository documentation:** [Apache License 2.0](./LICENSE).
- **Dataset images, archives, annotations, samples, prompts, evaluation data, and dataset-derived visual assets:** [Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](./DATA_LICENSE).

The dataset and benchmark data assets are provided for academic and non-commercial research use. Commercial use requires separate permission from the rights holders.
