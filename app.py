
import streamlit as st
import pandas as pd
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA

# -------------------- Streamlit UI --------------------
st.set_page_config(page_title="🛍️ Product Info Assistant", layout="centered")
st.title("🛍️ Product Info Assistant (CSV Upload)")

st.write("📂 Upload a CSV file with columns: **name, description**")

uploaded_file = st.file_uploader("Upload your product CSV", type=["csv"])

if uploaded_file:
    # Load CSV
    df = pd.read_csv(uploaded_file)

    # Show preview
    st.subheader("📋 Product List")
    st.dataframe(df)

    # Convert to LangChain documents
    docs = [Document(page_content=row["description"], metadata={"name": row["name"]}) for _, row in df.iterrows()]

    # Embeddings + Vector DB
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = Chroma.from_documents(docs, embeddings)

    # Hugging Face model
    hf_pipeline = pipeline("text2text-generation", model="google/flan-t5-small", max_new_tokens=200)
    llm = HuggingFacePipeline(pipeline=hf_pipeline)

    # RAG chain
    retriever = db.as_retriever()
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    # Ask questions
    query = st.text_input("💬 Your Question:")
    if query:
        with st.spinner("Thinking..."):
            answer = qa.run(query)
        st.success(answer)
else:
    st.info("👆 Please upload a CSV file to start.")

