# Cheatsheet Creator Skill

AI agent skill for creating cheatsheets based on lecture notes, homeworks, and past exams.

Outputs two markdown files — a concise cheatsheet and an expanded version with italic source references back to the original slides, problem sets, and exams. Tuned for math/science (formulas, proofs, theorems) and CS/engineering (code, algorithms). Processes one file at a time so it doesn't blow past the context window on large courses.

## Download

```bash
npx skills add git@github.com:wyc79/cheatsheet-creator-skill.git
```

Or download the `cheatsheet-creator/` folder (which contains `SKILL.md`) and drop it into your agent's skills folder.

## Preferred Folder Structure

The skill works best when your course materials follow one of these conventions:

**Option A — Folder structure:**
```
my-course/
├── lectures/
│   ├── lecture_01.pdf
│   └── lecture_02.pptx
├── homework/
│   ├── hw_01.pdf
│   └── hw_01_solutions.pdf
└── exams/
    ├── midterm_2023.pdf
    └── final_2023.pdf
```

**Option B — Filename prefixes:**
```
my-course/
├── lecture_01_intro.pdf
├── lecture_02_continuity.pptx
├── hw_01.pdf
├── hw_01_solutions.pdf
├── exam_midterm_2023.pdf
└── exam_final_2023.pdf
```

If your files don't follow either, the skill will ask you to confirm classifications before parsing.

## Supported Input Formats

- PDF (text-based and scanned/handwritten)
- PPTX
- DOCX
- Standalone images of handwritten notes

## Output

The skill writes everything to a `cheatsheet/` folder:

```
cheatsheet/
├── <course>-cheatsheet.md            # concise, primary deliverable
├── <course>-cheatsheet-expanded.md   # with italic source refs (L3 slide 17), (HW2 P5), etc.
└── intermediate/                     # optional; opt out at start
    ├── lecture-summaries/
    ├── master-concepts.md
    ├── concepts-with-caveats.md
    ├── exam-frequency.md
    ├── worked-examples.md
    ├── coverage-audit.md            # self-check: is every tested problem solvable from the sheet?
    └── self-test.md                 # ablation self-test: no-sheet vs concepts-only vs full-sheet scores
```

The cheatsheet includes:
- **Concepts, formulas, definitions, theorems, algorithms** (in LaTeX / fenced code blocks where appropriate)
- **Standard problem-solving structures** — templated approaches lecturers teach (ε–δ proof skeletons, induction setups, etc.)
- **Caveats** — pitfalls and tricks mined from homework and past exams
- **Worked examples** — heavily-tested HW problems with step-by-step solutions, tagged by concept. If your materials don't include a solution, the skill proposes one and marks it `[PROPOSED — verify]`.

After building the sheet, the skill **self-checks** it (Step 5). A clean-context agent audits whether every mined exam problem is actually solvable from the sheet. Then an **ablation self-test** has cheap "student" agents attempt an exam under three conditions — no sheet (control), concepts only, and full sheet — so the score *difference* shows how much the cheatsheet itself is helping (vs. what the model already knew) and whether the worked examples earn their space. Because the control isolates the sheet's contribution, no exam needs to be held out by default (the sheet is built from all of them); holding one out is an optional stricter, out-of-sample check. Findings drive a single, size-budget-aware revision.

## Usage

Once the skill is installed, just upload your course materials and ask:

> "Make me a cheatsheet from these slides and homeworks for my final."

The agent will ask you for:
- Target size (e.g., one page, two pages, exhaustive study guide)
- Course name
- Cheatsheet rules, if any (e.g., "formulas only, no worked examples")
- Whether to save intermediate files (default: yes)
- Optionally, whether to hold out one exam for a stricter out-of-sample self-test (only relevant if you have ≥2 past exams; default: no — the self-test's control arm already isolates the sheet's value without a holdout)

Then it parses each file in turn, mines exams for emphasis, synthesizes the final cheatsheet, and self-checks it against the exams before handing it over.

## License

MIT License
