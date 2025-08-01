from langchain_google_genai import ChatGoogleGenerativeAI

def answer_question(question, db, api_key):
    retrieved_docs = db.similarity_search(question, k=5)
    context = "\n".join([doc.page_content for doc in retrieved_docs])
    prompt = f"""You are a legal assistant. Use the context below to answer the question.

Context:
{context}

Question: {question}
Answer:"""
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)
    return llm.invoke(prompt)
