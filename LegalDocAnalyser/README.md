# 🧠 Legal Document AI Assistant (Gemini + FAISS + Streamlit)

This web app allows users to upload legal PDF documents and receive intelligent, context-aware assistance using Google Gemini's language models. It supports semantic search, question answering, and summarization using a Retrieval-Augmented Generation (RAG) pipeline.

---

## 🚀 Features

- 📤 Upload legal PDF documents (text-based only)
- 📄 Extract and preview PDF content
- 🧱 Chunk text and embed using Gemini embeddings
- 🔍 Semantic search with FAISS vector store
- ❓ Ask document-specific questions
- 📝 Generate concise summaries
- 🔐 Secure API key management via `.env`

---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/ashwinipatil-ap/genai-projects/LegalDocAnalyser.git
cd LegalDocAnalyser
```

### 2. Set up a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Key
`.env`  add your Gemini API key:


## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

---

## 💬 Sample Prompts

| Document Type      | Sample Prompt                                           |
|--------------------|--------------------------------------------------------|
| Service Agreement  | What are the terms for termination?                   |
| NDA                | What is the duration of the confidentiality obligation? |
| Licensing Contract | Summarize key obligations and payment structures.      |

---
## 🛡️ Notes

- Only text-based PDFs are supported (not scanned images).
- Your Gemini API key is kept secure via environment variables.
- FAISS is used locally; no cloud vector DB needed.


