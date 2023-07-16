import sys
import json
import unittest
from app.api.endpoints import predict_class_sizes
<<<<<<< HEAD
from app.data_model.course import Course, pastEnrollment

class api_test(unittest.TestCase):
    def test_predictor_one_class(self):
=======
from app.data_model.course import Course, pastEnrol

class api_test(unittest.TestCase):
    def test_predictor_one_class(self):
        print("testing predictor with one class")
>>>>>>> 3fb1b2e5aa0d51fbf0b6666fa4fa96bed098494f
        data = [
            Course(
                course="CSC 115",
                term=5,
<<<<<<< HEAD
                pastEnrol=[
                    pastEnrollment(year=2024, term=5, size=0),
=======
                prereq=[],
                coreq=[],
                pastEnrol=[
                    pastEnrol(year=2017, term=5, size=0),
>>>>>>> 3fb1b2e5aa0d51fbf0b6666fa4fa96bed098494f
                ]
            )
        ]
        response = predict_class_sizes(data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
