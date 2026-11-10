# cover-letter-tailor

A Claude skill that writes personalized, tailored cover letters based on your CV and the job posting you want to apply for. No generic templates. Every letter is stitched to the specific role and company.

## What it does

- Reads your CV in `.tex` or plain text format
- Fetches the job posting from a URL (or asks you to paste it if the link is inaccessible)
- Asks which language you want the cover letter in (English or Portuguese)
- Writes a 250-380 word letter that connects your real experience to the job requirements
- Avoids hollow phrases like "I am a passionate team player"
- Never uses em dashes (—) anywhere in the output

## Install

```bash
npx skills add guithepc/cover-letter-tailor
```

## Usage

Paste your CV (`.tex` or plain text) and drop the job posting URL into the chat. The skill handles the rest.

---

by @pctheonee