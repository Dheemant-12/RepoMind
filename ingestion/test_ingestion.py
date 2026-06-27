from clone_repo import clone_repository
from file_scanner import scan_python_files


def main():

    repo = input("Enter GitHub Repository URL:\n")

    repo_path = clone_repository(repo)

    files = scan_python_files(repo_path)

    print("\nPython Files Found\n")

    print("=" * 40)

    for file in files:
        print(file)

    print("=" * 40)

    print(f"\nTotal Python Files: {len(files)}")


if __name__ == "__main__":
    main()