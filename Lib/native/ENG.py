import math
def ENG(x: float) -> str:
    """
    Converte número para notação de engenharia.
    SHIFT + ENG -> volta para decimal.
    """
    if x == 0:
        return "0"
    exp = int((math.log10(abs(x)) / 3) * 3)
    mantissa = x / (10 ** exp)
    return f"{mantissa}×10^{exp}"


