import numpy as np
import requests
import streamlit as st


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

st.title("Local RAG Assistant")
file = st.file_uploader("Upload text", type=["txt"])
question = st.text_input("Question", "Why do retries need backoff?")

if file and st.button("Run RAG"):
    chunks = [
        sentence.strip()
        for sentence in file.getvalue().decode("utf-8", errors="replace").split(".")
        if sentence.strip()
    ]
    query_vector = embed(question)
    ranked = sorted(chunks, key=lambda chunk: cosine(query_vector, embed(chunk)), reverse=True)[:3]
    prompt = f"Use this context: {' '.join(ranked)}\nQuestion: {question}"
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3.2:3b", "prompt": prompt, "stream": False},
        timeout=120,
    )
    response.raise_for_status()
    st.write(response.json()["response"])
    st.caption(ranked)
