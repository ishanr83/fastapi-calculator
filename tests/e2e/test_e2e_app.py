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
            r = requests.get(BASE, timeout=1)
            if r.status_code == 200:
                break
        except Exception:
            time.sleep(0.5)
    time.sleep(1)  # Extra wait for stability
    yield
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()


def test_ui_addition(page):  # pragma: no cover
    """Test addition through the UI."""
    page.goto(BASE, wait_until="networkidle")
    page.wait_for_selector("#a", state="visible", timeout=10000)
    page.fill("#a", "2")
    page.fill("#b", "3")
    page.select_option("#op", "add")
    page.click("#go")
    page.wait_for_function("document.getElementById('out').textContent !== ''", timeout=5000)
    text = page.text_content("#out")
    assert "5" in text


def test_ui_multiply(page):  # pragma: no cover
    """Test multiplication through the UI."""
    page.goto(BASE, wait_until="networkidle")
    page.wait_for_selector("#a", state="visible", timeout=10000)
    page.fill("#a", "4")
    page.fill("#b", "5")
    page.select_option("#op", "multiply")
    page.click("#go")
    page.wait_for_function("document.getElementById('out').textContent !== ''", timeout=5000)
    text = page.text_content("#out")
    assert "20" in text


def test_ui_divide_by_zero(page):  # pragma: no cover
    """Test division by zero error through the UI."""
    page.goto(BASE, wait_until="networkidle")
    page.wait_for_selector("#a", state="visible", timeout=10000)
    page.fill("#a", "10")
    page.fill("#b", "0")
    page.select_option("#op", "divide")
    page.click("#go")
    page.wait_for_function("document.getElementById('out').textContent !== ''", timeout=5000)
    text = page.text_content("#out")
    assert "division by zero" in text.lower()
