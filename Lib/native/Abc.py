from fractions import Fraction
def Abc(x: float) -> str:
    """
    Converte número em fração.
      Ab/c normal -> fração imprópria
      SHIFT + Ab/c -> número misto
    """
    frac = Fraction(x).limit_denominator()
    return f"{frac.numerator}/{frac.denominator}"
    

# print(Abc(eval("25÷85+12÷25")))