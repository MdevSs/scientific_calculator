from math import log10
def fnLog10(s: str) -> float:
    """log10(x). SHIFT -> 10^x."""
    formula = s
    if "log" in formula:
        formula = formula.strip()
        value = float(formula.removeprefix("log"))
    if value <= 0:
        raise ValueError("log indefinido para x <= 0")
    return log10(value)