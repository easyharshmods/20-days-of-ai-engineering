# Day 19 - Dockerize the AI App

## What we are building

Today we are Dockerizing a FastAPI wrapper around a local AI assistant.

The container runs the API service. Ollama still runs separately on the host or another runtime, which keeps the container focused on application code.

## Why this matters for AI engineering

Containers make AI services easier to run consistently across laptops, CI, and deployment environments.

## Concepts covered

- Dockerfile
- Requirements
- Ports
- Container runtime
- Local deployment
- External model runtime dependency

## Folder structure

```text
day-19-dockerize-the-ai-app/
  README.md
  requirements.txt
  Dockerfile
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
cd day-19-dockerize-the-ai-app
python -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Code walkthrough

The Dockerfile installs dependencies and starts `uvicorn`. `assistant.py` reads the Ollama host from `OLLAMA_BASE_URL` so the container can call an external Ollama runtime.

## Run the project

```bash
docker build -t local-ai-api .
docker run -p 8000:8000 -e OLLAMA_BASE_URL=http://host.docker.internal:11434 local-ai-api
```

When you are done recording or testing this lesson:

```bash
deactivate
```

## Expected output

`docker build` produces an image named `local-ai-api`. `docker run` starts uvicorn inside the container and logs:

```text
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Application startup complete.
```

With Ollama running on the host:

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
  "answer": "Backoff prevents retry storms by spacing out attempts..."
}
```

## Common issues and fixes

On Linux, `host.docker.internal` may need Docker host configuration. Keep Ollama running outside the app container for this lesson.

## What would change in production

Production images need vulnerability scanning, non-root users, resource limits, health checks, logs, secrets management, and deployment automation.

## Key takeaways

- Containerize the app, not necessarily the model runtime.
- Environment variables configure runtime endpoints.
- Ports and health checks matter.
- Docker is a packaging step, not the whole production architecture.

## Next step

In Day 20, we map the local app to AWS architecture.
