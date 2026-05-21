# Day 05 - Local LLM with Ollama

## What we are building

Today we are building the first local LLM script in the series.

The script sends a prompt to Ollama running on your laptop, asks `llama3.2:3b` to explain a cloud engineering concept, and prints the response.

This is still a small command-line program. The goal is to understand the request and response shape before we add modules, web UIs, chat memory, files, and RAG.

## Why this matters for AI engineering

An LLM call is an API call with model-specific inputs and outputs.

For cloud and DevOps engineers, Ollama is useful because it lets you practice model integration locally without creating cloud accounts, handling external credentials, or sending prompts outside your machine.

The analogy for this lesson is a local service dependency. Ollama is like a service listening on `localhost`; our Python script is the client.

## Concepts covered

- Ollama as a local LLM runtime
- The pinned model `llama3.2:3b`
- Optional more capable alternative model `gemma4:latest`
- HTTP POST requests
- JSON request bodies
- Localhost APIs
- Basic LLM error handling

## Folder structure

```text
day-05-local-llm-with-ollama/
  README.md
  requirements.txt
  code/
    main.py
```

## Prerequisites

- Python 3.14.5
- Ollama installed and running
- The default model pulled locally:

```bash
ollama pull llama3.2:3b
```

For an optional, more capable alternative model (heavier, ~9.6 GB, needs more RAM):

```bash
ollama pull gemma4:latest
```

The lesson code uses `llama3.2:3b` by default to keep the series consistent. If needed, you can edit the model constant in `code/main.py` to try the alternative locally.

## Setup

Run these commands from the repository root:

```bash
cd day-05-local-llm-with-ollama
python -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Code walkthrough

`code/main.py` calls Ollama's local HTTP API:

```text
http://localhost:11434/api/generate
```

The code is split into small pieces:

- `build_ollama_payload()` creates the JSON body for the model call.
- `ask_ollama()` sends the POST request and handles failures.
- `main()` defines a practical prompt and prints the model response.

The request sets `stream` to `false` so the response is returned as one JSON object. Streaming is useful later, but a single response is easier for the first LLM lesson.

## Run the project

Make sure Ollama is running, then run this from inside `day-05-local-llm-with-ollama`:

```bash
python code/main.py
```

When you are done recording or testing this lesson:

```bash
deactivate
```

## Expected output

The exact model response will vary, but it should answer this prompt:

```text
Explain virtual environments to a DevOps engineer in three practical bullets.
```

You should see output similar to:

```text
Local LLM response
Model: llama3.2:3b

- A virtual environment isolates Python packages for one project.
- It prevents dependency conflicts between tools and applications.
- It makes local development closer to a repeatable build environment.
```

## Common issues and fixes

**`Connection refused`**

Ollama is probably not running. Start Ollama and try again.

**Model not found**

Pull the pinned model:

```bash
ollama pull llama3.2:3b
```

**Want to try a more capable alternative model**

Pull the alternative (heavier than the default, ~9.6 GB):

```bash
ollama pull gemma4:latest
```

Then edit `DEFAULT_MODEL` in `code/main.py` to point at it.

**The response is slow**

Small local models still use CPU and memory. Close heavy applications and try again.

## What would change in production

In production, you would add timeouts, retries, request logging, model health checks, input limits, and monitoring.

You would also decide where the model runs, who can access it, how prompts are logged, and how sensitive data is handled. Local-only development keeps prompts on your machine, but production systems need explicit security boundaries.

## Key takeaways

- Ollama exposes a local HTTP API on `localhost`.
- `llama3.2:3b` is the pinned default model for this series.
- An LLM request is structured data, not magic.
- Local model calls still need error handling.
- Keep the first model call simple before adding UI or memory.

## Next step

In Day 06, we will split this script into a small modular Python project with a reusable local LLM client.
