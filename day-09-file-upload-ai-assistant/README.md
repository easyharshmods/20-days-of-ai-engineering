# Day 09 - File Upload AI Assistant

## What we are building

Today we are building a local Streamlit assistant that answers questions about an uploaded text file.

The app lets you upload a `.txt` file, previews the extracted text, accepts a question, sends the document context and question to Ollama, and displays the answer from `llama3.2:3b`.

## Why this matters for AI engineering

Many AI applications are document workflows: logs, runbooks, incident notes, architecture docs, policy files, tickets, and configuration exports.

Before building RAG, it helps to understand the simplest version: put a document into the prompt and ask a question about it. This works for small files, but it does not scale to large documents.

The analogy for this lesson is handing a short runbook to a teammate before asking a question. The teammate can answer only from the context you provide.

## Concepts covered

- Streamlit file upload
- Text extraction from uploaded files
- Document preview
- Prompt construction with document context
- Document Q&A
- Sensitive-file handling
- Limits of stuffing full documents into prompts

## Folder structure

```text
day-09-file-upload-ai-assistant/
  README.md
  requirements.txt
  sample/
    incident_notes.txt
  code/
    app.py
    document_logic.py
    llm_client.py
```

## Prerequisites

- Python 3.14.5
- Ollama installed and running
- The pinned default model:

```bash
ollama pull llama3.2:3b
```

Optional more capable alternative model (heavier, needs more RAM):

```bash
ollama pull gemma4:latest
```

The app uses `llama3.2:3b` by default.

## Setup

Run these commands from the repository root:

```bash
cd day-09-file-upload-ai-assistant
python -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Code walkthrough

The app has three main code files:

- `document_logic.py` cleans uploaded text, limits context length, and builds the document Q&A prompt.
- `llm_client.py` calls local Ollama.
- `app.py` renders the upload UI, preview, question input, and answer area.

The app reads uploaded bytes as UTF-8 text. It does not store the upload on disk.

The prompt asks the model to answer only from the provided document and say when the document does not contain enough information.

## Run the project

From inside `day-09-file-upload-ai-assistant`, with the virtual environment activated:

```bash
streamlit run code/app.py
```

When you are done recording or testing this lesson:

```bash
deactivate
```

## Expected output

Use `sample/incident_notes.txt` as a test upload.

Ask:

```text
What caused the elevated errors?
```

The answer should reference the uploaded incident notes.

## Common issues and fixes

**Uploaded file has unreadable characters**

This lesson expects UTF-8 `.txt` files. PDFs and other formats come later.

**Answer ignores part of the file**

The app limits document context to keep the prompt small. Larger documents need chunking and retrieval, which we will build later.

**Ollama connection fails**

Start Ollama and pull the pinned model:

```bash
ollama pull llama3.2:3b
```

## What would change in production

Uploaded files can contain credentials, customer data, incident details, or internal architecture information.

In production, you would define file size limits, file type validation, malware scanning, retention rules, encryption, access control, redaction, and audit logging.

This lesson keeps processing local and does not write uploaded files to disk.

## Key takeaways

- File upload turns an AI app into a document workflow.
- Small text files can be placed directly into a prompt.
- Prompt context should be bounded.
- Uploaded files may contain sensitive data.
- Full-document prompting does not scale to large files.

## Next step

In Day 10, we will extract text from PDFs and build a local PDF summarizer.
