from embeder import model
from database import collection


def search(query: str, n_results: int = 3):

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    
    retrieved_docs = results["documents"][0]

    unique_docs = []

    for doc in retrieved_docs:
        if doc not in unique_docs:
            unique_docs.append(doc)
    unique_docs = unique_docs[:3]

    context = "\n\n".join(unique_docs)
    return context,unique_docs