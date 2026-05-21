# Day 05 Content Package

## video_title

Local LLM with Ollama - Day 05

## thumbnail_text

Run an LLM Locally

## description

In Day 05 of 20 Days of AI Engineering, we make the first local LLM call with Ollama.

We use Python to send a prompt to Ollama's local API, call the pinned `llama3.2:3b` model, and print the response. The lesson also explains the low-RAM fallback model `gemma2:2b` for laptops with less memory.

This is the bridge from normal HTTP API calls to local AI application development.

GitHub repo: coming soon

## chapters

- 00:00 Hook
- 00:00 What we are building
- 00:00 Ollama as a local service
- 00:00 Pull the model
- 00:00 Build the request payload
- 00:00 Send the local LLM call
- 00:00 Handle errors
- 00:00 Production thinking
- 00:00 Recap

## youtube_script

# Local LLM with Ollama

## Hook

If you are a DevOps engineer, think of Ollama as a local service running on your laptop.

Our Python script is just a client. It sends a request to `localhost`, waits for a response, and prints the result.

## Intro

Welcome to Day 05 of 20 Days of AI Engineering.

In Day 04, we called a public HTTP API. Today we use the same basic idea to call a local LLM through Ollama.

The pinned model for this series is `llama3.2:3b`.

## Concept Explanation

An LLM call is still an API call.

We send a structured request. The request includes the model name, the prompt, and whether we want streaming.

For this first lesson, we set streaming to false. That means Ollama returns one JSON response instead of sending tokens gradually.

This keeps the code small and makes the response easier to inspect.

## Hands-on Build

First, make sure Ollama is installed and running.

Pull the default model with `ollama pull llama3.2:3b`.

If your laptop has less than 8 GB RAM, also pull `gemma2:2b` as a fallback for local testing.

Now open `code/main.py`.

The `build_ollama_payload` function creates the request body. It includes the model, prompt, and `stream: false`.

The `ask_ollama` function sends a POST request to `http://localhost:11434/api/generate`.

If the request fails or Ollama returns a non-200 status code, the code raises a clear local LLM error.

The prompt asks the model to explain virtual environments to a DevOps engineer in three practical bullets.

Run the script with `python code/main.py`.

## Production Thinking

Local-only development is useful because prompts stay on your machine and setup is simple.

Production is different. You need clear decisions about where the model runs, who can call it, what gets logged, how long requests can run, and what happens when the model is unavailable.

Even in this small script, we start with timeouts and error handling.

## Recap

Today we made the first local LLM call in the series.

We used Ollama, the pinned `llama3.2:3b` model, a JSON payload, and a local HTTP endpoint.

This prepares us to build a reusable LLM client in Day 06.

## CTA

The full code is in the GitHub repository for 20 Days of AI Engineering. Run Day 05 locally, then change the prompt and observe how the model response changes.

## pinned_comment

Day 05 uses Ollama locally with the pinned model `llama3.2:3b`. Pull it with `ollama pull llama3.2:3b`. Low-RAM fallback for local testing: `ollama pull gemma2:2b`.

## linkedin_post

Day 05 of my 20 Days of AI Engineering series is the first local LLM call.

The lesson treats Ollama like a local service dependency: Python sends a request to `localhost`, passes a prompt to `llama3.2:3b`, and prints the response.

The important idea is that an LLM call is still an API call. It needs structured input, timeouts, error handling, and clear boundaries.

## learning_objectives

- Pull and use the pinned local model `llama3.2:3b`.
- Understand Ollama as a local HTTP service.
- Build a JSON payload for a local LLM call.
- Send a POST request to Ollama.
- Test payload formatting without requiring a live model.

## common_mistakes

- Forgetting to start Ollama.
- Forgetting to pull `llama3.2:3b`.
- Running the script before installing `requests`.
- Assuming local model calls do not need timeouts.
- Sending sensitive data into prompts without thinking about logging and storage.

## expected_output

```text
Local LLM response
Model: llama3.2:3b

- A virtual environment isolates Python packages for one project.
- It prevents dependency conflicts between tools and applications.
- It makes local development closer to a repeatable build environment.
```

