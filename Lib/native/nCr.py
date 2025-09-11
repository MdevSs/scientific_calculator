from math import factorial;
def nCr(s):
    if "C" in s:
        n,k= s.split("C")
        return factorial(n) // (factorial(k) * factorial(n - k))
