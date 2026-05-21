# Day 12 Content Package

## video_title

Local Document Assistant - Day 12

## thumbnail_text

Local Document Assistant

## description

In Day 12 of 20 Days of AI Engineering, we combine everything from the past week into one Streamlit app: text upload, PDF upload, prompt modes, and a local Ollama call with `llama3.2:3b`.

The app accepts a `.txt` or `.pdf` file, extracts the text, lets the user pick a mode (`answer question`, `summarize`, `find risks`, `extract actions`), shows a document preview, builds a single bounded prompt, and sends the whole document context to local Ollama. We cap the context at six thousand characters so the prompt does not blow past the model window.

This is the last lesson where we stuff a full document into a single prompt. By the end of Day 12 the limit of that approach is obvious, and that limit is the motivation for retrieval, embeddings, and RAG starting in Day 13.

GitHub repo: coming soon

## chapters

- 00:00 Hook
- 00:00 What we are building
- 00:00 Why full-document prompting hits a wall
- 00:00 Reusing extraction from txt and PDF
- 00:00 Mode selector and prompt builder
- 00:00 The 6,000-character context cap
- 00:00 Running the app with the ops runbook
- 00:00 Production thinking
- 00:00 Recap

## youtube_script

# Local Document Assistant

## Hook

A lot of internal AI assistants stop here. Upload a document, pick a mode, get an answer.

It works well enough for short files. The trouble starts the moment someone uploads a real runbook, a long incident log, or a multi-page architecture doc. Suddenly the prompt is too big, the model ignores half of it, and answers get vague.

That wall is the reason RAG exists. Today we walk straight into it, on purpose.

## Intro

Welcome to Day 12 of 20 Days of AI Engineering.

This is a checkpoint lesson. We pull together the pieces from Days 07 through 11: Streamlit, file upload, PDF extraction, prompt templates, and the local Ollama call.

We build one Streamlit app, `code/app.py`, that handles both `.txt` and `.pdf`, lets the user pick a mode, and sends a bounded prompt to `llama3.2:3b`.

## Concept Explanation

The full-document pattern is simple. Read the file, drop the text into the prompt, ask a question, get an answer.

It is useful. It works well for short files where the whole document genuinely fits and the question is about the document as a whole.

It has two real limits. The first is the model's context window. Long documents do not fit, so we either truncate and lose information, or we exceed the window and the model gets confused. The second is signal. Even when the document fits, the model has to read every word to answer one question. Relevant facts get diluted.

In the next lesson we start fixing this by retrieving only the relevant chunks. Today we feel the pain so the fix makes sense.

## Hands-on Build

Open `code/document_logic.py`. It has four small functions.

`extract_text_from_txt` decodes the upload as UTF-8 with replacement for unknown bytes, so a stray non-UTF-8 character does not crash the app.

`extract_text_from_pdf` uses `pypdf` to walk the pages and prefix each one with `[Page N]`. Pages with no extractable text are skipped, which matters for scanned PDFs.

`truncate_context` enforces a six-thousand-character cap. If the document is longer, it cuts at the cap and appends `[Document truncated]` so the model knows it did not see everything.

`build_document_prompt` puts the model in a document-assistant role, names the mode, includes the truncated document between delimiters, and adds the question.

Open `code/app.py`. Streamlit gives us the file uploader, the mode selectbox, the question input, and the button. When the user clicks **Ask document assistant**, we route to the right extractor based on file extension, show a preview pane, build the prompt, and call `generate_answer` from `llm_client`. If the call fails, we show a clean error in the UI instead of a traceback.

Run the project with `streamlit run code/app.py`.

## Production Thinking

This is a real moment to talk about uploaded files.

Documents users upload to an assistant often contain things you do not want to leak. Incident notes name people. Runbooks describe controls. Architecture docs describe blast radius. A demo that keeps everything in memory is fine. A production version needs access controls, scanning, retention rules, audit logs, and a clear answer for who can see what.

There is also the truncation behavior. We tell the model when we truncated, but a production app should make truncation visible to the user and ideally point them at retrieval instead of silently cutting.

And model choice. A small local model is great for trying things on your laptop. A real internal tool needs evaluation, prompt versioning, and a deliberate decision about where the document text actually lives.

## Recap

Today we combined upload, extraction, prompt modes, and local generation into one app.

The app is intentionally the simplest form of document Q&A: stuff the whole document in, ask one question, get one answer. That pattern has a ceiling, and we hit it on purpose.

Starting tomorrow we change the shape of the problem. Instead of sending the whole document, we retrieve the parts that matter.

## CTA

The full code is in the GitHub repository for 20 Days of AI Engineering. Run Day 12 with the sample ops runbook, then try a longer document of your own and watch where the answers get vague.

## pinned_comment

Day 12 combines text upload, PDF upload, four prompt modes, and a 6,000-character context cap into one Streamlit app calling `llama3.2:3b` locally. This is the last full-document-prompting lesson before we move to retrieval and RAG in Day 13.

## linkedin_post

Day 12 of my 20 Days of AI Engineering series is the checkpoint before RAG.

One Streamlit app: txt or PDF upload, mode selector, bounded prompt, local Ollama with `llama3.2:3b`. It handles everyday "ask my document" use cases well.

It also fails predictably on long documents, and that is the point. From Day 13 onward we stop stuffing whole documents into the prompt and start retrieving the relevant parts.

## learning_objectives

- Combine file upload, PDF extraction, prompt modes, and the local LLM call in one app.
- Use a single bounded prompt with a clear character cap.
- Explain when full-document prompting stops working and why.
- Handle txt and PDF uploads with the same downstream code path.
- Show truncation to the user instead of silently dropping context.

## common_mistakes

- Treating temporary in-memory upload handling as production-ready.
- Sending the entire document into the prompt with no cap and no truncation signal.
- Mixing prompt construction inside Streamlit callback code.
- Forgetting that PDFs can be scanned images and contain no extractable text.
- Believing full-document prompting will scale to long documents if you "just use a bigger model".

## expected_output

A Streamlit app runs at `http://localhost:8501` with:

- a file uploader that accepts `.txt` or `.pdf`
- a mode selector (`answer question`, `summarize`, `find risks`, `extract actions`)
- a question input
- a document preview pane
- an **Answer** pane that appears after clicking **Ask document assistant**

Upload `sample/ops_runbook.txt`, pick `summarize`, click the button, and the answer pane shows a short engineer-focused summary grounded in the runbook. Long documents are truncated at six thousand characters with a `[Document truncated]` marker.

If Ollama is not running or the model is not pulled, the UI shows a clean error message instead of crashing.
