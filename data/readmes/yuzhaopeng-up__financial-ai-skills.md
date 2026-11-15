# Financial AI Skills

> **6大财务场景 + 8大财富场景 + 9大风控场景 AI 智能体，纯 Python 实现，零 API 费用，毫秒级响应**
>
> 发票查验 · 预算管控 · 财报速读 · 税务筹划 · 费用报销 · 资金预测 · 资产配置 · 风险评估

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/yuzhaopeng-up/financial-ai-skills?style=social)](https://github.com/yuzhaopeng-up/financial-ai-skills/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/yuzhaopeng-up/financial-ai-skills)](https://github.com/yuzhaopeng-up/financial-ai-skills/commits/main)
[![Issues](https://img.shields.io/github/issues/yuzhaopeng-up/financial-ai-skills)](https://github.com/yuzhaopeng-up/financial-ai-skills/issues)
[![Release](https://img.shields.io/github/v/release/yuzhaopeng-up/financial-ai-skills)](https://github.com/yuzhaopeng-up/financial-ai-skills/releases)

**If you find this useful, please give it a Star! Your support drives continuous improvement.**

---

## Why Financial AI Skills?

- **Zero API Cost**: Pure rule engines, no external API calls, ideal for high-frequency scenarios
- **Millisecond Response**: Local computation, average response < 100ms
- **Zero Dependencies**: Python standard library only, no pip install needed
- **IM-Friendly Output**: Native Markdown tables, perfect for WeCom/Feishu/DingTalk
- **104 Skills Ready**: Covering 4 major financial domains with 6+8+9+5+18+3+3 capability modules

---

## Quick Start (30 seconds)

```bash
# Clone
git clone https://github.com/yuzhaopeng-up/financial-ai-skills.git
cd financial-ai-skills

# Run immediately - no pip install needed!
cd skills/financial-intelligence/scripts

# Invoice verification
python3 financial_cli.py invoice 011001900111 12345678

# Budget control
python3 financial_cli.py budget 市场部

# Financial report analysis
python3 financial_cli.py report 美的集团 2025
```

<details>
<summary>Python API usage (click to expand)</summary>

```python
import sys
sys.path.insert(0, "skills/financial-intelligence")

from engines import InvoiceEngine, BudgetEngine, ReportEngine
from formatters import FinancialFormatter

# Invoice verification
engine = InvoiceEngine()
result = engine.verify("011001900111", "12345678")
print(FinancialFormatter.format_invoice(result))

# Budget analysis
engine = BudgetEngine()
result = engine.analyze(dept="市场部")
print(FinancialFormatter.format_budget(result))
```

</details>

---

## Live Demos

### Invoice Verification - 3 seconds to identify authenticity

```markdown
## Invoice Verification Result

**Result: Authentic**

| Field | Value |
|-------|-------|
| Invoice Code | 011001900111 |
| Invoice Number | 12345678 |
| Issuer | Beijing XX Technology Co., Ltd. |
| Amount | ¥12,580.00 |
| Total with Tax | **¥13,335.66** |

**Compliance Status**: Passed (Score: 100/100)
```

### Budget Control - Overspend warnings at a glance

| Category | Budget | Spent | Projected | Status |
|----------|--------|-------|-----------|--------|
| Travel | ¥150,000 | ¥168,000 | ¥185,000 | Over Budget |
| Advertising | ¥200,000 | ¥145,000 | ¥195,000 | Near Limit |

### Enterprise Risk Assessment

| Risk Type | Level | Description |
|-----------|-------|-------------|
| Market Risk | Medium | EV market competition intensifying |
| Supply Chain Risk | Medium | Battery raw material price volatility |
| Financial Risk | Low | Cash flow sufficient, debt ratio reasonable |

---

## Published Skills

| Skill | Scenarios | Core Capabilities | Status |
|-------|-----------|-------------------|--------|
| [financial-intelligence](skills/financial-intelligence/) | 6 | Invoice verification, Budget control, Financial report, Tax planning, Expense audit, Cash flow forecast | Released |
| [wealth-management](skills/wealth-management/) | 8 | Asset allocation, Financial health, Retirement planning, Insurance planning, Tax optimization, Education fund, Housing plan, Robo-advisor | Released |
| [risk-compliance](skills/risk-compliance/) | 9 | Enterprise risk, Credit rating, Anti-fraud, Compliance check, Financial diagnosis, Regulatory policy, Post-loan monitoring, Supply chain risk, Market sentiment | Released |
| [wecom-template-card](skills/wecom-template-card/) | 5 | Due diligence card, Market flash card, Risk alert card, Report card, Confirmation card | Released |
| [customer-marketing](skills/customer-marketing/) | 18 | Marketing scripts, Objection handling, Multi-style adaptation, Dialect scripts | Released |
| [product-manual-rag](skills/product-manual-rag/) | 3+ | Product manual Q&A (BM25+TF-IDF RAG), Source annotation, Auto product ID, Hit@1=100% | Released |
| [application-material-checker](skills/application-material-checker/) | 3 | Material auto-check, Completeness + compliance, 18 business rules, 4 report formats | Released |

---

## Technical Features

- **Zero API Cost**: Pure rule engines, no external API calls
- **Millisecond Response**: Local computation, average < 100ms
- **IM-Friendly Output**: Native Markdown tables for enterprise IM
- **Modular Design**: Each engine is independent and composable
- **Built-in Demo Data**: Mock data included, no configuration needed
- **Zero Dependencies**: Python standard library only
- **Knowledge Hub Integration**: Auto-sync GitHub Stars, articles, node status to Feishu

---

## Project Structure

```
financial-ai-skills/
├── skills/
│   ├── financial-intelligence/     # Financial Intelligence (6 engines)
│   ├── wealth-management/          # Wealth Management (8 capabilities)
│   ├── risk-compliance/            # Risk & Compliance (9 capabilities)
│   ├── wecom-template-card/        # WeCom Template Cards
│   ├── customer-marketing/         # Customer Marketing (18 scenarios)
│   ├── product-manual-rag/         # Product Manual RAG
│   └── application-material-checker/ # Application Material Checker
├── scripts/                        # Automation scripts
├── .github/workflows/              # GitHub Actions
├── docs/                           # Documentation
├── LICENSE
└── README.md
```

---

## Ecosystem

Part of the **Agent Skills** open-source ecosystem - 9 repositories covering the full Agent development lifecycle:

| Repository | Focus | Skills/Demos | Key Capabilities |
|------------|-------|-------------|------------------|
| **[financial-ai-skills](https://github.com/yuzhaopeng-up/financial-ai-skills)** (this repo) | Financial Industry | 104 Skills | Invoice, Budget, Risk, Wealth |
| **[teleagent-skills](https://github.com/yuzhaopeng-up/teleagent-skills)** | General Business | 5 Skills | Scoring engine, Evidence chain, Data aggregator, NL2Query, Visualization |
| **[agent-cluster-comm](https://github.com/yuzhaopeng-up/agent-cluster-comm)** | Agent Communication | 5 Skills | Encrypted P2P, Redis bus, Group bot, GitHub async, Health monitor |
| **[skill-framework](https://github.com/yuzhaopeng-up/skill-framework)** | Governance Framework | 208 cataloged | L0-L4 classification, YAML templates, Governance tools |
| **[fintech-h5-demos](https://github.com/yuzhaopeng-up/fintech-h5-demos)** | Financial Dashboards | 57 demos | Zero-dependency HTML, Interactive financial visualizations |
| **[soe-compliant-office](https://github.com/yuzhaopeng-up/soe-compliant-office)** | SOE-Compliant Office | 17 Skills | Built-in compliance, Audit trail, National standards |
| **[regulated-rag](https://github.com/yuzhaopeng-up/regulated-rag)** | RAG Toolkit | 1 toolkit | BM25+TF-IDF+RRF, Zero-dependency, No vector DB |
| **[agent-ops-toolkit](https://github.com/yuzhaopeng-up/agent-ops-toolkit)** | Agent Infrastructure | 1 toolkit | Cross-channel routing, Document pipelines, Alerting |

```
+---------------------------------------------------------------+
|                    Agent Skills Ecosystem                      |
+----------------+------------------+--------------------------+
| Industry Layer |  General Layer    |  Infrastructure Layer   |
| 104+17 Skills  |  5+1 Skills      |  5+1 Skills              |
|                |                  |                          |
| Finance        | Scoring Engine   | Encrypted P2P            |
| Wealth         | Evidence Chain   | Redis Message Bus        |
| Risk           | Data Aggregator  | Group Bot                |
| SOE Office     | NL2Query        | GitHub Async             |
| Marketing      | Visualization    | Health Monitor           |
|                | RAG Toolkit      | Ops Toolkit              |
+----------------+------------------+--------------------------+
```

---

## Contributing

Contributions are welcome! Please:

1. Ensure code is desensitized (no internal company information)
2. New engines must include `format_xxx` formatter methods
3. Run `python -m py_compile` before submitting
4. Update SKILL.md documentation

**How to write an Agent Skill?** See our guide: [How to Write an Agent Skill: From Zero to One](https://github.com/yuzhaopeng-up/financial-ai-skills/wiki)

**Found a bug?** [Open an Issue](https://github.com/yuzhaopeng-up/financial-ai-skills/issues/new)

**Want to contribute?** [Submit a PR](https://github.com/yuzhaopeng-up/financial-ai-skills/compare)

---

## License

[MIT License](LICENSE) - Free to use, modify, and distribute with attribution.

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yuzhaopeng-up/financial-ai-skills&type=Date)](https://star-history.com/#yuzhaopeng-up/financial-ai-skills&Date)

---

**If these Skills helped you, please give it a Star!** It takes 1 second and means a lot.

[![Star this repo](https://img.shields.io/github/stars/yuzhaopeng-up/financial-ai-skills?style=social&label=Star)](https://github.com/yuzhaopeng-up/financial-ai-skills)

> Also check out our other repos: [teleagent-skills](https://github.com/yuzhaopeng-up/teleagent-skills) | [agent-cluster-comm](https://github.com/yuzhaopeng-up/agent-cluster-comm) | [skill-framework](https://github.com/yuzhaopeng-up/skill-framework) | [fintech-h5-demos](https://github.com/yuzhaopeng-up/fintech-h5-demos) | [soe-compliant-office](https://github.com/yuzhaopeng-up/soe-compliant-office) | [regulated-rag](https://github.com/yuzhaopeng-up/regulated-rag) | [agent-ops-toolkit](https://github.com/yuzhaopeng-up/agent-ops-toolkit)