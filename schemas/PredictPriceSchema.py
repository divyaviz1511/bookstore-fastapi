from pydantic import BaseModel

#Request model
class BookFeatures(BaseModel):
    pageCount : int
    releasedYear : int
    author : str

#Response model
class PricePredictionResponse(BaseModel):
    suggested_price: float
