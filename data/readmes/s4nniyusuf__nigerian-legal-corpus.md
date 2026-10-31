# nigerian-law-corpus
A curated corpus of Nigerian legal texts, including the 1999 Constitution, selected Acts and Lagos tenancy law cleaned and structured for information retrieval, RAG, semantic search, and legal NLP.


## Folders and files

| Path | Description |
|---|---|
| `raw/` | Original source files, unmodified, for traceability |
| `processed/` | Cleaned and structured text, ready for RAG and NLP use |
| `LICENSE.md` | CC BY 4.0 license text |


## Sources
**Constitution** - [Food and Agricultural Organisation ](https://faolex.fao.org/docs/pdf/nig164561.pdf)

**Electoral Act** - [Policy and Legal Advocacy Centre](https://placng.org/i/acts/)

**Criminal Code Act** - [Policy and Legal Advocacy Centre](https://placng.org/i/acts/) (*here the schedule is the criminal code*)

**Lagos Tenancy law** - [Lagos Ministry of Justice](https://lagosministryofjustice.org/)


## Processing method

Each processed and structured dataset was extracted from its corresponding PDF in `raw/` and organized as JSONL, with one record per line.

The records are divided according to each law's structure. Record types include sections, preambles, and schedules. Schedule content is represented in multiple records where the source structure calls for it (Constitution and Criminal Code Act).

The Criminal Code is organized mainly as `code_section` records because its schedule contains the code itself. 

The available fields and record types therefore differ between datasets.


## Dataset metadata

Each JSONL file in `processed/` contains one dictionary per record. The keys below appear across the datasets; fields may be `null` or absent when they do not apply.

```python
{
    # Record-level identifier
    "id": "...",                 # Criminal Code only

    # Source document identifier
    "document_id": "...",

    # Original PDF filename
    "source_file": "...",

    # Record category: preamble, section, code_section,
    # act_section, schedule_text, schedule_paragraph,
    # schedule_table_row, or schedule_oath
    "record_type": "...",

    # Inclusive PDF page range
    "physical_page_start": 1,
    "physical_page_end": 1,

    # Structural labels, when present
    "chapter": "...",
    "chapter_title": "...",
    "part": "...",
    "part_title": "...",

    # Section reference and heading
    "section_number": "...",
    "section_title": "...",

    # Extracted legal text
    "text": "..."
}
```

The schema varies by source: 
- the Constitution includes chapter and part fields plus several schedule record types; 
- the Electoral Act includes part fields and schedule text; 
- the Criminal Code includes `id`, `chapter` fields, and `code_section` records;
- and the Tenancy Law mainly records sections and page references.

`record_type` values describe the source-specific record structure.


## Disclaimer

This corpus is intended for research and informational use; consult authoritative legal sources for current law and interpretation.

## License

The preprocessed dataset in this repository is licensed under the
[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
license.

See [LICENSE.md](LICENSE.md) for the full text.

This license applies to the original contributions in the dataset,
including its preprocessing and structuring. It does not claim
ownership of the underlying legal texts.
