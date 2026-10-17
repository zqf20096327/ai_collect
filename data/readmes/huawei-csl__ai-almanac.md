<p align="center">
  <a href="https://almanac.huawei-csl.com/">
    <img src="assets/banner.png" alt="The AI Almanac" width="100%">
  </a>
</p>

<p align="center">
  <a href="https://almanac.huawei-csl.com/"><img alt="Website" src="https://img.shields.io/badge/website-almanac.huawei--csl.com-d4622a?style=for-the-badge"></a>
  <a href="https://huggingface.co/datasets/huawei-csl/GitScholar"><img alt="Dataset on Hugging Face" src="https://img.shields.io/badge/%F0%9F%A4%97%20dataset-GitScholar-e5a52c?style=for-the-badge"></a>
  <a href="https://arxiv.org/abs/2609.26361"><img alt="Paper on arXiv" src="https://img.shields.io/badge/arXiv-2609.26361-a83f28?style=for-the-badge&logo=arxiv&logoColor=white"></a>
</p>

# 📖 Welcome to the official AI Almanac repository!

**[The AI Almanac](https://almanac.huawei-csl.com/)'s goal is to help researchers and the broader AI community get a clear, up-to-date view of the direction of AI research and how the field is evolving.**

It collects public information about new AI papers on arXiv and ranks them using signals from the academic world and GitHub. Beyond individual papers, it identifies and groups the ideas and methods they introduce, providing a higher-level view of which areas are growing and how the field is changing over time.

If you have found this website useful, please consider leaving a ⭐ on this repository! 

<p align="center">
  <a href="https://almanac.huawei-csl.com/"><img src="assets/screenshot-leaderboard.png" alt="The AI Almanac's leaderboard" width="100%"></a>
</p>

## Current Features

- 🏆 **[Leaderboard](https://almanac.huawei-csl.com/)**: the new AI papers posted to arXiv over the last week, month, quarter or year, ranked on what is known about them: early citations, author academic record, topic, textual features and GitHub activity. 
- 📈 **[Trends](https://almanac.huawei-csl.com/trends)**: how each research idea has grown over the last six months, year or two years, ranked by relative growth or by forecast. 

## Get involved

You are welcome to collaborate: don't hesitate to open an issue to request a new feature, suggest an improvement or report anything that looks wrong. Every feedback is useful, and you don't need to write code to contribute.

- 💡 **[Suggest an idea](../../issues/new?template=feature-request.yml)**: a view, a filter or a signal you would like to see.
- 🐛 **[Report a bug](../../issues/new?template=bug-report.yml)**: something on the site that does not work or display as it should.
- 💬 **[Join the discussion](../../discussions)**: questions, interpretations, and what you found this week.
- ✏️ **[Open any other issue](../../issues/new)**: Any other feedback or suggestion that you would like to give.

We maintain the website in our spare research time. We will do our best to address feature requests and bug reports, though we can't promise a fix or a timeline for each.

## The code

This repository also holds the site itself: the pages (React), the API (FastAPI over one read-only SQLite table) and the build that produces that table from each weekly release. [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) explains how the parts fit together, and [docs/DATA.md](docs/DATA.md) the data the build expects, which is not part of this repository. Pull requests are welcome.

<details>
<summary>Running and testing it locally</summary>

Requirements: Python 3.12 and Node 22.

```sh
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
(cd frontend && npm ci)

python build/build_papers_db.py --data-dir path/to/data   # writes backend/papers.sqlite
bash start.sh --dev                                       # the site on http://localhost:8101

python -m pytest                                          # the build and the backend
(cd frontend && npm run lint && npm run build)            # lints, type-checks and builds the site
```

</details>

## License

The code in this repository is released under the [BSD 3-Clause Clear License](LICENSE): you are free to use, modify and share it, keeping the copyright notice. It grants no patent rights. The fonts in `assets/src/fonts` keep their own [SIL Open Font License](https://openfontlicense.org).

## References

The AI Almanac is built on the [GitScholar dataset](https://huggingface.co/datasets/huawei-csl/GitScholar), which links arXiv AI papers to their citations and to the GitHub repositories that reference them. The dataset and its methodology are described in [*GitScholar: A Dataset for Predicting AI Research Impact from GitHub Engagement*](https://arxiv.org/abs/2609.26361).

If you have found the AI Almanac useful, please consider liking the [dataset on Hugging Face](https://huggingface.co/datasets/huawei-csl/GitScholar) and citing our paper or this website:

```bibtex
@article{guandalino2026gitscholar,
  title   = {GitScholar: A Dataset for Predicting AI Research Impact from GitHub Engagement},
  author  = {Guandalino, Emilien and Müller, Lorenz K. and Motetti, Beatrice Alessandra
             and Berestizshevsky, Konstantin and Cavigelli, Lukas},
  journal = {arXiv preprint arXiv:2609.26361},
  year    = {2026},
  url     = {https://arxiv.org/abs/2609.26361}
}

@misc{guandalino2026almanac,
  title   = {The AI Almanac},
  author  = {Guandalino, Emilien and Müller, Lorenz K. and Motetti, Beatrice Alessandra
             and Berestizshevsky, Konstantin and Cavigelli, Lukas},
  year    = {2026},
  url     = {https://almanac.huawei-csl.com/}
}
```

<details>
<summary>Citing the Semantic Scholar data</summary>

The paper and author data from Semantic Scholar is used under the [ODC-BY license](https://opendatacommons.org/licenses/by/1.0/). If you use it, please also cite the [Semantic Scholar Open Data Platform](https://arxiv.org/abs/2301.10140):

```bibtex
@misc{kinney2023semantic,
  title     = {The Semantic Scholar Open Data Platform},
  author    = {Kinney, Rodney and Anastasiades, Chloe and Authur, Russell and Beltagy, Iz and Bragg, Jonathan and Buraczynski, Alexandra and Cachola, Isabel and Candra, Stefan and Chandrasekhar, Yoganand and Cohan, Arman and Crawford, Miles and Downey, Doug and Dunkelberger, Jason and Etzioni, Oren and Evans, Rob and Feldman, Sergey and Gorney, Joseph and Graham, David and Hu, Fangzhou and Huff, Regan and King, Daniel and Kohlmeier, Sebastian and Kuehl, Bailey and Langan, Michael and Lin, Daniel and Liu, Haokun and Lo, Kyle and Lochner, Jaron and MacMillan, Kelsey and Murray, Tyler and Newell, Chris and Rao, Smita and Rohatgi, Shaurya and Sayre, Paul and Shen, Zejiang and Singh, Amanpreet and Soldaini, Luca and Subramanian, Shivashankar and Tanaka, Amber and Wade, Alex D. and Wagner, Linda and Wang, Lucy Lu and Wilhelm, Chris and Wu, Caroline and Yang, Jiangjiang and Zamarron, Angele and Van Zuylen, Madeleine and Weld, Daniel S.},
  publisher = {arXiv},
  year      = {2023},
  doi       = {10.48550/ARXIV.2301.10140},
  url       = {https://arxiv.org/abs/2301.10140}
}
```

</details>

The AI Almanac builds on data and infrastructure provided by the wider research community. We are grateful to the teams behind [arXiv](https://arxiv.org), [Semantic Scholar](https://www.semanticscholar.org), and [GitHub](https://github.com), and to the researchers who make their work and code publicly available.
