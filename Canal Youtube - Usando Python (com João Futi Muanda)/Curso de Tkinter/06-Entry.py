from tkinter import *
# Cores
dourado = "#C1AE7C"


def exibir():
    usuario = nome.get()
    anos = idade.get()
    nomeS["text"] = usuario
    idadeS["text"] = anos

    nome.delete(0, END)
    idade.delete(0, END)


# Configurações da tela
tela = Tk()
tela.title("Entrada de Dados")
tela.geometry("600x200")
tela.config(background=dourado)
tela.iconphoto(False, PhotoImage(file="imagens/logo01.png"))

# Entrada de Dados
nomel = Label(tela, width=15, font="Arial 12", text="Digite seu nome: ", anchor=W)
# 'anchor' faz o posicionamento usando North, South, East, West
nomel.grid(row=0, column=0, pady=10)
nome = Entry(tela, width=20, font="Arial 12")
nome.grid(row=0, column=1, pady=10)

idadel = Label(tela, width=15, font="Arial 12", text="Digite sua idade", anchor=W)
idadel.grid(row=1, column=0, pady=10)
idade = Entry(tela, width=20, font="Arial 12")
idade.grid(row=1, column=1, pady=10)


# Saída de Dados
nomeS = Label(tela, width=20, font="Arial 12", text=" ")
nomeS.grid(row=3, column=0, padx=10, pady=10)

idadeS = Label(tela, width=20, font="Arial 12", text=" ")
idadeS.grid(row=3, column=2, padx=10, pady=10)

# Acao
botao = Button(tela, command=exibir, width=15, height=2, text="clique aqui!")
botao.grid(row=2, column=1, padx=10, pady=10)


tela.mainloop()
