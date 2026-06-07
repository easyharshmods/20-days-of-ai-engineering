import requests
MODEL = "llama3.2:3b"
URL = "http://localhost:11434/api/generate"

def ask_ollama(prompt):
    response = requests.post(URL, json={"model": MODEL, "prompt": prompt, "stream": False}, timeout=60)
    response.raise_for_status()
    return response.json()["response"]
