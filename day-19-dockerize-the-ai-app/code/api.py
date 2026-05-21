from fastapi import FastAPI
from pydantic import BaseModel, Field

from .assistant import DEFAULT_MODEL, answer_question


app = FastAPI(title="Dockerized Local AI API")


class AskRequest(BaseModel):
    question: str = Field(min_length=3, max_length=1_000)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "model": DEFAULT_MODEL}


@app.post("/ask")
def ask(request: AskRequest) -> dict[str, str]:
    return {
        "model": DEFAULT_MODEL,
        "question": request.question,
        "answer": answer_question(request.question),
    }
