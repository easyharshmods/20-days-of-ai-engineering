# Day 04 Content Package

## video_title

API Calls with Python - Day 04

## thumbnail_text

Call APIs with Python

## description

In Day 04 of 20 Days of AI Engineering, we call a public HTTP API with Python.

This lesson prepares us for Day 05, where we use the same HTTP and JSON pattern to call a local LLM through Ollama.

GitHub repo: coming soon

## chapters

- 00:00 Hook
- 00:00 What we are building
- 00:00 HTTP and JSON basics
- 00:00 Install requests
- 00:00 Make a GET request
- 00:00 Check status codes
- 00:00 Format the API response
- 00:00 Production thinking
- 00:00 Recap

## youtube_script

# API Calls with Python

## Hook

Most useful engineering tools are not isolated scripts. They call APIs.

Cloud inventory, ticketing systems, deployment platforms, observability tools, and model runtimes all tend to expose HTTP APIs.

## Intro

Welcome to Day 04 of 20 Days of AI Engineering.

Today we are building a small Python script that calls a public API and prints a structured summary.

We will use the GitHub REST API because it returns simple JSON and does not require credentials for this example.

## Concept Explanation

An HTTP API call has a few basic parts.

There is a URL. There is a method, like GET or POST. There is a response status code. And often there is a JSON response body.

For beginner AI engineering work, this matters because local LLMs, hosted model APIs, retrieval services, and internal platform tools all use similar request and response patterns.

Today we focus on GET, status codes, JSON parsing, timeouts, and error handling.

## Hands-on Build

Open the Day 04 folder and install dependencies with `pip install -r requirements.txt`.

The dependency for this lesson is `requests`.

In `code/main.py`, we define the GitHub API URL for the Ollama repository.

The `fetch_repository` function imports `requests`, sends a GET request, and uses a timeout.

If the request fails or GitHub returns a non-200 status code, we raise a small custom `ApiError`.

Then `build_repository_summary` extracts the fields we care about: repository name, description, stars, forks, open issues, and default branch.

Finally, `format_summary` turns that dictionary into lines that are easy to print.

Run the script with `python code/main.py`.

## Production Thinking

In production, API code needs more guardrails.

You would think about authentication, retries, rate limits, structured logging, request IDs, metrics, and response validation.

You would also be careful about logging response bodies because APIs often return sensitive data.

This lesson keeps the API public and simple so the HTTP pattern is clear.

## Recap

This prepares us for the next lesson, where we call Ollama locally.

## CTA

The full code is in the GitHub repository for 20 Days of AI Engineering. Run Day 04 locally, then try changing the GitHub repository URL to inspect another project.

## pinned_comment

## linkedin_post

Day 04 of my 20 Days of AI Engineering series is about API calls with Python.

The lesson uses `requests` to call the GitHub API, checks status codes, parses JSON, and prints a structured summary.

The important part is the pattern: request, validate, parse, format, and test the non-network logic offline. That same pattern shows up when calling model runtimes and internal platform APIs.

## learning_objectives

- Make an HTTP GET request with `requests`.
- Use timeouts for API calls.
- Check response status codes.
- Parse JSON responses into Python dictionaries.

## common_mistakes

- Forgetting to install `requests`.
- Trusting the response before checking the status code.
- Leaving API calls without timeouts.
- Printing sensitive API responses in production logs.

## expected_output

```text
GitHub Repository Summary
Repository: ollama/ollama
Description: Run local models with Ollama.
Stars: 100000+
Forks: 8000+
Open issues: 1000+
Default branch: main
```

