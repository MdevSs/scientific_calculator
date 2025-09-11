def twoPoints(s):
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