# AI for OSINT

AI tools, models and agent tooling that open-source investigators and journalists use, with the limits written next to each one.

**146 entries. Every link was opened on 2026-11-16.**

Most AI tool lists tell you what a tool promises. This one also tells you two things that matter more in an investigation: **where your material goes** when you use the tool, and **what is known about how it fails**.

## How to read the tables

- **Runs** is the source-protection column. *Local* means the tool works on your own machine and your files stay there. *Cloud* means you upload material to someone else's servers. Do not put leaked documents, unpublished footage or anything that identifies a source into a cloud tool unless you have decided that risk is acceptable.
- **Type** is *Open source*, *Free web tool*, *Freemium*, *Paid* or *Restricted* (available only to vetted organisations or on request).
- **Known limit** is a documented limitation or risk. Where it is blank, we found nothing documented on the pages we checked. That is not the same as the tool having no limits.
- **Last activity** is the latest release, commit or post we could see. Tools marked *(stale)* have had no visible update for over a year.

## Three rules before you use any of these

1. **AI output is a lead, not a finding.** A transcript, a translation, a location guess or a detector score tells you where to look. Check it against the source material before it goes into a story.
2. **Detectors and geolocation models are confidently wrong, often.** Published tests in the last section show deepfake detectors losing much of their accuracy on real-world media, and language models inventing locations and citations. Never publish a detector score as proof.
3. **Speech-to-text models can invent words.** Check quotes against the audio.

## What is deliberately left out

Face-recognition services that identify private individuals, people-search and username or phone lookup tools, anything built on breached data, and penetration-testing toolkits. This list is about verifying media, reading documents, working across languages, analysing imagery and public records.

## Contents

- [Transcription and speech](#transcription-and-speech) (12)
- [Translation and languages](#translation-and-languages) (12)
- [OCR and documents](#ocr-and-documents) (12)
- [Searching big document sets](#searching-big-document-sets) (12)
- [Image and video verification](#image-and-video-verification) (16)
- [Geolocation and chronolocation aids](#geolocation-and-chronolocation-aids) (11)
- [Satellite and geospatial ML](#satellite-and-geospatial-ml) (16)
- [Entities, networks and text analysis](#entities-networks-and-text-analysis) (13)
- [MCP servers for OSINT](#mcp-servers-for-osint) (14)
- [Agent skills, prompts and agent frameworks for investigations](#agent-skills-prompts-and-agent-frameworks-for-investigations) (13)
- [Guidance, ethics and tested evaluations](#guidance-ethics-and-tested-evaluations) (15)

## Transcription and speech

| Tool | What it is for | Type | Runs | Known limit | Last activity |
|---|---|---|---|---|---|
| [AI4Bharat IndicConformer](https://huggingface.co/ai4bharat/indic-conformer-600m-multilingual) | Transcribes speech in the 22 scheduled Indian languages with one open model. | Open source | Local | Gated on Hugging Face: you must log in and share contact details to download the files. |  |
| [aTrain](https://github.com/aTrainTranscription/aTrain) | Offline GUI for transcribing interviews with speaker diarisation, aimed at researchers. | Open source | Local |  | 2026-11 |
| [Buzz](https://github.com/chidiwilliams/buzz) | Desktop app that transcribes and translates audio offline with Whisper, no command line needed. | Open source | Local | Same Whisper models, so the same hallucination risk. | 2026-11 |
| [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | Runs Whisper models several times faster on modest hardware for bulk transcription of footage and recordings. | Open source | Local | Same Whisper models, so the same hallucination risk on silence, noise and low-resource languages. | 2026-11 |
| [Good Tape](https://goodtape.io/) | Hosted transcription service built for newsrooms; upload a recording and get a searchable transcript. | Freemium | Cloud | Recordings are uploaded to a third-party cloud service; weigh that for sensitive sources. |  |
| [noScribe](https://github.com/kaixxx/noScribe) | Desktop app for interview transcription with speaker identification, built on Whisper and pyannote, fully offline. | Open source | Local | Same Whisper models, so the same hallucination risk. | 2026-11 |
| [NVIDIA Parakeet TDT v3](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3) | Fast open speech-to-text model for European languages with timestamps, an alternative to Whisper for long recordings. | Open source | Local | Model card: accuracy varies by language, accent, noise and domain; European languages only, no Indian languages. |  |
| [Omnilingual ASR](https://github.com/facebookresearch/omnilingual-asr) | Open speech recognition for 1,600+ languages, for audio in languages Whisper does not cover. | Open source | Local |  | 2025-12 |
| [pyannote.audio](https://github.com/pyannote/pyannote-audio) | Works out who spoke when in a recording (speaker diarisation), the basis for most open transcription tools. | Open source | Local | Models are gated: you must accept user conditions and create a Hugging Face token before first use. | 2026-11 |
| [Whisper](https://github.com/openai/whisper) | Transcribes and translates interviews, video and audio in about 100 languages on your own machine. | Open source | Local | Careless Whisper study found roughly 1% of transcriptions contained entirely hallucinated phrases; check quotes against the audio. | 2026-08 |
| [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | Runs Whisper on a laptop CPU or phone with no Python or GPU, for offline field transcription. | Open source | Local | Same Whisper models, so the same hallucination risk. | 2026-11 |
| [WhisperX](https://github.com/m-bain/whisperX) | Adds word-level timestamps and speaker labels to Whisper transcripts, useful for quoting and subtitling video evidence. | Open source | Local | README: numbers and symbols cannot be aligned to timings, overlapping speech is handled poorly, diarisation is far from perfect. | 2026-11 |

## Translation and languages

| Tool | What it is for | Type | Runs | Known limit | Last activity |
|---|---|---|---|---|---|
| [AI4Bharat IndicXlit](https://github.com/AI4Bharat/IndicXlit) | Transliterates names between Roman and 21 Indic scripts, useful for searching name spelling variants. | Open source | Local |  | 2023-10 (stale) |
| [Argos Translate](https://github.com/argosopentech/argos-translate) | Offline translation library and desktop app; install language packs and translate without any network connection. | Open source | Local |  | 2026-11 |
| [Bhashini](https://bhashini.gov.in/) | Government of India language platform offering translation and speech services across Indian languages. | Free web tool | Cloud | Cloud service run by a government; think before sending sensitive source material. |  |
| [DeepL](https://www.deepl.com/en/translator) | Commercial machine translation of text and documents in the browser. | Freemium | Cloud | Text is uploaded to DeepL's servers. |  |
| [Firefox Translations](https://github.com/mozilla/translations) | Translates web pages inside the browser on your device, so the page text never leaves your machine. | Open source | Local |  | 2026-10 |
| [IndicTrans2](https://github.com/AI4Bharat/IndicTrans2) | Translates between English and all 22 scheduled Indian languages with an open model you can run offline. | Open source | Local |  | 2025-10 (stale) |
| [LibreTranslate](https://github.com/LibreTranslate/LibreTranslate) | Self-hosted translation API and web interface that can run fully offline, a private alternative to cloud translators. | Open source | Both |  | 2026-11 |
| [MADLAD-400](https://huggingface.co/google/madlad400-3b-mt) | Apache-licensed translation model covering 400+ languages, usable where NLLB's non-commercial licence is a problem. | Open source | Local |  | 2023-11 (stale) |
| [NLLB-200](https://huggingface.co/facebook/nllb-200-distilled-600M) | Translates between 200 languages locally, including many low-resource ones commercial tools skip. | Open source | Local | Model card: research model, CC-BY-NC, not for legal or medical text, trained on inputs under 512 tokens. | (stale) |
| [OPUS-MT](https://github.com/Helsinki-NLP/Opus-MT) | Hundreds of small open translation models for specific language pairs, light enough for a laptop. | Open source | Local |  | 2026-02 |
| [SeamlessM4T](https://github.com/facebookresearch/seamless_communication) | Translates speech and text directly, including speech-to-text translation for foreign-language video. | Open source | Local |  | 2026-09 |
| [TranslateGemma](https://huggingface.co/google/translategemma-4b-it) | Open-weights translation model from Google that also translates text inside images. | Open source | Local | Gated: you must accept Google's Gemma licence on Hugging Face before downloading. | 2026-01 |

## OCR and documents

| Tool | What it is for | Type | Runs | Known limit | Last activity |
|---|---|---|---|---|---|
| [Docling](https://github.com/docling-project/docling) | Parses PDFs, Office files and scans into structured text and tables ready for search or LLMs. | Open source | Local |  | 2026-11 |
| [docTR](https://github.com/mindee/doctr) | Deep-learning OCR library for detecting and reading text in documents and photos. | Open source | Local |  | 2026-11 |
| [IndicPhotoOCR](https://github.com/Bhashini-IITJ/IndicPhotoOCR) | Reads text in photos (signboards, banners, posters) across 11 Indian languages, useful for geolocation clues. | Open source | Local |  | 2026-11 |
| [Kraken](https://github.com/mittagessen/kraken) | Trainable OCR engine for material standard OCR handles badly, such as historical print and less common scripts. | Open source | Local |  | 2026-11 |
| [Marker](https://github.com/datalab-to/marker) | Converts PDFs into clean Markdown or JSON, keeping tables and structure for analysis or LLM use. | Open source | Local | Model weights are free only for research, personal use and organisations under $5M funding/revenue. | 2026-11 |
| [MinerU](https://github.com/opendatalab/MinerU) | Turns complex PDFs and Office documents into Markdown or JSON for search or LLM pipelines. | Open source | Local |  | 2026-11 |
| [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) | Adds a searchable text layer to scanned PDFs in bulk, using Tesseract underneath. | Open source | Local |  | 2026-11 |
| [olmOCR](https://github.com/allenai/olmocr) | Uses a vision language model to linearise difficult PDFs with figures, multi-column layouts and insets. | Open source | Local | Needs a recent NVIDIA GPU with at least 12 GB memory; earlier versions hallucinated text on blank pages. | 2026-03 |
| [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | OCR and document parsing toolkit covering 100+ languages, turning PDFs and images into structured data. | Open source | Local |  | 2026-09 |
| [Surya](https://github.com/datalab-to/surya) | OCR, layout, reading order and table recognition in 90+ languages, strong on complex pages. | Open source | Local | Model weights are free only for research, personal use and organisations under $5M funding/revenue. | 2026-11 |
| [Tesseract](https://github.com/tesseract-ocr/tesseract) | Long-standing OCR engine for printed text in 100+ languages; the default for making scans searchable. | Open source | Local |  | 2026-11 |
| [Transkribus](https://www.transkribus.org/) | Reads handwriting and historical documents with 300+ community-trained models in 100+ languages. | Freemium | Cloud | Free tier is 50 credits a month; documents are uploaded to the service. |  |

## Searching big document sets

| Tool | What it is for | Type | Runs | Known limit | Last activity |
|---|---|---|---|---|---|
| [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) | Desktop app to chat with a folder of documents using local models, so files stay on your computer. | Open source | Local |  | 2026-11 |
| [Datashare](https://github.com/ICIJ/datashare) | Self-hosted search engine for large document sets, built by ICIJ for leak investigations; runs on your own machine. | Open source | Local |  | 2026-11 |
| [DocumentCloud](https://github.com/MuckRock/documentcloud) | Platform for uploading, annotating and publishing source documents, run by MuckRock. | Open source | Cloud | Hosted service. The website blocked automated checking (HTTP 403), so the repo was checked instead. | 2026-11 |
| [Google Pinpoint](https://journaliststudio.google.com/pinpoint/about/) | Google's research tool for journalists to explore and search large collections of documents with AI. | Free web tool | Cloud | Files sit on Google's servers; generative AI features need an early-access application. |  |
| [Kotaemon](https://github.com/Cinnamon/kotaemon) | Open-source interface for chatting with your own documents using local or hosted models. | Open source | Local |  | 2026-05 |
| [NotebookLM (now Gemini Notebook)](https://notebooklm.google.com/) | Ask questions across your uploaded sources and get answers that cite the passages used. | Freemium | Cloud | Sources are uploaded to Google's cloud. The old NotebookLM address now redirects to Gemini Notebook. |  |
| [OCCRP Aleph](https://aleph.occrp.org/) | OCCRP's hosted archive of leaks, company records and sanctions data, searchable by name. | Restricted | Cloud | OCCRP now develops Aleph Pro, which is not released as open source; the old open code is unmaintained. |  |
| [Ollama](https://github.com/ollama/ollama) | Runs open language models on your own computer; the engine behind most local document tools. | Open source | Local |  | 2026-11 |
| [Open Notebook](https://github.com/lfnovo/open-notebook) | Self-hosted alternative to NotebookLM that works with local or chosen model providers. | Open source | Local |  | 2026-11 |
| [Open WebUI](https://github.com/open-webui/open-webui) | Self-hosted chat interface for local models with built-in document search (RAG). | Open source | Local |  | 2026-11 |
| [OpenAleph](https://github.com/openaleph/openaleph) | Open-source fork of Aleph for storing, searching and cross-referencing large document and entity datasets. | Open source | Both | Needs server administration skills to self-host. | 2026-11 |
| [PrivateGPT](https://github.com/zylon-ai/private-gpt) | Question-answering over your own documents with local models and no data leaving your environment. | Open source | Local |  | 2026-11 |

## Image and video verification

| Tool | What it is for | Type | Runs | Known limit | Last activity |
|---|---|---|---|---|---|
| [Bellingcat Auto Archiver](https://github.com/bellingcat/auto-archiver) | Archives social media posts, videos and pages in bulk from a spreadsheet of links. | Open source | Local | Not an AI tool; listed because archiving comes before any AI analysis. | 2026-11 |
| [c2patool](https://github.com/contentauth/c2patool) | Command-line reader for C2PA manifests, so provenance checks can run offline. | Open source | Local | Absence of a manifest proves nothing about authenticity. | 2026-11 |
| [Content Credentials Verify](https://verify.contentauthenticity.org/) | Checks an image or video for C2PA Content Credentials and shows its signed edit history. | Free web tool | Cloud | Most files carry no credentials, and platforms often strip them; absence proves nothing. |  |
| [DeepFake-o-Meter](https://zinc.cse.buffalo.edu/ubmdfl/deep-o-meter/landing_page) | Runs a file through many open academic deepfake detectors at once and shows each score. | Free web tool | Cloud | Deepfake-Eval-2024: open-source detectors lost about 45-50% AUC on real 2024 deepfakes compared with lab benchmarks. |  |
| [Deepfakes Analysis Unit (India)](https://dau.trustedinfoalliance.in/) | WhatsApp tipline where the public and fact-checkers in India send suspected deepfakes for expert assessment. | Free web tool | Cloud | Human assessment through a tipline, not an instant automated verdict. |  |
| [ElevenLabs AI Speech Classifier](https://elevenlabs.io/ai-speech-classifier) | Estimates whether an audio clip was generated with ElevenLabs' own voice tools. | Free web tool | Cloud | Only covers ElevenLabs audio, and the page says it does not reliably classify Eleven v3 output. |  |
| [Google Fact Check Explorer](https://toolbox.google.com/factcheck/explorer) | Searches published fact-checks by claim to see whether something has already been debunked. | Free web tool | Cloud |  |  |
| [Google Lens](https://lens.google/) | Reverse image search with visual matching; often the fastest first step in locating or sourcing a picture. | Free web tool | Cloud | Bellingcat's 2025 test: Lens beat most LLMs at geolocation but lost narrowly to three ChatGPT models. |  |
| [Hive AI-generated content detection](https://hivemoderation.com/ai-generated-content-detection) | Commercial classifier with a free demo that scores images, video and audio as AI-generated or not. | Freemium | Cloud | Deepfake-Eval-2024: commercial detectors beat open models but do not reach the accuracy of human forensic analysts. |  |
| [ImageWhisperer](https://imagewhisperer.org/) | Image checker for journalists combining AI detection, C2PA, reverse search and fact-check lookups in one report. | Freemium | Cloud | Two free checks a day; images are uploaded to the service. |  |
| [InVID-WeVerify verification plugin](https://weverify.eu/verification-plugin/) | Browser toolkit for verification: keyframes, reverse image search, forensic filters, OCR and synthetic-image checks. | Free web tool | Both | 2026 arXiv study: forensic tools including InVID show high recall but poor specificity; humans outperformed all tools. | 2026-11 |
| [Reality Defender](https://www.realitydefender.com/) | Enterprise deepfake detection for audio, video and images. | Paid | Cloud | Deepfake-Eval-2024: commercial detectors beat open models but do not reach the accuracy of human forensic analysts. |  |
| [SynthID Detector](https://synthid.com/) | Checks images, video and audio for Google's invisible SynthID watermark. | Free web tool | Cloud | Only finds SynthID watermarks; content from models without it shows nothing. A negative result is not proof of authenticity. |  |
| [TrueMedia (Georgetown)](https://www.truemedia.org/) | Deepfake detection platform revived at Georgetown University after the original non-profit closed. | Restricted | Cloud | Access is by beta request. The original open-sourced models (truemediaorg on GitHub) are unmaintained since early 2025. |  |
| [Deepfake-Eval-2024 (benchmark)](https://arxiv.org/abs/2503.02857) | Benchmark of real deepfakes from social media in 2024, testing how detectors perform outside the lab. | Reading | | Finding: detector AUC fell 50% (video), 48% (audio), 45% (image) against earlier academic benchmarks. | 2025-03 |
| [How Effective Are Publicly Accessible Deepfake Detection Tools?](https://arxiv.org/abs/2603.04456) | 2026 study comparing six free forensic and AI image-detection tools against professional investigators. | Reading | | Finding: forensic tools over-flag, AI classifiers under-flag, and human evaluators substantially outperformed every tool. | 2026-03 |

## Geolocation and chronolocation aids

| Tool | What it is for | Type | Runs | Known limit | Last activity |
|---|---|---|---|---|---|
| [Bellingcat OpenStreetMap Search](https://osm-search.bellingcat.com/) | Finds places where chosen features (e.g. a mosque near a bridge) appear close together in OpenStreetMap. | Free web tool | Cloud | Not AI; only as complete as OpenStreetMap is for that area. |  |
| [GeoCLIP](https://github.com/VicenteVivan/geo-clip) | Open model that predicts GPS coordinates from a single image, run locally. | Open source | Local | No independent newsroom test found; treat the predicted coordinates as a lead to verify. | 2026-10 |
| [Picarta](https://picarta.ai/) | Upload a photo and get predicted coordinates with confidence scores from an AI model. | Freemium | Cloud | Site says accuracy depends on how distinctive the scene is; no independent test found. Photos are uploaded. |  |
| [PIGEON](https://github.com/LukasHaas/PIGEON) | Research code for a CVPR 2024 model trained on street-view data to predict where an image was taken. | Open source | Local | Research code with no commits since July 2024; its README links NPR coverage of the privacy concerns. | 2024-07 (stale) |
| [ShadowFinder](https://github.com/bellingcat/ShadowFinder) | Uses an object's height, shadow length and time to map everywhere on Earth the photo could have been taken. | Open source | Local | Needs a reliable time and measurable shadow on flat ground; gives a band of possible locations, not a point. | 2026-09 |
| [StreetCLIP](https://huggingface.co/geolocal/StreetCLIP) | Open CLIP model tuned on street-level imagery to guess country, region or city of a photo. | Open source | Local | CC-BY-NC licence, so non-commercial use only; no independent newsroom test found. | (stale) |
| [SunCalc](https://www.suncalc.org/) | Shows sun direction and shadow length for any place and time, the standard chronolocation check. | Free web tool | Cloud | Not AI; shows sun position only, you still need to measure the shadow yourself. |  |
| [Can AI Chatbots Be Used for Geolocation? (Bellingcat, 2023)](https://www.bellingcat.com/resources/2023/07/14/can-ai-chatbots-be-used-for-geolocation/) | The 2023 baseline test of Bing AI and Bard, useful for seeing how fast this changed. | Reading | | Both chatbots struggled and were highly prone to hallucination. | 2023-07 |
| [Doxing via the Lens (paper)](https://arxiv.org/abs/2504.19373) | Paper showing reasoning models can infer a home address or neighbourhood from ordinary user photos, including selfies. | Reading | | A privacy warning as much as a capability: the same technique exposes private people. | 2025-04 |
| [Have LLMs Finally Mastered Geolocation? (Bellingcat)](https://www.bellingcat.com/resources/how-tos/2025/06/06/have-llms-finally-mastered-geolocation/) | Bellingcat's 500-run test of 20 LLMs on 25 unpublished photos, with Google Lens as the baseline. | Reading | | Only ChatGPT o3, o4-mini and o4-mini-high beat Google Lens, narrowly; Claude and Mistral lagged well behind. | 2025-06 |
| [Updated Test of 24 LLMs for Geolocation (Bellingcat via GIJN)](https://gijn.org/stories/updated-test-24-llms-ai-geolocation/) | Re-run two months later adding GPT-5, Grok 4 and Google AI Mode. | Reading | | Google AI Mode scored best, but most models hallucinated at some point and even the best confidently named wrong places. | 2025-09 |

## Satellite and geospatial ML

| Tool | What it is for | Type | Runs | Known limit | Last activity |
|---|---|---|---|---|---|
| [AlphaEarth Foundations](https://deepmind.google/discover/blog/alphaearth-foundations-helps-map-our-planet-in-unprecedented-detail/) | Google's annual satellite embedding dataset in Earth Engine, for similarity search and change mapping without training. | Free web tool | Cloud | Released as annual embeddings at 10 m squares, so it cannot date a specific event within a year. | 2025-07 |
| [Clay](https://github.com/Clay-foundation/model) | Open foundation model producing embeddings of satellite imagery, for similarity search and change detection. | Open source | Local |  | 2026-03 |
| [Dynamic World](https://dynamicworld.app/) | Near-real-time 10 m global land cover from Sentinel-2, made with deep learning. | Free web tool | Cloud |  |  |
| [Earth Index](https://earthindex.ai/) | Search satellite imagery by example: mark a mine or feedlot and find similar sites across a region. | Free web tool | Cloud | Needs an account; results are look-alike candidates to confirm with high-resolution imagery. |  |
| [Geo-SAM (QGIS plugin)](https://github.com/coolzhao/Geo-SAM) | Point-and-click Segment Anything inside QGIS for tracing features in imagery. | Open source | Local |  | 2026-07 |
| [GeoAI](https://github.com/opengeos/geoai) | Python package bundling detection, segmentation and change detection for satellite and aerial imagery. | Open source | Local |  | 2026-11 |
| [Global Fishing Watch map](https://globalfishingwatch.org/map) | Maps fishing activity and vessels worldwide using ML on AIS and satellite radar detections. | Free web tool | Cloud |  |  |
| [Google Earth Engine](https://earthengine.google.com/) | Cloud platform with decades of satellite archives and built-in classifiers for land-change analysis. | Freemium | Cloud | Free for academic and research use; commercial use is paid. |  |
| [OlmoEarth](https://olmoearth.allenai.org/) | Open Earth-observation foundation models and a platform from Allen AI for environmental monitoring. | Open source | Both |  | 2026-11 |
| [Open-CD](https://github.com/likyoo/open-cd) | Toolbox of change-detection models for comparing before and after satellite images. | Open source | Local |  | 2026-06 |
| [Prithvi (IBM-NASA)](https://huggingface.co/ibm-nasa-geospatial) | Open Earth-observation foundation models from NASA and IBM for flood, fire-scar and land-use mapping. | Open source | Local |  |  |
| [segment-geospatial (SamGeo)](https://github.com/opengeos/segment-geospatial) | Segments buildings, fields, water or damage in satellite imagery with Segment Anything, from a notebook. | Open source | Local |  | 2026-11 |
| [SkyTruth Cerulean](https://cerulean.skytruth.org/) | Detects oil slicks in Sentinel-1 radar with ML and links them to likely source vessels. | Free web tool | Cloud | Detections come with confidence scores; treat a slick or source match as a lead. |  |
| [TerraTorch](https://github.com/torchgeo/terratorch) | Toolkit for fine-tuning geospatial foundation models such as Prithvi for floods, burn scars or crops. | Open source | Local |  | 2026-11 |
| [TESSERA](https://github.com/ucam-eo/tessera) | Cambridge foundation model giving per-pixel embeddings from Sentinel-1/2 time series for land classification. | Open source | Local |  | 2026-11 |
| [TorchGeo](https://github.com/torchgeo/torchgeo) | PyTorch library of geospatial datasets, samplers and pretrained models for training on satellite data. | Open source | Local | A developer library; needs ML experience. | 2026-11 |

## Entities, networks and text analysis

| Tool | What it is for | Type | Runs | Known limit | Last activity |
|---|---|---|---|---|---|
| [AI4Bharat IndicNER](https://huggingface.co/ai4bharat/IndicNER) | Named-entity recognition for 11 Indian languages. | Open source | Local | Gated on Hugging Face: you must log in and share contact details to download. | (stale) |
| [BERTopic](https://github.com/MaartenGr/BERTopic) | Groups thousands of posts or documents into readable topics using embeddings. | Open source | Local |  | 2026-11 |
| [FollowTheMoney](https://github.com/opensanctions/followthemoney) | Shared data model for people, companies, assets and relationships used by OpenSanctions and OpenAleph. | Open source | Local |  | 2026-11 |
| [Gephi](https://github.com/gephi/gephi) | Desktop network analysis and visualisation for mapping accounts, companies or citations. | Open source | Local |  | 2026-11 |
| [GLiNER](https://github.com/urchade/GLiNER) | Extracts any entity type you name (e.g. vessel, shell company) without training a model. | Open source | Local |  | 2026-11 |
| [GraphRAG](https://github.com/microsoft/graphrag) | Builds a knowledge graph from documents with an LLM, then answers questions across the whole set. | Open source | Both |  | 2026-11 |
| [LangExtract](https://github.com/google/langextract) | Uses an LLM to extract structured facts from long text and links each one to its source span. | Open source | Both | README: accuracy of inferred information depends on the chosen LLM and prompt; check highlighted spans. | 2026-11 |
| [nomenklatura](https://github.com/opensanctions/nomenklatura) | Entity resolution and deduplication toolkit for FollowTheMoney data, with a human review loop. | Open source | Local |  | 2026-11 |
| [OpenRefine](https://github.com/OpenRefine/OpenRefine) | Cleans messy spreadsheets, clusters name variants and reconciles them against external databases. | Open source | Local |  | 2026-11 |
| [OpenSanctions and yente](https://github.com/opensanctions/yente) | Open database of sanctions and politically exposed persons, with a self-hosted matching API. | Open source | Both | Commercial use needs a paid data licence; a name match is a lead, not an identification. | 2026-11 |
| [spaCy](https://github.com/explosion/spaCy) | Fast NLP library for pulling names, organisations and places out of large text collections. | Open source | Local |  | 2026-10 |
| [Splink](https://github.com/moj-analytical-services/splink) | Probabilistic record linkage: matches people or companies across datasets without shared IDs. | Open source | Local |  | 2026-11 |
| [Stanza](https://github.com/stanfordnlp/stanza) | Stanford NLP toolkit for tokenising, parsing and NER in many languages. | Open source | Local |  | 2026-11 |

## MCP servers for OSINT

| Tool | What it is for | Type | Runs | Known limit | Last activity |
|---|---|---|---|---|---|
| [data.gov.in MCP server](https://github.com/the-data-gateway-initiative/datagovin-mcp-server) | Exposes India's open government data portal APIs to agents. 2 stars. | Open source | Local | Needs a data.gov.in API key; no commits since November 2025. | 2025-11 (stale) |
| [gdelt-mcp-server](https://github.com/cyanheads/gdelt-mcp-server) | Searches GDELT global news coverage and US TV transcripts from an agent; no API key. 10 stars. | Open source | Local |  | 2026-11 |
| [mcp-india-tenders](https://github.com/switchr24/mcp-india-tenders) | Searches Indian government tenders from CPPP, eProc Rajasthan and defence portals. 2 stars. | Open source | Local | Tiny project with no commits since December 2025. | 2025-12 |
| [mcp-shodan](https://github.com/w0h1v/mcp-shodan) | MCP server for Shodan host search, DNS and CVE lookups. 191 stars. | Open source | Local | Needs your own Shodan API key. | 2026-11 |
| [mcp-wayback-machine](https://github.com/Mearman/mcp-wayback-machine) | MCP server and CLI to check, fetch and save Wayback Machine snapshots. 66 stars. | Open source | Local |  | 2026-10 |
| [MoSPI eSankhyiki MCP (India)](https://github.com/nso-india/esankhyiki-mcp) | Official Indian statistics ministry MCP server for economic, demographic and social indicators. 148 stars. | Open source | Both | Statistics only; no company, court, land or tender records. | 2026-11 |
| [OpenOSINT](https://github.com/OpenOSINT/OpenOSINT) | Agent and MCP server with 21 public-source tools (DNS, RDAP, WHOIS, GDELT, dorks). 1,939 stars. | Open source | Both | Passive tools work keyless; Shodan, Censys, VirusTotal and breach checks need keys. Infrastructure focus. | 2026-11 |
| [OpenRegistry](https://github.com/sophymarine/openregistry) | Hosted MCP for live company records from 27 official national registries. 23 stars. | Freemium | Cloud | Hosted service with sign-in; its README does not mention India. | 2026-10 |
| [osint-mcp-server (badchars)](https://github.com/badchars/osint-mcp-server) | 37 tools over 12 sources: DNS, WHOIS, crt.sh, BGP, Wayback, plus Shodan and VirusTotal. 62 stars. | Open source | Local | 21 tools work without keys; the other 16 need paid or registered API keys. | 2026-03 |
| [osmmcp](https://github.com/NERVsystems/osmmcp) | OpenStreetMap MCP server: geocoding, nearby places and routing for an agent. 32 stars. | Open source | Local |  | 2026-10 |
| [Sanctions Screening MCP](https://github.com/cyanheads/sanctions-screening-mcp-server) | Screens names against OFAC, EU, UK and UN lists offline from a local mirror; no key. 4 stars. | Open source | Local | Fuzzy name matches are leads, not identifications. | 2026-11 |
| [Sift](https://github.com/mefos-lab/sift) | MCP server and skills cross-referencing OpenSanctions, ICIJ Offshore Leaks, Companies House, SEC EDGAR and CourtListener. 6 stars. | Open source | Local | Small project; US and UK sources dominate. | 2026-08 |
| [World Intel MCP](https://github.com/marc-shade/world-intel-mcp) | 160 tools over free public APIs: conflict events, aircraft, maritime warnings, sanctions, markets. 1,079 stars. | Open source | Local | Some tools need API keys; README flags which. | 2026-10 |
| [Awesome OSINT MCP Servers](https://github.com/soxoj/awesome-osint-mcp-servers) | Curated directory of about 115 OSINT MCP servers by category. 548 stars. | Reading | | Includes people-search and breach-data servers; listings are not vetted for accuracy or ethics. | 2026-11 |

## Agent skills, prompts and agent frameworks for investigations

| Tool | What it is for | Type | Runs | Known limit | Last activity |
|---|---|---|---|---|---|
| [agentic-newsroom](https://github.com/emmapbingham/agentic-newsroom) | Data-journalism skills that load raw records into SQLite, screen for leads and track findings. 1 star. | Open source | Local | A contest entry built around US lobbying data, not a general tool. | 2026-10 |
| [Anthropic Agent Skills](https://github.com/anthropics/skills) | Official examples and specification for SKILL.md packs, the starting point for writing your own. | Open source | Local | Not OSINT-specific. | 2026-11 |
| [bullshit-detector](https://github.com/SerhiiKorniienko/bullshit-detector) | Agent skills that break a video, article or post into claims and check each against sources. 163 stars. | Open source | Local | Verdicts come from an LLM's web search; Full Fact logged dozens of chatbot fact-check errors in 2026. | 2026-09 |
| [claude-skills-journalism](https://github.com/jamditis/claude-skills-journalism) | Skill packs for newsrooms: source verification, C2PA, web archiving, FOIA requests, data journalism. 453 stars. | Open source | Local | Public-records skills are US-centric (FOIA, New Jersey OPRA) plus Brazil's LAI. | 2026-11 |
| [geo-sleuth](https://github.com/Oldcircle/geo-sleuth) | Agent skill that geolocates a photo using OpenStreetMap geometry, skylines, satellite imagery and street view. 7,088 stars. | Open source | Local | README admits no blind-test accuracy figure yet; published examples are regression checks on already-solved photos. | 2026-11 |
| [GPT Researcher](https://github.com/assafelovic/gpt-researcher) | Autonomous agent that searches the web and writes a cited research report on a question. | Open source | Both | Tow Center found AI search tools gave wrong answers to over 60% of news-citation queries; check every source. | 2026-11 |
| [Investigators Co-Pilot](https://github.com/assafkip/investigators-copilot) | Claude Code plugin for case management with evidence capture, A-F source grading and 54 lookup adapters. 76 stars. | Open source | Local | Needs a paid Claude plan; some adapters need outside paid keys. Includes username and email lookups. | 2026-11 |
| [Newsroom extension](https://github.com/ehurrn/newsroom-extension) | 18 skills for Claude and Gemini CLI covering FOIA, corporate research, evidence preservation and libel review. 8 stars. | Open source | Local | Includes subject-dossier skills; legal content is US-oriented and is not legal advice. | 2026-06 |
| [OSINT Forge Skills](https://github.com/OSINT-Forge-Community/osint-forge-skills) | 16 skills with offline Python helpers for evidence preservation, competing hypotheses and cited reports. 10 stars. | Open source | Local | Analyses files you supply; does not fetch archives or registries itself. French sources (BODACC) featured. | 2026-10 |
| [osint-investigation skill](https://github.com/reichaves/osint-investigation) | Berkeley Protocol-aligned skill for geolocation, photo verification and account checks that outputs a lead sheet. 7 stars. | Open source | Local | Methodology only, no bundled tools; public-records references cover Brazil. | 2026-05 |
| [STORM](https://github.com/stanford-oval/storm) | Stanford system that researches a topic and drafts a long, cited background article. | Open source | Both | No commits since September 2025. | 2025-09 (stale) |
| [Taranis AI](https://github.com/taranis-ai/taranis-ai) | Self-hosted OSINT monitoring: collects news sources, then uses NLP to cluster, summarise and tag items. | Open source | Local |  | 2026-11 |
| [Journalist's Toolbox AI](https://journaliststoolbox.ai/) | Regularly updated directory of AI tools, prompts and guides for reporters. | Reading | | A directory, not a tested evaluation. |  |

## Guidance, ethics and tested evaluations

| Reading | What it covers | Publisher | Key point | Date |
|---|---|---|---|---|
| [AI Search Has a Citation Problem (Tow Center)](https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php) | Test of eight AI search tools asked to identify the source article of news quotes. | Tow Center for Digital Journalism / CJR | Over 60% of answers were wrong; Perplexity erred 37% of the time, Grok 3 94%. | 2025-03 |
| [AP standards around generative AI](https://www.ap.org/the-definitive-source/behind-the-news/standards-around-generative-ai/) | The Associated Press's published rules on how its journalists may and may not use generative AI. | Associated Press |  |  |
| [BBC guidance: the use of artificial intelligence](https://www.bbc.co.uk/editorialguidelines/guidance/use-of-artificial-intelligence) | BBC editorial guidance on AI use, transparency and human oversight. | BBC |  |  |
| [Careless Whisper: Speech-to-Text Hallucination Harms](https://arxiv.org/abs/2402.08021) | Study measuring how often Whisper invents text that was never spoken. | Koenecke et al. | About 1% of transcriptions had hallucinated phrases; 38% of those included explicit harms. | 2024-05 |
| [Full Fact: AI chatbots and misinformation trial](https://fullfact.org/technology/full-fact-analysis--ai-chatbots-misinformation/) | UK fact-checker's 2026 log of what major chatbots said about false claims it was checking. | Full Fact | 39 major errors and 67 incorrect responses in five months, including calling AI-generated images real. | 2026-09 |
| [How newsrooms are using AI in investigations (Nieman Lab, Oct 2026)](https://www.niemanlab.org/2026/10/uber-agents-undercover-ai-personas-and-other-ways-newsrooms-are-using-ai-in-investigations/) | Round-up of how investigative teams actually use agents and LLMs, with their stated limits. | Nieman Lab | Quoted finding: AI is good at generating leads, much less capable of establishing publishable evidence. | 2026-10 |
| [News Integrity in AI Assistants (EBU / BBC)](https://www.ebu.ch/research/open/report/news-integrity-in-ai-assistants) | Study by 22 public broadcasters in 14 languages on how AI assistants answer news questions. | European Broadcasting Union and BBC | Reported 45% of answers had at least one significant issue (figure from EBU press coverage). | 2025-10 |
| [PAI Responsible Practices for Synthetic Media](https://syntheticmedia.partnershiponai.org/) | Framework on disclosure and labelling of synthetic media, with case studies from signatories. | Partnership on AI |  |  |
| [Paris Charter on AI and Journalism](https://rsf.org/en/rsf-and-16-partners-unveil-paris-charter-ai-and-journalism) | Ten principles on AI in journalism drafted by RSF and 16 partner organisations. | Reporters Without Borders (RSF) |  | 2023-11 |
| [Poynter AI ethics starter kit (2025 update)](https://www.poynter.org/ethics-trust/2025/a-lot-has-changed-since-we-created-ai-ethics-guidelines-for-newsrooms-heres-what-you-need-to-know-now/) | Template newsroom AI policy, updated with sections on visual journalism and AI products. | Poynter Institute |  | 2025-06 |
| [Reporter's Guide to Detecting AI-Generated Content (GIJN)](https://gijn.org/resource/guide-detecting-ai-generated-content/) | GIJN's practical guide to spotting AI-made images, video and audio by inspection and tools. | Global Investigative Journalism Network | Visual tells go out of date quickly as generators improve. |  |
| [Spotting the deepfakes in this year of elections (Reuters Institute / WITNESS)](https://reutersinstitute.politics.ox.ac.uk/news/spotting-deepfakes-year-elections-how-ai-detection-tools-work-and-where-they-fail) | WITNESS researchers tested public AI detectors and explain where they break. | Reuters Institute; shirin anlen and Raquel Vázquez Llorente | Lowering resolution or cropping a known deepfake flipped a detector's verdict to 'not a deepfake'. | 2024-04 |
| [TRIED Benchmark (WITNESS)](https://arxiv.org/abs/2504.21489) | Framework for judging AI detection tools on real-world usefulness, built from WITNESS casework. | WITNESS | A framework, not a league table of tools. | 2025-04 |
| [What Journalists Should Know About Deepfake Detection in 2025 (Tow Center)](https://www.cjr.org/tow_center/what-journalists-should-know-about-deepfake-detection-technology-in-2025-a-non-technical-guide.php) | Plain-language guide to how detectors work and why they fail on real-world media. | Tow Center for Digital Journalism / CJR | Cites an experiment where journalists over-relied on detector output when it matched their instinct. | 2025-03 |
| [Why AI Models Are Bad at Verifying Photos (Tow Center)](https://www.cjr.org/tow_center/why-ai-models-are-bad-at-verifying-photos.php) | Test of seven chatbots asked to identify the location, date and photographer of ten news photos. | Tow Center for Digital Journalism / CJR | Only 14 of 280 answers got location, date and source right. | 2025-08 |

## Tools that have closed or changed

See [research/NOTES.md](research/NOTES.md) for tools that shut down or became restricted (for example GeoSpy, the original TrueMedia.org and the open-source version of OCCRP Aleph), with a source for each.

## Contributing

Corrections are as welcome as additions: a tool that died, changed its pricing, or has a newly published test of its accuracy.

To add a tool, add an object to `research/entries.json` and run `python3 build_readme.py`. Fields: `category`, `name`, `url`, `what` (one sentence), `type`, `runs` (local, cloud or both), `maintainer`, `status` (active or stale), `last_activity` (YYYY-MM), `checked` (the day you opened the link) and `limit` (a documented limitation with its source, or an empty string). Please do not invent a limit, and keep to the scope above.

## Related

- [india-osint](https://github.com/Ghongha007/india-osint): public records and open data for investigating stories in India
- [chat2net](https://github.com/Ghongha007/chat2net): turn a chat or social-media export into a Gephi network
- [osint-skills](https://github.com/Ghongha007/osint-skills): agent skills for verification, geolocation, chronolocation and fact-checking
- [verify-mcp](https://github.com/Ghongha007/verify-mcp): an MCP server with keyless, read-only verification lookups
- [osint-visuals](https://github.com/Ghongha007/osint-visuals): agent skills for evidence graphics: ship and flight tracks, shadow diagrams, 3D scenes, satellite before/after and scroll stories

## Licence

The list is released under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The script is MIT. Compiled by [OSINT JOURNO](https://github.com/OSINT-JOURNO).
