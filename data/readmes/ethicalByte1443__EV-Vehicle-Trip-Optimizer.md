# ⚡ EV Trip Optimizer 🚗🔋

An AI-powered **Electric Vehicle (EV) Trip Optimization System** that helps drivers maximize efficiency and range.  
The system simulates **real-world EV driving conditions**, optimizes trip strategy, and visualizes energy usage through interactive charts.

---

## ✨ Features

✅ Intuitive **Web UI** for trip planning  
✅ **FastAPI backend** for serving optimization logic & ML predictions  
✅ Input form with real-world trip parameters:
- Distance to travel  
- Current Battery %  
- Outside & Battery Temperature  
- Traffic condition (Light / Medium / Heavy)  
- Driving condition (Highway / Intracity / Uphill / Downhill)  
- Mode preference (Eco / Normal / Sport / Custom)  
- Payload (passengers & luggage)  

✅ Output includes:
- ⚙️ Recommended driving settings (Speed, AC %, Regen braking, Acceleration limit)  
- 🔋 Predicted range & estimated battery left after trip  
- 📊 Optimization summary cards  
- 📈 Interactive Visualizations:  
  - Battery % vs Distance (Line Chart)  
  - Speed vs Consumption (Scatter/Line Chart)  
  - Mode Comparison (Bar Chart)  
  - Energy Breakdown (Pie Chart)  
  - Projected Range (Gauge Chart)  

✅ Future-ready:
- Integrate **ML model** (Regression + Optimization algorithms)  
- Support **live telemetry** and map-based simulation  

---

## 🛠️ Tech Stack

- **Frontend:** HTML, JavaScript, Plotly.js (charts), Axios (API calls)  
- **Backend:** FastAPI (Python), Uvicorn  
- **Machine Learning (Planned):** Scikit-learn / TensorFlow / PyTorch  
- **Database (Planned):** PostgreSQL / SQLite (for trip history & training data)  
- **Deployment:** Docker, Cloud (AWS/GCP/Render)  

---

## 🔄 System Workflow

1. User enters trip details on the **frontend form**  
2. Data sent to **FastAPI backend** via REST API  
3. Backend applies:
   - Rule-based optimization (initial version)  
   - ML-powered prediction (future upgrade)  
4. Results returned as:
   - JSON with recommended settings  
   - Numerical predictions (range, battery left)  
5. Frontend renders:
   - Optimization summary cards  
   - Dynamic interactive graphs using Plotly.js  

---

## 🏗️ Low Level Design (LLD)

### 📌 Components
- **Frontend Module**
  - `FormHandler` → Collects user input & validates data  
  - `APICaller` → Sends request to backend using Axios  
  - `ChartManager` → Renders Plotly.js charts  
  - `UIManager` → Displays results in structured format  

- **Backend Module (FastAPI)**
  - `InputModel` (Pydantic) → Schema validation  
  - `OptimizationEngine` → Core logic for speed, AC, regen braking  
  - `MLModelHandler` (Future) → Loads trained ML model for predictions  
  - `ResponseBuilder` → Formats output JSON  

- **Data Layer**
  - **Planned:** Store historical trips for ML training (SQLite/PostgreSQL)  

---

### 📌 Sequence Flow

```

User → Frontend Form → APICaller → FastAPI Endpoint (/optimize)
→ OptimizationEngine → MLModelHandler (future)
→ ResponseBuilder → JSON Response → ChartManager → UI

````

---

### 📌 Class-Level LLD (Python Backend)

```py
class TripInput(BaseModel):
    distance_km: float
    battery_percent: float
    outside_temp: float
    battery_temp: float
    traffic: str
    driving: str
    mode: str
    payload: float

class OptimizationEngine:
    def __init__(self, data: TripInput):
        self.data = data

    def compute_settings(self) -> dict:
        # Logic for speed, AC %, regen braking
        ...

    def predict_range(self) -> float:
        # Formula/ML prediction
        ...

    def estimate_battery_left(self) -> float:
        ...

class ResponseBuilder:
    def __init__(self, settings, range_val, battery_left):
        self.settings = settings
        self.range_val = range_val
        self.battery_left = battery_left

    def to_dict(self):
        return {
            "recommended_settings": self.settings,
            "predicted_range": self.range_val,
            "battery_left": self.battery_left
        }
````

---

## 📊 Example Output

```json
{
  "recommended_settings": {
    "speed": 55,
    "ac": 25,
    "regen": "Medium",
    "acceleration_limit": "Low"
  },
  "predicted_range": 178.5,
  "battery_left": 45.0
}
```

---

## 🚀 Setup Instructions

### 2️⃣ Setup Backend (FastAPI)

```bash
cd backend
pip install fastapi uvicorn pydantic
uvicorn main:app --reload --port 8000
```

Backend runs at 👉 `http://127.0.0.1:8000`

### 3️⃣ Run Frontend

Open `frontend/index.html` in your browser.
It connects to the backend API automatically.

---

## 🔮 Future Enhancements

* ✅ ML model integration for **range prediction & optimal strategy**
* ✅ Trip history database for personalized recommendations
* ✅ Google Maps API integration for **real routes**
* ✅ Real-time **driving telemetry simulation**
* ✅ Mobile app (React Native / Flutter)

---


