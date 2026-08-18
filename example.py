from sentence_transformers import SentenceTransformer
import chromadb
import ollama 
model = SentenceTransformer('all-MiniLM-L6-v2')

client= chromadb.PersistentClient(path="./chroma.db")
collection = client.get_or_create_collection(name="resumes")

documents = [
    "FastAPI is a modern Python web framework used to build APIs.",
    "Docker packages applications together with their dependencies.",
    "ChromaDB is a vector database used for storing and searching embeddings.",
    "Sentence Transformers generate embeddings that capture semantic meaning.",
    "PostgreSQL is a relational database management system."
]


embedding = model.encode(documents).tolist()
collection.add(
    ids=['1','2','3','4','5'],
    documents=documents,
    embeddings=embedding
)

query = "How can I create a backend API?"

query_embedding= model.encode(query).tolist()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

# print(results.keys())
# print(results["documents"])

# print(results["ids"])
# print(results["distances"])

retrieved_docs = results["documents"][0]

context = "\n\n".join(retrieved_docs)

# print(context)

# prompt = f"""
# You are a helpful assistant.

# Answer the question using only the provided context.
# If the answer is not present in the context, say:
# "I don't know based on the provided documents."

# Context:
# {context}

# Question:
# {query}

# Answer:
# """

# response = ollama.chat(
#     model="qwen2.5:0.5b",
#     messages=[
#         {
#             "role": "user",
#             "content": prompt
#         }
#     ]
# )

# print(response["message"]["content"])