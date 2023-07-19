import json
import unittest
from fastapi.testclient import TestClient
from app.main import app

class api_test(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_get_endpoint(self):
        response = self.client.get("/schedule")
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.json(), {"detail": "Method Not Allowed"})

    def test_one_class_json(self):
        with open("test/data/one_class.json") as f:
            json_data = json.load(f)
        response = self.client.post("/schedule", json=json_data)
        self.assertEqual(response.status_code, 200)

    def test_two_classes_json(self):
        with open("test/data/two_classes.json") as f:
            json_data = json.load(f)
        response = self.client.post("/schedule", json=json_data)
        self.assertEqual(response.status_code, 200)
    
    def test_single_class_no_pastEnrollment(self):
        with open("test/data/single_class_no_pastEnrollment.json") as f:
            json_data = json.load(f)
        response = self.client.post("/schedule", json=json_data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()