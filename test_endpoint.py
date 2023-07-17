import json
import unittest
from fastapi.testclient import TestClient
from app.api.main import app

class api_test(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_get_endpoint(self):
        response = self.client.get("/schedule")
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.json(), {"detail": "Method Not Allowed"})

    def test_single_class(self):
        json_data = '''
        [
            {
                "course": "csc115",
                "Term": [
                    5
                ],
                "Year": 2024,
                "pastEnrollment": [
                    {
                        "year": 2017,
                        "term": 5,
                        "size": 75
                    }
                ]
            }
        ]
        '''

        formatted_json_data = json.loads(json_data)
        response = self.client.post("/schedule", json=formatted_json_data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
