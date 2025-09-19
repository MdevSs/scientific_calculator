from fractions import Fraction
def Dc(x: float) -> str:
    frac = Fraction(x).limit_denominator()
    
    inteiro, resto = divmod(frac.numerator, frac.denominator)
    if inteiro == 0:
        return f"{resto}/{frac.denominator}"
    elif resto == 0:
        return str(inteiro)
    else:
        return f"{inteiro} {resto}/{frac.denominator}"

print(Dc(20.5))