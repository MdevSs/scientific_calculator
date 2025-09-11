from enum import Enum
from math import radians, cos;

class Poltype(Enum):
    SHIFT="shift"
    ALPHA="alpha"
    NONE="none"

def Pol(s, type = "none"):
    if (type == Poltype.NONE):
        s=s.replace("Pol(", "");
        s=s.replace(")", "");
        print(s)
        n, k = s.split(",")
        return ((float(n) ** 2 + float(k) ** 2) ** (1/2));
    elif type==Poltype.ALPHA:
        if("Ans" in s):
            s = s.replace("Ans", "")
            s = s.replace("x","*")
            expressions = s.split(":");

            for i in range(len(expressions)):
                if i==0:
                    expressions[i] = eval(expressions[i])
                else:
                    expression = str(expressions[i-1])+""+str(expressions[i])
                    expressions[i] = eval(expression)
            return expressions
        else:
            return ValueError("Sintax Error: Ans não informado")

    elif type == Poltype.SHIFT:
        s = s.replace("Rec(", "");
        s = s.replace(")", "");
        n, k = s.split(",")
        return (float(n) * cos(radians(float(k))))
    
# print(Pol("Rec(100, 60)", type=Poltype.SHIFT))