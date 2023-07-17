from typing import List
from pydantic import BaseModel

class Enrollment(BaseModel):
    year: int
    term: int
    size: int

class Course(BaseModel):
    course: str
    Term: List[int]
    Year: int
    pastEnrollment: List[Enrollment]

class CourseEnrollment(BaseModel):
    data: List[Course]
