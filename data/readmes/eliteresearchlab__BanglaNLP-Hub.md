# BanglaNLP Hub

A community-maintained catalog of Bangla / Bengali NLP papers, datasets, models,
tools, and benchmarks.

[Browse the catalog](https://eliteresearchlab.github.io/BanglaNLP-Hub/) · [Hugging Face dataset](https://huggingface.co/datasets/kishormorol/bangla-nlp-catalog) · [DOI](https://doi.org/10.5281/zenodo.22798635)

## Overview

BanglaNLP Hub helps researchers, students, and developers find resources for working
with Bangla. Search the catalog or browse by task to find papers, datasets, models,
and tools. Each entry links to its original source, making it easier to check the
details and choose what to use.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/screenshots/dark.webp">
  <img src="docs/screenshots/light.webp" alt="The BanglaNLP Hub home page, with Bangladesh river artwork behind a bilingual heading and the catalog search">
</picture>

## Run locally

Requires Node.js 22.23.4 or newer. Built with Astro, TypeScript, and vanilla JavaScript.

```sh
npm install
npm run dev
```

The development server runs at `localhost:4321`.

| Command | Action |
| --- | --- |
| `npm run build` | Build to `dist/` |
| `npm run preview` | Preview the production build |
| `npm run validate` | Validate catalog data |
| `npm run check-links` | Check published resource links |

## Shareable filters

Copy the address bar URL to share a filtered catalog view. Datasets accepts `q`,
`task`, `license`, and `year`; Papers accepts `q`, `task`, `venue`, and `year`.
For example: `/BanglaNLP-Hub/datasets?task=sentiment&license=open` or
`/BanglaNLP-Hub/papers?q=BanglaBERT&venue=ACL`.
Select values must match an option's value. Dataset license values are `open`,
`nc`, `research`, and `other` (Other / restricted). Unknown select values are
ignored; repeated parameters use the first value. Empty filters are removed from
the URL. Filter text is limited to 1,000 characters, including when read from a URL,
to keep shared addresses bounded.

License filters group the catalog's license text; they do not verify or certify a
dataset's license. Labels restricting commercial use and research labels take precedence. `open`
matches only MIT, Apache 2.0, CC0, ODC-BY, CC BY 4.0, and CC BY-SA 4.0.
All other text, including ND, Mixed, GPL/AGPL, and unknown labels, falls under `other`.
WikiANN's `ODC-By; research use only` label belongs to `research`, not `open`.
License sources and pending checks are documented in [`TODO-data.md`](./TODO-data.md).

Typing replaces the current history entry. Select changes and **Clear filters**
add an entry when the URL changes, so Back and Forward restore those views.
Other query parameters and resource hashes are kept. Initial loads, copied URLs,
reloads, and Back/Forward preserve explicit filters even when a retained resource
hash points to a hidden item. Hidden targets are not revealed or focused on load;
visible hash targets still open normally. Only explicit hash navigation after
load, including selecting the same hash again through search, can clear conflicting
filters to reveal a target. Without JavaScript, both pages show their full lists.

## Data honesty

The catalog is only useful if its contents are true, so the project holds a hard line:

- **No invented values.** Scores, citation counts, and BibTeX entries are never synthesised. A missing field is omitted and the UI hides the affected element.
- **Leaderboards stay empty until sourced.** Each benchmark carries a real dataset and metric, and a score row appears only with a citation to the paper it came from. B-REASO and BanglaRQA are populated, with four cited rows on BanglaRQA; the rest render a "No leaderboard curated yet" empty state rather than a plausible-looking number.
- **Links are checked.** Every published `link:` URL is verified nightly. Unverified `data/inbox/` candidates are excluded. Dead links are reported in a single tracking issue; entries are never removed automatically.
- **Entries get verified by hand.** Papers have been audited against the ACL Anthology, arXiv, and OpenAlex (title, authors, and abstract), and their task assignments are being spot-checked and corrected. Several entries inherited from the original design prototype turned out to be fabricated — a duplicate under an invented title, a model that does not exist, a paper with no publication — and were removed.

Known gaps are tracked in [`TODO-data.md`](./TODO-data.md): 1 dataset lacks BibTeX, SNLTR, and nine of the eleven leaderboards await rows.

Canonical BibTeX may come from ACL Anthology, arXiv, a publisher export, or an
official Crossref or DataCite export of registered metadata. Both
[Crossref](https://www.crossref.org/documentation/retrieve-metadata/content-negotiation/)
and [DataCite](https://support.datacite.org/docs/datacite-content-resolver) support
DOI content negotiation with `Accept: application/x-bibtex`. These registry
exports are canonical sources, not handcrafted citations. Preserve every exported
field and document the paper or release association in `TODO-data.md`; a citation
does not verify the dataset's other metadata.

**Dataset fields are verified at the source.** `license`, `size`, and `year` each had an audit pass in July 2026. Datasets added from resource papers use license and size statements from their own repository or card. A paper's license describes the paper. Corrections and entries without a confirmed figure are listed in `TODO-data.md`. Candidate datasets with unverifiable licenses or outside the current scope are held back rather than published.

A September 2026 audit replaced BHS's unsupported 30,000 count with 3,418 labelled statements in v1.0 and checked SentNoB, FLORES-200, TyDi QA, and WikiANN against pinned releases. BHS retains MIT from the original repository license, with that attribution in its description. WikiANN records both original release clauses as `ODC-By; research use only` while retaining its balanced split details. Pinned evidence and version scope are recorded in `TODO-data.md`. These labels report the sources without deciding their legal effect.

## Contribute

Entries live in YAML under [`data/`](./data). To suggest a resource,
[open an issue with its link](https://github.com/eliteresearchlab/BanglaNLP-Hub/issues/new?template=submit-resource.yml)
or follow [CONTRIBUTING.md](./CONTRIBUTING.md) and submit a PR.

**Only add information you can source.** Leave unknown fields out. Never invent
scores, counts, or BibTeX. Run `npm run validate` before submitting.

See [TODO-data.md](./TODO-data.md) for open data work and
[CONTRIBUTORS.md](./CONTRIBUTORS.md) for resource contributors.

## License

Site code is [MIT](./LICENSE). Linked resources have their own licenses.
Third-party notices and font licenses are retained in [`docs/`](./docs).
