from math import factorial, sqrt, cos, radians, log, log10, e
from fractions import Fraction
import math

# States
shift, alpha = False, False

def ativar_shift():
    """Ativa o modo SHIFT e desativa ALPHA."""
    global shift, alpha
    shift = True
    alpha = False

def ativar_alpha():
    """Ativa o modo ALPHA e desativa SHIFT."""
    global shift, alpha
    alpha = True
    shift = False


# nCr
def nCr(s: str, ftype="none"):
    """
    Calcula combinações e permutações.
    Ex:
      nCr("5C2") -> 10
      nCr("5P2", ftype="shift") -> 20
    """
    if ftype == "none":
        if "C" in s:
            n, k = s.split("C")
            return factorial(int(n)) // (factorial(int(k)) * factorial(int(n) - int(k)))
    elif ftype == "shift":
        if "P" in s:
            n, k = s.split("P")
            return factorial(int(n)) // factorial(int(n) - int(k))
    else:
        raise ValueError("Argument type not expected: " + ftype)


# Pol
def Pol(s: str, type="none"):
    """
    Funções POL (polares e retangulares).
      Pol("3,4") -> 5.0   (modo normal: módulo)
      Pol("3,60", type="shift") -> 1.5   (x = r*cos θ)
      Pol("Ans:...") com type="alpha" -> avalia expressão
    """
    if type == "none":
        s = s.replace("Pol(", "").replace(")", "")
        n, k = s.split(",")
        return sqrt(float(n) ** 2 + float(k) ** 2)

    elif type == "shift":
        s = s.replace("Rec(", "").replace(")", "")
        n, k = s.split(",")
        return float(n) * cos(radians(float(k)))

    elif type == "alpha":
        if "Ans" in s:
            s = s.replace("Ans", "").replace("x", "*")
            expressions = s.split(":")
            for i in range(len(expressions)):
                if i == 0:
                    expressions[i] = eval(expressions[i])
                else:
                    expression = str(expressions[i - 1]) + str(expressions[i])
                    expressions[i] = eval(expression)
            return expressions
        else:
            raise ValueError("Sintax Error: Ans não informado")

    else:
        raise ValueError("Modo não reconhecido: " + type)


# ENG
def ENG(x: float) -> str:
    """
    Converte número para notação de engenharia.
    SHIFT + ENG -> volta para decimal.
    """
    if x == 0:
        return "0"
    exp = int(math.floor(math.log10(abs(x)) / 3) * 3)
    mantissa = x / (10 ** exp)
    return f"{mantissa}×10^{exp}"


# Ab/c
def frac_repr(x: float, use_shift=False) -> str:
    """
    Converte número em fração.
      Ab/c normal -> fração imprópria
      SHIFT + Ab/c -> número misto
    """
    frac = Fraction(x).limit_denominator()
    if use_shift:
        inteiro, resto = divmod(frac.numerator, frac.denominator)
        if inteiro == 0:
            return f"{resto}/{frac.denominator}"
        elif resto == 0:
            return str(inteiro)
        else:
            return f"{inteiro} {resto}/{frac.denominator}"
    else:
        return f"{frac.numerator}/{frac.denominator}"


# ln
def fnLn(x: float) -> float:
    """ln(x). SHIFT -> e^x. ALPHA -> constante e."""
    if x <= 0:
        raise ValueError("ln indefinido para x <= 0")
    return log(x)


# log
def fnLog10(x: float) -> float:
    """log10(x). SHIFT -> 10^x."""
    if x <= 0:
        raise ValueError("log indefinido para x <= 0")
    return log10(x)