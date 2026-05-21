# Day 15 Content Package

## video_title

Embeddings Explained with Ollama - Day 15

## thumbnail_text

Embeddings, Locally

## description

In Day 15 of 20 Days of AI Engineering, we replace keyword matching with semantic similarity by generating embeddings locally.

The script asks a question, embeds the question with Ollama's embedding API using `nomic-embed-text`, embeds three engineering notes, and ranks the notes by cosine similarity to the question. There is no generation model in the loop. The whole lesson is about understanding what an embedding is and how similarity ranking works.

Embeddings are the missing piece from Day 13. The retriever there missed when the user said "revert" and the doc said "rollback". Today we move from exact word overlap to meaning, and the same query finds the right document even when no words match.

GitHub repo: coming soon

## chapters

- 00:00 Hook
- 00:00 What an embedding actually is
- 00:00 Pulling nomic-embed-text
- 00:00 The Ollama embeddings API
- 00:00 Cosine similarity with numpy
- 00:00 Ranking notes by similarity
- 00:00 Running the project
- 00:00 What this lets us build later
- 00:00 Production thinking
- 00:00 Recap

## youtube_script

# Embeddings Explained with Ollama

## Hook

Keyword search misses when your users and your docs disagree on the words.

Embeddings fix that, and you can run them locally on a laptop.

## Intro

Welcome to Day 15 of 20 Days of AI Engineering.

Day 13 showed us where naive retrieval breaks. Day 14 built the input side of retrieval, the chunker. Today we build the matching side. We turn text into vectors and rank by meaning, not by exact words.

We do all of this locally, with `nomic-embed-text` running through Ollama. No cloud API, no sentence-transformers, no torch.

## Concept Explanation

An embedding is a vector of numbers that represents the meaning of a piece of text. The model learns these numbers from data, so similar meanings end up at similar coordinates in vector space.

The practical effect is that "How do we avoid retry storms?" and "Use exponential backoff during downstream failures" land near each other, even though they share almost no words.

Cosine similarity is the usual way to compare two vectors. It measures the angle between them, not their length. Two vectors pointing in the same direction score close to 1.0. Two unrelated vectors score close to 0.0. Two opposite vectors score close to -1.0.

For a cloud engineer, the cleanest analogy is metric tags. Two services with similar tag profiles cluster together on a dashboard. Two pieces of text with similar embeddings cluster together in vector space.

## Hands-on Build

First make sure Ollama is running and pull the embedding model: `ollama pull nomic-embed-text`. Generation models like `llama3.2:3b` cannot do this job. Embedding models are trained for it.

Open `code/embeddings.py`.

`get_embedding` calls Ollama's embedding endpoint at `http://localhost:11434/api/embeddings`, sends the text and the model name, and returns the embedding list from the response.

`cosine_similarity` does the math. It tries numpy first for speed and clarity, and falls back to plain Python if numpy is missing, so the function works either way.

`rank_by_similarity` takes a query embedding and a list of items that already have embeddings, computes similarity for each, and returns the list sorted by score descending.

Open `code/main.py`. Three engineering notes are defined: one about exponential backoff for retries, one about cloud cost reviews, and one about rollback procedures. The query is "How do we avoid retry storms?". We embed each note, embed the query, rank, and print the score against each note.

Run the project with `python code/main.py`.

The backoff note ranks first even though the words "retry storms" do not appear in it. That is the whole point.

## Production Thinking

Embeddings have an operational story attached to them.

The embedding model is part of the index. If you change the model, every previously stored vector becomes meaningless to the new model, because the vector space is different. Production systems version the model, the chunking strategy, and the index together.

Similarity is not truth. A high cosine score means two pieces of text live near each other in vector space. It does not mean the model's answer using those chunks is correct. Evaluation still matters.

There is also a privacy angle. Embeddings often look like opaque numbers, but they can be partially inverted, and the source text is usually right next to them in your store. Treat the vector store with the same care as the source documents.

## Recap

Today we generated embeddings locally with `nomic-embed-text` and ranked engineering notes by cosine similarity.

The interesting result was that the relevant note ranked first without any shared keywords. That is the gap we set out to close from Day 13.

Tomorrow we use these vectors for top-k search across a small in-memory store.

## CTA

The full code is in the GitHub repository for 20 Days of AI Engineering. Run Day 15 locally, add two of your own notes, and find a query that ranks them in the order you expected.

## pinned_comment

Day 15 generates local embeddings with `nomic-embed-text` via Ollama, then ranks engineering notes by cosine similarity. This is the semantic step that fixes the keyword-only retrieval from Day 13. Use the same embedding model when you store and when you query.

## linkedin_post

Day 15 of my 20 Days of AI Engineering series is about embeddings, run locally.

I used `nomic-embed-text` through Ollama, embedded a query and three engineering notes, and ranked them by cosine similarity. The backoff note ranked first against a question about retry storms even though they share no exact words.

That is exactly the gap that keyword retrieval cannot close. From here, the next step is using these vectors for real top-k search.

## learning_objectives

- Generate text embeddings locally via Ollama with `nomic-embed-text`.
- Calculate cosine similarity between two vectors with numpy.
- Rank items by semantic similarity to a query.
- Explain why an embedding model is different from a generation model.
- Understand that the embedding model is part of the index, not an interchangeable detail.

## common_mistakes

- Using a generation model like `llama3.2:3b` for embeddings.
- Mixing two different embedding models across the same index.
- Treating cosine similarity as a correctness score.
- Forgetting to pull `nomic-embed-text` before running the script.
- Storing embeddings without recording which model produced them.

## expected_output

The script embeds the query *"How do we avoid retry storms?"* and three engineering notes, then prints the notes ranked by cosine similarity. The retry-related note should come out on top:

```text
Query: How do we avoid retry storms?
0.812 | Retries should use exponential backoff during downstream failures.
0.523 | Rollback procedures should identify the previous stable deployment.
0.487 | Cloud cost reviews should inspect idle compute and storage lifecycle rules.
```

Exact scores depend on the embedding model. The relative ranking should hold.

If Ollama is not running or `nomic-embed-text` is not pulled, the script exits with a clean error pointing at the missing service or model.
