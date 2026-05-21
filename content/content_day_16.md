# Day 16 Content Package

## video_title

Vector Search with Python and Numpy - Day 16

## thumbnail_text

Vector Search, Locally

## description

In Day 16 of 20 Days of AI Engineering, we use the embeddings from yesterday to build a tiny in-memory vector store and run top-k similarity search.

The script keeps a list of `VectorRecord` items, each with an id, the chunk text, metadata, and the embedding produced by `nomic-embed-text`. A query string gets embedded with the same model, then `search_vectors` ranks every record by cosine similarity and returns the top-k matches with their source metadata still attached.

There is no external database. We deliberately stay on numpy and a Python list. The whole lesson is about the shape of vector search, not about the storage layer. Once that shape is in your head, a real vector database is just a faster, durable version of the same idea.

GitHub repo: coming soon

## chapters

- 00:00 Hook
- 00:00 What top-k vector search is
- 00:00 The VectorRecord shape
- 00:00 Embedding chunks with nomic-embed-text
- 00:00 Cosine similarity with numpy
- 00:00 search_vectors and top-k
- 00:00 Running the project
- 00:00 What changes in a real vector database
- 00:00 Production thinking
- 00:00 Recap

## youtube_script

# Vector Search with Python and Numpy

## Hook

Embeddings are not useful by themselves. They become useful the moment you can rank a million of them against a query and return the closest few.

That ranking is vector search. Today we build the simplest version of it that still teaches the shape.

## Intro

Welcome to Day 16 of 20 Days of AI Engineering.

Day 15 turned text into vectors. Today we use those vectors. We store a handful of chunks in memory, each with its source metadata, embed a query, and return the top matches.

No external vector database. Just numpy and a Python list.

## Concept Explanation

Top-k vector search is straightforward. You have a collection of records, each with an embedding. You take a query string, embed it with the same model, compute the cosine similarity between the query embedding and every record's embedding, and return the top k by score.

Two details matter. The first is that every embedding in the index must come from the same model as the query embedding. Different models live in different vector spaces and the scores are not comparable. The second is that the record carries its source metadata around with the vector. The score tells you how close a chunk is to the query. The metadata is what lets you cite the chunk in the answer.

Real vector databases like FAISS, pgvector, Chroma, Pinecone, or OpenSearch add three things: speed at scale, durability, and metadata filters. None of that changes the shape of the operation we are doing today.

## Hands-on Build

Open `code/vector_search.py`.

`VectorRecord` is a TypedDict with `id`, `text`, `metadata`, and `embedding`. Having an explicit type keeps the index predictable.

`embed_text` calls Ollama's embedding endpoint with `nomic-embed-text` and returns the vector. We use the same function for both indexing chunks and embedding the query, which is exactly the consistency property we want.

`cosine_similarity` tries numpy first and falls back to plain Python. That keeps the lesson runnable even if a learner skips installing numpy.

`search_vectors` is the heart of the file. It builds a list of scored results from the records, sorts by score, and returns the top k. Each result keeps its id, text, metadata, and score.

Open `code/main.py`. Three small runbook-style chunks are defined: a retry chunk with backoff and jitter, a cost review chunk, and a rollback chunk. Each has metadata pointing at its source runbook. We embed all three, embed the query "How do retries avoid overload?", run `search_vectors`, and print the score, source, and text for each top result.

Run the project with `python code/main.py`. The retry chunk should come out first, with its source metadata still attached.

## Production Thinking

In a real system, three things are different.

First, the index is durable. You do not re-embed the world every time the process restarts. Production stores write embeddings, metadata, and source identifiers together, and reload them on startup.

Second, search has to be fast at scale. Cosine similarity over a Python list is fine for thousands of chunks. For millions, you want an index that supports approximate nearest neighbour search, with the trade-off that it returns very-close instead of exactly-closest.

Third, metadata filtering matters. The most useful production retrievers do not just rank by similarity. They also filter by tenant, by document type, by source permissions, or by document freshness. You want to retrieve the closest chunks the current user is allowed to see, not the closest chunks overall.

And again, evaluation. Vector search quality should be measured against real user queries. Recall@k against a labeled set is the cheapest useful metric to start with.

## Recap

Today we ran top-k vector search end-to-end with numpy and Ollama.

We kept the same embedding model on both sides of the query. We carried metadata along with each vector. We ranked by cosine similarity. The retry chunk ranked first against a retry-shaped question.

That is the retrieval engine for the local RAG assistant we put together on Day 17.

## CTA

The full code is in the GitHub repository for 20 Days of AI Engineering. Run Day 16, add two more chunks of your own, and try a query that should retrieve them. Inspect the scores when the right chunk does not win.

## pinned_comment

Day 16 builds the smallest useful vector search: an in-memory list of records with id, text, metadata, and `nomic-embed-text` embedding, ranked by cosine similarity. No external vector database. The shape is what matters.

## linkedin_post

Day 16 of my 20 Days of AI Engineering series is about vector search, on a laptop, in memory.

I built a tiny store of records (id, text, metadata, embedding) and a `search_vectors` function that returns the top-k matches by cosine similarity. Same embedding model on both sides of the query, metadata preserved through the search.

It is small enough to read in one screen, and it is exactly the shape that real vector databases scale up.

## learning_objectives

- Store vectors alongside source metadata in a typed record.
- Use the same embedding model for indexing and querying.
- Rank records by cosine similarity and return the top-k results.
- Reason about what a real vector database adds on top of this shape.
- Carry source metadata through the search so retrieved chunks remain citable.

## common_mistakes

- Embedding the index with one model and the query with another.
- Dropping metadata once the embedding is computed.
- Ranking by raw score without thinking about whether the result is actually relevant.
- Confusing approximate nearest neighbour results with exact cosine search.
- Assuming "vector DB" replaces evaluation and access control.

## expected_output

The script embeds three runbook-style chunks and the query *"How do retries avoid overload?"*, then prints the top matches with score and source metadata:

```text
0.798 | retry-runbook | Retries should use backoff and jitter.
0.412 | rollback-runbook | Rollback deploys the previous stable version.
0.355 | cost-runbook | Cost reviews inspect idle compute.
```

Exact scores depend on the embedding model. The retry chunk should rank first.

If Ollama is not running or `nomic-embed-text` is not pulled, the script exits with a clean error message instead of a raw traceback.
