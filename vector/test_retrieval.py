from vector.retrieval_engine import RetrievalEngine

engine = RetrievalEngine()

print("=" * 60)
print("REPOMIND RETRIEVAL ENGINE")
print("=" * 60)

while True:

    query = input("\nAsk RepoMind (exit to quit): ")

    if query.lower() == "exit":
        break

    result = engine.retrieve(query)

    print()

    print(result)