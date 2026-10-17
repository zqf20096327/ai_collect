# Construction Gamma Skills Library

AI-powered construction management skills for [Claude Cowork](https://claude.ai) by [Construction Gamma](https://www.constructiononclaude.com).

## What's Included

### 47 Domain Skills

**Project Management & Coordination** (11 skills)
Schedule Management (CPM) · Subcontractor Management · Construction Safety Management · Quality Control & Closeout · Commissioning & Closeout · Claims & Delay Documentation · Contract Administration · Owner/Stakeholder Communication · Preconstruction & Estimating · Procore Project Management · VDC/BIM Coordination

**Trades & Building Systems** (14 skills)
Structural Trades · Mechanical/Plumbing Systems · Electrical Systems · Fire Protection Systems · Building Envelope & Exterior · Interior Finishes & Trades · Doors, Frames & Hardware · Low Voltage Technology · Elevators & Vertical Transportation · Equipment (Division 11) · Specialties (Division 10) · Site Improvements (Division 32) · Early Phase & Enabling Trades · Sustainable Systems

**Building & Project Types** (22 skills)
Healthcare/Medical · Higher Education · K-12 Education · Data Center · Hospitality · Multifamily Residential · Industrial/Warehouse/Distribution · Life Sciences/Lab · Ground-Up Office/Mixed-Use · Heavy Civil/Infrastructure · Historic Renovation/Adaptive Reuse · Correctional/Detention · Cultural/Museum · Military/DoD · Parking Structures · Power/Energy · Public/Civic · Religious/Houses of Worship · Retail/Commercial Interiors · Senior Living/Assisted Living · Sports/Entertainment · Water/Wastewater

### 5 Slash Commands
- `/rfi-analysis` — Analyze RFIs, find bottlenecks, draft follow-ups
- `/daily-log-summary` — Generate daily reports from Procore logs
- `/owner-update` — Draft professional owner update emails
- `/submittal-review` — Review submittal status and deadlines
- `/safety-report` — Weekly safety summary from project data

### Procore Integration
When connected via Construction Gamma, all commands can pull live data from your Procore projects.

## Installation

### Via Construction Gamma (recommended — includes Procore integration)
1. Sign up at [constructiononclaude.com](https://www.constructiononclaude.com)
2. Connect your Procore account
3. Copy your marketplace URL from the Plugins page
4. In Cowork: `/plugin marketplace add <your-url>`

### Direct (skills only, no live Procore data)
```
/plugin marketplace add Construction-Gamma/construction-gamma-skills
/plugin install construction-intelligence
```

## License

© Construction Gamma. All rights reserved.
