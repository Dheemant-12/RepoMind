import ast
from pathlib import Path


def build_dependency_graph(repo_path: Path):
    nodes = set()
    edges = []

    for file in repo_path.rglob("*.py"):
        relative = str(file.relative_to(repo_path))

        nodes.add(relative)

        try:
            source = file.read_text(
                encoding="utf-8"
            )
        except UnicodeDecodeError:
            source = file.read_text(
                encoding="latin-1",
                errors="ignore",
            )

        try:
            tree = ast.parse(source)
        except Exception:
            continue

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):

                for alias in node.names:
                    edges.append(
                        {
                            "from": relative,
                            "to": alias.name,
                        }
                    )

            elif isinstance(node, ast.ImportFrom):

                module = node.module or ""

                edges.append(
                    {
                        "from": relative,
                        "to": module,
                    }
                )

    return {
        "nodes": sorted(nodes),
        "edges": edges,
    }