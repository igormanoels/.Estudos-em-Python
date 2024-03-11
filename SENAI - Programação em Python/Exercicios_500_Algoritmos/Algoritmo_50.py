import os
import math

os.system('cls')
# Entrar com a base e a altura de um retângulo e imprimir a seguinte saída: Perimetro, Area e Diagonal

base = float(input("Favor informar o valor da Base do triângulo: "))
altura = float(input("Favor informar o valor da Altura: "))

perimetro = ((altura + base) * 2)
area = base * altura
diagonal = math.sqrt((math.pow(base, 2) + (math.pow(altura, 2))))

print("\nPerimetro: ", perimetro, "\nÁrea: ", area, "\nDiagonal: ", diagonal)
