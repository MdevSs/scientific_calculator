from math import radians, cos;

def Pol(s):
    s=s.replace("Pol(", "");
    s=s.replace(")", "");
    print(s)
    n, k = s.split(",")
    return ((float(n) ** 2 + float(k) ** 2) ** (1/2));
        
    
# print(Pol("Rec(100, 60)", type=Poltype.SHIFT))