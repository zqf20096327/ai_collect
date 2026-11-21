<div align="center">
  <img src="assets/genesis-logo.png" width="88" alt="Genesis Molecular AI">
  <h1 align="center">GenesisPotency-2026</h1>
</div>

<div align="center">

**5.4 million public protein–ligand potency and activity measurements, with full upstream provenance.**

[Data on Hugging Face](https://huggingface.co/datasets/genesisml/GenesisPotency) ·
[Docs and examples on GitHub](https://github.com/genesistherapeutics/genesispotency) ·
[Genesis Molecular AI](https://genesis.ml)

</div>

GenesisPotency-2026 is the public-source part of the protein–ligand potency data that Genesis
Molecular AI used to train the potency models in the accompanying paper (see [Citation](#citation)).
Every row is a compound, a protein target and either a potency value (pIC50, pKi, pKd) or an
active/inactive call, exactly as used in training, together with the upstream record it came from.

- **5,410,616 rows** from ChEMBL 37, BindingDB (2026-07) and PubChem HTS bioassays.
- **1,773,271 potency measurements** and **3,637,345 binary calls**, including 200,662
  property-matched synthetic decoys.
- **1,038,258 compounds** and **3,640 protein sequences** across **69,939 assay contexts**.
- Each measured row links back to its upstream record: ChEMBL activity, BindingDB reactant set
  or PubChem AID/CID/SID, with the document, target accession and the value as published.
- 1,451 rows were **corrected by an LLM agent** that checked source documents, and are flagged.
- The paper's **public evaluation sets** ship beside the training data as a separate
  configuration: 1,594 potency observations for ranking and 9,364
  hit-identification compounds (see [Benchmarks](#benchmarks)).

**Get the data:** the files are hosted on Hugging Face at
[genesisml/GenesisPotency](https://huggingface.co/datasets/genesisml/GenesisPotency/tree/v2026);
[Using it](#using-it) shows how to load them.

## Using it

```bash
python -m pip install polars huggingface_hub datasets   # examples tested with polars 2.1.0
```

```python
import polars as pl

# The full file needs about 11 GB of memory; pass columns=[...] to load less.
df = pl.read_parquet("hf://datasets/genesisml/GenesisPotency@v2026/data/GenesisPotency-2026/data.parquet")

potency = df.filter(pl.col("task") == "regression")                  # pIC50 / pKi / pKd
exact = potency.filter(pl.col("label_relation") == "=")              # drop censored values
dedup = df.filter(pl.col("duplicate_of_row_id").is_null())           # one copy per measurement
measured = df.filter(pl.col("category") != "synthetic_decoy")        # no decoys
```

Or stream rows with the `datasets` library:

```python
from datasets import load_dataset

ds = load_dataset("genesisml/GenesisPotency", split="train", revision="v2026", streaming=True)
print(next(iter(ds)))
```

To download a local copy and run the quickstart:

```bash
hf download genesisml/GenesisPotency data/GenesisPotency-2026/data.parquet \
  --repo-type dataset --revision v2026 --local-dir .
python examples/quickstart.py data/GenesisPotency-2026/data.parquet
```

[examples/quickstart.py](examples/quickstart.py) shows filtering, deduplication, agent-corrected
rows, ambiguous rows and decoys.

## What is in it

| Source | Potency rows | Active | Inactive | Assay contexts | Compounds | Targets |
|---|---:|---:|---:|---:|---:|---:|
| ChEMBL 37 | 751,201 | 259,190 | 91,785 | 29,386 | 403,982 | 2,147 |
| BindingDB 2026-07 | 1,022,070 | 403,598 | 98,930 | 37,533 | 563,569 | 3,066 |
| PubChem HTS | – | 251,761 | 2,331,419 | 517 | 406,461 | 330 |
| Synthetic decoys | – | – | 200,662 | 2,503 decoy-only | 169,077 | – |
| **Total** | **1,773,271** | **914,549** | **2,722,796** | **69,939** | **1,038,258** | **3,640** |

Potency endpoints: IC50 1,148,723 rows, Ki 502,046, Kd 122,502. Targets are counted as distinct
sequences. Every context belongs to one source; decoys sit in the contexts of their source, and
2,503 contexts hold only decoys (see Decoys).

## Dataset structure

The training data is one Parquet file, one row per training example, 49 columns. The most used
ones:

| Column | Meaning |
|---|---|
| `row_id`, `assay_context_id` | Row ID, and the upstream assay on one target the row belongs to |
| `smiles` | Canonical SMILES of the compound as trained |
| `target_sequence`, `target_accession` | Protein sequence as trained, and its UniProt or NCBI accession |
| `task`, `readout` | `regression` (`IC50`, `Ki`, `Kd`) or `classification` (`binary`) |
| `label`, `label_relation`, `pX` | Regression label `clip(pX − 6, −6, 6)`, its relation in pX sense, and pX |
| `label_is_hit` | Classification label: 1 active, 0 inactive |
| `category` | `pX`, `active`, `inactive` or `synthetic_decoy` |
| `retrieved_from`, `chembl_activity_id`, `bindingdb_reactant_set_id`, `pubchem_aid` | Upstream source and record |
| `source_value`, `source_units`, `source_relation`, `source_smiles` | The upstream measurement and structure, unmodified |
| `duplicate_of_row_id` | Set on BindingDB rows that repeat a ChEMBL row in this file |
| `corrected_by_agent` | `label`, `structure` or `none` |

[DATA_DICTIONARY.md](DATA_DICTIONARY.md) describes every column, its type and when it is null,
for both configurations. `GenesisPotency-2026` (the default) has a single `train` split;
`GenesisPotency-2026-benchmarks` has the `ranking` and `hitid` splits. `v2026` is the release
tag; row and context IDs are stable within it. [manifest.json](manifest.json) lists every file
with its size and SHA-256.

## How it was built

**Scope.** These are the public-source rows of the training set of the paper's potency models.
Only measurements dated before 1 January 2023 were kept. A target was removed if any
alignment to a target of the paper's OpenFE, FEP+4 or hit-identification benchmarks reached 90%
sequence identity over at least half of either sequence, or if it shared that target's UniProt
accession. The paper gives the per-benchmark rules. It contains only rows from ChEMBL, BindingDB and PubChem; rows removed during
curation are not included. Rows, labels and model inputs are exactly as used in training; nothing
was re-derived for release.

**Labels.** Regression rows carry `label = clip(pX − 6, −6, 6)`, where pX is −log10 of the molar
IC50, Ki or Kd; `pX = label + 6` is given too. `label_relation` is the training relation **in pX
sense**: an upstream "IC50 > 10 µM" becomes `pX < 5`. 59 regression rows had pX above 12 and were
clipped (`pX_is_clipped`). Classification rows carry `label_is_hit` (1 = active).

**Decoys.** Synthetic decoys are inactive (`label_is_hit = 0`) compounds added to an assay context
and property-matched to a measured compound of the same assay, given as `decoy_partner_smiles` and
`decoy_partner_inchikey`. Every decoy and every partner is a ChEMBL, BindingDB or PubChem compound.
Decoys were generated before curation, and curation later removed some measurements: 2,503
contexts (23,942 decoys) now hold only decoys, and 25,365 decoys have a partner whose
measurement in that assay is not in this file. They are kept because they were part of the training data.
Decoys have no upstream record, so their measurement and provenance columns are null.

**Agent corrections.** An LLM agent read a sample of the source documents and checked compounds
and values against them. Where the source record was wrong, the training row was corrected:
854 labels (value, relation or binary call) and 597 structures. `corrected_by_agent` marks them. The upstream
value and structure stay in the `source_*` columns, so each correction is visible as a difference.
`corrected_by_agent = none` does **not** mean the row was checked: most rows were not.

**Structures.** `smiles` is RDKit's canonical SMILES of the training molecule. `source_smiles` is
the upstream string, unmodified; it differs in salts, charges or tautomers, and on structure-
corrected rows it is the upstream (wrong) structure. On structure-corrected rows the compound
identifiers (`chembl_molecule_id`, `pubchem_cid`, `pubchem_sids`, `bindingdb_monomer_id`) are null,
because the upstream ones name the uncorrected compound.
Every compound in the file, including decoys and their partners, is a ChEMBL, BindingDB or
PubChem compound. Where another database also records a compound, the published structure
matches a ChEMBL, BindingDB or PubChem structure (largest fragment, InChIKey connectivity); rows
whose structure could not be confirmed this way are not included.

**Identifiers.** All row and context IDs (`GP26-…`, for GenesisPotency 2026) are new and stable
for this version. ChEMBL
target accessions come from ChEMBL's target table (single-protein targets). BindingDB records that
BindingDB imported from ChEMBL get the matching ChEMBL activity ID where exactly one ChEMBL 37
activity matches on document, compound, endpoint, relation, value and target (869,258 of the
900,697 such rows that have a single upstream record); `xref_source` lists which ID columns are such cross-references.

**Checks.** Before release, every row was compared with the training data (labels, relations,
binary calls, sequences and molecules unchanged) and every linked ChEMBL and BindingDB row with
its upstream record (value, relation, units, document, compound). The benchmark labels equal the
paper's evaluation data, and the training-overlap columns were validated with positive and
negative controls.

## Things to know before using it

- **Duplicates across sources.** BindingDB re-hosts much of ChEMBL. 504,807 BindingDB rows are the
  same measurement as a ChEMBL row in this file and point to it with `duplicate_of_row_id`; both
  copies were used in training. A further 30,961 BindingDB rows share a ChEMBL activity with a
  row of the other task; use `chembl_activity_id` to find them. Duplicate pairs can draw the
  compound differently (a few thousand pairs differ by tautomer, e.g. azo vs hydrazone, or by
  stereo only), and about 12,000 pairs carry different target sequences (often the same
  accession). Paired potency labels can differ by up to 0.02 from rounding.
- **Ambiguous rows.** 40,396 classification rows match two or more upstream measurements of the
  same compound in the same assay and target; usually their values differ, and one BindingDB
  record can contribute several endpoints. The measurements are listed in
  `source_record_candidates`; the row's own record and value columns are null, and other scalar
  columns are filled only where every candidate agrees.
- **Assay contexts** group one upstream assay on one target: a ChEMBL assay, a BindingDB deposition
  (its PubChem AID if it has one, otherwise its article or patent), or a PubChem AID. Regression
  and binary rows of the same assay share a context.
- **Origin.** `origin` says who originally curated the record. 933,074 BindingDB rows come from
  ChEMBL and 275,295 ChEMBL rows come from BindingDB's patent curation.

## Known limitations

- Recovered ChEMBL activity IDs on BindingDB rows are matched, not given: an independent audit of
  232 matches found 2 pointing at a different compound (about 1%).
- PubChem target accessions are mostly NCBI protein IDs (`target_accession_namespace`); PubChem
  rows have no target name or organism.
- BindingDB measurement conditions are given as BindingDB states them; some "°C" temperatures are
  in kelvin.
- Two training rows and one decoy partner contain a dummy atom (`*`); that partner has no InChIKey.
- Censored values are clipped into the label range in pX sense; 11 clipped rows turned
  "pX < 13" into "pX < 12".
- Binary calls, decoy generation and the time split follow the paper and are not re-derivable
  from this file alone.

## Benchmarks

The `GenesisPotency-2026-benchmarks` configuration holds the public evaluation sets reported in
the paper, with their labels, provenance and overlap with the training data. They are kept
**separate from the training data**. They are not a new, untouched test set: the paper's
evaluations informed method development.

### Loading them

The benchmarks are the `GenesisPotency-2026-benchmarks` configuration, with the splits
`ranking` and `hitid` ([How to evaluate](#how-to-evaluate) reads them with polars):

```python
from datasets import load_dataset

ranking = load_dataset("genesisml/GenesisPotency", "GenesisPotency-2026-benchmarks",
                       split="ranking", revision="v2026")
hitid = load_dataset("genesisml/GenesisPotency", "GenesisPotency-2026-benchmarks",
                     split="hitid", revision="v2026")
```

### The sets

| Split | Family | Sets | Rows | Labels | Source |
|---|---|---:|---:|---|---|
| `ranking` | OpenFE | 58 | 873 | pX | OpenFE industry benchmark |
| `ranking` | FEP+4 | 4 | 87 | pX (IC50, Ki) | FEP+ benchmark series CDK2, JNK1, p38, TYK2 |
| `ranking` | OpenBind | 1 | 494 | pKd | OpenBind EV-A71 2A release (the paper's cohort) |
| `ranking` | CASP16 | 2 | 140 | pIC50 | CASP16 pharma ligands (autotaxin, chymase) |
| `hitid` | CACHE #1–#4 | 4 | 6,874 | active / inactive (502 active) | CACHE hit-finding challenges |
| `hitid` | Docking screen | 3 | 2,490 | active / inactive (506 active) | AmpC, D4 and σ2 large-scale docking campaigns |

**Potency ranking (`ranking`).** Can a model order compounds by potency within a congeneric
series, without seeing any measurement from it?

- **OpenFE**: 58 congeneric series from the OpenFE industry benchmark of relative binding free
  energy (Baumann et al. 2026), with the experimental values as tabulated by Mattsson and
  Walters.
- **FEP+4**: the four classic FEP+ series CDK2, JNK1, p38 and TYK2 (Wang et al. 2015).
- **CASP16**: Roche's autotaxin (123) and chymase (17) compounds released for the CASP16 ligand
  affinity challenge (Gilson et al. 2026).
- **OpenBind**: 494 compounds with measured affinity for the enterovirus A71 2A protease, from
  the first OpenBind release (Nelen et al. 2026).

**Hit identification (`hitid`).** Can a model pick out the actives among compounds that were
actually bought and tested in a screening campaign?

- **CACHE #1–#4**: compounds nominated by the participants of the first four CACHE hit-finding
  challenges and tested by the organizers, against LRRK2 WD40, SARS-CoV-2 Nsp13, SARS-CoV-2 Mac1
  and CBL-B.
- **Docking screens**: compounds bought and tested after ultra-large docking screens against
  AmpC β-lactamase (Liu et al. 2025), the dopamine D4 receptor (Lyu et al. 2019) and the σ2
  receptor (Alon et al. 2021). `source_compound_id` is the ZINC ID.

`benchmark` names the set each row belongs to, e.g. `openfe_jacs_set_tyk2`,
`hitid_cache2_nsp13`; always score within a set. A compound or target can recur in different
sets. `label_basis` says where each label comes from and `activity_definition` what "active"
means in each hit-ID set; see [DATA_DICTIONARY.md](DATA_DICTIONARY.md#benchmarks).

### How to evaluate

The paper scores the sets as follows.

- **OpenFE, FEP+4, CASP16:** Pearson r between prediction and pX within each set (each OpenFE
  series, each FEP+4 or CASP16 target), then the mean over a family's sets weighted by their
  number of compounds. Censored values (`label_relation` other than `=`) count at their bound.
- **OpenBind:** Spearman ρ over all 494 compounds.
- **Hit identification:** normalized enrichment nEF@q = (EF@q − 1) / (EF_max@q − 1) within each
  set, where EF@q is the active fraction in the top fraction q of the ranking divided by the
  overall active fraction, and EF_max@q is the best value any ranking could reach; 0 is random
  and 1 is perfect. The seven sets are averaged with equal weight, at q from 0.2% to 10%.

```python
import numpy as np
import polars as pl
from scipy.stats import pearsonr, spearmanr

base = "hf://datasets/genesisml/GenesisPotency@v2026/data/GenesisPotency-2026"
ranking = pl.read_parquet(f"{base}/ranking_benchmark.parquet")
hitid = pl.read_parquet(f"{base}/hitid_benchmark.parquet")
# Add your model's score for each row as a column "pred" (higher = more potent / more likely active).


def ranking_score(df: pl.DataFrame, family: str) -> float:
    rows = df.filter(pl.col("benchmark_family") == family)
    if family == "OpenBind":
        return spearmanr(rows["pX"], rows["pred"]).statistic
    sets = [(len(s), pearsonr(s["pX"], s["pred"]).statistic) for _, s in rows.group_by("benchmark")]
    return sum(n * r for n, r in sets) / sum(n for n, _ in sets)


def nef(active: np.ndarray, score: np.ndarray, q: float) -> float:
    top = max(1, round(len(active) * q))
    hits = active[np.argsort(-score, kind="stable")[:top]].mean()
    prevalence = active.mean()
    best = min(len(active) / top, 1 / prevalence)
    return (hits / prevalence - 1) / (best - 1)


def hitid_score(df: pl.DataFrame, q: float = 0.01) -> float:
    return np.mean([
        nef(s["label_is_hit"].to_numpy(), s["pred"].to_numpy(), q)
        for _, s in df.group_by("benchmark")
    ])
```

### Notes

- **Hit-ID labels differ by set.** `activity_definition` says what "active" means: SPR, HTRF or FP
  readouts with different thresholds. CACHE #4 (CBL-B) actives are two-run FP-screen responders,
  not orthogonally confirmed binders.
- **CACHE #1 (LRRK2 WD40) endpoint.** The source calls any compound with a measured SPR Kd a
  binder (189 actives). The paper uses Kd ≤ 150 µM instead (101 actives). This is a
  retrospective revision chosen after inspecting the data, not a correction of a transcription
  error, and it is not CACHE's own advancement decision. The curated Kd is in `source_value`, as
  CACHE gives it (some values are implausible, e.g. 3.7 M), and the original call in
  `source_label`.
- **OpenBind** is named for the EV-A71 2A protease, but the affinities were measured on the CVA16
  2A protease as a surrogate; `target_sequence` is the modeled EV-A71 2A construct. The 494 rows
  are the paper's cohort: the 494 of OpenBind's 499 compounds with a released pKd that
  OpenBind's own flags mark as non-covalent, structurally valid and not a suspected artefact,
  with one crystal structure per compound.
- **CASP16.** The autotaxin construct is the rat protein. Nine autotaxin compounds sit at the
  assay's 10 µM ceiling and are stored as `pX < 5`. The organizers' files state no licence;
  the rows are shared here with credit to CASP16 and Roche (see NOTICE).
- **Overlap with the training data** is given on every row. No OpenFE, FEP+4 or hit-ID target
  reaches the training-exclusion threshold against a training target (highest identity 0.899,
  0.84 and 0.81).
  CASP16 and OpenBind are separated from training by the date cutoff only, so their targets do
  have close training targets (`target_in_training`), and 11 CASP16 compound–target pairs also
  appear in training (`pair_in_training`).
- **Structures are as the benchmarks deposit them.** 144 hit-ID structures (128 CACHE, 16 docking
  screen) are salts or solvates with several components; in 54 CACHE structures a chloride is
  written as a neutral chlorine atom (`[Cl]`), probably an HCl salt. Their `inchikey` describes the whole mixture; compare compounds
  by their largest fragment (the training-overlap columns do). Six OpenBind compounds are
  deposited as cations, two of them with an implausible protonated amide (`C([NH3+])=O`), and
  for one FEP+4 p38 compound (2x) the structure file and the label table give opposite
  stereocentres; `source_smiles` follows the structure file.

## Intended use

Training and benchmarking machine-learning models of protein–ligand potency and activity, and
studying public bioactivity data and its provenance. Targets that overlap the paper's OpenFE,
FEP+4 and hit-identification benchmarks were removed from the training data, so models trained
on it can be evaluated on those sets; check `target_in_training` and `pair_in_training` before
evaluating on CASP16 or OpenBind. It is not intended for clinical or diagnostic decisions.

## Licensing and attribution

GenesisPotency-2026 is released under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). It adapts data from ChEMBL
(CC BY-SA 3.0), BindingDB (CC BY 4.0 for BindingDB curation; ChEMBL-derived records CC BY-SA 3.0),
PubChem (deposited by many organisations; see each AID's depositor) and UniProt (CC BY 4.0, for
target accessions). The benchmark configuration also adapts the OpenFE, FEP+ and PLB benchmarks
and the Mattsson–Walters benchmark tables (MIT), CACHE challenge results (which CACHE shares
under CC BY 4.0), the OpenBind release (CC0 1.0), the published results of three docking
campaigns, and the CASP16 affinities (no licence stated; shared with attribution). See [NOTICE.md](NOTICE.md) for the attributions and citations you must keep when you
redistribute or adapt this dataset.

## Citation

If you use this dataset, cite the accompanying technical report and the dataset, and the
upstream sources listed in [NOTICE.md](NOTICE.md).

```bibtex
@techreport{genesis2026ruby,
  title       = {{Ruby}: State-of-the-Art Potency Prediction across Discovery Regimes Using Learned
                 Structural Representations},
  author      = {{Genesis Research Team}},
  institution = {Genesis Molecular AI},
  type        = {Technical Report},
  year        = {2026},
  month       = nov
}

@misc{genesispotency2026,
  title        = {{GenesisPotency-2026}: public protein--ligand potency data with upstream provenance},
  author       = {{Genesis Molecular AI}},
  year         = {2026},
  howpublished = {\url{https://huggingface.co/datasets/genesisml/GenesisPotency}},
  note         = {Release v2026}
}
```

## Contact

Questions and corrections: open an issue on
[GitHub](https://github.com/genesistherapeutics/genesispotency/issues) or a discussion in the
Hugging Face Community tab. For a data problem, include the `row_id`.
