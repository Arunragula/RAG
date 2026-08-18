from loader import load_file
from chunking import create_chunks
from fastapi import FastAPI
from embeder import create_embeddings
from database import store_chunks
from query import search
import uvicorn 
FILE_PATH="/workspaces/RAG/Rag_mini/data/sample.txt"

app=FastAPI()
@app.get("/")
def get():
    return {"message": "RAG API is running"}

@app.get("/chunks")
def get_chunks():
    text = load_file(FILE_PATH)

    chunks = create_chunks(text)

    return {
        "total_chunks": len(chunks),
        "chunks": chunks
    }

@app.post("/ingest")
def store_embeds():
    text= load_file(FILE_PATH)
    chunks= create_chunks(text,chunk_size=500,chunk_overlap=50)
    embeddings= create_embeddings(chunks)

    store_chunks(
        chunks,
        embeddings
    )
    return {
        "message": "Document successfully ingested",
        "chunks": len(chunks),
        "embeddings": len(embeddings)
    }
@app.get("/search")
def search_doc(query:str):
    results = search(query, n_results=3)
    return {
        "documents": results["documents"],
        "distances": results["distances"],
        "ids": results["ids"]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

# def main():
#     text= load_file(FILE_PATH)
#     print("Total characters:", len(text))

#     chunks= create_chunks(
#         text,
#         chunk_size=500,
#         chunk_overlap=50
#     )

#     print("Total chunks:", len(chunks))

#     for i, chunk in enumerate(chunks):

#         print("\n" + "=" * 60)
#         print(f"CHUNK {i}")
#         print("=" * 60)

#         print(chunk)


# if __name__ == "__main__":
#     main()


