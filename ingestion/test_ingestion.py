import json

from ingestion.clone_repo import clone_repository
from ingestion.file_scanner import scan_python_files
from ingestion.function_extractor import extract_functions


def main():

    repo = input("Enter GitHub Repository URL:\n")

    repo_path = clone_repository(repo)

    python_files = scan_python_files(repo_path)

    all_functions = []

    for file in python_files:

        functions = extract_functions(file)

        all_functions.extend(functions)

    with open("functions.json", "w", encoding="utf-8") as f:
        json.dump(all_functions, f, indent=4)

    print(f"\n✅ Extracted {len(all_functions)} functions")
    print("✅ Saved to functions.json")


if __name__ == "__main__":
    main()