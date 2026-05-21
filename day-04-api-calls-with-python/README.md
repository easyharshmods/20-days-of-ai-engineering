# Day 04 - API Calls with Python

## What we are building

Today we are building a Python script that calls a public HTTP API and prints a structured summary.

The script calls the GitHub REST API for repository metadata, checks the HTTP status code, parses the JSON response, and prints fields that are useful to an engineer: repository name, description, stars, forks, open issues, and default branch.

## Why this matters for AI engineering

AI engineering work rarely happens in isolation. Real applications call APIs for documents, tickets, cloud inventory, logs, billing, identity, deployment metadata, and model runtimes.

Before calling local Ollama in Day 05, it helps to understand the normal HTTP pattern: send a request, check the status code, parse JSON, handle errors, and return a clean result.

The analogy for this lesson is a health check. An API response is only useful if we know whether the request succeeded and whether the response shape is what the program expects.

## Concepts covered

- HTTP GET requests
- Status codes
- JSON responses
- Request timeouts
- Error handling
- Separating API calls from formatting logic

## Folder structure

```text
day-04-api-calls-with-python/
  README.md
  requirements.txt
  code/
    main.py
```

## Prerequisites

- Python 3.14.5
- Internet access for `python code/main.py`
- Basic Python functions and dictionaries from earlier days

This lesson does not call an LLM. Later lessons use:

```bash
ollama pull llama3.2:3b
```

Optional more capable alternative model for later LLM lessons:

```bash
ollama pull gemma4:latest
```

## Setup

Run these commands from the repository root:

```bash
cd day-04-api-calls-with-python
python -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Code walkthrough

`code/main.py` uses `requests` to call:

```text
https://api.github.com/repos/ollama/ollama
```

The code is split into small functions:

- `fetch_repository()` performs the HTTP GET request.
- `build_repository_summary()` selects the fields we care about.
- `format_summary()` turns the summary dictionary into readable output.
- `main()` connects the API call and printing.

## Run the project

From inside `day-04-api-calls-with-python`, with the virtual environment activated:

```bash
python code/main.py
```

When you are done recording or testing this lesson:

```bash
deactivate
```

## Expected output

The live numbers can change, but the output should look like this:

```text
GitHub Repository Summary
Repository: ollama/ollama
Description: Run local models with Ollama.
Stars: 100000+
Forks: 8000+
Open issues: 1000+
Default branch: main
```

## Common issues and fixes

**`ModuleNotFoundError: No module named 'requests'`**

Install the lesson dependencies from inside the lesson folder:

```bash
pip install -r requirements.txt
```

**Network request times out**

Check your internet connection and try again. The script uses a timeout so it does not hang forever.

**GitHub API rate limit**

Unauthenticated GitHub API calls are rate-limited. Wait and try again later, or change the script to call another public JSON API.

## What would change in production

In production, you would usually add retries, structured logging, authentication, rate-limit handling, and stronger response validation.

You would also avoid printing sensitive API responses directly to logs. This lesson uses public repository metadata, so there are no secrets involved.

## Key takeaways

- APIs should be called with timeouts.
- Always check status codes before trusting a response.
- JSON API responses become Python dictionaries.
- Keep network calls separate from formatting logic.

## Next step

In Day 05, we will use the same HTTP and JSON ideas to call a local LLM through Ollama.
