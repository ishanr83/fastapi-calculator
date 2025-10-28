from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add():
    r = client.get("/api/add", params={"a":2,"b":3})
    assert r.status_code==200 and r.json()["result"]==5

def test_divide_by_zero():
    r = client.get("/api/divide", params={"a":1,"b":0})
    assert r.status_code==400
    assert "division by zero" in r.json()["detail"]

def test_root():
    r = client.get("/api/root", params={"a":27,"b":3})
    assert r.status_code==200 and abs(r.json()["result"]-3.0)<1e-6
