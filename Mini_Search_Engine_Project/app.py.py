
import streamlit as st
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec
from PyPDF2 import PdfReader
import os

# -------------------- API KEYS --------------------
PINECONE_API_KEY = "YOUR_PINECONE_API_KEY"
INDEX_NAME = "mini-search-engine"

# -------------------- PINECONE --------------------
pc = Pinecone(api_key=PINECONE_API_KEY)

if INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        name=INDEX_NAME,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

index = pc.Index(INDEX_NAME)

# -------------------- MODEL --------------------
model = SentenceTransformer("all-MiniLM-L6-v2")

# -------------------- STREAMLIT UI --------------------
st.title("Mini Search Engine")
st.write("Upload PDFs and search semantically")

uploaded_files = st.file_uploader(
    "Upload PDF Files",
    type=["pdf"],
    accept_multiple_files=True
)

def extract_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def split_text(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

# -------------------- UPLOAD PROCESS --------------------
if uploaded_files:
    for file in uploaded_files:
        text = extract_text(file)
        chunks = split_text(text)

        for i, chunk in enumerate(chunks):
            embedding = model.encode(chunk).tolist()

            index.upsert([
                (
                    f"{file.name}-{i}",
                    embedding,
                    {
                        "text": chunk,
                        "document": file.name
                    }
                )
            ])

    st.success("PDFs uploaded and indexed successfully!")

# -------------------- SEARCH --------------------
query = st.text_input("Enter your search query")

if st.button("Search"):
    query_embedding = model.encode(query).tolist()

    results = index.query(
        vector=query_embedding,
        top_k=5,
        include_metadata=True
    )

    st.subheader("Results")

    for match in results["matches"]:
        st.write("Document:", match["metadata"]["document"])
        st.write("Similarity Score:", round(match["score"], 3))
        st.write(match["metadata"]["text"])
        st.write("---")
