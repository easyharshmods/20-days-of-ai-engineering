# Day 16 - Vector Search

## What we are building

Today we are building a simple local vector search demo using numpy.

The script stores text chunks with vectors, embeds a query with `nomic-embed-text`, and returns the top-k most similar chunks.

## Why this matters for AI engineering

Vector search is the retrieval layer behind many RAG systems. It lets a system find semantically relevant chunks before asking the model to answer.

## Concepts covered

- Vector search
- Similarity ranking
- Top-k retrieval
- Metadata
- Numpy-based local search

## Folder structure

```text
day-16-vector-search/
  README.md
  requirements.txt
  code/main.py
  code/vector_search.py
```

## Prerequisites

```bash
ollama pull llama3.2:3b
ollama pull nomic-embed-text
ollama pull gemma4:latest
```

## Setup

```bash
cd day-16-vector-search
python -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Code walkthrough

`vector_search.py` stores chunk text, metadata, and embeddings. It ranks chunks by cosine similarity and returns the top matches.

## Run the project

```bash
python code/main.py
```

When you are done recording or testing this lesson:

```bash
deactivate
```

## Expected output

The script embeds three runbook chunks and the query *"How do retries avoid overload?"*, then prints top-k matches with score and source metadata:

```text
0.798 | retry-runbook | Retries should use backoff and jitter.
0.412 | rollback-runbook | Rollback deploys the previous stable version.
0.355 | cost-runbook | Cost reviews inspect idle compute.
```

Exact scores depend on the embedding model. The retry chunk should rank first.

## Common issues and fixes

If embedding calls fail, start Ollama and pull `nomic-embed-text`.

## What would change in production

Production systems use durable vector indexes, metadata filters, access control, reindexing workflows, and evaluation.

## Key takeaways

- Vector search ranks chunks by similarity.
- Top-k controls how many chunks are sent to generation.
- Metadata is needed for source-aware answers.
- Numpy is enough to learn the idea locally.

## Next step

In Day 17, we combine chunking, embeddings, vector search, and generation into a local RAG assistant.
