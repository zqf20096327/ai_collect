## About

QCell is a collection of 525k quantum-mechanical calculations for (bio)molecular systems that go beyond small molecules and proteins (see [paper](https://doi.org/10.1088/3050-287X/ae5267)). It includes fragments of nucleic acids, lipids, and carbohydrates, as well as dimers and ion–water clusters, all computed at the PBE0+MBD(-NL) level of theory. The dataset is intended as a practical resource for training and benchmarking machine learning force fields.

The data can be downloaded from the [Zenodo repository](https://doi.org/10.5281/zenodo.18385612) in `.h5` or `.xyz` format. This repository provides conformer generation workflows in the `scripts/` directory; each subfolder contains a dedicated `README.md` describing the dataset construction and sampling protocols.

The MBD-CPA ratios were extracted from a modified version of DFTB+, available in the GitHub repository: [https://github.com/suadou/dftbplus](https://github.com/suadou/dftbplus).

| Type | Size | # Atoms | Elements | Geometries |
|:------|:------|:------|:-----------|:-----------|
| Nucleic acids  | 34,838 | 14–382 | H, C, N, O, Na, Mg, S, P | new, [ref](https://doi.org/10.1063/5.0094727), [ref](https://doi.org/10.1093/nar/gkad630), [ref](https://doi.org/10.48550/arXiv.2505.08762) |
| Lipids | 16,000 | 125–402 | H, C, N, O, P | new |
| Carbohydrates | 74,087 | 35–75 | H, C, N, O | new |
| Ions & water | 30,000 | 4–301 | H, O, Na, Cl, K, Mg, Ca | new |
| Non‑covalent dimers (DES370K) | 370,956 | 2–34 | 20 elements | [ref](https://doi.org/10.1038/s41597-021-00833-x) |
| **Total** | 525,881 | 2–402 | 20 elements |  |

## Citation

If you use recomputed or newly generated datasets from QCell, please cite:

```bibtex
@article{kabylda2026qcell,
  title={QCell: Comprehensive Quantum-Mechanical Dataset Spanning Diverse Biomolecular Fragments},
  author={Kabylda, Adil and Su{\'a}rez-Dou, Sergio and Davoine, Nils and Br{\"u}nig, Florian N and Tkatchenko, Alexandre},
  journal={AI for Science},
  volume={2},
  number={2},
  pages={025003},
  year={2026},
  publisher={IOP Publishing}
}
```
