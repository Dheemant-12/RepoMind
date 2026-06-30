import json

from ingestion.clone_repo import clone_repository
from ingestion.file_scanner import scan_python_files
from ingestion.function_extractor import extract_functions
from ingestion.class_extractor import extract_classes


def main():

    repo = input("Enter GitHub Repository URL:\n")

    repo_path = clone_repository(repo)

    python_files = scan_python_files(repo_path)

    all_functions = []
    all_classes = []

    for file in python_files:

        all_functions.extend(extract_functions(file))
        all_classes.extend(extract_classes(file))

    with open("functions.json", "w", encoding="utf-8") as f:
        json.dump(all_functions, f, indent=4)

    with open("classes.json", "w", encoding="utf-8") as f:
        json.dump(all_classes, f, indent=4)

    print(f"\n✅ Functions Extracted : {len(all_functions)}")
    print(f"✅ Classes Extracted  : {len(all_classes)}")
    print("\nSaved:")
    print(" • functions.json")
    print(" • classes.json")


if __name__ == "__main__":
    main()