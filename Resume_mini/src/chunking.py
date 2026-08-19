import re

def split_sentences(text):
    """
    Split text into sentences.
    """
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    return [
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    ]


def create_chunks(
    pages,
    chunk_size=500,
    chunk_overlap=50
):
    chunks = []

    for page in pages:

        page_text = page["text"]
        page_number = page["page"]

        # First separate paragraphs
        paragraphs = re.split(r'\n\s*\n', page_text)

        current_chunk = ""

        for paragraph in paragraphs:

            paragraph = paragraph.strip()

            if not paragraph:
                continue

            sentences = split_sentences(paragraph)

            for sentence in sentences:

                # If adding this sentence is still within the limit
                if len(current_chunk) + len(sentence) + 1 <= chunk_size:

                    if current_chunk:
                        current_chunk += " " + sentence
                    else:
                        current_chunk = sentence

                else:
                    # Store current chunk
                    if current_chunk:
                        chunks.append({
                            "text": current_chunk,
                            "page": page_number
                        })

                    # Start new chunk
                    current_chunk = sentence

            # If paragraph itself is finished,
            # we prefer to keep paragraph boundaries.
            if current_chunk:
                chunks.append({
                    "text": current_chunk,
                    "page": page_number
                })

                current_chunk = ""

    return chunks