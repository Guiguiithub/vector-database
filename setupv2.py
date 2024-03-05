import os.path

import numpy as np
import pandas as pd
from qdrant_client import QdrantClient, models

from config import DATA_DIR, QDRANT_URL, COLLECTION_NAME, TEXT_FIELD_NAME, VECTOR_FIELD_NAME

# Define the CSV file path and NPY file path
csv_file_path = os.path.join(DATA_DIR, "./Data/RawData/steam.csv")
npy_file_path = os.path.join(DATA_DIR, "steam.npy")

client = QdrantClient(
    "localhost",
    port=6333
)

df = pd.read_csv(csv_file_path)

payload = df.to_dict('records')

vectors = np.load(npy_file_path)

client.recreate_collection(
    collection_name=COLLECTION_NAME,
    vectors_config={
        VECTOR_FIELD_NAME: models.VectorParams(
            size=vectors.shape[1],
            distance=models.Distance.COSINE,
            on_disk=True,
        )
    },
    # Quantization is optional, but it can significantly reduce the memory usage
    quantization_config=models.ScalarQuantization(
        scalar=models.ScalarQuantizationConfig(
            type=models.ScalarType.INT8,
            quantile=0.99,
            always_ram=True
        )
    )
)

# Create a payload index for text field.
# This index enables text search by the TEXT_FIELD_NAME field.
client.create_payload_index(
    collection_name=COLLECTION_NAME,
    field_name=TEXT_FIELD_NAME,
    field_schema=models.TextIndexParams(
        type=models.TextIndexType.TEXT,
        tokenizer=models.TokenizerType.WORD,
        min_token_len=2,
        max_token_len=20,
        lowercase=True,
    )
)

client.upload_collection(
    collection_name=COLLECTION_NAME,
    vectors={
        VECTOR_FIELD_NAME: vectors
    },
    payload=payload,
    ids=None,  # Vector ids will be assigned automatically
    batch_size=256  # How many vectors will be uploaded in a single request?
)

