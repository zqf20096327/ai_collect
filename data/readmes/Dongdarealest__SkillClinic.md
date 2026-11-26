<p align="center">
  <img src="https://raw.githubusercontent.com/Dongdarealest/skillclinic/main/assets/masthead.png" alt="SkillClinic: a checkup for the skills your AI runs" width="880">
</p>

<p align="center">
  One command audits every AI skill on your machine and gives each one a verdict:<br>
  valid or broken, safe or risky, and what it costs you in tokens.
</p>

<p align="center">
  <a href="https://github.com/Dongdarealest/skillclinic/releases"><img src="https://img.shields.io/github/v/release/Dongdarealest/skillclinic?style=flat-square&color=141414&label=release" alt="Latest release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-141414?style=flat-square" alt="MIT license"></a>
  <img src="https://img.shields.io/badge/python-3.10%2B-141414?style=flat-square" alt="Python 3.10 or newer">
  <img src="https://img.shields.io/badge/dependencies-zero-141414?style=flat-square" alt="Zero dependencies">
  <img src="https://visitor-badge.laobi.icu/badge?page_id=Dongdarealest.skillclinic" alt="Visitors">
  <a href="https://dongdarealest.github.io/skillclinic/"><img src="https://skilldoctor-badges.vercel.app/badges/Dongdarealest--skillclinic.svg" alt="Audited by SkillClinic"></a>
</p>

<p align="center">
  <a href="https://github.com/Dongdarealest/skillclinic/blob/main/REGISTRY.md"><img src="https://raw.githubusercontent.com/Dongdarealest/skillclinic/main/assets/audited-plaque.svg" alt="The SkillClinic audited plaque: the mark of a checked skill" width="560"></a>
</p>

Projects that pass the audit earn this plaque. The picture alone proves nothing, and anyone can paste one: the proof is the entry in the registry, kept live at [dongdarealest.github.io/skillclinic](https://dongdarealest.github.io/skillclinic/).

Skills are instruction files your AI loads and follows, often at the start of every conversation. Most people install them from repositories, gists, and chat messages without ever reading them. SkillClinic reads them for you. This is what an audit looks like:

<p align="center">
  <img src="https://raw.githubusercontent.com/Dongdarealest/skillclinic/main/assets/demo.png" alt="SkillClinic demo output: one clean skill passes, an invalid skill and a risky skill fail with reasons" width="880">
</p>

<p align="center"><em>One clean skill passes. Two fail, every failure with its reason and its fix.</em></p>

```text
$ skillclinic --demo

FAIL  Invalid_Skill Name
      folder: examples/invalid-skill
      score: 25 (F)
      - [error] name is not kebab-case: Invalid_Skill Name
        fix: Rename the skill with lowercase words joined by hyphens.

FAIL  risky-skill
      folder: examples/risky-skill
      score: 0 (F)
      - [high] security: skill pipes a network download straight into a shell
        fix: Never pipe a download into a shell. Download the file, read it,
        then decide whether to run it.
      - [high] security: skill instructs reading or sending credential material
        fix: Remove the credential access. A skill should ask the user,
        never read secret stores.

OK    clean-skill
      score: 100 (A)

Summary: 3 skills, 1 OK, 0 WARN, 2 FAIL
Health score: 42/100 (D)
```

## Quick start

```bash
pip install skillclinic   # the skillclinic package installs the skillclinic command
skillclinic                # audit the skill folders on this machine
skillclinic --demo         # see it work in ten seconds on the bundled examples
```

Point it at any folder to audit just that folder, and add `--json` for machine readable output in scripts and CI. No installer fan? The whole tool is one file: download `skillclinic.py` from this repo and run it the same way. It needs Python 3.10 or newer and nothing else.

<details>
<summary>One line installers, pinned and checksum verified</summary>

<br>

```bash
curl -fsSL https://raw.githubusercontent.com/Dongdarealest/skillclinic/v0.4.6/install.sh | bash
```

```powershell
irm https://raw.githubusercontent.com/Dongdarealest/skillclinic/v0.4.6/install.ps1 | iex
```

Both installers are pinned to the v0.4.6 release: they download `skillclinic.py` and its published SHA-256 as assets of that release and check the two match before installing, refusing on any mismatch. The tool audits installers it would not trust, so its own had to pass.

</details>

## What it checks

| Check | What it catches |
| --- | --- |
| Validity | Frontmatter that does not parse, missing name or description, names that are not kebab-case or do not match their folder, names and descriptions over the spec length limits |
| Security | Downloads piped into a shell, instructions touching credential stores, language that sends user data out, prompt override phrases, uninspectable base64 blobs, destructive commands, invisible Unicode characters, and the same patterns in the text files bundled with a skill |
| Conflicts | The same skill name installed in several host folders, near-duplicate descriptions that make hosts load the wrong skill. Skills namespaced inside a plugin, and the distribution copies inside one collection, are not conflicts |
| Token cost | Always-on tokens (the name and description a host loads into every conversation) counted apart from body tokens, which load only when a skill runs |
| Sample data | Skills found under `examples/`, `fixtures/` or `testdata/` folders are exhibits, not installations: they are listed in the report as not audited and are never scored, given a verdict, or entered into the conflict checks |

## Reading the report

- **OK**: the skill parses, identifies itself properly, and shows no risky patterns.
- **WARN**: worth a human look, for example a reference to a credential store or a very long file.
- **FAIL**: broken or dangerous. The report exits with code 1 when any skill fails, so it drops straight into CI.

Every skill also gets a score out of 100 and a letter grade, and so does the whole installation. Most findings carry a fix line that says exactly what to change, so the report reads as a work list, not just a verdict.

## Removing what fails

Finding a bad skill is only half the job, so SkillClinic can clear it out too. Removal is deliberately boring and reversible:

```bash
skillclinic --quarantine-failed   # move every FAIL skill out of its host folder
skillclinic --restore             # put the last batch back
```

Nothing is deleted outright. Failed skills move to `~/.skillclinic/quarantine` in a dated batch with a manifest of where each one came from, and `--restore` puts the most recent batch back exactly where it was. Only FAIL verdicts are moved; a WARN is a judgment call, and judgment calls stay yours. Add `--yes` to skip the confirmation prompt in scripts.

---

## The State of Public Skills

We pointed SkillClinic at the six biggest public skill collections. One in three skills failed.

<table align="center">
  <tr>
    <td align="center"><h2>777</h2>skills audited</td>
    <td align="center"><h2>267</h2>failed the audit</td>
    <td align="center"><h2>8</h2>carried the highest severity pattern</td>
  </tr>
</table>

The curated collections are nearly clean. The failures concentrate in the largest one, where duplicated skills and credential references pile up.

| Collection | Health |
| --- | --- |
| obra/superpowers | 100/100 |
| mattpocock/skills | 99/100 |
| anthropics/skills | 97/100 |
| K-Dense-AI/scientific-agent-skills | 96/100 |
| addyosmani/agent-skills | 92/100 |
| affaan-m/ECC | 76/100 |

Full method, findings, and limits: [The State of Public Skills](AUDIT.md).

---

## Show your audit

Publish skills of your own? A collection that passes the audit earns the plaque shown at the top of this page. Listings carry only the score their own repo's audit produced, a listing by hand is added only after the maintainers re-run the audit and the results match, and a daily re-audit keeps every listed badge honest after that.

Yours is served live, plaque and badge alike, from an address that carries your own GitHub identity:

```
https://skilldoctor-badges.vercel.app/badges/<owner>--<repo>.svg
```

Paste it into your README:

```markdown
[![Audited by SkillClinic](https://skilldoctor-badges.vercel.app/badges/<owner>--<repo>.svg)](https://dongdarealest.github.io/skillclinic/)
```

That paste is the whole enrollment. A daily job searches GitHub for the badge address, reads the owner and repo out of the address itself, audits that repo, and lists it in the registry with its real score. A brand new badge can take some hours to be discovered, while GitHub indexes it. Until the first verification the address serves a pending design, so it never renders as a broken image; from then on it serves the current result, and if the project stops passing it flips to a grey recheck design until it passes again. Take the badge out of your README and the listing is dropped on the next run. The generator on the [registry page](https://dongdarealest.github.io/skillclinic/) builds the ready to paste snippet for you, and the same address with `-plaque` before `.svg` gives the large format, for a place of honor.

This is a real one, SkillPort's badge, served live:

[![Audited by SkillClinic](https://skilldoctor-badges.vercel.app/badges/Dongdarealest--skillport.svg)](https://dongdarealest.github.io/skillclinic/)

[REGISTRY.md](REGISTRY.md) describes how verification works in full. For announcements and offline use, `skillclinic <folder> --write-badge` writes a dated static snapshot of the badge, the plaque, and the machine report instead; a failing audit writes nothing. The plain mark at [badges/audited.svg](https://skilldoctor-badges.vercel.app/badges/audited.svg) carries no score and enrolls nothing; only the personal address is an enrollment.

SkillClinic wears the small badge in the row at the top of this page, and it does not flatter itself: this repo carries no skills of its own, only the demo fixtures under `examples/`, so its badge shows the no skills state, and those fixtures are listed as not audited in every report rather than scored.

## In CI, and as a GitHub Action

This repo doubles as a GitHub Action, so a collection can audit itself on every push:

```yaml
- uses: Dongdarealest/skillclinic@v0.4.6
```

It audits the repository (or the folder given in the `path` input) and fails the build when any skill fails. Anywhere else, the plain command does the same job in CI: `skillclinic --json` for machines, exit code 1 on any FAIL.

## Why this exists

Public skill collections are growing faster than anyone can review them, and audits of popular collections keep finding files that are invalid, duplicated, or carry instructions no user would accept if they read them. Installing a skill is trusting a stranger's instructions inside your own AI. A checkup should take ten seconds, so here it is.

---

## Support

SkillClinic is free and MIT licensed. If it saved you from one bad install, a coffee keeps the next check coming.

<p>
  <a href="https://github.com/sponsors/Dongdarealest"><img src="https://img.shields.io/badge/GitHub%20Sponsors-141414?style=for-the-badge&logo=githubsponsors&logoColor=EA4AAA" alt="Sponsor on GitHub"></a>
  <a href="https://ko-fi.com/dongdarealest"><img src="https://img.shields.io/badge/Ko--fi-141414?style=for-the-badge&logo=kofi&logoColor=FF5E5B" alt="Buy me a coffee on Ko-fi"></a>
</p>

## Contributing

New checks are the most welcome contributions, especially patterns for risks this version does not catch yet. Open an issue with the skill that slipped through, or send a pull request with a test that proves the new check works. Questions and ideas are welcome in [Discussions](https://github.com/Dongdarealest/skillclinic/discussions).

## License

MIT. See [LICENSE](LICENSE).
