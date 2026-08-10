import chromadb
from sentence_transformers import SentenceTransformer
import warnings
warnings.filterwarnings("ignore",message=".*HF Hub.*")
model = SentenceTransformer('all-MiniLM-L6-v2')
client=chromadb.PersistentClient(path="./chroma_db")
sen="FastApi is python framerwork"
collection= client.get_or_create_collection(name='my_collection')
documents = [
    "FastAPI is a Python web framework.",
    "Python is a programming language.",
    "Docker helps package applications."
]

embedd= model.encode(documents).tolist()
collection.add(
    documents=documents,
    embeddings=embedd,
    ids=["1", "2", "3"]
)

print(collection.count())

result = collection.get(include=["documents", "embeddings"])

# print(result["documents"][1])
# print(result["embeddings"][1][:10])
query="How do I build APIs?"
query_embedding = model.encode(query).tolist()
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2,
    include=["documents", "embeddings"]
)

print(results)
