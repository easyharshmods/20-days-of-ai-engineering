# Day 19 Content Package

## video_title

Dockerize the AI App - Day 19

## thumbnail_text

Dockerize the AI API

## description

In Day 19 of 20 Days of AI Engineering, we package the FastAPI assistant from Day 18 into a Docker image and run it as a container.

The Dockerfile is intentionally small: start from `python:3.14-slim`, install pinned requirements, copy the `code/` package, expose port 8000, and launch `uvicorn`. The assistant reads `OLLAMA_BASE_URL` from the environment, defaulting to `http://localhost:11434` for local development. When running in Docker we pass `http://host.docker.internal:11434` so the container talks to Ollama on the host.

The deliberate choice in this lesson is that Ollama stays outside the container. We containerize the application, not the model runtime. That separation keeps the image small, keeps the model warm across container restarts, and matches how real systems separate the API tier from the model tier.

GitHub repo: coming soon

## chapters

- 00:00 Hook
- 00:00 What we are Dockerizing and what we are not
- 00:00 The Dockerfile, line by line
- 00:00 Reading OLLAMA_BASE_URL from the environment
- 00:00 Building the image
- 00:00 Running the container and host.docker.internal
- 00:00 Hitting /health and /ask
- 00:00 Production thinking
- 00:00 Recap

## youtube_script

# Dockerize the AI App

## Hook

The fastest way to make an app feel real is to put it in a container and watch it run the same way on a teammate's laptop.

We do that today, and we do it without breaking the model runtime.

## Intro

Welcome to Day 19 of 20 Days of AI Engineering.

Day 18 turned the assistant into a FastAPI service. Today we package that service into an image that runs anywhere Docker runs.

The shape we are building matches what most production AI services look like. The API runs in a container. The model runtime runs somewhere else, on a host, on a model server, or behind a managed service.

## Concept Explanation

Containerizing the FastAPI app is the easy part. Containerizing the model runtime is a different conversation: GPU support, model storage, restart behavior, warm-up time, and update cadence are all real concerns.

For this lesson we keep Ollama on the host and put only the application code in the image. The container talks to Ollama through `OLLAMA_BASE_URL`. On macOS and Windows that URL resolves to `http://host.docker.internal:11434`. On Linux you may need to add a host gateway or use the host network, but the pattern is the same.

There is a second reason for this split. Application images get rebuilt every time the code changes. Model runtimes get rebuilt much less often. Keeping them separate means a code change does not invalidate a multi-gigabyte model layer.

## Hands-on Build

Open the `Dockerfile`. It starts from `python:3.14-slim`, sets the working directory to `/app`, copies `requirements.txt`, runs `pip install --no-cache-dir -r requirements.txt`, copies the `code/` package into the image, exposes port 8000, and launches `uvicorn code.api:app --host 0.0.0.0 --port 8000`.

Two details matter. Copying `requirements.txt` and installing dependencies before copying the source code lets Docker cache the dependency layer separately from the application code. `--host 0.0.0.0` is what makes the API reachable from outside the container, instead of only from inside it.

Open `code/assistant.py`. The new piece since Day 18 is `OLLAMA_BASE_URL = getenv("OLLAMA_BASE_URL", "http://localhost:11434")`. The generate URL is built from that base, so the same code works on the host and inside a container.

Open `.env.example`. It documents the one variable a container operator needs to set: `OLLAMA_BASE_URL=http://host.docker.internal:11434`. The real `.env` is gitignored.

Build the image with `docker build -t local-ai-api .`.

Run the container with `docker run -p 8000:8000 -e OLLAMA_BASE_URL=http://host.docker.internal:11434 local-ai-api`. Hit `http://127.0.0.1:8000/health` and `POST /ask` exactly like Day 18.

## Production Thinking

A small Dockerfile is a starting point, not a finished image.

Scan images for vulnerabilities. Pin base image digests, not just tags. Update on a cadence you can actually keep up with.

Run as a non-root user. Containers run as root by default, which is fine for a demo and the wrong default for production.

Set CPU and memory limits. Without limits a single request that goes wrong can take the host down with it.

Health checks. A real production container has a `HEALTHCHECK` directive or an orchestrator-level liveness probe pointed at `/health`.

Secrets and configuration. `OLLAMA_BASE_URL` is fine as a plain environment variable. Anything sensitive, like API keys, belongs in a secrets manager that the orchestrator mounts at runtime, not in the image.

And logging. The default `uvicorn` log line is fine for a demo. A production setup wants structured logs, request IDs, and a way to ship them somewhere durable.

## Recap

Today we packaged the FastAPI assistant into a Docker image, with Ollama deliberately staying outside the container.

We used `OLLAMA_BASE_URL` to keep the same code working on the host and inside Docker. We documented the variable through `.env.example`. We kept the image small by separating dependency installation from code copy.

This is the last lesson before AWS.

## CTA

The full code is in the GitHub repository for 20 Days of AI Engineering. Build the Day 19 image, run it, and watch the same `/ask` call work both from the host and from inside the container. Then think about which production controls you would add before letting other tools call this image.

## pinned_comment

Day 19 packages the Day 18 FastAPI assistant in a `python:3.14-slim` image. Ollama stays on the host. The container reads `OLLAMA_BASE_URL` from the environment, defaulting to localhost so the same code runs everywhere. App image and model runtime are deliberately separate.

## linkedin_post

Day 19 of my 20 Days of AI Engineering series is the Docker step.

I packaged the FastAPI assistant from Day 18 into a small `python:3.14-slim` image. Ollama stayed on the host. The container talks to it through `OLLAMA_BASE_URL`, which defaults to localhost on the host and is pointed at `host.docker.internal` in the container.

App image and model runtime are deliberately separate. That is roughly how I would split them in a real internal AI service.

## learning_objectives

- Write a small Dockerfile for a Python FastAPI service.
- Use environment variables (`OLLAMA_BASE_URL`) to keep host and container behavior consistent.
- Build a Docker image and run it locally with port mapping.
- Reason about why the model runtime stays outside the application container.
- Document container configuration with a tracked `.env.example`.

## common_mistakes

- Bundling the model runtime into the application image.
- Forgetting `--host 0.0.0.0`, so the API is unreachable from outside the container.
- Hardcoding `localhost:11434` in code instead of reading it from the environment.
- Baking secrets into the image rather than passing them at runtime.
- Treating "it builds and runs" as production-ready.

## expected_output

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

If Ollama is not reachable at `OLLAMA_BASE_URL`, the API returns an error and `docker logs <container>` shows a clear connection failure instead of a silent hang.
