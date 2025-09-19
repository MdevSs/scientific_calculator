from math import radians, cos;

def Pol(s) -> float:
    s = s.replace("Pol(", "")
    if ")" in s: 
        s = s.replace(")", "")
    print(s)
    if "," not in s:
        raise ValueError("Faltando argumento em Pol(x, y)")
    n, k = s.split(",")
    if not n or not k:
        raise ValueError("Argumentos inválidos em Pol(x, y)")
    print(n, k)
    return ((float(n) ** 2 + float(k) ** 2) ** (1/2))