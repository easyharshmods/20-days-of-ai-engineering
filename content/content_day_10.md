# Day 10 Content Package

## video_title

Local PDF Summarizer with Ollama - Day 10

## thumbnail_text

Summarize PDFs Locally

## description

In Day 10 of 20 Days of AI Engineering, we build a local PDF summarizer.

The Streamlit app uploads a PDF, extracts text with `pypdf`, previews the extracted content, sends a bounded summary prompt to Ollama using `llama3.2:3b`, and displays an engineering-focused summary.

This lesson explains both the usefulness and limits of basic PDF summarization before we move into prompt templates and retrieval.

GitHub repo: coming soon

## chapters

- 00:00 Hook
- 00:00 What we are building
- 00:00 Why PDFs matter
- 00:00 Upload a PDF
- 00:00 Extract text with pypdf
- 00:00 Build a summary prompt
- 00:00 Call Ollama
- 00:00 Production file handling
- 00:00 Recap

## youtube_script

# Local PDF Summarizer with Ollama

## Hook

Engineering teams have a lot of important information trapped in PDFs.

Architecture reviews, audit reports, vendor docs, and incident summaries often arrive as documents before they become structured data.

## Intro

Welcome to Day 10 of 20 Days of AI Engineering.

Today we build a local PDF summarizer with Streamlit, `pypdf`, and Ollama.

## Concept Explanation

The model cannot summarize a PDF file directly in this app.

First, Python extracts text from the PDF. Then we place that extracted text into a prompt. Then the local model summarizes that text.

This is simple and useful for small text-based PDFs.

It does not solve scanned documents, very large files, or precise source retrieval.

## Hands-on Build

Open `pdf_logic.py`.

`extract_text_from_pdf` reads PDF bytes with `pypdf` and extracts text page by page.

`truncate_text` keeps the prompt bounded.

`build_summary_prompt` asks the model for an executive summary, technical details, risks, and next actions.

Open `app.py`.

The Streamlit app uploads a PDF, extracts text, shows a preview, and calls Ollama when the user clicks the summarize button.

Run the app with `streamlit run code/app.py`.

## Production Thinking

Production PDF processing needs strict controls.

You need file size limits, type validation, malware scanning, OCR for scanned PDFs, encryption, access control, retention rules, and audit logs.

You also need to decide whether the model runtime is allowed to receive the document text.

## Recap

Today we extracted text from PDFs and summarized it locally.

We also saw the limits of full-document summarization: extracted text quality, prompt size, and sensitive file handling.

## CTA

The full code is in the GitHub repository for 20 Days of AI Engineering. Run Day 10 locally with a small text-based PDF.

## pinned_comment

Day 10 builds a local PDF summarizer using Streamlit, `pypdf`, Ollama, and `llama3.2:3b`. Scanned PDFs may need OCR, which is outside this lesson.

## linkedin_post

Day 10 of my 20 Days of AI Engineering series is a local PDF summarizer.

The app uploads a PDF, extracts text with `pypdf`, previews the content, and sends a bounded prompt to local Ollama with `llama3.2:3b`.

The useful lesson is the boundary: PDF extraction is separate from model summarization, and full-document prompting only works for small documents.

## learning_objectives

- Upload PDFs with Streamlit.
- Extract text from text-based PDFs with `pypdf`.
- Build a structured summarization prompt.
- Keep document context bounded.
- Explain production risks around uploaded PDFs.

## common_mistakes

- Expecting `pypdf` to read scanned image PDFs.
- Sending very large PDFs into one prompt.
- Ignoring sensitive document handling.
- Mixing extraction, prompting, and UI logic into one large function.
- Treating generated summaries as verified facts without review.

## expected_output

The app opens a local PDF upload UI, extracts text, previews it, and generates a local summary using `llama3.2:3b`.

