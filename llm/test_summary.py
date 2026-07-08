from llm.repository_summary import RepositorySummarizer

summarizer = RepositorySummarizer()

print("=" * 60)
print("REPOMIND REPOSITORY SUMMARY")
print("=" * 60)

summary = summarizer.summarize()

print()

print(summary)