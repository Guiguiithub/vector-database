from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct
import json
import numpy as np

#Initialisation of the client
qdrant_client = QdrantClient("localhost", port=6333)

#Create a collection
qdrant_client.recreate_collection(
    collection_name="videoGames",
    vectors_config=VectorParams(size=384, distance=Distance.EUCLID),
)


fd = open("./steam.json")

payload = map(json.loads, fd)

vectors = np.load("./steam.npy")

qdrant_client.upload_collection(
    collection_name="videoGames",
    vectors=vectors,
    payload=payload,
)

"""
fd = open("./steam.json", encoding="utf-8")

data = map(json.loads, fd)
vectors = np.load("./steam.npy")

for game, vector in zip(data, vectors):
    qdrant_client.upsert(
        collection_name="videoGames",
        points=[
            PointStruct(
                id=game["appid"],
                vector=vector.tolist(),
                payload={
                    "name": game["name"],
                    "release_date": game["release_date"],
                    "developer": game["developer"],
                    "publisher": game["publisher"],
                    "platform": game["platform"],
                    "categories": game["categories"],
                    "genres": game["genres"]
                }
            )
        ]
    )
"""