import numpy as np
import requests

chunks = ["Retries need backoff and jitter", "Cost reviews inspect idle compute"]


def embed(text):
    response = requests.post(
        "http://localhost:11434/api/embeddings",
        json={"model": "nomic-embed-text", "prompt": text},
        timeout=60,
    )
    response.raise_for_status()
    return np.array(response.json()["embedding"])


def cosine(a, b):
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

question = "How should retries work?"
query_vector = embed(question)
best_chunk = max(chunks, key=lambda chunk: cosine(query_vector, embed(chunk)))
prompt = f"Context: {best_chunk}\nQuestion: {question}"
print(prompt)

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "llama3.2:3b", "prompt": prompt, "stream": False},
    timeout=90,
)
response.raise_for_status()
print(response.json()["response"])
