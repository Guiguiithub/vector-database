import pandas as pd
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
    ids=None,  # Vector ids will be assigned automatically
    batch_size=256,  # How many vectors will be uploaded in a single request?
)
