"""Mathematical operations."""


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("division by zero")
    return a / b


def power(a: float, b: float) -> float:
    """Raise a to the power of b."""
    return a ** b


def root(a: float, b: float) -> float:
    """Calculate the bth root of a."""
    if a < 0 and b % 2 == 0:
        raise ValueError("Cannot calculate even root of negative number")
    return a ** (1 / b)


def modulus(a: float, b: float) -> float:
    """Calculate a modulo b."""
    if b == 0:
        raise ValueError("Modulo by zero")
    return a % b


def int_divide(a: float, b: float) -> float:
    """Integer division of a by b."""
    if b == 0:
        raise ValueError("division by zero")
    return a // b


def percent(a: float, b: float) -> float:
    """Calculate what percent a is of b."""
    if b == 0:
        raise ValueError("division by zero")
    return (a / b) * 100


def abs_diff(a: float, b: float) -> float:
    """Calculate absolute difference between a and b."""
    return abs(a - b)
