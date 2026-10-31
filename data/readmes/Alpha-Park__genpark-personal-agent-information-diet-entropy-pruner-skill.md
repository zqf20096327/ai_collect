# genpark-personal-agent-information-diet-entropy-pruner-skill

![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Dependencies](https://img.shields.io/badge/dependencies-zero-success)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

GenPark Personal Agent Information Diet Entropy Pruner applies Shannon information theory, Jaccard lexical novelty metrics, and decibel SNR modeling to optimize personal reading diets.

```mermaid
flowchart TD
    A[Daily Ingested Reading & Media Stream] --> B[Category Distribution Histogram]
    B --> C[Shannon Information Entropy H]
    D[Pairwise Article Token Sets] --> E[Jaccard Redundancy & Echo Chamber Auditor]
    F[Source Insight vs Noise Densities] --> G[Decibel SNR Ranking Solver]
    C & E & G --> H[Pruning Recommendations & High-Signal Curation]
```

## Features
- **Shannon Entropy Scoring**: Quantifies intellectual breadth and flags doomscroll concentration.
- **Echo Chamber Jaccard Metric**: Detects repackaged duplicate ideas across different media outlets.
- **Decibel SNR Filtering**: Surfaces high-density thought leadership while pruning low-signal noise.

## Quickstart

```python
from client import PersonalAgentInformationDietEntropyPruner

pruner = PersonalAgentInformationDietEntropyPruner()
res = pruner.rank_content_sources_snr([{"name": "Research", "insight_density": 0.9, "noise_density": 0.1}])
print("SNR:", res["sources_ranked"][0]["snr_db"], "dB")
```

## FastMCP Integration

```bash
python -m genpark-personal-agent-information-diet-entropy-pruner-skill.mcp_server
```

## License
MIT
