import unittest
import json
import os
from app import app, db
from app.models.test_model import Test

basedir = os.path.abspath(os.path.dirname(__file__))

class TestApiTest(unittest.TestCase):
    def setUp(self):
   
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "test.db")
        app.config["WTF_CSRF_ENABLED"] = False

        self.client = app.test_client()

        # Set up the database
        with app.app_context():
            db.create_all()

#     def tearDown(self):
#         """
#         Clean up after each test
#         """
#         with app.app_context():
#             db.session.remove()
#             db.drop_all()

    def test_greeting_endpoint(self):
        """
        Test the ExampleApi /greeting endpoint
        """
        response = self.client.get("/api/v1/exampleapi/greeting")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode("utf-8"), "hello")

    def test_add_test_success(self):
        """
        Test adding a new Test record with the TestApi
        """
        payload = {"name": "Example Name"}
        response = self.client.post(
            "/api/v1/test-test",
            data=json.dumps(payload),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertIn("message", data)
        self.assertIn("id", data)
        self.assertEqual(data["message"], "Test record created successfully")

        # # Verify the record in the database
        # with app.app_context():
        #     test_record = db.session.get(Test, data["id"])
        #     self.assertIsNotNone(test_record)
        #     self.assertEqual(test_record.name, "Example Name")

if __name__ == "__main__":
    unittest.main()



