import ast


def extract_imports(file_path: str):
    """
    Extract all imports from a Python file and build an import map.
    """

    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source)

    imports = []
    import_map = {}

    for node in ast.walk(tree):

        # import module
        if isinstance(node, ast.Import):

            for alias in node.names:

                imports.append({
                    "module": alias.name,
                    "name": None,
                    "alias": alias.asname
                })

                local_name = alias.asname if alias.asname else alias.name
                import_map[local_name] = alias.name

        # from module import object
        elif isinstance(node, ast.ImportFrom):

            module = node.module

            for alias in node.names:

                imports.append({
                    "module": module,
                    "name": alias.name,
                    "alias": alias.asname
                })

                local_name = alias.asname if alias.asname else alias.name

                import_map[local_name] = f"{module}.{alias.name}"

    return {
        "file_path": file_path,
        "imports": imports,
        "import_map": import_map
    }