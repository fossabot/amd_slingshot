import os
import faiss
import numpy as np
from langchain_openai import OpenAIEmbeddings
from config.settings import VECTOR_STORE_PATH, OPENAI_API_KEY


# set environment variable for OpenAI
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY


class RAGService:

    def __init__(self):

        # embeddings model
        self.embeddings = OpenAIEmbeddings()

        # load FAISS index
        self.index = faiss.read_index(VECTOR_STORE_PATH)

        # load documents used for vector creation
        from services.document_loader import load_documents
        self.documents = load_documents()

    def search(self, query, k=3):

        # convert query to embedding
        q = self.embeddings.embed_query(query)

        q = np.array([q]).astype("float32")

        # search vector db
        distances, indices = self.index.search(q, k)

        results = []

        for i in indices[0]:
            if i < len(self.documents):
                results.append(self.documents[i])

        return "\n".join(results)