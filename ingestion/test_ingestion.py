from ingestion.clone_repo import clone_repository
from ingestion.file_scanner import scan_python_files
from ingestion.ast_parser import parse_python_file


def main():

    repo = input("Enter GitHub Repository URL:\n")

    repo_path = clone_repository(repo)

    files = scan_python_files(repo_path)

    print(f"\nFound {len(files)} Python files.\n")

    for file in files:
        parse_python_file(file)


if __name__ == "__main__":
    main()