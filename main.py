from typing import List
from fastapi import FastAPI, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas.PredictPriceSchema import BookFeatures, PricePredictionResponse
from schemas.PredictBookTrendSchema import BookForTrend
from schemas.search import SearchQuery
import loadModels

import numpy as np

app = FastAPI()

#Enable CORS for react integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers= ["*"]
)

#End point
@app.post("/predict_price", response_model=PricePredictionResponse, status_code=status.HTTP_200_OK)
def predict_price_endpoint(features: BookFeatures): 
    try:  
        predicted_price = loadModels.predict_price(features)
        return PricePredictionResponse(suggested_price=round(predicted_price, 2))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")


#End point
@app.post("/predict_best_seller", response_model=List[float], status_code=status.HTTP_200_OK)
def predict_book_best_seller(books: List[BookForTrend]): 
    try:  
        return loadModels.predict_book_best_seller(books)
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

#End Point
@app.post("/semantic_search_books", response_model=List[BookForTrend], status_code=status.HTTP_200_OK)
def semantic_search(queryRequest: SearchQuery):
    try:
        return loadModels.semantic_search_books(queryRequest)
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Semantic search results failed: {str(e)}")