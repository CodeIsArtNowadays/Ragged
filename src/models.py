import numpy as np
from loguru import logger
from sentence_transformers import SentenceTransformer

from src.calculations import bm25, cos_sim, min_max_norm

semantic_model = SentenceTransformer("all-MiniLM-L6-v2")


class Chunk:
    def __init__(self, id: int, chunk: str, metadata=None):
        self.id = id
        self.chunk = chunk
        self.vec = semantic_model.encode(chunk)
        self.metadata = metadata

    def __str__(self):
        return self.chunk


class Index:
    def __init__(self, text=None):
        self.chunks = []

        if text:
            raw_chunks = self._chunking_text(text)
            for i, raw_chunk in enumerate(raw_chunks):
                self.chunks.append(Chunk(i, raw_chunk))

    def _chunking_text(self, text, size: int = 300, overlap: int = 50):
        res = []

        step = size - overlap

        for i in range(0, len(text), step):
            res.append(text[i : i + size])

        return res

    def _cosine_similarity_rate(self, query_vector):
        res = {}
        for chunk in self.chunks:
            res[chunk.id] = cos_sim(query_vector, chunk.vec)

        return res

    def _bm25_similarity_rate(self, query):
        return bm25(query, self.chunks)

    def cossim_search(self, query, k=3):
        query_vector = semantic_model.encode(query)
        scores = self._cosine_similarity_rate(query_vector)
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return sorted_scores[:k]

    def bm25_search(self, query, k=3):
        scores_ = self._bm25_similarity_rate(query)
        sorted_scores = sorted(scores_.items(), key=lambda x: x[1], reverse=True)
        return sorted_scores[:k]

    def hybrid_search(self, query, k=3):

        query_vector = semantic_model.encode(query)
        cos_sim_scores = self._cosine_similarity_rate(query_vector)
        bm25_scores = self._bm25_similarity_rate(query)

        logger.warning(cos_sim_scores)
        logger.warning(bm25_scores)

        cs_scores_raw = np.array([*cos_sim_scores.values()])
        bm25_scores_raw = np.array([*bm25_scores.values()])

        cs_scores_normalized = min_max_norm(cs_scores_raw)
        bm25_score_normilized = min_max_norm(bm25_scores_raw)

        hybrid_score = cs_scores_normalized * 0.5 + bm25_score_normilized * 0.5

        res = list(zip([i for i in range(len(hybrid_score))], hybrid_score))

        res.sort(key=lambda x: x[1], reverse=True)
        return res[:k]
