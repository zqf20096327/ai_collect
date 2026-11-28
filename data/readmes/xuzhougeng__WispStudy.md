<p align="center">
  <img src="assets/branding/app-icon.png" width="96" alt="The Wisp Study app icon">
</p>

<h1 align="center">Wisp Study</h1>

<p align="center">
  <b>English</b> · <a href="README.zh-CN.md">简体中文</a>
</p>

<p align="center">
  <b>A local-first literature library: collect, screen and read papers, and ask your library questions.</b><br>
  Drawn natively with Rust + GPUI. Your papers and PDFs stay on your computer, and each library is one folder.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/platform-Windows%20%7C%20macOS-lightgrey" alt="Windows and macOS">
  <img src="https://img.shields.io/badge/built%20with-Rust%20%2B%20GPUI-dea584?logo=rust" alt="Built with Rust and GPUI">
  <a href="LICENSE"><img src="https://img.shields.io/github/license/xuzhougeng/WispStudy?color=green" alt="MIT license"></a>
  <img src="https://img.shields.io/badge/status-alpha-orange" alt="Alpha">
</p>

<p align="center">
  <a href="https://xuzhougeng.github.io/WispStudy/en/"><b>Home page</b></a> ·
  <a href="#install"><b>Install</b></a> ·
  <a href="#features">Features</a> ·
  <a href="#faq">FAQ</a> ·
  <a href="https://xuzhougeng.github.io/WispStudy/en/tutorials/">Tutorials</a> ·
  <a href="docs/ZOTERO.md">Zotero import</a> ·
  <a href="docs/CLI.md">Command line and MCP</a> ·
  <a href="docs/DATA.md">Data and privacy</a> ·
  <a href="docs/DEVELOPMENT.md">Development</a>
</p>

<p align="center">
  <img src="docs/images/en/library.png" width="100%" alt="The Library page of Wisp Study: views and tags on the left, the paper list in the middle, the selected paper's details and notes on the right.">
</p>

> [!NOTE]
> Wisp Study is at an early stage and changes fast. The interface comes in English and Chinese; switch in “Settings › General › Interface language” (设置 › 通用 › 界面语言). It takes effect at once and is saved. If this is your first time, follow the [tutorials](https://xuzhougeng.github.io/WispStudy/en/tutorials/) (also in the app: the book at the top right of the home page) and build a library from nothing; the later ones each cover one research task: close reading, asking, extracting, writing a review, writing a paper, revising. If you run into a problem or have an idea, [open an issue](https://github.com/xuzhougeng/WispStudy/issues), or better, send a pull request.

## Why Wisp Study

**🔒 Local-first: the papers are yours.** No account, no cloud. Each library is its own folder under the data directory, holding its database, PDFs and custom fields, so it can be backed up alone or copied away whole. Removing something only moves it to `removed/`; nothing is really lost. What leaves your computer is listed item by item in [Data and privacy](docs/DATA.md).

**🐋 Import broadly first, then let the assistant help you screen.** Save search queries for PubMed, Europe PMC, Crossref and arXiv and import in bulk. The assistant reads every paper and gives a suggestion, a reason, and one sentence quoted word for word from the text as evidence. A suggestion is only a suggestion: whether a paper is included is yours to confirm.

**💬 Answers carry sources, and the sources open.** Ask the whole library or a single paper. When the material is not enough, the assistant searches the full texts and reads them page by page on its own. A `[P3 p.5]` in an answer can be clicked: the PDF opens at that page with the quoted sentence highlighted.

**⚡ A native interface, not a web page.** The whole interface is drawn on the GPU by Rust and [GPUI](https://www.gpui.rs/): no WebView, no Electron. PDFs are rendered by [hayro](https://github.com/LaurenzV/hayro), in pure Rust, with no system PDF library.

## Install

Download from the [release page](https://github.com/xuzhougeng/WispStudy/releases/latest):

| Platform | File | Notes |
|---|---|---|
| **macOS**, Apple silicon | `WispStudy-v<version>-macos-arm64.dmg` | Signed with a Developer ID and notarized by Apple. Open it and drag Wisp Study into Applications |
| **macOS**, Intel | `WispStudy-v<version>-macos-x64.dmg` | As above |
| **Windows** 10 / 11 (x64), installer | `WispStudy-v<version>-windows-x64-setup.exe` | Installs for the current user (`%LOCALAPPDATA%\Programs\Wisp Study`), needs no administrator rights, Authenticode-signed |
| **Windows** 10 / 11 (x64), portable | `WispStudy-v<version>-windows-x64.zip` | Unzip and run `WispStudy.exe`; writes nothing to the registry, Authenticode-signed |
| **Linux** (x64) | `WispStudy-v<version>-linux-x64.tar.gz` | Unpack and run `wisp-study`; unsigned, and not tested on a real machine |

Wisp Study used to be called Wisp Paper. The old version's automatic update cannot find the renamed releases, so download the new version from the release page: the Windows installer replaces the old version in place; on macOS, once `Wisp Study.app` is installed you can delete the old `Wisp Paper.app`. Libraries and settings stay where they are, with nothing to migrate.

The command-line tool `wisp` ships in the package: next to the main program on Windows and Linux, at `Wisp Study.app/Contents/MacOS/wisp` on macOS.

Building from source needs Rust (the version is in `rust-toolchain.toml`; rustup installs it for you); on Windows it also needs the MSVC build tools.

```sh
git clone https://github.com/xuzhougeng/WispStudy
cd WispStudy
cargo run --release
```

To have a look first, generate a folder of demo data that does not touch your real library:

```sh
cargo run -p wisp_core --example seed -- /tmp/wisp-demo some.pdf
WISP_STUDY_HOME=/tmp/wisp-demo cargo run
```

### Building the exe on Windows

The exe has to be built on Windows; it cannot be cross-compiled from macOS or Linux. Install two things first (once):

```powershell
winget install Microsoft.VisualStudio.2022.BuildTools --override "--add Microsoft.VisualStudio.Workload.VCTools --includeRecommended --passive"
winget install Rustlang.Rustup
```

The first installs the MSVC build tools (“Desktop development with C++”, Windows SDK included). The first time `cargo` runs in the repository, rustup installs the version named in `rust-toolchain.toml`.

For the exe alone, run in the repository root:

```powershell
cargo build --release -p wisp_study -p wisp_cli
```

This produces `target\release\wisp_study.exe` (the app, with no console window) and `target\release\wisp.exe` (the command line; `wisp mcp` is the MCP server). The icon and `assets/` are compiled into the exe, so no other files need to go with it.

To make the same packages as the release page, run `scripts/package-windows.ps1`:

```powershell
pwsh -File scripts/package-windows.ps1 -NoInstaller   # the portable zip only: dist\WispStudy-v<version>-windows-x64.zip
winget install JRSoftware.InnoSetup                   # for the installer, install Inno Setup 6 first
pwsh -File scripts/package-windows.ps1                # the zip plus dist\WispStudy-v<version>-windows-x64-setup.exe
```

`-Sign` signs with SSL.com eSigner and needs the `ESIGNER_*` variables set; it is for the release workflow, not for trying things locally. Before a manual run you can set `$env:WISP_STUDY_HOME="C:\tmp\wisp-test"` so that the library in `Documents\WispStudy` is not touched.

Asking, the library wizard, screening, translation and the model's sectioning on the Writing page need a model provider, set up in “Settings › AI”: the Claude API, an OpenAI-compatible chat/completions endpoint, or OpenAI's Responses. You can add several models and say which one asking, bulk screening, translation and tidying full text each use, and how hard each thinks.

## Features

- **Libraries**: several independent libraries, each with a name, a topic and an accent color.
- **Collect**: paste a DOI or PMID, drop in PDFs, import BibTeX / RIS, or enter a record by hand; you can also [import from a local Zotero database](docs/ZOTERO.md) its records, tags, notes and downloaded PDFs. Deduplicated by DOI, PMID and title. Bulk imports show progress and a summary of the result.
- **Organise**: search, filter, sort; reading status, inclusion decision, favorites, tags, notes; fields each library defines for itself; a trash; export to BibTeX and CSV.
- **Saving notes**: “My notes” can be saved to a signed-in Notion MCP, or exported as Markdown with image attachments. On the Ask page you can pick earlier questions, preview them and save; the original notes and conversations stay. The assistant can call the same tools, see [exporting notes](docs/CLI.md#笔记保存与导出).
- **Search and import**: save search queries, try a search before importing, undo any import as a whole; scheduled updates are available.
- **Library wizard**: write down a topic, and the assistant drafts a few queries for each database and tries each one out; you pick the sound ones.
- **Screening**: the assistant reads several papers at once and gives inclusion suggestions with evidence from the text, and you confirm; a whole group can also be accepted as suggested.
- **Translation**: titles and abstracts translated in one click; translations are saved in the library.
- **Writing**: write a manuscript part by part (abstract, introduction, methods, results, discussion) with the sentences the library's papers wrote in that same part listed beside it: the openings of each paper before you start, and once you are writing, the sentences closest to the paragraph at hand; this works for Chinese text too. A sentence can be inserted as a citation, copied, or located in its PDF. PDFs in the library are read by layout and split into sections by their headings; where there are no headings to go by (a Nature introduction, say) a model can decide, and a model can read the pages of a scan. A manuscript can start from nothing, from an existing Word / Markdown file, or from a review the assistant wrote; the assistant leaves comments and proposes changes like Word's review, for you to accept; the exported Word file is written back into the original, with comments, and changes can be recorded as tracked changes. There are two ways of writing, switched above the outline: in “I write” you write and the assistant helps beside you; in “Assistant writes” the outline is on the left, the conversation with the assistant in the middle and the manuscript on the right: the assistant looks up the papers and writes, you watch it write and edit by hand at any time, and every section can be turned back to an earlier version.
- **Asking**: ask the library or a single paper; answers are laid out in Markdown. The sentences the assistant quotes are compared word for word with the original and the result is marked on the source; clicking a source highlights it in the PDF. When asking about one paper, the conversation and the PDF sit side by side, and text selected on the PDF or a region cut out as a picture goes straight into the question; text in an answer can be selected, copied and quoted. Type `/` for commands (search the full texts, find citations, write a review in stages, compare papers, check claim by claim); pictures can be pasted; conversations are kept as history and can be continued, and an answer can be saved as a note on the paper.
- **PDF**: read right in the detail panel, whose width can be dragged; zoom, fit width or fit page; select text, copy, take a screenshot; underline, highlight and attach notes. Annotations are saved as separate metadata and drawn over the page, and the assistant can read the text, the notes and where they are. A PDF that gives no text says why, and a model that can see can read its pages.
- **Figures**: frame a figure or a table on a PDF and save it to Figures, under Favorites; the figure number and caption are read off the page, or a model can look at the picture and write a caption, tags and a reading of it. Find figures by tag and keyword, and go back to the page they came from in one click.
- **Find open full text**: look up open-access full texts in bulk for papers that have no PDF, and attach the downloads to their records; paywalls are not bypassed.
- **Command line and MCP**: without opening a window, `wisp` creates libraries, imports local PDFs / folders, BibTeX / RIS and Zotero, and reads and writes the same data folder; `wisp mcp` hands the same set of tools to an outside AI client. See [docs/CLI.md](docs/CLI.md) and [SKILL.md](SKILL.md).
- **Settings**: light / dark, rebindable shortcuts, a global proxy and one per model provider. Changes are saved as you make them.

The detail of each is in [docs/FEATURES.md](docs/FEATURES.md) (in Chinese).

## FAQ

### Can one paper be in several libraries? If I take notes in library A, can I see them in library B?

It can be in both, but the notes are not shared. Each library is an independent folder and deduplication happens within a library, so the same paper can be imported into A and into B. Each side holds a record of its own: notes, annotations, tags, reading status and the inclusion decision belong to the library they were made in and are not synchronised.

This is deliberate. A library stands for one topic, and the same paper is read differently under different topics: the notes you took on it in A may be of no use in B, and B may not even need its full text, just the abstract. So most of the time one paper belongs in one library.

If you cannot decide how to split, start with one library. For example a “Learning” library just for reading papers and picking things up: its topics can be a mix, told apart by tags. When one direction grows into a project of its own, create a new library and use “Move to library…” in a paper's right-click menu to move the relevant papers over; the PDF, the annotations and the conversations about the paper go with it. A paper both libraries need can be copied with “Copy to library…”, which leaves the original where it is.

### Why are there no groups (folders, collections) inside a library?

The library itself is the group. Inside it, use tags.

A folder asks a paper to live in exactly one place, and papers rarely divide that cleanly: does a paper that studies root hair development with single-cell sequencing go under “single-cell” or under “root hair”? The ugly duckling theorem (Watanabe, 1969) says just this: without prior assumptions, any two objects are in theory equally similar, and how to classify them depends entirely on which features you choose to weigh.

Tags do not ask for a single home. A paper can carry several; in the sidebar, hold `⌘` / `Ctrl` to select more than one tag and keep only the papers that carry all of them, or hold `⌥` / `Alt` and click a tag to exclude it. On import from Zotero, collection paths become tags as well.

### Can two libraries be linked?

No, and this is deliberate too. From the start, a library was designed as an independent whole, with its own topic, inclusion criteria, tags and custom fields. Two libraries serve different goals and are best kept apart, so that one does not contaminate the other.

When a question does span several libraries, give it to the assistant on the home page: it can read every library on the shelf. Say “compare what libraries ‘A’ and ‘B’ have on …”, and it lists papers, searches the full texts and reads the originals in each; every source in its answer says which library it comes from, and a click opens that paper in that library. The libraries are read-only from there: it changes none of them.

What you have kept is one click away too: the star at the top right of the home page lists the starred papers, figures, methods and introductions of every library together, each saying which library it is in. It is a list to look through and go from: a click opens that library at that item, and each library's own Favorites still shows only its own.

Writing need not wait for a tidy library either: the pen beside the star lists every manuscript, and New manuscript starts one right away, with no library chosen. Have the assistant look things up as you write, then bind the manuscript to a library you already have (the manuscript, its conversations and the papers gathered go into it, and every paper of that library can be cited), or make a new library of what was gathered; an article that cites nothing can stay in no library.

### Will a large library burn tokens and give worse answers? How should I set up my libraries?

What one question costs depends on the current list, not on the whole library, and it has a ceiling. When you ask the library, the scope is the papers shown in the list (as set by the view, tags, search and filters): the ones most relevant to the question are given as full records (title, abstract, notes), those that do not fit are given as titles only, and of the full texts only the few dozen pages most relevant to the question are sent. So the cost does not grow without limit as the library grows, though a long list does cost more than a short one. When the material is not enough, the assistant goes on to search the full texts and read pages itself.

Saving tokens and getting better answers are the same thing: narrow the scope first, then ask.

- Click a tag, switch to a view or search for a word, then ask: the model is given only that part of the library.
- If you care about one paper, ask in that paper's “Ask”: the model reads its full text.
- When the list is long, put words the papers themselves would use into the question (English terms for papers in English): which papers get a full record is ranked by how often those words appear in the title, abstract, tags and notes.
- To check, open “Papers” at the top of the conversation: it says for each paper whether the model was given the full record or only the title, and how many pages of full text. Sources in an answer can be opened, and the sentences the assistant quotes are compared word for word with the original. With a DeepSeek model, the line below an answer also says how many tokens the question used and roughly what it cost.

Some advice on setting up libraries:

- **One library, one goal**: a project, a review, a field you want to learn. Whether to split depends on whether the goals and inclusion criteria differ, not on the number of papers.
- **Write the topic well.** The assistant reads it when it drafts queries, screens and answers.
- **Import broadly first, then screen.** Under one screening goal each paper is read only once, the irrelevant ones go to the trash, and what remains is the scope of every later question. A clean library matters more than a small one.
- **Give the bulk work to a cheap model.** Which model screening, translation and tidying full text each use is set separately in “Settings › AI”; keep the strong one for asking.

## Documentation

Apart from the tutorials, the documents below are in Chinese.

| | |
|---|---|
| [Tutorials](https://xuzhougeng.github.io/WispStudy/en/tutorials/) | Eighteen tutorials written around research tasks, with screenshots: building a library, talking first and building later, migrating, reading just one PDF, close reading, mind maps, reading side by side, listening to a paper, group-meeting slides, asking, picking papers by impact factor and quartile, extracting, writing a review, writing a paper, writing directly vs in Wisp Study, revising, keeping up with new papers, several topics at once |
| [A library, start to finish](docs/TUTORIAL.md) | The original record of building a “plant single-cell transcriptomics” library from nothing (v0.2.0) |
| [Features in detail](docs/FEATURES.md) | What each page can do |
| [Data and privacy](docs/DATA.md) | Where the files are, and what leaves your computer |
| [Command line and MCP](docs/CLI.md) | How to use `wisp`, the list of tools, MCP configuration |
| [Agent skill](SKILL.md) | The `SKILL.md` for outside agents: what is supported, the steps of building a library and importing, command examples |
| [Development](docs/DEVELOPMENT.md) | Building, testing, code structure |

## Acknowledgements

The literature side is ported from [BiblioCell](https://github.com/xuzhougeng/BiblioCell) (its datasets and web version are not ported); the app's structure and the way Markdown in answers is read follow [quiet-md](https://github.com/s1dashu/quiet-md).

## License

The code is released under the [MIT](LICENSE) license. Bundled third-party code and assets are listed in [THIRD_PARTY.md](THIRD_PARTY.md).
