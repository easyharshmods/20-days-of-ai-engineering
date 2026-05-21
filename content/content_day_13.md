# Day 13 Content Package

## video_title

Introduction to RAG - Day 13

## thumbnail_text

Intro to RAG

## description

In Day 13 of 20 Days of AI Engineering, we introduce retrieval augmented generation by building the simplest possible version of it.

The script loads a tiny knowledge base from `sample/knowledge_base.json`, scores each document against the user's question with a keyword overlap counter, picks the top matches, builds a prompt that includes only the selected context, and asks `llama3.2:3b` to answer with that context.

There are no embeddings yet, no vector database, and no chunking. The whole point of Day 13 is to separate retrieval from generation in your head, see how the answer changes when you change what is retrieved, and notice exactly where naive keyword matching gets the meaning wrong. That is the setup for embeddings on Day 15.

GitHub repo: coming soon

## chapters

- 00:00 Hook
- 00:00 What RAG actually means
- 00:00 The two-step shape: retrieve, then generate
- 00:00 The tiny knowledge base
- 00:00 Keyword overlap scoring
- 00:00 Building the RAG prompt with sources
- 00:00 Running the script
- 00:00 Where naive retrieval gets it wrong
- 00:00 Production thinking
- 00:00 Recap

## youtube_script

# Introduction to RAG

## Hook

Every time someone says "let's just put it all in the prompt," they are one document away from hitting the context window.

The fix is older than it sounds. Find the parts that matter, then ask the model.

## Intro

Welcome to Day 13 of 20 Days of AI Engineering.

Yesterday we shipped a Streamlit app that stuffed a whole document into a prompt. That works for short files and one-shot questions. It breaks for everything bigger.

Today we change the shape. We retrieve first, then generate. We will use the most boring retrieval possible, on purpose.

## Concept Explanation

RAG stands for retrieval augmented generation. The name describes a two-step pattern, not a model.

Step one is retrieval. Given a question, find the relevant pieces of your data. The retriever does not produce the final answer. Its job is to narrow context.

Step two is generation. Give the model the question plus only the retrieved context, and ask for an answer.

The two steps are usually run by very different things. Retrieval is search, sometimes keyword, sometimes vector, sometimes both. Generation is an LLM. Treating them as separate stages is the part that matters today, because every later RAG improvement is really an upgrade to one stage or the other.

For a cloud engineer, the cleanest analogy is grep then read: search narrows the noise, the model reads what is left.

## Hands-on Build

Open `sample/knowledge_base.json`. It is three documents: a rollback runbook, a retry policy note, and a cost review checklist. Each has an id, a title, and a body.

Open `code/retrieval.py`. The `tokenize` function lowercases and pulls alphanumeric tokens with a regex. `score_document` counts how many tokens the query and document share. `retrieve_documents` scores every document, sorts by score, takes the top two, and drops anything with a score of zero so we never pretend an unrelated document is a hit.

`build_rag_prompt` takes the question and the retrieved documents, joins them with their titles, and produces a single prompt that explicitly tells the model to answer using only the retrieved context.

Open `code/main.py`. It loads the JSON, picks the query, retrieves the top two documents, builds the prompt, and prints the answer from `llama3.2:3b`.

Run the project with `python code/main.py`.

Try changing the query to one that uses different words for the same idea: ask about "reverting a release" instead of "roll back a bad deployment". Notice how the score drops, and how the retrieved set sometimes misses the right document because there is no exact word overlap.

## Production Thinking

Naive keyword retrieval is fine for a teaching lesson. It is not fine for production.

Real RAG systems have to deal with vocabulary mismatch (your users say "revert", your docs say "rollback"), chunking (documents are too long to retrieve whole), source permissions (not every user can see every document), evaluation (you need to measure retrieval quality on real queries), and observability (you need to know which sources were used in any given answer).

There is also a security angle. The retriever decides what context the model sees. If the retriever returns the wrong source, the model will confidently answer from the wrong source. Source metadata, citations, and trust boundaries matter.

We will not solve all of this in 20 days. We will solve the most painful parts: chunking, embeddings, and vector search.

## Recap

Today we built the smallest RAG demo that still teaches the shape: retrieve, then generate.

We scored documents with keyword overlap, took the top results, included them in the prompt, and let `llama3.2:3b` answer.

The interesting part was where the retriever got it wrong. That is the motivation for everything from Day 14 onward.

## CTA

The full code is in the GitHub repository for 20 Days of AI Engineering. Run Day 13, change the query, and find one where keyword overlap misses the right document. Hold on to that example for Day 15.

## pinned_comment

Day 13 is the smallest possible RAG demo: keyword-overlap retrieval over a tiny knowledge base, then `llama3.2:3b` for generation. No embeddings, no vector DB. The point is to separate retrieval from generation and see where naive keyword matching breaks.

## linkedin_post

Day 13 of my 20 Days of AI Engineering series is the entry point into RAG.

I built the simplest possible version: a 3-document JSON knowledge base, a keyword-overlap scorer, top-k selection, and a prompt that gives the model only the retrieved context before calling `llama3.2:3b`.

The interesting moment is when the retriever misses, because the user said "revert" and the doc said "rollback". That is the exact gap embeddings fix, and that is where Day 15 picks up.

## learning_objectives

- Explain RAG as a two-step pattern: retrieve, then generate.
- Implement keyword-overlap scoring as a baseline retriever.
- Build a prompt that includes only retrieved context with source titles.
- Identify where naive retrieval misses semantically similar queries.
- Run an end-to-end retrieve-then-generate flow locally with `llama3.2:3b`.

## common_mistakes

- Calling any "send the document with the question" approach RAG. It is not RAG without a retrieval step.
- Returning unrelated documents instead of filtering by a score threshold.
- Hiding which sources were used, so the answer cannot be traced back.
- Skipping the prompt instruction that ties the answer to the retrieved context.
- Assuming retrieval quality and generation quality are the same problem.

## expected_output

The script scores the three documents in `sample/knowledge_base.json` against *"How should we roll back a bad deployment?"*, picks the top matches (the rollback runbook ranks first), and prints something like:

```text
To roll back a bad deployment, first identify the last stable version and pause new deployments. Deploy the previous artifact, then watch error rate and latency until they return to baseline. If the rollback does not reduce errors, escalate to the platform on-call.
```

Wording varies between runs. The answer should stay grounded in the rollback runbook text.

If Ollama is not running or the model is not pulled, the script exits with a clear error such as `Could not reach Ollama: ...` instead of a raw traceback.
