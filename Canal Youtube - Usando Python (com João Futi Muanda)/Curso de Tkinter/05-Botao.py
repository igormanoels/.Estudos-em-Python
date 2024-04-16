from tkinter import *

tela = Tk()
tela.title("Trabalhando com o Botão")
tela.geometry("600x450")
tela.config(background="#558C8C")
tela.iconphoto(False, PhotoImage(file="imagens/logo03.png"))

global contador
contador = 0
def executar():
    global contador

    texto01 = "Numero par"
    texto02 = "Numero impar"
    contador += 1

    if contador % 2 == 0:
        resultado = str(contador) + " " + texto01
        msg["fg"] = "blue"
    else:
        resultado = str(contador) + " " + texto02
        msg["fg"] = "red"
    msg["text"] = resultado


'''
    width=10                ----> Largura
    height=2                ----> Altura
    text="Clique em mim"    ----> Texto
    font="Arial"            ----> Fonte
    relief="flat"           ----> Modelo do botão
    bg="#EFF7FF"            ----> Cor de Fundo
    fg="#82204A"            ----> Cor da Fonte
    
    TIPOS DE BOTÃO
    flat, groove, solid, raised, sunken, ridge
'''
botao = Button(tela, command=executar, width=15, height=2, text="Clique em mim",
font="Arial", relief="ridge", bg="#EFF7FF", fg="#82204A")
botao.grid(row=1, column=1, padx=10, pady=10)

msg = Label(tela, width=25, height=4, text="Quantidades de Clique",
font="Arial 20", relief="ridge", bg="#EFF7FF", fg="#82204A")
msg.grid(row=2, column=1, padx=10, pady=10)

tela.mainloop()
