from embeder import model
from database import collection


def search(query: str, n_results: int = 3):

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results