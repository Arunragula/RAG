import chromadb

client =  chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(
    name="documents"
)

def store_chunks(chunks, embeddings):
    ids = [str(i) for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )
#     results = collection.get(
#     include=["documents", "metadatas"]
# )

#     for i, doc in enumerate(results["documents"]):
#         print(f"\nID: {results['ids'][i]}")
#         print("\n", i, doc[:200])
#     print("Total documents:", collection.count())
    print(f"Stored {len(chunks)} chunks in ChromaDB")
