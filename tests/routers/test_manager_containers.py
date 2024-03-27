import unittest
from starlette.testclient import TestClient
from app.main import app


class ContainersManagerTest(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_check_if_view_return_200(self):
        response = self.client.get("/manager/")
        assert response.status_code == 200
