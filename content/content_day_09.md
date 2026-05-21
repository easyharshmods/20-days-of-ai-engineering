# Day 09 Content Package

## video_title

File Upload AI Assistant with Streamlit - Day 09

## thumbnail_text

Ask Questions About Files

## description

In Day 09 of 20 Days of AI Engineering, we build a local file upload assistant.

The Streamlit app accepts a `.txt` file, previews the extracted text, lets the user ask a question, sends the document context to local Ollama with `llama3.2:3b`, and displays the answer.

This lesson introduces the simplest document Q&A pattern and explains why stuffing full files into prompts does not scale to larger documents.

GitHub repo: coming soon

## chapters

- 00:00 Hook
- 00:00 What we are building
- 00:00 Why document Q&A matters
- 00:00 Uploading text files
- 00:00 Previewing extracted text
- 00:00 Building the document prompt
- 00:00 Calling Ollama
- 00:00 Sensitive file trade-offs
- 00:00 Recap

## youtube_script

# File Upload AI Assistant with Streamlit

## Hook

Many useful AI apps start with a file.

A log, an incident note, a runbook, a policy, or a configuration export often contains the context the model needs.

## Intro

Welcome to Day 09 of 20 Days of AI Engineering.

Today we build a local assistant that answers questions about an uploaded text file.

This is the simplest version of document Q&A: put the document text into the prompt and ask a question.

## Concept Explanation

The flow has four steps.

First, upload a text file.

Second, decode the file into text.

Third, build a prompt that includes the document context and the user question.

Fourth, send that prompt to the local model.

This works for small files. It does not work well for large documents because prompts have size limits and larger context can reduce answer quality.

That limitation is why we will build chunking, embeddings, vector search, and RAG later.

## Hands-on Build

Open `document_logic.py`.

`decode_uploaded_text` turns uploaded bytes into UTF-8 text.

`clean_text` removes trailing whitespace from lines.

`truncate_context` keeps the prompt bounded.

`build_document_question_prompt` creates instructions that tell the model to answer only from the document.

Open `app.py`.

The Streamlit app uses `st.file_uploader` to accept `.txt` files.

It previews extracted text in a text area.

It accepts a question with `st.text_input`.

When the user clicks the button, the app builds the prompt, calls local Ollama, and displays the answer.

Use the sample file `sample/incident_notes.txt` and ask what caused the elevated errors.

## Production Thinking

Uploaded files can be sensitive.

They may contain credentials, customer data, architecture details, or incident information.

Production systems need file type validation, size limits, access control, encryption, malware scanning, retention rules, and audit logs.

This lesson keeps the file local and reads it into memory.

## Recap

Today we built a local text-file Q&A assistant.

We uploaded a file, extracted text, built a bounded prompt, called Ollama, and discussed the limits of full-document prompting.

## CTA

The full code is in the GitHub repository for 20 Days of AI Engineering. Run Day 09 locally and try the sample incident notes.

## pinned_comment

Day 09 builds a local file upload assistant for `.txt` files. It uses Ollama with `llama3.2:3b` and explains why full-document prompting is useful but limited.

## linkedin_post

Day 09 of my 20 Days of AI Engineering series adds file upload.

The app accepts a text file, previews the content, asks a question, and sends the document context to local Ollama using `llama3.2:3b`.

This is the simplest document Q&A pattern. It is useful, but it does not scale to large documents. That sets up chunking and RAG later.

## learning_objectives

- Upload text files with Streamlit.
- Decode uploaded bytes into text.
- Build a document Q&A prompt.
- Limit prompt context size.
- Explain sensitive-file handling trade-offs.

## common_mistakes

- Uploading non-text files before adding parsers.
- Sending very large files into one prompt.
- Forgetting that uploaded files may contain sensitive data.
- Saving uploaded files without a retention policy.
- Letting the model answer beyond the provided document context.

## expected_output

The app opens a local file upload UI. With `sample/incident_notes.txt`, it should answer questions about the incident cause, timeline, impact, and follow-up actions.

