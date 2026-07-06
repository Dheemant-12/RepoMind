from fastapi import FastAPI

from api.routes import router


app = FastAPI(
    title="RepoMind",
    version="0.1"
)


@app.get("/")
def root():

    return {

        "project": "RepoMind",

        "status": "running"
    }


app.include_router(router)