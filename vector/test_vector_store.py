from vector.vector_store import populate_vector_store

count = populate_vector_store()

print("=" * 50)

print(
    f"Stored {count} functions in ChromaDB"
)

print("=" * 50)