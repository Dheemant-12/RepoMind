import ast


def extract_functions(file_path: str):
    """
    Extract all functions from a Python file.
    """

    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    lines = source.splitlines()

    tree = ast.parse(source)

    functions = []

    for node in ast.walk(tree):

        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):

            function_data = {
                "name": node.name,
                "file_path": file_path,
                "start_line": node.lineno,
                "end_line": node.end_lineno,
                "arguments": [arg.arg for arg in node.args.args],
                "source_code": "\n".join(
                    lines[node.lineno - 1: node.end_lineno]
                ),
            }

            functions.append(function_data)

    return functions