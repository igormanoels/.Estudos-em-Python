from tkinter import *

# Colores
vinho = "#231123"

tela = Tk()
tela.title("Tela Principal")
tela.geometry("500x500")
tela.config(background="#E8DB7D")
tela.iconphoto(False, PhotoImage(file="imagens/logo02.png"))
tela.resizable(width=False, height=False)

'''
    'grid' - Ajusta os texto conforme o coordenada em formato de tabela
'''
msg_01 = Label (tela, width=10, height=2, text="Nome: ", font=("Arial 15 bold"), fg="white", bg="#231123")
msg_01.grid(row=0, column=0, pady=10) #Dimensiona as posições

msg_02 = Label (tela, width=10, height=2, text="Idade: ", font="Arial 15 bold", fg="blue")
msg_02.grid(row=1, column=0, pady=10) #Dimensiona as posições

msg_03 = Label (tela, width=10, height=2, text="Sexo: ", font="Arial 15 bold", fg="purple")
msg_03.grid(row=2, column=1, pady=10) #Dimensiona as posições

'''
    'place' - Ajusta o texto conforme coordenadas absolutas em pixels
'''

'''
    'pack' - coloca os widgets em um dos quatro lados da tela
'''


tela.mainloop()
