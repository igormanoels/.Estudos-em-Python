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
    'place' - Ajusta o texto conforme coordenadas absolutas em pixels
'''

msg_01 = Label(tela, width=10, height=2, text="Nome: ", font="Arial 15 bold", fg="white", bg="#231123")
msg_01.place(x=10, y=10)

resp_01 = Label(tela, width=10, height=2, text="Igor Manoel ", font="Arial 15", fg="white", bg="#231123")
resp_01.place(x=150, y=10)

msg_02 = Label(tela, width=10, height=2, text="Idade: ", font="Arial 15 bold", fg="blue")
msg_02.place(x=10, y=80)

msg_03 = Label(tela, width=10, height=2, text="Sexo: ", font="Arial 15 bold", fg="purple")
msg_03.place(x=10, y=150)


tela.mainloop()
