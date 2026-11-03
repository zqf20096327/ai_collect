<div align="center">

<a href="https://timbr.ai">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./.github/assets/timbr-logo-dark.png">
    <source media="(prefers-color-scheme: light)" srcset="./.github/assets/timbr-logo-light.png">
    <img alt="Timbr logo" src="./.github/assets/timbr-logo-light.png" width="220">
  </picture>
</a>

# Timbr Ontology Catalog

**Ready-to-use SQL ontologies for the Timbr semantic layer, the governed enterprise context layer for AI.**

Pick a domain, run one SQL script, map your data, and query it as a connected knowledge graph from SQL, BI tools, and AI agents.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Ontologies](https://img.shields.io/badge/ontologies-32-0a7b83.svg)](#the-catalog)
[![Timbr SQL](https://img.shields.io/badge/Timbr-SQL%20ontologies-1f6feb.svg)](https://docs.timbr.ai/doc/docs/sql/)
[![Docs](https://img.shields.io/badge/docs-docs.timbr.ai-informational.svg)](https://docs.timbr.ai/doc/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)
[![GitHub stars](https://img.shields.io/github/stars/WPSemantix/Timbr_Ontology_Catalogs?style=flat&logo=github)](https://github.com/WPSemantix/Timbr_Ontology_Catalogs/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/WPSemantix/Timbr_Ontology_Catalogs.svg)](https://github.com/WPSemantix/Timbr_Ontology_Catalogs/commits/main)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-timbr--ai-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/company/timbr-ai/)
[![YouTube](https://img.shields.io/badge/YouTube-@timbrai-FF0000?logo=youtube&logoColor=white)](https://www.youtube.com/@timbrai)
[![X](https://img.shields.io/badge/X-@timbr__ai-000000?logo=x&logoColor=white)](https://x.com/timbr_ai)

[Website](https://timbr.ai) · [Documentation](https://docs.timbr.ai/doc/) · [SQL Reference](https://docs.timbr.ai/doc/docs/sql/) · [Live Demo](https://timbr.ai/live-demos/) · [Contributing](./CONTRIBUTING.md)

</div>

---

## Table of Contents

- [SQL ontologies in Timbr](#sql-ontologies-in-timbr)
- [Quick start](#quick-start)
- [The catalog](#the-catalog)
- [Repository structure](#repository-structure)
- [Use the ontologies with AI agents](#use-the-ontologies-with-ai-agents)
- [Contributing](#contributing)
- [Support and community](#support-and-community)
- [License](#license)

---

## Summary

This repository is a library of **32 domain ontologies** written in Timbr SQL, from FIBO and FHIR to Supply Chain, Google Analytics 4 and Telecommunications. Each one models the concepts, properties, relationships, business rules and (where it applies) measures, views and cubes of a domain, so you start from a well-structured semantic model instead of a blank page.

Timbr turns these ontologies into a **virtual knowledge graph** over the data you already have. Nothing is copied or moved: Timbr maps the ontology onto your tables, then optimizes and pushes queries down to your databases, warehouses and lakehouses.

<div align="center">
  <img alt="Timbr ontology-based semantic layer architecture" src="./.github/assets/timbr-architecture.svg" width="820">
</div>

## SQL ontologies in Timbr

| | |
|---|---|
| **Semantic model** | Business concepts, hierarchies and inheritance defined once, in SQL. |
| **Relationships instead of JOINs** | Traverse the graph with `relationship[concept].property`; Timbr writes the joins. |
| **Reusable measures** | Define `total_revenue` once and use it everywhere with `AGGREGATE()`. |
| **Business rules as concepts** | Logic concepts like `late_delivery_shipment` or `high_value_customer_account`. |
| **Graph algorithms** | PageRank, Louvain, centrality and more, straight from SQL. |
| **AI-ready context** | Give LLMs and agents governed, deterministic context through MCP and SDKs. |

**Example:** revenue by customer segment in the Supply Chain model. No JOINs, no join keys to remember:

```sql
SELECT `of_customer[customer].customer_segment` AS customer_segment,
       AGGREGATE(`measure.count_of_order`)       AS number_of_orders,
       AGGREGATE(`measure.total_revenue`)        AS total_revenue
FROM dtimbr.`order`
GROUP BY `of_customer[customer].customer_segment`;
```

## Quick start

1. **Pick an ontology** from [the catalog](#the-catalog) below.
2. **Create a knowledge graph** in Timbr: *Manage → Knowledge Graphs → Create New Knowledge Graph*.
3. **Run the script.** Open *SQL Lab → SQL Editor*, select your knowledge graph, paste the model's `sql/<model>.sql` and run it.
4. **Map your data** to the concepts with `CREATE MAPPING` (most models ship structure-only). The example files include mapping templates.
5. **Query it.** Start with the model's `examples/example_queries.sql`, then explore it in the Ontology Explorer.

Each model folder has a step-by-step tutorial in `tutorial/`. New to Timbr? Start with [Ontology Modeling](https://docs.timbr.ai/doc/docs/getting-started/timbrmodeling) and [Querying the Knowledge Graph](https://docs.timbr.ai/doc/docs/getting-started/query-kg).

## The catalog

Models marked include a ready-to-run `examples/example_queries.sql`.

### Financial services

| Model | What it covers | Concepts |
|---|---|:---:|
| [FIBO](./fibo_model) | Financial Industry Business Ontology: agreements, institutions, securities, time and legal constructs | 113 |
| [Global Financial Data](./global_financial_data_model) | Global markets entities and relationships, based on LSEG (Refinitiv) data | 75 |
| [Insurance](./insurance_model) | Policies, coverages, premiums, claims, reserves and payments | 14 |
| [Asset Management](./asset_management_model) | Physical and digital assets, locations, inventory and maintenance | 8 |
| [Crunchbase](./crunchbase_model) | Startups, funding rounds, investors, acquisitions and IPOs | 67 |

### Healthcare and life sciences

| Model | What it covers | Concepts |
|---|---|:---:|
| [FHIR](./fhir_model) | HL7 FHIR resources and value sets for interoperable healthcare data | 87 |
| [Clinical Trials](./clinical_trials_model) | Studies, interventions, sites and outcomes | 33 |
| [Patient Journey](./patient_journey_model) | Conditions, encounters, care plans and treatments | 12 |
| [Gene](./gene_model) | Genetic data: biological processes, cellular components and molecular functions | 62 |

### Retail, e-commerce and supply chain

| Model | What it covers | Concepts |
|---|---|:---:|
| [Supply Chain](./supply_chain_model) | Orders, products, materials, shipments, plants and inventory, with mappings, measures and cubes | 28 |
| [E-commerce](./ecommerce_model) | Products, merchants, orders, shipments and a product tag taxonomy | 136 |
| [Retail Operations](./retail_operations_model) | Business entities, product offerings, payments and delivery logistics | 73 |
| [TPC Benchmark](./tpc_benchmark_model) | The TPC benchmark schema: customers, orders, suppliers, parts | 34 |

### Customer, marketing and digital analytics

| Model | What it covers | Concepts |
|---|---|:---:|
| [Customer 360](./customer_360_model) | Customer profiles, accounts, transactions, churn risk and retention offers | 12 |
| [Customer Service](./customer_service_model) | Accounts, service cases and feedback | 8 |
| [Marketing Campaign](./marketing_campaign_model) | Campaigns, activities, customer interactions and analytics | 12 |
| [Google Analytics 4](./google_analytics_4_model) | GA4 events, users, items, transactions, traffic sources and geo | 10 |
| [Social Network](./social_network_model) | Posts, comments, forums and connections between people | 85 |

### Media, entertainment and telecommunications

| Model | What it covers | Concepts |
|---|---|:---:|
| [Telecommunications](./telecommunications_model) | Subscribers, devices, calls, providers and contracts, with mappings and measures | 17 |
| [Media Communications](./media_communications_model) | Broadcasting, content production, advertising and audiences | 15 |
| [Media Entertainment](./media_entertainment_model) | Films, TV shows, video games and other media | 26 |
| [Film Operations](./film_operations_model) | Actors, facilities, organizational units and production processes | 23 |
| [Film Rental](./film_rental_model) | Customers, rentals, payments and film categories | 15 |

### Energy, utilities and mobility

| Model | What it covers | Concepts |
|---|---|:---:|
| [Energy Grid](./energy_grid_model) | Energy sources, power system resources and usage | 65 |
| [Utilities Management](./utilities_management_model) | Customers, service accounts, billing cycles and infrastructure projects | 22 |
| [Automotive](./automotive_model) | Vehicle production, customers and after-sales services | 14 |
| [Vehicle Accidents](./vehicle_accidents_model) | Accidents, contributing factors and the entities involved | 30 |

### Public sector and enterprise

| Model | What it covers | Concepts |
|---|---|:---:|
| [Government](./government_model) | Public assets, budgets, regulations and elections | 16 |
| [Higher Education](./higher_education_model) | Courses, students, faculty and institutions | 9 |
| [Human Resources](./human_resources_model) | Employees, departments, payroll, benefits, reviews and training | 7 |
| [Enterprise Communication](./enterprise_communication_model) | Email, chat and other internal communication | 13 |
| [Project Service Automation](./project_service_automation_model) | Projects, billing, compliance, procurement and resources | 11 |

## Repository structure

```text
Timbr_Ontology_Catalogs/
├── .github/
│   ├── assets/                   # Logos, architecture diagram, social preview
│   └── ISSUE_TEMPLATE/           # Issue forms
├── <domain>_model/
│   ├── README.md                 # Overview, key concepts, diagram, examples
│   ├── model.png                 # Ontology diagram from the Timbr Ontology Explorer
│   ├── sql/<domain>_model.sql    # The ontology DDL: run this in Timbr
│   ├── examples/                 # Example queries (selected models)
│   │   └── example_queries.sql
│   └── tutorial/                 # Step-by-step setup guide
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── CHANGELOG.md
└── LICENSE
```

## Use the ontologies with AI agents

Once a model is deployed and mapped, the same governed semantics power natural-language and agentic access to your data:

- **[Timbr MCP Server](https://docs.timbr.ai/doc/docs/integration/mcp/overview)**: connect Claude, ChatGPT, Cursor, VS Code and other MCP clients to your knowledge graph.
- **[LangChain SDK](https://docs.timbr.ai/doc/docs/integration/langchain-sdk)** and **[LangGraph SDK](https://docs.timbr.ai/doc/docs/integration/langgraph-sdk)**: build LLM apps and agents grounded in your ontology.
- **[Python connectors](https://docs.timbr.ai/doc/docs/integration/python/python_http)**, **[REST API](https://docs.timbr.ai/doc/docs/integration/rest)**, JDBC/ODBC and BI tools: query the knowledge graph from anywhere.

## Contributing

Contributions are welcome, from fixing a typo to adding a whole new industry ontology. Read the [contributing guide](./CONTRIBUTING.md) to get started, and please follow our [code of conduct](./CODE_OF_CONDUCT.md).

Ideas for a new ontology? [Open an issue](https://github.com/WPSemantix/Timbr_Ontology_Catalogs/issues/new/choose).

## Support and community

- [Timbr documentation](https://docs.timbr.ai/doc/)
- [Live demos](https://timbr.ai/live-demos/) and [YouTube](https://www.youtube.com/@timbrai)
- [Timbr support](https://timbr.ai/support/)
- [Report an issue with a model](https://github.com/WPSemantix/Timbr_Ontology_Catalogs/issues)

## License

This catalog is released under the [MIT License](./LICENSE).

FIBO, FHIR and TPC are standards owned by their respective organizations (EDM Council, HL7 and the Transaction Processing Performance Council). The models here are adaptations for Timbr; check the original licenses before redistributing derived work.

<div align="center">
<br>
The <a href="https://timbr.ai">Timbr</a> team · © WP-SEMANTIX LTD
</div>
