# Day 17 - Local RAG Assistant

## What we are building

Today we are building a complete local RAG assistant over an uploaded text file.

The app chunks the document, embeds chunks with `nomic-embed-text`, retrieves the most relevant chunks, and asks `llama3.2:3b` to answer with source-aware context.

## Why this matters for AI engineering

This is the core local AI engineering workflow: prepare documents, retrieve relevant context, and generate an answer grounded in that context.

## Concepts covered

- Chunking
- Embeddings
- Retrieval
- Answer generation
- Source-aware answers
- Local RAG trade-offs

## Folder structure

```text
day-17-local-rag-assistant/
  README.md
  requirements.txt
  sample/platform_notes.txt
  code/app.py
  code/rag_logic.py
  code/llm_client.py
```

## Prerequisites

```bash
ollama pull llama3.2:3b
ollama pull nomic-embed-text
ollama pull gemma4:latest
```

## Setup

```bash
cd day-17-local-rag-assistant
python -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Code walkthrough

`rag_logic.py` chunks text, builds RAG prompts, and ranks vectors. `llm_client.py` calls both Ollama embedding and generation APIs. `app.py` wires the workflow into Streamlit.

## Run the project

```bash
streamlit run code/app.py
```

When you are done recording or testing this lesson:

```bash
deactivate
```

## Expected output

A local Streamlit app at `http://localhost:8501` with:

- a file uploader for a UTF-8 `.txt` file
- a question input
- a **Run local RAG** button

Upload `sample/platform_notes.txt`, ask *"Why do retries need backoff?"*, and after a brief spinner the app shows:

- an **Answer** section with a grounded explanation
- a **Retrieved chunks** section listing the chunks used (id + similarity score + text preview)

## Common issues and fixes

If embedding fails, pull `nomic-embed-text`. If generation fails, pull `llama3.2:3b`.

## What would change in production

Production RAG needs durable indexing, source permissions, metadata filters, evaluation, observability, and careful handling of sensitive uploaded files.

## Key takeaways

- RAG is a pipeline, not one model call.
- Embeddings are used for retrieval, not generation.
- Source metadata matters.
- Local RAG is useful for learning before cloud architecture.

## Next step

In Day 18, we expose the assistant behind a FastAPI endpoint.
