from analysis.repository_metrics import RepositoryMetrics

metrics = RepositoryMetrics().calculate()

print("=" * 60)
print("REPOMIND METRICS DASHBOARD")
print("=" * 60)

for key, value in metrics.items():
    print(f"{key}: {value}")