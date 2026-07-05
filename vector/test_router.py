from vector.query_router import classify_query

print("=" * 50)
print("REPOMIND QUERY ROUTER")
print("=" * 50)

while True:

    query = input("\nAsk RepoMind (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    route = classify_query(query)

    print(f"\nSelected Route : {route}")