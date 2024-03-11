import os
import math

os.system('cls')
# Entrar com as notas da PR 1 e PR2 e imprimir a média final: media truncada, arredondada.

n1 = float(input("Favor informar o valor da primeira nota: "))
n2 = float(input("Favor informar o valor da segunda nota: "))

media = ((n1 + n2) / 2)
mediaArred = round(media, 2)
mediaTru = math.trunc(media)

print("\nMédia Arredondada: ", mediaArred, "\nMédia Trucanda: ", mediaTru)

input("\n\nPressione o \"enter\" para encerrar...")
