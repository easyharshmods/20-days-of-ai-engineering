# Day 12 - Local Document Assistant

## What we are building

Today we are building a Streamlit document assistant that combines chat-style questions, text upload, PDF upload, and prompt modes.

The app extracts document text, lets you choose a mode, builds a bounded prompt, and sends it to local Ollama with `llama3.2:3b`.

## Why this matters for AI engineering

Real AI tools combine pieces: file handling, prompt templates, model calls, UI state, and production guardrails. This lesson is a small complete local workflow before we introduce RAG.

## Concepts covered

- Text and PDF upload
- Prompt modes
- Document context
- Chat over files
- Limits of stuffing full documents into prompts

## Folder structure

```text
day-12-local-document-assistant/
  README.md
  requirements.txt
  sample/ops_runbook.txt
  code/app.py
  code/document_logic.py
  code/llm_client.py
```

## Prerequisites

```bash
ollama pull llama3.2:3b
ollama pull gemma4:latest
```

## Setup

```bash
cd day-12-local-document-assistant
python -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Code walkthrough

`document_logic.py` extracts text, truncates context, and builds prompts. `app.py` provides upload and question controls. `llm_client.py` calls Ollama.

## Run the project

```bash
streamlit run code/app.py
```

When you are done recording or testing this lesson:

```bash
deactivate
```

## Expected output

A local Streamlit app at `http://localhost:8501` with:

- a file uploader that accepts `.txt` or `.pdf`
- a mode selector (`answer question`, `summarize`, `find risks`, `extract actions`)
- a question input
- a document preview pane
- an answer pane that appears after clicking **Ask document assistant**

Upload `sample/ops_runbook.txt`, pick `summarize`, click the button, and the answer pane shows a short engineer-focused summary of the runbook.

## Common issues and fixes

Scanned PDFs may have no extractable text. Large files are truncated. Start Ollama if the model call fails.

## What would change in production

Production needs auth, file scanning, retention controls, encryption, access control, size limits, and audit logs. Uploaded files may contain sensitive data.

## Key takeaways

- A document assistant combines several simple components.
- Full-document prompting is useful but limited.
- Prompt modes make the assistant more predictable.
- Local-only does not remove data handling concerns.

## Next step

In Day 13, we introduce RAG and build a naive retrieval flow.
