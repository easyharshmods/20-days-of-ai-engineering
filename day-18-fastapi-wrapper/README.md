# Day 18 - FastAPI Wrapper

## What we are building

Today we are wrapping a local AI assistant behind a FastAPI endpoint.

The API accepts a question, builds a practical engineering prompt, calls Ollama with `llama3.2:3b`, and returns a structured JSON response.

## Why this matters for AI engineering

Production AI applications often need an API boundary. A UI, job runner, internal tool, or workflow engine should call a service endpoint instead of importing Streamlit code.

## Concepts covered

- FastAPI
- POST endpoint
- Request models
- Response models
- API testing
- Local model wrapper

## Folder structure

```text
day-18-fastapi-wrapper/
  README.md
  requirements.txt
  code/api.py
  code/assistant.py
```

## Prerequisites

```bash
ollama pull llama3.2:3b
ollama pull gemma4:latest
```

## Setup

```bash
cd day-18-fastapi-wrapper
python -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Code walkthrough

`assistant.py` builds prompts and calls Ollama. `api.py` defines request and response models plus a `/ask` endpoint.

## Run the project

```bash
uvicorn code.api:app --reload
```

When you are done recording or testing this lesson:

```bash
deactivate
```

## Expected output

`uvicorn` starts and logs:

```text
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Application startup complete.
```

In another terminal:

```bash
curl http://127.0.0.1:8000/health
# {"status":"ok","model":"llama3.2:3b"}

curl -X POST http://127.0.0.1:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "Why do retries need backoff?"}'
```

returns JSON like:

```json
{
  "model": "llama3.2:3b",
  "question": "Why do retries need backoff?",
  "answer": "Backoff spreads retry attempts so downstream services do not get overwhelmed..."
}
```

Interactive docs are available at `http://127.0.0.1:8000/docs`.

## Common issues and fixes

If `uvicorn` cannot import `code.api`, run from the lesson root. If Ollama fails, start it and pull `llama3.2:3b`.

## What would change in production

Production APIs need authentication, rate limits, request IDs, structured logs, metrics, timeouts, and input size limits.

## Key takeaways

- FastAPI gives the assistant a service boundary.
- Request and response models document the contract.
- API code should not depend on Streamlit.
- Model failures should return clear API errors.

## Next step

In Day 19, we Dockerize this AI API.
