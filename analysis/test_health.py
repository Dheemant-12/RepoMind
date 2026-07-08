from analysis.health_analyzer import CodebaseHealthAnalyzer

analyzer = CodebaseHealthAnalyzer()

report = analyzer.analyze()

print("=" * 60)
print("REPOMIND CODEBASE HEALTH REPORT")
print("=" * 60)

for key, value in report.items():

    print(f"{key}: {value}")