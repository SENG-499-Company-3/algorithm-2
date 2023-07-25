import json
import unittest
from fastapi.testclient import TestClient
from app.main import app

class api_test(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_one_class_json(self):
        with open("test/data/one_class.json") as f:
            json_data = json.load(f)
        response = self.client.post("/schedule", json=json_data)
        self.assertIsInstance(response.json(), list)
        result = response.json()

        # Summer
        self.assertEqual(result[0]["course"], "csc115")
        self.assertEqual(result[0]["term"], 5)
        self.assertTrue(result[0]["size"] >= 75)
        self.assertTrue(result[0]["size"] < 146)

        # Fall
        self.assertEqual(result[1]["course"], "csc115")
        self.assertEqual(result[1]["term"], 9)
        self.assertTrue(result[1]["size"] > 129)
        self.assertTrue(result[1]["size"] < 200)

        # Spring
        self.assertEqual(result[2]["course"], "csc115")
        self.assertEqual(result[2]["term"], 1)
        self.assertTrue(result[2]["size"] > 299)
        self.assertTrue(result[2]["size"] < 400)

if __name__ == '__main__':
    unittest.main()
