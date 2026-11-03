# Personal Agent Cold Pressor Pain Endurance Skill

[![OpenClaw Ecosystem](https://img.shields.io/badge/OpenClaw-Ecosystem-blue.svg)](https://github.com/Alpha-Park)
[![Dual-Org Sync](https://img.shields.io/badge/GitHub-Dual--Org_Mirrored-success.svg)](https://github.com/alphaparkinc)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard_Library_Only-brightgreen.svg)](https://www.python.org/)
[![Model Context Protocol](https://img.shields.io/badge/Protocol-MCP_Native-orange.svg)](https://modelcontextprotocol.io/)
[![Production Grade](https://img.shields.io/badge/Status-100%25_Grade_A_Verified-success.svg)](https://github.com/Alpha-Park)

Zero-dependency Cold Pressor Test (CPT) pain threshold and tolerance modeler, central autonomic pain gating quantifier, and sympathetic withdrawal recovery evaluator.

## Architecture

```mermaid
flowchart TD
    ColdWater[Water Temp, Threshold Latency, Tolerance Latency, VAS] --> CPTEngine[Cold Pressor Pain Gating Engine]
    CPTEngine --> PSIModeler[Pain Sensitivity Index: PSI]
    CPTEngine --> GatingTier[Central Pain Gating Tier: Elite to Sensitized]
    PostStressHR[Peak HR, 1-Min Recovery HR, 2-Min Recovery HR] --> VagalKinetics[Vagal Reactivation Modeler]
    VagalKinetics --> AutonomicScore[Autonomic Recovery Index & Sympathetic Withdrawal]
```

## Quickstart

```python
from client import PersonalAgentColdPressorPainEndurance

agent = PersonalAgentColdPressorPainEndurance()
res = agent.evaluate_cpt_pain_tolerance(water_temp_celsius=3.0, pain_threshold_seconds=20.0, pain_tolerance_seconds=80.0)
print(f"PSI: {res['pain_sensitivity_index_psi']} | Gating: {res['central_pain_gating_tier']}")
```
