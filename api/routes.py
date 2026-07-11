from fastapi import APIRouter
from pathlib import Path

from api.models import (
    AskRequest,
    AskResponse,
    AnalyzeRequest,
    AnalyzeResponse,
)

from llm.reasoning_engine import RepoMindAssistant
from ingestion.clone_repo import clone_repository

router = APIRouter()

assistant = RepoMindAssistant()


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze_repository(request: AnalyzeRequest):

    repo_path = clone_repository(request.repo_url)

    repository_name = Path(repo_path).name

    return AnalyzeResponse(
        status="success",
        repository=repository_name,
        message="Repository cloned successfully. Indexing will be added next."
    )


@router.post("/ask", response_model=AskResponse)
def ask_repo(request: AskRequest):

    answer = assistant.generate_answer(
        request.question
    )

    return AskResponse(
        answer=answer
    )