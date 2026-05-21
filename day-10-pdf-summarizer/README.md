# Day 10 - PDF Summarizer

## What we are building

Today we are building a local PDF summarizer with Streamlit, `pypdf`, and Ollama.

The app lets you upload a PDF, extracts text from its pages, previews the extracted content, sends a bounded summary prompt to `llama3.2:3b`, and displays a practical summary.

## Why this matters for AI engineering

PDFs show up everywhere in engineering work: architecture reviews, security reports, vendor docs, incident writeups, audit exports, and internal runbooks.

AI apps often need to extract text before a model can help. This lesson teaches the simplest version: extract text from a PDF and summarize it locally.

The analogy for this lesson is reading an operational report before a review meeting. The model can summarize only the text we successfully extract.

## Concepts covered

- PDF upload
- PDF text extraction with `pypdf`
- Document preview
- Summarization prompts
- Context limits
- Local-only document handling

## Folder structure

```text
day-10-pdf-summarizer/
  README.md
  requirements.txt
  code/
    app.py
    llm_client.py
    pdf_logic.py
```

## Prerequisites

- Python 3.14.5
- Ollama installed and running
- A small text-based PDF for testing
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
cd day-10-pdf-summarizer
python -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Code walkthrough

`pdf_logic.py` handles document logic:

- `extract_text_from_pdf()` reads uploaded PDF bytes with `pypdf`.
- `truncate_text()` keeps context within a small prompt budget.
- `build_summary_prompt()` asks for an engineering-focused summary.

`llm_client.py` sends the prompt to local Ollama.

`app.py` renders the Streamlit upload UI, document preview, and summary button.

## Run the project

From inside `day-10-pdf-summarizer`, with the virtual environment activated:

```bash
streamlit run code/app.py
```

When you are done recording or testing this lesson:

```bash
deactivate
```

## Expected output

After uploading a text-based PDF, the app should show:

- number of extracted characters
- a document preview
- a summarize button
- a local summary from `llama3.2:3b`

## Common issues and fixes

**Extracted text is empty**

The PDF may be scanned images rather than embedded text. `pypdf` does not perform OCR.

**Summary misses details**

The lesson truncates text to keep the prompt bounded. Large PDFs need chunking and retrieval.

**Ollama connection fails**

Start Ollama and pull the pinned model:

```bash
ollama pull llama3.2:3b
```

## What would change in production

Production PDF workflows need file size limits, file type validation, malware scanning, OCR for scanned documents, retention rules, encryption, access control, and audit logs.

You would also avoid sending confidential PDFs to a model runtime without a clear data handling policy.

## Key takeaways

- PDF extraction is a separate step before summarization.
- Not all PDFs contain extractable text.
- Full-document summarization works only for small documents.
- Uploaded files may contain sensitive data.
- Larger document systems need chunking and retrieval.

## Next step

In Day 11, we will make prompts more reusable with prompt templates for engineering workflows.
