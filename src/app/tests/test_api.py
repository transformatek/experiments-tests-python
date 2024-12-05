import pytest
import json
from app import app  ,db
from app.models.test_model import Test




token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNzMzNDA5Nzg4LCJqdGkiOiIyN2FkMTUzYS01NGRkLTQ3NzctOWJmNy1iZDlkYzdlNTE4YTYiLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoxLCJuYmYiOjE3MzM0MDk3ODgsImNzcmYiOiJhMmE2YjYyNi1kNTQ4LTRhZDUtODM0OS0wZjExYjVkNDBkODEiLCJleHAiOjE3MzM0OTYxODh9.mZVzaVxTPPJARZHJfli05JY7CG09nsC3sAtFIDT7P70" 

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client  



def test_get_test_records(client):
    """Test GET TEST"""
    
    response = client.get(
        '/api/v1/test/',
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "result" in data  
    assert isinstance(data["result"], list) 
    assert len(data["result"]) >= 1 

def test_create_record(client):
    """Test PUT"""
    payload = {"name": "fatima"}
    response = client.post(
        '/api/v1/test/',
        data=json.dumps(payload),
        content_type='application/json',
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 201 

def test_update_record(client):
    """Test DELETE"""
    record = db.session.query(Test).first()  
    payload = {"name": "ccccccc"}
    response = client.put(
        f'/api/v1/test/{2}',
        data=json.dumps(payload),
        content_type='application/json',
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200  




def test_delete_record(client):
    """Test pour mettre à jour un enregistrement existant."""
    record = db.session.query(Test).first()  
    payload = {"name": "ccccccc"}
    response = client.delete(
        f'/api/v1/test/{3}',
        data=json.dumps(payload),
        content_type='application/json',
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200  


    
def test_greeting(client):
    """Test the greeting endpoint in ExampleApi."""
    response = client.get('/api/v1/exampleapi/greeting') 
    assert response.status_code == 200  
    assert response.data.decode('utf-8') == "hello"