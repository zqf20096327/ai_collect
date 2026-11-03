<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/images/header-en-dark.svg">
    <img alt="AlphainZ: your literature research partner. Find new papers, highlight key points, sync across devices, ask about any passage, semantic search of text and figures." src="docs/images/header-en-light.svg" width="643">
  </picture>
</p>

<p align="center">
  <a href="https://github.com/Alphainfix/AlphainZ/releases/latest"><img alt="Latest release" src="https://img.shields.io/github/v/release/Alphainfix/AlphainZ?style=flat-square&color=8c3517"></a>
  <a href="https://www.zotero.org"><img alt="Zotero 7 or later" src="https://img.shields.io/badge/Zotero-7%2B-555?style=flat-square"></a>
  <a href="LICENSE"><img alt="License: AGPL-3.0" src="https://img.shields.io/badge/license-AGPL--3.0-blue?style=flat-square"></a>
</p>

<p align="center">
  <a href="https://alphain.app/z/">Website</a> ·
  <a href="https://github.com/Alphainfix/AlphainZ">GitHub</a> ·
  <a href="https://github.com/Alphainfix/AlphainZ/releases/latest">Download</a> ·
  <a href="https://github.com/Alphainfix">Author: Alphainfix</a>
</p>

<p align="center"><b>English</b> · <a href="README.zh-CN.md">简体中文</a></p>

**Free and open source. Customize it your way.** AlphainZ is a research assistant inside Zotero. You chat
with it using your own models and API keys, and there is no account to sign up for. Part of its front end
is forked from [Beaver](https://github.com/jlegewie/beaver-zotero) by Joscha Legewie; its back end lets you
talk to the model providers directly, with no one else's server in between: simple, safe and [affordable](#cost).

<p align="center">
  <img alt="Left: the AlphainZ pane in Zotero's PDF reader. A highlighted sentence was sent to AlphainZ, which answers 'Why the underestimate?' citing the paper and offers to save the answer to the highlight. Right: semantic search accuracy on a demo library with Gemini Embedding 2 (semantic search: the best match for 18 of 18 questions, against 0 for Zotero's own search; describing a figure: in the top 3 matches 11 times out of 12), and how AlphainZ connects your Zotero library directly to the model you choose." src="docs/images/overview-en.png">
</p>

## What it does

### Ask your whole library

AlphainZ decides how to look, and combines:

- **A vector index of your full texts.** Every PDF is split into passages and embedded, either by a cloud
  model (Gemini Embedding 2, OpenAI) or by one on your own computer (EmbeddingGemma 2 in Ollama). Search
  matches by meaning: a question finds the passages that mean the same thing even when they share no
  words, or are in another language. Indexing runs in the background and can be switched off.
- **Semantic figure search.** With an embedding model that also reads images, every page is indexed as a
  picture as well: describe a figure and it matches the page.
- **Text recognition down to the sentence.** The text of each PDF is read with the position of every
  sentence, so answers cite the sentence they rest on, and a click opens the PDF there with it
  highlighted. Scanned pages and figures are read from the page image by models that see images.
- Metadata (authors, years, journals), keyword search, and browsing by collection or tag.

### Ask about what you are reading

Select a passage, a figure or a table and ask from the popup, or ask about the whole paper in the side
pane.

### Keep the answer with the highlight

A question asked from a selection is anchored to a highlight. When the answer is in, a card at the bottom
of the side pane (in the screenshot above) saves the question and the answer into the highlight's comment:
they stay in the PDF, sync with Zotero, and reopen the conversation when you click the highlight.

### And more

- **Write into Zotero.** Add highlights and comments to the PDF, write notes, tag items and file them into
  collections; AlphainZ asks before each change.
- **Look beyond your library.** Search the literature through OpenAlex and add what you find to a
  collection.
- **Keep long chats affordable.** Older exchanges are summarized as a chat grows, and every question has
  limits on output and steps.
- **Use multiple computers.** Conversations and settings can sync through Zotero or a folder you choose
  (iCloud Drive, OneDrive, ...). API keys never leave the computer you entered them on.
- **Serve other agents.** Turn on Settings → Advanced → MCP Server, and AlphainZ writes a small bridge,
  `alphainz-mcp-stdio.mjs`, into your Zotero data folder. Add it to a client such as Claude Desktop as a
  stdio server run with `node`, and the client can search your library while Zotero is open.

## Accuracy of semantic image and text search

**A demonstration library.** Six synthetic papers ([`docs/benchmark`](docs/benchmark)) and 36 questions,
run through AlphainZ's search with no language model involved. The semantic questions avoid each paper's
own words, so only a match by meaning can find them:

| Question | AlphainZ with<br>EmbeddingGemma&nbsp;2<br>(local, free) | AlphainZ with<br>Gemini&nbsp;Embedding&nbsp;2<br>(your own API key) | Zotero's<br>built&#8209;in&nbsp;search |
|---|:-:|:-:|:-:|
| Semantic search,<br>English questions (12) | 12 of 12 best matches | 12 of 12 best matches | 0 of 12 matched |
| Semantic search, Chinese<br>questions on English papers (6) | 6 of 6 best matches | 6 of 6 best matches | 0 of 6 matched |
| Describing a figure (12) | 5 best matches,<br>8 top-3 matches | 6 best matches,<br>11 top-3 matches | not possible |
| Exact keywords (6) | 5 of 6 best matches¹ | 5 of 6 best matches¹ | 6 of 6 matched |

¹ Semantic search alone. AlphainZ also searches by keyword, which matches the sixth.

**A real library.** On a working research library of 249 PDFs (18,986 passages), with 15 semantic
questions (8 in English, 7 in Chinese), the paper holding the answer was the best match 12 times with
EmbeddingGemma 2 and 11 times with Gemini Embedding 2 (mean reciprocal rank 0.875 and 0.856, where 1 means
the right answer always comes first; OpenAI's text-embedding-3-large 0.813). With EmbeddingGemma 2, the
best match for each of the 7 Chinese questions was its English passage. Indexing that library cost
nothing on a MacBook Air (about 16 passages a second) and about $1 with Gemini.

## Compared with similar tools

| | AlphainZ | Beaver | Zotero GPT | PapersGPT |
|---|:-:|:-:|:-:|:-:|
| Works inside Zotero, on your own library | ✅ | ✅ | ✅ | ✅ |
| Searches the full text of the whole library | ✅ | ✅¹ | ❌² | ✅ |
| Matches a figure from a description | ✅ | ❌ | ❌ | ❌ |
| Cites the sentence and opens the PDF there | ✅ | ✅ | ❌ | 🟡 paper only |
| Writes highlights and notes into Zotero | ✅ | ✅ | 🟡 Pro only | 🟡 notes only |
| Your own API key, any OpenAI-compatible endpoint | ✅ | ✅ | ✅ | ✅ |
| Local models through Ollama | ✅ | ❌³ | – | ✅ |
| No account, no subscription | ✅ | ❌ | – | – |
| Open source | ✅ AGPL | ✅ AGPL | 🟡 core only⁴ | ✅ AGPL |

✅ offered · 🟡 partly · ❌ not offered, according to the product's own pages · – not stated. Checked in late October 2026 from each project's README and Zotero forum thread; corrections are welcome.<br>
¹ Semantic search of full texts on paid plans; the free plan searches titles and abstracts semantically.<br>
² Asks about the open PDF or the items you select.<br>
³ Requests run through Beaver's servers.<br>
⁴ The core is AGPL; Pro features are closed.

General chat-with-PDF services such as NotebookLM or ChatPDF work on files uploaded to their cloud,
outside Zotero.

## Models

Built in: DeepSeek, OpenRouter, Zhipu (BigModel), Google Gemini, OpenAI, and Ollama on your own computer.
Anything else that speaks the OpenAI API, such as a proxy, an institutional gateway or a local server, can
be added by hand, on Chat Completions or on the Responses API.

Each model can be told which thinking levels it takes (the Thinking menu then offers exactly those), how
large its context window is (a long chat is summarized before it fills 70% of it), and the most output one
answer may use.

## Cost

AlphainZ itself is free; what you pay is the model provider's token price. Averaged over 62 real
questions (about 80,000 tokens read per question, 83% of them from the provider's cache, and about 3,000
written), at the providers' list prices:

| Model | Per question | 100 questions a day |
|---|:-:|:-:|
| DeepSeek V4.1 Flash | about $0.004<br>($0.008 at peak hours) | about $0.40 |
| OpenAI gpt-6-luna | about $0.004 | about $0.40 |

So even a heavy day of 100 questions costs about 40 cents. A local model in Ollama costs nothing.
Indexing your library is separate: free with EmbeddingGemma 2 on your own computer, and about $1 per 250
papers with Gemini Embedding 2.

List prices as of late October 2026. DeepSeek charges double on weekdays during Beijing business hours
(01:00–04:00 and 06:00–10:00 UTC).

## Install

1. Download the `.xpi` file from the [latest release](https://github.com/Alphainfix/AlphainZ/releases/latest).
2. In Zotero 7 or later: Tools → Plugins → the gear icon → Install Plugin From File…, and choose the file.
3. Open AlphainZ from its toolbar button, then Settings → Model → Add provider: paste a key and pick a
   model.

Zotero checks this repository for new versions by itself.

## Privacy

- Your questions, and the parts of papers they need, go from your computer straight to the model provider
  you chose. There is no AlphainZ server.
- API keys are stored in Zotero's `prefs.js` on the computer you entered them on, in plain text, like other
  Zotero preferences.
- The search index, conversations and caches stay in `alphainz.sqlite` in your Zotero data folder.
- Literature search sends only the search terms (and your OpenAlex key, if you added one) to OpenAlex.

## Building from source

```bash
git clone https://github.com/Alphainfix/AlphainZ.git
cd AlphainZ/plugin
npm install
cp .env.production.example .env.production
npm run build        # writes .scaffold/build/alphain-z.xpi
npm test
```

The values in `.env.production` are inert placeholders: a component inherited from Beaver still
constructs a client it never uses, and fails to load without them.

## License

AlphainZ is free software under the [GNU Affero General Public License v3.0 or later](LICENSE), as is
Beaver, on which it is based. The screenshots and the benchmark use synthetic papers written for this
repository.

- [Beaver](https://github.com/jlegewie/beaver-zotero), by Joscha Legewie: the original plugin.
- [MuPDF](https://mupdf.com), by Artifex: PDF text and rendering (AGPL-3.0).
- [sentencex](https://github.com/wikimedia/sentencex), by Santhosh Thottingal: sentence segmentation (MIT).
- [Zotero Plugin Template](https://github.com/windingwind/zotero-plugin-template): the build scaffold.

Comparison sources: [Beaver](https://github.com/jlegewie/beaver-zotero) and its
[forum thread](https://forums.zotero.org/discussion/126573/),
[Zotero GPT](https://github.com/MuiseDestiny/zotero-gpt),
[PapersGPT](https://github.com/papersgpt/papersgpt-for-zotero).
