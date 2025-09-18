from math import radians, cos;
def Rec(s):    
    s = s.replace("Rec(", "");
    s = s.replace(")", "");
    n, k = s.split(",")
    return (float(n) * cos(radians(float(k))))