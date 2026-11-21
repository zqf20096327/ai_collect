# eight-eye

Agent Skills for Claude Code: production-grade code standards, one skill per area.

**silk** = shared standards · **spider** = one framework or tool

## Skills

| Category | Skill | Covers |
|---|---|---|
| Backend | `backend-silk` | Structure, layering, errors, logging, config, security, request/response schemas |
| | `sql-silk` | PostgreSQL / MySQL / SQLite with SQLAlchemy or Django ORM |
| | `mongodb-silk` | MongoDB with PyMongo |
| | `fastapi-spider` | FastAPI |
| | `flask-spider` | Flask |
| | `django-spider` | Django REST Framework |
| | `node-spider` | Node.js / Express 5 |
| | `rag-spider` | RAG pipelines and LLM features |
| | `mcp-spider` | MCP servers and clients (FastMCP) |

More categories (frontend, design, editing) are planned.

## Install

**Claude Code**: copy the skills you want into your skills folder:

```bash
git clone git@github.com:VivekShevale/eight-eye.git
cp -r eight-eye/skills/backend/* ~/.claude/skills/
```

**claude.ai**: download a skill's `.zip` from [Releases](https://github.com/VivekShevale/eight-eye/releases) and upload it in Settings → Capabilities → Skills.

Spiders build on the silk skills, so install `backend-silk` plus the database skill you use alongside any spider.

## License

MIT
