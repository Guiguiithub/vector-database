from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd
from tqdm.notebook import tqdm

model = SentenceTransformer(
    "all-MiniLM-L6-v2", device="cpu"
)

df = pd.read_json("./steam.json", orient="records")

vectors = model.encode(
    [row.name for row in df.itertuples()],
    show_progress_bar=True
)

print(vectors.shape)

np.save("steam.npy", vectors, allow_pickle=False)