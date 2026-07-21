from pathlib import Path

from fastapi import APIRouter, HTTPException
from api.models import (
    AskRequest,
    AskResponse,
    AnalyzeRequest,
    AnalyzeResponse,
    DashboardResponse,
    RepositoryTreeResponse,
    FileContentResponse,
)

from config.settings import REPOS_DIR
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

    return AskResponse(answer=answer)


@router.get("/dashboard", response_model=DashboardResponse)
def dashboard():
    repo_path = REPOS_DIR

    python_files = len(list(repo_path.rglob("*.py")))

    stats = get_repository_statistics(repo_path)

    functions = stats["functions"]
    classes = stats["classes"]
    imports = stats["imports"]

    avg_functions = (
        round(functions / python_files, 2)
        if python_files > 0 else 0
    )

    health_score = 100

    if avg_functions > 12:
        health_score -= 20

    if imports > functions:
        health_score -= 10

    if classes == 0:
        health_score -= 20

    health_score = max(0, health_score)

    if health_score >= 85:
        health_status = "🟢 Excellent"
    elif health_score >= 65:
        health_status = "🟡 Good"
    else:
        health_status = "🔴 Needs Improvement"

    return DashboardResponse(
        repository=LAST_REPOSITORY_NAME,
        python_files=python_files,
        functions=functions,
        classes=classes,
        imports=imports,
        avg_functions_per_file=avg_functions,
        health_score=health_score,
        health_status=health_status,
        summary=(
            f"{health_status} repository. "
            f"{python_files} Python files, "
            f"{functions} functions, "
            f"{classes} classes and "
            f"{imports} imports detected."
        ),
    )


@router.get("/repository-tree", response_model=RepositoryTreeResponse)
def repository_tree():
    repo_root = REPOS_DIR

    files = []

    if repo_root.exists():
        for file in repo_root.rglob("*"):
            if file.is_file():
                files.append(str(file.relative_to(repo_root)))

    files.sort()

    return RepositoryTreeResponse(
        repository=LAST_REPOSITORY_NAME,
        files=files,
    )


@router.get("/file-content", response_model=FileContentResponse)
def file_content(path: str):
    repo_root = REPOS_DIR
    file_path = repo_root / path

    if not file_path.exists() or not file_path.is_file():
        raise HTTPException(status_code=404, detail="File not found")

    try:
        content = file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        content = file_path.read_text(
            encoding="latin-1",
            errors="ignore"
        )
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Unable to read file",
        )

    return FileContentResponse(
        file_path=path,
        content=content,
    )