# Day 14 - Text Chunking

## What we are building

Today we are building a text chunking utility for documents.

The script splits text into overlapping chunks with metadata so later retrieval can search smaller, useful pieces instead of whole documents.

## Why this matters for AI engineering

Chunking affects retrieval quality. Chunks that are too small lose context. Chunks that are too large waste prompt space and can bury relevant details.

## Concepts covered

- Chunk size
- Overlap
- Metadata
- Retrieval quality
- Document preprocessing

## Folder structure

```text
day-14-text-chunking/
  README.md
  requirements.txt
  sample/runbook.txt
  code/main.py
  code/chunking.py
```

## Prerequisites

This lesson does not call an LLM, but later lessons use:

```bash
ollama pull llama3.2:3b
ollama pull gemma4:latest
```

## Setup

```bash
cd day-14-text-chunking
python -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Code walkthrough

`chunking.py` splits text by words, keeps overlap between neighboring chunks, and attaches metadata such as chunk index and source.

## Run the project

```bash
python code/main.py
```

When you are done recording or testing this lesson:

```bash
deactivate
```

## Expected output

`sample/runbook.txt` is roughly 71 words. With `chunk_size_words=35` and `overlap_words=7`, the script prints three chunks:

```text
runbook:0 | words=35 | Rollback runbook for checkout-api. First confirm the active deployment version and the last stable v
runbook:1 | words=35 | active. Deploy the previous stable artifact. Watch error rate, latency, saturation, and database co
runbook:2 | words=15 | escalate to the platform on-call and database on-call. After recovery, ...
```

Exact preview text depends on the sample. Chunk count and overlap behavior are the things to verify.

## Common issues and fixes

If chunks repeat too much, reduce overlap. If chunks lose meaning, increase chunk size.

## What would change in production

Production chunking may split by headings, paragraphs, token count, tables, or document structure. It should preserve source metadata for citations.

## Key takeaways

- Chunking is a retrieval design decision.
- Overlap preserves context across boundaries.
- Metadata is required for source-aware answers.
- There is no universal chunk size.

## Next step

In Day 15, we generate local embeddings with `nomic-embed-text`.
