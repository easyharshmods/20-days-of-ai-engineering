# Day 17 Content Package

## video_title

Local RAG Assistant - Day 17

## thumbnail_text

Local RAG Assistant

## description

In Day 17 of 20 Days of AI Engineering, we put all the RAG pieces together into one Streamlit app that runs entirely on your laptop.

You upload a UTF-8 text file. The app chunks it, embeds every chunk with `nomic-embed-text`, embeds your question with the same model, retrieves the top chunks by cosine similarity, builds a source-aware prompt, and generates the final answer with `llama3.2:3b`. The UI shows both the answer and the retrieved chunks with their scores, so it is obvious which sources the model used.

This is the payoff for the last few days. Day 13 gave us the retrieve-then-generate shape. Day 14 gave us chunking. Day 15 gave us embeddings. Day 16 gave us vector search. Today they become one app.

GitHub repo: coming soon

## chapters

- 00:00 Hook
- 00:00 What we are building
- 00:00 The RAG pipeline at a glance
- 00:00 Chunking the upload
- 00:00 Embedding with nomic-embed-text
- 00:00 Top-k retrieval
- 00:00 The source-aware prompt
- 00:00 Generating with llama3.2:3b
- 00:00 Showing retrieved chunks in the UI
- 00:00 Error handling and a clean UX
- 00:00 Production thinking
- 00:00 Recap

## youtube_script

# Local RAG Assistant

## Hook

For the last few days everything has been pieces. Today the pieces become an app.

This is the local version of what every production RAG system is doing under the hood.

## Intro

Welcome to Day 17 of 20 Days of AI Engineering.

We are going to take the chunker from Day 14, the embedding code from Day 15, the search idea from Day 16, and the local LLM client we have been using since Day 06, and wire them into one Streamlit app.

By the end you will have a working local RAG assistant. Upload a text file, ask a question, get an answer that is grounded in retrieved chunks of the document, and see which chunks were used.

## Concept Explanation

Local RAG is a four-step pipeline.

Chunk the document into overlapping word windows so retrieval has the right granularity. Embed every chunk with the embedding model so each one has a vector. Embed the question with the same model, then retrieve the top-k chunks by cosine similarity. Build a prompt that tells the model to answer using only the retrieved context, then call the generation model.

Two separate models live in this pipeline. The embedding model handles the semantics of retrieval. The generation model handles the wording of the answer. They are not interchangeable.

The other important property is that we show the retrieved chunks in the UI. The user, and you while debugging, can immediately see whether the right context was retrieved. If the retrieval is wrong, the answer will be wrong, and the chunk list tells you that before the model can hide it.

## Hands-on Build

Open `code/rag_logic.py`.

`chunk_text` is a slightly tuned version of the Day 14 chunker, with sixty-word chunks and a ten-word overlap. Each chunk has an id and a metadata block. `cosine_similarity` is the same numpy-with-fallback function we have been using since Day 15. `retrieve` scores embedded chunks against a query embedding and returns the top three by score. `build_rag_prompt` joins the retrieved chunks with their ids and scores into a single context block, then asks the model to answer using only that context.

Open `code/llm_client.py`. This module is the local Ollama client. It exposes a `LocalLlmError` exception, `DEFAULT_MODEL = "llama3.2:3b"`, `EMBEDDING_MODEL = "nomic-embed-text"`, and two functions: `embed_text` and `generate_answer`. Both wrap their HTTP calls in try/except for `requests.RequestException` and raise `LocalLlmError` with a helpful message if Ollama is unreachable, so a stopped Ollama becomes a single line of text instead of a traceback.

Open `code/app.py`. Streamlit gives us a file uploader, a question input, and a button. When the user clicks **Run local RAG**, the app chunks the text, embeds each chunk, embeds the question, retrieves the top chunks, builds the prompt, and generates the answer. The whole block is wrapped in a `try`/`except LocalLlmError` so any failure surfaces as a friendly `st.error` instead of a stack trace.

Below the answer, the app shows the retrieved chunks with their id, score, and a text preview. That panel is the single most useful debugging tool in a RAG system.

Run the project with `streamlit run code/app.py`.

## Production Thinking

A real RAG system has to deal with much more than this.

Indexing is a durable concern. You do not re-chunk and re-embed on every upload. You store chunks and embeddings somewhere persistent and reindex deliberately when chunking or models change.

Permissions matter. The retriever should only return chunks the requesting user is allowed to see. That usually means metadata filters tied to identity, not just a top-k over the whole index.

Evaluation matters. You need a small labeled set of queries and expected sources, run on every change to chunking, embeddings, or the prompt, so retrieval and generation quality do not drift silently.

Sensitive uploads matter. Documents from real engineering teams contain access controls, runbooks, account ids, and incident detail. Local RAG is fine for a demo. Production RAG needs encryption at rest, audit, retention policies, and clear answers to who can see which chunks.

## Recap

Today we built a complete local RAG assistant: chunk, embed, retrieve, generate.

The most important UX choice was showing the retrieved chunks alongside the answer. That panel is what makes RAG legible to the people using it and the people debugging it.

This is the last lesson where everything runs purely local. Day 18 turns the assistant into a service, Day 19 packages it in Docker, and Day 20 maps the whole thing to AWS.

## CTA

The full code is in the GitHub repository for 20 Days of AI Engineering. Run Day 17 with the sample platform notes, then try a longer document and see how chunking, retrieval scores, and the answer all move together.

## pinned_comment

Day 17 puts the RAG pipeline together: chunk, embed with `nomic-embed-text`, retrieve top-k by cosine similarity, generate with `llama3.2:3b`, show retrieved chunks in the UI. All local. Wrapped errors so a stopped Ollama shows a clean message instead of a traceback.

## linkedin_post

Day 17 of my 20 Days of AI Engineering series is the local RAG assistant.

It is the payoff for the last four lessons. Chunking from Day 14, embeddings from Day 15, vector search from Day 16, and the local Ollama client all wire into one Streamlit app. Upload a text file, ask a question, see the answer and the retrieved chunks side by side.

Two design choices I would carry into production. Use a real embedding model that is different from the generation model. And always show retrieved sources in the UI, because that is what makes RAG actually debuggable.

## learning_objectives

- Combine chunking, embeddings, vector retrieval, and generation into one local app.
- Use `nomic-embed-text` for retrieval and `llama3.2:3b` for generation.
- Show retrieved chunks in the UI alongside the generated answer.
- Wrap the pipeline in a single `try`/`except LocalLlmError` for a clean failure message.
- Reason about what would change to turn this into a production RAG system.

## common_mistakes

- Using the same model for embedding and generation.
- Hiding which chunks were retrieved, so failures look like model failures.
- Re-chunking and re-embedding on every interaction in a production system.
- Treating top-k score as evidence the answer is correct.
- Forgetting to pull both `nomic-embed-text` and `llama3.2:3b` before running.

## expected_output

A Streamlit app runs at `http://localhost:8501` with:

- a file uploader for a UTF-8 `.txt` file
- a question input
- a **Run local RAG** button

Upload `sample/platform_notes.txt`, ask *"Why do retries need backoff?"*, and after a brief spinner the app shows:

- an **Answer** section with a grounded explanation drawn from the retrieved chunks
- a **Retrieved chunks** section listing each chunk used, with its id, similarity score, and text preview

If Ollama is not running or either model is missing, the UI shows a clean `LocalLlmError` message at the top of the page instead of a traceback.
