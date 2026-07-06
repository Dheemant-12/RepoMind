from fastapi import APIRouter

from api.models import AskRequest, AskResponse

from llm.reasoning_engine import RepoMindAssistant


router = APIRouter()

assistant = RepoMindAssistant()


@router.post("/ask", response_model=AskResponse)
def ask_repo(request: AskRequest):

    answer = assistant.generate_answer(
        request.question
    )

    return AskResponse(
        answer=answer
    )