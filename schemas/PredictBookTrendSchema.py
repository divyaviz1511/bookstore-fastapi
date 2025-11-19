from pydantic import BaseModel
from typing import List
from datetime import date

class BookForTrend(BaseModel):
    id:int
    title: str
    author: str
    genre: str
    pageCount: int
    language: str
    releasedYear: int