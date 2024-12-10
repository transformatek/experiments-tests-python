# -*- coding: utf-8 -*-
import json

import pytest

from app import app, db
from app.models.test_model import Test
import os

basedir = os.path.abspath(os.path.dirname(__file__))

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNzMzODE5NDEyLCJqdGkiOiIwNDU5MTIwNC03YzFmLTQ4ODQtYWY5My1lODQ5ZWZhNTY2OGYiLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoxLCJuYmYiOjE3MzM4MTk0MTIsImNzcmYiOiIwOGNiNDQxNi1mMmM1LTQ4MmUtYmQ5MC1lYjk4YjcxNGI3MjUiLCJleHAiOjE3MzM5MDU4MTJ9.xAIUthTW_iuXYSFhu9iyhZyN5XByGpgRyvBlbU3nhpA"


@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "test.db")
    with app.test_client() as client:
        with app.app_context():
            db.create_all() 
        yield client
        # with app.app_context():
        #     db.drop_all() 



def test_get_test_records(client):
    """Test GET TEST"""

    response = client.get(
        "/api/v1/test/", headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "result" in data
    assert isinstance(data["result"], list)
    assert len(data["result"]) >= 1


def test_create_record(client):
    """Test POST"""
    payload = {"name": "fatima"}
    response = client.post(
        "/api/v1/test/",
        data=json.dumps(payload),
        content_type="application/json",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 201


def test_update_record(client):
    """Test PUT"""
    payload = {"name": "aichouche"}
    response = client.put(
        f"/api/v1/test/{3}",
        data=json.dumps(payload),
        content_type="application/json",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200


def test_delete_record(client):
    """Test DELETE"""
    response = client.delete(
        f"/api/v1/test/{3}",
        content_type="application/json",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200


def test_greeting(client):
    """Test the greeting endpoint in ExampleApi."""
    response = client.get("/api/v1/exampleapi/greeting")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "hello"


def test_create_recordd(client):
    """Test POST"""
    payload = {"name": "dounia"}
    response = client.post(
        "/api/v1/test-test",
        data=json.dumps(payload),
        content_type="application/json",
    )
    assert response.status_code == 201