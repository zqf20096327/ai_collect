# 📈 NeuroTrade AI - Professional Trading Signals

NeuroTrade AI is a modern, high-performance web application that provides institutional-grade trading signals using advanced Artificial Intelligence models. Built with React and TypeScript, it integrates real-time charts and highly accurate AI predictions.

## ✨ Features
- **Real-Time Market Charts**: Integrated TradingView Advanced Charts.
- **AI Signal Generation**: Utilizes powerful LLMs for technical analysis and probability scoring.
- **Premium UI/UX**: Professional glassmorphism design with responsive market indicators.
- **Crypto & Forex Support**: Live data analysis with accurate market-hours logic for Forex pairs.

## 🚀 Quick Start & Setup

To make this your own fully-functional AI trading platform, follow these steps:

### 1. Get an OpenRouter API Key
This app uses **OpenRouter** to access state-of-the-art AI models for generating trading signals.
1. Create an account at [OpenRouter.ai](https://openrouter.ai/).
2. Navigate to your Account settings and go to the **Keys** section.
3. Click **Create Key** and copy it securely.

### 2. Add Your API Key
In the source code, you need to provide your API key to authenticate requests.

Go to the file: `src/services/ai.ts`

Replace the placeholder API key with your own on **Line 1**:
```typescript
// Replace this with your actual OpenRouter key
export const OPENROUTER_API_KEY = "your-openrouter-api-key-here";
```
*(Alternatively, you can set it via an environment variable `VITE_OPENROUTER_API_KEY` for better security).*

### 3. Install & Run Locally

Install the required dependencies:
```bash
npm install
```

Start the development server:
```bash
npm run dev
```

### 4. Deploy to Vercel (1-Click Deploy)
This project is configured and ready to be deployed on **Vercel**.
1. Push your code to a GitHub repository.
2. Go to [Vercel](https://vercel.com/) and create a "New Project".
3. Import your GitHub repository. Vercel will automatically detect `Vite` settings and the `vercel.json` routing configuration.
4. Click **Deploy**. Your professional AI trading platform is now live!

---
*Disclaimer: Trading involves significant risk. This tool is for educational purposes and provides AI-generated analysis based on historical patterns, not guaranteed financial advice.*
