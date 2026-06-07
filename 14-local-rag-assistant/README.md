# Build a Local RAG Assistant with Streamlit

## What we are building

Build a complete local RAG app.

## Why this matters for AI engineering

This is a focused module in **AI Engineering for DevOps Engineers**. It teaches one concept first, then discusses production trade-offs after the code runs.

## Concepts covered

- RAG UI
- retrieval
- source display

## Folder structure

```text
14-local-rag-assistant/
  README.md
  requirements.txt
  code/app.py
```

## Prerequisites

- Python 3.13.13
- Ollama running

```bash
ollama pull llama3.2:3b
ollama pull llama3.2:1b        # lower-RAM fallback
ollama pull nomic-embed-text
```

## Setup

```bash
cd 14-local-rag-assistant
uv venv .venv --python 3.13.13
source .venv/bin/activate              # Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

When done:

```bash
deactivate
```

## Code walkthrough

Start with the simplest working version. Keep production hardening in the explanation rather than hiding the core idea behind abstractions.

## Run the project

```bash
streamlit run code/app.py
```

## Expected output

A Streamlit app answers with retrieved chunks.

## Common issues and fixes

- Run commands from the module root.
- Activate `.venv` before running code.
- Install packages with `uv pip install -r requirements.txt`.
- If Ollama is used, confirm `ollama list` shows the required model.

## What would change in production

Add validation, logging, observability, auth, rate limits, CI/CD, and security controls only after the simple version is understood.

## Key takeaways

- Make it work first.
- Explain the result.
- Discuss production improvements last.

## Next step

Continue to the next module.
