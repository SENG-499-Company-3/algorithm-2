from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.data_model.course import Course
from app.data_model.prediction import Prediction
import re

from app.model.predict import perform_algorithm

router = APIRouter()

@router.post("/schedule/", response_model=list[Prediction], response_model_exclude_unset=True, tags=["Schedule"], status_code=200)
def predict_class_sizes(courses: list[Course]) -> list[Prediction]:
    """
    Predicts class sizes for courses based on past enrollment data.

    Returns:
        A list of dictionaries containing course information and predicted class sizes.
    """
    predictions = []
    considered_courses = [
        "CSC", 
        "ECE", 
        "SENG"
    ]
    term_dict = {
        1: "Spring", 
        5: "Summer", 
        9: "Fall"
    }

    for course in courses:
        # Filter out invalid courses forms
        if not re.match(r"[a-zA-Z]{3,4}\d{3}", course.course):
            return JSONResponse(content={"error": "Invalid course format, must be of form: [a-zA-z]{3,4}\d{3}"}, status_code=400)
        
        # Ensure incoming courses are in the correct format
        prefix = re.match(r"([a-zA-Z]+)", course.course).group(1)
        if prefix.upper() not in considered_courses:
            return JSONResponse(content={"error": "Invalid course prefix, must be one of: CSC, ECE, SENG"}, status_code=400)
        
        suffix = re.match(r"[a-zA-Z]+(\d+)", course.course).group(1)
        course_name = f"{prefix.upper()} {suffix}"

        # ECE 458 has been renamed to ECE 363
        if course_name == "ECE 363":
            course_name = "ECE 458"
        
        for term in course.Term:
            class_size = perform_algorithm(course_name, term_dict[term], course.Year)
            prediction = Prediction(course=course.course, term=term, size=class_size)
            predictions.append(prediction)
            
    json_compatible_item_data = jsonable_encoder(predictions)

    return JSONResponse(content=json_compatible_item_data)