from math import log
def fnLn(x: float) -> float:
    """ln(x). SHIFT -> e^x. ALPHA -> constante e."""
    if x <= 0:
        raise ValueError("ln indefinido para x <= 0")
    return log(x)