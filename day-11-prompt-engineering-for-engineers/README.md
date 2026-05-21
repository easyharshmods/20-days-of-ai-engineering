# Day 11 - Prompt Engineering for Engineers

## What we are building

Today we are building a prompt-driven local assistant with multiple engineering modes.

The script lets you choose a prompt mode such as AWS explainer, Terraform reviewer, or incident summarizer. It builds a structured prompt, sends it to Ollama with `llama3.2:3b`, and prints the response.

## Why this matters for AI engineering

Good AI applications do not pass vague user text directly to a model. They wrap user input in clear instructions, constraints, and output expectations.

For engineers, prompt templates are like reusable runbooks. They make behavior more consistent and easier to review.

## Concepts covered

- Prompt templates
- Role instructions
- Structured output
- Prompt modes
- AWS explainer prompt
- Terraform reviewer prompt
- Incident summarizer prompt

## Folder structure

```text
day-11-prompt-engineering-for-engineers/
  README.md
  requirements.txt
  sample/
    terraform_snippet.txt
  code/
    main.py
    llm_client.py
    prompt_templates.py
```

## Prerequisites

```bash
ollama pull llama3.2:3b
ollama pull gemma4:latest
```

Use `gemma4:latest` only as a more capable local alternative if you have the RAM for it (it is heavier, not lighter). The lesson defaults to `llama3.2:3b`.

## Setup

```bash
cd day-11-prompt-engineering-for-engineers
python -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Code walkthrough

`prompt_templates.py` stores reusable prompt builders. `llm_client.py` handles the Ollama API call. `main.py` chooses a mode and sends one prompt.

This keeps prompts visible and reviewable instead of hiding them inside UI or API code.

## Run the project

```bash
python code/main.py
```

When you are done recording or testing this lesson:

```bash
deactivate
```

## Expected output

The script loads `sample/terraform_snippet.txt`, builds a `terraform_reviewer` prompt, and prints something like:

```text
Prompt mode: terraform_reviewer
1. The bucket has public access blocks enabled, which is good.
2. Consider adding server-side encryption (aws_s3_bucket_server_side_encryption_configuration).
3. Versioning and lifecycle policies are not set.
...
```

LLM wording varies between runs. Structure and topic should stay consistent.

## Common issues and fixes

If Ollama fails, start Ollama and run `ollama pull llama3.2:3b`. If imports fail, run commands from the lesson root.

## What would change in production

Production prompts should be versioned, evaluated, logged carefully, and tested against known examples. Avoid sending secrets, credentials, or private Terraform plans to a model runtime without a data policy.

## Key takeaways

- Prompt templates make model behavior easier to review.
- Roles and output formats reduce ambiguity.
- Prompt engineering is normal software design around model inputs.
- Templates should be tested like other code.

## Next step

In Day 12, we combine chat, file upload, PDFs, and prompt modes into one local document assistant.
