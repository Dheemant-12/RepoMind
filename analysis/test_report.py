from analysis.repository_report import RepositoryReport

report = RepositoryReport()

path = report.generate()

print("=" * 60)
print("REPOSITORY REPORT GENERATED")
print("=" * 60)

print(f"\nSaved to:\n{path}")