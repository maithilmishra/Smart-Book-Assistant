import faiss
import numpy as np


class VectorRetriever:
    def __init__(self):
        self.index = None
        self.chunks = []

    def build_index(self, embeddings):
        dimension = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings.astype(np.float32))

    def retrieve(self, query_embedding, k=3):
        distances, indices = self.index.search(query_embedding.astype(np.float32), k)
        return [self.chunks[i] for i in indices[0]]
