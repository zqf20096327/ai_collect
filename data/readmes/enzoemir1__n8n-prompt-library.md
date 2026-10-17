<p align="center">
  <img src="https://img.shields.io/badge/prompts-20-00D9FF?style=for-the-badge" alt="20 Prompts">
  <img src="https://img.shields.io/badge/categories-6-FF6D5A?style=for-the-badge" alt="6 Categories">
  <img src="https://img.shields.io/badge/platform-n8n-FF6D5A?style=for-the-badge" alt="n8n">
  <img src="https://img.shields.io/badge/ready_to_use-yes-3fb950?style=for-the-badge" alt="Ready to Use">
  <img src="https://img.shields.io/badge/license-MIT-FFD700?style=for-the-badge" alt="MIT">
  <img src="https://img.shields.io/github/stars/enzoemir1/n8n-prompt-library?style=for-the-badge&color=FFD700" alt="Stars">
</p>

<h1 align="center">n8n Prompt Library</h1>

<p align="center">
  <strong>20 production-ready AI prompts optimized for n8n workflows.</strong><br/>
  Copy-paste system prompts with model recommendations, cost estimates, and n8n integration tips.
</p>

---

## Why This Exists

Building AI workflows in n8n is easy. Writing good prompts for them is hard.

This library gives you **battle-tested system prompts** that you can drop directly into your n8n OpenAI / Anthropic / Ollama nodes. Each prompt includes:

- The full system prompt text (copy-paste ready)
- Recommended model and temperature settings
- Estimated cost per run
- A user prompt template with `{{placeholders}}` for n8n expressions
- Real example output
- n8n-specific integration tips

---

## Prompt Categories

### Content Generation (5 prompts)

| Prompt | Description | Model | Cost |
|--------|-------------|-------|------|
| [Twitter Thread Generator](prompts/content-generation/twitter-thread-generator.json) | Blog post to 5-7 tweet thread with hooks and CTAs | gpt-4o-mini | ~$0.003 |
| [LinkedIn Post Writer](prompts/content-generation/linkedin-post-writer.json) | Article to professional LinkedIn post (1200-1800 chars) | gpt-4o-mini | ~$0.003 |
| [Instagram Caption Creator](prompts/content-generation/instagram-caption-creator.json) | Content to caption with emojis, CTA, and hashtag block | gpt-4o-mini | ~$0.002 |
| [Facebook Post Adapter](prompts/content-generation/facebook-post-adapter.json) | Content to conversational Facebook post that drives comments | gpt-4o-mini | ~$0.002 |
| [YouTube Script Outline](prompts/content-generation/youtube-script-outline.json) | Topic to structured 8-12 min video outline with B-roll ideas | gpt-4o-mini | ~$0.003 |

### Data Processing (3 prompts)

| Prompt | Description | Model | Cost |
|--------|-------------|-------|------|
| [Web Scrape Extractor](prompts/data-processing/web-scrape-extractor.json) | Raw HTML to structured JSON with title, data points, sentiment | gpt-4o-mini | ~$0.005 |
| [CSV Data Cleaner](prompts/data-processing/csv-data-cleaner.json) | Fix dates, names, emails, duplicates in messy CSV data | gpt-4o-mini | ~$0.005 |
| [JSON Schema Transformer](prompts/data-processing/json-schema-transformer.json) | Transform JSON between schemas with field mapping rules | gpt-4o-mini | ~$0.003 |

### Email (3 prompts)

| Prompt | Description | Model | Cost |
|--------|-------------|-------|------|
| [Cold Email Writer](prompts/email/cold-email-writer.json) | Personalized B2B outreach with subject line, no spam triggers | gpt-4o-mini | ~$0.003 |
| [Email Reply Generator](prompts/email/email-reply-generator.json) | Tone-matching replies with action item extraction | gpt-4o-mini | ~$0.003 |
| [Newsletter Creator](prompts/email/newsletter-creator.json) | Bullet points to complete newsletter with sections and CTA | gpt-4o-mini | ~$0.004 |

### Classification (3 prompts)

| Prompt | Description | Model | Cost |
|--------|-------------|-------|------|
| [Email Classifier](prompts/classification/email-classifier.json) | Classify into urgent/important/info/spam with confidence score | gpt-4o-mini | ~$0.001 |
| [Sentiment Analyzer](prompts/classification/sentiment-analyzer.json) | Multi-dimensional sentiment with emotion detection and business signals | gpt-4o-mini | ~$0.001 |
| [Lead Scorer](prompts/classification/lead-scorer.json) | Score leads 1-100 based on company, role, engagement, recency | gpt-4o-mini | ~$0.002 |

### Customer Support (3 prompts)

| Prompt | Description | Model | Cost |
|--------|-------------|-------|------|
| [Support Ticket Responder](prompts/customer-support/support-ticket-responder.json) | Empathetic, step-by-step support responses with escalation detection | gpt-4o-mini | ~$0.002 |
| [FAQ Matcher](prompts/customer-support/faq-matcher.json) | Match questions to FAQ entries with confidence and related suggestions | gpt-4o-mini | ~$0.002 |
| [Escalation Detector](prompts/customer-support/escalation-detector.json) | Detect frustrated customers, legal threats, churn signals | gpt-4o-mini | ~$0.001 |

### SEO (3 prompts)

| Prompt | Description | Model | Cost |
|--------|-------------|-------|------|
| [Meta Description Writer](prompts/seo/meta-description-writer.json) | 3 variants at 150-160 chars with keyword, benefit, CTA | gpt-4o-mini | ~$0.001 |
| [Keyword Extractor](prompts/seo/keyword-extractor.json) | Primary, secondary, long-tail keywords with search intent | gpt-4o-mini | ~$0.002 |
| [Blog Title Optimizer](prompts/seo/blog-title-optimizer.json) | 5 title variants: how-to, listicle, question, power-word, curiosity-gap | gpt-4o-mini | ~$0.001 |

---

## How to Use in n8n

### 1. Pick a prompt

Browse the categories above and open the JSON file for the prompt you need.

### 2. Copy the system prompt

Each JSON file has a `system_prompt` field. Copy this into your n8n AI node's **System Message** field.

### 3. Set up the user prompt

Use the `user_prompt_template` as your **User Message**. Replace `{{placeholders}}` with n8n expressions:

```
// Example: Twitter Thread Generator
// In the User Message field:
Convert this blog post into a Twitter thread:

{{ $json.content }}
```

### 4. Configure the model

Each prompt specifies the recommended `model` and `temperature`. Set these in your n8n node's parameters.

### 5. Parse the output

Most prompts return JSON. Use n8n's **Code** node or **JSON Parse** to extract the fields you need.

---

## Prompt File Format

Every prompt follows this schema:

```json
{
  "id": "unique-slug",
  "name": "Display Name",
  "category": "content-generation",
  "description": "One-line description",
  "model": "gpt-4o-mini",
  "estimated_cost": "$0.003 per run",
  "n8n_node": "OpenAI Chat Model",
  "temperature": 0.7,
  "max_tokens": 1000,
  "system_prompt": "The full system prompt...",
  "user_prompt_template": "Template with {{placeholders}}...",
  "example_output": "What the prompt produces...",
  "tips": ["n8n-specific tips"]
}
```

---

## Cost Overview

Running all 20 prompts once costs approximately **$0.05** with gpt-4o-mini.

| Use Case | Prompts Used | Cost per Run | Daily (50 runs) | Monthly |
|----------|-------------|--------------|------------------|---------|
| Content repurposing | 4 (Twitter + LinkedIn + IG + FB) | $0.010 | $0.50 | $15 |
| Email automation | 2 (Classifier + Reply) | $0.004 | $0.20 | $6 |
| Support bot | 3 (Responder + FAQ + Escalation) | $0.005 | $0.25 | $7.50 |
| SEO pipeline | 3 (Keywords + Titles + Meta) | $0.004 | $0.20 | $6 |
| Lead pipeline | 2 (Scorer + Cold Email) | $0.005 | $0.25 | $7.50 |

**Want to calculate exact costs for your workflow?** Use our [n8n AI Cost Calculator](https://github.com/enzoemir1/n8n-cost-calculator).

---

## Model Guide

| Task Type | Recommended | Why |
|-----------|-------------|-----|
| Content generation | gpt-4o-mini | Best quality/cost ratio for creative text |
| Classification | gpt-4o-mini (temp 0.1) | Cheap, fast, accurate for structured output |
| Data extraction | gpt-4o-mini (temp 0.2) | Consistent output at low cost |
| Complex reasoning | gpt-4o | When mini's quality isn't sufficient |
| Free alternative | Llama 3.1 70B (Groq) | Zero cost, good for development |
| Local/private | Mistral 7B (Ollama) | No API calls, data stays local |

---

## Contributing

Have a prompt that works well in your n8n workflows? Contributions are welcome!

1. Fork this repo
2. Add your prompt JSON to the appropriate category folder
3. Follow the schema format above
4. Include real, tested `example_output`
5. Submit a PR

---

## Also by Automatia BCN

- **[autoflow-n8n-workflows](https://github.com/enzoemir1/autoflow-n8n-workflows)** — 8 free AI automation workflows for n8n
- **[n8n-telegram-approval](https://github.com/enzoemir1/n8n-telegram-approval)** — Human-in-the-loop approval via Telegram
- **[n8n-cost-calculator](https://github.com/enzoemir1/n8n-cost-calculator)** — Estimate AI workflow costs before you build
- **[free-ai-prompts](https://github.com/enzoemir1/free-ai-prompts)** — 90 free AI prompts for ChatGPT, Gemini & more

---

## License

MIT License — free for personal and commercial use.

---

<p align="center">
  <strong>If these prompts save you time, a star would mean a lot!</strong>
</p>
