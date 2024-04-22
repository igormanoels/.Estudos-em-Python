from tkinter import *
import time

# Paleta de core
preto = "#000000"
azul = "#14213D"
amarelo = "#FCA311"
cinza = "#E5E5E5"
branco = "#FFFFFF"

# Variaveis Globais
global tempo
global rodar
global contador


tempo = "00:00:00"
rodar = False
contador = 5


def cronometro():
    global tempo
    global contador

    if rodar:
        # Antes de Iniciar
        if contador > 0:
            inicio = "Começando em " + str(contador)
            display["fg"] = cinza
            display["text"] = inicio
            display["font"] = "HP 20"
        # Iniciando Cronometro
        else:
            display["font"] = "HP 40"
            display["text"] = tempo

            seg = 0
            temp = str(tempo)
            h, m, s = map(int, temp.split(":"))
            h = int(h)
            m = int(m)
            s = int(s)

            if s > 59:
                seg = 0
                m += 1

            if m > 59:
                seg = 0
                m = 0
                h += 1

            h = str(0)+str(h)
            m = str(0)+str(m)
            s = str(0)+str(s)
            temp = str(h[-2:]+":"+m[-2:]+":"+s[-2:])
            tempo = temp
            display["text"] = tempo
            seg += 1

    display.after(1000, cronometro)
    contador -= 1


def iniciar():
    global rodar
    rodar = True
    cronometro()


# Propriedades da Tela
tela = Tk()
tela.title('Cronometro')
tela.iconphoto(False, PhotoImage(file='icones/time.png'))
tela.geometry('480x200')
tela.resizable(width=False, height=False)
tela.config(background=azul)

# Botões
iniciar = Button(tela, command=iniciar, text="Iniciar", font="HP 16", bg=amarelo, fg=preto)
iniciar.place(x=50, y=15)

pausar = Button(tela, text="Pausar", font="HP 16", bg=amarelo, fg=preto)
pausar.place(x=200, y=15)

reiniciar = Button(tela, text="Reiniciar", font="HP 16", bg=amarelo, fg=preto)
reiniciar.place(x=360, y=15)

# Display
display = Label(tela, text=tempo, font="HP 40", bg=amarelo, fg=branco)
display.place(x=130, y=100)

tela.mainloop()
