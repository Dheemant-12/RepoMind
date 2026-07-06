import json

import chromadb

from vector.embedding_model import get_embedding


from config.settings import CHROMA_DIR

client = chromadb.PersistentClient(
    path=str(CHROMA_DIR)
)
collection = client.get_or_create_collection(
    name="repomind"
)


def populate_vector_store():

    with open(
        "functions.json",
        encoding="utf-8"
    ) as f:

        functions = json.load(f)

    for index, function in enumerate(functions):

        embedding = get_embedding(
            function["source_code"]
        )

        collection.add(

            ids=[str(index)],

            embeddings=[embedding],

            documents=[
                function["source_code"]
            ],

            metadatas=[
                {
                    "name": function["name"],
                    "file_path": function["file_path"]
                }
            ]
        )

    return len(functions)