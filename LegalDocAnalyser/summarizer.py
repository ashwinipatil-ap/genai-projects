from langchain_google_genai import ChatGoogleGenerativeAI

def summarize_text(chunks, api_key):
    # Use only the first few chunks to stay under token limits
    content = "\n\n".join(chunks[:5])

    # Better-formatted prompt
    prompt = (
        "You are a legal assistant. Summarize the following legal text.\n"
        "Focus on:\n"
        "- Obligations\n"
        "- Rights\n"
        "- Key dates\n"
        "- Payment terms\n\n"
        f"{content}"
    )

    # Initialize the Gemini model
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=api_key
    )

    # Call the model and return the result
    try:
        response = llm.invoke(prompt)
        return response.content if hasattr(response, "content") else response
    except Exception as e:
        return f"Error during summarization: {str(e)}"