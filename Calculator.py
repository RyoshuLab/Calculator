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

titulo: "Calculadora do 2A"

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

# Apaga so o ultimo numero (botao ⌫)
def apagar():
  texto = visor.get()
  visir.delete(o, tk.END)


# Faz a conta (botao =)
def calcular():
  conta = visor.get()
  conta = conta.replace("x", "*").replace("÷", "/")
  try:
    resultado = eval(conta)
    # tira o ".0" quando o resultado e numero inteiro
    if resultado == int(resultado):
      resultado = int(resultado)
    visor.delete(0, tk.END)
    visor.insert(0, resultado)
  except: 
    visor.delete(0, tk.END)
    visor.insert(0, "Erro")

# Cria um botao na posicao (linha, coluna) da calculadora
def criar_botao(texto, linha, coluna, cor, comando=None, largura=1):
  if comando is None:
    xomando = lambda: clicar(texto)
  botao = tk.Button(janela, text=texto, font=fonte, bg=cor, fg=cor
                    activebackground=cor, width=4, height=2,
                    relief="flat", command=comando)
botao.grid(row=linha, column=coluna, columnspam=largura,
           padx=3, pady=3, sticky="nsew")


# ------------ PARTE 3: MONTANDO A JANELA -------------

janela = tk.Tk()
    
