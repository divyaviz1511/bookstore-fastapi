import joblib
import requests
from typing import List
from preprocessing.author_score import return_author_score
from schemas.PredictPriceSchema import BookFeatures, PricePredictionResponse
from schemas.PredictBookTrendSchema import BookForTrend
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

#Global cache for books and embeddings (in memory for now)
_cached = {
    "books": None,
    "embeddings": None
}

#Load Encoder
loaded_encoder = joblib.load('models/genre_encoder.pkl')

#Load the trained model
model = joblib.load("models/book_price_predictor_model.pkl")
best_seller_model = joblib.load("models/book_bestseller_predictor_model.pkl")
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

#Price Predict
def predict_price(features: BookFeatures):
    author_score = return_author_score(features.author)
    
    input = [
        features.pageCount,
        features.releasedYear,
        author_score
    ]
    
    predicted_price = model.predict([input])[0]
    return round(predicted_price, 2)

#Predict Best Seller with value
def predict_book_best_seller(books: List[BookForTrend]):
    book_list_prob = []
    for book in books:
	    prob = predict_prob_book(book)
	    book_list_prob.append(prob)
    return book_list_prob


def predict_prob_book(book: BookForTrend):
    author_score = return_author_score(book.author)
    encoded_genre = loaded_encoder.transform([[book.genre]])
    encoded_genre_flat = encoded_genre.flatten().tolist() 
    	
    input = [book.pageCount, book.releasedYear, author_score] + encoded_genre_flat
    
    predicted_bestseller_prob = best_seller_model.predict([input])[0]
    return predicted_bestseller_prob


#Semantic search
def semantic_search_books(queryString: str):
    _initialize_cache()
    
    query_string = queryString.query 
    
    # Convert query string to embedding
    query_embedding = embedding_model.encode([query_string], convert_to_numpy=True)
    
    similarities = cosine_similarity(query_embedding, _cached["embeddings"])
    top_indices = np.argsort(similarities[0])[::-1][:5]  # top 5 results
    top_books = [_cached["books"][i] for i in top_indices]
    
    # Convert to BookForTrend schema objects
    result = [BookForTrend(
        id=b['id'],
        title=b['title'],
        author=b['author'],
        genre=b['genre'],
        pageCount=b.get('pageCount', 0),
        language=b.get('language', ''),
        releasedYear=0
    ) for b in top_books]
    
    return result

#Fetching Books using Java API
def fetch_books_from_java():
    response_data = requests.get("http://localhost:8080/api/book_details")
    if response_data.status_code == 200:
        return response_data.json()
    else:
        raise Exception(f"Failed to fetch books: {response_data.status_code}")

def _initialize_cache():
    if _cached["books"] is None or _cached["embeddings"] is None:
        _cached["books"] = fetch_books_from_java()
        
        book_texts = [f"{b['title']} {b['author']} {b['genre']} {b['language']}" for b in _cached["books"]]
        _cached["embeddings"] = embedding_model.encode(book_texts, convert_to_numpy=True)
    
    