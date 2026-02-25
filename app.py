# import streamlit as st
# from services.rag_service import VectorStore
# from services.privacy_analyzer import analyze_privacy
# from services.document_loader import load_documents


# st.title("AI Privacy Compliance Agent")

# query = st.text_input("Enter your privacy question")

# if "vector_store" not in st.session_state:
#     st.session_state.vector_store = VectorStore()

# if st.button("Analyze"):

#     if query:

#         indices = st.session_state.vector_store.search(query)

#         docs = load_documents()

#         context = ""

#         for i in indices[0]:
#             context += docs[i] + "\n"

#         result = analyze_privacy(context, query)

#         st.write(result)

import streamlit as st
from services.llm_service import ask_llm
from services.rag_service import RAGService
from services.document_loader import load_pdf, load_docx, load_text
from utils.prompts import get_full_prompt

st.set_page_config(page_title="AI Privacy Compliance Agent")

st.title("AI Privacy Compliance Agent")

# initialize vector store
if "vector_store" not in st.session_state:
    st.session_state.vector_store = RAGService()

# chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

uploaded_text = ""

# file uploader
uploaded_file = st.file_uploader(
    "Attach company document",
    type=["pdf", "docx", "txt"]
)

if uploaded_file:

    if uploaded_file.type == "application/pdf":
        uploaded_text = load_pdf(uploaded_file)

    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        uploaded_text = load_docx(uploaded_file)

    else:
        uploaded_text = load_text(uploaded_file)

# show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# chat input
prompt = st.chat_input("Ask about privacy compliance...")

if prompt:

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # retrieve RAG context
    context_docs = st.session_state.vector_store.search(prompt)

    context = "\n".join(context_docs)

    # build full prompt
    full_prompt = get_full_prompt(context, uploaded_text, prompt)

    # call LLM
    response = ask_llm(full_prompt)

    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})