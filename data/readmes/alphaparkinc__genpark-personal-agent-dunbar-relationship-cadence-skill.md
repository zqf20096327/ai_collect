# genpark-personal-agent-dunbar-relationship-cadence-skill

![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Dependencies](https://img.shields.io/badge/dependencies-zero-success)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

GenPark Personal Agent Dunbar Relationship Cadence organizes personal contacts into Dunbar's concentric circles, computes relationship half-life decay, and schedules intentional reconnections without social spam.

```mermaid
flowchart TD
    A[Personal Contact Log & Closeness Scores] --> B[Dunbar Concentric Layer Classifier]
    B --> C[Support Clique 5 / Sympathy 15 / Affinity 50]
    D[Days Since Last Meaningful Touchpoint] --> E[Exponential Relationship Half-Life Decay Solver]
    E --> F[Warmth & Social Drift Risk Assessment]
    F --> G[Weekly Mindful Reconnection Schedule]
```

## Features
- **Dunbar Circle Mapping**: Classifies close friends vs broader network according to anthropological Dunbar constraints.
- **Half-Life Warmth Decay**: Models realistic relationship entropy over time without artificial pressure.
- **Mindful Reconnection Cadence**: Schedules authentic touchpoints within user-defined weekly cognitive bandwidth.

## Quickstart

```python
from client import PersonalAgentDunbarRelationshipCadence

cadence = PersonalAgentDunbarRelationshipCadence()
res = cadence.classify_dunbar_layer_and_cadence("friend_1", 0.90, 14)
print("Warmth Level:", res["relationship_warmth_level"])
```

## FastMCP Integration

```bash
python -m genpark-personal-agent-dunbar-relationship-cadence-skill.mcp_server
```

## License
MIT
