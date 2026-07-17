import ast
from pathlib import Path


def parse_python_file(file_path):
    """
    Parse a single Python file and return its statistics.
    """

    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source)

    functions = 0
    classes = 0
    imports = 0

    for node in ast.walk(tree):

        if isinstance(node, ast.FunctionDef):
            functions += 1

        elif isinstance(node, ast.AsyncFunctionDef):
            functions += 1

        elif isinstance(node, ast.ClassDef):
            classes += 1

        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            imports += 1

    return {
        "functions": functions,
        "classes": classes,
        "imports": imports,
    }


def get_repository_statistics(repo_path):
    """
    Scan every Python file inside the repository
    and return overall statistics.
    """

    repo_path = Path(repo_path)

    total_functions = 0
    total_classes = 0
    total_imports = 0

    for py_file in repo_path.rglob("*.py"):

        try:
            stats = parse_python_file(py_file)

            total_functions += stats["functions"]
            total_classes += stats["classes"]
            total_imports += stats["imports"]

        except Exception:
            # Skip files that cannot be parsed
            continue

    return {
        "functions": total_functions,
        "classes": total_classes,
        "imports": total_imports,
    }