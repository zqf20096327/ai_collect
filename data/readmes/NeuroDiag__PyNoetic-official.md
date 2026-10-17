<div align="center">
  <img src="https://github.com/NeuroDiag/PyNoetic-official/assets/62457915/4c6aa260-66b5-4859-8c2e-5294ebf28fcc" width=60% />

  **A Modular Python Framework for No-Code Development of EEG Brain-Computer Interfaces**
</div>

-----------------

  <a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/python-3.8%20|%203.9%20|%203.10|%203.12-blue"></a>
  <a href="https://neurodiag.github.io/PyNoetic/"><img alt="Project" src="https://img.shields.io/badge/-Project%20Page-lightgrey?logo=Google%20Chrome&color=informational&logoColor=white"></a> 
  <a href="https://youtu.be/imYeke55XvA"><img alt="Tutorial" src="https://img.shields.io/badge/-Tutorial-ea3323?logo=youtube"></a> 
  <a href="https://github.com/NeuroDiag/PyNoetic-official/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-GPLv3-blue.svg"></a>
  ![](https://komarev.com/ghpvc/?username=aviralchharia&label=Visit+Counts&color=green)
  [![Citation](https://img.shields.io/badge/Citation-BibTeX-green)](https://github.com/NeuroDiag/PyNoetic-official/blob/main/citation)
  [![GitHub Stars](https://img.shields.io/github/stars/NeuroDiag/PyNoetic-official?style=social&cacheSeconds=60)](https://github.com/NeuroDiag/PyNoetic-official/stargazers)  
  ![Contributors](https://img.shields.io/badge/contributors-5-orange.svg)
  ![Repo size](https://img.shields.io/github/repo-size/NeuroDiag/PyNoetic-official)

This is the official PyTorch implementation of the paper *"PyNoetic: a Modular Python Framework for No-Code Development of EEG Brain-Computer Interfaces"* (PLOS ONE, 2025).

## :rocket:  :rocket: **Updates**
- ✅ **Jun. 26, 2025**: We released PyNoetic Codebase on GitHub.
- ✅ **Jun. 24, 2025**: PyNoetic accepted to PLoS One.

## :open_book: Introduction
<p align="center"><img src="docs/images/bci_workflow.png" width=60% /></p>

A fundamental challenge in the rapid development of BCI systems is the absence of comprehensive software solutions specifically tailored for advancing cognitive neuroscience experiments. Existing BCI frameworks suffer from critical limitations, including a lack of "stage-wise" flexibility crucial for experimental research, elevated costs stemming from reliance on proprietary software, and an absence of all-inclusive features leading to reliance on multiple softwares.

<p align="center"><img src="https://github.com/NeuroDiag/PyNoetic-official/assets/62457915/c2c2d481-db03-4d42-9adf-9f7630c04cc1" width=60% /></p>

We introduce PyNoetic- an end-to-end python framework that not only addresses these inherent limitations but also offers an extensive selection of methods, coupled with user-friendly compatibility for integrating novel algorithms at each developmental phase of a BCI system. PyNoetic offers a comprehensive suite of functions ranging from: stimuli presentation, data acquisition, channel selection techniques, filters, multiple feature extraction techniques, artifact removal, a wide array of analytical tools, brain-connectivity measures, ML classification models, data visualization, systematic testing via simulation, and evaluation of novel paradigms. To provide flexibility for research, the option to add custom functionality through scripting is provided for experienced users. PyNoetic exhibits versatility and suitability for both offline and real-time deployment of BCI systems.

## :hammer_and_wrench: Installation and Usage
To install the framework, clone the repository from Github and run the load.py file in the prototype folder. This should display a GUI on your screen.
```bash
git clone https://github.com/NeuroDiag/PyNoetic-official.git
python -m venv PyNoeticEnv
PyNoeticEnv/Scripts/activate
pip install -r requirements.txt
# You might need to use: sudo apt install libxcb==* for Linux
# For macOS : brew install labstreaminglayer/tap/lsl
cd gui
python load.py
```
Microsoft Visual C++ 14.0 or greater is required for advanced simulation functionality.

For MacOS, testing has been done with python 3.9.6 and a separate requirement.txt exists. 
Tested on both Ubuntu 22.04 and Windows 11 with python 3.12.4

### Sample Data
PyNoetic caters to both experienced programmers and those new to Python, expediting the experiment design process. This empowers researchers to concentrate on the intricate facets of BCI development, thus accelerating future research endeavors. The framework comes preloaded with some sample data for initial testing. The sample data was collected using Emotiv Epoc X and comprises of 14 channels AF3, F7, F3, FC5, T7, P7, O1, O2, P8, T8, FC6, F4, F8, AF4 with 02 references at P3, P4. PyNoetic loads the sample data by default.

### Adding your novel Machine Learning Classifier
The modularity of PyNoetic allows the users to add a novel/ custom machine learning classifier to the framework with a single line of code:
```python
# Navigate to ./gui/feature.py
cd gui
# Add a new function:
def custom_ml_classifier(self):
    X = self.data[:-1]
    Y = self.data[-1]
    ml_model = ml_classifier()  # Your custom ML function
    ml_model = ml_model.fit(X,Y)
    scores = cross_val_score(ml_model,X,Y)
    return scores
# Repeat the same for ./live_mode/feature.py to update live mode
```

### 🎮 Video Tutorial <sub><sup><sub>(click to watch the video)</sub></sup></sub>

<p align="center"> 
  <a href="https://youtu.be/imYeke55XvA" target="_blank" onclick="window.open('https://youtu.be/imYeke55XvA'); return true;">
  <img src="docs/images/PyNoetic.gif" alt="Demo" style="width: 75%;">
  </a>
</p>

## :abacus: Reposting Issues & Discussion Forum
To report a bug in the existing framework version, please open an issue. We are generally quick in responding and fixing issues/ bugs. Post any general questions/ request a new feature in PyNoetic's [Discussions Forum](https://github.com/NeuroDiag/PyNoetic-official/discussions).

## :e-mail: Contributors

<!-- Enable when public
<a href="https://github.com/NeuroDiag/PyNoetic-official/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=PyNoetic/PyNoetic"/>
</a> -->

PyNoetic was originally developed by [Gursimran Singh](https://www.linkedin.com/in/gursimran-singh-b590971a5/) (TIET), [Aviral Chharia](http://aviralchharia.github.io) (CMU), [Rahul Upadhyay](https://eced.thapar.edu/facultydetails/MTI0NQ) (TIET), [Vinay Kumar](https://eced.thapar.edu/facultydetails/MTIzNA) (TIET) and [Luca Longo](http://lucalongo.eu/about/about.html) (TU Dublin). Contribute to the toolbox and be featured here!

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=NeuroDiag/PyNoetic-official&type=Date)](https://www.star-history.com/#NeuroDiag/PyNoetic-official&Date)

## :scroll: License
PyNoetic is available under the GNU General Public License v3.0 See the [LICENSE](https://github.com/NeuroDiag/PyNoetic-official/blob/main/LICENSE) file for more details. For the supporting packages/ libraries on why PyNoetic is build, we acknowledge their individual Licenses.

## :bookmark_tabs: Citation
If you find our work useful for your project, please consider adding a star to this repository and citing the paper:
```bibtex
@article{singh2025pynoetic,
  title     =   {PyNoetic: a Modular Python Framework for No-Code Development of EEG Brain-Computer Interfaces}, 
  author    =   {Singh, Gursimran and Chharia, Aviral and Upadhyay, Rahul and Kumar, Vinay and Longo, Luca},
  journal   =   {PLoS One},
  year      =   {2025},
}
```

## Affiliations
[PyNoetic](https://neurodiag.github.io/PyNoetic/) is an open-source project supported by:
<p align="top">
    <img src="docs/images/Cognitive_Science_Computational_Intelligence_Lab.png" width="9%">    
    &nbsp;
    <img src="docs/images/logo_AICL_Labs.png" width="9.5%">
    &nbsp;
</p>

Developed by researchers affiliated with various leading universities.
<p align="top">
    <img src="docs/images/thapar.png" width="13.5%">
    &nbsp;
    <img src="docs/images/TUDublin.png" width="13.5%">
    &nbsp;
    <img src="docs/images/cmu_logo.png" width="32%">
</p>
