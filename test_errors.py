import json
import unittest
from fastapi.testclient import TestClient
from app.main import app

class api_test(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_post_incorrect_file_not_list(self):
        with open("test/data/incorrect_file_format.json") as f:
            json_data = json.load(f)
        response = self.client.post("/schedule", json=json_data)
        self.assertEqual(response.status_code, 422)

    def test_post_incorrect_file(self):
        with open("test/data/incorrect_file_format2.json") as f:
            json_data = json.load(f)
        response = self.client.post("/schedule", json=json_data)
        self.assertEqual(response.status_code, 422)

if __name__ == '__main__':
    unittest.main()