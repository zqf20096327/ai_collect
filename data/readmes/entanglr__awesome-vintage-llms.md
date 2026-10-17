# Awesome Vintage LLMs [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of **vintage large language models** — also called *historical LLMs*, *time-capsule LLMs*, or *time-locked LLMs* — together with the papers, datasets, demos, and discussions surrounding them.

A *vintage LLM* is a language model trained (typically *from scratch*) on text from a bounded historical period, with no information from after a given knowledge-cutoff date in its training corpus. The goal is to produce a model that does not merely *roleplay* a historical era when prompted, but whose vocabulary, worldview, and "mental furniture" are genuinely shaped by the textual culture of that period. The term *vintage LLM* was popularised by Owain Evans in his ["Vintage Large Language Models"](https://owainevans.github.io/talk-transcript.html) talk; for a humanist's perspective on the emerging field, see Benjamin Breen's essay ["Are 'Vintage LLMs' the start of a new humanistic field?"](https://resobscura.substack.com/p/are-vintage-llms-the-start-of-a-new).

These models are interesting because they enable, among other things:

- Counterfactual experiments (e.g. *can a pre-1915 model independently arrive at general relativity?*)
- Contamination-free benchmarks for temporal generalisation and forecasting
- Research in the digital humanities, social sciences, and history of ideas
- Aggregate "windows into the past" for studying period vocabulary, rhetoric, and assumptions

## Contents

- [Models](#models)
  - [MonadGPT (2023)](#monadgpt-2023)
  - [TimeCapsuleLLM (2025–2026)](#timecapsulellm-20252026)
  - [Ranke-4B / History LLMs (2025–2026)](#ranke-4b--history-llms-20252026)
  - [Machina Mirabilis / GPT-1900 (2026)](#machina-mirabilis--gpt-1900-2026)
  - [Mr. Chatterbox (2026)](#mr-chatterbox-2026)
  - [Talkie-1930 (2026)](#talkie-1930-2026)
- [Related reading](#related-reading)
- [Contributing](#contributing)
- [License](#license)

## Models

Listed in chronological order of first public release / announcement.

### MonadGPT (2023)

> *"What would have happened if ChatGPT was invented in the 17th century?"*

A 7B-parameter chatbot fine-tuned by **Pierre-Carl Langlais** (Pclanglais) from **Mistral-Hermes 2** on roughly 11,000 early-modern texts in English, French, and Latin (≈1400–1700 CE), drawn primarily from [EEBO](https://en.wikipedia.org/wiki/Early_English_Books_Online) and [Gallica](https://gallica.bnf.fr/). MonadGPT replies in archaic language and frequently invokes pre-modern references; it is in many ways the spiritual ancestor of the more recent train-from-scratch projects below, although it is technically a *fine-tune* rather than a clean-room vintage model. Released November 2023, it predates the term "vintage LLM" but is widely cited as an early example of the idea.

- 🤗 Source model: [Pclanglais/MonadGPT](https://huggingface.co/Pclanglais/MonadGPT)
- 🤗 Quantised / GGUF: [TheBloke/MonadGPT-GGUF](https://huggingface.co/TheBloke/MonadGPT-GGUF) · [TheBloke/MonadGPT-GPTQ](https://huggingface.co/TheBloke/MonadGPT-GPTQ)
- 📝 Coverage: [Simon Willison's Weblog](https://simonwillison.net/2023/Nov/27/monadgpt/) · [Medium write-up by Marek Okrutny](https://medium.com/@okrutny/unlocking-the-past-with-large-language-models-a-journey-through-historical-conversations-and-61efca2f5445) · [PNAS — "Large Language Models based on historical text could offer informative tools for behavioral science"](https://www.pnas.org/doi/10.1073/pnas.2407639121)
- 💬 Hacker News: [MonadGPT — a chatbot of the 17th century](https://news.ycombinator.com/item?id=38407510)

### TimeCapsuleLLM (2025–2026)

A series of models trained *from scratch* on London texts published between **1800 and 1875** by **Hayk Grigorian** (with academic supervision from Dr. Hamed Yaghoobian at Muhlenberg College). Versions range from a tiny 16M-parameter `v0` built on nanoGPT to a 1.2B-parameter `v2` trained on a 90 GB corpus of 136,344 documents. The `v1` model famously connected the year 1834 with Lord Palmerston and a real London protest unprompted, demonstrating that a small model trained only on period sources can surface genuine historical patterns from primary sources alone.

- 💻 GitHub: [haykgrigo3/TimeCapsuleLLM](https://github.com/haykgrigo3/TimeCapsuleLLM)
- 🤗 Models: [haykgrigorian/timecapsulellm-1800-1875-london](https://huggingface.co/collections/haykgrigorian/timecapsulellm-1800-1875-london)
- 🤗 Dataset: [postgrammar/london-llm-1800](https://huggingface.co/datasets/postgrammar/london-llm-1800)
- 📝 Coverage: [Popular Science — "This AI thinks it's the 1800s"](https://www.popsci.com/technology/this-ai-thinks-its-the-1800s/) · [byteiota — "Student's 1800s-trained AI accidentally discovers real 1834 history"](https://byteiota.com/timecapsulellm-students-1800s-trained-ai-accidentally-discovers-real-1834-history/)
- 💬 Hacker News: [TimeCapsuleLLM: LLM trained only on data from 1800–1875](https://news.ycombinator.com/item?id=46590280)

### Ranke-4B / History LLMs (2025–2026)

A family of 4B-parameter models based on the **Qwen3** architecture, trained from scratch on 80B tokens of carefully time-stamped historical text drawn from a curated 600B-token dataset. Each model in the family has a fixed knowledge cutoff: **1913, 1929, 1933, 1939, or 1946**. The project is led by **Daniel Göttlich, Dominik Loibner, Guohui Jiang, and Hans-Joachim Voth** at the University of Zurich and Cologne University. Ranke-4B-1913 famously does not know who Adolf Hitler is (its closest match is a Hessian philosopher of the 19th century). The project explicitly aims to preserve, rather than scrub away, the normative judgements acquired during pre-training, treating the resulting prejudices and worldviews as a *feature* for historical research rather than a bug to be sanitised.

- 💻 GitHub: [DGoettlich/history-llms](https://github.com/DGoettlich/history-llms) (information hub) · pretraining, data, and post-training repos forthcoming under [DGoettlich](https://github.com/DGoettlich)
- 🤗 Organisation: [uzh-echist-org](https://huggingface.co/uzh-echist-org)
- 📄 Pre-release notes: [ranke-4b/prerelease_notes.md](https://github.com/DGoettlich/history-llms/blob/main/ranke-4b/prerelease_notes.md)
- 📝 Coverage: [byteiota — "History LLMs Train AI on Pre-1913 Texts to Kill Hindsight Bias"](https://byteiota.com/history-llms-train-ai-on-pre-1913-texts-to-kill-hindsight-bias/) · [GIGAZINE](https://gigazine.net/gsc_news/en/20251222-ranke-4b/)
- 💬 Hacker News: [History LLMs: Models trained exclusively on pre-1913 texts](https://news.ycombinator.com/item?id=46319826)

### Machina Mirabilis / GPT-1900 (2026)

An experiment by **Michael Hla** asking whether a 3.3B-parameter LLM trained from scratch on **pre-1900** text can independently arrive at quantum mechanics and relativity, directly testing Demis Hassabis's well-known proposal. The pre-training corpus (~22B tokens) was assembled from Institutional Books, the British Library Books dataset, and American Stories newspapers, and aggressively filtered to remove any document referencing Einstein, quantum mechanics, or other post-1900 physics. After mid-training on ~290M tokens of pre-1900 physics texts and a careful instruction-tuning + RL post-training pipeline, the model shows "glimpses of intuition" — for example, occasionally asserting that light "is made up of definite quantities of energy" or that gravity and acceleration are locally equivalent — but the author is openly cautious about claiming genuine out-of-distribution reasoning.

- 💻 GitHub: [michaelhla/gpt1900](https://github.com/michaelhla/gpt1900) (forked from [karpathy/nanochat](https://github.com/karpathy/nanochat))
- 🌐 Demo: [gpt1900.com](https://gpt1900.com/)
- 🤗 Models: [mhla/gpt-1900 collection](https://huggingface.co/collections/mhla/gpt-1900)
- 🤗 Dataset: [mhla/gpt1900-instruct-data](https://huggingface.co/datasets/mhla/gpt1900-instruct-data)
- 📝 Blog post: ["Machina Mirabilis"](https://michaelhla.com/blog/machina-mirabilis.html) (Michael Hla, March 2026)
- 📄 Eval prompts: [`EVAL.json`](https://github.com/michaelhla/gpt1900/blob/master/EVAL.json) · [best generations](https://github.com/michaelhla/gpt1900/blob/master/results/physics_eval_v11/best_generations.md)

### Mr. Chatterbox (2026)

A ~340M-parameter chatbot (roughly the size of GPT-2-Medium) trained from scratch by **Trip Venturella** on 28,035 Victorian-era British texts published between **1837 and 1899**, drawn from the British Library's `blbooks` dataset. Built using Andrej Karpathy's [nanochat](https://github.com/karpathy/nanochat), it totals approximately 2.93 billion training tokens after filtering. The model is unapologetically weak compared to frontier systems — illustrating just how data-hungry "public-domain-only" LLMs are — but it is one of the cleanest demonstrations that an entirely out-of-copyright LLM is feasible on modest hardware, and it does answer in a recognisably 19th-century voice.

- 🤗 Source model: [tventurella/mr_chatterbox_model](https://huggingface.co/tventurella/mr_chatterbox_model)
- 🌐 Demo (HF Space): [tventurella/mr_chatterbox](https://huggingface.co/spaces/tventurella/mr_chatterbox)
- 🔌 LLM plugin: [simonw/llm-mrchatterbox](https://github.com/simonw/llm-mrchatterbox)
- 📝 Author's write-up: ["Mr. Chatterbox, or, The Modern Prometheus"](https://www.estragon.news/mr-chatterbox-or-the-modern-prometheus/) (Trip Venturella, Estragon)
- 📝 Coverage: [Simon Willison's Weblog](https://simonwillison.net/2026/Mar/30/mr-chatterbox/) · [GIGAZINE](https://gigazine.net/gsc_news/en/20260401-mr-chatterbox/)
- 💬 Hacker News: [Mr. Chatterbox is a Victorian-era ethically trained model](https://news.ycombinator.com/item?id=47582056) · [earlier thread](https://news.ycombinator.com/item?id=47575062)

### Talkie-1930 (2026)

The largest publicly released vintage LLM to date: a **13B-parameter** model trained on 260B tokens of pre-1931 English-language text (books, newspapers, periodicals, scientific journals, patents, and case law), built by **Alec Radford** (co-creator of GPT), **Nick Levine**, and **David Duvenaud**. The 1930 cutoff was chosen because U.S. copyright law places texts from that year into the public domain. The team also released `talkie-web-13b-base`, a "modern twin" with identical architecture and training FLOPs but trained on FineWeb, to enable controlled comparisons. The instruction-tuned `talkie-1930-13b-it` was post-trained without any modern chat data — instead using QA pairs extracted from pre-1931 etiquette manuals, encyclopaedias, letter-writing guides, and poetry collections, plus online DPO with an LLM-as-judge.

- 💻 GitHub: [talkie-lm/talkie](https://github.com/talkie-lm/talkie) ([organisation](https://github.com/talkie-lm))
- 🌐 Website / chat demo: [talkie-lm.com](https://talkie-lm.com/) · [chat](https://talkie-lm.com/chat)
- 📄 Announcement: [*Introducing talkie: a 13B vintage language model from 1930*](https://talkie-lm.com/introducing-talkie)
- 🤗 Source models: [talkie-lm/talkie-1930-13b-base](https://huggingface.co/talkie-lm/talkie-1930-13b-base) · [talkie-lm/talkie-1930-13b-it](https://huggingface.co/talkie-lm/talkie-1930-13b-it) · [talkie-lm/talkie-web-13b-base](https://huggingface.co/talkie-lm/talkie-web-13b-base) (modern-comparison twin)
- 📝 Coverage: [Benjamin Breen — "Are 'Vintage LLMs' the start of a new humanistic field?"](https://resobscura.substack.com/p/are-vintage-llms-the-start-of-a-new) · [Sesame Disk](https://sesamedisk.com/talkie-1930-vintage-language-model/) · [Let's Data Science](https://letsdatascience.com/news/talkie-releases-13b-vintage-language-model-trained-on-1930s-757bdb99)
- 💬 Hacker News: [Talkie: a 13B vintage language model from 1930](https://news.ycombinator.com/item?id=47927903)

## Related reading

A small selection of foundational and contextual writing on the field. Contributions of further high-quality references are welcome.

- Owain Evans — [*Vintage Large Language Models*](https://owainevans.github.io/talk-transcript.html) (talk transcript) · [PDF](https://owainevans.github.io/pdfs/vintage_LLMs.pdf). The piece that named the field.
- Benjamin Breen — [*Are 'Vintage LLMs' the start of a new humanistic field?*](https://resobscura.substack.com/p/are-vintage-llms-the-start-of-a-new), Res Obscura, April 2026. A historian's ranked taxonomy of useful and not-so-useful research applications.
- Hosseini, Beelen, Colavizza, Coll Ardanuy — [*Neural Language Models for Nineteenth-Century English*](https://arxiv.org/abs/2105.11321), Journal of Open Humanities Data, 2021. Earlier (BERT/word2vec) work on time-sliced 19th-century corpora.
- *Large Language Models based on historical text could offer informative tools for behavioral science*, [PNAS, 2024](https://www.pnas.org/doi/10.1073/pnas.2407639121). Argues for vintage LLMs as instruments for behavioural science beyond the WEIRD present.

## Contributing

Contributions are very welcome! This is a young, fast-moving field, and the list above is certainly incomplete. To suggest an addition or correction, please open a pull request that:

1. Adds the project in the appropriate chronological position.
2. Uses the same field structure as existing entries (short description; then GitHub, website / demo, paper, source HuggingFace, quantised / fine-tuned HuggingFace artefacts, reputable online publications, Hacker News discussions — as applicable).
3. Cites only reputable sources (academic venues, established publications, official author write-ups, well-known technical blogs). Please avoid SEO blogspam and AI-generated summaries.
4. Prefers project-from-scratch *vintage* models over plain fine-tunes or "system-prompt cosplay" of modern LLMs, although carefully-scoped fine-tunes (such as MonadGPT) are in scope.

Please also feel free to open issues to discuss whether a borderline project belongs on the list.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors of this list have waived all copyright and related or neighbouring rights to this work.
