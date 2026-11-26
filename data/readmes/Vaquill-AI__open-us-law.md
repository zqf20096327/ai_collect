# Open US Law

**US law in one free download, collected from government publishers.**

5 million+ entries · Updated September 30, 2026 · Free for non-commercial use

**[Download](https://oss-data-us.vaquill.ai/index.html)** · **[Watch the video](https://youtu.be/PvSEd6bdaO0)** · **[Hugging Face](https://huggingface.co/datasets/vaquill/open-us-law)** · **[Ask on Discord](https://discord.gg/GQtnwxf8nQ)**

**Free API, forever, for students, academics, researchers and legal aid.** [Sign up](https://app.vaquill.ai/auth/signup) or [log in](https://app.vaquill.ai/auth/login?redirect=%2Fdeveloper%3Ftab%3Dapi-key) to get your key with 1,000 credits. Need more? Email [contact@vaquill.ai](mailto:contact@vaquill.ai?subject=Open%20US%20Law%20API%20credits) and we will add as many as you need, free.

<a href="https://youtu.be/PvSEd6bdaO0"><img src="https://raw.githubusercontent.com/Vaquill-AI/open-us-law/main/assets/walkthrough-thumb.png" alt="Watch the Open US Law walkthrough" width="480"></a>

## What's inside

| Type of law | Covers | Entries |
|---|---|--:|
| **Statutes** | US Code, 45 states, DC, Puerto Rico | 1.8 million |
| **Regulations** | Federal, 37 states, DC, Puerto Rico | 1.4 million |
| **Past federal regulations** | Older editions, for history | 886,000 |
| **Other federal records** | Acts of Congress, agency decisions, treaties, executive orders | 764,000 |
| **Attorney general opinions** | 40 states, DC, Puerto Rico | 105,000 |
| **Agency guidance** | Federal, 47 states, DC, Puerto Rico | 54,000 |
| **Court rules** | Federal, 44 states, DC, Puerto Rico | 49,000 |
| **Constitutions** | US, 49 states, Puerto Rico | 12,000 |

## How to get it

| I want | Go to | Account needed |
|---|---|---|
| One state or type of law | [File list](https://oss-data-us.vaquill.ai/index.html) | No |
| Everything (6.9 GB) | [Full download](https://oss-data-us.vaquill.ai/v2026.09.1/open-us-law-v2026.09.1-parquet.tar) | No |
| The Hugging Face version | [Hugging Face](https://huggingface.co/datasets/vaquill/open-us-law) | Free account |
| Law that stays up to date | [Vaquill API](https://www.vaquill.ai/legal-api) | Yes, 1,000 free credits |

Files are in Parquet, a format for data tools. They don't open in Word or a PDF reader.

## Can I use it?

| Your use | Allowed? |
|---|---|
| Research, teaching, journalism | **Yes**, with credit |
| Non-commercial legal aid and open source | **Yes**, with credit |
| Commercial products or services | **[Email us for a license](mailto:contact@vaquill.ai)** |
| The words of the law itself | **Yes**, they are public domain |

## Before you rely on it

- **Not legal advice.** Check the official source.
- **A snapshot.** Changes after the update date may be missing.
- **Includes old law.** Check whether an entry is marked repealed or superseded.
- **Coverage varies.** States differ by type of law.

## More details

<details>
<summary><b>States included in statutes</b></summary>

Alabama, Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Idaho, Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Maryland, Massachusetts, Michigan, Minnesota, Missouri, Montana, Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, Pennsylvania, Rhode Island, South Carolina, South Dakota, Texas, Utah, Vermont, Virginia, Washington, West Virginia, Wisconsin, Wyoming, plus DC and Puerto Rico.

For other types of law, see the [file list](https://oss-data-us.vaquill.ai/index.html).

</details>

<details>
<summary><b>Where the law comes from</b></summary>

- Published by government bodies, or bodies they designate to publish the law.
- Each entry keeps a link to its source.
- Collected automatically, sometimes through US-based proxies for sites that serve only US visitors.
- No third-party licensed content is included.

</details>

<details>
<summary><b>Known issues</b></summary>

- About 44,000 entries include stray website menu or header text.
- Some source links open an index page instead of the exact section.
- Pennsylvania statutes cover the Consolidated Statutes only.
- About 19,600 Oklahoma regulation entries are copies the publisher labels unofficial.

</details>

<details>
<summary><b>License and credit</b></summary>

- **Legal text:** public domain (*Georgia v. Public.Resource.Org*, 2020).
- **This dataset:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) from v2026.09 onward.
- **Code:** [Apache-2.0](https://github.com/Vaquill-AI/open-us-law/blob/main/LICENSE).
- **Credit line:** Open US Law (v2026.09.1) by Vaquill AI, CC BY-NC 4.0, https://huggingface.co/datasets/vaquill/open-us-law

</details>

<details>
<summary><b>Free API access for non-commercial projects</b></summary>

- [Sign up](https://app.vaquill.ai/auth/signup) or [log in](https://app.vaquill.ai/auth/login?redirect=%2Fdeveloper%3Ftab%3Dapi-key) to get a key. It starts with 1,000 free credits.
- Need more? Email [contact@vaquill.ai](mailto:contact@vaquill.ai?subject=Open%20US%20Law%20API%20credits) with who you are and what you are building, and we will add more, free.
- Free keys have rate limits and no uptime guarantee.

</details>

<details>
<summary><b>For developers</b></summary>

**Download and read one file**

```bash
pip install pyarrow
curl -O https://oss-data-us.vaquill.ai/v2026.09.1/us_ak_statutes.parquet
python -c "import pyarrow.parquet as pq; print(pq.read_table('us_ak_statutes.parquet').slice(0, 5))"
```

**Run a scraper**

```bash
git clone https://github.com/Vaquill-AI/open-us-law.git
cd open-us-law
pip install -r requirements.txt
cd scripts/state_scrapers
OUT_DIR=./data python -m src.scrapers.us.states.ks.statutes.scrapeKS
```

| Scrapers | Folder |
|---|---|
| Federal | [scripts/federal](https://github.com/Vaquill-AI/open-us-law/tree/main/scripts/federal) |
| State statutes | [scripts/state_scrapers](https://github.com/Vaquill-AI/open-us-law/tree/main/scripts/state_scrapers), [scripts/statutes](https://github.com/Vaquill-AI/open-us-law/tree/main/scripts/statutes) |
| Regulations | [scripts/regulations](https://github.com/Vaquill-AI/open-us-law/tree/main/scripts/regulations) |
| Court rules | [scripts/court_rules](https://github.com/Vaquill-AI/open-us-law/tree/main/scripts/court_rules) |
| Constitutions | [scripts/constitutions](https://github.com/Vaquill-AI/open-us-law/tree/main/scripts/constitutions) |

- Scrapers are published for some sources, not all.
- Some need a US connection or Chrome, and can break when a government site changes.
- Pull requests that fix them are welcome.
- Column names and dataset configs are on the [dataset card](https://huggingface.co/datasets/vaquill/open-us-law).

</details>

## Help

Found a mistake or have a question? [Report it](https://github.com/Vaquill-AI/open-us-law/issues), [ask on Discord](https://discord.gg/GQtnwxf8nQ) or [email us](mailto:contact@vaquill.ai).

Built by [Priyansh Khodiyar](https://www.linkedin.com/in/zriyansh/) and [Vaquill AI](https://www.vaquill.ai).

*The law is public. Reading it should not cost money.*
