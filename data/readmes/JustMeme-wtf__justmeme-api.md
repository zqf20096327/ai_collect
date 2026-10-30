# justmeme.wtf API

Free, open meme API with 2,400+ templates. No auth required.

**Base URL:** `https://justmeme.wtf/api/v1`

**Docs:** [justmeme.wtf/api-docs](https://justmeme.wtf/api-docs)

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/templates` | List all templates (paginated) |
| GET | `/templates/search?q=drake` | Search templates by name |
| GET | `/templates/:slug` | Get single template details |
| GET | `/trending` | Top 20 trending templates |
| GET | `/categories` | List all categories |
| GET | `/random` | Get a random template |
| POST | `/ai-generate` | AI-powered meme generation |

## Quick Start

### JavaScript

```javascript
// Get all templates
const res = await fetch('https://justmeme.wtf/api/v1/templates?limit=10');
const data = await res.json();
console.log(data.templates);

// Search for a template
const search = await fetch('https://justmeme.wtf/api/v1/templates/search?q=drake');
const results = await search.json();

// Get a random template
const random = await fetch('https://justmeme.wtf/api/v1/random');
const meme = await random.json();

// AI generate a meme
const ai = await fetch('https://justmeme.wtf/api/v1/ai-generate', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ prompt: 'something funny about debugging code' })
});
const generated = await ai.json();
console.log(generated);
// { success: true, template: "drake-hotline-bling", top_text: "...", bottom_text: "...", editor_url: "..." }
```

### Python

```python
import requests

# Get templates
r = requests.get('https://justmeme.wtf/api/v1/templates', params={'limit': 10})
templates = r.json()['templates']

# Search
r = requests.get('https://justmeme.wtf/api/v1/templates/search', params={'q': 'drake'})
results = r.json()['templates']

# Random template
r = requests.get('https://justmeme.wtf/api/v1/random')
meme = r.json()['template']

# AI generate
r = requests.post('https://justmeme.wtf/api/v1/ai-generate',
    json={'prompt': 'working from home vs office'})
print(r.json())
```

### cURL

```bash
# List templates
curl https://justmeme.wtf/api/v1/templates?limit=5

# Search
curl https://justmeme.wtf/api/v1/templates/search?q=spongebob

# Random
curl https://justmeme.wtf/api/v1/random

# AI generate
curl -X POST https://justmeme.wtf/api/v1/ai-generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "monday morning meetings"}'
```

## Rate Limits

- **60 requests per minute** per IP address
- No authentication required
- CORS enabled (use from any origin)

## Response Format

All responses use a consistent envelope:

```json
{
  "success": true,
  "templates": [...],
  "total": 2393,
  "page": 1,
  "limit": 20
}
```

Errors:

```json
{
  "success": false,
  "error": "Error description"
}
```

## Templates

The API serves 2,400+ meme templates including all the classics:

- Drake Hotline Bling
- Distracted Boyfriend
- Expanding Brain
- Surprised Pikachu
- This Is Fine
- Stonks
- Woman Yelling at Cat
- And 2,390+ more...

## AI Meme Generation

The `/ai-generate` endpoint uses AI to pick the best template and write meme text based on your prompt. Just describe what you want a meme about, and it returns the template, text, and a direct link to the editor.

## Links

- **Website:** [justmeme.wtf](https://justmeme.wtf)
- **API Docs:** [justmeme.wtf/api-docs](https://justmeme.wtf/api-docs)
- **Make a Meme:** [justmeme.wtf](https://justmeme.wtf)

## License

MIT
