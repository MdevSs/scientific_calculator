# Não aceita letras;
# Sem divisão por 0;
# Não ter sinais seguidos "--";
# Ao iniciar com virgula, zero no início;
# C limpa a linha atual, a operação atual;
# CE limpa todo o cálculo;
# Resolver operação ao clicar igual ou outra operação;
# Só pode usar uma segunda virgula após o uso de um operador ou sinal de igual;
# Formatar com ponto números acima de mil.
from Lib.native.nCr import * 
from Lib.native.nPr import * 
from Lib.native.ENG import * 
from Lib.native.Ln import * 
from Lib.native.Log import * 
from Lib.native.Pol import * 
from Lib.native.Rec import * 
from Lib.native.twoPoints import *
from Lib.native.Abc import *
from Lib.native.Dc import *
import re
import math
from math import *
import tkinter as tk

# Colors
bg_color = "#1E1E1E"
btn_color = "#2D2D2D"
text_color = "#FFFFFF"
accent_color = "#3C3C3C"
equal_color = "#AAAAAA"

# State
current = ""
expression = ""
memory = 0
decimal_allowed = True
cientific = False
shift = False
alpha = False

def format_number(n: str):
  """Formata número com ponto separador de milhar e vírgula decimal."""
  try:
    if "." in n:
      int_part, dec_part = n.split(".")
      int_part = f"{int(int_part):,}".replace(",", ".")
      return f"{int_part},{dec_part[:8]}"
    else:
      return f"{int(n):,}".replace(",", ".")
  except:
    return n

def split_expression(expr: str):
    # Regex: números (com ^, decimais, negativos) ou operadores
    tokens = re.findall(
        r'Pol\([^\)]*\)?'                # Pol(x, y) com qualquer coisa dentro dos parênteses
        r'|Rec\([^\)]*\)?'               # Rec(x, y)
        r'|\d+C\d+'                     # nCr (ex: 8C3)
        r'|\d+P\d+'                     # nPr (ex: 20P3)
        r'|(?:log|ln|sin|cos|tan)\s*-?\d+(?:[.,]\d+)?'  # funções com número
        r'|-?\d+(?:[.,]\d+)?(?:\^?\d+)?'  # números decimais ou inteiros com expoente
        r'|[+\-×X÷*/()]',               # operadores
        expr.replace(" ", "")
    )
    tokens = [t.strip() for t in tokens if t.strip()]
    print(tokens)
    return tokens


def update_display():
  if current:
    display_var.set(current)
  elif expression:
    display_var.set(format_number(expression) if expression.replace(".", "").isdigit() else expression)
  else:
    display_var.set("0")

# def eval_expression():
#   global expression, current
#   print(current)
#   try:
#     if current:
#       expression += current.replace(",", ".")
    
#     expression = split_expression(expression);


#     for i in expression:
#       print(i)
#       if "C" in i:
#         result = nCr(current);
#         current = format_number(str(result))
#       elif "P" in i:
#         result = nPr(i);
#         i = format_number(str(result))
#       elif "ln" in i:
#         result = fnLn(i);
#         i = format_number(str(result))
#       elif "log" in i:
#         result = fnLog10(i);
#         i = format_number(str(result))

#     # print(expression)

#     result = eval(expression)
#     expression = ""
#     current = format_number(str(result))
#     return True
#   except ZeroDivisionError:
#     expression = ""
#     current = "Div/0"
#     return False
#   except:
#     expression = ""
#     current = "Erro"
#     return False

def eval_expression():
  global expression, current
  print(current)
  try:
    if current:
      expression = current
    
    tokens = split_expression(expression)
    new_tokens = []
    for i in tokens:
      #  nCr
      if re.fullmatch(r'\d+C\d+', i):
        result = nCr(i)
        new_tokens.append(str(result))
    # nPr
      elif re.fullmatch(r'\d+P\d+', i):
        result = nPr(i)
        new_tokens.append(str(result))
      # ln
      elif "ln" in i:
        result = fnLn(i)
        new_tokens.append(str(result))
      #  log 10
      elif "log" in i:
        result = fnLog10(i)
        new_tokens.append(str(result))
      elif "^" in i:
        n, k = i.split("^")
        result = float(n)**float(k)
        print(result)
        new_tokens.append(str(result))
      elif "Pol(" in i:
        result = Pol(i)
        new_tokens.append(str(result))
      elif "Rec(" in i:
        result = Rec(i)
        new_tokens.append(str(result))
      else:
      # operação normal
        new_tokens.append(i.replace("×", "*").replace("÷", "/").replace("−", "-"))
    
    # Junta os tokens em uma string para o eval
    expr_str = "".join(new_tokens)
    expr_str = expr_str.replace(",", ".")
    print(expr_str.replace(",", "."))
    result = eval(expr_str)
    print(result)
    expression = ""
    if re.fullmatch(r'.*([\+-xX*÷]\s*\d*\/\d*).|.(\d*\/\d*\s*[+\-xX*÷]).*', current.replace(" ", "")) and result != 1 :
    # if re.fullmatch(r'[-?\d+/\d+]?\s*[+\-xX*÷]\s*[-?\d+/\d+]?', current.replace(" ", "")):
      current = Abc(float(result))
    else:
      current = format_number(str(result))
    return True
  except ZeroDivisionError:
    expression = ""
    current = "Div/0"
    return False
  except Exception as e:
    print("Exception: ", e)
    expression = ""
    current = "Erro"
    return False
  
def to_engineering(x: float) -> str:
  """Converte número para notação de engenharia (expoente múltiplo de 3)."""
  if x == 0:
    return "0"
  exp = int(math.floor(math.log10(abs(x)) / 3) * 3)  # múltiplo de 3
  mantissa = x / (10 ** exp)
  return f"{mantissa}×10^{exp}"

def click(btn):
  global current, expression, memory, decimal_allowed, shift, alpha

  # States

  if btn == "SHIFT":
    shift = True
    return

  if btn == "ALPHA":
    alpha = True
    return

  # Cientific calculator

  if btn == "ENG":
    try:
      val = float(current.replace(",", ".")) if current else 0.0

      if shift:
        # SHIFT + ENG → volta para decimal formatado
        current = format_number(str(val))
        shift = False  # reseta o estado de shift após usar
      else:
        # ENG → notação de engenharia
        current = ENG(val)
    except Exception:
        current = "Erro"

    update_display()
    return
  
  if btn == "nCr":
    try:
      # O usuário precisa passar os valores separando por virgula
      current+="C";
      print(current)

    except Exception:
        current = "Erro"

    update_display()
    return
  
  if btn == "Pol(":
    try:
      if shift:
        # SHIFT -> Pol -> Rec(r,θ) -> retorna x
        current+="Rec("
        shift = False
      else:
        current+="Pol("
      # Pol(x,y) → retorna distância (raiz quadrada da soma dos quadrados)
      # if "," not in current:
      #   current = "Erro"

    except Exception:
      current = "Erro"

    update_display()
    return
  

  if btn == "Ab/c":
    try:
      # Converte o current em float
      if shift:
        # Shift + D/c → número misto
        if re.fullmatch(r'-?\d+([.,]\d*)?', current):
          current = Dc(float(current.replace(",", ".")))

        shift = False  # reseta shift após uso
      else:
        # Ab/c normal → fração imprópria
        # if re.fullmatch(r'-?\d+/\d+', current):
        #   current = eval(current)
        # elif re.fullmatch(r'-?\d+(?:[.,]\d+)?', current):
        #   print("Não sei")
        #   current = Abc(current)
        # else: 
        #   current += "/"
          if re.fullmatch(r'-?\d+/\d+', current):
            print("fraction")
            current = str(eval(current))
          # Se é decimal, transforma em fração
          elif re.fullmatch(r'-?\d+[.,]\d+', current):
            print("decimal")
            current = Abc(float(current.replace(",", ".")))
          # Se não tem barra, adiciona uma
          else:
            print("nothing")
            current += "/"

    except Exception as e:
      print("Abc erro: ", e)
      current = "Erro"

    update_display()
    return
  
  if btn == "ln":
    try:
      if shift:
        # SHIFT + ln → e^x
        val = float(current.replace(",", ".")) if current else 0.0
        current = format_number(str(math.e ** val))
        shift = False

      elif alpha:
        # ALPHA + ln → constante e
        expression += str(math.e)
        current = ""
        display_var.set(expression.replace(str(math.e), "e"))  # mostra "e" no display
        alpha = False

      else:
        # ln(x)
        current+="ln ";

    except Exception:
      current = "Erro"

    update_display()
    return

  if btn == "log":
    try:
      if shift:
        # SHIFT + log → 10^x
        val = float(current.replace(",", ".")) if current else 0.0
        current = format_number(str(10 ** val))
        shift = False

      elif alpha:
        # ALPHA + log → constante π (opcional, como nas Casio)
        expression += str(math.pi)
        current = ""
        display_var.set(expression.replace(str(math.pi), "π"))
        alpha = False

      else:
        current+="log ";

    except Exception:
      current = "Erro"

    update_display()
    return

  # Standard calculator

  if btn == "CE":
    current = ""
    expression = ""
    decimal_allowed = True
    update_display()
    return
  
  if btn == "AC":
    current = ""
    expression = ""
    decimal_allowed = True
    update_display()
    return

  if btn == "C":
    current = ""
    decimal_allowed = True
    update_display()
    return

  if btn == "⌫":
    current = current[:-1]
    if "," not in current:
      decimal_allowed = True
    update_display()
    return
  
  if btn == "x²":
    try:
      val = float(current.replace(",", "."))
      current = format_number(str(val ** 2))
    except:
      current = "Erro"
    update_display()
    return

  if btn == "²√x":
    try:
      val = float(current.replace(",", "."))
      current = format_number(str(sqrt(val)))
    except:
      current = "Erro"
    update_display()
    return

  if btn == "¹/x":
    try:
      val = float(current.replace(",", "."))
      if val == 0:
        current = "Div/0"
      else:
        current = format_number(str(1 / val))
    except:
      current = "Erro"
    update_display()
    return

  # if btn in ["MC", "MR", "MS", "M+", "M-"]:
  #   try:
  #     val = float(current.replace(",", ".")) if current else 0
  #   except:
  #     val = 0
  #   if btn == "MC":
  #     memory = 0
  #   elif btn == "MR":
  #     current = format_number(str(memory))
  #   elif btn == "MS":
  #     memory = val
  #   elif btn == "M+":
  #     memory += val
  #   elif btn == "M-":
  #     memory -= val
  #   update_display()
  #   return
  if btn == ")":
    current+=")"
    update_display()
    return

  if btn ==  "=":
    decimal_allowed = "," not in current
      # nCr normal -> combinação
    eval_expression()
    update_display()
    return

  if btn in ["+", "-", "×", "÷"]:
    if not current and not expression:
      return
    if current:
      current += " "+btn+" "
      expression += current.replace(",", ".")
    else:
      expression = expression.rstrip("+-*/") # rstrip remove os espaços em branco
    # resolve antes de adicionar novo operador
    # try:
    #   result = str(eval(expression))
    #   expression = result + {"+": "+", "−": "-", "×": "*", "÷": "/"}[btn]
    #   current = ""
    #   decimal_allowed = True
    # except ZeroDivisionError:
    #   current = "Div/0"
    #   expression = ""
    # except:
    #   current = "Erro"
    #   expression = ""
    update_display()
    return

  if btn in [",", "."]:
    if not decimal_allowed:
      return
    if current == "":
      current = "0,"
    elif "," not in current:
      current += ","
    decimal_allowed = False
    update_display()
    return

  if btn.isdigit():
    current += btn
    update_display()
    return

# Suporte ao teclado
def keypress(event):
  key = event.char
  key_map = {
    "\r": "=",  # Enter
    "\x08": "⌫",  # Backspace
    ",": ",",
    ".": ",",
    "+": "+",
    "-": "−",
    "*": "×",
    "/": "÷"
  }
  if key in "0123456789":
    click(key)
  elif key in key_map:
    click(key_map[key])

def press():
  global cientific
  cientific = not cientific  # True/False

  # Delete all frame buttons
  for widget in buttons_frame.winfo_children():
    widget.destroy()

  # Define buttons value with the state
  if cientific:
    buttons = [
      ["SHIFT", "ALPHA", "REPLAY", "MODE", "ON"],
      ["x-¹", "nCr", "Pol(", "x³"],
      ["Ab/c", "√", "x²", "Λ", "log", "ln"],
      ["(-)", "., ,,", "hyp", "sin", "cos", "tan"],
      ["RCL", "ENG", "(", ")", ",", "M+"],
      ["7", "8", "9", "⌫", "AC"],
      ["4", "5", "6", "×", "÷"],
      ["1", "2", "3", "+", "-"],
      ["0", ",", "EXP", "Ans", "="]
    ]
  else:
    buttons = [
      ["%", "CE", "C", "⌫"],
      ["¹/x", "x²", "²√x", "÷"],
      ["7", "8", "9", "×"],
      ["4", "5", "6", "−"],
      ["1", "2", "3", "+"],
      ["0", ",", "="]
    ]

  # Do the buttons
  for row in buttons:
    row_frame = tk.Frame(buttons_frame, bg=bg_color)
    row_frame.pack(expand=True, fill="both")
    for btn in row:
      tk.Button(
        row_frame,
        text=btn,
        bg=equal_color if btn == "=" else btn_color,
        fg="black" if btn == "=" else text_color,
        font=("Segoe UI", 12),
        bd=0,
        relief="flat",
        highlightthickness=0,
        activebackground=accent_color,
        activeforeground=text_color,
        width=14 if btn == "=" else 5,
        height=2 if cientific == False else 1,
        command=lambda b=btn: click(b)
      ).pack(side="left", expand=True, fill="both", padx=1, pady=1)

# Interface
root = tk.Tk()
root.title("Calculadora")
root.configure(bg=bg_color)
root.geometry("320x480")
root.resizable(False, False)

# Display
change_mode = tk.Button(root, text="Mode", command=press)
change_mode.pack(fill="x")

display_var = tk.StringVar(value="0")
display = tk.Label(root, textvariable=display_var, anchor="e", bg=bg_color, fg=text_color, font=("Segoe UI", 28), padx=10)
display.pack(fill="both", ipady=20)

# Buttons
buttons_frame = tk.Frame(root, bg=bg_color)
buttons_frame.pack(expand=True, fill="both")

# Start buttons on normal layout
press()

root.bind("<Key>", keypress)
root.mainloop()