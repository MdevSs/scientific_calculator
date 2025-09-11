# Não aceita letras;
# Sem divisão por 0;
# Não ter sinais seguidos "--";
# Ao iniciar com virgula, zero no início;
# C limpa a linha atual, a operação atual;
# CE limpa todo o cálculo;
# Resolver operação ao clicar igual ou outra operação;
# Só pode usar uma segunda virgula após o uso de um operador ou sinal de igual;
# Formatar com ponto números acima de mil.

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

def update_display():
  if current:
    display_var.set(current)
  elif expression:
    display_var.set(format_number(expression) if expression.replace(".", "").isdigit() else expression)
  else:
    display_var.set("0")

def eval_expression():
  global expression, current
  try:
    if current:
      expression += current.replace(",", ".")
    result = eval(expression)
    expression = ""
    current = format_number(str(result))
    return True
  except ZeroDivisionError:
    expression = ""
    current = "Div/0"
    return False
  except:
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
        current = to_engineering(val)
    except Exception:
        current = "Erro"

    update_display()
    return
  
  if btn == "nCr":
    try:
      # O usuário precisa passar os valores separando por virgula
      if "," not in current:
        current = "Erro"
      else:
        n_str, k_str = current.split(",")
        n, k = int(n_str), int(k_str)

        if shift:
          # SHIFT + nCr -> permutação (nPr)
          result = factorial(n) // factorial(n - k)
          shift = False  # reseta shift
        else:
          # nCr normal -> combinação
          result = factorial(n) // (factorial(k) * factorial(n - k))

        current = format_number(str(result))

    except Exception:
        current = "Erro"

    update_display()
    return
  
  if btn == "Pol(":
    try:
      if shift:
        # SHIFT -> Pol -> Rec(r,θ) -> retorna x
        if "," not in current:
          current = "Erro"
        else:
          r_str, ang_str = current.split(",")
          r, ang = float(r_str), float(ang_str)
          # x = r * cos(θ)   (em graus)
          result = r * math.cos(math.radians(ang))
          current = format_number(str(result))
          shift = False
      else:
        # Pol(x,y) → retorna distância (raiz quadrada da soma dos quadrados)
        if "," not in current:
          current = "Erro"
        else:
          x_str, y_str = current.split(",")
          x, y = float(x_str), float(y_str)
          result = math.sqrt(x**2 + y**2)
          current = format_number(str(result))

    except Exception:
      current = "Erro"

    update_display()
    return

  if btn == "Ab/c":
    try:
      # Converte o current em float
      val = float(current.replace(",", ".")) if current else 0.0
      from fractions import Fraction
      frac = Fraction(val).limit_denominator()

      if shift:
        # Shift + Ab/c → número misto
        numer, denom = frac.numerator, frac.denominator
        inteiro, resto = divmod(numer, denom)
        if inteiro == 0:
          current = f"{resto}/{denom}"
        elif resto == 0:
          current = str(inteiro)
        else:
          current = f"{inteiro} {resto}/{denom}"
        shift = False  # reseta shift após uso
      else:
        # Ab/c normal → fração imprópria
        current = f"{frac.numerator}/{frac.denominator}"

    except Exception:
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
        val = float(current.replace(",", ".")) if current else 0.0
        if val <= 0:
          current = "Erro"
        else:
          current = format_number(str(math.log(val)))  # log base e

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
        # log(x) = log base 10
        val = float(current.replace(",", ".")) if current else 0.0
        if val <= 0:
          current = "Erro"
        else:
          current = format_number(str(math.log10(val)))

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

  if btn == "=":
    eval_expression()
    decimal_allowed = "," not in current
    update_display()
    return

  if btn in ["+", "−", "×", "÷"]:
    if not current and not expression:
      return
    if current:
      expression += current.replace(",", ".")
    else:
      expression = expression.rstrip("+-*/") # rstrip remove os espaços em branco
    # resolve antes de adicionar novo operador
    try:
      result = str(eval(expression))
      expression = result + {"+": "+", "−": "-", "×": "*", "÷": "/"}[btn]
      current = ""
      decimal_allowed = True
    except ZeroDivisionError:
      current = "Div/0"
      expression = ""
    except:
      current = "Erro"
      expression = ""
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