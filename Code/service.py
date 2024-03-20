from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import NeuralSearcher

app = FastAPI()

# Create a neural searcher instance
neural_searcher = NeuralSearcher(collection_name="steamVideoGames")

# allow access
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
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type"],
)


@app.get("/api/search")
def search_startup(q: str):
    return {"result": neural_searcher.search(text=q)}


@app.get("/api/getall")
def all_startup():
    try:
        data = neural_searcher.get_all_data()
        return {"result": data}
    except Exception as e:
        return {"error": str(e)}

@app.post("/api/recommend")
def recommend(request: dict):
    try:
        liked_ids = request.get("likeIds", [])
        disliked_ids = request.get("dislikeIds", [])

        result = neural_searcher.recommend(positif=liked_ids, negitif=disliked_ids)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
