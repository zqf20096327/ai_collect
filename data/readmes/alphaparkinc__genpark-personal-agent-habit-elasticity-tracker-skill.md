# genpark-personal-agent-habit-elasticity-tracker-skill

![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Dependencies](https://img.shields.io/badge/dependencies-zero-success)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

GenPark Personal Agent Habit Elasticity Tracker implements Phillippa Lally's habit automaticity curves and behavioral friction elasticity to build unshakeable personal routines.

```mermaid
flowchart TD
    A[Habit Practice Days & Consistency] --> B[Lally Automaticity Kinetic Solver]
    B --> C[Automaticity Score & Second-Nature Plateau Date]
    D[Friction Barrier Interventions] --> E[Behavioral Price Elasticity Estimator]
    F[User Current Energy State] --> G[Minimum Viable Micro-Habit Deriver]
    C & G --> H[Continuous Unbroken Identity Streak]
```

## Features
- **Lally Automaticity Curve**: Forecasts days until a habit becomes effortless based on complexity tier.
- **Friction Elasticity Metric**: Quantifies how friction reductions directly multiply completion rates.
- **Streak Preserver Downscaling**: Protects habits on exhausting days with scientifically scaled micro-doses.

## Quickstart

```python
from client import PersonalAgentHabitElasticityTracker

tracker = PersonalAgentHabitElasticityTracker()
res = tracker.model_habit_automaticity_curve(45, 0.90)
print("Automaticity Level:", res["automaticity_score"])
```

## FastMCP Integration

```bash
python -m genpark-personal-agent-habit-elasticity-tracker-skill.mcp_server
```

## License
MIT
