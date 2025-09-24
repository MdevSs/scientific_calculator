# import functions.fnStranger.Lucas as batch1

# Replay
# Deve ter algumas variáveis criadas:

# Histórico para replay
historico = []  # cada item será (numero1, numero2, operacao, resultado)
indice_historico = -1  # começa no último item do histórico

# Para o cursor de edição
posicao_cursor = 0  
modo_cursor = False  

shift = False
alpha = False
# talvez útil manter último número digitado
lastNumber = "0"

# rounding helpers (optional, safe fallback)
round_mode = "norm"
round_digits = 2

def get_round_settings():
    return round_mode, round_digits

def set_round_mode(mode: str):
    global round_mode
    if mode in ("norm", "fix", "sci", "rnd"):
        round_mode = mode

def set_round_digits(n: int):
    global round_digits
    try:
        round_digits = max(0, int(n))
    except Exception:
        pass

# def toggle_shift():
#     global shift
#     print(f"Shift before: {shift}")
#     shift = batch1.toggle_shift(shift)
#     print(f"Shift: {shift}")

# def toggle_alpha():
#     global alpha
#     print(f"Alpha before: {alpha}")
#     alpha = batch1.toggle_alpha(alpha)
#     print(f"Alpha: {alpha}")