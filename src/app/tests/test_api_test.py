# -*- coding: utf-8 -*-
import json

import pytest

from app import app, db
from app.models.test_model import Test

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNzMzNjQ2MzgwLCJqdGkiOiI4ZDkzYjRjYi1hZWE2LTQ4NjQtOTJjYS1hN2MxYzU2NzI4NzEiLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoxLCJuYmYiOjE3MzM2NDYzODAsImNzcmYiOiJkNWZhN2NjOS1kM2FjLTQ0ZDItYTUxMi01ZGNiNDk4NmZiMGIiLCJleHAiOjE3MzM3MzI3ODB9.wM7XgQnXyYHyEY0qmv3LsSEw51vECxnxn8qHgfSRN9A"


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


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
    record = db.session.query(Test).first()
    payload = {"name": "aichouche"}
    response = client.put(
        f"/api/v1/test/{2}",
        data=json.dumps(payload),
        content_type="application/json",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200


def test_delete_record(client):
    """Test DELETE"""
    record = db.session.query(Test).first()
    response = client.delete(
        f"/api/v1/test/{4}",
        content_type="application/json",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200


def test_greeting(client):
    """Test the greeting endpoint in ExampleApi."""
    response = client.get("/api/v1/exampleapi/greeting")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "hello"
