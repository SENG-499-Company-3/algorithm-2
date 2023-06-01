from fastapi import HTTPException

def perform_algorithm(semester: str) -> int:
    """
    Perform the algorithm to determine the class size based on the given semester.

    Parameters:
        - semester (str): The semester for which class information is requested. Can be "FALL", "SPRING", or "SUMMER".

    Returns:
        - int: The determined class size based on the semester.

    Raises:
        - HTTPException (status_code=400): If an invalid semester is provided.
    """
    if semester == "FALL":
        class_size = 200
    elif semester == "SPRING":
        class_size = 150
    elif semester == "SUMMER":
        class_size = 100
    else:
        raise HTTPException(status_code=400, detail="Invalid semester")

    return class_size