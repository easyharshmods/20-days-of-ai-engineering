# Day 18 Content Package

## video_title

FastAPI Wrapper for a Local AI Assistant - Day 18

## thumbnail_text

AI Assistant as an API

## description

In Day 18 of 20 Days of AI Engineering, we put a real boundary around the local AI assistant by wrapping it in a FastAPI service.

The API exposes a `/health` endpoint and a `POST /ask` endpoint. A typed `AskRequest` validates the incoming question with a length range, and a typed `AskResponse` returns the model name, the question, and the answer. Under the hood, the assistant module builds an engineering-focused prompt and calls Ollama with `llama3.2:3b`, raising an `AssistantError` on failure that the API translates into a clean HTTP 503.

Everything in this series until today has been a script or a Streamlit app. From this point on we treat the assistant as a service that any UI, job, or workflow engine can call. That is the shape every production AI app eventually needs.

GitHub repo: coming soon

## chapters

- 00:00 Hook
- 00:00 Why an AI app needs a service boundary
- 00:00 The FastAPI app shape
- 00:00 AskRequest and AskResponse models
- 00:00 The /health endpoint
- 00:00 The POST /ask endpoint
- 00:00 AssistantError and HTTP 503
- 00:00 Running uvicorn locally
- 00:00 Testing with curl and the interactive docs
- 00:00 Production thinking
- 00:00 Recap

## youtube_script

# FastAPI Wrapper for a Local AI Assistant

## Hook

Streamlit was great for getting the assistant in front of someone fast.

The moment a second tool wants to call the assistant, the UI is in the way.

## Intro

Welcome to Day 18 of 20 Days of AI Engineering.

We are going to take the assistant pattern we have been using and move the LLM call behind a real API. A FastAPI app with typed request and response models, a health check, a question endpoint, and clean error handling.

The model stays exactly the same. `llama3.2:3b` running on local Ollama. The change is the contract around it.

## Concept Explanation

A service boundary is the line between "the model logic" and "the caller". An API contract draws that line explicitly.

FastAPI is a good fit for this lesson because the contract lives in code that is easy to read. You declare what the request looks like with a Pydantic model, you declare what the response looks like with another, and the framework handles validation, documentation, and error shaping for you.

Once the contract exists, the caller does not need to know whether the assistant runs locally, in a container, or behind an internal platform. The caller sends a question and gets back a typed answer. That is what makes the rest of this series (Docker on Day 19, AWS on Day 20) feel small instead of dramatic.

## Hands-on Build

Open `code/assistant.py`. This is the model-side module. `DEFAULT_MODEL` is `llama3.2:3b`. `build_prompt` puts the model in a practical engineering-assistant role, asks for clear answers with trade-offs, and includes the user question. `answer_question` posts to Ollama's `/api/generate` endpoint, wraps the request in `try`/`except requests.RequestException`, raises `AssistantError` on a connection failure, and also raises `AssistantError` if Ollama returns a non-200 status. The point is that any failure mode the API needs to react to becomes one exception type.

Open `code/api.py`. The FastAPI app is named after the assistant. `AskRequest` has a `question` field constrained to between three and one thousand characters, so the framework rejects empty or absurdly large inputs before we ever call the model. `AskResponse` returns the model name, the echoed question, and the answer, so the caller has everything needed to log the interaction.

The `/health` endpoint returns the status and the model name. Useful for orchestrators, useful for humans.

`POST /ask` calls `answer_question`. If `AssistantError` is raised, we translate it into a `HTTPException` with status 503 and the original message. Anything else is an unexpected bug and bubbles up as a 500, which is the behavior you want for genuine surprises.

Run the project with `uvicorn code.api:app --reload` from the lesson root. The lesson uses a `code/__init__.py` so `code` is importable as a package.

Hit `http://127.0.0.1:8000/docs` to see the FastAPI interactive docs. Try the `/health` endpoint and a `POST /ask` from there, or from curl.

## Production Thinking

A FastAPI app is a starting point. A production AI API has work on top.

Authentication and rate limits. There is no version of "we accept LLM requests from anyone, with no caps" that ends well. Even an internal API needs identity and per-tenant limits.

Observability. Request IDs, structured logs, latency metrics, model name and version on every response, and a way to correlate a request to the upstream caller and the model output.

Input limits and timeouts. We already restrict the question length. Real systems also bound output length, bound how long a request can run, and decline requests that are clearly oversized.

Failure shape. Today, model failures return HTTP 503 with a short message. In production you want a distinct error code per failure mode, and you want to drop sensitive provider error text before it leaves the service.

## Recap

Today we put a real service boundary around the local assistant.

We declared the contract with typed Pydantic models, added a health endpoint, mapped assistant failures to clean HTTP responses, and ran the whole thing under uvicorn.

The assistant is now a service that any other tool can call.

## CTA

The full code is in the GitHub repository for 20 Days of AI Engineering. Run Day 18 locally, hit `/docs`, and call `/ask` from curl. Then think about which of your existing internal tools could use a `/ask`-shaped endpoint.

## pinned_comment

Day 18 wraps the local assistant in FastAPI with a typed `AskRequest`, typed `AskResponse`, `/health`, and `POST /ask`. Model stays `llama3.2:3b` on local Ollama. `AssistantError` translates into a clean HTTP 503 so callers see a real status code, not a traceback.

## linkedin_post

Day 18 of my 20 Days of AI Engineering series is about service boundaries.

I wrapped the local Ollama assistant in a FastAPI app with typed request and response models, a `/health` endpoint, and a `POST /ask` endpoint that maps assistant failures to a clean HTTP 503.

The model did not change. The contract did. That contract is what makes Docker and AWS feel small in the next two lessons, instead of dramatic.

## learning_objectives

- Wrap a local model call behind a FastAPI service boundary.
- Define typed request and response models with Pydantic.
- Add a `/health` endpoint that reports the model name.
- Map a domain-level `AssistantError` to a clean HTTP 503.
- Test the API with curl and the FastAPI interactive docs.

## common_mistakes

- Exposing an AI endpoint with no authentication, no rate limits, and no input bounds.
- Mixing Streamlit UI code with service code so the API cannot stand on its own.
- Returning raw provider error text to clients.
- Returning HTTP 200 with an error in the body instead of a real status code.
- Forgetting `code/__init__.py`, so `uvicorn code.api:app` fails to import.

## expected_output

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

The interactive docs are at `http://127.0.0.1:8000/docs`. If Ollama is not running or `llama3.2:3b` is not pulled, `POST /ask` responds with HTTP 503 and a clear message instead of crashing the server.
