def add(a: float, b: float) -> float: return a + b
def subtract(a: float, b: float) -> float: return a - b
def multiply(a: float, b: float) -> float: return a * b
def divide(a: float, b: float) -> float:
    if b == 0: raise ZeroDivisionError("division by zero")
    return a / b
def power(a: float, b: float) -> float: return a ** b
def root(a: float, b: float) -> float:
    if b == 0: raise ValueError("0th root undefined")
    if a < 0 and int(b) == b and int(b) % 2 == 0:
        raise ValueError("even root of negative")
    return a ** (1.0 / b)
def modulus(a: float, b: float) -> float:
    if b == 0: raise ZeroDivisionError("mod by zero")
    return a % b
def int_divide(a: float, b: float) -> float:
    if b == 0: raise ZeroDivisionError("int divide by zero")
    return a // b
def percent(a: float, b: float) -> float:
    if b == 0: raise ZeroDivisionError("percent divide by zero")
    return (a / b) * 100.0
def abs_diff(a: float, b: float) -> float: return abs(a - b)
