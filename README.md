
# 📚 StudyMate AI

### AI-Powered Document Question Answering Assistant

StudyMate AI is a **Generative AI-powered document question-answering application** that allows students to upload PDF study materials and ask questions using natural language.

Instead of manually searching through lengthy documents, users can simply ask a question and receive an AI-generated answer based on the information available in their uploaded documents.

The project uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant document content before generating an answer.

---

## 🚀 Features

* 📄 Upload one or multiple PDF documents
* 💬 Ask questions using natural language
* 🔎 Semantic document search
* 🧠 Retrieval-Augmented Generation (RAG)
* 🤖 AI-powered answer generation
* 📑 Source/page references for answers
* 🎓 Designed for students and educational materials
* 🛡️ Reduces hallucination by grounding responses in uploaded documents
* 🌐 Simple and interactive Streamlit interface

---

## 🏗️ System Architecture

```text
                    ┌───────────────────┐
                    │    PDF Upload     │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │  Text Extraction  │
                    │      (PyPDF)      │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │   Text Chunking   │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │    Embeddings     │
                    │   HuggingFace     │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │   FAISS Vector    │
                    │      Store        │
                    └─────────┬─────────┘
                              │
                              │
             ┌────────────────┘
             │
             ▼
    ┌────────────────────┐
    │   User Question    │
    └─────────┬──────────┘
              │
              ▼
    ┌────────────────────┐
    │ Semantic Retrieval │
    └─────────┬──────────┘
              │
              ▼
    ┌────────────────────┐
    │ Relevant Document  │
    │      Chunks        │
    └─────────┬──────────┘
              │
              ▼
    ┌────────────────────┐
    │        LLM         │
    │ Answer Generation  │
    └─────────┬──────────┘
              │
              ▼
    ┌────────────────────┐
    │   Final Answer +   │
    │   Source Citation  │
    └────────────────────┘
```

---

## 🧠 How It Works

StudyMate AI follows a **Retrieval-Augmented Generation (RAG)** pipeline.

### 1. Upload Documents

The user uploads one or more PDF files containing study materials.

### 2. Extract Text

Text is extracted from the uploaded PDFs using PyPDF.

### 3. Split Documents

The extracted text is divided into smaller chunks so that relevant sections can be efficiently retrieved.

### 4. Generate Embeddings

Each text chunk is converted into a numerical vector using a HuggingFace embedding model.

### 5. Store in FAISS

The generated embeddings are stored in a FAISS vector index for fast similarity-based searching.

### 6. Ask a Question

The user enters a question in natural language.

### 7. Retrieve Relevant Content

The question is converted into an embedding and compared against the document embeddings.

The most relevant document chunks are retrieved.

### 8. Generate Answer

The retrieved context is provided to the LLM, which generates a natural-language answer.

### 9. Display Sources

The application can display the relevant document and page information so the user can verify the answer.

---

## 🛠️ Tech Stack

| Technology    | Purpose                                |
| ------------- | -------------------------------------- |
| Python        | Core programming language              |
| Streamlit     | Web application interface              |
| LangChain     | RAG pipeline and component integration |
| PyPDF         | PDF text extraction                    |
| HuggingFace   | Text embeddings                        |
| FAISS         | Vector similarity search               |
| LLM           | Natural-language answer generation     |
| python-dotenv | Environment variable management        |

---

## 📁 Project Structure

```text
StudyMate-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── .gitignore
│
├── data/
│   └── sample_documents/
│
├── src/
│   ├── pdf_processor.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   └── llm.py
│
└── assets/
    └── screenshots/
```

> The exact file structure can be modified depending on the final implementation.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/StudyMate-AI.git
cd StudyMate-AI
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
LLM_API_KEY=your_api_key_here
```

Replace the value with the API key required by the LLM provider used in your implementation.

**Never commit API keys or other secrets to GitHub.**

---

## ▶️ Running the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💡 Example Usage

### Step 1 — Upload PDF

Upload your study material, for example:

```text
DBMS_Notes.pdf
Operating_Systems.pdf
Computer_Networks.pdf
```

### Step 2 — Ask a Question

Example:

```text
What is a primary key?
```

### Step 3 — Receive the Answer

Example output:

```text
A primary key is a field or combination of fields
that uniquely identifies each record in a database table.
```

### Step 4 — Verify the Source

```text
Source: DBMS_Notes.pdf
Page: 12
```

---

## 🧪 Sample Test Cases

| Test Case | User Input                       | Expected Result                                                                 |
| --------- | -------------------------------- | ------------------------------------------------------------------------------- |
| TC01      | What is a primary key?           | Definition retrieved from the PDF                                               |
| TC02      | Explain normalization.           | Relevant explanation from the document                                          |
| TC03      | What are the advantages of DBMS? | List of advantages from the PDF                                                 |
| TC04      | What is blockchain?              | Response indicating information was not found if absent from uploaded documents |

---

## 📊 Advantages

* ⚡ Saves time when studying lengthy documents
* 🔎 Uses semantic rather than simple keyword search
* 💬 Provides an easy conversational interface
* 📚 Supports multiple documents
* 🤖 Uses Generative AI for natural-language responses
* 📑 Provides document/page references
* 🎓 Useful for students and educational content
* 🧠 Demonstrates a practical RAG-based GenAI application

---

## ⚠️ Limitations

* Answer quality depends on the quality of the uploaded documents.
* Scanned PDFs may require OCR.
* Complex tables and images may not be extracted correctly.
* Cloud-based LLMs may require an API key and internet connection.
* Large documents may require additional optimization.
* AI-generated answers should still be verified against the original source.

---

## 🔮 Future Enhancements

* 🎤 Voice-based questions and answers
* 🌐 Multilingual document Q&A
* 🖼️ OCR support for scanned PDFs
* 📝 Automatic document summarization
* ❓ AI-generated quizzes and MCQs
* 📊 Answer confidence scoring
* 🧠 Improved conversation memory
* ☁️ Cloud deployment
* 👥 User accounts and document management
* 📈 Learning progress and analytics

---

## 🎯 Project Objective

The objective of StudyMate AI is to demonstrate how **Generative AI, embeddings, vector databases and Retrieval-Augmented Generation** can be combined to create a practical educational application.

The system transforms static PDF study materials into an **interactive AI-powered learning assistant**.

---

## 📄 License

This project is developed for **educational and academic purposes**.

---

## ⭐ Acknowledgement

This project was developed as part of a **Generative AI / Large Language Model application project** to demonstrate the practical use of RAG, embeddings, vector search and LLM-based question answering.

---

### 📌 Project Summary

**StudyMate AI = PDF Documents + Embeddings + FAISS + RAG + LLM + Streamlit**

> **Ask your documents. Learn faster.**
