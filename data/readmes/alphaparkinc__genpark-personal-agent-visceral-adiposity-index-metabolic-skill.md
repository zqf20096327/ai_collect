# Personal Agent Visceral Adiposity Index Metabolic Skill

[![OpenClaw Ecosystem](https://img.shields.io/badge/OpenClaw-Ecosystem-blue.svg)](https://github.com/Alpha-Park)
[![Dual-Org Sync](https://img.shields.io/badge/GitHub-Dual--Org_Mirrored-success.svg)](https://github.com/alphaparkinc)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard_Library_Only-brightgreen.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/Protocol-MCP_Native-orange.svg)](https://modelcontextprotocol.io/)
[![Production Grade](https://img.shields.io/badge/Status-100%25_Grade_A_Verified-success.svg)](https://github.com/Alpha-Park)

Zero-dependency Amato Visceral Adiposity Index (VAI) calculator, Lipid Accumulation Product (LAP) modeler, and visceral adipose tissue (VAT) ectopic dysfunction risk evaluator.

## Architecture

```mermaid
flowchart TD
    BiomarkerInput[Waist Circumference, BMI, Triglycerides, HDL, Sex] --> VAIEngine[Amato VAI Mathematical Modeler]
    VAIEngine --> UnitConversion[TG & HDL mg/dL to mmol/L]
    UnitConversion --> GenderFormulas[Sex-Specific Denominators & Transporter Multipliers]
    GenderFormulas --> VAIScore[Visceral Adiposity Index: VAI Score]
    GenderFormulas --> LAPScore[Lipid Accumulation Product: LAP Score]
    VAIScore --> Stratification[Cardiometabolic & Hepatic Steatosis Risk Tier]
    Stratification --> DepletionPrescription[Fasted Zone 2 Lipolysis & Fasting Window Strategy]
```

## Quickstart

```python
from client import PersonalAgentVisceralAdiposityIndexMetabolic

agent = PersonalAgentVisceralAdiposityIndexMetabolic()
res = agent.calculate_visceral_adiposity_index(waist_circumference_cm=88.0, bmi=24.5, triglycerides_mg_dl=110.0, hdl_mg_dl=52.0)
print(f"VAI: {res['visceral_adiposity_index_vai']} | Tier: {res['visceral_fat_risk_tier']}")
```
