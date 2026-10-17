# RAG Knowledge Engine 📚

AI is great, but it often makes things up (hallucinations). I built this "Knowledge Engine" to make AI more reliable by grounding it in real documents.

### How it works:
You can upload PDFs or text files, and the system "reads" them. When you ask a question, the AI searches your documents first to find the exact answer, rather than guessing.

### The Tech:
- **LLM:** OpenAI GPT-4o.
- **Framework:** LangChain for the AI logic.
- **Storage:** ChromaDB (Vector Store) to keep track of document text.

This is a great tool for anyone who needs to search through large documents quickly and accurately.
