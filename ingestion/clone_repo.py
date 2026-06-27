from git import Repo
import tempfile
import os


def clone_repository(repo_url: str) -> str:
    """
    Clone a GitHub repository into a temporary directory.

    Returns:
        Local path of cloned repository.
    """

    temp_dir = tempfile.mkdtemp()

    Repo.clone_from(repo_url, temp_dir)

    print(f"Repository cloned successfully.")
    print(f"Location: {temp_dir}")

    return temp_dir