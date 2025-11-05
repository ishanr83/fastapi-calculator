"""FastAPI calculator application."""
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import app.operations as op
from app.logger import log

app = FastAPI(title="FastAPI Calculator")


def _calc(func, a: float, b: float) -> float:
    """Execute calculation with error handling."""
    try:
        result = func(a, b)
        log.info(f"success op={func.__name__} a={a} b={b} result={result}")
        return result
    except ValueError as e:
        log.error(f"error op={func.__name__} a={a} b={b} err={e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        log.error(f"error op={func.__name__} a={a} b={b} err={e}")
        raise HTTPException(status_code=500, detail="Internal server error")


@app.get("/", response_class=HTMLResponse)
def read_root():
    """Serve the calculator UI."""
    html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Calculator</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; }
        input, select, button { margin: 10px 5px; padding: 10px; font-size: 16px; }
        #out { margin-top: 20px; padding: 10px; background: #f0f0f0; border-radius: 5px; min-height: 20px; }
    </style>
</head>
<body>
    <h1>FastAPI Calculator</h1>
    <div>
        <input type="number" id="a" placeholder="Number A" step="any" value="">
        <input type="number" id="b" placeholder="Number B" step="any" value="">
    </div>
    <div>
        <select id="op">
            <option value="add">Add (+)</option>
            <option value="subtract">Subtract (-)</option>
            <option value="multiply">Multiply (×)</option>
            <option value="divide">Divide (÷)</option>
            <option value="power">Power (^)</option>
            <option value="root">Root (√)</option>
            <option value="modulus">Modulus (%%)</option>
            <option value="int_divide">Integer Divide (//)</option>
            <option value="percent">Percent</option>
            <option value="abs_diff">Absolute Difference</option>
        </select>
        <button id="go" onclick="calculate()">Calculate</button>
    </div>
    <div id="out"></div>
    <script>
        async function calculate() {
            const a = document.getElementById('a').value;
            const b = document.getElementById('b').value;
            const operation = document.getElementById('op').value;
            const outDiv = document.getElementById('out');
            
            if (!a || !b) {
                outDiv.textContent = 'Please enter both numbers';
                outDiv.style.display = 'block';
                return;
            }
            
            try {
                const response = await fetch('/api/' + operation + '?a=' + a + '&b=' + b);
                const data = await response.json();
                
                if (response.ok) {
                    outDiv.textContent = 'Result: ' + data.result;
                } else {
                    outDiv.textContent = 'Error: ' + data.detail;
                }
                outDiv.style.display = 'block';
            } catch (error) {
                outDiv.textContent = 'Error: ' + error.message;
                outDiv.style.display = 'block';
            }
        }
    </script>
</body>
</html>
"""
    return html_content


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
