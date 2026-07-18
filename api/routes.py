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

# Store the last analyzed repository name
LAST_REPOSITORY_NAME = "No Repository"


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze_repository(request: AnalyzeRequest):
    global LAST_REPOSITORY_NAME

    repo_path = clone_repository(request.repo_url)

    repository_name = Path(repo_path).name
    LAST_REPOSITORY_NAME = repository_name

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

    stats = get_repository_statistics(repo_path)

    return DashboardResponse(
        repository=LAST_REPOSITORY_NAME,
        python_files=python_files,
        functions=stats["functions"],
        classes=stats["classes"],
        imports=stats["imports"],
        summary=(
            f"Repository contains {python_files} Python files, "
            f"{stats['functions']} functions, "
            f"{stats['classes']} classes and "
            f"{stats['imports']} imports."
        ),
    )