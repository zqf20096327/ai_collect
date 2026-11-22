<p align="center">
  <img src="assets/banner.svg" alt="Automate Workflow n8n-projects banner" width="100%" />
</p>

<p align="center">
  <img src="assets/logo.svg" alt="n8n-projects logo" width="72" height="72" />
</p>

<h1 align="center">n8n-projects</h1>

<p align="center">
  Curated n8n projects to learn production automation across messaging, HR, text classification, voice, vision, video, and research workflows.
</p>

<!-- BADGES:START -->
<p align="center">
  <a href="LICENSE"><img src="assets/badges/license-mit.svg" alt="License: MIT" height="20" /></a>
  <a href="https://github.com/Automate-Workflow/n8n-projects/actions/workflows/validate.yml"><img src="https://github.com/Automate-Workflow/n8n-projects/actions/workflows/validate.yml/badge.svg" alt="Validate workflow status" height="20" /></a>
  <a href="https://github.com/Automate-Workflow/n8n-projects/actions/workflows/links.yml"><img src="https://github.com/Automate-Workflow/n8n-projects/actions/workflows/links.yml/badge.svg" alt="Link check workflow status" height="20" /></a>
  <a href="data/n8n_list.csv"><img src="assets/badges/projects-count.svg" alt="Projects: 50" height="20" /></a>
  <a href="data/n8n_list.csv"><img src="assets/badges/last-updated.svg" alt="Last verified: 2026-11-11" height="20" /></a>
</p>
<!-- BADGES:END -->

<p align="center">
  <img src="assets/divider.svg" alt="Section divider" width="100%" height="24" />
</p>

## Why This Directory Exists

Learning n8n effectively requires inspecting real, end-to-end workflows rather than isolated single-node demos. This repository organizes publicly accessible n8n workflows and integration repositories from [data/n8n_list.csv](data/n8n_list.csv) into clear categories and a four-phase learning progression. It is built for automation engineers, developers, technical operations teams, and students who want structured examples covering triggers, credentials, LLM routing, RAG, multimodal pipelines, and production safeguards.

## Table of Contents

- [Why This Directory Exists](#why-this-directory-exists)
- [Category Overview](#category-overview)
- [Learning Path Summary](#learning-path-summary)
- [Full Project Directory](#full-project-directory)
- [How to Use a Project](#how-to-use-a-project)
- [Quality and Trust Notes](#quality-and-trust-notes)
- [Community and Governance](#community-and-governance)
- [License and Acknowledgements](#license-and-acknowledgements)

<p align="center">
  <img src="assets/divider.svg" alt="Section divider" width="100%" height="24" />
</p>

## Category Overview

Each category links to a dedicated guide in [docs/categories/](docs/categories/) covering prerequisites, suggested order, and domain-specific risks (such as messaging API rules, scraping terms, PII handling, and API cost controls).

<!-- CATEGORIES:START -->
| Icon | Category | Projects | Difficulty Breakdown | Directory Section |
| --- | --- | --- | --- | --- |
| <img src="assets/icons/whatsapp.svg" alt="WhatsApp icon" width="28" height="28" /> | [WhatsApp](docs/categories/whatsapp.md) | 6 | 3 Intermediate, 3 Advanced | [Jump to WhatsApp](#category-whatsapp) |
| <img src="assets/icons/linkedin.svg" alt="LinkedIn icon" width="28" height="28" /> | [LinkedIn](docs/categories/linkedin.md) | 4 | 1 Intermediate, 3 Advanced | [Jump to LinkedIn](#category-linkedin) |
| <img src="assets/icons/resume-hr.svg" alt="Resume/HR icon" width="28" height="28" /> | [Resume/HR](docs/categories/resume-hr.md) | 6 | 2 Beginner, 3 Intermediate, 1 Advanced | [Jump to Resume/HR](#category-resume-hr) |
| <img src="assets/icons/text-classification.svg" alt="Text/Classification icon" width="28" height="28" /> | [Text/Classification](docs/categories/text-classification.md) | 10 | 7 Beginner, 2 Intermediate, 1 Advanced | [Jump to Text/Classification](#category-text-classification) |
| <img src="assets/icons/voice.svg" alt="Voice icon" width="28" height="28" /> | [Voice](docs/categories/voice.md) | 5 | 1 Beginner, 3 Intermediate, 1 Advanced | [Jump to Voice](#category-voice) |
| <img src="assets/icons/image.svg" alt="Image icon" width="28" height="28" /> | [Image](docs/categories/image.md) | 4 | 3 Beginner, 1 Intermediate | [Jump to Image](#category-image) |
| <img src="assets/icons/computer-vision.svg" alt="Computer Vision icon" width="28" height="28" /> | [Computer Vision](docs/categories/computer-vision.md) | 4 | 3 Intermediate, 1 Advanced | [Jump to Computer Vision](#category-computer-vision) |
| <img src="assets/icons/video.svg" alt="Video icon" width="28" height="28" /> | [Video](docs/categories/video.md) | 5 | 1 Beginner, 1 Intermediate, 3 Advanced | [Jump to Video](#category-video) |
| <img src="assets/icons/paper.svg" alt="Paper icon" width="28" height="28" /> | [Paper](docs/categories/paper.md) | 6 | 1 Beginner, 4 Intermediate, 1 Advanced | [Jump to Paper](#category-paper) |
<!-- CATEGORIES:END -->

<p align="center">
  <img src="assets/divider.svg" alt="Section divider" width="100%" height="24" />
</p>

## Learning Path Summary

Follow the four phases below in order, or open the detailed curriculum in [docs/learning-path.md](docs/learning-path.md).

<!-- LEARNING_PATH:START -->
<p><img src="assets/badges/phase-1.svg" alt="Phase 1 - Foundations" height="20" /></p>

### [Phase 1 - Foundations](docs/learning-path.md#phase-1---foundations)

Start with single-trigger workflows connecting email, chat, spreadsheets, and storage with an LLM node to learn credentials, prompts, and structured routing.

**Included projects (12):** [#17](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Gmail_and_Email_Automation/InboxZero%20Lite%20-%20AI%20Email%20Classifier.json), [#18](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Gmail_and_Email_Automation/Basic%20Automatic%20Gmail%20Email%20Labelling%20with%20OpenAI%20and%20Gmail%20API.json), [#19](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Gmail_and_Email_Automation/Auto%20Categorise%20Outlook%20Emails%20with%20AI.json), [#21](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Detect%20toxic%20language%20in%20Telegram%20messages.json), [#22](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Google_Drive_and_Google_Sheets/Qualify%20new%20leads%20in%20Google%20Sheets%20via%20OpenAI_s%20GPT-4.json), [#25](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Notion/Add%20positive%20feedback%20messages%20to%20a%20table%20in%20Notion.json), [#26](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Discord/Discord%20AI-powered%20bot.json), [#32](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Automated%20AI%20image%20analysis%20and%20response%20via%20Telegram.json), [#33](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Google_Drive_and_Google_Sheets/Automatic%20Background%20Removal%20for%20Images%20in%20Google%20Drive.json), [#34](https://github.com/enescingoz/awesome-n8n-templates/blob/main/AI%20product%20imagines.json), [#40](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Discord/Share%20YouTube%20Videos%20with%20AI%20Summaries%20on%20Discord.json), [#49](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Telegram%20chat%20with%20PDF.json)

<p><img src="assets/badges/phase-2.svg" alt="Phase 2 - Chatbots and Voice" height="20" /></p>

### [Phase 2 - Chatbots and Voice](docs/learning-path.md#phase-2---chatbots-and-voice)

Progress to stateful conversational assistants over Telegram and WhatsApp, adding speech-to-text transcription, local models, and vector retrieval.

**Included projects (10):** [#2](https://github.com/ZohaibCodez/n8n-whatsapp-ai-agent), [#3](https://github.com/lucaswalter/n8n-ai-automations), [#6](https://github.com/enescingoz/awesome-n8n-templates/tree/main/WhatsApp), [#20](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Gmail_and_Email_Automation/AI%20Email%20Auto-Responder%20with%20Ollama.json), [#27](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Translate%20Telegram%20audio%20messages%20with%20AI%20(55%20supported%20languages).json), [#28](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Angie,%20Personal%20AI%20Assistant%20with%20Telegram%20Voice%20and%20Text.json), [#29](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Telegram%20AI%20bot%20assistant_%20ready-made%20template%20for%20voice%20&%20text%20messages.json), [#30](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/%F0%9F%A4%96%20Telegram%20Messaging%20Agent%20for%20Text_Audio_Images.json), [#35](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Telegram%20AI%20Bot_%20NeurochainAI%20Text%20&%20Image%20-%20NeurochainAI%20Basic%20API%20Integration.json), [#48](https://github.com/enescingoz/awesome-n8n-templates/blob/main/PDF_and_Document_Processing/Chat%20with%20PDF%20docs%20using%20AI%20(quoting%20sources).json)

<p><img src="assets/badges/phase-3.svg" alt="Phase 3 - Documents, Vision and Data" height="20" /></p>

### [Phase 3 - Documents, Vision and Data](docs/learning-path.md#phase-3---documents-vision-and-data)

Build extraction pipelines for PDFs, resumes, forms, academic papers, and images using OCR, multimodal vision models, and structured output parsers.

**Included projects (14):** [#11](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/ResumeBot.json), [#12](https://github.com/enescingoz/awesome-n8n-templates/blob/main/PDF_and_Document_Processing/CV%20Resume%20PDF%20Parsing%20with%20Multimodal%20Vision%20AI.json), [#13](https://github.com/enescingoz/awesome-n8n-templates/blob/main/PDF_and_Document_Processing/Extract%20data%20from%20resume%20and%20create%20PDF%20with%20Gotenberg.json), [#14](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Airtable/Handling%20Job%20Application%20Submissions%20with%20AI%20and%20n8n%20Forms.json), [#15](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Google_Drive_and_Google_Sheets/Screen%20Applicants%20With%20AI,%20notify%20HR%20and%20save%20them%20in%20a%20Google%20Sheet.json), [#16](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Internship%20Informer.json), [#23](https://github.com/CodingAbdullah/n8n-workflows), [#36](https://github.com/enescingoz/awesome-n8n-templates/blob/main/PDF_and_Document_Processing/Extract%20license%20plate%20number%20from%20image%20uploaded%20via%20an%20n8n%20form.json), [#37](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Gmail_and_Email_Automation/Analyze%20Suspicious%20Email%20Contents%20with%20ChatGPT%20Vision.json), [#38](https://github.com/enescingoz/awesome-n8n-templates/blob/main/PDF_and_Document_Processing/Extract%20text%20from%20PDF%20and%20image%20using%20Vertex%20AI%20(Gemini)%20into%20CSV.json), [#41](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Google_Drive_and_Google_Sheets/Upload%20to%20Instagram%20and%20Tiktok%20from%20Google%20Drive.json), [#45](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Notion/Analyse%20papers%20from%20Hugging%20Face%20with%20AI%20and%20store%20them%20in%20Notion.json), [#47](https://n8n.io/workflows/2904-arxiv-paper-summarization-with-chatgpt/), [#50](https://github.com/enescingoz/awesome-n8n-templates/blob/main/PDF_and_Document_Processing/Invoice%20data%20extraction%20with%20LlamaParse%20and%20OpenAI.json)

<p><img src="assets/badges/phase-4.svg" alt="Phase 4 - Advanced Agents and Integrations" height="20" /></p>

### [Phase 4 - Advanced Agents and Integrations](docs/learning-path.md#phase-4---advanced-agents-and-integrations)

Combine multi-agent tool calling, self-hosted APIs, MCP servers, and multi-step media orchestration for production-grade automation systems.

**Included projects (14):** [#1](https://github.com/santifer/jacobo-workflows), [#4](https://github.com/devlikeapro/n8n-nodes-waha), [#5](https://github.com/devlikeapro/waha), [#7](https://github.com/simonleybovich/linkedin-job-alerts), [#8](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Notion/Automate%20LinkedIn%20Outreach%20with%20Notion%20and%20OpenAI.json), [#9](https://github.com/lucaswalter/n8n-ai-automations), [#10](https://n8n.io/workflows/5099-talentflow-ai-instantly-evaluate-applicants-github-linkedin-using-ai/), [#24](https://github.com/StructUK), [#31](https://github.com/lucaswalter/n8n-ai-automations), [#39](https://github.com/MetehanYasar11/ultralytics_mcp_server), [#42](https://github.com/StructUK), [#43](https://n8n.io/workflows/6014), [#44](https://github.com/lucaswalter/n8n-ai-automations), [#46](https://github.com/chidoziemanagwu/Research-Automation-Workflow)
<!-- LEARNING_PATH:END -->

<p align="center">
  <img src="assets/divider.svg" alt="Section divider" width="100%" height="24" />
</p>

## Full Project Directory

All entries below are generated directly from [data/n8n_list.csv](data/n8n_list.csv). Entries pointing to multi-workflow repositories or GitHub profiles with pinned repositories include an explicit navigation hint to help you locate the exact workflow file.

<!-- PROJECTS:START -->
<h3><a id="category-whatsapp"></a><img src="assets/icons/whatsapp.svg" alt="WhatsApp icon" width="28" height="28" align="absmiddle" /> WhatsApp (6)</h3>

Category guide and risk notes: [docs/categories/whatsapp.md](docs/categories/whatsapp.md)

| Title | Difficulty | Phase | Tools | Source type |
| --- | --- | --- | --- | --- |
| **#1** [Jacobo AI Agent (7 production workflows)](https://github.com/santifer/jacobo-workflows) | <img src="assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 4](docs/learning-path.md#phase-4---advanced-agents-and-integrations) | n8n, WhatsApp, ElevenLabs, multi-agent tool calling | GitHub repo |
| **#2** [n8n WhatsApp AI Agent](https://github.com/ZohaibCodez/n8n-whatsapp-ai-agent) | <img src="assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 2](docs/learning-path.md#phase-2---chatbots-and-voice) | n8n, WhatsApp Business API, Gemini | GitHub repo |
| **#3** [WhatsApp Hospitality Chatbot](https://github.com/lucaswalter/n8n-ai-automations) *(open the named workflow: `whatsapp_ai_chatbot_agent.json`)* | <img src="assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 2](docs/learning-path.md#phase-2---chatbots-and-voice) | n8n, WhatsApp, LLM | GitHub repo |
| **#4** [WAHA n8n Community Node](https://github.com/devlikeapro/n8n-nodes-waha) | <img src="assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 4](docs/learning-path.md#phase-4---advanced-agents-and-integrations) | n8n community node, WAHA | GitHub repo |
| **#5** [WAHA (WhatsApp HTTP API)](https://github.com/devlikeapro/waha) | <img src="assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 4](docs/learning-path.md#phase-4---advanced-agents-and-integrations) | Docker, REST, webhooks | GitHub repo |
| **#6** [WhatsApp Template Folder](https://github.com/enescingoz/awesome-n8n-templates/tree/main/WhatsApp) | <img src="assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 2](docs/learning-path.md#phase-2---chatbots-and-voice) | n8n, WhatsApp, OpenAI | GitHub folder |

<h3><a id="category-linkedin"></a><img src="assets/icons/linkedin.svg" alt="LinkedIn icon" width="28" height="28" align="absmiddle" /> LinkedIn (4)</h3>

Category guide and risk notes: [docs/categories/linkedin.md](docs/categories/linkedin.md)

| Title | Difficulty | Phase | Tools | Source type |
| --- | --- | --- | --- | --- |
| **#7** [LinkedIn Job Alerts](https://github.com/simonleybovich/linkedin-job-alerts) | <img src="assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 4](docs/learning-path.md#phase-4---advanced-agents-and-integrations) | n8n, Gemini, Notion, Telegram | GitHub repo |
| **#8** [LinkedIn Outreach with Notion and OpenAI](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Notion/Automate%20LinkedIn%20Outreach%20with%20Notion%20and%20OpenAI.json) | <img src="assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 4](docs/learning-path.md#phase-4---advanced-agents-and-integrations) | n8n, Notion, OpenAI, LinkedIn | GitHub file |
| **#9** [Content Repurposing Factory](https://github.com/lucaswalter/n8n-ai-automations) *(open the named workflow)* | <img src="assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 4](docs/learning-path.md#phase-4---advanced-agents-and-integrations) | n8n, Apify, Claude | GitHub repo |
| **#10** [TalentFlow AI](https://n8n.io/workflows/5099-talentflow-ai-instantly-evaluate-applicants-github-linkedin-using-ai/) | <img src="assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 4](docs/learning-path.md#phase-4---advanced-agents-and-integrations) | n8n, JotForm, ScrapingDog, Apify, OpenRouter | n8n.io template |

<h3><a id="category-resume-hr"></a><img src="assets/icons/resume-hr.svg" alt="Resume/HR icon" width="28" height="28" align="absmiddle" /> Resume/HR (6)</h3>

Category guide and risk notes: [docs/categories/resume-hr.md](docs/categories/resume-hr.md)

| Title | Difficulty | Phase | Tools | Source type |
| --- | --- | --- | --- | --- |
| **#11** [Resume Bot](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/ResumeBot.json) | <img src="assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 3](docs/learning-path.md#phase-3---documents-vision-and-data) | n8n, Telegram, Supabase, LaTeX | GitHub file |
| **#12** [CV Parsing with Multimodal Vision AI](https://github.com/enescingoz/awesome-n8n-templates/blob/main/PDF_and_Document_Processing/CV%20Resume%20PDF%20Parsing%20with%20Multimodal%20Vision%20AI.json) | <img src="assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 3](docs/learning-path.md#phase-3---documents-vision-and-data) | n8n, Vision LLM | GitHub file |
| **#13** [Resume Data Extraction to PDF (Gotenberg)](https://github.com/enescingoz/awesome-n8n-templates/blob/main/PDF_and_Document_Processing/Extract%20data%20from%20resume%20and%20create%20PDF%20with%20Gotenberg.json) | <img src="assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 3](docs/learning-path.md#phase-3---documents-vision-and-data) | n8n, LLM, Gotenberg | GitHub file |
| **#14** [Job Application Handling with n8n Forms](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Airtable/Handling%20Job%20Application%20Submissions%20with%20AI%20and%20n8n%20Forms.json) | <img src="assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 3](docs/learning-path.md#phase-3---documents-vision-and-data) | n8n Forms, LLM, Airtable | GitHub file |
| **#15** [Screen Applicants with AI](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Google_Drive_and_Google_Sheets/Screen%20Applicants%20With%20AI,%20notify%20HR%20and%20save%20them%20in%20a%20Google%20Sheet.json) | <img src="assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 3](docs/learning-path.md#phase-3---documents-vision-and-data) | n8n, LLM, Google Sheets | GitHub file |
| **#16** [Internship Informer](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Internship%20Informer.json) | <img src="assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 3](docs/learning-path.md#phase-3---documents-vision-and-data) | n8n, Telegram, Firecrawl, WhatsApp | GitHub file |

<h3><a id="category-text-classification"></a><img src="assets/icons/text-classification.svg" alt="Text/Classification icon" width="28" height="28" align="absmiddle" /> Text/Classification (10)</h3>

Category guide and risk notes: [docs/categories/text-classification.md](docs/categories/text-classification.md)

| Title | Difficulty | Phase | Tools | Source type |
| --- | --- | --- | --- | --- |
| **#17** [InboxZero Lite Email Classifier](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Gmail_and_Email_Automation/InboxZero%20Lite%20-%20AI%20Email%20Classifier.json) | <img src="assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 1](docs/learning-path.md#phase-1---foundations) | n8n, Gmail, OpenAI, Google Sheets | GitHub file |
| **#18** [Gmail Auto-Labelling with OpenAI](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Gmail_and_Email_Automation/Basic%20Automatic%20Gmail%20Email%20Labelling%20with%20OpenAI%20and%20Gmail%20API.json) | <img src="assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 1](docs/learning-path.md#phase-1---foundations) | n8n, Gmail API, OpenAI | GitHub file |
| **#19** [Auto-Categorise Outlook Email](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Gmail_and_Email_Automation/Auto%20Categorise%20Outlook%20Emails%20with%20AI.json) | <img src="assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 1](docs/learning-path.md#phase-1---foundations) | n8n, Outlook, LLM | GitHub file |
| **#20** [Email Auto-Responder with Ollama](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Gmail_and_Email_Automation/AI%20Email%20Auto-Responder%20with%20Ollama.json) | <img src="assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 2](docs/learning-path.md#phase-2---chatbots-and-voice) | n8n, Ollama (local LLM) | GitHub file |
| **#21** [Toxic Language Detection in Telegram](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Detect%20toxic%20language%20in%20Telegram%20messages.json) | <img src="assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 1](docs/learning-path.md#phase-1---foundations) | n8n, Telegram, LLM moderation | GitHub file |
| **#22** [Lead Qualification with GPT-4](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Google_Drive_and_Google_Sheets/Qualify%20new%20leads%20in%20Google%20Sheets%20via%20OpenAI_s%20GPT-4.json) | <img src="assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 1](docs/learning-path.md#phase-1---foundations) | n8n, Google Sheets, OpenAI | GitHub file |
| **#23** [Text Classification API + Issue Triage](https://github.com/CodingAbdullah/n8n-workflows) | <img src="assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 3](docs/learning-path.md#phase-3---documents-vision-and-data) | n8n, webhook, OpenAI, GitHub | GitHub repo |
| **#24** [emailPlus (StructUK)](https://github.com/StructUK) *(profile page: open the pinned repo)* | <img src="assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 4](docs/learning-path.md#phase-4---advanced-agents-and-integrations) | n8n, LLM, Google Sheets | GitHub profile (pinned repo) |
| **#25** [Feedback Sentiment into Notion](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Notion/Add%20positive%20feedback%20messages%20to%20a%20table%20in%20Notion.json) | <img src="assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 1](docs/learning-path.md#phase-1---foundations) | n8n, Typeform, Google NL, Notion, Slack | GitHub file |
| **#26** [Discord AI Routing Bot](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Discord/Discord%20AI-powered%20bot.json) | <img src="assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 1](docs/learning-path.md#phase-1---foundations) | n8n, Discord, LLM | GitHub file |

<h3><a id="category-voice"></a><img src="assets/icons/voice.svg" alt="Voice icon" width="28" height="28" align="absmiddle" /> Voice (5)</h3>

Category guide and risk notes: [docs/categories/voice.md](docs/categories/voice.md)

| Title | Difficulty | Phase | Tools | Source type |
| --- | --- | --- | --- | --- |
| **#27** [Telegram Audio Translator (55 languages)](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Translate%20Telegram%20audio%20messages%20with%20AI%20(55%20supported%20languages).json) | <img src="assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 2](docs/learning-path.md#phase-2---chatbots-and-voice) | n8n, Telegram, speech-to-text | GitHub file |
| **#28** [Angie Voice and Text Assistant](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Angie,%20Personal%20AI%20Assistant%20with%20Telegram%20Voice%20and%20Text.json) | <img src="assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 2](docs/learning-path.md#phase-2---chatbots-and-voice) | n8n, Telegram, LLM | GitHub file |
| **#29** [Voice and Text Assistant Template](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Telegram%20AI%20bot%20assistant_%20ready-made%20template%20for%20voice%20&%20text%20messages.json) | <img src="assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 2](docs/learning-path.md#phase-2---chatbots-and-voice) | n8n, Telegram, LLM | GitHub file |
| **#30** [Multimodal Messaging Agent](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/%F0%9F%A4%96%20Telegram%20Messaging%20Agent%20for%20Text_Audio_Images.json) | <img src="assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 2](docs/learning-path.md#phase-2---chatbots-and-voice) | n8n, Telegram, LLM | GitHub file |
| **#31** [Dental Practice Voice Agent](https://github.com/lucaswalter/n8n-ai-automations) *(open the named workflow: `dental_practice_voice_agent.json`)* | <img src="assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 4](docs/learning-path.md#phase-4---advanced-agents-and-integrations) | n8n, voice AI, Google Calendar | GitHub repo |

<h3><a id="category-image"></a><img src="assets/icons/image.svg" alt="Image icon" width="28" height="28" align="absmiddle" /> Image (4)</h3>

Category guide and risk notes: [docs/categories/image.md](docs/categories/image.md)

| Title | Difficulty | Phase | Tools | Source type |
| --- | --- | --- | --- | --- |
| **#32** [Telegram Image Analysis Bot](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Automated%20AI%20image%20analysis%20and%20response%20via%20Telegram.json) | <img src="assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 1](docs/learning-path.md#phase-1---foundations) | n8n, Telegram, vision LLM | GitHub file |
| **#33** [Background Removal for Drive Images](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Google_Drive_and_Google_Sheets/Automatic%20Background%20Removal%20for%20Images%20in%20Google%20Drive.json) | <img src="assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 1](docs/learning-path.md#phase-1---foundations) | n8n, Google Drive, image API | GitHub file |
| **#34** [AI Product Images](https://github.com/enescingoz/awesome-n8n-templates/blob/main/AI%20product%20imagines.json) | <img src="assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 1](docs/learning-path.md#phase-1---foundations) | n8n, image generation | GitHub file |
| **#35** [Text and Image Generation Bot](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Telegram%20AI%20Bot_%20NeurochainAI%20Text%20&%20Image%20-%20NeurochainAI%20Basic%20API%20Integration.json) | <img src="assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 2](docs/learning-path.md#phase-2---chatbots-and-voice) | n8n, Telegram, NeurochainAI | GitHub file |

<h3><a id="category-computer-vision"></a><img src="assets/icons/computer-vision.svg" alt="Computer Vision icon" width="28" height="28" align="absmiddle" /> Computer Vision (4)</h3>

Category guide and risk notes: [docs/categories/computer-vision.md](docs/categories/computer-vision.md)

| Title | Difficulty | Phase | Tools | Source type |
| --- | --- | --- | --- | --- |
| **#36** [License Plate Extraction](https://github.com/enescingoz/awesome-n8n-templates/blob/main/PDF_and_Document_Processing/Extract%20license%20plate%20number%20from%20image%20uploaded%20via%20an%20n8n%20form.json) | <img src="assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 3](docs/learning-path.md#phase-3---documents-vision-and-data) | n8n Forms, vision LLM | GitHub file |
| **#37** [Phishing Email Analysis with Vision](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Gmail_and_Email_Automation/Analyze%20Suspicious%20Email%20Contents%20with%20ChatGPT%20Vision.json) | <img src="assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 3](docs/learning-path.md#phase-3---documents-vision-and-data) | n8n, Gmail, ChatGPT Vision | GitHub file |
| **#38** [OCR from PDFs and Images to CSV](https://github.com/enescingoz/awesome-n8n-templates/blob/main/PDF_and_Document_Processing/Extract%20text%20from%20PDF%20and%20image%20using%20Vertex%20AI%20(Gemini)%20into%20CSV.json) | <img src="assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 3](docs/learning-path.md#phase-3---documents-vision-and-data) | n8n, Vertex AI Gemini | GitHub file |
| **#39** [Ultralytics YOLO MCP Server](https://github.com/MetehanYasar11/ultralytics_mcp_server) | <img src="assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 4](docs/learning-path.md#phase-4---advanced-agents-and-integrations) | Docker, YOLO, MCP, n8n | GitHub repo |

<h3><a id="category-video"></a><img src="assets/icons/video.svg" alt="Video icon" width="28" height="28" align="absmiddle" /> Video (5)</h3>

Category guide and risk notes: [docs/categories/video.md](docs/categories/video.md)

| Title | Difficulty | Phase | Tools | Source type |
| --- | --- | --- | --- | --- |
| **#40** [YouTube Summaries to Discord](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Discord/Share%20YouTube%20Videos%20with%20AI%20Summaries%20on%20Discord.json) | <img src="assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 1](docs/learning-path.md#phase-1---foundations) | n8n, YouTube, LLM, Discord | GitHub file |
| **#41** [Drive to Instagram and TikTok](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Google_Drive_and_Google_Sheets/Upload%20to%20Instagram%20and%20Tiktok%20from%20Google%20Drive.json) | <img src="assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 3](docs/learning-path.md#phase-3---documents-vision-and-data) | n8n, Google Drive, social APIs | GitHub file |
| **#42** [Video Cross-Posting Framework](https://github.com/StructUK) *(profile page: open the pinned repo)* | <img src="assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 4](docs/learning-path.md#phase-4---advanced-agents-and-integrations) | n8n, posting-provider adapters | GitHub profile (pinned repo) |
| **#43** [Faceless Video Pipeline](https://n8n.io/workflows/6014) | <img src="assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 4](docs/learning-path.md#phase-4---advanced-agents-and-integrations) | n8n, Gemini, ElevenLabs, Whisper, Shotstack | n8n.io template |
| **#44** [Viral Video Clipper](https://github.com/lucaswalter/n8n-ai-automations) *(open the named workflow)* | <img src="assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 4](docs/learning-path.md#phase-4---advanced-agents-and-integrations) | n8n, Vizard AI, Slack | GitHub repo |

<h3><a id="category-paper"></a><img src="assets/icons/paper.svg" alt="Paper icon" width="28" height="28" align="absmiddle" /> Paper (6)</h3>

Category guide and risk notes: [docs/categories/paper.md](docs/categories/paper.md)

| Title | Difficulty | Phase | Tools | Source type |
| --- | --- | --- | --- | --- |
| **#45** [Hugging Face Papers to Notion](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Notion/Analyse%20papers%20from%20Hugging%20Face%20with%20AI%20and%20store%20them%20in%20Notion.json) | <img src="assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 3](docs/learning-path.md#phase-3---documents-vision-and-data) | n8n, Hugging Face, LLM, Notion | GitHub file |
| **#46** [Research Automation (5 Academic APIs)](https://github.com/chidoziemanagwu/Research-Automation-Workflow) | <img src="assets/badges/difficulty-advanced.svg" alt="Advanced" height="18" /> | [Phase 4](docs/learning-path.md#phase-4---advanced-agents-and-integrations) | n8n, Groq, Sheets, Gmail | GitHub repo |
| **#47** [arXiv Paper Summariser](https://n8n.io/workflows/2904-arxiv-paper-summarization-with-chatgpt/) | <img src="assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 3](docs/learning-path.md#phase-3---documents-vision-and-data) | n8n, webhook, ChatGPT | n8n.io template |
| **#48** [Chat with PDF (quoting sources)](https://github.com/enescingoz/awesome-n8n-templates/blob/main/PDF_and_Document_Processing/Chat%20with%20PDF%20docs%20using%20AI%20(quoting%20sources).json) | <img src="assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 2](docs/learning-path.md#phase-2---chatbots-and-voice) | n8n, embeddings, vector store | GitHub file |
| **#49** [Telegram Chat with PDF](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Telegram%20chat%20with%20PDF.json) | <img src="assets/badges/difficulty-beginner.svg" alt="Beginner" height="18" /> | [Phase 1](docs/learning-path.md#phase-1---foundations) | n8n, Telegram, LLM | GitHub file |
| **#50** [Invoice Extraction (LlamaParse + OpenAI)](https://github.com/enescingoz/awesome-n8n-templates/blob/main/PDF_and_Document_Processing/Invoice%20data%20extraction%20with%20LlamaParse%20and%20OpenAI.json) | <img src="assets/badges/difficulty-intermediate.svg" alt="Intermediate" height="18" /> | [Phase 3](docs/learning-path.md#phase-3---documents-vision-and-data) | n8n, LlamaParse, OpenAI | GitHub file |
<!-- PROJECTS:END -->

<p align="center">
  <img src="assets/divider.svg" alt="Section divider" width="100%" height="24" />
</p>

## How to Use a Project

Follow the full setup walkthrough in [docs/getting-started.md](docs/getting-started.md) to run an isolated local n8n instance before importing workflows:

1. **Start an isolated n8n instance**: Run n8n locally via Docker (`docker.n8n.io/n8nio/n8n`) or `npx n8n` so tests never touch production data or credentials.
2. **Import the workflow JSON**: Open the project link, download the `.json` file (or copy the template on `n8n.io`), and import it using **Import from File** in the n8n editor while keeping the workflow inactive.
3. **Inspect nodes and add credentials**: Review every `Code`, `Execute Command`, `HTTP Request`, and community node, then map each service node to scoped test credentials stored in n8n's Credential Manager.
4. **Test with sample data**: Pin test payloads on the trigger node and run single-step executions before activating schedules or public webhooks.

## Quality and Trust Notes

- **Dataset integrity**: [data/n8n_list.csv](data/n8n_list.csv) is validated on every pull request by [scripts/validate_csv.py](scripts/validate_csv.py) and synchronized with this documentation by [scripts/build_readme.py](scripts/build_readme.py). See [data/README.md](data/README.md) for the full schema.
- **Automated link verification**: [scripts/check_links.py](scripts/check_links.py) runs on a weekly schedule via GitHub Actions (`.github/workflows/links.yml`) using HTTP `HEAD`/`GET` checks with retries and timeouts.
- **Understanding `verified_date` and `status`**: `verified_date` records the ISO date (`YYYY-MM-DD`) when a link was last checked; `status` documents its verification state (for example, entries initially collected from search or repository READMEs carry `Link seen in search or README; re-check before publishing` until independently reviewed).
- **Third-party ownership and no redistribution**: Nearly all workflows and repositories linked here are authored and maintained by independent third parties. Original authors retain full copyright and ownership of their work, and each linked project remains governed by its own upstream license. This repository publishes curated metadata and links only; it does not copy or redistribute third-party workflow files unless explicitly permitted.
- **Repository maintenance**: Maintainer procedures and review standards are documented in [docs/maintenance.md](docs/maintenance.md).

## Community and Governance

- **Contributing**: Read [CONTRIBUTING.md](CONTRIBUTING.md) for inclusion criteria, CSV rules, and pull request checks.
- **Code of Conduct**: Participation is governed by [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
- **Security**: Report malicious links, leaked upstream secrets, or tooling vulnerabilities privately via [SECURITY.md](SECURITY.md).
- **Support**: Ask questions in [GitHub Discussions](https://github.com/Automate-Workflow/n8n-projects/discussions) and review [SUPPORT.md](SUPPORT.md) for issue templates and scope boundaries.
- **Releases and Citation**: See [CHANGELOG.md](CHANGELOG.md) and [CITATION.cff](CITATION.cff).

## License and Acknowledgements

This curated repository's documentation, scripts, and original SVG assets are licensed under the [MIT License](LICENSE) (Copyright 2026 Automate Workflow).

### Notice on Linked Third-Party Projects

The MIT License applies solely to the files authored within `Automate-Workflow/n8n-projects`. Every external repository, workflow JSON file, and `n8n.io` template linked in this directory remains the property of its respective author and is subject to its own license terms. Always verify the upstream repository license before adapting third-party workflows for commercial or production use.

### Acknowledgements

- Thank you to the individual workflow authors, open-source maintainers, and `n8n.io` community creators whose projects make hands-on automation learning possible.
- Built for learners and practitioners in the n8n open-source ecosystem.
