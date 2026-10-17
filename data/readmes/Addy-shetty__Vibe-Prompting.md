# 🎨 Vibe Prompting

<div align="center">

**AI-Powered Prompt Generator with Smart Credit System**

Transform your ideas into powerful AI prompts instantly. Built with React, TypeScript, and Supabase.

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?style=for-the-badge&logo=vercel)](vibe-prompting-mod5hmq3z-harshithms1922-8008s-projects.vercel.app)
[![Vercel](https://img.shields.io/badge/Deployed%20on-Vercel-black?style=for-the-badge&logo=vercel)](https://vercel.com)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](./LICENSE)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.5-3178C6?style=flat-square&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![React](https://img.shields.io/badge/React-18.3-61DAFB?style=flat-square&logo=react&logoColor=black)](https://reactjs.org/)
[![Vite](https://img.shields.io/badge/Vite-5.4-646CFF?style=flat-square&logo=vite&logoColor=white)](https://vitejs.dev/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-3.4-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)
[![Supabase](https://img.shields.io/badge/Supabase-PostgreSQL-3ECF8E?style=flat-square&logo=supabase&logoColor=white)](https://supabase.com/)
[![Framer Motion](https://img.shields.io/badge/Framer-Motion-0055FF?style=flat-square&logo=framer&logoColor=white)](https://www.framer.com/motion/)

[🚀 Live Demo](https://vibe-prompting.vercel.app/) • [📖 Documentation](#-documentation) • [🤝 Contributing](./CONTRIBUTING.md) • [🔒 Security](./SECURITY.md)

</div>

---

## 📑 Table of Contents

- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [🚀 Quick Start](#-quick-start)
- [📁 Project Structure](#-project-structure)
- [📖 Documentation](#-documentation)
- [🎮 Usage Guide](#-usage-guide)
- [🤝 Contributing](#-contributing)
- [📝 License](#-license)
- [📧 Contact](#-contact)

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🚀 Core Capabilities
- ✅ **AI Prompt Generation** - Powered by Google Gemini 2.0 Flash & OpenRouter
- ✅ **14 Specialized Categories** - Frontend, Backend, DevOps, Security & more
- ✅ **Smart Tag System** - Organize with up to 5 tags per prompt
- ✅ **Real-time Streaming** - Watch prompts generate live
- ✅ **Public Gallery** - Discover community creations

</td>
<td width="50%">

### 🎯 User Experience
- ✅ **Anonymous Preview** - 3 free generations, no signup needed
- ✅ **50 Free Credits** - For registered users
- ✅ **Dark/Light Theme** - Beautiful adaptive UI
- ✅ **One-Click Copy** - Instant clipboard functionality
- ✅ **Fully Responsive** - Desktop, tablet & mobile ready

</td>
</tr>
</table>

### 🔒 Enterprise-Grade Security
Built with security at its core. [Learn more →](./SECURITY.md)

- ✅ **Row Level Security (RLS)** - Database-level access control
- ✅ **IDOR Protection** - Users can only access their own data
- ✅ **Input Validation** - Zod schemas + XSS prevention
- ✅ **Rate Limiting** - Protection against abuse
- ✅ **Password Strength** - Enforced requirements with visual feedback

### 📊 Fair Usage Credit System
[View detailed credit system documentation →](./docs/CREDITS_SYSTEM.md)

| User Type | Generations | Prompt Views | Storage | Cost |
|-----------|-------------|--------------|---------|------|
| 🎭 Anonymous | 3 free | 3 free views | localStorage | Free |
| ✨ Registered | 7 credits | Unlimited | Database | Free |
| Price          | Comming soon | 

---

## 🛠️ Tech Stack

<table>
<tr>
<td width="33%">

### Frontend
- ⚛️ **React 18.3** - UI library
- 📘 **TypeScript 5.5** - Type safety
- ⚡ **Vite 5.4** - Build tool
- 🎨 **Tailwind CSS** - Styling
- 🎬 **Framer Motion** - Animations
- 🛣️ **React Router** - Routing

</td>
<td width="33%">

### Backend
- 🗄️ **Supabase** - BaaS platform
- 🐘 **PostgreSQL** - Database with RLS
- ⚡ **Edge Functions** - Serverless

</td>
<td width="33%">

### AI Integration
- 🤖 **Gemini 2.0 Flash** - Primary model
- 🦙 **Llama 3.2** - Fallback via OpenRouter

</td>
</tr>
</table>

---

## 🚀 Quick Start

> **📋 Prerequisites:** Node.js 18+, npm, Supabase account (free), and at least one AI API key

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Addy-shetty/Vibe-Prompting.git
cd Vibe-Prompting
```

### 2️⃣ Install Dependencies

```bash
npm install
```

### 3️⃣ Set Up Environment Variables

Copy `.env.example` to `.env` and fill in your credentials:

```bash
cp .env.example .env
```

**Required variables:**
```env
# Supabase (Get from: https://app.supabase.com/project/_/settings/api)
VITE_SUPABASE_URL=your_supabase_project_url
VITE_SUPABASE_ANON_KEY=your_supabase_anon_key

# AI API Keys (choose at least one)
VITE_GEMINI_API_KEY=your_gemini_api_key        # https://aistudio.google.com/apikey
VITE_OPENROUTER_API_KEY=your_openrouter_key    # https://openrouter.ai/keys
```

> 💡 **Tip:** See [.env.example](./.env.example) for detailed setup instructions

### 4️⃣ Set Up Supabase Database

Run migrations in the [Supabase SQL Editor](https://app.supabase.com):

```bash
# Or use Supabase CLI
npx supabase db reset
```

📚 [Detailed database setup guide →](./docs/SUPABASE_SETUP.md)

### 5️⃣ Start Development Server

```bash
npm run dev
```

🎉 Visit **http://localhost:5173** and start creating prompts!

### 🚢 Build for Production

```bash
npm run build
npm run preview
```

---

## 📁 Project Structure

```
vibe-prompting/
├── src/
│   ├── components/        # React components
│   ├── pages/             # Page components
│   ├── context/           # React context
│   ├── hooks/             # Custom hooks
│   ├── lib/               # Utilities
│   └── styles/            # Global styles
├── supabase/
│   └── migrations/        # Database migrations
├── docs/                  # Documentation
└── public/                # Static assets
```

---

## 📖 Documentation

### 📚 Core Documentation
| Document | Description |
|----------|-------------|
| [🔒 Security Policy](./SECURITY.md) | Vulnerability reporting & security measures |
| [🤝 Contributing Guide](./CONTRIBUTING.md) | How to contribute to this project |
| [📜 MIT License](./LICENSE) | Open source license details |

### 🔧 Technical Guides
| Guide | Description |
|-------|-------------|
| [🔐 Authentication](./docs/AUTH_GUIDE.md) | Auth implementation & user flows |
| [💳 Credits System](./docs/CREDITS_SYSTEM.md) | How credits work & limitations |
| [🗄️ Database Setup](./docs/SUPABASE_SETUP.md) | Supabase configuration & migrations |
| [🛡️ Security Details](./docs/SECURITY_IMPLEMENTATION_FULL.md) | Complete security implementation |

### 🔗 Quick Links
- 📋 [.env.example](./.env.example) - Environment variables template
- 🗂️ [supabase/migrations](./supabase/migrations/) - Database migration files
- 🧩 [src/components](./src/components/) - React components
- 🎣 [src/hooks](./src/hooks/) - Custom React hooks

---

## 🎮 Usage Guide

### 🎭 For Anonymous Users

1. 🏠 **Visit Homepage** - Explore example prompts
2. 🎯 **Click a Category** - Choose your prompt type
3. ✨ **Generate** - Create up to 3 free prompts
4. 📋 **Copy** - One-click clipboard copy
5. 💾 **Sign Up** - To save prompts permanently

> ⚠️ **Note:** Anonymous prompts are stored in localStorage and may be lost

### ✨ For Registered Users

1. 📝 **Sign Up** - Get 50 free credits instantly
2. 🎨 **Generate Prompts** - Use your credits wisely
3. 🏷️ **Add Tags** - Organize with up to 5 tags
4. 🌍 **Make Public** - Share with the community
5. 📚 **Browse Gallery** - Discover & save others' prompts
6. ⚙️ **Manage** - Edit or delete your creations

### 💡 Pro Tips

- 🎯 **Be Specific** - More detailed inputs = better prompts
- 🏷️ **Use Tags** - Makes finding prompts easier later
- 🌍 **Go Public** - Help the community & get discovered
- 💳 **Track Credits** - Visible in navbar when logged in

---

## 🤝 Contributing

We ❤️ contributions! Whether it's bug reports, feature requests, or code contributions - all are welcome!

### 🚀 Quick Contribution Steps

1. 🍴 **Fork** the repository
2. 🌿 **Create** a feature branch
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. 💻 **Code** your changes
4. ✅ **Commit** with clear messages
   ```bash
   git commit -m 'feat: Add AmazingFeature'
   ```
5. 📤 **Push** to your branch
   ```bash
   git push origin feature/AmazingFeature
   ```
6. 🎯 **Open** a Pull Request

### 📋 Contribution Guidelines

Please read our [**Contributing Guide**](./CONTRIBUTING.md) for:
- 📜 Code of Conduct
- 🛠️ Development setup
- 💻 Coding standards
- ✉️ Commit message conventions
- 🧪 Testing requirements

### 🐛 Found a Bug?

[Open an issue](https://github.com/Addy-shetty/Vibe-Prompting/issues) with:
- Clear description
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)

### 💡 Feature Request?

We'd love to hear your ideas! [Create a feature request](https://github.com/Addy-shetty/Vibe-Prompting/issues) and describe:
- The problem it solves
- Proposed solution
- Alternative approaches

---

## 📝 License

This project is licensed under the **MIT License** - see the [**LICENSE**](./LICENSE) file for details.

### 📜 What This Means

✅ **Commercial use** - Use it in your business  
✅ **Modification** - Change and customize freely  
✅ **Distribution** - Share with anyone  
✅ **Private use** - Use for personal projects  

⚠️ **Conditions:**
- Include copyright notice
- Include license copy

📖 [Read the full MIT License →](./LICENSE)

---

## 🙏 Acknowledgments

This project wouldn't be possible without these amazing tools and services:

| Technology | Purpose | License |
|------------|---------|---------|
| [Google Gemini](https://ai.google.dev/) | AI prompt generation | Google AI |
| [Supabase](https://supabase.com/) | Backend infrastructure | Apache 2.0 |
| [React](https://reactjs.org/) | UI framework | MIT |
| [TypeScript](https://www.typescriptlang.org/) | Type safety | Apache 2.0 |
| [Tailwind CSS](https://tailwindcss.com/) | Styling | MIT |
| [Framer Motion](https://www.framer.com/motion/) | Animations | MIT |
| [Vite](https://vitejs.dev/) | Build tool | MIT |

Special thanks to:
- 🌟 All [contributors](https://github.com/Addy-shetty/Vibe-Prompting/graphs/contributors)
- 🐛 Bug reporters and testers
- 💡 Feature requesters
- ⭐ Everyone who starred this repo

---

## 📧 Contact

<div align="center">

### Harshith M S (Addy Shetty)

[![GitHub](https://img.shields.io/badge/GitHub-@Addy--shetty-181717?style=for-the-badge&logo=github)](https://github.com/Addy-shetty)
[![Email](https://img.shields.io/badge/Email-Harshithms@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:Harshithms@gmail.com)

</div>

### 💬 Get in Touch

- 💼 **GitHub:** [@Addy-shetty](https://github.com/Addy-shetty)
- 📧 **Email:** Harshithms@gmail.com
- 🐛 **Issues:** [Report bugs](https://github.com/Addy-shetty/Vibe-Prompting/issues)
- 💡 **Discussions:** [Join conversations](https://github.com/Addy-shetty/Vibe-Prompting/discussions)

---

<div align="center">

### 🌟 Show Your Support

If you find this project useful, please consider:

⭐ **Starring this repository**  
🍴 **Forking and contributing**  
🐛 **Reporting bugs**  
💡 **Suggesting features**  
📢 **Sharing with others**

---

**Made with ❤️ by [Addy Shetty](https://github.com/Addy-shetty)**

[![Star History](https://img.shields.io/github/stars/Addy-shetty/Vibe-Prompting?style=social)](https://github.com/Addy-shetty/Vibe-Prompting/stargazers)
[![Forks](https://img.shields.io/github/forks/Addy-shetty/Vibe-Prompting?style=social)](https://github.com/Addy-shetty/Vibe-Prompting/network/members)
[![Issues](https://img.shields.io/github/issues/Addy-shetty/Vibe-Prompting)](https://github.com/Addy-shetty/Vibe-Prompting/issues)

**Thank you for visiting! Happy Prompting! 🎨✨**

[⬆ Back to Top](#-vibe-prompting)

</div>
