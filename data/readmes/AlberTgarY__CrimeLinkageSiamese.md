<div align="center">
<h1>Enhancing Binary Encoded Crime Linkage Analysis Using Siamese Network</h1>

<a href="https://ojs.aaai.org/index.php/AAAI/article/view/41309" target="_blank" rel="noopener noreferrer">
  <img src="https://img.shields.io/badge/AAAI%20Conference%20on%20Artificial%20Intelligence-2026-blue" alt="AAAI 2026">
</a>
<a href="https://ojs.aaai.org/index.php/AAAI/article/view/41309"><img src="https://img.shields.io/badge/DOI-AAAI.v40i1.41309-orange" alt="DOI"></a>
<a href="https://www.aaai.org"><img src="https://img.shields.io/badge/Track-AI%20for%20Social%20Impact-green" alt="AI for Social Impact"></a>
<a href="https://github.com/AlberTgarY/CrimeLinkageSiamese"><img src="https://img.shields.io/badge/Code-GitHub-black" alt="GitHub"></a>

**Imperial College London** | **University of Birmingham** | **University of Leicester** | **UK National Crime Agency**

[Yicheng Zhan](https://albertgary.github.io/)<sup>1</sup>, Fahim Ahmed<sup>1</sup>, Amy Burrell<sup>2</sup>, Matthew Tonkin<sup>3</sup>, Sarah Galambos<sup>4</sup>, [Jessica Woodhams](https://www.birmingham.ac.uk/staff/profiles/psychology/woodhams-jessica)<sup>2</sup>, [Dalal Alrajeh](https://www.doc.ic.ac.uk/~da04/)<sup>1</sup>

<sup>1</sup>Imperial College London, <sup>2</sup>University of Birmingham, <sup>3</sup>University of Leicester, <sup>4</sup>UK National Crime Agency

</div>

```bibtex
@article{zhan2026enhancing,
  author  = {Zhan, Yicheng and Ahmed, Fahim and Burrell, Amy and Tonkin, Matthew and Galambos, Sarah and Woodhams, Jessica and Alrajeh, Dalal},
  title   = {Enhancing Binary Encoded Crime Linkage Analysis Using Siamese Network},
  journal = {Proceedings of the AAAI Conference on Artificial Intelligence},
  volume  = {40},
  number  = {46},
  pages   = {39576--39584},
  year    = {2026},
  month   = mar,
  doi     = {10.1609/aaai.v40i46.41309},
  url     = {https://ojs.aaai.org/index.php/AAAI/article/view/41309}
}
```

## Overview

We propose a Siamese Autoencoder framework for crime linkage analysis that learns meaningful latent representations from high-dimensional, sparse, binary-encoded crime data. Using the Violent Crime Linkage Analysis System (ViCLAS) dataset from the UK National Crime Agency, our approach integrates geographic-temporal features at the decoder stage to amplify behavioral representations, achieving up to **9% AUC improvement** over traditional methods.

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/AlberTgarY/CrimeLinkageSiamese.git
cd CrimeLinkageSiamese
pip install torch numpy pandas scikit-learn tqdm openpyxl matplotlib --break-system-packages
```

**Requirements:**

- Python 3.8+
- PyTorch 1.9+
- 16GB RAM minimum (32GB recommended)

## Quick Start

### Training

Train the Siamese Autoencoder on your crime linkage dataset:

```python
import pandas as pd
from Utils import EuclideanDistance
from train import evaluate_siamese

# Load data
df = pd.read_csv("your_crime_data.csv", index_col="VA_ID")

# Train model
evaluate_siamese(
    df,
    behaviours_list=None,      # Use all behavioral features
    contexts_list=None,         # Use all contextual features
    euclidean_distance=EuclideanDistance(),
    split_mode="random",
    num_epochs=2,
    batch_size=128,
    learning_rate=1e-3,
    weight_recon=1e4,
    repeat=1,
    data="all",
    name="siamese_model",
    dir_geo=None,               # Optional: path to geographic-temporal data
    device="cuda"               # or "cpu"
)
```

### Testing

Evaluate a trained model:

```python
from test import test_siamese

# Test model
test_siamese(
    df,
    behaviours_list=None,
    contexts_list=None,
    model_path="map5.pt",       # Path to trained model
    data="all",
    device="cuda",
    name="map5_evaluation"
)
```


## Geographic-Temporal Integration

To incorporate geographic-temporal features:

```python
# Process geographic-temporal data
from geo_loader import GeoDataSaver

saver = GeoDataSaver("path/to/geo_data.csv")
saver.save_pt("output/directory/")

# Train with geo-temporal integration
evaluate_siamese(
    df,
    ...,
    dir_geo="path/to/geo_directory",  # Enable decoder-stage integration
    device="cuda"
)
```

## Data Access

**Important:** Due to strict confidentiality and data-sharing agreements with the UK National Crime Agency, the ViCLAS dataset cannot be publicly shared.

**Requesting Access:**

Researchers interested in accessing ViCLAS data should:

1. Submit a formal data access request to the Serious Crime Analysis Section (SCAS) of the UK National Crime Agency
2. Provide detailed research proposals outlining intended use
3. Comply with all ethical requirements and data protection regulations
4. Obtain necessary institutional approvals

**Contact:** UK National Crime Agency, Serious Crime Analysis Section
**Website:** https://www.nationalcrimeagency.gov.uk/

Access to the data used in this research was granted through requests R123, R128, R182a, and R182b.

## Ethics Statement

This research implements safeguards for responsible deployment:

- **Human-in-the-Loop:** System supports, not replaces, investigative decision-making
- **Routine Bias Audits:** Continuous monitoring for demographic/geographic disparities
- **Transparent Evaluation:** Clear communication of performance, assumptions, and limitations
- **Continuous Adaptation:** Periodic retraining to address temporal distribution shifts

This approach aligns with the **National Police Chiefs' Council Covenant for Using AI in Policing**.

## Acknowledgments

This research was partially supported by funding from the National Crime Agency, UK. We thank the analysts from the Serious Crime Analysis Section at the National Crime Agency for their valuable assistance with data preparation and insightful feedback.

## License

This code is provided for **academic research purposes only**. Commercial use requires explicit permission from the authors and the UK National Crime Agency.

## Contact

For questions about the code or methodology:

- **Dalal Alrajeh:** dalal.alrajeh04@imperial.ac.uk

For data access inquiries, please contact the UK National Crime Agency directly.
