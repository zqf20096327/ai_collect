# Agentic SDLC Starter

Reference architecture for spec-driven, AI-assisted software development using GitHub Copilot, MCP, and repo-based context engineering.

## What Is This?

A 5-step AI pipeline that turns **PRD + User Stories → Production-Ready Code** using GitHub Copilot as the code generation engine. Each step is a specialized agent prompt that reads structured inputs and produces structured outputs.

```
PRD + TDD + User Stories
        ↓
  ┌─────────────┐
  │ 01 Assessor  │  → Finds gaps, ambiguities, conflicts
  └──────┬──────┘
         ↓
  ┌──────────────┐
  │ 01b Resolver │  → Answers questions from source docs
  └──────┬───────┘
         ↓
  ┌──────────────┐
  │ 02 Specifier │  → Generates machine-readable specs
  └──────┬───────┘
         ↓
  ┌──────────────┐
  │ 03 Generator │  → Produces code from specs only
  └──────┬───────┘
         ↓
  ┌──────────────┐
  │ 04 Validator │  → Reviews code against specs + guardrails
  └──────────────┘
```

## Quick Start

### 1. Clone and Configure

```bash
git clone https://github.com/microsoft/agentic-sdlc-starter.git
cd agentic-sdlc-starter
```

### 2. Configure for Your Project

Edit `agentic-config.yml` with your project details:

```yaml
company_name: "Contoso Healthcare"
project_name: "Payer Contract Intelligence"
industry: "healthcare"
sensitive_data_label: "PHI/PII"
compliance_terms: "PHI/PII, HIPAA"
```

Then run:

```bash
bash scripts/bootstrap.sh
```

This replaces all `{{PLACEHOLDER}}` tokens across prompts, guardrails, and scripts in one shot.

| Placeholder | What It Sets | Example |
|---|---|---|
| `{{COMPANY_NAME}}` | Organization name | `Contoso Healthcare` |
| `{{PROJECT_NAME}}` | Project name | `Payer Contract Intelligence` |
| `{{INDUSTRY}}` | Industry/domain | `healthcare`, `financial services`, `government` |
| `{{SENSITIVE_DATA_LABEL}}` | Sensitive data term | `PHI/PII`, `PCI/PII`, `CUI` |
| `{{COMPLIANCE_TERMS}}` | Compliance frameworks | `PHI/PII, HIPAA`, `SOC2, PCI-DSS` |

### 3. Add Your Inputs

Create your project-specific input documents:

```
ado/
  sprint-1/
    PRD.md                  ← Your Product Requirements Document
    Technical_Design_Document.md  ← Your Technical Design Document
    USER_STORIES.md         ← Your sprint user stories (from ADO/Jira/etc.)
```

### 4. Customize Guardrails

Edit `.github/copilot-instructions.md` to match your project:

- **Tech stack** — update language, framework, database, etc.
- **Architecture** — adjust layers, patterns, dependency rules
- **Security** — set your compliance requirements (HIPAA, SOC2, etc.)
- **Coding standards** — your team's conventions and rules

### 5. Run the Pipeline

Run each prompt sequentially in GitHub Copilot Chat (or any LLM with file access):

| Step | Prompt File | What It Does | Output |
|---|---|---|---|
| 1 | `prompts/01-assessor.md` | Analyzes inputs, finds gaps | `pipeline/01-assessment/assessment-report.md` |
| 1b | `prompts/01b-resolver.md` | Resolves questions from docs | `pipeline/01-assessment/assessment-decisions.md` |
| 2 | `prompts/02-specifier.md` | Generates detailed specs | `pipeline/02-specification/*.md` + `specs/*.md` |
| 3 | `prompts/03-generator.md` | Generates code from specs | `src/` |
| 4 | `prompts/04-validator.md` | Reviews code vs specs | `pipeline/04-review/review-checklist.md` |

**How to run a step:**
1. Open the prompt file (e.g., `prompts/01-assessor.md`)
2. Copy the full content into GitHub Copilot Chat (or paste as a system prompt)
3. The agent reads the source files listed at the top and generates the outputs
4. Review the output before proceeding to the next step

## Project Structure

```
.github/
  copilot-instructions.md   ← Coding guardrails (tech stack, architecture, rules)
prompts/
  01-assessor.md             ← Step 1: Gap analysis
  01b-resolver.md            ← Step 1b: Resolution gate
  02-specifier.md            ← Step 2: Spec generation
  03-generator.md            ← Step 3: Code generation
  04-validator.md            ← Step 4: Code review
ado/                         ← Your input documents (add these)
  sprint-1/
    PRD.md
    Technical_Design_Document.md
    USER_STORIES.md
pipeline/                    ← Generated outputs land here
  01-assessment/
  02-specification/
  04-review/
specs/                       ← Final specs (copied from pipeline)
src/                         ← Generated source code
```

## Key Concepts

### Zero-Assumption Principle
The pipeline never guesses. Every ambiguity is flagged, documented, and resolved before code generation. This prevents the #1 cause of AI-generated code failures: building confidently on wrong assumptions.

### Spec-Driven Generation
The Generator (Step 3) reads **only** the specs and copilot-instructions — it never sees the PRD or TDD directly. This forces the Specifier (Step 2) to be exhaustive. If it's not in the specs, it doesn't get built.

### Resolution Gate
Between assessment and specification, the Resolver checks every flagged question against source documents. This can be automated (agent resolves from docs), human-gated (PR review), or hybrid. The pipeline just reads `assessment-decisions.md` — it doesn't care who wrote it.

## Adapting for Your Stack

The included copilot-instructions are configured for Python/FastAPI/Neo4j. To adapt:

1. Replace the tech stack section with your stack
2. Update architecture patterns (Clean Architecture layers, dependency rules)
3. Adjust security/compliance rules for your industry
4. Update testing requirements and conventions

The **prompts are stack-agnostic** — they work with any language or framework. Only `copilot-instructions.md` is stack-specific.

## License

MIT — see [LICENSE](LICENSE).
