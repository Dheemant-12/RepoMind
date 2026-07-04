from vector.semantic_search import semantic_search

query = input("Enter Search Query:\n")

results = semantic_search(query)

print("\n" + "=" * 60)

print("SEMANTIC SEARCH RESULTS")

print("=" * 60)

for index, result in enumerate(results, start=1):

    print(f"\nResult {index}")

    print("-" * 40)

    print("Function :", result["function"])

    print("File     :", result["file"])

    print("Distance :", result["distance"])

    print("\nSource Preview:\n")

    print(result["source"][:300])

    print("\n")