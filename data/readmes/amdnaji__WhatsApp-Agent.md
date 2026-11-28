<div align="center">

# 🟠 Kahrman (كهرمان)
### Customizable AI WhatsApp Agent Framework & Starter Kit

**🌐 English | [🇸🇦 العربية](./README.ar.md)**

</div>

---

## 📖 Overview

**Kahrman (كهرمان)** is a flexible, plug-and-play **AI Agent Framework for WhatsApp**, designed with first-class support for Arabic (across all local dialects: Gulf, Egyptian, Levantine, and MSA) as well as English.

> [!NOTE]
> **Built for Any Industry — Travel is Just an Example!**
> While this repository currently includes a **Travel & Hotel Deals Assistant** as a complete working showcase, **Kahrman is not limited to tourism**. It is a blueprint and foundation that you can easily adapt to **any project or business domain** simply by changing the agent's persona and tools.

---

## 💎 Meaning of "Kahrman" & Why We Chose This Name

### What does "Kahrman" mean?
**Kahrman (كهرمان)** is the Arabic word for **Amber** — a rare, precious organic gemstone known for its warm golden glow. Formed over thousands of years, amber is historically famous for its natural electrostatic ability to **attract** objects and preserve valuable treasures within it.

### Why the name "Kahrman"?
1. **A Vessel for Any Precious Idea:** Just as amber preserves rare treasures inside it, **Kahrman** serves as the core container that holds your project's unique knowledge, tools, and business logic.
2. **Customer Attraction & Warmth:** Amber's natural power of attraction and warm golden hue reflect how the agent engages customers on WhatsApp—turning cold inquiries into warm, friendly conversations in their own dialect.
3. **The Trusted Steward:** In regional heritage, the name also echoes the concept of a *capable, trustworthy steward* who reliably manages tasks, answers inquiries, and captures opportunities across any field you assign to it.

---

## 🧩 One Core Engine, Endless Use Cases

The included **Hotel & Travel Agent** is a **proof-of-concept example**. You can repurpose **Kahrman** in minutes for any industry by editing two files:

1. **Change the Persona (`src/agent/persona.ts`):** Define your agent's role, tone, and strict domain boundaries.
2. **Plug in Your Tools (`src/agent/brain.ts` & `src/services/`):** Replace or add custom functions/APIs.

### Examples of What You Can Build with Kahrman:
| Industry / Project | Role of Kahrman | Custom Tool Example |
| :--- | :--- | :--- |
| 🏨 **Travel & Hospitality** *(Included Demo)* | Finds hotel deals & generates affiliate links | `searchHotels()` |
| 🛍️ **E-Commerce & Retail** | Recommends products, checks stock & tracks orders | `searchProducts()`, `getOrderStatus()` |
| 🏠 **Real Estate** | Matches buyers/renters with properties by budget & area | `findProperties()`, `bookViewing()` |
| 🏥 **Clinics & Healthcare** | Answers clinic FAQs & books patient appointments | `checkDoctorSlots()`, `bookAppointment()` |
| 🍽️ **Restaurants & Cafes** | Shares menu items, takes orders & reserves tables | `getMenu()`, `reserveTable()` |
| 💼 **B2B / Customer Support** | Handles tier-1 support tickets & lead qualification | `lookupTicket()`, `createLead()` |

---

## ✨ Key Features

- 🗣️ **Multi-Dialect Arabic & English:** Automatically detects and responds in the user's preferred dialect (Gulf/Saudi, Egyptian, Levantine, MSA, or English).
- 🛠️ **Tool Calling & Live Actions:** Built on the Vercel AI SDK to seamlessly execute backend functions, API calls, or web searches during conversation.
- 📅 **Context & Temporal Awareness:** Understands relative dates and conversational context across multi-turn WhatsApp chats.
- 🛡️ **Strict Domain Guardrails:** Easily lock the agent into your specific business scope so it politely declines off-topic questions.
- 🔌 **Multi-Provider AI Support:** Switch between **Google Gemini**, **OpenAI**, and **Anthropic Claude** via a single environment variable.
- 💬 **Direct Meta Cloud API Integration:** Connects directly to the official WhatsApp Business Cloud API with zero middleman fees.

---

## 🏗️ Tech Stack

- **Runtime & Web Framework:** Node.js + TypeScript + [Hono](https://hono.dev/) (ultra-fast and lightweight webhook handling).
- **AI Agent Brain:** [Vercel AI SDK (`ai`)](https://sdk.vercel.ai/) supporting Google Gemini, OpenAI, and Anthropic Claude.
- **External Tools (Demo):** Live web search via Serper.dev with dynamic affiliate deep-link generation.
- **WhatsApp Gateway:** Official **Meta WhatsApp Cloud API**.

---

## 📁 Project Structure

```text
kahrman/
├── src/
│   ├── index.ts               # Hono server & WhatsApp Webhook endpoints (GET/POST /webhook)
│   ├── config.ts              # Unified environment variables & provider config
│   ├── cli.ts                 # Interactive terminal CLI for local testing
│   ├── agent/
│   │   ├── persona.ts         # Agent persona & domain rules (Customize for your project!)
│   │   └── brain.ts           # Conversation memory & tool calling logic (Vercel AI SDK)
│   ├── services/
│   │   └── hotelSearch.ts     # Example service/tool (Replace or extend for your domain!)
│   └── whatsapp/
│       ├── client.ts          # WhatsApp Cloud API message sender (Meta Graph API)
│       └── types.ts           # TypeScript interfaces for WhatsApp webhook payloads
├── .env.example               # Example environment configuration
├── README.md                  # English documentation (Default)
├── README.ar.md               # Arabic documentation (النسخة العربية)
├── package.json
└── tsconfig.json
```

---

## 🚀 Quickstart

### 1. Clone the Repository & Configure Environment
```bash
git clone https://github.com/amdnaji/WhatsApp-Agent.git
cd WhatsApp-Agent
npm install
cp .env.example .env
```
Update `.env` with your preferred AI provider and API key:
```env
AI_PROVIDER=gemini        # Options: gemini | openai | anthropic
MODEL_NAME=gemini-2.5-flash
AI_API_KEY=your_api_key_here
```

### 2. Test in Terminal CLI (No WhatsApp Setup Needed)
You can chat with Kahrman directly in your terminal to test its persona and tool calling:
```bash
npm run cli
```

### 3. Start the Webhook Server
```bash
npm run dev
```
The server will start at `http://localhost:3000`.

---

## 📲 Connecting Meta WhatsApp Cloud API

1. Go to [Meta for Developers](https://developers.facebook.com/) and create a **Business** app.
2. Add the **WhatsApp** product to your app.
3. Copy your credentials into `.env`:
   - `META_PHONE_NUMBER_ID`: Your WhatsApp test or production Phone Number ID.
   - `META_ACCESS_TOKEN`: Your temporary or permanent Meta Graph API token.
4. Expose your local server to the internet using a tunnel like `ngrok`:
   ```bash
   ngrok http 3000
   ```
5. In the Meta App Dashboard > **WhatsApp > Configuration > Webhook**:
   - **Callback URL**: `https://your-ngrok-url.ngrok-free.app/webhook`
   - **Verify Token**: `kahrman_secret_token_2026` (or the value set in `META_WEBHOOK_VERIFY_TOKEN`).
   - Click **Verify and Save**, then subscribe to the **`messages`** webhook field.

---

## 👤 Author

- **amdnaji** — [@amdnaji](https://github.com/amdnaji)

