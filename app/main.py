from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from app import operations as op
from app.logger import logger

app = FastAPI(title="FastAPI Calculator")

HTML = """<!doctype html>
<html><head><meta charset="utf-8"><title>FastAPI Calculator</title></head>
<body style="font-family:Arial;max-width:600px;margin:40px auto">
  <h1>FastAPI Calculator</h1>
  <div>
    <input id="a" type="number" step="any" placeholder="a">
    <input id="b" type="number" step="any" placeholder="b">
    <select id="op">
      <option>add</option><option>subtract</option><option>multiply</option>
      <option>divide</option><option>power</option><option>root</option>
      <option>modulus</option><option>int_divide</option><option>percent</option><option>abs_diff</option>
    </select>
    <button id="go">Compute</button>
    <div id="out" style="margin-top:12px;font-weight:bold"></div>
  </div>
  <script>
    async function call(){
      const a = document.getElementById('a').value;
      const b = document.getElementById('b').value;
      const op = document.getElementById('op').value;
      const res = await fetch(`/api/${op}?a=${a}&b=${b}`);
      const data = await res.json();
      document.getElementById('out').textContent = data.result !== undefined ? data.result : (data.detail || "error");
    }
    document.getElementById('go').addEventListener('click', call);
  </script>
</body></html>"""


@app.get("/", response_class=HTMLResponse)
def index():
    """Serve the calculator UI."""
    return HTML


def _calc(fn, a: float, b: float) -> float:
    """Helper function to execute calculation with logging and error handling."""
    try:
        value = fn(float(a), float(b))
        logger.info("op=%s a=%s b=%s result=%s", fn.__name__, a, b, value)
        return value
    except Exception as e:
        logger.error("error op=%s a=%s b=%s err=%s", fn.__name__, a, b, e)
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/api/add")
def add(a: float, b: float):
    """Add two numbers."""
    return {"result": _calc(op.add, a, b)}


@app.get("/api/subtract")
def subtract(a: float, b: float):
    """Subtract b from a."""
    return {"result": _calc(op.subtract, a, b)}


@app.get("/api/multiply")
def multiply(a: float, b: float):
    """Multiply two numbers."""
    return {"result": _calc(op.multiply, a, b)}


@app.get("/api/divide")
def divide(a: float, b: float):
    """Divide a by b."""
    return {"result": _calc(op.divide, a, b)}


@app.get("/api/power")
def power(a: float, b: float):
    """Raise a to the power of b."""
    return {"result": _calc(op.power, a, b)}


@app.get("/api/root")
def root(a: float, b: float):
    """Calculate the bth root of a."""
    return {"result": _calc(op.root, a, b)}


@app.get("/api/modulus")
def modulus(a: float, b: float):
    """Calculate a modulo b."""
    return {"result": _calc(op.modulus, a, b)}


@app.get("/api/int_divide")
def int_divide(a: float, b: float):
    """Integer division of a by b."""
    return {"result": _calc(op.int_divide, a, b)}


@app.get("/api/percent")
def percent(a: float, b: float):
    """Calculate what percent a is of b."""
    return {"result": _calc(op.percent, a, b)}


@app.get("/api/abs_diff")
def abs_diff(a: float, b: float):
    """Calculate absolute difference."""
    return {"result": _calc(op.abs_diff, a, b)}
