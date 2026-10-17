# Employee Attrition Prediction — Deployable Project

Train in Google Colab → deploy a live "Retention Pulse" app on Streamlit
Community Cloud.

## Files

| File | Purpose | Push to GitHub? |
|---|---|---|
| `app.py` | Streamlit app — single & batch attrition risk predictions, full custom UI | ✅ Yes |
| `requirements.txt` | Python dependencies | ✅ Yes |
| `.streamlit/config.toml` | Theme colors (charcoal + amber accent) | ✅ Yes — keep the `.streamlit` folder name exactly |
| `attrition_model.pkl` | Trained, tuned Random Forest classifier | ✅ Yes |
| `scaler.pkl` | Fitted `StandardScaler` | ✅ Yes |
| `salary_encoder.pkl` | Fitted `LabelEncoder` for `salary` | ✅ Yes |
| `department_encoder.pkl` | Fitted `LabelEncoder` for `Department` | ✅ Yes |
| `feature_columns.pkl` | Exact column order the model expects | ✅ Yes |
| `Employee_Attrition_Prediction_Colab.ipynb` | Training notebook | Optional — nice to keep for reference |
| `Dataset_Employee_Attrition.csv` | Raw dataset | ❌ No — not needed at inference time |

## Step 1 — Train the model in Colab

1. Open `Employee_Attrition_Prediction_Colab.ipynb` in Google Colab.
2. Run all cells top to bottom.
3. Upload `Dataset_Employee_Attrition.csv` when prompted.
4. At the end, 5 files auto-download:
   - `attrition_model.pkl`
   - `scaler.pkl`
   - `salary_encoder.pkl`
   - `department_encoder.pkl`
   - `feature_columns.pkl`

## Step 2 — Arrange your project folder

```
attrition-app/
├── app.py
├── requirements.txt
├── .streamlit/
│   └── config.toml
├── attrition_model.pkl
├── scaler.pkl
├── salary_encoder.pkl
├── department_encoder.pkl
└── feature_columns.pkl
```

## Step 3 — Test locally

```bash
cd attrition-app

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
streamlit run app.py
```

Opens at `http://localhost:8501`.

## Step 4 — Push to GitHub

```bash
git init
git add app.py requirements.txt .streamlit *.pkl
git commit -m "Employee attrition prediction app"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

## Step 5 — Deploy on Streamlit Community Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
2. Click **New app**.
3. Select your repo, branch `main`, main file `app.py`.
4. Click **Deploy**.

You'll get a public URL like `https://<your-app>.streamlit.app`.

## Notes on model choice

The notebook trains a baseline Random Forest, then tunes it with
`GridSearchCV` and evaluates **both** on the same held-out test set (the
original notebook found the best hyperparameters but never actually
checked whether the tuned model was better — this version fixes that by
comparing both side by side before picking `final_model`).
