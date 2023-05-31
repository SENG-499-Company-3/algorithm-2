from fastapi import APIRouter
from app.algorithm.predict import perform_algorithm

router = APIRouter()

@router.get("/")
def class_room(class_size: int = 1000):
    result = perform_algorithm(class_size)
    return {"result": result}