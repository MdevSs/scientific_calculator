# functions/degrees.py
"""
Aqui é a conversão de decimais para graus, minutos e segundos.
Funciona com números negativos e positivos.
Essa função está dentro da função formatDegree, tenha a certeza de importá-la para o arquivo que formatDegree estiver.
Usar assim:
  from functions.fnNew import degrees as deg
  deg.convertDecimal(value)
"""

import variables as var

degreeSign = "°"
minuteSign = "'"
secondSign = '"'

def convertDecimal(value):
  if isinstance(value, str):
    vnorm = value.strip().replace(",", ".")
  else:
    vnorm = str(value)

  try:
    num = float(vnorm)
  except Exception:
    raise ValueError(f"Valor inválido para conversão: {value!r}")

  sign = "-" if num < 0 else ""
  a = abs(num)
  degrees = int(a)
  rem_minutes = (a - degrees) * 60.0
  minutes = int(rem_minutes)
  seconds = (rem_minutes - minutes) * 60.0
  precision_seconds = 2
  seconds = round(seconds, precision_seconds)

  if seconds >= 60.0:
    seconds -= 60.0
    minutes += 1
  if minutes >= 60:
    minutes -= 60
    degrees += 1

  if float(seconds).is_integer():
    sec_str = str(int(round(seconds)))
  else:
    raw = f"{seconds:.{precision_seconds}f}"
    raw = raw.rstrip("0").rstrip(".")
    sec_str = raw

  formatted = f"{sign}{degrees}{degreeSign}{minutes}{minuteSign}{sec_str}{secondSign}"

  return formatted