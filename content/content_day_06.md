# Day 06 Content Package

## video_title

Modular Python Project for a Local LLM - Day 06

## thumbnail_text

Modular LLM Client

## description

In Day 06 of 20 Days of AI Engineering, we turn the first local Ollama script into a modular Python project.

We split configuration, prompt construction, the Ollama client, and the command-line entry point into separate files. The result is a reusable local LLM client that can support the Streamlit and API lessons coming next.

The pinned model remains `llama3.2:3b`, with `gemma2:2b` as the low-RAM fallback for local testing.

GitHub repo: coming soon

## chapters

- 00:00 Hook
- 00:00 Why one-file scripts get hard to maintain
- 00:00 Project structure
- 00:00 Config module
- 00:00 Prompt module
- 00:00 LLM client module
- 00:00 Main entry point
- 00:00 Production thinking
- 00:00 Recap

## youtube_script

# Modular Python Project for a Local LLM

## Hook

A one-file script is useful when you are learning. But once you add prompts, model calls, UI code, and tests, that same file becomes harder to reason about.

Today we split the local LLM script into clear modules.

## Intro

Welcome to Day 06 of 20 Days of AI Engineering.

In Day 05, we called Ollama from a single Python file. Today we keep the behavior similar but improve the structure.

The goal is a reusable local LLM client.

## Concept Explanation

Modular Python is about responsibility.

Configuration belongs in one place. Prompt construction belongs in another. HTTP client logic should not be mixed with command-line printing.

This is similar to how infrastructure engineers split modules, variables, and environment-specific configuration.

The point is not to create a large framework. The point is to make the next change easier.

## Hands-on Build

Open the Day 06 folder.

`config.py` contains the Ollama endpoint, the pinned model `llama3.2:3b`, and the request timeout.

`prompts.py` builds an engineering explainer prompt. This lets us change prompt style without touching the HTTP client.

`llm_client.py` builds the Ollama payload and sends the local request.

`main.py` chooses the topic, builds the prompt, calls the client, and prints the answer.

Run the app with `python code/main.py`.

## Production Thinking

In production, this client would need more operational detail.

You would add structured logs, metrics, retries, request IDs, input limits, response validation, and clear failure behavior.

But the module boundaries would stay similar: config, prompt construction, client logic, and application entry point.

## Recap

Today we moved from a one-file local LLM script to a small modular Python project.

This gives us a cleaner foundation for Streamlit, chat memory, document workflows, and APIs.

## CTA

The full code is in the GitHub repository for 20 Days of AI Engineering. Run Day 06 locally and try changing the topic in `main.py`.

## pinned_comment

## linkedin_post

Day 06 of my 20 Days of AI Engineering series is about modular Python.

I took the local Ollama script from Day 05 and split it into config, prompts, an LLM client, and a main entry point.

This is where small AI scripts start becoming maintainable applications.

## learning_objectives

- Split a Python script into focused modules.
- Keep config separate from application logic.
- Build prompt text outside the LLM client.
- Create a reusable local Ollama client.
- Test module behavior without calling the model.

## common_mistakes

- Putting all logic in `main.py`.
- Mixing prompt templates into HTTP request code.
- Importing modules from the wrong working directory.
- Creating abstractions before there is a real reason.
- Forgetting to keep the pinned model consistent.

## expected_output

```text
Local LLM engineering explainer
Model: llama3.2:3b
Topic: why timeouts matter in API clients

<model response>
```

