from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

REPOS_DIR = BASE_DIR / "repos"
DATA_DIR = BASE_DIR / "data"
CHROMA_DIR = BASE_DIR / "chroma_db"

REPOS_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)
CHROMA_DIR.mkdir(exist_ok=True)