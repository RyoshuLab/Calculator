# =======================================
#   CALCULADORA COM INTERFACE - MODELO
# =======================================
# Como usar:
# 1. Rode o programa e teste a calculadora.
# 2. Troque tudo que tiver o aviso "TROQUE AQUI".
# 3. Cores podem ser em ingles ("red", "blue")
#    ou em codigo ("#ff0000").
# =======================================

import tkinter as tk  # biblioteca que cria janelas e botoes


# -------- PARTE 1: APARENCIA --------
# TROQUE AQUI: o titulo e as cores da sua calculadora

titulo: "Calciladora do 2A"

cor_fundo = "#1e1e2e"  # fundo da janela
cor_visor = "#2e2e3e"  # fundo do visor
cor_texto = "white"    # cor das letras
cor_numeros = "#44475a"  # botoes de numeros
cor_operacoes = "#ff9f43"  # botoes + - × e ÷
cor_igual = "#2ecc71"  # botao =
cor_limpar = "#e74c3c"  # botoes C e apagar

fonte = ("Arial", 20)


# ---------- PARTE 2: O QUE CADA BOTAO FAZ -----------

# Coloca o numero ou sinal clicando no visor
def clicar(valor):
  visor.insert(tk.END, valor)

# Limpa tudo (botao C)
def limpar():
  visor.delete(0, tk.END)

# Apaga so o ultimo numero (botao 
