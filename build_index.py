from services.document_loader import load_documents
from langchain_openai import OpenAIEmbeddings
import faiss
import numpy as np
from config.settings import VECTOR_STORE_PATH
import os

# Load framework documents
documents = load_documents()

print("Loaded documents:", len(documents))

# Initialize embedding model
embeddings = OpenAIEmbeddings()

# Create embeddings
vectors = [embeddings.embed_query(doc) for doc in documents]

dimension = len(vectors[0])

# Create FAISS index
index = faiss.IndexFlatL2(dimension)

# Add vectors
index.add(np.array(vectors).astype("float32"))

# Ensure folder exists
os.makedirs("vector_store", exist_ok=True)

# Save index
faiss.write_index(index, VECTOR_STORE_PATH)

print("Vector database created successfully")