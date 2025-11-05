from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_index():
    """Test that the index page loads."""
    r = client.get("/")
    assert r.status_code == 200
    assert "FastAPI Calculator" in r.text


def test_add():
    """Test addition endpoint."""
    r = client.get("/api/add", params={"a": 2, "b": 3})
    assert r.status_code == 200
    assert r.json()["result"] == 5


def test_subtract():
    """Test subtraction endpoint."""
    r = client.get("/api/subtract", params={"a": 10, "b": 4})
    assert r.status_code == 200
    assert r.json()["result"] == 6


def test_multiply():
    """Test multiplication endpoint."""
    r = client.get("/api/multiply", params={"a": 3, "b": 4})
    assert r.status_code == 200
    assert r.json()["result"] == 12


def test_divide():
    """Test division endpoint."""
    r = client.get("/api/divide", params={"a": 8, "b": 2})
    assert r.status_code == 200
    assert r.json()["result"] == 4


def test_divide_by_zero():
    """Test division by zero returns error."""
    r = client.get("/api/divide", params={"a": 1, "b": 0})
    assert r.status_code == 400
    assert "division by zero" in r.json()["detail"]


def test_power():
    """Test power endpoint."""
    r = client.get("/api/power", params={"a": 2, "b": 5})
    assert r.status_code == 200
    assert r.json()["result"] == 32


def test_root():
    """Test root endpoint."""
    r = client.get("/api/root", params={"a": 27, "b": 3})
    assert r.status_code == 200
    assert abs(r.json()["result"] - 3.0) < 1e-6


def test_root_error():
    """Test root with invalid input returns error."""
    r = client.get("/api/root", params={"a": -8, "b": 2})
    assert r.status_code == 400


def test_modulus():
    """Test modulus endpoint."""
    r = client.get("/api/modulus", params={"a": 10, "b": 3})
    assert r.status_code == 200
    assert r.json()["result"] == 1


def test_modulus_zero():
    """Test modulus by zero returns error."""
    r = client.get("/api/modulus", params={"a": 1, "b": 0})
    assert r.status_code == 400


def test_int_divide():
    """Test integer division endpoint."""
    r = client.get("/api/int_divide", params={"a": 7, "b": 2})
    assert r.status_code == 200
    assert r.json()["result"] == 3


def test_int_divide_zero():
    """Test integer division by zero returns error."""
    r = client.get("/api/int_divide", params={"a": 1, "b": 0})
    assert r.status_code == 400


def test_percent():
    """Test percent endpoint."""
    r = client.get("/api/percent", params={"a": 25, "b": 100})
    assert r.status_code == 200
    assert r.json()["result"] == 25.0


def test_percent_zero():
    """Test percent with zero denominator returns error."""
    r = client.get("/api/percent", params={"a": 1, "b": 0})
    assert r.status_code == 400


def test_abs_diff():
    """Test absolute difference endpoint."""
    r = client.get("/api/abs_diff", params={"a": 10, "b": 3})
    assert r.status_code == 200
    assert r.json()["result"] == 7
