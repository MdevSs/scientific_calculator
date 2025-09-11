from math import log10
def fnLog10(x: float) -> float:
    """log10(x). SHIFT -> 10^x."""
    if x <= 0:
        raise ValueError("log indefinido para x <= 0")
    return log10(x)