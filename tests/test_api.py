from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_api():
    r = client.get("/add", params={"a": 2, "b": 3})
    assert r.status_code == 200
    assert r.json()["result"] == 5

def test_divide_api():
    r = client.get("/divide", params={"a": 10, "b": 2})
    assert r.status_code == 200
    assert r.json()["result"] == 5

def test_divide_zero_api():
    r = client.get("/divide", params={"a": 1, "b": 0})
    assert r.status_code == 400
