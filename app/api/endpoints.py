from fastapi import APIRouter, Body
from app.data_model.course import Course

from app.model.predict import perform_algorithm

router = APIRouter()

@router.post("/schedule/", response_model=list, response_model_exclude_unset=True, tags=["Schedule"])
def predict_class_sizes(courses: list[Course]) -> list:
    """
    Predicts class sizes for courses based on past enrollment data.

    Returns:
        A list of dictionaries containing course information and predicted class sizes.
    """
    predictions = []
    term_dict = {"Spring":1,"Summer":5,"Fall":9}
    for course in courses:
        if course.course == "ECE 363":
            course.course = "ECE 458"
        class_size = perform_algorithm(course.course,term_dict[course.term])
        predictions.append({course.course:class_size})

    
    # perform_algorithm()
    return mock_data

# Example value
example_value = [
    {
        "course": "CSC 111",
        "prereq": [],
        "coreq": [],
        "pastEnrol": [
            {
                "year": 2022,
                "term": "Fall",
                "size": 292
            }
        ]
    }
]

predict_class_sizes.examples = [
    {
        "summary": "Example Request",
        "value": example_value
    }
]

# Mock data provided
mock_data = [
    {
        "course": "CSC 111",
        "prereq": [],
        "coreq": [],
        "pastEnrol": [
            {"year": 2022, "term": "Fall", "size": 292}
        ]
    },
    {
        "course": "CSC 115",
        "prereq": [],
        "coreq": [],
        "pastEnrol": [
            {"year": 2022, "term": "Fall", "size": 159},
            {"year": 2022, "term": "Summer", "size": 91}
        ]
    },
    {
        "course": "CSC 225",
        "prereq": [],
        "coreq": [],
        "pastEnrol": [
            {"year": 2022, "term": "Fall", "size": 197},
            {"year": 2022, "term": "Summer", "size": 58}
        ]
    },
    {
        "course": "CSC 226",
        "prereq": [],
        "coreq": [],
        "pastEnrol": [
            {"year": 2022, "term": "Fall", "size": 96},
            {"year": 2022, "term": "Summer", "size": 74}
        ]
    },
    {
        "course": "CSC 230",
        "prereq": [],
        "coreq": [],
        "pastEnrol": [
            {"year": 2022, "term": "Fall", "size": 128},
            {"year": 2022, "term": "Summer", "size": 46}
        ]
    },
    {
        "course": "CSC 320",
        "prereq": [],
        "coreq": [],
        "pastEnrol": [
            {"year": 2022, "term": "Fall", "size": 47},
            {"year": 2022, "term": "Summer", "size": 120}
        ]
    },
    {
        "course": "CSC 355",
        "prereq": [],
        "coreq": [],
        "pastEnrol": [
            {"year": 2022, "term": "Fall", "size": 110}
        ]
    },
    {
        "course": "CSC 360",
        "prereq": [],
        "coreq": [],
        "pastEnrol": [
            {"year": 2022, "term": "Fall", "size": 144},
            {"year": 2022, "term": "Summer", "size": 69}
        ]
    },
    {
        "course": "CSC 361",
        "prereq": [],
        "coreq": [],
        "pastEnrol": [
            {"year": 2022, "term": "Fall", "size": 71}
        ]
    },
    {
        "course": "CSC 370",
        "prereq": [],
        "coreq": [],
        "pastEnrol": [
            {"year": 2022, "term": "Fall", "size": 157},
            {"year": 2022, "term": "Summer", "size": 85}
        ]
    },
    {
        "course": "ECE 255",
        "prereq": [],
        "coreq": [],
        "pastEnrol": [
            {"year": 2022, "term": "Fall", "size": 127}
        ]
    },
    {
        "course": "ECE 260",
        "prereq": [],
        "coreq": [],
        "pastEnrol": [
            {"year": 2022, "term": "Fall", "size": 117},
            {"year": 2022, "term": "Summer", "size": 68}
        ]
    },
    {
        "course": "ECE 310",
        "prereq": [],
        "coreq": [],
        "pastEnrol": [
            {"year": 2022, "term": "Summer", "size": 26}
        ]
    },
    {
        "course": "ECE 355",
        "prereq": [],
        "coreq": [],
        "pastEnrol": [
            {"year": 2022, "term": "Fall", "size": 145}
        ]
    },
    {
        "course": "ECE 360",
        "prereq": [],
        "coreq": [],
        "pastEnrol": [
            {"year": 2022, "term": "Fall", "size": 78}
        ]
    },
    {
        "course": "SENG 265",
        "prereq": [],
        "coreq": [],
        "pastEnrol": [
            {"year": 2022, "term": "Fall", "size": 198},
            {"year": 2022, "term": "Summer", "size": 67}
        ]
    },
    {
        "course": "SENG 275",
        "prereq": [],
        "coreq": [],
        "pastEnrol": [
            {"year": 2022, "term": "Summer", "size": 35}
        ]
    },
    {
        "course": "SENG 310",
        "prereq": [],
        "coreq": [],
        "pastEnrol": [
            {"year": 2022, "term": "Fall", "size": 76},
            {"year": 2022, "term": "Summer", "size": 121}
        ]
    },
    {
        "course": "SENG 321",
        "prereq": [],
        "coreq": [],
        "pastEnrol": [
            {"year": 2022, "term": "Fall", "size": 67}
        ]
    },
    {
        "course": "SENG 350",
        "prereq": [],
        "coreq": [],
        "pastEnrol": [
            {"year": 2022, "term": "Fall", "size": 71}
        ]
    },
    {
        "course": "SENG 426",
        "prereq": [],
        "coreq": [],
        "pastEnrol": [
            {"year": 2022, "term": "Summer", "size": 81}
        ]
    },
    {
        "course": "SENG 440",
        "prereq": [],
        "coreq": [],
        "pastEnrol": [
            {"year": 2022, "term": "Summer", "size": 94}
        ]
    },
    {
        "course": "SENG 499",
        "prereq": [],
        "coreq": [],
        "pastEnrol": [
            {"year": 2022, "term": "Summer", "size": 77}
        ]
    }
]