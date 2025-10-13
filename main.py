from fastapi import FastAPI, status
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import joblib
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

#Load the trained model
model = joblib.load("book_price_predictor_model.pkl")

# Author popularity mapping
author_score_map = {
    "JK Rowling": 10,
    "Dan Brown": 8,
    "Stephenie Meyer": 7
}

#Request model
class BookFeatures(BaseModel):
    pageCount : int
    releasedYear : int
    author : str

#Response model
class PricePredictionResponse(BaseModel):
    suggested_price: float

#End point
@app.post("/predict_price", response_model=PricePredictionResponse, status_code=status.HTTP_200_OK)
def predict_price(features: BookFeatures):
    author_score = author_score_map.get(features.author, 5)
    
    input = [
        features.pageCount,
        features.releasedYear,
        author_score
    ]
    
    predicted_price = model.predict([input])[0]
    return PricePredictionResponse(suggested_price=round(predicted_price, 2))
