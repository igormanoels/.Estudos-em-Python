import math
import os

os.system('cls')
# Entrar com o raio de um cfrculo e imprimir a seguinte saída: perimetro, area:

raio = float(input("Favor informar o valor do raio de um círculo: "))

perimetro = (2 * math.pi * raio)
area = (math.pi * (math.pow(raio , 2)))

print("\nPerímetro: ", perimetro, "\nÁrea: ", area)
