from typing import List
from qdrant_client import QdrantClient
from qdrant_client.http.models.models import Filter
from sentence_transformers import SentenceTransformer


class NeuralSearcher:

    def __init__(self, collection_name: str):
        self.collection_name = collection_name
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.qdrant_client = QdrantClient("localhost", port=6333)

    # search for similar games based on input
    def search(self, text: str, filter_: dict = None) -> List[dict]:
        vector = self.model.encode(text).tolist()
        hits = self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            query_filter=Filter(**filter_) if filter_ else None,
            limit=150,
        )

        seen_name = []
        results = []

        # verification of duplicate
        for hit in hits:
            name = hit.payload["name"]
            if name not in seen_name:
                result = hit.payload
                result['score'] = hit.score
                result['ident'] = hit.id
                results.append(result)
                seen_name.append(name)
        return results

    # get all data from database
    def get_all_data(self) -> List[dict]:
        # Use an empty string as the query to retrieve all documents
        return self.search(text="", filter_=None)

    def recommend(self, positif: list, negitif: list) -> List[dict]:
        hits = self.recommend(
            collection_name = self.collection_name,
            positive=positif,
            negative = negitif,
            limit=15
        )

        seen_name = []
        results = []

        for hit in hits:
            name = hit.payload["name"]
            if name not in seen_name:
                result = hit.payload
                result['score'] = hit.score
                result['ident'] = hit.id
                results.append(result)
                seen_name.append(name)
        return results