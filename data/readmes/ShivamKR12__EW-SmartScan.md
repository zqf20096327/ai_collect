# EW SmartScan: Electronic Warfare Decision Support & Threat Scheduling Prototype

A real-time Electronic Warfare (EW) and Signal Intelligence (SIGINT) simulation prototype built with **Python**, **Streamlit**, and **Plotly**.

The system simulates a dense electromagnetic spectrum environment, intercepts synthetic RF signals, applies heuristic AI classification to evaluate threat potential, and dynamically reallocates receiver dwell time to continuously track high-priority threats.

## 📡 System Architecture

```
EW-SmartScan/
├── simulator.py        # Generates synthetic RF signals across 30 MHz - 3 GHz
├── ai_analyzer.py      # Heuristic & ML-mimicking threat scoring and tier classification
├── smart_scheduler.py  # Dynamic receiver resource & dwell-time allocation engine
└── app.py              # Interactive Streamlit dashboard with real-time Plotly telemetry
```

### Core Components

1. **Synthetic Signal Simulator (`simulator.py`)**:
   - Generates RF signals across 30 MHz to 3000 MHz.
   - Models critical parameters: Amplitude (dBm), Pulse Width ($\mu s$), and Modulation Types (`CW`, `AM`, `FM`, `BPSK`, `QPSK`, `Pulsed`, `Frequency Hopping`).
   - Injects suspicious signal patterns into military radar/communications bands.

2. **AI Threat Analyzer (`ai_analyzer.py`)**:
   - Heuristically scores each intercepted transmission based on frequency band, signal power, and complex modulation schemes.
   - Categorizes targets into three priority tiers:
     - 🔴 **Potential Threat** ($\ge 70\%$ Threat Score)
     - 🟡 **Unknown** ($30\% - 69\%$ Threat Score)
     - 🟢 **Normal / Commercial** ($< 30\%$ Threat Score)

3. **Smart Scheduler (`smart_scheduler.py`)**:
   - Implements dynamic resource weighting to optimize scanner focus.
   - Prioritizes scanner bandwidth and dwell time toward high-threat signals (70% base allocation) while maintaining periodic sweeps for unknown and background traffic.

4. **Telemetry Dashboard (`app.py`)**:
   - Built on Streamlit and Plotly for real-time visualization of spectrum occupation, threat distribution, and resource allocation breakdown.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+ installed on your system.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ShivamKR12/EW-SmartScan.git
   cd EW-SmartScan
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux / macOS:
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Launch the dashboard:
   ```bash
   streamlit run app.py
   ```

5. Open your browser to the local URL (typically `http://localhost:8501`).

---

## 🛠️ Tech Stack

- **Language**: Python 3
- **Web UI & Dashboard**: Streamlit
- **Data & Visualizations**: Pandas, NumPy, Plotly Express, Scikit-learn

