# CleanMol

**Reproducible cleaning and standardization of SMILES-based chemical datasets.**

CleanMol is a small, modular Python tool that turns messy chemical datasets
into clean, canonical, ML-ready tables — and writes a full audit trail of
every change it made along the way.

---

## Why this exists

Public chemical datasets (ChEMBL, PubChem, ZINC, vendor catalogs, internal
HTS dumps) are full of issues that silently corrupt downstream models:

- invalid or unparseable SMILES
- duplicate molecules written in non-canonical forms (`CCO` vs `OCC`)
- salts and counter-ions mixed in with the active compound
- inconsistent tautomers, charges, and functional-group encodings
- mixtures where only the largest fragment matters

If you train a QSAR model, fingerprint similarity search, or generative
model on dirty data, the bugs *do not* go away — they get baked into the
weights. The fix is preprocessing that is:

1. **reproducible** — same input + same config → same output, every time
2. **auditable** — you can prove which rows were dropped and why
3. **modular** — each step (validate, desalt, normalize, dedupe) is opt-in
4. **honest** — no silent failures; everything is logged

CleanMol is designed around those four properties.

---

## Installation

CleanMol requires Python 3.10+ and RDKit.

```bash
git clone https://github.com/nurtilekgalimov/cleanmol.git
cd cleanmol
pip install -e .
```

This installs the `cleanmol` command on your PATH.

> **RDKit note.** If `pip install rdkit` fails on your platform, install
> RDKit via conda first (`conda install -c conda-forge rdkit`) and then run
> `pip install -e . --no-deps && pip install pandas typer`.

---

## CLI usage

The basic invocation is:

```bash
cleanmol input.csv --smiles-column smiles --output cleaned.csv
```

### Common flags

| Flag | What it does |
| --- | --- |
| `--output, -o` | Where to write the cleaned CSV (default: `cleaned.csv`) |
| `--smiles-column` | Name of the SMILES column in CSV input (default: `smiles`) |
| `--report` | Write a detailed JSON report of every change |
| `--remove-salts` | Strip common salts using RDKit's `SaltRemover` (heuristic — see note below) |
| `--salt-definitions` | Path to a custom salt SMARTS file (overrides RDKit's default list) |
| `--keep-largest-fragment` | Reduce mixtures to the largest covalent fragment |
| `--normalize` | Apply RDKit standardization (functional groups, charges) |
| `--deduplicate` | Remove duplicate canonical SMILES |
| `--keep` | When deduplicating, keep `first` or `last` (default: `first`) |
| `--verbose, -v` | Verbose step-by-step logging to stderr |
| `--version` | Print the CleanMol version and exit |

### Full example

```bash
cleanmol chembl_subset.csv \
    --smiles-column canonical_smiles \
    --output chembl_clean.csv \
    --report chembl_report.json \
    --remove-salts \
    --keep-largest-fragment \
    --normalize \
    --deduplicate \
    --verbose
```

When the run completes, the CLI prints a JSON summary to stdout:

```json
{
  "input_count": 12000,
  "output_count": 11432,
  "invalid_removed": 47,
  "duplicates_removed": 401,
  "salts_removed": 312,
  "fragments_dropped": 89,
  "normalizations_applied": 1206
}
```

---

## Example input / output

**Input** (`example.csv`):

```csv
id,smiles
1,CCO
2,OCC
3,CC(=O)O.[Na]
4,not_a_molecule
5,c1ccccc1
6,C1=CC=CC=C1
```

**Command:**

```bash
cleanmol example.csv \
    --smiles-column smiles \
    --output cleaned.csv \
    --report report.json \
    --remove-salts \
    --deduplicate
```

**Output** (`cleaned.csv`):

```csv
id,smiles
1,CCO
3,CC(=O)O
5,c1ccccc1
```

**What happened (from `report.json`):**

| Row | Result |
| --- | --- |
| 1 `CCO` | kept (canonical) |
| 2 `OCC` | dropped — duplicate of row 1 (`CCO`) |
| 3 `CC(=O)O.[Na]` | sodium counter-ion stripped → `CC(=O)O` |
| 4 `not_a_molecule` | dropped — RDKit could not parse SMILES |
| 5 `c1ccccc1` | kept (canonical aromatic benzene) |
| 6 `C1=CC=CC=C1` | dropped — duplicate of row 5 after canonicalization |

---

## Programmatic use

```python
from cleanmol import CleanMolPipeline, PipelineConfig

config = PipelineConfig(
    smiles_column="smiles",
    remove_salts=True,
    keep_largest_fragment=True,
    normalize=True,
    deduplicate=True,
    verbose=True,
)

pipeline = CleanMolPipeline(config)
result = pipeline.run_from_csv("input.csv")

result.to_csv("clean.csv")
result.report.to_json("report.json")
print(result.report.summary())
```

You can also feed a plain list of SMILES:

```python
result = pipeline.run_from_smiles(["CCO", "OCC", "CC(=O)O.[Na]"])
print(result.dataframe)
```

---

## A note on salt removal

Salt removal is a **heuristic**, not a definitive call. In many cases the
parent/counter-ion split is obvious (`CC(=O)O.[Na]` → acetate + sodium), but
in plenty of real-world datasets it genuinely isn't — some "salts" in the
default RDKit list may *be* the molecule of interest for your project, and
some real counter-ions may be missing from it.

CleanMol gives you two knobs here:

- `--remove-salts` (off by default) enables the step at all.
- `--salt-definitions path/to/salts.txt` swaps in your own SMARTS file.

The file format is the standard RDKit one (one SMARTS pattern per line,
`#` for comments). Use this to tighten or loosen the default list to fit
the chemistry of your dataset. Every removal is logged in the report so
you can review which calls the heuristic actually made.

---

## Handling very large files

CleanMol currently loads the full table into memory. That's fine for
ChEMBL-scale datasets but will fall over on, say, a 200M-row vendor dump.
Two pragmatic workarounds today:

1. **External dedup with GNU `sort`.** Once you have a canonicalized CSV,
   `sort -t',' -k2,2 -u file.csv` will deduplicate on column 2 without
   ever loading it into memory. It's fast, battle-tested, and unbeatable
   for sheer scale.
2. **Chunked processing.** Split the input, run CleanMol per chunk, then
   concatenate and dedup. Lossy for cross-chunk dedup unless you follow
   up with the `sort -u` trick above.

Native streaming I/O with a streaming report is on the roadmap so this
becomes a one-flag operation.

---

## Pipeline flow

```
input  ──▶  validate  ──▶  canonicalize  ──▶  remove salts (opt.)
       ──▶  largest fragment (opt.)  ──▶  normalize (opt.)
       ──▶  re-canonicalize  ──▶  deduplicate (opt.)  ──▶  output + report
```

Each step is implemented as a small, side-effect-free function in
[cleanmol/standardize.py](cleanmol/standardize.py) or
[cleanmol/deduplicate.py](cleanmol/deduplicate.py). The pipeline orchestrator
in [cleanmol/pipeline.py](cleanmol/pipeline.py) decides which steps to run
based on `PipelineConfig`.

---

## Testing

```bash
pip install -e ".[test]"
pytest
```

The test suite covers SMILES validation, deduplication, salt removal, and a
small end-to-end run.

---

## Project layout

```
cleanmol/
├── cleanmol/
│   ├── __init__.py
│   ├── cli.py            # Typer-based CLI
│   ├── config.py         # PipelineConfig dataclass
│   ├── deduplicate.py    # Duplicate removal
│   ├── io.py             # CSV / SDF / list readers + writers
│   ├── pipeline.py       # Pipeline orchestration
│   ├── report.py         # Structured CleaningReport
│   ├── standardize.py    # Validation & RDKit normalization
│   └── utils.py          # Logging helpers
├── cli.py                # `python cli.py` shim
├── tests/
│   ├── test_pipeline.py
│   └── test_standardize.py
├── pyproject.toml
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## License

MIT — see [LICENSE](LICENSE).
