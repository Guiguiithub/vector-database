from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# The file where NeuralSearcher is stored
from API import NeuralSearcher

app = FastAPI()

# Create a neural searcher instance
neural_searcher = NeuralSearcher(collection_name="videoGames")

origins = [
    "http://localhost:63342",
    "https://localhost:63342",
    "http://127.0.0.1:63342",
    "https://127.0.0.1:63342",
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["Content-Type"],
)

@app.get("/api/search")
def search_startup(q: str):
    return {"result": neural_searcher.search(text=q)}

@app.get("/api/all")
def all_startup():
    return {"result": neural_searcher.get_all_data()}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
