from fastapi import APIRouter
from app.algorithm.predict import perform_algorithm

router = APIRouter()

@router.get("/")
def class_room(semester: str) -> dict:
    """
    Get class size for each course for the the given semester.

    Parameters:
        - semester (str): The semester for which class information is requested. Can be "FALL", "SPRING", or "SUMMER".

    Returns:
        - dict: A dictionary containing the course, class size, and semester.
    """
    class_size = perform_algorithm(semester)
    return {
        "course": "csc 115",
        "size": class_size,
        "semester": semester
    }