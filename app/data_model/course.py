from pydantic import BaseModel
from typing import List

class pastEnrollment(BaseModel):
    year:int
    term:int
    size:int

class Course(BaseModel):
    course: str
    Term: List[int] = []
    Year: int 
    pastEnrollment: list[pastEnrollment] | None

