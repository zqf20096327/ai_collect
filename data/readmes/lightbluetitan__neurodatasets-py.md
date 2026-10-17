# neurodatasets

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

The `neurodatasets` package provides a curated collection of neuroscience and brain-related datasets 
for data analysis, statistical modeling, and machine learning research. Includes biomedical voice recordings, MRI brain imaging, 
Alzheimer's and Parkinson's disease biomarkers, epilepsy seizures, ADHD symptoms, dopamine and serotonin measurements, 
cognitive impairment, brain size across species, sleep studies, PTSD, migraine treatment, and more from curated R packages on CRAN.

## Installation
You can install the `neurodatasets` package from PyPI:
```bash
pip install neurodatasets
```

## Usage
```python

import neurodatasets as nd

# List all available datasets

datasets = nd.list_datasets()
print(datasets)

# Load a specific dataset

df = nd.load_dataset('encephalitis_herpes')
print(df.head())

# Describe dataset

df_01 = nd.describe('sleep_study_college')
print(df_01)

```

## 📊 Some Available Datasets

| Dataset | Description | 
|---------|-------------|
| `gray_matter_patterns` | This dataset contains expected patterns of gray matter derived from large-scale meta-analyses by the ENIGMA consortium.| 
| `white_matter_patterns` | This dataset contains expected patterns of white matter derived from large-scale meta-analyses by the ENIGMA consortium.| 
| `encephalitis_herpes` | This dataset contains cases of herpes encephalitis in children observed in Bavaria and Lower Saxony between 1980 and 1993.| 
| `sleep_study_college` | This dataset contains data on sleep patterns and academic performance for college students.| 
| `alzheimer_smoking` | This dataset contains smoking history and disease classification from a case-control study on Alzheimer's disease.| 
| `brain_size_iq` | This dataset contains brain size, IQ scores and gender data from psychology students for intelligence research.| 
| `mammal_brains` | This dataset contains brain weight, body weight, gestation length and litter size across 96 mammal species.| 
| `chimp_brains` | This dataset contains Brodmann's area 44 asymmetry measurements in chimpanzees by sex.| 


> Run `neurodatasets.list_datasets()` or `nd.list_datasets()` (using `nd` as alias) to see the full list of available datasets.

## Disclaimer

The datasets included in `neurodatasets` are provided strictly for educational,
research, and informational purposes. All datasets originate from curated R packages
available on CRAN and retain their original licenses and attributions.

The author of `neurodatasets` makes no warranties, express or implied, regarding
the accuracy, completeness, or suitability of any dataset for a particular purpose.
Users are solely responsible for ensuring that their use of these datasets complies
with applicable laws, regulations, and ethical guidelines.

Any findings, conclusions, or decisions derived from the use of these datasets
are the sole responsibility of the user. The author shall not be held liable for
any direct, indirect, incidental, or consequential damages arising from the use
or misuse of the datasets included in this library.

For clinical, diagnostic, or medical decision-making purposes, always consult
qualified healthcare professionals.


## License

The `neurodatasets` library is released under the **GPL-3.0**, which allows free use, 
modification, and distribution, provided that any derivative work is also released 
under the same GPL-3.0 license. See the [LICENSE](LICENSE) file for details.