# Dockerize Your Local AI API

## What we are building

Package the AI API in Docker.

## Why this matters for AI engineering

This is a focused module in **AI Engineering for DevOps Engineers**. It teaches one concept first, then discusses production trade-offs after the code runs.

## Concepts covered

- Dockerfile
- host networking
- ports

## Folder structure

```text
16-dockerize-ai-api/
  README.md
  requirements.txt
  Dockerfile
  .env.example
  code/main.py
```

## Prerequisites

- Python 3.13.13
- Ollama running

```bash
ollama pull llama3.2:3b
ollama pull llama3.2:1b        # lower-RAM fallback
```

## Setup

```bash
cd 16-dockerize-ai-api
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
docker build -t local-ai-api .
docker run --add-host=host.docker.internal:host-gateway -p 8000:8000 -e OLLAMA_BASE_URL=http://host.docker.internal:11434 local-ai-api
```

## Expected output

The API runs in Docker on port 8000.

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
