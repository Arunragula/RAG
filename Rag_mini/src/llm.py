import ollama


def generate_answer(query, context):

    prompt = f"""
You are a helpful assistant.

Answer the question using ONLY the provided context.

If the answer is not present in the context, say:
"I don't know based on the provided documents."

Context:
{context}

Question:
{query}

Answer:
"""

    response = ollama.chat(
        model="qwen2.5:0.5b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]