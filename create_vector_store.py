from services.document_loader import load_documents
from langchain_openai import OpenAIEmbeddings
import faiss
import numpy as np
from config.settings import VECTOR_STORE_PATH


documents = load_documents()

embeddings = OpenAIEmbeddings()

vectors = [embeddings.embed_query(doc) for doc in documents]

dimension = len(vectors[0])

index = faiss.IndexFlatL2(dimension)

index.add(np.array(vectors).astype("float32"))

faiss.write_index(index, VECTOR_STORE_PATH)

print("Vector database created")