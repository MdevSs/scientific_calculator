from math import log
def fnLn(s: str) -> float:
    """ln(x). SHIFT -> e^x. ALPHA -> constante e."""
    formula = s
    if "ln" in formula:
        formula = formula.strip()
        value = float(formula.removeprefix("ln"))
    else:
        raise ValueError("log não está definido")
    if value <= 0:
        raise ValueError("ln indefinido para x <= 0")
    return log(value)