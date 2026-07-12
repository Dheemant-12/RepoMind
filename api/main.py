from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.exception_handler import global_exception_handler
from api.routes import router

app = FastAPI(
    title="RepoMind",
    version="0.1"
)

# CORS Configuration
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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