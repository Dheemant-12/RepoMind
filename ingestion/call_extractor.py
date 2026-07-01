import ast


class CallVisitor(ast.NodeVisitor):
    def __init__(self):
        self.calls = []

    def visit_Call(self, node):

        if isinstance(node.func, ast.Name):
            self.calls.append(node.func.id)

        elif isinstance(node.func, ast.Attribute):

            parts = []

            current = node.func

            while isinstance(current, ast.Attribute):
                parts.append(current.attr)
                current = current.value

            if isinstance(current, ast.Name):
                parts.append(current.id)

            self.calls.append(".".join(reversed(parts)))

        self.generic_visit(node)


def extract_calls(file_path: str):

    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source)

    results = []

    for node in ast.walk(tree):

        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):

            visitor = CallVisitor()

            visitor.visit(node)

            results.append(
                {
                    "function": node.name,
                    "file_path": file_path,
                    "calls": visitor.calls
                }
            )

    return results