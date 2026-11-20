# Oribi

**Give AI a useful picture of your data before it starts analyzing it.**

Oribi is an open source Python library that profiles a pandas DataFrame and turns what it finds into structured analytical context. The result describes the dataset, its columns, likely semantic roles, candidate keys, possible grain, relationships, and analytical warnings.

Use that context as a starting point for AI assisted analysis, SQL generation, charting, or your own data exploration. Oribi profiles the DataFrame locally. It does not send your rows to an AI provider, and it does not require a specific model or AI service.

## Get started

Install Oribi from PyPI:

```bash
python -m pip install oribi
```

Then inspect a DataFrame:

```python
import pandas as pd
from oribi import inspect

df = pd.DataFrame({
    "order_id": [101, 101, 102, 102],
    "product_id": [7, 8, 7, 8],
    "revenue": [25.0, 40.0, 30.0, -5.0],
})

context = inspect(df)

print(context.summary())
print(context.to_context(max_chars=2_000))
```

`summary()` gives you a readable overview. `to_context()` creates a compact representation that you can include in an AI prompt.

## What Oribi reports

Oribi records measurements from the DataFrame and keeps its interpretations tied to evidence.

| Area | What it reports |
| --- | --- |
| Dataset | Row and column counts, duplicate rows, and index information |
| Columns | Missingness, distinct counts, numeric summaries, categorical top values, and datetime bounds |
| Semantic roles | Likely identifiers, measures, dimensions, categories, temporal fields, booleans, text, or unknown columns |
| Keys and grain | Candidate single- and two column keys, plus an estimate of what one row may represent |
| Relationships | Cardinality and observed value relationships within the DataFrame |
| Analysis guidance | Recommendations for likely measures and identifier counts |
| Warnings | Duplicate rows, missingness, non unique identifiers, negative or skewed measures, high cardinality categories, and possible gaps in regular datetime series |

A role, key, relationship, or grain estimate is an **inference**, not a guarantee about business meaning. Oribi includes evidence so an analyst or downstream system can judge how much to trust each result.

## Choose an output format

A `DatasetContext` can be rendered for different uses:

```python
# Short overview
print(context.summary())

# Full report for people
markdown = context.to_markdown()

# Structured data for an application
payload = context.to_dict()
json_text = context.to_json()

# Compact context for an AI prompt
prompt_context = context.to_context(max_chars=8_000)
```

Each method renders the same profile. The serializers do not re read the DataFrame or run new inferences.

## Data handling

Oribi profiles the DataFrame in memory and does not keep a reference to it in the returned context. The in-memory `DatasetContext` retains local `top_values` and exact bounds for inspection.

Top values are ranked by frequency using pandas equality and counts. Ties use a stable value order for supported types, including strings, built-in numbers, and common date and time values. Tied opaque objects without a stable value key follow pandas count order, so reordering rows or categories can change which of them appears at the cutoff. Profiling does not call their `repr()` to rank them.

By default, `to_dict`, `to_json`, `to_markdown`, and `to_context` omit sampled cell values and exact bounds. Dictionary and JSON exports retain top frequency counts and omit strings in evidence details. They also omit means, medians, standard deviations, skewness, and quantiles when fewer than three non-missing values were observed.

You can explicitly include local values and bounds when exporting:

```python
json_text = context.to_json(include_values=True)
```

The other export methods accept the same option. Treat opt-in output as containing raw data details. Column and index names and aggregates can disclose information, so review context before sharing it, especially when the source is sensitive.

Opt-in text reports quote string category labels to distinguish them from numeric values. Compact reports include category lists when space remains after analytical guidance and evidence.

Since Oribi 0.2.0, dictionary and JSON exports use `schema_version: "2"`. Update consumers that expect schema version 1 or depend on the previous Markdown or compact text layout. Use `include_values=True` when callers need local samples and bounds in version 2.

## Configure a profile

Use `ProfileOptions` to control parts of the analysis:

```python
import pandas as pd
from oribi import ProfileOptions, inspect

df = pd.DataFrame({"amount": [12.5, 18.0, 20.0]})

context = inspect(
    df,
    options=ProfileOptions(
        top_k=5,
        max_exact_rows=50_000,
    ),
)
```

Options include `top_k`, `include_quantiles`, `max_exact_rows`, `max_key_columns`, `max_relationships`, `max_relationship_columns`, `max_gap_examples`, and `max_gap_warnings`.

`max_exact_rows` is an inclusive row-count limit on numeric quantiles, composite-key pair scans, and observed relationship scans. At or below the limit, each calculation also depends on its own options and on eligible input. Above the limit, quantiles are omitted, composite-key pairs are skipped, and the observed relationship collection is empty. Single-column observations, cardinalities, and semantic inference still run.

Use `context.profile.row_count` and the configured limit to tell when these calculations were skipped by the limit. If the grain also remains undetermined, its evidence reports `key_search_bounded` above the limit. An empty quantile mapping or observed relationship collection alone cannot show whether a calculation ran.

## How to interpret the results

Oribi uses deterministic heuristics based on observed values, data types, and supporting evidence. Column names can contribute to role inference, but they cannot establish a relationship by themselves.

- A candidate key with `verified_unique=True` has no observed collisions or null components. Approximate candidates can have collisions or missing values. A verified candidate still needs domain validation before it can be used as a business key.
- A likely grain describes a pattern in the observed rows. It can remain undetermined when the evidence is weak or ambiguous.
- A relationship within one DataFrame does not prove that a join to another table is valid or safe.
- Confidence scores describe heuristic strength. They are not calibrated probabilities.

Use the profile as evidence for further analysis, and check whether each inference fits the dataset's actual domain.

## Current scope and limitations

Oribi currently works with in memory pandas DataFrames. It does not connect to databases or remote data sources, and it does not include an AI provider integration. You choose where the generated context goes.

- Python 3.10–3.14 and pandas 1.5.3 or newer, below pandas 4. Use NumPy 1.x with pandas 1.5.3.
- Column labels must be unique strings.
- Datetime like text is not parsed automatically.
- Native complex valued columns are unsupported and raise `InvalidInputError`.
- Profiling may require several full column scans. Exact composite key and relationship checks are bounded by configured row and column limits.

## Development

Clone the repository and install the development dependencies:

```bash
git clone https://github.com/samhoon000/Oribi.git
cd Oribi

python -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
# .venv\Scripts\Activate.ps1

python -m pip install -e ".[dev]"
pytest -q
python -m build
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the contribution workflow and [DESIGN.md](DESIGN.md) for architecture notes. To run the end to end example:

```bash
python -m examples.quickstart
```

## Releases

The package version is defined in `project.version` in `pyproject.toml`. Releases use GitHub tags matching `v<version>`. The release workflow runs the test matrix, builds and validates the wheel and source distribution, then publishes those artifacts to PyPI through GitHub Actions Trusted Publishing.

See [CONTRIBUTING.md](CONTRIBUTING.md) for release steps and repository setup.

## Roadmap

The current release focuses on pandas DataFrames and deterministic, evidence-bearing heuristics. Additional data sources, configurable semantic rules, cross-table foreign-key analysis, and richer profiling options are future work.

## License

MIT. See [LICENSE](LICENSE).
