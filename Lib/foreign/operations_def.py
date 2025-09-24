'''
Aqui é a formatação dos graus
Faça com que o botão do grau adcione um símbolo de grau (°) ao final do número atual e a função vai reconhecer isso.
Coloque isso dentro da função de calcular, ele funciona como um eval normal, mas reconhece o símbolo de grau.
Usar assim:
 from functions.fnNew import formatDegree as fmtDeg
 fmtDeg.formatDegree(expression, app, display)
 expression = string que vai receber a formatação
 app = instância da classe App (main)
 display = campo de entrada (Entry) do tkinter
'''
import tkinter as tk
import re

import variables as var
'''
Esse import variables é aonde você guarda suas variáveis globais
Por exemplo shift, alpha.
Nesse caso ele vai pegar o modo que a calculadora está (fix, sci, norm) e a quantidade de dígitos
de arredondamento.
'''

from foreign import degrees as deg

def format_result(value, app):
    try:
        if hasattr(var, "get_round_settings"):
            mode, digits = var.get_round_settings()
        else:
            mode, digits = "norm", 2
        if mode == "fix":
            out = f"{value:.{digits}f}"
        elif mode == "sci":
            sig = max(1, int(digits))
            out = f"{value:.{sig}e}"
        else:
            out = f"{value:.12g}"
        if app.selecao.get() == "Normal":
            out = out.replace(".", ",")
        return out
    except Exception:
        return "Erro"

def formatDegree(expression, app, display):
    token_pattern = re.compile(r"([-+]?\d+(?:\.\d+)?)(°?)")
    tokens = list(token_pattern.finditer(expression))

    if tokens:
        all_have_deg = all(m.group(2) == "°" for m in tokens)

        def _strip_deg(match):
            return match.group(1)
        
        expr = token_pattern.sub(_strip_deg, expression)
        expr = re.sub(r"(\d+(?:\.\d+)?)%", r"(\1/100)", expr)
        resultado = eval(expr)
        var.lastNumber = str(resultado)

        if all_have_deg:
            try:
                dms_str = deg.convertDecimal(str(resultado))
            except Exception:
                texto = format_result(resultado, app)
                display.delete(0, "end")
                display.insert(0, texto)
                
                return

            if app.selecao.get() == "Normal":
                dms_str = dms_str.replace(".", ",")

            display.delete(0, "end")
            display.insert(0, dms_str)
            
            return
        else:
            texto = format_result(resultado, app)
            display.delete(0, "end")
            display.insert(0, texto)
            
            return
    else:
        resultado = eval(expression)
        var.lastNumber = str(resultado)
        texto = format_result(resultado, app)
        display.delete(0, "end")
        display.insert(0, texto)
        
        return