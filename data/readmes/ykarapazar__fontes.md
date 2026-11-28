<h1 align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/brand/lockup-dark.svg">
    <img src="docs/assets/brand/lockup.svg" alt="Fontes" width="360">
  </picture>
</h1>

<p align="center">
  Case law and legislation for your AI app, read live from court and government websites.
</p>

<!-- mcp-name: io.github.ykarapazar/fontes -->

Fontes is a free, open-source MCP server. It lets your AI app **look up court decisions and
legislation live on government and court websites** in 125 jurisdictions and international
courts. Every result links to the original. It can also show a law as it stood on a past date,
and read legislation from 91 more countries, from Lexifina's record (not the official
publisher). It is a standard Model Context Protocol (MCP) server, so it works in any app that
can run a local MCP server: Claude Desktop, Claude Code, OpenAI Codex, Cursor, VS Code (GitHub
Copilot), Gemini CLI, Windsurf, Zed, LM Studio and more.

- **For lawyers and researchers:** ask in plain language. Your AI app searches the official
  source and quotes from what it finds, with the source link.
- **For developers:** one MCP server with nine fixed research tools (plus `report_bug`); the
  jurisdiction is a parameter, so adding countries does not add tools. Python, Apache 2.0.
- **Checked against the official text:** for today's text of Dutch and UK legislation and US Code
  sections, `get_law_on_date` also fetches the official page and tells you whether Lexifina's
  record matches it, quoting any passages that differ. Other countries are not compared.

For machines: [llms.txt](https://ykarapazar.github.io/fontes/llms.txt).

## What can I ask?

```text
Find Dutch Supreme Court decisions on non-compete clauses since 2023.
Show me article 6 of the German Civil Code.
Find UK Supreme Court judgments since 2020 that mention "duty of care".
Search HUDOC for European Court of Human Rights judgments on Article 8 and surveillance.
Find Turkish Constitutional Court decisions on freedom of expression.
What did 11 U.S.C. §1182 say on 1 May 2022?
Which jurisdictions can Fontes search?
```

Your AI app picks the jurisdiction and tool, searches the official source, and gives you the
link to each result. Open it and read the original before you rely on it.

<p align="center"><img src="docs/assets/demo.gif" alt="Screen recording of an AI app using Fontes: asked for five funny court cases from around the world, it searches several countries' case law, then pulls the UK VAT Act 1994 sections behind a poppadom-versus-crisps tax case from legislation.gov.uk, with links." width="720"></p>

> **Beta (v0.1).** Fontes reads court and government websites live, and those sites change
> without notice. Expect some searches to fail, run slowly or return thin results. Today's state
> of every source is on the [status page](https://ykarapazar.github.io/fontes/status/), checked daily. If a result looks wrong,
> tell us: ask your AI app to "report a Fontes bug", or [open an issue](https://github.com/ykarapazar/fontes/issues).

<p align="center">
  <a href="LICENSE"><img alt="Licence: Apache 2.0" src="https://img.shields.io/badge/licence-Apache--2.0-blue"></a>
  <a href="pyproject.toml"><img alt="Python 3.13+" src="https://img.shields.io/badge/python-3.13%2B-blue"></a>
  <a href="https://pypi.org/project/fontes-mcp/"><img alt="PyPI: fontes-mcp" src="https://img.shields.io/pypi/v/fontes-mcp?label=PyPI"></a>
  <a href="https://modelcontextprotocol.io"><img alt="MCP server" src="https://img.shields.io/badge/MCP-server-6f42c1"></a>
  <a href="https://ykarapazar.github.io/fontes/status/"><img alt="Source health, checked daily" src="https://img.shields.io/github/actions/workflow/status/ykarapazar/fontes/health.yml?label=source%20health%20(daily)"></a>
</p>

<!-- languages:start -->
Languages: **English** · [简体中文](docs/i18n/zh-Hans/README.md) · [हिन्दी](docs/i18n/hi/README.md) · [español](docs/i18n/es/README.md) · [العربية](docs/i18n/ar/README.md)

<details>
<summary>All 80 languages</summary>

- **Europe:** **English** · [français](docs/i18n/fr/README.md) · [Deutsch](docs/i18n/de/README.md) · [русский](docs/i18n/ru/README.md) · [italiano](docs/i18n/it/README.md) · [polski](docs/i18n/pl/README.md) · [Nederlands](docs/i18n/nl/README.md) · [português europeu](docs/i18n/pt-PT/README.md) · [română](docs/i18n/ro/README.md) · [Türkçe](docs/i18n/tr/README.md) · [svenska](docs/i18n/sv/README.md) · [čeština](docs/i18n/cs/README.md) · [magyar](docs/i18n/hu/README.md) · [Ελληνικά](docs/i18n/el/README.md) · [català](docs/i18n/ca/README.md) · [српски](docs/i18n/sr/README.md) · [srpski](docs/i18n/sr-Latn/README.md) · [български](docs/i18n/bg/README.md) · [dansk](docs/i18n/da/README.md) · [slovenčina](docs/i18n/sk/README.md) · [shqip](docs/i18n/sq/README.md) · [hrvatski](docs/i18n/hr/README.md) · [suomi](docs/i18n/fi/README.md) · [norsk bokmål](docs/i18n/nb/README.md) · [norsk nynorsk](docs/i18n/nn/README.md) · [bosanski](docs/i18n/bs/README.md) · [босански](docs/i18n/bs-Cyrl/README.md) · [lietuvių](docs/i18n/lt/README.md) · [slovenščina](docs/i18n/sl/README.md) · [Gaeilge](docs/i18n/ga/README.md) · [latviešu](docs/i18n/lv/README.md) · [eesti](docs/i18n/et/README.md) · [Malti](docs/i18n/mt/README.md) · [Lëtzebuergesch](docs/i18n/lb/README.md) · [íslenska](docs/i18n/is/README.md) · [հայերեն](docs/i18n/hy/README.md) · [ქართული](docs/i18n/ka/README.md) · [azərbaycan](docs/i18n/az/README.md)
- **Middle East & North Africa:** [العربية](docs/i18n/ar/README.md) · [فارسی](docs/i18n/fa/README.md) · [עברית](docs/i18n/he/README.md) · [کوردیی ناوەندی](docs/i18n/ckb/README.md) · [ⵜⴰⵎⴰⵣⵉⵖⵜ](docs/i18n/zgh/README.md)
- **Sub-Saharan Africa:** [አማርኛ](docs/i18n/am/README.md) · [Èdè Yorùbá](docs/i18n/yo/README.md) · [Malagasy](docs/i18n/mg/README.md) · [Wolof](docs/i18n/wo/README.md) · [Ikinyarwanda](docs/i18n/rw/README.md)
- **South & Central Asia:** [हिन्दी](docs/i18n/hi/README.md) · [বাংলা](docs/i18n/bn/README.md) · [اردو](docs/i18n/ur/README.md) · [தமிழ்](docs/i18n/ta/README.md) · [پښتو](docs/i18n/ps/README.md) · [नेपाली](docs/i18n/ne/README.md) · [o‘zbek](docs/i18n/uz/README.md) · [ўзбекча](docs/i18n/uz-Cyrl/README.md) · [тоҷикӣ](docs/i18n/tg/README.md) · [türkmen dili](docs/i18n/tk/README.md) · [кыргызча](docs/i18n/ky/README.md) · [རྫོང་ཁ](docs/i18n/dz/README.md) · [ދިވެހި](docs/i18n/dv/README.md)
- **East & Southeast Asia:** [简体中文](docs/i18n/zh-Hans/README.md) · [繁體中文](docs/i18n/zh-Hant/README.md) · [臺灣台語](docs/i18n/nan-Hant/README.md) · [臺灣客家語](docs/i18n/hak-Hant/README.md) · [日本語](docs/i18n/ja/README.md) · [Tiếng Việt](docs/i18n/vi/README.md) · [Indonesia](docs/i18n/id/README.md) · [Filipino](docs/i18n/fil/README.md) · [မြန်မာ](docs/i18n/my/README.md) · [Melayu](docs/i18n/ms/README.md) · [ខ្មែរ](docs/i18n/km/README.md) · [ລາວ](docs/i18n/lo/README.md) · [монгол](docs/i18n/mn/README.md)
- **Americas & Pacific:** [español](docs/i18n/es/README.md) · [português](docs/i18n/pt/README.md) · [Runasimi](docs/i18n/qu/README.md) · [Aymar aru](docs/i18n/ay/README.md) · [Avañeʼẽ](docs/i18n/gn/README.md) · [Kreyòl ayisyen](docs/i18n/ht/README.md)

</details>
<!-- languages:end -->

Source status (checked daily): [ykarapazar.github.io/fontes/status/](https://ykarapazar.github.io/fontes/status/)
· Coverage per jurisdiction: [docs/COVERAGE.md](docs/COVERAGE.md)
· Questions and answers: [docs/FAQ.md](docs/FAQ.md)

## Quickstart

1. **Add Fontes to your app.**
   - **Claude Desktop:** download the Fontes `.mcpb` file from the
     [latest release](https://github.com/ykarapazar/fontes/releases/latest), double-click it,
     then click **Install**.
   - **Codex:** `codex mcp add fontes -- uvx fontes-mcp`
   - **Claude Code:** `claude mcp add fontes -- uvx fontes-mcp`
   - **Cursor, VS Code, Gemini CLI, Zed, LM Studio, Cline and other apps:** paste the snippet
     for your app from [docs/INSTALL.md](docs/INSTALL.md#other-apps).

   `uvx` comes with [uv](https://docs.astral.sh/uv/getting-started/installation/). To install
   uv on macOS or Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`. On Windows
   (PowerShell): `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`.
2. **Restart the app.** Quit it completely and open it again.
3. **Ask:** *"Which jurisdictions can Fontes search?"* It should list the countries.

**On a Mac or Windows PC**, a one-click installer sets up Fontes in Claude Desktop, Codex, Claude Code, Cursor,
VS Code, Windsurf, Gemini CLI, Zed, LM Studio and Cline, in each one on your computer, then
offers to add your keys. Download the installer for your computer from the [latest release](https://github.com/ykarapazar/fontes/releases/latest) and quit
those apps before you run it. Details:
[docs/INSTALL.md](docs/INSTALL.md#one-click-installer-mac-and-windows).
Some sources need a free key: see [docs/KEYS.md](docs/KEYS.md).

<!-- map:start -->
<p align="center"><a href="https://ykarapazar.github.io/fontes/#map"><picture><source media="(prefers-color-scheme: dark)" srcset="docs/assets/coverage-map-dark.svg"><img src="docs/assets/coverage-map.svg" alt="Map of the 125 live jurisdictions Fontes searches, 72 of them covered completely." width="880"></picture></a></p>
<!-- map:end -->

## What it does and doesn't do

- **Does:** fetch live at the moment you ask, from the publisher's own website or API. Every
  result names its source and carries its URL or official identifier so you can open the
  original.
- **Does not:** keep a database, download in bulk, cache texts to disk, or send your
  questions anywhere except to the source being searched (for Lexifina's record, that is
  Lexifina's server; see below). No account. Besides the sources,
  Fontes makes a once-a-day version check against PyPI (off with `FONTES_NO_UPDATE_CHECK=1`);
  anything else (usage counts, bug reports) is opt-in and asks you first.
- **Lexifina's record is the exception.** `get_law_on_date`, `get_law_history` and 91 more
  countries are read through [Lexifina](https://github.com/lexifina/global-law)'s free hosted
  server, not from the official site. See below.
- **Does not** give legal advice or decide which version of a text is authoritative.
  Coverage differs a lot between countries: some have full case law and consolidated
  legislation, some only one court or laws as originally published. The tables below and
  `list_jurisdictions` say exactly what each one covers.

### Past versions and more countries, from Lexifina

[Lexifina](https://github.com/lexifina/global-law) keeps the law of about 200 countries as git
history: each change is a commit dated the day it took effect. Fontes reads it through Lexifina's
free hosted MCP server (`https://global-law.lexifina.com/mcp`), which adds:

- `get_law_on_date` and `get_law_history`: a provision as in force on a past date, and what
  changed it, for any country in Lexifina's record.
- 91 more countries and territories (for example South Africa, Kenya, Mexico, New Zealand,
  Russia, South Korea, Belgium, Lithuania, Ukraine, Malaysia, Thailand, Saudi Arabia) through
  the four legislation tools. Legislation only, no case law. Coverage per country varies a lot
  (Kenya's national record holds 9 acts); `list_jurisdictions` shows what each holds. They are
  described separately from the 125 jurisdictions with live official coverage. India is one of those
  125 (Supreme Court judgments, live), and its Acts are read from Lexifina's record too.

Lexifina is not the official publisher, and its record is not live. Lexifina rechecks each country against
its official source from time to time; on 2026-11-26 its own freshness report counted 338 of 383
national bodies of law as not checked in the last 7 days. Every answer from it names
Lexifina as the source, links the official publisher's page and says how far the record goes. Check the official
text before you rely on it.

Lexifina's sourcing policy differs from Fontes's. It takes the view that official legal texts are
not protected by copyright, so in some countries it copies sites whose terms or robots.txt Fontes
itself respects (sometimes through Internet Archive copies). Fontes still respects robots.txt
and terms for everything it fetches itself; what comes through Lexifina follows Lexifina's own
legal judgement, recorded per country in its repositories (LICENSE/SOURCES.md). A few restrict
use: Kenya's publisher is CC BY-NC, and some sources ask for non-commercial use.

For these two tools and these countries, your search words, citations and dates go to Lexifina's
server (`global-law.lexifina.com`), not only to the official source. It is on by default; set
`WLM_LEXIFINA=0` to turn it off. No key or account. The free server allows 60 calls a minute and
10,000 a day per internet address. Fontes is not affiliated with Lexifina, which built and
maintains the record. See [docs/PRIVACY.md](docs/PRIVACY.md).

### Read this before you rely on a result

- **Not every source is the official, authentic version.** Most are government or court
  sites, but some consolidated texts are expressly unofficial (only the official gazette is
  authentic), and a few sources are non-government (e.g. LexiVox, LawPhil, Maqam, Wikisource).
  Fontes marks these with an "Unofficial source" notice in its answers. Check the official
  publication before you cite.
- **Each source has its own terms.** The data stays under its publisher's licence; some
  forbid commercial use, some require attribution (e.g. CC BY sources), and a few forbid
  automated access without permission. Sources that need permission are **off** by default
  (marked OFF below). See [Sources, terms and robots.txt](#sources-terms-and-robotstxt).
- **AI can misread.** Read the full decision or provision before relying on it; never cite
  from a search snippet or from the AI's summary alone.
- **Sources lag and have gaps.** A court may publish late or only some of its decisions, and a
  consolidated text may not yet include the latest amendment. Check the date of the text and
  the gaps `list_jurisdictions` lists for that jurisdiction.
- **Not legal advice.** Fontes is a research tool. Using it does not create a lawyer–client
  relationship with anyone, and it does not replace advice from a lawyer qualified where your
  question arises.
- **No warranty.** Fontes is provided "as is", without warranty of any kind, and its authors
  are not liable for how it is used, as far as the law allows. The full terms are in sections 7
  and 8 of the [LICENSE](LICENSE) (Apache 2.0).
- Fontes is an independent open-source project. It is not affiliated with or endorsed by any
  of the courts, governments or publishers it reads from.

## Why I built this

Fontes was made by a lawyer, for lawyers. =) And for everyone else who has ever needed to read the law that applies to them.

The law is public. Court decisions and legislation are published by courts and governments so that people can read them. But each country publishes in its own way, on its own website, in its own language, and many of those websites are built for people who already know where to look. AI assistants can help, but when they can't see the source, they guess.

Fontes connects your AI app to those official sources. It fetches court decisions and legislation live from the courts and governments that publish them, links every result to the original, and keeps no database of its own.

I believe every lawyer and every citizen, anywhere, should be able to look up the law that governs them, and use it to protect their rights. That is why Fontes is free and open source, for legal practitioners and citizens alike.

If something is broken, or a country you need is missing, please [open an issue](https://github.com/ykarapazar/fontes/issues). That is the most useful help there is.

Yüce Karapazar

## Coverage

Each jurisdiction's case-law and legislation sources. `list_jurisdictions` and
[docs/COVERAGE.md](docs/COVERAGE.md) give the full detail.

<details>
<summary>Coverage table (code, jurisdiction, case law, legislation)</summary>

<!-- coverage:start -->
| Code | Jurisdiction | Case law | Legislation |
|---|---|---|---|
| `ad` | [Andorra](https://ykarapazar.github.io/fontes/law/ad/) | Tribunal Constitucional del Principat d'Andorra: sentències and autes | Portal Jurídic del Principat d'Andorra (BOPA service, Govern d'Andorra / Consell General): consolidated laws and Government regulations, Consell General del Principat d'Andorra: Constitució (Catalan booklet PDF) |
| `af` | [Afghanistan](https://ykarapazar.github.io/fontes/law/af/) | — | Ministry of Justice laws database (de facto authority) |
| `afchpr` | [African Court on Human and Peoples' Rights](https://ykarapazar.github.io/fontes/law/afchpr/) | AJUDATA, the African Court's case database (ajudata.african-court.org) | — |
| `al` | [Albania](https://ykarapazar.github.io/fontes/law/al/) | Gjykata e Lartë (High Court of Albania, gjykataelarte.gov.al) | Qendra e Botimeve Zyrtare (qbz.gov.al, Ministry of Justice) |
| `am` | [Armenia](https://ykarapazar.github.io/fontes/law/am/) | ARLIS, Armenian Legal Information System (unified official publication website; Ministry of Justice / Official Bulletin CJSC) | ARLIS, Armenian Legal Information System (unified official publication website; Ministry of Justice / Official Bulletin CJSC) |
| `ar` | [Argentina](https://ykarapazar.github.io/fontes/law/ar/) | — | InfoLEG (national laws) |
| `at` | [Austria](https://ykarapazar.github.io/fontes/law/at/) | RIS (OGH, VfGH, VwGH, BVwG, LVwG, DSB) | RIS federal law |
| `au` | [Australia (Commonwealth)](https://ykarapazar.github.io/fontes/law/au/) | — | Federal Register of Legislation |
| `az` | [Azerbaijan](https://ykarapazar.github.io/fontes/law/az/) | e-qanun.az, Unified Electronic Database of Legal Acts (Ministry of Justice) (OFF) | e-qanun.az, Unified Electronic Database of Legal Acts (Ministry of Justice) (OFF) |
| `ba` | [Bosnia and Herzegovina](https://ykarapazar.github.io/fontes/law/ba/) | Ustavni sud Bosne i Hercegovine (ustavnisud.ba) – decisions database | Vlada Federacije BiH (fbihvlada.gov.ba) – Hronološki registar zakona (Federation laws as published), Parlamentarna skupština BiH (parlament.ba) – Ustav BiH and Prečišćeni tekstovi zakona (state level) |
| `bb` | [Barbados](https://ykarapazar.github.io/fontes/law/bb/) | Barbados Judicial System: judgments (barbadoslawcourts.gov.bb), CCJ judgment lists and PDFs (ccj.org) | Barbados Judicial System: Consolidated Laws (barbadoslawcourts.gov.bb) |
| `bd` | [Bangladesh](https://ykarapazar.github.io/fontes/law/bd/) | Supreme Court of Bangladesh (supremecourt.gov.bd) – Judgments and Orders | Laws of Bangladesh (bdlaws.minlaw.gov.bd), Legislative and Parliamentary Affairs Division |
| `bg` | [Bulgaria](https://ykarapazar.github.io/fontes/law/bg/) | Конституционен съд (Constitutional Court), constcourt.bg | Народно събрание (National Assembly), parliament.bg API: Constitution and laws as adopted |
| `bh` | [Bahrain](https://ykarapazar.github.io/fontes/law/bh/) | Legislation and Legal Opinion Commission (هيئة التشريع والرأي القانوني), lloc.gov.bh (OFF) | Legislation and Legal Opinion Commission (هيئة التشريع والرأي القانوني), lloc.gov.bh (OFF) |
| `bj` | [Benin](https://ykarapazar.github.io/fontes/law/bj/) | Cour constitutionnelle du Bénin: décisions (courconstitutionnelle.bj) | Secrétariat général du Gouvernement du Bénin: lois, décrets, ordonnances (sgg.gouv.bj) |
| `bo` | [Bolivia](https://ykarapazar.github.io/fontes/law/bo/) | Tribunal Agroambiental – Buscador de Resoluciones (SISAGRO consultas) | Cámara de Diputados – Leyes Promulgadas (WP REST API), laws as promulgated, LexiVox – Bolivian legislation (constitution, laws, decree-laws, codes; unofficial) |
| `br` | [Brazil](https://ykarapazar.github.io/fontes/law/br/) | STF (Supreme Federal Court) | normas.leg.br |
| `bs` | [The Bahamas](https://ykarapazar.github.io/fontes/law/bs/) | Find Case Law, The National Archives (UK): Judicial Committee of the Privy Council judgments, Court of Appeal of The Bahamas judgments (courtofappeal.org.bs), Supreme Court of The Bahamas judgments, The Judiciary of The Bahamas (courts.bs) | Statute Law of The Bahamas, Law Reform and Revision Commission (laws.bahamas.gov.bs) |
| `bt` | [Bhutan](https://ykarapazar.github.io/fontes/law/bt/) | — | Depository of Laws (legislation.gov.bt), Office of the Attorney General of Bhutan |
| `bz` | [Belize](https://ykarapazar.github.io/fontes/law/bz/) | Judgments of the Senior Courts of Belize, Belize Judiciary (belizejudiciary.org), CCJ judgment lists and PDFs (ccj.org), Find Case Law, The National Archives | Laws of Belize, Attorney General's Ministry (agm.gov.bz) |
| `ca` | [Canada (federal)](https://ykarapazar.github.io/fontes/law/ca/) | Supreme Court of Canada | Justice Laws |
| `ccj` | [Caribbean Court of Justice](https://ykarapazar.github.io/fontes/law/ccj/) | CCJ judgment lists and PDFs (ccj.org) | — |
| `ch` | [Switzerland (federal)](https://ykarapazar.github.io/fontes/law/ch/) | Federal Supreme Court (bger.ch) | Fedlex (SR) |
| `ci` | [Côte d'Ivoire](https://ykarapazar.github.io/fontes/law/ci/) | Cour de cassation de Côte d'Ivoire: jurisprudence (eservices / sigcc) | Assemblée nationale de Côte d'Ivoire: lois (assnat.ci) |
| `cl` | [Chile](https://ykarapazar.github.io/fontes/law/cl/) | — | BCN Ley Chile |
| `cm` | [Cameroon](https://ykarapazar.github.io/fontes/law/cm/) | Cour suprême du Cameroun (coursupreme.cm) | Présidence de la République du Cameroun (prc.cm), Actes: lois, ordonnances, décrets |
| `cn` | [China](https://ykarapazar.github.io/fontes/law/cn/) | Supreme People's Court guiding cases | — |
| `co` | [Colombia](https://ykarapazar.github.io/fontes/law/co/) | Corte Constitucional | Función Pública – Gestor Normativo (consolidated legislation) (OFF) |
| `cr` | [Costa Rica](https://ykarapazar.github.io/fontes/law/cr/) | — | SINALEVI – Sistema Nacional de Legislación Vigente (Procuraduría General de la República, SCIJ) |
| `cu` | [Cuba](https://ykarapazar.github.io/fontes/law/cu/) | — | Gaceta Oficial de la República de Cuba (gacetaoficial.gob.cu), Ministerio de Justicia de Cuba (Gaceta Oficial reposts) |
| `cv` | [Cabo Verde](https://ykarapazar.github.io/fontes/law/cv/) | Tribunal Constitucional de Cabo Verde (tribunalconstitucional.cv), Supremo Tribunal de Justiça de Cabo Verde, jurisprudência (stj.cv), JURIS CV – Jurisprudência Cabo-verdiana (Conselho Superior da Magistratura Judicial) | Tribunal Constitucional de Cabo Verde (tribunalconstitucional.cv) |
| `cz` | [Czechia](https://ykarapazar.github.io/fontes/law/cz/) | rozhodnuti.justice.cz (lower courts) | e-Sbírka |
| `de` | [Germany (federal)](https://ykarapazar.github.io/fontes/law/de/) | NeuRIS (federal courts, trial service) (OFF) | Gesetze im Internet |
| `difc` | [DIFC Courts (Dubai)](https://ykarapazar.github.io/fontes/law/difc/) | DIFC Courts judgments (OFF) | — |
| `dk` | [Denmark](https://ykarapazar.github.io/fontes/law/dk/) | — | Retsinformation |
| `do` | [Dominican Republic](https://ykarapazar.github.io/fontes/law/do/) | Tribunal Superior Electoral – visor de sentencias (visorpdf.tse.do) | — |
| `dz` | [Algeria](https://ykarapazar.github.io/fontes/law/dz/) | Cour constitutionnelle (and former Conseil constitutionnel) of Algeria | Journal Officiel de la République Algérienne (JORADP), Secrétariat Général du Gouvernement |
| `ec` | [Ecuador](https://ykarapazar.github.io/fontes/law/ec/) | Corte Constitucional del Ecuador – Buscador de Sentencias (public JSON backend) and signed decision PDFs (esacc storage) | — |
| `echr` | [European Court of Human Rights](https://ykarapazar.github.io/fontes/law/echr/) | HUDOC | — |
| `ecowas` | [ECOWAS Community Court of Justice](https://ykarapazar.github.io/fontes/law/ecowas/) | ECOWAS Community Court of Justice website (courtecowas.org), ECOWAS Court Law Reports (CCJELR), English volumes 2004-2017 (courtecowas.org) | — |
| `ee` | [Estonia](https://ykarapazar.github.io/fontes/law/ee/) | — | Riigi Teataja |
| `efta` | [EFTA Court](https://ykarapazar.github.io/fontes/law/efta/) | EFTA Court judgments | — |
| `eg` | [Egypt](https://ykarapazar.github.io/fontes/law/eg/) | المحكمة الدستورية العليا – Supreme Constitutional Court portal (judgments, full text) | — |
| `es` | [Spain](https://ykarapazar.github.io/fontes/law/es/) | Constitutional Court only | BOE consolidated law |
| `et` | [Ethiopia](https://ykarapazar.github.io/fontes/law/et/) | — | House of Peoples' Representatives: published laws (Federal Negarit Gazeta PDFs, hopr.gov.et) |
| `eu` | [European Union](https://ykarapazar.github.io/fontes/law/eu/) | CELLAR (CJEU) | CELLAR (EUR-Lex) |
| `fi` | [Finland](https://ykarapazar.github.io/fontes/law/fi/) | Finlex (KKO/KHO precedents) | Finlex open data |
| `fr` | [France](https://ykarapazar.github.io/fontes/law/fr/) | Judilibre (Cour de cassation, via PISTE), Légifrance API (DILA, via PISTE) | Légifrance API (DILA, via PISTE) |
| `gb` (alias `uk`) | [United Kingdom](https://ykarapazar.github.io/fontes/law/gb/) | Find Case Law (The National Archives, 2003 onward) | legislation.gov.uk |
| `ge` | [Georgia](https://ykarapazar.github.io/fontes/law/ge/) | Courts of Georgia (2018–2020) | Matsne |
| `gr` | [Greece](https://ykarapazar.github.io/fontes/law/gr/) | Areios Pagos | Government Gazette (FEK) (OFF) |
| `gt` | [Guatemala](https://ykarapazar.github.io/fontes/law/gt/) | Corte de Constitucionalidad – sentencias PDF (jurisprudencia.cc.gob.gt) (partial) | — |
| `gy` | [Guyana](https://ykarapazar.github.io/fontes/law/gy/) | CCJ judgment lists and PDFs (ccj.org) | Laws of Guyana, Ministry of Legal Affairs (mola.gov.gy) |
| `hk` | [Hong Kong](https://ykarapazar.github.io/fontes/law/hk/) | — | Hong Kong e-Legislation (open data) |
| `hn` | [Honduras](https://ykarapazar.github.io/fontes/law/hn/) | — | Biblioteca Virtual del Tribunal Superior de Cuentas (TSC) – laws, codes, regulations and decrees as published (PDF, mostly La Gaceta copies), ENAG – La Gaceta Digital (Diario Oficial de la República de Honduras) |
| `hr` | [Croatia](https://ykarapazar.github.io/fontes/law/hr/) | Constitutional Court (in the gazette) | Narodne novine |
| `ht` | [Haiti](https://ykarapazar.github.io/fontes/law/ht/) | — | Conseil Supérieur du Pouvoir Judiciaire (CSPJ): document library, Cour de cassation d'Haïti: Constitution PDF (1987 original) |
| `hu` | [Hungary](https://ykarapazar.github.io/fontes/law/hu/) | Bírósági Határozatok Gyűjteménye | — |
| `icj` | [International Court of Justice (ICJ)](https://ykarapazar.github.io/fontes/law/icj/) | International Court of Justice website (www.icj-cij.org): case pages and document search | International Court of Justice website (www.icj-cij.org): case pages and document search |
| `icsid` | [ICSID (investment arbitration)](https://ykarapazar.github.io/fontes/law/icsid/) | ICSID case database | — |
| `id` | [Indonesia](https://ykarapazar.github.io/fontes/law/id/) | — | JDIH Kementerian Sekretariat Negara (jdih.setneg.go.id) – Produk Hukum, Majelis Permusyawaratan Rakyat (www.mpr.go.id) – UUD NRI 1945 |
| `ie` | [Ireland](https://ykarapazar.github.io/fontes/law/ie/) | — | Irish Statute Book, LRC Revised Acts |
| `il` | [Israel](https://ykarapazar.github.io/fontes/law/il/) | — | Knesset law database; Open Law Book (Wikisource, non-official) |
| `in` | [India](https://ykarapazar.github.io/fontes/law/in/) | Indian Supreme Court Judgments (AWS Open Data; Dattam Labs mirror of the Supreme Court's e-SCR) | Lexifina's record (not the official publisher) |
| `iq` | [Iraq](https://ykarapazar.github.io/fontes/law/iq/) | — | Kurdistan Parliament legislation database (قاعدة التشريعات), legislation.krd (Kurdistan Region of Iraq only) |
| `is` | [Iceland](https://ykarapazar.github.io/fontes/law/is/) | Ísland.is court rulings | — |
| `it` | [Italy](https://ykarapazar.github.io/fontes/law/it/) | — | Normattiva |
| `itlos` | [ITLOS (International Tribunal for the Law of the Sea)](https://ykarapazar.github.io/fontes/law/itlos/) | ITLOS case pages (www.itlos.org) | — |
| `jm` | [Jamaica](https://ykarapazar.github.io/fontes/law/jm/) | Find Case Law, The National Archives (UK): Judicial Committee of the Privy Council judgments, Supreme Court of Jamaica judgments (supremecourt.gov.jm), Court of Appeal of Jamaica judgments (courtofappeal.gov.jm) | — |
| `jo` | [Jordan](https://ykarapazar.github.io/fontes/law/jo/) | Constitutional Court of Jordan (المحكمة الدستورية), cco.gov.jo | — |
| `jp` | [Japan](https://ykarapazar.github.io/fontes/law/jp/) | — | e-Gov 法令API |
| `kg` | [Kyrgyzstan](https://ykarapazar.github.io/fontes/law/kg/) | Constitutional Court of the Kyrgyz Republic (constsot.kg) | — |
| `kh` | [Cambodia](https://ykarapazar.github.io/fontes/law/kh/) | — | Council for the Development of Cambodia (CDC): Laws and Regulations |
| `la` | [Laos](https://ykarapazar.github.io/fontes/law/la/) | — | Official Gazette of the Lao PDR (Ministry of Justice): search index (partial) |
| `lb` | [Lebanon](https://ykarapazar.github.io/fontes/law/lb/) | المجلس الدستوري / Constitutional Council of Lebanon (cc.gov.lb) | المجلس الدستوري / Constitutional Council of Lebanon (cc.gov.lb) |
| `li` | [Liechtenstein](https://ykarapazar.github.io/fontes/law/li/) | Fürstlicher Oberster Gerichtshof – Entscheidungen (www.ogh.li) | Lilex – Gesetzesdatenbank des Fürstentums Liechtenstein (Rechtsdienst der Regierung) |
| `lu` | [Luxembourg](https://ykarapazar.github.io/fontes/law/lu/) | data.public.lu — Cour de cassation decisions (Administration judiciaire), yearly ZIPs of PDFs read member by member with HTTP Range | Legilux |
| `lv` | [Latvia](https://ykarapazar.github.io/fontes/law/lv/) | E-lietas (anonymised decisions) | — |
| `ly` | [Libya](https://ykarapazar.github.io/fontes/law/ly/) | المحكمة العليا - Supreme Court of Libya (alolya.gov.ly) | وزارة العدل - Ministry of Justice of Libya (aladel.gov.ly) |
| `ma` | [Morocco](https://ykarapazar.github.io/fontes/law/ma/) | Constitutional Court of Morocco (cour-constitutionnelle.ma) – Decisions | Ministry of Justice legal portal Adala (adala.justice.gov.ma) |
| `mc` | [Monaco](https://ykarapazar.github.io/fontes/law/mc/) | Legimonaco — Gouvernement Princier de Monaco (Direction des Affaires Juridiques): Constitution, codes, laws, ordinances, treaties and court decisions | Legimonaco — Gouvernement Princier de Monaco (Direction des Affaires Juridiques): Constitution, codes, laws, ordinances, treaties and court decisions |
| `md` | [Moldova](https://ykarapazar.github.io/fontes/law/md/) | Curtea Supremă de Justiție (Supreme Court of Justice), jurisprudenta.csj.md, Portalul Național al Instanțelor de Judecată (courts of appeal and district courts), instante.justice.md | Președinția Republicii Moldova: Constituția (consolidated PDF), presedinte.md |
| `me` | [Montenegro](https://ykarapazar.github.io/fontes/law/me/) | Ustavni sud Crne Gore (ustavnisud.me) – Sudska arhiva | — |
| `mg` | [Madagascar](https://ykarapazar.github.io/fontes/law/mg/) | Haute Cour Constitutionnelle (hcc.gov.mg) | CNLegis – Centre National LEGIS, Primature (cnlegis.gov.mg) |
| `mm` | [Myanmar](https://ykarapazar.github.io/fontes/law/mm/) | Supreme Court of the Union: Rulings and Case Management System (rcms.usc.gov.mm) | Supreme Court of the Union: laws, procedures and amending laws (unionsupremecourt.gov.mm) |
| `mn` | [Mongolia](https://ykarapazar.github.io/fontes/law/mn/) | shuukh.mn, electronic database of court decisions (Judicial General Council of Mongolia) | — |
| `mt` | [Malta](https://ykarapazar.github.io/fontes/law/mt/) | — | Legislation Malta (legislation.mt), Office of the State Advocate / Legislation Unit |
| `mu` | [Mauritius](https://ykarapazar.github.io/fontes/law/mu/) | Find Case Law, The National Archives (UK): Judicial Committee of the Privy Council judgments, Supreme Court of Mauritius website (supremecourt.govmu.org): judgment search (subordinate courts) and legislation library (OFF) | Supreme Court of Mauritius website (supremecourt.govmu.org): judgment search (subordinate courts) and legislation library, Revised Laws of Mauritius, Attorney General's Office (attorneygeneral.govmu.org), National Assembly of Mauritius (mauritiusassembly.govmu.org): Acts as passed (OFF) |
| `mv` | [Maldives](https://ykarapazar.github.io/fontes/law/mv/) | — | MvLaw (mvlaw.gov.mv), Attorney General's Office legislation database, Government Gazette of the Maldives (gazette.gov.mv), President's Office |
| `mz` | [Mozambique](https://ykarapazar.github.io/fontes/law/mz/) | Tribunal Supremo (ts.gov.mz): judgments tables of the TS and the Tribunais Superiores de Recurso, and its legislation page, Conselho Constitucional (cconstitucional.org.mz): acórdãos and deliberações | Tribunal Supremo (ts.gov.mz): judgments tables of the TS and the Tribunais Superiores de Recurso, and its legislation page |
| `ng` | [Nigeria](https://ykarapazar.github.io/fontes/law/ng/) | Supreme Court of Nigeria | National Assembly of Nigeria (nass.gov.ng) – Acts as passed, Nigerian Investment Promotion Commission (nipc.gov.ng) – Acts, PLAC Laws of Nigeria (lawsofnigeria.placng.org): unrevised LFN 2004 (unofficial), FAOLEX (FAO) – Constitution of Nigeria 1999, consolidated to 2023 (PLAC print) |
| `nl` | [Netherlands](https://ykarapazar.github.io/fontes/law/nl/) | rechtspraak.nl | wetten.overheid.nl (BWB) |
| `no` | [Norway](https://ykarapazar.github.io/fontes/law/no/) | Supreme Court (official summaries only) | — |
| `np` | [Nepal](https://ykarapazar.github.io/fontes/law/np/) | Nepal Kanoon Patrika (नेपाल कानून पत्रिका), Supreme Court of Nepal | — |
| `pa` | [Panama](https://ykarapazar.github.io/fontes/law/pa/) | Legispan – Asamblea Nacional de Panamá (texts as published in the Gaceta Oficial, including Supreme Court rulings published there) | Legispan – Asamblea Nacional de Panamá (texts as published in the Gaceta Oficial, including Supreme Court rulings published there) |
| `pe` | [Peru](https://ykarapazar.github.io/fontes/law/pe/) | Tribunal Constitucional – Consulta de causas and published resolutions | El Peruano – Diario Oficial, Búsquedas (Editora Perú): norms as published, Congreso de la República – Constitución Política del Perú, edición oficial (consolidated) |
| `ph` | [Philippines](https://ykarapazar.github.io/fontes/law/ph/) | The LawPhil Project (lawphil.net), Arellano Law Foundation: non-official (NGO) | The LawPhil Project (lawphil.net), Arellano Law Foundation: non-official (NGO) |
| `pk` | [Pakistan](https://ykarapazar.github.io/fontes/law/pk/) | Islamabad High Court (mis.ihc.gov.pk) – Case Law System | The Pakistan Code (pakistancode.gov.pk), Ministry of Law and Justice |
| `pl` | [Poland](https://ykarapazar.github.io/fontes/law/pl/) | Portal Orzeczeń (common courts) | Sejm ELI API |
| `ps` | [Palestine](https://ykarapazar.github.io/fontes/law/ps/) | Maqam – موسوعة القوانين وأحكام المحاكم الفلسطينية (An-Najah National University, Faculty of Law) – non-official (academic) | Maqam – موسوعة القوانين وأحكام المحاكم الفلسطينية (An-Najah National University, Faculty of Law) – non-official (academic) |
| `pt` | [Portugal](https://ykarapazar.github.io/fontes/law/pt/) | DGSI, Tribunal Constitucional | PGDL (unofficial consolidations) |
| `py` | [Paraguay](https://ykarapazar.github.io/fontes/law/py/) | Corte Suprema de Justicia – Sistema de Información de Jurisprudencia | Biblioteca y Archivo Central del Congreso Nacional (BACN) – Leyes Paraguayas |
| `ro` | [Romania](https://ykarapazar.github.io/fontes/law/ro/) | ÎCCJ decision by id only (no search) | cdep.ro index search only (no text) |
| `rs` | [Serbia](https://ykarapazar.github.io/fontes/law/rs/) | Vrhovni sud (Supreme Court of Serbia): Baza sudske prakse | Ustavni sud (Constitutional Court): Ustav RS i propisi |
| `rw` | [Rwanda](https://ykarapazar.github.io/fontes/law/rw/) | Portal of Rwandan Laws and Case Laws (amategeko.gov.rw), Rwanda Law Reform Commission and Judiciary of Rwanda | Portal of Rwandan Laws and Case Laws (amategeko.gov.rw), Rwanda Law Reform Commission and Judiciary of Rwanda |
| `sc` | [Seychelles](https://ykarapazar.github.io/fontes/law/sc/) | Judiciary of Seychelles website (judiciary.sc): Decisions from the Courts | Official Gazette of Seychelles (gazette.sc): Acts, S.I.s and Bills, Judiciary of Seychelles website (judiciary.sc): Laws of Seychelles (Constitution and main codes) |
| `se` | [Sweden](https://ykarapazar.github.io/fontes/law/se/) | Rättspraxis (Domstolsverket) | Riksdagen (SFS) |
| `sg` | [Singapore](https://ykarapazar.github.io/fontes/law/sg/) | SG Courts judgments (OFF) | — |
| `si` | [Slovenia](https://ykarapazar.github.io/fontes/law/si/) | Sodna praksa | PISRS |
| `sk` | [Slovakia](https://ykarapazar.github.io/fontes/law/sk/) | Supreme Court | Slov-Lex |
| `sn` | [Senegal](https://ykarapazar.github.io/fontes/law/sn/) | Conseil constitutionnel du Sénégal (decisions and consolidated Constitution), JURICAF (AHJUCAF): Cour suprême decisions (unofficial) | Conseil constitutionnel du Sénégal (decisions and consolidated Constitution), Primature / Secrétariat général du Gouvernement (lois, décrets, codes), Ministère de la Justice du Sénégal (codes, lois and décrets as PDF) |
| `sr` | [Suriname](https://ykarapazar.github.io/fontes/law/sr/) | Rechtspraak Suriname, Hof van Justitie (rechtspraak.sr) | Surinaamse wetten, De Nationale Assemblee (dna.sr) |
| `tj` | [Tajikistan](https://ykarapazar.github.io/fontes/law/tj/) | Constitutional Court of the Republic of Tajikistan (constcourt.tj) | Constitutional Court of the Republic of Tajikistan (constcourt.tj), Official website of the President of the Republic of Tajikistan (president.tj), Базаи қонунгузории ҶТ, National Legislation Centre under the President of the Republic of Tajikistan (base.mmk.tj) |
| `tm` | [Turkmenistan](https://ykarapazar.github.io/fontes/law/tm/) | Supreme Court of Turkmenistan (court.gov.tm) | Mejlis of Turkmenistan (mejlis.gov.tm), Supreme Court of Turkmenistan (court.gov.tm) |
| `tr` | [Türkiye](https://ykarapazar.github.io/fontes/law/tr/) | Bedesten, Constitutional Court | Bedesten (mevzuat) |
| `tt` | [Trinidad and Tobago](https://ykarapazar.github.io/fontes/law/tt/) | Judiciary of Trinidad and Tobago: Recent Judgments (ttlawcourts.org) and judgment PDFs (webopac.ttlawcourts.org), Find Case Law, The National Archives | Digital Legislative Library, Law Revision Commission (laws.gov.tt) |
| `tw` | [Taiwan](https://ykarapazar.github.io/fontes/law/tw/) | Judicial Yuan (FJUD) | MOJ law texts by pcode (no search) |
| `untc` | [UN Treaty Collection (multilateral treaties deposited with the UN Secretary-General)](https://ykarapazar.github.io/fontes/law/untc/) | — | United Nations Treaty Collection (treaties.un.org), MTDSG status records and certified true copies |
| `us` | [United States (federal)](https://ykarapazar.github.io/fontes/law/us/) | govinfo | US Code (uscode.house.gov) |
| `us-states` | [United States (state courts)](https://ykarapazar.github.io/fontes/law/us-states/) | CourtListener (Free Law Project, a non-profit): opinions of state supreme and appellate courts | — |
| `uy` | [Uruguay](https://ykarapazar.github.io/fontes/law/uy/) | BJN (Poder Judicial) | IMPO |
| `uz` | [Uzbekistan](https://ykarapazar.github.io/fontes/law/uz/) | lex.uz, National Database of Legislation (Ministry of Justice, 'Adolat' National Legal Information Centre) | lex.uz, National Database of Legislation (Ministry of Justice, 'Adolat' National Legal Information Centre) |
| `vn` | [Vietnam](https://ykarapazar.github.io/fontes/law/vn/) | Tòa án nhân dân tối cao: Trang tin điện tử về án lệ (anle.toaan.gov.vn) | Bộ Tư pháp: Cơ sở dữ liệu quốc gia về văn bản pháp luật (vbpl.vn), Cổng Thông tin điện tử Chính phủ: Hệ thống văn bản (vanban.chinhphu.vn) |
| `wto` | [WTO dispute settlement (World Trade Organization)](https://ykarapazar.github.io/fontes/law/wto/) | WTO dispute pages and dispute data files (www.wto.org) | — |
| `xk` | [Kosovo](https://ykarapazar.github.io/fontes/law/xk/) | Gjykata Kushtetuese e Republikës së Kosovës (Constitutional Court), gjk-ks.org | Gazeta Zyrtare e Republikës së Kosovës (Official Gazette, Office of the Prime Minister), gzk.rks-gov.net |
<!-- coverage:end -->

</details>

OFF = the source's terms need the operator's permission, so it is off by default. Set
`WLM_PERMITTED=<code>` only once you have that permission (see the sources table).

`list_jurisdictions` gives each one's exact coverage and gaps.

## Tools

| Tool | What it does |
|---|---|
| `list_jurisdictions(query?)` | Codes, names, sources, supported tools and each jurisdiction's extra filters. Call first. |
| `search_caselaw(jurisdiction, query, limit=10, page=1, filters={})` | Full-text search of court decisions. |
| `get_decision(jurisdiction, id, max_chars=60000, offset=0)` | One decision as markdown (nl: ECLI; gb: neutral citation or slug). |
| `search_legislation(jurisdiction, query, limit=20, page=1, filters={})` | Find laws / acts / instruments. |
| `get_legislation_toc(jurisdiction, id, keyword?)` | Structure of a law, with provision labels. |
| `get_legislation_provision(jurisdiction, id, provision)` | One article / section / regulation. |
| `get_legislation_text(jurisdiction, id, max_chars=60000, offset=0)` | Full consolidated text, pageable. |
| `get_law_on_date(provision, date="today", jurisdiction?)` | A provision's text as in force on a date (past dates too), with the law that last changed it. Takes a citation such as "Art. 1 GG" or a path. From Lexifina's record (not the official publisher). |
| `get_law_history(provision, jurisdiction?, date_a?, date_b?)` | Every law that changed a provision, or the word-by-word change between two dates. From Lexifina's record (not the official publisher). |
| `report_bug(note?)` | Prepares a bug report about Fontes. You see it first; it is sent only if you confirm. See [docs/PRIVACY.md](docs/PRIVACY.md). |

Filters per jurisdiction (unknown filter names are rejected with the list of valid ones):

- `nl` case law: `field` (alle/tekst/samenvatting/ecli/zaaknummer/vindplaats), `sort`
  (relevantie/publicatie/uitspraak/uitspraak_asc), `period` (week/maand/dit_jaar/vorig_jaar).
  Legislation: `current_only` (default true).
- `gb` case law: `court` (e.g. `uksc,ewca/civ`), `party`, `judge`, `order` (`-date`/`date`/`-updated`/`updated`).
  Legislation: `search_in` (`title`/`text`), `doc_type` (`ukpga`, `uksi`, ...), `year`.

## Install

Step-by-step for each app (Claude Desktop, Codex, Claude Code, Cursor, VS Code, Gemini CLI,
Zed, LM Studio, Cline): [docs/INSTALL.md](docs/INSTALL.md).

**Developers:** you need [uv](https://docs.astral.sh/uv/getting-started/installation/).

```bash
uvx fontes-mcp                 # from PyPI
uvx --from git+https://github.com/ykarapazar/fontes fontes   # straight from GitHub
uvx fontes-mcp --only nl,gb    # expose only some jurisdictions
```

Fontes is a stdio MCP server: an MCP client starts it, you don't run it by hand.
`nl-legal-mcp` and `uk-legal-mcp` (older names) are aliases for `fontes --only nl` / `--only gb`.

<details>
<summary>Optional environment variables</summary>

Optional environment variables: `WLM_US_GOVINFO_KEY` (free api.data.gov key for US case-law
search), `WLM_US_COURTLISTENER_KEY` (your own free CourtListener token: US state case law,
off without it), `WLM_FR_PISTE_CLIENT_ID` + `WLM_FR_PISTE_CLIENT_SECRET` (France is off without
them: free piste.gouv.fr app subscribed to Judilibre and Légifrance, steps in `research/fr.md`),
`WLM_PERMITTED=<codes>` (turn on sources whose terms need permission, only once you
have it), `FONTES_NO_UPDATE_CHECK=1`, `WLM_LEXIFINA=0` (turn off Lexifina's record: `get_law_on_date`,
`get_law_history` and the 91 countries read through it).

</details>

Most apps take the same entry; the file and the top-level key differ per app (see
[docs/INSTALL.md](docs/INSTALL.md#other-apps)):

```json
{
  "mcpServers": {
    "fontes": {
      "command": "uvx",
      "args": ["fontes-mcp"]
    }
  }
}
```

### Check that it works

Ask your AI app: *"Which jurisdictions can Fontes search?"* It should list the countries.

### From a checkout (development)

```bash
git clone https://github.com/ykarapazar/fontes && cd fontes
uv sync && uv run fontes --help
```

## Tests

```bash
uv run pytest -q                 # offline registry tests + live smoke tests (needs network)
uv run pytest tests/live/test_nl.py tests/live/test_conformance.py -k "test_nl or [nl]"  # one jurisdiction, live
uv run pytest tests/test_registry.py
```

## Adding a jurisdiction

The full contract is [docs/ADAPTER_SPEC.md](docs/ADAPTER_SPEC.md); read it with `base.py` and
`models.py`. In short:

<details>
<summary>Steps and rules</summary>

1. Pick the code: ISO 3166-1 alpha-2 lower-case (`de`), sub-national `us-ca`, international
   `eu`, `echr`. Create `src/world_legal_mcp/jurisdictions/<code>.py` (use a valid module
   name, e.g. `us_ca.py` with `code = "us-ca"`). It is discovered automatically.
2. Subclass `Jurisdiction` and set `code`, `name`, `languages`, `aliases`, `notes`, `samples`,
   `min_interval = {host: seconds}` and `sources`: for each `Source` its licence,
   `commercial_use`, `ai_use`, `auth`, `rate_limit` (and how you know it) and `terms_url`.
3. Implement only the async methods the official source supports (`search_caselaw`,
   `get_decision`, `search_legislation`, `get_legislation_toc`, `get_legislation_provision`,
   `get_legislation_text`). Return the records from `models.py`, not markdown; raise
   `NotFound` / `BadRequest` / `SourceError` on failure. Missing methods are reported as
   unsupported.
4. Declare extra search options in `caselaw_filters` / `legislation_filters` and read them
   from `filters`. Use `_http.get/post` (the project's own User-Agent, per-host throttle) and
   the shared `_http` helpers.
5. Add `tests/live/test_<code>.py` and run
   `uv run pytest tests/test_registry.py -q` and
   `uv run pytest tests/live/test_conformance.py -k "[<code>]" -s` (with brackets: a plain
   `-k <code>` matches other tests too).

Rules: official or public-body sources only; never scrape what robots.txt or the terms
forbid; identifiers come from the source and are never invented. A source whose terms need
permission for automated use gets `needs_permission=True` and a `warning`: the server never
calls it unless the operator lists the code in `WLM_PERMITTED` (e.g. `WLM_PERMITTED=in,de`).

</details>

## Sources, terms and robots.txt

Every request names this project in its User-Agent
(`Fontes/<version> (+https://github.com/ykarapazar/fontes; fontesmcp@proton.me)`); it never
poses as a browser. Requests are
made one at a time when a user asks something, not by crawling. If you self-host, you are
the operator each source sees, so check the column on the right before you deploy.
Checked 2026-11-05/06.

**If you run one of these sources** and we got something wrong (your terms, your robots.txt,
your rate limits, or anything else), email fontesmcp@proton.me. We will fix it or switch the
source off.

"AI use" is whether the source's terms or robots.txt say anything against AI/TDM use
("not stated" means silent, not permitted). Rate limits marked "documented" come from the
source; everything else is our own spacing. `list_jurisdictions` returns the same data.

<details>
<summary>Sources table (licence, commercial use, AI use, auth, rate limit, robots.txt)</summary>

<!-- sources:start -->
| Country | Source (host we call) | Licence | Commercial | AI use | Auth | Rate limit | robots.txt and what a self-hoster should know |
|---|---|---|---|---|---|---|---|
| ad | Tribunal Constitucional del Principat d'Andorra: sentències and autes (www.tribunalconstitucional.ad) | Unknown: the legal notice names the court as owner, says 'Tots els drets reservats' and is silent on reuse or automated access (checked 2026-11-06) | Unknown | Not stated | None | Unknown, nothing documented; 1 s spacing, no 429 seen in ~10 requests (2026-11). robots.txt: Drupal default, no Crawl-delay (2026-11-06) |  |
| ad | Portal Jurídic del Principat d'Andorra (BOPA service, Govern d'Andorra / Consell General): consolidated laws and Government regulations (portaljuridicandorra.ad) | Govern d'Andorra legal notice: all rights reserved; only personal use of downloadable files is authorised, commercial use not permitted | **No** | Not stated | None | Robots.txt Crawl-Delay: 10 (checked 2026-11-06); 10 s spacing | Personal use only: Portal Jurídic terms allow personal use only, no commercial use; consolidated texts are unofficial (the BOPA is the only authentic version). |
| ad | Consell General del Principat d'Andorra: Constitució (Catalan booklet PDF) (www.consellgeneral.ad) | Unknown: consellgeneral.ad has no legal notice or terms page (checked 2026-11-10); the Constitution is an official text | Unknown | Not stated | None | Unknown, nothing documented; 1 s spacing; one ~450 KB PDF, kept in a small in-memory cache; no 429 seen in ~10 requests (2026-11) |  |
| af | Ministry of Justice laws database (de facto authority) (laws.moj.gov.af) | Unknown; no terms or licence page, footer 'Copyright © 2019 \| MOJ. All Rights Reserved' | Unknown | Not stated | None | Unknown; 2 s spacing, no 429 seen in ~30 requests (2026-11) | Site of the Ministry of Justice of the current de facto administration (Islamic Emirate); texts and in-force status reflect that administration. PDFs as published in the Official Gazette, not consolidated; text extracted from PDF, check the original. |
| afchpr | AJUDATA, the African Court's case database (ajudata.african-court.org) | © African Court on Human and Peoples' Rights, "All Rights Reserved" (site footer); no terms-of-use page and no clause on automated access | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~25 requests (2026-11); page size fixed at 50 by the source |  |
| afchpr | African Union treaty page: African Charter on Human and Peoples' Rights and the Court's Protocol (au.int) | Not researched; link only, nothing is fetched from it | Unknown | Not stated | None | Unknown |  |
| afchpr | African Court website (Rules of Court) (www.african-court.org) | Not researched; link only, nothing is fetched from it | Unknown | Not stated | None | Unknown |  |
| al | Qendra e Botimeve Zyrtare (qbz.gov.al, Ministry of Justice) | Not stated. FAQ: published information is accessible to the general public without any restriction | Unknown | Not stated | None | Not published; 1 request/s self-imposed, no 429 seen in a handful of requests (2026-11-05) |  |
| al | Gjykata e Lartë (High Court of Albania, gjykataelarte.gov.al) | Not stated. Terms: the website is free to use and available to all users; only unlawful use is forbidden | Unknown | Not stated | None | API sends x-ratelimit-limit: 50 (window not stated); 1.5 s between requests self-imposed |  |
| am | ARLIS, Armenian Legal Information System (unified official publication website; Ministry of Justice / Official Bulletin CJSC) (www.arlis.am) | No licence or terms published (footer: '© All rights reserved'); the texts are official documents, which Copyright Law HO-142-N art. 4(1)(c) excludes from copyright | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~25 requests (2026-11) |  |
| ar | InfoLEG (www.argentina.gob.ar/normativa, Ministerio de Justicia) | Creative Commons Reconocimiento 2.5 Argentina (infoleg.gob.ar footer) | Unknown | Not stated | None | Unknown; no robots.txt (404); 2 s spacing, no 429 seen in ~10 requests (2026-11) | Credit "InfoLEG – Ministerio de Justicia de la Nación". Consolidated texts are not official (only the Boletín Oficial is). **No case law: SAIJ's terms allow personal use only, so it is not used.** |
| ar | InfoLEG – Leyes Argentinas (Ministerio de Justicia, argentina.gob.ar/normativa) | Creative Commons Attribution 4.0 International (argentina.gob.ar Términos y condiciones) | Yes | Not stated | None | Robots.txt Crawl-delay: 10 (checked 2026-11-05); 10 s spacing | CC BY 4.0: credit 'InfoLEG – Ministerio de Justicia de la Nación' when reusing. Consolidated texts are not official; only the Boletín Oficial is authentic. |
| at | RIS — Rechtsinformationssystem des Bundes (OGD API v2.6) (data.bka.gv.at) | CC BY 4.0 (stated in the RIS OGD FAQ at data.bka.gv.at/ris/api/v2.6/) | Yes | Not stated | None | Documented: max 0.5 req/s (2 s gap), no parallel connections; anything beyond manual-scale use must be announced to ris.it@bka.gv.at and run 20:00–05:00 or weekends (RIS OGD FAQ, read 2026-11-05). Using 2 s spacing. | robots.txt `Disallow: /` for all clients; officially documented open-data API, read as a template rule (unconfirmed). **Anything beyond manual-scale use must be announced to ris.it@bka.gv.at** and run 20:00–05:00 or weekends. |
| au | Federal Register of Legislation (api.prod.legislation.gov.au) | CC BY 4.0 (attribute to the Federal Register of Legislation and link legislation.gov.au; Coat of Arms and third-party material excluded) | Yes | Yes | None | Unknown (none published; API is the site's own backend); 1 s spacing, no 429 seen in ~30 requests (2026-11-05) | Undocumented site backend. www robots.txt: Crawl-delay 10; API host has none. |
| az | e-qanun.az, Unified Electronic Database of Legal Acts (Ministry of Justice) | Unknown: no terms page; footer says 'Bütün Haqqlar Qorunur' (All Rights Reserved). Official texts are excluded from copyright under the Azerbaijani Copyright Law (art. 7; unverified) | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~80 requests (2026-11) | e-qanun.az serves its text files only with an e-qanun.az Referer header (hotlink protection); this adapter sends one. Off until the operator decides that is acceptable. **Off by default — needs WLM_PERMITTED=az and the operator's permission.** |
| ba | Ustavni sud Bosne i Hercegovine (ustavnisud.ba) – decisions database | Unknown: no terms of use on the site (footer 'Copyrights @ 2026 Ustavni sud BiH Sva prava zadržana.'); official court decisions | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~25 requests (2026-11) |  |
| ba | Vlada Federacije BiH (fbihvlada.gov.ba) – Hronološki registar zakona (Federation laws as published) | Unknown: no terms of use on the site (footer 'Copyright 2021. Vlada Federacije Bosne i Hercegovine'); official legislative texts | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~20 requests (2026-11) | Federation of BiH entity laws only, as published in Službene novine FBiH (not consolidated; state, Republika Srpska and Brčko laws are not covered). |
| ba | Parlamentarna skupština BiH (parlament.ba) – Ustav BiH and Prečišćeni tekstovi zakona (state level) | Unknown: no terms of use found on the site; official Parliament publication. The consolidated texts are the Parliament's UNOFFICIAL consolidations (Neslužbeni prečišćeni tekst); only the Službeni glasnik BiH text is authentic | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~25 requests (2026-11) | State-level acts: the Constitution (with Amandman I) and the Parliament's unofficial consolidated texts, a selection of state acts (not every act); the authentic text is in Službeni glasnik BiH. |
| bb | Barbados Judicial System: judgments (barbadoslawcourts.gov.bb) | 'Copyright Barbados Judicial System 2015 - 2026. All Rights Reserved.' No licence; the 'Terms & Conditions' footer link is empty (no terms page, checked 2026-11-05); silent on reuse and automated access | Unknown | Not stated | None | Robots.txt Crawl-delay: 10 (honoured: 10 s spacing); no 429 in ~12 requests (2026-11) |  |
| bb | Barbados Judicial System: Consolidated Laws (barbadoslawcourts.gov.bb) | 'Copyright Barbados Judicial System 2015 - 2026. All Rights Reserved.' No licence; the 'Terms & Conditions' footer link is empty (no terms page, checked 2026-11-05); silent on reuse and automated access | Unknown | Not stated | None | Robots.txt Crawl-delay: 10 (honoured: 10 s spacing; law lists cached in memory 6 h) | Laws are OCR text of scanned printed revised editions (1971 / L.R.O. 1985 and later reprints): may predate amendments and contain OCR errors; check the PDF. |
| bb | CCJ judgment lists and PDFs (ccj.org) | © Caribbean Court of Justice; no licence stated (the Terms of Use page is empty, 2026-11-05) | Unknown | Not stated | None | Unknown; 1 s spacing, both lists cached in memory 6 h; no 429 seen in ~20 requests (2026-11) |  |
| bd | Laws of Bangladesh (bdlaws.minlaw.gov.bd), Legislative and Parliamentary Affairs Division | Unknown: no terms of use or licence; page footer 'Copyright © 2019, Legislative and Parliamentary Affairs Division' | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~20 requests (2026-11) |  |
| bd | Supreme Court of Bangladesh (supremecourt.gov.bd) – Judgments and Orders | Unknown: no terms of use, copyright or licence statement on the site | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~10 requests (2026-11) |  |
| bg | Конституционен съд (Constitutional Court), constcourt.bg | No licence or terms page; footer says 'съдържанието е обект на авторско право' (content is copyrighted), but official acts of state bodies are excluded from copyright (ЗАПСП art. 4 item 1) | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 in ~20 requests (2026-11-06); Cloudflare-fronted |  |
| bg | Народно събрание (National Assembly), parliament.bg API: Constitution and laws as adopted | No terms page; laws are excluded from copyright (ЗАПСП art. 4 item 1) | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 in ~40 requests (2026-11-06, -10) |  |
| bh | Legislation and Legal Opinion Commission (هيئة التشريع والرأي القانوني), lloc.gov.bh | Site terms: content is copyright LLOC; modifying it or using it 'for any other purposes' is called an infringement. Separately, Bahraini copyright law (22/2006 art. 4(b)) excludes legislation and judgments from copyright, but that does not lift the site's terms on automated use: reuse still needs LLOC's permission. | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~40 requests (2026-11) | LLOC's terms reserve copyright and forbid modifying content or using it 'for other purposes'; texts are passed on unmodified for reference. Check the official PDF before relying on them. Even with permission this source holds legislation and Constitutional Court judgments only, not Court of Cassation judgments. **Off by default — needs WLM_PERMITTED=bh and the operator's permission.** |
| bj | Cour constitutionnelle du Bénin: décisions (courconstitutionnelle.bj) | No terms published; footer '© Cour Constitutionnelle du Bénin - 2023' | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~20 requests (2026-11) |  |
| bj | Secrétariat général du Gouvernement du Bénin: lois, décrets, ordonnances (sgg.gouv.bj) | No terms (mentions légales page is empty); footer '© Présidence de la République du Bénin - 2026' | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~20 requests (2026-11) | Texts as promulgated, not consolidated; many recent PDFs are image-only scans with no extractable text. |
| bo | Tribunal Agroambiental – Buscador de Resoluciones (SISAGRO consultas) (arbol.tribunalagroambiental.bo) | Unknown: no terms-of-use or licence page on tribunalagroambiental.bo (checked 2026-11-06); court resolutions are official texts | Unknown | Not stated | None | Unknown; robots.txt allows all, no crawl-delay (2026-11-06); 1 s spacing, no 429 seen in ~10 requests |  |
| bo | Cámara de Diputados – Leyes Promulgadas (WP REST API), laws as promulgated (diputados.gob.bo) | Unknown: no terms-of-use page; site footer says '©2025. Cámara de Diputados. Todo los derechos reservados.' (checked 2026-11-06); laws are official texts | Unknown | Not stated | None | Unknown; robots.txt is 404 (no rules, 2026-11-06); 1 s spacing, no 429 seen in ~15 requests | Bolivian law texts here are the laws as promulgated (PDF, partly OCR'd by the source), not consolidated: check later amending laws. |
| bo | LexiVox – Bolivian legislation (constitution, laws, decree-laws, codes; unofficial) (www.lexivox.org) | GFDL / CC BY-SA 3.0: lexivox.org/terminos.html lets reusers copy, modify and redistribute the content with attribution (link to the source URL); each norm page says 'Derechos GFDL' (checked 2026-11-10). Run by DeveNet S.R.L., La Paz | Yes | Not stated | None | Unknown; robots.txt is 404 and pages carry meta robots ALL (2026-11-10); 1 s spacing, no 429 seen in ~15 requests | LexiVox is a private, unofficial compilation of Bolivian norms as published (texts transcribed from the Gaceta Oficial, not consolidated, no legal authority): check the Gaceta Oficial and later amending laws. |
| br | STF – Pesquisa de Jurisprudência (Supremo Tribunal Federal) (jurisprudencia.stf.jus.br) | Unknown: no STF terms of use found; judicial decisions are excluded from copyright under Lei 9.610/1998 art. 8, IV | Unknown | Not stated | None | Unknown: nothing published; jurisprudencia.stf.jus.br has no robots.txt (the SPA answers every path); 1 s spacing, no 429 seen in ~15 requests (2026-11-05). Undocumented internal API: may change without notice. | No robots.txt. Undocumented internal API; may change without notice. |
| br | normas.leg.br (Senado Federal / Câmara dos Deputados) – consolidated federal legislation | CC BY 4.0 (declared in every record's license/sdLicense); Senado portal policy: reuse allowed for lawful purposes with attribution | Yes | Not stated | None | Unknown: nothing published; normas.leg.br robots.txt allows all; legis.senado.leg.br robots.txt answers 403 (no rules readable). 1 s spacing, no 429 seen in ~20 requests (2026-11-05) | robots.txt allows all (legis.senado.leg.br's answers 403). |
| bs | Find Case Law, The National Archives (UK): Judicial Committee of the Privy Council judgments (caselaw.nationalarchives.gov.uk) | Open Justice Licence v2.0: free re-use incl. commercial; 'computational analysis' (programmatic bulk searching to identify, extract or enrich records) needs a separate, free licence | Yes | **No** | None | Documented: 1,000 requests / rolling 5 min per IP, HTTP 429 when exceeded (API docs, checked 2026-11) |  |
| bs | Statute Law of The Bahamas, Law Reform and Revision Commission (laws.bahamas.gov.bs) | Government of The Bahamas Copyright: 'Any reproduction shall ensure its accuracy, and the source and copyright status of the material is made evident to users. The website may only be used for informational non-commercial purposes' | **No** | Not stated | None | Unknown; no Crawl-delay; 1 s spacing, index and letter lists cached in memory 6 h; no 429 in ~15 requests (2026-11) | Statute Law of The Bahamas: Government copyright, informational non-commercial use only; not the authoritative text (that is the printed Revised Edition and the Official Gazette). |
| bs | Court of Appeal of The Bahamas judgments (courtofappeal.org.bs) | © Court of Appeal of the Commonwealth of The Bahamas, all rights reserved; no licence or terms of use; the site's only policy page is a privacy/data policy (read 2026-11-05) | Unknown | Not stated | None | Unknown; no Crawl-delay; 1 s spacing, no 429 in ~10 requests (2026-11) |  |
| bs | Supreme Court of The Bahamas judgments, The Judiciary of The Bahamas (courts.bs) | © The Judiciary of The Bahamas; no licence or terms of use; the site's only policy page is a privacy/data policy (read 2026-11-05) | Unknown | Not stated | None | Unknown; no robots.txt; 1 s spacing, the one-page judgment list (~1.2 MB) cached in memory 6 h; no 429 in ~10 requests (2026-11) |  |
| bt | Depository of Laws (legislation.gov.bt), Office of the Attorney General of Bhutan | None stated (no terms, licence or copyright notice on the site, 2026-11) | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~25 requests (2026-11) |  |
| bz | Judgments of the Senior Courts of Belize, Belize Judiciary (belizejudiciary.org) | '© 2024 Belize Supreme Court Judiciary' footer; no licence or terms-of-use page (checked 2026-11-06) | Unknown | Not stated | None | Unknown; no robots.txt, no Crawl-delay; 1 s spacing, no 429 in ~25 requests (2026-11) |  |
| bz | Laws of Belize, Attorney General's Ministry (agm.gov.bz) | '© 2022 By The Attorney General's Ministry of Belize - All Rights Reserved' footer; no terms-of-use page (checked 2026-11-06) | Unknown | Not stated | None | Unknown; no robots.txt, no Crawl-delay; 1 s spacing, no 429 in ~25 requests (2026-11) |  |
| bz | CCJ judgment lists and PDFs (ccj.org) | © Caribbean Court of Justice; no licence stated (the Terms of Use page is empty, 2026-11-05) | Unknown | Not stated | None | Unknown; 1 s spacing, both lists cached in memory 6 h; no 429 seen in ~20 requests (2026-11) |  |
| bz | Find Case Law, The National Archives (caselaw.nationalarchives.gov.uk) | Open Justice Licence v2.0: free re-use incl. commercial; 'computational analysis' (programmatic bulk searching to identify, extract or enrich records) needs a separate, free licence | Yes | **No** | None | Documented: 1,000 requests / rolling 5 min per IP, HTTP 429 when exceeded (API docs, checked 2026-11) |  |
| ca | Supreme Court of Canada judgments (decisions.scc-csc.ca, hosted by Lexum for the Court) | Reasons for judgment: Reproduction of Federal Law Order (SI/97-5), free reproduction incl. commercial if accurate and not presented as official. Headnotes and editorial features (paragraph numbers, lists of authorities): commercial reproduction needs the Court's written permission | Reasons: yes. Headnotes/editorial features: written permission | Yes | None | Unknown; 1 s spacing, no 429 seen (2026-11) | robots.txt blocks only one crawler (BUbiNG). |
| ca | Justice Laws Website, Department of Justice Canada (laws-lois.justice.gc.ca) | Open Government Licence – Canada (open.canada.ca XML dataset); also Reproduction of Federal Law Order (not to be presented as official) | Yes | Yes | None | Unknown; 1 s spacing, no 429 seen (2026-11) | No robots.txt. Must not be presented as the official version. |
| ccj | CCJ judgment lists and PDFs (ccj.org) | © Caribbean Court of Justice; no licence stated (the Terms of Use page is empty, 2026-11-05) | Unknown | Not stated | None | Unknown; 1 s spacing, both lists cached in memory 6 h; no 429 seen in ~20 requests (2026-11) |  |
| ch | Federal Supreme Court (search.bger.ch) | Unknown: no reuse terms published; the site footer says '© Alle Rechte vorbehalten', but court decisions are not copyright-protected in Switzerland (Art. 5(1)(c) URG, SR 231.1) | Unknown | Not stated | None | Robots.txt Crawl-delay: 2 (read 2026-11-05); using 2 s spacing, no 429 seen in a handful of requests (2026-11) |  |
| ch | Fedlex (fedlex.data.admin.ch SPARQL + www.fedlex.admin.ch/filestore) | Not copyright-protected (Art. 5 URG); free reuse under Art. 49 PublV (SR 170.512.1): text unchanged, kept apart from comments, with the notice 'Dies ist keine amtliche Veröffentlichung...'; paid redistribution only in value-added form | Yes | Not stated | None | Unknown, nothing documented; 1 s spacing on both hosts, no 429 seen (2026-11). fedlex.data.admin.ch robots.txt disallows /filestore/*, so files are read from www.fedlex.admin.ch/filestore (allowed) | **fedlex.data.admin.ch robots.txt disallows `/filestore/*`**; we fetch the same files from the www host, whose robots.txt allows them (what the Fedlex viewer itself loads). Defensible, not confirmed with Fedlex. |
| ci | Cour de cassation de Côte d'Ivoire: jurisprudence (eservices / sigcc) (eservices.courdecassation.ci) | No terms published; footer '© Copyright 2026. Tous Droits Réservés' | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~25 requests (2026-11) |  |
| ci | Assemblée nationale de Côte d'Ivoire: lois (assnat.ci) | No terms published; footer 'Copyright ©2019 assnat.ci - Tous droits réservés' | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~25 requests (2026-11) | Texts as adopted by the Assemblée nationale (not consolidated, mostly 2012-2020); the Journal officiel is the authentic version. |
| cl | BCN Ley Chile (www.leychile.cl, nuevo.leychile.cl) | Legal texts are excluded from copyright (Ley 17.336 art. 11 b); bcn.cl portal metadata declares CC BY-SA 3.0 CL; no Ley Chile terms page found | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~15 requests (2026-11-05); no robots.txt on leychile.cl / bcn.cl | No robots.txt. No Ley Chile terms page found. |
| cm | Cour suprême du Cameroun (coursupreme.cm) | 'Copyright © 2019 CSC. All Rights Reserved' (site footer); no terms of use or licence page (checked 2026-11-06) | Unknown | Not stated | None | Unknown; robots.txt 404 (no rules, no Crawl-delay); 1 s spacing, no 429 in ~15 requests (2026-11) |  |
| cm | Présidence de la République du Cameroun (prc.cm), Actes: lois, ordonnances, décrets | 'Copyright © 2026 Présidence de la République du Cameroun - Tous droits réservés' (site footer); the 'Règles de confidentialité' page is empty; no terms of use (checked 2026-11-06) | Unknown | Not stated | None | Unknown; robots.txt (Joomla default) only disallows system folders, no Crawl-delay; 1 s spacing, no 429 in ~30 requests (2026-11) |  |
| cn | Supreme People's Court of the PRC (最高人民法院), guiding cases (指导性案例) (www.court.gov.cn) | None published; site footer: 中华人民共和国最高人民法院 版权所有 (all rights reserved) | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~80 requests (2026-11-05) | No robots.txt. **No legislation: flk.npc.gov.cn robots.txt forbids all automated access.** China Judgments Online needs a login and is not used. |
| co | Corte Constitucional – relatoría (sentencias, full text) (www.corteconstitucional.gov.co) | Unknown: no terms or licence page found on corteconstitucional.gov.co (2026-11-05) | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~20 requests (2026-11-05); robots.txt explicitly allows /relatoria/, disallows /API/ and /sentencias/ | robots.txt allows /relatoria/ (full texts), disallows /API/ and /sentencias/. |
| co | datos.gov.co dataset of Corte Constitucional sentencias (Socrata) | Creative Commons Attribution-ShareAlike 4.0 (dataset metadata); attribution: Corte Constitucional | Yes | Not stated | None | Robots.txt Crawl-delay: 1; Socrata API without app token is throttled per IP (undocumented amount); no 429 seen in ~15 requests (2026-11-05) | Search matches metadata (number, magistrate, process), not judgment text. Dataset updated monthly. |
| co | Función Pública – Gestor Normativo (consolidated legislation) (www.funcionpublica.gov.co) | No open licence: terms say the content 'podrá ser utilizada teniendo en cuenta las normas que protegen el derecho a la propiedad intelectual' and forbid automated capture/copying without written consent (checked 2026-11-06) | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~25 requests (2026-11-06); robots.txt 'Disallow:' (allows all). TLS chain incomplete: the missing intermediate is bundled (intermediates.pem) for Linux | Función Pública's terms forbid using 'ningún mecanismo o hardware u otro proceso manual o automático para capturar, monitorizar como propio o copiar' the portal or its content without its written consent. No consent held. The Gestor also says it is informative only and does not vouch for a norm's current validity (vigencia). **Off by default — needs WLM_PERMITTED=co and the operator's permission.** |
| cr | SINALEVI – Sistema Nacional de Legislación Vigente (Procuraduría General de la República, SCIJ) (sinalevi.go.cr) | Unknown: no licence or terms page; footer says '© Procuraduría de la República. Todos los derechos reservados.' (2026-11-06) | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~25 requests (2026-11-06); no robots.txt (404) on sinalevi.go.cr or pgrweb.go.cr |  |
| cu | Gaceta Oficial de la República de Cuba (gacetaoficial.gob.cu) | Unknown; footer says 'Todos los Derechos Reservados \| © DESOFT 2019', no licence or terms page | Unknown | Not stated | None | Robots.txt Crawl-delay: 10 (obeyed, 10 s spacing). Host often times out on connect from abroad (unreachable 2026-11-06, reachable 2026-11-10) |  |
| cu | Ministerio de Justicia de Cuba (Gaceta Oficial reposts) (www.minjus.gob.cu) | Unknown; site says 'Todos los derechos reservados', no licence or terms page | Unknown | Not stated | None | Unknown; 2 s spacing, no 429 seen in ~25 requests (2026-11). Host often times out on connect (Cuban network) |  |
| cv | Tribunal Constitucional de Cabo Verde (tribunalconstitucional.cv) | 'Copyright © 2026 . Todos os direitos Reservados \| Tribunal Constitucional de Cabo Verde' footer; no terms-of-use page (checked 2026-11-06) | Unknown | Not stated | None | Unknown; no robots.txt, no Crawl-delay; 1 s spacing, no 429 in ~40 requests (2026-11) |  |
| cv | Supremo Tribunal de Justiça de Cabo Verde, jurisprudência (stj.cv) | '© 2023 Supremo Tribunal de Justiça, All Rights Reserved' footer; no terms-of-use page (checked 2026-11-06) | Unknown | Not stated | None | Unknown; no robots.txt, no Crawl-delay; 1 s spacing, no 429 in ~10 requests (2026-11) |  |
| cv | JURIS CV – Jurisprudência Cabo-verdiana (Conselho Superior da Magistratura Judicial) (jurisprudencia.cv) | /advertencia: 'As informações que constam deste sítio são públicas e podem ser reproduzidas, desde que a respectiva fonte seja mencionada. No entanto, é proibida a sua utilização para fins comerciais ou ofensivos.' (checked 2026-11-10) | **No** | Not stated | None (login optional, not used) | Robots.txt Crawl-delay: 10 (documented); 10 s spacing, no 429 in ~12 requests (2026-11-10) | JURIS CV: reproduction allowed with the source named (jurisprudencia.cv, CSMJ); commercial use is forbidden by its terms. |
| cz | rozhodnuti.justice.cz (Ministry of Justice) | Unknown: published as open data by the Ministry of Justice (rozhodnuti.justice.cz/opendata), no licence stated; not in the NKOD catalogue | Unknown | Not stated | None | Unknown, none documented; no 429 in ~30 requests (2026-11); using 1 s spacing | No robots.txt. Lower courts only, from 2020. |
| cz | e-Sbírka (Ministry of the Interior) (e-sbirka.gov.cz) | NKOD terms for the e-Sbírka open data: no copyrighted works, no database rights, no personal data (CC0-equivalent); legal texts are exempt under § 3 of the Czech Copyright Act. The /sbr-cache REST API itself is undocumented | Yes | Not stated | None | Unknown, none documented; no 429 in ~40 requests (2026-11); using 1 s spacing | No robots.txt. The REST backend is undocumented. |
| cz | Sbírka soudních rozhodnutí a stanovisek (Nejvyšší soud), sbirka.nsoud.cz | No terms page; court decisions are official works exempt from copyright (§ 3 Czech Copyright Act 121/2000) | Unknown | Not stated | None | None documented; robots.txt 'User-agent: * Disallow:' (allows all); no 429 in ~15 requests (2026-11-10); using 1 s spacing |  |
| cz | Vyhledávač NSS (Nejvyšší správní soud), vyhledavac.nssoud.cz | No terms page; court decisions are official works exempt from copyright (§ 3 Czech Copyright Act 121/2000) | Unknown | Not stated | None | None documented; robots.txt 404 (www.nssoud.cz robots asks Crawl-Delay 10, not binding here); using 2 s spacing |  |
| de | NeuRIS (testphase.rechtsinformationen.bund.de) | No licence stated; court decisions are public-domain official works (§ 5 UrhG) | Unknown | Not stated | None | Documented: 600 req/min per IP, 503 above (docs.rechtsinformationen.bund.de/guides/rate-limiting, 2026-11-05) | robots.txt `Disallow: /` for all clients, but the API is documented for building applications; same template reading as at/nl (unconfirmed). Still a trial service. **Off by default — needs WLM_PERMITTED=de and the operator's permission.** |
| de | Bundesfinanzhof – Entscheidungen online (bundesfinanzhof.de) | Impressum: decisions are official works (§ 5 UrhG), free to use | Unknown | Not stated | None | Robots.txt Crawl-Delay: 60 (2026-11-10); throttled to 1 request per 60 s |  |
| de | Gesetze im Internet (Bundesamt für Justiz / BMJV) (www.gesetze-im-internet.de) | No licence stated; statutes are public-domain official works (§ 5 UrhG) | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen (2026-11-05) |  |
| difc | DIFC Courts judgments (www.difccourts.ae) | © DIFC Courts; Terms of Use allow personal, non-commercial use only; no copying, storing or redistribution without express written permission | **No** | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~20 requests (2026-11) | robots.txt disallows only /menu and /videos. **Off by default — needs WLM_PERMITTED=difc and the operator's permission.** |
| dk | Retsinformation (Civilstyrelsen) (www.retsinformation.dk) | Civilstyrelsen open-data terms: free, non-exclusive, unlimited right of use (copy, distribute, modify, commercial and non-commercial); laws are not copyrighted (ophavsretsloven § 9). Must not imply endorsement by Civilstyrelsen. ELI XML is the documented channel; search and the HTML fallback use the website's own undocumented JSON | Yes | Yes | None | None documented for www.retsinformation.dk (terms: don't load the interface unreasonably); no 429 in ~25 requests (2026-11); using 1 s spacing | Search uses the website's undocumented JSON. **Case law not covered: Domsdatabasen only allows API access after an approved application**, so it is not used. |
| do | Tribunal Superior Electoral – visor de sentencias (visorpdf.tse.do) | No open licence stated; Términos de Uso §4 reserves the portal's content to the TSE; robots.txt Content-Signal search=yes, ai-train=no, use=reference | Unknown | **No** | None | Unknown; 1 s spacing, no 429 seen in ~20 requests (2026-11-06); no Crawl-delay in robots.txt | Electoral court only (TSE contentious judgments, 2021+); the site reserves its content against AI training (robots.txt ai-train=no, use=reference). |
| dz | Journal Officiel de la République Algérienne (JORADP), Secrétariat Général du Gouvernement (www.joradp.dz) | Unknown (no terms of use published on joradp.dz) | Unknown | Not stated | None | Unknown; 1.5 s spacing, no 429 seen in ~30 requests (2026-11) |  |
| dz | Cour constitutionnelle (and former Conseil constitutionnel) of Algeria (cour-constitutionnelle.dz) | Unknown (no terms of use, legal notice or copyright line on cour-constitutionnelle.dz) | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~15 requests (2026-11) |  |
| ec | Corte Constitucional del Ecuador – Buscador de Sentencias (public JSON backend) and signed decision PDFs (esacc storage) (buscador.corteconstitucional.gob.ec) | Unknown: no terms-of-use or licence page on buscador/esacc or corteconstitucional.gob.ec (checked 2026-11-06); footer says '© Corte Constitucional del Ecuador \| Todos los derechos reservados'; court decisions are official texts | Unknown | Not stated | None | Unknown; no robots.txt on either host (2026-11-06); 1 s spacing, no 429 seen in ~15 requests (2026-11-06) |  |
| echr | HUDOC (European Court of Human Rights) (hudoc.echr.coe.int) | © ECHR-CEDH; reproduction allowed free of charge, with acknowledgment, for private use or information/education about the Court's work | **No** | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~20 requests (2026-11) | No robots.txt. A commercial deployment needs the Court's permission. |
| echr | European Convention on Human Rights and Protocols (official PDF, read it there; not available through this server) (www.echr.coe.int) | Not stated | Unknown | Not stated | None | Unknown |  |
| ecowas | ECOWAS Community Court of Justice website (courtecowas.org) | © ECOWAS Community Court of Justice; reuse allowed with credit and changes indicated (Legal Notice); robots.txt Content-Signal search=yes, ai-train=no, use=reference | Unknown | **No** | None | Unknown; 1 s spacing, decision list (21 requests) cached in memory 12 h; no 429 seen in ~110 requests (2026-11-06) | Credit the ECOWAS Court of Justice when reusing; only the Reports of Cases / Official Journal texts are authentic; the site reserves its content against AI training (robots.txt ai-train=no, use=reference). |
| ecowas | ECOWAS Court Law Reports (CCJELR), English volumes 2004-2017 (courtecowas.org) | © ECOWAS Community Court of Justice; reuse allowed with credit and changes indicated (Legal Notice); robots.txt Content-Signal search=yes, ai-train=no, use=reference | Unknown | **No** | None | Same host as the decision list (1 s spacing); one 3-7 MB PDF per volume, 2 volumes kept in memory; no 429 seen (2026-11-10) | Credit the ECOWAS Court of Justice when reusing; the site reserves its content against AI training (robots.txt ai-train=no, use=reference). |
| ee | Riigi Teataja (State Gazette, Ministry of Justice and Digital Affairs) (www.riigiteataja.ee) | Legal acts are not protected by copyright (Copyright Act § 5 p 1); RT publishes all acts as XML open data (RT FAQ '9. Avaandmed'). RT Act § 12(1): texts shown elsewhere must refer to the Riigi Teataja text. | Yes | Not stated | None | Not published (behind Cloudflare); no 429 in ~40 requests (2026-11-05); using 1 s spacing | robots.txt disallows ~5,600 listed acts (we refuse those) and the court-decision routes, so **no case law**. |
| efta | EFTA Court website (eftacourt.int, api.eftacourt.int) | Unknown (no reuse terms published; the Legal Notice page is empty, footer '© 2026 EFTA Court') | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~20 requests (2026-11) | api.eftacourt.int robots.txt allows all; eftacourt.int has none. |
| eg | المحكمة الدستورية العليا – Supreme Constitutional Court portal (judgments, full text) (www.sccourt.gov.eg) | None stated: no terms page; footer 'جميع الحقوق محفوظة © 2025 للمحكمة الدستورية العليا' (all rights reserved). Court judgments are excluded from copyright under Egyptian Law 82/2002 art. 141 | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~40 requests (2026-11-06); robots.txt absent (404) |  |
| es | BOE consolidated law (www.boe.es) | BOE reuse conditions (licencia tipo, Resolución 27-06-2024, under Ley 37/2007): attribution with link to boe.es, consolidated texts must be marked as informative only with their last-update date | Yes | Not stated | None | Unknown: no limit in the API docs (APIconsolidada.pdf) or terms; robots.txt has no Crawl-delay. 1 s spacing, no 429 seen in ~20 requests (2026-11-05). | robots.txt has no Crawl-delay. |
| es | Constitutional Court HJ (hj.tribunalconstitucional.es) | Unknown: hj.tribunalconstitucional.es shows no aviso legal or reuse terms; the main site's aviso legal sits behind a JavaScript browser check and could not be read (2026-11-05). Court decisions are excluded from copyright (Ley de Propiedad Intelectual art. 13). | Unknown | Not stated | None | Unknown: nothing published; robots.txt is 404 (no rules). 1 s spacing; a search costs 2-3 requests (token, POST, list). No 429 seen (2026-11-05). | robots.txt 404. |
| et | House of Peoples' Representatives: published laws (Federal Negarit Gazeta PDFs, hopr.gov.et) | Terms of use page is empty; footer '© Copyright House of People's Representatives of Ethiopia, 2026. All rights reserved.' | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~25 requests (2026-11) | Negarit Gazeta issues as originally published (not consolidated); the library is kept by hand and a few entries link to a missing or wrong PDF. |
| eu | Publications Office CELLAR (EUR-Lex data): SPARQL + REST (publications.europa.eu) | EU legal documents reusable under Commission Decision 2011/833/EU (commercial or non-commercial reuse, acknowledge source, do not distort); EUR-Lex metadata CC0 | Yes (unconfirmed for CJEU material) | Not stated | None | None published (checked 2026-11); 1 s spacing, no 429 seen in ~40 requests (2026-11) | Allowed by robots.txt. Acknowledge the source; do not distort. |
| fi | Finlex open data (opendata.finlex.fi) | CC BY 4.0 (Finlex FAQ); statutes themselves are public domain (Copyright Act 404/1961 s. 9) | Yes | Not stated | None | Not published: guide says volumes 'may be restricted', answered with 429; no 429 in ~30 requests (2026-11-05); using 1 s spacing |  |
| fi | Finlex website (www.finlex.fi), KKO/KHO published decisions | Public, 'no restrictions on use' (Finlex FAQ); court decisions are public domain (Copyright Act s. 9); no personal-data misuse | Yes | Not stated | None | Not published; no 429 in ~15 requests (2026-11-05); using 1 s spacing |  |
| fr | Judilibre (Cour de cassation, via PISTE) (www.courdecassation.fr) | Licence Ouverte / Open Licence 2.0 (Etalab) + Cour de cassation reuse CGU | Yes | Not stated | Free key | Unknown; PISTE per-app quotas (README: 'quotas ... sur le portail PISTE'); 1 s spacing | Pseudonymised decisions: do not try to re-identify people; profiling, comparing or rating judges and court clerks is a criminal offence (COJ art. L111-13). |
| fr | Légifrance API (DILA, via PISTE) (www.legifrance.gouv.fr) | Licence Ouverte / Open Licence 2.0 (Etalab) | Yes | Not stated | Free key | Unknown; PISTE per-app quotas shown in the app's 'Consulter les quotas' (CGU IV.3); 1 s spacing | Légifrance API data are not legally binding: only the signed PDF Journal officiel is (CGU VI.1). Decisions: profiling, comparing or rating judges is a criminal offence (COJ art. L111-13, CJA art. L10). |
| gb | Find Case Law, The National Archives (caselaw.nationalarchives.gov.uk) | Open Justice Licence v2.0: free re-use incl. commercial; 'computational analysis' (programmatic bulk searching to identify, extract or enrich records) needs a separate, free licence | Yes | **No** (robots.txt blocks named AI bots: GPTBot, ClaudeBot…) | None | Documented: 1,000 requests / rolling 5 min per IP, HTTP 429 when exceeded (API docs, checked 2026-11) | Our User-Agent is not blocked. **Computational analysis needs the free licence from caselaw@nationalarchives.gov.uk — get it before hosting.** Coverage from 2003. |
| gb | legislation.gov.uk, The National Archives | Open Government Licence v3.0 | Yes | Yes | None | Documented: 1,500 requests / 5 min per user, requests blocked until the 5-min average drops (fair-use policy, checked 2026-11) | robots.txt: Crawl-delay 5. |
| ge | Legislative Herald of Georgia (Matsne), Ministry of Justice (matsne.gov.ge) | Unknown: no open licence; site footer says 'All Rights Reserved' | Unknown | Not stated | None | Robots.txt Crawl-delay: 10, so 10 s spacing; no 429 seen in ~20 requests (2026-11) | Supreme Court search (supremecourt.ge) is robots-disallowed and not used. |
| ge | Courts of Georgia decisions (ecd.court.ge) | Unknown: no terms published | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~20 requests (2026-11) | Decisions dated 2018-01 to 2020-04 only. |
| gr | Areios Pagos case law (www.areiospagos.gr) | Areios Pagos terms: further use allowed on the sole condition that texts are not altered or distorted and that the source and publication date are cited | Yes | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~20 requests (2026-11-05) | Supreme Civil and Criminal Court only. |
| gr | Government Gazette search (search.et.gr, Εθνικό Τυπογραφείο) | Terms of use: personal, informational, non-commercial use only; no reproduction or copying for non-personal use without permission | **No** | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~25 requests (2026-11-05) | **Off by default — needs WLM_PERMITTED=gr and the operator's permission.** Scanned FEK issues have no text layer and are reported, not OCR'd. |
| gt | Corte de Constitucionalidad – sentencias PDF (jurisprudencia.cc.gob.gt) | Unknown: no licence on the PDF host; the CC's terms (www.cc.gob.gt) sit behind a Cloudflare challenge; robots.txt Content-Signal search=yes, ai-train=no, use=reference | Unknown | **No** | None | Unknown; 1 s spacing, no 429 seen in ~10 requests (2026-11-06); no Crawl-delay in robots.txt | Constitutional Court rulings by id only (no search: the CC's search portal blocks automated clients); robots.txt reserves the content against AI training (ai-train=no, use=reference). |
| gy | Laws of Guyana, Ministry of Legal Affairs (mola.gov.gy) | 'Copyright @ Ministry of Legal Affairs. All rights reserved' (site footer); no terms of use or licence page (checked 2026-11-05) | Unknown | Not stated | None | Unknown; no Crawl-delay; 1 s spacing, no 429 in ~15 requests (2026-11) |  |
| gy | CCJ judgment lists and PDFs (ccj.org) | © Caribbean Court of Justice; no licence stated (the Terms of Use page is empty, 2026-11-05) | Unknown | Not stated | None | Unknown; 1 s spacing, both lists cached in memory 6 h; no 429 seen in ~20 requests (2026-11) |  |
| hk | Hong Kong e-Legislation (Department of Justice) open data on DATA.GOV.HK (data.gov.hk) | DATA.GOV.HK Terms and Conditions of Use v1.2 (free reuse incl. commercial, with source acknowledgement and attribution to the HKSAR Government, DoJ and DATA.GOV.HK) | Yes | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~12 requests (2026-11) | Attribute the HKSAR Government, DoJ and DATA.GOV.HK. Open-data XML, not the verified copies with legal status. **No case law: the Judiciary's Legal Reference System and HKLII both forbid automated access in robots.txt.** www.elegislation.gov.hk itself is robots-disallowed. |
| hn | Biblioteca Virtual del Tribunal Superior de Cuentas (TSC) – laws, codes, regulations and decrees as published (PDF, mostly La Gaceta copies) (www.tsc.gob.hn) | Unknown: no licence or terms of use on www.tsc.gob.hn; robots.txt disallows only /wp-admin/ (checked 2026-11-06) | Unknown | Not stated | None | Unknown; no Crawl-delay; 1 s spacing, no 429 seen in ~25 requests (2026-11-06) |  |
| hn | ENAG – La Gaceta Digital (Diario Oficial de la República de Honduras) (www.enag.gob.hn) | Unknown: no licence or terms page; the site says a Congreso–ENAG agreement gives 'acceso universal y gratuito a la legislación hondureña' published in La Gaceta (checked 2026-11-10) | Unknown | Not stated | None | Unknown; robots.txt standard Joomla (no Crawl-delay; /index.php/ allowed); 2 s spacing |  |
| hr | Narodne novine (official gazette of the Republic of Croatia) (narodne-novine.nn.hr) | No open licence stated; site terms say content is copyright and usable 'under the conditions of the law'. Laws, regulations and court decisions are official texts excluded from copyright (Zakon o autorskom pravu, čl. 8). | Unknown | Yes | None | Documented: 'configure scripts and bots to at most 3 requests per second' (data_access_hr.aspx, read 2026-11-05); using 0.5 s spacing, no 429 seen | robots.txt disallows ~100 gazette articles by path (checked before each fetch) and searches of the notices part (not used). Case law = Constitutional Court decisions published in the gazette only: odluke.sudovi.hr and sljeme.usud.hr are `Disallow: /`. |
| ht | Conseil Supérieur du Pouvoir Judiciaire (CSPJ): document library (cspj.ht) | Unknown: no terms page; footer 'Droit d'auteur © 2026 Conseil Supérieur du Pouvoir Judiciaire'. Haitian laws are official texts. | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~40 requests (2026-11) | Small selection (~17 laws on justice, family, foreigners, corruption, trafficking, free zones; no nationality law) uploaded by the CSPJ, as published, not consolidated; check Le Moniteur for amendments. |
| ht | Cour de cassation d'Haïti: Constitution PDF (1987 original) (www.courdecassation.ht) | Unknown: no terms page; no robots.txt (404). The Constitution is an official text. | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~4 requests (2026-11-10) | Constitution text is the 1987 original; the 2011 amended PDF on the same page is a scan. |
| hu | Bírósági Határozatok Gyűjteménye (eakta.birosag.hu, Országos Bírósági Hivatal) | Not stated (published free of charge for information; reuse terms not found) | Unknown | Not stated | None | Not published; 1 request/s self-imposed, no 429 seen in a handful of requests (2026-11-05) | Case law only, PDF full texts. **No legislation: the Nemzeti Jogszabálytár's terms forbid automated requests without written permission.** |
| icj | International Court of Justice website (www.icj-cij.org): case pages and document search | © International Court of Justice; site disclaimer: 'may not be reproduced or used for commercial purposes'. No other licence stated. | **No** | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~35 requests (2026-11) | ICJ site terms: its information may not be reproduced or used for commercial purposes (the Statute and Rules texts are read from its HTML pages). Decision texts are PDF-only and blocked by a bot challenge here: you get metadata and links, not the text. |
| icsid | ICSID case database (icsid.worldbank.org, icsidfiles.worldbank.org) | © ICSID / World Bank Group; WBG Terms and Conditions (2025-07-25): non-commercial use with attribution, no derivative or commercial use (ICSID's own /user-agreement page answers 403 to this client) | **No** | Not stated | None | Unknown; 1 s spacing, case list cached in memory 6 h; no 429 seen in ~10 requests (2026-11) | robots.txt allows /api and case pages. Text-layer PDFs only (no OCR). |
| id | JDIH Kementerian Sekretariat Negara (jdih.setneg.go.id) – Produk Hukum | No licence published; statutes are not copyright-protected (UU 28/2014 Pasal 42); site footer 'All Rights Reserved by Kementerian Sekretariat Negara RI' | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~25 requests (2026-11-06) |  |
| id | Majelis Permusyawaratan Rakyat (www.mpr.go.id) – UUD NRI 1945 | No licence published; the Constitution is not copyright-protected (UU 28/2014 Pasal 42); site footer 'HAK CIPTA (c) SEKRETARIAT JENDERAL MPR RI'; the book says 'MILIK NEGARA, TIDAK DIPERDAGANGKAN' | Unknown | Not stated | None | Unknown; 1 s spacing, one page + one ~35 MB PDF per load, cached (2026-11-10) |  |
| ie | Irish Statute Book (eISB, Office of the Attorney General) (www.irishstatutebook.ie) | Oireachtas (Open Data) PSI Licence, which incorporates CC BY 4.0 (attribution required). Search uses the site's own Solr title index (undocumented); texts use the documented ELI XML/HTML | Yes | Yes | None | None documented; robots.txt is 404 (no rules); no 429 in ~25 requests (2026-11); using 1 s spacing | robots.txt 404. Search uses the site's undocumented Solr index. **No case law: judgments.courts.ie robots.txt is `Disallow: /`.** |
| ie | Law Reform Commission Revised Acts (revisedacts.lawreform.ie) | Legislative text: Oireachtas (Open Data) PSI Licence (CC BY 4.0); LRC annotations: CC BY 4.0. Attribute the Houses of the Oireachtas and the LRC separately | Yes | Yes | None | None documented; robots.txt allows all; no 429 in ~15 requests (2026-11); using 1 s spacing | robots.txt allows all. Attribute the Oireachtas and the LRC separately. |
| il | Knesset OData (ParliamentInfo) – Israeli law database (official) (knesset.gov.il) | No licence stated; laws are not copyright-protected (Copyright Act 2007, s. 6) | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~20 requests (2026-11) | Official law index and metadata. |
| il | Sefer HaChukim (ספר החוקים, Reshumot) as-published PDFs on fs.knesset.gov.il (official) | No licence stated; laws are not copyright-protected (Copyright Act 2007, s. 6) | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~25 PDF requests (2026-11); no robots.txt (404) | Volunteer-maintained consolidated text (shown as a warning); check the Knesset gazette before relying on it. No case law. |
| il | Open Law Book (ספר החוקים הפתוח), Hebrew Wikisource – non-official (crowd-maintained, Wikimedia Foundation) (he.wikisource.org) | CC BY-SA 4.0 (Wikimedia Terms of Use s. 7) | Yes | Not stated | None | Unknown for article pages; 1 s spacing, no 429 seen (2026-11) | Consolidated text is volunteer-maintained on Wikisource, not an official version; check the Knesset gazette PDFs before relying on it. |
| in | Lexifina global law record (publisher: Legislative Department, Ministry of Law and Justice (Government of India)) (github.com) | Lexifina's tools and tables CC0; the law text under each publisher's terms (see the country's LICENSE in the repository) | Unknown | Not stated | None | 60 calls/min and 10,000/day per address, one at a time (documented 2026-11-27) | Not the official publisher. India Code's terms forbid automated access without written permission, so Fontes reads Lexifina's record of the Acts instead. |
| in | Indian Supreme Court Judgments (AWS Open Data; Dattam Labs mirror of the Supreme Court's e-SCR) (registry.opendata.aws) | Dataset CC BY 4.0 (AWS Open Data registry, read 2026-11-10); the judgments themselves are not copyright-protected for reproduction (s. 52(1)(q)(iv) Copyright Act 1957); attribute the Supreme Court of India / e-SCR | Yes | Yes | None (public S3 bucket, no AWS account) | None documented (Amazon S3); 0.5 s spacing, no 429/503 seen in ~30 requests (2026-11-10) | S.C.R.-reported judgments only; the official copy is at scr.sci.gov.in. |
| iq | Kurdistan Parliament legislation database (قاعدة التشريعات), legislation.krd (Kurdistan Region of Iraq only) | Unknown: no terms or copyright notice on legislation.krd (official legislative texts of the Kurdistan Region) | Unknown | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~30 requests (2026-11) | Kurdistan Region legislation only (not federal Iraqi law). Texts are as enacted; amendments are separate records. |
| is | Ísland.is court rulings (Stafrænt Ísland; Hæstiréttur, Landsréttur, héraðsdómstólar) (island.is) | No reuse licence stated; the island.is user terms (notendaskilmálar, 2022-12-05) say nothing on reuse or automated access. Court judgments are not protected by copyright in Iceland (höfundalög nr. 73/1972, 9. gr.; unverified). API is the portal's own undocumented GraphQL (frontend code is MIT on GitHub) | Unknown | Not stated | None | None documented; island.is has no robots.txt (404, 2026-11-05); no 429 in ~20 requests (2026-11); using 1 s spacing | No robots.txt. Undocumented GraphQL backend of the portal. |
| it | Normattiva open data (dati/api.normattiva.it) | CC BY 4.0 from 2026-01-01 (dati.normattiva.it 'Dati disponibili' page, read 2026-11-05; CC BY-NC 4.0 during the 2025 trial) | Yes | Not stated | None | Unknown (not documented); 1 s spacing, no 429 seen in ~20 requests (2026-11-05) |  |
| it | Normattiva — www.normattiva.it (texts by URN:NIR) | Reproduction allowed if the source is named and the text is said to be non-authentic and free (Note legali); only the Gazzetta Ufficiale is official | Unknown | Not stated | None | Unknown (not documented); 1 s spacing, no 429 seen in ~25 requests (2026-11-05). Codice civile pages are 2.6 MB and take 6-12 s. |  |
| itlos | ITLOS case pages (www.itlos.org) | ITLOS Terms and Conditions of Use: download and copy for personal, non-commercial use (academic, research, private study), Tribunal acknowledged as source; ITLOS Reports and Pleadings texts may not be reproduced or stored in a retrieval system without the Registrar's written permission | **No** | Not stated | None | Unknown; 1 s spacing, case list cached in memory 6 h; no 429 seen in ~8 requests (2026-11) | ITLOS terms: personal, non-commercial use only, acknowledge the Tribunal as source. Judgment/order texts (ITLOS Reports) need the Registrar's permission to reproduce, so only the case record and PDF links are given here. |
| jm | Find Case Law, The National Archives (UK): Judicial Committee of the Privy Council judgments (caselaw.nationalarchives.gov.uk) | Open Justice Licence v2.0: free re-use incl. commercial; 'computational analysis' (programmatic bulk searching to identify, extract or enrich records) needs a separate, free licence | Yes | **No** | None | Documented: 1,000 requests / rolling 5 min per IP, HTTP 429 when exceeded (API docs, checked 2026-11) |  |
| jm | Supreme Court of Jamaica judgments (supremecourt.gov.jm) | © the Court; no licence stated. Terms of Use page has a privacy policy and disclaimer only ('makes the information on this website available as a public service'); silent on reuse and automated access (read 2026-11-05) | Unknown | Not stated | None | Unknown; no Crawl-delay; 1 s spacing, no 429 in ~15 requests (2026-11) |  |
| jm | Court of Appeal of Jamaica judgments (courtofappeal.gov.jm) | © the Court; no licence stated. Terms of Use page has a privacy policy and disclaimer only ('makes the information on this website available as a public service'); silent on reuse and automated access (read 2026-11-05) | Unknown | Not stated | None | Unknown; no Crawl-delay; 1 s spacing, the two judgment lists cached in memory 6 h; no 429 in ~10 requests (2026-11) |  |
| jo | Constitutional Court of Jordan (المحكمة الدستورية), cco.gov.jo | Site copyright notice: content owned by the Constitutional Court (Copyright Law 22/1992); downloading, viewing and printing allowed for personal or in-house, non-commercial use; small parts may be republished unmodified with the source named; other uses need the court's permission. | **No** | Not stated | None | Unknown; 1 s spacing, no 429 seen in ~30 requests (2026-11) | Constitutional Court terms: personal or in-house non-commercial use only; cite 'المحكمة الدستورية' as the source and quote the text unmodified. |
| jp | Case law: 裁判所 裁判例検索 (courts.go.jp), NOT wired in, search down since 2026-11-05 (e-Gov has no case law) | Not reviewed | Unknown | Not stated | None | Unknown |  |
| jp | e-Gov 法令検索 / 法令API Version 2 (Digital Agency) (laws.e-gov.go.jp) | Public Data License 1.0 (公共データ利用規約 第1.0版, CC BY 4.0-compatible; attribution required, mark edits) per e-Gov terms. Statutes are also outside copyright (Copyright Act art. 13) | Yes | Not stated | None | Unknown (not in the OpenAPI spec); 1 s spacing, no 429 seen in ~25 requests (2026-11) |  |
| kg | Constitutional Court of the Kyrgyz Republic (constsot.kg) | None stated (footer: © Constitutional Court of the Kyrgyz Republic); court acts are official documents | Unknown | Not stated | None | Unknown; 1.5 s spacing, no 429 seen in ~20 requests (2026-11) |  |
| kh | Council for the Development of Cambodia (CDC): Laws and Regulations (cdc.gov.kh) | Unknown (no terms of use publ