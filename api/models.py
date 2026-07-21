from pydantic import BaseModel


class DashboardResponse(BaseModel):
    repository: str
    python_files: int
    functions: int
    classes: int
    imports: int
    avg_functions_per_file: float
    health_score: int
    health_status: str
    summary: str


class RepositoryTreeResponse(BaseModel):
    repository: str
    files: list[str]


class FileContentResponse(BaseModel):
    file_path: str
    content: str


class ExplainFileRequest(BaseModel):
    file_path: str


class ExplainFileResponse(BaseModel):
    explanation: str


class AskRequest(BaseModel):
    question: str


class AskResponse(BaseModel):
    answer: str


class AnalyzeRequest(BaseModel):
    repo_url: str


class AnalyzeResponse(BaseModel):
    status: str
    repository: str
    message: str