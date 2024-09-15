import os
from datetime import datetime
os.system('cls')

'''
Receba a hora de início e de final de um jogo (HH,MM)
sabendo que o tempo máximo é de 24 horas e pode começar num dia e terminar noutro.
'''

horaInicial = input("Informe a hora inicial do jogo, no formato HH:MM: ")
horaFinal = input("Informe a hora final do jogo, no formato HH:MM: ")

inicio = datetime.strptime(horaInicial, "%H:%M")
fim = datetime.strptime(horaFinal, "%H:%M")

if inicio < fim:
    diferenca = inicio - fim
else:
    diferenca = fim - inicio

print("Diferença:", diferenca)
