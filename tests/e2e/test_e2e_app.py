import subprocess
import time
import requests
import pytest

BASE = "http://127.0.0.1:8000"


@pytest.fixture(scope="session", autouse=True)
def run_server():  # pragma: no cover
    """Start uvicorn server for E2E tests."""
    proc = subprocess.Popen(
        ["python", "-m", "uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    # Wait until server is up
    for _ in range(30):
        try:
            requests.get(BASE, timeout=0.5)
            break
        except Exception:
            time.sleep(0.5)
    yield
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()


def test_ui_addition(page):  # pragma: no cover
    """Test addition through the UI."""
    page.goto(BASE)
    page.fill("#a", "2")
    page.fill("#b", "3")
    page.select_option("#op", "add")
    page.click("#go")
    # Wait for result to appear
    page.wait_for_selector("#out")
    text = page.text_content("#out")
    assert text.strip() == "5.0" or text.strip() == "5"


def test_ui_multiply(page):  # pragma: no cover
    """Test multiplication through the UI."""
    page.goto(BASE)
    page.fill("#a", "4")
    page.fill("#b", "5")
    page.select_option("#op", "multiply")
    page.click("#go")
    page.wait_for_selector("#out")
    text = page.text_content("#out")
    assert text.strip() == "20.0" or text.strip() == "20"


def test_ui_divide_by_zero(page):  # pragma: no cover
    """Test division by zero error through the UI."""
    page.goto(BASE)
    page.fill("#a", "10")
    page.fill("#b", "0")
    page.select_option("#op", "divide")
    page.click("#go")
    page.wait_for_selector("#out")
    text = page.text_content("#out")
    assert "division by zero" in text.lower()
