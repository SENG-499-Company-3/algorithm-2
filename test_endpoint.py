import sys
import json
import unittest
from app.api.endpoints import predict_class_sizes
from app.data_model.course import Course, pastEnrollment

class api_test(unittest.TestCase):
    def test_predictor_one_class(self):
        data = [
            Course(
                course="CSC 115",
                term=5,
                pastEnrol=[
                    pastEnrollment(year=2024, term=5, size=0),
                ]
            )
        ]
        response = predict_class_sizes(data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
