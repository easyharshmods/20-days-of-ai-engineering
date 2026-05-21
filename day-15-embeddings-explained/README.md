# Day 15 - Embeddings Explained

## What we are building

Today we are building a local embedding similarity script.

The script calls Ollama's embedding API with `nomic-embed-text`, compares text vectors with cosine similarity, and ranks which engineering notes are most similar to a query.

## Why this matters for AI engineering

Embeddings turn text into numeric vectors. Similar meaning should land near similar meaning in vector space. This is the foundation for semantic search and RAG.

## Concepts covered

- Embeddings
- Semantic similarity
- Vectors
- Cosine similarity
- Ollama embedding API

## Folder structure

```text
day-15-embeddings-explained/
  README.md
  requirements.txt
  code/main.py
  code/embeddings.py
```

## Prerequisites

```bash
ollama pull llama3.2:3b
ollama pull nomic-embed-text
ollama pull gemma4:latest
```

`nomic-embed-text` is the embedding model for this series.

## Setup

```bash
cd day-15-embeddings-explained
python -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Code walkthrough

`embeddings.py` calls Ollama for embeddings and calculates cosine similarity. `main.py` embeds a query and sample notes, then ranks them.

## Run the project

```bash
python code/main.py
```

When you are done recording or testing this lesson:

```bash
deactivate
```

## Expected output

The script embeds the query *"How do we avoid retry storms?"* and three engineering notes, then prints the notes ranked by cosine similarity. The retry-related note should come out on top:

```text
Query: How do we avoid retry storms?
0.812 | Retries should use exponential backoff during downstream failures.
0.523 | Rollback procedures should identify the previous stable deployment.
0.487 | Cloud cost reviews should inspect idle compute and storage lifecycle rules.
```

Exact scores depend on the embedding model. Relative ranking should hold.

## Common issues and fixes

If Ollama says the model is missing, run `ollama pull nomic-embed-text`.

## What would change in production

Production systems store embeddings, version embedding models, track source metadata, and rebuild indexes when chunking or embedding models change.

## Key takeaways

- Embeddings are vectors for text meaning.
- Cosine similarity compares vector direction.
- Embeddings enable semantic retrieval.
- Use `nomic-embed-text` through Ollama in this series.

## Next step

In Day 16, we store vectors and perform top-k search.
