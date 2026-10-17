# 🖼️ BG Remover — AI Background Remover

> Remove image backgrounds instantly with AI. Free, fast, and no signup required.

🌐 **[imagesbackgroundremover.com](https://imagesbackgroundremover.com)**

## ✨ Features

- **🎯 AI Background Removal** — Powered by advanced AI that detects subjects and removes backgrounds in seconds
- **📸 Drag & Drop Upload** — Supports JPG, PNG, and WebP (up to 10 MB)
- **🔍 Before/After Comparison** — Interactive slider to compare original and processed images
- **⬇️ One-Click Download** — Download transparent PNG with a single click
- **📱 Fully Responsive** — Works flawlessly on mobile, tablet, and desktop
- **🌍 Multi-language** — English and Chinese (中文) support
- **🔒 Privacy First** — Images are processed in real-time and never stored
- **🔍 SEO Optimized** — JSON-LD, Open Graph, Twitter Cards, semantic HTML, blog

## 🚀 Live Demo

Try it now at **[imagesbackgroundremover.com](https://imagesbackgroundremover.com)**

### How It Works

1. **Upload** your image (JPG, PNG, or WebP)
2. **AI processes** and removes the background automatically
3. **Download** the transparent PNG result

## 🛠️ Tech Stack

- [Next.js 16](https://nextjs.org/) — App Router with Edge Runtime
- [TypeScript](https://www.typescriptlang.org/)
- [Tailwind CSS 4](https://tailwindcss.com/)
- [Cloudflare Workers](https://workers.cloudflare.com/) — Edge deployment
- [PayPal](https://developer.paypal.com/) — Payment processing

## 📁 Project Structure

```
src/
├── app/
│   ├── api/
│   │   ├── remove-bg/route.ts     # Background removal API
│   │   ├── auth/                   # Google OAuth authentication
│   │   └── paypal/                 # Payment & subscription handling
│   ├── blog/                       # SEO blog with articles
│   │   ├── page.tsx                # Blog index
│   │   └── [slug]/page.tsx         # Individual blog posts
│   ├── pricing/page.tsx            # Pricing plans
│   ├── account/page.tsx            # User dashboard
│   ├── layout.tsx                  # Root layout with SEO metadata
│   └── page.tsx                    # Main app page
├── components/
│   ├── ImageUploader.tsx           # Drag & drop upload
│   ├── ImageComparison.tsx         # Before/after slider
│   ├── DownloadButton.tsx          # Download result as PNG
│   ├── FAQ.tsx                     # FAQ accordion
│   ├── HowItWorks.tsx             # 3-step process section
│   ├── Header.tsx                  # Navigation header
│   ├── Footer.tsx                  # Page footer
│   └── ...
└── lib/
    ├── i18n.ts                     # Internationalization (en/zh)
    ├── blog.ts                     # Blog post data & utilities
    └── ...
```

## 🏁 Getting Started

### Prerequisites

- Node.js 18+
- A [Remove.bg](https://www.remove.bg/api) API key

### Setup

```bash
# Clone the repo
git clone https://github.com/turnturn/image-background-remover.git
cd image-background-remover

# Install dependencies
npm install

# Copy environment variables
cp .env.example .env.local

# Edit .env.local and add your API key
# REMOVE_BG_API_KEY=your_api_key_here

# Start the dev server
npm run dev
```

Open [http://localhost:3000](http://localhost:3000).

### Production Build

```bash
npm run build
npm start
```

### Deploy to Cloudflare Workers

```bash
npm run deploy
```

## 📄 License

MIT

---

**[Try BG Remover Free →](https://imagesbackgroundremover.com)**
