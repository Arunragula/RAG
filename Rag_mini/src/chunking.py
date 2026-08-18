# def create_chunks(text, chunk_size=500, chunk_overlap=50):

#     chunks = []

#     start = 0

#     while start < len(text):

#         end = start + chunk_size

#         chunk = text[start:end]

#         chunks.append(chunk)

#         start = end - chunk_overlap

#     return chunks

import re


def split_paragraphs(text):
    paragraphs = re.split(r"\n\s*\n", text)

    return [
        paragraph.strip()
        for paragraph in paragraphs
        if paragraph.strip()
    ]
def split_sentences(text):
    sentences = re.split(r"(?<=[.!?])\s+", text)

    return [
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    ]

def create_chunks(
    text,
    chunk_size=500,
    chunk_overlap=1
):
    paragraphs = split_paragraphs(text)

    chunks = []
    current_sentences = []
    current_length = 0

    for paragraph in paragraphs:

        sentences = split_sentences(paragraph)

        for sentence in sentences:

            sentence_length = len(sentence)

            # If adding this sentence exceeds
            # the maximum chunk size
            if (
                current_length + sentence_length > chunk_size
                and current_sentences
            ):

                chunks.append(
                    " ".join(current_sentences)
                )

                # Keep last N sentences as overlap
                current_sentences = (
                    current_sentences[-chunk_overlap:]
                )

                current_length = sum(
                    len(s)
                    for s in current_sentences
                )

            current_sentences.append(sentence)

            current_length += sentence_length

    # Add remaining sentences
    if current_sentences:
        chunks.append(
            " ".join(current_sentences)
        )

    return chunks

# def create_chunks(
#     text,
#     chunk_size=500,
#     chunk_overlap=1
# ):
#     sentences = split_sentences(text)

#     chunks = []
#     current_chunk = []

#     current_length = 0

#     for sentence in sentences:

#         sentence_length = len(sentence)

#         if (
#             current_length + sentence_length > chunk_size
#             and current_chunk
#         ):
#             chunks.append(" ".join(current_chunk))

#             # Keep the last few sentences for overlap
#             current_chunk = current_chunk[-chunk_overlap:]

#             current_length = sum(
#                 len(s) for s in current_chunk
#             )

#         current_chunk.append(sentence)

#         current_length += sentence_length

#     if current_chunk:
#         chunks.append(" ".join(current_chunk))

#     return chunks