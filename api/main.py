from fastapi import FastAPI

app = FastAPI(
    title="RepoMind",
    description="AI-powered repository analysis using Knowledge Graphs and Vector Search",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "project": "RepoMind",
        "version": "0.1.0",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }