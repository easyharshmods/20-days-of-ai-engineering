# Day 06 - Modular Python Project

## What we are building

Today we are turning the Day 05 local LLM script into a small modular Python project.

Instead of keeping configuration, prompt text, HTTP logic, and command-line output in one file, we split the project into focused modules. The result is a reusable local Ollama client that can be imported by later scripts and apps.

## Why this matters for AI engineering

AI applications grow quickly. A one-file script is fine for the first model call, but it becomes hard to maintain once you add prompt templates, file uploads, chat history, retrieval, API endpoints, or UI code.

For DevOps and platform engineers, this is similar to splitting infrastructure code into modules. The goal is not abstraction for its own sake. The goal is to give each file a clear responsibility.

## Concepts covered

- `main.py` as the entry point
- Python modules
- Imports between local files
- Separation of concerns
- Reusable local LLM client
- Prompt construction

## Folder structure

```text
day-06-modular-python-project/
  README.md
  requirements.txt
  code/
    config.py
    llm_client.py
    main.py
    prompts.py
```

## Prerequisites

- Python 3.14.5
- Ollama installed and running for the main script
- The pinned default model:

```bash
ollama pull llama3.2:3b
```

Optional more capable alternative model (heavier, needs more RAM):

```bash
ollama pull gemma4:latest
```

The lesson code uses `llama3.2:3b` by default.

## Setup

Run these commands from the repository root:

```bash
cd day-06-modular-python-project
python -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Code walkthrough

The project is split by responsibility:

- `config.py` stores constants like the model name and Ollama endpoint.
- `prompts.py` builds a clear engineering prompt.
- `llm_client.py` contains the reusable Ollama HTTP client.
- `main.py` is the command-line entry point.

The important design choice is that `main.py` does very little. It chooses the topic, builds the prompt, calls the client, and prints the response.

## Run the project

Make sure Ollama is running, then run this from inside `day-06-modular-python-project`:

```bash
python code/main.py
```

When you are done recording or testing this lesson:

```bash
deactivate
```

## Expected output

The exact model response will vary, but it should explain the selected engineering topic:

```text
Local LLM engineering explainer
Model: llama3.2:3b
Topic: why timeouts matter in API clients

<model response>
```

## Common issues and fixes

**`ModuleNotFoundError` for a local module**

Run the command from the lesson root:

```bash
cd day-06-modular-python-project
python code/main.py
```

**Ollama connection fails**

Start Ollama and confirm the model is pulled:

```bash
ollama pull llama3.2:3b
```

**Want to try a more capable alternative model**

Pull the alternative (heavier than the default, ~9.6 GB):

```bash
ollama pull gemma4:latest
```

Then edit the model constant in `code/config.py` to point at it.

## What would change in production

In production, this client would likely include structured logging, retries, telemetry, request IDs, input limits, and stricter response validation.

You might also package the code as an installable module or service. For this lesson, plain files keep the module boundaries easy to see.

## Key takeaways

- Small modules make AI code easier to extend.
- `main.py` should stay focused on orchestration.
- Prompt construction belongs outside the HTTP client.
- A reusable LLM client prepares us for UI and API layers.

## Next step

In Day 07, we will build a simple Streamlit web UI on top of a local LLM call.
