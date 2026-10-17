# Knowledge Chatbot

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/1e3pm/knowledge-chatbot)

A minimal, open-source, embeddable AI chatbot that answers questions from your website content via text or voice.

Add your website as a knowledge source, embed the widget, and let visitors chat with your content.

Built entirely on the Cloudflare stack and designed for easy self-hosting.

> Expect breaking changes. Backward compatibility is not guaranteed.

## How to use

Click "Deploy to Cloudflare". During setup, select 768 for the Vectorize index dimensions and cosine for the metric.

## Features

- Embeddable chatbot widget
- Answers questions from your website content
- Text and voice chat
- Website crawling and content indexing
- Vector search with Cloudflare Vectorize
- AI inference through Cloudflare Workers AI
- Fully self-hosted on Cloudflare
- No separate backend server required

## Cloudflare Stack

Knowledge Chatbot uses:

- Cloudflare Workers
- Cloudflare D1
- Cloudflare Durable Objects
- Cloudflare Vectorize
- Cloudflare Workers AI
- Cloudflare Browser Rendering
- Cloudflare KV
- Cloudflare Assets

## License

GNU Affero General Public License v3.0.
