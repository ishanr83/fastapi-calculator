from fastapi import FastAPI, HTTPException
import logging

app = FastAPI(title="FastAPI Calculator")

# Logging setup
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@app.middleware("http")
async def log_requests(request, call_next):
    logging.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logging.info(f"Response: {response.status_code}")
    return response  # pragma: no cover

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Calculator!"}

@app.get("/add")
def add(a: float, b: float):
    return {"operation": "add", "result": a + b}

@app.get("/subtract")
def subtract(a: float, b: float):
    return {"operation": "subtract", "result": a - b}

@app.get("/multiply")
def multiply(a: float, b: float):
    return {"operation": "multiply", "result": a * b}

@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        logging.error("Division by zero attempted")  # pragma: no cover
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    return {"operation": "divide", "result": a / b}
