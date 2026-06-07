import os
import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Dockerized Local AI API")


class AskRequest(BaseModel):
    question: str


@app.post("/ask")
def ask(request: AskRequest):
    base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434").rstrip("/")
    response = requests.post(
        f"{base_url}/api/generate",
        json={"model": "llama3.2:3b", "prompt": request.question, "stream": False},
        timeout=90,
    )
    response.raise_for_status()
    return {"answer": response.json()["response"]}
