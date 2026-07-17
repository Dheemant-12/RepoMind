from pydantic import BaseModel


class DashboardResponse(BaseModel):
    repository: str
    python_files: int
    functions: int
    classes: int
    imports: int
    summary: str


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