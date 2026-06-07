import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Local AI API")


class AskRequest(BaseModel):
    question: str


@app.get("/health")
def health():
    return {"status": "ok", "model": "llama3.2:3b"}


@app.post("/ask")
def ask(request: AskRequest):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3.2:3b", "prompt": request.question, "stream": False},
        timeout=90,
    )
    response.raise_for_status()
    return {"answer": response.json()["response"]}
