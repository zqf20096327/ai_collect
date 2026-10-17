# 3D DenseNet ensemble for Alzheimer's classification

Code and weights for [3D DenseNet Ensemble in 4-Way Classification of Alzheimer's Disease](https://doi.org/10.1007/978-3-030-59277-6_8) (Brain Informatics, BI 2020).

Three 3D DenseNet-121 models classify T1 MRI scans as CN, AD, EMCI or LMCI, and the ensemble averages their outputs.

| Model | Growth rate | First conv | Val accuracy |
|---|---|---|---|
| `c1` | 32 | 3×3×3 | 53.3% |
| `c2` | 22 | 7×7×7 | 57.5% |
| `c3` | 28 | 7×7×7 | 66.7% |
| Ensemble | | | 83.3% |

## Quick start

```bash
pip install -r requirements.txt
python evaluate.py      # accuracy of each model and the ensemble
python train.py c1      # retrain one model, saved to model_weights/
```

Tested with Python 3.12 and torch 2.14. A GPU is used if available.

## Data

The scans come from [ADNI](https://adni.loni.usc.edu) and can't be redistributed, so you need your own ADNI account.
The paper used 600 preprocessed T1 scans from ADNI2 and ADNIGO, 150 per class.

Put them in `NiFTiFiles/` named `<class>_<n>.nii`, for example `EMCI_42.nii`, and run:

```bash
python make_splits.py NiFTiFiles/
```

## Files

| File | Contents |
|---|---|
| `densenet3d.py` | Model and the three configs |
| `data.py` | Dataset and scan loading |
| `train.py`, `evaluate.py` | Training and evaluation |
| `make_splits.py`, `splits.csv` | The 80/20 train/val split, with each scan's ADNI subject ID |
| `model_weights/` | Trained weights from the paper |
| `notebooks/` | The original notebooks, with outputs |

## Notes

- The split is by scan, not by subject, as in the paper. Most subjects have several scans, so train and val share subjects.
- There is no separate test set. The best epoch is picked on val.
- The published weights were trained on an earlier split that can't be recovered, so `evaluate.py` with them is not a held-out score.

## Credits

The model is adapted from [3D-ResNets-PyTorch](https://github.com/kenshohara/3D-ResNets-PyTorch) and the data loading from [cnn-interpretability](https://github.com/jrieke/cnn-interpretability).

## Citation

See `CITATION.cff`.
