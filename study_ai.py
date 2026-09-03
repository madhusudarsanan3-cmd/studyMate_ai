import streamlit as st

from components.pdf_processor import extract_text_from_pdf
from components.text_splitter import split_documents
from components.embeddings import get_embeddings
from components.vector_store import create_vector_store


st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚"
)

st.title("📚 StudyMate AI")
st.subheader("AI-Powered Document Q&A Assistant")


uploaded_files = st.file_uploader(
    "Upload PDF documents",
    type=["pdf"],
    accept_multiple_files=True
)


if uploaded_files:

    all_chunks = []

    for pdf in uploaded_files:

        pages = extract_text_from_pdf(pdf)

        chunks = split_documents(pages)

        all_chunks.extend(chunks)

        st.success(
            f"{pdf.name} processed successfully!"
        )

    st.write(
        f"Total chunks created: {len(all_chunks)}"
    )

    with st.spinner("Creating knowledge base..."):

        embeddings = get_embeddings()

        vector_store = create_vector_store(
            all_chunks,
            embeddings
        )

        st.session_state.vector_store = vector_store

    st.success("✅ Knowledge base created!")

    if "vector_store" in st.session_state:
        question = st.text_input(
        "💬 Ask a question about your documents:"
        )
        if question:
            results = st.session_state.vector_store.similarity_search(
            question,
            k=4
            )
            st.subheader("🔎 Relevant Information")
            for result in results:
                st.write(result.page_content)
                st.caption(
                    f"Source: Page {result.metadata['page']}"
                    )