# Local RAG-based Research Assistant

Ask questions about your own PDF and text files, fully offline. The assistant retrieves the most relevant passages from your documents and answers with a local LLM (Ollama + llama3.2). No cloud API, no data leaves your machine.

## Features

- **100% local**: embeddings and LLM both run on your computer
- **Grounded answers**: each reply ends with a `(sources: ...)` line showing which files were used
- **PDF support**: convert PDFs to text with one command
- **Dockerized**: run the chat in a container from PowerShell or Docker Desktop
- **Simple**: three scripts, no database server

## How it works

```
PDF/TXT files --> extract_pdf.py --> data/*.txt
                                        |
                                    ingest.py  (chunk + embed)
                                        |
                                  embeddings.npz
                                        |
Your question --> chat.py --> retrieve top chunks --> llama3.2 (Ollama) --> answer + sources
```

1. **Ingest**: documents are split into chunks and embedded with a sentence-transformer model.
2. **Index**: vectors are saved to `embeddings.npz`.
3. **Retrieve**: your question is embedded and matched against the stored chunks.
4. **Generate**: the best chunks are passed to llama3.2 as context to produce the answer.

## Tech stack

Python 3.11 · Ollama (llama3.2) · sentence-transformers / PyTorch · NumPy · Docker

## Project structure

| File | Purpose |
|---|---|
| `extract_pdf.py` | Converts a PDF to a `.txt` file in `data/` |
| `ingest.py` | Builds the index from `data/*.txt` |
| `chat.py` | Terminal chat: retrieves chunks and asks llama3.2 |
| `embeddings.npz` | Saved index (created by `ingest.py`) |
| `requirements.txt` | Pinned Python dependencies |
| `Dockerfile` | Container build |
| `HOW_TO_RUN.txt` | Detailed step-by-step guide |

## Quick start

**Requirements:** Windows PC with 8 GB RAM or more (16 GB recommended), Python 3.11, [Ollama](https://ollama.com).

```powershell
# 1. Clone
git clone https://github.com/a-gun8591/Local-RAG-based-Research-Assistant.git
cd Local-RAG-based-Research-Assistant

# 2. Get the model
ollama pull llama3.2

# 3. Set up Python
py -3.11 -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# 4. Add documents
#    Put PDFs in data\ then convert each one:
python extract_pdf.py "data\your_file.pdf"

# 5. Build the index
python ingest.py

# 6. Chat (Ollama must be running)
python chat.py
```

Type your question at the `You:` prompt. Type `exit` to quit.

## Run with Docker

Ollama keeps running on your computer; only the chat runs in the container.

**One-time setup**
1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) and wait for "Engine running".
2. Set the environment variable `OLLAMA_HOST` to `0.0.0.0`, then restart Ollama.

**Build**
```powershell
docker build -t local-rag .
```

**Option 1: PowerShell**
```powershell
docker run -it --rm local-rag
```

**Option 2: Docker Desktop**
```powershell
docker run -dit --name rag-chat local-rag tail -f /dev/null
```
Then open Docker Desktop > **Containers** > `rag-chat` > **Exec** tab and run:
```
python chat.py
```

The image includes `embeddings.npz` but not `data/`. To add documents, run `ingest.py` locally and rebuild the image.

## Troubleshooting

| Problem | Fix |
|---|---|
| `Could not reach Ollama` | Open Ollama so it runs in the system tray. For Docker, also set `OLLAMA_HOST=0.0.0.0` and restart it |
| `embeddings.npz not found` | Run `python ingest.py` |
| `No .txt files found in data/` | Convert PDFs with `extract_pdf.py` or add `.txt` files |
| Answers say "I don't know" | Use the exact terms from the document. Scanned (image-only) PDFs can't be searched |
| `pip install` fails | Recreate the venv with Python 3.11 |

More in [HOW_TO_RUN.txt](HOW_TO_RUN.txt).

## Limitations

- Scanned PDFs need OCR before use
- Answer quality depends on the local model and on how well the documents convert to text
- Terminal interface only

## Future improvements

- Web UI (Streamlit or Gradio)
- OCR support for scanned PDFs
- Persistent vector store (FAISS or Chroma)
- Docker Compose with Ollama as a service

## Author

[a-gun8591](https://github.com/a-gun8591)

## License

MIT (add a `LICENSE` file if you choose this).
