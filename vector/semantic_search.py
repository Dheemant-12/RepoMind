import chromadb

from vector.embedding_model import get_embedding

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection("repomind")


def semantic_search(query, top_k=5):

    query_embedding = get_embedding(query)

    results = collection.query(

        query_embeddings=[query_embedding],

        n_results=top_k
    )

    output = []

    documents = results["documents"][0]
    metadata = results["metadatas"][0]
    distances = results["distances"][0]

    for doc, meta, distance in zip(
        documents,
        metadata,
        distances
    ):

        output.append({

            "function": meta["name"],

            "file": meta["file_path"],

            "distance": round(distance, 4),

            "source": doc
        })

    return output