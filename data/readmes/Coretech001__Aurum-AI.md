# ✨ Aurum AI

### Smarter Insights. Sharper Trading.

**Aurum AI** is a desktop platform for gold market monitoring, market analysis, algorithmic trading, and local model experimentation. It integrates with **MetaTrader 5** through an MQL5 Expert Advisor (EA), combining market insights, trading tools, and model training in a single application.

The current desktop interface is built with **Python and Tkinter**, while the project is gradually transitioning to a modern stack based on **Rust, React, TypeScript, and Tauri**.

---

## 🚀 Features

- **Market Dashboard** — Monitor market data, open positions, trading robot status, model training, and application settings.
- **MetaTrader 5 Integration** — Optional integration with the official MetaTrader 5 platform.
- **MQL5 Expert Advisor** — Includes EA source files (`.mq5`, `.mqh`) and configuration presets (`.set`).
- **Market Intelligence** — Analyze market indicators, return correlations, and market regime classifications through Subgraph.
- **Local Model Training** — Experiment with model training in a local environment.
- **Developer Integrations** — Configurable integrations with GitHub, GitLab, Figma, and MCP.
- **Local Licensing** — Free, Pro, and Business plans with local entitlement management and activation without payment processing.
- **Social Paper Trading** — Share strategies exclusively in paper-trading and demo environments.
- **Application Distribution** — Windows installer built with PyInstaller and Inno Setup.
- **Release Management** — Application updates distributed through GitHub Releases.

---

## 🛠️ Technology Stack

### Current Application

| Component | Technology |
|---|---|
| Desktop interface | Python, Tkinter |
| Trading platform | MetaTrader 5 |
| Trading execution | MQL5 Expert Advisor |
| Testing | pytest |
| Application packaging | PyInstaller |
| Windows installer | Inno Setup |

### Next-Generation Architecture

The project is transitioning toward a more modern desktop architecture.

| Component | Planned Technology |
|---|---|
| Core backend | Rust, Axum, Tokio |
| Frontend | React, TypeScript |
| Desktop framework | Tauri |
| Trading execution | MQL5 Expert Advisor |

> **Migration status:** The new architecture is in progress. The technologies listed above describe the target stack and should not be interpreted as indicating that the migration is complete.

For architectural details, see [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

---

## 📋 Requirements

Before getting started, prepare the following:

- Windows environment.
- Python compatible with the project's dependency files.
- MetaTrader 5 installation if you need trading-platform integration.
- Git for source-code management.

For the exact Python version and dependency requirements, consult the project configuration and `requirements-lock.txt`.

---

## ⚡ Getting Started

### 1. Clone the Repository

```powershell
git clone https://github.com/Coretech001/Aurum-AI.git
cd AurumAI
```


### 2. Create a Virtual Environment

```powershell
python -m venv .venv
```

### 3. Install Dependencies

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt -r requirements-dev.txt
```

### 4. Launch the Application

```powershell
.\.venv\Scripts\python.exe app\main.py
```

The commands above describe the existing Python/Tkinter application workflow.

---

## 🧪 Testing

Run the test suite from the project root:

```powershell
.\.venv\Scripts\python.exe -m pytest -q tests
```

Run tests before integrating changes or preparing a new build.

---

## 🔌 Integrations and Privacy

Aurum AI is designed to operate locally.

The documented third-party integrations are:

- **GitHub** — Repository and release-related functionality.
- **GitLab** — Configurable development integration.
- **Figma** — Configurable design integration.
- **MCP** — Configurable tool integration.

Vercel, Sentry, Slack, and Kilo were removed on October 4, 2026.

The product is intended to operate without a hosted application API, external telemetry, or a model CDN.

Actual network behavior depends on the enabled integrations and should be verified against the implementation.

### Dependency Management

The reproducible environment is defined by `requirements-lock.txt`.

**Security guidelines:**
- Never commit API keys, access tokens, passwords, or database connection strings.
- Keep local secrets out of version control.
- Review third-party dependencies before updating them.
- Verify application network activity when assessing privacy requirements.

---

## 📦 Building the Windows Installer

The installer configuration is located at:

```text
installer/installer.iss
```

The installer detects the MetaTrader 5 data directory and installs the integration files into:

```text
MQL5/Files/AurumAI
```

The installation is designed to work without administrator privileges.

### Build Instructions

Navigate to the installer directory:

```powershell
Set-Location "C:\path\to\AurumAI\installer"
```

Run the build script:

```powershell
.\build_installer.cmd
```

### Build Architecture

The current PyInstaller configuration uses **onedir mode**, defined in `launcher.spec`.

The application executable and its dependencies are placed in:

```text
dist/AurumAI/AurumAI.exe
```

Inno Setup packages the application into a Windows installer.

### Tauri Installer

The Tauri installer, distributed through NSIS or MSI, follows a separate build process involving the Python gateway and Rust core.

Do not confuse the Python/Tkinter build artifacts with the Tauri build artifacts. A security scan of one package does not validate the other.

> **Release requirement:** Before public distribution or live-trading use, verify the relevant build through demo testing, digital-signature verification, cryptographic hash verification, and artifact-specific security scanning.

---

## 🔐 Operational Security

Security is particularly important for software connected to trading platforms.

- Never commit credentials, tokens, passwords, or DSNs.
- Keep API credentials and other secrets outside the repository.
- Review trading configuration before enabling the Expert Advisor.
- Verify installer integrity before deployment.
- Test new builds in an isolated or demo environment.
- Do not assume that a successful build means the application is safe for live trading.

---

## 📈 Trading Safety

Aurum AI provides tools for market analysis and algorithmic trading, but no strategy guarantees profits.

Before enabling the trading robot:

- Use a demo account until sufficient backtesting and forward-testing results are available.
- Review lot-size limits and position-sizing rules.
- Configure acceptable spread thresholds.
- Establish daily loss limits.
- Review maximum drawdown limits.
- Confirm that the Expert Advisor is operating as expected.

**Always understand and evaluate the risks before connecting the application to a live trading account.**

---

## 🗺️ Roadmap

The following areas represent the project's modernization direction, not a guarantee that each feature is complete.

- [ ] Continue migrating the desktop interface to React and TypeScript.
- [ ] Develop the Rust backend using Axum and Tokio.
- [ ] Integrate the new backend and frontend through Tauri.
- [ ] Preserve the MQL5 Expert Advisor as the trading execution component.
- [ ] Strengthen automated testing and release validation.
- [ ] Improve application security and distribution workflows.

---

## 🤝 Contributing

Contributions, bug reports, and technical suggestions are welcome.

When contributing:

1. Review the existing architecture before making changes.
2. Follow established coding conventions.
3. Run relevant tests before submitting changes.
4. Never include secrets or personal credentials.
5. Clearly document changes that affect trading behavior or application security.

---

## 📄 License

Add your project's license information here.

If the repository does not yet have a license, choose an appropriate license before accepting external contributions or distributing the application.

---

<div align="center">

**Aurum AI**

*Smarter Insights. Sharper Trading.*

Built for market analysis, algorithmic trading, and local experimentation.

</div>
