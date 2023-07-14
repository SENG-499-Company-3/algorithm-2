from pydantic import BaseModel
from typing import List

class Prediction(BaseModel):
    course:str
    term:int
    size:int
    constraints: List[str] = []