from math import factorial, sqrt, cos, radians, log10, e

import math

# States
shift, alpha = False, False

def ativar_shift():
    """Ativa o modo SHIFT e desativa ALPHA."""
    global shift, alpha
    shift = True
    alpha = False

def ativar_alpha():
    """Ativa o modo ALPHA e desativa SHIFT."""
    global shift, alpha
    alpha = True
    shift = False
