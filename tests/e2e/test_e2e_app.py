import asyncio, os, subprocess, time, requests
import pytest

BASE = "http://127.0.0.1:8000"

@pytest.fixture(scope="session", autouse=True)
def run_server():
    # start uvicorn in background
    proc = subprocess.Popen(["python","-m","uvicorn","app.main:app","--host","127.0.0.1","--port","8000"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # wait until up
    for _ in range(30):
        try:
            requests.get(BASE, timeout=0.5)
            break
        except Exception:
            time.sleep(0.5)
    yield
    proc.terminate()
    try: proc.wait(timeout=5)
    except subprocess.TimeoutExpired: proc.kill()

@pytest.mark.asyncio
async def test_ui_addition(page):
    await page.goto(BASE)
    await page.fill("#a","2")
    await page.fill("#b","3")
    await page.select_option("#op","add")
    await page.click("#go")
    # Wait for result to appear
    await page.wait_for_selector("#out")
    text = await page.text_content("#out")
    assert text.strip() == "5.0" or text.strip() == "5"
