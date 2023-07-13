from pydantic import BaseModel
from typing import List

class pastEnrol(BaseModel):
    year:int
    term:int
    size:int

class Course(BaseModel):
    course: str
    term: int
    prereq: List[str] = []
    coreq: List[str] = []
    pastEnrol: list[pastEnrol] | None = None