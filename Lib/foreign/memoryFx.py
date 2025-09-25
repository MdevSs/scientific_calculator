import tkinter as tk
from tkinter import simpledialog, messagebox
from foreign import auxiliar as var
'''
Funções de memória: STO, RCL e gerenciamento de slots.
Coloque as duas funções em um botão.
O arquivo auxiliar.py também será necessário, pois ele contém o dicionário de slots e funções auxiliares.
Usar assim:
  from functions.fnNew import memoryFx as mem
  mem._sto(display, app)  # Para armazenar
  mem._rcl(display, app)  # Para recuperar
  Display é o campo de entrada (Entry) do tkinter
  app é a instância da classe App (main)
'''

def valid_slots():
    return var.valid_slots()

def _ask_slot(parent, title):
    prompt = "Escolha um slot de memória (ex: A, B, C, ...):"
    slot = simpledialog.askstring(title, prompt, parent=parent)
    if not slot:
        return None
    slot = slot.strip().upper()
    if not var.is_valid_slot(slot):
        messagebox.showerror("Slot inválido", f"Slot '{slot}' inválido.\nUse: {', '.join(var.valid_slots())}", parent=parent)
        return None
    return slot

def _sto(display, parent):
    slot = _ask_slot(parent, "STO (armazenar)")
    if not slot:
        return
    val = display.get()
    if parent.selecao.get() == "Normal":
        val = val.replace(",", ".")
    if var.set_memory(slot, val):
        messagebox.showinfo("STO", f"Valor armazenado em {slot}", parent=parent)
    else:
        messagebox.showerror("STO", f"Não foi possível armazenar em {slot}", parent=parent)

def _rcl(display, parent):
    slot = _ask_slot(parent, "RCL (recuperar)")
    if not slot:
        return
    val = var.get_memory(slot)
    if val is None:
        messagebox.showerror("Erro", f"Nenhum valor em {slot}", parent=parent)
        return
    if parent.selecao.get() == "Normal":
        val = val.replace(".", ",")
    current = display.get()
    if current == "0" or current == "":
        display.delete(0, tk.END)
        display.insert(0, val)
    else:
        try:
            display.insert(tk.INSERT, val)
        except Exception:
            display.insert(tk.END, val)