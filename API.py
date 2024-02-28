from typing import List

from qdrant_client import QdrantClient
from qdrant_client.http.models.models import Filter
from sentence_transformers import SentenceTransformer

from config import QDRANT_URL, VECTOR_FIELD_NAME


class NeuralSearcher:

    def __init__(self, collection_name: str):
        self.collection_name = collection_name
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.qdrant_client = QdrantClient("localhost", port=6333)

    def search(self, text: str, filter_: dict = None) -> List[dict]:
        vector = self.model.encode(text).tolist()
        hits = self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=(VECTOR_FIELD_NAME, vector),
            query_filter=Filter(**filter_) if filter_ else None,
            limit=5,
        )
        results =[]
        for hit in hits:
            result = hit.payload
            result['score'] = hit.score
            results.append(result)
        return results
