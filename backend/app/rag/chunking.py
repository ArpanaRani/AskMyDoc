from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_pages(pages, chunk_size=1000, chunk_overlap=200):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )

    documents = splitter.create_documents(
        texts=[page["text"] for page in pages],
        metadatas=[
            {"page_number": page["page_number"]}
            for page in pages
        ]
    )

    chunks = []

    for index, document in enumerate(documents):
        chunks.append({
            "chunk_index": index,
            "page_number": document.metadata["page_number"],
            "text": document.page_content
        })

    return chunks