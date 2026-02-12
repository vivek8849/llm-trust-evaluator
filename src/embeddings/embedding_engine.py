from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


class EmbeddingEngine:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def encode(self, texts: list):
        return self.model.encode(texts)

    def compute_similarity_matrix(self, embeddings):
        return cosine_similarity(embeddings)
    # Embeddings capture semantic meaning, not surface form
    # use cosine similarity in embedding space

    def compute_consistency_score(self, similarity_matrix):
        """
        Compute average off-diagonal similarity.
        Higher = more consistent.
        """
        n = similarity_matrix.shape[0]

        # Remove diagonal (self-similarity)
        mask = ~np.eye(n, dtype=bool)
        values = similarity_matrix[mask]

        return np.mean(values)

# generate multiple responses, embed them using a sentence transformer, compute pairwise cosine similarity, and use the average semantic similarity as a consistency signal.
# High consistency = stable
# Low consistency = uncertain