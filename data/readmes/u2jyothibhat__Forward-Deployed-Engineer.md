# Forward Deployed Engineer: Code and Labs

Companion code for the book **Forward Deployed Engineer: Building, deploying and operating AI systems inside the enterprise, on AWS, Azure and Google Cloud** by **Jyothi Kodenkiri**. It is the first book in the *AI and Cloud Technology* series.

- Paperback and Kindle on Amazon: <https://www.amazon.com/dp/B0HNSNJLWD/>
- Book 2, *Site Reliability Engineering for AI*: <https://www.amazon.com/dp/B0HNT8Z95S/>, with its code at <https://github.com/u2jyothibhat/Site-Reliability-Engineering-for-AI>

Every code listing printed in the book is in this repository, organised chapter by chapter. The layout matches the `fde-labs` project you build in Chapter 5, so you can clone it and follow the labs without retyping anything.

## Get started

```bash
git clone https://github.com/u2jyothibhat/Forward-Deployed-Engineer.git fde-labs
cd fde-labs
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # then fill in your cloud and model settings
set -a; source .env; set +a
python smoke_test.py        # Chapter 5: check the model client works
```

Run everything from the repository root so imports such as `from fde_kit.llm import get_client` resolve.

## Chapter by chapter

| Chapter | Folder | What's inside |
|---|---|---|
| 1–4 | — | No code (the role, the field and the delivery approach) |
| 5. The FDE Technical Toolkit | `fde_kit/`, `smoke_test.py`, `requirements.txt`, `.env.example`, `snippets/chapter-05/` | A provider-neutral model client for Amazon Bedrock, Azure OpenAI and Vertex AI; tool install and cloud sign-in commands |
| 6. Lab: RAG assistant on enterprise documents | `lab06_rag/` | Extract, chunk, embed into PostgreSQL with pgvector, retrieve with access control, grounded answers with citations, FastAPI service |
| 7. Lab: data pipelines, legacy systems and personal data | `lab07_data/` | Data contract, incremental extract, PII detection and masking (local and cloud), pipeline and quality checks |
| 8. Lab: containers, IaC and cloud deployment | `lab08_deploy/`, `snippets/chapter-08/` | Dockerfile; Terraform for AWS ECS Fargate, Azure Container Apps and Google Cloud Run; Kubernetes manifest; canary roll-outs |
| 9. Lab: CI/CD, evaluation and guardrails | `lab09_quality/`, `eval/`, `.github/workflows/`, `snippets/chapter-09/` | Evaluation set, retrieval and LLM-as-judge evaluation, a pytest quality gate, input and output guardrails, a GitHub Actions pipeline |
| 10. Lab: observability, SLOs and AIOps | `lab10_observe/`, `snippets/chapter-10/` | OpenTelemetry instrumentation, SLO burn-rate alerts, CloudWatch / Azure Monitor / Cloud Monitoring equivalents, anomaly detection, incident summaries, a runbook |
| 11. Lab: agentic AI in the field | `lab11_agents/`, `snippets/chapter-11/` | Tools with risk levels, the agent loop, argument validation, human approval, audit trail, adversarial tests |
| 12. Lab: security and compliance | `lab12_secure/`, `snippets/chapter-12/` | Token validation and identity propagation, private endpoints, customer-managed keys, cloud policy guardrails |
| Appendix C. Templates | `templates/` | Runbook, incident review, field notes and discovery templates |

[LISTINGS.md](LISTINGS.md) lists every file in book order, with the section of the book it comes from.

### Notes on the layout

- Files the book names with a path comment (for example `# lab06_rag/extract.py`) are at exactly that path.
- Shorter fragments, shell commands and cloud-specific variants sit in `snippets/chapter-NN/`, numbered in the order they appear in the chapter.
- The instrumented version of `answer.py` from Chapter 10 is in `lab10_observe/answer_instrumented.py`, so the Chapter 6 version stays as printed.
- The input and output guardrails from Chapter 9 are combined in `lab09_quality/guardrails.py`.
- The Chapter 9 evaluation set is in `eval/cases.jsonl`, which is where the workflow in `.github/workflows/deliver.yml` looks for it.
- `requirements.txt` is the one from Chapter 5, plus `jsonschema` and `PyJWT`, which Chapters 11 and 12 use.

## Before you use it for real

The labs are written to teach. They are complete enough to run, but you should adapt them before they go anywhere near production:

- Replace model IDs, regions, resource names and thresholds with the ones your organisation has approved.
- Check cloud resource arguments against current provider documentation and your Terraform provider version.
- Never commit a real `.env` file (it is in `.gitignore`), and use your cloud's secret store for anything sensitive.
- Review everything against your organisation's security, data protection and change management controls.

## Errata and updates

Cloud and AI services change quickly. If something no longer works, please open an issue in this repository. Updates to the code will be made here.

## Licence

The code in this repository is released under the MIT Licence (see [LICENSE](LICENSE)). The book text and figures remain © 2026 Jyothi Kodenkiri, all rights reserved.
