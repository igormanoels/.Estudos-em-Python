from tkinter import *

# As cores podem ser atribuidas diretamente ou via variável
azul = "#EFF7FF"
vinho = "#82204A"
verde = "#558C8C"
amarelo = "#E8DB7D"

janela = Tk() #Objeto criado da janela do aplicativo
janela.title("Hello World") #Titulo que ficará contido na barra da janela
janela.geometry("500x350") #Dimensões das janelas

janela.config(background=vinho)
#Altera a cor de fundo da janela, também pode ser usado o comando bg="" tbm é aceitos valores em hexadecimal

janela.iconphoto(False, PhotoImage(file="imagens/logo01.png"))
#Altera o icone da janela, os arquivsos precisam estar no diretório da projeto

janela.resizable(width=False,height=False)
#Bloqueia o redimencionamento da tela, pode ser aplicado apenas a um atributo

janela.mainloop() # Garante que a janela permanecerá ativa depois que executada
