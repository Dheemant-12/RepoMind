import json

from ingestion.clone_repo import clone_repository
from ingestion.file_scanner import scan_python_files

from ingestion.function_extractor import extract_functions
from ingestion.class_extractor import extract_classes
from ingestion.import_extractor import extract_imports
from ingestion.call_extractor import extract_calls


def main():

    repo = input("Enter GitHub Repository URL:\n")

    repo_path = clone_repository(repo)

    python_files = scan_python_files(repo_path)

    functions = []
    classes = []
    imports = []
    calls = []

    for file in python_files:

        functions.extend(extract_functions(file))
        classes.extend(extract_classes(file))
        imports.append(extract_imports(file))
        calls.extend(extract_calls(file))

    with open("functions.json", "w", encoding="utf-8") as f:
        json.dump(functions, f, indent=4)

    with open("classes.json", "w", encoding="utf-8") as f:
        json.dump(classes, f, indent=4)

    with open("imports.json", "w", encoding="utf-8") as f:
        json.dump(imports, f, indent=4)

    with open("calls.json", "w", encoding="utf-8") as f:
        json.dump(calls, f, indent=4)

    combined = {
        "functions": functions,
        "classes": classes,
        "imports": imports,
        "calls": calls
    }

    with open("week1_output.json", "w", encoding="utf-8") as f:
        json.dump(combined, f, indent=4)

    print("\n========== WEEK 1 SUMMARY ==========")
    print(f"Functions : {len(functions)}")
    print(f"Classes   : {len(classes)}")
    print(f"Imports   : {len(imports)}")
    print(f"Calls     : {len(calls)}")

    print("\nGenerated Files:")
    print("✓ functions.json")
    print("✓ classes.json")
    print("✓ imports.json")
    print("✓ calls.json")
    print("✓ week1_output.json")


if __name__ == "__main__":
    main()