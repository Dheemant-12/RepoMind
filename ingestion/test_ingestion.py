import json

from ingestion.clone_repo import clone_repository
from ingestion.file_scanner import scan_python_files
from ingestion.import_extractor import extract_imports


def main():

    repo = input("Enter GitHub Repository URL:\n")

    repo_path = clone_repository(repo)

    python_files = scan_python_files(repo_path)

    all_imports = []

    for file in python_files:
        all_imports.append(extract_imports(file))

    with open("imports.json", "w", encoding="utf-8") as f:
        json.dump(all_imports, f, indent=4)

    print(f"\n✅ Processed {len(all_imports)} Python files")
    print("✅ Saved imports.json")


if __name__ == "__main__":
    main()