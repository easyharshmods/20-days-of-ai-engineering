import numpy as np
import requests


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

query = embed("retry backoff")
for note in ["use exponential backoff", "review idle compute"]:
    print(round(cosine(query, embed(note)), 3), note)
