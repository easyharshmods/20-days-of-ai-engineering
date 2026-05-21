# Day 13 - Introduction to RAG

## What we are building

Today we are building a simple retrieval-based assistant without embeddings or a vector database.

The script searches small document snippets with keyword scoring, selects the best context, and sends that context to `llama3.2:3b`.

## Why this matters for AI engineering

RAG means retrieval augmented generation. Instead of putting everything into the prompt, retrieve the most relevant context first, then ask the model to answer using that context.

## Concepts covered

- RAG
- Retrieval
- Generation
- Context windows
- Document search
- Naive keyword scoring

## Folder structure

```text
day-13-introduction-to-rag/
  README.md
  requirements.txt
  sample/knowledge_base.json
  code/main.py
  code/retrieval.py
  code/llm_client.py
```

## Prerequisites

```bash
ollama pull llama3.2:3b
ollama pull gemma4:latest
```

## Setup

```bash
cd day-13-introduction-to-rag
python -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Code walkthrough

`retrieval.py` scores documents by shared query words. `main.py` loads the sample knowledge base, retrieves context, builds a prompt, and calls Ollama.

## Run the project

```bash
python code/main.py
```

When you are done recording or testing this lesson:

```bash
deactivate
```

## Expected output

The script keyword-scores `sample/knowledge_base.json` against the query *"How should we roll back a bad deployment?"*, sends the top documents to `llama3.2:3b`, and prints an answer like:

```text
Pause new deployments, identify the last stable version, and redeploy it. Watch error rate and latency for ten minutes. If recovery does not happen, escalate to platform on-call.
```

Wording varies between runs. The answer should stay grounded in the retrieved snippets.

## Common issues and fixes

Keyword retrieval is limited. If wording differs too much, it may miss relevant documents.

## What would change in production

Production RAG needs chunking, embeddings, vector search, source tracking, evaluation, access control, and logging.

## Key takeaways

- RAG separates retrieval from generation.
- Retrieval chooses context before the model answers.
- Naive retrieval is useful for learning but limited.
- Better retrieval comes in later lessons.

## Next step

In Day 14, we build a text chunking utility.
