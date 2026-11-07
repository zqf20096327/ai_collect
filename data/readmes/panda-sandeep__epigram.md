<div align="center">

<img src="https://epigram.news/static/images/epigram-og.png" alt="Epigram - AI-powered news summaries" width="100%" />

# Epigram

[![Announcement](https://img.shields.io/badge/X-Announcement-black)](https://x.com/Sandeepg33k/status/1875373269307814113)
[![License](https://img.shields.io/badge/license-AGPL--3.0-blue)](/LICENSE.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/panda-sandeep/epigram/pulls)

Open-Source, Free, and AI-Powered News in Short.

**[Try Epigram.news »](https://epigram.news)**

[Features](#-features) •
[Tech Stack](#️-tech-stack) •
[Getting Started](#-getting-started) •
[Deployment](#-deployment) •
[Contributing](#-contributing)

<p align="center">
  <em>Built by humans, optimized by AI, with ❤️ from SF.</em>
</p>

</div>

## 🎯 Overview

Epigram simplifies the way you stay informed. With AI, it delivers quick, clear summaries from reliable sources, so you get the news without the overwhelm. For more details, dive into deeper analysis or explore topics you care about — all in a feed tailored to your interests.

Our goal is to use AI to make quality news easy to access, understand, and personalize. We're focused on connecting you with trusted sources while cutting through the noise, so you get the information that matters most.

## ✨ Features

- 🎯 **Personalized News Feed** - Get a curated news feed based on your preferences and interests
- 🤖 **AI-powered Summaries** - Get concise news summaries and in-depth analysis
- ✅ **Trusted Sources** - Access news from reputable sources worldwide
- 🎨 **User-friendly Interface** - Enjoy a sleek, intuitive interface designed for a seamless reading experience
- 📱 **Responsive Design** - Access Epigram on any device, anywhere, anytime (Add to home screen on Safari!)
- 🔍 **AI Deep dive** - Get in-depth analysis of news articles using AI

## 🛠️ Tech Stack

- [Next.js](https://nextjs.org/) - React framework for production
- [Exa](https://exa.ai/) - AI-powered news summaries
- [Google Cloud Run](https://cloud.google.com/run) - Serverless deployment
- [AI SDK](https://sdk.vercel.ai/docs) & [OpenAI](https://openai.com/) - AI analysis with `gpt-4o-mini`
- [Mediastack](https://mediastack.com/) - News data API
- [Upstash](https://upstash.com/) - Redis for caching and rate limiting

## 🚀 Getting Started

### Prerequisites

- Node.js 20+
- npm or yarn
- Git

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/panda-sandeep/epigram
    ```

2. **Navigate to the project directory**:
    ```bash
    cd epigram
    ```

3. **Install dependencies**:
    ```bash
    npm install
    ```

4. **Set up environment variables**:
    Copy `.env.example` to `.env.local` and configure:
    
    ```env
    MEDIASTACK_API_KEY=your_mediastack_api_key
    EXA_API_KEY=your_exa_api_key
    OPENAI_API_KEY=your_openai_api_key
    BASE_URL=http://localhost:3000
    UPSTASH_REDIS_REST_URL=your_upstash_redis_rest_url
    UPSTASH_REDIS_REST_TOKEN=your_upstash_redis_rest_token
    PER_TOPIC_NEWS_LIMIT=5
    NEXT_PUBLIC_GA_ID=your_google_analytics_id
    EPIGRAM_SECRET_HEADER_NAME=X-Epigram-Secret
    EPIGRAM_CRON_SECRET=your_cron_secret
    ```

5. **Start development server**:
    ```bash
    npm run dev
    ```

6. **Populate news data**:
    ```bash
    curl --header "X-Epigram-Secret: <your-secret>" http://localhost:3000/api/news/populate
    ```    

7. **View the app**:
    Open [http://localhost:3000](http://localhost:3000) in your browser

## 📦 Deployment

1. **Install dependencies**:
    ```bash
    npm install
    ```

2. **Build for production**:
    ```bash
    npm run build
    ```

3. **Start production server**:
    ```bash
    npm start
    ```

> **Note**: Set up a cron job to periodically hit `/api/news/populate` for fresh news content.

Deploy to any platform supporting Next.js:
- [Vercel](https://vercel.com?utm_source=github&utm_medium=epigram)
- [Netlify](https://netlify.com?utm_source=github&utm_medium=epigram)
- [Google Cloud Run](https://cloud.google.com/run?utm_source=github&utm_medium=epigram)
- [AWS Amplify](https://aws.amazon.com/amplify?utm_source=github&utm_medium=epigram)

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. [Fork](https://github.com/panda-sandeep/epigram/fork) the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

You can also:
- [Report bugs](https://github.com/panda-sandeep/epigram/issues)
- [Request features](https://github.com/panda-sandeep/epigram/issues)
- [Submit PRs](https://github.com/panda-sandeep/epigram/pulls)

## 📝 License

This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0) - see the [LICENSE.md](/LICENSE.md) file for details.

---

<div align="center">
  <b>Contributors</b> &nbsp;•&nbsp; 
  <a href="https://x.com/sandeepg33k">Sandeep Panda</a> &nbsp;•&nbsp; 
  <a href="https://x.com/fazlerocks">Fazle</a>
</div>
