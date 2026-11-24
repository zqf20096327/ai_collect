# Open Health Databases

🌐 **Live site: [healthdata.abdullahdmc.com](https://healthdata.abdullahdmc.com)**

A curated, searchable catalogue of **400 freely available health and clinical databases** in 17 categories, such as MIMIC-IV, eICU, NHANES, TCGA, PhysioNet and many more. Each entry gives:

- a short introductory description
- a link to the original descriptor article, where one exists
- a link to where you get the data
- the **access mode**:

| Label | Meaning |
|---|---|
| **Open** | Completely free. Direct download with no account. |
| **Registration** | Free. Create an account and/or accept the terms. |
| **Application** | Free. Submit a request or data use agreement for approval. |
| **Credentialed** | Free. Identity credentialing plus ethics training (e.g. CITI) and a DUA, as on PhysioNet. |

Fee-based sources (UK Biobank, CPRD, HCUP NIS, MarketScan, Optum) are deliberately excluded.

📋 **Full list as a table:** [DATABASES.md](DATABASES.md)

## Categories

ICU, perioperative and emergency care · EHR, cohorts, registries and synthetic data · population and public-health surveys · global health and vital statistics · radiology and medical imaging · pathology, dermatology and ophthalmology · neuroimaging and neuroscience · physiological signals and wearables · genomics and multi-omics · clinical trials and IPD · clinical text, literature and terminologies · drugs and pharmacovigilance · infectious diseases and AMR · data repositories and portals · medical AI, LLM and multimodal benchmarks · endoscopy and surgical video · dataset catalogues and search engines.

## Repository layout

```
data/            one JSON file per category: the single source of truth
site/            HTML template, CSS, JS and favicon
scripts/build.mjs   builds dist/ (site, databases.csv, databases.json) and DATABASES.md
scripts/verify.mjs  checks every access URL, resolves DOIs via Crossref, reads PhysioNet access policies
```

No dependencies. You only need Node 18 or later.

```bash
npm run build    # writes dist/ and DATABASES.md
npm run verify   # link / DOI / access-policy check
```

## Adding or correcting a database

Edit the right file in `data/`. Each item looks like this:

```json
{
  "id": "mimic-iv",
  "name": "MIMIC-IV",
  "full_name": "Medical Information Mart for Intensive Care IV",
  "description": "One or two sentences.",
  "provider": "Who maintains it",
  "region": "Country / Global",
  "access": "open | registration | application | credentialed",
  "access_note": "Exactly what a user must do to obtain it.",
  "url": "https://where-to-get-the-data",
  "paper": { "label": "Author et al. Journal Year;Vol:Page", "url": "https://doi.org/..." },
  "tags": ["EHR", "ICU"]
}
```

Use `"paper": null` when there is no descriptor article. Run `npm run build` (it validates the fields), then open a pull request.

## Acknowledging this catalogue

If you found a database through this site, please acknowledge it. GitHub's **"Cite this repository"** button (generated from `CITATION.cff`) gives the citation, or use:

> Khan MAS, et al. Open Health Databases: a catalogue of freely available health datasets. https://healthdata.abdullahdmc.com. Accessed yyyy-mm-dd.

Replace `yyyy-mm-dd` with the date you visited the site.

## Contributors

Everyone whose commit reaches `main` is credited automatically. After each push, the `contributors` GitHub Action adds new GitHub contributors to `contributors.json` (using the name on their GitHub profile, in "Surname Initials" form). It also regenerates `CITATION.cff`, and the site's citation and footer pick up the change on the next deploy. If your name isn't formatted the way you publish, edit your own entry in `contributors.json` in a pull request. The Action never overwrites existing entries.

## Verification notes

Every article DOI in the catalogue resolves through Crossref to the matching title. Access URLs were checked automatically. A few institutional sites (for example SAMHSA, HRS, ICPSR, LOINC and DrugBank) block automated requests, and a few others have certificate or timeout problems seen from scripts. These links point to the official provider pages and were kept. Access terms change, so always read the provider's current licence before you use the data.

## Deployment

The site is deployed on Vercel. `vercel.json` runs `node scripts/build.mjs` and serves `dist/`.

## License

Code: MIT. Catalogue text: CC BY 4.0. The datasets themselves are governed by their own licences.
