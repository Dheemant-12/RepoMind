from fastapi import FastAPI
from api.exception_handler import global_exception_handler
from api.routes import router


app = FastAPI(
    title="RepoMind",
    version="0.1"
)
app.add_exception_handler(
    Exception,
    global_exception_handler
)


@app.get("/")
def root():

    return {

        "project": "RepoMind",

        "status": "running"
    }


app.include_router(router)