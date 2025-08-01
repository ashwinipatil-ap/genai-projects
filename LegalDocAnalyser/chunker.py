from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_text(text):
    if not text:
        return []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    return splitter.split_text(text)
