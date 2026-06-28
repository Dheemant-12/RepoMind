import ast


def parse_python_file(file_path: str):
    """
    Parse a Python file and print all classes and functions.
    """

    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source)

    print(f"\n📄 File: {file_path}")
    print("=" * 60)

    for node in ast.walk(tree):

        if isinstance(node, ast.ClassDef):
            print(f"🏛️  Class: {node.name}")

        elif isinstance(node, ast.FunctionDef):
            print(f"⚙️  Function: {node.name}")

        elif isinstance(node, ast.AsyncFunctionDef):
            print(f"⚡ Async Function: {node.name}")