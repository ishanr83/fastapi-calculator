from fastapi import FastAPI, HTTPException, Query
from app.operations import add, subtract, multiply, divide
from app.logger import logger

app = FastAPI(title="FastAPI Calculator", version="1.0.0")

@app.get("/")
def root():
    # pragma: no cover
    return {"msg": "FastAPI Calculator. Visit /docs for Swagger UI."}

@app.get("/add")
def api_add(a: float = Query(...), b: float = Query(...)):
    result = add(a, b)
    logger.info("ADD a=%s b=%s result=%s", a, b, result)
    return {"result": result}

@app.get("/subtract")
def api_subtract(a: float = Query(...), b: float = Query(...)):
    result = subtract(a, b)
    logger.info("SUBTRACT a=%s b=%s result=%s", a, b, result)
    return {"result": result}

@app.get("/multiply")
def api_multiply(a: float = Query(...), b: float = Query(...)):
    result = multiply(a, b)
    logger.info("MULTIPLY a=%s b=%s result=%s", a, b, result)
    return {"result": result}

@app.get("/divide")
def api_divide(a: float = Query(...), b: float = Query(...)):
    try:
        result = divide(a, b)
        logger.info("DIVIDE a=%s b=%s result=%s", a, b, result)
        return {"result": result}
    except ValueError as e:
        logger.error("DIVIDE error a=%s b=%s err=%s", a, b, e)
        raise HTTPException(status_code=400, detail=str(e))
