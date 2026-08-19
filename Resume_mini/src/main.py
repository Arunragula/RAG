from fastapi import FastAPI
from chunking import create_chunks
from loader import load_pdf

import uvicorn

app=FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome To PDF Parser"
    }

FILE_PATH = "data/resume.pdf"
@app.get("/chunks")
def generate_chunks():
    pages=load_pdf(FILE_PATH)
    print("Total pages :",len(pages))

    chunks = create_chunks(text)

    print("Total chunks:", len(chunks))

    for i, chunk in enumerate(chunks):

        print("\n" + "=" * 60)
        print(f"CHUNK {i}")
        print(f"PAGE: {chunk['page']}")
        print("=" * 60)

        print(chunk["text"])
    
    return {
        "total_chunks": len(chunks),
        "chunks": chunks
    }