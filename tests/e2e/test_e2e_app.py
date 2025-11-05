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
    max_retries = 30
    for i in range(max_retries):
        try:
            r = requests.get(BASE, timeout=1)
            if r.status_code == 200:
                time.sleep(1)  # Extra stability wait
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
    page.locator("#a").fill("2")
    page.locator("#b").fill("3")
    page.locator("#op").select_option("add")
    page.locator("#go").click()
    # Wait for result
    page.locator("#out").wait_for(state="visible", timeout=5000)
    text = page.locator("#out").text_content()
    assert "5" in text


def test_ui_multiply(page):  # pragma: no cover
    """Test multiplication through the UI."""
    page.goto(BASE)
    page.locator("#a").fill("4")
    page.locator("#b").fill("5")
    page.locator("#op").select_option("multiply")
    page.locator("#go").click()
    page.locator("#out").wait_for(state="visible", timeout=5000)
    text = page.locator("#out").text_content()
    assert "20" in text


def test_ui_divide_by_zero(page):  # pragma: no cover
    """Test division by zero error through the UI."""
    page.goto(BASE)
    page.locator("#a").fill("10")
    page.locator("#b").fill("0")
    page.locator("#op").select_option("divide")
    page.locator("#go").click()
    page.locator("#out").wait_for(state="visible", timeout=5000)
    text = page.locator("#out").text_content()
    assert "division by zero" in text.lower()
