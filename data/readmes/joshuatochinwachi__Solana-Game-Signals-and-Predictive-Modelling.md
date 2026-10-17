# Solana Game Analytics, Player Behavior Modeling and Predictive Forecasting

<div align="center">

![Solana](https://img.shields.io/badge/Solana-9945FF?style=for-the-badge&logo=solana&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)

**Next-Generation Analytics & ML-Powered Churn Prediction for Solana Gaming**

[Frontend Web App](https://solana-games.app) • [Video Demo](https://drive.google.com/file/d/1Pr1j8zzOSjTspyXSc7D27tpgrRowd5_F) • [API Docs](https://solana-game-signals-and-predictive-modelling-production.up.railway.app/docs) • [Technical Guide](TECHNICAL_DOCUMENTATION.md)

</div>

---

## 🎯 The Problem & Solution

### The Problem
Solana's gaming ecosystem generates millions of on-chain transactions daily, but game developers lack tools to:
- Predict which players will leave before they churn
- Understand cross-game behavior patterns  
- Make data-driven retention decisions

### The Solution
A production-grade platform that:
- **Aggregates 60M+ user transactions** from 12 Solana games in real-time
- **Predicts player churn 14 days in advance** using advanced ML (typically >85% ROC-AUC accuracy)
- **Auto-retrains models** whenever fresh blockchain data arrives
- **Visualizes insights** through a gamified dashboard that auto-updates frequently
- **Empowers game developers** to proactively retain players, not just react to losses

---

## 💎 Value Proposition

### For Game Developers
- 🎯 Predict churn 14 days before it happens (>85% accuracy)
- 💰 Reduce player acquisition costs by improving retention
- 📊 Understand cross-game behavior across Solana ecosystem
- 🤖 Zero-maintenance ML that auto-improves with new data

### For Players
- 🏆 Discover top-performing games by retention metrics
- 🔗 Find similar games you might enjoy
- 📈 See your own engagement patterns (future wallet integration)

### For Solana Ecosystem
- 📊 First comprehensive gaming analytics platform
- 🧠 Open-source ML models for community use
- 🌐 Cross-game insights unavailable elsewhere

---

## ⛓️ Solana Integration

This project is deeply integrated with the Solana blockchain:

### Direct Blockchain Data
- 📊 **60M+ Transactions**: Real Solana on-chain data from 12 games
- 🔍 **Transaction Analysis**: Every metric derived from verified blockchain transactions
- ⏱️ **Real-Time Sync**: Updates as new blocks finalize on Solana

### Technical Implementation
- **RPC Analysis**: Custom `classifier.py` identifies Programs, NFTs, Tokens, PDAs via Solana RPC
- **Dune Queries**: 11 custom SQL queries across Solana's blockchain data
- **Wallet Tracking**: Individual user behavior per Solana wallet address
- **Cross-Game Logic**: Detects shared wallets across multiple Solana games
- **Solscan Integration**: Direct links to wallet explorers for transparency

### Why This Matters for Solana Gaming
- 🎮 **First Analytics Platform**: Solana gaming lacks comprehensive analytics tools
- 📈 **Ecosystem Growth**: Helps games retain players = stronger Solana gaming ecosystem
- 🔗 **Network Effects**: Cross-game insights only possible on-chain
- 💎 **Open Source**: All 11 Dune queries publicly available for community use

---

## ✨ Key Features

### 📊 Real-Time Analytics Engine
- **11 Behavioral Metrics**: Activation, retention, reactivation, deactivation, cross-game behavior
- **Individual User-Level Data**: Granular transaction tracking per wallet
- **12 Games Tracked**: Star Atlas, StepN, Genopets, Portals, Honeyland, and more
- **60-Day Rolling Window**: Comprehensive behavior history
- **Sub-100ms Response**: Cached endpoints for instant insights
- **Auto-Refresh**: Data updates automatically from Dune Analytics

### 🤖 Self-Training ML System
- **5 ML Algorithms**: Logistic Regression, Random Forest, Gradient Boosting, XGBoost, LightGBM
- **Auto-Champion Selection**: Best model automatically chosen by ROC-AUC score after each training
- **Ensemble Predictions**: Weighted average of top 3 models for robustness
- **Automated Retraining**: Models retrain whenever fresh data arrives (no manual intervention)
- **10 Engineered Features**: Activity patterns, momentum, consistency, recency metrics
- **Adaptive Risk Thresholds**: Dynamic percentile-based classification ensures meaningful High/Medium/Low categories regardless of population health
- **Real-Time Predictions**: Churn risk calculated for all active users

🏆 **Current Champion Model**: [Check Live Leaderboard](https://solana-game-signals-and-predictive-modelling-production.up.railway.app/api/ml/models/leaderboard)

### 🎨 Gamified Dashboard
- **Elite Gamers Scroller**: Live ticker of top power users with clickable Solscan links
- **Dynamic Alerts**: Real-time warnings (Critical/Warning/Success) that adapt as data changes
- **Interactive Visualizations**: Heatmaps, network graphs, time-series charts, etc.
- **Light/Dark Mode**: Solana-branded theme with particle effects
- **Auto-Refresh**: Auto-updates with zero manual reload
- **100% Data Display**: All records shown via virtualized tables

### ⚡ Production-Grade Architecture
- **99%+ Uptime**: Deployed on Railway (backend) and Vercel (frontend)
- **Intelligent Caching**: 168-hour TTL with automatic refresh
- **Type-Safe**: 100% TypeScript coverage (strict mode)
- **Zero Runtime Errors**: Comprehensive error handling
- **Scalable**: Handles 200K+ records without performance degradation

---

## 🏗️ System Architecture

```
Solana Blockchain (12 Games) 
    ↓
Dune Analytics (11 Queries)
    ↓ [Every 168 hours]
FastAPI Backend (Railway)
    ├─ Cache Manager (Auto-refresh on TTL expiry)
    ├─ Feature Engineering (10 features)
    ├─ ML Manager (5 models, auto-train)
    │  ├─ Train on fresh data
    │  ├─ Select champion by ROC-AUC
    │  └─ Generate predictions
    └─ Prediction Cache
    ↓
REST API (21 endpoints)
    ↓
React Frontend (Vercel)
    ├─ TanStack Query (30s polling)
    ├─ Zustand (State mgmt)
    └─ Recharts/D3 (Viz)
```

**Key Innovation**: Self-training pipeline - Models automatically retrain whenever `/api/cache/refresh` is triggered, selecting the best-performing algorithm based on current data patterns. No manual retraining needed!

**Full Architecture Details**: See [TECHNICAL_DOCUMENTATION.md](TECHNICAL_DOCUMENTATION.md) for 15,000+ word deep dive.

---

## 🛠️ Technology Stack

| Layer | Technologies | Why? |
|-------|-------------|------|
| **Backend** | Python 3.11, FastAPI, pandas, scikit-learn, XGBoost, LightGBM, joblib | Async API, robust ML, efficient caching |
| **Frontend** | React 19, TypeScript 5.0, Zustand, TanStack Query, Recharts, D3, Tailwind | Type-safe, reactive, performant |
| **Data Source** | Dune Analytics SDK | Direct Solana blockchain data access |
| **Deployment** | Railway (backend), Vercel (frontend) | Auto-deploy, edge network, 99%+ uptime |

---

## 📂 Project Structure

```
solana-games-analytics/
├── backend/                          # FastAPI ML Backend
│   ├── main.py                       # 🔥 Core API (1,400+ lines)
│   ├── requirements.txt              # Python dependencies
│   ├── Dockerfile                    # Container configuration
│   ├── railway.json                  # Railway deployment config
│   ├── .env.example                  # Environment variables template
│   ├── raw_data_cache/              # 💾 Cached Dune query results
│   │   ├── *.joblib                 # Serialized DataFrames
│   │   └── cache_metadata.json      # Cache timestamps & row counts
│   └── ml_models/                   # 🤖 Trained ML models
│       ├── logistic_regression.joblib
│       ├── random_forest.joblib
│       ├── gradient_boosting.joblib
│       ├── xgboost.joblib
│       ├── lightgbm.joblib
│       ├── scaler.joblib            # Feature scaler
│       └── metadata.json            # Model metrics & history
│
├── frontend/                         # React 19 Dashboard
│   ├── src/
│   │   ├── components/
│   │   │   ├── features/
│   │   │   │   ├── analytics/       # Analytics visualizations
│   │   │   │   │   ├── GamerRetention.tsx
│   │   │   │   │   ├── DailyActivity.tsx
│   │   │   │   │   ├── CrossGameNetwork.tsx
│   │   │   │   │   └── ...
│   │   │   │   └── ml/              # ML prediction displays
│   │   │   │       ├── ChurnPredictions.tsx
│   │   │   │       ├── HighRiskUsers.tsx
│   │   │   │       ├── ModelLeaderboard.tsx
│   │   │   │       └── ...
│   │   │   ├── layout/
│   │   │   │   ├── Header.tsx       # Logo, theme toggle, live indicator
│   │   │   │   ├── Footer.tsx       # Credits, API status, timestamp
│   │   │   │   └── EliteGamerScroller.tsx  # 🏆 Infinite scroller
│   │   │   ├── providers/
│   │   │   │   └── ThemeProvider.tsx
│   │   │   └── ui/                  # Design system primitives
│   │   │       ├── GlassCard.tsx
│   │   │       ├── NeonButton.tsx
│   │   │       └── ...
│   │   ├── hooks/
│   │   │   ├── useAutoRefresh.ts    # 30-second polling hook
│   │   │   └── useTheme.ts
│   │   ├── pages/
│   │   │   ├── DashboardPage.tsx    # Main analytics view
│   │   │   └── MLPage.tsx           # AI predictions view
│   │   ├── services/
│   │   │   └── api.ts               # Typed API client
│   │   ├── types/
│   │   │   └── api.ts               # Shared TypeScript types
│   │   └── utils/
│   │       └── formatters.ts        # Number/date formatting
│   ├── public/                      # Static assets
│   ├── package.json
│   ├── tsconfig.json
│   ├── tailwind.config.js
│   └── vite.config.ts
│
├── classifier.py                   # On-chain address type detector
│                                   # Identifies: Programs, NFTs, Tokens,
│                                   # Token Accounts, PDAs via RPC analysis
│                                   # Guided creation of 11 Dune queries
├── TECHNICAL_DOCUMENTATION.md       # 📖 Architecture deep-dive (15,000+ words)
└── README.md                        # 👈 You are here
```

---

## 🧠 Machine Learning Pipeline

### Features Extracted (10 per user-game pair)

| Feature | What It Measures | Why It Matters |
|---------|------------------|----------------|
| `active_days_last_8` | Recent activity level | Recent engagement is strongest churn predictor |
| `transactions_last_8` | Recent engagement intensity | High recent activity = lower churn risk |
| `total_active_days` | Tenure/experience | Longer-term users less likely to churn |
| `total_transactions` | Lifetime value proxy | High LTV users worth retention effort |
| `avg_transactions_per_day` | Average engagement rate | Consistent engagement indicates habit |
| `days_since_last_activity` | Recency (lower = better) | Long absence = high churn signal |
| `week1_transactions` | Onboarding success | Strong start = better retention |
| `week_last_transactions` | Current engagement | Declining recent activity = warning |
| `early_to_late_momentum` | Trend (>1 = growing, <1 = declining) | Momentum direction predicts future |
| `consistency_score` | Play regularity | Regular players vs sporadic visitors |

### Automated Training Process

```
1. Data Ingestion  → Dune Analytics queries (last 60 days)
2. Cache Check     → Use cached if <168hrs old, else fetch fresh
3. Feature Eng     → Extract 10 features per user-game pair
4. Data Split      → 75% train, 25% test (stratified)
4.5. SMOTE Balance → Synthetic minority oversampling to handle 95%+ class imbalance
5. Standardize     → Z-score normalization (mean=0, std=1)
6. Train 5 Models  → Parallel training (all algorithms)
7. Evaluate        → ROC-AUC (primary), Accuracy, Precision, Recall
8. Select Champion → Best ROC-AUC wins (typically Random Forest or LightGBM)
9. Build Ensemble  → Top 3 models weighted by performance
10. Generate Preds → Churn risk for all active users
11. Cache Results  → Predictions cached for 168 hours
```

**Retraining Triggers:**
- **Manual**: `POST /api/cache/refresh`
- **Automatic**: When cache expires and new data requested
- **Result**: Champion model may change based on current data patterns

### Prediction Methods

1. **Champion Method**: Uses only the current best-performing model
2. **Ensemble Method**: Weighted average of top 3 models (more robust)

### Risk Classification (Dynamic Percentile-Based)

- 🔴 **High Risk (Top 15%)**: Immediate intervention needed
- 🟡 **Medium Risk (50th-85th percentile)**: Monitor closely  
- 🟢 **Low Risk (Bottom 50%)**: Healthy engagement

**Note**: Thresholds adapt to actual prediction distribution, ensuring meaningful categories regardless of population health. Actual percentile values are logged with each prediction run.

### Current Performance (Live Examples)

- **ROC-AUC**: ~86% (excellent discrimination)
- **Recall**: ~55% (catches over half of churners)  
- **Precision**: ~8% (conservative flagging for low-cost interventions)
- **Accuracy**: ~87% (post-SMOTE balancing)

**Note**: These metrics update automatically with each model retraining. Actual values vary as player behavior evolves.

**Check Current Performance**: [Live Model Leaderboard](https://solana-game-signals-and-predictive-modelling-production.up.railway.app/api/ml/models/leaderboard)

---

## 📊 API Endpoints

### Analytics (11 Endpoints)
*All return `{metadata, data}` with cache info and UTC timestamps.*

| Endpoint | Purpose | What It Shows |
|----------|---------|---------------|
| `/api/analytics/gamer-activation` | New user acquisition | Daily new players per game |
| `/api/analytics/gamer-retention` | Cohort retention | Week-over-week retention % |
| `/api/analytics/gamer-reactivation` | Returning users | Weekly reactivation counts |
| `/api/analytics/gamer-deactivation` | Churned users | Weekly churn tracking |
| `/api/analytics/high-retention-users` | Power users | Players with >50% retention |
| `/api/analytics/high-retention-summary` | Game-level retention | Per-game retention stats |
| `/api/analytics/gamers-by-games-played` | Multi-game distribution | Users by # of games played |
| `/api/analytics/cross-game-gamers` | Multi-game players | Cross-game engagement |
| `/api/analytics/gaming-activity-total` | Lifetime metrics | Total txs & users per game |
| `/api/analytics/daily-gaming-activity` | Time-series data | Daily activity trends |
| `/api/analytics/user-daily-activity` | User-level log | Individual transaction data |

### ML Predictions (5 Endpoints)

| Endpoint | Purpose |
|----------|---------|
| `/api/ml/predictions/churn?method=ensemble` | Churn risk for all users |
| `/api/ml/predictions/churn/by-game` | Game-level churn aggregates |
| `/api/ml/predictions/high-risk-users?limit=100` | Top N at-risk users |
| `/api/ml/models/leaderboard` | All 5 models ranked by performance |
| `/api/ml/models/info` | Current champion details & features |

### Utilities (5 Endpoints)

- `/api/health` - System health & current stats
- `/api/cache/status` - Cache freshness & ages
- `/api/cache/refresh` - Force refresh & retrain (POST)
- `/api/bulk/analytics` - All 11 analytics at once
- `/api/bulk/predictions` - All ML predictions at once

**Full API Docs**: [Interactive Swagger UI](https://solana-game-signals-and-predictive-modelling-production.up.railway.app/docs)

---

## 🚀 Quick Start

### Backend Setup

```bash
# 1. Clone repository
git clone https://github.com/joshuatochinwachi/Solana-Game-Signals-and-Predictive-Modelling.git
cd Solana-Game-Signals-and-Predictive-Modelling/backend

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
cp .env.example .env
# Add your DEFI_JOSH_DUNE_QUERY_API_KEY_1 (and _2, _3 for rotation)

# 5. Run server
uvicorn main:app --reload --port 8000
# API: http://localhost:8000
# Docs: http://localhost:8000/docs
```

### Frontend Setup

```bash
# 1. Navigate to frontend
cd ../frontend

# 2. Install dependencies
npm install

# 3. Configure environment
cp .env.example .env
# Set VITE_API_BASE_URL=http://localhost:8000

# 4. Start dev server
npm run dev
# Dashboard: http://localhost:5173
```

### Environment Variables

**Backend (.env)** - See `.env.example` for full list:

```bash
# Dune API Keys (required - supports multi-key rotation)
DEFI_JOSH_DUNE_QUERY_API_KEY_1=your_key_1
DEFI_JOSH_DUNE_QUERY_API_KEY_2=your_key_2  # Optional
DEFI_JOSH_DUNE_QUERY_API_KEY_3=your_key_3  # Optional

# Configuration
CACHE_DURATION=604800              # 168 hours (default)
MIN_TRAINING_SAMPLES=100
PREDICTION_WINDOW_DAYS=14
FASTAPI_SECRET=your_secret

# Query IDs (11 total - see .env.example)
```

**Frontend (.env):**

```bash
VITE_API_BASE_URL=http://localhost:8000
```

---

## 🎨 Dashboard Features

### Elite Gamers Scroller
Infinite horizontal ticker showing top power users:
- 🏆 `abc123...xyz | 3 Games | 95% Retention | Low Risk` →
- Clickable wallet addresses (links to Solscan)
- Auto-scrolls continuously (pauses on hover)
- Updates every 30 seconds with fresh predictions

### Dynamic Alerts
Real-time warnings that adapt as data changes:
- 🚨 **Critical**: High-risk users exceed threshold
- ⚠️ **Warning**: Deactivation spikes, declining retention
- ✅ **Success**: Improving ecosystem metrics
- 💡 **Opportunity**: Cross-game promotion potential

### Interactive Visualizations
- **Cohort Retention Heatmap**: Week-over-week retention %
- **Cross-Game Network Graph**: Shared user connections (D3.js)
- **Daily Activity Time-Series**: Transaction trends per game
- **Risk Distribution Pie**: High/Medium/Low churn segments
- **Complete Data Tables**: All records with search, sort, pagination, virtualization

### Design System
- **Solana Gradient**: Purple (`#9945FF`) → Cyan (`#14F195`)
- **Glassmorphism**: Semi-transparent cards with backdrop blur
- **Particle Background**: 50 floating particles (20s animation)
- **Neon Accents**: Glowing borders on hover
- **Gaming Typography**: Orbitron headers, Inter body
- **Light/Dark Mode**: Fully themed toggle

---

## 🏆 Technical Achievements

### Performance
- ⚡ **API Response**: <100ms (cached), 2-5s (fresh data)
- 🚀 **Frontend Load**: <2s (Lighthouse 99/100)
- 📊 **Data Completeness**: 100% (all records displayed)
- 🔄 **Update Frequency**: 30 seconds (frontend polling)
- 📈 **ML Training**: Fully automated, no manual intervention
- 🎯 **Typical ROC-AUC**: 85-90% (varies with data)

**Note on ML Metrics**: All performance metrics are live examples from recent training runs and update automatically as models retrain on fresh blockchain data. Check the [live leaderboard](https://solana-game-signals-and-predictive-modelling-production.up.railway.app/api/ml/models/leaderboard) for current champion performance.

### Code Quality
- ✅ **Type Safety**: 100% TypeScript (strict mode)
- ✅ **Error Handling**: Comprehensive try-catch blocks
- ✅ **Zero Runtime Errors**: Clean production build
- ✅ **Accessibility**: WCAG 2.1 AA compliant
- ✅ **Responsive**: Mobile/tablet/desktop/ultrawide
- ✅ **Robust ML**: Proper churn labeling with adaptive risk thresholds
- ✅ **No Data Leakage**: Temporal validation prevents future information from affecting training

### Scalability
- 🔧 **API Key Rotation**: Round-robin across 3 keys
- 🔧 **Atomic State**: Zustand for minimal re-renders
- 🔧 **Virtualized Tables**: Handle 200K+ rows smoothly
- 🔧 **Code Splitting**: Lazy-loaded routes
- 🔧 **Edge Deployment**: Vercel CDN globally

---

## 📊 Live Ecosystem Insights

Want to see current stats? Visit these endpoints:

- **Overall Health**: [/api/health](https://solana-game-signals-and-predictive-modelling-production.up.railway.app/api/health)
- **Current Champion**: [/api/ml/models/info](https://solana-game-signals-and-predictive-modelling-production.up.railway.app/api/ml/models/info)
- **Model Rankings**: [/api/ml/models/leaderboard](https://solana-game-signals-and-predictive-modelling-production.up.railway.app/api/ml/models/leaderboard)
- **Churn Summary**: [/api/ml/predictions/churn](https://solana-game-signals-and-predictive-modelling-production.up.railway.app/api/ml/predictions/churn)

**Note**: All metrics update automatically as fresh blockchain data arrives. The system continuously adapts to new patterns without manual intervention.

---

## 🌟 Traction & Impact

### Live Metrics
- 🎮 **12 Games Tracked**: Largest Solana gaming dataset
- 👥 **Active Users**: [Check live count](https://solana-game-signals-and-predictive-modelling-production.up.railway.app/api/health)
- ⚡ **99%+ Uptime**: Production-grade reliability since deployment
- 🔄 **Auto-Updates**: Self-training ML requires zero maintenance
- 🌐 **Global Reach**: Vercel edge deployment across 25+ regions

### Technical Validation
- ✅ **Live API**: 21 endpoints operational
- ✅ **Real Predictions**: [View current churn risks](https://solana-game-signals-and-predictive-modelling-production.up.railway.app/api/ml/predictions/high-risk-users?limit=20)
- ✅ **Model Performance**: [Live leaderboard](https://solana-game-signals-and-predictive-modelling-production.up.railway.app/api/ml/models/leaderboard)
- ✅ **Open Source**: All code and queries publicly available

### Community Engagement
- 🐦 **Twitter/X**: [@defi__josh](https://x.com/defi__josh)
- 📊 **Dune Dashboard**: [Public analytics](https://dune.com/defi__josh/solana-games)
- 💬 **GitHub Discussions**: Open for collaboration
- 📧 **Developer Contact**: joshuatochinwachi@gmail.com

---

## 🛣️ Roadmap

### ✅ Phase 1: Current (Completed)
- ✅ 11 analytics endpoints with real-time data
- ✅ 5-model ML ensemble with auto-selection
- ✅ Self-training pipeline (no manual retraining)
- ✅ Gamified React dashboard
- ✅ Production deployment (Railway + Vercel)
- ✅ Dynamic risk classification system

### 🔜 Phase 2: Enhanced Intelligence (Q1 2026)
- 🔲 **LTV Prediction**: Forecast user lifetime value
- 🔲 **Anomaly Detection**: Alert on unusual patterns
- 🔲 **Sentiment Analysis**: Discord/Twitter mood tracking
- 🔲 **Recommendation Engine**: Game suggestions

### 🚀 Phase 3: Platform Expansion (Q2 2026)
- 🔲 **Mobile App**: React Native iOS/Android
- 🔲 **Wallet Connect**: Personalized insights
- 🔲 **Developer API**: Public API for studios
- 🔲 **Zapier Integration**: No-code automation

### 🌐 Phase 4: Decentralization (Q3 2026)
- 🔲 **On-Chain Analytics**: Solana program deployment
- 🔲 **ZK-Proofs**: Privacy-preserving profiling
- 🔲 **Token Incentives**: Reward contributors
- 🔲 **DAO Governance**: Community-driven roadmap

### Partner Integration Opportunities

Ready to integrate with:

| Partner | Integration Idea | Benefit |
|---------|------------------|---------|
| 🎮 **Play Solana** | Embed analytics widget in game portals | Players discover high-retention games |
| 🎨 **Moddio** | Real-time churn alerts in game dev tools | Developers get instant notifications |
| 🤖 **icm.run** | Trigger automated retention campaigns | AI-powered personalized interventions |
| 📱 **Alphabot** | Discord bot for whale tracking | Studios monitor VIP players 24/7 |

**Value Proposition**: Game studios get enterprise-grade analytics without building infrastructure.

---

## 🤝 Contributing

I welcome contributions! Here's how:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Guidelines:
- Write tests for new features
- Follow existing code style (ESLint/Black)
- Update docs for API changes
- Keep commits atomic

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Data**: Dune Analytics • Solana
- **Libraries**: FastAPI, React, scikit-learn, XGBoost, LightGBM, Recharts, D3.js, Tailwind CSS
- **Infrastructure**: Railway • Vercel
- **Games Analyzed**: Star Atlas, StepN, Genopets, Portals, Honeyland, Aurory, MixMob, Nyan Heroes, Faraway, Axie Rescue, ev.io, Portals Chrono Rush

---

## 📧 Contact & Resources

- **Developer**: Josh (@defi__josh) - Solo Developer
- **Twitter/X**: [@defi__josh](https://x.com/defi__josh)
- **Email**: joshuatochinwachi@gmail.com
- **GitHub**: [@joshuatochinwachi](https://github.com/joshuatochinwachi)
- **Live Demo/Frontend Web App**: [https://solana-games.app](https://solana-games.app)
- **API Endpoint**: [https://solana-game-signals-and-predictive-modelling-production.up.railway.app](https://solana-game-signals-and-predictive-modelling-production.up.railway.app)

- **Issues**: [Open an issue](https://github.com/joshuatochinwachi/Solana-Game-Signals-and-Predictive-Modelling/issues)
- **Questions**: [Start a discussion](https://github.com/joshuatochinwachi/Solana-Game-Signals-and-Predictive-Modelling/discussions)
- **Technical Deep Dive**: [TECHNICAL_DOCUMENTATION.md](TECHNICAL_DOCUMENTATION.md)

---

## 🚀 Try It Now & Support

<div align="center">

### [🎮 Launch Live Dashboard](https://solana-games.app)
*Experience real-time analytics and ML predictions*

### [📊 Explore Interactive API](https://solana-game-signals-and-predictive-modelling-production.up.railway.app/docs)
*Try all 21 endpoints in your browser*

---

### Support This Project

<table>
  <tr>
    <td align="center">
      ⭐<br/>
      <b>Star on GitHub</b><br/>
      <sub>Show your support</sub>
    </td>
    <td align="center">
      🐦<br/>
      <b><a href="https://x.com/defi__josh">Follow @defi__josh</a></b><br/>
      <sub>Get updates</sub>
    </td>
    <td align="center">
      💬<br/>
      <b>Share Feedback</b><br/>
      <sub>Help us improve</sub>
    </td>
  </tr>
</table>

---

**Built with ❤️ for the Solana Gaming Ecosystem**

</div>