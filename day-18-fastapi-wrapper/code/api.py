from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .assistant import DEFAULT_MODEL, AssistantError, answer_question


app = FastAPI(title="Local AI Engineering Assistant API")


class AskRequest(BaseModel):
    question: str = Field(min_length=3, max_length=1_000)


class AskResponse(BaseModel):
    model: str
    question: str
    answer: str


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "model": DEFAULT_MODEL}


@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest) -> AskResponse:
    try:
        answer = answer_question(request.question)
    except AssistantError as error:
        raise HTTPException(status_code=503, detail=str(error)) from error
    return AskResponse(model=DEFAULT_MODEL, question=request.question, answer=answer)
