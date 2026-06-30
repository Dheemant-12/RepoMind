import ast


def extract_classes(file_path: str):
    """
    Extract all classes from a Python file.
    """

    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source)

    classes = []

    for node in ast.walk(tree):

        if isinstance(node, ast.ClassDef):

            bases = []

            for base in node.bases:

                if isinstance(base, ast.Name):
                    bases.append(base.id)

                elif isinstance(base, ast.Attribute):
                    bases.append(base.attr)

                else:
                    bases.append(ast.dump(base))

            methods = []

            for item in node.body:

                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    methods.append(item.name)

            classes.append({
                "name": node.name,
                "file_path": file_path,
                "base_classes": bases,
                "methods": methods
            })

    return classes