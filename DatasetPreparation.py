from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd
from tqdm.notebook import tqdm
import os.path
from config import DATA_DIR, TEXT_FIELD_NAME


csv_file_path = os.path.join(DATA_DIR, "./Data/RawData/steam.csv")

model = SentenceTransformer(
    "all-MiniLM-L6-v2", device="cpu"
)

def calculate_embeddings(texts):
    embeddings = model.encode(texts, show_progress_bar=False)
    return embeddings


df = pd.read_csv(csv_file_path)

# Handle missing or non-string values in the TEXT_FIELD_NAME column
df[TEXT_FIELD_NAME] = df[TEXT_FIELD_NAME].fillna('')  # Replace NaN with empty string
df[TEXT_FIELD_NAME] = df[TEXT_FIELD_NAME].astype(str)  # Ensure all values are strings

batch_size = 1000
num_chunks = len(df) // batch_size + 1

embeddings_list = []

for i in tqdm(range(num_chunks), desc="Calculating Embeddings"):
    start_idx = i * batch_size
    end_idx = (i + 1) * batch_size
    batch_texts = df[TEXT_FIELD_NAME].iloc[start_idx:end_idx].tolist()
    batch_embeddings = calculate_embeddings(batch_texts)
    embeddings_list.extend(batch_embeddings)

# Convert embeddings list to a numpy array
embeddings_array = np.array(embeddings_list)

np.save("steam.npy", embeddings_array)
