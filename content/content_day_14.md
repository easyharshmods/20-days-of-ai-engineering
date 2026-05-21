# Day 14 Content Package

## video_title

Text Chunking for RAG - Day 14

## thumbnail_text

Chunking for RAG

## description

In Day 14 of 20 Days of AI Engineering, we build a small word-based text chunking utility with overlap and metadata.

The script reads `sample/runbook.txt`, splits the text into overlapping chunks of a configurable word count, and prints each chunk with its id, word count, and preview. There is no LLM call. The whole lesson is about the input side of retrieval.

Chunking sounds boring until you realize it is the lever that controls retrieval quality. Chunks that are too small lose context. Chunks that are too large waste prompt space and bury the relevant detail. Overlap stitches neighboring chunks together so a single concept does not get sliced in half. Metadata is how the rest of the RAG pipeline knows where a chunk came from.

GitHub repo: coming soon

## chapters

- 00:00 Hook
- 00:00 Why chunking is a design choice
- 00:00 Word-based chunking and TypedDict metadata
- 00:00 Walking through chunk_text
- 00:00 The role of overlap
- 00:00 Running the project on the runbook sample
- 00:00 Tuning chunk size and overlap
- 00:00 Production chunking
- 00:00 Recap

## youtube_script

# Text Chunking for RAG

## Hook

Most RAG quality problems get blamed on the model or the embeddings.

Half the time, the real culprit is upstream. The chunks are bad.

## Intro

Welcome to Day 14 of 20 Days of AI Engineering.

Day 13 gave us the retrieve-then-generate shape. Day 15 will give us embeddings. In between, today, we build the preprocessing step that decides what gets embedded in the first place.

We are not calling an LLM today. We are building a small chunking utility and running it on a real runbook.

## Concept Explanation

Chunking is the act of splitting a document into smaller pieces that you will later embed, index, and retrieve.

Three knobs matter. Chunk size controls how much text lives in one chunk. Overlap controls how much text is shared between neighboring chunks. Metadata controls what travels with each chunk so the retriever can tell where it came from.

A small chunk is precise but loses surrounding context. A large chunk preserves context but dilutes the relevant tokens and wastes prompt space later. Overlap is the practical compromise: the same concept appears in two neighboring chunks so retrieval cannot accidentally slice it.

There is no universal chunk size. Sentence-based, token-based, paragraph-based, and structure-aware chunking all work in different settings. Today we use word-based chunking because it is easy to read and easy to teach.

## Hands-on Build

Open `code/chunking.py`.

There is a `TextChunk` TypedDict at the top: `chunk_id`, `source`, `chunk_index`, `text`, and `word_count`. The id is the source name plus the index, which makes chunks easy to cite later.

`chunk_text` does the work. It validates that `chunk_size_words` is positive and that `overlap_words` is less than the chunk size, so an invalid call fails immediately. It splits the document by whitespace, then walks the word list in windows. Each window becomes a chunk, and the next window starts `chunk_size_words - overlap_words` later. The loop exits when the current window reaches the end of the word list.

Open `code/main.py`. It reads `sample/runbook.txt`, calls `chunk_text` with a chunk size of 35 words and an overlap of 7 words, and prints each chunk's id, word count, and a 90-character preview.

Run the project with `python code/main.py`.

The sample runbook is about 71 words, so you get three chunks. The first two are full chunks of 35 words. The third is a shorter tail chunk. The overlap between neighbors shows up clearly in the printed previews.

Now try changing the parameters. Drop chunk size to 20 and you get more chunks with finer-grained retrieval and more redundancy. Drop overlap to 0 and you can see boundary problems start to appear, where a sentence ends in one chunk and the next one starts mid-thought.

## Production Thinking

Word-based chunking is the right teaching tool. It is not always the right production tool.

Production chunkers respect structure. They split at section headings, paragraph breaks, list items, or token boundaries depending on the document type. They also count tokens, not words, because the model's context window is measured in tokens.

Metadata in production carries more than the index. It carries the source path, document type, version, author, sensitivity label, and any access-control identifier that the retriever needs to enforce permissions.

And then there is reindexing. The moment you change the chunk size, the overlap rule, or the embedding model, every chunk in your index is suddenly inconsistent with the new pipeline. Production systems plan for that.

## Recap

Today we built a small chunking utility with size, overlap, and metadata.

The point is not the code, which is short. The point is that the chunking step is a design decision that shapes everything downstream: retrieval precision, prompt budget, and the quality of the final answer.

## CTA

The full code is in the GitHub repository for 20 Days of AI Engineering. Run Day 14 on the sample runbook, then change the chunk size and overlap and watch how the chunks shift. Keep this utility in mind for Day 17, where we use it inside a real RAG pipeline.

## pinned_comment

Day 14 is the preprocessing lesson before embeddings: a small word-based chunker with size, overlap, and metadata. No LLM call. The chunking step is the lever that controls retrieval quality.

## linkedin_post

Day 14 of my 20 Days of AI Engineering series is about text chunking.

I built a small word-based chunker with configurable size, overlap, and per-chunk metadata. No LLM call. The whole lesson sits before embeddings on purpose.

Chunking is the cheapest place to ruin retrieval and the cheapest place to fix it. If your RAG answers feel vague, the model and the embeddings are often not the problem. The chunks are.

## learning_objectives

- Split text into chunks with a configurable word count.
- Use overlap to preserve context across chunk boundaries.
- Attach metadata so retrieved chunks remain traceable.
- Validate chunk parameters at the API boundary.
- Reason about the trade-off between chunk size, recall, and prompt budget.

## common_mistakes

- Picking a single chunk size and reusing it for every document type.
- Setting overlap to zero and then wondering why retrieval cuts ideas in half.
- Dropping metadata so the rest of the pipeline cannot cite sources.
- Confusing word count and token count when planning for the model's context window.
- Treating chunking as a one-time decision instead of something to revisit when retrieval changes.

## expected_output

`sample/runbook.txt` is roughly 71 words. With `chunk_size_words=35` and `overlap_words=7`, the script prints three chunks:

```text
runbook:0 | words=35 | Rollback runbook for checkout-api. First confirm the active deployment version and the last stable v
runbook:1 | words=35 | active. Deploy the previous stable artifact. Watch error rate, latency, saturation, and database co
runbook:2 | words=15 | escalate to the platform on-call and database on-call. After recovery, ...
```

Exact preview text depends on the sample. The chunk count and the visible overlap between neighbors are the things to verify.
