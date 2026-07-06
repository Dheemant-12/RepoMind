from git import Repo

from config.settings import REPOS_DIR
from config.logging_config import logger


def clone_repository(repo_url: str) -> str:
    """
    Clone a GitHub repository into the local repos folder.

    Returns:
        Local path of the cloned repository.
    """

    repo_name = repo_url.rstrip("/").split("/")[-1]

    repo_path = REPOS_DIR / repo_name

    # Repository already cloned
    if repo_path.exists():
        logger.info(f"Repository already exists: {repo_path}")
        return str(repo_path)

    # Clone repository
    Repo.clone_from(repo_url, str(repo_path))

    logger.info("Repository cloned successfully.")
    logger.info(f"Location: {repo_path}")

    return str(repo_path)