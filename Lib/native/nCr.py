from math import factorial;
def nCr(s, ftype = "none"):

    if (ftype=="none"):
        if "C" in s:
            n,k= s.split("C")
            return factorial(n) // (factorial(k) * factorial(n - k))
    elif ftype == "shift":
        if "P" in s:
            n,k = s.split("P")
            return factorial(n) // factorial(n - k)
    else:
        return ValueError("Argument type not expected: "+ftype)