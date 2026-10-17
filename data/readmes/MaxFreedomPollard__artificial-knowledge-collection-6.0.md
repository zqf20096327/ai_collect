# Artificial Knowledge Collection 6.0

<sub>Note: this is a growing collection, added to continuously. New bodies of knowledge arrive over time; what follows describes it as it stands.</sub>

[![release](https://img.shields.io/github/v/release/MaxFreedomPollard/artificial-knowledge-collection-6.0?label=release)](https://github.com/MaxFreedomPollard/artificial-knowledge-collection-6.0/releases)
![founding map](https://img.shields.io/badge/founding%20map-159%2C722%20records-2ea44f)
![collection](https://img.shields.io/badge/collection-544%2C279%20things-2ea44f)
![formats](https://img.shields.io/badge/formats-JSONL%20·%20Parquet%20·%20TXT%20·%20CSV-555)

Intelligence is the creation of knowledge from knowledge. Anyone who builds or works with AI needs a solid body of knowledge to build on and to check its output against. This repository exists to collect exactly that: knowledge that is cleaned, rare, or otherwise hard to come by, each body of it put into one ready-to-use file. This is artificial knowledge, knowledge gathered for the making of, and utilization by, artificial intelligence.

![A real neighborhood from the founding dataset: bicycle, its parent kinds, its sub-kinds, and what it cannot also be](docs/hero.svg)

## What is inside

**The What Exists List** (`what-exists-list/`). The merged master file, and the one thing here you will find nowhere else, because it is assembled in this repository. Every thing that all the other datasets know about, gathered into a single graph: 544,279 things and 1,003,336 links between them. A concept connects to the word that names it, to its plain definition, and to the everyday facts people have stated about it, each link traceable back to a human source. It is the single index to the whole collection, and the top download in every release.

**The founding common-sense knowledge base** (`max-map.jsonl`). 159,722 human-written concepts and the logical relationships between them, the largest body of common sense ever built by hand. This is the knowledge base from the Cyc program, the decades-long effort to teach a computer the ordinary things a person knows by the age of ten. It matters because this is the only uncorrupted copy in circulation. The mirrors that survive are deeply corrupted and salted with spam; this is the clean edition. It was written by people, one fact at a time, before generative AI existed.

**WordNet** (`wordnet/`). Princeton's hand-built map of the English language: 117,791 meanings, each with a definition and its links to other meanings. The reference lexical database of computing, freed here from the 1990s file format that kept it locked away.

**The human core of ConceptNet** (`conceptnet-human-core/`). 226,284 everyday facts typed in plain English by volunteers, such as "a knife is used for cutting." Where the founding map says what things are, this says what things do, the practical common sense of daily life.

**Physical constants** (`physical-constants/`). The CODATA 2022 values, the SI prefixes, and the exact unit conversions, 415 records. The numbers a tool-using model should check its arithmetic against.

**The sky and the elements** (`sky-and-elements/`). The measured physical universe in one file: 118 chemical elements, 3,352 isotopes, 9,096 stars of the Yale Bright Star Catalogue, the 13 planets and dwarf planets, 46 moons, the 107 Messier deep-sky objects (galaxies, nebulae, and clusters), and the 88 constellations. 12,820 records, from NIST, NASA/JPL, and the great sky catalogues.

**The world** (`world-factbook/`). A geography of the planet in three files: every country and territory from the CIA World Factbook (261 in all, with capital, population, borders, languages, and government), 7,342 cities with their coordinates and populations, and 645 named rivers and lakes. An answer key for geography and civics.

**Human word norms** (`human-word-norms/`). How people actually hold 85,889 words (how concrete each is, how early it is learned, how strongly one word calls another to mind), plus 72,089 measured association pairs. The empirical shape of human word knowledge.

**AKC-Eval** (`akc-eval/`). 11,250 yes or no reasoning questions whose every answer is provable from the knowledge itself. A test of reasoning grounded in human-checked fact rather than model output.

## Quick start

```python
import gzip, json

# the merged master list of everything that exists, and how it connects
things = {n["id"]: n for n in
          (json.loads(l) for l in gzip.open("what-exists-list.jsonl.gz", "rt", encoding="utf-8"))}

# or the founding common-sense map on its own
data = [json.loads(line) for line in open("max-map.jsonl", encoding="utf-8")]
```

The founding map also comes as `max-map.parquet` (columnar, for pandas, Polars, or DuckDB), `max-map.txt` (plain text), and `max-map.vector.jsonl` (embed-ready passages), with ready-made subsets in `extras/subsets/`. Every dataset folder carries a `KEY.md` explaining each field and a `FORMATION.md` recording where the data came from and what cleaning was applied.

## Why it matters

The founding common-sense knowledge base was made by people and nothing else. Every concept and every relationship in it was written by hand, before generative AI existed. Hand-built symbolic knowledge will be useful in the future for certain applications, like steel forged before atomic tests is valued for its lack of background radiation. Writing knowledge down this way was common on a macro scale, but extremely rare on a micro scale - thus the initiation of the project in the first place. The map holds no machine-written text and no machine-invented structure. As models increasingly learn from their own output, the worth of a clean, human-origin record only rises.

The founding map alone was the work of more than twenty years, a group of people writing out the things a person just knows and never thinks about again: that a mother is older than her child, that you cannot be in two places at once, that a wheel is round, ice is cold, and a bicycle is not a wagon. Not by scraping the web, and not by training on text, but by hand. That line of research ran for decades through AI, and through SRI's CALO project, the work that became Apple's Siri. The public version was pulled offline years ago, and it cannot be made again. It should be the first dataset any AI experimenter acquires in his quest for knowledge.

The porting of reality onto the internet is far less complete than people imagine, and the human-authored record is the only bridge raw computation can take to become intelligence without leaning on intelligence that already exists. Intelligence is the combination of knowledge into new knowledge, and it matters only in relation to the quality of the knowledge it works from and on. Benjamin Franklin wrote in his autobiography that he would often check "whether some error had not insinuated itself unperceived into my argument, so as to infect all that followed, as is common in metaphysical reasonings." Those who work with AI do the same. That is why this collection is offered with a focus on total accuracy, and why it will keep growing.

## Downloads

Every [release](https://github.com/MaxFreedomPollard/artificial-knowledge-collection-6.0/releases) carries the **What Exists List** as the top download, each individual dataset as its own checksummed file, and a single **master archive** with the entire collection, plus `SHA256SUMS.txt` so any download can be verified with `shasum -a 256 -c`.

## Credit and license

Compiled by **Max Freedom Pollard**. The compilation and the datasets original to it (the What Exists List and AKC-Eval) are released under **CC BY-SA 4.0**; each component dataset keeps the license of its source, documented in its `FORMATION.md`. See [LICENSE.md](LICENSE.md).
