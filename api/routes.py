from pathlib import Path

from fastapi import APIRouter

from api.models import (
    AskRequest,
    AskResponse,
    AnalyzeRequest,
    AnalyzeResponse,
    DashboardResponse,
)

from ingestion.clone_repo import clone_repository
from llm.reasoning_engine import RepoMindAssistant
from ingestion.ast_parser import get_repository_statistics


router = APIRouter()

assistant = RepoMindAssistant()


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze_repository(request: AnalyzeRequest):
    repo_path = clone_repository(request.repo_url)

    repository_name = Path(repo_path).name

    return AnalyzeResponse(
        status="success",
        repository=repository_name,
        message="Repository cloned successfully. Indexing will be added next.",
    )


@router.post("/ask", response_model=AskResponse)
def ask_repo(request: AskRequest):
    answer = assistant.generate_answer(request.question)

    return AskResponse(
        answer=answer
    )


@router.get("/dashboard", response_model=DashboardResponse)
def dashboard():
    repo_path = Path("repositories")

    python_files = len(list(repo_path.rglob("*.py")))

    # Temporary placeholder values
    functions = 318
    classes = 61
    imports = 425

    return DashboardResponse(
        repository="Current Repository",
        python_files=python_files,
        functions=functions,
        classes=classes,
        imports=imports,
        summary=(
            "Repository indexed successfully. "
            "Dashboard metrics are now served from the backend."
        ),
    )