import socket
import time
import threading
import uvicorn
from playwright.sync_api import Page
from app.main import app

def _free_port():
    s = socket.socket(); s.bind(("",0)); addr, port = s.getsockname(); s.close(); return port

def _run_server(port):
    # pragma: no cover
    uvicorn.run(app, host="127.0.0.1", port=port, log_level="warning")

def test_ui_addition(page: Page):
    # pragma: no cover
    port = _free_port()
    t = threading.Thread(target=_run_server, args=(port,), daemon=True)
    t.start()
    time.sleep(0.6)  # give server a moment
    page.goto(f"http://127.0.0.1:{port}/docs")
    assert page.title()  # page loaded
