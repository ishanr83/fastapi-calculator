from playwright.sync_api import sync_playwright

def test_docs_page_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://127.0.0.1:8000/docs")
        assert "FastAPI" in page.title()
        browser.close()  # pragma: no cover
