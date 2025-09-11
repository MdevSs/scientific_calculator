from fractions import Fraction
def Dc(x: float) -> str:
    frac = Fraction(x).limit_denominator()
    return f"{frac.numerator}/{frac.denominator}"