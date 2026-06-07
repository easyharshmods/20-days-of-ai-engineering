# Vector Search Explained from Scratch

## What we are building

Rank chunks by vector similarity.

## Why this matters for AI engineering

This is a focused module in **AI Engineering for DevOps Engineers**. It teaches one concept first, then discusses production trade-offs after the code runs.

## Concepts covered

- top-k
- cosine similarity
- ranking

## Folder structure

```text
12-vector-search/
  README.md
  requirements.txt
  code/main.py
```

## Prerequisites

- Python 3.13.13
- No Ollama required

## Setup

```bash
cd 12-vector-search
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
python code/main.py
```

## Expected output

The most similar records print first.

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
