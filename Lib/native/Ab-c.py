from fractions import Fraction
def Abc(x: float, use_shift=False) -> str:
    """
    Converte número em fração.
      Ab/c normal -> fração imprópria
      SHIFT + Ab/c -> número misto
    """
    frac = Fraction(x).limit_denominator()
    
    inteiro, resto = divmod(frac.numerator, frac.denominator)
    if inteiro == 0:
        return f"{resto}/{frac.denominator}"
    elif resto == 0:
        return str(inteiro)
    else:
        return f"{inteiro} {resto}/{frac.denominator}"
        