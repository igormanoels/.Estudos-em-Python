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
# Define as propriedade do label
msg_01.grid(row=0, column=0, padx=5, pady=5)
#Dimensiona as posições

resp_01 = Label (tela, width=10, height=2, text="Igor Manoel ", font=("Arial 15 bold"), fg="white", bg="#231123")
resp_01.grid(row=0, column=1)

msg_02 = Label (tela, width=10, height=2, text="Idade: ", font="Arial 15 bold", fg="blue")
msg_02.grid(row=1, column=0)

resp_02 = Label (tela, width=10, height=2, text="29 anos", font=("Arial 15 bold"), fg="blue")
resp_02.grid(row=1, column=1)

msg_03 = Label (tela, width=10, height=2, text="Sexo: ", font="Arial 15 bold", fg="purple")
msg_03.grid(row=2, column=1, padx=5, pady=5)



tela.mainloop()
