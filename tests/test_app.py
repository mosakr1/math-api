import json
from app import app

def test_addition():
    client = app.test_client()
    response = client.post("/solve", json={"expression": "2+3"})
    data = json.loads(response.data)
    assert data["result"] == 5

def test_multiplication():
    client = app.test_client()
    response = client.post("/solve", json={"expression": "4*5"})
    data = json.loads(response.data)
    assert data["result"] == 20
